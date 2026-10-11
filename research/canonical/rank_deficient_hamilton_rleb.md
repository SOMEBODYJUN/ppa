# 秩亏 Hamilton 例：完整输入图像上的 RLEB

登记：C241。数学状态：`derived-checked`，限于本页精确参数和完整独立证明；当前论文的同一证明已另经核心独立审查。比较状态：只比较本页列出的证书和明确版本的文献假设；不构成新颖性认证。本页不依赖历史笔记、论文 TeX 或其他规范页补充定义。

<a id="hrl-object"></a>

## 1. 精确对象与命题〔hrl-object〕

全页使用欧氏空间和欧氏范数。令

$$
X=\mathbb R^2_x\times\mathbb R^2_p,\qquad
\|(x,p)\|^2=\|x\|^2+\|p\|^2,
$$

$$
f(x)=\frac23|x_1|^{3/2},\qquad
k(p)=\frac23\|p\|^{3/2},
$$

$$
g(x)=\nabla f(x)=
\bigl(\operatorname{sgn}(x_1)\sqrt{|x_1|},0\bigr),\qquad
h(p)=\nabla k(p)=
\begin{cases}
p/\sqrt{\|p\|},&p\ne0,\\
0,&p=0.
\end{cases}
$$

约定 $\operatorname{sgn}(0)=0$。阻尼为 $\Gamma=99$，定义原算子及其完整图像

$$
F:X\to X,\qquad F(x,p)=(-h(p),g(x)+99p),\qquad
\operatorname{gph}F=\{(y,F(y)):y\in X\}.
$$

零点集、距离及真残差分别为

$$
S=F^{-1}(0)=\{((0,s),0):s\in\mathbb R\},
$$

$$
d(y,S)=\inf_{s\in S}\|y-s\|,\qquad
d((x,p),S)=\sqrt{x_1^2+\|p\|^2},\qquad
r_F(y)=\|F(y)\|.
$$

对 $F$ 的零点和残差没有另取替代算子。$S$ 非空且闭，包含全部自由位置坐标。

取步长 $\lambda=1$，预解关系是

$$
J_F(w)=\{y:w=y+F(y)\}.
$$

输入 $w=(a,b)\in\mathbb R^2\times\mathbb R^2$、输出 $y=(x,p)$ 的方程为

$$
a=x-h(p),\qquad b=g(x)+100p. \tag{H1}
$$

原全隐式迭代写为

$$
z^{j+1}=J_F(z^j),\qquad
x^{j+1}-x^j=h(p^{j+1}),\qquad
p^{j+1}-p^j=-g(x^{j+1})-99p^{j+1}. \tag{H2}
$$

取开放工作集 $U=X$ 及局部输入管

$$
R=10^{-6},\qquad
U_R=\{w:d(w,S)\leq R\}
=\{(a,b):a_1^2+\|b\|^2\leq R^2\}.
$$

此处 $a_2$ 完全不受限制。定义完整输入图像块

$$
\mathcal G_R=\{(y,F(y)):y+F(y)\in U_R\}. \tag{H3}
$$

这保留 $U_R$ 中每个输入的全部近端输出，不选分支、不删除点对。记
$M_+(y,F(y))=y+F(y)$，并定义
$J_{\mathcal G_R}(w)=\{y:(y,w-y)\in\mathcal G_R\}$。

本例的参数为

| 参数 | 取值 |
| --- | --- |
| $\lambda$ | $1$ |
| $\gamma$（RL 的 Hölder 指数） | $1/2$ |
| $L$ | $1/2$ |
| $\bar t$（残差区间上端） | $1$ |
| $\psi:[0,1]\to[0,\infty)$ | $\psi(t)=3t^2$ |
| $\kappa$ | $1/4$ |
| $R$ | $10^{-6}$ |

**命题 H。** $J_F$ 在整个 $X$ 上存在且唯一，且
$J_{\mathcal G_R}=J_F$ 在 $U_R$ 上成立。上述对象满足以下四项条件：

1. **覆盖与零点锚定。** $U_R\subset M_+(\mathcal G_R)$，每个 $w\in U_R$ 的最近零点 $s_w=((0,a_2),0)$ 满足 $(s_w,0)\in\mathcal G_R$。
2. **全部点对的 RL。** 对任意 $(y,F(y)),(v,F(v))\in\mathcal G_R$，记
   $\delta=\|(y+F(y))-(v+F(v))\|$。只要 $\delta\leq R$，就有

   $$
   \langle y-v,F(y)-F(v)\rangle
   \geq\frac14\bigl(\delta^2-L^2\delta^{2\gamma}\bigr). \tag{H4}
   $$

3. **输出上的真残差 EB。** 对每个 $y\in J_F(U_R)$，
   $r_F(y)\leq1$ 且 $d(y,S)\leq3r_F(y)^2$；并且
   $(R+LR^\gamma)/(2\lambda)\leq\bar t$。
4. **标量相容。** 对所有 $0<r\leq R$，

   $$
   \psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right)\leq\kappa r. \tag{H5}
   $$

因此每个 $z^0\in U_R$ 产生唯一无限轨道，轨道保持在 $U_R$ 内、具有有限长度，并收敛到某个 $z^\infty\in S$。令 $d_0=d(z^0,S)$，则

$$
d(z^j,S)\leq4^{-j}d_0,\qquad
\|z^j-z^\infty\|\leq\frac23\,4^{-j}d_0
                         +\frac12\,2^{-j}\sqrt{d_0}. \tag{H6}
$$

这允许非零初始动量。$\gamma=1/2$ 是同一完整局部图像上最大的 Hölder 指数，EB 的幂次 $2$ 也不能提升；(H6) 中的几何因子只作为统一上界，不宣称是实际最优收敛因子。

<a id="hrl-proof"></a>

## 2. 自足证明〔hrl-proof〕

### H-P1. 全空间求解与覆盖

动能的凸共轭为 $k^*(u)=\|u\|^3/3$。对任意输入 $(a,b)\in X$，考虑

$$
\Phi_{a,b}(u)=\frac13\|u-a\|^3+\frac1{100}f(u)
-\frac1{100}\langle b,u\rangle.
$$

三次范数项严格凸且强制，$f$ 凸且非负，线性项不破坏强制性。故 $\Phi_{a,b}$ 有唯一极小点 $x$。它处处可微，一阶条件是

$$
100\|x-a\|(x-a)+g(x)-b=0.
$$

令 $p=\|x-a\|(x-a)$，则 $h(p)=x-a$，包括 $x=a$ 时的 $p=0$；因此 $(x,p)$ 满足 (H1)。反过来，任何 (H1) 的解都满足上述一阶条件并且必须有 $p=\|x-a\|(x-a)$。这证明了全空间的存在性与唯一性。

根据 (H3)，$U_R$ 中唯一输出的图像点都保留在 $\mathcal G_R$，因此 $J_{\mathcal G_R}=J_F$ 在该输入管上成立。每个 $s\in S$ 满足 $F(s)=0$ 且 $s\in U_R$，故 $(s,0)\in\mathcal G_R$。最近零点 $s_w=((0,a_2),0)$ 可直接由距离公式算出。命题 H 的第 1 项得证。

### H-P2. 输出动量范围

设 $(a,b)\in U_R$，令 $(x,p)=J_F(a,b)$、$P=\|p\|$。有
$|a_1|\leq R$、$\|b\|\leq R$。若 $p_1g_1(x_1)\geq0$，则

$$
\|b\|^2=\|g(x)\|^2+10000P^2+200p_1g_1(x_1)\geq10000P^2,
$$

所以 $P\leq R/100$。若 $p_1g_1(x_1)<0$，则 $P>0$，
$x_1=a_1+p_1/\sqrt P$ 与 $p_1$ 异号，故
$|p_1|\leq|a_1|\sqrt P\leq R\sqrt P$。又 $p_2=b_2/100$，因此

