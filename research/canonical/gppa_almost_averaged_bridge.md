# C218 · 真残差到步残差的桥，以及非 calm 障碍的保真性

本页身份 C218-v1 / GP-ALMOST-BRIDGE，状态 `derived-checked`；[独立审查](../novelty/2026_10_09/new_claim_review.md)重构全部接口并关闭薄相对域反例。本页固定 C208/C209 的核关系与覆盖窗，不改变它们的身份。这里的正面桥是与既有文献接口的核对，不宣称首创。负面结论只排除同一映射及其双 Lipschitz 共轭下的有限常数 almost-averaged 证书，不排除任意换核、删支、升维或目标函数证明。

<a id="gab-data"></a>
## 对象、量词与文献门

在实 Hilbert 空间 H 上取关系 A、步长 λ>0、非空闭目标 Z⊂zer A。一个固定图块 Γ 包含全部 (p,0), p∈Z；在指定输入集合 E 上有 coverage 与零消失全对反射模，从而图块近端 T:E→H 单值。实际输出 y=Tz、选中值 f=(z−y)/λ 属于完整 A(y)。令 s=||z−y||。假设本窗 s≤s_max，并且在全部实际输出上有

\[
d(y,Z)\le\psi(r_A(y)),\quad r_A(y)=\inf_{g\in A(y)}\|g\|,
\quad\psi:[0,s_{\max}/\lambda]\to[0,\infty)
\]

连续、严格增加、ψ(0)=0。实际 residual 门由 r_A(y)≤s/λ 开启。若从 C209 调用，s_max=B(R) 且其评价域门已给出；不额外假定 residual 极小值取得、Z 有最近点或 E 自身完备。

