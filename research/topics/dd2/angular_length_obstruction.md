# 真实角度预算与不存在下有界距离势的连续完整图

沿用 [E0](core.md#dd2-exact-contract)，固定原真残差、同一最近输入锚和预设下降目标。C278 已表明严格降距和真实有限长度不保证距离势；本页在二维、精确单点零集、全域连续单值原算子与唯一完整近端中给另一种结构。真实状态含角度，单独投影到距离后会丢失可续接信息。

<a id="dd2-angular-length-obstruction"></a>
## AG1 · C457-v1 的对象与结论

**状态：derived-checked。三席已独立重构并逐式复读实际正文、身份、图边与地图，未留下致命异议。**

对每个 \(m\ge2,R>0\)，固定 \(H=\mathbb C\cong\mathbb R^2\)，共同数据为
\[
\lambda=1,\quad S=\{0\},\quad U=V_\psi=H,\quad
D_\psi=[0,\infty),\quad
\psi_m(\rho)=\rho^{1/m},\quad\Phi=0,\quad
\varphi_m=(a\mapsto\sqrt{a^2+a^{2m}})^{-1}.
\tag{AG1}
\]
以下定义一个全域同胚 J，并取完整 \(F=J^{-1}-I\)。F 全域连续单值，完整近端恰为 J，精确零集为 S，零输入驻定，所有 R 距离窗不变。每个输出满足
\(\rho=s=a^m,\ a=\psi_m(\rho)\)。

对这个同一图，每个实际输入尺度 \(t>0\) 都有
\[
\min\langle x-y,y\rangle=0,\qquad
\max a=\varphi_m(t),\qquad
\min s=\chi_\Sigma(t),\quad
\chi_\Sigma=(\operatorname{id}+\psi_m)^{-1},
\tag{AG2}
\]
其中极值遍历该图半径 t 的全部输入；前两项在同一条边取等。
原误差模在全输出域逐点最小。因此原 \(\Phi\)、原 \(\psi_m\) 和预设目标均不能在各自的纯尺度意义上再加强。

尽管 \(\int_0^\epsilon t/\chi_\Sigma(t)\,dt=\infty\)，而且任何有限非负距离势（更一般，在 \((0,R]\) 有共同有限下界的有限实值势）都不能以统一有限正常数支付全部边，所有真实轨道却有限长，且
\[
\sum_{j\ge k}s_j\le(1+\theta_k)t_k
\le(1+2\pi)t_k\longrightarrow0 .
\tag{AG3}
\]
这里 \(\theta_k\in[0,2\pi)\) 是实际轨道的一致主角度，\(x^k=0\) 时约定 \(\theta_k=0\)。无下界实值势不在不可能性结论内，AG7 另给明确支付例。
这既不否定 C420/C454 的全数据类必要性，也不声称上述常数最优。

## AG2 · J 的实际定义

对 \(\theta\in\mathbb R\) 令
\[
\beta(\theta)=\frac{\pi}{4}(1-\cos\theta).
\tag{AG4}
\]
它为 \(2\pi\) 周期函数，\(0\le\beta\le\pi/2\)，
\(|\beta'|\le\pi/4<1\)，\(\beta(0)=\beta(2\pi)=0\)，\(\beta(\pi)=\pi/2\)。
对输入 \(x=t e^{i\theta}\ne0\)，唯一求 \(a>0\) 满足
\[
t^2=a^2+2a^{m+1}\cos\beta(\theta)+a^{2m}.
\tag{AG5}
\]
右侧关于 a 连续严格增，从0趋于无穷，因为 \(\cos\beta\ge0\)。置
\[
v=a^{m-1},\qquad
\alpha(a,b)=\arg(1+v e^{ib}),\qquad
Jx=a e^{\,i[\theta-\alpha(a,\beta(\theta))]},\quad J0=0 .
\tag{AG6}
\]
所用 \(b\in[0,\pi/2]\)，复数实部至少1，所以主辐角无分支跳。
公式按周期识别角端点，不因选择 \(\theta\) 或 \(\theta+2\pi\) 改变 J。
由定义还有
\[
a\le t\le a+a^m .
\tag{AG7}
\]

## AG3 · 全局可解性、接缝与连续反演

对固定 \(a>0\)，直接微分得
\[
0\le\partial_b\alpha(a,b)
=\frac{v\cos b+v^2}{1+2v\cos b+v^2}<1 ,
\tag{AG8}
\]
因为分母减分子为 \(1+v\cos b>0\)。结合 \(\alpha(a,0)=0\)，有
\(0\le\alpha(a,b)\le b\)。令
\[
G_a(\theta)=\theta-\alpha(a,\beta(\theta)).
\]
则
\[
G_a'(\theta)\ge1-\pi/4>0,\quad
G_a(0)=0,\quad G_a(2\pi)=2\pi,\quad
G_a(\theta+2\pi)=G_a(\theta)+2\pi .
\tag{AG9}
\]
所以 \(G_a\) 给圆上的连续严格保序双射。

给定非零输出 \(y=a e^{i\eta}\)，先唯一反解输入角
\(\theta=G_a^{-1}(\eta)\)，再由 AG5 唯一恢复 t 和 x。径向根连续：参数收敛时根由 \(0\le a\le t\) 有界，任一子列极限满足同一个唯一根方程，故全列收敛。圆角映射亦连续，所以 J 在非零处连续；AG7 给原点连续。
逆也连续：若 \(y_n\to y\)，AG7 使唯一前像 \(x_n\) 有界，二维中任意收敛子列的极限由 J 连续和前像唯一性只能为 \(J^{-1}y\)，故全列收敛。此论证含零点；等价地，原点直接用 \(t\le a+a^m\to0\)。
因此 J 是全空间同胚，\(F=J^{-1}-I\) 是全域连续单值原算子，且
\(I+F=J^{-1}\) 保证完整近端确实就是 J，没有额外根或遗漏前像。

## AG4 · 完整真残差、原目标和精确尺度信息

写 \(\eta=\theta-\alpha(a,\beta(\theta))\)。AG5–AG6 共同给
\[
x=y[1+a^{m-1}e^{i\beta(\theta)}],\quad
x-y=a^m e^{i(\eta+\beta(\theta))}.
\tag{AG10}
\]
因此完整单值纤维确实满足
\[
\rho=s=a^m,\quad a=\psi_m(\rho),\quad
\langle x-y,y\rangle=a^{m+1}\cos\beta(\theta)\ge0 .
\tag{AG11}
\]
正 a 时 \(s>0\)，故精确 \(\operatorname{zer}F=\{0\}\)；J0=0 给零驻定。
对任意同一原数据的 E0 边，\(a^m\le\rho\le s\) 和零锚能量给
\(a^2+a^{2m}\le t^2\)。所以预设 \(\varphi_m\) 由原数据认证，不只是该固定图碰巧实现的曲线。

在输入角 \(\theta=\pi\) 上，\(\beta=\pi/2\)，同一边恰有
\[
a=\varphi_m(t),\quad s=a^m,\quad
\langle x-y,y\rangle=0 .
\tag{AG12}
\]
这证明 AG2 的最小锚和最大输出，且对每个正尺度取到。
所有边的 \(t\le a+a^m\) 又给
\(a\ge(\operatorname{id}+(\cdot)^m)^{-1}(t)\)，所以 \(s\ge\chi_\Sigma(t)\)；
输入角0恰取等。因此最小真实步就是 \(\chi_\Sigma\)，任何正可测有效实际步下界的同类积分也发散。

J 满射，每个输出半径 a 都能实现；原 \(\rho=a^m\) 遍历 \([0,\infty)\)，因此任何全输出真误差模都逐点不小于 \(\psi_m\)。在固定 R 输入窗，角 \(\pi\) 实现所有 \(0<a\le\varphi_m(R)\)，零输出由 \(J0=0\) 实现，故局部取等范围也明确。
这些精确性均属于这个固定图的相应对象，不把它们混成每条轨道逐步都取等。

## AG5 · 实际角度预算支付全部轨道

对 \(\theta\in[0,2\pi]\)，由 \(\beta(0)=0\) 及 \(\beta'\le\pi/4\) 得
\(\beta(\theta)\le(\pi/4)\theta\)。
结合 \(0\le\alpha\le\beta\)，实际输出主角度
\[
\eta=\theta-\alpha(a,\beta(\theta))
\quad\text{满足}\quad
0\le(1-\pi/4)\theta\le\eta\le\theta .
\tag{AG13}
\]
从 \(\theta_0\in[0,2\pi)\) 开始，后继始终在这一相同角度区间，不绕过接缝；正实轴选择角0并保持。

三角不等式及单位圆的弦长不超过相应角差给每条实际边
\[
s=|te^{i\theta}-ae^{i\eta}|
\le t-a+a|e^{i\theta}-e^{i\eta}|
\le t-a+a(\theta-\eta).
\tag{AG14}
\]
定义真正依赖位置的状态势
\[
V(0)=0,\qquad
V(te^{i\theta})=t(1+\theta)\quad(t>0,\ 0\le\theta<2\pi).
\tag{AG15}
\]
它在正实轴的角接缝处不连续，但 \(t\le V(x)\le(1+2\pi)t\)，零端归零。
由 \(\theta\ge\eta\) 且 \(t\ge a\)，
\[
V(x)-V(y)
=t-a+a(\theta-\eta)+(t-a)\theta
\ge s .
\tag{AG16}
\]
因此同一实际路径上 V 望远镜，给长度预算 \(V(x^0)\)。

零缺陷能量还给 \(t_k^2-t_{k+1}^2\ge t_{k+1}^{2m}\)。
如果距离有正极限，右侧最终有固定正下界，矛盾；故 \(t_k\to0\)，实际点趋零，\(V(x^k)\to0\)，得到 AG3 的尾界。
全部输入覆盖、距离窗不变、原真残差及零输入均已由完整图核实。这里的单一实际状态势不是距离势，后续边必须继承前一步的真实角度。

## AG6 · 精确距离投影不能支付全部边

设存在有限实值 \(\Theta:[0,R]\to\mathbb R\)、固定 \(0<C<\infty\)，且
\(\inf_{0<t\le R}\Theta(t)>-\infty\)，使全部真实边满足
\(s\le C[\Theta(t)-\Theta(a)]\)。
任选 \(u_0\in(0,R]\)，构造纯尺度序列
\[
u_{k+1}=\varphi_m(u_k),\qquad
\sigma_k=u_{k+1}^m .
\tag{AG17}
\]
AG12 保证每一条 \((u_k,u_{k+1},\sigma_k)\) 都属于这个同一固定图的准确距离—步长投影。
该序列的 \(u_k\downarrow0\)，而 [FG18](finite_length_countermodels.md#dd2-sharp-gauge-finite-length-pair) 的逐壳直接计算给
\[
2\int_{u_{k+1}}^{u_k}u^{1-m}\,du\le\sigma_k,\qquad
\sum_{k\ge0}\sigma_k=\infty .
\tag{AG18}
\]
逐项套假定的距离支付式再望远镜，却得到共同有限预算
\(C[\Theta(u_0)-\inf_{(0,R]}\Theta]\)，矛盾。

正尺度取等 \(a=\varphi_m(t)\) 在 AG5 中强制 \(\cos\beta(\theta)=0\)，故输入角只能是 \(\pi\) 模 \(2\pi\)。该伪链不是实际轨道：当真实输入角为 \(\pi\) 且半径正时，输出角
\(\pi-\alpha(a,\pi/2)<\pi\)，下一实际步不能重置成角 \(\pi\)。
所有实际轨道有限长度与其精确距离投影包含不可和伪链同时成立；不能用投影的坏链冒充真实坏轨道。
因此所有有限非负距离势、在零有有限极限的有限距离势等均被排除，但依赖真实位置的 V 完全有效。

## AG7 · 无下界的实值势为何不被排除

对固定 R，\(\chi_\Sigma\) 连续非减且在 \((0,R]\) 为正。定义
\[
W_R(t)=2\int_R^t\frac{u}{\chi_\Sigma(u)}\,du\quad(0<t\le R),
\qquad W_R(0)=0 .
\tag{AG19}
\]
每个正点的积分有限，但由 \(m\ge2\) 有 \(W_R(t)\to-\infty\)。
每条正边的 \(s\ge\chi_\Sigma(t)\) 与 \(t^2-a^2\ge s^2\) 给
\[
W_R(t)-W_R(a)
=2\int_a^t\frac{u}{\chi_\Sigma(u)}\,du
\ge\frac{t^2-a^2}{\chi_\Sigma(t)}
\ge s .
\tag{AG20}
\]
正输入不跳到零，零输入仅有零边，故这个有限实值函数确实支付全图；它没有有限下界，不能提供长度预算。这精确限制了 AG6 的否定量词，不把 C278 更强的“任何有限实值距离势”结论冒名移用。

本例不认定公开新颖性，不为一般算法或非精确迭代提供自动保证。它记录一个完整连续对象：每尺度的原锚、原模、原目标及最小真实步都已精确，真实角度预算仍是单纯距离证书没有包含的信息。C420/C454 的同数据统一类保留另一个真正无限长旋转；本固定好图不反驳其必要性。
