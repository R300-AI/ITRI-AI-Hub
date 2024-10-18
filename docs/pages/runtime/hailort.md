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

# HailoRT 4.17.0

```
conda create --name hailort python=3.8 && source activate hailort

sudo apt install hailo-all
sudo dpkg --install hailort-pcie-driver_4.17.0_all.deb
sudo dpkg --install hailort_4.17.0_arm64.deb -y
pip install hailort-4.17.0-cp38-cp38-linux_aarch64.whl

```

