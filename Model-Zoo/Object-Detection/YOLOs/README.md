# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy
|  Model     | Prorcess Time (hr)   |  mAP<sub>50     |  mAP<sub>50-95     |
|------------|-----------------|-----------------|--------------------|
| YOLOv5n    ||||
| YOLOv8n    ||||
| YOLO11n    ||||

## Inference Speed 

| Model            | Genio510<br><sub>(Mali GPU) | Genio510<br><sub>(MDLA 3.0) | Genio700<br><sub>(Mali GPU) | Genio700<br><sub>(MDLA 3.0) | Genio1200<br><sub>(Mali GPU) | Genio1200<br><sub>(MDLA 2.0) |
|------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|------------------------|
| YOLOv5n<sub>fp16 |                        |                  |                             |                    |                        |:x:                       |
| YOLOv5n<sub>fp32 |                        |                  |                             |                    |                        |:x:                       |
| YOLOv8n<sub>fp16 |                        |                  |                             |                    |                        |:x:                       |
| YOLOv8n<sub>fp32 |                        |                  |                             |                    |                        |:x:                       |
| YOLO11n<sub>fp16 |                        |                  |                             |                    |                        |:x:                       |
| YOLO11n<sub>fp32 |                        |                  |                             |                    |                        |:x:                       |


#

| APIs   |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN) | [NeuronRT](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT) |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN) | [NeuronRT](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT) |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN) | [NeuronRT](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT) |

|  Device    | Chipset     | API | YOLOv5n<sub>fp16  || YOLOv8n<sub>fp16 | YOLOv8n<sub>fp32 | YOLO11n<sub>fp32  | YOLO11n<sub>fp32 |
|------------|-------------|-------------|--------------------|-------------------|------------------|------------------|-------------------|------------------|
| Genio510   |`Mali GPU`   |        |          |          |          |          |          |          |
| Genio510   |`MDLA 3.0`   |     |          |          |          |          |          |          |
| Genio700   |`Mali GPU`   |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN)        |          |          |          |          |          |          |
| Genio700   |`MDLA 3.0`   |[NeuronRT](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT)     |          |          |          |          |          |          | 
| Genio1200  |`Mali GPU`   |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN)        |          |          |          |          |          |          |
| Genio1200  |`MDLA 2.0`   |NeuronRT     |       |:x:       |:x:       |:x:       |:x:       |:x:       |

## Usage Memory 