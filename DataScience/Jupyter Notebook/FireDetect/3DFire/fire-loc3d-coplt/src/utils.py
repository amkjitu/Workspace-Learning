"""
Utility functions for fire detection and localization.
"""

import os
import yaml
import json
import numpy as np
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional, Union
import cv2


def ensure_directory_exists(directory: Union[str, Path]):
    """
    Ensure directory exists, create if not.

    Args:
        directory: Directory path
    """
    directory = Path(directory)
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)


def load_config(config_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load configuration from YAML or JSON file.

    Args:
        config_path: Path to configuration file

    Returns:
        Configuration dictionary
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    if config_path.suffix.lower() in [".yaml", ".yml"]:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    elif config_path.suffix.lower() == ".json":
        with open(config_path, "r") as f:
            config = json.load(f)
    else:
        raise ValueError(f"Unsupported configuration file format: {config_path.suffix}")

    return config


def save_detections(detections: List[List[float]], output_path: Union[str, Path]):
    """
    Save detections to a file.

    Args:
        detections: List of detections, each as [x1, y1, x2, y2, confidence, class_id]
        output_path: Path to save detections
    """
    output_path = Path(output_path)
    ensure_directory_exists(output_path.parent)

    with open(output_path, "w") as f:
        for detection in detections:
            # Format: x1,y1,x2,y2,confidence,class_id
            line = ",".join(str(round(x, 6)) for x in detection)
            f.write(line + "\n")


def load_detections(input_path: Union[str, Path]) -> List[List[float]]:
    """
    Load detections from a file.

    Args:
        input_path: Path to load detections from

    Returns:
        List of detections, each as [x1, y1, x2, y2, confidence, class_id]
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Detections file not found: {input_path}")

    detections = []
    with open(input_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                values = line.split(",")
                detection = [float(x) for x in values]
                detections.append(detection)

    return detections


def resize_image_with_aspect_ratio(image, target_size):
    """
    Resize image while maintaining aspect ratio.

    Args:
        image: Input image
        target_size: Target size (width, height) or maximum dimension

    Returns:
        Resized image
    """
    h, w = image.shape[:2]

    if isinstance(target_size, int):
        # Scale to maximum dimension
        scale = target_size / max(h, w)
        target_width = int(w * scale)
        target_height = int(h * scale)
    else:
        # Scale to fit within target_size (width, height)
        target_width, target_height = target_size
        scale_w = target_width / w
        scale_h = target_height / h
        scale = min(scale_w, scale_h)
        target_width = int(w * scale)
        target_height = int(h * scale)

    resized = cv2.resize(
        image, (target_width, target_height), interpolation=cv2.INTER_AREA
    )
    return resized


def read_video_frame(video_path, frame_number):
    """
    Read a specific frame from a video.

    Args:
        video_path: Path to video file
        frame_number: Frame number to read (0-indexed)

    Returns:
        Frame image or None if frame cannot be read
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    # Check if frame_number is valid
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_number < 0 or frame_number >= total_frames:
        cap.release()
        raise ValueError(
            f"Invalid frame number: {frame_number}. Video has {total_frames} frames."
        )

    # Set position to frame_number
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read frame
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return None

    return frame


def estimate_fundamental_matrix(
    points1, points2, method=cv2.FM_RANSAC, ransac_threshold=3.0, confidence=0.99
):
    """
    Estimate fundamental matrix from corresponding points.

    Args:
        points1: Points in first image (Nx2)
        points2: Points in second image (Nx2)
        method: Method to compute fundamental matrix
        ransac_threshold: RANSAC threshold
        confidence: Confidence level

    Returns:
        F, mask: Fundamental matrix and inlier mask
    """
    if len(points1) < 8 or len(points2) < 8:
        raise ValueError("At least 8 point correspondences required")

    points1 = np.array(points1, dtype=np.float32)
    points2 = np.array(points2, dtype=np.float32)

    F, mask = cv2.findFundamentalMat(
        points1,
        points2,
        method,
        ransacThreshold=ransac_threshold,
        confidence=confidence,
    )

    return F, mask


def compute_homography(src_points, dst_points, method=cv2.RANSAC, ransac_threshold=3.0):
    """
    Compute homography matrix from corresponding points.

    Args:
        src_points: Source points (Nx2)
        dst_points: Destination points (Nx2)
        method: Method to compute homography
        ransac_threshold: RANSAC threshold

    Returns:
        H, mask: Homography matrix and inlier mask
    """
    if len(src_points) < 4 or len(dst_points) < 4:
        raise ValueError("At least 4 point correspondences required")

    src_points = np.array(src_points, dtype=np.float32)
    dst_points = np.array(dst_points, dtype=np.float32)

    H, mask = cv2.findHomography(src_points, dst_points, method, ransac_threshold)

    return H, mask


def format_time(seconds):
    """
    Format time in seconds to human-readable string.

    Args:
        seconds: Time in seconds

    Returns:
        Formatted time string
    """
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"
