# 接手阅读路线

标签：`CANONICAL`（导航）。不建议从最早研究档案开始顺读。

## 路线 A：30 分钟理解当前任务

1. [QUICK_HANDOFF](QUICK_HANDOFF.md)：目标、尝试、前人工具与唯一重大停点。
2. [STATUS](../STATUS.md)：逐项区分已有定理、受限工具与未决总体结论。
3. [OPEN_PROBLEM](../OPEN_PROBLEM.md)：四个相连任务和验收形态。
4. 浏览 [正式交接](../01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md) §§2–5，重点 §5.4；完整证明转路线 B，无需在 30 分钟内严核全部细节或先读旧的全部 O/OP 清单。

## 路线 B：泛函分析/描述集合/拓扑

先读 [观测定理的独立证明](../01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md) §§1–2、6，再查：

- [中立母空间与公理](../02_NEUTRAL_PPA_SYSTEM/ppa_system_team/01_ambient_axioms.md)。
- [收敛拓扑](../02_NEUTRAL_PPA_SYSTEM/ppa_system_team/02_convergence_topology.md)。
- [无标签对象类别](../03_CLASSIFICATION_STAGE/ppa_classification_team/03_object_category.md)。
- [理想问题的精确版本](../01_CANONICAL_HANDOFF/mathematician_handoff/02_ideal_problem_formulation.md)。

优先判断：具体观测的类别保持、原对象侧可替代机制、Baire 分母是否退化。勿把一般 proper 映射定理当成项目观测已保纲。

## 路线 C：变分分析/PPA/误差界

先看 [证书嵌入审计](../02_NEUTRAL_PPA_SYSTEM/ppa_system_team/07_embedding_math_audit.md)，再查：

- [证书嵌入主稿](../02_NEUTRAL_PPA_SYSTEM/ppa_system_team/03_certificate_embeddings.md)。
- [完整原图与 resolvent 族](../02_NEUTRAL_PPA_SYSTEM/ppa_system_team/06_resolvent_family.md)。
- [冻结的比较规格](../03_CLASSIFICATION_STAGE/ppa_classification_team/01_frozen_denominator.md)。
- [结构变形工具](../03_CLASSIFICATION_STAGE/ppa_classification_team/02_structural_deformation.md)。
- [RLEB 基础源包](../06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip)：调用时优先查 `sections/theorem_spine.tex`，不预设重审整篇。

优先判断：新表示是否保留全纤维真实残差，strict compatibility 与固定宏观域能否同时闭合。

## 路线 D：动力系统/构造/连续选择

- [研究 idea 与已审种子引理](../01_CANONICAL_HANDOFF/mathematician_handoff/04_research_ideas.md)。
- [独立审计](../01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md) §§3–6。
- [结构变形](../03_CLASSIFICATION_STAGE/ppa_classification_team/02_structural_deformation.md)。
- [步长谱](../03_CLASSIFICATION_STAGE/ppa_classification_team/04_step_spectrum.md)。

先区分充分工具与必要结构：某个塔/后继选择单点不推出整个同尾层刚性；只获 `(1+epsilon)` 尾放宽时必须说明跨层转移。

## 路线 E：文献与原创性

从 [PRIOR_ART_MAP](../04_AUDITS_AND_PRIOR_ART/PRIOR_ART_MAP.md) 到 [最新文献边界](../01_CANONICAL_HANDOFF/mathematician_handoff/05_priorart_boundary.md)，再按拟证明的精确主定理回查原论文。各阶段来源见 [审计导航](../04_AUDITS_AND_PRIOR_ART/README.md)。

不把“研究空间/使用 Baire”当创新，也不因这些外层语言已知就否定完整图、真实 EB 与动力分层组合的潜在新内容。

## 什么时候看历史文件

- 要避免重复参数族/有限平滑化路线：看 `05_EARLIER_EXPLORATIONS/genericity_team/`。
- 要复用特殊比较层的正确构造：看 `comparison_space_team/`，同时读其 naturalness audit。
- 要追问极限选择稳定性：看 `initial_value_stability_team/`；当前类别主问题不以读完它为前置。
- 要追溯原研究谱系：看 9/14 原始总包；它不是本次主问题的第一阅读入口。
