## 簡介
是 IBM 開發的求解器，在求解線性規劃上有不錯的表現  
但其為商用軟體，除非有學術需求，否則須自行購買才具有不受限的使用權限  
不同問題求最佳化有不同選擇，如[官網](https://www.ibm.com/docs/en/icos/12.8.0.0?topic=cplex-optimizer-options)所列  
用 python 接 CPLEX 的教學可見於[此](https://www.ibm.com/docs/en/icos/12.8.0.0?topic=tutorials-python-tutorial)  
以 Windows 10 為例進行安裝教學  

## 環境
* python 需為在 64 位元的作業系統上，並且版本 >= 3.6
* CPLEX 安裝的版本需對應 python 版本

## 安裝
有兩種方式：  
* 使用 pip：`pip install cplex docplex`
  * 這種安裝方法，用的 CPLEX 有限制變數和限制式數量
* 使用 IBM Installer
  1. 進入 IBM 官網[建立帳戶](https://www.ibm.com/account/reg/tw-zh/signup?formid=urx-19776&target=https%3A%2F%2Flogin.ibm.com%2Foidc%2Fendpoint%2Fdefault%2Fauthorize%3FqsId%3D134348ec-7617-4c01-ae40-c6cb1ad729bd%26client_id%3Dv18LoginProdCI)
    
  ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/cplex_log_in_myibm.PNG)
  
  2. 右上角點選＞My IBM＞登入帳密＞尋找產品輸入：CPLEX
  
  ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/cplex_search_product.PNG)
    
    *  點選中間[一般管道](https://www.ibm.com/tw-zh/products/ilog-cplex-optimization-studio?lnk=STW_TW_STESCH&lnk2=trial_ILOGOptStudio&pexp=def&psrc=none&mhsrc=ibmsearch_a&mhq=CPLEX)填寫資訊後方可下載
    *  點選右項[學術管道](https://www.ibm.com/academic/topic/data-science)填寫資訊後方可下載
        
    ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/cplex_academic_software.PNG)
        
  3. 這邊示範的是一般管道中的免費試用版，點選自己的作業系統下載
  
  ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/cplex_click_download_by_os.PNG)
  
  5. 下載完後，預設的路徑 yourCPLEXhome\python\VERSION\PLATFORM 下打開終端機並下指令 `python setup.py install`
* 兩種方法擇一下載後，就可以使用 python 呼叫 docplex 進行 programming 的部分

## 更多資源
* [Cplex Python: Installation, API, and Examples](https://www.pythonpool.com/cplex-python/)
* [Resource to learn Python](http://ibmdecisionoptimization.github.io/docplex-doc/getting_started_python.html)
