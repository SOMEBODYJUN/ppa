# M2 / SO-07：数学背景与文献清场

日期：2026-09-08  
项目：RL–PPA–VERIFY  
主题：退化预条件 PPA 的真实值域覆盖

---

## 1. 问题本身

设 \(H\) 为实 Hilbert 空间，

\[
A:H\rightrightarrows H,
\qquad
Q:H\to H,
\]

其中 \(Q\) 有界、线性、自伴、半正定，

\[
V:=\operatorname{ran}Q
\]

闭，并且 \(\ker Q\ne\{0\}\)。退化预条件 resolvent 为

\[
T=(A+Q)^{-1}Q.
\]

对任意输入都存在一步输出，等价于

\[
\boxed{
V\subseteq\operatorname{ran}(A+Q).
}
\tag{M2.1}
\]

这是真实值域覆盖，而不是闭包覆盖

\[
V\subseteq\overline{\operatorname{ran}(A+Q)}.
\tag{M2.2}
\]

二者的差别是：式 (M2.2) 只保证方程可以被残差趋零的序列逼近；式 (M2.1) 才保证方程真正取得解。

M2/SO-07 研究的就是从关于 \(A,Q\) 的可检查信息推出式 (M2.1) 的问题。

---

## 2. 原始出处

直接出处是：

