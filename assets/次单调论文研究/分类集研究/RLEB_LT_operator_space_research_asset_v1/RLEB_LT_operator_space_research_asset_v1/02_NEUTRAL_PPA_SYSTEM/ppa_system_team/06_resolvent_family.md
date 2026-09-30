# PPA 的比较对象：算子图、单步完整 resolvent 与一致 resolvent 族

日期：2026-09-20。职责范围：为体系化比较提供对象层、拓扑层和步长量词；不在本文断言 RLEB 或 LT 类的纲大小。下列代数与完备性论证独立复核，末节另列已读原始文献。

## 0. 推荐结论

**底层对象应当是完整闭图算子 \(F\)，等价地是一致的完整 resolvent 关系族；算法实例另外携带步长策略 \(\Sigma\)。**

这里“完整 resolvent”是完整关系 \((I+\lambda F)^{-1}\)，允许某些输入上为空、某些输入上多值，不预先保证全域可解。全域可解、单值、连续、留域和收敛应作为随后定义的子类性质，而不是偷偷写进底层对象。

关键事实是：

\[
\boxed{
\text{完整 }F
\quad\longleftrightarrow\quad
\text{任一固定步长的完整 }J_{\lambda F}\text{ 关系}
\quad\longleftrightarrow\quad
\text{一致的全 resolvent 关系族}
}
\tag{0.1}
\]

这三个空间可取彼此同胚的自然图拓扑，因此类别大小完全一致。**换成 family 语言不会新增自由度；真正改变母类的是把完整关系换成连续单值映射、选中分支，或预装某种收缩预算。**

首阶段建议状态空间取 \(H=\mathbb R^d\)，底层算子空间仍然是无限维的。这样不损失用户希望引入的泛函分析观点，却能同时得到 Polish 图空间、清晰的局部化和强弱收敛无歧义。一般 Hilbert 情形可随后扩展，但不能自动把有限维的 Polish 性、紧性论证搬过去。

## 1. 不需要单调性的精确图坐标

设 \(H\) 为实 Hilbert 空间，\(G=\operatorname{gph}F\subset H\times H\) 非空闭。对 \(\lambda>0\) 定义可逆有界线性变换

\[
L_\lambda(u,v)=(u+\lambda v,u),\qquad
L_\lambda^{-1}(x,y)=\left(y,\frac{x-y}{\lambda}\right).
\tag{1.1}
\]

直接按定义得到

\[
\operatorname{gph}J_{\lambda F}=L_\lambda G.
\tag{1.2}
\]

所以，任意闭关系 \(T\subset H\times H\) 都唯一确定一个闭图算子

\[
F_T(y)=\left\{\frac{x-y}{\lambda}:(x,y)\in T\right\},
\qquad J_{\lambda F_T}=T.
\tag{1.3}
\]

以上没有使用单调性、最大性、单值性、满射性或连续性。

必须区分两个“满”：

- \(J_{\lambda F}\) **输入全覆盖**等价于 \(\operatorname{ran}(I+\lambda F)=H\)。
- \(J_{\lambda F}\) **输出满射到 \(H\)**等价于 \(\operatorname{dom}F=H\)。

完整关系不等于上述任一种满射；它仅表示没有删去任何满足包含式的解。

另外，对每个 \(\lambda>0\)，有共同的零点/固定点恒等式

\[
\operatorname{zer}F
=\{s:s\in J_{\lambda F}(s)\}.
\tag{1.4}
\]

若 \(J_{\lambda F}\) 多值，(1.4) 不保证 \(J_{\lambda F}(s)=\{s\}\)。因此“解点是固定点”与“所有选择均不会离开解点”是两个不同性质。

## 2. 一族 resolvent 来自同一个算子的充要条件

### 定理 2.1：一般关系版本

给定非空步长集合 \(\Lambda\subset(0,\infty)\) 和一族非空闭关系 \(J_\lambda\subset H\times H\)。下列条件等价：

1. 存在唯一非空闭图 \(F\)，使 \(J_\lambda=(I+\lambda F)^{-1}\) 对全部 \(\lambda\in\Lambda\) 成立。
2. 对所有 \(\lambda,\mu\in\Lambda\) 和 \(x,y\in H\)，
   \[
   y\in J_\lambda(x)
   \quad\Longleftrightarrow\quad
   y\in J_\mu\left(\frac\mu\lambda x+
                   \left(1-\frac\mu\lambda\right)y\right).
   \tag{2.1}
   \]
