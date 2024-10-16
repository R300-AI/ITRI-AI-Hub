---
layout: default
title: Get Started
nav_order: 2
---

# Get Started

<br>Before selecting the architecture for your application and system, we recommend that you can start with a rough search of possible platforms from the [Home](https://r300-ai.github.io/ITRI-AI-Hub/) page. Then, you can conduct a detailed conceptual review of these systems.

<div style="margin-left: 20px;">
<br>If you have not previously installed the Configuration Tool, please follow the instructions below to install it on the host.
</div>

1. Choice HW 
2. Choice SW 
3. Benchmakring

## **Platform Overview**

### NVIDIA Jetson Series

<div style="margin-left: 20px;">
<p>The NVIDIA Jetson series of embedded systems is designed for high-performance computing, suitable for AI and machine learning applications. This series all running on the <strong>Ubuntu</strong> operating system.</p>
</div>

|  Devices     | Orin Nano     | Orin NX          | AGX Xavier        | AGX Orin          |
|:------------:|:-------------:|:----------------:|:-----------------:|:-----------------:|
| **Chipsets**     | NVIDIA Orin         | NVIDIA Orin         | NVIDIA Xavier     | NVIDIA Orin          |
| **Architecture** | arm64               | arm64               | arm64             | arm64                |
| **CPU**          | 6-core Cortex-A78AE | 8-core Cortex-A78AE | 8-core ARM v8.2   | 12-core Cortex-A78AE |
| **GPU**          | Ampere (1024-core)  | Ampere (1024-core)  | Volta (512-core)  | Ampere (2048-core)   |
| **Power**        | 5~15W               | 10~25W              | 10~30W            | 15~60W               |
| **Memory**       | 4GB/8GB LPDDR5      | 8GB/16GB LPDDR5     | 32GB LPDDR4x      | 32GB/64GB LPDDR5     |
 
### MediaTek Genio Series

<div style="margin-left: 20px;">
<p>The MediaTek Genio series of embedded systems is designed for versatile applications, offering a balance of performance and power efficiency. This series all supporting <strong>Ubuntu 22.04</strong> and <strong>Yocto</strong> operating systems.</p>
</div>

|  Devices     | Genio 350    | Genio 510     | Genio 700     | Genio 1200     |
| :----------: |:------------:|:-------------:|:-------------:|:--------------:|
| **Chipsets** |  MT8365      |  MT8385       |   MT8395      |   MT8396       |
| **Architecture** | arm64    | arm64         | arm64         | arm64          |
| **CPU**      | Cortex-A53   | Cortex-A73/A53 | Cortex-A76/A55 | Cortex-A78/A55 |
| **GPU**      | Mali-G52     | Mali-G57      | Mali-G57      | Mali-G57       |
| **Power**    | 3~5W         | 5~10W         | 7~15W         | 10~20W         |
| **Memory**   | 2GB/4GB LPDDR4 | 4GB/8GB LPDDR4 | 4GB/8GB LPDDR4 | 8GB/16GB LPDDR5 |

### ARM Raspberry Pi Series

<div style="margin-left: 20px;">
<p>The ARM RaspberryPi series is an affordable and popular choice for embedded systems, ideal for education, DIY projects, and lightweight applications. This series all running on the <strong>Raspbian</strong> operating system.</p>
</div>

|  Devices  | Gen-1        | Gen-2        | Gen-3        | Gen-4        | Gen-5         |
|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:------------:|
| **Chipsets** | BCM2835    | BCM2836      | BCM2837      | BCM2711      | BCM2712       |
| **Architecture** | arm64  | arm64        | arm64        | arm64        | arm64         |
| **CPU**    | ARM1176JZF-S | Cortex-A7    | Cortex-A53   | Cortex-A72   | Cortex-A76    |
| **Power**  | 1.8~3.5W    | 2.5~4W       | 2.5~5W       | 3~6W         | 4~8W          |
| **Memory** | 256MB/512MB SDRAM | 1GB LPDDR2 | 1GB LPDDR2  | 2GB/4GB/8GB LPDDR4 | 4GB/8GB LPDDR4 |
