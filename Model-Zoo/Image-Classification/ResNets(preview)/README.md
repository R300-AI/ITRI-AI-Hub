# About ResNet

The ResNet family of models referenced in this guide are provided by Torchvision. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the BSD 3-Clause license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Training/Performance Evaluation

|  Model     |  Input Size         |  params (M)         | Time (hr)<br>T4 GPU   |  Accuracy  | Pre-built Models   |
|------------|---------------------|---------------------|-----------------------|------------|--------------------|
| resnet18         |224  | 11.7         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnet18.onnx)          |
| resnet34         |224  | 21.8         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnet34.onnx)          |
| resnet50         |224  | 25.5         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnet50.onnx)          |
| resnet101        |224  | 44.5         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnet101.onnx)          |
| resnet152        |224  | 60.2         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnet152.onnx)          |
| resnext50_32x4d  |224  | 25.0         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnext50_32x4d.onnx)          |
| resnext101_32x8d |224  | 88.8         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnext101_32x8d.onnx)          |
| resnext101_64x4d |224  | 83.4         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/resnext101_64x4d.onnx)          |
| wide_resnet50_2  |224  | 68.9         |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/wide_resnet50_2.onnx)          |
| wide_resnet101_2 |224  | 126.8        |                       |            |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Image-Classification/ResNets/wide_resnet101_2.onnx)          |


## Memory Usage
## Power Consumption
