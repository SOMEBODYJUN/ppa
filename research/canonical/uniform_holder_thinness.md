# 精确固定集连续自映射层中的 Hölder 薄性

本页从明定对象独立重建历史障碍审计 §7.1 的一个受限结论：一致拓扑下，固定正 Hölder 指数与常数的块闭且无处稠密。局部扰动仅保持值域、精确固定集及一致距离；收敛、全时间距离和共同尾预算不在其保持结论内。

<a id="uht-object"></a>
## C180-v1 / UNIFORM-HOLDER-THINNESS：对象与量词

令 \(E\) 是有限维实赋范空间，\(K\subset E\) 是非空紧凸集，且 \(\operatorname{int}_E K\ne\varnothing\)。固定非空闭真子集 \(S\subsetneq K\)，假定
\[
\operatorname{int}_E(K\setminus S)\ne\varnothing,
\qquad
\mathfrak X=\{T\in C(K,K):\operatorname{Fix}T=S\}\ne\varnothing.
\tag{UH1}
\]
这里 \(\operatorname{Fix}T=\{x\in K:T(x)=x\}\)，两处内点均为环境空间内点。\(C(K,K)\) 表示全部连续自映射，\(\mathfrak X\) 配一致距离
\[
d_\infty(T,U)=\sup_{x\in K}\|T(x)-U(x)\|.
\]
不另加轨道或证书要求。非空 \(S\) 不额外排除所请求的对象：在有限维非空紧凸 \(K\) 上，Brouwer 固定点定理保证每个连续自映射都有固定点，因此 \(\mathfrak X\ne\varnothing\) 已迫使 \(S\ne\varnothing\)；真子集条件也由 (UH1) 推出。此处把这两项明写，避免后文距离与固定目标量词有空集歧义。若 \(\dim E=0\)，则 \(K\) 是单点，\(\mathfrak X\ne\varnothing\) 强制 \(S=K\)，与 (UH1) 矛盾。因此这些假设下 \(\dim E\ge1\)，且 \(D=\operatorname{diam}K>0\)。

对每个固定 \(\alpha>0\) 与 \(0\le M<\infty\)，定义
\[
\mathcal H_{\alpha,M}
=\{T\in\mathfrak X:
\|T(x)-T(y)\|\le M\|x-y\|^\alpha
\text{ 对全部 }x,y\in K\}.
\tag{UH2}
\]
**结论。** 每个 \(\mathcal H_{\alpha,M}\) 在 \(\mathfrak X\) 中闭且无处稠密；具有某个正 Hölder 指数及有限全域常数的全部映射之并类
\[
\mathcal H_+
=\bigcup_{\alpha>0,\ 0\le M<\infty}\mathcal H_{\alpha,M}
\tag{UH3}
\]
在 \(\mathfrak X\) 中第一纲。该非空母空间是 Baire 空间，\(\mathfrak X\setminus\mathcal H_+\) 是稠密的 \(G_\delta\)。闭性、内部、闭包与第一纲均相对于这一精确固定集空间，不相对于整个 \(C(K,K)\)。本结论也允许 \(\alpha>1\)；构造选用的尖点指数会小于 1。

<a id="uht-baire"></a>
## 精确固定集母空间的 Baire 门

\(C(K,K)\) 的一致距离完备：一致 Cauchy 列逐点在闭的 \(K\) 中有极限，并一致收敛到连续的 \(K\)-值映射。其子空间
\[
Z=\{T\in C(K,K):T(s)=s\text{ 对全部 }s\in S\}
\]
闭，因而也完备。令 \(K_j=\{x\in K:d(x,S)\ge1/j\}\)，忽略空的 \(K_j\)。这些集紧，且并集等于 \(K\setminus S\)。对非空 \(K_j\) 定义
\[
m_j(T)=\min_{x\in K_j}\|T(x)-x\|.
\]
反三角不等式给 \(|m_j(T)-m_j(U)|\le d_\infty(T,U)\)。因此
\[
\mathfrak X=\bigcap_{j:K_j\ne\varnothing}\{T\in Z:m_j(T)>0\}
\tag{UH-B}
\]
是完备空间 \(Z\) 的 \(G_\delta\) 子空间。

