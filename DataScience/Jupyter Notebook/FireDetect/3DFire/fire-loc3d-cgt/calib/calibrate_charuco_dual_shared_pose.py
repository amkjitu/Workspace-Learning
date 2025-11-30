# calib/calibrate_charuco_dual_shared_pose.py
"""
Dual-camera ChArUco shared-pose calibration.

- Uses existing intrinsics (K, dist) for LEFT and RIGHT cameras.
- Captures both RTSP frames "at once" and estimates each camera pose (R, T)
  with respect to the SAME ChArUco board/world frame from the SAME instant.
- Saves cam_left_shared.npz and cam_right_shared.npz with K, dist, R, T, P.

Recommended board (yours):
  squares_x=7, squares_y=5, square_len_mm=30, marker_len_mm=15, aruco_dict=5X5_100

Usage (Windows PowerShell example):
  py -3.10 -m calibrate_charuco_dual_shared_pose `
    --rtsp_left  "rtsp://<LEFT_URL>" `
    --rtsp_right "rtsp://<RIGHT_URL>" `
    --intr_left  calib/cam_left.npz `
    --intr_right calib/cam_right.npz `
    --out_left   calib/cam_left_shared.npz `
    --out_right  calib/cam_right_shared.npz `
    --squares_x  7 --squares_y 5 --square_len_mm 30 --marker_len_mm 15 `
    --aruco_dict 5X5_100 --preview

After success, point your app’s YAML to the *_shared.npz files.

py -3.10 -m calibrate_charuco_dual_shared_pose --rtsp_left "rtsp://admin:L200461B@192.168.0.182:554/cam/realmonitor?channel=1&subtype=0" --rtsp_right "rtsp://admin:L2574467@192.168.0.151:554/cam/realmonitor?channel=1&subtype=0" --intr_left calib/cam_left.npz --intr_right calib/cam_right.npz --out_left calib/cam_left_shared.npz --out_right calib/cam_right_shared.npz --squares_x 7 --squares_y 5 --square_len_mm 30 --marker_len_mm 15 --aruco_dict 5X5_100 --preview

py -3.10 -m calibrate_charuco_dual_shared_pose --rtsp_left "rtsp://admin:L200461B@192.168.0.182:554/cam/realmonitor?channel=1&subtype=0" --rtsp_right "rtsp://admin:L2574467@192.168.0.151:554/cam/realmonitor?channel=1&subtype=0" --squares_x 12 --squares_y 9 --square_len_mm 50 --marker_len_mm 35 --aruco_dict 5X5_100 --preview --recalibrate

"""


import os
import cv2
import numpy as np
import argparse


# -------------------- Utils --------------------
def open_rtsp(url: str) -> cv2.VideoCapture:
    cap = cv2.VideoCapture(
        f"{url}?tcp&fflags=nobuffer&flags=low_delay&max_delay=1", cv2.CAP_FFMPEG
    )
    if not cap.isOpened():
        raise SystemExit(f"[DualPose] Cannot open: {url}")
    try:
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    except Exception:
        pass
    return cap


def sync_grab_retrieve(capL: cv2.VideoCapture, capR: cv2.VideoCapture):
    """Grab both first (to minimize skew), then retrieve."""
    capL.grab()
    capR.grab()
    okL, imL = capL.retrieve()
    okR, imR = capR.retrieve()
    return okL, imL, okR, imR


def split_view(imL, imR, scale=0.75, sep_px=4):
    """Return one canvas showing LEFT | RIGHT with a thin separator."""
    hL, wL = imL.shape[:2]
    hR, wR = imR.shape[:2]
    H = min(hL, hR)
    if hL != H:
        imL = cv2.resize(imL, (int(wL * H / hL), H), interpolation=cv2.INTER_AREA)
    if hR != H:
        imR = cv2.resize(imR, (int(wR * H / hR), H), interpolation=cv2.INTER_AREA)
    sep = np.full((H, sep_px, 3), (40, 40, 40), np.uint8)
    canvas = np.hstack([imL, sep, imR])
    if scale != 1.0:
        canvas = cv2.resize(
            canvas, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA
        )
    return canvas


