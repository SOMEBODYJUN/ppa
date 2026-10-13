# 非精确 PPA 的可计算几何余量与完整接受关系

本页 C275-v1 固定原算子，研究由真实图值和方程缺陷定义的非精确近端迭代。证明不使用精确近端解的误差，也不在算法中查询零集距离。经典重叠与公开优先权在[研究入口](README.md)中分开评判。

<a id="igs-object"></a>
## 1. 对象和完整接受关系

令 $X=\mathbb R^n$，$F:X\rightrightarrows X$，$\lambda>0$，完整零集 $S=\operatorname{zer}F$ 非空闭。记 $d(x)=d(x,S)$、$r_F(y)=\inf_{w\in F(y)}\|w\|$，空纤维残差为 $+\infty$。取开集 $U\subset X$、$R,\rho,\bar t>0$，$U_R=\{x\in U:d(x)\le R\}$。固定明定图块 $\mathcal G\subset\operatorname{gph}F$，包含 $S\times\{0\}$。全图版本取 $\mathcal G=\operatorname{gph}F$。

取有限非减函数 $\omega:[0,\rho]\to[0,\infty)$、$\psi:[0,\bar t]\to[0,\infty)$，在零处连续且为零。定义

\[
B(t)=\frac{t+\omega(t)}2,\quad
Q(u)=\inf\{t\in[0,\rho]:u\le B(t)\}.
\tag{IG1}
\]

取 $0<\bar u\le\min\{\lambda\bar t,B(\rho)\}$，只在 $u\in[0,\bar u]$ 使用 $Q$。它是已知反射模的标量逆尺度，不是到未知零集的距离。$Q$ 有限非减，$Q(0)=0$，$Q(u)>0$ 对 $u>0$ 成立，并且 $Q(u)\to0$ 当 $u\downarrow0$。后两点分别由 $B$ 在零处连续和对每个 $t>0$ 有 $B(t)\ge t/2>0$ 得到。允许 $B$ 在正点跳跃，下面不要求逆的下确界达到。

每个输入 $x$，内层返回真实图对 $(y,w)\in\mathcal G$，计算

\[
e=x-y-\lambda w,\quad E=\|e\|,\quad u=\lambda\|w\|.
\tag{IG2}
\]

给定 $0<\theta<1$、$\kappa_0<\kappa<1$，完整接受规则为

\[
\boxed{u\le\bar u,\qquad
E\le\min\left\{\theta Q(u),\ Q(u)-\frac{\psi(u/\lambda)}\kappa\right\}.}
\tag{IG3}
\]

下一物理点是 $y$，所有满足 IG2–3 的真实图对投影成关系 $\mathcal A(x)$。不选最小范数图值，不选连续分支；对于全图版本，它保留所有通过同一规则的输出。$\psi(\|w\|)$ 只是可计算的上界证书，真实残差始终为完整 $r_F$。

<a id="igs-assumptions"></a>
## 2. 共同条件

假设以下合取成立。

1. **零锚图几何**：对每个 $(y,w)\in\mathcal G$ 和每个 $p\in S$，只要 $\|y+\lambda w-p\|\le\rho$，就有
   \[
   \|y-\lambda w-p\|\le\omega(\|y+\lambda w-p\|).
   \tag{IG4}
   \]
   它只需零锚比较；完整全对 RL 是充分条件。它比只检验旧精确输出的 C249-G2 强，不能由原 G2 自动搬来。
2. **精确种子覆盖**：每个 $x\in U_R$ 有至少一对 $(y,w)\in\mathcal G$ 使 $x=y+\lambda w$。不要求在 $x-e$ 另调用覆盖。
3. **真实输出 EB**：每个 $y\in\pi_X\mathcal G$，若 $r_F(y)\le\bar t$，则 $d(y)\le\psi(r_F(y))$。它须覆盖尚未证明留域的候选输出。
4. **窗口与兼容**：
   \[
   B(R)\le\bar u,\qquad R+\theta Q(\bar u)\le\rho,
   \qquad \psi(u/\lambda)\le\kappa_0Q(u)\quad(0\le u\le\bar u),
   \quad0<\kappa_0<1.
   \tag{IG5}
   \]
   第一个评价 $B(R)$ 要求 $R\le\rho$，也由第二式保证。旧 RLEB 的前向证书
   $\psi(\min\{\bar u,B(t)\}/\lambda)\le\kappa_0t$ 对全部 $t\in[0,\rho]$ 成立，足以给出 IG5 的逆尺度式：对所有 $u\le B(t)$ 取下确界。没有把 $u\le B(Q(u))$ 当成恒真。

