# RL foundations 独立量词与局部 PPA 审稿报告

> 审查对象：**work/rl_foundations_definitions.md** 与
> **work/rl_foundations_ppa_theorem.md**  
> 审查边界：只做数学与量词审查；未检索文献，不评价新颖性，不修改原文件。  
> 总结论：**PASS WITH MINOR REPAIRS**。未发现 critical、major 或
> moderate 数学错误；定义层的核心 Cayley/Minty 逻辑与局部 PPA 定理均闭合。
> 合并前建议完成四项低风险统一，其中只有 Q-01 具有实质定义区分意义。

## 1. 严重度与总览

- **Critical**：核心结论为假，且不能靠局部改写修复。
- **Major**：定理缺少实质假设，或证明有影响主要结论的逻辑断点。
- **Moderate**：结论可保留，但需加入非平凡假设或明显重组证明。
- **Minor**：不影响现有证明，但术语、参数域或边界量词需统一。
- **Editorial**：仅影响可读性或交叉引用。

本次计数：Critical 0，Major 0，Moderate 0，Minor 4，Editorial 2。

## 2. 需要修复的问题

### Q-01 — residual-window gauge 与 neighborhood-only gauge 不无条件同义

- **Severity：Minor（定义学上实质，但不影响 PPA 定理）**
- **定位：** definitions，Definition 6.2，约第 654--676 行，尤其是
  $r_F(u)<\delta$。
- **问题：** 文件冻结的是

  \[
  r_F(u)<\delta\Longrightarrow d(u,S)\leq\psi(r_F(u)),
  \]

  即同时对 $u$ 和 residual 作局部化。对允许有零平台的一般 gauge，它比
  “对所有充分靠近 $\bar u$ 的 $u$”的 neighborhood-only 版本严格更弱。
- **显式反例：** 取 $H=\mathbb R$，

  \[
  F(0)=\{0\},\qquad F(u)=\{1\}\quad(u\ne0).
  \]

  此时 $S=\{0\}$。令 $\psi\equiv0$，取 $\delta=1/2$。窗口条件只在
  $u=0$ 被触发，故成立；但 neighborhood-only 条件会要求
  $|u|\leq0$ 对所有充分小的 $u\ne0$ 成立，故失败。
- **最小修复：** 将公开名称改成
  “residual-windowed local gauge error bound”，或保留现名但立即声明
  本文采用双局部化 convention，跨文献比较时必须打印 residual window。
- **power 情形不受影响：** 若 $\psi(t)=\rho t^q$，窗口版在缩小邻域后
  推出 neighborhood-only 版。取

  \[
  U'\subset U\cap B(\bar u,\rho\delta^q).
  \]

  当 $r_F(u)<\delta$ 用原假设；当 $r_F(u)\geq\delta$ 时，

  \[
  d(u,S)\leq\|u-\bar u\|
  <\rho\delta^q\leq\rho r_F(u)^q.
  \]

  因此 Definition 6.3 与 PPA 的 power corollaries 不需改定理。

### Q-02 — power-RL 的 $L$ 参数域不一致

- **Severity：Minor**
- **定位：** definitions 的 power modulus 取 $L>0$；PPA 第 1 节与
  Proposition 4.1 允许 $L\geq0$。
- **问题：** 所有 PPA 证明对 $L=0$ 仍成立，但基础定义没有把它列为合法
  power certificate。
- **最小修复（二选一）：**

  1. 全文统一为 $L\geq0$，注明 $L=0$ 是退化情形；或
  2. 主理论统一为 $L>0$，把 $L=0$ 单列为 degenerate corollary。

### Q-03 — 空图上的 global RL 语义未冻结

- **Severity：Minor**
- **定位：** definitions 的 Definition 3.1 要求
  $\Gamma\ne\varnothing$，Definition 3.2 又对任意集合值算子取
  $\Gamma=\operatorname{gph}F$。
- **问题：** 当 $\operatorname{gph}F=\varnothing$ 时，global RL 是
  “未定义”还是按全称量词真空成立没有确定。PPA 因 $S\ne\varnothing$
  不受影响。
- **最小修复：** 明确选择 convention。可允许空图真空满足 all-pairs
  inequality，并重申任何算法定理仍需 coverage；也可在 global 定义中明写
  $\operatorname{gph}F\ne\varnothing$。

### Q-04 — output scaling 的解释句需注明比较方向

- **Severity：Minor**
- **定位：** definitions，Proposition 8.3 后约第 910 行。
- **问题：** 命题本身正确；“$c\lambda$ 或 $\lambda/c$”若不标方向，
  容易被误读成两个参数均可随意选。
