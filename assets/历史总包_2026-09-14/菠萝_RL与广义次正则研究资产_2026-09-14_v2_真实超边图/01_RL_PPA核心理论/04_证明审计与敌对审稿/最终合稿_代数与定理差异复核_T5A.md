# T5 审计 A：真实合稿 delta audit

日期：2026-09-08。审计对象：`upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md`，共 1881 行。

源文件 SHA-256：`8bc3d4906f9d28ca349aad1df068eb8d5f9272d65bb731346f0949f63b9975e9`。

本次是对既有 `T5_AUDIT_A_ALGEBRA.md` 的落地核验，不重写旧审计，也不把旧模块的问题自动转记为真实合稿缺陷。已逐行重读合稿第 1–845 行的核心代数和锐性正文，另对第 1188–1330、1420–1518、1580–1642、1787–1881 行进行定点核对，并全文搜索 exact/sharp、最近点及常数量词。未声称对其他专题证明或引文进行了本轮完整审计。

## 1. 当前判定

**PASS（仅限 A 审计的代数、常数、量词和 sharp/exact 范围）；没有遗留 REPAIR，也未发现 FATAL。**

旧报告的 A01–A05 已在合稿中修复，或通过不纳入有问题的中间表述而消除。此前针对替代源模块的总判定 REPAIR 不应继续套到这份已上传合稿。本文没有执行编辑，也不修改阶段状态；整篇论文、文献新颖性及投稿通过仍不由本审计员判定。

## 2. 旧问题逐项核对

| 旧 ID | 合稿精确定位 | 当前事实与数学判断 | 判定 |
| --- | --- | --- | --- |
| A01：任意固定解点误换集合距离 | 第 204–209 行；第 265–278 行；第 1605–1618 行；第 1622–1635 行 | 主定理明确对每个 covered input 和每个 admissible transition，存在最近点；native semimonotonicity 导入也已补 same nearest solution；FS-only 禁止换最近点在第 1635 行再声明 | PASS — 已修复 |
| A02：有效 L 误写为 L≤U | 第 764–773 行，(3.52) | 正文为 one valid reflected-map coefficient，公式第 767 行明确写 `L:=`，没有允许任意更小 L | PASS — 已修复 |
| A03：局部最优指数未限定锚点 | 第 150–158 行；第 599 行；第 723 行；第 775–784 行 | 定义限定 at an input；可达族限定 every solution input；退化族限定 (0,0) 的全邻域，并以固定附近 h 的比较排除更大指数 | PASS — 已修复 |
| A04：二次配方 z、w 未定义 | 第 1589–1599 行 | 合稿只保留用 a,b,μ,ν,λ 全部已明示量写出的 Cayley 常数，没有纳入旧稿那个含未定义 z,w 的中间配方；这是通过删除歧义式解决，不是补入定义 | PASS — 缺陷未进入合稿 |
| A05：`q>0,quad K>0` | 第 173–176 行，(2.12) | 第 175 行已写成合法 `q>0,\quad K>0` | PASS — 已修复 |

### 2.1 A01 的关键量词已真正进入数学前提

合稿第 204 行的量词为

\[
\forall x\text{ covered by (3.1)},\quad
\forall(y,v)\in\mathcal A(x),\quad
\exists p=p(x,y,v)\in P_S(x).
\]

所以第 265 行使用 \(\|a+b\|=\|x-p\|=d(x,S)\) 有合法依据；第 274–278 行的 energy inequality 不再有锚点距离替换漏洞。

native 导入的第 1605 行同样明确要求最近点比较，第 1607 行保留两项非负性，第 1613 行保留 EB 与正分母条件。因此

\[
(1+2\lambda\mu)d_+^2+(1+2\nu/\lambda)s^2\le d^2,
\qquad
\kappa_{\mu,\nu}=
\frac{\rho}{\sqrt{(1+2\lambda\mu)\rho^2+\lambda^2+2\lambda\nu}}
\]

在合稿的现有前提下成立。旧报告给出的 \(x=(3,1),y=(1,2),v=(2,-1)\) 反例不满足此最近点前提，因而不是该合稿结论的反例。

第 146–148 行的 scope table 进一步把 moving-projection、fixed-solution、along-trajectory 分开；第 147 行明确 fixed-solution 仅给 \(\|x-\bar p\|\)，不自动给 \(d(x,S)\)。修复是前提、证明与解释三处一致，而不是只加一句免责声明。

## 3. scalar exact / operator sharp 的最终限定

| 核验对象 | 合稿精确行号 | 最终限定与结论 | 判定 |
| --- | --- | --- | --- |
| 标量后果不是反射等价条件 | 317 | 明说 consequences，不是 equivalent reformulation | PASS |
| 精确 envelope 保留哪些信息 | 433–453 | energy、两项 B cap、EB；明确不保留 reverse-triangle，也不保证向量/算子图可实现 | PASS |
| nonlinear exact limsup 的假设与证明 | 455–512 | γ∈(0,1)、L>0 在本小节前置；ψ 非减、零点消失；证明覆盖有限、零与无穷 limsup | PASS |
| exact 不是各算子最优速率 | 514 | 直接限定到 (3.26) scalar relaxation | PASS |
| γ=1 因子强度 | 411–425 | 三项 min 完整；只称 certified bound，不称某个算子的最优率 | PASS |
| 渐近模量不等于固定正半径常数 | 641–650 | 明确先固定 Lδ 求 d→0，再 δ→0，并否认 L0 必在指定正半径有效 | PASS |
| denominator 2 的不可提高范围 | 678 | 限定为统一 critical certificate；D>2 的反例使用真正正半径 Lδ；否认 scalar relaxation operator-exact 和普遍必要性 | PASS |
| 变步长不能暗改算子 | 519、530、680–688 | 冻结 λ0；换算法步长 τ 后明示需重新核验 | PASS |
| threshold 不是实际收敛必要条件 | 50、369、427、710、799、825–827 | 多处区分该统一 scalar 规则与实际 normal dynamics；未声称全部证书都失败 | PASS |
| natural class 的 sharp exponent 不等于 sharp constants | 1190–1236 | 匹配下界与 residual 上界均出现；第 1236 行明确不称 Lδ 或 K 最优 | PASS |
| exact disk trajectory 的初值与速率对象 | 1476–1504 | τ≥0、y0>0 明示；distance ratio 1/8、point-error ratio 1/4 与 certificate factor 分开 | PASS |
| 结论段是否重新扩大 sharp 范围 | 1568、1842–1848、1853、1870 | 重申信息类、充分性、AP-RL 与弱 transition 条件差别；没有实例最优或普遍必要性回流 | PASS |

### 3.1 denominator 2 和 sqrt(2) 没有混淆

第 265–270 行由完整反射向量加减推出

\[
s\le\frac{d+Ld^\gamma}{2}.
\]

第 473 行保留

\[
A(d)-B(d)^2=\frac{(Ld^\gamma-d)^2}{4}\ge0.
\]

第 514 行把 energy-only 的 \(L/(\sqrt2\lambda)\) 与 full-step 的 \(L/(2\lambda)\) 分开。因此真实合稿没有把两个信息集的系数相互冒充。第 678 行还给出 D>2 时的有限尺度见证，不仅比较两个形式极限。

### 3.2 上界的量词、正半径和可达性仍一致

第 344 行明确对所有 \(d\le r\) 的 admissible transitions 给 \(d_+\le\beta(r)d\)；第 355–367 行明确正半径存在与严格临界条件等价，并且实际因子是 \(\beta(r)\)，不是 \(\kappa_0\)。第 398 行明确临界等号不能从当前公式提供严格因子。

可达族第 572–590 行的 \(L_\delta\) 覆盖所有 location 与 cross-sign pairs；第 662–676 行先固定有效 \(L_\delta\)，再选正 \(r\)，并补 \(r\le\delta\)。第 641 行还明确了 scalar envelope 中使用的 \(\gamma=\alpha\)、\(\lambda=\lambda_0\)、\(\psi(s)=b^{-1/\alpha}s^{1/\alpha}\)，比旧模块消除了一个参数映射的隐含步骤。

自然类的第 1254–1259 行同时保留 \(r\le\delta\) 和额外 contraction check；第 1315–1329 行区分 \(r=\delta\) 的 solution comparison 与完整半径 r 球需采用的 \(\delta=2r\)。未发现半径/直径回归错误。

## 4. 额外 delta：统一 gauge 反例的证明有所增强

旧模块 `t5_sharpness.md` 的最后一段直接使用 S.2 的 limsup 结论。真实合稿第 825 行改为在 \(t_d=B(d)/\lambda_0\) 处直接应用 (3.56)，使

\[
\frac{\psi(t_d)}d\ge\frac{B(d)}{k\lambda_0d}\to+\infty,
\]

而其余两个 endpoint 几何项也趋于无穷。因此推出 \(\widehat R(d)/d\to+\infty\)，并明确不需要 \(\psi(t)\to0\)。这避免向 Theorem 3.3 导入不保证零点连续的 gauge。当前论证成立，属于有益强化，不是新缺陷。

## 5. 本次最终 disposition

旧修复项：5/5 已处理。核心 algebra/sharpness 回归：PASS。当前 A 范围新增阻断项：0。当前 A 范围新增必须修复项：0。

合稿第 1881 行的阶段接受文字属于已有文稿内容，不是本审计员作出的阶段决策。本报告仅把 A 审计范围的意见由“替代模块需修复”更新为“实际上传合稿通过本项核验”。

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review
project_id: RL-PPA-VERIFY
paper_family: T
stage_id: T5
task_id: null
task_status: COMPLETE
inputs_reviewed:
  - T5_AUDIT_A_ALGEBRA.md (prior completed audit)
  - upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md (lines 1-845 and targeted ranges listed in scope)
outputs:
  - /workspace/scratch/01cfe9a021bd/T5_AUDIT_A_FINAL_MANUSCRIPT_DELTA.md
evidence_status:
  - VERIFIED_USER_MATERIAL: actual uploaded manuscript with line-level locators and SHA-256 recorded
  - AI_INFERENCE: independent confirmation of repaired assumptions and preserved algebraic scope
  - EXECUTED_LOCAL: source hash and read-only text checks
assumptions:
  - This is a bounded delta audit against the five prior A findings and the exact/sharp algebra scope
  - No complete-manuscript or bibliography acceptance is inferred
author_input_needed: []
manual_actions: []
quality_checks:
  - A01 nearest-projection quantifier appears in both main theorem and native-energy import
  - A02 effective constant is assigned with :=
  - A03-A05 have no unresolved counterpart in the actual manuscript
  - Scalar feasibility and operator realizability are explicitly distinct
  - Linear endpoint, nonlinear threshold, positive-radius sharpness and limit order verified
  - No source file or stage state modified
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: Replace the obsolete source-module REPAIR disposition with this bounded PASS when synthesizing the actual manuscript audit
stage_acceptance_recommendation: PASS_CANDIDATE
```

唯一下一行动：主协调者在真实合稿的总审计中，将旧 A01–A05 标记为已解决，并采用本份 bounded PASS。
