# 完整图剖面、统一紧相容性与定量逃逸

这些工具服务于总体算子空间的构造，但不指定尚未选定的自然母空间，也不证明 LT/RLEB/极大单调的规模比较。三个对象分别是完整关系、紧对象块、固定状态域上的映射空间；跨节须重新核同一对象和拓扑。

<a id="op-profile"></a>
## C166-v1 / OP-PROFILE · 图值剖面到真残差的准确桥

固定实 Hilbert 空间 \(H\)、完整关系 \(F:H\rightrightarrows H\)、输出窗 \(V\subseteq H\) 和非空闭目标 \(S\subseteq H\)。本引理不要求 \(S=F^{-1}(0)\)；用于 PPA 时另核该目标条件。记
\[
r_F(u)=\inf_{v\in F(u)}\|v\|,\qquad
\mathcal B_{F,V,S}(t)=\sup\{d(u,S):u\in V,\ v\in F(u),\ \|v\|\le t\},\quad t\ge0. \tag{OP1}
\]
空纤维残差为 \(+\infty\)，空上确界为 0；剖面允许 \(+\infty\)。固定有限非减函数 \(\psi:[0,\infty)\to[0,\infty)\)，不预设它在每个正点连续。以下全部残差求值只对 \(u\in V\) 的有限残差。

若另用有限定义域 \([0,\bar t]\)，OP2 的逼近须在 \(r_F(u)<\bar t\) 内进行。上端点 \(r_F(u)=\bar t\) 不取到时，域内的逐图值测试可能为空；相对右连续没有域外逼近点，须取到或另有明确的域外控制。本页全域陈述不省略这个边界。

1. \(\mathcal B_{F,V,S}(t)\le\psi(t)\) 对每个 \(t\ge0\) 成立，当且仅当每个 \(u\in V,v\in F(u)\) 有 \(d(u,S)\le\psi(\|v\|)\)。
2. 真残差 EB \(d(u,S)\le\psi(r_F(u))\) 推出上述两个等价条件。
3. 反向，逐图值界总给
\[
d(u,S)\le\psi(r_F(u)+):=\inf_{t>r_F(u)}\psi(t). \tag{OP2}
\]
若对每个这样的 \(u\)，残差由某个 \(v_u\in F(u)\) 取到，**或** \(\psi(r_F(u)+)=\psi(r_F(u))\)，则得到同一 \(\psi\) 的真残差 EB。两种充分门可以按输出逐点混用。有限维闭图保证每个有限残差取到；一般 Hilbert 闭图不保证这一点。

**证明。** 若剖面界成立，把 \(t=\|v\|\) 代入 OP1。若逐图值界成立，对 \(\|v\|\le t\) 用单调性后取上确界。若真 EB 成立，\(r_F(u)\le\|v\|\) 与单调性给逐图值界。反向，对于任意 \(t>r_F(u)\)，下确界定义给某个 \(v\in F(u)\) 满足 \(\|v\|<t\)，故 \(d(u,S)\le\psi(t)\)；对所有 \(t\) 取下确界即 OP2。取到时直接代入极小图值；右连续时用 OP2。有限维闭纤维中，任意极小序列有有界子列及收敛子列，闭性使极限仍在纤维，连续范数取得下确界。此论证没有把一条选中值的界当成全部图值的界。□

<a id="op-nonattainment"></a>
### 完整闭图反例：原点连续的 gauge 仍不够

取 \(H=\ell^2(\mathbb N_0)\)，标准正交基 \((e_n)_{n\ge0}\)，定义完整关系
\[
F(0)=\{0\},\qquad F(e_0)=\{\sqrt{1+1/n}\,e_n:n\ge1\},\qquad F(u)=\varnothing\quad(u\notin\{0,e_0\}). \tag{OP3}
\]
其完整零集 \(S=\{0\}\)，取 \(V=H\)，以及
\[
\psi(t)=\begin{cases}0,&0\le t\le1,\\1,&t>1.\end{cases} \tag{OP4}
\]
这是非减、有限、\(\psi(0)=0\) 且在原点连续的 gauge。\(F(e_0)\) 中不同值间的距离大于 \(\sqrt2\)，故任何强收敛值序列最终固定；两个不同输出位置也不能交替收敛。因此完整图在范数乘积拓扑中闭。所有 \(e_0\) 图值范数大于 1，且其下确界恰为 1，不取到。

