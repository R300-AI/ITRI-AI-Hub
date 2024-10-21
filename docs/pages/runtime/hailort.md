---
layout: default
title: "　-　HailoRT"
nav_order: 35
---
# Install HailoRT 4.17.0 for ARM64 System
##### update : 2024/10 by Markov Chen
<br>

HailoRT is a runtime library provided by Hailo and designed for the Hailo-8 m.2 edge AI processor.HailoRT supports major deep learning frameworks such as TensorFlow, PyTorch and ONNX, and provides a rich set of APIs that allow developers to easily deploy deep learning models on Hailo-8 m.2. HailoRT is designed to provide high-performance inference at low power consumption, and is particularly suitable for edge computing and low-power application scenarios. By using HailoRT, developers can achieve efficient data processing and model inference, significantly improving application performance and response time.

## Installation

### **Step 1. Install PCIe driver and CLI**
Download Linux Packages and install it by following commands.<br>
[[Download PCIe Driver]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/hailort-pcie-driver_4.17.0_all.deb), [[Download CLI]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/hailort_4.17.0_arm64.deb)

```bash
$ sudo dpkg --install hailort-pcie-driver_4.17.0_all.deb
$ sudo dpkg --install hailort_4.17.0_arm64.deb
```

### **Step 2. Install PyHailoRT**
Download PyHailoRT APIs and install it by following commands.<br>
[[PyHailoRT]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/hailort-4.17.0-cp38-cp38-linux_aarch64.whl)

```bash
$ conda create --name hailort python=3.8 && source activate hailort
$ pip install hailort-4.17.0-cp38-cp38-linux_aarch64.whl
```

### **Step 3. Verify the Installation**

Download and unzip the sample code to run this demonstration.<br>
[[Hailo-Sample-Code]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/Hailo-Sample-Code.zip)

```bash
$ cd Hailo-Sample-Code
$ pip install -r requirements.txt
$ python3 ./hailo_onnxruntime_inference.py yolov5m_wo_spp.hef yolov5m_wo_spp_postprocess.onnx
```

