## Backbone Preview

* [This notebook show how we build these models.](https://github.com/R300-AI/model_zoo_library/blob/main/notebooks/Export_EfficientDets_via_AutoML.ipynb)
* Dataset: COCO val2017

| Model Name  | **Dtype** |**mAP**    |  **Input Size**  | **Params**   | **GFLOPS**  | **Memory**  | **Pre-trained Weights**    |
|   -------   | -------   |   ------- |   ------------   |   ---------  |  ---------  |  --------   |   ----------------------   |
| **EfficientDet_lite0** | FLOAT32 |    27.1     |    1x320x320x3   | 3.2 B        |   1.7       |   11.2 M    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite0.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite0.tflite) |
| **EfficientDet_lite1** | FLOAT32 |    32.2     |    1x384x384x3   | 4.2 B        |   3.5       |   16.1 M    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite1.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite1.tflite) |
| **EfficientDet_lite2** | FLOAT32 |    35.9     |    1x448x448x3   | 5.2 B        |   6.0       |   21.8 M    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite2.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite2.tflite) |
| **EfficientDet_lite3** | FLOAT32 |    39.6     |    1x512x512x3   | 8.3 B        |   13.7      |   28.5 M    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite3.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite3.tflite) |
| **EfficientDet_lite4** | FLOAT32 |    44.2     |    1x640x640x3   | 15.1 B       |   37.6      |   44.5 M    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite4.onnx), [[TFLite]](https://itriaihub.blob.core.windows.net/modelzoo-efficientdets/efficientdet_lite4.tflite) |

## Benchmarks

### Embedded Chips Runtime

  |                        | Core i9<br><sub>(tflite) | G350<br><sub> | G510<br><sub> | G700<br><sub> | G1200<br><sub>(onnx) | 
  | ---------------------- | ---------------------- |  ------------ |  ------------ |  ------------ | -------------------- |
  | **EfficientDet_lite0** |  101 ms                |               |               |               |        19 ms         |
  | **EfficientDet_lite1** |  202 ms                |               |               |               |        29 ms         |
  | **EfficientDet_lite2** |  324 ms                |               |               |               |        72 ms         |
  | **EfficientDet_lite3** |  643 ms                |               |               |               |        107 ms        |  
  | **EfficientDet_lite4** |  1559 ms               |               |               |               |        266 ms        |
  
### M.2 & PCIe Plugins Runtime
  | **Model Name**         | RTX 3080 |  Hailo   |
  | ---------------------- | -------- | -------- |
  | **EfficientDet_lite0** |          |          |
  | **EfficientDet_lite1** |          |          |
  | **EfficientDet_lite2** |          |          |
  | **EfficientDet_lite3** |          |          |
  | **EfficientDet_lite4** |          |          |


  
