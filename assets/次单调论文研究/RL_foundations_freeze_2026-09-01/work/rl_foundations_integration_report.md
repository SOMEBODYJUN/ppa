# RL foundations integration report

> 对应输出：work/RL_foundations_draft.md。  
> 本报告记录结构取舍、referee 反向修补与待审问题；不构成新颖性或投稿阶段判定。

## 1. 任务完成状态

已生成一份自洽、量词闭合、暂未语言润色的 canonical theorem package。
正文保留 RL 作为内部代号，并明确正式公开命名未锁。SCI contract、过程性
decision log 与大段 prior-art bookkeeping 均留在本报告，不进入基础稿正文。

### 已审输入

- work/rl_foundations_integration_blueprint.md
- work/rl_foundations_definitions.md
- work/rl_foundations_ppa_theorem.md
- work/rl_foundations_anchor_theorems.md
- work/rl_foundations_alignment_sharpness.md
- work/rl_foundations_structure_claim_safe_matrix.md
- work/rl_proof_referee.md
- work/rl_foundations_referee_quantifiers.md
- work/rl_foundations_referee_constants.md
- work/rl_foundations_referee_structure.md
- research/example_properties.md，仅核对 GX-071--GX-074

未读取其他项目材料来补写数学主张。

## 2. 入选结构

| 顺序 | 入选模块 | 冻结的 claim strength |
|---:|---|---|
| 0 | ambient、distance、Minty/Cayley、relation、RL/gauge/branch 定义 | 完整量词与 convention |
| 1 | RL--IP、restricted Minty injectivity、reflector、firm-type 与 Cayley pullback | 精确等价；只在自然域 |
| 2 | coverage、exclusion、invariance | 三个独立逻辑层 |
| 3 | \(\gamma=1\) tied dictionary、inverse、output scaling | 精确代数 |
| 4 | all-pairs RL branch verifier | all-pairs 是充分 verifier，不是 PPA 最弱假设 |
| 5 | named-branch local gauge--PPA | 条件收敛、显式 margin、finite length、endpoint membership |
| 6 | power phase corollaries | upper order；临界常数仅充分 |
| 7 | moving output-anchor reflection | superlinear gauge 下的 moving-center law |
| 8 | fixed-anchor power/general-gauge flatness | branchwise 等价；same-gauge 需 dilation stability |
| 9 | isolated-zero named PPA | \(q\)-upper recurrence；另列 exact Q-factor 判据 |
| 10 | nonisolated alignment/drift composition | \(\theta q\) uniform upper exponent |
| 11 | joint-saturation sharpness 与 GX-071--073 | attainability、separation、escape 三类判决 |
| 12 | theorem dependency / assumption ledger | 正文末尾集中冻结 |

## 3. 合并决策

### 3.1 定义层与结构层

1. 将 full、restricted、graph-local、all-pairs、anchored 分开定义；
   未保留含糊的 “locally RL” 或 “selection-wise AFNE”。
2. firm-type inequality 不另立新对象，而作为同一 Cayley inequality
   的等价表示。
3. restricted uniqueness、input coverage、full-branch exclusion 与
   orbit invariance 分成四个判断，不用一个 “local PPA” 词组包办。
4. 空图 convention 冻结为 all-pairs 全称命题真空成立；算法定理仍要求
   \(S\ne\varnothing\) 与 coverage。
5. power RL 统一采用 \(L\ge0\)。\(L=0\) 单列为 constant-reflector
   degeneration，此时 \(\gamma\) 不可识别。

### 3.2 Gauge 与 power interface

1. 采用 residual-windowed local gauge error bound 的公开名称，明确
   base neighborhood 与 residual cutoff 是两重 locality。
