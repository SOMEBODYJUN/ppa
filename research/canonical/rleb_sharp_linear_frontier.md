# 最近零锚 RL–PPA 的联合包络与锐收敛边界

本注固定欧氏范数、步长 $\lambda>0$、关系 $F:\mathbb R^n\rightrightarrows\mathbb R^n$ 和非空闭目标集 $S\subset\operatorname{zer}F$。$r_F(y)=\inf_{w\in F(y)}\|w\|$。合法输入 $x\in U_R=\{x\in U:d(x,S)\le R\}$ 的每个允许输出 $y\in\mathcal J(x)$ 都满足 $(x-y)/\lambda\in F(y)$。覆盖、截断与窗口沿用稿件假设，特别是每个合法输入至少有一个允许输出。对每个这样的 $(x,y)$，存在一个最近锚 $p\in P_S(x)$ 满足 $\|2y-x-p\|\le\omega(d(x,S))$。误差界 $d(y,S)\le\psi(r_F(y))$ 只用于真实残差 $r_F(y)\le\bar t$ 的实际输出。两种模均非降、在零点连续、取零值。

<a id="rsl-envelope"></a>
## 1. 候选 A 的充分性

记 $t=d(x,S)$、$q=d(y,S)$、$s=\|x-y\|$、$a=\|y-p\|$，以及

$$
B(t)=\frac{t+\omega(t)}2,\qquad E(t)^2=\frac{t^2+\omega(t)^2}2.
$$

对同一个锚使用平行四边形恒等式和三角不等式得 $a^2+s^2\le E(t)^2$ 与 $\max\{a,s\}\le B(t)$。先保留 $B(R)/\lambda\le\bar t$，于是 $r_F(y)\le s/\lambda\le\bar t$，再由误差界及非降性得 $q\le\psi(s/\lambda)$。同时 $q\le a\le\sqrt{E(t)^2-s^2}$。因此

$$
q\le\Phi(t)=\sup_{0\le s\le B(t)}\min\{\psi(s/\lambda),\sqrt{E(t)^2-s^2}\}.
$$

$B(t)\le E(t)$，所以上式有定义。$\Phi(t)\le\psi(B(t)/\lambda)$。在线性实例 $F(y)=y/2$、$\lambda=1$、$S=\{0\}$、$L=1/3$、$K=2$ 中，旧门为 $4/3$，新门为 $2/3$，局部有界输入窗可取适当残差帽。这证明严格放宽。该实例已见 `发表成果整理/正则性关系核查.md` §4.1。

若 $\Phi(t)\le\kappa t$ 对所有 $0<t\le R$ 成立且 $0<\kappa<1$，仍有 $s\le B(t)$ 和 $\Theta(t)=\sum_{j\ge0}B(\kappa^jt)$。当 $t=0$ 时反射自动强制 $y=x$。保留 $\Theta(R)<\infty$，以 $B(\kappa^jR)$ 支配并用 $B$ 在零点连续得 $\Theta(t)\to0$。初值严格预算 $\Theta(d(x^0,S))<d(x^0,U^c)$ 使任意合法有限前缀下一输出仍在 $U_R$，继而反复使用覆盖。几何距离、逐步长度、总长度、余尾和极限属于 $S\cap U$ 的原有结论全部保留。此证明只需要 $B$ 非降且在零点连续。

## 2. 保留被候选 A 消去的几何约束

反射不等式等价于 $y$ 落在以 $(x+p)/2$ 为中心、半径 $\omega(t)/2$ 的球内。三角形与距离函数为 1-Lipschitz 分别给出

$$
\max\{0,(t-\omega(t))/2\}\le s\le B(t),\qquad
\max\{0,t-s\}\le q\le \min\{\psi(s/\lambda),t+s,\sqrt{E(t)^2-s^2}\}.
$$

这组约束准确刻画逐点几何松弛。在 $n\ge2$ 中，对每个可行 $(t,q,s)$，可取

$$
\max\{|t-s|,q\}\le a\le\min\{t+s,\sqrt{E(t)^2-s^2}\}
$$

