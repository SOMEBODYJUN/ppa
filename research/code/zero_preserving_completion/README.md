# C233–C235 的有限复算范围

从仓库根运行 `python3 research/code/zero_preserving_completion/verify.py`。
依赖 NumPy；实际 Python/NumPy 版本、seed 20261011、结果及诊断误差在 results.json。

Fraction 精确枚举闭输入半径0至1/8和四个步长，反算三次EB系数、输出半径、局部残差及非局部输入下界。NumPy binary64 在 Sym_0(3) 的500组法向输入核 Veronese嵌入、谱投影、三次法向收缩、独立逆输入和完整近端图包含。含零半径、闭管边界、重复下特征值、重复最大特征值的失败检测。几何绝对容差2e-12；逆三次根可能放大输出舍入，另给2e-7诊断容差，实际最大误差记录于结果。100位Decimal检查极小半径递推，避免把矩阵减法的下溢当数学零；凸拼接有限样本独立核三角不等式机制。

该程序没有实现全局Hopf延拓器。它不证明拓扑定理、一般无零完成、无限时间收敛或全称完整纤维结论；承重证明在[规范正文](../../canonical/zero_preserving_completion.md)。矩阵示例的reach只证明下界，不声称精确值。
