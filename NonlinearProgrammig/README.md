## 專案內容
1. 涉及非線性規劃
2. 出貨有優先順序
3. 除了主料件還有替代料件，但主料用完才能用替料
4. 提供模擬資料、程式範例及 requirements


## 常見套包
1. [GEKKO])(https://gekko.readthedocs.io/en/latest/)
    * 實際解決問題時碰到運算限制
    * 僅提供簡單的[應用案例](https://github.com/yuning-lin/SideProjects/blob/main/NonlinearProgrammig/nonlinear_programming_gekko_simple.ipynb)
2. [PySCIPOpt](https://scipopt.github.io/PySCIPOpt/docs/html/)
    * 安裝過程[詳見](https://github.com/yuning-lin/SideProjects/blob/main/NonlinearProgrammig/SCIP.md)
    * [實際應用案例](https://github.com/yuning-lin/SideProjects/blob/main/NonlinearProgrammig/nonlinear_programming_scip_with_pgp.ipynb)
3. [ipyopt](https://gitlab.com/g-braeunlich/ipyopt/-/tree/master/)


## 關於 [IPOPT](https://coin-or.github.io/Ipopt/)
* 為設計來解決大型、稀疏非線性規劃問題的求解器
* 須先安裝：
   * BLAS (Basic Linear Algebra Subroutines) and LAPACK (Linear Algebra PACKage)［對大型問題運算時間會有影響］ 
   * 稀疏對稱不定線性求解器［必須要能夠提供被分解的對稱矩陣的 inertia（正負特徵值的數量）］
* 提醒：
   * 在對於 MA27 or MA57 這兩個線性求解器，可以使用 MC19 對線性系統降維
   * IPOPT 是用 C++ 寫的，所以需要用 C++ compiler 創建 ipopt library
* [如何使用](https://projects.coin-or.org/Ipopt/export/1861/trunk/Ipopt/doc/documentation.pdf)：
   * [以六種 IPOPT 接口為例](https://coin-or.github.io/Ipopt/INTERFACES.html)，即 AMPL（A Mathematical Programming Language）建模語言以及 C++, C, Fortran, Java, and R 等 code interfaces
   * AMPL：
      * 直接用 AMPL 建模
      * 並且利用 command line 使用 ipopt
   * code interfaces（須提供五項資訊）：
      * Problem dimensions（變數與限制式的數量）
      * Problem bounds（變數與限制式的邊界）
      * Initial starting point（起始點）
      * Problem Structure（問題結構）
      * Evaluation of Problem Functions（問題函數的評估，如目標函數等）


## 學習資訊
* [交大線上課程：非線性規劃](http://ocw.nctu.edu.tw/course_detail.php?bgid=3&gid=0&nid=358)
* [線代啟示錄：多胞形](https://ccjou.wordpress.com/2013/05/20/%E5%A4%9A%E8%83%9E%E5%BD%A2/)
* [Mathematical Optimization](https://scipbook.readthedocs.io/en/latest/intro.html)
* [PYSCIPOPT: Mathematical Programming in Python with the SCIP Optimization Suite](https://opus4.kobv.de/opus4-zib/files/6134/PySCIPOpt.pdf)
* [SCIP official site](https://scipopt.org/#scipoptsuite)
* [SCIP functions](https://scipopt.github.io/PySCIPOpt/docs/html/classpyscipopt_1_1scip_1_1Model.html)

