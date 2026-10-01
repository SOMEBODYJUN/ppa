# 第 2 组：固定点、单调算子与算法极限回缩的初值稳定性

日期：2026-09-19。范围：固定单值迭代映射 \(T\) 的原 Picard 极限 \(\Pi_Tx=\lim_nT^nx\)，不是参数扰动后的解映射，也不是另外构造的回缩。只核查本次问题与原稿 §5.2 接口，不重新审原 RLEB。

## 1. 直白结论

有人长期研究这个问题，经典答案并不只有“强单调、唯一解”这一种。最重要的现成分层是：

1. 共同轨道区域上的非扩张 \(T\) 加迭代收敛，直接给 \(\Pi_T\) 为 1-Lipschitz；无需唯一解。
2. 更弱的统一幂 Lipschitz 控制 \(\sup_n\operatorname{Lip}(T^n)<\infty\) 也足够；每一步可以扩张。
3. 单步仅为有限常数 Lipschitz（允许 \(L>1\)），结合 RLEB 的共同几何点尾界，已有一般定理给正阶 Hölder 极限选择。这个“加一个条件”的基准结论已知，不应包装成新的抽象定理。
4. 只加 Fejér 单调、quasi-nonexpansive 或 strongly quasi-nonexpansive，不等于两条轨道之间的稳定性证书。这类文献很多，但相当一部分只证明每条轨道收敛。
5. 若要保留原稿真正的 \(\gamma<1\) 非 Lipschitz 算子优势，最值得研究的是切向增益可求和、法向误差可求和地注入切向等“分方向”条件。原稿 §5.2 已经是这个方向的一个严格三角特例。

这些条件不形成完全线性强弱排序。例如“单步 Lipschitz + 几何尾界”和“单步非扩张 + 无速率收敛”不可直接比较；条件的自然性要对具体图块判断。

## 2. 可直接复核的基准证明

### 2.1 非扩张极限继承，不要混淆三件事

设 \(W\) 为共同初值域，所有 \(T^nx\) 留在一个区域 \(V\)，且

\[
\|Tu-Tv\|\le\|u-v\|\qquad(u,v\in V).
\]

若 \(T^nx\to\Pi_Tx\) 对 \(x\in W\) 成立，则

\[
\|\Pi_Tx-\Pi_Ty\|=\lim_n\|T^nx-T^ny\|\le\|x-y\|. \tag{2.1}
\]

这是初等继承，不需要全空间非扩张、不需要统一收敛率、不需要解唯一。在 Hilbert/Banach 空间，如果只有弱极限且属于固定点集，则由范数弱下半连续性同样得 (2.1)；但这不把轨道本身升级为强收敛。

要区分：

- 非扩张本身不保证 Picard 迭代收敛；\(T=-I\) 已是反例。
- averaged/firmly nonexpansive 的经典条件提供弱收敛，有限维时弱强等价；RLEB 可另提供强收敛。
- 原 Picard 极限是非扩张回缩，但一般不等于最近点投影，也不自动 sunny。

最近点辨别的最小二维例：令 \(A=\mathbb R\times\{0\}\)，\(B=\{(u,v):v\ge u\}\)，\(T=P_AP_B\)。两投影复合是 averaged，\(S=A\cap B=(-\infty,0]\times\{0\}\)。但

\[
T(-1,-3)=P_A(-2,-2)=(-2,0)\in S,
\quad\Pi_T(-1,-3)=(-2,0)\ne(-1,0)=P_S(-1,-3).
\]

这是独立算式，不援引某个文献的特例。

### 2.2 统一幂 Lipschitz 比每步非扩张弱

若

\[
\|T^nx-T^ny\|\le M\|x-y\|\quad(n\ge0,x,y\in W), \tag{2.2}
\]

则取极限得 \(\operatorname{Lip}(\Pi_T|_W)\le M\)。例：

\[
T(a,r)=(a+br,qr),\quad 0<q<1,
\qquad
\Pi_T(a,r)=\left(a+\frac b{1-q}r,0\right).
\]

当 \(b\ne0\) 时 \(T\) 可以在 Euclidean 范数下扩张，但 \(T^n(a,r)=(a+b(1-q^n)r/(1-q),q^nr)\) 有统一有限 Lipschitz 常数。没有唯一解，极限仍 Lipschitz。这个例子仅说明条件的严格弱化，不声称满足用户原稿全部新增构造条件。

### 2.3 单步 Lipschitz + 共同几何尾界：已有 Hölder 结论

假设共同域上

\[
\|T^nx-\Pi_Tx\|\le C\tau^n,\qquad
\|Tu-Tv\|\le L\|u-v\|,
\quad0<\tau<1<L.
\]

则对 \(\delta=\|x-y\|\)，

\[
\|\Pi_Tx-\Pi_Ty\|\le 2C\tau^n+L^n\delta.
\]

