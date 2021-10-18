## 簡介
AIOps（Artificial Intelligence for IT Operations，智慧維運）  
即利用大數據結合機器學習，來達到全／半自動化流程或監控的功能  
中國自 2018 開始有智慧維運相關的大型比賽，比賽的資料多來自知名企業  
故 side project 內容以 KPI 異常檢測為題，  
通過演算法學習 KPI 的訓練集時間序列數據，對測試集資料做是否為異常的判斷    
內容根據 2018 年的冠軍的報告內容與報導，並參考網上他人實作，推測冠軍做法並還原之  

## 專案步驟
1. 讀檔［注：讀 .hdf］
2. 原值做 MinMaxScaler
3. MinMaxScaler 後的值做特徵工程［注：特徵工程內容參考他人實作］
4. 每個特徵各自做 StandardScaler
5. 過取樣［注：放大頭七個異常的取樣次數］
6. 切分資料為訓練及驗證集［注：8:2］
7. 訓練集建模
8. 網格搜尋最佳閾值［注：用比賽的變形 fscore，參用他人實作的評估方式］
9. 比對模型判斷測試集結果

## 檔案內容
內容|檔名
----|----
預賽訓練、測試集|[data set](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master/Preliminary_dataset)
決賽訓練集|phase2_train.csv
決賽測試集|phase2_ground_truth.hdf（需先解壓縮）
使用套件|requirements.txt（需先解壓縮）
專案主檔|implementation.ipynb

## 參考來源
* [競賽頁面](http://iops.ai/competition_list/)
* [歷屆研討會](https://workshop.aiops.org/)
* [KPI 異常檢測](http://iops.ai/problem_detail/?id=5)
* [2018 冠軍專訪](http://blog.itpub.net/31562044/viewspace-2285169/)
* [他人實作](https://github.com/chengqianghuang/exp-anomaly-detector-AIOps)
* [資料來源](https://github.com/NetManAIOps/KPI-Anomaly-Detection)
