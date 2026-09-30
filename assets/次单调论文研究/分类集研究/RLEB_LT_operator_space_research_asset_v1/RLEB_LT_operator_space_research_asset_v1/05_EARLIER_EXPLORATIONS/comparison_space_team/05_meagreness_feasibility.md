# RLEB 与 Luke–Tam all-pairs 类的范畴比较：可行性证明与边界

日期：2026-09-20。角色：第五组，独立数学可行性／反证压力测试。本文不修改原稿；不重新审查原 RLEB 的无关结果。以下新命题是本轮独立推导，尚非经过完整优先权排除的“新定理”。

## 0. 结论先行

可以做出比有限参数相图强得多的结果：在一个明确、无限维、非三角的 **固定解集、固定反射 Hölder 模、共同法向超吸引预算** 的完整 resolvent 空间中，所有算子都满足共同严格 RLEB，而在指定解点附近满足 Luke–Tam 2025 all-pairs 几何条件的算子构成第一纲集；其补为余稀集。

这不是“从一个例子推多数”的推断。关键是母空间有闭凸结构：每个固定 Lipschitz 常数层闭；同一个 admissible sharp-Hölder witness 与该层中的任意点作任意小凸组合，都会离开此层。本文给出完整的不抵消证明。

但必须保留三条限定：

1. 这是一个自然但有额外法向超吸引结构的 RLEB **层**，不是全部 RLEB 算子空间的定理。它不包含固定正几何法向因子、靠切向尖点实现超线性 EB 的全部旧例。
2. 使用的是 `LT all-pairs + 完整局部覆盖 ⇒ 局部 Lipschitz resolvent`。不把 “Lipschitz resolvent” 与 Luke–Tam 全部收敛假设等同，也不把 pointwise almost-averaged 文献全部归入被排除类。
3. 一般凸组合不保持二值性。本文另给一个与整个 Hölder 函数球同胚的、恰二值的 compact/Baire 结构层；其中也能证明 LT 类第一纲。没有将这个结论升级成所有至多二值 RLEB 算子空间的泛性。

优先推荐顺序是：**先采用 §1–4 的非三角共同结构空间作为主定理，再用 §5 的有限纤维函数空间说明此差异不来自无限纤维；最后才研究更大母空间和拓扑不变性。**

## 1. 一个全部满足 RLEB 的非三角母空间

这一空间方案由架构组提出，本组独立核算其全部下述接口与范畴证明。

令 \(E=\mathbb R^d\)，固定含原点的真线性子空间 \(S\)，并假定

\[
1\le\dim S<d.
\]

仿射情形平移后完全相同。固定

\[
0<\gamma<1,\qquad \nu=1/\gamma>1,\qquad
0<q<1,\quad R>0,\quad A>R^{1-\gamma}.
\]

定义

\[
m(t)=\min\{t^\nu,t\},
\]

以及满足以下三项的全部连续映射组成的空间 \(\mathcal Y\)：

\[
T|_S=I, \tag{1.1}
\]

\[
\|2(Tx-Ty)-(x-y)\|\le A\|x-y\|^\gamma
\quad\bigl(\|x-y\|\le R\bigr), \tag{1.2}
\]

\[
d(Tx,S)\le q\,m(d(x,S))\qquad(x\in E). \tag{1.3}
\]

所有量词是全输入的；没有只沿选中支、只沿某条轨道或只相对某个解点检查 (1.2)。法向约束 (1.3) 不要求三角形、不要求法向更新独立于切向变量，也不要求任何有限参数表达。

取 \(\lambda=1\) 只为减轻记号。一般 \(\lambda>0\) 采用

\[
F_T(u)=\{(x-u)/\lambda:Tx=u\}
\]

时，将下文 EB 中的残差 \(t\) 换成 \(\lambda t\) 即可，兼容常数最终不变。

### 1.1 完整算子、闭图和真 min-residual

定义整个多值算子

\[
F_T(u)=\{x-u:Tx=u\}. \tag{1.4}
\]

对任意 \(x,u\in E\)，

\[
u\in J_{F_T}(x)
\iff x-u\in F_T(u)
\iff Tx=u.
\]

因此完整 \(J_{F_T}=T\) 在整个 \(E\) 上成立。图关系

\[
\operatorname{gph}F_T
=\{(Tx,x-Tx):x\in E\} \tag{1.5}
\]

是 \(\operatorname{gph}T\) 的可逆线性变换，故闭图成立。

写 \(a=d(x,S)\)。反三角不等式和 (1.3) 给

\[
\|x-Tx\|\ge d(x,S)-d(Tx,S)
\ge(1-q)a. \tag{1.6}
\]

又因 \(m(a)\le a^\nu\)，

\[
d(Tx,S)\le qa^\nu
\le\frac q{(1-q)^\nu}\|x-Tx\|^\nu. \tag{1.7}
\]

故所有 \(T\in\mathcal Y\) 共用

\[
\boxed{\psi(t)=\frac q{(1-q)^\nu}t^\nu.} \tag{1.8}
\]

(1.7) 对 **每个** 逆纤维中的输入同时成立，所以取下确界得

\[
d(u,S)\le\psi(r_{F_T}(u)),\qquad
r_{F_T}(u)=\inf_{Tx=u}\|x-u\|. \tag{1.9}
\]

这是全部值集上的最小范数。空纤维只需按算子定义域约定处理；不将一个不存在的有限残差代入公式。

若 \(Tx=x\)，由 \(a\le qa\) 得 \(a=0\)。结合 (1.1)，

\[
\operatorname{zer}F_T=\operatorname{Fix}T=S. \tag{1.10}
\]

### 1.2 同一个严格 RLEB 余量和共同覆盖／吸引域

对 \(0\le t\le R\)，

\[
\begin{aligned}
\psi\!\left(\frac{t+At^\gamma}{2}\right)
&=\frac q{(1-q)^\nu}
\left(\frac{t^{1-\gamma}+A}{2}\right)^\nu t\\
&\le\kappa t,
\end{aligned}
\]

其中

\[
\boxed{\kappa=
\frac q{(1-q)^\nu}
\left(\frac{R^{1-\gamma}+A}{2}\right)^\nu<1.} \tag{1.11}
\]

把 (1.11) 作为固定预算。其非空性不成问题，例如

\[
\gamma=1/2,\quad\nu=2,\quad q=1/16,
\quad R=10^{-2},\quad A=1
\]

给 \(\kappa<0.022\)，且 \(A>R^{1-\gamma}=0.1\)。

每个输入都有唯一完整 proximal 输出，故覆盖是全局的。(1.3) 还直接给所有 \(T\) 的共同法向因子 \(d(Tx,S)\le qd(x,S)\)。对初始 \(d(x,S)\le R\)，所有后继仍在同一管域内。由 (1.2) 与最近解点比较，

\[
\|Tx-x\|\le\frac12\bigl(d(x,S)+A d(x,S)^\gamma\bigr).
\]

因此共同点尾界为

\[
\|T^kx-\Pi_Tx\|
\le\frac{R q^k}{2(1-q)}+
\frac{A R^\gamma q^{\gamma k}}{2(1-q^\gamma)}. \tag{1.12}
\]

这里实际共同法向上界 \(q\) 与 RLEB 保守证书 \(\kappa\) 是两项不同数值；本证明不混用它们。

### 1.3 闭凸、紧、无限维、Baire

赋予 \(C(E,E)\) 紧集上一致收敛拓扑。它由通常的 complete compact-open metric 给出。(1.1)–(1.3) 均对局部一致极限闭合。

\(\mathcal Y\) 是凸的：固定点条件仿射，(1.2) 是线性表达式的范数上界；由于 \(S\) 仿射，\(u\mapsto d(u,S)\) 凸，故 (1.3) 对凸组合保持。

(1.2) 给共同局部模

\[
\|Tx-Ty\|\le\tfrac12(\|x-y\|+A\|x-y\|^\gamma).
\]

加 \(T0=0\)，通过沿线段分段即得每个闭球上的共同有界性。有限维 Arzelà–Ascoli、逐球对角抽取、闭性说明 \(\mathcal Y\) 紧、可度量、完备、Baire。

它不是一个有限维参数集合：例如固定切向单位向量 \(e\in S\)，允许任意小的 \(\gamma\)-Hölder 函数 \(h\)，且 \(h|_S=0\)，取 \(T=P_S+h e\)，就得到无限维函数自由度。§5 给出更具体的完整函数球嵌入。

## 2. 主命题：LT all-pairs 层第一纲

固定 \(s\in S\)，取 \(r_j\downarrow0\)，令 \(B_j=\overline B_{r_j}(s)\)。定义

\[
\mathcal L_{m,j}=
\{T\in\mathcal Y:\|Tx-Ty\|\le m\|x-y\|
\ \forall x,y\in B_j\},\qquad m,j\in\mathbb N. \tag{2.1}
\]

每个 \(\mathcal L_{m,j}\) 对 compact-open 拓扑闭。并且

\[
\mathcal L_{\rm germ}(s)=\bigcup_{m,j}\mathcal L_{m,j} \tag{2.2}
\]

恰为在 \(s\) 的某个完整邻域内两点 Lipschitz 的映射类。

### 2.1 合法 sharp witness

取切向单位向量 \(e\in S\)、法向单位向量 \(n\in S^\perp\)，并选

\[
0<c\le\frac{A-R^{1-\gamma}}2.
\]

定义

\[
T_*(x)=P_Sx+c\,d(x,S)^\gamma e. \tag{2.3}
\]

其输出落入 \(S\)，所以 (1.3) 自动成立；它固定 \(S\)。由于距离函数 1-Lipschitz、\(t^\gamma\) 为 \(\gamma\)-Hölder，反射差满足

