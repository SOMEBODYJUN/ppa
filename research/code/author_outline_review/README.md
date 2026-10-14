# 作者逐节大纲：复算说明

范围：2026-10-14 的大纲和团队核查。代码不注册新 Claim，不修改主稿。

从仓库根目录运行：

```bash
PYTHONPATH=/workspace/scratch/cabc4e00b63a/ppa_math_deps python3 research/code/author_outline_review/verify_outline_math.py
python3 research/code/author_outline_review/sharp_scope_verify.py
```

第一个脚本需要 SymPy 1.14.0；给出的 `PYTHONPATH` 指本次环境中的已安装依赖。在其他环境直接安装 SymPy 后运行该脚本即可。第二个脚本只用 Python 标准库。运行环境 Python 3.12.14，参数在脚本中固定，无随机数；代数用精确符号与有理数，根式显示用80位 Decimal。

输出分别为 `outline_math_results.json`、`sharp_scope_results.json`，均已复算并保存。第一个检查同窗参数差值、完整旋转逆映射、短多值完整输出与真残差、弱凸目标接缝和径向近端反算、非单射核的合法不收敛物理轨道。第二个检查完整锐性族、旋转参数边界、临界锚定反例和三角证书。

零输入、跨符号、认证边界、接缝和远端输入均有具体测试。数学量词与证明范围以大纲和四份团队报告为准，有限算术不证明全部输入结论。报告里的临界新反例仅在锚定类别成立；不得据此升级为同常数全对 RL 的反例或新增规范定理。
