# DD 补偿的步长反演与原算子选参

本页核算作者补交的步长材料。DD1/DD2 主定理继续描述固定近端边的分段几何。本页从同一条判据反过来解 \(\lambda\)，再用一类独立于 \(\lambda\) 的原算子数据保证共同认证和实际近端覆盖。

<a id="dd-parameter-inversion"></a>
## C479 · 一次反演与整个尺度窗

固定非负共同缺陷 \(D(t)\)（对应下界 \(\Phi=-D\)）、原真残差模 \(\psi\) 和目标 \(0<A(t)<t\)。共同指同一 \(F,S\) 的证书在所有受检候选参数上有效。对任一 \(t>0\)，写
\[
r=\frac{A(t)}t,\qquad
q_t=\inf\{\rho\in D_\psi:\psi(\rho)>A(t)\},\qquad
B_D(t)=\frac{t+\sqrt{t^2+4D(t)}}2 .
\]
空坏层时误差界已足够。若坏层非空且 \(q_t=0\)，没有有限正 \(\lambda\) 通过该尺度的自由单边判据。对 \(0<q_t<\infty\)，定义
\[
H(t)=
\begin{cases}
\dfrac{\sqrt{t^2-A(t)^2+2D(t)}}{q_t},
 &D(t)\le A(t)(t+A(t)),\\[6pt]
\dfrac{B_D(t)}{q_t},
 &D(t)>A(t)(t+A(t)).
\end{cases}
\tag{P\lambda1}
\]
则在维数至少二的自由闭目标单边类，DD2 的指定非严格下降 \(a\le A(t)\) 判据，恰为 \(\lambda\ge H(t)\)，仅当第二支且 \(q_t\) 属于严格坏层时改用 \(\lambda>H(t)\)。空坏层可记 \(H(t)=0\)，非空且 \(q_t=0\) 记 \(H(t)=+\infty\)。

