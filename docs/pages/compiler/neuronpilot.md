---
layout: default
title: "　-　NeuronPilot"
nav_order: 24
---

# Install NeuronPilot for Workstations
##### update : 2024/10 by Markov Chen
<br>

NeuronPilot is an acceleration kit for MediaTek's Genio series of SoCs (e.g., MT8395, MTK8390, etc.) that allows developers to quickly delegate models to the NPU. It includes a model quantisation tool (`mtk_converter`) and a compilation tool (`ncc-tflite`), both of which are used on Linux-based x86_64 workstations without APU intervention. The current version of **NeuronPilot** is **6.0.5**, and `mtk_converter` only support with **Python 3.7** and **PyTorch from 1.3.0 to 2.0.0**. If this meets your expectations you can follow the instructions to install the NeuronPilot environment.

### Prerequisites

* To install the **NCC-TFLite** and **MTK-Converter**, you should use **Ubuntu 22.04** LTS workstation with **x86_64** processors.
  
## Installation

### Step 1: Create and Activate Conda Environment
Execute the following command to create and activate the Conda environment:

```bash
$ conda create --name neuronpilot python=3.7
```
### Step 2: Extract and Install NeuronPilot
Download the NeuronPilot from [HERE](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/neuronpilot-6.0.5_x86_64.tar.gz) and install it:

```bash
$ sudo apt-get update
$ sudo apt install libncurses5 libstdc++6 libc++1
$ tar zxvf neuronpilot-6.0.5_x86_64.tar.gz -C ~
$ export LD_LIBRARY_PATH=~/neuronpilot-6.0.5/neuron_sdk/host/lib:$LD_LIBRARY_PATH
```

### Step 3: Set Library Path and Install Dependencies
Execute the following commands to install dependencies:

```bash
$ source activate neuronpilot
$ pip install ~/neuronpilot-6.0.5/offline_tool/mtk_converter-2.9.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl
$ pip install torch==1.9.0 torchvision==0.10.0
```

### Step 4: Verify Installation
Reboot and execute the following command to verify the installation:

```bash
$ python3 -c 'import mtk_converter; print(mtk_converter.__version__)'
>> 2.9.0
```

## Appendix
* [Neuropilot Converter Tool and Demo with YOLOv5 (Failed)](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/ml-guide/neuron-dev-flow/model_converter/neuropilot_converter_tool.html)
