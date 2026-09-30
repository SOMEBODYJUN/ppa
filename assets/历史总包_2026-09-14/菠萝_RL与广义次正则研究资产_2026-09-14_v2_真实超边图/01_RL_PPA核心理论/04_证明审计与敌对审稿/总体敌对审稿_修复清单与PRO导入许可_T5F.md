# T5 总体敌对审稿 F：证明可信度、贡献边界与 Pro 主张许可

日期：2026-09-08。审查性质：理论优化论文的独立预投稿审查；不是实际编辑决定，也不更改项目阶段。

## 0. 真实合稿最终复核：本节优先于历史模块判断

最终审查对象是用户后来上传的 `upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md`，**1881 行全文已读**。本节所有行号均指这份原件，SHA-256 为 `8bc3d4906f9d28ca349aad1df068eb8d5f9272d65bb731346f0949f63b9975e9`。未修改原件。历史 portfolio 仍缺失，但现在不能再用“缺失合稿”作为本轮核心审查阻断理由。

**最终总裁决仍为 REPAIRABLE；主要数学核心属于可用范围，未发现需判 UNSOUND 的核心定理。**剩余修复集中在源范围/依赖关系和引言措辞，外部新颖性仍待核；不应把它们夸大为主要收敛定理已被推翻。相反，也不能把文末第 1881 行的内部 “T5 is therefore accepted” 当作本轮独立审稿、投稿准备或 M1 已就绪的证明。

### 0.1 源审查中的修复是否进入真实合稿

| 项目 | 合稿行号 | 最终状态与证据 |
|---|---|---|
| 删除无当前证明的 tangentially nondegenerate PSM 排除 | 1550、1579 | **已修复。**前段不再宣布该排除；PSM 表格改写为退化正常测试成功。旧源模块第 55 行不再代表合稿。 |
| 逆例只排除 AP-RL，不排除 Theorem 3.1 | 1853 | **已修复。**结论明确写出这一区别。第 1566 行也明确以 AP-RL 为对象。不得把历史 CMP-M01 整体当现存错误。 |
| 引言同步使用同样严格的逆向范围 | 52 | **部分修复。**后句已明确 AP-RL；前句仍称 “the resulting certificate ... in both directions”，容易把弱接口也算入。属措辞收窄项，不再是全稿无条件 overclaim。 |
| native PSM 全零集与闭子目标的导入边界 | 18、61、1541–1546、1639–1653 | **未明确落地。**总体允许 `S⊆F⁻¹(0)`，EB 段暂令 `S=F⁻¹(0)`，native PSM 仍未明确这是全零集专用或重新假设了子目标耦合。历史 CMP-M03 的最小前导句仍缺。 |
| 移除比较公式前的内部编辑说明 | 1585 | **未落地。**仍有 “technical integration”“need not all appear in the short main text”“supplied report”。 |
| scalar/matrix 文献归属与 scalar calculus 区分 | 1577 | **未落地。**仍用 scalar 来源行笼统支持 “shift, inversion, and composition operations” 的 scalar/matrix 联合标签；建议收窄来源描述。 |
| 不暗示既有 PPA 理论漏掉 coverage | 52 | **未落地。**仍有 “closes the otherwise missing coverage ... steps”；宜写成明确本接口所需的 coverage 假设和预算，不暗示本文填补旧定理逻辑漏洞。 |
| 正常直接证明的编号 | 1335、1700、1845 | **已修复。**已统一为 Proposition 5.4；Proposition 5.2 正确用于尖锐指数。 |
| source 中 `q>0,quad` 排版 | 175 | **已修复。**合稿为正确 `q>0,\\quad K>0`。 |
| 正尺度与尖锐族参数匹配、general-gauge 包络的零连续性边界 | 641、674、826 | **已修复/更严谨。**合稿明确所用 γ、λ、ψ；更强包络反例直接用端点下界，避免把未经假设的 `ψ(t)→0` 交给 Theorem 3.3。 |

### 0.2 当前合稿需要修改的句子

| 当前 ID / 严重度 | 行号与问题 | 最小可用修复 |
|---|---|---|
| MF01 / MODERATE，Pro 导入前应修 | 1639–1653：native PSM 的目标和适用图点没有在导入处钉死；1544 的局部全零集定义与总体闭子集 convention 需衔接 | 在 1639 前加：“For this native property take `S=F⁻¹(0)`. For a smaller target, assume the same coupled inequality explicitly for that set. Suppose the inequality holds for every retained `(u,b)∈gph F`.” 在 1541 说明本段是 full-zero-set specialization。代数本身正确。 |
| MF02 / MODERATE，依赖图措辞 | 14：称两个 verification modules 被应用后产生自然类全部结论；但 863–916 的 Proposition 4.1 是纯 `(-h(z),A(z))`，不能直接覆盖 1018–1021 的 `∂σ_D(t)` 依赖；920–984 的两项残差转移也不是 1164–1182 的直接 gap 证明 | 把该句改成：“A separate structural calculation verifies both inputs for a support-function/normal-cone inclusion, using cross-active-face proximal sensitivity and a direct residual gap.” 自然类证明 1127–1162 已正确补上参数化 proximal 机制；不需重做定理。 |
| MF03 / MINOR，范围同步 | 52：`resulting certificate ... in both directions` 仍比 1853 的限定宽 | 改为 directed separation from the specified finite tests, together with a reverse obstruction specifically to AP-RL。 |
| MF04 / MINOR，贡献公平性 | 52：`closes the otherwise missing coverage ... steps` | 改为 `states the coverage hypotheses and localization budget needed for whole-orbit, finite-length, and point-convergence conclusions`。 |
| MF05 / MINOR，正文清理 | 1585：内部编辑说明未删 | 改为：“The following algebraic consequences show how each stated native inequality enters a Euclidean PPA transition, with its original domain, quantifier, and comparison set retained.” |
| MF06 / MODERATE（归属待核，而非公式错） | 1525–1533、1576–1577：Luke–Tam 参数域及 scalar/matrix 来源 scope 本轮未重取一手来源；1577 仍未采用历史来源收窄建议 | 可原样使用经过本轮证明的代数式；文献归属附原定义参数范围。1577 最小改成已归属的 scalar shift/inversion/sum calculus；不凭文献标签推出一般 matrix/composite coverage。 |
| MF07 / MAJOR（外部证据，不阻断内部数学使用） | 1876–1881：内部 verified/accepted 记录并不等于当前最近先行核验或新 M1 的前提 | 论文正文不携带内部 stage acceptance。Pro 明确把 publication priority、当前 open status、M1 原文 scope 当独立待核项。 |