逐式代入 [C430 的原分段](reverse_compensation.md#dd2-compensation-piecewise)。第三支 \(\Sigma=r(r-1)<0\) 无法支付 \(D(t)/t^2\ge0\)。中支所需 \(z^2\ge 1-r^2+2D(t)/t^2\)，根自带 \(z\ge1-r\)，且根在 \(1+r\) 以内当且仅当 \(D(t)\le A(t)(t+A(t))\)。更大缺陷在高支解 \(z(z-1)\ge D(t)/t^2\)。两支相接，边界 \(z=1+r\) 属中支；开闭端点沿用原判据。若 \(\psi\) 在区间上连续严格递增且 \(A(t)\) 在其像的内部，\(q_t=\psi^{-1}(A(t))\)，坏层首端不取到。该版本下，若 \(\lambda>H(t)\)，可把 \(A(t)\) 向下微调仍通过判据，于是 \(a<A(t)\)。一般原模不作这个严格输出推断。

在固定窗 \(0<t\le R\)，取 \(H_R=\sup_{0<t\le R}H(t)\)。当 \(H_R<\infty\)，从共同证书、原根覆盖和窗条件的有效参数里选 \(\lambda>H_R\) 即认证下降；\(\lambda=H_R>0\) 按逐尺度端点检验。仍按原 DD2 条件支付长度、续接和留域。若有已知有限参数上限，严格充分测试是有效参数中确有一点大于 \(H_R\)，尤其在上限内侧连续可选时可与上限比较。固定图可能有更强证书；这里的反向精确性限描述自由单边几何。

### DD1 的闭式与两种极限

对 \(D(t)=\sigma t^2,\ \psi(\rho)=\ell\rho,\ A(t)=rt\)，(P\(\lambda\)1) 给附件的两支步长阈值。令 \(r\uparrow1\)，或直接反解 [DD1 的严格门](dd1_recovery.md#dd1-final-calibrated-gate)，统一线性下降证书恰为
\[
\lambda>\ell
\begin{cases}
\sqrt{2\sigma},&0\le\sigma\le2,\\
(1+\sqrt{1+4\sigma})/2,&\sigma\ge2.
\end{cases}
\tag{P\lambda2}
\]
其上有裕度便可选一个 \(r<1\)；等号在准确统一门上不承诺统一严格下降。此式要求 \(\sigma\) 是共同证书。若只知 \(\sigma_\lambda(R)\)，当 \(\lambda\le2\ell\)，原门是 \(\sigma_\lambda(R)<\lambda^2/(2\ell^2)\)，故 \(\sigma_\lambda(R)\to0\) 单独不够。

另一种可用的极限是 \(t\downarrow0\)。若 \(\lambda>\limsup_{t\downarrow0}H(t)\) 且该 \(\lambda\) 有相容的原根和数据窗，就可缩小窗得到统一逐尺度证书。例如设 \(D(t)\le C t^p,\ \psi(\rho)\le K\rho^q\) 分别在零附近成立，\(p,q>0\)，令 \(m=\min\{1,p/2\}\)。步帽 \(B_D(t)=O(t^m)\)，实际 \(r_F(y)\le B_D(t)/\lambda\)。因此每个固定 \(\lambda>0\) 有 \(a=O_\lambda(t^{mq})\)。若 \(mq>1\)，对每个固定正 \(\lambda\) 都可缩窗做到任意指定比例 \(r<1\)；长度按几何下降与 \(O(t^m)\) 步帽即可求和，再用原覆盖及位置预算。这里是 \(\forall\lambda\ \exists R_\lambda\) 的尺度结论。\(F(y)=\operatorname{sgn}(y)|y|^\alpha\)（\(0<\alpha<1\)）每个 \(\lambda\) 满域唯一，\(\Phi=0,\psi(\rho)=\rho^{1/\alpha}\)，直接展示这一现象。在固定正输入，\(\lambda\downarrow0\) 时根趋输入，所以这些固定比例一般无共同正半径。完整幂次分类见 [C399 等](../../canonical/dd2_power_defect_finite_length.md)。

<a id="dd-parameter-raw-angle"></a>
## C480 · 原算子角度、线性误差界与可变步长

设 \(F:\mathbb R^n\to\mathbb R^n\) 在闭球 \(V=\overline B(p_0,R_0)\) 的邻域连续，\(S\subseteq\operatorname{zer}F\) 非空闭且 \(p_0\in S\)。给定 \(\ell>0,\ 0\le\mu<1\)，对全部 \(y\in V,\ p\in S\cap V\) 假设
\[
d(y,S)\le\ell\|F(y)\|,\qquad
\langle F(y),y-p\rangle\ge-\mu\|F(y)\|\,\|y-p\|.
\tag{P\lambda3}
\]
两项原始数据不使用近端参数。允许关系取 \(J_{\lambda F}(x)\cap B(p_0,R_0)\)。

**统一覆盖。** 令 \(H_\tau(y)=y+\tau\lambda F(y)\)（\(0\le\tau\le1\)）。在 \(\partial V\) 用 \(p=p_0\) 配方得 \(\|H_\tau(y)-p_0\|^2\ge(1-\mu^2)R_0^2\)。所以对每个 \(\|x-p_0\|<\sqrt{1-\mu^2}R_0\)，边界同伦不会击中 \(x\)，Brouwer 度保持为恒等映射的 1，给球内根。该输入球对所有 \(\lambda>0\) 相同。选开认证球 \(U=B(p_0,r_0)\)，\(r_0<\min\{R_0/2,\sqrt{1-\mu^2}R_0\}\)，则每个 \(p_x\in P_S(x)\) 由 \(\|p_x-p_0\|\le2\|x-p_0\|\) 落在 \(V\)。

**由原角导出 DD1。** 对任何合法边，记 \(b=\|y-p_x\|,\ s=\|x-y\|,\ t=d(x,S),\ a=d(y,S)\)。有
\[
t^2\ge b^2+s^2-2\mu bs\ge2(1-\mu)bs,\quad
s\le t/\sqrt{1-\mu^2},\quad a\le\ell s/\lambda .
\]
于是 \(-\langle x-y,y-p_x\rangle\le\sigma_\mu t^2\)，\(\sigma_\mu=\mu/[2(1-\mu)]\)。用 (P\(\lambda\)1) 或 (P\(\lambda\)2) 即可从 \((\ell,\mu)\) 选择 \(\lambda\)。零输入下 \(s=0\)，故驻定。

**保留角度得到另一显式阈值。** 对 \(a>0\)，令 \(h=s/a\ge\lambda/\ell\)，在 \(b/a\ge1\) 上最小化平方估计，给
\[
t^2/a^2\ge 
\begin{cases}
1+h^2-2\mu h,&\mu h\le1,\\
(1-\mu^2)h^2,&\mu h\ge1 .
\end{cases}
\]
两支接合，且 \(h\ge\mu\) 时右端非减。令其达到 \(r^{-2}>1\)，得到
\[
\lambda_*(r)=\ell
\begin{cases}
\mu+\sqrt{\mu^2+r^{-2}-1},&\mu\le r/\sqrt{1+r^2},\\
1/(r\sqrt{1-\mu^2}),&\mu\ge r/\sqrt{1+r^2}.
\end{cases}
\tag{P\lambda4}
\]
\(\lambda\ge\lambda_*(r)\) 保证 \(a\le rt\)。这是 [C381 的逐边角度支付](../common_structure/two_anchor_angle_inverse.md#two-anchor-angle) 对指定 \(r\) 的反演，并非新角度几何。与压成 \(\sigma_\mu\) 的算法，同取 \(\ell=1,\mu=4/5,r=9/10\)，前者阈值 \(50/27\)，后者 \(20/9\)。改善的是在相同原数据下的统一证书，固定图最优需要另证。

**任取合法参数仍保持轨道。** 以上任一认证给 \([\lambda_0,\infty)\) 的统一 \(a\le rt\) 和统一 \(s\le t/\sqrt{1-\mu^2}\)。从 \(x^0\in U\) 且
\[
\frac{d(x^0,S)}{(1-r)\sqrt{1-\mu^2}}<d(x^0,U^c)
\]
出发，每个 \(\lambda_k\ge\lambda_0\) 和每条允许选择轨道均由有限前缀证明留在 \(U\)，并点收敛于 \(S\cap U\)，尾长至多 \(d(x^k,S)/[(1-r)\sqrt{1-\mu^2}]\)。若连续性和原图条件都全局成立，可用同一个球面论证对每个输入取得根；此时取完整允许关系，无初值位置门。局部声明只管指定球内的根；结论允许逐步更换参数，未规定一个可观察的最优步长搜索。

<a id="dd-parameter-small-step-examples"></a>
## C481 · 小步极限、固定阈值和文献对照的例子

**每个参数都可解，仍有小步扩张。** 令 \(Q\) 为平面直角旋转，\(F(y)=(-I+2Q)y\)，\(S=\{0\}\)。\(\|F(y)\|=\sqrt5\|y\|\)，\(\langle F(y),y\rangle=-\|y\|^2\)，故原角常数与线性误差界常数均为 \(1/\sqrt5\)。\(I+\lambda F=(1-\lambda)I+2\lambda Q\) 是尺度为 \(\sqrt{1-2\lambda+5\lambda^2}\) 的旋转伸缩，对每个 \(\lambda>0\) 满射双射。原近端距离比为倒数，严格下降恰在 \(\lambda>2/5\)。实际最小锚缺陷比 \(\sigma_\lambda=\lambda/(1-2\lambda+5\lambda^2)\to0\)。DD1 按实际 \(\sigma_\lambda\) 代入的能量因子等于真实距离比。对同一图，Luke–Tam Definition 2 的原图点对也可直接算出此 \(\tau_\lambda\)；式 (29) 与输出残差导出的能量估计相同。其 Theorem 2 明写的兼容门在 \(\lambda=1/2\) 失败、在 \(\lambda=11/5\) 通过，故不能拿这个明确算子的 \(2.2\) 作明写门分离。附件提及的另一未标明旋转算子不作引用。

**每一步严格下降与变步有限长度。** 若 \(F=Q\)，原根唯一满域，\(t_{k+1}/t_k=(1+\lambda_k^2)^{-1/2}\)。取 \(\lambda_k=1/\sqrt{k+1}\)（\(k\ge0\)），则 \(t_k=t_0/\sqrt{k+1}\)，\(s_k=\lambda_k t_{k+1}\) 与 \(1/k\) 同阶。该轨道趋于零且有无限长度；取 \(\sum_k\lambda_k^2<\infty\) 时距离保持正极限。固定步可任意小和变步量趋零有不同的累计进展问题。

**相对于 Luke–Tam 图条件的结构分离。** \(F(0)=0\)、\(F(y)=(2+\sin(1/|y|))y\)（\(y\ne0\)），连续、精确零集 \(\{0\}\)、\(\ell=1,\mu=0\)。\(H_\lambda(y)=y+\lambda F(y)\) 与 \(y\) 同号且 \(|H_\lambda(y)|\ge(1+\lambda)|y|\)，连续并向两端发散，完整覆盖。实际全输出满足 \(|y|\le |x|/(1+\lambda)\)，而压成 DD1 证书给 \(1/\sqrt{1+\lambda^2}\)。任意 \(\lambda>0\)，\(H_\lambda'(y)\) 在正半轴趋零时反复变号，故在每个小正区间非单射。近零同输入的两个不同输出 \(y_1,y_2\) 使 \(\langle y_1-y_2,\lambda F(y_1)-\lambda F(y_2)\rangle=-|y_1-y_2|^2\)，但 Luke–Tam Definition 2 的右端为零。两图点及其图值均可落入任何原点图窗，故其全对前件无法直接用于该完整原图。正锚条件和连续有限维覆盖已有其他方法可用，本例只承担指定假设的分离。
