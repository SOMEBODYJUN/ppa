# C144 公开必要性问题接口的精确有限复算

对应 [选题与证明接口](../../topics/random_markov/public_necessity_target.md#pnt-c144)，保持 C144 原身份；未新建重复数学 Claim。

运行：`python research/code/public_problem_bridge/verify.py`。Python 标准库，`fractions.Fraction` 精确算术，无随机性、seed 或浮点容差。结果保存在 [results.json](results.json)。

实际检查：625 对有理网格状态的期望 firmness 恒等式；35 个四状态四分之一质量律的 `P²=P`；六个含 `t=0,1/2` 边界的参数，各枚举两源至最近目标及实际极限目标的全部运输顶点，反算 `t²,2t²` 成本与最优零同步残差，并核更新后到指定固定不变律的距离不下降。

边界输入的有限检查不扩大原 C144 `0<t<1/2` 的 canonical 见证范围。任意连续律、全部不变目标的全局最近性、一般问题量词和发表先行性须读规范证明与一手来源；`PASS` 不证明它们。
