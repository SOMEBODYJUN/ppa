# 固定核 GPPA 的物理指数、核差次数与值域

<a id="gpi-index"></a>

## 对象与结论

在 \(\mathbb R^n\) 中取 \(\lambda>0\)、关系 \(F:\mathbb R^n\rightrightarrows\mathbb R^n\)、核 \(v:\mathbb R^n\to\mathbb R^n\) 和非空紧集 \(M\subset F^{-1}(0)\)。令 \(d(x)=d(x,M)\)。设 \(U\) 是含 \(M\) 的开集、\(R>0\)，且完整关系
\[
J_{\lambda F}^v(x)=\{y:v(x)-v(y)\in\lambda F(y)\}
\]
在 \(U_R=\{x\in U:d(x)\le R\}\) 上单值、连续，记为 \(T\)。假设存在 \(0<\kappa<1\) 使 \(d(Tx)\le\kappa d(x)\) 对 \(x\in U_R\) 成立。完整性给出 \(\operatorname{Fix}T=F^{-1}(0)\cap U_R\)（固定点集合取在 \(U_R\) 上）。现行稿的 G1–G5 是上述一步收缩的充分条件。以下的局部指数只需要一步距离收缩。

**命题 1（任意紧零簇的物理局部指数）。** 存在包含 \(M\) 的有界开集 \(V\)、\(\overline V\subset U_R\)，使 \(F^{-1}(0)\cap\overline V=M\)。\(M\) 的有理 Čech 上同调各阶有限维、仅有限多个阶非零，且
\[
\operatorname{ind}(T,V)
=\deg(\operatorname{Id}-T,V,0)
=\sum_{j\ge0}(-1)^j\dim_{\mathbb Q}\check H^j(M;\mathbb Q)
=:\chi_{\check H}(M).
\]
当 \(M\) 是紧 ENR，右端即通常 Euler 示性数。现行稿的 G1–G5 确保对足够小的闭邻域有统一物理长度尾，此时 \(M\) 还是紧 ENR。若 \(T\) 另在包含 \(\overline V\) 的有界开集 \(\Omega\) 的闭包上连续、单值，满足同一完整近端关系，且 \(\partial\Omega\) 上无固定点，则
\[
\operatorname{ind}(T,\Omega\setminus\overline V)
=\operatorname{ind}(T,\Omega)-\chi_{\check H}(M).
\]
若右端非零，\(\Omega\setminus\overline V\) 必含 \(F\) 的一个零点。

