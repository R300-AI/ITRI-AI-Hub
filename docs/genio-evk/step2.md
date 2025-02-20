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


### Step 2: Connect the Board to Your Host
Connect the Genio EVK to your host using a USB cable based on board layout configuration.

<div align="center">
<img src="assets/images/pages/genio_510_layout1.png" width="560"/>
</div>

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