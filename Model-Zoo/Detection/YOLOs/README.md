# YOLOs

## Support Metric

### MediaTek Genios

#### Support Metric

|          | Genio 350          | Genio 510          | Genio 700          | Genio 1200         |
|----------|--------------------|--------------------|--------------------|--------------------|
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |

### Prerequisites

* **Ubuntu 22.04 LTS** Workstation with **x86_64** processors and **NeuronPilot** installed. ([Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html))
* A **Genio-1200 EVK** board which **NeuronRT** Library has been installed.([Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/get-started/genio-evk.html))

## Converting Model for Deployment
### Environment and Train
* Conda
```bash
$ conda create --name ultralytics python==3.11 && source activate ultralytics
$ pip install -r requirements.txt
```
* [Train](https://docs.ultralytics.com/modes/train/) and [Export](https://docs.ultralytics.com/modes/export/#usage-examples) by Python

### Convert to INT8-TFLite Format

```bash
$ yolo export model=yolov8s.pt imgsz=640 format=torchscript
```
```bash
$ source activate neuronpilot
$ python3 convert_to_tflite_quantized.py
```

### Convert to INT32-TFLite Format
```bash
$ yolo export model=yolov8s.pt imgsz=640 format=tflite half=True int8=True
```
* Compile by NeuronPilot
```bash
$ source deactivate && source activate neuronpilot
$ ~/neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 ./yolov8s_saved_model/yolov8s_float32.tflite
```

## Board

```bash
conda create --name YOLOs python=3.9 && source activate YOLOs
sudo pip install numpy==1.26.4 opencv-python tflite-runtime
```