\[
\|2\Delta T_*-\Delta x\|
\le\|\Delta x\|+2c\|\Delta x\|^\gamma
\le A\|\Delta x\|^\gamma
\]

当 \(\|\Delta x\|\le R\)。所以 \(T_*\in\mathcal Y\)。又

\[
T_*(s+tn)-T_*(s)=c t^\gamma e,\quad t>0, \tag{2.4}
\]

给出每个 \(s\in S\) 邻域里的 sharp exponent \(\gamma\)。

### 2.2 不抵消的小扰动：完整证明

只需对可能的内点 \(T\in\mathcal L_{m,j}\) 做扰动。令

\[
T_\theta=(1-\theta)T+\theta T_*,\qquad0<\theta<1. \tag{2.5}
\]

凸性保证 \(T_\theta\in\mathcal Y\)，因此所有完整图、真实 EB、同一 \(S\)、严格余量和覆盖接口均保持。且 \(T_\theta\to T\) 局部一致。

对 \(0<t<r_j\)，由 (2.4)、反三角不等式和 \(T\in\mathcal L_{m,j}\)，

\[
\frac{\|T_\theta(s+tn)-T_\theta(s)\|}{t}
\ge\theta c\,t^{\gamma-1}-(1-\theta)m
\longrightarrow+\infty. \tag{2.6}
\]

因此任意 \(\theta>0\) 的扰动都不在 \(\mathcal L_{m,j}\)，事实上在 \(s\) 处不可能局部 Lipschitz。这里明确排除了“原函数恰好抵消尖点”的漏洞：被扰动的基点本来属于固定 Lipschitz 层，其 \(O(t)\) 项无法抵消非零 \(t^\gamma\) 项。

故每个 \(\mathcal L_{m,j}\) 闭且无内点，即 nowhere dense。由 (2.2)：

\[
\boxed{\mathcal L_{\rm germ}(s)\text{ 在 }\mathcal Y\text{ 中第一纲。}} \tag{2.7}
\]

其补是稠密 \(G_\delta\)。所有映射本来都满足 RLEB，所以这不是在一个大空间中证明“多数两种理论都不覆盖”。

### 2.3 到 Luke–Tam 类的合法逻辑链

Luke–Tam 2025 的 Definition 2 / Proposition 3 的 all-pairs submonotonicity，对同一 scale 的完整图输入坐标 \(x=u+u^+\)，给

\[
\|2(Tx-Ty)-(x-y)\|^2
\le(1+4\tau)\|x-y\|^2. \tag{2.8}
\]

只要所比较的输入邻域由满足该条件的完整裁剪图覆盖，就有

\[
\operatorname{Lip}(T)
\le\frac{1+\sqrt{1+4\tau}}2<\infty. \tag{2.9}
\]

所以对 **固定尺度、固定算法、局部完整图条件** 的 LT 类，

\[
\mathcal{LT}_{\rm conv}(s)
\subseteq\mathcal{LT}_{\rm geom}(s)
\subseteq\mathcal L_{\rm germ}(s). \tag{2.10}
\]

结合 (2.7)，得到它们都第一纲，而

\[
\boxed{\mathcal Y\setminus\mathcal{LT}_{\rm geom}(s)
\text{ 包含稠密 }G_\delta\text{，且为余稀集。}} \tag{2.11}
\]

“余稀集”按补为第一纲的通常定义使用；这里不自动声称 LT 类本身 Borel，也不自动声称 (2.11) 的整个集合恰为 \(G_\delta\)。明确的 \(G_\delta\) 是 \(\mathcal Y\setminus\mathcal L_{\rm germ}(s)\)。

本论证只需蕴含方向，不需要证明 maximal submonotonicity 对任意 Lipschitz \(T\) 的局部反向。Luke–Tam Theorem 2 还要求完整 maximality、metric subregularity、self-mapping、coverage，以及

\[
2\tau(1+\rho/\lambda)^2<1. \tag{2.12}
\]

这些不能从“\(T\) Lipschitz”自动得到。本文没有做这种替换。

文献原始依据：D. Russell Luke、Matthew K. Tam，*Generalized Monotonicity and the Proximal Point Algorithm*，Mathematics of Operations Research，2025，DOI [10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)。已读工作区原论文 Definition 2、Proposition 3、Assumption 2、Theorem 2，而非仅依据摘要。

## 3. 这个结论非空、也不是预先把 LT 删除

最简单的 LT 成员是 \(T_0=P_S\)。其 \(F_{T_0}=N_S\) 是最大单调算子，LT violation 为零，且完整 resolvent 满域。它属于 \(\mathcal Y\)，而 \(T_*\) 不局部 Lipschitz。

若不希望依赖“全部输出一步落入 \(S\)”的退化成员，取余维一坐标 \(x=(z,r)\)，令

\[
g_+(r)=q\,\operatorname{sgn}(r)\min\{|r|^\nu,|r|\},\qquad q\nu\le1,
\]

\[
T_0(z,r)=(z,g_+(r)). \tag{3.1}
\]

