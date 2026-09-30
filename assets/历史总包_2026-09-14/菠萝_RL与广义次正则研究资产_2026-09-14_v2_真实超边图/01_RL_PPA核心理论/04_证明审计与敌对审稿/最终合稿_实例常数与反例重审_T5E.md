# T5 E：真实合稿例子与历史修复落地复核

日期：2026-09-08。**最终裁决：PASS（本轮限定的例子、历史修复与 M1 benchmark 提取范围）；无 FATAL。**

这次输入是用户实际上传的 `upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md`，1881 行，SHA-256：

`8bc3d4906f9d28ca349aad1df068eb8d5f9272d65bb731346f0949f63b9975e9`

该值与 `t5_compare_recheck_033.md` 所记录的最终快照完全一致。本次不再依据“缺失合稿”保留 E-SCOPE-01 障碍；它已由真实上传与直接逐项读取解除。旧 `T5_AUDIT_E_EXAMPLES.md` 的数学复算仍可用，但其缺失合稿/重建风险判定由本补充取代。此 PASS 不冒充整稿全部定理或投稿 readiness 的最终验收。

## 1. 范围与核查方法

直接核对实际合稿：摘要与引言、§2 的 coverage/单值/量词、§3.4 两分支、§3.5 退化 shear、§5 自然类全节、§6 比较/正反例/结论；补充核对 §3 的 set/point rate 与线性 endpoint。所有本表行号均指本次上传文件，不指旧源模块。可见数学例子共为：两分支 sharpness、退化 shear、自然 support/normal 类、圆盘及多面体实例、正向旧证书排除序列、reverse F₀。B4 非凸 reach 与 B5 inexact 例仍是外部模块，**没有被假报为已并入该合稿**。

使用预投稿审查技能按数学、比较、沟通三个视角核对；继承上一轮的独立代数与执行记录，本轮重点确认实际文本没有在合并时改变公式、量词或边界。没有修改用户合稿，没有新增文献检索或优先权认证。

## 2. 历史修复落地表

| 修复 / 审计点 | 合稿行号 | 直接证据与判定 |
|---|---|---|
| CMP-M01：reverse 只能排除 AP-RL | 1809；1836；1853 | 命题与碰撞证明均限定 AP-RL；结论明确说不能把它理解为与较弱 Theorem 3.1 的分离。PASS |
| Introduction 同步限制反向比较 | 52 | 虽仍写 “in both directions”，同段立即限定 reverse 满足 anchored/partial 而违反 all-pairs RL。结合1853无扩大解释。PASS |
| CMP-M02：删除未经定义证明的笼统 PSM 排除 | 1550；1702 | 正文只列指定有限 weak/oblique-Minty、informative scalar 和 coercive matrix；命题结尾限制为(6.1)–(6.4)。未重复旧源模块的 “stated tangentially nondegenerate partial tests”。PASS |
| R033：退化方向修正 | 1391；1395；1579；1697 | 矩阵为(1+λa)P_N；明确在切向退化、法向保留信息，表格为 “tangentially degenerate normal-projector”。PASS |
| 不隐藏成功竞争证明 | 1333；1335；1418；1556；1845 | 明确 same algorithm、global convergence、without condition(5.19)，并承认 scalar aggregate 更弱。PASS |
| 不把 AP-RL 当 coverage | 120；126；128；1849 | 单值图像、全输入覆盖、patch 外分支、跨分支耦合分别说明。PASS |
| 不把距离率当点率 | 388；706；1355；1504；1848 | 一般定理区分 distance Q 与 point R；显式轨道才给 exact point ratio。PASS |
| 不把 best γ 推导误成单锚 noncalm | 150；723；784 | 退化 shear 明确为 neighborhood all-pairs 性质；没有称其在原点 noncalm。自然类1190的 noncalm 则有1215的锚定下界支持。PASS |

历史审计的额外编辑建议并非全部逐字采纳：第52行仍有 “closes the otherwise missing ...” 的可能歧义；第1585行仍保留 “technical integration / supplied report / need not all appear” 的内部写作措辞；第1639行的 native PSM 可更明确重申 S=F⁻¹(0)，或者直接假设同一 S 上的 coupled inequality。它们不推翻本轮例子与要求重点的 PASS；投稿精修时建议处理，不能写成“历史所有可选润色项均已落实”。

## 3. 两分支与退化 shear 的真实落地

### 3.1 Proposition 3.4

| 核查项 | 合稿行号 | 复算结果 |
|---|---|---|
| 算子固定参数 λ₀；y<0 空值 | 519；524；525；530 | 两值正常输出差2cy/λ₀>0；S=ℝᵐ×{0}。正确 |
| 两条 Minty 像 | 541；543 | 正常输入 cy 与−cy；正负半空间完整拼接。正确 |
| actual complete resolvent | 550；551；555 | J(p,ξ_N)=(p+λ₀bc^(−α)|ξ_N|^αe,|ξ_N|/c)；接口同一图点不计碰撞。正确 |
| 跨分支 RL 常数与最佳 γ | 569；579；590；599 | Lδ=2λ₀bc^(−α)+(1+2/c)δ^(1−α)，γmax=α。正确 |
| original minimal residual 与最大 q | 605；613；623 | r=√(b²y^(2α)+((c−1)y/λ₀)²)，qmax=1/α。正确 |
| exact distance ratio 与临界常数 | 628；635；637；650 | 距离比1/c，临界最优极限数据乘积1/c；L₀不冒充正半径常数。正确 |
| 正半径及 universal 2 反证 | 657；665；672；676；678 | 必须 r≤δ；c=1距离不降，真实Lδ也反驳分母D>2。正确 |
| 冻结步长、改变算法 τ 时重算 | 680；683；685；688 | 两系数变为1+τ(c−1)/λ₀、1−τ(c+1)/λ₀；不是同一公式的步长优化。修复已完整落地 |
| set 与 point | 693；694；701；706 | 距离比c⁻¹；切向尾比c^(−α)，一般只宣称point R上界。正确 |

### 3.2 Proposition 3.5

第731行给 a(ξ_N)<1 下的严格递增切向 bijection；第736行完整逆正确。第775行取邻域内非零 h 来见证 AP Hölder 下界，第784行明确这是 neighborhood all-pairs property。沿 t=0 的 residual 第789行是线性，故第799行的 q≤1 与 θ≤γ<1 正确。

第825行已采用更直接的 envelope endpoint 发散证明，明确不再额外依赖 ψ(t)→0；比旧模块表述更严谨。第829行及第832行保留实际递推；第843行保留初始 y₀≥0 和保持切向盒域所需的初始化说明。未发现合并引入的新数学问题。

## 4. 自然类、圆盘、多面体与旧证书排除

| 核查项 | 合稿行号 | 判定 |
|---|---|---|
| 原生 assumptions 与完整 F | 1007；1014；1019；1020 | 一般闭凸C、0∈C、symM≥aI；域外空值。PASS |
| 全域正常逆的实际存在 | 1086；1092；1098；1102 | contraction 证明独立于RL，未把injectivity当coverage。PASS |
| 切向实际完整 inverse | 1053；1123；1134 | 强凸prox最优性，含s=0，正反两向验证，不是branch selection。PASS |
| 跨活动面 parameter estimate | 1136；1139；1146；1166 | ‖T_s−T_s'‖≤λR_D|s−s'|，完整subdifferential含t=0。PASS |
| 独立 EB | 1067；1073；1168；1178；1182 | 对所有输出作统一下界再取inf；使用d_D而不是R_D。PASS |
| 非孤立和真多值的边界 | 1186 | 未称所有类成员都多值；singleton D等例外保留。PASS |
| 最佳指数和常数区别 | 1190；1201；1215；1234；1236 | C非平凡必要；最佳γ=α、最大q=1/α；未称Lδ/K最优。PASS |
| 两尺度及输出状态EB | 1247；1254；1267；1301；1315；1322 | r与δ分开；actual residual属于F(Jx)；完整半径r球内的AP估计用δ=2r。PASS |
| 同算法更强直接证明 | 1333；1335；1338；1341；1355；1365 | 全域point convergence不需要Δ>0；set≤η，point R≤η^α。PASS |
| surviving partial tester | 1383；1384；1391；1410；1416 | 切向退化，算法仍Euclidean；额外切向可和性未省略。PASS |
| 圆盘完整resolvent和常数 | 1441；1442；1459；1466；1468；1470 | z=ξ_N⁺/8；L=5/2、K=2^(−3/2)、κ=(3/4)^(3/2)。PASS |
| 圆盘合法显式轨道 | 1477；1481；1482；1490；1500 | τ≥0、y₀>0；闭式与误差平方均正确。PASS |
| 圆盘三种率不能混淆 | 1504 | 实际distance1/8、实际point渐近1/4、聚合distance≈0.649519与point上界3/4。PASS |
| 多面体全活动面 | 1511；1513；1517 | subgradient为活动顶点凸包；R_D=max顶点距离；无固定活动集及uniform complexity承诺。PASS |
| 正向finite full-input排除范围 | 1667；1672；1679；1689；1693；1702 | finite fixed V、full input patch、positive-definite Cayley 等限制齐全；degenerate survivor明确。PASS |
| 排除证明实际图点和coverage | 1714；1715；1719；1728 | scale-separation图点合法；删掉它们会违反完整输入范围。PASS |

## 5. Reverse 例确实只排除 AP-RL

第1794行定义 F₀，第1806行给两值完整J₀。第1829行证明所有选择正常坐标每次乘1/2或1/3，切向不动；第1832与1833行展示同一Minty输入的不同图点；第1836行两个反射分别为(p,0)、(p,−ξ_N/3)。因此AP-RL右侧零、左侧非零，任意正γ失败。

第1811行的真实partial tester也已并入，(Ξ,N,H)=(2I,2I,3I)，第1836行把inf算成(2a+1)y²≥3y²，数学正确。

最关键的历史修复在第1853行已经明确落地：该例“不把这些 anchored/partial 类与较弱 Theorem 3.1 分离”。本轮独立确认它确实可取moving-projection几何ω(d)=d/3与ψ(s)=s，原理如下：分支a∈{1,2}有u_N=ξ_N/(1+a)、v_N=aξ_N/(1+a)，反射到最近解的距离是|1−a|d/(1+a)≤d/3。故主接口给2d/3安全界，真实最坏比为1/2。主稿未把这个可计算补充写出，但已有正确口径，不构成缺陷。

## 6. 给 M1 / SO-06 Pro 可安全抽取的 benchmark

M1 是 implicit coverage 参数集Λ的结构验证，不是 B5。直接从第524、525行取 λ₀=b=1、c=2、α=1/2、m=1，得到固定算子

\[
F(t,y)=\{(-\sqrt y,y),(-\sqrt y,-3y)\},\qquad y\ge0,
\]

y<0 空值。原稿第683、685行恰好给对任意算法步长τ的正常Minty系数1+τ与1−3τ。由此新增的手算benchmark结论是

\[
\Lambda_{\mathrm{direct\ Minty}}=(1/3,\infty).
\]

| τ区域 / 对照 | 实际coverage | 完整单值 | 明确witness |
|---|---|---|---|
| τ>1/3 | 全ℝ² | 是 | q≥0取y=q/(1+τ)，q<0取y=−q/(3τ−1)，t=p+τ√y |
| 0<τ<1/3 | 否 | 正q时也不单值 | q<0缺preimage；q>0对应两个不同y=q/(1+τ)、q/(1−3τ) |
| τ=1/3 | 否 | q=0无限多值 | 任意y≥0、t=p+τ√y给同一(p,0)；q<0缺coverage |
| τ=1只保留第一分支 | 否 | 在像上是 | q<0缺coverage，显示好chart不创造缺失输入 |
| 合稿F₀，第1794行，τ=1 | 是 | 否 | 第1832、1833行是同一输入的collision |

最小正例τ=1的J(p,q)=(p+√(|q|/2),|q|/2)，两标签在q=0是同一图点，故不能凭“有两支”判断collision。单支inverse、跨支一致性、actual coverage与参数边界必须分别测试。

**安全边界：**这些都是可溯源的 direct-Minty 回归测试。Λ=(1/3,∞) 是在原稿冻结步长说明基础上新作的正确手算扩展，不是原稿已经宣称的SO-06原文Λ结论。这些例子仍可三角消元，尚未匹配SO-06的A、B、P、R、𝓛、Ω全部假设，绝不能写成已经解决非三角/循环composite semimonotone问题。给Pro的要求应是“先通过这些coverage/collision逻辑基准，再展示真正的循环实例及其原文假设匹配”。

## 7. 最终三视角裁决与下一步

- 数学：本轮全部真实例子、actual inverse、参数、最佳指数、error bound、递推及速率区分通过；无需要改定理的失败见证。
- 比较：两个历史必修scope和退化方向均在真实合稿落地；非排他性、同算法更强竞争证明保留。
- 沟通：一般R界与显式Q比值已分开；剩余少量内部措辞属于投稿前编辑精修，不把它们夸大成例子错误。

因此本轮限定范围 **PASS / PASS_CANDIDATE**；原 E-SCOPE-01 的“合稿缺失”及 E-REBUILD-02 的“可能重建回退”不再阻塞。文献新颖性与整稿所有定理仍以主线程其他审计为准。

## SCI-Skills Expert Contract 1.0

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review
project_id: RL-PPA-VERIFY
paper_family: T
stage_id: T5
task_id: T5-AUDIT-E-MERGED-RECHECK
task_status: COMPLETE
inputs_reviewed:
  - upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md, stated example/comparison/definition/rate scopes
  - T5_AUDIT_E_EXAMPLES.md, prior independent calculations
  - t5_merge_comparison_audit.md, historical required and optional repairs
  - t5_compare_recheck_033.md, final recorded hash and repair scope
outputs:
  - /workspace/scratch/01cfe9a021bd/T5_AUDIT_E_MERGED_RECHECK.md
evidence_status:
  - VERIFIED_USER_MATERIAL: directly read uploaded final core and exact line locators
  - EXECUTED_LOCAL: final upload SHA-256 equals the recorded repaired snapshot
  - AI_INFERENCE: example recalc, reverse moving-projection import, and direct-Minty parameter benchmark
  - PENDING_VERIFICATION: SO-06 original composite hypothesis embedding and genuinely nontriangular gain
  - NOT_EXECUTED: user manuscript edits, fresh primary-source novelty review, whole-stage acceptance
assumptions:
  - verdict is bounded to assigned examples and historical comparison-scope repairs
  - actual fixed operator is retained when deriving the M1 parameter benchmark
author_input_needed: []
manual_actions: []
quality_checks:
  - direct uploaded text checked rather than inferred from historical PASS
  - all visible examples checked, external B4/B5 not mislabeled merged
  - actual coverage, all branches, collision and parameter boundary distinguished
  - frozen step and exact changed-step coefficients retained
  - stronger same-algorithm direct natural proof present
  - set-distance and point-error rates distinguished
  - reverse claim confined to AP-RL and not Theorem 3.1
  - required historical repairs resolved without claiming all optional edits done
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: use the verified two-branch and collision cases as M1 verifier benchmarks while requiring a separate nontriangular composite hypothesis match
stage_acceptance_recommendation: PASS_CANDIDATE
```

唯一下一步：主线程把经核验的两分支/碰撞例作为 M1 verifier 基准交给 Pro，并另行要求真正非三角 composite 假设匹配。