没有找到“源中的主要数学修复正确，但合稿把正确公式重新改错”的实质例子；本轮真正未落地项是上表列出的作用域和依赖说明。不能为满足敌对审查形式而把已修复的重大问题重新列成当前错误。

### 0.3 合稿哪些部分可原样给 Pro

“原样”指整段假设、结论、证明及限制一起使用；不是抽掉限定后只复制结论。

| 合稿位置 | 许可 |
|---|---|
| 59–192，尤其 106–148 | 定义、耦合 Minty 等价、AP/移动投影/固定锚点/轨道量词和 coverage 分离，可原样使用。 |
| 194–317 | Theorem 3.1 与非循环轨道证明可原样使用。 |
| 319–429 | 幂率、正半径、线性端点可原样使用；不加入实际收敛必要性。 |
| 431–515 | 精确 scalar relaxation 和 limsup 证明可原样使用；exact 限于该松弛。 |
| 517–706 | 固定 λ₀ 的 attainability、c=1 边界和两类率可原样使用。 |
| 708–843 | 退化剪切、固定邻域位置无关 gauge 障碍及局部轨道可原样使用。 |
| 847–984 | 两个独立模块可按各自准确结构和前提使用；不能当一般 nontriangular coverage/EB 生产器。 |
| 986–1236 | 自然类完整逆、参数化 proximal 估计、直接 gap EB、尖锐指数可原样使用。 |
| 1238–1418 | 两尺度证书与无 margin 的更强正常分块证明可原样使用，二者须并列。 |
| 1420–1517 | 指定 ray、y₀ 范围、聚合/距离/点误差区别均保留时，disk 公式可原样使用。 |
| 1587–1635 | scalar semimonotone 与 weak-Minty 代数可原样使用，保留最近点、符号、分母条件；文献归属另核。 |
| 1637–1653 | 先按 MF01 固定 S 和全称图点作用域，再给 Pro；不是代数否决。 |
| 1655–1836 | 两个 scoped separation 命题可原样使用；排除对象仅为所列测试/AP-RL。 |
| 1851–1853 | 已修复的最终贡献边界可原样作为 Pro 定位约束。 |
| 1–54、1521–1585、1857–1881 | 摘要/引言/外部比较/内部 acceptance 不宜整体无条件导入；先按 MF01–MF07 筛选。 |

M1 闸门仍见第 7 节，且现在有合稿直接证据：**863 行是正常 inverse 完整性假设；894–903 行只是把这个假设经三角消元传给 G。**把它套到 M1 的循环联立图而未独立证明正常/全局 inverse，会把待证的 `τ∈Λ` 放进前提，构成循环。**984 行明说残差模块不证明 inverse 覆盖。**它们绝不能被当成 M1 既定事实。

## 1. 裁决与来源边界

**总裁决：REPAIRABLE。投稿准备度：NOT_READY。**

现存核心数学可以保留：本轮未找到推翻 Theorem 3.1、Corollary 3.2、精确标量渐近式、固定步长尖锐族或支撑函数/法锥自然类主要定理的反例。结论为 REPAIRABLE 而非 UNSOUND，是因为剩余问题可以通过范围与依赖说明、来源核验和编辑修复处理，不需要重建基本收敛机制。初轮模块审计确有旧 PSM 排除等风险；**真实合稿到位后的最终状态以第 0 节为准，不再把这些已修复问题算作现错。**

最初指定的两份历史文件缺失时，主线程先指定下列材料作替代审计对象；随后用户上传真实合稿，本轮又完整阅读其 1881 行，完成第 0 节的最终逐行复核。下表是同时保留的九份源模块证据：

