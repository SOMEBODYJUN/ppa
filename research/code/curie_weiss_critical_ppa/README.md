# Curie–Weiss 临界完整 PPA 复算

运行（Python 3.11+，仅标准库）：

```bash
python3 research/code/curie_weiss_critical_ppa/verify.py
```

结果写至同目录 `results.json`。80位 Decimal 对有限输入重算完整方程、能量下降、全尺度反射 Hölder 立方式、局部反射/真残差/位移和临界立方阶；Fraction 核验显式指数 Taylor 正项下界、兼容和长度预算。没有随机 seed。

完整全域覆盖、严格单调、全称 Hölder 界和固定点指数以 [候选卡](../../candidates/curie_weiss_critical_ppa.md) 的解析证明为依据。有限点输出不能证明全称命题或外部优先；数值正根只作读图参考。程序不使用零点处不存在的近端导数。
