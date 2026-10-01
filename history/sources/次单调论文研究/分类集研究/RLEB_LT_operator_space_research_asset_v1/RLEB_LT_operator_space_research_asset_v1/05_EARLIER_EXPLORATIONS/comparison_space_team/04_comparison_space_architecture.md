# RLEB 与 Luke–Tam 的统一算子空间：架构与可证明的相对纲差距

日期：2026-09-20。角色：空间架构与独立推导。本文不修改原稿；不把参数相图当作算子空间结论；不宣称已经分类全部 RLEB 算子。

## 0. 结论及比较口径

可以搭建一个真正无限维、紧致 Polish/Baire 的算子空间，并在一个明确的非线性结构层内证明：**RLEB 覆盖整个结构层，而 Luke–Tam 2025 Theorem 2 的同接口 all-pairs 类只占第一纲。** 这里的结构层不是有限参数族，也不固定三角算子公式；它由固定解集、共同连续模和一个法向超线性上界定义。

但必须保留三个边界：

1. 这是一个 **superattracting normal（法向超吸引）结构层中的相对定理**，不是“全部 RLEB 中 LT 为第一纲”。
2. “LT”在此指 Luke–Tam 2025 Theorem 2 / Assumption 2 的 all-pairs submonotonicity 接口。§5 先证明相同步长的版本；经独立复核，§11 已加强为：固定 \(T=J_{\lambda F_T}\) 的空间后，允许 LT 自由选择任意 \(\mu>0\)，可认证者仍为第一纲。这通过一个统一必要条件证明，不靠不可数并。不能把 Luke–Thao–Tam 的所有 pointwise almost-averaged 理论也装进这个结论。
3. 第一纲不是零测、不是某个百分比，也不自动证明理论原创。本文的纲证明采用标准的凸性与 Baire 方法；潜在研究价值在结构层的自然性、完整证书实现，以及能否扩展到更多不人为偏置的层。

我建议采用两级架构：

- 共同动力学母空间 \(\mathfrak X\)：固定解集、共同反射模和共同实际法向收缩；容纳普通 LT 及非线性 RLEB，负责公平的对象与拓扑口径。
- 最小可行主比较层 \(\mathfrak Y\subset\mathfrak X\)：加强为法向超线性上界；这一层全体均有同一严格 RLEB 证书，并可完整证明 LT 第一纲。

下文先给 \(\mathfrak Y\) 的完整证明，再解释更大母空间、证书分层和拓扑限制。

## 1. 完整 resolvent 是统一坐标，不预设原算子单值

固定有限维状态空间 \(E=\mathbb R^d\)、\(\lambda>0\)，以及真非单点仿射子空间 \(S\)。平移后令 \(0\in S\)，故可把 \(S\) 看作线性子空间，且

\[
1\le \dim S\le d-1.
\]

变量是连续映射 \(T:E\to E\)。定义整个多值算子

\[
F_T(u):=\{(x-u)/\lambda:\ T x=u\}.
\tag{1.1}
\]

这里 \(T^{-1}\) 是集合值逆像，未假定可逆。直接逐点计算：

\[
u\in J_{\lambda F_T}(x)
\iff (x-u)/\lambda\in F_T(u)
\iff T x=u.
\tag{1.2}
\]

所以 \(J_{\lambda F_T}=T\) 在整个 \(E\) 成立，不是挑选分支后的 identity。图关系为

\[
\operatorname{gph}F_T
=\{(T x,(x-T x)/\lambda):x\in E\}.
\tag{1.3}
\]

映射 \((x,y)\mapsto(y,(x-y)/\lambda)\) 是全空间线性同胚；因此连续 \(T\) 给出闭图 \(F_T\)。令 \(R_T=2T-I\)。对任意两个图点，取

\[
a=u-v,
\qquad b=u^*-v^*,
\qquad x=u+\lambda u^*,\ y=v+\lambda v^*.
\]

则

\[
a+\lambda b=x-y,
\qquad a-\lambda b=R_Tx-R_Ty.
\tag{1.4}
\]

所以 all-pairs Hölder RL 与 \(R_T\) 的 Hölder 模完全等价。此坐标没有遗漏跨分支比较。

## 2. 最小可行主比较层 \(\mathfrak Y\)

### 2.1 精确定义

固定

\[
0<\gamma<1,\quad \nu=1/\gamma,
\quad 0<q<1,\quad R>0,\quad A>R^{1-\gamma}.
\]

距离单位已归一化；\(\min\{t^\nu,t\}\) 的切换尺度为 \(1\)。如果需要物理尺度 \(r_0\)，可等价改成 \(t\min\{(t/r_0)^{\nu-1},1\}\)，并相应恢复常数。

定义 \(\mathfrak Y=\mathfrak Y(S;\gamma,A,R,q)\) 为全部连续 \(T:E\to E\)，满足

\[
T|_S=I, \tag{Y1}
\]

\[
\|R_Tx-R_Ty\|\le A\|x-y\|^\gamma
\quad(x,y\in E,\ \|x-y\|\le R), \tag{Y2}
\]

\[
d(Tx,S)\le q\min\{d(x,S)^\nu,d(x,S)\}
\quad(x\in E). \tag{Y3}
\]

预先要求数值严格余量

\[
\kappa_*:=\frac{q}{(1-q)^\nu}
\left(\frac{R^{1-\gamma}+A}{2}\right)^\nu<1.
\tag{2.1}
\]

这是全部映射满足的三个结构不等式，并非一个有限参数化算子族。除这些不等式外，切向分量可依赖全部输入变量，法向分量也不固定为某个三角公式。

严格模余量 \(A>R^{1-\gamma}\) 也立即保证所需的非 Lipschitz 见证存在：取任意单位切向量 \(e\in S\) 和

