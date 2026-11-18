# 单调性与正则性的共同结构

<a id="mother-question"></a>
## 首要问题

寻找原算子 \(F\) 的内生几何或变分对象 \(M\)。在有独立数学意义的两种附加结构下，分别恢复清楚指定的单调性及正则性，并找出它们之间可以计算或证明的桥梁。若要推出原 PPA 的新结论，需再找出对同一近端弦起作用的耦合推导。一般非线性、非孤立、非势且允许多值的层面目前开放。

此前 C320 用原图值的对称闭凸包改进标量兼容，但仍保留最近零锚 RL 和真残差假设。C323 还表明，在光滑局部全部根的合同上，C320 与横向距离收缩等价。因此，C320 作为已证的方向误差界继续使用，本轮研究的母结构另开问题。[C320](../../canonical/ppa_two_step_and_directional_residual.md#td-directional) · [C323](../../canonical/ppa_native_alignment_and_transverse_test.md#native-transverse)

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
| [原图间隙的两个切片](../../canonical/graph_gap_monotonicity_regularity.md) | 图上零值刻画单调或弱单调，零残差截面的二次增长在明确覆盖下等价于真残差线性次正则。反向线性图给直接收敛蕴含的反例。 |
| [能量、支撑与满秩复合](energy.md) | 精读 LMZ，给出支撑亏损的锐路线：当 \(d^q\lesssim r\)，保住 KL 指数 \(q/(1+q)\) 的全类阈值是 \(\alpha\ge\max(0,1-1/q)\)。另给用原增长支撑直接证明完整近端收敛、且对任意收缩因子排除 C320 的曲复合实例。 |
| [图投影、横截性与活动零点](geometry.md) | 检查同一图的两类观察能解释什么，以及固定一点的一阶等式会漏掉什么。 |
| [角度、法向变化和非势算子](angle.md) | 比较半单调、原图角度、对偶间隙和法向尺度，给出可检验的子类及其先行性边界。 |
| [非势原图的临界曲率](critical_graph.md) | 全对图亏损的候选收敛分界、完整单值原 PPA 的恒距圆轨道及有限长度反例。精确的小常数临界问题仍开放。 |
| [两个独立审查与研究优先级](ASSESSMENT.md) | 核对哪些桥已证、哪些是既有语言、哪些反例决定了下一步。 |
| [给 GPT Pro 的完整任务书](GPT_PRO_PROMPT.md) | 可直接交接。里面固定了定义、量词、去重索引、试证方向和验收条件。 |

<a id="bridge-guards"></a>
## 两项最短验收反例

统一类若允许 \(F(a,n)=(0,n^3)\)，令 \(S=\mathbb R\times\{0\}\)。该图最大单调，全域唯一原根，但 \(d(y,S)/d(x,S)=(1+\lambda n^2)^{-1}\to1\)，真残差也不满足线性次正则。恢复普通单调性的分支如果要直接推出固定 \(\kappa\) 的 A，必须另外排除此类平坦图。它不阻止依靠非线性尺度的收敛。

同一 \(S\) 取 \(F(a,n)=(0,-n)\)，真残差等于 \(d(\cdot,S)\)，固定 \(0<\lambda<1\) 的全域唯一原根却给 \(d(y,S)=(1-\lambda)^{-1}d(x,S)\)。所以恢复零值次正则的分支单独不能给收缩。 \(\mathbb R\) 上的 \(F=-I\) 还给普通强度量正则下的同样反例。两例用来限定强度，并不排除两支之间存在结构桥。