$$
P^2=p_1^2+p_2^2\leq R^2P+R^2/10000.
$$

若 $P>R$，则

$$
P^2-R^2P>R^2-R^3=R^2(1-R)>R^2/10000,
$$

矛盾。因此所有允许输出都满足

$$
\|p\|\leq R. \tag{H7}
$$

第一种情形已经包含 $p=0$，不存在除零步骤。

### H-P3. 原动能梯度的割线估计，包含原点

令 $\beta=\sqrt2/4$。设 $p=(q,r)$、$\widetilde p=(\widetilde q,\widetilde r)$ 均在闭球 $\|p\|\leq R$ 内。若
$\Delta q=q-\widetilde q\geq\beta|\Delta r|$，则

$$
h_1(p)-h_1(\widetilde p)
\geq\frac{\Delta q-\beta|\Delta r|}{2\sqrt R}. \tag{H8}
$$

证明如下。沿原函数的线段
$p_\tau=\widetilde p+\tau(p-\widetilde p)$，球的凸性保证
$\|p_\tau\|\leq R$。在 $p_\tau\ne0$ 处直接求导：

$$
A(q,r)=\partial_qh_1
=\frac{q^2+2r^2}{2(q^2+r^2)^{5/4}}
\geq\frac1{2\sqrt R},\qquad
B(q,r)=\partial_rh_1
=-\frac{qr}{2(q^2+r^2)^{5/4}}.
$$

由于 $q^2+2r^2\geq2\sqrt2|qr|$，有 $|B|\leq\beta A$。所以

$$
\frac d{d\tau}h_1(p_\tau)
=A(p_\tau)\Delta q+B(p_\tau)\Delta r
\geq\frac{\Delta q-\beta|\Delta r|}{2\sqrt R}.
$$

不经过原点的线段直接由微积分基本定理得 (H8)。若两端均为零，结论显然。其余情况下线段至多在一个 $\tau_0$ 处经过原点。令
$v=p-\widetilde p\ne0$，则有原函数的精确表达式

$$
p_\tau=(\tau-\tau_0)v,\qquad
h_1(p_\tau)=
\operatorname{sgn}(\tau-\tau_0)\sqrt{|\tau-\tau_0|}
\frac{v_1}{\sqrt{\|v\|}}.
$$

这在 $\tau_0$ 连续。若 $0<\tau_0<1$，先在
$[0,\tau_0-\varepsilon]$ 和 $[\tau_0+\varepsilon,1]$ 上分别积分上面的导数下界，其总长度为 $1-2\varepsilon$。缺少区间的端点差由精确表达式趋于零。令 $\varepsilon\downarrow0$ 得 (H8)。若 $\tau_0=0$ 或 $1$，只去掉相应端点的单侧区间并作同样计算。这里没有使用平滑正则化、正则化 Jacobian 或未证明的平滑极限。

### H-P4. 原近端方程的两点动量估计，包含 $x_1=0$

取任意两个允许输入 $(a,b),(\widetilde a,\widetilde b)\in U_R$，及其唯一输出 $(x,p),(\widetilde x,\widetilde p)$。由 (H1)，

$$
\Delta p_2=\frac{\Delta b_2}{100}.
$$

证明以下有限差分界：

$$
|\Delta p_1|\leq
\max\left\{\frac{|\Delta b_1|}{100},
2\sqrt R|\Delta a_1|+\frac{\beta}{100}|\Delta b_2|\right\}. \tag{H9}
$$

先设 $\Delta q=\Delta p_1>0$。若它严格大于右侧的两个量，则
$\Delta q>\beta|\Delta p_2|$，由 (H7) 和 (H8) 得
$h_1(p)-h_1(\widetilde p)>|\Delta a_1|$。于是 (H1) 的第一式给出
$\Delta x_1=\Delta a_1+h_1(p)-h_1(\widetilde p)>0$。
$g_1(t)=\operatorname{sgn}(t)\sqrt{|t|}$ 连续且严格递增，因此
$\Delta g_1>0$。但第二式给出
$\Delta g_1=\Delta b_1-100\Delta q<0$，矛盾。
交换两点处理 $\Delta q<0$；$\Delta q=0$ 时显然。
这仅使用 $g_1$ 的单调性，故适用于 $x_1=0$、
$\widetilde x_1=0$ 和两点跨越零点的情形。

