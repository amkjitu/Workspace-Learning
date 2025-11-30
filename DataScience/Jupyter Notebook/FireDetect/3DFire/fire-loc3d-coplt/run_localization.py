#!/usr/bin/env python3
"""
3D Fire Localization Script

This script detects fires in multiple camera views and localizes them in 3D space.
"""
import os
import sys
import argparse
import cv2
import numpy as np
import time
from pathlib import Path
import matplotlib.pyplot as plt

# Add the src directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Import project modules
from src.detector import FireDetector
from src.localize3d import FireLocalizer3D
from src.utils import load_config, read_video_frame, ensure_directory_exists
from src.visualize import (
    visualize_3d_scene,
    draw_detections,
    create_video_with_detections,
)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="3D Fire Localization")
    parser.add_argument(
        "--config",
        type=str,
        default="configs/cameras.yaml",
        help="Path to camera configuration file",
    )
    parser.add_argument(
        "--model", type=str, default=None, help="Path to fire detection model"
    )
    parser.add_argument(
        "--input",
        type=str,
        nargs="+",
        default=None,
        help="Input video files or images (one per camera)",
    )
    parser.add_argument(
        "--output", type=str, default="outputs", help="Output directory"
    )
    parser.add_argument(
        "--planes",
        type=str,
        default="configs/planes.json",
        help="Path to planes configuration file",
    )
    parser.add_argument(
        "--confidence", type=float, default=0.5, help="Detection confidence threshold"
    )
    parser.add_argument("--visualize", action="store_true", help="Show visualization")
    parser.add_argument(
        "--save-video", action="store_true", help="Save output video with detections"
    )

    return parser.parse_args()


def process_images(image_paths, detector, localizer, args):
    """
    Process a set of images from multiple cameras.

    Args:
        image_paths: List of paths to images
        detector: Fire detector
        localizer: 3D localizer
        args: Command-line arguments

    Returns:
        fire_locations: 3D fire locations
        images_with_detections: Images with detections drawn
    """
    # Load images
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        if image is None:
            print(f"Error: Could not read image {path}")
            continue
        images.append(image)

    # Run detection on each image
    all_detections = {}
    images_with_detections = []

    for i, image in enumerate(images):
        # Detect fires
        detections = detector.detect(image)

        # Filter by confidence
        detections = [d for d in detections if d[4] >= args.confidence]

        # Get center points for localization
        centers = detector.get_center_points(detections)

        # Store detections
        camera_id = f"cam{i+1}"
        all_detections[camera_id] = centers

        # Draw detections
        image_with_detections = detector.draw_detections(image, detections)
        images_with_detections.append(image_with_detections)

    # Localize fires in 3D
    fire_locations = localizer.localize_fire(all_detections)

    return fire_locations, images_with_detections


def process_videos(video_paths, detector, localizer, args):
    """
    Process videos from multiple cameras.

    Args:
        video_paths: List of paths to videos
        detector: Fire detector
        localizer: 3D localizer
        args: Command-line arguments

    Returns:
        All detected fire locations over time
    """
    # Open videos
    caps = []
    for path in video_paths:
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            print(f"Error: Could not open video {path}")
            continue
        caps.append(cap)

    if not caps:
        print("Error: No videos could be opened")
        return []

    # Create output video writers if needed
    writers = []
    if args.save_video:
        output_dir = Path(args.output) / "videos"
        ensure_directory_exists(output_dir)

        for i, cap in enumerate(caps):
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            output_path = output_dir / f"output_cam{i+1}.mp4"
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
            writers.append(writer)

    # Process videos frame by frame
    all_fire_locations = []
    frame_count = 0

    try:
        while True:
            # Read frames
            frames = []
            for cap in caps:
                ret, frame = cap.read()
                if not ret:
                    raise StopIteration
                frames.append(frame)

            # Run detection on each frame
            all_detections = {}

            for i, frame in enumerate(frames):
                # Detect fires
                detections = detector.detect(frame)

                # Filter by confidence
                detections = [d for d in detections if d[4] >= args.confidence]

                # Get center points for localization
                centers = detector.get_center_points(detections)

                # Store detections
                camera_id = f"cam{i+1}"
                all_detections[camera_id] = centers

                # Draw detections and save video if needed
                if args.save_video:
                    frame_with_detections = detector.draw_detections(frame, detections)
                    writers[i].write(frame_with_detections)

            # Localize fires in 3D
            fire_locations = localizer.localize_fire(all_detections)
            all_fire_locations.extend(fire_locations)

            # Print progress
            frame_count += 1
            if frame_count % 10 == 0:
                print(
                    f"Processed {frame_count} frames, found {len(fire_locations)} fires"
                )

    except StopIteration:
        print(f"Finished processing {frame_count} frames")

    # Release resources
    for cap in caps:
        cap.release()

    for writer in writers:
        writer.release()

    return all_fire_locations


