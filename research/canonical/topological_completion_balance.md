# Hölder–RL 全局完成的拓扑代价：吸引零簇与指数缺额

本模块固定一个新的研究问题：在保留局部完整近端动力时，全尺度 Hölder–RL 完成能否同时保留全部零集？它不改动 C04 的任意紧纤维实现，也不把 C11 的连续回缩升级为形变回缩。研究基线为 `4930596e20e48f8fdb3af09706461c7a58131c7c`，日期 2026-10-10。C231 在以下限定范围为 `derived-checked`，经过两位独立审查者逐段攻击；证明使用经典固定点指数。本库中的新连接与公开发表优先分别判断。

<a id="tcb-contract"></a>
## TC1 · 完整对象和保真合同

取有限维实空间 \(H=\mathbb R^n\)、\(n\ge1\)、\(\lambda>0\)。设 \(M\subset H\) 是非空紧嵌入 \(C^2\) 无边界子流形，允许有限多个分量。取 \(0<\rho<\operatorname{reach}(M)\)，记
\[
N_\rho=\{p:d(p,M)\le\rho\}.
\]
管有唯一最近点投影，并由法向线性缩放强形变回缩到 \(M\)；这是管的几何假设，独立于 C11。

在 \(N_\rho\) 上指定连续 \(T\)，满足
\[
T|_M=\operatorname{Id},\qquad
d(Tp,M)\le\theta d(p,M)\quad(p\in N_\rho),\qquad0\le\theta<1. \tag{TC1}
\]
于是 \(T(N_\rho)\subset\operatorname{int}N_\rho\)，管内固定点恰为 \(M\)。令 \(C_0(p)=2T(p)-p\)。假设 \(C_0\) 在整个管上为 \((L,\gamma)\)-Hölder，\(L>0,0<\gamma<1\)。考虑任一在全部 \(H\) 上有某个有限同指数 Hölder 常数 \(\widehat L\) 的延拓 \(\widehat C\)，要求
\[
\widehat C|_{N_\rho}=C_0. \tag{TC2}
\]
同常数扩张是本合同的特例；存在性可调用 [HE-EXT](holder_extension.md#he-extension)。以下结论并不需要最优常数。

定义完整原关系
\[
\widehat T(p)=\frac{p+\widehat C(p)}2,\qquad
\operatorname{gph}\widehat F
=\{(\widehat T(p),(p-\widehat T(p))/\lambda):p\in H\}. \tag{TC3}
\]
其完整 \(J_{\lambda\widehat F}\) 在全部输入上单值且等于 \(\widehat T\)；满 Minty 输入使该图在固定 \((\lambda,\widehat L,\gamma)\) 下 graph-maximal。它不因此成为极大单调。

TC2 保存整个输入管上的全部近端输出，不是仅保存有限样本、单条轨道或零集。它保存相应原图点；不自动保证原输出位置的完整前向纤维没有增加其它非局部图点。

<a id="tcb-balance"></a>
## C231-v1 · 总指数、局部 Euler 特征与被迫新增零点

在 TC1–TC3 的全部条件下，\(\operatorname{Fix}\widehat T=\operatorname{zer}\widehat F\) 为紧集，管内部分恰为 \(M\)。令
\[
K=\operatorname{Fix}\widehat T\setminus M.
\]
则 \(K\) 是位于 \(H\setminus N_\rho\) 的紧固定点簇，并与 \(M\) 有正距离；允许 \(K=\varnothing\)。其聚簇指数满足
\[
\operatorname{ind}(\widehat T,M)=\chi(M),\qquad
\operatorname{ind}(\widehat T,K)=1-\chi(M). \tag{TC4}
\]
空簇指数约定为零。因此
\[
\chi(M)\ne1\Longrightarrow K\ne\varnothing. \tag{TC5}
\]
若完整零集就是 \(M\)，必要条件为 \(\chi(M)=1\)。若整个零集由不交的有限个此类严格管吸引簇组成，则其 Euler 特征之和必须为 1。

**外部导入。** Benjamin–Gottlieb, *Fixed Point Indices and Manifolds with Collars*, [作者 PDF](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf)，§2.1，PDF p.3–4：localization (2.1.1)、additivity (2.1.2)、compact ENR normalization \(I(f)=L(f)\) (2.1.4)、commutativity (2.1.6)。球和光滑闭管均为紧 ENR；管允许有边界，不需假定为有限多面体。使用有理同调计算 Lefschetz 数。经典指数性质不是本库新定理。

**证明。**

1. **全局有限性与总指数。** Hölder 界给
   \(\|\widehat C(p)\|\le\|\widehat C(0)\|+\widehat L\|p\|^\gamma\)。故充分大的 \(R\) 满足
   \[
   \frac{R+\|\widehat C(0)\|+\widehat L R^\gamma}{2}<R.
   \]
   对全部 \(\|p\|\le R\)，\(\widehat T(p)\in B_R\)。对更大半径同一严格界排除固定点，故全部固定点有界；连续性使其闭，从而紧。大闭球上的自映射 Lefschetz 数为 1，因为仅 \(H_0\cong\mathbb Q\) 非零。compact ENR normalization 给球空间中的指数 1。令 \(W=\widehat T^{-1}(B_R)\)，则 \(W\) 开且包含整个闭球；\(\widehat T:W\to\overline B_R\) 与包含 \(\overline B_R\hookrightarrow H\) 的两个 composite 有相同固定点。commutativity 将这个指数换成环境空间指数，再以 localization 得 ambient 总指数 1。

2. **局部指数。** 选任意 \(0<\delta<\rho\)。闭管 \(N_\delta\) 强形变回缩到 \(M\)，其包含 \(i:M\hookrightarrow N_\delta\) 诱导逐阶同调同构。TC1 给 \(T:N_\delta\to\operatorname{int}N_\delta\) 且 \(Ti=i\)，所以 \(T_*i_*=i_*\)，即 \(T_*=\operatorname{Id}\)。故 \(L(T|_{N_\delta})=\chi(M)\)，compact ENR normalization 得管内指数。

3. **换空间的显式接口。** 不把紧管内部指数未经说明换成环境空间指数。取 \(\delta<\delta'<\rho\) 且 \(\theta\delta'<\delta\)。TC1 保证 \(\widehat T:\operatorname{int}N_{\delta'}\to N_\delta\)。与包含 \(j:N_\delta\to H\) 组成两个 composite：环境中的 \(j\widehat T\) 和紧管中的 \(\widehat Tj\)。二者固定点都恰为 \(M\)；§2.1(2.1.6) commutativity 给相同指数。再以 localization 将该环境局部指数定位到 \(M\)。这也处理了所用闭管的边界。

4. **缺额与非空性。** TC1 排除整个 \(N_\rho\setminus M\) 的固定点，尤其边界无固定点。全局固定点紧，故管外剩余 \(K\) 紧并与 \(M\) 分离。选两个不交开邻域分别围住 \(M,K\)，以 additivity 将总指数 1 分解，得到 TC4。非零指数的簇不能为空，得到 TC5。多个簇的结论同理。证毕。

对每个 \(z\in K,s\in M\)，因 \(\widehat C(z)=z,\widehat C(s)=s\)，还有
\[
\|z-s\|\le\widehat L^{1/(1-\gamma)}. \tag{TC6}
\]
这是既有零纤维直径界的直接应用，给额外零点的定位而非新的一般定位原理。

<a id="tcb-sphere"></a>
## TC6 · 完整单值锐基准：吸引球面与补偿原点

取 \(n\ge2,\lambda=1\)，定义径向映射 \(T(p)=\tau(\|p\|)p/\|p\|\)，\(T(0)=0\)，其中
\[
\tau(r)=\begin{cases}
7r/4,&0\le r\le1/2,\\
1+(r-1)^3,&1/2\le r\le3/2,\\
r/4+3/4,&3/2\le r\le3,\\
r/2,&r\ge3.
\end{cases} \tag{TC7}
\]
接缝精确相等；每段严格增加，包括导数在 \(r=1\) 为零的三次段。\(\tau\) 满射非负实轴，所以 \(T\) 是全域同胚。取全域连续单值原算子 \(F(y)=T^{-1}(y)-y\)，则完整 \(J_F=T\)，没有漏支或选中残差替换。

令 \(C=2T-\operatorname{Id}\)，其径向量 \(c(r)=2\tau(r)-r\) 为
\(5r/2\)、\(2+2(r-1)^3-r\)、\(3/2-r/2\)、\(0\)。径向导数绝对值和切向比值 \(|c(r)|/r\) 均不超过 \(5/2\)。分段光滑径向映射的线段积分给
\[
\operatorname{Lip}(C)\le5/2,\quad
\sup\|C\|=B:=1+\frac{2}{3\sqrt6}.
\]
最大值由中段 \(r=1-1/\sqrt6\) 达到。对任意 \(0<\gamma<1\)，用
\(\min\{(5/2)d,2B\}\le((5/2)d)^\gamma(2B)^{1-\gamma}\) 得全尺度 Hölder–RL 常数
\[
L_\gamma=(5/2)^\gamma(2B)^{1-\gamma}. \tag{TC8}
\]

逐段解 \(\tau(r)=r\) 得完整零集精确为
\[
S=\operatorname{zer}F=\{0\}\cup S^{n-1}. \tag{TC9}
\]
在球面输入管 \(|\|p\|-1|\le1/2\) 内，令 \(t=\|p\|-1\)。有
\[
t^+=t^3,\quad
d(Tp,S^{n-1})=|t|^3\le\tfrac14|t|,\quad
\|F(Tp)\|=|t-t^3|.
\]
因此真实单值残差满足
\[
d(Tp,S)\le\left(\frac43\right)^3\|F(Tp)\|^3. \tag{TC10}
\]
输出半径在 \([7/8,9/8]\)，到完整 \(S\) 的最近距离确为到球面的距离。取 \(\gamma>1/3\)，则 \(q=3\) 给 \(q\gamma>1\)；全对模、完整 coverage、零锚和真 EB 均来自同一关系，直接兼容在小尺度成立。更直接地，TC7 已逐点给管不变和有限径向长度。

这个 \(q=3\) EB 仅在球面输出窗成立；原点附近 \(F(y)=-3y/7\)，不满足同一个三次 EB，也不是严格吸引零点。不能把 TC10 扩大成全部零集邻域的统一 RLEB。

球面局部指数 \(\chi(S^{n-1})=1+(-1)^{n-1}\)。原点附近 \(T(p)=7p/4\)，其指数为 \(\operatorname{sign}\det(I-7I/4)=(-1)^n\)。它恰好补偿 TC4 的缺额：
\[
\chi(S^{n-1})+(-1)^n=1. \tag{TC11}
\]
平面吸引圆需补 \(+1\)，三维吸引二球面需补 \(-1\)。TC5 要求至少一个额外零点，此例恰好增加一个孤立点。这不证明 TC8 的 Hölder 常数最优，也不证明任意拓扑缺额都能由一个孤立点实现。

<a id="tcb-frontier"></a>
## 真正的下一问题与攻击边界

**Q-TC-v1（open）。** 固定同一局部完整 \(T\)、整管 \(C_0\)、\(\lambda,L,\gamma\)。何时存在保留整管数据且不增加零点的全域同常数 Hölder–RL 完成？C231 给 \(\chi(M)=1\) 的必要条件。充分性未证；嵌入补空间、固定点类、同常数插值和纤维约束可能产生额外障碍。应分别研究允许增大常数与必须保精确常数两种合同。

第一阶段只做三件有鉴别力的事：查指数缺额是否是可实现完成的唯一拓扑障碍；对一个 \(\chi=1\) 的非可缩紧光滑实例实际构造或反驳保零完成；再考虑一般紧 ENR/分层零集，并明确建立不变紧邻域而不是借用 C11 的回缩。

**与已有资产的真关系。** C04 对任意允许紧零纤维的实现不要求给定近端吸引动力；C231 限制同时保存动力的完成，二者不矛盾。C11 已给 ENR，未给本定理使用的管/同调等价。C05-v2 给局部鲁棒 forcing，局部非零指数与全局总指数 1 的身份不同。固定核 GPPA 若经连续双射把同一完整局部动力转到核空间，可以在那个有限维核空间另核 TC1–TC3；非单射 union、任意 lift 或物理回代不能直接套用。

**不能提升的范围。** 局部 RL 没有无穷远总指数；有限数据没有整管保真；一般逐点收敛没有不变紧管；回缩没有自动同伦等价；无限维没有本证明的有限维紧球接口。\(\chi=1\) 没有充分性结论。本定理也不排除 Luke–Tam 的全部广义非单调框架或全部改写。

**价值和先行性。** 经典指数、Lefschetz 和管几何提供机制，不能称其首次发现。值得继续的是固定 Hölder 完成合同中的必要/充分条件、最小额外零点与可定位性。本轮有界检索未建立全球优先性。

**独立攻击记录。** 三位 Astra 分别重构本质联系、切向新机制及存在/算法边界。拓扑路线的主要 fatal objection 是“由连续回缩直接认同 Euler 特征”；正文改用独立的光滑管和显式 commutativity 接口。最终正文由本质联系与反向审查两位 Astra 各自逐段核 TC1–TC11、完整原图/完整零集、管边界及经典引用；未发现现存 fatal objection。两者均指出全局球指数换空间需要显式接口，该接口已补入 Step 1。审查者不以数值结果授予全称证明，也未核发表优先性；代码由主代理独立运行。

**可复算。** [verify.py](../code/topological_completion/verify.py) 和 [results.json](../code/topological_completion/results.json) 保存接缝、逆式、完整近端身份、真实 EB、Cayley 界和指数算术的有限检查。它们不证明一般扩张量词或外部指数定理。
