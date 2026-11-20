# 两个最近零锚与逆映射的角度补偿

固定有限维欧氏空间上的原关系 \(F\)、非空闭集 \(S\subseteq F^{-1}(0)\) 和步长 \(\lambda>0\)。考察原步 \(x=y+\lambda v\)、\(v\in F(y)\)。记 \(h=x-y,\ s=\|h\|\)，取 \(p_1\in P_S(x)\)、\(p_2\in P_S(y)\)，其中 \(P_S\) 表示全部最近点。真残差为 \(r_F(y)=\inf_{w\in F(y)}\|w\|\)，空纤维记 \(+\infty\)。

<a id="two-anchor-angle"></a>
## C381 · 换锚恒等式与两段锐门

对非空输出纤维，正则性 \(d(y,S)\le\psi(r_F(y))\) 对连续非减模 \(\psi\) 等价于 \(d(y,S)\le\psi(\|w\|)\) 对每个 \(w\in F(y)\) 成立。反向在完整纤维上逼近下确界即可。沿原步有 \(\|y-p_2\|\le\psi(s/\lambda)\)。圆的中心是 \(y\)，误差界给出半径上界。方向侧的 \(\langle y-p_1,h\rangle\) 则等于三角形 \(x,y,p_1\) 在 \(y\) 的内角余弦乘以 \(-\|y-p_1\|s\)。给定两边和内角，第三边由余弦定理固定。

两个最近性差值满足
\[
\begin{aligned}
d(x,S)^2-d(y,S)^2
 &=s^2+2\langle y-p_1,h\rangle
   +\underbrace{\|y-p_1\|^2-\|y-p_2\|^2}_{B\ge0},\\
\underbrace{\|x-p_2\|^2-\|x-p_1\|^2}_{A\ge0}+B
 &=2\langle h,p_1-p_2\rangle .
\end{aligned}
\tag{1}
\]
第一式先固定 \(p_1\) 展开平方，再在输出处换到 \(p_2\)。第二式分别展开在 \(x,y\) 处的两个交叉差。沿轨道望远镜相消的是第一式左边的距离差。\(A+B\) 测量锚移动在原步方向上的分量。

当 \(S\) 凸时，投影变分不等式给 \(A,B\ge\|p_1-p_2\|^2\)。仿射情形二者都等于 \(\|p_1-p_2\|^2\)。一般闭集可有小差值和大跳锚，例如 \(S=\{-1,1\}\)、\(x=\epsilon,y=-\epsilon\)、\(0<\epsilon<1\)，两差值都为 \(4\epsilon\)，锚距为 2。这是一步投影例。即使锚移趋零或平方可和，仍需另证锚点序列收敛。

**距离下降支付长度。** 假设每条受检原步存在输入最近点 \(p_1\) 使
\[
\langle y-p_1,h\rangle\ge-\alpha\|y-p_1\|s,\qquad 0\le\alpha\le1.
\tag{2}
\]
这是最近输入零锚的余弦下界。较大的 \(\alpha\) 允许较多逆向分量。另设同一输出的完整真残差满足 \(d(y,S)\le K r_F(y)\)、\(K>0\)。令 \(t=d(y,S),\ b=\|y-p_1\|\)。则 \(b\ge t\)，且 \(s>0\) 时 \(t/s\le K/\lambda\)。保留整个 \(B=b^2-t^2\)，对 \(b\ge t\) 配方得到
\[
d(x,S)^2\ge s^2+b^2-2\alpha bs
\ge (1-\alpha^2)s^2+(t-\alpha s)_+^2 .
\tag{3}
\]
最坏半径为 \(b=\max\{t,\alpha s\}\)。若 \(b=t\)，可以取同一个最近锚。若 \(\alpha s>t\)，最坏半径超过正则侧的距离，两个锚的区别进入认证。

函数 \(u\mapsto\sqrt{1-\alpha^2+(u-\alpha)_+^2}-u\) 非增，因为其中平方根项是 1-Lipschitz。令 \(\gamma=K/\lambda\)，则
\[
d(x,S)-d(y,S)\ge\eta s,\qquad
\eta=\sqrt{1-\alpha^2+(\gamma-\alpha)_+^2}-\gamma .
\tag{4}
\]
零步长也满足 (4)。严格余量 \(\eta>0\) 恰等价于
\[
\frac{\lambda}{K}>
\begin{cases}
2\alpha,&0\le\alpha\le1/\sqrt2,\\
(1-\alpha^2)^{-1/2},&1/\sqrt2<\alpha<1.
\end{cases}
\tag{5}
\]
在 \(\gamma\ge\alpha\) 和 \(\gamma\le\alpha\) 分别平方检验 \(1-2\alpha\gamma>0\) 和 \(1-\alpha^2>\gamma^2\) 即得。当 \(\alpha=1\) 时无统一正余量。单点目标强制 \(b=t\)，其阈值一直为 \(\lambda/K>2\alpha\)，包括 \(\alpha=1\)。