def aruco_dictionary(name="5X5_100"):
    name = name.strip().upper()
    table = {
        "4X4_50": cv2.aruco.DICT_4X4_50,
        "4X4_100": (
            cv2.aruco.DICT_4X_100
            if hasattr(cv2.aruco, "DICT_4X_100")
            else cv2.aruco.DICT_4X4_100
        ),
        "5X5_50": cv2.aruco.DICT_5X5_50,
        "5X5_100": cv2.aruco.DICT_5X5_100,
        "6X6_50": cv2.aruco.DICT_6X6_50,
        "6X6_100": cv2.aruco.DICT_6X6_100,
        "5X5_1000": cv2.aruco.DICT_5X5_1000,
    }
    if name not in table:
        raise SystemExit(f"[DualPose] Unknown --aruco_dict '{name}'")
    return cv2.aruco.getPredefinedDictionary(table[name])


def draw_detected(
    img,
    corners,
    ids,
    ch_corners,
    ch_ids,
    label,
    K=None,
    dist=None,
    rvec=None,
    tvec=None,
    axis_length=100,
):
    out = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    if ids is not None and len(ids):
        cv2.aruco.drawDetectedMarkers(out, corners, ids)
    if ch_corners is not None and ch_ids is not None and len(ch_ids):
        cv2.aruco.drawDetectedCornersCharuco(out, ch_corners, ch_ids, (255, 255, 0))

    # Draw coordinate axes if pose is available
    if K is not None and dist is not None and rvec is not None and tvec is not None:
        try:
            # Make axes much more visible
            axis_len = axis_length * 3  # Triple the length
            # print(f"[DEBUG] Drawing axes with length {axis_len}, rvec shape: {rvec.shape}, tvec shape: {tvec.shape}")
            if hasattr(cv2, "drawFrameAxes"):
                cv2.drawFrameAxes(out, K, dist, rvec, tvec, axis_len)
                # print(f"[DEBUG] Used cv2.drawFrameAxes")
            elif hasattr(cv2.aruco, "drawAxis"):
                cv2.aruco.drawAxis(out, K, dist, rvec, tvec, axis_len)
                # print(f"[DEBUG] Used cv2.aruco.drawAxis")
            else:
                print(f"[DEBUG] No axis drawing function available")
        except Exception as e:
            print(f"[DEBUG] Failed to draw axes: {e}")
            import traceback

            traceback.print_exc()

    m = 0 if ids is None else len(ids)
    c = 0 if ch_ids is None else len(ch_ids)
    cv2.putText(
        out,
        f"{label}: markers={m} ch={c}",
        (12, 30),
        font,
        0.9,
        (30, 255, 255),
        2,
        cv2.LINE_AA,
    )
    return out


def detector_params():
    # Compatibility across OpenCV builds
    if hasattr(cv2.aruco, "DetectorParameters_create"):
        p = cv2.aruco.DetectorParameters_create()
    else:
        p = cv2.aruco.DetectorParameters()
    p.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_CONTOUR
    # p.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_SUBPIX
    p.cornerRefinementWinSize = 7
    p.adaptiveThreshWinSizeMin = 3
    p.adaptiveThreshWinSizeMax = 53
    p.adaptiveThreshWinSizeStep = 4
    p.adaptiveThreshConstant = 7
    p.minMarkerPerimeterRate = 0.02
    p.maxMarkerPerimeterRate = 4.0
    p.minCornerDistanceRate = 0.04
    return p