| 材料 | 本轮用途 | 不允许推出的结论 |
|---|---|---|
| `t5_core_theorem.md`，493 行 | 定义、量词、轨道证明、幂率和线性端点 | 合稿一致性以本轮真实原件复核为准，不靠源稿推定 |
| `t5_sharpness.md`，682 行 | 标量包络、尖锐族、非必要性与一般 gauge 反例 | 不是全部算子的最优速率理论 |
| `t5_natural_class.md`，786 行 | 完整逆、跨活动面参数估计、EB、尖锐指数、直接证明 | 不是已验证工程模型或算法性能试验 |
| `t5_comparison.md`，314 行 | 原生二次信息和文献作用域的当前措辞 | 继承的引文不算本轮重新核验一手文献 |
| `t5_objections.md`，438 行 | 自包含的有限测试排除和逆例证明 | 不能把未写入的 PSM 排除自动补入 |
| `t5_full_audit.md`，508 行 | 历史验收规范与风险清单 | 文件明确是 upstream-only 审查，不是终稿通过记录 |
| `t5_merge_comparison_audit.md`，170 行 | 历史合稿的两项范围缺陷 | 历史记录本身不能决定当前状态；本轮已据真实合稿确认两项主缺陷修复 |
| `main_derivations.md`，277 行 | 原始推导背景与不得回流的宽泛表达 | “待交叉审计”材料不优先于较完整的 T5 定理 |
| `upload/01-OPEN_PROBLEMS_STRUCTURED_OPERATORS.md`，349 行 | 应用层级与 verifier 能力边界 | 不证明候选问题当前仍开放，更不证明 T5 已解决它们 |

历史 merge audit 所列 SHA-256 与新上传的当前合稿不同，不能用历史未修复状态覆盖真实文件。本轮没有生成或修改主稿原件。

## 2. 数学核心：通过了哪些敌对检查

### 2.1 定义与主定理量词

`t5_core_theorem.md` §2 至 Theorem 3.1 的框架自洽，以下限定不可在交给 Pro 时压掉：

- 有限维 Euclidean 空间、固定正步长、同一个非空闭目标集 `S ⊆ F⁻¹(0)`；闭目标保证投影存在及极限属于目标。
- 允许转换集 `𝒜` 先固定。输入覆盖是 `∀x ∃(y,v)∈𝒜(x)`；证书有效性是 `∀x ∀(y,v)∈𝒜(x) ∃p∈P_S(x)`。它们不是“存在一条好分支”或“存在一个共同锚点”。
- AP-RL 是图块上的所有图点对条件；它给 Minty 输入单射与耦合反射 Hölder 性，不给输入覆盖。图块唯一性不排除图块外的其他 resolvent 值。
- 误差界用实际输出处的普通残差。由 `r_F(y)≤‖v‖` 和 `ψ` 单调，才可传到本次所选 `v=(x−y)/λ`。
- Theorem 3.1 只需移动最近点的 solution comparison，AP-RL 是更强的生产方式，不能把二者当同一个类。

反射向量令 `a=y−p`、`b=λv` 后，`a+b=x−p`、`‖a−b‖≤ω(d)`。因此

\[
s\le B(d)=\frac{d+\omega(d)}2,\qquad
d_+\le\psi(B(d)/\lambda),\qquad
d_+^2+s^2\le\frac{d^2+\omega(d)^2}2.
\]

这里没有把单个残差选择误当最小残差，也没有把 scalar consequences 反称为向量几何的等价式。

轨道部分没有循环：在已有效输入处用 coverage 取得下一步；用现有证书控制该步及累计位移；严格预算 `dist(x⁰,X\V)>H(d₀)` 保证下一输入仍在 `V`；然后才再用 coverage。有限长度、Cauchy 性、闭目标极限均成立。一般 gauge 只需所列单调性；求和条件独立，不能由 `ω(t)→0` 代替。

### 2.2 幂率、线性端点与“尖锐”的准确对象

Corollary 3.2 的正半径式

\[
\beta(r)=\frac{K}{(2\lambda)^q}r^{\gamma q-1}(r^{1-\gamma}+L)^q
\]

在 `γq≥1` 时随 `r` 非减，故 `β(r)<1` 确实给统一距离收缩。超临界给距离超线性上界，临界正半径存在当且仅当此组成式的极限系数严格小于一。次临界只排除这条证书，不排除真实收敛。

`t5_sharpness.md` Theorem S.2 的端点证明成立：在 `t=B(d)/λ` 处，其余两个 cap 除以 `d` 均趋于无穷；`d↦t` 连续严格递增且覆盖零附近的正 `t`，因此不会漏掉 `ψ(t)/t^(1/γ)` 的 limsup 子序列。有限、零和无穷三种 limsup 都处理了。**这个 exactness 仅是 S.5 明列标量松弛的精确性。**该松弛没有保留全部距离几何或图可实现性。

固定 `λ₀` 的两分支族确实有完整单值 inverse、跨正负输入的 Hölder 控制、正确的最小残差和真实距离因子 `1/c`。在 `c=1` 时，距离不降，但任何把普适分母 `2` 改成更大数的同型充分律都会在足够小且真实有效的正尺度上误判。这足以支持“分母 2 在所列普适渐近律中不可改进”，不支持“有限半径 β 最优”“每一算子的最佳率已算出”或“步长可在同一算子中任意替换”。

`γ=1` 必须单列；`d+Ld` 的两项同阶。当前式 (3.25)/(S.15) 保留 `1+L` 并可使用能量与线性 EB 的更强组合，没有把非线性极限公式硬套到线性端点。

### 2.3 自然类的可验证性与 genuine 行为

`t5_natural_class.md` Theorem 5.1 的正面证明有实质内容：