3. 对一个任意固定的 \(\lambda_0\in\Lambda\)，
   \[
   L_\lambda^{-1}\operatorname{gph}J_\lambda
   =L_{\lambda_0}^{-1}\operatorname{gph}J_{\lambda_0}
   \quad(\lambda\in\Lambda).
   \tag{2.2}
   \]

**证明。** 若 \(y\in J_\lambda(x)\)，则 \(v=(x-y)/\lambda\in F(y)\)。令
\(w=y+\mu v=(\mu/\lambda)x+(1-\mu/\lambda)y\)，得到 \(y\in J_\mu(w)\)。逆推完全相同。反过来，由 (2.2) 将公共闭图定义为 \(G\)，(1.2) 即给出全部关系。唯一性由任意一个 \(\lambda_0\) 的可逆变换得出。证毕。

这是非单调/多值情形可直接使用的完整 resolvent identity。若只验证一条选中轨道或一个选中分支，不足以得到 (2.1)。

### 2.2 单值全域版本

若每个 \(T_\lambda:H\to H\) 是单值全域映射，则上面的相容性等价于经典形式

\[
T_\lambda x
=T_\mu\left(\frac\mu\lambda x+
            \left(1-\frac\mu\lambda\right)T_\lambda x\right)
\quad(\lambda,\mu\in\Lambda,\ x\in H).
\tag{2.3}
\]

这里要求**全部有序步长对**。以 \(\lambda_0\) 重构 \(F\) 后，一个方向用 \((\lambda,\mu)=(\mu,\lambda_0)\)，另一个方向用 \((\lambda_0,\mu)\)，得到与完整 \(J_{\mu F}\) 的相等，而非仅一侧包含。

独立指定一些看起来很好的 \(T_\lambda\) 不一定来自同一个 \(F\)。最小例：令每个 \(T_\lambda=I/2\)。每个映射单独都是某个最大单调算子的 resolvent，但重构得到 \(F_\lambda=I/\lambda\)，不可能对不同 \(\lambda\) 是同一个算子。

### 2.3 从单个单值映射换步长

若 \(T=J_{\lambda F}:H\to H\) 单值全域，置 \(c=\mu/\lambda\)，

\[
Q_c=cI+(1-c)T.
\tag{2.4}
\]

精确地有

\[
J_{\mu F}(z)=\{Tx:Q_cx=z\}=T\circ Q_c^{-1}(z).
\tag{2.5}
\]

这时 \(J_{\mu F}\) 输入全覆盖当且仅当 \(Q_c\) 满射；单值当且仅当 \(Q_c\) 单射。后一断言利用：若 \(Q_cx_1=Q_cx_2\) 且 \(Tx_1=Tx_2\)，则 \(c(x_1-x_2)=0\)。故全域单值当且仅当 \(Q_c\) 双射。

**不能把 (2.5) 无条件推广成多值映射的普通关系复合。** 取

\[
F(u)=\{0,-1\},\qquad \lambda=1,\quad\mu=2.
\]

则 \(T(x)=\{x,x+1\}\)，若机械地定义 \(Q_2(x)=\{x,x-1\}\)，便得到

\[
T\circ Q_2^{-1}(z)=\{z,z+1,z+2\},
\qquad J_{2F}(z)=\{z,z+2\}.
\tag{2.6}
\]

多出来的 \(z+1\) 来自两次选值时丢掉了“同一个输出 \(y\)”的耦合。一般情形必须保留 (2.1) 或 graph shear。

## 3. 一个不预载收敛的完备母空间

令 \(E=H\times H\)，记 \(\mathrm{CL}(E)\) 为全部非空闭子集，亦即全部非空闭图算子。固定原点，定义

\[
q_m(G,H)=\sup_{\|z\|\le m}|d(z,G)-d(z,H)|,
\]
\[
d_{AW}(G,H)=\sum_{m=1}^{\infty}2^{-m}\min\{1,q_m(G,H)\}.
\tag{3.1}
\]

这是 Attouch–Wets 的距离函数形式：在每个有界球上一致比较到图的距离。不要直接以 \(G\cap B_m\) 与 \(H\cap B_m\) 的 Hausdorff 距离代替；切球边界会产生额外问题。有关 (3.1) 和有界局部 excess 的等价性，可对照 Voytsitskyy 的 §2、Proposition 2。

