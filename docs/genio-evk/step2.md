---
layout: default
title: "-　Step2. Flash Image"
nav_order: 4
---

# Genio EVK Setup Guide
##### update : 2025/01 by ITRI (EOSL-R3)

### Prerequisites

* An **Ubuntu 22.04** LTS workstation with **x86_64** processors to install the AIoT Tools (including `aiot-config`, `aiot-flash`, `aiot-board`).
* Be prepared with the **Genio-350/ 510/700/ 1200 EVK** board, power cable and USB to Micro cable.


## Flashing Pre-built Image to Board

### Step 1: Download Compatible Pre-built Image
Download the compatible pre-built image from the table below:

| OS\ Device    | Genio350  | Genio510  | Genio700 | Genio1200 |
|---------------|-----------|-----------|----------|-----------|
| Yocto         |[[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-350-evk_private_240626075838.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-510-evk_private_240626080308.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-700-evk_private_240626082053.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Yocto/kirkstone_k5.15_v24.0_genio-1200-evk_private_240626084538.tar.gz) |
| Ubuntu 22.04  |[[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio350/genio-classic-server-2204-x09-20231004-131.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio350/ubuntu-boot-firmware-genio-350-evk-v23.1.3.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio510/genio-classic-desktop-2204-20240322-185.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio510/ubuntu-boot-firmware-genio-510-evk-v23.2.1.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio700/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio700/ubuntu-boot-firmware-genio-700-evk-v23.1.3.tar.gz) | [[Image]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio1200/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Firmware]](https://itriaihub.blob.core.windows.net/prebuilt-images/MediaTek-Genio-Ubuntu/genio1200/ubuntu-boot-firmware-genio-1200-evk-v23.1.3.tar.gz) |

* `Yocto` already includes the Board Support Packages (BSPs) supported by MediaTek Genio, while `Ubuntu` requires an additional step to install the BSPs according to the subsequent instructions.

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