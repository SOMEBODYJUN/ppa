# 次单调路线：可复算验证

从仓库根目录运行：

    python3 research/code/submonotonicity_routes/run_all.py

[run_all.py](run_all.py) 实际调用六个独立验证器，保存 [all_verifiers_output.json](all_verifiers_output.json)。每项有返回码、完整 stdout/stderr、脚本 SHA256 和 Python 版本；因此不依赖聊天中的临时输出。标准库脚本无需安装依赖；根代理的 route_bridge_verify 另使用已安装 NumPy，版本写入其结果。

| 验证器 | 对象和实际边界 |
| --- | --- |
| [primal_verify.py](primal_verify.py) | Fraction 四次恒等式；临界完整立方根近端；DG/LT量词反例；正/负阻尼完整反代与轨道 |
| [inverse_verify.py](inverse_verify.py) | 同F同lambda的diag精确常数；零/远端/步长临界；三次逆图10^5步及无限长度的解析渐近反算 |
| [semimonotone_verify.py](semimonotone_verify.py) | Fraction逐变量二次多项式的张量插值恒等式；非交换有理矩阵配方；多值同输入和负参数退化 |
| [gauge_verify.py](gauge_verify.py) | 普适包络远端攻击；critical cubic；GU3的4096个12步完整分支前缀；零纤维漂移 |
| [order_verify.py](order_verify.py) | quasi完整负支；pseudo多纤维；200000步径向旋转及无限长度渐近；单零锚/全零集与循环恒等式 |
| [route_bridge_verify.py](route_bridge_verify.py) | 根代理714个同图换参、500个平移Cayley恒等式、6138个10层完整分支转移；强EB/fullcoverage的cusp失败；compact-convex零纤维漂移 |

Fraction部分精确；浮点部分为 binary64，容差按各脚本断言明列。随机样本的 seed 为20261014，其他为确定网格；逆图临界轨道为100次二分，order轨道为65次二分。根桥的环境、参数、容差和脚本哈希另存 [route_bridge_output.json](route_bridge_output.json)；order实跑结果另存 [order_verify_results.json](order_verify_results.json)。完整 stdout 均以统一输出为本轮接收依据。

finite run不是图纤维或无限政策的枚举。全称覆盖、所有输出、非收敛、无限长度、参数必要性、同图等价及任意合法模排除，均由[报告正文](../../novelty/2026_10_14_submonotonicity/README.md)的解析证明承担。它们不认证世界首创、应用工作量或主稿发布。
