# 移动零点锚下的渐近反射

本页重写 9/01 RL_foundations §6 的点态几何。对象是**每个实际图点和随之选择的输出近邻零点**；它不给 reflector 的全对模，也不替代近端输入覆盖。

<a id="ma-object"></a>
## MA-OBJECT · 真残差输出与可选择的近锚

令 H 为实 Hilbert 空间，\(\lambda>0\)，非空 \(S\subset F^{-1}(0)\)，\((y,w)\in\operatorname{gph}F\)，\(0<t=\|w\|<\eta\)。在这一实际输出 y 上假设真残差 EB
\[
d(y,S)\le\psi(r_F(y)),
\]
其中 \(\psi:[0,\eta)\to[0,\infty)\) 有限非减且 \(\psi(t)=o(t)\)。取 \(e(t)\ge0,e(t)=o(t)\) 和 \(p\in S\) 使 \(\|y-p\|\le d(y,S)+e(t)\)。若 \(e(t)>0\)，从 infimum 定义可选这样的 p，无须 \(P_S(y)\ne\varnothing\)；若 \(e(t)=0\)，须实际有最近零点。令
\[
x=y+\lambda w,\quad \widehat x=y-\lambda w,\quad
\delta_t=\frac{\psi(t)+e(t)}{\lambda t}.
\]
真残差方向 \(r_F(y)\le t\) 和 \(\psi\) 非减给 \(\|y-p\|\le\delta_t\lambda t\)。条件作用于同一个图点；没有假设所有 w 或所有输入存在某个统一选择 p。

<a id="ma-reflect"></a>
## C51-v1 / MA-REFLECT · 输出近锚的双边反射比

对每个上述图点，若 \(\delta_t<1\)，有
\[
\frac{1-\delta_t}{1+\delta_t}
\le\frac{\|\widehat x-p\|}{\|x-p\|}
\le\frac{1+\delta_t}{1-\delta_t},\qquad
\frac{\|\widehat x-(2p-x)\|}{\|x-p\|}
\le\frac{2\delta_t}{1-\delta_t}. \tag{MA-1}
\]
沿任意合法图点序列 \(t_n\to0,t_n>0\)，若逐项选到上述 \(p_n\)，则比值趋 1 且
\(\widehat x_n-p_n=-(x_n-p_n)+o(\|x_n-p_n\|)\)。

**证明。** 写 \(a=y-p,b=\lambda w\)，则 \(x-p=a+b,\widehat x-p=a-b,\|a\|\le\delta_t\|b\|\)。正反三角不等式同时把两范数夹于 \((1-\delta_t)\|b\|\) 与 \((1+\delta_t)\|b\|\)，给双边比。又 \(\widehat x-(2p-x)=2a\)，且 \(\|x-p\|\ge(1-\delta_t)\|b\|\)，给缺陷界。因为 \(\delta_{t_n}\to0\)，相对缺陷趋零。这里“趋于反射比 1”不意味着距离到集合 S 的收缩。

<a id="ma-power"></a>
## C52-v1 / MA-POWER · 幂型缺陷的明确常数

若另有 \(q>1,\rho,c\ge0\)、\(d(y,S)\le\rho r_F(y)^q\) 与所选 p 的 \(\|y-p\|\le d(y,S)+ct^q\)，置 \(A=\rho+c\)。若 \((A/\lambda)t^{q-1}\le1/2\)，则
\[
\|\widehat x-(2p-x)\|
\le\frac{2^{q+1}A}{\lambda^q}\|x-p\|^q. \tag{MA-2}
\]
确实，\(\|y-p\|\le At^q\) 且 \(\|x-p\|\ge\lambda t-At^q\ge\lambda t/2\)，再用缺陷恒等式。\(A=0\) 时直接得零缺陷，不用除以 A；此数值常数是充分界，不声称最优。

<a id="ma-limit"></a>
## 边界：移动锚不能换成固定锚或集合距离收缩

取 \(H=\mathbb R^2,S=\mathbb R\times\{0\}\)。令 \(F(y)=\{(0,0)\}\cup\{(1/n,1/n):n\ge1\}\) 对 \(y\in S\)，其余 y 处为空。对 \(y=(1,0),w_n=(1/n,1/n)\)，真实 \(r_F(y)=0=d(y,S)\)；可取 \(p_n=y\)，所以 MA-1 的 \(\delta=0\) 且反射比恰为 1。可是对固定 \(p_0=(0,0)\)，缺陷 \(\widehat x_n-(2p_0-x_n)=2y\) 不趋 0，相对 \(\|x_n-p_0\|\) 的比值趋 2；且 \(d(x_n,S)=d(\widehat x_n,S)=\lambda/n\)。因此移动锚结论不能写成“关于任一固定零点的渐近反射”或“到 S 的严格收缩”。此例不宣称全对 RL，也不反驳另有兼容、coverage 的局部收敛定理。

<a id="ma-source"></a>
## 来源与范围

从 [9/01 RL_foundations §6.1–6.2](../../history/sources/次单调论文研究/RL_foundations.md) 重新推导双边比、幂型系数和近似锚的存在门。状态 derived-checked 限这些点态推导与本页反例。它与[孤立零点的固定 p](isolated_zero_flatness.md)及[非孤立零集的输出最近锚漂移](nonisolated_alignment.md)对象相邻而量词不同：若要把三者接成算法定理，还须同一输入域上的分支存在、真实输出 EB、统一预算与留域。
