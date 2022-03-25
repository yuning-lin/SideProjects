## 自動提交表單
1. [建立虛擬環境](https://github.com/yuning-lin/EnvironmentSetup/blob/main/Python/WindowsInstallation.md#%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83)並命名為 env_robot
2. 測試運行提交表單主程式
3. 測試成功後建立工作排程執行檔 .bat
4. 先於 CMD 鍵入 `fsutil file createnew .\env_robot\Lib\site-packages\a.pth 0` 並逐行測試 .bat 程式碼
5. [建立工作排程](https://github.com/yuning-lin/EnvironmentSetup/blob/main/WindowsTaskScheduler/README.md)

## 程式架構
檔名|內容
----|----
config.py|存放參數
main.py|主程式
requirements.txt|使用套件
scheduler.bat|工作排程執行檔

## 常見問題
### 常見 Error 1
  ```python
  selenium.common.exceptions.WebDriverException: Message: ‘chromedriver’ executable needs to be in PATH.
  ```
1. 前往[下載](https://sites.google.com/chromium.org/driver/) Latest stable release 的 Chrome Driver
2. 解壓縮後將 `chromedriver.exe` 移至和主程式同一資料夾下
3. 並且在 .py 檔指定 chrome dirver 的路徑位置：`webdriver.Chrome(executable_path = conf.chrome_path)`

### 常見 Error 2
  ```python
  selenium selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element
  ```
1. 有可能為網頁尚未加載完全就取網頁元素導致
2. 建議可以加入 `time.sleep(3)`