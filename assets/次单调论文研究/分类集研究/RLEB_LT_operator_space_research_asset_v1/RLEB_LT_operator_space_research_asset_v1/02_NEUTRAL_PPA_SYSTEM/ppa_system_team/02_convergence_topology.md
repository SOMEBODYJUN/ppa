# 以 PPA 收敛本身为对象的算子空间：拓扑、完备性与共同接口

日期：2026-09-20。任务：不预设 RLEB 或 Luke–Tam 条件，先研究“所有使 PPA 收敛的算子”如何成为合法的拓扑对象。下文的独立命题用于搭建体系，不主张其拓扑原理具有原创优先权。

## 0. 结论先行

用户提出的母空间不是不能建立。需要区分两种同样有数学意义、但回答不同问题的拓扑。

1. **单步/图拓扑**：两个算子的一次 proximal 更新接近。在此拓扑下，所有收敛算子并不自动构成闭集；局部一致收敛类有明确的 Borel 上界，而全部逐点收敛类直接只能给出 coanalytic 上界。不能从“不闭”跳到“不是 Baire”。
2. **全时间动力学拓扑**：两套算法从共同初值出发，在所有迭代时刻都接近。在此拓扑下，可以把全部逐点收敛类做成完备/Baire 空间；把全部局部一致收敛类做成 Polish 空间。无需指定几何收敛、Hölder 模、RLEB、LT 或共同收敛率。

核心构造是

\[
d_{\rm dyn}(T,U)=\sup_{n\ge0}d_X(T^n,U^n),
\]

其中 \(X=C_{\rm loc}(\mathbb R^d,\mathbb R^d)\)，\(d_X\) 是下文给出的有界完备局部一致度量。全部局部一致收敛映射的迭代序列构成 \(c(X)\) 中的闭子集；\(c(X)\) 配一致序列距离是 Polish。这提供了真正不带 RLEB/LT 标签的母空间。

**关键保留**：该拓扑比单步拓扑严格强；相同 Borel 集不意味着相同第一纲集。以后得到“LT 第一纲”时必须写清使用哪一个拓扑，不能在两个体系之间无条件转移。

核心完备性、Polish 性及非可分反例，已由本轮 `axiom_system_stress` 组独立核验通过。

## 1. 先固定对象，不把单步映射偷换成所有步长的算子

### 1.1 固定步长的完整 resolvent 坐标

令 \(E=\mathbb R^d\)，固定 \(\lambda>0\)。对任意连续全域映射 \(T:E\to E\)，定义整个集合值算子

\[
F_T(u)=\{(x-u)/\lambda:T x=u\}.
\tag{1.1}
\]

则

\[
J_{\lambda F_T}=(I+\lambda F_T)^{-1}=T,
\qquad \operatorname{zer}F_T=\operatorname{Fix}T.
\tag{1.2}
\]

这是完整 resolvent 等式，不是某个分支选择。图由线性同胚

\[
(x,T x)\longmapsto(T x,(x-T x)/\lambda)
\tag{1.3}
\]

得到，故 \(F_T\) 闭图。反之，凡完整 \(J_{\lambda F}\) 全域、单值且连续的 \(F\)，都由此唯一恢复。

因此下面的 \(T\)-空间可以严谨地称为“**固定步长 \(\lambda\) 的连续完整 proximal 动力系统空间**”。它暂不包括 genuinely multivalued resolvent 的任意分支轨道，也不自动包括同一个 \(F\) 的任意变步长 PPA。

若只在紧集 \(K\) 上定义 \(T:K\to K\)，公式 (1.1) 只保证输入在 \(K\) 上的完整 resolvent；不能据此声称全空间覆盖。全域体系与局部共同吸引域的关系见第 9 节。

### 1.2 跨步长一致性不是可省略的标签

给定 \(T=J_{\lambda F}\)，令 \(\mu>0\) 并定义

\[
H_{\mu,\lambda}(x)
=\frac\mu\lambda x+\left(1-\frac\mu\lambda\right)T x.
\tag{1.4}
\]

直接用同一个完整图得到

\[
J_{\mu F}(y)=\{T x:H_{\mu,\lambda}(x)=y\}.
\tag{1.5}
\]

因 \(\mu>0\)，若 \(H(x_1)=H(x_2)\) 且 \(T x_1=T x_2\)，必有 \(x_1=x_2\)。所以 \(J_{\mu F}\) 全域单值，当且仅当 \(H\) 双射；若它还连续，则

\[
H^{-1}(y)=\frac\lambda\mu y+
\left(1-\frac\lambda\mu\right)J_{\mu F}(y).
\tag{1.6}
\]

故“两个步长下均全域单值连续”等价于 \(H\) 为同胚，并且

\[
J_{\mu F}=T\circ H_{\mu,\lambda}^{-1}.
\tag{1.7}
\]

这说明不能把任意一族连续映射 \(T_\mu\) 当作同一个算子的 resolvent 家族。第 10 节给出保留该一致性的无标签 family/strategy 空间。

