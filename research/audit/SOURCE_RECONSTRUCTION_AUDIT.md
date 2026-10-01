# 来源重构覆盖审计

审计基线：`2d127c9`；2026-10-01。开始时工作树干净，先读取 README、CLAIMS、RESEARCH_STATE、FAILED_ROUTES。下列来源簇覆盖表以该基线为准；本轮新增内容的整合状态另见第 6 节，不能凭文件出现自动关闭缺口。

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

所有历史路径统一指向 `history/sources/`。迁移只改变位置，原件字节不得改变。每次新导入记录独立批次，不重写初次导入哈希。

## 2. 来源簇 → 现有规范层 → 仍需重写

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
| 9/25 PDF | [holder_structure](../holder_structure.md) H07 | 整窗指定 T 的拓扑假设及 Lefschetz 引用未关闭，不能靠有限数据补足 |

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

两行只裁决上述数学单元，逐文件 TSV 的 `semantic_disposition=unreviewed` 暂不批量改成 `rewritten`，因为同一来源仍含其他 Claim、例和版本。应在逐单元映射齐备后，才给整份来源关闭状态。

## 7. 后续增量：合法路径与复合次正则的逐单元重写

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

## 15. 增量：§1.1–§2 的闭域门与已有重写去向

从 foundations §1.1–§1.4 的剪切与 pullback 重新证明 [C58 闭图—闭自然域](../canonical/closed_graph_minty_domain.md#cg-closure)，增加原稿没有作为定理单列的完备性与稠密性合取门。闭图单独无覆盖，图块闭域也不排除完整图外分支。§1.1 的能量代数、§1.4 的 coverage/exclusion 与 §2.1(a)–(c) 的 tied、inverse、缩放此前已在 [参数字典](../canonical/parameter_dictionary.md) 独立重算，此次各给逐单元去向，避免在新正文重复证明后虚增成果。新增五行来源裁决仅针对这些明确语句；§0.4 的残差窗口由下一节另行裁决，更多 GX/同稿边界仍未逐项关闭，源文件级状态继续开放。

## 16. 增量：§0.4 的一般 gauge 残差窗口

[C59](../canonical/residual_window_bridge.md#rw-positive) 将旧稿定义0.4 的幂函数缩域推理重写为有正阈值的充分门，并显式限制到 gauge 可评价残差；[RW-FLAT](../canonical/residual_window_bridge.md#rw-flat) 给闭完整图的平坦 gauge 反例，阻断无条件去窗口。这项新增只关闭 §0.4 中被声明的量词关系，不验证同稿其余定义与后续定理，也不否定另加 all-pairs RL 的特殊结果。逐单元 TSV 增加一行，文件级状态仍开放。
