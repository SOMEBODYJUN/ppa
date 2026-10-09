# 历史代码到规范命题的登记

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