1. 先用 strongly monotone 正常块构造完整覆盖的逆，不从 Hölder 不等式倒推 existence。
2. 再求参数化 proximal 方程，证明完整 tangential inverse，不遗漏活动面。
3. 参数估计 `‖T_s(p)−T_s′(p)‖≤λR_D|s−s′|` 包含 `s=0`，且通过子梯度单调性适用于跨 exposed faces 的比较。
4. RL 上界依赖 `R_D=max‖f−v‖`；EB 下界依赖 `d_D=dist(f,D)`。EB 下界对每一个真实输出成立，所以也控制 infimal residual。
5. 一般闭凸 `C` 只用了 `⟨n,y⟩≥0`，没有误用锥齐次性或等号。
6. 尖锐指数证明使用 `y_ε=εw∈C`、`0∈N_C(y_ε)` 和 `h_ε=(I+λM)y_ε`，输入变化为 `O(ε)`，切向位移下界为 `Ω(ε^α)`。故 `C≠{0}` 时 J、Q 在每一解输入不 calm，且最大局部 Hölder 指数确为 `α`。另一合法残差路径排除 `q′>1/α`。

这些结论比“写出一个低于 1 的指数”更强；后者对任何局部 Lipschitz 图也能做，不能作为 genuine 证据。还要分清：S.5 退化剪切在原点没有局部 pairwise Lipschitz 邻域，但它在原点可以是 point-anchored calm；不能把这个反例的 pairwise 非 Lipschitz 说成每个锚点均不 calm。自然类 Proposition 5.2 的更强不 calm 结论则有自己的下界序列。

自然类有全球输入覆盖和沿整个解集一致的 near-pair 模量，因此其 tube 证明无需捏造一个切向有限边界；一般局部 Theorem 3.1 的预算仍然必要。`δ` 是输入对距离上限，`r` 是到解集距离；整球 all-pairs 断言要保护 `2r`，不能照抄 `δ=r` 的 solution-comparison 数值。

### 2.4 非必要性与一般 gauge 障碍

S.39–S.41 的加强结论在声明的范围内成立。固定完整邻域中，非零切向锚点强制 `ω(d)≳d^γ`；在 `t=0` 的另一路径上，普通或允许转换误差界强制小 `s` 满足 `ψ(s)≥s/k`。因此同一固定邻域上的位置无关 scalar composition 比值至少为常数乘 `d^(γ−1)`，不能给严格统一收缩；`ω` 有正右极限时同样不行。

这个反例具体揭示了信息损失：聚合器把不同位置上的最坏几何与最弱残差并在一起。它不排除点依赖 gauge、块估计或原生正常方程；也不反对在 `t≠0` 的另一个局部目标附近取得更高阶 EB。实际正常递推和切向无限乘积有证明，非必要性不是只画一条形式上的距离曲线。

## 3. 顶级优化期刊视角：贡献是否站得住

### Contribution lens

最可信的贡献组合是：**带完整量词和正半径的可组合充分条件、所列信息松弛的精确渐近系数、可实现的系数边界、跨活动面的完整结构性验证、以及聚合信息损失的明确反例。**

不能把“两个证书可以独立提供，然后代入”本身当新的逻辑原理。主定理的一步代数很短，这是优点也是新颖性压力。稿件应靠尖锐对象、完整轨道结论和可追溯的结构参数承担贡献，而不是靠“compiler”“unified calculus”“首个多值非孤立理论”的名称承担贡献。

自然类的全局直接证明比 RL–EB 路线更强：`‖y_{j+1}‖≤η‖y_j‖`，切向增量可求和，不需 `R_Dη^α<d_D`。所以这个自然类证明的是一种可验证几何机制和证书比较，并未证明 RL 获得旧路线达不到的新收敛区。若论文希望主打“新算法能力”或“更宽的收敛域”，当前材料不足；若主打上述严格受限的验证定理，则可继续评估，但一手最近先行结果的 theorem-to-theorem 差异尚未完成。

### Methods lens

现存主要证明链自包含，最危险的不是计算错误，而是导入另一模块时丢失覆盖、所有输出、固定目标、残差域、正半径或测试非退化条件。没有统计实验不是本理论审查的缺陷；本轮也不凭空要求工程数值。但如果作者把计算可验证性当贡献，必须明确输入表示、待解有限优化量及输出证书，不能把难度转移到“假设完整逆已可得”后称为通用验证器。

### Communication lens

源模块曾有编号冲突；真实合稿现在已统一自然类 Proposition 5.2 的尖锐指数与 Proposition 5.4 的直接证明，并将比较 import 置于 §6.2。这些不是当前错误。仍需处理第 1585 行的编辑说明，以及从学术正文分离内部 stage dossier。

## 4. 初轮模块审计记录：最终合稿状态由第 0 节覆盖

下表保留初轮发现及其证据，便于追踪修复；F-R01/F-R02/F-R03/F-R06/F-R08 不再作为真实合稿的当前缺陷。MF01–MF07 才是最终剩余修复清单。

