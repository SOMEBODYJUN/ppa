# GPPA 的物理提升：核距离、点尾和长度是三个不同结论

本页直接证明一般模 GPPA 的物理变量接口，并给出同一完整关系上的锐边界。固定比较原文为 [arXiv:2608.01584v1](sources/gppa_2608.01584v1.pdf)，Definition 3、Theorem 2（印刷 pp.5–8）。该文的 adaptive strong monotonicity 是对 **pair** \((F,v)\) 的条件；本页另用的强单调性是对 **kernel 本身** \(v\) 的条件，两者不能替换。本页不宣称全球先行性。

<a id="gp-data"></a>
## 1. 固定完整对象、真残差与物理输出领圈

令 \(H\) 为实 Hilbert 空间，\(F:H\rightrightarrows H\) 是固定完整关系，\(v:H\to H\) 单值，\(\lambda>0\)。物理 GPPA 的一次允许转移为

\[
v(x)-v(y)=\lambda f,\qquad f\in F(y).
\tag{GP1}
\]

记 \(S\subseteq\operatorname{zer}F\) 非空闭，\(Z=v(S)\) 非空闭，\(r(x)=d(v(x),Z)\)，而

\[
r_F(y)=\inf_{f\in F(y)}\|f\|.
\tag{GP2}
\]

\(r(x)\) 是核零像的距离，不是物理零集距离，也不是所选步长。所选图值只给

\[
r_F(y)\le\|f\|=\|v(x)-v(y)\|/\lambda.
\tag{GP3}
\]

以下假设使用同一 \(F,v,S,\lambda\)。设 \(U\subseteq H\) 开，\(E\subseteq H\) 是一个物理输出领圈，\(U\subseteq E\)。在 \(U_R=\{x\in U:r(x)\le R\}\) 的每个输入上，指定的允许转移非空，并且全部允许输出属于 \(E\)。若结论拟授予完整 warped resolvent，必须把这里的“允许”逐输入等同于完整 \((v+\lambda F)^{-1}(v(x))\)；一个好截面不能代替全部输出的认证。

输出领圈是实质条件：在证明输出留在 \(U\) **之前**，需要对输入及其输出应用下面的反演模。只在 \(U\times U\) 有反演界、又未独立保证输出在 \(U\)，会形成留域证明的循环。

<a id="gp-one-step"></a>
## 2. 从真物理 EB 到核收缩的一次推导

设 \(\omega:[0,R]\to[0,\infty)\) 连续非减，\(\omega(0)=0\)。在同一认证图及所用零图点上要求核全对反射条件

\[
\|v(y)-v(p)-\lambda(f-0)\|
\le\omega(\|v(y)-v(p)+\lambda(f-0)\|).
\tag{GP4}
\]

更强的、可直接使用的前件是对认证图的全部两图点 \((y,f),(y',f')\) 成立相同形式，并只在核输入对距不超过 \(R\) 时使用。要求每个 \(x\in U_R\) 有一个 \(p\in S\) 使 \(v(p)\in P_Z(v(x))\)，且 \((p,0)\) 属于同一图。有限维的非空闭 \(Z\) 自动有最近点；Hilbert 版本把这项最近锚可达性明列，不由闭性猜测。

再假设实际输出上的 **完整真残差** EB

\[
d(y,S)\le\psi(r_F(y)),\qquad
\psi:[0,\bar t]\to[0,\infty),
\tag{GP5}
\]

其中 \(\psi\) 非减、在零处连续、\(\psi(0)=0\)。核与物理零距离之间另给一个向前传递模

\[
d(v(y),Z)\le\sigma(d(y,S)),
\tag{GP6}
\]

\(\sigma\) 非减且零处连续，在所用参数上有定义。若 \(v\) 在实际输出和全部所用近极小零锚点对上 \(L_v\)-Lipschitz，可取 \(\sigma(t)=L_vt\)。这是一项 **到零集的向前界**；不要求物理逆映射已 Lipschitz。

设 \(h_\omega(t)=(t+\omega(t))/2\)，并核

\[
h_\omega(R)/\lambda\le\bar t,
\qquad
\sigma\!\left(\psi(h_\omega(t)/\lambda)\right)\le\kappa t
\quad(0<t\le R),\quad0<\kappa<1.
\tag{GP7}
\]

取 \(a=v(y)-v(p)\)、\(b=v(x)-v(y)\)。由 GP1、GP4，\(\|a+b\|=r(x)\)，\(\|a-b\|\le\omega(r(x))\)。平行四边形及反三角不等式给

