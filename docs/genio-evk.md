---
layout: default
title: Genio Evaluation Kits
nav_order: 2
---

# How to Install Your Genio Board?
##### update : 2025/01 by ITRI (EOSL-R3)

<div align="center">
<img src="assets/images/pages/genio_510_evk.png" width="560"/>
</div>

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


## Process to delegate