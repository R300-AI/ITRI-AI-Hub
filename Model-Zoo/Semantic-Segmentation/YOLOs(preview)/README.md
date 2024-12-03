# About YOLOs

The YOLO family of models referenced in this guide is provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy

In the training demonstration, we can utilized open-source datasets such as COCO8-seg, Crack-seg, and Package-seg. All these datasets are automatically downloaded through the Ultralytics API. You can also create your own custom datasets for training by following the guidelines in the [[Training Notebook]](), and export it by [[Delegating Notebook]](). The following metrics are from previous benchmarks measured based on COCO8-pose, include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>).

|  Model     |  params<sub>(M)     | Time (hr)<br>T4 GPU   |  mAP<sub>50     |  mAP<sub>50-95     |  mAP<sub>50(M)     |  mAP<sub>50-95(M)     | Pre-built Models   |
|------------|-------|-----------------|-----------------|--------------------|--------------------|--------------------|--------------------|
| yolov8n-seg    | 3.4  |             |             |                |    |     |[[ONNX]]() |
| yolov8s-seg    | 11.8 |             |             |                |    |     |[[ONNX]]() |
| yolov8m-seg    | 27.3 |             |             |                |    |     |[[ONNX]]() |
| yolov8l-seg    | 46.0 |             |             |                |    |     |[[ONNX]]() |
| yolov8x-seg    | 71.8 |             |             |                |    |     |[[ONNX]]() |
| yolo11n-seg    | 2.9  |             |             |                |    |     |[[ONNX]]() |
| yolo11s-seg    | 10.1 |             |             |                |    |     |[[ONNX]]() |
| yolo11m-seg    | 22.4 |             |             |                |    |     |[[ONNX]]() |
| yolo11l-seg    | 27.6 |             |             |                |    |     |[[ONNX]]() |
| yolo11x-seg    | 62.1 |             |             |                |    |     |[[ONNX]]() |

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
