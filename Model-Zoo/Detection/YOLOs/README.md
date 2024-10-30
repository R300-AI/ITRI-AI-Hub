# About YOLOs

The YOLO family of models referenced in this guide are provided by Ultralytics. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official AGPL-3.0 license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

## MediaTek Genios

#### Support Metric

|          | Genio 350          | Genio 510          | Genio 700          | Genio 1200         |
|----------|--------------------|--------------------|--------------------|--------------------|
| YOLOv8s  | :x:                | :white_check_mark: | :white_check_mark: | :x:                |

#### Prerequisites

* **Ubuntu 22.04 LTS** Workstation with **x86_64** processors and **NeuronPilot** installed.

### Converting Model for Deployment

#### Step 1: Environment Setup
To set up the environment and prepare for model training, execute the following commands:

```bash
$ conda create --name ultralytics python==3.11 && source activate ultralytics
$ pip install -r requirements.txt
```

#### Step 2: Model Training and Export
Use the following commands to export the pre-trained model, or you can retrain your own model by following the guidelines in the [Ultralytics Documentation](https://docs.ultralytics.com/modes/train/#usage-examples):

```bash
$ yolo export model=<model_name>.pt imgsz=640 format=tflite
```

#### Step 3: Model Compilation with NeuronPilot
Use the following commands to compile a model in NeuronPilot, if you do not have NeuronPilot installed please refer to the guide [HERE](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html):

```bash
$ source deactivate && source activate neuronpilot
$ ~/neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 ./<model_name>_saved_model/<model_name>_float32.tflite ./<model_name>_float32_mdla3.tflite
```
