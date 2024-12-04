# About Ollama
# Benchmarks
## Inference/Performance Evaluation

|  Model         | Size        |  Max Speed<sub>tokens/s     |  Memory Usage     |  Memory Usage     |
|----------------|-------------|-----------------------------|-------------------|-------------------|
| smollm2:135m   |270 MB       |5.74                         |                   |                   |
| smollm2:360m   |726 MB       |                             |                   |                   |
| smollm2:1.7b   |1.8 GB       |                             |                   |                   |
| qwen2.5:0.5b   |397 MB       |5.74                         |                   |                   |
| qwen2.5:1.5b   |986 MB       |                             |                   |                   |
| qwen2.5:3b     |1.9 GB       |                             |                   |                   |
| qwen2.5:7b     |4.7 GB       |                             |                   |                   |
| llama3.2:1b    |1.3 GB       |6.09                         |                   |                   |
| llama3.2:3b    |2.0 GB       |                             |                   |                   |
| phi3.5         |2.2 GB       |                             |                   |                   |

```bash
ollama run smollm2:135m "Gravity is" --verbose

# >> Gravity. A fundamental concept in physics that has puzzled mathematicians and physicists for centuries. It arises from the way objects fall towards the ground due to gravity. However, it's fascinating to note that gravitational mass doesn't exactly depend on its density or composition - a subtle difference between gravity and inertia can arise.
```
```bash
ollama run qwen2.5:0.5b "Give me a short introduction to large language model." --verbose

# >> Certainly! A large language model (LLM) is a type of artificial intelligence system designed and trained using deep learning algorithms. These models can generate human-like text and perform specific tasks such as translation, summarization, machine translation, and more.
```
```bash
ollama run llama3.2:1b "The key to life is" --verbose

# >> It sounds like you're about to share something interesting. The phrase "The key to life" can refer to various things, and I'm curious - what are your thoughts on it? Are you looking for inspiration, wisdom, or perhaps a specific insight that will help guide you through life's journey?
```
