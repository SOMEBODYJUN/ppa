# 有限状态 Markov 分类成果包：期刊门槛重新评估

日期：2026-09-09。任务：`journal_bar_redteam` 后续审查。证据基准：新完成的有限状态分类、lazy four-cycle 独立审计、汇总定理包与随机质量稀释审计。

## 1. 更新后的判决

**判断上调，但上调到的是“一篇值得按 SIOPT 标尺完成的聚焦理论论文候选”，不是“随机 RL 旗舰已成立”，也不是“已经达到两本期刊的录用水平”。** MP 可以保留为条件性冲刺；当前没有足够证据把 MP 或更高目标作为保守结果预期。投稿就绪状态仍为 **REPAIR / NOT_READY**，聚焦论文建设则为 **GO**。

新结果确实消除了上次审查的一项实质阻断：正向部分现在保留**原始同步 \(\Psi\)、原始 ordinary \(W_2\)、外层全部不变律、内层实际最优输运**，给出固定有限状态类的完整误差界分类和有限验证器。它不再依赖换到条件度量去完成正向叙事。

因此，对这篇**有限/无限状态 discrepancy 分类论文**，撤销上次为“新随机 RL 旗舰”设置的强制升级条件——不必先发明一个非高斯多值随机 proximal 收敛定理，才允许成稿。原门槛仍适用于将来另行提出的随机 RL 方法论文。不能因研究目标改变而机械沿用旧门，也不能因新增定理而把条件性投稿判断说成结果保证。

## 2. 新资产究竟增加了什么

| 新资产 | 已证数学内容 | 对上一轮判断的改变 |
|---|---|---|
| 固定有限状态分类 | \(\Psi^{-1}(0)=\mathcal I\iff d_{W_2}(\mu,\mathcal I)\le K\Psi(\mu)\) 全局成立；无需任何混合/收缩假设 | 有了同一原问题内的正向类定理；不再只是反例加条件度量替代品 |
| 完整 OT 紧边表示 | 通过 normalized transport-dual vertices 表示所有 source-admissible plans；保留两个 infimum | 新意的主要承载点之一；不能简化成对任意 coupling 的单个 LP |
| 原生有限验证器与锐常数 | 零残差面上的有限 stationarity LP tests；\(K_*^2=\max_v E(rv)/(R\cdot v)\) | 由“存在某个 EB”推进为可核对的精确 source certificate；不代表高效大规模算法 |
| Lazy four-cycle | 位移签名碰撞，但 OT 最优约束排除假零点；删去 OT 就失败 | 证明精确表示确有作用，超出全局 pointwise residual co-Lipschitz 条件 |
| 有限状态 rate 不兼容 | sharp global \(K^2=13/p\)，sharp local \(K^2=4/p\)；真实 R 几何收敛而任意邻域一步距离可增大 | 把 EB 存在、系数和 source 一步率机制分开；不能把这一点叫新的混合原理 |
| 与无限紧致模型对照 | exact zeros + uniform Q/R rates，却无正 Hölder EB | 无穷尺度现在有结构性必要性：这类反例不可能藏在一个固定有限系统里 |

可被清楚表达的中心结论已经形成：**对这个特定不变输运差异，识别性、误差界存在性与率兼容性是不同问题；有限状态的多面体结构把前两者锁在一起，紧致无限状态则不能。**

这比“一个 discrepancy 看不到相关性”的单例更完整。它仍是 source-specific 的分类，不是所有 Markov 残差、所有度量、所有随机优化算法的一般逆定理。

## 3. 数学审查：通过的部分与必须并入主稿的修正

本轮阅读并核对：

- `MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md` §§1–10，包括 exact union、vertex sharpness、Hoffman/continuity 与 lazy-cycle。
- `AUDIT_MARKOV_FINITE_STATE_LAZY4.md` 全文及独立 exact 程序。
- `MARKOV_PAPER_THEOREM_PACKAGE.md` 的框架、Theorem F、紧致边界、主要否定结论与汇总 scope。
- `AUDIT_STOCHASTIC_MASS_DILUTION_AND_MATCHING.md` 的定理、近邻归约及与本文中心的关系。
- `MARKOV_GLOBAL_NOVELTY_AUDIT.md` 的 finite/compact/source/WPI 对照与本轮补充检索。

