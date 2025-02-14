---
layout: default
title: Quick Start
nav_order: 1
---

# Welcome to ITRI AI Hub Tutorials
##### update : 2025/01 by ITRI (EOSL-R3)

<br>ITRI AI Hub offers simple, fast, and commercialized Edge AI implementation solutions for enterprises and developers. Before selecting a system, we recommend evaluating which devices are suitable for your applications based on model type, computing power, memory, and energy efficiency. The diagram below summarizes the memory and computing power distribution of devices we selected, helping you compare them more intuitively with Model Zoo, open-source communities, or other custom models.

<div align="center"><img src="./docs/assets/images/pages/metric_of_all_devices.png" width="760"/></div>


## **Development Flow Overview**

<div style="margin-left: 20px;">
<br>


In the following documents, we provide software installation guidelines for Work Stations and Evaluation Kits to meet the basic needs of developing embedded AI:
<br>
* **Work Station**: This term refers to the host used to develop and train AI models (usually through PyTorch or TensorFlow), which mainly includes facilities such as GPUs and CPUs. Typically, it is separate from embedded systems because this stage requires high performance and high power consumption.
<br>
**Converter Tools**: These tools involve vendor-specific properties designed to translate the model into instructions readable by the embedded processors.
<br>
**Evaluation Kits**: This term refers to lightweight motherboards designed specifically for certain embedded processors. Due to their highly reconfigurable hardware, they are often used in the development of various portable devices and electronic products.
<br>
**Runtime APIs**: APIs that delegate the model inference process to designated computing units. Usage examples can be found in the Model Zoo.

</div><br>

## **How to Build Your Own Application?**

* [Train Your Own Model]()
* [Pre-trained Model from Model Zoo or Third-Party]()