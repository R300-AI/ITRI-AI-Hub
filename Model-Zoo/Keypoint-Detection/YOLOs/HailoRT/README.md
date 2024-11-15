# Deploy YOLOs on HailoRT (Preview)

HailoRT is an inference engine designed specifically for the Hailo expansion accelerator, providing developers with high-performance, low-power deep learning operations.

To illustrate the process of converting a model from the ONNX format to a Hailo binary file (.hef), we will use the pre-built YOLOv8n-pose model from Ultralytics as an example. The model is trained on the COCO-Pose dataset, which contains 1 class of people with 17 keypoints. Please follow the instructions provided in the previous sections to obtain the model on your workstation, then proceed with the steps outlined in this document to complete the conversion process. Finally, use a simple Python example to verify the accuracy of the inference results.

### Prerequisites

* The **YOLOv8n-pose** model in ONNX(`opset=11`) format has been exported by Ultralytics.
* **Ubuntu 22.04 LTS x86_64 Workstation** with **Data-Compiler** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/data-compiler.html))
* A **Evaluation Board (Hailo-8 M.2 expansion)** with **HailoRT** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/hailort.html))

## Convert ONNX to hef on Workstation

if you do not install ultralytics, please follow the instruction previous directory
```bash
$ source activate ultralytics
(ultralytics)& python pruning_onnx.py --model_name <name_of_onnx_file>
```
```bash
$ source activate data-compiler
(data-compiler)& python parsing_har.py
```

## Deploy Sample Codes on Board
```bash
$ source activate hailort
(hailort)& python run_hailo.py
```