## 2. 不预设收敛的单步母空间

取

\[
X=C(E,E),\qquad
d_X(T,U)=\sum_{j=1}^{\infty}2^{-j}
\min\{1,\sup_{\|x\|\le j}\|T x-U x\|\}.
\tag{2.1}
\]

这是局部一致（compact-open）拓扑。\(X\) 完备且可分。完备性由每个闭球上的一致 Cauchy 极限拼接得到；可分性可由逐球分片线性逼近得到。有限维下 bounded-uniform 与 compact-open 一致。

对紧度量状态空间 \(K\)，平行版本是 \(X=C(K,K)\)，度量

\[
d_X(T,U)=\min\{1,\|T-U\|_\infty\}.
\tag{2.2}
\]

若 \(K\) 不是欧氏集，则将范数换成 \(K\) 的完备兼容距离。

**命题 2.1：composition 与全部有限次迭代连续。**

若 \(T_i\to T\)、\(U_i\to U\) 局部一致，则 \(T_i\circ U_i\to T\circ U\) 局部一致。

证明：对固定紧集 \(B\)，\(U_i(B)\) 最终包含于一个共同紧集 \(L\)；在 \(L\) 上 \(T_i\to T\) 一致，而 \(T\) 在 \(L\) 附近一致连续。于是

\[
\sup_B\|T_i(U_i x)-T(Ux)\|
\le\sup_L\|T_i-T\|+
\sup_B\|T(U_i x)-T(Ux)\|\to0.
\]

故 \(T\mapsto T^n\) 对每个有限 \(n\) 连续。证毕。

### 2.1 固定解集：至少固定与恰好固定不同

对非空闭集 \(S\subset E\)，

\[
X_S=\{T:T|_S=I\}
\tag{2.3}
\]

是闭 Polish 子空间。进一步要求 \(\operatorname{Fix}T=S\) 得到 \(G_\delta\) 子空间：令

\[
A_{j,m}=\{x:\|x\|\le j,\ d(x,S)\ge1/m\},
\]

则在 \(X_S\) 中

\[
\{T:\operatorname{Fix}T=S\}
=\bigcap_{j,m}\{T:\min_{x\in A_{j,m}}\|T x-x\|>0\}.
\tag{2.4}
\]

每个非空 \(A_{j,m}\) 紧；括号内为开集。空集条件视为自动满足。因此该 exact-fixed-set 空间是完全可度量/Polish，虽然一般不是原度量下的闭集。

这修正一个容易误判的地方：\((1-1/n)I\to I\) 只能证明恰好固定 \(S\) 的集合不闭，不能证明它不是 Baire。

### 2.2 图拓扑的口径

最安全且不歧义的算子拓扑，是按 (1.1)–(1.3) 把 (2.1) 拉回到 \(F\) 上。这是真实完整 resolvent 拓扑。

在有限维、全域连续单值 resolvent 范围内，它也与完整图的 Painlevé–Kuratowski 收敛相容。一个可直接核验的理由是：对全域连续 \(T_i:E\to E\)，若图收敛到连续 \(T\) 的图而不局部一致，则存在 \(x_i\to x\) 使输出偏离 \(T x\) 至少 \(\varepsilon\)。图下极限给出 \(z_i\to x\)、\(T_i z_i\to T x\)。连接 \(x_i,z_i\) 的短线段，并对连续 \(T_i\) 用中间值性质，可找到 \(w_i\to x\) 使 \(\|T_i w_i-Tx\|=\varepsilon/2\)。有限维球面紧，从而产生图上极限中不等于 \((x,Tx)\) 的点，矛盾。反向由局部一致立即成立；再用线性图变换 (1.3)。

但“所有闭图算子”的 hyperspace 比该坐标层更大；全域单值 resolvent 性不在任意图极限下保持。例如 \(T_n(x)=n x\) 的图趋于竖直关系，而非连续单值全域图。不能把对完整 resolvent 层的结论直接扩成所有闭图算子结论。

## 3. 三种收敛必须分别定义

在 \(X_S\) 中定义：

\[
\begin{aligned}
\mathcal C_{\rm pt}(S)
&=\{T:\forall x,\ T^n x\to\Pi_T x\in S\},\\
\mathcal C_{\rm lu}(S)
&=\{T:T^n\to\Pi_T\text{ 在每个紧初值集上一致，且 }\Pi_T(E)\subset S\},\\
\mathcal C_{\rm dist}(S)
&=\{T:\forall x,\ d(T^n x,S)\to0\}.
\end{aligned}
\tag{3.1}
\]

有

\[
\mathcal C_{\rm lu}(S)\subset\mathcal C_{\rm pt}(S)
\subset\mathcal C_{\rm dist}(S),
\]

但两个包含都可能严格。对真正点收敛的连续 \(T\)，极限自动为不动点，因此 \(\operatorname{Fix}T=S\)，并有

\[
T\Pi_T=\Pi_T,\quad\Pi_T T=\Pi_T,\quad\Pi_T|_S=I.
\tag{3.2}
\]

