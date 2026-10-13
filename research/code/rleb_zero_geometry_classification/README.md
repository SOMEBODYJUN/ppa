# 零集几何分类的有限精确复算

命令：在仓库根目录运行 `python3 research/code/rleb_zero_geometry_classification/verify.py`。

环境：Python 3.12.14；仅标准库；所有断言使用整数或 `fractions.Fraction` 精确算术，无随机参数。输出写入 `results.json`。

检查对象：九组补集 Euler／指数算术；凸方形完整近端的双向反算、零输入、边界、角点及坐标达 100 的远端输入；全部采样点对的反射非扩张与 Hölder 界；同一方形的 12 步精确轨道；管模型的窗口与严格长度预算；四组 quartic 对完整零集的距离扩张反算；任意闭集投影机制在双点集合上的完整反纤维（含零输入的两个输出）、远端输入与共有证书系数。

区域 Euler 数由报告中的解析拓扑识别给定，程序只核符号与加法。没有用有限点对证明全局界，也没有实现 Hopf 完成、一般指数或 ENR 识别算法。全称证明见 [分类研究](../../../发表成果整理/本轮重构/RLEB零集几何分类研究.md) 与 [分量分类卡](../../candidates/rleb_component_index_classification.md)。
