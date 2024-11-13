# Deploy YOLOs on ArmNN (Preview)

ArmNN is an inference engine designed specifically for Cortex-A CPUs and Mali-GPUs. Developers can flexibly use these processors to implement high-performance, low-power deep learning operations without additional conversion work.

To illustrate how to delegate a model in TFLite format, we will use Ultralytics' pre-built YOLOv8n model as an example. The model is trained on the COCO dataset, which includes 80 categories of objects. Please follow the instructions provided in the previous table of contents to obtain the model on your workstation. Then, continue with the steps outlined in this document to complete the Python example to verify the inference results.

### Prerequisites

* Exported **YOLOv8n** model in TFlite format ([[Tutorial]](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs/Delegate_Models_to_ONNX_and_TFLite.ipynb)).
* A **Genio-510/700/1200 EVK (Mali GPU)** board which **ArmNN** Library has been installed.
