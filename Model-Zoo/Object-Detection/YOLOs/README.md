# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy

For training demonstration purposes, we utilized a small-scale [HardHat](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/datasets/HardHat_Dataset.YOLO.zip
) dataset, which includes three categories: person, hat, and head. This dataset consists of a total of 100 samples, partitioned into 70 for training, 20 for testing, and 10 for validation. 

These training was executed on a **CUDA** workstation equipped with a T4 GPU, and the metrics include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>).

|  Model     | Prorcess Time (hr)<br>T4 GPU   |  mAP<sub>50     |  mAP<sub>50-95     |
|------------|--------------------------------|-----------------|--------------------|
| YOLOv5n    |0.072                           |0.63             | 0.45               |
| YOLOv8n    |0.065                           |0.63             | 0.44               |
| YOLO11n    ||||

## Inference Speed 

**Demo**: [[ArmNN]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN) | [[NeuronRT]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT)

| Model            | Genio510<br><sub>Mali GPU | Genio510<br><sub>MDLA 3.0 | Genio700<br><sub>Mali GPU | Genio700<br><sub>MDLA 3.0 | Genio1200<br><sub>Mali GPU | Genio1200<br><sub>MDLA 2.0 |
|------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|------------------------|
| YOLOv5n<sub> (fp16) |                        |                  |                             |                    |                        |:x:                       |
| YOLOv5n<sub> (fp32) |                        |                  |                             |                    |                        |:x:                       |
| YOLOv8n<sub> (fp16) |                        |                  |                             |                    |                        |:x:                       |
| YOLOv8n<sub> (fp32) |                        |                  |                             |                    |                        |:x:                       |
| YOLO11n<sub> (fp16) |                        |                  |                             |                    |                        |:x:                       |
| YOLO11n<sub> (fp32) |                        |                  |                             |                    |                        |:x:                       |

## Memory Usage