\[
0<c\le\frac{A-R^{1-\gamma}}2,
\qquad T^\sharp x=P_Sx+c\,d(x,S)^\gamma e.
\tag{2.1a}
\]

它固定 \(S\)、法向输出为零，而其反射差满足

\[
\|R_{T^\sharp}x-R_{T^\sharp}y\|
\le\|x-y\|+2c\|x-y\|^\gamma
\le A\|x-y\|^\gamma
\]

当 \(\|x-y\|\le R\) 时成立，故 \(T^\sharp\in\mathfrak Y\)。沿单位法向 \(n\) 有切向位移 \(c|t|^\gamma e\)，所以它在任何解点的完整邻域都不是 Lipschitz。此见证足以支撑下文全部空内点证明；若要求见证本身也具有非退化法向运动，则按 §4 的 (4.3) 另选 signed 构造参数，例如 (4.6)。

### 2.2 拓扑、完备性、紧性及值域有界性的来源

在 \(C(E,E)\) 上用紧集上一致收敛度量

\[
d_{\rm loc}(T,U)=\sum_{j\ge1}2^{-j}
\min\{1,\|T-U\|_{\overline B_j(0)}\}.
\tag{2.2}
\]

\(C(\mathbb R^d,\mathbb R^d)\) 在这个拓扑下可分且完全度量。\(d_{\rm loc}\)-Cauchy 序列在每个闭球上一致 Cauchy，局部极限相容且连续，给出完备性。

条件 (Y1)–(Y3) 对局部一致极限闭合，因此 \(\mathfrak Y\) 是闭子空间。进一步，由 (Y2)

\[
\|Tx-Ty\|\le h(\|x-y\|),\qquad
h(t)=\tfrac12(t+At^\gamma),\quad 0\le t\le R.
\tag{2.3}
\]

这给共同局部等度连续性。又由 (Y1) 有 \(T0=0\)。给定整数 \(j\ge1\)，选固定整数 \(N_j\) 使 \(j/N_j\le R\)，将 \([0,x]\) 分为 \(N_j\) 段，则

\[
\sup_{T\in\mathfrak Y,\ \|x\|\le j}\|Tx\|
\le N_jh(j/N_j)<\infty.
\tag{2.4}
\]

**因此不需要假设整个定义域或整个值域有界。** 所用的是：状态空间有限维，闭球紧；每个固定闭球上的映射值有共同界。这两点使逐球 Arzelà–Ascoli 与可数对角线抽取成立。所得极限仍在 \(\mathfrak Y\)，所以

\[
\boxed{\mathfrak Y\text{ 紧致、完全可度量、可分，因而 Polish 且 Baire。}}
\tag{2.5}
\]

这里不能原样换成无限维 Hilbert 状态空间：闭球不再紧，(2.4) 不足以推出值集相对紧。当前状态空间有限维，而映射空间已经无限维；无需为使用泛函分析而先把状态空间也无限维化。

### 2.3 凸性

若 \(T,U\in\mathfrak Y\) 且 \(0\le\theta\le1\)，令 \(V=(1-\theta)T+\theta U\)。

- 固定 \(S\) 的条件保持。
- \(R_V=(1-\theta)R_T+\theta R_U\)，所以 (Y2) 由三角不等式保持。
- 因为 \(S\) 仿射，\(d(z,S)=\|P_{S^\perp}z\|\) 是凸函数，故 (Y3) 保持。

因此 \(\mathfrak Y\) 是凸的。此处使用仿射/凸解集至关重要；任意非凸 \(S\) 不具有这个论证。

## 3. 所有成员的完整 RLEB 证书

### 3.1 零集和真实最小残差

由 (Y3) 有 \(d(Tx,S)\le qd(x,S)\)。若 \(Tx=x\)，则 \(d(x,S)\le qd(x,S)\)，故 \(x\in S\)。结合 (Y1)，

\[
\operatorname{zer}F_T=\operatorname{Fix}T=S.
\tag{3.1}
\]

距离函数是 1-Lipschitz，因而对每个输入 \(x\)

\[
\|x-Tx\|\ge d(x,S)-d(Tx,S)
\ge(1-q)d(x,S).
\tag{3.2}
\]

于是

\[
d(Tx,S)\le qd(x,S)^\nu
\le\frac q{(1-q)^\nu}\|x-Tx\|^\nu.
\tag{3.3}
\]

定义同一个 gauge

\[
\psi(t)=q\left(\frac{\lambda t}{1-q}\right)^\nu.
\tag{3.4}
\]

对固定 \(u\in\operatorname{dom}F_T\)，(3.3) 对整个纤维 \(T^{-1}(u)\) 的每个输入均成立。因此

\[
d(u,S)\le\psi\bigl(r_{F_T}(u)\bigr),
\qquad
r_{F_T}(u)=\frac1\lambda\inf_{Tx=u}\|x-u\|.
\tag{3.5}
\]

这使用整个多值算子的最小范数，不是选择残差。实际上非空值 \(F_T(u)\) 闭，有限维范数的下水平集紧，故该最小范数取得。空值的残差为 \(+\infty\)，EB 的陈述限于非空值即可。

值得注意的是，(3.3) 的下界来自法向位移，所以不会因切向项互相抵消而失效。这正是 \(\mathfrak Y\) 可以保持凸性的结构原因。

### 3.2 All-pairs RL、覆盖及严格兼容

(Y2) 和 (1.4) 给整个 \(\operatorname{gph}F_T\) 的 \(\mathrm{RL}(\lambda,\gamma,A)\)，包括所有跨分支点对。(1.2) 给全空间完整 range coverage。

取 \(s=P_Sx\)，\(r=d(x,S)\le R\)。由 (Y1)–(Y2) 的标准解点比较，或直接写 \(2(Tx-x)=(R_Tx-R_Ts)-(x-s)\)，得

