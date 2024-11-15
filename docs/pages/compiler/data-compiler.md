---
layout: default
title: "　-　Data Compiler"
nav_order: 31
---

# Install Data Compiler for Workstations
##### update : 2024/10 by Markov Chen
<br>

Hailo Data Compiler is a tool designed for Hailo's AI processors, enabling developers to efficiently compile and optimize models for deployment on Hailo hardware. It includes a model compilation tool (hailo_dataflow_compiler) and is compatible with HailoRT runtime. The current version of Hailo Data Compiler is 3.27, and it supports Python 3.8. If this meets your expectations, you can follow the instructions to install the Hailo Data Compiler environment.

### Prerequisites

* To install the **Data Compiler** and **Hailo RT**, you should use **Ubuntu 22.04** LTS workstation with **x86_64** processors.
  
## Installation

### Step 1: Create and Activate Conda Environment
Execute the following commands to create and activate the Conda environment:

```bash
$ conda create --name data-compiler python=3.8
$ source activate data-compiler
```

### Step 2: Set Library Path
Set the library path by executing the following command:

```bash
$ export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
```

### Step 3: Install Dependencies
Download the Data Compiler 3.27.0 from [HERE](https://itriaihub.blob.core.windows.net/github-download-resources/repository/ITRI-AI-Hub/hailo_dataflow_compiler-3.27.0-py3-none-linux_x86_64.whl) and install it:

```bash
$ sudo apt-get install -y graphviz-dev
$ pip install hailo_dataflow_compiler-3.27.0-py3-none-linux_x86_64.whl

$ pip install --extra-index-url https://developer.download.nvidia.com/compute/redist nvidia-dali-cuda110 nvidia-dali-tf-plugin-cuda110   #optional for accelerate process
```

### Step 4: Verify Installation
Reboot the system and verify the installation by executing the following commands:

```bash
$ hailo scan
$ python3 -c "import hailo_sdk_client; print('OK')"   # you also can learn how to use it by 'hailo tutorial' command
```



