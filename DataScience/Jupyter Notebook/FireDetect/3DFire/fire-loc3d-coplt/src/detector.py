import torch
import torch.nn as nn
import cv2
import numpy as np
from PIL import Image
import torchvision.transforms as transforms


class FireDetector:
    """Fire detector using YOLOv5 model."""

    def __init__(
        self,
        model_path,
        device="cuda" if torch.cuda.is_available() else "cpu",
        conf_thres=0.5,
        iou_thres=0.45,
    ):
        """
        Initialize the fire detector.

        Args:
            model_path: Path to the YOLOv5 model weights
            device: Device to run inference on ('cuda' or 'cpu')
            conf_thres: Confidence threshold for detections
            iou_thres: IoU threshold for NMS
        """
        self.device = device
        self.conf_threshold = conf_thres
        self.iou_threshold = iou_thres

        # Load model
        try:
            self.model = torch.hub.load(
                "ultralytics/yolov5", "custom", path=model_path, device=self.device
            )
        except Exception as e:
            print(f"Error loading model: {e}")
            print("Trying alternative loading method...")
            # Fallback to local model if torch hub fails
            import sys
            import os

            # Add the yolov5 directory to path
            sys.path.append(os.path.join(os.path.dirname(__file__), "..", "yolov5"))
            from models.experimental import attempt_load

            self.model = attempt_load(model_path, device=self.device)

        # Set model parameters
        self.model.conf = self.conf_threshold
        self.model.iou = self.iou_threshold

        print(f"Fire detector initialized on {self.device}")

    def preprocess_image(self, image):
        """
        Preprocess image for the model.

        Args:
            image: OpenCV image in BGR format

        Returns:
            Processed image ready for inference
        """
        # If image is already a torch tensor, return it
        if isinstance(image, torch.Tensor):
            return image

        # Convert BGR to RGB
        if isinstance(image, np.ndarray) and image.shape[2] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Use the model's built-in preprocessing
        return image

    def detect(self, image):
        """
        Detect fires in an image.

        Args:
            image: Input image (numpy array in BGR format or torch tensor)

        Returns:
            List of detections, each with [x1, y1, x2, y2, confidence, class_id]
        """
        # Preprocess image
        processed_image = self.preprocess_image(image)

        # Run inference
        with torch.no_grad():
            results = self.model(processed_image)

        # Extract detections (convert from torch to numpy)
        detections = results.pandas().xyxy[0]

        # Format as [x1, y1, x2, y2, confidence, class_id]
        formatted_detections = []
        for _, detection in detections.iterrows():
            x1, y1, x2, y2 = (
                detection["xmin"],
                detection["ymin"],
                detection["xmax"],
                detection["ymax"],
            )
            confidence = detection["confidence"]
            class_id = detection["class"]
            formatted_detections.append([x1, y1, x2, y2, confidence, class_id])

        return formatted_detections

    def draw_detections(self, image, detections):
        """
        Draw detection boxes on image.

        Args:
            image: OpenCV image in BGR format
            detections: List of [x1, y1, x2, y2, confidence, class_id]

        Returns:
            Image with drawn detections
        """
        image_copy = image.copy()

        for x1, y1, x2, y2, confidence, class_id in detections:
            # Convert coordinates to integers
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Draw bounding box
            cv2.rectangle(image_copy, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # Draw label and confidence
            label = f"Fire: {confidence:.2f}"
            (text_width, text_height), _ = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1
            )
            cv2.rectangle(
                image_copy,
                (x1, y1 - text_height - 4),
                (x1 + text_width, y1),
                (0, 0, 255),
                -1,
            )
            cv2.putText(
                image_copy,
                label,
                (x1, y1 - 2),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1,
            )

        return image_copy

    def get_center_points(self, detections):
        """
        Get center points of all detections.

        Args:
            detections: List of [x1, y1, x2, y2, confidence, class_id]

        Returns:
            List of [cx, cy, confidence, class_id]
        """
        centers = []
        for x1, y1, x2, y2, confidence, class_id in detections:
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            centers.append([cx, cy, confidence, class_id])

        return centers