OP1 的剖面精确等于 OP4：\(t\le1\) 时只有零图点可贡献；\(t>1\) 时取足够大 \(n\) 得贡献 \(d(e_0,S)=1\)。逐图值界成立，却
\[
d(e_0,S)=1>0=\psi(r_F(e_0)). \tag{OP5}
\]
这里 \(\psi(1+)=1\) 正好给 OP2。故“完整图点约束没有选中残差问题”仍不足以删去取到/右连续门。此例不宣称满足 coverage、RL 或算法留域。

<a id="op-compactness"></a>
## C167-v1 / OP-COMPACTNESS · 一个统一紧对象块中的相容性

固定非空紧拓扑空间 \(\mathcal K\)，给闭子集 \(C_i\subseteq\mathcal K\)，\(i\ge1\)。则
\[
\bigcap_{i\ge1}C_i\ne\varnothing
\quad\Longleftrightarrow\quad
\bigcap_{i=1}^N C_i\ne\varnothing\quad\text{对每个 }N\ge1. \tag{OP6}
\]
**证明。** 正向直接。若全部交为空，\(\{\mathcal K\setminus C_i\}\) 为开覆盖；紧性给有限子覆盖，把其索引包含在 \(1,\ldots,N\) 中，得到有限交为空，矛盾。□

在对象构造中，\(\mathcal K\) 必须预先固定完整图/完整源、拓扑、全部纤维和共同预算；每个实际约束须在该拓扑下证明闭。若要保 \(\kappa<1\) 的严格兼容，可固定 \(\kappa\le1-\eta\)，\(\eta>0\)，再核该预算约束闭。每个 \(N\) 都可行却允许 \(\eta_N\downarrow0\)、\(L_N\to\infty\) 或改变 \(\mathcal K\)，不是 OP6 的前提。

闭性不可省：在 \(\mathcal K=[0,1]\) 取 \(C_i=(0,1/i)\)，全部有限交非空而总交空。统一紧性不可省：在 \(\mathcal K=\mathbb R\) 取闭集 \(C_i=[i,\infty)\)。紧性提供的是**给定同一闭约束体系已经有限可行**之后的极限，不构造有限可行解，也不自动把网格条件升级为全部图点条件。

<a id="op-hole"></a>
## C168-v1 / OP-HOLE · 越界余量与相对孔洞的区别

固定非空紧度量状态空间 \(K\)、非空闭 \(S\subseteq K\)，以及映射空间 \(\mathfrak X\subseteq C(K,K)\) 配一致度量 \(d_\infty\)。固定 \(M\ge0\)，定义必要条件层
\[
\mathcal A_M=\{T\in\mathfrak X:d(Tx,x)\le M d(x,S)\text{ 对所有 }x\in K\}. \tag{OP7}
\]
若 \(U\in\mathfrak X\) 在某个 \(x_*\in K\) 满足
\[
d(Ux_*,x_*)\ge M d(x_*,S)+a,\qquad a>0, \tag{OP8}
\]
则相对球 \(B_{\mathfrak X}(U,a/2)\) 与 \(\mathcal A_M\) 不相交。

**证明。** 对球内 \(V\)，三角不等式给
\[
d(Vx_*,x_*)\ge d(Ux_*,x_*)-d_\infty(U,V)>M d(x_*,S)+a/2.
\]
所以 \(V\notin\mathcal A_M\)。□