\[
\|Tx-x\|\le\frac{r+Ar^\gamma}{2}.
\tag{3.6}
\]

代入同一个 \(\psi\)：

\[
\begin{aligned}
\frac1r\psi\!\left(\frac{r+Ar^\gamma}{2\lambda}\right)
&=\frac q{(1-q)^\nu}
\left(\frac{r^{1-\gamma}+A}{2}\right)^\nu\\
&\le\kappa_*<1 \qquad(0<r\le R).
\end{aligned}
\tag{3.7}
\]

故 \(\mathfrak Y\) 的所有成员满足同一个严格 direct RLEB 证书；gauge 定义在整个正半轴，不存在遗漏定义域预算。

### 3.3 共同初值域和统一尾界

固定 \(0<\rho\le R\) 并令 \(V_\rho=\{x:d(x,S)\le\rho\}\)。由 (Y3) 的实际收缩，所有 \(T\in\mathfrak Y\) 均有

\[
d(T^kx,S)\le q^k d(x,S)\le q^k\rho.
\tag{3.8}
\]

\(V_\rho\) 对所有成员前向不变。由 (3.6) 求和，

\[
\|T^kx-\Pi_Tx\|\le
\frac{\rho q^k}{2(1-q)}+
\frac{A\rho^\gamma q^{\gamma k}}{2(1-q^\gamma)}=:E_k.
\tag{3.9}
\]

因此所有成员在同一个管域收敛到 \(S\)。对固定初值紧集，轨道还留在共同的更大有界集内。这里 \(q\) 是从结构假设得到的实际统一因子；\(\kappa_*\) 是 RLEB 标量证书，不能混为同一个参数。

## 4. 非空性、无限维性和非退化 LT 成员

以下在最小状态空间 \(E=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\) 给出明确验证；已足以建立非平凡算子空间。

令

\[
g(r)=q\operatorname{sgn}(r)\min\{|r|^\nu,|r|\},
\qquad
T_0(z,r)=(z,g(r)),
\]

\[
T_*(z,r)=(z+c|r|^\gamma,g(r)),\qquad c>0.
\tag{4.1}
\]

\(g\) 连续、严格递增、满射且全局 Lipschitz，常数不超过 \(q\nu\)。利用

\[
\big||r|^\gamma-|r'|^\gamma\big|\le|r-r'|^\gamma,
\]

以及粗而足够的基底反射 Lipschitz 界 \(1+2q\nu\)，得到

\[
\|R_{T_*}x-R_{T_*}y\|\le
\bigl[2c+(1+2q\nu)R^{1-\gamma}\bigr]\|x-y\|^\gamma
\tag{4.2}
\]

在 \(\|x-y\|\le R\) 时成立。因此，只要

\[
A\ge 2c+(1+2q\nu)R^{1-\gamma},
\tag{4.3}
\]

两者均属于 \(\mathfrak Y\)。\(T_*\) 在任意 \((z,0)\) 的完整邻域都不是 Lipschitz，因为沿法向

\[
\frac{\|T_*(z,r)-T_*(z,0)\|}{|r|}
\ge c|r|^{\gamma-1}\longrightarrow\infty.
\tag{4.4}
\]

二者均为全空间同胚，所以对应 \(F_T\) 是单值闭图算子，完整 PPA 没有分支遗漏，也不是一步坍缩到解集的退化投影。

若再令 \(q\nu\le1\)，则 \(g\) 在一维单调且 1-Lipschitz，从而 firmly nonexpansive；\(T_0=I\times g\) 也 firmly nonexpansive。对应 \(F_{T_0}\) 为 maximal monotone：单调性由反射非扩张等价式给出，maximality 可直接证明——任何可加入的单调图点与具有相同 proximal 输入的已有图点比较，会迫使两点相同。

又由法向收缩

\[
d(T_0x,S)\le\frac q{1-q}\|x-T_0x\|,
\]

所以 \(F_{T_0}\) 有全局线性 EB 常数

\[
\rho_{\rm EB}=\frac{\lambda q}{1-q}.
\tag{4.5}
\]

它以 \(\tau=0\) 满足 LT2025 的 scalar threshold，且 coverage 全局成立。故 LT 在本层不是空集，也不只含一步投影。

例如以下参数同时满足全部数值条件：

\[
\gamma=\tfrac12,\ \nu=2,\ q=\tfrac1{16},\ R=\tfrac1{16},
\ c=\tfrac14,\ A=\tfrac{13}{16},
\]

\[
\psi(t)=\frac{16}{225}\lambda^2t^2,
\qquad \kappa_*=\frac{289}{14400}<1.
\tag{4.6}
\]

无限维性也可以直接看出：把切向项 \(c|r|^\gamma\) 换成任意满足 \(h(0)=0\)、\([h]_\gamma\le c\) 的连续函数（例如在 \([-1,1]\) 上选择后用 clamp 延拓），即嵌入一个完整 Hölder 函数球。它不是由有限多个参数决定。整个 \(\mathfrak Y\) 还允许非三角依赖，严格大于这个函数球切片。

## 5. LT 第一纲：精确引用、推导和闭集证明

### 5.1 LT 为什么落入局部 Lipschitz 类

原始来源：D. Russell Luke, Matthew K. Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, Mathematics of Operations Research, DOI [10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863)。本工作区提供的原论文全文为 `c01_luke_tam.txt`。

- Definition 2 的 submonotonicity 是指定图块上的 all-pairs 条件。
- Proposition 4 明确给出反射 resolvent 的 Lipschitz 常数 \(\sqrt{1+4\tau}\)，并与 \(\alpha=1/2\)、violation \(2\tau\) 的 almost-firm nonexpansiveness 等价。
- Theorem 2 使用 Assumption 2 的 all-pairs maximal submonotonicity、线性 metric subregularity、coverage 与 localization。

