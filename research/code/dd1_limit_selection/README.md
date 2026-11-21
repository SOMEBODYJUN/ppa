# C462 的固定模型复算

证明入口：[完整 DD1 与极限解选择](../../topics/dd2/limit_selection_stability.md#dd1-limit-selection-stability)。

运行 `python3 research/code/dd1_limit_selection/verify_limit_selection.py`。
只使用 Python 标准库 Decimal（120 位）和 Fraction；固定 B=R=1/4、r0=1/8，
无随机数、无 seed、无外部输入。56 个正负法向/切向点核完整逆的往返、
真残差、锚界和 DD1 收缩；六个固定初值 ε=exp(−z)，z=16,64,256,1024,4096,16384，
输出首次饱和时刻及 −log 极限差与 √z 的比值。
实际 Python 版本、脚本 SHA256 与数值输出均保存于 `results.json`。

饱和后的截断由解析上界 B*r/(1−R) 控制，程序在该界不超过当前切向和的
10^(−105) 时停止。Decimal 使用默认最近偶数舍入，输出不是有向舍入区间证书；
普遍量词、精确零集、同胚性、Q-二次和非 Hölder 结论均依赖正文证明。
