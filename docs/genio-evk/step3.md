---
layout: default
title: "-　Step3. Install Packages"
nav_order: 5
---

# Genio EVK Setup Guide
##### update : 2025/01 by ITRI (EOSL-R3)

> ### Prerequisites
> * A **Genio-350, 510, 700**, or **1200 EVK** with the operating system flashed.
> * Ensure the **WiFi6** or **5G** module is connected to the antenna and activated.
> * It is recommended to use **Miniconda for Linux** to manage Python applications. Follow the [Installation Guide](https://docs.anaconda.com/miniconda/install/).

## Install Board Support Packages (BSP) for Ubuntu on Genio<sub>

### Step 1: Install CMake from Source Code
To install CMake, execute the following commands:

```bash
$ sudo apt-get install libssl-dev
$ git clone https://github.com/Kitware/CMake.git && cd CMake
$ ./bootstrap && make && sudo make install
```

### Step 2: Install NeuronRT Library
Follow the [NeuronRT Installation Guide (NeuroPilot Hardware Packages)](https://mediatek.gitlab.io/genio/doc/ubuntu/bsp-installation/neuropilot.html#) to install the NeuronRT on Ubuntu OS, to access MediaTek Deep Learning Accelerator (MDLA) and Vision Processor (VP).


### Step 3: Install Kleidi Kernel
(None)