# 有限数据代理：同一 QP、全局映射与覆盖证书的自足证明

本页给 [C19](../../CLAIMS.md) 与 [C20-v2](../../CLAIMS.md#c20-v2) 的完整论证。
固定有限样本，所有查询共享同一个映射；没有逐查询任选球交点，也不调用 C03 的无限图扩张或 C04 的 degree/纤维分类。
来源稿已有这些结论，本页重建证明，不主张新颖性。值域覆盖 C18 是另一条尚待验收的链。

<a id="fd-object"></a>
## FD-OBJECT · 固定对象和参数

固定整数 \(n,m\ge1\)、\(\lambda>0\)、\(0<\sigma<1\)、\(a>0\) 及
\((x_i,v_i)\in\mathbb R^n\times\mathbb R^n\)，\(1\le i\le m\)。置
\[
p_i=x_i+\lambda v_i,\quad c_i=x_i-\lambda v_i,\quad
P=[p_1\ \cdots\ p_m],\quad V=[c_1\ \cdots\ c_m].
\]
样本兼容条件为
\[
\|c_i-c_j\|^2\le\sigma^2\|p_i-p_j\|^2+2a^2
\qquad(1\le i,j\le m). \tag{FD-1}
\]
同一组样本和这些固定参数定义
\[
\begin{aligned}
Q&=\sigma^2P^TP+V^TV+a^2I_m,\\
d_i(q)&=\sigma^2\|p_i\|^2-\|c_i\|^2-4\sigma^2\langle p_i,q\rangle,\\
\Delta_m&=\{\theta\in\mathbb R^m:\theta_i\ge0,\ \sum_i\theta_i=1\},\\
\Phi_q(\theta)&=\theta^TQ\theta+d(q)^T\theta,\\
\theta(q)&=\arg\min_{\theta\in\Delta_m}\Phi_q(\theta),\qquad
N_m(q)=V\theta(q).
\end{aligned} \tag{FD-2}
\]
这里 \(q\in\mathbb R^n\) 是查询的 Cayley 参数，\(Q\) 是矩阵，\(V\) 是样本列矩阵；它们不是其它主题中的指数或活跃空间。

C19 的参数是 \(a^2=M_\sigma/2\)。若另给 \(L>0,0<\gamma<1\)，全对 Hölder 样本自动满足 FD-1，因为
\[
\begin{aligned}
R&=L^{1/(1-\gamma)},\\
M_\sigma&=\sup_{t\ge0}\{L^2t^{2\gamma}-\sigma^2t^2\}\\
&=(1-\gamma)\gamma^{\gamma/(1-\gamma)}
 R^2\sigma^{-2\gamma/(1-\gamma)}>0.
\end{aligned} \tag{FD-3}
\]
证明：正临界点满足 \(t^{2(1-\gamma)}=\gamma L^2/\sigma^2\)；
函数在此之前增、之后减，代入即得显示值，原点为零且无穷远趋负无穷。
FD-1 本身只要求有限样本兼容，不假设未观测原图已满足 RL。

<a id="fd-qp"></a>
## FD-QP · 唯一解和同一个全局 \(\sigma\)-Lipschitz 映射

\(\Delta_m\) 非空紧，目标连续；\(Q\succeq a^2I_m\) 且 \(a>0\)，
故极小解存在唯一。对任何可行 \(\xi\)，极小解满足
\[
\langle2Q\theta(q)+d(q),\,\xi-\theta(q)\rangle\ge0. \tag{FD-4}
\]
反过来，因目标凸，此条件也充分：精确展开目标差，余项为非负的
\((\xi-\theta)^TQ(\xi-\theta)\)。

取两个查询 \(q,r\)，记 \(h=q-r\)、\(\delta_\theta=\theta(q)-\theta(r)\)。
在两个 FD-4 中互用对方的解，相加并用
\(d(q)-d(r)=-4\sigma^2P^Th\)，得到
\[
\delta_\theta^TQ\delta_\theta\le2\sigma^2\langle P\delta_\theta,h\rangle.
\]
将平方项移项并配方：
\[
\|V\delta_\theta\|^2+\sigma^2\|P\delta_\theta-h\|^2+a^2\|\delta_\theta\|^2
\le\sigma^2\|h\|^2. \tag{FD-5}
\]
所以 \(\|N_m(q)-N_m(r)\|\le\sigma\|q-r\|\)，对所有查询同时成立。
这一步不需要 FD-1；FD-1 用于下一步与样本的交叉估计。

<a id="fd-cross"></a>
## FD-CROSS · 有限抬升插值和每个样本的交叉界

在 \(E=\mathbb R^n\oplus\mathbb R^m\) 中取标准正交基 \(e_i\)，令
\[
z_i=(p_i,(a/\sigma)e_i),\qquad Z=[z_1\ \cdots\ z_m].
\]
则 \(Q=\sigma^2Z^TZ+V^TV\)。对每个 \(z\in E\)，用同一 \(Q,\Delta_m\)、
系数
\[
d_i^E(z)=\sigma^2\|z_i\|^2-\|c_i\|^2-4\sigma^2\langle z_i,z\rangle
\]
定义唯一解 \(\theta_z\) 和 \(\widetilde N(z)=V\theta_z\)。
在 \(z=(q,0)\) 时 \(d_i^E(z)=d_i(q)+a^2\)，
新增项在单纯形上为常数，故 \(\theta_{(q,0)}=\theta(q)\)。
对 \(z,w\in E\)，记 \(\Delta=\theta_z-\theta_w\)。同样的两条变分不等式给
\[
\Delta^TQ\Delta\le2\sigma^2\langle Z\Delta,z-w\rangle,\qquad
\|V\Delta\|^2+\sigma^2\|Z\Delta-(z-w)\|^2\le\sigma^2\|z-w\|^2.
\]
这里 \(Q=\sigma^2Z^TZ+V^TV\)，\(a^2\|\Delta\|^2\) 已在 \(Z\) 项内，
不能再次相加。于是
\(\|\widetilde N(z)-\widetilde N(w)\|\le\sigma\|z-w\|\)。

在 \(z=z_j\) 取可行顶点 \(e_j\)。它的梯度第 \(i\) 项与第 \(j\) 项之差恰为
\[
[2Qe_j+d^E(z_j)]_i-[2Qe_j+d^E(z_j)]_j
=\sigma^2\|z_i-z_j\|^2-\|c_i-c_j\|^2. \tag{FD-6}
\]
\(i=j\) 时为零；\(i\ne j\) 时
\(\sigma^2\|z_i-z_j\|^2=\sigma^2\|p_i-p_j\|^2+2a^2\)，
FD-1 保证非负。对任意 \(\xi\in\Delta_m\)，梯度与 \(\xi-e_j\)
的内积就是这些非负差的凸组合。因此 \(e_j\) 满足最优条件；
唯一性给 \(\theta_{z_j}=e_j\)、\(\widetilde N(z_j)=c_j\)。
比较 \(z_j\) 与 \((q,0)\)，得到
\[
\|c_j-N_m(q)\|^2\le\sigma^2\|p_j-q\|^2+a^2
\qquad\text{对每个 }j\text{ 及每个 }q. \tag{FD-7}
\]
这里的有限抬升完全由 FD-2 定义，不用任何外部扩张定理。
重复参数无需合并以保证 QP 唯一；若把它们作为同一 RL 图的样本，则同输入的反射值必须一致。

<a id="fd-shadow"></a>
## FD-SHADOW · 强单调双 Lipschitz 同胚和样本误差

定义
\[
X(q)=\tfrac12(q+N_m(q)),\qquad
Y(q)=\tfrac1{2\lambda}(q-N_m(q)).
\]
对每个 \(x\)，方程 \(X(q)=x\) 等价于 \(q=2x-N_m(q)\)；
对每个 \(v\)，方程 \(Y(q)=v\) 等价于 \(q=2\lambda v+N_m(q)\)。
两右侧均为 \(\sigma<1\) 的收缩。逐次代入的相邻差被几何级数控制，
在完备 \(\mathbb R^n\) 中有唯一固定点。因此 \(X,Y\) 均双射，
\[
A_m=Y\circ X^{-1},\qquad A_m^{-1}=X\circ Y^{-1}
\]
是同一个全域代理及其逆。
从 FD-5 和三角不等式，
\[
\begin{aligned}
\tfrac{1-\sigma}{2}\|q-r\|&\le\|X(q)-X(r)\|
 \le\tfrac{1+\sigma}{2}\|q-r\|,\\
\tfrac{1-\sigma}{2\lambda}\|q-r\|&\le\|Y(q)-Y(r)\|
 \le\tfrac{1+\sigma}{2\lambda}\|q-r\|.
\end{aligned} \tag{FD-8}
\]
故
\[
\operatorname{Lip}A_m\le\frac{1+\sigma}{\lambda(1-\sigma)},\qquad
\operatorname{Lip}A_m^{-1}\le\frac{\lambda(1+\sigma)}{1-\sigma}. \tag{FD-9}
\]
若 \(h=q-r,k=N_m(q)-N_m(r)\)，则
\[
\langle X(q)-X(r),Y(q)-Y(r)\rangle
=\frac{\|h\|^2-\|k\|^2}{4\lambda}
\ge\frac{1-\sigma}{\lambda(1+\sigma)}
\|X(q)-X(r)\|^2. \tag{FD-10}
\]
这给 \(A_m\) 的显示强单调常数；不声称 conditioning 常数最优。

FD-7 换回原坐标：对每个样本及任意 \(z\in\mathbb R^n\)，
\[
\|(x_i-z)-\lambda(v_i-A_m(z))\|^2
\le\sigma^2\|(x_i-z)+\lambda(v_i-A_m(z))\|^2+a^2. \tag{FD-11}
\]
分别取 \(z=x_i\) 和 \(z=A_m^{-1}(v_i)\)，得
\[
\lambda\|v_i-A_m(x_i)\|\le\frac a{\sqrt{1-\sigma^2}},\qquad
\|x_i-A_m^{-1}(v_i)\|\le\frac a{\sqrt{1-\sigma^2}}. \tag{FD-12}
\]
至此 C19 的有限样本结论闭合；没有用未观测图或其纤维非空性。

<a id="fd-cover"></a>
## FD-COVER · 同图同尺度覆盖和完整纤维的全称门

另给同一个原完整关系 \(F\) 或图块 \(\mathcal G\subseteq\operatorname{gph}F\)，
将认证图记为 \(\Gamma=\operatorname{gph}F\) 或 \(\Gamma=\mathcal G\)。
C20-v2 中，全部样本及每个待认证点均属 \(\Gamma\)，该同一图满足已声明的全尺度或局部 RL。
FD-1 的**全部样本对兼容性仍为前件**；
局部 RL 只认证近对，不能自动提供远距样本对兼容性。
固定 \(L>0,0<\gamma<1,\delta\ge0\)。
对每个待认证图点 \((x,v)\)，记 \(p=x+\lambda v,c=x-\lambda v\)；
要求存在样本 \(i\) 使
\[
\|p-p_i\|\le\delta,\qquad
\|c-c_i\|\le L\|p-p_i\|^\gamma. \tag{FD-13}
\]
若仅有局部 \(\mathrm{RL}(\lambda,\gamma,L;R_0)\)，还必须
\(\|p-p_i\|\le R_0\)；\(\delta\le R_0\) 是可用的充分门。
全尺度 RL 自动满足尺度门。FD-13 不能借用另一个图块的证书。

令 \(b=L\delta^\gamma\)。由 FD-7、FD-13，对任意 \(q\) 有
\[
\|c-N_m(q)\|
\le b+\sqrt{\sigma^2(\|p-q\|+\delta)^2+a^2}. \tag{FD-14}
\]
取 \(q=X^{-1}(x)=x+\lambda A_m(x)\)，则
\(\|p-q\|=\|c-N_m(q)\|=\lambda\|v-A_m(x)\|\)。
取 \(q=Y^{-1}(v)=A_m^{-1}(v)+\lambda v\)，则两个范数都为
\(\|x-A_m^{-1}(v)\|\)。两种比较的 \(t\ge0\) 均满足
\[
t\le b+\sqrt{\sigma^2(t+\delta)^2+a^2}. \tag{FD-15}
\]
若 \(t<b\) 可直接界住；若 \(t\ge b\)，平方两边的非负部分得
\[
(1-\sigma^2)t^2-2(b+\sigma^2\delta)t
+b^2-\sigma^2\delta^2-a^2\le0.
\]
其较大根为
\[
K_\delta=
\frac{b+\sigma^2\delta+
\sqrt{\sigma^2(b+\delta)^2+(1-\sigma^2)a^2}}{1-\sigma^2}
\ge b. \tag{FD-16}
\]
所以每个 FD-13 图点有
\(\lambda\|v-A_m(x)\|,\|x-A_m^{-1}(v)\|\le K_\delta\)。
当 \(\delta=0\) 时 \(K_0=a/\sqrt{1-\sigma^2}\)；
再同时取 FD-3 的 \(a^2=M_\sigma/2\)、\(\sigma=\sqrt\gamma\)，得 \(K_0=R/\sqrt2\)。

若完整 \(F(x)\) 非空，且其**每个**图点属于认证图并满足 FD-13，
才有 \(d_H(F(x),\{A_m(x)\})\le K_\delta/\lambda\)；
完整 \(F^{-1}(v)\) 非空且逐图点满足相同门，才有
\(d_H(F^{-1}(v),\{A_m^{-1}(v)\})\le K_\delta\)。
因为非空集合到 singleton 的 Hausdorff 距离就是所有点距的 supremum。
图块证书不排除块外远支，覆盖原输入 \(x\) 不等于覆盖 \(p=x+\lambda v\)。

<a id="fd-eval"></a>
## FD-EVAL · gap、查询误差与反演误差

对可行 \(\widehat\theta\in\Delta_m\)，令
\[
g_q=2Q\widehat\theta+d(q),\qquad
G=\langle g_q,\widehat\theta\rangle-\min_i(g_q)_i\ge0.
\]
写 \(\theta_*=\theta(q),h=\widehat\theta-\theta_*\)。
在 \(\theta_*\) 处用 FD-4，并精确展开目标：
\[
h^TQh\le\Phi_q(\widehat\theta)-\Phi_q(\theta_*).
\]
在 \(\widehat\theta\) 处用凸性和 \(\theta_*\in\Delta_m\)：
\[
\Phi_q(\widehat\theta)-\Phi_q(\theta_*)
\le\langle g_q,\widehat\theta-\theta_*\rangle\le G.
\]
所以 \(\|V\widehat\theta-N_m(q)\|\le\sqrt G\)。
这只给当前查询的 \(e_N\)；若 \(\widehat N(q)=V\widehat\theta\)，可取 \(e_N=\sqrt G\)。

给定观测 \(\widetilde v\)，令 \(q_*=Y^{-1}(\widetilde v)\)。
它满足 \(q_*=2\lambda\widetilde v+N_m(q_*)\)。
若 \(\|\widehat N(q)-N_m(q)\|\le e_N\)，收缩给
\[
(1-\sigma)\|q-q_*\|
\le\|q-2\lambda\widetilde v-\widehat N(q)\|+e_N.
\]
取 \(\widehat x=q-\lambda\widetilde v\)，
\(A_m^{-1}(\widetilde v)=q_*-\lambda\widetilde v\)，故可认证
\[
e_x=\frac{\|q-2\lambda\widetilde v-\widehat N(q)\|+e_N}{1-\sigma}
\ge\|\widehat x-A_m^{-1}(\widetilde v)\|. \tag{FD-17}
\]
也可用任何独立证明的 \(e_x\)；FD-17 是充分办法，不是必经算法。
单有很小 gap 不约束候选 \(q\) 的固定点残差，见 [F35](../../FAILED_ROUTES.md#f35)。
浮点 \(G,e_N,e_x\) 若作为严格证书，需包含向外取整或已经证明的误差界。

<a id="fd-total"></a>
## FD-TOTAL · 同一真目标的三项误差

若 \(\|\widetilde v-v\|\le\eta\)，完整非空 \(F^{-1}(v)\) 的所有图点
满足 FD-13，且 \(e_x\) 是上述独立反演证书，则对**每个**
\(x\in F^{-1}(v)\)，在 \(x,\widehat x\) 之间插入
\(A_m^{-1}(v),A_m^{-1}(\widetilde v)\)，由 FD-9、FD-16 得
\[
\|x-\widehat x\|
\le K_\delta+\frac{\lambda(1+\sigma)}{1-\sigma}\eta+e_x. \tag{FD-18}
\]
不要求观测 \(\widetilde v\) 的原纤维非空，代理逆映射已全域定义；
原图覆盖认证针对真 \(v\) 的完整纤维。此结论不包含采样可获得性、
维数无关复杂度、全空间无限图认证或一般优越性。

<a id="fd-audit"></a>
## 证据、依赖和审查范围

FD-1–18 是有限维代数、有限抬升、变分不等式和收缩固定点证明。
来源：[S23 TeX §6](../../history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex)，
标签 thm:finite_qp、thm:covered、cor:coveredfibers、prop:evaluation、cor:totalerror。
原稿身份与本页推导相同；局部同图同尺度调用是 C20-v2 另已固定的范围。
独立审查记录与状态以 [当前接收记录](../audit/BLIND_RECEIPT_2026-10-05_QP.md)、
[Claim 总账](../../CLAIMS.md) 为准。C20-v1 的越尺度反例保留在 [F36](../../FAILED_ROUTES.md#f36)。