为不把完全可度量性暗作假设，可在 \(\mathfrak X\) 上直接使用兼容距离
\[
\widehat d(T,U)=d_\infty(T,U)
+\sum_{j:K_j\ne\varnothing}2^{-j}
\min\{1,|m_j(T)^{-1}-m_j(U)^{-1}|\}.
\]
有限前段中的倒数函数连续、级数尾一致小，故它与相对一致拓扑相同。若 \((T_n)\) 是 \(\widehat d\)-Cauchy 列，它在 \(Z\) 中有一致极限 \(T\)。对每个 \(j\)，实数列 \(m_j(T_n)^{-1}\) 为 Cauchy 列，因而有有限极限；由 \(m_j(T_n)\to m_j(T)\)，不能有 \(m_j(T)=0\)。故 \(T\in\mathfrak X\)，再用有限前段和级数尾得 \(\widehat d(T_n,T)\to0\)。所以 \(\widehat d\) 完备。

应用 Baire 完备度量空间定理，\(\mathfrak X\) 为 Baire 空间。该标准基础接口可直接由嵌套闭球证明：在任意非空开集及给定的可数个稠密开集中，依次选半径趋零的非空闭球，每个球包含于前球内部与下一个稠密开集的交；球心为 Cauchy 列，完备性给交点，位于最初开集和全部给定稠密开集中。本页的非空假设确保这一结论有内容，没有给任何动力子层的 Baire 性作推断。

本例的非空门也可以直接验收，不需要 \(S\) 是回缩像。任取 \(s_0\in S\)，令 \(\eta(x)=\min\{1,d(x,S)\}\)，则
\[
T_*(x)=(1-\eta(x))x+\eta(x)s_0
\]
由凸性是连续 \(K\)-值映射。在 \(S\) 上 \(\eta=0\)，而在 \(K\setminus S\) 上 \(\eta>0\) 且 \(x\ne s_0\)，故 \(T_*(x)-x=\eta(x)(s_0-x)\ne0\)。所以 \(T_*\in\mathfrak X\)。它只验收空间非空，不提供共同尾或回缩性质。

<a id="uht-closed"></a>
## 固定预算的闭性

设 \(T_j\in\mathcal H_{\alpha,M}\) 且 \(T_j\to T\) 在 \(\mathfrak X\) 的一致距离下成立。对任意固定 \(x,y\in K\)，由范数连续性得
\[
\|T(x)-T(y)\|
=\lim_{j\to\infty}\|T_j(x)-T_j(y)\|
\le M\|x-y\|^\alpha.
\]
故 \(T\in\mathcal H_{\alpha,M}\)。这只证明相对闭性，未声称 \(\mathfrak X\) 在 \(C(K,K)\) 中闭。

<a id="uht-cusp"></a>
## 保持值域与精确固定集的尖点构造

固定 \(T\in\mathcal H_{\alpha,M}\) 及任意 \(\varepsilon>0\)。我们构造 \(U\in\mathfrak X\)，满足 \(d_\infty(U,T)<\varepsilon\)，并且 \(U\) 不具有任何有限 \(\alpha\)-Hölder 常数。

由 (UH1)，可取 \(a\in E\)、\(r>0\)，使闭球
\[
B=\overline B(a,3r)\subset\operatorname{int}_E(K\setminus S).
\]
球 \(B\) 紧且没有 \(T\) 的固定点，所以连续函数 \(x\mapsto\|T(x)-x\|\) 有严格正的最小值
\[
\delta=\min_{x\in B}\|T(x)-x\|>0.
\tag{UH4}
\]
再取 \(q\in\operatorname{int}_E K\) 与 \(\rho>0\)，使 \(\overline B(q,\rho)\subset K\)。定义两个连续、Lipschitz 的径向 cutoff：
\[
\theta(x)=
\begin{cases}
1,&\|x-a\|\le2r,\\
(3r-\|x-a\|)/r,&2r<\|x-a\|<3r,\\
0,&\|x-a\|\ge3r,
\end{cases}
\qquad
\chi(x)=
\begin{cases}
1,&\|x-a\|\le r,\\
(2r-\|x-a\|)/r,&r<\|x-a\|<2r,\\
0,&\|x-a\|\ge2r.
\end{cases}
\tag{UH5}
\]
取 \(0<\mu<1\) 充分小，使
\[
\mu D<\min\{\varepsilon/2,\delta/4\},
\qquad
G(x)=(1-\mu\theta(x))T(x)+\mu\theta(x)q.
\tag{UH6}
\]
凸性保证 \(G(K)\subset K\)，且 \(\|G-T\|_\infty\le\mu D\)。在 \(\|x-a\|\le2r\) 时 \(\theta(x)=1\)，因此对每个 \(\|v\|\le\mu\rho\)，
\[
G(x)+v=(1-\mu)T(x)+\mu(q+v/\mu)\in K.
\tag{UH7}
\]
这是逐个输出都具有的统一值域余量，不能由“扰动很小”单独替代。

