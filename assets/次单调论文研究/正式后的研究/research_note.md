# RLEB–PPA 中解选择映射的最优稳定性

**研究推导稿｜2026-09-18**

起点：用户提供的论文 *Nonlinear Generalized Monotonicity and Error Bounds for Proximal Point Convergence at Multivalued Graph Junctions* 的完整 TeX 源码，特别是正文 RL 条件、一步估计、局部收敛定理及平方根接缝例子。

**状态。** 下文给出本轮推导的完整数学论证及可复核构造，不把数值测试当作证明。与原稿相比，所研究的对象是新增的：初值到最终解的映射。全球文献优先权尚未确认；附带的 Codex 任务用于独立证伪和定理级优先权核查。

## 0. 结果概览和精确边界

记 $T=J_{\lambda F}$，$\Pi(x)=\lim_{k\to\infty}T^k x$。本稿证明：

1. 在原稿的 all-pairs Hölder RL 与统一几何距离收敛下，$\Pi$ 有统一的对数型连续模
   $$\|\Pi(x)-\Pi(y)\|\le C\left(\frac{\log\log(1/\delta)}{\log(1/\delta)}\right)^\beta,
   \qquad \beta=\frac{\gamma\log(1/q)}{\log(1/\gamma)},\quad\delta=\|x-y\|\downarrow0.$$
2. 对每一对 $0<\gamma,q<1$，存在满足原稿严格 RLEB 兼容条件的闭图二值算子，具有精确距离因子 $q$，并达到这个连续模的量级。因而一般不能推出任何正阶 Hölder 初值稳定性。
3. 若统一距离递推是 $d_{k+1}\le Kd_k^\nu$，$\nu>1$，则连续模改进为
   $$C\exp\{-c[\log(1/\delta)]^\alpha\},\qquad
   \alpha=\frac{\log\nu}{\log(\nu/\gamma)}.$$
   指数 $\alpha$ 也不能提高。一个显式半代数二值算子使每条非平凡局部轨道的**点误差**都 Q-二次收敛，但其极限解选择仍不是任何正阶 Hölder 映射。

这里 $q$ 是已经证明的统一距离因子，可以取原稿的 $\kappa$；若可独立证明更精确的距离因子，则可使用后者。例子中的精确 $q=1/4$ 不等于保守 RLEB 标量证书的极限因子 $1/2$。最优性是在给定实际统一 $q$ 与 $\gamma$ 的类别中陈述的。

本稿不声称新例子满足原稿附录的强切向反演假设；例子特意允许另一个切向退化方向。它们满足正文的 all-pairs RL、完整 proximal coverage、输出误差界和严格兼容条件。

## 1. 从有限步正则性向极限映射传递

### 定理 1：统一尾界与 Hölder 迭代的稳定性传递

设 $T$ 的一族轨道都存在并留在同一工作区域 $V$。对某个 $H,R>0$、$0<\gamma<1$，假设

$$\|Tx-Ty\|\le H\|x-y\|^\gamma\quad
(x,y\in V,\ \|x-y\|\le R).\tag{1.1}$$

设初值集合 $B\subset V$ 上每条轨道都收敛，记极限为 $\Pi(x)$。

**(a) 几何尾界。** 若存在 $M>0$、$0<\sigma<1$，使得

$$\|T^k x-\Pi(x)\|\le M\sigma^k\quad(x\in B,k\ge0),\tag{1.2}$$

则存在 $C,\delta_0>0$，使对 $x,y\in B$、$0<\delta=\|x-y\|<\delta_0$，

$$\|\Pi(x)-\Pi(y)\|\le
C\left(\frac{\log\log(1/\delta)}{\log(1/\delta)}\right)^\beta,
\qquad \beta=\frac{\log(1/\sigma)}{\log(1/\gamma)}.\tag{1.3}$$

**(b) 超几何尾界。** 若存在 $M,c_0>0$、$\nu>1$，使得

$$\|T^k x-\Pi(x)\|\le M\exp(-c_0\nu^k)\quad(x\in B,k\ge0),\tag{1.4}$$

则存在 $C,c,\delta_0>0$，使

