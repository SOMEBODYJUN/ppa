# 法向增长与平坦核：完整驻点 GPPA 的结构性验证

本页 C272-v1 从目标函数的原始增长条件推出完整近端覆盖、所有输出的界、同一物理最近锚、真残差 EB 和 C249 的共同证书。无需先解近端映射。一般目标可以非凸，算法保留全部驻点根；它不等于仅取 Bregman 子问题的全局极小点。外部首创性未认证，经典方法的重叠见末节。

<a id="ngf-object"></a>
## 对象与可检查的原始条件

物理空间为 $X=\mathbb R^n\times\mathbb R^d$，$n,d\ge1$，使用 Euclidean 乘积范数。固定 $m>1$、$\lambda>0$、$\mu>0$、$B\ge0$。设 $f\in C^1(X)$，对**整个空间**满足

\[
f(0,z)=0,\qquad
\langle u,\nabla_u f(u,z)\rangle\ge\mu\|u\|^2,
\qquad \|\nabla_z f(u,z)\|\le B\|u\|^2.
\tag{NG1}
\]

原始模型的一个充分入口是状态依赖精度的残差拟合：
$f(u,z)=\frac12\langle A(z)u,u\rangle$，其中 $A(z)$ 对称、$C^1$，
$A(z)\succeq\mu I$，且 $\sup_{\|w\|=1}\|DA(z)[w]\|\le2B$ 全域成立。
$u$ 是已中心化的观测残差，$z$ 是未被零残差识别的参数，$A(z)$ 是其加权矩阵。这是可解释的优化问题类，不宣称已有特定设备采用下面的核。

径向积分 NG1 得 $f(u,z)\ge\mu\|u\|^2/2$；因此 $\nabla_u f(0,z)=0$，$\nabla_z f(0,z)=0$。固定

\[
F=\{\nabla f\},\quad S=\operatorname{zer}F=\operatorname{argmin}f
=\{0\}\times\mathbb R^d,\quad
h(u,z)=\frac{\|u\|^{m+1}}{m+1}+\frac{\|z\|^2}{2},\quad
v=(\mathcal B_m(u),z),\quad \mathcal B_m(u)=\|u\|^{m-1}u.
\tag{NG2}
\]

这里 $S$ 是完整非孤立零集，$d((u,z),S)=\|u\|$。$v$ 全域单射，但其法向逆在零点只有 $1/m$ 阶；核在每个零点的法向 Hessian 为零。

输入域为整个 $X$，算法为完整关系 $J=(v+\lambda F)^{-1}v$。对输入 $x=(a,b)$，**全部纤维**是

\[
J(a,b)=\{(u,z):\mathcal B_m(u)+\lambda\nabla_u f(u,z)=\mathcal B_m(a),\quad
z+\lambda\nabla_z f(u,z)=b\}.
\tag{NG3}
\]

不假定这个集合单值。真残差始终为 $r_F(u,z)=\|\nabla f(u,z)\|$，不是核步长。

<a id="ngf-coverage"></a>
## 全输入覆盖与完整纤维定位

对每个输入，$h(y)+\lambda f(y)-\langle v(x),y\rangle$ 是连续 coercive 函数：NG1 的积分下界及 $h$ 的超线性增长控制线性项。其全局极小点供应至少一个 NG3 根；这只证明存在，随后估计适用于**任意驻点根**。

令 $t=\|a\|$、$r=\|u\|$。第一式点乘 $u$ 给

\[
r^{m+1}+\lambda\mu r^2\le t^m r,
\qquad r^m+\lambda\mu r\le t^m\quad(r>0).
\tag{NG4}
\]

令 $\phi(t)$ 为 $s^m+\lambda\mu s=t^m$ 的唯一非负根。每个完整输出满足

\[
r\le\phi(t)<t\ (t>0),\quad r\le Ct^m,\quad
\|z-b\|\le\lambda B r^2\le Dt^{2m},\quad
C=(\lambda\mu)^{-1},\quad D=B/(\lambda\mu^2).
\tag{NG5}
\]

这些是全域根界，推导没有预先假定输出靠近 $S$。NG3 连续且所有根有界，故每个纤维非空紧。输入 $t=0$ 时 NG4 强制 $u=0$，第二式强制 $z=b$，所以完整零输入纤维恰为输入本身。$\operatorname{Fix}J=S$ 也由 NG3 与 $v(x)-v(x)=0$ 直接成立。

<a id="ngf-certificate"></a>
## 同一组 C249 证书

对输入的唯一物理最近零点取 $p_x=(0,b)$。输入核距离恰为 $\delta=t^m$。NG5 对所有输出给

