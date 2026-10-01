# 数学关系超边图

本图从 [graph.json](graph.json) 生成；运行 python3 research/build_graph.py 同时生成本页和 [交互 HTML](map.html)。每条边的输入是**合取**；范围、版本及证据状态不可省。节点链接进入重构的数学模块，原始证据见 [SOURCES.md](SOURCES.md)。

关系 conditional 带有额外前提，open 是目标而非证明，limits 是反例或边界；necessary 和 sufficient 分别对应纤维分类的两个方向；sharpness 只给声明范围内的下界见证。

## 定义

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E01 | [D01 · 完整图、真残差与图剪切](foundations.md#d01) ∧ [D02 · 全对 RL 与指定尺度](foundations.md#d02) | equivalence → [D03 · Cayley 表示](foundations.md#d03) | 同图块、同 λ、同输入对尺度；**代数可复核** |

## 收敛

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E02 | [D02 · 全对 RL 与指定尺度](foundations.md#d02) ∧ [COV · 图块 coverage 与最近零点图](rleb_ppa.md#cov) ∧ [D04 · 真实 EB 与 gauge](foundations.md#d04) | implies → [R01 · 一步能量、步长、输出界](rleb_ppa.md#r01) | 实际输出、最近解点均在图块；真残差 EB；**S19 稿内证明** |
| E03 | [R01 · 一步能量、步长、输出界](rleb_ppa.md#r01) ∧ [CMP · 统一兼容 κ<1](rleb_ppa.md#cmp) ∧ [LOC · 留域预算与闭零集](rleb_ppa.md#loc) | implies → [R02 · 局部 PPA 有限长度](rleb_ppa.md#r02) | 局部 J_G 轨道；完整 J_F 另需 FULL；**S19 稿内证明** |
| E04 | [R01 · 一步能量、步长、输出界](rleb_ppa.md#r01) ∧ [D04 · 真实 EB 与 gauge](foundations.md#d04) ∧ [LOC · 留域预算与闭零集](rleb_ppa.md#loc) | implies → [R03 · 能量证书与临界阈值](rleb_ppa.md#r03) | ψ 连续严格增、q_E<1、能量分支预算；**S19 稿内证明** |
| E05 | [R04 · signed-Schur 跨支验证](rleb_ppa.md#r04) ∧ [D04 · 真实 EB 与 gauge](foundations.md#d04) ∧ [CMP · 统一兼容 κ<1](rleb_ppa.md#cmp) ∧ [LOC · 留域预算与闭零集](rleb_ppa.md#loc) | conditional → [R02 · 局部 PPA 有限长度](rleb_ppa.md#r02) | Schur 定向、完整纤维排他和 EB 各自验证；**条件验证器** |
| E06 | [COV · 图块 coverage 与最近零点图](rleb_ppa.md#cov) ∧ [D04 · 真实 EB 与 gauge](foundations.md#d04) ∧ [CMP · 统一兼容 κ<1](rleb_ppa.md#cmp) ∧ [LOC · 留域预算与闭零集](rleb_ppa.md#loc) ∧ [DIN · 一般模与 Dini 条件](holder_structure.md#din) | conditional → [R05 · 一般模 RL + Dini 的点收敛](holder_structure.md#r05) | 一般模全对 RL；有限长度另需 Dini；**S19 一般模版本** |
| E25 | [R01 · 一步能量、步长、输出界](rleb_ppa.md#r01) ∧ [GROW · 真实残差幂增长](rleb_ppa.md#grow) | conditional → [CMP · 统一兼容 κ<1](rleb_ppa.md#cmp) | a<γ 自动小尺度；a=γ 要 λm>L/2；a>γ 此标量测试失败；**S19 residual growth** |
| E26 | [R01 · 一步能量、步长、输出界](rleb_ppa.md#r01) ∧ [GROW · 真实残差幂增长](rleb_ppa.md#grow) | conditional → [R03 · 能量证书与临界阈值](rleb_ppa.md#r03) | a=γ 的能量阈值 λm>L/√2，另一充分证书；**S19 能量分支** |
| E27 | [SCHUR · 反向 Schur 定向与全纤维排他](rleb_ppa.md#schur) | conditional → [R04 · signed-Schur 跨支验证](rleb_ppa.md#r04) | 切向反演、两支相反 signed growth、完整纤维和统一导数界；**S19 条件验证器** |

## 反例

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E07 | [LOG · 对数接缝精确门槛](holder_structure.md#log) | limits → [R05 · 一般模 RL + Dini 的点收敛](holder_structure.md#r05) | a≤1 的完整接缝：距离收缩仍无点收敛；**显式反例** |
| E28 | [COLLIDE · 逐支正则但跨支碰撞](rleb_ppa.md#collide) | limits → [R04 · signed-Schur 跨支验证](rleb_ppa.md#r04) | 逐支正则不能替代跨支定向；**S19 collision 反例** |
| E30 | [STOCH · 期望距离收缩与路径 Dini 步长](holder_structure.md#stoch) ∧ [POLISH-GAP · 拓扑 Polish 不保指定度量完备](holder_structure.md#polish-gap) | refutes → [STOCH-LIMIT · 随机极限在闭 S 内](holder_structure.md#stoch-limit) | X=(0,2) 通常距离；有限长度而极限在空间外；**本轮显式反例** |
| E32 | [F03 · 图块外额外输出反例](solution_selection.md#f03) | refutes → [FULL · 局部与完整 resolvent 一致](solution_selection.md#full) | F(u)={u,-u} 的图块 A1–A4；J_G(0) 单值、J_F(0) 全实线；**显式反例** |
| E39 | [C-NONAMEN · nice 非 amenable 边界例](cone_markov.md#c-nonamen) | refutes → [C-UNIV · 顶点系统普遍 MSCQ](cone_markov.md#c-univ) | nice 非 amenable 锥的线性满秩冻结系统失 MSCQ；**来源旧锥加本包路径** |
| E40 | [M-FALSE · 快混合仍 Ψ 假零](cone_markov.md#m-false) | refutes → [FAST-EB · 快混合必有原 Ψ exact-zero](cone_markov.md#fast-eb) | 公平 bit 一步平稳但相关律 Ψ=0、距不变律>0；**Markov 显式模型** |
| E41 | [M-NOPOWER · exact-zero 快率无正幂 EB](cone_markov.md#m-nopower) | refutes → [POWER-EB · exact-zero + 快率必有正幂 EB](cone_markov.md#power-eb) | 无限紧可数状态 exact-zero 且快率，却无任何局部正幂 EB；不反驳有限状态定理；**Markov 显式模型** |
| E52 | [Q-ORACLE · 无界域有限确定性总查询](range_finite_data.md#q-oracle) | implies → [Q-NOGLOBAL · 有限 transcript 无全空间认证](range_finite_data.md#q-noglobal) | 两张全局 Hölder 图在有限自适应查询上同 transcript、远端分离；**S23 不可区分反例** |

## 结构

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E08 | [H01 · 全局 RL 与固定参数 maximal](holder_structure.md#h01) ∧ [LIFT · 二次 excess 与正交提升](holder_structure.md#lift) | implies → [H02 · 同一强单调影子](holder_structure.md#h02) | 全图全尺度；正交扩张与 Banach contraction；**S23 稿内证明、局部重算** |
| E09 | [H01 · 全局 RL 与固定参数 maximal](holder_structure.md#h01) ∧ [PROPER · 有限维 properness、degree](holder_structure.md#proper) | necessary → [H03 · 有限维完整纤维分类](holder_structure.md#h03) | 有限维、graph-maximal、直径界；**S23 稿内证明** |
| E10 | [FIX · 任意紧集精确固定点构造](holder_structure.md#fix) ∧ [D03 · Cayley 表示](foundations.md#d03) | sufficient → [H03 · 有限维完整纤维分类](holder_structure.md#h03) | 每个非空紧 K、diam K≤R，存在某个 F；**S23 稿内构造** |

## 交叉限制

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E11 | [R05 · 一般模 RL + Dini 的点收敛](holder_structure.md#r05) ∧ [D03 · Cayley 表示](foundations.md#d03) ∧ [COV · 图块 coverage 与最近零点图](rleb_ppa.md#cov) | implies → [RET · 连续极限回缩](holder_structure.md#ret) | 一般模版本的同图块 all-pairs 连续性、共同开域与统一尾界；**S19 稿内证明** |
| E12 | [H03 · 有限维完整纤维分类](holder_structure.md#h03) ∧ [RET · 连续极限回缩](holder_structure.md#ret) | limits → [OB-TOPO · 非局部可缩零集的附加收敛假设障碍](holder_structure.md#ob-topo) | 任意紧零集实现不保证回缩；额外局部收敛假设排除 Cantor 型零集附近同时成立；**条件障碍** |
| E21 | [C-MSCQ · 原锥残差 MSCQ](cone_markov.md#c-mscq) ∧ [D01 · 完整图、真残差与图剪切](foundations.md#d01) | conditional → [D04 · 真实 EB 与 gauge](foundations.md#d04) | 需额外 d(G(x),C)≤χ(r_F(x)) 与同一零集；**尚未建立的一般桥** |
| E24 | [M-COND · 守恒边缘条件残差](cone_markov.md#m-cond) ∧ [M-PSI · 同步 OT 残差 Ψ](cone_markov.md#m-psi) | limits → [OB-RES · 条件残差不可代入同步 OT 能量](cone_markov.md#ob-res) | 条件残差不能直接替换同步 OT 残差；需同一耦合和回耦损失控制；**显式两 bit 障碍** |
| E44 | [M-MOMENT · 小质量混合 pq≤r](cone_markov.md#m-moment) | limits → [D04 · 真实 EB 与 gauge](foundations.md#d04) | 对有限支撑混合点态 q 阶到 Lp/Lr 需 pq≤r；跨确定性到随机的矩门；**Markov Proposition M** |
| E87 | [DC-GAP · 全对 RL 加真 EB 不给输入覆盖](topics/path_dynamics/discrete_coverage.md#dc-gap) | limits → [COV · 图块 coverage 与最近零点图](rleb_ppa.md#cov) | GX-074 反驳 D02∧D04→零点输入球 coverage 的无条件跳跃；COV 在局部 PPA 中仍须独立假设，不能改变目标 S=K。；**本轮紧图反例；非对已有 coverage 定理的反驳** |

## 局部拓扑

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E13 | [SAMPLE · 有限 proximal 样本与包络](holder_structure.md#sample) ∧ [WINDOW · 整窗 usc、acyclic 与上同调条件](holder_structure.md#window) | conditional → [H07 · 原关系局部值域候选](holder_structure.md#h07) | collar、χ(A)≠0、同调满射、rational Lefschetz；指定 T 可为子关系；**S25 候选；外部定理门未闭** |

## 解选择

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E14 | [TAIL · 共同轨道与统一尾界](solution_selection.md#tail) ∧ [D02 · 全对 RL 与指定尺度](foundations.md#d02) | conditional → [S01 · 极限解选择的对数模](solution_selection.md#s01) | 共同迭代域、统一几何或超几何尾；D02 给局部 Hölder；**修订包内部审计** |
| E15 | [R02 · 局部 PPA 有限长度](rleb_ppa.md#r02) ∧ [TAIL · 共同轨道与统一尾界](solution_selection.md#tail) | implies → [S02 · RLEB 极限选择版本](solution_selection.md#s02) | 仅局部 J_G；若要完整 J_F 加 FULL；**修订版** |
| E16 | [R02 · 局部 PPA 有限长度](rleb_ppa.md#r02) ∧ [FULL · 局部与完整 resolvent 一致](solution_selection.md#full) ∧ [TAIL · 共同轨道与统一尾界](solution_selection.md#tail) | conditional → [S02 · RLEB 极限选择版本](solution_selection.md#s02) | 完整 resolvent 的共同轨道区域一致性；**修订版** |
| E31 | [S01 · 极限解选择的对数模](solution_selection.md#s01) ∧ [SEL-EX · 完整半代数二值例与匹配下界](solution_selection.md#sel-ex) | conditional → [SEL-SHARP · 极限选择无正阶两点 Hölder](solution_selection.md#sel-sharp) | 完整模型、跨支 RL、真 EB、兼容与首次切换下界；**修订包内部审计** |

## 算子空间

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E17 | [D01 · 完整图、真残差与图剪切](foundations.md#d01) ∧ [LT · Luke–Tam 公共 all-pairs 证书](operator_space.md#lt) ∧ [D04 · 真实 EB 与 gauge](foundations.md#d04) ∧ [COV · 图块 coverage 与最近零点图](rleb_ppa.md#cov) | conditional → [OS-E · RLEB 能量证书](operator_space.md#os-e) | 同 S、同 coverage/留域；公共 all-pairs LT 归一化；**S20 内部证明** |
| E18 | [PHI · 紧 T-only 图卡的 proper Φ](operator_space.md#phi) | limits → [SIZE · 中立母空间中的规模比较](operator_space.md#size) | proper/quotient 不推出保纲；局部观测不恢复完整 F；**反例支持的缺口** |
| E19 | [LT · Luke–Tam 公共 all-pairs 证书](operator_space.md#lt) ∧ [OS-E · RLEB 能量证书](operator_space.md#os-e) ∧ [PHI · 紧 T-only 图卡的 proper Φ](operator_space.md#phi) | open → [SIZE · 中立母空间中的规模比较](operator_space.md#size) | 需中立完整对象、鉴别性量尺、保纲与反塌缩；**开放目标** |
| E33 | [PHI · 紧 T-only 图卡的 proper Φ](operator_space.md#phi) | limits → [CAT-GAP · proper/quotient 不保纲](operator_space.md#cat-gap) | proper 闭满射 x↦max(x,0) 的无处稠密集合逆像有内点；**S20 反例** |
| E34 | [PHI · 紧 T-only 图卡的 proper Φ](operator_space.md#phi) | limits → [LOCAL-LOSS · 局部观测不控制完整原图](operator_space.md#local-loss) | T_N 在 K 上同观测，域外 r=2 附近无一致紧性；**S20 反例** |
| E35 | [NO-GO · 旧 Baire/孔隙共同塌缩报告](operator_space.md#no-go) | limits → [SIZE · 中立母空间中的规模比较](operator_space.md#size) | N05/N08/N10 量尺共同塌缩；原孔隙审计未恢复；**S21 历史报告** |

## 锥

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E20 | [C-RANK · 冻结秩夹逼](cone_markov.md#c-rank) ∧ [C-FACE · 面稳定与共同流形](cone_markov.md#c-face) | conditional → [C-MSCQ · 原锥残差 MSCQ](cone_markov.md#c-mscq) | nice+冻结 CRSC+参考面 amenability+法向/切向修正；**证明包内部审计** |
| E36 | [C-RANK · 冻结秩夹逼](cone_markov.md#c-rank) | conditional → [C-FACE · 面稳定与共同流形](cone_markov.md#c-face) | nice、闭像及常秩核投影给面稳定；**锥证明包内部审计** |
| E37 | [C-FACE · 面稳定与共同流形](cone_markov.md#c-face) ∧ [C-NORMAL · 共同法向/切向修正](cone_markov.md#c-normal) ∧ [C-AMEN · 参考面 amenability](cone_markov.md#c-amen) | implies → [C-MSCQ · 原锥残差 MSCQ](cone_markov.md#c-mscq) | 法向流形修正与参考面切向误差界联合；**锥证明包内部审计** |
| E38 | [C-AMEN · 参考面 amenability](cone_markov.md#c-amen) ∧ [C-RANK · 冻结秩夹逼](cone_markov.md#c-rank) | conditional → [C-UNIV · 顶点系统普遍 MSCQ](cone_markov.md#c-univ) | 固定 proper nice 锥的每个顶点冻结 CRSC 系统；**锥证明包内部审计** |

## Markov

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E22 | [M-PSI · 同步 OT 残差 Ψ](cone_markov.md#m-psi) | conditional → [M-EXACT · exact-zero 与一般 gauge](cone_markov.md#m-exact) | 紧连续随机映射；exact-zero 等价一般 gauge；**证明包内部审计** |
| E23 | [M-PSI · 同步 OT 残差 Ψ](cone_markov.md#m-psi) ∧ [M-EXACT · exact-zero 与一般 gauge](cone_markov.md#m-exact) | conditional → [M-FIN · 有限状态顶点测试与线性 EB](cone_markov.md#m-fin) | 固定有限状态几何；有限 OT tight-edge 顶点；**证明包内部审计** |
| E42 | [M-COND · 守恒边缘条件残差](cone_markov.md#m-cond) ∧ [M-BINARY · bit 刷新 a*>0 判据](cone_markov.md#m-binary) | conditional → [COND-EB · 守恒边缘条件残差 EB](cone_markov.md#cond-eb) | 固定守恒边缘的 bit 刷新；a*>0 等价条件 EB 与统一速率，不是原 Ψ；**Markov 定理包** |
| E43 | [M-COND · 守恒边缘条件残差](cone_markov.md#m-cond) ∧ [M-GAUSS · Gaussian 谱隙 ζ](cone_markov.md#m-gauss) | conditional → [COND-EB · 守恒边缘条件残差 EB](cone_markov.md#cond-eb) | Gaussian Gibbs、Q>0、ζ>0，条件残差锐 EB 常数 ζ^-1/2；**Markov 定理包** |
| E45 | [M-RECOUP · 回耦损失控制](cone_markov.md#m-recoup) ∧ [M-PSI · 同步 OT 残差 Ψ](cone_markov.md#m-psi) | conditional → [M-EXACT · exact-zero 与一般 gauge](cone_markov.md#m-exact) | 只有趋近同一 Ψ inf 的耦合及损失界，收缩才可反推 EB；**Markov 条件桥** |

## 随机

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E29 | [STOCH · 期望距离收缩与路径 Dini 步长](holder_structure.md#stoch) ∧ [METRIC · 所指定度量完备](holder_structure.md#metric) | implies → [STOCH-LIMIT · 随机极限在闭 S 内](holder_structure.md#stoch-limit) | 给定度量完备、闭 S、不变域；期望收缩与 Dini；**9/19 修补版本** |

## 值域

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E46 | [H01 · 全局 RL 与固定参数 maximal](holder_structure.md#h01) ∧ [RHO · 最大根 ρ 与 h(r) 标量定位](range_finite_data.md#rho) | conditional → [W01 · 全纤维值域球](range_finite_data.md#w01) | 有限维 graph-maximal、非空完整逆纤维、r>R；**S23 稿内证明** |
| E47 | [W01 · 全纤维值域球](range_finite_data.md#w01) ∧ [REL-MAX · 相对 maximal 窗口](range_finite_data.md#rel-max) | conditional → [W02 · 固定窗口全纤维覆盖](range_finite_data.md#w02) | 同参数全局 completion、窗口球包含与目标窗口；**S23 稿内证明** |
| E48 | [RHO · 最大根 ρ 与 h(r) 标量定位](range_finite_data.md#rho) | limits → [W01 · 全纤维值域球](range_finite_data.md#w01) | 一维 C(p)=L(p_+)^γ 给 r>R 严格门和半径锐性；**S23 锐性反例** |

## 有限数据

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E49 | [QSAMPLE · 样本交叉兼容](range_finite_data.md#qsample) ∧ [LIFT · 二次 excess 与正交提升](holder_structure.md#lift) | implies → [QP · 严格凸 QP 与全局 N_m](range_finite_data.md#qp) | 同一固定样本的严格凸 QP，所有查询共用 N_m；**S23 稿内构造** |
| E50 | [QP · 严格凸 QP 与全局 N_m](range_finite_data.md#qp) ∧ [Q-COVER · Cayley 参数 δ-覆盖](range_finite_data.md#q-cover) ∧ [D02 · 全对 RL 与指定尺度](foundations.md#d02) | conditional → [Q-BOUND · 正反纤维配对 Kδ 界](range_finite_data.md#q-bound) | 未知每个图点的 Cayley 参数被 δ-覆盖；全纤维需全部点；**S23 稿内证明** |
| E51 | [Q-BOUND · 正反纤维配对 Kδ 界](range_finite_data.md#q-bound) ∧ [Q-EVAL · 已验证 gap、噪声与求值误差](range_finite_data.md#q-eval) | conditional → [Q-TOTAL · 覆盖 + 噪声 + 求值三项界](range_finite_data.md#q-total) | 真输出的全纤维覆盖、已认证 gap、噪声 η 和求值 e；**S23 稿内证明** |
| E53 | [DEADBAND · deadband 精确逆跳跃与稳定代理](range_finite_data.md#deadband) | refutes → [Q-ADVANTAGE · 影子代理普遍优于定制正则化](range_finite_data.md#q-advantage) | 稳定代理不必是精确逆；恒等代理已有同半径，不能宣称普遍优越；**S23 显式实例** |

## 随机近端

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E54 | [RP-OBJECT · 有限维不一致二次近端与守恒边缘](canonical/random_proximal.md#rp-object) | implies → [RP-GAP · 活跃空间严格均方谱隙](canonical/random_proximal.md#rp-gap) | 有限维 H、有限正权重、H_i 半正定、b_i 在像中、V=共同核正交补非零；谱间隙只在 V 上。；**本轮独立推导；未核外部优先权** |
| E55 | [RP-OBJECT · 有限维不一致二次近端与守恒边缘](canonical/random_proximal.md#rp-object) ∧ [RP-GAP · 活跃空间严格均方谱隙](canonical/random_proximal.md#rp-gap) | implies → [RP-CONTRACTION · 条件 Wasserstein 收缩与不变律分类](canonical/random_proximal.md#rp-contraction) | 同一独立新索引同步耦合；固定守恒边缘 ν 与有限二阶矩；不变律分类是所有联合 P2 律。；**本轮独立推导；未核外部优先权** |
| E56 | [RP-CONTRACTION · 条件 Wasserstein 收缩与不变律分类](canonical/random_proximal.md#rp-contraction) ∧ [RP-OBJECT · 有限维不一致二次近端与守恒边缘](canonical/random_proximal.md#rp-object) | implies → [RP-EB · 真实条件 law-step 线性误差界](canonical/random_proximal.md#rp-eb) | 同一固定 ν、条件运输距离、整个混合核的真实 law-step 残差；双边常数 1±c、有限长度；不能换普通物理步长。；**本轮独立推导；未核外部优先权** |
| E57 | [RP-BRANCH · 分支残差零集是共同固定点](canonical/random_proximal.md#rp-branch) ∧ [RP-CONTRACTION · 条件 Wasserstein 收缩与不变律分类](canonical/random_proximal.md#rp-contraction) | limits → [OB-RES · 条件残差不可代入同步 OT 能量](cone_markov.md#ob-res) | 分支 firmly nonexpansive 且各有固定点时，逐支推前残差零集是共同固定点支持律；混合不变律可存在而该残差严格正。；**本轮独立推导；未核外部优先权** |
| E58 | [RP-SCALAR · 标量尖锐性与正物理步长](canonical/random_proximal.md#rp-scalar) | sharpness → [RP-EB · 真实条件 law-step 线性误差界](canonical/random_proximal.md#rp-eb) | 在双分支标量子族，c=a 且一般 EB 上界系数 1/(1-c) 与相对收缩 c^k 同时取等；不声称每个固定矩阵模型最优。；**本轮独立推导；未核外部优先权** |

## 例库

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E59 | [EX-ROT · 纯旋转完整图与 resolvent](canonical/example_atlas.md#ex01) | refutes → [OB-STRONG · J 严格收缩必推出 F 强单调（错误）](canonical/example_atlas.md#ex01) | 全图 R²、每个 ω,λ>0，完整 J 的 Lip 严格小于 1，而 F 的单调内积恒为 0；无附加条件的逆推论错误。；**本轮独立推导；仅此例/族** |
| E60 | [EX-DIAG · 正紧对角无限维尾方向](canonical/example_atlas.md#ex02) | refutes → [OB-GAUGE · 严格单调+cocoercive 必有趋零 gauge EB（错误）](canonical/example_atlas.md#ex02) | H=ℓ² 的同一个 F；对每个趋零 ψ，不存在任意局部统一 C,δ；有限维截断不继承反例。；**本轮独立推导；仅此例/族** |
| E61 | [EX-CUBIC · 三次映射与完整 J](canonical/example_atlas.md#ex03) | implies → [EX-MODULI · 固定/移动目标与算法残差三种精确模](canonical/example_atlas.md#ex03) | F=x³ 的固定目标 q=1/3 模 1、两变量模 2^(2/3)、Gλ=I−JλF 局部模下确界 λ^(−1/3)；对象及取到性不同。；**本轮独立推导；仅此例/族** |

## 参数字典

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E62 | [D02 · 全对 RL 与指定尺度](foundations.md#d02) ∧ [PD-QUANTIFIERS · 全对/锚定、图块/全图、尺度/coverage](canonical/parameter_dictionary.md#pd-quantifiers) | equivalence → [PD-CAYLEY · Cayley 与成对能量等价式](canonical/parameter_dictionary.md#pd-cayley) | 同一图块、同一步长、每对指定图点；RL 与 C 在自然域的连续模及两条能量式精确等价，coverage 独立。；**本轮代数/反例独立重算；文献命名另核** |
| E63 | [PD-CAYLEY · Cayley 与成对能量等价式](canonical/parameter_dictionary.md#pd-cayley) ∧ [PD-QUANTIFIERS · 全对/锚定、图块/全图、尺度/coverage](canonical/parameter_dictionary.md#pd-quantifiers) | conditional → [PD-TIED · γ=1 tied 参数曲线含 L=0](canonical/parameter_dictionary.md#pd-tied) | γ=1，固定同一 λ、全部相同配对；θ∈(−1/2,1/2]，L=0 对应 θ=1/2；一般独立双参数不在此边结论。；**本轮代数/反例独立重算；文献命名另核** |
| E64 | [PD-CAYLEY · Cayley 与成对能量等价式](canonical/parameter_dictionary.md#pd-cayley) | conditional → [PD-STEP · 同图换步的单射与 coverage 门](canonical/parameter_dictionary.md#pd-step) | 同一图 Γ，η>0；新自然域 Q(D)，Cη 良定 iff Q 单射；Lipschitz 上界另要求旧 C 的 L 与 α−\|β\|L>0，coverage 另核。；**本轮代数/反例独立重算；文献命名另核** |
| E65 | [PD-SCALE · 有界降指数与无界反例](canonical/parameter_dictionary.md#pd-scale) | limits → [OB-SCALE · 无界域不能自由换 Hölder 指数](canonical/parameter_dictionary.md#pd-scale) | 同一有界 D 可高指数降低指数；C(s)=s 和 sign(s)\|s\|^γ 在无界 D 分别阻断反向/全局通用改指数。；**本轮代数/反例独立重算；文献命名另核** |
| E66 | [PD-RESIDUAL · 真残差与选中值的方向](canonical/parameter_dictionary.md#pd-residual) | refutes → [OB-SELECTED · 选中步残差不能倒推真 EB](canonical/parameter_dictionary.md#pd-residual) | r_F(u)≤‖v‖；非减 gauge 下真 EB→选中值界。F(u)={u,u²} 反驳选中值界→真 EB 的无条件逆推。；**本轮代数/反例独立重算；文献命名另核** |
| E67 | [PD-REGULARITY · MR/MSR 与 strong 的量词方向](canonical/parameter_dictionary.md#pd-regularity) | refutes → [OB-MR-MSR · MR 与 strong MSR 无条件互推（错误）](canonical/parameter_dictionary.md#pd-regularity) | MR 固定目标给 MSR；F(x)=\|x\| 和 F(x,y)=x 在原点分别反驳 strong MSR→MR 与 MR→strong MSR。；**本轮代数/反例独立重算；文献命名另核** |

## 路径图集

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E68 | [PA-DEF · 合法词与路径前缀](canonical/path_atlas.md#pa-def) ∧ [PA-COVER · 实际前缀延拓及留域覆盖](canonical/path_atlas.md#pa-whole) ∧ [PA-BUDGET · 统一终点与可求和位移](canonical/path_atlas.md#pa-whole) | implies → [PA-WHOLE · 每条实际轨道有限长收敛](canonical/path_atlas.md#pa-whole) | R^n、闭 S、开 V；每条合法选择；统一 Θ≤κt、H(t)<∞，初值 H(d0)<距边界。；**本轮重写证明；未核新颖性** |
| E69 | [PA-BLOCK · 块 RL 和实际输出 EB](canonical/path_atlas.md#pa-block) ∧ [PA-COVER · 实际前缀延拓及留域覆盖](canonical/path_atlas.md#pa-whole) ∧ [PA-BUDGET · 统一终点与可求和位移](canonical/path_atlas.md#pa-whole) | conditional → [PA-WHOLE · 每条实际轨道有限长收敛](canonical/path_atlas.md#pa-whole) | 同一个合法块的最近零点比较与实际输出 EB 给终点 ρ；另要 ρ≤κt、中间前缀界、延拓及位移预算。；**本轮代数与整轨道证明** |
| E70 | [PA-POWER · 合法词幂及统一量词](canonical/path_atlas.md#pa-power) ∧ [PA-DEF · 合法词与路径前缀](canonical/path_atlas.md#pa-def) | conditional → [PA-CONTRACT · 统一幂词终点收缩](canonical/path_atlas.md#pa-power) | 只获得统一终点收缩：有限词集全 A>1，或无限词集 inf A>1、sup C<∞；中间覆盖与位移求和仍需另证。；**本轮量词反例；未断言完整预算** |
| E71 | [PA-CYCLES · 独立的相位极限命题](canonical/path_atlas.md#pa-cycles) | limits → [PA-WHOLE · 每条实际轨道有限长收敛](canonical/path_atlas.md#pa-whole) | 非平凡周期有不消失块内位移，不满足 PA-WHOLE 的 H<∞；相位极限需独立连续性命题，Fix T^m 不等于 Fix T。；**本轮 T(x)=1−x 反例** |
| E77 | [M1-OBJECT · 显式 M1 映射、线段零集与端点球](topics/path_dynamics/m1_capture.md#m1-object) | conditional → [M1-CAPTURE · 每个球内初值两步捕获](topics/path_dynamics/m1_capture.md#m1-capture) | 仅给定单值 T，R=1/(96√10)，Z=[−2/3,2/3]×{0}；对 B_R((2/3,0)) 的每个初值两步进入 Z；不涵盖原生多值 Sign 方程的所有选择。；**本轮由显式映射独立重算；原生图桥未核** |
| E78 | [M1-OBJECT · 显式 M1 映射、线段零集与端点球](topics/path_dynamics/m1_capture.md#m1-object) | conditional → [M1-SHARP · 锐一步距离因子 3/√10](topics/path_dynamics/m1_capture.md#m1-sharp) | 同一 T、Z、R；全体球内初值的一步距离上界 3/√10，沿 z_t=(2/3+3t,t) 取等；不推出全对 RL 或真残差 EB。；**本轮代数与锐性序列独立重算** |
| E81 | [PS-OBJECT · 幂次剪切完整图与指定步长](topics/path_dynamics/power_shear.md#ps-object) | conditional → [PS-RATE · 法向 γq 精确可达与切向预算](topics/path_dynamics/power_shear.md#ps-rate) | λ=1、0<γ<1、q>1/γ、α=γq；完整 F=J^−1−I 的真 EB，单条轨道法向速率 r_+=r^α；反射全对 γ 只在有界输入窗口，留域另需切向余量。；**本轮反演、残差渐近与轨道预算独立重算；非普适速率** |
| E82 | [OS-OBJECT · 振荡剪切完整图与局部孤立零点](topics/path_dynamics/oscillatory_shear.md#os-object) | conditional → [OS-SCALING · 双边 q 阶与最大全对 γ 指数](topics/path_dynamics/oscillatory_shear.md#os-scaling) | λ=1、q>1、0<γ<1、β=q/γ−1；全域双边 J 范数，局部真残差 q-EB 与局部轨道 q 阶；反射最大全对 γ 只在有界窗口；归一化 Q 因子未证。；**本轮双边界、两尺度 Hölder 和相位锐性独立重算** |
| E83 | [DE-OBJECT · 指定 Minty 域振荡反射图](topics/path_dynamics/domain_escape.md#de-object) | conditional → [DE-ESCAPE · 真残差线性而非零轨道有限逃逸](topics/path_dynamics/domain_escape.md#de-escape) | 0<α<1、β>0、0<δ<1、λ=1、输入域 D=[−δ,δ]；每个非零初值半径严格增且有限步出 D，真残差局部线性；锚定 α 和全对 α/(β+1) 不给不变域。；**本轮两尺度、有限逃逸及全原像残差一致性独立重算** |
| E86 | [DC-OBJECT · GX-074 紧离散图与零集](topics/path_dynamics/discrete_coverage.md#dc-object) | conditional → [DC-GAP · 全对 RL 加真 EB 不给输入覆盖](topics/path_dynamics/discrete_coverage.md#dc-gap) | H=R、K={0}∪{1/n}、gph F=K×{0}、S=K；每个 0<γ≤1 的完整图全对 RL(λ,γ,1) 及图输出真 EB 同时成立，自然输入域仍只有 K。；**本轮完整纤维和量词直接计算** |

## 复合次正则

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E72 | [CS-OBJECT · 复合真残差与目标集合](canonical/composite_subregularity.md#cs-object) | conditional → [CS-TRANSFER · 弱分离下目标集合一致](canonical/composite_subregularity.md#cs-transfer) | 有限连续 f、局部最小、驻点弱分离、S⊆Γ 且包含所有局部极小点；x∈B_{R/4}。；**本轮独立重算** |
| E73 | [CS-OBJECT · 复合真残差与目标集合](canonical/composite_subregularity.md#cs-object) | conditional → [CS-EB · 满行秩复合 gauge EB](canonical/composite_subregularity.md#cs-eb) | c∈C^{1,1}、Dc 满行秩且 βR<σ0、φ 有限凸、c(x̄)∈C、外层真实 EB；目标 S=c^{-1}(C)；x∈B_r。；**本轮修复、链式、残差三门重算** |
| E74 | [CS-EB · 满行秩复合 gauge EB](canonical/composite_subregularity.md#cs-eb) ∧ [CS-OBJECT · 复合真残差与目标集合](canonical/composite_subregularity.md#cs-object) | conditional → [CS-PROX · 局部 RL、coverage、轨道预算](canonical/composite_subregularity.md#cs-prox) | 另需全部外层次梯度界 M、λβM<1；仅局部输出。轨道再需 Ψ_F(bd)≤κd、最近零点同图块和初值留域预算。；**本轮完整局部证明；不升为完整 J_F** |
| E75 | [CS-MODEL · 曲面幂和非幂锐例](canonical/composite_subregularity.md#cs-model) | refutes → [CS-POWER-GENERAL · 所有满秩复合都有超线性幂 EB 的过强命题](canonical/composite_subregularity.md#cs-model) | 同一个满秩曲面 c=t−(s_+)²，η=u log(e/u) 有非幂趋零 gauge，却对任意固定 q>1 无 q 次幂 EB；只否定普遍幂次升级。；**本轮直接计算** |
| E76 | [CS-RANK-EX · 秩亏同阶传递反例](canonical/composite_subregularity.md#cs-objections) | limits → [CS-OPEN-RANK · 秩亏原生 verifier 开放目标](canonical/composite_subregularity.md#cs-objections) | c=x²、φ=z²/2 保留外层线性 EB，却不保复合线性 EB；秩亏开放目标必须加入真实残差乘子桥。；**本轮显式反例** |
| E79 | [CI-OBJECT · 曲面尖点外层与真多值次梯度](topics/composite_regular/cusp_identification.md#ci-object) ∧ [CS-PROX · 局部 RL、coverage、轨道预算](canonical/composite_subregularity.md#cs-prox) | conditional → [CI-IDENTIFY · 局部近端一步识别非孤立零集](topics/composite_regular/cusp_identification.md#ci-identify) | 曲面 c=t−(s_+)²、ν>0、η 连续严格增无界；0<R<1/2、M=ν+η(R+R²)、h=2M、λh<1，x∈B_{r/2} 且 d(x,S)<λν(1−λh)，r=R(1−2R)/4；仅唯一球内近端输出。；**本轮从真残差间隙和局部步长界独立重算** |
| E80 | [OT-MAXIMA · 驻点极大序列及二阶目标障碍](topics/composite_regular/oscillating_target.md#ot-maxima) | refutes → [OB-TARGET · 局部最小自动保证二阶目标 EB 的错误猜测](topics/composite_regular/oscillating_target.md#ot-scope) | C∞ 非负 f 在 0 严格全局最小，却有 x_k→0 的 f′=0、f″<0；仅否定不加目标一致/弱分离时到完整 Θ₂ 的全邻域 Ψ(0)=0 EB。；**本轮区间变号和目标距离独立证明** |

## 孤立零点

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E84 | [IZ-GERM · 孤立零点图 germ 的 B/J/R 平坦性](canonical/isolated_zero_flatness.md#iz-germ) ∧ [IZ-FIBERS · 真实 EB 到实际图值的方向](canonical/isolated_zero_flatness.md#iz-fibers) | conditional → [IZ-PPA · 指定分支超线性上阶](canonical/isolated_zero_flatness.md#iz-ppa) | 同一孤立 p、q>1、λ>0；IZ-FIBERS 仅用真 EB→实际图值方向，不需反向的 residual-complete；另需指定 T 在输入邻域全域选择、实际输出真 q-EB、步残差 <η、ρη^(q−1)≤λ/2 和闭球留域；只给上阶。；**本轮逐图点及球不变证明** |
| E85 | [IZ-PPA · 指定分支超线性上阶](canonical/isolated_zero_flatness.md#iz-ppa) | conditional → [IZ-FACTOR · 正 Q 因子的归一化门](canonical/isolated_zero_flatness.md#iz-factor) | 同一非终止轨道；另需 \|\|x^(k+1)−p\|\|/\|\|w_k\|\|^q→μ∈(0,∞)；结论 Q 因子 μ/λ^q；上阶不自动给极限。；**本轮三角双边界重算** |

## 不蕴含关系

- 局部单值 J_G 不推出完整 J_F 单值；见 [解选择反例](solution_selection.md)。
- 固定紧源 Φ proper 不推出保纲，也不恢复域外原图；见 [算子空间](operator_space.md)。
- 任意紧零集可在全局 RL 实现，不保证局部 EB、Dini、coverage 与回缩；见 [结构与拓扑](holder_structure.md)。
- 有限样本不验证指定 T 在整窗的 usc/acyclicity；见 [局部值域](holder_structure.md)。
- 锥 MSCQ、条件 Markov 残差与确定性 RLEB 属于不同对象；见 [额外桥](cone_markov.md)。
