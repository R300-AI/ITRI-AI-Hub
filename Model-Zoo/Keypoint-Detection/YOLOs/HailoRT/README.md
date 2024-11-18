# Deploy YOLOs on HailoRT (Preview)

HailoRT is an inference engine designed specifically for the Hailo expansion accelerator, providing developers with high-performance, low-power deep learning operations.

Currently, we only support the YOLOv8 series Pose (Keypoints) models on Hailo-8. Before deployment, we need to export the PyTorch model to an ONNX file with `opset=11`, and then use the Data-Compiler to quantize and calibrate the model into a Hailo binary file (.hef). During this process, you will also need to extract a portion of images from your training dataset as calibration samples to prevent accuracy degradation due to quantization.

This document will guide you through this process and successfully recognize an image on Hailo-8. Please follow the instructions provided in the previous sections to obtain the Ultralytics pre-trained PyTorch model (`yolov8n-pose.pt`) on the COCO-pose dataset, which contains 1 class of people with 17 keypoints, and then proceed with the steps outlined in this document to complete the task.


### Prerequisites

* The **YOLOv8n-pose** model in ONNX(`opset=11`) format has been exported by Ultralytics.
* **Ubuntu 22.04 LTS x86_64 Workstation** with **Data-Compiler** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/data-compiler.html))
* A **Evaluation Board (Hailo-8 M.2 expansion)** with **HailoRT** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/hailort.html))

## Convert ONNX to hef on Workstation

Pruning the model into accelerable and non-acceleratable parts through ONNX. .if you don't have `ultralytics` environment, please follow the instruction [previous](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Keypoint-Detection/YOLOs) directory to build it.
```bash
$ source activate ultralytics
(ultralytics)& python pruning_onnx.py --model_name <name_of_onnx_file>
```
Parsing the model, and move this directory with the hef model to the evaluation board.
```bash
$ source activate data-compiler
(data-compiler)& python parsing_har.py
```

## Deploy Sample Codes on Evaluation Board
```bash
$ source activate hailort
(hailort)& python run_hailo.py
```
