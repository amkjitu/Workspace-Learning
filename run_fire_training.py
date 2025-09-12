#!/usr/bin/env python3
"""
Simple wrapper script for fire detection training using configuration file.
This makes it easier to run training without remembering all command line arguments.
"""

import subprocess
import sys
from fire_detection_config import *

def run_training():
    """Run training with configuration from fire_detection_config.py"""
    
    cmd = [
        sys.executable, "copy_of_fire_train_amk.py",
        "--roboflow-api-key", ROBOFLOW_API_KEY,
        "--workspace", WORKSPACE,
        "--project", PROJECT,
        "--dataset-version", str(DATASET_VERSION),
        "--model-name", MODEL_NAME,
        "--epochs", str(EPOCHS),
        "--batch-size", str(BATCH_SIZE),
        "--image-size", str(IMAGE_SIZE),
        "--save-period", str(SAVE_PERIOD),
        "--drive-root", DRIVE_ROOT
    ]
    
    # Add resume flag if enabled
    if RESUME_TRAINING and not FORCE_RESTART:
        cmd.append("--resume")
    elif FORCE_RESTART:
        cmd.append("--force-restart")
    
    print("Starting fire detection training with configuration:")
    print(f"Model: {MODEL_NAME}")
    print(f"Epochs: {EPOCHS}")
    print(f"Batch size: {BATCH_SIZE}")
    print(f"Resume: {RESUME_TRAINING}")
    print(f"Force restart: {FORCE_RESTART}")
    print("-" * 50)
    
    # Run the training script
    try:
        subprocess.run(cmd, check=True)
        print("Training completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Training failed with exit code {e.returncode}")
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        print("\nTraining interrupted by user")
        sys.exit(1)

if __name__ == "__main__":
    run_training()