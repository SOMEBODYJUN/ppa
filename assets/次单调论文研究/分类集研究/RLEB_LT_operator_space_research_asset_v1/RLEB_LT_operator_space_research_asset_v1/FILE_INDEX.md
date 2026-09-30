# 文件索引

版本：v1 · 2026-09-20。此索引覆盖 73 个交付文件（包括校验表自身）；源 ZIP 内部文件保持各自索引，不在此重复展开。

标签含义见 [README](README.md)：CANONICAL 是当前入口或指定模块版本，HISTORICAL 是受限工具/研究历史，SUPERSEDED 表示对应综合状态或策略被替代，不等于整篇定理作废。来源与精确审计关系见 [PROVENANCE](PROVENANCE.md)；机器可读版本为 [FILE_REGISTER.json](FILE_REGISTER.json)。

## 根目录

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [CHANGELOG.md](CHANGELOG.md) | CANONICAL | 记录本次资产整理的编排和范围变化。 |
| [FILE_INDEX.md](FILE_INDEX.md) | CANONICAL | 为每个交付文件给出状态标签和一句用途，支持定位。 |
| [FILE_REGISTER.json](FILE_REGISTER.json) | CANONICAL | 提供逐文件来源、标签、用途、审计状态的机器可读索引。 |
| [MANIFEST.sha256](MANIFEST.sha256) | CANONICAL | 给出所有交付文件（不含自身）的完整性校验值。 |
| [OPEN_PROBLEM.md](OPEN_PROBLEM.md) | CANONICAL | 把求助集中为一个主桥梁及四个相连接口和验收标准。 |
| [PROVENANCE.md](PROVENANCE.md) | CANONICAL | 记录源到交付映射、身份、代理可核程度和审计链。 |
| [README.md](README.md) | CANONICAL | 项目目标、当前主桥梁、阅读路径、版本标签与接手总入口。 |
| [STATUS.md](STATUS.md) | CANONICAL | 登记已核结果、适用范围、未完成主问题与禁止外推。 |

## 00_START_HERE

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [QUICK_HANDOFF.md](00_START_HERE/QUICK_HANDOFF.md) | CANONICAL | 用短篇说明目标、前人工具、尝试、当前停点及要什么idea。 |
| [READING_ROUTES.md](00_START_HERE/READING_ROUTES.md) | CANONICAL | 提供30分钟入口与按学科分工的证明阅读路径。 |

## 01_CANONICAL_HANDOFF

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [01_full_handoff_draft.md](01_CANONICAL_HANDOFF/mathematician_handoff/01_full_handoff_draft.md) | SUPERSEDED | 交接初稿与详细历史索引，不能沿用已被关闭的未知项。 |
| [02_ideal_problem_formulation.md](01_CANONICAL_HANDOFF/mathematician_handoff/02_ideal_problem_formulation.md) | CANONICAL | 精确定义中立比较口径、步长量词和内生剖面。 |
| [03_obstruction_taxonomy.md](01_CANONICAL_HANDOFF/mathematician_handoff/03_obstruction_taxonomy.md) | CANONICAL | 保存O1–O12的最小反例与技术边界，按问题检索。 |
| [04_research_ideas.md](01_CANONICAL_HANDOFF/mathematician_handoff/04_research_ideas.md) | CANONICAL | 给出构建候选、种子引理与验收线，供选取主桥梁路线。 |
| [05_priorart_boundary.md](01_CANONICAL_HANDOFF/mathematician_handoff/05_priorart_boundary.md) | CANONICAL | 整理当前体系的原始文献对应及未清关优先权。 |
| [06_math_audit.md](01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md) | CANONICAL | 独立核准T-only观测和种子引理并限制其向完整图外推。 |
| [07_final_handoff.md](01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md) | CANONICAL | 最新完整技术综合与已核范围，作为数学家交接主稿。 |
| [README.md](01_CANONICAL_HANDOFF/mathematician_handoff/README.md) | SUPERSEDED | 旧技术交接导航，作为来源保留，首页由本包新入口替代。 |
| [README.md](01_CANONICAL_HANDOFF/README.md) | CANONICAL | 解释当前技术交接文件的优先级和旧初稿地位。 |

