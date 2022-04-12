## 主題
### Situation
**想知道有興趣的建案和公司行車距離，但物件繁多無法用人腦記憶**
### Task
1. 需事先收集有興趣建案的地址（因為需經個人喜好挑選，所以此步為人工紀錄）
2. 並計算個別行車距離才能做排序或畫圖
### Action
1. 獲得人工地址收集後須將地址轉經緯度
2. 因為建案很多地址是模糊的，故採用模糊地址查詢錯誤機會較小的全國門牌地址定位服務
3. 全國門牌地址定位服務為 TWD97，要能計算行車距離需轉成經緯度 WGS84
4. 網路提供的同一建案有多個地址，將返還的地址經緯度做平均
5. 有了經緯度才能當  Google Maps Distance Matrix API 的計算參數 
### Result
* 可以根據建案格局、距目標地行車距離做篩選及排序

## 前言
在計算行車距離前須先有經緯度  
以下比較不同方法查詢經緯度的差別：

|方法|優缺點|
|----|----|
|使用 [Geocoding API](http://g.co/dev/maps-no-account)| 需先申請每轉換一千筆就要五美元的 API KEY|
|爬取 `https://www.google.com/maps/place?q=地名或地址` |免費，但僅能爬取一百多筆，即要再等候一段時間才能再爬|
|爬取[台灣電子地圖服務網](https://www.map.com.tw/)|免費，但需要精準地址，否則容易出錯|
|爬取[全國門牌地址定位服務](https://tgos.nat.gov.tw/TGOS/Web/Address/TGOS_Address.aspx)|免費，可以不用精準地址，但會回吐多個精準地址|
  
EX：同樣查詢「新竹縣竹北市新瀧五街口」
* 台灣電子地圖服務網：將其定位到「新竹縣竹北市公所」
* 全國門牌地址定位服務：回吐多個詳細地址，由於應用只會有某某街口，故都取第一個地址代替

參考資料：
* [批量處理地址轉換經緯度](https://medium.com/%E8%8A%B1%E5%93%A5%E7%9A%84%E5%A5%87%E5%B9%BB%E6%97%85%E7%A8%8B/geocoding-%E6%89%B9%E9%87%8F%E8%99%95%E7%90%86%E5%9C%B0%E5%9D%80%E8%BD%89%E6%8F%9B%E7%B6%93%E7%B7%AF%E5%BA%A6-721ab2564c88)
* [留言區：TWD97坐標轉換](http://fyyang.blogspot.com/2012/09/python-twd97.html)

## 所需套件
|名稱|用途|
|----|----|
|pandas|用於資料表合併、增減|
|concurrent.futures|平行化處理程式|
|tqdm|顯示進度條|
|time|用於網頁開啟後做停留以利爬取|
|random|隨機生成停留時間防拜訪網頁被阻擋|
|selenium|用於爬蟲|
|pyproj|用於 TWD97 和 WGS84 互相轉換|

## 程式內容
|檔名|內容|
|----|----|
|config.py|置放路徑、參數|
|collect_data.py|收集模糊地址的經緯度|
|calculate_distance.py|利用爬蟲 google map 計算行車距離|
|GoogleMapsDistanceMatrixAPI.md|Google Maps Distance Matrix API 計算行車距離|


