from threading import local
import cv2
import time
import numpy as np

# Replace <COMPUTER_IP> with your computer's IP (e.g., '192.168.1.10')
url_cam1 = "http://192.168.0.102:4747/video"
url_cam2 = "http://192.168.0.102:4747/video"
local_cam = 0  # Local camera index (usually 0 for the default camera)


def initialize_camera(source, name="Camera"):
    """Initialize camera with robust settings"""
    cap = cv2.VideoCapture(source)

    # Set buffer size to reduce latency and avoid frame accumulation
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    # Set timeouts for network streams
    if isinstance(source, str) and source.startswith("http"):
        cap.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, 5000)
        cap.set(cv2.CAP_PROP_READ_TIMEOUT_MSEC, 5000)

    if not cap.isOpened():
        print(f"Warning: Could not initialize {name}")
        return None

    print(f"{name} initialized successfully")
    return cap


def reconnect_camera(source, name="Camera"):
    """Attempt to reconnect to a camera"""
    print(f"Attempting to reconnect {name}...")
    return initialize_camera(source, name)


# Initialize video captures with robust settings
cap1 = initialize_camera(url_cam1, "Camera 1 (IP)")
cap2 = initialize_camera(local_cam, "Camera 2 (Local)")

# Check if at least one camera is available
if cap1 is None and cap2 is None:
    print("Error: Could not connect to any cameras.")
    exit()

# Counters for error handling
cam1_error_count = 0
cam2_error_count = 0
MAX_CONSECUTIVE_ERRORS = 10
last_frame1 = None
last_frame2 = None

print("Starting camera feed... Press 'q' to quit, 'r' to reconnect cameras")

while True:
    ret1, frame1 = False, None
    ret2, frame2 = False, None

    # Try to read from Camera 1 (IP camera)
    if cap1 is not None:
        ret1, frame1 = cap1.read()
        if ret1:
            last_frame1 = frame1.copy()
            cam1_error_count = 0
        else:
            cam1_error_count += 1
            print(f"Camera 1 read error ({cam1_error_count}/{MAX_CONSECUTIVE_ERRORS})")

            # Try to reconnect after consecutive errors
            if cam1_error_count >= MAX_CONSECUTIVE_ERRORS:
                print("Too many errors on Camera 1. Attempting reconnection...")
                if cap1 is not None:
                    cap1.release()
                cap1 = reconnect_camera(url_cam1, "Camera 1 (IP)")
                cam1_error_count = 0
                time.sleep(1)  # Wait before next attempt

    # Try to read from Camera 2 (local camera)
    if cap2 is not None:
        ret2, frame2 = cap2.read()
        if ret2:
            last_frame2 = frame2.copy()
            cam2_error_count = 0
        else:
            cam2_error_count += 1
            print(f"Camera 2 read error ({cam2_error_count}/{MAX_CONSECUTIVE_ERRORS})")

            # Try to reconnect after consecutive errors
            if cam2_error_count >= MAX_CONSECUTIVE_ERRORS:
                print("Too many errors on Camera 2. Attempting reconnection...")
                if cap2 is not None:
                    cap2.release()
                cap2 = reconnect_camera(local_cam, "Camera 2 (Local)")
                cam2_error_count = 0
                time.sleep(1)  # Wait before next attempt

    # Display frames (use last good frame if current read failed)
    if ret1 or last_frame1 is not None:
        display_frame1 = frame1 if ret1 else last_frame1
        if display_frame1 is not None:
            # Add status overlay
            status_text = "LIVE" if ret1 else "RECONNECTING"
            color = (0, 255, 0) if ret1 else (0, 0, 255)
            cv2.putText(
                display_frame1,
                status_text,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                2,
            )
            cv2.imshow("Camera 1 (IP)", display_frame1)

    if ret2 or last_frame2 is not None:
        display_frame2 = frame2 if ret2 else last_frame2
        if display_frame2 is not None:
            # Add status overlay
            status_text = "LIVE" if ret2 else "RECONNECTING"
            color = (0, 255, 0) if ret2 else (0, 0, 255)
            cv2.putText(
                display_frame2,
                status_text,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                2,
            )
            cv2.imshow("Camera 2 (Local)", display_frame2)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("r"):
        # Manual reconnection
        print("Manual reconnection triggered...")
        if cap1 is not None:
            cap1.release()
        if cap2 is not None:
            cap2.release()
        cap1 = reconnect_camera(url_cam1, "Camera 1 (IP)")
        cap2 = reconnect_camera(local_cam, "Camera 2 (Local)")
        cam1_error_count = 0
        cam2_error_count = 0

    # If both cameras are completely unavailable, break
    if cap1 is None and cap2 is None:
        print("No cameras available. Exiting...")
        break

    # Small delay to prevent excessive CPU usage
    time.sleep(0.01)

# Cleanup
print("Cleaning up...")
if cap1 is not None:
    cap1.release()
if cap2 is not None:
    cap2.release()
cv2.destroyAllWindows()
print("Camera feed ended.")

#####################################################################
# ## Run this command in Terminal/Command Prompt:
# ## ngrok http http://192.168.0.102:4747

# import cv2
# from google.colab.patches import cv2_imshow
# import numpy as np
# import requests
# from IPython.display import clear_output
# import time

# # Replace with your ngrok URLs (add /video at end)
# url1 = "https://25e1-103-186-57-169.ngrok-free.app/video"
# url2 = "https://25e1-103-186-57-169.ngrok-free.app/video"

# # Initialize captures (use CAP_FFMPEG for better streaming)
# cap1 = cv2.VideoCapture(url1)
# cap2 = cv2.VideoCapture(url2)

# # Verify connections
# if not cap1.isOpened() or not cap2.isOpened():
#     print("Error opening streams. Check URLs and firewall")
#     # Fallback: Try without FFMPEG
#     cap1 = cv2.VideoCapture(url1)
#     cap2 = cv2.VideoCapture(url2)

# # Display loop
# for _ in range(50):  # Show 50 frames
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()

#     if not ret1 or not ret2:
#         print("Frame read error")
#         break

#     # Combine frames horizontally
#     combined = np.hstack((frame1, frame2))

#     # Display in Colab (with clearing previous output)
#     clear_output(wait=True)
#     cv2_imshow(combined)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#     time.sleep(0.05)  # Control frame rate

# cap1.release()
# cap2.release()
# print("Stream ended")
