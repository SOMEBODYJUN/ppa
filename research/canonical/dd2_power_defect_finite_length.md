# DD2 的幂次缺陷、Hölder 误差界与有限长度

<a id="dd2-power-defect"></a>
## C399-v1 · 普通 PPA 的同一步长度估计

固定有限维欧氏空间、\(\lambda>0\)、非空闭 \(S\subseteq\operatorname{zer}F\)、开集 \(U\) 和 \(R_0>0\)。设允许关系 \(\mathcal J(x)\subseteq J_{\lambda F}(x)\) 在 \(x\in U,\ d(x,S)\le R_0\) 时非空。要求对每个此类 \(x\) 及每个 \(y\in\mathcal J(x)\)，至少有一个最近锚 \(z\in P_S(x)\) 使

\[
\langle x-y,y-z\rangle\ge-Md(x,S)^p,
\qquad
d(y,S)\le K r_F(y)^q,\qquad r_F(y)=\inf_{v\in F(y)}\|v\|.
\tag{1}
\]

取 \(K>0,\ M\ge0,\ p>0,\ 1/2<q<1\)。若 \(M=0\)，或 \(p>2/q\)，或 \(p=2/q\) 且 \(2M<\lambda^2K^{-2/q}\)，则存在 \(0<R\le R_0\) 与 \(C,\gamma>0\)，使每条 \(d(x,S)\le R\) 的允许步满足

\[
\|x-y\|\le C[d(x,S)^\alpha-d(y,S)^\alpha],\quad
d(y,S)\le d(x,S)-\gamma d(x,S)^{1+\nu},
\qquad
\alpha=2-1/q,\quad \nu=2/q-2.
\tag{2}
\]

若 \(d_0=d(x^0,S)\le R\) 且 \(Cd_0^\alpha<d(x^0,U^c)\)，则每个允许选择轨道均可续接，且保持在工作窗。总长至多 \(Cd_0^\alpha\)，第 \(k\) 步起的尾长至多 \(Cd_k^\alpha\)，轨道收敛到 \(S\cap U\)。有 \(d_k=O(k^{-1/\nu})\) 及 \(\|x^k-x^\infty\|=O(k^{-\alpha/\nu})\)。

**证明。** 写 \(t=d(x,S)\)、\(a=d(y,S)\)、\(s=\|x-y\|\)、\(h=K/\lambda^q\)。平方展开与最近性给

\[
a^2+s^2\le t^2+2Mt^p,\qquad a\le h s^q,\qquad t\le a+s .
\tag{3}
\]

第一项使 \(s\) 随 \(t\downarrow0\) 一致趋零。对任意固定 \(0<c<h^{-1/q}=\lambda K^{-1/q}\)，缩窗使 \(h+s^{1-q}\le c^{-q}\)，由 \(t\le h s^q+s\) 得 \(s\ge c t^{1/q}\)。三种门中均可选定 \(c\)、\(0<\delta<1\) 及小窗，使 \(2Mt^p\le(1-\delta)c^2t^{2/q}\le(1-\delta)s^2\)。因此 \(t^2-a^2\ge\delta s^2\)。若 \(t>0\)，这给出严格下降及

\[
t-a\ge \frac{\delta c^2}{2}\,t^{2/q-1},\qquad
s\le\frac{2}{\delta c}t^{1-1/q}(t-a)
\le\frac{2}{\alpha\delta c}(t^\alpha-a^\alpha).
\]

最后一步用 \(u^\alpha\) 的凹性。当 \(t=0\)，(3) 强制 \(s=a=0\)。对任意有限前缀，(2) 的望远镜预算保证新输出仍在 \(U\) 且距离不增，故覆盖假设可归纳使用。全程留在以 \(x^0\) 为中心、半径 \(Cd_0^\alpha\) 的闭球内，球包含于 \(U\)。有限长度给 Cauchy 极限，距离递推及 \(S\) 闭给极限属于 \(S\)。对正距离用 \(u^{-\nu}\) 的凸性得 \(d_{k+1}^{-\nu}-d_k^{-\nu}\ge\nu\gamma\)。遇零后驻定。尾预算代入距离率即得点误差率。

这个证明使用同一步的实际 \(s\)。只将 (3) 的独立步长上包络 \(O(t)\) 与距离上界逐项相加，通常得不到这里的全指数范围。形式上的距离模可取 \(t-\gamma t^{1+\nu}\)，充分缩窗后它非负、非减，且其与 \(t\) 的比趋于 1。

<a id="dd2-power-witnesses"></a>
## 边界与严格实例

