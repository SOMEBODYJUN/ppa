# 数学关系超边图

本图从 [graph.json](graph.json) 生成；运行 python3 research/build_graph.py 同时生成本页和 [交互 HTML](map.html)。每条边的输入是**合取**；范围、版本及证据状态不可省。节点链接进入重构的数学模块，原始证据见 [SOURCES.md](SOURCES.md)。

关系 conditional 带有额外前提，open 是目标而非证明，limits 是反例或边界；necessary 和 sufficient 分别对应纤维分类的两个方向；sharpness 只给声明范围内的下界见证。

## 定义

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E01 | [D01 · 完整图、真残差与图剪切](foundations.md#d01) ∧ [D02 · 全对 RL 与指定尺度](foundations.md#d02) | equivalence → [D03 · Cayley 表示](foundations.md#d03) | 同图块、同 λ、同输入对尺度；**代数可复核** |
| E101 | [PD-CAYLEY · Cayley 与成对能量等价式](canonical/parameter_dictionary.md#pd-cayley) | conditional → [CG-CLOSURE · 闭图当且仅当 Minty 自然域闭](canonical/closed_graph_minty_domain.md#cg-closure) | 同一非空 G⊂H×H，H 完备，固定 λ>0；每对输入差<R 的图点满足 ω(0)=0 且 ω(t)→0 的全对模。剪切图的闭包是延拓 Cayley 的 pullback；G 闭 iff M_+(G) 闭。；**C58 近对角线模与闭包独立证明；正尺度跳跃模不自动延续原常数** |
| E102 | [CG-CLOSURE · 闭图当且仅当 Minty 自然域闭](canonical/closed_graph_minty_domain.md#cg-closure) | conditional → [CG-COVERAGE · 闭图与稠密输入域合取给满覆盖](canonical/closed_graph_minty_domain.md#cg-closure) | 同一图块另证 G 闭且 D=M_+(G) 在整个 H 稠密，才由 D 闭推出 D=H。单独闭图无 coverage；图块结论不排除完整图其他输出。；**C58 直接推论；边界取闭 G=[0,1]×{0}，见 F16** |
| E103 | [PD-RESIDUAL · 真残差与选中值的方向](canonical/parameter_dictionary.md#pd-residual) ∧ [RW-OBJECT · 真残差窗口与可评价邻域量词](canonical/residual_window_bridge.md#rw-object) | conditional → [RW-POSITIVE · 正阈值一般 gauge 的缩邻域桥](canonical/residual_window_bridge.md#rw-positive) | 同一完整 F 和 S=F^-1(0)∋ubar；有限非减 ψ:[0,η) 且窗口 EB 对全部 r_F(u)<δ 成立；另需 0<δ<η 与 ψ(δ)>0。V=U∩B(ubar,ψ(δ)) 上对所有 r_F(u)<η 得同一 EB；定义域外不得擅用 ψ。；**C59 正阈值直接证明；正幂是特例，条件只充分** |

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
| E94 | [MA-LIMIT · 固定锚与集合收缩的反例边界](canonical/moving_anchor_reflection.md#ma-limit) | limits → [MA-REFLECT · 移动零点锚的渐近反射比](canonical/moving_anchor_reflection.md#ma-reflect) | S=R×{0}、y=(1,0)、w_n=(1/n,1/n)、p_n=y；移动锚缺陷零，但固定 p0=0 相对缺陷→2，且两侧到 S 距离相等。不可升级为固定锚或集合收缩。；**本轮完整图值与距离直接计算** |
| E97 | [NB-OSC · 振荡分支的锚定/全对分离](canonical/named_branch_local.md#nb-oscillation) | refutes → [OB-NB-ALL · 锚定收缩必有全对线性 RL（错误）](canonical/named_branch_local.md#nb-oscillation) | 完整 R 上 λ=1、T(x)=x[3/10+sin(x^-2)/10]；锚 γ=1,L=3/5、真 EB 2/3、实际距离至多 2/5，却无任意零邻域全对线性 RL；只阻断锚定→同指数全对升级。；**新构造，全部原像残差下界与 Cayley 导数独立计算** |
| E100 | [AV-GAP · 完整多值零集未被图块零锚覆盖](canonical/all_pairs_verifier.md#av-gap) | refutes → [OB-AV-ANCHOR · 全对图块加 coverage 自动给完整零集锚（错误）](canonical/all_pairs_verifier.md#av-gap) | 完整 F(y)={0,y}、图块 G={(y,y)} 在 R 上全对 L=0 且满 coverage；S=R,S_G={0}，非零输入 d(x,S)=0 而 Tx=x/2。缺的是零锚保距离，完整排他也独立失败。；**新反例，全部完整纤维与两种零集直接核算** |
| E104 | [RW-FLAT · 闭图扁平 gauge 的窗口反例](canonical/residual_window_bridge.md#rw-flat) | refutes → [OB-RW-NEIGH · 一般窗口 EB 自动成为邻域 EB（错误）](canonical/residual_window_bridge.md#rw-flat) | 完整闭图 F(0)={0,1},F(u)={1} (u≠0)，S={0}、ψ(t)=max(t−2,0)、δ=1/2；窗口只检验零点，但任意邻域有 r_F=1 且 ψ(1)=0<\|u\|。不附加全对 RL。；**C59 边界反例，完整图与全部纤维直接计算** |
| E107 | [DR-TAN · GX-069 切触 DR 的半阶真残差](topics/examples/dr_tangency_transversality.md#dr-tangent) | refutes → [OB-DR-STRICT · 半阶 EB 自动给统一一步严格距离收缩（错误）](topics/examples/dr_tangency_transversality.md#dr-tangent) | z_s=(s,−s²)→0 时 d(Tz_s,S)=d(z_s,S)>0；虽有全邻域半阶 EB，任何统一 ρ<1 的一步距离比均失败。；**C60 精确取等序列** |
| E121 | [SME-POWER · 幂次最坏矩与同变量复合](topics/random_markov/scalar_moment_envelope.md#sme-power) | refutes → [OB-AGGREGATE · 分开矩聚合的临界失相关障碍](../FAILED_ROUTES.md#f24) | 0<γ<1、q>1、γq=1、0<t<R：分开最坏包络与先复合的最坏上界比 (R/t)^(1−γ)；各自锐的极值分布未必相同。并非证明任何物理随机轨道发散。；**F24 的定量失相关见证** |
| E122 | [SME-OBJECT · 硬支持下所有概率律的矩提升对象](topics/random_markov/scalar_moment_envelope.md#sme-object) | conditional → [SME-SUPPORT · 小矩距离不提供逐点支撑](topics/random_markov/scalar_moment_envelope.md#sme-support) | 对全部 0≤D≤R 且 \|\|D\|\|p≤ε 的变量，线性矩界 iff 整个 [0,R] 的逐点线性界；稀薄 R 幅度可落在任意小矩球内。局部 gauge 需另加真实支撑或尾部门。；**C69 稀薄二点律的必要性** |

## 局部拓扑

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E13 | [FSC-COLLAR · 有限包络与整窗条件给内域余量](canonical/finite_sample_collar.md#fsc-collar) ∧ [WINDOW · 整窗 usc、acyclic 与上同调条件](holder_structure.md#window) | conditional → [H07 · 原关系局部值域候选](holder_structure.md#h07) | 指定 T 整窗非空紧 usc、Čech-Q-acyclic，有限多面体 A⊂int B、χ(A)≠0、上同调满射和 rational Lefschetz；FSC-COLLAR 只闭合度量内域余量，不能单独给 coincidence；T 可为子关系；**S25 候选；一手 Lefschetz 引文适用门已核，整窗 T 假设独立** |

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
| E108 | [FP-OBJECT · 同一目标的全局 prox 与指定选择核](topics/random_markov/proximal_selection_seam.md#ps-objects) | conditional → [FP-ABSORB · 固定目标平稳律的吸收支持](topics/random_markov/proximal_selection_seam.md#ps-absorption) | 同一个 proper Borel f 的全局 proximal 最小解、每个域内输入有非空解且 K 只选该集合；对每个支撑于 dom f 的平稳概率律 π，πK=π iff π(A_K)=1。无需 ∫\|f\|，不适用于完整非凸次梯度 resolvent 或随机换目标。；**C62 有界 arctan 严格下降证明** |
| E109 | [FP-SEAM · 非乘积 prox 的闭图与核接缝](topics/random_markov/proximal_selection_seam.md#ps-example) ∧ [FP-ABSORB · 固定目标平稳律的吸收支持](topics/random_markov/proximal_selection_seam.md#ps-absorption) | conditional → [FP-NOEB · 完整 W2 邻域的 law-step gauge 障碍](topics/random_markov/proximal_selection_seam.md#ps-no-eb) | 固定二维非乘积 group-ℓ0、λ=1 与 fair tie 核；唯一不变律 δ0，μk=(1−ε)δ0+εδakv 在任意给定完整 W2 邻域中可取固定 ε>0，真实 law-step→0 而到不变律距离→√(2ε)>0。非 Feller 接缝与闭 prox 图并存。；**C63 全图、全部平稳点与显式最优运输重算；V10 仅有限代数** |

## 例库

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E59 | [EX-ROT · 纯旋转完整图与 resolvent](canonical/example_atlas.md#ex01) | refutes → [OB-STRONG · J 严格收缩必推出 F 强单调（错误）](canonical/example_atlas.md#ex01) | 全图 R²、每个 ω,λ>0，完整 J 的 Lip 严格小于 1，而 F 的单调内积恒为 0；无附加条件的逆推论错误。；**本轮独立推导；仅此例/族** |
| E60 | [EX-DIAG · 正紧对角无限维尾方向](canonical/example_atlas.md#ex02) | refutes → [OB-GAUGE · 严格单调+cocoercive 必有趋零 gauge EB（错误）](canonical/example_atlas.md#ex02) | H=ℓ² 的同一个 F；对每个趋零 ψ，不存在任意局部统一 C,δ；有限维截断不继承反例。；**本轮独立推导；仅此例/族** |
| E61 | [EX-CUBIC · 三次映射与完整 J](canonical/example_atlas.md#ex03) | implies → [EX-MODULI · 固定/移动目标与算法残差三种精确模](canonical/example_atlas.md#ex03) | F=x³ 的固定目标 q=1/3 模 1、两变量模 2^(2/3)、Gλ=I−JλF 局部模下确界 λ^(−1/3)；对象及取到性不同。；**本轮独立推导；仅此例/族** |
| E105 | [DR-OBJECT · DR 算法残差及两种集合几何](topics/examples/dr_tangency_transversality.md#dr-objects) | conditional → [DR-TAN · GX-069 切触 DR 的半阶真残差](topics/examples/dr_tangency_transversality.md#dr-tangent) | C=横轴、D=抛物线、G=I-T，投影管 U={b>−1/2}；对全部零附近输入的真算法残差给最优半阶模 1，不把法锥和 N_C+N_D 当 G。；**C60 完整投影参数与取等序列重算** |
| E106 | [DR-OBJECT · DR 算法残差及两种集合几何](topics/examples/dr_tangency_transversality.md#dr-objects) | conditional → [DR-TRANS · GX-070 横截 DR 的精确线性模](topics/examples/dr_tangency_transversality.md#dr-transverse) | 改为夹角 θ∈(0,π/2) 的两条横截线、同一 DR 公式；G=I−cosθ Qθ，全域 MR/MSR 精确模 1/sinθ，实际 T 轨道因子 cosθ；是另一对象。；**C61 反射与奇异值恒等式重算** |
| E115 | [IS-OBJECT · 身份与平方并图的完整关系](topics/examples/identity_square_branch_union.md#is-object) | conditional → [IS-OP · 原算子真残差锐半阶](topics/examples/identity_square_branch_union.md#is-operator-eb) | F(x)={x,x²} 完整图，S={0}；0<\|x\|<1 时真 r_F=x²，最优半阶模 1；最近逆点量词不能替代全部局部逆像。；**C66 完整纤维计算** |
| E116 | [IS-OBJECT · 身份与平方并图的完整关系](topics/examples/identity_square_branch_union.md#is-object) | conditional → [IS-STEP · 指定分支与完整最小步残差分离](topics/examples/identity_square_branch_union.md#is-resolvent) | 固定 λ>0，完整 J 包括身份根、近平方根与远平方根；指定 J₁ 线性步模 (1+λ)/λ，完整 inf 步模 1/√λ 的局部半阶；远根不得删。；**C67 完整方程和三根渐近** |
| E117 | [IS-OBJECT · 身份与平方并图的完整关系](topics/examples/identity_square_branch_union.md#is-object) | conditional → [IS-RL · 同输入跨支碰撞](topics/examples/identity_square_branch_union.md#is-collision) | 任意固定 λ>0、任意零邻域内两支图点可有相同 Minty 输入而不同 Cayley 输出；故包含两支的局部完整图无任意正指数全对 RL。；**C68 同输入碰撞** |

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

## 非孤立对齐

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E88 | [NA-OBJECT · 非孤立零集的输入与输出最近点家族](canonical/nonisolated_alignment.md#na-object) | conditional → [NA-DRIFT · 输出锚与最近点漂移包络](canonical/nonisolated_alignment.md#na-drift) | 指定同一 J、S，整个 0<d(x,S)≤r0 家族的 P_S(x) 与 P_S(Jx) 非空；集合间 infimum 可不取到；逐点 r≤a≤r+δ≤3a。；**本轮近似点对三角证明** |
| E89 | [NA-DRIFT · 输出锚与最近点漂移包络](canonical/nonisolated_alignment.md#na-drift) ∧ [D04 · 真实 EB 与 gauge](foundations.md#d04) | conditional → [NA-COMPOSE · 真 EB 和锚模的条件合成](canonical/nonisolated_alignment.md#na-compose) | 同一指定步、全家族实际输出的真 EB、ψ=o(id) 非减、全部 attained t 上 ψ(t)≤λt/2、gauge 参数在定义域；包络另需 A(r)≤Kr^θ。只给上指数。；**本轮 |a−λt|≤s 逐点重算** |
| E90 | [D04 · 真实 EB 与 gauge](foundations.md#d04) | conditional → [NA-APPROX · 无最近点时的正容差近似锚](canonical/nonisolated_alignment.md#na-approx) | 不需 proximinality；对同一实际输出的 t>0 取 e(t)>0，ψ(t)+e(t)≤κλt、κ<1 和 a_e/((1−κ)λ)<ηψ；只替换最近点存在性，不给输入 coverage。；**本轮近似锚 infimum 证明** |
| E91 | [NA-DRIFT · 输出锚与最近点漂移包络](canonical/nonisolated_alignment.md#na-drift) ∧ [NA-COMPOSE · 真 EB 和锚模的条件合成](canonical/nonisolated_alignment.md#na-compose) | conditional → [NA-SHARP · 同序列 θq 饱和门](canonical/nonisolated_alignment.md#na-sharp) | 上指数 θq 的下界需同一 x_n 的 a_n/r_n^θ→A>0、t_n/a_n→B>0、s_n/t_n^q→C>0；归一化极限 CB^qA^q；超线性 EB 还强制 B=1/λ。；**本轮同序列乘积与步长渐近** |

## 移动锚

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E92 | [MA-OBJECT · 图点真 EB 与逐点输出近锚](canonical/moving_anchor_reflection.md#ma-object) | conditional → [MA-REFLECT · 移动零点锚的渐近反射比](canonical/moving_anchor_reflection.md#ma-reflect) | 同一 (y,w)∈gph F、t=\|\|w\|\|>0、真 EB ψ=o(id)、p 为输出近锚且 e=o(id)、δ=(ψ(t)+e(t))/(λt)<1；双边反射比及缺陷界仅关于这个 p。；**本轮三角双边界独立重算** |
| E93 | [MA-OBJECT · 图点真 EB 与逐点输出近锚](canonical/moving_anchor_reflection.md#ma-object) ∧ [MA-REFLECT · 移动零点锚的渐近反射比](canonical/moving_anchor_reflection.md#ma-reflect) | conditional → [MA-POWER · 幂型近锚反射缺陷常数](canonical/moving_anchor_reflection.md#ma-power) | 同一逐点 p；另需 q>1、真 ρt^q EB、近锚误差 ct^q 及 (ρ+c)t^(q−1)/λ≤1/2；充分缺陷系数 2^(q+1)(ρ+c)/λ^q。；**本轮逐点幂界；常数未证最优** |

## 指定分支

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E95 | [NB-OBJECT · 指定分支、近似锚与实际输出真 EB](canonical/named_branch_local.md#nb-object) | conditional → [NB-LOCAL · Hilbert 指定轨道有限长度与局部闭零集](canonical/named_branch_local.md#nb-local) | 实 Hilbert；同一 T 在开球 U 覆盖，A 对所有 d(x,S)≤δ（含 d=0）给近似最近零点锚，E 对每个实际 Tx 给真残差窗口 EB；另需 limsup Φ(t)/t<1 与初值严格留域预算。只得指定轨道、U 内闭 S，不得升级完整 J_F 任意选择。；**§4 重算逐步界、Hilbert 完备性与零距离输入** |
| E96 | [NB-LOCAL · Hilbert 指定轨道有限长度与局部闭零集](canonical/named_branch_local.md#nb-local) | conditional → [NB-POWER · 幂次充分门与退化端点](canonical/named_branch_local.md#nb-power) | 同一 B/A/E、ψ(t)=ρt^q 且窗口门保持；γ<1,L>0 使用 p=γq；γ=1 使用 q；L=0 使用 q，不受 γ 影响。p>1 或临界系数<1 是充分门，另需留域；只给 upper order。；**§5 重新分解三类端点，未声称必要或正 Q 因子** |
| E98 | [AV-OBJECT · 全对图块、输入覆盖与零锚保距离](canonical/all_pairs_verifier.md#av-object) | conditional → [AV-BRIDGE · 全对验证器给指定锚与双输入模](canonical/all_pairs_verifier.md#av-bridge) | 实 Hilbert、同一 G⊂gph F 的所有图点对 RL(λ,L,γ)、U⊂M_+(G)，且 active set A 每个 x 有 d(x,S_G)=d(x,S)<∞；由图块单射与近似零锚得指定分支 A 及 U 上反射模。；**旧 §3.1 逐图点重算；EB 与轨道尚未提供** |
| E99 | [AV-BRIDGE · 全对验证器给指定锚与双输入模](canonical/all_pairs_verifier.md#av-bridge) ∧ [D04 · 真实 EB 与 gauge](foundations.md#d04) | conditional → [NB-LOCAL · Hilbert 指定轨道有限长度与局部闭零集](canonical/named_branch_local.md#nb-local) | 取 U 开球、A=Aδ 含零距离输入；另对每个实际 Tx 核真残差窗口 E、同一 ψ 的 h(δ)<η 与 limsup Φ/r<1，并给每个初值严格留域。只得指定轨道；完整 J_F 任意选择须另证排他。；**C56 的 B/A 接口加 C53 独立 E/兼容/留域；不把定义 D04 当成已验输出 EB** |

## 路径动力学

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E110 | [SL-INCLUSION · 新 Sign 包含与全纤维图](topics/path_dynamics/m1_sign_lift.md#sl-inclusion) | implies → [SL-RESOLVENT · 新完整图的 J 等于 M1 显式 T](topics/path_dynamics/m1_sign_lift.md#sl-graph) | 新定义 F_lift(u,0) 的全部 (h,q) 由 u+h−3q∈(2/3)Sign(h)+(2/3)h³ 给出，轴外为空；λ=1，Sign(0)=[−1,1]。对每个 z∈R² 唯一 h=f(p−3q)，完整 J_Flift(z)={Tz}，自然 Minty 域全平面；绝不认证历史原生循环方程。；**C64 全分支与端点独立反演** |
| E111 | [SL-INCLUSION · 新 Sign 包含与全纤维图](topics/path_dynamics/m1_sign_lift.md#sl-inclusion) | conditional → [SL-RESIDUAL · 新图端点的锐线性真残差](topics/path_dynamics/m1_sign_lift.md#sl-zero-residual) | 同一新图的全部残差纤维在端点给 r_F(c+δ,0)=δ/3、d((c+δ,0),zer F)=δ (0<δ<1)；线性 EB 常数 3 锐利，和 C38/C39 的动力证明逻辑独立。；**C64 按 h 正/零/负分支求 infimum** |
| E112 | [SL-RESOLVENT · 新完整图的 J 等于 M1 显式 T](topics/path_dynamics/m1_sign_lift.md#sl-graph) ∧ [M1-CAPTURE · 每个球内初值两步捕获](topics/path_dynamics/m1_capture.md#m1-capture) ∧ [M1-SHARP · 锐一步距离因子 3/√10](topics/path_dynamics/m1_capture.md#m1-sharp) | conditional → [SL-DYNAMICS · 新图完整 resolvent 的显式捕获与锐一步界](topics/path_dynamics/m1_sign_lift.md#sl-status) | 仅对新 F_lift 的完整 resolvent J=T，C38 两步捕获与 C39 一步锐因子各自已对这个显式映射证明，合取后可用于这个新完整 J；本边不把历史原生循环算法认作 F_lift。；**调用关系，非新证明** |
| E118 | [SL-RESOLVENT · 新完整图的 J 等于 M1 显式 T](topics/path_dynamics/m1_sign_lift.md#sl-graph) | conditional → [SL-RL · 新 Sign 完整图的端点局部最大全对指数](topics/path_dynamics/m1_sign_lift.md#sl-rl) | 仅新 F_lift、λ=1、U=Bρ((2/3,0)) 且 ρ<min(1/2,c/(2√10))；每对完整图点的 Minty 输入在 U 时有 γ=1/3 常数 Lρ；端点正向序列排除 γ>1/3。不能认证旧循环图或无界全域。；**C65 立方根界与端点锐性** |

## Hilbert 扩张

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E113 | [HE-SNOW · Hilbert γ 雪花的条件负定核](canonical/holder_extension.md#he-snowflake) ∧ [LIT-ALM · Hilbert 间同常数 Kirszbraun 正式 Theorem 1.2](LITERATURE.md#lit-alm-2021) | conditional → [HE-EXT · 同常数 Hölder 扩张与固定参数图完成](canonical/holder_extension.md#he-extension) | 任意非空 D⊂H、0<γ<1、同一 L≥0 的全对 Hölder 映射；雪花等距入 Hilbert 后以正式 Theorem 1.2 同常数扩张，回拉到 H；不保持额外像集或单调性。；**H01 的扩张步骤重新证明及一手前提核对** |
| E114 | [D02 · 全对 RL 与指定尺度](foundations.md#d02) ∧ [D03 · Cayley 表示](foundations.md#d03) ∧ [HE-EXT · 同常数 Hölder 扩张与固定参数图完成](canonical/holder_extension.md#he-extension) | conditional → [H01 · 全局 RL 与固定参数 maximal](holder_structure.md#h01) | 只针对完整非空全图、固定 λ,L,γ 的 RL 类；同参数 graph-maximal iff Minty 输入域 H。图块局部模不获全域扩张；不是 maximal monotone。；**H01 中 maximal 子命题，不升级结构稿其他候选** |

## 随机矩

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E119 | [SME-OBJECT · 硬支持下所有概率律的矩提升对象](topics/random_markov/scalar_moment_envelope.md#sme-object) | conditional → [SME-ENV · 连续 gauge 的最小凹上包络](topics/random_markov/scalar_moment_envelope.md#sme-envelope) | 1≤p<∞、R>0、连续非减 φ(0)=0、对所有概率律且实际 D≤R；最坏矩 p 次方等于 (cav g)(t^p)，g(z)=φ(z^(1/p))^p，至多二点幅度取等。；**C69 紧均值集与凹包络证明** |
| E120 | [SME-ENV · 连续 gauge 的最小凹上包络](topics/random_markov/scalar_moment_envelope.md#sme-envelope) | conditional → [SME-POWER · 幂次最坏矩与同变量复合](topics/random_markov/scalar_moment_envelope.md#sme-power) | 幂 φ(u)=Au^α 特化：α≤1 为 At^α，α≥1 为 AR^(α−1)t；同一个 D 上逐点 S≤CD^γ、D+≤KS^q 先复合再取矩，必须同一合法耦合及支撑。；**C69 幂次与同变量复合** |

## 局部值域的分析层

| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |
| --- | --- | --- | --- |
| E123 | [SAMPLE · 有限 proximal 样本与包络](holder_structure.md#sample) | conditional → [FSC-ENV · 经验证样本的全空间距离双包络](canonical/finite_sample_collar.md#fsc-envelope) | 非空有限样本每对实际输出分别独立验证步界和输出零距界；φ严格增；对整个 R^n 得 g_E≤d(·,S)≤u_E，不证明整窗 T；**C70-v1a 独立重算 (8.3)** |
| E124 | [FSC-ENV · 经验证样本的全空间距离双包络](canonical/finite_sample_collar.md#fsc-envelope) ∧ [FSC-FULL · 指定 T 的整窗每个输出满足步界与误差界](canonical/finite_sample_collar.md#fsc-object) | conditional → [FSC-COLLAR · 有限包络与整窗条件给内域余量](canonical/finite_sample_collar.md#fsc-collar) | 另加 A⊂int B 紧、sup_A u_E≤u、inf_{B\int A}g_E≥m>0、φ(u)<d(A,B^c)、α=cφ(u)^q<m；所有 p∈A 和 y∈T(p) 留在 int A 且 d(y,A^c)≥m−α；**C70-v1b 独立重算 (8.4)→(8.7)；未证拓扑 coincidence** |

## 不蕴含关系

- 局部单值 J_G 不推出完整 J_F 单值；见 [解选择反例](solution_selection.md)。
- 固定紧源 Φ proper 不推出保纲，也不恢复域外原图；见 [算子空间](operator_space.md)。
- 任意紧零集可在全局 RL 实现，不保证局部 EB、Dini、coverage 与回缩；见 [结构与拓扑](holder_structure.md)。
- 有限样本不验证指定 T 在整窗的 usc/acyclicity；见 [局部值域](holder_structure.md)。
- 锥 MSCQ、条件 Markov 残差与确定性 RLEB 属于不同对象；见 [额外桥](cone_markov.md)。
