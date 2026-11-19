# 单调性与正则性的共同结构

<a id="mother-question"></a>
## 首要问题

本线的目标是构造可逐行扩展的共同充分条件 \(W\)，把指定的单调或次单调、指定的正则性及该组合的可行参数窗接成原 PPA 的收敛证明。最低结论为从每个认证初值存在一条收敛的原轨道。全根收敛及更强速率属于附加结论。原 RLEB 测试行须保留原一般反射模及根量词。[目标、三项条件与前期误判](OBJECTIVE_AND_PITFALLS.md)

首要义务是找同一个 \(W\)，证明它在两种附加条件下分别等价于单调或次单调、正则性，并能推出原 PPA 收敛。[C341 的补偿锚距条件](compensated_anchor_convergence.md#ca-definition) 已把投稿原 RLEB 与有限维极大单调 PPA 导入同一收敛证书。当前任务和完成条件见 [GPT Pro 任务书](GPT_PRO_PROMPT.md#pro-hard-gates)。

新增的 [C345 同纤维反射刚性](fiber_reflection_rigidity.md) 给出可单独使用的图值—锚差估计，但其相对方向项尚未用于原PPA下降，不能代替该首要义务。[F114](../../../FAILED_ROUTES.md#f114) 明确了从加权平方退回旧半和兼容的断点。

[C346 回返缺口与循环归约](return_gap_and_loop_reduction.md) 保留全锚平方耗散下的完整真残差转接，但一般原 RLEB 的循环导入仍由旧下降与连续补偿给出；[F115](../../../FAILED_ROUTES.md#f115) 记录两个反向恢复尚缺的具体位置。

[C347 保残差最大补全](residual_preserving_fiber_completion.md) 在固定原允许关系和整套 RLEB 参数时填满完整纤维方向，精确限制倾斜残差或完整低范数功剖面的无条件导入。

[C348 倾斜纤维两等价](tilted_fiber_equivalences.md) 已核数学推导，但其原一般 RLEB 下降仍被旧下逆更强估计覆盖；固定原κ的改进没有关闭机制门。

此前 C320 用原图值的对称闭凸包改进标量兼容，但仍保留最近零锚 RL 和真残差假设。C323 还表明，在光滑局部全部根的合同上，C320 与横向距离收缩等价。因此，C320 作为已证的方向误差界继续使用；C341 通过补偿锚距处理固定距离收缩之外的原图，其他组合仍需单独导入。[C320](../../canonical/ppa_two_step_and_directional_residual.md#td-directional) · [C323](../../canonical/ppa_native_alignment_and_transverse_test.md#native-transverse)

<a id="mother-result"></a>
## 已接收的共同条件及其边界

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
| [同一完整残差下的图值与零锚差](fiber_reflection_rigidity.md) | C345：原一般反射模的最优加权恒等及两个同纤维真实图值的共同约束。证明成立；跨值方向关系的动力学承重和结构新意仍未完成。 |
| [回返缺口与循环误差的准确来源](return_gap_and_loop_reduction.md) | C346：全锚平方耗散下的回返—真残差双侧估计；连续补偿已推出任意周期误差界，原最近零锚一般模的反向方向恢复未闭。 |
| [保残差补全与完整纤维方向自由度](residual_preserving_fiber_completion.md) | C347：固定原允许 RLEB、完整真残差和误差界时的最大补全；检验允许方向与完整残差是否被错误扩充为完整纤维方向条件。 |
| [倾斜纤维的两等价与承重边界](tilted_fiber_equivalences.md) | C348：真实双右端距离的结构恢复成立；原一般模导入的下降可由旧下逆更强地推出，仍不能宣布共同结构完成。 |
| [原图间隙的两个切片](../../canonical/graph_gap_monotonicity_regularity.md) | 图上零值刻画单调或弱单调，零残差截面的二次增长在明确覆盖下等价于真残差线性次正则。反向线性图给直接收敛蕴含的反例。 |
| [能量、支撑与满秩复合](energy.md) | 精读 LMZ，给出支撑亏损的锐路线：当 \(d^q\lesssim r\)，保住 KL 指数 \(q/(1+q)\) 的全类阈值是 \(\alpha\ge\max(0,1-1/q)\)。另给用原增长支撑直接证明完整近端收敛、且对任意收缩因子排除 C320 的曲复合实例。 |
| [图投影、横截性与活动零点](geometry.md) | 检查同一图的两类观察能解释什么，以及固定一点的一阶等式会漏掉什么。 |
| [角度、法向变化和非势算子](angle.md) | 比较半单调、原图角度、对偶间隙和法向尺度，给出可检验的子类及其先行性边界。 |
| [非势原图的临界曲率](critical_graph.md) | 全对图亏损的候选收敛分界、完整单值原 PPA 的恒距圆轨道及有限长度反例。精确的小常数临界问题仍开放。 |
| [两个独立审查与研究优先级](ASSESSMENT.md) | 核对哪些桥已证、哪些是既有语言、哪些反例决定了下一步。 |
| [研究目标与已有教训](OBJECTIVE_AND_PITFALLS.md) | 三项前提怎样合用，存在轨道和全选的区别，参数的精确例子、本线主要误判及下一步。 |
| [GPT Pro 持续研究任务书](GPT_PRO_PROMPT.md) | 候选必须逐项证明原 RLEB 导入、独立基准导入、真实参数窗、原轨道存在及新数学信息。未通过就试证、反证或换机制。 |
| [补偿锚距条件与双锐边界](compensated_anchor_convergence.md) | C341 的共同定义、无限续接与点收敛、原 RLEB 同模同预算导入、全部固定正步长的极大单调导入；C342 的旋转族双门和 C277/C329 的完整去重。继续这一线先读。 |
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
