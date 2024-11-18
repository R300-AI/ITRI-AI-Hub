# Deploy YOLOs on Kleidi AI (Preview)

ArmNN is an inference engine designed specifically for Cortex-A CPUs and Mali GPUs. Developers can use these processors flexibly to implement high-performance, low-power deep learning operations without additional conversion work.

To illustrate how to delegate a model in TFLite format, we will use the pre-built YOLOv8n model from Ultralytics as an example. The model is trained on the COCO dataset, which includes 80 categories of objects. Please follow the instructions provided in the previous sections to obtain the model on your workstation. Then, continue with the steps outlined in this document to complete the Python example and verify the inference results.

### Prerequisites

* The **YOLOv8n** model in `ONNX` format has been exported from [[Previous Directory > Benchmarks > Train/Val Accuracy]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Object-Detection/YOLOs).
* An **Evaluation Board (Mali GPU)** with **ArmNN** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/armnn.html))

