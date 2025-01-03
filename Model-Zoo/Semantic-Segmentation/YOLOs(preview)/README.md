# About YOLOs

The YOLO family of models referenced in this guide is provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Training/Performance Evaluation

In the training demonstration, we can utilized open-source datasets such as COCO8-seg, Crack-seg, and Package-seg. All these datasets are automatically downloaded through the Ultralytics API. You can also create your own custom datasets for training by following the guidelines in the [[Training Notebook]](), and export it by [[Delegating Notebook]](). The following metrics are from previous benchmarks measured based on **COCO8-seg**, include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>).

|  Model     |  Input Size     |  params<sub>(M)     | Time (hr)<br>T4 GPU   |  mAP<sub>50     |  mAP<sub>50-95     |  mAP<sub>50(M)     |  mAP<sub>50-95(M)     | Pre-built Models   |
|------------|------------|-------|-----------------|-----------------|--------------------|--------------------|--------------------|--------------------|
| yolov8n-seg    |640 | 3.4  |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolov8n-seg.onnx) |
| yolov8s-seg    |640 | 11.8 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolov8s-seg.onnx) |
| yolov8m-seg    |640 | 27.3 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolov8m-seg.onnx) |
| yolov8l-seg    |640 | 46.0 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolov8l-seg.onnx) |
| yolov8x-seg    |640 | 71.8 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolov8x-seg.onnx) |
| yolo11n-seg    |640 | 2.9  |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolo11n-seg.onnx) |
| yolo11s-seg    |640 | 10.1 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolo11s-seg.onnx) |
| yolo11m-seg    |640 | 22.4 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolo11m-seg.onnx) |
| yolo11l-seg    |640 | 27.6 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolo11l-seg.onnx) |
| yolo11x-seg    |640 | 62.1 |             |             |                |    |     |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Instance-Segmentation/YOLOs/yolo11x-seg.onnx) |

These training sessions were executed on a **CUDA Workstation** equipped with a T4 GPU. To train your own model or reproduce the results above, here we provide instructions to get started:

**Step 1**. Clone expected **Jupyter Notebook** to your Workstation.

* [How to setup GPU for your own workstation?](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/workstation.html)

**Step 2**. Create an environment and install dependencies.

```bash
$ conda create --name ultralytics python=3.11 && conda activate ultralytics
(ultralytics)$ pip install -r requirements.txt
```

**Step 3**. Open **Jupyter Notebook** to execute the training and export sessions.

```bash
$ conda activate ultralytics
(ultralytics)$ jupyter notebook
```

## Inference Speed 

| Model/Chipset               | Genio510<br><sub>KleidiAI | Genio510<br><sub>Hailo-8 | Genio700<br><sub>KleidiAI | Genio700<br><sub>Hailo-8 | Genio1200<br><sub>KleidiAI | Genio1200<br><sub>Hailo-8 |
|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|------------------------|
| yolov8n-seg<sub> (fp32) |                       |                       |                       |                       |                        |             |

## Memory Usage
## Power Consumption