### 定理 3.1：完备性

若 \(E\) 完备，则 (3.1) 是完备度量。

**独立证明。** 设 \((G_n)\) 为 Cauchy 列，则 \(d(\cdot,G_n)\) 在每个有界球上一致 Cauchy，极限为有限、非负、1-Lipschitz 函数 \(f\)。证明 \(f=d(\cdot,G)\)，其中 \(G=\{f=0\}\)。

首先 \(d(0,G_n)\) 有共同上界 \(M\)。选充分靠后的子列 \(G_{n_j}\)，使其距离函数在 \(B_{M+3}\) 上的相邻误差可求和、且和小于 \(1/4\)。从 \(g_1\in G_{n_1}\cap B_{M+1}\) 出发，递推选 \(g_{j+1}\in G_{n_{j+1}}\)，令
\(\|g_{j+1}-g_j\|\) 小于相邻误差再加同阶的可求和余量。所有点仍在该球内，且构成 Cauchy 列。极限 \(g\) 满足 \(f(g)=0\)，故 \(G\ne\varnothing\)。

由 \(f\) 的 1-Lipschitz 性，\(f(x)\le d(x,G)\)。反向，对任意 \(x\) 和 \(\varepsilon>0\)，取充分靠后的 \(g_1\in G_{n_1}\) 满足
\(\|x-g_1\|<f(x)+\varepsilon/2\)。在一个包含 \(x\)、\(g_1\) 和所有后续点的固定大球内重做上述链，使其总移动量小于 \(\varepsilon/2\)，便获得 \(g\in G\) 且
\(\|x-g\|<f(x)+\varepsilon\)。于是 \(d(x,G)=f(x)\)。距离函数在有界球上的一致收敛即给 \(d_{AW}(G_n,G)\to0\)。证毕。

当 \(H=\mathbb R^d\) 时，这个空间可分，故为 Polish 空间。在无限维可分 Hilbert 空间中，不能因为 \(H\) 可分就断言 \(\mathrm{CL}(E)\) 的 AW 拓扑可分；有界一致的 hyperspace 通常不具该性质。不过完备性与 Baire 性仍成立。

### 定理 3.2：graph shear 是同胚，且对紧步长区间一致

\[
G\longmapsto L_\lambda G
\tag{3.2}
\]

是 \(\mathrm{CL}(E)\) 的同胚。若 \(I=[a,b]\Subset(0,\infty)\)，则

\[
G_n\to G\ \text{in AW}
\quad\Longrightarrow\quad
\sup_{\lambda\in I}d_{AW}(L_\lambda G_n,L_\lambda G)\to0.
\tag{3.3}
\]

**证明要点。** \(L_\lambda\)、\(L_\lambda^{-1}\) 的算子范数在 \(I\) 上有共同界。AW 收敛等价于对每个固定球，\(G_n\) 到 \(G\) 及 \(G\) 到 \(G_n\) 的局部 excess 趋零。一个有界的变换后图点，其原像由共同逆范数界控制；其近似图点经 \(L_\lambda\) 变换后的误差由共同正向范数界控制。这同时给出两侧 excess 的一致收敛，故得 (3.3)。对 \(L_\lambda^{-1}\) 同理。另由 \(L_\lambda\) 的算子范数连续性，\(\lambda\mapsto L_\lambda G\) 本身 AW 连续。证毕。

### 3.3 全 resolvent-family space

在
\[
C((0,\infty),\mathrm{CL}(E))
\]
上取紧步长区间一致 AW 度量

\[
d_{\mathrm{fam}}(\mathcal J,\mathcal K)
=\sum_{m=1}^{\infty}2^{-m}
  \sup_{\lambda\in[1/m,m]}
  d_{AW}(\operatorname{gph}J_\lambda,
         \operatorname{gph}K_\lambda).
\tag{3.4}
\]

取其中满足 (2.1) 的相容族子空间 \(\mathfrak R\)。则：

1. 每个闭图 \(G\) 产生属于 \(\mathfrak R\) 的族 \(\lambda\mapsto L_\lambda G\)。
2. \(\mathfrak R\) 在上述连续函数空间中闭：固定 \(\lambda,\mu\)，相容性就是两个经固定线性变换后的闭集相等；此等式对 AW 极限封闭。
3. (3.4) 在 \(\mathfrak R\) 上完备。连续函数空间的紧一致 Cauchy 列可逐区间取极限，闭相容性保留。
4. \(G\mapsto\mathcal J_G\) 为同胚，逆映射是 \(\mathcal J\mapsto L_1^{-1}\operatorname{gph}J_1\)。

