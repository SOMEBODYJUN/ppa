# Research State · 2026-10-01

<a id="active-frontier"></a>
## 现在从哪里继续

| 优先 | 精确待办与输入 | 达成标准 / 真实阻塞 |
| --- | --- | --- |
| 总体规模比较 | [operator_space](research/operator_space.md#size) 的完整原图、真残差与统一测试域上，冻结计数对象 \(F\) 或 \((F,\lambda)\)、三类成员谓词和一项大小不变量；先用同页的 proper 不保纲、局部观测丢远端图反例攻击 | 目前**没有**冻结的共同母空间与量尺，不能声称总体规模定理；I-097–099/I-102 原证明仍缺件，旧 N10 只作待恢复的来源报告 |
| 局部值域模型 | [C05-v2 条件证明](research/canonical/local_range_without_supercriticality.md#lr-theorem) 与 [C70 度量链](research/canonical/finite_sample_collar.md) 已重算；下一步给一个目标原生模型逐输出认证整窗 \(T\) 的近端包含、两项估计、非空紧 usc/acyclic 与同一 collar | 有限样本只证包络，不能提供整窗的拓扑/全称门；9/25 原稿 [C05-v1](research/holder_structure.md#h07) 仍保留其 \(q\gamma>1\) 候选身份，外部文献适用门已核 |
| 清洗未裁决来源 | 按 [逐单元表](research/audit/UNIT_DISPOSITIONS.tsv) 选可独立复算的小节；先区分同一对象的不同观察与重复文件 | 目前仅 52 个来源数学单元有逐项去向；251 原件和 178 ZIP 成员的哈希清点不是验收。无法从单元数/文件数算覆盖率 |

以下为**按时间形成的研究日志**。其中“下一步”“本轮”只表示当时 checkpoint 的判断；当前优先级以上表和文末活跃目标的精确义务为准。

## 本批增量：条件值域的新版本与 GX-075

[新版本 C05-v2](research/canonical/local_range_without_supercriticality.md#lr-theorem) 在保留 C05-v1 全部整窗、collar 和拓扑合取前提下，仅将 qγ>1 改为 q>0；Vietoris–Begle、上同调注入、紧 morphism Lefschetz 与扰动同伦已独立逐步检查。一个 qγ=1/2 的有理网格实例验证此放宽非空。原稿 v1 仍是原稿事实；现实原生模型能否给这些全称前提、优先权及其它拓扑候选依然未闭。

[GX-075 / C72–C75](research/topics/examples/diagonal_spike_relation.md) 从完整图重算真算子/完整步线性 EB、每条合法近端路径的锐有限长收敛、全对同输入碰撞和完整二参数区。[F25](FAILED_ROUTES.md#f25) 保存从收敛逆推全对 RL 的断点。逐源表为此增加一行；同 ZIP 的其它 GX 仍待裁决。

## 本批增量：惰性四循环的最优运输边界

[C71](research/topics/random_markov/lazy_cycle_ot.md#lc-sharp) 从 9/14 有限状态分类稿 §10.2 重算固定四状态模型的同步 OT 残差：位移签名碰撞不妨碍原残差精确识别唯一不变律，整律空间锐 EB 常数为 √(13/p)。同一核放松内层输入 OT 最优性则有假零点。此独立对象卡不关闭来源稿的有限状态一般分类、速率兼容或优先权；该批完成时逐单元表增至 51 行，随后 GX-075 增至 52 行。

## 本批增量：9/25 度量层与拓扑候选分离

[C70](research/canonical/finite_sample_collar.md) 从 S25 §8 独立重算有限样本全空间双包络、整窗全称步界和 EB 加上 collar 后的内域余量。C70 不给固定点或值域球；原稿 C05-v1 当时的 usc/acyclic、上同调和 Lefschetz 合取仍独立；其后 C05-v2 已对条件拓扑链重算。按 (8.3) 与 (8.4)–(8.7) 两个来源单元登记，不把 §8 整节判为已审。

## 当前增量：同常数扩张、GX-068、矩包络和新图的局部指数

[HE-EXTENSION](research/canonical/holder_extension.md#he-extension) 从 Gaussian 正定核重建 Hilbert \(\gamma\) 雪花，导入正式版 [LIT-ALM-2021 Theorem 1.2](research/LITERATURE.md#lit-alm-2021) 的同常数 Hilbert Lipschitz 扩张，闭合 H01 **固定参数 graph-maximal 完成**这一步的适用条件；不由此裁决 C03 整个影子定理或其他外部定理。

[C66–C68 / GX-068](research/topics/examples/identity_square_branch_union.md) 把 \(F(x)=\{x,x^2\}\) 的真算子残差锐半阶、指定身份近端的线性步残差、完整多值近端的半阶最小步残差及同输入跨支碰撞分为三个 Claim。历史同卡的两变量 MR、semimonotonicity 仍未验收。[C65](research/topics/path_dynamics/m1_sign_lift.md#sl-rl) 在**新定义**的完整 Sign 图上，证端点指定输入窗口的最大全对 RL 指数 \(1/3\)；它不认证旧循环方程或无界全图常数。

[C69 标量矩包络](research/topics/random_markov/scalar_moment_envelope.md#sme-envelope) 对硬支持下的全部概率律给精确凹上包络与两点取等。临界 \(\gamma q=1\) 时，若把同变量的两条逐点证书分开取最坏矩再复合，会虚增 \((R/t)^{1-\gamma}\)；[F24](FAILED_ROUTES.md#f24) 保存这个失相关机制。合法随机算法的同耦合、实际支撑和目标边缘仍是独立输入，不能将 C69 当作原生收敛定理。这批数学卡由三条独立代理分工并互相逆向检查；主线核量词、登记来源和依赖。

## 当前增量：三条独立重写与一个原生身份边界

[C60/C61](research/topics/examples/dr_tangency_transversality.md) 重算 9/01 ZIP 的 GX-069/070：同一 Douglas–Rachford 算法残差 \(G=I-T\) 在切触线/抛物线的唯一投影管有全邻域锐半阶 EB 模 1，但不存在统一一步距离严格收缩；横截两线则全域线性可逆，精确模 \(1/\sin\theta\)，轨道因子 \(\cos\theta\)。这是两种对象，该模不能授给法锥和。

[C62/C63](research/topics/random_markov/proximal_selection_seam.md) 对同一 proper Borel 目标的**全局**近端与指定 Borel 选择核重证所有域内平稳律只支撑吸收点，无需 \(f\) 可积。一个二维非乘积 group-\(\ell_0\) 目标有闭完整近端图和唯一不变律，却有有限长度轨道趋非不变点；每个完整 \(W_2\) 零点邻域内的真实 law-step 残差都缺一致消失 gauge EB。历史 V10 有理数脚本本轮复跑，只算有限代数观察；[F22](FAILED_ROUTES.md#f22) 留下闭图与核连续性之间的断点。它与 C22/C23 的随机换目标、同步 OT \(\Psi\) 均不同。

[C64](research/topics/path_dynamics/m1_sign_lift.md) 是从已核显式 T **新反演**出的完整 Sign 多值关系：全部图值与单位步长 resolvent 的所有纤维已算，\(J_{F_{\rm lift}}=T\) 在整个 \(\mathbb R^2\) 成立，端点真残差锐线性模 3。历史多步 §5 只给外层 T、未给原生循环方程全部相位和选择；另一个 M1/SO-06 是不同算子。[F23](FAILED_ROUTES.md#f23) 固定这条仍未闭的身份桥。下一步若得到原生方程，须逐图点和逐路径对照，不得用新构造替它认证。

## 当前增量：一般 gauge 的残差窗口

[C59](research/canonical/residual_window_bridge.md#rw-positive) 将旧 foundations 定义0.4 的正幂缩域推广为有条件的一般非减 gauge 桥：窗口阈值 \(\delta\) 处若 \(\psi(\delta)>0\)，可在半径 \(\psi(\delta)\) 内删除 **\(r_F<\delta\)** 的限制，但仍只对 \(\psi\) 定义域内的残差作陈述。[F21](FAILED_ROUTES.md#f21) 的完整闭图与扁平 gauge 表明不能无条件删除；该例不满足附加全对 RL，不能扩大其否定范围。逐源去向已补 §0.4。下一步可核 §0 其他定义在不同稿件的版本冲突，或优先清洗尚无对象卡的 GX 与 M1 原生多值桥。

## 前一增量：闭图与 Minty 自然域闭性的条件桥

[C58](research/canonical/closed_graph_minty_domain.md#cg-closure) 从旧 foundations §1.1–§1.4 的剪切坐标继续推导：同一非空图块上全对模只需在对角线附近于零点消失，完备 Hilbert 空间中 Cayley 唯一延拓至自然域闭包，图闭 iff 自然输入域闭。**再加自然域在整个空间稠密**才给满输入覆盖；闭图及全对 RL 本身仍无覆盖。E101–E102 明列两层额外门，不能把图块覆盖与完整 resolvent 任意纤维混同。§2 的 tied、inverse、缩放已在参数字典重算，这批将 §1–§2 五个精确单元补入逐源去向；这不是整份 foundations 的验收。随后 §0.4 的残差窗口边界已在上节处理。

## 第二批增量：§3 图块验证器的零锚保距离

[C56](research/canonical/all_pairs_verifier.md#av-bridge) 在实 Hilbert 空间把同图块全对 RL、指定输入 coverage 和 \(d(x,S_G)=d(x,S)\) 对所有活跃输入的保距离，精确接到 C53 的 B/A；实际输出真残差 EB、兼容和留域仍独立。[C57](research/canonical/all_pairs_verifier.md#av-gap) 以完整 \(F(y)=\{0,y\}\)、图块 \(G=\{(y,y)\}\) 表明全对 \(L=0\) 与满输入 coverage 仍可能在所有非零零距离输入失去锚，完整排他亦失败；[F20](FAILED_ROUTES.md#f20) 记录两个缺口。其后 §1.1–§2 的选定接口已按上节裁决；其他 GX 单元及 M1 原生多值桥仍开放。

## 当前增量：§4–§5 的指定分支与全对边界

[C53/C54](research/canonical/named_branch_local.md) 从旧 foundations §4–§5 重写了实 Hilbert 空间的 named PPA：B 整球分支覆盖、A 对所有小距离输入（包括零距离点）的近似最近零点锚、E 对实际输出的真实全纤维残差 EB、兼容与严格留域预算须合取。由 A/B 还可推出 \(U\cap\overline S=U\cap S\)，故无需额外假设全局闭零集或最近点存在。幂次门在 \(0<\gamma<1,L>0\)、\(\gamma=1\)、\(L=0\) 三种参数情形分别记录，只提供上阶和充分条件，不提供普适正 Q 因子。

[C55](research/canonical/named_branch_local.md#nb-oscillation) 是该批新反例：完整闭图有指定分支 anchored \(\gamma=1,L=3/5\)、全图真 EB、实际收缩，但反射在任意零邻域非 Lipschitz。[F19](FAILED_ROUTES.md#f19) 阻止把这条弱接口的结论作为 R02 全对 RL 的证明。该批留下的 §1.3–§2 入口已在本次选定单元中处理；其他 GX 和 M1 原生多值方程仍须核目标对象与全部完整纤维。

## 第三笔增量：逐图点移动锚与固定锚的边界

[C51/C52 移动锚反射](research/canonical/moving_anchor_reflection.md) 从旧 foundations §6 重算实际图点的输出近锚双边比、幂型缺陷及正容差近锚选择。真 EB 是输出 y 的全纤维残差，p 随 y、w 改变；[F18](FAILED_ROUTES.md#f18) 的线性零集完整关系说明不能将它变成任意固定锚的反射或集合距离收缩。下一步从 9/01 其余未验收 GX 或 §5 的局部收敛门选独立单元，继续按同对象、同目标和实际分支逐项裁决。

## 第二笔增量：非孤立解集的锚点漂移与锐性

[C48–C50 / 非孤立 alignment](research/canonical/nonisolated_alignment.md) 重新证明 9/01 foundations §8–§9.1 的锚点界、真 EB 合成与同序列饱和。\(P_S(x)\) 和 \(P_S(Jx)\) 的存在必须覆盖整个输入家族；未取到的集合间 infimum 用近似点对处理。若没有 proximinality，NA-APPROX 用正容差并要求额外 \(\kappa\) 预算。统一 \(\mathcal A(r)\le Kr^\theta\) 与实际输出真 EB 只给 upper \(\theta q\)；[F17](FAILED_ROUTES.md#f17) 记录“不同序列的两个锐指数相乘”的量词断点。下一步选择一个尚未重写的 GX 对象或 §5 的局部收敛门，逐项核图、目标与轨道；不要把 C49 当作它们的普遍最优性证明。

## 本轮增量：孤立零点与输入覆盖的独立门

[C45–C46 / 孤立零点正文](research/canonical/isolated_zero_flatness.md) 重写 9/01 foundations §7.1–7.6：同图 germ 的 B/J/R 平坦性逐点等价，但从有利选中值倒推真实全纤维 EB 必须覆盖所有小残差图值；指定分支的上阶还要全部输入/输出窗口、小步门及闭球留域。正 Q 因子要求另一条归一化极限，不由上阶产生。双值关系已给反向的精确障碍。§8 的非孤立 alignment 已在上节另立 C48–C50，仍须保持孤立与非孤立版本分离。

[C47 / GX-074](research/topics/path_dynamics/discrete_coverage.md) 将全图紧性、全对 RL 和目标 \(S=K\) 的真 EB 与输入 coverage 分离：[F16](FAILED_ROUTES.md#f16) 记录从前两者偷推零点输入球的失败机制。下一步若将此模型用于任何 PPA 结论，先明确初值是否在自然 Minty 域，以及是否另有不变性；更换零集目标会改变 EB 命题。逐源去向新增五个小节，不代表整份 foundations 已裁决。

## 当前新增前沿：规范层继续生长

上一批将 9/09 两份来源按**数学单元**重写为 [合法路径](research/canonical/path_atlas.md) C31–C33 和 [复合次正则](research/canonical/composite_subregularity.md) C34–C37；[逐单元去向](research/audit/UNIT_DISPOSITIONS.tsv) 明记哪些旧节被改写、哪些仍未审。历史 C11 复合任务与现 C11 极限回缩保持不同身份。两条新链都可以供未来研究调用，但不宣称旧文件全覆盖或文献新颖性。

路径链的承重条件是每条实际选择的前缀延拓、统一终点收缩、可求和的**块内**位移及初值边界预算。旧札记的无限词逐词幂条件缺统一余量，非平凡周期也不能从整轨道有限总长定理推出；[F12](FAILED_ROUTES.md#f12) 给反例。本批从**显式单值映射**重算 [M1 两步捕获和锐一步收缩](research/topics/path_dynamics/m1_capture.md) C38/C39：它已有一步因子 $3/\sqrt {10}<1$，不能用作现有一步轨道定理必然失败的见证，[F14](FAILED_ROUTES.md#f14) 固定修订。下一步恢复原生多值广义方程，核其隐式求解和全部允许分支是否确与这个 T 一致；当前 C38/C39 只供显式 T 调用。

复合链的承重条件是满行秩修复、凸链式规则和真实残差外层 EB 的合取；局部 PPA 还要全部乘子界、步长、gauge 兼容和留域。[F13](FAILED_ROUTES.md#f13) 的秩亏例阻止无条件传递。本批 [复合主题目录](research/topics/composite_regular/README.md) 对尖点外层给图真多值且局部近端一步识别的定量输入门 C40；[振荡反例](research/topics/composite_regular/oscillating_target.md) C41 给光滑坏驻点序列，证明无弱分离时到二阶目标的 EB 失败，[F15](FAILED_ROUTES.md#f15)。下一步研究带原生不抵消条件的秩亏版本，并单独核外部定理先行性。任何新结果按 [增长协议](RESEARCH_PROTOCOL.md) 直接进入正文及新 Claim 版本，不需等历史区清空。

数学定义、精确命题与来源分别见 [foundations](research/foundations.md)、[CLAIMS](CLAIMS.md)、[SOURCES](research/SOURCES.md)。数学状态以本仓库的精确证据为准。
## 活跃目标 A：RLEB–LT–极大单调的总体规模比较

**Exact gap**：给自然、参数中立、保留完整原图与真实残差的对象空间 \(\mathfrak X\)，明定计数单位 \(F\) 或 \((F,\lambda)\)、合法选择及局部域量词，再选一个不把目标类一齐压小的大小不变量 \(\mathcal I\)，证明同一母空间中 RLEB、LT 公共 all-pairs 和极大单调类的规模关系。当前没有该总体定理。

**已知组件**：完整全域 \(T=J_{\lambda F}\) 的图反演；匹配接口下 LT→RLEB 能量证书；固定紧 T-only 图卡 \(\Phi=(w,m)\) proper；有受限严格分离构造。均不能单独解决总体问题。[operator_space](research/operator_space.md)

**承重障碍**：

1. proper/quotient 不推出 category-preserving；单一局部 \(T\) 观测不保全局 \(F\) 和 \(r_F\)。
2. 9/21 总账报告 N05/N08/N10 的共同塌缩与 N09 远端自由度；其中 I-097–099 原孔隙审计及 I-102 正式表示稿未在当前盘点的原件名中发现，保留“来源包报告”而非重构证明。
3. 同时，9/21 旧 SOURCE-MISSING 是**当时**状态：I-001 已恢复 100/101 的历史展开内容（受限第三方 PDF 未入库）；I-002、I-003–005、I-059 已恢复；I-075 的 73 文件专题包以展开内容恢复，原重复 ZIP 未保留。I-005 实为审计**任务书**，不能当审计通过记录。解选择的实际修补证据在 I-059 内 revision_math_audit 与 revision_math_closure。

**下一判别**：写一页 \((\mathfrak X,\mathcal I,\mathcal R,\mathcal L,\mathcal M)\) 规格，先找 N05/N08/N09/N10 的反塌缩反例；若量尺共同塌缩，换表示或不变量，而非在特殊层追加成员例。

## 活跃目标 B：局部 RLEB 与结构稿的精确边界

- **S19 局部 PPA**：coverage + 同图块全对 RL + 真实输出 EB + gauge 兼容 + 留域，给有限长及尾界；一般模还需 Dini。该组合的缺一条件不能静默删除。[R01–R04](research/rleb_ppa.md)
- **9/19 新资产**：对数二支完整图 \(a\le1\) 显示几何距离收缩而切向漂移发散；\(a>1\) 收敛。统一尾与同图块全对连续性给局部极限回缩。这使“任意紧零集可实现”和“额外收敛条件下零集为邻域回缩”形成可检验的条件限制。[H04/H05](research/holder_structure.md)
- **9/19 随机措辞**：原稿写 Polish，证明用给定 \(d_{\mathsf X}\) 完备；\((0,2)\) 上的确定性序列满足其他假设却收敛到空间外。原命题若按拓扑 Polish 解释为假；修订版本明确 complete metric。[H06](research/holder_structure.md)、[FAILED F07](FAILED_ROUTES.md)
- **S23 全局结构**：同一个强单调双 Lipschitz 影子及有限维完整纤维分类的证明已局部独立重算，未见内部计算致命断点；Hilbert 同常数扩张的导入门已核；有限维 degree/fixed-set 的完整应用及同对象先行性仍是独立门。固定维数的最优因子仍开放。
- **S23 值域与有限数据**：最大根定位给全局与相对 maximal 窗口的**整个纤维**锐覆盖；有限兼容样本的 QP 给全局一致 \(A_m\)，但未知图点只在 Cayley 参数覆盖下认证。可验证 gap、噪声和求值误差叠加成三项界；有限总查询在无界 Hölder 类不能全空间认证。[range_finite_data](research/range_finite_data.md)。这条链原八条 Claim 未记录，现立 C18–C21。
- **S25 局部值域**：指定 \(T\) 可以是完整 resolvent 的子关系；有限数据包络和整窗 usc/Čech-acyclic/topological 条件是不同层。Theorem 8.1 的外部引用 [6, Theorem 6.2] 已与[一手原文](research/LITERATURE.md#lit-grn-2002)逐项核 retract、Vietoris span、紧 morphism→CAC 及非零 Lefschetz 数；这不核定整窗模型、有限样本认证以外的假设或新颖性，原稿 C05-v1 仍为 PDF-only 候选；C05-v2 是另立的已重算条件版本。[H07](research/holder_structure.md)

## 独立旁支与依赖门

| 链 | 当前可使用的精确成果 | 不得越过的门 |
| --- | --- | --- |
| 锥 | nice + 冻结 CRSC 的秩夹逼、面稳定，参考面 amenability 与法向/切向修正给 MSCQ；nice 非 amenable 的普遍量词边界 | 原锥残差到 \(r_F\) 的桥、同一零集、反射和 coverage 另证；文献正式版优先权待核 |
| Markov | 紧连续同步 OT \(\Psi\) 的 exact-zero⇔一般 gauge；有限状态顶点测试⇔线性 EB；条件 bit/Gaussian 修复 | 表示依赖、同耦合、守恒边缘、recoupling；不能由快收敛反推原 \(\Psi\) EB |
| 解选择 | 统一尾 + 局部 Hölder → 对数/超几何极限模；完整显式例的两点非 Hölder | 只对 \(J_{\mathcal G}\) 直接导入；完整 \(J_F\) 须全纤维一致；经典 AGM 先例已覆盖较宽现象 |
| 不一致随机近端 | 固定守恒边缘与活跃均方谱隙给条件 \(W_2\) 收缩、完整混合核 law-step 的线性 EB 和有限长度；逐分支残差的零集则是共同定点支持律，标量例使统一 EB 系数锐 | C22/C23 的证明和反例在 [RP 模块](research/canonical/random_proximal.md)；不改成普通联合 \(W_2\)、同步缺陷或物理步长；外部优先权、无限维/变参数仍待审 |

各链的定义、量词与反例在 [cone_markov](research/cone_markov.md) 和 [solution_selection](research/solution_selection.md)。

## 证据与下一阶段

现有独立工作只对各模块明确标注的公式、证明链和反例进行了重算；未逐行 referee 全部 251 个来源记录，也未完成外部文献精确适用条件与全球新颖性。历史 HTML/JSON 的 35 条边是搜索种子；当前 133 条边经版本和范围重组，数目不是数学质量指标。数值代码和审计 PASS 仍保持原证据层。

**覆盖边界**：原件 251 个、ZIP 11 个及成员 178 个已清点，其中 41 个成员与展开件字节相同；这不是数学验收数。逐单元去向只覆盖表列的 52 个数学单元；GX 余项、随机其他支线、M1 **历史原生图桥**、复合秩亏原生证明和其他外部文献仍待核。十个历史验证器的退出码与环境记录在审计 JSON，不能证明一般命题。
**例库新增**：[C42 幂次剪切](research/topics/path_dynamics/power_shear.md) 从完整图重算真残差和精确法向速率；只在有界输入窗有全对次线性反射证书，切向余量单独控制轨道留域。[C43 振荡剪切](research/topics/path_dynamics/oscillatory_shear.md) 另给有界窗最大全对指数 γ、但局部双边实际阶 q>γq 的独立对象；真残差与局部零集已核。[C44 自然域逃逸](research/topics/path_dynamics/domain_escape.md) 从同稿另立多值原图对象，核了锚定/全对指数、全纤维线性残差与每条非零轨道有限步越域。三例不能按共享幂指数合并。

**例库首批**：C24–C26 的 EX01 旋转、EX02 正紧对角、EX03 三次映射已给完整对象、真实残差和直接证明。尤其 EX02 排除任何趋零 gauge 的统一局部 EB，却保留每个初值的 PPA 强收敛；EX03 将固定目标常数 1、两变量 \(2^{2/3}\) 与算法残差下确界 \(\lambda^{-1/3}\) 分开。此三例只关闭对应 GX-004/009/021 的本轮数学单元，原卡其他性质和其余 GX 尚待重写。

**定义/参数首批**：[PD 字典](research/canonical/parameter_dictionary.md)重写了全对/锚定、全图/图块、coverage/exclusion、同图换步、线性 RL tied 曲线、有界尺度指数及真残差方向，C27–C30 分别固定数学身份。若要比较不同步长，先核新 Minty 输入 \(Q(D)\) 的单射与 coverage；若要把选中步界写成真 EB，先核全纤维最小残差的方向。这些是当前可直接复用的基础，旧 checkpoint 的完整定义和全部示例尚未逐项关门。

下一阶段先补证据门：追 I-097–099/I-102；在 9/25 [6] 引文已核的基础上独立审整窗模型与数值包络；正式修随机完备性；再让总体比较的一个精确空间/量尺接受反塌缩攻击。若没有新证据，不新增“已证”节点。
