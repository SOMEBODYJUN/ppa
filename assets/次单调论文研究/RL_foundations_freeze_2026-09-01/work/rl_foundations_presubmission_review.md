# RL foundations 成品级预审与固定基线 readiness 报告

> 审查目的：判断 `research/RL_foundations.md` 是否可作为“后续 RL 研究的固定数学基础稿”，并将这一判断与“是否已是可投稿稿件”严格分开。  
> 审查边界：只审阅指定 bounded package；未检索新文献，未修改主文件，未预测编辑决定。  
> 终稿身份：`research/RL_foundations.md`，SHA-256 `0adf8ca1593148bebce576e9659f3da50e61a77880c0b311cbcc35d0dcbb4ebd`。

## 1. 执行摘要与裁决

| 用途 | 裁决 | 核心理由 |
|---|---|---|
| 后续 RL 研究的固定数学基础稿 | **READY** | 未发现阻塞冻结的实质数学错误；定义—定理—例证—边界账本闭合；polishing 未升级 claim strength，也未把 named branch、full relation、upper order、exact exponent 与 Q-factor 混同。仅余少量 MINOR/EDITORIAL 清晰度与版本管理问题。 |
| 对外投稿稿件 | **NOT_READY** | 当前文本有意不主张新颖性；缺正式公开命名、完整引言/贡献定位、正文引用与参考文献；关键全文重叠仍为 `PENDING_FULL_TEXT`。这属于投稿定位与完整性缺口，不是本数学基线的正确性缺口。 |

**阻塞冻结的实质数学问题：无。** 对固定基线用途，本审未发现 `BLOCKER`、`MAJOR` 或 `MODERATE` 问题；因此建议为 `PASS_CANDIDATE`，最终 stage acceptance 仍由 SCI-Skills orchestrator 决定。

## 2. Scope and inputs

### 2.1 已审输入

| 文件 | 用途 | 证据状态 |
|---|---|---|
| `research/RL_foundations.md` | 被审数学基础稿 | `VERIFIED_USER_MATERIAL`；当前 hash 已本地复核 |
| `work/rl_foundations_final_referee.md` | 冻结源的逐定理 proof referee 与 QA 证据 | `VERIFIED_USER_MATERIAL` |
| `work/rl_foundations_polishing_report.md` | 冻结源到终稿的编辑边界与 QA | `VERIFIED_USER_MATERIAL` |
| `work/rl_foundations_locked_content_ledger.yaml` | 公式、量词、常数、术语与 uncertainty 锁定账本 | `VERIFIED_USER_MATERIAL` |
| `work/rl_foundations_structure_claim_safe_matrix.md` | prior-art claim gate 与投稿定位边界 | `VERIFIED_USER_MATERIAL`；其中若干全文状态仍为 `PENDING_VERIFICATION` |

### 2.2 未执行事项

- 未检索或补充新文献。
- 未独立取得 Wang--Li--Ng 2023、Moursi--Vanderwerff 2025 或 Luque 1984 的未核全文。
- 未验证任何期刊的可变投稿要求，也未假设目标期刊。
- 未修改 `research/RL_foundations.md`，未把风险建议写成期刊强制要求。

## 3. Fact base

