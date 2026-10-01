# RL 理论的新颖性、数学价值与投稿层级评估

> 版本：2026-09-01 研究检查点  
> 状态：**provisional / repair required**。本文不是“新颖性证书”，也不是录用预测。

## 1. 结论先行

### 1.1 最初长期任务是否完成

没有完成。

目前已完成的是一轮可继续维护的研究底稿：理论 atlas、77 个 canonical example 的 gap catalog、逐例复算和第一版 synthesis。它已经足以否定“所有 monotonicity 与 regularity 可排成一条一维跷跷板”这一过强设想，但还没有完成用户要求的穷尽性文献核验、全部严格关系的多例支撑、所有算法族的统一比较和最终统一/否定定理。

当前项目仍处于理论路线 T2：**理论谱系与精确先例核验**。第一版 synthesis 只能作为 provisional hypothesis report，不能当最终结论。

### 1.2 RL 是否新颖

分三层回答：

| 主张层级 | 当前判定 | 原因 |
|---|---|---|
| “Hölder 映射 \(\|Rx-Ry\|\le L\|x-y\|^\gamma\) 是新概念” | **否** | 一般 Hölder mapping 已有 Kirk/Barroso 等先例；令 \(R=R_{\lambda F}\) 不会使 map-side 公式本身变新。见 [Barroso 2023](https://arxiv.org/abs/2207.03057)。 |
| “\(\gamma=1\) 的 RL 是新 generalized monotonicity” | **否** | 它精确落在 equal-parameter semimonotonicity 的 tied curve；\(L\ge1\) 时与 Luke--Tam submonotonicity 换参等价，\(\tau=(L^2-1)/4\)。见 [Luke--Tam 2025](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863) 与 [Evens et al.](https://link.springer.com/article/10.1007/s10107-024-02182-0)。 |
| “\(0<\gamma<1\) 的 operator-side Hölder--Cayley 图理论及其算法后果” | **可能有新意，但未完成核验** | 本轮未找到完全相同的 operator-graph theory；但 Cayley pullback 本身是直接代数，故新意必须来自非平凡 calculus、maximality/range、sharp examples 或新算法定理，而不能只来自定义。 |

所以最安全的定位是：

> RL 不是一个已经可以无保留宣称“全新”的定义；它是一个可能产生新算子理论的 Hölder--Cayley 坐标框架。论文价值取决于该框架能否产生现有一般 Hölder-map、semimonotonicity 和 fixed-point regularity 理论不能直接给出的结果。

### 1.3 RL 是否有价值

**有研究价值，但当前价值集中在结构问题，不在名称和等价改写。**

已经确认有内容的部分：

1. \(0<\gamma<1\) 的 defect 是 scale-dependent：近对角线的相对二次 violation 发散，大尺度行为反而更强；它不能放入普通一维 monotonicity 强弱轴。
2. all-pairs、solution-anchored、input-nearest anchored 和 orbit profile 可以具有不同指数；这不是术语差别，而会改变实际 PPA rate。
3. 一般 gauge composition 比机械的 \(\gamma q\) 更本质；但 composition 本身仍不是新理论，必须增加 sharpness 或 necessity。
4. 新的内部结构定理表明，高阶 regularity 与 Cayley 几何之间存在比原稿更精细的三层分解：pairwise roughness、centered reflection defect、solution drift/alignment。

## 2. 当前数学上真正站得住的成果

### 2.1 代数与几何字典

对受限 graph \(\Gamma\)，RL 精确等价于：

\[
\|R_\Gamma x-R_\Gamma y\|\le L\|x-y\|^\gamma.
\]

RL 本身强迫 Minty parametrization 在 \(\Gamma\) 上单射，因而受限 resolvent/reflected resolvent 在自然 Minty range 上单值。它不自动给出 full domain、surjectivity、maximality 或局部输入球覆盖。

\(\gamma=1\) 的精确 tied semimonotonicity 参数为

\[
\mu_L=\frac{1-L^2}{2\lambda(1+L^2)},\qquad
\rho_L=\lambda^2\mu_L.
\]

### 2.2 PPA 的条件性一步递推

在合法局部分支、RL localization 与 power subregularity 同时覆盖当前步时，原稿的一步估计正确：

\[
d(x^+,S)
\le \frac{\rho}{(2\lambda)^q}
\bigl(r+Lr^\gamma\bigr)^q,
\qquad r=d(x,S).
\]

因此 \(0<\gamma<1\) 时可得

\[
d(x^+,S)=O(r^{\gamma q}).
\]

但这只是 upper recurrence，不是已证 exact order、necessary boundary 或 universal compensation law。已有显式例子显示真实轨道可为 \(q>\gamma q\)。

### 2.3 新的 structure theorem：比 \(\gamma q\) 更重要

令

\[
x=y+\lambda w,\qquad R_{\lambda F}x=y-\lambda w,
\qquad w\in F(y),
\]

并设

\[
d(y,S)\le \rho\,d(0,F(y))^q,\qquad q>1.
\]

若 \(p_y\) 是 \(y\) 的最近或足够精确的近似最近零点，则

\[
R_{\lambda F}x-p_y
=-(x-p_y)+O(\|x-p_y\|^q).
\]

特别地，若零点 \(p\) 局部孤立，则沿任何已存在的局部 Minty branch，

\[
J_{\lambda F}x-p=O(\|x-p\|^q)
\]

可由 \(q\)-subregularity 本身推出，不需要 RL。因而在孤立零点情形，\(O(r^{\gamma q})\) 通常是偏松的，正确的 centered rate upper bound 是 \(O(r^q)\)。

非孤立零点时，output-nearest anchor \(p_y\) 与 input-nearest anchor \(p_x\) 会发生切向漂移。若 alignment profile 为

\[
\|x-p_y\|=O(d(x,S)^\theta),
\]

则更准确的结论是

\[
d(Jx,S)=O(d(x,S)^{\theta q}).
\]

原来的 \(\gamma q\) 是 \(\theta=\gamma\) 的充分情形。由此，值得发展的对象不是单一 \(\gamma\)，而是

\[
\boxed{
\text{pairwise Cayley roughness}
\;\oplus\;
\text{centered reflection defect}
\;\oplus\;
\text{solution drift/alignment}.}
\]

这一结构目前是内部新推导，尚未完成外部 prior-art 审计，不能直接宣称首次。

## 3. 当前原稿为什么不能投稿

原稿的 RL--IP、自然 Minty 域上的 RL--AFNE 等价及条件性一步估计基本正确。投稿阻断项是 Theorems 1--3 尚缺完整量词：

1. 没有保证 \(\operatorname{ran}(I+\lambda F)\) 覆盖一个局部输入邻域，PPA 可能根本无定义；
2. local graph 上的 RL 只使局部分支单值，不能排除 full resolvent 的远端分支；
3. “充分接近 \(S\)”不能控制非孤立解集的切向漂移，需要显式 two-radius/invariant margin；
4. Cauchy 极限属于 \(S\) 需要局部闭性或 branch continuity/fixed-point 论证；
5. \(\gamma q\)、临界常数和 gauge 条件当前都是 sufficient upper guarantees，尚未证明必要或 sharp。

这些是 major reconstruction 问题，不是文字润色问题；但它们是可修的，不等于核心递推为假。

## 4. 期刊层级：按三种成果包判断

| 成果包 | 当前评价 | 条件性期刊校准 |
|---|---|---|
| 当前初稿 | 不宜投稿；desk/reviewer 风险极高 | 暂不投正式期刊 |
| 修复后的聚焦 RL--PPA 论文 | 完整局部定理、明确 branch/range、4--8 个自然例、sharp/nonsharp 边界、完整 prior-art 对照 | 可校准到扎实专业理论期刊：fixed-point 取向参考 [JFPTA scope](https://link.springer.com/journal/11784/aims-and-scope)；operator/set-valued 取向参考 [SVVA scope](https://link.springer.com/journal/11228/aims-and-scope)；算法含义明显增强时可将 [JOTA scope](https://link.springer.com/journal/10957/aims-and-scope) 作为冲刺 |
| 强化后的统一框架 | anchored/gauge-Cayley theorem、必要或近必要 compatibility、exact/asymptotically sharp rates、自然问题类、variable/inexact PPA 或另一算法族 | 才能考虑 [SIAM Journal on Optimization](https://www.siam.org/publications/siam-journals/siam-journal-on-optimization/)；只有方法论深度和 OR/MS 相关性都显著时才考虑 [Mathematics of Operations Research](https://pubsonline.informs.org/page/moor/editorial-statement) 的高风险冲刺 |

最现实的判断是：

> **当前不是“能发什么档次”，而是“尚未形成投稿稿件”。若完成严格修复并把新 structure theorem 做成主线，达到 JFPTA/SVVA 一类专业期刊是现实目标；若再得到 sharp/near-necessary 的统一理论和更广算法后果，才有理由向 JOTA 或更高层级推进。**

以上是成果包校准，不是录用承诺，也没有使用影响因子、分区或录用率传闻。

## 5. 推荐的论文重构路线

### 路线 A：聚焦、较快形成一篇可靠论文

暂时不用“RL-submonotonicity”作为卖点标题，工作名改为 **Hölder--Cayley graph geometry**。主线为：

1. restricted graph / Minty-domain 的严格定义；
2. \(\gamma=1\) 与 semimonotonicity 的精确边界校准；
3. \(0<\gamma<1\) 的 scale-dependent graph geometry、inverse/scaling；
4. named local resolvent branch 下的完整 gauge-PPA theorem；
5. isolated/nonisolated solution 的分裂定理；
6. genuine all-pairs exponent、nonsharp orbit、exact drift-product 三类例子。

这一路线对应专业理论期刊成果包。

### 路线 B：延迟投稿，争取更强论文

把主对象升级为三 profile 框架：

1. pairwise Cayley modulus；
2. centered reflection-defect gauge；
3. solution alignment/drift gauge；
4. 与 inverse error-bound gauge 的 composition；
5. necessary/near-necessary compatibility；
6. 至少扩展至 variable/inexact PPA 或另一 splitting algorithm。

这一路线风险更高、时间更长，但更可能产生真正独立于现有 Hölder-map pullback 的统一理论。

## 6. 尚未解决的新颖性风险

1. Moursi--Vanderwerff 2025 关于 bounded-set/pointwise uniform monotonicity 与 reflection operator 的全文尚未取得，是最重要的直接风险。见 [官方页面](https://link.springer.com/article/10.1007/s10957-025-02633-4)。
2. Rolewicz、Ngai--Penot、\(\rho\)-paramonotonicity等 nonlinear-gauge graph 文献尚需逐式全文核验。
3. 普通 web 检索不能替代 MathSciNet、zbMATH、Scopus/Web of Science 的前后向引文链；本轮 negative finding 不能当“文献不存在”的证据。
4. 新 structure theorem 目前只做了内部证明与反例压力测试，尚需独立外部先例检索及正式 manuscript-level proof polishing。

## 7. 当前可信判断

1. **RL 作为“定义”新颖性偏弱。**
2. **RL 作为 operator-side 理论框架仍可能有价值。**
3. **原稿的 \(\gamma q\) 不是普遍精确规律；它更像 solution-alignment exponent 与 error-bound exponent 的一个充分乘积。**
4. **最有潜力的新成果已经从“提出 RL 定义”转移到“解释 all-pairs roughness、centered reflection 与 solution drift 为什么分离，以及这如何决定 PPA rate”。**
5. **当前稿不宜投稿；完成 major reconstruction 后，专业理论期刊是现实目标，更高层级取决于 sharpness、统一性和算法广度。**

