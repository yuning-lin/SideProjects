## 計算路徑規劃方法
|爬取[台灣電子地圖服務網](https://www.map.com.tw/)|免費，但導航分析的功能無法使用|
|爬取[全國門牌地址定位服務](https://tgos.nat.gov.tw/TGOS/Web/Address/TGOS_Address.aspx)|免費，但路徑規劃功能無法使用|
|爬取 google map 資訊|免費，但有筆數限制、且單點對多點的距離計算有限，對於`鄰`會有查詢不到的情形|
|[Google Distance Matrix API](https://console.cloud.google.com/apis/dashboard?project=_)|每月可獲得 USD 200.00 的免費額度，可用於地圖、路徑與地點；超過額度依筆數計算價錢|

## Google Distance Matrix API 使用步驟
1. [前往 Google Cloud Platform](https://console.cloud.google.com/apis/dashboard?project=_)
2. 建立專案
3. 前往搜尋列中輸入「Distance Matrix API」
4. 點選啟用 > 點選欲啟用的專案
5. 點選左列`憑證` > ＋建立憑證 > API 金鑰
注：必須 enable [繳費功能](https://console.cloud.google.com/project/_/billing/enable)

## 計算雷達搜尋
```python
latlon = (緯度, 經度)
radius = 25000
place_type = 'restaurant'
places_radar_result = gmaps.places_radar(latlon, radius, type=place_type)
```

## 計算兩點距離
```python
import googlemaps
original_latlon = (緯度, 經度)
destination_latlon = (緯度, 經度)
gmaps = googlemaps.Client(key = conf.google_api_key)
distance = gmaps.distance_matrix(original_latlon, destination_latlon, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
```

## 參考資料
* [官方：使用用戶端內含的 API 功能有哪些](https://developers.google.com/maps/web-services/client-library?hl=zh-tw)
* [官方：Distance Matrix API Introduction](https://developers.google.com/maps/documentation/distance-matrix/overview)
* [部落格：How to use Google Distance Matrix API in Python](https://medium.com/how-to-use-google-distance-matrix-api-in-python/how-to-use-google-distance-matrix-api-in-python-ef9cd895303c)
* [部落格：Google Maps API 學習筆記](https://www.letswrite.tw/google-map-api-distance-matrix/)
* [部落格：使用 Python 抓取 Google Maps API 地標資料](https://blog.goodjack.tw/2017/11/python-google-maps-api.html)