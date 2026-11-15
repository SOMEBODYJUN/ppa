# Hölder 映射的最坏最小位移与完整 RL 值域

<a id="hmd-characteristic"></a>
## C293 · 有界凸集上的线性阶

固定实 Banach 空间 \(X\) 和 \(0<\gamma<1\)。对非空有界闭凸集 \(K\subset X\) 及 \(T:K\to K\)，记 \(d_K(T)=\inf_{x\in K}\|x-Tx\|\)。令
\[
 \Lambda_\gamma(X)=\sup_{K,T}d_K(T),\qquad
 J_{\mathrm{rel}}(X)=\sup_{\operatorname{diam}K>0}
 \frac{\inf_{c\in K}\sup_{x\in K}\|x-c\|}{\operatorname{diam}K}.
\]
第一上确界取所有这样的 \(K\) 和满足 \(\|Tx-Ty\|\le\|x-y\|^\gamma\) 的自映射。第二上确界的集合类型相同，圆心须在集合内。零空间约定 \(J_{\mathrm{rel}}=0\)。则
\[
 \Lambda_\gamma(X)\le (1-\gamma)J_{\mathrm{rel}}(X). \tag{1}
\]
有限维时 \(\Lambda_\gamma=0\)。每个无限维实 Banach 空间均有 \(\Lambda_\gamma(X)=\Theta(1-\gamma)\) 当 \(\gamma\uparrow1\)。下界常数可依赖 \(X\)。

**有限直径归约。** 给定 \(K_0,T\)，递推 \(K_{j+1}=\overline{\operatorname{conv}}T(K_j)\)。由 \(T(K_0)\subset K_0\) 及归纳，\(K_{j+1}\subset K_j\) 且每个 \(K_j\) 为 \(T\)-不变。取闭凸包保持直径，故 \(\operatorname{diam}K_j\le(\operatorname{diam}K_0)^{\gamma^j}\)。若某级直径为零就有固定点。其余情形直接用 \(d_{K_0}(T)\le\operatorname{diam}K_j\) 得 \(\Lambda_\gamma(X)\le1\)。这里无需假设嵌套集的交非空。

**同一上确界的缩放。** 若允许任意正 Hölder 系数 \(t\)，相应上确界恰为 \(t^{1/(1-\gamma)}\Lambda_\gamma\)。确切变换是 \(K\mapsto aK,\ T\mapsto[x\mapsto aT(x/a)]\)，其中 \(a=t^{1/(1-\gamma)}\)。此变换双向保持相应类并精确缩放最小位移。固定 \(0<t<1\)、\(\eta>0\)。在 \(K_j\) 选 \(c_j\in K_j\)，使 \(\sup_{x\in K_j}\|x-c_j\|\le J_{\mathrm{rel}}\operatorname{diam}K_j+\eta\)。映射 \(T_{j,t}(x)=tT(x)+(1-t)c_j\) 是 \(K_j\) 的自映射，Hölder 系数至多 \(t\)。于是
\[
 d_{K_0}(T)\le d_{K_j}(T)
 \le t^{1/(1-\gamma)}\Lambda_\gamma+
 (1-t)\bigl(J_{\mathrm{rel}}\operatorname{diam}K_j+\eta\bigr).
\]
上界依次取 \(j\to\infty,\eta\downarrow0\)，再对 \(K_0,T\) 取上确界，可得 \((1-t^{1/(1-\gamma)})\Lambda_\gamma\le(1-t)J_{\mathrm{rel}}\)。最后取 \(t\uparrow1\) 得 (1)。

**下界。** 对无限维 \(X\) 的闭单位球，Lin–Sternfeld 主定理给 Lipschitz 自映射 \(S\)，其最小位移 \(\delta>0\)。前提为非全有界凸集，闭单位球满足。取 \(\kappa>1\) 为其 Lipschitz 常数的上界。对 \(0<a\le1\) 置 \(S_a=(1-a)I+aS\)，则 \(d(S_a)=a\delta\)，斜率至多 \(k=1+a(\kappa-1)\)。缩放到半径 \(r=\tfrac12 k^{-\gamma/(1-\gamma)}\) 的闭球。新映射的距离上界为 \(\min\{k s,2r\}\le k^\gamma(2r)^{1-\gamma}s^\gamma=s^\gamma\)。当 \(\gamma\ge1/\kappa\)，取 \(k=1/\gamma\)，给
\[
 \Lambda_\gamma(X)\ \ge\
 \frac{\delta}{2(\kappa-1)}(1-\gamma)\gamma^{\gamma/(1-\gamma)-1}. \tag{2}
\]
幂因子趋于 \(e^{-1}\)。这个下界使用一个预先固定的 \(S\)，其余参数随 \(\gamma\) 变化。有限维由 Brouwer 对任意非空紧凸集给固定点。

