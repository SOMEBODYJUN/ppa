# 原图的跨位置反射—残差相容结构

**C351-v1：数学推导 `derived-checked`；三项任务门的最终接收另见审查记录。**

此处的 \(M\) 是对原始数据逐对检验的一个不等式。在一般原关系上，它精确刻画是否存在同一收缩系数的投稿 RLEB 模。它不扩大该存在性版本所覆盖的原图。两个恢复、分块障碍和与 C315 的重合范围分别说明。数学推导与研究新意的验收是两件事。

<a id="two-point-definition"></a>
## 1. 对象和两点条件

设 \(X\) 为有限维欧氏空间，原关系 \(F:X\rightrightarrows X\)，\(S\subseteq F^{-1}(0)\) 非空闭，\(\lambda>0\)，\(d(x)=\operatorname{dist}(x,S)\)。固定开集 \(U\)、\(R>0\)、输入 \(U_R=U\cap\{d\le R\}\) 和每个输入的非空原允许根集 \(\mathcal J(x)\subseteq (I+\lambda F)^{-1}(x)\)。记真实允许边集 \(\mathcal E=\{(x,z):x\in U_R,\ z\in\mathcal J(x)\}\) 和实际输出集 \(Y=\mathcal J(U_R)\)。对于边 \(e=(x,z)\) 定义
\[
 t_e=d(x),\qquad
 a_e=\min_{p\in P_S(x)}\|2z-x-p\| .
\]
最近输入锚集非空紧，选择该反射的最小值正好表达投稿 (P2) 的存在量词。对 \(y\in Y\) 定义 \(q_y=d(y)\)、\(\rho_y=\lambda\inf_{v\in F(y)}\|v\|\)，始终使用完整输出纤维，容许不达到。另用符号 \(0_*\) 表示数对 \((t_{0_*},a_{0_*})=(0,0)\)；它代表任何允许模的非负标量底限，不充当一条新增 PPA 边。记 \(\mathcal E_*=\mathcal E\cup\{0_*\}\)。固定 \(0<\kappa<1\)，定义
\[
 \boxed{\quad
 q_y\ \le\ \kappa\max\{t_e,\;2\rho_y-a_e\}
 \qquad(y\in Y,\quad e\in\mathcal E_*).
 \quad}                                                     \tag{M}
\]
两次量化彼此独立。等价地，当 \(t_e<q_y/\kappa\) 时，整纤维下端必须满足 \(2\rho_y\ge q_y/\kappa+a_e\)。若 \(t_e=q_y/\kappa\) 此边不限制 \(a_e\)；这个严格边界不能改。特别地，一个位置的完整短图值可以排除另一个原输入处的反射方向。

<a id="two-point-distance"></a>
## 2. 精确图形距离和兼容判据

置
\[
 W(t)=\sup_{\substack{e\in\mathcal E_*\\t_e\le t}}a_e,\qquad
 H(t)=\tfrac12[t+W(t)]\quad(0\le t\le R),\qquad
 Q(u)=\sup\big(\{q_y:y\in Y,\ \rho_y\le u\}\cup\{0\}\big).
\]
零符号和零基线分别处理空源壳和空残差级集。先假定 \(W(R)<\infty\)。对每条实际边 \(e=(x,z)\)，用同一最优最近锚 \(p\) 对 \(x-p\) 和 \(2z-x-p\) 取半和与半差，得到
\[
 d(z),\ \|x-z\|\le \tfrac12(t_e+a_e)\le H(t_e),\qquad
 \rho_z\le \|x-z\|.
                                                               \tag{1}
\]
从而一切实际 \(\rho_y,q_y\le H(R)\)，且 \(Q\) 有限非减。定义边柱集
\[
 C=\bigcup_{e\in\mathcal E_*}\{t_e\}\times(-\infty,a_e]\subset\mathbb R^2 .
\]
对 \(0\le u\le H(R)\) 有精确恒等式
\[
 \begin{aligned}
 L(u)&=\operatorname{dist}_{\infty}((0,2u),C)\\
 &=\inf_{e\in\mathcal E_*}\max\{t_e,\,2u-a_e\}\\
 &=\inf\{t\in[0,R]:H(t)\ge u\}.                         \tag{2}
 \end{aligned}
\]
第一等号按到每根竖直下半线的 \(\ell_\infty\) 距离计算；\(t_e\ge0\) 已包括 \(2u-a_e<0\) 的情形。对第二等号，记右边为 \(L_0\)。对任一边令 \(b=\max\{t_e,2u-a_e\}\)。若 \(b\le R\)，则 \(2H(b)\ge b+a_e\ge2u\)；若 \(b>R\)，则 \(L_0\le R<b\)。故 \(L_0\le\inf_e b\)。反方向，任选 \(H(t)\ge u\) 的尺度。在 \(t_e\le t\) 内取 \(a_e\to W(t)\) 的边或零符号，得到 \(\limsup b\le\max\{t,2u-W(t)\}\le t\)。再取下确界，结论成立。证明没有交换上下确界，没有要求极值、纤维最近图值或模的单侧极限取到。

