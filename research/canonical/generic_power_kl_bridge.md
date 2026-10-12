# 已认证完整幂几何的共同 KL–ABS 桥

本页给 C266-v1/v2 的独立证明。它是取得完整几何之后的比较桥，不是自然应用候选，不声称旧论文已经供应这些几何，也不认证公开优先。所用 ABS 合同为[已核一手接口](../LITERATURE.md#lit-smooth-kl-obstruction)中的 proper-lsc、limiting 次梯度 H1/H2/H3 与 Theorem 2.9；可定义性不是该抽象定理的必要前件。

<a id="gpk-contract"></a>
## C266-v2 · 对象与全部量词

固定有限维 Euclidean 空间 $X=\mathbb R^N$、非空闭集 $S$，记 $d(x)=\operatorname{dist}(x,S)$。固定

\[
0<\gamma\le1,\quad q>0,\quad q\gamma\ge1,\quad
b=1/q,\quad a=\min\{2\gamma,1+b\},\quad\theta=b/a.
\tag{PK1}
\]

于是 $q\ge1$、$0<b\le1$、$2b\le a\le2$、$a\le2\gamma$、$a\le1+b$，以及 $0<\theta\le1/2$。取 $0<R<1$，使

\[
t^b\le a t^{a-1}\quad(0<t\le R).
\tag{PK2}
\]

这样的半径存在：$1+b-a>0$ 时要求 $R^{1+b-a}\le a$；等于零时 $a=1+b>1$，不等式自动成立。

固定认证状态窗 $D\subset\{d\le R\}$ 和实际完整关系 $J:D\rightrightarrows X$。要求每个 $w\in D$ 的纤维非空、全部 $y\in J(w)$ 均在 $D$，且同一组 $0\le\kappa<1$、$C,c>0$、$\lambda_*>0$ 对**全部输入与全部输出**满足

\[
d(y)\le\kappa d(w),\qquad
\|w-y\|^2\le C d(w)^{2\gamma},\qquad
d(y)\le c r_F(y)^q,\qquad
r_F(y)\le\|w-y\|/\lambda_*.
\tag{PK3}
\]

这里 $F:X\rightrightarrows X$，$r_F(y)=\inf_{z\in F(y)}\|z\|$ 评价完整原算子。普通隐式步 $w-y\in\lambda F(y)$、$\lambda\ge\lambda_*$ 供应最后一式，不能把 inf 等同步长。一般 GPPA 仅有 $r_F\le\|v(w)-v(y)\|/\lambda$，**不自动**供应 PK3；必须另有到物理步的正确转接。也可直接以 $d(y)\le D_*\|w-y\|^q$、固定有限 $D_*>0$ 代替 PK3 后两式，令相应 $\beta=D_*^b$；零常数界可以放宽为任意正 $D_*$。

前向留窗是前件。如果来自局部 $U_R$，必须先认证全部输出留 $U$，不能借无限轨道反推第一步留域。$d(w)=0$ 时步长界强制 $y=w$。

**结论。** 存在一个固定、全域有限连续 proper-lsc 函数 $E$，$E^{-1}(0)=S$，同时对全部合法转移满足

\[
E(w)-E(y)\ge\alpha\|w-y\|^2,
\qquad \exists\xi_y\in\partial_LE(y):\ \|\xi_y\|\le\beta\|w-y\|,
\tag{PK4}
\]

其中可取 $\alpha=(1-\varepsilon-\kappa^a)/C>0$、$\beta=c^b/\lambda_*$，$0<\varepsilon<1-\kappa^a$。$E$ 在全部 $S$ 点有统一 KL 指数 $\theta$，每条完整轨道满足 H3。因此同一个 ABS 抽象定理可用于原算法的全部政策，不更换根或图。

<a id="gpk-construction"></a>
## 固定能量与加权区间估计

枚举 $(0,R)$ 的有理数 $r_j$，$j\ge1$，置

\[
\sigma_j=\varepsilon2^{-j-5},\quad
I_j=(r_j(1-\sigma_j),r_j(1+\sigma_j))\cap(0,R),\quad
\Omega=\bigcup_j I_j.
\tag{PK5}
\]

$\Omega$ 稠密开。$\sigma_j<1/16$，对 $r\in I_j$、$0<a\le2$ 有 $a r^{a-1}\le3r_j^{a-1}$：$a\ge1$ 用上端点，$a<1$ 用下端点。若 $I_j\cap(0,t)\ne\varnothing$，则 $r_j<16t/15$，且 $(16/15)^a<2$。故

\[
\int_{\Omega\cap(0,t)}a r^{a-1}\,dr
\le\sum_{j:\,I_j\cap(0,t)\ne\varnothing}6\sigma_jr_j^a
\le\sum_{j\ge1}12\sigma_jt^a
=\frac38\varepsilon t^a<\varepsilon t^a.
\tag{PK6}
\]

区间可重叠；可数次可加性足以给上界。加权估计处理 $a<1$ 时 baseline 在零处发散的导数。

对 $t>0$ 定义 $\ell(t)=t^b$（$t\in\Omega$），其余处定义 $\ell(t)=a t^{a-1}$。令

\[
\varphi(t)=\int_0^t\ell(r)\,dr,\qquad E(x)=\varphi(d(x)).
\tag{PK7}
\]

$\ell(0)$ 任意赋值。$\Omega$ 仅在 $(0,R)$；其外继续 baseline。$a>0$ 保证零处可积，故 $\varphi$ 全域有限、连续、严格增，$E$ 全域连续非负且零集恰 $S$。由 PK2/PK6，

\[
(1-\varepsilon)t^a\le\varphi(t)\le t^a\quad(0\le t\le R).
\tag{PK8}
\]

正距离处 $E$ 局部 Lipschitz。$a\ge1$ 时零处也局部 Lipschitz；$a<1$ 时一般不是，这仍属于 ABS 的 proper-lsc 范围。

<a id="gpk-subgradient"></a>
## 任意闭零集，包括多最近点

固定 $x\notin S$、$d=d(x)$，任取 $p\in P_S(x)$，$n=(x-p)/d$。有限维闭性保证最近点存在。令 $x_t=p+tn$，$0\le t\le d$。距离的 Lipschitz 下界与 $p$ 比较上界给 $d(x_t)=t$。

当 $0<t<d$，$p$ 还是唯一最近点：若 $q$ 也是，则

\[
d\le\|x-q\|\le\|x-x_t\|+\|x_t-q\|=(d-t)+t=d;
\]

Euclidean 三角等号强制 $q=p$。唯一投影使 $d$ 在 $x_t$ 可微且梯度为 $n$。自足理由是：附近最近点 $p_h$ 有界，任何聚点均为 $x_t$ 的最近点，故 $p_h\to p$；以 $p$ 作上界、$p_h$ 作下界展开平方距离，得到
$d(x_t+h)^2=t^2+2\langle tn,h\rangle+o(\|h\|)$。

记 $\widehat\partial$、$\partial_L$ 为 Fréchet 与 limiting 次微分。若 $0<d(x)\le R$、$\xi\in\widehat\partial E(x)$，沿内向 $x-hn$ 的测试和 $\ell(t)\ge t^b$ 给

\[
\langle\xi,n\rangle\ge d(x)^b,\qquad\|\xi\|\ge d(x)^b.
\tag{PK9}
\]

limiting 次梯度按定义取 Fréchet 值的极限，范数下界逐点传递，不需要投影单值。跨 $d=R$ 的序列也合法：外侧 baseline 连续且 $aR^{a-1}\ge R^b$，其局部下界趋于至少 $R^b$。

反向取 $t_j\in\Omega$、$t_j\uparrow d$、$t_j<d$。在 $x_{t_j}$，距离可微且 $\varphi$ 在相应区间为 $C^1$，所以真实梯度为 $t_j^bn$。梯度、点和能量共同收敛，得到 $d^bn\in\partial_LE(x)$。于是

\[
\boxed{\operatorname{dist}(0,\partial_LE(x))=d(x)^b}
\quad(0<d(x)\le R).
\tag{PK10}
\]

$d=0$ 时 $E$ 取全局最小值，$0\in\widehat\partial E$。这里没有假定正 reach、光滑零集、medial axis 外的输入或可测投影。

<a id="gpk-abs"></a>
## 全部 ABS 前件和后验意义

PK3/PK8 给

\[
E(w)-E(y)\ge(1-\varepsilon-\kappa^a)d(w)^a
\ge\frac{1-\varepsilon-\kappa^a}{C}\|w-y\|^2,
\tag{PK11}
\]

其中 $a\le2\gamma$、$d\le R<1$。PK10 给一个范数恰 $d(y)^b$ 的 limiting 值，再由真实 EB 和 inf 上界得 $\|\xi_y\|\le c^b\|w-y\|/\lambda_*$。H2 是存在所选值，不是全部次梯度均小。

在 $0<E(x)<\varphi(R)$ 的整个 level 窗，$d<R$、$E\le d^a$，故 $\operatorname{dist}(0,\partial_LE)\ge E^\theta$。同一个凹去奇异函数 $\chi(t)=t^{1-\theta}/(1-\theta)$ 满足 KL 不等式，统一于全部 $S$ 点。非零点附近内向测试还给严格正的次梯度范数下界，线性去奇异函数使 $E$ 在这些点也有 KL 性质。

每个有限前缀先由非空纤维和前向不变认证，继而

\[
d(w_k)\le\kappa^kd(w_0),\qquad
\sum_{k\ge0}\|w_{k+1}-w_k\|
\le\frac{\sqrt C\,d(w_0)^\gamma}{1-\kappa^\gamma}.
\tag{PK12}
\]

有限维完备性给 Cauchy 极限，闭 $S$ 给极限属于 $S$，全域连续 $E$ 给 H3。$\kappa=0$ 时一步到 $S$ 并吸收。至此原 ABS Theorem 2.9 的 H1/H2/H3/KL 均逐条供应。

**PK12 已经证明有限长度。** 本桥说明已证几何可以编译到旧抽象定理，不能反过来说旧论文此前已经认证了某应用的全部隐式根。它阻止“整个 ABS/KL 无法分析”的总排除，不否定 RLEB 在任务认证、完整真残差和共同政策上的价值。

<a id="gpk-v1"></a>
## C266-v1 · 平方 EB 的简式

取 $\gamma=1/2,q=2$，故 $a=1,b=1/2,\theta=1/2$。PK3 化为 $d_+\le\kappa d$、$s^2\le Cd$、$d_+\le D_*s^2$。共同人工能量全域 1-Lipschitz，最小 limiting 范数恰 $\sqrt d$，H1 可取 $(1-\varepsilon-\kappa)/C$，H2 可取 $\sqrt{D_*}$，KL 去奇异函数为 $2\sqrt t$。它推广[C262特定反馈桥](artificial_kl_energy_bridge.md#akb-theorem)到任意非空闭 $S$，不要求相位管。

<a id="gpk-distance-power"></a>
## 无需人工微区间的正面子区

若额外有 $2\gamma\ge1+1/q=1+b$，直接取 $E_0=d^{1+b}$。同一个内向射线证明给最小 limiting 范数 $(1+b)d^b$；H1/H2 可取 $(1-\kappa^{1+b})/C$ 和 $(1+b)c^b/\lambda_*$，KL 指数为 $1/(q+1)$，H3 仍由 PK12。

只有当 $S$ 与 $t\mapsto t^{1+b}$ 在**同一个** o-minimal 结构中可定义时，才可在该结构断言 $E_0$ 可定义。$q$ 有理、$S$ 半代数时保持半代数；一般实 $q$ 与半代数 $S$ 可放到 $\mathbb R_{\mathrm{an},\exp}$。不得由固定结构中的 $S$ 可定义自动断言任意实幂可定义。

当前反馈的 $\gamma=1/2,q=2$ 不在此子区，因此不反[C261强链式共同能量障碍](smooth_kl_full_relation_obstruction.md#sko-nonsmooth)。

<a id="gpk-boundaries"></a>
## 边界攻击

步长下界不可省：$F(y)=\operatorname{sign}(y)\sqrt{|y|}$、$S=\{0\}$，对正 $w$ 取 $\lambda(w)=(1-\kappa)\sqrt w/\sqrt\kappa$，完整唯一输出为 $y=\kappa w$。真 EB 恰 $d=r_F^2$，但 $d(y)/\|w-y\|^2\to\infty$，本桥 H2 的转接失效；不排这个标量算法有其他能量。

严格 $\kappa<1$、物理步长幂界和前向留窗各自承重：定距绕圆允许无限旋转；距离缩小却跨两个相反相位跳跃允许不收敛。零输入吸收不能替代这些前件。无限维任意闭非凸集可能没有最近点，本证明不授该范围。

当 $S\ne X$，人工 $E$ 沿内向射线的导数在补集正测处为 baseline，而同一点有投影为 $t^b$ 的 limiting 值；因此违反全部次梯度的强链式法则。也不可定义：一维可定义连续函数局部有限分段 $C^1$，稠密 $\Omega$ 迫使分段导数等于 $t^b$，与正测补集上的不同 baseline 矛盾。$a<1$ 时这不是 C261 的零处 locLip 反例。$S=X$ 的 $E=0$ 是平凡例外。

这里给充分桥，不证明 $q\gamma<1$ 无桥、不证明 $2\gamma<1+1/q$ 时无任何自然能量、不比较全球理论大小。解析证明承担全称结论；[有限算术复算](../code/model_selection_limits/README.md)只检查参数和边界。