def main():
    """Main function."""
    args = parse_args()

    # Load configuration
    config = load_config(args.config)

    # Create output directory
    output_dir = Path(args.output)
    ensure_directory_exists(output_dir)

    # Initialize fire detector
    model_path = args.model
    if model_path is None:
        # Try to find a model in the default location
        model_path = Path("best.pt")
        if not model_path.exists():
            print(f"No model specified and default model not found at {model_path}")
            print("Please specify a model with --model")
            return

    print(f"Loading fire detection model from {model_path}")
    detector = FireDetector(
        model_path=model_path, conf_thres=args.confidence, iou_thres=0.45
    )

    # Initialize 3D localizer
    print(f"Initializing 3D fire localizer")
    localizer = FireLocalizer3D(
        camera_configs=config["cameras"],
        min_cameras=config["localization"]["min_cameras"],
        max_reprojection_error=config["localization"]["max_reprojection_error"],
        triangulation_method=config["localization"]["triangulation_method"],
    )

    # Process input
    if args.input is None:
        print("No input specified. Please provide images or videos with --input")
        return

    input_paths = args.input

    # Determine if inputs are images or videos
    input_type = "unknown"
    for path in input_paths:
        ext = Path(path).suffix.lower()
        if ext in [".jpg", ".jpeg", ".png", ".bmp"]:
            if input_type == "unknown":
                input_type = "images"
            elif input_type == "videos":
                print(
                    "Error: Mixed input types. Please provide either all images or all videos."
                )
                return
        elif ext in [".mp4", ".avi", ".mov", ".mkv"]:
            if input_type == "unknown":
                input_type = "videos"
            elif input_type == "images":
                print(
                    "Error: Mixed input types. Please provide either all images or all videos."
                )
                return
        else:
            print(f"Warning: Unrecognized file extension for {path}")

    print(f"Processing {len(input_paths)} {input_type}")

    # Process inputs
    if input_type == "images":
        fire_locations, images_with_detections = process_images(
            input_paths, detector, localizer, args
        )

        # Save output images
        for i, image in enumerate(images_with_detections):
            output_path = output_dir / f"detection_cam{i+1}.jpg"
            cv2.imwrite(str(output_path), image)
            print(f"Saved detection image to {output_path}")

    elif input_type == "videos":
        fire_locations = process_videos(input_paths, detector, localizer, args)
    else:
        print("Error: Could not determine input type")
        return

    # Save fire locations
    fire_locations_path = output_dir / "fire_locations.json"
    import json

    with open(fire_locations_path, "w") as f:
        json.dump(fire_locations, f, indent=2)
    print(f"Saved {len(fire_locations)} 3D fire locations to {fire_locations_path}")

    # Visualize results
    if fire_locations and (args.visualize or input_type == "images"):
        fig = visualize_3d_scene(
            fire_locations,
            camera_params=localizer.get_camera_parameters(),
            planes_file=args.planes if Path(args.planes).exists() else None,
            show_cameras=True,
        )

        # Save figure
        fig_path = output_dir / "fire_locations_3d.png"
        plt.savefig(fig_path)
        print(f"Saved 3D visualization to {fig_path}")

        if args.visualize:
            plt.show()


if __name__ == "__main__":
    main()
