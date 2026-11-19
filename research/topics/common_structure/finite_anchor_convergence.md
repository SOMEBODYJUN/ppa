# 有限零锚的测距与原图功预算

<a id="finite-anchor-candidate"></a>

**候选身份 M002-v1。** 范围为有限维普通精确 PPA、固定正步长，以及指定的非空闭零点子集。本文提出有限个零锚的测距判据，给出由原图功和完整真残差导入点收敛的证明，并在同一完整原图和同一窗口上与全零锚检验比较。

**Status**：`candidate`。本候选自身的独立 G1–G7 审查尚未完成。以下推导、实例及比较构成供复核的证据。数学证据与公开先行性分开判断。

## 1. 有限零锚的静态判据

固定有限维欧氏空间 \(X\)、关系 \(F:X\rightrightarrows X\)、步长 \(\lambda>0\) 及非空闭集 \(S\subseteq F^{-1}(0)\)。记 \(d(x)=\operatorname{dist}(x,S)\)，\(r_F(y)=\inf_{u\in F(y)}\|u\|\)。对于每个待认证初值 \(z\)，以下数据都在选择轨道之前指定。

* 给定包含 \(z\) 的有界集合 \(D\subset X\)。不要求它闭。给定完整原图中的一个块 \(\Gamma\subset\{(y,v)\in\operatorname{gph}F:y\in D,\ y+\lambda v\in D\}\)，记 \(Y=\operatorname{pr}_1\Gamma\)。可用完整原图和这两个位置条件作为默认块。
* 给定非空有限集 \(P\subset S\)。要求 \(s\mapsto (\|s-p\|^2)_{p\in P}\) 在 \(S\cap\overline D\) 上单射。这是纯几何条件。等价地，任意两个不同的局部目标点的垂直平分超平面都不包含整个 \(P\)。总能从 \(S\) 选择一个仿射基作为分点集，因两点到每个基点等距将迫使其差既平行又垂直于该仿射包的方向空间。测距零锚可位于工作域之外。对具体的 \(S\cap\overline D\)，有时只需一个测距零锚。
* 要求对任何 \(y_j\in Y\)，若 \(r_F(y_j)\to0\)，则 \(d(y_j)\to0\)。等价地，对每个 \(\epsilon>0\)，残差下界 \(m_Y(\epsilon)=\inf\{r_F(y):y\in Y,\ d(y)\ge\epsilon\}\) 为正，空下确界取 \(+\infty\)。被评价的是完整 \(F(y)\)，即使 \(\Gamma\) 小于全图。
* 给定有限非负函数 \(h:[0,R_D]\to[0,\infty)\)，其中 \(R_D\ge\sup_{x\in D}d(x)\)，且 \(h(0)=0,\lim_{t\downarrow0}h(t)=0\)。在 \(R_D=0\) 的退化窗只需 \(h(0)=0\)。给定 \(c>0\)，置 \(\sigma_P(v)=\max_{p\in P}\langle p,v\rangle\)。对每个 \(x\in D\)，要求至少有一个 \(y\in D\) 和 \(v\in F(y)\)，使 \((y,v)\in\Gamma, x=y+\lambda v\) 且

\[
 2\lambda\big(\sigma_P(v)-\langle y,v\rangle\big)
 \le (1-c)\lambda^2\|v\|^2+h(d(x))-h(d(y)).                    \tag{1}
\]

以上条件定义给定初值 \(z\) 的 \(M(z)\)。当一个含非解初值的集合内每一点都具备这个证书时，即得到非平凡初值域。最后一项是原图纤维与有限个由 \(x,y,v,\lambda,h,c\) 明定的不等式的交非空。它只涉及一步和既定区域，可用公式、覆盖定理、代数检验或分支夹逼验证。\(h\) 的定义和验证都不依赖轨道的一个未知极限或尚未构造的值函数。

原 RLEB 容许最近输入零锚随分支改变，切向移动可以比到零集的距离大，原参数门用完整真残差和反射模吸收这项移动。经典极大单调 PPA 的同一图值则在每个零点方向做非负功，所有正步长都可用，集合距离甚至可以亚线性下降。在非孤立零集上，分点条件使有限个距离极限足以识别聚点。第 5 节在同一个闭半柱上比较有限分点锚与全部局部零锚的检验。