所以 \(F\)-space 和相容 family-space 的第一纲、余稀、稠密性等，必须逐一精确对应。家族坐标的价值是把步长选择显式化，而非制造一个更大的独立参数世界。

## 4. 连续单值 family 是有用图表，不是全部算子的母空间

固定 \(I=[a,b]\Subset(0,\infty)\)。在有限维取
\[
\mathcal C_I=C(I\times H,H)
\]
及紧一致拓扑。满足 (2.3) 的 \(T\) 组成一个闭、完全可度量子空间：若 \(T^n\to T\) 紧一致，对固定 \(\lambda,\mu,x\)，内部参数
\(c x+(1-c)T^n_\lambda x\) 收敛且留在一个紧集，故能逐点通过复合等式的极限。

一般 Hilbert 空间可改用“连续且在有界集合上有界”的函数空间和有界一致度量，其完备性也成立；但不要自动称其 Polish。

这类空间内每个元素都来自唯一 \(F\)，并在 \(I\) 上拥有完整、单值、连续的 resolvent。它适合研究这一**良定性图表内**的收敛与证书。它不包含所有闭图算子，也不包含全部可能多值的 PPA 理论。

### 4.1 单调类的经典校准

在全正步长的一致 family 中，下列三项等价：

1. 底层 \(F\) 最大单调；
2. 每个 \(J_{\lambda F}\) 全域且 firmly nonexpansive；
3. 每个 \(J_{\lambda F}\) 全域、单值且 nonexpansive。

其中 \(3\Rightarrow1\) 可以直接证明。对任意两个图点 \((u,a),(v,b)\)，所有正步长下的非扩张性给
\[
0\le2\lambda\langle u-v,a-b\rangle+\lambda^2\|a-b\|^2.
\]
除以 \(\lambda\) 再令 \(\lambda\downarrow0\)，得单调性。若 \((u,a)\) 与全图单调相关，给定 \(\lambda>0\)，取完整输出 \(y=J_{\lambda F}(u+\lambda a)\) 及 \(b=(u+\lambda a-y)/\lambda\in F(y)\)。单调相关性变为
\(-\|u-y\|^2/\lambda\ge0\)，故 \((u,a)\in G\)，得最大性。

这不是新定理的原创性主张：Sipoş 的 **Theorem 3.3** 已在 CAT(0) 空间证明“各映射非扩张＋resolvent identity”等价于 jointly firmly nonexpansive family；在 Hilbert 空间配合经典 Minty 对应正是上述校准。它应当作为新体系要恢复的基准层。仅某一个步长 \(J_{\lambda F}\) 非扩张则不够，\(J_{\lambda F}=-I\)、\(F=-2I/\lambda\) 即反例。

特别地，\(C(K,K)\) 上单步映射的工作不能未经说明升级成整个 \(F\)-空间的结论：

- 若只知道 \(T\) 在紧集 \(K\) 上的值，(1.3) 只重构相应的截断图，未知外部图可能向同一输入贡献额外解。
- 变步长后的输入 \(c x+(1-c)Tx\) 在 \(c>1\) 时可能离开 \(K\)，即使 \(K\) 凸。
- 因此局部 family 需要带着可变输入域的图表相容性，不能把所有步长都生硬放进同一个 \(C(K,K)\) 然后套 (2.3)。

## 5. 固定解集与良定性如何编码

### 5.1 固定非点解集不要求收缩

给定非空闭 \(S\subset H\)，定义

\[
\mathfrak X_S^+=\{G\in\mathrm{CL}(E):S\times\{0\}\subset G\}.
\tag{5.1}
\]

这是 AW 闭子空间，因而完备。它只规定 \(S\subset\operatorname{zer}F\)，未加入 RLEB、LT 或收敛性。

在有限维，精确解集切片

\[
\mathfrak X_S=\{G:G\cap(H\times\{0\})=S\times\{0\}\}
\tag{5.2}
\]

在 \(\mathfrak X_S^+\) 中为 \(G_\delta\)，故完全可度量/Polish。证明：令

\[
K_m=\{u:\|u\|\le m,\ d(u,S)\ge1/m\}.
\]

每个 \(K_m\) 紧，并且