\[
\|v(y)-v(p_x)\|\le (C\delta)^m+\lambda B(C\delta)^2,
\]
\[
\|2v(y)-v(x)-v(p_x)\|
\le\omega(\delta),\qquad
\omega(s)=s+2(Cs)^m+2\lambda B(Cs)^2.
\tag{NG6}
\]

这是同一最近锚的反射界，没有任选一个更方便的零点，也没有断言全对 RL。真实 EB 是全域的：

\[
r_F(u,z)\ge\|\nabla_u f(u,z)\|\ge\mu\|u\|,
\qquad \psi(s)=s/\mu.
\tag{NG7}
\]

固定任意 $0<\kappa<1$，取 $R>0$ 满足

\[
CR^{m-1}+C^{m+1}R^{m^2-1}+CDR^{2m-1}\le\kappa.
\tag{NG8}
\]

一个仅用原始常数的正半径是以下三个上界的最小值：
$(\kappa/(3C))^{1/(m-1)}$、
$(\kappa/(3C^{m+1}))^{1/(m^2-1)}$、
$(\kappa/(3CD))^{1/(2m-1)}$；$D=0$ 时略去第三项。
全套数据为

\[
U=X,\quad \mathcal J=J,\quad a_{\rm scale}(t)=t^m,\quad
\omega\text{ 如 NG6},\quad \psi(s)=s/\mu,\quad
\mathfrak h(t,s)=t+Ct^m+Dt^{2m},
\]
\[
K(t)=t^m+C^m t^{m^2}+Dt^{2m},\qquad
\bar t\ge K(R)/\lambda,
\]
\[
H(t)=t+Ct^m+Dt^{2m},\qquad
\Theta(t)=\frac{t}{1-\kappa}+\frac{Ct^m}{1-\kappa^m}
+\frac{Dt^{2m}}{1-\kappa^{2m}}.
\tag{NG9}
\]

所有模函数全域有限、非减并在零处连续。G1 是 NG3–5 的完整覆盖；G2 是 NG6 的同锚两界；G3 是 NG5 与物理三角不等式 $\|y-x\|\le t+r+\|z-b\|$。$\mathfrak h$ 可不依赖第二参数，这是 C249 允许的转移提升，未使用 Lipschitz 逆核。G4 是 NG7 的真实 EB 与指定 $\bar t$。NG8 恰给全部 $0<t\le R$ 的 G5：$\psi(K(t)/\lambda)\le\kappa t$。$\Theta$ 有限；$U^c$ 为空，严格留域预算自动成立。

故所有 $d(x_0,S)\le R$ 的完整选择轨道留在同管，有限物理长度趋于 $S$，且尾长由同一个 $\Theta(\kappa^k d_0)$ 控制。验证过程没有计算完整近端逆。

<a id="ngf-rate"></a>
## 更强的全域结论与平坦阶的含义

NG4 另有短直接证明，不能隐去：$\phi$ 连续递增且 $\phi(t)<t$，所以迭代标量上界 $\phi^k(t_0)$ 递减到零。所有完整轨道在有限前缀后进入 NG8 的同一个半径；覆盖保证前缀继续，有限前缀加 NG9 的可和尾保证全域有限长度。因此每个有限初值、每个完整分支选择都收敛到某个 $(0,z_\infty)$，一般没有无需进一步求解的 $z_\infty$ 闭式。

设 $r_k=\|u_k\|$。在小管内，$r_{k+1}\le Cr_k^m$，并且

\[
\|z_\infty-z_k\|\le
\frac{\lambda B r_{k+1}^2}{1-\kappa^2}
\le\frac{D r_k^{2m}}{1-\kappa^2}.
\tag{NG10}
\]

若 $r_0>0$，NG3 和 $\nabla_u f(0,z)=0$ 排除法向有限终止，因而 $\|x_k-x_\infty\|/r_k\to1$。若另外 $f$ 在 $(0,z_\infty)$ 附近为 $C^2$，则
$A_\infty=\nabla^2_{uu}f(0,z_\infty)\succeq\mu I$，实际输出处 Taylor 展开给

\[
u_{k+1}=\lambda^{-1}A_\infty^{-1}\mathcal B_m(u_k)+o(r_k^m).
\tag{NG11}
\]

这里用 NG5 先知 $r_{k+1}=O(r_k^m)$。因 $\nabla_u f(0,z)=0$，沿固定 $z_{k+1}$ 的法向线段积分 Hessian 得 $\nabla_u f(u_{k+1},z_{k+1})=A_\infty u_{k+1}+o(r_{k+1})$；$\mathcal B_m(u_{k+1})=o(r_{k+1})$，所以 NG11 的余项为 $o(r_k^m)$。于是法向及完整物理点误差均有锐的双边 $m$ 阶：比值 $r_{k+1}/r_k^m$ 的 liminf、limsup 分别被 $1/(\lambda\lambda_{\max}(A_\infty))$、$1/(\lambda\lambda_{\min}(A_\infty))$ 夹住。标量法向的比值极限恰为 $1/(\lambda A_\infty)$；一般向量情形不擅自宣称单个标量极限存在。仅 NG1 的 $C^1$ 类保证 $m$ 阶上界，不保证每个成员都有匹配下界。