2. 补入 positive power gauge 的缩邻域等价：windowed power bound 可在
   \(U'\subset U\cap B(\bar u,\rho\delta^q)\) 上升级为
   neighborhood-only bound。
3. 将 PPA 的 E 直接写成 orbit-output relative assumption；若从标准
   at-\((\bar u,0)\) local GMSR 导入，必须另验
   \(Tx\in U_{\rm EB}\) 及 residual cutoff。
4. full residual 与 selected graph residual 不混写；branchwise converse
   只在 residual completeness 下给出。

### 3.3 PPA theorem

1. 以 B/A/E 三层组织主定理：
   B 是 named Minty coverage，A 是 epsilon-nearest anchored estimate，
   E 只在 selected output 使用。
2. 保留精确 \(1/2\) step bound、residual bound 与 gauge recurrence。
3. 使用 strict finite-length margin 证明 orbit invariance，而不假设
   \(T(U)\subset U\)。
4. endpoint-wide A 在 Cauchy limit 处重新调用，故无需另加
   \(S\) closed 或 \(T\) continuous；同时明确
   \(A+B\Rightarrow U\cap\overline S=U\cap S\)。
5. full-resolvent arbitrary selection 只在另有 branch exclusion 时成立。

### 3.4 Rate 与 sharpness

冻结三层术语：

1. \(r_{k+1}=O(r_k^p)\)：upper order；
2. \(r_{k+1}=\Theta(r_k^p)\)：two-sided exact exponent；
3. \(r_{k+1}/r_k^p\to c\in(0,\infty)\)：exact Q-order with factor \(c\)。

GX-071 达到第三层且 factor 为 1；GX-072 只冻结第二层，不声称
normalized quotient 收敛。critical coefficients 只称 sufficient。

### 3.5 Fixed 与 moving anchors

1. moving-anchor theorem 使用 output-nearest 或
   \(o(\|w\|)\)-accurate output-near zero；不替换成 fixed/input-nearest
   anchor。
2. fixed-anchor power flatness保留
   branch residual \(\Leftrightarrow J\)-flatness
   \(\Leftrightarrow\) centered reflection defect。
3. general gauge 只冻结 rescaled forms
   \(\beta(2\|x-p\|/\lambda)\) 与
   \(\alpha(2\lambda\|w\|)\)；literal same-gauge form 另需
   fixed-dilation stability。阶梯 gauge 反例仅作短 remark。
4. isolated superlinear-gauge named PPA 补成独立 corollary：
   \[
   \|Tx-p\|\le\psi(2\|x-p\|/\lambda)=o(\|x-p\|).
   \]

### 3.6 Nonisolated alignment

1. 采用非循环 quantities
   \(a_J(x)=d(x,P_S(Jx))\) 与 nearest-anchor drift
   \(\delta_J(x)=d(P_S(x),P_S(Jx))\)。
2. 显式定义 set-to-set distance，避免 point-to-set notation overload
   未声明。
3. exact-projection theorem 与 approximate-anchor theorem 分开；
   “无 proximinality”版本明确要求相关 approximate projection set
   非空，或充分地 \(e(t)>0\)。
4. 保留 \(a_J(x)=\lambda\|w(x)\|(1+o(1))\) 的 limiting caveat：
   composition 是 step scale 的几何分解，不包装成独立深层分类。

## 4. 剔除或降格的内容

| 候选内容 | 决策 | 理由 |
|---|---|---|
| RL 自动满域、maximal 或 graph closed | 剔除 | Minty injectivity 不给 range/closedness |
| arbitrary full-resolvent PPA | 降为 named branch | local restriction 不排除 remote selections |
| “充分靠近 \(S\)”即 invariant | 剔除 | 非孤立切向 drift；GX-071 |
| \(\gamma q\) universal exact order | 剔除 | 只是一条 upper route；GX-072 严格分离 |
| critical coefficient necessary/sharp | 剔除 | 仅由当前 triangle/residual route 得到 |
| arbitrary \(o(t)\) gauge 的 literal same-gauge equivalence | 剔除 | 缺 fixed-dilation stability；阶梯 gauge 反例 |
| favorable selected residual law 即 full MSR | 剔除 | 需 residual completeness |
| fixed/input-nearest anchor 替代 output-nearest anchor | 剔除 | nonisolated counterexamples否定 |
| one-step \(\Theta(r^\alpha)\) 即 convergence rate | 剔除 | GX-073 finite escape |
| universal monotonicity--regularity seesaw | 剔除 | 无 theorem-level 证据 |
| 首次 higher-order MSR/PPA/nonisolated superlinear/alignment | 剔除 | 已知或邻近文献边界；不作优先权 claim |
| 独立 SCI contract 写入理论正文 | 剔除 | contract 仅保留在 integration report |

## 5. Referee 修补落实表

### 5.1 Proof-referee 主修补

| Referee objection | Draft resolution |
|---|---|
| RL 不给 resolvent existence | Definition 0.5 + B 明列 coverage |
| local RL 不控制 remote full branch | (EX) 与 named iteration 分开 |
| distance-to-\(S\) 小不保证 localization | strict step-budget margin |
| limit 只知落在 \(\overline S\) | endpoint-wide A+B 重用一步估计 |
| \(\gamma q\) 被误称 exact | 三层 rate 术语与 GX-072 判决 |

### 5.2 Quantifier referee Q-01--Q-06

| ID | 处理 |
|---|---|
| Q-01 | 命名 residual-windowed gauge，并补 power shrinkage equivalence |
| Q-02 | 全文统一 \(L\ge0\) |
| Q-03 | 冻结空图真空 all-pairs convention |
| Q-04 | scaling 写成 \(F@\lambda\leftrightarrow cF@(\lambda/c)\) 与 \(cF@\lambda\leftrightarrow F@(c\lambda)\) |
| Q-05 | 补 \((0,1)\times\{0\}\) 的统一非闭性见证 |
| Q-06 | tail proof 明写 \(r_{k+j}\le\theta^jr_k\) 再求和 |

### 5.3 Constant referee R1--R4

| ID | 处理 |
|---|---|
| R1 | \(L=0\) 单列 \(r_+\le\rho(2\lambda)^{-q}r^q\)，phase 由 \(q\) 控制 |
| R2 | upper order / two-sided exponent / exact Q-factor 三分 |
| R3 | 明写 \(A+B\Rightarrow U\cap\overline S=U\cap S\) |
| R4 | 明写 local GMSR 导入 E 需 output base-neighborhood membership |

### 5.4 Structure referee STR-M01--M02、D01--D07、N01--N04

| ID | 处理 |
|---|---|
| STR-M01 | Proposition 8.3 明列 \(P_S^{e(t)}(Jx)\ne\varnothing\)；无 proximinality 时要求 attained \(t>0\) 上 \(e(t)>0\)，并核 gauge argument domain |
| STR-M02 | GX-072 分段定义 \(h(0)=0\)；GX-073 分段定义 \(R(0)=0\) |
| STR-D01 | §8 固定整个 envelope family \(\mathcal F_{r_0}\)，并对每个 family member 假设 \(P_S(x),P_S(Jx)\ne\varnothing\) |
| STR-D02 | 所有非负 empty sup 约定为 \(0\)；显式要求 \(\mathcal A_J(r)<\lambda\eta_\psi/2\) 及每个 \(\psi\)-argument 落在 \([0,\eta_\psi)\) |
| STR-D03 | Proposition 7.3 standalone 写明 \(q>0\) |
| STR-D04 | Proposition 7.6 standalone 写明 \(q>1\)、Theorem 7.4 invariant named nonterminating orbit 与 \(w_k\to0\) |
| STR-D05 | GX-072 打印 \(s_n,t_n,x_n,y_n\) phase-extremum points、normalized reflector limit 与 generated \(F\) 的 full \(q\)-MSR 两行证明 |
| STR-D06 | GX-073 打印 phase-extremum limit、uniform all-preimage residual ratio、exact linear modulus \(1\) 与 finite escape |
| STR-D07 | GX-072 用 \(u=Jz,\ w=z-u=z+o(\|z\|)\) 把 map scaling 转为 full \(q\)-MSR，并用 phase-zero inputs 排除 \(p>q\) |
| STR-N01 | 三例前统一 signed power；GX-071--073 明列 \(\lambda=1\) |
| STR-N02 | general gauges、isolated gauge-PPA、alignment 与 approximate-anchor 全部打印 residual/argument windows |
| STR-N03 | 未保留不完整的 approximate-drift prose；只保留量词闭合的 Proposition 8.3 |
| STR-N04 | 统一使用 “phase-extremum points”，不称其为函数的 exact critical extrema |

结构审稿后的 additional final-check 修复：

- Theorem 7.4 选定 \(U\) 使
  \(d(y,S)=\|y-p\|\) 对所有 \(y\in U\) 成立，避免 branch output
  跳向另一 zero；
- 明确有效 input neighborhood \(V_0\subset V\)，并要求
  \(\overline B(p,\delta_0)\subset V_0\)；
- Corollary 7.5 继承 \(U,V_0\) 与全部 gauge-domain 条件；
- GX-072 明列 \(F=J^{-1}-I\)，GX-073 明列
  \(\operatorname{gph}F=\Gamma_R^1\)，使 zero set 与 full residual
  结论有明确 underlying relation。

## 6. 三例与 coverage 警戒的最终用途

| ID | 在基础稿中的唯一角色 | 不赋予的含义 |
|---|---|---|
| GX-071 | joint saturation、exact \(\gamma q\) factor 1、tangential margin | generic/natural/universal law |
| GX-072 | all-pairs \(\gamma\) 与 alignment \(1\) 分离；two-sided \(q\)-scaling | normalized Q-factor 已存在 |
| GX-073 | one-step power scale 与 finite escape | convergence-order counterexample under \(q>1\) theorem |
| GX-074 | RL natural domain 不给 input-ball coverage | sharpness 三例之一 |

## 7. 待审问题

1. 对修补后的 integrated draft 做一次独立 proof-only fresh read；
   本轮已把既有 theorem packages 与四份 referee 报告反向整合。
2. 是否将 endpoint-wide A 保留为最弱 readable assumption，或在最终论文
   另给“orbit-only A + local closedness/continuity”的平行版本。
3. 当前 step/critical constants 在联合 RL + error-bound assumptions 下
   是否最优。
4. GX-071 的 optimal restricted RL constant、GX-072/073 的 optimal
   endpoint all-pairs constants。
5. Wang--Li--Ng 2023 与 Moursi--Vanderwerff 2025 的 full-text
   theorem-level overlap；在核完前不得使用排他性 novelty wording。
6. 是否能找到 application-derived、非 reverse-calibrated 的 exact
   \(\theta q\) witness。
7. RL 的最终公开名称与 notation。

## 8. 文件级质量检查

- theorem 顺序与 integration blueprint 对齐；
- 每个 theorem/proposition/corollary 后紧跟 proof 或明确为 definition/example；
- display-math delimiters 数量匹配；
- equation tags 未发现重复；
- Section 7 仅保留一个主 heading；
- Q-01--Q-06、R1--R4 全部落入正文；
- STR-M01--M02、D01--D07、N01--N04 全部落入正文；
- upper/exact/normalized-limit 用语已分层；
- coverage/exclusion/invariance、full/branchwise、all-pairs/anchored 已分层；
- 未修改任何源文件；
- 未写新颖性、maximality、满域或 universal seesaw claim。

## 9. SCI-Skills Expert Contract 1.0

~~~yaml
contract_version: "1.0"
expert_skill: "sci-skills-manuscript-writing"
project_id: null
paper_family: null
stage_id: null
task_id: null
task_status: "COMPLETE"
inputs_reviewed:
  - "work/rl_foundations_integration_blueprint.md"
  - "work/rl_foundations_definitions.md"
  - "work/rl_foundations_ppa_theorem.md"
  - "work/rl_foundations_anchor_theorems.md"
  - "work/rl_foundations_alignment_sharpness.md"
  - "work/rl_foundations_structure_claim_safe_matrix.md"
  - "work/rl_proof_referee.md"
  - "work/rl_foundations_referee_quantifiers.md"
  - "work/rl_foundations_referee_constants.md"
  - "work/rl_foundations_referee_structure.md"
  - "research/example_properties.md (GX-071--GX-074 only)"
outputs:
  - "work/RL_foundations_draft.md"
  - "work/rl_foundations_integration_report.md"
evidence_status:
  - label: "VERIFIED_USER_MATERIAL"
    item: "All listed theorem packages, claim-safe matrix entries, four referee reports, and GX-071--GX-074 catalog records were read from the shared workspace."
  - label: "AI_INFERENCE"
    item: "The canonical ordering, merge/exclusion decisions, compact restatements, and dependency ledger are integration judgments grounded in the reviewed material."
  - label: "EXECUTED_LOCAL"
    item: "Heading inventory, display-math delimiter balance, duplicate equation-tag scan, and terminology/reference scans were run on the integrated draft."
  - label: "PENDING_VERIFICATION"
    item: "Wang--Li--Ng 2023 and Moursi--Vanderwerff 2025 theorem-level overlap, optimal constants, and application-derived sharp examples remain unresolved."
assumptions:
  - "The reviewed source theorem packages and referee reports are the authoritative inputs for this bounded integration task."
  - "All mathematical claims remain conditional on the complete domains, graph restrictions, residual windows, branch selections, and margins printed in the draft."
  - "RL is an internal working label; no final public nomenclature or novelty claim is inferred."
author_input_needed:
  - "Choose the final public name and notation for RL before manuscript lock."
manual_actions: []
quality_checks:
  - "Integrated complete graph, domain, residual-window, and selection quantifiers."
  - "Separated all-pairs from anchored hypotheses and full relations from named branches."
  - "Separated coverage, exclusion, and invariance."
  - "Applied quantifier-referee Q-01--Q-06 and constant-referee R1--R4."
  - "Applied structure-referee STR-M01--M02, D01--D07, and N01--N04."
  - "Kept L=0 as a degenerate constant-reflector branch with q-controlled power phase."
  - "Separated upper order, two-sided exact exponent, and exact Q-factor."
  - "Added general-gauge rescaling, dilation-stability boundary, and isolated gauge-PPA."
  - "Required nonempty approximate projection sets in the no-proximinality theorem."
  - "Printed family-wide projection existence, empty-supremum conventions, and every local gauge argument domain."
  - "Added explicit phase-extremum sequences and full-residual proofs for GX-072 and GX-073."
  - "Retained only claim-safe GX-071--GX-074 roles."
  - "Added theorem dependency and assumption ledgers without placing the SCI contract in the draft."
conflicts:
  - conflict_id: "RL-INT-C01"
    conflict_type: "domain_and_branch"
    claim: "Local RL and an error bound alone define and control arbitrary full-resolvent PPA."
    source_or_locator: "work/rl_proof_referee.md; work/rl_foundations_referee_quantifiers.md"
    competing_values_or_interpretations:
      - "Restricted injectivity only."
      - "Named coverage plus separate full-branch exclusion."
    recommended_resolution: "Resolved in the draft by Definition 0.5, Proposition 1.4, and Assumptions B/A/E."
  - conflict_id: "RL-INT-C02"
    conflict_type: "parameter_and_rate"
    claim: "The gamma*q phase remains meaningful at L=0, and two-sided bounds already give an exact Q-factor."
    source_or_locator: "work/rl_foundations_referee_constants.md"
    competing_values_or_interpretations:
      - "L=0 has q-controlled phase and unidentifiable gamma."
      - "L>0 has the gamma*q upper phase; a Q-factor requires a normalized limit."
    recommended_resolution: "Resolved in Corollary 5.3 and Remark 5.4."
  - conflict_id: "RL-INT-C03"
    conflict_type: "gauge_scope"
    claim: "Every superlinear gauge transfers unchanged between residual and Minty-input coordinates."
    source_or_locator: "work/rl_foundations_anchor_theorems.md"
    competing_values_or_interpretations:
      - "Rescaled gauges always transfer locally."
      - "Literal same-gauge transfer requires fixed-dilation stability."
    recommended_resolution: "Resolved in Proposition 7.2."
  - conflict_id: "RL-INT-C04"
    conflict_type: "literature_boundary"
    claim: "The narrow moving-anchor/alignment formulas have been proved absent from prior literature."
    source_or_locator: "work/rl_foundations_structure_claim_safe_matrix.md"
    competing_values_or_interpretations:
      - "Potential narrow structural distinction."
      - "Pending full-text overlap with two recent sources."
    recommended_resolution: "Keep novelty language excluded until full-text verification."
conflict_resolution_status: "UNRESOLVED"
merge_permission: "orchestrator_only"
recommended_next_action: "Run one fresh independent proof-only review of work/RL_foundations_draft.md, then merge it only if that review confirms the repaired quantifiers and constants."
stage_acceptance_recommendation: "PASS_CANDIDATE"
~~~
