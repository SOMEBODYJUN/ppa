# RLEB–LT 相关研究资产：范围、权威版本与纳入审查

日期：2026-09-20。角色：独立资产范围／版本审核。

本报告核对当前工作区中的源文件、综合稿、修订关闭记录与实际 SHA-256，确定新研究资产包应怎样组织。它不是重做数学证明或文献优先权审计；下文“通过”仅转述相应审计的明示范围，不向新文件、新定理或总体比较移植。

## 1. 总判断

应打包成“当前接手入口＋可复核证明资产＋原件和历史”的研究档案，而不是把全部旧报告平铺后让接手者自行判断。

当前核心任务是：在不按 RLEB/LT 证书预选成员的 PPA 对象体系中，判断两种认证覆盖的真实结构差距。当前尚缺的是将动力学分层、完整原图和真实全纤维残差接起来的有效类别比较工具。把它合并为一个主桥梁便于交接，但不应声称已经证明所有解法必须通过某个特定的 `Φ` 投影；直接在原对象空间证明仍是合法路线。

新包应有一个新的、简短的主入口，按“期望—前人工具—尝试—保留下来的成果—唯一主求助”组织。`mathematician_handoff/07_final_handoff.md` 是目前最完整的数学技术综合，而不是最适合未经导航直接阅读的首页。其 O1–O12、OP1–OP10 保留为技术索引，不重新全部列为需要用户解决的独立难题。

## 2. 标签与冲突处理规则

| 标签 | 含义 | 是否作为当前主任务结论 |
|---|---|---|
| `CURRENT_CORE` | 目前问题口径、精确数学范围和最新状态的权威文件 | 是，仍须带范围 |
| `SUPPORTING` | 可复用证明、反例、原始文献对应或已关闭审计 | 按指定用途引用 |
| `HISTORICAL_SCOPE` | 数学内容可能仍有效，但研究问题／建议方向已改变 | 否；不等于数学被推翻 |
| `SUPERSEDED_STATE` | 原审计状态、问题清单或建议已被后续修订明确取代 | 只能作审计轨迹 |
| `SOURCE_SNAPSHOT` | 用户原件／原包字节快照 | 保留原貌，不改成当前总结 |
| `EXCLUDE_DUPLICATE` | 重复解包、构建缓存、预修订冗余或无关旁支 | 不进入当前阅读主干 |

优先级不是单纯按文件序号或日期排序：

1. 新包 README 负责最新阅读顺序和用户本轮需求；不新增未经证明的数学判决。
2. 对当前比较口径，采用 `mathematician_handoff/07_final_handoff.md`，并以 `06_math_audit.md` 与 `02`／`04` 的审计后修订解释其证明范围。
3. 对具体基础定理，引用其最新专题文件和对应审计，不用后来的综合稿替代完整证明。
4. 对同版修订状态，以明确绑定稿件哈希的关闭记录覆盖早期 `MINOR_REPAIR`；不得删除原审计证据。
5. 数学正确性、文献主张范围、文件 QA 是不同审查，不能合成一个“全部研究 PASS”。

## 3. 两份用户基础源资产：已验证身份与不同角色

| 当前源路径 | 实测规模 | SHA-256 | 纳入角色 |
|---|---:|---|---|
| `upload/01-_RL-_2026-09-14_v2_-.zip` | 6.3 MB；101 个文件 | `753a09e11eab5dbcf981fa418713cabd7676e09350bfca8ca4171f0b0168868d` | `SOURCE_SNAPSHOT`：RL＋锥＋Markov 的历史总研究资产和离线超边导航 |
| `upload/04-RLEB_PPA_-_2026-09-18.zip` | 383 KB；17 个实文件＋3 个目录条目 | `a377f9dd6a66f9281b1b98089c311b81923e908e541093768bfa9e9d1fe03871` | `SOURCE_SNAPSHOT`：本次调用的 RLEB–PPA 专题基础稿 |

两者都实际存在，均重新计算哈希，并已读取压缩包目录及当前解包副本的说明文件。它们不是同一内容的不同压缩格式。

