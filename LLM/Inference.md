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

### 方法二：下載模型
在任意 HuggingFace 平台上的[模型頁面](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)  
和 Model card, Filesand versions, Community 同階層有直列的三個點  
左鍵點選後 > 點選 Clone repository > 第一次下載 LLM 需先安裝 `git lfs install` 才得以下載如此大的檔案 > `git clone https://huggingface.co/microsoft/Phi-3-mini-128k-instruct`  
  
Example：
```python
messages = [
    {"role": "system", "content": "You are a helpful digital assistant. Please provide safe, ethical and accurate information to the user."},
    {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
    {"role": "assistant", "content": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."},
    {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"},
]
llm_model_path = "/llm_test/llm_models/Phi-3-mini-128k-instruct"
model = AutoModelForCausalLM.from_pretrained(
    llm_model_path,
    device_map="cpu",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(llm_model_path)
tokenizer.chat_template = "{% for message in messages %}{% if loop.first %}[gMASK]sop<|{{ message['role'] }}|> \n {{ message['content'] }}{% else %}<|{{ message['role'] }}|> \n {{ message['content'] }}{% endif %}{% endfor %}{% if add_generation_prompt %}<|assistant|>{% endif %}"
input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_tensors="pt")

output_ids = model.generate(
    input_ids=input_ids,
    max_new_tokens=500,
    temperature=0.0,
    do_sample=False,
)

print(tokenizer.decode(output_ids[0], skip_special_tokens=True))
```