<a id="ngf-all-roots"></a>
## 任意近零的非极小根不能删掉

取标量两块、$m=3,\lambda=1$，

\[
f(u,z)=\tfrac12 A(z)u^2,\qquad
A(z)=2-\frac{|z|^{3/2}}{1+|z|^{3/2}}.
\tag{NG12}
\]

这个 $C^1$ 非凸函数满足 $1<A\le2$、$|A'|\le3/2$，所以同组 $\mu=1,B=3/4$ 全域有效。对任意输入 $(a,0)$、$a>0$，完整纤维含中心 $(r,0)$，其中 $r^3+2r=a^3$。它**不是局部极小点**：固定 $u=r$ 的子问题目标差为
$z^2/2-r^2|z|^{3/2}/[2(1+|z|^{3/2})]<0$，当非零 $z$ 充分小时成立。

还至少有两个不同非零切向根。令 $t=\sqrt{|z|}$，$u(t)>0$ 是
$u^3+[(2+t^3)/(1+t^3)]u=a^3$ 的唯一根。连续函数
$t(1+t^3)^2-3u(t)^2/4$ 在零处为负、无穷远为正，因此至少有一个正根，每个正根产生 $(u(t),\pm t^2)$。不声称完整纤维恰有三点。这些根在 $a\downarrow0$ 时全部受 NG5 定位，任何分支仍受同一个证书及三阶收敛界控制。

例如 $R=1/4,\kappa=1/4,\bar t=1,U=X$。NG8 左端恰为 $4145/65536<1/4$。完整 $\Theta$ 为 NG9 的同组 $C=1,D=3/4$ 公式。这个机制例展示全驻点关系相对仅取全局 argmin 的实质范围；它不是工业性能案例。

<a id="ngf-boundaries"></a>
## 必须保留的边界和比较

1. **全域条件承重。** 仅在零管内有 NG1 不够。$f(u,z)=u^2/2-u^4/2$、$m=3,\lambda=1$ 在 $|u|\le1/2$ 有法向系数 $\mu=1/2$、切向导数零；完整零输入却有 $(0,b),(1,b),(-1,b)$ 三根，因为 $u^3+f_u=u-u^3=0$。未排除的远根破坏零纤维吸收，不能按本定理接收。
2. **反射非扩张不可默认。** 对 $f(u,z)=(2+\sin z)u^2/2$，选实际输出 $(r,0)$ 和反算输入 $a^m=r^m+2\lambda r$、$b=\lambda r^2/2$。同一最近锚下 $\langle v(y)-v(p),F(y)\rangle=2r^{m+1}-\lambda r^4/4$。$m>3$（或 $m=3,\lambda>8$）时它在任意小窗为负，故不能换用 $\omega=Id$；NG6 的三角界仍成立。
3. **经典比较。** $C^2$ 子类的法向正曲率、EB、Morse–Bott/PL/KL 关系已有经典结果。下节 NG13 更强地对全部 $C^1$ 完整驻点根给同一个 $E=\|u\|^2$ 的 ABS 合同，无需原目标 KL；NG14–16 对整个 SPD 二次子类精确改写为普通 PPA，已有增长理论恢复物理 $m$ 阶。NG4–5 本身也有更短的直接收敛证明。保留的结构内容是原始条件到完整驻点证书的转接、全根控制与精确定量化；它们的字面优先权仍需审查，不能整体称新收敛原理。指定需要局部强凸核或正定核 Hessian 的定理不能直接套，不等于排除整个 Bregman/KL 理论。
4. **创新性限域。** 内部数学闭合，公开先行性仍待逐定理核查。局部原始条件加全纤维排远门、更一般平移/弯曲零流形、时变核和误差版本尚未证明。本定理不推出隐藏的额外零点；NG1 已确定完整零集。

<a id="ngf-classical-full"></a>
## 新颖性复核的完整经典桥：不改变 C272 身份

这是同一对象的补充证明和比较证据，不增加一个新收敛原理。

**所有 $C^1$ 目标和全部驻点根的自然 KL 桥。** 取 NG8 小管及同一个 $\kappa$，令 $E(u,z)=\|u\|^2$。对任何完整转移，$s=\|u_+\|\le\kappa t$、$\|z_+-z\|\le\lambda B\kappa^2t^2$，所以

