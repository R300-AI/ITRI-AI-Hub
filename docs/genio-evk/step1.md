---
layout: default
title: "-　Step1. Setup Toolkits"
nav_order: 3
---

# Installation Guide for Genio EVK
##### update : 2025/01 by ITRI (EOSL-R3)


> ### Prerequisites

> * An **x86_64 Computer** with **Ubuntu 22.04 LTS** is required for install the Flash Tools (including `aiot-config`, `aiot-flash`, `aiot-board`) and NeuronPilot Compilers(including `NCC-TFLite` and `MTK-Converter`).

## Install Flash Tools

### Step 1: Install Required Packages
Execute the following command to install the necessary packages:

```bash
$ sudo apt update && sudo apt upgrade -y
$ sudo apt-get install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev
```

### Step 2: Install Fastboot and Setup the Environment
Execute the following command to install Fastboot and set up the environment:

```bash
$ sudo apt-get install android-tools-adb android-tools-fastboot
```

### Step 3: Install USB Driver and Setup the Environment
Execute the following commands to install the USB driver and set up the environment:

```bash
$ echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", $ GROUP="plugdev"' | sudo tee -a /etc/udev/rules.d/96-rity.rules
$ echo -n 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="0003", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0403", MODE="0660", TAG+="uaccess" SUBSYSTEM=="gpio", MODE="0660", TAG+="uaccess" ' | sudo tee /etc/udev/rules.d/72-aiot.rules
$ sudo udevadm control --reload-rules
$ sudo udevadm trigger
$ sudo usermod -a -G plugdev $USER
```

### Step 4: Install Genio Tools and Verify the Installation
Execute the following commands to install Genio tools and verify the installation:

```bash
$ pip3 install -U genio-tools
$ sudo usermod -a -G dialout $USER
```
Verify the installation:
```bash
$ genio-config
fastboot: OK
udev rules: OK
```

## Install NeuronPilot Converters

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
# Output should be: 2.9.0
```