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