标量 \(g_+\) 严格递增、满射、1-Lipschitz，故 firmly nonexpansive；\(T_0\) 也 firmly nonexpansive。它的完整 \(F_{T_0}\) 为单值最大单调图，法向输出非零，具有真正超线性法向收敛。反射为非扩张，所以只需 \(A\ge R^{1-\gamma}\) 即属于 \(\mathcal Y\)。

对它加小切向尖点 \(c|r|^\gamma\) 得到同空间非-LT witness，且保持单纤维。这说明共同结构层确实同时含有旧理论成员与旧 all-pairs 几何不能覆盖的算子。

## 4. 拓扑改变后结论如何变化

### 4.1 Compact-open／同层图拓扑

§2 已证明局部 Lipschitz 类第一纲。没有证明它在一般 \(\mathcal Y\) 中稠密，因而不把“第一纲”改写成“无处稠密”。

在固定等度连续的紧层 \(\mathcal Y\) 上，局部一致 resolvent 收敛与对应完整图的有限维局部图收敛相容；完整图由 (1.5) 的可逆线性坐标变换编码。这一同层等价可用直接图收敛／等度连续论证，或紧到 Hausdorff 图空间的连续单射证明。离开共同模层，不声称任意 graph topology 都等同 compact-open。

### 4.2 强 \(C^{0,\gamma}_{\rm loc}\) 拓扑

使用局部 Hölder 半范数族，而不是全空间有界 \(C_b^{0,\gamma}\)：后者不能容纳无界 \(S\) 上的恒等映射。

\(\mathcal Y\) 在此 Fréchet 空间中闭，故完全度量且 Baire；一般不紧。凸组合 (2.5) 在强拓扑也趋于 \(T\)，因此第一纲证明仍然有效。

还可以加强为 nowhere dense。定义

\[
a_s(T)=\lim_{r\downarrow0}[T]_{\gamma;\overline B_r(s)},
\qquad
\mathcal Z_s=\{T\in\mathcal Y:a_s(T)=0\}. \tag{4.1}
\]

极限存在，因为局部半范数随 \(r\downarrow0\) 单调不增。若 \(T_n\to T\) 强 \(C^\gamma\) 且 \(a_s(T_n)=0\)，对任意固定球有

\[
a_s(T)\le[T-T_n]_{\gamma;B_r(s)}+a_s(T_n)\to0.
\]

故 \(\mathcal Z_s\) 闭。局部 Lipschitz 映射必在 \(\mathcal Z_s\) 中。对任何 \(T\in\mathcal Z_s\)，沿 (2.4) 计算得

\[
a_s((1-\theta)T+\theta T_*)\ge\theta c>0.
\]

所以 \(\mathcal Z_s\) 无内点，继而

\[
\boxed{\mathcal L_{\rm germ}(s),\ \mathcal{LT}_{\rm geom}(s)
\text{ 在强 }C^\gamma_{\rm loc}\text{ 的 }\mathcal Y\text{ 中均 nowhere dense。}} \tag{4.2}
\]

这是更强的拓扑排斥，不是概率结论。

### 4.3 little-Hölder 拓扑

在每个紧集上满足

\[
\lim_{\delta\downarrow0}
\sup_{0<\|x-y\|\le\delta}
\frac{\|Tx-Ty\|}{\|x-y\|^\gamma}=0
\]

的 little-Hölder 子空间内，原来的 \(t^\gamma\) witness 被排除。不能照抄 §2 的同一个 witness。

但对任意 \(\gamma<\eta<1\)，

\[
T_\eta(x)=P_Sx+c_\eta d(x,S)^\eta e
\]

是 little-\(\gamma\) 而非 Lipschitz。选

\[
2c_\eta R^{\eta-\gamma}+R^{1-\gamma}\le A
\]

即可使它仍在 \(\mathcal Y\)。little 子空间闭、凸，因此相同的 (2.5)–(2.6) 证明仍给 LT 类第一纲。

不过 (4.2) 的闭 nowhere-dense 容器在此不再有用：little 空间所有元素都属于 \(\mathcal Z_s\)。确实，在下面的标准函数球切片中，LT germ 可以 **稠密且第一纲**，所以不能无条件声称 little 拓扑中 LT nowhere dense。

## 5. 完整有限纤维的无限维函数空间切片

固定 \(H>0\)，令

\[
\mathcal H=\{h\in C([-1,1]):h(0)=0,\ [h]_\gamma\le H\}.
\tag{5.1}
\]

将 \(h\) 用 \(h(\max(-1,\min(1,r)))\) 延拓到全实轴。clamp 是 1-Lipschitz，所以延拓保持同一个 Hölder 常数。

\(\mathcal H\) 赋一致范数是无限维紧凸 Baire 空间；赋强 Hölder 范数是闭、完备、一般非可分的 Baire 空间。

### 5.1 恰二值切片

取

\[
g_-(r)=q\min\{|r|^\nu,|r|\},
\qquad T_h^-(z,r)=(z+h(r),g_-(r)). \tag{5.2}
\]

