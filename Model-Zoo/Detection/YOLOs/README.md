# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks

## Speed 
|  Device    | Chipset     | Runtime API | YOLOv8n       |
|------------|-------------|-------------|-------------|
| Genio350   |`Mali GPU`   |ArmNN        ||
| Genio350   |`VPU`        |NeuronRT     |:x:|
| Genio510   |`Mali GPU`   |ArmNN        ||
| Genio510   |`MDLA 3.0`   |NeuronRT     ||
| Genio700   |`Mali GPU`   |ArmNN        ||
| Genio700   |`MDLA 3.0`   |NeuronRT     ||
| Genio1200  |`Mali GPU`   |ArmNN        ||
| Genio1200  |`MDLA 2.0`   |NeuronRT     |:x:|

## Memory 
|  Device    | Chipset     | Runtime API | YOLOv8n       |
|------------|-------------|-------------|-------------|
| Genio350   |`Mali GPU`   |ArmNN        ||
| Genio350   |`VPU`        |NeuronRT     |:x:|
| Genio510   |`Mali GPU`   |ArmNN        ||
| Genio510   |`MDLA 3.0`   |NeuronRT     ||
| Genio700   |`Mali GPU`   |ArmNN        ||
| Genio700   |`MDLA 3.0`   |NeuronRT     ||
| Genio1200  |`Mali GPU`   |ArmNN        ||
| Genio1200  |`MDLA 2.0`   |NeuronRT     |:x:|