令

\[
\widehat B(t)=\min\{\bar u,B(t)\},\quad
H(t)=\widehat B\!\left(\min\left\{\rho,\frac{t}{1-\theta}\right\}\right)
       +\frac{\theta t}{1-\theta},\quad
\Theta(t)=\sum_{j\ge0}H(\kappa^jt).
\tag{IG6}
\]

要求 $\Theta(R)<\infty$。充分条件是 $\int_0^\rho\omega(t)\,dt/t<\infty$：对足够小的几何采样，线性项可和，非减模的采样和与该积分比较；截断部分只涉及有限项。

<a id="igs-theorem"></a>
## 3. C275-v1 · 全接受输出的有限长度

**定理。** 在上述条件下，$\mathcal A(x)\ne\varnothing$ 对每个 $x\in U_R$ 成立。若 $x^0\in U_R$ 且

\[
\Theta(d_0)<d(x^0,X\setminus U),\qquad d_0=d(x^0),
\tag{IG7}
\]

则每条 $x^{k+1}\in\mathcal A(x^k)$ 均可无限延拓，留在 $U_R$，有有限物理长度，并趋于 $x^\infty\in S\cap U$。统一于全部接受输出和图值，

\[
d(x^k)\le\kappa^kd_0,\quad
\|x^{k+1}-x^k\|\le H(\kappa^kd_0),\quad
\sum_{j\ge k}\|x^{j+1}-x^j\|\le\Theta(d(x^k)).
\tag{IG8}
\]

每个零距离输入恰有输出自身。更具体地，每个合法转移都有事后证书

\[
0\le Q(u)-E\le d(x),\qquad
d(y)\le\psi(r_F(y))\le\psi(\|w\|)
\le\kappa[Q(u)-E].
\tag{IG9}
\]

**证明。** 任取合法输入与任意接受对，取同一个 $p\in P_S(x)$。有限维闭非空 $S$ 保证最近点达到。接受上限和窗口先给

\[
\tau=\|y+\lambda w-p\|=\|x-e-p\|\le d(x)+E
\le R+\theta Q(\bar u)\le\rho.
\]

所以实际候选点可用 IG4，未先假设 $y\in U$。由两个向量差等于 $2\lambda w$，

\[
u\le B(\tau)\le B(d(x)+E),\qquad Q(u)\le d(x)+E.
\tag{IG10}
\]

IG3 的两部分分别给

\[
(1-\theta)Q(u)\le Q(u)-E\le d(x),\qquad
\psi(u/\lambda)\le\kappa[Q(u)-E]\le\kappa d(x).
\tag{IG11}
\]

真实残差方向为 $r_F(y)\le\|w\|\le\bar u/\lambda\le\bar t$，故 EB 合法，给 IG9 和距离收缩。另有 $E\le\theta d(x)/(1-\theta)$；IG10、$u\le\bar u$ 及已证 $d+E\le\rho$ 给 IG6 的核步上界，因而 $\|x-y\|\le u+E\le H(d(x))$。$d=0$ 时 IG11 强制 $Q(u)=E=0$，逆模在正点为正，故 $u=0,y=x$。

为证非空，先取精确种子 $x=y+\lambda w$。IG4 在最近锚处给 $u\le B(d(x))\le B(R)\le\bar u$，所以帽条件不是预设。IG5 给 $Q(u)-\psi(u/\lambda)/\kappa\ge(1-\kappa_0/\kappa)Q(u)\ge0$，精确种子 $E=0$ 通过规则。

逐有限前缀归纳：已到 $x^k\in U_R$，一步界给下一距离不超过 $\kappa^{k+1}d_0$，并且

\[
\|x^{k+1}-x^0\|\le\sum_{j=0}^kH(\kappa^jd_0)
\le\Theta(d_0)<d(x^0,X\setminus U).
\]

新点仍在 $U_R$，覆盖可用于下一步。可和位移使轨道 Cauchy；完备性、$S$ 闭及距离趋零给极限在 $S$，严格预算还给极限在 $U$。从任意指数求尾和得到 IG8。全程未调用精确解误差、最小残差选择或单支。□

<a id="igs-forcing"></a>
## 4. 简单误差预算与幂次

