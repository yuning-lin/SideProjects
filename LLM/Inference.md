## 簡介
簡單介紹如何在地端快速 inference 大型語言模型  

## 所需套件
```python
pip install transformers
pip install torch
pip install accelerate
```

### 方法一：pipeline 
pipeline 是 Transformer 提供可以處理常見的 NLP 任務和預訓練模型間的接口  
[常見的 NLP 任務](https://huggingface.co/docs/transformers/main_classes/pipelines)有：question-answering、summarization、text-generation 等

Example from HuggingFace: [sample inference code of Phi-3-mini](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct",
    device_map="cpu",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

messages = [
    {"role": "system", "content": "You are a helpful digital assistant. Please provide safe, ethical and accurate information to the user."},
    {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
    {"role": "assistant", "content": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."},
    {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"},
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.0,
    "do_sample": False,
}

output = pipe(messages, **generation_args)
print(output[0]['generated_text'])
```

