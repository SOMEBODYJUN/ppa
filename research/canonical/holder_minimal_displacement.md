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
