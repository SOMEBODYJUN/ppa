# PPA 研究地图：数学节点与真实超边

导航单位是**定义、精确命题、证明义务、反例与合取关系**。[可筛选的 HTML 超边图](research/map.html) 和 [Markdown 关系表](research/HYPERGRAPH.md) 展示 126 个数学节点、80 条关系；[graph.json](research/graph.json) 是可校验的结构数据。原稿保存在 [history/sources/](history/README.md) 作证据，不充当导航树，也不因标题含“终审”自动成为定理。HTML 下载后可在浏览器打开；GitHub 文件页未必执行 HTML。

**这是正在增长的规范研究库。** [研究增长协议](RESEARCH_PROTOCOL.md) 规定新定义、Claim、证明、反例、代码和文献事实的落点与验收门；[来源重构覆盖审计](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md) 逐项记录仍未裁决的旧材料。历史材料的清点不等于数学验收，未来工作也无需先清空历史待办才可进入规范正文。

> 当前判断：局部 RLEB–PPA 的收敛机制有可读证明链；总体 RLEB–LT–极大单调的自然母空间规模比较仍开放。Hölder–RL 全局影子和有限维纤维分类有候选稿证明及局部独立重算，外部定理与先行性门未关闭。9/25 局部值域证书另有独立整窗拓扑假设。

## Research Goal

1. **收敛机制**：在同一图块、真实全纤维残差、coverage 与留域预算下，确定非线性全对 RL 和误差界如何控制 PPA，区分距离收缩与点收敛。
2. **规模比较**：找不以认证参数定义的自然完整原算子空间及有鉴别力的大小量尺，比较 RLEB、Luke–Tam 公共 all-pairs 类与极大单调类。严格多一个例子或特殊层余稠不回答总体规模。
3. **结构与纤维**：全图全尺度 Hölder–RL 下研究一个同时近似正反纤维的强单调影子、固定参数极大图的完整纤维与最优常数。
4. **独立旁支**：冻结面 CRSC→MSCQ、Markov/运输残差与解选择稳定性分别保留自己的对象和量词；跨线连接须证明桥。
5. **随机近端的条件律残差**：在守恒坐标下分类混合不变律，核验真实 law-step 的误差界，同时攻击把逐分支或物理步长当作同一残差的偷换。

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
更完整的[参数与正则性字典](research/canonical/parameter_dictionary.md)把全对/锚定、图块/全图、输入尺度、同图换步与改变关系分开；\(\gamma=1\) 的 tied 曲线包括 \(L=0\) 端点，真残差 EB 与选中步界只有一个无条件方向。
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

完整命题身份、版本、异议在 [CLAIMS.md](CLAIMS.md)。下面是**数学路线而非文件链**；每行的合取和适用域见 [超边表](research/HYPERGRAPH.md)，承重边的量词逐项见 [条件逻辑契约](research/LOGIC_CONTRACTS.md)。

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
| 不一致随机近端 | 有限维二次近端 + 正权重 + 固定守恒边缘 + 独立新噪声 → 活跃谱隙 → 条件 \(W_2\) 收缩 → 真实 law-step EB；逐分支残差零集另由共同定点决定 | C22/C23 本轮独立推导；与普通 \(W_2\)、物理步长、Markov 同步缺陷的替换不成立 |
| 规范例库 | 纯旋转：完整 J 严格收缩而 F 无强单调；正紧对角：严格单调+cocoercive 而无任意趋零 gauge EB；三次映射：固定目标/两变量/算法残差的精确模不同 | C24–C26 的三个对象及证明；历史 GX 编号是观察别名，不代表 77 个独立算子 |
| 参数与逻辑转换 | 同图换步：旧 Cayley → \(Q=\alpha I+\beta C\)，新 Cayley 良定 iff \(Q\) 单射；线性 RL → tied 参数曲线；有界输入域高指数→低指数；真残差 EB → 选中值界 | C27–C30 分别限定相同对象、配对与尺度，折叠和分支反例阻断逆向推理 |
| 合法多步路径 | 实际前缀 coverage ∧ 统一终点收缩 ∧ 可求和块内位移 ∧ 初值留域 → 每条轨道有限长收敛；块 RL/输出 EB 只生产终点估计 | C31–C33 已重新证明；无限词逐词指数 >1 不给统一半径，周期相位极限须单独处理 |
| M1 显式动力 | 同一状态的活动关系 \(s=a-3b\) → 球内两步捕获及锐一步距离因子 \(3/\sqrt {10}\) | C38/C39 对给定单值 T 重算；原生多值方程到 T 的桥仍未核，不能声称一步定理严格失败 |
| 复合次正则 | 原生凸外层 EB ∧ 满行秩定量修复 ∧ 链式残差下界 → 复合真实 EB；再加全部乘子界、步长门、gauge 兼容和留域 → 局部近端有限长 | C34–C37 已重写；尖点外层特例在 C40，秩亏原生推广开放；历史 C11 不等于回缩 C11 |
| 复合模型的独立边界 | 曲面尖点外层 + 真残差间隙 + 局部近端步长门 → 一步识别；光滑驻点极大序列 → 无弱分离时二阶目标 EB 失败 | C40/C41 本轮重算；前者图真多值而局部输出唯一，后者只攻击到 \(\Theta_2\) 的扩大陈述 |

