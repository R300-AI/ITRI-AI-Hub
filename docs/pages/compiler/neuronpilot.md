---
layout: default
title: "　-　NeuronPilot"
nav_order: 24
---

# Install NeuronPilot for Genio Boards
##### update : 2024/10 by Markov Chen
<br>

NeuronPilot is an acceleration kit for MediaTek's Genio series of SoCs (e.g., MT8395, MTK8390, etc.) that allows developers to quickly delegate models to the NPU. It includes a model quantisation tool (`mtk_converter`) and a compilation tool (`ncc-tflite`), both of which are used on Linux-based x86_64 workstations without APU intervention. The current version of **NeuronPilot** is **6.0.5**, which only supports **Python 3.7** and **PyTorch from 1.3.0 to 2.0.0**. You can install the NeuronPilot environment by following instructions.

## Installation

### Step 1: Create and Activate Conda Environment
Execute the following command to create and activate the Conda environment:

```bash
$ conda create --name neuronpilot python=3.7 && source activate neuronpilot
```
### Step 2: Extract and Install NeuronPilot
Download and Extract the NeuronPilot from [HERE](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/neuropilot-6.0.5_x86_64.zip) and install it:

```bash
$ tar zxvf neuropilot-6.0.5.tar.gz && mv ./neuropilot-6.0.5 ~/neuropilot-6.0.5
$ pip install ~/neuropilot-6.0.5/offline_tool/mtk_converter-2.9.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl
```

### Step 3: Set Library Path and Install Dependencies
Execute the following commands to set the library path and install dependencies:

```bash
$ export LD_LIBRARY_PATH=/neuropilot-6.0.5/neuron_sdk/host/lib
$ sudo apt install libncurses5
```

### Step 4: Verify Installation
Execute the following command to verify the installation:

```bash
$ python3 -c 'import mtk_converter; print(mtk_converter.__version__)'
```

## Appendix
* [Neuropilot Converter Tool and Demo with YOLOv5](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/ml-guide/neuron-dev-flow/model_converter/neuropilot_converter_tool.html)
