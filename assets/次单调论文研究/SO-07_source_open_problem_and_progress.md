# SO-07：退化预条件 PPA 的真实值域覆盖

## 原始出处、公开问题背景与截至 2026-09-08 的已有进展

项目：RL–PPA–VERIFY  
任务：M2 / SO-07 文献扫雷  
证据等级：原文定理级核验 + 项目内严格推导  

---

## 0. 结论先行

SO-07 是一个有明确作者出处的公开研究方向；本次检索尚未发现其一般形式已被解决的证据，但这不构成全球不存在性证明。准确地说：

> Xue–Zhang 已经抽象刻画了退化预条件 resolvent 何时具有全定义域；作者明确留下的是闭包值域、真实值域与 strong-relative-interior 条件之间的关系。本项目把这一方向强化为：怎样从更原生、可检查的算子信息出发，把“闭包意义下几乎覆盖”升级为真实值域覆盖。

设

\[
\mathcal T=(\mathcal A+\mathcal Q)^{-1}\mathcal Q,
\qquad
\mathcal Q\succeq0,
\qquad
\ker\mathcal Q\ne\{0\}.
\]

算法能够接受任意输入，等价于

\[
\operatorname{ran}\mathcal Q
\subseteq
\operatorname{ran}(\mathcal A+\mathcal Q).
\tag{SO-07.1}
\]

在 \(\mathcal A\) 最大单调、\(0\in\operatorname{ran}\mathcal A\) 等条件下，Xue–Zhang 只能无条件得到

\[
\operatorname{ran}\mathcal Q
\subseteq
\overline{\operatorname{ran}(\mathcal A+\mathcal Q)}.
\tag{SO-07.2}
\]

从 (SO-07.2) 到 (SO-07.1) 的缺口是“极限右端可以被任意逼近，但对应方程未必真正有解”。这不是形式问题：他们引用并重新分析的二维最大单调反例恰好满足闭包覆盖，却在 \(\operatorname{ran}\mathcal Q\) 的一整段右端上没有解。

截至本次核验：

- **公开问题身份：VERIFIED。** 最终接受稿仍在 Proposition 14 后明确写明这一关系留作 future work。
- **一般问题：未见已解决证据。** 定向检索没有发现一个覆盖一般非多面最大单调算子的原生、可核 actual-coverage 定理；这不是全球不存在性证明。
- **有限维 piecewise-polyhedral 子类：ALREADY COVERED。** Li–Rockafellar–Sun 2026 的投影/限制最大单调性定理无需 relative-interior CQ，能直接闭合这一完整子类。
- **若干强结构子类：ALREADY COVERED。** 现成 warped-resolvent 条件包括 surjectivity、强单调、带增长模要求的 uniform monotonicity、bounded-domain，以及特定 finite-valued coercive-convex subdifferential 情形。
- **与 T5 的关系：严格但非直接。** SO-07 解决 T5 必须单独假设的 coverage；它本身不产生误差界。经标准降维后可以得到一个普通 Euclidean PPA；在当前 restricted-monotone + full-domain 框架中，RL 自动取 \((\gamma,L)=(1,1)\)，不会产生 genuine 非 Lipschitz 几何。

因此，SO-07 值得攻，但只有得到一个严格超出上述已知子类、并覆盖自然非多面/多值模型的定理，才不是小打小闹。

---

## 1. 为什么这个问题重要

### 1.1 退化预条件并非病态装饰

许多 splitting 方法写成预条件 PPA 后，预条件矩阵天然只有半正定而非正定。Douglas–Rachford、某些 ADMM、Chambolle–Pock、图分裂和最小 lifting 构造都可能出现这种情况。退化性用于消去冗余变量或降低 lifting 维数，因此往往正是算法结构的来源。

经典 PPA 中，最大单调性通过 Minty 定理保证

\[
\operatorname{ran}(I+\mathcal A)=\mathcal H,
\]

所以 resolvent 对每个输入有定义。把 \(I\) 换成奇异的 \(\mathcal Q\) 后，这一结论不再成立；\(\mathcal Q\) 在核方向不提供任何强制增长，最大单调性本身也不能阻止隐变量逃逸。

### 1.2 coverage 是算法存在性的门槛

