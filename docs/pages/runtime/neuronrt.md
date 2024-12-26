---
layout: default
title: "　-　NeuronRT"
nav_order: 45
---

# Installation of NeuronRT
##### update : 2024/12 by Markov Chen
<br>

NeuronRT is an AI acceleration engine designed for MTK Genio SoCs , which is suitable for applications such as autonomous driving and industrial automation. Currently, NeuronRT mainly supports TensorFlow Lite model deployment framework to provide the best inference efficiency.

Our ITRI AI Hub also provides automated installation scripts in [Genio-Ubuntu](https://github.com/R300-AI/Genio-Ubuntu) according to the guidelines of [Ubuntu on Genio](https://mediatek.gitlab.io/genio/doc/ubuntu/index.html) Document, you can follow the steps below to install NeuronRT for your embedded devices.

## Installation Instructions

### Step 1: Install GStreamer and NeuronPilot Library
Clone the repository and execute the setup script for your specific Genio device. Replace `<your_device>` with one of the following options: `genio350`, `genio510`, `genio700`, or `genio1200`.

```bash
$ git clone https://github.com/R300-AI/Genio-Ubuntu.git && cd Genio-Ubuntu
$ bash ./setup_<your_device>.sh
```

### Step 2: Reboot the System
Reboot your system to restart the Ubuntu kernel and complete the installation process.

```bash
$ sudo reboot
```

### Step 3: Verify the Installation
Verify the installation by running the following command:

```bash
$ sudo python3 /usr/share/neuropilot/benchmark_dla/benchmark.py --auto
```
