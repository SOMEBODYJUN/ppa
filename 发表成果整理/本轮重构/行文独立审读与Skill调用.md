# 行文独立审读与 Skill 调用

本稿已经把“到零集的距离趋零”和“收敛到零集中的一点”分开证明。主线可由首次阅读者重构：先取得距离收缩和步长界，再用有限前缀预算保证局部迭代继续存在，最后由可和步长得到点收敛。受检一手引用中未发现明确误引。并行修订已消除本次指出的主要接口歧义；剩余建议以阅读次序和局部简化为主。本报告不作新颖性或投稿就绪认证。

## 1. 触发方式、独立性与实际加载

- 任务显式指定 `/workspace/scratch/15cd717a5884/ppa/.agents/skills/academic-writing-skills`；`ppa/AGENTS.md` 也要求数学论文与审读使用该单一 Skill。这里实测的是**显式加载路径**，不是只按名称模仿。
- 已实际读取 `AGENTS.md`、`RESEARCH_PROTOCOL.md`、指定 `SKILL.md`，以及 `references/mathematics.md`、`mathematical-exposition.md`。还按所需模式读取了 prose-and-citation-editing、universal-integrity、introduction-and-study-context、execution-and-acceptance、lifecycle-and-routing、state-and-authority、reviewer-red-team-and-release 与 banned_words。
- 数学对象以主稿和 `research/foundations.md` D01–D04、`research/NOTATION_CONTRACT.md` 的相关定义为准；未把旧来源报告当作证明。
- 本代理未读本轮内部报告、预计答案、Skill 测试案例或其他代理的审读结果。收到的并行改稿通知只用于复读实际变动段落；原读稿、后改稿和本代理提出的建议在下面分开记录。
- 三项实际任务分别按中文局部润色、英文编辑、命题审查模式执行。它们共享已加载的 Skill，但各自以本项原文为输入，各自给出结果与理由；没有把另一任务的输出当作本项证明。
- **原生 CLI 的隐式触发未测。** 本轮没有启动三个原生 CLI 会话，也未验证未显式点名时 Skill 是否会由运行器自动选择；不能将本轮显式加载结果宣称为自动触发通过。

实际读取的核心文件 SHA256：

| Skill 文件 | SHA256 |
| --- | --- |
| SKILL.md | `a28dadaa99b492326177c2ccb645b49fe91ae2086e1a81e873e008bb297eeb8b` |
| references/mathematics.md | `356feacf46c916bff6c84d88ccc9ef4c0466caa8080ba5e2c46f83eba63e1587` |
| references/mathematical-exposition.md | `9dcbf4703caaa1fcc9685abd496b7922c3668ad17ccaf12248c09b98c16eb7a5` |

## 2. 审读版本

A 是本代理开始冷读时保存的源码快照；B 是收到冻结通知后复读变动段落、重新计算的源码快照。`main.tex` 通过 `theorem_spine.tex` 嵌套载入 `preliminaries.tex`，因此前置收敛判定属于实际主稿范围。

集合指纹采用：按相对路径排序，将每项的 `路径 + NUL + SHA256 + 换行` 连接后再计算 SHA256。A 的集合指纹为 `3673dc6860b859d649581efea771464a036391764e2878ffdb75f21c3188d684`；B 为 `eade893f7b8b437d138ec39fdea218ec5d2a29b2d62ad909295e952c560218bf`。以下逐文件 SHA 是报告结论的版本边界；后续修改不自动属于本报告已审内容。

