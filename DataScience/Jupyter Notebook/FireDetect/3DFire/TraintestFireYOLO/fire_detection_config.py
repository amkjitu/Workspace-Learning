# Fire Detection Training Configuration
# Copy this file and modify as needed for your training runs

# Roboflow Dataset Configuration
ROBOFLOW_API_KEY = "KRl7MmkK5Na8s9ci4KzV"  # Replace with your API key
WORKSPACE = "ai-training-course-rximv"
PROJECT = "fire-and-smoke-detection-vzqpf"
DATASET_VERSION = 3

# Model Configuration
MODEL_NAME = "yolov8s.pt"  # Options: yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt

# Training Parameters
EPOCHS = 100
BATCH_SIZE = 16
IMAGE_SIZE = 640
SAVE_PERIOD = 10  # Save checkpoint every N epochs

# Resume Configuration
RESUME_TRAINING = True  # Set to False to start fresh
FORCE_RESTART = False   # Set to True to ignore existing checkpoints

# Google Drive Configuration
DRIVE_ROOT = "/content/drive"  # Default for Google Colab

# Hardware Configuration (auto-detected)
DEVICE = "auto"  # Options: "auto", "cpu", "cuda", "mps"

# Logging Configuration
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR