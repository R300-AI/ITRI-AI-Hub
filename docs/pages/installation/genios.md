## Setup Build Environment

Ubuntu 22.04 (LTS)

At least 200 GiB of free disk space

At least 16 GiB of system memory

Internet connection


You can choose between **Yocto** and **Ubuntu** operating systems on your Genio board. When you choose Ubuntu, it means higher development flexibility, but you also need to install the accelerator API by yourself, please refer to [here](https://github.com/R300-AI/Embedded-Research/blob/main/docs/05_Install_ArmNN_and_NeuronPilot_on_Ubuntu_for_Genio_Boards.md) for details.

## Tutorial

**Step1.** Prepare a Ubuntu host server, and connect your development board to the host server's USB with a micro USB on the board.

> * [Genio 350-EVK](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/hw/i350-evk.html)
> * [Genio 510-EVK](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/hw/g510-evk.html)
> * [Genio 700-EVK](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/hw/g700-evk.html)
> * [Genio 1200-EVK](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/hw/g1200-evk.html)

<img src="https://github.com/R300-AI/AI-Research/blob/main/docs/snapshots/03_Flashing_Yocto_or_Ubuntu_for_Your_Genio_Boards/3-1.png" width="640">

* (1). Connect the 12V power supply of the board, (2) then connect the Micro USB to the port assigned to "image download" by MTK. (in the case of Genio-510, it is connected to USB0).

**Step2.** If you have not installed the Genio-Flash utility before, please follow the instructions below to install it on your Ubuntu server.  *Reboot is required after installation to enable serial write permission.
-  [a. Setup Build Environment Tutorial (Linux)](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/env-setup/build-env-linux.html)
- [b. Setup Tool Environment Tutorial (Linux)](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/env-setup/flash-env-linux.html)

**Step3.** Download the compatible OS according to your device type (Choose one of the following sources, but ITRI's version is more stable).  **It is recommended to use ubuntu to download as some of the configuration files will be lost in windows.*


|<div style="width:100px">Device Type</div>| Yocto v24 (kirkstone5.15)  |   <div style="width:300px">Ubuntu 22.04 (Desktop)</div>|
|---|---|---|
|Genio-350-EVK      |[[Yocto 20240626]](https://download.mediatek.com/aiot/page/download.html?Mes=type1&Code=kirkstone_k5.15_v24.0_genio-350-evk_private_240626075838.tar.gz)|[[Ubuntu 20231004]](https://people.canonical.com/~platform/images/mediatek/ubuntu-server-22.04/genio-classic-server-2204-x09-20231004-131.tar.xz?_gl=1*75ka73*_gcl_au*MTk5OTAwMTMwOC4xNzE5NDQ5NDEz*_ga*NjUwNTU5NDk3LjE3MTk0NDk0MTE.*_ga_5LTL1CNEJM*MTcyMjg2MzUxNi45LjEuMTcyMjg2NDAwNy40OS4wLjA.&_ga=2.201824722.217401924.1722850353-650559497.1719449411), [[Boot Firmware]](https://download.mediatek.com/iot/download/ubuntu/boot-firmware/latest/genio-350-evk)|
|Genio-350-EVK(備份) |[[Yocto 20240626]](https://r3resources.blob.core.windows.net/genio/kirkstone_k5.15_v24.0_genio-350-evk_private_240626075838.tar.gz)|[[Ubuntu 20231004]](https://r3resources.blob.core.windows.net/genio/genio-classic-server-2204-x09-20231004-131.tar.xz), [[Boot Firmware]](https://r3resources.blob.core.windows.net/genio/ubuntu-boot-firmware-genio-350-evk-v23.1.3.tar.gz)|
|Genio-510-EVK      |[[Yocto 20240626]](https://download.mediatek.com/aiot/page/download.html?Mes=type1&Code=kirkstone_k5.15_v24.0_genio-510-evk_private_240626080308.tar.gz)|[[Ubuntu 20240322]](https://people.canonical.com/~platform/images/mediatek/ubuntu-desktop-22.04/genio-classic-desktop-2204-20240322-185.tar.xz), [[Boot Firmware]](https://download.mediatek.com/iot/download/ubuntu/boot-firmware/latest/genio-510-evk)|
|Genio-510-EVK(備份) |[[Yocto 20240626]](https://r3resources.blob.core.windows.net/genio/kirkstone_k5.15_v24.0_genio-510-evk_private_240626080308.tar.gz)|[[Ubuntu 20240322]](https://r3resources.blob.core.windows.net/genio/genio-classic-desktop-2204-20240322-185.tar.xz), [[Boot Firmware]](https://r3resources.blob.core.windows.net/genio/ubuntu-boot-firmware-genio-510-evk-v23.2.1.tar.gz)|
|Genio-700-EVK      |[[Yocto 20240626]](https://download.mediatek.com/aiot/page/download.html?Mes=type1&Code=kirkstone_k5.15_v24.0_genio-700-evk_private_240626082053.tar.gz)|[[Ubuntu 20231005]](https://people.canonical.com/~platform/images/mediatek/ubuntu-desktop-22.04/genio-classic-desktop-2204-x01-20231005-133.tar.xz?_gl=1*1frhvg6*_gcl_au*MTk5OTAwMTMwOC4xNzE5NDQ5NDEz*_ga*NjUwNTU5NDk3LjE3MTk0NDk0MTE.*_ga_5LTL1CNEJM*MTcyMjg2MzUxNi45LjEuMTcyMjg2Mzc1MC44LjAuMA..&_ga=2.222205403.217401924.1722850353-650559497.1719449411), [[Boot Firmware]](https://download.mediatek.com/iot/download/ubuntu/boot-firmware/latest/genio-700-evk)|
|Genio-700-EVK(備份) |[[Yocto 20240626]](https://r3resources.blob.core.windows.net/genio/kirkstone_k5.15_v24.0_genio-700-evk_private_240626082053.tar.gz)|[[Ubuntu 20231005]](https://r3resources.blob.core.windows.net/genio/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Boot Firmware]](https://r3resources.blob.core.windows.net/genio/ubuntu-boot-firmware-genio-700-evk-v23.1.3.tar.gz)|
|Genio-1200-EVK     |[[Yocto 20240626]](https://download.mediatek.com/aiot/page/download.html?Mes=type1&Code=kirkstone_k5.15_v24.0_genio-1200-evk_private_240626084538.tar.gz)|[[Ubuntu 20231005]](https://people.canonical.com/~platform/images/mediatek/ubuntu-desktop-22.04/genio-classic-desktop-2204-x01-20231005-133.tar.xz?_gl=1*1frhvg6*_gcl_au*MTk5OTAwMTMwOC4xNzE5NDQ5NDEz*_ga*NjUwNTU5NDk3LjE3MTk0NDk0MTE.*_ga_5LTL1CNEJM*MTcyMjg2MzUxNi45LjEuMTcyMjg2Mzc1MC44LjAuMA..&_ga=2.222205403.217401924.1722850353-650559497.1719449411), [[Boot Firmware]](https://download.mediatek.com/iot/download/ubuntu/boot-firmware/latest/genio-1200-evk)|
|Genio-1200-EVK(備份)|[[Yocto 20240626]](https://r3resources.blob.core.windows.net/genio/kirkstone_k5.15_v24.0_genio-1200-evk_private_240626084538.tar.gz)|[[Ubuntu 20231005]](https://r3resources.blob.core.windows.net/genio/genio-classic-desktop-2204-x01-20231005-133.tar.xz), [[Boot Firmware]](https://r3resources.blob.core.windows.net/genio/ubuntu-boot-firmware-genio-1200-evk-v23.1.3.tar.gz)|


**Step4.** Unzip the image and create a port between the image and the board via genio-flash.
```
# for Yocto 
sudo tar -zxvf <YOCTO_IMAGE>.tar.gz -C <IMAGE_PATH>

cd <IMAGE_PATH>/<YOCTO_FOLDER>
genio-flash --load-dtbo gpu-mali.dtbo --load-dtbo apusys.dtbo --load-dtbo video.dtbo

# for Ubuntu 
sudo tar -zxvf <UBUNTU_IMAGE>.tar.xz -C <UBUNTU_IMAGE_PATH>
sudo tar --strip-components=1 -xvf <BOOT_FIRMWARE>.tar.gz -C <IMAGE_PATH>/<UBUNTU_FOLDER>

cd <IMAGE_PATH>/<UBUNTU_FOLDER>
genio-flash
```

<img src="https://github.com/R300-AI/AI-Research/blob/main/docs/snapshots/03_Flashing_Yocto_or_Ubuntu_for_Your_Genio_Boards/3-2.png" width="640">
* No UART0 connected is allowed, because it is only used to output logs.


**Step5.** Follow these steps on mother board to start burning process

<img src="https://github.com/R300-AI/AI-Research/blob/main/docs/snapshots/03_Flashing_Yocto_or_Ubuntu_for_Your_Genio_Boards/3-3.png" width="400">
* (a). Press and keep pressing the Download button on the board. (b). Press and release the RST button.

<img src="https://github.com/R300-AI/AI-Research/blob/main/docs/snapshots/03_Flashing_Yocto_or_Ubuntu_for_Your_Genio_Boards/3-4.png" width="640">
* After this process, you can see the log Erasing 'mmc0' message, as shown above.

>After the download is complete, it is recommended to reboot the board to enter the operating system (the default login password for the Ubuntu operating system is 'ubuntu').

### Login Your Genio board and Install the Dependencies

⚠️**IMPORTANT**: Resetting the password is necessary, everything must be done after resetting the password.

#### 1. Genio package archives and drivers
```
sudo apt-get update
sudo apt-get upgrade

sudo apt-add-repository ppa:mediatek-genio/genio-public
```
```
# for Genio 350
sudo apt install mediatek-vpud-genio350
sudo apt install mediatek-mdpd-genio350

# for Genio 510
sudo apt install mediatek-vpud-genio510

# for Genio 700
sudo apt install mediatek-vpud-genio700

# for Genio 1200
sudo apt install mediatek-vpud-genio1200
```
```
reboot
```

#### 2. Compilers and Tools

```
# Requrie for C/C++ Runtime and Python packages Management
sudo apt-get install python3-pip
sudo apt-get install cmake

#  Config Environments
python3 -m pip install --upgrade pip
# add this line to .bashrc
PATH="/home/ubuntu/.local/bin:$PATH"

pip install pyproject-toml
pip install numpy==1.26.4
pip install h5py
```

#### 3. System Monitoring

```
sudo apt-get install clinfo

# Monitoring Arm GPU
clinfo -l
```


#### D-Link DWA-171 Wifi Dongle Driver on Ubuntu (if necessary)
```
sudo apt update
sudo apt-get upgrade

sudo apt install --reinstall build-essential git bc dkms
git clone https://github.com/morrownr/8821cu-20210916.git
cd 8821cu-20210916
sudo ./install-driver.sh
sudo modprobe 8821cu
```

## Reference
1. [MedaiTek IoT Yocto Developer Guide - IoT Yocto documentation](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/index.html )
2. [Ubuntu on Genio - Ubuntu on Genio documentation](https://mediatek.gitlab.io/genio/doc/ubuntu/index.html )
