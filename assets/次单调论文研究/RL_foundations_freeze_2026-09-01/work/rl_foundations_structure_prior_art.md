# RL foundations：structure theorem 的窄而深 primary-source 先例审计

> **project_id**: `monotonicity-regularity-seesaw-2026-09`  
> **paper_family / stage / task**: `T / RL-FND-PRIOR / RL-FND-PRIOR-05`  
> **expert_skill**: `sci-skills-literature-search`  
> **contract_version**: `1.0`  
> **检索日**: 2026-09-01  
> **范围**: higher-order metric subregularity、PPA 的高阶收敛、reflected-resolvent 渐近、非孤立解集上的 moving anchors / solution drift / alignment，以及 graphical derivative / coderivative 刻画。  
> **方法边界**: 只用出版社/期刊官网、作者或机构公开稿、arXiv 等 primary/official sources；未调用第三方 API。平台不提供稳定的数据库命中总数、主题词树和完整引文网络。因此本文是**有边界、可复核的 primary-source audit**，不是系统综述；任何“未命中”均不得升级为新颖性证明。

配套决策表见 [`rl_foundations_structure_claim_safe_matrix.md`](rl_foundations_structure_claim_safe_matrix.md)。

## 0. 执行结论

### 0.1 会改变论文定位的命中

**Zhu 1995 是必须正面处理的最强先例。** 在有限维、maximal-monotone、精确 PPA 语境中，Zhu 允许非单点解集，以 \(T^{-1}\) 的 \(r>1\) growth condition 推出实际迭代点趋于其极限的高阶 Q-superlinear convergence；其正式“order \(r\)”定义给出每个 \(1<t<r\) 的超线性结论，而不是端点

\[
\|z_{k+1}-\bar z\|=O(\|z_k-\bar z\|^r).
\]

同文 Lemma 4.1 还证明了轨道误差方向相对于解集切锥的渐近法向对齐。故以下广义新颖性说法已经不安全：

- “首次在非孤立解集上得到 PPA 高阶超线性”；
- “首次发现非孤立 PPA 的切向/法向对齐机制”；
- “higher-order subregularity 首次导致 actual-iterate superlinear convergence”。

### 0.2 当前 structure theorem 仍可保留的窄贡献面

经现有全文核验，当前结果最可能保留的区别不是“高阶 PPA”本身，而是以下定量结构的组合：

1. **branchwise endpoint equivalence**：在局部孤立零点和已有 Minty branch 下，把
   \[
   \|y-p\|=O(\|w\|^Q),\quad
   \|J_{\lambda F}x-p\|=O(\|x-p\|^Q),\quad
   R_{\lambda F}x=2p-x+O(\|x-p\|^Q)
   \]
   写成精确等价链；
2. **stepwise two-anchor geometry**：明确区分 \(p_y\in P_S(Jx)\)、\(p_x\in P_S(x)\)、固定 \(\bar p\) 与 arbitrary graph pair；
3. **quantified alignment composition**：若
   \[
   \|x-p_y\|=O(d(x,S)^\theta),
   \]
   则
   \[
   d(Jx,S)=O(d(x,S)^{\theta Q});
   \]
4. **moving-center reflected asymptotic**：在 output-nearest anchor 上得到
   \[
   R_{\lambda F}x-p_y=-(x-p_y)+O(\|x-p_y\|^Q).
   \]

但这四点中，(1) 和 (4) 的核心等式都接近 Minty/Cayley 坐标下的一步代数推论；(3) 若只停留在“两个指数相乘”，也不足以单独支撑重大新颖性。真正可发表的增量需要来自：**更宽的非单调/restricted-branch 适用域、可验证的 alignment 条件、端点 sharpness，以及把这三层几何完整分类**。

### 0.3 尚不能锁死的两个关键风险

- **Wang–Li–Ng 2023**：官方摘要已核验，但全文未公开取得；其 exact-PPA rate theorem 是否覆盖 \(Q>1\)、endpoint order、actual iterate 或非孤立集合，均为 **PENDING_FULL_TEXT**。
- **Moursi–Vanderwerff 2025**：官方摘要与关键词已核验，全文未公开取得；其 pointwise/at-each-point monotonicity 与 reflection-operator 结果是否含局部中心化 reflection 渐近，均为 **PENDING_FULL_TEXT**。

在这两篇全文核验前，不能使用 “first”, “novel”, “previously unknown” 等排他性表述。

---

## 1. 统一记号与指数翻译

令

\[
S:=F^{-1}(0),\qquad
J_{\lambda F}:=(I+\lambda F)^{-1},\qquad
R_{\lambda F}:=2J_{\lambda F}-I.
\]

对 \((y,w)\in\operatorname{gph}F\)，置

\[
x:=y+\lambda w,\qquad y=J_{\lambda F}x.
\]

