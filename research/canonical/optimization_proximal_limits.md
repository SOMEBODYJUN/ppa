# 优化来源近端例的结构边界与非单射核逃出

本页给 C267/C268 的独立规范证明。优化目标、完整全局 argmin、完整 stationary resolvent 和 target 分别定义；它们不能以同名 prox 混合。结果用于筛选应用，不认证公开先行，也不宣称一个旧合同失效便排除全部经典方法。

<a id="opl-argmin"></a>
## C267-v1 · 普通全局极小近端的 all-output calmness

设 $f:\mathbb R^m\to(-\infty,+\infty]$ proper lsc，$S_{\min}=\operatorname{argmin}f\ne\varnothing$、$f_*\in\mathbb R$。固定 $\lambda>0$，定义完整算法

\[
T_\lambda(x)=\operatorname{argmin}_y\left[f(y)+\frac1{2\lambda}\|y-x\|^2\right].
\tag{OP1}
\]

因 $f\ge f_*$，子问题 coercive；任意 global minimum 为有限 comparator，所以全部输入均有非空紧纤维。非空闭 $S_{\min}$ 有最近点。对每个输入 $x$、每个 $y\in T_\lambda(x)$ 和任意 $p\in P_{S_{\min}}(x)$，比较 $p$ 给

\[
\boxed{\|y-x\|^2+2\lambda(f(y)-f_*)\le d(x,S_{\min})^2.}
\tag{OP2}
\]

因此 $\|y-x\|\le d$、$\|y-p\|\le2d$、$\|2y-x-p\|\le3d$，零输入完整纤维为 singleton。对每个固定 $p_0\in S_{\min}$，

\[
\sup_{y\in T_\lambda(x)}\|y-p_0\|\le2\|x-p_0\|.
\tag{OP3}
\]

这是相对固定解输入的完整点态 calmness，包括非孤立 $S_{\min}$；不宣称所有输入对的 Lipschitz/Aubin 性或单值性。普通 global-min prox 不能保留原 Hamilton 在真实解点的非 calm 作用。

若 $F=\partial_L f$，Fermat 给 $(x-y)/\lambda\in F(y)$，真实 $r_F(y)\le\|x-y\|/\lambda\le d/\lambda$。同窗真实 EB $d(y,S_{\min})\le c r_F(y)^q$ 因而给 $d_+\le c(d/\lambda)^q$。$q>1$ 缩窗自动有严格距离收缩，物理步长 $\le d$ 直接给有限长度。仍须核完整输出窗和留域，不能把 $S_{\min}$ 替为完整 $\operatorname{zer}\partial f$ 后沿用 OP2。

<a id="opl-nonfirm"></a>
## calm 不等于 firm：光滑反例

令 $f(y)=y^2(y-2)^2+y^2/4$，$S_{\min}=\{0\}$，$\lambda=1/3$、输入 $x=5/4$。以 $t=y-1$ 写子问题导数为

\[
\frac{d}{dy}\left[f(y)+\frac32(y-5/4)^2\right]
=(t-1/2)(4t^2+2t+1/2).
\tag{OP4}
\]

第二因子处处正，唯一完整 global-min 输出为 $y=3/2$。然而 $\langle y,x-y\rangle=-3/8<0$，最近 global-min 零锚 firm 必要式失败。完整梯度零集另为 $\{0,3/2-\sqrt2/4,3/2+\sqrt2/4\}$。乘无作用坐标 $f(y,t)=f(y)$ 得非孤立 global-min 直线，同一反例保留。它不声称任意小根邻域都失败 firm。

<a id="opl-bregman-zero"></a>
## Bregman argmin 的完整零输入分类

设 $h$ 全域 convex $C^1$，$v=\nabla h$，$D_h(y,x)=h(y)-h(x)-\langle v(x),y-x\rangle$。定义完整 argmin $T_h(x)=\operatorname{argmin}_y[\lambda f(y)+D_h(y,x)]$；非零输入的存在性需另证。对每个 $p\in S_{\min}$，已有 comparator $p$，故

