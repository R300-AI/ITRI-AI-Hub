---
layout: default
title: "-　Step2. Flash Genio Board"
nav_order: 4
---

# Genio EVK Setup Guide
##### update : 2025/01 by ITRI (EOSL-R3)

> ### Prerequisites
> * An x86_64 computer (running Ubuntu 22.04 LTS) with **Flash Tools** and **NeuronPilot** installed.
> * Prepare one of the following: **Genio510, 700**, or **1200 EVK** board with power cable.
> * A **USB to Micro USB cable** to connect the computer and the board.

## Flashing Pre-built Image to Board

### Step 1: Download Compatible Pre-built Image
Choose one of the following options. The Board Support Packages (BSPs) are already included in `Yocto`. For `Ubuntu`, you need to install the BSPs manually.

| OS\ Device    | Genio510  | Genio700 | Genio1200 |
|---------------|-----------|----------|-----------|
| Yocto         |[[Image]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-yocto/kirkstone_k5.15_v24.0_genio-510-evk_private_240626080308.tar.gz) | [[Image]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-yocto/kirkstone_k5.15_v24.0_genio-700-evk_private_240626082053.tar.gz) | [[Image]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-yocto/kirkstone_k5.15_v24.0_genio-1200-evk_private_240626084538.tar.gz) | 
| Ubuntu        |[[Image]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-ubuntu/genio510/genio-classic-desktop-2204-20240322-185.tar.xz), [[Firmware]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-ubuntu/genio510/ubuntu-boot-firmware-genio-510-evk-v23.2.1.tar.gz) | [[Image]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-ubuntu/genio700/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Firmware]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-ubuntu/genio700/ubuntu-boot-firmware-genio-700-evk-v23.1.3.tar.gz) | [[Image]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-ubuntu/genio1200/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Firmware]](https://githubstorageblob.blob.core.windows.net/file-share/image/genio-ubuntu/genio1200/ubuntu-boot-firmware-genio-1200-evk-v23.1.3.tar.gz) |

### Step 2: Extract the Downloaded Image
Extract the downloaded image using the following command:

```bash
$ sudo tar -zxvf <IMAGE>.tar.gz -C <IMAGE_PATH>

# If you are using Ubuntu, please run following command
$ sudo tar --strip-components=1 -xvf <BOOT_FIRMWARE>.tar.gz -C <IMAGE_PATH>/<IMAGE>
```

### Step 3: Connecting Board to Host
Following the official instruction [HERE](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/connect.html).
1. Connect the board to your host machine using a USB cable.
2. Ensure the board is powered on.
3. Verify the connection by checking if the device is listed using the `lsusb` command.

### Step 4: Launch genio-flash Tool
Navigate to the directory where the image was extracted and launch the genio-flash tool:

```bash
$ cd <IMAGE_PATH>/<IMAGE>
```

### Step 5: Enter Download Mode
To enter download mode, use the following commands:

```bash
# for Yocto 
$ genio-flash --load-dtbo gpu-mali.dtbo --load-dtbo apusys.dtbo --load-dtbo video.dtbo
# for Ubuntu
$ genio-flash
```

### Step 6: Boot the Board into Fastboot Mode
To boot the board into Fastboot mode, press and hold **Download** button and tap **RST** button on your board.

### Step 7: Verify Installation
After the board reboots, verify the installation by checking the boot logs and ensuring the system boots correctly.

### Step 8: Verify Installation
After the board reboots, verify the installation by checking the boot logs and ensuring the system boots correctly.