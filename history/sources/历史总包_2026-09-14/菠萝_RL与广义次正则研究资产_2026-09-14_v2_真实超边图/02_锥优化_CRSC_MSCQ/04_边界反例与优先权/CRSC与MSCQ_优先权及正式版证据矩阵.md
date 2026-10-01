# CRSC–MSCQ：有界先行性证据矩阵

项目：RL-CONIC-2026；论文类型：theoretical；阶段：T4；任务：LIT-PRIORITY。核验日：2026-09-09（UTC）。

## 1. Scope and inputs

目的：核对 frozen minimal-face CRSC 对 nice/amenable 锥的局部非线性面约化、原锥残差 MSCQ 与边界刻画，尤其排查 DOI 10.1007/s10107-025-02237-w 的最终版是否直接覆盖。本报告是有界最近邻与版本核验，不是系统综述、数学正确性认证或全球优先权证明；没有修改主稿或推进阶段。

已完整读取当前工作区中的三个输入：

- `output/JOURNAL_PRIORITY_AUDIT_GENERAL_AMENABLE_CRSC_MSCQ.md`
- `output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md`
- `output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md`

输入中的证明与独立审计属于 `VERIFIED_USER_MATERIAL`：仅表示确实读到了这些材料，不将其中的“PROVED/PASS”转成外部文献认证。

固定比较对象：有限维 Euclidean 空间、proper 闭凸锥 C、C1 映射 G、G(x̄)=0，A=DG(x̄)，F=minFace(Im A∩C)。CRSC 包含 A*C* 闭，以及冻结 F 后 rank(DG(x)*|F⊥) 在整个开放输入邻域恒定。目标 MSCQ 是 d(x,G⁻¹(C))≤κd(G(x),C)，不是仅面残差误差界，也不是 Hölder 误差界。

| 概念块 | 检索词与必须区分的近义项 |
|---|---|
| CQ | CRSC；constant rank of the subspace component；CRCQ；facial constant rank；minimal face |
| 锥几何 | amenable cones；nice cones；facially dual complete；conjugate face |
| 正则性 | metric subregularity；MSCQ；local error bound；Lipschitz/Hölder error bound |
| 约化 | facial reduction；nonlinear conic；A1/A2；cone reducibility |
| 误匹配控制 | Lourenço 的 cone amenability ≠ fully amenable composite；arbitrary C1 ≠ cone-concave；apex derivative constant ≠ 任意非顶点 reduction derivative constant |

检索对象为优化与凸锥几何的理论论文、作者稿、正式期刊页与 arXiv/Optimization Online 原始记录；不设语种或发表年过滤，重点回查 2025–2026 更新。只用平台原生搜索与普通原始/官方网页，没有第三方 API、机构凭据、自动数据库导出或绕过付费墙。

## 2. Specialist findings：结论与门禁

`PROVISIONAL / REPAIR`。本次可读原文中，未识别到直接包含“任意 C1 + 冻结 minimal-face CRSC + amenable cone ⇒ 原残差 MSCQ”完整假设—结论组合的定理。但这只是 `AI_INFERENCE` 的有界非覆盖判断，不等于“首次”已证实。

