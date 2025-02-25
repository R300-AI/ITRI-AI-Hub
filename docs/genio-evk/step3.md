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


## Install NeuronRT on Ubuntu Genio
### Step 1: Install CMake from source code

```bash
$ sudo apt-get install libssl-dev
$ git clone https://github.com/Kitware/CMake.git && cd CMake
$ ./bootstrap && make && sudo make install
$ cd            # go back to the root directory
```

### Step 2: Install and verify the NeuronRT library
Follow the [Instruction](https://mediatek.gitlab.io/genio/doc/ubuntu/bsp-installation/neuropilot.html#) to install and verify the NeuroPilot Hardware Packages (NeuronRT), to access MediaTek Deep Learning Accelerator (MDLA) and Vision Processor (VP).

## Install ArmNN on Ubuntu Genio

### Step 1: Install the ArmNN with Arm Compute Library (ACL) from source code

```bash
git clone https://github.com/ARM-software/armnn.git && cd armnn
cd build-tool/scripts
sudo ./install-packages.sh

./setup-armnn.sh --target-arch=aarch64 --all
./build-armnn.sh --target-arch=aarch64 --all --neon-backend --cl-backend

./setup-armnn.sh --help
./build-armnn.sh --help
```

### Step 2: Verify the installation

```bash
$ cd            # go back to the root directory
```

## Install KleidiAI on Ubuntu Genio
### Step 1: Install KleidiAI from source code

```bash
$ git clone https://git.gitlab.arm.com/kleidi/kleidiai.git && cd kleidiai
$ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=cmake/toolchains/aarch64-none-linux-gnu.toolchain.cmake -S . -B build/
$ cmake --build ./build
$ cd            # go back to the root directory
```

### Step 2: Install KleidiCV from source code

```bash
$ git clone https://git.gitlab.arm.com/kleidi/kleidicv.git && cd kleidicv
$ cmake -S /path/to/kleidicv -B build-kleidicv-linux
$ cmake --build build-kleidicv-linux --parallel
$ cd            # go back to the root directory
```

<br>
<div align="right">
  
[ Finished >>  ]

</div>
