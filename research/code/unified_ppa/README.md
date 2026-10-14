# 联合次单调 PPA 的本批复算

在仓库根运行：

~~~bash
python3 research/code/unified_ppa/run_all.py
~~~

[完整输出](all_verifiers_output.json)记录每条命令、Python版本、退出码、stdout/stderr和脚本SHA-256。四个专属脚本只用标准库；raw_verify.py 另需 NumPy（本次 2.3.5）。没有随机seed。Fraction是精确有理算术；明确标为浮点的部分用Python binary64及脚本列出的容差。raw脚本另保存[自身结果](raw_verify_output.json)。

| 脚本 | 有限验证对象 | 解析证明 |
| --- | --- | --- |
| [joint_verify.py](joint_verify.py) | Gram恒等式、semimonotone参数、慢支逆平方、GU3、壳层势、nilpotent两步与状态势 | [C277/C278](../../canonical/unified_ppa_joint_certificates.md) |
| [raw_verify.py](raw_verify.py) | 非交换矩阵完成平方、有理LMI主元/行列式、diagonal及扰动、signed余项、完整两个GU3分支、临界逆图和交替SPD | [C279/C280](../../canonical/unified_ppa_raw_calculus.md) |
| [coverage_verify.py](coverage_verify.py) | 预算反算、极大图整数层、相邻两球缺口、非负型核值3/8、临界恢复degree的显式机制 | [C280/C281](../../canonical/unified_ppa_coverage.md) |
| [curved_verify.py](curved_verify.py) | 圆径向反算、曲率临界、zero/内外符号、精确与二次补偿、共同显式半径 | [C282](../../canonical/unified_ppa_curved_geometry.md) |
| [inexact_verify.py](inexact_verify.py) | cohypo剖面、类级临界旋转、GU3全方向政策、联合长度、固定/移动投影极值、统一SPD精确发散、membership预算 | [C283/C284](../../canonical/unified_ppa_inexact_interfaces.md) |

每个脚本头部/输出写定参数、算术种类与误差。有限网格不能证明全部输入、全部纤维、全政策收敛、最优模或公开先行性。全部全称由对应规范正文中的解析证明、完整关系恒等式或明列经典定理承担。机器PASS与独立数学冷审分别登记。