据此，无需任何正点连续性，
\[
 (M)\quad\Longleftrightarrow\quad q_y\le\kappa L(\rho_y)\ (y\in Y)
 \quad\Longleftrightarrow\quad Q(H(t))\le\kappa t\ (0\le t\le R).
                                                               \tag{3}
\]
最后的等价直接将 \(H(t)\ge\rho_y\) 与 \(q_y\le\kappa t\) 配对。若给定 \(u\) 恰是跳点阈值，使用收集 \(\rho_y\le u\) 的实际集合和 (2) 的真实下确界。倘若只对 \(\rho_y<u\) 检验，将漏掉某些完整小图值。

因此，除可和性外，同一窗口可认证的最佳兼容因子是
\[
 \kappa_*=\sup_{\substack{y\in Y\\e\in\mathcal E_*}}
      \frac{q_y}{\max\{t_e,\;2\rho_y-a_e\}} .                \tag{4}
\]
约定 \(0/0=0\)、正数除零为 \(+\infty\)、空上确界为零。给定 \(0<\kappa<1\) 时判据恰为 \(\kappa_*\le\kappa\)，边界等号允许。若固定同一原 \(F\) 而把政策、源壳或图块分成任意族 \(\mathcal E=\bigcup_i\mathcal E_i\)，并令 \(Y_i\) 为相应输出，则 (4) 正好是所有块对 \((i,j)\) 的上确界，\(e\in\mathcal E_i\cup\{0_*\},y\in Y_j\)。同一原图在每一块分别可用某组模，只控制 \(i=j\)。所有交叉块给出可否使用**同一组**原模的完整附加条件。如果分别原算子也改变，则必须用联合任务中的实际完整残差重新计算。

<a id="two-point-characterization"></a>
## 3. 一般投稿 RLEB 的双向判定及原 PPA

固定上面的覆盖、\(S,U,R,\lambda,\mathcal J,\kappa\) 和一个给定的真实残差帽 \(\bar t>0\)。记 \(\Theta_H(t)=\sum_{j\ge0} H(\kappa^j t)\)。以下两项等价。

* 存在原投稿 (P2)–(P4) 允许的有限非减模 \(\omega:[0,R]\to[0,\infty),\psi:[0,\bar t]\to[0,\infty)\)，二者在零处连续、取零值；在同一帽、同一原允许图和同一 \(\kappa\) 成立。
* (M) 成立，且 \(H(R)\le\lambda\bar t,\ \Theta_H(R)<\infty\)。这里可以先允许 \(W\) 为扩展值；可和性令 \(W(R)\) 有限、\(W(0)=0\) 且 \(W(t)\to0\) 当 \(t\downarrow0\)。

**正向。** 每一组真正给定的原参数均有 \(W(t)\le\omega(t)\)。写 \(B(t)=(t+\omega(t))/2\)，有 \(H(t)\le B(t)\)、\(\Theta_H\le\Theta_B\)、\(H(R)\le\lambda\bar t\)。对所有 \(\rho_y\le H(t)\) 的实际输出，原 (P3)、原帽及 (P4) 给
\[
 q_y\le\psi(\rho_y/\lambda)\le\psi(B(t)/\lambda)\le\kappa t.
\]
\(t=0\) 由零模同样成立。故由 (3) 得 (M)，未调用原收敛定理。也可逐对直接证明：若 \(t_e<q_y/\kappa\)，则对 \(s\in[t_e,q_y/\kappa)\) 的任意合法尺度，(P2) 给 \(a_e\le\omega(s)\)，(P3)–(P4) 禁止 \(\rho_y\le B(s)\)；以 \(s\uparrow q_y/\kappa\) 获得 (M) 的原始耦合不等式（\(q_y\le\kappa R\) 先由全帽取得）。原 \(\omega,\psi\) 可以在每个正点跳跃。