一级文献：Luke–Thao–Tam, arXiv:1605.05725v2，Definition 2.3、Propositions 2.4/2.8、Definition 2.17、Theorem 2.18/Corollary 2.19，[全文](https://arxiv.org/html/1605.05725v2)。该版本 Definition 2.3 的 violation ε∈[0,1)，背景为有限维 Euclidean 空间。本页初等恒等式可在任意 Hilbert 空间证明；导入其定理须另核有限维、相对域、全管 almost-averaged、环域 gauge 及 rate 条件，不能由一个公式相似自动授予。

<a id="gab-residual"></a>
## 输入步残差桥

对每个 z∈E 都有

\[
d(z,Z)\le s+\psi(s/\lambda)=:h(s).
\tag{AB1}
\]

证明：三角距离不等式给 d(z,Z)≤||z−y||+d(y,Z)，再用完整 r_A(y)≤||f||=s/λ 与 ψ 单调性。不需要最近点或残差取到。h 在 [0,s_max] 连续严格增加；若需文献的全域 gauge，可在其上端接任意正斜率直线，形成连续严格增加无界函数，保持本窗全部估计。因此完整真 EB 与输入步 EB 的位置不同，并不是不可跨越的区别。

要把 AB1 命名为源 Definition 2.17 的相对 gauge subregularity，须另给相对域 Λ、T 的同域定义/输出以及 d(z,Z)=d(z,Fix T∩Λ) 的目标保距离合同。闭 Z⊂zer A 与局部 U 本身不保证 Z∩U 保留全部零点距离。AB1 作为明定目标 Z 的距离桥不需要这些附加门；源定理导入需要逐项核它们。

反向不成立：允许转移的步残差可以漏掉完整 A(y) 中更小的图值，见 [F48](../../FAILED_ROUTES.md#f48)。本页没有从输入步 EB 反推同 ψ 的完整真 EB。

AB1 常数可取等。令 A=ε Id、Tz=z/(1+λε)、Z={0}、ψ(t)=t/ε，任取 z≠0；则 s=λε||z||/(1+λε)、ψ(s/λ)=||z||/(1+λε)，二者之和正好是 d(z,Z)。

<a id="gab-linear"></a>
## 线性反射角的精确已有接口

固定一对已覆盖输入 z,w，δ=||z−w||，定义 C=2T−Id。平行四边形恒等式给

\[
\|Tz-Tw\|^2+\|(I-T)z-(I-T)w\|^2
=\frac{\delta^2+\|Cz-Cw\|^2}{2}.
\tag{AB2}
\]

若同一受检点对有 ||Cz−Cw||≤Lδ，则

\[
\|Tz-Tw\|^2+\|(I-T)z-(I-T)w\|^2
\le(1+\varepsilon)\delta^2,
\quad\varepsilon=\max\{0,(L^2-1)/2\}.
\tag{AB3}
\]

在 L<√3 时 ε∈[0,1)，AB3 正是源 Proposition 2.4 在 α=1/2 的 almost-firmly-nonexpansive 形式；L≤1 是 firm 角。对 L≥√3，AB2/AB3 仍为代数界，但不能沿该版本 Definition 2.3 不加条件地调用原定理。反向，AB3 给反射 Lipschitz 常数 √(1+2ε)。cutoff 图块只给同 cutoff 的结论，不能改写成全空间声明。

更直接的 PPA 先行是 Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, MOR (2025), [DOI 正文](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)，Proposition 3(b)、Lemma 1、Theorem 2。其 submonotonicity 参数对缩放关系 λA 为 τ=max{0,(L²−1)/4}；Lemma 1 已给线性 ψ(t)=ρt 时的 AB1，即 d(z,S)≤(1+ρ/λ)s。该文 maximal submonotonicity、局部同域/coverage、τ(1+ρ/λ)²<1/2 等门不能被本页代数替代。

因此线性反射与线性/一般 gauge EB 这一重合角已有明确文献机制。AB1/AB2 的证明并不担任新颖性证据。

<a id="gab-obstruction"></a>
## 完整 SF 的非 calm 障碍及双 Lipschitz 不变量

固定 ν>1、0<γ<1、A0>0、0<ρ<1，采用 [C215 的完整二维 SF](gppa_reformulation_boundary.md#grb-linearization)：

\[
F(\xi,y)=\{(-A_0 y^{\gamma/\nu},y^{1/\nu}-y),
(-A_0 y^{\gamma/\nu},-y^{1/\nu}-y)\},\ y\ge0,
\]

负 y 空，λ=1。全部完整近端为

\[
T(\xi,r)=(\xi+A_0|r|^\gamma,|r|^\nu),
\quad S=\mathbb R\times\{0\}.
\]

它满足 C215 明写的同图局部反射模、真 EB、coverage、小窗兼容与留域条件。任意固定点 p=(ξ0,0)，取 z_r=(ξ0,r)、0<r<ρ，则

\[
\frac{\|Tz_r-p\|}{\|z_r-p\|}\ge A_0 r^{\gamma-1}\longrightarrow\infty.
\tag{AB4}
\]

任意 α∈(0,1)、任意有限 ε≥0 的标准 almost-averaged 平方界在固定点 p 上都会给 ||Tz−p||²≤(1+ε)||z−p||²，因为被减去的步项非负。这与 AB4 冲突。故在包含一整条 z_r→p 正常序列的输入域上，不能给 T 在 p 的任何有限 violation 的 almost-averaged 证书；特别适用于二维开邻域，或完整正半窗在其自身拓扑中的 p 邻域。任意更薄相对域并不在排除范围，例如仅取 Λ=S 时 T=Id，恰为 averaged。这比“所选 Hölder 上界的比率发散”强，是实际映射的必要门失败。

该障碍在双 Lipschitz 动态共轭下保持。具体地，设 H0 在包含 p、z_r、Tz_r 的同一相对邻域为单射且

\[
m\|x-y\|\le\|H_0x-H_0y\|\le M\|x-y\|,
\quad0<m\le M<\infty.
\]

定义 T'=H0 T H0^{-1}、p'=H0p。则

\[
\frac{\|T'H_0z_r-p'\|}{\|H_0z_r-p'\|}
\ge\frac mM A_0 r^{\gamma-1}\longrightarrow\infty.
\tag{AB5}
\]

所以 T' 仍无上述证书。换等价 Hilbert 范数是此结论的特例。只删负支仍保留这些正输入，AB4 仍成立；但换成另一种 warped 更新或允许额外核和选支，不是本页同映射共轭合同，不能据 AB5 排除。C215 的 homeomorphism 不为 Lipschitz，因而其线性共轭与此结论无冲突。

**范围。** 源 Theorem 2.18 的 almost-averaged 条件在整管 S_{γ^iδ} 上，gauge 只在相应环域；仅在离零点有正距离的环上取有限局部斜率，没有关闭整管门。AB4/AB5 排除上述直接导入合同，但既非对所有 LMZ/KL 目标函数表示的反例，也非任意改写 GPPA 的分离定理，更非全球首创认证。

<a id="gab-checks"></a>
## 证据与独立审查门

一般结论由 AB1–AB5 的完整推导承担。确定性 Fraction 枚举和输入趋零边界见 [复算脚本](../code/gppa_novelty/almost_averaged_check.py)；有限计算不证明极限或首创。新颖性对照的实际阅读范围与仍未闭接口见 [本轮总报告](../novelty/2026_10_09/README.md)。独立审查已关闭薄域量词异议，审查范围和最终状态以 CLAIMS.md 的 C218 身份卡为准。
