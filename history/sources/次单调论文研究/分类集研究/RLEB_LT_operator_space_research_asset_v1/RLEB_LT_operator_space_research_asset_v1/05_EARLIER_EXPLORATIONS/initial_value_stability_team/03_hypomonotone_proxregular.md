# 第 3 组：次单调、prox-regular 与初值极限选择

核查日期：2026-09-19。对象：`solution_selection_revised_v1/research_note.md` 全稿；不重新审计原 RLEB 收敛定理。

## 0. 先给结论

**有成熟的相邻研究，而且已有条件能够确实保证多解情形的初值极限稳定；不是只能证明唯一解的参数稳定。** 但要分三层：

1. 普通 hypomonotonicity 加合适小步长使一步 resolvent Lipschitz；再接入本稿已经建立的“共同初值邻域上的统一几何点尾界”，就得到极限选择的正 Hölder 阶。这个传递机制已有先例，不宜作为新的主定理包装。
2. cohypomonotonicity 加足够大步长、局部变分凸性等可以直接给非扩张/firmly nonexpansive 的迭代。若共同邻域内迭代收敛，则极限选择非扩张。这保留多解，不需要把解压成唯一点。
3. prox-regularity、单步单值 Lipschitz、强度量正则等，分别控制不同对象；不能不加说明地当成多解极限选择稳定的结论。

真正贴近当前 RLEB 新稿的研究机会是：**允许法向仍然只有 Hölder 正则，只限制切向的累计放大及法切耦合**。本稿 §5.2 的三角情形已体现这一机制；若能处理更一般图块、给出易检验的算子条件、并且严格弱于已有非扩张/全空间 Lipschitz 条件，才可能有实质增量。本组尚未证明这种一般化，也不作“首创”判断。

## 1. 本次必须固定的对象

记迭代为

\[
x_{k+1}=T x_k,\qquad \Pi_T(x)=\lim_{k\to\infty}T^k x.
\]

研究的是同一算法、同一图块/分支规则、不同初值的两点估计

\[
\|\Pi_T(x)-\Pi_T(y)\|\le \omega(\|x-y\|).
\]

它不是以下三个问题：一步 \(T\) 的正则性；右端参数扰动后的零点映射 \(F^{-1}(v)\)；唯一局部解附近算法是否收敛。

本稿已有的可调用接口是：共同初值集合 \(U\)，共同轨道区域 \(W\)，迭代在 \(W\) 内，以及

\[
\sup_{x\in U}\|T^k x-\Pi_Tx\|\le M\sigma^k,
\qquad 0<\sigma<1. \tag{1.1}
\]

这里 \(\sigma\) 是**点尾界因子**，不是自动等于到解集的实际收缩因子。按本稿的通常传递，若距离因子为 \(q\)、单步只有 \(\gamma\)-Hölder，则使用的尾界因子可为 \(\sigma=q^\gamma\)。保守证书也不能不加区别地代入实际因子。

下面涉及局部 resolvent 的结论均需保证：(a) 定义在共同输入邻域；(b) 两条轨道调用的图点均在同一受控图域内；(c) 若声称是**完整** \(J_{\lambda F}\)，需另外排除图域外的其他 proximal 解。对局部截断图的结论不能直接升级成完整算子结论。

## 2. 三种“次单调”不能混称

设 \((u,a),(v,b)\in\operatorname{gph}F\)，本报告取 \(\rho\ge0\)。

| 条件 | 定量不等式 | 对 resolvent 的作用 |
|---|---|---|
| 普通 \(\rho\)-hypomonotonicity | \(\langle u-v,a-b\rangle\ge-\rho\|u-v\|^2\) | \(\lambda\rho<1\) 时一步 Lipschitz，常数通常大于 1 |
| \(\rho\)-cohypomonotonicity | \(\langle u-v,a-b\rangle\ge-\rho\|a-b\|^2\) | \(\lambda\ge2\rho\) 时一步非扩张；严格大于时可得 averaged |
| Daniilidis–Georgiev 意义 submonotonicity | 对任意 \(\varepsilon>0\)，充分小邻域内 \(\langle u-v,a-b\rangle\ge-\varepsilon\|u-v\|\) | 右端是一阶距离；不能直接推出固定 Lipschitz 常数 |

