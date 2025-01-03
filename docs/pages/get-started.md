---
layout: default
title: Get Started
nav_order: 2
---

# Get Started
##### update : 2024/11 by Markov Chen

<br>Before selecting an embedded processor for your application, we recommend that you review the use cases or similar real-world models in Model Zoo. Then, select the appropriate Evaluation Kits based on their performance benchmarks on different processors. (...增加下圖的描述)

<div align="center"><img src="../assets/images/software-support-metric.png" width="840"/></div>

In the following documents, we provide software installation guidelines for Work Stations and Evaluation Kits to meet the basic needs of developing embedded AI:

* **Work Station**: This term refers to the host used to develop and train AI models (usually through PyTorch or TensorFlow), which mainly includes facilities such as GPUs and CPUs. Typically, it is separate from embedded systems because this stage requires high performance and high power consumption.
    > **Converter Tools**: These tools involve vendor-specific properties designed to translate the model into instructions readable by the embedded processors.

* **Evaluation Kits**: This term refers to lightweight motherboards designed specifically for certain embedded processors. Due to their highly reconfigurable hardware, they are often used in the development of various portable devices and electronic products.
    > **Runtime APIs**: APIs that delegate the model inference process to designated computing units. Usage examples can be found in the Model Zoo.


## **Evaluation Kits Overview**

Below is a list of currently supported options:

### NVIDIA Jetson Series

<div style="margin-left: 20px;">
<p>The NVIDIA Jetson series of embedded systems is designed for high-performance computing, suitable for AI and machine learning applications. This series all running on the <strong>Ubuntu</strong> operating system.</p>
</div>

|  Devices     | Orin Nano     | Orin NX          | AGX Xavier        | AGX Orin          |
|:------------:|:-------------:|:----------------:|:-----------------:|:-----------------:|
| **Chipsets**         | `Cortex-A`, `Ampere` | `Cortex-A`, `Ampere` | `Volta`         | `Cortex-A`, `Ampere` |
| **Converter Tool**   | TensorRT             | TensorRT             | TensorRT        | TensorRT             |
| **Runtime SDK**      | `Kleidi AI`, `TensorRT` | `Kleidi AI`, `TensorRT`| `TensorRT` | `Kleidi AI`, `TensorRT` |
| **Power**            | 5~15W               | 10~25W              | 10~30W            | 15~60W               |
| **Memory**           | 4GB/8GB LPDDR5      | 8GB/16GB LPDDR5     | 32GB LPDDR4x      | 32GB/64GB LPDDR5     |
 
### MediaTek Genio Series

<div style="margin-left: 20px;">
<p>The MediaTek Genio series of embedded systems is meticulously engineered for versatile applications, offering an optimal balance between performance and power efficiency. This series fully supports the <strong>Ubuntu 22.04</strong> operating system, with the primary distinctions being the types of NPUs. For fundamental image processing requirements, the <strong>Genio 350</strong> suffices; the <strong>Genio 510</strong> and <strong>Genio 700</strong> support the most extensive range of AI operators. The <strong>Genio 1200</strong> is primarily intended for scenarios requiring high CPU and GPU utilization and basic AI operations, but it is not capable of delegating more complex models (e.g., YOLO) to the NPU for computation.</p>
</div>

|  Devices     | Genio 510     | Genio 700     | Genio 1200     |
| :----------: |:-------------:|:-------------:|:--------------:|
| **Chipsets** |  `Cortex-A`, `Mali GPU`, `MDLA 3.0` |   `Cortex-A`, `Mali GPU`, `MDLA 3.0` |   `Cortex-A`, `Mali GPU`, `MDLA 2.0` |
| **Converter Tool**   | NeuronPilot                         | NeuronPilot                          | NeuronPilot                          |
| **Runtime SDK**      | `Kleidi AI`, `ArmNN`, `NeuronRT`| `Kleidi AI`, `ArmNN`, `NeuronRT` | `Kleidi AI`, `ArmNN`, `NeuronRT` |
| **Power**    | 5~10W         | 7~15W         | 10~20W         |
| **Memory**   | 4GB/8GB LPDDR4 | 4GB/8GB LPDDR4 | 8GB/16GB LPDDR5 |

<div style="margin-left: 20px;">
<p>The Genio 1200 is also available as a lighter board (ADLINK I-Pi SMARCs 1200) with the Yocto operating system.</p>
</div>

### ARM Raspberry Pi Series

<div style="margin-left: 20px;">
<p>The ARM RaspberryPi series is an affordable and popular choice for embedded systems, ideal for education, DIY projects, and lightweight applications. This series all running on the <strong>Raspbian</strong> operating system.</p>
</div>

|  Devices   | Gen-3        | Gen-4        | Gen-5         |
|:----------:|:------------:|:------------:|:-------------:|
| **Chipsets**     | `Cortex-A`      | `Cortex-A`       | `Cortex-A`        |
| **Converter Tool**   | -                         | -                          | -   |
| **Runtime SDK**      | `Kleidi AI` | `Kleidi AI` | `Kleidi AI` |
| **Power**        | 2.5~5W       | 3~6W         | 4~8W          |
| **Memory**       | 1GB LPDDR2  | 2GB/4GB/8GB LPDDR4 | 4GB/8GB LPDDR4 |
