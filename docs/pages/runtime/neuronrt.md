---
layout: default
title: "　-　NeuronRT"
nav_order: 45
---

# Install NeuronRT for Genio Boards
##### update : 2024/10 by Markov Chen
<br>

NeuronPilot is an AI acceleration platform designed for MTK Genio SoCs for applications such as autonomous driving and industrial automation. NeuronPilot supports deep learning frameworks such as TensorFlow, PyTorch, and ONNX, and is specifically optimised for Neuron hardware to deliver the best performance and efficiency. NeuronPilot provides easy-to-use APIs and tools that enable developers to quickly deploy models to Neuron hardware for efficient inference and data processing.

## Installation

### Step 1: Install Gstreamer and NeuronPilot Library
Clone the repository and run the setup script for your specific Genio device:
`<your_device>` can be `genio350`, `genio510`, `genio700` or `genio1200`.

```bash
$ git clone https://github.com/R300-AI/Genio-Ubuntu.git && cd Genio-Ubuntu
$ bash ./setup_<your_device>.sh
```

### Step 2: Reboot to restart the Ubuntu kernel

```bash
$ reboot
```

### Step 3: Verify the Installation
verify the installation by running the following command:

```bash
$ sudo python3 /usr/share/neuropilot/benchmark_dla/benchmark.py --auto
```
