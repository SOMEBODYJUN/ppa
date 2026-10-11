# 物理空间的 RLEB–GPPA：父定理、能量分支与自然模型

本页是 C245–C249-v1 的独立规范正文。有限维 Euclidean 空间、固定全域核、物理真残差和同一允许关系为共同约定。与 C208–C210 的完整核 chart 对象不同；不直接改变其身份，不宣称包含该体系全部非几何收缩实例，也不认证外部首创。

共同距离定义为 $d(x,S)=\inf_{p\in S}\|x-p\|$，
$P_S(x)=\{p\in S:\|x-p\|=d(x,S)\}$。
有限维非空闭 $S$ 保证最近点存在。固定点集为 $\operatorname{Fix}T=\{x:x\in T(x)\}$；
完整普通近端关系 $(I+\lambda F)^{-1}$ 的固定点集恰为 $F^{-1}(0)$。
父定理中的 $d(x)$ 是 $d(x,S)$ 的简记，完整真残差为 $r_F(y)=d(0,F(y))$，空值残差取 $+\infty$。
本页的 C245/C246/C247/C248/C249 分别固定自己的对象，例子更换 $F$ 时重新声明目标 $S$。

<a id="prg-object"></a>
## C245-v1 · 对象与物理父定理

- **Status**：`derived-checked`。完整证明及本轮两位独立审查覆盖实际源；外部先行性未核。


### 广义近端迭代的局部收敛


<a id="sec-rleb-gppa-main"></a>





### 近端关系与物理位移


设 $X=\mathbb R^n$，$F:X\rightrightarrows X$，$\lambda>0$，
并固定一个处处有定义的核 $v:X\to X$。广义近端关系为

\[
 J^v_{\lambda F}(x):=(v+\lambda F)^{-1}(v(x))
 =\{y:v(x)-v(y)\in\lambda F(y)\}.
\]
我们研究物理空间中的迭代 $x^{k+1}\in\mathcal J_v(x^k)$，
其中 $\mathcal J_v$ 是这一关系的允许子关系。
固定非空闭集 $S\subset F^{-1}(0)$，记
$d(x)=d(x,S)$、$r_F(y)=d(0,F(y))$。
其中到空集的距离取 $+\infty$。残差评价完整 $F$；
由算法选出的图值范数只提供其上界。

核的作用有两个方面：核增量控制算法所选图值，
而从核增量到物理位移还需要一个独立估计。
后者可以来自逆映射，也可以直接来自算法对核纤维内运动的控制。
下面的定理直接对物理闭零集作出结论，
同时把核几何与相邻物理位移分别列为可验证条件。


### 有限长度定理



**theorem · RLEB--GPPA 的局部有限长度。**


<a id="thm-rleb-gppa-physical"></a>

设 $U\subset X$ 开，$R,\bar t>0$，$0<\kappa<1$，并置
$U_R=\{x\in U:d(x)\le R\}$。
取有限非减函数

\[
 a:[0,R]\to[0,\infty),\qquad
 \omega:[0,a(R)]\to[0,\infty),\qquad
 \psi:[0,\bar t]\to[0,\infty),
\]
三者在零处连续且取值为零。
取有限函数 $h:[0,\infty)^2\to[0,\infty)$，
它对各变量均非减，在 $(0,0)$ 连续且 $h(0,0)=0$。
定义

\[
 K(t)=\frac{a(t)+\omega(a(t))}{2},\qquad
 H(t)=h(t,K(t)),\qquad
 \Theta(t)=\sum_{j=0}^{\infty}H(\kappa^jt),\quad 0\le t\le R.
\]
假设同一个允许关系 $\mathcal J_v$ 满足：


- **(G1)** 对每个 $x\in U_R$，
$\varnothing\ne\mathcal J_v(x)\subset J^v_{\lambda F}(x)$。

