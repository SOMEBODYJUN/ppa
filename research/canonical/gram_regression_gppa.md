# 耦合 Gram 核的欠定矩阵回归

本页 C270-v1 给自然优化来源的定量 GPPA 例：非强凸原生矩阵核、未观测变量漂移、完整唯一近端、显式极限。RLEB–GPPA可直接认证一个共同物理窗；经典核坐标证明更能给全空间全参数收敛，必须并列。它不承担“全部旧理论不能分析”的主例作用，也不认证设备性能或公开优先。

<a id="grg-object"></a>
## 任务、完整算法与全部纤维

取 $X=\mathbb R^{m\times2}$、$m\ge2$，使用 Frobenius 范数，$Z=[a\ b]$。欠定 least-squares 只观测第一列：

\[
f(Z)=\tfrac12\|a\|^2,\quad F(Z)=\{[a\ 0]\},\quad
S=F^{-1}(0)=\operatorname{argmin}f=\{[0\ b]\},\quad r_F(Z)=d(Z,S)=\|a\|.
\tag{GR1}
\]

预先选取耦合 Gram/Schatten-4 核

\[
h(Z)=\tfrac14\operatorname{tr}((Z^TZ)^2),\quad v(Z)=ZZ^TZ=[u\ k],
\quad u=\|a\|^2a+\langle a,b\rangle b,\quad
k=\langle a,b\rangle a+\|b\|^2b.
\tag{GR2}
\]

不是从理想映射反造目标。此任务无低秩约束，不能改称低秩恢复。非零数据可先用预定数据和中心作残差坐标平移；核也明确作用于残差矩阵。文献[Gram背景与指定旧合同](../LITERATURE.md#lit-gram-degenerate)不等于已经发表本纯退化算法。

任意固定 $\lambda>0$、全空间输入，使用完整 $J^v_{\lambda F}=(v+\lambda F)^{-1}v$。对输入 $Z$，全部输出 $Y=[\alpha\ \beta]$ 恰满足

\[
(\|\alpha\|^2+\lambda)\alpha+\langle\alpha,\beta\rangle\beta=u,
\qquad \langle\alpha,\beta\rangle\alpha+\|\beta\|^2\beta=k.
\tag{GR3}
\]

以下严格凸性和 $h\ge\|Z\|_F^4/8$ 使 $h+\lambda f-\langle v(Z),Y\rangle$ coercive、严格凸、$C^1$。因此每个输入完整纤维恰一个根，也是完整 Bregman argmin；不存在删去的非极小根。没有通用初等闭式向量 inverse，GR3加唯一性就是完整逆关系。

<a id="grg-inverse"></a>
## 全域逆模、退化与零输入

直接微分得

\[
D^2h(Z)[H,H]=\tfrac12\|ZH^T+HZ^T\|_F^2+\|Z^TH\|_F^2.
\]

沿段 $Z+tH$ 在中点展开，第一项变化平方积分贡献 $\|HH^T\|_F^2/6$，第二项贡献 $\|H^TH\|_F^2/12$，其余中点平方非负。两列给

\[
\langle v(Z+H)-v(Z),H\rangle\ge\tfrac14\|H^TH\|_F^2
\ge\tfrac18\|H\|_F^4,
\quad\|Z-Z'\|_F\le2\|v(Z)-v(Z')\|_F^{1/3}.
\tag{GR4}
\]

所以 $h$ 严格凸。SVD 将奇异值 $\sigma$ 变成 $\sigma^3$，说明 $v$ 全域同胚。对 $Z=[0\ b]$、$H=[w\ 0]$、$w\perp b$，Hessian为零；$b=0$ 时所有方向均零。故每个零点邻域都没有正强凸模，单射性却保留。

零输入的 GR3 首式点乘 $\alpha$ 强制 $\alpha=0$，次式径向单射强制 $\beta=b$；整个非孤立 $S$ 完整吸收，包括中心。

<a id="grg-certificate"></a>
## 同一物理最近锚与显式 C249 证书

唯一物理最近点为 $P_Z=[0\ b]$。每个完整输出满足

\[
\langle v(Y)-v(P_Z),F(Y)\rangle
=\|\alpha\|^4+\langle\alpha,\beta\rangle^2\ge0.
\tag{GR5}
\]