| 项目 | 审查事实 |
|---|---|
| paper family | `T`：理论/方法基础稿 |
| 当前 article type | 内部 canonical mathematical foundation / theory note；不是完整投稿 article |
| target | 未给定；期刊与栏目要求均未核验 |
| central claim | RL 条件在 Minty--Cayley 坐标中等价于自然域上的 reflector modulus；在明确区分 coverage、exclusion、invariance 与 named/full branch 后，可把 anchored estimate 和 full residual error bound 组合成局部 PPA 收敛上界 |
| 核心结构贡献 | (i) full/restricted 与 all-pairs/anchored 的量词账本；(ii) `gamma=1` 参数字典及 inverse/scaling；(iii) named-branch gauge PPA；(iv) isolated-zero q-flatness；(v) nonisolated two-anchor alignment composition；(vi) GX-071--GX-073 的可达性、保守性和 domain escape 边界 |
| data / statistics | 无；纯理论稿，无数据集、样本量、统计估计或经验实验 |
| methods | Hilbert 空间中的代数恒等式、局部量词分析、误差界复合、有限长度/不变性证明、显式反例与 sharpness sequence |
| validation | 前置 referee 对冻结 hash 的 30 个编号对象逐项重推并报告全通过；polishing 报告与锁定账本报告 711 个数学片段、125 个 equation tags 与全部量词/常数未变；本审复核当前终稿 hash、125 个 tags、30 个编号对象及关键 claim-strength 词链 |
| key results | 定理 1.1、2.1、4.2、6.1、7.1、7.4、8.2；推论 5.1--5.3、7.5；命题 7.6、8.3、9.1；GX-071--GX-073 |
| figures / tables | 无结果图；有依赖账本、术语判别表与 examples 总判决表。对纯理论基础稿不构成缺失 |
| limitations | 正式命名未锁；常数的 necessity/optimality 未证；两篇关键全文重叠待核；无 application-derived exact `theta q` witness；任意 full-resolvent selection 的收敛未声称 |
| unavailable supplements | 无声明必须存在而未提供的数学 supplement；prior-art 详细证据文件不是本次 bounded package 的审查对象 |

## 4. Lens 1 — Contribution

### 4.1 评价

作为固定数学基线，贡献定位清楚：它冻结“哪些结论在何种量词、自然域和 branch 条件下成立”，并系统记录不成立或尚未证明的更强说法。作为投稿稿，其广义新颖性与期刊受众价值尚未建立；claim-safe matrix 已主动承认这一点，因而不存在过度宣称，但也不能据此形成投稿贡献论证。

### 4.2 Concerns

| ID | 位置 | 证据 | 为什么重要 | 严重度 | minimum repair | ideal repair |
|---|---|---|---|---|---|---|
| C1 | 主稿开头、注 2.2、§11；claim-safe matrix C1--C9 与 final gate | 主稿明确“不主张新颖性”；matrix 判定广义新颖性不通过、投稿级贡献尚需 theorem package | 对固定基线这是诚实边界；对投稿稿则缺少可由同行判断的 central contribution thesis | **MAJOR（仅投稿用途）**；固定基线无缺陷 | 投稿分支中只选一条 claim-safe 窄贡献，并逐条映射到已有结果；当前基线保持不动 | 形成“现有定理—本文增量—必要假设—sharp witness—适用对象”的贡献表，并据此重写引言与讨论 |
| C2 | 注 2.2、§11(4)；matrix C12--C13 | Wang--Li--Ng 2023 与 Moursi--Vanderwerff 2025 的 theorem-level overlap 明列为待全文核验 | 未闭合的最近工作重叠使排他性、首次性或“未被覆盖”表述均不可投稿 | **MAJOR（仅投稿用途）** | 在任何投稿版中继续禁止排他性 wording，直至取得并核对全文 | 对两个来源做逐假设、逐结论、逐常数的 theorem comparison ledger，并将结果写入 related work |
| C3 | §11(5)；matrix C8--C9 与投稿级贡献 gate | 现有 exact `theta q` witness 为 reverse-calibrated，尚无 application-derived witness | 不影响定理真值或基线效用，但会削弱投稿时对自然性、重要性与受众价值的论证 | **MODERATE（仅投稿用途）** | 把该限制保留为 limitation，不把 naturality 当作已证 | 若研究目标需要，另行开发可追溯到实际 operator/problem class 的验证准则或自然例；这是一项风险型增强，不是已知期刊硬性要求 |

## 5. Lens 2 — Methods and mathematical rigor

### 5.1 通过的高风险检查