### 3.1 逐点收敛不保证连续极限回缩

在 \(K=[0,1]^2\)、\(S=[0,1]\times\{0\}\) 上令

\[
T(s,r)=(\min\{1,s+r\},\ r/(1+r)).
\tag{3.3}
\]

当 \(r>0\) 时，\(r_n=r/(1+nr)\)，且 \(\sum_n r_n=\infty\)，故

\[
\Pi_T(s,r)=
\begin{cases}
(s,0),&r=0,\\
(1,0),&r>0.
\end{cases}
\tag{3.4}
\]

全部轨道收敛到同一个固定的凸非单点解集，但 \(\Pi_T\) 不连续。故若把 \(\Pi\in C(K,S)\) 写进对象定义，已经主动舍弃了部分全轨道收敛系统，必须明说。

一般的 \(\Pi_T\) 是连续迭代函数的逐点极限，至多可直接说它是 Baire-1 映射；“连续回缩”只有在相应连续性条件下成立。

### 3.2 到解集收敛不等于轨道收敛

取 \(K=\overline{\mathbb D}\times[0,1]\)、\(S=\overline{\mathbb D}\times\{0\}\)，其中 \(\mathbb D\subset\mathbb C\)。令

\[
T(z,r)=(e^{ir}z,\ r/(1+r)).
\tag{3.5}
\]

\(S\) 是凸非单点固定集，且距离 \(r_n\to0\)。当 \(z\ne0,r>0\) 时，角增量趋零而总角增量无界，所以角度在圆周上反复绕行，不收敛。不能仅把“吸引到解集”的空间当作“PPA 点收敛”的空间。

## 4. 单步拓扑下的闭性与描述集合复杂度

### 4.1 收敛类一般不闭

在 \(K=[0,1]\times[-1,1]\)、\(S=[0,1]\times\{0\}\) 上取

\[
T_j(s,r)=(s,-(1-1/j)r),\qquad j\ge2.
\tag{4.1}
\]

每个 \(T_j\) 在 \(K\) 上一致收敛到投影 \((s,0)\)，而 \(T_j\to T\) 一致，其中 \(T(s,r)=(s,-r)\) 有非平凡二周期。每个算子连同极限都恰好固定相同 \(S\)。

所以 \(\mathcal C_{\rm pt}(S)\)、\(\mathcal C_{\rm lu}(S)\) 在单步拓扑下通常不闭，其继承的单步度量不完备。**这不决定它们能否完全可度量，或是不是 Baire。**

### 4.2 局部一致收敛类：\(\Pi^0_3\) 上界

在 exact-fixed-set 空间中，局部一致收敛等价于

\[
\bigcap_{j,m\ge1}\ \bigcup_{N\ge1}\ 
\bigcap_{p,q\ge N}
\left\{T:
\sup_{\|x\|\le j}\|T^p x-T^q x\|\le1/m
\right\}.
\tag{4.2}
\]

有限次迭代连续，故内层集合闭。因此 \(\mathcal C_{\rm lu}(S)\) 是 \(F_{\sigma\delta}=\Pi^0_3\) 集。这里仅给上界，不声称在所选 \(E,S\) 上是 \(\Pi^0_3\)-complete，也不据此声称它必非 \(G_\delta\)。

### 4.3 全部初值逐点收敛：直接只有 coanalytic 上界

对固定 \(x\)，Cauchy 条件

\[
\forall m\ \exists N\ \forall p,q\ge N:
\|T^p x-T^q x\|\le1/m
\tag{4.3}
\]

是 \(\Pi^0_3\)。但“对所有 \(x\)”是一个不可数全称量词。由于 \((T,x)\mapsto T^n x\) 连续，非收敛对 \((T,x)\) 的集合 Borel；对 \(x\) 投影后，坏算子集 analytic，故全部逐点收敛类 coanalytic。

这尚未证明该类在当前有限维母空间非 Borel，也尚未证明其 coanalytic-complete。未查到可以不加假设直接替代这一缺口的原始定理，故不宣称已解决其精确复杂度。

只检查可数稠密初值集不够：若没有迭代族的等度连续性，稠密集上的收敛不能控制其补集。若整个迭代族 \(\{T^n\}\) 在每个紧集等度连续，则可用有限网把点态收敛升级为局部一致收敛；这是充分桥梁，但不能把单步 Hölder 连续误当成全迭代族等度连续。

## 5. 普通加权迭代乘积拓扑并没有增加长期控制

定义

\[
d_{\rm prod}(T,U)=\sum_{n=1}^{\infty}2^{-n}d_X(T^n,U^n).
\tag{5.1}
\]

它与 \(d_X\) 拓扑等价：\(n=1\) 项控制单步收敛；反向对有限项用命题 2.1，对尾项用 \(d_X\le1\)。

迭代图

\[
T\longmapsto(I,T,T^2,\ldots)
\]

