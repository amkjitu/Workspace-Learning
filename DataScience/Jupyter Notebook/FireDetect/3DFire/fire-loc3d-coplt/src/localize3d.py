"""
3D fire localization from multiple camera views.
"""

import numpy as np
import cv2
from typing import List, Dict, Tuple, Any, Optional

from .geometry import dlt_triangulate, compute_reprojection_error


class FireLocalizer3D:
    """Fire localization in 3D space using multiple camera views."""

    def __init__(
        self,
        camera_configs: Dict[str, Any],
        min_cameras: int = 2,
        max_reprojection_error: float = 5.0,
        triangulation_method: str = "DLT",
    ):
        """
        Initialize the 3D fire localizer.

        Args:
            camera_configs: Dictionary of camera configurations from config file
            min_cameras: Minimum number of cameras for triangulation (default: 2)
            max_reprojection_error: Maximum allowed reprojection error (default: 5.0)
            triangulation_method: Method for triangulation (default: "DLT")
        """
        self.camera_configs = camera_configs
        self.min_cameras = min_cameras
        self.max_reprojection_error = max_reprojection_error
        self.triangulation_method = triangulation_method

        # Extract camera parameters
        self.cameras = {}
        self.projection_matrices = {}
        self.load_camera_parameters()

        # Camera pairs for computing fundamental matrices
        self.fundamental_matrices = {}
        self.compute_fundamental_matrices()

    def load_camera_parameters(self):
        """
        Load camera parameters from configurations.
        """
        for cam_id, config in self.camera_configs.items():
            if "calibration_file" in config:
                # Load calibration data
                try:
                    with open(config["calibration_file"], "r") as f:
                        import json

                        calib_data = json.load(f)

                    # Extract camera matrix and distortion coefficients
                    camera_matrix = np.array(
                        calib_data.get(
                            "camera_matrix", calib_data.get("projection_matrix")
                        )
                    )
                    dist_coeffs = np.array(
                        calib_data.get("distortion_coefficients", [0, 0, 0, 0, 0])
                    )

                    # Extract extrinsic parameters if available
                    if (
                        "rotation_matrix" in calib_data
                        and "translation_vector" in calib_data
                    ):
                        R = np.array(calib_data["rotation_matrix"])
                        t = np.array(calib_data["translation_vector"])
                    else:
                        # Default to identity rotation and zero translation
                        R = np.eye(3)
                        t = np.zeros(3)

                    # Store camera parameters
                    self.cameras[cam_id] = {
                        "camera_matrix": camera_matrix[:3, :3],  # Make sure it's 3x3
                        "dist_coeffs": dist_coeffs,
                        "rotation": R,
                        "translation": t,
                        "position": np.array(config.get("position", [0.0, 0.0, 0.0])),
                        "resolution": config.get("resolution", [1920, 1080]),
                    }

                    # Compute projection matrix
                    if camera_matrix.shape == (3, 4):
                        # If already a projection matrix
                        self.projection_matrices[cam_id] = camera_matrix
                    else:
                        # Construct projection matrix from intrinsics and extrinsics
                        Rt = np.column_stack((R, t))
                        self.projection_matrices[cam_id] = camera_matrix[:3, :3] @ Rt

                except Exception as e:
                    print(f"Error loading calibration data for camera {cam_id}: {e}")

    def compute_fundamental_matrices(self):
        """
        Compute fundamental matrices for all camera pairs.
        """
        camera_ids = list(self.cameras.keys())
        for i, cam_i in enumerate(camera_ids):
            for j, cam_j in enumerate(camera_ids):
                if i >= j:
                    continue

                try:
                    from .geometry import compute_fundamental_matrix

                    # Get projection matrices
                    P_i = self.projection_matrices[cam_i]
                    P_j = self.projection_matrices[cam_j]

                    # Compute fundamental matrix
                    F_ij = compute_fundamental_matrix(P_i, P_j)

                    # Store it
                    self.fundamental_matrices[(cam_i, cam_j)] = F_ij
                    self.fundamental_matrices[(cam_j, cam_i)] = (
                        F_ij.T
                    )  # Transpose for reverse direction

                except Exception as e:
                    print(
                        f"Error computing fundamental matrix for cameras {cam_i}-{cam_j}: {e}"
                    )

    def localize_fire(
        self, fire_detections: Dict[str, List[List[float]]]
    ) -> List[Dict[str, Any]]:
        """
        Localize fire in 3D space from multiple camera views.

        Args:
            fire_detections: Dictionary of fire detections for each camera
                             {cam_id: [[cx, cy, confidence, class_id], ...]}

        Returns:
            List of dictionaries with 3D fire locations and metadata
        """
        from .associate import associate_across_multiple_views

        # Convert detections to format expected by association function
        camera_ids = list(fire_detections.keys())
        all_detections = []
        for cam_id in camera_ids:
            detections = fire_detections.get(cam_id, [])
            all_detections.append(detections)

        # Associate detections across views
        associations = associate_across_multiple_views(
            all_detections,
            {
                (i, j): self.fundamental_matrices.get((camera_ids[i], camera_ids[j]))
                for i in range(len(camera_ids))
                for j in range(len(camera_ids))
                if i != j
            },
            max_distance=self.max_reprojection_error,
        )

        # Triangulate 3D positions
        fire_locations = []
        for association in associations:
            if len(association) < self.min_cameras:
                continue

            # Gather projection matrices and points
            P_list = []
            points_list = []
            confidences = []

            for cam_idx, det_idx in association:
                cam_id = camera_ids[cam_idx]
                detection = all_detections[cam_idx][det_idx]

                P_list.append(self.projection_matrices[cam_id])
                points_list.append(detection[:2])  # Extract point coordinates
                confidences.append(detection[2])  # Extract confidence

            # Triangulate the 3D point
            try:
                if self.triangulation_method == "DLT":
                    point_3d = dlt_triangulate(P_list, points_list)
                else:
                    # Alternative methods could be implemented here
                    point_3d = dlt_triangulate(P_list, points_list)

                # Compute reprojection error
                errors = []
                for P, point_2d in zip(P_list, points_list):
                    # Convert 3D point to homogeneous coordinates
                    point_3d_h = np.append(point_3d, 1.0)

                    # Project 3D point to 2D
                    projected = P @ point_3d_h
                    projected = projected[:2] / projected[2]

                    # Compute error
                    error = np.sqrt(np.sum((projected - point_2d) ** 2))
                    errors.append(error)

                # Only include points with acceptable reprojection error
                if np.mean(errors) <= self.max_reprojection_error:
                    fire_locations.append(
                        {
                            "position": point_3d.tolist(),
                            "num_views": len(association),
                            "confidence": np.mean(confidences),
                            "reprojection_error": float(np.mean(errors)),
                            "camera_indices": [cam_idx for cam_idx, _ in association],
                            "detection_indices": [
                                det_idx for _, det_idx in association
                            ],
                        }
                    )

            except Exception as e:
                print(f"Error triangulating point: {e}")

        return fire_locations

    def get_camera_parameters(self) -> Dict[str, Any]:
        """Get camera parameters for visualization."""
        return {
            "cameras": self.cameras,
            "projection_matrices": {
                k: v.tolist() for k, v in self.projection_matrices.items()
            },
            "fundamental_matrices": {
                str(k): v.tolist() for k, v in self.fundamental_matrices.items()
            },
        }
