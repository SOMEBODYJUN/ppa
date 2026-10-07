# Failed Routes / Obstructions

这些卡片保存**失败的精确目标和机制**。9/21 v0.9 的历史 SOURCE-MISSING 不能原封不动当作当前状态：I-001 历史包 100/101 项已展开、I-002/I-003–005/I-059 已恢复，I-075 专题包以展开内容恢复；I-097–099 与 I-102 仍未在盘点文件名中发现。I-005 是审计任务书，不是审计报告。未重构原证明的 N05/N10 仍标“来源包报告”；详情见 [来源谱系](research/SOURCES.md) 与 [no-go ledger](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。一种量尺在一个空间失败，不是整个比较问题不可能。

## F01 · 以单个 cusp / 仿射漂移层代替总体覆盖

- **尝试及机制**：构造严格 RLEB、所有正步长排除 LT 的算子，或在预置超吸引／尖点的比较层内证明 LT 第一纲；希望推广到自然完整原图母空间。
- **失败点**：特殊层可以是 Baire 且在自身余稀，却在母空间第一纲或位置未知；固定证书指数、局部缩域和精确同尾的量词并未自动保留。属于**总体推广逻辑缺口**，不是受限构造被反例否定。
- **排除范围与 salvage**：排除“一个例子/层内 residual 就完成总体大小”的论证。受限变形、任意步长排除仍是可复用测试；今后只有证明母空间位置和精确接口时才重启。[9/20 STATUS S6](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/STATUS.md)，[9/21 N07](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。

## F02 · 局部 resolvent 数据冒充完整原算子

- **尝试及机制**：只看 \(T|_U\) 的轨道和反射模，或以选中的 proximal step 残差代替 \(r_F(u)=\inf_{v\in F(u)}\|v\|\)，再在原对象上使用误差界／类别结论。
- **失败点**：域外完整图点仍可改变逆纤维和最小残差；proper/quotient 的 T-only 观测也不自动 category-preserving。**信息损失和缺少提升定理**，不是“全域 T 不决定 F”。
- **salvage / 重启条件**：固定步长的全域完整 \(T\) 可由 \(F(u)=\{(p-u)/\lambda:p\in\operatorname{dom}T,\ u\in T(p)\}\) 反演。可从一开始采用完整紧源 \(F_{T,K}\)，或证明局部图卡的保真及类别保持条件。[9/20 07_final_handoff §2, §5](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md)。

## F03 · 旧解选择稿把 \(J_{\mathcal G}\) 无条件升级为 \(J_{\lambda F}\)

- **尝试及机制**：用局部图块 \(\mathcal G\) 的收敛证明直接声称完整算子 resolvent 同样单值并具有全部模界。
- **致命反例**：\(F(u)=\{u,-u\}\)，\(\mathcal G=\{(u,u)\}\) 时 \(J_{\mathcal G}(x)=x/2\)，但 \(J_F(0)=\mathbb R\)。原量词版本错误。
- **salvage / 修补版本**：一般定理只陈述局部 \(T=J_{\mathcal G}\)，或另证共同轨道区域的完整纤维一致性；具体两个显式构造单独验证了完整 resolvent，故不受该一般接口漏洞牵连。[9/21 verified core §4](history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md) 与 [修订关闭包](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)。

## F04 · 普通完整图／\(C^0\) Baire 作为最终量尺

- **尝试及机制**：在中立无参数的宽图空间或普通一致收敛动力空间直接比较“多少对象”有 LT / RLEB 证书。
- **来源包报告的失败点**：局部完整连续 resolvent 类本身第一纲；粗糙近恒等扰动把全部正 Hölder 类一起判小。测到野生连续动力与正则动力的差，而不是两套认证的相对能力。
- **salvage / 重启条件**：将这些来源报告作为新母空间的待恢复反塌缩测试；当前不能作已证反定理调用；若要另用 Baire，应给非退化分母及结构上有理由的拓扑，并追齐原证明的精确图卡。[9/21 N05](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)；部分原审计文件本次未附。

## F05 · 原动力度量的“差集非 σ-upper-porous”目标

- **尝试及机制**：对 \((X_D,d_{\rm dyn})\) 的 \(\mathcal R_D\setminus(\mathcal L_D\cup\mathcal M_D)\) 证明绝对孔隙意义下不小。
- **来源包报告的反定理**：\(\mathcal R_D\subseteq\mathcal H_+\in\sigma\mathcal P^-\subseteq\sigma\mathcal P^+\)，差集作为子集也被判小；整个原目标在该环境中被否定。机制是正 Hölder 层可制造统一微观孔洞。
- **salvage / 重启条件**：保留所报告的负结论和量尺诊断；同一 \(X_D,d_{\rm dyn}\) 上的原目标与报告冲突，须先恢复精确定义与证明，或明确反驳该报告；摘要本身不是已证禁止门。若新度量／等价关系改变，须先解释其自然性并核验相应孔隙传递条件。原精确定义、常数和证明需从历史 PRO 包恢复。[9/21 N10](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。

## F06 · 其他量尺／结构捷径

| 路线 | 具体停点 | 保留的东西与重新尝试条件 |
| --- | --- | --- |
| 轨道小集理想 \(\mathcal J_{\rm orb}^B\) | 来源包报告 LT、RLEB 和差集同时小；比第一纲细仍无鉴别力 | 用作候选大小不变量的反塌缩测试，N08 |
| 可数紧包络 | LT 的闭无限维 Banach 球“大”来自远端无关自由度 | 新尺度须对该自由度稳定，N09 |
| 局部 germ 直接商 | 非Hausdorff排除Polish，但不自动排除Baire；[C177](research/canonical/topological_repair_obstructions.md#tr-germ)给多点平凡拓扑且仍Baire的精确商 | 分别核分离性和Baire性；不能借该例认证历史完整图/全时间空间，N06 |
| fixed-\(E\) Foran 修复 | 闭性不保证线性正则相交；[C178](research/canonical/topological_repair_obstructions.md#tr-intersection)给轴/抛物线反例，[C166](research/canonical/operator_profile_tools.md#op-nonattainment)给闭纤维残差不达 | 历史orbit-code/Poisson预算仍为来源报告，先恢复精确对象与原证明，再核 \(\forall U\exists V\)，N11–N12 |
| 为锥、Markov、RL 强设一个母定理 | 锥 MSCQ 缺同目标和反射接口，Markov \(\Psi\) 非 ordinary RL residual | 可统一叙事，数学定理保持独立，N04 |

表中 N 编号均指 [9/21 原 no-go ledger](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。网络、工具、审稿模型或编译失败均不在这里当数学反证。

<a id="f07"></a>
## F07 · “Polish”被当作给定度量完备

- **原尝试**：9/19 扩展稿 extensions_moduli_structure.tex 的随机推论仅写 \((\mathsf X,d_{\mathsf X})\) Polish；在期望距离收缩和 Dini 步长包络下证明几乎处处有限长度，然后用“completeness”推出空间内极限。
- **错误位置与性质**：Polish 若取拓扑可完备的标准含义，不保证**所指定** \(d_{\mathsf X}\) 完备。取 \(\mathsf X=(0,2)\) 通常距离，\(S=\{2^{-n}:n\ge1\}\)，确定性 \(X_k=2^{-(k+2)}+4^{-(k+2)}\)。令 \(D_k=4^{-(k+2)}\)，\(\omega(t)=4\sqrt t\)，\(\kappa=1/4,R=1/16\)；有 \(D_{k+1}=D_k/4\) 和 \(s_k\le[D_k+\omega(D_k)]/2\)，却 \(X_k\to0\notin\mathsf X\)。这是否定原**措辞的一个解释**的真实反例，不否定期望和 Dini 的求和计算。
- **salvage / 修补**：明示给定度量完备（可用 complete separable metric space），则稿内 Tonelli、有限长度、Cauchy 与闭 \(S\) 的证明链成立；不需另加 \(\omega\) 凹性。确定性 complete-metric transfer 本就明确完备，不受影响。[holder_structure H06](research/holder_structure.md)。

## F08 · 全局纤维实现误读为局部收敛认证

- **诱人的错误推论**：9/23 的 graph-maximal 全局 RL 可实现每个直径受限非空紧零集，于是把任意这类 \(K\) 当作也满足 9/19 局部收敛/极限回缩条件。
- **精确障碍**：9/19 的连续极限回缩需同图块全对模、局部 coverage、输出 EB、兼容、Dini 与不变开域；合取成立则 \(S\cap U\) 为 Euclidean neighborhood retract、局部可缩。Cantor 型紧集在其非孤立点不局部可缩，因此其全局实现不能在那些点同时满足这套附加条件。
- **salvage**：全局纤维分类与局部回缩结果都保留；这条跨稿条件限制可用来攻击某个给定实现的 EB/coverage，而不是宣称结构定理互相矛盾。[结构模块 H03/H05](research/holder_structure.md)。

## F09 · 将逐分支或物理步长当作混合律的真实残差

- **尝试及机制**：对随机近端核用 \(\sum_i p_iW_2(\mu,(T_i)_\#\mu)^2\) 或 \(\mathbb E\|X-T_\xi X\|^2\) 测量到不变律的距离，试图把它们直接代入混合核的 law-step EB。
- **精确失败点**：有限个有定点的 firmly nonexpansive 分支，其逐支推前残差零集仅是共同定点集支持的律。标量不一致双近端 \(T_\pm x=ax\pm(1-a)\)、\(0<a<1\) 有唯一混合不变律 \(\pi_a\)，两分支无共同定点；在平稳状态真实 law-step 为零，却有 \(\mathbb E|X-T_\xi X|^2=2(1-a)^2/(1+a)>0\)。这是**残差对象错误**，不否定混合核自身的线性 EB。
- **可回收成果与重启条件**：逐支残差精确检测共同固定点支持律；混合律用相同守恒边缘的 \(\mathcal R_\nu(\mu)=\mathsf W_\nu(\mu,\mu P)\)，其双边 EB 见 [RP-EB](research/canonical/random_proximal.md#rp-eb)。若要改用同步 OT 缺陷或普通 \(W_2\)，先独立证明零集和完整同对象桥；不得因为数值趋势相近而换残差。

<a id="f10"></a>
## F10 · 从算法收缩或单调性直接倒推原图误差界

- **原尝试**：由完整 \(J_{\lambda F}\) 严格收缩猜 \(F\) 强单调；或由 \(F\) 严格单调、cocoercive 且每条 PPA 轨道收敛猜存在趋零 gauge 的统一局部真残差 EB。
- **失败机制**：[EX01 旋转](research/canonical/example_atlas.md#ex01) 对任意 \(\lambda\omega>0\) 的完整 J 收缩因子 \((1+(\lambda\omega)^2)^{-1/2}<1\)，而单调内积恒为零。[EX02 无限维正紧对角](research/canonical/example_atlas.md#ex02) 对 \(x=te_n\) 有固定距离 \(t\) 而真残差 \(t/n\to0\)；每个固定有限迭代次数 \(k\) 的算子范数 \(\|J_\lambda^k\|_{\mathrm{op}}=1\)，尽管每个固定非零初值的轨道强收敛到 0。两例分别阻断不同的无条件逆推；后者依赖无限维尾方向。
- **可回收成果与重启条件**：旋转例仍有精确线性真 EB 和 PPA 速率；对角例仍逐点强收敛。新增定理需说明使谱隙、闭值域或原图几何联结起来的额外条件，并在相同空间和量词下证明；有限维截断不能作为对角例的反证。

## F11 · 同一图任意换步而保留全对 Hölder–RL

- **原尝试**：已知固定 \(\lambda\) 的全图 \(\gamma<1\) RL，直接宣称所有 \(\eta>0\) 仍有同类全对证书。
- **失败点**：用旧 Cayley \(C(s)=\operatorname{sgn}(s)|s|^\gamma\) 反生成同一完整图。新输入映射 \(Q=\alpha I+\beta C\) 在 \(\eta>\lambda\) 时折叠两旧输入，故新 Cayley 连单值都不是；在 \(0<\eta<\lambda\) 时虽可成为全局 Lipschitz，新反射无穷远线性增长，所有全局次线性 Hölder 指数仍失败。[PD-STEP](research/canonical/parameter_dictionary.md#pd-step)。
- **可回收成果与重启条件**：确切换步坐标、\(Q\) 单射判据与 \(\alpha-|\beta|L>0\) 时的 Lipschitz 充分界成立。任何新换步推广先核同图、自然域与目标 coverage；取逆或缩放值域是改变关系的另一操作。

<a id="f12"></a>
## F12 · 多步路径的逐词量词与非平凡周期

- **尝试与机制**：9/09 札记 §4 从每个合法词的幂指数 A_w>1 直接说有共同收缩半径；§3.4 将非平凡相位周期写作整轨道有限长度定理的推论。前者交换了“对每个词存在半径”与“存在半径对每个词”；后者忽略周期内不消失的位移。
- **精确反例**：无限一阶词取 C_j=1、A_j=1+1/j。各词在近零尺度都比线性小，但对任意固定 0<t<1，sup_j t^{A_j}=t，无法取统一 κ<1。T(x)=1−x 满足 T²=I，非中点的相位序列恒为两点周期；任何管控实际块内位移的 G(0)>0 使 Σ_qG(0) 发散。
- **salvage / 重新尝试条件**：[C31–C33](research/canonical/path_atlas.md) 将 universal-selection 前缀覆盖、统一位移预算和终点收缩合取；有限词集或 inf A_w>1 且 sup C_w<∞ 恢复统一幂结论；仅知块迭代收敛时用单独的相位连续性命题。历史 M1 捕获常数须从原生图重新核算，不能继承本修订的状态。旧来源见该模块 PA-SOURCE。

<a id="f13"></a>
## F13 · 不保秩地传递外层线性误差界

- **尝试与断点**：把 φ 的残差 EB 和 c(x̄)∈argmin φ 当作足以给 φ∘c 的同阶真实残差界，漏掉 Dcᵀ 对外层次梯度的统一下界与到目标的定量修复。
- **反例**：c(x)=x²，φ(z)=z²/2，x̄=0。外层 d(z,{0})=||∂φ(z)||；复合 F(x)=2x³，S={0}，不存在邻域常数 K 使 |x|≤K|2x³|。这证伪同阶线性传递，不证伪一切非线性 gauge。
- **salvage / 重启**：[C35 满秩版本](research/canonical/composite_subregularity.md#cs-eb) 用 σ>0 同时保证修复及真实残差；秩亏研究需原生乘子不抵消和临界方向条件，不能把待证的残差增长当前提。

<a id="f14"></a>
## F14 · M1 两步捕获被误当成缺乏一步距离收缩

- **原尝试与关键机制**：旧多步札记 §5 的显式 \(T\) 在端点附近两步进入线段零集，分别提取的反射指数 \(1/3\) 和输出 EB 指数 \(1\) 的乘积小于 1；因而曾用它支持“必须越过已有一步轨道定理”的扩大判断。
- **具体断点**：两个各自最坏的标量模没有保持同一状态的 \(s=a-3b\)。对**这个单值映射**，在 \(B_{1/(96\sqrt {10})}((2/3,0))\) 上实际已有锐一步距离因子 \(3/\sqrt {10}<1\)，[C39](research/topics/path_dynamics/m1_capture.md#m1-sharp) 给逐项证明。此前两步捕获结论本身仍成立；错误在于从标量证书失败推断一步几何失败或推出对现有轨道定理的严格分离。
- **可回收内容与重启门**：[C38](research/topics/path_dynamics/m1_capture.md#m1-capture) 保留显式两步捕获，联合活动关系比独立标量包络更强；它仍是研究原生路径证书的动机。要声称真正多值算法的每条选择或已有理论的严格排除，先恢复原始 `Sign` 图、证明输出与分支同一性，并逐项核旧定理前提。历史 9/09 多步札记与随后旗舰升级札记 §2 是此修订的版本谱系。

<a id="f15"></a>
## F15 · 从局部最小和驻点残差直接转到二阶目标

- **尝试与缺口**：只凭基点为局部极小，便把到驻点集 \(\Gamma\) 的残差论证用于更小的二阶目标 \(\Theta_2\)，遗漏附近其他驻点是否仍为目标。属于**目标集合不一致**，并非外层 gauge 的数值精度问题。
- **精确反例**：[C41](research/topics/composite_regular/oscillating_target.md#ot-maxima) 的 \(C^\infty\) 正函数在零点严格全局最小，却有 \(x_k\to0\) 的严格局部极大点。它们真残差为零，到完整 \(\Theta_2\) 距离为正；任意 \(\Psi(0)=0\) 的全邻域目标正确 EB 失败。驻点弱分离也恰好失效，因为 \(f(x_k)>f(0)\)。
- **salvage 与重启条件**：[C34](research/canonical/composite_subregularity.md#cs-transfer) 保留局部最小、弱分离与目标夹逼的正向距离一致性。若要在弱分离以外工作，需另证某种排除坏驻点的原生目标一致条件；不能把目标 \(\Theta_2\) 改成 \(\Gamma\) 后仍称解决原命题。

<a id="f16"></a>
## F16 · 把完整图全对 RL 和真 EB 当成输入覆盖

- **尝试与机制**：由完整图上的全对反射模、非空闭零集和实际图输出的真实残差 EB，断言零点附近所有输入存在 proximal 步，从而启动局部 PPA。
- **致命缺口**：[C47 / GX-074](research/topics/path_dynamics/discrete_coverage.md#dc-gap) 取紧图 \(K\times\{0\}\)，\(K=\{0\}\cup\{1/n\}\)。整个自然域 K 上每个 \(0<\gamma\le1\) 有全对 \(\mathrm{RL}(\lambda,\gamma,1)\)，在所有有限残差输出上 \(d(u,S)=r_F(u)=0\)，但任意零邻域有输入不在 K，完整 resolvent 的纤维为空。图闭性和全图量词都不能修复缺失的输入。
- **可回收成果与重启门**：图上的全对模和输出 EB 各自保留；要得到每个邻近输入的轨道，另证 \(V_0\subset\operatorname{ran}(I+\lambda F)\)，还需同一分支的输出留域、兼容及总长度预算。若目标从 \(S=K\) 改为 \(\{0\}\)，旧 EB 不再成立，这属于不同命题。此路线与 F02 的“局部图不保完整纤维”是两种独立的信息门。

<a id="f17"></a>
## F17 · 两个分离的最坏指数不能相乘为锐轨道阶

- **尝试与断点**：已知某些输入达到锚漂移指数 \(\theta\)，另一些图点达到残差 EB 指数 q，就断言指定映射的实际输出有锐 \(\theta q\) 阶。两个存在量词可指不同序列，且不保证选中步与锚距离同阶或这些序列都是合法近端输入。
- **可回收结论**：[C49](research/canonical/nonisolated_alignment.md#na-compose) 在整个共同输入家族的真 EB、小步门和统一锚模下给 upper \(\theta q\)；[C50](research/canonical/nonisolated_alignment.md#na-sharp) 再要求**同一**序列上 \(a_n/r_n^\theta\)、\(t_n/a_n\)、\(s_n/t_n^q\) 的三个正有限极限，才给相应的正归一化因子。旧 §9.1 也明确区分二者。没有同序列见证时保持上阶，不写“最优”。

<a id="f18"></a>
## F18 · 将移动输出锚的反射界改为固定锚或集合收缩

- **尝试与断点**：从 \(d(y,S)=o(\|w\|)\) 及 \(\widehat x\) 关于**输出附近选取的** \(p=p(y,w)\) 近似反射，推断任一固定 \(p_0\in S\) 的反射缺陷小，或推断 \(d(\widehat x,S)<d(x,S)\)。
- **反例与回收**：[MA-LIMIT](research/canonical/moving_anchor_reflection.md#ma-limit) 取线性零集 S 与在每个零点均含 0、\((1/n,1/n)\) 的关系。真残差与输出距离都为零，移动锚取 \(p=y\) 有零缺陷；固定 \(p_0=0\) 的相对缺陷却趋 2，集合距离反射前后相等。C51/C52 的点态界仍成立。
- **重启条件**：要谈固定锚，另控 \(\|p(y,w)-p_0\|\) 相对输入尺度；要谈集合距离收缩，另证最近点漂移、兼容和留域等针对**同一算法**的条件。只改锚的名称不是证明。

<a id="f19"></a>
## F19 · 将指定分支的锚定模升级为全对 RL

- **尝试与断点**：只控制每个输入相对其近似最近零点的 Cayley 偏移，并有真残差 EB 与收缩，于是想对任意两个输入断言同参数的全对 RL。锚定比较没有控制两个非零输入之间的振荡。
- **完整反例**：[C55](research/canonical/named_branch_local.md#nb-oscillation) 的完整关系由 \(T(x)=x[3/10+(1/10)\sin(x^{-2})]\) 反演。对零点锚有 \(\gamma=1,L=3/5\)，所有输出满足 \(|y|\le(2/3)r_F(y)\)，而 Cayley 导数沿 \(x_n=(2\pi n)^{-1/2}\) 无界，故任何零邻域的全对线性 RL 均失败。
- **回收与重启门**：[C53/C54](research/canonical/named_branch_local.md) 直接用 anchored 条件证明指定分支的有限长度及幂次上阶，无需全对升级。若目标是完整图上任意两点的模或所有完整 resolvent 分支，另证跨输入比较与完整纤维条件；本例不否定可能的较弱 Hölder 指数。

<a id="f20"></a>
## F20 · 全对图块与覆盖不足以生产完整零集的锚

- **尝试与断点**：由图块全对 RL、指定输入 coverage 直接推 C53 的锚定条件，忽略图块所含零图点 \(S_G\) 对完整零集 \(S\) 的距离是否保真。全对不等式只能拿同一个图块里的 \((p,0)\) 来比较。
- **反例**：[C57](research/canonical/all_pairs_verifier.md#av-gap) 的完整 \(F(y)=\{0,y\}\)、图块 \(G=\{(y,y)\}\) 满足 \(L=0\) 全对 RL 且满输入覆盖，但 \(S=\mathbb R,S_G=\{0\}\)。所有非零输入到 \(S\) 距离零而指定 \(T(x)=x/2\) 不固定，输出真 EB 仍成立；完整 J 同时含 \(x\) 和 \(x/2\)。
- **回收及重启条件**：[C56](research/canonical/all_pairs_verifier.md#av-bridge) 在 active set 上另加 \(d(x,S_G)=d(x,S)\)，便能以近似 infimum 构造锚，无须投影取到；之后真 EB、兼容、留域和完整排他各自另证。这里的反例不宣称该保距离条件是任何算法收敛的普遍必要条件。

<a id="f21"></a>
## F21 · 一般 gauge 的残差窗口被当作无窗口邻域界

- **尝试及断点**：窗口假设只检查 \(r_F(u)<\delta\) 的点；若直接把它用于邻域内全部有限残差，就必须控制阈值以上的 \(d(u,S)\) 与 \(\psi(r_F(u))\)。正幂有 \(\psi(\delta)>0\)，但允许的非减 gauge 可在残差 \(1\) 仍为零。
- **闭图反例**：[RW-FLAT](research/canonical/residual_window_bridge.md#rw-flat) 的完整闭图取 \(F(0)=\{0,1\}\)、\(F(u)=\{1\}\) 对 \(u\ne0\)，\(S=\{0\}\)、\(\psi(t)=\max\{t-2,0\}\)、\(\delta=1/2\)。窗口内只见零点；任意零邻域的非零点却有 \(r_F=1\)、\(\psi(r_F)=0<d(u,S)\)。这是量词及 gauge 阈值的漏洞，不否定窗口版原陈述。
- **可回收结果与重启门**：[C59](research/canonical/residual_window_bridge.md#rw-positive) 给出 \(\psi(\delta)>0\) 时缩至 \(B(\bar u,\psi(\delta))\) 的充分桥。若 gauge 只在 \([0,\eta)\) 定义，桥的无窗口结论只针对 \(r_F<\eta\)；改为全部残差须另定义全域 gauge。反例不满足额外全对 RL，因此不能被拿去否定加 RL 的特殊定理。

<a id="f22"></a>
## F22 · 闭的全局近端图与有限长轨道自动给不变极限或 law-step EB

- **尝试与断点**：把全局多值近端图的闭性当作任意指定选择核的弱连续性，遂由有限长物理轨道推极限律不变；再把真实 law-step 的精确零集自动升级为零点附近一致消失 gauge EB。图的闭性只管允许的**集合**，不管在 tie 点跳变的选择概率；exact-zero 只管残差恰零，不管趋零序列的紧性或逆连续性。
- **完整反例**：[C63](research/topics/random_markov/proximal_selection_seam.md#ps-example) 的固定二维 group-\(\ell_0\) 目标有闭完整全局 prox 图；fair tie 核沿 \(a_kv\downarrow v\) 有有限长度而 \(K(v)=\tfrac12\delta_0+\tfrac12\delta_v\)。唯一平稳律是 \(\delta_0\)，但每个完整 \(W_2\) 邻域可装入 \(\mu_k\) 使 \(\mathcal R(\mu_k)\to0\)、\(d(\mu_k,\delta_0)\to\sqrt{2\epsilon}>0\)。
- **回收与重启门**：[C62](research/topics/random_markov/proximal_selection_seam.md#ps-absorption) 的同一目标全局 prox 平稳吸收律仍成立，真 law-step 的零集仍是平稳律。要救极限不变性须核具体核在**该极限**的闭/连续传递；要救 EB 须限制真正排除上述质量稀释序列的律空间或加入定量逆界。改用随机换目标、同步 OT 残差或完整次梯度 resolvent 是新对象，不沿用本反例的真值。

<a id="f23"></a>
## F23 · 从同名 M1 显式外层映射认证历史原生 Sign 方程

- **尝试与断点**：历史多步 §5 给出 \(T(p,q)=(p-f(p-3q),0)\) 并称来自一个真正多值 Sign 广义方程，企图据此把显式 T 的两步捕获、锐一步界或真实残差赋给**历史原生循环算法的全部路径**。旧稿没有写出原生方程的完整图、每个相位与全部允许选择；另有同名 M1/SO-06 是不同的两分支 Minty benchmark，不能拼作来源。
- **诚实回收**：[C64 新构造](research/topics/path_dynamics/m1_sign_lift.md#sl-graph) 反向定义一个闭的完整多值 \(F_{\rm lift}\)，其全域单位步长 resolvent 恰为这个 T，并直接算零集及真残差。这只证明**存在一个** Sign 图实现；完整 J 若在全域预先等于 T，其图可反演唯一，但历史模型未证明是该完整 J，也可能是多相位组合。
- **重启条件**：恢复历史原生方程的完整定义、自然域、全部图值和每步相位/选择；逐输入检验它们与 T 的路径对应。缺任何一项则 C38/C39 只授给显式 T 或已经明确新定义的 \(F_{\rm lift}\)，不能写“原生多值桥已闭”。

<a id="f24"></a>
## F24 · 将两次最坏矩包络当作同耦合复合的锐界

- **尝试与断点**：对同一联合变量逐点已有 \(S\le CD^\gamma,D_+\le KS^q\)，却先各自对**所有**概率律取最坏 \(L^p\) 包络，再把两个标量函数复合，误以为其锐性可以在同一个分布上同时取到。
- **定量见证**：[C69](research/topics/random_markov/scalar_moment_envelope.md#sme-power) 在 \(0<\gamma<1,q>1,\gamma q=1,0\le D\le R\) 上：同一变量先复合再取矩是 \(KC^qt\)，分开取各自锐包络是 \(KC^qR^{1-\gamma}t^\gamma\)，比值 \((R/t)^{1-\gamma}\) 随 \(t\downarrow0\) 发散。两个“锐”极值可由不同概率律实现，不能拼成同一耦合的锐性。
- **回收与重启门**：若有同一合法耦合上的两条逐点证书和 \(D\le R\) 的实际硬支持，可先复合再积分；仅有 \(\|D\|_p\) 小无法调用局部 gauge。原生 Markov 更新仍需核目标边缘与可测耦合，抽象包络不代替这项存在性。

<a id="f25"></a>
## F25 · 全纤维线性收敛被逆推为完整图全对 RL

- **原尝试与断点**：从闭完整图、满 Minty 输入域、原算子和完整最小步的线性真 EB，以及**每条**近端选择路径的统一线性收敛，猜存在同一完整图块上任意两点的零消失反射模。轨道只控制实际输入与其可选输出相对零集的径向行为，没有排除同一输入的跨支碰撞。
- **精确反例**：[GX-075 新对象卡 C72–C75](research/topics/examples/diagonal_spike_relation.md#ds-rl) 的对角图并原点离散竖支具有上述全部性质，但两个趋零图点的 Minty 输入均为 \(\lambda/n\)、Cayley 输出不同，任何 \(\omega(0)=0\) 的全对 RL 即刻失败。零锚最优线性模 1 同时成立。
- **保留与重启**：该例的完整每选择有限长度、真残差和二参数区仍可独立调用。要恢复全对条件，另核同输入唯一性及跨输入的统一反射模；不能从动力收敛或选中锚定条件反推它。更换完整图或只取一支属于新命题。

<a id="f26"></a>
## F26 · 将最近逆点的线性模或半阶 MR 移植给其它正则轴

- **尝试与断点**：GX-076 的 \(d(0,\Theta^{-1}(y))=|y|\) 仅看最近逆点，不能断言全部逆点线性 calm，更不能断言以任意附近输入和目标为量词的线性 MR。相反 \(\Theta^{-1}(y)\) 对小正 \(y\) 含 \((0,\sqrt y)\)；\((0,t),y=0\) 给距离 \(|t|\)、残差 \(t^2\)，线性固定目标和两变量 MR 均失败。
- **保留及精确门**：[C76/C77](research/topics/examples/hemiregular_piecewise_parabola.md) 的最近逆点 HREG 线性锐模 1 与两变量半阶锐模 1 分别成立；负目标纤维端点不取到但距离可对闭包求。此映射 \(\mathbb R^2\to\mathbb R\) 没有本项目同空间 Cayley/RL 身份；原点连续也不提供参考点附近的局部闭图。若改用闭图版本或同空间嵌入，必须重建对象和量词。

<a id="f27"></a>
## F27 · 原算子零系数误差界移植给近端步残差

- **尝试与断点**：在完整 \(F=\partial|x|\) 上，非零点真原算子残差恒为 1，因输入邻域可缩，固定零目标线性 EB 的最优**局部系数下确界**为 0。若因此对 \(J_{\lambda F}\) 的 fixed-point 步残差声称系数 0，则改变了残差对象。
- **精确见证与回收**：[C78/C79](research/topics/examples/absolute_value_subgradient.md) 对每个 \(\lambda>0\) 给完整 \(J(p)=\operatorname{sgn}(p)(|p|-\lambda)_+\)；\(|p|<\lambda\) 时 \(d(p,\operatorname{Fix}J)=|p-J(p)|=|p|\)，步 EB 的锐局部系数是 1。原算子逆像局部钉住与一步终止依然同时成立，但两种常数不能相互替换。若 gauge 只定义在残差小于 1 的窗口，原算子窗口只剩零点，须另列真空范围。

<a id="f28"></a>
## F28 · 受限图的一步证书被授给完整母图或无限轨道

- **尝试与断点**：GX-032 先给 \(F_\infty(x)=-\sqrt x\) 的半直线母图，再在 \(U=[0,1/16]\) 截取 \(\Gamma\)。若把短支逆图公式称为母图完整 resolvent，便漏掉母图从输入 0 到输出 1 的远支；若由受限 \(L=3\)、真二次 EB 和一步 \(O(p^2)\) 猜无限二次收敛，便漏掉下一输入是否仍在受限自然域。
- **精确反证**：[C85/C86](research/topics/examples/restricted_root_graph.md#sr-escape) 在受限 \(F_U\) 中给 \(D_U=[-3/16,0]\)、每个非零输入的输出 \(J(p)>0\notin D_U\)，没有非零合法第二步。[C87](research/topics/examples/restricted_root_graph.md#sr-parent) 对真正完整的 \(F_\infty\) 给 \(J(0)=\{0,1\}\)，同输入不同反射输出使零消失全对模失败；非零完整路径向 \(+\infty\)。
- **可回收与重启门**：受限图三项锐成对常数、真二次输出 EB 和锐一步比值都独立成立。任何轨道定理须逐步证明指定输入域不变和完整纤维排他；任何母图断言须重新对全部远支检验。扩大原关系是改变对象，不是为受限证书补一个推理步骤。

<a id="f29"></a>
## F29 · 大零集上的真空固定目标 EB 被当作扰动目标正则性

- **尝试与断点**：只因完整关系 \(F=N_B\) 在参考零点的固定目标 MSR 系数下确界为 0、全域反射非扩张，便推原关系有任意正指数两变量 MR/HREG 或 inverse Aubin。固定目标在 \(\operatorname{dom}F=B=S\) 上两边均零，域外残差为无穷，完全没有测量非零目标的逆像跳变；全邻域的 \(0\cdot\infty\) 还需约定，故只称系数**下确界** 0。
- **精确反例**：[BN-REGULARITY](research/topics/examples/ball_normal_cone.md#bn-regularity) 对每个边界 \(e\in\partial B\) 取 \(y=-te\to0\)：\(F^{-1}(y)=\{-e\}\)，\(d(e,F^{-1}(y))=2\)，而 \(\|y\|=d(y,F(e))=t\)。内部参考点的非零目标逆点也立即跳到球面。因而每个参考零点的两变量及固定输入正指数界失败；逆 Aubin 取 \(e\in F^{-1}(0)\) 同样失败。
- **回收与重启门**：完整法锥的全图二参数区和锐 \(L=1\) 反射非扩张仍成立；固定目标系数下确界 0 仍是诚实但真空的陈述。要得到有内容的 EB，先说明非孤立零集、域外残差、目标扰动和输入 coverage 的同一规范；改零集或引入其它残差须另立命题。

<a id="f30"></a>
## F30 · 锐全局逆像界被误读为 rectangularity 或反射严格收缩

- **尝试与断点**：把完整、极大且严格单调的全域线性图的全局 MR 常数 1，当作正 cocoercivity、rectangularity 或同一步长全对反射 \(L<1\) 的证书。逆像界控制 \(\|F^{-1}\|\)，等价地控制 \(F\) 的下奇异值；它不管 \(\langle h,Fh\rangle/\|Fh\|^2\) 在高维尾部趋零。
- **完整见证**：[C102/C103](research/topics/examples/skew_compact_diagonal.md#scd-inverse) 的 \(F=D+B\) 有 \(\|F^{-1}\|=1\)、所有目标完整单值逆像、全域近端严格收缩，但高块使正 cocoercivity 模为零、反射锐 \(L=1\)。对 \(x=0,v=(1/n)_n\in\operatorname{ran}F\)，有限支撑 \(z^{(N)}\) 又直接给 rectangular 条件的配对下确界 \(-\tfrac14\sum_{n\le N}1/n\to-\infty\)，无需导入旧稿所用外部等价命题。
- **回收与重启门**：全局真逆像界、每条近端几何收敛和极大单调各自成立。要得正 cocoercivity 或反射严格模，须另证同一完整图的内积下界相对 \(\|Fh\|^2\) 或相应 Cayley 严格界；有限块上的正系数不可无条件统一至 \(\ell^2\)。

<a id="f31"></a>
## F31 · 逐向量严格下降被当作统一近端收缩

- **尝试与断点**：在完整 Volterra 图上，由 \(\|J_\lambda p\|<\|p\|\) 对每个非零 \(p\) 断言存在一个共同 \(c<1\)，或由每个轨道强趋零断言有限时间的一致收敛率。逐点的严格不等式并无单位球紧性，高频方向可任意接近不动方向。
- **精确见证**：[C105](research/topics/examples/volterra_integration.md#vo-prox) 对每个固定整数 \(k\ge1\) 给 \(\|J_\lambda^k\|_{\rm op}=1\)，而由能量、稠密值域另证 \(J_\lambda^kp\to0\) 对每个固定 \(p\) 强成立。同一高频序列分别否定真算子残差和近端步残差的任何统一消失 gauge EB；两种残差不能互换。
- **可回收与重启门**：极大单调、全域完整近端、全对反射锐 \(L=1\) 和逐轨道强收敛均保留。要给统一速率或误差界，须增加可独立验证的频率一致性、闭值域/逆界或更强的共同模；有限维截断的常数不自动统一到 \(L^2\)。

<a id="f32"></a>
## F32 · 把负三次图块的单值近端称作完整近端

- **尝试与断点**：在 \(3\lambda M^2<1\) 的负三次短图块得到全对线性 RL 和单值 \(T_M\)，便断言完整全域关系 \(F(x)=-x^3\) 的 \(J_{\lambda F}\) 也单值、全对，或据一步图块界推出无限路径。完整零输入同时有 \(0,\pm\lambda^{-1/2}\) 三个输出；图块非零合法路径又有限步离开其自然输入域。
- **回收与重启门**：[C106/C107](research/topics/examples/negative_cubic_branch.md#nc-object) 的图块锐常数、固定零目标真 \(1/3\) EB 与完整逆像两目标 \(1/3\) 模各自成立，后两者和正三次 EX03 有符号对应。要研究完整算法的全部选择，须保留远支并逐步验证完整纤维；要延长指定短分支，需新不变域证明，不能仅把图块扩大名称。

<a id="f33"></a>
## F33 · 零系数真残差或严格近端模被当作非零无限路径

- **尝试与具体断点**：GX-055 极点图在所有固定目标正幂上有局部 EB 系数下确界 0；当 \(\lambda>2\varepsilon^2\)，完整 J 在**自身自然域**还有锐 Lipschitz 模小于 1。若据此声称非零初值存在无限 PPA 路径，便漏掉输出仍可作下一输入的留域条件。此步长的自然域除 0 外只含负输入，而全部非零近端输出为正，第一步后立即无合法续步。\(\lambda<\varepsilon^2\) 虽有零输入球，却在 0 有完整双输出，所有极点支路径也有限步离域。
- **可回收与重启门**：[C108/C109](research/topics/examples/isolated_pole_relation.md#ip-minty) 的全步长锐全对模、完整 J Lipschitz 模、残差逃逸及路径分类分别成立。固定目标零系数是缩窗下确界，不是字面零常数；图闭与零点图孤立也不产生非零小残差输出。若要收敛定理，先在**同一完整 J 或已命名分支**上证明输入 coverage、自映射留域及兼容，不能只比较一阶模。

<a id="f34"></a>
## F34 · 旋转族的循环阶被误说成不能由其强模还原

- **原断言与范围**：Z07 GX-063 第 902–905 行将 GX-062 与 GX-063 的循环阶差异，解释为“不能还原到标量强单调模”。它们的完整逆像模确实都等于 1，但强单调系数分别为 \(1/2\) 与 \(1/\sqrt2\)，并不相同。
- **断点与修补**：在**这个**全域平面旋转族中 \(\mu=\cos\theta\)，而 [C123](research/topics/examples/planar_rotation_family.md#pr-cyclic) 的完整 Fourier 证明给 \(n\)-循环单调恰当且仅当 \(\mu\ge\cos(\pi/n)\)。因此族内的循环阶可以从该标量还原；可保留的比较只涉及同逆像条件数而不同循环阶。
- **边界**：这不证明一般算子只凭强单调系数就能识别循环阶。若在更广的图类重新提出“不可还原”，必须给同强模而循环性质不同的两个完整对象，并固定该模的精确定义。

<a id="f35"></a>
## F35 · 把 QP 输出 gap 直接加到反演总误差

- **尝试与断点**：旧 [Q03 摘要](research/range_finite_data.md#q-eval) 先用 \(e\) 表示候选参数 \(q\) 处 \(\|\widehat N(q)-N_m(q)\|\)，随后把同一个 \(e\) 直接加进 \(\|x-\widehat x\|\) 的三项界。前者仅是代理函数一次求值的误差；后者要求 \(\|\widehat x-A_m^{-1}(\widetilde v)\|\le e_x\)。漏掉候选点的固定点残差及 \(1/(1-\sigma)\) 放大。
- **精确反向检验**：即使 \(N_m(q)\) 完全精确、\(e_N=0\)，也可任意选择远离 \(A_m^{-1}(\widetilde v)\) 的候选 \(q\)，使 \(\widehat x=q-\lambda\widetilde v\) 很远；只由 gap 无法约束它。若 \(\lambda=1,F=I,C=0\)，单个零样本可取 \(N_m=0\)，\(v=\widetilde v=0\)，取 \(q> K_0\) 就使旧读法 \(\|0-q\|\le K_0+0+0\) 失败，其中 \(K_0=a/\sqrt{1-\sigma^2}\)。
- **可回收与重启门**：S23 原稿 `prop:evaluation` 与 `cor:totalerror` 分别给正确的两种误差门，并未被此反例否定。取 \(\widehat x=q-\lambda\widetilde v\)，先认证 \(e_N\)，再用 \(e_x=(\|q-2\lambda\widetilde v-\widehat N(q)\|+e_N)/(1-\sigma)\)；最后在完整逆纤维的共同 coverage 与观测噪声门下调用 [C20/Q03](research/range_finite_data.md#q-total)。这里修的是规范层缩写的类型错位，不是声称原稿定理错误。

<a id="f36"></a>
## F36 · 局部 RL 被用于测试尺度外的有限数据点对

- **尝试与断点**：旧 [C20-v1](CLAIMS.md#c20-v1) 允许局部 RL，只要求未知 Cayley 参数到样本的距离不超过 \(\delta\)，便在 Q02 中用 \(\|c-c_i\|\le L\delta^\gamma\)。但局部 \(\mathrm{RL}(\lambda,\gamma,L;R_0)\) 只对**同一认证图上、参数对距不超过 \(R_0\)** 的图点对成立；覆盖半径 \(\delta\) 本身不是这项证书。
- **完整反例**：在 \(\mathbb R\) 取 \(\lambda=1,\gamma=1/2,L=1,R_0=1\)，完整图恰为 \(\{(0,0),(51,-49)\}\)。两点的 Cayley 参数为 \(p=0,2\)，反射参数为 \(c=0,100\)，故局部 RL 对所有被测试的同点对成立，而跨点对在尺度外。只采样 \((0,0)\)，取 \(\sigma=1/2\)，则 \(M_\sigma=\sup_{t\ge0}(t-t^2/4)=1\)、\(a^2=1/2\)；单样本 QP 给 \(N_m=0,A_m=I\)。未知点参数被 \(\delta=2\) 覆盖，旧公式给 \(K_2<5\)，实际 \(\lambda|v-A_m(x)|=|-49-51|=100\)。全部样本兼容条件都真，失败仅来自越过局部成对尺度。
- **可回收与重启门**：[C20-v2/Q02](research/range_finite_data.md#q-cover) 保留原稿全图全尺度情形，并允许严格声明的局部版：样本与未知点属于同一 RL 图，每个使用的参数点对在证书尺度内（\(\delta\le R_0\) 是充分门）；要对完整逆纤维结论，须逐个覆盖**所有完整纤维图点**且它们属于该图。此反例不反驳 S23 的全尺度证明，也不把局部证书自动扩成全图性质。

<a id="f37"></a>
## F37 · 有限纤维的正选择条件被用于全部近端纤维

- **尝试与断点**：固定目标全局近端的主吸收等价只涉及指定核的吸收集 \(A_K=\{x:K(x,\{x\})=1\}\)。旧 [C62-v1](CLAIMS.md#c62-v1) 只要求**有限多值**纤维的各成员获正概率，却对所有输入断言 \(A_K=\{x:P_\lambda f(x)=\{x\}\}\)；无穷纤维允许核恒选输入本身。
- **完整反例**：在 \(\mathbb R\) 令 \(\lambda=1\)，\(f(y)=-y^2/2\) 对 \(|y|\le1\)，其余为 \(+\infty\)。目标函数在 \([-1,1]\) 上是 \(-xy+x^2/2\)，故 \(P_1f(0)=[-1,1]\)，对非零 \(x\in[-1,1]\) 则 \(P_1f(x)=\{\operatorname{sign}x\}\)。取 \(K(0)=\delta_0\)，其余输入选唯一解；所有有限纤维都满足正选择，而 \(0\in A_K\) 且 \(P_1f(0)\ne\{0\}\)。
- **回收与重启门**：[C62-v2](CLAIMS.md#c62-v2) 的 \(\pi K=\pi\iff\pi(A_K)=1\) 仍由同一目标的严格下降证明；纤维等式需对**每个**输入要求完整纤维有限并逐成员正概率，或另给每个纤维足以排除额外最小解的全支撑条件。二维 fair-tie 模型的纤维确为有限集，其后续结论不受影响。

<a id="f38"></a>
## F38 · 锚包络的指数与趋零步长被隐含调用

- **同一完整证人**：在 \(H=\mathbb R,\lambda=1,S=\{0,1\}\) 上取 \(x_n=1/n\)（\(n\ge8\)），\(D=U=\{x_n:n\ge8\}\)，指定 \(Jx_n=y=5/4\)。令完整关系在这些相关点上为 \(F(0)=F(1)=\{0\}\)、\(F(5/4)=\{x_n-5/4:n\ge8\}\)，其它纤维为空。于是 \(w_n=x_n-5/4\in F(y)\)，\(r_F(y)=9/8\)，\(r_n=d(x_n,S)=x_n\)，\(P_S(y)=\{1\}\)，\(a_n=1-x_n\)，\(t_n=5/4-x_n\)，\(s_n=d(y,S)=1/4\)。取 \(\psi(t)=t^2/4\) 定义于 \([0,3)\)，则 \(s_n=1/4\le\psi(9/8)=81/256\)、\(\psi(t_n)\le t_n/2\)，且 \(\psi(t)=o(t)\)。全部指定步均在此真 EB 和小步窗口内。
- **C49-v1 的断点**：对 \(r_0=1/8,K=1/8,\theta=-1\)，包络 \(\mathcal A(r)\le1\le K/r\)（\(0<r\le r_0\) 且家族非空）；端点 \(2Kr_0^{-1}=2<\eta_\psi=3\)。旧推论却对所有更小 r 写 \(\psi(2K/r)\)，当 \(r\le1/12\) 时其输入 \(\ge3\) 已越出 gauge 定义域。\(\mathcal A(r)\le Kr^\theta\) 只排除 \(\theta>1\)，不自动给 \(\theta>0\)。
- **C50-v1 的断点**：同一模型取 \(\theta=0,q=2\)，则 \(a_n/r_n^0\to A=1\)，\(t_n/a_n\to B=5/4\)，\(s_n/t_n^2\to C=4/25\)，三项比值均为正，\(r_n\to0\)，C49 的实际小步与 \(\psi=o(t)\) 也成立，但 \(t_n\to5/4\ne0\)，所以 \(B\ne1/\lambda\)。比值乘积 \(CB^qA^q=1/4\) 仍正确。
- **回收与重启门**：[C49-v2](CLAIMS.md#c49-v2) 对包络推论另取 \(K>0,\theta>0\)，端点门便控制所有更小半径；逐点 NA-3 无需此幂假设。[C50-v2](CLAIMS.md#c50-v2) 的乘积仍为代数恒等式，只有在 \(t_n\to0\) 时由 NA-4 和 \(\psi=o(t)\) 进一步推出 \(B=1/\lambda\)。

<a id="f39"></a>
## F39 · 增长步长的上界被当作速率下界

- **旧断言**：9/01 算法记录把 \(q\)-次正则 PPA 的 \(\lambda_k=O(k^s)\) 用于依赖 \(s\) 的加速率；特别 \(q=1/2,s=2\) 的历史第 (iii) 式预言 \(d_k=O(k^{-3/2})\)。这里审查的是**该量词版本**，不判断外部论文的勘误状态。
- **完整反例**：在 \(\mathbb R\) 取全域 \(F(x)=x|x|\)，它连续单调，故极大单调；\(S=\{0\}\)，\(r_F(x)=|x|^2\)，所以固定零目标有精确 \(d(x,S)=r_F(x)^{1/2}\)。取 \(\lambda_k=1\)，它属于 \(O(k^2)\)；任意正初值的完整 PPA 递推为 \(x_k=x_{k+1}+x_{k+1}^2\)。序列趋零且 \(1/x_{k+1}-1/x_k=1/(1+x_{k+1})\to1\)，从而 \(x_k\sim1/k\)，并非 \(O(k^{-3/2})\)。
- **回收范围**：现行 [C02](CLAIMS.md) 和 [C53](research/canonical/named_branch_local.md#nb-local) 使用已固定的步长和明确兼容，不调用此旧增长命题。把旧 \(O\) 改为 \(\Omega\) 或 \(\Theta\) 后仍须独立重审原定理的其他前提与速率，不能凭本反例宣布修正版成立。

<a id="f40"></a>
## F40 · 任意度量空间的 \(q>1\) MR 被说成必退化

- **旧断言与范围**：9/01 正则性记录把“two-variable \(q>1\) MR 只可能局部常值型”写进任意度量空间设置；从赋范空间线段细分得到的直觉不能无条件移植到任意输出度量。
- **全域反例**：任取 \(q>1\)，令 \(X=(\mathbb R,|\cdot|)\)，\(Y=(\mathbb R,|\cdot|^{1/q})\)，\(F:X\to Y\) 为恒等映射。雪花指数 \(1/q\in(0,1)\) 给合法度量，且对所有 \(x,y\) 有 \(d_X(x,F^{-1}(y))=|x-y|=d_Y(y,F(x))^q\)。这是非局部常值、系数 1 的全域 two-variable \(q\)-MR。
- **回收范围**：现行 [D04](research/foundations.md#d04) 的固定零目标真残差 EB 不是此处的 two-variable MR。若重提赋范/长度空间退化命题，须另立 inverse localization、值域与路径几何的精确假设及证明；本例只反驳旧任意度量版本。

<a id="f41"></a>
## F41 · 紧源新图直接充当极大单调子类成员

- **尝试与关键机制**：用 C132 的紧源 \(K\)、连续 \(U:K\to K\) 和新定义完整 \(F_{U,K}\) 保真记录轨道与真实逆纤维，然后把这张图直接当成三类比较中**极大单调子类的一员**，或把母空间完全限定为这样的紧图而仍要求极大单调子类非空。
- **断点**：这张图是紧的。非零 Hilbert 空间中，任何非空紧图或本身不单调，或可在有界图外加一个仍与全图单调的点；[C142](research/operator_space.md#os-compact-barrier) 给出不依赖 Minty 定理的统一加点证明。因此紧源图本身不能极大单调。它的完整近端自然输入域仅为 \(K\)，不能靠换一个“母空间”名称获得环境满输入覆盖。
- **保留与重启门**：C132 的紧逆纤维极小值和真 EB 对这张**新图**仍成立。若希望嵌入非紧或极大单调关系，需显式给出延拓、同一空间的类谓词与拓扑，并重审完整纤维、最小残差及证书；简单加图点可能改变它们。共同母空间仍可同时容纳紧图和非紧的极大单调图；本障碍不证明不存在任何可用的自然完整母空间，也不解决总体规模比较。


<a id="f42"></a>
## F42 · AGM 的共同快尾与线性真 EB 被拼成严格兼容

- **同一完整对象**：[C146](research/topics/examples/arithmetic_geometric_mean.md#agm-object) 的F=G⁻¹−I，完整近端输入域P，工作窗W_R=[0,R]²。闭半代数完整图、唯一近端、半阶全对反射、线性真EB及共同几何点尾均直接成立。
- **断点**：[C148 / AGM18–20](research/topics/examples/arithmetic_geometric_mean.md#agm-compatibility) 用同窗输入(c,δ),(c,0)迫使ω(δ)≥√(cδ)，轴上实际输出又迫使非减EB gauge ψ(h)≥h/√2；兼容比值至少√c/(2√2√δ)而发散。换安全常数无法产生κ<1。
- **保留与重启门**：[C147](research/topics/examples/arithmetic_geometric_mean.md#agm-selection) 的共同几何尾和坏极限选择保持成立，正初值Q二次却不跨坏轴统一。若改变量、提升、完整关系或工作窗，须重新核全纤维、真残差和同窗全部点对；本条不排除这些新对象，也不否定其它收敛证明。

<a id="f43"></a>
## F43 · 仅凭超线性 gauge 就不重标度地跨 Minty 坐标

- **被否定的接口**：同一 graph germ 的 |y−p|≤ψ(‖w‖)、ψ=o(id)，就推出某个有限 C 的 |y−p|≤Cψ(‖y+λw−p‖)。
- **完整见证**：[C159](research/canonical/gauge_dilation_boundary.md#gd-theorem) 固定 λ=1；完整紧图上真实残差 EB 取等，但 xₙ=tₙ−tₙ² 处 ψ(xₙ)=tₙ⁴，|J_Fxₙ|/ψ(xₙ)=tₙ⁻²→∞，任意缩小 germ 仍失败。
- **重启门**：保留正确的 ψ((2/λ)‖x−p‖)，或另证所需固定 dilation 控制。正点连续 gauge、邻域输入 coverage、原生 PPA 等额外要求须另核；本例不认证它们。

<a id="f44"></a>
## F44 · P16 的负起步索引公式被原样移植为共同尾

- **指定旧接口**：arXiv1412.2997v1 Theorems1–2及正式版 Theorems3.2–3.3 的打印 n₀=ceil log₂[(e^(Kd)−1)/(e^ℓ−1)] 没有夹到非负；小非零直径下 n₀→−∞。读取原页只认证打印事实，不认证该公式在全部初值上成立。
- **解析反例**：[QA-FIRST-ROUND](research/canonical/selection_quasi_arithmetic_boundary.md#qa-first-round) 取合规 f±(t)=e^(±t)、K=1、初值(d/2,−d/2)。实际 d₁=2log cosh(d/2)∼d²/4，原合法 n=1 的尾却是 o(d²)；优化式在任何固定超过其极限起步阈值的整数 n 同样与 dₙ∼4^(1−2ⁿ)d^(2ⁿ) 矛盾。只否定指定打印公式的小直径量词，不否定作者全部结果或宣称正式勘误。
- **已闭修补**：[C160](research/canonical/selection_quasi_arithmetic_boundary.md#qa-uniform-tail) 先固定共同K,D及ℓ<1/α，使用 N=max(0,ceil(...))；另独立证明共同超几何尾与同域Lipschitz选择界，处理首步和退化情形。固定正AGM窗的结论不移到坏轴，编码成完整PPA仍须另验。
<a id="f45"></a>
## F45 · 全部图值界被无条件换成同 gauge 真残差界

- **尝试/断点**：对完整图每个v∈F(u)都有d(u,S)≤ψ(‖v‖)，直接把范数换成r_F(u)=inf‖v‖。一般非减且原点连续的ψ在正点可右跳，Hilbert闭纤维也可不取到inf。
- **完整反例**：[C166 OP3–5](research/canonical/operator_profile_tools.md#op-nonattainment)固定强闭ℓ²图、完整S={0}、r(e0)=1不达及ψ(t)=0(t≤1),1(t>1)。全部图值界成立、真EB失败。
- **salvage/重启门**：总可得ψ(r+)，逐输出取到或该残差处右连续足够恢复同ψ；有限定义域的上端点另核。紧源C132已经有极小值取得，未被反例否定；不同的窗口桥C59身份保持。

<a id="f46"></a>
## F46 · 宽母空间的第一纲不能自动传到算法或共同尾子层

[C179](research/canonical/attouch_wets_fixed_input_thinness.md#aw-boundary)在有限维宽AW空间证明固定λ、固定输入的可解类第一纲；限制到已经要求该输入可解的算法层后，该事件成为整个子层。不可数实步长的并也不能由可数并法推出第一纲。

[C180](research/canonical/uniform_holder_thinness.md#uht-boundary)在精确FixS的一致映射空间证明全部正Hölder并类第一纲；但K=[−1,1]、S={0}、e_n=0(n≥1)的共同尾层只含T=0，Hölder类在它内就是全空间。重启须证明同一实际子层中的扰动保持，或给确切范畴转移；两个不同母空间的薄性不构成总体RLEB–LT–极大单调比较。

<a id="f47"></a>
## F47 · 满Minty输入与非空零集被当成无限维正反满纤维

- **指定失败接口**：将有限维C04的必要性只凭全图全尺度Hölder–RL、固定参数图极大、闭图和非空零集推广到无限维Hilbert；满近端输入并不是I±C分别满射。
- **完整反例**：[C183 / IF3–6](research/canonical/infinite_fiber_boundary.md#if-counterexample)对每组λ,L>0、0<γ<1给同预算ℓ²完整图、全部输入单值J、精确单点零集，但F(ae₁)=∅与F⁻¹(ae₁/λ)=∅。非扩张前提实际失败：两个指定输入的输出距离比为√2。
- **保留与重启门**：有限维C04与任意HilbertC03仍成立。增加同一C原范数下非扩张，C184可在任意Hilbert恢复全部纤维非空闭凸弱紧；球投影仍反驳无限维范数紧性。换图、等价范数或外部328的未验收Banach定理不能默补原对象门；轨道EB/兼容和总体比较另证。

<a id="f48"></a>
## F48 · 允许所选值的 EB 被误当成完整真残差 EB

- **尝试及断点**：从允许转移的 d(y,S)≤ψ(||v||)，仅加完整残差取到或 ψ 连续就替换为 ψ(r_F(y))。允许集合可能漏掉完整纤维的更小图值；C166 的全图值前件没有得到。
- **同对象反例**：[C185 边界](research/canonical/allowed_transition_local.md#at-boundaries)取 ℝ、λ=1、F(y)={y,3y}、S={0}，只允许 y=x/4,v=3x/4。ω(t)=t/2、ψ(s)=s/3、κ=1/4 给全域 coverage、逐步锚界、所选 EB、有限长和严格留域，但取到的完整 r_F(y)=|y| 在全部非零输出都使真 EB 失败。
- **可保留及重启门**：C185 的全部允许轨道结论仍成立。反向桥须控制全部完整纤维，或明给允许范数极小值／满足界的近极小允许序列并核 gauge 右连续。F45 的不达/右跳障碍处理全图值界，是另一个不能省略的门；两者不能互相替代。