9/14 历史包本身已有 149 个实体、35 条超边；本图以它为搜索种子，读入 9/18–9/25 版本后重新判断，没有把历史边直接升级为当前真理。

## Research Frontier

**首要开放点**是完整、参数中立、非退化的算子母空间与规模量尺。9/20 的 \(\Phi=(\text{实际尾},\text{实际反射模})\) 在固定紧 T-only 图卡 proper，但 proper/quotient 不推出 category-preserving，局部观测丢失完整 \(F\) 的域外信息。9/21 总账报告普通 Baire、轨道理想与旧动力度量孔隙性同时把目标类判小；原证明恢复情况须逐项核对。详见 [operator_space.md](research/operator_space.md)。

结构稿的 proof obligations：Hilbert Hölder 扩张、统一影子常数下界、有限维 degree、fixed-set 构造、固定窗口 completion 与有限样本覆盖的适用条件；有限总查询的全空间障碍要保持确定性、无界域量词。[值域与有限数据](research/range_finite_data.md)。9/25 另需逐条核引用的 rational morphism Lefschetz 定理，有限样本只认证包络，不认证整窗 \(T\) 的拓扑性质。9/19 随机推论用到**给定度量完备**，若“Polish”仅按拓扑意义，已有显式反例；见 [holder_structure.md](research/holder_structure.md) H06。

## Known Results、Refuted / Failed、Open Problems

- 可直接复核的代数：Cayley 双向坐标、固定步长全域完整 resolvent 的原图反演、同图块内同输入唯一。
- 有证明文本和限定内部审计的研究结果：局部 RLEB、固定紧源 \(\Phi\)、解选择修订版、锥与 Markov 条件命题。候选稿与外部审稿、文献新颖性是独立层。
- 已证伪的扩大陈述：局部 \(J_{\mathcal G}\) 自动等于完整 \(J_F\)；Polish 拓扑性质自动给指定度量完备；proper 即保纲。精确反例和可回收部分见 [FAILED_ROUTES.md](FAILED_ROUTES.md)。
- 尚未解：总体规模比较；9/21 N10 原孔隙否定证明可追溯性；9/25 外部拓扑定理应用；各固定维数影子最优常数；同对象同量词的全球先行性。
- 新的 C22/C23 以完整证明写入[随机近端模块](research/canonical/random_proximal.md)：条件 law-step 与逐分支推前残差具有不同零集；标量例使 EB 的统一常数锐。历史验证器的有限运行记录与证明分开保存。
- [规范例库](research/canonical/example_atlas.md) 已重写 GX-004/009/021 所指的三个对象，分别证明收缩逆推的边界、无限维无 gauge EB、三种局部模的精确常数；其余 GX 性质仍按逐单元义务处理。
- [参数字典](research/canonical/parameter_dictionary.md) 的同图换步公式、\(\gamma=1\) tied 端点、有限尺度换指数、真残差方向及 MR/MSR 量词已分别给证明或反例。它是可调用的条件记录，不替代外部定理的先行性核验。

## Next Actions

