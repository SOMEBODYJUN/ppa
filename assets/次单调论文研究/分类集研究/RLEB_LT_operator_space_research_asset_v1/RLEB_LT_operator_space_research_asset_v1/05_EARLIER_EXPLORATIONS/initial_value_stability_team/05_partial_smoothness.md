# 第 5 组：部分光滑、活动流形与初值极限选择

核查日期：2026-09-19。任务边界：文献审阅与可借用结构，不修改原 RLEB 或 solution-selection 稿，不声称提出新定理。已直接阅读下列原始论文的相关定理、假设及证明段落；定理号按注明的版本。

## 结论先行

**有人研究，而且有直接以“初值到迭代极限”映射为对象的先例；但 partial smoothness、有限辨识、tilt stability 这些词本身不能直接当成多解初值稳定性定理。**

本组发现的直接先例主要来自光滑流形上的投影／Newton 型迭代：

1. Schost–Spaenlehauer (2016)，Theorems 4.1–4.2：同一局部初值邻域上 Q-二次收敛；算法极限与最近点投影的误差为二阶；极限算子在每个满足假设的**解点**可微。
2. Chen–He–Huang (2026 预印本)，Theorems 2–3：clean intersection 下，交替投影及若干非精确变体的极限，在**切丛参数域**上为 C¹／C² 回缩。不是只有单轨道速率。
3. 经典 partial smoothness 文献主要给出“识别活动流形→在流形上计算”的接口；若要保留非孤立解集并控制选择，还要加上沿解流形的敏感度控制，不能简单加 tilt stability，因为后者通常把局部解变成唯一。

因此建议 RLEB 下一步优先吸收的经验是：**保持法向收敛证书不变，控制两条轨道之间累积的切向放大；局部非扩张只是一个方便但较强的充分条件，沿轨道可和的膨胀更贴近现稿。** 不宜把“partial smoothness”单独列为已经证明足够的答案。

## 1. 必须区分的四个对象

设固定算法为 T，Π_T(z)=lim T^k(z)。

| 对象 | 准确问题 | 与本题关系 |
|---|---|---|
| 单步 proximal 映射 | z ↦ prox_{λf}(z) 是否局部 C¹／Lipschitz | 可作输入接口，不是极限选择本身 |
| 有限辨识 | 对一条已知收敛轨道，是否存在 K 使 x_k∈M（k≥K） | 通常 K 依赖轨道，M 不一定是解集 |
| 数据／tilt 参数解映射 | v ↦ argmin[f(x)−⟨v,x⟩] 是否单值稳定 | 改变问题，不是固定问题改变初值 |
| 初值极限选择 | z ↦ Π_T(z) 是否两点 Hölder／Lipschitz／C¹ | 本次真正目标 |

特别要区分活动流形 M 与解流形 S：例如 f(a,r)=r² 完全光滑，其活动流形可取整个平面，而解集是直线 r=0。识别 M 不等于已经停止切向运动。若强制 Hessian 在整个 T_xM 上正定，常把解隔离掉；要保留多解，更自然的是允许沿 T_xS 零曲率，只控制横向方向及耦合。

## 2. 原始文献逐项对应

### P1. 已有的直接“快收敛＋初值极限可微”定理

