# Deploy YOLOs on HailoRT (Preview)

HailoRT is an inference engine designed specifically for the Hailo expansion accelerator, providing developers with high-performance, low-power deep learning operations.

To illustrate the process of converting a model from the ONNX format to a Hailo binary file (.hef), we will use the pre-built YOLOv8n-pose model from Ultralytics as an example. The model is trained on the COCO-Pose dataset, which contains 1 class of people with 17 keypoints. Please follow the instructions provided in the previous sections to obtain the model on your workstation, then proceed with the steps outlined in this document to complete the conversion process. Finally, use a simple Python example to verify the accuracy of the inference results.

### Prerequisites

* The **YOLOv8n-pose** model in ONNX format has been exported from [[Previous Directory > Benchmarks > Train/Val Accuracy]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Keypoint-Detection/YOLOs).
* **Ubuntu 22.04 LTS x86_64 Workstation** with **Data-Compiler** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/data-compiler.html))
* A **Evaluation Board (Hailo-8 M.2 expansion)** with **HailoRT** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/hailort.html))

## Convert ONNX to hef on Workstation

```bash
$ source activate ultralytics
(ultralytics)$ pip install -r requirements.txt
```
```bash
(ultralytics)& python pruning_onnx.py
```
```bash
$ source activate data-compiler
(data-compiler)& python parsing_har.py
```

## Deploy Sample Codes on Board
