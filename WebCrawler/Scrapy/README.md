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
`scrapy crawl 爬蟲.py名稱 -o 輸出檔案名稱`|輸出爬取內容並命名，附檔可為 json,csv,xml|`scrapy crawl lottery -o result.json`


## 檔案架構
```
project
│   scrapy.cfg（scrapy 專案部署設定檔）
│
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

## 參考資源
* [Docs：Scrapy](https://docs.scrapy.org/en/latest/index.html)
* [Docs：Scrapy Documentation 2017](https://docs.scrapy.org/_/downloads/en/xpath-tutorial/pdf/)
* [GitHub：Scrapy with selenium](https://github.com/clemfromspace/scrapy-selenium)
* [GitHub：Scrapyscript](https://github.com/jschnurr/scrapyscript)
* [Blog：Scrapy教學系列](https://www.learncodewithmike.com/search/label/Scrapy%E6%95%99%E5%AD%B8%E7%B3%BB%E5%88%97)
* [Blog：Scrapy + Python 3: PTT 資料抓取與分析](https://jasonblog.github.io/note/python/scrapy_+_python_3_ptt_zi_liao_zhua_qu_yu_fen_xi.html)
* [Blog：Scrapy爬蟲與資料處理30天筆記](https://ithelp.ithome.com.tw/users/20107514/ironman/1919)
* [Blog：scrapy數據解析 | xpath | CSS | re](https://blog.csdn.net/Heart_for_Ling/article/details/103590220)
* [Blog：Scrapy中XPath選擇器的基本用法](https://blog.csdn.net/qq_27283619/article/details/88704479)
* [stackoverflow：scrapyscript](https://stackoverflow.com/questions/40237952/get-scrapy-crawler-output-results-in-script-file-function)
