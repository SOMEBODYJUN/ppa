# Hölder／模连续算子空间中的 Lipschitz 子类：范畴核查与可迁移定理

日期：2026-09-20。研究角色：独立核查函数空间范畴工具，服务于 RLEB 与 Luke–Tam 条件类的比较；不把二者预先等同为 Hölder 与 Lipschitz。

## 0. 结论先行

1. **工具不是空白。** 固定凹模连续映射空间的“泛型达到允许的粗糙度”已有原始论文；Ravasini 2024 Theorem 3.3 是明确先例。普通 Hölder 空间中较光滑子类很小，本身也不是新的数学现象。
2. **最合理的第一拓扑是固定证书层上的局部一致拓扑。** 有限维状态空间下，它能使共同模、固定解集和闭不等式形成紧致 Polish／Baire 空间。不要把“所有 Hölder 映射”只配一致拓扑后直接使用 Baire 定理。
3. **有一个很短的结构性范畴引理。** 一个凸映射类只要包含一个非 Lipschitz 成员，则其中 Lipschitz 子类是第一纲。故研究的主要困难不一定是复杂扰动，而是能否组织出自然、非退化、保留 RLEB 证书的凸层，或保留开放坐标投影的层。
4. **旧的固定 direct-RLEB 证书层一般不凸。** 本报告给出两个完整二值 resolvent 编码的显式成员，其平均离开同一个 EB 证书层，不能直接套用凸性引理。
5. 与空间架构代理交叉讨论后，得到一个**可以证明的超线性法向 RLEB 凸层**。在它里面，局部 Lipschitz 子类第一纲确实成立。但它只比较一个指定相对层，不能据此宣布全 RLEB 比整个 Luke–Tam 体系大，更不能仅凭第一纲结论判定理论优先权。

## 1. 原始文献：已读到的准确结果与未核到的部分

### 1.1 Ravasini：固定凹模的泛型饱和

