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

| Model            | Device | Genio510<sub>Mali GPU | Genio510<sub>MDLA 3.0 | Genio700<sub>Mali GPU | Genio700<sub>MDLA 3.0 | Genio1200<sub>Mali GPU | Genio1200<sub>MDLA 3.0 |
|                  |        |                        |                  |                             |                    |                        |                       |
| YOLOv5n<sub>fp16 |        |                        |                  |                             |                    |                        |                       |
| YOLOv5n<sub>fp32 |        |                        |                  |                             |                    |                        |                       |
| YOLOv8n<sub>fp16 |        |                        |                  |                             |                    |                        |                       |
| YOLOv8n<sub>fp32 |        |                        |                  |                             |                    |                        |                       |
| YOLO11n<sub>fp16 |        |                        |                  |                             |                    |                        |                       |
| YOLO11n<sub>fp32 |        |                        |                  |                             |                    |                        |                       |

## Usage Memory 