\[
\boxed{T_h(p)=S_{\min}\cap v^{-1}(v(p)).}
\tag{OP5}
\]

证明：最小值为 $\lambda f_*$，argmin 等价于 $f(y)=f_*$ 和 $D_h(y,p)=0$。convex $C^1$ 的同一支持平面同时接触 $p,y$ 当且仅当 $v(y)=v(p)$。因此完整零输入吸收恰要求 $v|_{S_{\min}}$ 单射，**不要求全空间单射**。

任意完整 GPPA 也有必要门：若 $p\in S\cap U$、$q\in S\subset\operatorname{zer}F$、$p\ne q$ 满足 $vp=vq$，则 $q\in J^v_{\lambda F}(p)$，与[父定理](physical_rleb_gppa.md#prg-object)的 G2/G3 在认证输入 $d=0$ 时强迫驻定冲突。只有 $S\subset U$ 时，才由此推出 $v|_S$ 全局单射；允许子关系可另行限制核纤维输出。

核长度并不代替物理长度。取 $f=h=x_1^2/2$、$v=(x_1,0)$，完整 argmin 为 $(x_1/(1+\lambda),s)$，$s\in\mathbb R$。核上 firm 收缩，但物理第二坐标可任意跳跃，完整物理收敛为假。

<a id="opl-metric"></a>
## 度量变化的准确边界

若 OP1 使用 $\|y-x\|_M^2$，且同一族 $mI\preceq M\preceq\overline m I$、$0<m\le\overline m<\infty$，比较最近 global minimum 仍给 $\|y-x\|\le\sqrt{\overline m/m}\,d$，统一 pointwise calmness。任意正定性本身不供应这个统一常数。

具体取 $f(y)=y_1^2/2$、$S_{\min}=\{0\}\times\mathbb R$，

\[
M_\epsilon=\begin{pmatrix}2&\epsilon\\\epsilon&\epsilon^2\end{pmatrix},\quad\epsilon>0.
\]

输入 $(a,0)$ 的唯一 metric prox 为 $(a/(1+\lambda),\lambda a/[(1+\lambda)\epsilon])$。$\epsilon=\sqrt a$ 时相对输入幅度有半阶切向漂移，每个固定 mode 仍 calm。此族失去统一正下界且更换核；它不是 C249 的固定核结论或任意时变度量收敛证书。

<a id="opl-fenchel"></a>
## C268-v1 · 非单射核的完整 Fenchel–Young 优化例

取物理状态 $(x,s)\in\mathbb R^2$，实立方根记 $\sqrt[3]x$，定义标准共轭一致性目标

\[
f(x,s)=\frac34|x|^{4/3}+\frac14s^4-xs\ge0,
\quad F=\nabla f=(\sqrt[3]x-s,s^3-x),
\quad S=\{(c^3,c):c\in\mathbb R\}.
\tag{FY1}
\]

Fenchel–Young 等号及两梯度分量给 $S=\operatorname{argmin}f=F^{-1}(0)$，闭、非孤立，无遗漏的非极小零点。定义原生凸退化核 $h(x,s)=x^2/2$、$v=(x,0)$，固定 $\lambda=2$、输入域全 $\mathbb R^2$，使用**完整**
$J^v_{\lambda F}=(v+\lambda F)^{-1}v$。

任意输入 $(a,b)$ 的第二方程强制 $x=s^3$，第一方程随即强制 $x=a$。所以

\[
\boxed{J^v_{\lambda F}(a,b)=\{(a,\sqrt[3]a)\}.}
\tag{FY2}
\]

这个式子对任意 $\lambda>0$ 都成立。它也是完整 global argmin $\operatorname{argmin}[\lambda f+(x-a)^2/2]$：每个 $x$ 唯一以 $s=\sqrt[3]x$ 使 gap 为零，再唯一以 $x=a$ 使 quadratic 为零。全部 stationary 根、全部 minima 和算法完全相同；coverage 与远端纤维已闭式穷尽。

真实残差为

\[
r_F(x,s)=\sqrt{(\sqrt[3]x-s)^2+(s^3-x)^2},\qquad
d((x,s),S)\le|\sqrt[3]x-s|\le r_F(x,s).
\tag{FY3}
\]

不是选取某图值；$F$ 单值。输出处残差恰零，但保留全域非平凡 EB $\psi(t)=t$。

<a id="opl-fenchel-certificate"></a>
### 同窗最近锚与父定理完整证书

取 $U=\mathbb R^2$、$R=\bar t=1$、$\kappa=1/2$，

\[
a(t)=t,\quad\omega(t)=t,\quad\psi(t)=t,\quad
\mathfrak h(t,q)=3t^{1/3}\quad(t,q\ge0).
\tag{FY4}
\]

对每个 $d(a,b)\le1$，任意物理最近点 $p=(c^3,c)$ 都有 $\delta=\|v(a,b)-v(p)\|=|a-c^3|\le d$。因 $v(y)=v(a,b)$，核反射范数恰 $\delta$，同一个最近锚供应 G2 两项。

跨符号完整立方根界为

\[
|\sqrt[3]u-\sqrt[3]w|\le4^{1/3}|u-w|^{1/3}.
\tag{FY5}
\]

同号由立方差分解、异号由 $(r+t)^3\le4(r^3+t^3)$，常数由 $r=t$ 达到。于是实际全部转移的物理步长
$\|y-(a,b)\|=|\sqrt[3]a-b|\le4^{1/3}d^{1/3}+d\le3d^{1/3}$，供应 G3。

$K(t)=t$、$\psi(K(t)/\lambda)=t/2=\kappa t$，$K(R)/\lambda=1/2\le\bar t$；全域 FY3 供应 G4。$H(t)=3t^{1/3}$，

\[
\Theta(t)=\frac{3t^{1/3}}{1-2^{-1/3}}<\infty.
\tag{FY6}
\]

到 $U$ 补集的距离为 $+\infty$，严格预算自动成立。输入为零距离时 FY2 输出自身；全部纤维无例外。父定理直接给全部初值 $d\le1$ 的统一长度证书。独立闭式 FY2 更强：任意全空间初值一步到 $(a,\sqrt[3]a)$ 后驻定，总长度恰 $|b-\sqrt[3]a|$，完整极限已给出。

### 锐指数与实际比较作用

完整映射在原点的点态最佳 Hölder 指数为 $1/3$，由输入 $(t,0)$ 和 $t\downarrow0$ 取得；有界尺度所有输入对也有 $1/3$ 界，其他 $S$ 点局部 Lipschitz。没有宣称这个图在全空间全尺度有同一个 $1/3$ 常数，也不宣称真实 EB 的最大幂是1；FY3只给充分线性 EB，输出上全零 EB 没有非平凡锐幂身份。

每步 $\Delta v=0$，非解输入的物理步长却非零。因此任何 $\eta(0)=0$ 的纯逆核提升 $\|y-x\|\le\eta(\|v(y)-v(x)\|)$ 均不可能。G3 的 $d$ 项确实处理核不可见运动，$v|S$ 单射与全空间非单射并存。

然而算法本身是一步 consistency solver，直接证明已经极短。它是**自然优化来源的结构例**，展示非单射核范围与真实物理桥，不能作为困难应用、性能优势或全部旧理论无法分析的主例。普通 argmin 阻断 OP2 与它不矛盾：此处是退化 Bregman 核，缺少物理 quadratic 控制。

跨符号、零输入、非孤立 $S$、完整远纤维和参数 $\lambda$ 均已解析穷尽。$\lambda=2$ 是同窗证书的一组参数，不是算法收敛的临界门。有限 [Python 反算](../code/model_selection_limits/README.md)只检查算术；全称结论来自 FY1–6。