**不变紧邻域。** 取 \(0<a<b<b'<R\)，使 \(\kappa b'<a\) 且闭 \(b'\)-管处于 \(U\)。以小网格选取与闭 \(a\)-管相交的全部闭网格立方体，令其并为 \(N\)。网格直径小于 \(b-a\)，所以
\[
\{d\le a\}\subset\operatorname{int}N\subset N\subset\{d<b\}.
\]
第一包含可逐点核对：对 \(p\in\{d\le a\}\)，所有含 \(p\) 的网格立方体均被选中，这些立方体的并包括 \(p\) 的一个开邻域。有限格子可正规三角剖分，故 \(N\) 是紧多面体和 ENR。令 \(V=\operatorname{int}N\)。每个闭立方体是其内部的闭包，故 \(\overline V=N\)。令 \(W=\{d<b'\}\)。对 \(x\in W\) 有 \(Tx\in\{d<a\}\subset V\)。每个 \(M\) 中的点均为 \(T\) 的固定点，其余 \(W\) 中的点由严格收缩排除。

**G1–G5 下的直接计算。** 一步位移上界为 \(H_v(d(x))\)。在 \(N\) 上迭代求和得到
\[
\sup_{x\in N}\|T^kx-P(x)\|\le
\sum_{j=k}^{\infty}H_v(\kappa^j b)\longrightarrow0,
\quad P(x):=\lim_{k\to\infty}T^kx\in M .
\]
同理在 \(W\) 上定义 \(P\)。因此 \(P\) 连续、\(P|_M=\operatorname{Id}\)、\(PT=P\)，且 \(M\) 是欧氏开邻域的回缩。

记 \(i:M\hookrightarrow N\)。取足够大 \(m\)，使 \(T^m(x)\) 与 \(P(x)\) 的距离一致小于 \(d(M,N^c)>0\)。连接 \(T^m(x)\) 和 \(P(x)\) 的整个线段在 \(N\) 内，故 \(T^m|_N\) 与 \(iP\) 在 \(N\) 中同伦。对每阶有理奇异同调，
\[
H_j(N)=\operatorname{im}i_*\oplus\ker P_* .
\]
因 \(T i=i\) 和 \(P T=P\)，两个直和项各自不变，第一项上 \(T_*=\operatorname{Id}\)，第二项上 \((T_*)^m=0\)。故 \(\operatorname{tr}(T_*|H_j(N))=\dim H_j(M)\)，\(L(T|_N)=\chi(M)\)。

**仅有一步距离收缩时。** 令 \(N_k=T^k(N)\)。这些嵌套紧集满足 \(\bigcap_k N_k=M\)：\(T|_M=\operatorname{Id}\) 给出一个包含，而 \(d(z,M)\le\kappa^k b\) 对所有 \(z\in N_k\) 给出另一个。令 \(A^j=\check H^j(N;\mathbb Q)\)、\(B^j=\check H^j(M;\mathbb Q)\)、\(u=T^*:A^j\to A^j\)、\(i^*:A^j\to B^j\)。\(A^j\) 有限维，且 \(i^*u=i^*\)。下证 \(i^*\) 将 \(u\) 的稳定像 \(E^j=\bigcap_{m\ge0}\operatorname{im}u^m\) 同构到 \(B^j\)。

若 \(\alpha\in A^j\) 且 \(i^*\alpha=0\)，嵌套紧集的 Čech 上同调连续性给出某个 \(k\)，使 \(\alpha|_{N_k}=0\)。因 \(T^k:N\to N_k\)，有 \(u^k\alpha=0\)。又因有限维，\(u\) 在 \(E^j\) 上可逆，故 \(i^*|_{E^j}\) 单射。另一方面，每个 \(\beta\in B^j\) 由某个 \(\check H^j(N_k;\mathbb Q)\) 上的类 \(\beta_k\) 代表。经 \(T^k:N\to N_k\) 拉回 \(\beta_k\) 得 \(\alpha\)，因 \(T^k|_M=\operatorname{Id}\)，有 \(i^*\alpha=\beta\)。对充分大 \(m\)，\(u^m\alpha\in E^j\) 且仍限制为 \(\beta\)。于是 \(i^*|_{E^j}\) 同构，\(i^*u=i^*\) 又说明 \(u|_{E^j}=\operatorname{Id}\)。有限维 Fitting 分解的其余项上 \(u\) 幂零，故 \(\operatorname{tr}u=\dim B^j\)。有限多面体的 Čech 与奇异上同调一致，有理上、下同调的自映射互为对偶，故得到相同 Lefschetz 数。

**环境空间中的次数。** 设 \(f=T|_W:W\to N\)、\(g:N\hookrightarrow\mathbb R^n\) 为包含映射。\(W\subset\mathbb R^n\) 是开集，\(N\) 作为自身空间也是开集。\(gf:W\to\mathbb R^n\) 与 \(fg:N\to N\) 的固定点集均为同一个紧集 \(M\)。固定点指数的交换性给出 \(I_{\mathbb R^n}(T|_W)=I_N(T|_N)\)，紧 ENR 归一化给出 \(I_N(T|_N)=L(T|_N)\)。欧氏环境指数对应 Brouwer 次数，局部化去掉 \(W\setminus V\)，故等式成立。全局差额由可加性得到。

<a id="gpi-forcing"></a>

**命题 2（核差桥与扰动余量）。** 沿用命题 1，若 \(v\) 在 \(\overline V\cup T(\overline V)\) 上连续，定义 \(D_v(x)=v(x)-v(Tx)\)。额外要求对每个 \(x\in\partial V\)，
\[
D_v(x)\ne0,\qquad
\langle D_v(x),x-Tx\rangle\ge0 .
\]
则 \(\deg(D_v,V,0)=\chi_{\check H}(M)\)。若该值非零，设 \(\eta=\min_{\partial V}\|D_v(x)\|>0\)，则
\[
B(0,\eta/\lambda)\subset F(T(V)).
\]
更一般地，每个在 \(T(\overline V)\) 上连续且满足 \(\lambda\|f\|_\infty<\eta\) 的扰动 \(f\)，都有某个 \(y\in T(V)\) 满足 \(f(y)\in F(y)\)。证明是从 \(\operatorname{Id}-T\) 到 \(D_v\) 作线段同伦。端点均无边界零点，内点因这两个非零向量的内积非负也无边界零点。再对 \(D_v(x)-\lambda f(Tx)\) 作扰动同伦，边界余量使次数保持非零，给出 \(x\in V\) 令 \(D_v(x)=\lambda f(Tx)\)。完整近端包含给出 \(f(Tx)\in F(Tx)\)。取常值 \(f\) 得值域球。严格单调核在每对实际边界输入和输出上自动给出两项条件。单调性本身给出内积条件。

<a id="gpi-obstruction"></a>

**反例（相同的核与完整物理迭代，原值域不同）。** 在 \(\mathbb R^2\) 取 \(\lambda=1\)、\(v(x_1,x_2)=(x_1,0)\)。比较 \(F_+(y_1,y_2)=(y_1,y_2)\) 和 \(F_-(y_1,y_2)=(y_1,y_2^2)\)。各自的完整广义近端方程第一分量给 \(y_1=x_1/2\)，第二分量分别给 \(y_2=0\) 或 \(y_2^2=0\)，故都得到 \(T(x)=(x_1/2,0)\) 和 \(M=\{0\}\)。

对两关系，取任意 \(R>0\)、\(U=\mathbb R^2\)、\(a(t)=t\)、\(\omega_v=0\)、\(\psi(s)=s\)、\(\kappa=1/2\)、\(h(t,s)=3t/2\) 和 \(\bar t\ge R/2\)。最近锚固定为 \(p=0\)，\(\delta=|x_1|\le d(x)\)，且 G2 的内积恰等于 \(\delta^2/4\)。每个完整输出都满足 \(r_{F_\pm}(Tx)=\|Tx\|=d(Tx)\)，而 \(\|x-Tx\|\le\|x\|\le h(d(x),s_v)\)。因此 G1–G5 均成立，\(\Theta_v(R)=3R\)。物理指数为 \(+1\)，也可由 \(\operatorname{Id}-T=\operatorname{diag}(1/2,1)\) 直接求出。核差却是 \(D_v(x)=(x_1/2,0)\)，沿整条竖轴为零，任何围住原点的有界邻域边界均与该轴相交。\(F_+(\mathbb R^2)=\mathbb R^2\)，而 \(F_-(\mathbb R^2)=\mathbb R\times[0,\infty)\)。因此即使在相同核、相同完整映射、相同真残差输出估计和相同正指数下，后者也没有任何以零为中心的值域球。

**边界核差无零仍可能有零次数。** 固定 \(\lambda=1\)、\(v(x)=(\|x\|^2,0)\)，取光滑函数 \(\varphi(t)=0\)（\(t\ge0\)）、\(\varphi(t)=e^{-1/t^2}\)（\(t<0\)），并令
\[
F(y_1,y_2)=(y_1^2,y_2^2+\varphi(y_1)).
\]
第二个近端方程强制 \(y_2=0,\,y_1\ge0\)，第一个方程再给完整连续单值 \(T(x)=(\|x\|/\sqrt2,0)\)，且 \(M=\{0\}\)。取 \(t=d(x)=\|x\|\)、\(a(t)=t^2\)、\(\omega_v=0\)、\(\psi(s)=\sqrt s\)、\(\kappa=1/\sqrt2\)、\(h(t,s)=(1+\kappa)t\) 和 \(\bar t\ge R^2/2\)。核锚的内积等于 \(t^4/4\)，\(K_v(t)=t^2/2=r_F(Tx)\)，\(d(Tx)=\kappa t=\psi(K_v(t))\)，而三角不等式给 (G3)，所以 G1–G5 成立。物理指数为 \(+1\)。核差 \(D_v(x)=(\|x\|^2/2,0)\) 的零点恰为原点，但在任何含原点的有界开邻域内按边界正余量将目标微移出水平轴可见 \(\deg(D_v,V,0)=0\)。例如 \(x=(-r,0)\) 时核差与物理位移的内积为负。\(F\) 同样没有包含原点的值域球，因为第一分量始终非负。故边界核差无零这个条件单独不足以继承物理次数。

## 来源与稿件位置

- 当前主稿的「发表成果整理/RLEB/sections/topological_obstruction.tex」第 159–207 行在完整普通 PPA 下用光滑管。「sections/conclusion.tex」第 27–33 行明确提出一般非线性核的物理指数问题。「research/canonical/topological_completion_balance.md」第 128–139 行将一般 ENR、明确构造不变紧邻域和非单射物理回代列为未覆盖范围。「research/canonical/physical_rleb_gppa.md」第 291–314 行含上面的 \(F_+\) 基线和无物理控制的振荡例。
- 归一化、交换性、局部化与可加性使用 Benjamin–Gottlieb, *Fixed Point Indices and Manifolds with Collars*, §2.1.1、§2.1.2、§2.1.4、§2.1.6，原文 PDF 第 3–4 页。[作者原文](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf)
- Čech 连续性见 Wendl, *Topology III*, Theorem 43.25（引 Eilenberg–Steenrod，第 X 章）。这里所有 \(N_k\) 紧，包含构成逆序列，逆极限等于交集。[课程讲义原文](https://www2.mathematik.hu-berlin.de/~wendl/Sommer2025/Topologie3/lecturenotes.pdf)
- 已知动力系统先行。Richeson–Wiseman, *A Fixed Point Theorem for Bounded Dynamical Systems*, arXiv:math/0108064v2，第 2–3 页在全域有界轨道情形，用迭代经过可缩球得出高阶同调作用幂零及 Lefschetz 数为 1。Hirsch, *Topology of Fixed Point Sets of Surface Homeomorphisms*, Proposition 3.1，对保向曲面同胚吸引子建立 Čech Betti 数有限与吸引盆域的 Čech 上同调同构。这里需要比较的是完整 GPPA 下点态固定零簇的稳定像计算，以及物理次数到原关系取值的条件桥和反例。[Richeson–Wiseman 原文](https://arxiv.org/pdf/math/0108064) [Hirsch 刊本](https://www.math.uh.edu/~hjm/pdf26%284%29/09hirsch.pdf)
- 最直接的先行是 Hernández-Corbato–Ruiz del Portal–Sánchez-Gabites, *Infinite series in cohomology: attractors and Conley index*, Corollary 5，印页 5，2020 刊本 DOI 10.1007/s00209-019-02318-5。对流形上连续映射的渐近稳定吸引子，若它是 Čech 上同调有限生成的孤立不变连续统，原文已经给出局部指数等于限制映射的 Čech Lefschetz 数。取限制映射为恒等即为 Euler 示性数。在本命题的严格收缩设定中，稳定像另外证明有理同调有限维并允许不连通紧集。单值物理指数应定位为对已有动力系统原理的 GPPA 应用。进一步的价值要看原值域桥、纤维反例和完整多值版本。[作者原文](https://arxiv.org/pdf/1802.02521)
- 命题 2 是 GPPA 原方程上的次数接口。已有 C05-v2 则在普通 PPA 中使用经过单独核定的有限样本配领、Vietoris 跨度和 Lefschetz 数来证明扰动值域，两者的近端算法及前件不同。仓库文件为「research/canonical/local_range_without_supercriticality.md」第 12–67 行。
- 以上证明调用经典固定点指数、Čech 连续性和 Brouwer 次数。内部新增点是对同一完整物理 GPPA 的严格吸引、核差同伦和不可推广边界的拼接。公开文献中的精确先行性仍需查核。可将命题 1 的 G1–G5 直接证明、命题 2 和匹配反例合并进现行稿第 4 节，Čech 加强可独立呈现。

- Hernández-Corbato–Ruiz del Portal–Sánchez-Gabites [2018 预印本](https://arxiv.org/pdf/1802.02521) Corollary 5 对有限生成 Čech 上同调的孤立不变 continuum 给 Lefschetz 型指标关系，吸引情形恢复限制映射的 Lefschetz 数。本文在完整 GPPA 假设下直接建立有限秩，另外连接核差及原值域。