Éric Schost, Pierre-Jean Spaenlehauer, **A Quadratically Convergent Algorithm for Structured Low-Rank Approximation**, *Foundations of Computational Mathematics* 16 (2016), 457–492. DOI [10.1007/s10208-015-9256-x](https://doi.org/10.1007/s10208-015-9256-x)，[arXiv:1312.7279](https://arxiv.org/abs/1312.7279)，已读 [原文 PDF](https://arxiv.org/pdf/1312.7279)。

**定理对应：** Theorems 4.1、4.2。E 为仿射空间，V 为光滑流形，W=E∩V；假设 P_V 在交点 ζ 附近 C²，E 与 V 在 ζ 横截。对共同小邻域内所有初值，NewtonSLRA 的极限 Φ(x) 满足

\[
\|x_{k+1}-x_\infty\|\le C\|x_k-x_\infty\|^2,
\qquad
\|\Phi(x)-P_W(x)\|\le C'\operatorname{dist}(x,W)^2,
\]

并且

\[
D\Phi(\zeta)=P_{T_\zeta W}.
\]

**覆盖：** 真正的非孤立解集、初值决定极限、Q-二次点收敛、解点处极限映射可微。

**未覆盖：** 不是一般 RLEB/resolvent 算子定理；Thm 4.2 只声称在解点 ζ 可微，不能擅自升级为整个欧氏邻域的两点 C¹ 或 Lipschitz。其几何、横截和二阶近投影条件明显强于现稿只有 Hölder 单步控制的假设。

### P2. 最新的直接“极限回缩”先例

Shixiang Chen, Yixiao He, Wen Huang, **Retractions by Alternating Projections**, [arXiv:2605.17384v1](https://arxiv.org/abs/2605.17384)，2026-05-17；本次按 [v1 全文](https://arxiv.org/html/2605.17384v1) 核查，未声称已有正式刊本。

**定理对应：** Theorem 2（C¹），Theorem 3（C² 和 second-order retraction）；Assumptions 1–3。两 C^{p,1} 流形 cleanly intersect，且满足文中迭代分解、精度与导数条件。结论针对

\[
\psi(x,\eta)=\lim_{k\to\infty}\varphi^k(x+\eta),
\qquad x\in M,\quad \eta\in T_xM.
\]

**覆盖：** 直接研究迭代极限的正则性，而非仅给距离收敛。法向收缩、切向单位作用、导数增量的一致可和是证明要点（Lemmas 4.8–4.9、4.12）。

**未覆盖／重要量词：** 定理域是 TM 的局部开集，不是任意欧氏初值 z 的完整邻域；本文没有直接给出一般 RLEB 类结论，也不能从摘要省略 Assumptions 2–3。此文是必须比较的直接先例，不能宣称“首次从迭代极限构造光滑回缩”。

### P3. 光滑横截给统一收敛，但原定理不是两初值稳定定理

Adrian S. Lewis, Jérôme Malick, **Alternating Projections on Manifolds**, *Mathematics of Operations Research* 33 (2008), 216–234. DOI [10.1287/moor.1070.0291](https://doi.org/10.1287/moor.1070.0291)，已读 [正式刊本作者副本](https://people.orie.cornell.edu/aslewis/publications/08-alternating.pdf)。

**定理对应：** Lemma 2.1 给光滑流形投影局部 C^{k−1} 及 DP_M(ζ)=P_{T_ζM}；Theorems 4.2–4.3 给横截流形的局部线性收敛，角度控制收敛率。

**覆盖：** 在共同局部范围内提供光滑单步映射和几何尾估计，可与一般尾界—模传递工具组合。

**缺口：** 不能把 Thm 4.3 的“一初值轨道到其极限的速率”直接引成对任意 x,y 的 Lipschitz 估计。完整两点结论需要另做推论并明确写出统一邻域。

### P4. 比横截更弱的 clean/non-tangential intersection

Fredrik Andersson, Marcus Carlsson, **Alternating Projections on Non-Tangential Manifolds**, *Constructive Approximation* 38 (2013), 489–525；已读 [arXiv:1107.4055v1](https://arxiv.org/pdf/1107.4055)，此处定理号按该版本，不虚构未核实的正式刊本 DOI 或定理重编号。

**定理对应：** Theorem 6.1。C² 非切触流形下，对给定 ε>0 和合适 c<1，存在共同初值球，迭代极限 B∞ 满足

\[
\|B_\infty-P_M(B)\|<\varepsilon\operatorname{dist}(B,M),
\qquad
\|B_k-B_\infty\|\le c^k\operatorname{dist}(B,M).
\]

**覆盖：** 初值与所选极限相对最近点投影的定量关系；比要求两个切空间和为全空间更弱。

**缺口：** 估计以单个 B 和 P_M(B) 为参照，不是两个任意初值的 Lipschitz 性。不能把“离投影很近”直接当成“极限映射两点 Lipschitz”。

### P5. 活动流形辨识的基本结果

Warren L. Hare, Adrian S. Lewis, **Identifying Active Constraints via Partial Smoothness and Prox-Regularity**, *Journal of Convex Analysis* 11(2) (2004), 251–266；[期刊正文](https://journalofconvexanalysis.com/articles/jca11017/jca11017.pdf)。期刊页面未列 DOI，不补造。

**定理对应：** Theorem 5.3：C^p 部分光滑（p≥2）、prox-regular、0∈ri∂f(\bar x)，给定 x_k→\bar x 且 f(x_k)→f(\bar x)，则

\[
x_k\in M\text{ 最终成立}
\quad\Longleftrightarrow\quad
\operatorname{dist}(0,\partial f(x_k))\to0.
\]

**覆盖：** 从近驻点轨道导出最终进入光滑活动流形。

**缺口：** 预先给定单条收敛轨道；没有直接比较 Π_T(x) 与 Π_T(y)，也没有自动给所有初值共同的辨识时刻。适合为后续光滑／切向分析提供接口，不能单独当作稳定性证书。

### P6. splitting 下的部分光滑识别与速率

Jingwei Liang, Jalal Fadili, Gabriel Peyré, **Activity Identification and Local Linear Convergence of Forward–Backward-type Methods**, *SIAM Journal on Optimization* (2017), DOI [10.1137/16M106340X](https://doi.org/10.1137/16M106340X)；已读 [arXiv:1503.03703v8](https://arxiv.org/pdf/1503.03703)。

**定理对应：** Theorem 3.4：已收敛序列、部分光滑、−∇F(x*)∈ri∂R(x*) → 有限辨识。§4 restricted injectivity 条件 ker∇²F(x*)∩T_{x*}M={0} 与非退化条件会导向唯一最小点，不能把这种正定路线误当作保留多解的弱条件。

**覆盖／缺口：** 非惯性凸 FB 的极限初值稳定可由单步非扩张直接推出；那是非扩张结构的结论，不是部分光滑的独占增量。文中 FISTA／惯性结论不能未经核验按同一非扩张论证处理。

对应 DR 文献：Jingwei Liang, Jalal Fadili, Gabriel Peyré, Russell Luke, **Activity Identification and Local Linear Convergence of Douglas–Rachford/ADMM under Partial Smoothness**, SSVM 2015，DOI [10.1007/978-3-319-18461-6_51](https://doi.org/10.1007/978-3-319-18461-6_51)，[arXiv:1412.6858](https://arxiv.org/pdf/1412.6858)。该预印本 Thm 3.1 是有限辨识，Thm 4.8 是局部线性化／速率；不是单独新建一般非凸初值稳定理论。

### P7. tilt stability 的用途与不适用之处

Dmitriy Drusvyatskiy, Adrian S. Lewis, **Tilt Stability, Uniform Quadratic Growth, and Strong Metric Regularity of the Subdifferential**, *SIAM Journal on Optimization* 23(1) (2013), 256–267. DOI [10.1137/120876551](https://doi.org/10.1137/120876551)，[正式刊本作者副本](https://people.orie.cornell.edu/aslewis/publications/13-tilt.pdf)。

**定理对应：** Theorem 3.3，在文中 prox-regularity／subdifferential continuity 等相应假设下，比较 strong metric regularity、tilt stability 与统一二次增长。

**覆盖：** 扰动 v 下局部逆 (∂f)^{-1}(v) 单值 Lipschitz。可认证唯一解的参数稳定。

**缺口：** 局部非孤立零集意味着 (∂f)^{-1}(0) 在该邻域不是单点，故不能直接满足这里的 strong metric regularity。若 RLEB 已保证全体近初值收敛到这个唯一局部解，Π_T 是常值；虽然稳定，但避开了用户关心的多解选择问题。

### P8. 可借用的“非凸图 → 活动流形”局部接口

Adrian S. Lewis, S. Zhang, **Partial Smoothness, Tilt Stability, and Generalized Hessians**, *SIAM Journal on Optimization* 23(1) (2013), 74–94. DOI [10.1137/110852103](https://doi.org/10.1137/110852103)，已读 [正式刊本作者副本](https://people.orie.cornell.edu/aslewis/publications/13-partial.pdf)。

**定理对应：** Proposition 4.5 给非退化、C² 部分光滑、prox-regular 情况下小 λ 的 extended-smooth reduction；Corollary 5.2 给局部子微分图的光滑流形约化。Theorem 6.3 的强临界／tilt-stable 等价仍属孤立稳定最小点路线。

**覆盖：** 把近驻点图写为活动流形上的光滑函数加法锥，可作为 RLEB 后续切向验证的接口。

**缺口：** 不能据局部图约化就自动声称所有完整 resolvent 纤维都相同；作者使用 f-attentive localization 与局部化条件。也不提供多解极限映射的一般正则性。

### P9. 自动微分研究的是哪个参数？

Sheheryar Mehmood, Peter Ochs, **Fixed-Point Automatic Differentiation of Forward–Backward Splitting Algorithms for Partly Smooth Functions**, [arXiv:2208.03107](https://arxiv.org/abs/2208.03107)，本次阅读 [v3 正文](https://arxiv.org/html/2208.03107v3)。

**定理对应：** Theorem 25 在 nondegeneracy 和活动流形 restricted positive definiteness 下，得到数据参数 u↦ψ(u) 的 C¹ 解映射及其导数；Lemma 30／Corollary 32 给单步 proximal／PGD 映射局部 C¹，后者不要求 Assumption 3.2 的 restricted positive definiteness。

**覆盖：** 单步平滑化接口，以及参数化问题的微分。

**缺口：** 不等于固定算子下，多个可能极限的初值选择 Π_T。将初始化也写为程序输入，并不能把“最终优化器局部唯一”的定理改造成非唯一解选择定理。

## 3. 与现稿 §5.2 的准确接点

本组直接检查了本会话上传的 `upload/02-research_note.md` §5.2。该节已经使用

\[
T(a,r)=(a+B(a,r),qr),\qquad
\operatorname{Lip}_a B(\cdot,r)\le Cr^\eta,
\]

从而

\[
\prod_{k\ge0}(1+CR^\eta q^{\eta k})<\infty.
\]

这不是空想方向，恰好对应成熟证明经验中的“切向累计放大有限”。但该稿自己已正确注明是标准离散 Gronwall，应保留这个归属，不将这一乘积估计本身宣传为新发明。

可以借用的结构按目标区分如下。

| 想恢复的结论 | 适合先检查的附加结构 | 必须保留的限制 |
|---|---|---|
| 某个正阶 Hölder | 在共同不变轨道邻域，单步 T 的两点 Lipschitz 常数有限，加共同几何尾 | 只是局部假设且共同邻域必须闭合；不能只在各自极限处检查 |
| Lipschitz | 所有有限步 T^k 的两点 Lipschitz 常数统一有界；更易验证的充分形式是沿轨道的膨胀可和 | 不能由每步 L>1 的固定上界直接得到 |
| C¹／更高 | 光滑活动／解流形、法向收缩、切向线性化为恒等、导数增量沿轨道一致可和 | 需要独立核实“活动流形≠解流形”、耦合项及共同吸引域 |
| 数据参数也稳定 | 上述结构及 RLEB 常数、邻域对参数统一，另有参数方向正则性 | 当前问题只研究初值，不能顺手宣称参数稳定 |

前两行是可独立验证的通用推论，不是本组找到的新优先权成果：若 

\[
\|T^k x-T^k y\|\le C\|x-y\| \quad(\text{同一 }C\text{，全部 }k),
\]

则 k→∞ 立即给出 

\[
\|\Pi_T(x)-\Pi_T(y)\|\le C\|x-y\|.
\]

若仅有单步 Lipschitz 常数 L>1 和共同尾界 Aρ^k，平衡 

\[
\|\Pi_T(x)-\Pi_T(y)\|\le 2A\rho^k+L^k\|x-y\|
\]

只得到某个 Hölder 指数 

\[
\theta=\frac{\log(1/\rho)}{\log L+\log(1/\rho)},
\]

不能未经额外控制称为 Lipschitz。L≤1 且共同轨道域上可逐步使用时，则极限直接非扩张。

## 4. 对“越弱越自然”的具体建议

1. **不优先加唯一性／tilt stability。** 它会使局部选择变成常值，过强而且容易失去原问题。
2. **不把 partial smoothness 单独当最终条件。** 它适合做结构接口：将算法局部约化到可算的切向／法向块。后面仍要验证敏感度如何累计。
3. **优先研究“非扩张＋可和缺陷”或“切向可和放大”。** 它允许有限或逐渐衰减的扩张，比要求每一步都非扩张更弱，也保留了不同初值选择不同解。
4. **若研究流形化扩展，比较 clean intersection、正常吸引／Morse–Bott 型结构。** 不必一开始要求全空间严格正定；允许解流形切向零模，同时控制横向谱与切向耦合。但将其精确翻译成一般 RLEB 的算子图条件仍是待证明工作，不能宣称现有文献已直接解决。
5. **不要按单条轨道的有限辨识 K(x) 直接拼接统一稳定定理。** 需要共同有限 K，或者可替代的统一有限步敏感度／尾部控制。如果初始前段只有 γ-Hölder，有限 K 步的模可能变为 γ^K，不能保留原指数不变。

## 5. 已覆盖与可保留空间

已覆盖：流形迭代的极限回缩、部分情形的极限可微性；部分光滑辨识；局部 proximal 光滑化；孤立解的 tilt／参数稳定；有限步差与尾界平衡等基本机制。

尚未由本组文献直接覆盖：

- 保留原 RLEB 非 calm／仅 Hölder 的核心广度，同时用真正弱而可核验的**算子图或切向条件**保证整个共同初值邻域的 Hölder／Lipschitz 选择。
- 与完整多值 resolvent、真实 min-residual、all-pairs RL 及局部预算严格兼容的统一接口。
- 从现稿三角结构推广到耦合法向动力学或一般曲面，同时给出明确常数与必要性／反例边界。

这些是“未被本组找到的定理直接覆盖”，不是首创认证。尤其 2026 年极限回缩论文表明这个方向仍活跃；拟提出定理必须逐条对照上述域、正则阶数和量词，不能只比较研究主题。

## 6. 审查状态与有限性

- 已核原文：P1–P9 上述定理及关键假设。
- P4 采用可读 arXiv 版本编号；正式版定理号未逐页复核。
- P2 是 2026 年预印本，本文报告其定理陈述与证明机制，不代表独立验收该 63 页稿的全部证明。
- 未对全球所有 partial-smoothness／retraction 文献作穷尽检索。
- 本组没有改动任何上传稿、没有新建 RLEB 定理，也没有将数据稳定偷换成初值稳定。