本段保留图几何、精确种子、真实 EB 及帽域，改用下面的兼容和窗口。一个便于使用的特例接受 $u\le\bar u,E\le\phi(u)$，其中 $\phi$ 有限非减、零处连续且为零。对全部 $0\le t\le\rho$，若同窗（取 $\vartheta\ge0$）

\[
\psi(\widehat B(t)/\lambda)\le\kappa_0t,\quad
\phi(\widehat B(t))\le\vartheta t,\quad
\kappa_0+\vartheta<1,\quad R+\phi(\bar u)\le\rho,
\tag{IG12}
\]

则 $E\le\vartheta(d+E)$ 给 $E\le\vartheta d/(1-\vartheta)$，并给距离因子 $\kappa=\kappa_0/(1-\vartheta)$。IG6 换 $\theta=\vartheta$ 后，同一留域证明适用。

取 $\eta\ge0$ 和 $\phi(u)=\eta\psi(u/\lambda)$，便有 $\vartheta=\eta\kappa_0$ 和

\[
\|x-y-\lambda w\|\le\eta\psi(\|w\|),\qquad
\kappa=\frac{\kappa_0}{1-\eta\kappa_0}<1
\quad\text{当 }\kappa_0(1+\eta)<1.
\tag{IG13}
\]

在共同帽与窗口上它是 IG3 的特例，取 $\theta=\eta\kappa_0$：原误差不超过 $\eta\kappa_0Q(u)$，而 IG3 第二预算至少也是此数。$\eta=0$ 的精确版本可直接用 IG12，不需要 IG3 中的严格 $\theta>0$。

若 $0<\gamma\le1$、$L\ge0$、$c>0$、$p,q>0$、$a\ge0$，取 $\omega(t)=Lt^\gamma,\psi(r)=cr^p,\phi(u)=a u^q$，令

\[
\kappa_0(\rho)=\frac{c}{2^p\lambda^p}\rho^{\gamma p-1}
 (\rho^{1-\gamma}+L)^p,\qquad
\vartheta(\rho)=\frac{a}{2^q}\rho^{\gamma q-1}
 (\rho^{1-\gamma}+L)^q.
\tag{IG14}
\]

$\gamma p\ge1,\gamma q\ge1$ 及两系数之和小于1是充分门；帽、种子与残差评价域仍要核。**误差预算的幂 $q$ 与真 EB 幂 $p$ 分开。** 在 $\gamma p>1$ 时，直接使用 EB 幂可能要求超过必要的内层精度；当 $0<\gamma<1,L>0$ 时，IG3 可利用 $Q(u)\asymp u^{1/\gamma}$ 给更宽预算；$L=0$ 时则 $Q(u)=2u$（在所用域内）。[C276](sharp_precision_frontier.md#isp-frontier)仅对其明确完整模型认证锐必要性，不把 IG14 判为每个算子的必要条件。

<a id="igs-implementation"></a>
## 5. 可实施性和比较边界

IG3 只用真实图见证、已认证的标量模、向量范数及残差帽。IG9 揭示它的目的：比较输入距离的可计算下界 $Q(u)-E$ 与输出距离的可计算上界 $\psi(\|w\|)$。模和局部管仍需先认证，本定理不承诺自动发现未知盆地或最优常数。

若内层真实图对 $(y_j,w_j)\in\mathcal G$ 趋于精确种子且该种子严格在帽内，非零距离输入 $x\notin S$ 保证 $u_\ast=\lambda\|w_\ast\|>0$。由 IG5，IG3 的预算至少为 $mQ(u_j)$，其中 $m=\min\{\theta,1-\kappa_0/\kappa\}>0$。最终 $u_j\ge u_\ast/2$，所以预算至少为固定正数 $mQ(u_\ast/2)$；缺陷趋零，内层有限步接受。这不需要 $\psi$ 在正点连续或严格为正。非空接受关系本身不保证任意内层算法终止；近似图成员资格、浮点零检测及实际工作量尚非结论。

在线性模／最大单调或逆亚单调子类中，已有 PPA/HPE 理论能正面恢复大量相同轨道。普通输入缺陷可写 $y\in J(x-e)$，但这只是一条算法身份，不给非 Lipschitz 完整关系上的输出误差。物理 GPPA 的更广候选证明见[推导草案](../../candidates/inexact_rleb_forcing.md)；非单射核仍必须给物理提升，本页没有自动授予它。

复算、独立接收与逐篇先行性见[入口](README.md)。C275 是可计算停止合同及精度设计的条件定理；其短证明不是新的普遍收敛原理，公开首创尚未认证。
