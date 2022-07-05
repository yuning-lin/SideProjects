## 情境
如何快速讓沒有安裝 python 的電腦應用寫好的功能？  

## 套件 
* `pip install auto-py-to-exe`：使用 GUI 的畫面操作 pyinstaller 打包專案成 .exe
* `pip install pyinstaller`：使用指令操作 pyinstaller 打包專案成 .exe
* 可以使用 `auto-py-to-exe --version`、`pyinstaller --version` 檢查是否安裝成功

## 步驟
1. 建立專案虛擬環境並完成專案程式邏輯
2. WINDOWS 使用者：於 CMD、POWER SHELL 激活該專案虛擬環境
    * 於 CMD：`env_test\Scripts\activate`
    * 因為 pyinstaller 會將使用到的套件也做打包，所以建議建立乾淨的虛擬環境
3. 以專案架構舉例：
    * 打包時僅需使用 main.py 即可，即使 main.py 會呼叫 func1.py、func2.py
    * 打包前架構如下
    ```
    project
    │   README.md
    │   main.py 
    │   func1.py
    │   func2.py
    │
    └───folder1
    │   │   file011.csv
    │   │   file012.csv
    │   
    └───folder2
        │   file021.ppt
        │   file022.ppt
    ```
    * 於 CMD ：`pyinstaller -D main.py` > 在 dist 下打包成一個檔案，因為單一檔案要包山包海，執行時間較久，適合小型專案
    * 於 CMD ：`pyinstaller -F main.py` > 在 dist 下打包成一個資料夾，會有其他用到的檔案一放置於資料夾中，執行時間較快
    * `pyinstaller -F main.py` 打包後架構如下
    ```
    project
    │   README.md
    │   main.py 
    │   func1.py
    │   func2.py
    │
    └───dist
    │   │
    │   └───main
    │       │   main.exe
    │       │   python36.dll
    │       │   ...
    │
    └───build
    │   │
    │   └───main
    │       │   main.exe
    │       │   ...
    │
    └───main.spec
    │
    └───folder1
    │   │   file011.csv
    │   │   file012.csv
    │   
    └───folder2
        │   file021.ppt
        │   file022.ppt
    ```
4. 若 main.py 有讀 folder1 下的檔，則須將 folder1 移至與 main.exe 同層
5. 建議於 CMD 先測試 .exe，如此可以看見程式錯誤於何處
    * 於 CMD：cd 至資料夾 dist/main 下，鍵入 main.exe，觀察運行情況
    * 再直接至資料夾 dist/main 下，點兩下 main.exe 觀察是否執行成功
6. 最後將 main 這個 folder 壓縮傳送給使用者即可
