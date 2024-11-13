---
layout: default
title: "　-　ArmNN"
nav_order: 42
---

# ArmNN

```bash
wget -O ArmNN-aarch64.tgz https://github.com/ARM-software/armnn/releases/download/v23.08/ArmNN-linux-aarch64.tar.gz
mkdir armnn
tar -xvf ArmNN-aarch64.tgz -C armnn

vim ~/.bashrc
#add this line to .bashrc
export LD_LIBRARY_PATH=<path_to_your_armnn_folder>

source ~/.bashrc
```
```bash
sudo ln ${LD_LIBRARY_PATH}/libarmnnDelegate.so.29.0 libarmnnDelegate.so.29
sudo ln ${LD_LIBRARY_PATH}/libarmnn.so.33.0 libarmnn.so.33
```
