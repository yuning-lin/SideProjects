## ANTLR 簡介
ANTLR（ANother Tool for Language Recognition）使用規則來描述程式語言，  
利用 Lexer 將程式碼轉換成字元流、Parser 將字元流解析成抽象語法樹（AST）  
可以拿來做語言解析、語言查詢等應用  

## 以解析 JAVA 檔案為例
1. 安裝套件：
  ```linux
  pip install antlr4-python3-runtime==4.7.2
  pip install antlr4-tools
  ```
2. 前往 [grammar](https://github.com/antlr/grammars-v4/blob/master/java/java8/) 下載對應 .g4 檔：Java8Lexer.g4、Java8Parser.g4
3. 利用 .g4 生成出欲使用的語言檔案，EX：想用 python 解析 .java 檔
  ```linux
  antlr4 -Dlanguage=Python3 Java8Lexer.g4
  antlr4 -Dlanguage=Python3 Java8Parser.g4
  antlr4 -Dlanguage=Python3 -visitor *.g4
  ```
4. 可以在 antlr_test.py 搭配 test.java 看到如何使用以上生成出來的檔案

## 參考資源
* [Org：ANTLR](https://www.antlr.org/)
* [GitHub：ANTLR v4](https://github.com/antlr/antlr4)
* [GitHub：grammars-v4](https://github.com/antlr/grammars-v4/tree/master)
* [The ANTLR Mega Tutorial](https://tomassetti.me/antlr-mega-tutorial/)
* [Python：antlr4-python3-runtime](https://pypi.org/project/antlr4-python3-runtime/)