本轮实际重跑：

```text
python3 output/audit_markov_finite_state_lazy4_exact.py
```

程序全部 PASS，核对了 35 个 subdivision vertices、global/local witnesses、OT 约束、source 参数、R-rate 和局部一步膨胀。无限紧致证明采用已经完成的独立解析审计；本轮没有重跑其所有脚本。

### 3.1 有限主定理没有发现新的致命漏洞

1. Normalized Kantorovich dual 的 pointedness 正确；零 marginal 也有 optimal dual vertex。
2. 紧边集合同时涵盖并仅涵盖实际边缘对的最优 coupling；没有把外层 anchor 偷换为最近不变律。
3. 每个分支是 compact polytope，源 minimum attained；零残差面是 face。
4. \(E=d_{W_2}(\cdot,\mathcal I)^2\) 对质量向量凸，因 stationary polytope 凸；这是 vertex 证明的关键。
5. 正 residual vertex ratios 不只是上界。任何全局 EB 系数也须逐 vertex 支配该 ratio，故最大值确实锐。
6. Empty zero-face 分支用正 residual minimum 处理，而没有对不相容系统误用 Hoffman。
7. 固定 constraint matrix 的 Hoffman + transport value Lipschitz 给 optimal-plan set 的 Hausdorff Lipschitz；\(\Psi^2\) 的连续 piecewise-affine 声明有证明。

有限验证器的假设包括**数据固定**。一族有限截断中最优 \(K\) 可以发散；不应把它误读为对所有有限 Markov 系统具有统一 EB。任意实数输入的“decidable”也须保留 exact-comparison oracle 或 rational/algebraic representation 条件。

### 3.2 Lazy-cycle 的四项修正不得丢失