- **最小修复：** 明写

  \[
  F\text{ at }\lambda
  \Longleftrightarrow cF\text{ at }\lambda/c,
  \qquad
  cF\text{ at }\lambda
  \Longleftrightarrow F\text{ at }c\lambda.
  \]

### Q-05 — “RL 不推出闭性”应补统一见证

- **Severity：Editorial**
- **定位：** definitions 第 9 节反例表约第 925 行。
- **现状：** 判断正确，但该行不像相邻各行那样有显式对象。
- **最小补强：** 取 $H=\mathbb R$，

  \[
  F(u)=\{0\}\quad(0<u<1),\qquad
  F(u)=\varnothing\quad\text{otherwise}.
  \]

  对 $\gamma=1,L=1$ 有 global all-pairs RL；但
  $\operatorname{gph}F=(0,1)\times\{0\}$、$S=(0,1)$ 与
  $D_\lambda(F)=(0,1)$ 均不闭，图也非 maximal。

### Q-06 — tail bound 可多写一行

- **Severity：Editorial**
- **定位：** PPA，Theorem 3.1 证明末尾约第 368--369 行。
- **现状：** (3.9) 正确；但已打印的 (3.12) 从 $r_0$ 出发。
- **最小补强：** 先写

  \[
  r_{k+j}\leq\theta^j r_k\qquad(j\geq0),
  \]

  再从 $j=0$ 求和，直接得到
  $\|x^k-x^\infty\|\leq B_\gamma(r_k,\theta)$。

## 3. 核心定义与代数逐项 PASS

| 项目 | 判定 | 独立核查要点 |
|---|---|---|
| Minty/Cayley 坐标重构 | **PASS** | $u=(M+C)/2$、$u^*=(M-C)/(2\lambda)$，无附加假设。 |
| full resolvent/reflected relation | **PASS** | 自然域恰为 $\operatorname{ran}(I+\lambda F)$；未偷用满域或单值。 |
| restricted relations | **PASS** | 均为 full relation 的子 relation；同一 $x,u$ 唯一决定 $u^*=(x-u)/\lambda$。 |
| relational fixed points | **PASS** | $x\in J(x)\iff0\in F(x)$；restricted 版准确多出 $(x,0)\in\Gamma$。 |
| graph-local / Minty-local | **PASS** | 两类 locality 的 graph 与 input 量词已分开。 |
| all-pairs / anchored / solution-anchored | **PASS** | moving--moving 与 moving--anchor 的 universal quantifiers 清楚，未混用。 |
| RL 内积形式 | **PASS** | 由平方恒等式双向推出，平方不改变方向。 |
| Minty injectivity | **PASS** | 同 Minty input 使右端为 $\omega(0)=0$，再由 $M,C$ 重构 graph pair。 |
| restricted $J,R$ 的 map 性质 | **PASS** | 只在 $D_\lambda(\Gamma)$ 上声称 map，没有隐含 coverage $=H$。 |
| Cayley pullback | **PASS** | 构造中 $M=x,C=Rx$，故双向等价严格成立。 |
| firm-type characterization | **PASS** | 左侧恰为 $\frac12(\|x-y\|^2+\|Rx-Ry\|^2)$；coupled selections 在 $x=y$ 时强迫单值。 |
| $\gamma=1$ 字典 | **PASS** | tied coefficients 与 Luke--Tam coefficient 均正确。 |
| inverse rule | **PASS** | 新常数 $L\lambda^{\gamma-1}$；反演两次恢复 $L$。 |
| output scaling | **PASS** | 正确新步长为 $\lambda/c$；仅需 Q-04 的方向说明。 |

具体地，

\[
\|a-\lambda b\|^2
=\|a+\lambda b\|^2-4\lambda\langle a,b\rangle
\]

给出 Proposition 4.1；而

\[
\|a\|^2+\|\lambda b\|^2
=\frac12\bigl(\|a+\lambda b\|^2+\|a-\lambda b\|^2\bigr)
\]

给出 firm-type identity。$\gamma=1$ 时核得

\[
\mu_L=\frac{1-L^2}{2\lambda(1+L^2)},\qquad
\rho_L=\frac{\lambda(1-L^2)}{2(1+L^2)},\qquad
\tau_L=\frac{L^2-1}{4}.
\]

上述恒等式另用 Python Fraction 与多参数数值断言复算，全部通过。

## 4. Coverage、exclusion 与 set-valued branch