取 \(n=\lfloor\log(1/\delta)/\log(L/\tau)\rfloor\) 得

\[
\|\Pi_Tx-\Pi_Ty\|\le(1+2C/\tau)\delta^\theta,
\qquad
\theta=\frac{\log(1/\tau)}{\log(L/\tau)}\in(0,1).
\tag{2.3}
\]

尺度单位可预先归一化。这里 \(\tau\) 是实际/已证明的统一“点尾”因子，不能直接拿“到解集距离”因子代入，除非先经过长度预算的转换。\(L\le1\) 时直接用 (2.1)/(2.2)。此段是对 Wiśnicki Lemma 1 的独立平衡计算，绝非新颖性主张。

### 2.4 沿轨道可求和膨胀：适合 RLEB 的接口，但一般乘积估计本身不新

设 \(W_k=T^kW\)，且

\[
\|Tu-Tv\|\le(1+\epsilon_k)\|u-v\|
\quad(u,v\in W_k),\qquad
\epsilon_k\ge0,\quad\sum_k\epsilon_k\le E<\infty.
\]

则

\[
\|\Pi_Tx-\Pi_Ty\|\le\prod_k(1+\epsilon_k)\|x-y\|
\le e^E\|x-y\|.\tag{2.4}
\]

重要量词：\(\epsilon_k\) 必须同时控制同一共同初值域中的所有轨道对，而不是每条轨道各自有一个不可统一的和。

一个可验证的充分接口是：\(d(T^kx,S)\le D\tau^k\) 对所有 \(x\in W\) 统一，并在共同轨道区域满足

\[
\|Tu-Tv\|\le\left[1+c(d(u,S)+d(v,S))^\eta\right]\|u-v\|.
\]

此时可取 \(\epsilon_k=c(2D)^\eta\tau^{\eta k}\)。该接口是本组独立写出的初等推论，尚未做精确文献首见裁定；应标为标准估计/候选证书，而非新定理。它仍要求全方向的有限 Lipschitz 性，不能无损容纳原反例的横向平方根尖点。

### 2.5 Fejér/quasi-nonexpansive 能保证什么、不能保证什么

若 \(T\) 连续，所有轨道强收敛到 \(S=\operatorname{Fix}T\)，并且

\[
\|Tx-s\|\le\|x-s\|\quad(s\in S),
\]

则 \(\Pi_T\) 连续。独立证明：固定 \(x\)，选 \(N\) 使 \(T^Nx\) 靠近 \(\Pi_Tx\)。有限步 \(T^N\) 连续，而 quasi-nonexpansiveness 给

\[
\|\Pi_Ty-\Pi_Tx\|\le\|T^Ny-\Pi_Tx\|
\le\|T^Ny-T^Nx\|+\|T^Nx-\Pi_Tx\|.
\]

这只是连续性，尚不是有指定指数的两点 Hölder。

一个排除“强 quasi-nonexpansive 自动 Lipschitz”的显式例：在 \([0,2]\) 上，取 \(a=1/2\)，令

\[
T(x)=x\ (x\le1),\qquad
T(1+s)=1-f(s),\qquad
f(s)=\tfrac12\min\{s,\sqrt{|s-a|}\},\quad0\le s\le1.
\]

则 \(T\) 连续、半代数、1/2-Hölder，\(\operatorname{Fix}T=[0,1]\)，一步后落入解集，所以 \(\Pi_T=T\)。对 \(z\in[0,1]\)，记 \(b=1-z\ge0\)，有

\[
|1+s-z|^2-|T(1+s)-z|^2
=(s+f)(2b+s-f)
\ge\tfrac13(s+f)^2
=\tfrac13|1+s-T(1+s)|^2.
\]

因此它是 \(1/3\)-strongly quasi-nonexpansive（也是连续 paracontraction），然而在 \(x=1+a\) 不 Lipschitz，因为极限差为 \(\tfrac12\sqrt{|h|}\)。若将根号替换为连续的 \(\ell(|s-a|)\)，其中 \(\ell(0)=0\)、\(\ell(t)=1/\log(e/t)\)，相同计算给连续 SQNE 而 \(\Pi_T\) 不属于任何正阶 Hölder；后者不半代数且单步也不 Hölder，不能用来冒充对用户“RLEB + all-pairs Hölder”联合条件的反例。

另一个特殊正面结论：若 \(S\) 是完整闭仿射子空间而不是仅一个局部片，则 Fejér 条件迫使每步保持正交切向投影 \(P_STx=P_Sx\)。证明把 \(s\) 沿 \(S\) 任意远移动，比较平方范数中的线性项。于是若收敛到 \(S\)，必有 \(\Pi_T=P_S\)，为 1-Lipschitz。这说明不能把“相对解集”条件笼统说成永远无用；解集几何至关重要。

