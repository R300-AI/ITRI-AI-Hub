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
```
```
# If you are using Ubuntu, please run this subsequent command
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

> We Recommand that you can install bellow extentions manually if you are using **Ubuntu OS**.
> * NeuronPilot
>   ```
>   # Genio 350
>   sudo apt install mediatek-vpud-genio350
>   sudo apt install mediatek-mdpd-genio350
>  
>   # Genio 510
>   sudo apt install mediatek-vpud-genio510
>   sudo apt install mediatek-apusys-firmware-genio510
>   sudo apt install mediatek-libneuron mediatek-neuron-utils mediatek-libneuron-dev
>  
>   # Genio 700
>   sudo apt install mediatek-vpud-genio700
>   sudo apt install mediatek-apusys-firmware-genio700
>   sudo apt install mediatek-libneuron mediatek-neuron-utils mediatek-libneuron-dev
>  
>   # Genio 1200
>   sudo apt install mediatek-vpud-genio1200
>   sudo apt install mediatek-apusys-firmware-genio1200
>   sudo apt install mediatek-libneuron mediatek-neuron-utils mediatek-libneuron-dev
>   ```
> * Gstreamer
>   ```
>   sudo apt install pulseaudio
>   sudo apt install pulseaudio-utils
>   sudo apt install gstreamer1.0-alsa
>   sudo apt install gstreamer1.0-plugins-base
>   sudo apt install gstreamer1.0-plugins-good
>   sudo apt install gstreamer1.0-plugins-bad
>   sudo rm ~/.cache/gstreamer-1.0/registry.aarch64.bin
>   rm ~/.cache/gstreamer-1.0/registry.aarch64.bin
>   ```