- 定理 1.1 的 relation/map 与自然域边界闭合；all-pairs 只给 restricted injectivity，full singleton 另需 exclusion。
- 定理 4.2 的 coverage、anchored estimate、output error bound 与 finite-length invariance 分工清楚；endpoint membership 未偷用 `S` closed、`T` continuous 或 graph closed。
- 推论 5.1--5.3 正确分开 `0<gamma<1, L>0`、`gamma=1` 和 `L=0`，没有把退化端点误标成 `gamma q` phase。
- §6--§8 没有把 moving anchor、fixed anchor、isolated zero 与 nonisolated alignment 相互替换。
- upper order、two-sided exact exponent 与 positive exact Q-factor 的证据门槛保持分层。
- GX-071--GX-073 的结论分别限定为 attainability、conservativeness 与 finite domain escape，没有外推 genericity、necessity 或 universality。

### 5.2 Concerns

| ID | 位置 | 证据 | 为什么重要 | 严重度 | minimum repair | ideal repair |
|---|---|---|---|---|---|---|
| M1 | 命题 7.3 与定理 7.4 的“在 `U` 上满足 q-power error bound”；对照定义 0.4 的 residual-window convention | 定义 0.4 已证明正 power bound 可在缩邻域后转成 neighborhood-only 版本；§7 的证明实际按“对所有 `y in U`”使用 | 数学链可由已打印的缩邻域等价闭合，但下游读者可能把 §7 的 `on U` 误读为仍带 residual window，继而漏掉一次 localization | **MINOR** | 在后续版本中加一句“`U` 已按定义 0.4 缩到 neighborhood-only power bound 成立” | 在 §7 开头统一声明本节对 power bound 使用哪一 convention，并给出一次明确 cross-reference |
| M2 | 固定基线的版本身份；当前 hash 只在 polishing report 与本报告中出现 | 当前主稿 hash 与 polishing report 完全一致；但主稿自身没有冻结版本标识 | 内容本身正确；风险在于后续研究若引用未标识的可变文件，可能无意跨版本复用定理 | **MINOR（版本管理）** | 由 orchestrator 在权威项目状态中登记当前 hash；无需改主稿 | 以后任何实质改动从该 hash 分支，并要求新 hash 重新走 bounded proof review |

未发现需要修改定理、证明、常数、指数或量词才能成立的数学 repair。

## 6. Lens 3 — Communication and package completeness

### 6.1 评价

润色后的摘要、术语入口和中文编号体系明显改善内部可读性。关键边界反复出现且彼此一致，尤其是 named/full、coverage/exclusion/invariance 和 upper/exact/Q-factor 三组。投稿完整性则明显不足：文本从范围与定义直接进入理论，没有完整的研究问题、贡献定位、文献综述、引用系统和参考文献。

### 6.2 Concerns

| ID | 位置 | 证据 | 为什么重要 | 严重度 | minimum repair | ideal repair |
|---|---|---|---|---|---|---|
| K1 | GX-072，式 (9.12a) 后 | “full `q`-MSR”只出现一次，未在定义 0.4 或术语说明中定义；正文其余部分使用 PEB/GEB | 熟悉不同 subregularity convention 的读者可能不确定该缩写是否严格等同于本文 full q-power error bound | **MINOR** | 后续版本把该处改成“full q-power error bound (PEB)”，或首次给出 q-MSR 的精确定义 | 全文只保留一个主术语，并在 related-work 版中把它与领域标准术语逐一定义对齐 |
| K2 | 主稿第 3 行；对照 GX-072/073 的 “maximal exponent/power” | 前置说明无修饰地写“不主张……最大性”，而 examples 确实证明例级 maximal Hölder exponent / maximal power | 不改变任何数学 claim，但“最大性”可能被读成既包括 operator maximality，也包括例级 sharp exponent，从而与后文表面冲突 | **MINOR** | 将前置边界理解并在后续版本明确为“不主张普适最优性、概念新颖性或文献优先权；例级已证 sharpness 除外” | 在术语说明中分开 maximal monotonicity、maximal exponent 与 universal optimality |
| K3 | 整体结构；claim-safe matrix final gate | 无标准引言、related work、正文引文与参考文献表；现有两个人名年份只作为 caveat 出现 | 投稿读者无法核验来源、判断增量或理解受众与问题动机 | **MAJOR（仅投稿用途）** | 投稿分支补齐引言、贡献列表、相关工作和可核验参考文献；在完成前维持 NOT_READY | 按 claim-safe matrix 逐 claim 建立 citation-to-claim map，并让每项外部事实有 primary-source 支撑 |
| K4 | 标题、前置说明、§11(1) | `RL` 明示为项目内部代号，公开命名未确定 | 内部基线足够稳定；对投稿而言，未命名对象无法形成可检索、可引用、可与既有术语对齐的公开叙事 | **MAJOR（仅投稿用途） / MINOR（固定基线）** | 固定基线继续保留内部代号；投稿前由作者确定公开名并完成术语冲突检查 | 选择与既有 semimonotonicity/subregularity 词汇兼容的名称，并在标题、定义和 related work 中统一 |
| K5 | 全文术语风格 | 中文正文保留大量 full/restricted、all-pairs、anchored、named branch 等英文控制词 | 术语轴本身没有误读，但投稿时会增加跨语言阅读成本 | **EDITORIAL** | 固定基线无需修改 | 投稿版建立双语符号表，并选定“中文主词 + 首次英文”或全英文的一致体例 |