给定输入 \(x\)，一步迭代要求求解

\[
\mathcal Qx\in (\mathcal A+\mathcal Q)y.
\]

因此全定义域恰好是 (SO-07.1)。若只有闭包覆盖，则可以找到残差趋于零的近似解，却不能保证存在任何真正的下一步。收敛率、Fejér 性、RL、误差界都不能替代这一步存在性。

### 1.3 多值性使“存在”与“唯一”必须分开

对 \(\mathcal T=(\mathcal A+\mathcal Q)^{-1}\mathcal Q\)：

- actual range coverage 解决每个输入是否至少有一个输出；
- restricted injectivity 解决输出在核方向是否唯一；
- restricted monotonicity只保证值域分量的单值性/firm geometry，不自动补齐完整输出。

任何把 SO-07 说成“一步证明 \(\mathcal T\) well-defined”的结果，都必须另行核对 single-valuedness；coverage 本身只解决 existence。

---

## 2. 原始出处与版本交叉核对

### 2.1 基础框架的出处

退化预条件 PPA 的系统框架来自：

- K. Bredies, E. Chenchene, D. A. Lorenz, E. Naldi, *Degenerate Preconditioned Proximal Point Algorithms*, SIAM Journal on Optimization 32(3), 2376–2401 (2022), [arXiv:2109.11481](https://arxiv.org/abs/2109.11481), [PDF](https://arxiv.org/pdf/2109.11481).

其 Definition 2.1 把“admissible preconditioner”定义为：\(\mathcal Q\) 线性、有界、自伴、半正定，且 \((\mathcal Q+\mathcal A)^{-1}\mathcal Q\) 单值并具有全定义域。Remark 2.2 明确指出，即使 \(\mathcal A\) 最大单调，退化情形也不能自动保证这一点；原文因此把 admissibility 当作假设。

### 2.2 SO-07 的直接原始出处

直接出处是：

- F. Xue, H. Zhang, *On Degenerate Preconditioned Proximal Point Methods under Restricted Monotonicity*, Journal of Optimization Theory and Applications 208, article 74 (2026), DOI [10.1007/s10957-025-02915-x](https://link.springer.com/article/10.1007/s10957-025-02915-x); [arXiv:2401.08431](https://arxiv.org/abs/2401.08431), [v5 HTML](https://arxiv.org/html/2401.08431v5), [PDF](https://arxiv.org/pdf/2401.08431).

书目信息经官方页面核对：arXiv v1 提交于 2024-01-16，v5 修订于 2025-12-12；正式论文于 2025-12-30 在线发表，编入 JOTA 208、article 74 (2026)。

SO-07 是本项目内部编号，不是原论文中的问题编号。原论文没有单列“Open Problem”；公开问题是 v5 §3.2 Proposition 14 后的作者陈述。

### 2.3 精确位置与编号

以 arXiv v5 为准：

| 位置 | 已证内容 | SO-07 中的角色 |
|---|---|---|
| Assumption 1 | \(\mathcal Q\) 有界、线性、自伴、半正定、退化且值域闭 | 退化度量环境 |
| Definition 3 / Assumption 2 | \(\operatorname{gph}\mathcal A\cap(\mathcal H\times\operatorname{ran}\mathcal Q)\) 的 restricted monotonicity 及基本 viability | 保证 range component 的单调几何 |
| Lemma 10 | 在 \(V=\operatorname{ran}\mathcal Q\) 上的 restricted Minty theorem | 将 maximality 与 full Minty range 等价 |
| Theorem 11 | \(\operatorname{dom}\mathcal T=\mathcal H\) 当且仅当 \(P_V\mathcal A^{-1}|_V\) 在 \(V\) 上最大单调 | 全定义域的抽象精确刻画 |
| Assumption 4 | \(\mathcal A\) 最大单调且 \(0\in\operatorname{sri}(\operatorname{ran}\mathcal Q-\operatorname{ran}\mathcal A)\) | 强的全局 CQ |
| Corollary 13 | Assumption 4 推出 projected inverse 最大单调，故推出 full domain | 已知充分条件 |
| Proposition 14 | 若再有 \(0\in\operatorname{ran}\mathcal A\)，则得到闭包覆盖 (SO-07.2) | “几乎覆盖” |
| Proposition 14 后正文 | actual range inclusion 不必成立，闭包值域与真实值域的关系困难，和 Assumption 4(ii) 的潜在联系留待 future work | 公开问题原句所在位置 |
| Definition 16 / Theorem 18 | restricted injectivity 与完整 \(\mathcal T\) 单值性的条件 | 与 coverage 独立的第二门槛 |

旧版本与最终版本的定理编号发生过变化。引用时应优先写“v5 Theorem 11 / Corollary 13 / Proposition 14”或直接引用 §3.1–3.2，避免沿用早期稿中的编号。

---

## 3. 原论文到底已经解决了什么

令

\[
V:=\operatorname{ran}\mathcal Q,
\qquad
\mathcal B_V:=P_V\circ\mathcal A^{-1}|_V:V\rightrightarrows V.
\]

在 Xue–Zhang 的 restricted-monotonicity 假设下：

\[
\boxed{
\operatorname{dom}\big((\mathcal A+\mathcal Q)^{-1}\mathcal Q\big)=\mathcal H
\iff
\mathcal B_V\text{ 在 }V\text{ 上最大单调}.
}
\tag{SO-07.3}
\]

所以“full domain 有没有抽象刻画”并不是开放问题；答案已经是 (SO-07.3)。

实际缺口是：给定 \(\mathcal A\) 的原生描述，例如 subdifferential、normal cone、分支/活动集、增长或 recession 信息，怎样不用先知道整个 \(\mathcal B_V\) 的图，就验证其最大单调性或直接验证 (SO-07.1)。

原论文提供的标准答案是全局 CQ

\[
0\in\operatorname{sri}
\big(\operatorname{ran}\mathcal Q-\operatorname{ran}\mathcal A\big),
\tag{SO-07.4}
\]

但其 Example 3 说明 (SO-07.4) 不是 full domain 的必要条件。另一方面，来自 Bredies 等的 exponential counterexample 说明，删除 (SO-07.4) 后也不能无条件得到 full domain。

这就留下一个非空且非平凡的中间地带。

---

## 4. 公开问题的保守表述与本项目的强化表述

### 4.1 作者明确留下的版本（VERIFIED）

在 \(\mathcal A\) 最大单调、\(\mathcal Q\) 退化半正定且值域闭、并满足原文 viability/restricted monotonicity的框架内，研究

\[
\overline{\operatorname{ran}(\mathcal A+\mathcal Q)}
\quad\text{与}\quad
\operatorname{ran}(\mathcal A+\mathcal Q)
\]

之间的关系，以及它与 strong-relative-interior 条件 (SO-07.4) 的联系。

### 4.2 本项目要交给 PRO 的强化版本（PROJECT FORMULATION）

有限维优先。寻找由 \(\mathcal A\) 与 \(\mathcal Q\) 的原生、可检查结构推出

\[
\operatorname{ran}\mathcal Q
\subseteq
\operatorname{ran}(\mathcal A+\mathcal Q)
\]

的定理，并满足：

1. 不只是重述 (SO-07.3)；
2. 不把 actual coverage 或 restricted maximality 本身放回假设；
3. 严格超出 global sri/ri CQ、piecewise-polyhedral、强单调、带增长模条件的一致单调、特定 coercive-convex、bounded-domain 等已知路径中的至少一个实质维度；
4. 覆盖自然的非多面且最好真正多值的算子类；
5. 给出反例或必要性边界，说明结论不是一个隐藏的经典 CQ；
6. 若声称完整 \(\mathcal T\) well-defined，另证 single-valuedness；
7. 若接入 T5，必须经过同一实际 reduced operator、同一范数、同一目标集的严格转换。

本项目强化了验收要求；不能把这些强化条件反向归因给 Xue–Zhang 原文。

---

## 5. 已有进展与必须排除的重做区域

### 5.1 通用 warped-resolvent 条件

Bùi–Combettes 的 warped resolvent 定义本来就是

\[
J^K_M=(K+M)^{-1}K.
\]

其 Proposition 3.8 把 viability 分为 \(\operatorname{ran}K\subseteq\operatorname{ran}(K+M)\) 与 \(K+M\) 的 injectivity；Proposition 3.9 给出若干 coverage 充分条件，包括：

- \(K+M\) surjective；
- \(K+M\) 最大单调且 \(D\cap\operatorname{dom}M\) 有界；
- \(K+M\) 最大单调，并且或者 uniform monotone 且其模满足 \(\phi(t)/t\to+\infty\)，或者强单调；
- \(K\) 最大单调且 \(M=\partial\varphi\)，其中 \(\varphi:X\to\mathbb R\) 是有限值、下半连续、coercive convex 函数。

来源：M. N. Bùi, P. L. Combettes, *Warped Proximal Iterations for Monotone Inclusions*, JMAA 491 (2020), 124315, [作者 PDF](https://pcombet.math.ncsu.edu/jmaa5.pdf), Propositions 3.8–3.9。

任何新结论若只是这些条件在 \(K=\mathcal Q\)、\(M=\mathcal A\) 下的改写，不构成 SO-07 的实质推进。

### 5.2 代表函数与 closedness-type CQ

Boţ–Grad 已用 Fitzpatrick/representative functions 给出 maximal-monotone sums 的值域/满射刻画和 closedness-type 充分条件，并明确比较了比经典 interiority 条件更弱的情形。

来源：R. I. Boţ, S.-M. Grad, *Closedness Type Regularity Conditions for Surjectivity Results Involving the Sum of Two Maximal Monotone Operators*, [arXiv:1007.3652](https://arxiv.org/html/1007.3652v1), 尤其 Theorems 3、6 及相关 surjectivity 推论。

这套理论对单个右端给出必要充分的代表函数刻画，并给出满射充分条件。任何正确的 coverage 定理最终当然会满足其必要充分刻画，所以不能要求新结果“落在该刻画之外”。真正的新颖性门槛是：不得只重述抽象 exactness/lower-semicontinuity 条件或直接套用其现成充分推论；应从更原生的信息验证这些条件，或产生一个新的可检查充分类。仅宣称“比 sri 弱”不够。

### 5.3 parallel composition / infimal postcomposition

Xue–Zhang 的 reduced operator 是一个 parallel composition。该运算的 resolvent、最大单调性和凸函数 infimal postcomposition 已有专门理论：

- L. M. Briceño-Arias, F. Roldán, *Resolvent of the Parallel Composition and Proximity Operator of the Infimal Postcomposition*, Optimization Letters 17, 399–412 (2023), [arXiv:2109.06771](https://arxiv.org/abs/2109.06771).

因此，新结果不能只把 projected inverse 改名为 parallel composition，或重复已有 mild qualification condition。

### 5.4 2026 年 piecewise-polyhedral 闭合结果

Li–Rockafellar–Sun 证明：在有限维空间中，对最大单调且 piecewise-polyhedral 的映射，projection、argument restriction、linear pullback 和 sum 在仅有非空可行交条件时保持最大单调，无需 classical relative-interior CQ。

来源：X. Li, R. T. Rockafellar, D. Sun, *Maximal Monotonicity of Piecewise Polyhedral Mappings*, [arXiv:2607.07358](https://arxiv.org/abs/2607.07358), [HTML](https://arxiv.org/html/2607.07358v1), Theorems 3.3 and 4.1。

这给出关闭 SO-07 如下子类的一条通用 preservation-calculus 路径。

**推论（项目推导，PROVED）。** 设空间有限维，\(\mathcal A\) 最大单调且 piecewise polyhedral，\(V=\operatorname{ran}\mathcal Q\)，并且

\[
V\cap\operatorname{ran}\mathcal A\ne\varnothing.
\]

则

\[
P_V\mathcal A^{-1}|_V
\]

在 \(V\) 上最大单调且 piecewise polyhedral。若再满足 Xue–Zhang 的退化预条件假设，则 \(\mathcal T\) 具有全定义域。

**理由。** \(\mathcal A^{-1}\) 仍为最大单调 piecewise-polyhedral 映射。对 \(M=\mathcal A^{-1}\) 和子空间 \(V\) 使用 Li–Rockafellar–Sun Theorem 4.1(a)，非空交条件恰为 \(V\cap\operatorname{dom}\mathcal A^{-1}=V\cap\operatorname{ran}\mathcal A\ne\varnothing\)。所得 argument restriction 正是 \(P_V\mathcal A^{-1}|_V\)。再用 Xue–Zhang Theorem 11。

特别地，若 \(0\in\operatorname{ran}\mathcal A\)，非空交自动成立。因此，有限维 PLQ subdifferentials、polyhedral normal cones 及完整 piecewise-polyhedral 最大单调类不能再作为 SO-07 的新正例主类。

这一子类还可由更短的闭值域论证闭合，并不依赖“等到 2026 才解决”：有限维 piecewise-polyhedral \(\mathcal A\) 使 \(\operatorname{ran}(\mathcal A+\mathcal Q)\) 成为有限个多面体的并，因而闭；在 \(0\in\operatorname{ran}\mathcal A\) 时，Xue–Zhang Proposition 14 的 closure coverage 立即升级为 actual coverage。若只知某个 \(a_0\in V\cap\operatorname{ran}\mathcal A\)，可对平移算子 \(\mathcal A-a_0\) 使用同一论证，并利用 \(V+a_0=V\)。Li–Rockafellar–Sun 的意义是同时提供了更系统的投影/限制最大单调性演算。

### 5.5 后续算法文献中的验证瓶颈

Xue–Zhang 的引言明确列出：Bredies 等首先把 full domain 与 single-valuedness 纳入 admissible-preconditioner 假设；后续若干工作仍假定 full domain、单值连续，或只在特定 splitting 的更新公式中验证。这说明 verification bottleneck 实际存在；但“后续论文仍假设它”本身不是新定理证据，任何具体范围陈述都应随引用逐篇核对。

---

## 6. 对 subdifferential 类的精确翻译

若 \(\mathcal A=\partial f\)，其中 \(f\) proper、闭、凸，则对每个 \(q\in V=\operatorname{ran}\mathcal Q\)：

\[
q\in\operatorname{ran}(\partial f+\mathcal Q)
\]

当且仅当参数化凸函数

\[
x\longmapsto
f(x)+\frac12\langle x,\mathcal Qx\rangle-\langle q,x\rangle
\tag{SO-07.5}
\]

取得最小值。

所以在 subdifferential 情形，SO-07 也是一个“沿所有 \(q\in V\) 的统一 attainment”问题。\(\mathcal Q\) 只在 \(V\) 方向提供二次控制，在 \(\ker\mathcal Q\) 方向没有强制增长；真正困难的是核方向 recession/逃逸与 range 方向载荷之间的耦合。

这是一条等价翻译，不是新 coverage 定理，也不应作为给 PRO 规定的证明路线。

---

## 7. SO-07 与 T5/RL–PPA 的严格接口

### 7.1 coverage 先于 RL 和误差界

T5 明确区分：

1. Minty 图的 injectivity / RL geometry；
2. 输入 coverage；
3. 输出 error bound；
4. 轨道 localization。

SO-07 只负责第 2 项。即使已经有完整 RL 与误差界，对于任何一个未覆盖输入仍然没有 PPA 下一步。

### 7.2 不能直接在 \(\mathcal Q\)-半范数中套 Euclidean T5

原退化迭代的几何写成

\[
\|x\|_{\mathcal Q}=\sqrt{\langle \mathcal Qx,x\rangle},
\]

这是半范数，在 \(\ker\mathcal Q\) 上为零。T5 当前固定的是有限维 Euclidean PPA。未经降维或显式 metric conversion，不能把 \(\mathcal Q\)-firm nonexpansiveness 当作 T5 的 Euclidean AP-RL。

### 7.3 正确接法是 reduced operator

按 Xue–Zhang Fact 3 与 §6，取某个实 Hilbert 空间 \(\mathcal H'\) 和有界满射

\[
\mathcal C:\mathcal H\to\mathcal H',
\]

使得

\[
\mathcal Q=\mathcal C^{\top}\mathcal C
\]

并在 reduced space 定义

\[
F_{\mathrm{red}}
:=
\mathcal C\triangleright\mathcal A
=
\big(\mathcal C\mathcal A^{-1}\mathcal C^{\top}\big)^{-1}.
\]

则 reduced transition 为

\[
\widetilde{\mathcal T}
=
\mathcal C(\mathcal A+\mathcal C^{\top}\mathcal C)^{-1}\mathcal C^{\top}
=J_{F_{\mathrm{red}}}.
\tag{SO-07.6}
\]

令 \(c^k=\mathcal Cx^k\)。Xue–Zhang Propositions 24–26 给出

\[
c^{k+1}=\widetilde{\mathcal T}c^k,
\qquad
c^k-c^{k+1}\in F_{\mathrm{red}}(c^{k+1}),
\]

以及原 full-domain coverage 与 reduced resolvent 的 full domain 等价。要接入当前 T5，还必须要求 \(\mathcal H'\) 有限维，并另有 \(\operatorname{zer}\mathcal A\ne\varnothing\)。在这些附加条件下，这是步长 \(\lambda_{\mathrm{T5}}=1\) 的 Euclidean PPA，而且

\[
\|\mathcal Cx\|=\|x\|_{\mathcal Q},
\qquad
S_{\mathrm{red}}
=\operatorname{zer}F_{\mathrm{red}}
=\mathcal C(\operatorname{zer}\mathcal A).
\]

若不另证 \(\operatorname{zer}\mathcal A\ne\varnothing\)，coverage 只说明每个输入存在下一步，不能提供 T5 所需的非空目标集。

于是，一个 SO-07 coverage 定理可以准确补入 T5 的 coverage 槽位。若要改用任意 T5 步长 \(\lambda>0\)，应定义 \(F_{\mathrm{T5}}=F_{\mathrm{red}}/\lambda\)，并同步转换残差误差界常数；这只是归一化，不能凭缩放制造更强的收敛结论。

在当前 restricted-monotone + full-domain 框架中，\(F_{\mathrm{red}}\) 最大单调，所以 AP-RL 自动成立，可取 \((\gamma,L)=(1,1)\)。随后调用 T5 时仍须对同一个 \(F_{\mathrm{red}}\) 独立验证 ordinary error bound，核对同一 Euclidean norm、同一目标集、同一图块/输出域和共同正半径。只有离开这一单调框架去追求 genuine 非 Lipschitz 几何时，才须重新独立验证

\[
\|a-b\|
\le L\|a+b\|^\gamma,
\qquad (a,b)=(u-u',v-v'),
\]

对单位步长的 \(F_{\mathrm{red}}\) 成立，并同时独立验证

\[
d(y,S_{\mathrm{red}})
\le K\,d(0,F_{\mathrm{red}}(y))^q,
\]

且重新核对 coverage、共同正半径与所有量词。若使用 \(F_{\mathrm{T5}}=F_{\mathrm{red}}/\lambda\)，则 RL 与 EB 两式都必须针对该缩放后的同一算子书写。

### 7.4 对 nonlinear T5 的真实边界

在 Xue–Zhang 的 restricted-monotone + full-domain 框架中，\(F_{\mathrm{red}}\) 最大单调；这使 \(J_{F_{\mathrm{red}}}\) firmly nonexpansive，其 reflected resolvent 是非扩张的。因而标准 reduced application 可取

\[
\gamma=1,\qquad L\le1,
\]

并且不会产生 genuine 非 Lipschitz 几何。它在有界小域上当然也可写成较弱的 \(\gamma<1\) Hölder 上界，但那不代表最佳指数小于 1。

所以：

- SO-07 可成为 T5 的一个重要 coverage verifier；
- 它可支持线性 RL + ordinary metric subregularity 的 reduced-PPA 收敛结论；
- 它本身不展示 T5 的 genuine nonlinear critical mechanism；
- 若要得到 genuinely nonlinear RL，必须额外改变/放宽算子几何，并重新证明 reduced map 的覆盖、RL 和 EB，不能从原最大单调结论自动推出。

另外，T5 在 reduced space 得到的是 reduced orbit 的点收敛。要恢复原空间整个轨道的点收敛，还需 Xue–Zhang 的 kernel-component single-valuedness/continuity 或其他 lift reconstruction；不能只凭 reduced convergence 宣称 full-space point convergence。

---

## 8. 剩余的真实研究前沿

剔除已知结果后，可信的剩余问题至少要求：

- 非 piecewise-polyhedral；
- 不依赖 global sri/ri CQ；
- 不由强单调、带增长模条件的一致单调、现成 coercivity 或 bounded-domain 路径直接推出；
- 条件可从 \(\mathcal A\) 与 \(\mathcal Q\) 的原生表示检查，而不是先求完整 projected inverse；
- 能处理核方向 escape 与 range 方向 load 的耦合；
- 最好覆盖多值 \(\mathcal A\)、非孤立零集或跨分支结构；
- 至少给出一个严格分离例子，证明新条件成功而上述已知条件失败。

可能的成功形态有两种，二者都可接受：

1. **正定理：** 一个广泛、自然、手算可核的 actual-coverage 原理；
2. **障碍定理：** 证明某一大类“只依赖局部/分支/渐近信息”的 verifier 不可能保证 actual coverage，并给出需要额外全局信息的最小形式。

后者若边界足够精确，同样具有理论价值；不应为了正结果而退回已知子类。

---

## 9. 价值审计与停止条件

### 9.1 若攻克，价值在哪里

一个真正成功的 SO-07 定理会：

1. 把大量文献中的“admissible preconditioner”从黑箱假设变成可验证条件；
2. 解释何时退化 splitting 的隐式子问题对所有状态确实可解；
3. 扩展 Xue–Zhang 的 restricted Minty characterization，使其从抽象等价变成原生 calculus；
4. 为 reduced Euclidean PPA（包括 T5）提供缺失的 coverage 模块；
5. 若覆盖自然非多面多值结构，可独立成为一项 monotone-operator / splitting 理论贡献。

### 9.2 什么结果不值得继续

出现以下任一情形，应降级或停止 M2：

- 只证明一个具体矩阵例子可解；
- 只重述 \(P_V\mathcal A^{-1}|_V\) 最大单调；
- 假设 \(\operatorname{ran}(\mathcal A+\mathcal Q)\) 闭而不给原生 verifier；
- 结果只是 sri/ri CQ、Bùi–Combettes Proposition 3.9、Boţ–Grad 的抽象 exactness/closedness 刻画或其现成充分推论、或 Li–Rockafellar–Sun 的直接改写；新的原生条件可以通过验证既有必要充分刻画来获得价值；
- 只处理 piecewise-linear/quadratic 或完整可枚举 polyhedral graph；
- 把 coverage 与 single-valuedness 混为一谈；
- 只在 \(\mathcal Q\)-半范数中给几何，却无 reduced Euclidean conversion；
- 把 \(\gamma=1\) 的最大单调 reduced map 宣称为 genuine nonlinear RL 应用。

### 9.3 当前评级

| 维度 | 评级 | 理由 |
|---|---|---|
| 公开问题真实性 | 高 | 最终接受稿明确 future work |
| 数学基础性 | 高 | 关系到 resolvent 是否存在、Minty maximality 与值域闭合 |
| 算法广泛性 | 高 | 退化 PPA 覆盖多种 splitting |
| 与 T5 coverage 的接口 | 高 | 正好补 T5 的独立 coverage 槽位 |
| 与 genuine nonlinear RL 的直接接口 | 中低 | 原始最大单调 reduced map 落在 \(\gamma=1\) |
| 形成大成果的潜力 | 中高但条件苛刻 | 必须越过多个成熟旧理论并覆盖自然非多面类 |

---

## 10. 主张—证据账本

| 主张 | 状态 | 证据 |
|---|---|---|
| 最大单调 \(\mathcal A\) 不保证退化 resolvent 全定义 | VERIFIED_SOURCE | Bredies et al. Remark 2.2；Xue–Zhang Example 2 |
| full domain 等价于 projected inverse 最大单调 | VERIFIED_SOURCE | Xue–Zhang Theorem 11 |
| global sri 条件充分但不必要 | VERIFIED_SOURCE | Corollary 13 与 Example 3 |
| 在 \(0\in\operatorname{ran}\mathcal A\) 下有 closure coverage | VERIFIED_SOURCE | Proposition 14 |
| closure 与 actual range 的关系被明确留作 future work | VERIFIED_SOURCE | Proposition 14 后正文 |
| finite-dimensional piecewise-polyhedral 子类已闭合 | PROVED_PROJECT_IMPORT | Li–Rockafellar–Sun Theorem 4.1(a) + Xue–Zhang Theorem 11 |
| 一般非多面 SO-07 截至 2026-09-08 仍未解决 | PENDING_GLOBAL_VERIFICATION | 定向检索未发现直接闭合；不能由未检索到推出全球不存在 |
| SO-07 自动产生 genuine nonlinear T5 应用 | FALSE | reduced maximal monotonicity给 \(\gamma=1\) reflected Lipschitz geometry |

---

## 11. 核验过的核心原始来源

1. [Xue–Zhang, arXiv v5 HTML](https://arxiv.org/html/2401.08431v5)；[arXiv record](https://arxiv.org/abs/2401.08431)；[JOTA version of record](https://link.springer.com/article/10.1007/s10957-025-02915-x)。
2. [Bredies–Chenchene–Lorenz–Naldi, Degenerate Preconditioned Proximal Point Algorithms](https://arxiv.org/pdf/2109.11481)，Definition 2.1、Remark 2.2、Theorems 2.13–2.14。
3. [Bùi–Combettes, Warped Proximal Iterations](https://pcombet.math.ncsu.edu/jmaa5.pdf)，Definition 1.1、Propositions 3.8–3.10。
4. [Boţ–Grad, Closedness-Type Regularity Conditions](https://arxiv.org/html/1007.3652v1)，Theorems 3、6 及相关 surjectivity 推论。
5. [Briceño-Arias–Roldán, Parallel Composition](https://arxiv.org/abs/2109.06771)。
6. [Li–Rockafellar–Sun, Maximal Monotonicity of Piecewise Polyhedral Mappings](https://arxiv.org/html/2607.07358v1)，Theorems 3.3 and 4.1。

检索日期为 2026-09-08。检索覆盖 arXiv、出版社官方页面及可访问作者全文；没有把摘要级信息升级为定理级结论，也没有把“未检索到”写成全球首创性证明。

---

## 12. 研究审计状态

```yaml
contract_version: "1.0"
expert_skill:
  - sci-skills-literature-search
  - sci-skills-paper-deep-reading
project_id: RL-PPA-VERIFY
paper_family: theoretical
stage_id: T2
task_id: SO-07-source-and-progress
task_status: COMPLETE_WITH_NOVELTY_GATE
inputs_reviewed:
  - RL_PPA_T5_core_manuscript_2026-09-07.md
  - OPEN_PROBLEMS_STRUCTURED_OPERATORS.md
  - Xue-Zhang arXiv:2401.08431v5 and JOTA record
  - Bredies-Chenchene-Lorenz-Naldi arXiv:2109.11481
  - Bui-Combettes warped-resolvent paper
  - Bot-Grad arXiv:1007.3652
  - Briceno-Arias-Roldan arXiv:2109.06771
  - Li-Rockafellar-Sun arXiv:2607.07358v1
outputs:
  - exact source and version crosswalk
  - author-stated open-problem reconstruction
  - theorem-level progress matrix
  - piecewise-polyhedral closure deduction
  - exact reduced-space T5 interface
  - novelty and stop gates
evidence_status:
  - VERIFIED_SOURCE: author-stated future work and cited theorem scopes
  - PROVED_PROJECT_IMPORT: finite-dimensional piecewise-polyhedral SO-07 subcase
  - PENDING_GLOBAL_VERIFICATION: no exhaustive proof that no other general solution exists
assumptions:
  - finite-dimensional priority for integration with current T5
  - coverage and single-valuedness are separate
  - Euclidean T5 is applied only after an exact reduced-space conversion
author_input_needed: []
manual_actions: []
quality_checks:
  - version numbering corrected to arXiv v5
  - closure inclusion distinguished from actual inclusion
  - abstract characterization distinguished from native verifier
  - polyhedral subclass removed from novelty space
  - semidefinite metric distinguished from Euclidean T5 metric
  - gamma=1 distinguished from genuine nonlinear RL
conflicts:
  - SO-07 is high-value as a coverage problem but not automatically a genuine nonlinear T5 application
conflict_resolution_status: RESOLVED_BY_SCOPE_SEPARATION
merge_permission: orchestrator_only
recommended_next_action: give this dossier, the T5 core manuscript, and M2_Codex_clearance_and_PRO_brief.md to PRO for the gated M2 attack
stage_acceptance_recommendation: ACCEPT
```