在与本文相同的 \(\lambda\) 和完整 proximal 输入域上，将其 scaled 条件写成

\[
\lambda\langle a,b\rangle\ge-\tau\|a+\lambda b\|^2.
\tag{5.1}
\]

于是

\[
\|a-\lambda b\|^2
=\|a+\lambda b\|^2-4\lambda\langle a,b\rangle
\le(1+4\tau)\|a+\lambda b\|^2.
\]

结合 (1.4)，

\[
\|Tx-Ty\|\le
\frac{1+\sqrt{1+4\tau}}2\|x-y\|.
\tag{5.2}
\]

因此任何在一个完整局部初值域上提供 LT2025 这类证书的成员，必定在该域 Lipschitz。这是 all-pairs 推论；只在解点处成立的 pointwise almost-averaged 条件不能用 (5.2) 替代。

本结论还要求相同的完整 resolvent/共同输入域。若 LT 只证某个低维不变集合上的局部选择，不能据本文的全邻域非 Lipschitz 将那个不同问题也排除。

### 5.2 固定共同邻域上的第一纲定理

此处使用 §2.1 的参数条件，特别是 \(A>R^{1-\gamma}\) 和 (2.1)；(2.1a) 已保证非空性及非 Lipschitz 见证。参数 (4.6) 还提供非退化见证，但空内点证明不额外依赖 (4.3)。固定 \(s\in S\)、\(0<\varepsilon\le\rho\)，令 \(B=\overline B_\varepsilon(s)\)。这个球包含真实的法向与切向初值，不能取成 \(B\subset S\)。定义

\[
\mathcal L_m(B)=\{T\in\mathfrak Y:
\|Tx-Ty\|\le m\|x-y\|\ \forall x,y\in B\}.
\tag{5.3}
\]

每个 \(\mathcal L_m(B)\) 在 \(d_{\rm loc}\) 下闭：局部一致极限可逐对传递不等式。

它没有相对内点。任取 \(T\in\mathcal L_m(B)\)，取 (2.1a) 的 \(T^\sharp\) 并记为 \(T_*\)；若 (4.3) 成立，也可用 (4.1) 的非退化见证。由凸性，对 \(0<\theta<1\)

\[
T_\theta=(1-\theta)T+\theta T_*\in\mathfrak Y,
\qquad T_\theta\longrightarrow T\quad(d_{\rm loc}).
\tag{5.4}
\]

若某个 \(T_\theta\) 在 \(B\) Lipschitz，则

\[
T_* =\theta^{-1}\bigl(T_\theta-(1-\theta)T\bigr)
\]

也在 \(B\) Lipschitz，矛盾。因此任意相对邻域都含不属于 \(\mathcal L_m(B)\) 的点。闭性和无内点给出 nowhere dense。

所以

\[
\operatorname{Lip}(B)\cap\mathfrak Y
=\bigcup_{m\ge1}\mathcal L_m(B)
\quad\text{为第一纲 }F_\sigma,
\tag{5.5}
\]

其补是稠密 \(G_\delta\)。由 (5.2)，

\[
\boxed{\mathfrak{LT}_{2025}(B)\cap\mathfrak Y
\text{ 是 }\mathfrak Y\text{ 中的第一纲子集。}}
\tag{5.6}
\]

不要求 LT 子集本身先是闭集或 Borel：它包含在一个第一纲集合中已经足够。若需要 LT 自身的 Borel 编码，见 §7。

### 5.3 允许缩小邻域的 germ 口径

取 \(B_n=\overline B_{\varepsilon/n}(s)\)。在 \(s\) 的某个完整邻域 Lipschitz 的成员为

\[
\mathcal L_{\rm germ}(s)=\bigcup_{n,m\ge1}\mathcal L_m(B_n).
\tag{5.7}
\]

同一个 \(T_*\) 在每个 \(B_n\) 非 Lipschitz，故仍为第一纲。因而对允许选择更小完整局部域的 LT germ 类，结论也成立。

这不证明 LT 在 \(\mathfrak Y\) 稠密或不稠密。某个三角函数球切片中的削平近似可证明该切片的 germ-LT 稠密，但不能自动升级到整个 \(\mathfrak Y\)，更不能把可变域的稠密性说成固定共同球上的稠密性。

## 6. 更大的共同母空间，以及不能写错的包含关系

### 6.1 共同动力学包络

把 (Y3) 放宽为

\[
d(Tx,S)\le qd(x,S)\qquad(x\in E),
\tag{X3}
\]

并保留 (Y1)–(Y2)，得 \(\mathfrak X(S;\gamma,A,R,q)\)。同样的论证证明它闭、凸、紧、Polish/Baire，且有同一完整 resolvent 和共同收敛域。

这个母空间可以同时容纳普通线性法向收缩和非 Lipschitz 的 RLEB 成员。因为母空间条件并不预先指定哪一套证书证明收敛，适合安放 direct、energy 和 LT 三种证书子类。

但若只在 \(\mathfrak X\) 中证明 Lipschitz/LT 第一纲，尚不足以说 RLEB 增加了余稀的一大块：必须再证明那个余稀集合被 RLEB 覆盖。\(\mathfrak Y\) 的作用正是提供一个确实全覆盖的自然结构层，而不把所有不属于 LT 的连续动力系统算作 RLEB。

### 6.2 Direct 与 energy 不可合并成一个假包含

最小反例取

\[
T_a(z,r)=(z,ar),\qquad \tfrac12\le a<1.
\tag{6.1}
\]

对应 \(F\) 为最大单调算子，线性 EB 的最小常数为

\[
\rho=\frac{\lambda a}{1-a}.
\]

由于切向恒等，\(\gamma=1\) 的 all-pairs 反射常数至少为 \(L=1\)。Direct scalar 条件要求

