from src.highlight_object import overlay_from_json_like

# Update these paths if your image lives elsewhere
INPUT_IMAGE = r"data\\field.JPG"  # original JPG
OUTPUT_IMAGE = r"data\\field_boxed.JPG"  # output with overlay


detections = [
    # {"box_2d": [126, 642, 175, 676], "label": "Suspected Landmine/UXO", "score": 0.92}
    {"box_2d": [408, 314, 424, 330], "label": "Suspected Landmine", "score": 0.85}
]


def main() -> None:
    overlay_from_json_like(INPUT_IMAGE, detections, OUTPUT_IMAGE)


if __name__ == "__main__":
    main()
