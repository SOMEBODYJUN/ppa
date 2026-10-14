# 历史代码到规范命题的登记

## C277–C284：联合原图、完整覆盖与变化核

[本批复算](code/unified_ppa/README.md)运行 python3 research/code/unified_ppa/run_all.py，五个脚本全部返回0（四个只用标准库，raw另用NumPy 2.3.5）；[完整输出](code/unified_ppa/all_verifiers_output.json)绑定命令、版本、精度说明、脚本hash与stdout/stderr。Fraction核提升/非交换矩阵/有理LMI/预算反算/两步终止/统一SPD精确发散，binary64核明确的分支、曲率、壳层势与projector极值。所有全称coverage、全fibers、allpolicy长度、sharp门及最大化反例由[规范证明](topics/unified_ppa/README.md)解析承担。程序不认证有限状态完备性、自然应用、内层复杂度或公开首创；闭合结果与open交接分开。

## 理论发展与同算法经典恢复

[新增经典桥复算](code/novelty_development/README.md)运行 `python3 research/code/novelty_development/verify.py`，保存[结果](code/novelty_development/output.json)：16个C272 SPD、10个C273完整Gram、10个C274部分对偶PPA和13个C1合法输出能量合同。Decimal100/binary64的参数、版本、容差及哈希均登记。零/跨符号/远输入/中心临界门已实跑；原点Bregman与中心距离幂算法同速率但不同输出亦反算。不枚举全部数值纤维，不认证公开优先；全称数学由[规范补充证明](novelty/2026_10_13/README.md)承担。

## 原始模型到完整 GPPA 证书

[结构复算](code/structural_verification/README.md)登记 C272–C274：Fraction 共同半径系数、100 位 Decimal 的 C1 多驻点/非极小根反算、零/跨符号/远输入、局部远根与反射失败、非零数据 Gram 的 15 个缩放方程见证、混合幂核中心/非zero切向层及反馈共同证书临界门。运行 `python3 research/code/structural_verification/verify.py` 写 [output.json](code/structural_verification/output.json)，包括代码哈希、精度、原式/缩放残差和舍入界。不枚举完整数值纤维、不证明所有输入/输出或最优指数；这些量词在对应规范正文中解析证明。

## 本轮新增：GPPA 首创性核查与精确边界

[四路接续复算](code/gppa_novelty/README.md)和[followup_verification.json](code/gppa_novelty/followup_verification.json)另外登记C221/C222、GPPA经典桥及NFB旧更新的四组程序；基线94cbbbd，初轮记录保持，不混写阅读或执行时间。

[gppa_novelty/README.md](code/gppa_novelty/README.md)登记 C218–C220 与先行比较中的五个标准库有限复算程序，精确Fraction/Decimal与binary64范围分别声明。[verification.json](code/gppa_novelty/verification.json)给实际命令、版本、退出码和hash。脚本检查显示恒等式、指定轨道、共振余项常数和锐线性子族；不认证全球首创或任意非线性关系锐性。

此登记只让代码可找、可复跑、可判断证据范围。原程序保留在 `history/sources/`，不是规范证明或自动升级的定理。新计算若有长期价值，按 [增长协议](../RESEARCH_PROTOCOL.md) 写入 `research/code/<topic>/` 并保存参数、seed、依赖、精度和输出。

[完整运行记录](audit/LEGACY_VERIFIER_RUNS.json)含 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、每脚本 SHA-256、执行命令、stdout/stderr 与退出码。本轮十个退出码均为 0。

