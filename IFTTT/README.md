## 專案目標：發送股市即時訊息至 LINE
當指定標的觸及發送示警的標準時，傳訊至 LINE  
以即時做股票的買賣

## 檔案內容：
* SendInfoToLine.ipynb：示範程式檔
* InstructionsPics：存放 IFTTT 設置圖示
* README.md：圖示 IFTTT 設置流程

## 圖示 IFTTT 設置流程
1. 於 [官網](https://ifttt.com/user/new?user%5Bemail%5D=&wp_=1) 申請 IFTTT 帳號
2. 申請成功後會跳出：Welcoe to IFTTT! > 點選 Cancel 回到首頁
3. 點選首頁右上角 Create > 點選頁面中的 Add > 鍵入 Webhooks > 點選 Receive a web request > 點選 Connect > 新增 Event Name
5. 點選頁面中 Then That 旁的 Add > 鍵入 line > 點選 Send message > 點選 Connect > 輸入 line 的帳密 > 手機驗證 > 同意並連動
6. line 會接收到 LINE Notify，之後的示警訊息就會出現在此群組
7. 回到 IFTTT 網站 > 客製化訊息 > 點選 Create action > 並打開程序
8. 前往：https://ifttt.com/maker > 點選右上角 Settings > Account Info 的 URL：https://maker.ifttt.com/use/... 刪節號觸即為觸發程序的授權碼
