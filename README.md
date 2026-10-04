# PPA 研究地图：数学节点与真实超边

导航单位是**定义、精确命题、证明义务、反例与合取关系**。先进入 [动态研究宇宙](visualization/cosmos/index.html)：太阳系承载 RLEB–PPA 主链，其他星域承载相邻方向；行星和卫星按视觉轨道公转，D3 双层力学处理主题星系整组漂移、碰撞与拖动，以及内部非轨道节点的排布。真实跨域超边随天体位置重绘，灰色导航线与数学关系分离。太阳系的 `E02/E03` 等航道仍是原图的**合取超边**，公转和星系形态不表示证明顺序或证据等级。[宇宙语义契约](visualization/COSMOS_SEMANTIC_CONTRACT.md) 与 [宇宙项目说明](visualization/cosmos/README.md) 记录对象对应和增长方式；[Markdown 关系表](research/HYPERGRAPH.md) 与 [graph.json](research/graph.json) 保存精确文字及机读结构，当前有 331 个数学节点、218 条关系。原件在 [history/sources/](history/README.md) 作证据，不充当导航树，也不因标题含“终审”自动成为定理。离线 HTML 内嵌关系数据；进入规范 Markdown 正文的相对链接仍需要完整仓库。GitHub 文件页未必执行 HTML。