对 \(y>0\)，令

\[
a(y)=
\begin{cases}
(y/q)^{1/\nu},&0\le y\le q,\\
y/q,&y\ge q.
\end{cases}
\]

则完整图为

\[
F_h^-(u,y)=
\begin{cases}
\{(-h(a),a-y),(-h(-a),-a-y)\},&y>0,\\
\{(0,0)\},&y=0,\\
\varnothing,&y<0.
\end{cases} \tag{5.3}
\]

负输入、零输入均已包含；两支在 \(y=0\) 连续接合。由逆像唯一的 \(z=u-h(\pm a)\)，每个 \(y>0\) 恰两值，零面一值。对任意输入完整 \(J_{F_h^-}=T_h^-\)，零集固定为 \(\mathbb R\times\{0\}\)。

真残差精确为两支范数的最小值，且

\[
r_{F_h^-}(u,y)
\ge(1-q)a(y),\qquad
y\le q a(y)^\nu,
\]

所以同一个 (1.8) 成立，无需选支。

由于 \(g_-\) 是 \(q\nu\)-Lipschitz，反射差在 \(\delta\le R\) 时不超过

\[
\bigl(2H+(1+2q\nu)R^{1-\gamma}\bigr)\delta^\gamma. \tag{5.4}
\]

选择 \(q,R,H,A\) 使 (5.4) 的系数不超过 \(A\)，同时 (1.11) 严格成立，即把整个函数球置于同一个 \(\mathcal Y\) 证书层中。

映射 \(h\mapsto T_h^-\mapsto F_h^-\) 在本层是拓扑嵌入；其逆只需读取 \(T_h^-(0,r)\) 的首坐标。因此这一二值切片与 \(\mathcal H\) 同胚，在一致／compact-open 拓扑中是 **compact/Baire**，并不是未经证明的“全部二值映射的闭子空间”。

对 \(h\) 的 Lipschitz 层，§2 的尖点扰动直接适用：从 \(h\in\mathrm{Lip}_{m,j}\) 出发取

\[
h_\theta=(1-\theta)h+\theta H|r|^\gamma.
\]

它仍在 \(\mathcal H\)，且任意 \(\theta>0\) 都离开该 Lipschitz 层。因此此 **恰二值、完整 proximal、共同严格 RLEB** 的无限维层里，LT all-pairs 类第一纲。

此处不要求所有 (h) 半代数；无限维泛性和“全部半代数固定格式”是两种不同母空间。若额外强制半代数，必须重做 Baire 结构。

### 5.2 单纤维切片：实际 LT germ 稠密且第一纲

取 (3.1) 的 signed (g_+)，并设

\[
T_h^+(z,r)=(z+h(r),g_+(r)). \tag{5.5}
\]

它的完整图是单值

\[
F_h^+(u,y)=(-h(g_+^{-1}(y)),g_+^{-1}(y)-y). \tag{5.6}
\]

所有共同 EB／RLEB 证明不变。\(T_h^+\) 是全局 homeomorphism，故没有隐藏额外逆纤维。

给定任意 \(h\in\mathcal H\)，固定 \(0<\epsilon<1\)。将区间上的函数与全轴延拓显式分开，定义

\[
c_0(r)=\max\{-1,\min\{1,r\}\},\qquad
s_\epsilon(r)=\operatorname{sgn}(r)(|r|-\epsilon)_+,
\]

\[
h_\epsilon(t)=h(s_\epsilon(t))\quad(-1\le t\le1),
\qquad
\widehat h_\epsilon(r)=h(s_\epsilon(c_0(r)))\quad(r\in\mathbb R).
\tag{5.7}
\]

于是 \(\widehat h_\epsilon=h_\epsilon\circ c_0\) 正是 (5.1) 规定的 clamp 延拓；算子 \(T_{h_\epsilon}^+\) 的全轴切向项严格取 \(\widehat h_\epsilon\)。不能改成 \(\widehat h\circ s_\epsilon=h(c_0(s_\epsilon(r)))\)：该表达式通常在 \(1<r<1+\epsilon\) 上仍变化，因而不是固定切片的 clamp 延拓。

\(c_0\) 与 \(s_\epsilon\) 均 1-Lipschitz，且
\(\lvert s_\epsilon(c_0(r))-c_0(r)\rvert\le\epsilon\)。
因而 \(h_\epsilon\in\mathcal H\)、\([\widehat h_\epsilon]_{\gamma;\mathbb R}\le H\)，并且

\[
\|h_\epsilon-h\|_{\infty;[-1,1]}
=\|\widehat h_\epsilon-\widehat h\|_{\infty;\mathbb R}
\le H\epsilon^\gamma,
\qquad \widehat h_\epsilon=0\text{ 在 }[-\epsilon,\epsilon].
\tag{5.8}
\]

这不是宣称全局 \(h_\epsilon\) Lipschitz；它只在解集附近变为零。

