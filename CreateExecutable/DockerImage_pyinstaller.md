## 使用情境
原方法在 Windows 上打包好的執行檔僅能在 Windows 上運行，無法給 Mac 使用  
若在 Mac 直接打開會出現：`There was a problem while reading the contents of "main.exe": Data is corrupted`
故以下利用 docker image 處理跨平台打包執行檔  
並以在 **Windows 上打包給 Mac** 使用的執行檔為例  

## 操作步驟
0. 先將[ python 用 pyinstaller 打包成執行檔](https://github.com/yuning-lin/SideProjects/edit/main/CreateExecutable/README.md)
1. [下載 Docker](https://github.com/yuning-lin/EnvironmentSetup/edit/main/Docker/README.md)
2. 從 github 下載 [docker-pyinstaller](https://github.com/cdrx/docker-pyinstaller) 解壓縮名為 `docker-pyinstaller-master` 的資料夾
3. 在 `docker-pyinstaller-master` 下建立 `src` 資料夾，並在此資料夾下：
    * `pip freeze > requirements.txt` 把該專案套件存成 .txt 後續會根據此文件做打包
    * 將專案下所有互相呼叫的 .py 以及執行 pyinstaller 產生的 .spec 也複製於此資料夾下
    * 故 `src` 下會有 requirements.txt、.py、.spec 三種檔案
4. 於 CMD：`docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux` 將 .py 打包成 Mac 使用的執行檔