**从零继续研究的最短路径**：先读下方 Research Goal 和 Definition Map；再读 [当前活跃问题与完成标准](RESEARCH_STATE.md#active-frontier)，沿本页 Claim Map 的一条**合取**关系进入正文，最后对照 [Claim 精确身份](CLAIMS.md) 与 [现存异议](FAILED_ROUTES.md)。要新增结果按 [增长协议](RESEARCH_PROTOCOL.md) 写入主题目录。下方 File Map 是定位表，不要求顺读 251 个历史原件。

**规范层的独立性门**：一条 `derived-checked` 结论应仅靠所链接的规范定义、正文证明及明确导入的一手定理重建；历史路径只说明它从何而来，不补缺失的假设。仍为 `source-report` 或 `candidate` 的命题不能因 README 有箭头便当作已闭定理。[当前状态](RESEARCH_STATE.md) 只保留活跃义务，旧轮次的时间流水不充当研究前沿。

**这是正在增长的规范研究库。** [研究增长协议](RESEARCH_PROTOCOL.md) 规定新定义、Claim、证明、反例、代码和文献事实的落点；[全库协调验收门](RESEARCH_PROTOCOL.md#global-coordination-gate) 逐项核符号类型、量词、证据与独立性；[来源重构覆盖审计](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md) 逐项记录仍未裁决的旧材料。[全库语义分母计划](research/audit/SEMANTIC_INVENTORY_PLAN.md) 划定来源逐段枚举与数学清洗的两个完成门；[本轮空白接收记录](research/audit/BLIND_RECEIPT_2026-10-03.md) 保存本轮受检路径、发现的错误及复读范围。历史材料的清点不等于数学验收，未来工作也无需先清空历史待办才可进入规范正文。

> 当前判断：局部 RLEB–PPA 的收敛机制有可读证明链；总体 RLEB–LT–极大单调的自然母空间规模比较仍开放。Hölder–RL 全局影子和有限维纤维分类有候选稿证明及局部独立重算，部分外部定理与先行性门未关闭。9/25 局部值域证书的 Lefschetz 引文适用门已核，但仍有独立整窗拓扑假设和候选证明待审。

## Research Goal

1. **收敛机制**：在同一图块、真实全纤维残差、coverage 与留域预算下，确定非线性全对 RL 和误差界如何控制 PPA，区分距离收缩与点收敛。
2. **规模比较**：找不以认证参数定义的自然完整原算子空间及有鉴别力的大小量尺，比较 RLEB、Luke–Tam 公共 all-pairs 类与极大单调类。严格多一个例子或特殊层余稠不回答总体规模。
3. **结构与纤维**：全图全尺度 Hölder–RL 下研究一个同时近似正反纤维的强单调影子、固定参数极大图的完整纤维与最优常数。
4. **独立旁支**：冻结面 CRSC→MSCQ、Markov/运输残差与解选择稳定性分别保留自己的对象和量词；跨线连接须证明桥。
5. **随机近端的条件律残差**：在守恒坐标下分类混合不变律，核验真实 law-step 的误差界，同时攻击把逐分支或物理步长当作同一残差的偷换。

## Mathematical Objects 与 Definition Map

定义域、量词、约定在 [foundations.md](research/foundations.md)；跨主题复用的字母、残差类型和统一 \(\mathrm{RL}(\lambda,\gamma,L;R)\) 参数顺序见 [符号与适用域契约](research/NOTATION_CONTRACT.md)。核心坐标为

\[
J_{\lambda F}(p)=\{u:p-u\in\lambda F(u)\},\quad
r_F(u)=\inf_{v\in F(u)}\|v\|,\quad
p=u+\lambda v,\quad C(p)=u-\lambda v .
\]

对同一图块任意**两**图点、同一步长和输入对尺度，全对 RL 写成
\(\|\Delta u-\lambda\Delta v\|\le L\|\Delta u+\lambda\Delta v\|^\gamma\)。
它给部分定义的 Cayley 映射与图块单值 \(J_{\mathcal G}\)，**不提供输入 coverage**。
更完整的[参数与正则性字典](research/canonical/parameter_dictionary.md)把全对/锚定、图块/全图、输入尺度、同图换步与改变关系分开；\(\gamma=1\) 的 tied 曲线包括 \(L=0\) 端点。[非 tied 二参数图](research/canonical/non_tied_cayley.md#nt-object) 另保留交叉项及 \(A>0,\Delta\ge0\) 的门，不能用 tied 曲线代替。真残差 EB 与选中步界只有一个无条件方向。
局部 RLEB 另用实际输出上的 \(d(u,S)\le\psi(r_F(u))\)、兼容及初值长度预算。
全局结构稿取实 Hilbert 空间、非空完整图、\(L>0,0<\gamma<1\)、全部尺度；其中 graph-maximal 固定 \((\lambda,L,\gamma)\)，不是极大单调。有限维完整纤维分类再增加 \(H=\mathbb R^n\)。

| 前件 | 后件 | 需要额外检查 |
| --- | --- | --- |
| 全对 RL | Cayley 图坐标、图块内同输入唯一 | 完整或局部输入 coverage 独立 |
| 近对角线全对模 + 闭图 | Minty 自然域闭 | 还需该域在整个空间稠密才得满输入覆盖；完备环境与同一图块 |
| 局部图块 \(J_{\mathcal G}\) | 完整 \(J_{\lambda F}\) | 共同轨道输入域的全纤维一致性 |
| 局部或全时间 \(T\) 观测 | 原关系 \(F\) | 必须保存完整输入与完整输出纤维 |
| 锥 MSCQ | PPA 的真残差 EB | 同一零集及锥残差到 \(r_F\) 的桥 |
| 条件 Markov 残差 | 同步 OT 残差 \(\Psi\) | 同一耦合、目标和回耦损失界 |

## Claim Map 与 Dependency Graph

完整命题身份、版本、异议在 [CLAIMS.md](CLAIMS.md)。下面是**数学路线而非文件链**；每行的合取和适用域见 [超边表](research/HYPERGRAPH.md)，承重边的量词逐项见 [条件逻辑契约](research/LOGIC_CONTRACTS.md)。

| 路线 | 承重节点及联合前件 | 当前状态 |
| --- | --- | --- |
| 超线性法向选择 | 完整二支图 C141 + 输出 collar 的全对 γ 模 + 真 EB + 固定小 R 兼容 → 局部严格证书；同图超几何共同尾 + SS-TRANSFER → α 指数上界；固定初值配对的首次切换与 overshoot/饱和尾 → 匹配下界 | [C141 规范正文](research/canonical/selection_superlinear_family.md#sf-object) 为 `candidate`，待空白接收；ν=2、γ=1/2、A=B=1 是 C115/C116 同图特例，ν 与 C139 的 q 不互换 |
| 局部 RLEB | 图块全对 RL + coverage + 最近零点图 + 真实输出 EB → 一步估计；再加兼容 + 留域 → 有限长度；固定零点邻域的严格共同预算 + SS-TRANSFER → 同球共同尾与两点极限模 | [C02-v2 单值图块证明](research/rleb_ppa.md#r02-proof) 已独立重构，原 C02 多选择范围仍候选；[C136](research/canonical/solution_selection_rates.md#ss-rleb-ball) 的完整转移可用整个共同轨道窗的纤维等式作为充分门，也可只核全部实际可达输入，不能只核初值球 |
| 指定分支弱接口 | 整球 named coverage + 全家族近似零点锚 + 实际输出真 EB + 小尺度兼容 + 初值留域 → Hilbert 有限长度；零距离锚条件还给局部闭零集 | C53/C54 独立重算；C55 证明此接口不蕴含同指数全对 RL，不可回填 R02 的全对输入 |
| 全对图块到指定锚 | 同图块全对 RL + 指定输入 coverage + 图块零锚对完整零集保距离 → named B/A；实际输出 EB、兼容与留域另接 C53 | C56 条件桥；C57 完整关系说明前两项不能省去零锚保距离，完整排他也独立 |
| 闭图与自然域 | 近对角线全对消失模 + Hilbert 完备 → 闭图 iff Minty 自然域闭；**同一图块闭图** + 自然域在整个空间稠密 → 满覆盖 | C58 独立推导；仅稠密的非闭图仍可为真子域，图块外完整纤维另证 |
| 残差窗口的量词 | 完整真残差窗口 EB + 非减 gauge 在阈值 \(\delta\) 处为正 → 缩邻域后的可评价残差 EB | C59 充分门；平坦 gauge 与闭图仍可窗口真、邻域假，定义域外须另给 gauge |
| 非幂次边界 | 一般模 + Dini + 上述全部局部条件 → 点收敛；对数完整接缝 \(a\le1\) 有距离收缩但点发散 | 9/19 稿内构造与本轮局部重算 |
| 全局结构 | 全图 RL → Cayley；Hilbert 雪花 + 同常数 Lipschitz 扩张 → 固定参数 graph-maximal 完成；二次 excess + 正交提升 + Banach → 单一正反影子 | 扩张 [HE-EXTENSION](research/canonical/holder_extension.md#he-extension) 的量词和一手引文已核；C03 仍是独立候选 |
| 完整纤维 | 有限维 properness/degree + 直径界 → 必要性；紧集 fixed-set + Cayley → 充分性 | C04 候选，两方向分列 |
| 值域与有限数据 | 最大根定位 + 有限维全纤维非空 → 锐值域球；兼容样本 + 同一 QP → 全局代理；再加**同图同尺度** Cayley 参数覆盖、观测噪声界和已认证的反演求值误差 \(e_x\) → 未观测图点三项界 | C18/C19 与 [C20-v2](CLAIMS.md#c20-v2) 保留稿内证明状态；局部 RL 还须逐对在测试尺度内，完整纤维须全体在认证图中。[F36](FAILED_ROUTES.md#f36) 反驳漏尺度 v1；QP gap 与 \(e_x\) 的不同见 [F35](FAILED_ROUTES.md#f35)。有限查询不能全空间认证 C21 |
| 拓扑限制 | 局部 all-pairs + EB + Dini + coverage + 不变开域 → 连续极限回缩 | 不由任意紧零集实现自动得到 |
| 去超临界幂的条件值域 | C70 整窗度量余量 + 同一指定 T 非空紧 usc 有理 acyclic + 每阶上同调满射 + χ(A)≠0 → C05-v2 扰动 coincidence 与原关系局部值域；只需 q>0，原稿 C05-v1 的 qγ>1 仍原样保留 | 新版本的条件拓扑链已重算；存在 qγ=1/2 的完整可行实例，原生整窗模型仍须独立认证 |
| 有限数据值域 | [C70 样本双包络](research/canonical/finite_sample_collar.md#fsc-envelope) + **另证**整窗每个输出的步界/EB + collar → 内域余量；再加 usc/acyclic、上同调与 Lefschetz → 原关系局部值域球 | C70 度量层已独立重算；原稿 C05-v1 仍是 PDF-only 候选；C05-v2 是保留整窗拓扑条件而去 qγ>1 的独立条件推导。有限样本不认证整窗 \(T\) |
| 大小比较 | LT 公共接口 → RLEB 能量证书；紧 T-only \(\Phi\) proper；C131 塔给一致回缩，C132 在新定义紧源关系上把输出步界转为真 EB；C133-v1/v2 后继选择保共同尾与同一极限，C134 紧满射非扩张仅有等距变换；C135 给已证闭预算块的紧步长谱上半连续；还缺自然完整母空间与保纲桥 | [算子空间证明](research/operator_space.md#os-tower-proof) 的 C131–C134 仅在所述紧源前提下成立；[C135](research/operator_space.md#os-spectrum-proof) 尚未对 LT/direct/energy 原生预算块认证闭性和穷尽性；总体规模命题开放 |
| 锥与 Markov | 冻结秩→面稳定→MSCQ；同步 OT exact-zero→一般 gauge，有限状态顶点→线性 EB | 两条独立链，跨线桥待证 |
| 不一致随机近端 | 有限维二次近端 + 正权重 + 固定守恒边缘 + 独立新噪声 → 活跃谱隙 → 条件 \(W_2\) 收缩 → 真实 law-step EB；逐分支残差零集另由共同定点决定 | C22/C23 本轮独立推导；与普通 \(W_2\)、物理步长、Markov 同步缺陷的替换不成立 |
| 规范例库 | 纯旋转：完整 J 严格收缩而 F 无强单调；正紧对角：严格单调+cocoercive 而无任意趋零 gauge EB；三次映射：固定目标/两变量/算法残差的精确模不同 | C24–C26 的三个对象及证明；历史 GX 编号是观察别名，不代表 77 个独立算子 |
| DR 切触与横截 | 同一算法残差 \(I-T\) 在切触线/抛物线有锐半阶 MSR 模 1、无统一一步距离严格收缩；横截两线有全域线性 MR/MSR 模 \(1/\sin\theta\) 和轨道因子 \(\cos\theta\) | C60/C61 是两个对象；不能把算法模换成法锥和的模 |
| 对角竖支闭图 | 完整原图的线性真 EB + 满输入完整近端的线性步 EB + 每选择线性有限长，与零锚 RL 同时成立；同输入跨支碰撞排除任意全对零消失模 | C72–C75/GX-075 独立对象卡；F25 阻断从动力逆推全对 RL |
| 身份与平方并图 | 同一完整 \(F(x)=\{x,x^2\}\) 的真残差锐半阶、完整目标窗两变量半阶 MR、二参数图区域；指定身份近端线性步 EB 与完整最小步半阶分离，跨支同输入碰撞 | C66–C68、C92、C95/GX-068；\(\mu,\rho<0,\mu\rho\ge1/4\) 的区域与 C89 的 \(A>0\) 门不交，不能从 MR 补全对 RL |
| 闭球法锥 | 完整 \(N_B\) 的锐全域非扩张反射与二参数区；固定零目标真空 MSR 系数下确界 0，却无任意正指数两变量 MR/HREG | C93/C94/GX-067、F29；先核域外残差与非孤立零集，不能把真空 EB 当逆稳定 |
| 惰性四状态同步 OT | 固定四点循环、0<p<1、同一输入对唯一不变律的 C-最优耦合 + 同步残差成本 → 精确零集与锐 √(13/p) 线性界；放松内层 OT → 同核假零点 | C71 独立重算；一般固定有限状态证书另见下行 C15，来源其余速率结论及优先权待审 |
| 同核不同随机表示 | 四状态核固定，改为逐状态独立 Bernoulli 的随机映射表示 + 同一 C-最优输入运输 → 同一零集但锐平方系数 13/[p(7−6p)] | [C88](research/topics/random_markov/lazy_cycle_representations.md#lcr-sharp) 新推导；表示会改变同步残差，不能从核身份直接迁移常数 |
| 固定有限状态同步 OT | 固定互异状态及核 + 同一 C-最优耦合 + 全部不变律 + 零成本 tight-edge 顶点行边缘不变 ⇔ 精确零集 ⇔ 全律空间锐线性 EB | [C15 完整证明](research/topics/random_markov/finite_state_certificate.md#fs-theorem) 已独立重写；不需混合性，也不推动力收敛。§5 备用证明和 §6 正则性另有去向 |
| 随机矩门与回耦 | 共同零点与正 excursion + 全部状态的同系数点态界 + \(pq\le r\) ⇔ 全部有限支撑律的标量矩界；另在同一随机表示、同一律类上把收缩 + 原 \(\Psi\) 的输入最优近极小对 + 回耦损失界合取 → 线性 EB | [C126/C127 自足证明](research/topics/random_markov/moment_recoupling.md)；两条是不同接口，条件残差 \(\mathcal R\) 不能替换 \(\Psi\)，原生模型的回耦门仍待认证 |
| 条件刷新两模型 | 固定 \(\nu\) 的有限 bit 以 \(a_*>0\) 刻画 \(\mathsf W_\nu/\mathcal R\) 锐 EB 与统一到目标率；Gaussian Gibbs 在 \(Q\succ0,p_i>0\) 下以 \(\zeta>0\) 给 \(W_{2,Q}/\mathcal R_Q\) 锐 EB | [C129/C130 独立证明](research/topics/random_markov/conditional_refresh.md)；两种状态空间、距离、残差及目标各自闭合，旧 E43 的二进制/Gaussian 节点错接已拆开；均不推出同步 \(\Psi\) 的 EB |
| 有限状态残差正则性 | 固定有限数据 + C-最优计划的固定矩阵 Hoffman 界 + 运输成本变化界 → Φ=Ψ² 全域 Lipschitz；有限 tight-edge 分支 → 连续分片仿射 | [C80](research/topics/random_markov/finite_state_certificate.md#fs-regularity) 不要求 C15 的 exact-zero 判据；正则性不推出 EB |
| 正值正弦的错目标边界 | GX-064 完整 F=2+sin x 在 λ=1 的全对临界 1/3 阶与目标 3 的固定目标半阶属于不同参考图点；F 零集为空 | C81/C82 的缩窗锐常数与每选择向负无穷的完整路径已重算；不能拼成零集 PPA |
| 有界平方的锐性与留域边界 | GX-065 完整有界图的全图临界半阶锐性见证在左端点，零点真残差半阶在零点；两界可同窗成立但 \(q\gamma=1/4\) | C83/C84 重算全部锐模；正输入路径仅有 \(1/k\) 衰减，负输入有限步越域；粗指数与缺留域不支持统一零点收敛 |
| 有界负恒等图的步长门 | GX-066 的同一完整图在 \(\lambda=1\) 使全部 Minty 输入塌为零；\(\lambda>2\) 则所有合法近端路径线性收敛，但反射线性模大于 1 | C96/C97 全图锐模与每步自然域重算；固定零目标真 EB、输入覆盖、反射收缩和动力稳定属于不同命题 |
| 斜等距加紧正对角 | 完整 `D+B` 在实 ℓ² 上全域双射，逆映射全局锐线性而强单调与 cocoercivity 模均为零 | C102/C103：直接谐和级数见证非 rectangular；完整近端严格收缩、全对反射锐常数 1，不能相互授予严格性 |
| 有界负平方的全图与路径 | 完整 `-x²` 限在 `[0,1/2]`，步长 1 的全图端点半阶 RL 与零点真残差半阶同时成立 | C100/C101：全图锐常数 2、真 EB 锐常数 1；正侧近端路径有限步越域，不能把两个半阶模当作零点收敛 |
| Volterra 积分的逐点与统一量词 | 完整 L² 图全域近端、全对反射锐 1；零均值方向与高频向量分别见证图几何和残差障碍 | C104/C105：非 rectangular 且任意消失 gauge 的真残差与步残差 EB 均失败；每条近端轨道强收敛，每个有限幂范数仍为 1 |
| 负三次的完整图与图块 | 完整 F=−x³ 的零输入三根否定全对 RL；受限 [−M,M] 在 3λM²<1 才有锐图块线性模 | C106/C107：固定零目标与两目标锐 1/3 系数不同；图块非零路径有限步离开自然域，不能赋给完整多值近端 |
| 孤立极点图与阶梯图 | 前者完整图的零输入纤维按 λ=ε² 分相，后者全图线性 RL 按 λ=δ 分相，亚临界算术类型决定是否有精确碰撞 | C108–C111：真残差任意幂的零下确界模不提供两变量目标覆盖或非零无限路径；阶梯的完整最小步界需对全部 J 纤维取最小 |
| 负平方乘阶梯 | 两完整关系在 Euclidean 直积，线性段全图模取分量最大，但临界半阶的完整乘积最优常数须联合优化 | C112–C114/GX-057：零目标真 EB 锐半阶与仅零路径无限合法；临界全图锐系数严格大于 2，图点输出共同窗才为 2，仅限输入的固定窗仍严格大于 2 |
| 斜旋转法锥的逆像与全图反射 | 二维完整 \(K+N_B\) 的每个目标有唯一原像；全部图点给 \(\|\Delta x\|^2\le2\|\Delta y\|\)；同图另核单调与全部近端纤维 | C98/C99：原算子 MR 的锐半阶；C124/C125：rectangular 而非 paramonotone、完整近端满域，反射全图线性锐常数 1；两个残差坐标分开 |
| 负平方根的图身份门 | GX-032 的短受限图 \(F_U\) 有锐全对 \(L=3\) 与真二次 EB，但任一非零输入仅有一步；半直线母图 \(F_\infty\) 有远支，同输入碰撞 | C85–C87 分别重算两个完整关系，F28 禁止把短图证书与母图或无限轨道拼接 |
| 异维数正则性与两残差 | GX-076 的最近逆点线性但固定/双变量锐半阶；GX-077 的原算子残差跳跃系数下确界 0，但近端步残差锐系数 1 | C76–C79 独立对象卡；不能将 GX-076 赋予同空间 RL，也不能互换原算子与近端残差 |
| 固定目标随机近端 | 同一全局 prox + 域内平稳律 → 吸收支持；非乘积闭近端图 + fair tie 核 → 有限长非不变极限及完整 \(W_2\) 邻域无 law-step gauge EB | C62-v2/C63；从吸收点识别完整单点纤维需每个纤维有限且逐成员正选择，[F37](FAILED_ROUTES.md#f37) 反驳旧 C62-v1；与随机换目标 C22/C23、Markov 同步 OT \(\Psi\) 分离 |
| 非线性矩提升 | 连续非减 gauge + 实际硬支持 + 全部概率律 → 凹包络锐式；同一变量两条点态证书先复合再取矩 | C69 抽象工具；临界分开聚合损失见 F24，原生合法耦合和目标边缘未证 |
| 参数与逻辑转换 | 同图换步：旧 Cayley → \(Q=\alpha I+\beta C\)，新 Cayley 良定 iff \(Q\) 单射；线性 RL → tied 参数曲线；有界输入域高指数→低指数；真残差 EB → 选中值界 | C27–C30 分别限定相同对象、配对与尺度，折叠和分支反例阻断逆向推理 |
| 非 tied 二参数图 | 同图全对 \(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\) + \(A>0,\Delta\ge0\) → 平移 Cayley 球、锐普适反射/近端模；另合取 Hilbert 扩张 → 同参数图极大 iff 满 Minty 域；\(\Delta>0\) 才有可逆单调图变换 | C89–C91 从 9/01 §2.1 重写，步长端点碰撞和母图完整纤维范围均单列 |
| 合法多步路径 | 实际前缀 coverage ∧ 统一终点收缩 ∧ 可求和块内位移 ∧ 初值留域 → 每条轨道有限长收敛；块 RL/输出 EB 只生产终点估计 | C31–C33 已重新证明；无限词逐词指数 >1 不给统一半径，周期相位极限须单独处理 |
| M1 显式动力 | 同一状态的活动关系 \(s=a-3b\) → 球内两步捕获及锐一步距离因子 \(3/\sqrt {10}\) | C38/C39 对给定单值 T 重算；原生多值方程到 T 的桥仍未核，不能声称一步定理严格失败 |
| M1 的新 Sign 实现 | 新定义的全部 \(F_{\rm lift}\) 图值 → 全域完整 \(J_F=T\) 与端点真残差锐线性模 3；指定输入球上全对 RL 最大指数 \(1/3\)；同一个 T → C38/C39 动力可调用 | C64/C65 是新关系；历史原生循环方程缺相位/全部选择，不能认作它 |
| 幂次剪切校准 | 完整三角图与真残差 EB + 有界窗全对 \(\gamma\)-Hölder + 切向余量 → 法向速率精确可达 \(\gamma q\) | C42/GX-071，只是反向构造的可达例；无界全图 RL、普适精确速率都不成立 |
| 振荡剪切分离 | 完整三角图 + 振荡两尺度 → 有界窗最大全对指数 \(\gamma\)；同一映射的双边真实阶为 \(q>\gamma q\) | C43/GX-072，说明全对最坏指数可能保守；归一化 Q 因子未证收敛 |
| 自然域逃逸 | 指定 Minty 域振荡反射 + 锚定 \(\alpha\)、全对 \(\alpha/(\beta+1)\) + 线性真残差 → 非零轨道有限步出域 | C44/GX-073；一步尺度不能称收敛阶，改变域或延拓后是新对象 |
| 孤立零点分支 | 同图 germ 三模平坦性 + 真 EB + 指定输入/输出窗口及小步门 → 上 \(q\) 阶；再加正归一化极限 → 精确 Q 因子 | C45/C46；选中值不倒推真 EB，完整纤维另证 |
| 离散覆盖障碍 | 完整紧图全对 RL + \(S=K\) 上真 EB 仍不提供零点输入球 | C47/GX-074；coverage 独立 |
| 非孤立对齐 | 输出最近零点锚 + 全家族真 EB/小步门 + 正指数统一锚模 → 上 \(\theta q\) 阶；同序列三重饱和才给锐性 | C48、C49-v2、C50-v2；\(B=1/\lambda\) 还需步长趋零，[F38](FAILED_ROUTES.md#f38) 隔离旧量词；无最近点另用正容差 |
| 移动锚反射 | 同一实际图点的真 EB + 输出近锚 + 小残差 → 相对该锚的反射比趋 1；幂型给定量缺陷 | C51/C52；固定锚与集合距离收缩需要别的桥，F18 有反例 |
| 复合次正则 | 原生凸外层 EB ∧ 满行秩定量修复 ∧ 链式残差下界 → 复合真实 EB；再加全部乘子界、步长门、gauge 兼容和留域 → 局部近端有限长 | C34–C37 已重写；尖点外层特例在 C40，秩亏原生推广开放；历史 C11 不等于回缩 C11 |
| 复合模型的独立边界 | 曲面尖点外层 + 真残差间隙 + 局部近端步长门 → 一步识别；光滑驻点极大序列 → 无弱分离时二阶目标 EB 失败 | C40/C41 本轮重算；前者图真多值而局部输出唯一，后者只攻击到 \(\Theta_2\) 的扩大陈述 |

9/14 历史包本身已有 149 个实体、35 条超边；本图以它为搜索种子，读入 9/18–9/25 版本后重新判断，没有把历史边直接升级为当前真理。

[孤立零点平坦性](research/canonical/isolated_zero_flatness.md) 将图 germ 的代数、完整残差纤维、指定分支轨道上阶和正因子的额外极限分开；[GX-074](research/topics/path_dynamics/discrete_coverage.md) 给紧全图仍无 coverage 的见证。

[非孤立对齐](research/canonical/nonisolated_alignment.md) 用输出最近零点的锚距离及最近点漂移解释 \(\theta q\) 上界；无 proximinality 的近似锚与正 Q 因子各有附加门。[F17](FAILED_ROUTES.md#f17) 防止把不同序列的最坏指数相乘。

[移动锚反射](research/canonical/moving_anchor_reflection.md) 的逐图点双边比与幂型常数只围绕随输出选取的 p；线性零集反例使固定锚和集合距离的错误升级可直接检查。

[全对验证器](research/canonical/all_pairs_verifier.md) 划清图块零集与完整零集的距离门；C57 的完整多值图在全对 RL、满输入覆盖和输出真 EB 下仍缺指定锚，并保留远端完整分支。

[闭图与 Minty 自然域](research/canonical/closed_graph_minty_domain.md) 从同一图块的近对角线模证明闭图—闭域等价，并把“域另已稠密”作为满覆盖的承重前提；它不产生残差 EB 或完整图排他。

[残差窗口桥](research/canonical/residual_window_bridge.md) 固定真全纤维残差、gauge 定义域与阈值正性；闭完整图上的扁平 gauge 反例说明一般窗口 EB 不能未经条件改成邻域 EB。[F21](FAILED_ROUTES.md#f21) 保存错误推理的断点。

[指定分支局部定理](research/canonical/named_branch_local.md) 将旧 foundations §4–§5 的 anchored 近似锚、实际真残差 EB、Hilbert 完备性和留域预算写成 C53/C54；[振荡完整图 C55](research/canonical/named_branch_local.md#nb-oscillation) 把它同全对 RL 的逻辑边界具体化。

## Research Frontier

**首要开放点**是完整、参数中立、非退化的算子母空间与规模量尺。9/20 的 \(\Phi=(\text{实际尾},\text{实际反射模})\) 在固定紧 T-only 图卡 proper，但 proper/quotient 不推出 category-preserving，局部观测丢失完整 \(F\) 的域外信息。9/21 总账报告普通 Baire、轨道理想与旧动力度量孔隙性同时把目标类判小；原证明恢复情况须逐项核对。详见 [operator_space.md](research/operator_space.md)。

结构稿的 proof obligations：Hilbert Hölder 扩张已有[逐项重写和准确一手导入](research/canonical/holder_extension.md)；统一影子常数下界、有限维 degree、fixed-set 构造、固定窗口 completion 与有限样本覆盖仍需各自审查；有限总查询的全空间障碍要保持确定性、无界域量词。[值域与有限数据](research/range_finite_data.md)。9/25 的 rational morphism Lefschetz 定理现有[逐条件一手核验](research/LITERATURE.md#lit-grn-2002)；有限样本仍只认证包络，不认证整窗 \(T\) 的拓扑性质。9/19 随机推论用到**给定度量完备**，若“Polish”仅按拓扑意义，已有显式反例；见 [holder_structure.md](research/holder_structure.md) H06。

## Known Results、Refuted / Failed、Open Problems

- 可直接复核的代数：Cayley 双向坐标、固定步长全域完整 resolvent 的原图反演、同图块内同输入唯一。
- 有证明文本和限定内部审计的研究结果：局部 RLEB、固定紧源 \(\Phi\)、解选择修订版、锥与 Markov 条件命题。候选稿与外部审稿、文献新颖性是独立层。
- 已证伪的扩大陈述：局部 \(J_{\mathcal G}\) 自动等于完整 \(J_F\)；Polish 拓扑性质自动给指定度量完备；proper 即保纲。精确反例和可回收部分见 [FAILED_ROUTES.md](FAILED_ROUTES.md)。
- 尚未解：总体规模比较；9/21 N10 原孔隙否定证明可追溯性；9/25 整窗拓扑模型认证及剩余证明审查；各固定维数影子最优常数；同对象同量词的全球先行性。
- 新的 C22/C23 以完整证明写入[随机近端模块](research/canonical/random_proximal.md)：条件 law-step 与逐分支推前残差具有不同零集；标量例使 EB 的统一常数锐。历史验证器的有限运行记录与证明分开保存。
- [规范例库](research/canonical/example_atlas.md) 已重写 GX-004/009/021 所指的三个对象，分别证明收缩逆推的边界、无限维无 gauge EB、三种局部模的精确常数；其余 GX 性质仍按逐单元义务处理。
- [DR 双对象卡](research/topics/examples/dr_tangency_transversality.md) 从 GX-069/070 重算算法残差的切触/横截锐模；[固定目标随机近端](research/topics/random_markov/proximal_selection_seam.md) 重算吸收、核接缝和真 law-step 障碍。[新 Sign 图](research/topics/path_dynamics/m1_sign_lift.md) 给显式 M1 映射一个可核的完整多值实现，历史原生方程身份仍开放。
- [参数字典](research/canonical/parameter_dictionary.md) 的同图换步公式、\(\gamma=1\) tied 端点、有限尺度换指数、真残差方向及 MR/MSR 量词已分别给证明或反例。它是可调用的条件记录，不替代外部定理的先行性核验。

## Next Actions

1. 冻结总体比较的**计数对象、三类认证量词和大小不变量**的一页规格，先用 N05/N08/N09/N10 及远端自由度反例攻击，再尝试总体定理。
2. 逐项追索 9/21 的 I-097–099、I-102；可恢复者重构证明，缺者保持报告状态。已恢复的 I-001/I-002/I-003–005/I-059/I-075 也分别核版本和证据身份。
3. 为 9/25 §8 配对可编译源，并为一个目标原生模型逐输出认证整窗指定 \(T\) 的近端包含、两项估计、紧 usc/acyclic、上同调及同一 collar；[C70 包络](research/canonical/finite_sample_collar.md)与[引文适用门](research/LITERATURE.md#lit-grn-2002)已核，不能把有限样本认证当成这些全称条件。
4. 若制作 9/19 新投稿版本，明写随机推论所用**给定度量完备**假设并保留原措辞反例；分别推进结构、锥、Markov 的外部先行性核验。
5. 从[逐单元去向](research/audit/UNIT_DISPOSITIONS.tsv)继续核 foundations 尚未分项裁决的定义、其余 GX 单元，以及 M1 **历史原生循环图到已验显式 T 的桥**；新构造 C64 只说明一个可行 Sign 实现。GX-069/070 和非乘积随机近端的选定单元已有明确去向，不代表整个来源包关闭。下一步还应核复合秩亏原生桥和未审外部文献。新证明按[增长协议](RESEARCH_PROTOCOL.md)进入主题目录，再更新 Claim、图与前沿。

## File Map

| 仓库根相对完整路径 | 数学资产、目的、何时读取或更新 |
| --- | --- |
| [research/canonical/isolated_zero_flatness.md](research/canonical/isolated_zero_flatness.md) | IZ-GERM/FIBERS 与 C45/C46：孤立零点的图 germ 换算、真残差全部小纤维门、分支上阶及正 Q 因子的额外极限；研究孤立解 PPA 时读。 |
| [research/canonical/nonisolated_alignment.md](research/canonical/nonisolated_alignment.md) | NA-OBJECT/DRIFT/COMPOSE/APPROX/SHARP 与 C48、C49-v2、C50-v2：非孤立零集的锚漂移、正指数下的统一 gauge 上界、无最近点的正容差修补、同序列锐性；研究 \(\theta q\) 或 tangent drift 时读。旧量词版本及反例在 [F38](FAILED_ROUTES.md#f38)。 |
| [research/canonical/moving_anchor_reflection.md](research/canonical/moving_anchor_reflection.md) | MA-OBJECT/REFLECT/POWER/LIMIT 与 C51/C52：实际图点的输出近锚反射、幂型系数、固定锚及集合收缩反例；把局部 EB 用于反射或选锚时读。 |
| [research/canonical/named_branch_local.md](research/canonical/named_branch_local.md) | NB-OBJECT/LOCAL/POWER/OSCILLATION 与 C53–C55：Hilbert 空间不取最近点的 anchored 分支收敛、局部闭性、幂次退化门及全对线性 RL 的振荡反例；要将局部 PPA 从全对图块改为指定分支时读。 |
| [research/canonical/all_pairs_verifier.md](research/canonical/all_pairs_verifier.md) | AV-OBJECT/BRIDGE/GAP 与 C56/C57：同图块全对 RL、输入 coverage、零锚保距离三项如何生产指定 B/A，以及缺少保距离的完整多值反例；从 R02 接入 C53 时读。 |
| [research/canonical/closed_graph_minty_domain.md](research/canonical/closed_graph_minty_domain.md) | CG-OBJECT/CLOSURE/BOUNDARY 与 C58：完备 Hilbert 空间内近对角线消失模使图闭 iff 自然输入域闭；只有另证稠密才得满 coverage，且图块不排除完整外纤维。从闭图尝试推出输入存在性时先读。 |
| [research/canonical/residual_window_bridge.md](research/canonical/residual_window_bridge.md) | RW-OBJECT/POSITIVE/FLAT 与 C59：全纤维残差窗口、一般非减 gauge 正阈值下的缩域充分门，以及完整闭图的平坦 gauge 反例；调用 EB 时若残差可能超窗口或 gauge 有限定义域，先读。 |
| [research/canonical/local_range_without_supercriticality.md](research/canonical/local_range_without_supercriticality.md) | C05-v2：在 C70 与整窗拓扑条件已合取时把原稿 qγ>1 降为 q>0 的逐步证明，并给 qγ=1/2 的精确可行 collar；评估局部值域候选时与原稿 v1 并读，不用样本代替整窗认证。 |
| [research/canonical/finite_sample_collar.md](research/canonical/finite_sample_collar.md) | C70：9/25 §8 的实际样本距离上下包络和需要**全部整窗输出**条件的留域余量；证明不调用拓扑定理。读 C05 前先区分样本认证、分析余量、原稿 C05-v1 的候选状态及 C05-v2 已重算的条件拓扑链；原生模型整窗认证仍开放。 |
| [research/topics/path_dynamics/discrete_coverage.md](research/topics/path_dynamics/discrete_coverage.md) | C47/GX-074：紧完整图的全对 RL、真 EB 与自然 Minty 域缺口；从图模推输入存在性时读。 |
| [research/HYPERGRAPH.md](research/HYPERGRAPH.md)、[research/graph.json](research/graph.json) | 精确文字关系与机读节点边。数学 Claim 或条件边变化时按规范正文改图并运行 [research/build_graph.py](research/build_graph.py)；表现层只消费图，不能从景观倒推数学状态。 |
| [visualization/cosmos/](visualization/cosmos/README.md)、[动态宇宙](visualization/cosmos/index.html)、[像素舰船与星球图鉴](visualization/cosmos/art/contact-sheet.png)、[语义契约](visualization/COSMOS_SEMANTIC_CONTRACT.md) | 当前研究图的动态视图：原图 JSON、固定语义锚点、D3 力学、真实图节点的公转、合取阵点及沿正向航道运动的多构型舰船。20 种结构船型和 12 种星球地貌有可再生的 SVG 与多尺度接触表；造型不评级数学状态。新增或修订超边后运行 `build.py`，核对布局及关系回归。 |
| [visualization/xianxia/](visualization/xianxia/README.md)、[物件图鉴](visualization/xianxia/gallery.html)、[数学山海图](visualization/xianxia/index.html)、[增长交接](visualization/xianxia/HANDOFF.md) | 上一版修仙视觉实验，保留可编辑 SVG、静态世界清单与离线 HTML 供设计对照；新宇宙视图在 `visualization/cosmos/` 独立维护。 |
| [research/map.html](research/map.html)、[research/map/](research/map/) | 更早的像素探索图与可再生前端源码，保留作兼容和设计对照；精确关系仍以 `research/graph.json`、规范正文及 `CLAIMS.md` 为准。 |
| [research/LOGIC_CONTRACTS.md](research/LOGIC_CONTRACTS.md) | 关键超边的固定对象、量词、合取 side conditions 与不蕴含；使用跨稿箭头或改 Claim 版本时先核。 |
| [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md)、[research/validate_assets.py](research/validate_assets.py) | 新资产的精确身份、状态、证据与生长门槛；结构检查哈希、图目标和规范链接。新 Claim 进入前后读协议并执行校验。 |
| [research/foundations.md](research/foundations.md) | D01–D04 的关系、剪切、真残差、局部/完整区别；遇到定义混用先读。 |
| [research/rleb_ppa.md](research/rleb_ppa.md) | R01–R04：一步估计、两种证书、局部收敛、signed-Schur 验证和接缝；研究 PPA 假设时读。 |
| [research/holder_structure.md](research/holder_structure.md) | H01–H07：影子、纤维分类、Dini、回缩、随机完备性反例、9/25 值域候选；审结构或局部拓扑时读。 |
| [research/LITERATURE.md](research/LITERATURE.md)、[research/canonical/holder_extension.md](research/canonical/holder_extension.md) | LIT-GRN-2002 核 C05 的一手拓扑门；LIT-ALM-2021 Theorem 1.2 + HE-SNOWFLAKE/EXTENSION 核 H01 的 Hilbert 同常数扩张及固定参数 graph-maximal。引文核验不自动升级整稿。 |
| [research/range_finite_data.md](research/range_finite_data.md) | W01/Q01–Q04/B01：9/23 的锐值域球、固定窗口、同一有限 QP、参数覆盖、三项误差、有限查询障碍与 deadband；[Q03](research/range_finite_data.md#q-eval) 分开 QP 输出误差 \(e_N\) 与反演求值证书 \(e_x\)，要从结构定理走向可计算证书时读。 |
| [research/solution_selection.md](research/solution_selection.md)、[solution_selection_rates.md](research/canonical/solution_selection_rates.md)、[selection_geometric_cap.md](research/canonical/selection_geometric_cap.md)、[selection_geometric_sharpness.md](research/canonical/selection_geometric_sharpness.md)、[selection_parameter_family.md](research/canonical/selection_parameter_family.md)、[selection_tangential_condition.md](research/canonical/selection_tangential_condition.md)、[selection_superlinear_family.md](research/canonical/selection_superlinear_family.md) | S01–S03、C08、C115/C116、C136–C141：统一尾有限前缀的尺度证明；R01/R02 到同球共同轨道窗及完整近端的逐纤维门；**两种不同**完整二支模型分别给几何尾与 Q 二次尾。C137 的 §2 几何图有全对 RL、真 EB、固定兼容半径和共同尾；C138 的 §3 首次切换给同一图匹配配对下界。C139 推广到任意 0<γ,q<1 的同族证书与匹配阶；C140 则独立给出衰减切向敏感度恢复混合稳定性的充分门及尖点边界；C141 是超线性法向尾的任意 ν>1 候选族，逐轨道 Q-ν 与两点伸缩指数的量词分开。研究初值到极限解稳定性时读。 |
| [research/canonical/signed_schur_growth.md](research/canonical/signed_schur_growth.md) | C117–C119：双支 signed-Schur 的闭参数域图包含、切向球内全对模与完整纤维门；幂次/同修正坐标匹配、平方根原生图及反例。核局部 R04 或把图块结论转成完整近端前读。 |
| [research/operator_space.md](research/operator_space.md)、[固定紧源观测证明](research/canonical/compact_t_observation.md#ct-proper) | LT 嵌入、完整图信息、\(\Phi\) 的自足 proper 证明、C131–C134 四条紧源条件证明，以及 C135 闭预算关系的紧步长谱引理；原关系 \(F_{T,K}\) 的域是 \(T(K)\)，其近端输入域才是 \(K\)。若要把 C135 用于 LT/direct/energy，先分别核预算块闭性与证书穷尽；总体比较工作入口。 |
| [research/canonical/sigma_compact_baire.md](research/canonical/sigma_compact_baire.md#sc-proof) | C128：已给定 σ-紧度量空间的 Baire 等价判据；判据不替目标算子空间构造紧层或证明保纲。 |
| [research/cone_markov.md](research/cone_markov.md) | 锥秩–面–MSCQ 和 Markov 同步/条件残差链、反例与跨线桥；研究旁支时读。 |
| [research/topics/random_markov/conditional_refresh.md](research/topics/random_markov/conditional_refresh.md) | C129/C130 的两种独立条件刷新模型：二进制固定边缘 \(\mathsf W_\nu/\mathcal R\) 的等价判据和锐系数；Gaussian \(W_{2,Q}/\mathcal R_Q\) 的条件耦合、谱门与局部锐性。跨模型调用或辨别旧图 E42/E43 时读，不把它们接成原同步 \(\Psi\)。 |
| [research/topics/random_markov/moment_recoupling.md](research/topics/random_markov/moment_recoupling.md) | C126 的非负标量矩门及更新后律空间小质量障碍；C127 的同步 \(D_\eta\)、回耦损失 \(\Delta_\eta\) 与同一近极小 OT 对的条件线性 EB。研究从收缩反推 \(\Psi\) 的 EB 或随机幂次提升时读；原生耦合仍是独立义务。 |
| [research/canonical/random_proximal.md](research/canonical/random_proximal.md) | RP-OBJECT/GAP/CONTRACTION/EB/BRANCH/SCALAR 的全证明、尖锐例和残差替换障碍；研究随机近端或条件 \(W_2\) 时读，改假设须另立版本。 |
| [research/canonical/example_atlas.md](research/canonical/example_atlas.md) | EX01 旋转、EX02 正紧对角、EX03 三次映射的完整对象卡、真残差、参数、证明及历史别名；检验某个逆推、EB 或常数边界时读，新增 GX 先区分对象与观察。 |
| [research/topics/examples/diagonal_spike_relation.md](research/topics/examples/diagonal_spike_relation.md) | C72–C75/GX-075：对角图加离散竖支的完整残差、每条近端路径、零锚/全对分离及精确二参数区；攻击“收敛或 EB 逆推全对 RL”时读。 |
| [research/topics/examples/positive_sine_phase.md](research/topics/examples/positive_sine_phase.md) | C81/C82/GX-064：完整正值正弦图的步长三相、临界全对和锚定常数、非零目标半阶及无零集路径；比较局部 RL 与 EB 时先核目标和基点。 |
| [research/topics/examples/bounded_square_minty.md](research/topics/examples/bounded_square_minty.md) | C83/C84/GX-065：有界平方完整图的全图临界端点折叠与精确 Hölder 常数、零目标真残差半阶、正侧 \(1/k\) 与负侧自然域逃逸；两界可同窗但收缩兼容和留域不成立。 |
| [research/topics/examples/bounded_negative_identity.md](research/topics/examples/bounded_negative_identity.md) | C96/C97/GX-066：完整有界负恒等图在 \(\lambda=1\) 的零输入多值、各指数锐全对常数及全部合法路径的步长相变；检验近端收缩与反射模、自然域覆盖能否互授时读。 |
| [research/topics/examples/skew_compact_diagonal.md](research/topics/examples/skew_compact_diagonal.md) | C102/C103/GX-059：完整无限维斜等距加紧对角的锐逆像、非 rectangular 直接反例、近端幂范数及反射锐非严格界；攻击正则性到图几何的逆推时读。 |
| [research/topics/examples/bounded_negative_square.md](research/topics/examples/bounded_negative_square.md) | C100/C101/GX-053：完整有界负平方图随步长的 Minty 相变、端点全对锐半阶、零点真残差与临界正侧有限步越自然域；检验 coverage 与留域时读。 |
| [research/topics/examples/skew_ball_inverse.md](research/topics/examples/skew_ball_inverse.md) | C98/C99/C124/C125/GX-058：同一完整盘法锥的全域逆像、边界半阶、单调/rectangular 图几何、完整近端和全图反射锐模；研究原算子 MR 与 Cayley RL 的不同量词时读，两者各有独立推导。 |
| [research/NOTATION_CONTRACT.md](research/NOTATION_CONTRACT.md) | 跨主题符号表：RL 参数顺序、完整图和图块、真/步/算法/概率残差，以及锥、Markov、二参数图的局部字母重绑定；从某个方向引用另一方向结论前读。 |
| [research/topics/examples/restricted_root_graph.md](research/topics/examples/restricted_root_graph.md) | C85–C87/GX-032：严格分开受限负平方根完整短图与半直线完整母图，给锐成对常数、真二次 EB、受限无续步、母图远支与发散；从受限算法向母图推断时先读。 |
| [research/topics/examples/hemiregular_piecewise_parabola.md](research/topics/examples/hemiregular_piecewise_parabola.md)、[research/topics/examples/absolute_value_subgradient.md](research/topics/examples/absolute_value_subgradient.md) | C76/C77 与 C78/C79：前者是异维数完整映射的最近逆点与两变量正则对照、局部非闭图；后者把绝对值次梯度的原算子真残差跳跃和软阈值近端步残差分开。研究 MR/MSR 量词或残差模传递时读。 |
| [research/topics/examples/README.md](research/topics/examples/README.md)、[research/topics/examples/identity_square_branch_union.md](research/topics/examples/identity_square_branch_union.md)、[research/topics/examples/dr_tangency_transversality.md](research/topics/examples/dr_tangency_transversality.md) | C66–C68/C92/C95/GX-068 的完整并图、两种真残差、两变量半阶 MR、跨支碰撞及精确二参数区；C60/C61/GX-069/070 的 DR 算法残差锐模。先区分原算子、选支、完整步和算法残差。 |
| [research/topics/examples/ball_normal_cone.md](research/topics/examples/ball_normal_cone.md) | C93/C94/GX-067：完整法锥的全域投影/反射、二参数区，以及固定零目标的真空模与扰动逆像跳变；要用非孤立零集的 EB 或从反射稳定逆推 MR 时读。 |
| [research/topics/random_markov/lazy_cycle_ot.md](research/topics/random_markov/lazy_cycle_ot.md) | C71：惰性四循环的原同步 OT 残差、锐全律空间误差界及放松最优运输后的假零点；判断有限状态残差是否保留输入 OT 约束时读。 |
| [research/topics/random_markov/lazy_cycle_representations.md](research/topics/random_markov/lazy_cycle_representations.md) | C88：同一四状态核与不变律在共同开关及逐状态独立开关表示下的同步成本、零集和两个不同的锐模；改随机表示或比较核与残差时读。 |
| [research/topics/random_markov/finite_state_certificate.md](research/topics/random_markov/finite_state_certificate.md) | C15-v1：固定有限数据、全部平稳目标律与 C-最优计划的有限 tight-edge 证书、锐 EB 及动力边界；§5 零面/空零面备用证明。C80 独立证明 Ψ² 的全域 Lipschitz 与连续分片仿射，不假定 exact-zero。研究同步 OT 时先读。 |
| [research/topics/random_markov/README.md](research/topics/random_markov/README.md)、[research/topics/random_markov/proximal_selection_seam.md](research/topics/random_markov/proximal_selection_seam.md)、[research/topics/random_markov/scalar_moment_envelope.md](research/topics/random_markov/scalar_moment_envelope.md) | C62-v2/C63 固定目标全局近端的吸收与核接缝；C62-v1 的有限纤维漏门和 [F37](FAILED_ROUTES.md#f37) 同页可核。C69 连续 gauge 的锐标量矩包络与分开聚合损失须另证明原生合法耦合和硬支持。 |
| [research/canonical/parameter_dictionary.md](research/canonical/parameter_dictionary.md) | PD-QUANTIFIERS/CAYLEY/TIED/STEP/SCALE/RESIDUAL/REGULARITY：同一图换步的单射门、尺度、真残差和 MR/MSR 的量词；引入或改变 RL 参数、正则性、选中步残差时先读。 |
| [research/canonical/non_tied_cayley.md](research/canonical/non_tied_cayley.md) | C89–C91：非 tied 二参数全对条件的平移 Cayley 球、两项锐普适常数、步长门、退化面、单调图双射和 Hilbert 同参数图极大等价；从 tied 曲线推广或引用完整 Minty 覆盖时先核 \(A,\Delta\) 与图范围。 |
| [research/canonical/path_atlas.md](research/canonical/path_atlas.md) | PA-DEF/WHOLE/BLOCK/POWER/CYCLES：每条合法路径的前缀延拓、块内预算、整轨道证明；无限词统一性反例及非平凡周期的独立相位结论。做多步或多值算法时先核实际分支与留域。 |
| [research/topics/path_dynamics/README.md](research/topics/path_dynamics/README.md)、[research/topics/path_dynamics/m1_capture.md](research/topics/path_dynamics/m1_capture.md)、[research/topics/path_dynamics/power_shear.md](research/topics/path_dynamics/power_shear.md)、[research/topics/path_dynamics/oscillatory_shear.md](research/topics/path_dynamics/oscillatory_shear.md)、[research/topics/path_dynamics/domain_escape.md](research/topics/path_dynamics/domain_escape.md) | 路径主题入口与独立对象卡：C38/C39 的 M1 端点球和原生图缺口；C42 的可达性；C43 的保守指数；C44 的自然域逃逸与全纤维线性残差。新增对象先辨图、窗口和零集。 |
| [research/topics/path_dynamics/m1_sign_lift.md](research/topics/path_dynamics/m1_sign_lift.md) | C64/C65：新定义完整 Sign 图的全部纤维、全域 \(J_F=T\)、端点真残差模 3 和指定球上局部最大全对指数 \(1/3\)；历史原生循环方程仍须原始定义和路径桥。 |
| [research/canonical/composite_subregularity.md](research/canonical/composite_subregularity.md) | CS-TRANSFER/EB/PROX/MODEL：满行秩修复、链式真残差、局部近端轨道及曲面幂/非幂锐例；秩亏反例和开放乘子门。研究复合目标或调用历史 C11 时先辨身份。 |
| [research/topics/composite_regular/README.md](research/topics/composite_regular/README.md)、[research/topics/composite_regular/cusp_identification.md](research/topics/composite_regular/cusp_identification.md)、[research/topics/composite_regular/oscillating_target.md](research/topics/composite_regular/oscillating_target.md) | 复合主题可扩写入口与 C40/C41 独立证明：真多值次梯度的局部一步识别门、弱分离缺失时驻点极大序列的目标正确 EB 障碍。新增秩亏机制或目标反例时分别开卡，先核同一目标和真实残差。 |
| [research/audit/SOURCE_RECONSTRUCTION_AUDIT.md](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md)、[SOURCE_FILE_INVENTORY.tsv](research/audit/SOURCE_FILE_INVENTORY.tsv)、[ZIP_MEMBER_INVENTORY.tsv](research/audit/ZIP_MEMBER_INVENTORY.tsv)、[LEGACY_VERIFIER_RUNS.json](research/audit/LEGACY_VERIFIER_RUNS.json) | 251 个原件及 178 个包内成员的路径/哈希/语义未决字段，旧验证器环境与运行输出；逐源重写时更新 disposition 与规范锚点，不能将盘点算验收。 |
| [research/topics/examples/volterra_integration.md](research/topics/examples/volterra_integration.md)、[adjoint_volterra.md](research/topics/examples/adjoint_volterra.md)、[negative_cubic_branch.md](research/topics/examples/negative_cubic_branch.md) | C104/C105 与 C120/C121：Volterra 和伴随方向作为一个等距例型，右端点逆像另核；完整近端逐点强收敛而统一 gauge/有限幂界失败。C106/C107：负三次完整远支、图块锐模和路径越域。研究局部证书与完整算法时读。 |
| [research/topics/examples/planar_rotation_family.md](research/topics/examples/planar_rotation_family.md) | C122/C123：完整旋转族唯一 Minty 奇点、锐全对输入对距模、Fourier 循环阶与 GX-062/063 两角；修正旧稿“族内强模不决定循环阶”的过强解释。 |
| [research/topics/examples/isolated_pole_relation.md](research/topics/examples/isolated_pole_relation.md)、[rational_irrational_staircase.md](research/topics/examples/rational_irrational_staircase.md) | C108–C111/GX-055/056：前者全步长完整纤维、图窗、残差逃逸和全部合法路径；后者算术支纤维、锐 RL、真残差与完整最小步界。研究零系数模为何不提供输入/目标覆盖时读。 |
| [research/topics/examples/product_splice.md](research/topics/examples/product_splice.md) | C112–C114/GX-057：完整直积的全纤维、零残差与所有合法路径；临界全图、图点输出窗和仅限输入窗的不同锐半阶系数。组合不同例卡或改变图窗口时读。 |
| [research/audit/SOURCE_OCCURRENCES.tsv](research/audit/SOURCE_OCCURRENCES.tsv)、[PAYLOAD_GROUPS.tsv](research/audit/PAYLOAD_GROUPS.tsv)、[build_occurrence_index.py](research/audit/build_occurrence_index.py) | 429 个物理文件/ZIP 成员位置与 346 个不同字节内容的可复现索引；状态仍待逐段语义枚举，不能把来源组数当数学覆盖。 |
| [research/audit/SEMANTIC_UNIT_SEED.tsv](research/audit/SEMANTIC_UNIT_SEED.tsv) | 四个来源内容的连续行覆盖试点：S19（11 段）、SS1（19 段）、GX-053–065（39 段）及 F11 `04_research_ideas.md`（46 段）。C135 仅重写其中 G.1–G.2 的条件拓扑引理，G.3 reduction 仍开放；结构段内的独立属性和文献事实尚须逐项拆分。校验器检查行区间及已填锚点，不能把分段数量当验收率。 |
| [research/audit/UNIT_DISPOSITIONS.tsv](research/audit/UNIT_DISPOSITIONS.tsv) | 逐源单元的来源节、规范身份、精确锚点及未闭义务；目前 129 行有逐项去向（123 rewritten、3 superseded、3 deferred），只关闭列出的单元，不把整份原件标为已重写；[语义分母计划](research/audit/SEMANTIC_INVENTORY_PLAN.md) 另给全库逐段验收路径。新增历史单元时续记，原创工作直接从增长协议进入。 |
| [research/CODE_REGISTER.md](research/CODE_REGISTER.md) | 十个历史验证器 V01–V10 到当前 Claim/待重写对象的映射、执行范围和盲区；检查计算证据或重写可维护代码时读。新代码按协议进入 `research/code/<topic>/`。 |
| [research/code/README.md](research/code/README.md) | 新可复现实验的 Claim 绑定、seed、精度、运行与盲区模板；只有新程序经重新编写和验收后才进入此树。 |
| [research/SOURCES.md](research/SOURCES.md)、[research/HISTORICAL_EDGE_CROSSWALK.md](research/HISTORICAL_EDGE_CROSSWALK.md) | S14–S25/SS 的**完整原路径**、ZIP 成员与恢复身份；9/14 旧图 h01–h35 的逐边去向。由规范命题反查或确认旧关系是否丢失时读。 |
| [CLAIMS.md](CLAIMS.md)、[RESEARCH_STATE.md](RESEARCH_STATE.md)、[FAILED_ROUTES.md](FAILED_ROUTES.md) | 逐版本精确身份与显式状态、当前阻塞与完成门、已失败机制；每次进展后同步维护。研究状态是现行可执行前沿，旧提交记录保留在 Git 历史。 |
| [INGEST_MANIFEST.tsv](INGEST_MANIFEST.tsv)、[BATCH_README.md](BATCH_README.md)、[history/README.md](history/README.md) | 初始校验、旧批次盘点与原件使用约定；用于核原件，不再作为数学地图。原件保留在 `history/sources/`，Git 历史可追初始导入。 |

阅读顺序：本页和超边图 → 依节点进数学模块 → CLAIMS 的精确版本和现存 objection → 必要时 SOURCES 的原稿标签/页码。要写新资产时先读增长协议和当前前沿；图中路线是搜索种子，不是方法白名单。
