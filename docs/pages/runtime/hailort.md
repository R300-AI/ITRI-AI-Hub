---
layout: default
title: "　-　HailoRT"
nav_order: 33
---

# HailoRT 4.18.0
## PCIe Driver==

https://hailo.ai/developer-zone/documentation/hailort-v4-18-0/?sp_referrer=drivers%2Fpcie_linux.html
* GCC 12
```
sudo apt install gcc-12
sudo rm /usr/bin/gcc 
sudo ln -s /usr/bingcc-12 /usr/bin/gcc
```
* GCC 11.4
```
sudo apt install gcc
sudo rm /usr/bin/gcc
sudo ln -s /usr/bin/gcc-11 /usr/bin/gcc
```
```
gcc --version
```
* driver
```
conda create --name hailort python=3.8 && source activate hailort
git clone https://github.com/hailo-ai/hailort-drivers --branch v4.18.0
cd hailort-drivers/linux/pcie
make all
```

# Install HailoRT 4.17.0 for ARM64 System

### **Step 1. Install PCIe driver and CLI**
Download Linux Packages and install it by following commands.<br>
[[Download PCIe Driver]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/hailort-pcie-driver_4.17.0_all.deb), [[Download CLI]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/hailort_4.17.0_arm64.deb)

```
sudo dpkg --install hailort-pcie-driver_4.17.0_all.deb
sudo dpkg --install hailort_4.17.0_arm64.deb
```

### **Step 2. Install PyHailoRT**
Download PyHailoRT APIs and install it by following commands.<br>
[[PyHailoRT]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/hailort-4.17.0-cp38-cp38-linux_aarch64.whl)

```
conda create --name hailort python=3.8 && source activate hailort
pip install hailort-4.17.0-cp38-cp38-linux_aarch64.whl
```

### **Step 3. Verify the Installation**

Download and unzip the sample code to run this demonstration.<br>
[[Hailo-Sample-Code]](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/Hailo-Sample-Code.zip)

```
cd Hailo-Sample-Code
pip install -r requirements.txt
python3 ./hailo_onnxruntime_inference.py yolov5m_wo_spp.hef yolov5m_wo_spp_postprocess.onnx
```