放大 (H9) 的最大值为非负项之和，对第一坐标应用 Cauchy–Schwarz，再加上第二动量坐标的平方，得到

$$
\|p-\widetilde p\|
\leq K_R\|(a,b)-(\widetilde a,\widetilde b)\|,\qquad
K_R=\left(4R+\frac{2+\beta^2}{10000}\right)^{1/2}. \tag{H10}
$$

其中 $K_R^2=0.0002165<0.015^2<0.02^2$。因此可在所有点对上统一使用动量 Lipschitz 常数 $0.02$。

### H-P5. 动能梯度的全局 Hölder 界

对任意 $p,\widetilde p\in\mathbb R^2$，

$$
\|h(p)-h(\widetilde p)\|^2\leq2\|p-\widetilde p\|. \tag{H11}
$$

令 $u=h(p)$、$v=h(\widetilde p)$，则
$p=\|u\|u$、$\widetilde p=\|v\|v$，包括零向量。直接展开得

$$
\langle p-\widetilde p,u-v\rangle
=\frac{\|u\|+\|v\|}{2}
\left(\|u-v\|^2+(\|u\|-\|v\|)^2\right)
\geq\frac12\|u-v\|^3,
$$

因为 $\|u\|+\|v\|\geq\|u-v\|$。Cauchy–Schwarz 给出
$\|p-\widetilde p\|\|u-v\|\geq\|u-v\|^3/2$。
$u\ne v$ 时约去 $\|u-v\|$；$u=v$ 时结论显然。这证明 (H11)。

### H-P6. 完整图像块上的 all-pair RL

定义反射预解式 $C=2J_F-I$。由 (H1)，

$$
C(a,b)=(a+2h(p),2p-b).
$$

对上述任意两个输入，设 $\delta=\|(a,b)-(\widetilde a,\widetilde b)\|\leq R$。使用 (H10)、(H11) 和三角不等式得

$$
\begin{aligned}
\|C(a,b)-C(\widetilde a,\widetilde b)\|
&\leq\delta+2\|h(p)-h(\widetilde p)\|+2\|p-\widetilde p\|\\
&\leq2\sqrt{0.04\,\delta}+1.04\delta\\
&\leq(0.4+1.04\sqrt R)\sqrt\delta\\
&=0.40104\sqrt\delta\leq L\delta^{1/2}.
\end{aligned} \tag{H12}
$$

两输入相同时 (H12) 显然。每个 $\mathcal G_R$ 中图像点都对应一个 $U_R$ 中输入，所以 (H12) 已涵盖图像块的全部允许点对。

具体地，记 $A=y-v$、$B=F(y)-F(v)$，则输入差为 $A+B$、反射差为 $A-B$，且

$$
\|A+B\|^2-\|A-B\|^2=4\langle A,B\rangle.
$$

因此 (H12) 恰好等价于 (H4)，验证命题 H 的第 2 项。

### H-P7. 真残差误差界与区间

对允许输出 $y=(x,p)$ 令 $\rho=r_F(y)$。由原算子的定义，

$$
\rho^2=\|F(x,p)\|^2=\|p\|+\|g(x)+99p\|^2. \tag{H13}
$$

没有删去残差中的任一块。由 (H7)、(H13) 得

$$
\|p\|\leq\rho^2,\qquad
\|g(x)\|\leq\rho+99\|p\|
\leq(1+99\sqrt R)\rho.
$$

最后一步使用
$\|p\|\leq\sqrt R\sqrt{\|p\|}\leq\sqrt R\,\rho$。于是

