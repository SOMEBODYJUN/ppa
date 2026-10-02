# 当前研究状态

本页只记录**现在**可执行的研究前沿与阻塞。精确陈述和状态见 [Claim 总账](CLAIMS.md)，公式及证明见各主题正文，合取边见 [逻辑契约](research/LOGIC_CONTRACTS.md) 和 [超边图](research/HYPERGRAPH.md)。来源谱系和语义覆盖任务在 [审计区](research/audit/SEMANTIC_INVENTORY_PLAN.md)；不要求先阅读 `history/sources/` 才能理解已重写的命题。若某条仍标 `source-report` 或 `candidate`，不得把来源目录当作缺失的规范证明自动补齐。

<a id="active-frontier"></a>
## 活跃前沿与完成门

| 方向 | 已可直接调用的规范内容 | 精确未闭义务 / 完成门 |
| --- | --- | --- |
| **总体规模比较** | [D01–D04](research/foundations.md)、[固定紧 T-only 观测的证明](research/canonical/compact_t_observation.md#ct-proper)、[σ-紧 Baire 诊断](research/canonical/sigma_compact_baire.md#sc-proof)、[算子空间的反塌缩测试](research/operator_space.md)；局部观测丢完整图、proper 不保纲 | 冻结自然、参数中立的完整原算子母空间 \(\mathfrak X\)，计数对象 \(F\) 或 \((F,\lambda)\)、RLEB/LT/极大单调的同域成员谓词与非退化大小不变量 \(\mathfrak I\)；在此同一空间证明或反驳总体比较。C128 只在**已经构造同一空间的紧覆盖**后测试 Baire 性。当前**没有**总体定理。来源报告的孔隙否定缺原证明，不升级为本库结果。 |
| **局部 RLEB–PPA** | [图块收敛](research/rleb_ppa.md)、[指定分支弱接口](research/canonical/named_branch_local.md)、[全对到锚的桥](research/canonical/all_pairs_verifier.md)、[窗口和闭域门](research/canonical/residual_window_bridge.md) | 对一个**指定的完整原生关系**证明同一轨道区域的全部纤维排他、输入 coverage、真实输出残差 EB、统一兼容与留域；不可由全对 RL 单独推出。一般模的点收敛另需 Dini。M1 历史原生循环方程与已核显式映射的身份桥仍缺完整方程和全部合法选择。 |
| **全局结构与有限纤维** | [剪切与同常数扩张](research/canonical/holder_extension.md)、[结构候选正文](research/holder_structure.md)、[值域及有限数据](research/range_finite_data.md) | C03/C04、C18–C20 的稿内证明仍为 `candidate`：逐项核有限维 properness/degree、固定点实现、影子锐常数、QP 与完整纤维 coverage。`e_N` 只认证候选参数处的 QP 输出；反演三项误差另需固定点残差换算为 `e_x`。固定维数影子最优因子开放。 |
| **局部值域** | [C70 样本包络/整窗余量](research/canonical/finite_sample_collar.md) 与 [C05-v2 条件拓扑证明](research/canonical/local_range_without_supercriticality.md)；[一手引文适用门](research/LITERATURE.md#lit-grn-2002) 已核 | 给一个目标原生模型逐输出认证**同一个**指定 \(T\) 的近端包含、两项整窗估计、非空紧 usc/acyclic 值、同一 collar 与上同调门。有限样本不认证这些全称条件。PDF 原稿 C05-v1 的 \(q\gamma>1\) 候选身份不被只需 \(q>0\) 的 v2 悄悄替换。 |
| **锥、Markov 与随机近端旁支** | [锥/Markov 对象与条件](research/cone_markov.md)、[有限状态顶点证书](research/topics/random_markov/finite_state_certificate.md)、[C126/C127 矩与回耦](research/topics/random_markov/moment_recoupling.md)、[随机近端](research/canonical/random_proximal.md) | 锥 MSCQ 接 PPA 真残差需同一零集及锥残差桥；随机条件残差、同步 \(\Psi\) 与真实 law-step 各有不同目标。原生回耦的**同一输入最优近极小对**、目标边缘和损失界尚未对一般多值算法认证。外部先行性及未重写的旧推论独立待核。 |
| **来源语义覆盖** | [逐单元去向](research/audit/UNIT_DISPOSITIONS.tsv) 当前有 108 行（102 rewritten、3 superseded、3 deferred），[来源位置/字节组索引](research/audit/SEMANTIC_INVENTORY_PLAN.md) 保持溯源 | 251 个物理文件与 178 个 ZIP 成员只是 429 个出现位置、346 个字节组；尚未穷尽数学及证据单元的分母。三个内容组做了不同深度的逐段试点；其余内容须按 P1–P5 枚举并裁决。不能从 108/251、108/346 或图节点数报告清洗完成率。 |

## 条件链的使用顺序

1. **确定对象与残差。** 写完整图还是图块、\(S\subset F^{-1}(0)\) 还是完整零集、输入对距还是输入球、\(r_F\) 还是选中步或概率耦合。跨主题字母按 [符号契约](research/NOTATION_CONTRACT.md) 重新绑定。
2. **在同一窗口合取前提。** 例如从全对 RL 到 PPA 必须另证 coverage、零锚、实际输出真 EB、兼容与留域；从 Markov 收缩到原同步 \(\Psi\) 的线性 EB，须另证近极小 OT 对上的回耦损失。[条件契约](research/LOGIC_CONTRACTS.md) 不容许把不同对象的证书拼接。
3. **按证据层调用。** `derived-checked` 只在正文注明的推导和审查范围可继续使用；`candidate` 与 `source-report` 是待审入口，不是规范层已闭证明。单个 fatal objection 阻止升级。[失败路线](FAILED_ROUTES.md) 给明确反例和重启门。

## 下一轮具体行动

1. 先对总体比较写一页 \((\mathfrak X,\mathfrak I,\mathcal R,\mathcal L,\mathcal M)\) 规格；用 [operator_space](research/operator_space.md) 中局部观测、远端自由度与共同塌缩机制立即攻击。若量尺把目标类一同判小，改量尺或表示，不追加孤立成员例。
2. 为一份目标原生值域模型逐输出验证 C05-v2 的整窗 \(T\)，或给其条件不可同时满足的明确障碍。C70 与文献定理适用门已有规范记录，不重复把样本误当全称证据。
3. 对 C03/C04、C18–C20 的一个承重稿内步骤作真正独立证明或反例攻击，优先选择有限维 degree/fixed-set 或 QP/反演链；所得结果改变 Claim 状态时同步正文、总账与图。
4. 按 [语义分母计划](research/audit/SEMANTIC_INVENTORY_PLAN.md) 继续可验证的来源逐段裁决。每个有价值单元重写成自足正文；重复文件、来源报告、任务书和真实数学证明分开登记。缺失原证明不得补造；新数学研究不必等待覆盖任务全部结束。
5. 每次改动执行 [增长协议](RESEARCH_PROTOCOL.md) 的 Claim 版本、符号、合取图和验证门；由空白上下文只读规范层复述一条新承重链，发现需要猜原件定义时补正文或降状态。

## 完成判据

“一个新研究者可沿**受检链**安全接续”与“全部历史材料已语义验收”是两个不同判断。整个研究地基完工需：规范正文不依赖历史目录补定义或证明；各 Claim 的空间、域、量词、状态及引用版本一致；承重合取边可从正文独立重建；来源单元分母完成并逐项去向明确；若原件缺失或数学仍开放，必须有精确 `source-report`/`open` 边界，不能假称关闭。最近的空白接收范围与修补见 [接收记录](research/audit/BLIND_RECEIPT_2026-10-02.md)。
