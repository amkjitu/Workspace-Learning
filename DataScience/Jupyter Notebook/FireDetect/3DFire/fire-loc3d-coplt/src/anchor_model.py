import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class FireAnchorModel(nn.Module):
    """
    Fire detection model based on anchor boxes.
    This model is used to detect fires in images using an anchor-based approach.
    """

    def __init__(self, num_classes=1, input_size=(416, 416), anchors=None):
        """
        Initialize the fire anchor model.

        Args:
            num_classes: Number of classes to detect (default: 1 for fire)
            input_size: Input size for the model (width, height)
            anchors: List of anchor boxes as [(width, height)]
        """
        super(FireAnchorModel, self).__init__()
        self.num_classes = num_classes
        self.input_width, self.input_height = input_size

        # Default anchors if none provided
        if anchors is None:
            # These are example anchors that might work well for fire detection
            # Actual anchors should be derived from the dataset using k-means clustering
            self.anchors = [
                (10, 13),
                (16, 30),
                (33, 23),  # Small fire anchors
                (30, 61),
                (62, 45),
                (59, 119),  # Medium fire anchors
                (116, 90),
                (156, 198),
                (373, 326),  # Large fire anchors
            ]
        else:
            self.anchors = anchors

        # Number of anchors per scale
        self.num_anchors_per_scale = len(self.anchors) // 3

        # Define the backbone (feature extractor)
        self.backbone = self._create_backbone()

        # Define the detection heads (3 scales)
        self.head_s = self._create_detection_head(128, self.num_anchors_per_scale)
        self.head_m = self._create_detection_head(256, self.num_anchors_per_scale)
        self.head_l = self._create_detection_head(512, self.num_anchors_per_scale)

        # Detection layers (output convolutions)
        self.detect_s = self._create_detection_layer(128, self.num_anchors_per_scale)
        self.detect_m = self._create_detection_layer(256, self.num_anchors_per_scale)
        self.detect_l = self._create_detection_layer(512, self.num_anchors_per_scale)

    def _create_backbone(self):
        """Create the backbone feature extractor."""
        # Simple darknet-like backbone
        layers = [
            # Initial convolution
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(0.1),
            # Downsample 1 (416 -> 208)
            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.1),
            # Residual block 1
            nn.Conv2d(64, 32, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(0.1),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.1),
            # Downsample 2 (208 -> 104)
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.1),
            # Residual block 2
            nn.Conv2d(128, 64, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.1),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.1),
            # Downsample 3 (104 -> 52)
            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.1),
            # Residual block 3
            nn.Conv2d(256, 128, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.1),
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.1),
            # Downsample 4 (52 -> 26)
            nn.Conv2d(256, 512, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.1),
            # Residual block 4
            nn.Conv2d(512, 256, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.1),
            nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.1),
        ]
        return nn.Sequential(*layers)

    def _create_detection_head(self, in_channels, num_anchors):
        """Create a detection head for a specific scale."""
        return nn.Sequential(
            nn.Conv2d(
                in_channels,
                in_channels // 2,
                kernel_size=1,
                stride=1,
                padding=0,
                bias=False,
            ),
            nn.BatchNorm2d(in_channels // 2),
            nn.LeakyReLU(0.1),
            nn.Conv2d(
                in_channels // 2,
                in_channels,
                kernel_size=3,
                stride=1,
                padding=1,
                bias=False,
            ),
            nn.BatchNorm2d(in_channels),
            nn.LeakyReLU(0.1),
            nn.Conv2d(
                in_channels,
                in_channels // 2,
                kernel_size=1,
                stride=1,
                padding=0,
                bias=False,
            ),
            nn.BatchNorm2d(in_channels // 2),
            nn.LeakyReLU(0.1),
            nn.Conv2d(
                in_channels // 2,
                in_channels,
                kernel_size=3,
                stride=1,
                padding=1,
                bias=False,
            ),
            nn.BatchNorm2d(in_channels),
            nn.LeakyReLU(0.1),
        )

    def _create_detection_layer(self, in_channels, num_anchors):
        """Create a detection layer (final output)."""
        # Each anchor predicts: [x, y, w, h, objectness, class_prob_1, ..., class_prob_n]
        out_channels = num_anchors * (5 + self.num_classes)
        return nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, padding=0)

    def forward(self, x):
        """Forward pass."""
        # Extract features through backbone
        features = self.backbone(x)

        # Apply detection heads
        head_s_out = self.head_s(features)
        head_m_out = self.head_m(features)
        head_l_out = self.head_l(features)

        # Get detection outputs
        detect_s_out = self.detect_s(head_s_out)
        detect_m_out = self.detect_m(head_m_out)
        detect_l_out = self.detect_l(head_l_out)

        # Reshape detection outputs
        batch_size = x.size(0)
        s_grid = detect_s_out.size(2)  # e.g. 52x52 grid
        m_grid = detect_m_out.size(2)  # e.g. 26x26 grid
        l_grid = detect_l_out.size(2)  # e.g. 13x13 grid

        detect_s_out = detect_s_out.view(
            batch_size, self.num_anchors_per_scale, 5 + self.num_classes, s_grid, s_grid
        )
        detect_s_out = detect_s_out.permute(0, 1, 3, 4, 2).contiguous()

        detect_m_out = detect_m_out.view(
            batch_size, self.num_anchors_per_scale, 5 + self.num_classes, m_grid, m_grid
        )
        detect_m_out = detect_m_out.permute(0, 1, 3, 4, 2).contiguous()

        detect_l_out = detect_l_out.view(
            batch_size, self.num_anchors_per_scale, 5 + self.num_classes, l_grid, l_grid
        )
        detect_l_out = detect_l_out.permute(0, 1, 3, 4, 2).contiguous()

        return detect_s_out, detect_m_out, detect_l_out

    def get_loss(self, predictions, targets):
        """
        Calculate loss for the model.

        Args:
            predictions: Model predictions (outputs from forward pass)
            targets: Ground truth targets

        Returns:
            Total loss value
        """
        # Placeholder for loss calculation
        # In a real implementation, this would calculate box regression loss,
        # objectness loss, and classification loss

        # Example loss calculation:
        loss_box = torch.tensor(0.0)
        loss_obj = torch.tensor(0.0)
        loss_cls = torch.tensor(0.0)

        total_loss = loss_box + loss_obj + loss_cls
        return total_loss

    def predict(self, x, conf_threshold=0.5, nms_threshold=0.4):
        """
        Make predictions and apply non-max suppression.

        Args:
            x: Input tensor of shape (batch_size, 3, height, width)
            conf_threshold: Confidence threshold for detections
            nms_threshold: IoU threshold for NMS

        Returns:
            List of detections as [x1, y1, x2, y2, confidence, class_id]
        """
        # Forward pass
        outputs = self.forward(x)

        # Process outputs and apply NMS
        # This would transform the raw outputs into bounding box predictions
        # and filter them using non-maximum suppression

        # Placeholder for detection processing
        detections = []

        return detections
