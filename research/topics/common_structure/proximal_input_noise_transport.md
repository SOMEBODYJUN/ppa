# 原近端输入误差沿零集搬运的代价

<a id="input-noise-transport"></a>

固定原步长 \(\lambda>0\)。给输入加误差 \(e_k\) 指保留完整原包含
\[
x_k+e_k-x_{k+1}\in\lambda F(x_{k+1}).
\]
精确原轨道对应 \(e_k=0\)。下面先在一个完整原算子族上计算两零点之间的扰动代价，再给任意原 RLEB 的可和输入误差条件。两个结果区分径向趋零与切向误差积累。

## 小输入误差搬运的精确代价

取 \(0<\alpha<1\)、\(b>0\)。令 \(w:[0,\infty)\to[0,\infty)\) 连续非减、次可加、\(w(0)=0\)，并假定
\[
W(h)=\sum_{j=0}^\infty w(\alpha^jh)<\infty\qquad(h\ge0).
\]
该级数在任意紧区间一致收敛，故 \(W\) 连续且 \(W(0)=0\)。在 \(\mathbb R^2\) 上定义完整单值原算子
\[
F(u,z)=\lambda^{-1}\big((\alpha^{-1}-1)u,-b\,\operatorname{sgn}(u)w(|u|/\alpha)\big).
\]
它的零集恰为 \(S=\{0\}\times\mathbb R\)，而且每个输入有唯一原根
\[
J(t,z)=\big(\alpha t,z+b\,\operatorname{sgn}(t)w(|t|)\big).
\]
精确原轨道从任意初值 \((t,z)\) 出发，收敛到 \((0,z+b\,\operatorname{sgn}(t)W(|t|))\)。

给定连续非减代价 \(\rho:[0,\infty)\to[0,\infty)\)、\(\rho(0)=0\)，令 \(D_\delta(L)\) 是从 \((0,0)\) 到 \((0,L)\) 的有限输入扰动路径的 \(\sum_k\rho(\|e_k\|)\) 下确界。各步使用上述原包含，且 \(\|e_k\|\le\delta\)。对 \(h>0\) 定义
\[
m(h)=\max_{0\le u\le h}\{bW(u)+\sqrt{h^2-u^2}\}.
\]
对每个 \(L\ne0\)，有扩展实数等式
\[
\boxed{\displaystyle\lim_{\delta\downarrow0}D_\delta(L)
=|L|\liminf_{h\downarrow0}\frac{\rho(h)}{m(h)}.} \tag{1}
\]
\(L=0\) 的代价为零。\(m(h)\) 是一次幅度为 \(h\) 的输入误差及其随后原动力所能产生的最大切向位移。式 (1) 说明这一响应同时决定大量小误差累计时的最低单位代价。

**证明。** 写误差 \(e_i=(u_i,v_i)\)。第 \(k\) 步受扰输入的法向坐标是 \(\sum_{i\le k}\alpha^{k-i}u_i\)，因此终点切向位移满足
\[
|L|\le\sum_i|v_i|+b\sum_k w\!\left(\left|\sum_{i\le k}\alpha^{k-i}u_i\right|\right)
\le\sum_i(|v_i|+bW(|u_i|))\le\sum_i m(\|e_i\|).
\]
其中零误差项按零计。乘以 \(\inf_{0<h\le\delta}\rho(h)/m(h)\) 得下界。

由对称性只证 \(L>0\)。固定 \(h>0\)，取达到 \(m(h)\) 的 \(u\) 及 \(v=\sqrt{h^2-u^2}\)。从零法向坐标施加 \((u,v)\)，接着走 \(n-1\) 步精确原近端，然后用输入误差 \((-\alpha^nu,0)\) 把法向坐标复位为零。此段的切向增量和总成本分别为
\[
g_n=v+b\sum_{j=0}^{n-1}w(\alpha^ju),\qquad c_n=\rho(h)+\rho(\alpha^nu).
\]
有 \(g_n\uparrow m(h)\) 和 \(c_n\to\rho(h)\)。取 \(g_n>0\) 并串接 \(\lfloor L/g_n\rfloor\) 份。最后一份同时缩放 \((u,v)\) 和复位误差。增量随缩放系数连续，从零达到 \(g_n\)，所以可精确到达 \(L\)，且每份成本至多 \(c_n\)。全部误差不超过 \(h\)，故 \(D_h(L)\le(L/g_n+1)c_n\)。先对 \(n\) 取极限，再沿实现右侧有限下极限的 \(h\downarrow0\) 取极限。\(\rho(h)\to0\) 去掉最后一份的附加项。右侧无穷时下界已足够。\(\square\)

### 幂阈值与真正非线性的原 RLEB

取 \(w(h)=h^\gamma\)、\(0<\gamma<1\) 及 \(\rho(h)=h^p\)、\(p>0\)。由
\[
\frac{bh^\gamma}{1-\alpha^\gamma}\le m(h)\le \frac{bh^\gamma}{1-\alpha^\gamma}+h
\]
可知 (1) 在 \(p>\gamma\) 时为零，在 \(p=\gamma\) 时为 \((1-\alpha^\gamma)|L|/b\)，在 \(p<\gamma\) 时为无穷。因而任取不同的两个零点，可以用任意小的总欧氏输入误差在两点之间移动。交替串接这类有限路径，每一段耗费至多 \(2^{-j}\) 且单步误差上限趋零，就得到一条扰动可和却不点收敛的有界原包含轨道。各段用证明中的同号切向增量，可把轨道留在两零点之间的切向区间及任意给定正宽法向管内。

