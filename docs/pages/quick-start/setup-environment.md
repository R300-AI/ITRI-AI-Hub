---
layout: default
title: " - Setup Host Environment"
nav_order: 3
---

# Setup Configure Tool & Environments

## **NVIDIA Jetson Series**

## **MediaTek<sub>[1](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/env-setup/build-env-linux.html#), [2](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/env-setup/flash-env-linux.html), Windows are not supported**

### **Install `Genio-Flash` on Ubuntu Host**

> **Requirements:**
> * Python 3.8 or later
> * pip3 20.3 or later
> * Git 1.8 or later

  Step 1. Install the required packages.
  ```
  $ sudo apt update && sudo apt upgrade -y
  $ sudo apt-get install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev
  ```
  Step 2. Download Repo software and configure the environments.
  ```
  $ mkdir -p ~/.bin
  $ PATH="${HOME}/.bin:${PATH}"
  $ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
  $ chmod a+rx ~/.bin/repo
  ```

  Step 3. Install the Fastboot USB Driver and configure theirs environments.
  ```
  $ sudo apt-get install android-tools-adb android-tools-fastboot
  $ echo -n 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="0003", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0403", MODE="0660", TAG+="uaccess" SUBSYSTEM=="gpio", MODE="0660", TAG+="uaccess"' | sudo tee /etc/udev/rules.d/72-aiot.rules
  $ sudo udevadm control --reload-rules
  $ sudo udevadm trigger
  ```
  Step 4. Install Genio Tools with administrator privilege and verify the installation.
  ```
  $ pip3 install -U genio-tools
  $ sudo usermod -a -G dialout $USER
  ```
  ```
  $ genio-config
  fastboot: OK
  udev rules: OK
  ```

## **ARM Raspberry Pi Series**
