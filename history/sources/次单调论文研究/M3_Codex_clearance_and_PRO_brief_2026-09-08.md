# M3 文献扫雷、问题修复与 PRO 任务包

日期：2026-09-08  
对象：RL–PPA/T5 的误差界侧验证问题

## 一、结论先行

原 M3（“非孤立解集上的普通 (q>1) 次正则性之扰动传递”）**不应现在直接交给 PRO 开始证明**。

原因不是题目没有价值，而是目前已确认：

1. 普通 (q>1) 次正则性本身早已有理论；
2. 普通、非孤立、加性扰动这一宽组合也已有 (q=1) 理论；
3. T5 自己的 Proposition 4.2 已经证明了一类非孤立、保旧目标、显式常数与正管半径的 (q>1) 扰动结论；
4. 三篇 2025 年直接相关论文的全文尚未完成定理级核验，不能据摘要宣称剩余组合是公开空白；
5. 原题没有固定“旧目标还是新目标”“单值还是多值扰动”“点局部还是沿解流形统一”等量词，贸然开证明很容易得到一个已有结果、循环假设或错误命题。

因此，M3 当前评级是：**高匹配、但开放性未认证的 O3 候选；暂不占用 PRO 的主攻轮次。**

## 二、T5 真正需要的接口

设实际被分析的算子为 (F:X\rightrightarrows X)，固定闭目标集 (S\subset F^{-1}(0))。T5 需要的是同一输出域上的普通集合距离误差界

\[
d(y,S)\le K\,r_F(y)^q,
\qquad r_F(y):=d(0,F(y)),
\]

并且这些数据必须与同一 PPA 转移的 RL 几何匹配：同一算子、目标集、范数、选择范围和有效邻域。

对 (0<\gamma<1)，仅有 (q>1) 仍不够。幂次证书还必须满足

\[
\gamma q>1,
\]

或在临界情形

\[
\gamma q=1,
\qquad
K\left(\frac{L}{2\lambda}\right)^q<1,
\]

并给出与覆盖、RL、残差区间及轨道局部化共同兼容的正半径。

不能替代上述接口的对象包括：strong/孤立解次正则性、只对一条选定轨道成立的残差估计、渐近模量但无可用邻域、针对另一算子的误差界，以及只保持部分旧零点却允许新增零点的结论。

## 三、已经覆盖到哪里

| 来源 | 已核范围 | 对 M3/T5 的结论 |
|---|---|---|
| Li–Mordukhovich (2012), *Hölder Metric Subregularity…* | 普通集合距离、可非孤立；outer/restricted coderivative 保留 (x_k\notin S)；主要 (0<q\le1) | 是重要线性/分数阶生产工具；没有核实到普通 (q>1) 的完整运算规则。Remark 3.6(ii) 明说排除解集使 calculus 更难。 |
| Mordukhovich–Ouyang (2015), *Higher-Order Metric Subregularity…* | 定义覆盖任意 (q>0)；普通判据主要针对 subdifferential；扰动章节为 strong (q\ge1) | 证明普通 (q>1) 不是新概念；其 strong 扰动结果不能移作非孤立 ordinary 结论。预印本 Theorem 3.4 的一处选择步骤对 (q>1) 存在数值抽取疑点，未据此宣布定理错误。 |
| Cibulka–Dontchev–Kruger (2018) | strong (q>0) 的 calm 扰动稳定性，给显式新常数并保留给定共同半径 | 定量但仍是 strong/孤立范围。 |
| Gfrerer–Kruger (2023) | 普通 (q=1) 的 perturbation radius；含多值且非 strong 的例子 | “普通+多值+非孤立+扰动”不能作为宽泛新颖性。扰动大小半径不等于 T5 的状态邻域半径。 |
| T5 Proposition 4.2 | 若 (r_{F_0}\ge m d(\cdot,S)^\alpha)、(\|g\|\le\ell d(\cdot,S))、(0<\alpha<1)，则在显式管内保留旧零集并得到 (q=1/\alpha>1)、(K=(\theta m)^{-1/\alpha}) | 已经解决一个单值、距离小扰动类；重复它没有论文价值。 |
| Li–Mordukhovich–Zhu (2026 MOR; arXiv v1 2024) | 对 subdifferential/stationary targets 的一般 distance-side gauge；明确有非孤立例子；部分复合与目标距离转移 | 可为 T5 的特定 subdifferential 类生产 gauge；不是任意 multifunction 的 target-preserving sum/composition calculus，常数与半径常有存在性缩小。 |
| Wei–Théra–Yao (2024) | 凸函数 (q=1) 的普通扰动证书，特定条件下 (K\le(\tau-\varepsilon)^{-1}) 且全域 | 是已有定量正对照，但不是 (q>1)，且使用全局边界方向信息。 |
| Ouyang–Zhang–Zhu (2025) | 出版社摘要确认研究 (F+f) 的 ordinary metric subregularity 与 modulus estimate | 全文未得；(q>1)、目标、假设、状态半径均不得猜测。 |
| Gao–Ouyang–Zhang–Zhu (2025)；Huang–Liu–Zhou–Zhu (2025) | 摘要分别声称 generalized-subsmooth 下的充分条件、点式充要刻画 | 两篇都是 M3/R01 的决定性新近对照；全文未核前不能认证缺口。 |