- Feng Xue, Hui Zhang, *On Degenerate Preconditioned Proximal Point Methods under Restricted Monotonicity*, Journal of Optimization Theory and Applications 208, article 74 (2026), DOI [10.1007/s10957-025-02915-x](https://link.springer.com/article/10.1007/s10957-025-02915-x); [arXiv:2401.08431v5](https://arxiv.org/html/2401.08431v5).

SO-07 是本项目内部编号，不是原论文的问题编号。

Xue–Zhang v5 中相关结果为：

| 原文位置 | 内容 |
|---|---|
| Assumption 1 | \(Q\) 有界、线性、自伴、半正定、退化且值域闭 |
| Definition 3 / Assumption 2 | 在 \(H\times\operatorname{ran}Q\) 上的 restricted monotonicity 与基本 viability |
| Lemma 10 | \(V=\operatorname{ran}Q\) 上的 restricted Minty theorem |
| Theorem 11 | full domain 与 projected inverse 最大单调的等价刻画 |
| Assumption 4 / Corollary 13 | 全局最大单调性加 strong-relative-interior 条件给出充分性 |
| Proposition 14 | 在相应假设及 \(0\in\operatorname{ran}A\) 下得到闭包覆盖 |
| Proposition 14 后正文 | 明确指出真实值域包含未必成立，并把闭包/真实值域及其与 sri 条件的联系留作 future work |
| Definition 16 / Theorem 18 | 完整 resolvent 的 single-valuedness 是另一个独立问题 |

作者明确留下的是闭包值域、真实值域与 sri 条件之间的关系。本项目所说的“从原生、可检查信息得到 actual coverage”是对这一方向的强化表述，不是原文逐字提出的命题。

退化预条件 PPA 的基础框架来自：

- K. Bredies, E. Chenchene, D. A. Lorenz, E. Naldi, *Degenerate Preconditioned Proximal Point Algorithms*, SIAM Journal on Optimization 32(3), 2376–2401 (2022), [arXiv:2109.11481](https://arxiv.org/abs/2109.11481).

该文 Definition 2.1 将 full domain 与 single-valuedness 纳入 admissible-preconditioner 条件；Remark 2.2 指出最大单调性本身不足以保证退化 resolvent 良定义。

---

## 3. 已有的抽象答案

令

\[
B_V:=P_VA^{-1}|_V:V\rightrightarrows V.
\]

在 Xue–Zhang 的 restricted-monotonicity 框架下，Theorem 11 给出

\[
\boxed{
\operatorname{dom}\big((A+Q)^{-1}Q\big)=H
\iff
B_V\text{ 在 }V\text{ 上最大单调}.
}
\tag{M2.3}
\]

因此，“full domain 是否存在抽象必要充分条件”已经解决。尚未由式 (M2.3) 自动解决的是：如何从 \(A,Q\) 的直接描述验证右侧，而无需事先知道完整 projected-inverse graph。

如果 \(A\) 全局最大单调，并且

\[
0\in\operatorname{sri}
\bigl(\operatorname{ran}Q-\operatorname{ran}A\bigr),
\tag{M2.4}
\]

则 Xue–Zhang Corollary 13 给出 full domain。其 Example 3 同时表明该 sri 条件不是必要条件。

在 \(A\) 全局最大单调、满足原文其他假设且 \(0\in\operatorname{ran}A\) 时，Proposition 14 只自动给出式 (M2.2)。原文的反例说明，闭包覆盖不能无条件升级为真实覆盖。

---

## 4. 已经覆盖的主要范围

### 4.1 Warped resolvent 条件

Bùi–Combettes 的 warped resolvent

\[
J_M^K=(K+M)^{-1}K
\]

包含当前形式。其 Proposition 3.8 把存在性与 injectivity 分开；Proposition 3.9 给出若干 range-inclusion 充分条件，包括：

- \(K+M\) 满射；
- \(K+M\) 最大单调且 \(D\cap\operatorname{dom}M\) 有界；
- \(K+M\) 最大单调，并且或者强单调，或者一致单调且其模满足 \(\phi(t)/t\to+\infty\)；
- \(K\) 最大单调，且 \(M=\partial\varphi\)，其中 \(\varphi:X\to\mathbb R\) 是有限值、下半连续、coercive convex 函数。

来源：M. N. Bùi, P. L. Combettes, *Warped Proximal Iterations for Monotone Inclusions*, JMAA 491 (2020), 124315, [全文](https://pcombet.math.ncsu.edu/jmaa5.pdf)。

### 4.2 Representative-function 条件

Boţ–Grad 用 Fitzpatrick/representative functions 给出了 maximal-monotone sums 的 pointwise range 必要充分刻画以及满射充分条件。相关位置包括 Theorems 3、6 及其推论。

来源：R. I. Boţ, S.-M. Grad, *Closedness Type Regularity Conditions for Surjectivity Results Involving the Sum of Two Maximal Monotone Operators*, [arXiv:1007.3652](https://arxiv.org/html/1007.3652v1)。

这些 necessary-and-sufficient exactness 条件是可被进一步验证的抽象接口。它们不能被描述成一个正确新定理必须“绕开”的范围；新的内容只能来自更直接的条件如何验证这些抽象性质，而不能只是重述它们。

### 4.3 Parallel composition

Reduced operator 是一个 parallel composition。该运算的 resolvent、最大单调性和 infimal postcomposition 已有独立理论：

- L. M. Briceño-Arias, F. Roldán, *Resolvent of the Parallel Composition and Proximity Operator of the Infimal Postcomposition*, Optimization Letters 17, 399–412 (2023), [arXiv:2109.06771](https://arxiv.org/abs/2109.06771).

因此，projected inverse 或 reduced operator 改写成 parallel-composition 记号，本身不形成新的 coverage 结果。

### 4.4 有限维 piecewise-polyhedral 子类

有限维最大单调 piecewise-polyhedral 子类已经闭合。

若 \(A\) 最大单调且 piecewise polyhedral，且

\[
V\cap\operatorname{ran}A\ne\varnothing,
\]

则 \(A^{-1}\) 仍为最大单调 piecewise-polyhedral。Li–Rockafellar–Sun Theorem 4.1(a) 推出

\[
P_VA^{-1}|_V
\]

在 \(V\) 上最大单调；再由 Xue–Zhang Theorem 11 得到 full domain。

来源：X. Li, R. T. Rockafellar, D. Sun, *Maximal Monotonicity of Piecewise Polyhedral Mappings*, [arXiv:2607.07358v1](https://arxiv.org/html/2607.07358v1)，Theorems 3.3、4.1。

同一子类也可通过闭值域论证处理：有限维 piecewise-polyhedral \(A\) 使 \(\operatorname{ran}(A+Q)\) 成为有限个多面体的并，因而闭。平移后结合 Xue–Zhang Proposition 14，即可把闭包覆盖升级为真实覆盖。

因此，PLQ subdifferential、polyhedral normal cones 和一般 piecewise-polyhedral maximal-monotone operators 不属于当前剩余空白。

---

## 5. Subdifferential 情形的等价翻译

若 \(A=\partial f\)，其中 \(f\) proper、闭、凸，则对每个 \(q\in V\)：

\[
q\in\operatorname{ran}(\partial f+Q)
\]

当且仅当函数

\[
x\longmapsto
f(x)+\frac12\langle x,Qx\rangle-\langle q,x\rangle
\tag{M2.5}
\]

取得最小值。

因此，这一情形的 actual coverage 等价于式 (M2.5) 对所有 \(q\in V\) 都 attainment。这里 \(Q\) 在 \(\ker Q\) 方向没有二次控制，故普通的强凸论证不能自动应用。

这是等价翻译，不是新的 coverage 定理。

---

## 6. 与 RL–PPA/T5 的精确接口

取某个 Hilbert 空间 \(H'\) 和有界满射

\[
C:H\to H',
\qquad Q=C^{\top}C.
\]

定义 reduced operator

\[
F_{\rm red}
:=C\triangleright A
=\bigl(CA^{-1}C^{\top}\bigr)^{-1}.
\]

Xue–Zhang §6 给出

\[
\widetilde T
=C(A+C^{\top}C)^{-1}C^{\top}
=J_{F_{\rm red}}.
\tag{M2.6}
\]

若 \(c^k=Cx^k\)，则

\[
c^{k+1}=\widetilde T c^k,
\qquad
c^k-c^{k+1}\in F_{\rm red}(c^{k+1}).
\tag{M2.7}
\]

此外，

\[
\operatorname{dom}\widetilde T=H'
\iff
\operatorname{dom}T=H,
\]

并且

\[
\|Cx\|=\|x\|_Q.
\]

因此，SO-07 的 coverage 结论可以严格转化为 reduced Euclidean PPA 的 coverage。

要使用当前有限维 T5，还需要 \(H'\) 有限维和

\[
\operatorname{zer}A\ne\varnothing.
\]

此时

\[
S_{\rm red}
=\operatorname{zer}F_{\rm red}
=C(\operatorname{zer}A).
\]

Coverage 本身不保证零集非空，也不保证原空间完整输出的唯一性。

在 Xue–Zhang 的 restricted-monotone + full-domain 框架中，\(F_{\rm red}\) 最大单调。因此单位步长的 reflected resolvent 非扩张，AP-RL 可取

\[
(\gamma,L)=(1,1).
\]

这不会产生 genuine 非 Lipschitz RL 几何。对 T5 的收敛应用仍需针对同一个 \(F_{\rm red}\) 验证 ordinary set-distance error bound、有效输出域和共同正半径。Reduced 轨道的点收敛也不自动推出原空间轨道的点收敛；核分量的恢复是另一个问题。

若将同一单位步长转移写成任意 T5 步长 \(\lambda>0\)，应取

\[
F_{\rm T5}=F_{\rm red}/\lambda,
\]

并同时转换 RL 与误差界数据。这只是归一化，不产生新的算法性质。

---

## 7. 截至本次核验的剩余边界

已有材料尚未给出一个覆盖一般非多面最大单调算子的、直接作用于 \(A,Q\) 描述的 actual-coverage 定理。

已经确认不能作为剩余空白的范围包括：

- Xue–Zhang Theorem 11 的 projected-inverse maximality 等价；
- global sri 条件；
- Bùi–Combettes Proposition 3.9 的现成条件；
- Boţ–Grad 的抽象 necessary-and-sufficient exactness 刻画及现成充分推论；
- 单纯的 parallel-composition 改写；
- 有限维 piecewise-polyhedral 最大单调类。

目前尚未由所核文献闭合的目标，可以保守表述为：

> 对非 piecewise-polyhedral 的 \(A\)，在不直接假定 global sri、range closedness、actual coverage 或 projected-inverse maximality 的前提下，是否存在由 \(A,Q\) 的直接结构可验证的充分条件，保证
> \[
> \operatorname{ran}Q\subseteq\operatorname{ran}(A+Q),
> \]
> 并覆盖现有强单调、带增长模的一致单调、bounded-domain 和特定 coercive-convex 条件不能直接处理的自然多值类？

这是截至 2026-09-08 的项目强化问题。定向检索未发现其一般解，但这不是“全球不存在已有解”的证明。

---

## 8. 证据状态

| 主张 | 状态 |
|---|---|
| Xue–Zhang 明确留下闭包/真实值域关系的 future-work 方向 | VERIFIED_SOURCE |
| Full domain 与 projected-inverse maximality 等价 | VERIFIED_SOURCE |
| Global sri 是充分但非必要条件 | VERIFIED_SOURCE |
| Closure coverage 不自动推出 actual coverage | VERIFIED_SOURCE |
| 有限维 piecewise-polyhedral 子类已经闭合 | PROVED_PROJECT_IMPORT / ALREADY COVERED |
| 一般非多面强化问题尚无现成解 | PENDING_GLOBAL_VERIFICATION |
| SO-07 自动提供 genuine nonlinear RL | FALSE |

本文件只记录问题、来源、已有覆盖范围和与 T5 的数学接口；不包含研究流程、证明建议或面向任何模型的任务指令。