## 02_NEUTRAL_PPA_SYSTEM

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [01_ambient_axioms.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/01_ambient_axioms.md) | CANONICAL | 定义中立闭图本体、良定图表、公理与各动力层。 |
| [02_convergence_topology.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/02_convergence_topology.md) | CANONICAL | 证明逐点/局部一致及全时间/共同尾的拓扑关系。 |
| [03_certificate_embeddings.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/03_certificate_embeddings.md) | CANONICAL | 给direct/energy规范化、LT转换与标准图卡证书编码。 |
| [04_priorart.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/04_priorart.md) | CANONICAL | 保存WPO、BRZ、全时间拓扑与resolvent族原文证据。 |
| [05_stress_test.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/05_stress_test.md) | CANONICAL | 压力检查对象量词、单值/全域与证书投影推理。 |
| [06_resolvent_family.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/06_resolvent_family.md) | CANONICAL | 建立完整跨步长关系、相容族、轨道与策略接口。 |
| [07_embedding_math_audit.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/07_embedding_math_audit.md) | CANONICAL | 专项独立复核LT→energy、gauge规范化与紧图卡编码。 |
| [08_architecture_audit.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/08_architecture_audit.md) | CANONICAL | 审查母空间、局部良定图表与拓扑基础。 |
| [09_value_audit.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/09_value_audit.md) | HISTORICAL | 保存前人覆盖与价值分析，部分旧未完成状态已被后续替代。 |
| [10_final_blueprint.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/10_final_blueprint.md) | CANONICAL | 中立体系底座总览，列出公理和基础定理依赖。 |
| [README.md](02_NEUTRAL_PPA_SYSTEM/README.md) | CANONICAL | 指向体系底座并说明旧价值稿被关闭的技术状态。 |

## 03_CLASSIFICATION_STAGE

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [01_frozen_denominator.md](03_CLASSIFICATION_STAGE/ppa_classification_team/01_frozen_denominator.md) | CANONICAL | 固定完整原图、宏观域、真实残差和实际尾等比较规格。 |
| [02_structural_deformation.md](03_CLASSIFICATION_STAGE/ppa_classification_team/02_structural_deformation.md) | CANONICAL | 保存受限仿射结构层的保真变形与任意步长LT排除。 |
| [03_object_category.md](03_CLASSIFICATION_STAGE/ppa_classification_team/03_object_category.md) | CANONICAL | 给完整紧源对象侧K_sigma及类别诊断工具。 |
| [04_step_spectrum.md](03_CLASSIFICATION_STAGE/ppa_classification_team/04_step_spectrum.md) | CANONICAL | 处理实步长编码、局部谱实现及选择量词分离。 |
| [05_obstruction_audit.md](03_CLASSIFICATION_STAGE/ppa_classification_team/05_obstruction_audit.md) | CANONICAL | 交叉复核分类模块并给自第一纲和尾层退化边界。 |
| [06_priorart_tools.md](03_CLASSIFICATION_STAGE/ppa_classification_team/06_priorart_tools.md) | CANONICAL | 说明延拓、局部替换和共轭工具的前提与缺失接口。 |
| [07_stage_synthesis.md](03_CLASSIFICATION_STAGE/ppa_classification_team/07_stage_synthesis.md) | HISTORICAL | 保存分类阶段成果与旧策略，其仿射优先建议已降为工具路线。 |
| [README.md](03_CLASSIFICATION_STAGE/README.md) | CANONICAL | 保留分类模块但降级旧仿射优先策略。 |

## 04_AUDITS_AND_PRIOR_ART

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [ASSET_SCOPE_AUDIT.md](04_AUDITS_AND_PRIOR_ART/ASSET_SCOPE_AUDIT.md) | CANONICAL | 独立核对包的范围、权威版本、原件身份与审计状态优先级。 |
| [CLAIM_BOUNDARY_REGISTER.md](04_AUDITS_AND_PRIOR_ART/CLAIM_BOUNDARY_REGISTER.md) | CANONICAL | 逐项对照可用主张、禁止外推与证明证据。 |
| [PRIOR_ART_MAP.md](04_AUDITS_AND_PRIOR_ART/PRIOR_ART_MAP.md) | CANONICAL | 按原记录对照前人工具、精确文献位置和本项目缺桥。 |
| [README.md](04_AUDITS_AND_PRIOR_ART/README.md) | CANONICAL | 导航各阶段审计正文，避免将不同PASS合并。 |