- **(G2)** 对每个 $x\in U_R$ 和每个 $y\in\mathcal J_v(x)$，
存在同一个 $p\in P_S(x)$，使
<a id="eq-gppa-same-anchor"></a>
\[



 \delta:=\|v(x)-v(p)\|\le a(d(x)),\qquad
 \|2v(y)-v(x)-v(p)\|\le\omega(\delta).
\]

- **(G3)** 对上述全部允许转移，有物理位移估计
<a id="eq-gppa-physical-transfer"></a>
\[



 \|y-x\|\le h\bigl(d(x),\|v(y)-v(x)\|\bigr).
\]

- **(G4)** 对每个 $y\in\mathcal J_v(U_R)$，若
$r_F(y)\le\bar t$，则 $d(y)\le\psi(r_F(y))$；并且
$K(R)/\lambda\le\bar t$。

- **(G5)** 对每个 $0<t\le R$，
$\psi(K(t)/\lambda)\le\kappa t$，且 $\Theta(R)<\infty$。

取 $x^0\in U_R$，记 $d_0=d(x^0)$，约定 $d(x,\varnothing)=+\infty$。若
<a id="eq-gppa-physical-budget"></a>
\[



 \Theta(d_0)<d(x^0,X\setminus U),
\]
则每条允许轨道均可无限延拓，全部点属于 $U_R$，具有有限长度，
并收敛到某个 $x^\infty\in S\cap U$。对所有 $k\ge0$，有
<a id="eq-gppa-physical-distance"></a>
<a id="eq-gppa-physical-tail"></a>
\[
\begin{aligned}
 d(x^k)&\le\kappa^k d_0,

\\
 \|v(x^{k+1})-v(x^k)\|&\le K(d(x^k))\le K(\kappa^k d_0),\\
 \|x^{k+1}-x^k\|&\le H(d(x^k))\le H(\kappa^k d_0),\\
 \sum_{k\ge0}\|x^{k+1}-x^k\|&\le\Theta(d_0),\\
 \|x^\infty-x^k\|&\le\Theta(d(x^k))\le\Theta(\kappa^k d_0).



\end{aligned}
\]
常数统一于全部允许选择，极限点可以随选择改变。
若 $\mathcal J_v=J^v_{\lambda F}$，结论控制完整广义近端关系的全部选择。




**证明。**

任取合法输入 $x\in U_R$ 及任意允许输出 $y$，
并取 (G2) 中同时满足两项估计的最近零点 $p$。
置

\[
 A=v(y)-v(p),\qquad B=v(x)-v(y),\qquad d=d(x).
\]
则 $A+B=v(x)-v(p)$，而
$\|A-B\|\le\omega(\|A+B\|)$。
因此
<a id="eq-gppa-kernel-one-step"></a>
\[



 \|B\|\le\frac{\|A+B\|+\|A-B\|}{2}\le K(d).
\]
平行四边形恒等式还给出
<a id="eq-gppa-kernel-energy"></a>
\[



 \|v(y)-v(p)\|^2+\|B\|^2
 \le\frac{a(d)^2+\omega(a(d))^2}{2}.
\]
这里左侧第一项是到所选核零锚的距离，不是物理距离 $d(y)$。

由 (G1)，$B/\lambda\in F(y)$。于是