在普通乘积 \(X^{\mathbb N_0}\) 中确实闭合，因为递推关系 \(f_0=I,f_{n+1}=T\circ f_n\) 闭。但其中“序列随 \(n\to\infty\) 收敛”的部分不闭；(4.1) 仍然是反例。

因此，**“把所有有限次迭代列进乘积”与“控制无限时行为”不是一回事。**

## 6. 全时间拓扑：一个真正覆盖所有收敛率的中立体系

### 6.1 全部连续动力系统的完整空间

定义

\[
d_{\rm dyn}(T,U)=\sup_{n\ge0}d_X(T^n,U^n).
\tag{6.1}
\]

\(n=0\) 项为零；\(n=1\) 使其成为真正度量。

**定理 6.1。** \((X,d_{\rm dyn})\) 完备；\(\mathcal C_{\rm pt}(S)\) 在其中为闭子空间，因此完备且 Baire。

证明：令 \(T_i\) 为 \(d_{\rm dyn}\)-Cauchy。其第一坐标在 \(d_X\) 下 Cauchy，故 \(T_i\to T\in X\)。对每个固定 \(n\)，命题 2.1 给 \(T_i^n\to T^n\)。若 \(i,j\ge i_0\) 时对全部 \(n\) 有 \(d_X(T_i^n,T_j^n)<\varepsilon\)，令 \(j\to\infty\) 得对全部 \(n\) 有 \(d_X(T_i^n,T^n)\le\varepsilon\)，所以动力学距离收敛。

再设每个 \(T_i\in\mathcal C_{\rm pt}(S)\)。固定初值 \(x\)。这里使用 (2.1)/(2.2) 的标准度量：固定点评价对该度量一致连续，因此动力学距离收敛保证 \(T_i^n x\to T^n x\) 对时间 \(n\) 一致；因每个序列 \((T_i^n x)_n\) 在完备状态空间收敛，其关于全时间的一致极限也收敛。固定 \(S\) 与极限落入闭集 \(S\) 均保持。证毕。

若把 \(d_X\) 擅自换成任意兼容有界完备度量，则评价只保证连续、不一定全局一致连续；上述点态类闭性的证明不能原样使用。第 6.2 节的局部一致收敛类不存在这个问题，因其收敛序列在 \(X\) 中有紧闭包。

这里并未证明它一般可分。事实上一般不可分，见第 6.4 节。

### 6.2 全部局部一致收敛动力系统是 Polish

对任意 Polish 完备有界度量空间 \((X,d_X)\)，令

\[
c(X)=\{(f_n)_{n\ge0}: f_n\text{ 在 }X\text{ 中收敛}\},
\qquad D(f,g)=\sup_n d_X(f_n,g_n).
\tag{6.2}
\]

**引理 6.2。** \(c(X)\) 是 Polish，且极限坐标 \((f_n)\mapsto\lim_n f_n\) 为 1-Lipschitz。

证明：一致 Cauchy 的收敛序列族有一致极限，三角不等式使极限序列仍 Cauchy，故完备。取 \(X\) 的可数稠密集 \(D_0\)。由 \(D_0\) 中有限个初段项与一个常值尾段构成的序列可数，并在 \(c(X)\) 中稠密。极限坐标的不等式由 \(n\to\infty\) 得到。证毕。

**定理 6.3。** \((\mathcal C_{\rm lu}(S),d_{\rm dyn})\) 是 Polish，且

\[
T\longmapsto\Pi_T\in C(E,S)
\]

连续，并满足

\[
d_X(\Pi_T,\Pi_U)\le d_{\rm dyn}(T,U).
\tag{6.3}
\]

证明：把 \(T\) 等距嵌入 \(c(X)\) 为 \((I,T,T^2,\ldots)\)。迭代一致性是闭条件；\(T|_S=I\) 与极限函数取值于 \(S\) 也是闭条件。因此其像为 Polish 空间的闭子集。最后应用引理 6.2。证毕。

这是真正的“所有局部一致点收敛算法”母空间，不是固定一个几何率或超吸引层。**所有速度可以同时存在，而且不必把某一尾模写进对象的数学身份。**

自然的等价表述，是把离散时间紧化为 \(\mathbb N_0\cup\{\infty\}\)，把 \(n\mapsto T^n\)、\(\infty\mapsto\Pi_T\) 看成到 \(X\) 的连续映射。全时间拓扑就是紧化时间上的一致拓扑。在该局部一致收敛类上，换用 \(X\) 的其他兼容度量不改变此拓扑：固定收敛轨道序列连同其极限在 \(X\) 中紧，兼容度量在该紧集附近有统一比较。

### 6.3 Borel 结构不变，纲结构不能据此转移

在 \(\mathcal C_{\rm lu}(S)\) 上，动力学拓扑与单步子空间拓扑拥有相同的 Borel 集。一个直接证明是：对固定 \(T\)，动力学开球

\[
\{U:d_{\rm dyn}(T,U)<r\}
=\bigcup_{q\in\mathbb Q,\,0<q<r}
\bigcap_{n\ge0}\{U:d_X(T^n,U^n)\le q\}
\tag{6.4}
\]