| ID / 严重度 | 位置和证据 | 后果 | 最小修复 | 理想修复 |
|---|---|---|---|---|
| F-R01 / 初轮 BLOCKER，现已解除 | 初轮两份指定历史文件缺失；后续用户提供真实合稿 | 初轮不能验收全文 | 已完整阅读真实合稿并给第 0 节最终判断 | 不再列为当前缺陷 |
| F-R02 / 源模块 MAJOR，合稿已修 | `t5_comparison.md` 第 55 行与 partial 表格：声称排除 tangentially nondegenerate partial tests；`t5_objections.md` Proposition 6.1 未证明它 | 源模块旧句有无证明排除风险 | 真实合稿 1550、1579 已删除；不得恢复旧句 | 如今后确需排除，独立定义具体 PSM 类、非退化条件与完整证明，另审 |
| F-R03 / MAJOR（历史缺陷及传播风险） | merge audit CMP-M01 记录缺失合稿称逆例阻止 any opposite inclusion；源逆例只造成 AP collision | 把 AP verifier 的边界误传成 Theorem 3.1 的能力边界 | 明写只排除 AP-RL，不排除较弱 transition interface | 在逆例后直接加下文计算 |
| F-R04 / MAJOR（投稿证据） | comparison 的出版物、定理号和历史优先性来自继承记录；本轮没有对应一手全文核验 | 数学代数正确不等于最近先行关系已证 | Pro 只用代数/现有证明，文献归属及新颖性标为待核 | 完成狭窄的定义域、参数范围、量词、结论对照，不需无限文献扫荡 |
| F-R05 / MODERATE | 比较正文局部令 `S=F⁻¹(0)`；核心全局允许闭子集；native PSM 用同一 S 的 INF | 对全零集成立的既有 PSM 不能默认改为任意目标子集 | 在 native import 前声明用全零集；小目标另作明确假设 | 每个 producer 输出目标与 graph/input/output scope |
| F-R06 / MODERATE | objection 的 Proposition 5.2 指直接证明，natural 模块该号指尖锐指数；比较可选节号冲突 | 看似有引用，实际指向另一命题 | 统一编号与符号，按结果名重新映射 | 合稿自动检查 theorem/definition 引用并人工对照内容 |
| F-R07 / MODERATE | structured-operator 报告 §1.3 称 G “本身不证明 coverage” | 低估已证内容，同时可能混淆假设正常覆盖与导出全算子覆盖 | 改为：G 不从裸 Hölder 假设证明正常块覆盖，但在正常块完整覆盖前提下证明三角全算子的完整覆盖 | 保留输入前提/导出输出两栏，不把自然类直接 EB 生产器与一般转移恒等式混同 |
| F-R08 / MINOR | core 第 145 行 `q>0,quad K>0` | LaTeX 排版失误 | 改为 `q>0,\\quad K>0` | 统一正文数学排版 QA |

F-R03 的直接核验：对 `F₀(t,y)={(0,y),(0,2y)}`，`λ=1`，输入 `(p,ξ)`、分支 `a∈{1,2}`，令

\[
u=(p,\xi/(1+a)),\quad v=(0,a\xi/(1+a)),\quad p_S=(p,0).
\]

则

\[
\|(u-p_S)-v\|=\frac{|1-a|}{1+a}|\xi|\le\frac13 d,
\quad d(u,S)\le\|v\|.
\]

所以 Theorem 3.1 可取 `ω(d)=d/3`、`ψ(s)=s`，得到 `Φ(d)=2d/3`，coverage 也完整。这是对“逆例排除弱主定理”的直接反证，不是术语偏好。

线性旧理论关系还必须保留一个来源核验小项：代数上 `L²=1+4τ` 完全正确，参数须满足非负平方根的相容范围；若把它归属为某篇原文定义的完整等价，必须核对该原定义允许的 `τ` 范围。不能仅凭代数式替原文扩大参数域。

## 5. Pro 可安全使用的主张白名单

以下每条都是有条件的数学许可；不能删除右栏限定，也不能由“可用”自动升格为“历史新颖性已证”。

| 编号 | 可直接使用的主张 | 必须随行的限定 |
|---|---|---|
| W01 | AP-RL 等价于图块上 Minty 单射加耦合反射 chart 的 Hölder 控制 | 固定图块；单射不等于输入覆盖；不得重选 operator value |
| W02 | 独立几何与普通 EB 可经实际步长组合 | 同一 F、S、λ、范数、允许转换与有效域；ψ 单调 |
| W03 | Theorem 3.1 在已列覆盖和边界预算下给任意允许选择的有限长度与点收敛 | 不是任意未受控 resolvent 选择；不是距离收缩本身推出点收敛 |
| W04 | 幂证书给 `γq>1` 超线性距离上界及 `γq=1` 临界正半径条件 | 使用真实有限半径 `β(r)<1`；次临界仅指本证书失效 |
| W05 | S.5 标量松弛的 limsup 为 `C_γ(L/(2λ))^(1/γ)` | exact 的对象明确为该松弛，不是完整图几何优化 |
| W06 | 普适渐近充分律的分母 2 不可增大，且由两分支族实现边界 | 冻结算子参数 λ₀，再取算法步长 λ₀；渐近与有限半径分开 |
| W07 | 支撑函数/法锥类具有完整全输入单值 resolvent 和跨活动面 RL 上界 | D 紧凸非空、f∉D、C 闭凸含 0、sym M≥aI、a,b>0、0<α<1 |
| W08 | 自然类的 `q=1/α`、`K=(bd_D)^(−1/α)` 是有效 ordinary EB | 控制最小残差；不是 strong subregularity；K 未声称最优 |
| W09 | 非平凡 C 下 J、Q 的最大局部 Hölder 指数为 α，EB 不容许更大 q | 使用下界路径；C={0} 例外；不声称 Lδ 最优 |
| W10 | 自然类 RL/EB 常数来自不同几何量 `R_D` 与 `d_D` | “独立”不是概率独立，也不是不共享任何输入数据 |
| W11 | 同一自然类有无需聚合 margin 的更强全球正常分块证明 | 必须与聚合证书并列；保留切向增量求和 |
| W12 | 固定完整邻域的退化剪切可真实收缩却无兼容幂对，甚至无所列统一 scalar-gauge composition | 位置无关、同一邻域；不排除 block/point-dependent 信息 |
| W13 | Proposition 6.1 的具体有限 full-input tests 失败，指定退化矩阵测试成功 | 固定有限参数、声明图域与正定 Cayley 条件；不扩大为全部 PSM/矩阵理论 |
| W14 | 逆例的 anchored/partial 证书成功但 AP-RL 因碰撞失败 | 明说它仍适用 Theorem 3.1 |
| W15 | 线性反射与所列二次不等式可做代数互换；保留原生权重可能保留更多信息 | 不把 graph-level 等价写为整套收敛定理等价；外部定义参数域另核 |
| W16 | disk 的指定正射线轨道有距离因子 1/8、点误差比极限 1/4；聚合距离因子 `(3/4)^(3/2)` | τ≥0、y₀>0；与局部证书对照时 y₀≤1/8；三个率不可合并 |

