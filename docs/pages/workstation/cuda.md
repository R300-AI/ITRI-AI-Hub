---
layout: default
title: "　-　CUDA"
nav_order: 11
---

# Install NVIDIA Driver on Ubuntu 22.04 LTS
##### update : 2024/10 by Markov Chen
<br>

<div align="center"><img src="../../assets/images/cuda.png" width="720"/></div>

## Requirements

> * Conda

## Tutorial

### Step 1: Update and upgrade your system
Run the following commands to update and upgrade your system:

```bash
$ sudo apt update
$ sudo apt upgrade
```

### Step 2: Install NVIDIA driver
Run the following command to install the NVIDIA driver:

```bash
$ sudo ubuntu-drivers install nvidia:535
```

### Step 3: Verify the NVIDIA driver installation
Verify the installation by running the following command:

```bash
$ nvidia-smi
```

### Step 4: Install PyTorch with CUDA support
Run the following command to install PyTorch with CUDA support:

```bash
$ pip3 install torch torchvision torchaudio

$ python3 -c "import torch; print(torch.cuda.is_available())"
```

### Appendix
* [NVIDIA drivers installation](https://ubuntu.com/server/docs/nvidia-drivers-installation)


