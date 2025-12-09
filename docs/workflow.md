## Workflow:

1. Data: Run `uv run python validate_data.py` to clean data. Setup data.yaml.
2. Setup: Run `uv init`, `uv add ultralytics opencv-python`.
3. Train: Run `uv run python train.py`. It auto-saves best.pt. Monitor for overfitting (Validation Loss should decrease).
4. Inference: Run `uv run python predict.py` to visualize results on new data.

## Project Structure:

```text
project-root/
     ├── .venv/                     # Virtual environment (created by uv)
     ├── dataset/                   # YOUR DATA GOES HERE
     │   ├── train/
     │   │   ├── images/            # Training images (.jpg, .png)
     │   │   └── labels/            # Training labels (.txt)
     │   ├── valid/
     │   │   ├── images/            # Validation images
     │   │   └── labels/            # Validation labels
     │   └── test/                  # (Optional) Testing images
     │       ├── images/
     │       └── labels/
     ├── runs/                      # AUTO-GENERATED during training
     │   └── detect/
     │       └── train/             # Contains logs and models
     │           ├── weights/
     │           │   ├── best.pt    # <--- The model used for Phase 4
     │           │   └── last.pt
     │           └── args.yaml
     ├── data.yaml                  # Dataset configuration file
     └── ...
```