## 6. Pro 禁用清单

禁止把下列内容作为既定事实传入长篇写作或后续攻题：

1. “T5 已无条件通过当前独立审稿”“全部来源与新颖性已核完”“可直接投顶级期刊”。本轮有真实合稿并完成数学复核，但仍给 REPAIRABLE；第 1881 行内部验收记录不能消除 MF01–MF07 或 M1 前置义务。
2. “首个处理多值/非孤立零集/高阶 ordinary EB 的 PPA 理论”。现存比较模块自身把这些视为已有理论背景，本轮未核实任何 firstness。
3. “`γ<1` 自动 genuine”“genuine non-Lipschitz 自动不 calm”“有某个 Hölder 上界就找到了最佳指数”。这些性质不同。
4. “AP-RL 自动证明 coverage”“一条好分支推出任意选择”“关系复合可在 primal 点重选残差”。
5. “临界 `γq=1` 或系数条件是实际 PPA 收敛的必要条件”；本包有明确反例。
6. “分母 2 意味着每一算子的最优因子”“L₀ 可不加修正直接用于正半径”“改变 λ 仍是同一已算完的尖锐实例”。
7. “自然类收敛只能由 RL 证明”“RL 比正常/partial 方法快或条件更宽”；当前材料给出相反的直接对照。
8. “所有 weak-Minty、semimonotone、matrix、partial 或 almost-averaged 理论都失败”。只能使用当前明列测试及其范围。
9. “一般自然类所有 tangentially nondegenerate PSM 测试已被 Proposition 6.1 排除”。现存命题没有这项。
10. “逆碰撞例证明旧 anchored/partial 理论不包含于 Theorem 3.1”。该例可用 `ω=d/3,ψ=id` 直接接入主定理。
11. “普通零集 EB 可改为指定点强 EB”“全零集 INF 可无条件缩为任意局部零子集”“固定锚点可无条件替换成最近投影”。
12. “径向残差变换自动解决未知高阶 EB”“半代数性自动给兼容且实用的指数/常数”“存在通用高效自动 verifier”。恒等式与计算法、可计算与计算高效不是一回事。
13. 原始 `main_derivations.md` 中“通常强于”“最不损失信息的统一接口”等未经精确比较类限定的最优性宣传；其 §3 的任意锚点措辞也不得覆盖 T5 后来的 nearest-solution 限定。
14. “T5 已解决 structured-operator 候选中的 Coulomb FBF、Newton globalization、catch-up、隐式组装存在、全工程 PDE 或一般非三角 coverage 问题”。现有模型/算法作用域不匹配，候选清单也明确没有做此结论。
15. 历史数值执行、源码可复现、原始出版物 scope 或 current open status，若本轮只看到了内部文字记录，则不能升级成“已独立重跑/重查”。

建议交给 Pro 的一句话任务定位：

> 以现有自包含证明为依据撰写一项固定步长 Euclidean PPA 的定量充分证书研究，突出所列标量信息的渐近尖锐系数、完整局部轨道控制及跨活动面的结构参数验证；明确保留更强正常分块证明、AP 与弱接口差别及未核验的新颖性边界，不添加不存在的 PSM 排除或外部问题已解决结论。

## 7. M1 / SO-06：能否据此让 Pro 安全攻题

主线程已确认 M1 是 structured-operator 报告中的 SO-06，即 Alcantara–Dao–Takeda 非三角/循环 composite semimonotone inclusion 的 implicit coverage set `Λ`，不是新的编号推测。本节只审查任务交接是否安全，不声称已独立核验其原文或设计出新证明。

**交接结论：T5 safe pack 足以作为有闸门的攻题背景；不足以作为 M1 已满足假设的证明包。可以让 Pro 开始源范围冻结和有界反例/充分条件探索，不能让 Pro 从“Λ 已证”或“旧方法失败”继续推导。**

现存问题报告对 M1 的表达为

\[
\Phi_\tau(w)=(\tau A+\tau PBR+\mathcal L)^{-1}(w+\mathfrak q),
\qquad
\Lambda=\{\tau>0:\Omega^\perp\subseteq\operatorname{dom}\Phi_\tau,
\ \Phi_\tau\text{ 在 }\Omega^\perp\text{ 单值}\}.
\]

Pro 必须首先对照原文固定这套表达的全部对象、参数和范围；不能把报告的摘录当作已经齐全的定理假设。仅有上述显示式时，尚不能判断逆值空间是否有限维、全空间还是受限表示，以及单值性是否在原变量而非商空间中主张。

