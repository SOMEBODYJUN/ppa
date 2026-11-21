# PPA 研究地图：数学节点与真实超边

**当前主任务**是按[作者原版协议](research/topics/dd2/DD2_FINAL_ACCEPTANCE_PROTOCOL.md)完成 [DD1–DD2 全量验收清单](research/audit/DD2_ACCEPTANCE_CHECKLIST.md)。新会话先读 [GPT Pro 开工提示词](research/audit/DD2_PRO_START_HERE.md)，核清一般 \(\Phi\)、一般 \(\psi\) 和指定下降目标 \(\varphi\) 的角色，再从第一项未勾任务恢复。逐项证明、复核、提交并推送后继续下一项。清单本身就是交回作者的完整答卷。[历史审计入口](research/audit/DD2_FINAL_ACCEPTANCE.md)提供既有证据。


## 2026-11-21 最终协议验收入口

阶段提交 `cd028d5` 为 §1–§17、第八部分 28 问、第九部分 10 项交付物和最终六问建立了题号入口。原协议数学验收仍在进行。[总索引](research/audit/FINAL_PROTOCOL_MASTER_2026-11-21.md) 连接 [§1–§3](research/audit/FINAL_PROTOCOL_S1_S3_2026-11-21.md)、[§4–§8](research/audit/FINAL_PROTOCOL_S4_S8_2026-11-21.md) 和 [§9–§17](research/audit/FINAL_PROTOCOL_S9_S17_2026-11-21.md) 的当前证据。

