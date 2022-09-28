## 安裝
* `pip install scrapy`

## 常見錯誤訊息
* Error：
  ```
  Microsoft Visual C++ 14.0 is required
  ```
  * Solution：[Visual Studio 官方下載區](https://visualstudio.microsoft.com/downloads/) > 下載「Microsoft Build Tools 20XX」
* Error：
  ```
  AttributeError: module 'OpenSSL.SSL' has no attribute 'SSLv3_METHOD'
  ```
  * Solution：`pip install pyOpenSSL==22.0.0` 

## scrapy 終端機語法
語法|意義|範例
----|----|----
`scrapy bench`|檢視是否安裝成功
`scrapy startproject your_project_name .`|建置 scrapy 專案於當前目錄下，並命名為 your_project_name|`scrapy startproject crawler .`
`scrapy genspider 爬蟲.py名稱 目標網站網域名稱`|建立目標網站爬蟲檔案|`scrapy genspider lottery www.taiwanlottery.com.tw`
`scrapy crawl 爬蟲.py名稱`|爬取目標網站|`scrapy crawl lottery`

## 檔案架構
```
project
│   scrapy.cfg（scrapy 專案部署設定檔）
└───crawler
    │   __init__.py
    │   items.py（定義欲爬取或儲存的資料欄位）
    │   middlewares.py（定義 spiders＆ENGINE、ENGINE＆DOWNLOADER 間的中間件）
    │   pipelines.py（定義 items.py 資料的 ETL 處理）
    |   settings.py（scrapy 專案設定檔，EX：USER_AGENT 等）
    │
    └───spiders（放網頁爬蟲 .py）
        │   __init__.py
        │   lottery.py
```