$$\|\Pi(x)-\Pi(y)\|\le
C\exp\{-c[\log(1/\delta)]^\alpha\},
\qquad\alpha=\frac{\log\nu}{\log(\nu/\gamma)}.\tag{1.5}$$

#### 证明

取 $A\ge\max\{1,H^{1/(1-\gamma)}\}$，令 $t=\log(1/\delta)$。只要迭代比较始终处于距离 $R$ 内，由归纳

$$\|T^j x-T^j y\|\le A\delta^{\gamma^j}=Ae^{-t\gamma^j}.\tag{1.6}$$

(a) 记 $a=\log(1/\sigma)$、$b=\log(1/\gamma)$、$\beta=a/b$，取 $D=\beta+1$，并令

$$n=\left\lfloor\frac{\log[t/(D\log t)]}{b}\right\rfloor.$$

当 $t$ 足够大时 $n\ge0$，且

$$t\gamma^n\ge D\log t,\qquad
\sigma^n\le e^a\left(\frac{D\log t}{t}\right)^\beta.$$

对 $0\le j\le n$，式 (1.6) 的候选上界不超过 $At^{-D}$。当 $t$ 足够大时它小于 $R$，所以可由归纳闭合局部适用性，而不是未经检查地使用局部 Hölder 估计。于是

$$\|\Pi(x)-\Pi(y)\|
\le Ae^{-t\gamma^n}+2M\sigma^n
\le At^{-D}+2Me^aD^\beta(\log t/t)^\beta.$$

这给出 (1.3)。

(b) 取

$$n=\left\lfloor\frac{\log t}{\log(\nu/\gamma)}\right\rfloor.$$

则存在只依赖 $\gamma,\nu$ 的正数 $c_1,c_2$，使

$$t\gamma^n\ge c_1t^\alpha,\qquad\nu^n\ge c_2t^\alpha.$$

式 (1.6) 的候选上界在 $j\le n$ 时统一趋于零，同样可以闭合距离 $R$ 的局部限制。故

$$\|\Pi(x)-\Pi(y)\|
\le Ae^{-t\gamma^n}+2Me^{-c_0\nu^n}
\le Ce^{-ct^\alpha}.$$

证毕。

### 推论 1：原稿 RLEB 的直接后果

原稿的 all-pairs RL 等价于

$$\|2(Tx-Ty)-(x-y)\|\le L\|x-y\|^\gamma.$$

因此在 $\delta\le R$ 时，

$$\|Tx-Ty\|\le\tfrac12(\delta+L\delta^\gamma)
\le H\delta^\gamma,\quad H=\tfrac12(R^{1-\gamma}+L).\tag{1.7}$$

同一个常数控制步长：$\|Tx-x\|\le H d(x,S)^\gamma$。若统一有

$$d(T^k x,S)\le q^kD,$$

则

$$\|T^k x-\Pi(x)\|\le\frac{HD^\gamma}{1-q^\gamma}q^{\gamma k}.\tag{1.8}$$

在定理 1(a) 中取 $\sigma=q^\gamma$ 即得概览中的 $\beta$。

原稿的严格局部化预算可统一化：固定 $\bar x\in S\cap U$，选择足够小的初值球 $B_\varepsilon(\bar x)$，使原稿的长度预算 $\mathcal L(\varepsilon)<\operatorname{dist}(\bar x,U^c)-\varepsilon$。所有这些初值的轨道都留在共同图块中，且式 (1.8) 的常数统一。因此没有额外假设一个尚未证明存在的共同吸引域。

若 $d_{k+1}\le Kd_k^\nu$、$\nu>1$，令 $z_k=K^{1/(\nu-1)}d_k$，并将初值球缩小到 $z_0\le\vartheta<1$，则 $z_k\le\vartheta^{\nu^k}$。结合步长界和 $\nu^j\ge1+j(\nu-1)$，得到定理 1(b) 所需的统一尾界。

特别地，原稿 residual growth 的 $a<\gamma$ 情形给出 $\nu=\gamma/a>1$，故

$$\alpha=\frac{\log(\gamma/a)}{\log(1/a)}.$$

### 锚定连续性与两点连续性不同

如果 $s\in S$，则 $\Pi(s)=s$。由轨道尾界在初始步的估计，

