# DD2 其他分裂固定步证书审计

本记录把 `research/topics/dd2/splitting.md` 中的 FBF、外梯度和前向反射—后向三条路线重新按“实际更新步—图残差—锚定缺陷”的顺序核对。结论是：前两条在写明的单值 Lipschitz、凸投影和局部量词下确实给出 DD2 可用的同一步耗散；FRB 不能直接使用增广欧氏距离，必须使用算法自己的交叉项 Lyapunov 函数。这里不把这些固定步子类外推成变步长、非凸或一般分布式定理。

## 1. 前向–后向–前向（FBF）

设 (F=A+B)，(A) 极大单调，(B) 全域 (L_B)-Lipschitz，
(ell=lambda L_B<1)。给定

\[
 y=J_{\lambda A}(x-\lambda Bx),\qquad
 x^+=y+e,
 \qquad e=\lambda(Bx-By),
\]

并令

\[
 d=x-y,\qquad q=d-e=x-x^+ .
\]

则 (q/\lambda\in F(y))，且
\(\|e\|\le \ell\|d\|\)。若 (p\in\operatorname{zer}F)，单调性给出

\[
 \langle q,y-p\rangle
 =\lambda\langle d/\lambda-Bx+By,y-p\rangle
 \ge \lambda\langle By-Bp,y-p\rangle .
\]

因此，在允许一个局部锚缺陷
\(\lambda\langle By-Bp,y-p\rangle\ge-Md(x,S)^p\) 时，平方恒等式为

\[
\begin{aligned}
 \|x-p\|^2-\|x^+-p\|^2
 &=2\langle q,y-p\rangle+\|d\|^2-\|e\|^2\\
 &\ge (1-\ell^2)\|d\|^2-2Md(x,S)^p\\
 &\ge \frac{1-\ell}{1+\ell}\|q\|^2-2Md(x,S)^p .
\end{aligned}
\tag{O1}
\]

最后一个不等式使用
\(\|q\|\le(1+\ell)\|d\|\)。所以 FBF 的同一步 DD2 系数是
\(\chi_{\rm FBF}=(1-\ell)/(1+\ell)\)，而不是由 shadow 位移直接猜出的 \(1-\ell\)。

若在同一工作窗内
\(d(y,S)\le K_F d(0,F(y))^\theta\)，则

\[
 d(y,S)\le K_F\lambda^{-\theta}\|q\|^\theta,
 \qquad
 d(x^+,S)\le K_F\lambda^{-\theta}\|q\|^\theta
       +\frac{\ell}{1-\ell}\|q\| .
\tag{O2}
\]

这里第二项来自
\(\|d\|\le\|q\|/(1-\ell)\) 和
\(\|e\|\le\ell\|d\|\)。因此 C401 的积分势或幂模门可以直接应用于实际步 (q)；若只验证近端 shadow 的长度，还需额外用 (J_{\lambda A}) 的输入 Lipschitz 性转移到 (x^+)。

**量词边界。** (O1) 对最近锚只给距离递推；要得到全锚 Fejér，缺陷必须对每个固定 (p\in S) 成立。若 (B) 只在工作窗内 Lipschitz，必须先证明 FBF 的两个输入仍留在该窗；若 (A) 多值且预解式不是全域单值，(O2) 只能对实际选中的边写成存在量词。

## 2. 外梯度的双投影

设 (K_0) 非空闭凸，(F=N_{K_0}+B)，(B) 全域 (L_B)-Lipschitz，
\(x\in K_0\)，并取

\[
 y=\Pi_{K_0}(x-\lambda Bx),\qquad
 x^+=\Pi_{K_0}(x-\lambda By),
 \qquad d=x-y,\quad e=x^+-y,\quad q=d-e .
\]

投影最优性分别给出

\[
 \langle q,x^+-p\rangle\ge\lambda\langle By,x^+-p\rangle,
 \qquad
 \langle d,e\rangle\le\lambda\langle Bx,e\rangle .
\]

代入平方恒等式并用 \(\|By-Bx\|\le L_B\|d\|\) 得