## 7. Polishing claim-strength audit

### 7.1 核验结果

| 审计轴 | bounded evidence | 本审判定 |
|---|---|---|
| 终稿身份 | 当前 SHA-256 与 polishing report 的 `0adf...ebd` 一致 | **通过** |
| 数学对象 | polishing report/ledger 报告 711 个数学片段顺序与内容相同；本审在当前终稿复核 125 个 equation tags、30 个编号对象 | **通过**；未见公式、常数、指数或量词漂移 |
| claim-strength 层级 | 摘要称“条件性结论/收敛上界”；§5.4、§7.6、§9 明确分开 upper、two-sided 与 positive normalized limit | **通过**；没有把 upper bound 润色成 exact/Q-factor |
| branch scope | 定义 0.5、注 4.3、定理 7.4 后说明与 §10 账本均保留 named branch 不排除 remote selections | **通过**；没有把 named iteration 升级为 arbitrary full PPA |
| novelty/optimality | 前置说明、注 2.2、GX 判定与 §11 均保留 caveats；matrix 的危险 wording 未进入主稿 | **通过**；没有新增首次性或普适最优性 claim |
| 两处实质文字编辑 | 命题 7.2 明说 gauge 自变量留在定义域；§8 末限定 same locally isolated zero 的 localization | **通过**；二者收窄误读空间，没有增强结论 |
| 术语风险 | 唯一未完全闭合的是一次性 `q`-MSR 缩写，以及前置“最大性”的范围歧义 | **MINOR/EDITORIAL**；不构成 claim-strength 改变 |

### 7.2 总结

在本 bounded package 可见的证据范围内，polishing 是 **claim-safe** 的：数学片段、量词边界、常数、例证判决与 uncertainty 均保留；新增摘要没有把内部整理稿包装成新颖性论文。由于冻结源本身不在本次 bounded 输入清单中，本审不把 polishing report 的 source-to-final 字节比较冒充为重新执行；本审能独立确认的是当前终稿 hash、当前结构库存及终稿与 referee/ledger/matrix 的语义一致性。

## 8. Cross-review synthesis

### 8.1 Shared blockers and disagreements

- **固定数学基础稿 shared blockers：无。** 三个 lens 均未发现阻塞数学冻结的问题。
- **投稿 shared blockers：有。** Contribution 与 Communication lens 共同指向未完成的公开命名、贡献定位、引用/参考文献及关键全文重叠核验。
- **无证据冲突。** Methods lens 的 `READY` 与 Contribution/Communication lens 的投稿 `NOT_READY` 针对不同用途，不是互相矛盾的审稿意见。

### 8.2 Highest-risk claims

