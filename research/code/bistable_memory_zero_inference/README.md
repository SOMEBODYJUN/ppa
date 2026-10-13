# 六个记忆态的解析门与完整近端反算

从仓库根执行：

```bash
python research/code/bistable_memory_zero_inference/verify.py
```

维度8、三个正交±1模式、γ=3/10、λ=16/19、bias分母1000。六球根存在来自卡中的解析边界极小化，脚本准确验证共同scalar gates、有限近端反算及超临界七个完整见证。

环境：Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0。未使用SymPy／mpmath。输出 [results.json](results.json) 含参数、同一常数及本机结果。运行时间随机器变化，不是复杂度或加速证明。

对应 [候选卡](../../candidates/bistable_memory_zero_inference.md) 是全称结论的解析依据。完整coverage、全部纤维、真实残差、最近锚、留域与指数来自证明；脚本的有限输入、网格、轨道及solver标签仅为诊断。

当前代码SHA256：

- verify.py: `3de824f3d12e032244bc945cd890c2410d6dda65b1dd3281c56f56d871d6b3b8`
