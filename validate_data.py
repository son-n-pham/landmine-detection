import os
import cv2
from pathlib import Path


def validate_dataset(data_dir):
    """
    Validates images and labels in a YOLO dataset structure.
    """
    img_dir = Path(data_dir) / "images"
    label_dir = Path(data_dir) / "labels"

    # Supported extensions
    img_exts = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

    print(f"Checking dataset in: {data_dir}")

    for img_path in img_dir.rglob("*"):
        if img_path.suffix.lower() not in img_exts:
            continue

        # 1. Check Image Integrity
        img = cv2.imread(str(img_path))
        if img is None:
            print(f"[CORRUPT] Could not read image: {img_path}")
            # Optional: os.remove(img_path)
            continue

        # 2. Check Label Existence
        # Assumes label has same name as image but .txt extension
        label_path = label_dir / img_path.with_suffix(".txt").name

        if not label_path.exists():
            print(f"[MISSING LABEL] No text file for: {img_path.name}")
            continue

        # 3. Check for Empty Labels
        # Note: Empty files are valid in YOLO (background images),
        # but this alerts you if it was unintentional.
        if label_path.stat().st_size == 0:
            print(f"[EMPTY LABEL] Label file is empty: {label_path.name}")

    print("Validation complete.")


# Usage
# Structure should be: dataset/train/images and dataset/train/labels
if __name__ == "__main__":
    validate_dataset("dataset/train")
    validate_dataset("dataset/valid")
