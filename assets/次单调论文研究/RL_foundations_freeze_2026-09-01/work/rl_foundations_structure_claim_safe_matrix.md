# RL structure theorem：claim-safe prior-art matrix

> 对应任务：`RL-FND-PRIOR-05`。本表只用于决定“可写什么/不可写什么”；没有命中的格子不是新颖性证明。证据详见 [`rl_foundations_structure_prior_art.md`](rl_foundations_structure_prior_art.md)。

## 状态标签

- **KNOWN**：primary full text 已直接覆盖核心主题或公式。
- **KNOWN_ADJACENT**：已有结果非常接近；当前版本只能主张更窄的结构差异。
- **POTENTIAL_DISTINCTION**：本轮未检到精确同型，但仍有未核全文或检索边界。
- **PENDING_FULL_TEXT**：关键论文只有官方摘要/元数据。
- **NEGATIVE_BOUNDARY**：有边界未命中；绝非 novelty proof。

## Claim-safe matrix

| ID | 候选 claim | 最近 primary source | 已核验重叠 | 当前可守住的区别 | claim-safe 写法 | 不安全写法 | 状态 |
|---|---|---|---|---|---|---|---|
| C1 | \(Q>1\) higher-order metric/strong subregularity 是新概念 | Mordukhovich–Ouyang 2015 | 任意 \(q>0\) 的定义，重点 \(q>1\)；growth、perturbation、Newton applications | 无定义级区别 | “We use higher-order strong subregularity in the sense of…” | “We introduce higher-order metric subregularity.” | **KNOWN** |
| C2 | higher-order subregularity 首次连接 PPA | Zhu 1995；Luque 1984；Li–Mordukhovich 2012 | inverse growth 已连接 PPA rate；Zhu 对 \(r>1\) 给 actual-iterate 高阶超线性 | 可强调 branchwise endpoint equivalence、reflection remainder 或 nonmonotone scope | “We sharpen/recast the one-step Minty structure under our branch assumptions.” | “This is the first link between higher-order subregularity and PPA.” | **KNOWN** |
| C3 | 孤立零点下 fixed-step PPA 直接 \(Q\)-order | Zhu 1995；Mordukhovich–Ouyang 2015 | Zhu 正式结论是每个 \(t<Q\)；MO 是 Newton-type；但 isolated endpoint 可由同型 EB 与 PPA step 直接推出 | endpoint \(O(e_k^Q)\) 的显式 branchwise equivalence；可能宽于 maximal monotone | “Under an existing local Minty branch, the error bound yields the endpoint upper recursion directly.” | “The first superlinear/q-order PPA theorem under higher-order subregularity.” | **KNOWN_ADJACENT**；Wang 2023 **PENDING** |
| C4 | \(Jx-p=O(\lVert x-p\rVert^Q)\iff R x=2p-x+O(\lVert x-p\rVert^Q)\) | Cayley identity；Adly–Rockafellar 2021 | resolvent derivative/sensitivity 已知；二式由 \(R=2J-I\) 精确等价 | 可作为清晰的 structural equivalence，而非单独重大新定理 | “An explicit higher-order Cayley reformulation.” | “A fundamentally new reflected-resolvent phenomenon.” | **POTENTIAL_DISTINCTION / NEGATIVE_BOUNDARY** |
| C5 | moving-anchor asymptotic reflection \(R x-p_y=-(x-p_y)+O(\lVert x-p_y\rVert^Q)\) | Liu–Moursi–Vanderwerff 2023；Moursi–Vanderwerff 2025 | 2023 给 all-pairs reflected defect；2025 只核验摘要/关键词 | output-nearest moving center、局部 one-pair remainder | “We identify an output-centered asymptotic reflection law.” | “No previous work has pointwise reflection results.” | **POTENTIAL_DISTINCTION**；2025 **PENDING_FULL_TEXT** |
| C6 | 非孤立解集上 PPA 高阶超线性是新结果 | Zhu 1995 | 非单点解集、actual iterates、\(r>1\)、任意 \(t<r\) 的 Q-superlinear | endpoint、非单调 branch、两锚点定量结构若确有完整证明 | “Our distinction concerns endpoint/two-anchor structure, not the existence of nonisolated high-order PPA convergence.” | “First nonisolated superlinear PPA result.” | **KNOWN** |
| C7 | PPA 轨道首次出现 tangent/normal alignment | Zhu 1995 Lemma 4.1 | 轨道误差相对 \(T_S(\bar z)\) 渐近法向化 | stepwise \(p_y/p_x\) alignment exponent \(\theta\)，uniform map-level bound | “We quantify a stepwise two-anchor alignment not supplied by Zhu’s asymptotic orbit lemma.” | “We first discover alignment of PPA trajectories.” | **KNOWN_ADJACENT** |
| C8 | \(d(Jx,S)=O(d(x,S)^{\theta Q})\) 是新的 general law | Zhu 1995；当前 elementary composition | Zhu 无显式 \(\theta Q\) endpoint，但指数相乘本身是一行复合 | 可验证 \(\theta\) 的 operator criterion、matching lower bound、sharp example | “The theorem isolates alignment as the missing quantitative factor; sharpness is established separately.” | “The exponent multiplication alone is a major theorem.” | **POTENTIAL_DISTINCTION** |
| C9 | exact \(\theta Q\) sharpness / moving solution drift | 本轮未命中精确同型 primary theorem；Zhu 是邻近风险 | 无同型公式命中；但 bounded audit 不完备 | 若有自然 family、上/下界匹配且量词无漏洞，可形成真正贡献 | “Our examples show the conditional upper exponent is attained in the stated class.” | “No literature contains such examples, hence ours are first.” | **NEGATIVE_BOUNDARY** |
| C10 | strong subregularity 的 graphical derivative kernel criterion 是新结果 | Cibulka–Dontchev–Kruger；arXiv:2106.08149 | ordinary 与 Hölder/high-order derivative criteria 已知 | 将其正确接入 RL/Minty branch 的应用性 corollary | “We invoke an existing derivative criterion to verify the assumption.” | “We establish the first graphical-derivative characterization.” | **KNOWN** |
| C11 | coderivative 对 higher-order subregularity 给一般 iff | Cibulka–Dontchev–Kruger | 一般为 bound/sufficient structure；等号/iff 需额外假设 | 仅在原 theorem 的维数与局部凸性范围内陈述 | “A coderivative bound is available under…, with equality under local graph convexity.” | “For every multifunction, SMSR iff the coderivative kernel is trivial.” | **KNOWN WITH SCOPE RESTRICTION** |
| C12 | Wang–Li–Ng 2023 不覆盖 \(Q>1\)/endpoint | Wang–Li–Ng 2023 official abstract | 摘要只确认 Hölder MSR、inexact/exact PPA rates | 无法确认 | “A theorem-level comparison is pending full-text access.” | 任何肯定的覆盖/不覆盖断言 | **PENDING_FULL_TEXT** |
| C13 | Moursi–Vanderwerff 2025 不覆盖 centered reflection | Moursi–Vanderwerff 2025 official abstract | 摘要确认 at-each-point notions；keyword 有 reflection | 无法确认 | “Potential overlap remains pending full-text review.” | “Their paper is unrelated to our reflection theorem.” | **PENDING_FULL_TEXT** |

