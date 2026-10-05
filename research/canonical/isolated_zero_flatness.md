# 孤立零点的分支平坦性、真实残差与精确阶

本页重写 9/01 RL_foundations.md §7.1–7.6 的可独立使用链。对象是给定图点或指定近端选择；全图 RL、完整 resolvent 单值性不是下述代数的暗含前提。代数、邻域量词和反向障碍已重新核算；外部先行性未审。

<a id="iz-germ"></a>
## IZ-GERM · 同一个图 germ 上的三种平坦性

令 \(H\) 为实 Hilbert 空间，\(\lambda>0,q>1,p\in F^{-1}(0)\)，\(\Gamma\subset\operatorname{gph}F\) 且 \((p,0)\in\Gamma\)。只对充分接近 \((p,0)\) 的**所有** \((y,w)\in\Gamma\) 陈述以下估计，置 \(x=y+\lambda w,\widehat x=y-\lambda w\)：

\[
\begin{array}{ll}
(B_q)&\|y-p\|\le B\|w\|^q,\\
(J_q)&\|y-p\|\le J\|x-p\|^q,\\
(R_q)&\|\widehat x-(2p-x)\|\le R\|x-p\|^q.
\end{array}
\]

三种性质在可能不同的缩小 graph germ 上等价。\(B_q\Rightarrow J_q\) 可取 \(J=B(2/\lambda)^q\)；\(J_q\Rightarrow B_q\) 可取 \(B=J(2\lambda)^q\)；\(J_q\Leftrightarrow R_q\) 的常数满足 \(R=2J\)。这些是可用常数，不声称最优。

**证明。** 若 \(B_q\) 成立，把 germ 缩至 \(B\|w\|^{q-1}\le\lambda/2\)，则 \(\|x-p\|\ge\lambda\|w\|-\|y-p\|\ge\lambda\|w\|/2\)。反向把 germ 缩至 \(J\|x-p\|^{q-1}\le1/2\)，得 \(\lambda\|w\|\ge\|x-p\|-\|y-p\|\ge\|x-p\|/2\)。最后 \(\widehat x-(2p-x)=2(y-p)\) 逐图点成立。这些推导不要求 \(x\mapsto y\) 单值；要把 \(J_q,R_q\) 称为映射的模，必须另证输入唯一性和 coverage。

