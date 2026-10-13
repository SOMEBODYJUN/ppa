# 单强度临界 PPA 的复算

从仓库根目录运行：

```bash
python3 research/code/intensity_phase_critical_ppa/verify.py
```

仅依赖 Python 标准库。`Fraction` 精确核多项式分解和证书有理常数；`Decimal` 用80位有效数字核完整近端恒等式、原真残差、圆管边界、零/临界/远输入、越临界零纤维及轨道长度；平面边界绕数用 binary64 4096个节点核对。当前环境未安装 SymPy 或 mpmath，脚本明确记录这一事实。

固定 $b=\lambda=1$，同窗 $U=\{3/4<|x|<5/4\},R=1/16,\gamma=1,L=2/5,\bar t=1,\psi(q)=100q/171,\kappa=1/2$。真实完整近端为 $T(x)=|x|^{-2/3}x,T(0)=0$。结果写入同目录 `results.json`。

[候选正文]$../../candidates/intensity_phase_critical_ppa.md$ 给完整全称证明及经典正面。有限数值检查不是 coverage、误差界或指数的一般证明；本例的反射 $C=2T-I$ 无全尺度次线性 Hölder 界，使用独立大球指数入口，不能直接套 C254。