$$\|\Pi(x)-s\|\le\|x-s\|+C d(x,S)^\gamma
\le C'\|x-s\|^\gamma.$$

这是固定解点处的 Hölder calmness。它不推出某个完整邻域上对任意两点的 Hölder 连续性。下文反例正是在距离解集任意近的非解点处破坏后者。

## 2. 原稿内部的显式半代数反例

对 $y\ge0$，定义

$$D_y(\eta)=\min\left\{2\sqrt y,\frac{\sqrt{1+4\eta_+}-1}{2}\right\},
\qquad\eta_+=\max\{\eta,0\}.$$

定义 $F:\mathbb R^3\rightrightarrows\mathbb R^3$：

$$F(\xi,\eta,y)=
\begin{cases}
\{(-2\sqrt y,-D_y(\eta),3y),\ (-2\sqrt y,-D_y(\eta),-5y)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}\tag{2.1}$$

### 定理 2：完整 proximal 公式、RL、误差界和精确速率

算子 (2.1) 的图闭且半代数，在 $y>0$ 时恰有两个值，零集为

$$S=\mathbb R^2\times\{0\}.$$

其完整单位参数 proximal 映射全局单值且为

$$T(z,p,r)=\left(z+\sqrt{|r|},\ p+\sqrt{\min\{p_+,|r|\}},\ \frac{|r|}{4}\right).\tag{2.2}$$

对任意尺度 $R>0$，完整图满足 $\mathrm{RL}(1,1/2,L_R)$，其中

$$L_R=2\sqrt2+\tfrac32\sqrt R.\tag{2.3}$$

$1/2$ 是原点附近最大 RL 指数，且 $\lim_{R\downarrow0}L_R=2\sqrt2$ 是最优渐近常数。全局输出误差界为

$$d(u,S)\le\tfrac14r_F(u)^2.\tag{2.4}$$

原稿直接兼容因子可以取

$$\kappa_R=\frac{(\sqrt R+L_R)^2}{16}
=\frac{(2\sqrt2+\frac52\sqrt R)^2}{16}\longrightarrow\frac12<1.\tag{2.5}$$

例如 $R=0.01$ 时 $\kappa_R\approx0.5922946$。实际距离因子则是精确的 $q=1/4$。

#### 完整 proximal 公式的证明

给定 proximal 输入 $(z,p,r)$，正、负分支的第三坐标方程分别是 $r=4y$ 和 $r=-4y$，因此 $y=|r|/4$，且 $r\ne0$ 时恰好一个分支允许。第一坐标给出 $\xi=z+\sqrt{|r|}$。

令 $a=|r|$。第二坐标方程是 $p=\eta-D_{a/4}(\eta)$。该函数连续、严格递增且满射，其分段表达是

- $\eta\le0$：$p=\eta$；
- $0\le\eta\le a+\sqrt a$：令 $v=(\sqrt{1+4\eta}-1)/2$，则 $\eta=v^2+v$，$p=v^2$；
- $\eta\ge a+\sqrt a$：$p=\eta-\sqrt a$。

所以唯一的逆是 $\eta=p+\sqrt{\min\{p_+,a\}}$。在 $r=0$ 时两分支合并为同一零图点。没有遗漏任何 proximal fiber。

闭图性来自两支在闭半空间上的连续性；半代数性也由显式有限运算与非负平方根给出。第一分量非零当且仅当 $y>0$，故零集如上。

#### all-pairs RL 的证明

令 $x=(z,p,r)$、$x'=(z',p',r')$、$\delta=\|x-x'\|$，并记