Davide Ravasini, *Generic uniformly continuous mappings on unbounded hyperbolic spaces*, Journal of Mathematical Analysis and Applications 538(1) (2024), 128440；DOI [10.1016/j.jmaa.2024.128440](https://doi.org/10.1016/j.jmaa.2024.128440)；[原文 arXiv:2308.15277v2](https://arxiv.org/html/2308.15277v2)。以下按 v2 编号。

设完整、无界 hyperbolic 空间为 \(X\)，连续非零非降凹模为 \(\omega\)，\(\omega(0)=0\)，并令

\[
\mathcal C_\omega(X)=\{f:X\to X:\omega_f(t)\le\omega(t)\},\qquad
\omega_f(t)=\sup_{d(x,y)\le t}d(fx,fy).
\]

| 原文结果 | 拓扑 | 精确结论 |
|---|---|---|
| Theorem 3.3 | 有界集上一致 | 泛型 \(f\) 满足 \(\omega_f=\omega\) |
| Theorem 5.2 | 逐点；另要求 \(X\) 可分 | 同一饱和结论 |
| Theorem 4.1 | 有界像映射类上的全局一致距离 | 除 \(\sigma\)-lower porous 集外，\(\omega_f(t)<\omega(t)\) 对每个 \(t>0\) |

第三条不要求凹性，只要求原文的连续、非降、次可加模。以上是已核原文结论；不同空间／拓扑不能混用。

**本次独立推论：** 若 \(\omega(t)=Mt^\gamma\)、\(0<\gamma<1\)，则第一行的泛型映射不可能全局 Lipschitz，因为

\[
Mt^\gamma=\omega_f(t)\le Lt
\]

在 \(t\downarrow0\) 时矛盾。这个推论不等于“任一预先指定紧邻域上非 Lipschitz”；原文模中的点对可以随尺度移向无穷远。

### 1.2 Strobin：已确认先例，但本次未拿到原始定理页

Filip Strobin, *Some porous and meagre sets of continuous mappings*, Journal of Nonlinear and Convex Analysis 13(2) (2012), 351–361。

Ravasini 原文引言和参考文献 [8] 明确指出，Strobin 已在 Hilbert 空间的闭凸无界域上研究上述固定模空间，并得到饱和结论。**本次检索没有取得 Strobin 原始正文，因此不填造 DOI、arXiv 或定理号，不把二手归纳冒充独立读原文。** 数学使用以已完整核验的 Ravasini Theorem 3.3 为依据；历史最早编号仍待补核。

### 1.3 little Hölder 的原始研究论文核验

Jeremy LeCrone, *Elliptic Operators and Maximal Regularity on Periodic little-Hölder Spaces*, Journal of Evolution Equations 12 (2012), 295–325；DOI [10.1007/s00028-011-0133-z](https://doi.org/10.1007/s00028-011-0133-z)；[原文 arXiv:1110.5692v1](https://arxiv.org/html/1110.5692v1)。

**Proposition 1.2(a)**：非整数 \(\theta>0\)、\(\sigma>\theta\) 时，\(h^\theta(\mathbb T)\) 是 \(C^\sigma(\mathbb T)\) 在 \(C^\theta\) 范数中的闭包，包括 \(\sigma=\infty\)。这直接排除“光滑映射在 big Hölder 范数中稠密”的误说。本文不是 RLEB 范畴比较论文；这里只用其已核的空间结构事实。

## 2. 四种容易混淆的空间

以下先取 \(K=[0,1]\)，实值函数，\(0<\gamma<1\)：

\[
[f]_\gamma=\sup_{x\ne y}\frac{|f(x)-f(y)|}{|x-y|^\gamma},\qquad
\|f\|_\gamma=\|f\|_\infty+[f]_\gamma,
\]

\[
h^\gamma(K)=\left\{f\in C^{0,\gamma}(K):
\lim_{\delta\downarrow0}\sup_{0<|x-y|\le\delta}
\frac{|f(x)-f(y)|}{|x-y|^\gamma}=0\right\}.
\]

另令

\[
Z_{\gamma,M}=\{f\in C(K):f(0)=0,\ [f]_\gamma\le M\},\quad M>0.
\]

| 空间和拓扑 | 完备／Baire 性 | Lipschitz 子类的地位 |
|---|---|---|
| big \(C^{0,\gamma}\)，\(\|\cdot\|_\gamma\) | Banach；一般不可分 | 不稠密，闭包为 little Hölder；因而甚至是 nowhere dense 的子集 |
| little \(h^\gamma\)，同一范数 | Banach；在此紧区间可分 | 稠密且第一纲 |
| 固定模球 \(Z_{\gamma,M}\)，\(\|\cdot\|_\infty\) | 紧致、Polish、Baire | 稠密且第一纲 |
| 全 \(C^{0,\gamma}\)，只用 \(\|\cdot\|_\infty\) | 不完备，而且第一纲于自身 | 不能借 Baire 完备性解释“典型” |

这说明“稠密”与“第一纲”不矛盾；也说明更换范数会改变“可否用光滑算法逼近”的答案。

### 2.1 big 与 little 的独立核验

若 \(f\) 为 \(L\)-Lipschitz，则其小尺度 Hölder 商至多 \(L\delta^{1-\gamma}\to0\)，故 \(\operatorname{Lip}\subset h^\gamma\)。little 条件对 \(\|\cdot\|_\gamma\) 极限封闭。

但 \(f(t)=t^\gamma\) 不属于 little，因为 \(|f(t)-f(0)|/t^\gamma=1\)。对任意 Lipschitz \(g\)，

\[
\lim_{t\downarrow0}
\frac{(f-g)(t)-(f-g)(0)}{t^\gamma}=1,
\]

所以 \([f-g]_\gamma\ge1\)，光滑逼近不可能在同阶 big Hölder 范数中收敛。

另一方面，little 函数延拓后做卷积，在同阶范数中可逼近：先将增量分为 \(|x-y|\le a\) 和 \(|x-y|>a\)；前者由 little 模控制，后者由一致逼近误差除以 \(a^\gamma\) 控制。于是 Lipschitz／光滑闭包正是 little。作为 big 中真闭线性子空间，little 没有内点。

little 内的 Lipschitz 第一纲也可直接证明。每个

\[
L_m=\{f:|f(x)-f(y)|\le m|x-y|\ \forall x,y\}
\]

闭。取 \(\gamma<\sigma<1\)，\(t^\sigma\in h^\gamma\setminus\operatorname{Lip}\)；在任意 Lipschitz \(f\) 上加任意小非零倍的 \(t^\sigma\)，会离开全部 Lipschitz 类，故 \(L_m\) 无内点。

### 2.2 固定模球的稠密与第一纲：完整基准证明

\(Z_{\gamma,M}\) 在一致拓扑下闭、等度连续、有共同界 \(|f(t)|\le M\)，故 Arzelà–Ascoli 给出紧致性。

**稠密性：** 将 \(f\) 用区间截断投影延拓至 \(\mathbb R\)，其 Hölder 常数仍为 \(M\)。与标准非负核卷积，并减去在 0 的函数值，得到光滑 \(f_\varepsilon\)，仍满足 \(f_\varepsilon(0)=0\)、\([f_\varepsilon]_\gamma\le M\)，且一致收敛至 \(f\)。

**第一纲：** 对 \(f\in Z_{\gamma,M}\cap L_m\)，取

\[
g_\theta=(1-\theta)f+\theta Mt^\gamma,
\qquad 0<\theta<1.
\]

它仍在同一模球，且一致趋近 \(f\)，但

\[
\frac{|g_\theta(t)-g_\theta(0)|}{t}
\ge \theta M t^{\gamma-1}-(1-\theta)m\longrightarrow\infty.
\]

因此每个闭集 \(Z_{\gamma,M}\cap L_m\) 无内点，Lipschitz 子类为第一纲。

将 \(Mt^\gamma\) 换成 \(M(|t-a|^\gamma-|a|^\gamma)\)，并用可数有理子区间、\(\beta>\gamma\) 的可数指数和常数，得到更强的标准结论：泛型函数在任何非空子区间都不属于任何较高阶 \(C^{0,\beta}\)。**这不表示每个有限尺度的模都精确等于 \(Mt^\gamma\)**：在常值 0 的足够小一致邻域内，固定尺度 \(s>0\) 的振幅显然小于 \(Ms^\gamma\)。

### 2.3 为什么不能把常数自由的 Hölder 类直接当一致 Baire 空间

令 \(C_m=\{f:[f]_\gamma\le m\}\)。它们在 \(C^{0,\gamma}\) 的相对一致拓扑中闭，而

\[
C^{0,\gamma}=\bigcup_{m=1}^{\infty}C_m.
\]

给定 \(f\in C_m\)，加入任意小一致振幅、足够高频的光滑正弦函数 \(h\)，可使 \([h]_\gamma>2m\)，于是 \([f+h]_\gamma>m\)。故每个 \(C_m\) 无内点，整个空间第一纲于自身。将一切常数／指数／预算取并之后，其 Baire 性不能从各层的 Baire 性自动获得。

## 3. 最可用的结构引理：凸层与开放坐标

### 命题 A：凸层中的 Lipschitz 子类第一纲

设 \(Y\) 是取值于有限维线性空间的映射集合，\(B\) 为固定工作域。假设：

1. \(Y\) 对凸组合封闭；
2. 各点评价连续，且 \((1-\theta)T+\theta U\to T\) 当 \(\theta\downarrow0\)；
3. 存在 \(T_*\in Y\)，其 \(B\) 上限制非 Lipschitz。

则

\[
Y\cap\operatorname{Lip}(B)
=\bigcup_{m=1}^{\infty}
\{T\in Y:\|Tx-Ty\|\le m\|x-y\|\ \forall x,y\in B\}
\tag{A1}
\]

为第一纲 \(F_\sigma\) 集。若 \(Y\) 是非空 Baire 空间，其补集稠密且 residual。

**证明。** 各层由点评价连续性而闭。只需要检查闭层中的中心 \(T\)；它已经是 Lipschitz，无需给任意粗糙中心估计尖峰幅度。若 \(T\) Lipschitz，而 \(T_\theta=(1-\theta)T+\theta T_*\) 也 Lipschitz，则

\[
T_*=(T_\theta-(1-\theta)T)/\theta
\]

亦 Lipschitz，矛盾。这里准确排除了 cancellation：一个 Lipschitz 函数不能与非零倍的非 Lipschitz 函数相加而变成 Lipschitz。故每个闭层空内。证毕。

同一证明适用于任意固定较强 Hölder 阶。若 \(T_*\) 在 \(s\) 的每个邻域都非 Lipschitz，则对 \(B_n=\overline B_{1/n}(s)\) 再取可数并，可排除“在某个解点邻域内 Lipschitz”的子类。

**定理强度与新颖性界限：** 这是标准 Baire／线性空间套路的直接证明，不应作为新数学卖点。其优点是把工作集中到证书层的几何，而不是预先承诺某种尖峰扰动技术。

### 命题 B：开放坐标投影的迁移

若 \(\pi:Y\to Z\) 连续且开放，\(Z\) 中 \(L\) 第一纲，则 \(\pi^{-1}(L)\) 第一纲。对闭 nowhere dense 集 \(F\subset Z\)，若 \(\pi^{-1}(F)\) 包含非空开集 \(U\)，则非空开集 \(\pi(U)\subset F\)，矛盾；再取可数并即可。

因此，若能找到“局部可自由变化的切向函数坐标”，并证明

\[
\mathfrak R_{\rm LT}\cap Y
\subseteq\pi^{-1}(\operatorname{Lip}(B)),
\tag{A2}
\]

就可把已知函数空间范畴结果移入非凸 RLEB 层。**仅有连续 restriction map 不够；开放性／充分自由度必须证明。** 常值投影的反例即可看出：一个 meagre 单点的逆像可能是整个 \(Y\)。

## 4. 固定解集与完整 resolvent：哪部分自动，哪部分不自动

### 4.1 纯固定 trace 的 affine slice 很容易处理

在有内部的紧域 \(K\subset\mathbb R^d\) 上，固定闭集 \(S\cap K\) 上的 trace \(T|_S=I\)。若 \(K\setminus S\) 含一个球，可在球内取紧支撑 \(\gamma\)-尖峰。于是 big Hölder 的固定 trace 仿射空间中存在非 Lipschitz 成员，命题 A 直接给第一纲。

这甚至能解释为开放坐标：对球 \(B\Subset K\setminus S\)，取截断函数 \(\eta=1\) 于 \(B\)、支持避开 \(S\)，则

\[
Eh(x)=\eta(x)h(P_Bx)
\]

是 Hölder restriction 的有界线性右逆。因而仿射 Banach slice 到该球函数空间的 restriction 开放。加入 EB 和兼容条件之后，此右逆通常不再落在允许类中。

### 4.2 完整 resolvent 编码本身不增加困难

对连续 \(T:E\to E\) 定义

\[
F_T(u)=\{(x-u)/\lambda:Tx=u\}.
\tag{R1}
\]

则 \((I+\lambda F_T)^{-1}=T\) 在所有输入上精确成立；\(\operatorname{gph}F_T\) 是 \(\operatorname{gph}T\) 经可逆线性坐标变换的像，故闭。无需从选择分支推全图。

真正要保留的是：\(\operatorname{Fix}T=S\)、输出处的全纤维最小残差 EB、同一 all-pairs 反射模、共同局部预算和严格兼容。若还要求至多二值，需要另外保持输入纤维基数。

### 4.3 固定 direct-RLEB 证书层非凸：完整显式反例

取 \(E=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\)、\(\lambda=1\)、\(q=1/4\)，令

\[
T_\pm(p,r)=(p\pm\sqrt{|r|},q|r|),
\qquad \psi(t)=qt^2.
\tag{R2}
\]

每个 \(T_\pm\) 的所有非空逆纤维至多两点，因此 (R1) 给完整闭图至多二值算子，零集为 \(S\)。其反射满足，对 \(\delta=\|x-y\|\le R\)，

\[
\|R_{T_\pm}x-R_{T_\pm}y\|
\le 2\sqrt\delta+\tfrac32\delta
\le L\sqrt\delta,
\qquad L=2+\tfrac32\sqrt R.
\tag{R3}
\]

由于

\[
d(T_\pm x,S)=q|r|\le q\|x-T_\pm x\|^2,
\]

对全部输入纤维取下确界给真正最小残差 EB。兼容常数可取

\[
\kappa_R=\frac q4(\sqrt R+L)^2
=\frac q4(2+\tfrac52\sqrt R)^2<1.
\tag{R4}
\]

例如 \(R=0.01\) 时 \(\kappa_R=0.31640625\)。然而平均映射

\[
T_0=(T_++T_-)/2=(p,q|r|)
\]

在 \(r>0\) 小时，原 EB 将要求

\[
qr\le q(1-q)^2r^2,
\]

显然不成立。因此不能对原固定 \(\psi\) 层直接使用凸层引理。此例还说明“平均后进入一个 Lipschitz 类”不等于“仍保留相同 RLEB 证书”。

## 5. 一个可证明的 RLEB 相对层定理

以下是空间架构代理提出并由本分支独立核验的候选；它不是声称覆盖全 RLEB 的定理。

设有限维 \(E\)，非单点真仿射子空间 \(S\ni0\)，固定

\[
0<\gamma<1,\quad \nu=1/\gamma,\quad 0<q<1,
\quad R,\lambda>0,\quad A>R^{1-\gamma}.
\]

定义 \(Y\) 为所有连续 \(T:E\to E\) 满足

\[
T|_S=I,
\tag{Y1}
\]

\[
\|2(Tx-Ty)-(x-y)\|\le A\|x-y\|^\gamma
\quad(\|x-y\|\le R),
\tag{Y2}
\]

\[
d(Tx,S)\le q\min\{d(x,S)^\nu,d(x,S)\}
\quad(x\in E).
\tag{Y3}
\]

取局部一致拓扑，并要求

\[
\kappa:=\frac{q}{(1-q)^\nu}
\left(\frac{R^{1-\gamma}+A}{2}\right)^\nu<1.
\tag{Y4}
\]

### 5.1 全体成员的共同 RLEB 证书

令 \(d=d(x,S)\)。由 (Y3) 的线性上界和距离函数的 1-Lipschitz 性，

\[
\|x-Tx\|\ge d(x,S)-d(Tx,S)\ge(1-q)d.
\]

再由 (Y3) 的幂上界，

\[
d(Tx,S)\le qd^\nu
\le q\left(\frac{\|x-Tx\|}{1-q}\right)^\nu.
\]

对 (R1) 的全部输入纤维取下确界，得到

\[
d(u,S)\le\psi(r_{F_T}(u)),\qquad
\psi(t)=q\left(\frac{\lambda t}{1-q}\right)^\nu.
\tag{Y5}
\]

这不是选中残差。又因 \(\gamma\nu=1\)，对 \(0\le d\le R\)，

\[
\psi\left(\frac{d+Ad^\gamma}{2\lambda}\right)
\le\kappa d.
\tag{Y6}
\]

故同一严格 direct-RLEB 证书适用于整个 \(Y\)。固定点集恰为 \(S\)：若 \(Tx=x\)，(Y3) 给 \(d\le qd\)，只能 \(d=0\)。

### 5.2 空间结构

(Y1) 仿射，(Y2) 是范数凸约束，(Y3) 的右端只依赖输入而左端是到仿射集的凸距离，因此 \(Y\) 凸。三条在局部一致极限下封闭。

共同反射模给

\[
\|Tx-Ty\|\le\tfrac12(\|x-y\|+A\|x-y\|^\gamma),
\]

再用 \(T0=0\) 与线段分段，得到每个有界球上的共同界。有限维 Arzelà–Ascoli／对角线论证证明 \(Y\) 紧致，从而 Polish、Baire。非空性无需额外选择 signed 参数：正交投影 \(P_S\) 满足 (Y1)、(Y3)，其反射 \(2P_S-I\) 是等距映射，故对 \(0<\delta\le R\) 有 \(\delta\le R^{1-\gamma}\delta^\gamma<A\delta^\gamma\)，而 \(\delta=0\) 时条件显然成立，所以 \(P_S\in Y\)。

### 5.3 所有允许参数下的凸尖点见证，以及额外的非退化见证

**适用于上述全部允许参数的见证。** 因 \(S\) 非单点且为真子空间，可分别取单位切向量 \(v\in S\) 和单位法向量 \(n\in S^\perp\)。取

\[
0<c\le\frac{A-R^{1-\gamma}}2,
\qquad
T_c(x)=P_Sx+c\,d(x,S)^\gamma v.
\tag{Y7a}
\]

它固定 \(S\)，且像在 \(S\) 内，故满足 (Y3)。距离函数 1-Lipschitz，而 \(t\mapsto t^\gamma\) 在非负半轴的 Hölder 常数为 1，所以

\[
\|R_{T_c}x-R_{T_c}y\|
\le\delta+2c\delta^\gamma
\le(R^{1-\gamma}+2c)\delta^\gamma
\le A\delta^\gamma.
\]

于是 \(T_c\in Y\)。对每个 \(s\in S\)，

\[
\frac{\|T_c(s+tn)-T_c(s)\|}{\|tn\|}
=c|t|^{\gamma-1}\longrightarrow\infty.
\]

这给出命题 A 所需、在每个解点邻域均非 Lipschitz 的同层见证。因此下文 (Y9)–(Y11) 不依赖额外的 (Y8)。该见证有无限输入纤维；这不影响完整 resolvent 编码或全体 \(Y\) 的范畴结论，但不能借它声称有限纤维相对类的结论。

**满足额外预算时的非退化见证。** 下述 signed 构造另要求 (Y8)；它用于展示层内还可以同时具有有限纤维、非零法向动力学与粗糙切向变化，不作为所有允许参数下的非空论证。

在 \(E=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\) 令

\[
h(r)=\operatorname{sgn}(r)\min\{|r|^\nu,|r|\},
\]

\[
T_L(p,r)=(p,qh(r)),\qquad
T_*(p,r)=(p+c|r|^\gamma,qh(r)),\quad c>0.
\tag{Y7}
\]

\(h\) 连续、严格增、满射且 \(\operatorname{Lip}h\le\nu\)。于是两者都是全空间 homeomorphism，(R1) 实际给单值完整算子；不是靠所有点一步压到 \(S\) 的无限纤维退化。

若 \(q\nu\le1\)，则 \(T_L\) firmly nonexpansive，且其残差在法向有共同线性下界，因而是经典单调／几乎平均＋误差界接口的明确成员。具体 Luke–Tam 定理归属仍应由定义翻译分支最终列明。

\(T_*\) 在每个 \(s\in S\) 的邻域上非 Lipschitz；其反射模可由

\[
A\ge2c+(1+2q\nu)R^{1-\gamma}
\tag{Y8}
\]

保证；(Y8) 是这个特定 signed 见证的额外充分条件，不能由 \(A>R^{1-\gamma}\) 自动推出。选择 \(q\) 小和 \(R\) 小可同时满足 (Y4)。例如

\[
\gamma=\tfrac12,\quad\nu=2,\quad q=\tfrac1{16},
\quad c=\tfrac14,\quad R=0.01,\quad A=0.625
\]

时，\(q\nu<1\)，且 \(\kappa=0.009344\ldots<1\)。

### 5.4 可以下的结论

由命题 A，对任意固定 \(s\in S\)，

\[
\{T\in Y:T\text{ 在 }s\text{ 的某个完整邻域上 Lipschitz}\}
\tag{Y9}
\]

是第一纲。令 \(\mathfrak R_{\rm LT}^{\rm ap}\) 专指在同一完整 resolvent 上使用局部 all-pairs 几乎平均性接口的 Luke–Tam 子类。例如若某邻域内有

\[
\|Tx-Ty\|^2\le(1+\varepsilon)\|x-y\|^2
-\frac{1-\alpha}{\alpha}
\|(I-T)x-(I-T)y\|^2,
\quad 0<\alpha<1,
\tag{Y10}
\]

舍去非正项立即得到 \(\operatorname{Lip}T\le\sqrt{1+\varepsilon}\)。因此，令 \(\mathcal G_s\) 为 \(Y\) 中在 \(s\) 的每个邻域均非 Lipschitz 的 residual 集，可以准确写成

\[
\boxed{\quad
\mathcal G_s\subseteq
Y\cap\bigl(\mathfrak R_{\rm RLEB}\setminus
\mathfrak R_{\rm LT}^{\rm ap}\bigr),
\qquad
Y\cap\mathfrak R_{\rm LT}^{\rm ap}\text{ 第一纲}.
\quad}
\tag{Y11}
\]

**不是**把所有 Lipschitz 映射等同于 Luke–Tam 类；(Y10) 及所需 EB、非退化参数、算法匹配条件均可能比 Lipschitz 更强。其他 Luke–Tam 接口与其准确论文编号由定义翻译分支归档。

这里不能把“仅对解集的 pointwise／relative 几乎平均性”未经核对换成 all-pairs Lipschitz。若 Luke–Tam 采用更弱的相对点条件，(Y9) 不足以排除它。

### 5.5 仍不能下的结论

- 不是全体 RLEB 相对于全体 Luke–Tam 的范畴比较；普通线性法向率的 Luke–Tam 例子通常不在该超线性法向层。
- 不是 \(Y\) 内 Lipschitz 子类稠密的证明；meagre 与 dense 是两个问题。
- 不是在 \(Y_{\le2}\) 中的第一纲结论：虽然两个见证有限纤维，任意凸组合可能不保持有限纤维，ambient 第一纲不能任意限制到子空间。
- 不是半代数类内的泛型结论。广义 Hölder 空间典型成员可能处处粗糙，不具有有限公式的可表示性；若目标仍是半代数算法，应另外说明比较空间为何有实践含义。
- 不是“RLEB 只有坏初值稳定性”。这里只比较单步证书正则性，不是在判定极限选择非 Hölder 的大小。

## 6. 对可投稿价值的直接判断

最可能成功的 theorem route 是：

> **精确翻译两个理论的同一 resolvent 接口 → 定义有共同吸引域、共同证书且可证明 Baire 的相对算子层 → 证明该层的凸性或开放函数坐标 → 推出经典端点类第一纲。**

其中“第一纲推理”本身很基础；潜在可保留的新内容在于**自然且非人为排除旧理论的比较层、RLEB 证书保持、全图／全纤维 EB 桥接、以及对不同自然层的稳健比较**。

本次候选超线性法向层是一个真实的无限维函数空间结论，不是单个有限参数族。但它预先假定强法向衰减；收敛可直接由该衰减和共同 Hölder 单步模推出。因此，若论文止于这个层和命题 A，审稿人可能合理地认为：主要是已知函数空间粗糙性现象的一次框架内实现，尚不足以证明整个 RLEB 理论的深层优势。

要增强价值，优先补两类结构性成果：

1. 同一个自然比较空间中，同时容纳线性与超线性法向机制，并给各理论真正覆盖集的内部／稠密／第一纲分类，而不是只取一个方便层。
2. 将范畴差异与实质算法能力关联：同等可验证信息、相同算法和共同局部域下，哪些收敛现象只有 RLEB 可以认证；同时明确哪些仅是证明常数／证书选择差异。

## 7. 仍未解决清单

1. Strobin 2012 原始正文及准确定理号、可能 DOI：本分支未核到，不作填补猜测。
2. Luke–Tam 不同原定理使用 all-pairs 还是 relative-to-solution 条件的完整分类：交由定义翻译分支；(Y11) 严格限于明确定义的 all-pairs 接口，不能扩张到整个作者体系。
3. 普通几何法向 RLEB 层中的范畴结论：非凸反例阻止直接照搬，仍需开放坐标／保持证书的结构引理。
4. 至多二值、全单值或半代数相对类内的范畴：不能从大类的 residual 结论直接下推。
5. 跨所有证书层的统一 Baire 空间与结论：可数个 Baire 层取并不自动仍 Baire，也没有不依赖拓扑的“占多少”。

**最终评判：有可用且成熟的泛函分析体系；不需要从零搭建 Baire 理论。已有一个可证明的层内比较定理，但完整理论覆盖面的大小比较与价值判断仍需上述结构桥接，不能提前包装成“RLEB 几乎覆盖全部而 Luke–Tam 几乎什么也覆盖不了”。**