对该完整原图，输入 \((t,z)\) 的最近锚为 \((0,z)\)，令 \(s=|t|\)。实际锚反射长度为
\[
\sqrt{(2\alpha-1)^2s^2+4b^2s^{2\gamma}}.
\]
可以取原模 \(\omega(s)=|2\alpha-1|s+2bs^\gamma\)，及完整真误差模 \(\psi(r)=\alpha(\lambda r/b)^{1/\gamma}\)，因为
\[
\lambda r_F(u,z)=\sqrt{(\alpha^{-1}-1)^2u^2+b^2(|u|/\alpha)^{2\gamma}}.
\]
两种幂都最优。对于 \(B(s)=(s+\omega(s))/2\)，有 \(\psi(B(s)/\lambda)/s\to\alpha\)。任取 \(\alpha<\kappa<1\)，可缩小正半径 \(R\) 使原 (P1)–(P4) 成立，并满足任给正的残差帽。幂模保证原 Dini 级数有限。取 \(U=X\) 即认证全部 \(0<d(x,S)\le R\) 的非解初值。因此上述零代价搬运确实出现在完整、唯一、真正非线性的原 RLEB 内。对照而言，若原预解式非扩张且逐点固定 \(S\)，则任一受扰路径从 \(p\in S\) 到 \(q\in S\) 满足 \(\|q-p\|\le\sum_k\|e_k\|\)，由每步到 \(p\) 的三角不等式得到。

<a id="rleb-input-noise"></a>

## 原一般模 RLEB 的可和输入误差

取[投稿的原 (P1)–(P4)](../../../发表成果整理/RLEB/sections/theorem_spine.tex)，包括同一允许原根关系 \(\mathcal J\)、窗口 \(U_R\)、完整真残差、反射模 \(\omega\) 与兼容常数 \(\kappa\)。在受扰输入 \(z_k=x_k+e_k\) 上任选 \(x_{k+1}\in\mathcal J(z_k)\)。任取 \(\kappa<a<1\)，令 \(q=\kappa/a\)、\(C=1/(1-a)\)，并记
\[
\delta_i=\|e_i\|,\qquad v_0=d(x_0,S)+\delta_0,\qquad v_i=\delta_i\ (i\ge1),\qquad
\Theta_q(t)=\sum_{j\ge0}B(q^jt).
\]
若每个 \(Cv_i\le R\) 且
\[
\sum_{i\ge0}\big[\delta_i+\Theta_q(Cv_i)\big]<\operatorname{dist}(x_0,X\setminus U),\qquad
\sum_{i\ge0}\Theta_q(Cv_i)<\infty, \tag{2}
\]
则每条允许扰动轨道可无限延拓，长度至多为 (2) 中第一个不等式的左端，且点收敛到 \(S\cap U\)。\(\Theta_q(R)<\infty\) 由原 \(\Theta_\kappa(R)<\infty\) 得到。每个几何区间 \((\kappa^{i+1}R,\kappa^iR]\) 至多包含统一有界数量的 \(q^j R\)，再用 \(B\) 非减即可。

**证明。** 只对已经进入 \(U_R\) 的输入调用原条件。反射几何给 \(\|x_{k+1}-z_k\|\le B(d(z_k,S))\)，原真残差满足 \(r_F(x_{k+1})\le\|x_{k+1}-z_k\|/\lambda\)。按原帽和 (P4) 得 \(d(x_{k+1},S)\le\kappa d(z_k,S)\)。因此在适用的有限前缀上，下一输入的距离满足
\[
d(z_k,S)\le\sum_{i=0}^k\kappa^{k-i}v_i\le C\max_{0\le i\le k}q^{k-i}v_i\le R.
\]
利用 \(B\) 非减，\(B(d(z_k,S))\le\sum_{i\le k}B(Cq^{k-i}v_i)\)。每个有限前缀的原步长度和新输入的 \(\delta_k\) 加起来受 (2) 支配，故 \(z_k\) 留在 \(U\)，从而进入 \(U_R\) 并可选择下一原根。有限前缀归纳关闭覆盖与留域。总步长可和给 Cauchy 性，且 \(v_i\) 可和，因为 \(B(t)\ge t/2\)。上一卷积界趋零，故极限属于闭集 \(S\)，严格留域预算保证极限仍在 \(U\)。\(\square\)

原模在零处连续，允许在正点跳跃。对 \(B(t)\asymp t^\gamma\) 的真正非线性情形，\(\Theta_q(t)\asymp t^\gamma\)。式 (2) 的可和指数与上一节反例的临界指数一致。式 (2) 使用含输入误差的留域预算。

## 和已有研究的关系

Fathi–Pageault 用 \(\sum_k d(Hx_k,x_{k+1})\) 定义紧度量空间上同胚的 Mather 障碍，[作者论文](https://doi.org/10.1017/etds.2013.107)及 [Pageault 博士论文第 2 章 §3、Proposition 3.1](https://citeseerx.ist.psu.edu/document?doi=766604f02224a5333732a137536a8c2ea5519710&repid=rep1&type=pdf)给出定义和三角不等式。这里的可逆原近端把每个输入误差精确写为 \(J^{-1}(x_{k+1})-x_k\)。对于度量型代价，本文路径和逆映射的反向顺序链在代价上相同。上述结果计算的是带单步上限、任意连续非减代价的极限，并核验了幂临界值与完整原 RLEB 的关系。公开优先性未穷尽。

这一关系仍缺两项恢复：点对点的扰动代价能区分上述算子与非扩张原近端，却尚未刻画通常两点单调性，也尚未从同一代价推出一般完整真误差界。它限制的是把正的欧氏输入扰动搬运代价作为原 RLEB 普遍前提的路线。对无误差原 PPA 的点收敛结论没有反驳。
