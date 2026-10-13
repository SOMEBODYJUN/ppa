# Schlögl 非负完整 PPA 复算

运行（Python 3.11+，仅标准库）：

```bash
python3 research/code/schlogl_bistability_ppa/verify.py
```

结果写至同目录 `results.json`。80位 Decimal 重算全部选定输入，包括 \(-6\) 正常锥接缝和2处立方根奇点；核完整包含、能量下降、大球端点和局部反射/真残差/步长。Fraction 核验多项式身份及全部显式常数的有理算术。另检查 \(\lambda=2\) 的中间零输入三个真实正输出，以及全域反射线性增长的负输入见证。没有随机 seed。

全称覆盖和唯一性、管自映、大球总指数以及全域反射 Hölder 失败由 [候选卡](../../candidates/schlogl_bistability_ppa.md) 的解析推导证明。有限点计算不证明外部优先或一般参数族，也不能把边界正常锥多值替换成近端多值。
