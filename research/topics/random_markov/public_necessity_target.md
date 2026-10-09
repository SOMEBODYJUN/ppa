# 从仓库资产到公开必要性问题

<a id="pnt-decision"></a>
## 选题判断与发布路线

核查基线：`60456a325e5eb46294c8211f44dca0b95f59ec27`；公开来源核查日：2026-10-09 UTC。本页是公开问题的定位、精确版本和资产接口，不是完整作者问题已经解决的声明，也不替代现有证明。

**推荐先做随机迭代的误差界必要性边界。** 它有作者明确提出的公开问题，且本库 C14/C143/C144 已给紧性、速率与反例工具。剩余义务主要是问题量词对接、反例先行性和可发表的完整表述，信息成本较低。不能把已经有证明的模型再次当作未知命题无限搜索。

**发布主线建议（研究判断）**：以固定核一般模 GPPA 的完整 union 关系、标量收缩编译与独立物理提升为主线，原 RLEB 由 `v=Id` 作特例。调用 [C208–C214](../../canonical/generalized_ppa_modulus.md) 及其现存证明；不以经典 ASM、任意阶标签或单个非 calm 例子承担全部创新。结构/影子/完整纤维稿是另一条数学对象线，独立保留。Markov 必要性可以形成独立短稿，避免把所有旁支塞进 GPPA 主论文。以上是编排建议，不是期刊接收或新颖性保证。

| 资产 | 当前可以承担的工作 | 仍缺什么 |
| --- | --- | --- |
| C208–C214、C216/C220 | GPPA–RLEB 主论文：完整关系、标量证书、物理/误差边界 | 最终篇幅与统一表述、精确贡献的先行比较 |
| C14/C143/C144 | 公开随机律必要性问题的三层边界 | 原问题解释、源条件逐项对应、反例与兼容性边界的先行性 |
| C15/C71/C80、C127 | 有限状态认证、真实 OT 优化、回耦工具 | 到新随机算法的同对象桥，不能默认调用 |
| C03/C04/C18/C222 | 独立结构稿：配对影子、纤维、精确预算 | 原生对象应用、锐表述的先行比较 |
| 总体母空间/大小比较、M1 原生身份 | 明确障碍与待恢复接口 | 对象与量尺未冻结或原方程缺失；暂不作为下一轮主题 |

<a id="pnt-source"></a>
## 一手公开来源