<a id="finite-anchor-lemma"></a>

## 2. 点收敛与正距离壳层的访问次数

**命题。** 每个满足 \(M(z)\) 的初值 \(z\) 有一条无限原 PPA 轨道趋于 \(S\cap\overline D\)。每个满足 (1) 且留在所定图块的选择都可以无限延拓且有相同结论。对每个非空正距离壳层，另有

\[
 \#\{k\ge0:d(x^{k+1})\ge\epsilon\}
 \le {\displaystyle\min_{p\in P}(\|z-p\|^2+h(d(z)))\over
             c\lambda^2 m_Y(\epsilon)^2}.                         \tag{2}
\]

空壳层的访问次数为零。这里的次数界同时使用图值方向、完整真残差与步长。它是计数界，不给最后一次离开该壳层的具体时刻。

**证明。** 写 \(x=y+\lambda v\)。对每个 \(p\in P\)，平方展开将 (1) 等价写成
\[
 \|y-p\|^2+h(d(y))+c\lambda^2\|v\|^2
       \le \|x-p\|^2+h(d(x)).                                    \tag{3}
\]
取 \(x^0=z\)。从任何已构造的前缀端点，都能在 \(D\) 中取一个满足 (1) 的下一原根。归纳及逐次选择给出无限序列，无需连续或可计算的选择器。对同一个 \(p\) 望远镜得到步长平方和有限，且各 \(\|x^k-p\|^2+h(d(x^k))\) 有极限。若输出 \(d(y)\ge\epsilon\)，则选中图值满足 \(\|v\|\ge r_F(y)\ge m_Y(\epsilon)\)，从而 (2) 成立。也可先得 \(v_k\to0\)，再用 \(0\le r_F(x^{k+1})\le\|v_k\|\) 及输出上的正则性得 \(d(x^k)\to0\)。于是 \(h(d(x^k))\to0\)，每个测距平方均有极限。所有聚点属于 \(S\cap\overline D\)，至少有一个聚点，因为 \(D\) 有界。任意两个聚点具有相同的各测距极限，故相同。有限维中的有界序列若只有一个聚点，必整列收敛。整个论证没有用 \(D\) 的闭性或 \(h\) 在正点连续。

<a id="finite-anchor-rleb"></a>

## 3. 原最近输入零锚 RLEB 的原窗导入

使用 [投稿主定理](../../../发表成果整理/RLEB/sections/theorem_spine.tex) 假设 P1–P4 的原 \(F,S,\lambda,\mathcal J,U,R,\bar t,\omega,\psi,\kappa\)。\(B(t)=(t+\omega(t))/2\)，\(\Theta(t)=\sum_{j\ge0} B(\kappa^jt)\)。给定原条件认证的 \(z\in U_R\)，即 \(t_0=d(z)\)，\(\Theta(t_0)<\operatorname{dist}(z,X\setminus U)\)。\(\Theta\) 有限非减，在零连续。这一连续性只须以可和序列 \(B(\kappa^jR)\) 支配每一项、对每个固定 \(j\) 用 \(B\) 在零连续。不要求两个原模在任何正点连续。

对每个 \(x\in U_R\) 及每个 \(y\in\mathcal J(x)\)，记 \(t=d(x),q=d(y),s=\|x-y\|\)。P2 中的 \(p_x\in P_S(x)\) 是本次该输出的锚。因 \(\|(2y-x)-p_x\|^2=t^2-4\langle y-p_x,x-y\rangle\le\omega(t)^2\)，三角不等式给 \(s\le B(t)\)。\(r_F(y)\le s/\lambda\le B(R)/\lambda\le\bar t\) 后才用 P3 和 P4，得 \(q\le\psi(r_F(y))\le\psi(B(t)/\lambda)\le\kappa t\)。在 \(t=0\) 时 \(s=0\)。于是
\[
 s\le B(t)=\Theta(t)-\Theta(\kappa t)\le\Theta(t)-\Theta(q).    \tag{4}
\]