| 文件（相对于 RLEB） | 初读 SHA256（A） | 最后复核 SHA256（B） |
| --- | --- | --- |
| main.tex | `59747c041d4657380abbfb2de43c4162be9083cafcfc94f6b21b05d087f71faf` | `59747c041d4657380abbfb2de43c4162be9083cafcfc94f6b21b05d087f71faf` |
| sections/conclusion.tex | `ef79bfbee07be1a7c2ad94f9afd58e9b3453b600e99c1a7c284dfe35031cfb53` | `ef79bfbee07be1a7c2ad94f9afd58e9b3453b600e99c1a7c284dfe35031cfb53` |
| sections/frontmatter.tex | `bc5e7f8b82cfb50c7c0e2360db909598aa32a66189fd759305ba7697c263c3f9` | `29084df7a073ddddc4a484baf53fc5d93afeebb6fadd7d7036db2ee5505892fa` |
| sections/gppa_extension.tex | `d1e1f066dcb5b747f055f410644c55c3a88d990f7a785a978348c93178aa0f18` | `4d7fcc0c9d1697eb6c253eb2e16fd1d4dcf65ebaa9d90f93948767d8ec91f4fc` |
| sections/preliminaries.tex | `72056c451dfa995ecbd517b444083bb16e139eb1acc7bb2864231fa433bc7537` | `8c5f48b247860fcdcf234c8690b2390c9fef718007697cc35aa11d082110e473` |
| sections/related_work.tex | `403609aa1ef7ca572263d9a749ef18d357cc5f9aaefa6806aa019fa0e7c6d248` | `7d3ae4ecc49218f6a86698bdfd01124e849d6cdc1cf956a38619bddb441e511f` |
| sections/theorem_spine.tex | `19b5e58045d60a035fe20789b17009cf3aed4c881d54e073cb3accabf0be41be` | `490fff971ccedd189ba10b2aac127a0c9d52e864253667c4e195fa2a61746a22` |
| sections/topological_obstruction.tex | `5c37cd7d4bb43d9a1735f2d6224c4be0cd8b8d90fddaa29d16be1af88782af40` | `105e5a46ae0536872e9b2c234041725c3bc140fa7c6e05b464d31140741540ab` |
| sections/verification_example.tex | `274beb7e7faccefb5e5cc5bd56ca54ee2abe6382285072d8efcd5ae09c41f85a` | `dadeae2eb7859c7d332c1f21549cfb829bfae17d812fba374857458fa409ab17` |
| references.bib | `e79ba00d8f0f4f2387b74ac580aabda0f8d95d09805f934c8c7033996f720d8f` | `e79ba00d8f0f4f2387b74ac580aabda0f8d95d09805f934c8c7033996f720d8f` |

## 3. 首次阅读者能否沿主线前进

| 衔接 | 具体观察 | 结论与边界 |
| --- | --- | --- |
| 引言文献 → 问题 | 先给极大单调与次正则背景，再分近端几何和真输出误差界；问题落在非 Lipschitz 位移能否可和。 | 论题可识别，不是按年份列文献。没有把有限检索升级为“首个”或“全面优于已有理论”。 |
| 问题 → 前置收敛判定 | preliminaries 的 Cauchy 性、闭性和有限长度各有作用；距离–长度引理明确以已存在的无限序列为对象。 | 不能用距离趋零替代点收敛，也不能用该引理供应局部下一步存在。主稿守住了这两处边界。 |
| 前置判定 → 主定理 | 一步反射估计给出 \(s\le(d+Ld^\gamma)/2\)；真残差方向是 \(r_F(x^+)\le s/\lambda\)；B4 只在同一评价窗使用。 | 残差没有被选定图值取代。有限前缀归纳先完成无限延拓，之后才调用可和步长，逻辑次序正确。 |
| 主定理 → 三角例 | 完整近端公式同时给出覆盖和唯一性；真残差、锐指数、闭式轨道各自验证。 | 例子确实承担“非 Lipschitz 切向漂移仍可和”的工作。没有把局部定理的上界 \(\kappa=3/4\) 写成实际法向因子 \(1/2\)。 |
| 三角例 → GPPA | 同一三角对象的正对角核计算、非对角正定核反例、退化核反例逐步说明为何不能只靠“正定”或核坐标收敛。 | 固定 SPD 推论由完整关系、度量残差和最近锚的 \(Q\) 变换支持；对一般核没有偷移物理点有限长度结论。 |
| 局部收敛 → 拓扑 | 先明确完整全域单值映射、全尺度次线性反射界、完整紧流形零集，再使用管邻域指数。 | 此处是加假设后的全域限制，不是三角零线例的推论。全局吸引再额外产生回缩，区别于局部吸引。 |
| 新增补偿模型 → SPD 欧拉段 | \(C=P_B(2x)\) 有界且 2-Lipschitz；\(\min\{2\delta,2\}\le2\delta^\gamma\)。径向半径变换严格增加且满射，固定点为圆与原点。 | 圆附近法向距离减半，原点确在吸引管之外。该例解释零簇补偿，并非取代前面的非 Lipschitz 机制例。SPD 段最终已补齐完整紧无边界流形前提。 |

