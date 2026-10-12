# 应用筛选边界的有限算术复算

运行 `python3 research/code/model_selection_limits/verify.py`，依赖 Python 3、NumPy、SciPy，seed 266269。输出 `results.json` 记录环境、脚本 SHA256、精确 Fraction 多项式、指数端点、加权区间前缀、跨符号立方根、最近曲线有限根、向量驻点逆构、独立能量恒等式、Gram完整stationary反算和缩放t⁷族。

绑定[C266一般幂KL桥](../../canonical/generic_power_kl_bridge.md)、[C267/C268优化结构边界](../../canonical/optimization_proximal_limits.md)、[C269向量完整GPPA正面](../../canonical/vector_fenchel_classical.md)和[C270矩阵回归](../../canonical/gram_regression_gppa.md)。一般结论由相应解析证明承担。有限有理区间不能证明无限稠密构造，浮点根不能认证完整纤维，反算有限根不能证明所有政策，幂次数列不能认证最佳指数或任何公开优先。C270一步prox最佳指数仍只在[1/3,3/7]范围内，程序不关闭3/7上界。

Nearest-point 检查只用于有限样本算术；解析最近点存在、全符号、完整 coverage、留域、limiting 次微分与 KL 在规范证明中独立给出。验证不调用有利根选择或将正常误差等同真残差。
