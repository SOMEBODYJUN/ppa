# 直线调节与跨轴不确定性：完整近端及经典边界

本页 C271-v1 是一个比tomography更短的**控制设计基准**：恢复法向误差时，执行器可将未知有界比例的命令混入自由切向通道。它不是已映射的实测设备，也不是普通优化solver。完整鲁棒RLEB证书成立；同一算法另有更短的全域经典机械能证明，因此不能承担“旧分析方法无法处理”的强应用主例。

<a id="acr-object"></a>
## 模型、算法、完整零集

物理空间 $X=\mathbb R^2\times\mathbb R^2$，位置 $z=(z_t,z_n)$、动量 $p$，基向量为 $e_t,e_n$。法向恢复势 $V(z)=2|z_n|^{3/2}/3$；数字控制器使用非二次虚拟动能 $k(p)=2\|p\|^{3/2}/3$。记

\[
g(r)=\operatorname{sign}(r)\sqrt{|r|},\quad h(p)=p/\sqrt{\|p\|}\ (p\ne0),\quad h(0)=0.
\]

固定 $\Gamma=10$、$A=1+\Gamma=11$、$\lambda=1$，相对跨轴增益 $\delta\in[-1,1]$。完整不确定算子为

\[
F(z,p)=\{(-h(p),10p+g(z_n)(e_n+\delta e_t)):\delta\in[-1,1]\},
\quad S=F^{-1}(0)=\{(s e_t,0):s\in\mathbb R\}.
\tag{AC1}
\]

$S$ 闭、非孤立且是完整零集：第一分量强迫 $p=0$，第二分量的法向分量强迫 $g=0$。输入域全 $X$，完整普通关系 $J=(I+F)^{-1}$，而非极小支选择。每步可先选任意固定增益 $\delta_k$ 再取其完整隐式输出；也可使用后述连续状态律的全部根。所有转移均属于同一原 $J$。

等价的union参数 $e=\beta|g|$、$|\beta|\le1$ 给同一 $F$，但固定 $\beta$ 与固定 $\delta$ 是不同模式，不能跨符号混用。恢复力为凸势梯度，含切向泄漏的总力一般不是势场；力与恢复梯度正交的部分不等于对速度被动。

<a id="acr-fiber"></a>
## 全输入、全部纤维和零动量反算

任意输入 $w=(a,b)$、固定 $\delta$，令

\[
p_\delta(q)=\frac{b-q(e_n+\delta e_t)}A,\qquad
\Phi_\delta(q)=q|q|-a_n-h_n(p_\delta(q)).
\tag{AC2}
\]

完整模式纤维恰为 $p=p_\delta(q)$、$z=a+h(p)$，其中 $\Phi_\delta(q)=0$；此时 $z_n=q|q|$、$g(z_n)=q$。这个身份双向成立，包括 $p=0$。不能把方程乘以 $\sqrt{\|p\|}$ 后沿用为完整反算：在 $p=0$ 时乘后方程会出现未满足 $a_n=q|q|$ 的伪根。

$\Phi$ 连续，$q\to\pm\infty$ 时 $q|q|$ 支配 $h_n(p)=O(\sqrt{|q|})$，故IVT给每个模式、每个输入真实根。更强，根唯一：对 $P=\|p\|>0$、$\nu=p/P$，

\[
\frac d{dq}h_n(p_\delta(q))
=-\frac1{A\sqrt P}\left[1-\frac{p_n(p_n+\delta p_t)}{2P^2}\right]<0.
\tag{AC3}
\]

括号至少 $(3-\sqrt2)/4>0$，来自对称矩阵 $\bigl(\begin{smallmatrix}1&\delta/2\\\delta/2&0\end{smallmatrix}\bigr)$ 的最大特征值 $(1+\sqrt{1+\delta^2})/2$。至多一个 $p=0$ 点，连续拼接保留严格增的 $\Phi$。因此每个固定模式完整纤维singleton。

