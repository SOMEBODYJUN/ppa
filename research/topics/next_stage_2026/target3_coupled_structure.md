# 目标三：耦合 (A)+(B) 与新的弱结构性质

## 1. 条件的精确身份

对一个允许的 PPA 转移 (x\to y)，写

\[
\tag{A}d(y,S)\le\kappa d(x,S),\qquad0\le\kappa<1,
\]

\[
\tag{B}\|x-y\|\le B\,d(y,S).
\]

(A) 是输出距离的线性压缩；(B) 是以输出距离为尺度的上方形物理 calmness。若二者对每一步成立，则

\[
\sum_k\|x^{k+1}-x^k\|
\le B\sum_k d(x^{k+1},S)
\le \frac{B\kappa}{1-kappa}d(x^0,S),
\]

所以它们确实直接给有限长度。

<a id="t3-obstruction"></a>
## 2. 完整图上的不可绕过障碍

**引理 T3.1（A 已蕴含线性 metric subregularity）。** 假设 (A) 对完整 \(\operatorname{gph}F\) 的每个图点 \((y,w)\) 都成立，令 (x=y+\lambda w)。则

\[
d(x,S)\le d(y,S)+\lambda\|w\|,
\]

从而

\[
d(y,S)\le\kappa[d(y,S)+\lambda\|w\|]
\quad\Longrightarrow\quad
d(y,S)\le\frac{\kappa\lambda}{1-\kappa}\|w\|.
\]

对 (w\in F(y)) 取下确界，得到

\[
d(y,S)\le \frac{\kappa\lambda}{1-\kappa}r_F(y).
\tag{T3.1}
\]

因此，在完整图解释下，任何蕴含 (A) 的性质已经蕴含传统线性 metric subregularity；不可能再构造一个严格弱于 metric subregularity、同时推出 (A)+(B) 的完整图性质。若 (A) 只对一个严格允许子关系 \(\mathcal J(x)\subsetneq J_{\lambda F}(x)\) 成立，T3.1 只能对该子关系的选中图值成立，不能下传到 (r_F)。

这是本目标最重要的负面结果：任务书给出的逻辑链在 full-graph 量词下不相容，不能通过给 (A)+(B) 另起名字修复。

## 3. 反例和边界

### 3.1 (A) 但点列不收敛

取 (S=\mathbb R\times\{0\})，允许转移

\[
T(u,t)=(u+1,\kappa t),\quad0<\kappa<1.
\]

则 (d(Tx,S)=\kappa d(x,S))，但第一坐标每步增加 1，轨道不收敛。把图边写成 (x=y+w) 即可得到局部 PPA 关系；(B) 失败。这说明距离收缩不等于点列收敛。

### 3.2 (B) 但不收敛

在 (S=\{0\}) 上取 (T(x)=2x)。则 \(\|T(x)-x\|=d(Tx,S)\)，所以 (B) 取 (B=1)，但距离扩大，(A) 失败，轨道发散。

### 3.3 (A)+(B) 但不满足 pairwise 次单调性

令 (S=\mathbb R\times\{0\})，在图中加入零支 (S\times\{0\})，以及

\[
y_n=(1/n,1),\quad x_n=(1/n^3,3),\quad w_n=x_n-y_n,
\qquad n\ge2,
\]

并加入其极限边 (y_\infty=(0,1),x_\infty=(0,3),w_\infty=(0,2))。所有这些选中边满足

\[
d(y_n,S)=1\le\tfrac12 d(x_n,S)=\tfrac32,
\qquad
\|x_n-y_n\|\le3d(y_n,S),
\]

故 (A)+(B) 取 \((\kappa,B)=(1/2,3)\)。但对于 (m,n\to\infty)，水平分量满足 \(\Delta y\sim 1/n-1/m\)、\(\Delta w\sim-(1/n-1/m)\)，而输入差 \(\Delta x\sim1/n^3-1/m^3\)。所以

\[
\frac{-\langle\Delta y,\Delta w\rangle}{\|\Delta x\|^2}\to\infty,
\]

任何固定常数的 Luke–Tam 型 pairwise 次单调不等式都失败。该图是闭的（加入了唯一需要的极限边），因此这是完整图层面的严格反例；它不否定 T3.1，因为 metric subregularity 仍由 (A) 自动得到。

### 3.4 (A)+(B) 但不满足完整图 metric subregularity：只能在严格子关系上

令 (S=\{0\})，允许选择仅取 (x=2y,w=y) 的边，\(\lambda=1\)。则 (A) 取 \(\kappa=1/2\)，(B) 取 (B=1)。定义完整关系在 (y>0) 还包含额外值 (w=y^2)。于是

\[
r_F(y)\le y^2,
\qquad \frac{d(y,S)}{r_F(y)}\ge\frac1y\to\infty,
\]

完整图 metric subregularity 失败；但额外分支不属于允许选择，故选中边的 (A)+(B) 仍成立。这准确显示了“完整图”与“允许子关系”不能混写。若任务要求 full graph，这个例子不满足量词，不能用来宣称弱化完成。

### 3.5 传统次单调性与线性 MSR 甚至不能推出 (B)

