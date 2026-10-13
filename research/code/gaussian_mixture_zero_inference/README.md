# Gaussian未知临界簇的有限攻击与解析算术

从仓库根执行：

```bash
python research/code/gaussian_mixture_zero_inference/verify.py
```

三个均值(-4,0)、(4,0)、(0,5)，权重(1,2,3)/6，λ=1/16。Fraction验证exp(18)的有限Taylor下界和整窗算术；625次数值multistart不是全根分类。

环境：Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0。未使用SymPy／mpmath。输出 [results.json](results.json) 含参数、同一常数及本机结果。运行时间随机器变化，不是复杂度或加速证明。

对应 [候选卡](../../candidates/gaussian_mixture_zero_inference.md) 是全称结论的解析依据。完整coverage、全部纤维、真实残差、最近锚、留域与指数来自证明；脚本的有限输入、网格、轨道及solver标签仅为诊断。

当前代码SHA256：

- verify.py: `fd3fe696479a466e8feb111b1fcf6b243e5a7b61210dc053dd4c14a5b576b47e`