原union的全部纤维是 $\delta\in[-1,1]$ 对应的这些唯一输出，无遗漏远根；下节界给模式统一有界，根随参数连续，故完整纤维紧、连通。若 $a_n+h_n(b/A)=0$，所有模式的根均为 $q=0$、纤维坍缩为一个输出；否则全部 $q$ 同符号且非零，不同增益对应不同输出，原完整纤维是真实连续多值弧。

**连续状态律。** 给定连续 $\delta(z,p)\in[-1,1]$，消去 $z=a+h(p)$ 后，完整根满足
$A p+g(a_n+h_n(p))(e_n+\delta(a+h(p),p)e_t)-b=0$。其与 $p$ 的内积至少
$A P^2-BP-\sqrt2P\sqrt{|a_n|+\sqrt P}$，$B=\|b\|$，大球边界严格向外。Brouwer零点原理给全输入coverage；全部根仍在原union。跨步任意这样的律都可使用共同证书；不宣称任意不连续预定状态律有根。

<a id="acr-residual"></a>
## 完整真残差与同窗误差界

记 $P=\|p\|$、$G=|g(z_n)|$。原union的真残差是

\[
\rho(z,p)^2=P+(g(z_n)+10p_n)^2+
\bigl(\max\{|10p_t|-G,0\}\bigr)^2.
\tag{AC4}
\]

这是对全部增益区间的真正inf，不是某选中模式的残差。单模式残差只给它的上界。物理距离为 $d(z,p)=\sqrt{|z_n|^2+P^2}=\sqrt{G^4+P^2}$。

由 $P\le\rho^2$、$G\le\rho+10P$，有

\[
d\le G^2+P\le\rho^2+20\rho P+100P^2
\le(1+10\rho)^2\rho^2.
\tag{AC5}
\]

第二步使用 $P+(g+10p_n)^2\le\rho^2$，而不重复计入一份 $P$。所以在整个物理空间的 $\rho\le.006$ 窗，$d\le1.1236\rho^2\le1.6\rho^2$，$\rho>0$时第二项可严格。零残差给真实 $S$；无输出先留域前件。

<a id="acr-certificate"></a>
## 所有根、最近零锚和同一组常数

置输入距离 $d=\sqrt{a_n^2+B^2}$。任意真实根的法向方程与 $z_n=g|g|$ 给
$G\le|b_n|+A\sqrt P|a_n|$（$P=0$亦成立）。于是

\[
P\le cB+\sqrt2\sqrt P|a_n|,\qquad c=(1+\sqrt2)/11,
\quad P^2\le(c^2+2P)d^2,
\quad P\le d^2+d\sqrt{c^2+d^2}.
\tag{AC6}
\]

这是每个全空间根的界，未先假设输出邻近 $S$。当 $0<d\le R=10^{-4}$，$P<.221d$，$G\le\sqrt{1+121R}\,d$，$|z_n|\le1.0121d^2$。$d=0$ 时 AC6强迫 $P=G=0$，整个完整零纤维吸收。

唯一物理最近锚为 $p_0=(a_t e_t,0)$，$\|w-p_0\|=d$。全部 $d>0$ 转移满足

\[
\|2y-w-p_0\|^2
\le4P+4\sqrt P d+d^2+(2P+B)^2
\le[.884+4\sqrt{.221R}+(1+1.442^2)R]d<d.
\tag{AC7}
\]

$d=0$时完整吸收给反射恰零，统一使用界 $\|2y-w-p_0\|\le\sqrt d$。锚定RL的作用域准确为 $\{(y,\xi)\in\operatorname{gph}F:y+\xi\in U_R\}$ 对其同一个输入最近零图点 $(p_0,0)$；不是任意两个非零图点的全对RL。完整普通关系与该graph-block双向对应，没有删支。