要得到每个小球中的**统一相对孔洞**，还需另证存在同一个 \(0<c<1\)，对每个所声明中心 \(T\) 和全部足够小 \(r>0\)，能在同一 \(\mathfrak X\) 中构造 \(U\) 及见证余量 \(a\)，满足
\[
d_\infty(T,U)+cr\le r,\qquad a\ge2cr. \tag{OP9}
\]
此时球 \(B_{\mathfrak X}(U,cr)\subset B_{\mathfrak X}(T,r)\setminus\mathcal A_M\)。OP8 的单个见证没有 OP9 的全中心/全尺度量词，也不保证 \(U\) 保原完整图、精确尾或 RLEB 预算。若实际母空间度量不同，须独立证明其球控制这一个评价误差；不能直接搬一致球结论。此处给明确孔洞条件，不替未恢复的历史 \(\sigma\)-upper/lower-porosity 定理。

<a id="op-power"></a>
## C172-v1 / OP-POWER · 同一剖面的双侧幂阶门

固定 \(\lambda>0\)、\(0<\gamma\le1\)、\(p>0\)，非负函数 \(M(t)\) 和 OP1 的同一剖面 \(\mathcal B(r)\)。假设存在正常数 \(a_M,b_M,a_B,b_B\)，使所有足够小正 \(t,r\) 有
\[
a_Mt^\gamma\le M(t)\le b_Mt^\gamma,\qquad a_Br^p\le\mathcal B(r)\le b_Br^p. \tag{OP10}
\]
记 \(b_\lambda(t)=(t+M(t))/(2\lambda)\)。小尺度直接剖面兼容的量词是
\(\exists\kappa\in(0,1),\delta>0\ \forall t\in(0,\delta):\mathcal B(b_\lambda(t))\le\kappa t\)。它在 \(\gamma p>1\) 时成立，在 \(\gamma p<1\) 时不可能；端点 \(\gamma p=1\) 必须另核系数。超临界情形甚至对任意预先固定的 \(\kappa\in(0,1)\) 可缩窗实现；端点的“存在某个 \(\kappa\)”不承诺任意预给系数。

**证明。** 缩至 \(t\le1\)，\(t\le t^\gamma\) 给
\[
\frac{a_M}{2\lambda}t^\gamma\le b_\lambda(t)\le\frac{1+b_M}{2\lambda}t^\gamma.
\]
\(b_\lambda(t)\to0\)，故可同时缩进 OP10 的残差尺度，得到
\[
a_B\left(\frac{a_M}{2\lambda}\right)^p t^{\gamma p-1}
\le\frac{\mathcal B(b_\lambda(t))}{t}
\le b_B\left(\frac{1+b_M}{2\lambda}\right)^p t^{\gamma p-1}. \tag{OP11}
\]
两边极限给严格两种方向。端点时，右常数小于1是充分门，左常数不小于1阻止严格兼容；其它情形这两个包络不裁决。以 \(\gamma=p=1,M(t)=t,\mathcal B(r)=cr\) 为例，精确比为 \(c/\lambda\)，可小于、等于或大于1。□

结论只指 OP10 中的**双侧实际剖面**和所定义复合式，不把上界指数当必要条件。要转为 PPA 定理，仍须明确零锚、同尺度反射剖面、C166真残差桥、coverage和留域；实际轨道可能有更快的率。本条的 \(p\) 是残差剖面阶，不与其它主题的概率或算法参数同名替换。

<a id="op-sources"></a>
## 身份、依赖与可接续方向

- C166–C168及C172 在上述限定对象上为 `derived-checked`，全部证明在本页；仅用下确界、单调性、紧性、幂比较和三角不等式。外部新颖性未核。
- 来源路线 E.1/E.2、D.2/D.3、H.2 是问题种子；其图值到真残差、统一紧块与孔洞量词在此重新固定。C166 的反例是独立补写，不回填为源稿已经证明的结果。
- 与 [C132](../operator_space.md#os-fiber-eb) 一致：紧源完整纤维取到最小范数，故该处无需 gauge 连续；和 [C59](residual_window_bridge.md#rw-positive) 的“窗口到邻域”桥是不同问题。
- 下一行动：在一个指定自然完整对象空间中证明有限约束可行、闭性、完整纤维覆盖或 OP9 的同预算构造。它们都是明确的数学义务，不能因本页工具齐备而宣布总体比较完成。