本项目的 higher-order error bound 写作

\[
\tag{P-QEB}
d(y,S)\le \kappa\,d(0,F(y))^Q,
\qquad Q>1.
\]

以下指数 convention 必须显式区分：

| 来源 | 原文 convention | 与本项目 \(Q\) 的关系 |
|---|---|---|
| Li–Mordukhovich 2012 | \(d(x,S)\le c\,d(\bar y,F(x))^q\), \(0<q\le1\) | 同向 residual exponent；原文主范围不含 \(Q>1\) |
| Mordukhovich–Ouyang 2015 | 同向 \(q\)-metric/strong \(q\)-subregularity，允许任意 \(q>0\)，重点 \(q>1\) | \(q=Q\) |
| Zhu 1995 | inverse growth：\(z\in T^{-1}(w)\) 时 \(d(z,S)\lesssim\lVert w\rVert^r\) | 局部 gauge 与 (P-QEB) 同型，\(r=Q\)，常数参数化不同 |
| Hölder graphical derivative 文献 | 常写 \(\tau\lVert x-\bar x\rVert^q\le d(\bar y,F(x))\) | 其 \(q=1/Q\)；不能把同名字母直接代入 |

本文后续始终用大写 \(Q>1\) 表示项目中的 residual exponent。

---

## 2. higher-order metric subregularity：概念已知，PPA 专门结论需另分

### 2.1 Mordukhovich–Ouyang 2015