9 月 18 日稿题为 *Nonlinear Generalized Monotonicity and Error Bounds for Proximal Point Convergence at Multivalued Graph Junctions*，含 `main.tex`、分章源、PDF、`references.bib`、`locked_content_ledger.yaml` 等。后续 solution-selection 和 RLEB–LT 比较报告实际调用的是这份稿的 `sections/theorem_spine.tex`。所以它应是新包中“需要核查所调用 RLEB 基础接口时”的默认入口。

9 月 14 日总包具有独立的来源谱系和旁支内容，不应说 9 月 18 日稿全面替代它。另一方面，9 月 14 日旧导航中的 `PENDING` 标签绑定当时的稿件／审计版本，不能移植成对 9 月 18 日稿或后续结果的当前否定。

**建议：**两份 ZIP 原样保留在 `source_inputs/`，旁附角色、原上传名、哈希与阅读优先级；不需将 9 月 14 日全部锥／Markov 内容再展开一遍进入本轮主目录。若另行展开 9 月 18 日稿供便捷阅读，应标为“原件只读解包副本”，而非团队本轮新修订。

## 4. 当前主干 canonical map

以下路径均相对当前工作区；新包移动路径时应有一份源→交付路径映射。

### 4.1 数学家交接阶段

| 文件 | 标签 | 用途及优先级 |
|---|---|---|
| `mathematician_handoff/07_final_handoff.md` | `CURRENT_CORE` | 最新技术综合：统一符号、已证定理 P、范围边界、文献和所有问题详索引 |
| `mathematician_handoff/06_math_audit.md` | `CURRENT_CORE` | 本轮承重命题独立复核；特别是定理 P、局部观测不控全图、塔选择刚性边界 |
| `mathematician_handoff/02_ideal_problem_formulation.md` | `CURRENT_CORE` | 中立比较问题、实例／原算子量词、内生剖面；已纳入定理 P 加强 |
| `mathematician_handoff/04_research_ideas.md` | `SUPPORTING` | 已审种子引理和构建路线；路线本身不是已完成主定理 |
| `mathematician_handoff/03_obstruction_taxonomy.md` | `SUPPORTING` | O1–O12 技术反例索引；不作为新包首页待办清单 |
| `mathematician_handoff/05_priorart_boundary.md` | `CURRENT_CORE` | 当前体系所用前人结果的定理级对应、覆盖与未覆盖；仍非穷尽优先权判决 |
| `mathematician_handoff/README.md` | `HISTORICAL_SCOPE` | 原技术交接入口。其优先级说明可保留；新包首页应另写更短入口 |
| `mathematician_handoff/01_full_handoff_draft.md` | `SUPERSEDED_STATE` | 历史集成底稿和详索引；不得沿用其中已被关闭的未知项 |

`07` 明确采用 `06` 及 `02`／`04` 随后修订。最新有效状态是：固定紧状态、完整紧源的 T-only 图卡内，`Φ=(w,m)` 连续且 proper，实际像闭／Polish，纤维紧／Baire，映射 perfect／quotient。仍不能扩为 category-preserving、任意完整 F 的局部 atlas 上 properness 或总体 RLEB–LT 差距。

`06_math_audit.md` 的确切终判是“有两处范围表述须修正，所审种子引理成立；没有完成总体差距定理”，不能仅抽成无限范围的 `PASS`。其后 `02`、`04`、`07` 已明确纳入修正。

### 4.2 中立 PPA 体系阶段

| 文件 | 标签 | 用途及状态 |
|---|---|---|
| `ppa_system_team/10_final_blueprint.md` | `CURRENT_CORE`（底座） | P0–P10、五层对象体系、基础定理表；是底座权威，不是所有当前未决事项的最终权威 |
| `ppa_system_team/01_ambient_axioms.md` | `SUPPORTING` | 原闭图本体、良定 atlas、局部完整图表及其 AW／Polish 证明 |
| `ppa_system_team/02_convergence_topology.md` | `SUPPORTING` | 逐点／局部一致、全时间、共同尾拓扑桥 |
| `ppa_system_team/03_certificate_embeddings.md` | `SUPPORTING` | direct／energy 规范化、LT 公共接口→energy、标准图卡编码 |
| `ppa_system_team/04_priorart.md` | `SUPPORTING` | WPO、BRZ、Tikhonov、resolvent 家族等详细文献记录 |
| `ppa_system_team/05_stress_test.md` | `SUPPORTING` | 已修复的饱和逆像／任意见证投影区别，以及单值／全域量词 |
| `ppa_system_team/06_resolvent_family.md` | `SUPPORTING` | 完整跨步长关系、相容族、轨道与策略 |
| `ppa_system_team/07_embedding_math_audit.md` | `SUPPORTING` | `PASS`，仅为证书嵌入、gauge 规范化及固定紧图卡编码 |
| `ppa_system_team/08_architecture_audit.md` | `SUPPORTING` | 修补后 `PASS`，仅为明确有限维／共同域／量词下空间和拓扑基础 |
| `ppa_system_team/09_value_audit.md` | `SUPPORTING`＋部分 `SUPERSEDED_STATE` | 文献价值和最大 AW 退化论证仍有用；将 energy 规范化／局部图表列为未完成的旧句，由 `03/07/08/10` 取代 |