\[
\mathfrak X_S
=\bigcap_{m\ge1}
 \{G\in\mathfrak X_S^+:d(K_m\times\{0\},G)>0\}.
\tag{5.3}
\]

右边每个集合都 AW 开。在无限维，\(K_m\) 不必紧，这个证明不能照搬；需要另证或改用更强的统一分离预算。**不能把有限维的精确 \(S\) 切片结论无条件宣布到一般 Hilbert 空间。**

### 5.2 全输入可解与单值不是图空间的自动闭性质

令 \(H=\mathbb R\)，\(F_n=(1/n-1)I\)。则

\[
J_{F_n}=nI
\]

对所有输入全域、连续、单值，且 \(\operatorname{zer}F_n=\{0\}\)（\(n\ge2\)）。但 \(F_n\to-I\) 图收敛，而

\[
J_{-I}(0)=\mathbb R,\qquad J_{-I}(x)=\varnothing\ (x\ne0).
\tag{5.4}
\]

故若计划在“良定 PPA”子类直接用 Baire 定理，必须另外证明该子类完全可度量/Baire，或使用有共同紧性/连续性预算的图表。不能从闭图母空间完备直接推出所有子类完备。

## 6. 通用 PPA 动力关系与步长策略

### 定理 6.1：通用一步关系闭

定义

\[
\mathcal E=
\left\{(G,\lambda,x,y):
 \left(y,\frac{x-y}{\lambda}\right)\in G\right\}
\subset\mathrm{CL}(E)\times(0,\infty)\times H\times H.
\tag{6.1}
\]

它是闭集。若 \(G_n\to G\) AW、\((\lambda_n,x_n,y_n)\to(\lambda,x,y)\)、\(\lambda>0\)，则相应图点收敛并有共同范数界；有界球上的距离函数一致收敛给出极限图点到 \(G\) 的距离为零。

因此，给定闭策略集合 \(\Sigma\subset[a,b]^{\mathbb N}\)，轨道 incidence 空间

\[
\mathcal O_\Sigma=
\left\{(G,\boldsymbol\lambda,\boldsymbol x):
 \boldsymbol\lambda\in\Sigma,\quad
 \left(x_{k+1},\frac{x_k-x_{k+1}}{\lambda_k}\right)\in G
 \ \forall k\right\}
\tag{6.2}
\]

是 \(\mathrm{CL}(E)\times\Sigma\times H^{\mathbb N}\) 中的闭集；取标准完备乘积度量后它本身完备。若采用精确 \(S\) 的有限维切片，则仍完全可度量。这个结论没有使用任何收敛证书。

现在才定义动力性质。例如，对给定初值域 \(D\) 与策略 \(\Sigma\)，\(\mathfrak C^{\forall}_\Sigma(D,S)\) 应明确要求：

1. 每个被允许的初值/步长策略均有轨道，且规定的有限轨道能够延拓，避免“没有轨道所以全称收敛真”的真空问题；
2. 每条被允许的完整轨道都保持在指定工作域；
3. 每条轨道按事先指定的强/弱收敛意义，收敛到 \(S\) 中某点。

“存在一个选择收敛”是另一个类；若研究一个具体选值算法，则对象至少是 \((F,\text{选择规则},\Sigma)\)，而不只是 \(F\)。

### 6.2 同一算子不同步长可以完全不同

取 \(F=-I\)。当 \(\mu\ne1\)，

\[
J_{\mu F}=(1-\mu)^{-1}I.
\tag{6.3}
\]

- \(\mu>2\)：线性收敛到零；
- \(\mu=2\)：非零轨道为二周期；
- \(0<\mu<2,\ \mu\ne1\)：非零轨道发散；
- \(\mu=1\)：非零输入无解，零输入所有点都是输出。

所以“某个步长收敛”“某个步长区间内均收敛”“所有正步长收敛”不可混写。

### 6.3 即使最简单的单调算子也不能允许任意正步长序列

取 \(F=I\)，则

\[
x_k=x_0\prod_{j=0}^{k-1}(1+\lambda_j)^{-1}.
\tag{6.4}
\]

若 \(\lambda_j=2^{-j-1}\)，则 \(\sum_j\log(1+\lambda_j)<\infty\)，极限乘积严格正，非零初值不收敛到零。因此“全部正步长序列上的 PPA 收敛空间”连 \(I\) 都会排除。