在单步拓扑下为 Borel；动力学空间可分，所以其每个开集是可数个此类球的并。反向由单步拓扑较弱立即成立。

然而 residual、第一纲、内点、稠密性依赖拓扑，不只依赖 Borel \(\sigma\)-代数。**相同 Borel 结构不是把分类结论从一种拓扑搬到另一种的许可证。**

### 6.4 全部点态收敛类的非可分性：固定凸非点解集仍会发生

在 \(K=[0,1]^2\)、\(S=[0,1]\times\{0\}\) 上，对每个 \(a\in(0,1)\) 定义

\[
T_a(s,r)=\bigl(s+r\,s(1-s)(s-a),\ r/(1+r)\bigr).
\tag{6.5}
\]

该映射保持 \(K\)：负增量不超过 \(s(1-s)\)，正增量也不超过 \(s(1-s)\)。其固定集恰为 \(S\)。当 \(r>0\) 时，\(r_n=r/(1+nr)\)、\(\sum r_n=\infty\)。若 \(0<s<a\)，切向坐标单调下降；其极限不可能处于 \((0,a)\)，否则负增量有常数倍 \(r_n\) 的下界，故极限为 0。\(a<s<1\) 时同理趋于 1；\(s=a\) 保持。

对 \(a<b\)，取 \(a<s<b,r>0\)，则

\[
\Pi_{T_a}(s,r)=(1,0),\qquad
\Pi_{T_b}(s,r)=(0,0).
\]

用 (2.2) 有 \(d_{\rm dyn}(T_a,T_b)\ge1\)。因此存在不可数个两两 1 分离的元素，\(\mathcal C_{\rm pt}(S)\) 不可分。

这不是 RLEB/LT 的反例比较；它只用于说明为何“全部点态收敛/Baire”和“局部一致收敛/Polish”应设为体系的两个层次。

## 7. 极限映射、迭代与复合：哪些运算确实连续

1. 在单步母空间 \(X\) 中，复合与有限次迭代连续；在 \(\mathcal C_{\rm lu}(S)\) 的动力学拓扑中，\(\Pi_T\) 连续。
2. 幂映射在动力学度量下非扩张：

\[
d_{\rm dyn}(T^k,U^k)
=\sup_n d_X(T^{kn},U^{kn})
\le d_{\rm dyn}(T,U).
\tag{7.1}
\]

3. 收敛类一般**不是复合封闭的半群**，即使解集相同、每个映射两步终止。

最小线性例：在 \(K=[0,1]\times[-1,1]^2\)、\(S=[0,1]\times\{(0,0)\}\) 上，

\[
T(s,x,y)=(s,y,0),\qquad U(s,x,y)=(s,0,-x).
\tag{7.2}
\]

\(T^2=U^2=P_S\)，但

\[
(T\circ U)(s,x,y)=(s,-x,0)
\]

有二周期。故不能在公理里无证明要求“所有收敛算子组成代数”。

一个可验证的充分条件是**两映射交换**。在紧 \(K\) 上，若 \(T,U\in\mathcal C_{\rm lu}(S)\) 且 \(TU=UT\)，则两个极限回缩相同，且 \((TU)^n=T^nU^n\) 一致收敛到该回缩。证明利用：一致收敛的连续迭代族 \(\{T^n\}\) 等度连续，\(U^n\to\Pi_U\)，而 \(T^n\Pi_U=\Pi_U\)。交换再给出 \(\Pi_T=\Pi_U\)。

在“每对都交换”的相对子域，复合关于动力学拓扑连续；紧集上的估计为

\[
\sup_n\|T_i^nU_i^n-T^nU^n\|_\infty\le
\sup_n\|T_i^n-T^n\|_\infty+
\omega_T\left(\sup_n\|U_i^n-U^n\|_\infty\right),
\tag{7.3}
\]

其中 \(\omega_T\) 是 \(\{T^n\}\) 的共同连续模。

## 8. 尾模见证空间：有用的桥梁，不是全部母空间的替代

### 8.1 闭的 Polish 见证空间

令 \(c_0^+\) 为趋零非负序列的 Banach 闭锥。定义

\[
\mathcal E_S=
\{(T,\Pi,w)\in X_S\times C(E,S)\times c_0^+:
d_X(T^n,\Pi)\le w_n\quad\forall n\}.
\tag{8.1}
\]

每个不等式是闭条件，因此 \(\mathcal E_S\) 是 Polish。它自动给出 \(T^n\to\Pi\)；忘却投影覆盖全部 \(\mathcal C_{\rm lu}(S)\)。反之对任何成员可取

\[
w_n(T)=\sup_{m\ge n}d_X(T^m,\Pi_T)\to0.
\tag{8.2}
\]

这个规范最小单调尾模满足

\[
\|w(T)-w(U)\|_\infty\le2d_{\rm dyn}(T,U).
\tag{8.3}
\]