设 \(G=(0,1,3,4)\)、\(T:0\to1\to3\to4\to0\)、\(P_p=(1-p)I+pT_\#\)，\(0<p<1\)，不变律 \(\beta=(1/4,1/4,1/4,1/4)\)。

- **全局/局部不同：** global \(K^2=13/p\)，local \(K^2=4/p\)。从 \(\beta\) 连到 global maximizer 的混合射线在近处只有 ratio \(3/p\)，不能承接 global sharpness。
- **正确 local witness：** \(\mu_u=\beta+u(\delta_3-\delta_1)\)，有 \(E=4u\)、\(\Psi^2=pu\)。近 \(\beta\) 的 quantile transport 仅需相邻边，给 matching upper bound \(4/p\)。
- **source 参数：** 对 \(\tau=(1-\alpha)/\alpha>0\)，原生 expected almost-firm 最小 violation 为 \(\epsilon_{\min}=p(15+25\tau)\)。取 \(p=1/100,\tau=1\) 时 \(\epsilon=2/5<1\)；\(p=1/2\) 只适合数值/几何说明，不能冒称处于该 source violation 范围。
- **真实不满足一步收缩：** \(\nu_u=\beta+u(\delta_3-\delta_4)\)，\(E(\nu_u)=u\)，而 \(E(\nu_uP_p)/E(\nu_u)\) 等于 \(1+3p\)（\(p\le1/2\)）或 \(7p-1\)（\(p\ge1/2\)），均大于 1。

最后一点降低而非提高“惊人性”：R 线性混合与一步非 Q 收缩本来不同。该例的价值是用同一核、同一 source residual、同一几何把区别定量写全，不是首次发现 R 与 Q 不同。

任何 local EB gauge 必满足 \(\rho(r)\ge2r/\sqrt p\)，而指定 source strict one-step scalar formula 要求

\[
\rho(r)<\sqrt{\tau/\epsilon}\,r
\le\sqrt{\frac{\tau}{p(15+25\tau)}}r
<\frac{r}{5\sqrt p}.
\]

这严格排除了该固定原生参数机制下的任何兼容 gauge。不是“所有 source hypotheses 都满足而定理失败”，而是 **almost-firm 结构与普通线性 EB 可同时成立，rate-compatible gauge 仍失败**。不排除多步估计、其他 Lyapunov 函数、替代度量或改善后的证书。

## 4. 敌意审稿人仍然能提出什么

| 反对意见 | 严重度 | 目前是否挡得住 | 最低回答 |
|---|---|---|---|
| “finite exact-zero ⇒ EB 是多面体理论的常规推论” | MAJOR；若当作新一般原理则 BLOCKER | 能承认，不能反驳其一般机制古典性 | 把贡献放到保留嵌套 OT 的精确表示、sharp source certificate、OT-essential witness 与 finite/infinite 边界 |
| “你只研究一个特殊、原本就有假零点问题的量” | 重要性 BLOCKER 尚未完全消除 | 有已发表必要性问题与最近应用论文作依据，但并非影响力认证 | 用源定义/问题逐项表说明哪些实际主张被排除、finite verifier 能解除什么原生假设 |
| “无正 Hölder 反例是人为拼尺度” | MAJOR | 无穷尺度现在由 finite theorem 证明不可避免，但自然应用仍有限 | 解释构造约束与 uniform Q/relative R 的必要性；不把它叫 imaging/proximal 原生应用 |
| “所谓 algorithm 是枚举天文数量的 LP” | MAJOR if efficiency claimed | 能挡住，只要 claim 是 finite exact certificate | 写清输入、输出、分支数依赖、反例/常数证据；不称 polynomial-time 或 scalable |
| “R 收敛却没有一步收缩很常见” | MAJOR if principal novelty claimed | 同意 | 把 lazy-cycle 放作三个条件分离的锐见证，有限/无限定理才是中心 |
| “随机 RL、Gaussian、dilution 把原本清楚的文章弄散” | MAJOR communication/positioning | 目前 theorem package 确有此风险 | 精简主稿；这些最多短讨论或补充，不计主要创新 |
| “没有真实优化应用，SIOPT 是否匹配” | MAJOR venue risk，不是纯理论稿普遍拒稿规则 | 自然 random projection 与相关源算法背景提供基本连接 | 精确 native verifier 的数学应用可以先满足聚焦论文；若称实用优化新方法则另补真实算法类 |

这里最大的剩余风险已经从“正向数学闭合缺失”转为“source-specific 分类是否重要到指定期刊所需程度”。继续堆反例或调 sharper mixing 常数不能自动回答这一问题。

## 5. 最强近邻扣除：需要承认的旧机制

新 finite theorem 的一般机制必须明确放在 classical polyhedral error bounds 下。本轮直接核验了 Dolgopolik 的 **Theorem 5**：piecewise-affine function 在任意 bounded set 上有误差界；其引言还明确回溯 Robinson/Gowda 的相关理论。[Dolgopolik, 2023，原始全文](https://arxiv.org/pdf/2210.02606)。该文已正式发表于 *Set-Valued and Variational Analysis*，因此不能把这一条当尚未成熟的周边猜想。[原始版本记录](https://arxiv.org/abs/2210.02606)。

这并不自动给出本项目嵌套 \(\Psi\) 的完整表示、sharp formula 或 lazy-cycle；它说明一旦完成结构识别，普通 EB 存在性不是新的普遍定理。保留项目直接 vertex proof 很合理：它更自足，也产生 sharp source constant，但篇幅简短不意味着贡献必小，篇幅变长也不能增加新意。

有界优先权审计又指出 Hoffman 1952、Robinson 1981 polyhedral multifunctions、Mangasarian–Shiau 1987 LP solution Lipschitz 与 Burke–Ferris 1993 weak-sharp LP 传统。这些来源的具体访问深度记在 global novelty audit；本轮不将其他代理的 abstract-level 访问冒充自己逐定理读过。核心结论一致：**一般机制 NOT NOVEL；exact source-specific theorem 的 priority 仍 PENDING。**

对无限模型，ALPW 的 WPI 反例已经表明“几何混合不迫使每个既定耗散证书有效”这一宽泛观点有先例。其对象、范数、随机映射依赖与 source \(\Psi\) 不同，尚不能据此宣布本项目精确定理被覆盖。[ALPW 原始全文](https://arxiv.org/html/2312.11689v1)。

HLS 明知 CAT(0) 非负 discrepancy 不保证 exact zeros；Luke 后续问题允许“适当度量”。因此应写 **fixed original discrepancy / fixed ordinary W2 的精确分类与障碍**，不用“完全解决 Markov 次正则必要性猜想”。[HLS](https://arxiv.org/html/2206.05213v3)，[Luke §6](https://link.springer.com/article/10.1007/s10107-024-02124-w)。

## 6. 最低剩余门：Proof / Novelty / Application

这些是当前这篇聚焦论文的门，不是要求再启动一个更大研究项目。

### P：证明与版本冻结——大部分已过，剩下合并审计

**P1 必须：** 将 lazy audit 的 local \(4/p\)、small-p source 范围、任意邻域一步膨胀、严格 general-gauge incompatibility 合并到单一 authoritative theorem package；不得带入中间讨论中的 global-to-local 错射线或“35 个区域”误称。本轮未在现有汇总稿中发现这两种错误陈述；这是合并检查项。独立审计已给出正确结果，不需要再猜新定理。

**P2 必须：** 对最终同一版本完成逐式检查，重点是 original nested infimum、zero-marginal dual vertices、sharpness 两方向、固定数据依赖、infinite-block cross transport、attainment 与 rate quantifier。原证明和原审计的版本不同不能用“都 PASS”直接跳过合并检查。

**P3 条件性：** 若摘要承诺一个可运行 native verifier，就应至少提供一次一般有限输入的 exact/validated 实现，涵盖多个不变律、零质量边界、通过与失败实例。若只承诺 finite mathematical certificate，完整伪代码与证明即可；不强制建设大规模 LP 软件。

### N：优先权与意义——仍是决定期刊层级的硬门

**N1 必须：** 完成精确谓词矩阵：source \(\Psi\) 固定；outer \(\pi\) 全 invariant；inner optimal coupling；finite exact identification；linear W2 EB；sharp coefficient；finite certificate。逐项查原始谱系与 polyhedral/lexicographic LP 近邻，不只搜论文标题。

**N2 必须：** 对 infinite compact counterexample 与 ALPW/RFI 近邻给出对象、拓扑、uniform rate、zero set 和 realization 的逐项比较。未找到同题不等于优先权获证。

**N3 必须：** 贡献段明确写“经典多面体工具产生这个已被使用的 nested discrepancy 的完整有限结构”；解释它对源问题的一个正式含义确有决定性答案。若近期来源已有等价完整分类，有限结果须降级，整篇期刊判断重评。

### A：应用——聚焦理论论文已有基础，实用算法论文尚未有

**对聚焦分类文章，最低 A 门基本满足：** lazy-cycle 不是纯装饰，它证明忽略 OT optimality 和依赖 pointwise injectivity 会漏判；自然 convex projection 证明 false-zero 障碍确实发生在随机近端对象中；infinite example 给 sharp scope boundary。这些可以是理论文章的数学应用和必要性见证。

不需要为了报 SIOPT 而强制加非高斯模拟或一个人为“机器学习应用”。但不能把四状态链叫成新的 stochastic optimization algorithm，也不能把有限证书包装成高效停止规则。如果选择 algorithm/software 叙事，则必须另补一个真正算法类的验证收益与计算代价，当前 A 门就仍未过。

**最小值得加强而非硬性必需的应用：** 在一个非孤立 stationary polytope 的有限随机投影/分支模型中展示 general verifier 输出 false-zero witness 或 sharp EB，证明外层全部 invariant 的处理确有用途。它应服务主定理而非为篇数再造复杂模型。

## 7. 期刊层级：现在应怎样说

| 目标/状态 | 本次判断 | 还差什么 |
|---|---|---|
| 一篇完整聚焦理论论文 | **已有足够中心数学内容，GO 成稿** | 合并修正、紧凑主线和精确文献定位 |
| SIOPT 候选 | **有合理依据，允许进入面向该刊的最终审查** | N 门与版本冻结；审稿人仍可能认为 source-specific 作用域偏窄 |
| MP 候选 | **可以保留条件冲刺，不建议视为保守目标** | 不只是同领域 source 曾在 MP 发文；需证明本分类/反例对优化理论的重要后果足够突出 |
| “已经确实能发 SIOPT/MP” | **不能据当前证据认定** | 独立审稿只能评估差距，不能决定实际编辑判断 |
| 随机 RL 旗舰/更广顶级目标 | **仍未成立** | 需要 native matching、真多值机制或可迁移的新方法；不由 finite classifier 自动推出 |

这是对当前材料的条件性质量判断，不把 SIOPT 和 MP 当作一个固定线性排名。两刊官方范围均支持优化理论与变分分析，MP Series A 也允许重要短文；没有“必须长篇或必须实验”的形式障碍。[SIOPT 官方范围](https://www.siam.org/publications/siam-journals/siam-journal-on-optimization/)，[MP 官方范围](https://link.springer.com/journal/10107)。

## 8. 推荐主稿内容与停止扩张规则

建议主线按问题来组织：

1. Source discrepancy 与待判别的三个命题，完整保留原量词。
2. 自然凸随机投影：识别性本身可以失败。
3. Finite-state classification：exact zeros 自动给 linear EB，tight-edge verifier 与 sharp formula。
4. Lazy-cycle：OT 最优性不能删，普通 EB 与 source 一步率条件不能混。
5. Infinite compact theorem：即使 exact zeros + uniform Q/R 线性率，仍无任何正 Hölder EB；紧性只给任意一般 gauge。
6. 结论仅说明哪些必要性解释已被判定、哪些未决；条件输运修复用一个短段说明方向。

Gaussian、Dobrushin、one-bit weak-Poincaré、mass dilution 与 scalar concavification不宜全部平铺主稿。它们可以保留为独立技术笔记/补充材料；本次上调判断不是由这些段落累加而来。尤其 dilution 与匹配定理的主要输入仍是 native compatible coupling 的存在，尚未形成新的随机 RL 应用。

本轮之后应停止用“再找一个更复杂 stochastic RL 模型”作为这篇文章开工的前提。先交付这篇准确聚焦的完整稿和 novelty terminal check；若 N 门失败，回到专业理论期刊的范围评估，而不是继续放大标题或添成熟工具。

## 9. 证据与返回契约

本轮新增执行证据：`audit_markov_finite_state_lazy4_exact.py` 全部通过。新检索是有界 exact-source/PWA 对照，不是系统综述。官方期刊事实引用同日已核验原页；无 IF、分区、接受率、审稿期或费用判断。

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review + sci-skills-journal-recommendation
project_id: null
paper_family: theoretical
stage_id: null
task_id: journal_bar_redteam
task_status: PROVISIONAL
inputs_reviewed:
  - output/MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md
  - output/AUDIT_MARKOV_FINITE_STATE_LAZY4.md
  - output/audit_markov_finite_state_lazy4_exact.py
  - output/AUDIT_STOCHASTIC_MASS_DILUTION_AND_MATCHING.md
  - output/MARKOV_PAPER_THEOREM_PACKAGE.md
  - output/MARKOV_GLOBAL_NOVELTY_AUDIT.md
  - Dolgopolik 2210.02606v3 Theorem 5 and original version record
outputs:
  - output/JOURNAL_REEVALUATION_FINITE_MARKOV_CLASSIFICATION.md
evidence_status:
  - VERIFIED_USER_MATERIAL: complete finite classification and independent audit
  - EXECUTED_LOCAL: independent lazy-cycle exact script rerun passed
  - VERIFIED_SOURCE: PWA bounded-domain EB primary theorem and same-day journal scope pages
  - AI_INFERENCE: upward revision to focused SIOPT-oriented paper candidacy
  - PENDING_VERIFICATION: exact source-specific priority and final merged manuscript audit
assumptions:
  - focused discrepancy classification is the evaluated article, not a stochastic RL method flagship
  - finite-data constants are not uniform over changing systems
  - algorithmic efficiency is not claimed
author_input_needed: []
manual_actions: []
quality_checks:
  - source residual and ordinary metric retained in the new positive theorem
  - finite proof, OT strictness, local constants and actual R-versus-Q behavior inspected
  - standard PWA/Hoffman machinery deducted from novelty
  - previous flagship gates revised to match the now-narrower article goal
  - no new natural algorithm demanded merely to manufacture venue fit
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: Merge the audited finite and lazy-cycle results into a focused manuscript and complete its exact-source novelty gate.
stage_acceptance_recommendation: REPAIR
```

唯一下一步：**合并已审计的 finite/lazy-cycle 定理，完成聚焦主稿及 exact-source 新颖性终审；以此决定 SIOPT/MP 的具体投稿定位。**
