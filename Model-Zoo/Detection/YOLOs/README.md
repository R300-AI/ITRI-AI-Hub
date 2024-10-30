# About YOLOs

This repository primarily utilizes models provided by Ultralytics. Ultralytics offers a range of pre-trained models and tools for training custom models. Users can quickly train their own models using Ultralytics' tools while adhering to the AGPL3.0 LICENSE.

### Support Metric

|          | Genio 350          | Genio 510          | Genio 700          | Genio 1200         |
|----------|--------------------|--------------------|--------------------|--------------------|
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |

### Prerequisites

* **Ubuntu 22.04 LTS** Workstation with **x86_64** processors and **NeuronPilot** installed. ([Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html))

### Step 1: Set Up the Environment and Train the Model
To set up the environment and train the model, execute the following commands:
```bash
$ conda create --name ultralytics python==3.11 && source activate ultralytics
$ pip install -r requirements.txt
```

### Step 2: Convert the Model to INT8-TFLite Format
To convert the model to INT8-TFLite format, execute the following commands:

```bash
$ yolo export model=<model_name>.pt imgsz=640 format=tflite half=True int8=True
```
```bash
$ source activate neuronpilot
$ python3 convert_to_tflite_quantized.py
```

### Step 3: Convert the Model to INT32-TFLite Format
To convert the model to INT32-TFLite format, execute the following commands:

```bash
$ yolo export model=yolov8s.pt imgsz=640 format=tflite half=True int8=True
```

### Step 4: Compile the Model with NeuronPilot
To compile the model with NeuronPilot, execute the following commands:

```bash
$ source deactivate && source activate neuronpilot
$ ~/neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 ./yolov8s_saved_model/yolov8s_float32.tflite
```

