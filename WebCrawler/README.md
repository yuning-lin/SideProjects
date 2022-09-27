## 引入套件
* BeatifulSoup
* Selenium
* Scrapy

## 套件比較
了解其各自特性後，三種套件皆可搭配使用  
套件名稱|特性|難易程度|參考實作
----|----|----|----
BeatifulSoup|* 可擷取 HTML／XML 資訊 <br> * 通常會搭配套件 Requests 使用 <br> * 適合靜態網頁爬取|低|[爬取 0050 成分股](https://github.com/yuning-lin/SideProjects/blob/main/WebCrawler/Crawling_0050ConstituentStocks.ipynb)
Selenium|* 可爬取網頁有使用動態載入技術如 JavaScript / AJAX <br> * 擬人化操作適用於須登入、驗證、搜尋等網頁|中|
Scrapy|* 有相對完整且較易維護的爬蟲框架 <br> * 有較佳的執行速度適用於大型爬蟲專案|高|

## [主題：爬取 0050 成分股](https://github.com/yuning-lin/SideProjects/blob/main/WebCrawler/Crawling_0050ConstituentStocks.ipynb) 
示範 Requests（get）＋BeatifulSoup