| T5 能安全提供什么 | 对 M1 的准确作用 | 不能替代什么 |
|---|---|---|
| “覆盖”与“无碰撞”分开 | 把 `τ∈Λ` 分成存在与唯一性两个可验收义务 | 不能从已有逆的正则估计倒推出 existence |
| 完整图块与允许输入范围 | 检查跨活动面 preimage 是否缺失或冲突 | 一个稳定分支、若干已访问 faces 或 dense/closure coverage 都不等于完整 coverage |
| 三角 normal-feedback verifier | 在正常块完整 inverse 已证时，传递到三角全算子的 inverse 与模量 | **不处理一般非三角/循环耦合；不能把 M1 待证 Λ 当作它的正常块假设** |
| 参数化 proximal 敏感度 | 对确实符合其结构的块给跨 active-face 估计 | 不自动消除双向反馈，也不自动证明所有联立方程可解 |
| Scalar RL–EB 与轨道模块 | 在 M1 的逆、相同算法/metric 和证书另行成立后，可作后续结论接口 | `q,K` 与 EB 不负责证明 Λ；原 splitting 算法不自动是本文 Euclidean PPA |
| 尖锐/非必要性反例 | 防止 Pro 把不兼容证书写成算法失败，并提醒保留 block 信息 | 不能用 T5 的剪切反例证明 M1 所有传统条件失败 |

### 给 Pro 的 M1 前置闸门

1. **原问题身份。** 读取原文 Eq. (3.7)、Theorem 3.5、§4.2 及相关附录的精确内容，固定 `A,B,P,R,ℒ,𝔮,Ω,τ` 的类型、假设、输入域和 intended algorithm。若缺原文，先取得当前任务范围内可访问材料，不自补假设。
2. **既有充分条件基线。** 根据现存报告，lower-triangular Lemmas 4.4–4.5 与 Appendix B 的变换最大单调路径是正面基线；其精确范围须一手核验。新条件若只是三角消元、同一个变换后的最大单调性或已含于原条件，必须承认重述/特例，不能称 M1 突破。
3. **先定证明对象。** 第一阶段可只研究 `τ∈Λ` 的可检查结构充分条件或合法 collision/no-coverage 反证；不要求同时产生 `γ,L,q,K`，更不人为强制 `γ<1`。覆盖问题本身不依赖幂律临界匹配。
4. **同一对象比较。** 如改变量、metric、预条件或 quotient space，应证明与原目标的精确对应；不能得到另一个算法/另一个逆的良定性后宣称原 M1 已解决。
5. **结果验收。** 充分条件必须给输入表示、全称量词、正步长域、存在证明、唯一性证明和原基线比较；反例必须给原假设下的同一输入及两个不同合法 preimages，或给一个确实未被覆盖的原输入。采样和单支导数不是全域证书。

### M1 专用禁用主张

- “T5 Proposition 4.1 已经证明一般 `τ∈Λ`。”该命题既有限定结构，也把正常块 inverse 的完整性作为前提。
- “M1 主定理只差 EB，因此接入 T5 的 q/K 即可。”这是把 coverage 义务偷换成残差义务。
- “非三角或 cyclic 就超出所有旧理论。”原文的变换、最大单调、Schur/小耦合等正面范围必须逐个按实际假设比较，不能由结构标签排除。
- “必须找到 genuine `γ<1` 才算完成 M1。”Λ 的定义是 coverage 与单值性；若 γ=1 的原生结构条件新且适用，也可能推进这个精确子题，但仍须区别新结果与已知特例。
- “局部单值逆、闭包中的 range 或正常商空间中的唯一性等于原 `Ω⊥` 上完整覆盖和单值性。”每一个转换都需原文范围与证明。
- “T5 的普适系数 2 改进原 composite splitting 的收敛阈值。”尚无相同算法、同一 transition、norm 和 residual 的桥梁。
- “现有自然类给了 M1 的非三角实例。”当前自然类是单向三角结构，不能改名成循环模型。
- “SO-06 是公认尚未解决的一般猜想”或“解决 Λ 就解决整个 splitting/工程问题”。现有证据把它定位为 O2 验证瓶颈，研究结论必须用所证子类与任务层级命名。

安全任务标题可以是：“在原文数据与比较范围冻结后，为 M1 的指定非三角子类寻找完整输入覆盖与无碰撞的可检查充分条件，允许返回严格反例或证明已被既有理论覆盖；T5 仅作为后续模量/轨道接口，不作为待证 Λ 的来源。”

## 8. 修复优先级、证据状态与质量检查

最终合稿优先处理 MF01/MF02 的目标与依赖说明，再同步引言/比较措辞并删除内部编辑文字。历史 F-R02/F-R03 已修，不需重复修复。原件已完成本轮数学审查，一手最近先行比较仍是独立投稿证据任务；没有必要为了这些修复新增数值实验或改变算法。

- `VERIFIED_USER_MATERIAL`：上述九份源文件和后来上传的 1881 行真实合稿均已完整阅读；历史 portfolio 仍未提供。
- `AI_INFERENCE`：本审稿的证明复核、范围反证、贡献评价、许可清单及修复严重度。
- `EXECUTED_LOCAL`：只读文件列表/行数/定位/哈希检查，以及本报告文件创建。
- `PENDING_VERIFICATION`：一手文献的完整参数范围、最近先行差异和新颖性；开放问题当前状态；M1 原文身份与既有充分条件的完整作用域。
- `NOT_EXECUTED`：新文献检索、历史数值重跑、形式化证明助手检查、工程验证、图形生成和投稿。

质量检查：主定理的 `∀/∃` 顺序、闭目标、输出残差方向、gauge 域、循环延续风险、临界等号、正半径、γ=1 端点、尖锐对象、跨活动面、一般 C 与 C={0}、Q/R 速率、普通/强 EB、AP/锚定/INF 范围及成功旧路线均已逐项检查。未改写任何源模块或权威状态。

