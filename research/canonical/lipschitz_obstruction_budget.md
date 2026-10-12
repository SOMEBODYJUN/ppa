# 给定方向延拓后的 Lipschitz–Hölder 预算桥

本页接续 [C234](zero_preserving_completion.md#zpc-rp2) 与 [C240](completion_budget_gate.md#cbg-certificate)。它不声称解决 RP² 的原预算端点；它把 Hopf 的无零方向延拓和可量化的 Hölder 预算分开，并给出一个可直接审计的上界接口。

<a id="lob-object"></a>
## C245-v1 · 给定 Lipschitz 无零方向延拓时的预算上界

固定 C233 的共享对象，且 \(W=\overline B_R\setminus\operatorname{int}N_\rho\) 连通、\(0<\gamma<1\)。本引理另假定 \(D_0\)（等价地 \(C_0\)）在 \(N_\rho\) 上 Lipschitz，使内边界方向数据有有限 Lipschitz 常数；C234 的光滑 RP² 管满足这一附加条件。令
\[
D_0=\operatorname{Id}-T_0\quad\text{on }N_\rho,
\]
并在边界上定义
\[
g=\frac{D_0}{\|D_0\|}\quad(\partial N_\rho),\qquad
g(p)=p/R\quad(\partial B_R).
\]
假定给定一个 Lipschitz 延拓 \(e:W\to S^{n-1}\) 满足 \(e|_{\partial W}=g\)，其常数为 \(K_e\)；再给定一个正 Lipschitz 函数 \(a:W\to(0,\infty)\)，满足 \(a=\|D_0\|\) 于内边界、\(a=R/2\) 于外边界，且常数为 \(K_a\)，上界为 \(A\)。令 \(D=ae\)。

则存在全域连续、紧支撑的 \(\widehat C\)，保存整个 \(C_0\)，且
\[
\operatorname{Fix}\frac{\operatorname{Id}+\widehat C}{2}=M,
\qquad
[\widehat C]_{\gamma}\le (2R)^{1-\gamma}G_W
\max\{K_{C_0},\,1+2(K_a+A K_e)\},
\tag{LB1}
\]
其中 \(G_W<\infty\) 定义为以下固定拼接引理的常数：对分别定义在 \(N_\rho\)、\(W\) 和 \(\mathbb R^n\setminus B_R\) 上、在公共边界取相同迹的 Lipschitz 函数，三块拼接后的全域 Lipschitz 常数不超过 \(G_W\) 乘各块常数的最大值。给定本管和球的光滑边界，取有限个统一法向 collar 及其双 Lipschitz 坐标，这样的 \(G_W\) 有限且只依赖几何接缝，不依赖 \(e,a\)。
其中 \(K_{C_0}\) 是 \(C_0\) 在 \(N_\rho\) 上的 Lipschitz 常数。外部定义为
\[
\widehat C(p)=
\begin{cases}
C_0(p),&p\in N_\rho,\\
p-2a(p)e(p),&p\in W,\\
0,&p\notin B_R.
\end{cases}
\tag{LB2}
\]

**证明。** 在内边界 \(D=D_0\)，在外边界 \(D=p/2\)，所以 (LB2) 在两条接缝上连续。管内 \(\operatorname{Id}-\widehat T=D_0\) 只在 \(M\) 为零；管外 \(D=ae\) 且 \(a>0\)，无零点；球外 \(\operatorname{Id}-\widehat T=p/2\)，也无零点。于是固定点恰为 \(M\)。

由 \(e\) 为单位值，\(D=ae\) 的 Lipschitz 常数不超过 \(K_a+A K_e\)。因此球内外部段 \(p-2D\) 的常数不超过 \(1+2(K_a+A K_e)\)。三个闭段在光滑边界上取相同迹；由上面定义的有限拼接引理，得到全域 Lipschitz 常数不超过上式乘以 \(G_W\)，记为 \(K\)。若两点都在 \(\overline B_R\)，则 \(d=\|x-y\|\le2R\)，从而
\[
\|\widehat C(x)-\widehat C(y)\|
\le Kd\le K(2R)^{1-\gamma}d^\gamma.
\]
若一端在球外且 \(d>2R\)，沿接缝的相同迹和 collar 估计给 \(\|\widehat C(x)-\widehat C(y)\|\le KR\le K(2R)^{1-\gamma}d^\gamma\)；两端都在球外时差为零。若一端在球外且 \(d\le2R\)，直接用全域 Lipschitz 界即可。得 (LB1)。

<a id="lob-rp2"></a>
## RP² 压力测试的可审计参数

对 C234 的 \(\rho=1/8\)、\(R=2\)、\(\gamma=1/2\) 数据，投影谱隙至少为
\[
1-2\rho=\frac34.
\]
对距离小于谱隙一半的点对用 Davis–Kahan 的局部投影界，对距离较大的点对用投影范数的平凡界，可取保守的全域管上界 \(K_\Pi\le4/(1-2\rho)=16/3\)。在整管上
\[
K_{D_0}\le(1+\rho^2)(1+K_\Pi)=\frac{1235}{192},
\quad
K_{C_0}\le1+2K_{D_0}=\frac{1331}{96},
\quad
a_{\rm in}=(1-\rho^2)\rho=\frac{63}{512}.
\]
若选择一个取值于 \([0,1]\) 的 \(K_\tau\)-Lipschitz 标量接缝函数 \(\tau\)（内边界值 0、外边界值 1），取
\[
a=(1-\tau)a_{\rm in}+\tau,
\quad K_a\le\frac{449}{512}K_\tau,
\quad A=1,
\]
则任意可核验的方向延拓常数 \(K_e\) 给出
\[
[\widehat C]_{1/2}
\le 2G_W\max\left\{\frac{1331}{96},
1+2K_e+\frac{449}{256}K_\tau\right\}.
\tag{LB3}
\]
这把 RP² 的“预算是否有限”降为两个可审计对象：球值边界方向的 Lipschitz 延拓常数 \(K_e\)，以及一个标量接缝函数的常数 \(K_\tau\)。Hopf 只给方向延拓存在；若要得到数值预算，仍须给出具体延拓或其网格证书。

**状态边界。** C245 是条件的 `derived-checked` 引理：它不证明原预算 \(L_*=L_0\)，不提供 \(K_e\) 的最优值，也不把连续 Hopf 延拓自动称为可计算算法。它的价值是为 C240 的健壮证书提供一个明确的上界输入，并排除“拓扑存在但预算完全不可量化”这一含混表述。


## 欧氏拼接因子的后续证据改进

[C264支持粘接引理](rp2_explicit_completion.md#rec-gluing)已证明：本页各块若按前提均为欧氏全对 Lipschitz，并有一致迹，其有限闭覆盖拼接可直接取G_W=1。此取值符合LB1原有合同；无需依赖光滑collar几何。C258的G_T用于从单纯形内部导数转到欧氏界，不能因此删除。另[C265](rp2_explicit_completion.md#rec-exact-budget)给原RP²管C0的精确Lipschitz及半阶常数；原保守LB3仍有效。实际方向场已由[C264](rp2_explicit_completion.md#rec-construction)构造，最优预算继续开放。