取 \(0<\alpha<1\)、\(X=\mathbb R\)、\(S=\{0\}\)，令
\[
F(y)=\operatorname{sgn}(y)|y|^\alpha.
\]
它是凸函数 \(|y|^{1+\alpha}/(1+\alpha)\) 的梯度，因而最大单调；在 \(|y|\le1\) 上
\[
d(y,S)=|y|\le |y|^\alpha=r_F(y),
\]
所以线性 metric subregularity 成立。精确 PPA 方程为
\[
x=y+\lambda\operatorname{sgn}(y)|y|^\alpha.
\]
对 \(y>0\)，有 \(d(x,S)=y+\lambda y^\alpha\)，

\[
\frac{d(y,S)}{d(x,S)}=\frac{1}{1+\lambda y^{\alpha-1}}\to0,
\qquad
\frac{\|x-y\|}{d(y,S)}=\lambda y^{\alpha-1}\to+\infty.
\]

因此 (A) 在足够小的窗口内对任意预先给定的 \(\kappa\in(0,1)\) 成立，而 (B) 对任何有限 \(B\) 都失败。这是完整、单调、满足线性 MSR 的反例，直接否定任务书要求的“传统次单调性+MSR \(\Rightarrow\mathcal P\Rightarrow\)(A)+(B)”前件箭头；不是非单调或不完整 resolvent 的病理。

<a id="t3-ptd"></a>
## 4. 可回收的新结构：望远镜下降性质

虽然不能得到任务书字面要求的 \(\mathcal P\Rightarrow(A)+(B)\) 且严格弱于完整图 metric subregularity 的性质，但可以保留一个有独立意义的更弱长度结构：

\[
\tag{PTD}
d(y,S)\le\kappa d(x,S),
\qquad
\|x-y\|\le C\bigl(d(x,S)^\alpha-d(y,S)^\alpha\bigr),
\quad0<\alpha\le1.
\]

它是径向距离势 (d^\alpha) 的望远镜下降，而不是把 (A)+(B) 改名。PTD 立即给

\[
\sum_k\|x^{k+1}-x^k\|\le C\,d(x^0,S)^\alpha.
\]

反过来，(A)+(B) 蕴含 PTD（取 \(\alpha=1\)）：

\[
d(x,S)-d(y,S)\ge(1-\kappa)d(x,S)\ge\frac{1-\kappa}{\kappa}d(y,S),
\]

所以 (s\le B d(y,S)\le B\kappa(1-\kappa)^{-1}[d(x,S)-d(y,S)])。但 PTD 一般不蕴含 (B)，因为它允许 (s) 由 (d(x)^\alpha-d(y)^\alpha) 控制而不是由 (d(y)) 控制。

例如 (S=\mathbb R\times\{0\})，(T(u,t)=(u+|t|^\alpha,qt))，(q<1)，(0<\alpha<1)。则 PTD 成立且轨道长度有限，但

\[
\frac{\|T(u,t)-(u,t)\|}{d(T(u,t),S)}\asymp |t|^{\alpha-1}\to\infty,
\]

所以任何固定 (B) 的 (B) 失败。这是为什么 PTD 应记录为 salvage candidate，而不能伪装成任务书所需的 \(\mathcal P\)。

## 5. 一个有独立几何意义但尚未闭合前件箭头的候选

为保留“不是把 (A)+(B) 改名”的正面路线，可定义允许转移上的锚定扇区—相对平静性：存在同一锚
\(p\in P_S(x)\cap P_S(y)\)、常数 \(0<\mu<1/2\)、\(0\le\nu<1/2\)、\(c<\infty\)，使
\[
\langle y-p,x-y\rangle\ge \mu d(x,S)^2-\nu\|x-y\|^2,
\qquad
\left\|\frac{x-y}{\lambda}\right\|\le c\,d(y,S).
\tag{TC}
\]
由于 \(p\in P_S(y)\)，距离恒等式给出
\[
(1-2\mu)d(x,S)^2\ge d(y,S)^2+(1-2\nu)\|x-y\|^2,
\]
从而 (A) 取 \(\kappa=\sqrt{1-2\mu}\)，(B) 取 \(B=\lambda c\)。该性质分别包含共同投影锚、正扇区和选中图值 calmness 三个可检查机制，故独立于把 (A)+(B) 并列写成定义。

但第 3.5 节的最大单调反例表明传统次单调性+MSR 不推出 (TC) 的第二个分量；(TC) 目前只能作为 candidate。具体算子类中验证共同锚、扇区和选中纤维 calmness，是目标三下一步最有信息量的正面义务。

## 5. 当前结论与下一步

目标三的真实结论是一个逻辑分界：

1. 完整图上，(A) 已推出传统线性 metric subregularity；“更弱但推出 (A)+(B)”的要求不可同时满足。
2. 允许子关系上，可以有 (A)+(B) 而完整 (F) 不 metric-subregular，但这依赖选择域，不能称完整算子性质。
3. (A)+(B) 确实比 pairwise 次单调性宽，闭图离散反例给出严格证明。
4. PTD 是一个独立、可验证、直接给有限长度的结构，但其结论严格弱于 (B)；它是下一阶段可继续研究的真实候选。

**状态：** T3.1 为 `derived-checked`；第 3.5 节反例和离散闭图反例均为逐项可核的 obstruction；PTD 与 (TC) 都是 `candidate`。任务书要求的“传统前件推出严格弱化 (mathcal P)”在当前对象层面已被第 3.5 节否定，不能把两个候选升格为该逻辑链的完成。

