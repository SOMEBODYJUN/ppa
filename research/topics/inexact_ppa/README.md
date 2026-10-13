# 非精确 PPA：内层精度设计

本方向固定原算子与物理空间，区分真实图方程缺陷、精确输出误差、扩大算子残差及核误差。当前保留一个贡献包：**可计算的停止余量与完整关系下的锐精度边界**。

| 结果 | 正文与准确身份 |
| --- | --- |
| C275-v1：真实图接受关系的可计算证书 | [停止定理](real_graph_stopping.md#igs-theorem)：反射逆模给输入距离下界，真实 EB 给输出距离上界；全部接受输出的覆盖、零吸收、有限长度与留域。已知常数/图成员资格仍为前提 |
| C276-v1：临界 Hölder 完整精度边界 | [完整模型](sharp_precision_frontier.md#isp-object)、[全部接受纤维及锐帽门](sharp_precision_frontier.md#isp-frontier)、[幂次三分界](sharp_precision_frontier.md#isp-power)、[远端与经典条件](sharp_precision_frontier.md#isp-classical-boundary)。模型是诊断机制例，精确动态有 Hölder 共轭 |
| 自然验证基准 | [非势循环博弈](../../candidates/inexact_cyclic_game_benchmark.md)：任意原始数据的未知唯一 Nash 点、完整非精确输出；独立证明已核，但同算法被经典逆亚单调/直接收缩恢复，不作独占优势 |

较广的统一误差预算和物理 GPPA 转接保留在[推导草案](../../candidates/inexact_rleb_forcing.md)，不是主稿已经采用的结果；核不可见运动仍须物理提升。[HPE／松弛／分裂筛选](../../candidates/inexact_hpe_split_interfaces.md)和[应用筛选](../../candidates/inexact_application_selection.md)解释未升格方向。

[成果报告](../../../发表成果整理/本轮重构/非精确PPA迁移_成果与独立评判_2026-10-13.md)、[独立接收](../../audit/INEXACT_PPA_REVIEW_2026_10_13.md)、[复算](../../code/inexact_ppa/README.md)与[逐篇先行性](../../novelty/2026_10_13_inexact/primary_review.md)分别保存证据。最严价值判断见[Astra独立评判](../../novelty/2026_10_13_inexact/final_value_review.md)。

数学状态与新颖性分开：当前结果内部 derived-checked；充分定理的短证明为标准小增益/事后证书思想，较有分量的是完整精度边界。Wang–Li–Ng 2023 完整原文尚未取得，国际优先权未穷尽。最大单调、逆亚单调、现代 HPE 和 Hölder 坐标变换的正面恢复均保留，不宣称排除整个经典理论或已解决自然困难应用。

下一门：真实内层算法的终止/复杂度与认证成本；近似图成员资格误差；精确先行检索；在自然非 Lipschitz 模型中认证本合同的成本优势。主稿、摘要与已有编号未改。
