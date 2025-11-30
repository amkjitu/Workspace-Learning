import cv2
import numpy as np
import argparse
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils import ensure_directory_exists


def create_charuco_board():
    """Create a ChArUco board for calibration."""
    square_length = 0.04  # 4cm
    marker_length = 0.02  # 2cm
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    board = cv2.aruco.CharucoBoard((7, 5), square_length, marker_length, dictionary)
    return board


def detect_charuco_board(image, board):
    """Detect ChArUco board in an image."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect Aruco markers
    dictionary = board.getDictionary()
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    corners, ids, rejected = detector.detectMarkers(gray)

    # If at least one marker detected
    if ids is not None and len(ids) > 0:
        # Refine detection
        response, charuco_corners, charuco_ids = cv2.aruco.interpolateCornersCharuco(
            corners, ids, gray, board
        )
        return response, charuco_corners, charuco_ids

    return 0, None, None


def calibrate_camera(image_folder, board, image_extension=".jpg"):
    """Calibrate camera using ChArUco board images."""
    print(f"Looking for calibration images in {image_folder}...")

    # Prepare object points and image points
    all_corners = []
    all_ids = []
    image_size = None

    # Process each image in the folder
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(image_extension):
            image_path = os.path.join(image_folder, filename)
            print(f"Processing {filename}")

            # Read the image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Could not read {filename}")
                continue

            # Store image size for calibration
            if image_size is None:
                image_size = (image.shape[1], image.shape[0])

            # Detect ChArUco corners
            response, charuco_corners, charuco_ids = detect_charuco_board(image, board)

            # If detection was successful
            if response > 0:
                all_corners.append(charuco_corners)
                all_ids.append(charuco_ids)

                # Draw detection for visualization
                cv2.aruco.drawDetectedCornersCharuco(
                    image, charuco_corners, charuco_ids
                )
                cv2.putText(
                    image,
                    f"Found {response} corners",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

                cv2.imshow("Detection", image)
                cv2.waitKey(100)

    if not all_corners:
        print("No ChArUco corners detected in any image!")
        return None, None, None, None

    print(f"Calibrating using {len(all_corners)} images...")

    # Calibrate camera
    camera_matrix = np.eye(3)
    dist_coeffs = np.zeros((5, 1))

    flags = (
        cv2.CALIB_RATIONAL_MODEL
        + cv2.CALIB_FIX_ASPECT_RATIO
        + cv2.CALIB_FIX_PRINCIPAL_POINT
    )

    reprojection_error, camera_matrix, dist_coeffs, rvecs, tvecs = (
        cv2.aruco.calibrateCameraCharuco(
            all_corners,
            all_ids,
            board,
            image_size,
            camera_matrix,
            dist_coeffs,
            flags=flags,
        )
    )

    print(f"Calibration complete! Reprojection error: {reprojection_error}")
    return reprojection_error, camera_matrix, dist_coeffs, image_size


def capture_calibration_images(camera_id, output_folder, num_images=20):
    """Capture images from camera for calibration."""
    ensure_directory_exists(output_folder)

    # Create ChArUco board
    board = create_charuco_board()
    board_image = board.generateImage((1000, 800))
    cv2.imwrite(os.path.join(output_folder, "charuco_board.png"), board_image)

    # Open camera
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_id}")
        return False

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    print("Press SPACE to capture an image, ESC to exit")
    image_count = 0

    while image_count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read from camera")
            break

        # Display instructions
        cv2.putText(
            frame,
            f"Captured: {image_count}/{num_images}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )
        cv2.putText(
            frame,
            "SPACE: Capture, ESC: Exit",
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        # Detect board for preview
        response, corners, ids = detect_charuco_board(frame, board)
        if response > 0:
            cv2.aruco.drawDetectedCornersCharuco(frame, corners, ids)
            cv2.putText(
                frame,
                f"Detected {response} corners",
                (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

        # Show the frame
        cv2.imshow("Camera Calibration", frame)
        key = cv2.waitKey(1) & 0xFF

        # Capture image on spacebar
        if key == 32:  # SPACE key
            img_path = os.path.join(output_folder, f"calib_{image_count:02d}.jpg")
            cv2.imwrite(img_path, frame)
            print(f"Saved {img_path}")
            image_count += 1
        # Exit on ESC
        elif key == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()
    return image_count > 0


def main():
    parser = argparse.ArgumentParser(
        description="Camera calibration using ChArUco board"
    )
    parser.add_argument("--camera_id", type=int, default=0, help="Camera ID")
    parser.add_argument(
        "--output", type=str, default="calibration.json", help="Output calibration file"
    )
    parser.add_argument(
        "--image_folder",
        type=str,
        default="",
        help="Folder with existing calibration images",
    )
    parser.add_argument(
        "--num_images", type=int, default=20, help="Number of images to capture"
    )
    args = parser.parse_args()

    # Create calibration directory if it doesn't exist
    calibration_dir = os.path.join(os.path.dirname(__file__), "images")
    ensure_directory_exists(calibration_dir)

    # If image folder not specified, capture new images
    if not args.image_folder:
        camera_folder = os.path.join(calibration_dir, f"camera_{args.camera_id}")
        print(f"Capturing {args.num_images} calibration images...")
        if not capture_calibration_images(
            args.camera_id, camera_folder, args.num_images
        ):
            print("Calibration image capture failed.")
            return
        image_folder = camera_folder
    else:
        image_folder = args.image_folder

    # Create ChArUco board
    board = create_charuco_board()

    # Calibrate camera
    reprojection_error, camera_matrix, dist_coeffs, image_size = calibrate_camera(
        image_folder, board
    )

    if camera_matrix is None:
        print("Calibration failed.")
        return

    # Save calibration data
    calibration_data = {
        "camera_matrix": camera_matrix.tolist(),
        "distortion_coefficients": dist_coeffs.tolist(),
        "image_width": image_size[0],
        "image_height": image_size[1],
        "reprojection_error": float(reprojection_error),
        "calibration_time": "",  # Could add current time here
    }

    with open(args.output, "w") as f:
        json.dump(calibration_data, f, indent=2)

    print(f"Calibration saved to {args.output}")
    print(f"Camera Matrix:\n{camera_matrix}")
    print(f"Distortion Coefficients:\n{dist_coeffs.ravel()}")


if __name__ == "__main__":
    main()
