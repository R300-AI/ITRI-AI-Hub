## Model Summary
* **Benchmark Dataset**: MobileNet v1
* **Input Size**: 1x3x244x244
  | Model Name  |**acc@1**    | **acc@5** | **Params**   | **GFLOPS**  | **Memory**  |    **Delegated Model**     |
  |   -------   |   -------   |   -----   |   ---------  |  ---------  |  --------   |   ----------------------   |
  | **ResNet18**         |69.7        | 89.0        | 11.6B   | 1.81        | 71 MB   | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet18.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet18.tflite) |
  | **ResNet34**         |73.3        | 91.0        | 21.7B   | 3.66        | 124 MB | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet34.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet34.tflite) |
  | **ResNet50**         |76.1        | 92.8        | 25.5B   | 4.09        | 231 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet50.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet50.tflite) |
  | **ResNet101**        |77.3        | 93.5        | 44.5B   |7.80         | 361 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet101.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet101.tflite) |
  | **ResNet152**        |78.3        | 94.0        | 60.1B   | 11.51       | 503 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet152.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnet152.tflite) |
  | **ResNeXt50**        | 77.6       | 93.6        | 25.0B   | 4.23        | 269 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnext50_32x4d.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnext50_32x4d.tflite) |
  | **ResNeXt101_32**    | 79.3       | 94.5        | 88.7B   | 16.41       | 673 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnext101_32x8d.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnext101_32x8d.tflite) |
  | **ResNeXt101_64**    | 83.2       | **96.4**    | 83.4B   | 15.46       | 652 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnext101_64x4d.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/resnext101_64x4d.tflite) |
  | **Wide_ResNet50**    | 78.4       | 94.0        | 68.8B   | 11.40       | 417 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/wide_resnet50.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/wide_resnet50.tflite) |
  | **Wide_ResNet101**   | 78.8       | 94.2        | 126.8B  | 22.75       | 723 MB  | [[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/wide_resnet101.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-resnets/wide_resnet101.tflite) |

## Benchmarks

### Embedded Chips Runtime

  | **Model Name**         | Core i9<br><sub>(onnx) | G350<br><sub> | G510<br><sub> | G700<br><sub> | G1200<br><sub>(onnx) | 
  | ---------------------- | ---------------------- |  ------------ |  ------------ |  ------------ | -------------------- |
  | **ResNet18**           |        54 ms           |               |               |               |         55 ms       |
  | **ResNet34**           |        71 ms           |               |               |               |         110 ms       |
  | **ResNet50**           |        90 ms           |               |               |               |         127 ms       |
  | **ResNet101**          |        221 ms          |               |               |               |         262 ms      |
  | **ResNet152**          |        225 ms          |               |               |               |         443 ms      |
  | **ResNeXt50**          |        157 ms          |               |               |               |         139 ms       |
  | **ResNeXt101_32**      |        333 ms          |               |               |               |         471 ms      |
  | **ResNeXt101_64**      |        356 ms          |               |               |               |         479 ms      |
  | **Wide_ResNet50**      |        221 ms          |               |               |               |         313 ms      |
  | **Wide_ResNet101**     |        563 ms          |               |               |               |         686 ms      |

### M.2 & PCIe Plugins Runtime

  |                   | RTX 3080 |  Hailo   |
  | ----------------- | -------- | -------- |
  | **ResNet18**      |          |          |
  | **ResNet34**      |          |          |
  | **ResNet50**      |          |          |
  | **ResNet101**     |          |          |
  | **ResNet152**     |          |          |
  
## Demo
* [Delegate to MTK Genios]()
