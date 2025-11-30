# Fire-Loc3D: 3D Fire Localization System

A system for detecting and localizing fires in 3D space using multiple camera views and YOLO-based detection.

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Camera Calibration
```
python calib/calibrate_charuco_single.py --camera_id 0 --output calibration.json
```

### Run Fire Localization
```
python run_localization.py --config configs/cameras.yaml
```

## System Overview

This system uses the following pipeline:
1. Detect fires in 2D images using YOLO-based detector
2. Associate detections across multiple camera views
3. Triangulate 2D detections to 3D space
4. Visualize the results

## License

This project is licensed under the MIT License - see the LICENSE file for details.