沿任意受检无限轨道，(4) 给总长 \(\sum_k s_k\le d(x^0,S)/\eta\)，因而原点列收敛。由 \(t\le\gamma s\)，极限属于 \(S\)。任意最近点序列的锚位移也绝对可和，因为
\[
\|p_1-p_2\|\le d(x,S)+s+d(y,S)\le (2+2\gamma)s.
\]
若每个输入均有受检原根，则可以无限续接。若仅覆盖开域 \(U\) 内的输入，则从 \(d(x^0,S)/\eta<d(x^0,\mathbb R^n\setminus U)\) 的域内初值出发，有限前缀长度先保证留域。若另有输入距离窗，(4) 保证距离窗。覆盖是一项独立前提。

**一般模。** 若 \(d(y,S)\le\psi(r_F(y))\)，可在 (4) 的逐边版本用 \(\psi(s/\lambda)/s\) 代替 \(\gamma\)。方向亏损也可逐尺度变化。所有可达正步长上的统一正余量给同样的长度预算。逐点严格余量先给距离下降，点收敛或长度需另证。原最近锚反射模仅直接给 \(4\langle y-p_1,h\rangle\ge d(x,S)^2-\omega(d(x,S))^2\)，要转出 (2) 还须控制除数 \(bs\)。

**两段阈值的完整原图边界。** 固定 \(0<\alpha<1\)、\(\lambda>0\)，以下 \(J\) 为全域线性双射，令 \(F=(J^{-1}-I)/\lambda\)。其完整原近端就是 \(J\)，真残差为 \(s/\lambda\)。

- \(\alpha\le1/\sqrt2\) 时取 \(S=\{0\}\)，令平面 \(J\) 为角 \(2\arcsin(\alpha)\) 的旋转。于是 \(s=2\alpha t\)、\(\langle y,h\rangle=-s^2/2=-\alpha ts\)。第一段在等号处距离不减。直积恒等切向坐标给非孤立目标且两锚相同。
- \(\alpha>1/\sqrt2\) 时取 \(S=\mathbb R^2\times\{0\}\)，令 \(J(a,z)=(a+cz,Qz)\)，其中 \(Q\) 是 90 度旋转，\(c^2=(2\alpha^2-1)/(1-\alpha^2)\)。有 \(d(x,S)=t=\|z\|\)，锚距 \(c\|z\|\)，\(s^2=(c^2+2)t^2=t^2/(1-\alpha^2)\)，\(b^2=(c^2+1)t^2=\alpha^2s^2\)，以及 \(\langle y-p_1,h\rangle=-b^2=-\alpha bs\)。在第二段等号处，\(J^4=I\)，任意非零法向初值为非解周期。最坏情形确由锚移动实现。

相同见证也满足更宽松的误差界常数。\(\alpha=1\) 时，\(F(a,b)=(cb,0)\)、\(c>0\)，有任意小的 \(K=1/c\)，原步仍沿零平面平移。这继承已有剪切机制。故 (5) 是上述类的统一严格门。它与 [C288](../../canonical/rleb_nearest_anchor_geometry.md) 的反射模锐门使用不同的方向参数。

<a id="inverse-angle-branch"></a>
## C382 · 同一个逆分支角度条件给原根与点收敛