\[
\frac{(1+L)\rho}{2\lambda}<1,
\]

而此处左侧至少为 \(a/(1-a)\ge1\)。改用 \(\gamma<1\) 也不能救回 direct 证书：线性法向模型不具有所需的超线性残差 EB，兼容比在零处发散。它却完全属于 LT 单调情形。

正确口径是比较

\[
\mathfrak R_{\rm direct}\cup\mathfrak R_{\rm energy},
\]

不能无条件写 \(\mathfrak{LT}\subset\mathfrak R_{\rm direct}\)。原 RLEB 的线性 energy 条件为

\[
L^2<1+2\lambda^2/\rho^2.
\]

令 \(L^2=1+4\tau\)，变成 \(2\tau\rho^2<\lambda^2\)，可容纳 LT2025 的更强 scalar 阈值

\[
2\tau(1+\rho/\lambda)^2<1.
\tag{6.2}
\]

该包含还需相同完整/局部 coverage 接口，不能仅比较两个数值条件就忽略算子定义域。

一般非线性 energy 只保证 \(V(d_k)\) 几何衰减，不必给实际距离的逐步 Q-收缩。若要容纳它们，应再使用按共同能量 \(V\) 或共同尾预算分层的包络；不要声称 (X3) 已包含所有 energy 情形。

## 7. 证书层及 Borel 复杂度

### 7.1 固定证书层是闭的；整个可变证书类不自动 Baire

在 \(\mathfrak X\) 中固定 \(\lambda,\gamma,L,R,\psi,\kappa\)，其中 \(\psi\) 连续非降、\(\psi(0)=0\)。要求

\[
\|R_Tx-R_Ty\|\le L\|x-y\|^\gamma\quad(\|x-y\|\le R),
\]

\[
d(Tx,S)\le\psi(\|x-Tx\|/\lambda)\quad(x\in E),
\]

并要求相应 direct 或 energy 数值兼容。这些固定量词约束对局部一致收敛闭合，故固定证书层紧且 Baire（非空时）。

但可数个闭/紧证书层的并不自动是 Baire 空间。熟悉的类比是所有 \(\gamma\)-Hölder 函数按 Hölder 常数的可数并，在仅一致拓扑下可能第一纲于自身。不能先把所有常数放开，再未经证明称“整个 RLEB 是一个 Baire 空间”。

把“算子+证书”做成各层的不交并，确实可人为得到 Polish/Baire 空间，但同一算子会因证书不同重复出现；它的 category 可能依赖证书编码。此法适合审计记录，不宜冒充内在的算子大小比较。

### 7.2 固定指数与 power-gauge 全实指数的可数编码

固定 \(\gamma,\theta\) 时，对常数、严格余量和半径作可数分层是安全的。

**不能把所有 \(\gamma,\theta\) 都粗暴换成有理数。** 当最佳指数满足 \(\gamma\theta=1\)，且 \(\gamma\) 无理时，降低任一指数可破坏严格兼容，升高又可能破坏 RL 或 EB。

不过，对全空间 power-gauge 接口 \(\psi(t)=Kt^\theta\)，仍可严谨得到 \(F_\sigma\) 编码：对每个固定有理作用半径，保留实数指数，并把

\[
(\gamma,\theta,L,K,\kappa)
\]

放在可数族紧参数盒内，例如

\[
\gamma\in[1/n,1],\quad\theta\in[1/n,n],\quad
L\in[0,n],\quad K\in[1/n,n],\quad
\kappa\in[0,1-1/n].
\tag{7.1}
\]

在“算子 × 紧参数盒”中，RL、全纤维输入式 EB、direct 兼容都是闭约束。能量条件不必使用商，可以写成

\[
\frac{r^2+L^2r^{2\gamma}}2
\le\eta\bigl(r^2+\lambda^2K^{-2/\theta}r^{2/\theta}\bigr)
\quad(0\le r\le R),\quad \eta\le1-1/n,
\tag{7.2}
\]

同样闭合。紧参数投影为闭集；再对参数盒和半径可数并，得到相应 power direct / power energy 可认证类为 \(F_\sigma\)。这个方法不丢失无理临界指数。

任意连续 gauge 则可在 \(C_{\rm loc}([0,\infty))\) 的 Polish 参数空间中编码。若 witness relation 为 Borel，其存在性投影首先只能保证 analytic，不能直接宣布为 \(F_\sigma\)。如进一步固定紧致 gauge 模族，才可重复紧参数投影法。

### 7.3 LT 证书编码

固定同一个作用域/完整输入接口，分别标记：

- \(\mathfrak{LT}_{\rm geom}\)：存在有限 \(\tau\) 的 all-pairs scaled submonotonicity；
- \(\mathfrak{LT}_{\rm conv}\)：再有真最小残差线性 EB、coverage/localization，以及 LT2025 的 strict scalar threshold。

几何条件等价于有限 Lipschitz 常数的反射映射，是闭 Lipschitz 常数层的可数并。对收敛类，可将 \(\tau,\rho\) 放入有界参数盒，固定正 strict margin，加入全纤维输入式线性 EB，再投影；得到固定接口的 \(F_\sigma\) 编码。对严格不等式，向外微调常数至有理数也可行。

全球完整 resolvent 的 all-pairs 证书还自动给同常数的 maximality：如果扩张图中新增一点，以其 proximal 输入与现有完整图比较，输入差为零便迫使输出相同。局部图块的 maximality 和边界则需要单独核查，不能把此全球证明直接移植。

### 7.4 局部 EB 的边界陷阱

本文主层采取全空间输入式 EB，正是为了不漏掉域外逆纤维。如果仅要求“选中输入产生的输出满足 EB”，不能推出整个 \(F_T\) 的 min-residual EB。

