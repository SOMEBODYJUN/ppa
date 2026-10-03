# 非孤立零集：输出锚、漂移与同序列锐性

本页重新审读 9/01 RL_foundations §8–§9.1；这里的结论是指定近端分支上的**距离上界及条件锐性**，不是完整多值关系的所有轨道定理。数学证据是下列逐点三角估计和量词检查；外部新颖性未核。

<a id="na-object"></a>
## NA-OBJECT · 同一输入家族上的两个最近点集合

取实 Hilbert 空间 H、非空 \(S\subset F^{-1}(0)\)、\(\lambda>0\)、指定单值 \(J:D\to H\)，每个 \(x\in D\) 有 \(y=Jx,\ w=(x-y)/\lambda\in F(y)\)。固定 \(U\subset D,r_0>0\)，研究
\[
\mathcal X_{r_0}=\{x\in U:0<r_x=d(x,S)\le r_0\}.
\]
本节 exact-profile 版本对**该家族的每个** x 假设 \(P_S(x)\) 和 \(P_S(Jx)\) 都非空，并定义
\[
a(x)=d(x,P_S(Jx)),\qquad
\delta(x)=d(P_S(x),P_S(Jx)).
\]
两集合间的 d 为所有点对距离的 infimum，未假设两个投影集合之间的 infimum 取到。\(a\) 是输入到**输出最近零点**的锚距离，\(\delta\) 衡量输入最近点与输出最近点之间的最小漂移。定义未使用待证的 \(d(Jx,S)\) 的阶。

<a id="na-drift"></a>
## C48-v1 / NA-DRIFT · 锚距离与漂移包络等价

对上述每个 x 有
\[
r_x\le a(x)\le r_x+\delta(x)\le3a(x). \tag{NA-1}
\]
故在 \(0<r\le r_0\) 上，若空家族的非负 supremum 约定为 0，则
\[
\mathcal A(r)=\sup_{\substack{x\in U\\0<d(x,S)\le r}}a(x),\quad
\chi(r)=\sup_{\substack{x\in U\\0<d(x,S)\le r}}(r_x+\delta(x))
\quad\Longrightarrow\quad
\mathcal A(r)\le\chi(r)\le3\mathcal A(r). \tag{NA-2}
\]

**证明。** \(P_S(y)\subset S\) 给第一式。取任意 \(\varepsilon>0\) 和 \(p_x\in P_S(x),p_y\in P_S(y)\)，使 \(\|p_x-p_y\|\le\delta(x)+\varepsilon\)，便有 \(a(x)\le\|x-p_y\|\le r_x+\delta(x)+\varepsilon\)。反向取 \(p_y\in P_S(y)\) 使 \(\|x-p_y\|\le a(x)+\varepsilon\)，再取任意 \(p_x\in P_S(x)\)，则 \(\delta(x)\le\|p_x-p_y\|\le r_x+a(x)+\varepsilon\)。令 \(\varepsilon\downarrow0\)，并用 \(r_x\le a(x)\)；逐点取 supremum 得 NA-2。此处不假装最近点对一定实现 \(\delta\)。

若该家族在任意小 r 都非空，\(\mathcal A(r)\le K r^\theta\) 且 \(K<\infty\)，则上述距离下界**只排除 \(\theta>1\)**，并不推出 \(\theta>0\)。研究趋零幂包络时须**另取 \(K>0,\theta>0\)**，此时才有 \(0<\theta\le1\)：对每个实际 x，\(d(x,S)\le a(x)\le K d(x,S)^\theta\)，而 \(\theta>1\) 与趋零的实际距离矛盾。空尾部不产生此限制。

<a id="na-compose"></a>
## C49-v2 / NA-COMPOSE · 真 EB 与锚点模的合取上界

另设有限非减 gauge \(\psi:[0,\eta_\psi)\to[0,\infty)\)，\(\psi(t)=o(t)\)。对家族中每个 x，要求 \(t=\|w(x)\|<\eta_\psi\)、实际输出 \(y=Jx\) 的**真残差** EB
\[
s_x=d(y,S)\le\psi(r_F(y)),
\]
并在所有达到的 t 上有 \(\psi(t)\le\lambda t/2\)。若该 x 还满足 \((2/\lambda)a(x)<\eta_\psi\)，则
\[
s_x\le\psi((2/\lambda)a(x))
\le\psi((2/\lambda)[r_x+\delta(x)]), \tag{NA-3}
\]
后一项还需其自变量在定义域内。证明中的关键界是
\[
|a(x)-\lambda t|\le s_x\le\psi(t), \tag{NA-4}
\]
因对每个 \(p\in P_S(y)\) 有 \(|\|x-p\|-\|x-y\||\le\|y-p\|=s_x\)，再对 p 取 infimum。故 \(a(x)\ge\lambda t/2\)、\(r_F(y)\le t\)，并用 \(\psi\) 非减及 NA-1。注意 \(t=0\) 会使 \(x=y\in S\)，不在 \(r_x>0\) 的家族中。