因此以 $\xi=v(Y)-v(P_Z)$、$\eta=v(Z)-v(Y)=\lambda F(Y)$ 写，$\|\xi-\eta\|\le\|\xi+\eta\|$。同一个物理最近锚供应核反射界，未换成极限零点。

固定

\[
U=\{\|b\|<2\},\ R=10^{-6},\ \lambda=10,\ \bar t=1,\ \kappa=1/2,
\quad a_{\rm scale}(t)=5t,\quad\omega=\psi=Id,
\quad\mathfrak h(t,q)=2q^{1/3}.
\tag{GR6}
\]

G1全域唯一 coverage已证。对 $Z\in U_R$，$d=\|a\|$、$B=\|b\|<2$，

\[
\delta=\|v(Z)-v(P_Z)\|_F\le d^3+dB^2+d^2B
\le(4+2R+R^2)d\le5d.
\]

GR5给 G2反射 $\le\delta$；GR4全域给 G3，不预设输出留 $U$。GR1的真实 EB全域等号给 G4，$K(t)=5t$、$K(R)/\lambda=R/2\le\bar t$。全部 $0<t\le R$ 的 G5为 $\psi(K(t)/\lambda)=t/2$。

\[
H(t)=2(5t)^{1/3},\qquad
\Theta(t)=\frac{2\,5^{1/3}t^{1/3}}{1-2^{-1/3}},\qquad\Theta(R)<.167.
\tag{GR7}
\]

补集距离恰 $2-\|b_0\|$。所有满足 $\Theta(d_0)<2-\|b_0\|$ 的 $U_R$ 初值逐全部前缀留域、有限长度趋 $S$；特别 $\|a_0\|\le10^{-6},\|b_0\|\le1$ 全部成立。不声称靠近 $U$ 边界的全部 $U_R$ 初值自动满足预算。由C249有 $d_k\le2^{-k}d_0$、物理尾 $\le\Theta(2^{-k}d_0)$。

<a id="grg-limit"></a>
## 显式极限、轨道子族和锐读出指数

GR3使 $k$ 沿轨道恒定。令 $B_3(c)=\|c\|^2c$，则

\[
Z_\infty=[0\ B_3^{-1}(k_0)],\qquad
k_0=\langle a_0,b_0\rangle a_0+\|b_0\|^2b_0.
\tag{GR8}
\]

$B_3^{-1}(k)=\|k\|^{-2/3}k$（$k\ne0$），零处取零。一般未观测列改变；不是一步例。$a_0\perp b_0$ 时完整唯一输出保持正交、第二列不变，非零第一列长度满足 $e_k^3=e_{k+1}^3+\lambda e_{k+1}$，故 $e_{k+1}/e_k^3\to1/\lambda$。一般轨道无初等闭式，极限却有 GR8。

在输入范数球 $\|Z\|,\|Z'\|\le M$，$k(Z)$ 的 Lipschitz常数可取 $3M^2$，径向三次的逆模常数 $4^{1/3}$ 给
$\|Z_\infty-Z'_\infty\|\le(12M^2)^{1/3}\|Z-Z'\|^{1/3}$。固定任意小 $t>0$、单位 $c$，比较 $[tc,0]$ 与 $[tc,\epsilon c]$，极限差为 $|(t^2+\epsilon^2)\epsilon|^{1/3}\sim t^{2/3}|\epsilon|^{1/3}$。两点指数 $1/3$ **锐**，见证可任意近中心。

<a id="grg-prox-exponent"></a>
## 一步近端指数的已证范围

GR4与 $F$ 单调使 $v+\lambda F$ 仍有同一 $1/3$ 逆模，$v$ 在有界集 Lipschitz，所以完整物理prox两点有 $1/3$ 上界。

共线输入 $[tc,bc]$ 的唯一输出 $[u c,w c]$ 满足
$(u^2+w^2+\lambda)u=t(t^2+b^2)$、$(u^2+w^2)w=b(t^2+b^2)$。$b=0$ 时 $u\sim t^3/\lambda$；固定 $t>0$ 的 IFT给 $\partial w/\partial b=t^2/u^2\sim\lambda^2t^{-4}$，任意原点邻域无共同两点 Lipschitz常数。

进一步 $b=\zeta t^7$、$u=t^3U$、$w=t^3W$，$\zeta\ne0$，精确方程变为

\[
\lambda U+t^6(U^2+W^2)U=1+\zeta^2t^{12},\qquad
(U^2+W^2)W=\zeta+\zeta^3t^{12}.
\tag{GR9}
\]

