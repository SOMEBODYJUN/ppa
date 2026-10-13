# 第四章非主选／失败候选的有限检查

对应 [总筛选报告](../../../发表成果整理/本轮重构/应用候选筛选报告.md) 的秩二、倾斜双阱、半幂稀疏和硬 Procrustes 项。原算法和全称反例在报告中解析说明；代码不把数值轨道或点云变成证明。

仓库根运行：

```bash
python3 research/code/application_candidate_screen/verify.py
```

Python3.12.14，NumPy2.3.5；固定 seed20261013，倾斜双阱为 Decimal80位。程序运行两个明确分开的辅助检查后，验证500个秩二物理管输入、全部部分等距秩的固定实例、Procrustes目标零输入的四完整符号分支及奇异输入的流形纤维实例。辅助 `classical.py` 另检查半幂驻点方程和 global-min 阈值；后者不是完整驻点近端，结果独立标识。`tilt.py` 检查4002个局部输入和原 h=3/8 的兼容门失败。

输出为 `results.json`、`classical.json`、`scalar_tilt_results.json`。有限 SVD 实例没有认证全部低秩簇局部指数；原报告的该未核范围保持。跨符号、零、临界、远端和多输出的普遍结论仍由各模型的完整解析方程承担。