`10` 开头已经显式指出 `09` 有上述旧状态句。新 README 应保留这一具体冲突处理，不应暗示 `09` 全文失效，也不能借其旧句重开已补齐的技术工作。

### 4.3 中立分类的构建与障碍阶段

| 文件 | 标签 | 用途及边界 |
|---|---|---|
| `ppa_classification_team/01_frozen_denominator.md` | `SUPPORTING` | 固定宏观规格、完整原图、实际共同尾、全纤维残差 |
| `ppa_classification_team/02_structural_deformation.md` | `SUPPORTING` | 范围内已核结构变形工具；允许尾放宽和微观缩域，非总体分类 |
| `ppa_classification_team/03_object_category.md` | `SUPPORTING` | 紧图卡对象侧 `K_sigma`、LT 必要块、母空间位置问题 |
| `ppa_classification_team/04_step_spectrum.md` | `SUPPORTING` | 任意紧局部谱实现、保留实步长的闭块编码；不是宏观同域总体谱定理 |
| `ppa_classification_team/05_obstruction_audit.md` | `SUPPORTING` | 自第一纲、尾层退化、步长谱、完整图与 collar 的范围内交叉审计；§9 是本阶段各模块准确放行表 |
| `ppa_classification_team/06_priorart_tools.md` | `SUPPORTING` | 延拓、共轭和相关工具为何不自动保存目标量 |
| `ppa_classification_team/07_stage_synthesis.md` | `HISTORICAL_SCOPE` | 上一阶段综合。成果记录保留；“仿射漂移层优先”的推进建议被 `mathematician_handoff/02`、`07` 明确降为工具路线 |

**重要：**`07_stage_synthesis.md` 并非被数学推翻。被替代的是“应先在仿射漂移层完成分类”作为主战略，以及把三个局部瓶颈逐一交给用户的汇报方式。完整变形、对象编码和谱实现等结果仍可用，但必须保留原范围。

## 5. 早期比较与初值稳定性：应保留，但与当前主干分层

### 5.1 `comparison_space_team`

| 文件 | 标签 | 新包中的位置 |
|---|---|---|
| `01_exact_translation.md` | `SUPPORTING` | 共同接口字典，LT all-pairs／pointwise、direct／energy 的精确区别 |
| `02_monotone_category_literature.md` | `SUPPORTING` | 单调算子／非扩张映射空间的文献证据 |
| `03_holder_lipschitz_category.md` | `SUPPORTING` | 固定模、big/little Hölder、凸层 meagreness 工具 |
| `04_comparison_space_architecture.md` | `HISTORICAL_SCOPE`＋证明资产 | 超吸引结构层 Y 的完整定义和证明；仅测试层 |
| `05_meagreness_feasibility.md` | `HISTORICAL_SCOPE`＋证明资产 | 同阶段可行性、见证和模型；不能冒充中立空间总答案 |
| `06_math_audit.md` | `SUPPORTING` | 修补后 PASS，R1–R4 已关闭；任意步长加强范围内通过 |
| `07_priorart_value_audit.md` | `SUPPORTING` | 此受限组合定理的文献／价值审计，不是当前统一体系的最终优先权结论 |
| `08_naturalness_audit.md` | `SUPPORTING` | 解释预装超吸引为何不能代表全部 RLEB；适合“为什么换路”索引 |
| `09_final_synthesis.md` | `HISTORICAL_SCOPE` | 受限层综合；其关于总目标、最大证书层的下一步建议由中立体系与新交接取代 |