### 本轮快照

```text
deed144204d7b42a38198d5c8f9204c0a60c8f5a75cfeb952b654b4a9033c2c6  t5_core_theorem.md
b65605915de29c7ae704301fefecd58c1ec3ceb338e48dbfadb00f7a8af0e9dc  t5_sharpness.md
9e64e1ee061ef94dba7f3a73b19bcb18e726d101edc275b76e6764a03df503bf  t5_comparison.md
3fe4b2def3d7221dc21ff6346e9e45b72e1e7fdd8038b060f86301a2bb778af0  t5_natural_class.md
7371f444a82fb691a0ef8faa7c2b0a8d408a397b19242965f4f31b81a01a4abf  t5_objections.md
ab47071ce98cfa35c3af3b4044eb7e3f3e604b9d67715e0cbf9b847e1703e498  t5_full_audit.md
bb1ce5865cf164d091c2a6dc34b737cedd0f6e7d20b8aa5dab27d714be6b826e  t5_merge_comparison_audit.md
88beb6be932bae4f9c4af78c864b5b1dc8814e4cc86ff4bc13c28d03e7337369  main_derivations.md
646ab1a29819c8b6a96dff9508082e1e264632226241a1efe7c1366d555fad3b  upload/01-OPEN_PROBLEMS_STRUCTURED_OPERATORS.md
```

## 9. SCI-Skills Expert Contract 1.0

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review
project_id: null
paper_family: null
stage_id: null
task_id: null
task_status: COMPLETE
inputs_reviewed:
  - t5_core_theorem.md, complete
  - t5_sharpness.md, complete
  - t5_comparison.md, complete
  - t5_natural_class.md, complete
  - t5_objections.md, complete
  - t5_full_audit.md, complete
  - t5_merge_comparison_audit.md, complete
  - main_derivations.md, complete
  - upload/01-OPEN_PROBLEMS_STRUCTURED_OPERATORS.md, complete
  - Parent clarification: M1 is SO-06, implicit coverage set Lambda for nontriangular/cyclic composite semimonotone inclusion
  - upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md, all 1881 lines, SHA-256 8bc3d4906f9d28ca349aad1df068eb8d5f9272d65bb731346f0949f63b9975e9
outputs:
  - /workspace/scratch/01cfe9a021bd/T5_AUDIT_F_REFEREE.md
evidence_status:
  - VERIFIED_USER_MATERIAL: all nine authorized substitute inputs and the subsequently uploaded actual manuscript read fully
  - AI_INFERENCE: independent algebra, quantifier audit, scope refutations, contribution assessment
  - EXECUTED_LOCAL: read-only locator and hash checks, report creation
  - PENDING_VERIFICATION: primary-source parameter scopes, novelty, current open-problem status and complete native M1 scope
  - NOT_EXECUTED: new literature retrieval, numerical rerun, formal proof checking, submission
assumptions:
  - The parent authorized nine modules initially and later requested final audit of the actual uploaded manuscript
  - Direct-task identifiers were not supplied as schema fields and are therefore null
  - Mathematical statements retain all printed domain, target, metric, stepsize and selection hypotheses
author_input_needed:
  - M1 original-source scope and intended restricted target must be frozen before a new theorem claim
manual_actions: []
quality_checks:
  - All-pairs and moving-projection quantifiers separated
  - Coverage, gauge domains, output residual and noncircular trajectory induction checked
  - Critical scalar asymptotics, positive radius, linear endpoint and attainability checked
  - Full natural-class inverse, parameterized prox and legal sharpness paths checked
  - Stronger normal-block proof retained
  - Historical unsupported PSM exclusion and reverse-interface overreach confirmed repaired in actual manuscript
  - Remaining native-target scope and producer-dependency wording located by actual manuscript line numbers
  - Source inheritance not promoted to primary-source verification
  - Pro whitelist and forbidden claims explicitly supplied
  - M1 handoff readiness assessed separately from mathematical solution readiness
  - Circular use of an assumed complete inverse to prove Lambda explicitly prohibited
conflicts:
  - conflict_id: MF01
    conflict_type: target_scope_ambiguity
    claim: native PSM import retains the intended comparison set
    source_or_locator: actual manuscript lines 18, 61, 1541-1546 and 1639-1653
    competing_interpretations:
      - native full-zero-set property
      - global closed-zero-subset convention silently carried into native import
    recommended_resolution: explicitly fix the native full zero set or independently assume the same coupled property for the smaller target
  - conflict_id: MF02
    conflict_type: producer_dependency_ambiguity
    claim: the two independent modules are applied to yield the full support-function natural class
    source_or_locator: actual manuscript line 14 versus Proposition 4.1 and the separate Theorem 5.1 proof
    competing_interpretations:
      - separate structural verification of the two certificate inputs
      - direct application of a pure feedback theorem to a tangentially dependent subdifferential
    recommended_resolution: say that the natural class independently verifies both inputs using its own cross-active-face proximal sensitivity and direct residual gap
conflict_resolution_status: UNRESOLVED
merge_permission: orchestrator_only
recommended_next_action: Issue a bounded M1 task brief carrying this whitelist and requiring original-source scope and baseline freezing before any new proof claim
stage_acceptance_recommendation: REPAIR
```

唯一主要下一步：把上述白名单和禁用项写入有界 M1 任务书，让 Pro 先冻结原文作用域与既有正面基线，再开始新证明主张。
