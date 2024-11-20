

|  Model     | Size        |  mAP<sub>50     |  mAP<sub>50-95     |
|------------|-------------|-----------------|--------------------|
| [SmolLM2](https://ollama.com/library/smollm2:135m)    |270 MB       |0.63             | 0.45               |
| [Qwen2.5](https://ollama.com/library/qwen2.5:0.5b)    |397 MB       |0.63             | 0.44               |
| [Llama 3.2](https://ollama.com/library/llama3.2)      |1.3 MB       |0.77             | 0.51               |


```
ollama run smollm:135m "def print_hello_world():" --verbose
ollama run qwen2.5:0.5b "Give me a short introduction to large language model." --verbose
ollama run llama3.2:1b "The key to life is" --verbose
```
