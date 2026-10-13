# 双稳态关联记忆网络：六个记忆态推断至少五个未见平衡

状态：最终备选二。只做第四章筛选，未改主稿、摘要或编号。

一手来源是 McGraw–Menzinger, *Bistable Gradient Networks in the Thermodynamic Limit*, arXiv:cond-mat/0203568v1；正式对应 Phys. Rev. E 67, 016118 (2003)，DOI [10.1103/PhysRevE.67.016118](https://doi.org/10.1103/PhysRevE.67.016118)。[原文 PDF](https://arxiv.org/pdf/cond-mat/0203568)。Eq.(2) 的能量为

\[
\Phi(u)=\sum_i(u_i^4/4-u_i^2/2)-\frac\gamma2u^TWu-b^Tu,
\]

Eq.(6) 为零对角 Hebb coupling W=(ΞΞ^T−pI)/N，Eq.(1)/(4) 研究连续 gradient dynamics。本文的 ordinary critical PPA 是本轮另选算法，不是来源声称已有的 PPA 定理。来源主要考察 thermodynamic/low-loading 及几类 attractors，没有给本轮 finite heterogeneous-bias instance 的完整 stationary coordinates。

## 1 固定数据

N=8，取三个正交 ±1 memory patterns

\[
\begin{aligned}
s&=(1,1,1,1,1,1,1,1),\\
t&=(1,1,1,1,-1,-1,-1,-1),\\
r&=(1,1,-1,-1,1,1,-1,-1),
\end{aligned}
\]

Ξ=[s,t,r]，W=(ΞΞ^T−3I)/8，γ=3/10，

\[
b=(-7,4,2,-3,6,-5,1,8)/1000,
\quad F(u)=u^{\odot3}-u-\gamma Wu-b,
\quad v=I,
\quad\lambda=16/19.
\]

全部 off-diagonal W_ij 为 ±1/8 或 3/8，均非零，故是 dense coupling。P=ΞΞ^T/8 是到 span(s,t,r) 的 orthogonal projector：

\[
W=P-3I/8,
\quad\sigma(W)=\{5/8\;(3\text{次}),-3/8\;(5\text{次})\}.
\]

λ 正是全域 convexification 的临界步长，而非随意小 λ。

## 2 完整 proximal：全部 fibers、critical 与非 Lipschitz

写

\[
H_\lambda(u)=u+\lambda F(u)
=\lambda u^{\odot3}+Bu-\lambda b,
\quad B=(1-\lambda)I-\lambda\gamma W
=\frac{24}{95}(I-P)\succeq0.
\]

这是严格凸 coercive 函数

\[
\lambda\sum_i u_i^4/4+\tfrac12u^TBu-\lambda b^Tu
\]

的梯度。逐坐标 cubic strictly monotone、B positive semidefinite，故 H_λ strictly monotone；对每个 input x，减去 x^Tu 后的势仍 coercive 且 strictly convex，因此有且仅有 stationary root。H_λ 是 proper continuous bijection，故 homeomorphism。完整关系 T=H_λ^{-1} 同时为唯一 global argmin proximal，不含删分支步骤。

令 x_*=-λb。因为 Bs=0，

\[
T(x_*+\lambda\tau^3s)=\tau s.
\]

故 T 在 x_* 非 Lipschitz，指数 1/3 在此方向上不能提高。这是 input x_* 的非 Lipschitz；F(0)=−b≠0，所以该点不在本轮六个 minimum 的局部认证管中。

对任意 λ>16/19，B_λ 在 memory span 上有负 eigenvalue。在同一 input x_*=-λb，完整 proximal fiber 至少包含

\[
0,\quad\pm\sqrt{19/16-1/\lambda}\,s,
\quad\pm\sqrt{19/16-1/\lambda}\,t,
\quad\pm\sqrt{19/16-1/\lambda}\,r.
\]

这些是七个 distinct stationary outputs；故 critical λ 上的完整单值性不能扩成 λ>critical。

另外，cubic monotonicity 给全域

\[
\|T(x)-T(z)\|\le38^{1/3}\|x-z\|^{1/3}.
\]

但 C=2T−I 在无穷远有线性 −I 项，**不能直接满足现行 C254 的全尺度 sublinear reflected-Hölder 前件**。下文使用独立的大 cube index bridge。

## 3 六个真实 minimum 的解析证书

令 a=√19/4，p_0 依次取 ±as,±at,±ar。b=0 时 F_0(p_0)=0。使用

\[
217/200<a<109/100
\]

以及 W 的精确 spectrum，在每个 B_{1/20}(p_0) 上均有

\[
2I\preceq DF(u)\preceq(13/4)I.
\]

下界的直接粗估为 3(217/200−1/20)^2−19/16>2；上界为 3(109/100+1/20)^2−71/80<13/4。

由于 ||b||=√204/1000<3/200，在半径 ε=1/100 的球边界上

\[
\langle F(z),z-p_0\rangle
\ge2\varepsilon^2-\|b\|\varepsilon>0.
\]

Φ 在该闭球有 minimum；边界向外 gradient 正，minimum 必在内部，因而 F(p)=0。Hessian 下界给球内唯一 root，且

\[
\|p-p_0\|\le\|b\|/2<3/400.
\]

六个球互不相交，故得到六个 distinct actual minima p_j。它们仍具有指定六个 memory sign patterns；不宣称它们是全部 local minima 或 global minima。这个证书只证明六个小球，不需要枚举其余 roots，也不把 floating centers 冒充 exact roots。

## 4 同一元组的完整 RLEB、true EB、留域

令 M={p_1,…,p_6}，U=∪_j B_{3/100}(p_j)，R=1/100。用同一个参数元组

\[
\lambda=16/19,\quad a(t)=t,\quad\omega(t)=t/2,
\quad h(t,s)=s,\quad\psi(t)=t/2,
\quad\bar t=1,\quad\kappa=1/2.
\]

先认证实际输出。B_{1/25}(p_j) 包含于 B_{1/20}(p_{0,j})，故其上 DH_λ≽(51/19)I。H_λ 的全域 monotonicity 与射线 barrier 说明：||x−p_j||<3/100 时，唯一 y=T(x) 必在 B_{1/25}(p_j)。随后积分同一个 Hessian 下界给

\[
\|y-p_j\|\le(19/51)\|x-p_j\|.
\]

因此全部输入/全部完整输出已先验进入证书窗；没有用待证留域来调用局部 EB。

在该窗上 DT=(I+λDF)^{-1}，reflected derivative spectrum 是 (1−λh)/(1+λh)，h∈[2,13/4]，故 norm≤33/71<1/2。积分给同一物理最近锚

\[
\|2T(x)-x-p_j\|\le\tfrac12\|x-p_j\|.
\]

完整 F 为 single-valued，r_F(y)=||F(y)||。同一球内强 monotonicity 给

\[
d(y,M)=\|y-p_j\|\le\tfrac12\|F(y)\|.
\]

物理 step 就是 kernel increment。于是 K(t)=3t/4，

\[
K(R)/\lambda=57/6400<1,
\quad\psi(K(t)/\lambda)=57t/128<\tfrac12t,
\quad\Theta(t)=\tfrac32t.
\]

对每个 x∈U、d(x,M)≤R，有

\[
\Theta(d(x,M))\le3/200<1/50
\le d(x,U^c).
\]

所以 C249 的全部合取对完整关系、共同常数与所有允许初值成立；给全部轨道的留管、距离≤2^{-k}d_0、总长≤3d_0/2、相同 geometric tail。也可从直接 contraction 得到更小距离 factor 19/51；不把 C249 元组的 κ=1/2 称为尖率。

## 5 Cube、全局总 index 与管外缺额

设 m=||y||_∞，取达到最大绝对值的坐标。B_ii=3/19，Σ_{j≠i}|B_ij|=27/95。因此

\[
\|H_\lambda(y)\|_\infty+\lambda\|b\|_\infty
\ge\lambda m^3-12m/95.
\]

若 ||x||_∞≤2 而 y=T(x)，m≥2 会使右边至少 616/95>2+λ·8/1000，矛盾。故 T 将闭 cube [-2,2]^8 严格映入其内部。对 fixed point y=x，得到 m^3−(107/80)m≤8/1000；该表达式在 m≥2 严格增加，故 cube 外没有 fixed point（事实上 m<29/25）。

Cube 是 compact ENR，T 的总 index 为1。六个严格吸引小闭球分别与 singleton root 同伦等价，局部 index 各+1，总 i(T,M)=χ(M)=6。通过与 canonical C231 相同的 compact-ENR normalization、commutativity/localization 和 additivity，管外剩余 root cluster 有总 index

\[
1-6=-5.
\]

这里没有直接调用 C254 的失效 reflected-growth 前件，也没有对核换空间。

## 6 全球非退化与数量

在 R=Z_(3) 上，γ=3/10≡0，bias denominator 1000 为 unit，故

\[
DF(u)=3\operatorname{diag}(u_i^2)-I-\gamma W
\equiv-I\pmod3.
\]

[共同模3附页](graph_quartic_modular_certificate.md)的 finite-free argument 给全部 complex roots 非退化，恰3^8=6561个 simple complex roots。所有 real roots 有 ±1 local index。因此缺额 −5 强制至少五个未进入六个认证管的 distinct real roots；未知 root 数为奇数，总 real root 数至少11且为奇数。它们位于 [-2,2]^8\N_{3/100}(M)，不要求辨认其坐标。

在这些 fixed points 上 DH_λ 还可独立证为正定。其 kernel vector 必须属于 span(s,t,r)，并且只能支持在 u_i=0 的坐标。该 span 的 vector 在每种相同 pattern-row 的两节点上取相同值；而同组的 b_i 不相同，故同组两个 u_i 不可能同时为零（代入两个 F_i=0 并相减即与 b_i≠b_j 矛盾）。因此 kernel vector 在四组上都为零，DH_λ 正定。于是 local index 是 sign det DF，因为 det(I−DT)=λ^8 det DF/det DH_λ，分母正。还可绕过微分公式：H_λ 是 orientation-preserving monotone homeomorphism，(I−T)∘H_λ=λF，所以 fixed-point local index 等于 F 的 Brouwer degree。这条后一接口也适用于 H_λ 退化的其它数据。

经典 Morse 可额外断言至少五个 Morse index1 saddles；无须排其坐标。

## 7 实际计算与边界

六次 deterministic scipy.root，从 ±a memory patterns 起步，最大全欧氏 residual 1.84×10^{-14}；root shift 在 .00547–.00550；DF 的最低 observed eigenvalue 在2.3648–2.3760。它们是解析证书的数值复核，不是六根存在/唯一性或 global nondeg 的依据。没有运行 6561-path enumeration。

该 network 是自然关联记忆模型，但有限 N=8 与三个正交 patterns 保留了结构：有四种相同 pattern-row，每种两 nodes；W 为 rank3 perturbation of a diagonal matrix。forcing 在每个 pair 内不相等，破坏 exact group equality，所以不像二-pattern 版变成两个独立4-node systems。不过可引入三个 overlap q=Ξ^Tu，逐 node 解带 q 的 scalar cubic，形成低维 self-consistency 加 branch choices。**没有证明这比所有 root methods 更难，也不能把6561作为最优成本下界。** 扩大 N、loading、generic patterns 需要另做 instance 与 constants 认证。

λ=critical 保留全域非 Lipschitz full prox；附近 minima 的局部算法是 smooth/Lipschitz，classic local contraction/implicit function 可直接分析。原 Φ polynomial/coercive，完整 stationary prox 恰唯一 global argmin，故经典 ABS 的 H1/H2/H3/KL 也给同一算法的全域 finite length。因而该备选不能承载“旧收敛工具失效”的论点。它可以承载 `few certified memories + reusable proximal certificate ⇒ 未探测 equilibria/saddles 的 index/count/location`。


## 完整零集、准入表及交付范围

完整 S= {u∈R⁸:F(u)=0}，不是已认证的六个记忆态 M。上述全根非退化给 S 有限，但未求全部实零坐标。作为梯度模型，这里的零点为一般驻点；只有六个证书点被证明是严格局部极小，未称为全局最优。

| 门 | 裁决 |
|---|---|
| 自然模型/关联记忆来源 | 通过，有限确定参数为本轮实例 |
| 全输入、全部纤维与输出存在 | 通过，严格凸强制完整驻点prox=global-min prox |
| 目标隔离/最近锚 | 通过，六个彼此分离解析根球 |
| 完整反射、真残差 EB | 通过，相同物理锚和同窗 |
| 直接 C249 兼容/可和留域 | 通过，上述同元组 |
| C254 原全尺度反射门 | 失败，独立cube入口 |
| 全部 DF 与 DH 非退化 | 通过，模3商环与异质pair核排除分别证明 |
| 数量与未知点位置 | 通过，至少5点、奇数、净index−5；坐标/完整分类未核 |
| 与经典区别 | ABS和Morse正面适用，不承载旧理论不行的声称 |
| 任意度量 | 未核，只固定Id；不得自动改变核 |

主要证明约2页，承重步骤为临界完整凸化、六球存在、mod3引理。代码 [verify.py](../code/bistable_memory_zero_inference/verify.py) 和 [results.json](../code/bistable_memory_zero_inference/results.json) 中有限反算仅作诊断。
