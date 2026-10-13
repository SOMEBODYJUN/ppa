# 有向双稳态网络的部分根推断

从仓库根执行：

```bash
python research/code/directed_bistable_zero_inference/verify.py
```

维度13，a=7/25，c=11/50，bias分母1000，λ=1。seed20261013的18个局部动力提出步骤认证16根；seed20261014的366次后核初值得到15个负指数见证。Fraction精确验证，数值发现与近端反算为float64。

环境：Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0。未使用SymPy／mpmath。输出 [results.json](results.json) 含参数、同一常数及本机结果。运行时间随机器变化，不是复杂度或加速证明。

对应 [候选卡](../../candidates/directed_bistable_zero_inference.md) 是全称结论的解析依据。完整coverage、全部纤维、真实残差、最近锚、留域与指数来自证明；脚本的有限输入、网格、轨道及solver标签仅为诊断。

16个stable证书为精确残差＋LDL＋局部外向degree；15个negative证书为精确逆矩阵＋Banach不等式＋determinant符号。两类存在证明不能混淆。全部中心是有理数，详细证书在JSON。后发现15个见证不证明未见零点穷尽。

当前代码SHA256：

- verify.py: `4f71597b2e84bad0fdbd36cb712115c0a47a75962cd3515705b284991f024711`
