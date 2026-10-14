# 不同次单调与一般模：研究入口

日期：2026-10-14 UTC。比较的是同一原图、步长、目标、真残差和完整近端政策；不按名字或包含链评“本质”。

[综合报告](../../../发表成果整理/本轮重构/不同次单调与一般模路线_比较研究_2026-10-14.md)的主要裁决是：LT二次类有更早半单调同类；其他路线在函数结构、方向、参数或多值政策上确有优势；一般RL并不普遍最省，但也没有一条其他次单调的一般函数化整体取代RLEB。最有内容的后续问题是原始方向与输出相关性的保真认证。

| 分工 | 实际证明/比较范围 |
| --- | --- |
| [原变量与函数结构](primal_structural_review.md) | DG/Spingarn定义，Rolewicz一般模先行，原函数积分缺陷，正则化一致凸/非线性逆模，完整quartic及阻尼反证 |
| [逆变量几何](inverse_geometry_review.md) | co-hypo单值/coverage/松弛门，同算法diag参数优势，临界高阶余量点收敛但长度无穷，碰撞与非Lip反向例 |
| [半单调与矩阵](semimonotone_review.md) | Otero–Iusem旧tied同类，非tied/非交换矩阵配方，临界退化，Evens全多值导入与不能导入的线性条款 |
| [一般预算与压缩边界](gauge_unification_review.md) | 普适可行包络、零碰撞与远端，完整零纤维漂移，GU3固定物理C250盲区；GU1/GU3仍candidate |
| [变分序与弱Minty](variational_order_review.md) | pseudo的全覆盖/全部点收敛及无限长，quasi/cyclic失败，同锚能量及真EB，全零锚凸性与单锚不吸收 |
| [Astra独立反审](independent_verdict.md) | 先设判准再读五路全文；冷审最强换参、同算法优势、所有合法scalar排除和generalD边界，保存不支持的升级 |

[代码与执行输出](../../code/submonotonicity_routes/README.md)和[接收记录](../../audit/SUBMONOTONICITY_ROUTES_REVIEW_2026_10_14.md)分别承担有限复算与审查范围。数值不证明全称、优先或应用优势。一手文献均有公共URL、固定版本、定义/定理位置和读取边界；临时全文取证不纳入提交。

本轮不改变 C249/C250/C275/C276 身份，不新造首创定理，不改主稿/摘要/编号。新一般预算只作候选诊断；下一义务是能从原始组成/方向结构认证的新结果，而非再扩大模函数记号。