**临界缺陷常数。** 设 \(0<q<1\)，\(c_*=\lambda K^{-1/q}\)，固定小 \(\varepsilon>0\) 使 \(c_*\varepsilon^{1/q-1}<2\)。在平面上以 \(R_\theta\) 表示旋转，取

\[
T(x)=R_{\theta(\|x\|)}x,\qquad
\theta(r)=2\arcsin\bigl(c_*\min(r,\varepsilon)^{1/q-1}/2\bigr),\qquad
F=(T^{-1}-I)/\lambda .
\]

\(T\) 保半径，逐圆反向旋转即得连续全域逆。原算子连续单值，唯一零点为 \(0\)，完整 \(J_{\lambda F}=T\)。在 \(0<t\le\varepsilon\) 时，\(a=t,\ s=c_*t^{1/q}\)，故 (1) 的 EB 取等，内积为 \(-c_*^2t^{2/q}/2\)。当 \(p=2/q,\ 2M\ge c_*^2\) 时立即满足 (1)。当 \(p<2/q,\ M>0\) 时缩窗也满足 (1)。所有任意小非零轨道保半径。它复用 [C392 的保半径构造](../topics/common_structure/angle_residual_exponent_balance.md#angle-residual-exponent-balance)，这里固定的是输入距离幂次缺陷及其常数。

**半阶端点。** 取 \(\lambda=K=1\)，\(F(y)=\|y\|Jy\)，其中 \(J\) 是逆时针直角旋转。\(S=\{0\}\)，零锚内积恒为零，完整真残差为 \(\|y\|^2\)。\(\|y+F(y)\|=\|y\|\sqrt{1+\|y\|^2}\) 严增且值域为 \([0,\infty)\)，每个半径上的映射是旋转，因此全域近端唯一。非驻定轨道的正半径 \(d_k\downarrow0\) 且

\[
d_{k+1}^{-2}-d_k^{-2}=(1+d_{k+1}^2)^{-1}\longrightarrow 1,\qquad
\|x^{k+1}-x^k\|=d_{k+1}^2\sim 1/k .
\]

故轨道收敛而无限长。缩到残差不超过 1 后同一模型满足每个 \(0<q\le1/2\) 的误差界。

**超出线性正则与固定收缩的非单调实例。** 取 \(\lambda=1,\ S=\{0\}\) 及 \(F(y)=-r y+r^{1/3}Jy\)，\(r=\|y\|\)。真残差为 \(r^{4/3}\sqrt{1+r^{4/3}}\)，故 \(q=3/4,\ K=1\) 成立，线性误差界失效。内积 \(\langle F(y),y\rangle=-r^3\) 说明 \(F\) 非单调。输入半径为

\[
H(r)=r\sqrt{(1-r)^2+r^{2/3}}.
\]

\(H(r)\ge r^{4/3}\) 排除小输入的远根。\(H'(r)\to1\) 给小半径严格增性与覆盖，其方位关系为旋转，故充分小输入的完整近端唯一。小正 \(r\) 有 \(H(r)>r\) 和 \(H(r)/r\to1\)，所以 \(p=3,\ M=1\) 成立，且每个充分小非零轨道的距离比趋于 1。取对数后用 Cesàro 平均得 \(d_k^{1/k}\to1\)，故 R 线性距离率也失效。输入侧残差 \(r_{\mathrm{Id}-J_F}(x)\) 与输出侧残差 \(r_F(y)\) 相同地为 \(o(d(x,S))\)。该例分离的是线性速率假设及结论。它的 \(\langle F(y),y\rangle/\|F(y)\|^2\to0\)，故局部允许任意小的负弱 Minty 常数。

## 与相关定理的范围

- [C309](ppa_nonlinear_gauge_and_coupled_obstruction.md#c309-theorem) 接受已经给定的距离模和独立尾和条件。这里从同一步的锚定缺陷和输出真残差直接推出幂势。一般函数包络的存在与沿轨道有限长度仍是两个证明义务。
- [C212](generalized_ppa_modulus.md#gpm-strict) 的非负锚定壳层估计与 Li–Mordukhovich 2012 的极大单调 PPA 已能推出 \(q>1/2\) 的有限长度。此处确定的是一个允许负缺陷的输入距离条件、其临界常数及同一步尾势。对完整公开文献的优先性未判定。[一手定位与比较](../LITERATURE.md#lit-alcantara-dd)
- [C285](rleb_sharp_linear_frontier.md#rsl-threshold) 的任意闭集固定二次分段锐门仍独立成立。这里的幂次有限长度结论限于普通 PPA，退化 PPPA 的核方向恢复另需条件。
