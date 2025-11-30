"""
Geometric operations for 3D fire localization.
"""

import numpy as np
import cv2


def normalize_points(points):
    """
    Normalize points to improve numerical stability.

    Args:
        points: Nx2 or Nx3 array of points

    Returns:
        normalized_points: Normalized points
        T: Transformation matrix
    """
    if points.shape[1] == 2:
        # 2D points
        centroid = np.mean(points, axis=0)
        dist = np.sqrt(np.sum((points - centroid) ** 2, axis=1))
        scale = np.sqrt(2) / np.mean(dist)

        T = np.array(
            [
                [scale, 0, -scale * centroid[0]],
                [0, scale, -scale * centroid[1]],
                [0, 0, 1],
            ]
        )

        # Convert to homogeneous coordinates and normalize
        homogeneous = np.hstack((points, np.ones((points.shape[0], 1))))
        normalized_points = (T @ homogeneous.T).T

        return normalized_points[:, :2], T

    elif points.shape[1] == 3:
        # 3D points
        centroid = np.mean(points, axis=0)
        dist = np.sqrt(np.sum((points - centroid) ** 2, axis=1))
        scale = np.sqrt(3) / np.mean(dist)

        T = np.array(
            [
                [scale, 0, 0, -scale * centroid[0]],
                [0, scale, 0, -scale * centroid[1]],
                [0, 0, scale, -scale * centroid[2]],
                [0, 0, 0, 1],
            ]
        )

        # Convert to homogeneous coordinates and normalize
        homogeneous = np.hstack((points, np.ones((points.shape[0], 1))))
        normalized_points = (T @ homogeneous.T).T

        return normalized_points[:, :3], T

    else:
        raise ValueError("Points must be 2D or 3D")


def compute_fundamental_matrix(P1, P2):
    """
    Compute the fundamental matrix from two projection matrices.

    Args:
        P1: 3x4 projection matrix of the first camera
        P2: 3x4 projection matrix of the second camera

    Returns:
        F: 3x3 fundamental matrix such that x2^T F x1 = 0
    """
    # Compute the center of the first camera
    C1 = null_space(P1)
    C1 = C1[:3] / C1[3]  # Convert from homogeneous coordinates

    # Compute epipole in the second image
    e2 = P2 @ np.append(C1, 1)

    # Create skew-symmetric matrix from epipole
    e2_cross = np.array([[0, -e2[2], e2[1]], [e2[2], 0, -e2[0]], [-e2[1], e2[0], 0]])

    # Compute fundamental matrix
    F = e2_cross @ P2 @ np.linalg.pinv(P1)

    return F / np.linalg.norm(F)


def null_space(A):
    """
    Compute the null space of a matrix.

    Args:
        A: Matrix

    Returns:
        Null space of A
    """
    u, s, vh = np.linalg.svd(A)
    return vh[-1, :]


def compute_projection_matrix(K, R, t):
    """
    Compute projection matrix from intrinsic and extrinsic parameters.

    Args:
        K: 3x3 camera intrinsic matrix
        R: 3x3 rotation matrix
        t: 3x1 translation vector

    Returns:
        P: 3x4 projection matrix
    """
    Rt = np.hstack((R, t.reshape(3, 1)))
    P = K @ Rt
    return P


def dlt_triangulate(P_list, points_list):
    """
    Triangulate a 3D point from multiple 2D projections using DLT.

    Args:
        P_list: List of projection matrices (Nx3x4)
        points_list: List of 2D points (Nx2)

    Returns:
        X: 3D point (3x1)
    """
    num_views = len(P_list)
    A = np.zeros((2 * num_views, 4))

    for i in range(num_views):
        P = P_list[i]
        x, y = points_list[i]

        A[2 * i] = x * P[2] - P[0]
        A[2 * i + 1] = y * P[2] - P[1]

    # Solve for the 3D point using SVD
    _, _, vh = np.linalg.svd(A)
    X = vh[-1]

    # Convert to non-homogeneous coordinates
    X = X[:3] / X[3]

    return X


def dlt_calibration(points_3d, points_2d):
    """
    Calibrate camera using Direct Linear Transformation (DLT) algorithm.

    Args:
        points_3d: Nx3 array of 3D points
        points_2d: Nx2 array of corresponding 2D points

    Returns:
        P: 3x4 projection matrix
    """
    num_points = points_3d.shape[0]
    if num_points < 6:
        raise ValueError(
            "At least 6 point correspondences are required for DLT calibration"
        )

    # Create the design matrix A
    A = np.zeros((2 * num_points, 12))

    for i in range(num_points):
        X, Y, Z = points_3d[i]
        x, y = points_2d[i]

        A[2 * i] = [X, Y, Z, 1, 0, 0, 0, 0, -x * X, -x * Y, -x * Z, -x]
        A[2 * i + 1] = [0, 0, 0, 0, X, Y, Z, 1, -y * X, -y * Y, -y * Z, -y]

    # Solve for P using SVD
    _, _, vh = np.linalg.svd(A)
    P = vh[-1].reshape(3, 4)

    # Normalize P
    P = P / np.linalg.norm(P)

    return P


def compute_reprojection_error(points_3d, points_2d, P):
    """
    Compute reprojection error.

    Args:
        points_3d: Nx3 array of 3D points
        points_2d: Nx2 array of corresponding 2D points
        P: 3x4 projection matrix

    Returns:
        errors: Reprojection errors for each point
    """
    # Convert 3D points to homogeneous coordinates
    points_3d_h = np.hstack((points_3d, np.ones((points_3d.shape[0], 1))))

    # Project 3D points to 2D
    projected = (P @ points_3d_h.T).T
    projected = projected[:, :2] / projected[:, 2:]

    # Compute Euclidean distance between projected and actual 2D points
    errors = np.sqrt(np.sum((projected - points_2d) ** 2, axis=1))

    return errors


def compute_epipolar_lines(points, F, image_shape=None):
    """
    Compute epipolar lines in the second image given points in the first image.

    Args:
        points: Nx2 array of points in the first image
        F: 3x3 fundamental matrix
        image_shape: Optional tuple (height, width) to clip lines to image boundaries

    Returns:
        lines: Nx3 array where each row is (a, b, c) of the line equation ax + by + c = 0
    """
    # Convert points to homogeneous coordinates
    points_h = np.hstack((points, np.ones((points.shape[0], 1))))

    # Compute epipolar lines
    lines = (F @ points_h.T).T

    # Normalize lines
    norms = np.sqrt(lines[:, 0] ** 2 + lines[:, 1] ** 2)
    lines = lines / norms[:, np.newaxis]

    # Clip lines to image boundaries if image_shape is provided
    if image_shape is not None:
        height, width = image_shape
        # For each line, compute the endpoints where it intersects the image boundaries
        # This part is implementation-specific and depends on how you want to use the lines

    return lines
