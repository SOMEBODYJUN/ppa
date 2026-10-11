# C245 的参数复算

运行：

```bash
python3 research/code/lipschitz_obstruction_budget/verify.py
```

程序只用 Python 标准库和 `fractions.Fraction`，反算 C245 的 RP² 参数：\(\rho=1/8\)、谱隙、投影微分上界、\(D_0\) 与 \(C_0\) 的 Lipschitz 上界、内边界幅度和 (LB3) 的代数化。它不构造球值方向延拓，不证明 \(K_e\) 的数值，也不证明原预算端点达到；这些仍是正文中的条件义务。

