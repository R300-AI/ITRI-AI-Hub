---
layout: default
title: "-　Step1. Setup Workstations"
nav_order: 3
---

# Installation Guide for Genio EVK
##### Updated: January 2025 by ITRI (EOSL-R3)

> ### Prerequisites
> * An **x86_64 Workstation** with **Ubuntu 22.04 LTS** is required to install the Flash Tools (including `aiot-config`, `aiot-flash`, `aiot-board`).
> * Ensure **Conda** is installed on the computer to set up the NeuronPilot Tools (`NCC-TFLite`, `MTK-Converter`), which require Python 3.7.

## Install Flash Tools

### Step 1: Install Required Packages
Run the following command to install the necessary packages:

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

### Step 4: Install Genio Tools
Execute the following commands to install Genio tools and verify the installation:

```bash
$ pip3 install -U genio-tools
$ sudo usermod -a -G dialout $USER
```

### Step 5: Verify the Installation
Verify the installation:

```bash
$ genio-config
fastboot: OK
udev rules: OK
```

## Install NeuronPilot Tools

### Step 2: Extract and Install NeuronPilot
Download the NeuronPilot from [HERE](https://githubstorageblob.blob.core.windows.net/file-share/compiler/neuronpilot-6.0.5_x86_64.tar.gz) and install it:

```bash
$ sudo apt update
$ sudo apt install build-essential

# Make sure GLIBCXX_3.4.29 in your list.
$ strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX
```


### Step 3: Set Library Path and Install Dependencies

```bash
$ sudo apt install libncurses5 libstdc++6 libc++1
$ tar zxvf neuronpilot-6.0.5_x86_64.tar.gz -C ~
$ export LD_LIBRARY_PATH=~/neuronpilot-6.0.5/neuron_sdk/host/lib:$LD_LIBRARY_PATH
```

### Step 4: Verify the Installation

```bash
$ ~/neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite
```

<br>
<div align="right">
<a href="https://r300-ai.github.io/ITRI-AI-Hub/docs/genio-evk/step2.html"> 

[ Next >> Step2. Flash Genio Board ]
  
</a>
</div>
