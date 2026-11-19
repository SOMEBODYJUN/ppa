# 原 PPA 的补偿锚距条件与两个锐边界

**版本：第 004 轮 M003-v2；状态：derived-checked，登记为 C341–C342。** 第 003 轮 v1 的不等式不变；v2 把证书逐初值定义，再将“初值域含非解点”明确作为非平凡覆盖的资格，修正 v1 对 \(F\equiv0\) 的退化量词冲突。两版不混作同一精确声明。共有引理、两条导入、锐边界及旧合同的比较经过独立重构；[验收记录](../../audit/COMMON_STRUCTURE_M_ACCEPTANCE_2026-11-18.md) 区分证明、修订和仍未覆盖的范围。公开先行性未判定。

固定有限维欧氏空间 \(X\)、原关系 \(F:X\rightrightarrows X\)、固定 \(\lambda>0\)、非空闭 \(S\subseteq\operatorname{zer}F\)。写 \(d(x)=d(x,S)\)、\(r_F(y)=\inf_{v\in F(y)}\|v\|\)，空纤维取 \(+\infty\)。全程使用 \(J=(I+\lambda F)^{-1}\)。本页的共同收敛证明和两条导入均不调用待证的轨道收敛结论。

<a id="ca-definition"></a>
## 1. 静态条件及共有引理

对一点对令 \(s=\|x-y\|\)、\(A_p=\|x-p\|+\|y-p\|\)。固定任意长度尺度 \(\ell>0\)，定义
\[
 L_\ell(x,y;S)=\sup_{p\in S}\left[
 \|y-p\|-\|x-p\|+\frac{s^2}{\ell+A_p}\right].
 \tag{1}
\]
即使 \(S\) 无界，\(-s\le L_\ell\le2s\)，因为 \(s\le A_p\) 且两距离差绝对值至多 \(s\)。上确界无须达到。对合法弦 \(x=y+\lambda v\) 和 \(A_p>0\)，中括号恰等于
\[
 \frac{-2\lambda\langle y-p,v\rangle}{A_p}
 -\frac{\ell\lambda^2\|v\|^2}{A_p(\ell+A_p)} .
 \tag{2}
\]
若 \(A_p=0\)，用 (1)，该项为零。这给出同一图方向、步长和锚距尺度的原始表达式。

**条件 \(M(z)\)（M003-v2）。** 固定 \(\ell>0\)。对给定初值 \(z\)，给出静态集合 \(D\ni z\)、定义在包含 \(0,d(D)\) 的 \([0,R_*]\) 或 \([0,\infty)\) 上的有限函数 \(h\ge0\)，满足 \(h(0)=0,\ h(t)\to0\ (t\downarrow0)\)。允许 \(D,h\) 依赖 \(z\)，\(D\) 可不闭，也可无界。给出原图上的子关系 \(K\)，使

1. 对每个 \(x\in D\)，\(K(x)\ne\varnothing\)。每个 \(y\in K(x)\) 属于 \(D\cap J(x)\)，且
   \[
   L_\ell(x,y;S)\le h(d(x))-h(d(y)).
   \tag{3}
   \]
2. 对 \(Y=K(D)\) 的每个有界序列 \((y_j)\)，都有
   \[
   r_F(y_j)\to0\quad\Longrightarrow\quad d(y_j)\to0 .
   \tag{4}
   \]
   这是对输出点任意采样的静态正则条件。等价地，对每个有界球和每个 \(\varepsilon>0\)，该球中 \(y\in Y,\ d(y)\ge\varepsilon\) 时真残差下确界为正，空集取 \(+\infty\)。

\(K\) 可取为上游给出的所有允许弦，也可用具体不等式挑根。(1)–(4) 不引用未来轨道。\(x\in D\cap S\) 时取 \(p=x\)，(3) 迫使所选 \(y=x\)，而 \(x\in J(x)\)。对一个给定 \(U_0\)，逐点证明 \(M(z)\) 即覆盖其中每个初值；满足本研究的非平凡覆盖还要求 \(U_0\setminus S\ne\varnothing\)。若某退化实例只有零初值，证书给驻点结论，不把它计为非平凡实例。以下 C242 与平坦立方例分别见证两条必需导入均非空。

