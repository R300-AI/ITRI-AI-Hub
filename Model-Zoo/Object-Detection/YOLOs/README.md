# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy

For training demonstration purposes, we utilized a small-scale [HardHat](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/datasets/HardHat_Dataset.YOLO.zip
) dataset, which includes three categories: person, hat, and head. This dataset consists of a total of 100 samples, partitioned into 70 for training, 20 for testing, and 10 for validation. The metrics include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>)

|  Model     | Prorcess Time (hr)<br>T4 GPU   |  mAP<sub>50     |  mAP<sub>50-95     |
|------------|--------------------------------|-----------------|--------------------|
| YOLOv5n    |0.072                           |0.63             | 0.45               |
| YOLOv8n    |0.065                           |0.63             | 0.44               |
| YOLO11n    |0.077                           |0.77             | 0.51               |

These training sessions were executed on a **CUDA** workstation equipped with a T4 GPU. To train your own model or reproduce the results above, please follow the instructions below:


**Step 1**. Follow this [Installation Guideline](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/workstation/cuda.html) to setup CUDA on your T4 GPU workstation.

**Step 2**. Create a virtual environment for the PyTorch/Ultralytics framework.
```bash
$ conda create --name ultralytics python=3.11
$ source activate ultralytics
```
```bash
(ultralytics)$ pip install -r requirements.txt
```

**Step 3**. Open **Jupyter Notebook** to run the training scripts.
  ```bash
  (ultralytics)$ jupyter notebook
  ```

* [Tutorial: How to Train a custom YOLOs?](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs/Train_YOLOs_on_Workstation.ipynb)
* [Tutorial" How to Export and Use ONNX (or TFLite) on CPU?](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs/Delegate_Models_to_ONNX_and_TFLite.ipynb)

## Inference Speed 

**Deployment Template**: [[ArmNN]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN) | [[NeuronRT]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT)

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