$$
\begin{aligned}
d((x,p),S)
&=\sqrt{|x_1|^2+\|p\|^2}
\leq |x_1|+\|p\|\\
&=\|g(x)\|^2+\|p\|\\
&\leq\bigl((1+99\sqrt R)^2+1\bigr)\rho^2
=2.207801\rho^2\leq3\rho^2.
\end{aligned} \tag{H14}
$$

零残差意味着输出在 $S$，同一界成立。由 (H1)，
$g(x)+99p=b-p$，故

$$
\rho^2\leq R+4R^2<1.
$$

因此整个允许输出块都在 $\psi$ 的残差区间内。另有

$$
\frac{R+LR^\gamma}{2\lambda}
=\frac{10^{-6}+(1/2)10^{-3}}2
=0.0002505<1=\bar t.
$$

这验证第 3 项。

### H-P8. 标量相容、留域和整条轨道收敛

对 $0<r\leq R$，

$$
\frac{\psi((r+L\sqrt r)/2)}r
=\frac34(\sqrt r+1/2)^2
\leq\frac34(0.501)^2
=0.18825075<\frac14. \tag{H15}
$$

其 $r\downarrow0$ 极限是 $3/16<1$。这给出第 4 项。
数值 $1/4$ 是方便的统一收缩上界，不是该标量商的最小上界，也未被证明为实际轨道的最佳距离因子。

以下直接证明收敛，无需援引外部 RLEB 定理。给定 $w\in U_R$，
令 $s=s_w$ 为最近零点、$d=\|w-s\|\leq R$、$y=J_F(w)$。
由于 $J_F(s)=s$，(H12) 给出

$$
\|w-y\|
=\frac12\|(w-s)-(Cw-s)\|
\leq\frac12(d+L\sqrt d).
$$

$F(y)=w-y$，所以真残差恰为 $\rho=\|w-y\|$。由 (H14)、(H15)，

$$
d(y,S)\leq\psi(\rho)
\leq\psi((d+L\sqrt d)/2)\leq\kappa d.
$$

$d=0$ 时 $w\in S$，其唯一输出是自身，结论仍成立。
因此输出继续在 $U_R$ 内，归纳得到唯一无限轨道和
$d_j=d(z^j,S)\leq4^{-j}d_0$。又有

$$
\|z^{j+1}-z^j\|
\leq\frac12\left(4^{-j}d_0+\frac12\,2^{-j}\sqrt{d_0}\right).
$$

求和得有限长度及尾长度上界

$$
\sum_{\ell=j}^{\infty}\|z^{\ell+1}-z^\ell\|
\leq\frac23\,4^{-j}d_0+\frac12\,2^{-j}\sqrt{d_0}.
$$

欧氏空间完备，因此轨道收敛到 $z^\infty$；$d_j\to0$ 且 $S$ 闭，故 $z^\infty\in S$。尾项界由尾长度界得到。(H6) 得证。

这里 $U=X$，$X\setminus U=\varnothing$，约定
$d(z^0,\varnothing)=+\infty$。若采用“总长度预算小于到工作集补集的距离”的留域表述，总长度预算有限，因而该条件自动成立；输入管留域则已由上面的距离递推证明。

<a id="hrl-sharpness"></a>

## 3. 最优指数与上界、确率的区别〔hrl-sharpness〕

### H-S1. 完整局部图像上的最大 Hölder 指数是 $1/2$

取 $w_t=((0,0),(0,t))$，$0<t\leq R$，及 $w_0=0$。它们均在 $U_R$，由 (H1) 直接算得

$$
J_F(w_t)=((0,\sqrt{t/100}),(0,t/100)),
$$

$$
\|Cw_t-Cw_0\|^2=\frac t{25}+\left(\frac{49t}{50}\right)^2.
$$

因为 $\|w_t-w_0\|=t$，任何指数 $\eta>1/2$、有限常数 $L'$ 的同域 Hölder 界都要求
$\sqrt t/5\leq L't^\eta$，与 $t\downarrow0$ 矛盾。
结合 (H12)，最大指数恰为 $1/2$。对任意 $s\in S$，沿自由位置坐标平移同一构造即可在 $s$ 附近得到相同结论。