| ID | 原程序 | 所属规范命题/待重写对象 | 本次观测与不能推出的结论 |
| --- | --- | --- | --- |
| V01 | [验证_C11复合次正则.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/06_验证程序/验证_C11复合次正则.py) | 历史复合 C11（不等于现 C11）；现行 [C37 / CS-MODEL](canonical/composite_subregularity.md#cs-model) 的对数标量模型与 [CS-OBJECTIONS](canonical/composite_subregularity.md#cs-objections) 的 Clarke 区间；另核一条 hypomonotone–RL 代数恒等式 | 脚本未改写；二分法的有限输入、四个有限代数点和一个区间检查只是观察，C34–C37 的一般证明不依赖此运行 |
| V02 | [验证_RL合稿实例与常数.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/06_验证程序/验证_RL合稿实例与常数.py) | R04 与旧 RL 接缝/常数 | 有限两支抽样、固定随机种子 20260908；无一般证明 |
| V03 | [验证_SOC与PSD实例常数.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/02_锥优化_CRSC_MSCQ/05_验证程序/验证_SOC与PSD实例常数.py) | C13 锥面/MSCQ 例 | SOC/PSD 常数及有限确定性候选；不证最优模 |
| V04 | [验证_四状态反例精确证书.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_四状态反例精确证书.py) | M-FALSE；同步 OT 假零反例 | 有理数证书；同输入 OT 的一般定理另核 |
| V05 | [验证_惰性四循环精确有理数.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_惰性四循环精确有理数.py) | [C71 / LC-SHARP](topics/random_markov/lazy_cycle_ot.md#lc-sharp) 的固定惰性四循环；C15 是一般有限状态证书 | 特定有理参数下的有限顶点与平方常数 26；不证明 C71 对所有 \(0<p<1\) 的锐值 \(13/p\)，也不证明 C15 的全称等价 |
| V06 | [验证_投影与可数紧致扩展.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_投影与可数紧致扩展.py) | Markov 可数紧扩展/投影障碍 | 12 有理块；无限集合证明未由运行覆盖 |
| V07 | [验证_有限状态OT严格性.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_有限状态OT严格性.py) | C15 有限状态顶点判据 | 有限顶点枚举；与 V05 重叠但脚本不同 |
| V08 | [验证_条件残差修复独立复核.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_条件残差修复独立复核.py) | 条件 bit/Gaussian 分支 | 165 个 binary-simplex 律及 Gaussian 数值；一般参数边界另核 |
| V09 | [验证_随机近端相关性与常数.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_随机近端相关性与常数.py) | C22/C23 随机近端 | 有限矩阵和 1000 配对抽样、标量恒等式；证明在 RP 模块 |
| V10 | [验证_非乘积近端与吸收障碍.py](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_非乘积近端与吸收障碍.py) | C62/C63 固定目标全局 prox 的吸收与 law-step 接缝；[重写证明](topics/random_markov/proximal_selection_seam.md) | 2026-10-01 在 Python 3 复跑，有理恒等式及 k=0,1,2,5,10 PASS；只核有限代数，不证明所有 k、平稳律或邻域 EB 障碍 |

## 复跑与新增代码准入

从仓库根运行 JSON 中对应的 `command`；执行时不改动历史原件。若环境/依赖不同，记录新环境和差异，不覆盖旧结果。涉及随机数据的脚本必须先核内部 seed；没有可复现 seed 的抽样只作一次 observation。

新代码须声明绑定的 Claim **版本**、测试的有限对象、输入/seed/精度/误差、断言与盲区。验证器可否定某个精确有限断言，也可提示一般证明的漏洞；“PASS”本身不能把全称命题从 `candidate` 提升为 `canonical`。历史 V01 的 “C11” 仅是旧复合次正则编号，现 C11 为极限回缩，绝不能据脚本名关联。

## 2026-10-08 文献接口的精确检查

[check_scope.py](code/literature_refresh/check_scope.py) 绑定 C197-v1 / C198-v1 及 GPPA v1 Example1 校勘记录；[正文](literature_refresh_2026_10_08.md#lr-repro) 给复跑命令和全部一般证明。整数 / Fraction 精确算术，无随机 seed 或容差；只核 GPPA k=0,…,8 的合法性和能量式、四个有理点的16对 Hölder估计、参照1-Lipschitz两点失败和 Example1 的内积−1，以及日期差。[results.json](code/literature_refresh/results.json) 记录环境和代码hash，[sources.json](code/literature_refresh/sources.json) 记录六份已取得一手原稿的版本hash。有限PASS不认证全称结论、外部完整证明或全球新颖性。

## GPPA / NFB 完整对象比较的独立复算

按本轮集中保存比较证据的要求，脚本与结果同存 [专用比较目录](comparisons/2026_08_gppa_nfb/README.md#reproduce)，不修改历史程序。绑定C199–C203-v1；[verification.json](comparisons/2026_08_gppa_nfb/verification.json) 给Python环境、各脚本hash、实际命令及退出码。

| 脚本及输出 | 有限验证与误差范围 |
| --- | --- |
| [gppa_check.py](comparisons/2026_08_gppa_nfb/gppa_check.py)、[结果](comparisons/2026_08_gppa_nfb/gppa_check_results.json) | Fraction核显式核、边界法锥样本、普通/warped步及不变量/物理桥；完整cap合法步；binary64仅展示严格兼容常数及T4系数。一般ASM和无限分割由专篇证明，不由抽样证明。 |
| [nfb_check.py](comparisons/2026_08_gppa_nfb/nfb_check.py)、[结果](comparisons/2026_08_gppa_nfb/nfb_results.json) | 固定seed的1200组非对角SPD平方配方精确Fraction；四例逐20步PPA/NFB等式、source完整下降常数；15组product压缩；局部失败序列有限趋势及固定PDFhash。一般必要性靠N6/N11及解析阶比较，binary64趋势不是无限序列证明。 |
| [independent_attack_checks.py](comparisons/2026_08_gppa_nfb/independent_attack_checks.py)、[结果](comparisons/2026_08_gppa_nfb/independent_attack_results.txt) | 独立Fraction核source下降系数（旋转1/3，负恒等788/2967）、平方配方、T4严格余量和自然类/cap/超线性合法图点商；无随机容差。有限PASS不涵盖所有核/拆分/lift，正文明确量词。 |

复现命令见比较README；计算只是独立算术检查，不认证外部全球先行性或任意表示排除。

本轮指定6.1-sol ultra复审新增C204–C207正反接口，脚本仍集中在同一比较目录。[sol61_verification.json](comparisons/2026_08_gppa_nfb/sol61_verification.json)记录实际复跑命令、Python环境、脚本/结果hash及原文指纹；原verification记录保留初轮身份。

| 脚本与相邻JSON | 有限检查范围 |
| --- | --- |
| [pair_monotone_checks.py](comparisons/2026_08_gppa_nfb/pair_monotone_checks.py) | C204加权消元、跨支乘积界、带跳跃单调剖面的总变差分割；原cap与改图仿射更新 |
| [sol61_gppa_check.py](comparisons/2026_08_gppa_nfb/sol61_gppa_check.py) | C199非单位步长/完整边界、T4严格余量修补、C204分割；C205正支ASM/coverage/物理桥，C206级数严格安全常数，C207积分尾界 |
| [sol61_nfb_check.py](comparisons/2026_08_gppa_nfb/sol61_nfb_check.py) | 原source步长门、负恒等精确下降788/2967、旋转1/3，完整拆分平方配方、合法锚失败点及算法等式 |
| [sol61_independent_checks.py](comparisons/2026_08_gppa_nfb/sol61_independent_checks.py) | 独立C199/C202及改变原图的仿射同轨道校验，明确改变零集/完整纤维 |
| [sol61_branch_checks.py](comparisons/2026_08_gppa_nfb/sol61_branch_checks.py) | C205原正轨道及负首步；C206有限尾恒等与严格K上界；C207有积分剩余界的有限尾区间。一般系列/全图结论由独立证明承担 |

## C208–C214 一般模 GPPA 的独立有限复算

[verify.py](code/gppa_modulus/verify.py)、[说明](code/gppa_modulus/README.md)、[实际结果](code/gppa_modulus/results.json)只依赖 Python 标准库。精确 Fraction 反算一步能量、全部正 ASM 小参数、幂兼容临界系数1及误差卷积；确定性 seed 20261009 与 binary64 明示容差核非线性强单调 V 的逆、有限全部点对、SF 完整更新、selected/true 残差和对数积分尾区间。螺旋物理弦长再以坐标反算核验。六项有限检查均 PASS，不证明任意核排除、无限长度门、全部图点对或全球先行性。完整参数与脚本指纹在结果文件。

[PDF 源稿与作用域 renderer](manuscripts/gppa_modulus/gppa_modulus.tex)是集中证明交付；renderer 使用 ReportLab 和 Matplotlib MathText，不冒充完整 LaTeX 编译器。数学公式解析失败会报错，不静默丢失；公式数量、布局、实际 PDF 与源稿指纹和渲染目读记录相邻保存。

## GP-SCOPE：C215/C216与比较量词

[research/code/gppa_scope/README.md](code/gppa_scope/README.md)记录标准库复算入口；`verify.py`确定性运行，`results.json`保存80/120位Decimal、解析余尾、Fraction抵消反代、原图值、偏移/零/恒定/非单射核边界和跳跃gauge。有限集合模型仅检查比较量词不被混同，不决定算子类真值。正文先完成、计算佐证，外部先行性保持开放。

## C223：无共同固定点的正幂必要性边界

[verify.py](code/fixed_point_free_no_power/verify.py)、[范围和运行](code/fixed_point_free_no_power/README.md)、[实际结果](code/fixed_point_free_no_power/results.json) 使用标准库 Fraction，检查八块加原点的二状态积空间、全部有序点对、0–80矩阵时刻与两种混合区间、见证最优成本、e=0边界碰撞及指定小正幂指数反算。无随机性和浮点误差。有限精确证据不证明无限域、所有概率律或任意正幂；承重证明在 C223 正文 FP1–FP21。


## C224–C228: sparse threshold and complete dynamics

[Code entry](code/sparse_regularity/README.md) and [fingerprint manifest](code/sparse_regularity/verification_manifest.json) fix the actual runnable scripts, outputs, Python version, precision and diagnostic tolerances. `verify.py` independently checks268200 finite moment cases and60/100-digit boundaries. `sharp_dynamics_verify.py` uses exact Fraction certificates, three100000-step genuine implicit trajectories and Decimal50/80-digit repetitions. `independent_complete_review.py` supplies a separate50000-step two-variable recurrence and exact rational majorant check. No randomness, no substitution of scalar radial minimization for the actual update. The displayed analytic proofs and independent mathematical reception, not computationalPASS, carry all complete-fiber and infinite-time quantifiers. The manuscript is real LaTeX, with source/PDF fingerprints and visual check scope in[its entry](manuscripts/sparse_regularity/README.md).

C225-v2补充`upper_family_verify.py`及`upper_family_results.json`：Fraction四阶复合/端点六阶、alpha0和K反算、曲径四阶系数、Decimal80上侧p=2及更大有限p，另核strict-comp饱和的global-min分解及kappa可去值；解析证明负责全部实p量词。

C229/C230及最终独立接收补充两个从零重构的检查器：sextic_boundary_verify.py精确Fraction核六阶边界系数；final_dynamics_verify.py通过formal ODE重建偶系数并解真实二维implicit方程，含t0=1e−8的tracking测试及两步长。输出分别sextic_boundary_results.txt和final_dynamics_results.json，命令、精度/诊断误差与哈希见同一代码入口。C230的normal-form/标量barrier由自足解析证明承担，经典KL明确适用而不自称首创。


## 新前沿复算接口（2026-10-10）

- [topological_completion/README.md](code/topological_completion/README.md)：C231的完整球面例TC7–TC11，精确有理接缝、独立径向逆式、全部近端包含、真EB与有限Holder界；seed、运行版本、容差及实际结果随目录保存。指数定理与任意完成不由计算证明。
- [tangential_area/README.md](code/tangential_area/README.md)：C232候选的完整slab原图、真实近端包含与二阶面积基准；校正一阶振荡后的有限面积比值。候选接收和sharpRL仍开放。


## C233–C235：保零完成与射影平面

[zero_preserving_completion/README.md](code/zero_preserving_completion/README.md)给实际运行范围；verify.py核固定seed矩阵谱投影、三次法向、独立inverse及完整prox图，Fraction枚举全部指定有限边界参数并反算真EB系数，100位Decimal核极小半径，results.json保存环境及实际误差。程序没有实现全域Hopf延拓，不证明一般完成或全域收敛；承重证明和独立接收另列。

## C236/C237：锐零点数量与单点精确预算

[sharp_completion_cost/README.md](code/sharp_completion_cost/README.md)固定运行命令、seed及3e-11容差；verify.py和results.json核分量缺额枚举/反向计数、胞腔Euler反算、SC6绕数和全部指定正则原像、维数2/3/5范数与零点、Fraction径向界、线性旋转整球数据的精确预算/完整图回代及真实有限迭代。迭代步数按解析q界决定，避免θ接近1时固定循环长度不足；有限计算不实现Hopf延拓，不证明全域量词或发表先行。


## C238–C240：严格插值余量、对称障碍与有限证书


[completion_budget_gate/README.md](code/completion_budget_gate/README.md)给标准库复现命令、seed238240、3e−12浮点诊断容差及Fraction精确范围。verify.py与results.json检查280组概率方差/球半径、D2固定平面与偏置共同稳定子、以及真实覆盖的一维区间有限证书。不是RP²完成证书或全域扩张求解器；原预算下确界与达到性继续开放。


## C242/C243：简短机制例与固定SPD核

[triangular_rleb/README.md](code/triangular_rleb/README.md)与[结果](code/triangular_rleb/results.json)固定seed20261011、脚本指纹、容差和反算范围：15个边界输入、20885个有效点对、15条各35步完整PPA轨道、45条松弛轨道，以及完整方程、真实残差、独立锚定/全对常数和精确SPD反例。一般量词及无限极限由C242解析证明承担；例子特有的松弛结果不扩大主定理。

[rleb_spd/README.md](code/rleb_spd/README.md)与[结果](code/rleb_spd/results.json)记录5212项有限断言：完整Q桥、非对角零输入纤维、正对角小窗、退化丢失纤维和普通PPA成功而新核失败的边界。使用NumPy binary64及Fraction精确反算；环境、误差及seed见入口。不能以有限PASS认证所有核、一般GPPA或全域吸引。

## C245：给定方向延拓后的条件 Lipschitz 预算桥

[lipschitz_obstruction_budget/README.md](code/lipschitz_obstruction_budget/README.md)给标准库精确复算。`verify.py` 使用 Fraction 反算 RP² 压力测试的保守全域投影界、整管位移和半 Hölder 预算系数；`results.json` 保存实际输出。程序只核代数接口，不构造方向延拓，也不把条件上界升级为原预算结论。

## C246/C247/C248 与 C241-v2：完整近端示例独立比较

[free_particle_rleb/README.md](code/free_particle_rleb/README.md)给标准库复现命令、seed20261011、Python版本、容差和SHA256。verify.py检查signed/零输入、认证管端点、独立全图反算、24步显式轨道、全部SPD二次根与重根、真双残差、负剪切发散轨道、C241-v2严格预算及工程化弱凸边界。optimization_verify.py另核凸优化比较的完整prox、EB、跨符号和临界窗。结果只承担有限算术；无限轨道和全称证书由C246/C247规范页及C248独立比较记录解析证明承担。

## C249–C254：物理 RLEB–GPPA 父理论与论文数学包装

- [rleb_gppa/README.md](code/rleb_gppa/README.md)：4603项标准库有限恒等式、完整非线性/非单射GPPA、真实残差、严格预算与能量边界；不能证明一般定理。
- [rleb_gppa_example/README.md](code/rleb_gppa_example/README.md)：四次Bregman核、完整隐式步、110位Decimal和精确Fraction；实际10421项有限核验及误差记录。
- [rleb_packaging/README.md](code/rleb_packaging/README.md)：同点对二次参数识别、25个能量边界、弱凸径向目标的接缝/最优性/强凸/凸支撑与管邻域；一般凸性与指数由解析证明。
- [rleb_gppa_attack/README.md](code/rleb_gppa_attack/README.md)：独立246884项有限边界；非闭v(S)核收敛而物理发散的完整反例，Id能量与真实Bregman根；不能推理所有核/所有初值。

各verify.py均将结果写入自身目录，环境/精度/确定性范围由README和results.json保存；独立受检范围见发表成果整理/GPPA主理论。

## C255–C257：应用优势筛选与完整分支反算

[natural_gppa/README.md](code/natural_gppa/README.md)固定三条标准库复现命令及实际结果。verify.py核seed20261011的10015核输入、20000物理两点、35完整边界/远输入与80位尖点/锐配对；circle_verify.py用Fraction反算C256共同元组、中心排除、曲率Young系数、真EB、临界幂兼容、严格预算与替代能量系数，并对90个有理旋转的三输出公式进行80位反代。脚本指纹和误差均在对应JSON。全空间coverage、三输出穷尽、每个完整分支与无限轨道由规范解析证明承担。C255的计算PASS不改变旧零锚正面路径及撤回优势推荐的裁决。

C257另有damping_verify.py / damping_results.json：80位Decimal核八个Γ从10^−12至10^6的完全显式共同元组、16个指定κ元组、远输出间隙、真EB分母、兼容与留域；四个中心出现边界、三个小负Γ精确旋转轨道逆代，Fraction核中心负A临界系数。无随机。所有实Γ和锐门的全称断言仍由规范页D1–25证明，有限PASS不授予最大半径。

## C258：有限单纯形球值方向证书

[simplicial_sphere_budget_certificate/README.md](code/simplicial_sphere_budget_certificate/README.md)给二维和五维 toy 三角剖分的公共半球、重心梯度、路径因子和标量边界 collar 余量复算；`verify.py` 同时拒绝无正半球余量、无效 eta、零见证和反向（\(\varepsilon=2\)）collar。它不认证 RP² 的双 Lipschitz 参数化、真实边界迹或原预算端点。

## C259–C263：经典正面、完整反馈、能量边界与锐远纤维门

[natural_advantage/README.md](code/natural_advantage/README.md)给标准库命令、SHA与结果。Fraction核全域/normal/真EB/兼容/严格预算和C259短能量常数；80位Decimal七个逆定义sharp族及精确管外增能一步；seed20261012的720球投影/skew表示、100强度polarization复算通过。C261另核六个Γ/R辅助前驱边界。C260-v2新增R10⁻⁴三轮有理吸收、trueinf余量、全窗/严格预算；C262核dense预算与H1α.9；C263核十一个η±/0的闭式临界根反算。所有完整输出、无限轨道、指数锐性、能量不可能性、limiting/KL与临界全纤维仍由规范解析证明负责。

## C264/C265：RP² 实际完成与精确原管预算

[rp2_explicit_completion/README.md](code/rp2_explicit_completion/README.md)记录完整公式实现、seed20261012、NumPy/Python版本、binary64容差、脚本SHA及实际results.json。35784项有限检查含内反向圈、固定轴交换子两项正交、actual raw余量1/4达等、整管三次完整输出、rho/1/4/3/2/2接缝、球外紧支撑、幅度正余量、有限全对界、不同rho/gamma原管精确达等和径向平方恒等式；Fraction反算有理预算。代码不证明全域一般量词，不求L*；解析证明与独立审查承担Claim。

## Model-selection-limits · C266–C270

入口 [`code/model_selection_limits/README.md`](code/model_selection_limits/README.md)，运行 `python3 research/code/model_selection_limits/verify.py`。seed266269，Fraction精确多项式/firm反例；420加权区间前缀、指数角点、49单空核反算、1440向量stationary反算、540Gram完整三次逆反算及缩放t⁷族。环境/实际脚本SHA记录于results.json。全称coverage/limiting/KL/无限政策/最佳指数由规范解析证明承担；C270锐3/7上界仍开放。代码通过不认证全球优先或强应用优势。

C271另用同目录rail_verify.py，seed271、Fraction与Decimal80；1035真实固定gain标量逆、265同窗、38临界远根/二周期、五个sharp族、exactSPD完整zero3与真实漂移复算通过。零动量处主动拒绝乘过分母的伪根。脚本hash和环境在rail_results.json；不证全称，经典全域正面与共同能量合同不可能均由规范正文承担。


## C275–C276：非精确真实图停止与完整精度边界

运行 python3 research/code/inexact_ppa/verify.py；[代码说明](code/inexact_ppa/README.md)与[输出](code/inexact_ppa/output.json)记录版本、精度、容差、参数和脚本 SHA256。实际通过 1645 个联合停止规则的完整水平纤维端点/中点见证、492 个多值法锥图见证、125 组循环矩阵系数；另核跳跃逆的非达到下确界、零输入、跨符号、闭式轨道/共轭、临界及远端发散政策。独立标准库脚本 [check_frontier.py](code/inexact_forcing_attack/check_frontier.py) 的实跑输出保存于主 output。

全称覆盖、完整纤维、所有政策、锐指数和临界必要性由 [C275](topics/inexact_ppa/real_graph_stopping.md)／[C276](topics/inexact_ppa/sharp_precision_frontier.md) 解析证明承担。数值只反算有限参数，不认证公开优先、整个连续纤维或自然应用优势；真实残差与选中图值在多值见证中明确不同。


## 不同次单调与一般模路线：比较反算

[统一复算入口](code/submonotonicity_routes/README.md)运行 python3 research/code/submonotonicity_routes/run_all.py。六个独占脚本的完整 stdout/stderr、返回码、Python版本和脚本hash保存于 [all_verifiers_output.json](code/submonotonicity_routes/all_verifiers_output.json)；Fraction恒等式、零/临界/两符号/远输入、完整分支前缀、单零锚/完整零集和无限长度渐近分别标明。

本轮只增加比较证据：旧tied类精确换参、同算法direction-loss、一般预算边界与点收敛/finite-length区分。GU1/GU3保留报告级candidate，不新注册总账Claim，不改旧身份；全称由[各分报告](novelty/2026_10_14_submonotonicity/README.md)解析证明，数值不认证全部纤维、公开首创或实际成本。
