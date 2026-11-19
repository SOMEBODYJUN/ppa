# 用同一个闭链检验原近端步

先从原图标出可选根，再检验这些原弦能否和一般模梯度插值共用同一组势函数值。可行时，闭链构造给一个沿原轨道下降的势。位移代价用模积分的凸共轭。下文证明参数严格大于临界值时，真实位移按固定长度的块几何衰减，因而无须 Dini。也给出临界不收敛以及不能导入全部原 RLEB 的边界。

<a id="feedback-original-steps"></a>
## 原 PPA 的混合闭链判据

设 \(X\) 为有限维欧氏空间，\(F:X\rightrightarrows X\)，\(S\subseteq F^{-1}(0)\) 非空闭。写 \(d(x)=\operatorname{dist}(x,S)\)、\(r_F(y)=\inf_{v\in F(y)}\|v\|\)，下确界取完整纤维。固定连续非减凹无界的模 \(\omega\)，其中 \(\omega(0)=0\) 且正尺度为正。令
\[
\Phi(t)=\int_0^t\omega(u)\,du,\qquad
\Phi^*(s)=\sup_{t\ge0}\{st-\Phi(t)\}.
\]
在工作集 \(E\supseteq S\) 上标出允许弧 \(x\to y\)，要求对每个 \(x\in E\) 至少一条，所有终点均在 \(E\)，且 \(x-y\in\lambda F(y)\)。在 \(S\) 只需标出驻定弧。对标出的每个输出 \(y\notin S\)，要求
\[
r_F(y)\ge c\,\omega(d(y)),\qquad c>0.
\tag{1}
\]
步长 \(\lambda>0\) 固定。取参数 \(B,L>0\)，给定梯度数据 \(g:E\to X\)，满足 \(g|_S=0\)。使用三种有向边，允许同端点有多条不同边。

