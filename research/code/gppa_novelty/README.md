# 首创性审查的有限复算

这些脚本只检查显示恒等式、指定完整对象和有限参数，不证明全球先行性、全称框架覆盖或无穷长度判据。一般证明在 [C218](../../canonical/gppa_almost_averaged_bridge.md)、[C219](../../canonical/gppa_spiral_resonance.md)、[C220](../../canonical/gppa_regularized_inverse_branch.md) 及 [分报告](../../novelty/2026_10_09/README.md) 中；[独立审查](../../novelty/2026_10_09/new_claim_review.md)与数值证据分开。

从仓库根运行以下命令，Python 标准库，无外部依赖或随机抽样：

```bash
python3 research/code/gppa_novelty/almost_averaged_check.py
python3 research/code/gppa_novelty/core_prior_art_check.py
python3 research/code/gppa_novelty/spiral_resonance_check.py
python3 research/code/gppa_novelty/stability_review.py
python3 research/code/gppa_novelty/structure_check.py
```

| 脚本 / 结果 | 精度、参数、断言与盲区 |
| --- | --- |
| [almost_averaged_check.py](almost_averaged_check.py) / [JSON](almost_averaged_results.json) | Fraction精确216组线性向量恒等式、48组scalar真EB取等、SF正常输入和对角双Lipschitz下界、LTT violation窗；无浮点容差。有限序列不证明发散 |
| [core_prior_art_check.py](core_prior_art_check.py) / [JSON](core_prior_art_results.json) | Fraction线性AA/submonotone系数，Decimal70位四个正常输入的比值与所需violation；q=3/5、log uniform-shrinking比率下界。数字是解析证明的有限示例 |
| [spiral_resonance_check.py](spiral_resonance_check.py) / [JSON](spiral_resonance_check.json) | Decimal90位、Fraction Bernoulli系数、EM order20/shift256，Machin π和三角级数；q=3,3.5,10，k=10,100,1000,10000，含正负共振、0及非共振。解析截断界不包含Decimal舍入，容差1e−80；不是区间证明 |
| [stability_review.py](stability_review.py) / [JSON](stability_review_results.json) | Fraction核抵消、法锥一步取等、标量完整恒误差精确管和先行同对象预算；binary64复数核五个α和四个k的谐波轨道及族最大点，明示1e−9/1e−10量级容差。只验证指定子族，不给全类锐性 |
| [structure_check.py](structure_check.py) / [输出](structure_results.txt) | Fraction核优化指数，binary64对γ=1/4,1/2,3/4计算sharp/net/Ajiev预算；固定3×3×5组预算、三个simplex维数和一个覆盖根，容差1e−12。不证明一般固定集构造或全球优先性 |

[verification.json](verification.json) 保存实际命令、环境、退出码、stdout/stderr、脚本与正文指纹；另外复跑旧 C208–C214 与 C215/C216 验证器，检验新增入口未破坏原算术接口。先行全文只用于临时阅读，不随研究资产发布。


## 本次四路接续复算（C221/C222与双方来源桥）

[followup_verification.json](followup_verification.json)是本次真实94cbbbd基线的命令/环境/退出码/stdout/指纹记录，初轮verification.json保持原范围。运行：

```bash
python3 research/code/gppa_novelty/gppa_source_priority_check.py
python3 research/novelty/2026_10_09/nfb_source_priority_check.py
python3 research/code/gppa_novelty/noncalm_coverage_followup_check.py
python3 research/code/gppa_novelty/structure_priority_check.py
```

| 程序 | 有限检查、精度和边界 |
| --- | --- |
| [GPPA来源](gppa_source_priority_check.py) | stdlib Fraction确定性26244值对、ASM/原非单调、核轨道、q与预算、small-ε门；不把物理距离率改为点率 |
| [NFB来源](../../novelty/2026_10_09/nfb_source_priority_check.py) | Fraction78系数、36步更新同一性、36平方和及两个准确证书；参数改善只对RV-v1 |
| [非calm/势桥](noncalm_coverage_followup_check.py) | Fraction441能量恒等式、Decimal70位132尾恒等式，4个SFsector含等号和1280 signed样本，180能量scalar步、4096隐式递推及12 dyadic块；binary64等号误差明确给出，不证明无穷结论 |
| [结构精确预算](structure_priority_check.py) | seed222031004；Fraction部分精确scalar及binary64反演/方差/Hölder门、102710 scalar和55945重构检查，容差在脚本明写；不以随机有限点证明全参数边界 |

承重解析证明见[C221](../../canonical/gppa_tail_lyapunov_bridge.md)、[C222](../../canonical/sharp_holder_lipschitz_realization.md)和[先行复核](../../novelty/2026_10_09/PRIORITY_FOLLOWUP.md)。C¹ no-go、经典导入和全球日期判断不由有限计算代替。