取 $U=X$、$R=10^{-4}$、$\gamma=1/2$、$L=1$、$\bar t=.006$、$\psi(t)=1.6t^2$、$\kappa=1/2$。AC2–7对每个 $U_R$ 输入及全部输出供应coverage、同锚和真实EB。定义

\[
K(t)=(t+\sqrt t)/2,\quad K(R)=.00505<\bar t,
\quad\psi(K(t))\le.40804t\le\kappa t,
\quad\Theta(t)=t+\frac{\sqrt t}{2(1-1/\sqrt2)}.
\tag{AC8}
\]

$U$补集为空，严格预算对每个输入自动成立；[C02-v3](true_residual_selection_rleb.md#trs-theorem)或C249的准确Id特例给全部轨道无限延拓、留 $U_R$、有限长度并趋 $S$。所有模式、连续状态律及其全部根共享同一组常数；极限可随选择不同。

<a id="acr-sharp"></a>
## 锐局部系数、指数和精确轨道子族

由 $p_n=\sqrt P(z_n-a_n)=O(d^{3/2})$、$p_t=(b_t-\delta b_n)/A+\delta p_n$，最坏缩管距离因子为 $\sqrt2/11$。输入 $a_n=0$、$b=t(-e_t+e_n)/\sqrt2$、模式 $\delta=1$ 时 $g=b_n+O(t^{5/2})$、$P/t\to\sqrt2/11$，取得此因子。AC7的精确反射平方为 $4P+O(d^2)$，所以最小渐近半阶锚常数为 $2\sqrt{\sqrt2/11}$；有限窗不把渐近常数当作已达到的统一常数。

AC5使真实平方EB的最佳渐近系数为1；$z_n=0,p=P e_t$ 给 $d/\rho^2=1/(1+100P)\to1$，且排一切幂 $q>2$。系数1本身不是有限窗已有效的宣告，保留1.6安全窗。

当 $a_n=b_n=0$，所有模式的完整输出相同：$p=(b_t/11)e_t$、$z=a+\operatorname{sign}(b_t)\sqrt{|b_t|/11}\,e_t$。真实解输入的完整prox最佳点态指数为 $1/2$。沿这个完整子族，

\[
b_{t,k}=11^{-k}b_{t,0},\qquad
a_{t,k}=a_{t,0}+\operatorname{sign}(b_{t,0})\sqrt{|b_{t,0}|}\sum_{j=1}^k11^{-j/2},
\tag{AC9}
\]

极限由该几何和闭式给出。一般完整多值轨道没有闭式；完整映射由AC2的唯一标量逆给出。这里不认证全输入对Hausdorff最佳指数。

还有政策依赖的精确终点：初始动量为零、固定相对增益 $\delta$ 时，全部动量始终平行 $\delta e_t+e_n$，故位置不变量 $z_t-\delta z_n=a_{t,0}-\delta a_{n,0}$。全域正面给法向和动量归零，所以终点切向坐标恰 $a_{t,0}-\delta a_{n,0}$。当初始法向误差非零，不同固定增益已给一整段不同极限；这不宣称该段就是全部时变政策的极限集合。固定 $\beta|g|$ 模式不能跨符号继承这个不变量。

<a id="acr-critical"></a>
## 参数边界：零吸收不等于收敛

只在本节另绑定 $\Gamma\in\mathbb R$、$A=1+\Gamma$，其余 $g,h$、增益区间、$S$ 和 $\lambda=1$ 保持，算子记 $F_\Gamma$。完整零输入吸收恰为 $A>0$：$b=0$ 给 $Ap+g(e_n+\delta e_t)=0$，$a_n=0$ 又要求 $z_n=h_n(p)$ 与 $g$ 同号；$A>0$ 时除零外符号相反，故只有原零输出。

$A=0$ 时完整零纤维为 $p=p_t e_t$ 任意、$z=a+h(p)$，法向零；法向输入动量 $b_n=0$、$b_t\ne0$ 时根不存在，全输入coverage也失败。$A<0$ 时完整零纤维除原零外，恰为下述两条曲线：$\sigma\in\{\pm1\}$、$\delta\in[-1,1]$，$Q_\delta=\sqrt{1+\delta^2}$、$G=(|A|Q_\delta)^{-1/3}$，

\[
z=a+\sigma G^2(\delta e_t+e_n),\qquad
p=\frac{\sigma G}{|A|}(\delta e_t+e_n).
\tag{AC12}
\]

原方程先固定 $p$ 方向，位置法向再给 $G^2=\sqrt{G/(|A|Q_\delta)}$，穷尽非零根。$A\ne0$ 时每个固定模式全输入至少有根，仍由AC2的连续原方程IVT得到；$A<0$ 不继承唯一性。

当 $0<A\le1$，取初始非零切向动量 $p^{\mathrm{init}}$，自由轨道的动量为 $A^{-k}p^{\mathrm{init}}$，位置步同号且不趋零；当 $-1\le A<0$，同一自由支动量等幅交替或增长，也不收敛。$A=0$ 的全输入coverage已失败。对 $A<-1$，再取 $\delta=0$、$G=[4(-A-1)]^{-1/3}$、$r=G^2$、$p_n=4G^4$，两状态 $\pm(z=r e_n,p=p_n e_n)$ 互为完整输出：$\sqrt{p_n}=2r$，$(A+1)p_n=-G$，逐式成立。因此所有 $\Gamma\le0$ 都有全域结论的真实反证，而不只用零吸收失败推不收敛。

$\Gamma>0$ 是全空间全部初值/政策收敛的必要门；本页不判每个正 $\Gamma$ 充分。主证书及全域正面仍固定 $\Gamma=10$，不得从渐近 $\sqrt2/A$ 门偷换成完整参数收敛iff。

<a id="acr-classical"></a>
## 全域经典正面：不能强推荐

同一自然机械能 $E=V+k$ 对任意输入、任意完整根和任意增益有

\[
E(w)-E(y)=D_V(a_n,z_n)+D_k(b,p)+10P^{3/2}
+\delta g(z_n)p_t/\sqrt P.
\]

$P=0$ 时按原式或连续极限处理。$G\le B+11|p_n|$，$|p_n p_t|\le P^2/2$，以及
$D_k\ge2B^{3/2}/3+P^{3/2}/3-B\sqrt P$，给

\[
E(w)-E(y)\ge\tfrac23B^{3/2}+\tfrac{29}6P^{3/2}-2B\sqrt P
\ge\tfrac19B^{3/2}+\tfrac56P^{3/2}.
\tag{AC10}
\]

最后用 $2u-(5/9)u^{3/2}\le96/25<4$。此证明不借AC6/7。任意全空间初值的能量单调，$\sum B_k^{3/2}\le9E_0$，故 $B_k\to0$；$G_{k+1}\le B_k+11B_{k+1}\to0$，所以 $E_k\to0$。

又 $G\le B+11P$、AC10及 $(u+v)^3\le4(u^3+v^3)$ 给 $E_{k+1}\le.8E_k+5118E_k^2$。每条轨道最终进入 $E\le(4/3)10^{-6}$，之后 $E_{k+1}\le.81E_k$（正能量时严格，零能量完整驻定）。物理步 $\le\sqrt P+B+P$ 是该能量的 $1/3$、$2/3$幂之和，尾部可和，有限早前缀也有限。因此**全部初值、全部完整选择全域有限长度**。这个经典正面比局部RLEB范围更强；它为本轮推导，不假称某旧论文已有同式结果。

<a id="acr-energy-contract"></a>
## 具体共同能量合同仍确实失败

在本节固定开集 $O\supset U_R$；由已证完整留窗，全部输出也在 $O$。H1要求同一个 $\alpha>0$ 对每个 $w\in U_R$、每个 $y\in J(w)$ 有 $E(w)-E(y)\ge\alpha\|w-y\|^2$。H2要求同一个有限 $C\ge0$ 对上述全部转移存在 $\xi_y\in\partial_LE(y)$，使 $\|\xi_y\|\le C\|w-y\|$。强链式要求：对 $O$ 内每条AC曲线 $\eta$，在一个共同零测集外，对全部 $\xi\in\partial_LE(\eta(t))$ 都有 $(E\circ\eta)'(t)=\langle\xi,\eta'(t)\rangle$。下面两种能量都定义于该同一个 $O$。

若 $E$ 为一个共同 $C^1$ 单状态能量，要求对所有 $U_R$ 完整转移有 $E(w)-E(y)\ge\alpha\|w-y\|^2$、$\alpha>0$，已经不可能。取自由切向弦 $\ell$，$p=\ell|\ell|e_t$，输入 $w=(s e_t,11p)$、输出 $y=((s+\ell)e_t,p)$。H1除以 $|\ell|$ 并取双符号极限强迫 $\partial_tE(s,0)=0$，故 $E|S$ 常数。再仅沿动量方向Taylor，除以 $\ell^2$，下降商趋 $10\operatorname{sign}(\ell)\partial_{p_t}E(s,0)$；两个符号不能都至少为 $\alpha$。

对于有限locLip、满足全部limiting次梯度强链式法则的共同能量，H1加所选limiting-H2也不可能。零转移H2给 $0\in\partial_LE|S$，强链式使 $E|S$ 常数。每个小切向动量 $p$ 的真实前驱为 $(s e_t-h(p),11p)$，H2给一个次梯度范数 $O(\sqrt{\|p\|})$；沿纯动量段，强链式对这个值也成立，积分给 $|E(s e_t,p)-E|S|=O(\|p\|^{3/2})$，统一于 $s$。同样对输入的 $11p$使用其前驱（需 $121\|p\|\le R$），H1下降量只能 $O(\|p\|^{3/2})$，而步长平方至少 $\|p\|$，矛盾。

这包括已核可定义/Whitney-locLip类，负面由自由切向惯性触发，不证明跨轴不确定性本身独创此分离。AC10的非二次正面和[C266人工KL桥](generic_power_kl_bridge.md#gpk-contract)均保留；不得宣称整个ABS/KL或所有经典能量被排除。

<a id="acr-metric"></a>
## 正定GPPA度量也不能默认保持结论

保持原F，定义 $J^M=(M+F)^{-1}M$，$M$在 $(z_t,p_t)$ 块为 $\bigl(\begin{smallmatrix}1&-1/2\\-1/2&1\end{smallmatrix}\bigr)$，法向块为Id。$M\succ0$，$\operatorname{Fix}J^M=S$，但完整零输入纤维**恰三点**：零和

\[
\pm(z_t=88/1849,\ z_n=0,\ p_t=4/1849,\ p_n=0).
\tag{AC11}
\]

法向方程 $z_n=h_n(p)$、$11p_n+g(z_n)=0$先强制 $p_n=z_n=0$；自由方程再给 $(11-1/4)p_t=h_t/2$，穷尽三根。真实残差在这些输出按AC4评价，不因Fix身份而变零。

还存在完整合法不收敛轨道：$p_t=1/400$、$p_n=z_n=0$，每步 $z_{t,k+1}=z_{t,k}+1/20$。直接代入 $M(w-y)=F(y)$ 两自由分量为 $(-1/20,1/40)$，完全相等；反馈此时全坍缩为零。这是否定全部输出收敛本身。

新度量每个固定模式仍有全输入coverage：消去位置后，动量方程为 $(10.75p_t-.5h_t+\delta g,11p_n+g)=(.75b_t,b_n)$、$g=g(a_n+h_n(p))$；正线性动量项在大球支配 $\sqrt P$ 和 $P^{1/4}$项，Brouwer给根。存在、Fix、原真残差和全部输出分别核过，正定性不能修复零输入多值或实际漂移。任意时变度量未获认证。