**反向。** 取 \(\omega_*=W,\ \psi_*(u)=Q(\lambda u)\) 对 \(0\le u\le\bar t\)。可和性给 \(\omega_*\) 在零处连续。由零符号的 (M) 有 \(q_y\le2\kappa\rho_y\)，故 \(Q(u)\le2\kappa u\) 且零处连续、零值为零。(1) 给所有实际输出处的 \(Q\) 有限和真帽。(P2) 在原最近输入锚上由 \(a_e\le W(t_e)\) 得到，(P3) 是完整原残差的 \(q_y\le Q(\rho_y)\)，同一 \(\kappa\) 的 (P4) 由 (3) 得出。此方向恢复**一组规范模**，不意味着给任意事先指定、可能过小的 \((\omega,\psi)\) 都成立。若残差帽原来可选，可以取任何 \(\bar t\ge H(R)/\lambda\)；若固定得更小，必须保留帽条件。

**动力学。** 任取真实当前边 \(e=(x,z)\)，(1) 给 \(2\rho_z-a_e\le t_e\)。由 (M) 得
\[
 d(z)\le\kappa L(\rho_z)\le\kappa d(x),\qquad
 \|x-z\|\le H(d(x)).
                                                               \tag{5}
\]
对相邻允许步 \(y\to z\) 且 \(y\in Y\)，另有 \(L(\rho_z)\le d(y)\le\kappa L(\rho_y)\)。此有效标度只用于原迭代，不产生新的近端根。认证域取 \(x^0\in U_R\) 且 \(\Theta_H(d(x^0))<\operatorname{dist}(x^0,X\setminus U)\)，要求其中至少一个初值在 \(F^{-1}(0)\) 外。有限前缀按覆盖选任意下一根，由 (5) 得 \(d(x^{k+1})\le\kappa^{k+1}d(x^0)\)，物理已走长度至多 \(\sum_{j=0}^kH(\kappa^jd(x^0))\)，严格小于离域距离。依次留在 \(U_R\) 并无限续接；有限长使轨道为 Cauchy 列，闭 \(S\) 和严格留域给极限在 \(S\cap U\)。原来用 \(\omega\) 给定的每一个认证初值仍全部保留，因为 \(\Theta_H\le\Theta_B\)。若只承诺那个原域，可全程用更大的 \(\Theta_B\) 预算。


**非解入口的可核条件。** 若存在 \(p\in S\cap U\cap\overline{X\setminus F^{-1}(0)}\)，则上述认证域必含非解初值。可和性先给 \(H(t)\to0\)；又 \(H(\kappa^jt)\le H(\kappa^jR)\)，由级数的支配收敛得到 \(\Theta_H(t)\to0\)。取 \(\varepsilon>0\) 使 \(B_{2\varepsilon}(p)\subset U\)，再取 \(0<\delta<\min\{R,\varepsilon\}\) 使 \(\Theta_H(\delta)<\varepsilon\)。每个 \(x\in B_\delta(p)\) 都满足 \(d(x)\le\delta\) 和 \(d(x,U^c)>\varepsilon\)，因此均被认证；积聚假设保证其中有非解。若没有这类积聚假设，也必须直接核定认证域含非解，不能用只有驻定解的退化任务满足本轮要求。

**所覆盖的原始方向与正则类别。** 总入口是原最近输入锚 RL 与任意有限非减、零连续的真残差模 \(\psi\)，按原整窗条件匹配；不要求线性或二次模。普通全对单调在零锚处给 \(a_e\le t_e\)，所以 \(\omega(t)=t\) 配任何满足 \(\psi(t/\lambda)\le\kappa t\) 的真模即可。对 \(d(y)\le K r_F(y)\)，\(K/\lambda\le\kappa<1\) 是本结构的一组充分参数条件；这里不声称覆盖普通单调 PPA 的全部步长。