最安全的第一版本是先固定 \(0<a\le\lambda_k\le b<\infty\) 的策略全集，或另外明确给出其他非退化步长规则。更广的策略应作为体系参数，而非由某个证书临时决定。

### 6.4 全选择与存在选择不同

令

\[
F(0)=\mathbb R,\qquad F(u)=\{-u/2\}\ (u\ne0).
\]

图为一条直线与一条竖线的并，闭且零集为 \(\{0\}\)，完整 resolvent 为

\[
J_F(x)=\{0,2x\}.
\tag{6.5}
\]

每步选择零，一步到解；每步选择 \(2x\)，非零轨道发散。只写“该算子的 PPA 收敛”没有确定数学含义。

### 6.5 全收敛类不自动闭

在同一个精确零集 \(S=\{0\}\) 切片内，令

\[
F_n=-(2+1/n)I,
\qquad\Sigma=[1,2]^{\mathbb N}.
\]

对每个固定 \(n\)，所有允许步长满足

\[
\|J_{\mu F_n}\|=\frac1{(2+1/n)\mu-1}
\le\frac1{1+1/n}<1,
\]

所以所有策略与初值都收敛到零。然而 \(F_n\to-2I\)，极限在常步长 \(\mu\equiv1\) 下给 \(x_{k+1}=-x_k\)，不收敛。

该反例同时成立于算子图拓扑和 \([1,2]\) 上的单值 family 紧一致拓扑。它证明“所有 PPA 收敛算子”并非自动闭；**它不证明该类一定不是 Baire**。后一个问题需要独立的描述集合/完全可度量性分析。

## 7. 局部图块如何嵌入完整体系

设 \(\Gamma\subset G\) 是拟使用的局部图块。定义

\[
J_\lambda^\Gamma(x)
=\{y:(y,(x-y)/\lambda)\in\Gamma\}.
\tag{7.1}
\]

对同一个固定 \(\Gamma\)，相应族仍满足 (2.1)。但要在输入区 \(U_\lambda\) 上认证完整 PPA，必须有

\[
U_\lambda\subset\operatorname{dom}J_\lambda^\Gamma,
\quad
G\cap L_\lambda^{-1}(U_\lambda\times H)\subset\Gamma.
\tag{7.2}
\]

第二项正是全部纤维覆盖，保证 \(J_\lambda^\Gamma=J_{\lambda F}\) 在 \(U_\lambda\) 上，而非只有选中的分支正确。对一个步长区间必须逐 \(\lambda\) 要求 (7.2)。

**局部图 germ 本身不确定完整 resolvent 的局部行为。** 取 \(F_0=I\)，并令

\[
\operatorname{gph}F=operatorname{gph}I\cup\{(1,-1)\}.
\tag{7.3}
\]

两者在 \((0,0)\) 的小图邻域完全相同，零集也相同，但

\[
J_{F_0}(0)=\{0\},\qquad J_F(0)=\{0,1\}.
\]

远图点通过 \(u+\lambda v\) 的抵消可以进入任意小输入域。任何局部定理向全 PPA 的嵌入都必须处理这一点。

同理，真实原算子残差是

\[
r_F(u)=\inf\{\|v\|:(u,v)\in G\},
\tag{7.4}
\]

而非 \(\Gamma\) 内的最小值。\(r_\Gamma(u)\ge r_F(u)\)，因此对单调 gauge \(\psi\)，仅有 \(d(u,S)\le\psi(r_\Gamma(u))\) 一般不推出真实 EB。局部证书与底层完整图必须分层保存。

## 8. 什么条件能把一个步长扩展到附近步长

设完整 \(T=J_{\lambda F}:H\to H\) 单值全域，且反射 \(R=2T-I\) 全局 \(L\)-Lipschitz。由 (2.4)，

\[
Q_c=\frac{1+c}{2}I+\frac{1-c}{2}R.
\tag{8.1}
\]

若

\[
\Delta(c,L):=(1+c)-|1-c|L>0,
\tag{8.2}
\]

则 \(Q_c\) 双 Lipschitz 且满射。下界来自三角不等式；满射来自对每个 \(z\) 以

\[
x=\frac{2}{1+c}z-\frac{1-c}{1+c}Rx
\]

应用压缩映射定理。于是 \(J_{\mu F}\) 完整单值全域。又

\[
R_\mu(Q_cx)
=\frac{1-c}{2}x+\frac{1+c}{2}Rx,
\]

