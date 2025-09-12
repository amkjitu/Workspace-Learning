# Fire Detection Training with Google Drive Integration

## 🔥 Overview

This fire and smoke detection training script provides robust support for Google Colab's free tier limitations by integrating with Google Drive for persistent storage and checkpoint management. The script can automatically resume training after runtime disconnections, saving time and computational resources.

## ✨ Features

### 🚀 Core Features
- **YOLOv8-based** fire and smoke detection training
- **Google Drive integration** for persistent storage
- **Automatic resume** functionality after interruptions
- **Dataset caching** to avoid re-downloading
- **Multiple model export** formats (PyTorch, ONNX, TensorRT)
- **Comprehensive logging** and progress tracking

### 💾 Persistence Features
- Training state checkpoints saved every N epochs
- Dataset cached to Google Drive after first download
- Model weights and metrics automatically backed up
- Progress tracking with detailed logs

### 🔧 Configuration Options
- Command-line arguments for all parameters
- Configuration file support for easy customization
- Multiple YOLO model variants (nano to extra-large)
- Flexible batch sizes and training parameters

## 📦 Installation

1. **Install dependencies:**
```bash
pip install -r requirements_fire_detection.txt
```

2. **For Google Colab (recommended):**
```python
!pip install -r requirements_fire_detection.txt
```

## 🚀 Quick Start

### Basic Training (First Time)
```bash
python copy_of_fire_train_amk.py \
    --roboflow-api-key "your_api_key_here" \
    --epochs 100 \
    --batch-size 16 \
    --model-name yolov8s.pt
```

### Resume Training (After Interruption)
```bash
python copy_of_fire_train_amk.py \
    --roboflow-api-key "your_api_key_here" \
    --resume
```

### Using Configuration File
```bash
# Edit fire_detection_config.py with your settings
python run_fire_training.py
```

## 📋 Command Line Options

### Required Parameters
- `--roboflow-api-key`: Your Roboflow API key for dataset access

### Dataset Parameters
- `--workspace`: Roboflow workspace name (default: "ai-training-course-rximv")
- `--project`: Roboflow project name (default: "fire-and-smoke-detection-vzqpf")
- `--dataset-version`: Dataset version to use (default: 3)

### Training Parameters
- `--model-name`: YOLO model variant (default: "yolov8s.pt")
  - Options: `yolov8n.pt`, `yolov8s.pt`, `yolov8m.pt`, `yolov8l.pt`, `yolov8x.pt`
- `--epochs`: Number of training epochs (default: 100)
- `--batch-size`: Training batch size (default: 16)
- `--image-size`: Input image size (default: 640)
- `--save-period`: Checkpoint save frequency in epochs (default: 10)

### Resume Parameters
- `--resume`: Resume from latest checkpoint
- `--force-restart`: Ignore existing checkpoints and start fresh

### Storage Parameters
- `--drive-root`: Google Drive mount point (default: "/content/drive")

## 🗂️ File Structure

The script creates the following structure in Google Drive:

```
/content/drive/MyDrive/fire_detection_project/
├── datasets/
│   └── fire_smoke_dataset_v3/          # Cached dataset
│       ├── train/
│       ├── valid/
│       ├── test/
│       └── data.yaml
├── checkpoints/
│   ├── checkpoint_epoch_10.pkl         # Training state snapshots
│   ├── checkpoint_epoch_20.pkl
│   ├── ...
│   └── latest_checkpoint.txt           # Points to most recent checkpoint
├── models/
│   └── session_1234567890/             # Training session folder
│       ├── best_model_epoch_100.pt     # Best PyTorch model
│       ├── model_epoch_100.onnx        # ONNX export
│       ├── model_epoch_100.engine      # TensorRT export (if available)
│       └── metrics.json                # Training metrics
└── logs/
    └── training.log                    # Detailed training logs
```

## 🔄 Resume Training Workflow

1. **Training starts** → Checkpoints saved every N epochs to Google Drive
2. **Runtime disconnects** → All progress preserved in Google Drive
3. **Restart Colab** → Mount Google Drive
4. **Run with `--resume`** → Automatically loads latest checkpoint
5. **Training continues** → From exactly where it left off

## 🎯 Model Variants

Choose the right balance of speed vs accuracy:

| Model | Size | Speed | mAP | Use Case |
|-------|------|-------|-----|----------|
| yolov8n.pt | ~6MB | Fastest | Good | Mobile/Edge devices |
| yolov8s.pt | ~22MB | Fast | Better | **Recommended default** |
| yolov8m.pt | ~52MB | Medium | High | Balanced performance |
| yolov8l.pt | ~87MB | Slow | Higher | High accuracy needs |
| yolov8x.pt | ~136MB | Slowest | Highest | Maximum accuracy |

## 📊 Example Colab Workflow

```python
# 1. Install dependencies
!pip install -r requirements_fire_detection.txt

# 2. Start training (will cache dataset)
!python copy_of_fire_train_amk.py \
    --roboflow-api-key "KRl7MmkK5Na8s9ci4KzV" \
    --epochs 100 \
    --batch-size 16 \
    --model-name yolov8s.pt

# 3. If runtime disconnects, simply resume:
!python copy_of_fire_train_amk.py \
    --roboflow-api-key "KRl7MmkK5Na8s9ci4KzV" \
    --resume

# 4. Training continues from last checkpoint automatically!
```

## 🛠️ Troubleshooting

### Common Issues

**Google Drive not mounted:**
```bash
# In Colab, manually mount first:
from google.colab import drive
drive.mount('/content/drive')
```

**Out of memory errors:**
```bash
# Reduce batch size:
--batch-size 8

# Or use smaller model:
--model-name yolov8n.pt
```

**Dataset download fails:**
```bash
# Check API key and project settings
# Verify internet connection
# Try smaller dataset version
```

**Training very slow:**
```bash
# Use smaller model for faster training:
--model-name yolov8n.pt

# Reduce image size:
--image-size 416

# Smaller batch size:
--batch-size 8
```

### Performance Tips

1. **For fastest training:** Use `yolov8n.pt` with `--batch-size 32`
2. **For best accuracy:** Use `yolov8l.pt` with `--batch-size 8`
3. **For balanced approach:** Use `yolov8s.pt` with `--batch-size 16` (default)

## 📈 Monitoring Progress

The script provides comprehensive logging:

- **Console output:** Real-time training progress
- **Log files:** Detailed logs saved to Google Drive
- **Metrics tracking:** mAP, precision, recall, loss curves
- **Checkpoint summaries:** Training state at each save point

## 🔍 Testing the Installation

Run the test script to verify everything is set up correctly:

```bash
python test_fire_detection.py
```

Or run the interactive demo:

```bash
python colab_demo.py
```

## 📝 License

This project is part of the Workspace-Learning repository. Please refer to the repository's license for usage terms.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues or questions:

1. Check the troubleshooting section above
2. Review the example usage in `FIRE_DETECTION_USAGE.md`
3. Run the demo script for testing
4. Open an issue in the repository

---

**Ready to train fire detection models with confidence in Google Colab! 🔥🚀**