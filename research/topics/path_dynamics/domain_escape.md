# 振荡反射的自然域逃逸

<a id="de-object"></a>
## DE-OBJECT · 关系只在指定 Minty 域上定义

取 \(0<\alpha<1,\beta>0,0<\delta<1,\lambda=1\)，并定义带符号幂 \(P_\alpha(x)=\operatorname{sign}(x)|x|^\alpha\)（\(P_\alpha(0)=0\)）。对 \(x\ne0\) 令
\[
C(x)=P_\alpha(x)[2+\sin(|x|^{-\beta})],\quad C(0)=0,\quad
J(x)=\tfrac12(x+C(x)),\qquad x\in D=[-\delta,\delta].
\]
只定义关系 \(\operatorname{gph}F=\{(Jx,x-Jx):x\in D\}\)。输入自然域是 **D**；\(J\) 可因振荡而非单射，\(F(u)\) 允许多个值。\(J\) 连续且保持符号，\(Jx=0\) 仅在 \(x=0\)，所以 \(\operatorname{zer}F=\{0\}\)。图是紧的，任意实际输出纤维非空时真残差 \(r_F(u)=\min\{|x-u|:x\in D,Jx=u\}\)，不能先指定一个有利分支。

<a id="de-exponent"></a>
## 锚定与全对反射的两个指数

置 \(\eta_*=\alpha/(\beta+1)\)。对非零 \(x\in D\)，
\[
|x|^\alpha\le|C(x)|\le3|x|^\alpha.
\]
零点锚定的最大幂指数为 \(\alpha\)，其系数 3 在每个零邻域都是最小可用上界（相位令 \(\sin=1\)）。全对 Hölder 的最大局部指数则仅为 \(\eta_*<\alpha\)。

**两尺度证明。** 对两个近零输入的最大模 \(r\) 和差 \(\Delta\)，若 \(\Delta\ge r/2\)，振幅界给 \(O(\Delta^\alpha)\)，从而给 \(\eta_*\) 界。若 \(\Delta<r/2\)，两点同号且模可比；当 \(\Delta\ge r^{\beta+1}\) 用 \(O(r^\alpha)\le O(\Delta^{\eta_*})\)，当 \(\Delta<r^{\beta+1}\) 用导数 \(O(r^{\alpha-\beta-1})\Delta\le O(\Delta^{\eta_*})\)，因为 \(\alpha=\eta_*(\beta+1)\)。取 \(s_n=2\pi n+\pi/2,t_n=s_n+\pi,x_n=s_n^{-1/\beta},y_n=t_n^{-1/\beta}\)，则
\[
|x_n-y_n|\sim(\pi/\beta)s_n^{-1/\beta-1},\quad
|C(x_n)-C(y_n)|\sim2s_n^{-\alpha/\beta},
\]
故商 \( |C(x_n)-C(y_n)|/|x_n-y_n|^{\eta_*}\to2(\beta/\pi)^{\eta_*}>0\)。更高指数失败。这里锚定指数与全对指数是**同一图但不同配对量词**。

<a id="de-escape"></a>
## C44-v1 / DE-ESCAPE · 扩张导致有限步越出自然域

对每个非零 \(x_0\in D\)，若按该关系迭代 \(x_{k+1}=Jx_k\)，则在**有限**步出现 \(x_k\notin D\)；因此关系不再给合法下一步。设 \(r=|x|\in(0,\delta]\)、\(c(x)=2+\sin(r^{-\beta})\in[1,3]\)，则
\[
r_+=|Jx|=\frac{r+c(x)r^\alpha}{2},\qquad
\frac12r^\alpha\le r_+\le2r^\alpha,\qquad r_+>r.
\]
若所有步都留在 D，递增半径有极限 \(0<\ell\le\delta<1\)。连续性给 \(\ell=|J(\operatorname{sign}(x_0)\ell)|\)，即
\(\ell^{1-\alpha}=c(\ell)\ge1\)，与 \(\ell<1\) 矛盾。这个结论是**有限域逃逸**，不等于算法在更大且未定义的域上发散；\(r_+=\Theta(r^\alpha)\) 是一步尺度，不能称收敛阶。

<a id="de-residual"></a>
## 真残差的线性下确界与高次幂失败

对每个非零输出 \(u=Jx\) 和相应图点 \(w=x-u\)，当 \(r=|x|\to0\) 时
\[
\frac{|u|}{|w|}
=\frac{c(x)+r^{1-\alpha}}{c(x)-r^{1-\alpha}}
\longrightarrow1
\]
且收敛对 \(c(x)\in[1,3]\) **一致**。因为 \(|Jx|\ge r^\alpha/2\)，\(u\to0\) 时所有原像都趋零；J 连续、保符号且从 0 的像覆盖某个零邻域，所以每个充分小的非零 u 都有非空紧原像。对这些原像的最小残差取值后得到
\[
\frac{d(u,\{0\})}{r_F(u)}=\frac{|u|}{r_F(u)}\longrightarrow1
\quad(u\to0,\ u\ne0).
\]
因此对任意 \(K>1\)，缩小输出邻域后有 \(d(u,S)\le K r_F(u)\)；局部线性 EB 常数的**下确界**为 1，但这里不声称常数 1 在任何固定邻域取到。任意 \(q>1\) 的统一幂 EB 失败，因为 \(r_F(u)\sim|u|\) 且 \(u\to0\)。这条真实全纤维陈述不使用选中步代替 infimum。

<a id="de-source"></a>
## 来源与使用边界

从 [9/01 RL_foundations §9.4 / GX-073](../../../history/sources/次单调论文研究/RL_foundations.md) 重算。状态 derived-checked 限于自然域、两种指数、有限逃逸和全纤维残差的推导；不对外部文献优先性下结论。与 [GX-071](power_shear.md) 的切向留域和 [GX-072](oscillatory_shear.md) 的不变小球相比，本例专门攻击把一步模直接称为轨道速率的推理。改变 D 或给 J 全局延拓是**新对象**，不能继承此逃逸结论。