## 最终 claim gate

| gate | 当前判定 | 锁稿条件 |
|---|---|---|
| 数学正确性 | 由 proof-referee 另审；本任务不替代证明审计 | branch existence、anchor choice、quantifiers 全部闭合 |
| 广义新颖性 | 不通过 | 删除“首次非孤立超线性/首次 alignment”等 claim |
| 窄结构区别 | 条件通过 | 明确 endpoint、two-anchor、restricted/nonmonotone scope |
| 排他性 novelty wording | 不通过 | 先核验 Wang 2023 与 Moursi–Vanderwerff 2025 全文 |
| 投稿级贡献 | 尚需 theorem package | alignment criterion + sharpness + natural examples + prior-art differentiation |

## 可直接交给主稿的最短定位

> Zhu’s finite-dimensional maximal-monotone analysis already yields nonisolated actual-iterate superlinear convergence under an inverse growth condition and an asymptotic normal-alignment lemma. Accordingly, our contribution is not the broad existence of high-order PPA convergence. We instead isolate a one-step two-anchor mechanism: higher-order output flatness gives asymptotic reflection about an output-nearest solution, while a separate quantitative alignment exponent controls how this moving anchor translates into a set-distance rate.

## 证据状态

```yaml
task_id: "RL-FND-PRIOR-05"
matrix_status: "PARTIAL"
verified_full_text_core:
  - "Mordukhovich–Ouyang 2015"
  - "Li–Mordukhovich 2012"
  - "Zhu 1995"
  - "Liu–Moursi–Vanderwerff 2023"
  - "Adly–Rockafellar 2021"
  - "Cibulka–Dontchev–Kruger"
  - "arXiv:2106.08149"
pending_full_text:
  - "Wang–Li–Ng 2023"
  - "Moursi–Vanderwerff 2025"
  - "Luque 1984"
novelty_rule: "No exact-formula hit is treated as a negative boundary only, never as proof of novelty."
merge_permission: "orchestrator_only"
```
