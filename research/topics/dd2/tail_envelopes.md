# 尾部长度的最佳包络、同图实现与认证截断

沿用 [E0](core.md#dd2-exact-contract)。给定实际状态以后，尾长是后续物理步长之和；只留下距离，或把不同算子的边合并，会改变优化对象。本页先固定这三个层次，再证明零缺陷完整类的准确最坏尾，最后校准 C400 的匹配缺陷预算。所有预设目标仍先由原数据认证。

<a id="dd2-optimal-tail-values"></a>
## TV1 · 真实状态值与最小支付函数

固定同一个 F、S、λ、允许关系和输入工作集 \(D=U_R\)。保留每条输入 \(x\in D\) 的受检边，包括最后一步落到 D 外的边；到了 D 外停止，不再增加受检出边。对任意有限前缀
\[
x_0=x,\quad x_{j+1}\in\mathcal J(x_j),\quad x_j\in D\ (j<N),
\]
以 \(\sum_{j<N}\|x_{j+1}-x_j\|\) 为成本，空前缀成本0。定义
\[
V_N(x)=\sup_{\text{至多 }N\text{ 步前缀}}\sum_{j<N'}s_j,\qquad
V(x)=\sup_N V_N(x),\qquad V(x)=0\ (x\notin D).
\tag{TV1}
\]
这里上确界可为无穷，不预设有最大路径。对非负函数 f，令
\[
(Tf)(x)=\sup\bigl(\{0\}\cup
 \{\|x-y\|+f(y):y\in\mathcal J(x)\}\bigr)\quad(x\in D),
\qquad Tf=0\quad(x\notin D).
\tag{TV2}
\]
则 \(V_N=T^N0\)、\(V=TV\)。首边分解给递推；交换两个非负上确界给极限恒等式，不需要最优选择取到。

任意有限非负 W 若支付每条保留边，即 \(W\ge TW\)，归纳得 \(W\ge V_N\)，进而 \(W\ge V\)。反过来，若 V 逐点有限，\(V=TV\) 就是最小非负位置支付函数。这是 [PE1–PE4](../../canonical/unified_ppa_joint_certificates.md#ujc-distance-potential-existence) 在实际状态图上的同一有限前缀原理，不另称新收敛机制。

若每个前缀都能继续为无限合法轨道，则 V 也等于这些真实轨道总长的上确界：一边来自所有部分和，另一边来自每个有限前缀的延拓。若存在死枝，前缀值和只统计无限轨道的值不能混同；没有无限轨道也不能当作所有受检边成本为零。

## TV2 · 距离包络、算子类和局部预算

对确有输入的尺度 t，定义
\[
B_F(t)=\sup_{\substack{x\in D\\d(x,S)=t}}V_F(x).
\tag{TV3}
\]
它首先是该固定图所有这些状态的最小实际前缀预算；若每个前缀均可续接，它也等于全部无限轨道的最小尾上界。可续接是这个相等的充分条件，不声称必要。它一般不是同一步距离势。空尺度须注明无初值；若为书写设其值为0，此值不提供覆盖。给定算子类 \(\mathscr C\)，再取 \(B_{\mathscr C}(t)=\sup_{F\in\mathscr C}B_F(t)\)，每条路径始终留在同一个 F 内。

把固定图的实际边精确投影为 \((t,a,s)\)，再允许这些行在距离上任意续接，所得最小非负距离支付值记为 \(W_F\)。尺度域必须包含全部受检输入和输出，未认证的输入尺度不另添出边；只有先核 \(a\le R\) 时才能直接选 \([0,R]\)。这保留 TV1 的首个出域末边。于是
\[
B_F\le W_F,\qquad
B_{\mathscr C}\le\sup_{F\in\mathscr C}W_F
 \le W_{\bigcup_{F\in\mathscr C}E_F}.
\tag{TV4}
\]
外加安全几何包络只会再增大右端；每一个比较必须保相同的受检尺度和成本。单边可实现并不自动使最后的并边路径在同一原图实现。

[C457](angular_length_obstruction.md#dd2-angular-length-obstruction)有
\(B_F(t)\le(1+2\pi)t\)，却 \(W_F(t)=\infty\) 于每个正尺度；
[C278](../../canonical/unified_ppa_joint_certificates.md#ujc-distance-state)已有两步终止的同类分离。因此把真实径向尾包络当作势差，或者声称距离投影总能在有限倍内逼近真实尾，均不成立。C452 则是 \(B_F=W_F\) 有限但不能规则化的另一种情形。逐轨有限、逐状态有限、逐尺度有限及零端统一消失的量词边界见 [C459](tail_quantifier_obstructions.md#dd2-tail-quantifier-obstructions)。

用于局部留域时，TV1 必须计入首次出域的最后一条边。若已有 \(a\le R\)、输入覆盖，且
\[
V(x_0)<d(x_0,U^c),
\tag{TV5}
\]
则任意首出 U 前缀的成本至少为 \(d(x_0,U^c)\)，又至多 V，矛盾；故全选择留域且可续接。只统计已经留域的无限轨道，会遗漏需排除的出域边，不能用于此归纳。有限长度使点列 Cauchy；识别极限在 S 仍另用距离趋零和 S 闭。严格 TV5 另保极限在 U。

## TV3 · 有限截断怎样给近最佳证书

在同一个状态或尺度关系上，设 W 是有限非负上解 \(W\ge TW\)。定义
\[
L_N=T^N0,\qquad U_N=T^NW .
\]
则
\[
L_N\uparrow V,\qquad V\le U_N\downarrow,\qquad
0\le U_N(x)-L_N(x)\le
 \sup_{\text{恰 }N\text{ 步可达 }y}W(y).
\tag{TV6}
\]
早停路径的末预算取0；无 N 步路径时右端取0。展开两递推，只有走满 N 步的路径多出末值 W(y)，即得最后一式。

若已核非减比较映射 Q、\(d(y,S)\le Q^{\circ N}(t)\)，且
\(W(y)\le\omega(d(y,S))\)，其中 \(\omega\) 非减并在零消失，则误差至多
\(\omega(Q^{\circ N}(t))\)。没有这类末预算条件，不宣称截断上界必趋 V。
在一条实际无限路径上，有限 V 只给
\[
\sum_{j\ge k}s_j\le V(x_k)-\lim_{n\to\infty}V(x_n);
\]
右侧趋0，但不能据此直接把 \(V(x_n)\) 的极限写成0。有限层的上确界仍需可计算的输入合同；无限变分式、有限次黑箱查询和认证误差是不同义务。

<a id="dd2-zero-defect-optimal-tail"></a>
## ZT1 · C458-v1：零缺陷统一类的准确尾值

**状态：derived-checked。三席已独立重构并逐源冷读实际正文、身份、图边及地图，无未关闭实质异议。**

固定 \(\lambda,R>0\)，原 \(D_\psi=[0,\infty)\)，\(\psi\) 有限、连续、非减且 \(\psi(0)=0\)。令
\[
\eta(s)=\psi(s/\lambda),\quad
Q_0(s)=\sqrt{s^2+\eta(s)^2},\quad
b_0=Q_0^{-1},\quad A_0=\eta\circ b_0,\quad
\chi=(\operatorname{id}+\eta)^{-1},\quad
I_\chi(t)=\int_0^t\frac{u}{\chi(u)}\,du .
\tag{ZT1}
\]
两逆均全域连续严格递增；b₀ 不同于原域的步下界 χ。先指定
\(\varphi:[0,R]\to[0,R]\)，且已核 \(A_0\le\varphi\)。
本节量化 \(\Phi=0,U=V_\psi=H\) 的全部 E0 对象，空间为任意有限维实欧氏空间且包含二维，S 为非空闭子零集，每条原允许边满足完整真残差界，同一允许关系在全 R 距离窗非空覆盖。该类包含所有合格的二维闭完整图、精确 \(S=\{0\}\) 和全部近端选择，不另排除下面的见证。

原数据给 \(a\le A_0(t)<t\) 于正尺度；若 \(a>A_0(t)\)，单调性迫使
\(\lambda\rho>b_0(t)\)，与 \(a^2+s^2\le t^2=A_0(t)^2+b_0(t)^2\) 矛盾。
零输入驻定。A₀ 连续非减，故覆盖和距离窗不变使所有路径可续，且 \(t_k\to0\)。

对每个 \(t\in[0,R]\)，令
\[
r_0=t,\quad r_{k+1}=A_0(r_k),\qquad
\mathcal L_*(t)=\sum_{k\ge0}b_0(r_k).
\tag{ZT2}
\]
扩展实数值 \(\mathcal L_*(t)\) 同时等于：

- 同一原数据类从精确初距 t 出发的全部真实轨道长度上确界；
- 自由尺度行 \(0\le a\le A_0(t)\)、成本 \(c(t,a)=\sqrt{t^2-a^2}\) 的最小非负支付值；
- 下节一个固定二维闭完整算子的实际总长度，从任意半径 t 的初点都取到。

因此最优值不是仅由逐行构形猜出的；同一图实际达到全部尺度。若限制到不含该见证的结构类，仍只有上界，不能自动继承准确性。特别，\(\varphi<A_0\) 会改变原认证问题，不能悄悄删去坏行后沿用本结论。

## ZT2 · 同一完整旋转的纤维与全尺度达到

复用 [C420 的完整旋转](../../canonical/dd2_function_hypotheses.md#fh-zero-defect-sharp)。对 \(x\ne0,t=\|x\|\)，取
\[
\cos\theta(t)=A_0(t)/t,\quad
\sin\theta(t)=b_0(t)/t,\qquad
Jx=(A_0(t)/t)R_{-\theta(t)}x,\quad J0=0,
\]
并定义完整
\[
F(y)=\lambda^{-1}\{x-y:Jx=y\}.
\tag{ZT3}
\]
J 全域连续单值，F 闭图，完整近端恰为 J，精确零集为0。实际步 \(s=b_0(t)\)、输出距 \(a=A_0(t)\)、锚积0。

即使 η 有平台，也不能把 s 一概当作完整真残差：正输出 y 的全部前像恰由
\(q\in\eta^{-1}(a)\) 给出 \(x=y+qR_{\pi/2}y/a\)。该非空闭水平集有最小 \(q_*\)，所以 \(\lambda r_F(y)=q_*\)、\(\psi(r_F(y))=a\)。零输出的真残差为0；未取到的输出允许 F 空值，不影响近端覆盖。平方差为 \(b_0(t)^2\)，距离趋零，故真实总长正是 ZT2。

严格递增且满射的原 ψ 使 J 也是全域同胚、F 全域连续单值。于是这一更窄结构类只要包含该旋转，仍有同一准确尾值；一般平台模不冒称这样的结构。

## ZT3 · 为何最坏一步后继确实给最坏总长度

这里比较全部尾长，不声称贪心轨道对每个有限步数的前缀成本也最大：例如一步直接到零的标量成本 t 可以大于 \(b_0(t)\)。令贪心路径的平方降幅为
\[
G_k=r_k^2-r_{k+1}^2=b_0(r_k)^2 .
\]
因为 b₀ 非减，\(G_k\) 非增，且 \(\sum G_k=t^2\)。
任意真实轨道，或者上述尺度行的一条无限路径，记距离为 \(u_k\)，有
\(u_k\le r_k\)、\(u_k\to0\)。令
\[
\Delta_k=u_k^2-u_{k+1}^2\ge s_k^2,\qquad
\sum_k\Delta_k=t^2,\qquad
\sum_{k<n}\Delta_k\ge\sum_{k<n}G_k .
\tag{ZT4}
\]
这里不要求 \(\Delta_k\) 排序。对任意 \(z>0\)，G 的非增性给
\[
\sum_k(G_k-z)_+
 =\sup_{n\ge0}\left(\sum_{k<n}G_k-nz\right)
 \le\sum_k(\Delta_k-z)_+ .
\]
两列总额均为有限的 \(t^2\)，可安全相减，得
\(\sum_k\min\{G_k,z\}\ge\sum_k\min\{\Delta_k,z\}\)。
用直接可积的恒等式
\[
\sqrt q=\frac14\int_0^\infty\min\{q,z\}z^{-3/2}\,dz
\]
和非负积分换序，得到
\[
\sum_k s_k\le\sum_k\sqrt{\Delta_k}
 \le\sum_k\sqrt{G_k}=\mathcal L_*(t).
\tag{ZT5}
\]
允许右端无穷。有限尺度前缀可补一个到零的数值步，再以零延拓；补步只增加成本，故同一上界覆盖所有有限前缀。这里的补步用于上界证明，不冒称某个固定原图必须含该步。

反向由 ZT3 的同一个真实图达到，证明 ZT2 全部等式。有限时 \(\mathcal L_*\) 是尺度池上最小非负支付函数，因而对每条真实边
\(s\le\mathcal L_*(t)-\mathcal L_*(a)\)。这也给一般开 U 的局部版本：保原 E0、距离窗覆盖和
\(\mathcal L_*(t_0)<d(x^0,U^c)\)，按 TV2 的有限前缀归纳可得全选择留域、有限长和 S 中点极限。

## ZT4 · 四倍证书与可认证截断

令 \(I_{b_0}(t)=\int_0^t u/b_0(u)\,du\)。C420 的逐壳计算为
\[
\frac{b_0(t)}2\le\int_{A_0(t)}^t\frac{u}{b_0(u)}\,du\le b_0(t).
\]
故
\[
\frac12 I_\chi(t)\le I_{b_0}(t)\le
\mathcal L_*(t)\le 2I_{b_0}(t)\le2I_\chi(t).
\tag{ZT6}
\]
其中逆序比较来自 \(Q_0\le\operatorname{id}+\eta\le\sqrt2Q_0\)。
于是 \(\mathcal L_*(R)<\infty\) 当且仅当 \(I_\chi(R)<\infty\)；在可积窗内，原证书 \(2I_\chi\) 至多为最佳真实尾的4倍，不声称4不可改善。若 \(I_\chi(R)<\infty\)，\(\mathcal L_*\) 非减且在零消失；否则每个正初距的同一旋转都无限长。

具体地，对 \(r_N=A_0^{\circ N}(t)\)，
\[
\sum_{k<N}b_0(r_k)\le\mathcal L_*(t)
 \le\sum_{k<N}b_0(r_k)+2I_\chi(r_N).
\tag{ZT7}
\]
在可积窗内，末项趋0。这是准确系列的误差证书；b₀、A₀ 和积分尾的实际求值仍需认证域、精度及计算合同，不能用有限浮点和代替无限尾。

## ZT5 · 线性校准的准确常数

若原 \(\psi(\rho)=\ell\rho\)，\(L=\ell/\lambda>0\)，则
\[
q=\frac{L}{\sqrt{1+L^2}},\quad A_0(t)=qt,\quad
b_0(t)=\frac{t}{\sqrt{1+L^2}},\quad
\mathcal L_*(t)=\bigl(\sqrt{1+L^2}+L\bigr)t .
\tag{ZT8}
\]
等价地，每条边有
\(s/(t-a)\le\sqrt{(1+q)/(1-q)}\)，全尺度旋转取等。
这是零缺陷完整原数据类的最佳总长，不把它移给一般有符号下界，也不把该尾长等同于点到极限的距离。

<a id="dd2-sublinear-step-optimal-tail"></a>
## ZT6 · 严格逆分支的首项：无需正则变差

现在令 \(w:[0,\infty)\to[0,\infty)\) 连续严格递增、满射、\(w(0)=0\)，取原
\(\psi(\rho)=w^{-1}(\lambda\rho)\)，保持 ZT1 的原类与预设目标。
另设 \(w(t)/t\to0\)，且
\[
I_w(R)=\int_0^R\frac{u}{w(u)}\,du<\infty .
\]
则
\[
\mathcal L_*(t)\sim2I_w(t)\sim2I_\chi(t)\qquad(t\downarrow0).
\tag{ZT9}
\]
这给原积分证书的最佳首项常数2；不要求 w 可微、绝对连续、幂次、正则变差或点态 \(\chi(t)\sim w(t)\)。

**积分夹界。** 令
\[
c=(\operatorname{id}+w)^{-1}(t),\quad \chi(t)=w(c),\quad
\epsilon(c)=\sup_{0<v\le c}\frac{w(v)}v .
\]
ε 有限且趋0。按 \(u=v+w(v)\) 作连续递增的 Stieltjes 换元，得
\[
I_\chi(t)=I_w(c)+t+K(c),\qquad
K(c)=\int_{(0,c]}v\,d\log w(v)
 =\int_0^c\log\frac{w(c)}{w(v)}\,dv .
\tag{ZT10}
\]
可先在远离零的紧段按区间长度换元；\(d\log w=dw/w\) 由对数中值定理与连续性得到。零端用非负积分的单调极限，最后的双积分用非负换序，不假设边界分部项有极限。

因为 \(w(c)\le\epsilon c\)、\(w(v)\le\epsilon v\)，
\[
\log\frac{w(c)}{w(v)}
 \le\log\frac cv+\frac{\epsilon v}{w(v)}-1 .
\]
积分 \(\log(c/v)\) 为 c，故 \(K(c)\le\epsilon I_w(c)\)。
又 \(c\le\epsilon I_w(c)\)、\(t\le(1+\epsilon)c\)，从而
\[
I_w(t)\le I_\chi(t)
 \le(1+\epsilon(c))^2 I_w(c)
 \le(1+\epsilon(c))^2 I_w(t).
\tag{ZT11}
\]
首个不等式用 \(\chi(u)=w((\operatorname{id}+w)^{-1}u)\le w(u)\)。

**真实下界。** ZT3 在该严格逆分支就是
\(\lambda F(y)=w(\|y\|)R_{\pi/2}y/\|y\|\)，零处置零。
每个旋转步有 \(s=w(a)\)、\(t^2-a^2=s^2\)，所以
\[
\int_a^t\frac{u}{w(u)}\,du
 \le\frac{t^2-a^2}{2w(a)}=\frac s2 .
\tag{ZT12}
\]
沿全部真实尾壳相加得
\(2I_w(t)\le\mathcal L_*(t)\le2I_\chi(t)\)。
结合 ZT11 给 ZT9，极限遍历全部初始半径 \(t\downarrow0\)，不是仅一条轨道的子序列。

例如 \(w(t)=c\,t^m\)、\(1<m<2,c>0\)，有
\(\mathcal L_*(t)\sim2t^{2-m}/[c(2-m)]\)。
C451 的 \(w(t)=t^2[\log(1/t)]^\beta,\beta>1\) 配其原单调延拓，得到
\(\mathcal L_*(t)\sim2[\log(1/t)]^{1-\beta}/(\beta-1)\)。
后一式由 [LG1–LG6](nonpower_rates.md#dd2-log-half-order) 的原模确认；旋转达到最佳尾首项，剪切的实际尾首项为其一半，虽然剪切点误差与自身尾长等价。
在 \(m\ge2\) 或 \(\beta\le1\) 的发散支，不使用有限式；C420/C456 的真实旋转给无限长度。

<a id="dd2-matched-target-optimal-tail"></a>
## MT1 · C460-v1：C400 匹配预算的加法误差与首项

**状态：derived-checked。三席已独立重构并逐源冷读实际正文、身份、图边及地图，无未关闭实质异议。**

固定 \(\lambda,\ell,R>0,L=\ell/\lambda\ge1/2\)，
\(r_0=L/\sqrt{1+L^2}\)。原预设目标 \(A=\varphi:[0,R]\to[0,R]\) 连续非减，
\(A(0)=0\)，且 \(r_0t\le A(t)<t\) 于正尺度。
固定原 \(\psi(\rho)=\ell\rho\)、全域原残差域及恰好匹配的
\[
D(t)=t^2\Sigma_L(A(t)/t)
 =\frac{(1+L^{-2})A(t)^2-t^2}{2}\ge0,\quad D(0)=0,\quad
\Phi=-D .
\tag{MT1}
\]
量化 U=Vψ=H、全 R 距离窗覆盖的全部 E0 对象类，含 C400 的二维完整匹配旋转。记其最佳真实尾为 \(B_{\rm match}\)，并令
\[
H_A(t)=\sum_{j\ge0}A^{\circ j}(t),\qquad
Z_A(t)=\frac1L\sum_{j\ge1}A^{\circ j}(t).
\tag{MT2}
\]
则对每个 t，按扩展实数解释，
\[
Z_A(t)\le B_{\rm match}(t)\le Z_A(t)+Lt .
\tag{MT3}
\]
若 \(H_A(R)<\infty\)，右端亦为同一步非负距离支付势；若某 t 的级数发散，匹配旋转已从该初距给真实无限长。较小给定 D 继承上界，但不自动保留反向达到见证。

**上界。** C400 由原数据认证 \(a\le A(t)\)。先取 \(t>0\)，此时 \(A(t)>0\)；恰匹配的能量和平方根凹性给
\[
s\le\sqrt{(A(t)/L)^2+A(t)^2-a^2}
 \le A(t)/L+L[A(t)-a]\le A(t)/L+L(t-a).
\tag{MT4}
\]
零输入另由 \(D(0)=0\) 驻定。沿实际路径有 \(t_j\le A^{\circ j}(t_0)\)，求和即得 MT3 的上界。
有限时 \(Z_A\) 非减且
\(Z_A(t)=A(t)/L+Z_A(A(t))\)，故 MT4 也给
\(s\le[Z_A(t)+Lt]-[Z_A(a)+La]\)。
若 \(H_A(R)<\infty\)，各 \(A^{\circ j}\) 连续且在零为0，原 R 的可和级数支配每项，所以 \(Z_A(t)\to0\)；这给支付势的零端消失。
在一般开 U 中，原覆盖加严格预算 \(Z_A(t_0)+Lt_0<d(x^0,U^c)\)
可照 TV2 归纳留域；不先假设路径已留域。

**下界。** [C400 的完整匹配旋转](core.md#dd2-trajectory)在同一图满足
\(t_{j+1}=A(t_j)\)、\(s_j=t_{j+1}/L\)，所以实际总长恰为 Z_A。
即使 A 有平台，某个输出的全部前像位移均为 \(a/L\)，完整真残差仍取等。
原图闭、完整近端全域连续单值，原 F 可以多值；零输入驻定，精确零集0和原工作窗均已核。这里要求原 D 恰好为 MT1。

若另有 \(A(t)/t\to1\)，且 \(H_A(R)<\infty\)，每个固定 j 都有
\(A^{\circ j}(t)/t\to1\)，从有限部分和任意长可知 \(Z_A(t)/t\to\infty\)。
因此
\[
B_{\rm match}(t)\sim Z_A(t)\qquad(t\downarrow0).
\tag{MT5}
\]
C400 的原较粗步帽尾不是这里的最佳首项。对已认证的
\(L=1,A(t)=\exp[-\sqrt{\log^2(1/t)+1}]\)，
[NP1–NP3](nonpower_rates.md#dd2-stretched-exponential-target)给
\(Z_A(t)\sim2t\log(1/t)\)，故这也是匹配原数据完整类的最佳尾首项。
对 \(A(t)=t/(1+t)\) 的允许小窗，Z_A 发散，不能把它写成有限误差预算。

原 ψ 不连续或非单调的零缺陷上确界见 [C461](raw_tail_envelope.md#dd2-raw-gauge-optimal-tail)：它保原域，由完整有限图逼近，不把 C458 的同一旋转达到性直接外推。以上准确值、四倍比较和首项分别有各自的原数据合同。它们不认定公开新颖性，不把尾长上界当作每个固定算子的实际长度，也不把同一图的长度与点误差常数自动等同。