故

\[
\operatorname{Lip}R_\mu
\le
\frac{|1-c|+(1+c)L}{(1+c)-|1-c|L}.
\tag{8.3}
\]

这一推导由团队接口代理给出后再次独立代数复核。它给出真实的“步长图表迁移”定理：全局有限 Lipschitz resolvent 几何必有一个可容许开步长窗口。若 \(L\le1\)，全部正步长均满足 (8.2)，对应单调背景的稳定性。

局部版只能在共同邻域、边界余量、全部纤维控制下使用；不能用局部 Lipschitz 常数直接宣布全域满射，也不能忽略 (7.3) 的额外图点。

Hölder 指数 \(\gamma<1\) 单独不提供同类开窗口。以 \(\lambda=1\) 和完整单值

\[
T(x)=|x|^\gamma
\]

按 (1.3) 重构闭图 \(F\)。对任何 \(c>1\)，
\(Q_c(0)=Q_c(r)=0\)，其中
\(r=((c-1)/c)^{1/(1-\gamma)}>0\)；对任何 \(0<c<1\)，
\(Q_c(0)=Q_c(-r)=0\)，其中
\(r=((1-c)/c)^{1/(1-\gamma)}>0\)。这些原像的 \(T\) 输出不同。因此任意 \(\mu\ne1\) 的完整 \(J_{\mu F}(0)\) 都多值。

此例仅用于否定“闭图＋Hölder 单步性质自动推出开步长窗口”；**不声称它满足严格 RLEB 收敛证书**。是否完整 RLEB 额外结构能产生某种步长窗口，是另一个可研究定理。

## 9. 纲比较应在哪一层、以什么量词陈述

| 所用对象/空间 | 结论的准确含义 | 不能自动推出 |
|---|---|---|
| 全闭图 \(F\) 的 AW 空间 | 算子类本身的图拓扑类别 | 其收敛子类内的相对类别 |
| 任一完整 \(J_{\lambda F}\) 关系，使用输送图拓扑 | 与同一 \(F\)-空间完全等价 | 若再限为连续单值，就不再是原母类 |
| 满足 (2.1) 的全 relation-family | 与 \(F\)-空间同胚；步长量词清楚 | 各步长可独立选取或 independently generic |
| 单值连续 family 的指定良定图表 | 该共同良定性层内的类别 | 全闭图母空间中的类别 |
| \((F,\Sigma)\) 或带具体选择规则的算法实例 | 指定算法政策下的动力类别 | 同一 \(F\) 其他步长/选择下的性质 |
| 加统一 RL/EB/留域预算的证书空间 | 带证书对象的类别 | 去除证书标签后算子像的类别 |

所有“RLEB 比 LT 多多少”的结论均应先指定是哪个表格行、是绝对类别还是相对类别。

设 \(\mathfrak L_\lambda\) 为某一步长下可被完整 LT 证书认证的 \(F\) 类。即使每个 \(\mathfrak L_\lambda\) 第一纲，仍不能直接推出

\[
\bigcup_{\lambda>0}\mathfrak L_\lambda
\]

第一纲，因为这是不可数并。最小逻辑反例是实轴的每个单点第一纲，但所有单点之并为整个实轴。

若已经严格证明“一个证书成立则在某个开步长区间仍成立”，才可把存在步长约化到有理步长并。全局有限 Lipschitz 的几何部分可用 (8.2)–(8.3)；完整收敛证书还要同步迁移 EB、严格阈值、局部域与覆盖，不能仅迁移一个 Lipschitz 常数。

类似地，证书到算子的遗忘映射通常是多对一投影；第一纲集的连续像可能不是第一纲。类别从带标签空间下降到无标签算子空间，需要专门的投影/开放映射/可数化论证。

## 10. 推荐的体系顺序与仍需证明的事项

推荐以如下独立于 RLEB/LT 标签的顺序搭建：

1. **对象公理**：闭图 \(G\)，必要时固定解集切片；证明 (1.1)–(3.4) 的表示与拓扑等价。
2. **算法公理**：给定步长策略 \(\Sigma\)、初值/工作域、全选择或指定选择、强/弱收敛；用 (6.1)–(6.2) 建立统一动力对象。
3. **动力性质层**：可解、单值、连续、吸收解集、轨道预紧、渐近正则、点收敛、统一尾界、稳定性等。这些是图/轨道空间中的独立可研究性质。
4. **证书嵌入定理**：分别证明 RLEB、LT、单调等假设推出第 3 层中的哪些性质，并明确局部完整性及步长策略。
5. **无标签类比较**：在事先确定并证明为 Baire 的母空间或动力子空间内，研究证书可认证算子的像、闭包、内点和纲大小。