# -------------------- Core (same logic as your single) --------------------
def interpolate_charuco(gray, board, dictionary, min_corners=8):
    params = detector_params()
    # Use new API if available
    if hasattr(cv2.aruco, "ArucoDetector"):
        det = cv2.aruco.ArucoDetector(dictionary, params)
        corners, ids, _ = det.detectMarkers(gray)
    else:
        corners, ids, _ = cv2.aruco.detectMarkers(gray, dictionary, parameters=params)
    if ids is None or len(ids) == 0:
        return None, None, None

    # Try interpolation
    ret, ch_corners, ch_ids = cv2.aruco.interpolateCornersCharuco(
        corners, ids, gray, board
    )

    # Debug: print what interpolation returned
    if ret == 0 or ch_ids is None:
        print(
            f"[DEBUG] interpolateCornersCharuco returned ret={ret}, found {0 if ch_ids is None else len(ch_ids)} corners from {len(ids)} markers"
        )

    if not ret or ch_ids is None or len(ch_ids) < min_corners:
        return corners, ids, None
    return corners, ids, (ch_corners, ch_ids)


def estimate_pose_from_charuco(gray, K, dist, board, dictionary):
    corners, ids, ch = interpolate_charuco(gray, board, dictionary)
    if ch is None:
        return None, (corners, ids, None, None, None, None)
    ch_corners, ch_ids = ch
    ok, rvec, tvec = cv2.aruco.estimatePoseCharucoBoard(
        ch_corners, ch_ids, board, K, dist, None, None
    )
    if not ok:
        return None, (corners, ids, ch_corners, ch_ids, None, None)
    R, _ = cv2.Rodrigues(rvec)
    T = tvec.reshape(3, 1)
    P = K @ np.hstack([R, T])
    # mean reprojection error for sanity
    # get board 3D points for the indices we observed
    if hasattr(board, "chessboardCorners"):
        corners_3d = board.chessboardCorners
    else:
        corners_3d = board.getChessboardCorners()
    obj = corners_3d[ch_ids.flatten(), :]
    obj_cam = (R @ obj.T) + T
    proj = (K @ obj_cam).T
    proj = proj[:, :2] / proj[:, 2:3]
    err = float(np.linalg.norm(proj - ch_corners.reshape(-1, 2), axis=1).mean())
    return (R, T, P, err, len(ch_ids), rvec, tvec), (
        corners,
        ids,
        ch_corners,
        ch_ids,
        rvec,
        tvec,
    )


def calibrate_camera_charuco(images_gray, board, dictionary, image_size):
    """Calibrate camera from multiple ChArUco images."""
    all_corners = []
    all_ids = []

    for gray in images_gray:
        corners, ids, ch = interpolate_charuco(gray, board, dictionary, min_corners=4)
        if ch is not None:
            all_corners.append(ch[0])
            all_ids.append(ch[1])

    print(f"[DualPose] Using {len(all_corners)} images for calibration")
    if len(all_corners) < 5:
        return None

    ret, K, dist, rvecs, tvecs = cv2.aruco.calibrateCameraCharuco(
        all_corners, all_ids, board, image_size, None, None
    )

    return K, dist if ret else None