这组的“LT 在 Y 内第一纲”没有被撤销；撤销的是它能代表总体理论规模的读法。不要在文件标题前直接加“错误／作废”。

### 5.2 `genericity_team`

| 文件 | 标签 | 新包中的位置 |
|---|---|---|
| `01_operator_space.md` | `SUPPORTING` | 统一证书层、有限纤维、极限映射的集合结构工具 |
| `02_baire_literature.md` | `SUPPORTING` | 早期 Baire 文献记录，后有更直接的 BRZ 对应 |
| `03_prevalence_measure.md` | `SUPPORTING`＋`HISTORICAL_SCOPE` | prevalence／Haar-null 量词边界可复用；参数概率优先建议已非现主线 |
| `04_semialgebraic_families.md` | `HISTORICAL_SCOPE` | 坏选择／削圆的有限参数相图，作为路线历史和验算 |
| `05_rleb_robustness.md` | `SUPPORTING`＋`HISTORICAL_SCOPE` | 同证书削圆、C0 与强 Hölder 拓扑区别 |
| `06_math_stress.md` | `SUPERSEDED_STATE`（初审） | 文件保持 MINOR_REPAIR；四项处理见 `08` §7，不虚构独立终审关闭文件 |
| `07_value_priorart.md` | `HISTORICAL_SCOPE` | 当时坏类泛性方向的价值与优先权边界 |
| `08_final_synthesis.md` | `HISTORICAL_SCOPE` | 当时方向的 CONDITIONAL 终判；有限参数优先路线已被用户后续要求取代 |

本组研究的问题主要是“极限选择坏类多大”，不是当前“RLEB 和 LT 认证覆盖差距多大”。即使共享方法，也不能合并成同一项已证结论。

### 5.3 `initial_value_stability_team`

`01_terminology_map.md`、`02_fixedpoint_retraction.md`、`03_hypomonotone_proxregular.md`、`04_asymptotic_phase.md`、`05_partial_smoothness.md` 都为 `SUPPORTING` 文献和稳定性工具，适合附录资料层；不要求接手当前纲分类者先逐篇读完。

- `06_synthesis.md`：本专题的当前综合权威，作为 `SUPPORTING` 纳入。
- `07_synthesis_stress.md`：初审 `MINOR_REPAIR`，状态为 `SUPERSEDED_STATE`，数学推导与问题历史仍保留。
- `08_synthesis_closure.md`：绑定最终主稿哈希的 `SYNTHESIS_PASS`，明确关闭两项修补；它是本专题当前放行状态。

实测 `06_synthesis.md` SHA-256 为 `837e01e2a6178983bebbeb14d7d0039cdad9f5e41b84f20ee3c75efa9fcd5fbf`，与 `08` 绑定值一致。

## 6. Solution-selection 交付的权威与审计链

这一稿是独立已修订研究成果，是当前体系研究的重要动机和检验模型，但不是本次已完成的 LT–RLEB 类别分类。

| 文件／目录 | 标签 | 处理 |
|---|---|---|
| `solution_selection_revised_v1/research_note.md` | `CURRENT_CORE`（本专题） | 唯一内容权威源 |
| `solution_selection_revised_v1/solution_selection_revised.tex` | `SUPPORTING` | Markdown 同源机械生成，不能独立手改分叉 |
| `solution_selection_revised_v1/output/pdf/solution_selection_revised.pdf` | `SUPPORTING` | 20 页同源可阅读稿 |
| `SOURCE_MAP.md`、`response_to_audit.md`、`change_log.md`、`build_report.md` | `SUPPORTING` | 原件对应、修改责任和复现说明 |
| `revision_math_audit.md`、`revision_priority_audit.md` | `SUPERSEDED_STATE` | 首轮 MINOR_REPAIR；保留证据，不作当前阻断 |
| `revision_math_closure.md` | `SUPPORTING` | 最终 `REVISION_MATH_PASS`，关闭 N1/N2 |
| `revision_priority_closure.md` | `SUPPORTING` | 最终 `REVISION_CLAIMS_PASS`，关闭 P1/P2；没有关闭全球首创或 U1–U3 |
| `final_package_QA.md` | `SUPPORTING` | `PACKAGE_QA_PASS`，仅构建、内容保真、排版和冻结一致性 |
| `build.sh`、`manuscript_template.tex`、`prepare_pdf.lua`、`verify_research.py`、`results/` | `SUPPORTING` | 正式构建／复现必需文件；脚本不是数学证明 |
| `source_archive/` | `SOURCE_SNAPSHOT` | 原上传稿快照，不是最新版 |
| `build/research_note_pre_minor_repair.md` | `SUPERSEDED_STATE` | 仅供复查局部差分，不进入主阅读路径 |
| 其余 build 缓存、渲染页面和 QA 临时目录 | `EXCLUDE_DUPLICATE` | 正式源／PDF／审计已足够；可单独保持原发布 ZIP 以保全冻结交付 |

