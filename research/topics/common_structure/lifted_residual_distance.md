# 原 PPA 的增维真残差锚距及其仿射公式

**版本 M001-v1。Status：candidate。** 这个候选比较所有目标点观察到的原输入与输出，把完整图的真残差作为输出的一个额外正交坐标。仿射目标时，该比较量可精确计算，给出切向漂移的锐积分条件。下文给出逐初值收敛定理的推导及两个基准导入。M001-v1 尚未完成 G1–G7 的独立验收，公开先行性未判定。

<a id="lrd-definition"></a>
## 1　逐初值条件与共同收敛定理

固定有限维欧氏空间 \(X\)、原关系 \(F:X\rightrightarrows X\)、\(\lambda>0\) 和非空闭 \(S\subseteq F^{-1}(0)\)。令 \(J_{\lambda F}(x)=\{y:x-y\in\lambda F(y)\}\)，\(d(x)=\operatorname{dist}(x,S),\ r(y)=r_F(y)=\inf_{v\in F(y)}\|v\|\)，到空集的距离取 \(+\infty\)。在每条原弦 \(y\in J_{\lambda F}(x)\) 上定义
\[
 D(x,y)=\sup_{p\in S}\big[\sqrt{\|y-p\|^2+\lambda^2r(y)^2}-\|x-p\|\big].                 \tag{1}
\]
这比较同一锚 \(p\) 观察到的输入距离与把完整真残差作为额外正交坐标的输出距离。在 \(X\times\mathbb R\) 应用三角不等式，并用 \(r(y)\le\|x-y\|/\lambda\)，得到
\[
 -\|x-y\|\le D(x,y)\le \sqrt{\|x-y\|^2+\lambda^2r(y)^2}\le\sqrt2\|x-y\|.              \tag{2}
\]
所以 (1) 对无界目标也有限，只由原图及固定参数给出。要直接读出原弦的方向，记 \(v=(x-y)/\lambda\) 和 \(E_p(y)=\sqrt{\|y-p\|^2+\lambda^2r_F(y)^2}\)。则
\[
 (E_p(y)-\|x-p\|)(E_p(y)+\|x-p\|)
 =-2\lambda\langle y-p,v\rangle-\lambda^2(\|v\|^2-r_F(y)^2).
\]
同一式保留了所选图值的方向和完整纤维中的最小范数尺度；后式的括号非负，即使真残差的下确界未达到也成立。

对初值 \(z\)，给出含 \(z\) 的集合 \(K\subset X\)、有限非负静态函数 \(h:K\to[0,\infty)\) 和有限非减函数 \(\alpha:[0,\infty)\to[0,\infty)\)，使 \(\alpha(0)=0,\ \alpha(t)>0\ (t>0)\)。不要求 \(K\) 闭或有界，也不要求 \(h\) 连续。定义
\[
 C(x)=\{y\in J_{\lambda F}(x)\cap K:\quad
        \alpha(d(y))\le r(y),\quad D(x,y)\le h(x)-h(y)\}.                              \tag{3}
\]
条件 \(M_{001}(z)\) 要求存在上述 \(K,h,\alpha\)，使每个 \(x\in K\) 的 \(C(x)\) 非空。对指定初值域 \(U_0\subset X\)，覆盖的量词为 \(\forall z\in U_0,\ M_{001}(z)\)；\(K,h,\alpha\) 可依赖 \(z\)。非平凡行还须有 \(U_0\setminus S\ne\varnothing\)。各导入从上游数据构造这些静态对象，并在原图上检验单步可行性。若原定理给非空允许关系 \(\mathcal J\)，可由其中的输出见证非空；额外完整原根是否通过 (3)，由该根同一输出点的完整真残差和几何不等式决定。

