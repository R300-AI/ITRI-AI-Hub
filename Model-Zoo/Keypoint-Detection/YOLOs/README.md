# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy


For training demonstration purposes, we utilized a small-scale [HardHat-Pose](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/datasets/HardHat_Pose_Dataset.YOLO.zip) dataset, which includes one categories: person with 17 body keypoints. This dataset consists of a total of 100 samples, partitioned into 70 for training, 20 for testing, and 10 for validation. The metrics include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>)

These training was executed on a **CUDA** workstation equipped with a T4 GPU. You can set up your own workstation by following the guidelines in [Developer Zone](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/workstation/cuda.html).

|  Model     | Prorcess Time (hr)<br>T4 GPU   |  mAP<sub>50(B)     |  mAP<sub>50-95(B)     |  mAP<sub>50(P)     |  mAP<sub>50-95(P)     |
|------------|--------------------------------|--------------------------|-----------------------------|--------------------------|-----------------------------|
| YOLOv8n-pose    | 0.073                          | 0.92          | 0.78             | 0.86          | 0.70              |
| YOLO11n-pose    | 0.074                          | 0.91          | 0.78             | 0.88          | 0.70              |

* [Tutorial: How to Train a custom YOLOs?]()
* [Tutorial" How to Export and Use ONNX (or TFLite) on CPU?](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Keypoint-Detection/YOLOs/Delegate_Models_to_ONNX_and_TFLite.ipynb)

## Inference Speed 

**Deployment Template**: [[HailoRT]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Keypoint-Detection/YOLOs/HailoRT)

| Model               | Genio510<br><sub>Mali GPU | Genio510<br><sub>Hailo-8 | Genio700<br><sub>Mali GPU | Genio700<br><sub>Hailo-8 | Genio1200<br><sub>Mali GPU | Genio1200<br><sub>Hailo-8 |
|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|------------------------|
| YOLOv8n-pose<sub> (fp16) |                       |                       |                       |                       |                        |                     |
| YOLOv8n-pose<sub> (fp32) |                       |                       |                       |                       |                        |                     |
| YOLO11n-pose<sub> (fp16) |                       |                       |                       |                       |                        |                     |
| YOLO11n-pose<sub> (fp32) |                       |                       |                       |                       |                        |                     |