1. 冻结总体比较的**计数对象、三类认证量词和大小不变量**的一页规格，先用 N05/N08/N09/N10 及远端自由度反例攻击，再尝试总体定理。
2. 逐项追索 9/21 的 I-097–099、I-102；可恢复者重构证明，缺者保持报告状态。已恢复的 I-001/I-002/I-003–005/I-059/I-075 也分别核版本和证据身份。
3. 为 9/25 §8 配对可编译源，核 [6, Theorem 6.2] 的范畴与 Čech 同调条件；在正文保持“指定 \(T\)”量词。
4. 修订 9/19 随机推论的指定度量完备性，保留反例作为缘由；分别推进结构、锥、Markov 的外部先行性核验。
5. 从[逐单元去向](research/audit/UNIT_DISPOSITIONS.tsv)继续核 M1 **原生多值图到已验显式 T 的桥**；复合稿的真多值尖点与振荡弱分离例已有精确重写，下一步核秩亏原生桥和未审外部文献。新证明按[增长协议](RESEARCH_PROTOCOL.md)进入主题目录，再更新 Claim、图与前沿。

## File Map

| 仓库根相对完整路径 | 数学资产、目的、何时读取或更新 |
| --- | --- |
| [research/HYPERGRAPH.md](research/HYPERGRAPH.md)、[research/graph.json](research/graph.json)、[research/map.html](research/map.html) | 人读合取关系、机读节点边和 HTML 关系图；claim 版本或边变化时改 JSON 并运行 [research/build_graph.py](research/build_graph.py)。 |
| [research/LOGIC_CONTRACTS.md](research/LOGIC_CONTRACTS.md) | E02/03、E06/11/12、E17–19、E13、E54–80 的固定对象、量词、合取 side conditions 与不蕴含；使用跨稿箭头或改 Claim 版本时先核。 |
| [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md)、[research/validate_assets.py](research/validate_assets.py) | 新资产的精确身份、状态、证据与生长门槛；结构检查哈希、图目标和规范链接。新 Claim 进入前后读协议并执行校验。 |
| [research/foundations.md](research/foundations.md) | D01–D04 的关系、剪切、真残差、局部/完整区别；遇到定义混用先读。 |
| [research/rleb_ppa.md](research/rleb_ppa.md) | R01–R04：一步估计、两种证书、局部收敛、signed-Schur 验证和接缝；研究 PPA 假设时读。 |
| [research/holder_structure.md](research/holder_structure.md) | H01–H07：影子、纤维分类、Dini、回缩、随机完备性反例、9/25 值域候选；审结构或局部拓扑时读。 |
| [research/range_finite_data.md](research/range_finite_data.md) | W01/Q01–Q04/B01：9/23 的锐值域球、固定窗口、同一有限 QP、参数覆盖、三项误差、有限查询障碍与 deadband；要从结构定理走向可计算证书时读。 |
| [research/solution_selection.md](research/solution_selection.md) | S01–S03：统一尾到极限模、局部/完整修补、锐性模型；主张初值稳定时读。 |
| [research/operator_space.md](research/operator_space.md) | LT 嵌入、完整图信息、\(\Phi\) proper、大小量尺塌缩和未解桥；总体比较工作入口。 |
| [research/cone_markov.md](research/cone_markov.md) | 锥秩–面–MSCQ 和 Markov 同步/条件残差链、反例与跨线桥；研究旁支时读。 |
| [research/canonical/random_proximal.md](research/canonical/random_proximal.md) | RP-OBJECT/GAP/CONTRACTION/EB/BRANCH/SCALAR 的全证明、尖锐例和残差替换障碍；研究随机近端或条件 \(W_2\) 时读，改假设须另立版本。 |
| [research/canonical/example_atlas.md](research/canonical/example_atlas.md) | EX01 旋转、EX02 正紧对角、EX03 三次映射的完整对象卡、真残差、参数、证明及历史别名；检验某个逆推、EB 或常数边界时读，新增 GX 先区分对象与观察。 |
| [research/canonical/parameter_dictionary.md](research/canonical/parameter_dictionary.md) | PD-QUANTIFIERS/CAYLEY/TIED/STEP/SCALE/RESIDUAL/REGULARITY：同一图换步的单射门、尺度、真残差和 MR/MSR 的量词；引入或改变 RL 参数、正则性、选中步残差时先读。 |
| [research/canonical/path_atlas.md](research/canonical/path_atlas.md) | PA-DEF/WHOLE/BLOCK/POWER/CYCLES：每条合法路径的前缀延拓、块内预算、整轨道证明；无限词统一性反例及非平凡周期的独立相位结论。做多步或多值算法时先核实际分支与留域。 |
| [research/topics/path_dynamics/README.md](research/topics/path_dynamics/README.md)、[research/topics/path_dynamics/m1_capture.md](research/topics/path_dynamics/m1_capture.md) | 路径主题入口与 C38/C39 独立模型卡：完整 T、端点球、两步捕获、锐一步因子及原生多值桥缺口。新增路径对象/障碍时读入口并独立开卡；不得把此 T 的性质移给未核图。 |
| [research/canonical/composite_subregularity.md](research/canonical/composite_subregularity.md) | CS-TRANSFER/EB/PROX/MODEL：满行秩修复、链式真残差、局部近端轨道及曲面幂/非幂锐例；秩亏反例和开放乘子门。研究复合目标或调用历史 C11 时先辨身份。 |
| [research/topics/composite_regular/README.md](research/topics/composite_regular/README.md)、[research/topics/composite_regular/cusp_identification.md](research/topics/composite_regular/cusp_identification.md)、[research/topics/composite_regular/oscillating_target.md](research/topics/composite_regular/oscillating_target.md) | 复合主题可扩写入口与 C40/C41 独立证明：真多值次梯度的局部一步识别门、弱分离缺失时驻点极大序列的目标正确 EB 障碍。新增秩亏机制或目标反例时分别开卡，先核同一目标和真实残差。 |
| [research/audit/SOURCE_RECONSTRUCTION_AUDIT.md](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md)、[SOURCE_FILE_INVENTORY.tsv](research/audit/SOURCE_FILE_INVENTORY.tsv)、[ZIP_MEMBER_INVENTORY.tsv](research/audit/ZIP_MEMBER_INVENTORY.tsv)、[LEGACY_VERIFIER_RUNS.json](research/audit/LEGACY_VERIFIER_RUNS.json) | 251 个原件及 178 个包内成员的路径/哈希/语义未决字段，旧验证器环境与运行输出；逐源重写时更新 disposition 与规范锚点，不能将盘点算验收。 |
| [research/audit/UNIT_DISPOSITIONS.tsv](research/audit/UNIT_DISPOSITIONS.tsv) | 本轮 9/09 多步与复合原件的逐节去向、规范身份、精确锚点及未闭义务；只关闭列出的单元，不把整份原件标为已重写。新增历史单元时续记，原创工作直接从增长协议进入。 |
| [research/CODE_REGISTER.md](research/CODE_REGISTER.md) | 十个历史验证器 V01–V10 到当前 Claim/待重写对象的映射、执行范围和盲区；检查计算证据或重写可维护代码时读。新代码按协议进入 `research/code/<topic>/`。 |
| [research/code/README.md](research/code/README.md) | 新可复现实验的 Claim 绑定、seed、精度、运行与盲区模板；只有新程序经重新编写和验收后才进入此树。 |
| [research/SOURCES.md](research/SOURCES.md)、[research/HISTORICAL_EDGE_CROSSWALK.md](research/HISTORICAL_EDGE_CROSSWALK.md) | S14–S25/SS 的**完整原路径**、ZIP 成员与恢复身份；9/14 旧图 h01–h35 的逐边去向。由规范命题反查或确认旧关系是否丢失时读。 |
| [CLAIMS.md](CLAIMS.md)、[RESEARCH_STATE.md](RESEARCH_STATE.md)、[FAILED_ROUTES.md](FAILED_ROUTES.md) | 精确身份、当前阻塞、已失败机制；每次进展后同步维护。 |
| [INGEST_MANIFEST.tsv](INGEST_MANIFEST.tsv)、[BATCH_README.md](BATCH_README.md)、[history/README.md](history/README.md) | 初始校验、旧批次盘点与原件使用约定；用于核原件，不再作为数学地图。原件保留在 `history/sources/`，Git 历史可追初始导入。 |

阅读顺序：本页和超边图 → 依节点进数学模块 → CLAIMS 的精确版本和现存 objection → 必要时 SOURCES 的原稿标签/页码。要写新资产时先读增长协议和当前前沿；图中路线是搜索种子，不是方法白名单。