**共有引理。** 从每个认证 \(z\) 可无限续接原根；每条坚持选 \(K\) 的轨道点收敛于 \(S\)，且 \(\sum_k\|x^{k+1}-x^k\|^2<\infty\)。任取有限前缀，末点在 \(D\)，因 (3) 的覆盖可再取一步且仍在 \(D\)。递归给无限轨道。对固定 \(p\in S\) 设 \(E_p(x)=\|x-p\|+h(d(x))\)，则 (3) 给
\[
 E_p(y)+\frac{s^2}{\ell+A_p}\le E_p(x).
 \tag{5}
\]
固定一个 \(p_0\)，令 \(C=E_{p_0}(z)\)。沿轨道 \(\|x^k-p_0\|\le C\)，故 \(\ell+A_{p_0}\le\ell+2C\)，求和得 \(\sum_k s_k^2\le(\ell+2C)C\)。又 \(r_F(x^{k+1})\le s_k/\lambda\)，故由 (4) 得 \(d(x^k)\to0\)。有限维有界性给聚点 \(p_*\in S\)。取趋于 \(p_*\) 的子列，\(E_{p_*}\to0\)，用 (5) 在整列的单调性得 \(x^k\to p_*\)。只需 \(h\) 在零连续；极限落入 \(S\) 不用 \(D\) 闭。

