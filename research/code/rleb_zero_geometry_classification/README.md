# 零集几何分类的有限精确复算

命令：在仓库根目录运行 `python3 research/code/rleb_zero_geometry_classification/verify.py`。

环境：Python 3.12.14；仅标准库；所有断言使用整数或 `fractions.Fraction` 精确算术，无随机参数。输出写入 `results.json`。

检查对象：九组补集 Euler／指数算术；凸方形完整近端的双向反算、零输入、边界、角点及坐标达 100 的远端输入；全部采样点对的反射非扩张与 Hölder 界；同一方形的 12 步精确轨道；管模型的窗口与严格长度预算；四组 quartic 对完整零集的距离扩张反算；任意闭集投影机制在双点集合上的完整反纤维（含零输入的两个输出）、远端输入与共有证书系数。

区域 Euler 数由报告中的解析拓扑识别给定，程序只核符号与加法。没有用有限点对证明全局界，也没有实现 Hopf 完成、一般指数或 ENR 识别算法。全称证明见 [分类研究](../../../发表成果整理/本轮重构/RLEB零集几何分类研究.md) 与 [分量分类卡](../../candidates/rleb_component_index_classification.md)。

正向几何图：`RLEB_CJK_FONT=/path/to/NotoSansCJKsc-Regular.otf RLEB_FIGURE_DIR=发表成果整理/本轮重构/图件 python3 research/code/rleb_zero_geometry_classification/draw_geometry.py`。未指定已有字体时自动从 Noto CJK 官方仓库下载。输出 PNG、PDF、SVG；半径、边界、严格预算、反算与文字裁切在脚本中检查，图另经可视核验。准确的条件与图示意义见[图注](../../../发表成果整理/本轮重构/RLEB零点集合直观特征_图注.md)。

有限分叉的完整实现：`python3 research/code/rleb_zero_geometry_classification/verify_cross.py`，输出 `cross_results.json`。已跑 137 个精确输入、9316 个精确点对；125 个输入验证了完整有理轨道停驻，另 12 个远端输入验证精确径向上界。后续实际范数可能无理时，不伪造有理轨道。零输入、两坐标大小相等、端点截断、球边界、所有符号分区、远端和非单调图点均包含。全称覆盖、完整零集、真残差屏障及有限进入由[十字证明卡](../../candidates/rleb_cross_zero_set.md)承担；没有实现全部反输入的通用求解器。
