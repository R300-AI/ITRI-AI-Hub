# Demonstration List

The Model Zoo aggregates benchmarks for different tasks, providing information on the feasibility of applications across various chips. This enables developers to quickly select the most suitable chip system platforms.

In our Python Demo examples, developers will find a variety of pre-trained models. These resources are designed to facilitate rapid practical testing and provide a comprehensive understanding of the model deployment workflow. Additionally, experienced developers can leverage open-source frameworks such as TensorFlow and PyTorch to create custom models, enabling the realization of innovative AI designs.

## Computer Vision
### Image Classification
### Object Detection

| Model   |    Delegation    |     Platform     |        Chipsets         |    Speed (ms) |     Memory (GB)    |  Power (Watt) |     Temp (°C)    |    Demo    |
|---------|-------------------|------------------|-------------------------|---------------|---------------|---------------|------------------|---------------|
| YOLOv8n<sub>(fp32) |  --  | [Genio 510](https://r300-ai.github.io/ITRI-AI-Hub/docs/genio-evk.html) | `Cortex-A`    | 1252.1              |               |               |                  |[link](https://github.com/R300-AI/MTK-genio-demo/tree/main)                  |
| YOLOv8n<sub>(fp32) |  ArmNN  | [Genio 510](https://r300-ai.github.io/ITRI-AI-Hub/docs/genio-evk.html) | `Cortex-A` | 895.9              |               |               |                  |[link](https://github.com/R300-AI/MTK-genio-demo/tree/main)                  |
| YOLOv8n<sub>(fp32) |  ArmNN  | [Genio 510](https://r300-ai.github.io/ITRI-AI-Hub/docs/genio-evk.html) | `Mali G57 MC2`   | 572.4              |               |               |                  |[link](https://github.com/R300-AI/MTK-genio-demo/tree/main)                  |
| YOLOv8n<sub>(fp32) |  NeuronRT  | [Genio 510](https://r300-ai.github.io/ITRI-AI-Hub/docs/genio-evk.html) | `MDLA 3.0` | 2.6           | 0.1           |               |                  |[link](https://github.com/R300-AI/MTK-genio-demo/tree/main)                  |

### Keypoint Detection
### Semantic Segmentation