同一平方项实际控制正则尺度。对上述被 \(p_0,C\) 定下的有界窗，设 \(\eta(t)=\min(1,\inf\{r_F(y):y\in Y,\|y-p_0\|\le C,d(y)\ge t\})\)。对 \(t>0\)，(4) 使 \(\eta(t)>0\)，且 \(\lambda\eta(d(y))\le s\) 对 \(d(y)>0\) 的实际弦成立。于是同一次图方向与正则性推导给
\[
 E_p(y)+\frac{s^2+\lambda^2\eta(d(y))^2}{2(\ell+A_p)}
 \le E_p(x)\qquad
 \big(y\in Y\cap\overline B(p_0,C),\ d(y)>0\big).
 \tag{5a}
\]
这同时保留原弦方向、正则尺度与原步长，静态下界不用于假定根存在。准 Fejér 的聚点论证为已有方法；本轮的增量在共同原图入门与 §4 的两个分界。参考 Combettes, *Quasi-Fejérian Analysis of Some Optimization Algorithms*, Theorem 3.11，[作者原文](https://pcombet.math.ncsu.edu/ipa.pdf)。本页未证明一般 \(h\) 产生其 Definition 1.1 的可和非负误差序列，故不直接援引该定理代替上述自足证明，也不把聚点步骤主张为新原理。

<a id="ca-affine"></a>
**仿射目标的切向预算。** 若 \(S=p_0+V\) 是正维仿射子空间，则对任意弦
\[
 L_\ell(x,y;S)\ge\|P_V(y-x)\|.
 \tag{5b}
\]
证明：对每个单位 \(u\in V\) 取 \(p=p_0-Ru\in S\)，令 \(R\to\infty\)。两距离之差趋于 \(\langle u,y-x\rangle\)，归一化平方项趋于零。再对单位 \(u\) 取上确界得到 (5b)。因而在本证书下
\[
 \sum_{k\ge0}\|P_V(x^{k+1}-x^k)\|\le h(d(z)).
 \tag{5c}
\]
该结论直接由静态弦不等式望远镜得到，不调用轨道收敛。它说明同一证书允许法向无限绝对长度，同时要求沿仿射零集的输运由补偿量支付；§4 的两条边界正对应切向预算与平方耗散。正维要求用于无穷零锚的取法，不将同一上确界论证套到单点目标。

<a id="ca-rleb"></a>
## 2. 投稿 RLEB 的全部原预算

原件为[投稿主定理](../../../发表成果整理/RLEB/sections/theorem_spine.tex)，Assumption (P1)–(P4) 与紧随的局部定理。取其原 \(U,R,\bar t,\lambda,\omega,\psi,\kappa,\mathcal J,F,S\)，以及 \(U_R=\{x\in U:d(x)\le R\}\)。\(\omega,\psi\) 在各自闭窗有限非减、零处连续且值为零。写
\[
 B(t)=\tfrac12(t+\omega(t)),\qquad
 \Theta(t)=\sum_{j\ge0}B(\kappa^j t).
\]
\(\Theta(R)<\infty\)，同一 \(\lambda\) 满足 \(B(R)/\lambda\le\bar t\)，且 \(\psi(B(t)/\lambda)\le\kappa t\) 对全部 \(0<t\le R\) 成立。保留任何 \(\Theta(d(z))<d(z,X\setminus U)\) 的原认证 \(z\in U_R\)。

任给 \(x\in U_R\) 与 (P1) 允许的 \(y\in\mathcal J(x)\)，(P2) 给出可以依赖 \(y\) 的最近输入零锚 \(a\)，满足 \(4\langle y-a,x-y\rangle\ge d(x)^2-\omega(d(x))^2\)。平方恒等式给 \(\|2y-x-a\|^2=\|x-a\|^2-4\langle y-a,x-y\rangle\le\omega(d(x))^2\)。由 \(2(x-y)=(x-a)-(2y-x-a)\)，得 \(s\le B(d(x))\)。真实包含和原工作窗给 \(r_F(y)\le s/\lambda\le B(R)/\lambda\le\bar t\)，故 (P3)、\(\psi\) 非减与原兼容给
\[
 d(y)\le\psi(r_F(y))\le\psi(B(d(x))/\lambda)\le\kappa d(x)
 \quad (d(x)>0).
\]
若 \(d(x)=0\)，则 \(s=0\)。由 (P3) 与 \(\psi\) 零处连续，所有允许输出序列上均有 (4)，这里使用整个 \(F(y)\) 的残差。

\(\Theta\) 非减，\(\Theta(t)-\Theta(\kappa t)=B(t)\)。以任意有限项的零处连续和受 \(\sum_j B(\kappa^jR)<\infty\) 支配的一致尾，得 \(\Theta(t)\to0\)；不使用原模在正尺度的连续性。因此
\[
 s\le\Theta(d(x))-\Theta(d(y)).
 \tag{6}
\]
令 \(d_0=d(z)\)，取
\[
 D=\{x:d(x)\le d_0,\ \|x-z\|+\Theta(d(x))\le\Theta(d_0)\},
 \qquad h=2\Theta .
 \tag{7}
\]
\(z\in D\subset U_R\) 由原严格预算成立。给 \(x\in D\)，(6) 和三角不等式使每个原允许根仍属于 \(D\)，故 \(K=\mathcal J|_D\) 有逐点覆盖。(1)、(6) 给 \(L_\ell\le2s\le h(d(x))-h(d(y))\)。因而导入保留同模同窗、同 \(F,S,\lambda\) 和原初值域。因子 2 仅在 (3) 中使用，(7) 的实际留域阈仍是 \(\Theta(d_0)\)。若有指定不变状态集，给 (7) 取与其交。前件还给原绝对长度界 \(\sum_k s_k\le\Theta(d_0)\)、原极限在 \(S\cap U\)。

**C09 与 C242。** C09 另要求同一图块的全对反射、最近零锚进入该图块和图块覆盖。用其最近零锚的图点与所选输出图点配对即得上述 (P2)，同输入差为零还给图块内单值。原 Dini 积分与几何采样级数用每段 \([\kappa^{j+1}R,\kappa^jR]\) 的单调上下界相互推出。C09 的根只是完整 \(J\) 的子图时仍给原合法根。C242 则须检查真正非线性锚模。固定 \(F(u,v)=(u,-\sqrt{|u|})\)、\(\lambda=1,S=\{0\}\times\mathbb R\)，唯一完整根 \(y=(a/2,b+\sqrt{|a|/2})\)，输入 \(x=(a,b)\)。最近锚 \((0,b)\) 处的反射差范数恰为 \(\sqrt{2|a|}\)；\(r_F(u,v)^2=u^2+|u|\ge d(u,v)\)。取原 \(\omega(t)=\sqrt{2t},\ \psi(t)=t^2,\ R=1/16,\bar t=1,\kappa=3/4,\ U=X\)。\(B(R)=(1+4\sqrt2)/32<1\)，且 \(\sup_{0<t\le R}B(t)^2/t=(33+8\sqrt2)/64<3/4\)。几何和给 \(\Theta(t)=t/[2(1-\kappa)]+\sqrt{2t}/[2(1-\sqrt\kappa)]\)，故 (7) 认证整条原条带的每个初值。以 \((a,b),(0,b)\) 的小尺度比较可见不可能把相同锚模换成有限常数线性模。

<a id="ca-monotone"></a>
## 3. 有限维经典极大单调 PPA 的完整导入

取任意极大单调 \(F\)、非空 \(S=\operatorname{zer}F\)、任意固定 \(\lambda>0\)，\(D=U_0=X,K=J,h=0\)。Minty 满射定理给每个 \(x\in X\) 一个且仅一个原根，对整个关系成立，无需 \(F\) 本身处处有值。经典来源为 Rockafellar (1976), p.878, (1.5) 前后，[作者扫描](https://sites.math.washington.edu/~rtr/papers/rtr066-MonoOpProxPoint.pdf)。单调性给 \(\langle y-p,(x-y)/\lambda\rangle\ge0\)，故 (2) 非正；\(A_p=0\) 仍成立。极大性使图闭，具体地，图点收敛的极限与全图单调相关，按极大性仍在图内。若 (4) 失败，有有界 \(y_j\) 使 \(d(y_j)\ge\varepsilon,\ r_F(y_j)\to0\)，取 \(v_j\in F(y_j)\) 满足 \(\|v_j\|\le r_F(y_j)+1/j\)。抽聚点 \(y_*\) 后闭图使 \((y_*,0)\in\operatorname{gph}F\)，与距离连续矛盾。\(S\) 闭性也由闭图得到。此行不需误差界指数，有限维闭图与完整零集给定性有界窗正则 (4)。这条任意正步长的零亏损机制与 RLEB 的 \(\lambda,\omega,\psi\) 整窗兼容不同。这里只导入原任务的有限维精确固定步长版。

例如 \(F(a,n)=(0,n^3)\) 为凸函数 \(n^4/4\) 的梯度；也可直接由单调及 \(n+\lambda n^3\) 的严格增满射证明极大性（若一图点能加入，比较同一 Minty 输入的原点即得相同图点）。全部零线作 \(S\)，真残差为 \(|n|^3\)。所有 \(\lambda>0\) 有覆盖，\(d(y)/d(x)=1/(1+\lambda n^2)\uparrow1\) 当 \(n\to0,\ n\ne0\)，故任何零线邻域都无共同 \(\kappa<1\)。

<a id="ca-sharp"></a>
## 4. 一个原算子族上的两个锐边界

取 \(X=\mathbb R\times\mathbb R^2,\lambda=1,\ S=\mathbb R\times\{0\}\)，常数 \(c,\alpha,\beta>0\)，取平面旋转 \(Q\) 的角度 \(\theta=\pi/\sqrt2\)，故 \(\cos\theta<0\)，所有正整数 \(m\) 都有 \(Q^m\ne I\)。直接在输出变量上定义全空间单值连续原算子
\[
 F(b,w)=\big(-c r^\beta,\ ((1+r^\alpha)Q^{-1}-I)w\big),\quad r=\|w\| .
 \tag{8}
\]
完整近端方程对输入 \(x=(a,z)\)、输出 \(y=(b,w)\) 恰为
\[
 b=a+c r^\beta,\qquad z=(1+r^\alpha)Q^{-1}w,\qquad
 t:=\|z\|=r+r^{1+\alpha}.
 \tag{9}
\]
最后一式的右端在 \([0,\infty)\) 连续严格增且满射。它先唯一给 \(r\)，再由 \(w=Qz/(1+r^\alpha)\) 和 (9) 唯一给完整根。目标是完整零集。记 \(\sigma_\theta=\sqrt{2-2\cos\theta}>0\)。真残差精确为
\[
 r_F(b,w)^2=c^2r^{2\beta}+
 r^2\{(1+r^\alpha)^2+1-2(1+r^\alpha)\cos\theta\}
 \ \ge\ \sigma_\theta^2 r^2 .
 \tag{10}
\]
因此整个图有线性真误差界，适用于每个 \(c,\alpha,\beta\)。

**静态上游认证。** 若 \(\beta>\alpha,\ \alpha<2\)，任取 \(R>0\) 和 \(\ell>0\)，令 \(D=U_0=\{x:d(x)\le R\}\)。所有完整根由 (9) 仍在窗内。对任意锚 \(p=(p_a,0)\)，由半径减少、实轴平移三角不等式，
\[
 \|y-p\|-\|x-p\|=
 \sqrt{(b-p_a)^2+r^2}-\sqrt{(a-p_a)^2+t^2}
 \le c r^\beta .
 \tag{11}
\]
这是对全部无界锚线的同一个界；令 \(p_a\to-\infty\) 时该差趋于 \(c r^\beta\)。又
\[
 s^2\le c^2r^{2\beta}+(2+R^\alpha)^2r^2 .
\]
故
\[
 L_\ell(x,y;S)\le A r^\beta+B r^2,\quad
 A=c+c^2R^\beta/\ell,\qquad B=(2+R^\alpha)^2/\ell .
 \tag{12}
\]
对 \(q>\alpha\)，\(m_q=(q-\alpha)\min\{1,(1+R^\alpha)^{q-\alpha-1}\}>0\)。直接积分给
\[
 t^{q-\alpha}-r^{q-\alpha}
 =(q-\alpha)r^q\int_0^1(1+u r^\alpha)^{q-\alpha-1}\,du
 \ge m_q r^q .
\]
因此取
\[
 h(t)=\frac{A}{m_\beta}t^{\beta-\alpha}
      +\frac{B}{m_2}t^{2-\alpha}
 \tag{13}
\]
即可由 (12) 证明 (3)，而 (10) 给 (4)。此处在算轨道之前已完成从原图验证。特别地，\(\alpha=1,\beta=2\) 时 \(h\) 是线性的。

**必要性与实际动力学。** 设任意非解初值有 \(r_0>0\)，写 \(r_k=d(x^k)\)。由 (9)，\(r_k=r_{k+1}(1+r_{k+1}^\alpha)\)，所以 \(r_k\downarrow0\) 且
\[
 r_{k+1}^{-\alpha}-r_k^{-\alpha}
 =\frac{1-(1+r_{k+1}^\alpha)^{-\alpha}}{r_{k+1}^\alpha}\longrightarrow\alpha .
\]
求 Cesàro 平均给 \(r_k\sim(\alpha k)^{-1/\alpha}\)。于是对每个 \(q>0\)，\(\sum_{k\ge1}r_k^q<\infty\) 当且仅当 \(q>\alpha\)，等号时按调和级数发散。切向坐标递增，\(a_k=a_0+c\sum_{j=1}^k r_j^\beta\)。所以唯一轨道点收敛于 \(S\) 当且仅当 \(\beta>\alpha\)。若 \(\beta\le\alpha\)，任何证书都不能从此非解点推出收敛。若 \(\alpha\ge2\)，(10) 与 \(\lambda=1\) 给 \(s_k^2=\|F(x^{k+1})\|^2\ge\sigma_\theta^2r_{k+1}^2\)，从而平方步长和发散。§1 说明这排除 **任何** 允许的 \(D,h,K,\ell\) 认证此非解初值，即使 \(\beta>\alpha\) 时它实际收敛。

故对每个非解初值，M003-v2 可认证 **当且仅当** \(\beta>\alpha,\ \alpha<2\)；真实点收敛的门只有 \(\beta>\alpha\)。两条开边界均已处理。此判定只针对 (8)、所定 \(\lambda,S,\theta,c\)，不转用到一般 PPA。

<a id="ca-separation"></a>
### 与已有证书逐项去重

设 \(1\le\alpha<2,\ \beta>\alpha\)，保留 (8) 的同一完整原图、\(\lambda=1\)、完整零线与管 \(D=\{d\le R\}\)。这里不宣称新条件比所有可能的经典收敛理论更弱。

**有限长度及固定跨步。** 任意固定正整数 \(m\)，\(r_{k+m}/r_k\to1\)，且法向单位方向每次转 \(Q\)，故
\[
 \frac{\|w_{k+m}-w_k\|}{r_k}
 =\left|e^{im\theta}\frac{r_{k+m}}{r_k}-1\right|
 \longrightarrow |e^{im\theta}-1|>0.
\]
\(\sum_k r_k=\infty\)，故 \(\sum_k\|x^{k+m}-x^k\|=\infty\)。即使仅取 \(k=jm\) 的不重叠块，该和仍发散，因为 \(r_{jm}\asymp j^{-1/\alpha}\)。这排除 [C277](../../canonical/unified_ppa_joint_certificates.md) 的物理有限长度合同和 [C319](../../canonical/ppa_two_step_and_directional_residual.md#td-cancellation) 所需固定两步净位移可和。不可把“步长平方可和”写成“物理有限长度”。

**C277 的另一条全锚 Fejér 后端。** 它的 JP19–JP20 不要求有限长度，必须另排。令一条非零弦的切向增量 \(\delta=cr^\beta>0\)，取 \(p=(u,0)\)，则
\[
 \|y-p\|^2-\|x-p\|^2
 =2(a-u)\delta+\delta^2+r^2-t^2\longrightarrow+\infty
 \quad(u\to-\infty).
\]
故同一 \(S\) 上连 \(\sigma=0\) 的全锚 Fejér 不等式也失败。在 \(\alpha=1,\beta=2\) 时，还可取固定近锚 \(u=a-\varepsilon\)，\(\varepsilon>0\)，得到
\[
 2c\varepsilon r^2-2r^3+(c^2-1)r^4>0
\]
对充分小的正 \(r\) 成立；失败不只依赖远处零锚。新的 (1) 由于使用距离增量和归一化平方项，仍有对全部锚统一的有限上界 (12)。

**固定距离收缩。** \(r_{k+1}/r_k=(1+r_{k+1}^\alpha)^{-1}\to1\)，排除每个穿过零线的邻域上的统一 \(\kappa<1\)，以及原 RLEB 与 [C320](../../canonical/ppa_two_step_and_directional_residual.md#td-directional) 的整套假设。它们的 Dini 条件单独未必失败：本区 \(\beta>1,\alpha>0\) 的原图局部 Lipschitz，不能把整套兼容失败写成所有反射 Dini 模不存在。另一方面，§2 已证明原 RLEB 全部原前提推出 \(M\)，所以对该整套充分条件存在真正的单向包含及反向严格见证。

**C324/C329 的窄窗和宽锚输运窗。** 写弱单调常数为 \(B_w\)，与 (8) 的指数 \(\beta\) 区分。比较同一 \(b\) 处的 \((b,w)\) 与 \((b,0)\)，有
\[
 \frac{\langle(0,w),F(b,w)-F(b,0)\rangle}{r^2}
 =(1+r^\alpha)\cos\theta-1.
\]
因此任何包含零法向小邻域的统一弱单调常数都满足 \(B_w\ge1-\cos\theta>1\)，在 \(\lambda=1\) 下已不可能有窄门 \(2B_w<a<2/\lambda\)。这还不够排除 [C329 定理 2A](mother_fitzpatrick_bridge.md) 的宽窗，须再核其原条件
\[
 d(y)\le K r_F(y),\qquad
 \|y-p_x\|\le Ld(y),\quad p_x\in P_S(x),\quad L\ge1,
 \qquad \lambda>2B_wL^2K^2.
\]
由 \(\beta>\alpha\ge1\) 得 \(\beta>1\)，而 (10) 给
\(r_F(b,w)/r\to\sigma_\theta\)。于是同一任何近零窗的 EB 常数必须满足 \(K\ge1/\sigma_\theta\)，从而
\[
 2B_wL^2K^2\ge
 \frac{2(1-\cos\theta)}{\sigma_\theta^2}=1=\lambda.
\]
严格 Gate-AT 也完全失败。即使仅对本弦最近输入锚比较，\(-\langle y-p_x,F(y)\rangle/\|y-p_x\|^2\to1-\cos\theta\)，故不能通过把全对常数换成该锚常数绕过此界。距离比趋一也独立反驳 Gate-AT 所推出的固定收缩结论。

**C333–C339 与先行性。** [原非线性图桥](nonlinear_rl_bridge.md) 处理固定惩罚、同模延拓以及整纤维真残差；它们没有提供 (12) 的切向漂移和法向旋转分界。本证书不依赖固定输出位移惩罚，也不从锚模自动推出真残差正则性。上述分离只针对已精确陈述的原合同，不排除所有可能的重写、准 Fejér 理论或替代势，也不裁定公开首创。

<a id="ca-attacks"></a>
## 5. 量词攻击及 Luke–Tam 引文审查

**点收敛与平方步长可和仍不等于本证书。** 在 \(\mathbb R^2\) 取完整单值原图
\[
 F(b,w)=\big(w,-(2+|w|)w\big),\qquad
 S=\mathbb R\times\{0\},\qquad\lambda=1.
\]
完整根对输入 \((a,z)\) 满足 \(a=b+w\)、\(z=-(1+|w|)w\)，故全域唯一。任何非解初值的 \(w_k\) 交替变号，半径满足 \(r_k=r_{k+1}+r_{k+1}^2\)，按 §4 的倒数差推导有 \(r_k\sim1/k\)。切向增量为 \(-w_{k+1}\)，由交错级数判别可和，法向趋零，所以原点列收敛于 \(S\)。另一方面，\(s_k^2=r_{k+1}^2[1+(2+r_{k+1})^2]\) 可和，完整真残差满足 \(r_F\ge\sqrt5\,d\)，但切向绝对总长 \(\sum_k r_{k+1}=\infty\)。这与 (5c) 矛盾，排除任意允许的本证书。它进一步划清本充分条件的限制，不影响任何已证导入。

**真残差识别不能只改成点态非零。** 取 \(X=\mathbb R,\lambda=1\)，定义 \(F(0)=\{0\}\)，\(F(y)=\{y-1\}\) 当 \(y>1\)，其余纤维为空。于是完整零集 \(S=\{0\}\)。令 \(D=(1,2]\)、\(K(x)=\{(x+1)/2\}\)、\(h=0\)。每个输入有唯一完整原根且仍在 \(D\)。写 \(s=x-y>0\)，则对唯一零锚
\[
 L_\ell(x,y;S)=-s+\frac{s^2}{\ell+x+y}<0.
\]
所以覆盖、留域和 (3) 全部成立，每个非解输出的完整真残差也严格正。然而从 \(z=2\) 出发，唯一轨道为 \(x^k=1+2^{-k}\to1\notin S\)，同时 \(r_F(x^k)=2^{-k}\to0\)。失败恰在静态条件 (4)：有界输出序列靠近图在零值处的缺口。这个反例没有攻击正确版本中 \(D\) 可不闭的结论；它否定将 (4) 弱化为每点残差非零。

**坏参数。** \(F(y)=-by,\ b>0,\ S=\{0\}\)。令 \(q=\lambda b\)。当 \(q=1\) 时非解输入没有原根；\(0<q<2,\ q\ne1\) 时唯一根倍率的模大于一，非解初值无收敛选择；\(q=2\) 时唯一二周期上 \(d\) 不变而 (1) 的平方项严格正。\(q>2\) 时唯一根 \(y=-\gamma x,\ \gamma=(q-1)^{-1}\in(0,1)\)。取 \(K=J,D=X,\ h(t)=2(1+\gamma)t/(1-\gamma)\)，则 \(L_\ell\le2s=2(1+\gamma)d(x)=h(d(x))-h(d(y))\)，完整真残差 \(b|y|\) 给 (4)。此行精确恢复四种实际选择行为。

**同初值分根。** 用 C322 的全隐式两粒子比较，\(\lambda=100,\phi(a)=1/(1+a^2)\)，平均速度零并固定初始中心。差坐标原弦是 \(a_+-a=100b_+,\ b=(1+100\phi(|a_+|))b_+\)。\(z=(0,1/3)\) 的第一步小根取 \(s_-\in(0,1/2)\) 满足 \(s_-/100+s_-/(1+s_-^2)=1/3\)，给 \(a_+=s_-,b_+=s_-/100\)。另一根 \(s_+\in(30,31)\) 的后续分离无界，故拒绝它。在好锥 \(C=\{a\ge0,b\ge0,\ a+100b\le1\}\) 中，连续函数 \(u\mapsto (u-a)(1+100\phi(u))\) 在 \(u=a\) 为零并趋于无穷，从而每个输入有根。每个根满足 \(0\le b_+\le b,\ a\le a_+\le a+100b\le1\)，继而 \(b_+\le b/51,\ a_++100b_+\le a+100b\)。在 \(D=\{z\}\cup C\)，于 \(z\) 取小根，其余取上述好锥根。由 \(s_-<1/2\) 知首步也有 \(b_+\le b/51\)。实际粒子欧氏范数限制到零均值差坐标同时将差位置和差速度乘 \(1/\sqrt2\)，故 \(d(x)=b/\sqrt2\)，\(s\le(100b_++b-b_+)/\sqrt2\le(151/51)d(x)\)，所有选择上 \(d(y)\le d(x)/51\)。取 \(h(t)=7t\)，则 \(2s\le (302/51)d(x)< (350/51)d(x)\le h(d(x))-h(d(y))\) 对非零 \(d(x)\) 成立，零输入驻定。\(F\) 的位置图值为负速度，令 \(S\) 为速度为零的全部平衡态，原单值真残差至少为 \(d(y)\)。由此明确出了可续接的 M003 子图。C339 多值长支例同理可直接检查短支 \(y=x/2\)（反射值零），完整真残差为 \(|y|\)，\(h(t)=2t\) 支付 \(2s\)；长支无需通过。C337 只用最近锚模掺入小图值会击破外加真误差界，本候选没有从 (1) 或锚模独立推出 (4)。例如在原正则性被删掉时，由 (5) 只得物理步长趋零。F110 同零截面异动力不改变 (2) 所保留的弦内积。

**Luke–Tam 引文的独立核查。** [C340 完整证明](lt_ball_localization_obstruction.md#lt-ball-counterexample) 已逐项核对正式版 Definitions 1–2、Assumption 2、Theorem 2。完整 \(F(a,b)=(-b/2,b)\)、\(\lambda=1\) 满足全部原前提与严格参数门，但每个同半径零点球内都有唯一根离球的初值。其实际原轨道仍全局点收敛。故本页用 §3 的经典极大单调行满足 G3，不把 LT 同球印刷句当作已核的局部覆盖定理，也不把该局部化反例升级为 LT 收敛机制全面失效。

<a id="ca-gates"></a>
## 6. G1–G7 的承重证据与范围

| 项 | 证据与限定 |
| --- | --- |
| G1 | (1) 的有界实数、(2) 的原图方向、(4) 的真残差识别共同进入 (5a)；(5b)–(5c) 提取真实切向预算。两条上游显式构造静态域和补偿量，§4 的收敛但不可认证情形排除把结论原样改名。 |
| G2 | §2 覆盖投稿允许子图、逐输出最近输入锚、完整真残差、原窗口与严格初值预算。C09 仅在其实际图块上补说明。C242 用原平方根参数，未改反射模。 |
| G3 | §3 对有限维极大单调 \(F\)、完整非空零集、所有初值和每个固定 \(\lambda>0\) 给 Minty 覆盖、闭图推出定性正则、符号推出 (3)。§5 精确核查 LT 同球子句的独立断点。 |
| G4 | §2 列出原 \(\omega,\psi,\lambda,\kappa,R,\bar t\) 与 \(\Theta\)；§3 的参数窗为全部 \(\lambda>0\)；§4 固定原 \(\lambda=1\) 给二指数门及端点。§5 另给负标量的全部步长检测。 |
| G5 | §1 从静态子图逐步续走，先有有界性再由完整真残差检测到达 \(S\)，最后用所有锚距证明原点列收敛。§2 静态域保原预算，§5 同初值明确选择小根。 |
| G6 | §4 同一原场的真实点收敛门为 \(\beta>\alpha\)，本证书门为 \(\beta>\alpha,\alpha<2\)。任意固定分组长度、固定距离因子、C277 的两条后端及 C329 的宽 Gate-AT 均有独立排除证据；不把这种精确分离外推成对所有理论的严格包含。 |
| G7 | §1–§5 涵盖 \(S\) 无界、\(D\) 不闭、模只在零连续、选根续接、代入处完整纤维、参数临界、原图唯一性、负标量无根/二周期与真收敛超出证书的对象。正面推导及负面见证独立于数值实验。 |

一般 KL 或变化右端正则性、没有原根覆盖的裸正则、没有定量预算的一般次单调性、无限维非紧情形均无本轮全类导入。平方耗散证明及补偿 Fejér 结构有已知理论来源，本轮不判公开首创。范围中的数学可复核性与外部新颖性分开。本候选的额外限制是平方步长可和；§4 中 \(\alpha\ge2,\beta>\alpha\) 划出真实遗漏，不把它称作不收敛。
