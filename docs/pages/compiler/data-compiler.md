---
layout: default
title: "　-　Data Compiler"
nav_order: 21
---

# Install Data Compiler for Workstations
##### update : 2024/10 by Markov Chen
<br>

Hailo Data Compiler 3.27 compatible with HailoRT 4.17

### Prerequisites

* To install the **Data Compiler** and **Hailo RT**, you should use **Ubuntu 22.04** LTS workstation with **x86_64** processors.
  
## Installation

```
conda create --name data-compiler python=3.8 && source activate data-compiler
```
### x86
```
# data compiler
pip install hailo_dataflow_compiler-3.27.0-py3-none-linux_x86_64.whl

# hailo RT
sudo dpkg --install hailort-pcie-driver_4.17.0_all.deb
sudo dpkg --install hailort_4.17.0_amd64.deb -y
pip install hailort-4.17.0-cp38-cp38-linux_x86_64.whl
```
```
hailo h
hailo tutorial
```


