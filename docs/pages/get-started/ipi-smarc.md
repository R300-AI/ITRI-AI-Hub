---
layout: default
title: "　-　I-Pi SMARCs"
nav_order: 4
---

# Getting Started with MediaTek Genios Evaluation Kit

### Prerequisites

* To install the AIoT Tools (include `aiot-config`, `aiot-flash`, `aiot-board`), you should use **Ubuntu 22.04** LTS host system.
* Be prepared with the **I-Pi SMARC 1200**, power cable and USB to Micro cable.


## Make Sure Flash Tools Working on Host

> To install Genio Tools on a Linux host, you need:
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

  **Step 4.** Install AIoT Tools and verify the installation.
  ```
  $ pip3 install -U genio-tools
  $ sudo usermod -a -G dialout $USER
  ```
  ```
  $ aiot-config
  fastboot: OK
  udev rules: OK
  ```

## Flashing Pre-built Image to Board

**Step 1.** Download compatible pre-built image from above table.
| OS\ Device    | SMARC1200 |
|---------------|-----------|
| Yocto         | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/Adlink-SMARC/lec-mtk-i1200-ufs_3v4_22_07_24.tar.gz) |

**Step 2.** Unzip the image into `<IMAGE_PATH>` directory.

```
sudo tar -zxvf <IMAGE>.tar.gz -C <IMAGE_PATH>
```

**Step 3.**  Run following command and wait until the logs show up.

```
cd <IMAGE_PATH>/<IMAGE>
aiot-flash
```

**Step 4.** Press **reset** key on the board to make it into flash mode.

### Appendix

* [Introducing the I-Pi SMARC](https://www.ipi.wiki/pages/1200-docs?page=index.html)