要改成纯局部版本，至少应固定输出 collar，并对所有满足 \(Tx\) 落入 collar 的输入施加约束。若还限制残差阈值，单纯的条件式

\[
Tx\in V,\quad \|x-Tx\|/\lambda\le\bar t
\Longrightarrow d(Tx,S)\le\psi(\|x-Tx\|/\lambda)
\]

未必在变动 \(T\) 时闭合：极限点可能恰落在门槛边界，而近似点一直在门槛外。可用内外双 collar / 双残差阈值，以严格外门槛保护较小的闭工作域；或保留完整闭图-纤维量词另行证明闭性。不能删去本文全空间量词后沿用现成紧性证明。

### 7.5 至多二值与半代数条件

在有限维共同紧性框架中，“每个逆纤维至多两点”等价于一个 \(G_\delta\) 条件：对有界球中两两间距至少 \(1/m\) 的三点元组，三个像不能全部相等；相应连续最小值严格为正。因而

\[
\mathfrak Y_{\le2}=\{T\in\mathfrak Y:\#T^{-1}(u)\le2\ \forall u\}
\]

是 Polish/Baire 子空间，可用等价完备度量，但原限制度量未必完备。

**(5.6) 不能自动限制成 \(\mathfrak Y_{\le2}\) 内的第一纲结论。** 第一纲集合与任意子空间相交，可能等于整个子空间；凸混合也未必保持二对一。需要另外证明有限纤维子层中的密度/开放坐标桥梁，或使用独立的完整二值函数空间切片定理。

同样，不建议把“所有半代数映射”直接当作 Baire 母空间。它的描述复杂度是可数多种有限格式的并；必须指定复杂度层和拓扑后重新核查 Baire 性。无限维主空间中出现非半代数映射并不是缺陷，若需要保留半代数可实现性，应另研究有限描述切片或稠密近似，而不偷换母空间。

## 8. 不可混用的三种拓扑

| 拓扑 | 在本任务中的作用 | 不能据此偷换的结论 |
|---|---|---|
| 紧集上一致 / bounded-uniform resolvent 拓扑 | 本文主拓扑；共同模 + 锚点使层紧致 Polish；适合算子近似和同层大小比较 | 仅证明此拓扑的稠密/第一纲，不等于强 Hölder 范数结论 |
| 闭图的局部图拓扑，如有限维 Attouch–Wets | 可在共同模和锚定局部有界的本层中与上项对接 | 脱离本层、换成弱图拓扑或逐点拓扑后，不能照搬泛性；完整纤维仍须保留 |
| 固定紧域或局部 \(C^{0,\gamma}\) 强范数拓扑 | 控制 Hölder 尖点强度；闭约束可给 Baire 空间，但 big Hölder 通常不具可分性 | 一致拓扑的削圆近似一般不在强范数中收敛；little / big Hölder 不同；不能宣布同一个 Polish 空间 |

第二行的对接理由可以在本层自证：局部一致收敛给图收敛；反过来，图收敛加共同等度连续和局部有界，使任何子列都有局部一致收敛子子列，其极限图必须是指定图，所以全部局部一致收敛。\((x,Tx)\leftrightarrow(Tx,(x-Tx)/\lambda)\) 的线性同胚保留局部闭图收敛。有限维 proper 性把这些叙述对应到通常的局部距离函数/Attouch–Wets 描述。这里没有声称所有可能图拓扑都等价。

强 Hölder 拓扑还可能把差别放大：局部 Lipschitz 映射在固定 \(s\) 都满足

\[
\lim_{\rho\downarrow0}[T]_{\gamma;\overline B_\rho(s)}=0.
\]

这个 pointwise-little 条件在强 \(C^{0,\gamma}\) 拓扑闭合，而 (4.4) 的尖点不满足。故在那里可能得到 nowhere dense 的更强表述；这不是在一致拓扑下自动成立的结论。应先为应用理由选拓扑，不为得到更强结论而事后换拓扑。

此外，因 \(T|_S=I\) 且 \(S\) 无界、\(\gamma<1\)，通常的有界全局 \(C^\gamma(\mathbb R^d)\) 范数根本不容纳这些映射。需要固定紧域、局部半范数族或明确的仿射差/加权空间。

## 9. 已完成与仍需的桥接引理

### 已完成

1. 完整 resolvent 反构与闭图、全零集；
2. \(\mathfrak Y\) 的闭性、凸性、紧性、Polish/Baire 性；
3. 同一真最小残差 EB、all-pairs RL、全 coverage、严格兼容；
4. 同一非点解集、同一完整局部初值域、共同收敛尾；
5. 非退化 maximal-monotone/LT 成员和非 Lipschitz 成员同时存在；
6. LT2025 同接口类在 \(\mathfrak Y\) 中第一纲；
7. 固定证书和 power-gauge 可变证书的准确 Borel 编码框架。

### 尚未完成，不能写成定理

- **层间稳健性：**去掉固定超线性法向上界后，在更一般 RLEB 层仍否有上述差距？直接 RLEB 的一般固定证书层不一定凸，本文凸性证明不能原样移植。
- **全体 RLEB 的内在 Baire 模型：**怎样合并不同最佳指数、gauge、localization 与证书余量，又不让结果依赖证书标签或使空间第一纲于自身？
- **有限纤维桥梁：**\(\mathfrak Y_{\le2}\) 中是否仍有 LT 第一纲，或是否有一个连续开放的坐标投影到 Hölder 函数球，使 LT 落入 Lipschitz 逆像？
- **固定域 LT 稠密性：**可变小邻域的削平不能代替这个问题。本文不声称 fixed-domain 或全 \(\mathfrak Y\) 的 LT 稠密性。
- **更一般的跨步长理论：**LT2025 的局部 all-pairs 图块已由 §11 完成任意 \(\mu>0\) 的加强；任意步长下只锚定一个解点的 pointwise-AA 理论、任意低维比较集等没有被一并排除。
- **局部图块架构：**有限 collar 下的真 residual、full proximal coverage 和闭证书编码需要专门的局部扩张/隔离引理。
- **自然性与新增价值：**(Y3) 本身已给很强的法向动力学信息。需要说明此层为何在实际问题/原 RLEB 图块中自然出现，以及结论超出标准 Hölder-vs-Lipschitz 纲分离的具体部分。单凭第一纲标签不构成完整创新证明。

推荐论文级表述为：

> 在一个固定非点零集、完整 proximal 解、统一严格 RLEB 证书的无限维法向超吸引算子层中，能在指定解点取得 Luke–Tam 2025 局部 all-pairs 图块证书的成员，即使允许自由选择正步长，也只占第一纲；该层含非退化 maximal-monotone 成员。此为结构层内的相对覆盖差距，不是全部 RLEB 算子的全局泛性定理。

这已经实现了“先有算子空间及结构，再比较理论覆盖大小”的最小闭合版本；下一步应审查这个层的自然性和层间桥梁，而不是把一个范数或有限参数选择产生的大小错认成理论的绝对大小。

## 10. 阅读记录与协作接口

已读取：原 RLEB `sections/theorem_spine.tex` 的 RL、direct 和 energy 主干；修订 solution-selection `research_note.md` 的完整/局部接口与共同预算；`genericity_team/01_operator_space.md` 及 `06_math_stress.md` 的修补；LT2025 原文 Definition 2、Proposition 4 以及 Theorem 2 / Assumption 2 位置。

本报告采用 exact-translation 线核对的 LT all-pairs 口径、direct/energy 区别和无理临界指数警告。闭凸层的 Lipschitz 第一纲证明与 Hölder-category 线相互核对，法向 EB 与非退化 witness 与 feasibility 线相互核对。全部结论按本文公式独立展开；其他报告中的“PASS”不代替本文证明。

## 11. 第二轮加强：整个 \(\mathfrak Y\) 中允许任意正步长的 LT 类仍为第一纲

本节是对自然性审核提出的加强进行独立复核后的补充，替代初版中“全 \(\mathfrak Y\) 的任意步长比较尚未完成”的限制。它不假定另一步长的完整 resolvent 全局存在或单值，也不需要把 \(\mu\) 有理化。

### 11.1 精确的局部图块必要条件

仍以固定 \(\lambda>0\) 编码 \(F_T\)，固定一个解点 \(s\in S\)。假设存在某个 \(\mu>0\)、有限 \(\tau\ge0\)、\(s\) 的开邻域 \(U\) 和 \(0\) 的开邻域 \(W\)，使 \(\mu F_T\) 在 \(U\) 中、值限制于 \(W\) 时满足 LT 的 all-pairs submonotonicity：

\[
\langle u-v,a-b\rangle
\ge-\tau\|(u+a)-(v+b)\|^2
\tag{11.1}
\]

对所有 \(u,v\in U\)、\(a\in\mu F_T(u)\cap W\)、\(b\in\mu F_T(v)\cap W\) 成立。

这正是 LT2025 Definition 2 / Assumption 2(d)(i) 中的局部图几何部分；LT 主定理还要求 maximality、EB、coverage 和 strict threshold，但以下必要条件甚至不需要这些额外条件。因此它确实覆盖 LT 原文的局部截断接口，未以“完整 \(J_{\mu F}\) 在一个球内单值”替代原假设。

令

\[
c=\mu/\lambda>0,\qquad u=Tx,\qquad
a=c(x-u)\in\mu F_T(u),
\]

\[
z=u+a=cx+(1-c)u,
\qquad p=P_Sz.
\tag{11.2}
\]

当 \(x\to s\) 时，\(u\to s\)、\(a\to0\)、\(z\to s\)、\(p\to s\)。这里用到 \(T\) 连续、\(Ts=s\)、仿射投影连续。故只要 \(x\) 足够接近 \(s\)，就有 \(u,p\in U\)、\(a,0\in W\)。又因 \(p\in S=\operatorname{zer}F_T\)，\((p,0)\) 是允许的图点。可以在 (11.1) 中取 \(v=p,b=0\)。

LT Proposition 3(b) 的能量等价式在这里也可直接重算：

\[
\begin{aligned}
\|u-p\|^2+\|a\|^2
&=\|z-p\|^2-2\langle u-p,a\rangle\\
&\le(1+2\tau)\|z-p\|^2.
\end{aligned}
\tag{11.3}
\]

必须选 \(p=P_Sz\)，不是 \(P_Sx\)：于是右侧是 \((1+2\tau)d(z,S)^2\)。仿射性和 (Y3) 的较弱线性部分给

\[
\begin{aligned}
d(z,S)
&=\|cP_{S^\perp}x+(1-c)P_{S^\perp}Tx\|\\
&\le c\,d(x,S)+|1-c|\,d(Tx,S)\\
&\le\bigl(c+|1-c|q\bigr)d(x,S).
\end{aligned}
\tag{11.4}
\]

只取 (11.3) 的第二项，并用 \(\|a\|=c\|Tx-x\|\)，即得

\[
\boxed{\quad
\|Tx-x\|\le C_{\mu,\tau,q}\,d(x,S)
\quad\text{当 }x\text{ 足够接近 }s,\quad}
\tag{11.5}
\]

\[
C_{\mu,\tau,q}
=\sqrt{1+2\tau}\,\frac{c+|1-c|q}{c}<\infty.
\tag{11.6}
\]

结论的量词是：任何一个 \(\mu>0\) 的 LT 局部图块证书，都迫使原始 \(T=J_{\lambda F_T}\) 的位移在 \(s\) 附近被“到整个 \(S\) 的距离”线性控制。常数可依赖 \(\mu,\tau\)；无须在所有 \(\mu\) 上统一有界。

证明没有要求 \(x\mapsto z\) 可逆，没有假定 \(J_{\mu F_T}\) 全局存在或单值，也没有假定域外纤维不存在。所用图点全都由完整反构 (1.1) 提供，并通过邻域与连续性进入 LT 的实际测试图块。coverage 在 LT 收敛定理中仍是必要假设，但在这个排除用必要条件中不需要另行调用。

### 11.2 闭的位移层和无内点证明

对整数 \(m,j\ge1\)，定义

\[
\mathcal C_{m,j}(s)=\left\{T\in\mathfrak Y:
\|Tx-x\|\le m\,d(x,S)
\quad\forall x\in\overline B_{1/j}(s)\right\}.
\tag{11.7}
\]

\(\mathcal C_{m,j}(s)\) 对局部一致收敛闭合，故在 \(\mathfrak Y\) 中闭。

取 \(T\in\mathcal C_{m,j}(s)\)，使用 (2.1a) 的 witness 并记为 \(T_*\)；若 (4.3) 成立，也可用 §4 的非退化 witness。沿法向 \(x_t=s+tn\)，其中 \(n\) 是单位法向量、\(0<t<1/j\)，它具有尖锐切向位移

\[
P_S(T_*x_t-x_t)=a_*t^\gamma e,
\qquad a_*>0,\quad e\in S,\quad\|e\|=1.
\tag{11.8}
\]

在 (2.1a) 或二维公式 (4.1) 中，\(a_*=c\) 是该处的尖点系数；它与本节步长比 \(c=\mu/\lambda\) 无关，因此此处改记 \(a_*\)。

由 \(\mathfrak Y\) 凸性，\(T_\theta=(1-\theta)T+\theta T_*\in\mathfrak Y\)，且 \(T_\theta\to T\) 局部一致。由 (11.7)–(11.8)，

\[
\begin{aligned}
\frac{\|T_\theta x_t-x_t\|}{d(x_t,S)}
&\ge\frac{\|P_S(T_\theta x_t-x_t)\|}{t}\\
&\ge\theta a_*t^{\gamma-1}-(1-\theta)m
\longrightarrow+\infty.
\end{aligned}
\tag{11.9}
\]

因此任意 \(\theta>0\) 都使 \(T_\theta\notin\mathcal C_{m,j}(s)\)，甚至不能在 \(s\) 的任何完整邻域满足任何有限常数的线性位移界。故每个 \(\mathcal C_{m,j}(s)\) 无相对内点，进而 nowhere dense。

于是

\[
\mathcal C_{\rm germ}(s)
:=\bigcup_{m,j\ge1}\mathcal C_{m,j}(s)
\tag{11.10}
\]

是第一纲 \(F_\sigma\)，补集为稠密 \(G_\delta\)。

### 11.3 任意步长结论，以及不需要不可数并的原因

由 (11.5)，

\[
\left\{T\in\mathfrak Y:
\begin{array}{l}
\text{存在某个 }\mu>0\text{，使 }\mu F_T\text{ 在 }(s,0)\\
\text{的完整局部图块满足有限违约量的 LT submonotonicity}
\end{array}\right\}
\subset\mathcal C_{\rm germ}(s).
\tag{11.11}
\]

因此左侧是第一纲；满足 LT2025 完整收敛假设的类作为其子集，也为第一纲。这里从每个 \(\mu\) 的证书推出同一个可数 \(F_\sigma\) 必要条件族，所以没有使用“不可数个第一纲集合的并仍为第一纲”这一错误规则。

这是比 §5 更强的 **固定解点 \(s\)** 结论。它仍限于本文 \(\mathfrak Y\) 及所述完整局部图块。若问题改成“存在某个解点，某个很特殊的受限图子集/低维初值集合可以认证”，需重新核对量词；不能把固定 \(s\) 的结论不加说明地改为所有解点或任意局部选择的绝对排除。

### 11.4 单独记录：固定原步长的 pointwise-AA-at-\(s\) 类

对于原步长 \(\lambda\) 的单值 \(T\)，若在一个完整输入邻域上、锚定 \(s\in S\) 有 pointwise almost-averaged 估计

\[
\|Tx-s\|^2+
\frac{1-\alpha}{\alpha}\|x-Tx\|^2
\le(1+\epsilon)\|x-s\|^2,
\quad 0<\alpha<1,\quad\epsilon<\infty,
\tag{11.12}
\]

则至少推出固定点处的 Lipschitz calmness

\[
\|Tx-s\|\le\sqrt{1+\epsilon}\|x-s\|.
\tag{11.13}
\]

定义

\[
\mathcal A_{m,j}(s)=\{T\in\mathfrak Y:
\|Tx-s\|\le m\|x-s\|
\quad\forall x\in\overline B_{1/j}(s)\}.
\tag{11.14}
\]

这些集合闭。同样沿 \(s+tn\) 对 \(T\in\mathcal A_{m,j}(s)\) 与 (11.8) 的 witness 做凸混合，得到比值下界

\[
\theta a_*t^{\gamma-1}-(1-\theta)m\to\infty,
\]

因此每个 \(\mathcal A_{m,j}(s)\) 无内点。固定 \(\lambda\)、完整输入邻域上的 pointwise-AA-at-\(s\) 类包含在第一纲的 \(\bigcup_{m,j}\mathcal A_{m,j}(s)\) 中。

这是单独的 calmness 排除：它不把 pointwise-AA 误写成 all-pairs Lipschitz；也没有排除任意其他 \(\mu\) 下仅锚定一个解点的 pointwise-AA。若估计只在低维 \(\Lambda\) 上成立，而 \(\Lambda\) 不包含本文使用的法向输入，(11.14) 的量词不成立，本文不对此作排除结论。
