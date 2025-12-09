# 9-Dec-2025

## What I did:
- Downloaded three datasets from Roboflow for initial experiments. Used the latest dataset to set up the data pipeline, train the model, and run inference.
<img width="1591" height="197" alt="image" src="https://github.com/user-attachments/assets/d9e2d5f0-78a7-4a4a-8429-7fcbe41395fd" />
- Restructured the entire repository to better manage both the code and datasets.
<br>
<img width="215" height="521" alt="image" src="https://github.com/user-attachments/assets/696f3adc-1910-4413-b788-c61ce145a298" />
<br>
- Prepared all Python scripts for data validation, model training, and prediction using the trained YOLOv11 model.

## Next Steps
- Add code to process input images while preserving quality for training and prediction. This may include implementing a tiling strategy.
- Test the training and prediction scripts to evaluate and quantify performance.

## Consideration:
- Develop functionality to robustly merge additional datasets with the current one to improve model quality.
- Review the progress report from a Curtin student working on a similar project to extract lessons learned and apply them to this project.

# 2-Dec-2025:
- Go through the datasets listed in dataset.md to identify the most suitable ones for initial experiments.
- Focus on datasets that provide UAV imagery, both optical and thermal.

Good dataset:
## A UAV-Based VNIR Hyperspectral Benchmark Dataset for Landmine and UXO Detection:
    - 20GB dataset with hyperspectral images captured from UAVs.
    - Download link: [Google Drive](https://drive.google.com/drive/folders/1h91SUWjbSjwiETcw7U9IiCBURKFGe5IJ?usp=sharing)

    Here’s a clear summary of the dataset and how to handle it:

***

### ✅ **Dataset Summary**

*   **Name:** UAV-Based VNIR Hyperspectral Dataset for Landmine & UXO Detection
*   **Purpose:** Benchmark for humanitarian demining research.
*   **Content:**
    *   **Hyperspectral image cube** (ENVI format):
        *   Dimensions: **3123 × 6631 × 272** (rows × columns × spectral bands)
        *   Wavelength range: **398–1002 nm** (Visible + Near-Infrared)
        *   File size: \~21 GB
    *   **Header file (.hdr):** Metadata (dimensions, wavelengths, data type).
    *   **Color file (.cff):** ENVI visualization settings.
    *   **Spectral\_Signatures\_of\_Targets folder:** Ground-truth spectra for all targets (landmines, UXOs, calibration panels).
*   **Ground-truth info:** GPS coordinates for 143 targets, calibration panels, and GCPs for georeferencing.

***

### ✅ **How to Handle It**

#### **1. Viewing and Basic Analysis**

*   Use **ENVI** or **QGIS**:
    *   Open the `.hdr` file → loads the hyperspectral cube.
    *   Visualize RGB composites, zoom into targets, extract spectra.

#### **2. Python Workflow**

*   Install **Spectral Python (SPy)**:

```python
import spectral as spy

# Load hyperspectral image
img = spy.open_image('elm_corrected_vnir.hdr')
print(img.shape)  # (3123, 6631, 272)

# Extract spectrum for a pixel
spectrum = img[1500, 3000]
spy.plot_spectrum(spectrum)
```

#### **3. Linking Targets**

*   Use provided GPS coordinates + GCPs to map targets to pixel positions.
*   Tools: **QGIS**, **GDAL**, or Python libraries like **rasterio**.

#### **4. Machine Learning / Detection**

*   Create labeled datasets:
    *   Extract spectra for known targets (from coordinates).
    *   Use reference signatures for validation.
*   Apply algorithms for classification or anomaly detection.

***

### ✅ **Key Considerations**

*   **Large size (21 GB):** Requires sufficient RAM and disk space.
*   **Format:** ENVI is widely supported in remote sensing tools.
*   **Spectral richness:** 272 bands → ideal for material identification.

## Detection of “legbreaker” antipersonnel landmines by analysis of aerial thermographic images of the soil
- **Link:** https://www.sciencedirect.com/science/article/pii/S2352340923005437
- Small enough dataset to have the quick start. Looks like it is a popular dataset and there would be some pre-trained model available for transfer learning.
- Pretrained model link:
https://ieeexplore.ieee.org/document/11008598
https://github.com/JeiGeek/ThermalMineDetector

## Roboflow datasets
- Advantage: Labelled datasets ready for object detection model training (YOLO, Faster R-CNN, etc)


### https://universe.roboflow.com/dronecv/mineguard-thermal/model/5
