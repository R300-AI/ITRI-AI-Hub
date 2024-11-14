# About YOLOs

The YOLO family of models referenced in this guide is provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy

For training demonstrations, we use a small open-source dataset of COCO8-pose, Tiger-pose, and Hand-Keypoints that show how to tune different application types. The metrics include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>).

|  Model     | Prorcess Time (hr)<br>T4 GPU   |  mAP<sub>50(B)     |  mAP<sub>50-95(B)     |  mAP<sub>50(P)     |  mAP<sub>50-95(P)     |
|------------|--------------------------------|--------------------------|-----------------------------|--------------------------|-----------------------------|
| YOLOv8n-pose    | 0.073                          | 0.92          | 0.78             | 0.86          | 0.70              |
| YOLO11n-pose    | 0.074                          | 0.91          | 0.78             | 0.88          | 0.70              |

These training sessions were executed on a **CUDA Workstation** equipped with a T4 GPU. To train your own model or reproduce the results above, here we provide instructions to get started:

**Step 1**. Follow this [Installation Guideline](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/workstation.html) to setup CUDA/ROCm for your GPU.

**Step 2**. Create and environment with dependencies on your **Workstation**.

```bash
$ conda create --name ultralytics python=3.11 && conda activate ultralytics
(ultralytics)$ pip install -r requirements.txt
```

**Step 3**. Open **Jupyter Notebook** to execute the training and export sessions.

```bash
$ conda activate ultralytics
(ultralytics)$ jupyter notebook
```

* [Tutorial: How to Train a custom YOLOs?](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Keypoint-Detection/YOLOs/Train_YOLOs_on_Workstation.ipynb)
* [Tutorial" How to Export and Use ONNX (or TFLite) on CPU?](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Keypoint-Detection/YOLOs/Delegate_Models_to_ONNX_and_TFLite.ipynb)

## Inference Speed 

**Deployment Template**: [[HailoRT]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Keypoint-Detection/YOLOs/HailoRT)

| Model               | Genio510<br><sub>Mali GPU | Genio510<br><sub>Hailo-8 | Genio700<br><sub>Mali GPU | Genio700<br><sub>Hailo-8 | Genio1200<br><sub>Mali GPU | Genio1200<br><sub>Hailo-8 |
|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|------------------------|
| YOLOv8n-pose<sub> (fp16) |                       |                       |                       |                       |                        |                     |
| YOLOv8n-pose<sub> (fp32) |                       |                       |                       |                       |                        |                     |
| YOLO11n-pose<sub> (fp16) |                       |                       |                       |                       |                        |                     |
| YOLO11n-pose<sub> (fp32) |                       |                       |                       |                       |                        |                     |
