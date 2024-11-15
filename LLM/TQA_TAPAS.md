## 概要
不同訓練方式的模型，需要用不同方式引入  
以下範例為用 TAPAS 為 base 的模型  

## 參考資源
* [Tabular-Question-Answering-on-Relational-data-and-CSV-data-with-Gemini-LLM](https://github.com/Pavansomisetty21/Tabular-Question-Answering-on-Relational-data-and-CSV-data-with-Gemini-LLM)
* [Machine Learning for Table Parsing: TAPAS](https://github.com/christianversloot/machine-learning-articles/blob/main/easy-table-parsing-with-tapas-machine-learning-and-huggingface-transformers.md)
* [DOCS：TAPAS](https://huggingface.co/transformers/v4.8.0/model_doc/tapas.html)

## 範例程式：下載 tapas local model 做 inference
```python
from transformers import TapasTokenizer, TapasForQuestionAnswering

import pandas as pd

local_model_path = r".\llm_model\tapas\tapas-tiny-finetuned-sqa"  # 指定本地模型路徑

# Step 1: Prepare your table as a pandas DataFrame
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": ["24", "19", "22"],
#     "City": ["New York", "Los Angeles", "Chicago"]
# }
# table = pd.DataFrame.from_dict(data)
table = pd.read_excel(r".\data\test1.xlsx")
table = table.astype("str")

# Step 2: Prepare your question
question = "What is the age of Bob?"

# Step 3: Tokenize the inputs
tokenizer = TapasTokenizer.from_pretrained(local_model_path)  # "google/tapas-base-finetuned-wtq"
inputs = tokenizer(table=table, queries=question, padding="max_length", return_tensors="pt")

# Step 4: Run the model
model = TapasForQuestionAnswering.from_pretrained(local_model_path)  # "google/tapas-base-finetuned-wtq"
outputs = model(**inputs)

# Step 5: Post-process the output to get the answer
if hasattr(outputs, 'logits_aggregation') and outputs.logits_aggregation is not None:
    logits_aggregation = outputs.logits_aggregation.detach()
    results = tokenizer.convert_logits_to_predictions(
        inputs, outputs.logits.detach(), logits_aggregation
    )
else:
    results = tokenizer.convert_logits_to_predictions(
        inputs, outputs.logits.detach()
    )

# Extract results
if len(results) == 2:
    predicted_answer_coordinates, predicted_aggregation_index = results
else:
    predicted_answer_coordinates = results[0]
    predicted_aggregation_index = None

# Debug: Print the predicted answer coordinates
print(f"Predicted answer coordinates: {predicted_answer_coordinates}")

# Check if coordinates exist and are valid
if predicted_answer_coordinates:
    try:
        # Unpack the coordinates from the nested list
        row_index, col_index = predicted_answer_coordinates[0][0]
        # If the predicted answer is a cell, extract the cell's value
        answer = table.iat[row_index, col_index]
    except IndexError:
        answer = "Invalid answer coordinates: out of range"
else:
    answer = "No answer found"

print(f"Question: {question}")
print(f"Answer: {answer}")

```
