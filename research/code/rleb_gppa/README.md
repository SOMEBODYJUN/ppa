# 物理 RLEB–GPPA 有限复算

运行 `python3 research/code/rleb_gppa/verify.py`，只需Python标准库，结果写同目录results.json。固定网格，无随机seed；Fraction做普通多值PPA、单射边界与能量精确项，binary64用于100轮独立二分的非线性核、有限几何尾、幂预算；close容差2e−11乘尺度，局部边界另用1e−10诊断。实际4603项通过，脚本hash与Python版本由输出生成。

完整证明见canonical/physical_rleb_gppa.md；有限检查不证明全量词或无限步结论。