取单位向量 \(e\in E\)，指数 \(0<\beta<\min\{\alpha,1\}\)，以及 \(c>0\) 充分小，使
\[
c(2r)^\beta<\min\{\varepsilon/2,\delta/4,\mu\rho/2\}.
\]
令
\[
U(x)=G(x)+c\chi(x)\|x-a\|^\beta e.
\tag{UH8}
\]
三个保持量逐项成立。

1. **连续性与值域。** 所有项连续。尖点项仅在 \(\|x-a\|<2r\) 时非零，其范数小于 \(\mu\rho\)，由 (UH7) 得 \(U(x)\in K\)；其余点 \(U(x)=G(x)\in K\)。
2. **任意小一致距离。** 由 (UH6) 与尖点振幅的选择，
   \[
   d_\infty(U,T)\le\mu D+c(2r)^\beta
   <\min\{\varepsilon,\delta/2\}.
   \tag{UH9}
   \]
3. **精确固定集。** 在 \(K\setminus B\) 上两 cutoff 均为零，故 \(U=T\)；特别地 \(U|_S=I\)。在 \(B\) 上，(UH4)、(UH9) 给
   \[
   \|U(x)-x\|\ge\|T(x)-x\|-\|U(x)-T(x)\|>\delta/2.
   \]
   因而没有新增固定点，也没有删掉原固定点，\(\operatorname{Fix}U=S\)。所以 \(U\in\mathfrak X\)。

现在对 \(0<t<r\) 取 \(x_t=a+te\)。这些点在 \(K\) 内，两 cutoff 在 \(a,x_t\) 都等于 1。故
\[
U(x_t)-U(a)=(1-\mu)(T(x_t)-T(a))+ct^\beta e,
\]
从而
\[
\frac{\|U(x_t)-U(a)\|}{\|x_t-a\|^\alpha}
\ge ct^{\beta-\alpha}-(1-\mu)M
\longrightarrow+\infty.
\tag{UH10}
\]
反三角不等式同时排除了原映射增量可能抵消尖点主项的问题。\(U\) 因此不满足任何有限 \(\alpha\)-Hölder 预算，尤其 \(U\notin\mathcal H_{\alpha,M}\)。

若 \(\mathcal H_{\alpha,M}=\varnothing\)，它当然无处稠密；否则上述构造对每个块内点及每个一致邻域都给出块外的 \(\mathfrak X\) 成员，所以该块相对内部为空。与闭性合并，得相对无处稠密。这里不需要对不在该块中的任意连续映射假定 Hölder 增量。

<a id="uht-countable"></a>
## 正指数并类的可数化

事实上
\[
\mathcal H_+=\bigcup_{m,n\ge1}\mathcal H_{1/m,n}.
\tag{UH11}
\]
右侧显然包含于左侧。若 \(T\in\mathcal H_{\alpha,M}\)，选整数 \(m\ge1\) 使 \(1/m\le\alpha\)。对 \(0<s\le D\)，
\[
s^\alpha\le D^{\alpha-1/m}s^{1/m}.
\]
取整数 \(n\ge\max\{1,MD^{\alpha-1/m}\}\)，即得 \(T\in\mathcal H_{1/m,n}\)；\(x=y\) 时不等式直接为零。每个右侧块闭且无处稠密，所以 (UH11) 是可数个无处稠密集的并。这正是 \(\mathcal H_+\) 在 \(\mathfrak X\) 中第一纲的含义。其补集是可数个稠密开集 \(\mathfrak X\setminus\mathcal H_{1/m,n}\) 的交；由上面的 Baire 门，这个 \(G_\delta\) 在 \(\mathfrak X\) 中稠密。证毕。

<a id="uht-boundary"></a>
## 范围、反例与证书接口

