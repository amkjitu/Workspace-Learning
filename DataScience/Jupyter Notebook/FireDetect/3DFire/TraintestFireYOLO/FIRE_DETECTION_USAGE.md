# Fire Detection Training Script Usage Examples

## Google Colab Setup

1. **Install dependencies:**
```bash
!pip install -r requirements_fire_detection.txt
```

2. **Basic training (first time):**
```bash
!python copy_of_fire_train_amk.py \
    --roboflow-api-key "your_api_key_here" \
    --epochs 100 \
    --batch-size 16 \
    --model-name yolov8s.pt
```

3. **Resume training after interruption:**
```bash
!python copy_of_fire_train_amk.py \
    --roboflow-api-key "your_api_key_here" \
    --resume
```

4. **Force restart (ignore checkpoints):**
```bash
!python copy_of_fire_train_amk.py \
    --roboflow-api-key "your_api_key_here" \
    --force-restart \
    --epochs 50
```

## Local Machine Setup

1. **Install dependencies:**
```bash
pip install -r requirements_fire_detection.txt
```

2. **Training (local directories will be used):**
```bash
python copy_of_fire_train_amk.py \
    --roboflow-api-key "your_api_key_here" \
    --epochs 100 \
    --drive-root "./fire_detection_data"
```

## Configuration Options

### Required Parameters:
- `--roboflow-api-key`: Your Roboflow API key for dataset access

### Optional Parameters:
- `--workspace`: Roboflow workspace name (default: "ai-training-course-rximv")
- `--project`: Roboflow project name (default: "fire-and-smoke-detection-vzqpf")
- `--dataset-version`: Dataset version to use (default: 3)
- `--model-name`: YOLO model variant (default: "yolov8s.pt")
- `--epochs`: Number of training epochs (default: 100)
- `--batch-size`: Training batch size (default: 16)
- `--image-size`: Input image size (default: 640)
- `--save-period`: Checkpoint save frequency (default: 10 epochs)
- `--resume`: Resume from latest checkpoint
- `--force-restart`: Ignore existing checkpoints
- `--drive-root`: Google Drive mount point (default: "/content/drive")

## Model Variants

Choose the right model for your needs:
- `yolov8n.pt`: Nano (fastest, least accurate)
- `yolov8s.pt`: Small (good balance)
- `yolov8m.pt`: Medium (better accuracy)
- `yolov8l.pt`: Large (high accuracy)
- `yolov8x.pt`: Extra Large (best accuracy, slowest)

## Google Drive Structure

The script creates the following structure in Google Drive:
```
/content/drive/MyDrive/fire_detection_project/
├── datasets/
│   └── fire_smoke_dataset_v3/
├── checkpoints/
│   ├── checkpoint_epoch_10.pkl
│   ├── checkpoint_epoch_20.pkl
│   └── latest_checkpoint.txt
├── models/
│   └── session_1234567890/
│       ├── best_model_epoch_100.pt
│       ├── model_epoch_100.onnx
│       └── metrics.json
└── logs/
    └── training.log
```

## Features

### Resume Training
- Automatically saves checkpoints every N epochs
- Can resume training after Colab disconnection
- Preserves training state and metrics

### Dataset Caching
- Downloads dataset once and caches to Google Drive
- Avoids re-downloading on subsequent runs
- Supports different dataset versions

### Model Export
- Saves models in PyTorch format (.pt)
- Exports to ONNX format for deployment
- Attempts TensorRT export if available
- Saves training metrics alongside models

### Progress Tracking
- Detailed logging to file and console
- Progress bars for long operations
- Error handling and recovery

## Troubleshooting

1. **Google Drive not mounted:**
   - The script will fall back to local storage
   - For Colab, ensure drive.mount() works

2. **Out of memory errors:**
   - Reduce batch size: `--batch-size 8`
   - Use smaller model: `--model-name yolov8n.pt`

3. **Training interrupted:**
   - Use `--resume` flag to continue from last checkpoint
   - Check Google Drive for saved checkpoints

4. **Dataset download fails:**
   - Check Roboflow API key
   - Verify project and workspace names
   - Check internet connection

## Example Colab Notebook Cell

```python
# Install requirements
!pip install -r requirements_fire_detection.txt

# Run training with resume capability
!python copy_of_fire_train_amk.py \
    --roboflow-api-key "KRl7MmkK5Na8s9ci4KzV" \
    --epochs 100 \
    --batch-size 16 \
    --model-name yolov8s.pt \
    --resume
```