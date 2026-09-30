# 文献覆盖与原创边界：交给数学家团队的定位说明

日期：2026-09-20。范围：中立 PPA 算子空间、收敛动力学层、证书嵌入及范畴比较。本文不重审原 RLEB 正文，也不将当前结构层的数学正确性等同于其原创性已获确认。

## 1. 直接判断

用户期望的研究范式——先在有独立意义的算子空间中组织收敛行为，再比较两套可验证条件的覆盖——有充分先例，值得沿此方向继续。**不能把“算子空间＋Baire 分类”本身作为新创意，也不能因这些部件已知而判定 RLEB–LT 比较整体已知。**

目前的分界是：

- 已有文献分别提供收敛母类、固定多解集上的泛型回缩、全时间拓扑、相容 resolvent 族、共同收敛模，以及结构子类的无处稠密定理。
- 项目仍缺将这些工具接到同一个完整 PPA 对象上的桥梁：保留原全图、全部 proximal 解、真实最小残差、同一初值域、实际动力学预算和步长量词，然后证明类的位置及其跨层迁移。
- 当前“正常收缩＋切向漂移”变形定理可以作为桥梁的一个候选工具；若不能证明该结构层在中立母空间中的位置及层间转移，它仍只能说明一个受限层，不完成理想目标。

因此交接任务应是**寻找中立不变量与保类／保纲桥梁，或证明所要求的桥梁不可能**，而不是请数学家再设计一个更奇异的例子。

本轮回看了下列公开原文的相关定义和定理。BRZ 2001 使用工作区保存的原始论文文本核对；部分后续文献链仅核到书目信息，单列为待清关。定理编号按明确指定的版本，不将预印本编号冒称期刊编号。

## 2. 已经有定理支撑的各层

### 2.1 收敛母类与轨道分解：WPO

