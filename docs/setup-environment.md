---
layout: default
title: " - Setup Host Environment"
nav_order: 21
---

# Setup Flash Environments for Server Host 

## **MediaTek**<sub>[1](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/env-setup/build-env-linux.html#), [2](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/env-setup/flash-env-linux.html)

### **Install Genio-Flash on Ubuntu Host (*Windows is not supported)**

> **Requirements:**
> * Python 3.8 or later
> * pip3 20.3 or later
> * Git 1.8 or later

  **Step 1.** Install the required packages.
  ```
  $ sudo apt update && sudo apt upgrade -y
  $ sudo apt-get install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev
  ```
  **Step 2.** Install Fastboot and setup the environments.
  ```
  $ sudo apt-get install android-tools-adb android-tools-fastboot
  ```
  **Step 3.** Install USB Driver and setup the environments.
  ```
  $ echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", $ GROUP="plugdev"' | sudo tee -a /etc/udev/rules.d/96-rity.rules
  $ echo -n 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="0003", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0403", MODE="0660", TAG+="uaccess" SUBSYSTEM=="gpio", MODE="0660", TAG+="uaccess" ' | sudo tee /etc/udev/rules.d/72-aiot.rules
  $ sudo udevadm control --reload-rules
  $ sudo udevadm trigger
  $ sudo usermod -a -G plugdev $USER
  ```
  **Step 4.** Install Genio Tools (include `genio-config`, `genio-flash`, `genio-board`) and verify the installation.
  ```
  $ pip3 install -U genio-tools
  $ sudo usermod -a -G dialout $USER
  ```
  ```
  $ genio-config
  fastboot: OK
  udev rules: OK
  ```

## **ADLink**<sub>[1](https://docs.ipi.wiki/smarc/ipi-smarc-1200/AIoTToolInstallation.html)

### **Install AIoT-Flash on Ubuntu Host (*Windows is not supported)**

> **Requirements:**
> * Python 3.8 or later
> * pip3 20.3 or later
> * Git 1.8 or later

  **Step 1.** Install the required packages.
  ```
  $ sudo apt update && sudo apt upgrade -y
  $ sudo apt-get install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev
  ```
  **Step 2.** Install Fastboot and setup the environments.
  ```
  $ sudo apt-get install android-tools-adb android-tools-fastboot
  ```
  **Step 3.** Install USB Driver and setup the environments.
  ```
  $ echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", $ GROUP="plugdev"' | sudo tee -a /etc/udev/rules.d/96-rity.rules
  $ echo -n 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="0003", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0403", MODE="0660", TAG+="uaccess" SUBSYSTEM=="gpio", MODE="0660", TAG+="uaccess" ' | sudo tee /etc/udev/rules.d/72-aiot.rules
  $ sudo udevadm control --reload-rules
  $ sudo udevadm trigger
  $ sudo usermod -a -G plugdev $USER
  ```

  **Step 4.** Install AIoT Tools (include `aiot-config`, `aiot-flash`, `aiot-board`) and verify the installation.
  ```
  $ pip3 install -U genio-tools
  $ sudo usermod -a -G dialout $USER
  ```
  ```
  $ aiot-config
  fastboot: OK
  udev rules: OK
  ```