并实现边长 $(t,s,a)$ 的三角形。$s$ 的上下界保证 $|t-s|^2+s^2\le E(t)^2$，故右端至少等于左端。若 $q<a$，在从 $x$ 经 $y$ 向外的射线上放置第二锚，使其距 $y$ 为 $q$；它到 $x$ 的距离 $s+q\ge t$，所以 $p$ 仍最近。如果 $s=0$，已有 $q=a=t$。对给定统一闭目标集或全关系，跨输入实现仍需另证。候选 A 在一般模下可用这个可行域上的 $q$ 上确界替代；空可行域表示在该 $t$ 没有实际转移。

<a id="rsl-factor"></a>
## 3. 线性情形的精确统一一步常数

令 $\omega(t)=Lt$、$\psi(r)=Kr$，其中 $L\ge0$、$K>0$。记

$$
\eta=\lambda/K,\qquad b=(1+L)/2,\qquad e^2=(1+L^2)/2=b^2+(1-b)^2.
$$

由 $q\le s/\eta$ 及上节得到

$$
q\le mt,\qquad m=\min\left\{b,\frac b\eta,\frac e{\sqrt{1+\eta^2}}\right\}.
$$

其中后两项的最小值就是候选 A 的线性系数。对于 $t>0$，$t\le s+q\le (1+1/\eta)bt$，所以非平凡输入必须满足 $b\ge\eta/(1+\eta)$。特别地，$L<1$ 且 $\eta>(1+L)/(1-L)$ 时，在假设的覆盖与误差界下全部工作输入均在 $S$，任何返回的输出驻定。这一域可行性限制源自 $t\le s+q$。

在 $b\ge\eta/(1+\eta)$ 下，上界通过下列完整闭图关系达到。参数视为给定的合法上界，未统一要求 $L,K$ 都是原关系的最小模常数。

1. **$m=b$。** 取 $J=bI$，$F=(1/b-1)I/\lambda$，$S=\{0\}$。$b>0$，而 $b\le e/\sqrt{1+\eta^2}$ 给出 $|1-b|\ge\eta b>0$，所以 $F$ 有该零集和所需真残差 EB。反射范数为 $|2b-1|=L$。
2. **$m=e/\sqrt{1+\eta^2}$。** 记 $A=m$、$H=\eta m$。$A,H\le b$ 且 $A^2+H^2=e^2$，从 $(b^2-A^2)(b^2-H^2)\ge0$ 得 $AH\ge b|1-b|=|e^2-1|/2$。因此 $|A-H|\le1\le A+H$。在复平面取 $|z|=A$、$|1-z|=H$。定义完整线性 $J(x)=zx$，$F(y)=(z^{-1}-1)y/\lambda$。$z\ne0,1$。有 $r_F(y)=\eta\|y\|/\lambda$、$|2z-1|=L$、实际距离因子 $|z|=m$。该构造即原补充稿的旋转族在它的可行参数范围内。
3. **$m=b/\eta$ 严格最小。** 设 $c=b/\eta$。能量不等式的严格比较给 $c<|1-b|$，结合非空条件排除 $b<1$，故 $b>1$、$c<b-1$。令 $r_n=\delta^n$，其中 $0<\delta<1/(2c+b+3)$。设

$$
y_n=(2c+2)r_n,\quad p'_n=(c+2)r_n,\quad
p_n=(2c+b+1)r_n,\quad x_n=(2c+b+2)r_n.
$$

