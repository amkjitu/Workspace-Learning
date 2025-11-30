"""
py -3.10 -m  calibrate_charuco_single --rtsp "rtsp://admin:L200461B@192.168.0.182:554/cam/realmonitor?channel=1&subtype=1" --out cam_left.npz
"""

"""
https://docs.opencv.org/4.x/da/d0d/tutorial_camera_calibration_pattern.html
"""
import cv2
import numpy as np
import argparse
import time


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rtsp", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--squares_x", type=int, default=12)
    ap.add_argument("--squares_y", type=int, default=9)
    ap.add_argument("--square_len_mm", type=float, default=50.0)
    # ap.add_argument("--marker_len_mm", type=float, default=22.0)
    ap.add_argument("--marker_len_mm", type=float, default=35.0)
    args = ap.parse_args()

    cap = cv2.VideoCapture(args.rtsp, cv2.CAP_FFMPEG)
    # d = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    d = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
    board = cv2.aruco.CharucoBoard(
        (args.squares_x, args.squares_y), args.square_len_mm, args.marker_len_mm, d
    )
    all_corners, all_ids, imgsz = [], [], None
    print(
        "[Charuco] Press SPACE to capture a frame with clear board; press q to finish."
    )
    while True:
        ok, img = cap.read()
        if not ok:
            break
        imgsz = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = cv2.aruco.detectMarkers(gray, d)
        disp = cv2.aruco.drawDetectedMarkers(img.copy(), corners, ids)
        cv2.imshow("charuco", disp)
        k = cv2.waitKey(1) & 0xFF
        if k == ord(" "):
            if ids is None or len(ids) == 0:
                print("No markers.")
                continue
            ret, ch_corners, ch_ids = cv2.aruco.interpolateCornersCharuco(
                corners, ids, gray, board
            )
            if ret and ch_ids is not None and len(ch_ids) > 8:
                all_corners.append(ch_corners)
                all_ids.append(ch_ids)
                print(f"Captured {len(all_corners)}")
        elif k == ord("q"):
            break
    cv2.destroyAllWindows()
    cap.release()
    if len(all_corners) < 10:
        raise SystemExit("Need >=10 good captures.")

    # Calibrate intrinsics
    ret, K, dist, _, _ = cv2.aruco.calibrateCameraCharuco(
        charucoCorners=all_corners,
        charucoIds=all_ids,
        board=board,
        imageSize=(imgsz[1], imgsz[0]),
        cameraMatrix=None,
        distCoeffs=None,
    )

    # Estimate extrinsics on the last frame
    ok, img = cv2.VideoCapture(args.rtsp).read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(gray, d)
    ret, ch_corners, ch_ids = cv2.aruco.interpolateCornersCharuco(
        corners, ids, gray, board
    )
    # retval, rvec, tvec = cv2.aruco.estimatePoseCharucoBoard(
    #     ch_corners, ch_ids, board, K, dist
    # )
    retval, rvec, tvec = cv2.aruco.estimatePoseCharucoBoard(
        ch_corners, ch_ids, board, K, dist, None, None
    )
    if not retval:
        raise SystemExit("Pose estimation failed—ensure the board is visible and flat.")
    R, _ = cv2.Rodrigues(rvec)
    T = tvec.reshape(3, 1)
    # Build P = K [R|T]
    P = K @ np.hstack([R, T])
    np.savez(args.out, K=K, dist=dist, R=R, T=T, P=P, img_size=(imgsz[0], imgsz[1]))
    print(f"[OK] Saved {args.out}")


if __name__ == "__main__":
    main()
