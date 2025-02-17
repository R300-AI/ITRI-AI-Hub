---
layout: default
title: "-　Step1. Setup Flash Tools"
nav_order: 3
---

# Genio EVK Setup Guide
##### update : 2025/01 by ITRI (EOSL-R3)


> ### Prerequisites
> * An **x86_64 Computer** with **Ubuntu 22.04 LTS** is required for install the Flash Tools (including `aiot-config`, `aiot-flash`, `aiot-board`)

## Make Sure Flash Tools Working on Computer

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