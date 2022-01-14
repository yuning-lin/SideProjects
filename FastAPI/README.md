## 安裝套件
python 環境需在 3.6 以上才能使用  
```
pip install fastapi # 建立高效能的 web 框架
pip install uvicorn # ASGI Server 提供非同步能力的 Python Web server、框架、應用程式
pip install uvicorn[standard]  # This will install uvicorn with minimal (pure Python) dependencies.
```
## 基本流程
1. 建立 FastAPI 文件
    * create decorator with different operation（decorator:`@something`）［1］
    * define decorator with (async) function［2］
      * 關於要不要使用異步函數（async function），可以參考[官方文件](https://fastapi.tiangolo.com/async/#in-a-hurry)，
    * return content［3］
      
    以下例對應步驟：   
       
   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/") #［1］
   async def root(): #［2］
       return {"message": "Hello World"} #［3］
   ```
2. uvicorn 引用已建立的 FastAPI 文件  
     
   在 bash 啟動虛擬環境後，輸入 `uvicorn main:app --reload`
      * main：儲存創建 app 的 python 檔名，EX：main.py
      * app：創建 api 的對象，EX：app = FastAPI()
      * --reload：讓 server 在更新程式內容並**儲存**後會重新載入，適用於開發階段
      * 若 main 在 Code 這個資料夾下，可以下 `unicorn Code.main:app --reload`
3. 在本機提供的 URL 做查看
   網址|內容
   ----|----
   http://127.0.0.1:8000/|看到測試的 json 響應等
   http://127.0.0.1:8000/docs|看到 Swagger UI 提供的交互式 API 文檔
   http://127.0.0.1:8000/redoc|看到 ReDoc 提供自動生成的文檔
   http://127.0.0.1:8000/openapi.json|查看 OpenAPI 原始模式
   
## 註解
[Operation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)：在此代表某種 HTTP 方法，在開發 API 時常用到  
常見 Operation：
指令|意義
----|----
GET|獲取資料
POST|創建資料
PUT|更新資料
DELETE|刪除資料
  
其他 Operation：  
指令|意義
----|----
HEAD|獲取沒有正文的資料
CONNECT|建立到被目標資源標示的 server 的通道
OPTIONS|描述目標資源的溝通選項
TRACE|執行沿著到目標資源路徑的 message loop-back test
PATCH|對資源進行部分修改


## 補充說明
* [fastapi official site](https://fastapi.tiangolo.com/)
* [uvicorn official site](https://www.uvicorn.org/)
* [淺談 Coroutine 協程使用方法（含 async function 示例）](https://www.maxlist.xyz/2020/03/29/python-coroutine/)
