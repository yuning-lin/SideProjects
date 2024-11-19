## 概要
pandasai 可以針對 dataframe 使用 LLM 去做回答問題及繪圖  
但考慮資料安全性及隱私問題所以嘗試使用可以下載到地端的開源模型做測試  

## 使用步驟

### Windows
1. 下載 [ollama](https://ollama.com/download)
2. 確認下載完成，鍵入 `https://ollama.com/download`，在 windows 下載好後會跳出 powershell 的視窗
3. 指令
   
    |指令|意義|
    |----|----|
    |`ollama`|可以看見常用指令|
    |`ollama run mistral`|安裝下載模型（在[官網](https://ollama.com/search)點入想要下載的模型，複製程式碼至 powershell），並且會進入 ollama 的環境|
    |`/bye` 或是 Ctrl + d|跳出 ollama 的環境|
    |`ollama rm mistral`|卸載刪除模型|

### Python

```
pip install pandasai==2.3.0
pip install ollama==0.3.3
```
```python
from pandasai import SmartDataframe
from pandasai.llm.local_llm import LocalLLM

import pandas as pd

llm = LocalLLM(api_base="http://localhost:11434/v1", model="mistral", temperature=0)

table = pd.read_excel(r".\data\test1.xlsx")
print(table)
df_llm = SmartDataframe(table, config={"llm": llm})
df_llm.chat('your questiona bout df')
```
