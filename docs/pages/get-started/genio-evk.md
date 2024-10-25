---
layout: default
title: "　-　Genio EVKs"
nav_order: 3
---

# Genio EVK Setup Guide
##### update : 2024/10 by Markov Chen<br>

This document provides a comprehensive guide to setting up the Genio EVK (Evaluation Kit). Follow the steps below to ensure a successful installation and configuration.

### Prerequisites

* To install the AIoT Tools (include `aiot-config`, `aiot-flash`, `aiot-board`), you should use **Ubuntu 22.04** LTS workstation with **x86_64** processors.
* Be prepared with the **Genio-350/ 510/700/ 1200 EVK** board, power cable and USB to Micro cable.

## Make Sure Flash Tools Working on Host

### Step 1: Install Required Packages
Execute the following command to install the necessary packages:

```bash
$ sudo apt update && sudo apt upgrade -y
$ sudo apt-get install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev
```

### Step 2: Install Fastboot and Set Up the Environment
Execute the following command to install Fastboot and set up the environment:

```bash
$ sudo apt-get install android-tools-adb android-tools-fastboot
```

### Step 3: Install USB Driver and Set Up the Environment
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

## Flashing Pre-built Image to Board

### Step 1: Download Compatible Pre-built Image
Download the compatible pre-built image from the table below:

| OS\ Device    | Genio350  | Genio510  | Genio700 | Genio1200 |
|---------------|-----------|-----------|----------|-----------|
| Yocto         |[[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-350-evk_private_240626075838.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-510-evk_private_240626080308.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-700-evk_private_240626082053.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-1200-evk_private_240626084538.tar.gz) |
| Ubuntu 22.04  |[[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio350/genio-classic-server-2204-x09-20231004-131.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio350/ubuntu-boot-firmware-genio-350-evk-v23.1.3.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio510/genio-classic-desktop-2204-20240322-185.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio510/ubuntu-boot-firmware-genio-510-evk-v23.2.1.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio700/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio700/ubuntu-boot-firmware-genio-700-evk-v23.1.3.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio1200/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio1200/ubuntu-boot-firmware-genio-1200-evk-v23.1.3.tar.gz) |

### Step 2: Connect the Board to Your Host
Connect the Genio EVK to your host using a USB cable based on board layout configuration.

> * [[350-EVK layout]](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/connect/ports-g350-evk.html)
> * [[510/700-EVK layout]](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/connect/ports-g700-evk.html)
> * [[1200-EVK layout]](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/connect/ports-g1200-evk.html) 

<div align="center"><img src="../../assets/images/genio-flash/1.png" width="640"/></div>

### Step 3: Extract the Downloaded Image
Extract the downloaded image using the following command:

```bash
$ sudo tar -zxvf <IMAGE>.tar.gz -C <IMAGE_PATH>

# If you are using Ubuntu, please run following command
$ sudo tar --strip-components=1 -xvf <BOOT_FIRMWARE>.tar.gz -C <IMAGE_PATH>/<IMAGE>
```

### Step 4: Flash the Image to the Board
Navigate to the directory containing the extracted image files and execute the following command to flash the image:

```bash
$ cd <IMAGE_PATH>/<IMAGE>

# for Yocto Image
$ genio-flash --load-dtbo gpu-mali.dtbo --load-dtbo apusys.dtbo --load-dtbo video.dtbo
# for Ubuntu Image
$ genio-flash
```

<div align="center"><img src="../../assets/images/genio-flash/2.png" width="500"/></div>

### Step 5: Boot the Board into Fastboot Mode
To boot the board into Fastboot mode, press and hold **Download** button and tap **RST** button on your board.

<div align="center"><img src="../../assets/images/genio-flash/4.png" width="540"/></div>

## Install Board Support Packages (BSP)<sub>(*Ubuntu only)

Besides the native BSP that has been included with Yocto, we recommend that if you are using the Ubuntu operating system, please follow the steps below to complete the setup of your development environment.

> Gnome Desktop and Virtual Environment (important for changing monitor)
> * Disable Screen lock and Activate Automatic Login 
> * Miniconda ([Installation Guide](https://docs.anaconda.com/miniconda/))
> * WIFI driver ([[DWA-171]](https://github.com/CarlosSenobio/d-link-dwa-171-wifi-adapter-automatic-driver-installer)) 

### Step 1: Install CMake from Source Code
To install CMake, execute the following commands:

```bash
$ sudo apt-get install libssl-dev
$ git clone https://github.com/Kitware/CMake.git && cd Cmake
$ ./bootstrap && make && sudo make install
```

### Step 2: Install NeuronRT Library
Follow the [NeuronRT Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/neuronrt.html) to install the NeuronPilot for Genios-Ubuntu systems to access MediaTek Deep Learning Accelerator (MDLA).


### Step 3: Install Kleidi Kernel
Follow the [Kleidi Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/ml-engine/kleidi.html) to install the Kleidi kernel for Arm-based Ubuntu systems to unleash the AI performance on CPUs.

## Appendix

* [MediaTek IoT Yocto Developer Guide](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/)
* [Ubuntu on Genio Documents](https://mediatek.gitlab.io/genio/doc/ubuntu/index.html)
