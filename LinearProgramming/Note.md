## 單形法（simplex method）
* 線性規劃標準形式＋鬆弛變數（slack variable）--＞增強形式（augmented form）。增強形式才可以用高斯消去法進行求解
  * 線性規劃標準形式：  
    $\max{Z=c_1x_1+...+c_nx_n}$  
    $s.t.$  
    $
    \begin{cases}
    a_11x_1+...+a_1nx_n \leq b_1 \newline
    a_m1x_1+...+a_mnx_n \leq b_m \newline
    x_1,...,x_n \geq 0
    \end{cases}
    $
  
  * $
    鬆弛變數
    \begin{cases} 
    ＝0, 該點位於所對應之限制式上  \newline
    ＞0, 該點落在限制式可行的一側  \newline
    ＜0, 不可行
    \end{cases}
    $
  
* proper form：
  * 目標式裡變數要全為非基變量（non-basic）
  * 每個限制式只有一個基變量（basic variable）其係數要為 1，且不會在其他方程式出現
* 從可行角點開始在邊界移動尋找最佳解：
  1. Largest improvement rate：選定每上升一單位能讓目標式增量最大的變數 enter to basic
  2. Minimum ratio test： 選定變成 basic 的變數後，根據滿足限制式下最多可以增加的值，進而決定了哪個變數 leave 成為 non-basic 
  3. Optimality Test：當目標函數的係數無法再讓目標值更好，才結束求解
* 當產生退化解時有可能會有 infinite loop --> 選不同的點做 leaving variable  
  
**範例：**   
  1. 線性規劃標準形式  
    $\max{Z=5x_1+3x_2+x_3}$  
    $s.t.$  
    $
    \begin{cases}
    2x_1+4x_2+x_3 \leq 8 \newline
    x_1+2x_2+2x_3 \leq 10 \newline
    2x_1+6x_2 \leq 6 \newline
    x_1,x_2,x_3 \geq 0
    \end{cases}
    $
      
  2. 增強形式  
    $
    \begin{cases}
    2x_1+4x_2+x_3+x_4 = 8 \newline
    x_1+2x_2+2x_3+x_5 = 10 \newline
    2x_1+6x_2+x_6 = 6 \newline
    -5x_1-3x_2-x_3+P = 0
    \end{cases}
    $
      
  3. 取出係數列成單形表，根據 Largest improvement rate ，找出係數比較大，比較有機會讓目標值變大的變數
     
     ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/simplex_table1.PNG)
     
  4. 根據 Minimum ratio test 找出 ratio 最小的，即找到該變數最多可以為目標式增加的值
       
     ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/simplex_table2.PNG)
     
  5. 將 $x_1$ 的係數化為 1 後進行高斯消去法
       
     ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/simplex_table3.PNG)
     
  6. 持續 2～5 的步驟直到所有變數的係數皆為正，因為變數全為正，故目標式最好的情況就是如此了，不會再更好了
       
     ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/simplex_table4.PNG)
     
  7. 此時將非基變量，即目標式有出現的變數 $x_2,x_4,x_6$ 代為 0，則求得最佳解為 17，$(x_1, x_2, x_3)=(3,0,2)$


## Branch and Bound
初始設置： incumbent（到目前為止最佳的解） = -∞  
1. Branch（何時該切分）
    * 找最後產生之點來分支，若平手則選 bound 較好的
    * 對 Binary Integer Programming 而言：固定某個變數之值做分支
    * 對 Mixed Integer Programming 而言：$𝑥_{𝑖𝑗}≤⌊𝑥_{𝑖𝑗}^∗ ⌋,𝑥_{𝑖𝑗}≥⌊𝑥_{𝑖𝑗}^∗ ⌋+1$
2. Bound（哪裡是界限）
    * 目標式若是求 MAX，則求 bound 之上界；反之則求 bound 之下界
    * 對任一問題求出一界限，該問題之最佳解不會比這個界限還要好
    * 最簡單求解 bound 的方式即求解 LP relaxation（用 simplex 求解子問題）
3. Fathom（何時該停止分支）
    * 越分支下去表限制式越多，能符合的解就越差
    * 未剩下未被 fathom 之節點，則停止。fathom 條件如下：
        1. 找到整數解
            * 無須再往下分支
            * 比 incumbent 還好，則令 incumbent = 當前解
            * 要檢查其他子問題是否可以停止
        2. 不可行
        3. Max：bound ≤ incumbent  
  
**範例：**
* Binary Integer Programming
  
  ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/branch_and_bound_BIP.PNG)
   
* Mixed Integer Programming
  
  ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/branch_and_bound_MIP.PNG)
   
## Branch and Cut
現代商用混合整數線性規劃求解器都包含割平面法，但為了計算效率不會單獨被使用  
通常會結合割平面法、Branch and Bound --> Branch and Cut  
**割平面法：**  
  * 一般性割平面法：收緊線性鬆弛問題
    * Gomory 切割（first）
    * Mixed integer rounding 切割
    * Lift and project 切割
  * 結構性割平面法：簡化原問題
    * Knapsack Cover 切割
    * Clique 切割
 
**迭代步驟：**
1. 假設 P 為一 Mixed Integer Programming，求解 P 的線性鬆弛可獲得最佳解 𝜃
2. 若 𝜃 中整數變量的解是整數，則 𝜃 為最佳解，若比 incumbent 佳，取代 incumbent
3. 若 𝜃 中整數變量的解非整數，但有機會可以獲得更佳解，則在該節點向 P 添加切割平面至原線性鬆弛問題再求解
4. 若添加切割平面後 𝜃 中整數變量仍為非整數解，才再繼續分支

**Gomory 切割：**
以圖片的問題為例：
  
  ![](https://github.com/yuning-lin/SideProjects/blob/main/LinearProgramming/Pictures/gomory_cut.PNG)
  
* 通式：IL＋F＝f
  * IL 為一整數值的表達式
  * F 是嚴格正分數的和
  * f＜1 是嚴格正分數
  * EX：$(𝑧−𝑠_3−4)+(5/9 𝑦+2/9 𝑠_2+2/3 𝑠_3 )=4/9$  
* 根據限制式，通式可能有兩種情境
  * 情境一：零＋正分數＝小於一的正分數
  * 情境二：負整數＋正分數＝小於一的正分數
  * 故 f 一定是由 F 得來，則 F ≥ f
  * EX：$(5/9 𝑦+2/9 𝑠_2+2/3 𝑠_3)≥4/9$
* 得 Gomory 切割平面為： $(5/9 𝑦+2/9 𝑠_2+2/3 𝑠_3)≥4/9$
  * 同乘 9 將式子簡化為 $(5𝑦+2𝑠_2+6𝑠_3)≥4$
  * 將原問題的式子帶入得 $(2𝑥+𝑦+2𝑧)≤24$
* 把 Gomory 切割加到原問題，可保證
  * 切割移除了原線性鬆弛上的最優解（即移除了非整數的最優解）
  * 保留原混合整數線性規劃的可行解