主要原始来源：

- Li–Mordukhovich 2012: https://epubs.siam.org/doi/10.1137/120864660
- Mordukhovich–Ouyang 2015: https://arxiv.org/html/1507.04825v1
- Cibulka–Dontchev–Kruger 2018: https://arxiv.org/abs/1701.02078
- Gfrerer–Kruger 2023: https://arxiv.org/html/2206.10347v2
- Li–Mordukhovich–Zhu 2026: https://arxiv.org/abs/2406.13207
- Ouyang–Zhang–Zhu 2025: https://doi.org/10.1080/00036811.2025.2505614
- Gao–Ouyang–Zhang–Zhu 2025: https://doi.org/10.1007/s11228-025-00753-7
- Huang–Liu–Zhou–Zhu 2025: https://doi.org/10.1080/02331934.2025.2588424

## 四、原 M3 的逻辑修复

### 1. 三种目标必须分开

对 (G=F+H)：

- (S\subseteq G^{-1}(0))：旧解仍是新解；
- (G^{-1}(0)\cap U=S\cap U)：局部零集完全保持；
- (d(x,S)\le K r_G(x)^q)：相对于旧目标的误差界。

它们不是同一件事。对一般多值加法，(0\in H(s))（(s\in S)）只是保持旧零点的一种直接充分条件，不是必要条件，也不能排除新增零点。

### 2. 完全保持零集仍不足以保持 (q>1)

令

\[
F(s,t)=\operatorname{sgn}(t)|t|^{1/q},
\qquad S=\mathbb R\times\{0\}.
\]

则 (d((s,t),S)=|F(s,t)|^q)。取

\[
h(s,t)=t-F(s,t),
\]

得到 (G=F+h=t)，且 (G^{-1}(0)=S) 完全不变；但

\[
\frac{d((s,t),S)}{|G(s,t)|^q}=|t|^{1-q}\to\infty.
\]

所以真正要控制的是抵消与残差尺度，不只是零集。

### 3. 多值扰动不能只看最小残差

若

\[
H(s,t)=\{0,\,t-F(s,t)\},
\]

则 (d(0,H(s,t))=0)，但 (F+H=\{F,t\}) 的最小残差在小 (t) 时为 (|t|)，仍破坏 (q>1) 误差界。任何多值扰动定理必须控制完整分支或提供真正的非抵消机制。

### 4. 点局部不等于沿非孤立解集统一

每个解点分别有自己的 (K,r)，不自动给解流形一个共同管状邻域。T5 可局部于某个目标片，但其声明范围内必须有统一证书。

## 五、只有满足这些条件，M3 才值得发给 PRO 证明

新的 M3 必须明确交付：

1. 一个自然、具体的原生算子/扰动类，而不是“任意 (F,H)”；
2. 真正多值或真正跨分支的范围，严格超出 T5 Proposition 4.2；
3. 非孤立目标集和可接近它的域外点；
4. ordinary (q_H>1)，不是 strong、pseudo、relative Aubin 或 metric regularity；
5. 旧目标、移动目标或局部零集等同三者中的一个清晰版本；
6. 由原生部分信息产生 (q_H,K_H,r_H>0)，不得把目标误差界或等价残差比较当假设；
7. 对所有相关值/分支有效，不能只挑一个好选择；
8. 至少一个严格分离例子：现有 T5 Proposition 4.2、strong perturbation、(q=1) calculus 不能直接给出该证书，而新结论能；
9. 把结果代入同一算子的 T5，并核对 (gamma q_H\ge1)、临界常数和共同半径；
10. 若这些目标不可能同时达到，给出最小反例或结构性障碍，而不是弱化问题后宣布成功。

## 六、给 PRO 的任务提示词（不提供证明路线）

