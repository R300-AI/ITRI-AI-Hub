# About RT-DETR

The RT-DETR family of models referenced in this guide are provided by **Ultralytics**. This document aims to demonstrate how users can quickly train and acquire customized models for deployment to a given system. It is important to note that these models are intended for educational and demonstration purposes only. For any commercial or product-level deployments, users must thoroughly review the official **AGPL-3.0** license terms and comply with the licensing requirements to ensure proper use and distribution of the models. Users are responsible for ensuring that their use of the models does not infringe on any legal or copyright regulations.

# Benchmarks
## Training/Performance Evaluation 

In the training and validation demonstration, we can utilized open-source datasets such as COCO8, Objects365, LVIS...etc. All these datasets are automatically downloaded through the Ultralytics API. You can also create your own custom datasets for training by following the guidelines in the [[Training Notebook]], and export it by [[Delegating Notebook]](). The following metrics are from previous benchmarks measured based on **COCO8**, include the processing time for 100 epochs, mean Average Precision (mAP) at IoU threshold 0.50 (mAP<sub>50</sub>), and mean Average Precision across IoU thresholds from 0.50 to 0.95 (mAP<sub>50-95</sub>).

|  Model     |  params<sub>(M)     | Time (hr)<br>T4 GPU   |  mAP<sub>50     |  mAP<sub>50-95     | Pre-built Models   |
|------------|-------|-----------------------|-----------------|--------------------|--------------------|
| rtdetr-l    |32.97  |                       |                 |                    |[[ONNX]]() |
| rtdetr-x    |67.46  |                       |                 |                    |[[ONNX]]() |


These training sessions were executed on a **CUDA Workstation** equipped with a T4 GPU. To train your own model or reproduce the results above, here we provide instructions to get started:

**Step 1**. Clone expected **Jupyter Notebook** to your Workstation.

* [How to setup GPU for your own workstation?](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/workstation.html)

**Step 2**. Create an environment and install dependencies.

```bash
$ conda create --name ultralytics python=3.11 && conda activate ultralytics
(ultralytics)$ pip install -r requirements.txt
```

**Step 3**. Open **Jupyter Notebook** to execute the Training and Export Tutorial.

```bash
& conda activate ultralytics
(ultralytics)$ jupyter notebook
```

## Inference Speed 

| Model               | Genio510<br><sub>KleidiAI | Genio510<br><sub>NeuronRT | Genio700<br><sub>KleidiAI | Genio700<br><sub>NeuronRT | Genio1200<br><sub>KleidiAI |
|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|
| rtdetr-l<sub> (fp32) |                       |                       |                       |                       |                        |
| rtdetr-x<sub> (fp32) |                       |                       |                       |                       |                        |

## Memory Usage
## Power Consumption
