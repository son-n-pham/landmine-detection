# Landmine Detection Datasets

This document lists available datasets for landmine detection, including optical, thermal, and hyperspectral imagery from various sources.

## Academic & Research Datasets

### MineInsight: A Multi-sensor Dataset for Humanitarian Demining Robotics in Off-Road Environments
- **Paper:** [arXiv:2506.04842v1](https://arxiv.org/html/2506.04842v1)
- **Repository:** [GitHub](https://github.com/mariomlz99/MineInsight)
- Remarks from Son Pham: Don't use it as our objective is to detect landmines from drone.

### A UAV-Based VNIR Hyperspectral Benchmark Dataset for Landmine and UXO Detection
- **Paper:** [arXiv:2510.02700](https://www.arxiv.org/pdf/2510.02700)
- **Download:** [Google Drive](https://drive.google.com/drive/folders/1h91SUWjbSjwiETcw7U9IiCBURKFGe5IJ?usp=sharing)

### Drone Thermographic Dataset
- **Link:** [IEEE Xplore](https://ieeexplore.ieee.org/document/11008598)

### DETECTING PFM-1 LANDMINES
- **Project:** [de-mine.com](https://www.de-mine.com/project-pfm-1-landmines)

### Test Images of Buried Landmines
- **Link:** [Mendeley Data](https://data.mendeley.com/datasets/732ngnf4r3/4)

### Standard Dataset: Vision-Based Remote Sensing Imagery
- **Description:** Vision-Based Remote Sensing Imagery Datasets From Benkovac Landmine Test Site Using An Autonomous Drone For Detecting Landmine Locations.
- **Access:** [IEEE Dataport](https://ieee-dataport.org/documents/vision-based-remote-sensing-imagery-datasets-benkovac-landmine-test-site-using-autonomous#files) (Subscription required)

---

## Roboflow Datasets

These datasets are hosted on Roboflow and are suitable for training object detection models (e.g., YOLO, Faster R-CNN).

### Major Datasets

#### MineGuard-Thermal (by dronecv)
- **Description:** The largest dataset found in this category, specifically focused on thermal imaging for landmine detection. Contains over 3,000 images and includes a pre-trained model.
- **Link:** [MineGuard-Thermal](https://universe.roboflow.com/dronecv/mineguard-thermal)

#### landmine_detection(Orignal_FYP) (by AbbasAliGulzari)
- **Description:** A significant dataset with nearly 3,000 images, likely created for a Final Year Project (FYP). Strong candidate for optical landmine detection.
- **Link:** [landmine_detection](https://universe.roboflow.com/abbasaligulzari/landmine_detection-orignal_fyp)

#### Landmine Detection (by Muhammad Ali)
- **Description:** A large general-purpose dataset containing over 2,000 images. Used to train Faster RCNN models.
- **Link:** [Landmine Detection](https://universe.roboflow.com/muhammad-ali-ktjjq/landmine-detection-p7hwv)

#### Landmines detection dataset (by Northumbria)
- **Description:** High-quality dataset with approximately 1,194 images. Includes a deployed model for immediate testing.
- **Link:** [Landmines detection dataset](https://universe.roboflow.com/northumbria/landmines-detection-dataset)

### Additional Datasets

These datasets are useful for specific niches (like anti-personnel mines) or for augmenting larger training sets.

| Dataset Name | Author | Images (approx) | Description | Link |
|--------------|--------|-----------------|-------------|------|
| **Detection_Landmines** | Angiespace | 989 | | [Link](https://universe.roboflow.com/angiespace/detection_landmines) |
| **Landmine detection** | Second Paper | 925 | | [Link](https://universe.roboflow.com/second-paper/landmine-detection-vfihn) |
| **Legbreaker2** | Angiespace | 910 | Focuses on "legbreaker" anti-personnel mines | [Link](https://universe.roboflow.com/angiespace/legbreaker2) |
| **Alter_Minas** | Minas Dataset | 400 | | [Link](https://universe.roboflow.com/minas-dataset/alter_minas) |
| **Minen** | Alexander | 167 | | [Link](https://universe.roboflow.com/alexander/minen) |
| **Minas-Detección** | Minas Dataset | 100 | | [Link](https://universe.roboflow.com/minas-dataset/minas-deteccion) |
| **Infrarouge-Mines** | Deminage | 57 | Specialized infrared dataset | [Link](https://universe.roboflow.com/deminage/infrarouge-mines) |
| **Detect Land** | Pixels | 26 | | [Link](https://universe.roboflow.com/pixels/detect-land) |