<a id="hmd-range"></a>
## C294 · Hilbert 空间原关系的最大值域缺口

令 \(H\) 为实 Hilbert 空间。记 \(D_\gamma(H)=\sup_C\inf_{p\in H}\|p-C(p)\|\)，其中每个 \(C:H\to H\) 都在全尺度满足同一系数 1 的 \(\gamma\)-Hölder 估计。则 \(D_\gamma(H)=\Lambda_\gamma(H)\)。

**从全域到有界。** 每个 \(C\) 有不变闭球。取 \(M\) 足够大使 \(\|C(0)\|+M^\gamma\le M\) 即可。因此 \(D_\gamma\le\Lambda_\gamma\)。**从有界到全域。** 令 \(P_K\) 为闭凸集 \(K\) 的正交投影。\(C=T\circ P_K\) 满足相同 Hölder 条件，且
\[
 \|p-C(p)\|^2\ge \|P_Kp-T(P_Kp)\|^2+\|p-P_Kp\|^2.
\]
这用投影变分不等式，取 \(p\in K\) 即得两域最小位移相等。由 Hilbert 的 Jung 界 \(J_{\mathrm{rel}}\le1/\sqrt2\)，从 (1) 得
\[
 D_\gamma(H)\le(1-\gamma)/\sqrt2. \tag{3}
\]
这里的 Jung 界也可用 [C290 的有限球判据](quadratic_cross_approximation.md#qca-criterion)直接证明。直径为 \(d\) 的集合之有限点组的任意加权方差不超过 \(d^2/2\)。因此以各点为中心、半径 \(d/\sqrt2\) 的球在每个有限子族中相交。再用一个球的弱紧性得到全交点，并投影入 \(K\)，距离不增。

固定 \(\lambda,L>0\)，\(R=L^{1/(1-\gamma)}\)。令 \(F_C\) 为全域 Cayley 坐标定义的完整关系
\[
 \operatorname{gph}F_C=\{((p+C(p))/2,(p-C(p))/(2\lambda)):p\in H\},
\]
其中 \(C\) 的全尺度 \(\gamma\)-Hölder 系数至多 \(L\)。该关系满足 [C183 的完整 RL 合同](infinite_fiber_boundary.md#if-object)，满 Minty 输入且固定参数图极大。任意 \(v\in H\) 的真值域距离，及任意 \(x\in H\) 的真定义域距离，分别为
\[
 \begin{aligned}
  \operatorname{dist}(v,\operatorname{ran}F_C)
   &=\frac1{2\lambda}\inf_p\|p-C(p)-2\lambda v\|,\\
  \operatorname{dist}(x,\operatorname{dom}F_C)
   &=\frac12\inf_p\|p+C(p)-2x\|.
 \end{aligned}
\]
对 \(C\) 与目标取最坏值，分别等于 \(R D_\gamma(H)/(2\lambda)\) 与 \(R D_\gamma(H)/2\)。这是因为平移像或取负不改变 Holder 系数，且同时缩放定义域及像精确恢复 \(R\)。无限维阶由 (2)–(3) 闭合。上下界按自然尺度 \(R\) 归一化。若固定的是 \(L\ne1\)，则 \(R\) 自身也随指数变化。

**即使零点唯一也有正量级缺口。** 在 (2) 的 Hilbert 构造取 \(C_0=T\circ P_{\overline B(0,r)}\)，其中 \(T\) 是缩放后斜率为 \(k\) 的有界自映射。置 \(C_b(p)=C_0(p-b)\)。则 \(d_H(C_0)=\inf_p\|p-C_b(p)-b\|\)。\(C_b\) 的像仍在半径 \(r\) 的球，故每个固定点必须落在该球。若 \(\|b\|>(k+1)r\)，对球中的 \(p,p'\) 沿其平移线段，径向投影的导数范数至多 \(r/(\|b\|-r)\)。因此 \(C_b\) 在球上严格压缩，存在唯一固定点。给定同一 \(L\) 可按 \(R\) 再缩放。故实现 (2) 的正值域缺口可和一个确切的单点完整零集同时存在。

<a id="hmd-prior"></a>
## 外部先行与剩余问题

- Kirk 1997 综述 §2 的定理 2.2–2.5 和 Rhoades 2000 定理 8 给 Hölder 或放松型条件下的逐图位移估计。它们的可见合同涉及截断非扩张、系数的幂或正规结构系数。在已核陈述中未见 (1) 的归一化最坏包络及临界指数线性阶。[Kirk 1997 原文](https://www.bc.umcs.pl/Content/30480)，[Kirk 1998 刊本入口](https://doi.org/10.1080/01630569808816815)，[Rhoades 2000 原文](https://insa.nic.in/writereaddata/UpLoadedFiles/IJPAM/20005b10_625.pdf)。Kirk 1998 刊本全文是优先性剩余门。
- Barroso 2023 Proposition 1.2(ii) 已给无限维闭单位球上正最小位移的归一化 Hölder 映射，Theorem 3.8(3) 控制某些实例的位移上界。后者的存在量词不能给所有映射的最坏缺口上界。线性下界调入 Lin–Sternfeld，再先作平均，使 Lipschitz 常数随指数趋近 1。[Barroso v3](https://arxiv.org/pdf/2207.03057)，[Lin–Sternfeld](https://doi.org/10.1090/S0002-9939-1985-0776193-5)。
- 用 Lipschitz 影子加 Goebel 位移界也能给 \(O((1-\gamma)\log(1/(1-\gamma)))\)，已被 (1) 覆盖。由任意全局 Hölder 方程到有界闭凸自映射的精确等价仅在本页 Hilbert 投影合同下证明；Banach 结论针对 \(\Lambda_\gamma\)。
- 跨全部 Hilbert 映射的最优首项系数、\(\lim_{\gamma\uparrow1}D_\gamma/(1-\gamma)\) 是否存在、其与经典 Lipschitz 最小位移特征的定量关系仍开放。当前可声称归一化阶与真实原关系缺口，已有定理和有限文献检索不足以判定四大期刊主贡献。

<a id="hmd-c0"></a>
## C300 · 标准 \(c_0\) 单位球的一般凹模精确特征

给连续非减凹 \(\omega:[0,\infty)\to[0,\infty)\)，\(\omega(0)=0,\omega(1)=1\)。令 \(\Psi_\omega(c_0)\) 为闭单位球的全部 \(\omega\)-连续自映射的最小位移上确界，其中空间用标准上确界范数。则
\[
 \Psi_\omega(c_0)=m(\omega)=\max_{0\le s\le1}(\omega(s)-s).
\]
对 \(\omega(s)=s^\gamma\)、\(0<\gamma<1\)，此值也是全域 \(c_0\to c_0\) 的归一化 Hölder 最大位移，
\[
 m(\omega)=(1-\gamma)\gamma^{\gamma/(1-\gamma)}.
\]
对全域端点 \(\gamma=1\) 无此结论，因为非零平移已给任意正位移。

**近非扩张映射的逐坐标修正。** 设 \(T:A\to c_0\) 定义在任意非空度量空间，\(\|Tx-Ty\|_\infty\le d(x,y)+m\)。记
\[
 U_i(x)=\sup_{y\in A}(T_i(y)-d(x,y)),\qquad
 L_i(x)=\inf_{y\in A}(T_i(y)+d(x,y)).
\]
由加性界和三角不等式，\(L_i\le T_i\le U_i\)、\(U_i-L_i\le m\)，各函数都是有限 1-Lipschitz。置
\[
 S_i(x)=\operatorname{median}\{U_i(x)-m,\,0,\,L_i(x)+m\}.
\]
上下端有序，且该区间包含 \(T_i(x)\)。所以 \(S_i(x)\) 位于 \(0\) 与 \(T_i(x)\) 之间，且 \(|S_i(x)-T_i(x)|\le m\)。中位数在三坐标的上确界范数下是 1-Lipschitz，因此 \(S:A\to c_0\) 为非扩张映射，\(\|S(x)\|\le\|T(x)\|\)，\(\|S-T\|_\infty\le m\)。\(c_0\) 性质来自逐点无穷尾由 \(T(x)\) 支配。

在单位球上，\(\omega(s)-s\le m(\omega)\) 对全部尺度成立。对 \(s\ge1\) 这是由凹性和 \(\omega(1)=1\) 给出的 \(\omega(s)\le s\)。上述 \(S\) 是闭球的非扩张自映射，最小位移为零，因为 \(x\mapsto tS(x)\) 为严格压缩，取其固定点并令 \(t\uparrow1\)。故 \(d(T)\le m(\omega)\)。对全域系数 1 的 Hölder 映射，同理，因 \(\|T(0)\|+R^\gamma\le R\) 对充分大的球半径成立，\(S\) 在该球不变。

**匹配下界。** 令 \(q(s)=\min\{1,\max\{0,s\}\}\)，定义
\[
 T(x)=(1,\omega(q(x_1)),\omega(q(x_2)),\ldots).
\]
它是全域至闭单位球的映射，由凹模的次可加性和 \(q\) 非扩张可知满足同一模。若 \(m>0\)，取内点 \(s_*>0\) 达到最大值。由 \(\omega(s_*)\le1\)，\(1-m\ge s_*\)。若 \(\|Tx-x\|\le m\)，则 \(x_1\ge s_*\)，并递推 \(x_{i+1}\ge\omega(s_*)-m=s_*\) 对全部 \(i\)，与 \(x\in c_0\) 冲突。故最小位移为 \(m\)，该映射在 \(m>0\) 时未取到最小位移。\(m=0\) 直接由上界得结论。幂模的最大值由 \(s_*=\gamma^{1/(1-\gamma)}\) 代入。

Goebel 1973 Theorem 1、Example 3 与 Kapitan–Piasecki 2024 Example 1.1 给经典 Lipschitz \(c_0\) 最优位移移位。Barroso 2023 Theorem 5.1(1) 构造相关幂移位与某个映射的位移界。Barroso–Bedoya–da Silva 2025 主要结果讨论一般模的 AFPP/FPP 和存在性。已核陈述中尚无相同的全映射上包络。经典条件与程序性差异分别见 [Goebel](https://msp.org/pjm/1973/45-1/pjm-v45-n1-p14-p.pdf)，[Kapitan–Piasecki](https://math.ubbcluj.ro/~nodeacj/download.php?f=242-kap-pia-23-0098-final-final.pdf)，[Barroso 2023](https://arxiv.org/pdf/2207.03057)，[Barroso–Bedoya–da Silva 2025](https://arxiv.org/abs/2507.00859)。本结论没有确定跨任意闭凸集的 \(\Lambda_\gamma(c_0)\)，因为逐坐标支配不保证修正后留在任意凸集。

<a id="hmd-fixed"></a>
## C301 · 固定 Hilbert 凸集与固定 Banach 单位球

对固定非空有界闭凸 \(K\subset X\)，令 \(\Lambda_\gamma(K)=\sup_T d_K(T)\)，其中 \(T\) 为归一化 \(\gamma\)-Hölder 自映射。若 \(K\) 紧，则 Schauder 给零。以下两种非紧情形均有 \(\Lambda_\gamma(K)=\Theta_K(1-\gamma)\)，上界直接来自 C293。

**固定 Hilbert 凸集。** 在该 \(K\) 取 Lin–Sternfeld 映射 \(S\)，最小位移 \(\delta>0\)，Lipschitz 常数上界 \(\kappa>1\)。先以 \(a=(\gamma^{-1}-1)/(\kappa-1)\) 与恒等平均，\(\gamma\) 充分接近 1 时 \(0<a\le1\)，新斜率至多 \(k=\gamma^{-1}\)。取 \(c\in K\) 和比例 \(r=\min(1,1/\operatorname{diam}K)k^{-\gamma/(1-\gamma)}\le1\) 缩到 \(K'=c+r(K-c)\subset K\)。插值给系数 1，位移变为 \(ra\delta\)。与 \(P_{K'}\) 复合后是整个 \(K\) 的同模自映射，且最小位移不变，论证如 C294。比例趋非零常数，所以得到线性下界。

**固定直径小于 1 的 Banach 凸集。** 对 \(0<D=\operatorname{diam}K<1\) 的非紧 \(K\)，取同样的 \(S,\delta,\kappa\)。与恒等平均，系数 \(a=(D^{-(1-\gamma)/\gamma}-1)/(\kappa-1)\) 对 \(\gamma\) 足够接近 1 属于 \((0,1]\)。范围仍在 \(K\)，斜率至多 \(D^{-(1-\gamma)/\gamma}\)，与直径 \(D\) 插值得系数至多 1，位移为 \(a\delta=\Theta_K(1-\gamma)\)。此结论针对给定范数尺度，不意味着可将任意固定的 \(K\) 直接替换成缩小的集合。

**固定任意 Banach 的闭单位球。** 在原单位球取同样的 \(S,\delta,\kappa\)。令 \(r=2^{1-4\kappa}\) 并令 \(R_r\) 为到半径 \(r\) 球的径向截断，Lipschitz 常数至多 2。定义 \(F(x)=rS(R_rx/r)\)，斜率至多 \(2\kappa\)，像落在 \(rB_X\)。对任意 \(x\in B_X\)，\(\|x-R_rx\|\le\|x-F(x)\|\)，故 \(r\delta\le\|R_rx-F(x)\|\le2\|x-F(x)\|\)。写 \(\epsilon=1-\gamma\)，令 \(a=(1-2^{-\epsilon})/(1-r)\) 及 \(T=(1-a)I+aF\)。对输入间距 \(s\in[0,2]\)，其差上界为
\[
 \min\{[1+a(2\kappa-1)]s,\,(1-a)s+2ar\}.
\]
在 \(0\le s\le2r\)，用 \(\log(1+a(2\kappa-1))\le\epsilon(2\kappa-1)\log2/(1-r)\le-\epsilon\log(2r)\)。在 \(2r\le s\le2\)，\(s^\gamma-(1-a)s-2ar\) 凹且两端非负。故 \(T\) 满足所需模，\(d(T)\ge a r\delta/2\)，是线性阶。这把 Barroso 单位球正位移存在的已知事实量化为整个特征在 \(\gamma\uparrow1\) 的锐阶。

**全体凸集的 Lipschitz 一侧比较。** 令 \(\Phi_X(k)\) 为所有有界闭凸正直径 \(K\)、所有 \(k\)-Lipschitz 自映射的 \(d_K(T)/\operatorname{diam}K\) 上确界。与恒等平均表明 \(\Phi_X(k)/(k-1)\) 对 \(k>1\) 非增。由以相对圆心压缩的经典估计 \(\Phi_X(k)\le J_{\rm rel}(X)(1-1/k)\)，可取有限右极限 \(A_X\)。对任意 \(T\) 用直径与 Lipschitz 插值后缩放，得
\[
 \Lambda_\gamma(X)\ge\sup_{k>1}k^{-\gamma/(1-\gamma)}\Phi_X(k),
 \qquad
 \liminf_{\gamma\uparrow1}\frac{\Lambda_\gamma(X)}{1-\gamma}\ge A_X/e.
\]
最后取 \(k=1/\gamma\)。这是直径归一化、跨可变凸集的特征，与单位球特征不同。匹配上界未知。

**一般固定 Banach 凸集的剩余义务。** 小像加平均的标量步骤能推广到任意直径，但需要在每个非紧凸集内构造像任意小且位移正的 Lipschitz 自映射。Bessaga 1994 印刷 Proposition 2.2 所写的支撑至多两个任意坐标的膜与证明所用的相邻三角膜在非顶点处有不同局部紧性，不能直接合并。其 (ii) 文字的全 \(\epsilon>0\) 与有界性亦冲突。这个来源缺口不会影响以上 Hilbert 及 Banach 单位球结论。[原文 pp.20–21](https://topology.nipissingu.ca/tp/reprints/v19/tp19002.pdf)。
