# 一手文献事实与本项目的定理导入

本页只把已经读到原文的**确切语句**与本项目的解释分开记录。文献事实不证明项目稿件中的其他前提，也不判定新颖性。后续新增文献时给版本、页码、原定理假设和逐项对象映射。

<a id="lit-bwy-2012"></a>
## LIT-BWY-2012 · 三种图例的来源及版本编号

**Paper fact / 本次原文核验。** H. H. Bauschke, X. Wang, L. Yao,
*Rectangularity and paramonotonicity of maximally monotone operators*，
[arXiv:1201.4220v1](https://arxiv.org/abs/1201.4220v1)，
[v1 PDF](https://arxiv.org/pdf/1201.4220v1)。核对的是该 v1；
[作者站 074.pdf](https://bauschke.ca/publications) 所链接的 22 页稿有不同编号：

| v1 的精确位置 | 已核内容 | 作者站稿的对应编号 |
| --- | --- | --- |
| p.9，Proposition 3.4 / Example 3.5 | 平面斜旋转加单位球法锥：极大单调、rectangular、非 paramonotone | Proposition 3.6 / Example 3.7 |
| p.14，Proposition 5.1 | 连续、线性、单调 \(A:X\to X^*\) 的 rectangularity 等价于存在正 cocoercivity 系数；实 Hilbert 情形另有等价项 | Proposition 5.2 |
| pp.15–16，Example 5.3 | \(L^2[0,1]\) 的 Volterra 及其伴随均非 rectangular、非 paramonotone | Example 5.4 |
| p.17，Example 5.5 | \(\ell^2\) 上对角 \(1/n\) 与成对斜旋转的**和**：严格且极大单调、paramonotone、非 rectangular | Example 5.7 |

**项目身份。** 分别对应 GX-058、GX-060/061、GX-059；这些例卡的结论已有
直接规范证明。Proposition 5.1 不是非线性、多值或受限图的无条件接口。
此核验关闭列出的原文归属和编号，不认证例卡后来增加的锐 RL、残差或路径结果，
也不判定本项目新颖性。不能把作者站稿编号直接拼到 v1 引用上。

<a id="lit-voisei-2024"></a>
## LIT-VOISEI-2024 · 旋转的有限循环阶

**Paper fact。** M. D. Voisei, *General monotonicity*，
[arXiv:2411.04212v2](https://arxiv.org/abs/2411.04212v2)，
[v2 PDF](https://arxiv.org/pdf/2411.04212v2)，当前入口已核为 2024-11-18 的 v2。
印刷页 31，Example 43 (Rotation)：全域平面旋转 \(R_\theta\)，
\(-\pi\le\theta\le\pi\)，对每个整数 \(n\ge2\)，
\(n\)-monotone（并为该类极大）当且仅当 \(|\theta|\le\pi/n\)；
全循环单调当且仅当 \(\theta=0\)。v1 的同号例不是同一定位，须带版本引用。

**项目身份。** [C123](topics/examples/planar_rotation_family.md#pr-cyclic)
在规范页以循环二次型独立证明相同阈值。此文献事实不认证该页的完整 Minty
奇点、RL 常数、MR 或任何总体类大小结论。

<a id="lit-lei-he-2020"></a>
## LIT-LEI-HE-2020 · VI 伪单调与拟单调的严格前件

**Paper fact。** Ming Lei, Yiran He,
*A hybrid projection-proximal point algorithm for solving nonmonotone variational inequality problems*，
[作者提交的 Optimization Online PDF](https://optimization-online.org/wp-content/uploads/2020/02/7602.pdf)，
印刷页 3，Definitions 2.2–2.3：有限维单值 \(F\) 在 \(C\) 上，对所有
\(x,y\in C\)，pseudo 的符号前件为非负，quasi 的前件为严格正，
后件均为 \(\langle F(y),y-x\rangle\ge0\)。同页给
\(F(x)=x^2,C=[-1,1]\) 的 quasi 非 pseudo 例。

**项目身份。** [PD-GEOMETRY](canonical/parameter_dictionary.md#pd-geometry)
冻结所用的 VI 类型；GX-064 的正值函数和 GX-065 的平方例须用各自直接证明。
这里没有导入该文算法收敛定理，也不把 VI 条件换成弱序列或多值版本。

<a id="lit-lt-2025"></a>
## LIT-LT-2025 · 非负 LT violation 的准确对象

**Paper fact。** D. Russell Luke, Matthew K. Tam,
*Generalized Monotonicity and the Proximal Point Algorithm*，
[出版社完整正文](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)，
§3 Definition 2 / (10)：在 \(U\times W\) 的全部图点对上，\(\tau\ge0\)
且 \(\langle\Delta u,\Delta v\rangle\ge-\tau\|\Delta u+\Delta v\|^2\)。
文献的这一显示式步长为 1；固定 \(\lambda\) 的项目式用于关系 \(\lambda F\)，
不是不声明变换就移动步长。

**项目推导。** [PD-TIED](canonical/parameter_dictionary.md#pd-tied) 的平方恒等式
在同一图给 \(L^2=1+4\tau\) 的参数转换；若锐反射模小于 1，最小**非负**
violation 为 0。这个直接代数结论与文献 Proposition 4 自带的
\(\tau<1/2\) 范围分别记录，不把该命题的原范围偷偷放宽。
§3 和参考文献 [38] 只给 Spingarn 名称的二手定位；1981 原文全文本次仍被
访问门阻挡，因此没有认证其完整映射、极大性或一阶商与该名称等价。

<a id="lit-hoffman-1952"></a>
## LIT-HOFFMAN-1952 · 固定线性系统的一致右端误差界

**Paper fact.** A. J. Hoffman, “On Approximate Solutions of Systems of Linear Inequalities,” *Journal of Research of the National Bureau of Standards* **49** (1952), 263–265, [NIST 原文](https://nvlpubs.nist.gov/nistpubs/jres/049/4/V49.N04.A05.pdf), DOI [10.6028/jres.049.027](https://doi.org/10.6028/jres.049.027)。印刷页 263，§2 主定理：对**有解**的有限线性不等式系统与允许的正齐次距离量尺，存在误差界常数，使到可行集的距离受违反量控制。证明在页 263–264 通过有限活动行子集取常数；因此固定左端矩阵时可在所有**有解的**右端间选取同一常数。等式可写成两侧不等式，在有限维用所需的 \(\ell^1\) 范数。

**Project mapping / scope.** [FS-HOFFMAN](topics/random_markov/finite_state_certificate.md#fs-hoffman) 的零面系统只在 \(Z_k\ne\varnothing\) 时调用；空零面以紧性和正成本下界替代。[FS-REGULARITY](topics/random_markov/finite_state_certificate.md#fs-regularity) 对每个目标边缘 \(b'\) 的最优计划集 \(\mathsf S(b')\) 非空，且所有系统的左端矩阵相同，右端 \((b',w(b'))\) 变动。该文不证明有限状态模型的最优耦合表示、锐常数、分片仿射结构或跨模型统一模，这些是项目内另行推导。

<a id="lit-alm-2021"></a>
## LIT-ALM-2021 · Hilbert 间同常数 Lipschitz 扩张

**Paper fact.** D. Azagra, E. Le Gruyer, C. Mudarra, “Kirszbraun’s Theorem via an Explicit Formula,” *Canadian Mathematical Bulletin* **64** (2021), 142–153, [出版社正式 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/15797B44C630B0E2A4BB12547759929D/S0008439520000314a.pdf/kirszbrauns_theorem_via_an_explicit_formula.pdf), DOI [10.4153/S0008439520000314](https://doi.org/10.4153/S0008439520000314)。印刷页 144 **Theorem 1.2**：任意两个 Hilbert 空间 `X,Y`、任意子集 `E⊂X`、Lipschitz `G:E→Y`，可扩张为 `X→Y` 且保持 Lipschitz 常数。论文给出一个显式公式；本项目只导入存在与同常数性质，不使用该公式的额外正则性。历史稿其他位置若按预印本的编号引 “Theorem 2”，不可直接当正式出版版 Theorem 2；此处以正式页码与 Theorem 1.2 为准。

**Project mapping (2026-10-01).** [HE-EXTENSION](canonical/holder_extension.md#he-extension) 先用 (HE2)–(HE4) 独立将 `H` 的 `γ` 雪花等距嵌入一个 Hilbert `E_γ`，再令源子集为 `J(D)⊂E_γ`、目标为原 Hilbert `H`、Lipschitz 常数为 `L`。因此 [H01](holder_structure.md#h01) 中同一 `λ,L,γ` 的 graph-maximal 完成可用这条**准确引文 + 独立嵌入**调用。此文不证明随机分支、局部图块 coverage、其他 topology/degree 引用或文献先行性。

<a id="lit-grn-2002"></a>
## LIT-GRN-2002 · Górniewicz–Rozpłoch-Nowakowska 的 morphism Lefschetz 定理

**Paper fact.** L. Górniewicz and D. Rozpłoch-Nowakowska, “The Lefschetz Fixed Point Theory for Morphisms in Topological Vector Spaces,” *Topological Methods in Nonlinear Analysis* **20** (2002), 315–333, [期刊原版 PDF](https://www.tmna.ncu.pl/static/files/v20n2-07.pdf), DOI [10.12775/TMNA.2002.039](https://doi.org/10.12775/TMNA.2002.039). 该文印刷页 327 的 Theorem 6.2：若 \(X\) 是 Klee-admissible 拓扑向量空间 \(E\) 中某个开集的 retract，且 \(\varphi\in M(X,X)\) 属于 \(CAC(X)\)，则其 Lefschetz 数有定义；若数不为零，\(\varphi\) 有固定点。印刷页 315–318 的 Definition 1.1、2.1–2.4 把 morphism 表示为 \(X\xleftarrow{p}\Gamma\xrightarrow{q}X\)：\(p\) 是 perfect surjection 且每个纤维在**有理 Čech homology with compact carriers** 下 acyclic，\(q\) 连续。印刷页 320–322 的 Definition 2.6、3.1 与紧类包含关系 \(K(X)\subset CAC(X)\) 表明紧 morphism 足以满足 Theorem 6.2 的动力条件。此定理本身不要求 morphism 的输出纤维 acyclic。

**Interpretation / C05-v1 import check (2026-10-01).** 对 [9/25 候选稿 §8, Theorem 8.1](../history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)，取 \(X=A\subset\mathbb R^n\)，\(\Gamma=\{(p,y):p\in A,y\in T(p)\}\)，\(p=\pi(p,y)\)，\(q=e_h(p,y)=y+\lambda h(y)\)。逐项门如下：

| 引文前提 | 稿件中对应的**额外假设或推导** |
| --- | --- |
| \(E\) Klee-admissible，\(X\) 为开集 retract | \(E=\mathbb R^n\)；\(A\) 是紧有限多面体，故是 Euclidean neighborhood retract。 |
| \(p\) Vietoris，\(q\) 连续 | \(A\) 紧、\(T\) 在邻域 usc、非空紧值，给紧图与 perfect surjection；\(T(p)\) 的有理 Čech acyclicity 给纤维条件。\(h\) 连续给 \(e_h\) 连续。注意原稿用 Čech **cohomology** 描述 acyclicity，需采用其对紧度量纤维的有理 homology 等价。 |
| \(q(\Gamma)\subset A\)，紧 morphism \(\subset CAC(A)\) | 原稿 (8.4) 的完整 shell/collar 和 (8.7) 保证每个 \(y\in T(p)\) 离 \(A^c\) 至少 \(m-\alpha\)；\(\sup_A\|h\|<(m-\alpha)/\lambda\) 故 \(e_h(\Gamma)\subset\operatorname{int}A\)。紧 \(\Gamma\) 的连续像紧，按原文 \(K(A)\subset CAC(A)\)。 |
| 非零 Lefschetz 数 | 原稿要求 \(b^*:H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 全阶满射，并用 \([p,y]\subset B\) 得 \(e^*=\pi^*\)；\(e_{th}\) 全在 \(A\) 中，同伦不改诱导映射。有限多面体上的有理同调与上同调维数有限，因此 \(\Lambda=\chi(A)\ne0\)。 |

**审查结论与边界。** 原引文确实适用于上述**紧 span**，不需要另证明非线性像 \(e_h(T(p))\) acyclic。这里关闭的是“[6, Theorem 6.2] 是否有 CAC/图/回缩适用门”这一个导入问题。原稿整条 C05-v1 仍是候选：有限观测不能证明整窗 (8.1)–(8.2)、\(T\) 的存在、usc 与 acyclicity，也没有逐行 referee 其余数值包络或核外部先行性。若换成非紧 \(A\)、放弃全部纤维 acyclicity、或只凭有限样本声称整窗条件，就不再是同一导入。稿件的 Čech cohomology/homology 等价是单独的标准拓扑事实，本次只在紧度量纤维范围使用，没有把它扩张到任意空间。 同一导入门在保留整窗与拓扑假设、仅改 q>0 的 [C05-v2](canonical/local_range_without_supercriticality.md#lr-theorem) 中亦适用；这项新版本不是该论文或 9/25 原稿的陈述。
