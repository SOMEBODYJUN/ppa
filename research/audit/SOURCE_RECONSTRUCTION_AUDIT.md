# 来源重构覆盖审计

审计基线：`2d127c9`；2026-10-01。开始时工作树干净，先读取 README、CLAIMS、RESEARCH_STATE、FAILED_ROUTES。下列来源簇覆盖表以该基线为准；现行逐数学单元状态以 [UNIT_DISPOSITIONS.tsv](UNIT_DISPOSITIONS.tsv) 为准，以下第 6 节起是逐批增量记录，不能凭文件出现自动关闭缺口。

**盘点不等于数学验收。** 本次逐文件字节盘点、ZIP 成员枚举、历史审计核读及代码复跑，不能声称已独立读完每份原稿的每个证明。新资产应从原件重写精确数学内容；历史文本只作证据和反例线索。未来原创研究也按同一规范进入，不以历史文件数量限制增长。

## 1. 可重复核对的范围

| 对象 | 实测数量 | 本次完成的工作 | 尚不表示 |
| --- | ---: | --- | --- |
| 原件文件 | 251 | 路径、长度、SHA-256 | 251 个文件的所有数学内容均已裁决 |
| ZIP | 11 | 对每包枚举非目录成员，并递归检测 ZIP | 包中每一命题已重写 |
| ZIP 非目录成员 | 178 | 哈希、长度、与展开原件的逐字节匹配 | 178 个独立成果 |
| 与展开原件相同的成员 | 41 | 哈希匹配 | 不同文件的语义等价；其余 137 项无价值 |
| 已展开数学验证器 | 10 | 当前环境全部退出码 0，保存完整输出 | 普遍定理成立、代码数值方法正确、所有端点已证 |

本次 11 个 ZIP 内未发现更深 ZIP。外层上传包与历史已展开包不在这 11 个仓库 ZIP 的计数中。每个来源的具体路径见 [原件清单](SOURCE_FILE_INVENTORY.tsv)；每个包内小文件见 [成员清单](ZIP_MEMBER_INVENTORY.tsv)。清单中的 `semantic_disposition=unreviewed` 是**逐项验收未关闭**，不等于从未有人读过该文本。不能把哈希去重填成 `proved`。

**当前覆盖读法**：当前 110 行逐源单元有去向（104 rewritten、3 superseded、3 deferred），最近的 GX-055–058、SS1 解选择、S19 signed-Schur 与 Markov Theorems 6/8 的选定单元见逐单元表；文件级、ZIP 成员级的 `unreviewed` 保留至该来源的全部有价值单元均有理由明确的去向。逐源行数除以 251 不是覆盖率：分子是章节/命题，分母是文件，且数份历史稿重复同一对象；目前尚无全部有价值单元的语义分母。[来源位置表](SOURCE_OCCURRENCES.tsv)与[内容组表](PAYLOAD_GROUPS.tsv)已由[生成器](build_occurrence_index.py)精确对账，仍只有格式提示及待枚举状态；[分母计划](SEMANTIC_INVENTORY_PLAN.md) 中逐段数学枚举尚未完成。

所有历史路径统一指向 `history/sources/`。迁移只改变位置，原件字节不得改变。每次新导入记录独立批次，不重写初次导入哈希。

## 2. 来源簇 → 现有规范层 → 仍需重写

### 下一批可定位的证明单元（局部工作清单）

此表是从**已有原件**中定位的高价值缺口，不是全库有价值单元的穷尽分母；未列入逐单元表的单元仍为待裁决。完成一项后以精确节、版本和正文锚点记入 `UNIT_DISPOSITIONS.tsv`，不能仅凭本表的存在标为 `rewritten`。

