# About ResNet

The ResNet family of models referenced in this guide are provided by Torchvision. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the BSD 3-Clause license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Training/Performance Evaluation

|  Model     |  Input Size         |  params (M)         | Time (hr)<br>T4 GPU   |  Accuracy  | Pre-built Models   |
|------------|---------------------|---------------------|-----------------------|------------|--------------------|
| resnet18         |244  | 11.7                 |                       |            |[[ONNX]]()          |
| resnet34         |244  | 21.8                 |                       |            |[[ONNX]]()          |
| resnet50         |244  | 25.5                 |                       |            |[[ONNX]]()          |
| resnet101        |244  | 44.5                |                       |            |[[ONNX]]()          |
| resnet152        |244  | 60.2                |                       |            |[[ONNX]]()          |
| resnext50_32x4d  |244  | 25.0          |                       |            |[[ONNX]]()          |
| resnext101_32x8d |244  | 88.8         |                       |            |[[ONNX]]()          |
| resnext101_64x4d |244  | 83.4         |                       |            |[[ONNX]]()          |
| wide_resnet50_2  |244  | 68.9          |                       |            |[[ONNX]]()          |
| wide_resnet101_2 |244  | 126.8        |                       |            |[[ONNX]]()          |


## Memory Usage
## Power Consumption
