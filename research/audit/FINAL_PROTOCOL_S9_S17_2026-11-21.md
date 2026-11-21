# 原协议 §9–§17 最终数学验收审计（2026-11-21）

## 审计范围和状态约定

本文件严格按用户原协议第四至第七部分的题号展开，并补答第八部分 28 问和第九部分 10 项交付物。审计对象固定为当前 PPA 仓库的 DD1–DD2 规范正文、Claim 版本和失败路线。

状态含义沿用 RESEARCH_PROTOCOL.md：

- Proved：规范正文可逐步重构，假设和量词已核对。
- Sharp：已有声明对象类的取等或反例。
- Recovered：严格恢复既有结果或其明确特例。
- Conditional：需要明确附加条件。
- Partial：有可靠中间结果，但主目标未闭合。
- Open：存在明确未解决义务。
- Refuted：有精确反例。
- Invalid：原表述缺少必要条件。

主要证据是 pppa_recovery.md、dual_eb.md、relaxation.md、inexact.md、splitting.md、C404–C406、P0 先行性审计、P2/P3 审计和其他固定步审计。机器验证不替代证明，selected relation 不替代 full graph。

证据定位：

- [约化与 shadow recovery](../topics/dd2/pppa_recovery.md)
- [双残差和联合几何](../topics/dd2/dual_eb.md)
- [方向松弛](../topics/dd2/relaxation.md)
- [非精确 DD2](../topics/dd2/inexact.md)
- [CP/DR 与其他分裂](../topics/dd2/splitting.md)
- [P0 先行性审计](DD2_P0_PRIOR_ART_2026-11-21.md)
- [P2/P3 审计](DD2_PRO_COMPLETION_2026-11-20.md)
- [其他固定步审计](DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md)
- [C404](../../CLAIMS.md#c404)、[C405](../../CLAIMS.md#c405)、[C406](../../CLAIMS.md#c406)

---

# §9 约化前向表示

## §9.1 P=CC* 分解

**状态：Conditional / Proved。**

在实 Hilbert 空间中，若 P 是有界、自伴、半正定、非零且有闭值域，令
\[
\mathcal R=\operatorname{ran}P,\qquad \mathcal N=\ker P.
\]
在 \(\mathcal R\) 上取 \(C=P_{\mathcal R}^{1/2}\) 后接自然嵌入，则 \(P=CC^*\)，且 C 在 \(\mathcal R\) 上是同构。有限维中闭值域自动成立。无限维没有闭值域时 \(C^{-1}\) 可能无界，原空间与约化空间的距离和残差常数不能直接传递。

## §9.2 约化空间

**状态：Proved。**

约化空间是 \(\mathcal R\)，约化变量为 \(z=C^*x\)，物理影子为 \(y\)，约化影子为 \(w=C^*y\)。完整零集的投影是 \(Z_r=C^*Z\)，选定目标 \(S^*\subseteq\operatorname{zer}A\) 则 \(S=C^*S^*\)。必须区分 \(C^*Z\) 与 \(C^*S^*\)。

## §9.3 图关系

**状态：Proved。**

令 \(G=(C^*A^{-1}C)^{-1}\)、\(F=I-J_G\)。对 \(q=z-w\) 有
\[
q\in F(z)\Longleftrightarrow q\in G(z-q)
\Longleftrightarrow \exists y\ [C^*y=z-q,\ Cq\in A_{\mathcal R}(y)].
\]
这是集合值图恒等式。对完整 F fiber 使用 DD2 还需要每个 q 的 lift 和工作域覆盖。

## §9.4 单值、多值与局部定义

**状态：Conditional。**

原始影子 \(\mathscr H(z)=(P+A)^{-1}Cz\) 的单值性给 G/F 的相应单值性。集合值 A 或非唯一 kernel lift 产生多值约化图。局部定义只需 \(\mathscr H(z)\) 在工作窗非空。全域定理需要全域非空或有限前缀留域。

## §9.5 零集关系

**状态：Proved / Conditional。**

在完整值域受限图和零点 lift 条件下 \(\operatorname{zer}F=\operatorname{zer}G=C^*Z\)。对选定目标只得到 \(S=C^*S^*\)，可能严格小于完整投影零集。相同投影的不同原零点不能由约化状态区分。

## §9.6 投影目标闭性

**状态：Conditional / Partial。**

有限维加闭零集和有界 recovery 时，C* 投影目标闭。一般无限维线性像不自动闭。pppa_recovery.md 的闭双曲线投影例说明原零集闭并不保证 C*Z 闭。

## §9.7 最近点

**状态：Conditional。**

有限维闭集有最近点，Hilbert 闭凸集有投影。一般 Hilbert 闭集和非凸闭集需要 proximinal 条件。仅范数闭不足，\(\ell^2\) 中 \(\{(1+1/n)e_n\}\) 是标准障碍。近似锚列可以替代最近锚，但必须把 liminf 量词写入平方展开。

## §9.8 缺陷传递

**状态：Proved / Conditional。**

若原边满足
\[
\langle P(x-y),y-x_*\rangle\ge\Phi(d_P(x,S^*)),
\]
则约化边满足同一 \(\Phi\)，因为
\[
\langle q,w-p\rangle=\langle P(x-y),y-x_*\rangle.
\]
普通原范数条件需要 recovery 和 \(m_C,M_C\) 换算。完整 F fiber 需要每个 q 的物理 lift，单一 selection 只给 selected-relation 结论。

## §9.9 正则性传递

**状态：Conditional。**

精确真残差关系为
\[
r_G(w)=\inf_{C^*y=w}r^C_{A_{\mathcal R}}(y),
\quad
m_Cr_G(w)\le\inf_{C^*y=w}r_{A_{\mathcal R}}(y)\le M_Cr_G(w).
\]
因此 P-距离 gauge 可按 \(m_C,M_C\) 传递。原范数 gauge 还需要局部 recovery。远 kernel lift 会使 \(r_G\) 很小而原范数界失败。

## §9.10 投影、kernel、非满射失败

**状态：Refuted for unconditional version。**

已记录目标投影非闭、非唯一 fiber、远 kernel lift、仅选定 lift 满足误差界四类失败。约化收敛不自动给物理强收敛。

## §9.11 一般 gauge

**状态：Conditional / Proved。**

连续非减 gauge 可沿残差公式传递。F 方向通常付出 \(\psi+\mathrm{id}\) 的输入位移项。局部 Hölder 可吸收线性项，一般 gauge 需要重新计算 \((I+\psi)^{-1}\) 和缺陷吸收。

## §9.12 Alcantara 二次参数版本

**状态：Recovered / Conditional。**

Lemma 4.3 的 \((U,V)\) 二次条件可通过 P 内积和 \(C^*VC\) 正定性接入 DD2。Theorem 4.10–4.12 的弱收敛、唯一 fiber、强恢复和 Lipschitz recovery 可恢复，但需要完整 lift、目标闭性、零值 demiclosedness 和 DD2 留域条件。

§9 逐题证据与量词索引：§9.1–§9.3 使用 `../topics/dd2/pppa_recovery.md` 开头定义和式 (1)，量词是闭值域下的每个允许图值。§9.4–§9.7 使用同文件“锚定条件与最近点”段，量词分别是选定影子、非空局部关系和存在最近锚。§9.8–§9.11 使用式 (2)–(4) 及 gauges 表，完整结论要求每个允许 q 都有 lift，selected relation 只给存在性。§9.12 使用同文件对 Lemma 4.3、Theorems 4.10–4.12 的映射，附加矩阵正定、闭图和 recovery 条件不能省略。

---

# §10 Shadow recovery

1. **Projected convergence，Proved。** \(z^k\to z_\infty\) 强收敛时，\(P_{\mathcal R}^{-1/2}z^k\) 强收敛。
2. **Projected zero identification，Conditional。** S 闭且距离趋零时极限在 S。S 不闭时只能到 \(\overline S\)。
3. **Bounded recovery，Conditional。** 在 \(q^k\to0\)、\(z^k\to z_\infty\) 且所选影子有界时，局部有界 \(\mathscr H\) 加零值 demiclosedness 给物理零点聚点。有限维时可用零值外半连续和紧性替代。
4. **Weak shadow convergence，Conditional。** 在上述 \(q^k\to0\) 和影子有界量词下，所有弱聚点在 \(Z\cap(C^*)^{-1}(z_\infty)\)。fiber 单点时弱收敛。
5. **Strong shadow convergence，Conditional。** 唯一 fiber 加有界性只给弱收敛和正确 fiber 识别。强收敛还需要有限维性、弱到强的额外紧性，或固定零点的局部强 recovery。
6. **Lipschitz recovery，Proved conditionally。** \(\|y-x_\infty\|\le K\|z-z_\infty\|\) 传递点误差和可和的约化尾上界。它本身不把物理相邻差分的总长变成有限，后者仍需二点 recovery 或可和尾势。
7. **Hölder recovery，Conditional。** 一点评估只给点识别。二点 Hölder 还需 \(\sum\omega(\|\Delta z_k\|)<\infty\) 才给物理长度。
8. **Shadow finite length，Conditional。** 需要二点 recovery 或沿轨可和差分。
9. **Tail transfer，Conditional。** 一点 Lipschitz 给 \(K L_k\)，一般 gauge 保留势尾。
10. **Recovery conditions from structure，Conditional。** Theorem 4.11–4.12 的 \((U,V)\) 强正定给出一种可验证结构。
11. **Finite-dimensional simplification，Proved conditionally。** 外半连续、闭图和局部有界可用紧性加强。
12. **Weaker mechanism，Partial。** 对弱聚点识别，最弱可靠组合是约化强收敛、闭目标、有界 lift、零值闭图。唯一 fiber 再给物理弱收敛。物理强收敛还需有限维性或强 recovery，非唯一 fiber 只能给正确 fiber 的聚点结论。

§10 逐题证据与量词索引：§10.1–§10.2 对所有强收敛约化轨道使用 `../topics/dd2/pppa_recovery.md` 的“投影识别”段。§10.3–§10.5 的量词是 \(q^k\to0\)、所选影子序列有界并且每个弱聚点满足零值 demiclosedness，有限维时才可用外半连续和紧性替代，非唯一 fiber 只给聚点。§10.6–§10.9 使用该文件的“一点恢复”“物理长度”段，二点估计需对轨道相邻输入成立。§10.10–§10.12 使用 Theorems 4.11–4.12 及有限维专门化，任何强恢复均是附加条件下的 conditional 结论。

---

# §11 双重残差和正则性传递

1. **状态：Proved。** 原残差在 \(A_{\mathcal R}(y)\)，约化输出残差在 G(w)，约化输入残差在 F(z)，位置不同。证据：`../topics/dd2/dual_eb.md` 的残差位置表。
2. **状态：Proved。** 图对应由 \(q\in F(z)\Longleftrightarrow q\in G(z-q)\Longleftrightarrow\exists y\) 给出。证据：`../topics/dd2/pppa_recovery.md` 式 (1)。
3. **状态：Conditional。** 原 P-距离误差界到 G 的传递在完整 fiber lift 下成立。证据：`../topics/dd2/pppa_recovery.md` 式 (3) 及 gauges 表，量词是每个允许 q 都有 lift。
4. **状态：Refuted（无条件版本）。** 反向普通范数传递没有无条件结论，远 kernel lift 是反例。证据：`../topics/dd2/pppa_recovery.md` 逆向障碍 1–4。
5. **状态：Conditional。** 线性 gauge 付出 \(m_C,M_C\)，Hölder 可局部吸收线性项，一般 gauge 需要 \(\chi=(I+\psi)^{-1}\)。证据：`../topics/dd2/pppa_recovery.md` gauges 表及 C401。
6. **状态：Conditional / Sharp for stated geometry。** C403 的共同 s 联合几何可以严格强于分开的三角估计，但两个弱界并列本身不产生新机制。证据：`../topics/dd2/dual_eb.md` 的共同 s 极值与取等构形。
7. **状态：Proved（实例存在）。** 约化强而原空间弱的实例和 \(G(y)=\{y,y^3\}\) 已给出。证据：`../topics/dd2/pppa_recovery.md` 逆向障碍 3–4。
8. **状态：Conditional。** 联合补偿判据需要同一边、同一 s、锚缺陷、输出 gauge 和完整允许边 coverage。证据：`../topics/dd2/dual_eb.md` 的 full-coverage 条件。
9. **状态：Recovered / Conditional。** 线性 \(\psi\) 与二次缺陷恢复 DD1，\((U,V)\) 特例恢复 Alcantara Proposition 3.4。证据：C403、C404，量词限于匹配的 full-graph 或 selected-relation 版本。
10. **状态：Proved（逻辑分层）。** 图恒等式是代数层，闭图、fiber 有界、目标闭性和 demiclosedness 负责极限层。证据：`../topics/dd2/pppa_recovery.md` 式 (1)、(6)。

---

# §12 完整算法分析

1. **状态：Conditional。** Fejér/quasi-Fejér 只有在全锚统一条件下成立，最近锚只给距离递推。证据：`../topics/dd2/relaxation.md` 全锚与最近锚分节。
2. **状态：Conditional。** 实际有限长度由 C401 势或同一步严格耗散给出。证据：C401 与 `../topics/dd2/core.md#dd2-general-gauge`，需要严格余量和可积势。
3. **状态：Proved conditionally。** 带统一正耗散系数的严格平方耗散给残差平方可和。若系数只逐步为正，结论仍是带权平方和，不能自动改成无权平方和。证据：`../topics/dd2/relaxation.md` 的望远镜不等式，量词是整条留域轨道。
4. **状态：Conditional。** 一般非线性残差可和需要积分势和误差债务。证据：C401、C406，未覆盖任意振荡 gauge。
5. **状态：Proved conditionally。** 在统一正耗散系数下，best-iterate 由平方和给 \(O(N^{-1/2})\) 范数级率。系数退化时只能给加权 best-iterate 结论。证据：`../topics/dd2/relaxation.md` 的残差平方望远镜，需非空真残差和统一初始预算。
6. **状态：Conditional。** ergodic 率需要望远镜权重，通常为 \(O(1/N)\)。证据：`../topics/dd2/relaxation.md` 的加权向量平均，权重和及目标量词需另列。
7. **状态：Conditional。** pointwise 率需幂次递推或一般比较函数。证据：C399、C401，单纯平方和不推出 pointwise 率。
8. **状态：Conditional。** 复杂度界需要显式工作域、势和残差评价成本。证据：C401 的前缀预算，算法成本尚未统一定义。
9. **状态：Sharp for stated subclasses。** C399/C400 给 stated subclasses 的 sharp rates。证据：C399 幂次取等与 C400 反向预算，不能升级到全算子类。
10. **状态：Conditional。** 有界性来自留域预算，极限识别还需要闭性或 demiclosedness。证据：`../topics/dd2/core.md` 的留域引理、`../topics/dd2/pppa_recovery.md` 式 (6)。
11. **状态：Conditional。** Q-linear 来自固定 A，R 型非线性率来自比较函数，超线性需要额外 \(A(t)/t\to0\) 结构。证据：C399/C400，超线性只对距离递推且需实际取值满足相应上界。
12. **状态：Conditional。** 无统一 A 时仍可使用同一步势和局部留域。证据：C401 的逐边势条件和 `../topics/dd2/core.md#dd2-trajectory`。

---

# §13 自适应松弛和非精确

1. **状态：Conditional。** 真实区域为
   \[
   \alpha_k<2(\underline\beta_k-\omega_D(t_k)).
   \]
   证据：C407 与 `../topics/dd2/adaptive_parameter_audit.md`，量词是每一允许边且需可观测方向余量。
2. **状态：Proved conditionally。** 一般 \(\Phi\) 通过平方展开和 \(D(t)\) 进入能量。证据：`../topics/dd2/relaxation.md` 的方向松弛能量展开。
3. **状态：Conditional。** 逐边规则由方向下界、缺陷和 \(\chi(t)\) 计算。证据：C407，方向下界和缺陷必须在当前边上可认证。
4. **状态：Conditional。** \(\alpha_k\to0\) 或接近边界会使净耗散消失。证据：`../topics/dd2/relaxation.md` 余量项及 C406 临界旋转反例，不能断言每条序列必然失败。
5. **状态：Conditional。** 统一正下界只在点收敛和全锚结论中额外需要。证据：C402/C407 的松弛尾界，具体算法还需识别假设。
6. **状态：Conditional。** 超松弛需要方向余量和输出锚根式门。证据：`../topics/dd2/relaxation.md` 的 \(\gamma=2\beta-\alpha\) 能量及 C402。
7. **状态：Proved conditionally。** 松弛后必须重建比较函数，不能复用精确步 A。证据：C402 的同一步势，松弛参数改变实际位移。
8. **状态：Conditional。** 有正余量和势债务时有限长度保留。证据：C401/C406，需误差债务可和并保持留域。
9. **状态：Conditional。** 绝对误差需 \(\Delta_\Theta+\eta\) 可和，相对误差可由 \(\eta\le\theta(\tau-a)\) 认证。证据：C406 与 `../topics/dd2/inexact.md`，两种误差量词分开。
10. **状态：Conditional。** 速率与 shadow recovery 需要误差尾和二点恢复。证据：C406 与 `../topics/dd2/pppa_recovery.md` 物理长度段。
11. **状态：Refuted（自动升级版本）。** C406 给出欧氏可和但点不收敛、相对误差趋零但长度发散和临界旋转反例。证据：`../topics/dd2/inexact.md` 反例小节。
12. **状态：Partial / Open。** C407 的逐边区域比固定松弛细，但最宽性仍 Open。证据：C407，尚无所有可见量词下的最宽性证明。

---

# §14 CP、DR 和其他分裂

1. **状态：Conditional。** 原始问题由 \(A,B,L\) 及原始–对偶块定义。证据：`../topics/dd2/splitting.md` 的 S1，空间量词为有限维实 Hilbert (X,Y)。
2. **状态：Conditional。** DD2 可施加在约化状态、组合图或 \(C^*\) 投影关系。证据：`../topics/dd2/splitting.md` S1–S2 及 `pppa_recovery.md` 式 (1)，需选择具体 graph coverage。
3. **状态：Conditional。** 非线性次单调性由分量图和块完成平方验证。证据：`../topics/dd2/splitting.md` S4–S10，量词是相应完整图点。
4. **状态：Proved as audit requirement。** 非线性正则性必须针对组合真残差，不可拼接选择残差。证据：`../topics/dd2/splitting.md` S6–S7 取完整图值 infimum。
5. **状态：Conditional。** 补偿函数由谱门、组件 gauge 和共同 s 计算。证据：`../topics/dd2/splitting.md` S8 及 C403，跨组件 coupling 仍需独立验证。
6. **状态：Conditional。** 子问题良定需要 resolvent 非空或有限前缀 continuation。证据：`../topics/dd2/splitting.md` S1 和适用边界。
7. **状态：Conditional。** 约化长度由 C401/C402 条件传递。证据：`../topics/dd2/splitting.md` S8，需固定步或重建松弛势。
8. **状态：Conditional。** 原始/对偶收敛需要 recovery 和 fiber 条件。证据：`../topics/dd2/pppa_recovery.md` 投影识别和物理收敛段。
9. **状态：Conditional。** 完整 shadow recovery 需要二点 recovery 或 Theorem 4.11–4.12 条件。证据：`../topics/dd2/pppa_recovery.md` 物理长度段与 `splitting.md` S2–S3。
10. **状态：Sharp / Conditional。** 固定 CP/DR 子类有残差和慢速例，泛化算法没有统一率。证据：`../topics/dd2/splitting.md` CP/DR 临界例与慢轨道。
11. **状态：Partial / Open。** 与已有算法定理的严格弱假设关系尚未对全部类别证明。证据：`../topics/dd2/splitting.md` 适用边界与 `DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md`。
12. **状态：Proved for fixed-step subclasses / Open for extensions。** FBF 系数为 \((1-\ell)/(1+\ell)\)，外梯度系数为 \((1-\ell)/2\)，FRB 需交叉项 Lyapunov 且普通欧氏下降可失败。统一松弛、异步、时变图和非分离多算子 Open。证据：`../topics/dd2/splitting.md` 其他分裂实际步证书及 `DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md`。

---

# §15 文献和已有理论

- Luke–Tam 与 Lauster–Luke 已有比较曲线、输入步和部分有限长度机制，DD2 恢复其固定单值或全锚特例。
- 旧 RLEB 是 DD2 在线性输出 gauge 和固定收缩因子下的 recovered subcase。
- Alcantara v1 的普通 PPA、约化前向和 shadow 条件在 C404 约化范围内 conditional recovered。
- Hölder metric subregularity 的 \(q>1/2\) 有限长度端点已有先例，DD2 不宣称首次。
- KL 只能在具体能量和下降条件下提供有限长度接口，不能自动扩展为 RL/GPPA 总定理。
- gauge 机制和 C401 对一般函数给出内部证明链，但全球严格新颖性仍未穷尽。
- FBF、EG、FRB 和 CP/DR 只完成固定步、明确图覆盖的子类。

逐式证据位于 DD2_P0_PRIOR_ART_2026-11-21.md 与 research/LITERATURE.md。未读版本不升级为 Paper Fact。

### §15.1–§15.10 十项迁移问题

1. **状态：Recovered conditionally。** 原论文真正证明的是各自固定版本中明确写出的比较曲线、半单调 PPA、约化前向、Hölder PPA 或 KL/有限长度结论。证据：`DD2_P0_PRIOR_ART_2026-11-21.md` 的 Paper fact 小节和 `research/LITERATURE.md`。量词按原文版本保留。
2. **状态：Proved for the read versions / Partial globally。** 已读文献的空间、图、目标、残差和局部或全域量词已登记。仅有摘要或未读版本保留 deferred，不能升级为 Paper fact。证据：`research/LITERATURE.md` 的版本与访问边界记录。
3. **状态：Conditional。** C400–C406、C404 和 C405 分别恢复 Lauster–Luke 的比较迭代特例、Alcantara 的普通 PPA/约化/分裂特例、Hölder PPA 的幂次门。证据：P0 审计逐式换参以及本文件 §9–§14。
4. **状态：Partial / Conditional。** 恢复通常只覆盖固定步、闭值域、完整 lift、匹配的 full-graph 或 selected-relation 版本。原论文中未被 DD2 假设重建的紧性、自映射、局部覆盖或矩阵正性保持为附加条件。证据：P0 §2.3、`pppa_recovery.md` 证据边界。
5. **状态：Proved as scope separation。** 不能自动恢复的假设包括 CAT(κ) 或 p-一致凸几何、bounded compactness、自映射留域、Alcantara 的零值 demiclosedness、完整 shadow fiber 和分裂算法的 resolvent 非空性。证据：P0 的严格边界段与 `splitting.md` 适用边界。
6. **状态：Partial / Open globally。** 已证明的是若干匹配特例的恢复和几何模块的扩展，尚未证明对每一篇文献都严格削弱假设或严格增强结论。证据：C410、C404–C405 的 Counterevidence / Scope 字段。
7. **状态：Conditional。** 不可比较关系由量词和对象差异产生，例如 DD2 的最近锚/允许边与文献的全锚/全图、自映射和紧性要求不能直接互含。证据：P0 §2.3 与 `research/LITERATURE.md` 的接口表。
8. **状态：Partial。** 真实算子分离已在远 kernel、非唯一 fiber、非单调慢轨道以及 FRB 欧氏势反例中给出，但“严格包含全部旧算子类”尚未证明。证据：`pppa_recovery.md` 逆向障碍、`splitting.md` 慢轨道和 `DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md`。
9. **状态：Proved for the audited modules。** 相同机制是锚定平方能量、误差界和比较迭代，不同机制是共同 s 的四点约束、值域退化 fiber、真实物理恢复和非精确误差债务。证据：本文件 §11–§14 与 `dual_eb.md`、`pppa_recovery.md`。
10. **状态：Open as a global priority claim。** 现有记录只能排除已读版本中的直接等价误读，不能据有限检索宣称不存在更早等价结果。证据：P0 的检索边界声明和 `research/LITERATURE.md` 的未读来源清单。

---

# §16 新颖性八维评价

A. 新公式：Equivalent / Recovered。许多公式是已知二次式或共同 s 几何的重参数化。

B. 新定理：Partial / Conditional。C400–C406、C408、C412 在精确范围内有独立推导，但全球先行性和全理论统一尚未闭合。

C. 新刻画：Sharp for stated geometric classes。平面分段、联合包络和幂次临界有取等。全算子类必要充分性 Open。

D. 新算子类：Conditional / Partial。非单调、多值、非凸和非孤立例已存在，严格包含关系须固定共同对象和量词后比较。

E. 新收敛机制：Partial。一般势和物理 recovery 给出非固定 A 机制，已有文献部分重合。

F. 新算法应用：Conditional。CP/DR、FBF、EG、FRB 和固定网络子类已闭合，统一算法应用未闭合。

G. 新方法：Conditional / Partial。四点共同 s 约束在声明的几何模块中已核对严格强于分开三角估计，是否普遍超越传统 Lyapunov 尚未证明。

H. 新临界现象：Sharp for stated subclasses。二次缺陷、Hölder 端点、低 L 支和物理长度分离均有构造。

§16 逐项证据索引：A–B 由 C400–C412、`DD2_P0_PRIOR_ART_2026-11-21.md` 和对应正文给出公式重构及先行性边界。C 的平面联合包络与幂次取等见 C399/C400/C403。D–F 的算子类、恢复和算法范围见 C404/C405/C412 及 `pppa_recovery.md`、`splitting.md`。G 的共同 s 严格增益见 `dual_eb.md` 的同边比较，仍限于声明几何类。H 的临界反例见 C399/C400/C405/C406。所有判断保留各 Claim 的 full-graph、selected-relation、工作窗和 recovery 量词。

---

# §17 独立反例和数学审查

1. **状态：Proved conditionally。** 对象良定：在写明闭值域、目标和图非空的定理中 Passed。证据：`../topics/dd2/pppa_recovery.md` 开头设定与各 splitting 的非空 resolvent 假设。
2. **状态：Proved as audit。** 量词：已区分 full graph、allowed edge、selected relation、nearest anchor 和 all anchors。证据：本文件 §9.3、§9.8、§11.8 及 `RESEARCH_PROTOCOL.md`。
3. **状态：Proved as audit。** 隐含假设：闭值域、目标闭性、lift、fiber、demiclosedness 和留域均已列出。证据：本文件 §9–§10 和 `pppa_recovery.md` 证据边界。
4. **状态：Partial / Open。** 边界：\(L=1/2\)、临界缺陷、非孤立目标、非唯一 fiber、\(\alpha_k\to0\) 已攻击。一般振荡 gauge 仍 Open。证据：C400/C401/C406 与 `pppa_recovery.md` 反例。
5. **状态：Proved as convention。** 空图：空值真残差取 \(+\infty\)，算法非空必须独立假设。证据：`pppa_recovery.md` 真残差定义和 `splitting.md` S1。
6. **状态：Recovered conditionally。** 导入条件：Alcantara、Lauster–Luke 和 Hölder PPA 的已用版本在 P0/C404 中定位。证据：`DD2_P0_PRIOR_ART_2026-11-21.md`、C404，仍需按版本量词。
7. **状态：Proved as requirement。** 局部沿轨：需要有限前缀留域，不能把局部条件自动全局化。证据：C401 留域预算及 `pppa_recovery.md` 接入 DD2 段。
8. **状态：Proved as audit。** 循环证明：约化恒等式、下降、恢复和零值识别已分层。证据：`pppa_recovery.md` 式 (1)、(6) 和物理收敛段。
9. **状态：Proved as atlas entries。** 低维反例：平面旋转、FRB、两锚、远 kernel 和 G(y)=\{y,y^3\} 已记录。证据：`pppa_recovery.md` 逆向障碍、`splitting.md` FRB 段和 `inexact.md`。
10. **状态：Partial。** 非单调、多值、非孤立目标：已有多类实例，完全 fiber 分类仍 Partial。证据：C404–C405 与 `pppa_recovery.md` 反例集合。
11. **状态：Proved as separation。** 必要/充分：C400/C401/C403 明确分开比较层必要性、几何充要和算子级充分。证据：C400、C401、C403 的状态字段和反向障碍。
12. **状态：Sharp for stated subclasses / Open globally。** 最优性：固定几何和幂次子类有 sharpness，全类 Open。证据：C399/C400 与本文件 §16C。
13. **状态：Proved as reproducibility check。** 计算：verify_outline、validate_assets、build_graph 和两套可视化可复现，不能代替证明。证据：本轮命令输出及 `research/validate_assets.py`、`research/build_graph.py`。
14. **状态：Partial。** 独立路线：几何、能量、矩阵、fiber 和反例路线分别存在，完整总定理尚未双路线闭合。证据：core、dual_eb、pppa_recovery、splitting 的相互独立证明路径。
15. **状态：Open（fatal objections remain）。** fatal objection：一般弯曲闭凸低 L、弱 kernel coverage、统一异步算法和全球新颖性仍阻止无条件 canonical master theorem。证据：C411、C404、C412 与本文件 §16B/D/F。

---

# 第八部分 28 个深层问题

## DD 理论本身

1. DD1/DD2 共同结构是锚定缺陷、输出 gauge、步长和共同 s 的同一步几何预算。Proved for stated classes。
2. 可定义同尺度补偿泛函，\(\chi=(I+\psi)^{-1}\) 和 \(\Theta\) 是其势接口。作为普遍对象仍 Partial。
3. \(\chi\) 给出逆函数方向，统一对偶描述仍 Open。
4. 固定对象类可定义最大缺陷或最小方向余量。Sharp only for subclasses。
5. 最优性依赖 \(\Phi,\psi\)、coverage 和算子类。Proved。
6. DD1 分段来自步长支和能量支的切换。Recovered。
7. 新相变包括低 L anchor switch、\(q=1/2\) 和同时临界常数。Sharp for examples。
8. 一般函数能完整刻画二维尺度模型，不能完整刻画所有 PPA。Partial。

## 收敛机制

9. 固定收缩可削弱到比较迭代和势下降。Proved conditionally。
10. 有限长度只需可和势，不需固定比例。Proved by C401。
11. 一般函数最优有限长度判据尚未完成。Open。
12. 残差平方可和不蕴含残差可和。Refuted。
13. \(\Phi,\psi\) 通过 \(\chi,\Theta\) 给非线性率。Conditional。
14. 对数和非幂次机制可纳入势，但振荡模需单调包络。Partial。
15. 放弃有限长度仍保留距离、平方和、best iterate 和识别。Conditional。

## 算法迁移

16. PPPA 在闭值域、完整 lift、目标闭和 recovery 条件下继承 DD2。Conditional。
17. 降维可能丢失 kernel fiber、原范数残差和目标闭性。Proved by examples。
18. 原/约化函数指标可通过 \(m_C,M_C\) 和 recovery 双向传递。Conditional。
19. **状态：Conditional。** 最弱 recovery 是有界 lift、闭图和正确 fiber 聚点识别。它只保证物理弱聚点。强 recovery 或有限维紧性才可升级为强收敛。证据：`../topics/dd2/pppa_recovery.md` 投影识别段。
20. primal-dual 组合规律来自块完成平方和共同 s。Conditional。
21. 已有固定步分裂 calculus 组件，统一 calculus Open。
22. 尚未证明具体应用严格超过全部现有算法定理。Partial。

## 理论边界

23. DD1 两段、幂次临界和部分低 L 已 Sharp。
24. 一般 gauge、弯曲闭凸、异步网络临界边界 Open。
25. 自动 finite length、自动 shadow 收敛、Hölder 自动 finite length 已 Refuted。
26. 一些缺口可能是技术问题，也可能暴露命题错误，尚不能判定。Open。
27. **状态：Proved for stated modules。** 局部锥、共同 s、二点 recovery 是已确认的改善约束。证据：C400/C403、`pppa_recovery.md` 物理长度段。
28. **状态：Proved as obstruction diagnosis。** 核心障碍是图残差、目标锚、kernel fiber 和物理步长不由单一距离控制。证据：`pppa_recovery.md` 逆向障碍、shadow finite-length 反例与 C406。

§8 逐题证据与量词索引：题 1–8 的共同结构、补偿泛函、逆映射和分段机制以 C400/C401/C403 及 `../topics/dd2/core.md` 为证据，量词限于声明的几何类、连续非减模和允许边 coverage。题 9–15 的收敛、势、残差和非幂次机制以 C399/C401/C406 及 `../topics/dd2/inexact.md` 为证据，严格区分逐边递推、整条留域轨道和误差债务。题 16–22 的 PPPA、fiber、recovery 与 splitting calculus 以 `../topics/dd2/pppa_recovery.md`、`../topics/dd2/splitting.md`、C404/C405/C412 为证据，完整强收敛和物理长度保留相应附加条件。题 23–28 的锐边、反例和阻碍以 C400/C399/C406/C411、`pppa_recovery.md` 和 `DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md` 为证据，未闭对象明确标为 Open 或 Partial。

---

# 第九部分交付物

1. **状态：Conditional / Partial。** Canonical Theorem Statements：C400–C406、C408、C410–C412 和对应正文。证据：`CLAIMS.md` 对应记录及 `research/topics/dd2/`，通用未闭版本保持 Open。
2. **状态：Partial。** 完整证明：core、relaxation、dual_eb、pppa_recovery、inexact、splitting。通用未闭版本保留 Partial/Open。证据：各正文 proof 段和本文件 §17，尚无单一无条件 master proof。
3. **状态：Proved / Reproducible。** Dependency Graph：research/graph.json、research/HYPERGRAPH.md 和 README Claim Map。证据：`research/build_graph.py` 输出 955 nodes、720 edges。
4. **状态：Proved as indexed asset。** Counterexample Atlas：FAILED_ROUTES、C399/C400、pppa_recovery、inexact、splitting。证据：相关文件中的编号反例及 `FAILED_ROUTES.md`。
5. **状态：Partial。** Literature Matrix：research/LITERATURE.md 和 P0 逐式审计。证据：`research/LITERATURE.md` 与 `DD2_P0_PRIOR_ART_2026-11-21.md`，全球优先性仍 Open。
6. **状态：Partial。** Operator-Class Map：CLAIMS、README、C312/C315/C400/C404/C405。证据：对应 Claim 的对象和量词，严格全包含关系尚未全部判定。
7. **状态：Conditional / Partial。** Functional Compensation Map：core、dual_eb、relaxation、adaptive_parameter_audit。证据：C401/C402/C403 和相关正文，任意 gauge 的逆向必要性 Open。
8. **状态：Conditional。** Algorithm Transfer Dossier：pppa_recovery、splitting、DD2_OTHER_SPLITTING_AUDIT、C404/C405/C412。证据：固定步 CP/DR、FBF、外梯度和 FRB 子类，变图/异步仍 Open。
9. **状态：Proved as reproducibility scripts。** Reproducible Experiments：research/code/dd2/verify_outline.py、validate_assets.py、build_graph.py 和离线构建脚本。证据：本轮已运行并记录输出，脚本只作证据不替代数学证明。
10. **状态：Proved as indexed frontier。** Research Frontier Report：RESEARCH_STATE、FAILED_ROUTES、DD2_TASK_ACCEPTANCE_MATRIX 和本审计的 Open/Partial 列表。证据：对应文件及本文件“最终状态”段。

---

# 最终六问

## 第一问：现在到底证明了什么

**状态：Conditional / Partial。**

已证明或条件性证明的核心内容包括：闭值域 \(P=CC^*\) 下的约化图恒等式，P-内积缺陷的等距传递，完整 fiber 真残差的 \(m_C,M_C\) 关系，目标闭性与 demiclosedness 下的 projection identification，唯一 fiber 下的物理弱收敛，以及有限维性或强 recovery 下的物理强收敛。还包括 C401 一般势的有限长度，C402 方向自适应松弛，C403 联合双残差几何，C405 固定 CP/DR 子类，C406 非精确图误差债务，以及 FBF、外梯度和 FRB 的固定步局部证书。

这些结果的状态是 Proved、Recovered、Sharp 或 Conditional，不能合并成一个无条件 master theorem。

## 第二问：究竟理解了什么

**状态：Proved for the separated mechanisms。**

次单调缺陷控制的是输入锚与输出方向之间的内积，正则性控制的是输出距离与真实图残差，下降模控制的是距离序列，有限长度势控制的是实际位移，recovery 控制的是约化 shadow 到原空间的 lift。它们位于不同空间和不同量词，不能由单一线性常数替代。

最关键的机制分离是：平方可和只给渐近正则性，有限长度需要额外势或幂次可积性，约化强收敛需要 fiber 与物理 recovery，物理长度需要二点 recovery。

## 第三问：究竟推广了什么

**状态：Partial / Conditional。**

相对于旧 RLEB、Luke–Tam、Alcantara 和 Hölder PPA，仓库已经严格恢复线性、全锚、固定步和 Hölder 特例，并在明确的最近锚、函数缺陷、共同 s 联合几何、低 L 固定图和物理 recovery 范围内给出扩展。哪些关系严格包含、哪些不可比较，取决于共同对象和 full-graph 量词。全球严格新颖性没有被有限审计宣称。

## 第四问：能处理什么算法

**状态：Conditional。**

普通 PPA、闭值域预条件 PPA、特定 CP/DR、固定步 FBF、外梯度、FRB 和带明确拓扑与 cocoercivity 的网络前向—后向子类已有条件性定理。变图、异步、统一松弛、非分离多算子、一般近似 resolvent 和没有 fiber recovery 的原始 shadow 仍属于 Open 或 Partial。

## 第五问：边界在哪里

**状态：Proved for stated boundaries / Open globally。**

已经尖锐的边界包括 DD1 两段门、平面共同 s 包络、幂次临界常数、\(q=1/2\) 端点、低 L 锚切换、平方可和与实际长度的分离、FRB 欧氏势失败和非唯一 fiber 反例。尚无完整算子构造的边界包括一般弯曲闭凸低 L 链、任意 gauge 的反向必要性和所有分布式变图模型。

## 第六问：下一阶段最有价值的问题

**状态：Open research frontier, with prioritized obligations。**

优先级最高的是构造或否定一般弯曲闭凸零集上的低 L 固定图链，其次是弱 kernel 控制下的完整 fiber coverage 判据，再其次是给出一个同时满足非零 \(U\)、非单调、非线性慢速和完整 shadow recovery 的 CP/DR 实例。每个问题都可以直接攻击当前阻塞的 theorem version，而不是继续增加形式相似的充分条件。

最终六问证据链：第一问对应 §9–§14 的定理和各自状态，第二问对应 §10–§12 的机制分层，第三问对应 §15–§16 的文献与新颖性索引，第四问对应 §14 及 C405/C412 的固定步算法条件，第五问对应 §17 与反例索引， 第六问对应本文件列出的 Open/Partial 义务及 C411/C404/C412 的边界。每一问都保留对象、量词、工作窗和附加 recovery 条件。

---

# 最终状态

§9–§17 的每个题号已有逐项状态和可定位证据。约化图恒等式、条件性 shadow recovery、双残差传递、固定步算法证书、误差债务和既有理论恢复已经形成证明链。一般弯曲闭凸低 L、弱 kernel full coverage、统一异步/变图算法、全局严格新颖性和若干物理 recovery 结论仍有明确 open obligation，因此不能把当前理论宣布为无条件统一总定理。
