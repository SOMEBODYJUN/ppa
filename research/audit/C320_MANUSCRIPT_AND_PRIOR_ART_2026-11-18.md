# 方向残差集合的 PPA 收敛定理与文献定位

本页给出可独立阅读的普通 PPA 定理、假设强弱和文献比较。\(M_{\rm dir}\) 是固定 Dini 时的结构条件；\(M_{\rm pt}\) 是以两步净位移替代 Dini 后的点收敛条件。两者沿用 [C319/C320 的已证身份](../canonical/ppa_two_step_and_directional_residual.md#td-combined)。

<a id="m-setting"></a>
## 1. 对象、共同假设与精确量词

设 \(X=\mathbb R^n\) 赋予欧氏范数，\(F:X\rightrightarrows X\)，\(S\subseteq\{z:0\in F(z)\}\) 非空且闭。取开集 \(U\subseteq X\) 且 \(S\cap U\ne\varnothing\)，\(\lambda>0\)、\(R>0\)、\(0<\kappa<1\)。记
\[
d(x)=\operatorname{dist}(x,S),\quad
U_R=\{x\in U:d(x)\le R\},\quad
J_{\lambda F}(x)=\{y:x-y\in\lambda F(y)\}.
\]
对每个 \(x\in U_R\)，给定非空的允许输出集 \(\mathcal J(x)\subseteq J_{\lambda F}(x)\)，并令 \(Y=\bigcup_{x\in U_R}\mathcal J(x)\)。若要证明完整 PPA 的全部轨道，取 \(\mathcal J(x)=J_{\lambda F}(x)\) 对每个 \(x\in U_R\) 成立。局部覆盖另列为假设。

取有限非减函数 \(\omega:[0,R]\to[0,\infty)\)，要求 \(\omega(0)=0\) 且在 \(0\) 连续。记 \(H(t)=(t+\omega(t))/2\)。以下 P2、P3 的定义与 [正式稿](../../发表成果整理/RLEB/sections/theorem_spine.tex) 一致。

- **最近零锚 P2。** 对每个 \(x\in U_R\) 和每个 \(y\in\mathcal J(x)\)，存在 \(p\in S\) 满足 \(\|x-p\|=d(x)\) 及
  \[
  \|2y-x-p\|\le \omega(d(x)).
  \]
  \(p\) 可以依赖于 \(x,y\)。该式与正式稿的内积式等价，因为 \(\|2y-x-p\|^2=d(x)^2-4\langle y-p,x-y\rangle\)。
- **真残差误差界 P3。** 固定 \(\bar s>0\) 及有限非减、零处连续且 \(\psi(0)=0\) 的 \(\psi:[0,\bar s]\to[0,\infty)\)，使 \(H(R)/\lambda\le\bar s\)。对每个 \(y\in Y\)，若 \(r_F(y)=\inf_{v\in F(y)}\|v\|\le\bar s\)，则 \(d(y)\le\psi(r_F(y))\)。\(r_F\) 取自完整纤维。

<a id="m-direction"></a>
## 2. 方向残差条件与最小检验

对每个 \(t\in[0,R]\)，从已指定的允许关系中形成集合
\[
V_t=\{(x-y)/\lambda: x\in U_R,\ d(x)\le t,\ y\in\mathcal J(x)\}.
\]
定义 \(M_{\rm dir}\) 为共同覆盖、P2、P3 与以下条件的合取。**存在一族** \((K_t)_{t\in[0,R]}\) 以零为中心的闭对称凸集，满足
\[
\begin{aligned}
 &0\le s\le t\le R \ \Longrightarrow\ K_s\subseteq K_t,\\
 &V_t\subseteq K_t\subseteq\overline B(0,H(t)/\lambda)\qquad(0\le t\le R),\\
 &\forall t\in[0,R]\ \forall y\in Y:
       F(y)\cap K_t\ne\varnothing\ \Longrightarrow\ d(y)\le\kappa t .
\end{aligned}\tag{M}
\]
最后一行检查的是：某个输出 \(y\) 的完整纤维有一个图值进入该尺度的包络，就必须落在更小的距离层。这个图值可以来自另一输入，甚至来自当前工作窗外的输入。交叉检查的对象是 \(y\in Y\)，并非所有 \(y\in X\)。

**最小集合。** 可直接取
\[
 C_t=\overline{\operatorname{conv}}\bigl(\{0\}\cup V_t\cup(-V_t)\bigr).
\]
由 P2 及 \(2(x-y)=(x-p)-(2y-x-p)\)，有 \(\|x-y\|\le H(d(x))\)。所以 \(C_t\) 嵌套且位于规定的闭球中。任一合格的 \(K_t\) 都含 \(C_t\)，因此 (M) 等价于用这族唯一确定的 \(C_t\) 验证最后一行。闭凸包可能把两个实际步的图值或其相反向量组合成一个新向量，故最后一行比逐独立步检查 A 多出真正的跨输出限制。

<a id="m-support"></a>
### 等价的线性分离检验

设 \(\sigma_t(u)=\sup(\{0\}\cup\{|\langle u,w\rangle|:w\in V_t\})\)。在 P2 下，(M) 等价于
\[
 \forall t\in[0,R]\ \forall y\in Y\ \bigl[d(y)>\kappa t
 \ \Longrightarrow\ \forall v\in F(y)\ \exists u\in X,\ \|u\|=1:
 |\langle u,v\rangle|>\sigma_t(u)\bigr].\tag{S}
\]
因为 \(C_t\) 闭、凸、有界且包含原点，对 \(v\notin C_t\) 可取严格分离方向 \(u\)（例如用投影点 \(P_{C_t}v\) 得到）。对称性及线性泛函在闭凸包上的上确界给 \(\sup_{w\in C_t}\langle u,w\rangle=\sigma_t(u)\)。反之该严格不等式排除 \(v\in C_t\)。方向允许依赖于尺度、输出与图值。应用中可尝试用切向/法向分解、有限个支撑方向或可计算的外包验证此式，且对应的验证必须覆盖全部相关输出纤维。

<a id="m-theorem"></a>
## 3. 收敛定理与证明

**定理 1（方向残差条件下的有限长度）。** 假设 \(M_{\rm dir}\)，并假定
\[
 \int_0^R\frac{\omega(t)}t\,dt<\infty,\qquad
 \Theta(t)=\sum_{j=0}^\infty H(\kappa^jt).
\]
对任意 \(x^0\in U_R\)，若 \(\Theta(d(x^0))<\operatorname{dist}(x^0,X\setminus U)\)，则按 \(x^{k+1}\in\mathcal J(x^k)\) 选取的每一条轨道均可无限延拓、留在 \(U_R\)，并收敛到 \(x^\infty\in S\cap U\)。对每个 \(k\ge0\)，
\[
 d(x^k)\le\kappa^k d(x^0),\qquad
 \|x^k-x^\infty\|\le\sum_{j=k}^{\infty}\|x^{j+1}-x^j\|
       \le\Theta(d(x^k)).
\]
约定到空集的距离为 \(+\infty\)。

证明：任取 \(x\in U_R\) 和 \(y\in\mathcal J(x)\)。令 \(t=d(x)\)，则 \((x-y)/\lambda\in F(y)\cap K_t\)，所以 (M) 给 A，P2 给 B。由于 \(\omega\) 非减，几何分割区间上的积分与端点值比较给出 \(\sum_j\omega(\kappa^jR)<\infty\)，故 \(\Theta\) 有限。对每个已生成的有限前缀，A 保证下一输出距离至多 \(R\)，B 保证到初值的累计位移小于开窗余量，故下一点仍在 \(U_R\)。覆盖使归纳可继续，对每条选择均成立。沿已得到的无限轨道从任意 \(k\) 求和得到尾界。尾和有限给 Cauchy 性，闭集 \(S\) 和严格开窗余量分别把极限定位在 \(S,U\)。

**定理 2（两步净位移下的点收敛）。** 以 \(M_{\rm pt}\) 表示 \(M_{\rm dir}\) 加上以下条件。存在有限非减 \(W:[0,R]\to[0,\infty)\)，\(W(0)=0\) 且在零处连续，使对每个 \(x,y\in U_R\)、\(y\in\mathcal J(x)\) 和每个 \(z\in\mathcal J(y)\)，有
\[
 \|z-x\|\le W(d(x))-W(d(z)).
\]
这里 \(d(z)\le\kappa d(y)\le R\) 由 A 得到，尚不要求 \(z\in U\)。记 \(d_0=d(x^0)\)。若
\[
 \max\{W(d_0),H(d_0)+W(\kappa d_0)\}<\operatorname{dist}(x^0,X\setminus U),
\]
则从 \(x^0\in U_R\) 出发的每条允许轨道均可无限延拓、留在 \(U_R\)，并收敛到 \(S\cap U\) 中一点。对每个 \(k\ge0\)，
\[
 \|x^k-x^\infty\|\le\sum_{j\ge0}\|x^{k+2j+2}-x^{k+2j}\|\le W(d(x^k)).
\]
证明：对任一有限前缀沿奇偶两类子序列分别求和。偶数点距 \(x^0\) 至多 \(W(d_0)\)，奇数点距 \(x^1\) 至多 \(W(d(x^1))\)，故距 \(x^0\) 至多 \(H(d_0)+W(\kappa d_0)\)。严格预算使下一点仍在工作窗，覆盖归纳成立。偶子序列有限长，B 给 \(\|x^{2j+1}-x^{2j}\|\to0\)，合并即得同一个极限。自任意 \(k\) 开始同样求和给尾界。单步原轨道允许无限长度，甚至允许步长平方和发散，见 [完整图的严格分离](../canonical/ppa_two_step_and_directional_residual.md#td-links)。

P3 在两项新定理的直接证明中没有被调用。保留它使新旧结构的比较锁定同一个真残差条件。若以后为省假设而从定理删除 P3，应另行声明更弱版本，并保留其与旧条件的比较。

<a id="m-strength"></a>
## 4. 相对于旧 RLEB 和 A+B 的精确强弱

旧结构用标量兼容 \(\psi(H(t)/\lambda)\le\kappa t\)（所有 \(t>0\)）。用原闭球 \(K_t=\overline B(0,H(t)/\lambda)\) 时，若 \(F(y)\cap K_t\ne\varnothing\)，则 \(r_F(y)\le H(t)/\lambda\le\bar s\)。P3、单调性和旧兼容即给 (M)。因此固定 Dini 时，有
\[
 \text{旧结构包}\ \Longrightarrow\ M_{\rm dir}\ \Longrightarrow\ A+B.
\]
对旧完整包，\(\Theta(t)=H(t)+\Theta(\kappa t)\) 给逐步望远镜，故取 \(W=\Theta\) 推出 \(M_{\rm pt}\)，并准确恢复旧初值预算。反过来，若 Dini 已是共同假设，任何 A+B 都可取这个两步势。固定 Dini 下的严格性来自 (M) 本身。

两个反向都失败，即使固定 P2、P3、Dini、\(\lambda=R=1\)、\(\kappa=3/4\) 和同一 \(\psi(s)=3s/2,\omega(t)=t+2\sqrt t\)。第一项构造中，正侧的大切向分量拉大旧球半径，负侧的线性残差破坏旧兼容；法向方向保留后，(M) 仍成立。第二项构造中，所有实际步都满足 A+B，但相反方向的另一个图值被对称包络纳入后，其逆像落在过远的位置。这说明 (M) 比 A+B 多的内容确实是跨输入的图值排除。两例均是完整原算子上的严格见证。[参数与逐式核对](../canonical/ppa_two_step_and_directional_residual.md#td-directional)

为逐项核对上一段，取 \(X=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\)、\(U=X\)、\(\bar s=2\)，用 \(F=T^{-1}-I\) 将以下全域双射实现为完整近端。

- 取 \(T(a,b)=(a+\sqrt{b_+},3b/5)\)。实际图值为 \(v=(-\sqrt{b_+},2b/5)\)，输出距离为 \(3|v_2|/2\)。取 \(K_t\) 为盒 \([-\sqrt t,\sqrt t]\times[-2t/5,2t/5]\) 与规定闭球的交。它覆盖 \(V_t\)；逆像输出距离由法向图值给出，至多 \(3t/5\)。锚定反射范数不超过 \(2\sqrt t+t/5\)，故 P2 成立，\(d(y)\le 3r_F(y)/2\) 给 P3。任意有效锚定模在正侧至少 \(2\sqrt t\)，任意有效真残差标尺在负侧的小残差上至少 \(3s/2\)，故旧兼容左端至少 \(3\sqrt t/2\)，在任意缩窗都失败。
- 取 \(T(a,b)=(a,q(b)b)\)，正侧 \(q=1/5\)，负侧 \(q=3/5\)。每步满足 A、B，锚定反射范数至多 \(3t/5\)，而 \(d(y)\le 3r_F(y)/2\)，故同 P2、P3、Dini 仍成立。正高 \(b=t\) 的图值 \((0,4t/5)\) 必进 \(K_t\)。对称性也纳入 \((0,-4t/5)\)，它在负高 \(b=-2t\) 被实际使用，输出距离 \(6t/5\) 超过 \(\kappa t\)。

<a id="m-gauge"></a>
## 5. 与广义残差、投影残差的抽象关系

给定最小族 \(C_t\)，定义扩展值函数
\[
 g_C(v)=\inf\{t\in[0,R]:v\in C_t\},\qquad \inf\varnothing=+\infty .
\]
则 (M) 最后一行等价于
\[
 d(y)\le\kappa\inf_{v\in F(y)}g_C(v)\qquad(y\in Y).
\]
正向对每个包含 \(v\) 的尺度取下确界，再对 \(v\) 取下确界；反向若 \(v\in F(y)\cap C_t\)，则 \(g_C(v)\le t\)。这一等价不要求任一个下确界达到。\(g_C(0)=0\)，对 \(v\ne0\) 为正或 \(+\infty\)，因为 \(\|v\|\le H(t)/\lambda\) 排除了尺度趋零。它可视为图值侧的非径向残差函数，不能因此自动套用既有文献的有限性、Lipschitz 或线性下界判据。举例说，§4 第一例的 \(v_t=(-\sqrt t,2t/5)\in C_t\)，故 \(g_C(v_t)/\|v_t\|\le\sqrt t\to0\)。

固定线性观察 \(L\) 是一种验证方式。若 \(\chi,\rho\) 为非减模，且 \(d(y)\le\chi(\inf_{v\in F(y)}\|Lv\|)\) 对每个 \(y\in Y\) 成立，每个受检步满足 \(\|L((x-y)/\lambda)\|\le\rho(d(x))\)，以及 \(\chi(\rho(t))\le\kappa t\)，则取 \(K_t=\overline B(0,H(t)/\lambda)\cap\{v:\|Lv\|\le\rho(t)\}\) 得 (M)。这时 \(\inf_{v\in F(y)}\|Lv\|=\operatorname{dist}(0,(L\circ F)(y))\)，是在复合映射上的普通残差。零集的保持需要结合指定的目标和工作窗核查。

<a id="m-beyond-projection"></a>
### 严格超出任一固定线性观察的局部完整例

取 §4 第一例的 \(T_0(a,b)=(a+\sqrt{b_+},3b/5)\)，令 \(F_0=T_0^{-1}-I\)，取 \(U=(-1,1)\times\mathbb R\)，其他参数同 §4。令
\[
 F(y)=
 \begin{cases}
  \{F_0(y),10 e_1\},&y\in[-2,2]\times[-1,1],\\
  \{F_0(y)\},&\text{其他 }y .
 \end{cases}
\]
这是闭图关系，且零集不变。新增图值的输入 \(y+10e_1\) 的第一坐标至少为 8，因而 \(U_R\) 上完整近端仍是 \(T_0\)。新增图值在所有外球之外（该窗 \(H(t)\le2\)），所以 (M) 原封成立。它也大于实际步长，P3 的真残差不变。

设 \(L\) 是任一固定线性观察，记 \(\ell_i=\|Le_i\|\)。若 \(\ell_1=0\)，在新增支适用的非零高度输出有 \(r_L=0<d(y)\)。若 \(\ell_2=0\)，负侧的原图值也给 \(r_L=0<d(y)\)。若两者均正，负侧高度从零连续变化时，由于新增支的观察残差为常数 \(10\ell_1>0\)，充分小的观察残差仍来自原法向支，故任一误差标尺 \(\chi\) 都有 \(\chi(s)\ge 3s/(2\ell_2)\) 对全部充分小 \(s>0\)。正侧的原图值满足
\[
 \|L(-\sqrt t,2t/5)\|\ge\ell_1\sqrt t-2\ell_2t/5 .
\]
该观察残差趋零，最终也小于 \(10\ell_1\)，故任何有效包络 \(\rho\) 即使只需要上界真正的 \(r_L\)，仍迫使 \(\chi(\rho(t))\) 至少为平方根阶，无法被 \(\kappa t\) 控制。正负两列合法步可取任意趋近原点的小尺度，因此在任意缩小的原点工作窗都失败。这个分离针对在完整 \(F(y)\) 上评价的固定线性观察，另加图值截断会改变所比较的对象。

<a id="m-prior-art"></a>
## 6. 先行研究与可移植的方法

检索截至 2026-11-18。查询覆盖普通、非线性和各向异性 PPA，广义/方向/复合映射次正则，图值凸包与逆像误差界，以及多步 Lyapunov 方法。查阅了下列作者稿、arXiv 原文或出版页面。检索限于公开可取得的版本，不能裁定全网或全部文献的首创性。

| 研究与原文位置 | 已有方法 | 与本定理的关系 |
|---|---|---|
| A. Y. Kruger, *Nonlinear Metric Subregularity*, §4.1 式 (22)–(23)、§4.4 Theorem 4.1，JOTA 2016。 [全文](https://arxiv.org/pdf/1502.06159) | 以图值函数 \(g(v)\) 取代欧氏残差的径向外层修正，再用原空间斜率、次梯度和余导数给出误差界判据。 | 这是最接近的抽象先例。式 (23) 与 §5 的 \(g_C\) 不等式同型。其后所用的有限性、局部 Lipschitz 和 (P2′) 的正线性下界不能自动导入 \(g_C\)；§5 给出比值趋零的实际图值。核读的定理未规定由普通 PPA 的可达图值生成 \(C_t\)、也未给出两侧的 RLEB 严格比较。 |
| T. Valkonen, *Preconditioned Proximal Point Methods and Notions of Partial Subregularity*，J. Convex Anal. 2021，Definition 4.2、Lemma 4.4、Example 4.6 和 §5。 [作者稿](https://tuomov.iki.fi/mathematics/subreg.pdf) · [刊本](https://journalofconvexanalysis.com/articles/jca28017/) | 以半正定算子对误差及到解集的平方距离加权，形成部分次正则 (PSR)。把部分误差界放入测试后的预条件 PPA 递推；Example 4.6 还讨论单调普通 PPA。§5 用结构投影和 Young 不等式与部分强次单调互证。 | 这是最接近的 PPA 先例。部分度量和只控制相关方向均已有研究。其 Definition 4.2 使用算子参数的平方距离；本定理用普通 PPA 的实际图值生成可随尺度改变的集合，并做完整逆像排除。§5 的分离覆盖固定线性观察的特定合同，并未证明排除 Valkonen 的全部部分次正则算子合同。 |
| H. Gfrerer, *On Directional Metric Subregularity and Second-Order Optimality Conditions for a Class of Nonsmooth Mathematical Programs*，SIAM J. Optim. 2013。M. Benko、H. Gfrerer、J. V. Outrata 的 *Stability Analysis for Parameterized Variational Systems with Implicit Constraints*，Definition 2.5、Theorem 2.6。 [Gfrerer 作者稿](https://numa.jku.at/media/filer_public/3c/f1/3cf151fd-c2b7-40d9-99fa-88fbc50a13c5/2012-07.pdf) · [方向定义全文](https://library.utia.cas.cz/separaty/2019/MTR/outrata-0506147.pdf) | 沿指定方向或锥形邻域检验误差界，使用图导数、方向余导数及一阶或二阶判据。 | 方向信息及其分析工具已有体系。这里是按尺度从**实际近端图值**生成值域集合，并排除完整逆纤维中的坏输出。方向余导数适合寻找验证这项排除的充分条件，须另证明与 (S) 的关系。 |
| D. R. Luke、N. H. Thao、M. K. Tam, *Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings*，作者 v2，Theorem 2.15、Definition 2.17、Theorem 2.18，MOR 2018。 [作者稿](https://num.math.uni-goettingen.de/~rluke1/publications/1605.05725v2.pdf) | 几乎平均性与 \(T-\mathrm{Id}\) 的相对误差界配合，得到到固定点集的距离收缩。 | 这是最接近的收敛框架之一。收敛后端有明确先例。本定理的独立部分是使用原 \(F\) 的完整纤维和受检近端图值所生成的集合推出 A；其中一个严格例的反射映射没有两点线性模。与 Luke–Tam 后来的普通 PPA 定理整套条件不可比。 |
| G. Li、B. S. Mordukhovich、J. Zhu, *Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods*，arXiv v1，Definition 3.1、Theorem 4.3、Theorem 5.1。 [原文](https://arxiv.org/html/2406.13207v1) | 用解集距离侧的函数与欧氏次梯度残差配合；抽象框架把缩减序列、实际位移代理和能量差联系起来，并由 KL 版本结出有限长度。 | 标量非线性误差界、模型函数迭代与望远镜均有先例。它的欧氏残差条件未保留由近端图生成的 \(C_t\)；定理 2 的无限长度子类超出其有限长度结论所覆盖的范围。编号仅对应已读 v1。 |
| E. Laude、P. Patrinos, *Anisotropic Proximal Point Algorithm*，arXiv:2312.09834v4，§1、式 (4.1)、Proposition 4.1 及式 (4.13)。 [原文](https://arxiv.org/pdf/2312.09834v4) | 用 Legendre 梯度在对偶空间非线性预条件，定义各向异性预解式，利用 Bregman–Fejér 结构分析收敛。其速率分析使用原算子的 Hölder 型逆增长界。 | “各向异性 PPA”已有专门含义，论文中应避免沿用这个名称。这里保留欧氏近端更新，各向异性只出现在用于认证收缩的集合 \(K_t\)。 |
| J. H. Alcantara, *Degenerate Preconditioned Proximal Point Algorithms as Forward Methods for Nonmonotone Inclusions*，2026-11-16 arXiv v1，§§4.1–4.3、§4.5。 [原文](https://arxiv.org/html/2611.20523v1) | 在退化预条件器的值域中约化迭代，用解相对半单调与误差界处理投影收敛，再用恢复条件推及原空间点。 | 说明方向筛选和全空间恢复是活跃问题。这里 \(K_t\) 只用于原图认证，迭代本身不做值域约化。查阅段落未给出同一最小可达图值凸包条件。 |
| N. Noroozi、R. Geiselhart、L. Grüne、F. R. Wirth, *Control of Discrete-Time Nonlinear Systems via Finite-Step Control Lyapunov Functions*，Definition 6、Proposition 8。 [原文](https://arxiv.org/pdf/1908.09660) | 在 \(M\) 步后下降，而非强制每一步下降，并约束块内中间状态。 | 按块证明有明确先例。本定理中的额外信息是原 PPA 图的两步**位置净位移**可求和，以及允许一步平方和发散的同结构对照。仅控制到目标集的有限步距离并不能锁定零集中的一个极限点。 |

**检索结论。** 所查原文中，有广义非径向残差、指定方向的次正则、算法映射的相对误差界、非欧氏预解式和多步稳定性。未发现同一结果同时要求：(i) 用普通 PPA 在各输入距离尺度的可达原图值生成最小闭对称凸包；(ii) 对所有相关输出的完整纤维做交叉排除；(iii) 在同一 Dini、窗口、原更新和线性误差界基线下证明严格介于正式 RLEB 与 A+B。§5 的新分离说明固定全纤维投影误差界不能覆盖这一集合条件，但未排除一般化误差界文献中的等价改写。

**纳入论文的判断。** 可将定理 1 作为主定理之后的结构推广，贡献重点放在由原图生成的最小集合、等价分离检验与两个严格蕴含。定理 2 的结论是点收敛，可放在独立小节讨论取消 Dini 的代价和边界。若作为全文主贡献，仍需一个来自实际问题原算子的验证例，展示如何先验得到支持方向或两步相消；仅从一个设计好的预解映射反演原图主要验证可行性与逻辑严格性。统一弱化 Luke–Tam 和正式 RLEB 仍是另一个目标。本页的比较结果不足以据此宣称首创一般方向次正则或多步 Lyapunov 方法。
