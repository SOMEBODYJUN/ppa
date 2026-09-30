# RL foundations 学术润色报告

## 1. scope_and_inputs

- 润色级别：`标准`，并对前置结构与局部论证衔接作保守优化。
- 冻结输入：`work/RL_foundations_draft.md`，SHA-256 `e24b415afe82ba6a98bd5fd7740bc25f5026da151934cd66d7cfbd22e5924815`。
- 审查输入：`work/rl_foundations_final_referee.md`；其结论为 `PASS FOR MATHEMATICAL FREEZE`，同时保留 novelty、optimality、universal order 与全文文献重叠等边界。
- 输出边界：只优化中文学术表达、前置结构、术语说明、编号对象标签与两处 editorial precision；不改定义量词、定义域、公式、常数、指数、假设、证明逻辑、claim strength、GX 判决或 novelty caveats。

## 2. specialist_findings

### 2.1 诊断

| 类型 | 诊断 | 处置 |
|---|---|---|
| 科学逻辑 | 独立 referee 未发现阻断性问题 | 锁定，不作科学内容修复 |
| 证据强度 | upper、two-sided exact exponent、exact Q-factor 已严格分层 | 原强度逐项保留 |
| 结构 | 缺少面向读者的摘要与术语入口 | 增补摘要、关键词与术语说明 |
| 术语 | 中英技术词有意混用，但对象标签与 process tone 不统一 | 保留通行技术词，统一中文编号对象与证明标签 |
| 风格 | 标题含 `canonical draft`，前言含“暂不做语言润色” | 改为研究标题与范围说明 |
| 格式 | 英文句点式 Proof/Remark/Verdict 标签与中文正文不一致 | 改为“证明/注/判定”及中文标点 |
| LaTeX | 冻结稿分隔符、标签与引用完备 | 711 个数学片段全部原样保留 |

### 2.2 主要前后差异

| 位置 | 原稿 | 终稿 | 理由 |
|---|---|---|---|
| 标题 | “RL 基础理论 canonical draft” | “RL 基础理论：Minty--Cayley 坐标、误差界与近端点迭代” | 删除过程腔，明确主题 |
| 前置内容 | 内部稿说明 | 范围说明、摘要、关键词、术语说明 | 改善读者定位；不新增科学主张 |
| 编号对象 | Definition/Theorem/Proposition 等 | 定义/定理/命题等 | 统一中文学术体例 |
| 证明标签 | Proof/Remark/Verdict | 证明/注/判定 | 统一语言与标点 |
| 定义 0.1 | graph restriction、空 restriction | 图限制、空的图限制 | 局部清晰度 |
| 定义 0.2 | “首先是 relations”“子 relation”“maps” | “先按关系定义”“子关系”“映射” | 保留 relation/map 边界并改善自然度 |
| 命题 7.2 证明 | 定义域只由“充分小 germ”隐含 | 明说重标度自变量留在函数定义域 | referee 指定的 editorial precision |
| 第 8 节末 | “isolated zero 时” | 限定为围绕同一局部孤立零点的充分小 localization | 避免脱离局部区域误读 |

### 2.3 术语控制

| 术语轴 | 终稿控制 |
|---|---|
| full / restricted relation | 完全/限制关系；自然域不升级 |
| all-pairs / anchored | 全对量词与锚定量词不互换 |
| named branch / full relation | 指定分支结论不升级为任意 full selection |
| coverage / exclusion / invariance | 存在性、full 唯一性、迭代合法性三者分离 |
| residual window / base neighborhood | 双局部化约定保留 |
| upper / two-sided exact / Q-factor | 主张强度逐级增强且不可互换 |

完整锁定项与差异见 `work/rl_foundations_locked_content_ledger.yaml`。

## 3. evidence_and_execution_status

| 标签 | 项目 | 状态 |
|---|---|---|
| VERIFIED_USER_MATERIAL | 冻结稿、独立 referee 报告 | 已完整审阅 |
| EXECUTED_LOCAL | 文件生成、哈希、数学片段、标签、引用、编号、表格与控制字符检查 | 已执行 |
| AI_INFERENCE | 语言问题分类、术语控制与保守润色判断 | 已明确标注为编辑判断 |
| PENDING_VERIFICATION | 文献全文重叠、novelty 与最优常数 | 未在本任务中验证，原 caveats 保留 |

## 4. deliverables

- `research/RL_foundations.md`：中文学术终稿。
- `work/rl_foundations_locked_content_ledger.yaml`：锁定内容、术语、不确定性与差异账本。
- `work/rl_foundations_polishing_report.md`：本报告。