取

\[
U=\mathbb R\times(-g_+(\epsilon),g_+(\epsilon)),
\qquad W=E.
\]

则在 \(U\) 上，完整算子恰为

\[
F_{h_\epsilon}^+(u,y)=(0,g_+^{-1}(y)-y). \tag{5.9}
\]

若 \(q\nu\le1\)，后一个标量函数单调且连续，所以 (5.9) 是单调图。它在 \(U\times E\) 上 **局部最大单调**：若某个单调扩展在 \(v\in U\) 增加值 \(w\)，与原图点 \(v+td\in U\) 比较，再令 \(t\to0^\pm\)，得到

\[
\langle d,w-F(v)\rangle=0\quad\forall d,
\]

故 \(w=F(v)\)。这是直接的 maximality 证明，没有把裁剪图最大性当作自动事实。

同时

\[
U'=\mathbb R\times(-\epsilon,\epsilon)
\subseteq (I+F_{h_\epsilon}^+)(U),
\]

完整覆盖成立；\(D=E\) 自映射；固定零集闭；超线性 EB 在小输出邻域给线性 subregularity。LT violation \(\tau=0\)，所以 Theorem 2 的严格阈值自动满足。

因此每个 \(F_{h_\epsilon}^+\) 都真正满足 LT Theorem 2 的 **germ 条件**，而 (5.8) 证明它们在整个函数球的一致拓扑中稠密。结合第一纲结论：

\[
\boxed{\text{signed 单纤维切片中，实际 LT germ 类稠密且第一纲。}} \tag{5.10}
\]

这不与补余稀矛盾。两类都稠密完全可能。

需要强调：LT 邻域随 \(\epsilon\downarrow0\) 缩小。**(5.10) 不是在固定共同初值球、固定 LT 参数预算上的稠密定理。** 对 fixed-domain LT 本文只保留第一纲和非空性。对 (5.2) 的 abs 二值切片，本文也不从 deadzone 自动推出局部 maximal submonotonicity，故不声称实际 LT germ 的稠密性；其 all-pairs 排除／第一纲证明不受影响。

### 5.3 little-Hölder 函数球中的实际 LT germ 仍稠密

若 \(h\) 是 little-\(\gamma\)，则 \(h_\epsilon\) 也是 little-\(\gamma\)，且 (5.7) 实际在强 \(C^\gamma\) 中趋于 \(h\)。证明：

先在 \([-1,1]\) 上证明。固定小 \(\delta>0\)，取 \(r,t\in[-1,1]\)。当 \(|r-t|\le\delta\)，因 \(s_\epsilon\) 1-Lipschitz，

\[
\frac{|(h\circ s_\epsilon-h)(r)-(h\circ s_\epsilon-h)(t)|}
{|r-t|^\gamma}
\le2\omega_h(\delta),
\]

其中 \(\omega_h(\delta)\to0\) 为 little-Hölder 小尺度半范数。当 \(|r-t|>\delta\)，比值不超过

\[
2\|h_\epsilon-h\|_\infty/\delta^\gamma\to0.
\]

先选 \(\delta\) 再令 \(\epsilon\to0\)，即得区间上的强收敛。又
\[
\widehat h_\epsilon-\widehat h=(h_\epsilon-h)\circ c_0,
\qquad
[\widehat h_\epsilon-\widehat h]_{\gamma;\mathbb R}
\le[h_\epsilon-h]_{\gamma;[-1,1]},
\]
所以固定 clamp 切片上的全轴／局部强 Hölder 收敛同时成立。因此 signed 切片中 LT germ 在 little-Hölder 拓扑也稠密；用适当归一化的 \(|r|^\eta\)、\(\gamma<\eta<1\) 扰动又证明它第一纲。

相反，在 big Hölder 强拓扑中，\(h=|r|^\gamma\) 与任何在 0 附近 Lipschitz 的 \(g\) 都满足

\[
[h-g]_\gamma\ge
\limsup_{r\downarrow0}\frac{|r^\gamma-g(r)+g(0)|}{r^\gamma}=1,
\]

所以 LT germ 不可能稠密。这给出了同一结构问题中可以精确验证的拓扑差异。

### 5.4 signed 切片的非-LT 性对任意 proximal 步长保持

本加强由架构组提出输入变换，本组独立核准。它只适用于当前 signed 结构切片，不能无证明升级到一般 \(\mathcal Y\)。

把 (5.5) 的算子按基准尺度 \(\lambda_0>0\) 编码：

\[
F_h(u,g(r))=
\left(-\frac{h(r)}{\lambda_0},
\frac{r-g(r)}{\lambda_0}\right),
\qquad g=g_+.
\]

对任意其他尺度 \(\mu>0\)，记 \(c=\mu/\lambda_0\)，定义

\[
H_c(r)=c r+(1-c)g(r). \tag{5.11}
\]

假定 \(g\) 单调且 Lipschitz 常数 \(a=q\nu\le1\)。对 \(r>s\)，若 \(0<c\le1\)，