最重要的未闭合项没有改变：**minimal-face 论文的正式最终正文未取得，不能确认它是否保留 A1/A2，也不能排除最终修订增添了本稿主定理。** 当前官方页明确只提供订阅预览；不得以摘要、脚注、引用或作者旧稿替代最终正文逐定理比对。[Springer 正式记录](https://link.springer.com/article/10.1007/s10107-025-02237-w)

本次新增的可靠信息主要是版本与比较精度：arXiv 的最新可见版本比作者页稿更早；C-CRSC 的 2026 正式开放全文已核验，仍是标量 NLP；另纳入 Scott 的 joint supporting subspace 稿作凸模型近邻，未把它错当非线性 CRSC–MSCQ 定理。

### 2.1 目标 DOI 的版本证据

| 版本 | 已核实的内容 | 未核实内容 / 处理 |
|---|---|---|
| VOR：2025-05-24；MP 215 (2026), 743–769；Series A，Full Length Paper | `VERIFIED_SOURCE`：作者 Roberto Andreani、Gabriel Haeser、Leonardo M. Mito、Héctor Ramírez；接受日 2025-05-04；公开脚注说明二阶之外部分只需 C1。[官方页](https://link.springer.com/article/10.1007/s10107-025-02237-w) | 正文为 subscription preview；SharedIt 未提供链接；最终定义、命题、定理、开放问题段仍 `PENDING_VERIFICATION`。 |
| 作者页：2025-03-20 修订，19 页 | `VERIFIED_SOURCE`：p.7 Definition 3.2；pp.14–15 Proposition 5.2；p.15 Theorems 5.1–5.2 与紧接其后的开放问题。[作者稿](https://www.ime.usp.br/~ghaeser/crsc-redcones.pdf) | 这不是已经确认与 VOR 逐字相同的 accepted/final manuscript。 |
| arXiv:2304.13881v2，2024-11-30 | `VERIFIED_SOURCE`：当前记录只列 v1=2023-04-26、v2=2024-11-30。[版本记录](https://arxiv.org/abs/2304.13881) | 早于作者页稿，不用它冒充最终版本；未进行全文逐行版本差分。 |

公开作者稿的精确比较摘要：Definition 3.2 的 F 在参考点冻结并包含参考闭像；Proposition 5.2 要求共轭面相对内点核乘子与共轭面 span 的邻域恒秩；Theorem 5.2 仍加入 A1（邻域闭像）、A2（邻域 minimal-face 稳定），并把删除这两项列为开放问题。上述定位仅属于该作者稿，**不能自动套用正式页码**。[作者稿](https://www.ime.usp.br/~ghaeser/crsc-redcones.pdf)

从输入证明出发的 `AI_INFERENCE`：固定 S=span(C*∩F⊥)⊂H=F⊥ 后，参考闭像给 rank(A*|S)=rank(A*|H)，连续最大非零子式与 CRSC 给邻域秩夹逼。因此本稿 FR 与已有 Proposition 5.2 的距离很短；应承认这一依赖，不将 FR、秩夹逼和 A1/A2 当作三个完全独立的深机制。该推断不替代最终版核验。

## 3. 原始来源与纳入理由

状态用法：`VERIFIED_SOURCE` 表示相应原文或官方记录实际可读并已核对；`PENDING_VERIFICATION` 表示尚未达到所需版本/全文层级；`AI_INFERENCE` 用于“能否直接覆盖”的跨论文比较。相关性使用“精确同方向 / 同领域近似 / 仅作类型示例”；本任务不是 AI 应用选题，故不强套 AI-application 分类。

| ID | 经核对的文献身份与版本 | 内容定位 / 访问层级 | 纳入理由与相关性 |
|---|---|---|---|
| M01 | Andreani–Haeser–Mito–Ramírez, *A minimal face constant rank constraint qualification for reducible conic programming*. MP 215, 743–769 (2026), DOI 10.1007/s10107-025-02237-w；作者稿修订 2025-03-20 | 定理层作者稿；最终仅公开记录，见 §2.1 | 精确同方向；最直接优先权门禁。 |
| M02 | Gábor Pataki, *On the Closedness of the Linear Image of a Closed Convex Cone*. MOR 32(2), 395–412 (2007), DOI 10.1287/moor.1060.0242 | `VERIFIED_SOURCE`：[原始全文](https://optimization-online.org/wp-content/uploads/2006/12/1556.pdf) Theorem 1.1；[官方题录](https://pubsonline.informs.org/doi/10.1287/moor.1060.0242) | 同领域近似 / 进口工具：closed image 与 conjugate-face 像等价在所需 nice 条件下成立；不是本稿新闭像准则。 |
| M03 | Bruno F. Lourenço, *Amenable cones: error bounds without constraint qualifications*. MP 186, 1–48 (2021), DOI 10.1007/s10107-019-01439-3；online 2019-11-07；仓库更新 2019-08-09 | `VERIFIED_SOURCE`：[作者全文](https://optimization-online.org/wp-content/uploads/2017/11/6348.pdf) Definition 8，Propositions 9,11–13,33；[正式记录](https://link.springer.com/article/10.1007/s10107-019-01439-3) | 同领域近似 / 进口工具：面误差界、amenable⇒nice、类与乘积性质；Prop.12 已给面 amenability 与 apex subtransversality/线性正则性等价。 |
| M04 | Bruno F. Lourenço–Vera Roshchina–James Saunderson, *Amenable Cones Are Particularly Nice*. SIOPT 32(3), 2347–2375 (2022), DOI 10.1137/20M138466X；电子发表 2022-09-22 | `VERIFIED_SOURCE`：[作者提供正式排版全文](https://bflourenco.github.io/papers/amenable_nice.pdf)，Prop.3.2（p.2352），§5、Props.5.1–5.2、Thm.5.3（p.2365） | 精确同方向的锥几何边界：四维 nice 非 amenable 锥已存在；面正则性等价已有。 |
| M05 | Nguyen Huy Chieu–Nguyen Thi Quynh Trang–Nguyen Thi Hai Yen, *Revisiting the Constant-Rank Constraint Qualification for Second-Order Cone Programs*. arXiv:2604.00365v1，2026-04-01 | `VERIFIED_SOURCE`：[全文](https://arxiv.org/html/2604.00365v1) §2 CQ、(3.1)、Theorem 5.1；[版本页](https://arxiv.org/abs/2604.00365) 当前仅 v1，无已核验期刊 DOI | 精确同方向但范围窄：仿射 single-SOC CRCQ⇔MSCQ；还纠正非顶点自然约化后 FCR 自动成立的误读。 |
| M06 | Nguyen Quang Huy–Nguyen Huy Hung–Nguyen Van Tuyen–Hoang Ngoc Tuan, *Error Bounds for a Class of Cone-Convex Inclusion Problems*. arXiv:2502.04716v1，2025-02-07 | `VERIFIED_SOURCE`：[全文](https://arxiv.org/html/2502.04716v1) Theorem 4.1；[版本页](https://arxiv.org/abs/2502.04716) 当前仅 v1；未核验期刊发表 | 精确同方向的 EB 近邻：smooth cone、C1 且 K-concave、邻域 ACQ。 |
| M07 | Ying Lin–Tianxiang Liu–Bruno F. Lourenço, *Facial reduction for nice (and non-nice) convex programs*. 稿日 2025-12-17，仓库发布 2025-12-18 | `VERIFIED_SOURCE`：[58页全文](https://optimization-online.org/wp-content/uploads/2025/12/cfr.pdf) 摘要、引言模型；[仓库记录](https://optimization-online.org/2025/12/facial-reduction-for-nice-and-non-nice-convex-programs/) | 同领域近似：两凸集交、两闭真凸函数、恢复强对偶；不是任意 C1 非凸逆像模型。 |
| M08 | Mitsuhiro Nishijima–Guoyin Li–Bruno F. Lourenço, *Radial-type error bounds for semidefinite feasibility problems without strict feasibility: qualitative estimates and asymptotic tightness*. arXiv:2608.09013v2，2026-08-28（v1 2026-08-10） | `VERIFIED_SOURCE`：[全文](https://arxiv.org/html/2608.09013v2) 摘要与 §1 模型；[版本记录](https://arxiv.org/abs/2608.09013)；未逐定理审计 | 同领域近似：affine-space/PSD feasibility 与径向 Hölder EB，非一般非线性 CRSC。 |
| M09 | Scott B. Lindstrom–Bruno F. Lourenço–Ting Kei Pong, *Error bounds, facial residual functions and applications to the exponential cone*. MP 200, 229–278 (2023), DOI 10.1007/s10107-022-01883-8；online 2022-10-13 | `VERIFIED_SOURCE`：[正式开放全文](https://link.springer.com/article/10.1007/s10107-022-01883-8)，§1 (Feas)、Definition 2.1、§3 / Thm.3.8 | 同领域近似：仿射锥可行性、FRF、非 Lipschitz 模数；框架宽并不意味着本题指数 1 或输入纠偏自动成立。 |
| M10 | Roberto Andreani–Mariana da Rosa–Leonardo D. Secchin, *A New Constant-Rank-Type Condition Related to MFCQ and Local Error Bounds*. JOTA 209, article 21 (2026), DOI 10.1007/s10957-026-02965-9；VOR 2026-03-26 | `VERIFIED_SOURCE`：[正式开放全文](https://link.springer.com/article/10.1007/s10957-026-02965-9) §1 (NLP)；[作者稿](https://optimization-online.org/wp-content/uploads/2025/01/final_OO.pdf) 更新 2026-02-16 | 同领域近似：C-CRSC 与 reduction-induced CQ 的 LEB，但模型为 C1 标量 h=0,g≤0。 |
| M11 | Roberto Andreani–Gabriel Haeser–Mariana da Rosa–Daiana O. Santos, *On constraint qualifications for non-relaxable sets and an augmented Lagrangian method*. COAP (2026), DOI 10.1007/s10589-026-00792-2；VOR 2026-05-15 | `VERIFIED_SOURCE`：[正式开放全文](https://link.springer.com/article/10.1007/s10589-026-00792-2)，§2 (NLP)、Definition 3.1 | 同领域近似：upper/lower 标量约束；Lower-CRSC 只沿 lower 可行点测试，与本稿开放邻域冻结面 CQ 不同。 |
| M12 | Matthew S. Scott, *Qualification-free convex analysis via the joint supporting subspace*. arXiv:2510.12244v3，2025-11-25 | `VERIFIED_SOURCE`：[原始全文](https://arxiv.org/html/2510.12244v3)，摘要、§§1.1–1.3 与 §2 的模型和定位；未逐定理审计 | 同领域近似：f(x)+g(Ax) 的凸分析与两凸集双边面约化；joint 一词不构成非线性 CRSC 定理覆盖。 |

更正/撤稿状态：在本次访问的上述原始记录与官方页面中未见针对这些记录的更正/撤稿提示；这不是完整更正数据库审计。M01 另执行了精确标题 correction/erratum 查询，未取得针对该 DOI 的官方更正；搜索中的作者主页汇总把其他论文的 correction 混在一起，不能据此给 M01 标“有更正”。其最终内容仍待核验。M05/M06/M08/M12 只按明确版本作为预印本引用，不假定经过同行评审或已无后续版本。

## 4. Claim-to-reference evidence matrix

下表“非覆盖/增量”一栏全部是 `AI_INFERENCE`，建立在 §3 已核实的模型和定理假设上；不把检索无命中当成数学证明。

| 本稿候选主张 | 最近邻已证内容 | 非覆盖 / 本稿候选增量 | 先行性状态与写法 |
|---|---|---|---|
| C1 frozen CRSC 自动 A1/A2（proper nice C） | M01 作者稿仍额外假定 A1/A2；M02 是点态闭像工具 | 两固定子空间秩夹逼，再作连续核投影；不需移动面 | 作者稿层面差异可证实；VOR 层面 `PENDING_VERIFICATION`。写“删除该作者稿中的附加稳定性假设”，不用无版本限定“首次解决已发表开放问题”。 |
| nice + CRSC ⇒ 局部 G⁻¹(C)=G⁻¹(F) | M01 Prop.5.2 已给关键 FR 命题；M07/M12 是凸模型约化 | 本稿固定秩接口使 M01 命题适用；不是首次提出 nonlinear FR | 同上；承认与 Prop.5.2 的短推导关系。 |
| nice + particular F amenable ⇒ 原残差 MSCQ；amenable C 的统一表述 | M03/M04 给输出面度量性质；M05 affine SOC；M06 cone-concavity；M09 affine FRF | 先以原残差控制到 M={P_F⊥G=0} 的输入距离，再在同一个 M 上纠偏；任意 G(x) 不在 span F，不能直接套 amenability | 本次有界检索未发现直接覆盖；全球优先权及 M01 VOR 仍 `PENDING_VERIFICATION`。这是最值得保留的候选主增量。 |
| nice 锥内 amenability ⇔ 每个 apex C1 CRSC 系统 MSCQ | M03 Prop.12、M04 Prop.3.2 已提供面正则性等价 | 充分方向依赖本稿非线性接口；必要方向只是线性面嵌入 + 齐次性 | 可写 universal characterization 的定理内容；不能称必要方向是全新的深层 amenability 机制。 |
| full facial CRCQ 仍可能无 MSCQ | M04 已有 nice 非 amenable 四维锥和切触几何 | 在面 span 的等距线性嵌入上测试；底层锥与失败几何不是原创 | 未找到已按该 exact CQ 命名的使用；优先权仍待核验。写“adapt the cone of Lourenço–Roshchina–Saunderson”。 |
| SOC/p-cone products、PSD 高维面 | M03 已给 amenability 类与乘积性质；PSD/symmetric 常数也是已有工具 | 新的任意联合输入映射推论若主定理新则随之新；不能把 output product 估计宣传为新的 input intersection theorem | 可写“主定理统一适用”，不写“首次证明这些锥 amenable/首次建立它们的误差界”。 |
| 只需 C1；非顶点可通过约化返回 | M01 官方脚注已经承认非二阶部分 C1；M05 强调自然约化会改变导数恒秩测试 | 需在该具体点确实存在并冻结有效 reduction；不是任意 amenable cone 处处可约 | C1 本身不能作为相对 M01 的新放宽。 |

核心负面边界：`nice ⇒ MSCQ under CRSC` 的无条件写法已被输入中的线性面嵌入论证否定。M04 的已知几何支持该反例入口；本任务没有重做完整数学审计。`local feasible-set equality ⇒ original-residual linear error bound` 也不能作为通用逻辑使用。

## 5. 检索与筛选日志

### 5.1 实际执行的完整查询

所有查询日期均为 **2026-09-09 UTC**，来源均为平台原生 Web 搜索；未设置 domain、语种、年份或 recency 过滤。系统未返回可复核的完整数据库总命中数，故每项 hit count 均记为 **NR（not reported）**，不是 0。搜索结果用于发现，最终判断回到 §3 原始/官方来源。顺序按本次调用记录；相邻查询可能在同一请求内并行执行。

| Query ID | 完整查询 | 筛选后用途 / 可读证据 |
|---|---|---|
| Q01 | `"10.1007/s10107-025-02237-w"` | M01 官方页、作者副本；第三方索引仅作线索。 |
| Q02 | `"crsc-redcones" "minimal face"` | M01 作者稿及仓库版本追踪。 |
| Q03 | `"amenable cones" "constant rank"` | M02/M03/M04 关联线索；没有凭关键词并列认定覆盖。 |
| Q04 | `"CRSC" "metric subregularity" conic` | facial/sequential CQ 文献线索；不同 CQ 不自动合并。 |
| Q05 | `"nice cones" "error bound" nonlinear` | M03/M06/M09 及一般 EB 文献线索。 |
| Q06 | `"minimal face" "A1" "A2" CRSC` | M01 可读作者稿中的实际假设段。 |
| Q07 | `"CRSC" "amenable"` | 多数同缩写/一般英语误命中，见排除日志。 |
| Q08 | `"CRCQ" "amenable"` | fully amenable 与 NLP/MPCC 误匹配控制。 |
| Q09 | `"facial reduction" "CRSC" 2026` | M11 与其他 CRSC 近邻。 |
| Q10 | `"A minimal face constant rank" correction erratum` | 未取得 M01 的官方更正记录；不把其他论文的 erratum 移植过来。 |
| Q11 | `"amenable cones" "nonlinear" "error bounds"` | M03/M09；标题宽泛不代表 nonlinear input model。 |
| Q12 | `"nice cones" "metric subregularity"` | 凸锥几何/一般正则性线索。 |
| Q13 | `"Facial reduction for nice (and non-nice) convex programs"` | M07 原始仓库记录、作者全文。 |
| Q14 | `"Revisiting the Constant-Rank Constraint Qualification"` | M05 原始全文与版本页。 |
| Q15 | `"constant rank of the subspace component" conic "error bound"` | M10、经典 NLP CRSC 与 conic 文献。 |
| Q16 | `"minimal face" "metric subregularity" conic` | M05、M12 等模型核对。 |
| Q17 | `"constant rank" "amenable cones" nonlinear` | 交叉补查；没有识别完整目标假设—结论组合。 |
| Q18 | `"Error Bounds for a Class of Cone-Convex Inclusion Problems"` | M06 原始全文与版本页；未把作者介绍中的 submitted 当正式发表。 |

### 5.2 定向原始来源检查

除以上搜索外，直接打开了输入文件中给出的作者/仓库/正式页链接，完整 URL 已列于 §2–§3。关键全文查找字符串实际包括：M01 `Definition 3.2`, `Proposition 5.2`, `Theorem 5.2`, `open`；M02 `Theorem 1.1`；M03 `Definition 8`, `Proposition 12`, `Proposition 13`；M04 `Proposition 3.2`, `Proposition 5.1`, `Theorem 5.3`；M05 `Theorem 5.1`；M06 `Theorem 4.1`；M07 `CRSC`, `constant rank`, `error bound`；M08 `affine`；arXiv 记录 `Submission history`。

M07 的三个字串均未匹配。这里只把未匹配用作辅助定位，**非覆盖判断的实质依据是其凸集/凸函数模型**，不是字串查找能排除所有等价定理。M08 的仿射模型已在 §1 明述，且主要范围为径向 Hölder EB。

### 5.3 纳排规则与日志

纳入：至少与目标 CQ、锥几何、FR 或 residual-transfer 中的一项直接相关，并能在原始或官方来源确定实际模型。最直接竞争者优先做定理层核验；背景来源仅做所使用命题层核验。排除出“直接覆盖集合”不等于排除出参考文献。

| 项目 | 决定 | 理由 / 证据状态 |
|---|---|---|
| M01 | 保留为不可绕过的版本门禁 | 公开作者稿非常接近；最终正文未取得。 |
| M02–M04 | 保留为工具/边界原始来源 | 来源可以承载已有定理和归属；不当成任意非线性主定理。 |
| M05 | 保留比较、排除直接覆盖 | 原文 (3.1) 为 Ax+b∈single SOC；一般 C1 与一般 amenable C 超出其定理范围。 |
| M06 | 保留比较、排除直接覆盖 | Thm.4.1 的 K-concavity 与 smooth-cone 假设不能删除。 |
| M07/M12 | 保留现代近邻、排除直接覆盖 | 两凸集或 f+g∘A 模型；一般 C1 inverse image 不自动是凸集。 |
| M08/M09 | 保留 EB 近邻、排除直接覆盖 | affine feasibility；Hölder/一般模数不是目标原残差 Lipschitz EB。 |
| M10/M11 | 保留现代 CQ 近邻、排除直接覆盖 | 正式正文显示为标量 NLP；Lower-CRSC 的测试域也不同。 |
| Henrion–Kruger–Outrata, *Some remarks on stability of generalized equations* | 术语消歧；排除直接覆盖 | [原始全文](https://optimization-online.org/wp-content/uploads/2011/12/3293.pdf) §2 的 fully amenable 使用 C2 到 polyhedral set 的表示及 normal-kernel 条件；不是 M03 的 face-distance 定义。正式年份/DOI未作完整核验，不填造。 |
| Andreani–Haeser–Schuverdt–Silva, *Two New Weak Constraint Qualifications and Applications* | 经典 NLP 背景；不作新的 conic 竞争者 | [原始正式排版全文](https://www.ime.usp.br/~ghaeser/ahss2.pdf) 已有 CRSC 与 error bound；不能泛称“首次 CRSC⇒EB”。 |
| 军人补偿、研究中心、医学/牙科等 CRSC/CRCQ 命中 | 排除 | 同缩写或一般英语 amenable，与优化对象不符。 |
| ResearchGate、Semantic Scholar、SciSpace、EBSCO、Emergent Mind 等结果 | 不作定理/最终版依据 | 仅可发现题名；本报告判断引用原始/官方来源，不据其摘要生成不存在的 theorem。 |

去重执行为人工书目核对：优先 DOI，其次规范化题名，再作者—题名—年份。M01 的 Springer、作者页、仓库及 arXiv 归同一 work，但版本独立；M03 的 2017 投稿、2019 online、2021 issue 不计三篇；M05/M06/M08 的 HTML/PDF/abs 不计多篇；M10 作者稿与正式文归同一 work。核心表保留 12 个 work。未形成全部搜索结果的下载数据集，因此不报告“全库检出/筛选/排除 N 篇”或 PRISMA 数字。

## 6. 允许与禁止的新颖性措辞

下列允许句是当前证据边界下的定位建议，均为 `AI_INFERENCE`，不为全球首次背书。

| 允许（当前即可在工作稿使用） | 禁止 / 必须改写 |
|---|---|
| “我们证明冻结 minimal-face CRSC 在 proper nice 锥上蕴含全邻域闭像和面稳定。” | “这是已确认的全球首个 nice-cone 稳定性定理。” |
| “这删除了 Andreani 等人 2025-03-20 公开稿 Theorem 5.2 中的 A1/A2；最终发表版的对应表述仍待比对。” | “我们首次解决了最终发表论文明确留下的开放问题。”（最终正文门禁未关闭） |
| “据截至 2026-09-09 本次核验的原文，尚未发现直接覆盖任意 C1 frozen-CRSC amenable-cone MSCQ 的定理。” | “现有文献没有任何一般锥误差界结果”“已穷尽全部文献”。 |
| “核心接口是由 CRSC 得到同一输入流形上的原残差法向纠偏，再调用已有 face amenability。” | “我们引入 amenability/首次发现 amenable⇒nice/首次证明乘积或 PSD amenability”。 |
| “在 nice 锥类内得到 universal characterization；反向是线性面嵌入与已有面正则性的直接联系。” | “充分与必要两个方向均提出全新、相互独立的深机制。” |
| “将 Lourenço–Roshchina–Saunderson 的锥改写为 full facial CRCQ 但无 MSCQ 的线性系统。” | “构造一个全新的四维 nice 非 amenable 锥”“首次发现该切触阶数”。 |
| “适用于耦合的 SOC/p-cone products 和 PSD 高维面。” | “由逐块 MSCQ 自动得到所有联合输入的 MSCQ”。 |
| “假定该参考点存在固定有效 C1 reduction 后，估计可传回原问题。” | “任意 amenable 锥处处 C1-reducible”“相对 M01 首次把 C2 降到 C1”。 |

英文可用的最小定位句：

> We derive an original-residual local linear error bound for C1 systems satisfying frozen minimal-face CRSC over amenable cones. The argument connects constant-rank normal correction on a common input manifold with established facial amenability estimates.

避免在标题、摘要或 cover letter 中出现未经门禁核实的 `first`, `for the first time`, `settles the published open problem`。无首次措辞不妨碍准确陈述定理；不能为回避措辞而淡化对 M01–M04 的归属。

## 7. Evidence and execution status / limitations

- `VERIFIED_SOURCE`：§2–§3 的版本、模型、已指定命题位置；M01 作者稿的 A1/A2；M03/M04 的面正则性与既有反例；M05/M06 的关键限制。
- `VERIFIED_USER_MATERIAL`：冻结理论包及输入独立审计，不代表本专家重新证明所有定理。
- `AI_INFERENCE`：§4 的比较、候选新增接口、相对贡献大小、允许的新颖性措辞。
- `PENDING_VERIFICATION`：M01 VOR 逐定理差分；是否已有他人以 exact facial CRSC/CRCQ 命名过同一线性反例；有限检索之外的先行工作。
- `EXECUTED_LOCAL`：本次只执行输入读取与本报告创建/结构检查；没有运行数值、符号或证明验证。
- `NOT_EXECUTED`：机构数据库完整导出、最终 PDF 取得、投稿、联系作者/编辑、任何全球优先权认证。

限制：搜索排序/索引覆盖会变化；没有付费库或机构导出；不能证明所有后续 work 均已检出。M01 订阅访问是明确 stop condition：此处保留最强中间产物并暂停该最终版本子任务，不绕过限制。根据 SCI-Skills 文献检索规范，缺少最终正文时不能升级为 `PASS_CANDIDATE` 的无保留优先权结论。

### 7.1 最终版差分验收清单（尚未执行）

| 必须返回的项目 | 核验目的 |
|---|---|
| DOI、VOR 标识、正式页码、合法取得的全文或相关页 | 区分最终版与作者预印本；若正文未标版本，不能自行认定。 |
| 对应 Definition 3.2 | F 冻结方式、闭像是否属于 CQ、测试域是否开放邻域。 |
| 对应 Proposition 5.2、Theorems 5.1–5.2 | 共轭 span 恒秩、A1/A2 是否删除/自动推得；若编号改变要按标题/内容定位。 |
| 开放问题段、所有新增 remark/corollary | 是否增添 CRSC⇒MSCQ、amenability、error bound 或同等陈述。 |
| C1/C2 脚注 | 一阶 C1 不作本稿新放宽。 |
| 一页差异表 | 每行：公开稿位置、最终位置、改变/未改变、对应原文证据；只有摘要不通过。 |

### 7.2 可复制的手工操作陪跑 Prompt

仅当作者具有合法访问时使用；不要求购买、不联系第三方、不提交稿件。回传核验后由 orchestrator 决定阶段，不由本专家推进。

```text
你现在是“SCI-Skills 操作陪跑助手”。

请帮助我完成下面这项论文外部操作。每次只告诉我一个步骤，等待我确认或发送截图后再继续。不要假设我已经完成操作。如果页面、按钮或软件界面与预期不同，请让我截图，并根据截图重新指导。

不要索取或要求我粘贴密码、验证码、私钥、会话信息或完整访问凭据。如果需要登录，只指导我在网页中自行登录。不要把安装或配置软件作为主线前置条件；先给我无安装替代方案。只有我明确选择可选增强后，才说明软件来源、系统要求、磁盘空间、风险和卸载方法。

项目ID：RL-CONIC-2026
论文类型：theoretical
当前阶段：T4
任务ID：LIT-PRIORITY-FINAL-VERSION
操作平台或软件：Springer Nature 期刊普通网页；我已合法获得的最终 PDF 也可以
本次目标：取得 DOI 10.1007/s10107-025-02237-w 的正式最终全文，并与 2025-03-20 作者稿作关键定理差分。
已有文件：作者稿 https://www.ime.usp.br/~ghaeser/crsc-redcones.pdf；当前 PRIORITY_EVIDENCE_MATRIX.md
完成标准：核对对应 Definition 3.2、Proposition 5.2、Theorems 5.1–5.2、A1/A2 后开放问题段、C1/C2 脚注；记录正式页码和是否有新增 CRSC⇒MSCQ/amenability/error-bound 结论。
安全与隐私限制：不得绕过权限；没有合法访问就停下并报告。不要购买、联系作者/编辑或进行投稿操作；不要回传账户与机构凭据。
需要带回原对话的材料：合法最终 PDF（或足够核验的相关页），一页关键差异表，以及以下 SCI-Skills 操作回传卡。

完成后，请核验生成或下载的文件，并输出一张“SCI-Skills 操作回传卡”，保留项目ID、阶段和任务ID，列明实际步骤、参数、文件、标识符、限制和未解决问题。
```

```yaml
contract_version: "1.0"
project_id: RL-CONIC-2026
paper_family: theoretical
stage_id: T4
operation_task_id: LIT-PRIORITY-FINAL-VERSION
platform_or_software: Springer Nature ordinary webpage / lawfully supplied final PDF
operation_date: null
completed_steps: []
queries_filters_or_parameters: []
generated_identifiers: []
returned_files: []
logs_or_screenshots: []
record_count_or_output_summary: null
access_license_or_export_limits: []
problems_encountered: []
unresolved_items: []
user_confirmation: null
credentials_or_secrets_included: false
```

导出说明：这不是系统检索，当前无需批量数据库导出。若作者以后补充合法 RIS/BibTeX/CSV，保留 DOI、完整作者、标题、年份、期刊、卷页、版本日期、原始 URL 与 access note 后再人工去重；本任务没有生成或宣称生成数据库导出。

## 8. Quality checks and deliverable

- [x] 三个输入均读取；冻结的 CQ、原残差和 apex/reduction 范围保持一致。
- [x] 18 条实际查询、共同日期、过滤方式、NR 命中限制记录齐全。
- [x] 12 个核心 work 去重；online、issue、预印本日期分开。
- [x] 最近邻逐模型/关键假设比较；最终版与公开作者稿分开。
- [x] 所有定理非覆盖与新颖性评价标为推断；没有把摘要当全文。
- [x] LRS 锥构造、amenability、closed-image、C1 脚注等已有内容归属明确。
- [x] 主稿、项目权威状态、其他代理文件未修改。
- [ ] M01 正式最终正文逐定理差分——仍需作者合法回传。

交付：`output/conic_paper/PRIORITY_EVIDENCE_MATRIX.md`。本报告由根代理统一保存与合并，不单独修改稿件、项目阶段或书目。

## 9. Exact SCI-Skills expert result

```yaml
contract_version: "1.0"
expert_skill: sci-skills-literature-search
project_id: RL-CONIC-2026
paper_family: theoretical
stage_id: T4
task_id: LIT-PRIORITY
task_status: PROVISIONAL
inputs_reviewed:
  - output/JOURNAL_PRIORITY_AUDIT_GENERAL_AMENABLE_CRSC_MSCQ.md
  - output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md
  - output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md
  - primary and official sources M01-M12 and disambiguation sources in Sections 2-5
outputs:
  - output/conic_paper/PRIORITY_EVIDENCE_MATRIX.md
evidence_status:
  - "VERIFIED_SOURCE: M01 author manuscript retains A1/A2; official record and C1 note checked"
  - "VERIFIED_SOURCE: M01 arXiv latest visible v2 predates the author-hosted March 2025 manuscript"
  - "VERIFIED_SOURCE: amenability tools and nice nonamenable cone are established prior work"
  - "VERIFIED_SOURCE: affine, cone-concave, convex-model and scalar-NLP restrictions checked"
  - "VERIFIED_USER_MATERIAL: frozen theorem package and supplied mathematical audit reviewed"
  - "AI_INFERENCE: no accessible checked nearest-neighbor theorem directly covers the full target package"
  - "PENDING_VERIFICATION: M01 final theorem text, exact counterexample prior naming and broader priority"
  - "NOT_EXECUTED: institutional export, final PDF retrieval, submission or external coordination"
assumptions:
  - finite-dimensional proper cone and C1 apex system with a frozen reduction when applicable
  - CRSC includes reference adjoint cone-image closedness and full-open-neighborhood fixed-face rank
  - amenability is face-distance cone amenability, not full amenability of a smooth composite
author_input_needed:
  - lawful final PDF or sufficient final theorem pages for DOI 10.1007/s10107-025-02237-w
manual_actions:
  - operation companion and return card supplied for LIT-PRIORITY-FINAL-VERSION; not executed
quality_checks:
  - exact source/version distinctions and theorem locators recorded
  - search queries, date, filters, unavailable hit counts and screening reasons recorded
  - DOI-title-author deduplication with versions retained separately
  - source findings separated from AI inference and pending priority claims
  - permissible and prohibited novelty language supplied
  - no manuscript or stage-state mutation
conflicts:
  - conflict_id: PRIORITY-VOR-ACCESS
    type: version_evidence_gap
    claim: the final published M01 theorem has not already removed A1/A2 or added the target MSCQ conclusion
    source_or_locator: DOI 10.1007/s10107-025-02237-w versus author manuscript revised 2025-03-20
    competing_values_or_interpretations:
      - public author manuscript retains assumptions and an open question
      - final theorem text is inaccessible and may differ
    recommended_resolution: obtain lawful final text and complete the Section 7.1 difference check
conflict_resolution_status: UNRESOLVED
merge_permission: orchestrator_only
recommended_next_action: obtain and compare the lawful M01 final theorem text before releasing any unconditional first-result or published-open-problem claim
stage_acceptance_recommendation: REPAIR
```

唯一主要下一步：合法取得并核对 M01 最终正文，关闭版本差分门禁后再发布无保留的先行性措辞。
