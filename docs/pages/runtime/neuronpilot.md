---
layout: default
title: "　-　NeuronPilot"
nav_order: 31
---

# Install NeuronPilot for Genio Boards
##### update : 2024/10 by Markov Chen
<br>

NeuronPilot is an AI acceleration platform designed for MTK Genio SoCs for applications such as autonomous driving and industrial automation. NeuronPilot supports deep learning frameworks such as TensorFlow, PyTorch, and ONNX, and is specifically optimised for Neuron hardware to deliver the best performance and efficiency. NeuronPilot provides easy-to-use APIs and tools that enable developers to quickly deploy models to Neuron hardware for efficient inference and data processing.

## Installation

### Step 1: Install Gstreamer and NeuronPilot Library
Clone the repository and run the setup script for your specific Genio device:

```bash
$ git clone https://github.com/R300-AI/ITRI-AI-Hub.git

# Genio 350
$ bash ITRI-AI-Hub/tools/setup_genio350.sh
# Genio 510
$ bash ITRI-AI-Hub/tools/setup_genio510.sh
# Genio 700
$ bash ITRI-AI-Hub/tools/setup_genio700.sh
# Genio 1200
$ bash ITRI-AI-Hub/tools/setup_genio1200.sh
```

### Step 2: Reboot and Verify the Installation
Reboot your system and verify the installation by running the following command:

```bash
$ sudo python3 /usr/share/neuropilot/benchmark_dla/benchmark.py --auto
```
