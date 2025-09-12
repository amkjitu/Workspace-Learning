#!/usr/bin/env python3
"""
Fire and Smoke Detection Training Script with Google Drive Integration
Author: AMK
Description: YOLOv8-based fire and smoke detection model training with Google Drive support
             for resuming training sessions in Google Colab environment.
"""

import os
import sys
import argparse
import json
import pickle
import time
import shutil
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# Core ML libraries
import torch
import yaml
from ultralytics import YOLO
import numpy as np
from roboflow import Roboflow

# Google Drive integration
try:
    from google.colab import drive
    from google.colab import auth
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
    from google.oauth2.credentials import Credentials
    COLAB_AVAILABLE = True
except ImportError:
    COLAB_AVAILABLE = False
    print("Warning: Google Colab libraries not available. Some features may be limited.")

# Progress tracking
from tqdm import tqdm
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('training.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class GoogleDriveManager:
    """Manages Google Drive operations for dataset and model persistence."""
    
    def __init__(self, drive_root: str = "/content/drive"):
        self.drive_root = Path(drive_root)
        self.project_folder = self.drive_root / "MyDrive" / "fire_detection_project"
        self.datasets_folder = self.project_folder / "datasets"
        self.checkpoints_folder = self.project_folder / "checkpoints"
        self.models_folder = self.project_folder / "models"
        self.logs_folder = self.project_folder / "logs"
        
        self.service = None
        self._setup_drive()
    
    def _setup_drive(self):
        """Setup Google Drive access."""
        if not COLAB_AVAILABLE:
            logger.warning("Google Colab not available. Using local filesystem.")
            # Create local directories
            for folder in [self.project_folder, self.datasets_folder, 
                          self.checkpoints_folder, self.models_folder, self.logs_folder]:
                folder.mkdir(parents=True, exist_ok=True)
            return
            
        try:
            # Mount Google Drive
            drive.mount(str(self.drive_root))
            
            # Authenticate and build service
            auth.authenticate_user()
            creds = Credentials.from_authorized_user_info({
                'token': open('/content/drive/MyDrive/token.json').read() if 
                os.path.exists('/content/drive/MyDrive/token.json') else None
            })
            self.service = build('drive', 'v3', credentials=creds)
            
            # Create project directories
            for folder in [self.project_folder, self.datasets_folder, 
                          self.checkpoints_folder, self.models_folder, self.logs_folder]:
                folder.mkdir(parents=True, exist_ok=True)
                
            logger.info(f"Google Drive mounted successfully at {self.drive_root}")
            
        except Exception as e:
            logger.error(f"Failed to setup Google Drive: {e}")
            # Fallback to local directories
            for folder in [self.project_folder, self.datasets_folder, 
                          self.checkpoints_folder, self.models_folder, self.logs_folder]:
                folder.mkdir(parents=True, exist_ok=True)
    
    def save_checkpoint(self, checkpoint_data: Dict[Any, Any], epoch: int):
        """Save training checkpoint to Google Drive."""
        checkpoint_path = self.checkpoints_folder / f"checkpoint_epoch_{epoch}.pkl"
        
        try:
            with open(checkpoint_path, 'wb') as f:
                pickle.dump(checkpoint_data, f)
            logger.info(f"Checkpoint saved: {checkpoint_path}")
            
            # Save latest checkpoint reference
            latest_path = self.checkpoints_folder / "latest_checkpoint.txt"
            with open(latest_path, 'w') as f:
                f.write(str(checkpoint_path))
                
        except Exception as e:
            logger.error(f"Failed to save checkpoint: {e}")
    
    def load_latest_checkpoint(self) -> Optional[Tuple[Dict[Any, Any], int]]:
        """Load the latest checkpoint from Google Drive."""
        latest_path = self.checkpoints_folder / "latest_checkpoint.txt"
        
        if not latest_path.exists():
            logger.info("No previous checkpoint found.")
            return None
            
        try:
            with open(latest_path, 'r') as f:
                checkpoint_path = Path(f.read().strip())
                
            if not checkpoint_path.exists():
                logger.warning(f"Checkpoint file not found: {checkpoint_path}")
                return None
                
            with open(checkpoint_path, 'rb') as f:
                checkpoint_data = pickle.load(f)
                
            epoch = int(checkpoint_path.stem.split('_')[-1])
            logger.info(f"Loaded checkpoint from epoch {epoch}")
            return checkpoint_data, epoch
            
        except Exception as e:
            logger.error(f"Failed to load checkpoint: {e}")
            return None
    
    def save_model(self, model_path: Path, epoch: int, metrics: Dict[str, float]):
        """Save trained model to Google Drive in multiple formats."""
        try:
            # Create model directory for this training session
            timestamp = int(time.time())
            session_folder = self.models_folder / f"session_{timestamp}"
            session_folder.mkdir(parents=True, exist_ok=True)
            
            # Copy model files
            if model_path.exists():
                dest_path = session_folder / f"best_model_epoch_{epoch}.pt"
                shutil.copy2(model_path, dest_path)
                logger.info(f"Model saved: {dest_path}")
                
                # Save metrics
                metrics_path = session_folder / "metrics.json"
                with open(metrics_path, 'w') as f:
                    json.dump(metrics, f, indent=2)
                
                # Export in different formats if possible
                try:
                    model = YOLO(str(dest_path))
                    
                    # Export to ONNX
                    onnx_path = session_folder / f"model_epoch_{epoch}.onnx"
                    model.export(format="onnx", imgsz=640)
                    
                    # Export to TensorRT (if available)
                    try:
                        trt_path = session_folder / f"model_epoch_{epoch}.engine"
                        model.export(format="engine", imgsz=640)
                    except:
                        logger.info("TensorRT export not available")
                        
                except Exception as e:
                    logger.warning(f"Model export failed: {e}")
                    
        except Exception as e:
            logger.error(f"Failed to save model: {e}")
    
    def cache_dataset(self, dataset_path: Path, dataset_name: str) -> Path:
        """Cache dataset to Google Drive to avoid re-downloading."""
        cached_path = self.datasets_folder / dataset_name
        
        if cached_path.exists():
            logger.info(f"Using cached dataset: {cached_path}")
            return cached_path
            
        try:
            logger.info(f"Caching dataset to: {cached_path}")
            shutil.copytree(dataset_path, cached_path)
            return cached_path
        except Exception as e:
            logger.error(f"Failed to cache dataset: {e}")
            return dataset_path


class FireDetectionTrainer:
    """Main trainer class for fire and smoke detection."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.drive_manager = GoogleDriveManager()
        self.model = None
        self.dataset_path = None
        self.start_epoch = 0
        self.training_state = {}
        
    def setup_dataset(self) -> Path:
        """Setup dataset with caching support."""
        logger.info("Setting up dataset...")
        
        # Check if dataset is already cached
        dataset_name = f"fire_smoke_dataset_v{self.config['dataset_version']}"
        cached_path = self.drive_manager.datasets_folder / dataset_name
        
        if cached_path.exists() and (cached_path / "data.yaml").exists():
            logger.info(f"Using cached dataset: {cached_path}")
            return cached_path
            
        # Download dataset using Roboflow
        logger.info("Downloading dataset from Roboflow...")
        rf = Roboflow(api_key=self.config['roboflow_api_key'])
        project = rf.workspace(self.config['workspace']).project(self.config['project'])
        version = project.version(self.config['dataset_version'])
        
        # Download to temporary location
        temp_dataset = version.download("yolov8")
        temp_path = Path(temp_dataset.location)
        
        # Cache to Google Drive
        cached_path = self.drive_manager.cache_dataset(temp_path, dataset_name)
        
        return cached_path
    
    def setup_model(self):
        """Setup YOLO model."""
        model_name = self.config.get('model_name', 'yolov8s.pt')
        self.model = YOLO(model_name)
        logger.info(f"Initialized model: {model_name}")
    
    def save_training_state(self, epoch: int, metrics: Dict[str, float]):
        """Save current training state."""
        state = {
            'epoch': epoch,
            'config': self.config,
            'metrics': metrics,
            'timestamp': time.time(),
            'model_state': None  # Model weights saved separately
        }
        
        self.drive_manager.save_checkpoint(state, epoch)
    
    def load_training_state(self) -> bool:
        """Load previous training state if available."""
        if not self.config.get('resume', False):
            return False
            
        checkpoint = self.drive_manager.load_latest_checkpoint()
        if checkpoint is None:
            return False
            
        state, epoch = checkpoint
        self.start_epoch = epoch + 1
        self.training_state = state
        
        logger.info(f"Resuming training from epoch {self.start_epoch}")
        return True
    
    def train(self):
        """Main training loop with checkpoint support."""
        logger.info("Starting training...")
        
        # Setup dataset and model
        self.dataset_path = self.setup_dataset()
        self.setup_model()
        
        # Try to resume from checkpoint
        resumed = self.load_training_state()
        
        # Training parameters
        epochs = self.config.get('epochs', 100)
        imgsz = self.config.get('image_size', 640)
        batch_size = self.config.get('batch_size', 16)
        
        # Data yaml path
        data_yaml = self.dataset_path / "data.yaml"
        
        try:
            # Start training
            results = self.model.train(
                data=str(data_yaml),
                epochs=epochs,
                imgsz=imgsz,
                batch=batch_size,
                project=str(self.drive_manager.project_folder),
                name=f"training_session_{int(time.time())}",
                save=True,
                save_period=self.config.get('save_period', 10),  # Save every N epochs
                resume=resumed
            )
            
            # Save final model and metrics
            if hasattr(results, 'best'):
                metrics = {
                    'mAP50': float(results.box.map50) if hasattr(results.box, 'map50') else 0.0,
                    'mAP50-95': float(results.box.map) if hasattr(results.box, 'map') else 0.0,
                    'precision': float(results.box.p.mean()) if hasattr(results.box, 'p') else 0.0,
                    'recall': float(results.box.r.mean()) if hasattr(results.box, 'r') else 0.0,
                }
                
                best_model_path = Path(self.model.trainer.best)
                self.drive_manager.save_model(best_model_path, epochs, metrics)
                
            logger.info("Training completed successfully!")
            return results
            
        except KeyboardInterrupt:
            logger.info("Training interrupted. Saving checkpoint...")
            self.save_training_state(self.model.trainer.epoch, {})
            raise
        except Exception as e:
            logger.error(f"Training failed: {e}")
            raise


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Fire Detection Training Script")
    
    # Dataset parameters
    parser.add_argument('--roboflow-api-key', type=str, required=True,
                       help='Roboflow API key')
    parser.add_argument('--workspace', type=str, default='ai-training-course-rximv',
                       help='Roboflow workspace name')
    parser.add_argument('--project', type=str, default='fire-and-smoke-detection-vzqpf',
                       help='Roboflow project name')
    parser.add_argument('--dataset-version', type=int, default=3,
                       help='Dataset version to use')
    
    # Training parameters
    parser.add_argument('--model-name', type=str, default='yolov8s.pt',
                       help='YOLO model to use (yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.)')
    parser.add_argument('--epochs', type=int, default=100,
                       help='Number of training epochs')
    parser.add_argument('--batch-size', type=int, default=16,
                       help='Batch size for training')
    parser.add_argument('--image-size', type=int, default=640,
                       help='Image size for training')
    parser.add_argument('--save-period', type=int, default=10,
                       help='Save checkpoint every N epochs')
    
    # Resume parameters
    parser.add_argument('--resume', action='store_true',
                       help='Resume training from latest checkpoint')
    parser.add_argument('--force-restart', action='store_true',
                       help='Force restart training (ignore checkpoints)')
    
    # Drive parameters
    parser.add_argument('--drive-root', type=str, default='/content/drive',
                       help='Google Drive mount point')
    
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_arguments()
    
    # Create configuration dictionary
    config = {
        'roboflow_api_key': args.roboflow_api_key,
        'workspace': args.workspace,
        'project': args.project,
        'dataset_version': args.dataset_version,
        'model_name': args.model_name,
        'epochs': args.epochs,
        'batch_size': args.batch_size,
        'image_size': args.image_size,
        'save_period': args.save_period,
        'resume': args.resume and not args.force_restart,
        'drive_root': args.drive_root
    }
    
    logger.info("Fire Detection Training Script Started")
    logger.info(f"Configuration: {json.dumps(config, indent=2)}")
    
    try:
        trainer = FireDetectionTrainer(config)
        results = trainer.train()
        
        logger.info("Training completed successfully!")
        logger.info(f"Results: {results}")
        
    except KeyboardInterrupt:
        logger.info("Training interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Training failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()