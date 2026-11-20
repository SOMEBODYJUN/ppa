# 单调性与正则性的共同结构

<a id="mother-question"></a>
## 首要问题

从原算子图出发，找出单调性与正则性各自约束的变化及其在原步中的共同机制。已有收敛定理用于候选成形后的覆盖检验，下面的旧路线和反例用于核对候选的适用范围。[现行研究任务](GPT_PRO_M_RESEARCH_PROMPT.md)


[两锚角度与逆分支](two_anchor_angle_inverse.md)按作者几何图区分原步三角形与误差界圆。C381 保留输出换锚的平方余量，得到完整真误差界与最近锚方向余弦的两段锐门和长度预算。C382 以同一逆支角度式构造原根并证点收敛，允许非孤立、多值及一般逆模。原一般 RL 的导入仍开放。

[第二批强弱补偿技术库](compensation_methods_2.md)保存28张技术卡、12项初试及逐组深试义务：C377完整残差K包络、C378强逆端点、C379有符号锥、C380弱凸增长支付，以及窗口、图修正和未来点几何。来源、重复家族和范围分别标明；一般M仍开放。首批[25项技术初试](compensation_trials.md)继续作为基础，不能把两批数量当作独立理论数。

[反馈的两个限定恢复](gradient_feedback_recovery.md#feedback-recovery) 给出未知共同势在线性类的精确内积单调恢复，以及完整增益图下的同势增长与一般模正则等价。原图可任意缩速与跨位置旋转的证明，解释一般恢复为何仍失败；不依赖法向或切向分解。

[C372 当前反馈 M 的恢复边界与验证成本](operational_m_assessment.md) 固定本轮裁决：障碍来自单点/两点量词和完整纤维信息的丢失，而非二次与一般模的阶数；线性类只在等价内积或度量兼容子类中恢复欧氏单调。法向/切向公式保留为诊断，不作为完整 M 的验收条件。


[C363–C365 原近端混合闭链](gradient_feedback_proximal_cycles.md#feedback-original-steps) 把完整原弦与 C362 的插值条件放进同一闭链。严格参数时从闭链建立原 PPA 点收敛；临界绕行、慢位移完整 RLEB 以及两步极小化障碍标出覆盖边界。[C366 从闭链得到原根](gradient_feedback_proximal_cycles.md#feedback-original-root-existence) 给出预先没有原根覆盖的版本。

[C362 一般模反馈](gradient_feedback_general_modulus.md#feedback-modulus-cycles) 用原图选出的梯度和闭合链判断能否来自同一平坦势。凸版本给两点碰撞的非二次代价。路径定理量化实现整条已给定近端路径的扰动大小，也能恢复完整真残差的固定目标扰动半径。用于比较线性与非线性反馈及识别原根生成缺口。

[C361 反馈插值](gradient_feedback_interpolation.md#feedback-interpolation)保留两点弱单调与固定目标置零的刻画。[当前定义与 PPA 公式复核](gradient_feedback_interpolation.md#feedback-review)给出全点抵消必需的 \(r_F\le Ld\) 和梯度限制，说明其原一般 RLEB 导入失败。原距离估计在一般闭零集上不成立，单点目标及限定参数版本另有证明。后续可研究同一反馈关系中的两类稳定余量，但不能据现有两个测试宣布已恢复同一 \(M_L\)。

[C360 原离散阻尼与连续场障碍](rleb_discrete_damping_and_flow_obstruction.md#rleb-discrete-damping) 在同一尖锐非线性原认证及全域唯一收敛原近端下实现原连续周期、漂移和任意给定的紧流因子。连续势或原连续趋稳不是普遍导入。

[C359 凸化原近端路径的正则盲区](convexified_proximal_paths_obstruction.md#convexified-proximal-paths) 保持完整纤维与全部有限、无限原路径的凸化信息，并分离完整真误差界幂。两图共享真正非线性的原 RLEB。

[C358 的原近端切向搬运代价](proximal_input_noise_transport.md#input-noise-transport) 精确计算剪切图在一般小输入误差下的搬运成本，并给任意原一般模 RLEB 的可和扰动预算。单调与正则的共同恢复仍开放。

[C357 的保目标距离近端共轭障碍](ppa_conjugacy_obstruction.md#ppa-conjugacy) 说明原动力、精确目标距离及共同 RLEB 数据仍不能无条件决定欧氏单调和真残差幂。

**共同结构 \(M\) 尚未找到。C351 按本任务判失败。** 从原锚点 RL 与误差界出发的相容重写、消元和精确幅度匹配已被作者排除。[现行提示词](GPT_PRO_M_RESEARCH_PROMPT.md) · [F120](../../../FAILED_ROUTES.md#f120)

现行目标要求在两组各有独立含义的附加条件下，用同一个几何结构 \(M\) 分别恢复单调或次单调与正则性，再由该结构证明原 PPA 从每个认证初值至少有一条点收敛轨道。旧目标 \(W\) 只要求共用充分证书，详见[早期任务与前期误判](OBJECTIVE_AND_PITFALLS.md)。

C351 的两个限定恢复和原 PPA 推论作为数学关系保存，其任务验收已撤回。[C341 的补偿锚距条件](compensated_anchor_convergence.md#ca-definition)保存两条旧路线共用的收敛证书。后续研究要从各类性质的独立定义寻找共同结构，再用它容纳原 RLEB。

[C354 的近端度与选根障碍](rleb_degree_and_selection_obstruction.md#rleb-degree) 给出同参任意局部度，通过计算全部原根、最优幂反射模和完整残差模来检验拓扑候选的导入范围。

[C355 的两步方向实现](rleb_arbitrary_two_step_directions.md#arbitrary-two-step-directions) 在固定完整真残差和每弦全部剪切长度的同时，允许任意闭球面两步关系。用于检查只从精确长度数据推导跨步方向约束的候选。

[C356 的孤立覆盖步长](isolated_proximal_coverage_step.md#isolated-coverage-step) 用两个复块得到精确的全域与局部根覆盖谱。用于检验跨步长连续变形的覆盖前提。

新增的 [C345 同纤维反射刚性](fiber_reflection_rigidity.md) 给出可单独使用的图值—锚差估计，但其相对方向项尚未用于原PPA下降，未完成它自身的结构承重义务。[F114](../../../FAILED_ROUTES.md#f114) 明确了从加权平方退回旧半和兼容的断点。

[C346 回返缺口与循环归约](return_gap_and_loop_reduction.md) 保留全锚平方耗散下的完整真残差转接，但一般原 RLEB 的循环导入仍由旧下降与连续补偿给出；[F115](../../../FAILED_ROUTES.md#f115) 记录两个反向恢复尚缺的具体位置。

[C347 保残差最大补全](residual_preserving_fiber_completion.md) 在固定原允许关系和整套 RLEB 参数时填满完整纤维方向，精确限制倾斜残差或完整低范数功剖面的无条件导入。

[C348 倾斜纤维两等价](tilted_fiber_equivalences.md) 已核数学推导，但其原一般 RLEB 下降仍被旧下逆更强估计覆盖；固定原κ的改进没有关闭机制门。

[C349 两项匹配及归约](matching_certificate_reduction.md) 的两恢复与多值上下端为真，但新越界分支不参与原 RLEB 及两恢复，仍未通过共同机制验收。

[C350 跨边完整残差损失](incoming_residual_reflection.md) 已把优化反射偏差接到相邻完整残差与归一化长度预算；纯点收敛仍可删掉该费用，故为已证中间关系。

此前 C320 用原图值的对称闭凸包改进标量兼容，但仍保留最近零锚 RL 和真残差假设。C323 还表明，在光滑局部全部根的合同上，C320 与横向距离收缩等价。因此，C320 作为已证的方向误差界继续使用；C341 通过补偿锚距处理固定距离收缩之外的原图，其他组合仍需单独导入。[C320](../../canonical/ppa_two_step_and_directional_residual.md#td-directional) · [C323](../../canonical/ppa_native_alignment_and_transverse_test.md#native-transverse)

<a id="mother-result"></a>
## 旧候选与共用收敛证书的数学范围

C351 刻画存在相容原模的严格开壳条件，含最小包络的帽和 Dini 条件。两个恢复共用同一非线性参考尺度并依赖非对角项。任务验收已撤回，理由见 [F120](../../../FAILED_ROUTES.md#f120)。下列 C341–C342 的早期收敛证书按各自证明范围保存。

[C341–C342 正文](compensated_anchor_convergence.md) 固定原弦 \(x-y\in\lambda F(y)\)，用全部目标锚的距离增量加归一化平方步长，要求它由静态径向补偿 \(h(d(x))-h(d(y))\) 支付。真正则识别和可续接的原根子关系是独立、明确的前提。共有引理不要求固定距离收缩或物理有限长度。原 RLEB 以 \(h=2\Theta\) 导入而保留原 \(\Theta\) 留域预算；极大单调行以 \(h=0\) 导入。

旋转—漂移族将实际收敛的 \(\beta>\alpha\) 与证书附加的 \(\alpha<2\) 分开，在 \(1\le\alpha<2\) 给全部固定分组长度发散的严格见证。全锚 Fejér 和 C329 的宽参数门分别排除。三条独立重构及 v1→v2 的量词修订见 [第 004 轮历史验收](../../audit/COMMON_STRUCTURE_M_ACCEPTANCE_2026-11-18.md)。

下一步可用 [C343 增维残差候选](lifted_residual_distance.md) 和 [C344 有限锚候选](finite_anchor_convergence.md) 检查不同的补偿与目标识别；二者自身仍为 candidate，勿与已接收的 M003-v2 混为等价公式。实际收敛且平方步长可和的交错切向例仍不能被 M003-v2 认证，见正文的量词攻击节。

<a id="bridge-literature"></a>
## 从朱江醒的论文读出什么

[朱江醒与合著者的预印本](https://arxiv.org/html/2406.13207v1#S6) 里，Propositions 6.2–6.3、Corollary 6.5 的桥是
\[
\text{能量—斜率 KL}
\ \Longrightarrow\
d\big(x,[f\le f(\bar x)]\big)\lesssim (f(x)-f(\bar x))^{1-\theta}
\ \Longrightarrow\
d(x,\Theta)\lesssim\|\nabla f(x)\|^{(1-\theta)/\theta}.
\]
第二步用到了子水平集与驻点集的局部目标识别，同时再用一次 KL 消掉能量差。原文采用距离端 \(\psi(d)\le C r\)，所以写的幂是 \(\theta/(1-\theta)\)；本库残差端 \(d\le \widetilde\psi(r)\) 对应倒数。Theorem 5.1 是另一层的算法证明，用下降、相对误差与 KL 望远镜推出**实际步长绝对可和**。更抽象的先例是 Bolte–Daniilidis–Ley–Mazet 的解奇异化上图映射正则性。上图映射的值类型是能量水平，和原算子图的向量值不同。[定理原文位置和其他一手材料](../../LITERATURE.md#lit-monotonicity-regularity-bridge)

<a id="bridge-checklist"></a>
## 研究资料的读法

| 材料 | 能复用的结论或用途 |
| --- | --- |
| [原图跨位置反射—残差相容](two_point_scale_compatibility.md) | C351：任意原模存在性的充要关系、同一非线性尺度下的方向/真误差恢复及原轨道证明；跨位置项不可由同一条边的数据代替。 |
| [反射余量与完整残差阈值](reflection_residual_transfer_candidate.md) | C352：有符号平移、完整纤维可实现区间及恢复；单独路线尚未完成最终结构验收。 |
| [全部剪切长度的单调性盲区](radial_shear_obstruction.md) | C353：一点所有剪切范数也不能无条件决定通常两点单调；保留锚定和全对量词的区分。 |
| [同一完整残差下的图值与零锚差](fiber_reflection_rigidity.md) | C345：原一般反射模的最优加权恒等及两个同纤维真实图值的共同约束。证明成立；跨值方向关系的动力学承重和结构新意仍未完成。 |
| [回返缺口与循环误差的准确来源](return_gap_and_loop_reduction.md) | C346：全锚平方耗散下的回返—真残差双侧估计；连续补偿已推出任意周期误差界，原最近零锚一般模的反向方向恢复未闭。 |
| [保残差补全与完整纤维方向自由度](residual_preserving_fiber_completion.md) | C347：固定原允许 RLEB、完整真残差和误差界时的最大补全；检验允许方向与完整残差是否被错误扩充为完整纤维方向条件。 |
| [倾斜纤维的两等价与承重边界](tilted_fiber_equivalences.md) | C348：真实双右端距离的结构恢复成立；原一般模导入的下降可由旧下逆更强地推出，仍不能宣布共同结构完成。 |
| [两项匹配、纤维阈值与主链归约](matching_certificate_reduction.md) | C349：同参数两个恢复、一般多值切向上界及原 PPA；三个要求链均可删去新越界机制，恢复可归约到同一近端最小增益水平。 |
| [跨边完整残差与反射损失](incoming_residual_reflection.md) | C350：最近输入零锚偏差、使用值非最小性、前后完整残差的精确分解；同参恢复和原一般 RLEB 全部初值已核，方向费用尚未承担纯点收敛的必要推导。 |
| [原图间隙的两个切片](../../canonical/graph_gap_monotonicity_regularity.md) | 图上零值刻画单调或弱单调，零残差截面的二次增长在明确覆盖下等价于真残差线性次正则。反向线性图给直接收敛蕴含的反例。 |
| [能量、支撑与满秩复合](energy.md) | 精读 LMZ，给出支撑亏损的锐路线：当 \(d^q\lesssim r\)，保住 KL 指数 \(q/(1+q)\) 的全类阈值是 \(\alpha\ge\max(0,1-1/q)\)。另给用原增长支撑直接证明完整近端收敛、且对任意收缩因子排除 C320 的曲复合实例。 |
| [图投影、横截性与活动零点](geometry.md) | 检查同一图的两类观察能解释什么，以及固定一点的一阶等式会漏掉什么。 |
| [角度、法向变化和非势算子](angle.md) | 比较半单调、原图角度、对偶间隙和法向尺度，给出可检验的子类及其先行性边界。 |
| [非势原图的临界曲率](critical_graph.md) | 全对图亏损的候选收敛分界、完整单值原 PPA 的恒距圆轨道及有限长度反例。精确的小常数临界问题仍开放。 |
| [两个独立审查与研究优先级](ASSESSMENT.md) | 核对哪些桥已证、哪些是既有语言、哪些反例决定了下一步。 |
| [研究目标与已有教训](OBJECTIVE_AND_PITFALLS.md) | 三项前提怎样合用，存在轨道和全选的区别，参数的精确例子、本线主要误判及下一步。 |
| [新写的 GPT Pro 研究任务](GPT_PRO_M_RESEARCH_PROMPT.md) | 从两类性质的独立含义寻找共同 M，明确两个恢复、原 PPA 推论和已排除的 RL 修补路线。先读此任务，再按需要调用旧资产。 |

本稿于 2026-11-19 独立起草。写法参考 [prompt-master 1.8.2 的 SKILL 和 OpenAI Task Brief](https://github.com/nidhinjs/prompt-master/tree/49b3a72469b1e7287d66387004ccfcca90e5968a)，数学任务表述参考 [MathResearchPrompts](https://github.com/optsuite/MathResearchPrompts/tree/0f7890f202ec26645b2b90d322d91bee711c7d75)。本次拉取的两库主分支最近提交分别为 2026-10-22 和 2026-08-25。前者有 GPT-6.1 及 OpenAI 推理模型说明，后者有实际数学研究提示词。本轮未核实到专为 GPT-6.2 Pro 数学研究设置的开源库，模型写法同时核读 [OpenAI 当前 GPT-6.2 指南](https://developers.openai.com/api/docs/guides/latest-model)和[推理模型提示指南](https://developers.openai.com/api/docs/guides/reasoning-best-practices)。这些参考提供起草方法，本稿尚未经 Pro 研究运行检验。
| [补偿锚距条件与双锐边界](compensated_anchor_convergence.md) | C341 的共用收敛证书、原 RLEB 同模同预算导入、全部固定正步长的极大单调导入；C342 的旋转族双门和 C277/C329 的完整去重。用于比较候选的收敛覆盖。 |
| [第 004 轮接收记录](../../audit/COMMON_STRUCTURE_M_ACCEPTANCE_2026-11-18.md) | 四轮候选的实际裁决、v1 的退化量词反例、修订版本的 G1–G7 承重证据，以及内部正确性和公开新颖性的分界。 |
| [增维真残差锚距](lifted_residual_distance.md) | C343 候选：无连续性静态补偿、仿射精确公式、漂移函数的锐积分门；保留完整推导，独立验收尚未结束。 |
| [有限零锚的测距与图功](finite_anchor_convergence.md) | C344 候选：有限测距点分开局部目标、壳层访问界和全锚比较；读其固定窗口量词后再尝试推广。 |
| [LT 同球留域反例](lt_ball_localization_obstruction.md#lt-ball-counterexample) | C340 逐项满足正式 Assumption 2，却否定其 Theorem 2 的同半径欧氏球根覆盖。实际完整轨道仍收敛；用于 G3 导入时区分正确结构条件与错误局部化。 |
| [原非线性 RL 与真残差的图桥](nonlinear_rl_bridge.md) | C333 排除固定输出惩罚的同弦证明。C334 用同一非线性反射模转接真残差与原弦。C335 显示标量图宽度改变最佳幂。C336 给固定原模的精确向量检验，C337–C339 分别定位最近锚、多尺度数据和多值长支的障碍。 |
| [二次移位 Fitzpatrick 母面桥](mother_fitzpatrick_bridge.md) | 常数二次弱单调子类：全图间隙的图截面等价弱单调，零锚截面在完整近端覆盖下等价真残差线性次正则；同一近端弦在 \(\lambda\beta<1/2,\lambda>2\beta K^2\) 下给输入版 \(A+B\)、点收敛和有限长度，并给出 \(F=B(y)T(Cy)\) 的完整纤维传递与 \(CB(y)\) 定向功。 |
| [临界 \(q=2,\alpha=1\) 的 reach 子类](critical_q2_reach.md) | 在 \(C^{1,1}\) 零流形、统一 reach、严格平方下降和完整根共同留域下，切向图值估计与二进制尺度求和给每条轨道点收敛；它不覆盖一般闭非孤立零集，也不自动给物理有限长度。 |
| [\(q=2\) 间隙振幅截面](q2_gap_amplitude.md) | 对同一 \(M\) 取 \(\sqrt{g_a}\)，把二次间隙增长与 \(d^2\lesssim r_F\) 精确接上；反向常数需要完整近端覆盖和图值帽。 |
| [单调边界与 firm Fejér](mother_fitzpatrick_bridge.md#mother) | \(\beta=0\) 时任意非空闭零集的完整 PPA 轨道点收敛、平方步长可和；这标出 value-weighted 临界问题真正从 \(C>0\) 开始。 |

<a id="bridge-guards"></a>
## 两项最短验收反例

统一类若允许 \(F(a,n)=(0,n^3)\)，令 \(S=\mathbb R\times\{0\}\)。该图最大单调，全域唯一原根，但 \(d(y,S)/d(x,S)=(1+\lambda n^2)^{-1}\to1\)，真残差也不满足线性次正则。恢复普通单调性的分支如果要直接推出固定 \(\kappa\) 的 A，必须另外排除此类平坦图。它不阻止依靠非线性尺度的收敛。

同一 \(S\) 取 \(F(a,n)=(0,-n)\)，真残差等于 \(d(\cdot,S)\)，固定 \(0<\lambda<1\) 的全域唯一原根却给 \(d(y,S)=(1-\lambda)^{-1}d(x,S)\)。所以恢复零值次正则的分支单独不能给收缩。 \(\mathbb R\) 上的 \(F=-I\) 还给普通强度量正则下的同样反例。两例用来限定强度，并不排除两支之间存在结构桥。