```text
你现在处理 RL–PPA/T5 项目的 M3 任务。不要预设一定存在新定理，也不要为了得到正结果而弱化 ordinary、q>1、非孤立、多值、跨分支、显式常数或共同正半径中的任何一项。

我会提供：
1. RL_PPA_T5_core_manuscript_2026-09-07.md；
2. 本 M3 文献扫雷与问题修复文件；
3. 若能取得，三篇决定性 2025 论文全文：
   DOI 10.1080/00036811.2025.2505614；
   DOI 10.1007/s11228-025-00753-7；
   DOI 10.1080/02331934.2025.2588424。

任务目标不是重复定义高阶次正则性，而是判断并尽可能解决：

能否从一个自然的、多值且具有非孤立零集的算子的原生部分信息，分别、定量地推出 ordinary 高阶误差界数据 (q,K,r)，并把它作为独立证书与该同一算子的 RL 数据 (gamma,L) 在 T5 中匹配，从而得到现有最接近理论不能直接给出的 PPA 结论？

开始研究前必须先完成两项复述：
A. 用自己的话准确说明 T5 接受什么 RL 证书、什么 ordinary 输出误差界证书，以及二者为何可以分别验证后再匹配；
B. 用自己的话准确说明 M3 中旧目标、新目标、局部零集保持、非孤立 ordinary 与 strong/孤立之间的区别。

随后按以下门控工作：

第一阶段：定理级文献核验
- 全文核验上述三篇 2025 论文及其直接相关前后文献；
- 给出 theorem/definition 编号、全部关键假设、指数约定、目标集、普通/strong 范围、模量和半径；
- 判定哪些结果能直接产出 T5 所需 (q,K,r)，哪些只能形式转换，哪些不适用；
- 若全文无法取得，明确暂停相应 novelty 结论，不得用摘要补定理。

第二阶段：价值判定
- 若已有理论实质覆盖 M3，直接证明“已覆盖到何种程度”，列出如何导入 T5，并停止发明新定理；
- 若只剩狭窄缺口，给出一个完全量化、自然、非循环、可证伪的最终问题；
- 只有在该缺口通过文献排除后，才进入证明探索。

第三阶段：证明或障碍
- 尝试得到从原生部分信息到 ordinary (q,K,r) 的严格定理；
- 必须覆盖非孤立目标和完整多值/跨分支量词；
- 必须给正共同半径、常数与指数，而不只给渐近存在性；
- 必须构造自然实例并完成与最接近理论的 implication/equivalence/incomparability 比较；
- 必须把证书代入 T5 的同一实际算子，检查 gamma*q 和临界常数；
- 若失败，输出最小障碍定理/反例及其对 T5 的精确含义。

禁止事项：
- 不得把 strong 次正则性冒充 ordinary；
- 不得把 q<=1 的定理外推到 q>1；
- 不得把 perturbation-size radius 冒充状态邻域半径；
- 不得只证明零集保持就声称指数保持；
- 不得用 d(0,H(x)) 控制多值 H 的所有分支；
- 不得重复 T5 Proposition 4.2 或简单重述 r_G>=c r_F 后宣称新 calculus；
- 不得把另一算子、另一目标或选定轨迹的 EB 代入 T5；
- 不得因“没搜到”宣布首创。

最终返回必须将每项主张标记为 PROVED、ALREADY COVERED、OBSTRUCTED、PENDING VERIFICATION 或 SPECULATIVE，并给出可逐行复核的证明或原始文献位置。

如果缺少完整论文、需要大规模符号验证、反例搜索或文件级证明核对，请明确要求我把相应子任务转给 Codex；不要假装已经完成。
```

## 七、资源调度建议

- **现在的 PRO 主攻轮次：不建议给 M3。** M3 的决定性文献门还未关闭，证明任务尚未唯一化。
- **现在更适合给 PRO：M2 / SO-07（退化 PPA 的 actual range coverage）**，因为它有明确作者出处、明确未解决陈述和较清楚的验收目标。
- M3 保留为第二队列；取得三篇 2025 全文后，用上面的提示词开启。若全文显示已覆盖，就把现有工具直接拉入 T5，而不是硬造新理论。

## 八、研究审计状态

```yaml
contract_version: "1.0"
expert_skill:
  - sci-skills-literature-search
  - sci-skills-paper-deep-reading
project_id: null
paper_family: theoretical
stage_id: T2
task_id: M3-clearance
task_status: PROVISIONAL
inputs_reviewed:
  - RL_PPA_T5_core_manuscript_2026-09-07.md
  - OPEN_PROBLEMS_REGULARITY.md
  - accessible primary papers and official records listed above
outputs:
  - theorem-scope coverage matrix
  - T5 import requirements
  - logical stress tests
  - repaired M3 acceptance gates
  - no-proof-hints PRO prompt
evidence_status:
  - VERIFIED_SOURCE: accessible theorem-level sources through 2026-09-08
  - VERIFIED_USER_MATERIAL: T5 and open-problem files
  - PENDING_VERIFICATION: three decisive 2025 full texts
  - AI_INFERENCE: M3 should not yet consume the principal PRO proof round
assumptions:
  - all exponents use d(x,S) <= K*d(0,F(x))^q
  - ordinary and strong subregularity remain distinct
author_input_needed:
  - lawful full texts of the three decisive 2025 papers if available
manual_actions: []
quality_checks:
  - target sets and inclusion directions separated
  - q conventions checked
  - constants, moduli, perturbation radii and state radii separated
  - abstract-only evidence not promoted to theorem evidence
  - no novelty claim from failed searches
conflicts:
  - M3 broad wording overlaps T5 Proposition 4.2 and existing q=1 ordinary perturbation theory
  - decisive 2025 theorem scopes remain inaccessible
conflict_resolution_status: UNRESOLVED
merge_permission: orchestrator_only
recommended_next_action: assign PRO to M2/SO-07; retain M3 behind its full-text gate
stage_acceptance_recommendation: REPAIR
```
