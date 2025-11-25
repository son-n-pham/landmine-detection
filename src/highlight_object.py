from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

from PIL import Image, ImageDraw, ImageFont


@dataclass
class Detection:
    box_2d: Sequence[int]
    label: str
    score: float | None = None

    @classmethod
    def from_mapping(cls, data: dict) -> "Detection":
        return cls(
            box_2d=data["box_2d"],
            label=data.get("label", ""),
            score=data.get("score"),
        )


def _format_label(d: Detection) -> str:
    if d.score is None:
        return d.label
    return f"{d.label} ({d.score:.2f})"


def draw_detections(
    image_path: str | Path,
    detections: Iterable[Detection],
    output_path: str | Path,
    *,
    box_color: tuple[int, int, int] = (255, 0, 0),
    text_color: tuple[int, int, int] = (255, 255, 255),
    box_width: int = 3,
) -> None:
    """Draw bounding boxes and labels on an image and save it.

    Coordinates in ``box_2d`` are interpreted as [x_min, y_min, x_max, y_max]
    in pixel units on the original image.
    """

    image_path = Path(image_path)
    output_path = Path(output_path)

    with Image.open(image_path).convert("RGB") as im:
        draw = ImageDraw.Draw(im)

        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except OSError:
            font = ImageFont.load_default()

        for det in detections:
            x_min, y_min, x_max, y_max = map(int, det.box_2d)

            # Draw rectangle
            for offset in range(box_width):
                draw.rectangle(
                    [
                        (x_min - offset, y_min - offset),
                        (x_max + offset, y_max + offset),
                    ],
                    outline=box_color,
                )

            # Draw label background + text
            label_text = _format_label(det)
            if label_text:
                bbox = draw.textbbox((0, 0), label_text, font=font)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
                margin = 2
                bg_coords = [
                    (x_min, max(0, y_min - text_h - 2 * margin)),
                    (x_min + text_w + 2 * margin, y_min),
                ]
                draw.rectangle(bg_coords, fill=box_color)
                draw.text(
                    (x_min + margin, bg_coords[0][1] + margin),
                    label_text,
                    fill=text_color,
                    font=font,
                )

        im.save(output_path)


def overlay_from_json_like(
    image_path: str | Path,
    detections_json_like: Sequence[dict],
    output_path: str | Path,
) -> None:
    """Helper that accepts a list of dicts parsed from JSON.

    Example element: {"box_2d": [126, 642, 175, 676], "label": "...", "score": 0.65}
    """

    detections: List[Detection] = [
        Detection.from_mapping(d) for d in detections_json_like
    ]
    draw_detections(image_path, detections, output_path)
