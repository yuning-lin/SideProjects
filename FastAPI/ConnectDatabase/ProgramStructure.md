## 程式結構
|檔名|功能|
|-----|-----|
|database.py|連接 DB 路徑 > 創建 engine > 創建 Session > 宣告 mapping（Base）|
|main.py|若表格不在則創建表格；在則保持原樣 > 執行串接 @app.post 的內容寫入 DB 的動作、@app.get 取出表所有資料、@app.get 取出表中指定資料，並在所有動作完成後關閉 DB|
|models.py|從 database.py 的設置，創建表格的 schema；直接執行此檔即可創建 DB|
|schemas.py|pydantic BaseModel 的參數設置|
|requirements.txt|使用套件及對應版本|

## 程式運行步驟
1. `pip install -r requirements.txt` 下載所需套件
2. 創建 DB（By [TablePlus](https://github.com/yuning-lin/EnvironmentSetup/tree/main/TablePlus), [SQLite](https://github.com/yuning-lin/EnvironmentSetup/tree/main/SQLite),...）
3. 