本次重新计算三个冻结文件，全部与两份关闭记录及最终 QA 一致：

| 文件 | SHA-256 |
|---|---|
| `research_note.md` | `91ad4b0948a21443fc557b5ea579e692650399504e735223d72347ba86bea1b8` |
| `solution_selection_revised.tex` | `b0c750a8235ecfe2c1959f5b6da37bc2b539afe0f7ace618c26243ea33ee2a56` |
| `output/pdf/solution_selection_revised.pdf` | `0bd11b6c3e8c246842151a0190928b0bc02c3f1662405d0d0771c4687d418c03` |

已发布 ZIP `solution_selection_revised_v1_delivery.zip` 实测 SHA-256：`cae4a31c80b5c29c21af3444a66e6a4de007cfac24db21ffd5a5f261fbb037f6`。

原交接 ZIP `mathematician_handoff_delivery.zip` 实测 SHA-256：`ae3696992dcc473256eab4b6b0d904d92845da7b3b24a10467eef58873510db4`。新包如果已经完整纳入其源目录，无需再嵌入这个旧 ZIP；哈希记录足以追踪原交付，不必造成重复的两个“最终入口”。

## 7. 不应纳入主包／阅读主干的内容

1. `ss_audit_stage/A`、`B`、`C` 的重复解包：同一个原稿最多保留一个只读来源副本，或保留原 ZIP；不要三套同时进入主树。
2. `ss_package_qa.*`、`tmp/`、PDF 页 PNG、TeX 工具链、字体安装缓存、`__pycache__`、中间编译文件：不属于研究正文，除非复现清单明确需要。
3. `papers/`、`output/pdf` 中的多轮 RL／锥／Markov 旧编排：这些是另一个写作阶段。当前包以 9 月 18 日 RLEB 原件和修订 solution-selection 为基础，不混入多个未说明身份的“final/v2/v3”稿。
4. 整个 Koopman 或锥／Markov 后续旁支研究目录：当前没有调用，不为凑“完整”而展开纳入；用户 9 月 14 日原 ZIP 已保存历史。
5. 同一原始文献的 PS／PDF／TXT／逐页 PNG 全套重复：优先保留一个原件和有必要的可搜索文本，并写出处。不要把来源文本误标为本项目新研究。
6. 数值测试输出不能纳入“证明通过”栏。保留时必须标为 `NUMERICAL_REPRODUCTION`。

以上“排除”只指不复制进新交付，不授权删除工作区或用户原件。

## 8. 给主编的最小落地建议

新 README 只需要让数学家一眼回答五件事：

1. 我们希望比较什么对象、什么意义的差距？
2. 先读哪一份短交接，然后查哪一份技术综合？
3. 哪些具体命题已有证明／范围内审计，在哪个文件？
4. 哪一个核心 idea 目前需要他们提供，而不是要求他们重审所有旧研究？
5. 历史文件出现相反口径／MINOR_REPAIR 时，去哪里确认已替代状态？

建议新包保留完整证明文本，但分为当前核心、证明与审计、文献对应、基础稿与复现、历史路线、用户原件六个角色。每个目录加短 README，所有旧正文原样存放，通过外部清单标状态，不逐篇改写历史。

交付前必须检查：内部相对链接、源路径映射、哈希清单、ZIP 实际解压内容、关键 PDF／TeX 是否存在，以及新首页是否再次把特殊层结论写成总体结论。当前 scope audit 没有发现阻止打包的缺失原件；最需要修复的是阅读入口和状态优先级，不是再启动新一轮数学研究。
