import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import cv2
import numpy as np
import argparse
import yaml
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
from PIL import Image

from anchor_model import FireAnchorModel
from utils import ensure_directory_exists


class FireDataset(Dataset):
    """Dataset for fire detection."""

    def __init__(self, img_dir, label_dir, img_size=(416, 416), transform=None):
        """
        Initialize the fire dataset.

        Args:
            img_dir: Directory containing images
            label_dir: Directory containing labels (YOLO format)
            img_size: Input image size for the model (width, height)
            transform: Image transformations
        """
        self.img_dir = img_dir
        self.label_dir = label_dir
        self.img_size = img_size
        self.transform = transform

        # Get all image files
        self.img_files = [
            f for f in os.listdir(img_dir) if f.endswith((".jpg", ".jpeg", ".png"))
        ]

    def __len__(self):
        """Return the number of images in the dataset."""
        return len(self.img_files)

    def __getitem__(self, idx):
        """Get an item from the dataset."""
        img_path = os.path.join(self.img_dir, self.img_files[idx])

        # Load image
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Get original dimensions
        orig_h, orig_w = img.shape[:2]

        # Resize image
        img = cv2.resize(img, self.img_size)

        # Apply transformations if any
        if self.transform:
            img = self.transform(img)
        else:
            # Convert to tensor and normalize
            img = img.transpose(2, 0, 1) / 255.0  # HWC to CHW, 0-255 to 0-1
            img = torch.from_numpy(img).float()

        # Load labels (if available)
        label_file = os.path.splitext(self.img_files[idx])[0] + ".txt"
        label_path = os.path.join(self.label_dir, label_file)

        labels = []
        if os.path.exists(label_path):
            with open(label_path, "r") as f:
                for line in f:
                    # Each line: class x_center y_center width height
                    # Values are normalized [0-1]
                    values = line.strip().split()
                    if len(values) == 5:
                        class_id = int(values[0])
                        x_center = float(values[1])
                        y_center = float(values[2])
                        width = float(values[3])
                        height = float(values[4])

                        # Append the label
                        labels.append([class_id, x_center, y_center, width, height])

        # Convert labels to tensor
        labels = torch.tensor(labels)

        return img, labels


def train(model, train_loader, optimizer, device, epoch, total_epochs, log_interval=10):
    """Train the model for one epoch."""
    model.train()
    running_loss = 0.0

    pbar = tqdm(
        enumerate(train_loader),
        total=len(train_loader),
        desc=f"Epoch {epoch}/{total_epochs}",
    )

    for batch_idx, (data, targets) in pbar:
        # Move data to device
        data = data.to(device)
        targets = targets.to(device)

        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(data)

        # Calculate loss
        loss = model.get_loss(outputs, targets)

        # Backward pass and optimize
        loss.backward()
        optimizer.step()

        # Update running loss
        running_loss += loss.item()

        # Log progress
        if batch_idx % log_interval == 0:
            avg_loss = running_loss / (batch_idx + 1)
            pbar.set_postfix({"Loss": f"{avg_loss:.4f}"})

    return running_loss / len(train_loader)


def validate(model, val_loader, device):
    """Validate the model."""
    model.eval()
    val_loss = 0.0

    with torch.no_grad():
        for data, targets in tqdm(val_loader, desc="Validation"):
            # Move data to device
            data = data.to(device)
            targets = targets.to(device)

            # Forward pass
            outputs = model(data)

            # Calculate loss
            loss = model.get_loss(outputs, targets)

            # Update validation loss
            val_loss += loss.item()

    return val_loss / len(val_loader)


def plot_losses(train_losses, val_losses, save_path):
    """Plot and save the loss curves."""
    plt.figure(figsize=(10, 6))
    plt.plot(train_losses, label="Training Loss")
    plt.plot(val_losses, label="Validation Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Training and Validation Loss")
    plt.legend()
    plt.savefig(save_path)
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Train Fire Detection Model")
    parser.add_argument(
        "--train_dir", type=str, required=True, help="Directory with training images"
    )
    parser.add_argument(
        "--train_labels", type=str, required=True, help="Directory with training labels"
    )
    parser.add_argument(
        "--val_dir", type=str, required=True, help="Directory with validation images"
    )
    parser.add_argument(
        "--val_labels", type=str, required=True, help="Directory with validation labels"
    )
    parser.add_argument(
        "--epochs", type=int, default=100, help="Number of epochs to train"
    )
    parser.add_argument("--batch_size", type=int, default=16, help="Batch size")
    parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")
    parser.add_argument("--img_size", type=int, default=416, help="Input image size")
    parser.add_argument(
        "--output_dir", type=str, default="./outputs", help="Output directory"
    )
    parser.add_argument("--config", type=str, default=None, help="Configuration file")
    args = parser.parse_args()

    # Create output directory
    ensure_directory_exists(args.output_dir)

    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Load configuration
    config = {}
    if args.config and os.path.exists(args.config):
        with open(args.config, "r") as f:
            config = yaml.safe_load(f)

    # Create datasets
    train_dataset = FireDataset(
        img_dir=args.train_dir,
        label_dir=args.train_labels,
        img_size=(args.img_size, args.img_size),
    )

    val_dataset = FireDataset(
        img_dir=args.val_dir,
        label_dir=args.val_labels,
        img_size=(args.img_size, args.img_size),
    )

    # Create data loaders
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=4,
        pin_memory=True,
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=4,
        pin_memory=True,
    )

    # Create model
    model = FireAnchorModel(
        num_classes=1, input_size=(args.img_size, args.img_size)  # Just fire class
    )
    model = model.to(device)

    # Create optimizer
    optimizer = optim.Adam(model.parameters(), lr=args.lr)

    # Create scheduler
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode="min", factor=0.1, patience=10, verbose=True
    )

    # Train the model
    train_losses = []
    val_losses = []
    best_val_loss = float("inf")

    for epoch in range(1, args.epochs + 1):
        # Train
        train_loss = train(model, train_loader, optimizer, device, epoch, args.epochs)
        train_losses.append(train_loss)

        # Validate
        val_loss = validate(model, val_loader, device)
        val_losses.append(val_loss)

        # Update scheduler
        scheduler.step(val_loss)

        # Print epoch summary
        print(
            f"Epoch {epoch}/{args.epochs} - Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}"
        )

        # Save model if validation loss improved
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(
                model.state_dict(), os.path.join(args.output_dir, "best_model.pt")
            )
            print(f"Saved best model with validation loss: {val_loss:.4f}")

        # Save checkpoint
        if epoch % 10 == 0:
            torch.save(
                {
                    "epoch": epoch,
                    "model_state_dict": model.state_dict(),
                    "optimizer_state_dict": optimizer.state_dict(),
                    "train_loss": train_loss,
                    "val_loss": val_loss,
                },
                os.path.join(args.output_dir, f"checkpoint_epoch_{epoch}.pt"),
            )

    # Save final model
    torch.save(model.state_dict(), os.path.join(args.output_dir, "final_model.pt"))

    # Plot losses
    plot_losses(
        train_losses, val_losses, os.path.join(args.output_dir, "loss_curves.png")
    )

    print("Training completed!")


if __name__ == "__main__":
    main()
