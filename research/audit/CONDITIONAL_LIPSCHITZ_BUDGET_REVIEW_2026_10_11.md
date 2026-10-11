# C245 条件预算桥接收记录

日期：2026-10-11。两路独立审查分别攻击了 C242 的拼接、量词和研究价值；意见已反映到规范正文。

## 接收范围

- `research/canonical/lipschitz_obstruction_budget.md` 的 C245-v1、LB1–LB3；
- `research/code/lipschitz_obstruction_budget/verify.py` 及其 `results.json`；
- 与 C233、C240 的依赖及 `CLAIMS.md`、`RESEARCH_STATE.md`、`README.md`、`research/graph.json` 的新增去向。

## 攻击与修补

1. C233 的原始合同只给 Hölder，不自动给整管 Lipschitz。C242 已明确增加 `D0/C0` 在整管上的 Lipschitz 前件；RP² 光滑模型满足它。
2. 分片函数的全局 Lipschitz 界不能只引用各块常数。正文把 `G_W` 定义为固定三块及其统一法向 collar 的 seam-gluing 常数，并把外部零块包含在定义中。它是几何常数，未被误称为已算出的数值。
3. 支撑外点不一定满足距离 ≤`2R`。正文先用跨接缝的全域 Lipschitz 界，再按距离是否超过 `2R` 分段；Hölder 反算只对支撑内点直接使用直径 `2R`。
4. RP² 标量接缝函数必须保持正幅度。正文现要求 `0≤τ≤1`；因此 `a=(1−τ)a_in+τ` 正且 `A=1`。
5. C245 是条件定量桥，不是 RP² 原预算结论：没有构造或认证 `K_e`、`G_W` 的最优值，也没有推出 `L*=L0`、端点达到或全域收敛。
6. RP² 的投影常数采用保守的全域管上界 `K_Pi≤4/(1−2ρ)=16/3`，由小距离的 Davis–Kahan 界与大距离的平凡投影界分段得到；因此复算中的 `K_D0=1235/192`、`K_C0=1331/96` 与正文一致。

## 结论

C242 以 `derived-checked` 的**条件引理**接收。它的独立价值是把“给定无零方向延拓”转成明确的有限 Hölder 预算接口；主研究门仍是 RP² 原预算下的真实覆盖/余量或严格 gap。

