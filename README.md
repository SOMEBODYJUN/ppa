# PPA 研究地图：数学节点与真实超边

导航单位是**定义、精确命题、证明义务、反例与合取关系**。[可筛选的 HTML 超边图](research/map.html) 和 [Markdown 关系表](research/HYPERGRAPH.md) 展示 81 个数学节点、53 条关系；[graph.json](research/graph.json) 是可校验的结构数据。原稿保存在 history/sources/ 作证据，不充当导航树，也不因标题含“终审”自动成为定理。HTML 下载后可在浏览器打开；GitHub 文件页未必执行 HTML。

> 当前判断：局部 RLEB–PPA 的收敛机制有可读证明链；总体 RLEB–LT–极大单调的自然母空间规模比较仍开放。Hölder–RL 全局影子和有限维纤维分类有候选稿证明及局部独立重算，外部定理与先行性门未关闭。9/25 局部值域证书另有独立整窗拓扑假设。

## Research Goal

1. **收敛机制**：在同一图块、真实全纤维残差、coverage 与留域预算下，确定非线性全对 RL 和误差界如何控制 PPA，区分距离收缩与点收敛。
2. **规模比较**：找不以认证参数定义的自然完整原算子空间及有鉴别力的大小量尺，比较 RLEB、Luke–Tam 公共 all-pairs 类与极大单调类。严格多一个例子或特殊层余稠不回答总体规模。
3. **结构与纤维**：全图全尺度 Hölder–RL 下研究一个同时近似正反纤维的强单调影子、固定参数极大图的完整纤维与最优常数。
4. **独立旁支**：冻结面 CRSC→MSCQ、Markov/运输残差与解选择稳定性分别保留自己的对象和量词；跨线连接须证明桥。

## Mathematical Objects 与 Definition Map

定义域、量词、约定在 [foundations.md](research/foundations.md)。核心坐标为

\[
J_{\lambda F}(p)=\{u:p-u\in\lambda F(u)\},\quad
r_F(u)=\inf_{v\in F(u)}\|v\|,\quad
p=u+\lambda v,\quad C(p)=u-\lambda v .
\]

对同一图块任意**两**图点、同一步长和输入对尺度，全对 RL 写成
\(\|\Delta u-\lambda\Delta v\|\le L\|\Delta u+\lambda\Delta v\|^\gamma\)。
它给部分定义的 Cayley 映射与图块单值 \(J_{\mathcal G}\)，**不提供输入 coverage**。
局部 RLEB 另用实际输出上的 \(d(u,S)\le\psi(r_F(u))\)、兼容及初值长度预算。
全局结构稿取实 Hilbert 空间、非空完整图、\(L>0,0<\gamma<1\)、全部尺度；其中 graph-maximal 固定 \((\lambda,L,\gamma)\)，不是极大单调。有限维完整纤维分类再增加 \(H=\mathbb R^n\)。

| 前件 | 后件 | 需要额外检查 |
| --- | --- | --- |
| 全对 RL | Cayley 图坐标、图块内同输入唯一 | 完整或局部输入 coverage 独立 |
| 局部图块 \(J_{\mathcal G}\) | 完整 \(J_{\lambda F}\) | 共同轨道输入域的全纤维一致性 |
| 局部或全时间 \(T\) 观测 | 原关系 \(F\) | 必须保存完整输入与完整输出纤维 |
| 锥 MSCQ | PPA 的真残差 EB | 同一零集及锥残差到 \(r_F\) 的桥 |
| 条件 Markov 残差 | 同步 OT 残差 \(\Psi\) | 同一耦合、目标和回耦损失界 |

## Claim Map 与 Dependency Graph

完整命题身份、版本、异议在 [CLAIMS.md](CLAIMS.md)。下面是**数学路线而非文件链**；每行的合取和适用域见 [超边表](research/HYPERGRAPH.md)。