对有限非减、原点为零且 \(o(t)\) 的 gauge \(\beta,\alpha\)，相同证明只给
\[
\|y-p\|\le\beta(\|w\|)
\Longrightarrow\|y-p\|\le\beta((2/\lambda)\|x-p\|),\quad
\|y-p\|\le\alpha(\|x-p\|)
\Longrightarrow\|y-p\|\le\alpha(2\lambda\|w\|).
\]
须保证缩域后重标度自变量仍在 gauge 定义域。若要换成同一个 gauge 仅乘常数的界，还需对应固定 dilation 的 \(\psi(ct)=O(\psi(t))\)；单凭 \(\psi=o(t)\) 不给这一性质。[C159 的完整阶梯图](gauge_dilation_boundary.md#gd-theorem)给每个缩小 graph germ 的反例，真实全纤维 EB 取等；带重标度的正向界仍成立。

<a id="iz-fibers"></a>
## IZ-FIBERS · 从完整残差到分支以及反向的缺门

令 \(S=F^{-1}(0)\)，\(p\) 在 \(S\) 中局部孤立。缩小输出球 \(U\) 后可令 \(d(y,S)=\|y-p\|\) 对所有 \(y\in U\) 成立。若在 \(U\) 的真实全纤维残差上有 \(\|y-p\|\le\rho r_F(y)^q\)，则每个 \(w\in F(y)\) 都有 \(\|y-p\|\le\rho\|w\|^q\)，因为 \(r_F(y)\le\|w\|\)。如原 EB 只在 \(r_F(y)\le\bar t\) 的窗口成立，这一方向也只在该窗口调用。

反向需覆盖近零的**全部小残差图值**：存在 \(U_c\ni p,\eta>0\)，使
\[
\{(y,w):y\in U_c,\ w\in F(y),\ \|w\|<\eta\}\subset\Gamma. \tag{IZ-1}
\]
若 \(B_q\) 在这部分 \(\Gamma\) 上以同一常数 \(B\) 成立，则在缩小的输出球内存在 \(C\) 使 \(\|y-p\|\le C r_F(y)^q\) 对所有有限残差 \(y\) 成立。确实，若 \(r_F(y)<\eta/2\)，可取 \(w_n\in F(y)\) 且 \(\|w_n\|\to r_F(y)\)、最终 \(\|w_n\|<\eta\)，再取极限；若 \(r_F(y)\ge\eta/2\) 且 \(\|y-p\|<d_0\)，用 \(d_0(2/\eta)^q r_F(y)^q\) 覆盖。不假设 infimum 取到。

**不能只检查一条有利分支。** 在 \(H=\mathbb R,q>1\) 令 \(F(0)=\{0\}\)，\(F(y)=\{|y|^{1/q},y^2\}\)（\(0<|y|<1\)；其他点可置空）。\(p=0\) 是孤立零点；选择 \(w=|y|^{1/q}\) 满足 \(|y|=|w|^q\)，但真实 \(r_F(y)=|y|^2\)，任何 \(|y|\le C r_F(y)^q\) 在 \(y\to0\) 都失败。此图未声明全对 RL；反例仅攻击“选中值界 \(\Rightarrow\) 真 EB”的逆向。

<a id="iz-ppa"></a>
## C45-v1 / IZ-PPA · 指定分支的超线性上阶

沿用孤立零点，取 \(q>1,\rho>0\)。设 \(T:V\to H\) 是指定的单值选择，对每个 \(x\in V\) 有 \(Tx\in J_{\lambda F}(x)\)，且 \(T(p)=p\)。写 \(w(x)=(x-Tx)/\lambda\in F(Tx)\)。假设存在输入邻域 \(V_0\subset V\)、输出球 \(U\) 与 \(\eta>0\)，使每个 \(x\in V_0\) 都满足 \(Tx\in U,\|w(x)\|<\eta\)，并在这些输出上有真实 EB \(\|Tx-p\|\le\rho r_F(Tx)^q\)，同时 \(\rho\eta^{q-1}\le\lambda/2\)。则对所有 \(x\in V_0\)
\[
\|Tx-p\|\le C_q\|x-p\|^q,\quad
\|(2T-I)x-(2p-x)\|\le2C_q\|x-p\|^q,\quad C_q=\rho(2/\lambda)^q. \tag{IZ-2}
\]
若 \(\overline B(p,\delta_0)\subset V_0\)，选 \(0<\delta\le\delta_0\) 且 \(C_q\delta^{q-1}\le\theta<1\)，则此闭球在 \(T\) 下不变；对其中每个由此选择产生的轨道，\(r_k=\|x^k-p\|\) 满足
\[
r_{k+1}\le C_qr_k^q,\qquad
r_k\le C_q^{(q^k-1)/(q-1)}r_0^{q^k}\to0. \tag{IZ-3}
\]

**证明。** EB 与 \(r_F(Tx)\le\|w(x)\|\) 给 \(\|Tx-p\|\le\rho\|w(x)\|^q\le(\lambda/2)\|w(x)\|\)。于是 \(\|x-p\|\ge\lambda\|w(x)\|/2\)，得到 (IZ-2)；反射式是 IZ-GERM 的恒等式。球内 \(\|Tx-p\|\le\theta\|x-p\|\le\theta\delta<\delta\)，每一步仍可调用相同邻域假设；归纳得 (IZ-3)。只给 upper \(q\)-order，不保证正的归一化极限。完整 resolvent 的任意选择若要继承，须另证该域上所有完整纤维遵守这些条件。

对一般非减且 \(\psi(t)=o(t)\) 的真实 gauge EB，若同样的窗口保证 \(\|w(x)\|\) 足够小且重标度位于 gauge 定义域，则 \(\|Tx-p\|\le\psi((2/\lambda)\|x-p\|)=o(\|x-p\|)\)。足够小的输入球不变，非终止轨道的距离比趋零；输入 coverage、输出留域与小步门仍需核。

<a id="iz-factor"></a>
## C46-v1 / IZ-FACTOR · 正的精确 Q 因子需要另一个极限

在 C45 的球内取非终止轨道，令 \(w_k=(x^k-x^{k+1})/\lambda\)。若额外知道
\[
\frac{\|x^{k+1}-p\|}{\|w_k\|^q}\longrightarrow\mu\in(0,\infty), \tag{IZ-4}
\]
则 \(\|x^{k+1}-p\|=o(\|w_k\|)\)，而 \(x^k-p=(x^{k+1}-p)+\lambda w_k\) 给 \(\|x^k-p\|/(\lambda\|w_k\|)\to1\)。故
\[
\frac{\|x^{k+1}-p\|}{\|x^k-p\|^q}\longrightarrow\mu/\lambda^q.
\]
若没有 (IZ-4)，C45 的上界可能严格保守；距离上阶、正 Q 因子和全对反射指数是不同观察。

<a id="iz-source"></a>
## 来源、修订范围与待核义务

来源是 [9/01 RL_foundations §7.1–7.6](../../history/sources/次单调论文研究/RL_foundations.md)。本页将 7.3 中“全 EB”是否限残差窗口显式分开，并在反向加入全部小残差纤维 (IZ-1)；身份以此版本为准。第 7.4–7.6 节的指定分支和归一化极限机制重新推导；未把 §8 非孤立零集的 alignment 或先行性一起验收。[GX-074 coverage 反例](../topics/path_dynamics/discrete_coverage.md)检验另一独立门：图上的模与 EB 均不能生成输入邻域。
