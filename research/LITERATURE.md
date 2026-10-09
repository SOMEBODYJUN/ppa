# 一手文献事实与本项目的定理导入

本页只把已经读到原文的**确切语句**与本项目的解释分开记录。文献事实不证明项目稿件中的其他前提，也不判定新颖性。后续新增文献时给版本、页码、原定理假设和逐项对象映射。

<a id="lit-august-gppa-nfb"></a>
## LIT-AUGUST-GPPA-NFB · 固定v1逐结果比较

| 一手版本及实读位置 | Paper fact | 本库推导与明确限域 |
| --- | --- | --- |
| Le–Mordukhovich–Théra，[2608.01584v1](https://arxiv.org/abs/2608.01584v1)，首发2026-08-03；Def1/3/4/5/6、T1 p6、T2 pp7–8、Lemma3 pp8–9、T4 pp9–11 | T2允许非线性非单射kernel、完整all-pairs adaptive强门与warped coverage，给核率；逆像R-Lipschitz另给集合距离率。T4换到F+εv、均匀不消失误差δ=ε²，给原零集的双极限邻近界 | [逐篇报告](comparisons/2026_08_gppa_nfb/gppa_review.md) 重构T2及T4小技术门修补；C199保同原图普通选择并输送物理率，C200为ASM完整图障碍，C204另加强到无正则性配对单调；C205–C207保零集子关系可导入指定cap/超线性/log原尾。完整图障碍不能当收敛不可导入；任意lift和一般统一涵盖仍未核。 |
| Pesquet–Roldán，[2608.22687v1](https://arxiv.org/abs/2608.22687v1)，首发2026-08-24；§3 p6–17、§4 p17–29、§5 p29–31相关定义、定理及证明 | Assumption3.1含全域cocoercive前向、solution-anchored comonotone、固定正定metric、满域单值warped inverse、总图闭与kernel/步长门。T3.10(i)弱收敛，(ii)正μ锚给唯一物理解及范数R-linear；T4.10为标准product归约 | [逐篇报告](comparisons/2026_08_gppa_nfb/nfb_review.md) 明列每个门；C201任意同空间拆分的必要原图二次锚，C203标准full-graph lift压缩，C202真实非单调算法重合。有限维weak=strong；物理几何点尾自动有限长。 |

[版本、附件、基线与哈希](comparisons/2026_08_gppa_nfb/BASELINE.md) 和 [综合定位](comparisons/2026_08_gppa_nfb/COMPARISON.md#positioning) 将paper fact、本库推导、有限计算及新颖性分开。任意kernel/拆分量词靠正文证明，不靠有限PASS。两篇收敛框架未给本库结构线同身份定理，不据此认证C03/C04/C18/C19/C20全球首创。

<a id="lit-refresh-2026-10-08"></a>
## LIT-REFRESH-2026-10-08 · 近期非单调近端、误差界与扩张比较

[定向刷新与逐项适用门](literature_refresh_2026_10_08.md#lr-scope) 固定 2026-10-08 截止、8–10 月主窗口及 7 月补查。核 GPPA v1 的 Theorems 2/4、NFB v1 的 Assumption 3.1 / Theorem 3.10、Spingarn 2025 v1 的局部 PPPA 接口及 2026-08-27 刊本日期、10/06 KKT v1 的指定推论、Ciosmak 7 月扩张的核心定理；9 月纤维稿仅核陈述，ORL HVP-EB 仅核出版社摘要 / 预览。

本库直接给 [C197 核坐标与物理点收敛边界](literature_refresh_2026_10_08.md#lr-gppa-physical)、[C198 Hölder参照与保距扩张门边界](literature_refresh_2026_10_08.md#lr-holder-reference)，另定位 GPPA v1 Example 1 的负内积。C193 只用于同一原图完整邻域的固定二次锚接口比较。新增外部比较义务，不升级外部全篇证明或项目新颖性；没有由此关闭总体规模、复合秩亏或全库来源覆盖门。

<a id="lit-selection-interfaces"></a>
## LIT-SELECTION-INTERFACES · 本轮固定版本与逐陈述定位

核验日期为 2026-10-05。完整对象边界和直接证书在
[选择文献接口](canonical/selection_literature_boundaries.md)；历史“已读全文”是独立的访问报告。

| 代号 | 实读的一手版本、编号与印页 | 当前准入边界 |
| --- | --- | --- |
| LTTQ | Luke–Thao–Tam, *Quantitative convergence analysis of iterated expansive, set-valued mappings*：[arXiv1605.05725v2](https://arxiv.org/abs/1605.05725v2)，实读PDF40页；2.15 pp.11–12、2.18 pp.14–15、2.19 pp.15–16；[正式PDF](https://pubsonline.informs.org/doi/epdf/10.1287/moor.2017.0898)，MOR43(4)(2018)1143–1176，分别2.1 pp.1152–1153、2.2 p.1155、2.3 p.1156 | 指定三条逐陈述跨号已核；固定锚和环域量词不替代全对 Hölder。非整篇逐字等同 |
| LTTP | Luke–Thao–Tam, *Implicit Error Bounds for Picard Iterations on Hilbert Spaces*：[Springer书目](https://link.springer.com/article/10.1007/s10013-018-0279-x)，VJM46(2018)243–258；[Nguyen H. Thao作者上传全文](https://www.researchgate.net/publication/323317906_Implicit_Error_Bounds_for_Picard_Iterations_on_Hilbert_Spaces)，2018-02-22公开上传、同DOI；Th1在线321–334、Th2 394–415、Remark1 455–522、Th4 902–917、Prop3 1188–1197行 | 作者 typeset全文已读；提取稿无正式印页，保留issue页码/版本对应门。Th4无非扩张前提，仅EB；一般φ率不升级独立证明 |
| LMZ | Li–Mordukhovich–Zhu, *Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods*：[v1](https://arxiv.org/abs/2406.13207v1)，实读33页PDF首页v1；BA p.7、4.3 pp.8–9、4.4 p.10、4.5/4.6 p.11；[正式DOI](https://pubsonline.informs.org/doi/10.1287/moor.2024.0570)于2026-04-07上线、Articles in Advance | v1指定内容门已闭，刊本编号/条件对应未闭。4.4确为实际点误差；4.6惩罚系数与标准步长互为倒数 |
| LP22 | Lee–Pham, *Openness, Hölder Metric Regularity, and Hölder Continuity Properties of Semialgebraic Set-Valued Maps*：[v2](https://arxiv.org/abs/2004.02188v2)，实读23页PDF首页v2；Def2.1 pp.5–6、Lem2.2 p.7、Th3.1 pp.12–14、Cor3.1 p.14、Prop3.1 pp.14–15；[正式DOI](https://epubs.siam.org/doi/10.1137/20M1331901)，SIOPT32(1)(2022)56–74 | 刊本书目已核，刊本逐条对应未闭。闭半代数图紧集EB不要求有限纤维；多值continuity按原文开逆像定义 |
| B93 | W.-J. Beyn, *On smoothness and invariance properties of the Gauss–Newton method*，NFAO14(5–6)(1993)503–514：[原刊扫描](https://scispace.com/pdf/on-smoothness-and-invariance-properties-of-the-gauss-newton-1ufiov541u.pdf)，[机构入口](https://pub.uni-bielefeld.de/download/1784250/2314357/OCT3780.pdf)当前防机器人；Th2.1/(2.1) p.505、Th2.2 p.507、Th3.1 pp.507–509 | 原刊数学接口已读；\(F\in C^k,G\in C^{k-1}\)只给极限\(C^{k-1}\)。共同尾须局部收小，不能授全流形常数 |
| P16 | P. Pasteczka, *Iterated quasi-arithmetic mean-type mappings*：[arXiv1412.2997v1](https://arxiv.org/abs/1412.2997v1)，实读13页；函数类p.3、Th1–2 p.4、Th3 p.5、§3.2 pp.6–7、Lem4.3–4.4 p.11；登记的刊本为Colloq.Math.144(2)(2016)215–228，DOI10.4064/cm6479-2-2016 | 指定v1内容已核；精确Th2/Th3分母式被C158独立解析证书阻断，安全共同双指数尾由SL3直接证明重建；刊本Th3.3精确式同受解析阻断，详见下方补核 |
| CHH | Chen–He–Huang, *Retractions by Alternating Projections*：[明确v2全文](https://arxiv.org/html/2605.17384v2)，PDF63页；Ass1 p.5、Ass2 p.14、Ass3 pp.20–21、Prop2 pp.19–20、Lem4.9 p.27、Th2 p.28、Th3 p.33 | 安全接口为紧局部切束域上的C1/C2；高p全C^{p−1}不能从指定证明补足，二阶回缩不是点误差Q2 |
| KR | Kvalheim–Revzen, *Reverse-engineering invariant manifolds with asymptotic phase*：[v1](https://arxiv.org/abs/1608.08442v1)，实读29页官方PDF；Prop1 pp.4–5/AppendixF p.25、§3.2.2 p.6、Prop6 pp.8–9、Prop8 pp.10–11、Th2 p.11/AppendixG p.28 | 相位对象及预设光滑相位已核；k1/k3支配阈值与L身份仍有具体未闭门，不能当成已证数值预算 |

arXiv未带版本PDF只在实际首页和登记页同时锁定版本后使用。
LMZ/LP22官方全文入口当前返回摘要/访问选项；不把摘要当成刊本定理。
上述有限陈述比较不认证“全球没有同类先例”。

**P16 刊本补核。** [IM PAN官方14页全文](https://www.impan.pl/shop/publication/transaction/download/product/91474)
为上述DOI，印刷215–228，线上2016-03-16。函数类p.218；
v1 Th1→刊本Th3.2、Th2→Th3.3均p.219，Lem4.3/4.4在p.224/p.225，
AGM→§5 pp.226–227。正式Th3.3保留同一分母精确式，C158的非恒定合法输入证书仍适用。
正式证明p.226更换代换链，不能沿用v1的特定证明批评；v1 Th3表示应用仍按v1引用。

<a id="lit-cox-1984"></a>
## LIT-COX-1984 · 正实数AGM积分接口

David A. Cox, *The Arithmetic-Geometric Mean of Gauss*，L’Enseignement Mathématique30(1984)275–330，
DOI10.5169/seals-53831。[官方§1分章PDF](https://www.e-periodica.ch/cntmng?bot=1&pid=ens-001%3A1984%3A30%3A%3A89)
由官方验证页公开的crawler链接取得，9数字化页（元数据页加原刊276–283）；
Th1.1 p.278及证明已读，条件 \(a\ge b>0\)、正平方根。
同一正实数AGM的椭圆积分身份已核；闭象限/零轴与坏模仍由C146–C148自证，
不把原定理外推至 \(b=0\)，不声称全56页逐命题审结。

<a id="lit-phase-candidates"></a>
## LIT-PHASE-CANDIDATES · 周期相位入口与当前访问范围

Chicone–Liu, *Asymptotic phase revisited*，JDE204(1)(2004)227–246，
DOI10.1016/j.jde.2004.03.011。[Missouri作者目录](https://math.missouri.edu/people/emeritus/chicone)
列Revised12/23/03；[作者公开上传原作](https://www.academia.edu/8166140/Asymptotic_phase_revisited)
为2003-12-23、22页手稿，定义p.2、Th2.5 p.5、Th2.8 p.10、Th3.1 p.14、
Ex1 p.18、Prop3.6 p.19已读。对象是随周期轨道运动的相位，不是静止点极限。
刊本逐号对应仍未闭；Th2.8声明C2却使用三阶大O Taylor余项的证明步骤，
须刊本或独立证明另闭，不判定理错误。

Battelli–Palmer, *Smoothness of Asymptotic Phase Revisited*：
[作者机构条目](https://iris.univpm.it/handle/11566/64420)列ANS11(4)(2011)837–851，
摘要指hyperbolic periodic solution稳定流形上的相位，文件栏明确无关联文件。
正式/作者全文及定理号、精确正则条件未取得；只授书目/摘要身份，不从摘要补定理。
这两个入口不能机械移成SS静态选择映射，更不构成全球阴性优先权证明。

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
| pp.16–17，Proposition 5.4 / Example 5.5 | \(\ell^2\) 上对角 \(1/n\) 与成对斜旋转的**和**：严格且极大单调、paramonotone、非 rectangular | Example 5.7 |

Prop5.4 的一般构造另要求反身空间、连续线性单调 A/B、A paramonotone 且值域稠密真、B 双射且 skew；本项目不把这些前提删除。

**项目身份。** 分别对应 GX-058、GX-060/061、GX-059；这些例卡的结论已有
直接规范证明。Proposition 5.1 不是非线性、多值或受限图的无条件接口。
此核验关闭列出的原文归属和编号，不认证例卡后来增加的锐 RL、残差或路径结果，
也不判定本项目新颖性。不能把作者站稿编号直接拼到 v1 引用上。
最后一行作者稿的跨号只核 Example 5.7，不宣称一般 Proposition 5.4 的作者稿对应号已核。

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
§3 和参考文献 [38] 本身只给 Spingarn 的二手定位；本次另取得
[1980完整作者稿及1981作者报告](canonical/spingarn_author_definitions.md#sp-versions)，
已核一阶定义与极大性对象。两正式刊本正文仍受访问门阻挡，不能混称相同版本。

本次进一步核正式版 Proposition1 p.3、Proposition4 p.5、Example2 p.8、
Lemma2 pp.9–10、Assumption2 p.10、Theorem2 pp.10–11。
指定印刷事实及有效导入的四项边界在
[SL-LT](canonical/selection_literature_boundaries.md#sl-lt)；其中收敛定理的导入仍有具体待证门，
不因正文可读就授予完整算法认证。

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

**Paper fact.** L. Górniewicz and D. Rozpłoch-Nowakowska, “The Lefschetz Fixed Point Theory for Morphisms in Topological Vector Spaces,” *Topological Methods in Nonlinear Analysis* **20** (2002), 315–333, [期刊原版 PDF](https://www.tmna.ncu.pl/static/files/v20n2-07.pdf), DOI [10.12775/TMNA.2002.039](https://doi.org/10.12775/TMNA.2002.039). 该文印刷页 327 的 Theorem 6.2：若 \(X\) 是 Klee-admissible 拓扑向量空间 \(E\) 中某个开集的 retract，且 \(\varphi\in M(X,X)\) 属于 \(CAC(X)\)，则其 Lefschetz 数有定义；若数不为零，\(\varphi\) 有固定点。印刷页 315–318 的 Definitions 1.1、2.1–2.3 及印刷 p.319 的 Theorem 2.4 把 morphism 表示为 \(X\xleftarrow{p}\Gamma\xrightarrow{q}X\)：\(p\) 是 perfect surjection 且每个纤维在**有理 Čech homology with compact carriers** 下 acyclic，\(q\) 连续。印刷页 320–322 的 Definition 2.6、3.1 与紧类包含关系 \(K(X)\subset CAC(X)\) 表明紧 morphism 足以满足 Theorem 6.2 的动力条件。此定理本身不要求 morphism 的输出纤维 acyclic。

**Vietoris–Begle 精确接口（2026-10-05）。** 同文 p.316 Theorem 1.2 明确保证 Definition 1.1 的 Vietoris 映射在带紧载体的有理 Čech 同调上诱导同构。紧纤维的上同调假设经原引 [15] Górniewicz 1976 I.§1 Theorem (1.1)（p.8）的自然对偶及 I.§3（p.12）的紧载体识别转为该同调条件；是同调等于上同调代数对偶的方向，不把无限维空间与双对偶识别。原始 PDF、页码及 C05-v2 每项图条件见[完整导入卡](audit/VIETORIS_IMPORT.md)。

**Interpretation / C05-v1 import check (2026-10-01).** 对 [9/25 候选稿 §8, Theorem 8.1](../history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)，取 \(X=A\subset\mathbb R^n\)，\(\Gamma=\{(p,y):p\in A,y\in T(p)\}\)，\(p=\pi(p,y)\)，\(q=e_h(p,y)=y+\lambda h(y)\)。逐项门如下：

| 引文前提 | 稿件中对应的**额外假设或推导** |
| --- | --- |
| \(E\) Klee-admissible，\(X\) 为开集 retract | \(E=\mathbb R^n\)；\(A\) 是紧有限多面体，故是 Euclidean neighborhood retract。 |
| \(p\) Vietoris，\(q\) 连续 | \(A\) 紧、\(T\) 在邻域 usc、非空紧值，给紧图与 perfect surjection；\(T(p)\) 的有理 Čech acyclicity 给纤维条件。\(h\) 连续给 \(e_h\) 连续。注意原稿用 Čech **cohomology** 描述 acyclicity，需采用其对紧度量纤维的有理 homology 等价。 |
| \(q(\Gamma)\subset A\)，紧 morphism \(\subset CAC(A)\) | 原稿 (8.4) 的完整 shell/collar 和 (8.7) 保证每个 \(y\in T(p)\) 离 \(A^c\) 至少 \(m-\alpha\)；\(\sup_A\|h\|<(m-\alpha)/\lambda\) 故 \(e_h(\Gamma)\subset\operatorname{int}A\)。紧 \(\Gamma\) 的连续像紧，按原文 \(K(A)\subset CAC(A)\)。 |
| 非零 Lefschetz 数 | 原稿要求 \(b^*:H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 全阶满射，并用 \([p,y]\subset B\) 得 \(e^*=\pi^*\)；\(e_{th}\) 全在 \(A\) 中，同伦不改诱导映射。有限多面体上的有理同调与上同调维数有限，因此 \(\Lambda=\chi(A)\ne0\)。 |

**审查结论与边界。** 原引文确实适用于上述**紧 span**，不需要另证明非线性像 \(e_h(T(p))\) acyclic。这里关闭的是“[6, Theorem 6.2] 是否有 CAC/图/回缩适用门”这一个导入问题。原稿整条 C05-v1 仍是候选：有限观测不能证明整窗 (8.1)–(8.2)、\(T\) 的存在、usc 与 acyclicity，也没有逐行 referee 其余数值包络或核外部先行性。若换成非紧 \(A\)、放弃全部纤维 acyclicity、或只凭有限样本声称整窗条件，就不再是同一导入。稿件的 Čech cohomology/homology 等价是单独的标准拓扑事实，本次只在紧度量纤维范围使用，没有把它扩张到任意空间。 同一导入门在保留整窗与拓扑假设、仅改 q>0 的 [C05-v2](canonical/local_range_without_supercriticality.md#lr-theorem) 中亦适用；这项新版本不是该论文或 9/25 原稿的陈述。


<a id="lit-common-tail"></a>
## LIT-COMMON-TAIL · Lipschitz 前缀加共同尾的一手先例

**Paper facts。** Wiśnicki 的 [arXiv:1204.6464v2](https://arxiv.org/abs/1204.6464v2) 预印本 Lemma 1（PDF pp.2–3），对应 [正式 TMNA 43 (2014) 原文](https://www.tmna.ncu.pl/static/published/2014/v43n1-06.pdf) 印刷 p.91 Lemma 2.1：完备有界度量空间、k-Lipschitz 自映射、全初值共同几何增量，给 Hölder 极限；证明使用有限前缀加两条共同尾。[Pérez García–Fetter 2010 正式 PDF](https://journals.umcs.pl/a/article/download/3985/2887) 印刷 pp.38–40 Lemma 2.1，特别(c)，对连续T和p-Lipschitz辅助u、ST5全部点约束给uⁿ的极限回缩；p>1的幂指数是log(1/A)/(log p+log(1/A))，要求有限直径。

**项目接口。** [C149 的 ST1–6](canonical/selection_truncation_prior_tools.md#st-lipschitz) 独立写出量词、指数和辅助对象；本页无界版是本项目证明，非原引理删条件。已核引理未陈述指定 Hölder 单步的两种非幂包络；一般先行性及转引 BL00 Proposition 1.10 的原页仍未核。

<a id="lit-brent-1976"></a>
## LIT-BRENT-1976 · AGM 与椭圆积分的精确接口

**Paper fact。** Richard P. Brent, *Fast Multiple-Precision Evaluation of Elementary Functions*，Journal of the ACM 23 (1976), 242–251，[作者站原文](https://maths-people.anu.edu.au/~brent/pd/rpb034.pdf)，[DOI](https://doi.org/10.1145/321941.321944)。印刷 pp.245–246，(4.16)–(4.18)：a₀=1、b₀=cosφ>0的算术–几何平均递推极限为π/[2F(φ)]，其中F是原页第一类椭圆积分。

**项目接口。** [AGM13–14](topics/examples/arithmetic_geometric_mean.md#agm-selection) 取cosφ=ε并逐步估计积分得π/[2log(1/ε)]；积分渐近是项目推导。非任意 Hölder、非半代数及严格兼容障碍由递推自足证明；该积分系数是补充。Cox指定Th1.1原页已核，见[LIT-COX-1984](#lit-cox-1984)。

<a id="lit-bmw-2019"></a>
## LIT-BMW-2019 · 逆图编码的自然输入域

**Paper fact。** Bauschke–Moursi–Wang, *Generalized monotone operators and their averaged resolvents*，[arXiv:1902.09827v1](https://arxiv.org/abs/1902.09827v1)，[v1 PDF](https://arxiv.org/pdf/1902.09827v1)，2019-02-26，Fact 2.1，印刷 pp.3–4：非空D⊂H、单值T:D→H，A=T⁻¹−I给J_A=T，故自然输入域恰D。

**项目接口。** C146直接证明该关系身份。AGM的D输入在其本页记P，输出域记D，引用时重绑定；Fact2.1附带单调/firm等价条件不自动授给AGM。

<a id="lit-c11-m1-fixed"></a>
## C11/M1的固定比较范围

[逐来源范围](audit/C11_M1_SOURCE_SCOPES.md#cm-scope)及[16张一手卡](canonical/c11_m1_literature_interfaces.md)
给出版本、位置和必要门。原句宽paper-facts按专表收紧；不把旧“已查”标签当本次访问证明。
以下事实不授予新项目Claim或全球先行性结论。

| 固定文献组 | 本次核到的接口 | 保留门 |
| --- | --- | --- |
| BAP v1、WX v1、LPQ v4、LDZ v2、WANG v1、MA v1、LP 2024 | 分别核实际二阶目标、可识别流形EB、特殊二阶目标的假定EB/近端Newton、弱凸同level转换、uniformized level-set三条件、可行域增长及特殊目标KL+growth EB | \(\Theta_2\)、argmin、level set、特殊 \(X^*\) 不自动同一；ordinary \(\partial\) 真残差与prox residual不自动同一；完整原生数据验证及刊本/精确公式另核 |
| LW官方2026-02-11 | GE和resolvent residual的setup及假定Hölder EB | 各弱Jacobian速率定理的全部门尚未读完 |
| BLL正式2022、KLAN作者2019-04-28、FM指定PDF、LTT v2、DJL v1 | 分别核有限composition的共同Fix门、gauge迭代可和门、Fejér+modulus及额外gap终止门、连续paracontraction有限family、LTT有限violation/patch定理、DJL具体reflector patch与 \(\theta\) 迭代条件 | 原生M1/投影/RAAR的完整选择、实际前缀和目标身份另证；部分具体应用全文门仍未闭 |
| GAO、DTT v1、TT | 官方元数据/摘要主题，访问程度逐卡记录 | 定义、定理量词/方向、gauge、共同尾及精确非覆盖均deferred；不凭摘要写正文阴性 |

<a id="lit-selection-primary"></a>
## LIT-SELECTION-PRIMARY · LP22 / LMZ / P16 指定接口

[一手逐条卡](canonical/selection_primary_interfaces.md) 给准确版本与页码。LP22 arXiv2004.02188v2 Lemma2.2 为非零一元半代数函数的有理幂主项；正系数与正指数需应用中另有正性及趋零。Prop3.1/Th3.1/Cor3.1 是有限维闭半代数关系的存在性正则接口，不给指定图数值常数或严格兼容，也不证明无穷迭代极限半代数；SIAM书目已核，刊本文字/数学跨号未穷尽。

LMZ arXiv2406.13207v1 4.3 的有限长框架与 4.4 的实际点率分开。Example4.6 原初值1、目标 |t|^(3/2)+λ_L(t−t_k)²/2，其项目步长 h=1/λ_L；全实初值唯一完整近端到0及恒定选择由本库直接证明，不能归作原例量词。正式版差异仍未闭。

P16 v1 Theorems1–2对应正式版Theorems3.2–3.3；指定负起步公式在小非零直径有[解析反例 F44](../FAILED_ROUTES.md#f44)，原读取状态与数学验收分开。[C160](canonical/selection_quasi_arithmetic_boundary.md#qa-uniform-tail) 用非负N独立修复共同尾，并独立证明同域两初值Lipschitz界。v1 Theorem3的φ段不归给无对应段的刊本；既不授予任意粗糙M，也不关闭全篇版本差异及全球优先权。
<a id="lit-mt-category"></a>
## LIT-MT-CATEGORY · 类别转移的准确导入

Julien Melleray / Todor Tsankov，*Generic representations of abelian groups and extreme amenability*，[作者PDF](https://math.univ-lyon1.fr/~melleray/ext-amenability.pdf)，Appendix A、印刷p.25（PDF第25页）；2026-10-06核原页及证明。Proposition A.3给连续Polish映射的非空开像非第一纲判据；Theorem A.5还要求比较集合Baire可测，给母空间余稀与余稀参数下的纤维余稀等价。准确量词和项目逐项适用门见[规范接口](canonical/operator_space_construction_frontier.md#ocf-category-import)。

**边界**：外部定理不认证特定尾/反射模观测的保纲性。此核验不证明来源当年的访问行为，不等同于另一Melleray Theorem2.9版本核验，也不产生项目新颖性结论。

<a id="lit-oai-catalog-2026"></a>
## LIT-OAI-CATALOG-2026 · 外部目录与 PPA 的六个候选接口

**来源与实读范围。** 目录 *OpenAI Research Catalog*，2026-10-06，41页、372组结果、722稿件；本次扫描全目录并目读pp.35–36，另从公开仓库取得下面六份原稿及其TeX。固定外部仓库版本为 [`adc7f1241b42e322a6451854ab7e4b4c146bf78a`](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a)，核验日期2026-10-07 UTC。目录与原稿分开：条目编号不是定理编号。

**证据层与后续接收范围。** 初筛基线为 `ac68013`，六项陈述定位由 `2a5030e` 固定。2026-10-07后续已完整读332的构建TeX，并在[C181](canonical/l1_markov_extension.md#lm-proof)独立重构其实数平稳链主结论；C182再与下方Mendel–Naor一手接口合取。其余五稿仍仅是 `source-report` / 待核工具；332的复数推论、Lean实际覆盖及全部稿件未升级。选定证明的接收不改变C02/C03/C04/C11/C179/C180身份，也不代表外部全部结果或全球先行性验收。

### 332 · ℓ¹ 的 metric Markov cotype 与目标扩张

- **Paper fact / exact identity**：[2026-10-05原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/l1-markov-cotype.pdf)，9页。Definition1.1/Theorem1.2 p.1声称：对每个有限可逆随机矩阵A、其可逆概率向量π、整数t≥1及每组xᵢ∈ℓ¹，存在yᵢ∈ℓ¹，使
  \[
  \sum_i\pi_i\|x_i-y_i\|_1^2+t\sum_{i,j}\pi_i a_{ij}\|y_i-y_j\|_1^2
  \le3024\sum_{i,j}\pi_i\left(\frac1t\sum_{s=1}^t A^s\right)_{ij}\|x_i-x_j\|_1^2.
  \]
  Corollary6.2 p.9声称：存在统一K<∞，对每个实Hilbert H、子集D⊂H和Lipschitz f:D→ℓ¹，存在扩张f̂:H→ℓ¹，Lip(f̂)≤K Lip(f)。p.2/§6明确区分允许自由选择yᵢ的metric条件和指定线性平均的更强条件。
- **Proof receipt / exact version**：完整读取同一固定提交下[build/main.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/build/main.tex)，648行，SHA256 `656a6f35bf6543ecf0cf2dbc38a83a7a05427592123a5eb817be24250e2e6953`。C181完整重构二元编码、四次余量108、停止鞅及几何/Cesàro比较28；仅用平稳πA=π，非可逆范围原Remark5.1已有。C182的Hilbert Hölder扩张、任意度量源γ≤1/2扩张、显式概率回缩及ℓ¹预算放宽完成均在[规范正文](canonical/l1_markov_extension.md)逐项证明；非原稿新颖性主张。
- **Boundaries**：常数为KL，不能证明原(λ,L,γ)图极大必满域。原平滑点不保证在数据子空间；概率值域可由本库显式2-Lipschitz回缩保持但另损常数，固定边缘/不变律不随之保持。metric Markov cotype不是同步OT残差Ψ、条件残差或law-step误差界。复数与形式化覆盖仍未核。

### 328 · 反身Banach中的不动点与非扩张回缩

- **Paper fact / exact identity**：[2026-09-24原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/paper.pdf)，19页。Theorem1.1 p.1声称：每个实反身Banach X、非空范数闭有界凸C⊂X、原范数下每个非扩张自映射T:C→C有不动点。Corollary1.2同页声称：任意两两交换的此类映射族有非空共同固定集，并存在C到该集的非扩张回缩；证明明确另导入Bruck定理。已读pp.1–3的陈述、推论及证明路线，未审其全部关键引理。
- **Interpretation**：与[C11的一致极限回缩](canonical/general_modulus_dynamics.md)有对象接点，可作为Banach推广的候选工具。Hilbert非扩张固定点存在已有经典接口，本稿的扩大范围是任意给定范数的反身Banach。
- **Boundary / independent check**：存在一个回缩不说明它等于lim Tⁿ，也不给真实残差EB、轨道有限长或RLEB兼容。T=−I在实Hilbert闭单位球上非扩张且FixT={0}，非零轨道为二周期；对应完整关系F=−2I/λ的J_{λF}=−I。这直接阻断“固定点存在⇒完整PPA点收敛”的替换。一般Hölder–RL图的T=(I+C)/2也未必非扩张；闭凸不变域另证。优先核原稿adaptive-anchor/tree/switching承重引理及Bruck适用门。

### 098 · doubling不能认证有限维双Lipschitz表示

- **Paper fact / exact identity**：[2026-09-25原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf)，13页。Theorem1 p.2声称存在ℓ²子集S，doubling常数≤76800，对每个有限目标维数和每个有限失真均无Euclidean双Lipschitz嵌入。§7 Corollary6 pp.10–12另声称：存在统一Λ，每个无限维实Banach B中都有一个紧Λ-doubling K_B，对全部有限维实赋范目标均无任何有限失真的双Lipschitz嵌入。已读pp.1–2及§7，不视为完整基础障碍证明验收。
- **Interpretation / scope**：可用于攻击把有限覆盖复杂度当作有限维坐标认证的路线，与[C04有限维必要性](canonical/finite_fiber_classification.md#ff-object)、[C20实际参数覆盖](canonical/finite_data_proxy.md)相关。doubling不是紧性，更不是有限维假设的替代。
- **Obligations**：先审原稿§2–5的核心构造与导数障碍。即使命题可靠，也不否定有限样本近似、允许失真随尺度变化的表示、雪花表示或特定RL图的额外结构；不自动给C04无限维纤维反例。

### 329 · 对偶化不保证统一覆盖熵常数

- **Paper fact / exact identity**：[2026-09-24原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/main.pdf)，15页。Theorem1.1 p.1声称：对每个a,b≥1，存在维数n及原点对称凸体K⊂ℝⁿ，令L=[−1,1]ⁿ，有log N(K,L)>b log N(L° ,a⁻¹K°)。N为任意平移的覆盖数，凸体紧且内部非空，°为线性极体。已读pp.1–2及定理身份，未验收构造证明。
- **Interpretation / scope**：若以后以覆盖熵比较正反表示或认证类的复杂度，这是“维数统一常数不能凭对偶直觉给出”的待核障碍。它不是[RLEB–LT总体类别比较](canonical/operator_space_construction_frontier.md)的答案：极体不同于F⁻¹，覆盖数不同于Baire纲、孔隙性或prevalence，母空间和图编码仍另证。原稿还明确不声称固定维数反例。

### 327 / 324 · Banach几何与换表示的次级接口

- **327 paper fact**：[2026-09-23原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf)，14页，Theorem1.1 p.1声称每个对至少一个p>1有Markov type p的实Banach空间均superreflexive，即可等价一致凸重赋范。Markov type量化全部有限平稳可逆链、全部链状态到空间的映射及全部整数时刻。已读pp.1–2；完整证明未审。**Interpretation**：是Banach随机几何的候选约束，不能由一个指定核的收缩或同步Ψ误差界得到该空间性质；等价范数也不保持本库的原常数或Hilbert平行四边形恒等式。
- **324 paper fact**：[2026-09-24原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf)，23页，Theorem1.1 p.1声称存在全局双Lipschitz等价而不线性同构的可分实Banach X,Y。已读pp.1–2的身份，未审完整构造。**Interpretation**：与[完整图共轭义务](canonical/operator_space_construction_frontier.md#ocf-specification)相邻，但具体共轭保EB、零集、尾界和单调性须独立认证；本结果不证明任意某个共轭破坏这些性质，也不替代保纲桥。

**当前决策。** 332已接成C181/C182的具体工具；328的非扩张前提不能由一般Hölder图补出，[C183](canonical/infinite_fiber_boundary.md#if-counterexample)甚至给单点零集但空纤维，另由Hilbert自足证明C184得到额外非扩张下的弱紧补救，未调用328的一般Banach定理。098/329在实际表示/量尺路线被采用时再审，327/324仍次级。筛查与接入范围没有直接关闭自然完整母空间中的总体比较，也没有替代C02-v2全部局部门；不证明全球无先例或722稿件均已审完。

<a id="lit-mn-extension"></a>
## LIT-MN-EXTENSION · metric Markov cotype到全域扩张

**Primary paper fact。** Manor Mendel and Assaf Naor, *Spectral calculus and Lipschitz extension for barycentric metric spaces*, 以下固定作者公开原稿版本；已读作者[53页公开原稿](https://web.math.princeton.edu/~naor/homepage%20files/cat0-extension.pdf) Theorem1.11（PDF p.8）、Corollary1.13（PDF p.10）及p.11的snowflake说明，核验2026-10-07。Theorem1.11对p,Γ≥1、Markov type p源、metric Markov cotype p且W_p-barycentric常数Γ目标，给任意子集映射到任意有限输入集的扩张，Lip≤cΓM_pN_p。Corollary1.13在目标为对偶Banach时给全源扩张e(X,Y)≤cM_pN_p，c为统一绝对常数。p.11同时明确α-snowflake具有常数1的Markov type p，范围1<p≤1/α。

**Exact import / all gates。** 常数平方归一化及重心量词见[LM-MN-DEFINITIONS](canonical/l1_markov_extension.md#lm-mn-definitions)。C182取p=2、Y=ℓ¹(ℝ)=c₀*；均值重心由Jensen及任意耦合给W₂常数1，C181给N₂≤12√21。Hilbert源M₂=1；其0<γ<1雪花由HE-SNOWFLAKE等距嵌入Hilbert，γ=1直接用Hilbert。任意度量源在γ≤1/2用路径三角及2γ≤1独立给M₂≤1。子集任意、目标为完整ℓ¹而非任意闭子空间、弱星紧性所需对偶身份明确，故满足Corollary1.13的全部条件。此处使用存在统一K而非估计最优K。

**Boundary。** 该文Theorem1.14给某个ℓ¹闭线性子空间缺少所有metric Markov cotype，是关于子空间自身的目标性质；C181中自由平滑点可离开子空间，不与之矛盾。本接口不提供概率值域、EB、守恒边缘或同常数Cayley完成；这些须分别证明，C182仅提供明确损失常数的部分。