故动力学空间有连续的规范尾模截面。另一方面，\(\mathcal E_S\) 的积拓扑也连续地投到动力学空间：近似尾模在 \(c_0\) 中一致接近，给出共同的长时间控制，有限段由迭代连续控制。

**不能只在有标签的 \((T,\Pi,w)\) 空间证明某类第一纲，然后直接把结论投给无标签 \(T\)。** 连续投影一般不保第一纲；证书冗余可能决定纤维大小，必须另证 category-preserving 性或直接在无标签空间证明。

### 8.2 固定尾界层：两种拓扑在该层一致

固定 \(\varepsilon_n\downarrow0\)。在紧 \(K\) 上考虑满足

\[
\sup_{x\in K,\ m\ge n}\|T^m x-T^n x\|\le\varepsilon_n,
\qquad
\sup_{x\in K}d(T^n x,S)\le\varepsilon_n
\tag{8.4}
\]

的 \(T\in X_S\)。这是单步空间中的闭层，故完备/Polish；其极限落入 \(S\)。两种拓扑在该层等价，因为长时间差由两个统一尾界与一个有限时间差控制：

\[
\sup_{m\ge n}\|T^m-U^m\|_\infty
\le2\varepsilon_n+\|T^n-U^n\|_\infty.
\tag{8.5}
\]

这正是把 RLEB/LT 各自收敛证书送入共同体系的合适桥梁：**共同尾界是两类条件推出的结论预算，而不是为了偏向其中某类先写入全空间。**

### 8.3 没有覆盖全部收敛速度的可数预制尾率清单

任意给定可数列候选尾率 \(\varepsilon_n^{(j)}\to0\)，可以对角选择严格下降 \(b_n\to0\)，使 \(b_n\) 不被任一候选率最终支配；即便允许每个率乘有限常数也可做到。取足够大的 \(n_k\)，使对所有 \(j\le k\) 有 \(\varepsilon^{(j)}_{n_k}<k^{-2}\)，而令 \(b_{n_k}\) 为 \(k^{-1}\) 量级并在中间单调插值即可。

这样的速度由真正连续动力系统实现：在节点 \(b_n\) 上规定 \(f(b_n)=b_{n+1}\)，并在相邻节点间线性插值，令 \(f(0)=0\)。则 \(f\) 连续递增、\(0<f(x)<x\) 对 \(x>0\) 成立，且

\[
\sup_{0\le x\le b_0}f^n(x)=f^n(b_0)=b_n.
\tag{8.6}
\]

再取 \(T(s,r)=(s,f(r))\)，便得到固定非点 \(S\) 的任意慢一致收敛。故“取可数个几何/Hölder/超几何预算层”不是全部收敛母空间的穷尽构造。

## 9. 共同初值域、局部化与无限维限制

### 9.1 局部理论必须先统一初值域

原定理若只对每个 \(T\) 给出各自的邻域 \(B_T\)，这还没有把所有 \(T\) 放进可逐项比较的同一算法空间。至少应固定共同紧初值集 \(B\)，并将是否留在共同合法工作域 \(K\) 作为接口条件。

当 \(T\) 仍为全域映射、只要求 \(T^n|_B\) 一致收敛时，可用

\[
d_{B,\rm dyn}(T,U)=d_X(T,U)+
\sup_n\min\{1,\|T^n-U^n\|_B\}.
\tag{9.1}
\]

保留 \(d_X\) 是为了区分在 \(B\) 的可达轨道之外不同的算子。它把对象嵌入

\[
X\times c(C(B,E)),
\]

其中迭代限制与取值条件闭，故得到同类的 Polish 构造。若另要求 \(T^n(B)\subset K\) 对全部 \(n\)，\(B,K\) 紧闭时也是闭条件。

如果 \(B\) 不正向不变，极限只定义在 \(B\) 上；\(\Pi\circ T\) 在所有 \(B\) 上甚至未必有定义，不应无条件称为全域回缩。需 \(S\subset B\) 才有“在 \(S\) 上恒等”的回缩口径。

### 9.2 无穷维 Hilbert 空间不能照抄有限维 Polish 论证

无限维 Hilbert 空间不局部紧，compact-open 拓扑不能直接由可数闭球耗尽给出，闭球也不紧。若改用 bounded-uniform 拓扑，可在“有界集映到有界集，且每个有界集上一致连续”的映射类上获得完备性和复合连续性；但该映射空间通常不可分。

因此，无穷维版本中要分开要求：

- 完备/Baire 足够，还是确实需要 Polish/标准 Borel；
- 使用 bounded-uniform 还是稠密集上的逐点拓扑；
- 复合所需的共同局部有界性与外映射的一致连续性。

单调/非扩张类拥有的共同 Lipschitz 模可补足某些环节，但不能在包括非 Lipschitz RLEB 的母空间中偷偷沿用。

## 10. 变步长 PPA 的 family/strategy 版本

### 10.1 同一个算子的完整 resolvent 家族