预先指定
\[
 D=\{x:d(x)\le t_0,\ \|x-z\|+\Theta(d(x))\le\Theta(t_0)\},
 \qquad
 L=\Theta(t_0)+\max_{p\in P}\|z-p\|,
\]
其中 \(P\subset S\) 可取 \(S\) 的一个有限仿射基。\(z\in D\subset U_R\)，甚至 \(\overline D\subset U\) 因原严格预算。若 \(x\in D\)，P1 给真实允许根。由 (4) 及三角不等式，**每个**允许根都属于 \(D\)。取 \(\Gamma=\{(y,(x-y)/\lambda):x\in D,y\in\mathcal J(x)\}\)。原 P3 和在零连续的原 \(\psi\) 给 \(Y\) 上规定的完整真残差识别。置 \(c=1, h(t)=2L\Theta(t)\)，则
\[
 2\lambda\big(\sigma_P(v)-\langle y,v\rangle\big)
 \le 2Ls\le h(t)-h(q).
\]
故同一 \(M\) 成立。预算仍是 \(\Theta(t_0)\)，没有拿较大的 \(h(t_0)\) 替代原开域留量。原窗内全部允许输出都保留，有限长可再直接由 (4) 望远镜得到。C09 的比较行在同一原图块对全部双图点作反射比较，且要求最近零锚在该块中和输入覆盖，故推出上述 P2，并因同输入反射一致使该块单值。C09 的 Dini 积分在非减模下给同一几何级数有限，见 [C09 的全对一般模](../../canonical/general_modulus_dynamics.md#gm-data) 的 GM10–GM14。C09 的全对条件不是本导入的额外前提。

**[C242 的非线性检验](../../canonical/triangular_rleb.md#tri-object)。** \(\lambda=1, F(u,b)=(u,-\sqrt{|u|}),S=\{0\}\times\mathbb R\)。唯一根 \(T(a,b)=(a/2,b+\sqrt{|a|/2})\) 的最近锚为 \((0,b)\)，反射到它的距离为 \(\sqrt{2|a|}\)。完整真残差平方为 \(u^2+|u|\)。取原 \(R=1/16,\bar t=1,\omega(t)=\sqrt{2t},\psi(s)=s^2,\kappa=3/4,U=X\)，在全窗 \(B(R)<1, \psi(B(t))/t\le(33+8\sqrt2)/64<3/4\)。可用 \(P=\{(0,0),(0,1)\}\) 及上述显式 \(D,h\)，每个条带初值得到原轨道。反射对 \(t\downarrow0\) 没有有限线性模。其全对比较的常数可以比最近锚常数大，导入并未替换原 \(\sqrt{2t}\)。

<a id="finite-anchor-monotone"></a>

## 4. 经典极大单调 PPA 及参数边界

设 \(F\) 是有限维全空间上的极大单调关系，\(S=F^{-1}(0)\ne\varnothing\)，并不要求 \(\operatorname{dom}F=X\)。对每个 \(\lambda>0\) 和每个输入，Minty 满射定理给唯一原根。用到的外部结论仅为这条覆盖与唯一性，见 Rockafellar 1976, *Monotone Operators and the Proximal Point Algorithm*, pp. 877–878, (1.5)–(1.6)，作者原文 <https://sites.math.washington.edu/~rtr/papers/rtr066-MonoOpProxPoint.pdf>。其假设为实 Hilbert 空间和极大单调图，此处均满足。

任选 \(p_0\in S\)，令 \(D=\overline B(p_0,\|z-p_0\|)\)。对任意原根 \(y\) 和 \(p\in S\)，因 \((p,0)\in\operatorname{gph}F\)，单调性给 \(\langle y-p,v\rangle\ge0\)。平方展开对 \(p_0\) 得 \(y\in D\)；对 \(S\) 任一有限仿射基 \(P\) 即得 (1)，取 \(h=0,c=1\)。在 \(D\) 中取所有真实图弦为 \(\Gamma\)。若 \(y_j\in Y,r_F(y_j)\to0\)，取 \(v_j\in F(y_j),\|v_j\|\le r_F(y_j)+1/j\)。任一收敛子列的极限 \(y_*\) 与 \(v_j\to0\) 同用，每个图点 \((u,w)\) 均满足 \(\langle y_*-u,-w\rangle\ge0\)。最大性强制 \((y_*,0)\in\operatorname{gph}F\)。有界性及距离连续性因此给 \(d(y_j)\to0\)。这证明正则性在有限维每个有界窗内自动具备，没有附加线性误差界。

非平坦与非线性速率的区分可用 \(F(a,n)=(0,n^3)\)，\(S=\mathbb R\times\{0\}\)。此图由凸函数 \(n^4/4\) 的梯度给出，或以全域连续单调性沿直线检验极大性。全空间完整真残差为 \(|n|^3\)，原根由 \(b=n+\lambda n^3\) 唯一决定，\(d(y)/d(x)=1/(1+\lambda n^2)\to1\)。整个 \(\lambda>0\) 窗适用。

对于直接能给 \(\langle y-p,v\rangle\ge-\rho\|v\|^2\) 的有限锚 \(p\in P\)，\(\lambda>2\rho\) 给 (1) 的 \(h=0,c=1-2\rho/\lambda>0\)。覆盖、分点和完整残差识别仍逐项核验。例如 \(F(y)=-by,b>0,S=\{0\}\) 给 \(\rho=1/b\)，全图精确真残差 \(b|y|\)。\(\lambda b>2\) 时 \(y=x/(1-\lambda b)\)，中心零的闭区间为不变 \(D\)，该 \(c\) 可用。\(0<\lambda b<2,\lambda b\ne1\) 的唯一非零轨道扩张，\(\lambda b=1\) 时非零输入无根，\(\lambda b=2\) 时二周期，均不能在非零初值达成本定理的结论。只在这个标量族声明这条分界。

Luke–Tam 原刊 Theorem 2 的同球留域子句已有反例。C340 在全部原 Assumption 2 与严格参数门下构造了每个正半径球都有输入的唯一完整根出球的线性算子；该例的原轨道仍全部收敛。上述独立行取有限维极大单调 PPA。文中没有给出 Luke–Tam 其余前提在不同初值域与工作域上的完整导入。[C340 的同球反例](lt_ball_localization_obstruction.md#lt-ball-counterexample)

<a id="finite-anchor-separation"></a>

## 5. 单个测距零锚与全部零锚的严格分离

设 \(X=\mathbb R\times\mathbb R^2\)，\(J(w_1,w_2)=(-w_2,w_1)\)，固定 \(A,R,\lambda>0\)。以 \(r=\|w\|\) 定义单值连续原算子
\[
 F(a,w)=(a r^2,rJw),\qquad S=\mathbb R\times\{0\},\qquad
 D=[0,A]\times\overline B(0,R).
\]
对任一输入 \((u,\xi)\)，输出 \((a,w)\) 满足
\[
 (u,\xi)=((1+\lambda r^2)a,(I+\lambda rJ)w).
\]
标量 \(r\mapsto r\sqrt{1+\lambda^2r^2}\) 在 \([0,\infty)\) 严格递增且满射，故先从 \(\|\xi\|\) 求唯一 \(r\)，再以可逆矩阵恢复 \(w\)，以正数 \(1+\lambda r^2\) 恢复 \(a\)。所得 \(w\) 确有指定范数，因为该矩阵的两个奇异值均为 \(\sqrt{1+\lambda^2r^2}\)。在 \(\xi=0\) 时 \(w=0,a=u\)；在 \(u=0\) 时 \(a=0\)。所有边界点的完整原根都留在 \(D\)。\(S\) 是全空间完整零集，\(d(a,w)=r\) 且 \(r_F(a,w)=r^2\sqrt{1+a^2}\)，从而全空间 \(d\le\sqrt{r_F}\)。

取 \(P=\{(0,0)\}\)；其测距在 \(S\cap D=[0,A]\times\{0\}\) 上为 \(a^2\)，单射。没有把完整目标换成半轴。对 \(v=F(a,w)\)，\(\langle(a,w),v\rangle=a^2r^2\ge0\)。故同一完整关系以 \(h=0,c=1\) 在整个 \(D\) 通过 (1)。对任意 \(0<a_*<p\le A\) 和 \(r>0\)，与零图点 \(((p,0),0)\) 配对得到 \((a_*-p)a_*r^2<0\)，说明该图在这个窗口并非单调。

任意 \(r_0>0\) 的唯一原轨道满足
\[
 r_k^2=r_{k+1}^2(1+\lambda^2r_{k+1}^2),\qquad
 {1\over r_{k+1}^2}-{1\over r_k^2}
    ={\lambda^2\over1+\lambda^2r_{k+1}^2}\le\lambda^2.
\]
递减半径的极限只能为零。因此 \(r_{k+1}/r_k\to1\)，任意正半径窗上均无统一 \(\kappa<1\) 给出原距离收缩。另一方面 \(r_k^2\ge(r_0^{-2}+k\lambda^2)^{-1}\)，故 \(\sum r_k^2=\infty\)。真实步长为 \(\lambda r_{k+1}^2\sqrt{1+a_{k+1}^2}\)，物理总长度发散。此图不能由承诺全部实际轨道有限长度的 [C277 主定理](../../canonical/unified_ppa_joint_certificates.md#ujc-theorem)认证，亦不能满足原 RLEB 或 [C320](../../canonical/ppa_two_step_and_directional_residual.md#td-directional) 的固定因子。[C329](mother_fitzpatrick_bridge.md) 需要的线性真残差界在 \(a=0,r\downarrow0\) 失败。

**即使允许径向补偿，全部局部零锚也不够。** 固定同一 \(F,\lambda,S,D\) 和全部输入，假设 (1) 对每个 \(p\in S\cap D\) 成立，允许任意固定 \(c>0\) 和任意有限非负径向 \(h\)。固定 \(0<a_*<p\le A\)。给任意小 \(q>0\)，取输出 \((a_*,w)\)，\(\|w\|=q\)，记输入法向半径 \(t=q\sqrt{1+\lambda^2q^2}\)。由于 \(a_*<A\)，可预取 \(q_*>0\)，使全部 \(q\le q_*\) 的输入与输出均在 \(D\)。在同一原弦上直接代入这一指定零锚得到
\[
 h(t)-h(q)\ \ge\
 2\lambda(p-a_*)a_*q^2-(1-c)\lambda^2(1+a_*^2)q^4
 \ \ge\ \lambda(p-a_*)a_*q^2                                  \tag{5}
\]
对所有充分小 \(q\) 成立，\(c\ge1\) 时最后一步直接成立。选 \(r_0\) 小于该统一阈值，按上述实际法向半径递推获得 \(r_j\)。逐一以 \(q=r_{j+1},t=r_j\) 应用 (5)，给
\[
 h(r_0)\ \ge\ h(r_N)+\lambda(p-a_*)a_*\sum_{j=0}^{N-1}r_{j+1}^2
 \ \longrightarrow\ \infty ,
\]
与 \(h(r_0)\) 有限矛盾。用来检验 (5) 的输出在每个法向尺度都重新取相同 \(a_*\)，所以仅将标量不等式相加，并未假称这些辅助弦在原空间上下拼接。每条都是固定完整窗必须覆盖的真实弦。这排除了同一窗所有局部零锚的补偿条件，对 C277 伴随的 JP19–JP20 全锚版本尤其有效。若另缩到逐起点的较薄工作集，此处分离不能自动外推过去。

<a id="finite-anchor-branch"></a>

## 6. C322 同一初值的可续选根

取 [C322](../../canonical/ppa_native_alignment_and_transverse_test.md#native-sharp) 的原物理空间 \(X=\mathbb R^2\times P_0\)，两粒子一维、零均速，\(F(q,p)=(-p,L(q)p)\)，\(S=\mathbb R^2\times\{0\}\)。固定均值位置，\((a,b)=(q_2-q_1,p_2-p_1)\)。均值位置随每个准确步不变，此平片内任意两状态的物理距离平方是两项差分坐标的通常距离平方乘 \(1/2\)。特别地 \(d(a,b)=|b|/\sqrt2\)，完整纤维是给定原场的一个值，其残差为
\[
 r_F(a,b)=\frac{|b|}{\sqrt2}\sqrt{1+\phi(|a|)^2}\ge d(a,b).
\]
取 \(\lambda=100,\phi(s)=(1+s^2)^{-1}\)，原初值 \(z=(0,1/3)\)。在该平片预定
\[
 D=\{z\}\cup\{(a,b):a,b\ge0,\ a+100b\le1\}.
\]
首步令输出分离为 \(u\)，原方程为 \(f(u)=u/100+u/(1+u^2)=1/3\)。有 \(f(0)=0\)，\(f(1/2)=81/200>1/3\)，故有 \(0<u<1/2\) 的根，输出速度差是 \(u/100\)，且 \(u+100(u/100)<1\)。另 \(f(30)=3/10+30/901<1/3\)，\(f(31)=31/100+31/962>1/3\)，存在 \(u>30\) 的大根，未进入 \(D\)。这是完整同一个原图，没有删改 \(F(y)\) 来评价残差。

任意三角形内输入 \((a,b)\) 至少有一个根，因 \(s\mapsto(s-a)(1+100\phi(s))\) 在 \(s=a\ge0\) 为零并趋于无穷，可以取值 \(100b\)。每个根都满足原方程 \(a'=a+100b'\)，\(b=(1+100\phi(|a'|))b'\)。故 \(0\le b'\le b,\ a\le a'\le a+100b\le1\)。于是 \(\phi(a')\ge1/2\)，\(b'\le b/51\)，且 \(a'+100b'=a+200b'\le a+100b\le1\)。\(b=0\) 时恰为原地根。这样就证明整块的后续覆盖，未经任何无限轨道假设。

取零点 \(p_*\) 与 \(z\) 有相同均值位置、分离 \(1\)、速度 \(0\)。在 \(S\cap D\) 上，测距平方 \((1-a)^2/2\) 在 \(0\le a\le1\) 单射。对首步被选小根及每个三角形内的后续根，\(a\le a'\le1,\ b\ge b'\ge0\)。因此
\[
 \|x-p_*\|^2-\|y-p_*\|^2
 =\tfrac12\{(1-a)^2-(1-a')^2+b^2-b'^2\}
 \ge\tfrac12\{(a'-a)^2+(b-b')^2\}=\|x-y\|^2 .
\]
(1) 在 \(P=\{p_*\},h=0,c=1\) 下成立。大根本身没有否定存在性；C322 已独立给 \(u>30\) 后面的每个后继发散。通过有限锚检验的分支由同一 \(D\) 可无限继续。


## 7. 证据范围与复核义务

下表记录 M002-v1 的证据位置及其自身尚待独立核验的环节。

| 验收项 | 可重建的证据与待核问题 |
| --- | --- |
| G1 | 第 1–2 节将有限零锚的原图功、支出系数 \(c\lambda^2\) 与完整真残差壳层下界合在 (2) 中。需独立检查有限锚分点与共同径向函数的量词，以及这两项在同一图块上的作用。 |
| G2 | 第 3 节在逐输出最近输入零锚和完整真残差的原窗口内构造 \(D,h\)。需核对原 \(R,\bar t,\lambda,\omega,\psi,\kappa,\mathcal J\)、原严格预算、允许正点跳跃的模，以及 C09 和 C242 的各自范围。 |
| G3–G4 | 第 4 节以全域 Minty 覆盖、单调性及图闭性导入全部正固定步长的有限维极大单调 PPA，另核负标量算子的四种参数行为。完整零集与局部有界性的用途须保留。 |
| G5 | 第 2 节的逐点原根选择在同一 \(D\) 可续，完整真残差给出聚点位置，有限锚分点给聚点唯一。第 6 节给一个物理原场上同初值分根的具体实现，需独立核算首步与后续的原范数。 |
| G6 | 第 5 节在同一个 \(F,\lambda,S,D\) 上给出无穷物理长度、没有统一严格距离因子的实例。固定 \(a_*\) 的 (5) 对整个窗口的真实原弦施测，要求全部局部零锚的任意有限非负径向补偿都不能成立。若更换工作域，这个比较不自动延续。 |
| G7 | 需独立从原关系重建全部根，核 \(r=0,\ a=0\)、完整残差、壳层求和与初值范围，并检查是否存在击穿上述任一箭头的反例。 |

有限锚分点不从有限图样本恢复完整真残差，因而保留 [C337–C339](nonlinear_rl_bridge.md#rl-anchor-independence) 所定位的真残差与长支量词。[C324/C329](mother_fitzpatrick_bridge.md) 的间隙截面解决另一种图对与真残差转接。准 Fejér 列的经典强收敛判别可对照 Combettes 的 Theorem 3.11；本文对有限分点零锚和固定窗口的比较尚未完成公共文献先行性审查。[作者原文](https://pcombet.math.ncsu.edu/ipa.pdf)
