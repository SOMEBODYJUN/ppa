# 结构性验证：实际正文的独立接收范围

日期：2026-10-13。任务为新增原始模型到完整 RLEB–GPPA 证书的结构结果；不是主稿改写或投稿合规认证。读取 AGENTS、研究协议、C249 及相邻规范定义，使用仓库 academic-writing-skills 的证明审查模式。

## 实际研究与独立复核

| 分工 | 实际阅读与完成 | 接收判断 |
| --- | --- | --- |
| `structural_kernel_theorem`，GPT-6 Astra，ultra | 从原始强凸目标与混合幂核独立推导完整纤维、同锚、真inf、物理预算、不变量、sharp阶与中心层反例 | 对应 C274；没有宣称经典方法失效 |
| `structural_cascade_theorem`，ultra | 独立推导耦合反馈 verifier；全文冷读混合核稿和 native Gram 稿，重算 G1–G5、sharp2/3、经典slice/ABS正面 | C273/C274 无 fatal gap；反馈另存候选，不抢主贡献 |
| `structural_gram_model`，ultra | 推进非zero数据且核不平移的原生矩阵模型，完整singleton、samephysicalanchor、预算、全输入点态2/3及匹配见证；补每轨道eventualABS | 对应 C273，不混同C270；最终完整文本在会话断流前已保存并由另一代理实读 |
| `structural_classical_review`，ultra | 独立重构法向增长类并攻击raw条件，实读八个一手接口；冷读最终 C272 规范全文，核所有公式、系数与C1非极小多根例 | 无fatal修补；建议明确实际output Taylor余项，最终正文已展开 |
| `structural_full_fiber_attack`，ultra | 独立复核coverage/completefiber、trueinf、物理h、radius、zero/farroot、sharpfullpointtail；给局部条件远根反例与反射失败 | C272 全域版本通过；只local版本不可接收 |
| 主代理 | 阅读各完整证明并独立重构；C273/C274规范化保持受检数学原文，C272写成自足中文正文；核代码原方程与报告量词 | 只接收本批三个精确对象，不认证整库或全球首创 |

## 逐项数学接收

| 承重项 | C272 | C273 | C274 |
| --- | --- | --- | --- |
| 完整输入coverage | coercive原始子问题供应一根；每root另定位 | strictlyconvex/coercive全部stationary=唯一min | convexsumrule、strictlyconvex/coercive全部root=唯一min |
| 完整零集/固定点/zero输入 | S完整且zero纤维singleton；任意nearzero有非min多根 | S_c完整且全部zero吸收；kernel原中心 | S完整；非光滑subdiff允许emptyoffdomain，输入仍满覆盖 |
| 同一个物理nearest锚 | p=(0,inputz)，反射三角模 | p=[c,inputb]，上下kernelinput界+comparator | p=(0,inputz)，normalwork非负 |
| 真残差 | singletongrad f，原始sector给全域EB | 物理trueEB等号；不换成kernelstep | 每个subgradient下界后取inf，不只selected值 |
| 物理提升/兼容/留域 | allrootbound先推h，显式R全部t≤R，Uall | comparator在output留域前成立，q_lambda/Theta strictbudget | 全域invariant先定位，same条带和严格物理budget |
| 定量结论 | C2近limit的双边m阶，vector只liminf/sup | fixedsolution allinput上界+同lambda见证恰2/3 | 非zero切向层q−1，SPD谱系数；center反例 |
| 经典正面 | directrootcontraction；KL适用子类可ABS | 全lambda全初值sliceclassic；每orbiteventual原fABS | classicalconvexBregman；directinvariant更短 |

## 发现并关闭的具体风险

1. 非线性 resolvent 不保持任意凸集的像；反馈候选的 Kakutani 调用改在 correctionvariables/productdomain，未沿用 stateonly 凸值错误。
2. C272 全域原始条件承重；localnormalpositive不排zeroinput的±1远根。omegaId同样会被明确合法输出否定。
3. C272 vector sharp order 不等于单个标量比值极限；C2 Taylor在实际输出点展开。C1一般只保证上界。
4. 复核中曾尝试把zero-data Gram的切向forcing估计套native nonzero-data；对象核对后撤回，不进入结果。
5. C273 uniformfullneighborhood H1障碍不等于每orbiteventual H1障碍；正面 IFT/不变量证明已加入规范。
6. C274 中心层与非zero切向层算法阶不同；nonsmooth可finiteidentification，sharp只限smooth非终止子类。

## 计算、写作及交付边界

复算 [verify.py](../code/structural_verification/verify.py) 与 [output.json](../code/structural_verification/output.json) 在本轮执行通过，代码自身哈希随输出登记。C1反算用100位Decimal，指定矩阵见证用精确缩放式和binary64，重建舍入界单独记录。不存在“网格证明完整纤维”或“数值轨道证明全称收敛”的升格。

最终规范文件的哈希与本轮接收 JSON 另存 [manifest](STRUCTURAL_VERIFICATION_MANIFEST_2026_10_13.json)。图与链接机器校验仅验证资产一致性；不承担数学证明。

受检范围已覆盖用户要求的结构研究、全输出攻击、原始参数证书、有限复算和经典重叠。主稿、摘要、排版、投稿规范不在本轮编辑范围；外部首创性、局部条件可靠排远门、一般时变核/误差、整库验收仍未关闭。没有将这些未核项目记为通过。
