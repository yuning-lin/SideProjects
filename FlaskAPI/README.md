## 先備知識小記
* HTTP（HyperText Transfer Protocol）為提供接收與發送 HTML 的方法
* HTTPS（HyperText Transfer Protocol Secure）為經由 HTTP 進行通訊，但藉由 SSL/TLS 進行加密
* SSL（Secure Sockets Layer）先於 TLS（Transport Layer Security），皆為安全協定
* TCP（Transmission Control Protocol）為有重傳封包機制的通訊協議，資料正確性較高傳輸速度較慢
* UDP（User Datagram Protocol）為無重傳封包機制的通訊協議，資料正確性較低傳輸速度較快
* HTTP（based on TCP） + SSL/TLS = HTTPS

## 使用套件
  
|名稱|用途|
|----|----|
|socket|搭建典型的 TCP 或 UDP 等通訊程式，進行傳遞及接收訊息的功能|
|flask|用 `@wrap` 創建輕量化 api 模組|
|flask_restful|用 `add_resource` 方式創建輕量化 api 模組|
|flask_cors|處理跨域資源共享 Cross Origin Resource Sharing (CORS)|
|cryptography|要使用臨時憑證 ad-hoc certificates 需要的套件|


### 關於 socket 套件
有以下兩個重要的引數
* family：
	* socket.AF_INET 用於伺服器們間的網路通訊
	* socket.AF_INET6 基於 IPV6 方式用於伺服器們間的網路通訊
* type：
	* socket.SOCK_STREAM 表示傳輸方式為 TCP
	* socket.SOCK_DGRAM 表示傳輸方式為 UDP


## 程式結構
* based on python 3.6.8
  
|檔名|功能|
|-----|-----|
|practice_flask.py|利用套件 flask 做的簡易 api 模板|
|practice_flask_restful.py|利用套件 flask、flask_restful 做的簡易 api 模板，內容可和 practice_flask.py 交互參照|
|download/|存放欲讓他人利用 api 下載的文件|
|requirements.txt|使用套件及對應版本|


## Call API
* bash
    * GET：`curl http://127.0.0.1:5000/api/get_request/`
    * POST：`curl -X POST -H "Content-Type: application/json" -d '{"param1": "value1", "param2": "value2"}' http://127.0.0.1:5000/api/post_request/`
* python
```python

```

## 參考資源
* [python socket 講解](https://shengyu7697.github.io/python-socket/)
* [postman 教學](https://www.wrpypl.com/postman.html)
* [flask 中文 IT 邦幫忙教學](https://ithelp.ithome.com.tw/articles/10199518)