该测试也给出 $1/2$ 阶常数的渐近下界 $1/5$。在固定半径 $R$ 上，任何统一常数至少为
$\sqrt{1/25+(49/50)^2R}$。本页取 $L=1/2$，并不主张该常数最优；(H12) 已给出更小的可行常数 $0.40104$。

### H-S2. EB 幂次 $2$ 不能提升

取 $y_t=((t^2,0),0)$，$t>0$。则

$$
r_F(y_t)=t,\qquad d(y_t,S)=t^2,\qquad
y_t+F(y_t)=((t^2,0),(t,0)).
$$

最后这个输入到 $S$ 的距离为 $\sqrt{t^4+t^2}$，故充分小 $t$ 时 $y_t\in J_F(U_R)$。若在同一输出块上有
$d(y,S)\leq K r_F(y)^{2+\varepsilon}$，
$\varepsilon>0$、$K<\infty$，就必须有
$1\leq Kt^\varepsilon$，不可能。因此 $2$ 是该幂型 EB 的最大幂次；常数 $3$ 不主张最优。

### H-S3. 统一上界不等于实际精确因子

对于初值 $z^0=w_t$，$0<t\leq R$，整条轨道可精确求出：

$$
z^j=\left(
\left(0,\frac{\sqrt t}{9}(1-10^{-j})\right),
(0,100^{-j}t)\right),\qquad
z^\infty=((0,\sqrt t/9),0).
$$

因此

$$
d(z^j,S)=100^{-j}t,\qquad
\|z^j-z^\infty\|
=\left(\frac t{81}100^{-j}+t^2 10000^{-j}\right)^{1/2}.
$$

这条轨道的距离精确因子为 $1/100$，尾项的相邻比极限为 $1/10$，均快于 (H6) 的一般上界。这里只对这条显式轨道作“精确因子”陈述，不把它推广为所有初值的最优速率。Hölder 指数最优性、EB 幂次最优性与轨道最佳收敛因子是三个不同结论。

<a id="hrl-comparison"></a>

## 4. 明确证书的排除与版本限定比较〔hrl-comparison〕

### H-C1. 本页实际排除的三个二次型条件

以下结论限定在同一 $\mathcal G_R$，或保留零点附近完整图像的邻域上，使用固定有限常数。

| 证书 | 本页排除的精确不等式 |
| --- | --- |
| Q1：两点近端二次能量证书 | $\Vert J_Fw-J_F\widetilde w\Vert^2+\Vert(w-J_Fw)-(\widetilde w-J_F\widetilde w)\Vert^2\leq K\Vert w-\widetilde w\Vert^2$ |
| Q2：固定零点的近端 Lipschitz 证书 | $\Vert J_Fw-s\Vert\leq K\Vert w-s\Vert$，$s\in S$ 固定 |
| Q3：Luke–Tam 类型的两点二次 Minty 证书 | $\langle y-v,F(y)-F(v)\rangle\geq-\tau\Vert(y+F(y))-(v+F(v))\Vert^2$，$\tau\geq0$ 固定且有限 |

证明只需 H-S1 中 $w_t,w_0$。令 $y_t=J_F(w_t)$、$y_0=0$，则

$$
\|y_t\|^2=\frac t{100}+\frac{t^2}{10000},\qquad
\|F(y_t)\|^2=\frac t{100}+\frac{9801t^2}{10000}.
$$

因此 Q1 左端与输入差平方之比为
$1/(50t)+0.9802\to+\infty$，Q2 的比值至少为
$1/(10\sqrt t)\to+\infty$。又

$$
\frac{\langle y_t,F(y_t)\rangle}{\|y_t+F(y_t)\|^2}
=-\frac1{100t}+\frac{99}{10000}\longrightarrow-\infty,
$$

故 Q3 对每个有限 $\tau$ 都失败。沿自由位置坐标平移适用于任意 $s\in S$。所有测试图像点和算子值都趋于 $(s,0)$，并且全部在相同完整输入图像块中。