1. Luke–Schultze–Grubmüller, *Stochastic algorithms for large-scale composite optimization: the case of likelihood maximization for X-FEL imaging*, [正式刊本](https://link.springer.com/article/10.1007/s10107-025-02319-9), Math. Program. 217 (2026), 407–437；在线 2026-01-12。实际阅读 Assumption 3、(10)、(15)–(18)、§3.2 (39) 后开放问题段落。该处明确提出：现有随机迭代设置下，metric subregularity 是否必要。DOI 中的 2025 不作为发表年份。
2. D. Russell Luke, *Convergence in distribution of randomized algorithms: the case of partially separable optimization*, [正式刊本](https://link.springer.com/article/10.1007/s10107-024-02124-w), Math. Program. 212 (2025), 763–798；在线 2024-07-27。实际阅读 (46)、Theorem 9 及 §6：作者提出非 paracontractive Markov 算子的定量收敛是否仍需 metric subregularity；已证必要性定理有额外 paracontraction 与 gauge-monotonicity 前提。
3. Hermer–Luke–Sturm, *Rates of convergence for chains of expansive Markov operators*, [正式来源](https://academic.oup.com/imatrm/article/7/1/tnad001/7459406), Trans. Math. Appl. 7 (2023), tnad001。检索返回的原刊全文 §3.2 明确区分 discrepancy 的零集与不变律集，不默认二者相同；本轮直接 `open` 页面失败，故其余定理不在此新增导入。假零机制不能仅凭这次对接就声称首次发现。

本轮定向检索 `Markov transport discrepancy necessary/counterexample`、`not paracontractions metric subregularity` 及上述题名，找到上述公开重述及有附加前提的必要性定理，未取得一般问题已解决的后续证据。这只描述有限检索范围，不证明全球仍未解决或我们首次回答。

<a id="pnt-exact"></a>
## Q-PUB-RFI-v1：必须先固定的三个版本

**Status：`open`，指作者问题的完整解释与发表定位尚未关闭。** 下列 A/C 的否定机制在既有证明范围成立；B 的紧类结论已有证明。作者开放段落没有给全部形式量词，因此 A/B/C 是本库的 **Interpretation**，不能冒称原作者逐字猜想。

**Objects / Domain / Definitions。** 非空紧 `G⊂R^d`，有限连续自映射 `T_j:G→G`，独立同分布且独立于当前状态的指标，固定概率 `p_j`。记 `μP=Σp_j(T_j)#μ`、全部不变律集 `I={π:πP=π}`、平方 Euclidean 运输距离 `W₂`，以及

\[
\Psi(\mu)^2=\inf_{\pi\in I}\inf_{\eta\in\operatorname{Opt}(\mu,\pi)}
\int\sum_jp_j\|(x-T_jx)-(y-T_jy)\|^2\,d\eta.
\]

`Opt` 是给定完整边缘的 **输入 W₂ 最优计划**；两状态共享同一指标。不可删除最优约束，或改成真实 law-step 而继续沿用问题身份。源期望 almost-firm 前提为全部 `x∈G` 及不变律支撑内 `y` 上

\[
\mathbb E\|T_\xi x-T_\xi y\|^2
\le(1+\varepsilon)\|x-y\|^2-\tau c_R(x,y),
\quad \tau=(1-\alpha)/\alpha>0,\quad0\le\varepsilon<1.
\]

**Quantifiers / Conclusions。** 固定一个系统，在上述前提下，假设全部初律存在不变极限 `Πμ`，同一 `C<∞, 0<r<1` 对全部 `μ,k≥0` 给 `W₂(μP^k,Πμ)≤Cr^k d(μ,I)`。应分别判以下必要性。A 的局部量词固定为：对每个 `barπ∈I`，是否存在 `a>0` 与一个这样的 `ρ`，对所有 `W₂(μ,barπ)<a` 的律给目标 EB；C144 在同一个指定 `barπ` 的每个正半径球均否定。B 使用完整律空间；C 的局部门固定为 C143 的 `δ₀` 球和全部充分小标量参数：

| 版本 | 精确待检验结论 | 当前证据与边界 |
| --- | --- | --- |
| A：不预授 exact-zero | 是否存在零处取零的连续严格递增 gauge `ρ`，在上述明确局部域有 `d(μ,I)≤ρ(Ψ(μ))`？ | C144 否定；局部也失败。不能称 Ψ 到它自身零集的 subregularity 失败。 |
| B：预授 `Ψ⁻¹(0)=I`，只求任意一般 gauge | 是否存在 `ρ`，使上述界成立？ | C14 在当前紧连续类中已由下半连续性给全局 gauge，与速率无关；不是待盲搜的新题。 |
| C：预授 exact-zero，要求线性/正幂或源公式兼容 gauge | 是否必有相应 gauge，或同一有效 `α,ε` 下 `0≤Θρ(t)<t`，其中 `Θρ(t)²=(1+ε)t²−τ[ρ⁻¹(t)]²`？ | C143 否定全部正幂与该固定参数严格兼容公式；任意一般 gauge 仍存在。无共同固定点的额外门现由 [C223 新模型](fixed_point_free_no_power.md#fpf-theorem) 闭合：原残差 exact-zero 与全部初律相对几何率成立，但同一锚点所有正幂局部 EB 失败；不改 C143 身份。 |

**Dependencies / Evidence。** [C14/C143/C144 的完整规范正文](compact_residual_boundaries.md)；相关 Claim 身份保持不变。上述区别不反驳 2024 Theorem 9，也不反驳把目标改成 `Ψ⁻¹(0)` 后的定义。

<a id="pnt-c144"></a>
## C144 的源条件桥与非 paracontraction 见证

保持 C144 的完整原对象：`G=[0,1]²`、`β=(δ₀+δ₁)/2`、公平 `T_j(x,y)=(x,j)`。两映射是闭凸水平线段的投影，连续且无共同固定点。

同步输出差为 `(x−x',0)`，位移差为 `(0,y−y')`，平方和等于原输入距离平方；所以源期望不等式在全部状态对成立，`α=1/2, ε=0`。

既有 C144 证明给 `μP=μ_x⊗β`、`P²=P`、`I={ν⊗β}`、`Ψ(μ)=W₂(μ_y,β)`。所有初律一步到不变律。另由同步耦合 `W₂(μP,π)≤W₂(μ,π)` 对每个 `π∈I` 成立，三角不等式和最近不变目标给 `W₂(μ,μP)≤2d(μ,I)`。因此任取同一个 `r∈(0,1)`，全部 `μ,k≥0` 满足 `W₂(μP^k,μP)≤2r^k d(μ,I)`；这不是样本路径收敛结论。

对 `0<t<1/2`，既有见证为

\[
\mu_t=\tfrac12\delta_{(1/2-t,0)}+\tfrac12\delta_{(1/2+t,1)},\quad
\bar\pi=\delta_{1/2}\otimes\beta,
\quad \Psi(\mu_t)=0,\quad d(\mu_t,I)=W_2(\mu_t,\bar\pi)=t.
\]

更新后第一坐标方差仍为 `t²`，第二坐标可与 `barπ` 完全匹配，因此 `W₂(μ_tP,barπ)=t`。非不变律到这一固定不变目标的距离没有严格下降，故 `P` 在 `W₂` 中不是 paracontraction；不能调用或否定有此额外前提的 Theorem 9。

现有 C144 到自身零集 `ZΨ={μ:μ_y=β}` 却有 `d(μ,ZΨ)=Ψ(μ)`。机制是残差漏掉坐标相关性；到 `I` 的目标识别失败，与到 `ZΨ` 的 metric subregularity 是两件事。把作者问题解读成 A 时已有否定答案，把它解读成 B/C 时必须使用各自证据。

**有限验证。** [代码与边界检查](../../code/public_problem_bridge/README.md) 用精确有理数枚举运输顶点及有限律；反算核对源/更新/极限成本。一般 `μ` 和任意不变目标的证明仍由 C144 正文与上面的耦合推导承担。

<a id="pnt-next"></a>
## 真正值得下一轮做的事

1. C223 已完成无共同固定点且 exact-zero 的正幂必要性精确版本；其自足正文、实际独立接收与有理复算可直接重建。若继续发布定位，先固定论文所回答的 A 或 C，不把“某版本已被既有资产否定”放大成所有必要性问题已解；先核 2026 Assumption 3 与 2024 非 paracontraction 段落的确切范围。
2. 独立复读 C143 的全域 Lipschitz/期望 almost-firm、全部初律速率、全部不变目标的 OT 下界、全部正幂局部失败及固定参数兼容性障碍。C144 先核到 `I` 和到 `ZΨ` 的区别，再核最近和实际极限锚的输入最优性。
3. 针对**否定必要性与固定公式兼容性**查先行，不只搜索“假零”。如果旧文已覆盖，停止首创主张，保留准确桥梁。
4. 只有在必要性边界确立后，再问可计算的识别/回耦条件怎样修复源残差；本库 [C127 回耦工具](moment_recoupling.md) 不是一般新模型的自动证明。这个修复目标是本库后续问题，不冒称作者原问题。

<a id="pnt-alternative"></a>
## 确定性主线的中期备选

Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, [2025 正式来源](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863), §5 提出把稀疏恢复中的负 `ℓ₂` 项替换为负 `ℓ_{3/2}`，留作后续研究。这是 **公开研究任务**，不是已经完整量化的未解猜想。

本库可提出的新精确目标：固定
\[
\Phi(x)=\tfrac12\|Ax-b\|^2+\eta(\|x\|_1-\|x\|_{3/2}),\quad\eta>0,
\quad F=\partial_{\mathrm{lim}}\Phi,\quad S=\operatorname{zer}F,
\]
在支持变化或退化驻点附近，能否核出完整普通 PPA 的 coverage、真残差 EB、反射模、兼容与不变窗口，并得到已有 KL/prox-regular 结果没有直接给出的速率或极限选择结论？须先固定 `A,b` 的允许类与步长，再决定量词是全部完整 resolvent 选择还是指定全局 proximal 最小解。后者仅包含于完整 `J_{λF}`，不能等同。

风险：识别支撑后的光滑非退化情形可能已被旧理论覆盖；退化驻点未必是极小点。首轮先在小维数、含秩亏的实例上核完整逆像分支和真实目标，找到值得投入的精确版本再升级。定向检索未取得同一模型与全部普通 PPA 结论的后续答案；不以未命中证明其全球未解。与推荐第一题相比，它更贴主线，但需要更多新的模型认证。

<a id="pnt-receipt"></a>
## 独立审查范围

三路代理分别读完所分配的连续背景范围，并实际审读仓库：发布/资产审查，公开来源检索，候选独立攻击。三方均指出 `I` 与 `ZΨ` 的 fatal 偷换风险，确认 B 不能被 C143 否定；查到旧 paracontraction 必要性门。根代理重新打开正式 2026/2024 刊本及 Luke–Tam §5，独立重构 C144 的源条件、统一有限步律收敛与非 paracontraction 见证，并运行精确有限验证。未逐证明重审全部仓库、未穷尽全球文献、未编写完成投稿稿。

下一轮可直接使用 [研究启动提示词](PUBLIC_NECESSITY_PROMPT.md)，也可以更换方法；当前资产不是方法白名单。
