## 文件簡介
SCIP 可以用來解決線性規劃、非線性規劃、整數規劃、混合整數規劃  
且在各個 solver 的比較上，效能、能處理的問題、價格上都相對表現不錯  
但 SCIP 在實際安裝的過程有碰到一些問題      
所以在此檔紀錄如何解決的步驟  

## 軟體版本
軟體|版本
---|---
Windows|10 1909
Python|3.9
SCIP|SCIPOptSuite-7.0.3-win64-VS15

## 安裝步驟
1. [於官網下載 SCIP](https://www.scipopt.org/index.php#download)
2. 填入個人資料始可下載
3. 雙擊 `SCIPOptSuite-7.0.3-win64-VS15.exe` 以安裝
4. 新增環境變數：
    * 直接在搜尋＞進階系統設定＞環境變數＞系統變數（S）＞path＞新增環境變數 `C:\Program Files\SCIPOptSuite 7.0.3\bin`
    * 在 CMD 激活虛擬環境後，鍵入 `set PATH=%PATH%;%SCIPOPTDIR%\bin` ，用 `echo %PATH%` 確認 PATH 這個變數內有無剛填的路徑
    * 在 git bash 激活虛擬環境後，鍵入 `export SCIPOPTDIR="C:\Program Files\SCIPOptSuite 7.0.3"` ，用 `printenv` 確認 PATH 這個變數內有無剛填的路徑
6. 重新開機
7. 安裝套件：
    ```
    python -m pip install pyscipopt
    pip install cython
    pip install wheel
    ```

## 安裝 pyscipopt 後，錯誤訊息
* 如果出現以下錯誤，則[安裝 Microsoft Visual C++](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 
  ```
  error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
  ```
* 如果出現以下錯誤，則
  ```
  src\pyscipopt\scip.c(640): fatal error C1083: \xe7\x84▒▒\xb3\x95\xe9\x96\x8b\xe5\x95\x9f\xe5\x8c\x85\xe5\x90▒▒\xaa\x94▒\x88: 'scip/scip.h': No such file or directory
  ```
  1. XXX的使用者變數、系統變數的 path 都確認有新增環境變數 `C:\Program Files\SCIPOptSuite 7.0.3\bin`
    
    ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/SCIP_add_env_var.PNG)
    
  2. XXX的使用者變數新增變數名稱：SCIPOPTDIR、變數值：`C:\Program Files\SCIPOptSuite 7.0.3`。即圖中藍底部分。
    
    ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/SCIP_add_path.PNG)
   
## 儲存格式
在寫完程式邏輯可以儲存檔案檢查邏輯是否正確  
```python
model.writeProblem("model.cip")
model.readProblem("model.cip")

model.writeProblem("model.lp") 
model.readProblem("model.lp")
```
* cip：人類可以閱讀的格式
* lp：線性規劃模型常用的格式
   * 注意：若要存成 .lp，限制式加註解要小心，在讀檔時比較會有問題
   * EX：model.addCons(a+b>=10, ~~"equation 1"~~)

## 資料來源
* [PySCIPOpt](https://github.com/scipopt/PySCIPOpt)
* [Building SCIP using CMake](https://www.scipopt.org/doc/html/md_INSTALL.php#CMAKE)
* [PySCIPOpt－INSTALL](https://github.com/scipopt/PySCIPOpt/blob/master/INSTALL.md)
* [Tutor: how to install Microsoft Visual C++](https://stackoverflow.com/questions/64261546/python-cant-install-packages)