\[
\|y-x\|\le L_Et,\quad L_E=1+\kappa+\lambda B\kappa^2R,
\qquad E(x)-E(y)\ge\frac{1-\kappa^2}{L_E^2}\|y-x\|^2,
\]
\[
\|\nabla E(y)\|=2s\le\frac{2\kappa}{1-\kappa}\|y-x\|.
\tag{NG13}
\]

第二式用物理法向步 $\|a-u\|\ge t-s$，不是选中 $F$ 图值。$E$ 是全域光滑 proper 函数，$\|\nabla E\|=2\sqrt E$ 给 KL 指数 $1/2$。法向几何界及切向二次步界先给全部前缀有界，有限维紧性供应聚点；$E$ 连续供应 H3，未先假设整条轨道收敛。因此 ABS 的 H1/H2/H3 和 Theorem 2.9 适用于同一完整轨道的尾部，不需要原目标 $f$ 具有 KL 性质。这比仅在 $C^2$ 子类调用原目标 KL 的比较更强。该桥依赖已经证明的 NG4–5 输出界，不能反过来声称 ABS 的原文自动供应本模型的全部根定位。

NG12 甚至保留原目标能量的合同：$1<A(z)\le2$ 给 $t^2/2\le f(x)\le t^2$，而所有根满足 $s\le t^3$，故 $f(y)\le t^6$。取 $R^4<1/2$ 时，$f(x)-f(y)\ge(1/2-R^4)t^2\ge a_f\|y-x\|^2$，其中 $a_f=(1/2-R^4)/L_E^2>0$。核 $(u^3,z)$ 在该法向条带上 Lipschitz，完整方程给输出梯度的 H2。真实梯度范数 $\|\nabla f\|\ge|u|\ge\sqrt f$ 使 $2\sqrt r$ 成为 KL 去奇异化函数；同样的有界性和连续性给 H3。这保留全部非极小根，不把驻点关系换成 argmin。

**常系数 SPD 子类的精确普通 PPA 改写。** 设 $f(u,z)=\langle Au,u\rangle/2$，$A\succ0$ 常矩阵。切向不动。令

\[
w=\mathcal B_m(u),\quad\eta=A^{-1/2}w,\quad
\beta=1+1/m,\quad
P(\eta)=\frac{m}{m+1}\|A^{1/2}\eta\|^{\beta}.
\tag{NG14}
\]

$P$ 全域有限、$C^1$、严格凸、coercive，唯一极小点为零，且
$\nabla P=A^{1/2}\mathcal B_{1/m}(A^{1/2}\eta)$。原完整法向方程在所有输入、所有 $\lambda>0$ 下与

\[
\eta_{k+1}+\lambda\nabla P(\eta_{k+1})=\eta_k
\tag{NG15}
\]

双向等价；不是另挑收敛分支。$P\ge\chi\|\eta\|^{\beta}$，
$\chi=\frac{m}{m+1}\lambda_{\min}(A)^{\beta/2}>0$。因此普通 PPA 的高阶增长理论可直接导入：Oikonomidis–Bodard–Laude–Patrinos 的固定 [2312.12205v3](https://arxiv.org/html/2312.12205v3) Theorem 3.6，取其正则化参数 $p=1$（普通平方 prox）、增长幂 $\nu=\beta$、exact/无加速、紧零集 $\{0\}$，给对偶变量 $m$ 阶上界。其完整凸目标、覆盖、coercivity、局部增长和 $p>\nu-1$ 全通过。

物理桥须另外写出：

\[
\lambda_{\max}(A)^{-1/2}\|u\|^m
\le\|\eta\|\le\lambda_{\min}(A)^{-1/2}\|u\|^m.
\tag{NG16}
\]

若 $\|\eta_+\|\le K_0\|\eta\|^m$，NG16 给
$\|u_+\|\le\lambda_{\max}(A)^{1/(2m)}K_0^{1/m}\lambda_{\min}(A)^{-1/2}\|u\|^m$。
所以这个完整 SPD 子类的物理 $m$ 阶不是首次由平坦核创造的收敛机制。源定理的上界不自行给 NG11 的精确系数；一般状态依赖非凸 $C^1$ 目标也没有由 NG14–15 获得凸 PPA 改写。全驻点原始验证与这些更细定量项的公开优先仍需单独判别。

一手比较的版本、条件及定位见 [文献接口](../LITERATURE.md#lit-structural-verification)及[发展复核](../novelty/2026_10_13/c272_development_review.md)。[复算](../code/structural_verification/README.md)和[新增经典桥检查](../code/novelty_development/README.md)只核有限参数与反算；全称结论由正文证明承担。[接收记录](../audit/STRUCTURAL_VERIFICATION_REVIEW_2026_10_13.md)记录前轮实际复核范围，本轮新增桥的接收见发展报告。
