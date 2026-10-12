# C264/C265：实际 RP² 完成与精确原管预算复算

在仓库根目录运行：

    python3 research/code/rp2_explicit_completion/verify.py

依赖 Python 3、NumPy；实际版本与脚本 SHA256 写入 results.json。seed=20261012，binary64，普通恒等式绝对诊断容差2e-10；接缝用1e-9两侧扰动、1e-6差值门。没有区间算术，不能把有限误差结果当作全域证书。

verify.py 实现完整分片 Cayley 映射，核整管三次输出、谱投影、固定轴交换子的两项正交、原始向量余量、完整反向圈、内外球接缝、球外紧支撑、管外正位移、有限全对常数，以及 C265 不同半径/指数的真实达等点对。另核零法向、相同投影、径向平方恒等式、γ=1与接近零的指数、零及非有限归一化拒绝；Fraction 反算有理预算系数。

results.json 记录实际检查数、最大误差、常数、环境和seed。精确半范数、整个无限域无新增零点、完整纤维和一般量词由[正文证明](../../canonical/rp2_explicit_completion.md)承担。程序未求最优完成常数，未证明 L*=L0 或严格 gap。