固定紧步长区间 \(\Lambda\subset(0,\infty)\)，考虑联合连续的

\[
\mathcal J:\Lambda\times E\to E,\qquad J_\lambda(x)=\mathcal J(\lambda,x),
\]

并要求对所有 \(\lambda,\mu\in\Lambda,x\in E\) 有完整一致性

\[
J_\lambda(x)=J_\mu\left(
\frac\mu\lambda x+
\left(1-\frac\mu\lambda\right)J_\lambda(x)
\right).
\tag{10.1}
\]

这些是联合 compact-open 空间 \(C(\Lambda\times E,E)\) 中的闭条件，故相应家族空间是 Polish。固定某个 \(\lambda_0\) 用 (1.1) 定义 \(F\)，双向使用 (10.1) 可验证所有 \(J_\lambda\) 都是同一个 \(F\) 的完整 resolvent。要求 \(J_\lambda|_S=I\) 仍为闭条件。

这是一个不预设单调、RL 或 EB 的共同步长族母空间。其覆盖边界也应明确：它要求 \(\Lambda\) 上每个步长都完整单值、并联合连续；只在零散可用步长上的算子要用另一个 family 层处理。

### 10.2 策略与非自治轨道

令允许策略集合 \(\Sigma\subset\Lambda^{\mathbb N_0}\) 为预先指定的闭集，策略 \(\sigma=(\lambda_0,\lambda_1,\ldots)\)。定义

\[
P_n(\mathcal J,\sigma)
=J_{\lambda_{n-1}}\circ\cdots\circ J_{\lambda_0},
\qquad P_0=I.
\tag{10.2}
\]

每个有限 \(P_n\) 关于 \((\mathcal J,\sigma)\) 连续。将“算子家族 + 策略”作为对象，用基空间距离再加

\[
\sup_n d_X\bigl(P_n(\mathcal J,\sigma),P_n(\mathcal J',\sigma')\bigr)
\tag{10.3}
\]

即可重复第 6 节的闭图/\(c(X)\) 证明，得到所有局部一致收敛 pair 的 Polish 空间。

若研究“对所有允许策略统一收敛”，\(\Sigma\) 紧时可把 \(P_n\) 看成 \(C(\Sigma,X)\) 的元素，并在该空间要求 \(P_n\) 收敛，仍得到 Polish 的全时间体系。这里统一性同时涉及初值紧集和策略。

必须分开以下量词：

\[
\exists\sigma\ \forall x\quad\text{收敛};\qquad
\forall\sigma\ \forall x\quad\text{收敛};\qquad
\text{在 }\sigma\text{ 与 }x\text{ 上共同一致收敛}.
\tag{10.4}
\]

三者不等价；从某一个固定步长的 \(T\)-空间定理不能越级推到后两者。把策略忘却后，“存在某策略”又引入投影，类的 Borel/纲性质必须重新审查。自适应、依赖当前状态的反馈步长不包含在上述预先给定序列策略内。

## 11. 可变解集的版本并非不可行

不固定 \(S\)，直接令

\[
\mathcal C_{\rm lu}=\{T:T^n\text{ 在 }X\text{ 中收敛}\},
\]

仍是动力学拓扑下的 Polish 空间；解集可事后定义为

\[
S_T=\operatorname{Fix}T=\Pi_T(E).
\tag{11.1}
\]

在紧状态空间上，

\[
d_H(S_T,S_U)\le\|\Pi_T-\Pi_U\|_\infty,
\tag{11.2}
\]

故解集对动力学拓扑连续。在 \(E=\mathbb R^d\) 上也有相应图/Fell 连续性：上极限由 \(T_i\to T\) 局部一致给出；对任意 \(s\in S_T\)，取 \(s_i=\Pi_{T_i}(s)\to s\) 得下极限。

固定非点 \(S\) 与可变 \(S\) 是两种合理比较口径。前者排除“泛型唯一解”把多解问题消掉；后者研究更大的算法世界。应把它们设成主空间与纤维，而不是以某个结论倒推应该只留哪一种。

## 12. 已核原始文献：哪些是既有语言，哪些尚待本项目完成

### 12.1 BRZ 2001：固定非点解集、完备空间、泛型极限回缩已有直接先例

