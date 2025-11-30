# ...existing code...


def associate_across_multiple_views(
    all_detections, fundamental_matrices, max_distance=10.0
):
    """
    Associate detections across multiple camera views.

    Args:
        all_detections: List of detection lists for each camera [cam_idx][detection_idx]
        fundamental_matrices: Dict of fundamental matrices from cam_i to cam_j {(i,j): F_ij}
        max_distance: Maximum allowed epipolar distance

    Returns:
        List of lists, where each inner list contains indices of associated detections
        across cameras [(cam1_idx, det1_idx), (cam2_idx, det2_idx), ...]
    """
    num_cameras = len(all_detections)

    # Initialize association groups
    association_groups = []

    # Start with camera pairs
    for cam_i in range(num_cameras):
        for cam_j in range(cam_i + 1, num_cameras):
            # Skip if either camera has no detections
            if not all_detections[cam_i] or not all_detections[cam_j]:
                continue

            # Get fundamental matrix
            F_ij = fundamental_matrices.get((cam_i, cam_j))
            if F_ij is None:
                continue

            # Associate detections
            matches = associate_detections(
                all_detections[cam_i], all_detections[cam_j], F_ij, max_distance
            )

            # Add to association groups
            for idx_i, idx_j in matches:
                # Create a new group
                group = [(cam_i, idx_i), (cam_j, idx_j)]
                association_groups.append(group)

    # Merge groups with common detections
    merged = True
    while merged:
        merged = False
        i = 0
        while i < len(association_groups):
            j = i + 1
            while j < len(association_groups):
                # Check if groups share any detection
                if any(det in association_groups[j] for det in association_groups[i]):
                    # Merge groups
                    association_groups[i].extend(
                        [
                            det
                            for det in association_groups[j]
                            if det not in association_groups[i]
                        ]
                    )
                    association_groups.pop(j)
                    merged = True
                else:
                    j += 1
            i += 1

    # Verify consistency of each group using epipolar constraints
    consistent_groups = []
    for group in association_groups:
        if len(group) < 2:
            continue

        # Check consistency for each camera pair in the group
        is_consistent = True
        for i, (cam_i, idx_i) in enumerate(group):
            for j, (cam_j, idx_j) in enumerate(group[i + 1 :], i + 1):
                # Skip if fundamental matrix is not available
                F_ij = fundamental_matrices.get((cam_i, cam_j))
                if F_ij is None:
                    continue

                # Get points
                point_i = (
                    all_detections[cam_i][idx_i][0],
                    all_detections[cam_i][idx_i][1],
                )
                point_j = (
                    all_detections[cam_j][idx_j][0],
                    all_detections[cam_j][idx_j][1],
                )

                # Check epipolar distance
                dist_ij = compute_epipolar_distance(point_i, F_ij, point_j)
                dist_ji = compute_epipolar_distance(point_j, F_ij.T, point_i)

                if max(dist_ij, dist_ji) > max_distance:
                    is_consistent = False
                    break

            if not is_consistent:
                break

        if is_consistent:
            consistent_groups.append(group)

    return consistent_groups
