import cv2
from ultralytics import YOLO


def run_inference(image_path, model_path):
    # 1. Load the trained model
    model = YOLO(model_path)

    # 2. Run prediction
    # conf=0.5 ensures we only see detections with >50% confidence
    results = model.predict(source=image_path, conf=0.5, save=False)

    # 3. Load image for drawing
    image = cv2.imread(image_path)
    result = results[0]  # Get first result (since we only passed one image)

    # 4. Iterate through detections and draw
    for box in result.boxes:
        # Get coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Get confidence and class info
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        label_name = model.names[cls_id]

        # Draw Rectangle (Green)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Draw Label Background
        label_text = f"{label_name} {conf:.2f}"
        (w, h), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(image, (x1, y1 - 20), (x1 + w, y1), (0, 255, 0), -1)

        # Draw Text (White)
        cv2.putText(
            image,
            label_text,
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1,
        )

    # 5. Show or Save result
    cv2.imshow("Detections", image)
    cv2.imwrite("output_prediction.jpg", image)

    print("Press any key to close window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Update path to where your training script saved the model
    # Usually: runs/detect/train/weights/best.pt
    run_inference("test_image.jpg", "runs/detect/train/weights/best.pt")