## 4. 具体行文发现及最后状态

严重程度仅针对所列问题；“AI 式”在这里指可观察的流程句、重复预告或空泛指代，不推断写作来源。

| 编号 | 定位 | 初读发现或复核发现 | B 版本状态 |
| --- | --- | --- | --- |
| E1（S2，semantic，confirmed） | frontmatter，引言首段 | “较弱的近端连续性”容易被理解为输入之间的 Hölder 连续性；主定理只要求最近零点锚比较，并允许严格多值。 | 已改“较弱的近端几何控制”，核心歧义解决。若进一步简化，可将前一句的“Hölder 型控制”也直接说成“相对最近零点的 Hölder 阶反射位移控制”。 |
| E2（S2，section，confirmed） | theorem_spine 的 RL 定义/\(J\) 侧引理与 selection-RLEB | 冷读先见全对 RL 保证单值，稍后才见主定理允许多值。初读需回头确认两项条件不同。 | 数学区分已经写明，无效性问题不存在。可选行文调整：把全对 RL 定义与 \(J\) 侧引理放到“全对图块的充分验证条件”，先讲主定理真正使用的零点锚反射比较。无需为这项建议改数学范围。 |
| E3（S1，surface，confirmed） | verification_example 开头三句 | 第一、二句重复法向/切向分工，第三句再次预告结论。 | 仍可作任务 1 所示的局部压缩；不需要更换例子。 |
| E4（S2，surface，confirmed） | verification_example，锐性证明后 | 前一句用 \(q>2\) 作反证参数，下一段直接写 \(\gamma q=1\)，没有重置到锐幂次 2。并非“q 从未出现”。 | 已明确“取本例的锐误差界幂次 q=2”，解决；最大指数也已定位于零线任一点的邻域。 |
| E5（S3，semantic，confirmed） | gppa_extension，压缩后的 SPD 推论 | 中间稿只替换范数、距离、最近点，未明确主定理 B2 的内积也须替换。字面条件与 \(Q\) 证明不一致。 | B 版本已定义 \(\langle\cdot,\cdot\rangle_M\)，明确替换内积并给出 B2 的 M 反射范数式。该问题解决；不是正定核定理被反驳。 |
| E6（S1，surface，confirmed） | theorem_spine 证明末段；GPPA 推论 | 主定理重复前置引理的 Cauchy/尾和证明；GPPA 重列 B1–B4 后又逐项变换。 | 已保留承重的有限前缀归纳，随后引用前置引理；SPD 条件改为精确度量替换，完整 \(Q\) 证明保留。重复明显减少。 |
| E7（S1，surface，confirmed） | verification_example 的计算后；related_work 后半 | “误差界前件及其同窗兼容”“不需要在此重复”“固定正定度量合同”是流程或项目用语。 | 分别改为明确的 B3–B4、具体推论引用和度量条件，解决。 |
| E8（S2，section，confirmed） | topological_obstruction，指数归一化处及 SPD 段 | ENR 首次出现无释义；新增 SPD 欧拉段一度只重提映射与界，完整紧流形前提需跨段补回。 | B 版本已解释 ENR，SPD 段已重提非空紧 C² 无边界嵌入流形和完整零集。范围歧义解决。 |
| E9（S1，surface，confirmed） | related_work，指定 Lipschitz/二次型证书 | “指定…二次型条件的失效”没有就近点出哪项证书，首次读者可能误听成所有二次型理论都失效。 | 现有下一句已明确不排除其他区域/锚/更新，因而不是广泛排除结论。仍可将“二次型条件”直接定位为“γ=1 的全对 RL 估计”，让比较可在本文公式中追查。 |
| E10（S1，surface，confirmed） | frontmatter、preliminaries、theorem_spine 证明收尾 | “下面先…再…”、“没有预先假设整条轨道留域”等反复提醒读者同一证明顺序。 | 可只在引言交代一次路线，在有限前缀证明处保留具体数学。实际归纳和严格预算不可删除；此项是可选简化，不是要求消灭必要术语重复。 |

