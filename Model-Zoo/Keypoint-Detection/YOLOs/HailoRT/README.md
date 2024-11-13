# Deploy YOLOs on HailoRT (Preview)

HailoRT is an inference engine designed specifically for the Hailo expansion accelerator, providing developers with high-performance and low-power deep learning operations.

To illustrate the process of delegating a model from the ONNX format to a Hailo binary file (.hef), we will use Ultralytics' pre-built YOLOv8n-pose model as an example. The model is trained on the COCO-Pose dataset, which contains 1 class of people with 17 keypoints. Please follow the instructions provided in the previous table of contents to obtain the model on your workstation, then proceed with the steps outlined in this document to complete the conversion process. Finally, a simple Python example is used to verify the accuracy of the inference results.