**Ioan A. Rus**, *Weakly Picard mappings*, Commentationes Mathematicae Universitatis Carolinae **34**(4) (1993), 769–773。公开原文：[DML-CZ PDF](https://dml.cz/bitstream/handle/10338.dmlcz/118632/CommentatMathUnivCarolRetro_34-1993-4_14.pdf)。未核到 DOI/arXiv，不补造。

核对位置：Definition 2，Theorems 1–2。所有初值的迭代收敛到允许依赖初值的不动点，已有 weakly Picard 语言。存在某个完备度量／广义度量使映射具有该性质，也是其研究内容。

**未覆盖的桥：**更换状态空间度量不保原 Hilbert 几何、PPA inclusion、RL 模和 EB；该文不建立原几何下全部可收敛 PPA 的统一算子范畴比较。

**Ioan A. Rus, Adrian Petruşel, Marcel Adrian Şerban**, *Weakly Picard operators: equivalent definitions, applications and open problems*, Fixed Point Theory **7**(1) (2006), 3–22。[期刊原文](https://www.math.ubbcluj.ro/~nodeacj/download.php?f=061rus.pdf)。未核到 DOI/arXiv。

核对位置：Definition 1.6，Theorems 6.2、8.1。Theorem 6.2 在完备 K-metric 空间的 closed Q-graph contraction 条件下给出 WPO、有限长度、极限纤维分解及

\[
d(A^nx,A^\infty x)\le (I-Q)^{-1}Q^n d(x,Ax).
\]

Theorem 8.1 的若干等价表征允许改变收敛结构。**已有的是轨道结构语言；未有的是本项目完整图证书在原几何中的表示与类比较。**因此“定义极限回缩／按选中解分纤维”不能单独主张原创。

### 2.2 固定非单点目标集上的泛型回缩：最接近的先例

**Dan Butnariu, Simeon Reich, Alexander J. Zaslavski**, *Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces*, Journal of Applied Analysis **7**(2) (2001), 151–174。[DOI 10.1515/JAA.2001.151](https://doi.org/10.1515/JAA.2001.151)，[作者原始 PS](https://math.haifa.ac.il/dbutnaru/publications/but-rei-zas-jaa.ps)。

核对位置：Assumption A，Theorems 2.1、3.1、3.2，Lemmas 4.1、4.2、5.1。固定闭凸目标集 \(S\)，使用相对 Bregman 下降母类

\[
\mathcal M=\{T:K\to K:D_f(s,Tx)\le D_f(s,x),\ s\in S,\ x\in K\}.
\]

在原文距离相容性、投影和连续性条件下，有界集一致拓扑中的泛型迭代一致趋于到 \(S\) 的回缩，并有邻近算子的长期控制。投影混合 \(T_\eta=\eta P+(1-\eta)T\) 是保类变形工具。

**精确边界：**母类固定共同目标 \(S\)，通常只先保证 \(S\subseteq\operatorname{Fix}T\)；泛型结论才迫使 \(\operatorname{Fix}T=S\)。更重要的是母类预装共同 Bregman 下降，不能未经表示定理就把一般非 Fejér RLEB 放进去。它不是当前全部 PPA 收敛者空间的现成替代品。

### 2.3 长期行为母类与全时间拓扑：Tikhonov

**Sergei V. Tikhonov**, *Complete metric on mixing actions of general groups*, Journal of Dynamical and Control Systems **19** (2013), 17–31。[DOI 10.1007/s10883-013-9162-y](https://doi.org/10.1007/s10883-013-9162-y)，[arXiv:1207.5255](https://arxiv.org/pdf/1207.5255)。

核对位置：§§1–2，Lemmas 1–2，Theorem 1。以 mixing 长期性质定义群作用母类，再使用

\[
m(T,U)=d(T,U)+\sup_{g\in G}a(T^g,U^g)
\]

得到完备可分空间。相同距离放到更大的全部群作用类，可能不再可分。

**已有的 idea：**先按长期行为定义空间，再强化全时间控制以获得 Polish 结构。**未覆盖的桥：**该文研究测度相关函数的 mixing，不是点轨道的 PPA 收敛；也不证明动态拓扑与原图拓扑保同一纲。项目的全时间拓扑有独立合理性，但不能由此把在该拓扑中的小类直接称为 AW／单步拓扑中的小类。

### 2.4 相容 resolvent 家族与抽象 PPA

**Laurenţiu Leuştean, Adriana Nicolae, Andrei Sipoş**, *An abstract proximal point algorithm*, Journal of Global Optimization **72** (2018), 553–577。[DOI 10.1007/s10898-018-0655-9](https://doi.org/10.1007/s10898-018-0655-9)，[arXiv:1711.09455](https://arxiv.org/pdf/1711.09455)。

核对位置：Definition 3.6，Theorems 3.13、3.15、5.1。共同不动点、jointly firmly nonexpansive／jointly(P2) 家族及步长条件导出 \(\Delta\)／弱收敛；共同 uniform(P2) 等加强条件给强收敛率。

**Andrei Sipoş**, *Revisiting jointly firmly nonexpansive families of mappings*, Optimization **71**(13) (2022), 3819–3834。[DOI 10.1080/02331934.2021.1915312](https://doi.org/10.1080/02331934.2021.1915312)，[arXiv:2006.02167v3](https://arxiv.org/html/2006.02167v3)。

核对位置：Theorems 3.3、5.3，编号按 arXiv v3。Theorem 3.3 将 jointly FNE 等价于每个 \(T_\gamma\) 非扩张加 resolvent identity

\[
T_{(1-t)\gamma}((1-t)x+tT_\gamma x)=T_\gamma x,
\qquad0\le t<1.
\]

Theorem 5.3 是步长参数趋于无穷时的投影极限，不是固定步长反复迭代的极限。

**未覆盖的桥：**非单调、可能多值、仅局部良定的完整同一原图，在所有可用步长上的表示与类大小。一般关系的 graph-shear 恒等式是基础代数，不宜独立包装为新的收敛定理；额外动力学后果才有研究内容。

### 2.5 证书转共同动力学模：proof mining

**Ulrich Kohlenbach, Genaro López-Acedo, Adriana Nicolae**, *Moduli of regularity and rates of convergence for Fejér monotone sequences*, Israel Journal of Mathematics **232** (2019), 261–297。[DOI 10.1007/s11856-019-1870-x](https://doi.org/10.1007/s11856-019-1870-x)，[arXiv:1711.02130](https://arxiv.org/pdf/1711.02130)。

核对位置：Definition 3.1，Theorem 4.1，Proposition 4.4 及 PPA 应用。Fejér 性、近似零点界 \(\alpha\) 与 regularity modulus \(\varphi\) 给共同 Cauchy 模 \(\alpha(\varphi(\varepsilon/2))\)。PPA 应用采用 \(\operatorname{dist}(0,A(x))\) 的完整值集残差。Proposition 4.4 还在非扩张条件下，从共同初值收敛率反推出 regularity modulus。

**未覆盖的桥：**非 Fejér RLEB 到同一无标签动力学坐标的双向表征，以及这些坐标下证书像的保纲性。不能把“统一模”或“用真实残差”本身记为全新。

作为相关但不同的工具，**Jeremy Avigad, José Iovino**, *Ultraproducts and metastability*, [arXiv:1301.3063v4](https://arxiv.org/html/1301.3063v4)，Theorem 2.1，给类的统一 metastability 与超积序列收敛之间的关系。它可以组织统一见证，但不能把有限窗口量词自动变成共同无限尾界。本交接不补未核定的期刊编号。

### 2.6 真正研究“算子类有多大”的先例

**Xianfu Wang**, *Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent*, Nonlinear Analysis **87** (2013), 69–82。[DOI 10.1016/j.na.2013.03.008](https://doi.org/10.1016/j.na.2013.03.008)，[arXiv:1301.6443](https://arxiv.org/pdf/1301.6443)。

核对位置：Propositions 2.1、2.3、2.4，Theorems 2.13–2.16，Corollaries 2.17、3.9–3.10。极大单调图、FNE resolvent、非扩张 reflector 经完备度量联系；收缩稠密机制给泛型 super-regular／唯一零点。强单调类本身可以稠密而第一纲。

**未覆盖的桥：**预先固定非点 \(S\) 后严格收缩不存在，原稠密机制不能直接使用。这也说明“第一纲”绝不等于数学上差、应用上无用，更不是比例小的数值结论。

**Heinz H. Bauschke, Jason Schaad, Xianfu Wang**, *On Douglas–Rachford operators that fail to be proximal mappings*, Mathematical Programming **168** (2018), 55–61。[DOI 10.1007/s10107-016-1076-5](https://doi.org/10.1007/s10107-016-1076-5)，[arXiv:1602.05626](https://arxiv.org/pdf/1602.05626)。

核对位置：Proposition 2.8，Theorem 3.1，Remark 3.3。\(\mathbb R^n\)、\(n\ge2\)，对称极大单调线性关系对空间配 resolvent 算子范数；产生 proximal Douglas–Rachford 映射的子类闭且无处稠密。

这正是“先固定有结构母空间，再比较结构子类”的已成定理范式。**边界：**对象是线性关系对，不是一般非线性单算子 PPA；Remark 3.3 曾把推广至一般次微分列为问题，不能未经后续检索宣称该问题至今仍开放。

### 2.7 模饱和与拓扑敏感性

**Davide Ravasini**, *Generic uniformly continuous mappings on unbounded hyperbolic spaces*, Journal of Mathematical Analysis and Applications **538**(1) (2024), 128440。[DOI 10.1016/j.jmaa.2024.128440](https://doi.org/10.1016/j.jmaa.2024.128440)，[arXiv:2308.15277v2](https://arxiv.org/html/2308.15277v2)。

核对位置：Lemma 3.2，Theorems 3.3、4.1、5.2。固定非零凹模的自映射空间，在完整无界 hyperbolic 域及有界集一致拓扑下，泛型模恰等于允许模；有界像空间与不同拓扑需使用不同定理。

**未覆盖的桥：**固定解点附近的非 Lipschitz、共同实际尾、完整纤维 EB 及精确固定集均不随模饱和自动得到。全局模的见证点对可逃到无穷。因此套一句“Lipschitz 在 Hölder 中第一纲”并不完成 RLEB–LT 比较。

**Davide Ravasini, Daylen K. Thimm**, *Generic nonexpansive Hilbert space mappings*, Studia Mathematica **283** (2025), 281–301。[DOI 10.4064/sm240722-12-3](https://doi.org/10.4064/sm240722-12-3)，[arXiv:2407.03881v2](https://arxiv.org/pdf/2407.03881v2)。

核对位置：Theorems 4.1、4.2、5.3。可分无限维 Hilbert 空间中，逐点拓扑下的泛型固定点／无固定点行为依赖域的 somewhat bounded／totally unbounded 几何。此处第二作者是 **Daylen K. Thimm**，更正旧笔记中的姓名误写。

它与 Wang 的有界集一致拓扑结果不矛盾。**对本项目的警告：**“同一个算子类”而拓扑不同，可以有不同泛型结论；拓扑不是可以最后再补的说明。

## 3. LT 基准应锁定为哪套原始定理

**D. Russell Luke, Matthew K. Tam**, *Generalized Monotonicity and the Proximal Point Algorithm*, Mathematics of Operations Research，2025 online。[DOI 10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)。基准位置：正式版 Definition 2，Propositions 3–4，Lemma 1，Assumption 2，Theorem 2。

该文给 submonotonicity 与 resolvent 几何的对应，以及 metric subregularity 下的局部线性 PPA 收敛。它不是算子空间的 Baire 类比较论文。项目已有的同接口翻译将 all-pairs 几何写作 reflector Lipschitz 条件；这不等于把所有 LT/LTT 定理都化约为同一个类。

**D. Russell Luke, Nguyen H. Thao, Matthew K. Tam**, *Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings*, Mathematics of Operations Research **43** (2018), 1143–1176。[DOI 10.1287/moor.2017.0898](https://doi.org/10.1287/moor.2017.0898)，[arXiv:1605.05725v2](https://arxiv.org/abs/1605.05725v2)。按 v2：Definition 2.3，Proposition 2.4，Definition 2.17，Theorem 2.18，Corollary 2.19。

其 pointwise almost-averaged 与 gauge metric subregularity 允许不同于 all-pairs 单值接口的对象。**因此比较必须声明 LT2025 all-pairs、LTT pointwise 或两者并类。**把 LT 公共证书纳入 RLEB-energy 可以解决包含的组织问题，却不解决中立母空间内的覆盖规模。

## 4. 仍缺哪几条桥：这才是可交给数学家想 idea 的地方

以下是从上述文献与本项目数学状态作出的研究判断，不冒充现成文献定理。

| 候选桥梁 | 已有工具到哪里 | 目前准确缺口 | 应接受的成果形式 |
|---|---|---|---|
| **中立表示桥** | WPO、有限长度、共同模、resolvent family 都已有 | 从原 RLEB／LT 假设推出哪些不带证书标签的内生不变量；是否有必要充分或接近必要的表示 | 表征定理、严格单向嵌入及不能反向的结构原因 |
| **对象闭合桥** | 固定步长完整图编码、扩张、共轭、BRZ 投影混合、模饱和可用 | 同时保持完整原图语义、精确 \(S\)、真实 EB、共同域和实际尾；不是只保持单步正则性 | 统一闭合操作／局部坐标定理，或证明某组保持要求相互冲突 |
| **母空间位置桥** | 结构层内部的范畴分析及一般开放映射工具 | 当前正常收缩—漂移层在中立良定／收敛空间中究竟开、稠密、非第一纲还是薄层 | 位置定理，允许结果是否定；不能只赋予该层更强拓扑后自证 Baire |
| **跨尺度保纲桥** | 共同尾时两种拓扑的有限段＋尾部比较；已有近恒等变形 | \(\mathfrak D_e\to\mathfrak D_{(1+\varepsilon)e}\) 不等于同层稠密；需要开放／保纲映射或合适分层原理 | 可检验的保纲／稳定剖面定理，或精确尾预算不可迁移的障碍定理 |
| **步长与 witness 消去桥** | 同图 resolvent identity；项目有部分实步长紧块编码 | 不能把一份证书的类别直接投成原算子的类别；也不能假设可用步长谱开放后只取有理数 | 无标签对象侧的表示、步长谱结构及量词完整的比较 |

一条有意义的目标，不必预设所有 RLEB 总类都是 Baire。可以先在**独立于证书定义**的中立 Polish 空间 \(\mathfrak X\) 或明确自然的层中，证明某个非空开区 \(V\) 满足

\[
\mathcal R\cap V\text{ 非第一纲（或余稀）},\qquad
\mathcal L\cap V\text{ 第一纲},
\]

并给 \(V\) 的动力学意义、步长量词和与原图拓扑的联系。另一种同样有内容的答案是证明该配置不可能，转而给出两类不同的性能谱／几何结构剖面。**不能把想获得的类差结论写进母空间定义。**

若只证明 \(\mathcal L\) 在一个可能自第一纲的 \(\mathcal R\) 中第一纲，或者仅在预装超吸引的层中证明差集余稀，理想比较仍未完成。这里的问题是推论桥缺失，不是“再多跑几轮审稿”即可自动解决。

## 5. 哪些可谈创新，哪些仍未清关

### 5.1 已有强先例，不应单列为原创主张

- WPO、极限选择、按最终解分纤维、有限长度到选中极限的界；
- 固定共同非点目标集的算子空间与泛型回缩；
- 为长期动力学定义全时间拓扑并证明完备／可分；
- 非扩张 resolvent family 的公理化、identity 与 joint FNE 表征；
- Fejér 条件下 regularity modulus 到共同收敛率；
- 极大单调／FNE／非扩张空间中的泛型性质；
- 模饱和、较强正则性子类的第一纲、凸混合或开放映射的标准范畴机制。

这些是应引用和复用的语言，不是本项目应从零重造的东西。

### 5.2 可能有实质新内容，但尚非首创判决

1. **完整非单调图的内生证书表示。**特别是同时处理外部输入纤维、允许缩域与固定宏观域、任意实步长和无标签证书像。描述集论的投影技巧本身是标准的；新增价值须在准确数学对象和非平凡结构后果。
2. **保全纤维 EB 与实际动力学的结构操作。**若能建立一般闭合或刚性定理，而不局限于一个预设尖点族，会成为桥梁的实质内容。
3. **中立分层中的 RLEB–LT 覆盖判决及跨层迁移。**这是理想目标的核心；上述文献没有直接供给此结论，但尚未证明检索穷尽。
4. **完整局部步长谱的实现／限制。**当前任意紧谱实现及单值良定与全选择收敛谱分离值得独立审计优先权；不能仅因以新记号命名谱，就判断首次。

### 5.3 优先权仍需专门补查的链

| 文献链 | 当前核查状态 | 交给数学家／文献组的准确问题 |
|---|---|---|
| **S. Reich, A. J. Zaslavski**, *Convergence of generic infinite products of nonexpansive and uniformly continuous operators*, Nonlinear Analysis **36** (1999), 1049–1065，[DOI 10.1016/S0362-546X(98)00080-7](https://doi.org/10.1016/S0362-546X(98)00080-7) | 书目和摘要已核；本交接未完成原文逐定理核对，不补定理号 | 是否已有比 BRZ 更一般、保共同吸引集／Lyapunov 模的空间与保类操作？ |
| **S. Reich, A. J. Zaslavski**, *Genericity in Nonlinear Analysis*, Springer (2014)，[DOI 10.1007/978-1-4614-9533-8](https://doi.org/10.1007/978-1-4614-9533-8) | 未完整读相关章节；目录不能当覆盖证明 | convex Lyapunov、Bregman、powers、infinite products 各章是否包含本项目所需非 Fejér 桥梁或其不可能性？ |
| **Filip Strobin**, *Some porous and meagre sets of continuous mappings*, Journal of Nonlinear and Convex Analysis **13**(2) (2012), 351–361 | Ravasini 原文确认其先例位置；未取得可核定理页，不补 DOI／定理号 | 固定 trace／局部域／指定模的原始最早结论到底到哪一步？ |
| 一般 WPO／c-WPO 算子空间、稳定性与算子拓扑后续文献 | 已核 Rus 主干，不是穷尽性审计 | 是否已有原几何下全部 WPO 的算子空间表示及类分离，而非更换状态空间度量？ |
| Attouch–Wets／graphical convergence、generalized resolvent、局部谱与参数依赖 | 当前只具备相关接口先例 | 任意紧局部良定谱等实现是否已有抽象关系论版本？强限制下是否有谱开性定理？ |
| 描述集论中的收敛算子集、Baire 分解及 category-preserving maps | 现有项目用了标准工具，尚未作专门优先权清关 | 当前 \(F_\sigma\)/\(K_\sigma\)、全轨道闭表示及跨层转移，哪些只是一般定理的直接应用？ |

“尚未清关”不是“很可能已知”，也不是“搜索没结果所以新”。数学家团队可以先研究桥梁，同时由文献组定理级查证；两条工作线不应相互替代。

## 6. 对现有建议的最终定位

“先把仿射 \(S\)＋正常收缩＋切向非退化做完”有两种不同身份：

1. **作为受控实验层与构建工具：合理。**它可以验证哪些不变量可一起保持，以及哪类 RLEB 证书与 LT 必要条件冲突。
2. **作为理想总体比较的替代品：不够。**没有母空间位置、非退化分母与跨尺度桥梁，层内定理不能回答用户真正问的“在统一体系下多出多少”。

后续是否继续做该层，应由它能否帮助完成第 4 节桥梁来判断，而不是由它是否容易制造非 Lipschitz 来判断。若桥梁受刚性阻碍，交接包应把“哪条保持要求导致哪项变形／迁移不可能”陈述成明确问题，允许数学家提出不同的不变量、拓扑或分类对象。

**可对外使用的谨慎表述：**现有研究已建立若干基础空间、表示模块及受限结构层结果；原始文献支持这种体系化路径，但中立母空间中的 RLEB–LT 类规模判决尚未完成。当前最可能产生实质新理论的地方，是将原图证书与长期动力学分类接起来的结构定理，而不是外层语言本身。