有符号缺陷版本 [C414](CLAIMS.md#c414) 保留正 \(\Phi\) 的根区间与能量预算。复核恢复了作者原 F1–F3，并核回 [C285](research/canonical/rleb_sharp_linear_frontier.md#rsl-threshold) 对一般完整闭图的 DD1 临界锐性。[C416](CLAIMS.md#c416) 证明 \(q>1,p=2/q\) 的锐门是 \(M<\lambda^2K^{-2/q}\)，用一个完整闭图的任意小二周期达到临界失败。[C399 的剪切见证](research/canonical/dd2_power_defect_finite_length.md#dd2-sublinear-power-rates) 实现 \(0<q<1\) 的距离指数及 \(q>1/2\) 时的最坏点误差与实际尾长指数。

主索引记录已关闭的证明义务和仍待研究的具体问题。第九部分的文献矩阵、算子类图与完整证明均仍有未交齐的部分。

[单调性与正则性的共同结构](#common-structure-frontier)是另一研究线。先从各自的定义找出两种几何约束及其在原近端步中的联系。已有收敛定理和仓库里的共用证书只在此后用于核验覆盖或定位障碍。

[DD2 主线](research/topics/dd2/core.md)从指定下降目标 \(\varphi\) 反推锚定下界 \(\Phi\) 与输出真误差界 \(\psi\) 的补偿。DD1 与 DD2 都允许一般有符号的 \(\Phi\)，一般 \(\psi\) 属于 DD2 的研究范围。[C400](CLAIMS.md#c400) 给线性误差界特例的精确反演及实际轨道反例，[C401](CLAIMS.md#c401) 在一般 \(\psi\) 下以同一步积分势推出长度和留域。

[函数条件的逐层裁决](research/canonical/dd2_function_hypotheses.md)给出 C417–C420：原始非单调真残差的联合可行域、正锚下界的完整前像障碍、全部标量递推趋零的精确右侧条件、任意原模的位移下界，以及零缺陷统一算子类的固定模积分充要性。它们把单边、完整整窗、固定图和统一轨道的必要性分开；旧 C400/C401/C414 的身份保持。 [C421](CLAIMS.md#c421) 进一步将原残差联合域精确消成一维上确界，并分别给出连续模或非减点值合同下的有限精度证书和无信息采样的失败机制。 [C422](CLAIMS.md#c422) 说明原域非空时前缀化保持自由单边最优值，却可能改变取等和完整整窗前件；固定图、目标及维数的严格差距均有实际见证。

[目标几何的分层裁决](research/topics/dd2/target_geometry.md)给 C426–C427：二维及以上，紧凸线段甚至同一固定射线都能逐边实现完整自由四点的全部标量；凸性仍限制指定四点，却不降低自由单边最优值。仿射目标的法切正交分解则在越锚支增加精确平方代价。同一组 \(\lambda=1,\Phi=-2t^2,\psi=r/4\) 下，自由凸目标、自由仿射目标和固定单点的锐因子依次为 \(1/2,(1+\sqrt{193})/32,1/3\)，中项有全域连续单值线性算子取等。非正整窗的完整真残差实现与固定轨道的动态障碍分别保留。

[C428 的有符号线性标尺](research/canonical/dd2_function_hypotheses.md#fh-signed-linear-calibration)在固定 \(\lambda=1,\psi(r)=r\) 下给 \(M_\Phi(t)=\sqrt{t^2/2-\Phi(t)}\) 及完整闭图逐尺度取等。密集变号、每个正尺度都不连续的 \(\Phi\) 仍可统一有限长；决定距离与长度的是跨尺度余量和实际步预算。图闭也不容许自动加强证书为邻尺度上极限。

[广义逆合同与 C429](research/canonical/dd2_function_hypotheses.md#fh-generalized-inverse-contract)将精确反向判定与长度下界分开：前者保留严格／非严格超水平的首端归属，后者不要求端点达到。原真残差位移下界恰等于精确前缀的广义逆，并自动非减且 \(1\)-Lipschitz；它仍只对应两条标量约束，不能代替完整几何或长度证书。

[C430 的双向补偿](research/topics/dd2/reverse_compensation.md)在自由单边类固定指定目标 \(A\)：给定一般有符号 \(\Phi\)，求原 \(\psi\) 在危险残差前缀上必须满足的点态帽；给定任意原 \(\psi\)，用三个下界条件的并集和准确非空上端，求允许的 \(\Phi(t)\) 区间。非减、连续或严格可逆都不必预设，开闭端点不可丢失。非正整窗、\(U=H\) 且无额外输出位置限制时，有完整闭图统一类的反向实现；正下界另有连续目标的完整前像分离例。

[充分与必要的量词表](research/topics/dd2/reverse_compensation.md#dd2-compensation-necessity)把指定非严格目标、每条边严格下降、共同收缩余量、固定图和轨道证书分开。精确上确界等于目标却不达到时，每条边仍可严格低于目标。[C431](CLAIMS.md#c431) 还给出每个尺度都非空且统一达标、完整整窗却不可存在的实际反例；同一数据有一个固定闭图的允许选择实现，障碍来自全部完整前像必须同时受检。

[DD2 松弛](research/topics/dd2/relaxation.md#dd2-adaptive-length)给方向余量、全锚和最近锚的速率差异。[方向参数审计](research/topics/dd2/adaptive_parameter_audit.md)把方向商、缺陷吸收和 α 的可计算性分开，并固定 Hölder 同时临界门及零聚点量词。[双误差界](research/topics/dd2/dual_eb.md#dd2-dual-envelope)保留输入、输出和过松弛最近锚的精确几何。[退化 PPPA](research/topics/dd2/pppa_recovery.md#dd2-pppa-gauges)给核纤维上的真残差公式、投影识别及物理长度的独立门。 [C423](CLAIMS.md#c423) 给非减模逐尺度精确界的分解，并证明连续非单调输入模通过完整纤维可在指定尺度产生严格联合增益。

[次阶缺陷长度门](CLAIMS.md#c424)在临界缺陷主阶固定后，以剩余次阶预算精确区分有限长和无限长。[同一 DR 约化下的原变量长度](CLAIMS.md#c425)刻画角分配丢失的相邻变化，给同一约化数据下的真实有限长／无限长分离。

[C432 的真实优化约束](research/canonical/optimization_proximal_limits.md#opl-gauge-length)用全局极小近端的 Moreau 能量替代锚定缺陷预算，在同一真误差模下排除 C424 的 \(q>1/2\) 发散构形，并给逐壳驻留步数和跨步弦长限制。[C433 的同约化真实 DR](research/topics/dd2/splitting.md#dd2-dr-objective-shadow)在临界步长固定完整约化映射和曲率，给完整原图误差模及实际长度的充要判据。前者是普通 PPA 的极小化结构，后者是分裂算法的退化恢复，使用不同的能量和图。[正文选材的一手依据](research/LITERATURE.md#lit-dd2-selection-evidence)列明已知有限长、约化正则性及公开提出的非零 \(U\) 问题。

[P2 覆盖与矩阵门](research/audit/DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-coverage)给出近极小完整图值 lift 的必要量词、选定分支的反例以及原始—对偶块的 Schur 补可计算证书，并由 [C408](CLAIMS.md#c408) 登记其作用域。

[P0 先行性审计](research/audit/DD2_P0_PRIOR_ART_2026-11-21.md)逐式核对 Lauster–Luke 2021、Alcantara v1 和 Li–Mordukhovich 2012，明确 DD2 与既有比较曲线、全锚半单调 PPA 及 Hölder PPA 的重合和量词差异；它把公开优先性保留为未决，不把代数重合写成首创。[P2/P3 扩张审计](research/audit/DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-verification)补充一般势扰动、物理二点恢复和有通信假设的分布式固定步证书，由 [C410](CLAIMS.md#c410)、[C412](CLAIMS.md#c412) 登记。[C411](CLAIMS.md#c411) 给出低 \(L\) 固定图逐步达到，[C413](CLAIMS.md#c413) 排除有限维闭凸目标上的严格步长支收敛锚与可和链。

[DD2 论文选材裁决](research/manuscripts/dd2/DD2_outline_and_pro_handoff.md)比较各开放问题取得实质答案后的数学价值，给五章排法、应用首选及逐项选材。[CP／DR](research/topics/dd2/splitting.md#dd2-splitting-component)给分量充分条件、显式非零位置模及慢收敛的完整算法例；[其他分裂固定步审计](research/audit/DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md)逐式核对 FBF、外梯度和 FRB 的实际步能量及反例。[Inexact DD2](research/topics/dd2/inexact.md#dd2-inexact-absolute)给真图扰动、尾和与临界精度。

[DD1/DD2 与 Alcantara 的同参数比较](research/LITERATURE.md#lit-alcantara-dd) 定位普通 PPA 的共同二次式、分段锐门及退化 PPPA 的恢复条件。[C399](research/canonical/dd2_power_defect_finite_length.md#dd2-power-defect) 从输入距离次单调性缺陷和输出 Hölder 真残差误差界直接推出同一步长度势，给临界常数、半阶无限长度见证及超出线性收敛的非单调原算子。

[从原算子出发的 C322/C323](research/canonical/ppa_native_alignment_and_transverse_test.md) 用标准 Cucker–Smale 完整全隐式场检验 C320：统一耗散预算给所有根收敛，旧 RLEB 即使用实际图值的最紧欧氏球也会失败。对光滑零流形，C323 把 A/C320 精确化为横向奇异值一项检验，量化两次标量化损失，并清楚区分这一结构与抽象统一目标。

[C318 · A 与输入距离步界 B 的必要性](research/canonical/ppa_ab_necessary_bounds.md) 固定普通 PPA 的允许图量词，给出精确一步可行域、A 强制的真线性次正则及锐残差窗，以及固定一般模在全部允许关系上的锐长度预算与 Dini 充要性。完整单值近端同时达到每一步与每条尾的上界。

[普通 PPA 的两步净位移与方向残差](research/canonical/ppa_two_step_and_directional_residual.md) 给出两个已证接口。C319 以两步净位移势推出全部允许轨道的点收敛，容许一步平方和发散。C320 以保留方向的原图值集合替代旧标量整窗兼容，在同一 Dini 基线上严格介于旧结构与 A+B。两者可合取；[C317-v2](research/canonical/ppa_two_step_and_directional_residual.md#td-common-contract) 另恢复非 Dini 下的有限长度子类，并纠正原窄 bump 只攻击全对 RL 的量词。

[C320 定理稿和先行审查](research/audit/C320_MANUSCRIPT_AND_PRIOR_ART_2026-11-18.md) 从对象到留域统一写出两项定理。C321 给出最小图值集合的支持函数判据，并证明完整集合条件严格超出固定线性观察；同页核对 Kruger、Valkonen 等最接近的公开先例。

[C315 · 普通 PPA 的整窗正则性严格弱化](research/canonical/rleb_residual_filtered_angle.md) 在相同 RL 与 Dini 基线下，用线性度量次正则性和一个条件性角度估计替代旧的真实残差误差界与整窗兼容。它证明旧条件蕴含整个新条件，给出完整 Hölder–RL 严格例，并从距离收缩与原 Dini 预算得到有限长度。该页同时定位裸 GMSR、输出相对步长界和 KL 的不同作用。 [与 C277 和 Luke–Tam 的比较](research/canonical/rleb_residual_filtered_angle.md#rfa-comparison) 说明，C315 区分了旧论文的整窗假设，但证明及严格例均可由已有联合证书处理，因此只作为具体证书保留。

**2026-11-17 PPA 下一阶段入口**：[启动报告](research/audit/PPA_NEXT_STAGE_2026-11-17.md)恢复了普通 PPA/GPPA 的 G1–G4、C02-v3/C09 和上传投稿源，并把导师的三个方向固定为三个不同的数学对象。[C309](CLAIMS.md#c309) 用一般函数迭代 \(\Phi^{\circ k}\) 替换固定 \(\kappa^k\)，同时保留精确步长预算 \(\sum B(\Phi^{\circ j}(t))\)；[C311](CLAIMS.md#c311) 从 LMZ v1 Theorem 5.1 重构 exact subgradient PPA 的 KL 有限长度接口；[C310](CLAIMS.md#c310) 以最大单调 \(F(y)=\operatorname{sgn}(y)|y|^\alpha\) 反驳“传统次单调性+MSR 自动推出输出相对步长界 (B)”。三条路线不强行合并；三席独立 RL–KL 审查见 [收口报告](research/audit/RL_KL_THREE_AGENT_REVIEW_2026-11-18.md)，C311 的 exact PPA 与条件式 transfer 已闭；C314 的 full-graph 四周期例子已否证 `RL alone => Lyapunov/H11`，普通 PPA 已有 C315 的整窗弱化，一般 GPPA 与 KL 代替 Dini 仍开放；C313 给出一个已闭合但仍依赖线性 MSR 的非次梯度基准类。本轮原任务见 [GPT Pro 任务书](research/audit/RESEARCH_TASK_PROMPT_2026-11-18.md)：由于 A 强制 LMSR，现在固定 LMSR 为必要基础，寻找新条件 \(\mathcal K\)，使整体正则性包 \(\mathrm{LMSR}+\mathcal K\) 严格弱于 GMSR，并在 RL 下连接到 \(A+B\) 或 KL 望远镜接口。C309 的原生临界模型、一般多值/GPPA Lyapunov 桥和修正版 \(\mathcal P_{\rm TC}\) 仍是活跃义务。

本轮 idea 队列与去重裁决见 [2026-11-15 候选前沿索引](research/audit/IDEA_FRONTIER_2026-11-15.md)。当前最值得继续验证的是 C307 的准解析 Denjoy–Carleman 有界变步 sharp 分界；C308 的周期 SPD 变度量 Floquet 中心流形判据作为第二主线。两者均为 candidate，尚未闭合，不得当作现成定理。

[当前候选前沿](CLAIMS.md#c303)记录本轮三条相互独立的研究入口：二阶阻尼梯度系统的相空间开盆域圆形非收敛（及其变量步惯性 PPA 桥）、纯 Gram GPPA 近端的候选精确 \(3/7\) 两点指数，以及固定 radial-twist 单调反绕行门。它们均保持 candidate 状态；二阶连续证明稿、管估计和离散桥审查分别见 [proof v1](research/topics/path_dynamics/second_order_open_basin_proof_v1.md)、[HJ lemma](research/topics/path_dynamics/hj_tube_estimates_v1.md) 与 [bridge review](research/audit/C303_BRIDGE_REVIEW_ROUND2_2026-11-15.md)。新增的 FNE 管状固定流形方向已由三席独立审查判为淘汰，详见 [C306](CLAIMS.md#c306) 与 [F102](FAILED_ROUTES.md#f102)。读者不得把这些候选当作已闭定理。

[准解析性与精确近端的正则性分界](research/canonical/quasianalytic_proximal_dichotomy.md)给 C302：强对数凸总权重下的一侧有限长度，另一侧用同类 Beurling 势实现所有允许聚点集和严格 Hölder 预算。解析逼近、全阶衰减及文献归属均保留。

[标准 c0 的一般凹模精确位移及固定凸集](research/canonical/holder_minimal_displacement.md#hmd-c0)补 C300–C301。c0 单位球和全域幂模的精确包络由逐坐标非扩张修正和移位屏障闭合；固定 Hilbert 凸集及 Banach 单位球的线性阶另立。

[精确近端与梯度下降的聚点集](research/canonical/exact_proximal_limit_sets.md)给出 C297–C299：同维补分量边界刻画、任意紧连通集的一维提升、严格直径预算下的精确全局近端、标准梯度下降的同轨道对应。Fokin 的连续时间结论及 Noll 近端圆例的范围分别核明。

[三维梯度临界集与固定嵌入的最小预算](research/canonical/gradient_holder_budget.md)给出 C295–C296：proper 临界集的精确梯度 RL 接口、任意严格直径增量可实现，以及临界预算的达到与不达到见证。已知拓扑分类与本轮解析归约分开记录。

[跨点平方误差的精确方差判据](research/canonical/quadratic_cross_approximation.md)登记 C290–C292：异质容差的充要条件、有限维正反近似的准确 Jung 因子，以及固定 Hölder 参数下有限跨点预算的精确判定复杂性和近似界。[独立审查与接续](research/audit/ORIGINAL_DISCOVERY_CHECKPOINT.md)保留。另见[Hölder 最小位移与真值域](research/canonical/holder_minimal_displacement.md)的 C293–C294，归一化最坏缺口的线性阶已闭，首项系数仍开放。

[零集切法几何与线性锐门](research/canonical/rleb_nearest_anchor_geometry.md)补上 C288：仿射目标的精确因子、紧 C² 目标的严格小窗门与临界原近端，解释 C285 高参数最坏类和规则几何子类的阈值差。

[紧零簇的非 Dini 绕行与多项式有界可定义有限长度](research/canonical/rleb_dini_geometry.md)给出 C287-v1/v2 的证明、明确适用域及失败边界：C287-v2 证明同一给定非 Dini \(\omega\) 可作为局部同尺度全对 RL 上界，同时以显式较小内部模 \(\widehat\omega\) 闭合真残差兼容和无限绕行。下一步核更自然的单调/次微分模型、全局尺度延拓，以及是否能让同一模承担半和兼容；不得把局部 pair gate 或内部模偷换成全局单模结论。

[固定核 GPPA 的物理局部指数与原值域条件桥](research/canonical/gppa_physical_local_index.md)给出 C286 的证明、明确适用域及失败边界。下一步核完整 usc acyclic 多值 GPPA 的相应指数，以及可独立验证核差边界门的非平凡原生模型。

[最近零锚 PPA 的精确线性边界](research/canonical/rleb_sharp_linear_frontier.md)用同一步反射、几何可行域及真残差给出 C285 的三支最坏一步因子。低参数旋转与高参数完整闭图二周期分别支撑锐收敛门的两段；C253 继续提供能量充分条件。相关[失败与限度](FAILED_ROUTES.md#f96)及[下一门](RESEARCH_STATE.md#active-frontier)保留连续单值等严格子类。

[投稿口头汇报备讲](发表成果整理/PPA_两日备讲与逐步推导.md)按作者指定顺序组织两日复习、板书推导与追问。它针对本轮英文投稿 zip，逐项区分 Luke–Tam 正式参数、直接/能量分支、旋转锐性的可行域和回缩/指数的附加条件；为教学材料，不改变既有 Claim 状态。

[联合次单调 PPA 研究入口](research/topics/unified_ppa/README.md)新增 C277–C284：原图联合与有限状态证书、两级标量化边界、同预算完整覆盖子类、原始曲管结构及可实施非精确物理接口。它保留 RL 一般模和逆/矩阵方向的不同优势，未宣称完备大一统或新收敛原理；主稿、摘要和正文编号未改。[结果报告](发表成果整理/本轮重构/次单调PPA统一框架_证明与边界_2026-10-14.md)与[6pro精确交接](发表成果整理/本轮重构/6pro_统一次单调PPA_研究交接.md)分别记录已证范围与真正开放目标。

当前作者写作安排见[逐节展开的论文大纲](发表成果整理/论文写作大纲_逐节展开_2026-10-12.md)。现已按该大纲完成[中文 LaTeX 正文及技术附录](发表成果整理/RLEB/README.md)：普通 PPA 为定理2，固定核 GPPA 为独立假设3与定理3，广义单调性比较和零集几何各成一章；现有 Claim 身份不变。第一章保留广义度量次正则与模函数、广义预解式及普通 PPA；固定核推广由独立假设3和定理3陈述。

本轮论文成果见 [发表成果整理](发表成果整理/README.md)：仅保留一个综合写作 Skill；[RLEB–PPA 中文修订稿](发表成果整理/RLEB/README.md) 以一般模普通 PPA 为主定理，幂次推论保留 C02-v3；[C249/C250 固定核物理理论与能量分支](research/canonical/physical_rleb_gppa.md#prg-object) 在主文中作为附带物理提升的推广推论。[C251 自然 Bregman 例](research/canonical/physical_rleb_gppa.md#prg-bregman)、[C252 弱凸圆](research/canonical/physical_rleb_gppa.md#prg-circle)、[C253 线性能量](research/canonical/physical_rleb_gppa.md#prg-linear-energy) 与 [C254 局部指数桥](research/canonical/rleb_kernel_topology_interfaces.md#rkt-local-index) 解释条件。C242 三角例保留，C241 Hamilton 原证明仍在补充稿。

[接续筛选](发表成果整理/应用优势继续筛选.md)撤回C256/C257“经典方法无法分析”的强推荐：[C259](research/canonical/amplitude_classical_energy.md#eca-fixed99)有同窗全部驻点短经典能量证明。当前可采用设计应用为[C260-v2](research/canonical/orthogonal_feedback_rleb.md#ofr-large-window)：未知有界反Hermitian梯度混合、任意模式切换及全部隐式根，原真inf/同锚证书的共同半径提高到10⁻⁴，并另补指定固定/连续模式全域coverage。[C261-v3](research/canonical/smooth_kl_full_relation_obstruction.md#sko-nonsmooth)排共同可定义/强链式locLip单状态ABS-H1/H2；C¹甚至H1自身不可能。但[C262](research/canonical/artificial_kl_energy_bridge.md#akb-theorem)人工非可定义KL能量可导入ABS，禁止全理论排除。[C263](research/canonical/orthogonal_feedback_critical_gate.md#ofc-threshold)给完整远纤维锐门Γ>26m−1≈9.0074及临界恰三输出。它仍是明确反馈设计原型：现成公开算法逐项映射、设备预算和公开优先未认证；不能宣称已满足主证明比原例更短的目标。主稿未替换，C241/C246/C251/C255原作用保留。

继续参数攻击得到 [C257锐正阻尼门](research/canonical/amplitude_circle_damping_threshold.md#damp-tuple)：每个Γ>0都有完全显式共同小圆管与全部输出证书，Γ≤0从精确圆零输入破坏吸收；最坏一步距离商、锐EB–半阶锚积随缩管同趋1/(1+Γ)，所有正阻尼下仍真三分支。完整中心零输入及全局二周期另保留，正阻尼不能推出全域收敛。最大有限窗仍未优化。 接续C259已给每个正Γ的经典局部能量路径，参数数学与显式半径价值保留，不再承担全经典不可解叙事。

导航单位是**定义、精确命题、证明义务、反例与合取关系**。先进入 [动态研究宇宙](visualization/cosmos/index.html)：太阳系承载 RLEB–PPA 主链，其他星域承载相邻方向；行星和卫星按视觉轨道公转，D3 双层力学处理主题星系整组漂移、碰撞与拖动，以及内部非轨道节点的排布。真实跨域超边随天体位置重绘，灰色导航线与数学关系分离。太阳系的 `E02/E03` 等航道仍是原图的**合取超边**，公转和星系形态不表示证明顺序或证据等级。[宇宙语义契约](visualization/COSMOS_SEMANTIC_CONTRACT.md) 与 [宇宙项目说明](visualization/cosmos/README.md) 记录对象对应和增长方式；[Markdown 关系表](research/HYPERGRAPH.md) 与 [graph.json](research/graph.json) 保存精确文字及机读结构，当前有 970 个数学节点、734 条关系。原件在 [history/sources/](history/README.md) 作证据，不充当导航树，也不因标题含“终审”自动成为定理。离线 HTML 内嵌关系数据；进入规范 Markdown 正文的相对链接仍需要完整仓库。GitHub 文件页未必执行 HTML。

**从零继续研究的最短路径**：先读下方 Research Goal 和 Definition Map；再读 [当前活跃问题与完成标准](RESEARCH_STATE.md#active-frontier)，沿本页 Claim Map 的一条**合取**关系进入正文，最后对照 [Claim 精确身份](CLAIMS.md) 与 [现存异议](FAILED_ROUTES.md)。要新增结果按 [增长协议](RESEARCH_PROTOCOL.md) 写入主题目录。下方 File Map 是定位表，不要求顺读 251 个历史原件。

**规范层的独立性门**：一条 `derived-checked` 结论应仅靠所链接的规范定义、正文证明及明确导入的一手定理重建；历史路径只说明它从何而来，不补缺失的假设。仍为 `source-report` 或 `candidate` 的命题不能因 README 有箭头便当作已闭定理。[当前状态](RESEARCH_STATE.md) 只保留活跃义务，旧轮次的时间流水不充当研究前沿。

**这是正在增长的规范研究库。** [研究增长协议](RESEARCH_PROTOCOL.md) 规定新定义、Claim、证明、反例、代码和文献事实的落点；[全库协调验收门](RESEARCH_PROTOCOL.md#global-coordination-gate) 逐项核符号类型、量词、证据与独立性；[来源重构覆盖审计](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md) 逐项记录仍未裁决的旧材料。[全库语义分母计划](research/audit/SEMANTIC_INVENTORY_PLAN.md) 划定来源逐段枚举与数学清洗的两个完成门；[本批清洗与空白接收记录](research/audit/BLIND_RECEIPT_2026-10-07_CLEANUP.md) 保存本批实际阅读范围、修补及完成边界；[GX/AGM 记录](research/audit/BLIND_RECEIPT_2026-10-05_GX_AGM.md) 保存先前范围，较早范围见[10/03 记录](research/audit/BLIND_RECEIPT_2026-10-03.md)。历史材料的清点不等于数学验收。来源清洗的未闭门继续保留；按当前明确研究任务，新增[一般模广义 PPA 融合](research/canonical/generalized_ppa_modulus.md)及其独立接收，不将这批新结果冒充全库清洗完成。

> 当前判断：局部 RLEB–PPA 的收敛机制有可读证明链；总体 RLEB–LT–极大单调的自然母空间规模比较仍开放。Hölder–RL 全局影子、有限维完整纤维分类、固定窗口锐覆盖与有限 QP 已有完整独立规范证明；实际原生认证和外部先行性分别保留门。9/25 局部值域证书的 Lefschetz 引文适用门已核，但仍有独立整窗拓扑假设和候选证明待审。

当前 GPPA 比较的下一入口是[C215改写边界](research/canonical/gppa_reformulation_boundary.md)、[C216正则化稳定性](research/canonical/gppa_regularized_stability.md)及[有界先行审查](research/audit/GPPA_PRIORITY_AUDIT_2026_10_09.md)。源T4正则化距离输出已接入并降低印刷残差预算；现有严格例子的收敛可经保零集改写导入，不能证明任意改写饱和类严格分离。全球首创和[C217总体比较](CLAIMS.md#c217)继续开放。

新的选题入口：[全局完成的拓扑代价](research/canonical/topological_completion_balance.md)把全尺度RL、完整近端吸引和零集拓扑接在同一合同下：局部指数χ(M)与全局总指数1的缺额必须由额外零点补偿。它不反驳任意紧纤维实现。[C233–C235保零完成与全域吸引](research/canonical/zero_preserving_completion.md)现证明：连通管外、允许有限新常数时χ1也充分；不可缩RP²可保整个局部三次RLEB动力和全部零集，但全域趋零在严格投影管下强迫可缩。[C236/C237锐代价与精确预算基准](research/canonical/sharp_completion_cost.md)进一步闭合逐分量缺额、最少一般/非退化补偿数量，以及单点严格球管的原常数完成和全域收敛。[C238–C240预算门](research/canonical/completion_budget_gate.md)进一步给严格插值余量、RP²残余对称障碍及健壮有限证书等价；[C245预算桥](research/canonical/lipschitz_obstruction_budget.md#lob-object)把给定单位方向延拓和正幅度的 Lipschitz 常数转成一个可审计的有限 Hölder 上界；新增[C258有限单纯形证书](research/canonical/simplicial_sphere_budget_certificate.md#ssc-object)进一步把 \(K_e\) 降为半球余量、重心梯度和几何路径常数，本轮[C264显式完成与C265精确原预算](research/canonical/rp2_explicit_completion.md)用旋转交换子直接闭合RP²实际方向场，认证半阶完成预算≤3025/32，并给整个原管L0≈1.53514418989；无需先完成五维剖分。非单点原常数的精确保零完成仍开放。另保留[切向有向面积候选](research/canonical/tangential_area_seed.md)，研究绝对长度之外的点收敛机制。

阶段进展与下一入口：[接收记录](research/audit/ZERO_PRESERVING_COMPLETION_REVIEW_2026_10_11.md)逐项核Hopf条件、非Lipschitz整管拼接、完整前向纤维真残差和全局吸引的独立量词。[后续独立接收与团队路线裁决](research/audit/COMPLETION_BUDGET_REVIEW_2026_10_11.md)已核C236/C237并接收C238–C240；C245 先把预算量化接口固定下来，本轮 C258 将方向延拓改写成有限证书。[C264/C265独立接收](research/audit/RP2_EXPLICIT_COMPLETION_REVIEW_2026_10_12.md)已核实际物理collar、全对常数与原管达等极值。下一关保持整个原管，按幅度加权优化完整位移差商，攻L*=L0（任意增量预算的健壮证书）或严格gap，最后核端点达到；现有大上界不证明gap。

<a id="common-structure-frontier"></a>
## 当前专题：单调性和正则性是否有共同结构

**来源不决定资格。** 已知数学结构若能在本问题中描述并完成所需联系，就可以作为 M；不因工具已知而否决。当前按单调／次单调与正则的强弱补偿机制广筛技术并即时初试，来源、新颖性与适用范围分别记录。

[C396 · 同一目标直线上的四点投影不变量](research/topics/common_structure/orthogonal_projection_four_point_invariant.md)给出本轮修正。若两锚在同一仿射目标直线上，X、Y 为同侧正交投影，则两条接缝平方分解消去 P1P2，得到 XP1²+YP1²−XY²=2XP1·YP2，所以只用四个指定边长的无量纲不变量等于 1。等价地，单调性三角余量 a²−XY²−YP1² 与 PPA 补偿余量 2(XP1·YP2−YP1²) 精确相等。单调性角约束和正则性半径关系只筛选允许构形。若只保留一般不等式而不加这条正交投影结构，则不存在非平凡四量恒等式。

[2026-11-20 教师讨论稿 DD1（Obsidian 版）](research/manuscripts/dd1_2026_11_20/DD1_2026-11-20_教师讨论稿.md) 是对上传讨论稿的可渲染整理，保留 DD1 作为“几何充分条件草稿”的身份。配图把目标集 S 改画为任意闭集合的曲线轮廓；P1、P2 只是两个最近点，连接段不再暗示 S 为直线或存在垂直/平行关系。该稿不新增 Claims 条目，不把充分性、几何尖锐性或开放的必要性升级为规范定理。

[DD1 公开先例核查](research/novelty/DD1_PRIOR_ART_2026-11-20.md) 已确认 Alcantara arXiv:2611.20523v1 明写第二收缩因子，同文步长估计可重建第一因子；半单调根式与缺陷—正则性补偿机制也有更早文献。完整分段锐门及临界构形尚未检出直接外部先例，公开新颖性仍未决。DD1 的固定二次包络与既有 C285 经 \(L=\sqrt{1+4\sigma},\eta=1/\rho\) 对应；竞赛稿严格下降还须补 \(XP_1>0\)，两项上界不能泛称全参数精确因子。核查报告区分原文事实、代数推论及未核范围。

[C398 · 角度加权的仿射投影平衡与维数无关的 τ–L 收缩门](research/topics/common_structure/affine_projection_gram_compensation.md)修正了 C396 的维数范围。仿射子空间上的正确恒等式是 a²+b²−s²=2at cosθ，并有四边长度的 Gram 缺陷；常数 1 只在共同法向或余维一同侧成立。图中 Aτ+BL 的分段 T(L) 则由最近性和三角不等式推出，在任意有限维欧氏空间都有效。完整图量词下 BL 已经是线性 GMSR 的近端重写，不能把这项结果表述成脱离正则性的来源定理。

[C395 · 直线投影四边形的局部不变量](research/topics/common_structure/folded_projection_quadrilateral.md)保留方向许可、圆半径与步边、换锚和前后高度四种数据。直角与平方根半径边界共同给 \(YP_2^3/(YP_1\cdot P_1P_2)=L\)。平方预算由方向三角形推出，折返嵌套保证点极限，普通步长和仍发散。单独放宽两条边界会把该量推向常数的两侧。

[C394 · 固定圆上的四边形不变量](research/topics/common_structure/diameter_chord_quadrilateral.md)给出独立的竞赛几何题。直径上取固定三等分点，作一次弦和半转，变动四边形满足 \(XY^2/(XP_1\cdot YP_2)=1/2\)。相似三角形与托勒密给证明，反复作图趋于直径端点。定比的反向结论刻画相应的共点弦。

[C392–C393 · 两锚角度与完整残差的指数制衡](research/topics/common_structure/angle_residual_exponent_balance.md)把 C390 无量纲化为方向亏损、完整逆正则量、选中图值比例与换锚项。距离侧正则幂 \(p>1\) 与坏角度衰减幂 \(\beta\) 的锐临界线为 \(\beta=p-1\)，临界常数为 \(2A=\lambda c\)。严格侧给平方步长可和。有限零集或两个固定零点的平方距离控制给二维点收敛，显式旋转模型说明绝对长度仍可发散。

[C390–C391 · 两圆的圆幂不变量](research/topics/common_structure/two_circle_power_invariant.md)给出两锚独立移动时的共同不变量。方向投影与交叉切线平方恰好合成根轴位置，根轴到中点的有向距离给出真实平方距离下降。统一根轴余量与完整残差的积分条件推出原 PPA 有限长度，幂型距离侧指数在 \(2\) 处有连续、唯一原根的二维漂移反例。

[C389 · 二维线段与圆盘的分离性质](research/topics/common_structure/planar_segment_separation.md)定义候选 \(M_H\)，同一径向线段保留角度、输出半径和锚距。它给闭图、原根覆盖下的有限长度原 PPA 收敛，允许非线性长度尺度，并覆盖平方根剪切原例。一般 RLEB 的全部原边导入已由同页反例排除，选根导入及两个独立等价恢复仍开放。

[C388 · 两圆与一条射线](research/topics/common_structure/two_circles_common_minimum.md)给出一道独立的平面尺规作图题。两圆交点或角度边界射线的首交点给出同一对最优锚，同时最小化锚边和 \(p_1\) 到射线 \(xy\) 上每一点的距离。证明只用三角不等式、夹角比较及圆的基本性质。

[C387 · 两锚图的平面充要定理](research/topics/common_structure/planar_two_anchor_feasibility.md)固定原步长与输入距离，把同一锚上的方向、一般反射模、完整误差界给出的圆半径及锚边上限消元成输出距离的精确可行区间。每个可行值都能以线段零集达到，且最短锚边与最短反射线段同时达到。按此区间检验距离下降及有限长度预算。

[平面圆与两锚几何](research/topics/common_structure/euclidean_two_anchor_geometry.md)把原近端三角形、误差界圆与输入最近距离圆画在同一张图。C383 给精确锚距区间和直接标锚边的下降式，C384 用反向空球加强原一般反射模，C385 给双空球的锚移锐界，C386 给余维一仿射目标的原 PPA 锐门。经典几何移植与维数限制见正文。

[两锚角度与逆分支](research/topics/common_structure/two_anchor_angle_inverse.md)按作者几何图区分原步三角形与误差界圆。C381 保留输出换锚的平方余量，得到完整真误差界与最近锚方向余弦的两段锐门和长度预算。C382 以同一逆支角度式构造原根并证点收敛，允许非孤立、多值及一般逆模。原一般 RL 的导入仍开放。

[第二批强弱补偿技术储备](research/topics/common_structure/compensation_methods_2.md)将插值、逆映射、变分模型和跨步动力学整理成28张有亲缘关系的技术卡及12项初试。[C377](CLAIMS.md#c377)把完整真残差的K包络同时接到方向比较与一般模距离下剖面；[C378](CLAIMS.md#c378)给局部强逆正则的原PPA端点；[C379](CLAIMS.md#c379)以有符号变差支付非孤立乘积锥中的完整轨道长度；[C380](CLAIMS.md#c380)在弱凸势子类由同一支撑产生残差与一步捕获。每项均明写范围，极大单调端点允许没有定量误差界；一般非孤立类尚不能只用一个标量次正则模定义相反端点。后续深试任务、验证成本和摘要层待核来源同页列出，完整M仍开放。

[强弱补偿的技术初试](research/topics/common_structure/compensation_trials.md)已筛 25 个有亲缘关系的技术入口，展开 10 项证明试验。[C374 的一般模支付门](research/topics/common_structure/compensation_trials.md#truncated-compensation)计算方向亏损与完整残差的尺度交换；[C375 的拟对称转接](research/topics/common_structure/compensation_trials.md#distortion-residual)由跨点方向产生一般残差模，并保留产品型非孤立目标；[C376 的 Carlier 余项](research/topics/common_structure/compensation_trials.md#carlier-original-step)将原、逆 Bregman 差与实际原步写入同一恒等式。[C373 的端点储能](research/topics/common_structure/compensation_trials.md#endpoint-storage)保留大步长负方向的稳定。联合几何、交叉储能、动态乘子等其余初试及断点同页可读，尚未完成一般多值共同结构。

**当前唯一研究提示词**是[GPT_PRO_M_RESEARCH_PROMPT.md](research/topics/common_structure/GPT_PRO_M_RESEARCH_PROMPT.md)：先从本库已掌握的成果推进，外部搜索补具体缺口，最终完成同一 M 的两个恢复与原 PPA 定理。数学方法保持自主；增量角度／拟对称不再被指定为唯一首攻。[发现与筛选安排](research/topics/common_structure/ASSESSMENT.md#discovery-reset)区分阶段成果与完整目标，[文献记录](research/LITERATURE.md#lit-discovery-distortion)保存已核事实，不据此提前判定某路线有效。

[C369–C371 反馈的恢复范围](research/topics/common_structure/gradient_feedback_recovery.md#feedback-recovery) 分别证明两个限定恢复。未知平坦势在线性类精确刻画某个等价内积下单调，正规矩阵类恢复原欧氏单调；完整图有有界可逆增益表示时，同势增长与一般模真误差界等价。缩速不变性和跨位置自由说明一般恢复仍缺何种信息。二次与非线性并不构成这条边界。

[C363 原近端混合闭链](research/topics/common_structure/gradient_feedback_proximal_cycles.md#feedback-original-steps) 先标出可续接原根，再把原弦的模共轭代价加入梯度插值闭链。严格参数下从闭链推出原轨道点收敛和有限长度，无需预设距离收缩或 Dini。[C364](CLAIMS.md#c364) 给出临界绕行及无法覆盖的原 Dini 慢位移，[C365](CLAIMS.md#c365) 关闭同一势精确极小化原步的普遍导入。[C366](CLAIMS.md#c366) 用分数弦闭链进一步得到原根存在，完整的单调性与正则性共同结构仍开放。

[C362 一般模梯度反馈](research/topics/common_structure/gradient_feedback_general_modulus.md#feedback-modulus-cycles) 用闭合链消去未指定的势函数值，给出平坦和凸梯度插值的反馈判据。同一平坦势能实现一条给定几何尺度衰减的扰动近端路径，也能把完整真残差界解释为保目标集的扰动半径。原 C242 的轨道抵消有精确半阶门槛。原算子的轨道生成和两类性质的统一恢复仍开放。

[C361 反馈插值](research/topics/common_structure/gradient_feedback_interpolation.md#feedback-interpolation)给出两点弱单调刻画和固定目标置零代价。[复核](research/topics/common_structure/gradient_feedback_interpolation.md#feedback-review)证明当前全点平坦梯度抵消强制 \(r_F\le Ld\)，其一般 RLEB 导入受到限制；两个反馈测试尚未成为同一 \(M_L\) 的恢复。原 PPA 距离估计对一般闭零集的声明已撤回，保留单点目标及限定参数下的版本。反馈可实现关系中的共同联系仍值得研究，当前状态为候选。

**主问题。** 从原算子图出发，解释单调性与正则性各自约束的几何变化，并找出它们为什么在原近端步中发生联系。候选提出后，再逐条检验哪些既有 PPA 定理能在原假设、允许步长和初值范围下推出同一个 \(M\)。下列旧路线和反例用于检验覆盖及定位失败。[现行任务](research/topics/common_structure/GPT_PRO_M_RESEARCH_PROMPT.md)

[C360 原离散阻尼与原连续流分离](research/topics/common_structure/rleb_discrete_damping_and_flow_obstruction.md#rleb-discrete-damping) 以同一精确非线性近端轮廓给原连续周期与零平面漂移，并在完整认证下实现指定紧流因子。原 PPA 仍点收敛。用于排除普遍的原流趋稳和正定梯度导入。[F127](FAILED_ROUTES.md#f127)

[C359 凸化原近端路径的正则性盲区](research/topics/common_structure/convexified_proximal_paths_obstruction.md#convexified-proximal-paths) 给出两个非线性原 RLEB 算子。完整纤维及每个初值的全部原路径在凸化后相同，完整真残差的最佳误差界幂仍不同。用于检验仅依赖线性支持或凸化路径的恢复定理。[F126](FAILED_ROUTES.md#f126)

[C358 原近端输入误差的切向搬运](research/topics/common_structure/proximal_input_noise_transport.md#input-noise-transport) 对剪切型完整原图计算零点间的精确小误差搬运代价，并对任意原一般模 RLEB 给出可和输入误差条件。真正非线性的幂阈值可锐化，欧氏输入误差可和本身可与有界轨道不点收敛并存。

[C357 的保距离近端共轭反例](research/topics/common_structure/ppa_conjugacy_obstruction.md#ppa-conjugacy) 把 C353 的单调盲区加强到切于恒等的解析原动力共轭，并在另一组共享非线性原 RLEB 数据的原图上分离完整真残差的最佳幂。共同结构的恢复须辨认跨点欧氏方向和原弦长度，见 [F124](FAILED_ROUTES.md#f124)。

**统一结构 \(M\) 尚未找到，C351 的任务验收撤回。** 作者明确排除从原锚点 RL 加误差界出发的相容重写、模消元、局部推广和精确幅度匹配。C351 的数学关系保存，其统一结构探索按失败记录。后续 Pro 要从单调、次单调和正则性的独立含义寻找共同结构，再用它容纳原 RLEB。[现行任务](research/topics/common_structure/GPT_PRO_M_RESEARCH_PROMPT.md) · [F120](FAILED_ROUTES.md#f120)

[C354 的任意局部度障碍](research/topics/common_structure/rleb_degree_and_selection_obstruction.md#rleb-degree) 保持全部原根覆盖和幂最优的非线性反射模与完整真残差模，同时让近端输入映射的局部度独立取任意整数。一般 RLEB 的导入不能依赖非零度或连续选根，见 [F121](FAILED_ROUTES.md#f121)。

[C355 的两步方向实现](research/topics/common_structure/rleb_arbitrary_two_step_directions.md#arbitrary-two-step-directions) 固定完整真残差和每条原弦的全部实剪切长度，在同一非线性原 RLEB 窗口实现任意闭球面两步关系。该证明用来检验候选的跨步方向假设是否真的由原数据决定。见 [F122](FAILED_ROUTES.md#f122)。

[C356 的孤立覆盖步长](research/topics/common_structure/isolated_proximal_coverage_step.md#isolated-coverage-step) 给同一个连续单值原算子的精确满射和零邻域覆盖谱，指定的真正非线性 RLEB 步长在谱中孤立。用于检查参数变形能否承担原近端根的存在。见 [F123](FAILED_ROUTES.md#f123)。

[C350 跨边完整残差与反射损失](research/topics/common_structure/incoming_residual_reflection.md) 将当前完整残差、下一原弦的最近输入零锚偏差及下一完整残差接成精确损失分解，并保持原一般 RLEB 的全部初值。纯点收敛仍可舍去新增方向费用；[F119](FAILED_ROUTES.md#f119) 固定这条路线的承重缺口。

[C345 同纤维反射刚性](research/topics/common_structure/fiber_reflection_rigidity.md) 固定一条阶段性关系：完整真残差下界压缩各真实图值的最优加权反射余量，从而限制同一输出纤维中缩放值差与输入最近零锚差。其证明保留一般非线性模，不改原图、不凸化纤维；当前还不能由跨值关系推出相容或下降，见 [F114](FAILED_ROUTES.md#f114)。

[C346 回返缺口与完整残差](research/topics/common_structure/return_gap_and_loop_reduction.md) 在全锚平方耗散类给出与路径长度无关的正则转接，并证明任意周期的共同零锚误差界来自连续补偿耗散。原最近锚一般反射行的导入仍后置于旧下降；这一区分阻止把循环条件误报为新的共同机制，见 [F115](FAILED_ROUTES.md#f115)。

[C347 保残差最大补全](research/topics/common_structure/residual_preserving_fiber_completion.md) 给当前最直接的对象门：全部原允许 RLEB 数据、完整残差和完整零集保持不变，完整输出纤维仍可填满残差开球以外的所有方向。候选必须区分允许弦的方向与完整纤维的大小；不能默默要求未选图值也有良好方向。

[C348 倾斜纤维的两种恢复](research/topics/common_structure/tilted_fiber_equivalences.md) 证明同一条件在独立范围内分别等价于零锚单调和完整真线性误差界；一般非线性 RLEB 的导入却仍被已有下逆的更强下降支配。两等价是真实阶段成果，固定参数没有关闭共同机制门，见 [F117](FAILED_ROUTES.md#f117)。

[C349 两项尺度匹配](research/topics/common_structure/matching_certificate_reduction.md) 的两条同参数恢复成立，并给一般多值纤维上下端的精确条件；冷审将两恢复归为同一原近端扩张水平。新反射越界机制可从三个必需测试中删掉，故尚不连接到主目标，见 [F118](FAILED_ROUTES.md#f118)。

**此前两条基准的共同收敛证书。** [C341 的补偿锚距条件 M003-v2](research/topics/common_structure/compensated_anchor_convergence.md#ca-definition) 在第 004 轮通过 [G1–G7 独立验收](research/audit/COMMON_STRUCTURE_M_ACCEPTANCE_2026-11-18.md)。投稿原最近输入零锚 RLEB 的一般非线性模、完整真残差、全部允许输出和初值预算原样导入；有限维极大单调 PPA 对完整非空零集和每个固定正步长也可导入。共同引理保证原根无限续接和原点列收敛。[机制层复核](research/audit/COMMON_STRUCTURE_M_ACCEPTANCE_2026-11-18.md#m-mechanism-review) 定位了原 RLEB 先建立旧收缩预算、正则尺度后置的问题，并给出同一旋转原图改变步长的区分检验。

[C342 的同图双门](research/topics/common_structure/compensated_anchor_convergence.md#ca-sharp) 说明为什么这不只是旧 A+B 的改名：一个显式旋转—漂移原场实际点收敛 iff \(\beta>\alpha\)，本证书可认证 iff \(\beta>\alpha,\alpha<2\)。在 \(1\le\alpha<2\) 的严格见证中，任意固定分组的绝对长度都发散；C277 的全锚 Fejér 端与 C329 的宽参数门也单独排除。其他单调–正则组合及公开先行性仍开放。两份有独立内容但未完成自身独立验收的备选证明保留为 [C343](research/topics/common_structure/lifted_residual_distance.md) 与 [C344](research/topics/common_structure/finite_anchor_convergence.md)，状态均为 candidate。

[C340 的同球留域反例](research/topics/common_structure/lt_ball_localization_obstruction.md#lt-ball-counterexample)精确限制 Luke–Tam 正式定理的导入：全部原前提及严格参数门成立，也不保证某个固定零点的同半径欧氏球自覆盖。切向输运是失败原因，实际轨道仍可全局收敛。此例用于核对候选成形后的根覆盖与留域量词。

[早期共用收敛证书的目标与教训](research/topics/common_structure/OBJECTIVE_AND_PITFALLS.md)记录共同充分条件 \(W\) 的数学身份及测试范围。现行任务还要求用同一个几何结构分别恢复两种性质，并由该几何关系解释原步。

[研究导读](research/topics/common_structure/README.md)给出已证数学、失败路线和开放问题。[当前 GPT Pro 研究任务](research/topics/common_structure/GPT_PRO_M_RESEARCH_PROMPT.md)直接说明要找的 M、两个恢复与原 PPA 推论，并带入已经排除的 RL 修补类型。C324 的原图间隙有单调和正则两个切片，但同一零切片仍可对应相反动力学；C325 的残差支撑在次梯度分支给 KL 与真残差的锐幂转换；C326 用活动零锚识别固定切锥漏掉的退化；C327 的原曲复合完整 PPA 可由直接耗散证明，且任意缩窗仍越过 C320 的边界。此前的 [二次移位 Fitzpatrick 母面桥](research/topics/common_structure/mother_fitzpatrick_bridge.md)：同一全图间隙的图截面精确给弱单调，零锚截面在完整近端覆盖下精确给真残差正则；共同近端弦在锚输运和参数条件下给输入版 A+B、点收敛与有限长度，并给出 \(F=B(y)T(Cy)\) 的零集/残差传递和 \(CB(y)\) 定向功。一般观察核仍需对齐或正功条件，不能由标量切片自动补出。

[原非线性 RL 的转接](research/topics/common_structure/nonlinear_rl_bridge.md)保留原反射模。C333 排除固定输出位移惩罚的统一同弦下界；C334 给图宽度、真残差和原近端弦的定量联系；C335 说明标量宽度的正则幂会变差。C336 精确恢复同模延拓的真残差，C337–C339 将困难定位到最近锚的小图值、多尺度数据及多值长支。C329 只作为常数二次弱单调专门结果。

## Research Goal

共同结构线仍要找同一个 \(M\)，证明两类性质在不同条件下是它的两种表现，并据此解释原 PPA 收敛。锚点 RL 与误差界内部的重写及精确匹配已按任务排除，见 [专题状态](RESEARCH_STATE.md)。C341 与 C351 的已证数学内容各自保存。

1. **收敛机制**：固定核完整 GPPA 已接入一般模、残差平方能量与物理提升，见 [C208–C214](research/canonical/generalized_ppa_modulus.md)；在同一图块、真实全纤维残差、coverage 与留域预算下，确定非线性全对 RL 和误差界如何控制 PPA，区分距离收缩与点收敛。
2. **规模比较**：找不以认证参数定义的自然完整原算子空间及有鉴别力的大小量尺，比较 RLEB、Luke–Tam 公共 all-pairs 类与极大单调类。严格多一个例子或特殊层余稠不回答总体规模。
3. **结构与纤维**：全图全尺度 Hölder–RL 下研究一个同时近似正反纤维的强单调影子、固定参数极大图的完整纤维与最优常数。
4. **独立旁支**：冻结面 CRSC→MSCQ、Markov/运输残差与解选择稳定性分别保留自己的对象和量词；跨线连接须证明桥。
5. **随机近端的条件律残差**：在守恒坐标下分类混合不变律，核验真实 law-step 的误差界，同时攻击把逐分支或物理步长当作同一残差的偷换。

## Mathematical Objects 与 Definition Map

定义域、量词、约定在 [foundations.md](research/foundations.md)；跨主题复用的字母、残差类型和统一 \(\mathrm{RL}(\lambda,\gamma,L;R)\) 参数顺序见 [符号与适用域契约](research/NOTATION_CONTRACT.md)。核心坐标为

\[
J_{\lambda F}(p)=\{u:p-u\in\lambda F(u)\},\quad
r_F(u)=\inf_{v\in F(u)}\|v\|,\quad
p=u+\lambda v,\quad C(p)=u-\lambda v .
\]

对同一图块任意**两**图点、同一步长和输入对尺度，全对 RL 写成
\(\|\Delta u-\lambda\Delta v\|\le L\|\Delta u+\lambda\Delta v\|^\gamma\)。
它给部分定义的 Cayley 映射与图块单值 \(J_{\mathcal G}\)，**不提供输入 coverage**。
更完整的[参数与正则性字典](research/canonical/parameter_dictionary.md)把全对/锚定、图块/全图、输入尺度、同图换步与改变关系分开；\(\gamma=1\) 的 tied 曲线包括 \(L=0\) 端点。[非 tied 二参数图](research/canonical/non_tied_cayley.md#nt-object) 另保留交叉项及 \(A>0,\Delta\ge0\) 的门，不能用 tied 曲线代替。真残差 EB 可推选中值界，仍须选中范数落在 gauge 定义域并满足同一 EB 窗；逆向还需完整纤维门。
局部 RLEB 另用实际输出上的 \(d(u,S)\le\psi(r_F(u))\)、兼容及初值长度预算。
全局结构稿取实 Hilbert 空间、非空完整图、\(L>0,0<\gamma<1\)、全部尺度；其中 graph-maximal 固定 \((\lambda,L,\gamma)\)，不是极大单调。有限维完整纤维分类再增加 \(H=\mathbb R^n\)。

完整 GPPA 另固定核 \(v\)，以 \(A(z)=\bigcup_{v(x)=z}F(x)\) 和 \(z=v(x)\) 作精确全纤维 PPA；\(r_A(v(x))\le r_F(x)\)，非单射时不能写等号。新反射量是 \(\Delta v\pm\lambda\Delta f\)，物理步不是核步，详见 [统一入口](research/canonical/generalized_ppa_modulus.md#gpm-objects)。

| 前件 | 后件 | 需要额外检查 |
| --- | --- | --- |
| 全对 RL | Cayley 图坐标、图块内同输入唯一 | 完整或局部输入 coverage 独立 |
| 近对角线全对模 + 闭图 | Minty 自然域闭 | 还需该域在整个空间稠密才得满输入覆盖；完备环境与同一图块 |
| 局部图块 \(J_{\mathcal G}\) | 完整 \(J_{\lambda F}\) | 共同轨道输入域的全纤维一致性 |
| 局部或全时间 \(T\) 观测 | 原关系 \(F\) | 必须保存完整输入与完整输出纤维 |
| 锥 MSCQ | PPA 的真残差 EB | 同一零集及锥残差到 \(r_F\) 的桥 |
| 条件 Markov 残差 | 同步 OT 残差 \(\Psi\) | 同一耦合、目标和回耦损失界 |

## Claim Map 与 Dependency Graph

共同结构的新已证链为：**投稿 P1–P4 与原预算 → C341 的同一个 M；极大单调与完整零集、\(\lambda>0\) → 同一个 M；M 与其静态覆盖及真残差识别 → 原根无限续接、平方步长可和与点收敛。** C342 另提供双门、严格见证和遗漏区；不是这条正向证明的前件。C343/C344 仍为候选，不能以图谱位置代替独立验收。

**首创性查证已形成可审阅结论**：[团队总报告](research/novelty/2026_10_09/README.md)逐项区分先行机制、固定核严格扩张与精确候选；[C218–C220](CLAIMS.md#c218)给既有接口/非calm保真障碍、完整临界共振分类与逆核稳定性分支。全球优先性未认证，具体源位置、已关闭反例和下一缺口均在报告。

本轮可直接接续：[C208–C214 一般模 GPPA](research/canonical/generalized_ppa_modulus.md)包含完整核关系、direct/energy/anchor 三分支、全部正 ASM 源 T2 核包含、非线性强单调核完整严格例、任意指定精确 Q-ν、壳层弱 EB、物理复合 Dini 锐门及误差管；[独立受检范围](research/audit/GPPA_MODULUS_RECEPTION_2026_10_09.md)与[可复算代码](research/code/gppa_modulus/README.md)同时保存。比较固定完整图/算法和 T2 假设类，不宣称整篇外文或全部改写的绝对优越。

完整命题身份、版本、异议在 [CLAIMS.md](CLAIMS.md)。下面是**数学路线而非文件链**；每行的合取和适用域见 [超边表](research/HYPERGRAPH.md)，承重边的量词逐项见 [条件逻辑契约](research/LOGIC_CONTRACTS.md)。

| 路线 | 承重节点及联合前件 | 当前状态 |
| --- | --- | --- |
| 与其他次单调的一般模路线比较 | [同图换参/原函数/逆耗散/矩阵/零锚六路研究](research/novelty/2026_10_14_submonotonicity/README.md)：LT与旧tied类精确同类；同算法diag和GU3示方向关联损失；点收敛、长度、完整多值政策分开 | [独立裁决与综合报告](发表成果整理/本轮重构/不同次单调与一般模路线_比较研究_2026-10-14.md)否定RL普遍最本质/最省，也不支持其他一般模整体取代；新一般D仅候选诊断，既有Claim状态保持，主稿不改。 |
| 非精确 PPA 的完整精度设计 | [C275 停止余量](research/topics/inexact_ppa/real_graph_stopping.md#igs-theorem)：真实图缺陷和反射逆模→可计算距离证书/全部接受输出长度；[C276 锐边界](research/topics/inexact_ppa/sharp_precision_frontier.md#isp-frontier)：完整纤维、有限帽临界、幂次三分界与合法发散政策 | [独立接收](research/audit/INEXACT_PPA_REVIEW_2026_10_13.md)及[复算](research/code/inexact_ppa/README.md)通过内部数学；[价值评判](发表成果整理/本轮重构/非精确PPA迁移_成果与独立评判_2026-10-13.md)仅保留技术贡献。旧非单调/非精确与现代 HPE 正面已核；自然基准有经典恢复，强应用优势及精确优先开放，主稿不改。 |
| 原始模型到完整物理GPPA证书 | [C272法向增长/平坦核](research/canonical/normal_growth_flat_kernel.md#ngf-object)：全域原始不等式→所有驻点root覆盖/定位/同锚/真EB/物理预算和sharp m阶；[C273非零原始Gram](research/canonical/native_gram_structural.md#native-gram-object)：原生核不平移、完整唯一J、解点锐2/3；[C274混合幂核](research/canonical/mixed_power_kernel_structural.md#mixed-power-object)：集合值强凸法向目标、显式limit、非zero切向层sharp q−1 | [结构报告](发表成果整理/本轮重构/结构性验证结果_2026-10-13.md)与[前轮接收](research/audit/STRUCTURAL_VERIFICATION_REVIEW_2026_10_13.md)保留。[理论发展复核](research/novelty/2026_10_13/README.md)新增完整经典恢复：C272全C1共同KL/整个SPD普通PPA，C273全输入对偶PPA/投影，C274部分对偶/整个SPD旧增长。数学有效性保持，创新权重下调；锐composite2/3等精确优先未决。[新反算](research/code/novelty_development/README.md)；不改主稿、不推未知额外zero或默认变度量。 |
| **稀疏恢复的锐自动结构与完整动力学** | [C224–C226](research/topics/sparse_recovery/automatic_regularity.md)：自动active-PD的锐3/2阈值、[C225-v2](research/topics/sparse_recovery/automatic_regularity.md#sr-sharpness-all-p)全部有限p>3/2退化严格极小族与显式完整J/变步线性窗口；[C228](research/topics/sparse_recovery/automatic_regularity.md#sr-wide-ranges)分开strict comp的1<p<2与support独立的全部p>1；[C227](research/topics/sparse_recovery/sharp_instance_dynamics.md)闭合指定p=7/4的锐1/3真EB、完整prox留域、真实非轴慢尾及精确常数；[C229](research/topics/sparse_recovery/sextic_boundary.md)给上侧六阶例锐1/5，[C230](research/topics/sparse_recovery/sharp_instance_dynamics.md#sd-kl)自足证指定例sharp KL3/4与经典阶界 | 数学证明与独立接收已闭，见[集中论文](research/manuscripts/sparse_regularity/sharp_sparse_regularity.tex)。模型/support先行已明确；[优先审查](research/audit/SPARSE_PRIORITY_AUDIT_2026_10_09.md)仍缺Wang–Zhang2017主体与Huo等2023全文。有范围的可审阅投稿候选稿已完成；阈值首次发表仍未认证，须据全文继续判别；不将局部定理扩大成任意初始化收敛或全部上侧统一指数。 |
| 与8月GPPA/NFB的精确关系 | [C199–C207综合比较](research/comparisons/2026_08_gppa_nfb/COMPARISON.md#verdict-table)：真实重合；完整双支→无正则性配对核同轨道障碍；保零集子关系→cap/超线性/log原尾GPPA导入；任意NFB拆分与标准full-graph product→原二次锚 | 已核明确v1与证明范围；物理几何尾自动有限长。完整图不涵盖不等于收敛不可导入；固定核一般模 GPPA 已由 C208–C214 完成；任意其它lift及结构线/全球先行性仍开放 |
| 图值剖面与自然母空间工具 | [C166–C168/C172](research/canonical/operator_profile_tools.md)：完整图值剖面→真残差需取到或右连续门；同一紧对象块闭约束；鲁棒孔洞及双侧实际幂门。[八项构造前沿](research/canonical/operator_space_construction_frontier.md)列清总体比较的实际义务 | 工具证明已重构；没有自动获得自然母空间、孔隙定理或总体规模比较 |
| 有限状态与条件刷新完整接口 | [C169–C171](research/topics/random_markov/finite_state_completion.md)：多面体目标锐证书、三状态支撑识别、四循环真实率和指定标量公式障碍；[C173–C176](research/topics/random_markov/conditional_refresh_interfaces.md)：相关Gibbs、连续可数刷新、三种残差/拓扑分离 | 自足证明及独立复算；目标、同输入最优性、固定边缘和权重门分别保留，条件残差不换成原Ψ |
| 恢复的两种宽母空间薄性 | [C179固定输入AW薄性](research/canonical/attouch_wets_fixed_input_thinness.md#aw-object)、[C180一致映射Hölder薄性与显式证书接口](research/canonical/uniform_holder_thinness.md#uht-object) | 两个不同母空间均有自足证明；固定步长/固定输入与精确S门明列，不转移到任意算法或共同尾子层，不替代总体比较 |
| 自然支撑函数/法锥的完整实例 | [C191](research/canonical/support_normal_natural_class.md#sn-triangular)：全部完整纤维→独立全对RL与真EB→同δ/r严格匹配；法向/切向另给无匹配门的全域长度。[C192](research/canonical/support_normal_natural_class.md#sn-feedback)分开反馈全域存在/全部选择和小条带唯一；[C193](research/canonical/support_normal_natural_class.md#sn-failures)给非退化最佳指数与固定二次锚失败 | 同一原图的推导自足，圆盘解析轨道携τ≥0；全域单值扩大与C={0}漏门有明确反例，工程应用身份仍独立待核 |
| 全局随机近端的选择合同 | [C187–C190](research/canonical/global_proximal_selection.md#npr-objects)：真实物理零参考吸收、共同极小点锚界、a.e.唯一/密度卷积、坐标稀疏全部支撑 | 完整直接证明；全局近端最小解不等于非凸次梯度resolvent，强Feller新核不授予不变律或速率 |
| 相同一步层的相对薄性 | [C186](research/canonical/relative_holder_thinness.md#rht-object)：矩形底边回缩，正Hölder块内低指数扰动仍保全同一一步尾 → H+自身第一纲 | 精确相对结论已证；原生RLEB名称等价仍独立待核，不能推出任意K/S或总体比较 |
| 商拓扑与闭性修补的障碍 | [C177/C178](research/canonical/topological_repair_obstructions.md)：明确germ商非Polish而仍Baire；闭轴/抛物线无局部线性相交界 | 直接证明；不把历史未给原空间/父层的报告当作已证原定理 |
| AGM 与经典共同尾先例 | [C146–C148](research/topics/examples/arithmetic_geometric_mean.md#agm-object) 完整编码→锐真EB/共同几何尾/坏选择，另由同窗配对证明严格兼容失败；[C149](research/canonical/selection_truncation_prior_tools.md#st-lipschitz) 全点Lipschitz+共同增量→Hölder回缩 | 直接证明已重构；AGM输入P与输出D分开，正初值Q二次不跨轴；辅助迭代u与T分开。文献先例只在已核原页范围调用，全球先行性未核 |
| 超线性法向选择 | 完整二支图 C141 + 输出 collar 的全对 γ 模 + 真 EB + 固定小 R 兼容 → 局部严格证书；同图超几何共同尾 + SS-TRANSFER → α 指数上界；固定初值配对的首次切换与 overshoot/饱和尾 → 匹配下界 | [C141 规范正文](research/canonical/selection_superlinear_family.md#sf-object) 在 SF-1–12 的固定参数范围为 `derived-checked`；ν=2、γ=1/2、A=B=1 是 C115/C116 同图特例，ν 与 C139 的 q 不互换 |
| 局部 RLEB | 图块全对 RL + coverage + 最近零点图 + 真实输出 EB → 一步估计；再加兼容 + 留域 → 有限长度；固定零点邻域的严格共同预算 + 同一图块单步模 + SS-TRANSFER → 同球共同尾与两点极限模 | [C02-v2 单值图块证明](research/rleb_ppa.md#r02-proof) 已独立重构，本轮 [C02-v3 真残差多选择版本](research/canonical/true_residual_selection_rleb.md#trs-theorem) 已另立精确身份并证明，历史 C02 其他范围仍候选；[C09/C10/C11 的一般模链](research/canonical/general_modulus_dynamics.md#gm-data) 已完整证明；[C136](research/canonical/solution_selection_rates.md#ss-rleb-ball) 的完整转移可用整个共同轨道窗的纤维等式作为充分门，也可只核全部实际可达输入，不能只核初值球。C137 的完整几何尾图单独由 [GC-3a](research/canonical/selection_geometric_cap.md#gc-certificates) 提供 SS-T1 的单步模，不依赖该图的严格兼容半径 |
| 允许多选择的弱接口 | [C185](research/canonical/allowed_transition_local.md#at-object)：逐输入允许coverage + 逐转移最近锚/所选值EB + 统一距离收缩 + 可和H/严格留域 → 全部允许轨道有限长 | 与C02-v2单值图块、C53真残差各自独立；[F48](FAILED_ROUTES.md#f48)排除所选值向完整真EB的漏量词反推 |
| 指定分支弱接口 | 整球 named coverage + 全家族近似零点锚 + 实际输出真 EB + 小尺度兼容 + 初值留域 → Hilbert 有限长度；零距离锚条件还给局部闭零集 | C53/C54 独立重算；C55 证明此接口不蕴含同指数全对 RL，不可回填 R02 的全对输入 |
| 全对图块到指定锚 | 同图块全对 RL + 指定输入 coverage + 图块零锚对完整零集保距离 → named B/A；实际输出 EB、兼容与留域另接 C53 | C56 条件桥；C57 完整关系说明前两项不能省去零锚保距离，完整排他也独立 |
| 闭图与自然域 | 近对角线全对消失模 + Hilbert 完备 → 闭图 iff Minty 自然域闭；**同一图块闭图** + 自然域在整个空间稠密 → 满覆盖 | C58 独立推导；仅稠密的非闭图仍可为真子域，图块外完整纤维另证 |
| 残差窗口的量词 | 完整真残差窗口 EB + 非减 gauge 在阈值 \(\delta\) 处为正 → 缩邻域后的可评价残差 EB | C59 充分门；平坦 gauge 与闭图仍可窗口真、邻域假，定义域外须另给 gauge |
| 非幂次边界 | 一般模 + Dini + 上述全部局部条件 → 点收敛；对数完整接缝 \(a\le1\) 有距离收缩但点发散 | [C10/GM26–39 完整独立证明](research/canonical/general_modulus_dynamics.md#gm-log-object) |
| 全局结构 | 全图 RL → Cayley；Hilbert 雪花 + 同常数 Lipschitz 扩张 → 固定参数 graph-maximal 完成；二次 excess + 正交提升 + Banach → 单一正反影子 | 扩张 [HE-EXTENSION](research/canonical/holder_extension.md#he-extension) 的量词和一手引文已核；[C03/GSH-1–22](research/canonical/global_shadow.md#gsh-object) 已完整重构；任意 Hilbert 上界与任意维统一锐性闭合，指定锚另有因子 1 |
| 完整纤维 | 有限维闭球满射/properness + 直径界 → 必要性；紧集 fixed-set + Cayley → 充分性 | [C04/FF1–27](research/canonical/finite_fiber_classification.md#ff-object) 已完整证明，两方向分列；不授予无限维必要性或 degree 数值 |
| ℓ¹与概率值域的扩张完成 | C181平稳链平方平滑 + 明确Markov type/对偶目标门 → C182扩张；显式2-Lipschitz概率回缩；同空间Cayley拉回 | [完整证明](research/canonical/l1_markov_extension.md)：Hilbert源0<γ≤1、任意度量源0<γ≤1/2；常数KL/2KL。ℓ¹关系在γ≤1/2完成至满输入，新预算KL，不能反推原预算极大性 |
| 无限维纤维的障碍与补救 | C183平移右移图给单点零集但空正反纤维；同一C另非扩张 + 次线性增长 → C184全纤维非空闭凸弱紧 | [自足反例与证明](research/canonical/infinite_fiber_boundary.md)：每组λ,L>0、0<γ<1的ℓ²反例；非扩张补救限Hilbert，球投影排除范数紧推广。外部328未被导入 |
| 值域与有限数据 | 最大根定位 + 有限维全纤维非空 → 锐值域球；兼容样本 + 同一 QP → 全局代理；再加**同图同尺度** Cayley 参数覆盖、观测噪声界和已认证的反演求值误差 \(e_x\) → 未观测图点三项界 | [C18/FC1–12](research/canonical/full_fiber_coverage.md#fc-object) 的全局与固定窗完整纤维、统一锐性已独立重构；[C19/C20-v2 自足证明](research/canonical/finite_data_proxy.md#fd-object) 在全部样本兼容及同图同尺度门下为 derived-checked；局部 RL 只在每个未知点与所选覆盖样本的点对上使用，全部样本对另须独立兼容；完整纤维须全体在认证图中。[F36](FAILED_ROUTES.md#f36) 反驳漏尺度 v1；QP gap 与 \(e_x\) 的不同见 [F35](FAILED_ROUTES.md#f35)。有限查询不能全空间认证 C21 |
| 拓扑限制 | 局部 all-pairs + EB + Dini + coverage + 不变开域 → 连续极限回缩 | 不由任意紧零集实现自动得到 |
| 去超临界幂的条件值域 | C70 整窗度量余量 + 同一指定 T 非空紧 usc 有理 acyclic + 每阶上同调满射 + χ(A)≠0 → C05-v2 扰动 coincidence 与原关系局部值域；只需 q>0，原稿 C05-v1 的 qγ>1 仍原样保留 | 新版本的条件拓扑链已重算；存在 qγ=1/2 的完整可行实例，原生整窗模型仍须独立认证 |
| 有限数据值域 | [C70 样本双包络](research/canonical/finite_sample_collar.md#fsc-envelope) + **另证**整窗每个输出的步界/EB + collar → 内域余量；再加 usc/acyclic、上同调与 Lefschetz → 原关系局部值域球 | C70 度量层已独立重算；原稿 C05-v1 仍是 PDF-only 候选；C05-v2 是保留整窗拓扑条件而去 qγ>1 的独立条件推导。有限样本不认证整窗 \(T\) |
| 大小比较 | LT 公共接口 → RLEB 能量证书；紧 T-only \(\Phi\) proper；C131 塔给一致回缩，C132 在新定义紧源关系上把输出步界转为真 EB；C133-v1/v2 后继选择保共同尾与同一极限，C134 紧满射非扩张仅有等距变换；C135 给已证闭预算块的紧步长谱上半连续；C142 排除紧图直接充当极大单调成员；还缺自然完整母空间与保纲桥 | [算子空间证明](research/operator_space.md#os-tower-proof) 的 C131–C134 仅在所述紧源前提下成立；[C135](research/operator_space.md#os-spectrum-proof) 尚未对 LT/direct/energy 原生预算块认证闭性和穷尽性；总体规模命题开放 |
| 锥与 Markov | C13 候选路线为冻结秩→面稳定→MSCQ，未闭的独立证明与退化分支明示；同步 OT exact-zero→一般 gauge，有限状态顶点→线性 EB；C143 紧可数模型有统一几何率却无任何正幂 EB；C144 原 OT 残差有局部假零；[C223](research/topics/random_markov/fixed_point_free_no_power.md#fpf-theorem) 无共同固定点且 exact-zero，全部初律相对几何率仍无任何局部正幂 EB | 各自证据状态独立；[两个完整边界证明](research/topics/random_markov/compact_residual_boundaries.md#crb-theorem) 已重构，锥候选与跨线桥不随之升级 |
| 不一致随机近端 | 有限维二次近端 + 正权重 + 固定守恒边缘 + 独立新噪声 → 活跃谱隙 → 条件 \(W_2\) 收缩 → 真实 law-step EB；逐分支残差零集另由共同定点决定 | C22/C23 本轮独立推导；与普通 \(W_2\)、物理步长、Markov 同步缺陷的替换不成立 |
| 规范例库 | 纯旋转：完整 J 严格收缩而 F 无强单调；正紧对角：严格单调+cocoercive 而无任意趋零 gauge EB；三次映射：固定目标/两变量/算法残差的精确模不同 | C24–C26 的三个对象及证明；历史 GX 编号是观察别名，不代表 77 个独立算子 |
| DR 切触与横截 | 同一算法残差 \(I-T\) 在切触线/抛物线有锐半阶 MSR 模 1、无统一一步距离严格收缩；横截两线有全域线性 MR/MSR 模 \(1/\sin\theta\) 和轨道因子 \(\cos\theta\) | C60/C61 是两个对象；不能把算法模换成法锥和的模 |
| 对角竖支闭图 | 完整原图的线性真 EB + 满输入完整近端的线性步 EB + 每选择线性有限长，与零锚 RL 同时成立；同输入跨支碰撞排除任意全对零消失模 | C72–C75/GX-075 独立对象卡；F25 阻断从动力逆推全对 RL |
| 身份与平方并图 | 同一完整 \(F(x)=\{x,x^2\}\) 的真残差锐半阶、完整目标窗两变量半阶 MR、二参数图区域；指定身份近端线性步 EB 与完整最小步半阶分离，跨支同输入碰撞 | C66–C68、C92、C95/GX-068；\(\mu,\rho<0,\mu\rho\ge1/4\) 的区域与 C89 的 \(A>0\) 门不交，不能从 MR 补全对 RL |
| 闭球法锥 | 完整 \(N_B\) 的锐全域非扩张反射与二参数区；固定零目标真空 MSR 系数下确界 0，却无任意正指数两变量 MR/HREG | C93/C94/GX-067、F29；先核域外残差与非孤立零集，不能把真空 EB 当逆稳定 |
| 惰性四状态同步 OT | 固定四点循环、0<p<1、同一输入对唯一不变律的 C-最优耦合 + 同步残差成本 → 精确零集与锐 √(13/p) 线性界；放松内层 OT → 同核假零点 | C71独立重算；[C171](research/topics/random_markov/finite_state_completion.md#fsc-lazy-rate)另给全初律相对几何率及指定标量公式障碍。一般固定有限状态证书见C15/C169，历史执行身份和优先权仍待核 |
| 同核不同随机表示 | 四状态核固定，改为逐状态独立 Bernoulli 的随机映射表示 + 同一 C-最优输入运输 → 同一零集但锐平方系数 13/[p(7−6p)] | [C88](research/topics/random_markov/lazy_cycle_representations.md#lcr-sharp) 新推导；表示会改变同步残差，不能从核身份直接迁移常数 |
| 固定有限状态同步 OT | 固定互异状态及核 + 同一 C-最优耦合 + 全部不变律 + 零成本 tight-edge 顶点行边缘不变 ⇔ 精确零集 ⇔ 全律空间锐线性 EB | [C15 完整证明](research/topics/random_markov/finite_state_certificate.md#fs-theorem) 已独立重写；不需混合性，也不推动力收敛。§5 备用证明和 §6 正则性另有去向 |
| 随机矩门与回耦 | 共同零点与正 excursion + 全部状态的同系数点态界 + \(pq\le r\) ⇔ 全部有限支撑律的标量矩界；另在同一随机表示、同一律类上把收缩 + 原 \(\Psi\) 的输入最优近极小对 + 回耦损失界合取 → 线性 EB | [C126/C127 自足证明](research/topics/random_markov/moment_recoupling.md)；两条是不同接口，条件残差 \(\mathcal R\) 不能替换 \(\Psi\)，原生模型的回耦门仍待认证 |
| 条件刷新两模型 | 固定 \(\nu\) 的有限 bit 以 \(a_*>0\) 刻画 \(\mathsf W_\nu/\mathcal R\) 锐 EB 与统一到目标率；Gaussian Gibbs 在 \(Q\succ0,p_i>0\) 下以 \(\zeta>0\) 给 \(W_{2,Q}/\mathcal R_Q\) 锐 EB | [C129/C130 独立证明](research/topics/random_markov/conditional_refresh.md)；两种状态空间、距离、残差及目标各自闭合，旧 E43 的二进制/Gaussian 节点错接已拆开；均不推出同步 \(\Psi\) 的 EB |
| 非均匀单 bit | 全部可测幅度可实现 + 含原子和端点的强对偶 → 最小非降包络；同一核的精确 law-step → 全初律绝对尾和允许∞的律长度；指定公平 bit 补空间 → 谱余项 | [C145/BIT1–18 独立证明](research/topics/random_markov/one_bit_envelope.md#bit-object)；幂剖面给长度阈值，指数剖面排除每个局部正幂 EB。饱和模、绝对尾、相对率、律长度及样本路径分别量化，不回写为原同步 \(\Psi\) |
| 有限状态残差正则性 | 固定有限数据 + C-最优计划的固定矩阵 Hoffman 界 + 运输成本变化界 → Φ=Ψ² 全域 Lipschitz；有限 tight-edge 分支 → 连续分片仿射 | [C80](research/topics/random_markov/finite_state_certificate.md#fs-regularity) 不要求 C15 的 exact-zero 判据；正则性不推出 EB |
| 正值正弦的错目标边界 | GX-064 完整 F=2+sin x 在 λ=1 的全对临界 1/3 阶与目标 3 的固定目标半阶属于不同参考图点；F 零集为空 | C81/C82 的缩窗锐常数与每选择向负无穷的完整路径已重算；不能拼成零集 PPA |
| 有界平方的锐性与留域边界 | GX-065 完整有界图的全图临界半阶锐性见证在左端点，零点真残差半阶在零点；两界可同窗成立但 \(q\gamma=1/4\) | C83/C84 重算全部锐模；正输入路径仅有 \(1/k\) 衰减，负输入有限步越域；粗指数与缺留域不支持统一零点收敛 |
| 有界负恒等图的步长门 | GX-066 的同一完整图在 \(\lambda=1\) 使全部 Minty 输入塌为零；\(\lambda>2\) 则所有合法近端路径线性收敛，但反射线性模大于 1 | C96/C97 全图锐模与每步自然域重算；固定零目标真 EB、输入覆盖、反射收缩和动力稳定属于不同命题 |
| 斜等距加紧正对角 | 完整 `D+B` 在实 ℓ² 上全域双射，逆映射全局锐线性而强单调与 cocoercivity 模均为零 | C102/C103：直接谐和级数见证非 rectangular；完整近端严格收缩、全对反射锐常数 1，不能相互授予严格性 |
| 有界负平方的全图与路径 | 完整 `-x²` 限在 `[0,1/2]`，步长 1 的全图端点半阶 RL 与零点真残差半阶同时成立 | C100/C101：全图锐常数 2、真 EB 锐常数 1；正侧近端路径有限步越域，不能把两个半阶模当作零点收敛 |
| Volterra 积分的逐点与统一量词 | 完整 L² 图全域近端、全对反射锐 1；零均值方向与高频向量分别见证图几何和残差障碍 | C104/C105：非 rectangular 且任意消失 gauge 的真残差与步残差 EB 均失败；每条近端轨道强收敛，每个有限幂范数仍为 1 |
| 负三次的完整图与图块 | 完整 F=−x³ 的零输入三根否定全对 RL；受限 [−M,M] 在 3λM²<1 才有锐图块线性模 | C106/C107：固定零目标与两目标锐 1/3 系数不同；图块非零路径有限步离开自然域，不能赋给完整多值近端 |
| 孤立极点图与阶梯图 | 前者完整图的零输入纤维按 λ=ε² 分相，后者全图线性 RL 按 λ=δ 分相，亚临界算术类型决定是否有精确碰撞 | C108–C111：真残差任意幂的零下确界模不提供两变量目标覆盖或非零无限路径；阶梯的完整最小步界需对全部 J 纤维取最小 |
| 负平方乘阶梯 | 两完整关系在 Euclidean 直积，线性段全图模取分量最大，但临界半阶的完整乘积最优常数须联合优化 | C112–C114/GX-057：零目标真 EB 锐半阶与仅零路径无限合法；临界全图锐系数严格大于 2，图点输出共同窗才为 2，仅限输入的固定窗仍严格大于 2 |
| 斜旋转法锥的逆像与全图反射 | 二维完整 \(K+N_B\) 的每个目标有唯一原像；全部图点给 \(\|\Delta x\|^2\le2\|\Delta y\|\)；同图另核单调与全部近端纤维 | C98/C99：原算子 MR 的锐半阶；C124/C125：rectangular 而非 paramonotone、完整近端满域，反射全图线性锐常数 1；两个残差坐标分开 |
| 负平方根的图身份门 | GX-032 的短受限图 \(F_U\) 有锐全对 \(L=3\) 与真二次 EB，但任一非零输入仅有一步；半直线母图 \(F_\infty\) 有远支，同输入碰撞 | C85–C87 分别重算两个完整关系，F28 禁止把短图证书与母图或无限轨道拼接 |
| 异维数正则性与两残差 | GX-076 的最近逆点线性但固定/双变量锐半阶；GX-077 的原算子残差跳跃系数下确界 0，但近端步残差锐系数 1 | C76–C79 独立对象卡；不能将 GX-076 赋予同空间 RL，也不能互换原算子与近端残差 |
| 固定目标随机近端 | 同一全局 prox + 域内平稳律 → 吸收支持；非乘积闭近端图 + fair tie 核 → 有限长非不变极限及完整 \(W_2\) 邻域无 law-step gauge EB | C62-v2/C63；从吸收点识别完整单点纤维需每个纤维有限且逐成员正选择，[F37](FAILED_ROUTES.md#f37) 反驳旧 C62-v1；与随机换目标 C22/C23、Markov 同步 OT \(\Psi\) 分离 |
| 非线性矩提升 | 连续非减 gauge + 实际硬支持 + 全部概率律 → 凹包络锐式；同一变量两条点态证书先复合再取矩 | C69 抽象工具；临界分开聚合损失见 F24，原生合法耦合和目标边缘未证 |
| 参数与逻辑转换 | 同图换步：旧 Cayley → \(Q=\alpha I+\beta C\)，新 Cayley 良定 iff \(Q\) 单射；线性 RL → tied 参数曲线；有界输入域高指数→低指数；真残差 EB → 选中值界 | C27–C30 分别限定相同对象、配对与尺度，折叠和分支反例阻断逆向推理 |
| 非 tied 二参数图 | 同图全对 \(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\) + \(A>0,\Delta\ge0\) → 平移 Cayley 球、锐普适反射/近端模；另合取 Hilbert 扩张 → 同参数图极大 iff 满 Minty 域；\(\Delta>0\) 才有可逆单调图变换 | C89–C91 从 9/01 §2.1 重写，步长端点碰撞和母图完整纤维范围均单列 |
| 合法多步路径 | 实际前缀 coverage ∧ 统一终点收缩 ∧ 可求和块内位移 ∧ 初值留域 → 每条轨道有限长收敛；块 RL/输出 EB 只生产终点估计 | C31–C33 已重新证明；无限词逐词指数 >1 不给统一半径，周期相位极限须单独处理 |
| M1 显式动力 | 同一状态的活动关系 \(s=a-3b\) → 球内两步捕获及锐一步距离因子 \(3/\sqrt {10}\) | C38/C39 对给定单值 T 重算；原生多值方程到 T 的桥仍未核，不能声称一步定理严格失败 |
| M1 的新 Sign 实现 | 新定义的全部 \(F_{\rm lift}\) 图值 → 全域完整 \(J_{\lambda F}=T\) 与端点真残差锐线性模 3；指定输入球上全对 RL 最大指数 \(1/3\)；同一个 T → C38/C39 动力可调用 | C64/C65 是新关系；历史原生循环方程缺相位/全部选择，不能认作它 |
| 幂次剪切校准 | 完整三角图与真残差 EB + 有界窗全对 \(\gamma\)-Hölder + 切向余量 → 法向速率精确可达 \(\gamma q\) | C42/GX-071，只是反向构造的可达例；无界全图 RL、普适精确速率都不成立 |
| 振荡剪切分离 | 完整三角图 + 振荡两尺度 → 有界窗最大全对指数 \(\gamma\)；同一映射的双边真实阶为 \(q>\gamma q\) | C43/GX-072，说明全对最坏指数可能保守；归一化 Q 因子未证收敛 |
| 自然域逃逸 | 指定 Minty 域振荡反射 + 锚定 \(\alpha\)、全对 \(\alpha/(\beta+1)\) + 线性真残差 → 非零轨道有限步出域 | C44/GX-073；一步尺度不能称收敛阶，改变域或延拓后是新对象 |
| 孤立零点分支 | 同图 germ 三模平坦性 + 真 EB + 指定输入/输出窗口及小步门 → 上 \(q\) 阶；再加正归一化极限 → 精确 Q 因子 | C45/C46；选中值不倒推真 EB，完整纤维另证 |
| 离散覆盖障碍 | 完整紧图全对 RL + \(S=K\) 上真 EB 仍不提供零点输入球 | C47/GX-074；coverage 独立 |
| 非孤立对齐 | 输出最近零点锚 + 全家族真 EB/小步门 + 正指数统一锚模 → 上 \(\theta q\) 阶；同序列三重饱和才给锐性 | C48、C49-v2、C50-v2；\(B=1/\lambda\) 还需步长趋零，[F38](FAILED_ROUTES.md#f38) 隔离旧量词；无最近点另用正容差 |
| 移动锚反射 | 同一实际图点的真 EB + 输出近锚 + 小残差 → 相对该锚的反射比趋 1；幂型给定量缺陷 | C51/C52；固定锚与集合距离收缩需要别的桥，F18 有反例 |
| 复合次正则 | 原生凸外层 EB ∧ 满行秩定量修复 ∧ 链式残差下界 → 复合真实 EB；再加全部乘子界、步长门、gauge 兼容和留域 → 局部近端有限长 | C34–C37 已重写；尖点外层特例在 C40，秩亏原生推广开放；历史 C11 不等于回缩 C11 |
| 复合模型的独立边界 | 曲面尖点外层 + 真残差间隙 + 局部近端步长门 → 一步识别；光滑驻点极大序列 → 无弱分离时二阶目标 EB 失败 | C40/C41 本轮重算；前者图真多值而局部输出唯一，后者只攻击到 \(\Theta_2\) 的扩大陈述 |

9/14 历史包本身已有 149 个实体、35 条超边；本图以它为搜索种子，读入 9/18–9/25 版本后重新判断，没有把历史边直接升级为当前真理。

[孤立零点平坦性](research/canonical/isolated_zero_flatness.md) 将图 germ 的代数、完整残差纤维、指定分支轨道上阶和正因子的额外极限分开；[GX-074](research/topics/path_dynamics/discrete_coverage.md) 给紧全图仍无 coverage 的见证。

[非孤立对齐](research/canonical/nonisolated_alignment.md) 用输出最近零点的锚距离及最近点漂移解释 \(\theta q\) 上界；无 proximinality 的近似锚与正 Q 因子各有附加门。[F17](FAILED_ROUTES.md#f17) 防止把不同序列的最坏指数相乘。

[移动锚反射](research/canonical/moving_anchor_reflection.md) 的逐图点双边比与幂型常数只围绕随输出选取的 p；线性零集反例使固定锚和集合距离的错误升级可直接检查。

[全对验证器](research/canonical/all_pairs_verifier.md) 划清图块零集与完整零集的距离门；C57 的完整多值图在全对 RL、满输入覆盖和输出真 EB 下仍缺指定锚，并保留远端完整分支。

[闭图与 Minty 自然域](research/canonical/closed_graph_minty_domain.md) 从同一图块的近对角线模证明闭图—闭域等价，并把“域另已稠密”作为满覆盖的承重前提；它不产生残差 EB 或完整图排他。

[残差窗口桥](research/canonical/residual_window_bridge.md) 固定真全纤维残差、gauge 定义域与阈值正性；闭完整图上的扁平 gauge 反例说明一般窗口 EB 不能未经条件改成邻域 EB。[F21](FAILED_ROUTES.md#f21) 保存错误推理的断点。

[指定分支局部定理](research/canonical/named_branch_local.md) 将旧 foundations §4–§5 的 anchored 近似锚、实际真残差 EB、Hilbert 完备性和留域预算写成 C53/C54；[振荡完整图 C55](research/canonical/named_branch_local.md#nb-oscillation) 把它同全对 RL 的逻辑边界具体化。

## Research Frontier

共同结构线的前沿是在原图上直接建立方向亏损、完整正则尺度和步长之间的定量联系，并用它推导可核参数窗或可续原根。[C342](research/topics/common_structure/compensated_anchor_convergence.md#ca-sharp) 的临界步长与切向相消、C322 的同初值分根均可区分候选机制；C343/C344 自身独立审查、修正后的 LT 局部化以及精确公开先行性仍待完成。

**规模比较的开放点**是完整、参数中立、非退化的算子母空间与规模量尺。9/20 的 \(\Phi=(\text{实际尾},\text{实际反射模})\) 在固定紧 T-only 图卡 proper，但 proper/quotient 不推出 category-preserving，局部观测丢失完整 \(F\) 的域外信息。9/21 总账报告普通 Baire、轨道理想与旧动力度量孔隙性同时把目标类判小；原证明恢复情况须逐项核对。详见 [operator_space.md](research/operator_space.md)。

结构主线已有完整可调用证明：[GSH 的同一正反影子及统一锐性](research/canonical/global_shadow.md#gsh-object)、[FF 的完整纤维与任意紧集实现](research/canonical/finite_fiber_classification.md#ff-object)、[FC 的固定窗口全纤维覆盖](research/canonical/full_fiber_coverage.md#fc-object)、[FD 的有限 QP/覆盖/反演](research/canonical/finite_data_proxy.md#fd-object)。有限维满目标由明示 Brouwer 闭球接口证明；来源投影 degree 数值没有纳入本轮。固定维数最优因子、应用对象的实际网与严格数值求值、外部先行性继续分别研究；有限总查询障碍保持确定性、无界域量词。9/25 的 rational morphism Lefschetz 定理现有[逐条件一手核验](research/LITERATURE.md#lit-grn-2002)；有限样本仍只认证包络，不认证整窗 \(T\) 的拓扑性质。9/19 随机推论用到**给定度量完备**，若“Polish”仅按拓扑意义，已有显式反例；见 [holder_structure.md](research/holder_structure.md) H06。

## Known Results、Refuted / Failed、Open Problems

- 本次共同结构接收：[C341–C342](research/topics/common_structure/compensated_anchor_convergence.md) 证明最低两行的同一 M、原点收敛及双锐边界；[C340](research/topics/common_structure/lt_ball_localization_obstruction.md) 只反驳 LT 的同球局部化；[F113](FAILED_ROUTES.md#f113) 反驳将真正则识别弱化成点态非零。C343/C344 保持候选。
- 可直接复核的代数：Cayley 双向坐标、固定步长全域完整 resolvent 的原图反演、同图块内同输入唯一。
- 有证明文本和限定内部审计的研究结果：局部 RLEB、固定紧源 \(\Phi\)、解选择修订版、锥与 Markov 条件命题。候选稿与外部审稿、文献新颖性是独立层。
- 已证伪的扩大陈述：局部 \(J_{\mathcal G}\) 自动等于完整 \(J_{\lambda F}\)；Polish 拓扑性质自动给指定度量完备；proper 即保纲。精确反例和可回收部分见 [FAILED_ROUTES.md](FAILED_ROUTES.md)。
- 尚未解：总体规模比较；9/21 N10 原孔隙否定证明可追溯性；9/25 整窗拓扑模型认证及剩余证明审查；各固定维数影子最优常数；同对象同量词的全球先行性。
- 新的 C22/C23 以完整证明写入[随机近端模块](research/canonical/random_proximal.md)：条件 law-step 与逐分支推前残差具有不同零集；标量例使 EB 的统一常数锐。历史验证器的有限运行记录与证明分开保存。
- [规范例库](research/canonical/example_atlas.md) 已重写 GX-004/009/021 所指的三个对象，分别证明收缩逆推的边界、无限维无 gauge EB、三种局部模的精确常数；其余 GX 性质仍按逐单元义务处理。
- [DR 双对象卡](research/topics/examples/dr_tangency_transversality.md) 从 GX-069/070 重算算法残差的切触/横截锐模；[固定目标随机近端](research/topics/random_markov/proximal_selection_seam.md) 重算吸收、核接缝和真 law-step 障碍。[新 Sign 图](research/topics/path_dynamics/m1_sign_lift.md) 给显式 M1 映射一个可核的完整多值实现，历史原生方程身份仍开放。
- [参数字典](research/canonical/parameter_dictionary.md) 的同图换步公式、\(\gamma=1\) tied 端点、有限尺度换指数、真残差方向及 MR/MSR 量词已分别给证明或反例。它是可调用的条件记录，不替代外部定理的先行性核验。

## Next Actions

从 [DD1–DD2 全量验收清单](research/audit/DD2_ACCEPTANCE_CHECKLIST.md)认领第一项未勾任务。该项签收并确认远端提交后，再认领下一项。清单全部签收后进入下面的研究专题。

### 其他研究专题入口

第 004 轮的共同收敛证明可以直接调用。下一步按 [现行任务与验收](research/topics/common_structure/GPT_PRO_M_RESEARCH_PROMPT.md) 寻找联系单调性与正则性的结构定理，让原一般非线性 RL 真正参与其中。旧文献仅在具体证明需要核对时回查，已掌握的背景不作为默认发现入口。

固定核GPPA首创性以[四路接续裁决](research/novelty/2026_10_09/PRIORITY_FOLLOWUP.md)为当前入口：双方旧算法/收敛骨架、C209标量尾势和SF合法KL导入已查明，C222精确预算全域Lip实现已独立接收。下一步核完整编译、物理政策、锐配对/离散共振的精确发表先行和尚未取得正文，冻结C217保真合同；不将固定核扩展、经典可导性或未命中升级为全球首次。

现行任务和优先次序统一维护在[研究状态的下一轮具体行动](RESEARCH_STATE.md#next-actions)。已核规范链可以承接新研究；历史清洗按实际依赖补齐，不要求全历史验收后才研究。当前新增[公开问题选题与资产接口](research/topics/random_markov/public_necessity_target.md)：随机律收敛与原同步 OT 误差界必要性的精确版本须区分不变目标、残差零集和兼容 gauge；[C223 完整新反例](research/topics/random_markov/fixed_point_free_no_power.md#fpf-theorem) 已关闭无共同固定点且 exact-zero 的正幂必要性版本；[启动提示词](research/topics/random_markov/PUBLIC_NECESSITY_PROMPT.md)可直接接续。新正向模型进展见[C224–C226锐自动正则性](research/topics/sparse_recovery/automatic_regularity.md)；指定上侧真实轨道已由C227闭合；下一门是两篇主体全文的精确先行，而非重复已闭数学义务。总体母空间/量尺和原生认证仍保留各自开放门。新增结果、障碍与版本修订按[增长协议](RESEARCH_PROTOCOL.md)进入对应主题；来源任务继续按[覆盖快照](research/audit/CURRENT_COVERAGE.md)处理，不能重复记已枚举组为未开始，也不能把未证结论当已完成。

## File Map

| 完整路径 | 内容与使用时机 |
| --- | --- |
| [research/topics/dd2/DD2_FINAL_ACCEPTANCE_PROTOCOL.md](research/topics/dd2/DD2_FINAL_ACCEPTANCE_PROTOCOL.md) | 作者原版 DD1–DD2 验收协议，逐字节保存。启动、续接和结束当前主任务前读取，包含 17 节逐问要求、强制交付物和最后六问。 |
| [research/audit/DD2_ACCEPTANCE_CHECKLIST.md](research/audit/DD2_ACCEPTANCE_CHECKLIST.md) | 唯一的逐项工作清单和最终答卷。280 个任务覆盖原协议主项及附加义务，每项保存裁决、结论、证据及复核。 |
| [research/audit/DD2_PRO_START_HERE.md](research/audit/DD2_PRO_START_HERE.md) | 新会话的可复制提示词。用一步近端解释反向补偿，区分指定目标与实际界，并在接续清单前做短自检。 |
| [research/code/dd2/verify_acceptance_checklist.py](research/code/dd2/verify_acceptance_checklist.py) | 核对题面和编号、证据文件、单项暂存及远端提交历史。终结检查要求全部勾选。 |
| [research/audit/DD2_FINAL_ACCEPTANCE.md](research/audit/DD2_FINAL_ACCEPTANCE.md) | 当前验收入口，逐节定位既有数学证据和剩余义务，包含有符号模及不连续模的公式检查、逐问关闭规则和最终交付门。 |
| research/novelty/DD1_PRIOR_ART_2026-11-20.md | 六路公开先例核查：固定 DD1 的正距离量词，逐式比对 Otero–Iusem、almost averaged 框架、Luke–Tam 与 Alcantara 的原文；给出 C285 换参、已存在的估计、未检出的完整分段锐门及可复核检索词。写 DD1 的贡献、引文或修订竞赛题退化条件前读取。 |
| [research/topics/dd2/core.md](research/topics/dd2/core.md) | DD2 主线及 §0 Exact Theorem Statements：公共对象、每边锚量词、真残差评价域，分别列出有符号几何、原模可行域、线性反演、距离、比较尾和及两种长度势版本。核主定理或将一步结论用于实际轨道前先读；C417–C420 的完整证明由本页链接。 |
| [research/canonical/dd2_general_phi_exact.md](research/canonical/dd2_general_phi_exact.md) | C414 有符号一步定理及四点完整证明。G1–G6 对应输入/输出最近性、四个三角、同锚能量与二维两锚坐标；逐一核退化和删除限制的伪数据。核一步公式的几何完整性或准备添加目标结构时先读。 |
| [research/canonical/dd2_function_hypotheses.md](research/canonical/dd2_function_hypotheses.md) | C417–C422、C428–C429 的完整函数条件、包络计算及最优性范围证明。包含非单调真残差联合域、单边与完整前像的严格分离、标量右侧判据、原模位移下界、零余量无限长例和零缺陷固定模积分充要性。另有原残差的一维消元、网格误差证书、前缀最优值等价和完整图/固定目标的严格差距。C428 另给一般有符号下界下的线性真残差精确值、完整图取等及密集变号见证。C429 另核原残差下界与前缀广义逆的等值和正则性，保留反向判定首端归属。核函数假设、计算前提、广义逆端点及距离/长度必要性时读取。 |
| [research/topics/dd2/target_geometry.md](research/topics/dd2/target_geometry.md) | C426–C427 的目标几何与完整图证明。以紧凸线段和同一固定射线实现全部自由单边标量；法向辅助前像保留原真残差、闭图和非正整窗覆盖。另给指定凸四点条件、自由仿射精确域、同参数四级最优值及全域线性取等。研究凸性／仿射性是否改善一步界，或区分逐边与轨道锐性时读取。 |
| [research/topics/dd2/reverse_compensation.md](research/topics/dd2/reverse_compensation.md) | C430–C431 的原真残差双向预算与兼容边界。给定目标后，以危险前缀求允许的 ψ，以非空上端和三个下界条件求允许的有符号 Φ；包含整窗交集、线性标尺、首端见证及正下界完整窗必要性失败。§6 按对象类核必要性，给严格上确界不达例，并以全部前像矛盾证明逐尺度非空不保证完整整窗存在；同参数允许子关系有固定闭图实现。设计下降曲线、反推强度或区分自由标量与共同算子时读取。 |
| [research/canonical/dd2_power_defect_finite_length.md](research/canonical/dd2_power_defect_finite_length.md) | C399 的同一步耗散与幂势证明，包括局部覆盖、留域、点率、临界旋转和无线性次正则的非单调实例。比较 DD2 与线性收敛结果或导入退化 PPPA 前读取。 |
| [research/topics/dd2/lowL_dynamic_sharpness.md](research/topics/dd2/lowL_dynamic_sharpness.md) | C411 在同一闭零集和固定完整图上逐步实现低 \(L<1/2\) 的严格步长支，包含局部孤立零点与无限长度例、闭仿射单步障碍。C413 以相对法锥的统一正向排除一般有限维闭凸目标上的收敛锚链及可和链。研究动态尖锐性、最近锚切换或写主文范围时读取。 |
| [research/audit/DD2_TASK_ACCEPTANCE_MATRIX_2026-11-21.md](research/audit/DD2_TASK_ACCEPTANCE_MATRIX_2026-11-21.md) | 旧交接稿的七项 P0–P3 专项审计，绑定 C407/C408/C410/C411/C412、证明和未闭义务。用作最终协议相应小问的证据。 |
| [research/audit/DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md](research/audit/DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md) | FBF、外梯度和 FRB 的固定步实际能量、残差 lift、欧氏距离反例与交叉项 Lyapunov 作用域；写其他分裂扩展或检查其不能自动统一时读取。 |
| research/topics/common_structure/folded_projection_quadrilateral.md | C395 的方向和平方根半径题设、三条几何长度的不变量、无限续接、平方预算和折返固定点。普通步长发散是一个同题设见证。 |
| research/manuscripts/dd1_2026_11_20/DD1_2026-11-20_教师讨论稿.md | 给老师的 Obsidian 可渲染讨论稿；保留 DD1 的四点几何、分段补偿、充分性证明和开放问题，并嵌入任意闭集合 S 的新示意图。仅作 discussion-draft/source-report，不替代 CLAIMS.md 的规范身份。 |
| research/manuscripts/dd1_2026_11_20/DD1_平面几何竞赛题_题面与标准解.md | 按竞赛标准答案体例重排的题面与解答：题面只给四点条件，证明中依次调用阿波罗尼斯中线定理、泰勒斯定理、阿波罗尼斯圆和沃罗诺伊最近区域，最后给出分段锐补偿函数。 |
| research/audit/DD1_OBSIDIAN_DELIVERY_2026-11-20.md | 记录本轮 Obsidian 语法转换、任意闭集合图示修正、渲染检查和数学边界；用于恢复交付范围，不作为 DD1 的新证明。 |
| research/topics/common_structure/orthogonal_projection_four_point_invariant.md | C396 的修订题设、两次正交分解、只含 XY、YP1、XP1、YP2 的恒等式，以及一般不等式不足以产生不变量的自由度诊断。 |
| research/topics/common_structure/diameter_chord_quadrilateral.md | C394 的纯平面题面、弦平方与两条高的定比、两高收缩和四边形的迭代极限。反向证明确定共点弦。 |
| research/topics/common_structure/angle_residual_exponent_balance.md | C392 的归一化圆幂恒等式、幂指数及常数锐门和原旋转反例。C393 的二维平方和点收敛条件、无限长度收敛原例及近锚方向亏损为零的漂移见证。分别检验指数交换与点收敛时读此页。 |
| research/topics/common_structure/two_circle_power_invariant.md | C390 的竞赛题、圆幂不变量与沿原轨道的精确求和式。C391 给根轴与一般完整误差模的有限长度条件及幂型临界漂移构造。用于从实际四点构形检验方向和正则半径的共同恒等式。 |
| research/topics/common_structure/planar_segment_separation.md | C389 的候选 \(M_H\)、垂足检验、闭图与原根覆盖下的二维有限长度定理、反单调和非线性原例。F134 定位径向线段增添虚拟点的损失。检验这个候选能否导入某个二维原图时读取。 |
| research/topics/common_structure/two_circles_common_minimum.md | C388 的独立平面题面、尺规作图、两个圆的充要构形分类和等号条件。用于理解同一个构形为何同时优化锚边和整条射线上的距离。 |
| research/topics/common_structure/planar_two_anchor_feasibility.md | C387 的平面充要条件、输出距离的可行区间与线段取等构造。需联合检验原一般反射模、完整误差界、夹角与锚边限制，或从逐步距离差建立长度预算时读此页。 |
| research/topics/common_structure/euclidean_two_anchor_geometry.md | C383–C386 的精确两圆弧、短锚边、反向空球原 RL、双正向空球及余维一锐门。包含标注图和经典来源的实际移植清单。检验附加零集几何时读此页。 |
| `research/topics/common_structure/compensation_methods_2.md` | 第二批28张技术卡、12项原对象初试和六组Pro深试义务。保存K完整残差包络及全对RL/值平移比较、强逆端点、图修正覆盖、弱凸增长支付、定向Schur补、识别、窗口根策略、有符号锥和自收缩未来点几何；来源核读深度与原图验证成本分别记录。继续技术收集或逐项深试时先读，不是完整M的完成声明。 |
| `research/topics/common_structure/compensation_trials.md` | 强弱补偿的 25 项技术入口与 10 项实际初试；保存联合方向—幅度集合、C374 一般模截断支付、C375 拟对称校准及产品零集、C376 Carlier 原弦余项、C373 端点 Stein，以及测试变换、供给重标度和动态乘子的具体断点。寻找下一项可迁移技术、比较补偿预算或重试某一步时读此页；来源与证据深度同页可查，不是完整 M 的完成声明。 |
| `research/topics/common_structure/fiber_reflection_rigidity.md` | C345 的加权反射恒等、完整残差下界和同纤维两值锚差估计，含零尺度、零反射和跳跃误差模的处理。用于检查正则尺度如何限制方向，以及区分真实结构推导与旧半和界的再包装；跨值关系承担PPA下降仍开放。 |
| `research/topics/common_structure/convexified_proximal_paths_obstruction.md` | C359：闭图多值算子的同凸纤维、同全部有限和无限凸化原路径、异真误差界幂。给共同原一般模、全部根、非解初值，用于排查凸化丢失的正则信息。 |
| `research/topics/common_structure/rleb_discrete_damping_and_flow_obstruction.md` | C360：同一精确反射与完整真残差下的原连续周期、零平面漂移及任意紧流因子。给完整原根、离散阻尼、局部功形式及梯度表示的严格边界。 |
| `research/topics/common_structure/proximal_input_noise_transport.md` | C358：原输入误差在剪切型零线上的精确小幅搬运代价、临界幂和任意原一般模 RLEB 的可和扰动预算。研究扰动稳定性和切向漂移时读取。 |
| `research/topics/common_structure/return_gap_and_loop_reduction.md` | C346：原允许图的有限回返缺口、全锚平方耗散到完整真残差的双侧转接，以及连续补偿推出周期无关的同锚误差模。包含原一般 RLEB 的原窗连续上包络、完整近极小值覆盖和正共次单调系数；用于防止把既有下降后果当成共同结构。 |
| `research/topics/common_structure/residual_preserving_fiber_completion.md` | C347：保持全部当前原 RLEB 数据、完整零集和真残差的逐点最大纤维补全；给低范数最小功及全部倾斜残差的同时精确下包络。用于审查候选是否从允许图偷升到完整纤维方向，完整截断/闭图等附加结构须另证。 |
| `research/topics/common_structure/tilted_fiber_equivalences.md` | C348：同一完整纤维在零右端与倾斜右端的距离比较、两个精确恢复、原 PPA 充分性及保持原κ的非线性导入。独立审查证明该导入仍被旧下逆的更强余项估计支配；用于区分正确等价与真正承重的共同结构。 |
| `research/topics/common_structure/matching_certificate_reduction.md` | C349：两项尺度排序、完整残差可取阈值、一般法切纤维的精确上下端、同参数单调/正则两恢复及原 PPA 充分性。独立冷审证明新增越界分支可从三条要求链删去，两个恢复均为既有扩张水平，不能据此宣告新共同机制。 |
| `research/topics/common_structure/incoming_residual_reflection.md` | C350：当前完整残差约束下一原弦反射，优化剪切点偏差与所用值的非最小性成为相邻完整残差的非负损失；两种同参标定、原全部初值及正点跳跃模证明齐全。读此文件以使用跨边定量关系，勿把可删方向费用升级为共同结构已完成。 |
| `发表成果整理/本轮重构/C351_结构与条件_重写.md` | C351 的可读正文：用输入、输出、距离和真残差直接写条件 M，展开 A、B 的精确等式及两种恢复，给出不经过广义逆的原模存在性与 PPA 证明。包含强附加条件、锚定与全对单调的区别，以及对原研究期望的范围判断。读 C351 先读此文。 |
| `research/topics/common_structure/GPT_PRO_M_RESEARCH_PROMPT.md` | 当前唯一启动提示词。固定共同 M、两个等价恢复、一般非线性 RL 与原 PPA 目标；说明如何继承仓库、按缺口外搜、避免重复旧理论，并要求少代换、完整量词和清楚说明。方法不预定，阶段成果不冒充任务完成。 |
| `research/topics/common_structure/two_point_scale_compatibility.md` | C351 的完整技术正文：跨位置不等式消去两套原模的存在量词，含边柱距离、两个恢复、原 PPA 全部初值证明及不可删非对角项的原图证明。与 C315 已有的给定模下逆比较，具体恢复前提见重写稿。 |
| `research/audit/C351_TWO_POINT_STRUCTURE_ACCEPTANCE.md` | C351 原验收及撤回记录。保留开壳条件、原模重建、限定恢复和轨道证明的审计，并记录为什么这些推导未解释共同来源。 |
| `research/topics/common_structure/reflection_residual_transfer_candidate.md` | C352：原反射余量对完整残差阈值的有符号平移、跳跃上集、原PPA与偏移球面恢复；包括允许值严格大于完整不达到残差的版本。数学可复用，本路线独立结构终审尚未完成。 |
| `research/topics/common_structure/radial_shear_obstruction.md` | C353：所有实剪切与全部轨道的一步标量长度相同，通常两点单调仍可不同；用以阻止从零锚或一点范数信息无条件升级全对单调。 |
| `research/topics/common_structure/compensated_anchor_convergence.md` | C341–C342 的精确定义和完整证明：原弦锚距上确界、可续根、真正则识别、两条原预算导入、仿射切向预算、旋转族双门及 C277/C329 全部受比合同的反证。要继续扩大共同条件覆盖时首先读取；不能将证书遗漏区写成实际发散。 |
| `research/audit/COMMON_STRUCTURE_M_ACCEPTANCE_2026-11-18.md` | 记录四轮实际候选与 G1–G7 裁决，保留 v1 退化量词反例和 v2 修复、独立重构的承重步骤、有限维/固定步长/完整零集的作用域。审查或提升后续版本时核对。 |
| `research/topics/common_structure/lifted_residual_distance.md` | C343 候选的完整推导：真残差增维、无需连续的静态补偿、仿射精确公式与漂移积分门。未通过自身独立 G7；研究不同残差支付机制或与 C341 的关系时读取。 |
| `research/topics/common_structure/finite_anchor_convergence.md` | C344 候选的有限零锚分点条件、图功预算、壳层访问次数界及同一窗口的全锚反证。需要减少锚检验或分析局部目标识别时读取；更换窗口不能直接继承严格比较。 |
| `research/topics/common_structure/lt_ball_localization_obstruction.md` | C340 的完整线性原图、LT 极大性/真残差/参数门核对、任意球的有理数离球见证及仍成立的显式轨道。导入 LT 局部定理或比较初值域、工作域时先读；修订不得把同球反例升级成实际发散。 |

| 新增研究入口 | 用途 |
| --- | --- |
| [research/canonical/topological_completion_balance.md](research/canonical/topological_completion_balance.md)、[复算](research/code/topological_completion/verify.py) | C231：光滑吸引管/全尺度Holder完成的指数守恒、被迫新增零点与完整球面补偿例；保存整管完整近端动力时读，χ1充分性、一般ENR和精确常数完成仍开放。 |
| [research/canonical/tangential_area_seed.md](research/canonical/tangential_area_seed.md)、[复算](research/code/tangential_area/verify_area.py) | C232候选：同一普通完整PPA的Heisenberg切向有向面积、点/长度分类及显式Abel余项；推进原生交换子判据时读，不当作旧兼容定理反例或已核sharp RL定理。 |
| [公开必要性问题与选题](research/topics/random_markov/public_necessity_target.md)、[启动提示词](research/topics/random_markov/PUBLIC_NECESSITY_PROMPT.md) | 2026/2024 正式公开问题、A/B/C 精确解释、C14/C143/C144 对接和未闭优先义务；GPPA 发布编排与确定性备选。不是整个作者问题已解的声明。 |
| [当前首创性裁决](research/novelty/2026_10_09/PRIORITY_FOLLOWUP.md)、[初次六分工快照](research/novelty/2026_10_09/README.md) | 四路逐篇版本核对、经典可导性/发表优先区分、剩余精确候选和未读门；算法/全尺度结构分开 |
| [C221](research/canonical/gppa_tail_lyapunov_bridge.md)、[C222](research/canonical/sharp_holder_lipschitz_realization.md)、[独立接收](research/audit/PRIORITY_FOLLOWUP_RECEPTION_2026_10_09.md) | 前验标量势、完整SF直接C¹/KL分界、任意Hilbert紧K精确预算全域Lip充分实现；不认证全球先行 |
| [C218](research/canonical/gppa_almost_averaged_bridge.md)、[C219](research/canonical/gppa_spiral_resonance.md)、[C220](research/canonical/gppa_regularized_inverse_branch.md) | 自足证明与域/窗口/完整纤维量词；各有独立审查 |
| [可复算代码和结果](research/code/gppa_novelty/README.md) | 标准库精确与高精度算术、指定轨道、脚本/正文hash；不以有限计算证明无穷结论 |

| 仓库根相对完整路径 | 数学资产、目的、何时读取或更新 |
| --- | --- |
| [research/comparisons/2026_08_gppa_nfb/](research/comparisons/2026_08_gppa_nfb/README.md)、[综合裁决](research/comparisons/2026_08_gppa_nfb/COMPARISON.md) | 固定两篇v1原文/hash/数学基线并复下核同；逐篇原式、非单调重合、无正则性双支障碍、保零集子关系导入、任意NFB拆分必要锚与标准lift压缩；三份指定6.1-sol ultra审查与独立复算。C199–C207为精确接口，结构/纤维线先行性另核。 |
| [research/literature_refresh_2026_10_08.md](research/literature_refresh_2026_10_08.md)、[精确检查](research/code/literature_refresh/check_scope.py) | 2026-10-08 近期文献刷新：GPPA / NFB / Spingarn、KKT EB、Kirszbraun与单调纤维；C197/C198给核坐标和参照扩张边界。定位与候选工具分开，外部全篇 / 全球新颖性未验收。 |
| [research/canonical/isolated_zero_flatness.md](research/canonical/isolated_zero_flatness.md) | IZ-GERM/FIBERS 与 C45/C46：孤立零点的图 germ 换算、真残差全部小纤维门、分支上阶及正 Q 因子的额外极限；研究孤立解 PPA 时读。 |
| [research/canonical/nonisolated_alignment.md](research/canonical/nonisolated_alignment.md) | NA-OBJECT/DRIFT/COMPOSE/APPROX/SHARP 与 C48、C49-v2、C50-v2：非孤立零集的锚漂移、正指数下的统一 gauge 上界、无最近点的正容差修补、同序列锐性；研究 \(\theta q\) 或 tangent drift 时读。旧量词版本及反例在 [F38](FAILED_ROUTES.md#f38)。 |
| [research/canonical/moving_anchor_reflection.md](research/canonical/moving_anchor_reflection.md) | MA-OBJECT/REFLECT/POWER/LIMIT 与 C51/C52：实际图点的输出近锚反射、幂型系数、固定锚及集合收缩反例；把局部 EB 用于反射或选锚时读。 |
| [research/canonical/allowed_transition_local.md](research/canonical/allowed_transition_local.md) | C185允许转移全选择的自足证明、实际幂半径与点R/距离Q区别；零锚可依转移改变，EB只用所选值。遇到候选多选择扩展或从selected EB反推真残差时先读；F48完整图给严格边界。 |
| [research/canonical/named_branch_local.md](research/canonical/named_branch_local.md) | NB-OBJECT/LOCAL/POWER/OSCILLATION 与 C53–C55：Hilbert 空间不取最近点的 anchored 分支收敛、局部闭性、幂次退化门及全对线性 RL 的振荡反例；要将局部 PPA 从全对图块改为指定分支时读。 |
| [research/canonical/all_pairs_verifier.md](research/canonical/all_pairs_verifier.md) | AV-OBJECT/BRIDGE/GAP 与 C56/C57：同图块全对 RL、输入 coverage、零锚保距离三项如何生产指定 B/A，以及缺少保距离的完整多值反例；从 R02 接入 C53 时读。 |
| [research/canonical/closed_graph_minty_domain.md](research/canonical/closed_graph_minty_domain.md) | CG-OBJECT/CLOSURE/BOUNDARY 与 C58：完备 Hilbert 空间内近对角线消失模使图闭 iff 自然输入域闭；只有另证稠密才得满 coverage，且图块不排除完整外纤维。从闭图尝试推出输入存在性时先读。 |
| [research/canonical/residual_window_bridge.md](research/canonical/residual_window_bridge.md) | RW-OBJECT/POSITIVE/FLAT 与 C59：全纤维残差窗口、一般非减 gauge 正阈值下的缩域充分门，以及完整闭图的平坦 gauge 反例；调用 EB 时若残差可能超窗口或 gauge 有限定义域，先读。 |
| [research/canonical/local_range_without_supercriticality.md](research/canonical/local_range_without_supercriticality.md) | C05-v2：在 C70 与整窗拓扑条件已合取时把原稿 qγ>1 降为 q>0 的逐步证明，并给 qγ=1/2 的精确可行 collar；评估局部值域候选时与原稿 v1 并读，不用样本代替整窗认证。 |
| [research/canonical/finite_sample_collar.md](research/canonical/finite_sample_collar.md) | C70：9/25 §8 的实际样本距离上下包络和需要**全部整窗输出**条件的留域余量；证明不调用拓扑定理。读 C05 前先区分样本认证、分析余量、原稿 C05-v1 的候选状态及 C05-v2 已重算的条件拓扑链；原生模型整窗认证仍开放。 |
| [research/topics/path_dynamics/discrete_coverage.md](research/topics/path_dynamics/discrete_coverage.md) | C47/GX-074：紧完整图的全对 RL、真 EB 与自然 Minty 域缺口；从图模推输入存在性时读。 |
| [research/topics/path_dynamics/second_order_open_basin_proof_v1.md](research/topics/path_dynamics/second_order_open_basin_proof_v1.md)、[HJ 管估计引理](research/topics/path_dynamics/hj_tube_estimates_v1.md) | C303：HJ 二阶阻尼系统的开盆域圆形非收敛候选及其首次离开 bootstrap；估计引理核 (q_\vartheta,q_r)、边界内漂移、Hessian 和 cutoff 尾部分离。保持 `candidate`，仍缺原式逐字接收、外部优先性和 PPA/GPPA 离散桥。 |
| [research/c303_discrete_bridge.md](research/c303_discrete_bridge.md)、[v2](research/c303_discrete_bridge_v2.md)、[v3](research/c303_discrete_bridge_v3.md)、[v4](research/c303_discrete_bridge_v4.md) | C303 离散桥候选：变量步隐式惯性 PPA、全局 resolvent coverage、\(w_k=O(h_k)\) 递推和连续步长参数的跨壁 barrier；v3 将步长门改为先证多项式指数再选 \(\alpha\)。v4 已条件性闭合角度 schedule 门；仍未闭统一余项、cutoff 全局导数和完整开集量词。 |
| [research/c303_global_bounds.md](research/c303_global_bounds.md) | C303 全局导数与完整 resolvent 覆盖引理：在 source-conditional 的全局 C∞ cutoff 延拓下，HJ 物理支撑落在固定紧环带，\(f\in C^\infty\) 给出 \(g,H,D^3f\) 统一界，\(I+\lambda\nabla\chi_a\) 在小步长下全域单值满射；不承担尾管留域或离散开盆结论。 |
| [research/c303_normal_error_recursion.md](research/c303_normal_error_recursion.md)、[research/c303_tau_common_tail_v5.md](research/c303_tau_common_tail_v5.md)、[有限前缀共同余量](research/c303_finite_prefix_margin.md)、[transient 角度误差](research/c303_transient_angular_error.md) | C303 条件性公共尾管审计：精确 \(w\)-矩阵恒等式、共同 \(O(h_k)\) 误差、\(\tau\)-路径首接触、无循环 \(\alpha>2/3\) 角度超解；有限前缀计算本身已条件性扩展到固定 \(\alpha<1\)。outer-strip 尾分离已有 cutoff-free 条件门，源身份和首接触几何常数仍需核对。 |
| [research/audit/C303_FINITE_PREFIX_W_EXTENSION_REVIEW_2026-11-15.md](research/audit/C303_FINITE_PREFIX_W_EXTENSION_REVIEW_2026-11-15.md) | 独立核查固定 \(1/2<\alpha<1\) 下 finite-prefix 的 \(K_*\)、\(T_{\rm tr}\le T_*\) 与共同初始开集量词；允许速度半径随 \(h_0^2\) 缩小，裁决为 source-conditional / continue validation。 |
| [research/audit/C303_FINITE_PREFIX_ALPHA_SCOPE_REVIEW_2026-11-15.md](research/audit/C303_FINITE_PREFIX_ALPHA_SCOPE_REVIEW_2026-11-15.md) | 独立量词审查：固定 \(\alpha\in(1/2,1)\) 时 \(T_{\rm tr}\le T_*\) 可由阈值代数得到，但初始速度半径依赖 \(h_0^2\)，且不覆盖无界 lifted angle；裁决为 continue validation。 |
| [research/audit/C303_MAJOR_CONTRIBUTION_FRONTIER_REVIEW_2026-11-15.md](research/audit/C303_MAJOR_CONTRIBUTION_FRONTIER_REVIEW_2026-11-15.md) | 三席独立主要贡献门复核：Truth 条件性、Value 可能实质、Novelty provisional、Ambition 保留；source/lift、完整离散留域和外部优先性仍阻止“达到主要贡献标准”。 |
| [C303 瞬态量词独立审查](research/audit/C303_TRANSIENT_QUANTIFIER_REVIEW_2026-11-15.md) | 独立复核 TE/FP/OS 的双侧角度界、\(K_*/T_{\rm tr}\) 合并和共同停止域；post-review ledger 记录已修补的形式门及仍未闭的 HJ cutoff/outer-strip 源义务。 |
| [research/c303_outer_strip_gate.md](research/c303_outer_strip_gate.md) | C303 的 cutoff-free normalized outer-strip 构造：显式 \(\Pi\) 支撑分离、\(q_r=O(e^\vartheta)\) 与角度包络下的首接触前条带包含；需再核 HJ cutoff 自由选择和全局平坦延拓。 |
| [research/c303_hj_cutoff_construction.md](research/c303_hj_cutoff_construction.md) | C303 HJ cutoff source gate：把 HJ 明示的连通 support 条件改写成位于初始外环带的紧连通 (C^\infty) dumbbell，并证明其与整个 normalized 尾条带分离；仍需逐字排除原文未摘录的额外 cutoff 约束。 |
| [research/audit/C303_HJ_SOURCE_AUDIT_2026-11-15.md](research/audit/C303_HJ_SOURCE_AUDIT_2026-11-15.md) | 一手 HJ source audit：修补 \(\theta_{\rm supp}\in(0,2\pi)\) 的 cutoff 几何，并记录原文 \(X:=\nabla f\) 与显式 \(Y=-\nabla f\) 的身份符号不一致；source/lift/\(\beta\) 身份仍待闭合。 |
| [research/audit/C303_PRIORITY_AUDIT_2026-11-15.md](research/audit/C303_PRIORITY_AUDIT_2026-11-15.md) | 外部一手优先性复核：generic inertial PPA/隐式二阶格式已有先例；C303 潜在新颖性只能放在同一 HJ \(F=\nabla\chi_a\) 的变量步开盆非收敛定理，EP/W 局部引理不单独授予四大级优先。 |
| [research/c303_common_stopping_domain.md](research/c303_common_stopping_domain.md) | C303 conditional merge：把核心管、cutoff-free outer strip、transient angle bootstrap 和 \(\tau\)-path 首接触写成同一最小指标停止域；保留共同停止域、source cutoff 与 lift/injectivity 的未闭条件。 |
| [research/c303_exact_endpoint_barrier.md](research/c303_exact_endpoint_barrier.md) | C303 exact endpoint identity (EP1–EP4) 与极角增量 (EP7–EP8)：可替代导数定义的 CS5/TE2，但平面 face 反例证明 \(q_k\) 项不能删除，仍需 \(q_k+h_k=o(m_{\rm face}(\theta_k))\) 与 \(q_k+h_k=o(\phi(\theta_k))\)，以及 source gates。 |
| [research/audit/C303_EXACT_ENDPOINT_BARRIER_REVIEW_2026-11-15.md](research/audit/C303_EXACT_ENDPOINT_BARRIER_REVIEW_2026-11-15.md) | 独立复核 EP1–EP8：代数成立，但要求 \(I-\beta H\) 在整个缩放同伦上统一可逆，并保留 radial margin 与 \(q_k\) 同域；裁决为 partial replacement / continue validation。 |
| [research/audit/C303_COMMON_STOPPING_DOMAIN_REVIEW_2026-11-15.md](research/audit/C303_COMMON_STOPPING_DOMAIN_REVIEW_2026-11-15.md) | 两轮独立审查记录 CS4 的停时量词、\(K/j\) off-by-one、\(h_j e^{\theta_j}\) 一致界和仍未闭的 HJ source/lift gates；裁决为 continue validation。 |
| [research/c303_sharp_schedule_bootstrap.md](research/c303_sharp_schedule_bootstrap.md) | C303 新候选：以 \(W_k=\exp(z_k^2)\) 和 \(S(t)=K(1+t)\log(e+t)\) 替代旧的 \(\exp(z_k^2/2)\) 超解，把首接触充分步长门从 \(\alpha>2/3\) 推到条件性的任意 \(1/2<\alpha<1\)；并记录了 \(\alpha=1/2\) 时现有 \(O(h_k)\) 首接触余项与 \(\phi(\theta_k)\asymp[(1+t_k)\sqrt{\log t_k}]^{-1}\) 的临界障碍。依赖双侧角度估计、共同停止域和 source gate，尚无优先性结论。 |
| [research/audit/C303_W_SCHEDULE_COMMON_DOMAIN_REVIEW_2026-11-15.md](research/audit/C303_W_SCHEDULE_COMMON_DOMAIN_REVIEW_2026-11-15.md)、[独立比率复核](research/audit/C303_SHARP_SCHEDULE_COMMON_DOMAIN_REVIEW_2026-11-15.md) | W 超解接入 CS3–CS7 的条件性接口：固定 \(\alpha>1/2\) 后选 \(\varepsilon\)，保留 transient 与统一 \(T_{\rm tr}\le T_*\) 义务，并给出 \(\alpha=1/2\) 的对数障碍；两份文件是详细接口与独立复核，不升级 C303。 |
| [research/audit/HJ_SECOND_ORDER_FINAL_REVIEW_2026-11-15.md](research/audit/HJ_SECOND_ORDER_FINAL_REVIEW_2026-11-15.md) | 三席最终复核：动力学符号/首次接触无新致命异议，Truth/Value 高但 Ambition 尚为 ODE；决定下一步必须攻离散桥。 |
| [research/fne_falsification.md](research/fne_falsification.md)、[FNE 短弦审查](research/audit/FNE_TUBULAR_INDEPENDENT_REVIEW_2026-11-15.md) | C306/F102：FNE 固定点 Fejér 恒等式、(q)-距离收缩的有限长度 scope lemma，以及曲固定流形短弦/零第二基本形式障碍；主要贡献候选已淘汰。 |
| [research/HYPERGRAPH.md](research/HYPERGRAPH.md)、[research/graph.json](research/graph.json) | 精确文字关系与机读节点边。数学 Claim 或条件边变化时按规范正文改图并运行 [research/build_graph.py](research/build_graph.py)；表现层只消费图，不能从景观倒推数学状态。 |
| [visualization/cosmos/](visualization/cosmos/README.md)、[动态宇宙](visualization/cosmos/index.html)、[像素舰船与星球图鉴](visualization/cosmos/art/contact-sheet.png)、[语义契约](visualization/COSMOS_SEMANTIC_CONTRACT.md) | 当前研究图的动态视图：原图 JSON、固定语义锚点、D3 力学、真实图节点的公转、合取阵点及沿正向航道运动的多构型舰船。20 种结构船型和 12 种星球地貌有可再生的 SVG 与多尺度接触表；造型不评级数学状态。新增或修订超边后运行 `build.py`，核对布局及关系回归。 |
| [visualization/xianxia/](visualization/xianxia/README.md)、[物件图鉴](visualization/xianxia/gallery.html)、[数学山海图](visualization/xianxia/index.html)、[增长交接](visualization/xianxia/HANDOFF.md) | 上一版修仙视觉实验，保留可编辑 SVG、静态世界清单与离线 HTML 供设计对照；新宇宙视图在 `visualization/cosmos/` 独立维护。 |
| [research/map.html](research/map.html)、[research/map/](research/map/) | 更早的像素探索图与可再生前端源码，保留作兼容和设计对照；精确关系仍以 `research/graph.json`、规范正文及 `CLAIMS.md` 为准。 |
| [research/LOGIC_CONTRACTS.md](research/LOGIC_CONTRACTS.md) | 关键超边的固定对象、量词、合取 side conditions 与不蕴含；使用跨稿箭头或改 Claim 版本时先核。 |
| [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md)、[research/validate_assets.py](research/validate_assets.py) | 新资产的精确身份、状态、证据与生长门槛；结构检查哈希、图目标和规范链接。新 Claim 进入前后读协议并执行校验。 |
| [research/foundations.md](research/foundations.md) | D01–D04 的关系、剪切、真残差、局部/完整区别；遇到定义混用先读。 |
| [research/canonical/generalized_ppa_modulus.md](research/canonical/generalized_ppa_modulus.md)、[完整研究稿](research/manuscripts/gppa_modulus/gppa_modulus.pdf) | C208–C214 广义 PPA 融合入口与集中完整证明；数学源稿、独立审查与复算从入口可找。 |
| [research/topics/inexact_ppa/README.md](research/topics/inexact_ppa/README.md) | C275 真实图停止合同/C276 完整精度边界的短入口；独立规范证明、完整纤维、锐政策、自然基准、逐篇先行性、反审与代码分别定位。仅技术贡献内部已核，不宣称强应用优势或整个经典排除。 |
| [research/novelty/2026_10_14_submonotonicity/README.md](research/novelty/2026_10_14_submonotonicity/README.md) | 同名次单调的原始结构、完整算法与一般函数化比较；五路源审查/数学报告、Astra独立反审、同算法严格优势、任意scalar压缩盲区和复算。读后按原模型选择入口，不按术语宣布冠军。 |
| [research/canonical/gppa_reformulation_boundary.md](research/canonical/gppa_reformulation_boundary.md) | C215完整二维SF正盆地共轭、精确物理阶与变坐标线性率、全空间resolvent身份引理；定义C217保真改写量词，避免把同图排除当所有改写排除。 |
| [research/canonical/gppa_regularized_stability.md](research/canonical/gppa_regularized_stability.md) | C216真实精确输出的原残差抵消、跳跃gauge距离管、源T4的正则化双极限包含和更紧残差预算；补充C213，保留点/长度边界。 |
| [research/audit/GPPA_PRIORITY_AUDIT_2026_10_09.md](research/audit/GPPA_PRIORITY_AUDIT_2026_10_09.md)、[research/code/gppa_scope/README.md](research/code/gppa_scope/README.md) | 有界先行来源、实际阅读位置及未闭新颖性义务；新证明的参数、双精度尾和、Fraction反代及scope复算。 |
| [research/rleb_ppa.md](research/rleb_ppa.md) | R01–R04：一步估计、两种证书、局部收敛、signed-Schur 验证和接缝；研究 PPA 假设时读。 |
| [research/canonical/rleb_residual_filtered_angle.md](research/canonical/rleb_residual_filtered_angle.md) | C315：普通 PPA 中用真实残差标尺决定在哪些图点检验最近零锚弱 Minty 角度。含旧包到新包、全图严格例、相同残差场的失败伴例和 Dini 长度接口。核对 GMSR 弱化或将其转入固定核 GPPA 时先读。 |
| [research/canonical/ppa_two_step_and_directional_residual.md](research/canonical/ppa_two_step_and_directional_residual.md) | C319、C320、C317-v2：两步净位移的留域与点收敛、保方向的完整图值误差界、固定窗的严格层级，以及同一旧单步结构下的三类动力学；适用于比较绝对可和与点收敛。 |
| [research/canonical/ppa_ab_necessary_bounds.md](research/canonical/ppa_ab_necessary_bounds.md) | C318：输入距离步界与距离收缩的锐一步域、全图残差量词、固定模长度极值及紧零集反例。研究 A/B 的逆向含义时与 C09、C10、C287 同读。 |
| [research/canonical/general_modulus_dynamics.md](research/canonical/general_modulus_dynamics.md) | C09/C10/C11：同图块一般模的完整Dini/严格预算证明；对数完整双支的真残差、全对非幂模与a=1边界；开域剩余预算、全域统一尾和显式局部同伦。 |
| [research/canonical/rleb_dini_geometry.md](research/canonical/rleb_dini_geometry.md)、[C287-v2 接收](research/audit/C287_V2_REVIEW_2026-11-14.md) | C287-v1 的紧圆非 Dini 绕行与可定义幂步界；C287-v2 进一步给同一指定 \(\omega\) 的局部同尺度全对 RL，上界与 RLEB 兼容内部模 \(\widehat\omega\) 分开。读 Dini 必要性、紧目标聚点和 pair-gate 量词时使用；自然单调模型与同模半和兼容仍开放。 |
| [research/canonical/global_shadow.md](research/canonical/global_shadow.md)、[finite_fiber_classification.md](research/canonical/finite_fiber_classification.md)、[full_fiber_coverage.md](research/canonical/full_fiber_coverage.md) | C03/C04/C18 的独立完整证明：非可分 Hilbert 同一正反影子与统一最优因子；有限维所有目标、proper 与任意紧集双向实现；最大根、固定窗完整纤维与开球锐性。无锚、指定锚和有限维必要性分别量化。 |
| [research/holder_structure.md](research/holder_structure.md) | H01–H07：影子、纤维分类、Dini、回缩、随机完备性反例、9/25 值域候选；审结构或局部拓扑时读。 |
| [research/LITERATURE.md](research/LITERATURE.md)、[research/canonical/holder_extension.md](research/canonical/holder_extension.md) | LIT-GRN-2002核C05拓扑门；LIT-ALM-2021及HE核Hilbert同常数扩张。LIT-OAI-CATALOG-2026的332实数主链现由C181重构，LIT-MN-EXTENSION的全部导入门支撑C182；其余五稿、复数/Lean/全球先行性仍未验收。 |
| [research/canonical/l1_markov_extension.md](research/canonical/l1_markov_extension.md) | C181的3024平稳链平滑；C182的Hilbert/任意度量半阶ℓ¹扩张、概率值域与新预算满输入关系完成。常数、目标、完整纤维及原生残差边界明确。 |
| [research/canonical/relative_holder_thinness.md](research/canonical/relative_holder_thinness.md) | C186固定矩形/底边一步回缩的正Hölder类自身第一纲；低指数扰动保持值域、回缩、精确固定集及同一尾预算。研究相对纲、全时间子层或源B2时读，不将环境第一纲与子集自身第一纲混同。 |
| [research/canonical/infinite_fiber_boundary.md](research/canonical/infinite_fiber_boundary.md) | C183每组参数的单点零集空纤维完整图；C184额外非扩张下的任意Hilbert非空弱紧纤维与非范数紧球投影。补上C04无限维必要性的真实边界。 |
| [research/range_finite_data.md](research/range_finite_data.md) | W01/Q01–Q04/B01：9/23 的锐值域球、固定窗口、同一有限 QP、参数覆盖、三项误差、有限查询障碍与 deadband；[Q03](research/range_finite_data.md#q-eval) 分开 QP 输出误差 \(e_N\) 与反演求值证书 \(e_x\)，要从结构定理走向可计算证书时读。 |
| [research/solution_selection.md](research/solution_selection.md)、[solution_selection_rates.md](research/canonical/solution_selection_rates.md)、[selection_geometric_cap.md](research/canonical/selection_geometric_cap.md)、[selection_geometric_sharpness.md](research/canonical/selection_geometric_sharpness.md)、[selection_parameter_family.md](research/canonical/selection_parameter_family.md)、[selection_tangential_condition.md](research/canonical/selection_tangential_condition.md)、[selection_superlinear_family.md](research/canonical/selection_superlinear_family.md) | S01–S03、C08、C115/C116、C136–C141：统一尾有限前缀的尺度证明；R01/R02 到同球共同轨道窗及完整近端的逐纤维门；**两种不同**完整二支模型分别给几何尾与 Q 二次尾。C137 的 §2 几何图有全对 RL、真 EB、固定兼容半径和共同尾；C138 的 §3 首次切换给同一图匹配配对下界。C139 推广到任意 0<γ,q<1 的同族证书与匹配阶；C140 则独立给出衰减切向敏感度恢复混合稳定性的充分门及尖点边界；C141 是已按 SF-1–12 独立重建的任意 ν>1 超线性法向族，逐轨道 Q-ν 与两点伸缩指数的量词分开。研究初值到极限解稳定性时读。 |
| [research/canonical/signed_schur_growth.md](research/canonical/signed_schur_growth.md) | C117–C119-v2：双支 signed-Schur 的闭参数域图包含、切向球内全对模与完整纤维门；幂次/同修正坐标匹配、平方根原生图、显式 Whitney 反例、全纤维/图册门及未恢复前驱版本边界。核局部 R04 或把图块结论转成完整近端前读。 |
| [research/operator_space.md](research/operator_space.md)、[固定紧源观测证明](research/canonical/compact_t_observation.md#ct-proper) | LT 嵌入、完整图信息、\(\Phi\) 的自足 proper 证明、C131–C134 四条紧源条件证明，以及 C135 闭预算关系的紧步长谱引理；原关系 \(F_{T,K}\) 的域是 \(T(K)\)，其近端输入域才是 \(K\)；[C142](research/operator_space.md#os-compact-barrier) 的显式加点证明表明此紧图不能直接属于非零 Hilbert 的极大单调类。若要把 C135 用于 LT/direct/energy，先分别核预算块闭性与证书穷尽；总体比较工作入口。 |
| [research/canonical/sigma_compact_baire.md](research/canonical/sigma_compact_baire.md#sc-proof) | C128：已给定 σ-紧度量空间的 Baire 等价判据；判据不替目标算子空间构造紧层或证明保纲。 |
| [research/cone_markov.md](research/cone_markov.md) | 锥秩–面–MSCQ 和 Markov 同步/条件残差链、反例与跨线桥；研究旁支时读。 |
| [research/topics/random_markov/conditional_refresh.md](research/topics/random_markov/conditional_refresh.md) | C129/C130 的两种独立条件刷新模型：二进制固定边缘 \(\mathsf W_\nu/\mathcal R\) 的等价判据和锐系数；Gaussian \(W_{2,Q}/\mathcal R_Q\) 的条件耦合、谱门与局部锐性。跨模型调用或辨别旧图 E42/E43 时读，不把它们接成原同步 \(\Psi\)。 |
| [research/topics/random_markov/moment_recoupling.md](research/topics/random_markov/moment_recoupling.md) | C126 的非负标量矩门及更新后律空间小质量障碍；C127 的同步 \(D_\eta\)、回耦损失 \(\Delta_\eta\) 与同一近极小 OT 对的条件线性 EB。研究从收缩反推 \(\Psi\) 的 EB 或随机幂次提升时读；原生耦合仍是独立义务。 |
| [research/canonical/global_proximal_selection.md](research/canonical/global_proximal_selection.md) | C187–C190：物理/支持/运输合同，全部全局prox锚界，有限维a.e.唯一及指定模型密度卷积，坐标ℓ0全部完整支撑与平稳支持分类；复用C62-v2/C63但不互换残差。 |
| [research/canonical/support_normal_natural_class.md](research/canonical/support_normal_natural_class.md) | C191–C193：三角和反馈完整原图、全对模与真EB独立、同尺度匹配、全部选择长度，以及最大指数、固定二次锚失败和退化例外；圆盘/多面体为同图实例。 |
| [research/canonical/random_proximal.md](research/canonical/random_proximal.md) | RP-OBJECT/GAP/CONTRACTION/EB/BRANCH/SCALAR 的全证明、尖锐例和残差替换障碍；研究随机近端或条件 \(W_2\) 时读，改假设须另立版本。 |
| [research/canonical/example_atlas.md](research/canonical/example_atlas.md) | EX01 旋转、EX02 正紧对角、EX03 三次映射的完整对象卡、真残差、参数、证明及历史别名；检验某个逆推、EB 或常数边界时读，新增 GX 先区分对象与观察。 |
| [research/topics/examples/diagonal_spike_relation.md](research/topics/examples/diagonal_spike_relation.md) | C72–C75/GX-075：对角图加离散竖支的完整残差、每条近端路径、零锚/全对分离及精确二参数区；攻击“收敛或 EB 逆推全对 RL”时读。 |
| [research/topics/examples/positive_sine_phase.md](research/topics/examples/positive_sine_phase.md) | C81/C82/GX-064：完整正值正弦图的步长三相、临界全对和锚定常数、非零目标半阶及无零集路径；比较局部 RL 与 EB 时先核目标和基点。 |
| [research/topics/examples/bounded_square_minty.md](research/topics/examples/bounded_square_minty.md) | C83/C84/GX-065：有界平方完整图的全图临界端点折叠与精确 Hölder 常数、零目标真残差半阶、正侧 \(1/k\) 与负侧自然域逃逸；两界可同窗但收缩兼容和留域不成立。 |
| [research/topics/examples/bounded_negative_identity.md](research/topics/examples/bounded_negative_identity.md) | C96/C97/GX-066：完整有界负恒等图在 \(\lambda=1\) 的零输入多值、各指数锐全对常数及全部合法路径的步长相变；检验近端收缩与反射模、自然域覆盖能否互授时读。 |
| [research/topics/examples/skew_compact_diagonal.md](research/topics/examples/skew_compact_diagonal.md) | C102/C103/GX-059：完整无限维斜等距加紧对角的锐逆像、非 rectangular 直接反例、近端幂范数及反射锐非严格界；攻击正则性到图几何的逆推时读。 |
| [research/topics/examples/bounded_negative_square.md](research/topics/examples/bounded_negative_square.md) | C100/C101/GX-053：完整有界负平方图随步长的 Minty 相变、端点全对锐半阶、零点真残差与临界正侧有限步越自然域；检验 coverage 与留域时读。 |
| [research/topics/examples/skew_ball_inverse.md](research/topics/examples/skew_ball_inverse.md) | C98/C99/C124/C125/GX-058：同一完整盘法锥的全域逆像、边界半阶、单调/rectangular 图几何、完整近端和全图反射锐模；研究原算子 MR 与 Cayley RL 的不同量词时读，两者各有独立推导。 |
| [research/canonical/finite_data_proxy.md](research/canonical/finite_data_proxy.md) | C19/C20-v2 的 FD-1–18 自足证明：全部样本兼容、双 VI、有限抬升插值、两次收缩、强单调及正反误差、同图覆盖根、gap/e_N/e_x 分型和真目标三项界；研究有限数据代理前直接读本页，S23 只作溯源，C03/C04/C18 不作为本链前件。 |
| [research/NOTATION_CONTRACT.md](research/NOTATION_CONTRACT.md) | 跨主题符号表：RL 参数顺序、完整图和图块、真/步/算法/概率残差，以及锥、Markov、二参数图的局部字母重绑定；从某个方向引用另一方向结论前读。 |
| [research/topics/examples/restricted_root_graph.md](research/topics/examples/restricted_root_graph.md) | C85–C87/GX-032：严格分开受限负平方根完整短图与半直线完整母图，给锐成对常数、真二次 EB、受限无续步、母图远支与发散；从受限算法向母图推断时先读。 |
| [research/topics/examples/hemiregular_piecewise_parabola.md](research/topics/examples/hemiregular_piecewise_parabola.md)、[research/topics/examples/absolute_value_subgradient.md](research/topics/examples/absolute_value_subgradient.md) | C76/C77 与 C78/C79：前者是异维数完整映射的最近逆点与两变量正则对照、局部非闭图；后者把绝对值次梯度的原算子真残差跳跃和软阈值近端步残差分开。研究 MR/MSR 量词或残差模传递时读。 |
| [research/topics/examples/README.md](research/topics/examples/README.md)、[research/topics/examples/identity_square_branch_union.md](research/topics/examples/identity_square_branch_union.md)、[research/topics/examples/dr_tangency_transversality.md](research/topics/examples/dr_tangency_transversality.md) | C66–C68/C92/C95/GX-068 的完整并图、两种真残差、两变量半阶 MR、跨支碰撞及精确二参数区；C60/C61/GX-069/070 的 DR 算法残差锐模。先区分原算子、选支、完整步和算法残差。 |
| [research/topics/examples/ball_normal_cone.md](research/topics/examples/ball_normal_cone.md) | C93/C94/GX-067：完整法锥的全域投影/反射、二参数区，以及固定零目标的真空模与扰动逆像跳变；要用非孤立零集的 EB 或从反射稳定逆推 MR 时读。 |
| [research/topics/sparse_recovery/automatic_regularity.md](research/topics/sparse_recovery/automatic_regularity.md) | C224–C226的自动active-PD锐3/2、保留端点六阶及独立曲径四阶、完整近端窗口；C225-v2上侧strictmin族扩到全部有限p>3/2，v1范围保留；C228分开更宽strict comp/support范围及p>=2饱和global-min反例。每次引用自动结构或变步线性率先读此处。 |
| [research/topics/sparse_recovery/sharp_instance_dynamics.md](research/topics/sparse_recovery/sharp_instance_dynamics.md) | C227指定p=7/4自足链：Cauchy余项、star真EB、全部远输出排除、global-prox存在/等式、闭球留域、真实径向跟随与慢尾常数，另给临界曲线非不变障碍。 |
| [research/topics/sparse_recovery/sextic_boundary.md](research/topics/sparse_recovery/sextic_boundary.md) | C229固定p3六阶strictmin、局部隔离与锐strong trueEB1/5；alpha=alpha0，明确排除全部上侧统一1/3，无新增PPA结论。 |
| [research/manuscripts/sparse_regularity/sharp_sparse_regularity.tex](research/manuscripts/sparse_regularity/sharp_sparse_regularity.tex)、[PDF](research/manuscripts/sparse_regularity/sharp_sparse_regularity.pdf) | 集中英文论文，完整陈述及自足证明C224–C230，显式窗口和真实算法锐性；[论文入口](research/manuscripts/sparse_regularity/README.md)记录编译、目读和优先缺口。 |
| [research/audit/SPARSE_PRIORITY_AUDIT_2026_10_09.md](research/audit/SPARSE_PRIORITY_AUDIT_2026_10_09.md)、[阈值审查](research/audit/SPARSE_THRESHOLD_REVIEW_2026_10_09.md)、[完整轨道审查](research/audit/SPARSE_COMPLETE_DYNAMICS_REVIEW_2026_10_09.md) | 主体全文读取范围、已核2015先行、精确未闭优先门，以及两路独立重构和交叉攻击；不能用内部接受认证发表优先。 |
| [research/topics/random_markov/fixed_point_free_no_power.md](research/topics/random_markov/fixed_point_free_no_power.md) | C223：三点紧可数块 × 公平刷新；完整四映射与源参数、位移单射及原 OT 取得、全部初律相对几何尾、同一锚点全部正幂失败。研究无共同固定点的必要性时直接读；复算入口在 research/code/fixed_point_free_no_power/README.md，不继承 C143 B8。 |
| [research/topics/random_markov/compact_residual_boundaries.md](research/topics/random_markov/compact_residual_boundaries.md) | C143/C144：完整紧可数模型的全域运输、统一率、律空间长度与所有正幂失败；正方形投影原残差的假零、最近和实际极限锚；末节与 C71 的放松 OT 假零逐对象区分。 |
| [research/topics/random_markov/lazy_cycle_ot.md](research/topics/random_markov/lazy_cycle_ot.md) | C71：惰性四循环的原同步 OT 残差、锐全律空间误差界及放松最优运输后的假零点；判断有限状态残差是否保留输入 OT 约束时读。 |
| [research/topics/random_markov/lazy_cycle_representations.md](research/topics/random_markov/lazy_cycle_representations.md) | C88：同一四状态核与不变律在共同开关及逐状态独立开关表示下的同步成本、零集和两个不同的锐模；改随机表示或比较核与残差时读。 |
| [research/topics/random_markov/finite_state_certificate.md](research/topics/random_markov/finite_state_certificate.md) | C15-v1：固定有限数据、全部平稳目标律与 C-最优计划的有限 tight-edge 证书、锐 EB 及动力边界；§5 零面/空零面备用证明。C80 独立证明 Ψ² 的全域 Lipschitz 与连续分片仿射，不假定 exact-zero。研究同步 OT 时先读。 |
| [research/topics/random_markov/README.md](research/topics/random_markov/README.md)、[research/topics/random_markov/proximal_selection_seam.md](research/topics/random_markov/proximal_selection_seam.md)、[research/topics/random_markov/scalar_moment_envelope.md](research/topics/random_markov/scalar_moment_envelope.md) | C62-v2/C63 固定目标全局近端的吸收与核接缝；C62-v1 的有限纤维漏门和 [F37](FAILED_ROUTES.md#f37) 同页可核。C69 连续 gauge 的锐标量矩包络与分开聚合损失须另证明原生合法耦合和硬支持。 |
| [research/canonical/parameter_dictionary.md](research/canonical/parameter_dictionary.md) | PD-QUANTIFIERS/CAYLEY/TIED/STEP/SCALE/RESIDUAL/REGULARITY：同一图换步的单射门、尺度、真残差和 MR/MSR 的量词；引入或改变 RL 参数、正则性、选中步残差时先读。 |
| [research/canonical/non_tied_cayley.md](research/canonical/non_tied_cayley.md) | C89–C91：非 tied 二参数全对条件的平移 Cayley 球、两项锐普适常数、步长门、退化面、单调图双射和 Hilbert 同参数图极大等价；从 tied 曲线推广或引用完整 Minty 覆盖时先核 \(A,\Delta\) 与图范围。 |
| [research/canonical/path_atlas.md](research/canonical/path_atlas.md) | C31–C33及C163/C164：全部合法块末点的完整反向编码、前缀覆盖与步界生产、整轨道预算、有限进入/吸收/驻定的区别；无限词充分门与独立相位结论。做多步或多值算法时先核实际分支与留域。 |
| [research/topics/path_dynamics/README.md](research/topics/path_dynamics/README.md)、[research/topics/path_dynamics/m1_capture.md](research/topics/path_dynamics/m1_capture.md)、[research/topics/path_dynamics/power_shear.md](research/topics/path_dynamics/power_shear.md)、[research/topics/path_dynamics/oscillatory_shear.md](research/topics/path_dynamics/oscillatory_shear.md)、[research/topics/path_dynamics/domain_escape.md](research/topics/path_dynamics/domain_escape.md) | 路径主题入口与独立对象卡：C38/C39 的 M1 端点球和原生图缺口；C42 的可达性；C43 的保守指数；C44 的自然域逃逸与全纤维线性残差。新增对象先辨图、窗口和零集。 |
| [research/topics/path_dynamics/m1_sign_lift.md](research/topics/path_dynamics/m1_sign_lift.md) | C64/C65：新定义完整 Sign 图的全部纤维、全域 \(J_{\lambda F}=T\)、端点真残差模 3 和指定球上局部最大全对指数 \(1/3\)；历史原生循环方程仍须原始定义和路径桥。 |
| [research/canonical/composite_subregularity.md](research/canonical/composite_subregularity.md) | C34–C37及C161/C162/C165：满行秩真残差及局部近端；proper-lsc目标转移、实际二阶/Clarke反例、局部完整零集替换和曲面幂/非幂锐例。秩亏扩展仍开放。研究复合目标或调用历史 C11 时先辨身份。 |
| [research/topics/composite_regular/README.md](research/topics/composite_regular/README.md)、[research/topics/composite_regular/cusp_identification.md](research/topics/composite_regular/cusp_identification.md)、[research/topics/composite_regular/oscillating_target.md](research/topics/composite_regular/oscillating_target.md) | 复合主题可扩写入口与 C40/C41 独立证明：真多值次梯度的局部一步识别门、弱分离缺失时驻点极大序列的目标正确 EB 障碍。新增秩亏机制或目标反例时分别开卡，先核同一目标和真实残差。 |
| [research/audit/SOURCE_RECONSTRUCTION_AUDIT.md](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md)、[SOURCE_FILE_INVENTORY.tsv](research/audit/SOURCE_FILE_INVENTORY.tsv)、[ZIP_MEMBER_INVENTORY.tsv](research/audit/ZIP_MEMBER_INVENTORY.tsv)、[LEGACY_VERIFIER_RUNS.json](research/audit/LEGACY_VERIFIER_RUNS.json) | 251 个原件及 178 个包内成员的路径/哈希/语义未决字段，旧验证器环境与运行输出；逐源重写时更新 disposition 与规范锚点，不能将盘点算验收。 |
| [10/07清洗与空白接收](research/audit/BLIND_RECEIPT_2026-10-07_CLEANUP.md)、[逐文件接收范围](research/audit/COORDINATION_SCOPE_2026_10_07.tsv) | 四个全源范围、C185–C193独立证明、全局入口/Claim/图协调与修补循环；明确区分受检链可接续与全库仍有330个字节组未枚举，不把机械校验或局部接收当全库完工。 |
| [10/05 空白接收](research/audit/BLIND_RECEIPT_2026-10-05.md)、[10/03 接收](research/audit/BLIND_RECEIPT_2026-10-03.md) | 逐次记录空白读者实际阅读的链、反向复算、发现和修补；10/05 明确 C137 的 E221→E207、C141/C142 的本次受检证据、H04/H05 有限维接线及三类未闭缺口。核某条 Claim 的审查范围时读，不把局部接收当全库验收。 |
| [research/topics/examples/volterra_integration.md](research/topics/examples/volterra_integration.md)、[adjoint_volterra.md](research/topics/examples/adjoint_volterra.md)、[negative_cubic_branch.md](research/topics/examples/negative_cubic_branch.md) | C104/C105 与 C120/C121：Volterra 和伴随方向作为一个等距例型，右端点逆像另核；完整近端逐点强收敛而统一 gauge/有限幂界失败。C106/C107：负三次完整远支、图块锐模和路径越域。研究局部证书与完整算法时读。 |
| [research/topics/examples/planar_rotation_family.md](research/topics/examples/planar_rotation_family.md) | C122/C123：完整旋转族唯一 Minty 奇点、锐全对输入对距模、Fourier 循环阶与 GX-062/063 两角；修正旧稿“族内强模不决定循环阶”的过强解释。 |
| [research/topics/examples/isolated_pole_relation.md](research/topics/examples/isolated_pole_relation.md)、[rational_irrational_staircase.md](research/topics/examples/rational_irrational_staircase.md) | C108–C111/GX-055/056：前者全步长完整纤维、图窗、残差逃逸和全部合法路径；后者算术支纤维、锐 RL、真残差与完整最小步界。研究零系数模为何不提供输入/目标覆盖时读。 |
| [research/topics/examples/product_splice.md](research/topics/examples/product_splice.md) | C112–C114/GX-057：完整直积的全纤维、零残差与所有合法路径；临界全图、图点输出窗和仅限输入窗的不同锐半阶系数。组合不同例卡或改变图窗口时读。 |
| [research/topics/examples/gx059_065_property_completion.md](research/topics/examples/gx059_065_property_completion.md)、[AGM](research/topics/examples/arithmetic_geometric_mean.md)、[共同尾先例](research/canonical/selection_truncation_prior_tools.md) | C146–C158：完整AGM图/坏选择/严格兼容障碍，经典Lipschitz共同尾和辅助迭代器，GX053–065剩余图几何、完整逆纤维、VI及非零参考点；[选择文献边界](research/canonical/selection_literature_boundaries.md)给锚/集合距离不蕴含选择模的完整见证、校正先例阶数和P16安全尾/精确式阻断。 |
| [GX053–065 逐单元覆盖](research/audit/GX053_065_COVERAGE.md#gx-scope)、[专用表登记](research/audit/ATOMIC_SCOPE_REGISTRY.tsv) | 该成员1219物理LF行全部由独立属性、证据或组织余项覆盖。作者版本命名已核，刊本对应与旧网格执行证据分别保留未闭门；这一内容关闭枚举门，其他历史内容仍须逐项推进。 |
| [research/audit/SOURCE_OCCURRENCES.tsv](research/audit/SOURCE_OCCURRENCES.tsv)、[PAYLOAD_GROUPS.tsv](research/audit/PAYLOAD_GROUPS.tsv)、[build_occurrence_index.py](research/audit/build_occurrence_index.py) | 429 个物理文件/ZIP 成员位置与 346 个不同字节内容的可复现索引；状态仍待逐段语义枚举，不能把来源组数当数学覆盖。 |
| [research/audit/SEMANTIC_UNIT_SEED.tsv](research/audit/SEMANTIC_UNIT_SEED.tsv)、[SS1 数值来源复跑](research/audit/SS1_NUMERICAL_PROVENANCE.md) | 四个早期来源标题分段均由当前原子细表承接，旧结构段统一保留为 superseded-by-atomic-table；F11 的578 LF见[完整来源表](research/audit/OPERATOR_IDEAS_FULL_COVERAGE.md)。枚举完整不表示八项开放构造已解决；SS1旧程序复跑仍不认证修订稿的逐行版本同一性。 |
| [research/canonical/selection_primary_interfaces.md](research/canonical/selection_primary_interfaces.md)、[selection_quasi_arithmetic_boundary.md](research/canonical/selection_quasi_arithmetic_boundary.md) | LP22/LMZ/P16 的完整原定理接口、准确版本与映射均在规范层；C160 独立修复 P16 的负起步边界，证明共同超几何尾和同域 Lipschitz 选择界。刊本未核范围、完整 PPA 与优先权分开。 |
| [research/canonical/gauge_dilation_boundary.md](research/canonical/gauge_dilation_boundary.md) | C159/GD-1–7：完整紧图上的真实超线性 gauge EB 不授予不重标度的同 gauge Minty 界；每个 graph germ 的完整反例及正确重标度界。离散自然域不等于邻域输入 coverage。 |
| [SS1 全文枚举](research/audit/SS1_FULL_COVERAGE.md)、[foundations 最终正文枚举](research/audit/FOUNDATIONS_FINAL_COVERAGE.md) | SS1 的 763 行与最终 foundations 的 2096 行全部逐断言去向可查；具体文献、最佳常数及数值版本义务仍分别保留。仅关闭两个内容组的枚举门，不关闭全部历史包。 |
| [research/audit/UNIT_DISPOSITIONS.tsv](research/audit/UNIT_DISPOSITIONS.tsv) | 逐源单元的来源节、规范身份、精确锚点及未闭义务；当前行数和状态分布仅由[生成快照](research/audit/CURRENT_COVERAGE.md)给出，不是独立成果数或清洗率。全量来源枚举和逐项数学验收按[语义分母计划](research/audit/SEMANTIC_INVENTORY_PLAN.md)分别判定。 |
| [research/audit/C11_M1_SOURCE_SCOPES.md](research/audit/C11_M1_SOURCE_SCOPES.md)、[ATOMIC_SCOPE_REGISTRY.tsv](research/audit/ATOMIC_SCOPE_REGISTRY.tsv) | GX、SS1、最终foundations、C11 §8、M1 §5及§6–§9的精确逐断言范围；当前范围和原子记录以登记表及[覆盖快照](research/audit/CURRENT_COVERAGE.md)为准；有逐项去向，不代表全库346内容组已验收。 |
| [10/06 空白接收与清洗验收](research/audit/BLIND_RECEIPT_2026-10-06.md#receipt-result) | 三份完整原件、全部Claim/图条件协调、最后隔离Astra的实际范围与C37一般轨道补证明；可接续的受检链与全历史未完工边界分开。 |
| [图值/紧约束/孔洞/幂门工具](research/canonical/operator_profile_tools.md)、[完整原算子空间构造前沿](research/canonical/operator_space_construction_frontier.md)、[拓扑与闭性障碍](research/canonical/topological_repair_obstructions.md) | C166–C168/C172/C177/C178的精确定义、证明和开放边界；读总体规模比较前先冻结同一个对象空间、量尺与类别谓词。 |
| [有限状态补全](research/topics/random_markov/finite_state_completion.md)、[条件刷新补全](research/topics/random_markov/conditional_refresh_interfaces.md) | C169–C171/C173–C176及可测耦合、分位数和Gaussian补充；全部保持实际目标、输入最优性与残差类型。 |
| [F11路线完整来源](research/audit/OPERATOR_IDEAS_FULL_COVERAGE.md)、[有限状态完整来源](research/audit/FINITE_STATE_FULL_COVERAGE.md)、[条件修复完整来源](research/audit/CONDITIONAL_REPAIR_FULL_COVERAGE.md)、[NO-GO完整来源](research/audit/NO_GO_LEDGER_FULL_COVERAGE.md)、[本批接收](research/audit/BLIND_RECEIPT_2026-10-06_INVENTORIES.md) | 本批四个内容组逐独立断言覆盖；数学重建、旧身份/文献证据与历史报告分别裁决。接收记录只认证实际受检范围。 |
| [恢复的AW薄性](research/canonical/attouch_wets_fixed_input_thinness.md)、[恢复的一致Hölder薄性](research/canonical/uniform_holder_thinness.md)、[原母空间证明恢复范围](research/audit/MOTHER_SPACE_PROOF_RECOVERY.md)、[M1原生缺件检查](research/audit/M1_NATIVE_RECOVERY_CHECK.md) | C179/C180的前批两份完整原子来源；后续[C186](research/canonical/relative_holder_thinness.md#rht-object)已补stage synthesis全源，B1不再是其当前全件范围；现有材料可恢复的受限证明与确切未恢复身份分别记账。501位置检索不是501份数学验收；历史HTML内嵌载荷已核读，未新增原件。 |
| [research/CODE_REGISTER.md](research/CODE_REGISTER.md) | 十个历史验证器 V01–V10 到当前 Claim/待重写对象的映射、执行范围和盲区；检查计算证据或重写可维护代码时读。新代码按协议进入 `research/code/<topic>/`。 |
| [research/code/README.md](research/code/README.md) | 新可复现实验的 Claim 绑定、seed、精度、运行与盲区模板；只有新程序经重新编写和验收后才进入此树。 |
| [research/SOURCES.md](research/SOURCES.md)、[research/HISTORICAL_EDGE_CROSSWALK.md](research/HISTORICAL_EDGE_CROSSWALK.md) | S14–S25/SS 的**完整原路径**、ZIP 成员与恢复身份；9/14 旧图 h01–h35 的逐边去向。由规范命题反查或确认旧关系是否丢失时读。 |
| [research/canonical/zero_preserving_completion.md](research/canonical/zero_preserving_completion.md)、[复算入口](research/code/zero_preserving_completion/README.md) | C233–C235：保整管、保零集的有限新常数Euler必要充分性；谱投影可核的RP²及锐三次完整真EB；全域趋近产生真回缩的障碍。研究定量同常数完成或全域算法时读；不能把局部EB升级全域。 |
| [research/canonical/sharp_completion_cost.md](research/canonical/sharp_completion_cost.md)、[复算入口](research/code/sharp_completion_cost/README.md) | C236逐分量δ_j与锐新增数量：一般孤立点最少非零分量数，非退化最少Σ绝对缺额，指定位置可达到；C237用球投影达到单点原数据的精确最小Hölder常数并全域收敛。研究指数与数量、原预算与新预算之前先读；非单点同常数仍开放。 |
| [research/canonical/completion_budget_gate.md](research/canonical/completion_budget_gate.md)、[research/canonical/lipschitz_obstruction_budget.md](research/canonical/lipschitz_obstruction_budget.md)、[research/canonical/simplicial_sphere_budget_certificate.md](research/canonical/simplicial_sphere_budget_certificate.md)、[接收记录](research/audit/COMPLETION_BUDGET_REVIEW_2026_10_11.md)、[C245接收](research/audit/CONDITIONAL_LIPSCHITZ_BUDGET_REVIEW_2026_10_11.md)、[复算入口](research/code/completion_budget_gate/README.md)、[C245复算](research/code/lipschitz_obstruction_budget/README.md)、[C258复算](research/code/simplicial_sphere_budget_certificate/README.md) | C238严格雪花插值余量；C239 RP²单矩阵协变公式的固定平面障碍；C240给定预算保零完成的健壮有限网证书等价；C245把给定方向延拓的 Lipschitz 数据转成 Hölder 预算上界；C258把方向延拓降为有限半球、重心和 collar 证书。下一步分开下确界、达到与严格gap；不能用普通有限点避零代替全域余量。 |
| [research/canonical/rp2_explicit_completion.md](research/canonical/rp2_explicit_completion.md)、[独立接收](research/audit/RP2_EXPLICIT_COMPLETION_REVIEW_2026_10_12.md)、[复算入口](research/code/rp2_explicit_completion/README.md) | C264用固定轴旋转交换子避开内边界RP¹反向圈，给保整个RP²三次管、保全部完整零集的实际全域公式，半阶预算≤3025/32；C265给全部0<rho≤1/8、0<gamma≤1的精确原管半范数及真实达等点对。有限闭覆盖直接粘接、幅度加权和反向collar下界可复用；下一步优化预算或构造真实覆盖证书时先读。 |
| [CLAIMS.md](CLAIMS.md)、[RESEARCH_STATE.md](RESEARCH_STATE.md)、[FAILED_ROUTES.md](FAILED_ROUTES.md) | 逐版本精确身份与显式状态、当前阻塞与完成门、已失败机制；每次进展后同步维护。研究状态是现行可执行前沿，旧提交记录保留在 Git 历史。 |
| [INGEST_MANIFEST.tsv](INGEST_MANIFEST.tsv)、[BATCH_README.md](BATCH_README.md)、[history/README.md](history/README.md) | 初始校验、旧批次盘点与原件使用约定；用于核原件，不再作为数学地图。原件保留在 `history/sources/`，Git 历史可追初始导入。 |

阅读顺序：本页和超边图 → 依节点进数学模块 → CLAIMS 的精确版本和现存 objection → 必要时 SOURCES 的原稿标签/页码。要写新资产时先读增长协议和当前前沿；图中路线是搜索种子，不是方法白名单。

当前稿新增规范入口：[C242完整三角例](research/canonical/triangular_rleb.md)、[C243/C244固定SPD与Euler桥](research/canonical/rleb_kernel_topology_interfaces.md)。解析结论、有限计算和外部先行性保持不同证据范围。

**2026-11-17 三目标研究入口：** [research/topics/next_stage_2026/README.md](research/topics/next_stage_2026/README.md) 汇总非线性函数复合收缩、MOR-KL 有限长度迁移和 (A)+(B) 耦合结构的独立报告。C309 给出 \(\sum B(\varphi^{\circ k}(r))\) 长度门及 (F(y)=y|y|) 的非线性 PPA 例；C311 记录 MOR Theorem 5.1 到函数型精确 PPA 的 H11/H2/H3 映射及一般非单调迁移的开放桥；C312 记录完整 full-graph PPA 满足 (A)+(B) 但脱离传统次单调性的严格扩张例；C310 只保留旧条件不自动推出 (B) 的辅助障碍，并保留完整图 (A) 的 MSR 量词边界。读取这三份报告时必须保留 full graph 与允许子关系的区别。

| 新文件 | 数学资产与读取时机 |
| --- | --- |
| [research/topics/next_stage_2026/README.md](research/topics/next_stage_2026/README.md) 及三份目标报告 | 2026-11-17 三个独立研究方向的补充报告：T1.1 函数复合收缩—长度接口、C311 的 MOR-KL 条件迁移、C310 的 full-graph/输出步长障碍与 PTD salvage。每次继续研究前先核对各自的量词、状态和开放义务。 |
| [research/notes/target1_state.md](research/notes/target1_state.md)、[research/notes/target1_adversarial_review.md](research/notes/target1_adversarial_review.md)、[research/notes/target2_kl.md](research/notes/target2_kl.md)、[research/notes/target3_coupling.md](research/notes/target3_coupling.md) | 本轮独立审查笔记：保存非线性率的积分门与 PPA 边界、目标一的量词/Dini/粗步长攻击、MOR v1 逐式 KL 审计及版本限制、(A)+(B) 的闭图反例和严格子关系边界。笔记是报告的证据补充，不替代规范报告中的精确结论。 |
| [research/notes/integration_three_targets_review.md](research/notes/integration_three_targets_review.md)、[research/notes/target2_boundary_review.md](research/notes/target2_boundary_review.md) | 跨目标整合与目标二边界审查：说明 C309 几何尾与 C311 KL 能量只能并列使用，PTD/TC 在 coverage 前件下如何编译到 C309，以及 exact global PPA 的 level-set、H3、KL 索引、有限前缀和 S/Xi 量词不能混写。 |
| [research/notes/literature_version_review.md](research/notes/literature_version_review.md) | LMZ 正式 INFORMS metadata/abstract 与 arXiv v1 定理编号的版本边界审计；正式版定理级差异、常数、假设、证明和速率式继续记为 unknown。 |
| [research/canonical/free_particle_rleb.md](research/canonical/free_particle_rleb.md) | C246完整全图逆式、同一常数的全对/锚定/真EB证书、锐指数及所有闭式轨道；C247全部SPD二次根和实际发散；C241-v2原对象更短锚证。比较非Lipschitz示例或换度量时读取。 |
| [research/canonical/amplitude_circle_hamilton.md](research/canonical/amplitude_circle_hamilton.md) | C256完整Clarke零集与全部纤维、全空间coverage、全分支曲率界、统一圆管、恰三输出、锐锚1/2与EB2、准确旧合同和正面能量替代。完整多值校准；C259经典正面已闭，强推荐撤回。 |
| [research/canonical/amplitude_circle_damping_threshold.md](research/canonical/amplitude_circle_damping_threshold.md) | C257全实参数coverage、Γ>0锐圆零吸收/收敛门、每个正阻尼完全显式共同元组、锐距离1/(1+Γ)、真三输出持续、中心完整零纤维、全局二周期/负阻尼旋转；最大半径留门。 |
| [research/canonical/amplitude_classical_energy.md](research/canonical/amplitude_classical_energy.md) | C259不借新曲率的同窗完整经典能量正面；C256/C257强推荐撤回。 |
| [research/canonical/orthogonal_feedback_rleb.md](research/canonical/orthogonal_feedback_rleb.md) | C260-v1/v2全维反馈球、真inf、全部根、R10⁻⁴共同窗、指定模式coverage及sharp sqrt26/11；设计原型身份与能量替代明确。 |
| [research/canonical/smooth_kl_full_relation_obstruction.md](research/canonical/smooth_kl_full_relation_obstruction.md) | C261-v1/v2光滑H1与v3强链式/可定义非光滑H1/H2严格障碍；C262人工非可定义KL桥限定全部ABS排除。 |
| [继续筛选](发表成果整理/应用优势继续筛选.md)、[完整正面反审](发表成果整理/候选正面反审明细.md)、[复算](research/code/natural_advantage/README.md) | 新候选循环、经典正面淘汰、独立coldread及改稿清单，现成系统映射未认证。 |
| [research/canonical/perspective_bregman_gppa.md](research/canonical/perspective_bregman_gppa.md) | C255完整退化核优化、边界/远输入与物理桥、锐prox两点1/2及极限两点1/3；经典零锚长度路径已核，不作为优势分离。 |
| [应用筛选](发表成果整理/应用优势导向的候选筛选.md)、[接收范围](发表成果整理/本轮应用例独立接收.md)、[复算入口](research/code/natural_gppa/README.md) | 多轮失败机制、四维评价、精确文献合同、全部选择量词、临界/远中心攻击和采用后的摘要/比较/附录重写清单；未冒称稿件已替换。 |
| [发表成果整理/非Lipschitz近端例独立比较.md](发表成果整理/非Lipschitz近端例独立比较.md) | 优化来源、机制、原Hamilton的四轴比较；凸幂完整合同、C248弱凸离零奇点、致命分支攻击及实际主稿采用清单。要选正文例或重写比较贡献时读取。 |
| [research/code/free_particle_rleb/README.md](research/code/free_particle_rleb/README.md) | 上述Claim的实际参数、seed、边界与独立反算、Python版本和hash；两份运行结果用于复现有限算术，不作为普遍证明。 |
| [research/canonical/artificial_kl_energy_bridge.md](research/canonical/artificial_kl_energy_bridge.md) | C262人工非可定义KL能量的完整ABS正面桥；禁止把C261的CR障碍扩大为整个ABS排除。 |
| [research/canonical/orthogonal_feedback_critical_gate.md](research/canonical/orthogonal_feedback_critical_gate.md) | C263全n真实phase零吸收锐门及全部临界纤维，局部系数不能替代远门。 |
| [research/canonical/generic_power_kl_bridge.md](research/canonical/generic_power_kl_bridge.md) | C266任意闭S、正确物理转接和qγ≥1的完整幂几何可编译共同KL–ABS；自然距离幂子区另给正面，不授全理论排除。 |
| [research/canonical/optimization_proximal_limits.md](research/canonical/optimization_proximal_limits.md) | C267 全局极小近端解点界和 Bregman 零纤维，C268 非单射核见证。比较通常 PPA 的抽象与优化轨道时读 C431 的真误差模、长度势及跨步限制。 |
| [research/canonical/vector_fenchel_classical.md](research/canonical/vector_fenchel_classical.md) | C269原生向量FY完整驻点，全λ/allinput/allroot经典正面与物理有限长度；原f-H1失败不产生整体理论空白。 |
| [research/canonical/gram_regression_gppa.md](research/canonical/gram_regression_gppa.md) | C270自然欠定矩阵回归、退化Gram核、共同物理证书、显式极限与锐1/3读出；经典正面并列，prox锐3/7未闭。 |
| [最新应用筛选](发表成果整理/应用优势筛选_结构边界.md)、[规范接收](发表成果整理/本轮模型筛选独立接收.md)、[有限复算](research/code/model_selection_limits/README.md) | 本轮四轴评价、全关系攻击、经典正面淘汰、原例关键角色及具体改稿清单；强应用主例仍未找到。 |
| [research/canonical/affine_crosstalk_rleb.md](research/canonical/affine_crosstalk_rleb.md) | C271短直线控制设计：每模式唯一真实标量逆、原union多值、完整共同RLEB窗/trueinf/政策终点、参数远门和fixedSPD完整反例；全域原机械能更强，强推荐仍撤回。 |

| [research/canonical/ppa_nonlinear_gauge_and_coupled_obstruction.md](research/canonical/ppa_nonlinear_gauge_and_coupled_obstruction.md) | C309/C310/C311 的规范正文：一般函数迭代的 PPA 长度预算、LMZ KL 到 exact subgradient PPA 的有限长度重构、目标三的最大单调 MSR 反例及锚定扇区—相对平静性修正版候选。研究非线性收缩、KL 迁移或 (A)+(B) 时先读。 |
| [research/audit/PPA_NEXT_STAGE_2026-11-17.md](research/audit/PPA_NEXT_STAGE_2026-11-17.md) | 本轮五项交付的研究状态报告：现有定理/G1–G4、LMZ 正式版元数据与 arXiv v1 页码、三个目标问题表、联合路线和 proof obligations。正式刊本全文未取得的边界在此记录。 |