\[
r(y)^2+\|b\|^2\le\tfrac12[r(x)^2+\omega(r(x))^2],
\qquad \|b\|\le h_\omega(r(x)).
\tag{GP8}
\]

GP3、GP5 的真残差与所选范数均在评价域内，故 GP6、GP7 给

\[
r(y)\le\sigma(\psi(r_F(y)))
\le\sigma(\psi(\|b\|/\lambda))\le\kappa r(x),
\quad
d(y,S)\le\psi(h_\omega(r(x))/\lambda).
\tag{GP9}
\]

若 \(r(x)=0\)，最近锚与 GP4 强制 \(b=0\)，GP5 又强制 \(y\in S\)。这还没有强制 \(y=x\)：非单射核可在同一零像纤维内跳动。

真物理 EB 在这里不是步残差 EB 的别名。完整核推前关系

\[
A(z)=\bigcup_{v(x)=z}F(x)
\tag{GP10}
\]

满足 \(\operatorname{zer}A=v(\operatorname{zer}F)\)，但一般只有 \(r_A(v(x))\le r_F(x)\)。例如 \(v(t,y)=(t,0)\)、\(F(t,y)=(t,y)\)，则 \(r_A(v(t,y))=|t|\)，物理真残差是 \(\sqrt{t^2+y^2}\)。不能未经证明把二者写成等号。