\[
c(r-s)\le H_c(r)-H_c(s)
\le[c+(1-c)a](r-s);
\]

若 \(c\ge1\)，

\[
[c-(c-1)a](r-s)
\le H_c(r)-H_c(s)\le c(r-s).
\]

下界常数在两种情形都严格为正，且 \(H_c(0)=0\)，故 \(H_c\) 是全实轴到全实轴的双 Lipschitz 同胚。独立解完整 proximal inclusion 得

\[
\boxed{
J_{\mu F_h}(z,t)=
\left(z+c\,h(H_c^{-1}(t)),\ g(H_c^{-1}(t))\right).
} \tag{5.12}
\]

如果 \(J_{\mu F_h}\) 在原点附近 Lipschitz，取相同 \(z\) 比较第一坐标，再用 \(t=H_c(r)\) 的 Lipschitz 性，就推出 \(h\) 在 0 附近 Lipschitz。反之，若 \(h\) 不局部 Lipschitz，(5.12) 对 **每个** \(\mu>0\) 都不可能局部 Lipschitz。

因此在 signed 函数球切片中，

\[
\{h:\exists\mu>0,\ F_h
\text{ 在尺度 }\mu\text{ 满足 LT all-pairs germ 条件}\}
\subseteq\mathcal L_{\rm germ}(0). \tag{5.13}
\]

右侧第一纲，故左侧也第一纲；典型 \(h\) 对所有正步长都超出 LT all-pairs 覆盖。这里没有对不可数个第一纲集合直接作并的错误：是每个尺度统一蕴含同一个右侧集合。

这也不是借步长破坏算法定义域。所有 \(\mu>0\) 的完整 resolvent 在 (5.12) 中都全域单值。事实上，令 \(v=g(r)/r\in[0,q]\)（\(r\ne0\)），则

\[
\frac{|g(r)|}{|H_c(r)|}
=\frac{v}{c+(1-c)v}
\le\frac{q}{c+(1-c)q}<1.
\]

故改步长后仍有法向收缩，只是共同预算依赖 \(\mu\)。本节不声称它们保留基准 \(\lambda_0\) 的同一 RL/EB 常数。

## 6. 尖锐指数、拓扑与“多多少”的准确读法

§2 不只能排除 Lipschitz。对任何 \(\beta>\gamma\)、固定 \(m,j\)，在 \(B_j\) 上满足 \(\beta\)-Hölder 常数 \(m\) 的闭层也无内点，因为 (2.6) 中将 \(mt\) 换成 \(mt^\beta\) 即可。对一列 \(\beta_n\downarrow\gamma\) 取可数并，可得：

> 在 \(\mathcal Y\) 的 compact-open 拓扑中，典型完整 resolvent 在 \(s\) 的每个邻域都没有任何优于 \(\gamma\) 的 Hölder 指数。

这给“RLEB 的非 Lipschitz 增量不是少数孤立例子”一个严格的相对范畴含义。但它不是“占百分之多少”。Baire residual 不等于概率一；本文没有建立 prevalence、shyness 或任何未指定分布下的测度结论。

| 母空间／拓扑 | 已证的 LT 类大小 | 未证／不能推断 |
|---|---|---|
| 非三角超吸引层 \(\mathcal Y\)，compact-open／同层图拓扑 | 第一纲；补含稠密 \(G_\delta\) | LT 本身是否稠密、是否 nowhere dense；全 RLEB 的大小 |
| 同一 \(\mathcal Y\)，strong \(C^\gamma_{\rm loc}\) | nowhere dense | 任何概率／prevalence 结论 |
| \(\mathcal Y\) 的 little-\(\gamma\) 子空间 | 第一纲 | 一般层中的稠密性；不能沿用 sharp-\(\gamma\) witness |
| 恰二值函数球切片，compact-open | 第一纲；补余稀 | 实际 LT germ 的稠密性尚未证 |
| signed 单纤维函数球切片，compact-open | 实际 LT germ 稠密且第一纲 | 固定域 LT 证书稠密 |
| signed 单纤维函数球，允许任意正步长的 LT all-pairs 覆盖 | 仍第一纲；典型成员对所有正步长均不满足 | 任意一般 RLEB 算子的跨步长结论 |
| signed little-\(\gamma\) 函数球，strong little 拓扑 | 实际 LT germ 稠密且第一纲 | 不能改成 nowhere dense |

## 7. 两个必须写进论文的反例／限制

### 7.1 旧几何法向层会预先排除 Lipschitz，不能拿来公平数类

若某个固定层同时要求

\[
d(Tx,S)\ge q_-d(x,S),\quad q_->0,
\]

以及超线性 EB \(d(Tx,S)\le C\|x-Tx\|^\nu\)、\(\nu>1\)，那么它本来就不可能容纳在 \(S\) 附近 Lipschitz 的 \(T\)。因为 \(T|_S=I\)，Lipschitz 常数 \(K\) 给