1. 对所有 \(a,b\in E\)，取 [C362 的插值上界 (D)](gradient_feedback_general_modulus.md#feedback-modulus-cycles)。若两端均在 \(S\)，边权取零。
2. 每条标出的原弧 \(x\to y\) 加一条边，边权取 \(-\Phi^*(L\|x-y\|)\)。
3. 从每一点加一条返回固定 \(p\in S\) 的零权边。

要求每条有限闭合链的权和非负。这一项检验对整个标出图进行，可在选轨道之前陈述。它等价于存在一组共同的势函数值，在每条边上满足“终值减始值不超过边权”，并在 \(S\) 取零。必要性由沿链相加得到。充分性取从 \(p\) 到各点的有限链权下确界。直达边与零权回边确保下确界有限，追加一条边给各边的约束。两方向的锚点零权边给 \(h=0\) 于 \(S\)，回边给非负性。按 C362 的原插值定理，所得函数值及 \(g\) 可由同一全域 \(C^{1,\omega}\) 势 \(h\) 实现，且该势在 \(S\) 平坦。取最近锚点 \(p_x\in S\)，在 \(p_x\to x\) 的边权公式里以测试点 \(x\) 取上界，再用原弧边，得到
\[
0\le h(x)\le B\Phi(d(x)),\qquad
h(x)-h(y)\ge\Phi^*(L\|x-y\|).
\tag{2}
\]
反过来，如有全域平坦的 \(C^{1,\omega}\) 势非负于 \(E\)，且付得起所有标出弧的代价，取它的梯度和模预算即可通过闭链检验。

**原轨道定理。** 若 \(\lambda Lc>1\)，则从每个 \(x^0\in E\) 出发，每条按标出弧选取的原 PPA 轨道均可无限续接、有限长，并收敛到 \(S\) 中一点。此处无需先建立距离收缩或 Dini。以下证明同时给出一个与初值无关的分块长度及几何因子。

写 \(d_k=d(x^k)\)、\(s_k=\|x^k-x^{k+1}\|\)、\(h_k=h(x^k)\)。令 \(a=\lambda Lc>1\)。由原近端方程和 (1)，\(Ls_k\ge a\,\omega(d_{k+1})\)。在共轭定义中取 \(t=d_{k+1}\)，并用 \(t\omega(t)\ge\Phi(t)\)，得到
\[
h_k-h_{k+1}\ge(a-1)\Phi(d_{k+1})
                  \ge \frac{a-1}{B}h_{k+1}.
\]
所以 \(h_{k+1}\le\beta h_k\)，其中 \(\beta=B/(B+a-1)<1\)。

取 \(K\ge 1\) 足够大使 \(1+B/K<a\)，再取正整数 \(m\) 使 \(B\beta^{m-1}/(a-1)\le K^{-2}\)。由前式，
\[
\Phi(d_{k+m})\le \frac{B\beta^{m-1}}{a-1}\Phi(d_k)
                \le\Phi(d_k/K).
\]
最后一步用凹性给 \(\Phi(t/K)\ge K^{-2}\Phi(t)\)。因此 \(Kd_{k+m}\le d_k\)。若尚未落入 \(S\)，在共轭定义中改取 \(t=Kd_k>0\)。用 (2) 可得
\[
Ls_k\le \frac{B\Phi(d_k)+\Phi(Kd_k)}{Kd_k}
      \le (1+B/K)\omega(Kd_k).
\]
把此式用于 \(k+m\)，并用原残差提供的下界，得到
\[
\omega(d_{k+m+1})\le \frac{1+B/K}{a}\,\omega(d_k).
\tag{3}
\]
在同一个估计中取 \(K=1\)，可得 \(s_k\le (B+1)\omega(d_k)/L\)。于是对 \(m+1\) 个余类逐级求和，得 \(\sum_k s_k<\infty\)。如果到达 \(S\)，以后均驻定。覆盖保证了原步可续，(3) 保证极限到 \(S\) 的距离为零。闭性给出极限在 \(S\)。全证明无需原图闭性，也无需 \(E\) 闭。

<a id="feedback-original-root-existence"></a>
## 让闭链本身产生原近端根

上述定理先要求每个输入有可续接的原弧。以下可以从图值验证，无需预先给原根。取 \(E=X\)。在每个位置 \(y\) 给一个非空紧凸子纤维 \(V(y)\subseteq F(y)\)，要求 \(V\) 闭图且局部有界。对所有 \(y\)、\(v\in V(y)\) 和 \(0<t\le1\)，在 C362 的插值边及回锚边之外，加入
\[
y+t\lambda v\ \longrightarrow\ y,\qquad\text{边权 }-\Phi^*(Lt\lambda\|v\|).
\tag{4}
\]
若所有这样的混合闭链都无负权，构造出的同一个势满足
\[
h(y+t\lambda v)-h(y)\ge\Phi^*(Lt\lambda\|v\|).
\tag{5}
\]
在这个版本，完整残差条件 (1) 要求对所有 \(y\notin S\) 成立。

**根存在性。** 固定任意原输入 \(x\)，取以 \(x\) 为心的闭球 \(K\)，半径 \(R\) 大到 \(\Phi^*(LR)>h(x)\)。这样的 \(R\) 存在，因为在共轭定义中固定任意正测试距离即可得随 \(R\) 无界的下界。取另一闭球 \(D\) 包含 \(\bigcup_{y\in K}V(y)\)，用局部有界性与 \(K\) 紧性保证。映射
\[
(y,v)\ \longmapsto\ \{P_K(x-\lambda v)\}\times V(y)
\]
在 \(K\times D\) 上有闭图、非空紧凸值。由 [Kakutani 定理及紧凸集推论](https://www.math.ucdavis.edu/~deloera/TEACHING/READINGSEMINAR/PAPERS/kakutanioriginal.pdf) 有不动点，故 \(v\in V(y)\) 且 \(y=P_K(x-\lambda v)\)。如果 \(y\) 在球面上，投影法向条件给 \(x=y+t\lambda v\) 对某个 \(0<t\le1\) 成立。于是 (5) 和 \(h(y)\ge0\) 推出 \(h(x)\ge\Phi^*(LR)\)，矛盾。因此 \(y\) 在球内，投影不动点就是 \(x=y+\lambda v\)。它是完整原图上的合法原 PPA 根。以所有这样选到的原根为允许弧，(5) 在 \(t=1\) 给出真实原步的下降。若 \(x\in S\)，下降条件强制 \(y=x\)，因为 \(\Phi^*(s)>0\) 对 \(s>0\) 成立。由上一节，在 \(\lambda Lc>1\) 时，从任意初值存在有限长点收敛的原轨道。实际上所有这些根的选择皆可。

**由凸反馈直接验证。** 如果用 C362 的凸闭链 (C) 验出一个全域凸势 \(h\)，使 \(\nabla h=g\)，且在 \(S\) 平坦，可以把 \(V(y)\) 选为
\[
\left\{v\in F(y):\ \lambda\langle g(y),v\rangle\ge\Phi^*(L\lambda\|v\|)\right\}.
\]
当 \(F\) 闭图、局部有界、凸值，并且上述交纤维逐点非空时，这个 \(V\) 满足所需条件。凸支撑给 \(h(y+t\lambda v)-h(y)\ge t\lambda\langle g(y),v\rangle\)。再由 \(\Phi^*(ts)\le t\Phi^*(s)\)，得到 (5)。这里 \(g\) 是统一势的梯度，无需等于原图值或原输入。若正则下界在全空间成立，则这个凸版本强迫 \(S=\arg\min h\)，因而 \(S\) 凸。在任一极小点，\(g=0\) 使非空交纤维只能含零值，真残差下界再把该点放进 \(S\)。一般的分数弦版本无凸势要求，但任何 \(y\notin S\) 的所选非零图值产生的分数输入均不能落在 \(S\)，否则 (5) 与平坦及非负性矛盾。因此[下文的反向两步图](#feedback-original-variational-obstruction)无法纳入这个全分数弦版本。

**直接核原 C242。** 对其完整 \(F(u,z)=(u,-\sqrt{|u|})\) 取 \(\lambda=1\)、反馈模 \(\omega(t)=t+\sqrt t\)。若 \(t=|u|\)，则 \(r_F=\sqrt{t^2+t}\ge\omega(t)/\sqrt2\)。取 \(L>\sqrt2\)，令 \(h(u,z)=L^3\Phi(|u|)\)，它是凸的平坦 \(C^{1,\omega}\) 势。由于 \(r_F\le\omega(t)\) 且 \(\omega(L^2 t)\ge L\omega(t)\)，
\[
\Phi^*(Lr_F)\le Lr_F\,\omega^{-1}(Lr_F)\le L^3t\omega(t)
                  =\langle\nabla h(u,z),F(u,z)\rangle .
\]
故逐点所有完整纤维都通过凸反馈验证。根存在性及收敛均来自定理，无须先求解原轨道或借助原反射。

**凸性在这里负责原根存在。** 取 \(X=\mathbb R\)、\(S=\{0\}\)、\(\lambda=1\)、\(\omega(t)=t\)、\(L=2\)。在正轴定义 \(F(y)\) 为 \(y\) 加阶梯函数 \(\sum_{2^{-j}<y}2^{-j}/8\)，\(j\ge1\)，并在每个跳点只保留阶梯左右两个端值。非正轴取 \(F(y)=y\)。原图闭、局部有界、单调，且所有原值满足 \(|y|\le|v|\le5|y|/4\)。取 \(h(y)=3y^2/2\)，每个原值都满足 \(3yv\ge2|v|^2=\Phi^*(2|v|)\)，所以包括全部分数弦的闭链均通过，真残差可取 \(c=1\)。但 \(I+F\) 的值域在每个跳点留下一个开区间，且这些缺口向 \(0\) 聚集。若将紧凸子纤维换成任意非空紧子纤维，根存在结论失败。

<a id="feedback-original-coverage"></a>
## 与原 RLEB 的交叉范围

设原最近零锚 RLEB 的步长包络为 \(H(t)=(t+\omega_{\rm RL}(t))/2\)，保留其实际工作窗、全部原根或原允许关系，以及完整真残差。设能找一个上述反馈模，使得在原半径上 \(H(t)\ge b\,\omega(t)\) 对某 \(b>0\) 成立，并且存在 \(L>1/b\) 与有限 \(A\) 使
\[
\Phi^*(L H(t))\le A\Phi(t).
\tag{6}
\]
原反射和相容给 \(\|x-y\|\le H(d(x))\)、\(d(y)\le\kappa d(x)\)。对正距离的实际输出 \(y\)，若 \(\lambda r_F(y)\le H(d(y))\)，则完整真误差界和同尺度相容合起来给 \(d(y)\le\kappa d(y)\)，矛盾。因此 (1) 成立，取 \(c=b/\lambda\)。若原定理有开集留域限制，可固定原定理允许的初值集合，取从中可由有限条原允许弧到达的点，并补上 \(S\)。老定理的一步估计和原前缀预算保证这个集合上的所有这些弧都留在原工作窗，加入的零点可驻定。这一步只用原留域预算。

为核混合闭链，可取 \(h\) 为足够大的倍数的 \(\Phi(\rho)\)，其中 \(\rho\) 是与 \(d\) 任意接近的光滑距离，梯度和二阶导数满足下文的界。选 \(0<\epsilon<(1-\kappa)/(1+\kappa)\)，则
\[
\rho(y)\le\frac{\kappa(1+\epsilon)}{1-\epsilon}\rho(x)=:\kappa'\rho(x),
\qquad
\Phi(\rho(x))-\Phi(\rho(y))\ge\frac{1-\kappa'}{(1+\epsilon)^2}\Phi(d(x)).
\]
式 (6) 保证这个下降放大一个固定倍数后支付所有原弧的代价。取该势的梯度数据，统一验证所有闭链。特别是 \(H(t)\) 与 \(t^\alpha\) 双边可比、\(0<\alpha\le1\) 时，取 \(\omega(t)=t^\alpha\)，式 (6) 直接由幂次共轭得到。这个导入保留原 RLEB 的完整纤维、允许根、初值与真正非线性模。它额外要求 (6)，并且是用原一步估计验入新判据。

**光滑距离的构造。** 取单位球内支撑的非负光滑积分核 \(\eta\)，积分为一。令 \(D(x,t)=\int d(x-tu)\eta(u)\,du\)。它对 \(x,t\) 分别为 1-Lipschitz，且 \(|D(x,t)-d(x)|\le t\)。标量压缩 \(\rho=D(x,\epsilon\rho)\) 对每个 \(x\) 有唯一非负解，并给
\[
d/(1+\epsilon)\le\rho\le d/(1-\epsilon),\qquad
\|\nabla\rho\|\le (1-\epsilon)^{-1},\qquad
\|D^2\rho\|\le C/d\quad (d>0).
\]
后两式由隐函数定理得到。对 \(t>0\) 写成变尺度卷积，各二阶核导数对常数的积分为零、\(L^1\) 范数为 \(O(t^{-2})\)，再用 \(d\) 的 1-Lipschitz 性得 \(D\) 的二阶导数为 \(O(t^{-1})\)。隐函数分母至少为 \(1-\epsilon\)。第一导数的界也直接给 \(\rho\) 全局 Lipschitz。现在 \(\Phi(\rho)\) 于 \(S\) 延零为平坦 \(C^1\)，外部梯度为 \(\omega(\rho)\nabla\rho\)。若两点距离 \(r\ge\min(d(x),d(y))/2\)，两端的梯度范数皆为 \(O(\omega(r))\)。若 \(r\) 更小，线段距 \(S\) 至少为较小距离的一半，用二阶界估计 \(\nabla\rho\) 的差。结合 \(|\omega(u)-\omega(v)|\le\omega(|u-v|)\) 及 \(\omega(d)r/d\le\omega(r)\) 对 \(r\le d\) 成立，得到梯度有全局 \(\omega\) 模。该构造不要求零集凸。

**非 Dini 的实际覆盖。** 任选上述凹模，许可其在零附近为 \(\omega(t)=1/\log(e^2/t)\)，在凹性区间外用正斜率切线延拓。取 \(0<q<1/(2\sqrt{2})\)、\(b>0\)，令 \(f(t)=\omega^{-1}(q\omega(t))\le qt\)。在 \(\mathbb R^2\) 定义完整近端映射
\[
J(u,z)=(\operatorname{sgn}(u)f(|u|),z+b\omega(|u|)),
\qquad F=(J^{-1}-I)/\lambda .
\]
它为全局同胚，原图完整单值，\(S=\{0\}\times\mathbb R\)。取足够小的半径使 \(t\le b\omega(t)\)。在条带内，弦长 \(s\) 落在 \(b\omega(t)\) 与 \(\sqrt{2}b\omega(t)\) 之间，其中 \(t=d(x)\)。因此 (1) 可取 \(c=b/(\lambda q)\)，并取 \(L=1/(\sqrt{2}b)\) 使 \(\lambda Lc>1\)。由 \(\Phi^*(\omega(t))=t\omega(t)-\Phi(t)\le\Phi(t)\) 可知 \(\Phi^*(Ls)\le\Phi(t)\)。势 \(h=(1-q)^{-1}\Phi(|u|)\) 同时支付所有原弦，其梯度有全局 \(\omega\) 模。最近输入零锚的反射范数至少为 \(2b\omega(t)\)，所以对所述非 Dini 模，这些弦没有 Dini 反射上界。这个例子核实了无 Dini 结论的适用范围。若选正斜率切线延拓并令 \(b\) 足够大使 \(t\le b\omega(t)\) 对全域成立，它也可直接通过上一节的凸点态检验。对 \(y=Jx\)，取 \(h(y)=M\Phi(d(y))\)，则 \(\lambda\langle\nabla h(y),F(y)\rangle=Mq\omega(t)(t-f(t))\ge Mq(1-q)t\omega(t)\)，取 \(Mq(1-q)\ge1\) 便足够。

<a id="feedback-original-limits"></a>
## 严格参数和覆盖的边界

**临界参数。** 取任意上述非 Dini 模，\(\lambda=L=1\) 及 \(0<q<1\)。在 \(\mathbb R\times\mathbb R^2\) 定义 \(I+F\) 将输出 \((u,z)\) 映到输入
\[
\left(u/q,\ R_{\theta(|u|,\|z\|)}z\right),\quad
\theta(t,r)=2\arcsin\left(\frac{b(t)}{2\max(1,r)}\right),
\qquad
b(t)=\sqrt{\omega(t)^2-(q^{-1}-1)^2t^2}
\]
在零附近取上式的 \(b\)，\(b(0)=0\)，向外作连续非负有界延拓使 \(b\le1\)。模非 Dini 保证 \(\omega(t)/t\to\infty\)，因而小窗内根号良定。位置半径在原步下保持不变，角度可由已知半径和法向输入唯一求回，故这是连续全域双射，原根唯一。取工作集为全部 \(S=\{0\}\times\mathbb R^2\) 加上小法向条带内的环带 \(1\le\|z\|\le2\)。在环带上 \(\|x-y\|=\omega(d(y))=r_F(y)\)，故可取 \(c=1\)。势 \(h=q(1-q)^{-1}\Phi(|u|)\) 支付共轭代价，因 \(\Phi(t/q)\ge q^{-1}\Phi(t)\) 且 \(\Phi^*(\omega(t))\le\Phi(t)\)。然而任何环带内非驻定轨道的角度每步向同一方向转动，增量趋零，总转角发散。这里用 \(d_k=q^k d_0\)、\(b(t)\sim\omega(t)\) 及非 Dini 等价于 \(\sum_k\omega(q^k d_0)=\infty\)，后者由单调性在等比分割区间上积分得到。累计角度越过每个 \(2\pi n\) 与 \(2\pi n+\pi\) 的首次误差均趋零，产生两个不同聚点。故轨道有界，但不点收敛。对允许任意凹模的判据，\(\lambda Lc>1\) 的严格性因此不可删。

<a id="feedback-critical-dini"></a>
**即使 Dini 和全域凸接触都在，临界仍失败。** 固定 \(1<p\le2\)，令 \(\omega(t)=\log(e^2/t)^{-p}\) 于足够小的正尺度，并用正斜率切线作凹的全域延拓。该模满足 Dini。定义
\[
a(t)=\Phi^*(\omega(t))/\omega(t)=t-\Phi(t)/\omega(t)\quad(t>0),\qquad a(0)=0.
\]
于是 \(0<a(t)\le t\) 且 \(a\) 非减，因为 \(a'(t)=\Phi(t)\omega'(t)/\omega(t)^2\)。模的正尾斜率保证 \(\inf_{t>0}\omega(t)/t>0\)。取 \(M>0\) 足够大使 \(a(t)/M\le\omega(t)/2\) 全域成立。对 \(y=(u,z)\) 与 \(t=|u|\) 取连续完整图
\[
F(u,z)=\left(\operatorname{sgn}(u)\,\frac{a(t)}M,\
      \sqrt{\omega(t)^2-a(t)^2/M^2}\right).
\]
取 \(\lambda=L=c=1\)、\(S=\{0\}\times\mathbb R\)、\(h(u,z)=M\Phi(|u|)\)。这里 \(r_F(y)=\omega(d(y))\) 精确成立，且 \(\langle\nabla h(y),F(y)\rangle=\Phi^*(\|F(y)\|)\)。因此全域凸接触和全部分数弦均成立。原根唯一，因为法向半径由 \(t_{\rm in}=t_{\rm out}+a(t_{\rm out})/M\) 唯一倒推，切向随后确定。

对非解初值，法向半径 \(t_k\downarrow0\)。令 \(A_k=\log(e^2/t_k)\)。分部积分或求导比较给
\[
\Phi^*(\omega(t))=p\int_0^t \log(e^2/s)^{-p-1}\,ds
           \sim pt\log(e^2/t)^{-p-1}.
\]
故 \(a(t)/t\sim p/\log(e^2/t)\)，而
\[
A_{k+1}-A_k=\log\!\left(1+\frac{a(t_{k+1})}{M t_{k+1}}\right)
              \sim\frac{p}{M A_{k+1}}.
\]
由此 \(A_{k+1}^2-A_k^2\to 2p/M\)，即 \(A_k\sim\sqrt{2pk/M}\)。每步切向位移方向相同且大小 \(\asymp k^{-p/2}\)，总和发散。这证明严格参数在产生原根的强版本中仍不可删。此例的法向一步因子趋于一，未满足原 RLEB 的固定距离收缩。

**完整的原 Dini RLEB 也不能全部导入。** 在 [C242](../../canonical/triangular_rleb.md#tri-object) 中把平方根换成 \(\ell(t)=\log(e^2/t)^{-2}\) 于足够小的正尺度，令 \(\ell(0)=0\)，再作凹的正斜率切线延拓。保持 \(F(u,z)=(u,-\ell(|u|))\) 及 \(\lambda=1\)。原根仍全域唯一，法向每步减半，完整残差至少为 \(\ell(d)\)，精确原反射模为 \(2\ell(t/2)\)。因此取真误差模 \(\psi=\ell^{-1}\) 和 \(\kappa=3/4\)。由于
\[
\ell(3t/4)-\ell(t/2)\asymp \log(e^2/t)^{-3}\gg t/2 ,
\]
缩小原半径就有 \(H(t)=t/2+\ell(t/2)\le\ell(3t/4)\)，满足原相容，且 \(H\) 满足 Dini。原轨道点收敛，但其步长是 \(\asymp(k+1)^{-2}\) 而非几何级。式 (3) 和 \(s_k\le (B+1)\omega(d_k)/L\) 会强制步长的几何上界，所以对这张完整原图，**任意另选的反馈模**和满足严格参数门的混合闭链均不能导入任何非驻定原初值。唯一原根也排除了换分支的可能。

<a id="feedback-original-variational-obstruction"></a>
## 势最小化为何不能作为必经机制

**相邻两步已可破坏所有凸加载。** 任取 \(0<q,\gamma<1\)、\(b,\lambda>0\)。令全域双射
\[
J(u,z)=(-qu,z+b\operatorname{sgn}(u)|u|^\gamma),\qquad F=(J^{-1}-I)/\lambda .
\]
\(S=\{0\}\times\mathbb R\)，每个输入有唯一原根。若 \(t=|u|\)，原步长与精确最近输入锚的反射分别为
\[
s(t)^2=b^2t^{2\gamma}+(1+q)^2t^2,\qquad
W(t)^2=4b^2t^{2\gamma}+(1+2q)^2t^2.
\]
完整真残差满足 \(\lambda r_F(Jx)=s(t)\) 且 \(d(Jx)=qt\)，可取 \(\psi(r)=q(\lambda r/b)^{1/\gamma}\)。原包络 \(H(t)=(t+W(t))/2\) 满足 \(H(t)/(bt^\gamma)\to1\)，故 \(\psi(H(t)/\lambda)/t\to q\)。任选 \(\kappa\in(q,1)\)，缩小窗口可同时满足相容、残差帽及 Dini。反射最佳幂为 \(\gamma\)，真误差界最佳幂为 \(1/\gamma\)。

任一非驻定原轨道头两步 \(x_0,x_1,x_2\) 满足
\[
\langle x_0-x_1,x_1-x_2\rangle
=-b^2q^\gamma t^{2\gamma}-q(1+q)^2t^2<0.
\]
如果要以同一个凸势在两个输出 \(x_1,x_2\) 插值梯度 \(x_0/\lambda,x_1/\lambda\)，两点凸闭链已经要求上式非负。更一般，即使允许任意标量能量 \(G\)，若这两步分别将 \(x_1,x_2\) 选为 \(G(z)+\|z-x_j\|^2/(2\lambda)\) 的全局极小点、且两处能量有限，把两条极小性用彼此输出作竞争点后相加，也得到同一非负条件。任何模、任何反馈预算都不能救这个精确加载。该障碍针对共用势的原步极小化，不排除用势认证原步。

**二次下降亦过强。** 在原 C242 上，设一个 \(C^1\) 势 \(h\) 在 \(S\) 平坦。沿任一非驻定原轨道，最近锚与迭代点趋同一点，故 \(|h(x^k)|=o(d_k)\)，由从最近锚积分且梯度连续得到。另一方面 \(\|x^k-x^{k+1}\|^2\ge d_k/2\)。所以不存在固定 \(c>0\) 使 \(h(x^k)-h(x^{k+1})\ge c\|x^k-x^{k+1}\|^2\) 沿整条尾成立。更一般，在匹配幂次 \(\omega(t)=t^\alpha\) 的剪切中，\(h\) 平坦 \(C^{1,\omega}\) 强制 \(|h|\lesssim d^{1+\alpha}\)，而步长 \(\asymp d^\alpha\)。若下降惩罚为步长的 \(p\) 次幂，必有 \(p\ge1+1/\alpha\)。混合闭链使用的正是这个共轭幂。

## 未完成的共同结构

原 PPA 的受限动力结论已由同一套混合闭链导出。分数弦版本也从闭链得到原根存在性，但要求具有合适凸子纤维及全分数弦的控制。两个定理均使用按反馈模衡量的完整真残差下界。当前没有从两类原性质推出混合闭链的一般定理，也没有从该判据分别恢复单调性和正则性。严格参数下的分块几何衰减排除了原 RLEB 中允许的慢速位移，说明即使另换反馈模，这条定理也不能充当完整的 \(M\)。若继续发展，须让闭链支付的量分辨法向误差与切向输运，或直接支付后者的累计变化，并允许可和但非几何的位移。

判据的扩张部分沿用 [C362 的已定位 Whitney 定理](gradient_feedback_general_modulus.md#feedback-modulus-cycles)。本页只据所给证明登记数学范围，公开优先性未核定。
