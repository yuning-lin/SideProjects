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

### 常見 Error 3
  ```python
  [16068:2596:0328/093602.183:ERROR:device_event_log_impl.cc(214)] [09:36:02.184] Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed.
  ```
1. [相關討論](https://stackoverflow.com/questions/61561112/how-to-solve-getting-default-adapter-failed-error-when-launching-chrome-and-tr)
2. 加入以下程式碼，可以解決
      ```python
      options = webdriver.ChromeOptions() 
      options.add_experimental_option("excludeSwitches", ["enable-logging"])
      ```
### 常見 Error 4
  ```python
  selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 99 Current browser version is 102.0.5005.115 with binary
  ```
 1. 由於 browser 常會自動更新，此時就會跟下載的 chromedriver 版本不同
 2. 故[此套件](https://pypi.org/project/webdriver-manager/)會取得和 browser 相符的 chromedriver
 3. `pip install webdriver-manager` 
 4. 原程式碼（上）改成會自動更新 chromedriver 的程式碼（下）
      ```python
      from selenium import webdriver
      driver = webdriver.Chrome(executable_path = conf.chrome_path)
      ```
      ```python
      from selenium import webdriver
      from webdriver_manager.chrome import ChromeDriverManager
      driver = webdriver.Chrome(ChromeDriverManager(path=conf.chrome_path).install())
      ```
 ### 常見 Error 5
  ```python
  webdriver.Chrome(ChromeDriverManager(path).install()) TypeError: __init__() got multiple values for argument 'executable_path'
  ```
  1.  `executable_path = conf.chrome_path`、`ChromeDriverManager(path=conf.chrome_path).install()` 不能同時出現
  2.  解法如上方所示
      ```python
      from selenium import webdriver
      from webdriver_manager.chrome import ChromeDriverManager
      driver = webdriver.Chrome(ChromeDriverManager(path=conf.chrome_path).install())
      ```
