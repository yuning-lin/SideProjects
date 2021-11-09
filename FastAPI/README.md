## 功能簡介
## 安裝套件
python 環境需在 3.6 以上才能使用  
```
pip install fastapi # 建立高效能的 web 框架
pip install uvicorn # ASGI Server 提供非同步能力的 Python Web server、框架、應用程式
pip install uvicorn[standard]  # This will install uvicorn with minimal (pure Python) dependencies.
```
## 基本流程
1. 建立 FastAPI 文件
    * create decorator（decorator:`@something`）
    * define decorator with (async) function
    * return content
3. uvicorn 引用已建立的 FastAPI 文件 

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