若同一整个家族另有 \(K>0,\theta>0\) 及 \(\mathcal A(r)\le K r^\theta\) 对每个 \(0<r\le r_0\) 成立，且缩小 \(r_0\) 后 \((2K/\lambda)r_0^\theta<\eta_\psi\)，则右端 gauge 对所有更小 r 都有定义，并且
\[
\sup_{\substack{x\in U\\0<d(x,S)\le r}} d(Jx,S)
\le\psi((2K/\lambda)r^\theta). \tag{NA-5}
\]
幂型 \(\psi(t)=\rho t^q\)、\(q>1\) 给逐点 \(d(Jx,S)\le\rho(2K/\lambda)^q d(x,S)^{\theta q}\)。这是 uniform **upper exponent**；未给轨道留域、完整 resolvent 任意选择或最优指数。若 \(t\to0\)，NA-4 与 \(\psi(t)=o(t)\) 还给 \(a(x)/t\to\lambda\)；锚模是实际步长的几何分解，不是脱离算法另生一个速率定理。

<a id="na-approx"></a>
## NA-APPROX · 未取得最近点时的近似锚

不假设上述 projection 非空。对 \(\varepsilon\ge0\) 定义 \(P_S^\varepsilon(y)=\{p\in S:\|y-p\|\le d(y,S)+\varepsilon\}\)。对每个实际 \(0<t=\|w(x)\|<\eta_\psi\)，令 \(e(t)>0\)（或另证 \(P_S^{e(t)}(y)\ne\varnothing\)），并设 \(a_e(x)=d(x,P_S^{e(t)}(y))\)。若同一输出真 EB 且对全部相关小 t 有
\[
\psi(t)+e(t)\le\kappa\lambda t,\quad 0\le\kappa<1,
\quad a_e(x)/((1-\kappa)\lambda)<\eta_\psi, \tag{NA-6}
\]
则 \(d(Jx,S)\le\psi(a_e(x)/((1-\kappa)\lambda))\)。因为每个近似锚 p 都有 \(\|x-p\|\ge\lambda t-d(y,S)-e(t)\ge(1-\kappa)\lambda t\)，取 infimum 后用真 EB 与单调性即可。\(e(t)>0\) 利用非空 S 和有限距离保证近似集合非空；没有这一条件不能凭空选点。本节只替换最近点存在性，不替换输入 coverage 或同一输出 EB。

<a id="na-sharp"></a>
## C50-v2 / NA-SHARP · \(\theta q\) 锐性必须在同一序列合取

令 \(x_n\in\mathcal X_{r_0}\)、\(r_n=d(x_n,S)\downarrow0\)，写 \(a_n=a(x_n),t_n=\|w(x_n)\|,s_n=d(Jx_n,S)\)。对任意已声明的 \(\theta,q\) 且同一序列有 \(a_n\asymp r_n^\theta,\ t_n\asymp a_n,\ s_n\asymp t_n^q\)，则 \(s_n\asymp r_n^{\theta q}\)。若三个正比值分别收敛到 \(A,B,C\in(0,\infty)\)，则
\[
\frac{s_n}{r_n^{\theta q}}\longrightarrow C B^q A^q. \tag{NA-7}
\]
这是三个比值相乘，并非由 \(\theta\) 和 q 在**不同序列**上分别锐而来。在 C49-v2 的 \(\psi=o(t)\) 条件**且 \(t_n\to0\)** 下，NA-4 进一步强制 \(B=1/\lambda\)；\(\theta>0,A<\infty\) 和正比值也会使这一趋零条件自动成立。\(\theta=0\) 时仅凭“固定小步”不够，见 [F38](../../FAILED_ROUTES.md#f38)。正的归一化因子仍是附加证据，不从 NA-5 的上界产生。

<a id="na-source"></a>
## 来源、状态与未闭范围

来源：[9/01 RL_foundations §8–§9.1](../../history/sources/次单调论文研究/RL_foundations.md)。C48–C50 和近似锚的证明在此以全部 index family、非取到的集合间 infimum、gauge 定义域与同序列量词重算。状态 derived-checked 限这些条件关系；GX-071–073 的具体对象另有卡，不能从它们倒证一般最优性。§9.2–§9.4 已有各自对象卡；本轮没有审文献的先行性，也没有从逐点上界推任何全轨道收敛结论。