| 逻辑环节 | 判定 | 说明 |
|---|---|---|
| restricted uniqueness | **PASS** | all-pairs RL 只给 $M_\lambda|_\Gamma$ 单射。 |
| input coverage | **PASS** | $E\subset D_\lambda(\Gamma)$ 独立打印。 |
| full-branch exclusion | **PASS** | Minty input 落在 $E$ 的 full graph points 全部纳入 $\Gamma$。 |
| full resolvent equality | **PASS** | coverage 给存在，exclusion 拉回 $\Gamma$，injectivity 给唯一。 |
| self-map/invariance | **PASS** | 未从 RL 自动推出；PPA 用 finite-length margin 闭合。 |

最小反例也正确：$\Gamma=\{(0,0)\}$ 不覆盖任何 input neighborhood；
向 full graph 加入 $(1,-1/\lambda)$ 后，restricted branch 仍唯一，而
$J_{\lambda F}(0)$ 多值。

## 5. 局部 gauge--PPA 定理逐链审查

### 5.1 Assumption B

**PASS。** $\sigma:U\to G$ 是明确给定的 graph-pair map，不是从 RL
偷得的逆。由 $M_\lambda\sigma(x)=x$ 得

\[
Vx=(x-Tx)/\lambda\in F(Tx),\qquad Tx\in J_{\lambda F}(x).
\]

这足以定义 named iteration，但不控制 full resolvent 的 remote
selections；正文准确保留了该边界。

### 5.2 Assumption A 与 proximinality

**PASS。** 对每个 active $x$，先存在一条可依赖于 $x$ 的
$\varepsilon$-nearest sequence，再要求 anchored inequality 沿整条
sequence 成立。证明只令 $n\to\infty$，没有使用 $P_Sx$，也没有假设
$S$ 闭、凸或 proximinal。

当 $d(x,S)=0$ 时，A+B 自动给

\[
\|x-Tx\|\leq\tfrac12(0+L0^\gamma)=0.
\]

故 A+B 本身蕴含
$\{x\in U:d(x,S)=0\}\subset S$。这正是 endpoint membership 的有效
机制，不是循环论证。

### 5.3 Lemma 2.1

**PASS。** 恒等式

\[
2(x-Tx)=(x-p_n)-(2Tx-x-p_n)
\]

给出精确的 $1/2$ step bound；B 给 selected residual
$\|(x-Tx)/\lambda\|$，E 只在 $Tx$ 使用，再借 $\psi$ 非减得到

\[
d(Tx,S)\leq
\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right).
\]

没有把 selected residual 错写成 minimal residual 的等号。

### 5.4 Theorem 3.1：contraction、invariance 与 finite length

**PASS。** 从 limsup $<1$ 可选统一
$\Phi_\gamma(r)\leq\theta r$；归纳得到
$r_k\leq\theta^k r_0$。step sum 是两个几何级数：

\[
\sum_k\|x^{k+1}-x^k\|
\leq\frac12\left(
\frac{r_0}{1-\theta}
+\frac{Lr_0^\gamma}{1-\theta^\gamma}
\right).
\]

严格 outer-radius margin 保证每个下一 iterate 以及极限均在开球 $U$；
因此没有隐含 $T(U)\subset U$。Hilbert 完备性随后给 norm limit。

### 5.5 Endpoint membership

**PASS。** finite length 只先给 $d(x^\infty,S)=0$，正文没有把这一步
误写成 $x^\infty\in S$。严格 margin 给 $x^\infty\in U$，而 A 覆盖所有
active inputs，故可在 $x^\infty$ 再用 one-step bound 得
$Tx^\infty=x^\infty$。B 随后给 $0\in F(x^\infty)$。所以不需 $S$ 闭、
graph closed 或 $T$ 连续。

若 A 只沿轨道成立，则需要另外用局部 $S$ 闭，或用足以把 fixed-point
identity 传到极限的连续性/闭图条件；正文已正确提示这一边界。

### 5.6 Proposition 4.1 与 full branch

**PASS。** all-pairs RL on $G$ 给 restricted Minty injectivity；
coverage $U\subset M_\lambda(G)$ 才给 branch 存在；
$d(x,S_G)=d(x,S)$ 才能从 $G$ 中抽出 nearest-anchor sequence；条件
(4.6) 再单独排除 $G$ 外的 full selections。四层量词没有互相替代。

### 5.7 Power corollaries

**PASS。** 对 $0<\gamma<1,L>0$，

\[
r+Lr^\gamma=r^\gamma(r^{1-\gamma}+L)
\]

给出 upper exponent $p=\gamma q$。当 $p>1$ 可缩小半径得到
contraction；当 $p=1$ 的极限系数为

\[
\kappa_\gamma=\rho\left(\frac{L}{2\lambda}\right)^q;
\]

