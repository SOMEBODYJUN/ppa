# 9/14 超边逐边重判

来源 S14H 的 资产关系数据.json 含 35 条历史超边、149 个实体和 101 个资产元数据。本页记录**每条旧边在当前数学图中的去向**，避免简单丢弃或把历史 PROVED/PENDING 标签原样升级。旧边的精确来源片段仍在 JSON 的 sources 字段；当前重构的数学范围、量词和异议以对应模块为准。原历史包实际保留 100/101 文件，受限第三方 PDF 未入库。

| 旧边 | 历史数学关系 | 当前去向及重判 |
| --- | --- | --- |
| h01 | AP-RL ⇔ 耦合 Minty 图 | [D02–D03](foundations.md)、E01；代数保留，coverage 独立。 |
| h02 | RL–PPA 收敛机制 | [R01–R02](rleb_ppa.md)、E02–E03；采用 S19 精确 A1–A4 和留域量词，完整 \(J_F\) 不自动进入。 |
| h03 | 固定 \(\kappa\) 到一般比较序列 | 历史 PENDING；不当作新定理。一般模的真正可用版本是独立 [C09](../CLAIMS.md)，需 Dini。 |
| h04 | 幂型阈值与可达锐性 | [R03](rleb_ppa.md)、E25–E26；直接 \(\lambda m>L/2\) 与能量 \(\lambda m>L/\sqrt2\) 是不同证书的阈值。 |
| h05 | 标量 exact 的信息边界 | 保留为证书充分性边界；[R03](rleb_ppa.md) 不将标量条件失败解释为轨道发散。 |
| h06 | 自然类的独立认证 | 旧证明追 [S14R](SOURCES.md)；现有 [signed-Schur/接缝](rleb_ppa.md) 需要独立覆盖与真 EB，不以旧实例替代总体规模比较。 |
| h07 | 直接分块支配汇总应用 | 历史 ALREADY_COVERED；保留价值判断，不建“新颖定理”边。 |
| h08 | Minty collision 排除范围 | [R04](rleb_ppa.md)、E28；逐支正则不能替代跨支定向。 |
| h09 | 冻结 CRSC 秩夹逼 | [CM-RANK](cone_markov.md)、E36；保留 nice、闭像及完整邻域秩条件。 |
| h10 | 锥 CRSC→MSCQ | [CM-FACE/NORMAL/MSCQ](cone_markov.md)、E37；参考面 amenability 不能删除。 |
| h11 | amenable 的普遍量词 | [锥普遍边界](cone_markov.md)、E38；只对固定 proper nice 锥的每个顶点冻结系统。 |
| h12 | nice 不能代替 amenability | [非 amenable 反例](cone_markov.md)、E39；旧文献锥不冒充新构造。 |
| h13 | 锥 EB 接入 RL | [跨线桥](cone_markov.md)、E21；需锥残差到 \(r_F\) 的同零集比较，仍是条件边。 |
| h14 | 核、表示与原残差 | [同步 \(\Psi\)](cone_markov.md)、C14；同核不同随机表示可以改变该证书。 |
| h15 | 有限 OT→exact-zero⇔EB | [CM-FINITE](cone_markov.md)、C15/E23；固定有限数据和 tight-edge 顶点，不推广无限状态。 |
| h16 | lazy cycle：EB 与速率分离 | 具体参数和原残差已在 [C71 四状态卡](topics/random_markov/lazy_cycle_ot.md#lc-object) 自足给出；EB 不推动力的直接例见 [C15 翻转](topics/random_markov/finite_state_certificate.md#fs-boundary)。旧 S14M 仅作溯源。 |
| h17 | 有限/无限状态边界 | [CM-NO-POWER](cone_markov.md)、E41；无限状态 exact-zero 与快率仍无正幂 EB。 |
| h18 | 点态高阶到矩匹配 | [CM-MOMENT](cone_markov.md)、E44；有限支撑小质量测试给 \(pq\le r\)，非任意残差普遍 no-go。 |
| h19 | 合法随机 RL 匹配 | [跨线桥](cone_markov.md)；共同耦合、几何实现和真实目标仍是开放接口。 |
| h20 | 相关性条件修复改变接口 | [条件残差](cone_markov.md)、E24/E42–E43；不能偷换原同步 \(\Psi\)。 |
| h21 | 正类旧机制覆盖 | 历史 ALREADY_COVERED，新颖性/价值单独判断；不用作一般数学蕴含。 |
| h22 | 多值图 ≠ 连续选择核 | [C62-v2/C63 规范卡](topics/random_markov/proximal_selection_seam.md#ps-absorption) 的吸收选择/非不变极限障碍；不声称每个多值图可表示为合法连续随机核。 |
| h23 | Markov 同核表示边界 | [C88 同核两表示](topics/random_markov/lazy_cycle_representations.md#lcr-object) 已固定模型证明证书差异；一般原生表示桥及其它来源断言仍开放。 |
| h24 | 广义次正则三线共用接口 | 共用“距离–残差”语言，原残差不同；[foundations](foundations.md)、E21/E44 明示附加桥。 |
| h25 | 多值/非孤立共享但不同 | [D01–D04](foundations.md) 中的域和真实残差界；不是三个领域的共同母定理。 |
| h26 | 原生信息→证书→收敛/障碍 | 仅研究组织框架；现 [HYPERGRAPH](HYPERGRAPH.md) 将具体合取边逐条展开。 |
| h27 | 优先权/文献/版本硬门 | 继续作为 [RESEARCH_STATE](../RESEARCH_STATE.md) 的 proof obligations，不是数学证明。 |
| h28 | 后续基线覆盖历史验收 | 版本优先级已按 S18/S19/S20/S21/S23/S25 重判；较晚日期不补缺失证明。 |
| h29 | 原始来源到限定主张 | [SOURCES](SOURCES.md) 管理证据路线；不能把来源关系当蕴含。 |
| h30 | RL 主定理证据包 | [RLEB–PPA](rleb_ppa.md) S18/S19 源和限定内部审计；未全篇 referee。 |
| h31 | 锥 MSCQ 证据包 | [锥模块](cone_markov.md) S14C/CM-C；优先权与退化常数门保留。 |
| h32 | 有限状态分类证据包 | [Markov 模块](cone_markov.md) S14M/CM-M；有限顶点机制保留。 |
| h33 | 无限状态障碍证据包 | [Markov 反例](cone_markov.md)；不能以有限状态结论覆盖。 |
| h34 | 随机选择障碍证据包 | [C62-v2/C63](topics/random_markov/proximal_selection_seam.md#ps-example) 已自足重写非乘积吸收选择和非不变极限；只作指定机制的反例。 |
| h35 | 同核表示前沿证据包 | [C88 固定四状态分离](topics/random_markov/lazy_cycle_representations.md#lcr-sharp) 已完成；一般原生表示和证书桥仍需独立 proof obligation。 |

9/18–9/25 的 RLEB 一般模、完整对数接缝、局部回缩、修补后的解选择、结构影子、纤维分类、[锐值域与有限 QP](range_finite_data.md)及 PDF-only 局部值域不是 h01–h35 的“同名重排”；它们在当前 [超边图](HYPERGRAPH.md) 有新的节点与边。历史失败的路线和缺失原证明见 [FAILED_ROUTES.md](../FAILED_ROUTES.md)。