# -------------------- Main --------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rtsp_left", required=True)
    ap.add_argument("--rtsp_right", required=True)
    ap.add_argument("--intr_left", default="calib/cam_left.npz")
    ap.add_argument("--intr_right", default="calib/cam_right.npz")
    ap.add_argument("--out_left", default="calib/cam_left_shared.npz")
    ap.add_argument("--out_right", default="calib/cam_right_shared.npz")
    ap.add_argument("--squares_x", type=int, default=7)
    ap.add_argument("--squares_y", type=int, default=5)
    ap.add_argument("--square_len_mm", type=float, default=30.0)
    ap.add_argument("--marker_len_mm", type=float, default=15.0)
    ap.add_argument("--aruco_dict", default="5X5_100", help="MUST match printed board")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument(
        "--recalibrate",
        action="store_true",
        help="Capture 10+ images to recalibrate intrinsics",
    )
    args = ap.parse_args()

    d = aruco_dictionary(args.aruco_dict)
    # Charuco board (same constructor you used)
    if hasattr(cv2.aruco, "CharucoBoard_create"):
        board = cv2.aruco.CharucoBoard_create(
            args.squares_x, args.squares_y, args.square_len_mm, args.marker_len_mm, d
        )
    else:
        board = cv2.aruco.CharucoBoard(
            (args.squares_x, args.squares_y), args.square_len_mm, args.marker_len_mm, d
        )

    capL, capR = open_rtsp(args.rtsp_left), open_rtsp(args.rtsp_right)

    if args.recalibrate:
        print(
            "[DualPose] RECALIBRATION MODE: Capture 10-15 images from different angles."
        )
        print(
            "[DualPose] Press SPACE to capture each image, ENTER when done, ESC to quit."
        )

        captured_left = []
        captured_right = []
        win = "Dual Calibration (SPACE=capture, ENTER=done, ESC=quit)"
        cv2.namedWindow(win, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(win, 1280, 720)

        while True:
            okL, imL, okR, imR = sync_grab_retrieve(capL, capR)
            if not (okL and okR):
                continue

            gL = cv2.cvtColor(imL, cv2.COLOR_BGR2GRAY)
            gR = cv2.cvtColor(imR, cv2.COLOR_BGR2GRAY)

            cL, iL, chL = interpolate_charuco(gL, board, d)
            cR, iR, chR = interpolate_charuco(gR, board, d)

            visL = draw_detected(
                imL,
                cL,
                iL,
                None if chL is None else chL[0],
                None if chL is None else chL[1],
                f"LEFT [{len(captured_left)}]",
            )
            visR = draw_detected(
                imR,
                cR,
                iR,
                None if chR is None else chR[0],
                None if chR is None else chR[1],
                f"RIGHT [{len(captured_right)}]",
            )
            canvas = split_view(visL, visR, scale=0.75)
            cv2.imshow(win, canvas)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:  # ESC
                capL.release()
                capR.release()
                cv2.destroyAllWindows()
                return
            if k == ord(" "):  # SPACE
                if chL is not None and chR is not None:
                    captured_left.append(gL)
                    captured_right.append(gR)
                    print(f"[DualPose] Captured pair {len(captured_left)}")
                else:
                    nL = 0 if chL is None else len(chL[1])
                    nR = 0 if chR is None else len(chR[1])
                    print(
                        f"[DualPose] Detection failed - LEFT: {nL} corners, RIGHT: {nR} corners (need 4+)"
                    )
            if k == 13:  # ENTER
                if len(captured_left) >= 5:
                    break
                else:
                    print(
                        f"[DualPose] Need at least 5 images, have {len(captured_left)}"
                    )

        print("\n[DualPose] Calibrating cameras...")
        img_size = (gL.shape[1], gL.shape[0])

        result_L = calibrate_camera_charuco(captured_left, board, d, img_size)
        result_R = calibrate_camera_charuco(captured_right, board, d, img_size)

        if result_L is None or result_R is None:
            raise SystemExit(
                "[DualPose] Calibration failed. Try capturing more varied images."
            )

        K_L, dist_L = result_L
        K_R, dist_R = result_R

        # Save intrinsics from recalibration for inspection
        np.savez(args.intr_left, K=K_L, dist=dist_L)
        np.savez(args.intr_right, K=K_R, dist=dist_R)

        print("[DualPose] Calibration successful!")
        print(f"  LEFT  camera matrix:\n{K_L}")
        print(f"  RIGHT camera matrix:\n{K_R}")
        print(f"  LEFT  distortion: {dist_L.ravel()}")
        print(f"  RIGHT distortion: {dist_R.ravel()}")

    else:
        # Load known intrinsics (same format as your single-cam .npz)
        D_L, D_R = np.load(args.intr_left), np.load(args.intr_right)
        K_L, dist_L = D_L["K"], D_L["dist"]
        K_R, dist_R = D_R["K"], D_R["dist"]

    print("[DualPose] Put the ChArUco board FLAT on the FLOOR. Do NOT move it.")
    print("[DualPose] Make the board BIG (≈40–70% width), reduce tilt/glare.")
    print("[DualPose] Press SPACE to capture; ESC to quit.")

    win = "Dual Preview (SPACE=capture, ESC=quit)"
    if args.preview:
        cv2.namedWindow(win, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(win, 1280, 720)

    # ---- Live preview with detections (same logic as single) ----
    while True:
        okL, imL, okR, imR = sync_grab_retrieve(capL, capR)
        if not (okL and okR):
            continue
        if args.preview:
            gL = cv2.cvtColor(imL, cv2.COLOR_BGR2GRAY)
            gR = cv2.cvtColor(imR, cv2.COLOR_BGR2GRAY)

            # Estimate poses for visualization
            poseL_preview, dbgL_preview = estimate_pose_from_charuco(
                gL, K_L, dist_L, board, d
            )
            poseR_preview, dbgR_preview = estimate_pose_from_charuco(
                gR, K_R, dist_R, board, d
            )

            cL, iL, chL_corners, chL_ids, rvecL, tvecL = dbgL_preview
            cR, iR, chR_corners, chR_ids, rvecR, tvecR = dbgR_preview

            visL = draw_detected(
                imL,
                cL,
                iL,
                chL_corners,
                chL_ids,
                "LEFT",
                K_L,
                dist_L,
                rvecL,
                tvecL,
                axis_length=args.square_len_mm,
            )
            # Debug: check what we're passing
            if rvecL is not None:
                print(f"[DEBUG] LEFT has valid pose, rvec shape: {rvecL.shape}")
            else:
                print(f"[DEBUG] LEFT rvec is None")

            visR = draw_detected(
                imR,
                cR,
                iR,
                chR_corners,
                chR_ids,
                "RIGHT",
                K_R,
                dist_R,
                rvecR,
                tvecR,
                axis_length=args.square_len_mm,
            )
            if rvecR is not None:
                print(f"[DEBUG] RIGHT has valid pose, rvec shape: {rvecR.shape}")
            else:
                print(f"[DEBUG] RIGHT rvec is None")

            canvas = split_view(visL, visR, scale=0.75)
            cv2.imshow(win, canvas)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                capL.release()
                capR.release()
                cv2.destroyAllWindows()
                return
            if k == ord(" "):
                break
        else:
            break

    # ---- Capture & estimate on the same instant ----
    print("[DualPose] Processing captured frame...")
    grayL = cv2.cvtColor(imL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imR, cv2.COLOR_BGR2GRAY)

    print("\n[DualPose] CAPTURED! Estimating pose...")

    poseL, dbgL = estimate_pose_from_charuco(grayL, K_L, dist_L, board, d)
    poseR, dbgR = estimate_pose_from_charuco(grayR, K_R, dist_R, board, d)

    # --- Debugging prints ---
    cornersL, idsL, ch_cornersL, ch_idsL, rvecL, tvecL = dbgL
    cornersR, idsR, ch_cornersR, ch_idsR, rvecR, tvecR = dbgR
    markersL = 0 if idsL is None else len(idsL)
    charucoL = 0 if ch_idsL is None else len(ch_idsL)
    markersR = 0 if idsR is None else len(idsR)
    charucoR = 0 if ch_idsR is None else len(ch_idsR)
    print(f"[DualPose] LEFT : Found {markersL} markers -> {charucoL} ChArUco corners.")
    print(f"[DualPose] RIGHT: Found {markersR} markers -> {charucoR} ChArUco corners.")
    # --- End debugging prints ---

    if poseL is None or poseR is None:
        print("[DualPose] Saving debug images to debug_left.png and debug_right.png")
        visL_fail = draw_detected(
            imL, cornersL, idsL, ch_cornersL, ch_idsL, "LEFT (FAIL)"
        )
        visR_fail = draw_detected(
            imR, cornersR, idsR, ch_cornersR, ch_idsR, "RIGHT (FAIL)"
        )
        cv2.imwrite("debug_left.png", visL_fail)
        cv2.imwrite("debug_right.png", visR_fail)

        capL.release()
        capR.release()
        cv2.destroyAllWindows()

        error_msg = "[DualPose] Pose estimation failed for: "
        if poseL is None and poseR is None:
            error_msg += "BOTH cameras"
        elif poseL is None:
            error_msg += "LEFT camera"
        else:
            error_msg += "RIGHT camera"
        error_msg += f". (LEFT: {charucoL} corners, RIGHT: {charucoR} corners)"
        error_msg += "\nMake the board larger, reduce tilt/glare, and try again."

        raise SystemExit(error_msg)

    print("[DualPose] Pose estimation successful!")
    R_L, T_L, P_L, errL, nL = poseL[:5]
    R_R, T_R, P_R, errR, nR = poseR[:5]

    # Validate reprojection errors
    if errL > 5.0 or errR > 5.0:
        print(f"\n[WARNING] High reprojection error detected!")
        print(f"  LEFT:  {errL:.2f}px (threshold: 5.0px)")
        print(f"  RIGHT: {errR:.2f}px (threshold: 5.0px)")
        print(
            f"  This may indicate poor calibration quality or board detection issues."
        )
        print(f"  Consider:")
        print(f"    - Recalibrating with more varied board positions")
        print(f"    - Ensuring board is perfectly flat and well-lit")
        print(f"    - Checking camera focus and reducing motion blur")

        response = input("\nDo you want to save these results anyway? (y/n): ")
        if response.lower() != "y":
            capL.release()
            capR.release()
            cv2.destroyAllWindows()
            return

    # ---- Save extrinsics (board is the shared world) ----
    print(f"[DualPose] Preparing to save files...")
    print(f"  Output LEFT:  {args.out_left}")
    print(f"  Output RIGHT: {args.out_right}")

    # Ensure directory exists only if there's a directory in the path
    out_dir_left = os.path.dirname(args.out_left)
    out_dir_right = os.path.dirname(args.out_right)

    if out_dir_left:  # Only create if there's a directory
        print(f"  Creating directory: {out_dir_left}")
        os.makedirs(out_dir_left, exist_ok=True)
    if out_dir_right and out_dir_right != out_dir_left:
        print(f"  Creating directory: {out_dir_right}")
        os.makedirs(out_dir_right, exist_ok=True)

    print(f"[DualPose] Saving LEFT camera data...")
    np.savez(args.out_left, K=K_L, dist=dist_L, R=R_L, T=T_L, P=P_L)
    print(f"  ✓ Saved: {args.out_left}")

    print(f"[DualPose] Saving RIGHT camera data...")
    np.savez(args.out_right, K=K_R, dist=dist_R, R=R_R, T=T_R, P=P_R)
    print(f"  ✓ Saved: {args.out_right}")

    C_left = (-R_L.T @ T_L).ravel()
    C_right = (-R_R.T @ T_R).ravel()
    baseline = float(np.linalg.norm(C_right - C_left))

    print("[DualPose] Saved shared-pose extrinsics:")
    print(f"  {args.out_left}  | reproj err: {errL:.2f}px on {nL} ch-corners")
    print(f"  {args.out_right} | reproj err: {errR:.2f}px on {nR} ch-corners")
    print(
        f"  Camera centers (world units):\n    C_left  = {C_left}\n    C_right = {C_right}"
    )
    print(f"  Baseline (world units): {baseline:.2f}")
    print(
        "  (If you used mm sizes, set unit_scale_m_per_world_unit: 0.001 in your app.)"
    )

    capL.release()
    capR.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