| 原件与精确单元 | 当前规范层的不足 | 准入义务 |
| --- | --- | --- |
| S19 ZIP `RLEB_投稿扩展版_2026-09-19/sections/appendix_signed_schur.tex`：`thm:signed-schur-growth`、`cor:schur-power-constants`、`prop:schur-matched-jet`、`prop:schur-sharp-exponent`、`prop:schur-square-root-test`、`prop:schur-collision-counterexample` | 六个指定标签现见 [C117–C119 独立重构](../canonical/signed_schur_growth.md#ss-source)；全稿其它单元与原版范围仍未穷尽 | 逐单位独立核前提及证明，区分局部图块与完整近端。S18 ZIP 的同名成员与 S19 成员 SHA-256 同为 `9927b4006234fa5f435d831a8583c426311906ba8288a60894516f97cea829d2`；数学重算一次、版本归属分别保留。 |
| SS1 修订 ZIP `research_note.md`：§1 定理 1/推论 1、§2 定理 2、§3 定理 3、§4 定理 4、§5.1–5.2 两个结构推论 | §1 定理 1、§4 定理 4、§5.1 选定单元见 [SS-TRANSFER/SS-Q2](../canonical/solution_selection_rates.md)；§1 推论 1、§2–§3、§5.2 仍缺逐项重构 | 已核所列抽象尾与特定二次完整模型；仍须分别核几何尾模型、§1 推论 1、§2–§3、§5.2 与 §6 的一手先行性。 |
| 9/01 ZIP `work/a_consistency_audit.md`：B-01、M-02、M-04、M-05、M-06 | 来源指出增长步长 rate、有限维 converse、inverse 的 PSNC 方向、一般度量 (q>1) 和 Luke–Tam Euclidean scope 的具体风险；当前没有逐项关闭记录 | 对每个原命题与现行正文做对象/维数/量词对照；修正则另立版本，已避免则写带锚点的 `superseded` 或 `duplicate` 理由。不能把旧审计题头当证明。 |
| 9/14 锥与 Markov 的原始证明、conditional bit/Gaussian 证书 | [锥/Markov 总述](../cone_markov.md) 可定位路线，但部分子定理仍缺独立正文及逐源去向 | 先按面稳定、MSCQ、同步耦合与目标边缘分成不同 Claim，逐条核完整残差桥、全部参数与外部引用；不把有限验证器 PASS 升级为全称结论。 |

GX-055–057 的指定单元已有 C108–C114 正文；GX-061 的端点、残差和近端已按 C120/C121 验收，GX-062/063 的旋转族、循环阶和锐模也已按 C122/C123 重写；9/01 其余例卡仍须按**完整对象和观察**逐项处理。一张卡的已审属性不关闭其 VI 标签、二参数区和外部先行性。缺失的 I-097–099/I-102 原证明与上表“原件可得但未重写”属于不同障碍。

| 来源簇与定位 | 基线规范入口 | 尚未关闭的内容与验收要求 |
| --- | --- | --- |
| 9/01 三个 checkpoint，`research/theory_atlas.md`、`work/a_*` | [foundations](../foundations.md)、[operator_space](../operator_space.md) 仅部分覆盖 | 单调性与正则性完整定义字典、术语冲突、逐边严格性、不同空间的引用条件；逐条保留 MR/MSR 与 inverse Aubin/calm 的对象方向 |
| 9/01 `research/gap_examples.md`、`example_properties.md`、六份 `work/c_gx*.md` | 尚无完整规范例库 | GX-001–077 逐卡重写、同构/缩放/参考点去重；每卡需完整 F、域、零集、λ、残差、局部窗、最优常数证明或待定标记 |
| 9/01 `work/c_consistency_audit.md` | 尚无逐项修正关闭表 | 历史审计有 18 项以上具体修正；不是全部 PASS。优先保留 tuned-step、fixed-target/two-variable、modulus-zero 机制、例卡重复和限定窗 |
| 9/01 `work/a_consistency_audit.md` | 尚无规范冲突台账 | PPA-03 增长步长 O/Ω 争议、Spingarn 命名、有限维 converse 被 Hilbert 化、PSNC inverse 方向、一般度量 q>1 反例；均是历史报告，引用外部原文前再核 |
| 9/01 novelty checkpoint，`RL_novelty_boundary.md`、`novelty_*`、`claim_safe_matrix` | 各模块零散提及先例 | 新颖性对照需独立文献卡：检索日期、访问深度、逐定理对象映射和未读全文门；旧“deepread”标题可能仅为摘要级读取 |
| 9/09 T4 包，`ATTACK_C11_COMPOSITE_GENERALIZED_SUBREGULARITY.md`、`verify_c11_composite.py` | 基线缺独立模块 | 复合次正则与多步路径应重写；历史 C11 与当前 C11（极限回缩）不同身份，必须有命名空间，禁止直接合并 |
| 9/14 历史总包，RL 核心及 35 条超边 | [rleb_ppa](../rleb_ppa.md)、[旧边对照](../HISTORICAL_EDGE_CROSSWALK.md) | 旧边逐条对照已存在，但逐源命题/例/失败机制尚非全部覆盖；边有去向不意味着所有原件内容有去向 |
| 9/14 随机与 Markov 分支 | [cone_markov](../cone_markov.md) | 基线时相关性感知近端、四点耦合、非乘积/吸收障碍、可数紧扩展需独立命题身份及依赖；本轮 RP 子链的新增去向见第 6 节，其余未关闭 |
| 9/14 锥分支与 v04 ZIP | [cone_markov](../cone_markov.md) | 原始 CRSC、nice/amenable、面稳定、法向/切向修正的每个依赖及验证器尚需一一关联 |
| 9/18 投稿与 9/19 扩展 ZIP | [rleb_ppa](../rleb_ppa.md)、[holder_structure](../holder_structure.md) | 主要收敛/Dini/回缩已整理；signed-Schur verifier、锁定台账和来源版本仍需逐项裁决；随机完备性修正版与原措辞保持不同版本 |
| 9/18 解选择及修订关闭 ZIP | [solution_selection](../solution_selection.md) | 规范层保留修补方向；`Codex_independent_audit.md` 是任务书，真实审计在修订包，不能让文件名替代证据身份；数值 CSV 不是证明 |
| 9/20 分类集与 9/21 提纯总账 | [operator_space](../operator_space.md)、FAILED_ROUTES | 当前缺失原证明与历史 SOURCE-MISSING 分开；恢复源文件只关闭“找不到”，不会自动关闭“证明未核”；I-097–099/I-102 仍需原件/精确证明 |
| 9/23 正式 TeX | [holder_structure](../holder_structure.md)、[range_finite_data](../range_finite_data.md) | 主要结果覆盖但外部定理适用性与先行性独立；候选稿不是公认定理 |
| 9/25 PDF | [holder_structure](../holder_structure.md) H07 | 整窗指定 T 的拓扑假设及其实际认证仍未关闭；原引文 Theorem 6.2 的 retract/Vietoris/compact→CAC 适用门后来已在 [LIT-GRN-2002](../LITERATURE.md#lit-grn-2002) 一手核对，不能靠有限数据补足其他前提 |

上述“尚无”按 `2d127c9` 判断。并行新增模块应在后续提交中填写：精确锚点、重写版本、审核者、未闭义务；不直接删除来源簇。

## 3. 例库增长必须防止的错误

核读旧 `c_consistency_audit.md` 得到以下**来源提出的整合要求**，本次不是对全部 GX 证明的独立确认：

1. 77 个 GX 是观察条目，不能统计成 77 个独立算子。Volterra 与其伴随的酉共轭、同一 cubic 的不同残差、同一法锥的参考点观察须分清。
2. 一个规范对象可以有多个 observation；不同映射如 `N_L` 与 `I-P_L` 不能因为共享集合就合并。
3. fixed-target MSR/SMSR 与 nearby-target MR/SMR 分开存常数。`modulus=0` 指缩域后常数下确界；需标大零集、域外真空、分支钉住、残差跳跃或超线性 germ，不能当统一强度。
4. RL 记录至少包含 `(graph/window, λ, γ, L, local/global, all-pairs/anchored, genuine/inherited)`。所有步长碰撞、临界值与尾部抵消必须随观察保留。
5. GX-071 属反向校准构造，不能用其定义得到的 `γq` 恒等式充当普遍经验定律。GX-025/026 的共同推导可以共享，但规范观察应各有身份。
6. 上界被改进与旧命题被反例推翻是两种关系。不得把 `C-SHARPEN`、`C-REFINE`、`C-UPGRADE` 一律记成历史错误。

## 4. 代码与再现性

[运行记录](LEGACY_VERIFIER_RUNS.json) 保存 Python、NumPy、SciPy 版本、脚本哈希、命令、退出码及 stdout/stderr。十个展开数学验证器全部运行成功。历史构图/校验程序、字体生成器、ZIP 内 `verify_research.py` 不包含在这十个结果中；它们不能继承 PASS。

下一步代码验收必须逐个登记：规范 Claim 版本、数学测试对象、精确有理/浮点/随机类别、输入及固定种子、容差、依赖、预期输出、已知盲区。旧脚本内容只作为参考；需要继续维护的代码应重写到规范代码区并与 Claim 同版本变化。一次数值 exit 0 不能证明无界域、所有样本、任意维数、锐常数或收敛端点。

## 5. 可增长的验收门

新研究与历史重构共用下列门；每项允许状态停留，并记录阻塞理由。

| 门 | 必交付的内容 | 通过后允许的使用 |
| --- | --- | --- |
| G0 来源或研究问题 | 来源哈希/位置或原创问题、任务范围、现有对象检索 | 进入待研究区，不获得真值标签 |
| G1 身份 | 稳定 ID、版本、对象与规范同一性、来源别名；例卡区分 object/observation | 可索引，避免重复计算和编号碰撞 |
| G2 精确陈述 | 空间、域、量词次序、全部合取假设、结论、残差、参数与窗；定义先存在 | 可进入候选图，不得假装可调用定理 |
| G3 证明及攻击 | 可独立读懂的推导、依赖版本、反例测试；外部定理写精确接口 | 按实际审查深度标正文证明/局部核验/独立验收 |
| G4 范围和证据 | 区分分析证明、有限计算、来源报告、新颖性；反向/否定边有独立见证 | 可建立带 scope 的超边，禁止证据等级自动传播 |
| G5 整合 | 正文精确锚点、Claim、图、反例、前沿状态同步；检索能从结论找到条件和证据 | 成为后续研究规范入口 |
| G6 可重现与保存 | 代码/链接/锚点检查，相关运行记录，提交与远端核对 | 完成该批交付；不表示所有来源清洗结束 |

语义覆盖的关闭条件：对一份来源的每个有价值单元给出 `rewritten / superseded / refuted / duplicate / nonmathematical / deferred` 之一及理由。`rewritten` 必须指向规范单元的版本与锚点；`duplicate` 必须说明是字节相同还是数学等价；`deferred` 保留可执行下一步。不得用“整个 ZIP 已读”代替这些映射。

未来增长不要求先清空所有历史待办。新命题、桥、反例、例子、算法实验和失败路线可独立进入 G0；通过 G5 后加入规范正文，旧版本保留 `supersedes/refines/refutes` 关系。研究地图由这些对象和关系生成。

## 6. 本轮已整合单元与仍开放的同簇范围

| 来源单元 | 新规范身份与位置 | 重写和证据深度 | 后续义务 |
| --- | --- | --- | --- |
| 9/14 随机相关性感知报告的有限维不一致二次近端正类 | [C22-v1 / RP-EB](../canonical/random_proximal.md#rp-eb)，前置 RP-OBJECT/GAP/CONTRACTION；图 E54–E56 | 矩阵谱隙、同步耦合、不变律分类、条件 law-step 双边 EB 与有限长度独立重算；`derived-checked` | 外部文献优先权、变参数/无限维版本；历史验证器仅有限运行 |
| 同报告的逐分支残差障碍及标量实例 | [C23-v1 / RP-BRANCH](../canonical/random_proximal.md#rp-branch)、[RP-SCALAR](../canonical/random_proximal.md#rp-scalar)，[F09](../../FAILED_ROUTES.md)；图 E57–E58 | firm nonexpansiveness 积分证明、平稳物理步长反例与锐常数推导；`derived-checked` | 不同残差的零集桥需另证；不声称整个 9/14 随机目录均已裁决 |
| 9/01 GX-004/009/021 的对象与本轮选择的观察 | [C24–C26 / EX01–EX03](../canonical/example_atlas.md)，图 E59–E61 | 旋转、正紧对角、三次映射的对象、真残差、完整 J、边界及常数均直接重算；`derived-checked` | 其他 GX 与这三张原卡尚未重写的属性（如 paramonotone、rectangular）仍是 `unreviewed` |
| 9/01 foundations / regularity 的选定定义、参数与 GX-015 换步 | [C27–C30 / PD 字典](../canonical/parameter_dictionary.md)，图 E62–E67 | 全对量词、Cayley、tied 曲线端点、同图换步、尺度及残差方向独立重算；`derived-checked` | 一般二参数 semimonotonicity、coderivative、全 GX 最优常数未吸收；原 ZIP 其他单元仍 `unreviewed` |

上表四行只裁决所列数学单元，逐文件 TSV 的 `semantic_disposition=unreviewed` 暂不批量改成 `rewritten`，因为同一来源仍含其他 Claim、例和版本。应在逐单元映射齐备后，才给整份来源关闭状态。

## 7. 历史 checkpoint：合法路径与复合次正则的逐单元重写

本节保留当时的待办快照；后续 §8–§9 已关闭其中部分单元。当前状态以逐单元表和前文覆盖边界为准。

[逐单元去向](UNIT_DISPOSITIONS.tsv) 新增 14 个来源单元：9/09 多步札记的 §2–§4 有规范版本 C31–C33，其中 §3.4 与 §4 的扩大陈述被修订，§5 M1 具体常数和 §6–§9 外部比较仍未核；复合模块 §2–§5.2 的 C34–C37 已重写，§5.3 真多值、§6.2 振荡弱分离和 §8 文献仍待裁决。每行给源文件、精确小节、版本、锚点、修订理由和下一义务。9/09 T4 ZIP 内复合稿与 9/14 展开件同 SHA-256，算一份证据。

本批新增 [path_atlas](../canonical/path_atlas.md) 和 [composite_subregularity](../canonical/composite_subregularity.md) 的数学正文及 [F12/F13](../../FAILED_ROUTES.md)。两个原件均还有未审单元，故原件和 ZIP 清单的文件级语义状态继续保持未关闭；“逐节已重写”不等于“整份材料已验收”。后续原创研究不受这些待办约束，按增长协议直接进入新 Claim。

## 8. 增量：M1 的显式映射与较晚来源修订

9/09 多步札记 §5 的**给定单值外层映射**已经在 [C38](../topics/path_dynamics/m1_capture.md#m1-capture) 重算：指定端点球的每个初值两步捕获。历史区较晚的旗舰架构札记 §2 给出关键修订；[C39](../topics/path_dynamics/m1_capture.md#m1-sharp) 独立重算了同一球上锐的一步因子 \(3/\sqrt {10}\)。因此“独立标量 RL–EB 乘积小于 1”只说明该证书丢失活动相关性，不能说实际一步距离不收缩；见 [F14](../../FAILED_ROUTES.md#f14)。两份来源与对应小节分别进入逐单元 TSV。

历史札记还称原生隐式方程含真正多值 `Sign` 图。现有本批重算没有它的完整方程和允许选择契约，故 `§5 原生 Sign 图与隐式求解` 保留 `deferred`。文件级清单仍未关闭；这两条数学结论绝不等于整份多步札记、9/14 包或 251 个来源的验收。

## 9. 增量：复合稿的尖点外层与弱分离障碍

历史复合稿 §5.3 的真多值变体已拆成 [CI-OBJECT / C40](../topics/composite_regular/cusp_identification.md)：在同一满秩曲线上写出全部次梯度、S 外残差间隙，并把“步残差小于 \(\nu\)”转成对局部近端输入、步长、乘子界的明确充分门。它没有解决秩亏，也没有检查远端完整近端纤维。§6.2 的振荡函数已拆成 [C41](../topics/composite_regular/oscillating_target.md)：给出趋零的严格局部极大驻点序列，证实无弱分离时到完整二阶目标的全邻域 EB 不可能。两行在逐单元 TSV 从 `deferred` 改为 `rewritten`，外部 §8 仍未核。

[复合主题入口](../topics/composite_regular/README.md)示范目录按独立对象/证明增长；原来源文件级状态依然未关闭。新的数学结论按自身证据身份使用，不能用旧稿的 `PROVED` 字样替代上述条件。

## 10. 增量：9/01 GX-071 的对象卡

[幂次剪切 C42](../topics/path_dynamics/power_shear.md) 从 9/01 foundations §9.2 的 GX-071 重新反演完整图、计算真残差和法向精确速率，并把全对反射指数限定为有界输入窗，附上单条轨道的切向留域预算。它是反向校准的可达性见证，不能当成普遍必要或最佳常数定理。逐单元 TSV 新增此节；同一 foundations 稿其他定义和 GX-072/073、其他历史副本仍未逐项裁决。

## 11. 增量：9/01 GX-072 的振荡剪切

[振荡剪切 C43](../topics/path_dynamics/oscillatory_shear.md) 从 9/01 foundations §9.3 重新证明全域三角逆、局部孤立零点、双边 J 的 q 阶、完整图的真残差 q-EB、两尺度 Hölder 上界及相位极值的锐性。它是一个与 GX-071 不同的对象：全对指数 γ 可保守，实际非零轨道双边阶 q>γq。没有证明归一化 Q 因子收敛，也未审外部先行性。逐单元 TSV 新增此节；GX-073 与原稿其余内容仍待裁决。

## 12. 增量：9/01 GX-073 的自然域逃逸

[自然域逃逸 C44](../topics/path_dynamics/domain_escape.md) 从 foundations §9.4 重算指定 Minty 域上的多值原关系、锚定与全对两种指数、所有非零初值有限步越域，以及对全部原像一致的真实残差线性模。它不是 GX-071/072 的全域三角图；一步尺度不能替代不变性和收敛。逐单元 TSV 新增此节。9/01 foundations 的其余定理和历史副本仍未全量裁决。

## 13. 增量：孤立零点分支链与 GX-074

[孤立零点平坦性](../canonical/isolated_zero_flatness.md) 按 foundations §7.1–7.6 重写：图 germ 的 B/J/R 三模等价不需先假设完整 resolvent 单值；真 EB 到逐分支界只用残差方向，反向必须覆盖所有小残差纤维；C45 的指定近端分支上阶需全部输入/输出窗口及小步门；C46 的正 Q 因子是额外归一化极限。双值关系给选中界不蕴含真 EB 的直接反例。

[GX-074 / C47](../topics/path_dynamics/discrete_coverage.md) 从同稿注 1.5 重算紧图上全对 RL、目标 S=K 的真 EB 与任意零邻域缺输入；它只反驳无条件 coverage 升级，见 [F16](../../FAILED_ROUTES.md#f16)。逐单元 TSV 为这两组数学内容新增五行；foundations 的 §8 非孤立 alignment、§9.1 与别处尚未逐项验收，不能把整稿置为 rewritten。

## 14. 增量：非孤立解集的对齐与同序列锐性

[非孤立 alignment](../canonical/nonisolated_alignment.md) 把 §8.1–8.3 和 §9.1 拆成 C48–C50 及 NA-APPROX：最近点存在性须覆盖整个 envelope 输入家族，集合间 infimum 不要求取到；真 EB、小步门、锚漂移 profile 和 gauge 定义域合取才给上指数；无最近点时另用正容差近似锚；精确 \(\theta q\) 见证需同一序列的三个正比值。逐源 TSV 再增加四行。GX-071–074 的对象卡另有自身证明，不能反向证明这条一般定理最优；其他 foundations 小节和外部文献仍未关闭。

## 15. 增量：moving-anchor 与固定锚的分界

[移动锚反射](../canonical/moving_anchor_reflection.md) 从 foundations §6.1–6.2 重算真残差输出近锚的双边渐近反射比和幂型缺陷常数 C51/C52；线性零集的显式完整关系阻断将输出近锚换为任意固定零点或集合距离收缩，[F18](../../FAILED_ROUTES.md#f18) 记录机制。逐单元 TSV 增加两行。此结果逐图点成立，不自动赋予原算法的输入 coverage、全对 RL 或轨道留域；文件级清洗仍开放。

## 16. 增量：named branch §4–§5 和新振荡反例

[C53/C54](../canonical/named_branch_local.md) 对旧 foundations §4.1–4.3、§5.1–5.4 另立条件链：Hilbert 完备性、B 的指定输入覆盖、A 的全家族近似零点锚（含零距离输入）、E 的实际输出真残差窗口、兼容和留域预算。§5 的 \(\gamma=1\) 与 \(L=0\) 端点不能沿用非退化 \(\gamma q\) 标签。[C55](../canonical/named_branch_local.md#nb-oscillation) 是新构造，显示锚定线性证书加真 EB 和收缩仍不提供完整图的全对线性 RL；此例不是历史原稿声称的来源事实。三行已进入逐单元 TSV，分别标注重写和新推导。本次没有裁决该原稿 §1.3–§3 的全部接口、其余 GX 性质或外部优先权；来源文件级状态继续开放。

## 17. 增量：§3.1 全对图块验证器

[C56](../canonical/all_pairs_verifier.md#av-bridge) 重新证明同图块全对 RL、指定输入 coverage 和 \(d(x,S_G)=d(x,S)\) 对活跃输入的保距离合取，只生产指定分支的 B/A，不生产实际输出真 EB 或完整图排他。[C57](../canonical/all_pairs_verifier.md#av-gap) 是新的完整关系反例：图块 \(L=0\) 全对且满域，但其零图点不保完整零集距离，故零距离输入上的锚条件失败。两行进入逐单元 TSV；旧 §1.1–§2 的其他代数或参数条目与全部 GX 性质并未据此整份关闭。

## 18. 增量：§1.1–§2 的闭域门与已有重写去向

从 foundations §1.1–§1.4 的剪切与 pullback 重新证明 [C58 闭图—闭自然域](../canonical/closed_graph_minty_domain.md#cg-closure)，增加原稿没有作为定理单列的完备性与稠密性合取门。闭图单独无覆盖，图块闭域也不排除完整图外分支。§1.1 的能量代数、§1.4 的 coverage/exclusion 与 §2.1(a)–(c) 的 tied、inverse、缩放此前已在 [参数字典](../canonical/parameter_dictionary.md) 独立重算，此次各给逐单元去向，避免在新正文重复证明后虚增成果。新增五行来源裁决仅针对这些明确语句；§0.4 的残差窗口由下一节另行裁决，更多 GX/同稿边界仍未逐项关闭，源文件级状态继续开放。

## 19. 增量：§0.4 的一般 gauge 残差窗口

[C59](../canonical/residual_window_bridge.md#rw-positive) 将旧稿定义0.4 的幂函数缩域推理重写为有正阈值的充分门，并显式限制到 gauge 可评价残差；[RW-FLAT](../canonical/residual_window_bridge.md#rw-flat) 给闭完整图的平坦 gauge 反例，阻断无条件去窗口。这项新增只关闭 §0.4 中被声明的量词关系，不验证同稿其余定义与后续定理，也不否定另加 all-pairs RL 的特殊结果。逐单元 TSV 增加一行，文件级状态仍开放。

## 增量：GX-069/070、固定目标随机近端、M1 的可行 Sign 实现

[C60/C61 DR 双对象卡](../topics/examples/dr_tangency_transversality.md) 从 9/01 ZIP 的 `work/c_gx066_077.md` 两张卡独立重算投影管、真算法残差、半阶/线性最优模及各自一步/轨道范围。来源用 `archive.zip!/work/c_gx066_077.md` 在逐单元 TSV 定位，验证器检查 ZIP 成员存在；原卡的其余 primal 标签和外部先行性未验收。

[C62/C63 固定目标近端](../topics/random_markov/proximal_selection_seam.md) 从 9/14 非乘积稿 §3、§5 重写域内平稳律吸收、全局近端完整图及 fair tie 核接缝。历史 V10 有理脚本 2026-10-01 复跑退出码 0，只是有限代数观察；一般平稳律与每个 \(W_2\) 邻域的障碍在正文另给证明。四个选定来源单元在 TSV 新增去向，当前共 45；同稿其他随机机制和其余 ZIP 成员仍未裁决。

[C64 新 Sign 实现](../topics/path_dynamics/m1_sign_lift.md) 是针对已核显式 T 的**原创反向构造**，不是把历史原生方程作 `rewritten`；因此不新增虚假的历史单元去向，原 §5 原生桥继续 `deferred`。[F23](../../FAILED_ROUTES.md#f23) 记录两份同名 M1 的身份隔离及恢复原生方程的精确义务。9/25 所引 [6, Theorem 6.2] 的一手适用门另由 [LIT-GRN-2002](../LITERATURE.md#lit-grn-2002) 关闭，但 C05 的整窗模型仍候选。

## 增量：Hilbert 扩张、GX-068 与随机标量提升

[HE-EXTENSION](../canonical/holder_extension.md#he-extension) 重新写出 S23 §2 的 Hilbert 雪花核正性与固定参数极大图逻辑；一手 Hilbert Lipschitz 同常数扩张的正式编号是 [LIT-ALM-2021 Theorem 1.2](../LITERATURE.md#lit-alm-2021)。这里只关闭 H01 扩张步骤的适用范围，不审整篇结构稿。

[C66–C68](../topics/examples/identity_square_branch_union.md) 对 9/01 ZIP 内 GX-068 逐对象重算原算子、全部近端根、完整最小步残差及跨支 RL 碰撞；[C69](../topics/random_markov/scalar_moment_envelope.md) 从 9/14 质量稀释审计 §4 重写任意连续非减 gauge 的硬支持锐矩包络、二点取等与临界分开聚合损失。逐源 TSV 各新增一个数学单元；原卡其他性质及原生随机耦合未验收。[C65](../topics/path_dynamics/m1_sign_lift.md#sl-rl) 对原创 C64 的同一个新完整图补端点球局部指数证明，不虚报为历史原生图的来源单元。代理交叉核了对象常数、近端远根、端点与硬支持，结构与完整证明审查仍有明确范围。

## 增量：有限状态惰性循环的 OT 约束

[C71](../topics/random_markov/lazy_cycle_ot.md#lc-sharp) 将 9/14 有限状态稿 §10.2 的四状态惰性循环拆为完整同步 OT 模型、精确零集、锐常数和去掉 OT 最优性后的假零点，矩阵符号与取等律由正文独立重算。逐源表增加一个单元；原稿一般有限状态定理、其它例、速率兼容和文献先行性继续未审。

## 增量：GX-075 与条件值域版本

[GX-075 C72–C75](../topics/examples/diagonal_spike_relation.md#ds-object) 已从 9/01 ZIP 的 work/c_gx066_077.md 逐项重算并新增一行去向；其余例卡和原稿标签不因此验收。[C05-v2](../canonical/local_range_without_supercriticality.md#lr-theorem) 是从 9/25 PDF §8 候选证明独立推出的更弱假设版本，故不冒充来源原文的新单元，保留 C05-v1 原身份。空白接收审查发现的 C58 总账闭性漏项已纠正，并将 \mathbb Q\times\{0\} 型稠密非闭图反例写入该 Claim。

## 增量：一般有限状态证书与 GX-076/077

[C15](../topics/random_markov/finite_state_certificate.md#fs-theorem) 的原摘要本轮补成完整 finite LP 对偶 tight-edge 证明，保持同一 Claim 版本；两点翻转单列误差界不推收敛的动力边界。来源 §§1–4、§7 与 §8 两个单元进入逐源表；§5/§6 后于下段单列去向。C71 四状态模型继续保留自己的直接锐常数证明。

[C76/C77](../topics/examples/hemiregular_piecewise_parabola.md#hp-object) 从 GX-076 重算异维数映射的锐固定目标/两变量半阶与最近逆点线性模；[C78/C79](../topics/examples/absolute_value_subgradient.md#av-object) 从 GX-077 重算完整原算子残差跳跃与近端步残差锐模 1。两张对象卡不把历史 `verified` 字样当成数学证据；前者所引一手 Example 2.3 只支持定性对象/对照。盲读指出的 C69 总账硬支持参数 \(0\le t\le R\) 和 C31 的 M1 过期状态已修正。

本轮空白接收可以仅靠规范层恢复收敛链、候选与开放义务，但指出总体规模比较尚无冻结的共同母空间与量尺；这属于实际研究问题未完成。历史 I-097–099/I-102 原证明缺件属于来源材料缺口。其余逐源覆盖属于尚未做完的清洗工作，不能一概归因于缺件。

## 增量：有限状态备用证明与全域正则性

[FS-HOFFMAN](../topics/random_markov/finite_state_certificate.md#fs-hoffman) 重写同一 C15 的非锐备用证据：非空零面用 Hoffman，空零面用紧性正下界。[C80](../topics/random_markov/finite_state_certificate.md#fs-regularity) 在固定有限状态上分离出 \(\Phi=\Psi^2\) 的全域 Lipschitz 与连续分片仿射性，不用 C15 的零集鉴别；[Hoffman 原文](../LITERATURE.md#lit-hoffman-1952) 的固定矩阵且目标系统有解的接口已核。来源 §5、§6 两行只关闭这两个单元，原稿其它例及先行性依然未审。

此处原列的 GX-068 两变量正则、GX-032 受限图与 `work/a_monotonicity.md` §2.1 非 tied Cayley 是**当时的下一步建议**；现分别见 [C92](../topics/examples/identity_square_branch_union.md#is-mr)、[C85/C86](../topics/examples/restricted_root_graph.md#sr-geometry)、[C89–C91](../canonical/non_tied_cayley.md#nt-audit) 的选定单元重写。GX-068 的二参数 semimonotonicity 区域随后又由 [C95](../topics/examples/identity_square_branch_union.md#is-semimono) 重证；继续核 §2.2 以后其它参数类、VI/外部先行性。来源级 `unreviewed` 目前同时覆盖未建语义索引与已有部分逐源去向，不能从该字段估算验收比例；完整关闭前须对声明的文件/成员 hash 范围建立穷尽的单元表，每个单元给去向及证据层。`deferred` 可完成分类，但数学义务仍开放。

## 增量：GX-067 与 GX-068 CCA-M14

[C92](../topics/examples/identity_square_branch_union.md#is-mr) 对完整并图同时核目标正负的两变量半阶 MR、逆 Hölder–Aubin 量词和系数 1 的最大对称窗口；只关闭旧 CCA-M14，不以最近逆点的线性模代替完整逆关系。[C93/C94](../topics/examples/ball_normal_cone.md#bn-object) 从完整闭球法锥重算全域反射与二参数区，区分固定零目标的真空 MSR 系数**下确界**与每个参考点上两变量/逆像稳定性的失败。敌对重算已纠正零乘无穷的语义及 HREG/UHREG 分母的差别。历史原卡其余性质仍待审。

[C95](../topics/examples/identity_square_branch_union.md#is-semimono) 再以完整跨支割线重证 GX-068 的全图/同窗二参数区域 \(\mu<0,\rho<0,\mu\rho\ge1/4\)，并验证这些同图参数对每个步长均不满足 C89 的正 \(A\) 门。独立敌对重算确认边界 \(\mu\rho=1/4\) 包含及同输入图碰撞；其它旧标签仍不能按整卡升级。

## 增量：正值正弦图的目标与尺度分离

[C81/C82](../topics/examples/positive_sine_phase.md) 对 9/01 ZIP `work/c_gx053_065.md` GX-064 分两项重写：完整图在 \(\lambda=1\) 的全对临界常数需要**任意两**图点的统一积分界；非零目标 3 的半阶 EB 属另一个图点和目标。两项逐源行已登记；新增的每选择近端向负无穷是本库直接推导。它无零点，不构成 PPA 零目标反例；CCA-M08 的修订仅把两种模区分为观察精化。该 ZIP 的其余 GX 和旧卡其它 VI/二参数性质仍未验收。

## 增量：GX-060 Volterra 与 GX-054 负三次

[C104/C105](../topics/examples/volterra_integration.md#vo-object) 重写 GX-060 的完整积分图、真残差及反射，另证每个有限近端幂范数为 1 与每初值强收敛并存；真残差和步残差分别给消失 gauge 的高频反例。来源 CCA-M10 指出 GX-061 伴随图酉等价，现又在 [C120/C121](../topics/examples/adjoint_volterra.md#av-object) 验收 GX-061 的端点、残差与完整近端，保留两方向一例型的去重范围；未核外部 BWY 归属和旧目录其它属性。

[C106/C107](../topics/examples/negative_cubic_branch.md#nc-object) 重写 GX-054 的完整远根与受限分支；固定零目标/两目标模和 EX03 正三次有符号变换关系，而全图 RL 碰撞与指定路径越域另行证明。旧二参数分类和其它标签未核。这两条历史逐源行只关闭其明确数学单元；该批当时总表为 106 行，现行总表以文件首段与实际 TSV 为准，文件级清单仍不能算数学验收。

## 增量：Z07 GX-053–065 成员的结构分段

[语义试点表](SEMANTIC_UNIT_SEED.tsv) 已对该成员 1–1219 行建立 39 个连续结构段，包括 13 张 GX 卡、交叉审计逐行、文献和数值/合同尾部。14 段仅有部分规范对象锚点，25 段没有；所有卡内尚须拆成独立属性/量词/版本单元。验证器只确认行范围连续、锚点存在，并未认证全卡属性或来源所称一手文献。此前 S19、SS1 两个试点保留原状态；当前仍无 346 内容组的全库语义分母。

## 增量：旋转族共同公式与 GX-062/063

[C122/C123](../topics/examples/planar_rotation_family.md#pr-object) 从 Z07 765–908 行重建全部旋转参数的完整 Minty 纤维、输入对距模、循环门和两角精确表。GX-063 902–905 行族内“强模不能还原循环阶”的解释已分项 `superseded`，保留同逆像条件数而不同循环阶的比较；来源其它标签及 Voisei 引文未因此关闭。