**点收敛定理。** 若 \(M_{001}(z)\) 成立，则 \(x^0=z,\ x^{k+1}\in C(x^k)\) 的任意有限前缀都可无限延拓；每条如此选取的轨道在原空间收敛于某个 \(x^\infty\in S\)。对每个 \(p\in S\)，
\[
  \lambda^2\sum_{k\ge0}r(x^{k+1})^2\le2(\|z-p\|+h(z))^2.                              \tag{4}
\]
多值时这控制真残差，不宣称所选位移平方可和。

**证明。** 已构造有限前缀且末点属于 \(K\)，就可按 (3) 再取一个原根，仍在 \(K\)。由递归选择得到无限原轨道。令 \(V_p(x)=\|x-p\|+h(x)\)。同一个根同时对每个 \(p\in S\) 满足
\[
 V_p(x)-V_p(y)\ge E_p(y)-\|y-p\|\ge0,\qquad E_p(y)=\sqrt{\|y-p\|^2+\lambda^2r(y)^2}.
\]
每个 \(V_p(x^k)\) 单调非负，而且 \(E_p(y)\le V_p(x)-h(y)\le V_p(z)\)。故轨道有界，且
\[
 \lambda^2r(y)^2=(E_p(y)-\|y-p\|)(E_p(y)+\|y-p\|)
     \le2V_p(z)(V_p(x)-V_p(y)).
\]
求和得 (4)，包括 \(V_p(z)=0\) 的情形。因此 \(r(x^k)\to0\)。若子列 \(d(x^{k_j})\ge\epsilon>0\)，则正指标上 \(r(x^{k_j})\ge\alpha(\epsilon)>0\)，矛盾。由闭性任一聚点属 \(S\)。对 \(p,q\in S\)，\(\|x^k-p\|-\|x^k-q\|=V_p(x^k)-V_q(x^k)\) 有极限。若 \(p,q\) 为两个不同聚点，该差沿两个子列趋于相反的非零数，矛盾。故有限维有界序列收敛到唯一聚点。聚点不必先属于 \(K\)，也不需 \(h\) 在聚点有定义或连续。

<a id="lrd-rleb"></a>
## 2　投稿 RLEB 的原最近输入零锚与原预算

使用投稿主定理的 P1–P4。取开集 \(U\)、\(R,\bar t>0,\ 0<\kappa<1,\ U_R=U\cap\{d\le R\}\)。\(\omega:[0,R]\to[0,\infty)\)、\(\psi:[0,\bar t]\to[0,\infty)\) 有限非减，只要求在零处连续，均取零。令 \(B(t)=(t+\omega(t))/2,\ \Theta(t)=\sum_{j\ge0}B(\kappa^jt)\)。对每个 \(x\in U_R\)，有非空 \(\mathcal J(x)\subset J_{\lambda F}(x)\)。每个 \(y\in\mathcal J(x)\) 有可依输出变化的 \(p\in P_S(x)=\{p\in S:\|p-x\|=d(x)\}\)，使 \(4\langle y-p,x-y\rangle\ge d(x)^2-\omega(d(x))^2\)。仅在实际输出且 \(r(y)\le\bar t\) 时要求 \(d(y)\le\psi(r(y))\)。保持 \(B(R)/\lambda\le\bar t,\ \Theta(R)<\infty,\ \psi(B(t)/\lambda)\le\kappa t\ (0<t\le R)\)，以及原初值 \(z\in U_R,\ d_0=d(z),\ \Theta(d_0)<\operatorname{dist}(z,U^c)\)。[投稿主定理](../../../发表成果整理/RLEB/sections/theorem_spine.tex)

在同一 \(\omega,\psi,\lambda,F,S,R,\kappa\) 上预先置
\[
 \begin{split}
 K&=\{x:d(x)\le d_0,\ \|x-z\|+\Theta(d(x))\le\Theta(d_0)\},\\
 h(x)&=\sqrt2\,\Theta(d(x)),\\
 \alpha(t)&=\inf\big(\{s\in[0,\bar t]:\psi(s)\ge t\}\cup\{\bar t\}\big).
 \end{split}                                                                           \tag{5}
\]
\(\alpha(0)=0\)；非减性和每个正尺度的正性由 \(\psi(0)=0\) 与零处连续性得到。不需假定正点连续、广义反函数或真残差达到。\(K\subset\overline B(z,\Theta(d_0))\subset U\)，故 \(K\subset U_R\)。

