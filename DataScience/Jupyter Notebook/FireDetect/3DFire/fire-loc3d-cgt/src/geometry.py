import numpy as np


def cam_center(R, T):
    return (-R.T @ T).reshape(3)


def ray_from_pixel(u, v, K, R, T):
    p = np.array([u, v, 1.0])
    d_cam = np.linalg.inv(K) @ p
    d_world = (R.T @ d_cam).ravel()
    C = cam_center(R, T)
    d_world /= np.linalg.norm(d_world) + 1e-12
    return C, d_world


def intersect_plane(C, d, n, b):
    denom = n @ d
    if abs(denom) < 1e-8:
        return None
    lam = -(n @ C + b) / denom
    return C + lam * d


# def triangulate(C1, d1, C2, d2):
#     # closest points between skew rays
#     r = C2 - C1
#     a = d1 @ d1
#     b = d1 @ d2
#     c = d2 @ d2
#     d = d1 @ r
#     e = d2 @ r
#     denom = a * c - b * b
#     if abs(denom) < 1e-10:
#         return None, None
#     t = (b * e - c * d) / denom
#     s = (a * e - b * d) / denom
#     P1 = C1 + t * d1
#     P2 = C2 + s * d2
#     return 0.5 * (P1 + P2), np.linalg.norm(P1 - P2)


def triangulate(C1, d1, C2, d2):
    """
    Robust ray-ray triangulation.
    Returns (midpoint, gap). Never returns None; if nearly parallel,
    gap will be large and caller can reject.
    """
    # Ensure unit directions
    d1 = d1 / (np.linalg.norm(d1) + 1e-12)
    d2 = d2 / (np.linalg.norm(d2) + 1e-12)

    r = C2 - C1
    A = np.column_stack((d1, -d2))  # shape (3,2)
    # Solve A [t s]^T ≈ r in least-squares sense
    ts, *_ = np.linalg.lstsq(A, r, rcond=None)
    t, s = ts[0], ts[1]
    P1 = C1 + t * d1
    P2 = C2 + s * d2
    mid = 0.5 * (P1 + P2)
    gap = float(np.linalg.norm(P1 - P2))
    return mid, gap