若欲由 GP5/GP6 得完整 \(A\) 的真 EB，须对 **全部物理纤维的每个图值** 给同一界 \(d(z,Z)\le\sigma\psi(\|f\|)\)，再对 \(f\in A(z)\) 取近极小列。残差取到，或 \(\sigma\circ\psi\) 在该残差处右连续，才能保留原 gauge；一般只能得右极限 gauge。GP8–9 直接在实际物理输出使用 GP5，避免这项不必要的换残差。相关一般反例见 [图值剖面工具](../../canonical/operator_profile_tools.md#op-nonattainment)。

<a id="gp-lift"></a>
## 3. 物理有限长度定理及精确 Dini 门

在上一节条件之外，假设在整个输出领圈 \(E\) 上有连续非减反演模 \(\eta\)，\(\eta(0)=0\)：

\[
\|x-y\|\le\eta(\|v(x)-v(y)\|)
\qquad(x,y\in E).
\tag{GP11}
\]

\(\eta\) 须在实际核步长及核尾距离上有定义；可直接取全域 gauge。置

\[
H(t)=\eta(h_\omega(t)),\qquad
L_H(r)=\sum_{j\ge0}H(\kappa^jr).
\tag{GP12}
\]

要求

\[
\int_0^R H(t)\,\frac{dt}{t}<\infty.
\tag{GP13}
\]

若 \(x_0\in U\)、\(r_0=r(x_0)\le R\)，且

\[
L_H(r_0)<d(x_0,H\setminus U),
\tag{GP14}
\]

则每条允许物理轨道全程存在、留在 \(U_R\)、有限长并收敛到 \(S\cap U\)。对全部 \(k\ge0\)，

\[
r(x_k)\le\kappa^kr_0,
\quad \|x_{k+1}-x_k\|\le H(\kappa^kr_0),
\quad
\|x_k-x_\infty\|\le L_H(r(x_k))\le L_H(\kappa^kr_0).
\tag{GP15}
\]

证明完全由估计承担。GP8、GP11 给实际物理步界，GP9 给核距离收缩。连续非减 \(H\) 满足

\[
\log(1/\kappa)H(\kappa^{j+1}r)
\le\int_{\kappa^{j+1}r}^{\kappa^jr}H(t)\,dt/t
\le\log(1/\kappa)H(\kappa^jr),
\tag{GP16}
\]

故 GP13 等价于 GP12 的几何采样可和，并使该级数在 \([0,R]\) 一致收敛。\(L_H\) 连续、零处消失，且

\[
\|x-y\|+L_H(r(y))\le H(r(x))+L_H(\kappa r(x))=L_H(r(x)).
\tag{GP17}
\]

GP14 和此式先证明新输出留在 \(U\)，再续用下一步 coverage，不循环使用留域。可和步长给 Hilbert 空间内的极限。GP9 的物理真 EB 右端趋零，闭 \(S\) 给极限在 \(S\)；严格预算给极限在 \(U\)。这一步无需由 \(r(x_k)\to0\) 反推 \(x_k\to S\)，也不要求 \(v^{-1}(Z)=S\)。

若 \(\eta(t)=Mt^\alpha\)、\(0<\alpha\le1\)，物理长度门是

\[
\int_0^R[h_\omega(t)]^\alpha\,dt/t<\infty.
\tag{GP18}
\]

幂模 \(\omega(t)=Lt^\gamma\)、\(0<\gamma\le1\) 自动满足此门，且物理共同尾为 \(O(r^{\alpha\gamma})\)；若 \(\omega(t)\asymp[\log(e/t)]^{-a}\)，则核长度只需 \(a>1\)，物理长度的本门却是 \(a\alpha>1\)。下文 C214 说明这不是只由证明松弛造成的差别。

<a id="gp-point"></a>
## 4. 物理点收敛只需较弱的核 Dini 门

已另行保证物理轨道一直在 \(E\) 及相关输入域时，核 Dini

\[
\int_0^R\omega(t)\,dt/t<\infty
\tag{GP19}
\]

给核有限长及核尾

\[
L_\omega(r)=\sum_{j\ge0}h_\omega(\kappa^jr),
\qquad
\|v(x_l)-v(x_k)\|\le L_\omega(\kappa^kr_0)\quad(l\ge k).
\tag{GP20}
\]

GP11 因而直接给物理 **端点** Cauchy 界

\[
\|x_l-x_k\|\le\eta(L_\omega(\kappa^kr_0)),
\qquad
\|x_k-x_\infty\|\le\eta(L_\omega(\kappa^kr_0)).
\tag{GP21}
\]

只需 \(\eta\) 在零处连续，不需 GP13。Hilbert 完备性及 GP9 的真物理 EB 仍给 \(x_\infty\in S\)。因此不能为了证明点收敛而强加物理长度 Dini，也不能从点尾 GP21 自动推出长度可和。

该较弱版本不自动提供上一节的物理留域预算：端点 Cauchy/尾界是给已合法轨道的结论。可用独立输出不变性、核域预算加 homeomorphism，或者更强 GP13 的物理预算先认证全部步骤。

<a id="gp-kernel-types"></a>
## 5. 强单调核、逆 Hölder 核与非单射截面

若核本身 \(m\)-强单调，

\[
\langle v(x)-v(y),x-y\rangle\ge m\|x-y\|^2,
\tag{GP22}
\]

Cauchy–Schwarz 给 GP11 的 \(\eta(t)=t/m\)。它给单射和像集上的 Lipschitz 逆，不单独给满射、连续性、完整 GPPA coverage 或保持零集。即使在 \(\mathbb R\)，强单调单值映射也可有跳跃：\(v(x)=x+\operatorname{sgn}(x)\)，在零处指定 \(\operatorname{sgn}(0)=1\)，满足 GP22 的 \(m=1\)，但不是满射也不连续。

若 \(v:H\to H\) 又全域 \(L\)-Lipschitz，则确为双射：对每个目标 \(z\)，\(x\mapsto x-c(v(x)-z)\) 在 \(0<c<2m/L^2\) 时有收缩因子 \(\sqrt{1-2cm+c^2L^2}<1\)，Banach 定理给唯一 \(v(x)=z\)。这是额外前件后的覆盖证明，不能把 GP22 本身说成满射定理。

局部 Hölder 逆只在明确输出领圈内给 GP11，不能把一个初值邻域的反演界使用到未经认证的远支。非单射核也可通过一个确定截面 \(g:Q\to H\)、\(v\circ g=\operatorname{Id}\)，并在 \(g(Q)\) 上满足 GP11，得到 **该截面政策** 的点/长度结论。它不覆盖完整 warped 纤维的任意选择；目标回缩也只固定该截面中的零代表。

完整反例仍是 [C197](../../literature_refresh_2026_10_08.md#lr-gppa-physical)：\(F(t,y)=v(t,y)=(t,0)\)、\(\lambda=1\)。该 pair 为 1-ASM，所有完整源前件成立，物理真 EB 为 \(d((t,y),S)=r_F(t,y)=|t|\)，核反射模甚至 \(\omega=0\)。但合法完整轨道 \((2^{-k},(-1)^k)\) 不点收敛、长度无限。源 ASM 的强常数没有消除零像纤维自由度。

<a id="gp-retraction"></a>
## 6. 连续极限回缩的两个物理版本

在 GP1–18 的条件下，若 \(v\) 在 \(U\) 连续，并且同图全对 GP4 对所有所用输入点对成立，则允许输出在 \(E\) 唯一：GP4 先强制核输出唯一，GP11 再强制物理输出唯一。记该物理映射为 \(T_x\)。它连续，因为 kernel 的两输入估计是

\[
\|v(T_xx)-v(T_xy)\|\le
\sqrt{\tfrac12[\delta^2+\omega(\delta)^2]},\qquad
\delta=\|v(x)-v(y)\|\le R,
\tag{GP23}
\]

再接 GP11 和 \(v\) 连续性即可。严格物理预算开域

\[
\mathcal O_x=\{x\in U:r(x)<R, L_H(r(x))<d(x,H\setminus U)\}
\tag{GP24}
\]

前向不变。证明用 GP17 及 \(d(T_xx,H\setminus U)\ge d(x,H\setminus U)-\|T_xx-x\|\)，和一般模 [GM21](../../canonical/general_modulus_dynamics.md#gm-retraction) 完全同型。GP15 的共同尾在整个 \(\mathcal O_x\) 上不超过 \(L_H(\kappa^kR)\to0\)，所以连续有限迭代的一致极限

\[
\Pi_x:\mathcal O_x\to S\cap U
\tag{GP25}
\]

连续，并固定每个 \(S\cap U\) 点。即为连续回缩；没有自动宣称强形变回缩。

另一版本只需 **核 Dini**：若 \(v:U\to W\) 为 homeomorphism，核开域 \(\mathcal O_z\subseteq W\) 的 GPPA 已由核预算认证连续极限回缩 \(\Pi_z\)，则

\[
\Pi_x=v^{-1}\circ\Pi_z\circ v:
v^{-1}(\mathcal O_z)\to v^{-1}(Z\cap\mathcal O_z)
\tag{GP26}
\]

也是连续回缩。目标须确为所用物理零集；完整坐标共轭 \(A(z)=F(v^{-1}z)\) 给此身份。GP26 不需要物理长度 Dini，C214 就有连续极限选择而部分轨道物理长度无限。非单射核的核回缩不能以此公式回缩全部物理零集。

<a id="gp-rates"></a>
## 7. 任意阶在哪里成立

GP9 的核距离递推是 \(r_{k+1}\le\Phi(r_k)\)，其中
\(\Phi(t)=\sigma(\psi(h_\omega(t)/\lambda))\)。例如向前零距离 Lipschitz，\(\omega(t)=Lt^\gamma\)、\(\psi(t)=ct^q\)，则小尺度 \(\Phi(t)=O(t^p)\)，\(p=\gamma q\)。\(p\) 可以大于 2；这是 **标量核零距离上界的阶**。

若 \(r_{k+1}\le Kr_k^p\)、\(p>1\)、\(a_0=K^{1/(p-1)}r_0<1\)，则

\[
r_k\le K^{-1/(p-1)}a_0^{p^k}.
\tag{GP27}
\]

逆 Hölder 桥及 GP15 可把它变成物理超几何点尾 \(O(a_0^{\alpha\gamma p^k})\)。但是 **上界不等于实际 Q 阶的等号**，也不自动给到某个选中极限的物理 Q-\(p\) 递推。非孤立零集存在切向漂移；只知物理点尾的上界，不能用它作下一步递推的分母下界。

一个可直接推出物理 Q-\(p\) 上界的充分门是：局部目标为孤立 \(S=\{s\}\)，核到该零点满足 \(\|v(x)-v(s)\|\le L_v\|x-s\|\)，并且 GP5 在全部实际输出上是所述幂 EB。此时
\(\|x_{k+1}-s\|\le C\|x_k-s\|^{\gamma q}\)。非孤立情形要得到同一 Q 阶，需另外证明核距离与所选物理点误差的匹配；上下同阶或显式不变量是可用的桥。

因此“我们允许任意阶”不能单独推出“严格优于原文”：要注明它是误差模参数、证明上界还是实际物理 Q 阶，且比较是否固定完整 \(F\)、kernel、输出政策和假设类。源 Theorem 2 的二次范数能量书写也不是“算法最多二次收敛”的定理。

<a id="gp-spiral"></a>
## 8. C214：核有限长而物理无限长的完整逆 Hölder 螺旋

- **Status**：`derived-checked`，下述直接构造与无限轨道证明；外部先行性未核。
- **范围**：每个 \(a>1\) 的 \(\mathbb R^3\) 完整关系、固定 \(\lambda=1\)、homeomorphic kernel。在 \(1<a<2\) 物理点收敛但长度无限；\(a>2\) 物理有限长。下文另校准 \(a=2\) 边界。

使用 [C10 的完整凹对数剖面](../../canonical/general_modulus_dynamics.md#gm-log-object) \(\ell_a\)，在核空间 \(w=(w_1,w_2,y)\) 定义完整双支关系

\[
G_a(w)=\{(-\ell_a(4y),0,3y),
(-\ell_a(4y),0,-5y)\}\quad(y\ge0),
\qquad G_a(w)=\varnothing\quad(y<0).
\tag{GP28}
\]

全部核纤维直接反演为

\[
J_{G_a}(p_1,p_2,q)=
(p_1+\ell_a(|q|),p_2,|q|/4),
\quad Z=\mathbb R^2\times\{0\}.
\tag{GP29}
\]

其完整 all-pairs 核反射模仍可取

\[
\Omega_a(t)=\sqrt{[t+2\ell_a(t)]^2+\tfrac94t^2},
\quad \Omega_a(t)\sim2\ell_a(t).
\tag{GP30}
\]

证明只把 GM31 的横坐标差改成两维切向范数：切向反射差至多 \(t+2\ell_a(t)\)，正常差至多 \(3t/2\)。所以其 Dini 门仍恰为 \(a>1\)。完整真残差仍是

\[
r_{G_a}(w)=\chi_a(y)=\sqrt{\ell_a(4y)^2+9y^2}\quad(y\ge0).
\tag{GP31}
\]

固定 \(c>0\)，在切向平面用 complex 记号定义极坐标 twist

\[
g(z)=e^{ic/|z|}z\quad(z\ne0),\qquad g(0)=0.
\tag{GP32}
\]

\(g\) 保持半径，连续双射，逆为 \(g^{-1}(z)=e^{-ic/|z|}z\)；它们在零点均连续，故是全域 homeomorphism。无需选择角度分支。

它们有全域统一模 \(\|g(z)-g(z')\|\le C_c(\delta+\sqrt\delta)\)，\(\delta=\|z-z'\|\)。为核此式，记 \(R=\max(|z|,|z'|)\)。若 \(\delta\ge R/2\)，输出差至多 \(2R\le4\delta\)；若 \(\delta<R/2\)，较小半径至少 \(R/2\)。拆开旋转得到

\[
\|g(z)-g(z')\|\le\delta+2c\delta/R,
\qquad \|g(z)-g(z')\|\le2R.
\tag{GP33}
\]

在 \(R\le\sqrt\delta\) 用后一界，在 \(R>\sqrt\delta\) 用前一界，便得所写模。逆 twist 同证明。在任何固定有界领圈上，可用 \(M\sqrt\delta\) 吸收线性项；不声称保半径的无界映射有全域纯半阶模。

半阶是局部最大指数：取同一射线上半径 \(r\) 和 \(r'=r/(1+\pi r/c)\)。输入差为 \(\pi r^2/(c+\pi r)\)，旋转角差精确为 \(\pi\)，输出差为 \(r+r'\)。因此任何指数 \(\alpha>1/2\) 的固定局部 Hölder 常数均失败。

现在置

\[
v(x_1,x_2,y)=(g^{-1}(x_1+ix_2),y),\qquad
F_a(x)=G_a(v(x)).
\tag{GP34}
\]

这里切向 complex 值仍视作两实坐标；\(F_a\) 的图值没有被旋转，它是核坐标关系的物理拉回。该 \(F_a\) 完整闭图，\(S=\mathbb R^2\times\{0\}\)，且 \(v\) 全域双射。完整 GPPA 恰逐步共轭于 GP29，完整 coverage 成立。

GP34 保留正常坐标，因此物理 **真** EB 和到零像的向前传递没有损失：

\[
d(x,S)=d(v(x),Z)=y=\chi_a^{-1}(r_{F_a}(x))
\quad(y\ge0).
\tag{GP35}
\]

它满足 GP7 的每个固定 \(\kappa\in(1/4,1)\) 的充分小尺度兼容，证明正是 [GM35](../../canonical/general_modulus_dynamics.md#gm-log-residual)。这是同一完整物理关系的真残差、kernel RL 与严格兼容，不是只凭一个设计好的序列。

取充分小 \(y_0>0\)，令

\[
y_k=4^{-k}y_0,\quad
\rho_k=\sum_{j=k}^{\infty}\ell_a(y_j),\quad
w_k=(-\rho_k,0,y_k),\quad
x_k=(g(-\rho_k),y_k).
\tag{GP36}
\]

\(a>1\) 保证 \(\rho_k\) 有限；\(\rho_k-\rho_{k+1}=\ell_a(y_k)\) 给 \(w_{k+1}=J_{G_a}w_k\)，故 GP36 是 **完整** \(F_a,v\) 的合法 GPPA 轨道。核轨道有限长，物理轨道收敛到 0，且物理距离到整个 \(S\) 精确几何下降。

设 \(b=\log4\)、\(A_k=\log(e/y_0)+kb\)。充分大 \(k\) 时

\[
\rho_k\sim\frac{A_k^{1-a}}{(a-1)b},
\quad \rho_k-\rho_{k+1}=A_k^{-a},
\quad
\Delta\theta_k=c(\rho_{k+1}^{-1}-\rho_k^{-1})
\sim c(a-1)^2b^2A_k^{a-2}.
\tag{GP37}
\]

当 \(1<a<2\)，角增量趋零，径向增量相对于 \(\rho_k\Delta\theta_k\) 的比值趋零。因此由两极坐标点的距离公式

\[
|g(-\rho_{k+1})-g(-\rho_k)|^2
=(\rho_k-\rho_{k+1})^2
+2\rho_k\rho_{k+1}(1-\cos\Delta\theta_k),
\tag{GP38}
\]

得到

\[
|g(-\rho_{k+1})-g(-\rho_k)|
\sim c\frac{\rho_k-\rho_{k+1}}{\rho_k}
\sim\frac{c(a-1)}{k}.
\tag{GP39}
\]

故物理轨道长度无限，虽核轨道有限长、核与物理点均收敛、真残差 EB 和严格 kernel 兼容全部成立。

\(a=2\) 时 \(\Delta\theta_k\to cb^2\)。选 \(c=\pi/b^2\)，此极限为 \(\pi\)，GP38 给位移同阶于 \(2\rho_k\asymp1/k\)，仍无限长。\(a>2\) 时，不论角度如何，切向步界为 \(\rho_k+\rho_{k+1}\)，而 \(\sum_k\rho_k<\infty\)；正常变差也可和，故物理长度有限。

于是这个校准的完整族具有精确物理长度门 **\(a>2\)**，正好对应半阶逆的 GP18 门 \(a\alpha>1\)、\(\alpha=1/2\)。它说明不能把核 Dini \(a>1\) 无损输送成逆 Hölder 物理有限长度。与此同时，GP21 的物理端点上界为 \(O(k^{-(a-1)/2})\)，此例实际点尾是 \(\rho_k+o(\rho_k)\asymp k^{1-a}\)；一般反演上界不声称每个例子都取等。

对所有物理初值，这个完整映射还具有显式连续极限回缩。记 \(E_a(t)=\sum_{j\ge0}\ell_a(4^{-j}t)\)，\(a>1\) 时该函数有限、连续且零处消失，则

\[
\Pi_x(x_1+ix_2,y)
=\left(g\big(g^{-1}(x_1+ix_2)+E_a(|y|)\big),0\right).
\tag{GP40}
\]

实数 \(E_a\) 加在第一切向坐标。其连续性由固定有界参数上的 Dini 一致尾及连续有限前缀给出；在 \(y=0\) 为恒等。因此 C214 也直接分开“连续回缩存在”和“每条物理轨道有限长”。

## 9. 与当前 GPPA 比较的使用边界

本页增加的是明确的 kernel/物理桥、回缩及逆 Hölder 长度边界。它没有撤销 [C199 的真实重合](COMPARISON.md#gppa-overlap)，也没有把 [C204 的完整图障碍](pair_monotone_barrier.md#pm-proof) 升级为原轨道不能借删支证明。持续误差的物理输出到核输出桥及误差管见 [一般模 inexact GPPA](../../canonical/gppa_inexact_modulus.md#gi-physical)；在那里同样需用实际点对的向前核模，并将点收敛与物理长度分别判断。

直接身份：GP8–9 是 kernel anchored 几何与真物理残差的桥；GP12–18 是物理有限长度与留域；GP19–21 是较弱的物理点尾；GP24–26 是两种回缩；GP28–40 是完整构造 C214。有限计算仅可复核常数和有限步，不能承担 Dini 或无限螺旋长度证明。