第三行的定义与等价性见 Daniilidis–Georgiev (2004) 式 (1)、Theorem 2、Corollary 3；该文研究近似凸性/下 \(C^1\) 与 subdifferential 的关系，**不是** \(\Pi_T\) 定理。[原论文](https://www.arisdaniilidis.at/DG_ac.pdf)

注意 BMW 的 \(\rho\)-comonotone 允许 \(\rho<0\)，与本报告第二行关系为其参数 \(-\rho\)。术语“weak monotonicity”也必须以实际不等式为准。

## 3. 可以立刻接上 RLEB 的正面接口：普通 hypomonotonicity

### 3.1 独立推导一步常数

取

\[
x=u+\lambda a,\quad y=v+\lambda b,
\quad a\in F(u),\ b\in F(v).
\]

若共同图域内满足普通 hypomonotonicity，则

\[
\langle x-y,u-v\rangle
=\|u-v\|^2+\lambda\langle a-b,u-v\rangle
\ge(1-\lambda\rho)\|u-v\|^2.
\]

因此在 \(\lambda\rho<1\) 时，同一受控局部逆具有

\[
\|Tx-Ty\|\le L\|x-y\|,
\qquad L=\frac1{1-\lambda\rho}. \tag{3.1}
\]

这个推导同时给“至多一个局部解”；它不替代存在性/满射性/完整解覆盖的证明。

全域情形若 \(M=F+\rho I\) maximal monotone，则

\[
J_{\lambda F}
=J_{\frac{\lambda}{1-\lambda\rho}M}
 \circ\frac1{1-\lambda\rho}I,
\]

因此存在性与完整逆的 Lipschitz 常数也一并得到。对于弱凸函数 subdifferential，BMW **Proposition 6.3(iv)** 明确给出此阈值和常数：其记号为 \(f\) 是 \(1/\ell\)-hypoconvex、\(0<\mu<\ell\)，则完整 \(\operatorname{Prox}_{\mu f}=J_{\mu\partial^{\#}f}\) 为 \(\ell/(\ell-\mu)\)-Lipschitz；换元 \(\rho=1/\ell\)、\(\lambda=\mu\) 即 (3.1)。该节假设 \(f\) proper lsc 且有二次下界，并规定了 \(\partial^{\#}\) 的性质。[精确原始定理](https://arxiv.org/pdf/1902.09827)

### 3.2 一步 Lipschitz 加统一尾界给两点 Hölder

由 (1.1)、(3.1)，对于同处共同吸引域的初值，

\[
\|\Pi_Tx-\Pi_Ty\|
\le L^n\delta+2M\sigma^n,
\qquad \delta=\|x-y\|. \tag{3.2}
\]

若 \(L>1\)，令

\[
\theta=\frac{\log(1/\sigma)}{\log L+\log(1/\sigma)}\in(0,1),
\quad
n=\left\lfloor\frac{\log(1/\delta)}{\log L+\log(1/\sigma)}\right\rfloor
\]

即可在 \(0<\delta<1\) 的归一化局部尺度上得到

\[
\boxed{\quad
\|\Pi_Tx-\Pi_Ty\|
\le (1+2M/\sigma)\,\delta^\theta.
\quad} \tag{3.3}
\]

如果 (3.1) 仅对距离小于固定尺度 \(\eta\) 的图点有效，也可关闭归纳：所有 \(j\le n\) 满足 \(L^j\delta\le L^n\delta\le\delta^\theta<\eta\)。仍需轨道本身留在共同图域。

若 \(L\le1\)，则直接对每个 \(n\) 使用 \(\|T^nx-T^ny\|\le\|x-y\|\)，取极限得到 \(\Pi_T\) 非扩张；若 \(L<1\)，共同域内收敛极限实际上必须相同。

**优先权定位：** Wiśnicki (2014), Lemma 1 已有“Lipschitz 迭代 + 统一几何增量尾界 \(\Rightarrow\) Hölder 极限回缩”的机制。其表述使用完备有界度量空间及 \(d(T^{n+1}x,T^nx)\le c\gamma^n\)；当前 (1.1) 直接给尾界，(3.2) 是同一有限前缀/无限尾部平衡。因此这里是可用的现成接口，不是 RLEB 独有的新发现。[原论文预印本](https://arxiv.org/pdf/1204.6464v2)

**实施限制：** 必须在同一 \(\lambda\) 上同时验证 RLEB 严格兼容和 \(\lambda\rho<1\)。不能为了 (3.1) 改小步长，然后不复核原兼容条件/图块覆盖就继续调用旧尾界。

### 3.3 这不是保持当前奇异图特征的“最弱”条件

对新稿 (2.1) 原构造取

\[
u_t=(t,0,t),\quad v=(0,0,0),\quad
a_t=(-2\sqrt t,0,3t)\in F(u_t),\quad b=0\in F(v).
\]

则

\[
\frac{\langle u_t-v,a_t-b\rangle}{\|u_t-v\|^2}
=\frac{-2t\sqrt t+3t^2}{2t^2}
=\frac32-\frac1{\sqrt t}\longrightarrow-\infty.
\]

故该图在原点附近不满足任何有限常数的普通 hypomonotonicity。加上此条件会排除这个反例，也会排除它的某些正常 Hölder 奇异性；它是稳妥基线，不一定是最有研究价值的最终条件。

## 4. 多解而且 Lipschitz：cohypomonotonicity 是直接的旧路线

由第二种不等式独立计算，

\[
\begin{aligned}
\|x-y\|^2
&=\|u-v\|^2+2\lambda\langle u-v,a-b\rangle
  +\lambda^2\|a-b\|^2\\
&\ge\|u-v\|^2+\lambda(\lambda-2\rho)\|a-b\|^2.
\end{aligned} \tag{4.1}
\]

所以 \(\lambda\ge2\rho\) 给 \(T\) 非扩张；有共同轨道收敛便给

\[
\|\Pi_Tx-\Pi_Ty\|\le\|x-y\|. \tag{4.2}
\]

若 \(\lambda>2\rho\)，(4.1) 还给 averaged 参数

\[
\alpha=\frac{\lambda}{2(\lambda-\rho)}\in[1/2,1).
\]

存在性和全域结论需要适当 maximality；局部版本要保留局部图/轨道限制。

**准确已有结果。** Bauschke–Moursi–Wang 的 Proposition 3.13(iii),(v) 及 Corollary 3.14（所读 arXiv 版本编号）给 comonotonicity 与 resolvent 非扩张/averaged 的对应。[原论文](https://arxiv.org/pdf/1902.09827)

Combettes–Pennanen (2004), Lemma 2.4 给局部 cohypomonotone resolvent 与单调 resolvent 的松弛恒等式；Theorem 3.1 证明局部 inexact relaxed PPA 的可行性与弱收敛。该定理要求局部 maximal cohypomonotonicity、闭零集与统一邻域余量、步长余量、松弛比例及误差预算。单算子、固定步长、精确不松弛的情形可取 \(\lambda>2\rho\)。在有限维弱收敛即强收敛；加 (4.1) 立即得到多初值 Lipschitz 极限选择。[原论文](https://pcombet.math.ncsu.edu/sicon3.pdf)

这是**已有定理加一行推论**，不应虚称两篇原文另有命名的“极限选择 Lipschitz 定理”。边界 \(\lambda=2\rho\) 只有非扩张，单独不保证 Picard 收敛；如果收敛由 RLEB 独立提供，则仍够用。

另外，这一路可能过强：全域 maximal cohypomonotone 的适当参数下，零集是凸的（BMW Corollary 3.15），它不能原样囊括一般弯曲解流形。

## 5. prox-regularity 能给什么，不能给什么

### 5.1 非凸函数：局部 prox 单步 Lipschitz，不等于极限稳定

Poliquin–Rockafellar (1996), Theorem 3.2 把 prox-regularity 与 **f-attentive 截断** subdifferential 加二次项后的单调性联系起来；Theorem 4.4 在其附加下界 (4.1) 与 \(0<\lambda<1/r\) 下给局部单值 Lipschitz prox，并与这个截断 subdifferential 的 resolvent 对应。[原论文](https://sites.math.washington.edu/~rtr/papers/rtr157-ProxRegular.pdf)

因此可通过 §3 和统一点尾界推出 Hölder \(\Pi_T\)。但不能跳过 attentive localization、步长、共同轨道，也不能自动把局部 prox 认作整个非凸 subdifferential inclusion 的全部解。

### 5.2 独立最小反例：甚至光滑、全局弱凸、全局 Lipschitz prox 都不够

令

\[
f(u)=\frac14(u^2-1)^2,
\quad f''(u)=3u^2-1\ge-1,
\quad0<\lambda<1.
\]

函数为光滑、半代数、弱凸且 prox-regular。每个输入的 proximal objective 严格凸，故完整 prox 单值，满足

\[
x=h(u):=(1-\lambda)u+\lambda u^3,
\qquad T=h^{-1},\qquad
\operatorname{Lip}T\le\frac1{1-\lambda}.
\]

固定点为 \(-1,0,1\)。由于 \(h\) 严格递增且在 \((0,1)\) 上 \(h(u)<u\)，在 \((1,\infty)\) 上 \(h(u)>u\)，直接得

\[
\Pi_T(x)=
\begin{cases}
1,&x>0,\\
0,&x=0,\\
-1,&x<0.
\end{cases}
\]

所以极限选择在 0 不连续。不是数值试验，也不是因为 prox 分支没选好。

该例**不反驳** §3，因为它缺共同初值邻域上的统一尾界：取 \(x_n=h^n(1/2)\downarrow0\)，则 \(T^nx_n=1/2\)，而 \(\Pi_Tx_n=1\)，于是任意充分小共同初值邻域内，尾误差的上确界始终至少为 \(1/2\)。也不能把它当成满足当前严格 RLEB 接口的反例。

### 5.3 局部变分凸性：不要求全局凸，但能给强的正面结论

Rockafellar (2019), Theorem 1 证明 variational convexity 与 f-local monotonicity/maximal monotonicity 的对应；Theorem 2 是强版本。这里仍是 attentive 局部图，不是任意全图。[原论文](https://sites.math.washington.edu/~rtr/papers/rtr251-LocalMono.pdf)

Rockafellar (2021), Theorem 2 证明局部变分凸性给适当球上的 localized prox firmly nonexpansive；Theorem 3 在 prox-regularity 下给相应必要充分性。[原论文](https://sites.math.washington.edu/~rtr/papers/rtr254-ProxMaps.pdf)

若这个局部 prox 正是研究算法，且有共同轨道与收敛，则 \(\Pi_T\) 非扩张。这是**有局部结构意义、允许多解的既有充分路线**。对当前一般非势算子不能直接使用“变分凸性”；需要相应图局部单调条件。

### 5.4 prox-regular 集的投影是漂亮例子，但要防完整 resolvent 陷阱

Poliquin–Rockafellar–Thibault (2000), Theorem 1.3：闭集在参考点 prox-regular 时，邻域上的最近点投影 \(P_C\) 单值 Lipschitz，并与**截断正常锥** \(N_C^r=N_C\cap\operatorname{int}B(0,r)\) 的 resolvent 相同。Theorem 4.1 和 Lemma 4.2(i) 给一致管状邻域版本及 \(r/(r-\rho)\) 型 Lipschitz 常数。[原论文](https://sites.math.washington.edu/~rtr/papers/rtr170-LocalDiffDistance.pdf)

因为 \(P_C^2=P_C\)，算法一步后停在解集，所以 \(\Pi_{P_C}=P_C\) 是 Lipschitz 的；解集不需单点，甚至不需凸。这是几何机制已被研究的明确证据，但不是一般 PPA 极限选择理论。

**完整正常锥 inclusion 反例：** 令 \(C\) 为单位圆，\(c\in C\)，\(x=tc\)，\(t>0\) 且接近 1。正常锥 \(N_C(u)=\mathbb Ru\)。于是 \(u=c\) 和 \(u=-c\) 都满足 \(x-u\in N_C(u)\)，而最近点投影只有 \(P_Cx=c\)。因此

\[
P_C\ne(I+N_C)^{-1}
\]

即使输入就在集合附近也不能省去“截断/局部输出”条件。对本稿强调完整 proximal 解的任务，这一差别是实质性的。

## 6. “正则性”附加条件的对象检查

| 候选条件 | 单独是否控制多解初值极限选择 | 当前 RLEB 下的用途 |
|---|---|---|
| 局部 resolvent 单值 | 否 | 原稿坏例已经单值；还需定量跨初值估计 |
| resolvent 局部 Lipschitz | 否，见双井例 | 与共同统一几何尾界合用，得 §3 的 Hölder |
| resolvent 局部非扩张/averaged | 有共同轨道收敛时，是 | 极限选择非扩张；不需要速率用于最后取极限 |
| 普通 hypomonotonicity | 只给适当步长的一步界 | 同时满足原兼容条件后，接 §3 |
| cohypomonotonicity | 配合步长/存在性/共同域后，是 | §4，属于成熟非扩张路线 |
| prox-regularity | 否 | attentive 图上的一步 Lipschitz；需共同尾界 |
| f 的局部变分凸性 | 配合局部 prox 与收敛，是 | 非扩张极限；一般非势 F 未必可用 |
| F 在 \((s,0)\) 强度量次正则 | 局部零点孤立 | 若共同邻域收敛到 s，\(\Pi_T\equiv s\)；回避多解选择难点 |
| F 在 \((s,0)\) 强度量正则 | 局部参数解单值 Lipschitz | 仍主要是孤立解/参数稳定，不是所问多解机制 |
| \(I+\lambda F\) 的强度量正则 | 局部逆，即一步 resolvent Lipschitz | 不必令 F 的零集孤立；可与统一尾界合用 |
| 普通 metric subregularity/残差 EB | 否 | 控制到解集的距离，当前坏例说明其不自动控制选中谁 |

这里“强度量次正则导致孤立零点”直接来自其定义：

\[
\|u-s\|\le\kappa\operatorname{dist}(0,F(u))
\]

在邻域内对任何零点 \(u\) 迫使 \(u=s\)。不需要借用一个不可核查的文献定理。

## 7. 完整文献信息与核查级别

下列“已读”指已打开原始论文/作者全文，并逐条阅读这里调用的定理与相关证明；不等于该文每页都用于本任务。编号以链接版本为准。

| 文献 | DOI/arXiv | 精确入口及核查结论 |
|---|---|---|
| Hans H. Bauschke, Walaa M. Moursi, Xianfu Wang, **Generalized monotone operators and their averaged resolvents**, Mathematical Programming 189 (2021), 55–74 | [10.1007/s10107-020-01500-6](https://doi.org/10.1007/s10107-020-01500-6); [arXiv:1902.09827](https://arxiv.org/abs/1902.09827) | 已读 Definition 2.3, Proposition 3.13, Corollaries 3.14–3.15，另读 Proposition 6.3 及其证明；分别给 cohypo 的 averaged 对应、弱凸 prox 的小步长 Lipschitz，不另声称原文有 \(\Pi_T\) 定理 |
| Patrick L. Combettes, Teemu Pennanen, **Proximal Methods for Cohypomonotone Operators**, SIAM Journal on Control and Optimization 43(2) (2004), 731–742 | [10.1137/S0363012903427336](https://doi.org/10.1137/S0363012903427336) | 已读 Definitions 2.1–2.2, Lemmas 2.3–2.4, Theorem 3.1 及证明；直接研究该类 PPA，多初值非扩张极限为所述精确特例的即时推论 |
| R. A. Poliquin, R. T. Rockafellar, **Prox-Regular Functions in Variational Analysis**, Transactions AMS 348(5) (1996), 1805–1838 | [10.1090/S0002-9947-96-01544-9](https://doi.org/10.1090/S0002-9947-96-01544-9) | 已读作者全文 Theorems 3.2, 4.4；局部 attentive prox 单值 Lipschitz，不是 \(\Pi_T\) |
| R. A. Poliquin, R. T. Rockafellar, L. Thibault, **Local differentiability of distance functions**, Transactions AMS 352(11) (2000), 5231–5249 | [10.1090/S0002-9947-00-02550-2](https://doi.org/10.1090/S0002-9947-00-02550-2) | 已读原期刊 PDF Theorems 1.3, 4.1, Lemma 4.2；局部 Lipschitz 投影及截断正常锥 |
| R. Tyrrell Rockafellar, **Variational Convexity and the Local Monotonicity of Subgradient Mappings**, Vietnam Journal of Mathematics 47 (2019), 547–561 | [10.1007/s10013-019-00339-5](https://doi.org/10.1007/s10013-019-00339-5) | 已读 Theorems 1–4 的相关范围；本任务使用 1–2，tilt stability 不混作初值稳定 |
| R. Tyrrell Rockafellar, **Characterizing firm nonexpansiveness of prox mappings both locally and globally**, Journal of Nonlinear and Convex Analysis 22(5) (2021), 887–899 | [期刊页面](https://yokohamapublishers.jp/online2/opjnca/vol22/p887.html)；未定位 DOI/arXiv | 已读 Theorems 2–3；局部 prox firm nonexpansive 的准确结构条件 |
| Andrzej Wiśnicki, **Hölder continuous retractions and amenable semigroups of uniformly Lipschitzian mappings in Hilbert spaces**, Topological Methods in Nonlinear Analysis 43 (2014), 89–96 | [10.12775/TMNA.2014.006](https://doi.org/10.12775/TMNA.2014.006); [arXiv:1204.6464](https://arxiv.org/abs/1204.6464) | 已读 Lemma 1 证明；Lipschitz 迭代与统一几何尾部导出 Hölder 极限。不要把后面的特殊平均构造误当任意原算法 |
| Aris Daniilidis, Pando Georgiev, **Approximate convexity and submonotonicity**, Journal of Mathematical Analysis and Applications 291 (2004), 292–301 | [10.1016/j.jmaa.2003.11.004](https://doi.org/10.1016/j.jmaa.2003.11.004) | 已读式 (1), Theorem 2, Corollary 3；用于辨明 submonotone 的实际含义 |

### 尚不能关闭的优先权入口

1. J. E. Spingarn, **Submonotone mappings and the proximal point algorithm**, Numerical Functional Analysis and Optimization 4(2), 123–150 (1982), [DOI 10.1080/01630568208816109](https://doi.org/10.1080/01630568208816109)。已核对题录及摘要，全文入口被阻断。摘要明确涉及以 maximal strict submonotonicity 代替 maximal monotonicity 的 PPA，故它是高度相关的早期入口；**本轮不能给未经阅读的定理号，也不能断言其已经/没有研究两初值极限映射**。
2. Teemu Pennanen, **Local convergence of the proximal point algorithm and multiplier methods without monotonicity**, Mathematics of Operations Research 27(1) (2002), 170–191, [DOI 10.1287/moor.27.1.170.331](https://doi.org/10.1287/moor.27.1.170.331)。其核心路线已由可读的 Combettes–Pennanen 后续原论文交叉确认，但本轮未取得其全文，不能把引用转述升级为独立逐定理核验。
3. Poliquin–Rockafellar 作者预印本 Theorem 4.4 的排版/常数表达存在需与期刊版核对之处。本报告只采用该文已核实的定性单步 Lipschitz 结论；具体 \((1-\lambda\rho)^{-1}\) 常数由 §3.1 独立推导，不抄录有疑义的排版。

因此，**可以确定正面研究并非空白；不能宣称本轮已穷尽 submonotone 文献，更不能以检索不到作为首创证明。**

## 8. 给总协调者的建议

可以直白告诉用户：“你的方向是对的。负面例子不是说 RLEB 每个算子都不稳定，而是原条件没有统一保证。以前人的经验能先给两套有效药方：让一步映射 Lipschitz，可把现有几何尾界升级为正 Hölder 初值稳定；让它非扩张，则直接得到 Lipschitz 极限选择。但第一套可能删掉 RLEB 最有特色的正常 Hölder 奇异性，第二套更强。因此有价值的后续不是把已有药方换个名字，而是找只管切向累计放大、保留法向奇异性的条件。”

建议下一轮审稿/研究只追三个可证伪指标：

1. 新条件是否由原始算子/图块可检验，而非直接假设 \(\Pi_T\) 正则或把所求性质写进假设？
2. 是否严格涵盖某个不是全空间 Lipschitz、也不是非扩张的完整 resolvent 例子？
3. 是否在共同吸引域上得到两点 Hölder/Lipschitz，而非仅固定解点的 calmness，且真正超过本稿 §5.2 三角离散 Gronwall 结论？

本组没有把这些待证目标冒充已完成定理。
