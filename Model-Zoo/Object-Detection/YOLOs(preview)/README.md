# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy

In the training demonstration, we can utilized open-source datasets such as COCO8, Objects365, LVIS...etc. All these datasets are automatically downloaded through the Ultralytics API. You can also create your own custom datasets for training by following the guidelines in the [[Tutorial 1]](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs/Train_YOLOs_on_Workstation.ipynb). The following metrics are from previous benchmarks measured based on COCO8, include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>).

|  Model     |  params<sub>(M)     | Time (hr)<br>T4 GPU   |  mAP<sub>50     |  mAP<sub>50-95     | Pre-built Models   |
|------------|-------|-----------------------|-----------------|--------------------|--------------------|
| yolov5nu    |1.06  |0.072                  |0.63             | 0.45               |[[ONNX]() |
| yolov5su    |1.27  |                       |                 |                    |[[ONNX]() |
| yolov5mu    |1.86  |                       |                 |                    |[[ONNX]() |
| yolov5lu    |2.50  |                       |                 |                    |[[ONNX]() |
| yolov5xu    |3.81  |                       |                 |                    |[[ONNX]() |
| yolov8n     |3.2   |0.065                  |0.63             | 0.44               |[[ONNX]() |
| yolov8s     |11.2  |                       |                 |                    |[[ONNX]() |
| yolov8m     |25.9  |                       |                 |                    |[[ONNX]() |
| yolov8l     |43.7  |                       |                 |                    |[[ONNX]() |
| yolov8x     |68.2  |                       |                 |                    |[[ONNX]() |
| YOLO11n     |2.6   |0.077                  |0.77             | 0.51               |[[ONNX]() |
| yolo11s     |9.4   |                       |                 |                    |[[ONNX]() |
| yolo11m     |20.1  |                       |                 |                    |[[ONNX]() |
| yolo11l     |25.3  |                       |                 |                    |[[ONNX]() |
| yolo11x     |56.9  |                       |                 |                    |[[ONNX]() |












These training sessions were executed on a **CUDA Workstation** equipped with a T4 GPU. To train your own model or reproduce the results above, here we provide instructions to get started:

**Step 1**. Follow this [Installation Guideline](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/workstation.html) to setup CUDA/ROCm for your GPU.

**Step 2**. Create an environment with dependencies on your **Workstation**.

```bash
$ conda create --name ultralytics python=3.11 && conda activate ultralytics
(ultralytics)$ pip install -r requirements.txt
```

**Step 3**. Open **Jupyter Notebook** to execute the training and export sessions.

```bash
& conda activate ultralytics
(ultralytics)$ jupyter notebook
```

* [Tutorial: How to Train a custom YOLOs?](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs/Train_YOLOs_on_Workstation.ipynb)
* [Tutorial: How to Export and Use ONNX (or TFLite) on CPU?](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs/Delegate_Models_to_ONNX_and_TFLite.ipynb)

## Inference Speed 

**Deployment Template**: [[KleidiAI]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Object-Detection/YOLOs/KleidiAI) | [[NeuronRT]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT)

| Model               | Genio510<br><sub>Mali GPU | Genio510<br><sub>MDLA 3.0 | Genio700<br><sub>Mali GPU | Genio700<br><sub>MDLA 3.0 | Genio1200<br><sub>Mali GPU | Genio1200<br><sub>MDLA 2.0 |
|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|------------------------|
| YOLOv5n<sub> (fp16) |                       |                       |                       |                       |                        |:x:                     |
| YOLOv5n<sub> (fp32) |                       |                       |                       |                       |                        |:x:                     |
| YOLOv8n<sub> (fp16) |                       |                       |                       |                       |                        |:x:                     |
| YOLOv8n<sub> (fp32) |                       |                       |                       |                       |                        |:x:                     |
| YOLO11n<sub> (fp16) |                       |                       |                       |                       |                        |:x:                     |
| YOLO11n<sub> (fp32) |                       |                       |                       |                       |                        |:x:                     |

## Memory Usage
## Power Consumption