**不能删除离固定集的开区域而仍无条件保留结论。** 例如 \(K=[-1,1]\)、\(S=K\)，则 \(\mathfrak X=\{I\}\)。\(\mathcal H_{1,1}=\mathfrak X\)，在这个非空单点空间中有内点，不是无处稠密。这个例子只展示删除假设后的失败，不宣称 (UH1) 中每项都是必要条件。

**不能自动下传到收敛或共同尾子层。** 在 \(K=[-1,1]\)、\(S=\{0\}\) 上，(UH1) 成立。考虑固定实际尾预算
\[
e_0=2,\quad e_n=0\ (n\ge1),
\]
并以 \(T|_S=I\)、对全部 \(m\ge n\ge0\) 有 \(\|T^m-T^n\|_\infty\le e_n\)、对全部 \(n\ge0\) 有 \(\sup_{x\in K}d(T^n x,S)\le e_n\) 定义共同尾层。\(n=1\) 的距离条件强制 \(T(K)\subset S\)，因此此层恰为 \(\{T_0\}\)，其中 \(T_0(x)=0\)。它属于 \(\mathfrak X\)，一步终止，且具有全部正 Hölder 指数；\(\mathcal H_{1,1}\) 与该尾层的交为整个尾层，所以在尾层中不是第一纲。单点空间唯一无处稠密子集是空集。采用全时间轨道距离也不改变这个单点反例。

这个反例排除母空间第一纲向任意共同尾子层的自动转移。它没有计算全部无速率收敛映射空间中的类别。上面的 \(U\) 只受 (UH9) 的单步一致距离控制，未控制任何 \(U^n\)、极限回缩或共同尾。收敛母空间、全时间拓扑和非退化动力层中的相应命题均需新的保持构造或范畴转移定理。

<a id="uht-interfaces"></a>
## 两个可直接验收的同对象不等式接口

以下条件都作用于 (UH1) 的同一个 \(T\)、同一个完整工作域 \(K\) 和同一范数。它们允许常数随对象变化。

**局部距离范围的全对反射模。** 若存在 \(0<\gamma\le1\)、\(0\le L<\infty\)、\(R>0\)，使全部 \(x,y\in K\) 在 \(\|x-y\|\le R\) 时满足
\[
\|2T(x)-x-2T(y)+y\|\le L\|x-y\|^\gamma,
\tag{UH12}
\]
则 \(T\in\mathcal H_{\gamma,M}\)，其中可以取
\[
M=\max\left\{\frac{D^{1-\gamma}+L}{2},\frac{D}{R^\gamma}\right\}.
\tag{UH13}
\]
证明：令 \(s=\|x-y\|\)。当 \(0<s\le R\) 时，三角不等式及 \(s\le D\) 给
\[
2\|T(x)-T(y)\|
\le s+Ls^\gamma
\le(D^{1-\gamma}+L)s^\gamma.
\]
当 \(s>R\) 时，\(T(x),T(y)\in K\) 给 \(\|T(x)-T(y)\|\le D\le(D/R^\gamma)s^\gamma\)；\(s=0\) 直接成立。因此 (UH13) 是全工作域上的预算。满足某组 (UH12) 参数的全部 \(\mathfrak X\) 成员构成 \(\mathcal H_+\) 的子集，在 \(\mathfrak X\) 中第一纲。

**全对平方能量界。** 若存在 \(\tau\ge0\)、\(\epsilon\ge0\)，对全部 \(x,y\in K\) 有
\[
\|T(x)-T(y)\|^2
+\tau\|(x-T(x))-(y-T(y))\|^2
\le(1+\epsilon)\|x-y\|^2,
\tag{UH14}
\]
则丢掉左侧非负第二项后开平方，得到 \(T\in\mathcal H_{1,\sqrt{1+\epsilon}}\)。满足某组 (UH14) 参数的全部 \(\mathfrak X\) 成员也在 \(\mathfrak X\) 中第一纲。对子集的这一结论只用闭无处稠密块覆盖：每个子集与 \(\mathcal H_{1/m,n}\) 的交，其闭包仍包含在该闭块中。