1. `gamma=1` tied semimonotonicity 只能作为已知参数切片，不能声称新类。
2. `theta q` 是条件性 uniform upper exponent；只有同一 sequence 的 joint saturation 才支持 exactness。
3. GX-071 只证 attainability，GX-072 只证 all-pairs exponent 可保守，GX-073 只证 one-step scale 不等于 convergence order。
4. named branch 的收敛不能改写为任意 full-resolvent selection 的收敛，除非另有 exclusion。
5. sufficient route constants 不能升级为 necessary 或 optimal constants。

### 8.3 Missing validation

| 项目 | 对固定基线是否阻塞 | 对投稿是否阻塞 |
|---|---|---|
| 两篇关键来源的全文 theorem overlap | 否，主稿已明确保留 | 是，阻塞排他性定位 |
| 正式公开命名 | 否 | 是 |
| 引言、related work、引用与参考文献 | 否 | 是 |
| application-derived natural witness | 否 | 否；但属于显著投稿风险/增强项 |
| journal-specific format/compliance | 否 | 待目标期刊确定后核验 |

### 8.4 Readiness

- **Foundation readiness：READY。** 可按当前 hash 固定，供后续 RL 定理、例证和验证工作引用。
- **Submission readiness：NOT_READY。** 这不是接受率或编辑决定预测；只是依据当前 package 对稿件完整性与证据定位的判断。
- **Stage recommendation：PASS_CANDIDATE（仅针对“固定数学基础稿”验收目标）。** Stage authority 保留给 orchestrator。

## 9. Prioritized revision plan

| 优先级 | 适用分支 | 工作包 | 预期工作量 | 是否阻塞当前数学冻结 |
|---|---|---|---|---|
| P0 | 固定基线 | 在权威项目状态登记当前 hash 与 READY 裁决；后续实质改动另开版本 | 很低 | 否；这是冻结动作本身 |
| P1 | 后续清晰度版 | 明确 §7 的 neighborhood-only power convention；定义/替换 `q`-MSR；限定前置“最大性”用语 | 低 | 否；均为 MINOR/EDITORIAL，改后产生新 hash |
| P2 | 独立投稿分支 | 确定公开名、目标受众和窄贡献；完成关键全文 comparison；补引言、related work、引用与参考文献 | 高 | 不影响当前基线；投稿前必须完成 |
| P3 | 可选研究增强 | 寻找 application-derived alignment criterion/witness，并对新定理重新 proof review | 高且不确定 | 否；属于新研究，不应并入当前冻结稿后跳过复审 |

## 10. Evidence and execution status

- `VERIFIED_USER_MATERIAL`：指定五个 bounded inputs 已完整审阅。
- `EXECUTED_LOCAL`：复核当前终稿 SHA-256；清点 125 个 equation tags、30 个编号对象、7 个定理，并检索关键 scope/claim-strength 词链。
- `AI_INFERENCE`：三 lens 的严重度、双用途 readiness、投稿风险和预计工作量属于本专家判断。
- `PENDING_VERIFICATION`：Wang--Li--Ng 2023、Moursi--Vanderwerff 2025、Luque 1984 的相应全文覆盖；novelty 与最优常数。
- `NOT_EXECUTED`：新文献检索、期刊要求核验、主稿修改、外部提交或任何实验/代码运行。

## 11. Author inputs

固定数学基线的接纳不需要新增作者输入。若未来启动投稿分支，需作者决定：公开名称、目标受众/期刊、唯一主贡献叙事，以及是否把 natural application witness 设为投稿前研究门槛。

## 12. SCI-Skills Expert Contract 1.0

