# Failed Routes / Obstructions

这些卡片保存**失败的精确目标和机制**。9/21 v0.9 的历史 SOURCE-MISSING 不能原封不动当作当前状态：I-001 历史包 100/101 项已展开、I-002/I-003–005/I-059 已恢复，I-075 专题包以展开内容恢复；I-097–099 与 I-102 仍未在盘点文件名中发现。I-005 是审计任务书，不是审计报告。未重构原证明的 N05/N10 仍标“来源包报告”；详情见 [来源谱系](research/SOURCES.md) 与 [no-go ledger](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。一种量尺在一个空间失败，不是整个比较问题不可能。

## F01 · 以单个 cusp / 仿射漂移层代替总体覆盖

- **尝试及机制**：构造严格 RLEB、所有正步长排除 LT 的算子，或在预置超吸引／尖点的比较层内证明 LT 第一纲；希望推广到自然完整原图母空间。
- **失败点**：特殊层可以是 Baire 且在自身余稀，却在母空间第一纲或位置未知；固定证书指数、局部缩域和精确同尾的量词并未自动保留。属于**总体推广逻辑缺口**，不是受限构造被反例否定。
- **排除范围与 salvage**：排除“一个例子/层内 residual 就完成总体大小”的论证。受限变形、任意步长排除仍是可复用测试；今后只有证明母空间位置和精确接口时才重启。[9/20 STATUS S6](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/STATUS.md)，[9/21 N07](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。

## F02 · 局部 resolvent 数据冒充完整原算子

- **尝试及机制**：只看 \(T|_U\) 的轨道和反射模，或以选中的 proximal step 残差代替 \(r_F(u)=\inf_{v\in F(u)}\|v\|\)，再在原对象上使用误差界／类别结论。
- **失败点**：域外完整图点仍可改变逆纤维和最小残差；proper/quotient 的 T-only 观测也不自动 category-preserving。**信息损失和缺少提升定理**，不是“全域 T 不决定 F”。
- **salvage / 重启条件**：固定步长的全域完整 \(T\) 可由 \(F(u)=\{(p-u)/\lambda:Tp=u\}\) 反演。可从一开始采用完整紧源 \(F_{T,K}\)，或证明局部图卡的保真及类别保持条件。[9/20 07_final_handoff §2, §5](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md)。

## F03 · 旧解选择稿把 \(J_{\mathcal G}\) 无条件升级为 \(J_{\lambda F}\)

- **尝试及机制**：用局部图块 \(\mathcal G\) 的收敛证明直接声称完整算子 resolvent 同样单值并具有全部模界。
- **致命反例**：\(F(u)=\{u,-u\}\)，\(\mathcal G=\{(u,u)\}\) 时 \(J_{\mathcal G}(x)=x/2\)，但 \(J_F(0)=\mathbb R\)。原量词版本错误。
- **salvage / 修补版本**：一般定理只陈述局部 \(T=J_{\mathcal G}\)，或另证共同轨道区域的完整纤维一致性；具体两个显式构造单独验证了完整 resolvent，故不受该一般接口漏洞牵连。[9/21 verified core §4](history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md) 与 [修订关闭包](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)。

## F04 · 普通完整图／\(C^0\) Baire 作为最终量尺

- **尝试及机制**：在中立无参数的宽图空间或普通一致收敛动力空间直接比较“多少对象”有 LT / RLEB 证书。
- **来源包报告的失败点**：局部完整连续 resolvent 类本身第一纲；粗糙近恒等扰动把全部正 Hölder 类一起判小。测到野生连续动力与正则动力的差，而不是两套认证的相对能力。
- **salvage / 重启条件**：保留这些塌缩定理作为新母空间的反例测试；若要另用 Baire，应给非退化分母及结构上有理由的拓扑，并追齐原证明的精确图卡。[9/21 N05](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)；部分原审计文件本次未附。

## F05 · 原动力度量的“差集非 σ-upper-porous”目标

- **尝试及机制**：对 \((X_D,d_{\rm dyn})\) 的 \(\mathcal R_D\setminus(\mathcal L_D\cup\mathcal M_D)\) 证明绝对孔隙意义下不小。
- **来源包报告的反定理**：\(\mathcal R_D\subseteq\mathcal H_+\in\sigma\mathcal P^-\subseteq\sigma\mathcal P^+\)，差集作为子集也被判小；整个原目标在该环境中被否定。机制是正 Hölder 层可制造统一微观孔洞。
- **salvage / 重启条件**：保存负定理和量尺诊断；不再用同一 \(X_D,d_{\rm dyn}\) 重提原目标。若新度量／等价关系改变，须先解释其自然性并核验相应孔隙传递条件。原精确定义、常数和证明需从历史 PRO 包恢复。[9/21 N10](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。

## F06 · 其他量尺／结构捷径

| 路线 | 具体停点 | 保留的东西与重新尝试条件 |
| --- | --- | --- |
| 轨道小集理想 \(\mathcal J_{\rm orb}^B\) | 来源包报告 LT、RLEB 和差集同时小；比第一纲细仍无鉴别力 | 用作候选大小不变量的反塌缩测试，N08 |
| 可数紧包络 | LT 的闭无限维 Banach 球“大”来自远端无关自由度 | 新尺度须对该自由度稳定，N09 |
| 局部 germ 直接商 | 自然商常非 Hausdorff，不能直接称 Polish/Baire | 在后置关联谓词或严格规范表示中处理局部性，N06 |
| fixed-\(E\) Foran 修复 | 闭性不保证线性正则相交、下确界实现及一般合法修复 | orbit-code 和 Poisson 势预算可用，但需先处理 \(\forall U\exists V\)，N11–N12 |
| 为锥、Markov、RL 强设一个母定理 | 锥 MSCQ 缺同目标和反射接口，Markov \(\Psi\) 非 ordinary RL residual | 可统一叙事，数学定理保持独立，N04 |

表中 N 编号均指 [9/21 原 no-go ledger](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)。网络、工具、审稿模型或编译失败均不在这里当数学反证。

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

## F10 · 从算法收缩或单调性直接倒推原图误差界

- **原尝试**：由完整 \(J_{\lambda F}\) 严格收缩猜 \(F\) 强单调；或由 \(F\) 严格单调、cocoercive 且每条 PPA 轨道收敛猜存在趋零 gauge 的统一局部真残差 EB。
- **失败机制**：[EX01 旋转](research/canonical/example_atlas.md#ex01) 对任意 \(\lambda\omega>0\) 的完整 J 收缩因子 \((1+(\lambda\omega)^2)^{-1/2}<1\)，而单调内积恒为零。[EX02 无限维正紧对角](research/canonical/example_atlas.md#ex02) 对 \(x=te_n\) 有固定距离 \(t\) 而真残差 \(t/n\to0\)，并且每个有限迭代的范数仍为 1。两例分别阻断不同的无条件逆推；后者依赖无限维尾方向。
- **可回收成果与重启条件**：旋转例仍有精确线性真 EB 和 PPA 速率；对角例仍逐点强收敛。新增定理需说明使谱隙、闭值域或原图几何联结起来的额外条件，并在相同空间和量词下证明；有限维截断不能作为对角例的反证。

## F11 · 同一图任意换步而保留全对 Hölder–RL

- **原尝试**：已知固定 \(\lambda\) 的全图 \(\gamma<1\) RL，直接宣称所有 \(\eta>0\) 仍有同类全对证书。
- **失败点**：用旧 Cayley \(C(s)=\operatorname{sgn}(s)|s|^\gamma\) 反生成同一完整图。新输入映射 \(Q=\alpha I+\beta C\) 在 \(\eta>\lambda\) 时折叠两旧输入，故新 Cayley 连单值都不是；在 \(0<\eta<\lambda\) 时虽可成为全局 Lipschitz，新反射无穷远线性增长，所有全局次线性 Hölder 指数仍失败。[PD-STEP](research/canonical/parameter_dictionary.md#pd-step)。
- **可回收成果与重启条件**：确切换步坐标、\(Q\) 单射判据与 \(\alpha-|\beta|L>0\) 时的 Lipschitz 充分界成立。任何新换步推广先核同图、自然域与目标 coverage；取逆或缩放值域是改变关系的另一操作。