Mordukhovich–Ouyang, *Higher-order metric subregularity and its applications*, J. Global Optim. 63 (2015), 777–795, DOI [10.1007/s10898-015-0271-x](https://doi.org/10.1007/s10898-015-0271-x)；[作者公开全文](https://optimization-online.org/wp-content/uploads/2014/07/4440.pdf)。**VERIFIED_PRIMARY_FULL_TEXT**。

原文 Definition 3.1 定义任意 \(q>0\) 的 metric \(q\)-subregularity 与 strong metric \(q\)-subregularity，并明确聚焦 \(q>1\)。因此：

> “\(Q>1\) higher-order/strong metric subregularity 的概念”不是新概念。

其 Theorem 3.4 给出 subdifferential 情形与高阶增长不等式的刻画；Sections 4–5 处理 perturbation 与 Newton/quasi-Newton。Theorem 5.1 在 strong \(q\)-subregularity 和 Dennis–Moré 型近似条件下给出

\[
\frac{\|x_{k+1}-\bar x\|}{\|x_k-\bar x\|^q}\longrightarrow0.
\]

但这不是固定步长 PPA 的直接定理：其 Newton/quasi-Newton 假设不能仅由固定 proximal regularization 自动获得。故该文同时带来两条边界：

- **已知**：higher-order strong subregularity 可驱动 \(q\)-order Newton-type convergence；
- **未由该文直接覆盖**：固定步长 PPA 的 branchwise endpoint \(O(e_k^Q)\) 与 reflected-resolvent remainder。

### 2.2 Li–Mordukhovich 2012

Li–Mordukhovich, *Hölder Metric Subregularity with Applications to Proximal Point Method*, SIAM J. Optim. 22(4) (2012), 1655–1684, DOI [10.1137/120864660](https://doi.org/10.1137/120864660)；[作者公开全文](https://optimization-online.org/wp-content/uploads/2012/02/3340.pdf)。**VERIFIED_PRIMARY_FULL_TEXT**。

原文 PPA 部分使用 \(0<q\le1\) 的 Hölder metric subregularity，并允许一般非单点解集。其 Theorem 7.2 的核心集合距离递推可写成

\[
d(x_{k+1},S)^2
\le d(x_k,S)^2
-c^{-2/q}\lambda_k^2d(x_{k+1},S)^{2/q}.
\]

Theorem 7.3 在固定步长下给出 \(q<1\) 的 polynomial/sublinear distance rate；\(q=1\) 给出 linear rate，而 \(q=1\) 配合 \(\lambda_k\to\infty\) 给出 superlinear rate。它不直接覆盖本项目 \(Q>1\) 的固定步长 endpoint order，也不含 reflected-resolvent asymptotic。

因此它是“metric subregularity + PPA rate”的必要背景，但不是当前 \(Q>1\) 结构式的直接先例。

### 2.3 Wang–Li–Ng 2023

Wang–Li–Ng, *Convergence Rate of Inexact Proximal Point Algorithms for Operator with Hölder Metric Subregularity*, SIAM J. Optim. 33(3) (2023), 1996–2020, DOI [10.1137/22M152147X](https://doi.org/10.1137/22M152147X)。**VERIFIED_OFFICIAL_ABSTRACT / PENDING_FULL_TEXT**。

官方摘要可确认：

- 对象是 Hilbert 空间中的 maximal monotone operator；
- 研究 inexact PPA 的 global/local strong convergence 与 quantitative rates；
- exact PPA 结果改进 Li–Mordukhovich 2012。

本轮无法从公开 primary source 核验以下决定性细节：

1. Hölder exponent 是否严格限制在 \(0<q\le1\)；
2. exact-PPA theorem 是否给 actual iterate 或只给 set distance；
3. 是否有 endpoint \(O(e_k^Q)\)、非孤立 solution set 的高阶结果或 reflection statement。

以上全部标为 **PENDING_FULL_TEXT**，不能由题目、摘要或参考文献列表推断。

---

## 3. PPA 的高阶收敛：Zhu 1995 是主要重叠源

### 3.1 Zhu 的正式结果

C. Zhu, *Asymptotic Convergence Analysis of the Forward-Backward Splitting Algorithm*, Mathematics of Operations Research 20(2) (1995), 449–464, DOI [10.1287/moor.20.2.449](https://doi.org/10.1287/moor.20.2.449)；[Argonne primary prepublication P457](https://ftp.mcs.anl.gov/pub/tech_reports/reports/P457.pdf)。**VERIFIED_PRIMARY_FULL_TEXT**。

Zhu 的框架包含 exact PPA 特例

\[
z_{k+1}=(I+c_kT)^{-1}z_k,
\qquad T\text{ maximal monotone},
\]

解集 \(S=T^{-1}(0)\) 不要求为单点。其 inverse growth condition 在局部具有

\[
z\in T^{-1}(w)
\quad\Longrightarrow\quad
d(z,S)\lesssim\|w\|^r
\]

的形式。对 \(r>1\) 和 \(\liminf c_k>0\)，Theorem 4.3 证明实际迭代点 \(z_k\to\bar z\in S\) 具有其定义下的 Q-superlinear order \(r\)：对每个

\[
1<t<r,
\]

有

\[
\limsup_{k\to\infty}
\frac{\|z_{k+1}-\bar z\|}{\|z_k-\bar z\|^t}=0.
\]

这是 **actual-iterate** 结论，不只是 \(d(z_k,S)\) 的结论；Zhu 也明确把它与 Luque 的 set-distance 分析区分。

### 3.2 Zhu 的 alignment lemma

Zhu Lemma 4.1 令

\[
d\bigl(T_S(\bar z),z_k-\bar z\bigr)
=\alpha_k\|z_k-\bar z\|,
\]

并证明 \(\alpha_k\to1\)。这意味着轨道误差的 tangent component 渐近消失，归一化误差方向趋于 solution set 的 normal geometry。它是**沿 PPA 轨道、相对于最终极限点、无定量幂率**的 alignment statement。

因此 Zhu 已覆盖“非孤立 + actual iterate + 高阶超线性 + 渐近法向对齐”的宽主题。

### 3.3 Zhu 没有直接给出的端点与结构

经全文核验，Zhu 的正式 order-\(r\) 结论没有声明

\[
\|z_{k+1}-\bar z\|=O(\|z_k-\bar z\|^r),
\]

也没有给出：

- \(R_{\lambda F}x=2p-x+O(\lVert x-p\rVert^r)\)；
- input-nearest / output-nearest 两个移动锚点的逐步分离；
- 一个显式 alignment exponent \(\theta\) 及端点 \(\theta r\) law；
- nonmonotone/restricted Minty branch 的结构等价。

不过，**这不等于 isolated endpoint \(O(e^r)\) 自动具有强新颖性**。当 \(S=\{p\}\) 时，Zhu 的同型 inverse growth 与 PPA residual

\[
w_{k+1}=\frac{z_k-z_{k+1}}{c_k}
\]

已使 endpoint upper bound 成为非常直接的局部推论。故在未找到逐字同名定理时，仍不应把 isolated direct \(Q\)-order 宣传成独立重大突破；更稳妥的价值在 branchwise equivalence、非单调适用域与 reflection/two-anchor packaging。

### 3.4 Luque 1984：需要全文完成历史链

R. Luque, *Asymptotic Convergence Analysis of the Proximal Point Algorithm*, SIAM J. Control Optim. 22 (1984), 277–293, DOI [10.1137/0322019](https://doi.org/10.1137/0322019)。**VERIFIED_OFFICIAL_ABSTRACT / PENDING_FULL_TEXT**。

官方摘要确认其研究 maximal monotone PPA，并把收敛率与 \(T^{-1}\) 在原点附近离解集的 growth 联系起来。Zhu 对该文的比较表明 Luque 的主要 rate 对象是 set distance；但在未直接读取 Luque theorem blocks 前，不应对其 endpoint exponent 作二手式断言。

---

## 4. reflected-resolvent asymptotic：精确公式未命中，但不宜单独拔高

### 4.1 当前公式本身是精确 Cayley 恒等式的推论

若 \(p\in S\) 且 \(y=J_{\lambda F}x\)，则

\[
R_{\lambda F}x-(2p-x)=2(y-p).
\]

因此

\[
\|J_{\lambda F}x-p\|=O(\|x-p\|^Q)
\]

与

\[
R_{\lambda F}x=2p-x+O(\|x-p\|^Q)
\]

是常数差 \(2\) 的精确等价。这个 observation 很清楚，也很适合作为 structure theorem 的一环；但它的证明复杂度决定了不宜单独称为主要新定理。

### 4.2 最接近的已知 reflection 理论

Liu–Moursi–Vanderwerff, *Strongly Nonexpansive Mappings Revisited: Uniform Monotonicity and Operator Splitting*, SIAM J. Optim. 33 (2023), 2570–2597；[arXiv:2205.09040 全文](https://arxiv.org/pdf/2205.09040)。**VERIFIED_PRIMARY_FULL_TEXT**。

其 Lemma 3.4 对 uniformly monotone \(A\) 给出全 pair defect inequality

\[
\|x-y\|^2-\|R_Ax-R_Ay\|^2
\ge4\phi(\|J_Ax-J_Ay\|),
\]

Proposition 3.5 将 uniform monotonicity 与 \(-R_A\) 的 super strong nonexpansiveness 联系起来。该结果是全局/all-pairs defect theory，不是 moving-center 的高阶 Taylor-type remainder。

Adly–Rockafellar, *Sensitivity analysis of maximally monotone inclusions via the proto-differentiability of the resolvent operator*, Math. Program. 189 (2021), 37–54, DOI [10.1007/s10107-020-01515-z](https://doi.org/10.1007/s10107-020-01515-z)；[作者公开全文](https://sites.math.washington.edu/~rtr/papers/rtr253-Resolvent.pdf)。**VERIFIED_PRIMARY_FULL_TEXT**。

该文给出 resolvent 的一阶 proto-derivative 公式，是“resolvent derivative / sensitivity”的直接先例。它没有给出上述 \(Q>1\) remainder，但提示安全表述应是“higher-order branchwise Cayley reformulation”，而不能暗示 resolvent 局部导数研究此前不存在。

### 4.3 Moursi–Vanderwerff 2025 风险

Moursi–Vanderwerff, *On Further Notions of Strong Nonexpansiveness and Corresponding Notions of Monotonicity*, JOTA 205 (2025), article 50, DOI [10.1007/s10957-025-02633-4](https://doi.org/10.1007/s10957-025-02633-4)。**VERIFIED_OFFICIAL_ABSTRACT / PENDING_FULL_TEXT**。

官方摘要确认其研究 uniformly monotone on bounded sets / at each point 及对应 nonexpansive-map notions；官方关键词含 “Reflection operator”。公开摘要不足以判定其是否含 pointwise centered remainder、isolated zero 或 moving anchor 结果。本轮 exact-title、DOI、作者域名和公开预印本检索均未取得正文；这只是访问边界，不是 absence proof。

### 4.4 本轮 negative boundary

本轮对以下 formula/alias 作 exact search：

\[
R(x)=2p-x+O(\|x-p\|^Q),\qquad
R(x)-p=-(x-p)+O(\|x-p\|^Q),
\]

以及 “reflected resolvent derivative \(-I\)”, “higher-order resolvent flatness”, “proto-derivative of reflected resolvent”。在可访问 primary sources 中没有检到直接同式定理。状态仅为：

> **NEGATIVE_BOUNDARY_NOT_NOVELTY_PROOF**。

---

## 5. moving projections、solution drift 与 alignment

### 5.1 当前定理与 Zhu 的正确区分

当前 theorem 的基本对象是单步 graph pair：

\[
(y,w)\in\operatorname{gph}F,
\quad x=y+\lambda w,
\quad p_y\in P_S(y),
\quad p_x\in P_S(x).
\]

由 output-centered error bound 可得

\[
d(y,S)\le C\|x-p_y\|^Q.
\]

若另有 quantitative alignment

\[
\|x-p_y\|\le K\,d(x,S)^\theta,
\]

则

\[
d(J_{\lambda F}x,S)=O(d(x,S)^{\theta Q}).
\]

与 Zhu Lemma 4.1 的区别是：

| 维度 | Zhu 1995 | 当前 structure theorem |
|---|---|---|
| 对象 | 已生成的 PPA orbit | 任意局部合法 Minty graph pair / 一步映射 |
| anchor | 最终极限点 \(\bar z\) 与其 tangent cone | \(p_y\)、\(p_x\)、固定点和 arbitrary pair 分层 |
| alignment | 渐近方向，\(\alpha_k\to1\) | 假设或待验证的定量幂率 \(\theta\) |
| rate endpoint | 任意 \(t<r\) | 条件式 endpoint \(\theta Q\) upper law |
| operator scope | finite-dimensional maximal monotone | 可面向 restricted/nonmonotone branch，但需完整 existence/localization 假设 |

因此可以说当前结果**细化了所需的一步几何量**，但不能说首次发现非孤立对齐。

### 5.2 当前最可能成立的贡献边界

若要形成有分量的 theorem，而不是一个条件相乘式，至少要完成以下一项：

1. 从可核验的 operator geometry 推出具体 \(\theta\)，而非把 alignment 当黑箱；
2. 给出 \(\theta Q\) 的 matching lower example / sharpness；
3. 证明 \(p_y\)、\(p_x\) 与 fixed anchor 的不可交换性，并给出完整分类；
4. 在 Zhu 不覆盖的 restricted/nonmonotone branch 下保证 theorem 的存在性、局部不变性与 selection quantifier。

“若 \(A=O(r^\theta)\) 且 \(B=O(A^Q)\)，则 \(B=O(r^{\theta Q})\)”本身不是足够的新颖性单位。

### 5.3 本轮 negative boundary

对 “moving projection”, “output-nearest solution”, “input-nearest solution”, “solution drift”, “tangential drift”, “Fejér direction”, “PPA normal alignment” 等异名做公式级搜索，除 Zhu 的轨道 alignment 外，没有检到与

\[
\|x-P_S(Jx)\|=O(d(x,S)^\theta)
\]

同型的 stepwise theorem。状态仍仅为 **NEGATIVE_BOUNDARY_NOT_NOVELTY_PROOF**；Moursi–Vanderwerff 2025 和 Wang–Li–Ng 2023 全文未清除前尤其不能作排他声明。

---

## 6. graphical derivative / coderivative：刻画工具已存在，必须做 exponent inversion

### 6.1 ordinary strong metric subregularity

Cibulka–Dontchev–Kruger, *Strong Metric Subregularity of Mappings in Variational Analysis and Optimization*, [arXiv:1701.02078 全文](https://arxiv.org/pdf/1701.02078)。**VERIFIED_PRIMARY_FULL_TEXT**。

在适当有限维假设下，ordinary strong metric subregularity 可由 graphical derivative 的零核刻画：

\[
DF(\bar x\mid\bar y)^{-1}(0)=\{0\}.
\]

其 Fréchet coderivative theorem 一般给 modulus bound；只有附加局部凸 graph 条件时才可提升为等号式刻画。因此不能把一般 nonconvex multifunction 的 coderivative sufficient bound 写成无条件 iff。

### 6.2 higher-order / Hölder graphical derivatives

*Isolated calmness and sharp minima via Hölder graphical derivatives*, [arXiv:2106.08149 全文](https://arxiv.org/pdf/2106.08149)。**VERIFIED_PRIMARY_FULL_TEXT**。

该文使用 \(q\)-order graphical derivative，对 graph sequence 采用

\[
(\bar x+t_kx_k,\;\bar y+t_k^q y_k)\in\operatorname{gph}F
\]

的 scaling，并把 strong \(q\)-subregularity 写成

\[
\tau\|x-\bar x\|^q\le d(\bar y,F(x)).
\]

因此本项目

\[
\|x-\bar x\|\le \kappa\,d(\bar y,F(x))^Q
\]

对应其 derivative order

\[
q=1/Q,
\]

而不是 \(q=Q\)。该文给出从 strong Hölder subregularity 到 derivative positivity/kernel condition 的一般蕴含，并在有限维设置下给 iff / modulus 关系。它直接表明：

- isolated/strong \(Q\)-subregularity 的 graphical-derivative characterization 不能作为本项目的新概念；
- 任何写入 RL foundations 的 derivative criterion 必须注明 finite-dimensionality、strong/isolated quantifier 和 exponent inversion；
- ordinary nonisolated metric subregularity不能被一个孤立点零核判据偷换。

### 6.3 与 resolvent derivative 的接口

Adly–Rockafellar 的 proto-differentiability formula 可作为一阶接口：若局部 resolvent derivative 为零，则 reflected resolvent 的一阶 linearization 是 \(-I\)。但从一阶导数为零到

\[
R(x)=2p-x+O(\|x-p\|^Q)
\]

还需要明确的 \(Q\)-order remainder；不能只凭 proto-differentiability 推出。故建议把 derivative/coderivative 内容放在“可验证条件/后续 calculus”，不要把它当 structure theorem 的证明替代品。

---

## 7. claim-safe 判定

### 7.1 可直接写入文稿的定位句

以下表述在当前证据下相对安全：

> Higher-order metric subregularity and high-order convergence of proximal-type methods are established themes. In particular, Zhu obtained nonisolated actual-iterate superlinear convergence under an inverse growth condition for finite-dimensional maximal monotone PPA. Our result isolates a different one-step structure: a branchwise equivalence between higher-order resolvent flatness and reflected-resolvent asymptotic reflection, together with a two-anchor decomposition that identifies a quantitative solution-alignment exponent as the missing factor in the nonisolated case.

仍需把 “a different” 保持为结构区别，不能在 Wang 2023 与 Moursi–Vanderwerff 2025 全文核验前改成 “the first”。

### 7.2 不应出现的表述

- “We are the first to prove superlinear PPA convergence for a nonisolated solution set.”
- “Higher-order metric subregularity has not previously been connected to PPA.”
- “No prior work studies tangent/normal alignment of PPA iterates.”
- “The asymptotic reflection formula is entirely new.”
- “Graphical derivative/coderivative characterizations of higher-order subregularity are new.”
- “No exact-title/formula hit proves novelty.”

### 7.3 对投稿价值的冷静判断

单独的 isolated-zero endpoint bound 或 reflection identity 很可能过于直接；单独的 \(\theta Q\) composition 也偏薄。若完成以下 theorem package，SIAM/JOTA/MOR 级理论稿才更有说服力：

1. 正确且宽于 maximal-monotone PPA 的 branch/existence framework；
2. moving-anchor / fixed-anchor / all-pairs 三层必要性与严格分离；
3. 可验证的 alignment criterion，而非外加黑箱假设；
4. endpoint \(Q\) 或 \(\theta Q\) 的 sharp examples；
5. 与 Zhu 1995、Wang 2023、Moursi–Vanderwerff 2025 的 theorem-by-theorem 区分。

这是 **AI_INFERENCE**，不是期刊录用预测。

---

## 8. Primary-source ledger 与访问深度

| ID | primary / official source | 实际访问深度 | 支持范围 | 状态 |
|---|---|---|---|---|
| S1 | Li–Mordukhovich 2012, DOI 10.1137/120864660 | 作者公开全文 + 官方元数据 | \(0<q\le1\) HMSR 与 PPA set-distance rates | VERIFIED_PRIMARY_FULL_TEXT |
| S2 | Mordukhovich–Ouyang 2015, DOI 10.1007/s10898-015-0271-x | 作者公开全文 + official DOI | 任意 \(q>0\) higher-order MSR，Newton-type order | VERIFIED_PRIMARY_FULL_TEXT |
| S3 | Wang–Li–Ng 2023, DOI 10.1137/22M152147X | 官方摘要/元数据 | inexact/exact PPA scope only | PENDING_FULL_TEXT |
| S4 | Zhu 1995, DOI 10.1287/moor.20.2.449 | Argonne primary prepublication + official metadata | nonisolated actual-iterate superlinear order；alignment | VERIFIED_PRIMARY_FULL_TEXT |
| S5 | Luque 1984, DOI 10.1137/0322019 | 官方摘要/元数据 | inverse growth + PPA historical scope | PENDING_FULL_TEXT |
| S6 | Liu–Moursi–Vanderwerff 2023, arXiv:2205.09040 | arXiv 全文 + journal metadata | uniform monotonicity / reflected defect | VERIFIED_PRIMARY_FULL_TEXT |
| S7 | Moursi–Vanderwerff 2025, DOI 10.1007/s10957-025-02633-4 | 官方摘要/关键词 | at-each-point strong nonexpansiveness / reflection risk | PENDING_FULL_TEXT |
| S8 | Adly–Rockafellar 2021, DOI 10.1007/s10107-020-01515-z | 作者公开全文 | resolvent proto-derivative | VERIFIED_PRIMARY_FULL_TEXT |
| S9 | Cibulka–Dontchev–Kruger, arXiv:1701.02078 | arXiv 全文 | ordinary strong MSR graphical/coderivative criteria | VERIFIED_PRIMARY_FULL_TEXT |
| S10 | *Isolated calmness and sharp minima via Hölder graphical derivatives*, arXiv:2106.08149 | arXiv 全文 | Hölder graphical derivative criteria | VERIFIED_PRIMARY_FULL_TEXT |
| S11 | Aragón Artacho–Dontchev–Geoffroy 2007, ESAIM Proc. 17 | official journal PDF | metrically regular PPA adjacency | VERIFIED_PRIMARY_FULL_TEXT |

---

## 9. 检索式日志（去重；引号逐字保留）

以下检索均在 2026-09-01 执行。平台不暴露可复现的稳定总命中数，故不记录伪精确 hit count。检索结果只在 primary/official source 上形成证据。

### 9.1 higher-order subregularity + PPA

1. `"higher-order metric subregularity" "proximal point"`
2. `"higher order metric subregularity" "proximal point method"`
3. `"strong q-subregularity" "proximal point algorithm"`
4. `"q-subregularity" resolvent "q-order"`
5. `"metric subregularity of order q" "proximal point"`
6. `"power metric subregularity" "proximal point"`
7. `"higher-order metric subregularity" "fixed-step proximal point"`
8. `"Hölder metric subregularity" "proximal point" superlinear`
9. `"higher-order metric subregularity" resolvent convergence`
10. `site:optimization-online.org "higher-order metric subregularity"`
11. `"Hölder Metric Subregularity with Applications to Proximal Point Method" pdf`
12. `"Higher-order metric subregularity and its applications" pdf`

### 9.2 Wang–Li–Ng / Luque / Zhu

13. `"Convergence Rate of Inexact Proximal Point Algorithms for Operator with Hölder Metric Subregularity" pdf`
14. `"10.1137/22M152147X" pdf`
15. `site:epubs.siam.org/doi/10.1137/22M152147X`
16. `site:arxiv.org "Convergence Rate of Inexact Proximal Point Algorithms"`
17. `site:edu "22M152147X"`
18. `"Asymptotic Convergence Analysis of the Proximal Point Algorithm" Luque pdf`
19. `"10.1137/0322019" proximal point`
20. `"non-singleton solution set" "proximal point" superlinear`
21. `"proximal point" "Q-superlinear" nonunique solution`
22. `"growth condition" "proximal point" "order r"`
23. `"Asymptotic Convergence Analysis of the Forward-Backward Splitting Algorithm" pdf`
24. `site:ftp.mcs.anl.gov/pub/tech_reports/reports/P457.pdf Zhu`

### 9.3 reflected-resolvent asymptotic / aliases

25. `"reflected resolvent" "2p-x" asymptotic`
26. `"reflected resolvent" "O(||x-p||"`
27. `"resolvent" "J_A(x)-p" "higher order"`
28. `"derivative of the resolvent" isolated zero reflected resolvent`
29. `"reflected resolvent" derivative "-I" monotone`
30. `"R_A" "-Id" "proto-derivative"`
31. `"asymptotic reflection" resolvent monotone operator`
32. `"higher-order flatness" resolvent operator`
33. `"proto-differentiability" "reflected resolvent"`
34. `"uniform monotonicity" "reflection operator" at each point`
35. `"Strongly Nonexpansive Mappings Revisited" reflection pdf`
36. `"On Further Notions of Strong Nonexpansiveness and Corresponding Notions of Monotonicity" pdf`
37. `"10.1007/s10957-025-02633-4" pdf`
38. `site:arxiv.org "On Further Notions of Strong Nonexpansiveness"`

### 9.4 moving projection / drift / alignment aliases

39. `"proximal point" "tangent cone" "normal cone" convergence direction`
40. `"proximal point algorithm" "asymptotically normal" solution set`
41. `"dist(T_S" "proximal point"`
42. `"proximal point" "direction of convergence" solution set`
43. `"tangent cone" "z_k-z" "proximal point"`
44. `"growth condition" "tangent cone" "proximal point"`
45. `"Fejér monotone" "tangent cone" convergence direction`
46. `"Fejer monotone sequence" "normal cone" limit direction`
47. `"asymptotic direction" Fejér monotone convex set`
48. `"projection" "proximal point" tangential drift solution set`
49. `"moving projection" "proximal point algorithm"`
50. `"output-nearest" solution "proximal point"`
51. `"solution drift" resolvent projection`
52. `"P_S(Jx)" proximal point`

### 9.5 graphical derivative / coderivative aliases

53. `"strong metric subregularity" "graphical derivative" kernel`
54. `"higher-order metric subregularity" "graphical derivative"`
55. `"q-order graphical derivative" "strong metric subregularity"`
56. `"Hölder graphical derivative" isolated calmness`
57. `"coderivative" "higher-order metric subregularity"`
58. `"strong Hölder metric subregularity" coderivative`
59. `"proto-differentiability" resolvent operator derivative`
60. `"Sensitivity analysis of maximally monotone inclusions" resolvent pdf`

---

## 10. Negative boundaries 与未解决问题

| negative boundary | 本轮可说什么 | 本轮不能说什么 |
|---|---|---|
| 未命中 exact reflection remainder | 可访问 primary corpus 中未检到同式 theorem | 文献中不存在；因此一定新 |
| 未命中 stepwise \(p_y/p_x\) alignment exponent | Zhu 只有 orbit-level asymptotic alignment，未见同型幂率 | moving-anchor theory 首次出现 |
| 未命中 isolated endpoint PPA 的逐字定理 | 现有正式 statement 未见完全同形；但可从同型 EB 一步推得 | isolated direct order 是重大首创 |
| Wang 2023 无全文 | 摘要确认相关 PPA-rate scope | 指数范围、endpoint、非孤立量词 |
| Moursi–Vanderwerff 2025 无全文 | 摘要确认 pointwise notions，关键词含 reflection | 与当前 centered/moving reflection 无重叠 |
| Luque 1984 无全文 | 官方摘要确认 inverse growth 与 PPA rate | 具体 theorem exponent 与 actual-iterate 边界 |
| derivative 文献多为 isolated/strong | 可用作 isolated branch 的验证工具 | 直接刻画 ordinary nonisolated MSR |

---

## 11. 人工获取全文的最小操作说明

本轮不使用第三方 API，也不绕过访问控制。若作者能通过机构订阅或合法作者稿取得正文，最小补核对象为：

1. Wang–Li–Ng 2023：Definition of Hölder metric subregularity、exact-PPA corollary、rate exponent、solution-set/actual-iterate quantifier；
2. Moursi–Vanderwerff 2025：所有 “at each point” definitions、reflection-operator propositions、局部 modulus/remainder；
3. Luque 1984：inverse growth assumption 与 rate theorem 的原始 exponent/quantifier。

获取后只需提供 PDF；不需要手工摘录，后续应重新做 theorem-level comparison。

---

## 12. Expert-result contract

```yaml
contract_version: "1.0"
expert_skill: "sci-skills-literature-search"
project_id: "monotonicity-regularity-seesaw-2026-09"
paper_family: "T"
stage_id: "RL-FND-PRIOR"
task_id: "RL-FND-PRIOR-05"
task_status: "PARTIAL"
inputs_reviewed:
  - "work/rl_genuine_exponent.md"
  - "work/rl_nearest_deepread.md"
  - "work/rl_exact_prior_art.md"
  - "Li–Mordukhovich 2012 author-posted full text and official metadata"
  - "Mordukhovich–Ouyang 2015 author-posted full text and DOI metadata"
  - "Zhu 1995 Argonne primary prepublication and official metadata"
  - "Liu–Moursi–Vanderwerff 2023 arXiv full text"
  - "Adly–Rockafellar 2021 author-posted full text"
  - "Cibulka–Dontchev–Kruger arXiv full text"
  - "Hölder graphical derivatives paper arXiv:2106.08149 full text"
  - "Wang–Li–Ng 2023 official abstract and metadata"
  - "Moursi–Vanderwerff 2025 official abstract and metadata"
  - "Luque 1984 official abstract and metadata"
outputs:
  - "work/rl_foundations_structure_prior_art.md"
  - "work/rl_foundations_structure_claim_safe_matrix.md"
evidence_status:
  - "VERIFIED_PRIMARY_FULL_TEXT: Li–Mordukhovich 2012, Mordukhovich–Ouyang 2015, Zhu 1995, Liu–Moursi–Vanderwerff 2023, Adly–Rockafellar 2021, Cibulka–Dontchev–Kruger, arXiv:2106.08149"
  - "VERIFIED_OFFICIAL_ABSTRACT: Wang–Li–Ng 2023, Moursi–Vanderwerff 2025, Luque 1984"
  - "PENDING_FULL_TEXT: theorem-level overlap for Wang–Li–Ng 2023, Moursi–Vanderwerff 2025, Luque 1984"
  - "NEGATIVE_BOUNDARY_NOT_NOVELTY_PROOF: exact reflection remainder and stepwise two-anchor alignment searches"
  - "AI_INFERENCE: claim-safe novelty boundary and theorem-package assessment"
assumptions:
  - "Project exponent Q>1 means d(x,S)<=kappa*d(0,F(x))^Q"
  - "All Minty identities are branchwise unless maximality/full-range is separately available"
  - "A no-hit result is never treated as proof of novelty"
author_input_needed:
  - "Legally accessible full text of Wang–Li–Ng 2023"
  - "Legally accessible full text of Moursi–Vanderwerff 2025"
  - "Preferably the full text of Luque 1984 for historical theorem-level closure"
manual_actions:
  - "Use institutional access or request an author manuscript; do not bypass access controls"
  - "Provide obtained PDFs for theorem-level re-audit"
quality_checks:
  - "Formula and alias searches recorded verbatim"
  - "Only primary/official sources used for claims"
  - "Exponent conventions translated explicitly"
  - "Actual-iterate, set-distance, isolated, nonisolated, fixed-anchor, moving-anchor, and all-pairs quantifiers separated"
  - "Zhu 1995 theorem and alignment lemma treated as direct novelty threats"
  - "Paywalled sources marked PENDING rather than inferred from abstracts"
  - "No no-hit result upgraded to novelty"
conflicts: []
conflict_resolution_status: "NOT_REQUIRED"
merge_permission: "orchestrator_only"
recommended_next_action: "Obtain and theorem-audit the Wang–Li–Ng 2023 and Moursi–Vanderwerff 2025 full texts before freezing any first/novel wording for the endpoint or moving-anchor structure theorem."
stage_acceptance_recommendation: "REPAIR"
```
