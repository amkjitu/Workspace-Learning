"""
Visualization utilities for fire detection and 3D localization.
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional


def draw_detections(image, detections, color=(0, 0, 255), thickness=2):
    """
    Draw bounding boxes for fire detections.

    Args:
        image: OpenCV image
        detections: List of [x1, y1, x2, y2, confidence, class_id]
        color: Box color (BGR format)
        thickness: Line thickness

    Returns:
        Image with drawn detections
    """
    image_copy = image.copy()

    for detection in detections:
        x1, y1, x2, y2 = (
            int(detection[0]),
            int(detection[1]),
            int(detection[2]),
            int(detection[3]),
        )
        confidence = detection[4]

        # Draw bounding box
        cv2.rectangle(image_copy, (x1, y1), (x2, y2), color, thickness)

        # Draw confidence text
        text = f"{confidence:.2f}"
        font_scale = 0.5
        text_thickness = 1
        (text_width, text_height), _ = cv2.getTextSize(
            text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_thickness
        )

        # Draw text background
        cv2.rectangle(
            image_copy, (x1, y1 - text_height - 5), (x1 + text_width, y1), color, -1
        )

        # Draw text
        cv2.putText(
            image_copy,
            text,
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            (255, 255, 255),
            text_thickness,
        )

    return image_copy


def draw_epipolar_lines(image1, points1, image2, points2, F, colors=None, thickness=1):
    """
    Draw epipolar lines in two images.

    Args:
        image1: First image
        points1: Points in first image (Nx2)
        image2: Second image
        points2: Points in second image (Nx2)
        F: Fundamental matrix from image1 to image2
        colors: List of colors for each point pair
        thickness: Line thickness

    Returns:
        (image1_with_lines, image2_with_lines): Tuple of images with epipolar lines
    """
    image1_copy = image1.copy()
    image2_copy = image2.copy()

    h1, w1 = image1.shape[:2]
    h2, w2 = image2.shape[:2]

    if colors is None:
        import colorsys

        n = len(points1)
        colors = []
        for i in range(n):
            hue = i / n
            rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.8)
            color = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
            colors.append(color)

    # Convert points to homogeneous coordinates
    points1_h = np.column_stack((points1, np.ones(len(points1))))
    points2_h = np.column_stack((points2, np.ones(len(points2))))

    # Compute epipolar lines in the second image corresponding to points in the first
    lines2 = (F @ points1_h.T).T

    # Compute epipolar lines in the first image corresponding to points in the second
    lines1 = (F.T @ points2_h.T).T

    # Draw lines in the second image
    for i, (point, line) in enumerate(zip(points1, lines2)):
        color = colors[i % len(colors)]

        # Extract line parameters
        a, b, c = line

        # Find intersection points with image borders
        if abs(b) > 1e-7:
            x0, y0 = 0, -c / b
            x1, y1 = w2, -(a * w2 + c) / b
        else:
            x0, y0 = -c / a, 0
            x1, y1 = -(b * h2 + c) / a, h2

        # Draw line
        cv2.line(image2_copy, (int(x0), int(y0)), (int(x1), int(y1)), color, thickness)

        # Draw point
        cv2.circle(image1_copy, (int(point[0]), int(point[1])), 5, color, -1)

    # Draw lines in the first image
    for i, (point, line) in enumerate(zip(points2, lines1)):
        color = colors[i % len(colors)]

        # Extract line parameters
        a, b, c = line

        # Find intersection points with image borders
        if abs(b) > 1e-7:
            x0, y0 = 0, -c / b
            x1, y1 = w1, -(a * w1 + c) / b
        else:
            x0, y0 = -c / a, 0
            x1, y1 = -(b * h1 + c) / a, h1

        # Draw line
        cv2.line(image1_copy, (int(x0), int(y0)), (int(x1), int(y1)), color, thickness)

        # Draw point
        cv2.circle(image2_copy, (int(point[0]), int(point[1])), 5, color, -1)

    return image1_copy, image2_copy


def visualize_3d_scene(
    fire_locations,
    camera_params=None,
    planes_file=None,
    show_cameras=True,
    marker_size=100,
    figure_size=(10, 8),
):
    """
    Visualize fire locations and camera positions in 3D.

    Args:
        fire_locations: List of fire location dictionaries
        camera_params: Dictionary of camera parameters
        planes_file: Path to JSON file with plane definitions
        show_cameras: Whether to show cameras in the visualization
        marker_size: Size of fire markers
        figure_size: Size of the figure (width, height)

    Returns:
        fig: Matplotlib figure
    """
    fig = plt.figure(figsize=figure_size)
    ax = fig.add_subplot(111, projection="3d")

    # Plot fire locations
    x = [loc["position"][0] for loc in fire_locations]
    y = [loc["position"][1] for loc in fire_locations]
    z = [loc["position"][2] for loc in fire_locations]
    confidences = [loc["confidence"] for loc in fire_locations]

    # Scatter plot with confidence-based color
    scatter = ax.scatter(
        x, y, z, c=confidences, s=marker_size, cmap="hot", marker="o", alpha=0.8
    )
    plt.colorbar(scatter, label="Confidence")

    # Plot camera positions if available
    if show_cameras and camera_params is not None:
        cameras = camera_params.get("cameras", {})
        for cam_id, cam in cameras.items():
            pos = cam.get("position", [0, 0, 0])
            ax.scatter(pos[0], pos[1], pos[2], color="blue", marker="^", s=100)
            ax.text(pos[0], pos[1], pos[2], f"{cam_id}", color="black", fontsize=8)

            # Plot camera orientation if available
            R = cam.get("rotation", np.eye(3))
            if isinstance(R, list):
                R = np.array(R)

            # Camera coordinate system axes
            scale = 0.5  # Scale factor for axis visualization
            origin = np.array(pos)

            # X axis in red
            x_axis = origin + scale * R[:, 0]
            ax.plot(
                [origin[0], x_axis[0]],
                [origin[1], x_axis[1]],
                [origin[2], x_axis[2]],
                color="red",
                linewidth=2,
            )

            # Y axis in green
            y_axis = origin + scale * R[:, 1]
            ax.plot(
                [origin[0], y_axis[0]],
                [origin[1], y_axis[1]],
                [origin[2], y_axis[2]],
                color="green",
                linewidth=2,
            )

            # Z axis in blue
            z_axis = origin + scale * R[:, 2]
            ax.plot(
                [origin[0], z_axis[0]],
                [origin[1], z_axis[1]],
                [origin[2], z_axis[2]],
                color="blue",
                linewidth=2,
            )

    # Load and plot planes if specified
    if planes_file is not None:
        try:
            with open(planes_file, "r") as f:
                planes_data = json.load(f)

            # Plot ground plane
            if "ground_plane" in planes_data:
                ground = planes_data["ground_plane"]
                color = ground.get("color", [0.8, 0.8, 0.8])
                dims = ground.get("dimensions", [10.0, 10.0])

                # Create a grid
                x_grid = np.linspace(-dims[0] / 2, dims[0] / 2, 11)
                y_grid = np.linspace(-dims[1] / 2, dims[1] / 2, 11)
                X, Y = np.meshgrid(x_grid, y_grid)
                Z = np.zeros_like(X)

                # Plot as a surface with grid lines
                ax.plot_surface(
                    X, Y, Z, color=color, alpha=0.3, edgecolor="gray", linewidth=0.5
                )

            # Plot vertical planes
            if "vertical_planes" in planes_data:
                for plane in planes_data["vertical_planes"]:
                    equation = plane.get("equation", [0, 0, 1, 0])
                    color = plane.get("color", [0.9, 0.9, 0.5])
                    dims = plane.get("dimensions", [10.0, 5.0])

                    # Create a grid based on plane equation
                    a, b, c, d = equation

                    # Handle different orientations
                    if abs(c) > 1e-6:  # Horizontal plane
                        x_grid = np.linspace(-dims[0] / 2, dims[0] / 2, 11)
                        y_grid = np.linspace(-dims[1] / 2, dims[1] / 2, 11)
                        X, Y = np.meshgrid(x_grid, y_grid)
                        Z = (-a * X - b * Y - d) / c
                    elif abs(b) > 1e-6:  # Vertical plane along X
                        x_grid = np.linspace(-dims[0] / 2, dims[0] / 2, 11)
                        z_grid = np.linspace(0, dims[1], 11)
                        X, Z = np.meshgrid(x_grid, z_grid)
                        Y = (-a * X - c * Z - d) / b
                    elif abs(a) > 1e-6:  # Vertical plane along Y
                        y_grid = np.linspace(-dims[0] / 2, dims[0] / 2, 11)
                        z_grid = np.linspace(0, dims[1], 11)
                        Y, Z = np.meshgrid(y_grid, z_grid)
                        X = (-b * Y - c * Z - d) / a
                    else:
                        continue

                    # Plot as a surface with grid lines
                    ax.plot_surface(
                        X, Y, Z, color=color, alpha=0.3, edgecolor="gray", linewidth=0.5
                    )

        except Exception as e:
            print(f"Error loading or visualizing planes: {e}")

    # Set labels and title
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.set_title(f"3D Fire Localization: {len(fire_locations)} detections")

    # Equal aspect ratio
    ax.set_box_aspect([1, 1, 1])

    # Set limits with some margin
    if x:
        margin = max(1, 0.1 * (max(x) - min(x)))
        ax.set_xlim([min(x) - margin, max(x) + margin])
        ax.set_ylim([min(y) - margin, max(y) + margin])
        ax.set_zlim([min(z) - margin, max(z) + margin])

    return fig


def create_video_with_detections(
    video_path,
    output_path,
    detector,
    frame_processor=None,
    start_frame=0,
    end_frame=None,
    fps=None,
):
    """
    Create a video with fire detections.

    Args:
        video_path: Path to input video
        output_path: Path to save output video
        detector: Fire detector object
        frame_processor: Optional function to process frames further
        start_frame: First frame to process
        end_frame: Last frame to process (None for all frames)
        fps: Output video fps (None to use same as input)
    """
    # Open video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if fps is None:
        fps = cap.get(cv2.CAP_PROP_FPS)

    # Set end frame
    if end_frame is None or end_frame > total_frames:
        end_frame = total_frames

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Skip to start frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Process frames
    frame_count = start_frame
    while cap.isOpened() and frame_count < end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect fires
        detections = detector.detect(frame)

        # Draw detections
        frame_with_detections = draw_detections(frame, detections)

        # Apply additional processing if provided
        if frame_processor is not None:
            frame_with_detections = frame_processor(
                frame_with_detections, detections, frame_count
            )

        # Write frame
        out.write(frame_with_detections)

        # Increment counter
        frame_count += 1

        # Print progress
        if frame_count % 100 == 0:
            print(f"Processed frame {frame_count}/{end_frame}")

    # Release resources
    cap.release()
    out.release()
    print(f"Video saved to {output_path}")
