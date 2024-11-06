# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Prepare 

### YOLOv8n
|  Device    | Chipsets    | ArmNN |  NeuronRT<sub>  |
|------------|-------------|-------------|------------------|
| Genio350   |`Mali-G`||:x:|
| Genio350   |`MT83`  ||:x:|
| Genio510   |`Mali-G`|||
| Genio510   |`MT83`  |||
| Genio700   |`Mali-G`|||
| Genio700   |`MT83`  |||
| Genio1200  |`Mali-G`|||
| Genio1200  |`MT8395`||:x:|

#### Support Metric

|          | Genio 350          | Genio 510          | Genio 700          | Genio 1200         |
|----------|--------------------|--------------------|--------------------|--------------------|
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: |                 |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |
