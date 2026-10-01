# RL foundations 最终独立 proof referee 报告

> 审查对象：`work/RL_foundations_draft.md`  
> 冻结版本：SHA-256 `e24b415afe82ba6a98bd5fd7740bc25f5026da151934cd66d7cfbd22e5924815`  
> 文件状态：47,368 bytes；2,086 行；mtime `2026-09-01 05:58:44.700699475 -0500`  
> 审查纪律：从定义开始 fresh read；不采用作者或前审结论；不查文献；不修改被审稿。

## 1. 最终裁决

**裁决：PASS FOR MATHEMATICAL FREEZE。**

在上述精确 hash 上，未发现 `FAIL`，也未留下需要先改定理陈述或证明才能
成立的 `REPAIR`。30 个编号对象全部通过。特别是下列高风险链条已经闭合：

1. relation / map、full / restricted、coverage / exclusion / invariance
   的量词没有偷换；
2. local gauge--PPA 的 endpoint membership 不依赖未声明的闭性、连续性或
   proximinality；
3. \(L=0\)、\(0<\gamma<1\)、\(\gamma=1\) 三条 power phase 已分开；
4. moving-anchor、fixed-anchor、isolated-zero 与 nonisolated alignment 没有
   相互冒充；
5. upper order、two-sided exact exponent、positive exact Q-factor 已严格分层；
6. GX-071--GX-073 的 operator、零集、residual、Hölder sharpness、invariance
   或 escape 均可独立复算。

这项裁决只表示“当前数学内容可冻结”，不表示新颖性或文献优先权已经证明，
也不把充分常数升级为最优常数。

## 2. 审查方法与严重度

每个编号对象均按以下顺序检查：

- 先核作用域、自然域、空集约定与全称/存在量词；
- 再从恒等式重推结论与常数；
- 再尝试用多值 branch、非闭零集、非 proximinal 集、移动投影与 domain
  escape 构造反例；
- 最后核结论强度是否只是 upper、two-sided，或确有 normalized limit。

状态约定：

- `PASS`：陈述与证明在打印假设下成立；
- `REPAIR`：核心可救，但必须修改明文假设、结论或证明；
- `FAIL`：存在反例或主链不可修补。

严重度分为 `critical / major / moderate / minor / editorial / none`。本次所有
编号项均为 `PASS / none`；第 8 节末的一句局部化表述及两个 oscillatory
example 的复用证明可在语言优化时加强，但不改变任何定理真值。

## 3. 逐编号审查

### 3.1 定义层

| 编号 | 状态 | 严重度 | 独立核查结果 |
|---|---|---|---|
| Definition 0.1 | PASS | none | \(M_\lambda,C_\lambda\) 的反解 (0.1) 精确；不要求 graph 为单值。 |
| Definition 0.2 | PASS | none | full/restricted resolvent 与 reflector 先作为 relations；共同自然域和子 relation 方向正确。 |
| Definition 0.3 | PASS | none | all-pairs、graph-local、solution-anchored 量词完整；空 restriction、\(L=0\) 与自然域 coverage 均另行处理。 |
| Definition 0.4 | PASS | none | residual-windowed gauge 的定义域、base neighborhood 与 residual window 分离；positive power gauge 的缩邻域延拓论证成立。 |
| Definition 0.5 | PASS | none | coverage、remote-branch exclusion、orbit invariance 分别对应 existence、full uniqueness 与迭代合法性，互不替代。 |

Definition 0.4 的 power 延拓在 \(r_F(u)\ge\delta\) 时使用

\[
d(u,S)\le \|u-\bar u\|<\rho\delta^q\le\rho r_F(u)^q,
\]

没有把一般 gauge 误作 power gauge，也没有要求 residual infimum attained。

### 3.2 Minty--Cayley 与代数字典

| 编号 | 状态 | 严重度 | 独立核查结果 |
|---|---|---|---|
| Theorem 1.1 | PASS | none | RL、内积下界、restricted reflector modulus、firm-type inequality 四者精确等价；任一条件在 equal Minty input 时都给 graph-point equality。 |
| Proposition 1.3 | PASS | none | 任意 map \(R:D\to H\) 的 Cayley pullback 都有 \(M_\lambda=x,C_\lambda=Rx\)；即使 first coordinates 重合，生成对象仍是合法 set-valued relation。 |
| Proposition 1.4 | PASS | none | all-pairs 只给 restricted injectivity；\(E\subset D_\lambda(\Gamma)\) 给 existence；(EX) 才升级 full resolvent singleton。 |
| Theorem 2.1 | PASS | none | \(\gamma=1\) tied 参数、inverse 常数与 positive output scaling 全部重算一致。 |
| Proposition 3.1 | PASS | none | \(d(x,S_G)=d(x,S)\) 足以取得 \(S_G\) 中 epsilon-nearest anchors；没有暗用 exact projection。 |

Theorem 1.1 的主恒等式为

\[
\|a-\lambda b\|^2
=\|a+\lambda b\|^2-4\lambda\langle a,b\rangle,
\]

而 firm-type 式来自

\[
\|a\|^2+\|\lambda b\|^2
=\tfrac12\bigl(\|a+\lambda b\|^2+\|a-\lambda b\|^2\bigr).
\]

对 \(\gamma=1\)，重新整理平方不等式得到

\[
\langle a,b\rangle
\ge
\frac{1-L^2}{2\lambda(1+L^2)}\|a\|^2
+\frac{\lambda(1-L^2)}{2(1+L^2)}\|b\|^2,
\]

与 (2.1)--(2.2) 完全一致。inverse 两边都缩放 \(1/\lambda\)，故新常数
确为 \(L\lambda^{\gamma-1}\)；\(cF\) 在步长 \(\lambda/c\) 下逐项回到
原式。

### 3.3 Named-branch local PPA 与 power phase

| 编号 | 状态 | 严重度 | 独立核查结果 |
|---|---|---|---|
| Lemma 4.1 | PASS | none | epsilon-nearest anchor 给 sharp route constant (1/2)；selected residual 只用于上界，full residual 使用 infimum。 |
| Theorem 4.2 | PASS | none | scalar limsup、strict finite-length margin、inductive invariance、Cauchy convergence 与 endpoint membership 全部闭合。 |
| Corollary 5.1 | PASS | none | \(0<\gamma<1,L>0\) 时 upper exponent \(p=\gamma q\)；\(p=1\) 的充分系数是 \(\rho(L/(2\lambda))^q\)。 |
| Corollary 5.2 | PASS | none | \(\gamma=1\) 时保留 \(1+L\)，临界系数为 \(\rho(1+L)/(2\lambda)\)。 |
| Corollary 5.3 | PASS | none | \(L=0\) 时 \(\gamma\)-term 消失，phase 由 \(q\) 而非打印的 \(\gamma q\) 决定。 |

一步链条独立重算为

\[
2\|x-Tx\|\le r+Lr^\gamma,
\qquad
r_F(Tx)\le\frac{r+Lr^\gamma}{2\lambda},
\]

\[
d(Tx,S)\le
\Phi_\gamma(r)
:=\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right).
\]

若 \(\Phi_\gamma(r)\le\theta r\)，则

\[
\sum_{k\ge0}\|x^{k+1}-x^k\|
\le\frac12\left(
\frac{r_0}{1-\theta}
+\frac{Lr_0^\gamma}{1-\theta^\gamma}
\right).
\]

严格 margin 使每个 finite partial orbit 和极限都留在 open input ball。
距离函数只先给 \(d(x^\infty,S)=0\)；稿件随后在同一 interior input 上再次
使用 endpoint-wide A，得到 \(Tx^\infty=x^\infty\)，再由 B 得
\(0\in F(x^\infty)\)。因此没有偷用 \(S\) closed、\(T\) continuous 或
graph closed。

power 情形的准确比较量为

\[
\frac{\Phi_\gamma(r)}r
=\frac{\rho}{(2\lambda)^q}
r^{\gamma q-1}(r^{1-\gamma}+L)^q,
\]

这分别给出 \(\gamma q>1\)、\(=1\)、\(<1\) 三种结论。稿件正确地只把
它称为 upper guarantee；临界常数未被说成必要或最优。

### 3.4 Moving anchor、fixed anchor 与 isolated gauge PPA

| 编号 | 状态 | 严重度 | 独立核查结果 |
|---|---|---|---|
| Theorem 6.1 | PASS | none | output-near anchor 的 \(o(\|w\|)\) 偏差给出 norm ratio 与 vector reflection asymptotic；exact projection 只在 \(e(t)=0\) 时需要。 |
| Corollary 6.2 | PASS | none | power defect 常数 \(2^{q+1}(\rho+c)/\lambda^q\) 由反三角不等式直接得到。 |
| Theorem 7.1 | PASS | none | branchwise residual、resolvent output 与 reflection defect 三种 (q)-flatness 在 graph germ 上等价；打印常数安全但未声称最优。 |
| Proposition 7.2 | PASS | none | arbitrary superlinear gauges 只做 fixed rescaling；literal same-gauge big-(O) 另需 dilation stability。 |
| Proposition 7.3 | PASS | none | locally isolated zero 已缩到 \(d(y,S)=\|y-p\|\)；反向从 branchwise 到 full bound 明确要求 residual completeness。 |
| Theorem 7.4 | PASS | none | nearest-zero output neighborhood \(U\)、有效 input neighborhood \(V_0\)、small residual 与 ball \(\subset V_0\) 均已明文打印。 |
| Corollary 7.5 | PASS | none | general gauge 的 residual argument 和 rescaled input argument 均留在 \([0,\eta_\psi)\)；得到 genuine Q-superlinear upper ratio。 |
| Proposition 7.6 | PASS | none | nonterminating invariant orbit 先给 \(w_k\to0\)；附加 normalized residual limit 才导出 positive exact Q-factor。 |

Theorem 6.1 写 \(a=y-p,t=\lambda w\)，则

\[
\|a\|\le[\psi(\|w\|)+e(\|w\|)]
=\delta_w\|t\|.
\]

由 \(x-p=a+t\)、\(\widehat x-p=a-t\) 可同时得到 (6.4) 与 (6.5)。
Corollary 6.2 再用 \(\|x-p\|\ge\lambda\|w\|/2\)，常数正确。

Theorem 7.4 中，(7.3a) 与 full error bound 给

\[
\|Tx-p\|\le\rho\|w(x)\|^q.
\]

small residual 给

\[
\|x-p\|\ge\lambda\|w(x)\|-\rho\|w(x)\|^q
\ge\frac\lambda2\|w(x)\|,
\]

所以 \(C_q=\rho(2/\lambda)^q\)。\(C_q\delta^{q-1}<1\) 闭合 ball
invariance，递推展开的指数

\[
C_q^{1+q+\cdots+q^{k-1}}
=C_q^{(q^k-1)/(q-1)}
\]

正确。general gauge 情形只需
\(\psi((2/\lambda)r)=o(r)\)，不需要 dilation-stable same-gauge
equivalence。

### 3.5 Nonisolated alignment 与 sharpness

| 编号 | 状态 | 严重度 | 独立核查结果 |
|---|---|---|---|
| Lemma 8.1 | PASS | none | exact projection existence 对整个 envelope family 明文假设；best-anchor drift 给 \(r\le a\le r+\delta\le3a\)。 |
| Theorem 8.2 | PASS | none | projection family、empty supremum、gauge argument domain 与 residual window 均已闭合；power composition 只给 uniform upper \(\theta q\)。 |
| Proposition 8.3 | PASS | none | positive approximate tolerance 确保非 proximinal 情形的 anchor existence；\((1-\kappa)\lambda\) 常数和 gauge domain 正确。 |
| Proposition 9.1 | PASS | none | \(\theta q\) sharpness 必须在同一 sequence joint saturation；three-factor limit 为 \(CB^qA^q\)。 |

对 \(p\in P_S(Jx)\)，

\[
\bigl|\|x-p\|-\lambda\|w\|\bigr|
\le d(Jx,S).
\]

取 infimum 后仍保留双边界，故

\[
|a_J(x)-\lambda\|w\||
\le d(Jx,S)\le\psi(\|w\|).
\]

superlinear 小量条件给 \(\|w\|\le2a_J(x)/\lambda\)，再与
\(a_J(x)\le d(x,S)+\delta_J(x)\) 复合，得到 (8.7)--(8.10)。这里的
\(\theta\) 是 alignment profile 的 exponent，不被 all-pairs RL exponent
自动等同。

approximate-anchor 情形，对每个允许的 (p)，

\[
\|x-p\|\ge\lambda t-d(Jx,S)-e(t)
\ge(1-\kappa)\lambda t,
\]

取 infimum后方向不变，故 (8.13) 成立。

### 3.6 显式 examples

| 编号 | 状态 | 严重度 | 独立核查结果 |
|---|---|---|---|
| Example 9.2 / GX-071 | PASS | none | \(J\) 可逆、\(F=J^{-1}-I\)、\(S\)、full residual、alignment、bounded-tube RL、轨道与 tangential margin 全部复算。 |
| Example 9.3 / GX-072 | PASS | none | \(J\) 为 global triangular homeomorphism；local zero isolated；full \(q\)-MSR、two-sided orbit \(q\)-scale 与 maximal all-pairs \(\gamma\) 证据链完整。 |
| Example 9.4 / GX-073 | PASS | none | \(R(0)=0,\lambda=1,\Gamma_R^1\) 已定义；anchored \(\alpha\)、all-pairs \(\alpha/(\beta+1)\)、linear residual 与 finite domain escape 均成立。 |

GX-071 中 \(\alpha=\gamma q>1\)。直接计算

\[
a_J(x)=\sqrt{r^{2\gamma}+r^2}\sim r^\gamma,
\qquad
\|w\|=\sqrt{r^{2\gamma}+(r-r^\alpha)^2}\sim r^\gamma,
\]

\[
d(Jx,S)=r^\alpha=r^{\gamma q},
\qquad
\frac{d(Jx,S)}{\|w\|^q}\to1.
\]

轨道满足 \(r_{k+1}=r_k^\alpha\)，而
\(\alpha^k\ge1+k(\alpha-1)\) 给出 (9.10) 的 geometric upper sum。

GX-072 的 lower bound 可由下列简单 dichotomy 得到。令
\(A=|x|^q,B=|y|^q\)，且
\(|h(x)|\le A\)。若 \(B\le2A\)，first coordinate 已控制
\(\frac12\max(A,B)\)；若 \(B>2A\)，second coordinate 至少 \(B/2\)。
再用 \(\max(|x|,|y|)\ge\|z\|/\sqrt2\)，得到 (9.12)。因此
\(\|Jz\|=\Theta(\|z\|^q)\)，而 \(w=z-Jz\sim z\)，full residual
scale 确为 (q)。

对 (9.12b) 的相邻 extrema，独立展开得到

\[
|x_n-y_n|\sim\frac\pi\beta s_n^{-1/\beta-1},
\qquad
h(x_n)-h(y_n)\sim2s_n^{-q/\beta},
\]

故 reflector quotient 的极限正是
\(4(\beta/\pi)^\gamma\)。这证明 exponent \(>\gamma\) 失败，但不证明
normalized orbit factor 收敛；稿件的结论强度正确。

GX-073 中，同样的 phase pair 给 reflector quotient 极限
\(2(\beta/\pi)^{\alpha/(\beta+1)}\)。另一方面

\[
r_+=\frac{r+c(r)r^\alpha}{2}>r
\quad(0<r<1),
\]

所以 one-step \(\Theta(r^\alpha)\) 不能称为收敛阶。若轨道永不离开
自然域，单调极限 \(0<\ell<1\) 会满足
\(\ell^{1-\alpha}=c(\ell)\ge1\)，矛盾。最后，所有 local preimages 上

\[
\frac{|u|}{|w|}
=\frac{c(x)+r^{1-\alpha}}{c(x)-r^{1-\alpha}}\to1
\]

一致成立，故对 full residual 取 infimum 后 maximal power 仍为 (1)。

## 4. Remarks、边界与反例陈述

以下未单独编号的边界陈述也通过：

- Remark 1.2 的非闭 graph example 确实只有自然域 ((0,1))，不产生
  maximality、closedness 或 surjectivity；
- Remark 1.5 / GX-074 的自然域是
  \(K=\{0\}\cup\{1/k:k\ge1\}\)，bounded-domain Hölder certificate
  不给 generic input coverage；
- Remark 4.3 的 endpoint conclusion 实际隐含
  \(U\cap\overline S=U\cap S\)，稿件已明说；
- Remark 5.4 没有把 upper recurrence 写成 exact order，也没有把
  finite termination 配上正 Q-factor；
- Section 11 把 novelty、optimality、full-text overlap 与
  application-derived witness 保留为 open，边界正确。

语言优化时可做、但不影响 mathematical freeze 的三项小改进：

1. 在 Proposition 7.2 再加半句“缩小 germ 使重标度后的自变量仍小于
   \(\eta\)”；当前“充分小 graph germ”已足以使公式有定义。
2. 把第 8 节末“isolated zero 时”改成“围绕同一 locally isolated zero
   的充分小 localization 中”，避免脱离本节 local region 阅读。
3. 把 GX-072/073 共用的 oscillatory two-scale upper estimate 抽成一个
   一行 lemma，可减少重复而不改变证明内容。

三项均为 editorial precision，不是 theorem repair，也不应在数学冻结后
引入新 claim。

## 5. 自动与数值 QA

在冻结 hash 上执行的 inventory：

| 检查 | 结果 |
|---|---|
| 编号对象 | 30 个；30 PASS，0 REPAIR，0 FAIL |
| equation tags | 125 个，全部唯一 |
| tag-like references | 65 个，missing 0 |
| numbered-item references | missing 0 |
| inline math delimiters | `\(` 512，`\)` 512 |
| display math delimiters | `\[` 199，`\]` 199 |
| math fragments brace scan | 711 个 fragments，unmatched 0 |
| Markdown tables | escaped-pipe-aware column issues 0 |
| code fences | 0；不存在未闭合 fence |
| control / invisible characters | 0 |
| duplicated equation tags | 0 |

另做 10,000 组随机标量恒等式检查：Theorem 2.1 整理式最大相对浮点误差
\(4.25\times10^{-14}\)，inverse scaling 最大绝对误差
\(2.28\times10^{-13}\)。递推闭式 (7.10) 逐项通过。

GX phase-limit 的数值复算也收敛到稿中常数：

- GX-072：计算 quotient 从 `4.02812394`、`4.02809163`、
  `4.02808878` 收敛到理论值 `4.02808855`；
- GX-073：计算 quotient 从 `1.90420334`、`1.90246150`、
  `1.90228650` 收敛到理论值 `1.90226705`；
- GX-071：随着 \(r\downarrow0\)，\(a_J/r^\gamma\)、
  \(\|w\|/a_J\)、\(d(Jx,S)/\|w\|^q\) 均收敛到 \(1\)。

这些数值检查只用于发现代数或常数错误；最终裁决依据仍是前述解析证明。

## 6. 冻结边界与下一步

可冻结的内容是：定义、Minty--Cayley 等价、\(\gamma=1\) 字典、inverse/
scaling、named-branch local gauge PPA、power phase、moving/fixed-anchor
flatness、isolated gauge PPA、nonisolated alignment composition，以及
GX-071--GX-073 的当前 claim strength。

不可随冻结自动获得的内容是：

- RL 名称或概念的新颖性；
- 现有 sufficient constants 的 necessity / optimality；
- \(\gamma q\) 的 universal law；
- 任意 full-resolvent selection 的 convergence；
- 未查全文来源的排他性 prior-art claim。

建议下一操作是：复制冻结 hash 为数学基线，只做一次不改变公式、量词、
常数和 claim strength 的逻辑/语言优化；任何实质新增定理都另开版本并重新
送 proof review。

## 7. SCI-Skills Expert Contract 1.0

~~~yaml
contract_version: "1.0"
expert_skill: "independent-proof-analysis"
project_id: "monotonicity-regularity-seesaw-2026-09"
paper_family: "T"
stage_id: "T2"
task_id: "RL-FND-FINAL-REF-08"
task_status: "COMPLETE"
inputs_reviewed:
  - "work/RL_foundations_draft.md @ sha256:e24b415afe82ba6a98bd5fd7740bc25f5026da151934cd66d7cfbd22e5924815"
outputs:
  - "work/rl_foundations_final_referee.md"
evidence_status:
  - label: "VERIFIED_ALG"
    item: "Fresh rederivation of every numbered definition, lemma, theorem, proposition, corollary, and example; all 30 numbered items passed."
  - label: "EXECUTED_LOCAL"
    item: "Delimiter, equation-tag, reference, brace, table, control-character, recurrence, random algebra, inverse-scaling, and GX phase-limit checks executed on the frozen hash."
  - label: "AI_INFERENCE"
    item: "Severity classification, mathematical-freeze verdict, and the separation between blocking repairs and editorial optimization are independent referee judgments."
  - label: "NOT_PERFORMED"
    item: "No literature search, novelty claim, journal assessment, or modification of the reviewed draft was performed by instruction."
assumptions:
  - "H is a real Hilbert space and lambda is strictly positive as printed in the draft."
  - "Power and gauge statements use the residual-window and natural-domain conventions printed in Definitions 0.2--0.4."
  - "The review verdict is tied to the exact SHA-256 hash listed above."
author_input_needed: []
manual_actions: []
quality_checks:
  - "Read the frozen draft from Definition 0.1 through Section 11 and re-read every repaired section after the final mtime."
  - "Stress-tested relation versus map, full versus restricted, coverage versus exclusion versus invariance, and named versus arbitrary full selections."
  - "Stress-tested exact and approximate projections, nonclosed solution sets, residual infima, gauge domains, and empty envelopes."
  - "Reproved endpoint membership without S closed, graph closed, or T continuous."
  - "Recomputed all one-step constants, finite-length sums, critical coefficients, inverse/scaling coefficients, q-flatness constants, and normalized limits."
  - "Verified GX-071--GX-073 zero sets, residual scales, sharp Hölder exponents, orbit behavior, and exact-versus-upper claim labels."
  - "Ran Markdown, math-delimiter, equation-tag, cross-reference, brace, table, and control-character inventory checks."
  - "Modified neither the reviewed draft nor any source theorem file."
conflicts: []
conflict_resolution_status: "NONE_OPEN_ON_REVIEWED_HASH"
merge_permission: "orchestrator_only"
stage_acceptance_recommendation: "PASS_FOR_MATHEMATICAL_FREEZE"
recommended_next_action: "Freeze the reviewed hash as the mathematical baseline, then perform language and logical-flow optimization without changing statements, constants, quantifiers, or claim strength."
~~~
