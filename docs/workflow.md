## Workflow:

1. Data: Run validate_data.py to clean data. Setup data.yaml.
2. Setup: Run uv init, uv add ultralytics opencv-python.
3. Train: Run train.py. It auto-saves best.pt. Monitor for overfitting (Validation Loss should decrease).
4. Inference: Run predict.py to visualize results on new data.

## Project Structure:
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
├── pyproject.toml             # Project settings (managed by uv)
├── uv.lock                    # Dependency lock file (managed by uv)
├── validate_data.py           # Phase 1: Script to check data integrity
├── train.py                   # Phase 3: Script to train the model
├── predict.py                 # Phase 4: Script to run inference
└── test_image.jpg             # A sample image to test prediction