## 3. 原始文献定理核查表

下列“已读”指本次打开原作者论文并核对应定理，不等于穷尽性优先权认证。只获元数据的列为未闭环，不用它支持精确断言。

| 文献 | 精确位置与假设 | 结论及与本任务的关系 | 核查状态 |
|---|---|---|---|
| Andrzej Wiśnicki, *Hölder continuous retractions and amenable semigroups of uniformly Lipschitzian mappings in Hilbert spaces*, TMNA 43 (2014), 89–96, [arXiv:1204.6464v2](https://arxiv.org/abs/1204.6464v2) | Lemma 1：完备有界度量空间、\(L\) 为 \(k\)-Lipschitz、所有初值统一 \(d(L^{n+1}x,L^nx)\le c\gamma^n\) | 强收敛的原 Picard 极限 Hölder；这是 §2.3 最直接先例。Theorem 2 的半群回缩则由 invariant mean 定义的 \(\bar T_\mu\) 迭代构造，不应偷换为原 \(T^n\) 极限。 | 原文 Lemma 1、Theorem 2 及证明已读。 |
| Ronald E. Bruck, Jr., *Nonexpansive projections on subsets of Banach spaces*, Pacific J. Math. 47 (1973), 341–355, [DOI 10.2140/pjm.1973.47.341](https://msp.org/pjm/1973/47-2/p04.xhtml)；[原文](https://msp.org/pjm/1973/47-2/pjm-v47-n2-p04-s.pdf) | Theorem 1：回缩的 ray/sunny 非扩张、firm、orthogonal 条件；光滑 Banach 空间下等价且唯一。Theorem 2：均匀光滑等条件下，非扩张 retract 可得到非扩张 ray projection。Corollary 1：严格凸且均匀光滑、非扩张 \(T\) 有固定点。 | 存在良好回缩/投影，不是原 Picard 极限稳定性定理。Hilbert 最近点投影是关键特例。 | 原文定义及 Theorems 1–2、Corollary 1 已读。 |
| Heinz H. Bauschke and Yuan Gao, *On a result by Baillon, Bruck, and Reich*, [arXiv:2404.04402](https://arxiv.org/abs/2404.04402) | Fact 1.1 引 Reich Theorem 2：Hilbert 空间、\(R\) 非扩张且有固定点、\(\sum_n\lambda_n(1-\lambda_n)=\infty\)。Theorem 1.3/2.5：再加 \(R\) 线性及 \(\epsilon\le\lambda_n\le1-\epsilon\)；Theorem 3.4 仿射版。 | 一般情形弱收敛；线性/仿射时强收敛到 \(P_{\operatorname{Fix}R}x_0\)。固定共同参数下由非扩张继承得 1-Lipschitz 选择。无限维的弱强差别不能省。 | 原文相应定理及证明已读；Reich 1979 原页未直接读到。 |
| Heinz H. Bauschke and Jonathan M. Borwein, *On Projection Algorithms for Solving Convex Feasibility Problems*, SIAM Rev. 38 (1996), 367–426, [DOI 10.1137/S0036144593251710](https://epubs.siam.org/doi/10.1137/S0036144593251710)；[作者原文](https://cmps-people.ok.ubc.ca/bauschke/Research/05.pdf) | Fact 1.3、Facts 1.5：firm 与 reflected nonexpansive 等价及凸集投影。Theorem 2.16：Hilbert 空间 Fejér 序列，刻画弱/强收敛及 \(\|x_n-x_\infty\|\le2d(x_n,C)\)。 | 固定轨道到解集/到极限的控制，不直接给两个初值的输出差。Remarks 2.2 特别说明该文 attracting 定义包含非扩张，而其他作者 paracontracting 定义可能不包含。 | 对应原页已读。 |
| Andrzej Cegielski, Simeon Reich, Rafał Zalas, *Regular Sequences of Quasi-Nonexpansive Operators and Their Applications*, [DOI 10.1137/17M1134986](https://epubs.siam.org/doi/10.1137/17M1134986)；[arXiv:1710.00534v2](https://arxiv.org/abs/1710.00534v2) | Theorem 6.1：Hilbert 空间，\(U_k\) 为 \(\rho_k\)-SQNE、\(\inf\rho_k>0\)，共同非空闭凸目标集；弱/有界/有界线性正则分别加强。 | 分别给弱/强/R-线性收敛；(64) 给 \(\|x_k-x_*\|\le2d(x_0,C)(1-\rho/\delta^2)^{k/2}\)。原定理未给 \(x_0\mapsto x_*\) 的 Hölder/Lipschitz 结论；还须跨轨道控制。 | 原文 Theorem 6.1 与证明已读。 |
| L. Elsner, I. Koltracht, M. Neumann, *Convergence of sequential and asynchronous nonlinear paracontractions*, Numer. Math. 62 (1992), 305–319, [DOI 10.1007/BF01396232](https://link.springer.com/article/10.1007/BF01396232) | 出版页确认有限维 nonlinear paracontractions 的序列/异步迭代收敛。 | 不能仅凭摘要宣称有初值 Hölder/Lipschitz；本轮未取得原始定理页。 | 元数据已核；定理号/完整假设未闭环。 |
| Yair Censor and Simeon Reich, *Iterations of paracontractions and firmly nonexpansive operators with applications to feasibility and optimization*, Optimization 37 (1996), 323–339, [DOI 10.1080/02331939608844225](https://www.tandfonline.com/doi/abs/10.1080/02331939608844225) | 原始正文未取得。 | 作为后续定向阅读线索，未用其标题冒充初值稳定性定理。 | 未闭环。 |
| Ronald E. Bruck and Simeon Reich, *Nonexpansive projections and resolvents of accretive operators in Banach spaces*, Houston J. Math. 3(4) (1977), 459–470, [作者机构记录](https://cris.technion.ac.il/en/publications/nonexpansive-projections-and-resolvents-of-accretive-operators-in/) | DOI/arXiv 本轮未确认，不能编造；原文未取得。 | 与强非扩张/预解算子背景相关，但没有本轮第一手定理级证据。 | 元数据已核；正文未闭环。 |

补注：Baillon–Bruck–Reich 1978 原始题名为 *On the asymptotic behavior of nonexpansive mappings and semigroups in Banach spaces*, Houston J. Math. 4 (1978), 1–9。本轮通过 Bauschke–Gao 论文核到经典来源；不假装已读 1978 原页。Reich 的 *Weak convergence theorems for nonexpansive mappings in Banach spaces* 正确刊期为 JMAA 67 (1979), 274–276，DOI 从出版 PII 对应为 10.1016/0022-247X(79)90024-6；本轮只按书目线索保留，定理 2 由后文明确转引，不作为已经第一手闭环。

## 4. 怎么与 RLEB 拼接，哪些方向有研究价值

### 4.1 最自然、最便宜的基准：共同域局部 Lipschitz 单步

不要直接把全空间单调性加回去。只要在同一个共同轨道区域验证 \(J_\mathcal G=T\) 的 all-pairs 有限 Lipschitz 常数，并从原 RLEB 局部预算取得同一初值邻域上的几何点尾界，§2.3 就给正阶 Hölder。这是立即可用的正面结论，但抽象方法已知。

接口必须保留上轮修订：局部图预解算子 \(J_\mathcal G\) 不是自动等于完整 \(J_{\lambda F}\)；只有完整纤维一致/覆盖得到核验，才把它称为原完整 proximal 算法。

### 4.2 单调算子的直接拼接是经典，强单调并非必要

若共同输出图块具有 all-pairs 单调性，\(u=Tx\)、\(v=Ty\)、\((x-u)/\lambda\in F(u)\)、\((y-v)/\lambda\in F(v)\)，则

\[
\langle u-v,(x-u)-(y-v)\rangle\ge0
\implies \|u-v\|^2\le\langle u-v,x-y\rangle.
\]

这直接给 local firmly nonexpansive，从而极限 1-Lipschitz。它保留多解，但条件可能排除 RLEB 想涵盖的非单调/非 Lipschitz 特色。因此适合作“经典恢复基准”，不适合作新论文唯一成果。

### 4.3 更适合保留 RLEB 广度：分方向的可求和增益

上传稿 §5.2 已写出

\[
T(a,r)=(a+B(a,r),qr),\quad
\|B(a,r)-B(b,r)\|\le Cr^\eta\|a-b\|,
\quad
\|B(a,r)-B(a,s)\|\le H|r-s|^\gamma.
\]

其结论是切向初值 Lipschitz、法向初值 \(\gamma\)-Hölder，且法向部分允许真正非 Lipschitz。思想与 §2.4 的乘积有限一致。这一版本严格比“所有方向单步 Lipschitz”更适合用户的奇异模型，但只覆盖三角结构。能否从可检查的图几何/弱单调性推出这些各向异性估计，或放宽独立法向 \(qr\) 为耦合动力学，是需要真正新工作的地方。

## 5. 本组建议给用户的一句话

“是的，已有理论早就知道：多解不妨碍稳定选择；非扩张给 Lipschitz，单步 Lipschitz 加统一快收敛给 Hölder。你值得继续研究的不是把这些旧条件改叫 RLEB 条件，而是保留 RLEB 允许的非 Lipschitz、非单调法向结构，只补最少的切向跨轨道控制，并证明条件可由算子图验证。”

这不是宣告“最弱条件已经找到”，也不是宣告“加准非扩张就一定足够得到 Hölder”。