普通度量次正则性可写成 \(F^{-1}\) 在零值处的 calmness。度量正则对应逆关系的 Aubin 性质，强度量正则对应局部单值 Lipschitz 逆。文献见 [Dontchev–Rockafellar](https://sites.math.washington.edu/~rtr/papers/rtr191-RegularityConditioning.pdf) Theorems 2.2、3.2、4.2 及 [Aragón Artacho–Mordukhovich](https://rua.ua.es/dspace/bitstream/10045/29037/1/2011_Aragon_Mordukhovich_JGlobalOptim.pdf) §4。若只指定一个零集真子集，误差界以该子集为目标。

**原步定理。** 固定 \(p\in S\)、\(\lambda,R>0\)。假设原逆关系在闭值球 \(\overline B(0,R)\) 上有连续选择 \(Y\)，满足 \(Y(0)=p\)、\(v\in F(Y(v))\)。若每个 \(0<\|v\|\le R\) 满足
\[
2\langle Y(v)-p,v\rangle+\lambda\|v\|^2>0,
\tag{6}
\]
则每个 \(\|x^0-p\|\le\lambda R/2\) 的初值都有一条始终留在该闭球、可无限续接并收敛到 \(p\) 的原 PPA 轨道。允许原逆关系多值及 \(p\) 非孤立。结论量化所构造的根。

**根存在。** 写 \(G(v)=Y(v)+\lambda v\)。对 \(\|v\|=R\) 和 \(\|x-p\|\le\lambda R/2\)，(6) 给 \(\langle G(v)-x,v\rangle>0\)。对闭值球上的连续自映射 \(v\mapsto P_{\overline B(0,R)}(v-G(v)+x)\) 用 Brouwer 定理。若不动点位于球面，以 0 作投影变分不等式的比较点得到 \(\langle G(v)-x,v\rangle\le0\)，矛盾。内部不动点满足 \(G(v)=x\)，所以 \(y=Y(v)\) 是原根。

**续接与收敛。** 原边的平方展开给
\[
\|x-p\|^2-\|y-p\|^2
 =\lambda\bigl(2\langle Y(v)-p,v\rangle+\lambda\|v\|^2\bigr).
\]
同一个 (6) 保证原球自覆盖。沿所选近端步求和，右侧在远离 0 的任何紧环上有正最小值，故 \(v_k\to0\)，从而 \(Y(v_k)\to p\)。

**强弱交换。** 若 \(\|Y(v)-p\|\le\psi(\|v\|)\)，且 \(\langle Y(v)-p,v\rangle\ge-\alpha\|Y(v)-p\|\|v\|\)，则 \(\lambda r>2\alpha\psi(r)\) 对所有 \(0<r\le R\) 即可。Lipschitz 情形 \(\psi(r)=\kappa r\) 给 \(\lambda>2\alpha\kappa\)。\(\alpha=1\) 给出 C378 已见的最坏角度门。方向功非负时，任意连续逆选择即够用，无需定量 Lipschitz 速率。对 \(0<\alpha\le1\)，在线性平面取 \(Y(v)=\kappa(-\alpha I+\sqrt{1-\alpha^2}Q)v\)，\(Q\) 为 90 度旋转，\(F=Y^{-1}\)、\(p=0\)。在 \(\lambda=2\alpha\kappa\) 时 \(\|Y(v)+\lambda v\|=\|Y(v)\|=\kappa\|v\|\)，两张线性图均可逆，原 PPA 保持非零范数，故该门的等号不能纳入。

**非孤立与非线性见证。** 在 \(\mathbb R^m\times\mathbb R\) 取 \(F(a,b)=\mathbb R^m\times\{\operatorname{sgn}(b)|b|^q\}\)、\(q>1\)。完整零集为 \(\mathbb R^m\times\{0\}\)，完整真残差为 \(|b|^q\)。对 \(p=(a_0,0)\) 选 \(Y(v)=(a_0,\operatorname{sgn}(v_{m+1})|v_{m+1}|^{1/q})\)，则 \(\|Y(v)-p\|\le\|v\|^{1/q}\)，方向功非负。取初值的最近锚为固定 \(p\)，所构造原步保持切向位置。完整原图对不同切向位置的图值差可以任意大且逆向，因此任意有限的欧氏弱单调常数均失败。

**紧凸值逆分支。** 连续单点选择可替换为闭值球上的集合值 \(\mathcal Y\)，要求非空紧凸值、闭图、一致有界、\(\mathcal Y(v)\subseteq F^{-1}(v)\) 及 \(\mathcal Y(0)=\{p\}\)。把 (6) 对每个 \(y\in\mathcal Y(v)\) 施加。取包含全部 \(\mathcal Y(v)\) 的闭位置球 \(C\)。在 \(\overline B(0,R)\times C\) 上使用 Kakutani，映射为
\[
(v,y)\longmapsto\{P_{\overline B(0,R)}(v-y-\lambda v+x)\}\times\mathcal Y(v).
\]
它有闭图、非空紧凸值，并映入同一紧凸域。任一不动点满足 \(y\in\mathcal Y(v)\)，球面用相同角度条件排除，球内得到原步。下降量在任何远离 0 的紧图环带上有正最小值，故 \(v_k\to0\)。闭图、一致有界及 \(\mathcal Y(0)=\{p\}\) 给 \(y_k\to p\)。此扩展采用的是逆值的凸性，原 \(F(y)\) 仍可非凸。无需预设一条连续选择。

C382 使用固定锚的可选逆分支，C381 使用随原步变动的最近锚及完整误差界。所选逆图只控制其中的点，不能反推出完整 \(r_F\) 的下界，也不能由一般锚式 RL 或逆关系的 calmness 直接推出。[C354](rleb_degree_and_selection_obstruction.md) 对完整原理论无连续近端选根的障碍仍有效。开放义务是在一般原 RL 中构造可用的逆图，或用无需凸值的逆运输保留原根覆盖与换锚差值的控制。
