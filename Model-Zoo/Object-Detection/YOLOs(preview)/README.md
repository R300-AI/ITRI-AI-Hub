# About YOLOs

The YOLO family of models referenced in this guide are provided by **Ultralytics**. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official **AGPL-3.0** license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Training/Performance Evaluation 

In the training and validation demonstration, we can utilized open-source datasets such as COCO8, Objects365, LVIS...etc. All these datasets are automatically downloaded through the Ultralytics API. You can also create your own custom datasets for training by following the guidelines in the [[Training Notebook]](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs(preview)/Train_YOLOs_on_Workstation.ipynb), and export it by [[Delegating Notebook]](https://github.com/R300-AI/ITRI-AI-Hub/blob/main/Model-Zoo/Object-Detection/YOLOs(preview)/Delegate_Models_to_ONNX_and_TFLite.ipynb). The following metrics are from previous benchmarks measured based on **COCO8**, include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>).

|  Model     |  Input Size     |  params (M)     | Time (hr)<br>T4 GPU   |  mAP<sub>50     |  mAP<sub>50-95     | Pre-built Models   |
|------------|---------|-------|-----------------------|-----------------|--------------------|--------------------|
| yolov5nu   | 640      |1.06  |0.072                  |0.63             | 0.45               |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov5nu.onnx) |
| yolov5su   | 640      |1.27  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov5su.onnx) |
| yolov5mu   | 640      |1.86  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov5mu.onnx) |
| yolov5lu   | 640      |2.50  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov5lu.onnx) |
| yolov5xu   | 640      |3.81  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov5xu.onnx) |
| yolov8n    | 640      |3.2   |0.065                  |0.63             | 0.44               |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov8n.onnx) |
| yolov8s    | 640      |11.2  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov8s.onnx) |
| yolov8m    | 640      |25.9  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov8m.onnx) |
| yolov8l    | 640      |43.7  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov8l.onnx) |
| yolov8x    | 640      |68.2  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolov8x.onnx) |
| YOLO11n    | 640      |2.6   |0.077                  |0.77             | 0.51               |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolo11n.onnx) |
| yolo11s    | 640      |9.4   |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolo11s.onnx) |
| yolo11m    | 640      |20.1  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolo11m.onnx) |
| yolo11l    | 640      |25.3  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolo11l.onnx) |
| yolo11x    | 640      |56.9  |                       |                 |                    |[[ONNX]](https://itriaihub.blob.core.windows.net/modelzoo/Object-Detection/YOLOs/yolo11x.onnx) |

These training sessions were executed on a **CUDA Workstation** equipped with a T4 GPU. To train your own model or reproduce the results above, here we provide instructions to get started:

**Step 1**. Clone expected **Jupyter Notebook** to your Workstation.

* [How to setup GPU for your own workstation?](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/workstation.html)

**Step 2**. Create an environment and install dependencies.

```bash
$ conda create --name ultralytics python=3.11 && conda activate ultralytics
(ultralytics)$ pip install -r requirements.txt
```

**Step 3**. Open **Jupyter Notebook** to execute the Training and Export Tutorial.

```bash
& conda activate ultralytics
(ultralytics)$ jupyter notebook
```

## Inference Speed 

| Model               | Genio510<br><sub>KleidiAI | Genio510<br><sub>NeuronRT | Genio700<br><sub>KleidiAI | Genio700<br><sub>NeuronRT | Genio1200<br><sub>KleidiAI |
|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|
| YOLOv5n<sub> (fp32) |                       |                       |                       |                       |                        |
| YOLOv8n<sub> (fp32) |                       |                       |                       |                       |                        |
| YOLO11n<sub> (fp32) |                       |                       |                       |                       |                        |

## Memory Usage
## Power Consumption