Dan Butnariu、Simeon Reich、Alexander J. Zaslavski，*Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces*，Journal of Applied Analysis 7(2) (2001), 151–174，DOI [10.1515/JAA.2001.151](https://doi.org/10.1515/JAA.2001.151)，[作者原稿](https://math.haifa.ac.il/dbutnaru/publications/but-rei-zas-jaa.ps)。本轮直接读取已有原稿提取文本的 Introduction、Theorems 2.1、3.1–3.2、Proposition 5.1 及相关证明段。

其母空间固定闭凸 \(F\)，以 Bregman 相对非扩张条件定义 \(M(f;K;F)\)，在 bounded-uniform 拓扑下完备；连续/有界集上一致连续子空间均闭。**Theorem 2.1** 在附加假设下给剩余类，其迭代在有界初值集上一致收敛到 \(F\) 的回缩，并对邻近算子给统一长时间接近；**Theorems 3.1–3.2** 给其他相对非扩张层及扰动/初值连续性；**Proposition 5.1** 明确使用有界集上的一致连续性保证有限次迭代连续。

因此“固定多解集 + 完备算子空间 + 泛型极限回缩”本身不是新语言。该文的母空间仍带一个预设 Bregman 结构，未在上述原定理中声明覆盖全部连续 weakly Picard/PPA 收敛映射。

### 12.2 Reich–Zaslavski 2005：共同轨道合法域是不可省略的假设

Simeon Reich、Alexander J. Zaslavski，*Convergence of Iterates of Typical Nonexpansive Mappings in Banach Spaces*，C. R. Math. Rep. Acad. Sci. Canada 27(4) (2005), 121–128，[原始 ESI 1668](https://www.esi.ac.at/preprints/esi1668.pdf)。**Theorem 1.1** 在非扩张、有近似不动点的完备空间中给出除 \(\sigma\)-porous 集外的唯一固定点与稳定有限时间进入性质；因映射 \(K\to X\) 不必 self-map，迭代结论明确限于留在 \(K\) 的轨道段。它不能替代共同吸引域的核查。

### 12.3 Wang 2013：完整 resolvent 与单调算子空间的既有基线

Xianfu Wang，*Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent*，Nonlinear Analysis 87 (2013), 69–82，DOI [10.1016/j.na.2013.03.008](https://doi.org/10.1016/j.na.2013.03.008)，[arXiv:1301.6443](https://arxiv.org/pdf/1301.6443)。**Propositions 2.1、2.3、2.4** 给非扩张、极大单调和 resolvent 的完备空间；**Proposition 2.3(ii)** 在有限维识别图拓扑。**Theorem 2.13** 的泛型模板需要严格压缩稠密；固定至少两个解点的空间不满足该前提。这里应借鉴对象与拓扑设计，不能自动继承其唯一解泛型结论。

### 12.4 Tikhonov：全时间拓扑有成熟动力系统先例

S. V. Tikhonov，*Complete metric on mixing actions of general groups*，DOI [10.1007/s10883-013-9162-y](https://doi.org/10.1007/s10883-013-9162-y)，[arXiv:1207.5255](https://arxiv.org/pdf/1207.5255)。其 §2 使用 leash/lead 类型度量

\[
m(T,S)=d(T,S)+\sup_g a(T^g,S^g),
\]

**Theorem 1** 证明混合群作用空间完备且可分；§2 同时指出该全时间距离在全部群作用上通常不可分。对象是保测群作用、距离是相关性距离，不是 PPA；但“先按渐近性质定义对象，再用全时间一致控制建立完备可分空间”的原则确有先例。第 6 节不能据形式新颖宣称首创，须另做其精确版本的优先权检索。

## 13. 推荐的体系选择与仍未解决问题

推荐建立双层而非只选一个方便出结论的空间：

| 层次 | 对象/拓扑 | 可立即使用的结构 | 需要后续证明的内容 |
|---|---|---|---|
| 单步母空间 | 全部连续完整 resolvent；\(d_X\) | Polish；复合、有限迭代连续；图坐标明确 | 收敛类的相对 Baire 性；RLEB/LT 像集与纲 |
| 全点态收敛母空间 | \(\mathcal C_{\rm pt}(S),d_{\rm dyn}\) | 完备/Baire；不预设任何速度 | 一般不可分；极限仅 Baire-1；证书像的描述性质 |
| 全局部一致收敛母空间 | \(\mathcal C_{\rm lu}(S),d_{\rm dyn}\) | Polish；极限回缩连续；规范尾模 | RLEB/LT 是否都落入；其相对大小；单步拓扑之间能否转移 |
| 共同结论预算层 | 固定真正尾界 \(\varepsilon_n\) | 单步闭；两种拓扑等价 | 从每套原定理统一推出共同初值域和预算 |
| 变步长层 | 一致 resolvent 家族 + 指定策略类 | 闭 family 空间；非自治乘积版本 | 步长量词、策略投影及 adaptive 策略 |

现阶段确立的是建体系可行性与严格拓扑接口，**没有**证明下列命题：

- 全部 RLEB 算子在这个中立母空间中比全部 LT 算子大多少；
- LT 在 \(\mathcal C_{\rm pt}\) 或 \(\mathcal C_{\rm lu}\) 中第一纲；
- RLEB 可认证类在全部收敛类中稠密、余稀或覆盖大多数；
- 各类在单步拓扑和动力学拓扑中具有相同纲；
- 全部逐点收敛类在有限维单步拓扑下的最优描述集合复杂度。

真正的下一步是把两套条件分别翻译成上述无标签空间中的内生性质/证书映射，证明其落位与共同域，然后再问类的内部、闭包、纲、商空间或测度性质。反例和尖点只能检查某条映射/包含论断，不能替代这整个体系。
