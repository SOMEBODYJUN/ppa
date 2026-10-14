# 当前论文大纲的复算

仅核当前大纲的结构、已显示代数和边界实例，不注册新 Claim。

从仓库根目录运行：

```bash
python3 research/code/author_outline_review/verify_author_structure.py
```

依赖 SymPy 1.14.0；本次环境可在命令前加 `PYTHONPATH=/workspace/scratch/cabc4e00b63a/ppa_math_deps`。运行环境 Python 3.12.14，参数固定，无随机数；符号及有理算术精确，Decimal 显示精度80位。

唯一输出为 `author_structure_results.json`，绑定当前大纲及脚本哈希。检查第一章完整前置内容、RL等价引理、普通PPA主定理、独立假设3／定理3、第三章具体比较和第四章结果安排；代数包括RL／J侧余量、Luke–Tam预算比较、近端反算、完整多值、真实残差、弱凸接缝、核物理反例、锐性及临界参数。包含零输入、跨符号、边界与远端输入的有限复算；全称结论以大纲中的解析证明为准。