## 5. limitations_and_risks

- RL 的正式公开命名仍未确定。
- 本任务未检索文献，未验证 Wang--Li--Ng 2023 或 Moursi--Vanderwerff 2025 的全文覆盖。
- 现有 constants 仍只是 sufficient route constants，不升级为 necessary 或 optimal。
- GX-071--GX-073 的当前判决保持不变；不外推 genericity、necessity、naturality 或 universality。
- 未新增定理、公式、引用、数据、统计分析或应用型 witness。

## 6. quality_checks

| 检查 | 结果 |
|---|---|
| 冻结源 SHA-256 | `e24b415afe82ba6a98bd5fd7740bc25f5026da151934cd66d7cfbd22e5924815`，未改变 |
| 终稿 SHA-256 | `0adf8ca1593148bebce576e9659f3da50e61a77880c0b311cbcc35d0dcbb4ebd` |
| 数学片段 | source 711 / final 711；顺序与内容逐项完全相同 |
| 数学片段序列 SHA-256 | source/final 均为 `cf896959aae5cdcead9d75989e45f8a3efcb7f718d2fffa33f3eacd0a10f5245` |
| inline delimiters | `\(` 512，`\)` 512 |
| display delimiters | `\[` 199，`\]` 199 |
| math braces | 711 个片段 unmatched 0 |
| equation tags | source 125 / final 125；顺序相同；重复 0 |
| tag-like references | 65；missing 0 |
| 编号对象 | 30；重复 0；引用缺失 0 |
| 对象分布 | 定义 5、定理 7、命题 8、引理 2、推论 5、例 3 |
| 定理与证明 | 7 个定理均有紧随其陈述的完整证明；缺失 0 |
| headings | 47；层级跳跃 0 |
| Markdown tables | 列数问题 0 |
| control / invisible characters | 0 / 0 |
| GX-071--GX-073 | 除中文 heading/verdict 标签外，与冻结块逐字相同 |
| legacy object labels | `### Definition/Theorem/...` 残留 0 |

## 7. SCI-Skills Expert Contract 1.0

```yaml
contract_version: "1.0"
expert_skill: "sci-skills-academic-polishing"
project_id: null
paper_family: null
stage_id: null
task_id: null
task_status: "COMPLETE"
inputs_reviewed:
  - "work/RL_foundations_draft.md @ sha256:e24b415afe82ba6a98bd5fd7740bc25f5026da151934cd66d7cfbd22e5924815"
  - "work/rl_foundations_final_referee.md"
outputs:
  - "research/RL_foundations.md"
  - "work/rl_foundations_locked_content_ledger.yaml"
  - "work/rl_foundations_polishing_report.md"
evidence_status:
  - label: "VERIFIED_USER_MATERIAL"
    item: "The frozen manuscript and independent referee report were reviewed."
  - label: "EXECUTED_LOCAL"
    item: "Hash, math-fragment, delimiter, brace, tag, reference, heading, numbering, proof-link, table, control-character, and GX-block checks were executed."
  - label: "AI_INFERENCE"
    item: "Language diagnosis and conservative editorial choices are specialist judgments."
  - label: "PENDING_VERIFICATION"
    item: "Novelty, literature overlap, and optimality remain outside this task and retain the manuscript's caveats."
assumptions:
  - "The independent referee verdict applies only to the exact frozen source hash."
  - "Technical English terms retained in the terminology note are controlled terms, not unedited process language."
  - "Exact equality of all math fragments is the primary guard for equations, constants, exponents, and mathematical notation."
author_input_needed:
  - "The public name of RL remains a future author decision; it does not block this polishing deliverable."
manual_actions: []
quality_checks:
  - "Frozen source hash matched the instructed SHA-256."
  - "All 711 math fragments matched the source exactly and in order."
  - "All 125 equation tags matched; duplicate and missing-reference counts were zero."
  - "All 30 numbered objects were present with no duplicate or missing object reference."
  - "All 7 theorems retained complete proofs."
  - "GX-071--GX-073 remained unchanged except for translated heading and verdict labels."
  - "Heading, table, delimiter, brace, control-character, and invisible-character checks passed."
conflicts: []
conflict_resolution_status: "NOT_REQUIRED"
merge_permission: "orchestrator_only"
recommended_next_action: "Have the SCI-Skills orchestrator verify the locked-content ledger and QA evidence, then decide whether to accept the polished artifact."
stage_acceptance_recommendation: "NOT_ASSESSED"
```

## 8. one_next_action

由 SCI-Skills orchestrator 核验锁定账本与 QA 证据，并决定是否接纳润色终稿。
