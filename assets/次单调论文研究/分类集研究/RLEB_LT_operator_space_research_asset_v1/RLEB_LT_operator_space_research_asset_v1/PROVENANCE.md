# 来源、版本与审计关系

版本：v1 · 2026-09-20。源工作区：`/workspace/scratch/bf20ae56bc4b`。本表记录本轮如何整理既有文件，不宣称重做所有证明。

## 1. 内容保真与作者身份

- 55 个源文件/源包按字节复制；原数学报告不改公式、不改证明、不就地替换旧状态。新增文档单列编辑身份。
- 原报告大多只记录职责/工作组，未在文件中署可核的具体代理 ID；本表不由内容猜造作者或模型。具体生成身份可核时才写出。
- 新导航和索引的编辑代理为 `/root/research_asset_curator`；独立范围检查为 `/root/research_asset_scope_audit`。这两项是资产编辑/版本检查，不是一次新的全部数学审计。
- 逐文件机器数据见 [FILE_REGISTER.json](FILE_REGISTER.json)；交付内容哈希见 [MANIFEST.sha256](MANIFEST.sha256)。

## 2. 原始输入与冻结稿身份

| 原工作区路径 | 包内位置 | 角色/日期 | SHA256 |
| --- | --- | --- | --- |
| `upload/01-_RL-_2026-09-14_v2_-.zip` | [9/14历史总包](06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RL_generalized_subregularity_assets_2026-09-14_v2.zip) | 用户原资产；2026-09-14；RL＋锥＋Markov及离线导航 | `753a09e11eab5dbcf981fa418713cabd7676e09350bfca8ca4171f0b0168868d` |
| `upload/04-RLEB_PPA_-_2026-09-18.zip` | [9/18RLEB基础稿](06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip) | 用户源资产；2026-09-18；本次调用接口的默认基础 | `a377f9dd6a66f9281b1b98089c311b81923e908e541093768bfa9e9d1fe03871` |
| `solution_selection_revised_v1_delivery.zip` | [修订研究稿交付](06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip) | 此前修订发布的冻结交付；数学/主张/构建关闭记录在包内 | `cae4a31c80b5c29c21af3444a66e6a4de007cfac24db21ffd5a5f261fbb037f6` |

9/14包在当前对话的原上传名为“菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图.zip”；9/18包的内层根目录为“RLEB_PPA_投稿资产_2026-09-18”。两包分别有101个实文件及17个实文件（另3目录条目），内容不同，不是同一稿的不同压缩。9/18不全面替代9/14的全部历史资产。

旧 `mathematician_handoff_delivery.zip` 的原发布哈希为 `ae3696992dcc473256eab4b6b0d904d92845da7b3b24a10467eef58873510db4`；其当前源目录已完整纳入新包，因此不再嵌套重复旧ZIP。本包从源目录取快照，而不声称两个外层ZIP内容字节相同。

## 3. 状态冲突时怎样判读

1. **研究目标/阅读顺序：**以本包新 README、QUICK_HANDOFF、OPEN_PROBLEM 为入口；这不覆盖原证明的量词。
2. **当前技术综合：**以 `mathematician_handoff/07_final_handoff.md`、`06_math_audit.md` 及审后 `02`/`04` 为准；旧初稿不再是未决清单权威。
3. **中立底座：**`ppa_system_team/10_final_blueprint.md` 与专项证明/审计为准；`09_value_audit.md` 的energy规范化和局部图表旧未完成句已被后续关闭。
4. **分类策略：**`ppa_classification_team/07_stage_synthesis.md` 的仿射优先建议被降为工具路线；其已成立的变形/编码/谱模块没有因此撤销。
5. **初值稳定性专题：**`07_synthesis_stress.md` 的初审由 `08_synthesis_closure.md` 哈希绑定关闭；`06_synthesis.md` 实测哈希与关闭值一致。
6. **genericity专题：**`06_math_stress.md` 是MINOR_REPAIR初审；`08_final_synthesis.md` §7说明四项修补，但未发现独立最终closure，不能替它补造PASS。
7. **solution-selection专题：**外置最终审计审的是修订前稿；修订包的 `revision_math_closure.md`/`revision_priority_closure.md`/`final_package_QA.md` 才对应修订稿冻结状态。数学、宣告范围和文件QA三种放行不等于全球优先权关闭。