另一明确类别是允许零锚的负共单调估计 \(\langle z-p,v\rangle\ge-\nu\|v\|^2\)，\(v=(x-z)/\lambda\)、\(\nu\ge0\)，\(\lambda>2\nu\)。展开原平方给 \(t^2\ge(1-2\nu/\lambda)\|x-z\|^2\)，以及
\[
 a_e^2\le t^2+(4\nu/\lambda)\|x-z\|^2
 \le \frac{\lambda+2\nu}{\lambda-2\nu}\,t^2.
\]
取 \(L=\sqrt{(\lambda+2\nu)/(\lambda-2\nu)}\)，任何完整真模 \(\psi\) 若满足 \(\psi((1+L)t/(2\lambda))\le\kappa t\) 及原帽，就导入同一 \(\mathsf M_\kappa\)；线性 \(H\) 的几何可和性自动成立。全对负共单调可与 \((p,0)\) 配对给该零锚估计。根覆盖始终使用本节共同声明的原 \(\mathcal J\)，不从方向或误差不等式单独臆推出存在性。

<a id="two-point-recoveries"></a>
## 4. 同一非线性参考模的两个精确恢复

两条切片都取全尺度 \(U=X\) 和非空仿射 \(S\ne X\)。检验 (M) 的所有有限半径，不在任何单一有限 \(R\) 处截断。局部可和性须对每个有限起始尺度成立。全尺度使任一指定 \(q/\kappa\) 的两边都可探测；不宣称把全遍历切片不加修改地截成同一有限半径还能保留反向。一般原 RLEB 的有限窗导入已经在第 3 节独立证明。

固定一个连续非减、零处取零的参考反射模 \(\omega_0\)，使 \(g(t)=(t+\omega_0(t))/2\) 严格递增到无穷。规定同一组 \(\kappa,\lambda,S,\omega_0\)；所比较的真正则模为 \(\psi_0(r)=\kappa g^{-1}(\lambda r)\)。若在两个切片上附加原 PPA 的有限长度结论，取 \(\sum_{j\ge0}g(\kappa^jT)<\infty\) 对每个有限 \(T\)。

**A，完整图值的幅度由输出半径决定，方向自由。** 令 \(Y\) 的距离半径遍历全部 \([0,\infty)\)。例如原关系在每个 \(y\) 有值并检验全部真实根；仍须另证所有输入有根。假设 \(\lambda F(y)\) 是半径 \(g(d(y)/\kappa)\) 球面上的任意非空集合；不预设该集合的方向或任何最近锚反射界。事实上只须其全纤维半径下确界等于此数。给定边 \(e\)，因可取任意 \(q_y=\kappa r\)，(M) 要求 \(r\le\max\{t_e,2g(r)-a_e\}\) 对全部 \(r\ge0\)。对 \(r>t_e\) 它恰为 \(a_e\le 2g(r)-r=\omega_0(r)\)。令 \(r\downarrow t_e\) 即得
\[
 (M)\quad\Longleftrightarrow\quad
 a_e\le\omega_0(t_e)\quad(\text{每条原允许边}).
                                                               \tag{6}
\]
反向只用 \(\omega_0\) 非减。右端是原最近输入锚的指定模 RL 次单调性。当指定 \(\omega_0(t)=t\)、\(S=\{0\}\)、原 \(F\) 为单值线性且取完整图时，(6) 又恰为通常全对单调；全对图差在此确实再次是原图点。一般非线性原图只恢复所明示的最近输入锚 RL。若 \(\omega_0\) 有正点右跳，这个全尺度 A 只测试 \(\omega_0(t_e+)\)，因此 (6) 明确保留参考模连续性（右连续也足够）。第 3 节对每个原 \(\omega\) 的导入没有这个限制。

**B，原反射落在给定半径的球面，方向自由。** 以原允许映射的几何给条件，例如在仿射目标的唯一 \(p=P_S(x)\) 下，原允许根均写成
\[
 z=\tfrac12[x+p+\omega_0(d(x))u],\qquad \|u\|=1 ,
\]
其中方向的非空集合可依输入而变，所选 \(z\) 必须原本就是真实近端根。对每个源半径都有输入。这规定反射的长度，不限定完整 \(r_F(y)\) 的任何下界。于是 \(a_e=\omega_0(t_e)\) 且每个 \(t\ge0\) 均有边，故 (2) 化为 \(L(u)=g^{-1}(u)\)。由 (3) 得
\[
 (M)\quad\Longleftrightarrow\quad
 d(y)\le\kappa\,g^{-1}(\lambda r_F(y))\qquad(y\in Y).       \tag{7}
\]
允许关系不等于全部根时 (7) 仍对完整 \(F(y)\) 取下确界。也可用每个源半径的近极值反射逼近同一 \(\omega_0\) 来放宽 B。本节两组前件固定的是不同的、可在原图检查的几何。A 不先假设待恢复的方向，B 不先假设待恢复的真正则。