| 路线 | 承重节点及联合前件 | 当前状态 |
| --- | --- | --- |
| 局部 RLEB | 图块全对 RL + coverage + 最近零点图 + 真实输出 EB → 一步估计；再加兼容 + 留域 → 有限长度 | R01/R02 稿内证明，完整 \(J_F\) 需另证同一性 |
| 非幂次边界 | 一般模 + Dini + 上述全部局部条件 → 点收敛；对数完整接缝 \(a\le1\) 有距离收缩但点发散 | 9/19 稿内构造与本轮局部重算 |
| 全局结构 | 全图 RL → Cayley；二次 excess + 正交提升 + Banach → 单一正反影子 | C03 候选 |
| 完整纤维 | 有限维 properness/degree + 直径界 → 必要性；紧集 fixed-set + Cayley → 充分性 | C04 候选，两方向分列 |
| 值域与有限数据 | 最大根定位 + 有限维全纤维非空 → 锐值域球；兼容样本 + 同一 QP → 全局代理；再加参数覆盖 → 未观测图点误差 | C18–C20 稿内证明；有限查询不能全空间认证 C21 |
| 拓扑限制 | 局部 all-pairs + EB + Dini + coverage + 不变开域 → 连续极限回缩 | 不由任意紧零集实现自动得到 |
| 有限数据值域 | 样本包络 + 整窗 \(T\) 的 usc/acyclic + collar + 上同调 + Lefschetz → 原关系局部值域球 | C05 PDF-only，外部定理门未闭 |
| 大小比较 | LT 公共接口 → RLEB 能量证书；紧 T-only \(\Phi\) proper；还缺完整对象与保纲桥 | 总体规模命题开放 |
| 锥与 Markov | 冻结秩→面稳定→MSCQ；同步 OT exact-zero→一般 gauge，有限状态顶点→线性 EB | 两条独立链，跨线桥待证 |

9/14 历史包本身已有 149 个实体、35 条超边；本图以它为搜索种子，读入 9/18–9/25 版本后重新判断，没有把历史边直接升级为当前真理。

## Research Frontier

**首要开放点**是完整、参数中立、非退化的算子母空间与规模量尺。9/20 的 \(\Phi=(\text{实际尾},\text{实际反射模})\) 在固定紧 T-only 图卡 proper，但 proper/quotient 不推出 category-preserving，局部观测丢失完整 \(F\) 的域外信息。9/21 总账报告普通 Baire、轨道理想与旧动力度量孔隙性同时把目标类判小；原证明恢复情况须逐项核对。详见 [operator_space.md](research/operator_space.md)。

结构稿的 proof obligations：Hilbert Hölder 扩张、统一影子常数下界、有限维 degree、fixed-set 构造、固定窗口 completion 与有限样本覆盖的适用条件；有限总查询的全空间障碍要保持确定性、无界域量词。[值域与有限数据](research/range_finite_data.md)。9/25 另需逐条核引用的 rational morphism Lefschetz 定理，有限样本只认证包络，不认证整窗 \(T\) 的拓扑性质。9/19 随机推论用到**给定度量完备**，若“Polish”仅按拓扑意义，已有显式反例；见 [holder_structure.md](research/holder_structure.md) H06。

## Known Results、Refuted / Failed、Open Problems

- 可直接复核的代数：Cayley 双向坐标、固定步长全域完整 resolvent 的原图反演、同图块内同输入唯一。
- 有证明文本和限定内部审计的研究结果：局部 RLEB、固定紧源 \(\Phi\)、解选择修订版、锥与 Markov 条件命题。候选稿与外部审稿、文献新颖性是独立层。
- 已证伪的扩大陈述：局部 \(J_{\mathcal G}\) 自动等于完整 \(J_F\)；Polish 拓扑性质自动给指定度量完备；proper 即保纲。精确反例和可回收部分见 [FAILED_ROUTES.md](FAILED_ROUTES.md)。
- 尚未解：总体规模比较；9/21 N10 原孔隙否定证明可追溯性；9/25 外部拓扑定理应用；各固定维数影子最优常数；同对象同量词的全球先行性。

