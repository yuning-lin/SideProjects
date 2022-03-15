## 程式結構
|檔名|功能|
|-----|-----|
|database.py|連接 DB 路徑 > 創建 engine > 創建 Session > 宣告 mapping（Base）|
|main.py|若表格不在則創建表格；在則保持原樣 > 執行串接並在所有動作完成後關閉 DB|
|models.py|從 database.py 的設置，創建表格的 schema；直接執行此檔即可創建 DB|
|schemas.py|pydantic BaseModel 的參數設置|
|requirements.txt|使用套件及對應版本|

### main.py 程式內容
* @app.post：內容寫入 DB 的動作
* @app.get：取出表所有資料、取出表中指定資料
* @app.delete：刪除資料
* @app.put：有資料存在才更新資料，否則 error messages
* 指定 status code、error messages
* 加入 tags 可以將功能分區

## 程式運行步驟
1. `pip install -r requirements.txt` 下載所需套件
2. 創建 DB（By [TablePlus](https://github.com/yuning-lin/EnvironmentSetup/tree/main/TablePlus), [SQLite](https://github.com/yuning-lin/EnvironmentSetup/tree/main/SQLite),...）
3. 在終端機下：`uvicorn main:app --reload`
4. 開啟 [Swagger UI](http://127.0.0.1:8000/docs) refresh 網頁測試程式執行
