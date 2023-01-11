## Google API
google 有提供眾多功能的 API  
取得憑證及啟用目標 API 即可使用  
當然付費才有更多權限  

## 使用步驟
以 Google Maps Services 的 Places API 為例  
1. 前往 [Google Cloud console](https://console.cloud.google.com/apis/credentials)
2. 同意授權
3. 左列點選程式庫
      
    ![](https://github.com/yuning-lin/SideProjects/blob/main/GoogleMapAPI/Pictures/google_api_lib.PNG)  
      
4. 搜尋目標 API 並點選啟用
      
    ![](https://github.com/yuning-lin/SideProjects/blob/main/GoogleMapAPI/Pictures/google_api_activate.PNG)  
      
5. 點選建立付費帳戶（必須有信用卡資訊才能使用）
      
    ![](https://github.com/yuning-lin/SideProjects/blob/main/GoogleMapAPI/Pictures/google_api_charge.PNG)  
      
6. 返回前頁即可看到 API 已啟用
    
    ![](https://github.com/yuning-lin/SideProjects/blob/main/GoogleMapAPI/Pictures/google_api_activated.PNG)  
      
7. 取得憑證並複製以使用
    
    ![](https://github.com/yuning-lin/SideProjects/blob/main/GoogleMapAPI/Pictures/google_api_key.PNG)  
      
## Python 應用要件
* Python 3.5+
* 根據應用安裝相關套件：`pip install googlemaps`
* Google Maps API key

## 參考資源
* [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python)：Google Maps 相關 API