令 $S=\{0\}\cup\{p_n,p'_n:n\ge1\}$，以所有投影输出 $P_S(x)$ 组成 $J$，另添 $J(x_n)\ni y_n$。各组处于两两不交的区间 $[r_n,(2c+b+3)r_n]$，且 $x_n,y_n$ 离所在区间外边界的距离至少分别为 $r_n,cr_n$。故 $d(x_n,S)=r_n$ 最近锚 $p_n$，$d(y_n,S)=cr_n$ 最近锚 $p'_n$；后者离 $p_n$ 的距离为 $(b-1)r_n>cr_n$。定义

$$
F(u)=\{(x-u)/\lambda:u\in J(x)\}.
$$

$\operatorname{gph}P_S$ 闭，新增边只累积于 $(0,0)$，故 $J$ 和 $F$ 是闭图，$J$ 完整、$S=\operatorname{Fix}J=\operatorname{zer}F$。投影边反射比为 $1$（零输入驻定），因此由 $L>1$ 覆盖；其输出均在 $S$。额外边有 $s=br_n$、$r_F(y_n)=br_n/\lambda$，反射比为 $2b-1=L$，且 $d(y_n,S)=K r_F(y_n)=cr_n$。整个关系满足所需真残差条件。等号支由前两种情形覆盖。三种构造各有趋于基点的取等输入；下节说明有界输入内的截断可以完整保留所需边与覆盖。

<a id="rsl-threshold"></a>
## 4. 全部允许选择的锐局部收敛门

上述距离因子结合步长界 $s\le bt$ 得到严格门

$$
L<L_{\mathrm{crit}}(\eta)=
\begin{cases}
\sqrt{1+2\eta^2},&0<\eta\le2,\\
2\eta-1,&\eta>2.
\end{cases}
$$

确实，$m<1$ 等价于 $L<\max\{1,2\eta-1,\sqrt{1+2\eta^2}\}$，两后一项在 $\eta=2$ 换序。对 $0<\eta\le2$，原旋转族在等号可取 $F(u)=(\alpha I+\beta Q)u/\lambda$，$\alpha=-\eta^2/2$、$\beta^2=\eta^2(1-\eta^2/4)$，其中 $Q$ 是九十度旋转。$J$ 为非恒等正交变换，所有非零轨道范数恒定且步长恒正，故不收敛；$\eta=2$ 时为 $J=-I$。

对 $\eta>2$，令 $0<\delta<1/(\eta+3)$、$r_n=\delta^n$，设置

$$
x_n=2r_n,\quad y_n=(\eta+2)r_n,\quad
p_n=3r_n,\quad p'_n=(\eta+1)r_n.
$$

定义 $S=\{0\}\cup\{p_n,p'_n:n\ge1\}$ 及 $J=P_S$ 加上所有 $x_n\leftrightarrow y_n$ 双向边，$F$ 按上一节由 $J$ 恢复。各组落在两两不交的 $[r_n,(\eta+3)r_n]$。两端到 $S$ 均为 $r_n$，最近锚分别是 $p_n,p'_n$，因此双向步长是 $\eta r_n$ 且真实残差都是 $\eta r_n/\lambda$。这些端点只由相对端点作前像，真 EB 为等号；投影输出的误差与残差均为零。双向边都满足 $\|2y-x-p\|=(2\eta-1)d(x,S)$，投影边只需要 $L=1$。两关系闭图、全输入都有投影输出，完整零集是 $S$。取任意足够大的有界开区间 $V'\supset U_R$、$V=\mathbb R$，再取含 $\{x-p:x\in V',p\in P_S(x)\}$ 的开窗口 $W$，得到截断覆盖。在足够小的工作半径内，$B(R)/\lambda\le\bar t$；所有充分大的 $n$ 的双向边仍在截断窗口内，其端点趋于 $0$。这些轨道严格二周期，因此不存在从 $0$ 的某邻域开始、所有允许选择均收敛的保证。更大的声明 $L$ 仍允许同一个例子。

若 $\bar x$ 局部孤立，可缩小输入域，使 $x,y$ 的最近零均是 $\bar x$。此时 $\eta q\le s\le t+q$，故 $\eta>2$ 时已有 $q\le t/(\eta-1)$，任意有限 $L$ 均可。这个区别说明高 $\eta$ 区间的完整类必要性见证依赖非孤立零锚几何。固定空间维数为一时，低 $\eta$ 分支的二维达到见证不能作一维锐性结论。

## 5. 与仓库既有成果的边界

基线为 `911cb5b4da26301db1a7d96725783dbb85a7972f`。`C253`／`research/canonical/physical_rleb_gppa.md` 第 579–648 行已给线性能量充分性及准确评价窗，`C277`／`research/canonical/unified_ppa_joint_certificates.md` 第 21–102 行已给一般原图联合投影方法。英文附件 `PPA_LaTeX/sections/theorem_spine.tex` 第 112–146 行含过强的全参数锐性和一步残差窗缺项，`PPA_LaTeX/supplements/linear_attainment.tex` 第 28–57 行已将旋转实现限定在可行参数及 $\eta\le2$ 边界。仓库的中文修订正文 `发表成果整理/RLEB/sections/theorem_spine.tex` 第 191–247、340–386 行已补评价窗并限制旋转族与能量充分条件的范围。定向检索既有规范正文、声明和失败路线，未发现上述非孤立零锚的完整闭图高参数反例或对有限维类统一的分段锐门。该查重范围也允许另处出现同一结果，公开优先性需另做一手文献比对。
