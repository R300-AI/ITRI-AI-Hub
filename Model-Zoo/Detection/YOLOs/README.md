# YOLOs

## MediaTek Genios

### Support Metric

|          | Genio 350          | Genio 510          | Genio 700          | Genio 1200         |
|----------|--------------------|--------------------|--------------------|--------------------|
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |

### Prerequisites

* **Ubuntu 22.04 LTS** Workstation with **x86_64** processors and **NeuronPilot** installed. ([Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html))

### Converting Model for Deployment
step1 Conda
```bash
$ conda create --name ultralytics python==3.11 && source activate ultralytics
$ pip install -r requirements.txt
```
* [Train](https://docs.ultralytics.com/modes/train/) and [Export](https://docs.ultralytics.com/modes/export/#usage-examples) by Python

step2 Convert to INT32-TFLite Format
```bash
$ yolo export model=<model_name>.pt imgsz=640 format=tflite half=True int8=True
```
step3 Compile by NeuronPilot
```bash
$ source deactivate && source activate neuronpilot
$ ~/neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 ./<model_name>_saved_model/<model_name>_float32.tflite
```