<a id="two-point-necessity"></a>
## 5. 恢复关系中跨位置检验不可删除的证明

同一参数取 \(0<\gamma<1,\ 0<\kappa<1,\ \omega_0(t)=t+t^\gamma\)，故 \(g(t)=t+t^\gamma/2\)。取 \(X=\mathbb R^2,S=\mathbb R\times\{0\}\)，\(\lambda\) 任意固定。\(g\) 的几何采样可和。以下两项专门验证删除 (M) 中独立位置会同时破坏两个恢复。两图都是全域唯一完整 PPA，及早固定所有非解初值可测试。原始输入的切向坐标记 \(b\)、法向坐标记 \(n\)，半径 \(t=|n|\)。

* **A 的严格对照。** 给定完整原映射 \(J_A(b,n)=(b+\ell_A(t),\kappa n)\)，其中 \(\ell_A(t)=\sqrt{g(t)^2-(1-\kappa)^2t^2}\)。令 \(\lambda F_A=J_A^{-1}-I\)。法向按常数缩放、切向只按源半径平移，所以 \(J_A\) 是全局双射。其完整零集为 \(S\)，对 \(t>0\) 有 \(\ell_A(t)>0\)。在每一条真实边上 \(q=\kappa t\) 且 \(\rho=s=\|x-J_Ax\|=g(t)=g(q/\kappa)\)，完全属于 A。由于输入最近锚位移是法向而反射位移具有非零切向分量，三角不等式严格，\(2s<t+a_e\)。于是 \(a_e>2g(t)-t=\omega_0(t)\)。每条实际自身图对都满足 (M)，而每个非零源均违反 (6)，相应的非对角检验必然失败。
* **B 的严格对照。** 令 \(\beta=2\kappa-1\)，\(\ell_B(t)=\tfrac12\sqrt{\omega_0(t)^2-\beta^2t^2}\)，定义 \(J_B(b,n)=(b+\ell_B(t),\kappa n)\)、\(\lambda F_B=J_B^{-1}-I\)。同样全局双射，完整零集为 \(S\)。每个非零源的反射位移长度 \(\sqrt{4\ell_B(t)^2+\beta^2t^2}=\omega_0(t)\)，属于 B，且这个非线性幅度是原图实际所需。仍由严格三角不等式 \(s<g(t)\)。因为完整根的反向输入唯一，\(\rho=s\)，于是 \(q=\kappa t>\kappa g^{-1}(\rho)\)，(7) 在每个非零输出失败。自身图对仍全部通过。

两例均不能用其同边收缩后端拒绝。它们否定把 (M) 中的 \(y\) 强行等同于 \(e\) 的输出，即便这种退化还保留 \(q\le 2\kappa\rho\) 作为虚拟零边的额外检验：若要求连零边一起在全空间满足，可选相同 \(\kappa\le1/2\)，A 有 \(\rho=g(t)\ge t\)，B 有 \(\rho\ge(1-\kappa)t\ge t/2\)。因此真正需要的是另一条**非虚拟真实边**。两例各自的 PPA 动力都点收敛；被拒的是两条要恢复的原性质，不能将此写成发散。

两切片也实际能通过。A 可取纯法向原图值 \(\lambda F(a,n)=(0,\operatorname{sgn}(n)g(|n|/\kappa))\)。其完整近端全局覆盖，反射长度至多输入距离，故 (6) 成立。B 保持反射半径 \(\omega_0(t)\)，将上式中的法向系数 \(\kappa\) 改成 \(\alpha=\kappa 2^{-1/\gamma}/2\)，令 \(\beta=2\alpha-1\)，相应平移仍取 \(\frac12\sqrt{\omega_0(t)^2-\beta^2t^2}\)。则
\[
 \rho=s=\tfrac12\sqrt{\omega_0(t)^2+(1-2\beta)t^2}\ge\omega_0(t)/2
 \ge g(2^{-1/\gamma}t).
\]
后一不等式由 \(2^{-1/\gamma}\le1/2\) 及 \( (2^{-1/\gamma})^\gamma=1/2\) 直接得到。因此 \(q=\alpha t\le\kappa g^{-1}(\rho)\)。两种通过的图均有任意非解认证初值、无限步、有限长与原空间极限。

