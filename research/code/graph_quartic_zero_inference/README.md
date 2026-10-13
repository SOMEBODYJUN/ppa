# 图四次势的局部根与全根模证书

从仓库根执行：

```bash
python research/code/graph_quartic_zero_inference/verify.py
python research/code/graph_quartic_zero_inference/modular_verify.py
```

维度13、J=1/4、bias分母1000、λ=1。默认 --starts 17 --select 16；seed20261013。--starts 128只是可选非穷尽探索，88等观察数不是准确计数。局部和模门用Fraction准确算术，候选发现用float64。

环境：Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0。未使用SymPy／mpmath。输出 [results.json](results.json) 含参数、同一常数及本机结果。运行时间随机器变化，不是复杂度或加速证明。

对应 [候选卡](../../candidates/graph_quartic_zero_inference.md) 是全称结论的解析依据。完整coverage、全部纤维、真实残差、最近锚、留域与指数来自证明；脚本的有限输入、网格、轨道及solver标签仅为诊断。

[modular_results.json](modular_results.json)另记录13阶exact determinant、mod3、小维商环与退化／非法分母攻击。共同 [代数附页](../../candidates/graph_quartic_modular_certificate.md) 完整证明mod3单位身份，不生成指数阶矩阵。

当前代码SHA256：

- modular_verify.py: `10ef0ec461d7e2ffbe637bb129fe2121ab399cfe9bffc78967c4955cf902268d`
- verify.py: `91d16d5ad7dccad2b73fa9253f9f81ab5a06795872cf884517edbba3a7689103`