## 05_EARLIER_EXPLORATIONS

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [01_exact_translation.md](05_EARLIER_EXPLORATIONS/comparison_space_team/01_exact_translation.md) | HISTORICAL | 建立RLEB与LT共同接口词典，区分all-pairs和pointwise。 |
| [02_monotone_category_literature.md](05_EARLIER_EXPLORATIONS/comparison_space_team/02_monotone_category_literature.md) | HISTORICAL | 查单调/resolvent/非扩张算子空间的类别先例。 |
| [03_holder_lipschitz_category.md](05_EARLIER_EXPLORATIONS/comparison_space_team/03_holder_lipschitz_category.md) | HISTORICAL | 分析固定模、big/little Hölder和模饱和的拓扑差异。 |
| [04_comparison_space_architecture.md](05_EARLIER_EXPLORATIONS/comparison_space_team/04_comparison_space_architecture.md) | HISTORICAL | 构造统一严格RLEB的特殊超吸引比较层Y。 |
| [05_meagreness_feasibility.md](05_EARLIER_EXPLORATIONS/comparison_space_team/05_meagreness_feasibility.md) | HISTORICAL | 给特殊结构层的meagreness见证和可行性证明。 |
| [06_math_audit.md](05_EARLIER_EXPLORATIONS/comparison_space_team/06_math_audit.md) | HISTORICAL | 独立核准特殊层定理与列明的任意步长加强。 |
| [07_priorart_value_audit.md](05_EARLIER_EXPLORATIONS/comparison_space_team/07_priorart_value_audit.md) | HISTORICAL | 记录该受限组合构造的优先权与研究价值边界。 |
| [08_naturalness_audit.md](05_EARLIER_EXPLORATIONS/comparison_space_team/08_naturalness_audit.md) | HISTORICAL | 说明预设超吸引为何不能代表全部RLEB或全部收敛者。 |
| [09_final_synthesis.md](05_EARLIER_EXPLORATIONS/comparison_space_team/09_final_synthesis.md) | HISTORICAL | 保存特殊层综合结论与当时下一步建议。 |
| [01_operator_space.md](05_EARLIER_EXPLORATIONS/genericity_team/01_operator_space.md) | HISTORICAL | 构造共同证书层及极限选择的集合结构工具。 |
| [02_baire_literature.md](05_EARLIER_EXPLORATIONS/genericity_team/02_baire_literature.md) | HISTORICAL | 保存早期Baire文献与拓扑敏感性记录。 |
| [03_prevalence_measure.md](05_EARLIER_EXPLORATIONS/genericity_team/03_prevalence_measure.md) | HISTORICAL | 区分Baire、prevalence、Haar-null与参数概率的量词。 |
| [04_semialgebraic_families.md](05_EARLIER_EXPLORATIONS/genericity_team/04_semialgebraic_families.md) | HISTORICAL | 保留有限参数坏选择/削圆相图作为研究历史与测试。 |
| [05_rleb_robustness.md](05_EARLIER_EXPLORATIONS/genericity_team/05_rleb_robustness.md) | HISTORICAL | 分析同证书平滑化与C0/强Hölder鲁棒性的区别。 |
| [06_math_stress.md](05_EARLIER_EXPLORATIONS/genericity_team/06_math_stress.md) | SUPERSEDED | 保留初审缺口和精确修补要求，追踪研究演变。 |
| [07_value_priorart.md](05_EARLIER_EXPLORATIONS/genericity_team/07_value_priorart.md) | HISTORICAL | 记录坏选择泛性方向当时的价值与先例评判。 |
| [08_final_synthesis.md](05_EARLIER_EXPLORATIONS/genericity_team/08_final_synthesis.md) | HISTORICAL | 综合早期坏类方向并记录修补说明和条件性结论。 |
| [01_terminology_map.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/01_terminology_map.md) | HISTORICAL | 对齐次单调等术语、RLEB接口与初值稳定性语言。 |
| [02_fixedpoint_retraction.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/02_fixedpoint_retraction.md) | HISTORICAL | 查极限回缩及统一迭代尾传递的正则性先例。 |
| [03_hypomonotone_proxregular.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/03_hypomonotone_proxregular.md) | HISTORICAL | 整理hypo/cohypo、prox-regular的步长和稳定性充分条件。 |
| [04_asymptotic_phase.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/04_asymptotic_phase.md) | HISTORICAL | 查渐近相位及极限映射光滑性对应。 |
| [05_partial_smoothness.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/05_partial_smoothness.md) | HISTORICAL | 分析部分光滑和切向条件可能怎样恢复稳定。 |
| [06_synthesis.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/06_synthesis.md) | CANONICAL | 初值稳定性专题的最终综合与明示充分接口。 |
| [07_synthesis_stress.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/07_synthesis_stress.md) | SUPERSEDED | 保留初值稳定性综合的独立初审与修补项。 |
| [08_synthesis_closure.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/08_synthesis_closure.md) | CANONICAL | 绑定最终综合哈希并关闭两项初审修补。 |
| [README.md](05_EARLIER_EXPLORATIONS/README.md) | CANONICAL | 解释三组历史探索与当前主问题的关系和审计状态。 |

## 06_RELATED_MANUSCRIPT_ASSETS

| 文件 | 标签 | 一句用途 |
| --- | --- | --- |
| [README.md](06_RELATED_MANUSCRIPT_ASSETS/README.md) | CANONICAL | 说明三份源ZIP的角色、优先阅读顺序和修订稿冻结身份。 |
| [solution_selection_final_audit.md](06_RELATED_MANUSCRIPT_ASSETS/solution_selection_final_audit.md) | HISTORICAL | 保存修订前solution-selection新稿最终审计和精确文献边界。 |
| [solution_selection_revised_v1_delivery.zip](06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip) | CANONICAL | 原样封存修订稿、PDF、TeX、复现与数学/主张/文件关闭记录。 |
| [RL_generalized_subregularity_assets_2026-09-14_v2.zip](06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RL_generalized_subregularity_assets_2026-09-14_v2.zip) | HISTORICAL | 原样保存9/14 RL、锥、Markov历史总资产和离线超边导航。 |
| [RLEB_PPA_submission_assets_2026-09-18.zip](06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip) | CANONICAL | 原样保存本次调用的9/18 RLEB–PPA专题基础稿。 |