当 $p<1$ 明确只是不推出结论。对 $\gamma=1$，系数正确保留 $1+L$：

\[
A_1=\rho\left(\frac{1+L}{2\lambda}\right)^q.
\]

rate 结论均是 one-step upper order，没有升级为 exact order 或 sharp
threshold；非终止轨道上的 ratio limsup 也已正确限定。

## 6. 最小合并建议

在不改变核心证明的前提下，合并稿只需：

1. 处理 Q-01 的 gauge 命名，并写明 power window 的可缩邻域等价；
2. 统一 $L>0$ / $L\geq0$；
3. 冻结空图 convention；
4. 加入 Q-04 的双向 scaling 读法；
5. 可选加入 Q-05 的闭性反例与 Q-06 的 shifted tail 一行。

完成 1--4 后，建议把 definition layer、Lemma 2.1、Theorem 3.1、
Proposition 4.1 与 Corollaries 5.1--5.2 送入最终整合稿。无需增加闭性、
proximinality、full-resolvent uniqueness 或 global self-map 假设。

## 7. SCI-Skills Expert Contract 1.0

~~~yaml
contract_version: "1.0"
expert_skill: "independent-proof-analysis"
project_id: "monotonicity-regularity-seesaw-2026-09"
paper_family: "T"
stage_id: "T2"
task_id: "RL-FND-REF-Q-06"
task_status: "COMPLETE"
inputs_reviewed:
  - "work/rl_foundations_definitions.md"
  - "work/rl_foundations_ppa_theorem.md"
outputs:
  - "work/rl_foundations_referee_quantifiers.md"
evidence_status:
  - label: "VERIFIED_ALG"
    item: "Every Cayley/Minty identity, gamma=1 coefficient, inverse/scaling rule, one-step recurrence, localization sum, endpoint argument, and power coefficient was independently rederived."
  - label: "EXECUTED_LOCAL"
    item: "Fraction-based exact checks passed for the firm and gamma=1 coefficient identities; multi-parameter numerical checks passed for the inverse coefficient."
  - label: "AI_INFERENCE"
    item: "Severity, terminology, and merge recommendations are independent mathematical-referee judgments."
  - label: "NOT_PERFORMED"
    item: "No literature search or novelty assessment was performed by instruction."
assumptions:
  - "The reviewed files are the exact versions present in the shared workspace during this audit."
  - "H is a real Hilbert space and lambda is strictly positive."
  - "Metric subregularity in Definition 6.2 is interpreted with the project's printed residual-window convention."
author_input_needed: []
manual_actions: []
quality_checks:
  - "Read both files in full and audited every definition, proposition, theorem, corollary, and counterexample entry."
  - "Stress-tested set-valued relation semantics and the natural Minty domain."
  - "Separated restricted injectivity, input coverage, full-branch exclusion, and invariance."
  - "Stress-tested all-pairs, anchored, and epsilon-nearest-anchor quantifiers."
  - "Verified that no proximinality or closedness is hidden in the one-step proof."
  - "Reproved endpoint membership without assuming S closed or T continuous."
  - "Checked all power exponents and critical coefficients separately for gamma<1 and gamma=1."
  - "Distinguished upper order, exact order, necessity, and sharpness."
  - "Modified neither reviewed source file and performed no literature search."
conflicts:
  - conflict_id: "RL-REF-Q01"
    conflict_type: "definition_convention"
    claim: "Residual-window gauge subregularity is automatically identical to every neighborhood-only convention."
    source_or_locator: "work/rl_foundations_definitions.md, Definition 6.2"
    competing_values_or_interpretations:
      - "Residual-windowed gauge error bound adopted in the project."
      - "Neighborhood-only gauge inequality without a residual cutoff."
    recommended_resolution: "Name the convention explicitly and state shrinkage equivalence separately for positive power gauges."
  - conflict_id: "RL-REF-Q02"
    conflict_type: "parameter_domain"
    claim: "The RL constant domain is uniform across the definition and PPA files."
    source_or_locator: "definitions power modulus; PPA Section 1"
    competing_values_or_interpretations:
      - "L>0 in the definition layer."
      - "L>=0 in the PPA layer."
    recommended_resolution: "Choose one public convention and isolate L=0 if retained."
conflict_resolution_status: "MINOR_REPAIRS_PENDING"
merge_permission: "orchestrator_only"
stage_acceptance_recommendation: "PASS_WITH_MINOR_REPAIRS"
recommended_next_action: "Apply Q-01--Q-04 during foundations integration; preserve Lemma 2.1 and Theorem 3.1 apart from the optional one-line tail expansion."
~~~
