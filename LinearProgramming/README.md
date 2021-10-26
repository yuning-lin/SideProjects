## 說明
雖非 ML 領域但於工作過程中接觸到，  
發現許多物理事件轉換成數學公式的精妙，  
將花時間學到的線性規劃技巧紀錄於此 folder  
主要實現工具為 python pulp 套件。  
首要動作：`pip install pulp`

## 內容
查詢到在供應鏈管理、運籌學的課程也時有連結，   
建議以英文查詢欲達成之目標，  
以下附上網路轉載之表格（Beamon, 1998）以利查詢   
<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="0" style="width:735.0pt;border-collapse:collapse;mso-yfti-tbllook:1056;
 mso-padding-alt:0cm 0cm 0cm 0cm">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:17.9pt">
  <td width="69" style="width:52.0pt;border-top:solid black 2.25pt;border-left:
  none;border-bottom:solid black 2.25pt;border-right:none;background:#1AB39F;
  padding:.75pt .75pt .75pt .75pt;height:17.9pt"></td>
  <td width="355" style="width:266.0pt;border-top:solid black 2.25pt;border-left:
  none;border-bottom:solid black 2.25pt;border-right:none;background:#1AB39F;
  padding:.75pt .75pt .75pt .75pt;height:17.9pt">
  <p class="MsoNormal"><b><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">衡量指標</span></b></p>
  </td>
  <td width="555" style="width:416.0pt;border-top:solid black 2.25pt;border-left:
  none;border-bottom:solid black 2.25pt;border-right:none;background:#1AB39F;
  padding:.75pt .75pt .75pt .75pt;height:17.9pt">
  <p class="MsoNormal"><b><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">說明</span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:21.5pt">
  <td width="69" rowspan="5" style="width:52.0pt;border:none;mso-border-top-alt:
  solid black 2.25pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">以成本為考量之定量績效衡量指標</span></p>
  </td>
  <td width="355" style="width:266.0pt;border:none;mso-border-top-alt:solid black 2.25pt;
  background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">成本最小化</span><span lang="EN-US"><br>
  (Cost Minimization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;border:none;mso-border-top-alt:solid black 2.25pt;
  background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">這是最為廣泛使用的衡量，用於供應鏈整體或特有的商業單位、階段</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:21.5pt">
  <td width="355" style="width:266.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">銷售最<span class="GramE">大化</span></span><span lang="EN-US"><br>
  (Sales Maximization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">使銷售金額或單位銷售量最大化</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:21.5pt">
  <td width="355" style="width:266.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">利潤最<span class="GramE">大化</span></span><span lang="EN-US"><br>
  (Profit Maximization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">收益扣除成本後之最大化</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:21.5pt">
  <td width="355" style="width:266.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">庫存投資最小化</span><span lang="EN-US"><br>
  (Inventory Investment Minimization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">將庫存成本最小化</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:21.5pt">
  <td width="355" style="width:266.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">過期存貨最小化</span><span lang="EN-US"><br>
  (Inventory Obsolescence Minimization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">將過期存貨最小化</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:21.5pt">
  <td width="69" rowspan="6" style="width:52.0pt;border:none;border-bottom:solid black 2.25pt;
  background:white;padding:.75pt .75pt .75pt .75pt;height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">以顧客回應程度為考量之定量績效衡量指標</span></p>
  </td>
  <td width="355" style="width:266.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">訂單完成率最<span class="GramE">大化</span></span><span lang="EN-US"><br>
  (Fill Rate Maximization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">及時完成顧客訂單<span class="GramE">佔</span>全部訂單的比例</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:21.5pt">
  <td width="355" style="width:266.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">目標完成率之達成</span><span lang="EN-US"><br>
  (Target Fill Rate Achievement)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">達成<span class="GramE">一</span>目標服務水準或完成率</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:21.5pt">
  <td width="355" style="width:266.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">產品延遲最小化</span><span lang="EN-US"><br>
  (Product Lateness Minimization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">承諾產品遞送日與實際產品遞送日之間的時間最小化</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:21.5pt">
  <td width="355" style="width:266.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">顧客回應時間最小化</span><span lang="EN-US"><br>
  (Customer Response Time Minimization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">從顧客下訂單到顧客收到產品之間所花費的時間最小化</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:21.5pt">
  <td width="355" style="width:266.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">前置時間最小化</span><span lang="EN-US"><br>
  (Lead Time Minimization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;background:white;padding:.75pt .75pt .75pt .75pt;
  height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">從<span class="GramE">一</span>產品開始製造到完成的時間為前置時間，將其最小化</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;mso-yfti-lastrow:yes;height:21.5pt">
  <td width="355" style="width:266.0pt;border:none;border-bottom:solid black 2.25pt;
  background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">缺貨機率最小化</span><span lang="EN-US"><br>
  (<span class="SpellE">Stockout</span> Probability Minimization)</span></p>
  </td>
  <td width="555" style="width:416.0pt;border:none;border-bottom:solid black 2.25pt;
  background:#E7E7E7;padding:.75pt .75pt .75pt .75pt;height:21.5pt">
  <p class="MsoNormal"><span style="font-family:&quot;新細明體&quot;,serif;mso-ascii-font-family:
  Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:新細明體;
  mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
  mso-hansi-theme-font:minor-latin">將缺貨機率最小化</span></p>
  </td>
 </tr>
</tbody></table>


根據有接觸到的子題做程式範例如下：  
* [基礎整數規劃＋出貨有優先順序](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/pulp_with_preemptive_goal_programming.ipynb)
* 料件使用有優先順序（替代料件）
* 共用料件

## 線性規劃（linear programming）
求解以單形法、內點法延伸為大宗，基本上是根據追求求解時間更快等做變形的計算
方法名稱|計算概念|應用時機
----|----|----
[單形法（simplex method）](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Note.md#%E5%96%AE%E5%BD%A2%E6%B3%95simplex-method)|沿著邊界尋找最佳可行角點，若鄰點更好則繼續迭代|解小型線性規劃問題有不錯的表現
內點法（interior method）|衡量移動的方向及步長，在可行解集合逼近最佳解|解大型、稀疏線性規劃問題效率表現較佳
橢球法（ellipsoid method）|製造一個涵蓋極值的橢球。依照梯度移動球心、迭代調整橢球形狀並縮小體積，以使球心逐步收斂至極值|實際應用效率不如另兩種方法

## 整數規劃（integer programming）
其想法來自於：窮舉（太花時間）--> 部分窮舉（分開求解）
* [分支限界法（branch and bound）](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Note.md#branch-and-bound)
* [分支切割法（branch and cut）](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Note.md#branch-and-cut)

## 求解工具
[知名 LP solvers 效能比較](https://mattmilten.github.io/mittelmann-plots/)
* 套裝軟體
  * [LINGO](https://www.lindo.com/index.php/ls-downloads/try-lingo)
  * [GUROBI](https://www.gurobi.com/resource/switching-from-open-source/)
* 網頁介面
  * [OR-Tools](https://developers.google.com/optimization/lp)
  * [online-optimizer](https://online-optimizer.appspot.com/)
  * [frepple](https://demo.frepple.com/)
* 開源程式（下列介紹以 python 套件為主）
  * [scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)
    * 不能解整數規劃
    * 無法對接外部 solver
  * [pulp](https://coin-or.github.io/pulp/)
    * 可以求解整數、混合整數規劃問題
    * 可以對接外部 solver，如：Gurobi、CPLEX、GLPK 等（當然商業軟體還是會有使用上限）
                                                   
     solver name| package
     ---|---
     CoinOR|`pip install coinor-cbc`
     Gurobi| `pip install gurobipy`
     CPLEX| `pip install cplex`
     GLPK| `pip install glpk-utils`
     [SCIP](https://github.com/scipopt/PySCIPOpt)|`pip install pyscipopt`
  
* 檢測安裝結果
```python
import pulp
print(pulp.__version__)
pulpTestAll() # 內建測試功能
listSolvers() # 列出所有 solver
listSolvers(onlyAvailable=True) # 列出環境可以使用的 solver
```
* [如何使用其他 solver](https://coin-or.github.io/pulp/guides/how_to_configure_solvers.html)


## 參考來源
* [COIN-OR Mixed Integer Linear Programming with Python](https://buildmedia.readthedocs.org/media/pdf/python-mip/latest/python-mip.pdf)
* [Python MIP - Developing Customized Branch-&-Cut algorithms](https://docs.python-mip.com/en/latest/custom.html)
* [scipy vs pulp](https://realpython.com/linear-programming-python/)
* [branch and bound vs branch and cut](https://www.cnblogs.com/dengfaheng/p/11344488.html)
* [Coursera Gomory Cut](https://zh-tw.coursera.org/lecture/lisan-youhua-suanfapian/3-3-3-qie-ge-ping-mian-loPYl)
* [Cutting Plane Method and Strong Valid Inequalities](https://ocw.nctu.edu.tw/course/ip002/lecture_IP6.pdf)
* [線性規劃－基礎數學觀念、單形法](https://ccjou.wordpress.com/%e5%b0%88%e9%a1%8c%e6%8e%a2%e7%a9%b6/%e7%b7%9a%e6%80%a7%e8%a6%8f%e5%8a%83%e5%b0%88%e9%a1%8c/)
* [線性規劃簡介](https://www.wikiwand.com/zh-hk/%E7%BA%BF%E6%80%A7%E8%A7%84%E5%88%92)
* [線性最佳化含圖解](https://web.ntnu.edu.tw/~algo/LinearOptimization.html)
* [線性規劃－內點法](https://blog.csdn.net/dymodi/article/details/46441783)
* [交大線上課程：單形法](https://www.youtube.com/watch?v=RTe7_OO17ww&list=PLj6E8qlqmkFufn5avTvkdFDcYA9cnuzcd&index=5)
* [交大線上課程：整數規劃](https://www.youtube.com/watch?v=G5a8NOIxc8s&list=PLj6E8qlqmkFvyhyY3oCLq2OBIIew52c0b&index=6)
* [交大線上課程：非線性規劃](http://ocw.nctu.edu.tw/course_detail.php?bgid=3&gid=0&nid=358)
* [線代啟示錄：多胞形](https://ccjou.wordpress.com/2013/05/20/%E5%A4%9A%E8%83%9E%E5%BD%A2/)
