import numpy as np
import cv2
import argparse
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils import ensure_directory_exists
from src.geometry import dlt_calibration, normalize_points, compute_projection_matrix


def calibrate_using_dlt(points_3d, points_2d):
    """
    Calibrate camera using Direct Linear Transformation (DLT) algorithm.

    Args:
        points_3d: List of 3D points in world coordinates
        points_2d: List of corresponding 2D points in image coordinates

    Returns:
        P: 3x4 projection matrix
    """
    # Convert points to numpy arrays
    points_3d = np.array(points_3d, dtype=np.float32)
    points_2d = np.array(points_2d, dtype=np.float32)

    # Normalize points to improve numerical stability
    points_3d_norm, T3d = normalize_points(points_3d)
    points_2d_norm, T2d = normalize_points(points_2d)

    # Calculate DLT projection matrix
    P_norm = dlt_calibration(points_3d_norm, points_2d_norm)

    # Denormalize the projection matrix
    P = np.linalg.inv(T2d) @ P_norm @ T3d

    # Ensure P[2,3] = 1
    P = P / P[2, 3]

    return P


def decompose_projection_matrix(P):
    """
    Decompose projection matrix into intrinsic and extrinsic parameters.

    Args:
        P: 3x4 projection matrix

    Returns:
        K: 3x3 camera intrinsic matrix
        R: 3x3 rotation matrix
        t: 3x1 translation vector
    """
    # Extract the first 3x3 submatrix
    M = P[:, 0:3]

    # QR decomposition to get K and R
    # Note: Since we need upper triangular K, we use RQ decomposition (QR of M^T)^T
    K, R = np.linalg.qr(np.linalg.inv(M).T)
    K = np.linalg.inv(K).T
    R = R.T

    # Ensure K has positive diagonal elements
    T = np.diag(np.sign(np.diag(K)))
    K = K @ T
    R = T @ R

    # Normalize K so that K[2,2] = 1
    K = K / K[2, 2]

    # Extract the translation vector
    t = np.linalg.inv(M) @ P[:, 3].reshape(3, 1)

    return K, R, t


def collect_calibration_points(points_file):
    """
    Load or collect calibration points (3D world points and their 2D image projections).

    Args:
        points_file: File to save/load calibration points

    Returns:
        points_3d: List of 3D points
        points_2d: List of corresponding 2D points
    """
    # Try to load existing points
    if os.path.exists(points_file):
        with open(points_file, "r") as f:
            data = json.load(f)
            return np.array(data["points_3d"]), np.array(data["points_2d"])

    # If not available, provide sample points (this would typically be collected interactively)
    points_3d = np.array(
        [
            [0.0, 0.0, 0.0],  # Origin
            [1.0, 0.0, 0.0],  # X-axis point
            [0.0, 1.0, 0.0],  # Y-axis point
            [0.0, 0.0, 1.0],  # Z-axis point
            [1.0, 1.0, 0.0],  # XY plane point
            [1.0, 0.0, 1.0],  # XZ plane point
            [0.0, 1.0, 1.0],  # YZ plane point
            [1.0, 1.0, 1.0],  # Point in 3D space
        ],
        dtype=np.float32,
    )

    # Sample 2D points (these would be manually marked in a real scenario)
    points_2d = np.array(
        [
            [512, 384],  # Origin in image
            [612, 384],  # X-axis point in image
            [512, 284],  # Y-axis point in image
            [512, 484],  # Z-axis point in image
            [612, 284],  # XY plane point in image
            [612, 484],  # XZ plane point in image
            [512, 584],  # YZ plane point in image
            [612, 584],  # Point in 3D space in image
        ],
        dtype=np.float32,
    )

    # Save the points
    with open(points_file, "w") as f:
        json.dump(
            {
                "points_3d": points_3d.tolist(),
                "points_2d": points_2d.tolist(),
            },
            f,
            indent=2,
        )

    return points_3d, points_2d


def main():
    parser = argparse.ArgumentParser(description="Camera calibration using DLT method")
    parser.add_argument(
        "--output",
        type=str,
        default="calibration_dlt.json",
        help="Output calibration file",
    )
    parser.add_argument(
        "--points_file",
        type=str,
        default="calibration_points.json",
        help="File with 3D-2D point correspondences",
    )
    args = parser.parse_args()

    # Create calibration directory if it doesn't exist
    ensure_directory_exists(os.path.dirname(args.output))

    # Load or collect calibration points
    points_3d, points_2d = collect_calibration_points(args.points_file)

    # Perform DLT calibration
    P = calibrate_using_dlt(points_3d, points_2d)

    # Decompose projection matrix
    K, R, t = decompose_projection_matrix(P)

    # Calculate reprojection error
    points_3d_homogeneous = np.hstack((points_3d, np.ones((points_3d.shape[0], 1))))
    projected_points = (P @ points_3d_homogeneous.T).T
    projected_points = projected_points[:, :2] / projected_points[:, 2:]
    reprojection_errors = np.linalg.norm(points_2d - projected_points, axis=1)
    mean_error = np.mean(reprojection_errors)

    print(f"Projection Matrix:\n{P}")
    print(f"Camera Matrix (K):\n{K}")
    print(f"Rotation Matrix (R):\n{R}")
    print(f"Translation Vector (t):\n{t}")
    print(f"Mean Reprojection Error: {mean_error:.4f} pixels")

    # Save calibration data
    calibration_data = {
        "projection_matrix": P.tolist(),
        "camera_matrix": K.tolist(),
        "rotation_matrix": R.tolist(),
        "translation_vector": t.flatten().tolist(),
        "reprojection_error": float(mean_error),
        "calibration_method": "DLT",
        "image_width": int(max(points_2d[:, 0]) * 1.2),  # Estimate image size
        "image_height": int(max(points_2d[:, 1]) * 1.2),  # Estimate image size
    }

    with open(args.output, "w") as f:
        json.dump(calibration_data, f, indent=2)

    print(f"Calibration saved to {args.output}")


if __name__ == "__main__":
    main()
