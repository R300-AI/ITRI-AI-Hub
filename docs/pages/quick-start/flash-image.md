---
layout: default
title: " - Flashing Image to Board"
nav_order: 5
---

# Flash Image to Boards

## Genio-Flash

### **MediaTek Genio 350/510/700/1200 EVK**<sub>[1](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/flash/flash-g350-evk.html)[2](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/flash/flash-g700-evk.html)[3](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/flash/flash-g1200-evk.html)

**Step 1.** Connect the **Image Download** port of your board to the USB port of the Host according to board layout documents.[[350-EVK]](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/connect/ports-g350-evk.html), [[510/700-EVK]](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/connect/ports-g700-evk.html) and [[1200-EVK]](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started/connect/ports-g1200-evk.html) 

<div align="center"><img src="../../assets/images/genio-flash/1.png" width="640"/></div>

**Step 2.** Unzip the image into `<IMAGE_PATH>` directory.

```
sudo tar -zxvf <IMAGE>.tar.gz -C <IMAGE_PATH>

# If you are using Ubuntu, please run following command
sudo tar --strip-components=1 -xvf <BOOT_FIRMWARE>.tar.gz -C <IMAGE_PATH>/<IMAGE>
```

**Step 3.**  Run following command and wait until the logs show up.

```
cd <IMAGE_PATH>/<IMAGE>

# for Yocto Image
genio-flash --load-dtbo gpu-mali.dtbo --load-dtbo apusys.dtbo --load-dtbo video.dtbo
# for Ubuntu Image
genio-flash
```

<div align="center"><img src="../../assets/images/genio-flash/2.png" width="500"/></div>

**Step 4.** Press and hold **Download** button and tap **RST** button on the board to start flashing.

<div align="center"><img src="../../assets/images/genio-flash/4.png" width="540"/></div>

> We recommand that you can install bellow extentions on board if you are using **Ubuntu**.
> * Gnome Desktop
>   * Disable Password Login (important for changing monitor, Setting->Privacy->Screen)
>   * Miniconda ([Installation Guide](https://docs.anaconda.com/miniconda/))
>   * WIFI driver ([[DWA-171]](https://github.com/CarlosSenobio/d-link-dwa-171-wifi-adapter-automatic-driver-installer)) 
> * Gstreamer & NeuronPilot
>   ```
>   git clone https://github.com/R300-AI/ITRI-AI-Hub.git
>   
>   # Genio 350
>   bash ITRI-AI-Hub/tools/setup_genio350.sh
>   # Genio 510
>   bash ITRI-AI-Hub/tools/setup_genio510.sh
>   # Genio 700
>   bash ITRI-AI-Hub/tools/setup_genio700.sh
>   # Genio 1200
>   bash ITRI-AI-Hub/tools/setup_genio1200.sh
>   ```
>   ```
>   # Reboot and verify the installation
>   sudo python3 /usr/share/neuropilot/benchmark_dla/benchmark.py --auto
>   ```