$$h_1=\sqrt{|r|}-\sqrt{|r'|},\qquad
h_2=\sqrt{\min\{p_+,|r|\}}-\sqrt{\min\{p'_+,|r'|\}}.$$

因为 $\min$ 对无穷范数是 1-Lipschitz，正部与绝对值也是 1-Lipschitz，故 $|h_1|,|h_2|\le\sqrt\delta$。写 $\mathcal R=2T-I$，有

$$\mathcal R x-\mathcal R x'
=(\Delta z,\Delta p,\tfrac12\Delta|r|-\Delta r)+2(h_1,h_2,0).$$

第一个向量范数不超过 $\tfrac32\delta$，第二个不超过 $2\sqrt2\sqrt\delta$。因此

$$\|\mathcal R x-\mathcal R x'\|
\le\tfrac32\delta+2\sqrt2\sqrt\delta
\le L_R\sqrt\delta\quad(\delta\le R).$$

这包含异号 $r,r'$ 的跨分支比较。等价关系立即给出原稿内积形式的 RL。

为验证最优指数与渐近常数，取 $x_t=(0,t,t)$、$x_t'=(0,t,0)$。此时

$$\|x_t-x_t'\|=t,\qquad
\|\mathcal R x_t-\mathcal R x_t'\|^2=8t+t^2/4.$$

所以任何指数大于 $1/2$ 的局部 RL 都失败，且在指数 $1/2$ 时渐近常数至少 $2\sqrt2$。

#### 输出误差界和兼容性的证明

$$r_F(\xi,\eta,y)^2=4y+D_y(\eta)^2+9y^2\ge4y.$$

这证明 (2.4)。在 $\eta\le0$、$y\downarrow0$ 时比值 $y/r_F^2\to1/4$，故系数渐近最优。代入原稿的 $\psi(t)=t^2/4$ 及步长界得到 (2.5)。由于 $T$ 全局定义，可在 $U=\mathbb R^3$ 使用原稿定理，局部化预算不存在出界障碍。

#### 精确法向速率与统一尾界

对初值 $(z_0,p_0,r_0)$，令 $a_0=|r_0|$。则

$$a_k=4^{-k}a_0,\qquad
z_k=z_0+2\sqrt{a_0}(1-2^{-k}),$$

且 $p_k$ 单调不减，每步增量位于 $[0,\sqrt{a_k}]$。于是 $p_k$ 收敛，并且在 $k\ge1$ 时

$$\|T^k x-\Pi(x)\|\le2\sqrt2\sqrt{a_0}\,2^{-k}+a_0\,4^{-k}.\tag{2.6}$$

对 $r_0\ge0$，(2.6) 从 $k=0$ 起成立；对 $r_0<0$，初始点的总长度可用 $2\sqrt2\sqrt{a_0}+\tfrac32a_0$ 控制。证明是把切向增量范数界 $\sqrt2\sqrt{a_k}$ 求和，再把单调法向变化求和。

## 3. 初值到极限解的精确劣化

固定任意 $0<r_0<1$，比较

$$x_0=(0,0,r_0),\qquad x_\varepsilon=(0,\varepsilon,r_0),\quad\varepsilon>0.$$

两条轨道的第一、第三坐标完全相同。第一条轨道第二坐标恒为零；第二条满足

$$p_{k+1}=p_k+\sqrt{\min\{p_k,r_k\}},\quad
p_0=\varepsilon,\quad r_k=4^{-k}r_0.\tag{3.1}$$

### 定理 3：最优的对数–对数连续模

存在依赖 $r_0$ 的 $c,C,\varepsilon_0>0$，使

$$c\frac{\log\log(1/\varepsilon)}{\log(1/\varepsilon)}
\le\|\Pi(x_\varepsilon)-\Pi(x_0)\|
\le C\frac{\log\log(1/\varepsilon)}{\log(1/\varepsilon)}
\quad(0<\varepsilon<\varepsilon_0).\tag{3.2}$$

特别地，对所有 $\theta>0$，

$$\frac{\|\Pi(x_\varepsilon)-\Pi(x_0)\|}{\|x_\varepsilon-x_0\|^\theta}\longrightarrow+\infty.$$

#### 证明：首次切换时刻

令 $t=\log(1/\varepsilon)$，定义

$$N=\min\{k:p_k\ge r_k\}.$$

这个时刻有限：若永不发生，则 $p_k\ge\varepsilon>0$，而 $r_k\to0$，矛盾。并且 $N\to\infty$ 当 $\varepsilon\downarrow0$，由每个有限次迭代对初值的连续性可知。

在 $k<N$ 时，$p_k<r_k\le r_0<1$，因此

$$\sqrt{p_k}\le p_{k+1}\le2\sqrt{p_k}.$$

迭代取对数，得到对所有 $0\le k\le N$ 一致成立的

$$e^{-t2^{-k}}\le p_k\le4e^{-t2^{-k}}.\tag{3.3}$$

注意上界常数不随 $k,N,\varepsilon$ 增长。

由 $p_N\ge r_N$ 及 $p_{N-1}<r_{N-1}$，结合 (3.3)，得到

$$t2^{-N}\le N\log4+O(1),\qquad
t2^{-(N-1)}\ge(N-1)\log4+O(1).$$

因此 $t2^{-N}=\Theta(N)$，继而

$$N=\frac{\log t-\log\log t}{\log2}+O(1),\qquad
2^{-N}=\Theta(\log t/t).\tag{3.4}$$

从 $N$ 起一直处于饱和段，因为 $p_k$ 不减而 $r_k$ 递减。于是有**精确公式**

$$p_\infty=p_N+\sum_{k=N}^\infty\sqrt{r_k}
=p_N+2\sqrt{r_0}\,2^{-N}.\tag{3.5}$$

另外

$$p_N\le r_{N-1}+\sqrt{r_{N-1}}\le C_0\sqrt{r_N}.$$

式 (3.5) 同时给出下界 $p_\infty\ge2\sqrt{r_N}$ 和同阶上界，所以 $p_\infty=\Theta(2^{-N})$。再用 (3.4) 即得 (3.2)。两条轨道的其余极限坐标相同，故极限差的欧氏范数就是 $p_\infty$。

由 $\gamma=1/2,q=1/4$，定理 1 的 $\beta=1$，上、下界完全匹配。尤其不能删除分子中的 $\log\log$，得到统一的 $O(1/\log)$ 界。这里的 $\Theta$ 不主张存在归一化比值极限；离散切换时刻允许有界振荡。

### 任意 $\gamma,q$ 的 RLEB 内部最优性

取 $A,B>0$，定义

$$T(z,p,r)=\left(z+A|r|^\gamma,\ p+B\min\{p_+,|r|\}^\gamma,\ q|r|\right).\tag{3.6}$$

令 $h(s)=s+Bs^\gamma$，并设 $\tau_a$ 是严格递增满射

$$p\mapsto p+B\min\{p_+,a\}^\gamma$$

的逆，即

$$\tau_a(\eta)=
\begin{cases}
\eta,&\eta\le0,\\
h^{-1}(\eta),&0<\eta<h(a),\\
\eta-Ba^\gamma,&\eta\ge h(a).
\end{cases}$$

对 $y\ge0$、$a=y/q$，定义两值

$$F(\xi,\eta,y)=\{(-Aa^\gamma,\tau_a(\eta)-\eta,a-y),
(-Aa^\gamma,\tau_a(\eta)-\eta,-a-y)\},\tag{3.7}$$

并在 $y<0$ 令其为空。它是闭图二值算子，完整 resolvent 就是 (3.6)，零集仍为平面。若 $\gamma$ 为有理数，则它是半代数算子。

同样的 all-pairs 估计给出

$$L_R=2\sqrt{A^2+B^2}+(1+2q)R^{1-\gamma},$$

而

$$r_F(u)\ge A(y/q)^\gamma,\qquad
\psi(t)=q(t/A)^{1/\gamma}.$$

原稿兼容商的极限是

$$\kappa_*=q\left(1+(B/A)^2\right)^{1/(2\gamma)}.$$

对任何给定 $\gamma,q$，都可选

$$0<B/A<\sqrt{q^{-2\gamma}-1}$$

使 $\kappa_*<1$。因此该族真正位于严格 RLEB 兼容区域内部，而非仅在临界边界。

对 $p_0=\varepsilon$ 的首次切换时刻 $N$，取 $t=\log(1/\varepsilon)$。未饱和时

$$\log p_{k+1}=\gamma\log p_k+\log(B+p_k^{1-\gamma}).$$

最后一项在固定有界区间内，故

$$\log p_k=-\gamma^k t+O(1)\quad(0\le k\le N).\tag{3.8}$$

与 $r_k=q^kr_0$ 的交叉条件给出

$$N=\frac{\log t-\log\log t}{\log(1/\gamma)}+O(1).$$

饱和后

$$p_\infty=p_N+\frac{B r_N^\gamma}{1-q^\gamma},\qquad
p_N\le r_{N-1}+B r_{N-1}^\gamma=O(r_N^\gamma).$$

从而

$$p_\infty=\Theta(r_N^\gamma)
=\Theta\left((\log t/t)^{\gamma\log(1/q)/\log(1/\gamma)}\right).$$

这证明定理 1(a) 在每个给定 $\gamma,q$ 的 RLEB 类中的量级最优性。

## 4. Q-二次点收敛仍不能保证 Hölder 解选择

令

$$\widetilde D_y(\eta)=\min\left\{y^{1/4},\frac{\sqrt{1+4\eta_+}-1}{2}\right\},$$

并定义闭图半代数二值算子

$$\widetilde F(\xi,\eta,y)=
\begin{cases}
\{(-y^{1/4},-\widetilde D_y(\eta),\sqrt y-y),
(-y^{1/4},-\widetilde D_y(\eta),-\sqrt y-y)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}\tag{4.1}$$

### 定理 4：二次收敛与根对数指数稳定性

其完整 resolvent 是

$$\widetilde T(z,p,r)=\left(z+\sqrt{|r|},\ p+\sqrt{\min\{p_+,|r|\}},\ r^2\right).\tag{4.2}$$

在任意固定 $|r|\le R_0<1$ 的输入 collar 上，它满足 $\gamma=1/2$ 的 all-pairs RL；全局输出误差界为

$$d(u,S)\le r_{\widetilde F}(u)^4.\tag{4.3}$$

原稿的直接兼容 map 为 $O(d^2)$，所以属于严格超临界误差界匹配区域。对 $0<|r_0|<1$，每条轨道的点误差 $e_k=\|\widetilde T^k x-\widetilde\Pi(x)\|$ 均具有确切的 Q-二次量级：存在正数 $c,C$，使

$$ce_k^2\le e_{k+1}\le Ce_k^2\quad(k\ \text{充分大}).\tag{4.4}$$

然而对固定 $0<r_0<1$、$x_\varepsilon=(0,\varepsilon,r_0)$、$x_0=(0,0,r_0)$，存在 $c,C>0$，使

$$\exp(-C\sqrt{\log(1/\varepsilon)})
\le\|\widetilde\Pi(x_\varepsilon)-\widetilde\Pi(x_0)\|
\le\exp(-c\sqrt{\log(1/\varepsilon)}).\tag{4.5}$$

所以这个二次点收敛的半代数 PPA 仍不具有任何正阶 Hölder 初值到最终解的稳定性。

#### 证明

第三坐标方程是 $r=\pm\sqrt y$，故 $y=r^2$；第二坐标反演与定理 2 相同，cap 的输入量现在是 $|r|$。这证明完整公式。

在 $|r|\le R_0$ 时，$r\mapsto2r^2-r$ 的 Lipschitz 常数不超过 $1+4R_0$，故对距离不超过 $D$ 的输入对，

$$\| (2\widetilde T-I)x-(2\widetilde T-I)x'\|
\le[2\sqrt2+(1+4R_0)\sqrt D]\sqrt{\|x-x'\|}.$$

第一分量给出 $r_{\widetilde F}(u)\ge y^{1/4}$，即 (4.3)。取 $\psi(t)=t^4$ 时，原稿直接 map

$$\psi((d+L\sqrt d)/2)=(d+L\sqrt d)^4/16=O(d^2).$$

令 $a_0=|r_0|\in(0,1)$，则从第 1 步起法向坐标为 $r_k=a_0^{2^k}>0$。第一切向坐标的尾部至少为 $\sqrt{r_k}$；两切向增量范数至多为 $\sqrt2\sqrt{r_k}$，且法向变化总和为 $r_k$。用

$$\sum_{j=0}^\infty r_k^{2^j/2}\le
\frac{\sqrt{r_k}}{1-\sqrt{a_0}}$$

可得 $e_k\asymp\sqrt{r_k}$，继而 $e_{k+1}\asymp r_k\asymp e_k^2$。

更精确地，当 $p_0\le0$ 时第二切向坐标恒定，$e_k\sim\sqrt{r_k}$，故 $e_{k+1}/e_k^2\to1$。当 $p_0>0$ 时最终进入并留在饱和段，两个切向尾部相同，故 $e_k\sim\sqrt2\sqrt{r_k}$，从而 $e_{k+1}/e_k^2\to1/\sqrt2$。

现在考虑初值差 $\varepsilon$。未饱和时仍有

$$\log p_k=-2^{-k}t+O(1),\quad t=\log(1/\varepsilon).$$

在上述正初值比较中，令 $A_0=-\log r_0>0$，阈值变成 $r_k=\exp(-A_0 2^k)$。由 $p_N\ge r_N$、$p_{N-1}<r_{N-1}$，

$$N=\frac{\log t}{\log4}+O(1).$$

所以 $t2^{-N}=\Theta(\sqrt t)$、$2^N=\Theta(\sqrt t)$。由于

$$p_\infty=p_N+\sum_{k=N}^\infty\sqrt{r_k},$$

第一项和尾部的对数都为 $-\Theta(\sqrt t)$，即 (4.5)。注意这里不能错误地套用几何法向情形的 $p_N=O(r_N^{1/2})$；超几何下降时这一般不成立。本证明分别控制 overshoot 项与饱和尾项。

### 任意超线性阶数的最优指数

更一般地，把 (3.6) 的最后一个坐标换成 $|r|^\nu$，$\nu>1$。完整算子由 (3.7) 把 $a=y/q$ 换成 $a=y^{1/\nu}$ 得到。误差界变成

$$d(u,S)\le(r_F(u)/A)^{\nu/\gamma}.$$

在固定 $|r|<R_0<1$ 上，all-pairs RL 指数仍是 $\gamma$，且原稿兼容 map 是 $O(d^\nu)$。点误差满足 $e_k\asymp r_k^\gamma$，因而具有确切的 Q-$\nu$ 量级。

对敏感初值，首次切换满足

$$\gamma^N t\asymp\nu^N,\qquad
N=\frac{\log t}{\log(\nu/\gamma)}+O(1).$$

于是

$$p_\infty=\exp[-\Theta(t^\alpha)],\qquad
\alpha=\frac{\log\nu}{\log(\nu/\gamma)}.$$

这与定理 1(b) 匹配：不能统一替换为任何更大的根对数指数 $\alpha'>\alpha$。这里的最优性是指数层面的，不主张指数前常数最优。若 $\gamma,\nu$ 为有理数，则该族也是半代数的。

## 5. 两个结构性推论

### 5.1 半代数有限步映射的极限不必半代数

定理 2、4 中的 $F,T$ 均为半代数，每个有限次迭代 $T^k$ 也半代数。然而极限映射在原点的任何完整邻域内都不是半代数。

证明：若该极限映射在某个完整邻域内半代数，取充分小的固定 $r_0>0$，限制到 $(0,\varepsilon,r_0)$。得到一个连续、正、趋零的半代数一元函数。半代数增长二分引理使其具有 $c\varepsilon^a+o(\varepsilon^a)$ 的首项，且 $a>0$。这与 (3.2) 或 (4.5) 对每个正幂都更慢的衰减矛盾。所用增长二分引理可见 Lee–Pham，arXiv:2004.02188v2，Lemma 2.2。

因此不能把“每一步是半代数”偷换成“迭代无穷次后的算法解选择也是半代数”。

### 5.2 一项真正恢复 Hölder 稳定性的切向条件

以下命题的证明是标准离散 Gronwall 估计；不把这一证明技巧主张为创新。它用于识别上述反例中确实缺少的结构。

设

$$T(a,r)=(a+B(a,r),qr),\quad 0\le r\le R,\quad0<q<1,$$

其中 $B(a,0)=0$，并且对某些 $C,H,\eta>0$、$0<\gamma\le1$，

$$\|B(a,r)-B(b,r)\|\le Cr^\eta\|a-b\|,$$

$$\|B(a,r)-B(a,s)\|\le H|r-s|^\gamma.$$

则轨道有限长，其极限第一坐标 $\Pi_a$ 满足

$$\|\Pi_a(a,r)-\Pi_a(b,s)\|
\le \exp\!\left(\frac{CR^\eta}{1-q^\eta}\right)
\left[\|a-b\|+\frac{H}{1-q^\gamma}|r-s|^\gamma\right].\tag{5.1}$$

证明：$\|B(a,r)\|\le Hr^\gamma$ 保证轨道收敛。两轨道第一坐标差 $u_k$ 满足

$$u_{k+1}\le(1+CR^\eta q^{\eta k})u_k+Hq^{\gamma k}|r-s|^\gamma.$$

将乘积界

$$\prod_{k\ge0}(1+CR^\eta q^{\eta k})
\le\exp(CR^\eta/(1-q^\eta))$$

与几何级数结合，再取极限即得 (5.1)。反例的 $p\mapsto\sqrt{p_+}$ 切向尖点明显不满足第一项 Lipschitz 条件。

此命题只针对明确写出的三角结构，不声称已证明一般曲面、耦合法向动力学或原稿所有 signed-Schur 图块的 Hölder 稳定性。

## 6. 文献位置与尚未确认的优先权

本轮核对的原始资料包括：

- Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, DOI 10.1287/moor.2025.0863，尤其 Theorem 2 的局部轨道收敛及全图/点态条件的差别。
- Luke–Thao–Tam, *Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings*, DOI 10.1287/moor.2017.0898，arXiv:1605.05725v2。其 almost-averaged 与 metric-subregularity 框架是需精确比较的先例。
- Luke–Thao–Tam, *Implicit Error Bounds for Picard Iterations on Hilbert Spaces*, DOI 10.1007/s10013-018-0279-x。其非扩张迭代与误差界关系可作稳定性强条件的对照；本轮读到出版社摘要，不把摘要当成完整定理排查。
- Li–Mordukhovich–Zhu, *Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods*, DOI 10.1287/moor.2024.0570，arXiv:2406.13207v1。广义误差界及超线性/二次收敛本身已有先例，不能作为本稿独立新颖性。
- Lee–Pham, *Openness, Hölder Metric Regularity, and Hölder Continuity Properties of Semialgebraic Set-Valued Maps*, DOI 10.1137/20M1331901，arXiv:2004.02188v2。这里使用其 Lemma 2.2 的标准增长二分事实。

本稿拟主张的研究贡献是：**在正文 RLEB 类内部，统一轨道收敛速度与极限解选择稳定性的最优量级关系，以及达到该界的完整闭图半代数二值 proximal 构造。** 不是一般 Picard 迭代、不动点存在性、高阶误差界、半代数增长引理或离散 Gronwall 方法本身。

这些资料的定向核对尚未发现与上述完整结果相同的定理，但不是穷尽性优先权证明。还需专门排查连续/Hölder 离散动力系统的 limit retraction、asymptotic phase、uniform limits of iterates 文献，判断定理 1 是否已有同量级表述，以及例子的 RLEB 实现与半代数二次收敛分离是否已有先例。

## 7. 数值核查与复现

`verify_research.py` 使用确定种子，对两个显式模型各作 100000 组检查，覆盖异号 proximal 输入、切向尖点和接缝：完整 graph identity、两个分支分别反演回输出、输出 EB、随机 all-pairs RL，以及直接迭代与切换后的精确几何尾和交叉核对。连续域的结论仍由以上证明保证。

初次运行的最大 graph identity 绝对误差约为 $1.91\times10^{-17}$，两个分支逆向检查的最大绝对误差约为 $1.53\times10^{-16}$；抽样没有发现 EB 或 RL 违反。完整数值保存在 JSON 和 CSV 中。

几何模型固定 $r_0=0.01$，$\varepsilon=e^{-t}$：

| $t$ | 切换时刻 $N$ | 极限解差 | 极限解差 $\times t/\log t$ |
|---:|---:|---:|---:|
| $10^2$ | 4 | 0.0144341844 | 0.313434 |
| $10^4$ | 10 | 0.000252706683 | 0.274373 |
| $10^6$ | 16 | 0.00000328791013 | 0.237987 |
| $10^{12}$ | 35 | $6.05004654\times10^{-12}$ | 0.218958 |

代码在切换前使用 $\log p$，因此无需把 $e^{-10^6}$ 存成普通浮点数。超线性模型同时报告对数极限差和遗漏正尾项的几何级数上界；这些是浮点计算，不是区间算术或形式化证书。
