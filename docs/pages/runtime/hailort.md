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
[Download PCIe Driver](), [Download CLI]()

```
sudo dpkg --install hailort-pcie-driver_4.17.0_all.deb
sudo dpkg --install hailort_4.17.0_arm64.deb
```

### **Step 2. Install PCIe driver and CLI**
Download PyHailoRT APIs and install it by following commands.<br>
[PyHailoRT]()

```
conda create --name hailort python=3.8 && source activate hailort
pip install hailort-4.17.0-cp38-cp38-linux_aarch64.whl
```

* Step2
```
```

