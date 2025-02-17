---
layout: default
title: "-　Step3. Install Packages"
nav_order: 5
---

# Genio EVK Setup Guide
##### update : 2025/01 by ITRI (EOSL-R3)

### Prerequisites

* Be prepared with the **Genio-350/ 510/700/ 1200 EVK** board, power cable and USB to Micro cable.

## Install Board Support Packages (BSP)<sub>(*Ubuntu only)

Besides the native BSP that has been included with Yocto, we recommend that if you are using the Ubuntu operating system, please follow the steps below to complete the setup of your development environment.

> Gnome Desktop and Virtual Environment (important for changing monitor)
> * Disable Screen lock and Activate Automatic Login 
> * Miniconda ([Installation Guide](https://docs.anaconda.com/miniconda/))
> * WIFI driver ([[DWA-171]](https://github.com/CarlosSenobio/d-link-dwa-171-wifi-adapter-automatic-driver-installer)) 

### Step 1: Install CMake from Source Code
To install CMake, execute the following commands:

```bash
$ sudo apt-get install libssl-dev
$ git clone https://github.com/Kitware/CMake.git && cd CMake
$ ./bootstrap && make && sudo make install
```

### Step 2: Install NeuronRT Library
Follow the [NeuronRT Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/neuronrt.html) to install the NeuronRT on Ubuntu OS to access MediaTek Deep Learning Accelerator (MDLA).


### Step 3: Install Kleidi Kernel
Follow the [Kleidi Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/kleidi.html) to install the Kleidi kernel for Arm-based Ubuntu systems to unleash the AI performance on CPUs.

## Appendix

* [MediaTek IoT Yocto Developer Guide](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/)
* [Ubuntu on Genio Documents](https://mediatek.gitlab.io/genio/doc/ubuntu/index.html)