## 4. 源文件 → 交付文件

表内源路径相对原工作区；目的路径相对本包。具体代理未署名者只记录原工作组。审计列是既有记录的范围转述，不把所有文件统一判成PASS。

### 01_CANONICAL_HANDOFF

| 原路径 | 包内文件 | 标签 | 来源/生成身份 | 审计关系 |
| --- | --- | --- | --- | --- |
| `mathematician_handoff/01_full_handoff_draft.md` | [01_full_handoff_draft.md](01_CANONICAL_HANDOFF/mathematician_handoff/01_full_handoff_draft.md) | SUPERSEDED | 数学家交接工作组（源文件未署可核代理 ID） | 由同目录02/04审后修订、06审计及07综合覆盖当前状态 |
| `mathematician_handoff/02_ideal_problem_formulation.md` | [02_ideal_problem_formulation.md](01_CANONICAL_HANDOFF/mathematician_handoff/02_ideal_problem_formulation.md) | CANONICAL | 数学家交接工作组（源文件未署可核代理 ID） | 06复核；含审计后定理P加强 |
| `mathematician_handoff/03_obstruction_taxonomy.md` | [03_obstruction_taxonomy.md](01_CANONICAL_HANDOFF/mathematician_handoff/03_obstruction_taxonomy.md) | CANONICAL | 数学家交接工作组（源文件未署可核代理 ID） | 本轮06及07采用；并非全部为独立未决问题 |
| `mathematician_handoff/04_research_ideas.md` | [04_research_ideas.md](01_CANONICAL_HANDOFF/mathematician_handoff/04_research_ideas.md) | CANONICAL | 数学家交接工作组（源文件未署可核代理 ID） | 06核种子引理；路线覆盖和总体结论未证 |
| `mathematician_handoff/05_priorart_boundary.md` | [05_priorart_boundary.md](01_CANONICAL_HANDOFF/mathematician_handoff/05_priorart_boundary.md) | CANONICAL | 数学家交接工作组（源文件未署可核代理 ID） | 文献边界记录；非穷尽首创判决 |
| `mathematician_handoff/06_math_audit.md` | [06_math_audit.md](01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md) | CANONICAL | 数学家交接工作组（源文件未署可核代理 ID） | 两处范围修正；种子命题成立；总体差距未完成 |
| `mathematician_handoff/07_final_handoff.md` | [07_final_handoff.md](01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md) | CANONICAL | 数学家交接工作组（源文件未署可核代理 ID） | 采用06与02/04审后修订；不等于总体PASS |
| `mathematician_handoff/README.md` | [README.md](01_CANONICAL_HANDOFF/mathematician_handoff/README.md) | SUPERSEDED | 数学家交接工作组（源文件未署可核代理 ID） | 旧导航；非数学审计 |

### 02_NEUTRAL_PPA_SYSTEM

