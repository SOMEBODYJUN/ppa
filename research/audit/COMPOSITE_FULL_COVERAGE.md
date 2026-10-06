# C11 复合模块：完整内容枚举与逐项去向

<a id="composite-full"></a>
## 冻结来源与物理范围

本批处理现有原件 `history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/C11复合次正则_定量模块与未解边界.md`。它有 **420 个物理 LF 行**，末尾 LF、无 CR，SHA-256 为 `d9f9e5c53c41d827a7fd25250fbd5cbee3c3f2d08c41d245dc9b8f552b084619`。本批逐字节复核它与现有 `RL_T4_CODEX_HANDOFF_2026-09-09.zip!/ATTACK_C11_COMPOSITE_GENERALIZED_SUBREGULARITY.md` 相同；这是同一证据内容的两个来源位置，不能计作两份独立证明。未改动或新增历史原件。

| 断言表 | LF 范围（含端点） | 记录数 | 内容 |
| --- | --- | ---: | --- |
| [COMPOSITE_CORE_UNITS.tsv](COMPOSITE_CORE_UNITS.tsv) | 1–311；338–420 | 264 | §1–§7 定义、条件、定理、证明、实例、障碍；§9–§12 状态、开放目标、数值报告与合同字段 |
| [C11_SECTION8_UNITS.tsv](C11_SECTION8_UNITS.tsv) | 312–337 | 72 | 保留已有逐条文献接口和历史检索身份 |

两表并集恰为 **LF1–420**。核心表有219个非结构记录和45个组织记录；后者仅含标题、空行、表头、分隔或代码围栏，每个未被实质记录覆盖的行都逐行检查。标题上的 `PROJECT_PROOF` 状态另有实质记录，未借“组织”隐藏断言。相同源行包含多个独立数学/证据/状态断言时，行范围可以重叠。336条记录不是336个定理，也不是全库来源清洗率。

核心表处置为121 rewritten、16 duplicate、7 superseded、45 deferred、75 nonmathematical；§8原表为43 rewritten、19 deferred、10 nonmathematical。两个表的 deferred 都有本项精确义务，没有用整节未读 catch-all 替代枚举。组织、价值判断和待证目标均不计为已证数学。

## 符号与调用域

| 符号 | 本规范固定含义 | 不自动获得的替换 |
| --- | --- | --- |
| `Γ` | 完整 limiting 次梯度零集 `zer ∂f` | 任意选定的单点或较小零集 |
| `Θ₂` | stationary 且每个方向的实际 `d²f(x\|0)` 非负 | Clarke Hessian 的“每个 PSD”或“存在 PSD” |
| `S` | CS-EB 中的完整 preimage `c^{-1}(argmin φ)` | 把单条轨道极限当作误差界目标 |
| `T` | C165 的另一个闭 stationary 子目标，与 `S` 在同一 `B_R` 内相等 | 删去 `T⊂Γ` 后只保留包含关系 |
| `r_F(x)` | 对完整 `F(x)` 纤维取 inf 的真实残差 | 某个选定乘子、实际步残差或 prox residual 的无条件等号 |
| `Ψφ, ΨF` | 非降、零处为零且趋零的残差侧 gauge | LMZ 原距离侧 gauge 未验反演就同名代入 |
| `A, B` | `A=Dc(barx)`，`B=A†` | `B` 不是目标球；证明的切片是 `x+ran Aᵀ` |
| `β, h` | 内层导数 Lipschitz 常数与 `h=βM` | 不把外层 `η` 误写成 RL 指数 |
| `γ, q` | 此模块 RL 指数固定1；幂 EB 指数 `q=1/a` | 真正 `γ<1` 的独立新机制 |
| 局部近端输出 | 基点在同一 `B_R` 的唯一完整局部纤维，输入范围和轨道预算另明写 | 完整 resolvent 在球外无其它输出 |

## 自足规范数学及本次补足

