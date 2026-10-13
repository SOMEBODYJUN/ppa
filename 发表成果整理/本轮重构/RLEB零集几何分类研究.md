# RLEB 认证零簇的几何分类：回缩、指数与嵌入补偿

日期：2026-10-13。研究基线：`a13da078bc41270a4788ecdf842ca2f429f83958`。本轮只写研究报告、候选证明卡和可复算代码，不修改活跃论文、摘要、规范定理或编号。新增 ENR 指数桥和分量 Euler 公式保留候选身份；显示证明已分别受到独立攻击，内部复核不等于发表先行性认证。

**研究问题与正向回答。** 在 RLEB 及相应局部／全局条件已经成立以后，零点集合必然有什么可画出的特点？三个递进层次分别是：局部连续近端与统一消失尾界使零簇成为可连续收拢的邻域回缩；紧零簇的吸引几何及全局指数限制未知零点的补偿区域；所有初值进入同一局部吸引域则使零簇整体可缩。它们不强迫零集凸、光滑或只有一个点。以下反例用于标明这些正向结论需要哪些条件，不把研究问题替换成“从形状反推 RLEB”。

直观图见[图件及图注](RLEB零点集合直观特征_图注.md)：孤立点、闭环和有角点的零区域均可呈现；连续单值局部分支排除 Cantor 式无限碎裂；严格环形整管加全局指数条件迫使环内有额外零点；全域吸引则排除不能整体缩成点的环形完整零集。

## 1. 先冻结被分类的对象

固定有限维物理空间 $X=\mathbb R^n$、完整关系 $F:X\rightrightarrows X$、步长 $\lambda>0$，以及非空闭目标 $M\subset S:=\operatorname{zer}F$。普通 PPA 是

\[
J_{\lambda F}(x)=\{y:(x-y)/\lambda\in F(y)\},\qquad
r_F(y)=\inf_{w\in F(y)}\|w\|.
\]

分类时还必须写定允许关系 $\mathcal J$、输入域 $U$、认证半径及全部常数。若 $\mathcal J$ 只是完整近端的一部分，结论先属于该允许算法；全文需要完整零点／固定点对应时，另核 $\mathcal J=J_{\lambda F}$。本文的反例和显式方形例都采用完整关系，$v=I,\lambda=1$。

[C02-v3](../../research/canonical/true_residual_selection_rleb.md) 对所有允许输出统一给出

\[
d(x^{k+1},M)\le\kappa d(x^k,M),\qquad
\sum_{j\ge k}\|x^{j+1}-x^j\|
\le\Theta(d(x^k,M))\le\Theta(\kappa^kR),
\tag{G0}
\]

其中 $0<\kappa<1$，$\Theta(0)=0$，$\Theta(t)\to0$。它不自动给单值性或连续性。下面的几何结论须增加：同一个物理近端算法在开局部域上是连续单值 $T$，零点驻定，严格预算证明留域。全对 RL 图块可以供应其中一部分，但仍须单独核输入 coverage 和完整纤维桥。

因此本文分类的基本字段是 $(F,M,\mathcal J,\lambda,v,U)$ 及证书；“$F$ 是 RLEB”只能作为冻结这些字段后的简称。同一个 $F$ 对某些零簇通过，对另一些零簇可能失败。

**连续性门确实不可删。** 对任意非空闭 $K\subset\mathbb R^n$，取固定 $\lambda=1$ 的完整关系

\[
\operatorname{gph}F_K
=\{(y,x-y):x\in\mathbb R^n,\ y\in P_K(x)\}.
\tag{G0a}
\]

完整 $J_{F_K}(x)=P_K(x)$，因为图点里的输入由 $x=y+w$ 唯一恢复；$\operatorname{zer}F_K=K$，$r_{F_K}(y)=0$ 于 $K$，在 $K$ 外为 $+\infty$。图闭，全部输入均有最近点，全部完整输出均在 $K$。对任一输出取最近锚 $p=y$，则 $\|2y-x-p\|=d(x,K)$。C02-v3 取

\[
U=\mathbb R^n,\quad R=\bar t=1,\quad L=\gamma=1,\quad
\psi(t)=t/4,\quad\kappa=1/2
\]

全部通过：输出真 EB 为 $0\le\psi(0)$，窗口上界为 $1$，直接兼容为 $t/4\le t/2$，长度预算 $2d$ 留域自动成立。每条完整轨道一步进入 $K$ 后驻定；零距离输入 $x\in K$ 只有自身输出。坐标原点 $x=0$ 是否多值则取决于 $K$，例如 $K=\{-1,1\}$ 时完整纤维有两个输出。若 $K$ 是 Cantor 集，这一近端多值并且没有连续选择，仍非 ENR。