**原生认证类的对象身份仍需单列。** (UH12)–(UH14) 已证明明定不等式类的包含，不自动把它们命名为全部 RLEB、LT 或极大单调类。任何实际认证类若要应用本页，须证明其成员属于同一 \(\mathfrak X\)，并在同一完整 \(K\) 上满足上述接口或其它正 Hölder 包含。仅有解点附近、轨道上、缩域后、选中分支上或另一步长图表上的条件，不是这里的全对同对象条件。本页未建立任意既有完整原图类、germ、AW 拓扑或变步长认证像与 \(\mathfrak X\) 的整体对象及拓扑身份；下段只核一份主动定义的紧源图卡。即使两个原生认证类分别完成这一包含，共同第一纲也不给二者严格包含、相对类别、覆盖比例或价值排序。

<a id="uht-source-card"></a>
## 完整紧源图卡的固定步长代数：复用 C179

这里仅核来源 §3 的具体源图定义，并复用 [C179 的 AW8 完整坐标恒等式](attouch_wets_fixed_input_thinness.md#aw-shear)。固定 \(\lambda>0\)、非空紧 \(K\) 与连续 \(T:K\to K\)，设 \(\operatorname{Fix}T=S\)，定义整个关系
\[
F_{T,K}(u)=\{(x-u)/\lambda:x\in K,\ T(x)=u\}.
\]
令 \(\Gamma_T=\{(x,T(x)):x\in K\}\)。它是非空紧集，而
\[
\operatorname{gph}F_{T,K}=L_\lambda^{-1}\Gamma_T,
\qquad L_\lambda(u,v)=(u+\lambda v,u).
\]
连续线性像保持紧性，故这确是非空紧闭原图。由完整关系的定义，
\[
u\in J_{\lambda F_{T,K}}(p)
\iff (u,(p-u)/\lambda)\in\operatorname{gph}F_{T,K}
\iff p\in K\ \text{且}\ u=T(p).
\]
因此完整 resolvent 在 \(K\) 上恰为 \(T\)，在 \(E\setminus K\) 上为空；\(0\in F_{T,K}(u)\) 当且仅当 \(u\in K\)、\(T(u)=u\)，所以精确零集为 \(S\)。

若进一步满足来源 §3 的 \(T(K)\subset S\)、\(T|_S=I\)，则每个非空 \(F_{T,K}(u)\) 都有 \(u\in S\)，从而 \(d(u,S)=0\)。这仅说明真实误差界的距离左端在所有非空输出纤维上为零；其证书充分性仍需各自的反射模、gauge及兼容条件。关系从一开始就被完整定义为上述集合，没有从某个先给原图中删除分支。

这段固定 \(\lambda\) 代数适用于这个明确图卡，未建立该回缩空间与宽 AW 母空间的拓扑同胚，也没有把 C179 的固定输入薄性转移到回缩算法子层。随 \(\lambda\) 改变这份定义一般会改变原图；它不是同一既有 \(F\) 的任意步长断言。来源 §3 的回缩空间完备性、Lipschitz插值、正 Hölder 并类自第一纲以及 RLEB 证书等价，均不由 C179 的 AW1–AW9 推出。

<a id="uht-source"></a>
## 来源与数学状态

C180-v1 标记为 `derived-checked`，证据为 (UH1)–(UH14)、(UH-B) 的直接证明以及上面的两个明确反例；全球先行性、来源的历史审查行为和其他定理不由该状态认证。

原思路来自 [05_obstruction_audit.md](../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/03_CLASSIFICATION_STAGE/ppa_classification_team/05_obstruction_audit.md) §7.1，物理 LF400–404；原稿 §1（LF13–50）明确区分“固定 \(S\) 上恒等”和“精确固定集”，§6.3 后的 LF390 明确维持有限维首版。[07_stage_synthesis.md](../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/03_CLASSIFICATION_STAGE/ppa_classification_team/07_stage_synthesis.md) B1（LF97–104）复述该结果。本页明写 \(\mathfrak X\ne\varnothing\)、环境内点、范数、预算量词与三项保持估计；没有把来源中的证书措辞补作隐藏假设。

来源 §7.1 的局部尖点方法在上述范围内成立，但原稿简述没有给出 cutoff、两个独立余量和精确预算；(UH4)–(UH10) 补齐这些承重点。关于收敛/共同尾的原警告得到明确单点尾层见证，证书结论则仅保留已核包含门。完整来源的逐断言去向与枚举边界记于 [专用审计](../audit/UNIFORM_HOLDER_FULL_COVERAGE.md)。