<a id="two-point-prior"></a>
## 6. 与已有下逆的准确关系

[C315 的基线及其旧条件导入](../../canonical/rleb_residual_filtered_angle.md#rfa-strict) 已经证明，对于**给定**原反射上界 \(\omega\)，其 \(B(t)=(t+\omega(t))/2\) 与 \(a_\omega(y)=\inf\{t:B(t)\ge\lambda r_F(y)\}\) 满足 \(d(y)\le\kappa a_\omega(y)\le \kappa d(x)\) 以及 \(d(y)\le2\kappa\lambda r_F(y)\)。[同文两张表](../../canonical/rleb_residual_filtered_angle.md#rfa-comparison)的第一张已经使用该下逆来判定原边。本文 (2) 的 \(L(\rho_y)\) 正是拿**最小反射上包络 \(W\)** 作为该原模时的 \(a_\omega(y)\)，不是另一种数值尺度。(5) 的距离收缩、下逆时钟与 Dini 输入长度机制均不能作为新原理。

与此逐式重合之后尚有以下独立可证内容。首先，不申报任何一套模时，(M) 给出同一原图两个可以相距任意远的真实位置的**必要且充分**数值相容限制，包含跳跃端点、原帽、任意分块和最优因子 (4)。每个失败来自具体的图点对（当 \(\kappa_*>\kappa\) 时上确界给出严格违反的真实或零边对），而不归因为任意提交的一套模太松。其次，(6)、(7) 以及两项同一真正非线性参考模的全图对照，说明这批非对角不等式承担两个恢复，而且旧自身边下降在二者中都可能对所有非零点成立。与两项匹配不同，删除非对角后同时破坏两个必要恢复；不是把一个只在三个要求测试之外才活跃的例外分支附在上面。第三，源于不同块的单独原模一般不能合并；(4) 确切给出交叉失败量。[C315 的正负半图](../../canonical/rleb_residual_filtered_angle.md#rfa-strict) 已有这种失配的具体机制，不能将分块失配现象本身报作新发现。

这些新增成立与否可独立核验。其推导仍是最小包络和下确界的初等次序运算，(M) 的整个可认证原图类恰是投稿原 RLEB 在模上的存在性投影。故没有声称更大收敛理论、普遍的数学唯一性、对任意完整图恢复通常全对单调或外部首创。独立验收须决定：这个从原始图对强制得到、不能用逐边信息代替的双向兼容判据及两个同参数非线性恢复，是否达到项目所要求的“同一结构”；若要求超出原 RLEB 模的存在性投影，本候选未给出。


<a id="two-point-external"></a>
### 最接近的一手文献与知识层级

**Paper fact。** Luke–Thao–Tam 的 [2018 年正式论文](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2017.0898)，Theorems 2.1–2.2、Definition 2.5，已经把 almost averaged 违反量与 \(T-\mathrm{Id}\) 的 gauge metric regularity 联合用于收缩。因此，“方向允许违反，正则性补偿后收敛”本身是已有思想。Luke–Tam 的 [2025 年正式论文](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)，Definition 2、Proposition 3 与 Assumption 2，直接联合原算子的二次次单调性和线性度量次正则。

**本库结构推导。** 本文消去的是原允许图上任意两套可行的非线性模，把其存在性精确转为 \(\mathcal E\times Y\) 的数值禁配；并给同一非线性参考尺度的两种反向恢复。原最近输入锚和完整原 \(F(y)\) 都是该禁配的输入。它不是上述文献的一个收敛结论换记号；必须另外证明最小 \(W,Q\) 可重建原模、保持跳跃端点，以及非对角项对恢复不可删除。这里的次序运算、广义逆和 Cauchy 收敛后端并不单独主张新颖。未穷尽全部公开文献，公开优先权保持未定。本文自证局部续接，不调用 [C340 已指出问题的 LT 同球覆盖句](lt_ball_localization_obstruction.md#lt-ball-counterexample)。