[C34–C37 的原稳定范围](../canonical/composite_subregularity.md#cs-transfer)保持原有身份：有限连续目标转移、满行秩有限凸复合真残差、局部全部图点 RL 与 coverage、曲面幂/非幂模型。满行秩、全部乘子界、最近零点同域、初始距离和位置预算都是实际前件，没有由抽象“链式规则”替代。

本次新增三个独立规范身份：

- [C161 / CS-TRANSFER-LSC](../canonical/composite_subregularity.md#cs-transfer-lsc)：proper lsc 扩展实值函数、有限值基点、局部极小、弱分离和 `local-min⊂S⊂Γ` 下，同一 `B_{R/4}` 三个完整集合距离相等。证明不需要投影或集合闭性；不把 C34-v1 静默扩大，也不授予扩展实值复合的链式规则或近端覆盖。
- [C162 / CS-CLARKE](../canonical/composite_subregularity.md#cs-clarke)：完整计算 `g'`、`g''`、局部 Lipschitz、Clarke 聚值区间及 `d²g`、`d²(−g)`，分别排除“全部 PSD”和“存在 PSD”替代。定义的 C²/Taylor 退化也已独立写出。
- [C165 / CS-LOCAL-TARGET](../canonical/composite_subregularity.md#cs-local-target)：在 C35 的同一原生数据上替换为闭 `T⊂Γ` 且保留局部完整零集；证明距离相等、`r≤R/4`、最近点同图以及 C36 留域沿用。

另补 [Lipschitz 障碍](../canonical/composite_subregularity.md#cs-lipschitz-obstruction)的同域投影证明，以及非幂外层的积分、逆 gauge 渐近、实际竖线输出存在唯一性和任意已定位非终止轨道的距离比趋零。这些细节支持原 C37 的量词，不声称新全局算法结果。

§5.3 真实多值尖点由现有 [C40](../topics/composite_regular/cusp_identification.md#ci-identify)承接，其跳跃残差识别依赖实际局部步。§6.2 由现有 [C41](../topics/composite_regular/oscillating_target.md#ot-maxima)承接，保留完整 `Θ₂` 和严格局部极大序列。

## 精确修复与待核门

源 LF72 的“mere containment 不足”需要条件辨析：保留 `T⊂Γ` 且已知 `Γ∩B_R=S∩B_R` 时，`S∩B_R⊂T` 本身已强迫局部相等；只有删除 stationary 子集门后单向包含才不足。CSC-U215 把这一原句单独 superseded，C165 不保留过强否定。

源 LF274–277 的“derivative sign”有变量歧义：`H(u)` 是 `g'(u)` 的符号，`u=x^{-4}` 在正半轴有 `u'<0`，所以不是 `f'(x)` 的符号。现行 C41 使用正确链式式 `f''=g''(u)(u')²` 并保留极大结论；这项修复单独记账，不把正确反例整体降为未证。几何修复迭代先验自映射、闭球乘子预算以及打包 `PROVED` 标签也分别 superseded。

§1 LMZ 的日期/DOI/v1身份沿用现有明确一手卡。源稿对 Def3.1、Lemma3.6、Prop6.3、Th6.4、Cor6.5 和 §8 未来方向的精确归属各留独立文献义务；已读 §4 卡不扩大成这些条目已核。§7 每种工具的正向调用须补确切定理和前件；其作用域边界不被改写成否定一切额外假设定理的普遍反例。§8既有72项保持原身份及全文、刊本、公式、历史行为和优先权边界。

§11 的成功执行、六个数值、无 underflow、检查项目和环境报告逐项保留 `source-report/deferred`；本轮没有复跑历史脚本。数学公式和渐近有自足证明，既不依赖旧浮点输出，也不认证旧执行行为。§12的独立 agent/数学审计报告同样需要历史产物；合同里技能、merge 和工作流字段只是来源内容，不作为本轮指令。

§9 的期刊定位属于研究判断；§10 的秩亏、活动变化、完整原生乘子验证、可计算同目标 gauge 和最近文献对照仍是具体未证目标。完成本文件内容枚举不等于解决公开扩展问题、关闭全部先行性或完成全库清洗。