取 \(x\in K,\ y\in\mathcal J(x)\)。对该根的原最近锚，
\[
 \|2y-x-p\|^2=\|x-p\|^2-4\langle y-p,x-y\rangle\le\omega(d(x))^2,\qquad
 2\|x-y\|\le d(x)+\omega(d(x)).
\]
若 \(d(x)=0\)，得 \(y=x\)。若 \(d(x)>0\)，有
\[
 r(y)\le\|x-y\|/\lambda\le B(d(x))/\lambda\le\bar t,\qquad
 d(y)\le\psi(r(y))\le\psi(B(d(x))/\lambda)\le\kappa d(x).
\]
由 (5) 得 \(\alpha(d(y))\le r(y)\)。有限非减函数 \(\Theta(t)=B(t)+\Theta(\kappa t)\) 给出
\[
 \|x-y\|+\Theta(d(y))\le\Theta(d(x)).
\]
三角不等式直接给 \(y\in K\)，(2) 给 \(D(x,y)\le h(x)-h(y)\)。所以全部原允许根通过 (3)，且仍可从这些允许根中继续选择。没有调用旧收敛结论。势中的 \(\sqrt2\) 没有乘进初值预算；\(\overline K\subset U\)。相对不变状态 \(D_0\) 的版本取 \(K\cap D_0\)，极限属于原指定闭目标 \(S\subset D_0\)。