\[
\|x-Tx\|\le(1+K)d(x,S),
\]

于是

\[
q_-d(x,S)\le C(1+K)^\nu d(x,S)^\nu,
\]

对 \(d(x,S)\downarrow0\) 矛盾。

所以若沿用原来的严格正几何法向因子与超线性 EB，得到“LT 空集”只是预先选空间导致的结果。用户要求先搭建公平母空间，这一点在数学上完全有根据。

### 7.2 换成 Lipschitz 母空间，结论当然可相反

这里必须同时保留 EB。精确定义

\[
\mathcal Y_{\rm FNE}
=\{T\in\mathcal Y:
\|Tx-Ty\|^2\le\langle Tx-Ty,x-y\rangle
\ \forall x,y\in E\}.
\tag{7.1}
\]

该额外不等式是闭条件，因此 \(\mathcal Y_{\rm FNE}\) 是紧／Baire 子空间；它含 \(P_S\) 及 (3.1) 的非退化正常模型。全部成员的完整逆图来自最大单调算子。

不仅有超线性 EB，(1.3) 与 (1.6) 还直接给

\[
d(Tx,S)\le q\,d(x,S)
\le\frac q{1-q}\|x-Tx\|.
\]

对每个完整逆纤维取下确界，得到真正的全局线性 EB

\[
\boxed{d(u,S)\le\frac q{1-q}\,r_{F_T}(u)}
\qquad(u\in\operatorname{dom}F_T).
\tag{7.2}
\]

故这里的 LT 收敛覆盖不是只凭最大单调性：完整 maximality、覆盖、自映射、闭零集与线性 EB 均成立，violation \(\tau=0\) 使严格阈值自动满足。因此在**这个保留共同法向／EB 预算的**母空间内，LT 可覆盖全部成员，而不是第一纲。

若删去 \(\mathcal Y\) 的 EB／法向限制，只说“固定 \(S\) 的 FNE resolvent 空间全部满足 LT 收敛定理”，则为假。最小反例是

\[
F(z,r)=(0,r^3),\qquad S=\mathbb R\times\{0\}.
\tag{7.3}
\]

它是连续全域最大单调算子，其完整 resolvent firmly nonexpansive，且同样固定非单点零集；但
\[
d((z,r),S)=|r|,\qquad r_F(z,r)=|r|^3,
\]
不存在原点附近的有限线性 EB 常数 \(\rho\)，因为 \(1\le\rho r^2\) 不可能对任意小 \(r\ne0\) 成立。因此它满足 LT **几何层**，却缺少这里的收敛证书假设；本报告不把这两层混同。

这不是反驳本报告的定理，而是说明不存在不依赖母空间的“RLEB 比 LT 大多少”。必须解释为什么选 Hölder normal-superattracting 环境，而不是仅用结果偏好挑选拓扑。

## 8. 价值判断与剩余真正难题

本轮已经超过“有限参数试验”的层次：有一个完整无限维非三角 Baire 空间，以及真图、真 EB、共同严格兼容下的相对余稀分离命题；另有完整恰二值函数球，说明该分离并不必然来自无限值算子。

但其范畴核心仍是经典的“较弱 Hölder 空间中 Lipschitz 子类小”机制。并且法向预算 (1.3) 加共同单步模本身就足以给 (1.12) 的收敛；本命题主要增加覆盖范围的结构比较，不是另一个更弱收敛判据。若论文只有给标准机制换成 resolvent 名字，创新强度可能有限。

本结论也没有证明“坏初值选择泛型”。例如 \(T=P_S+h e\) 的输出一步落在 \(S\)，所以 \(\Pi_T=T\) 本来就有 \(\gamma\)-Hölder 初值稳定性，而粗糙 \(h\) 仍可使 \(T\) 不属于 LT all-pairs 类。排除 LT 与极限选择失稳是两个不同问题。

真正需要第二轮审计的问题是：

1. 法向超吸引层是否是具有独立算法／几何意义的、已被研究过的标准类；该 RLEB 统一证书与 LT 排除是否形成未有的组合定理？
2. 能否把共同正常控制推广到允许几何法向、耦合残差支撑 EB 的非凸证书层，而不预先排空 LT？
3. 是否能在完整“至多二值”RLEB 子空间里证明第一纲，而不只在固定 normal 图的函数球切片？凸组合会破坏有限纤维，这是实质新障碍。
4. 是否能得到与一大类合理拓扑一致、或具有鲁棒定量内容的分类，而不是只在一个宽 Hölder 拓扑中重复粗糙函数的 genericity？
5. 有些 LT 系列收敛结果只要求相对固定点的 pointwise 几何，不等同 all-pairs Lipschitz。必须先明确该更大体系有没有覆盖这里的典型算子，才能把 (2.11) 写成对整个“Luke–Tam 体系”的排除。

**审计建议：`GO — 精确相对范畴定理已可成形；禁止升级为全 RLEB／全 Luke–Tam／绝对首创结论。`**