\[
 r_F(y)\le\|B\|/\lambda
 \le K(d)/\lambda\le K(R)/\lambda\le\bar t.
\]
这条链先验证真残差误差界的评价域，再由 (G4)--(G5) 得到
$d(y)\le\psi(K(d)/\lambda)\le\kappa d$（$d>0$）。
(G3) 与 [对应公式](#eq-gppa-kernel-one-step) 给出 $\|y-x\|\le H(d)$。
当 $d=0$ 时，闭性给出 $x\in S$，最近锚只能是 $p=x$。
(G2) 强制 $B=0$，(G3) 再强制 $y=x$；
所以零距离输入的全部允许输出驻定，距离递推仍成立。

由 (G1) 可以构造第一步。若已构造到 $x^k\in U_R$，
上述一步估计及有限前缀归纳给出

\[
 d(x^{k+1})\le\kappa^{k+1}d_0,\qquad
 \|x^{k+1}-x^0\|\le\sum_{j=0}^kH(\kappa^jd_0)
 \le\Theta(d_0)<d(x^0,X\setminus U).
\]
因而 $x^{k+1}\in U_R$，(G1) 可以再次使用。
这证明全部有限前缀合法以及无限延拓，
而没有预先假设后继输出位于 $U$。

长度可和给出 Cauchy 性；$X$ 完备，故轨道有极限。
$d(x^k)\to0$ 和 $S$ 闭给出 $x^\infty\in S$，
同一严格预算给出 $x^\infty\in U$。
从任意 $k$ 开始重新求和即得 [对应公式](#eq-gppa-physical-tail)。
全部估计均逐输入、逐允许输出成立，故不依赖所选分支。




**corollary · 解附近的统一初值邻域。**


<a id="cor-gppa-physical-basin"></a>

在定理~[对应结果](#thm-rleb-gppa-physical) 的条件下，取 $\bar x\in S\cap U$
及有限 $b>0$，使 $B_b(\bar x)\subset U$。
存在 $0<\delta\le R$ 满足 $\delta+\Theta(\delta)<b$。
每个 $x^0\in B_\delta(\bar x)$ 的全部允许轨道均可无限延拓，
留在 $B_b(\bar x)$，并收敛到 $S\cap B_b(\bar x)$ 中一点。



**证明。**

当 $t\downarrow0$ 时，每项 $H(\kappa^jt)\to0$，
且在 $0\le t\le R$ 上由可和列 $H(\kappa^jR)$ 控制。
级数的控制收敛给出 $\Theta(t)\to0$，故可选上述 $\delta$。
对 $x^0\in B_\delta(\bar x)$，有 $d_0\le\|x^0-\bar x\|<\delta$，且
$d(x^0,X\setminus U)\ge b-\|x^0-\bar x\|>b-\delta>\Theta(d_0)$。
应用主定理，全部轨道及极限到 $\bar x$ 的距离均小于
$\delta+\Theta(\delta)<b$。




**说明 · 提升条件的两种来源。**

若在实际输入及其全部输出之间有逆模
$\|x-y\|\le\eta(\|v(x)-v(y)\|)$，则可取 $h(t,s)=\eta(s)$。
必须在证明输出留域之前认证这些点对；
只在 $U\times U$ 上有逆估计并不足以证明新输出留在 $U$。
对于非单射核，可以取 $h(t,s)=\eta(s)+\zeta(t)$，
其中 $\zeta$ 控制核不可见方向的运动，$\zeta(0)=0$。
定理只需要相邻允许转移上的位移界，不要求全域逆映射存在。




**corollary · 可检验的长度条件。**


<a id="cor-gppa-dini-length"></a>

在主定理其他条件下，$\Theta(R)<\infty$ 等价于

\[
 \int_0^R H(t)\,\frac{dt}{t}<\infty.
\]
若 $a(t)\le At^\beta$、$\omega(s)\le Ls^\gamma$，并且
$h(t,s)\le Ms^\theta+Nt^\delta$，其中
$A>0$，$L,M,N\ge0$，$\beta,\delta>0$，$0<\gamma,\theta\le1$，
则长度条件成立，且

\[
 \Theta(t)\le\frac{M}{2^\theta}
 \left(\frac{A^\theta t^{\beta\theta}}{1-\kappa^{\beta\theta}}
 +\frac{L^\theta A^{\gamma\theta}t^{\beta\gamma\theta}}
              {1-\kappa^{\beta\gamma\theta}}\right)
 +\frac{Nt^\delta}{1-\kappa^\delta}.
\]




**证明。**

由 $H$ 非减，对每个 $j\ge0$ 有

\[
 \log(1/\kappa)H(\kappa^{j+1}R)
 \le\int_{\kappa^{j+1}R}^{\kappa^jR}\frac{H(t)}t\,dt
 \le\log(1/\kappa)H(\kappa^jR).
\]
求和得到等价性。幂模情形利用
$(r+s)^\theta\le r^\theta+s^\theta$，再分别求几何级数。




**说明 · 非单射核与物理位移。**


<a id="ex-gppa-null-fiber"></a>

在 $\mathbb R^2$ 上取 $v(t,s)=(t,0)$、$\lambda=1$。
若 $F(t,s)=(t,s)$，则完整输出唯一，
$J_F^v(t,s)=(t/2,0)$，零集为 $S=\{0\}$。
取 $a(t)=t$、$\omega=0$、$h(t,s)=t+s$、$\psi(t)=t$，
有 $K(t)=t/2$、$H(t)=3t/2$、$\kappa=1/2$、$\Theta(t)=3t$。
这些条件对完整关系成立；例如 $R=1$、$\bar t=1$、$U=\mathbb R^2$。
位移界来自
$\|(t,s)-(t/2,0)\|\le|t|/2+|s|\le K(d)+d$。
核不可见的第二坐标在第一步被消除。
这给出核全域非单射而完整物理迭代仍收敛的例子。

若改取 $F=v$，目标零集相应改为 $S=\{0\}\times\mathbb R$，
完整输出变为 $\{(t/2,q):q\in\mathbb R\}$。
此时 $d((t/2,q),S)=r_F(t/2,q)=|t|/2$，
物理真残差误差界和核反射估计仍成立，
但不存在上述有限位移控制。轨道
$x^k=(2^{-k},(-1)^k)$ 合法而不收敛。
因此核不可见方向的控制不能由真误差界代替。
此外，完整关系下若 $p\in S\cap U$、$q\in S$ 且 $v(p)=v(q)$，
则 $q\in J^v_{\lambda F}(p)$；(G2)--(G3) 在零距离输入处强制 $q=p$。
故当 $S\subset U$ 时，完整关系的条件要求 $v|_S$ 单射，
但并不要求 $v$ 在全空间单射。



<a id="prg-ppa"></a>
### C02-v3 的准确特例

令 v=Id、a(t)=t、ω(t)=Lt^γ、h(t,s)=s。前向界与物理提升自动成立，同一最近零锚反射条件正是 C02-v3 的B2；G1/G4/G5分别为B1/B3/B4，Θ(R)<∞ 自动由两项几何级数得到，Θ(t)=½[t/(1−κ)+Lt^γ/(1−κ^γ)]。因此不是另加假设后得到的旧结果，而是逐条件原样恢复。证明用 ||x−p||²−||2y−x−p||²=4⟨y−p,x−y⟩，所有允许输出和严格预算保持。C02-v3 独立身份仍见 [真残差允许关系正文](true_residual_selection_rleb.md#trs-theorem)。

<a id="prg-energy"></a>
## C246-v1 · 一般核能量分支

- **Status**：`derived-checked`。它保留 G1–G4、物理预算与 ΣH(κʲR) 可和性，替换直接兼容。


**corollary · 核能量供应的物理收缩。**


<a id="cor-gppa-physical-energy"></a>

沿用定理~[对应结果](#thm-rleb-gppa-physical) 的对象和 (G1)--(G4)，
记 $M_0=\psi(\bar t)$，并取有限非负函数
$\rho,g:[0,M_0]\to[0,\infty)$，$\rho(0)=g(0)=0$。
对每个允许转移 $x\mapsto y$，要求 (G2) 中可以选择同一个最近零锚
$p$，既满足该项的两条估计，又满足

\[
 \rho(d(y))\le\|v(y)-v(p)\|.
\]
对每个 $y\in\mathcal J_v(U_R)$，当 $r_F(y)\le\bar t$ 时，另要求
$g(d(y))\le r_F(y)$。
将 (G5) 的直接兼容条件替换为下列标量条件：
对每个 $0<t\le R$ 和每个 $0\le q\le M_0$，
<a id="eq-gppa-energy-scalar-gate"></a>
\[



 \rho(q)^2+\lambda^2g(q)^2
 \le\frac{a(t)^2+\omega(a(t))^2}{2}
 \quad\Longrightarrow\quad q\le\kappa t.
\]
仍保留 $\Theta(R)<\infty$。
则满足严格物理初值预算的全部允许轨道具有主定理的全部结论。




**证明。**

核一步估计仍先给
$r_F(y)\le\|v(x)-v(y)\|/\lambda\le K(R)/\lambda\le\bar t$。
所以 (G4) 给出 $0\le d(y)\le M_0$，而残差下界给出
$\lambda g(d(y))\le\|v(x)-v(y)\|$。
与同一最近零锚的下界及核平行四边形估计合并，得到

\[
 \rho(d(y))^2+\lambda^2g(d(y))^2
 \le\|v(y)-v(p)\|^2+\|v(x)-v(y)\|^2
 \le\frac{a(d(x))^2+\omega(a(d(x)))^2}{2}.
\]
当 $d(x)>0$ 时，[对应公式](#eq-gppa-energy-scalar-gate) 给出
$d(y)\le\kappa d(x)$。当 $d(x)=0$ 时，
(G2)--(G3) 已强制 $y=x$。
物理步长仍至多 $H(d(x))$，故主定理的有限前缀留域、无限延拓与尾和证明
逐项适用。这里不需要 $\rho$ 或 $g$ 可逆，也没有越过其输出评价域。





<a id="prg-bregman"></a>
## C247-v1 · 四次 Bregman 核的完整自然模型

- **Status**：`derived-checked`。完整物理最优性和全部轨道直接证明；未认证这个初等例的最早来源。


### Bregman 近端中的核平坦性与物理速率


<a id="subsec-gppa-bregman-quartic"></a>


Bregman 近端法为非线性核提供了一个直接的优化解释。
对可微凸函数 $h$，记

\[
 D_h(y,x)=h(y)-h(x)-\langle\nabla h(x),y-x\rangle.
\]
对于适当下半连续凸函数 $f$，最小化 $\lambda f(y)+D_h(y,x)$ 的最优性条件为
$\nabla h(x)\in\nabla h(y)+\lambda\partial f(y)$
（所用文献见本页末的一手来源接口）。
下面的二次目标已足以说明，核在解附近的平坦性能够改变物理迭代的速率。

在 $\mathbb R^2$ 上取

\[
 f(t,s)=\frac12t^2,\qquad
 h(t,s)=\frac14t^4+\frac12s^2,
 \qquad v(t,s)=\nabla h(t,s)=(t^3,s).
\]
目标的解集是直线 $S=\{0\}\times\mathbb R$。
核 $v$ 是全空间上的非线性同胚，但其逆在 $S$ 附近不局部 Lipschitz。
完整 Bregman 近端步满足
<a id="eq-gppa-bregman-cubic-step"></a>
\[



 t_k^3=t_{k+1}^3+\lambda t_{k+1},\qquad
 s_{k+1}=s_k.
\]
因为 $u\mapsto u^3+\lambda u$ 连续、严格递增且满射，
这一完整近端映射对每个输入都存在且唯一。


**proposition。**


<a id="prop-gppa-bregman-cubic"></a>

对任意 $\lambda>0$ 与任意初值 $(t_0,s_0)$，
迭代 [对应公式](#eq-gppa-bregman-cubic-step) 收敛到 $(0,s_0)$，
物理轨道的总长度恰为 $|t_0|$。
若 $t_0\ne0$，令 $e_k=|t_k|$，则

\[
 \lim_{k\to\infty}\frac{e_{k+1}}{e_k^3}=\frac1\lambda.
\]



**证明。**

方程 [对应公式](#eq-gppa-bregman-cubic-step) 使 $t_{k+1}$ 与非零的 $t_k$ 同号，
并给出 $|t_{k+1}|<|t_k|$。
将其代入极限方程可知 $t_k\to0$，而 $s_k=s_0$。
于是总长度由 $\sum_k|t_k-t_{k+1}|=|t_0|$ 给出。
同一方程还给

\[
 \frac{|t_{k+1}|}{|t_k|^3}
 =\frac1{\lambda+t_{k+1}^2}\longrightarrow\frac1\lambda.
\]



本例对主定理的条件可直接在物理空间中验证。
$F=\partial f$ 的真实残差为 $r_F(t,s)=|t|=d((t,s),S)$，
而对最近零点 $p=(0,s)$，有

\[
 \|v(t,s)-v(p)\|=|t|^3.
\]
因此前向锚模为 $a(r)=r^3$，真实物理误差界为 $\psi(q)=q$。
核坐标中的完整关系是
$A(z,w)=(\sqrt[3]{z},0)$；其单调性给反射模 $\omega(q)=q$。
相应的一步直接界为 $d(x_{k+1},S)\le d(x_k,S)^3/\lambda$。
取 $R^2<\lambda$、$\kappa=R^2/\lambda$ 及 $\bar t\ge R^3/\lambda$，
它在 $0\le d(x_k,S)\le R$ 上给出严格收缩。
对全部合法转移，第二坐标不变且第一坐标同号，故

\[
 \|x_{k+1}-x_k\|
 \le\|v(x_{k+1})-v(x_k)\|^{1/3}.
\]
故可取 $h(t,q)=q^{1/3}$，有 $H(t)=t$、$\Theta(t)=t/(1-\kappa)$。
在 $U=\mathbb R^2$ 上，输入覆盖、评价窗与初值预算全部满足，
即使核逆在解附近不满足 Lipschitz 界，主定理仍给出物理有限长度。

若改用二次核 $h_0(t,s)=(t^2+s^2)/2$，
同一个目标的普通 PPA 则给 $t_{k+1}=t_k/(1+\lambda)$。
因此这里的立方速率来自近端正则项的改变。
本例说明的是非线性核与物理速率的关系；
非 Lipschitz 近端及沿解集的漂移由[C242 三角例](triangular_rleb.md#tri-object)承担。

<a id="prg-circle"></a>
## C248-v1 · 弱凸优化的圆与补偿临界点

- **Status**：`derived-checked`。它把 C231 和 C244 的圆形机制实现为一个明定 C¹ 弱凸目标；下面完整近端计算不依赖从任意指定 T 反造 F。


### 圆形极小点集与一个补偿临界点


平面中的圆具有欧拉示性数零，故[C250 指数平衡](rleb_kernel_topology_interfaces.md#rkt-local-index)要求吸引管外的零点
贡献总指数 $1$。这一现象已经出现在一个简单的弱凸优化问题中。
对 $y\in\mathbb R^2$，置 $r=\|y\|$，定义
<a id="eq-radial-weakconvex-function"></a>
\[



 f(y)=
 \begin{cases}
 -r^2/6,&0\leq r\leq3/4,\\
 r^2/2-r+3/8,&r\geq3/4.
 \end{cases}
\]
两个表达式及其径向一阶导数在 $r=3/4$ 处吻合。
而 $f(y)+\|y\|^2/6$ 的径向表达式在 $[0,3/4]$ 上为零，
在 $[3/4,\infty)$ 上为 $2r^2/3-r+3/8$，
是凸且非减的函数。因此 $f$ 为 $C^1$ 的 $1/3$-弱凸函数，
即 $f+(1/6)\|\cdot\|^2$ 为凸函数。
其全局极小点集是单位圆 $M=\{y:\|y\|=1\}$，
而梯度的完整零集还包含原点：

\[
 F(y):=\nabla f(y)=
 \begin{cases}
 -y/3,&\|y\|\leq3/4,\\
 (1-1/\|y\|)y,&\|y\|\geq3/4,
 \end{cases}
 \qquad F^{-1}(0)=M\cup\{0\}.
\]

取 $\lambda=1$。由于 $f$ 为 $1/3$-弱凸函数，
$y\mapsto f(y)+\|y-x\|^2/2$ 为 $2/3$-强凸且强制的函数，
故其唯一极小点给出完整近端映射 $T=J_F$。
最优性条件 $x=y+F(y)$ 保持方向，径向方程为

\[
 \|x\|=
 \begin{cases}
 2\|y\|/3,&\|y\|\leq3/4,\\
 2\|y\|-1,&\|y\|\geq3/4.
 \end{cases}
\]
于是，若 $B$ 为闭单位圆盘，则
<a id="eq-radial-proximal-map"></a>
\[



 T(x)=\frac{x+P_B(2x)}2,\qquad
 C(x):=(2T-I)x=P_B(2x).
\]
$C$ 有界且为 $2$-Lipschitz，因而

\[
 \|C(x)-C(y)\|\leq\min\{2\|x-y\|,2\}
 \leq2\|x-y\|^\gamma\qquad(0<\gamma<1).
\]

在圆的闭管 $N_{1/4}$ 内，最近点是 $p=x/\|x\|$，
且 $C(x)=p$。反射锚定条件因此可取 $L=0$；
实际输出的半径至少为 $7/8$，所以
$r_F(Tx)=d(Tx,M)$。取 $\psi(t)=t$，直接得到

\[
 d(Tx,M)=\tfrac12d(x,M),\qquad
 \|Tx-x\|=\tfrac12d(x,M).
\]
因此，在 $U=\mathbb R^2$、$R=1/4$、$\bar t=1$ 下，
取 $\gamma=1$、$L=0$、$\psi(t)=t$、$\kappa=1/2$，
PPA 推论的 (B1)--(B4) 对目标圆成立。
圆附近每条轨道沿固定径向收敛到一个极小点。
原点附近却有 $T(x)=3x/2$，故原点是一个排斥固定点，
其平面固定点指数为
$\operatorname{sign}\det(I-(3/2)I)=1$。
圆的吸引管贡献指数零，原点恰好补足全局总指数。
它位于吸引管之外，同时仍在圆盘内部。


<a id="prg-linear-energy"></a>
## C249-v1 · 线性误差界的能量收缩

- **Status**：`derived-checked`。对象与前件明确映到 [C02-v3](true_residual_selection_rleb.md#trs-object) 的 B1–B3，γ=1，ψ(q)=cq（下式局部字母 K=c）；不保留原 B4。一步能量与真残差链由平行四边形和 (x−y)/λ∈F(y) 直接得出。


**corollary · 线性误差界下的能量收缩。**


<a id="cor-linear-energy-convergence"></a>

沿用PPA 推论~C02-v3 的普通 PPA 陈述 的对象和符号，令 $\gamma=1$。
只假设 (B1)--(B3)，其中 $\psi(t)=Kt$、$K>0$，
并保留相同的输出评价窗
$ (1+L)R/(2\lambda)\leq\bar t$。
以如下条件代替 (B4) 及原初值预算：
<a id="eq-linear-energy-factor"></a>
\[



 \begin{aligned}
 \rho_E&:=\left(\frac{1+L^2}{2(1+(\lambda/K)^2)}\right)^{1/2}<1,
 \qquad \mathcal L_E(r):=\frac{(1+L)r}{2(1-\rho_E)},\\
 \mathcal L_E(d_0)&<d(x^0,X\setminus U).
 \end{aligned}
\]
则从 $x^0\in U_R$ 出发的每条允许轨道均可无限延拓，
留在 $U_R$，具有有限长度，并收敛到 $x^\infty\in S\cap U$。
对所有 $k\geq0$，有
<a id="eq-linear-energy-rates"></a>
\[



 d(x^k,S)\leq\rho_E^k d_0,\qquad
 \|x^\infty-x^k\|\leq\mathcal L_E(d(x^k,S)).
\]




**证明。**

对每个合法输入 $x$ 和每个允许输出 $y$，令 $d=d(x,S)$、$d^+=d(y,S)$、$s=\|x-y\|$，
并取 B2 的最近零锚 $p$。该条件等价于 $\|2y-x-p\|\le Ld$。
平行四边形给 $\|y-p\|^2+s^2\le(1+L^2)d^2/2$，
三角不等式给 $s\le(1+L)d/2$。
由 $(x-y)/\lambda\in F(y)$，先有 $r_F(y)\le s/\lambda\le\bar t$，
同窗真误差界才可使用。因此得到

\[
 (d^+)^2+s^2\leq\frac{1+L^2}{2}d^2,\qquad
 d^+\leq K r_F(y)\leq(K/\lambda)s.
\]
消去 $s$ 得
$[1+(\lambda/K)^2](d^+)^2\leq(1+L^2)d^2/2$，
所以 $d^+\leq\rho_Ed$。
以上三角估计同时给出 $s\leq(1+L)d/2$。
对任意已构造的有限轨道前缀求和，便有

\[
 \|x^{k+1}-x^0\|
 \leq\frac{1+L}{2}\sum_{j=0}^{k}\rho_E^j d_0
 \leq\mathcal L_E(d_0)<d(x^0,X\setminus U).
\]
因此下一步仍在 $U_R$，(B1) 继续保证非空，归纳给无限延拓。
可和步长直接使序列为 Cauchy 列；有限维空间完备，
故轨道有极限。距离趋零与 $S$ 闭性使其属于 $S$；
从任意指标重新对几何步长求和，即得显示的尾项估计。
严格初始预算还保证极限留在 $U$。




其线性 RL 参数识别为 μ=(1−L²)/(2λ(1+L²))、ν=λ²μ；当L≥1，τ=(L²−1)/4给 λ⟨a,b⟩≥−τ||a+λb||²。平方展开是可逆证明，限同一受检点对。L=1时能量因子K/√(K²+λ²)<1对每个λ>0成立；极大单调完整覆盖、牢固非扩张留输出于原小球和局部真EB一起给完整 PPA 局部点线性收敛。不是仅由核正定或单调性名称推出。

## 一手来源、独立边界与复现

- Bauschke–Borwein–Combettes 2003 [作者原文](https://pcombet.math.ncsu.edu/sicon2.pdf)，Definitions 3.7/3.16、Proposition 3.22：Bregman 最优性和近端关系；本例完整存在、率与长度直接重构，不导入全文收敛定理。
- Bùi–Combettes 2020 [作者原文](https://pcombet.math.ncsu.edu/jmaa5.pdf)，Definition 1.1 与 Examples 3.1/3.4：核化近端关系的背景；该定义的覆盖和注入性不被自动视作这里允许多值关系的假设。
- Leventhal [0902.4200v1](https://arxiv.org/pdf/0902.4200)，Theorem 3.1 pp.6–7：K²/(K²+λ²) 为距离平方因子。Luke–Tam 正式版 Definition 2 与 Assumption 2(d)(ii)、Evens 2305.03605v2 Definition 4.1 只按实际尺度/点对/覆盖接口使用。
- 主稿 [gppa_theory.tex](../../发表成果整理/RLEB/sections/gppa_theory.tex)、[自然例](../../发表成果整理/RLEB/sections/bregman_example.tex)；[开发报告](../../发表成果整理/GPPA主理论/主理论开发.md)、[边界审查](../../发表成果整理/GPPA主理论/独立边界审查.md)、[整稿冷读](../../发表成果整理/GPPA主理论/整稿独立冷读.md)定位实际阅读与修补。
- [主接口复算](../code/rleb_gppa/verify.py)、[自然例高精度复算](../code/rleb_gppa_example/verify.py)、[包装公式复算](../code/rleb_packaging/verify.py)、[独立攻击复算](../code/rleb_gppa_attack/verify.py)仅验证指定有限实例；一般量词由本页证明承担。

当前接收仅限本页及对应主稿的新链；不等于全库语义审计、穷尽文献或同行评审。一般非几何收缩、时变核、误差、松弛及全局物理指数的核不变性不是本页已证结论。
