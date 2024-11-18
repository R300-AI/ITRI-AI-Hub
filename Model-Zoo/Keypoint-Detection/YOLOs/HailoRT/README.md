# Deploy YOLOs on HailoRT (Preview)

HailoRT is an inference engine designed specifically for the Hailo expansion accelerator, providing developers with high-performance, low-power deep learning operations.

Currently, we only support the YOLOv8 series Pose (Keypoints) models on Hailo-8. Before deployment, we need to export the PyTorch model to an ONNX file with `opset=11`, and then use the Data-Compiler to quantize and calibrate the model into a Hailo binary file (.hef). During this process, you will also need to extract a portion of images from your training dataset as calibration samples to prevent accuracy degradation due to quantization.

This document will guide you through this process and successfully recognize an image on Hailo-8. Please follow the instructions provided in the previous sections to obtain the Ultralytics pre-trained PyTorch model (`yolov8n-pose.pt`) on the COCO-pose dataset, which contains 1 class of people with 17 keypoints, and then proceed with the steps outlined in this document to complete the task.


### Prerequisites

* The **YOLOv8n-pose** model in ONNX(`opset=11`) format has been exported by Ultralytics.
* **Ubuntu 22.04 LTS x86_64 Workstation** with **Data-Compiler** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/data-compiler.html))
* A **Evaluation Board (Hailo-8 M.2 expansion)** with **HailoRT** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/hailort.html))

## Convert ONNX to hef on Workstation

* If you need to customise a paragraph for acceleration, you can use [Netron](https://netron.app/) to view the workflow of the model and fill in the desired `<model_name>` and corresponding `<end_nodes>` into `./config.yaml` file to complete the initial setup.
  > **Note**: *Reshape* is only supported for use ‘between the Conv and Dense layers’ and is not supported for use in the final stage, in which case it is recommended that you specify the area in the red box below as the end_node to avoid errors.

<div align="center">
  <img src="https://github.com/R300-AI/ITRI-AI-Hub/blob/main/assets/images/end_node.png" width="900"/>
</div>

* Pruning the model into accelerable and non-acceleratable parts through ONNX. .if you don't have `ultralytics` environment, please follow the instruction [previous](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Keypoint-Detection/YOLOs) directory to build it.
  ```bash
  $ source activate ultralytics
  (ultralytics)& python pruning_onnx.py --model_name <model_name>
  ```
  
* Parse the front-end acceleratable model , and move this directory with the `.hef` (front) model and `.onnx` (end) model to the evaluation board.
  ```bash
  $ source activate data-compiler
  (data-compiler)& python parsing_har.py --model_name <model_name>
  ```

## Deploy Sample Codes on Evaluation Board
* Before you start running the demo, we recommend you to maximise the **CPU Frequency Setting** tool (e.g. [cpupower-gui](https://launchpad.net/ubuntu/+source/cpupower-gui)) to ensure Hailo is running correctly.
<div align="center">
  <img src="https://github.com/R300-AI/ITRI-AI-Hub/blob/main/assets/images/cpu-frequency-setting.png" width="600"/>
</div>

* Run
```bash
$ source activate hailort
(hailort)& python run_hailo.py --model_name <model_name>
```