```yaml
contract_version: "1.0"
expert_skill: "sci-skills-presubmission-review"
project_id: "monotonicity-regularity-seesaw-2026-09"
paper_family: "T"
stage_id: "T2"
task_id: null
task_status: "COMPLETE"
inputs_reviewed:
  - "research/RL_foundations.md @ sha256:0adf8ca1593148bebce576e9659f3da50e61a77880c0b311cbcc35d0dcbb4ebd"
  - "work/rl_foundations_final_referee.md @ sha256:2e9e05d789d0a365768281a27332819f9a7daa01c3ce9605e61bcf8779525864"
  - "work/rl_foundations_polishing_report.md @ sha256:435bcddeb0a8d5ad63ffeaf658058acfb0c633d4d3284e5fc7bd76cf589f6be0"
  - "work/rl_foundations_locked_content_ledger.yaml @ sha256:d6b92ec251c5d71e9284b493363f03e7856429100d7c7de368ed0655ee41b016"
  - "work/rl_foundations_structure_claim_safe_matrix.md @ sha256:ac2ed090bd4f7adad9b081a72ef7cc0c3ad278dc2b59597870bbf75332f4384e"
outputs:
  - "work/rl_foundations_presubmission_review.md"
evidence_status:
  - label: "VERIFIED_USER_MATERIAL"
    item: "All five bounded inputs were read in full; theorem, terminology, claim-boundary, polishing, and prior-art matrices were cross-checked."
  - label: "EXECUTED_LOCAL"
    item: "The current final hash, equation-tag count, numbered-object count, theorem inventory, and key claim-strength terminology were checked locally."
  - label: "AI_INFERENCE"
    item: "The three-lens severity judgments, purpose-separated readiness verdicts, and effort estimates are reviewer synthesis."
  - label: "PENDING_VERIFICATION"
    item: "Theorem-level overlap for Wang--Li--Ng 2023, Moursi--Vanderwerff 2025, and the relevant Luque 1984 full text remains pending; novelty and optimality are not verified."
  - label: "NOT_EXECUTED"
    item: "No new literature search, journal-requirement verification, manuscript edit, submission action, experiment, or external API operation was performed."
assumptions:
  - "The fixed-foundation acceptance target is distinct from external journal submission readiness."
  - "Project, paper-family, and stage identifiers are preserved from the bounded final-referee record; no new task_id was supplied."
  - "The polishing source-to-final exact-fragment comparison is treated as reviewed package evidence, not falsely claimed as independently rerun against an out-of-bound source file."
author_input_needed:
  - "None for accepting the fixed mathematical baseline."
  - "For a future submission branch: public name, target audience/venue, primary contribution thesis, and whether a natural application witness is required before submission."
manual_actions: []
quality_checks:
  - "Confirmed no BLOCKER, MAJOR, or MODERATE issue for the fixed-foundation use case."
  - "Rechecked relation/map, full/restricted, all-pairs/anchored, coverage/exclusion/invariance, and named/full-selection boundaries."
  - "Rechecked upper order, two-sided exact exponent, and positive exact Q-factor claim levels."
  - "Checked that GX-071--GX-073 retain only their stated attainability, conservativeness, and escape implications."
  - "Confirmed the current final hash matches the polishing report and the local inventory contains 125 equation tags and 30 numbered objects."
  - "Audited the two substantive polishing clarifications and found them claim-narrowing/clarifying rather than claim-strengthening."
  - "Separated fixed-foundation READY from submission NOT_READY without predicting an editorial decision."
  - "Modified neither the main manuscript nor any bounded input."
conflicts: []
conflict_resolution_status: "NOT_REQUIRED"
merge_permission: "orchestrator_only"
recommended_next_action: "由 SCI-Skills orchestrator 将 research/RL_foundations.md @ sha256:0adf8ca1593148bebce576e9659f3da50e61a77880c0b311cbcc35d0dcbb4ebd 登记为后续 RL 研究的固定数学基线。"
stage_acceptance_recommendation: "PASS_CANDIDATE"
```

## 13. one_next_action

**由 SCI-Skills orchestrator 将 `research/RL_foundations.md` @ SHA-256 `0adf8ca1593148bebce576e9659f3da50e61a77880c0b311cbcc35d0dcbb4ebd` 登记为后续 RL 研究的固定数学基线。**
