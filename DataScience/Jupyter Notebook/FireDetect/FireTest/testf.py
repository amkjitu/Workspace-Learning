import cv2
import torch
from ultralytics import YOLO

# --- Configuration ---
MODEL_PATH = "DataScience/Jupyter Notebook/FireDetect/FireTest/best.pt"
# SOURCE = 0  # 0 for default webcam, or provide a video file path (e.g., 'test_video.mp4')
SOURCE = "rtsp://admin:L200461B@192.168.0.182:554/cam/realmonitor?channel=1&subtype=0"
CONFIDENCE_THRESHOLD = 0.5  # Only show detections above this confidence level

# NOTE: Replace these class names with the actual names your model was trained on.
# Common classes for fire/smoke detection might be:
CLASS_NAMES = ["fire", "smoke"]
# The index in this list (0, 1, ...) must match the class indices in your model's training data.
# For example, if 'fire' was class 0 and 'smoke' was class 1.

# --- 1. Load the Model ---
try:
    # Use YOLO from ultralytics to load the trained PyTorch model
    model = YOLO(MODEL_PATH)
    print(f"✅ Model '{MODEL_PATH}' loaded successfully on device: {model.device}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    print(
        "Please ensure you have the 'ultralytics' library installed and 'best.pt' is a valid YOLO model file."
    )
    exit()

# --- 2. Initialize Video Capture ---
cap = cv2.VideoCapture(SOURCE)
if not cap.isOpened():
    print(
        f"❌ Error: Could not open video source {SOURCE}. Check camera connection or video path."
    )
    exit()

print("🎥 Starting real-time detection. Press 'q' to exit.")

# --- 3. Main Detection Loop ---
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        print("End of stream or read error. Exiting...")
        break

    # --- 4. Run Inference ---
    # The 'stream=True' flag uses a generator for more efficient processing
    results = model(frame, conf=CONFIDENCE_THRESHOLD, verbose=False, stream=True)

    # --- 5. Process and Display Results ---
    for result in results:
        # Get bounding boxes and class IDs
        boxes = (
            result.boxes.xyxy.cpu().numpy().astype(int)
        )  # xmin, ymin, xmax, ymax coordinates
        confs = result.boxes.conf.cpu().numpy()  # Confidence scores
        class_ids = result.boxes.cls.cpu().numpy().astype(int)  # Class indices

        # Loop through each detection
        for box, conf, class_id in zip(boxes, confs, class_ids):
            x1, y1, x2, y2 = box

            # Ensure class_id is valid for the CLASS_NAMES list
            if class_id < len(CLASS_NAMES):
                label = CLASS_NAMES[class_id]
            else:
                label = f"Unknown Class ID: {class_id}"

            confidence_str = f"{conf:.2f}"
            display_text = f"{label}: {confidence_str}"

            # Set color based on detection (Red for Fire, Orange for Smoke)
            color = (0, 0, 255) if label == "fire" else (0, 165, 255)

            # Draw the bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Draw the label background rectangle
            (w, h), _ = cv2.getTextSize(display_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(frame, (x1, y1 - h - 10), (x1 + w, y1), color, -1)

            # Put the text label
            cv2.putText(
                frame,
                display_text,
                (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2,
            )

            # --- ALERTING (Optional but crucial for a complete project) ---
            if label == "fire" and conf >= 0.7:
                # Example: Print a high-priority alert to the console
                print(
                    f"!!! 🔥 HIGH ALERT: FIRE DETECTED at ({x1},{y1}) with {confidence_str} confidence. !!!"
                )
                # In a real system, you would integrate email/SMS/API call here.

    # --- 6. Display the frame ---
    cv2.imshow("Fire and Smoke Detection (Press Q to Quit)", frame)

    # Wait for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# --- 7. Cleanup ---
cap.release()
cv2.destroyAllWindows()
print("🛑 Detection finished and resources released.")