C09 在同一图块、原输入对距尺度上的全对条件及图块最近零锚推出 P2，全对零尺度还保证图块根单值。其 Dini 条件给 \(\sum_{j\ge1}\omega(\kappa^jR)\le(\log(1/\kappa))^{-1}\int_0^R\omega(t)\,dt/t\)，故其原 \(\ell_\omega=\Theta\) 和初值预算不变。投稿的允许多值版本只用逐输出最近零锚。[C09 全对条件](../../canonical/general_modulus_dynamics.md#gm-data)

C242 取 \(F(u,v)=(u,-\sqrt{|u|}),\ S=\{0\}\times\mathbb R,\lambda=1,\ R=1/16,\bar t=1,\omega(t)=\sqrt{2t},\psi(t)=t^2,\kappa=3/4\)。唯一完整根 \((a/2,b+\sqrt{|a|/2})\) 对最近零锚达到反射等号，\(r(u,v)^2=u^2+|u|\)，原兼容比至多 \((33+8\sqrt2)/64<3/4\)。\(\alpha(t)=\min(\sqrt t,1)\)，同一原非线性 \(\omega\) 进入 (5)。完整多值投稿例 \(F(y)=\{2y,3y\},\lambda=1\) 的两个根也均保留。[C242 三角图](../../canonical/triangular_rleb.md#tri-certificate)

<a id="lrd-monotone"></a>
## 3　有限维最大单调完整 PPA

设 \(F\) 最大单调，\(S=F^{-1}(0)\ne\varnothing\)。每个 \(\lambda>0,\ z\in X\) 都在本行范围。任取 \(p_0\in S\)，取 \(K=\overline B(p_0,\|z-p_0\|),\ h=0\)。完整原根全域唯一（证明如下）。对所有 \(p\in S,\ v=(x-y)/\lambda\in F(y)\)，单调性给
\[
 \|x-p\|^2=\|y-p\|^2+2\lambda\langle y-p,v\rangle+\lambda^2\|v\|^2
 \ge\|y-p\|^2+\lambda^2r(y)^2 .
\]
故 \(D(x,y)\le0\)，取 \(p=p_0\) 即知 \(y\in K\)。正则尺度由紧的原图窗给
\[
 \alpha(t)=\inf\big(\{r(u):u\in K\cap\operatorname{dom}F,\ d(u)\ge t\}\cup\{1\}\big).
\]
\(\alpha(0)=0\) 因 \(p_0\in K\)。若 \(\alpha(t)=0\) 对某 \(t>0\)，则取 \(u_j\in K,\ d(u_j)\ge t,\ w_j\in F(u_j),\ w_j\to0\)，再抽 \(u_j\to u\)。图闭，因为任一图极限和全图单调相容，最大性将其纳入图。因此 \(u\in S\)，与 \(d(u)\ge t\) 矛盾。这项定性正则性不承诺线性误差界。\(F(a,n)=(0,n^3)\) 全域连续单调且最大（与 \(u\pm\epsilon e\) 比较再取极限即证）；其 \(r=|n|^3\)，法向距离比例 \((1+\lambda n^2)^{-1}\to1\)，是本行非平凡例。

**有限维满输入的自足证明。** Minty 坐标 \(a=u+\lambda v,\ b=u-\lambda v\) 将单调性转为 \(\|b-b'\|\le\|a-a'\|\)，所以 \(b=b(a)\) 单值。给定 \(x\in X\)，寻找所有球 \(\overline B(b(a),\|x-a\|)\) 的共同点。对任一有限非空子族 \((a_i,b_i)\)，极小化强制函数 \(\max_i(\|b-b_i\|^2-\|x-a_i\|^2)\)。在极小点活动向量 \(b-b_i\) 的凸包含零，否则沿严格分离方向的反向可同时降低活动项，非活动项留有正间隔。因此 \(b=\sum\theta_i b_i\) 可取活动项凸权。其最小值为
\[
 \tfrac12\sum_{i,j}\theta_i\theta_j\|b_i-b_j\|^2-\sum_i\theta_i\|x-a_i\|^2
 \le-\left\|x-\sum_i\theta_i a_i\right\|^2\le0 .
\]
有限交非空，固定一个紧锚球（图非空）可得全交非空。对应新增 Minty 点换回原坐标与全图单调相容，最大性确保已在原图。故任意 \(x\) 有根，同输入的唯一性已由非扩张得证。

Luke–Tam 2025 年正式版 Theorem 2 印刷的同球原根子结论已有反例。C340 中，二维完整线性图满足 Assumption 2 的全部前提，却对每个 \(\delta>0\) 都存在严格位于 \(B_\delta(0)\) 内的初值，其唯一根严格在闭球外，极限也在该球之外。该例的原轨道全域收敛。它排除从原前提直接导入同一个球的留域结论；若改用不同的初值窗和工作窗，仍需证明相应预算。以上采用最大单调 PPA 作为独立基准。一般 KL、变化右端度量正则、一般次单调或非精确更新的全类接口仍开放。[C340 的同球反例与仍成立的动力学](lt_ball_localization_obstruction.md#lt-ball-counterexample)

<a id="lrd-affine"></a>
## 4　正维仿射目标下的精确计算

设 \(S\) 为正维仿射子空间，\(P\) 为正交投影。写 \(u=\|Py-Px\|,\ A=\sqrt{d(y)^2+\lambda^2r(y)^2},\ B=d(x)\)。则
\[
    D(x,y)=\sqrt{u^2+(A-B)_+^2}.                                                    \tag{6}
\]
平移切向原点后，要计算在切平面上 \(\sqrt{\|Py-\xi\|^2+A^2}-\sqrt{\|Px-\xi\|^2+B^2}\) 关于 \(\xi\) 的上确界。若 \(A>B\)，在高一维空间用三角不等式得右侧上界，再取 \(\xi=Px-B(Py-Px)/(A-B)\) 共线达到，上式也包括 \(B=0\)。若 \(A\le B\)，将 \(A\) 提升为 \(B\) 再沿切向平移，得上界 \(u\)。当 \(u>0\) 取 \(\xi=Px-t(Py-Px)/u,\ t\to\infty\)，该差趋 \(u\)；当 \(u=0\) 取任一切向无穷射线，该差趋零。若 \(S\) 仅含一点，实际差可以为负，故等式指明正维。式 (6) 显示切向位移一定产生代价，法向耗散却可直接吸收真残差的平方。

<a id="lrd-integral"></a>
## 5　旋转原场的切向漂移、锐积分条件与无穷物理长度

取 \(X=\mathbb R\times\mathbb R^2,\ S=\mathbb R\times\{0\}\)，\(Q(w_1,w_2)=(-w_2,w_1)\)。令 \(g:[0,\infty)\to[0,\infty)\) 有限非减、在零处连续且 \(g(0)=0\)。固定原算子、步长
\[
 F_g(a,w)=(-g(\|w\|),\,\|w\|^2 Qw),\qquad \lambda>0 .                              \tag{7}
\]
对任意 \(R>0\)，每个 \(0<d(x^0)\le R\) 有唯一完整近端轨道。此轨道点收敛于 \(S\) 的充要条件为
\[
             \int_0^R g(s)s^{-5}\,ds<\infty .                                         \tag{8}
\]
成立时 (3) 在整管 \(K=\{d\le R\}\) 有显式证书；发散时唯一轨道切向趋 \(+\infty\)。任一非零初值的物理总长度在这两种情形均无穷。

写输入和输出的法向半径 \(t=d(x), q=d(y)\)，由原包含得到 \(n=(I+\lambda q^2Q)w,\ t^2=q^2+\lambda^2q^6\)，切向增量 \(U=\lambda g(q)\)。右式关于 \(q\ge0\) 严格递增满射，每个 \(q\) 的矩阵可逆且所解 \(w\) 有正确的范数，故完整根全域唯一。零集恰为 \(S\)，\(r(y)^2=q^6+g(q)^2\)，取 \(\alpha(t)=t^3\)。在 (6) 中 \(A=\sqrt{t^2+U^2}, B=t,u=U\)，故
\[
 D(x,y)=\sqrt{U^2+(\sqrt{t^2+U^2}-t)^2},\qquad U\le D(x,y)\le\sqrt2\,U .             \tag{9}
\]
这是由原法向的正交性与同一个 \(F_g\) 的完整残差得到的精确消去。

置 \(v=\lambda^2q^4\)。当 \(0<q\le t\le R\) 时
\[
 \int_q^t s^{-5}ds=\frac{\lambda^2(2+v)}{4(1+v)^2}
 \in[\beta_R,\lambda^2/2],\qquad
 \beta_R=\frac{\lambda^2(2+\lambda^2 R^4)}{4(1+\lambda^2R^4)^2}>0 .
\]
在 (8) 下，迭代前取
\[
 h(a,w)=\frac{\sqrt2\,\lambda}{\beta_R}\int_0^{\|w\|}g(s)s^{-5}\,ds .
\]
因 \(g(s)\ge g(q)\ (q\le s\le t)\)，有 \(h(x)-h(y)\ge\sqrt2\lambda g(q)\ge D(x,y)\)，\(t=0\) 则驻定。\(q\le t\) 保证整管不变，故共同定理给出结论。反之非零轨道半径 \(t_k\downarrow0\)，这是单调极限代入半径方程的直接结论。因 \(g\) 有限非减，积分发散只可能来自零处。分割 \((0,t_0]\) 并在每个区间以上端 \(g(t_k)\) 控制，得
\[
 \int_0^{t_0}g(s)s^{-5}\,ds\le(\lambda^2/2)\sum_{k\ge0}g(t_k).
\]
积分发散使右侧也发散。去掉首个有限项，切向累计 \(\lambda\sum_{k\ge0}g(t_{k+1})\) 发散，唯一轨道无收敛支。

由同一半径恒等式
\[
 t_{k+1}^{-4}-t_k^{-4}
 =\frac{\lambda^2(2+\lambda^2t_{k+1}^4)}{(1+\lambda^2t_{k+1}^4)^2}
 \longrightarrow2\lambda^2 .
\]
Cesàro 平均给 \(t_k\sim(2\lambda^2k)^{-1/4}\)。实际法向步长为 \(\lambda t_{k+1}^3\)，其和发散。取 \(g(s)=\mu s^m,\mu,m>0\)，(8) 等价于 \(m>4\)；端点 \(m=4\) 对数发散。

**与已有条件的关系。** 法向旋转及其无穷长度在 C277 JP21、VO6–VO8 的 \(g=0\) 已有。取上述 \(m>4,\ \mu>0\) 时，每个非零步有切向位移。沿相反切向趋于无穷的零锚给 \(\|y-p\|>\|x-p\|\)，所以 C277 JP19–JP20 即便取 \(\sigma=0\) 也不适用。实际无穷长度排除了 JP12/13 的联合有限长度条件。\(q/t\to1\) 排除原 RLEB、C319/C320 的固定收缩。此例还有 \(r(y)\sim q^3\)，排除 C329 定量动力学条件的线性真次正则前提。式 (9) 将须由势支付的代价控制在切向原图数据 \(g\) 的尺度上。Fejér/Opial 型聚点论法和可加势已有先例，现有区分针对上述具体条件。[C277 联合证书与 JP19–21](../../canonical/unified_ppa_joint_certificates.md#ujc-theorem) · [VO6–VO8](../../novelty/2026_10_14_submonotonicity/variational_order_review.md) · [C319/C320](../../canonical/ppa_two_step_and_directional_residual.md#td-combined) · [C329](mother_fitzpatrick_bridge.md#mother)

<a id="lrd-stepsize"></a>
## 6　同一原算子的步长边界

令 \(X=\mathbb R^2,\ S=\mathbb R\times\{0\}\)，原图 \(F(a,n)=(-|n|,-c_{\operatorname{sgn}n}n)\)，其中 \(c_+=1,c_-=3,\ F(a,0)=0\)。在 \(\lambda>1\) 时，唯一根的非零法向严格变号。从输入符号 \(s\) 到输出符号 \(-s\)，大小乘 \(q_+=1/(3\lambda-1)\) 或 \(q_-=1/(\lambda-1)\)，切向增量为 \(\tau_s|n|,\ \tau_s=\lambda q_s\)。真实残差为 \(r(y)=\sqrt{1+c_{-s}^2}\,d(y)\ge\sqrt2\,d(y)\)。式 (6) 给 \(D(x,y)=L_s|n|\)，其中
\[
 L_s=\sqrt{\tau_s^2+\big(\sqrt{q_s^2+\tau_s^2+(1+q_s)^2}-1\big)^2}>0 .
\]
若 \(q_+q_-<1\)，令 \(K=X,\alpha(t)=\sqrt2 t,\ h(a,n)=C_s|n|\)，在零处取零，其中 \(C_s=(L_s+q_sL_{-s})/(1-q_+q_-)\)。两恒等式 \(C_s-q_sC_{-s}=L_s\) 给出 (3)。两步法向大小实际乘 \(q_+q_-\)，乘积为 1 或大于 1 时任何非零初值均无收敛至 \(S\) 的原轨道。\(\lambda>1\) 内实际充要阈值为 \(\lambda>4/3\)。当 \(4/3<\lambda<2\)，一支在每个任意小尺度实际放大法向距离，排除每步须满足 JP12 的 C277（含该有限状态版）及 C320；非零切向步也排除 JP20。此处比较始终固定同一原算子，未声称分类 \(\lambda\le1\) 的行为。

<a id="lrd-tests"></a>
## 7　多值选根与边界检验

- **C322。** 在两粒子固定质心的相对差坐标 \((a,b)\) 上，原欧氏位移范数为相对坐标标准范数的 \(1/\sqrt2\)。保持原 \(\lambda=100,\phi(s)=(1+s^2)^{-1},z=(0,1/3)\)。取 \(K=\{z\}\cup\{a,b\ge0,\ a+100b\le1\}\) 的原空间像，\(h=2\sqrt2 b,\ \alpha(t)=t\)。因为原场的位置分量为负速度，所以完整 \(r\ge d\)。初步方程 \(s/100+s/(1+s^2)=1/3\) 在 \(0<s<1/2\) 有根，进第二片。从第二片每个根满足 \(a_+=a+100b_+,\ b=(1+100\phi(|a_+|))b_+\)，故 \(a_+\le a+100b\le1,\ b_+\le b/51,\ a_++100b_+\le a+100b\le1\)。根存在性由连续方程在 \(a_+=a\) 与无穷远之间取值得到，\(b=0\) 时驻定。初步小根也有 \(\phi(a_+)\ge1/2\)。对这些根，实际物理步长不超过 \(100b_+\)，所以 \(D\le100\sqrt2 b_+\le2\sqrt2(b-b_+)\)。首步大根 \(s\in(30,31)\) 不在 \(K\)。该物理选根及每个后继可继续，未将大根误作否定存在性的证据。
- **C339、C337。** C339 完整 \(r(y)=|y|\)，短根 \(y=x/2\) 全域存在。取 \(K=X,\ h=0,\alpha(t)=t\)，\(D=(1/\sqrt2-1)|x|\le0\)。小非零输入的长根 \(D=\sqrt2|y|-|x|>0\) 被筛去。C337 的任意小图值说明 \(\alpha\) 的正性不能从裸最近锚推出。改变 \(F(y)\) 就须重算完整 \(r(y)\)。未使用 C333 的固定输出位移惩罚、C334/C335 的标量图宽度、C336 的全对扩张或 C338 的有限采样推断。
- **\(F(y)=-by,\ b>0\)。** 写 \(\chi=\lambda b\)。\(\chi=1\) 非零初值无根，\(0<\chi<2,\chi\ne1\) 唯一轨道扩张，\(\chi=2\) 非零轨道二周期。因此这些非零初值不能满足 (3)。若 \(\chi>2\)，唯一根 \(y=x/(1-\chi)\)，\(\alpha(t)=bt,\ K=X,\ h(x)=[\sqrt{1+\chi^2}-(\chi-1)]|x|/(\chi-2)\) 在 (1) 中取等。
- **C319 和目标身份。** 其交替非 Dini 漂移的单值原图有点收敛轨道，但步长平方和发散。单值使 \(r(x^{k+1})=\|x^k-x^{k+1}\|/\lambda\)，(4) 阻止 (3)。所以存在收敛本身不蕴含本候选。最大单调导入的完整零集不能任换为真子集，例如 \(F=0\) 的非目标初值始终固定。

上述检验用的原图、原始输入及完整纤维可从各自正文重建。[C322 两粒子分根](../../canonical/ppa_native_alignment_and_transverse_test.md#native-sharp) · [C337 与 C339](nonlinear_rl_bridge.md#rl-anchor-independence) · [C319 的交替轨道](../../canonical/ppa_two_step_and_directional_residual.md#td-cancellation)

<a id="lrd-distinction"></a>
## 8　与补偿锚距条件的单向区分

固定 \(X=\mathbb R\times\mathbb R^2,\ S=\mathbb R\times\{0\},\ \lambda=1\)，令 \(Q\) 是角度 \(\theta=\pi/\sqrt2\) 的平面旋转，\(c>0,\ 1\le\nu<2,\ \beta>\nu\)。考虑同一个完整单值原图
\[
 F(b,w)=\big(-c r^\beta,\ ((1+r^\nu)Q^{-1}-I)w\big),\qquad r=\|w\|.
\]
若输入 \(x=(a,n)\) 的法向半径为 \(t=\|n\|\)，则输出 \(y=(b,w)\) 满足 \(b=a+cr^\beta,\ n=(1+r^\nu)Q^{-1}w,\ t=r(1+r^\nu)\)。该半径方程全域唯一可解。置 \(\sigma_\theta=\sqrt{2-2\cos\theta}>0\)，则
\[
 r_F(y)^2=c^2r^{2\beta}+r^2\big[(1+r^\nu)^2+1-2(1+r^\nu)\cos\theta\big]
 \ge \sigma_\theta^2r^2,
\]
在任意固定管 \(t\le R\)，补偿锚距条件 M003-v2 以正系数的 \(h_*(t)=C_1t^{\beta-\nu}+C_2t^{2-\nu}\) 认证每个初值。具体地，其全锚距离差至多 \(cr^\beta\)，其以固定 \(\ell>0\) 归一化的平方项至多 \(O_{R,\ell,c,\nu}(r^{2\beta}+r^2)\)；对 \(j=\beta,2\)，\(t^{j-\nu}-r^{j-\nu}\ge c_{j,R}r^j\)，其中 \(c_{j,R}>0\)。该条件在同一原根上闭合。[补偿锚距条件的旋转族与显式系数](compensated_anchor_convergence.md#ca-sharp)

增维真残差锚距 (1) 在输入投影锚 \(p=(a,0)\) 给出另一结果。因 \(\|x-p\|=t,\ \|y-p\|\ge r\)，
\[
 D(x,y)\ge\sqrt{1+\sigma_\theta^2}\,r-t
   =\big(\sqrt{1+\sigma_\theta^2}-1-r^\nu\big)r.
\]
充分小的 \(r>0\) 上，右侧至少为 \(\tfrac12(\sqrt{1+\sigma_\theta^2}-1)r\)。令 \(r_k=d(x^k)\)。非零初值的唯一轨道满足 \(r_k\downarrow0\)，且
\[
 r_{k+1}^{-\nu}-r_k^{-\nu}
   =\frac{1-(1+r_{k+1}^{\nu})^{-\nu}}{r_{k+1}^{\nu}}\longrightarrow\nu .
\]
故 \(r_k\sim(\nu k)^{-1/\nu}\)，由 \(\nu\ge1\) 得 \(\sum r_k=\infty\)。若 \(M_{001}(z)\) 成立，唯一原根迫使这条轨道一直通过 (3)；其充分靠后的每个 \(D(x^k,x^{k+1})\) 均有上述正下界，但从任一时刻 \(N\) 起望远镜求和又给 \(\sum_{k=N}^{m}D(x^k,x^{k+1})\le h(x^N)\)。矛盾。因此在这组固定原图、参数与非解初值上，M003-v2 可认证，M001-v1 不可认证。这项比较只证明所示方向的分离。

<a id="lrd-review"></a>
## 9　尚待独立复核的义务

证据由上面的逐弦推导、两个导入、模型边界及反例组成。独立 G1–G7 验收仍未完成；M001-v1 保持 **candidate** 状态。具体须在同一原图及量词下完成以下复核。

| 验收项 | 对照证明与检验重点 |
| --- | --- |
| G1、G5 | 从 (1)–(4) 重建同一根对所有锚的估计、完整残差平方和与双锚差判据，检查 \(K\) 不闭、\(h\) 不连续及无限原根选择时的论证。 |
| G2 | 按投稿 P1–P4 核 §2 的广义正则尺度 (5)、原初值预算、输出评价窗与逐输出最近输入锚；以 C242 的实际非线性原模和投稿多值关系反测。 |
| G3、G4 | 重建 §3 的有限维满输入与紧窗残差分离，核 §6 在同一 \(F,S\) 上的 \(\lambda=4/3\) 及两侧行为。将 [C340](lt_ball_localization_obstruction.md#lt-ball-counterexample) 限定在它实际反驳的同球子句。 |
| G6、G7 | 重算 (6) 的有限锚达到与无穷锚极限、(8) 的两个方向和临界幂；复核 §7 的小根可续、§8 的单向分离，分别与 C277 的两个后端和 C319/C320/C329 的明确条件比较。 |

公开优先性及其他单调结构与正则性组合的覆盖均保留独立问题。[共同充分条件的验收标准](GPT_PRO_PROMPT.md#pro-hard-gates)
