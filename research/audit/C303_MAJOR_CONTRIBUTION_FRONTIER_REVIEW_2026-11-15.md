# C303 主要贡献门独立审查

日期：2026-11-15  
状态：**continue validation**；不是“达到主要贡献标准”，也不是“淘汰”。

本审查独立重构当前 C303 的完整目标、最接近的先行结论、已获得的条件性引理和仍会阻止主要贡献裁决的义务。它不把局部恒等式、数值趋势或搜索未命中升级为定理或首创性。

## 精确目标和当前裁决

候选主张是：对 HJ 的同一个 (C^\infty) 势 (f)，取
[
\chi_a=af-\tfrac12\|\nabla f\|^2,
\qquad F=\nabla\chi_a,
\]
在 (a>\sup\lambda_{\max}(\nabla^2f)) 和一个变量步隐式惯性 PPA/resolvent 方案下，存在一个相空间非空开集 (U)，使得每个从 (U) 出发的轨道全局定义、有界且满足 (omega=S^1)，从而不收敛。

当前证据只支持下列较弱身份：

- 连续 HJ 螺旋管的首次离开机制有条件性 bootstrap；
- EP1–EP3 是终点 resolvent 方程的精确代数恒等式；EP4 可给出首接触障碍，EP7–EP8 可给出双侧角度增量；
- EP6 的平面 face 例子说明 (q_k=\|w_k\|) 项是结构性必要的，不能删除；
- (W_k=e^{z_k^2}) 只在固定 (alpha\in(1/2,1))、同一首个 drop threshold、统一 normal recursion、统一 finite-prefix 常数和 source/lift 条件下，条件性地把 (m_{\rm face}) 与 (phi) 的首接触门推进到 (q_k+h_k=o(m_{\rm face}),o(\phi))；
- 现有 (O(h_k)) 首接触误差在 (alpha=1/2) 处留下 (h_k/\phi(\theta_k)\asymp\sqrt{\log k}) 障碍。

因此裁决为 **继续验证**。这里没有足以淘汰条件性链条的反例，但也没有可把它升级为完整离散开盆定理的证据。

## 与最近先行工作的关系

项目的 priority audit 已核对：一般变量步隐式二阶格式、inertial PPA/resolvent 重写和以能量或 Łojasiewicz 机制证明离散平衡收敛的工作已经存在。因此“使用惯性 PPA”或“建立一个 W 超解”不能单独承担主要贡献。

HJ 2020 的已核对象是圆形 (omega)-极限的一阶梯度构造，并明确把二阶阻尼系统的相空间开集非收敛问题留下为开放方向。若 C303 最终闭合，它的潜在增量是把同一 HJ 几何真正桥接到变量步隐式二阶离散动力学，并在相空间开集上证明 (omega=S^1)。这个增量可能实质，但目前仍是 conditional candidate；局部 EP/W 结果本身不构成四大级贡献。

## 阻止“达到主要贡献”裁决的义务

1. **source 与向量场身份。** HJ 文字把某处的 (X) 写成 (
abla f)，而显式径向项与 (Y=-\nabla f) 相符。必须在 C303 的全部 normal recursion、边界符号和 resolvent 方程中固定同一身份。cutoff 的 (C^\infty)、值域、初始区域归一化、支撑条件和正实轴 branch-cut 两侧 jets 仍需逐字从原构造闭合；当前 dumbbell/平台管是 source-conditional 安全构造。

2. **共同开集与 finite-prefix 量词。** 现有 `c303_finite_prefix_margin.md` 的明确范围仍是固定 (alpha>2/3)。W 路线若要使用任意固定 (1/2<alpha<1)，必须在同一个 (K_*) 上证明有限前缀安全带、(T_{\rm tr}=t_{K_*}\le T_*<\infty)、(W_{K_*})、(E_*) 和 (C_\varepsilon) 对同一初始开集及足够小 (h_0) 一致有界。否则 transient 项的 (O(h_0^2)) 吸收可能依赖初始 lift 或 (h_0^{-1})。

3. **首接触同伦与 coverage。** EP4/EP7–EP8 的使用需要 (I-\beta H) 在完整缩放 (	au)-同伦上统一可逆、端点位移 bootstrap、同一紧 pre-contact patch、物理投影 lift/injectivity 以及 (q_k) 递推。它们目前是条件接口，而不是共同停止域已经闭合后的自动推论。

4. **完整离散结论。** 尚未把这些条件接口合并成：对一个明确的相空间开集 (U) 的全称量词、每一步 resolvent 分支的全局存在、整条轨道留在同一 lifted 管、无限时间有界性以及 (omega=S^1)。只有这条链完整闭合，候选主张才从“可能的新机制”变成可审查的主要数学结果。

5. **外部优先性。** 当前检索只排除了若干最近的 generic inertial/implicit second-order 结果，没有证明 EP/W 或整个离散 HJ 桥的首创性。必须逐项对比同一 (F=\nabla\chi_a)、步长、相空间开集和 (omega)-结论，而不能用“未检索到”替代优先性证明。

## 哪种证据会改变裁决

最小的改变裁决证据是一个完整、可复核的定理，明确给出：

- HJ cutoff/source 的逐字适用条件与统一 (Y=-\nabla f) 约定；
- 固定 (\alphain(1/2,1))（或一个已证明的更大范围）下的共同 finite-prefix 开集、(T_*\) 和所有常数；
- 同一停止域上的全局 resolvent coverage、统一缩放同伦和 normal-error 递推；
- 端点首接触禁止、无限时间留域、角度发散与 (omega=S^1) 的全称结论；
- 与 HJ 2020 及最近惯性/隐式二阶离散工作的逐项对象差异和可核先行性说明。

反方向的决定性证据是：原始 HJ cutoff 的精确条件与当前构造不相容，或某个满足当前明确假设的 (q_k)、lift、finite-prefix 或 resolvent 分支反例破坏首次离开链。

## Truth / Value / Novelty / Mechanism / Ambition

- **Truth：** 条件性引理和局部恒等式已有支持；完整 C303 主张未闭合。
- **Value：** EP1–EP8、(q_k) 必要性和 W 接口提供了可复用的技术理解，价值可能实质。
- **Novelty：** provisional；generic 算法模式已有先例，完整 HJ 离散桥的优先性仍待核。
- **Mechanism：** 局部机制更清楚，尤其是 shrinking margin、normal error 和 (alpha=1/2) 障碍；尚未形成完整动力学机制定理。
- **Ambition：** 仍保留原始相空间开盆非收敛目标，但目前只能标为 candidate。

最终裁决：**continue validation**。本轮没有“达到主要贡献标准”的依据；下一项最有信息价值的任务是闭合或反驳固定 (alpha>1/2) 的 finite-prefix/common-open-set 量词，而不是继续扩展局部 W 或 EP 文字。