这些计算没有排除删去测试点的薄图像块、允许状态依赖模量的条件、其他度量或预条件、其他步长、其他动能，亦没有排除一切广义单调性或一切 Hamilton 收敛理论。关于二次证书的结论仅是 Q1–Q3 的失败。

### H-C2. Luke–Tam 的精确版本

来源：D. Russell Luke、Matthew K. Tam，*Generalized Monotonicity and the Proximal Point Algorithm*，*Mathematics of Operations Research*，**Articles in Advance，2025-11-21 发布，pp. 1–13**，DOI [10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863)；本页核对的原文是 [出版社 PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863)，读取日期 2026-10-11。

该版 Definition 2、式 (10) 定义了上述 Q3 类型的 submonotonicity；Proposition 3 给出对应二次能量形式；Proposition 4（*Resolvents of Submonotone Mappings*）在其受限图像和 Minty 输入域上，对 $\tau<1/2$ 给出反射预解式 Lipschitz 常数 $\sqrt{1+4\tau}$ 的等价描述。

H-C1 在同一完整局部图像上排除了每个有限 $\tau$ 的 Q3，因而也排除了 Proposition 4 所比较的这一证书在该图像块上的直接适用。这里不把 Proposition 4 说成“所有非单调 PPA 都必须满足 Lipschitz”，也不把本例视为对该论文所有定理或其他局部化的否定。

### H-C3. Maddison 等的精确版本

来源：Chris J. Maddison、Daniel Paulin、Yee Whye Teh、Brendan O'Donoghue、Arnaud Doucet，*Hamiltonian Descent Methods*，**arXiv:1809.05042v1**，提交日期 2018-09-13，PDF 题页日期 2018-09-14；固定版本链接 [摘要](https://arxiv.org/abs/1809.05042v1)、[PDF](https://arxiv.org/pdf/1809.05042v1)，读取日期 2026-10-11。

该版 §3.1 的式 (33) 为全隐式 Hamilton 更新；式 (34) 给出相应极小化形式。本文 (H2) 对应其步长 $\epsilon=1$、阻尼参数 $\gamma_{\rm M}=99$。符号 $\gamma_{\rm M}$ 是该文的阻尼，不是本页 RL 指数 $\gamma=1/2$。

该版隐式收敛结果是 **Proposition 3.2**，不是 Lemma 3.1。它使用 Assumptions A、B；其中 A.1 要求唯一最小点、A.3 要求阻尼在 $(0,1)$，B.1 的式 (35) 要求存在统一有限常数 $C_{f,k}$ 使

$$
|\langle\nabla f(x),\nabla k(p)\rangle|
\leq C_{f,k}\bigl(f(x)-f(x^\star)+k(p)\bigr).
$$

Proposition 3.2 还规定相应步长范围，并以零初始动量给出目标值界。本页不把该命题改写成一般状态轨道收敛定理。

本例中 $f$ 的最小点为整条直线，因此 A.1 不满足；$\Gamma=99$ 也不满足 A.3。另一个独立的不适用原因是 B.1 在任意原点邻域都失败：取 $x=p=(t,0)$，$t>0$，有

$$
\frac{|\langle\nabla f(x),\nabla k(p)\rangle|}
{f(x)-\min f+k(p)}
=\frac t{(4/3)t^{3/2}}
=\frac3{4\sqrt t}\longrightarrow+\infty.
$$

因此不能直接用该固定版本的 Proposition 3.2 推出命题 H。它的隐式更新形式与本例一致，并不意味着其收敛假设满足；本页也没有证明该文的其他论证、其他参数选择或后续研究无法处理此类实例。

### H-C4. 非新颖性边界

本页认证的是可重建的具体实例及完整有限差分证明、指数结论和 Q1–Q3 的条件分离。没有完成穷尽文献检索、优先权比对或与所有 Hamilton/PPA 收敛框架的蕴含关系比较，故不以文献条件不适用作为“实例首次提出”“结论首次成立”或“理论整体严格强于既有理论”的证据。
