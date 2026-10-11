# 应用候选的有限复算

从仓库根目录运行：

```bash
python3 research/code/natural_gppa/verify.py
python3 research/code/natural_gppa/circle_verify.py
python3 research/code/natural_gppa/damping_verify.py
```

只用 Python 标准库，实际环境 Python 3.12.14。输出分别为 [results.json](results.json)、[circle_results.json](circle_results.json) 和 [damping_results.json](damping_results.json)，各含脚本 SHA256、参数、实际误差及作用域；结果指纹随 Git 保存。

| 程序 | 计算范围 | 明确盲区 |
| --- | --- | --- |
| [verify.py](verify.py)，C255 | seed20261011；10015核输入、20000物理两点、35完整边界/等号/远输入；binary64单调根反算与80位Decimal尖点、精确轨道递推、1/2锐两点族，Fraction临界预算 | 不以有限样本证明所有纤维、最优指数上界或无限长度；这些在规范页解析证明 |
| [circle_verify.py](circle_verify.py)，C256 | 无随机；Fraction认证共同元组、中心排除、Young算术、真实EB、整窗端点与单调公式、预算及替代能量系数；六种尺度、五种有理旋转、三输出共90个80位Decimal逆代，另核圆弦LT/H1见证 | 不搜索全空间驻点、不用数值极小点穷尽完整纤维；exact-three穷尽、所有远输出、一般全称和无限轨道由规范证明负责 |
| [damping_verify.py](damping_verify.py)，C257 | 无随机；80位Decimal核Γ=10^−12至10^6的八个正参数全元组、16个指定κ元组，包括远纤维间隙、EB分母、整窗和严格预算；四个中心出现边界、三个负阻尼旋转轨道逆代、Fraction核中心半径临界系数 | 不由有限参数认证所有实Γ或锐临界门；完全显式公式、Γ>0 iff及渐近最优系数由参数规范页承担 |

C256 最大逆代误差为2·10^−80，诊断容差10^−65；C255方程最大误差约1.11·10^−16，主窗诊断容差10^−14，远输入10^−10。二分根不是通用闭式prox，也不供应完整性证据。

C255检查器另用Fraction核直接物理父定理的R10^−9同窗/锚与严格预算余量，用80位Decimal复核Θ(R)≈.01832173<39/2000<1/8。直接物理接口的所有输入、所有输出与同锚量词由PBG17–20承担。

规范对象：[C255退化核](../../canonical/perspective_bregman_gppa.md)、[C256圆幅值](../../canonical/amplitude_circle_hamilton.md)、[C257锐阻尼门](../../canonical/amplitude_circle_damping_threshold.md)。C255被淘汰为“旧线性理论无法分析”的推荐，原因是已经找到经典正面路径；计算PASS不改变此裁决。比较范围见[应用筛选](../../../发表成果整理/应用优势导向的候选筛选.md)。
