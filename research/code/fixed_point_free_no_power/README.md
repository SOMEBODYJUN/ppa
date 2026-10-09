# C223 的精确有限复算

运行：`python3 research/code/fixed_point_free_no_power/verify.py`。
依赖仅 Python 标准库。参数为正文固定值；全部计算使用 `fractions.Fraction`，没有随机抽样、浮点误差或 seed。固定前八个三点块及原点，枚举完整二状态积空间的全部有序状态对。检查源期望不等式、同步残差恒等式、标签单射、无共同固定点、T³=T、四状态模型的全部 0–80 次矩阵幂/非负混合恒等式，以及见证成本与最近 recurrent 支撑下界。退化 e=0 明确检查标签碰撞；小正指数另外反算 log₂ 幂式。

`results.json` 为一次实际运行的环境和输出。这里的有限计算只是证据；无限状态、所有概率律与全部正幂的证明在 [规范正文](../../topics/random_markov/fixed_point_free_no_power.md)。不把有限检查提升为定理证明。
