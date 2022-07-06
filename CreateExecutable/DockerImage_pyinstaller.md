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
    * 注：若是要在 Mac 打包給 Windows 使用，於終端機：`docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows`

## 參考來源
* [PyInstaller Docker Images](https://github.com/cdrx/docker-pyinstaller)
* [Python 程式打包為執行檔.exe ( Mac OS )](https://medium.com/%E6%88%91%E5%B0%B1%E5%95%8F%E4%B8%80%E5%8F%A5-%E6%80%8E%E9%BA%BC%E5%AF%AB/python-%E5%B0%87%E7%A8%8B%E5%BC%8F%E6%89%93%E5%8C%85%E7%82%BA%E5%9F%B7%E8%A1%8C%E6%AA%94-exe-mac-os-e9521bc87e24)