## Next Actions

1. 冻结总体比较的**计数对象、三类认证量词和大小不变量**的一页规格，先用 N05/N08/N09/N10 及远端自由度反例攻击，再尝试总体定理。
2. 逐项追索 9/21 的 I-097–099、I-102；可恢复者重构证明，缺者保持报告状态。已恢复的 I-001/I-002/I-003–005/I-059/I-075 也分别核版本和证据身份。
3. 为 9/25 §8 配对可编译源，核 [6, Theorem 6.2] 的范畴与 Čech 同调条件；在正文保持“指定 \(T\)”量词。
4. 修订 9/19 随机推论的指定度量完备性，保留反例作为缘由；分别推进结构、锥、Markov 的外部先行性核验。

## File Map

| 仓库根相对完整路径 | 数学资产、目的、何时读取或更新 |
| --- | --- |
| [research/HYPERGRAPH.md](research/HYPERGRAPH.md)、[research/graph.json](research/graph.json)、[research/map.html](research/map.html) | 人读合取关系、机读节点边和 HTML 关系图；claim 版本或边变化时改 JSON 并运行 [research/build_graph.py](research/build_graph.py)。 |
| [research/foundations.md](research/foundations.md) | D01–D04 的关系、剪切、真残差、局部/完整区别；遇到定义混用先读。 |
| [research/rleb_ppa.md](research/rleb_ppa.md) | R01–R04：一步估计、两种证书、局部收敛、signed-Schur 验证和接缝；研究 PPA 假设时读。 |
| [research/holder_structure.md](research/holder_structure.md) | H01–H07：影子、纤维分类、Dini、回缩、随机完备性反例、9/25 值域候选；审结构或局部拓扑时读。 |
| [research/range_finite_data.md](research/range_finite_data.md) | W01/Q01–Q04/B01：9/23 的锐值域球、固定窗口、同一有限 QP、参数覆盖、三项误差、有限查询障碍与 deadband；要从结构定理走向可计算证书时读。 |
| [research/solution_selection.md](research/solution_selection.md) | S01–S03：统一尾到极限模、局部/完整修补、锐性模型；主张初值稳定时读。 |
| [research/operator_space.md](research/operator_space.md) | LT 嵌入、完整图信息、\(\Phi\) proper、大小量尺塌缩和未解桥；总体比较工作入口。 |
| [research/cone_markov.md](research/cone_markov.md) | 锥秩–面–MSCQ 和 Markov 同步/条件残差链、反例与跨线桥；研究旁支时读。 |
| [research/SOURCES.md](research/SOURCES.md)、[research/HISTORICAL_EDGE_CROSSWALK.md](research/HISTORICAL_EDGE_CROSSWALK.md) | S14–S25/SS 的**完整原路径**、ZIP 成员与恢复身份；9/14 旧图 h01–h35 的逐边去向。由规范命题反查或确认旧关系是否丢失时读。 |
| [CLAIMS.md](CLAIMS.md)、[RESEARCH_STATE.md](RESEARCH_STATE.md)、[FAILED_ROUTES.md](FAILED_ROUTES.md) | 精确身份、当前阻塞、已失败机制；每次进展后同步维护。 |
| [INGEST_MANIFEST.tsv](INGEST_MANIFEST.tsv)、[BATCH_README.md](BATCH_README.md) | 初始校验与旧批次盘点；用于核原件，不再作为数学地图。原件保留在 [history/sources/](history/sources/)，Git 历史可追初始导入。 |

阅读顺序：本页和超边图 → 依节点进数学模块 → SOURCES 的原稿标签/页码 → CLAIMS 的现存 objection。图中路线是搜索种子，不是方法白名单。