| 原路径 | 包内文件 | 标签 | 来源/生成身份 | 审计关系 |
| --- | --- | --- | --- | --- |
| `ppa_system_team/01_ambient_axioms.md` | [01_ambient_axioms.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/01_ambient_axioms.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 架构08列明范围内复核 |
| `ppa_system_team/02_convergence_topology.md` | [02_convergence_topology.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/02_convergence_topology.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 架构08范围内复核；不可扩大到任意Hilbert情形 |
| `ppa_system_team/03_certificate_embeddings.md` | [03_certificate_embeddings.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/03_certificate_embeddings.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 07专项PASS；固定图卡/接口边界 |
| `ppa_system_team/04_priorart.md` | [04_priorart.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/04_priorart.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 文献记录；优先权非总清关 |
| `ppa_system_team/05_stress_test.md` | [05_stress_test.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/05_stress_test.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 修订压力记录；与07/08合读 |
| `ppa_system_team/06_resolvent_family.md` | [06_resolvent_family.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/06_resolvent_family.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 独立代数/拓扑论证；范围见08 |
| `ppa_system_team/07_embedding_math_audit.md` | [07_embedding_math_audit.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/07_embedding_math_audit.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | PASS，附明确接口边界 |
| `ppa_system_team/08_architecture_audit.md` | [08_architecture_audit.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/08_architecture_audit.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 修补后PASS，仅明示有限维/共同域/量词范围 |
| `ppa_system_team/09_value_audit.md` | [09_value_audit.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/09_value_audit.md) | HISTORICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | energy/局部图表旧句由03/07/08/10替代 |
| `ppa_system_team/10_final_blueprint.md` | [10_final_blueprint.md](02_NEUTRAL_PPA_SYSTEM/ppa_system_team/10_final_blueprint.md) | CANONICAL | 中立PPA体系工作组（源文件未署可核代理 ID） | 底座权威；当前未决任务以后续交接为准 |

### 03_CLASSIFICATION_STAGE

| 原路径 | 包内文件 | 标签 | 来源/生成身份 | 审计关系 |
| --- | --- | --- | --- | --- |
| `ppa_classification_team/01_frozen_denominator.md` | [01_frozen_denominator.md](03_CLASSIFICATION_STAGE/ppa_classification_team/01_frozen_denominator.md) | CANONICAL | PPA分类构建工作组（源文件未署可核代理 ID） | 05§9范围内交叉复核 |
| `ppa_classification_team/02_structural_deformation.md` | [02_structural_deformation.md](03_CLASSIFICATION_STAGE/ppa_classification_team/02_structural_deformation.md) | CANONICAL | PPA分类构建工作组（源文件未署可核代理 ID） | 05范围内通过；同尾/宏观同域/母空间位置未闭合 |
| `ppa_classification_team/03_object_category.md` | [03_object_category.md](03_CLASSIFICATION_STAGE/ppa_classification_team/03_object_category.md) | CANONICAL | PPA分类构建工作组（源文件未署可核代理 ID） | 05范围内复核；不外推任意未控域外图 |
| `ppa_classification_team/04_step_spectrum.md` | [04_step_spectrum.md](03_CLASSIFICATION_STAGE/ppa_classification_team/04_step_spectrum.md) | CANONICAL | PPA分类构建工作组（源文件未署可核代理 ID） | 05范围内复核；优先权未清关 |
| `ppa_classification_team/05_obstruction_audit.md` | [05_obstruction_audit.md](03_CLASSIFICATION_STAGE/ppa_classification_team/05_obstruction_audit.md) | CANONICAL | PPA分类构建工作组（源文件未署可核代理 ID） | §9为该阶段精确放行范围 |
| `ppa_classification_team/06_priorart_tools.md` | [06_priorart_tools.md](03_CLASSIFICATION_STAGE/ppa_classification_team/06_priorart_tools.md) | CANONICAL | PPA分类构建工作组（源文件未署可核代理 ID） | 文献/工具适用性记录 |
| `ppa_classification_team/07_stage_synthesis.md` | [07_stage_synthesis.md](03_CLASSIFICATION_STAGE/ppa_classification_team/07_stage_synthesis.md) | HISTORICAL | PPA分类构建工作组（源文件未署可核代理 ID） | 成果未撤销；策略由最新07交接替代 |

### 04_AUDITS_AND_PRIOR_ART

| 原路径 | 包内文件 | 标签 | 来源/生成身份 | 审计关系 |
| --- | --- | --- | --- | --- |
| `research_asset_scope_audit.md` | [ASSET_SCOPE_AUDIT.md](04_AUDITS_AND_PRIOR_ART/ASSET_SCOPE_AUDIT.md) | CANONICAL | /root/research_asset_scope_audit | 资产范围/版本QA，不是新数学审计 |

### 05_EARLIER_EXPLORATIONS

| 原路径 | 包内文件 | 标签 | 来源/生成身份 | 审计关系 |
| --- | --- | --- | --- | --- |
| `comparison_space_team/01_exact_translation.md` | [01_exact_translation.md](05_EARLIER_EXPLORATIONS/comparison_space_team/01_exact_translation.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 可用接口工具；当前转换用体系03/07 |
| `comparison_space_team/02_monotone_category_literature.md` | [02_monotone_category_literature.md](05_EARLIER_EXPLORATIONS/comparison_space_team/02_monotone_category_literature.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 文献记录；最新边界用交接05 |
| `comparison_space_team/03_holder_lipschitz_category.md` | [03_holder_lipschitz_category.md](05_EARLIER_EXPLORATIONS/comparison_space_team/03_holder_lipschitz_category.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 06修补后范围内通过 |
| `comparison_space_team/04_comparison_space_architecture.md` | [04_comparison_space_architecture.md](05_EARLIER_EXPLORATIONS/comparison_space_team/04_comparison_space_architecture.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 06范围内通过；08限制母空间代表性 |
| `comparison_space_team/05_meagreness_feasibility.md` | [05_meagreness_feasibility.md](05_EARLIER_EXPLORATIONS/comparison_space_team/05_meagreness_feasibility.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 06范围内通过；不是中立母空间总定理 |
| `comparison_space_team/06_math_audit.md` | [06_math_audit.md](05_EARLIER_EXPLORATIONS/comparison_space_team/06_math_audit.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 修补后PASS；R1–R4关闭，范围见§§7–8 |
| `comparison_space_team/07_priorart_value_audit.md` | [07_priorart_value_audit.md](05_EARLIER_EXPLORATIONS/comparison_space_team/07_priorart_value_audit.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 非当前中立体系最终优先权判决 |
| `comparison_space_team/08_naturalness_audit.md` | [08_naturalness_audit.md](05_EARLIER_EXPLORATIONS/comparison_space_team/08_naturalness_audit.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 受限层自然性边界 |
| `comparison_space_team/09_final_synthesis.md` | [09_final_synthesis.md](05_EARLIER_EXPLORATIONS/comparison_space_team/09_final_synthesis.md) | HISTORICAL | 早期比较空间工作组（源文件未署可核代理 ID） | 总问题口径由中立体系及新交接替代 |
| `genericity_team/01_operator_space.md` | [01_operator_space.md](05_EARLIER_EXPLORATIONS/genericity_team/01_operator_space.md) | HISTORICAL | 早期坏选择泛性工作组（源文件未署可核代理 ID） | 06提修补；08§7说明处理，未见独立终审closure |
| `genericity_team/02_baire_literature.md` | [02_baire_literature.md](05_EARLIER_EXPLORATIONS/genericity_team/02_baire_literature.md) | HISTORICAL | 早期坏选择泛性工作组（源文件未署可核代理 ID） | 后续文献链有更直接BRZ对照 |
| `genericity_team/03_prevalence_measure.md` | [03_prevalence_measure.md](05_EARLIER_EXPLORATIONS/genericity_team/03_prevalence_measure.md) | HISTORICAL | 早期坏选择泛性工作组（源文件未署可核代理 ID） | 06提修补；08§7说明处理 |
| `genericity_team/04_semialgebraic_families.md` | [04_semialgebraic_families.md](05_EARLIER_EXPLORATIONS/genericity_team/04_semialgebraic_families.md) | HISTORICAL | 早期坏选择泛性工作组（源文件未署可核代理 ID） | 不作总体类大小证据 |
| `genericity_team/05_rleb_robustness.md` | [05_rleb_robustness.md](05_EARLIER_EXPLORATIONS/genericity_team/05_rleb_robustness.md) | HISTORICAL | 早期坏选择泛性工作组（源文件未署可核代理 ID） | 受限鲁棒性工具 |
| `genericity_team/06_math_stress.md` | [06_math_stress.md](05_EARLIER_EXPLORATIONS/genericity_team/06_math_stress.md) | SUPERSEDED | 早期坏选择泛性工作组（源文件未署可核代理 ID） | 原状态MINOR_REPAIR；08§7说明四项修补，无独立最终PASS文件 |
| `genericity_team/07_value_priorart.md` | [07_value_priorart.md](05_EARLIER_EXPLORATIONS/genericity_team/07_value_priorart.md) | HISTORICAL | 早期坏选择泛性工作组（源文件未署可核代理 ID） | 非当前认证覆盖问题终判 |
| `genericity_team/08_final_synthesis.md` | [08_final_synthesis.md](05_EARLIER_EXPLORATIONS/genericity_team/08_final_synthesis.md) | HISTORICAL | 早期坏选择泛性工作组（源文件未署可核代理 ID） | CONDITIONAL；参数优先路线已不再采用 |
| `initial_value_stability_team/01_terminology_map.md` | [01_terminology_map.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/01_terminology_map.md) | HISTORICAL | 初值稳定性工作组（源文件未署可核代理 ID） | 专题背景，非当前大小主问题 |
| `initial_value_stability_team/02_fixedpoint_retraction.md` | [02_fixedpoint_retraction.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/02_fixedpoint_retraction.md) | HISTORICAL | 初值稳定性工作组（源文件未署可核代理 ID） | 文献与充分条件工具 |
| `initial_value_stability_team/03_hypomonotone_proxregular.md` | [03_hypomonotone_proxregular.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/03_hypomonotone_proxregular.md) | HISTORICAL | 初值稳定性工作组（源文件未署可核代理 ID） | 专题07/08列明通过项 |
| `initial_value_stability_team/04_asymptotic_phase.md` | [04_asymptotic_phase.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/04_asymptotic_phase.md) | HISTORICAL | 初值稳定性工作组（源文件未署可核代理 ID） | 原始文献对象区分工具 |
| `initial_value_stability_team/05_partial_smoothness.md` | [05_partial_smoothness.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/05_partial_smoothness.md) | HISTORICAL | 初值稳定性工作组（源文件未署可核代理 ID） | 候选接口；不宣称最弱条件 |
| `initial_value_stability_team/06_synthesis.md` | [06_synthesis.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/06_synthesis.md) | CANONICAL | 初值稳定性工作组（源文件未署可核代理 ID） | 08哈希绑定SYNTHESIS_PASS，仅专题范围 |
| `initial_value_stability_team/07_synthesis_stress.md` | [07_synthesis_stress.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/07_synthesis_stress.md) | SUPERSEDED | 初值稳定性工作组（源文件未署可核代理 ID） | 初审MINOR_REPAIR由08关闭 |
| `initial_value_stability_team/08_synthesis_closure.md` | [08_synthesis_closure.md](05_EARLIER_EXPLORATIONS/initial_value_stability_team/08_synthesis_closure.md) | CANONICAL | 初值稳定性工作组（源文件未署可核代理 ID） | SYNTHESIS_PASS；非最弱性/全球优先权证明 |

### 06_RELATED_MANUSCRIPT_ASSETS

| 原路径 | 包内文件 | 标签 | 来源/生成身份 | 审计关系 |
| --- | --- | --- | --- | --- |
| `solution_selection_final_audit.md` | [solution_selection_final_audit.md](06_RELATED_MANUSCRIPT_ASSETS/solution_selection_final_audit.md) | HISTORICAL | solution-selection终审工作组（源文件未署可核代理 ID） | ABC_PASS_AFTER_REPAIR/PARTIAL-PRIOR；修订后状态看交付zip内closure |
| `solution_selection_revised_v1_delivery.zip` | [solution_selection_revised_v1_delivery.zip](06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip) | CANONICAL | solution-selection修订/交付工作组（源文件未署可核代理 ID） | 内含REVISION_MATH_PASS、REVISION_CLAIMS_PASS、PACKAGE_QA_PASS；非全球首创 |
| `upload/01-_RL-_2026-09-14_v2_-.zip` | [RL_generalized_subregularity_assets_2026-09-14_v2.zip](06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RL_generalized_subregularity_assets_2026-09-14_v2.zip) | HISTORICAL | 用户上传来源；包内各资产按原署名 | 用户源快照；不以旧PENDING评判新稿 |
| `upload/04-RLEB_PPA_-_2026-09-18.zip` | [RLEB_PPA_submission_assets_2026-09-18.zip](06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip) | CANONICAL | 用户上传来源；包内各资产按原署名 | 用户源快照；当前仅核实际调用接口 |

## 5. 本轮新增文件

| 文件 | 编辑身份 | 作用/状态 |
| --- | --- | --- |
| [00_START_HERE/QUICK_HANDOFF.md](00_START_HERE/QUICK_HANDOFF.md) | /root/research_asset_curator | 用短篇说明目标、前人工具、尝试、当前停点及要什么idea。 |
| [00_START_HERE/READING_ROUTES.md](00_START_HERE/READING_ROUTES.md) | /root/research_asset_curator | 提供30分钟入口与按学科分工的证明阅读路径。 |
| [01_CANONICAL_HANDOFF/README.md](01_CANONICAL_HANDOFF/README.md) | /root/research_asset_curator | 解释当前技术交接文件的优先级和旧初稿地位。 |
| [02_NEUTRAL_PPA_SYSTEM/README.md](02_NEUTRAL_PPA_SYSTEM/README.md) | /root/research_asset_curator | 指向体系底座并说明旧价值稿被关闭的技术状态。 |
| [03_CLASSIFICATION_STAGE/README.md](03_CLASSIFICATION_STAGE/README.md) | /root/research_asset_curator | 保留分类模块但降级旧仿射优先策略。 |
| [04_AUDITS_AND_PRIOR_ART/CLAIM_BOUNDARY_REGISTER.md](04_AUDITS_AND_PRIOR_ART/CLAIM_BOUNDARY_REGISTER.md) | /root/research_asset_curator | 逐项对照可用主张、禁止外推与证明证据。 |
| [04_AUDITS_AND_PRIOR_ART/PRIOR_ART_MAP.md](04_AUDITS_AND_PRIOR_ART/PRIOR_ART_MAP.md) | /root/research_asset_curator | 按原记录对照前人工具、精确文献位置和本项目缺桥。 |
| [04_AUDITS_AND_PRIOR_ART/README.md](04_AUDITS_AND_PRIOR_ART/README.md) | /root/research_asset_curator | 导航各阶段审计正文，避免将不同PASS合并。 |
| [05_EARLIER_EXPLORATIONS/README.md](05_EARLIER_EXPLORATIONS/README.md) | /root/research_asset_curator | 解释三组历史探索与当前主问题的关系和审计状态。 |
| [06_RELATED_MANUSCRIPT_ASSETS/README.md](06_RELATED_MANUSCRIPT_ASSETS/README.md) | /root/research_asset_curator | 说明三份源ZIP的角色、优先阅读顺序和修订稿冻结身份。 |
| [CHANGELOG.md](CHANGELOG.md) | /root/research_asset_curator | 记录本次资产整理的编排和范围变化。 |
| [FILE_INDEX.md](FILE_INDEX.md) | /root/research_asset_curator | 为每个交付文件给出状态标签和一句用途，支持定位。 |
| [FILE_REGISTER.json](FILE_REGISTER.json) | /root/research_asset_curator | 提供逐文件来源、标签、用途、审计状态的机器可读索引。 |
| [MANIFEST.sha256](MANIFEST.sha256) | /root/research_asset_curator | 给出所有交付文件（不含自身）的完整性校验值。 |
| [OPEN_PROBLEM.md](OPEN_PROBLEM.md) | /root/research_asset_curator | 把求助集中为一个主桥梁及四个相连接口和验收标准。 |
| [PROVENANCE.md](PROVENANCE.md) | /root/research_asset_curator | 记录源到交付映射、身份、代理可核程度和审计链。 |
| [README.md](README.md) | /root/research_asset_curator | 项目目标、当前主桥梁、阅读路径、版本标签与接手总入口。 |
| [STATUS.md](STATUS.md) | /root/research_asset_curator | 登记已核结果、适用范围、未完成主问题与禁止外推。 |

## 6. 保留的历史链接与刻意排除项

旧数学报告里的 `sandbox:/workspace/…` 绝对链接、短路径和编号保持原样，避免篡改历史正文；它们是出处记录，不保证换机器后可点击。通过第4节源→交付映射与 FILE_INDEX 可在新包定位同一资源。本轮新入口的本地链接全部采用包内相对路径。

未额外复制下载的第三方整本论文PDF/PS/TXT、同一稿的A/B/C重复解包、TeX工具链和编译缓存、页面PNG、无关旁支展开目录。原用户9/14 ZIP内部所含素材则原样保存，不逐项改写或删除。

没有删除工作区原件，也没有将新包写回替换用户原ZIP。本包是新编排的研究快照；以后新增证明请新建版本并更新本索引、状态和哈希，不把历史报告就地改成“早已证明”。