第一式界 $U$，第二式界 $W$，聚点唯一给 $U\to1/\lambda$、$(\lambda^{-2}+W_\zeta^2)W_\zeta=\zeta$、$W_\zeta\ne0$。输入对距 $|\zeta|t^7$，输出对距为至少常数 $t^3$，故任何指数 $>3/7$ 的共同界失败。

**尚未证明 $3/7$ 上界**；最佳两点指数只已知在 $[1/3,3/7]$。这不是 fixed-zero noncalm：两输入到 $S$ 的距离都是 $t$。包含点乘 $Y$ 给 $\|Y\|_F^4/2\le\langle v(Z),Y\rangle\le\|Z\|_F^3\|Y\|_F$，所以原点锚仍有 $\|Y\|\le2^{1/3}\|Z\|$。不能取代 C241的解点非calm作用。真 EB为精确线性等号，最大幂1由法向缩小族直接取得。

<a id="grg-classical"></a>
## 更短全域经典正面及实际比较

第二列 $k$ 守恒；第一列 $u_{\rm in}=u_{\rm out}+\lambda\alpha$，GR5点乘首列给
$\|u_{\rm in}\|^2\ge\|u_{\rm out}\|^2+\lambda^2\|\alpha\|^2$。因此核范数不增。$\|Z\|_F^3\le2\|v(Z)\|_F$ 给全前缀界 $M_0=(2\|v(Z_0)\|_F)^{1/3}$。$M_0>0$ 时 $\|u_{\rm out}\|\le M_0^2\|\alpha\|$，故

\[
\|u_{k+1}\|\le\rho\|u_k\|,\quad
\rho=\frac{M_0^2}{\sqrt{M_0^4+\lambda^2}}<1,
\quad\sum_k\|Z_{k+1}-Z_k\|_F
\le\frac{2[(1+\rho)\|u_0\|]^{1/3}}{1-\rho^{1/3}}.
\tag{GR10}
\]

$M_0=0$ 直接驻定。核同胚及 $u_k\to0$ 给GR8。这个**同算法**正面适用于全部初值、全部固定 $\lambda>0$，比GR6局部证书更强，不需要新RLEB几何。固定核零锚为 $[0,B_3^{-1}(k_0)]$，不冒充物理最近锚。

在GR6同组 $\lambda=10$、$U_R$ 局部窗口内，原目标也有ABS正面。GR3首式给 $\|\alpha\|<.41d$（$d>0$；$d=0$时吸收取等）；守恒式 $B_3(\beta)-B_3(b)=\langle a,b\rangle a-\langle\alpha,\beta\rangle\alpha$，配合
$\langle B_3(\beta)-B_3(b),\beta-b\rangle\ge(\|b\|^2+\|\beta\|^2)\|\beta-b\|^2/2$，分分母平方根是否至少 $d$ 两情形，给 $\|\beta-b\|\le2\sqrt2d$，实际步 $\le4d$。于是原 $f$ 有H1系数 $(1-.41^2)/32$、H2系数 $.41/.59$、KL指数 $1/2$，严格内窗有限长度供应H3。不应声称原能量不能满足ABS。

指定[BSTV 1706.06461v1 §4.2](../LITERATURE.md#lit-gram-degenerate)的 Eq.(3.4)以其 $f$ 取本 $f$、$g=0$、$h$取GR2，正是本算法；$g=0$使任意 $L>0$ 的smad成立，可取 $\lambda L=1/2$。其Theorem4.1正强凸核前件在所有零点邻域失败，不能直接用；这只说明**免该指定前件**，GR10及原f-ABS正面仍存在。

添加正二次 $\sigma\|Z\|^2/2$ 会改变核与真实算法：不变量变为 $k_\sigma=k_0+\sigma b_0$，极限满足 $(\|b_{\infty,\sigma}\|^2+\sigma)b_{\infty,\sigma}=k_\sigma$。$\sigma>0$读出在紧集上Lip，纯Gram读出锐1/3，不是无代价的同算法修补。没有由此授任意时变核、任意正定度量或全局统一率。

本例适合补充自然定量GPPA接口，不作强应用优势主例。完整证明与[接收](../../发表成果整理/本轮模型筛选独立接收.md)分开，有限[Python](../code/model_selection_limits/README.md)不证明所有输出或最佳未闭指数。
