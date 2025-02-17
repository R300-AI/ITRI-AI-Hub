# Deploy RT-DETR on Kleidi AI

Kleidi AI is an inference engine designed specifically for Cortex-A CPUs and Mali GPUs. Developers can use these processors flexibly to implement high-performance, low-power deep learning operations without additional conversion work.

To illustrate how to delegate a model in ONNX format, we will use the pre-built RTDETRr-l model from Ultralytics as an example. The model is trained on the COCO dataset, which includes 80 categories of objects. Please follow the instructions provided in the previous sections to obtain the model on your workstation. Then, continue with the steps outlined in this document to complete the Python example and verify the inference results.

### Prerequisites

* Any **RT-DETR** model in `ONNX` format obtained from [[Training/Performance Evaluation]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Object-Detection/RT-DETR(preview)) part.
* An **Arm Processors Board** with **Kleidi AI** Library installed. ([[Installation Guide]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/kleidi.html))

## Deploy Sample Codes on Board

**Step 1.** Install dependencies on your board.

```bash
$ pip install -r requirements.txt
```

**Step 2.** Execute an detection for `./bus.jpg`.

```bash
$ python run.py --model_path <path_to_your_model>.onnx
```
