from ultralytics import YOLO


def train_model():
    # 1. Load the model
    # 'yolo11n.pt' is the Nano version (fastest).
    # Use 'yolo11s.pt', 'yolo11m.pt', 'yolo11l.pt', 'yolo11x.pt' for higher accuracy.
    model = YOLO("yolo11n.pt")

    # 2. Train
    results = model.train(
        data="data.yaml",
        epochs=100,  # Maximum epochs
        imgsz=640,  # Image resolution
        batch=16,  # Batch size (reduce if you run out of GPU memory)
        patience=10,  # Early Stopping: Stop if no improvement for 10 epochs
        save=True,  # Save checkpoints
        device=0,  # Use 0 for GPU, 'cpu' for CPU
        # --- Augmentation Hyperparameters ---
        mosaic=1.0,  # Probability of Mosaic (0.0 - 1.0)
        close_mosaic=10,  # Turn off mosaic for the last 10 epochs (improves precision)
        # --- Overfitting Controls ---
        # If overfitting (Training Loss Low, Val Loss High):
        # 1. Increase weight_decay (e.g., 0.0005 -> 0.001)
        # 2. Increase dropout (e.g., 0.0 -> 0.1 or 0.2)
        weight_decay=0.0005,
        dropout=0.0,
    )

    print("Training Complete. Best model saved at:", results.save_dir)


if __name__ == "__main__":
    train_model()