\[
\begin{aligned}
 \|x-p\|^2-\|x^+-p\|^2
 &\ge 2\lambda\langle By,y-p\rangle
 +\|d\|^2+\|e\|^2-2\ell\|d\|\|e\|\\
 &\ge 2\lambda\langle By,y-p\rangle
 +\frac{1-\ell}{2}\|q\|^2 .
\end{aligned}
\tag{O3}
\]

第二行只用了
\(2\|d\|\|e\|\le\|d\|^2+\|e\|^2\) 以及
\(\|q\|^2\le2(\|d\|^2+\|e\|^2)\)。故外梯度的直接 DD2 系数可取
\(\chi_{\rm EG}=(1-\ell)/2\)。

若 \(p\) 是零点且
\(\lambda\langle By,y-p\rangle\ge-Md(x,S)^p\)，则 (O3) 与 C401 相同地给出长度势。真实图残差在 \(y\) 处为

\[
 v=d/\lambda-Bx+By\in F(y),
 \qquad
 \|v\|\le \frac{1+\ell}{\lambda(1-\ell)}\|q\|,
\tag{O4}
\]

因为非扩张投影给 \(\|e\|\le\ell\|d\|\)，而
\(q=d-e\) 从而 \(\|d\|\le\|q\|/(1-\ell)\)。这一步说明外梯度不能只把 \(q/\lambda\) 当作图值；图值还包含第一次投影的法向量，必须使用 (O4) 的 lift。

## 3. 前向反射—后向（FRB）的反例和正确作用域

FRB 使用两个状态。即使 \(A=0\)、\(B=I\)、\(0<\lambda<1/2\)，从
\((x,w)=(\varepsilon,0)\) 更新到
\((y,x)=((1-2\lambda)\varepsilon,\varepsilon)\)。因此增广欧氏平方距离从
\(\varepsilon^2\) 变为

\[
 ((1-2\lambda)^2+1)\varepsilon^2>\varepsilon^2 .
\tag{O5}
\]

然而该线性迭代的特征根
\[
 \frac{1-2\lambda\pm\sqrt{1+4\lambda^2}}2
\]
均在单位圆内，所以“每一步欧氏下降”不是 FRB 的必要机制。可用的能量必须含有交叉项；对
\(d=y-x, e=x-w, V_x=Bx-Bw, V_y=By-Bx\)，取

\[
 E_p(x,w)=\|x-p\|^2-2\lambda\langle V_x,x-p\rangle+\tfrac12\|e\|^2 .
\]

在 \(\ell=\lambda L_B<1/2\) 且 \(r=-d/\lambda+V_y-V_x\in F(y)\) 时，直接展开得到

\[
 E_p(x,w)-E_p(y,x)
 \ge 2\lambda\langle r,y-p\rangle+(\tfrac12-\ell)(\|d\|^2+\|e\|^2).
\tag{O6}
\]

所以 FRB 只有在能量 \(E_p\) 对零锚一致等价、图残差和实际增广步满足同一工作窗时，才能接入 DD2。把普通 PPA 的 C400 距离势直接套在 \(\|(x,w)-(p,p)\|\) 上会被 (O5) 反驳。集合值 \(A\)、变步长或仅局部 Lipschitz 的 \(B\) 还需重新证明 (O6) 的交叉项可控。
## 4. 验收结论

- FBF：在 \(\ell<1\) 和写明最近锚缺陷时，(O1)–(O2) 给出实际步耗散、残差 lift 和 C401 势门。
- 外梯度：在闭凸投影和 \(\ell<1\) 时，(O3)–(O4) 给出实际步证书；第一次投影的法向量不能省略。
- FRB：固定 \(\ell<1/2\) 的交叉项能量 (O6) 可用；普通欧氏距离证书在 (O5) 已失败。
- 未闭合范围：统一松弛、变步长、非凸投影、多算子非分离耦合和一般时间变化通信图仍需各自的 Lyapunov 函数及实际图覆盖，不能从这三条固定步公式自动推出。

**与正文的关系。** 这份审计只核对并收紧 `splitting.md` 已给出的固定步子类；它不改变 C405 的 CP/DR 结论，也不宣称其他分裂的全局优先性。