这说明**锚定型多值 RLEB 仅凭自身，不排除任何非空闭零集形状**。G0a 是根据全部最近点投影生成的机制关系，不冒充一般非凸指标函数的完整次微分；最近点算法本身等于全局近端最小化 $\delta_K(y)+\|y-x\|^2/2$。同输入的不同输出会直接反驳全对 RL，所以该例没有全尺度完整反射证书。后续 ENR 分类严格属于增加了连续单值物理映射门的 RLEB–Euler 分支。该对照的完整纤维、远端、零输入和真残差另经独立攻击确认。

## 2. 局部本质：统一收敛产生邻域回缩

设同一连续单值 $T$ 在 $M$ 的开吸引域 $O$ 上前向不变，满足 G0。每个 $T^k$ 连续，尾界对 $x\in O$ 统一趋零，故

\[
P(x):=\lim_{k\to\infty}T^kx
\]

连续。距离趋零、物理尾可和及闭 $M$ 给 $P(x)\in M$；零距离输入驻定给 $P|_M=I$。所以 $M$ 是开集 $O$ 的连续回缩，即 Euclidean neighborhood retract（ENR）。这是 [C11](../../research/canonical/general_modulus_dynamics.md#gm-retraction) 已有的结构；对 C02-v3 的连续单值版本，同一证明直接适用。

开域不能省略。C02-v3 的连续长度预算给

\[
O=\{x\in U:d(x,M)<R,\ \Theta(d(x,M))<d(x,U^c)\}.
\]

利用 $\Theta(t)=B(t)+\Theta(\kappa t)$ 与一步上界 $s\le B(d)$，可核 $T(O)\subset O$。对一般物理 C249 的仅零点连续模，$\Theta$ 未必在正尺度连续；此时应先取右上包络或缩小开球并构造开吸引域，不能把上式不加核验地称为开集。修复详见[内禀卡](../../research/candidates/rleb_zero_geometry_intrinsic.md)。

局部可缩的准确含义也可直接证明。给 $p\in M$ 及其相对邻域 $V$，由 $P$ 连续，取小球 $B_a(p)\subset O$ 且 $P(B_a(p))\subset V$。则

\[
H(q,t)=P((1-t)q+tp),\qquad q\in M\cap B_a(p),
\]

把这个较小邻域的包含映射在 $V$ 内同伦为常值 $p$。不据此声称该较小邻域自身可缩，也不声称 $O$ 强形变回缩到 $M$。

由此得到真实的几何排除：Cantor 式完全碎裂、无限组件在目标内部聚积且破坏局部可缩的零簇，不能满足上述连续、统一物理 RLEB 门。若整个 $M$ 紧，则其组件只有有限个，并具有有限维有理同调。另一方面，这一结论没有给正 reach、曲率、维数、光滑性或凸性。

## 3. 紧 ENR 的指数桥：可去掉预设光滑流形

下面是本轮候选扩展，尚不替换规范 C254。假定 $M$ 非空紧，$T$ 在其邻域连续单值，$T|_M=I$，并满足 G0 和相同的统一尾。选足够小 $0<a<c$ 使 $\kappa c<a$，并令闭 $c$-邻域位于吸引域内。取有限 cubical polyhedron $K$，满足

\[
N_a(M)\subset\operatorname{int}K\subset K\subset N_c(M).
\]

于是 $T(K)\subset N_{\kappa c}(M)\subset\operatorname{int}K$。记 $A=T|_K$、$j:M\hookrightarrow K$、$p=P|_K$。统一收敛给某个整数 $m$，使 $\|T^mx-Px\|<a$ 在 $K$ 上同时成立；从 $T^m$ 到 $jp$ 的直线同伦留在每个 $P(x)$ 周围的 $a$-球，因而留在 $K$。所以

\[
A_*^m=j_*p_*,\qquad pj=I,\qquad Aj=j,\qquad pA=p.
\]

在有理同调上

\[
H_q(K;\mathbb Q)=j_*H_q(M;\mathbb Q)\oplus\ker p_*.
\]

$A_*$ 在第一项为恒等，在第二项幂零；第一项有限维，因为它是有限 polyhedron 同调的直和项。因此 $L(A)=\chi(M)$。经典紧 ENR 指数正规化、交换性和局部化将其转回环境局部指数，得到

\[
\boxed{i(T,V_M)=\chi(M).}
\tag{G1}
\]

这里 $V_M$ 是充分小的隔离邻域；完整 $T$ 时局部固定点恰为 $M$，因为严格距离收缩排除 $M$ 外固定点。证明没有预设 $K$ 形变回缩到 $M$，也没有把 $T^m$ 的指数误当作 $T$ 的指数；幂零分项正是这一缺口的承重步骤。

经典接口为 Benjamin–Gottlieb, *Fixed Point Indices and Manifolds with Collars*，作者九页 PDF，§2.1.1、§2.1.4、§2.1.6。转到环境指数时，取 $K$ 的开邻域 $W$，同时要求 $W$ 留在原认证域内且 $T(W)\subset\operatorname{int}K$；如此两边的固定点集恰为同一 $M$。这里只导入其指数性质，G0 到回缩及幂零同调桥是本对象的推导。参见[完整证明卡](../../research/candidates/rleb_zero_geometry_intrinsic.md)。

## 4. 一套明确的四类几何，但不是准入充要分类

在“有限维、紧目标、连续单值完整近端、统一物理尾”这个共同范围中，可按下表分四类。全局列另外要求总固定点指数为 $1$；若下表对象只作局部目标，$S$ 仍可能比 $M$ 大。

| 目标零簇几何 | 局部连续 RLEB 的限制 | 总指数 $1$ 后的限制 | 全部初值吸引到它 |
|---|---|---|---|
| 非 ENR：Cantor 等局部碎裂集合 | 被邻域回缩结论排除 | 不可直接写 $i=\chi(M)$ | 点态收敛仍可能存在，见完整 Cantor PPA |
| ENR 且 $\chi(M)\ne1$：圆、球面、双柄曲面、多个孤立吸引点 | 可局部认证，仍须核解析门 | 外部固定点净指数必须为 $1-\chi(M)\ne0$ | 被可缩性排除 |
| ENR、$\chi(M)=1$ 但不可缩：$\mathbb{RP}^2$ | 不被局部几何排除 | 总 Euler 缺额为零；一般嵌入还查逐分量缺额 | 被可缩性排除；可能没有额外零点而存在其他极限行为 |
| 可缩紧 ENR：点、凸方形等 | 通过这些拓扑必要门，仍不保证给定算法 RLEB | 总 Euler 缺额为零 | 拓扑上允许，须另证动力条件 |

这是一套必要约束和障碍分类。它没有证明每个 ENR 都能按指定常数、指定完整图实现 RLEB，也没有提出有效的 ENR 识别算法。对于既有的光滑整管完成合同，下一节的分量向量才给精确的存在式零点代价分类。

## 5. 全局条件与零点补偿

一种具体全局入口是完整 $T:\mathbb R^n\to\mathbb R^n$ 连续单值，反射 $C_T=2T-I$ 有全尺度 Hölder 界，指数 $0<\gamma_*<1$。于是

\[
\|C_T(x)\|\le\|C_T(0)\|+L_*\|x\|^{\gamma_*}=o(\|x\|).
\]

充分大球面上 $x-sC_T(x)$ 对所有 $0\le s\le1$ 非零。因此全部固定点位于一个紧球内，且 $\deg(I-T,B_R,0)=1$。也可以使用已经独立核验的凸不变域和边界同伦；非原点居中凸域应同伦到域内常值点，不能默用 $I-sT$。

G1 与指数加法性给

\[
\boxed{i(T,B_R\setminus\overline{V_M})=1-\chi(M).}
\tag{G2}
\]

右端非零就保证 $M$ 外存在固定点，完整 PPA 时即额外零点。只得到净指数，不自动得到 $|1-\chi(M)|$ 个零点；单个退化点可承载任意整数指数。若全部额外点孤立且非退化，每点指数 $\pm1$，才有相应数量下界。

若把 $M$ 改成完整零集 $S$，又在全部 $S$ 上通过局部门，就得到 $\chi(S)=1$。例如完整零集若有限且每点都通过同一局部吸引结构，只能有一个点；多个已认证吸引点必须由未通过该局部门的其他零点补偿。不能用仅在部分吸引点上成立的 RLEB，把整个驻点集的指数都改写成正值。

## 6. 比总 Euler 更细：补集区域决定补偿位置和锐数量

沿用 [C236](../../research/canonical/sharp_completion_cost.md) 的准确合同：$n\ge2$，紧纯维 $C^2$ 无边界嵌入流形 $M$，$\rho<\operatorname{reach}(M)$，完整指定整管 $N_\rho$ 上的 $T_0$，$T_0|_M=I$ 且 $d(T_0x,M)\le\theta d(x,M)$、$\theta<1$。允许全域完成使用某个有限新 Hölder 常数，保持整个原输入管。

设大球中的管外连通区域为 $W_j$，含外球边界者为 $W_\infty$。本轮从严格管合同推得边界位移方向同伦于管法向，再用向外 Gauss map degree 定理，得到

\[
\delta_j=(-1)^n\chi(W_j)\quad(j\ne\infty),\qquad
\delta_\infty=1+(-1)^n(\chi(W_\infty)-1).
\tag{G3}
\]

同伦不能只写线性插值：对管边界 $x$ 用 $z_t=\Pi x+(1-t)(x-\Pi x)$、$h_t=T_0z_t$，严格收缩给 $d(h_t,M)<\rho=d(x,M)$，故 $x-h_t$ 永不为零，终止方向为 $x-\Pi x$。区域内管边界上它是 $W_j$ 的向内法向；反足次数是 $(-1)^n$。外球单独贡献 $1$。这是 G3 的全部符号来源。

C236 的存在与锐达到结论给

\[
\min\#(S\setminus M)=\#\{j:\delta_j\ne0\},\qquad
\min\#(S\setminus M)_{\rm nondeg}=\sum_j|\delta_j|.
\tag{G4}
\]

因此可以进一步分为所有 $\delta_j=0$ 的零点保留类、一个非零缺额区域的集中补偿类、多个非零区域的分散补偿类。它们是上述完成合同的精确分类，不是固定原常数的分类。

| 嵌入目标 | $\chi(M)$ | 按区域的缺额 | 最少一般补偿点 | 最少非退化补偿点 |
|---|---:|---|---:|---:|
| 单圆 $S^1\subset\mathbb R^2$ | 0 | 内 $1$，外 $0$ | 1 | 1 |
| $S^2\subset\mathbb R^3$ | 2 | 内 $-1$，外 $0$ | 1 | 1 |
| 两个嵌套平面圆 | 0 | 最内 $1$，中间 $0$，外 $0$ | 1 | 1 |
| 两个互不嵌套平面圆 | 0 | 两个内部各 $1$，共同外部 $-1$ | 3 | 3 |
| 标准双柄曲面 $\Sigma_2\subset\mathbb R^3$ | $-2$ | 有界侧 $1$，外侧 $2$ | 2 | 3 |
| 同一 $\Sigma_2\subset\mathbb R^4$ | $-2$ | 唯一补集 $3$ | 1 | 3 |
| $\mathbb{RP}^2\subset\mathbb R^5$ | 1 | 唯一补集 $0$ | 0 | 0 |

同一抽象零流形的不同嵌入可改变补偿位置和最少点数；这一信息不能由总 Euler 数恢复。两圆例子是最短的正文解释。高余维补集连通用 Hatcher Theorem 3.44 的 Alexander duality，具体适用条件见[分量证明卡](../../research/candidates/rleb_component_index_classification.md)。

范围修正：在 C236 的纯维紧无边界欧氏流形合同中，$\chi(M)=1$ 排除余维一，强迫余维至少二，因而补集连通，有限新常数下无额外零点完成已经可能。“圆加外部孤立点”是混合维集合，不能用来暗中反驳该纯维结论。若扩展到混合维 ENR，必须另证相应邻域及延拓合同。

## 7. 上表确实有完整局部 RLEB，不只是画出一个管映射

取 $T_0=(I+\Pi)/2$。任一保整管的完成 $\widehat T$ 都用完整图

\[
\operatorname{gph}\widehat F
=\{(\widehat T(x),(x-\widehat T(x))/\lambda):x\in\mathbb R^n\}.
\]

Minty 输入从图点唯一恢复，所以完整 $J_{\lambda\widehat F}=\widehat T$，全输入覆盖，全部纤维单值；$\widehat F$ 本身可以多值。对 $y\in N_{\rho/2}(M)$，令 $s=d(y,M)$。唯一管内反输入为 $x_{\rm loc}=\Pi y+2(y-\Pi y)$，其图值范数是 $s/\lambda$。管外任一反输入满足

\[
\|x-y\|>\rho-s\ge s,
\]

因为距离函数 1-Lipschitz。因此**完整**真残差精确为 $r_{\widehat F}(y)=s/\lambda$，远端完整纤维不会降低下确界。零输出也成立。

取 $U=\operatorname{int}N_\rho$、$R=\rho/3$、$\gamma=1,L=0$、$\psi(t)=\lambda t$、$\bar t=R/(2\lambda)$、$\kappa=1/2$。最近锚 $p=\Pi x$ 给 $2T_0x-x-p=0$；完整输出 EB、窗口与直接兼容取等；长度预算 $\Theta(d)=d<\rho-d=d(x,U^c)$ 对所有合法初值成立。精确轨道及极限是

\[
x^k=\Pi x^0+2^{-k}(x^0-\Pi x^0),\qquad x^\infty=\Pi x^0.
\]

这关闭了“只保输入管，不保完整输出纤维，因而 EB 未核”的危险接口。它仍是几何机制构造，不能伪称某个实际模型原生提供此管与完成。

## 8. 进一步要求全域吸引，会强迫可缩

设完整 $T:\mathbb R^n\to\mathbb R^n$ 连续，已有 $M$ 的上述开吸引域 $O$，$M$ 紧，并另证每个全空间轨道满足 $d(T^kx,M)\to0$。紧性使 $O$ 包含一个统一小领圈，所以每个初值都在某个有限时刻进入 $O$。在该初值的邻域定义

\[
P_{\rm glob}(x)=P(T^mx).
\]

这些局部定义由 $PT=P$ 相容，拼成全域连续回缩 $P_{\rm glob}:\mathbb R^n\to M$。给 $p_0\in M$，$P_{\rm glob}((1-t)p+tp_0)$ 是 $M$ 到单点的收缩同伦，所以 $M$ 可缩。这里的连续性来自先前的局部统一尾与有限进入，不来自一般点态极限。

因此 $\chi(M)=1$ 还不够：$\mathbb{RP}^2$ 的整同调有 $\mathbb Z_2$ 挠项，虽 $\chi=1$，仍不可缩。C234 的无新零点完成不可能使所有初值趋近它；次线性反射又给有界轨道，于是至少有管外的非固定点 $\omega$ 极限行为。不能进而宣称周期或混沌。若目标是正维紧无边界流形，可缩性排除它；零维时只剩单点。若目标有边界或奇点则不能套用这一“只剩单点”，下一方形例正好说明。

## 9. 同一零集、相反的严格证书：零集不决定 RLEB 归属

对 $S=\{0\}$，取两个完整普通 PPA：

\[
F_{\rm good}(y)=y,\qquad
F_{\rm flat}(y)=y e^{-1/y^2}\ (y\ne0),\quad F_{\rm flat}(0)=0.
\]

它们分别是严格凸强制目标 $y^2/2$ 与 $\int_0^y s e^{-1/s^2}\,ds$ 的梯度。$I+F_i$ 全域严格单调满射，所有完整纤维唯一，两种 PPA 均从每个初值有限长度趋零，总长 $|x^0|$。共同零集、共同总指数 $1$，共同全局有界非扩张反射，均有真 EB。

良性例 $T=x/2$ 以 $L=0,\gamma=1,\psi=t,\kappa=1/2,R=\bar t=1,U=\mathbb R$ 精确通过 C02-v3。平坦例则在输入 $x=y+F(y)$ 上有

\[
\frac{|Tx|}{|x|}=\frac1{1+e^{-1/y^2}}\longrightarrow1.
\]

因严格证书必先推出统一一步 $d(Tx,S)\le\kappa d(x,S)$，平坦例排除**任意**同算法、同物理距离严格 C02-v3／C250 元组，不只是某个幂 gauge 失败。其仍有 $\psi=(t e^{-1/t^2})^{-1}$ 的非幂型 EB，经典单调凸 PPA 仍有效。完整证明与精度边界见[对照卡](../../research/candidates/rleb_same_zero_set_countermodels.md)。

## 10. 野性零集仍可以有完整 PPA 和所有轨道收敛

令 $C$ 为三分 Cantor 集，定义完整单值

\[
F(y)=\begin{cases}y,&y<0,\\d(y,C)/2,&0\le y\le1,\\y-1,&y>1.\end{cases}
\]

$F$ 全局 1-Lipschitz 且 $F+I/2$ 单调，$H=I+F$ 为全域 $1/2$-强单调同胚。完整 $T=H^{-1}$，也是 $f(y)=\int_0^yF$ 的唯一完整 proximal argmin。$f\in C^{1,1}$、$1/2$-弱凸且强制；$C$ 是完整驻点集，**唯一全局极小点是 $0$**。

每个间隙 $(a,b)$，$\ell=b-a$，完整反演是

\[
T(x)=a+\tfrac23(x-a)\quad(x\le a+3\ell/4),\qquad
T(x)=b+2(x-b)\quad(x\ge a+3\ell/4).
\]

再加 $T|_C=I$、外侧两条 $1/2$ 分支，覆盖全部输入。反射全局有界且 3-Lipschitz，真 EB 全域 $d\le2r_F$；每条轨道都有限长度收敛。可是 $x=b-\varepsilon$ 给

\[
d(Tx,C)=2\varepsilon=2d(x,C),\qquad
P(x)=a,\quad P(b)=b.
\]

极限在右端跳跃；总长度趋间隙长 $\ell$，不随初始距离 $\varepsilon\to0$ 而趋零。Cantor 集不能是开邻域的连续回缩。故完整 coverage、完整真 EB、全局反射控制、全部轨道逐一有限长度乃至总指数 $1$，仍不能替代统一物理 RLEB 门。这是刻意构造的机制反例，不作为自然应用。见[完整卡](../../research/candidates/rleb_cantor_zero_geometry.md)。

## 11. 凸方形：局部几何结论不要求光滑无边界零流形

取 $K=[-1,1]^2$，$F(y)=y-P_Ky=\nabla(d_K^2/2)$。固定 $\lambda=1,v=I$。逐坐标完整反演 $x=2y-P_Ky$ 得

\[
T(x)=(x+P_Kx)/2,\qquad S=K,\qquad r_F(y)=d(y,K).
\]

所有完整纤维唯一，全输入覆盖。对最近锚 $p=P_Kx$，反射 $2Tx-x=p$，真实 EB 为等式。取 $U=\mathbb R^2,R=\bar t=1,L=0,\gamma=1,\psi=t,\kappa=1/2$，全部 C02-v3 门通过。轨道是 $p+2^{-k}(x-p)$，极限 $p$，总长 $d(x,K)$。全局反射是有界非扩张的 $P_K$，也满足任意指数 $0<\gamma_*<1$ 的全尺度界。

$K$ 有角点和边界，但为可缩 ENR，$\chi(K)=1$。这是经典凸优化基准，说明局部 RLEB 不强迫目标光滑、无边界或零维；它不展示超越单调 PPA 的优势。平方距离和完整反算在精确代码中核了边界、角点与远端输入。

**有限分叉已补成完整正例。** [十字零集证明卡](../../research/candidates/rleb_cross_zero_set.md)给出整个有限十字为完整零集的关系：完整 PPA 全输入连续单值、完整全尺度 Hölder–RL、同一局部真残差 RLEB 常数，以及所有初值有限步到零集。它非凸且交点不是流形，最近点还可多值；算法诱导的极限回缩仍连续。该机制实现不作为原生优化应用，但使“有限分叉未被排除”从拓扑允许性推进为已完整验证的实例。其算子不单调，不能将此分支的共同几何属性概括成凸性或单调性。137 个精确输入、9316 点对复算通过，完整纤维、低残差窗与全部远端输出另经独立 ultra 审查。

## 12. 与已有理论的真实关系及研究方向

**从不能出现的形状抽离出的属性。** 对被认证零集，当前严格 RLEB 的共同动力结论是相对于零集的统一距离吸引，以及趋近过程中可和的物理位移。连续单值完整近端分支再把这种动态规则变成零集的邻域回缩与局部可缩性。具体写成

\[
d(Tx,S)\le\kappa d(x,S),\qquad
\sum_{j\ge k}\|T^{j+1}x-T^jx\|
\le\Theta(\kappa^k d(x,S)),\qquad\Theta(t)\to0\ (t\downarrow0).
\]

连续 $T$ 下，由此得到 $P=\lim T^k$、$P|_S=I$、$PT=P$ 和 $\|P(x)-x\|\le\Theta(d(x,S))$。Cantor 碎裂、孤立组件内部积聚、不可缩小环的无限堆积，都在这项连续邻域回缩门上失败。零点可在集合内部组成连续族，偏离它的距离则必须统一缩小；即使沿零集附近发生漂移，总物理位移也受预算约束。该动态稳定性不等于对算子参数扰动的结构稳定性，不自动给正 reach 或正常双曲性。残差控制的准确作用域仍是认证输出／认证低残差窗，不静默扩大为任意环境点或任意残差尺度。

最一般的锚定多值 RLEB 保留前述距离吸引与位移预算；连续回缩和拓扑排除属于另核连续单值门的分支。这里讨论正向共同属性，不把外形作为准入判据。后续写作应围绕这一动力到几何的推导组织，而不把点、圆、区域的例子目录当作算子本质。

最大单调算子的全域 resolvent 是 firmly nonexpansive，因而其完整零集为闭凸集。凸性也可直接由非扩张固定点证明：两个固定点 $a,b$ 的内分点 $z$，$Tz$ 同时落在半径 $t\|a-b\|$ 与 $(1-t)\|a-b\|$ 的两球内，三角等号迫其为 $z$。这比本文的 ENR 必要门更强，但采用了不同解析前提。原文接口为 Bauschke–Moursi–Wang，作者 PDF 2020-03-08 版，Fact 2.2–2.3；不由此宣称全部经典 PPA 的零集必须凸。

全尺度 Hölder–RL 单独只有直径门，并不自动给回缩。[C04](../../research/canonical/finite_fiber_classification.md) 在其固定参数、图极大合同中允许任意非空紧 $K$ 满足 $\operatorname{diam}K\le L^{1/(1-\gamma)}$ 作为完整零集。与此相比，连续统一 RLEB 的 ENR 限制确实筛除了野性零集。但同一单点的平坦对照证明 ENR 仍远非严格证书的充分条件。

零点补偿的数学本质仍是经典固定点指数、Lefschetz 与 degree 守恒。本项目值得研究的接口是：如何从非 Lipschitz／非单调的完整近端与真残差条件，快捷地认证局部拓扑结构和分量指数输入；哪些真实模型能自然提供这些数据。不能把经典守恒公式改称新的零点存在原理，也不能把经典能量证明可用的模型宣称只有 RLEB 能分析。

已有直接研究固定点集几何的文献也不能遗漏。Hirsch 的 *Topology of Fixed Point Sets of Surface Homeomorphisms*（2000）Theorem 2.6，在保向曲面自同胚及其 Hypothesis (H) 下，从一部分固定组件的 Čech Euler 缺额 $\nu$ 推出 $\nu$ 个互补区域各含额外无环固定组件。其 (H) 包括：完整固定点集非空紧且有限组件、环境 $H_1$ 有限生成、非恒等映射，以及没有预紧且单连通的完整固定点补集组件。这里对象限于曲面自同胚，不能仅由普通 PPA 连续性替代，也不把 Čech Euler 与未经认证的奇异同调混用。这是一条明确的相关几何研究，说明“由已知组件及补集几何推断额外组件”已有经典研究；我们的候选方向应放在 RLEB 的可验证接口及不同条件范围，而非笼统宣称首次研究零点几何。

**新颖性续核（2026-10-13）。** Pérez García–Fetter Nathansky（2010）Lemma 2.1 已从连续辅助迭代的局部共同几何尾界构造固定集回缩；Wiśnicki（2014）Lemma 2.1 给共同增量界下的 Hölder 连续极限，并明确称它为已有结果的变体。两篇原文的对象、条件和页码已记录在 [LIT-ZERO-GEOMETRY-RETRACTION-PRIOR](../../research/LITERATURE.md#lit-zero-geometry-retraction-prior)。因此 C11 的回缩及 ENR 排除应作为可核验 RLEB 收敛证书的结构后果，不能单独承载新拓扑原理的宣称。不同假设的旧引理不因此被说成包含全部 RLEB 定理。

这条研究线的创新强度应分开：固定参数的完整零纤维分类及 C222 精确最小 Hölder 预算达到，是较明确的定量贡献候选；从完整物理 RLEB 证书接出几何与指数，是条件接口贡献；C236 的逐区域锐完成代价，是较有辨识度的结构问题。总 Euler 缺额和局部可缩性属于经典机制的应用。C236 保持任意给定整管 T0，但不自动保持其完整真残差 EB；§7 对法向平均模型核了远端完整纤维，不能把这一特殊桥扩成任意 T0 的现成定理。

Goebel 2016 Claim 1 的逐轨道收敛及线段单调性，已容许任意闭固定集和有限总长；其极限可能不连续。任意指定固定集、单值 Lipschitz 原算子等宽泛存在性不能代替 C04/C222 的预算端点区别。Luke–Tam 2025 Theorem 1 还直接讨论正逆局部纤维的弱凸下水平集结构；“首次研究 PPA 零点几何”不是当前可辩护的表述。经典固定点理论可经完整图坐标写成 PPA，因此仅换名也不是贡献；要保留完整纤维、真残差、精确预算和保动力达到性等额外合同。现有内部证明及这轮有限先行检索仍不认证全球首次。

下一步有意义的三个精确问题是：给定非凸 ENR 零簇，何种完整图的横向增长与锚反射几何能构成可检查准入标准；在原 Hölder 预算下，分量分类的锐完成成本怎样定量化；在真实优化／平衡模型里，哪些补集区域可用低成本证书认证，而无需解出其全部零点。本轮没有关闭这些充分性与算法成本问题。

GPPA 的转接范围也须保持精确：如果已定义的完整物理更新本身连续单值且通过物理 C249／C250 与统一尾，就直接使用以上物理几何。若只在核空间证明结论，必须提供连续、相容的物理提升；非单射核的影子零集不能替代物理零集。只有已核 ambient homeomorphism 的共轭，才可直接搬运回缩与拓扑。任意正定度量对指定模型是否保留覆盖、所有输出、固定点和真残差，需要重新核验，不由这份拓扑报告自动成立。

## 13. 文献、复算与接收范围

一手来源均于本轮打开原文，网页搜索摘要不承担包含关系：

- Benjamin–Gottlieb, *Fixed Point Indices and Manifolds with Collars*，[作者 PDF](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf)，九页版本，印页 3，§2.1.1／.4／.6。导入局部化、紧 ENR 正规化和交换性；没有导入其主定理作为现成 RLEB 结论。[期刊元数据](https://link.springer.com/article/10.1155/FPTA/2006/87657)核定正式版 2006，Article 87657，DOI `10.1155/FPTA/2006/87657`；作者版页码和编号不冒充正式版定位。
- Gottlieb, *Normal Degree and Coincidence Numbers*，[作者 PDF](https://www.math.purdue.edu/~gottlieb/Papers/ndg.pdf)，六页版本，印页 5 的 Theorem。区域包含嵌入满足同维浸入前件，得向外 Gauss 次数 $\chi(W)$。此作者版本未据此认证 DOI 或公开优先性。
- Hatcher, *Algebraic Topology*, CUP 2002，Theorem 3.44，印页 255，[大学镜像原书 PDF](https://math.uchicago.edu/~farb/algtop2023/Hatcher.pdf)。紧、局部可缩、非空真子集的 Alexander duality；这里只用于光滑高余维目标的补集连通。
- Bauschke–Moursi–Wang, *Generalized monotone operators and their averaged resolvents*，[作者 PDF](https://cmps-people.ok.ubc.ca/bauschke/Research/127.pdf)，2020-03-08 版，Fact 2.2–2.3。只调用 firmly nonexpansive resolvent／最大单调的对应与 coverage。[期刊元数据](https://link.springer.com/article/10.1007/s10107-020-01500-6)核定 *Mathematical Programming* 189 (2021), 55–74，在线正式版 2020-04-25，DOI `10.1007/s10107-020-01500-6`；具体条件定位仍使用实际读过的作者版。
- Hirsch, *Topology of Fixed Point Sets of Surface Homeomorphisms*, *Houston Journal of Mathematics* 26(4), 2000，[期刊原文 PDF](https://www.math.uh.edu/~hjm/pdf26%284%29/09hirsch.pdf)，Theorem 2.6，印页 772；Hypothesis (H) 印页 769。只作为不同前提的相关几何研究，未导入为 PPA 定理；所读 PDF 未据此核定 DOI。
- C236 的锐达到性另使用其已核的一手 Hopf 延拓接口；本轮重新核其对象映射，不把 finite-new-constant 合同扩大成保持原常数。

复算命令（仓库根目录）：

```bash
python3 research/code/rleb_same_zero_set_countermodels/verify.py
python3 research/code/rleb_cantor_zero_geometry/verify.py
python3 research/code/rleb_zero_geometry_classification/verify.py
```

Python 3.12.14。三项均已实际重跑通过。平坦例用标准库 binary64 和部分精确多项式算术，601 个输出反算的最大相对误差约 $4.30\times10^{-16}$；Cantor 用 `Fraction` 检查 835 点、35778 点对和 63 个实际间隙；分类验证器精确核了九组指数算术及方形的 81 个输入、3240 点对。Cantor 检查实际无限集的有理三进制循环，不使用有限近似集。所有结果及精度限制分别记录在代码目录的 README 和结果文件；全称结论由显示证明承担。

独立接收覆盖：同零集对照的完整纤维及任意严格元组排除；Cantor 的跨无限间隙全对界、唯一 argmin、完整驻点集、非 ENR 和非统一尾；ENR 指数桥的同调幂零分项与环境指数转接；分量公式的定向、纯维限制和远端完整纤维真残差。没有全库验收、原常数完成算法、任意 GPPA 度量变更或外部新颖性认证。
