# C259–C263的有限复算

从仓库根运行：

```bash
python3 research/code/natural_advantage/verify.py
```

Python标准库；实际Python3.12.14，seed20261012，Fraction有理余量与80位Decimal。结果与脚本SHA256保存于[results.json](results.json)。

| 范围 | 实际检查 | 不承担的全称结论 |
|---|---|---|
| C259经典正面 | 同R10⁻⁴的远输出反证、动能/Bregman余量、336系数和能量缩率算术 | 所有驻点、闭图紧性与无限长度由[规范证明](../../canonical/amplitude_classical_energy.md)负责 |
| C260完整反馈 | v1 R10⁻¹²与v2 R10⁻⁴三轮吸收、同组全窗/预算及normal/EB余量；720个全维球投影和skew表示；100个校准polarization算术 | 全部输入/反馈/远纤维/全部根和留域由[OF1–26](../../canonical/orthogonal_feedback_rleb.md)负责 |
| C260sharp与全局增能 | 七个逆定义sharp族80位反算及极限商；准确η5增能一步的逆代、能量严格界 | 不把该管外一步当任意小认证管内增能；最佳指数/尖常数由解析上下界证明 |
| C261 | 六个Γ/R边界元组辅助前驱与步长余量、三个Γ的六个正负有理圆弦反算 | 不由有限元组证明C¹或强链式能量不可能；[全称反证](../../canonical/smooth_kl_full_relation_obstruction.md)承担该结论 |

| C262人工KL桥 | 稠密区间预算与大窗H1 α.9的有理系数 | 稠密性、全部limiting次梯度、KL/H3由[AK1–6](../../canonical/artificial_kl_energy_bridge.md)解析证明 |
| C263临界门 | 十一个η的正负/零临界闭式输出，80位反算实际零输入；A11与远门/局部门严格比较 | 全n零纤维穷尽、临界恰三根和所有实参数iff由[CG1–4](../../canonical/orthogonal_feedback_critical_gate.md)负责 |

最高相对残差误差约4.56·10⁻¹⁶；Decimal反算误差<10⁻⁶⁰。没有用数值root搜索或单条轨道冒充完整近端纤维。
