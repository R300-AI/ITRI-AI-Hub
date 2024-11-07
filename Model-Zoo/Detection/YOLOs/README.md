# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Train/Val Accuracy
## Inference Speed 
|  Device    | Chipset     | Runtime API | YOLOv5nu<sub>fp16<\sub>  | YOLOv5nu<sub>fp32<\sub> | YOLOv8n<sub>fp16<\sub> | YOLOv8n<sub>fp32<\sub> | YOLO11n<sub>fp32<\sub>  | YOLO11n<sub>fp32<\sub> |
|------------|-------------|-------------|----------|----------|----------|----------|----------|----------|----------|
| Genio350   |`Mali GPU`   |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN)        |          |          |          |          |          |          |
| Genio350   |`VPU`        |NeuronRT     |:x:       |:x:       |:x:       |:x:       |:x:       |:x:       |
| Genio510   |`Mali GPU`   |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN)        |          |          |          |          |          |          |
| Genio510   |`MDLA 3.0`   |[NeuronRT](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT)     |          |          |          |          |          |          |
| Genio700   |`Mali GPU`   |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN)        |          |          |          |          |          |          |
| Genio700   |`MDLA 3.0`   |[NeuronRT](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/NeuronRT)     |          |          |          |          |          |          | 
| Genio1200  |`Mali GPU`   |[ArmNN](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs/ArmNN)        |          |          |          |          |          |          |
| Genio1200  |`MDLA 2.0`   |NeuronRT     |:x:       |:x:       |:x:       |:x:       |:x:       |:x:       |

## Usage Memory 