引言末段对固定度量与全域拓扑各有一句预告，之后的路线表说明其位置；这属于有作用的导航。结论的三个结果与主稿对应，没有发现新增结论。将 GPPA 与拓扑一并放入论文的价值判断仍由作者决定，本次不把篇章偏好当作数学障碍。

## 5. 引用核查：已查什么，未查什么

检索日期：2026-10-11。技术核查只用原论文、作者稿、出版社原文或作者书稿。下列“核对”不等于验证全文所有引文或文献新颖性。

| 原文与主稿用途 | 实际核对位置及结果 |
| --- | --- |
| [Luke–Tam，2025 正式论文](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863) | Definition 2 的 λF 次单调不等式；Lemma 2 的线性距离收缩＋线性步界；Assumption 2(d)(ii) 的截断值域覆盖；Theorem 2 的适当局部选择。主稿对应识别、非线性步界推广和 B1 覆盖映射一致，未把该文定理整套假设省成仅有覆盖。 |
| [Leventhal 作者预印本](https://arxiv.org/pdf/0902.4200) | Theorem 3.1 假设极大单调、在零点处度量次正则、初值足够近，给出零集距离线性估计。引言用途一致；不把其中距离结论单独当作任意非单调轨道的点收敛。 |
| [Combettes–Pennanen 作者稿](https://pcombet.math.ncsu.edu/sicon3.pdf) | Lemma 2.4 的松弛近端/正则化关系；Theorem 3.1 的非精确松弛负余单调迭代。引言描述的研究途径和更新类型相符。 |
| [Evens 等，2305.03605v2](https://arxiv.org/pdf/2305.03605v2) | Definition 2.1 为指定零点集合的 oblique weak Minty；Definition 4.1 为带符号双参数半单调性；Theorem 2.4(iii),(v) 区分影子序列与附加条件下完整状态收敛。主稿参数切片和边界叙述对应。 |
| [Benjamin–Gottlieb 作者稿](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf) | §2.1 的 (2.1.1) 局部化、(2.1.4) 紧 ENR 归一化、(2.1.6) 交换性，支持管内/环境指数的桥。主稿不是借论文标题代替所需性质。 |
| [Hatcher 作者书稿](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) | Theorem 3.26 给闭连通流形最高维模二同调非零；主稿的可缩性反证可逐分支使用。Example 2.42 的实射影空间胞腔/同调计算支持 RP² 的 χ=1 且不可缩。编号匹配。 |
| [Luke–Thao–Tam 作者摘要](https://arxiv.org/abs/1605.05725)、[Kruger 作者摘要](https://arxiv.org/abs/1502.06159)、[Mordukhovich–Ouyang 作者摘要](https://arxiv.org/abs/1507.04825)、[Li–Mordukhovich 作者稿](https://web.maths.unsw.edu.au/~gyli/papers/lm-subreg12final.pdf) | 对应“扩张集值固定点框架”“一般非线性次正则”“任意正阶”“Hölder 次正则”的概括有原文/摘要支持。没有在本文从这些来源直接导入一个未逐项映射的具体收敛定理。摘要级核查不是这些论文定理的完整复核。 |
| [Rockafellar 出版社页](https://epubs.siam.org/doi/10.1137/0314056) | 核对题录和官方摘要的极大单调 PPA 背景；本次未读付费全文，未重新认证其每条基础性质。此项核查深度低于上述有精确编号的调用。 |

references.bib 保存了预印本 v2 与正式 Evens 论文两个键；编号引用使用 v2，叙述引用使用正式发表键，身份可辨。本轮未核正式 Evens 版的逐项编号，所以不把 v2 的核查冒充正式版编号审计。未作穷尽文献检索、全球先行性比较或期刊要求核查。

## 6. 三项实际 Skill 任务

### 任务 1：中文例子开头

输入是 B 版本 `verification_example.tex` 的开头三句，及其后紧邻的 F、S、λ 定义和完整近端公式。任务只允许在报告中提出改稿。

**原文**

> 下面考虑一个具有线性法向阻尼与平方根切向漂移的二维三角系统。
> 一个坐标向零集作线性收缩，另一个坐标沿零集漂移。
> 这个例子说明，近端映射虽不局部 Lipschitz，切向位移的可和性仍能保证点收敛。

**改稿**

> 下面的二维三角系统同时具有线性法向阻尼和平方根切向漂移。其近端映射在零线附近不局部 Lipschitz，但法向距离线性衰减、切向位移可和，轨道仍收敛到零线中的一点。

**理由与验收**：第一句说明对象的两个分量；第二句把距离衰减、切向可和与点收敛接起来。删去重复的“一个坐标/另一个坐标”，保留两项收敛原因，并把非 Lipschitz 结论定位于已证明的零线邻域。后接 F、S、λ 定义时没有重复公式或新符号；不改方程、常数、锐指数或引用。模拟普通研究者逐句朗读，两句各增加不同信息。候选为表述简化，不是新数学断言。

### 任务 2：英文句子

此项单独使用所给英文句和数学写作模式，未将任务 3 的输出当作证据。

**原文**

> The distance goes to the set, therefore the sequence converges to one point, even if the mapping is multivalued.

原句存在科学含义问题，不宜只做语法润色：“distance goes to the set”应是距离趋零，但这不能独自推出点收敛；“one point”也容易被理解为所有选择具有同一个极限。

**建议改稿（显式补足条件）**

> In a complete metric space, a Cauchy sequence whose distance to a nonempty closed set tends to zero converges to a point in that set, even when the generating mapping is set-valued.

**理由与验收**：把错误因果修成有条件的陈述；完备性供应极限，闭性和距离趋零将极限放入目标集。`a point` 指这一条轨道的极限，不声称解唯一或各选择同极限；`set-valued` 是此处惯用术语。该改稿增加 Cauchy、完备性和闭集前提，属于明确的数学修正，不能标作“原意完全不变的英文润色”。在本稿 X=Rⁿ 中，完备性已经具备，Cauchy 性由已证有限长度供应。没有新增引用，也不声称集值性本身带来收敛。

### 任务 3：命题审查

**原命题**

> If d(x_k,S)->0 and S is closed, then x_k converges.

**判定**：错误。即使 S 紧、凸且序列有界，仍不成立。

在 \(X=\mathbb R\) 中取
\[
S=[-1,1],\qquad x_k=(-1)^k\left(1+\frac1{k+1}\right),\quad k\ge0.
\]
S 非空闭、紧且凸，且
\[
d(x_k,S)=\frac1{k+1}\longrightarrow0.
\]
但偶数子列趋于 1，奇数子列趋于 −1，因此整列不收敛。每一前提与失败结论均可解析核验，不依靠模拟。

**修正命题**

> 设 X 是完备度量空间，S⊂X 是非空闭集。若序列 (x_k) 是 Cauchy 列且 d(x_k,S)→0，则存在 x∞∈S 使 x_k→x∞。有限长度 ∑_k d(x_{k+1},x_k)<∞ 是 Cauchy 性的一种充分条件。

**证明**：完备性给出 \(x_k\to x_\infty\in X\)。距离函数是 1-Lipschitz，故
\[
d(x_\infty,S)\le d(x_\infty,x_k)+d(x_k,S)\to0.
\]
S 闭，推出 \(x_\infty\in S\)。若长度级数可和，则任意尾段满足
\[
d(x_m,x_n)\le\sum_{j=n}^{m-1}d(x_{j+1},x_j)\to0\quad(m>n\to\infty),
\]
所以序列 Cauchy。若 S 本来就是单点，距离趋零也直接给点收敛；这属于另一种更窄的修正，不能代替本文的非孤立零集情形。

### 三项候选的精确检查记录

实际调用了 Skill 的 `audit_candidate_text.audit_candidate`，对三个独立 UTF-8 候选文本逐项检查。输入为从本稿定义提取的局部术语/保护词字典，没有加载原始投稿包的旧状态，也没有新建正式项目账本。三个候选均未产生该扫描器的诊断匹配。

| 候选（纯文本末尾含一个换行） | SHA256 | 实际检查 |
| --- | --- | --- |
| 任务 1 改稿 | `f6a3cf6e99929e797f917f12a76db43d5f88d6a501d6e1e2fd3855014df0956a` | 原文/改稿语义、前后衔接、重复与普通朗读；无公式或引文改动。 |
| 任务 2 改稿 | `4c5095cc845d5abf84c64a6cdf7428458ecfb7bd1e6be69664c0eac81996be52` | 逐从句检查前提与结论；明确标出新增数学前提；技术连字符 set-valued 保留。 |
| 任务 3 修正命题 | `029ed17e6c25066cb001d357988e0718e4a5dbf9998be595fa368afe1fea3dcf` | 反例的每一前提、两个子列极限、修正命题的完整证明与可和尾段。 |

扫描器主要处理英文词形与注册规则，不能凭“无匹配”认证中文自然度、逻辑完整性或全文通过。上述结论同时依靠已记录的人工语义与连续性检查。报告未改主稿、Skill 或账本，也未提交。

## 7. 功能覆盖回看

- **checked**：按实际输入顺序完成论证结构、证据/范围、学术行文、源码交付四类阅读；覆盖引言、前置判定、主定理、三角例、固定 SPD 与一般核边界、局部/全域拓扑、比较段和结论。变动后只复读受影响段落及邻段，再绑定 B 快照。
- **checked**：源码标签/引用键检查未发现重复 label、未定义 ref 或缺失 bib 键；精确候选扫描实际执行。外部来源核查深度见第 5 节，不将摘要核查升级为逐定理复核。
- **not applicable**：没有编辑格式化主稿，不需要为本报告重新编译或检查新 PDF 版式；没有改变作者/批注身份、图表、数据或期刊格式。
- **outside scope**：补充稿、历史投稿稿、内部报告、Skill 改写、正式账本、提交/推送、全球新颖性和投稿认证。
- **unverified**：原生 CLI 隐式触发；付费 Rockafellar 全文；未声明逐项核验的其他论文定理；当前 PDF 是否与 B 源码一致。
- **剩余项**：E2 为已明确数学区分后的可选阅读次序调整；E1 的首句可进一步具体化；E3、E9、E10 为局部简化建议。没有据此制造新的主定理假设或声称整个投稿包已就绪。

本报告可以作为指定版本的独立行文反馈和三类显式 Skill 使用记录。三项任务的完成不等于主稿整体质量认证，也不等于隐式触发测试通过。