本报告已证明前两层中的基本表示/完备性/闭动力关系，不证明后两层的类别结论。尚未解决的核心事项是：

- 选定 \(\Sigma,D,S\) 后，全部 PPA 收敛类的准确描述集合复杂性、Baire 性，以及其自然完备表示；
- 哪一种独立动力性质层足够宽，同时允许 RLEB 与 LT 的完整证书自然嵌入；
- 证书类投影到无标签 \(F\)-空间后的类别迁移；
- 全步长族上的可容许区间是否由 RLEB 的某些弱附加结构推出；
- 真正的 LT/RLEB 类别比较定理。

这些问题不由尖点例子、某个有限参数族或上面基础空间的完备性自动回答。本文构造的是可承载这些问题的公共框架。

## 11. 已读原始文献与使用界限

1. Heinz H. Bauschke, Sarah M. Moffat, Xianfu Wang, **Firmly nonexpansive mappings and maximally monotone operators: correspondence and duality**, arXiv:1101.4688。已读 Fact 1.2、式 (9)–(15)、Theorem 2.1 的对应关系。它提供最大单调/firmly-nonexpansive 的经典 Minty 对应；本文一般闭图的 (1.1)–(2.2) 是直接集合代数，不假借最大单调假设。[原始全文](https://arxiv.org/pdf/1101.4688)

2. Xianfu Wang, **Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent**, arXiv:1301.6443。已读 Proposition 1.3、Proposition 1.5、Propositions 2.1/2.3/2.4。它已建立最大单调、resolvent、非扩张映射空间间的对应和完备度量；Proposition 2.3(ii) 明确把通常 graphical convergence 的等价结论限制在有限维。不能把该文的有界一致拓扑、逐点拓扑和一般 Hilbert 的图收敛无条件视为同一拓扑。[原始全文](https://arxiv.org/pdf/1301.6443)

3. Rostyslav Voytsitskyy, **Hyperspaces with the Attouch–Wets topology homeomorphic to \(l_2\)**, *Matematychni Studii* 29(2), 207–214 (2008), arXiv:0803.2098。已读 §2 的 AW metric 定义、脚注中 Beer 的和式版本及 Proposition 2 的 bounded-excess 刻画。本文的 shear 同胚证明使用这一标准拓扑；完整性另外给出独立证明。[原始全文](https://arxiv.org/pdf/0803.2098)

4. Andrei Sipoş, **Revisiting jointly firmly nonexpansive families of mappings**, arXiv:2006.02167v3。已读 §3 和 **Theorem 3.3**：在 CAT(0) 空间，各 \(T_\gamma\) 非扩张且满足经典 resolvent identity，当且仅当 family jointly firmly nonexpansive。该文原式写 \(t\in[0,1]\) 而 family 只在正参数定义；在本文引用时取 \(0\le t<1\)，避免无定义的 \(T_0\) 端点。上述 §4.1 的单调层不能作为新内容包装。[原始全文](https://arxiv.org/pdf/2006.02167)

5. Laurenţiu Leuştean, Adriana Nicolae, Andrei Sipoş, **An abstract proximal point algorithm**, *Journal of Global Optimization* 72 (2018), 553–577，DOI: [10.1007/s10898-018-0655-9](https://doi.org/10.1007/s10898-018-0655-9)，arXiv:1711.09455。已读 **Theorems 3.13/3.15**（jointly (P2)/jointly FNE、共同固定点、\(\sum\gamma_n^2=\infty\) 下的 \(\Delta\)/弱收敛）、**Theorem 5.1**（uniform (P2) 下强收敛与定量率）及序言末尾对非凸弱单调/多值 resolvent 的扩展讨论。family 的公理化 PPA 收敛路线已有直接先例；该文不提供一般闭图非单调母空间的 Baire 分类。[原始全文](https://arxiv.org/pdf/1711.09455)

以上原始材料足以支持“算子图/映射空间及其 Baire 语言不是从零发明”。它们并没有在此被拿来声称已经证明一般非单调 PPA 收敛类与 RLEB/LT 的大小比较。
