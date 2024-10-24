---
layout: default
title: "　-　I-Pi SMARCs"
nav_order: 4
---

# I-Pi SMARC Setup Guide
##### update : 2024/10 by Markov Chen<br>

This document provides a comprehensive guide to setting up the I-Pi SMARC 1200 Board. Follow the steps below to ensure a successful installation and configuration.

### Prerequisites

* To install the AIoT Tools (include `aiot-config`, `aiot-flash`, `aiot-board`), you should use **Ubuntu 22.04** LTS workstation with **x86_64** processors.
* Be prepared with the **I-Pi SMARC 1200**, power cable and USB to Micro cable.


## Make Sure Flash Tools Working on Host

> To install Genio Tools on a Linux host, you need:
> * Python 3.8 or later
> * pip3 20.3 or later
> * Git 1.8 or later

### Step 1: Install Required Packages
Execute the following commands to install the necessary packages:

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

### Step 4: Install AIoT Tools and Verify the Installation
Execute the following commands to install AIoT tools and verify the installation:

```bash
$ pip3 install -U genio-tools
$ sudo usermod -a -G dialout $USER
```

Verify the installation:

```bash
$ aiot-config
fastboot: OK
udev rules: OK
```

## Flashing Pre-built Image to Board

### Step 1: Download Compatible Pre-built Image
Download the compatible pre-built image from the table below:

| OS\ Device    | SMARC1200 |
|---------------|-----------|
| Yocto         | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/Adlink-SMARC/lec-mtk-i1200-ufs_3v4_22_07_24.tar.gz) |

### Step 2: Extract the Downloaded Image
Extract the downloaded image using the following command:

```bash
$ sudo tar -zxvf <IMAGE>.tar.gz -C <IMAGE_PATH>
```

### Step 3: Flash the Image to the Board
Navigate to the directory containing the extracted image files and execute the following command to flash the image:

```bash
$ cd <IMAGE_PATH>/<IMAGE>
$ aiot-flash
```

### Step 4: Reboot the Board
After the flashing process is complete, reboot the board by pressing the reset key.

## Appendix

* [Introducing the I-Pi SMARC](https://www.ipi.wiki/pages/1200-docs?page=index.html)
