# Claim Ledger · 精确身份与证据

本页的“稿内证明”指可阅读的证明文本，不代表全部已重新独立验真；“内部审计”也不是外部同行评审或优先权确认。对同一编号的量词、域、假设或结论作任何改变，须另立版本。依赖和合取关系见 [超边图](research/HYPERGRAPH.md)；原稿路径与版本见 [SOURCES.md](research/SOURCES.md)。C01–C08 保留初始身份；后续版本按新的精确对象逐项进入，历史同号不得直接合并。

## C01 · 全图 RL 的 Cayley 坐标

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain**：非空关系 \(F:H\rightrightarrows H\)，实 Hilbert 空间 \(H\)，\(\lambda,L>0\)，\(0<\gamma<1\)。在**每一对**图点 \((x,v),(y,w)\) 上有 \(\|(x-y)-\lambda(v-w)\|\le L\|(x-y)+\lambda(v-w)\|^\gamma\)，当且仅当 \(D=\{x+\lambda v:(x,v)\in\operatorname{gph}F\}\) 上 \(C(x+\lambda v)=x-\lambda v\) 良定且为 \(L\)-Hölder；反向图重建为 \(((p+C(p))/2,(p-C(p))/(2\lambda))\)。若 \(D=H\) 则图在**同一固定参数**下 maximal。
- **Dependencies / Evidence**：图点求和、求差和同输入唯一性；[9/23 TeX Lemma `cayley`](history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 直接给出双向证明。反向“任何极大图必满域”的同常数扩张已在 [HE-EXTENSION](research/canonical/holder_extension.md#he-extension) 从 Hilbert 雪花正性及[一手 Kirszbraun 引文](research/LITERATURE.md#lit-alm-2021)单独重写。
- **Objections / Status / Scope**：`derived-checked` 仅针对剪切代数及已核的同常数扩张条件；只说固定参数的 graph-maximal，绝不等同于极大单调；局部图块须重新声明量词。

## C02 · 9/18 局部 RLEB–PPA 收敛（原稿版本）

- **Status**：`candidate`。

- **Exact Statement / Objects / Domain**：\(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，\(\lambda>0\)，非空闭 \(S\subset F^{-1}(0)\)，图块 \(\mathcal G\)、开域 \(U\)、\(0<\gamma\le1\)、\(L\ge0\)、\(R,\bar t>0\)，非减 \(\psi(0)=0\) 且原点连续，\(0<\kappa<1\)。A1：\(U_R\) 上局部 range coverage 且每个输入有图块中的最近零点；A2：\(\mathcal G\) 在尺度 \(R\) 满足 all-pairs RL；A3：实际输出上的 \(d(y,S)\le\psi(r_F(y))\) 及 gauge domain；A4：对 \(0<t\le R\)，\(\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t\)。初值还需 \(d_0\le R\) 和 \(\mathcal L(d_0)=\tfrac12[d_0/(1-\kappa)+Ld_0^\gamma/(1-\kappa^\gamma)]<\operatorname{dist}(x^0,X\setminus U)\)。
- **Conclusion**：唯一的**局部** \(J_{\mathcal G}\) 轨道无限继续、留域、有限长度、收敛到 \(S\) 中一点；\(d(x^k,S)\le\kappa^kd_0\)，且 \(\|x^\infty-x^k\|\le\tfrac12[\kappa^kd_0/(1-\kappa)+L\kappa^{\gamma k}d_0^\gamma/(1-\kappa^\gamma)]\)。允许多选择版本改用每个合法 transition 的共同 anchored 估计，不能把多值图与单值局部 \(J\) 混同。
- **Dependencies / Evidence**：C01 的局部形式、一步能量和 \(s\le(d+Ld^\gamma)/2\)、真实输出残差、A1–A4、归纳留域；[9/18 原投稿 ZIP 的 `sections/theorem_spine.tex`](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip)。
- **Objections / Status / Scope**：`candidate`：有稿内证明及内部语义核对，尚未重审全部证明。\(r_F\) 为全部输出纤维的 inf；没有额外证明 \(J_{\mathcal G}=J_{\lambda F}\) 时，不得把定理写成全算子完整 resolvent 结论。旧稿中的数值兼容常数不能代替实际收缩率。

<a id="c02-v2"></a>
## C02-v2 · 同图块单值局部 RLEB–PPA 条件定理

- **Status**：`derived-checked`，仅针对以下单值图块版本；C02 原稿身份连同未独立重核的多选择推广仍为 `candidate`。
- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R^n\) 固定同一 \(F,\mathcal G,S,U,\lambda,L,0<\gamma\le1,R,\bar t,\psi,\kappa\)，其中 \(S\subset F^{-1}(0)\) 非空闭、\(U\) 开、\(\psi:[0,\bar t]\to[0,\infty)\) 非减、\(\psi(0)=0\) 且在零连续、\(0<\kappa<1\)。对每个 \(x\in U_R=\{x\in U:d(x,S)\le R\}\)，同一图块有 proximal 输出和最近零锚 \((p,0)\)；该图块的每个适用输入点对满足尺度 \(R\) 的全对 RL；每个实际输出满足完整真残差 EB；\((R+LR^\gamma)/(2\lambda)\le\bar t\)，且全部 \(0<t\le R\) 有 \(\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t\)。对每个 \(x^0\in U_R\) 再要求 \(\mathcal L(d_0)<\operatorname{dist}(x^0,\mathbb R^n\setminus U)\)。则唯一图块轨道无限继续、留在 \(U_R\)、有限长并收敛到 \(S\)；\(d_k\le\kappa^kd_0\)、\(s_k\le(\kappa^kd_0+L\kappa^{\gamma k}d_0^\gamma)/2\)，到极限的尾界为 \(\mathcal L(\kappa^kd_0)\)。其中 \(\mathcal L(d)=\tfrac12[d/(1-\kappa)+Ld^\gamma/(1-\kappa^\gamma)]\)。
- **Dependencies / Evidence**：[R01 代数与 R02 归纳证明](research/rleb_ppa.md#r02-proof) 从同图块零锚、平行四边形、真实输出 EB、严格预算和 Euclidean 完备性逐步重建；[C136](research/canonical/solution_selection_rates.md#ss-rleb-ball) 再加共同球条件才给统一尾与极限选择模。历史原稿仅是来源线索。
- **Counterevidence / Objections / Scope**：局部单值只对 \(\mathcal G\) 有效；完整 \(J_{\lambda F}\) 可在同输入有额外分支，需在共同可达输入上另证全纤维一致。多选择 extension、能量分支 R03 及一般 Dini 版本不从本版本自动获得；本状态也不判新颖性。

<a id="c03"></a>
## C03 · 全局双向 simultaneous shadow

- **Status**：`derived-checked`；原全图 Hilbert 身份、同一正反影子、σ 族常数与任意维数统一最优性均有独立完整证明。
- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert H，允许无限维及非可分；非空完整关系图满足固定 λ,L>0、0<γ<1 的全对全尺度 RL。R=L^{1/(1−γ)}。存在一个强单调双 Lipschitz 同胚 A:H→H，对每个原图点同时有 ‖v−A(x)‖≤R/(√2λ)、‖x−A⁻¹(v)‖≤R/√2。更一般每个 0<σ<1 有同一个 Aσ 及 GSH-3/10/11/13 的半径与常数；σ=√γ 最小化显示半径。
- **Definitions / Dependencies / Evidence**：[GSH-1–22 全部证明](research/canonical/global_shadow.md#gsh-object) 将任意指标集 ℓ²(D) 提升、任意 Hilbert 间同常数 Lipschitz 扩张的准确接口、双 Banach 反演、全图交叉配对和正则单纯形双向下界展开。C03 不依赖有限 QP 的 C19、graph-maximal、原图闭或 C04 的满纤维。[来源 S23 §3](history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 仅作同身份溯源。
- **Counterevidence / Scope**：1/√2 是所有有限维共同常数的最优因子，不决定每个固定维数最优值或 conditioning 锐性。保留指定图锚的不同命题由 [GSH-19–22](research/canonical/global_shadow.md#gsh-anchor) 另证最优因子 1；不能把它与无锚结论合并。逐图点界不提供原纤维非空、局部 RL 推广、真实逆分支选择稳定或外部新颖性。

<a id="c04"></a>
## C04 · 有限维完整纤维分类

- **Status**：`derived-checked`；原固定参数有限维双向分类在 FF1–27 完整重构并独立逐式接收，未扩大必要性的维数。
- **Exact Statement / Objects / Domain / Quantifiers**：固定 n≥1、λ,L>0、0<γ<1、R=L^{1/(1−γ)}。在 Rⁿ 的固定参数 graph-maximal 全尺度 RL 关系中，K 能作为某个关系的完整 F⁻¹(0)，当且仅当 K 非空紧且 diam K≤R；完整 F(0) 的对应门为 diam K≤R/λ。每个这样的关系对全部输入/输出有非空紧纤维；反向是每个合法 K 分别存在某个关系，不同时任意指定一个关系的两种纤维。
- **Definitions / Dependencies / Evidence**：[FF1–27 全部证明](research/canonical/finite_fiber_classification.md#ff-object) 给同参数 Cayley 极大性、显式有限维 Brouwer 闭球满射、properness/闭图/usc、完整纤维直径；Hilbert 投影短证明、凸包余量、全对正 bump、正权一致级数与无额外 fixed point；最后完整双向 pullback。原 S23 finite_geometry/margin/fixedset/fibers 仅溯源。该证明显式导入已声明前件的 Brouwer；不以 degree 摘要作为证明。
- **Counterevidence / Scope**：任意 Hilbert 空间上的紧 K 同常数 fixed-set 实现与双向实现是已证充分性；每个关系的纤维非空紧必要性只在有限维。实现图极大性允许最小 Hölder 常数小于参数上界 L，包括 singleton。R_K 的像只包含于闭凸包，未声称满射该凸包。graph-maximal 不是极大单调，不授予 PPA 真 EB、收敛、回缩、degree 数值或外部先行性。

## C05-v1 · 原关系局部值域的有限数据拓扑证书（9/25 稿候选）

- **Status**：`candidate`，仅保留 PDF 原稿的精确候选身份；C05-v2 的条件证明不是对原稿逐行验收。

- **Exact Statement / Objects / Domain**：\(F:\mathbb R^n\rightrightarrows\mathbb R^n\)，完整闭非空零集 \(S=F^{-1}(0)\)；\(\lambda,L>0\)，\(0<\gamma<1\)，\(q\gamma>1\)，\(\kappa>0\)，\(\phi(r)=(r+Lr^\gamma)/2\)、\(c=\kappa\lambda^{-q}\)。指定的实际 proximal 对应 \(T(p)\) 在相关窗满足 \((p-y)/\lambda\in F(y)\)、\(\|p-y\|\le\phi(d(p,S))\)、\(d(y,S)\le c\|p-y\|^q\) **对每个** \(y\in T(p)\)。两个非空紧有限多面体 \(A,B\) 且 \(A\subset\operatorname{int}B\)；\(T\) 在 \(A\) 某邻域 upper semicontinuous，且该邻域每个值非空紧 Čech-\(\mathbb Q\)-acyclic；经验证有限样本定义的包络在 A／B 的 collar 满足 PDF (8.4)：\(\sup_Au_E\le u\)、\(\inf_{B\setminus\operatorname{int}A}g_E\ge m>0\)、\(\phi(u)<d(A,B^c)\)、\(\alpha=c\phi(u)^q<m\)。\(H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 对每个 j 满射，且 \(\chi(A)\ne0\)。
- **Conclusion**：\(B(0,(m-\alpha)/\lambda)\subset F(\operatorname{int}A)\)；更一般地，\(\sup_A\|h\|<(m-\alpha)/\lambda\) 的连续 \(h:A\to\mathbb R^n\) 有 \(x\in\operatorname{int}A\) 满足 \(h(x)\in F(x)\)、\(d(x,S)\le\kappa\|h(x)\|^q\)。
- **Dependencies / Evidence**：[9/25 PDF §8 Theorem 8.1](history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)；有限样本包络及另需整窗条件的 collar 已独立重算为 [C70-v1](research/canonical/finite_sample_collar.md)，其后 Vietoris–Begle 与有理 morphism Lefschetz theorem 仍是 C05 的拓扑链。[LIT-GRN-2002](research/LITERATURE.md#lit-grn-2002) 已逐项核一手 [6, Theorem 6.2] 的 retract、Vietoris span、紧 morphism \(\subset CAC\) 与 Lefschetz 数导入；这只关闭引文适用门。
- **Objections / Status / Scope**：**PDF-only 来源候选**：原稿整条新增模块没有按其原有条件逐行审计；后来 C05-v2 的独立条件证明也适用于本 v1 的幂参数范围，但它不是原稿审计或来源版本确认。全文明言它不从全图 RL 自动推出；有限观测不证明整窗 (8.1)–(8.2) 或 \(T\) 的存在、usc 和 acyclicity。稿件的紧度量值 Čech cohomology/homology 等价及其余包络推理继续按明示范围核，不因外部定理导入核验而自动升级 C05。

## C05-v2 / LR-RANGE · 去除超临界幂条件的整窗条件定理

- **Status**：`derived-checked`，仅指下述全部整窗假设给定后的条件推导；原生模型的这些假设尚未认证。

- **Exact Statement / Objects / Domain / Quantifiers**：保持 C05-v1 的同一完整 \(F:\mathbb R^n\rightrightarrows\mathbb R^n\)、非空闭 \(S=F^{-1}(0)\)、\(\lambda,L,\kappa>0\)、\(0<\gamma<1\)、两个非空紧有限多面体 \(A,B\) 且 \(A\subset\operatorname{int}B\)、指定 \(T\) 的全部整窗输出 (8.1)–(8.2)、独立核定的非空有限样本与 (8.4) 四项 collar、usc 非空紧有理 Čech-acyclic 值、每阶 \(b^*\) 满射及 \(\chi(A)\ne0\)。**仅把 \(q\gamma>1\) 改为 \(q>0\)**，仍取 \(c=\kappa\lambda^{-q}\)。则对每个 \(\lambda\|h\|_{\infty,A}<m-\alpha\) 的连续 \(h:A\to\mathbb R^n\)，有 \(x\in\operatorname{int}A\) 满足 \(h(x)\in F(x)\)、\(d(x,S)\le\kappa\|h(x)\|^q\)；尤其 \(B(0,(m-\alpha)/\lambda)\subset F(\operatorname{int}A)\)。所有数字、集合、对应及样本须属于同一实例。
- **Definitions / Dependencies / Evidence**：[LR-OBJECT/THEOREM](research/canonical/local_range_without_supercriticality.md#lr-theorem) 在 [C70-v1](research/canonical/finite_sample_collar.md) 度量链之后，核紧图、Vietoris–Begle、线段与扰动同伦、上同调满射和 [LIT-GRN-2002](research/LITERATURE.md#lit-grn-2002) 的 coincidence 导入。9/25 PDF §8 是 C05-v1 的来源，不是本版本原文；本版本为新增 derived-checked 条件推导。[LR-FEASIBLE](research/canonical/local_range_without_supercriticality.md#lr-feasible) 给 \(q\gamma=1/2\) 的全项实例，排除删条件后 vacuous 的解释。
- **Counterevidence / Objections / Status / Scope**：有限样本仍不能认证指定 \(T\) 在整个窗的非空、usc、acyclic 或 (8.1)–(8.2)；实际原生问题可能无法生成合适的 (8.4)。外部拓扑导入适用门已核，但整条候选的文献新颖性、原生模型和其它定理推广未审。删去 \(q\gamma>1\) 是数学身份变化，不回写 C05-v1 的来源事实；若未来出现 Čech/CAC 的承重异议，应降回候选并隔离拓扑结论。

## C06 · 固定紧 T-only 图卡的内生观测

- **Status**：`derived-checked`；本仓库已从对象定义重构完整 proper/quotient 证明并作独立逆向审读，范围仅为此固定紧源 T-only 图卡。

- **Exact Statement / Objects / Domain**：非空紧 \(K\subset\mathbb R^d\)，非空闭 \(S\subset K\)。令 \(X=\{T\in C(K,K):T|_S=I,\ T^n\to\Pi_T\text{一致},\Pi_T(K)\subset S\}\)，全时间度量 \(d_{\mathrm{all}}^K(T,U)=\sup_{n\ge0}\|T^n-U^n\|_K\)。定义 \(w_n(T)=\max\{\sup_{k,\ell\ge n}\|T^k-T^\ell\|_K,\ \sup_{k\ge n,x\in K}d(T^kx,S)\}\)：第一项看**所有尾部两迭代差**，不是仅相邻步差。令 \(m_j=\sup_{\|x-y\|\le2^{-j}}\|(2T-I)x-(2T-I)y\|\)。则 \(\Phi:X\to c_0\times c_0\)，\(T\mapsto(w,m)\) 连续 proper；其实际像闭 Polish，非空精确纤维紧/Baire，映射到像 perfect/quotient。
- **Dependencies / Evidence**：[CT-OBJECT/PROPER](research/canonical/compact_t_observation.md#ct-proper) 的闭迭代嵌入、共同模与尾预算、Arzelà–Ascoli、全时间收敛和闭映射证明；两路独立条件/反例审读。历史 [9/20 `06_math_audit.md` §1](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md) 仅定位来源。
- **Objections / Status / Scope**：\(X\ne\varnothing\) 当且仅当 \(S\) 是 \(K\) 的回缩像；空 \(X\) 时非空纤维结论无实例。proper/quotient 不推出 category-preserving；局部 \(T\) 不代表完整全局 \(F\)，也不证明总体规模比较。

## C07 · 原 Baire／多孔性比较量尺的塌缩报告

- **Status**：`source-report`；缺失的原证明不能由来源总账的“verified”标签替代。

- **Exact Statement / Objects / Domain**：9/21 包报告在其先前定义的完整图 Polish／普通 \(C^0\) 与动力度量 \((X_D,d_{\rm dyn})\) 中，正 Hölder 类受共同粗糙化影响；特别 \(\mathcal R_D\subseteq\mathcal H_+\in\sigma\mathcal P^-(X_D,d_{\rm dyn})\)，所以 \(\mathcal R_D\setminus(\mathcal L_D\cup\mathcal M_D)\in\sigma\mathcal P^-\subseteq\sigma\mathcal P^+\)。\(\sigma\mathcal P^-\) 是包内的 σ-lower-porous 类。**域 \(D\)、全部图卡与孔隙常数须在原证明恢复后冻结，不由此摘要补造。**
- **Dependencies / Evidence**：[9/21 `02_VERIFIED_CORE.md` §6](history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md) 与 [`03_NO_GO_LEDGER.md` N05、N08、N10](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)；v0.9 区分 V-A/V-B、SOURCE-MISSING。
- **Objections / Status / Scope**：**历史总账报告，尚非本仓库重构的原孔隙证明**；I-097–099 原审计和 I-102 正式表示稿未在盘点文件名中找到。总账另标 SOURCE-MISSING 的 I-001/I-002/I-003–005/I-059/I-075 已以原包或展开件恢复，但这不能替代 N10 原证明。旧目标“差集非 σ-upper-porous”只在其所指空间中被报告为假，不是所有合理量尺均失败。 有限维AW固定输入前身与一致拓扑Hölder前身现分别有[C179](research/canonical/attouch_wets_fixed_input_thinness.md#aw-object)/[C180](research/canonical/uniform_holder_thinness.md#uht-object)的自足受限证明；不把这两个不同母空间的结论合并为本条动态孔隙定理。

## C08-v1 · 解选择稳定性（修订身份）

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain**：一族在共同区域有轨道与统一尾界的 \(T\)，满足局部 \(\|Tx-Ty\|\le H\|x-y\|^\gamma\)，\(0<\gamma<1\)。若 \(\|T^kx-\Pi(x)\|\le M\sigma^k\) 对全体初值和 \(k\ge0\) 一致成立，则 \(\|\Pi(x)-\Pi(y)\|\le C(\log\log(1/\delta)/\log(1/\delta))^\beta\)，\(\beta=\log(1/\sigma)/\log(1/\gamma)\)；若统一尾界 \(M e^{-c_0\nu^k}\)，\(\nu>1\)，则是 \(C e^{-c(\log(1/\delta))^\alpha}\)，\(\alpha=\log\nu/\log(\nu/\gamma)\)，足够小 \(\delta=\|x-y\|>0\)。修订包给完整 proximal 的显式半代数例说明即使点误差 Q-二次，\(\Pi\) 也无需正阶 Hölder。
- **Dependencies / Evidence**：[SS-TRANSFER 独立证明](research/canonical/solution_selection_rates.md#ss-transfer) 给出有限前缀的共同局部尺度闭合及两种平衡指数；来源 [原 `research_note.md` §1–4](history/sources/次单调论文研究/正式后的研究/research_note.md)、[修订审计 ZIP](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)，9/21 `02_VERIFIED_CORE.md` §4。
- **Objections / Status / Scope**：抽象模传递部分 `derived-checked`，原修订包的内部审计是来源证据。一般 RLEB 推论只能直接用于局部 \(J_{\mathcal G}\)，或另加共同轨道区域 \(J_{\lambda F}=J_{\mathcal G}\)；旧稿无条件升级完整 resolvent 的版本已失效。固定解点的 anchored Hölder calmness 与邻域中任意两初值的 Hölder 连续性不同。具体二次模型另立 C115/C116，不把来源中两个例子混成同一对象。

<a id="c09"></a>
## C09 · 9/19 一般模 RL 的 Dini 点收敛（新增版本）

- **Status**：`derived-checked`；GM1–18 在原有限维同图块量词下完整重构并独立逐式接收。

- **Exact Statement / Objects / Domain / Quantifiers**：\(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，非空闭 \(S\subset F^{-1}(0)\)，同图块 \(\mathcal G\)，\(U\) 开、\(R,\bar t,\lambda>0\)，连续非减 \(\omega:[0,R]\to[0,\infty)\)、\(\omega(0)=0\)、非减 \(\psi:[0,\bar t]\to[0,\infty)\)，\(\psi(0)=0\) 且在原点右连续、\(0<\kappa<1\)。对**每个** \(x\in U_R\) 假设图块输入覆盖与最近解点 \((p,0)\in\mathcal G\)；对**每对**图点在输入尺度 \(R\) 有 \(\|\Delta u-\lambda\Delta v\|\le\omega(\|\Delta u+\lambda\Delta v\|)\)；在全部实际输出有真实 \(r_F\) EB；\((R+\omega(R))/(2\lambda)\le\bar t\)；对每个 \(0<t\le R\) 有 \(\psi((t+\omega(t))/(2\lambda))\le\kappa t\)；且 \(\int_0^R\omega(t)dt/t<\infty\)。
- **Conclusion**：若 \(d_0\le R\) 且 \(d_0/[2(1-\kappa)]+\frac12\sum_{j\ge0}\omega(\kappa^jd_0)<d(x^0,X\setminus U)\)，则唯一图块轨道全程存在、有限长并收敛于 \(S\)；\(d_k\le\kappa^kd_0\)，步长与尾界按同一模级数。量词不自动覆盖完整 \(J_F\)。
- **Dependencies / Evidence / Objections / Status / Related Files**：[GM1–18 完整证明](research/canonical/general_modulus_dynamics.md#gm-data) 给一步真残差评价域、Dini/采样等价、连续长度函数和严格剩余预算归纳；9/19 S19 thm:modulus-dini 仅作溯源。C02 是幂次版，C09 改变模与额外条件，不能覆盖旧编号。

<a id="c10"></a>
## C10 · 完整对数接缝的 Dini 边界

- **Status**：`derived-checked`；GM26–39 给每个固定正参数的完整双支、全对模、真残差和动力边界证明。

- **Exact Statement / Objects / Domain / Quantifiers**：对**每个** \(a>0\)，\(\ell_a(0)=0\)，在 \(0<t\le e^{-a}\) 为 \([\log(e/t)]^{-a}\)，以后用接点切线延伸。\(F_a(\xi,y)=\{(-\ell_a(4y),3y),(-\ell_a(4y),-5y)\}\) 当 \(y\ge0\)，其余空。步长 1，\(S=\mathbb R\times\{0\}\)。
- **Conclusion**：完整 \(J_a(p,q)=(p+\ell_a(|q|),|q|/4)\)，整图有非幂次模 \(\Omega_a(t)=\sqrt{(t+2\ell_a(t))^2+9t^2/4}\) 且真实残差在 \(y\ge0\) 为 \(r_{F_a}(\xi,y)=\sqrt{\ell_a(4y)^2+9y^2}\)，域外为 \(+\infty\)。对每个 \(|q_0|>0\) 距离按 \(4^{-k}\) 收缩，轨道有限长且收敛于一点当且仅当 \(a>1\)；若 \(a\le1\)，切向坐标趋 \(+\infty\)。
- **Dependencies / Evidence / Objections / Status / Related Files**：[GM26–39 完整证明](research/canonical/general_modulus_dynamics.md#gm-log-object) 重构切线延拓凹性/次可加、完整正负支反演、跨支全对模、真残差与逆 gauge、小尺度兼容和正负初值长度；S19 thm:logarithmic-seam 只溯源。必要性只对**此族**，不是“非 Dini 必发散”的一般断言。

<a id="c11"></a>
## C11 · 统一尾给连续极限回缩

- **Status**：`derived-checked`；同一 C09 前件下 GM19–25 的精确预算、开域、共同尾及显式局部同伦完整重构。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 C09 的 \(X=\mathbb R^n\)，其整套局部假设在 \(U_R\) 成立，置 \(\ell_\omega(r)=r/[2(1-\kappa)]+\frac12\sum_{j\ge0}\omega(\kappa^jr)\)，\(\mathcal O=\{x\in U:d(x,S)<R,\ell_\omega(d(x,S))<d(x,X\setminus U)\}\)。
- **Conclusion**：\(\mathcal O\) 开且正向不变，包含 \(S\cap U\)；每个 \(x\in\mathcal O\) 的极限 \(\Pi(x)\) 构成连续回缩 \(\mathcal O\to S\cap U\)，所以 \(S\cap U\) 为 Euclidean neighborhood retract。局部可缩的明确量词是：每个 p 及其相对邻域 V 存在更小 W⊂V，使包含 W→V 在 V 内同伦于常值 p；未声称 W 本身可缩或强形变回缩。
- **Dependencies / Evidence / Objections / Status / Related Files**：[GM19–25 完整证明](research/canonical/general_modulus_dynamics.md#gm-retraction) 用 s+ℓω(d⁺)≤ℓω(d) 得前向不变，在整个 O 上用同一 ℓω(κᵏR) 尾；线段后复合 Π 给局部同伦。S19 prop:limit-retraction 只溯源；不需增加完整纤维等式或 S=F⁻¹(0)。C04 的任意紧零集实现未附 C11 假设；Cantor 型零集不能在相应点满足整套条件。

## C12-v0 · 随机推论的原 Polish 措辞

- **Status**：`refuted`，仅针对将 Polish 理解为拓扑可完备、而所指定度量不必完备的精确版本。
- **Exact Statement / Objects / Domain / Quantifiers**：S19 thm:stochastic-rleb 取 \((\mathsf X,d)\) “Polish”、闭 \(S\)、适应过程 \(X_k\)，记 \(D_k=d(X_k,S)\)、\(s_k=d(X_{k+1},X_k)\)；过程留在 \(0\le D_k\le R\) 的不变域、非减 Dini \(\omega\)、\(0<\kappa<1\)，逐路径 \(s_k\le(D_k+\omega(D_k))/2\) 和 \(\mathbb E[D_{k+1}\mid\mathcal F_k]\le\kappa D_k\)。原结论为 \(\sum s_k<\infty\) 且 \(X_k\to X_\infty\in S\) 几乎处处。
- **Counterevidence / Scope**：若 Polish 只保证拓扑可完备，极限在 \(S\) 的结论**错误**。\((0,2)\) 的通常距离、闭 \(S=\{2^{-n}:n\ge1\}\)、确定性 \(X_k=2^{-(k+2)}+4^{-(k+2)}\)、\(\omega(t)=4\sqrt t\)、\(R=1/16,\kappa=1/4\) 满足前件而 \(X_k\to0\notin\mathsf X\)。有限长度求和部分不受影响。[H06](research/holder_structure.md#stoch)、[F07](FAILED_ROUTES.md#f07)。

## C12-v1 · 给定度量完备的修补推论

- **Status**：`derived-checked`，仅指补充指定度量完备后从有限长度到空间内极限的修补；原稿未据此自动改版。
- **Exact Statement / Objects / Domain / Quantifiers**：在**给定度量 \(d\) 完备**的 \((\mathsf X,d)\) 上取非空闭 \(S\)，适应过程 \(X_k\)，\(D_k=d(X_k,S)\)、\(s_k=d(X_{k+1},X_k)\)。假设过程留在 \(0\le D_k\le R\) 的不变域、\(\omega\) 非减且 Dini、\(0<\kappa<1\)，逐路径有 \(s_k\le(D_k+\omega(D_k))/2\)，并且 \(\mathbb E[D_{k+1}\mid\mathcal F_k]\le\kappa D_k\)。则 \(\sum_k s_k<\infty\)，\(X_k\to X_\infty\in S\) 几乎处处。
- **Dependencies / Evidence / Scope**：[H06](research/holder_structure.md#stoch) 的截断阈值、Dini 求和与 Tonelli 给有限长度；指定度量完备给 Cauchy 极限，闭 \(S\) 给极限归属。仅拓扑 Polish 的 C12-v0 被反例否定，不得混成同一假设集。修补不代表原稿其它随机断言或外部先行性已验收。

## C13 · 冻结面 CRSC 与 MSCQ（锥旁支）

- **Status**：`candidate`；内部证明包和承重步骤已有核读，完整退化分支与外部定理适用门仍待独立审查。

- **Exact Statement / Objects / Domain / Quantifiers**：有限维 \(X,E\)、闭尖满维 nice 凸锥 \(C\)、\(C^1\) 映射 \(G\) 在 \(\bar x\) 满足 \(G(\bar x)=0\)。设 \(A=DG(\bar x)\)，\(\mathfrak F=F_{\min}(\operatorname{Im}A\cap C)\)，\(H=\mathfrak F^\perp\)，\(S_{\mathrm{dual}}=\operatorname{span}(C^*\cap\mathfrak F^\perp)\)。假设 \(A^*C^*\) 闭、存在 \(\bar x\) 的开邻域使 \(\operatorname{rank}(DG(x)^*|_H)\) 对其中每个 \(x\) 恒定，且参考面 \(\mathfrak F\) amenable。闭像与邻域常秩前件即这里列明的两项。
- **Conclusion**：冻结秩夹逼使面稳定，经共同法向流形与切向修正，存在邻域和 \(\kappa<\infty\)，对其中每个 \(x\) 有 \(d(x,G^{-1}C)\le\kappa d(G(x),C)\)。此为**当前单系统参考面**的条件结论。另对固定 proper nice 锥，“每个在顶点冻结 CRSC 的 \(C^1\) 系统均 MSCQ”与**整个锥每个面 amenable** 等价；逆向测试是各面的线性嵌入。单个参考面 amenable 不蕴含全锥的普遍结论。
- **Dependencies / Evidence / Objections / Status / Related Files**：[cone_markov §1](research/cone_markov.md)，S14C 主稿及 CM-C 证明包。内部审计与承重步骤重读；正式版文献和退化常数分支待独立核。该锥距离残差不是 \(r_F\)，不能自动迁移 RLEB。

## C14 · 紧 Markov 同步残差的 exact-zero 门槛

- **Status**：`derived-checked`；原 a.e. 连续量词下的整条紧性、取得、下半连续和严格 gauge 证明已在 CG1–CG7 独立重构。

- **Exact Statement / Objects / Domain / Quantifiers**：非空紧状态集 \(G\subset\mathbb R^d\)，任意概率噪声域上联合可测的随机自映射；存在同一个可测满概率噪声集，使其中每个 \(T_\xi:G\to G\) 在整个 \(G\) 连续。独立新噪声定义核 \(P\)，保留原不变律集合 \(\mathcal I\ne\varnothing\) 假设；其非空性另由 Cesàro 证明。\(\Psi(\mu)^2=\inf_{\pi\in\mathcal I}\inf_{\eta\in\operatorname{Opt}_{W_2}(\mu,\pi)}\int\mathbb E\|(x-T_\xi x)-(y-T_\xi y)\|^2d\eta\)；两侧**同噪声**，内层必须为该两边缘的平方成本最优耦合。
- **Conclusion**：在该紧连续设置下，极小值取得、\(\Psi\) 下半连续，且 \(\Psi^{-1}(0)=\mathcal I\) 当且仅当存在严格一般 gauge \(\rho\) 使 \(d_{W_2}(\mu,\mathcal I)\le\rho(\Psi(\mu))\) 对每个概率律成立。没有自动幂次或速率兼容。
- **Dependencies / Evidence / Objections / Status / Related Files**：[CG1–CG7 完整证明](research/topics/random_markov/compact_residual_boundaries.md#crb-general-gauge) 给核和同步成本的有界控制收敛、全部目标的联合最优计划闭性、取得/lsc、严格包络及两个方向；CM-M Theorem 1 仅作来源。此共同噪声异常集量词不能换成逐状态异常集；\(\Psi\) 表示依赖，不是 \(W_2(\mu,\mu P)\)，也不从本条推出上半连续、幂次界或速率兼容。

## C15-v1 · 固定有限状态的顶点判定

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定有限状态几何、随机映射与概率，C14 的同一 \(\Psi\)；枚举最优运输对偶 tight-edge 图产生的有限计划多面体，令 \(\mathcal V\) 为全部顶点，\(E(\mu)=d_{W_2}(\mu,\mathcal I)^2\)，\(R\cdot v\) 为同步残差成本。
- **Conclusion**：\(\Psi^{-1}(0)=\mathcal I\) 当且仅当每个 \(v\in\mathcal V\) 且 \(R\cdot v=0\) 的行边缘在 \(\mathcal I\)，当且仅当存在 \(B<\infty\) 对**所有**律有 \(E(\mu)\le B\Psi(\mu)^2\)；最佳平方系数为 \(\max_{v:R\cdot v>0}E(r(v))/(R\cdot v)\)，空集最大值 0。
- **Dependencies / Evidence / Objections / Status / Related Files**：[FS-CELLS/THEOREM](research/topics/random_markov/finite_state_certificate.md#fs-theorem) 独立重建 LP 对偶有限 tight-edge 分支、完整耦合与凸目标顶点证明；[FS-HOFFMAN](research/topics/random_markov/finite_state_certificate.md#fs-hoffman) 用非空零面的 Hoffman 界及空零面的紧性提供另一个非锐存在性证明，状态 `derived-checked`。[cone_markov CM-FINITE](research/cone_markov.md#m-fin) 是早期摘要，来源 CM-M Theorem F。此处 \(G\) 有有限个互异点，\(R\) 由同噪声成本给定，\(\mathcal I\) 遍历所有不变律；没有暗加最近不变律或混合性。只针对固定数据，不承诺多项式算法、动力收敛或无限状态推广。

## C16 · 匹配公共接口下的 LT→RLEB 能量证书

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：有限维完整原图且全域单值 \(T=J_{\lambda F}\)，\(\lambda>0,\tau\ge0,\rho>0\)，同一非空闭目标 \(S\subset F^{-1}(0)\)、同域最近零锚、同一 coverage/测试域/真实残差、gauge 评价域和留域接口；公共 all-pairs LT 假设 \(\operatorname{Lip}(2T-I)\le\sqrt{1+4\tau}\)、\(d(u,S)\le\rho r_F(u)\) 和 \(2\tau(\lambda+\rho)^2<\lambda^2\)。
- **Conclusion**：在此接口中取 \(\gamma=1,L^2=1+4\tau,\psi(t)=\rho t\)，能量分支的 \(q_E=(1+2\tau)\rho^2/(\rho^2+\lambda^2)<1\)，故公共 LT 证书类包含于相应 RLEB 能量证书类。不是完整 LTT 框架全部版本的包含，也不保存最佳常数或最大域。
- **Dependencies / Evidence / Objections / Status / Related Files**：R03 的能量式及归一化代数，[operator_space §2](research/operator_space.md)，S20 OS-H §3.2。状态 `derived-checked` 只针对上述匹配接口的代数转换；不推出两类在自然母空间的大小差异。\(\rho=0\) 时 \(\alpha(t)=t/\rho\) 无定义，若有退化 EB 须另列版本；signed \(\tau\) 不由此条覆盖。

## C17 · 固定紧 T-only 图卡的 proper \(\Phi\)（C06 的范围细化）

- **Status**：`derived-checked`（直接引用 C06 的同一规范证明）；范围细化不另立较强定理。

- **Exact Statement / Objects / Domain / Quantifiers**：C06 的非空固定紧 \(K\)、闭 \(S\subset K\) 和全时间度量空间 \(X\)；尾 \(w_n\) 同时看所有 \(k,\ell\ge n\) 的迭代差与到 \(S\) 距离，反射模 \(m_j\) 看输入尺度 \(2^{-j}\) 的 \(2T-I\)。
- **Conclusion**：\(\Phi=(w,m):X\to c_0^2\) 连续 proper，像闭 Polish，非空精确纤维紧；这与 C06 同一数学身份，是释义细化，**不另造较强定理**。
- **Dependencies / Evidence / Objections / Status / Related Files**：[CT-PROPER](research/canonical/compact_t_observation.md#ct-proper) 与 [operator_space §3](research/operator_space.md#phi)；S20 OS-A §1 只作溯源。Arzelà–Ascoli 需紧参数集在 \(c_0\) 中的一致趋零预算；proper/quotient 不推出 category-preserving，局部图卡不恢复完整全局 \(F\)。

<a id="c18"></a>
## C18 · 有限维固定窗口的全纤维值域覆盖

- **Status**：`derived-checked`；FC1–12 完整重构并独立接收，限定于全尺度同参数关系、全部纤维与显示窗口。
- **Exact Statement / Objects / Domain / Quantifiers**：固定 n≥1、λ,L>0、0<γ<1，R=L^{1/(1−γ)}。全局 graph-maximal RL 关系 F 取任意图锚 (x₀,v₀)；每个 r>R 有唯一 h(r)∈(0,r) 解 r−h=L(r+h)^γ。则对每个 v∈B(v₀,h(r)/λ)，整个非空 F⁻¹(v)⊂B(x₀,r)，因此该输出球⊂F(B(x₀,r))。固定窗版本另取任意 U,W⊂Rⁿ 与非空全尺度 RL 图 G⊂U×W，在该同窗中相对 graph-maximal，锚属于 G、B(x₀,r)⊂U、B(v₀,s)⊂W、r>R、s>0；则每个 v∈B(v₀,min{s,h(r)/λ}) 的整个非空 G⁻¹(v) 在该输入球，且等于任一同参数 completion 的对应完整纤维。
- **Definitions / Dependencies / Evidence**：[FC1–12](research/canonical/full_fiber_coverage.md#fc-object) 展开最大根定位、严格增性、有限维 Brouwer 全目标满射、同参数 completion 与窗口限制身份、全纤维全称界，以及一维 C(p)=L(p₊)^γ 同对象的半径与严格门锐性。C04 的 [FF-COERCIVITY](research/canonical/finite_fiber_classification.md#ff-coercivity) 另给同一全值域证明；来源 S23 lem:rho/coverage/window/coveragesharp 只溯源。
- **Counterevidence / Scope**：统一半径不可提高，r≤R 下没有全类统一的正中心输出球；不声称每个指定关系最佳半径相等。不是任意非相对极大子图、仅局部测试 RL 的覆盖，亦不认证 S25 指定整窗拓扑 T。全部纤维身份只授予列出的目标球，未认定窗口外完整关系相等；外部新颖性未核。

<a id="c19"></a>
## C19 · 有限样本的全局一致二次规划影子

- **Status**：`derived-checked`；仅限下列固定有限样本及已认证条件，完整自足证明已独立重构和攻击；其有限证明不依赖 C03/C04/C18。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 \(n,m\ge1,\lambda,L>0,0<\gamma<1\)，有限 \(m\) 个 \(\mathbb R^n\) 图样本，\(p_i=x_i+\lambda v_i,c_i=x_i-\lambda v_i\)，固定 \(0<\sigma<1\) 和 S23 的 \(M_\sigma,a^2=M_\sigma/2\)。对所有样本对有 \(\|c_i-c_j\|^2\le\sigma^2\|p_i-p_j\|^2+M_\sigma\)。按 [FD-1–3 规范定义](research/canonical/finite_data_proxy.md#fd-object) 的 \(Q,d(q),\Delta_m\) 定义唯一 QP 最小解 \(\theta(q)\) 与 \(N_m(q)=V\theta(q)\)。
- **Conclusion**：同一个 \(N_m:\mathbb R^n\to\mathbb R^n\) 全局 \(\sigma\)-Lipschitz，对每个 \(i,q\) 有 \(\|c_i-N_m(q)\|^2\le\sigma^2\|p_i-q\|^2+a^2\)；其 Cayley 代理 \(A_m\) 为强单调双 Lipschitz 同胚，对全部**样本点**有统一正反误差。对未知原图点还须 C20-v2 的同图、同尺度参数 coverage。
- **Dependencies / Evidence / Objections / Status / Related Files**：严格凸 QP、有限抬升插值、双变分不等式、两次 contraction 及强单调代数，完整证明 [FD-1–12](research/canonical/finite_data_proxy.md#fd-qp)。独立 reviewer 先从规范陈述重建加权/VI 证明，再核 S23 thm:finite_qp 的同一身份，逐式攻击本页正文；审查范围见 [本次记录](research/audit/BLIND_RECEIPT_2026-10-05_QP.md)。不依赖 C03/C04 或无限图 Kirszbraun 扩张；全球定义的代理不等于全球认证原关系，外部先行性未核。

<a id="c20-v1"></a>
## C20-v1 · 局部 RL 不限成对尺度的错误扩写

- **Status**：`refuted`。
- **Exact Statement / Objects / Domain / Quantifiers**：旧总账把 C19 的样本与未知图点放在“完整或明确图块 RL”内，要求未知 Cayley 参数距某样本至多 \(\delta\)，却**没有**要求两点属于同一已认证图块、\(\delta\) 落入局部 \(\mathrm{RL}(\lambda,\gamma,L;R_0)\) 的输入对尺度；仍声称 \(\lambda\|v-A_m(x)\|\le K_\delta\) 及后续全纤维界。
- **Counterevidence / Scope**：[F36](FAILED_ROUTES.md#f36) 的两点完整图在 \(R_0=1\) 上满足局部全对 RL，未知参数距样本为 \(\delta=2\)，但实际代理偏差为 100，超过旧公式的 \(K_2\)。此反例只否定这次规范总账的无尺度扩写，不否定 S23 全图全尺度原稿。局部图块外完整纤维的同图门另见 [C20-v2](#c20-v2)。

<a id="c20"></a>
<a id="c20-v2"></a>
## C20-v2 · 同图同尺度的参数覆盖与三项误差

- **Status**：`derived-checked`；在 C19 全部样本兼容、同图同尺度、完整非空纤维的全称 coverage 及独立反演误差证书下，FD-13–18 全链已独立重构。

- **Exact Statement / Objects / Domain / Quantifiers**：先继承 C19 的全部样本对兼容条件（局部 RL 不自动认证远距样本对）；C19 样本与每个待认证未知图点均属于**同一个**完整 RL 图或指定图块，且该点的 Cayley 参数 \(p=x+\lambda v\) 与某个样本参数 \(p_i\) 满足 \(\|p-p_i\|\le\delta\) **并在 RL 成对尺度内**：全尺度版自动满足，局部 \(\mathrm{RL}(\lambda,\gamma,L;R_0)\) 版以 \(\delta\le R_0\) 为充分门，亦可逐对直接验证 \(\|p-p_i\|\le R_0\)。置 \(b=L\delta^\gamma\)，\(K_\delta\) 为 [Q02](research/range_finite_data.md#q-cover) 的显式正根上界。若结论指向完整 \(F^{-1}(v)\)，该非空纤维的**每个图点**还必须属于同一 RL 图且逐个满足该覆盖和尺度门。对反演目标 \(v\) 的观测 \(\widetilde v\) 有 \(\|\widetilde v-v\|\le\eta\)，代理求值 \(\widehat x\) 须有 \(e_x\ge\|\widehat x-A_m^{-1}(\widetilde v)\|\) 的独立证书。若以候选参数 \(q\) 计算，取 \(\widehat x=q-\lambda\widetilde v\)，已认证的 \(e_N\ge\|\widehat N(q)-N_m(q)\|\) 还须和固定点残差合并，方得 \(e_x=(\|q-2\lambda\widetilde v-\widehat N(q)\|+e_N)/(1-\sigma)\) 的可用上界。
- **Conclusion**：每个被覆盖图点有 \(\lambda\|v-A_m(x)\|,\|x-A_m^{-1}(v)\|\le K_\delta\)；覆盖整个纤维才得对应 Hausdorff singleton 界。对每个 \(x\in F^{-1}(v)\)，\(\|x-\widehat x\|\le K_\delta+\lambda(1+\sigma)\eta/(1-\sigma)+e_x\)。可行 QP 解的 Frank–Wolfe gap \(G\) 仅给 \(\|V\widehat\theta-N_m(q)\|\le\sqrt G\)；取 \(\widehat N(q)=V\widehat\theta\) 才可置 \(e_N=\sqrt G\)，且还需上述固定点残差。浮点 gap 需验证容差。
- **Dependencies / Evidence / Objections / Status / Related Files**：C19、**同一可用尺度内的成对**原图 Hölder、同输入/同输出交叉估计、逆代理 Lipschitz 常数。[range_finite_data Q02/Q03](research/range_finite_data.md)，S23 thm:covered、cor:coveredfibers、prop:evaluation、cor:totalerror 只作溯源；[本次审查](research/audit/BLIND_RECEIPT_2026-10-05_QP.md) 独立重建正根、gap、反演与噪声链。完整规范证明 [FD-13–18](research/canonical/finite_data_proxy.md#fd-cover) 已独立逐式复核；全图全尺度是原稿身份，局部版是 C20-v2 原已固定的同图同尺度范围，身份未改变。\(\delta\)-网的获得和维数复杂度不自动保证；[F36](FAILED_ROUTES.md#f36) 阻断漏尺度版本。

## C21 · 有限总查询的全空间信息障碍

- **Status**：`derived-checked`，只对正文的确定性有限点查询模型和全空间误差结论；其余 oracle 模型另立问题。

- **Exact Statement / Objects / Domain / Quantifiers**：\(n\ge1,L>0,0<\gamma<1\)。对**任何**仅有限次（可自适应）点查询未知全局 \(L\)-Hölder \(C:\mathbb R^n\to\mathbb R^n\)、随后输出单值 \(A\) 且不再访问 oracle 的确定性程序，存在允许的 \(C\) 使 \(A\) 对其 RL 关系没有全空间统一有限正向纤维误差。
- **Dependencies / Evidence / Counterevidence / Status / Related Files**：零图的有限查询集 \(E\) 与 \(C_1(p)=L d(p,E)^\gamma e\) 给同 transcript 而远端偏差无界。[range_finite_data Q04](research/range_finite_data.md)，S23 prop:information。稿内反例与本轮推理核读。结论不覆盖固定紧域、持续 oracle、随机保证或已知解析映射；它是精确查询模型的障碍。

## C22-v1 / RP-EB · 有限维不一致二次近端的条件律误差界

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定有限维欧氏空间 \(H\)、有限个正权重 \(p_i\)、\(\lambda>0\)，每支 \(T_i=\operatorname{prox}_{\lambda f_i}\)，其中 \(f_i(x)=\langle x,H_i x\rangle/2-\langle b_i,x\rangle\)、\(H_i=H_i^*\succeq0\)、\(b_i\in\operatorname{range}H_i\)。逐步使用与当前状态独立、同分布的新索引。令 \(U=\cap_i\ker H_i,V=U^\perp\ne\{0\}\)；在 \(V\) 上 \(A_i=(I+\lambda H_i)^{-1}\)、\(c=\sqrt{\lambda_{\max}(\sum_i p_i A_i^*A_i|_V)}<1\)。对**每一个固定** \(\nu\in\mathscr P_2(U)\) 和**所有**守恒边缘为 \(\nu\) 的 \(\mu\in\mathscr M_\nu\)，用同一条件距离 \(\mathsf W_\nu^2=\int W_2(\mu_u,\eta_u)^2d\nu\) 及**完整混合核** \(P\) 的真实 law-step 残差 \(\mathcal R_\nu(\mu)=\mathsf W_\nu(\mu,\mu P)\)。
- **Conclusion**：活跃核有唯一 \(\pi\in\mathscr P_2(V)\)，所有联合有限二阶矩不变律恰为 \(\{\nu\otimes\pi:\nu\in\mathscr P_2(U)\}\)。置 \(E_\nu(\mu)=\mathsf W_\nu(\mu,\nu\otimes\pi)\)，则 \((1-c)E_\nu\le\mathcal R_\nu\le(1+c)E_\nu\)，\(E_\nu(\mu P^k)\le c^kE_\nu(\mu)\)，且 \(\sum_{k\ge0}\mathsf W_\nu(\mu P^{k+1},\mu P^k)\le\mathcal R_\nu(\mu)/(1-c)\)。
- **Definitions / Dependencies / Evidence**：[规范证明 RP-OBJECT→RP-GAP→RP-CONTRACTION→RP-EB](research/canonical/random_proximal.md#rp-eb) 给矩阵谱隙、同步耦合、不变律分类和三角不等式。9/14 [历史相关性感知报告](research/canonical/random_proximal.md#rp-object) 是来源线索；本轮重算关键步骤。标量子族证明统一 EB 系数 \(1/(1-c)\) 的类内尖锐性。
- **Counterevidence / Objections / Status / Scope / Related Files**：本轮推导 `derived-checked`，未核外部优先权。不能把 \(\mathcal R_\nu\) 换成逐支推前残差、同步 OT 缺陷、物理步长或普通联合 \(W_2\) 的同名量词。\(V=0\)、无限维、权重或参数随守恒坐标变化均是新版本义务。历史脚本运行仅属有限观察；精确路径和输出在[审计](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md)。

## C23-v1 / RP-BRANCH · 分支残差的零集边界

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：有限个 firmly nonexpansive \(S_i:H\to H\)，每支有固定点，所有 \(p_i>0\)；对**每一个** \(\mu\in\mathscr P_2(H)\)，\(\sum_i p_i W_2(\mu,(S_i)_\#\mu)^2=0\) 当且仅当 \(\mu(\cap_i\operatorname{Fix}S_i)=1\)。\(H\) 是有限维欧氏空间；该命题不要求 \(S_i\) 为同一个目标的近端。
- **Dependencies / Evidence**：firm nonexpansiveness 的定点平方不等式，分别积分并利用有限二阶矩与推前律相等。[规范证明](research/canonical/random_proximal.md#rp-branch)；标量不一致双近端给混合不变律存在而分支残差严格正的实例。
- **Counterevidence / Status / Scope / Related Files**：本轮 `derived-checked`；对象是逐支残差的零集，不能推出混合核不变律的零集判据。若取消每支固定点或换成同步缺陷，必须另立版本。[反例与尖锐例](research/canonical/random_proximal.md#rp-scalar)。历史 C11 复合次正则与现 C11 回缩同号，均不得占用 C22/C23 身份。

## C24-v1 / EX01 · 旋转 resolvent 收缩不蕴含强单调

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R^2\) 取 \(K(x_1,x_2)=(-x_2,x_1)\)，固定任意 \(\omega,\lambda>0\)，\(F=\omega K\)。完整 \(J_{\lambda F}=(I-\lambda\omega K)/(1+(\lambda\omega)^2)\) 在全空间的 Lipschitz 常数为 \((1+(\lambda\omega)^2)^{-1/2}<1\)，但 \(\langle x-y,Fx-Fy\rangle=0\) 对**全部** \(x,y\) 成立，故无正强单调常数。反射 \(2J-I\) 是等距映射，固定步长全图 RL \(\gamma=1\) 的锐常数为 1；任意 \(0<\gamma<1\) 的无界全图 RL 无有限常数。
- **Definitions / Dependencies / Evidence**：完整原图、同一步长及全对尺度；直接矩阵反演和正交范数计算，见[规范例卡 EX01](research/canonical/example_atlas.md#ex01)，历史别名 GX-004。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；只否定没有额外假设的 “完整 J 严格收缩 ⇒ F 强单调”。\(r_F(x)=\omega\|x\|\) 的真 EB 与此失败并存；变步长或有界尺度必须另标范围。

## C25-v1 / EX02 · 正紧对角的任意趋零 gauge 障碍

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(H=\ell^2\)，\((Fx)_n=x_n/n\) 满域，\(S=\{0\}\)、\(r_F(x)=\|Fx\|\)。对**任意** \(\psi:[0,\varepsilon)\to[0,\infty)\) 满足 \(\psi(t)\to0\) 当 \(t\downarrow0\)，**不存在** \(C,\delta>0\) 使 \(\|x\|\le C\psi(r_F(x))\) 对所有 \(\|x\|<\delta\) 成立。与此同时 \(F\) 严格单调、1-cocoercive、极大单调；每个固定 \(\lambda>0\) 的完整 PPA 对每个初值强收敛到 0，但每个有限迭代的算子范数 \(\|J_{\lambda F}^k\|=1\)。
- **Dependencies / Evidence**：固定 \(0<t<\delta\) 用 \(x=te_n\) 让真残差 \(t/n\to0\)；逐坐标乘子 \(n/(n+\lambda)\) 及受控尾部证明逐点收敛。[规范例卡 EX02](research/canonical/example_atlas.md#ex02)，历史别名 GX-009。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；无限维尾方向是障碍，有限维截断不属于同一 Claim。没有统一 EB 不推出某条特定轨道不收敛；也不反驳加闭值域等前提后的命题。

## C26-v1 / EX03 · 三次映射的三种精确模

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：\(F:\mathbb R\to\mathbb R, F(x)=x^3\)，\(S=\{0\},r_F(x)=|x|^3\)。固定目标 \(q=1/3\) EB 对全部 \(x\) 恒等且最佳常数 1；两变量 \(|x-F^{-1}(y)|\le2^{2/3}|Fx-y|^{1/3}\) 对全部 \(x,y\) 成立，且最佳局部和全局常数均 \(2^{2/3}\)。对每个固定 \(\lambda>0\)，算法残差 \(G_\lambda=I-J_{\lambda F}\) 的固定目标 \(q=1/3\) **局部常数下确界**为 \(\lambda^{-1/3}\)，但该值在任何含非零邻点的固定邻域不取到。
- **Dependencies / Evidence**：\(4(a^2+ab+b^2)-(a-b)^2=3(a+b)^2\ge0\) 且 \(a=-b\) 取等；\(p=u+\lambda u^3\) 直接算 \(G_\lambda(p)=\lambda u^3\)。见[规范例卡 EX03](research/canonical/example_atlas.md#ex03)，历史别名 GX-021。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；\(F\)、\(G_\lambda\) 与 \(\eta F\) 是不同观察对象。固定目标与移动目标的常数不能互换；\(q<1\) 的逆 Hölder 不等于普通 Lipschitz 强正则。原卡其他属性尚未逐项重写。

## C27-v1 / PD-STEP · 固定同图换步的单射门

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 Hilbert 关系的指定图块 \(\Gamma\)，若在 \(\lambda>0\) 下全对 RL 使旧 Cayley \(C:D_\lambda(\Gamma)\to H\) 良定，对**任意指定**新步长 \(\eta>0\) 置 \(t=\eta/\lambda,\alpha=(1+t)/2,\beta=(1-t)/2\) 与 \(Q=\alpha I+\beta C\)。新 Minty 输入域恰为 \(Q(D_\lambda)\)；相同图块在新步长具有单值 Cayley **当且仅当** \(Q\) 单射，此时 \(C_\eta=(\beta I+\alpha C)\circ Q^{-1}\)。若旧 \(C\) 为 \(L\)-Lipschitz 且 \(m=\alpha-|\beta|L>0\)，新映射在新自然域的 Lipschitz 常数至多 \((|\beta|+\alpha L)/m\)。
- **Dependencies / Evidence**：同一图点的正反射二坐标线性变换，矩阵行列式 \(t>0\)；下界 \(\|\Delta Q\|\ge m\|\Delta x\|\)。[PD-STEP 证明及尖锐反例](research/canonical/parameter_dictionary.md#pd-step)；历史 GX-015 只作来源别名。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；\(C(s)=\operatorname{sgn}(s)|s|^\gamma\) 表明 \(\eta>\lambda\) 可折叠，\(\eta<\lambda\) 可变 Lipschitz 且失去所有全局次线性指数。即使单射，另须核新目标输入的 coverage；这不是对不同关系缩放或取逆的陈述。

## C28-v1 / PD-TIED · 线性 RL 与 tied 双参数的精确等价

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定同一图块、步长 \(\lambda>0\)、全部指定配对及其尺度，\(L\ge0\)，\(a=u-u',b=v-v'\)。对每一对，\(\|a-\lambda b\|\le L\|a+\lambda b\|\) 当且仅当 \(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\)，其中 \(\theta=(1-L^2)/(2(1+L^2)),\mu=\theta/\lambda,\rho=\lambda\theta\)。有限 \(L\ge0\) 的精确范围为 \(-1/2<\theta\le1/2\)，上端 \(L=0\) 被包含。
- **Dependencies / Evidence / Status**：平方展开、分母正性及反向同一步；[PD-TIED](research/canonical/parameter_dictionary.md#pd-tied) 直接证明，`derived-checked`。若 \(L>1\)，\(\mu,\rho<0\) 不可删负项；完整独立二参数类不等同这条 tied 曲线。命名和先行性另核。

## C29-v1 / PD-SCALE · 有界降指数与无界反向障碍

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定同一 Cayley 输入域 \(D\)、同一 \(C:D\to H\)。若 \(0<\Delta<\infty\)且\(\operatorname{diam}D\le\Delta\)，\(0<\gamma_1\le\gamma_2\le1\) 且 \(C\) 是 \((L_2,\gamma_2)\)-Hölder，则它在同一域是 \((L_2\Delta^{\gamma_2-\gamma_1},\gamma_1)\)-Hölder。无界 \(D\) 上没有这条一般包含：\(C(s)=s\) 的更小指数全局失败；\(C(s)=\operatorname{sgn}(s)|s|^\gamma\) 在零点对更大指数、无穷远对更小指数失败。
- **Dependencies / Evidence / Counterevidence / Status**：尺度幂代数及相反数给凹幂的全局锐常数 \(2^{1-\gamma}\)，见[PD-SCALE](research/canonical/parameter_dictionary.md#pd-scale)；`derived-checked`。单点域真空，局部下界配对只给远离对角线的估计，不冒充邻域 Lipschitz。

## C30-v1 / PD-RESIDUAL · 完整最小残差的推理方向

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：任意关系 \(F\) 的非空零集 \(S\)，\(r_F(u)=\inf_{v\in F(u)}\|v\|\)，固定合法步 \(x=u+\lambda v\)。总有 \(r_F(u)\le\|v\|\)。若有限 \(\psi:[0,\eta_\psi)\to[0,\infty)\) 非减、所选 \(\|v\|<\eta_\psi\)，**已有**对实际输出的 \(d(u,S)\le\psi(r_F(u))\) 才可推出 \(d(u,S)\le\psi(\|v\|)\)；反向不成立。若对该纤维**每个** \(v\) 有 \(d(u,S)\le\kappa\|v\|^q\)，\(q>0\)，取 inf 可得真残差幂 EB；一般非减 gauge 需额外右连续性或实际下确界可取。
- **Dependencies / Evidence / Counterevidence / Status**：infimum 定义及趋近序列；\(F(u)=\{u,u^2\}\) 选 \(v=u\) 时有选中值线性界，而在零附近 \(r_F(u)=u^2\) 不支持真线性 EB。[PD-RESIDUAL](research/canonical/parameter_dictionary.md#pd-residual)，`derived-checked`。零点、输出窗口与空纤维约定随新问题重新固定；不能从算法步长推回完整图条件。

## C31-v1 / PA-WHOLE · 合法块收缩与整条轨道

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：X=R^n，非空闭 S、开 V、块长 m、半径 r,η>0；对每个 V 中距离 S≤r 的块起点、每个合法前缀和每个允许转移，都有可延拓合法词及非减前缀距离界 D_{w,j}、步位移界 G_{w,j}。所有 w,j<m,t∈[0,r] 有 D_{w,j}(t)<η；统一终点包络 Θ(t)=sup_w D_{w,m}(t)≤κt，0≤κ<1；统一块位移 G(t)=sup_w Σ_j G_{w,j}(t) 满足 H(t)=Σ_{q≥0} G(κ^q t)<∞。
- **Conclusion / Scope**：若 x₀∈V、d₀≤r 且 H(d₀)<dist(x₀,X\V)，每条合法轨道都可无限延拓并留在 V，块端点 d(x_{qm},S)≤κ^q d₀，整轨道总长≤H(d₀)，收敛到 S 中一点。量词为每条实际选择，不是存在一条。
- **Definitions / Dependencies / Evidence**：[PA-DEF、PA-WHOLE 完整证明](research/canonical/path_atlas.md#pa-whole)；闭 S、指定度量完备、实际前缀 coverage、统一可求和预算。状态 derived-checked；由 9/09 札记重新推导，外部先行性未核。
- **Counterevidence / Objections / Related Files**：终点收缩不管中间留域；非平凡周期不满足可求和步长。原札记周期推论不能作为本 Claim 的推论。[F12](FAILED_ROUTES.md#f12)。显式 M1 映射的捕获半径已在 [C38](research/topics/path_dynamics/m1_capture.md#m1-capture) 独立重算；历史原生多值循环方程与该映射的身份桥仍未证明。[F23](FAILED_ROUTES.md#f23)。

## C32-v1 / PA-POWER · 无限合法词的统一性门

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 m，对每个合法词 w=(σ₀,…,σ_{m−1}) 逐边有 d_{j+1}≤c_{σ_j}d_j^{α_{σ_j}}，正系数与正指数。则 d_m≤C_w d₀^{A_w}，其中 A_w=Π_j α_{σ_j}，C_w=Π_j c_{σ_j}^{Π_{ℓ>j}α_{σ_ℓ}}。有限词集的全体 A_w>1 给共同小半径；无限词集的一组充分条件是 inf_w A_w>1 与 sup_w C_w<∞，由这组条件可对预设 0<κ<1 给统一小半径收缩。
- **Dependencies / Evidence / Status**：逐次代入及 m=1、A_j=1+1/j、C_j=1 的反例见 [PA-POWER](research/canonical/path_atlas.md#pa-power)；状态 derived-checked。
- **Counterevidence / Scope**：A_w<1 只说明分离上界不能证收缩；联合路径仍可能有限捕获。A_w=1 还要统一控制 C_w。[F12](FAILED_ROUTES.md#f12)。

## C33-v1 / PA-CYCLES · 相位极限独立陈述

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：确定性周期映射 T₀,…,T_{m−1}；C=T_{m−1}∘⋯∘T₀，P_j=T_{j−1}∘⋯∘T₀。若某初值另已证 C^q x₀→x̄₀∈Fix C，且每个 P_j 在 x̄₀ 连续，则 x_{qm+j}→P_j x̄₀；整轨道收敛当且仅当这些相位极限相等。
- **Dependencies / Evidence / Status / Related Files**：[PA-CYCLES](research/canonical/path_atlas.md#pa-cycles) 直接使用连续性；状态 derived-checked。T(x)=1−x 有 Fix T²≠Fix T，表明块固定点不是原算法固定点。该命题不由 C31 的有限总长定理推出。[F12](FAILED_ROUTES.md#f12)。

## C34-v1 / CS-TRANSFER · 局部目标集合一致性

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：有限连续 f:ℝⁿ→ℝ；在 B_α(x̄) 有 f≥f(x̄)，且每个 Γ=zer ∂f 中 B_ς(x̄) 的点满足 f(y)≤f(x̄)。指定 S⊆Γ 且包含全部局部极小点。对每个 0<R<min(α,ς) 及每个 x∈B_{R/4}(x̄)，d(x,S)=d(x,Γ)=d(x,{f≤f(x̄)})。
- **Dependencies / Evidence / Status**：局部三集合一致、球外距离隔离、Fermat 及局部极小的二阶必要条件；[CS-TRANSFER](research/canonical/composite_subregularity.md#cs-transfer) 完整证明。状态 derived-checked；历史复合 C11 是来源别名，与现 C11 不同。
- **Counterevidence / Scope**：S 若随意缩小到一个零点，f(x,y)=x² 即失败；仅 x̄∈Θ₂ 不替代局部最小，f=−x⁴ 为反例。目标集合的身份先于残差界。

## C35-v1 / CS-EB · 满行秩复合真实残差界

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：c:ℝⁿ→ℝᵐ 在全域连续，且在闭球 B̄_R(x̄) 的开邻域 C^{1,1}，Dc 的 β-Lipschitz 预算；A=Dc(x̄) 满行秩，σ₀=σ_min(A)>βR，σ=σ₀−βR>0，J=||A||+βR，r=R/[2(1+J/σ)]。φ:ℝᵐ→ℝ 有限凸，C=argmin φ 非空、c(x̄)∈C；f=φ∘c，S=c^{-1}(C)，F=∂f。对每个 z∈c(B_R) 外层有 d(z,C)≤Ψφ(d(0,∂φ(z)))，Ψφ 非减并趋零。则对每个 x∈B_r(x̄)，d(x,S)≤σ^{-1}Ψφ(r_F(x)/σ)，且局部 Γ=Θ₂=S。全域连续性保证 S 闭，与 C36 最近零点步骤使用的同一前提一致。
- **Dependencies / Evidence / Status**：[CS-EB](research/canonical/composite_subregularity.md#cs-eb) 分开证明满秩切片修复的闭球自映射、凸链式规则、最小奇异值对全部次梯度的下界。状态 derived-checked；外部先行性未审。
- **Counterevidence / Scope**：c(x)=x²,φ(z)=z²/2 使原生线性 EB 不传递为复合线性 EB；秩亏版本是独立开放问题。若外层幂增长 r_{∂φ}(z)≥m₀d(z,C)^a，才取得 q=1/a 与 K=σ^{-1-1/a}m₀^{-1/a}。历史验证脚本不是证明。

## C36-v1 / CS-PROX · 复合的局部 RL 与近端轨道

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：保留 C35 全部前提，再对每个 z∈c(B̄_R)、每个 w∈∂φ(z) 设 ||w||≤M。令 h=βM、λ>0、λh<1。对每对 u,u'∈B_R 和每个 v∈F(u),v'∈F(u')，有〈u−u',v−v'〉≥−h||u−u'||²，故同图块、同 λ 的全对 RL 指数 1、常数 (1+λh)/(1−λh)。每个 x∈B_{R/2} 有唯一 B_R 内局部近端输出，x∈B_{r/2} 则输出在 B_r；不声称完整 J_F 无其他球外纤维。
- **Conditional convergence / Evidence**：再加 Ψ_F(bd)≤κd 对 0≤d≤δ，b=1/[λ(1−λh)]、0<κ<1，以及 d₀≤δ、||x⁰−x̄||+d₀/[(1−λh)(1−κ)]<r/2，才有每条该局部轨道 d_k≤κ^kd₀、有限总长、极限在 S。[CS-PROX](research/canonical/composite_subregularity.md#cs-prox) 的弱凸、最近零点、覆盖和位置预算证明；状态 derived-checked。
- **Objections / Scope**：满秩 EB 单独不提供轨道结论；删除乘子上界或留域、把局部输出升级完整 resolvent 均是新 Claim。

## C37-v1 / CS-MODEL · 曲面上幂与非幂的不同速率

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：c(s,t)=t−(s_+)²，S={(s,(s_+)²):s∈ℝ}；对连续严格增无界 η、η(0)=0 取 φ(z)=∫₀^{|z|}η(u)du，F=∂(φ∘c)。每点 r_F=η(|c|)√(1+4s_+²)，d((s,t),S)≤η^{-1}(r_F)。η(u)=u^a、0<a<1 时，幂 q=1/a 的最佳常数 1；η(u)=u log(e/u) 于 0≤u≤1、随后 η(u)=u 时有趋零 gauge η^{-1}(r)∼r/log(1/r)，但任何 q>1 的幂 EB 失败。
- **Dependencies / Evidence / Status**：[CS-MODEL](research/canonical/composite_subregularity.md#cs-model) 逐点公式、竖线锐性和标量近端方程；状态 derived-checked。对后一模型保持 C36 的全部 λh<1、gauge 兼容和严格留域预算；每条非驻定局部轨道的集合距离和实际点误差均超线性，且每个固定 p>1 的下一步误差/当前误差^p 比值趋∞。[CS-Q1–4](research/canonical/composite_subregularity.md#cs-model-q)用完整近端坐标、真实距离线性化和同轨道长度尾补足一般轨道证明；不是仅由竖线例外推。
- **Objections / Scope**：这里 c 为 C^{1,1} 而非 C²；源文的其他真多值变体未纳入本命题，外部新颖性未审。

## C38-v1 / M1-CAPTURE · 显式外层映射的两步捕获

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在 Euclidean \(\mathbb R^2\)，令 \(c=2/3\)、\(f(r)=\operatorname{sign}(r)[3(|r|-c)_+/2]^{1/3}\)、\(T(z_1,z_2)=(z_1-f(z_1-3z_2),0)\)、\(Z=[-c,c]\times\{0\}\)、\(z_*=(c,0)\)、\(R=1/(96\sqrt {10})\)。对**每个** \(z\in B_R(z_*)\)，\(T^2z\in Z=\operatorname{Fix}T\)，以后轨道固定。不存在分支选择量词；这是明确给出的单值 \(T\) 的命题。
- **Definitions / Dependencies / Evidence**：同一状态的 \(s=a-3b\) 与 \(h=(3s_+/2)^{1/3}\)，先证明第一步在 \((-c,c+R)\times\{0\}\)，再对第一步超出 \(c\) 的量 \(0<\delta<R\) 直接计算第二步。[对象和完整证明](research/topics/path_dynamics/m1_capture.md#m1-capture)；历史 9/09 多步札记 §5 只作来源线索。
- **Counterevidence / Objections / Status / Scope / Related Files**：`derived-checked`，仅此映射与球；原生多值 `Sign` 广义方程、它的全部允许选择、完整 resolvent 和真正残差尚未恢复，不能用此条给它们认证。[未闭桥](research/topics/path_dynamics/m1_capture.md#m1-obligation)。外部新颖性未审。

## C39-v1 / M1-SHARP · 同一映射的锐一步距离收缩

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：保留 C38 的**同一** \(T,Z,z_*,R\)。对每个 \(z\in B_R(z_*)\)，\(d(Tz,Z)\le(3/\sqrt {10})d(z,Z)\)。常数 \(3/\sqrt {10}<1\) 为这个球上统一距离因子的最小值：\(z_t=(c+3t,t)\)、\(t\downarrow0\) 实现该距离比。
- **Definitions / Dependencies / Evidence**：用完整活动关系 \(s=a-3b\) 而不是分别放大两个标量模；分 \(s\le0\) 和 \(s>0\) 的代数证明在 [M1-SHARP](research/topics/path_dynamics/m1_capture.md#m1-sharp)。`derived-checked`；历史较晚的旗舰架构札记 §2 指出这项修正，本轮重新核算。
- **Counterevidence / Objections / Scope / Related Files**：这**不**直接给出全对 RL、真残差 EB 或局部无限轨道留域；C38 独立地给有限捕获。旧例仍可说明独立最坏标量组合失真，却不能作为“一步距离收缩不存在”的反例。[F14](FAILED_ROUTES.md#f14)。

## C40-v1 / CI-IDENTIFY · 真多值次梯度的局部一步识别

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R^2\) 固定 \(c(s,t)=t-(s_+)^2\)、\(\nu>0\)、连续严格增无界 \(\eta:[0,\infty)\to[0,\infty)\) 且 \(\eta(0)=0\)，令 \(\phi_\nu(z)=\nu|z|+\int_0^{|z|}\eta(u)du\)、\(F_\nu=\partial(\phi_\nu\circ c)\)、\(S=c^{-1}(0)\)。在 S 上 F 的纤维为 \(Dc^T[-\nu,\nu]\) 而且真多值，在 S 外 \(r_{F_\nu}\ge\nu\)。任取 \(0<R<1/2\)，令 \(M=\nu+\eta(R+R^2),h=2M,r=R(1-2R)/4\)，固定 \(\lambda>0\) 且 \(\lambda h<1\)。对**每个** \(x\in B_{r/2}(0)\) 满足 \(d(x,S)<\lambda\nu(1-\lambda h)\)，唯一基点在 \(B_R(0)\) 的局部近端输出 \(y\) 属于 S，随后相同局部规则固定于 y。
- **Definitions / Dependencies / Evidence**：[CI-OBJECT 和 CI-IDENTIFY 完整计算](research/topics/composite_regular/cusp_identification.md#ci-identify)；需要 [C36](research/canonical/composite_subregularity.md#cs-prox) 的**局部** coverage、满秩、全部乘子界和同图步长估计。其外层 gauge 可取 \(\eta^{-1}((q-\nu)_+)\)。状态 `derived-checked`，从历史复合稿 §5.3 的观察补上输入半径、步长和真实残差门。
- **Counterevidence / Objections / Scope / Related Files**：图多值不等于局部近端输出多值；没有核远端完整 resolvent，也不处理秩亏或所有初值。与一般 Hölder–RL 路线的优劣和外部新颖性未核。

## C41-v1 / OT-MAXIMA · 弱分离缺失时二阶目标 EB 的障碍

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 \(f(0)=0\)、\(f(x)=e^{-1/x^2}(2+\sin(1/x^4))\) \((x\ne0)\)，令 \(\Gamma=\{f'=0\}\)、\(\Theta_2=\{x\in\Gamma:d^2 f(x\mid0)(w)\ge0\ \forall w\}\)。存在 \(x_k\downarrow0\) 使 \(f'(x_k)=0,f''(x_k)<0\)，故 \(d(x_k,\Theta_2)>0\)。对**任意** \(\Psi\) 满足 \(\Psi(0)=0\)，不存在包含 0 的邻域使 \(d(x,\Theta_2)\le\Psi(|f'(x)|)\) 在整个邻域成立。
- **Definitions / Dependencies / Evidence**：[OT-MAXIMA](research/topics/composite_regular/oscillating_target.md#ot-maxima) 的 \(u=x^{-4}\) 区间变号及负二阶导证明；\(f\in C^\infty\)，0 是严格全局极小点但近邻驻点函数值为正。状态 `derived-checked`；历史复合稿 §6.2 是来源线索。
- **Counterevidence / Objections / Scope / Related Files**：只否定没有目标一致/弱分离前件时**到完整 \(\Theta_2\)** 的误差界；不否定到 \(\Gamma\) 的界或 [C34](research/canonical/composite_subregularity.md#cs-transfer) 在完整前提下的正向结论。[F15](FAILED_ROUTES.md#f15)。

## C42-v1 / PS-RATE · 幂次剪切的可达速率校准

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：\(0<\gamma<1\)、\(q>1/\gamma\)、\(\alpha=\gamma q>1\)，在 \(\mathbb R^2\) 固定 \(\lambda=1\) 与 \(J(t,z)=(t+|z|^\gamma,P_\alpha z)\)，\(F=J^{-1}-I\)、\(S=\mathbb R\times\{0\}\)。对全部 \((s,u)\)，\(d((s,u),S)\le r_F(s,u)^q\)，而 \(q\) 在 \(u\to0\) 不可增大。对全部 \(0<|z|<1\) 的实际轨道一步，有 \(d(J(t,z),S)=d((t,z),S)^{\gamma q}\)，且 \(d(Jx,S)/\|x-Jx\|^q\to1\) 当 \(|z|\downarrow0\)。每个**有界**且含法向邻域的输入矩形上反射 \(2J-I\) 有全对 \(\gamma\)-Hölder 界，此指数不能增大。
- **Definitions / Dependencies / Evidence**：[PS-OBJECT、PS-RATE 与有界窗口证明](research/topics/path_dynamics/power_shear.md) 直接反演完整图、比较真残差、算沿法向比例和切向位移预算；状态 derived-checked，历史 GX-071 / 9/01 foundations §9.2 是来源别名。
- **Counterevidence / Objections / Scope / Related Files**：无界全图不继承次线性全对 RL；整个有界矩形不自动不变，单条轨道需正切向余量。只证明 \(\gamma q\) 在此反向校准族**可达到**，不是普适精确速率、必要条件或有界窗最优 RL 常数。[C43](research/topics/path_dynamics/oscillatory_shear.md) 是不同对象的保守指数对照。

## C43-v1 / OS-SCALING · 粗全对指数与双边实际阶分离

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R^2\) 固定 \(q>1,0<\gamma<1,\beta=q/\gamma-1\)，\(h(0)=0,h(x)=|x|^q\sin(|x|^{-\beta})\) 非零时，\(J(x,y)=(P_qx,P_qy+h(x))\)，\(F=J^{-1}-I,\lambda=1\)。对**全部** \(z\)，\(2^{-1-q/2}\|z\|^q\le\|Jz\|\le\sqrt5\|z\|^q\)。对足够小的球内全部非零轨道，局部零集为 \(\{0\}\)，距离有统一双边 \(q\)-阶；完整 \(F\) 的真实残差有局部 \(q\)-EB 而无任何更大幂指数。反射 \(2J-I\) 在每个有界输入窗为全对 \(\gamma\)-Hölder，在含零邻域无更高指数。
- **Definitions / Dependencies / Evidence**：[OS-OBJECT / SCALING / REFLECTION](research/topics/path_dynamics/oscillatory_shear.md) 的双边范数、局部固定点、两尺度 Hölder 与相位极值序列的直接证明；状态 derived-checked，来源别名 GX-072 / 9/01 foundations §9.3。
- **Counterevidence / Objections / Scope / Related Files**：实际阶 \(q>\gamma q\) 说明全对最坏指数可能保守，不反驳 C42 的可达构造；归一化 Q 因子未证明有极限。零集只在原点附近孤立，完整图在其他远端仍有零点；无界全图次线性 RL 不成立。外部先行性未核。

## C44-v1 / DE-ESCAPE · 自然 Minty 域上一步尺度不等于收敛阶

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：取 \(0<\alpha<1,\beta>0,0<\delta<1,\lambda=1,D=[-\delta,\delta]\)，\(C(0)=0,C(x)=P_\alpha(x)[2+\sin(|x|^{-\beta})]\) 非零时，\(J=(I+C)/2\) 仅在 D 定义，\(\operatorname{gph}F=\{(Jx,x-Jx):x\in D\}\)。\(S=\operatorname{zer}F=\{0\}\)。对**每个**非零初值 \(x_0\in D\)，迭代 \(x_{k+1}=Jx_k\) 有有限的首次 \(x_k\notin D\)；一步 \(r_+=\Theta(r^\alpha)>r\)。零点锚定反射最大指数为 \(\alpha\)、局部常数 3；全对反射最大指数为 \(\alpha/(\beta+1)\)。对所有充分小非零输出 u 的完整纤维，\(d(u,S)/r_F(u)\to1\)，线性 EB 常数的缩域下确界 1，任何 \(q>1\) 幂 EB 失败。
- **Definitions / Dependencies / Evidence**：[DE-OBJECT / EXPONENT / ESCAPE / RESIDUAL](research/topics/path_dynamics/domain_escape.md) 的两尺度证明、单调半径与多原像一致残差比；状态 derived-checked，历史 GX-073 / 9/01 foundations §9.4 是来源别名。
- **Counterevidence / Objections / Scope / Related Files**：只给原关系**自然域**内轨道的有限逃逸，不谈未定义延拓后的动力；不能由一步指数声称收敛。把选中残差比提升到真实 infimum 依赖所有原像一致趋零及非空紧纤维；改变 D 须另立版本。外部先行性未核。

## C45-v1 / IZ-PPA · 孤立零点上指定分支的上阶

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间 \(H\)、\(\lambda>0,q>1,\rho>0\)，\(p\in S=F^{-1}(0)\) 局部孤立。指定单值 \(T:V\to H\)，每个 \(x\in V\) 都有 \(Tx\in J_{\lambda F}(x)\)，\(T(p)=p\)。存在 \(V_0\subset V\)、输出球 U 和 \(\eta>0\)，使每个 \(x\in V_0\) 的 \(Tx\in U,\|(x-Tx)/\lambda\|<\eta\)，且这些输出满足真实 EB \(\|Tx-p\|\le\rho r_F(Tx)^q\)、\(\rho\eta^{q-1}\le\lambda/2\)。则 \(\|Tx-p\|\le\rho(2/\lambda)^q\|x-p\|^q\)。若闭输入球 \(\overline B(p,\delta)\subset V_0\) 且 \(C_q\delta^{q-1}<1\)，其中 \(C_q=\rho(2/\lambda)^q\)，该球内每条由 T 生成的轨道留域、趋 p，满足 \(r_{k+1}\le C_qr_k^q\)。
- **Definitions / Dependencies / Evidence**：[IZ-GERM/FIBERS/PPA](research/canonical/isolated_zero_flatness.md#iz-ppa) 给逐图点剪切、真实残差方向、小步门、球不变与完整归纳。状态 derived-checked；旧 RL_foundations §7.1–7.5 是来源，现版本明确输出 EB 的残差窗口和所有输入的分支门。
- **Counterevidence / Objections / Scope / Related Files**：这是 upper \(q\)-order，不含正 Q 因子；只对指定 T，不升级为完整多值 resolvent 的全部选择。选中图值的幂界不能无条件倒推真实 EB，见 [IZ-FIBERS 双值反例](research/canonical/isolated_zero_flatness.md#iz-fibers)。外部优先性未核。

## C46-v1 / IZ-FACTOR · 精确因子的额外归一化门

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C45 的不终止轨道上令 \(w_k=(x^k-x^{k+1})/\lambda\)。如果另有 \(\|x^{k+1}-p\|/\|w_k\|^q\to\mu\in(0,\infty)\)，则 \(\|x^{k+1}-p\|/\|x^k-p\|^q\to\mu/\lambda^q\)。
- **Definitions / Dependencies / Evidence**：[IZ-FACTOR](research/canonical/isolated_zero_flatness.md#iz-factor) 的三角双边界与 \(q>1\)；derived-checked，从旧 §7.6 重新核算。
- **Counterevidence / Objections / Scope / Related Files**：归一化极限是额外假设，C45 的上界自身不产生它；不对有限终止或完整 resolvent 的其他分支声称正因子。

## C47-v1 / DC-GAP · GX-074 的独立 coverage 障碍

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R\) 令 \(K=\{0\}\cup\{1/n:n\ge1\}\)、\(\lambda>0\)、\(F(u)=\{0\}\) 对 \(u\in K\)，域外空值；\(S=K\)。完整紧图在全部图点对上对**每个** \(0<\gamma\le1\) 满足 \(\mathrm{RL}(\lambda,\gamma,1)\)，常数 1 在整个 K 上锐；全部有限残差输出有 \(d(u,S)=r_F(u)=0\)。但是自然输入域恰为 K，任何以 0 为心的开球均不被覆盖。
- **Definitions / Dependencies / Evidence**：[DC-OBJECT/GAP](research/topics/path_dynamics/discrete_coverage.md#dc-gap) 逐对计算 Cayley、完整纤维、EB 的作用域与域外无步；derived-checked，旧 GX-074 / foundations 注 1.5 是来源。
- **Counterevidence / Objections / Scope / Related Files**：若把目标换成 \(\{0\}\)，在 \(1/n\) 上真 EB 就失败；不能偷换目标以声称更强结论。反例只否定从 RL 和有限残差 EB 推出输入 coverage，不否定额外假设 coverage 的 PPA 定理。[F16](FAILED_ROUTES.md#f16)。

## C48-v1 / NA-DRIFT · 输出锚距离与最近点漂移的包络

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间，非空 \(S\subset F^{-1}(0)\)、固定 \(\lambda>0\) 与指定 \(J:D\to H\) 的每个 \(x\in U\subset D\)，取 \(y=Jx\)、\(w=(x-y)/\lambda\in F(y)\)。对整个 \(0<d(x,S)\le r_0\) 家族，假设 \(P_S(x),P_S(y)\ne\varnothing\)。置 \(r_x=d(x,S),a(x)=d(x,P_S(y)),\delta(x)=d(P_S(x),P_S(y))\)。对每个 x，\(r_x\le a(x)\le r_x+\delta(x)\le3a(x)\)，相应非负上包络满足 \(\mathcal A(r)\le\chi(r)\le3\mathcal A(r)\)。
- **Definitions / Dependencies / Evidence**：[NA-OBJECT/DRIFT](research/canonical/nonisolated_alignment.md#na-drift) 用任意近似实现两集合间 infimum 的点对证明；derived-checked，从旧 foundations §8.1 重写。非空实际距离趋零时 \(\mathcal A(r)\le Kr^\theta\) 必有 \(\theta\le1\)。
- **Counterevidence / Objections / Scope / Related Files**：未声称投影集合间最近点对取到；定义本身不保证锚包络有幂界。若投影集合不保证非空，用 NA-APPROX 的另一陈述，不把两种前提混写。

<a id="c49-v1"></a>
## C49-v1 / NA-COMPOSE · 旧幂包络的未限制指数版本

- **Status**：`refuted`，只针对旧幂包络推论的 gauge 定义域；逐点 NA-3 的真 EB 合成未被否定。
- **Exact Statement / Objects / Domain / Quantifiers**：在 C48 的实 Hilbert 指定分支、完整真残差与有限非减 \(\psi:[0,\eta_\psi)\to[0,\infty)\) 等 C49-v2 基本前提下，允许任意实 \(\theta\) 且 \(\mathcal A(r)\le Kr^\theta\)，仅检查端点 \((2K/\lambda)r_0^\theta<\eta_\psi\)，便对**每个** \(0<r\le r_0\) 写 \(\psi((2K/\lambda)r^\theta)\) 为输出上界。
- **Counterevidence / Related Files**：[F38](FAILED_ROUTES.md#f38) 的 \(\theta=-1\) 例满足端点门而右端在更小 r 超出 gauge 定义域。正指数必须是额外假设，见 C49-v2；这不是一般 NA-3 的反例。

<a id="c49-v2"></a>
## C49-v2 / NA-COMPOSE · 非孤立零集的条件 gauge 合成

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C48 同一全体输入家族上，要求每个实际步 \(t=\|w(x)\|<\eta_\psi\)，输出的真实 EB \(d(Jx,S)\le\psi(r_F(Jx))\)，\(\psi\) 有限非减且 \(\psi(t)=o(t)\)，全部达到的 t 有 \(\psi(t)\le\lambda t/2\)。若 \((2/\lambda)[r_x+\delta(x)]<\eta_\psi\)，则 \(d(Jx,S)\le\psi((2/\lambda)a(x))\le\psi((2/\lambda)[r_x+\delta(x)])\)。若另取 **\(K>0,\theta>0\)**，对全部 \(0<r\le r_0\) 有 \(\mathcal A(r)\le Kr^\theta\) 且缩域使 \((2K/\lambda)r_0^\theta<\eta_\psi\)，则输出距离包络至多 \(\psi((2K/\lambda)r^\theta)\)；\(\psi(t)=\rho t^q\) 时为上指数 \(\theta q\)。
- **Definitions / Dependencies / Evidence**：[NA-COMPOSE](research/canonical/nonisolated_alignment.md#na-compose) 的 \(|a(x)-\lambda t|\le d(Jx,S)\) 是承重引理；同一实际输出的真 infimum 与 gauge 单调性给结论。状态 derived-checked，旧 §8.2 的近锚界重算。
- **Counterevidence / Objections / Scope / Related Files**：这是指定 J 的逐点/包络上界，未给全轨道留域、完整 resolvent 任意选择或指数最优。旧 C49-v1 在 \(\theta<0\) 时右端越过 gauge 域，见 [F38](FAILED_ROUTES.md#f38)。无 proximinality 用 [NA-APPROX](research/canonical/nonisolated_alignment.md#na-approx) 的正容差和额外预算；不得省略。外部先行性未核。

<a id="c50-v1"></a>
## C50-v1 / NA-SHARP · 旧固定小步推出 \(B=1/\lambda\) 的版本

- **Status**：`refuted`，只针对从固定小步窗口推出归一化常数；同序列三个正比值的乘积恒等式保留。
- **Exact Statement / Objects / Domain / Quantifiers**：在 C48/C49 的指定分支和 \(\psi=o(t)\)、\(\psi(t)\le\lambda t/2\) 的实际步窗下，取 \(r_n\downarrow0\) 且 \(a_n/r_n^\theta\to A>0,t_n/a_n\to B>0,s_n/t_n^q\to C>0\)；不要求 \(t_n\to0\)，仍断言 \(B=1/\lambda\)。
- **Counterevidence / Related Files**：[F38](FAILED_ROUTES.md#f38) 的 \(\theta=0,t_n\to5/4\) 例给 \(B=5/4\ne1\)（\(\lambda=1\)）。修补版 C50-v2 显式要求步长趋零；乘积极限在旧版中也成立。

<a id="c50-v2"></a>
## C50-v2 / NA-SHARP · 同序列饱和才能得到 \(\theta q\) 见证

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C48 的同一序列 \(x_n\) 上，令 \(r_n=d(x_n,S)\downarrow0,a_n=a(x_n),t_n=\|w(x_n)\|,s_n=d(Jx_n,S)\)。若 \(a_n/r_n^\theta\to A>0,t_n/a_n\to B>0,s_n/t_n^q\to C>0\)，则 \(s_n/r_n^{\theta q}\to CB^qA^q\)；同序列双边 \(\asymp\) 前提给双边阶。在 C49-v2 的小步超线性 EB **且 \(t_n\to0\)** 下，必有 \(B=1/\lambda\)；若 \(\theta>0\) 且上述正比值极限成立，步长趋零自动成立。
- **Definitions / Dependencies / Evidence**：[NA-SHARP](research/canonical/nonisolated_alignment.md#na-sharp) 的比值乘积及 C49-v2/NA-COMPOSE 在 \(t_n\to0\) 下的步长误差 \(o(t_n)\)；derived-checked，从旧 §9.1 重算。
- **Counterevidence / Objections / Scope / Related Files**：分别在不同序列取得两个最坏指数不足以给 \(\theta q\) 的锐性；C49 的上界不自动提供此序列或正 Q 因子。GX-071 只是一个具体可达构造，不代表普适必要性。

## C51-v1 / MA-REFLECT · 输出近锚的渐近反射

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间、\(\lambda>0,S\subset F^{-1}(0)\) 非空，任意实际图点 \((y,w)\)、\(0<t=\|w\|<\eta\)，真残差输出 EB \(d(y,S)\le\psi(r_F(y))\)，\(\psi\) 有限非减且 \(o(t)\)。逐点选 \(p\in S\) 满足 \(\|y-p\|\le d(y,S)+e(t)\)，\(e(t)\ge0,e(t)=o(t)\)，\(e(t)>0\) 时不需投影取到，\(e(t)=0\) 时需取到。置 \(x=y+\lambda w,\widehat x=y-\lambda w,\delta_t=(\psi(t)+e(t))/(\lambda t)\)。当 \(\delta_t<1\) 有 MA-1 的双边反射比及相对缺陷界；沿任何 \(t_n\to0\) 的合法序列，比值趋 1。
- **Definitions / Dependencies / Evidence**：[MA-OBJECT/REFLECT](research/canonical/moving_anchor_reflection.md#ma-reflect) 以同一图点和 p 的三角双边界直接证明；derived-checked，从旧 foundations §6.1 重算。
- **Counterevidence / Objections / Scope / Related Files**：p 可随图点移动；不能改成固定零点、所有图点对的 reflector 模，或集合距离收缩。[MA-LIMIT](research/canonical/moving_anchor_reflection.md#ma-limit) 给完整具体反例；外部先行性未核。

## C52-v1 / MA-POWER · 移动锚幂型缺陷

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C51 的同一图点和 p 上，若 \(q>1,\rho,c\ge0\)、真 EB \(d(y,S)\le\rho r_F(y)^q\)、\(\|y-p\|\le d(y,S)+c\|w\|^q\)，令 \(A=\rho+c\)。当 \((A/\lambda)\|w\|^{q-1}\le1/2\)，有 \(\|\widehat x-(2p-x)\|\le2^{q+1}A\lambda^{-q}\|x-p\|^q\)。
- **Definitions / Dependencies / Evidence**：[MA-POWER](research/canonical/moving_anchor_reflection.md#ma-power) 的 \(\|x-p\|\ge\lambda\|w\|/2\) 和缺陷恒等式；derived-checked，从旧 §6.2 重算。
- **Counterevidence / Objections / Scope / Related Files**：常数为充分界，未证最优；\(A=0\) 的零缺陷单独由恒等式得出。结论只相对逐点 output-near p，不提供 branch existence、全对 RL 或 PPA 留域。

## C53-v1 / NB-LOCAL · 近似零点锚下指定分支的有限长度

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert \(H\)、完整 \(F\)、\(S=F^{-1}(0)\ne\varnothing\)、\(\bar x\in S\)、\(U=B(\bar x,R)\)、\(\lambda>0,L\ge0,0<\gamma\le1,\delta>0\)。指定 **同一个** \(T:U\to H\) 对每个 \(x\in U\) 都有真实近端图值 \((Tx,(x-Tx)/\lambda)\)（NB-B）；对每个 \(x\in A_\delta=\{x\in U:d(x,S)\le\delta\}\)，**包括零距离输入**，有一列 \(p_n\in S\) 满足 \(\|x-p_n\|\to d(x,S)\) 且逐项满足 \(\|2Tx-x-p_n\|\le L\|x-p_n\|^\gamma\)（NB-A），且每个实际输出满足真全纤维残差窗口 \(r_F(Tx)<\eta\)、\(d(Tx,S)\le\psi(r_F(Tx))\)（NB-E）。其中 \(\psi:[0,\eta)\to[0,\infty)\) 有限非减、零点连续、\(\psi(0)=0\)；\((\delta+L\delta^\gamma)/(2\lambda)<\eta\)，\(c=\limsup_{t\downarrow0}\psi((t+Lt^\gamma)/(2\lambda))/t<1\)。记 \(\Phi(t)=\psi((t+Lt^\gamma)/(2\lambda))\)，选 \(c<\theta<1\) 和使 \(\Phi(t)\le\theta t\) 的 \(0<\delta_\theta\le\delta\)。对每个 \(x^0\in U\)、\(r_0=d(x^0,S)\le\delta_\theta\)，**再要求** \(\|x^0-\bar x\|+\frac12[r_0/(1-\theta)+Lr_0^\gamma/(1-\theta^\gamma)]<R\)（NB-2）。则指定轨道全程合法、\(r_k\le\theta^kr_0\)、总长度至多 NB-2 中的方括号半值、趋于 \(S\) 且有该预算的尾界；并有 \(U\cap\overline S=U\cap S\).
- **Definitions / Dependencies / Evidence**：[NB-OBJECT/NB-LOCAL](research/canonical/named_branch_local.md#nb-local) 从逐图点恒等式、真残差方向、全家族量词和 Hilbert 完备性独立证明；旧 foundations §4 是来源。状态 derived-checked，文献先行性未核。
- **Counterevidence / Objections / Scope / Related Files**：A 只是 anchored，不是全对 RL；没有最近点、全局闭 \(S\) 的要求。不能将指定 \(T\) 的结论升级为完整 \(J_{\lambda F}\) 的任意选择；若 A 排除零距离输入，局部闭性及极限归属的论证失效。需对完整纤维另证统一条件。

## C54-v1 / NB-POWER · 幂次上界与退化端点

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C53 同一 \(F,T,U,S\) 和所有输出窗口假设下令 \(\psi(t)=\rho t^q\)，\(\rho,q>0\)。当 \(0<\gamma<1,L>0\)，充分门是 \(\gamma q>1\)，或 \(\gamma q=1\) 且 \(\rho(L/(2\lambda))^q<1\)；当 \(\gamma=1\)，充分门是 \(q>1\)，或 \(q=1\) 且 \(\rho(1+L)/(2\lambda)<1\)；当 \(L=0\)，不论打印的 \(\gamma\)，充分门是 \(q>1\)，或 \(q=1\) 且 \(\rho/(2\lambda)<1\)。每种情况还需缩半径及 C53 的实际初值留域预算；结论是相应一步 upper order、C53 有限长度，以及临界系数的 ratio limsup 上界。
- **Definitions / Dependencies / Evidence**：[NB-POWER](research/canonical/named_branch_local.md#nb-power) 对 C53 的 \(\Phi(r)\) 分别展开并核退化参数；derived-checked，与 R03 的非退化门槛相容，但 C53 的对象与量词不同。
- **Counterevidence / Objections / Scope / Related Files**：指数低于 1 时此上界不判定收敛或发散；系数只为该证明证书的充分量，不是一般必要界。Upper order 不给双边精确阶或正 Q 因子；\(L=0\) 时不能沿用 \(\gamma q\) 标签。

## C55-v1 / NB-OSCILLATION · 锚定线性 RL 不推出全对线性 RL

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R,\lambda=1\) 取 \(T(0)=0,T(x)=x[3/10+(1/10)\sin(x^{-2})]\)（\(x\ne0\)），完整定义 \(F(y)=\{x-y:T(x)=y\}\)。对唯一 \(S=\{0\}\) 及每个输入，A 以 \(\gamma=1,L=3/5\) 成立，且真 EB 为 \(|y|\le(2/3)r_F(y)\)，故 C53 的 \(\Phi(r)=(8/15)r\)；但任何零邻域上此完整图的全对 \(\gamma=1\) RL 均失败。
- **Definitions / Dependencies / Evidence**：[NB-OSCILLATION](research/canonical/named_branch_local.md#nb-oscillation) 以 \(1/5\le a(x)\le2/5\) 控制所有原像的真残差，并以 Cayley 导数沿明确序列无界证明不蕴含；新构造，derived-checked。
- **Counterevidence / Objections / Scope / Related Files**：只排除全对线性指数，不排除其他较弱 Hölder 指数。不能以这个例子的完整 \(J_F=T\) 反推任意原关系的完整 resolvent 同一性；外部优先性未核。

## C56-v1 / AV-BRIDGE · 全对图块到指定锚接口

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert \(H\)、完整 \(F\)、\(S=F^{-1}(0)\ne\varnothing\)、\(G\subset\operatorname{gph}F\)、\(\lambda>0\)。若 \(G\) 对任意两图点满足同一 \(L\ge0,0<\gamma\le1\) 的全对 RL，\(U\subset M_+(G)\)，且对 active set \(A\subset U\) 的每个输入 \(d(x,S_G)=d(x,S)<\infty\)，其中 \(S_G=\{p\in S:(p,0)\in G\}\)，则图块唯一指定分支在 \(U\) 上存在；对所有 \(x\in A\) 可取近似最近 \(p_n\in S_G\) 满足 C53 的锚界，且反射在 \(U\) 的任意两输入间有全对 Hölder 模。
- **Definitions / Dependencies / Evidence**：[AV-OBJECT/BRIDGE](research/canonical/all_pairs_verifier.md#av-bridge) 使用剪切单射、覆盖、同图块零锚及距离 infimum 重算旧 foundations §3.1；derived-checked。若要调用 C53，另加对实际输出的真残差 E、兼容和初值留域预算。
- **Counterevidence / Objections / Scope / Related Files**：不要求 \(S_G=S\)，但保距离的 (AV-2) 不可凭 RL 与 coverage 删除，见 C57。完整 \(J_{\lambda F}\) 的任意输出还需对完整输入纤维排他；不提供全局 closedness 或算法不变性。

## C57-v1 / AV-GAP · 失去零锚保距离的完整关系反例

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：\(H=\mathbb R,\lambda=1,F(y)=\{0,y\}\)、\(G=\{(y,y):y\in\mathbb R\}\)。全图块任意两点以 \(L=0\) 满足每个 \(0<\gamma\le1\) 的 RL，且 \(M_+(G)=\mathbb R\)，但完整 \(S=\mathbb R\)、\(S_G=\{0\}\)，对每个 \(x\ne0\) 有 \(d(x,S_G)=|x|>0=d(x,S)\)。指定 \(T(x)=x/2\) 不固定这些零距离输入；完整 \(J_F(x)\) 还同时含 \(x\) 与 \(x/2\)。
- **Definitions / Dependencies / Evidence**：[AV-GAP](research/canonical/all_pairs_verifier.md#av-gap) 直接计算全部图值、自然域、反射与零集；新反例，derived-checked。
- **Counterevidence / Objections / Scope / Related Files**：否定“全对图块 RL + coverage 自动产生 C53 的 A”及“图块单值自动给完整排他”，不是对 C56 的反例；其 (AV-2) 不成立。即使真输出 EB 在本例成立，仍不能替代零锚保距离。

## C58-v1 / CG-CLOSURE · 闭图与自然 Minty 域的闭性

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间 \(H\)、\(\lambda>0\)、非空图块 \(G\subset H\times H\)；存在 \(R>0\) 及有限 \(\omega:[0,R)\to[0,\infty)\)，满足 \(\omega(0)=0\)、\(\lim_{t\downarrow0}\omega(t)=0\)，且对 **每一对** Minty 输入差小于 \(R\) 的图点有 \(\|\Delta M_-\|\le\omega(\|\Delta M_+\|)\)。则 \(D=M_+(G)\) 上 Cayley \(C\) 单值并唯一连续延拓至 \(\overline D\)；图的闭包是该延拓的 Cayley pullback。特别地，\(G\) 闭 iff \(D\) 闭；**若另有 \(G\) 闭且 \(D\) 在整个 \(H\) 稠密**，才有 \(D=H\)。
- **Definitions / Dependencies / Evidence**：[CG-OBJECT/CLOSURE](research/canonical/closed_graph_minty_domain.md#cg-closure) 从同一图块的剪切逆映射、近对角线模和 Hilbert 完备性独立证明，derived-checked。旧 foundations §1.1–§1.4 只是坐标与闭性例的来源；该闭域定理不是旧稿状态的升级。
- **Counterevidence / Objections / Scope / Related Files**：闭图单独不足以 coverage，\(G=[0,1]\times\{0\}\) 有完整反例；稠密但不闭也不足，\(G=\mathbb Q\times\{0\}\subset\mathbb R^2\) 的自然域是 \(\mathbb Q\ne\mathbb R\)，并满足模 \(\omega(t)=t\)。后一项由空白接收审查发现总账抄漏合取前提，规范证明与 E102 原已正确。没有零点消失模时闭域亦不保闭图。一般跳跃模只保证延拓/闭性，不声称闭包在跳跃尺度仍保同一模。图块结论不排除完整关系中图块外的纤维；文献先行性未核。[CG-BOUNDARY](research/canonical/closed_graph_minty_domain.md#cg-boundary)。

## C59-v1 / RW-POSITIVE · 一般 gauge 的窗口到邻域转换

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert \(H\)、完整 \(F:H\rightrightarrows H\)、\(S=F^{-1}(0)\ni\bar u\)、真残差 \(r_F=d(0,F(u))\)。有限非减 \(\psi:[0,\eta)\to[0,\infty)\)、\(\psi(0)=0\)、原点连续。若存在 \(U\ni\bar u\)、\(0<\delta<\eta\)，对 **每个** \(u\in U\) 且 \(r_F(u)<\delta\) 有 \(d(u,S)\le\psi(r_F(u))\)，并且 \(\psi(\delta)>0\)，则在 \(V=U\cap B(\bar u,\psi(\delta))\) 对 **每个** \(r_F(u)<\eta\) 的 \(u\) 成立同一界。若 gauge 另有全域非减延拓，可将无窗口量词扩大至全部可评价的有限残差（空纤维按 \(+\infty\) 约定）。
- **Definitions / Dependencies / Evidence**：[RW-OBJECT/POSITIVE](research/canonical/residual_window_bridge.md#rw-positive) 用 \(d(u,S)\le\|u-\bar u\|\) 与阈值以上的 gauge 单调性直接证明；derived-checked。旧 foundations 定义0.4 只给正幂特殊情形；本页一般充分门为独立推导。
- **Counterevidence / Objections / Scope / Related Files**：正阈值不是普遍必要条件；没有它时闭图完整关系也可窗口版真而邻域版假，见 [RW-FLAT](research/canonical/residual_window_bridge.md#rw-flat)。有限定义域外 \(\psi(r_F(u))\) 无定义，不能把受限可评价量词暗写成所有 \(u\)；文献先行性未核。

## C60-v1 / DR-TAN · 切触线与抛物线的算法残差

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：\(C=\mathbb R\times\{0\},D=\{(s,s^2):s\in\mathbb R\}\subset\mathbb R^2\)，\(U=\{(a,b):b>-1/2\}\)，\(T=I-P_C+P_DR_C\)、\(G=I-T\)。\(P_DR_C\) 在整个 \(U\) 单值，\(S=G^{-1}(0)=\{(0,b):b>-1/2\}\)。对原点附近 **所有** \(z=(a,b)\in U\)，若 \(a=s+2s(s^2+b)\)，则 \(d(z,S)=|a|\le(1+2|b|+2s^2)\|Gz\|^{1/2}\)；半阶局部最优模为 1，任何 \(q>1/2\) 的相同目标幂 EB 失败。不存在原点邻域上统一 \(\rho<1\) 的 \(d(Tz,S)\le\rho d(z,S)\)。
- **Definitions / Dependencies / Evidence**：[DR-TAN](research/topics/examples/dr_tangency_transversality.md#dr-tangent) 从全管唯一投影及 \(G=(2s(s^2+b),-s^2)\) 重算；\(z_s=(s,-s^2)\) 达成半阶模 1 和一步距离比 1。状态 `derived-checked`；来源为 9/01 ZIP `work/c_gx066_077.md` GX-069，详见正文哈希。
- **Counterevidence / Objections / Scope**：这是算法残差，不是 \(N_C+N_D\) 的 EB；\(D\) 非凸、投影唯一只在所列管上。管不变不保证每条轨道留在某个小邻域或有指定渐近率。文献优先性未核。

## C61-v1 / DR-TRANS · 横截线的精确线性模

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：\(C,D\subset\mathbb R^2\) 为过原点且夹角 \(0<\theta<\pi/2\) 的直线；全空间同一 \(T=I-P_C+P_DR_C\)、\(G=I-T\)。令 \(c=\cos\theta,s=\sin\theta\)，某旋向的 \(Q_\theta\) 使 \(T=cQ_\theta\)、\(G=I-cQ_\theta\)。对 **所有** \(z,z'\)，\(\|Gz-Gz'\|=s\|z-z'\|\)；\(G^{-1}\) 全局 Lipschitz、MR/MSR 精确模 \(1/s\)，\(\|T^kz\|=c^k\|z\|\) 对每个 \(k\ge0\)。
- **Definitions / Dependencies / Evidence**：[DR-TRANS](research/topics/examples/dr_tangency_transversality.md#dr-transverse) 的平面反射复合和奇异值恒等式；状态 `derived-checked`。来源为同一 9/01 ZIP GX-070，不将它和 C60 当作同一算子的改参。
- **Counterevidence / Objections / Scope**：法锥和 \(N_C+N_D\) 的定义域和残差不同；横截构造不能给任意两集合的普遍模。外部先行性未核。

<a id="c62-v1"></a>
## C62-v1 / PS-FIBER-IDENTITY · 只核有限纤维的旧推论

- **Status**：`refuted`；这是旧 C62 复合陈述中漏量词的纤维等式，不反驳平稳律吸收主定理。
- **Exact Statement / Objects / Domain / Quantifiers**：在下列 C62-v2 的同一有限维、固定 \(\lambda>0\)、proper Borel \(f\) 与支持完整全局近端纤维的 Borel 核条件下，仅要求“每个**有限多值** \(P_\lambda f(x)\) 的不同成员均获正选择概率”，便断言对**所有** \(x\in\operatorname{dom}f\)，\(A_K=\{x:P_\lambda f(x)=\{x\}\}\)。无穷纤维未受这一前提约束。
- **Counterevidence / Related Files**：[F37](FAILED_ROUTES.md#f37) 和 [PS-ABSORPTION](research/topics/random_markov/proximal_selection_seam.md#ps-absorption) 的 \(f(y)=-y^2/2\) 紧区间例在 \(x=0\) 有无穷纤维而 \(K(0)=\delta_0\)。主等价 \(\pi K=\pi\iff\pi(A_K)=1\) 未失败；修补版另立 C62-v2。

<a id="c62-v2"></a>
## C62-v2 / PS-ABSORPTION · 固定全局近端的平稳律吸收

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：有限维 \(\mathbb R^n\)、\(\lambda>0\)、同一个 proper Borel \(f:\mathbb R^n\to(-\infty,+\infty]\)。对每个 \(x\in\operatorname{dom}f\)，全局最小解集合 \(P_\lambda f(x)\ne\varnothing\)；Borel 核 \(K(x,P_\lambda f(x))=1\)。令 \(A_K=\{x\in\operatorname{dom}f:K(x,\{x\})=1\}\)。对 **每个** 支撑于 \(\operatorname{dom}f\) 的概率律 \(\pi\)，\(\pi K=\pi\) 当且仅当 \(\pi(A_K)=1\)，不要求 \(f\) 可积或二阶矩。附加**每个**完整纤维 \(P_\lambda f(x)\) 均有限且其每个成员获正选择概率，才有 \(A_K=\{x:P_\lambda f(x)=\{x\}\}\)。
- **Definitions / Dependencies / Evidence**：[PS-ABSORPTION](research/topics/random_markov/proximal_selection_seam.md#ps-absorption) 以同律下有界严格递增 \(\arctan f\) 避免 \(\int|f|\) 的隐藏门，再用平方罚项的严格下降。`derived-checked`；来源 9/14 非乘积近端稿 §3，已重构而非继承标题。
- **Counterevidence / Objections / Scope**：仅对同一个目标的**全局**近端最小解和域内平稳律；非凸 limiting-subdifferential 的完整 resolvent 可含非最小驻点，随机切换目标亦另需证明。旧 C62-v1 只核有限纤维即断言完整吸收点身份，已由 [F37](FAILED_ROUTES.md#f37) 反驳；主吸收等价保留。外部新颖性未核。

## C63-v1 / PS-SEAM · 闭近端图与非不变极限的 law-step 障碍

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：\(\lambda=1,H=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right),b=(3,3)\)，\(f(y)=\tfrac12y^THy-b^Ty+4\mathbf1_{y\ne0}\)，\(Q=H+I\)、\(t(x)=Q^{-1}(b+x)\)、\(g(x)=\tfrac12(b+x)^TQ^{-1}(b+x)\)。完整全局近端图按 \(g<4,=4,>4\) 分别为 \(\{0\},\{0,t(x)\},\{t(x)\}\)；在 tie 各支选概率 \(1/2\) 的核 \(K\) 有唯一平稳律 \(\delta_0\)。沿 \(v=(1,1),a_0>1\) 的真实轨道 \(a_k=1+(a_0-1)4^{-k}\) 有有限总长度却趋向非平稳 \(\delta_v\)。对 **每个** \(W_2\) 邻域 \(B_r(\delta_0)\)，存在固定 \(\epsilon>0\) 与 \(\mu_k=(1-\epsilon)\delta_0+\epsilon\delta_{a_kv}\) 全部在邻域，使 \(W_2(\mu_k,\mu_kK)\to0\) 而 \(W_2(\mu_k,\delta_0)\to\sqrt{2\epsilon}>0\)；故该完整邻域上不存在任何零点消失的 law-step gauge EB。
- **Definitions / Dependencies / Evidence**：[PS-SEAM/NO-EB](research/topics/random_markov/proximal_selection_seam.md#ps-example) 的全图比较、C62 吸收律和射线上显式最优运输；历史 V10 的有理有限恒等式本轮复跑只作观察。`derived-checked`；来源 9/14 非乘积近端稿 §5，外部优先性未核。
- **Counterevidence / Objections / Scope**：零残差仍恰为不变律；问题是**一致消失模**和核的接缝连续性。闭多值图不保证所选核 Feller；这不是 C22/C23 的不一致随机二次近端，亦不是同步 OT \(\Psi\)。

## C64-v1 / SL-LIFT · M1 显式映射的新完整 Sign 图实现

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：\(c=2/3\)、\(A(h)=c\operatorname{Sign}(h)+2h^3/3\)，\(\operatorname{Sign}(0)=[-1,1]\)。新关系 \(F_{\rm lift}(u,v)=\varnothing\) 当 \(v\ne0\)；当 \(v=0\)，其**全部**值是 \(\{(h,q):u+h-3q\in A(h)\}\)。对每个 \(z=(p,q)\in\mathbb R^2\)，完整单位步长 resolvent \(J_{F_{\rm lift}}(z)=\{(p-f(p-3q),0)\}=\{Tz\}\)，自然 Minty 域全为 \(\mathbb R^2\)，零集为 \([-c,c]\times\{0\}\)。对 \(0<\delta<1\)，\(r_{F_{\rm lift}}(c+\delta,0)=\delta/3\) 且到零集距离 \(\delta\)，端点线性 EB 常数 3 锐利；左端对称。
- **Definitions / Dependencies / Evidence**：[SL-INCLUSION/GRAPH/ZERO](research/topics/path_dynamics/m1_sign_lift.md#sl-inclusion) 从 Sign 单调包含的三分支唯一反演并对全部残差纤维取 infimum；`derived-checked`。这是**新构造**，可将 C38/C39 对显式 \(T\) 的结论调用到此新关系的完整 resolvent。
- **Counterevidence / Objections / Scope**：历史多步 §5 只给外层 \(T\) 与来源声明，不给原生循环方程全部允许分支；本构造绝不认证历史原生图身份。另一同名 M1/SO-06 是不同算子。新图在指定端点输入窗口的全对 RL 另见 C65；无界全图、历史算法路径对应及外部优先性仍未核。

## C65-v1 / SL-RL · 新 Sign 图端点局部最大全对指数

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C64 **同一个新完整图**上固定 \(\lambda=1,c=2/3\) 和 Minty 输入窗口 \(U=B_\rho((c,0))\)，\(0<\rho<\min\{1/2,c/(2\sqrt{10})\}\)。对所有输入均在 U 的**任意两**图点，有全对 \(\gamma=1/3\) Hölder–RL，常数 \(L_\rho=(2\rho)^{2/3}+2(3/2)^{1/3}10^{1/6}\)；任何包含端点输入的正半径球上、\(\gamma>1/3\) 均失败。
- **Dependencies / Evidence**：[SL-RL](research/topics/path_dynamics/m1_sign_lift.md#sl-rl) 从完整 \(J_F=T\)、\(C(p,q)=(p-2f(p-3q),-q)\)、立方根不等式与端点 \(x_t=(c+t,0)\) 逐项重算；独立逆向检查常数与球的正侧条件。`derived-checked`。
- **Counterevidence / Objections / Scope**：局部全对图块，不称无界域相同指数/常数；只对新构造 C64，不授给历史原生循环方程。端点真残差线性与全对指数 \(1/3\) 不否定 C39 通过同一活动关系得到的一步严格收缩。

## C66-v1 / IS-OP · 身份与平方并图的真残差锐半阶

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：\(F(x)=\{x,x^2\}\) 在 \(\mathbb R\) 上为完整关系，\(S=\{0\}\)；每个 \(0<|x|<1\) 的 \(r_F(x)=x^2\)、\(d(x,S)=|x|\)。固定目标局部半阶 EB 的收缩邻域最优模为 1，任意指数 \(q>1/2\) 失败。最近逆点 \(d(0,F^{-1}(y))=|y|\) (\(|y|<1\)) 是不同量词；全部局部逆像的最优阶仍仅 \(1/2\)。
- **Dependencies / Evidence**：[IS-OP](research/topics/examples/identity_square_branch_union.md#is-operator-eb) 重算完整算子及逆纤维；9/01 ZIP `work/c_gx066_077.md` 的 GX-068 是来源线索。`derived-checked`。
- **Counterevidence / Objections / Scope**：不能把最近逆点线性律当所有原像的线性 calm；同一完整图的两变量半阶 MR 现见 C92，二参数 semimonotonicity 全区域现见 C95，均不改变本固定目标 Claim 的量词。历史 VI 标签与外部先行性未审。

## C67-v1 / IS-STEP · 同一并图的指定步与完整步残差

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 \(\lambda>0\)，完整 \(J_{\lambda F}(p)\) 含身份根 \(p/(1+\lambda)\)，当 \(p\ge-1/(4\lambda)\) 另含平方根的近根与远根（\(p=0\) 远根 \(-1/\lambda\)）。指定身份选择 \(J_1\) 的 fixed-point EB 精确线性模 \((1+\lambda)/\lambda\)；完整最小步残差 \(r_J(p)=\inf_{u\in J(p)}|p-u|=\lambda p^2(1+o(1))\)，故收缩邻域最优半阶模 \(1/\sqrt\lambda\)，所有更高幂次失败。
- **Dependencies / Evidence**：[IS-STEP](research/topics/examples/identity_square_branch_union.md#is-resolvent) 解一元二次方程并比较完整纤维中的三类根，`derived-checked`。
- **Counterevidence / Objections / Scope**：指定分支的线性轨道不能升级成完整多值 J 的任意选择定理；本地锐常数指邻域收缩下确界，不声称固定邻域端点常数取到。

## C68-v1 / IS-RL · 同输入跨支碰撞排除全对模

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C66 的完整图及任何固定 \(\lambda>0\)，任意零邻域存在不同两图点 \((x,x)\)、\((y,y^2)\)，其中 \(0<y<1\)、\(x=(y+\lambda y^2)/(1+\lambda)\)，满足同一 Minty 输入而 Cayley 输出不同。因此包含完整局部两支的图块对任意 \(\gamma>0\) 无有限全对 Hölder–RL 常数，完整 J 也不是局部单值。
- **Dependencies / Evidence**：[IS-RL](research/topics/examples/identity_square_branch_union.md#is-collision) 的同输入零分母计算，`derived-checked`。
- **Counterevidence / Objections / Scope**：不否定任何一条指定单支可能有良好模；与 C67 的残差分离相关但不是由半阶 EB 自动推出。

## C69-v1 / SME-ENVELOPE · 硬支持下非线性证书的锐矩提升

- **Status**：`derived-checked`，证据强度限于该条所列独立推导；适用范围与未闭义务见下。

- **Exact Statement / Objects / Domain / Quantifiers**：\(1\le p<\infty,R>0,\ 0\le t\le R\)，连续非减 \(\varphi:[0,R]\to[0,\infty)\) 且 \(\varphi(0)=0\)；对所有概率空间和所有 \(0\le D\le R\) a.s.、\(\|D\|_p\le t\) 的随机变量取最坏 \(\|\varphi(D)\|_p\)。置 \(g(z)=\varphi(z^{1/p})^p\)，精确 p 次方等于 \(\operatorname{cav}g(t^p)\)，每个 \(t\in[0,R]\) 可由至多两个幅度达到。幂次 \(\varphi(u)=Au^\alpha\) 时得 \(At^\alpha\) (\(\alpha\le1\)) 或 \(AR^{\alpha-1}t\) (\(\alpha\ge1\))；同一个 D 上逐点复合 \(S\le CD^\gamma,D_+\le KS^q\) 的临界 \(\gamma q=1\) 先复合提升为 \(KC^qt\)，分开取两个锐包络给 \(KC^qR^{1-\gamma}t^\gamma\)，比值 \((R/t)^{1-\gamma}\) 只对 \(0<t\le R\) 陈述，且两层 gauge 的输入支持需匹配。
- **Dependencies / Evidence**：[SME-ENVELOPE/POWER](research/topics/random_markov/scalar_moment_envelope.md#sme-envelope) 的紧区间均值集、凹包络、两点极值与同一变量复合；[SME-SUPPORT](research/topics/random_markov/scalar_moment_envelope.md#sme-support) 另证仅小 \(L^p\) 距离无法替代逐点硬支持。`derived-checked`，9/14 质量稀释独立审计 §4 是来源。
- **Counterevidence / Objections / Scope**：上确界对**所有概率律**，不是指定原生耦合的可实现最优值；真实随机 PPA 的合法耦合、目标边缘与更新核须另证。分开聚合的损失不是物理轨道发散。

## C70-v1 / FSC-ENVELOPE-COLLAR · 有限样本包络与整窗内域余量

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：非空闭 \(S=F^{-1}(0)\subset\mathbb R^n\)、\(\lambda,L,c>0\)、\(0<\gamma<1,q>0\)、\(\phi(r)=(r+Lr^\gamma)/2\)。非空有限样本中**每个** \((p_i,y_i)\) 是实际 proximal 对，独立验证 \(\|p_i-y_i\|\le\phi(d(p_i,S))\)、\(d(y_i,S)\le c\|p_i-y_i\|^q\)。定义 \(\rho_i=\phi^{-1}(\|p_i-y_i\|)\)、\(e_i=c\|p_i-y_i\|^q\)、\(g_E(z)=\max_i(\rho_i-\|z-p_i\|)\)、\(u_E(z)=\min_i(\|z-y_i\|+e_i)\)，则**所有** \(z\in\mathbb R^n\) 有 \(g_E(z)\le d(z,S)\le u_E(z)\)。再给非空紧 \(A\subset\operatorname{int}B\)、紧 B，指定 \(T(p)\) 对每个 \(p\in A\) 非空，且以上两估计对**每个** \(y\in T(p)\) 均成立；若 \(\sup_Au_E\le u\)、\(\inf_{B\setminus\operatorname{int}A}g_E\ge m>0\)、\(\phi(u)<d(A,B^c)\)、\(\alpha=c\phi(u)^q<m\)，则对所有 \(p\in A,y\in T(p)\)：\([p,y]\subset B\)、\(y\in\operatorname{int}A\)、\(d(y,A^c)\ge m-\alpha\)。任意 \(\lambda\|h\|_{\infty,A}<m-\alpha\) 的连续扰动沿 \(y+t\lambda h(y)\) 留在内域。
- **Dependencies / Evidence / Status**：[FSC-ENVELOPE/COLLAR](research/canonical/finite_sample_collar.md#fsc-envelope) 给 1-Lipschitz 双包络和 shell 边界的逐式证明；9/25 PDF §8 印刷页 20–21，(8.1)–(8.4)、(8.7) 为来源。`derived-checked` 仅针对度量分析层；有限覆盖误差预算也在正文。输出可为完整 resolvent 的指定子关系。
- **Counterevidence / Objections / Scope**：样本验证不能建立整窗全称条件、非空/usc/acyclic \(T\)。内域余量不提供 \(p=y+\lambda h(y)\) 的 coincidence 或 \(F(\operatorname{int}A)\) 值域球；C05 仍需多面体、拓扑条件和外部定理。该分析链不要求 \(q\gamma>1\)，不能将 C05 的其它前提一并删去。

## C71-v1 / LC-OT · 惰性四循环的锐同步运输误差界

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 \(G=(0,1,3,4)\)、循环 \(T:0\to1\to3\to4\to0\)、\(0<p<1\)，每步概率 \(1-p\) 取 Id、概率 \(p\) 取 T；唯一不变律 \(\pi=(1/4)^4\)。\(C_{ij}=|g_i-g_j|^2\)、\(R_{ij}=p[(g_i-Tg_i)-(g_j-Tg_j)]^2\)。对 **所有** \(\mu\in\Delta_4\)，\(\Psi(\mu)^2=\min_{\eta\in\operatorname{Opt}_C(\mu,\pi)}R\cdot\eta\)，则 \(\Psi^{-1}(0)=\{\pi\}\)、\(W_2(\mu,\pi)\le\sqrt{13/p}\Psi(\mu)\)，系数对这个完整四点律空间最优。
- **Dependencies / Evidence / Status**：[LC-OBJECT/SHARP](research/topics/random_markov/lazy_cycle_ot.md#lc-sharp) 从唯一有序最优耦合、零成本交换、矩阵 \(C-(13/p)R\) 的符号抵消及取等律独立证明。状态 derived-checked，来源为 9/14 有限状态分类稿 §10.2；不继承其余一般结论和优先权声明。
- **Counterevidence / Objections / Scope**：同一输入 \(\mu^+=(1/2,1/4,0,1/4)\) 去掉输入对目标的 **OT 最优性** 后有松弛残差零而真实 \(\Psi^2=p/2\)；见 [LC-RELAX](research/topics/random_markov/lazy_cycle_ot.md#lc-relax)。此例不证明任意有限模型必需点态位移签名分离，也不给变动 \(p\) 的统一常数；随机核相同但残差表示或耦合集改变是另一命题。

## C72-v1 / DS-EB · 对角线竖支图的残差量词分离

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：完整闭关系 \(F(0)=A=\{0\}\cup\{1/n:n\ge1\}\)、\(F(x)=\{x\}\) (\(x\ne0\))，\(S=F^{-1}(0)=\{0\}\)。对所有 \(x\in\mathbb R\)，真 \(r_F(x)=|x|=d(x,S)\)，线性 EB 精确模 1。对所有右端 \(y\) 的完整逆像均有 \(|x|\le|y|\)；但 \(h(y)=d(0,F^{-1}(y))\) 不满足任何零邻域上 \(h(y)\le K\psi(d(y,F(0)))\)，其中 \(K<\infty\)、\(\psi(t)\to0\)；取 \(y\to1/n\) 而不在 \(A\) 给反例。
- **Dependencies / Evidence / Status**：[DS-EB](research/topics/examples/diagonal_spike_relation.md#ds-eb) 逐纤维公式与目标序列独立证明；9/01 ZIP GX-075 仅为观察来源。derived-checked。
- **Objections / Scope**：固定零目标、全部逆像的 \(|y|\) 界和右端到 \(F(0)\) 的两变量 MR 是不同残差；后者失败专指以零为参考的目标邻域。外部先行性未核。

## C73-v1 / DS-PPA · 完整近端每条合法路径的锐收敛

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C72 同一完整 \(F\) 上，固定任意 \(\lambda>0\)、\(\tau=(1+\lambda)^{-1}\)。对每个 \(p\in\mathbb R\)，完整 \(J_{\lambda F}(p)=\{\tau p\}\cup(\{0\}\text{ if }p\in\lambda A)\)、\(\operatorname{Fix}J=\{0\}\)、真最小步 \(r_J(p)=(1-\tau)|p|\)。对每个初值和 **每条** 无限合法选择路径 \(p_{k+1}\in J(p_k)\)，\(|p_k|\le\tau^k|p_0|\)、\(\sum_k|p_{k+1}-p_k|=|p_0|\)、\(p_k\to0\)。最坏统一因子 \(\tau\) 及全域步 EB 模 \((1+\lambda)/\lambda\) 均锐。
- **Dependencies / Evidence / Status**：[DS-PPA](research/topics/examples/diagonal_spike_relation.md#ds-ppa) 解完整方程并列出两种选择，保号望远镜求和；derived-checked。
- **Objections / Scope**：每条实际路径的结论不能用来反推完整图全对 RL；零重置只在离散输入，始终取对角分支实现锐因子。

## C74-v1 / DS-RL · 锚定最优与全对全模失败并存

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C72 同一完整图，任意固定 \(\lambda>0\)，每图点相对 \((0,0)\) 有 \(|u-\lambda v|\le|u+\lambda v|\)，最优零锚常数为 1。对任意原点完整图邻域，存在趋零的两图点 \((0,c_n)\)、\((\lambda c_n/(1+\lambda),\lambda c_n/(1+\lambda))\)，其 Minty 输入同为 \(\lambda c_n\) 而 Cayley 输出不同；故每个 \(\omega(0)=0\) 的完整全对模均失败，尤其任何 Hölder–RL。
- **Dependencies / Evidence / Status**：[DS-RL](research/topics/examples/diagonal_spike_relation.md#ds-rl) 的碰撞和端点竖支取等，derived-checked。
- **Objections / Scope**：闭图、全输入 coverage、C72/C73 两种真线性 EB 和全选择线性收敛的合取仍不修复同输入非单值；这不攻击全对 RL 的充分收敛定理。

## C75-v1 / DS-QUADRATIC · 同图的精确二参数区域

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：仍在 C72 的全部完整图点对上，以 \(a=\Delta u,b=\Delta v\) 定义 \(ab\ge\mu a^2+\rho b^2\)。全域有效参数区与原点任意完整图邻域的局部有效区均精确为 \(\mu<0,\rho<0,\mu\rho\ge1/4\)，包含边界；单参数 hypo/cohypo 下模均为 \(-\infty\)。
- **Dependencies / Evidence / Status**：[DS-QUADRATIC](research/topics/examples/diagonal_spike_relation.md#ds-quadratic) 用跨支差实现任意斜率并核二次式最大值；derived-checked。
- **Objections / Scope**：该区亦是一般实差的负负正定门，本例的意义在于局部所有斜率可由趋零图点实现；不推出其它例卡的 semimonotonicity 区。

## C76-v1 / HP-FIXED · 分段抛物映射的半阶固定目标与线性最近逆点

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：完整 \(\Theta:\mathbb R^2\to\mathbb R\)，\(\Theta(a,b)=a+b^2\) 当 \(a\ge0\)，否则 \(a-b^2\)，欧氏范数，参考 \(((0,0),0)\)。对所有 \((a,b)\)，\(|\Theta(a,b)|=|a|+b^2\)，零集仅原点；局部固定目标 \(d((a,b),S)\le|\Theta(a,b)|^{1/2}\) 的最高幂指数为 \(1/2\)、该指数锐模 1。对所有 \(0<|y|<1/2\)，完整逆纤维的**最近**点距 \(d(0,\Theta^{-1}(y))=|y|\)，线性 HREG/UHREG 锐模 1；整纤维的 centered inverse calmness 只有半阶最大指数。
- **Dependencies / Evidence / Status**：[HP-FIXED](research/topics/examples/hemiregular_piecewise_parabola.md#hp-fixed) 列出正负完整纤维和取等序列，`derived-checked`；Uderzo Example 2.3 只提供对象及定性 HREG/非 MR，一般锐模是本库重算。
- **Counterevidence / Scope**：最近逆点不代表所有逆点；\(\Theta\) 不在同一 Hilbert 空间自映射，PPA/Cayley/RL 不适用，图在参考点不局部闭。

## C77-v1 / HP-MR · 共同窗口两变量锐半阶 MR

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C76 同一完整 \(\Theta\) 和全部 \(|a|,|b|,|y|\le1/4\)，\(d((a,b),\Theta^{-1}(y))\le|\Theta(a,b)-y|^{1/2}\)。最大两变量幂指数 \(1/2\)，局部锐模 1。对任何小正 \(y\)，完整逆纤维在零附近非单点，故不存在任何强逆局部单值化。
- **Dependencies / Evidence / Status**：[HP-MR](research/topics/examples/hemiregular_piecewise_parabola.md#hp-mr) 分同号、异号及负目标开放端点的全部情形证明；`derived-checked`，不调用局部闭图外部定理。
- **Counterevidence / Scope**：原点连续不保证任何邻域内图局部闭；零目标线性 MR 已由 \((0,t)\) 反证。不同维数对象不得赋予全对 RL 身份。

## C78-v1 / AV-OP · 绝对值次梯度的残差跳跃与逆像钉住

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：完整 \(F=\partial|\cdot|:\mathbb R\rightrightarrows\mathbb R\)，\(S=\{0\}\)。对每个非零 \(x\)，真残差 \(r_F(x)=1\)，而 \(r_F(0)=0\)；固定目标局部线性 EB 的可行系数下确界为 0。对每个 \(|y|<1\)，完整 \(F^{-1}(y)=\{0\}\)，故局部逆 Aubin、强度量正则及两变量 MR 的系数下确界亦为 0。
- **Dependencies / Evidence / Status**：[AV-OP](research/topics/examples/absolute_value_subgradient.md#av-operator) 全纤维及邻域量词直接计算，`derived-checked`；来源 GX-077 仅观察别名。
- **Counterevidence / Scope**：下确界 0 不表示在含非零输入的某固定邻域内可取系数 0；残差小于 1 的窗口是只含零点的真空范围，不与全邻域误差界混同。

## C79-v1 / AV-PROX · 同图近端步残差锐模 1

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C78 同一完整关系，固定每个 \(\lambda>0\)，全输入 \(J_{\lambda F}(p)=\operatorname{sgn}(p)(|p|-\lambda)_+\)。在全部 \(|p|<\lambda\)，\(\operatorname{Fix}J=\{0\}\)，且 \(d(p,\operatorname{Fix}J)=|p-J(p)|=|p|\)，局部步残差线性 EB 锐系数 1、一步进入零点。全图反射 \(2J-I\) 的 Lipschitz/全对线性 RL 锐常数 1；无界全图的任何 \(0<\gamma<1\) 有限 Hölder 常数失败。
- **Dependencies / Evidence / Status**：[AV-PROX](research/topics/examples/absolute_value_subgradient.md#av-prox) 完整解近端包含式及分段反射证明，`derived-checked`。
- **Counterevidence / Scope**：原算子残差局部系数下确界 0 不转移到近端步残差；全域步 EB 不成立，局部 \(\gamma<1\) 可继承界不表示全图次线性 RL。

## C80-v1 / FS-REGULARITY · 有限状态同步残差平方的连续分片仿射性

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定有限互异状态 \(G=\{g_1,\ldots,g_N\}\subset\mathbb R^d\)、有限随机自映射与权重、同噪声成本 \(R\)、平方欧氏运输成本 \(C\)、**全部**不变律 \(\mathcal I\)，以及 C15 (FS2) 的原始嵌套最优耦合残差 \(\Phi=\Psi^2\)。对**全部** \(\mu,\mu'\in\Delta_N\)，存在依赖固定系统的 \(L<\infty\)，使 \(|\Phi(\mu)-\Phi(\mu')|\le L\|\mu-\mu'\|_1\)；\(\Phi\) 是有限连续分片仿射函数，且 \(|\Psi(\mu)-\Psi(\mu')|\le\sqrt L\|\mu-\mu'\|_1^{1/2}\)。不以 C15 的 exact-zero 判据为前提。
- **Dependencies / Evidence / Status / Related Files**：[FS-REGULARITY](research/topics/random_markov/finite_state_certificate.md#fs-regularity) 的最大耦合成本估计、固定系数最优计划多面体 Hoffman 界、有限 LP 分支细分；[LIT-HOFFMAN-1952](research/LITERATURE.md#lit-hoffman-1952) 逐条件导入。来源 9/14 有限状态稿 §6，但证明由本库重写；`derived-checked` 限固定有限数据。§5 的 [FS-HOFFMAN](research/topics/random_markov/finite_state_certificate.md#fs-hoffman) 是同一 C15 存在性结论的独立非锐证明，不改变 C15 身份。
- **Counterevidence / Objections / Scope**：\(\Phi\) 未被证明凸；嵌套最小化本身不能保证连续性。\(L\) 不跨核或状态集统一，\(\Psi\) 的半阶是可用上模而未宣称各模型均锐；此正则性单独不蕴含 \(\Phi^{-1}(0)=\mathcal I\) 或 EB/动力收敛。原稿先行性与无限状态推广未核。

## C81-v1 / SIN-PHASE · 正值正弦图的完整步长三相

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：完整 \(F(x)=2+\sin x:\mathbb R\to\mathbb R\)，每个固定 \(\lambda>0\)，Minty \(g_\lambda=x+\lambda F(x)\)，反射 \(c_\lambda=x-\lambda F(x)\)。对 \(0<\lambda<1\)，完整 \(J=g_\lambda^{-1}\) 全域单值且全图线性全对 RL 锐常数 \((1+\lambda)/(1-\lambda)\)。\(\lambda=1\) 全域仍单值；在每个 \(x_0=(2m+1)\pi\) 的缩参数窗，全对最高局部指数 \(1/3\)，该指数常数下确界 \(4\sqrt[3]3\)；**只固定基点** \(x_0\) 的下确界为 \(2\sqrt[3]6\)。任意 \(\lambda>0\) 的无界全图 \(0<\gamma<1\) 失败；\(\lambda=1\) 全图线性亦失败。\(\lambda>1\) 完整图出现同输入不同反射输出，对任何零消失全图模都失败。
- **Dependencies / Evidence / Status / Related Files**：[SIN-PHASE](research/topics/examples/positive_sine_phase.md#sin-phase) 的割线、全体临界端点的积分界 (SN4)、对称取等序列与显式同输入碰撞；`derived-checked`，来源 ZIP GX-064 的同对象观察，CCA-M08 将旧 `C-DISAGREE` 精化为 `C-REFINE`。
- **Counterevidence / Scope**：完整自然输入域有 coverage，但 \(\lambda>1\) 无全图单值；正规局部分支未被碰撞反例否定。锐常数是缩窗系数**下确界**，不是预定窗口取到值；全图次线性失败与局部临界半阶/三分之一阶不得混写。\(S=F^{-1}(0)=\varnothing\)，没有零目标 PPA 定理可由此调用。

## C82-v1 / SIN-TARGET · 非零目标的锐固定目标半阶

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C81 同一完整 \(F\)，参考 \((\bar x,\bar y)=(\pi/2,3)\)，\(x\) 仅在 \(\bar x\) 的局部窗，完整逆纤维 \(F^{-1}(3)\)。固定目标 EB \(d(x,F^{-1}(3))\le K|F(x)-3|^q\) 的最高指数 \(q=1/2\)，该指数缩窗锐系数下确界 \(\sqrt2\)；较低正指数下确界 0，较高指数无有限系数。任何要求目标 \(y\) 在 3 的**双侧邻域**且对全部近输入成立的正指数两变量 MR 失败，因为 \(y>3\) 有空逆像。
- **Dependencies / Evidence / Status / Related Files**：[SIN-TARGET](research/topics/examples/positive_sine_phase.md#sin-target) 的完整逆像及 \(1-\cos h\sim h^2/2\)；`derived-checked`，来源同一 GX-064 的非零目标观察。
- **Counterevidence / Scope**：C81 的临界 \(x_0\) 对应输出 2，而本 Claim 的目标是 3；\(F^{-1}(0)=\varnothing\)。[SIN-BOUNDARY](research/topics/examples/positive_sine_phase.md#sin-boundary) 逐步证明每条完整近端选择路径趋 \(-\infty\)，因此不能把两个局部锐指数当零点收敛证书。外部新颖性未核。

## C83-v1 / BS-PHASE · 有界平方完整图的 Minty 端点相变

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：\(F(x)=\{x^2\}\) 仅在 \([-1,1]\)，其余为空；每个固定 \(\lambda>0\) 对**整个**完整图所有点对求 RL 锐模。\(0<\lambda<1/2\) 时自然输入域上完整 \(J\) 单值，全图线性锐常数 \((1+2\lambda)/(1-2\lambda)\)。\(\lambda=1/2\) 仍单值，全图最高 Hölder 指数 \(1/2\)，该指数锐常数 \(2\sqrt2\)，低于半阶的锐常数见 (BS5)，高于半阶失败。\(\lambda>1/2\) 有同输入跨图点碰撞，无零消失全对模。
- **Dependencies / Evidence / Status / Related Files**：[BS-PHASE](research/topics/examples/bounded_square_minty.md#bs-phase) 以完整区间的割线 (BS2)、可实现点对约束 (BS3)–(BS5) 和对称折叠重算；`derived-checked`。来源 ZIP GX-065 的此观察，旧 PASS 标签不是证据。
- **Counterevidence / Scope**：临界全图半阶来自 **\(x=-1\) 端点**，在零点邻域线性 RL 缩窗常数下确界为 1；自然输入域有限，不能声称满实输入或把端点半阶当作零点局部半阶。

## C84-v1 / BS-ZERO · 同图零残差半阶及临界两侧合法路径

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C83 同一 \(F\)，完整算子真残差 \(r_F(x)=x^2\) 在 \([-1,1]\)，\(S=\{0\}\)，故固定零目标局部 EB 最高指数 \(q=1/2\)，锐缩窗系数 1。固定 \(\lambda=1/2\)、完整 \(J\) 和实际自然输入域 \([-1/2,3/2]\)：每个 \(0<p_0<3/2\) 的唯一无限路径 \(p_{k+1}=J(p_k)\) 满足 \(kp_k\to2\)；每个 \(-1/2\le p_0<0\) 仅有有限条合法步，最终离开自然输入域。
- **Dependencies / Evidence / Status / Related Files**：[BS-ZERO](research/topics/examples/bounded_square_minty.md#bs-zero) 的完整残差恒等式、逆图迭代和有界单调反证；`derived-checked`。零目标观察取材于 GX-065，正/负路径是本仓库新增推导。
- **Counterevidence / Scope**：双侧目标 MR 因负目标空逆像失败。全图半阶 RL 和零点真 EB 可在零点小窗合取；但全图半阶的**锐性见证**在左端点，零点局部 RL 可线性，且半阶相乘只得 \(q\gamma=1/4\)，不满足收缩兼容门。负侧轨道又失去不变域，故不能从两个半阶数字声称统一局部收敛。

## C85-v1 / SR-GEOMETRY · 受限负平方根图的锐成对常数

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：完整受限关系 \(F_U(x)=\{-\sqrt x\}\) 当 \(0\le x\le1/16\)、其余为空，单位步长；对图中任意**两**点，图差 \(a=\Delta x,b=\Delta v,d=a+b,r=a-b\)。最小有效非负 LT \(ab\ge-\tau d^2\) 常数 \(\tau=2\)，全对线性 \(|r|\le L|d|\) 锐 \(L=3\)，cohypomonotone \(ab\ge-\rho b^2\) 锐 \(\rho=1/2\)。任意原点右图窗无有限 \(ab\ge-\rho a^2\) 的 hypomonotone 常数。
- **Dependencies / Evidence / Status**：[SR-GEOMETRY](research/topics/examples/restricted_root_graph.md#sr-geometry) 以参数 \(s,t\in[0,1/4]\) 的全部图点割线和逼近端点重算；`derived-checked`。来源 GX-032 仅作为线索，成员定位见逐源表。
- **Counterevidence / Scope**：只用于受限图和单位步长；不授给母图 \(F_\infty(x)=-\sqrt x\) (\(x\ge0\)) 的完整 resolvent。历史命名及外部优先性未核。

## C86-v1 / SR-ESCAPE · 受限真二次 EB 不给第二步

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C85 同一完整受限 \(F_U\)，自然输入域 \(D_U=[-3/16,0]\)，每个非零 \(p\in D_U\) 唯一输出 \(J_{F_U}(p)=t(p)^2>0\notin D_U\)。全部图输出的真残差 \(r_{F_U}(x)=\sqrt x\)，\(S_U=\{0\}\)，故固定零目标 \(d(x,S_U)=r_{F_U}(x)^2\) 的最高局部幂 2、系数 1；\(p\uparrow0\) 的锐一步比值 \(J(p)/|p|^2\to1\)，但无任何非零两步合法路径。
- **Dependencies / Evidence / Status**：[SR-ESCAPE](research/topics/examples/restricted_root_graph.md#sr-escape) 的完整逆图根、自然域和全输出残差直接证明；`derived-checked`。
- **Counterevidence / Scope**：一步模与真 EB 是有效结果；没有输入不变域，不能称“二次收敛”。若改回完整母图，输入域、纤维及命题身份均变。

## C87-v1 / SR-PARENT · 半直线母图的完整远支

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：定义**另一个**完整关系 \(F_\infty(x)=\{-\sqrt x\}\) 当 \(x\ge0\)、其余为空；固定 \(\lambda=1\)，完整自然域 \([-1/4,\infty)\)，\(-1/4\le p\le0\) 的全部输出为 \(t_\pm(p)^2\)，\(p>0\) 仅为 \(t_+(p)^2\)，\(p<-1/4\) 为空。\(J_{F_\infty}(0)=\{0,1\}\) 阻断所有零消失全对 RL；任何非零合法初始输入的每条完整近端路径在第一步后为唯一正路径并趋 \(+\infty\)，零初值可恒零或稍后逃逸。
- **Dependencies / Evidence / Status**：[SR-PARENT](research/topics/examples/restricted_root_graph.md#sr-parent) 完整二次根及逐步差分证明；`derived-checked`。母图身份来自原 GX-032 的第一句，全部路径是本库新增推导。
- **Counterevidence / Scope**：受限图 \(\Gamma\) 的公式只对其短支与短域成立；不得把受限 \(L=3\)、二次一步或零目标路径结论移植给母图。旧稿的 LT 外部调用及先行性另审。

## C88-v1 / LCR-SHARP · 同一四状态核的表示相关同步 OT 模

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 \(G=(0,1,3,4)\)、循环 \(T\)、每个 \(0<p<1\)、同一个 \(P_p=(1-p)I+pT_\#\)、唯一不变律 \(\pi\) 与平方距离成本 \(C\)。另定义一次噪声中的四个逐状态独立 Bernoulli\((p)\) 开关；对**每个** \(\mu\in\Delta_4\)，仅在 \(\operatorname{Opt}_C(\mu,\pi)\) 上对其同噪声位移成本取最小 \(\Psi_{\rm ind}^2\)。于是 \(\Psi_{\rm ind}^{-1}(0)=\{\pi\}\)，且 \(W_2^2(\mu,\pi)\le[13/(p(7-6p))]\Psi_{\rm ind}(\mu)^2\)，系数全律空间锐。共同开关表示的对应锐平方系数为 C71 的 \(13/p\)。
- **Dependencies / Evidence / Status / Related Files**：[LCR-OBJECT/SHARP](research/topics/random_markov/lazy_cycle_representations.md#lcr-sharp) 的全部成本、两项无交叉抵消界及取等计划独立证明；C71 提供同对象 \(C\le13A\) 的已核引理。`derived-checked`；这是本库新增表示和命题，不是历史 C71 的来源报告。
- **Counterevidence / Scope**：核和平稳律相同不代表同步成本相同；i=j 时两分支必须使用同一个噪声，不能套独立输入公式。结论限此四点几何、固定 \(p\) 与 OT 最优计划；不推出随机轨道的收敛率或跨表示统一残差。

## C89-v1 / NT-QUADRATIC-SHARP-STEP · 非 tied 二参数图的精确 Cayley 球

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实非零 Hilbert 空间、固定 \(\lambda>0,\mu,\rho\in\mathbb R\)、非空完整关系图或指定图块 \(\Gamma\)。对**任意两**图点以 \(a=\Delta x,b=\Delta v\) 要求 \(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\)。令 \(m=\lambda\mu,s=\rho/\lambda,A=1+m+s,B=m-s,\Delta=1-4\mu\rho\)。另记 \(d=a+\lambda b,r=a-\lambda b\)。无参数门时它等价于 \(A\|r\|^2+2B\langle d,r\rangle\le(1-m-s)\|d\|^2\)；若 \(A>0,\Delta\ge0\)，则等价于 \(\|r+(B/A)d\|\le(\sqrt\Delta/A)\|d\|\)，自然域上的 Cayley 单值，普适锐反射和近端 Lipschitz 上界分别为 \((|B|+\sqrt\Delta)/A\) 与 \((|1+2s|+\sqrt\Delta)/(2A)\)。\(\Delta>0\) 时此类统一保证单射的锐步长门是 NT9 的开区间；端点 \(A\le0\) 存在完整碰撞图。
- **Dependencies / Evidence / Status / Related Files**：[NT-QUADRATIC/SHARP/STEP](research/canonical/non_tied_cayley.md#nt-quadratic) 的配方、完整 Minty 域线性取等图和端点反例逐项证明。来源是 9/01 ZIP `work/a_monotonicity.md` §2.1 精确单元，哈希和另一字节相同 checkpoint 见正文；`derived-checked` 限数学推导，文献新颖性未核。
- **Counterevidence / Scope**：反射一个未平移的 Lipschitz 常数不能恢复非 tied 交叉项；只在图块得图块近端单值，不产生完整 \(J_{\lambda F}\) 的 coverage、排他或真残差 EB。\(\Delta<0\)、\(A\le0\) 不套平方根上界。

## C90-v1 / NT-TRANSFORM · 二参数图到单调图的双射

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C89 的同一全对图及任意 \(\Delta=1-4\mu\rho>0\)，不另要求步长门，令 \(t=\sqrt\Delta,\nu=2\mu/(1+t),\xi=\rho/t,w=v-\nu x,z=x-\xi w\)。全部图点的线性双射 \((x,v)\mapsto(w,z)\) 将 C89 二参数图条件等价地送到单调图条件，并在整个 \(H\times H\) 保图包含；全局同 \((\mu,\rho)\) 图极大当且仅当变换图极大单调。
- **Dependencies / Evidence / Status / Related Files**：[NT-TRANSFORM](research/canonical/non_tied_cayley.md#nt-transform) 的逆公式和 \(\langle\Delta w,\Delta z\rangle=t^{-1}(\langle a,b\rangle-\mu\|a\|^2-\rho\|b\|^2)\) 直接证明；同一 9/01 ZIP §2.1 为来源，`derived-checked`。
- **Counterevidence / Scope**：\(\Delta=0\) 时该变换因 \(1/t\) 无定义；不得用 C91 的零判别式扩张范围替代。这里的极大性是全图、同参数的包含极大，不是局部极大或未经变换的普通极大单调。

## C91-v1 / NT-MAXIMAL · 非 tied 图极大性与满 Minty 输入域

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：固定 C89 的实 Hilbert 空间和 \(\lambda,\mu,\rho\)，假设 \(A>0,\Delta\ge0\)；对每个非空、完整或图块视作**独立完整图对象**的全对二参数图 \(\Gamma\)，全局同参数图极大当且仅当其 Minty 自然域 \(D=H\)。每个这样的图可在保持相同参数下扩张到满域；\(\Delta=0\) 亦在范围内。
- **Dependencies / Evidence / Status / Related Files**：[NT-MAXIMAL](research/canonical/non_tied_cayley.md#nt-maximal) 将 C89 的平移 Cayley \(\sqrt\Delta/A\)-Lipschitz 映射用已核 [HE-EXTENSION](research/canonical/holder_extension.md#he-extension) 的 \(\gamma=1\) Hilbert 同常数扩张后反剪切；反向用同输入唯一性。`derived-checked`；同一 9/01 ZIP §2.1 满域句是来源种子。
- **Counterevidence / Scope**：不从局部窗口图极大推出全空间 coverage；对完整母关系的指定子图作极大扩张是新对象，不能把原关系域外纤维一并认证。满域也不产生零点、真残差 EB 或近端动力收敛。

## C92-v1 / IS-MR · 身份与平方完整并图的两变量半阶 MR

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：完整 \(F(x)=\{x,x^2\}:\mathbb R\rightrightarrows\mathbb R\)。对每个 \(0<\delta\le1/3\)、所有 \(|x|,|y|<\delta\)，\(d(x,F^{-1}(y))\le d(y,F(x))^{1/2}\)，共同窗口系数 1 取等、最大局部指数 \(1/2\)；对**系数恰为 1 的对称开窗口**最大半径为 \(1/3\)。对 \(|u|,|v|<\delta\)、全部 \(z\in F^{-1}(u)\cap(-\delta,\delta)\) 又有 \(d(z,F^{-1}(v))\le|u-v|^{1/2}\)，系数锐 1；完整逆像不存在原点单值局部化。
- **Dependencies / Evidence / Status / Related Files**：[IS-MR](research/topics/examples/identity_square_branch_union.md#is-mr) 从完整逆纤维逐正负目标和身份/平方残差重算；来源 9/01 ZIP `work/c_consistency_audit.md` §CCA-M14 的半阶观察，本库另证最大对称窗口。`derived-checked` 限此对象和共同窗口；证据不是有限计算。
- **Counterevidence / Objections / Scope**：C66 固定目标真残差、C67 完整近端最小步、(I3) 最近逆点线性律与本两变量 MR 量词不同。半阶逆 Aubin 不给线性 MR，也不等于单值局部化；C68 同图全对 RL 仍因同输入碰撞失败。二参数区域现另由 C95 核定；外部优先性未核。

## C93-v1 / BN-GEOMETRY · 闭球完整法锥的两参数图与全域反射

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：每个 \(m\ge1\)、\(B=\{x\in\mathbb R^m:\|x\|\le1\}\)、完整 \(F=N_B\)，每个 \(\lambda>0\) 满全输入 \(J_{\lambda F}=P_B,R=2P_B-I\)。对**全部图点对**，\(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\) 当且仅当 \(\mu\le0,\rho\le0\)；反射全域线性 RL 锐 \(L=1\)，任何无界全对 \(0<\gamma<1\) 的有限 Hölder 常数失败。
- **Dependencies / Evidence / Status / Related Files**：[BN-GEOMETRY](research/topics/examples/ball_normal_cone.md#bn-geometry) 直接用法锥不等式、完整投影与 firm nonexpansiveness；`derived-checked`。来源 9/01 ZIP `work/c_gx066_077.md` GX-067 仅作对象线索。
- **Counterevidence / Scope**：图上的 \(\mu=\rho=0\) 不表示强单调或正 cocoercive；有界输入窗可继承低指数，不可转述成全域低指数。其它历史 VI 标签和外部先行性未核。

## C94-v1 / BN-REGULARITY · 法锥真空 MSR 与扰动逆像不稳定

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C93 同一完整 \(N_B\)，每个 \(\bar x\in B\) 的参考 \((\bar x,0)\)，\(S=B\)。固定零目标的真残差 EB/MSR 可行系数下确界为 0，因为域内残差和距离同时为零、域外残差为 \(+\infty\)；逆关系 ordinary calm 的局部系数亦为 0。对任意这样的参考点，全部正指数的两变量 Hölder MR 与固定输入 hemiregularity 失败；inverse Aubin 失败；SMSR/isolated calm 因零点不孤立而失败。
- **Dependencies / Evidence / Status / Related Files**：[BN-REGULARITY](research/topics/examples/ball_normal_cone.md#bn-regularity) 分球内、\(m=1\) 边界、\(m\ge2\) 边界逐目标构造；`derived-checked`，只属 GX-067 选定单元。
- **Counterevidence / Objections / Scope**：零系数是域/大零集机制，不能作为非真空正残差增长，也不能推目标扰动稳定。若将零目标改为球心或边界是不同命题；历史其它性质及优先权待审。

## C95-v1 / IS-SEMIMONO · 身份平方完整并图的精确二参数区域

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C66 的同一完整关系 \(F(x)=\{x,x^2\}\)，在全图或原点处同时含两支的任意共同小图点窗，对**所有两图点**要求 \(ab\ge\mu a^2+\rho b^2\)。精确参数集合 \(\Sigma(F)=\{(\mu,\rho):\mu<0,\rho<0,\mu\rho\ge1/4\}\)；全部实数割线斜率在每个共同原点窗可实现，故局部不能扩大区域。每个 \(\lambda>0\) 与有效参数对均有 \(A=1+\lambda\mu+\rho/\lambda\le0\)、\(\Delta=1-4\mu\rho\le0\)，无一满足 C89/C91 的 \(A>0,\Delta\ge0\) 联合门。
- **Dependencies / Evidence / Status / Related Files**：[IS-SEMIMONO](research/topics/examples/identity_square_branch_union.md#is-semimono) 的跨支斜率实现、全实二次多项式极小与 AM–GM；[C89](research/canonical/non_tied_cayley.md#nt-quadratic) 的参数定义。来源 9/01 ZIP `work/c_gx066_077.md` GX-068 的区域观察，现独立重算；`derived-checked`，已做独立敌对复核。
- **Counterevidence / Objections / Scope**：边界 \(\mu\rho=1/4\) 包含在内；\(A=0\) 仅在该边界的配平步长。此签名区域不提供非负 hypomonotone/cohypomonotone 单项模，也不能压倒 C68 的同输入跨支碰撞。C92 的两变量半阶 MR 与全对 RL 失败共存；VI 标签与外部先行性另核。

## C96-v1 / BNI-MINTY · 有界负恒等图的全对步长相变

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：完整实关系 \(F(x)=\{-x\}\) 对 \(|x|\le1\)，其余为空。每个固定 \(\lambda>0\)，任意两图点、同一 \(\lambda\)：若 \(\lambda\ne1\)，自然输入域 \(D_\lambda=(1-\lambda)[-1,1]\)，完整 \(J(p)=p/(1-\lambda)\)，完整反射 \(C(p)=(1+\lambda)p/(1-\lambda)\)。全图线性 RL 锐常数 \((1+\lambda)/|1-\lambda|\)，每个 \(0<\gamma<1\) 的锐常数 \(2^{1-\gamma}(1+\lambda)|1-\lambda|^{-\gamma}\)。\(\lambda=1\) 时 \(D_1=\{0\},J_F(0)=[-1,1]\)，同输入不同输出排除任意零消失全对模。完整真残差在 \(|x|\le1\) 为 \(r_F(x)=|x|=d(x,\{0\})\)，域外为 \(+\infty\)；此处只作固定零目标 EB。
- **Dependencies / Evidence / Status / Related Files**：[BNI-MINTY](research/topics/examples/bounded_negative_identity.md#bni-minty) 由全部完整图点剪切重算，来源 9/01 ZIP `work/c_gx066_077.md` GX-066；`derived-checked`，无外部定理调用。
- **Counterevidence / Scope**：低于一阶的常数使用图直径 2；换成无界母图即是新对象。\(\lambda=1\) 的残差 EB 不产生输入覆盖；不能拼接不同步长的纤维。

## C97-v1 / BNI-PATH · 同图全部合法近端路径的步长分类

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C96 的同一完整关系，每个固定 \(\lambda>0\)、每个 \(p_0\in D_\lambda\)、每条每步输入留在 \(D_\lambda\) 的近端路径。\(0<\lambda<2,\lambda\ne1\) 的每个非零初值有限步越域；\(\lambda=1\) 唯一无限合法路径恒零；\(\lambda=2\) 的非零初值二周期；\(\lambda>2\) 所有初值的唯一无限路径以锐因子 \((\lambda-1)^{-1}\) 有限长趋零。同一 \(\lambda>2\) 的反射线性模却是 \((\lambda+1)/(\lambda-1)>1\)。
- **Dependencies / Evidence / Status / Related Files**：[BNI-PATH](research/topics/examples/bounded_negative_identity.md#bni-path) 的闭式迭代、自然域检查和边界分类；依赖 C96 的完整 \(J\) 纤维，`derived-checked`。来源 GX-066 的图公式为线索，步长全路径分类由本库推导。
- **Counterevidence / Scope**：有限步越域不等于发散的无限合法轨道；\(\lambda>2\) 的动力稳定不能倒推反射收缩，也不反驳含 \(L<1\) 等额外前提的定理。

## C98-v1 / SB-INVERSE · 斜旋转法锥的完整逆像与全域锐半阶

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：\(K=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\)，\(B\subset\mathbb R^2\) 为闭单位盘，完整 \(F=K+N_B\)。对全部目标 \(y\in\mathbb R^2\)，\(F^{-1}(y)=\{G(y)\}\)，其完整显式公式为 (SB1)。任意图点对满足 \(\|x-z\|^2\le2\|u-v\|\)；因此对**全部** \(u,v\in\mathbb R^2\) 与 \(0<q\le1/2\)，\(\|G(u)-G(v)\|\le2^{1-q}\|u-v\|^q\)。对全部 \(x\in B,y\in\mathbb R^2\)，\(\|x-G(y)\|\le2^{1-q}d(y,F(x))^q\)。两式的全域系数锐，每个 \(q>1/2\) 在边界附近失败。
- **Dependencies / Evidence / Status / Related Files**：[SB-INVERSE](research/topics/examples/skew_ball_inverse.md#sb-inverse) 的全纤维求逆、三类图点配对及边界取等；来源 9/01 ZIP `work/c_gx053_065.md` GX-058 的对象和边界观察，锐全域结论为本库新增推导；`derived-checked`，无外部定理调用。
- **Counterevidence / Scope**：两变量 MR 限 \(x\in B\)，避免盘外无值残差与零系数语义；这是原算子的逆映射与 MR，不是 Cayley 反射 RL。其它旧属性和外部先行性未核。

## C99-v1 / SB-BOUNDARY · 非零边界目标的局部锐半阶

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C98 同一完整图，每个单位 \(\bar x\) 取 \(\bar y=K\bar x\ne0\)。固定目标 \(F^{-1}(\bar y)=\{\bar x\}\) 且对**全部** \(x\in B\) 有 \(\|x-\bar x\|^2\le2d(\bar y,F(x))\)。在 \((\bar x,\bar y)\) 共同邻域，固定目标 MSR、两变量 MR、逆映射 Hölder 的半阶系数下确界均为 \(\sqrt2\)；\(q<1/2\) 的局部系数下确界为 0，\(q>1/2\) 失败。全局 \(q\le1/2\) 的取等发生在对径点，与局部锐见证分开。
- **Dependencies / Evidence / Status / Related Files**：[SB-BOUNDARY](research/topics/examples/skew_ball_inverse.md#sb-boundary) 的同一完整法向射线 \(z_\theta,v_\theta\) 同时取最近残差与逆像距离；依赖 C98 的上界，`derived-checked`。
- **Counterevidence / Scope**：\((0,0)\) 的局部图为可逆旋转，普通线性 MR/MSR 系数 1；边界非零目标的半阶不能移植为零目标正则性。低幂零局部下确界不能写成非平凡邻域中系数 0 的可达界。

## C100-v1 / BNS-MINTY · 有界负平方完整图的全对步长相变

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实完整关系 \(F(x)=\{-x^2\}\) 当 \(0\le x\le1/2\)、其余为空；固定每个 \(\lambda>0\)，对**全部**两图点且同一步长：\(0<\lambda<1\) 的完整 Minty 自然域为 \([0,1/2-\lambda/4]\)，单值且全图线性 RL 锐常数 \((1+\lambda)/(1-\lambda)\)；\(\lambda=1\) 的自然域 \([0,1/4]\)，单值但全图临界指数 \(1/2\) 锐常数 2，低指数锐值为 (NS5)；\(\lambda>1\) 有完整图同输入跨点碰撞，排除任意零消失全对反射模。
- **Definitions / Dependencies / Evidence / Status / Related Files**：[BNS-OBJECT/MINTY](research/topics/examples/bounded_negative_square.md#bns-minty) 从所有区间点对、可实现差值和端点序列重算；来源是 9/01 ZIP `work/c_gx053_065.md` 的 GX-053 选定观察；`derived-checked`，不调用外部定理。
- **Counterevidence / Scope**：全图半阶锐性发生在 \(1/2\) 端点，不是零点局部指数；临界 \(J\) 只在自然域定义；局部缩图的 RL 与完整母图的全对条件是不同命题。历史 Spingarn 名称、VI 分类和先行性未审。

## C101-v1 / BNS-ZERO-PATH · 真零残差与临界合法路径越域

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C100 的同一完整图，\(S=\{0\}\)；对每个域内 \(x\)，\(d(x,S)=r_F(x)^{1/2}\)，固定零目标的最大局部幂次 \(q=1/2\)，系数 1 锐。固定 \(\lambda=1\)，对**每个** \(p_0\in[0,1/4]\) 和每一步在自然域的完整近端路径：零路径恒零；每个正初值的唯一合法路径只能有限步延续，随后输出越出自然输入域。
- **Definitions / Dependencies / Evidence / Status / Related Files**：[BNS-ZERO](research/topics/examples/bounded_negative_square.md#bns-zero) 的完整残差恒等式、严格递增与极限反证；路径依赖 C100 的完整 \(J\) 纤维；`derived-checked`。来源 GX-053 仅提供图和 EB 线索，逐路径结论为本库推导。
- **Counterevidence / Scope**：正目标逆像为空，固定目标 EB 不提供两变量 MR；全图半阶乘真 EB 半阶既不产生收缩门，也不提供负输入 coverage 或正侧留域；有限合法路径越域不是发散的无限合法轨道。

## C102-v1 / SCD-INVERSE · 斜等距加紧正对角的锐逆像与非 rectangularity

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 \(H=\ell^2\)，完整全域单值线性 \(F=D+B\)，\(D(x_n)=(x_n/n)\)、\(B\) 为两两坐标的正交斜旋转。\(F\) 有界双射，\(\|F^{-1}\|=1,\|F\|=3/2,S=\{0\}\)；对全部 \(x,y\in H\)，\(d(x,F^{-1}(y))\le\|Fx-y\|\) 的系数全局及逐参考点局部锐。\(F\) 严格且极大单调、paramonotone，但强单调与正 cocoercivity 模均为零，并非 rectangular（存在 \(x\in\operatorname{dom}F,v\in\operatorname{ran}F\) 使 \(\inf_z\langle x-z,v-Fz\rangle=-\infty\)）。
- **Definitions / Dependencies / Evidence / Status / Related Files**：[SCD-INVERSE](research/topics/examples/skew_compact_diagonal.md#scd-inverse) 的全部块奇异值、完整逆图、双侧单调极大性证明和谐和级数反例；`derived-checked`。9/01 ZIP `work/c_gx053_065.md` GX-059 为对象来源；非 rectangularity 已用直接见证重证，无须旧稿 BWY 等价引文。
- **Counterevidence / Scope**：有限维截断的正 cocoercivity 不可对维数取统一下界；这是逆映射 MR，而非全对反射的严格收缩。外部先行性和同稿其它 GX 未审。

## C103-v1 / SCD-PROX · 完整近端严格收缩与锐非严格反射

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C102 同一完整图，对每个固定 \(\lambda>0\)，\(J_{\lambda F}\) 全空间单值且 \(\|J_{\lambda F}^m\|=(1+\lambda^2)^{-m/2}\) 对全部整数 \(m\ge0\)；全域合法轨道几何有限长趋零。同参数反射 \(R=2J-I\) 的全图 all-pairs 线性 RL 锐常数为 1，无界全图任何 \(\gamma<1\) 的有限 Hölder 常数失败。
- **Definitions / Dependencies / Evidence / Status / Related Files**：[SCD-PROX](research/topics/examples/skew_compact_diagonal.md#scd-prox) 的完整块逆、能量恒等式和高块锐性序列；依赖 C102 的统一奇异值下界；`derived-checked`，近端的精确收缩与全部幂为本库补出的结论。
- **Counterevidence / Scope**：全图反射模 \(L=1\) 不推出慢轨道；近端收缩不能倒推反射 \(L<1\)。改变原图为紧对角 \(D\) 或有限维块截断后是新对象。

## C104-v1 / VO-GAUGE · Volterra 完整图与无统一消失 gauge

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 \(H=L^2(0,1)\) 上全域完整 \(Vx(t)=\int_0^t x(s)\,ds\)，\(S=\{0\}\)、真残差 \(r_V(x)=\|Vx\|\)。其逆纤维恰是满足 \(y\in H^1,y(0)=0\) 时的 \(\{y'\}\)，否则为空；值域稠密非满。\(V\) 极大单调但非严格、非 paramonotone、非 rectangular。对任意 \(\eta>0\)、在 \([0,\eta)\) 上右极限为零的非负 gauge \(\psi\)，任意 \(C,\delta>0\)，存在 \(\|x\|<\delta,\|Vx\|<\eta\) 使 \(\|x\|>C\psi(\|Vx\|)\)；不要求 \(\psi\) 单调。
- **Dependencies / Evidence / Status / Related Files**：[VO-OBJECT/GRAPH](research/topics/examples/volterra_integration.md#vo-graph) 从积分分部、显式直线见证与高频余弦直接推导；来源 9/01 ZIP work/c_gx053_065.md GX-060，`derived-checked` 限本对象。无 BWY 外部调用。
- **Counterevidence / Scope**：这是固定零目标原算子真残差的统一邻域障碍；点态近端轨道仍可强收敛。稠密值域不等于满值域，伴随 GX-061 的其它观察未核。

## C105-v1 / VO-PROX · 全域近端强收敛而无统一有限步收缩

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C104 同一完整图，每个固定 \(\lambda>0\)，\(J_\lambda=(I+\lambda V)^{-1}\) 全 \(H\) 单值；对所有图点对，全图 all-pairs 线性 RL 锐 \(L=1\)，取等的零均值条件在图点差上。每个整数 \(k\ge1\) 有 \(\|J_\lambda^k\|_{\rm op}=1\)，每个非零输入逐次严格缩短，且对每个 \(p\in H\)，\(J_\lambda^kp\to0\) 强收敛。对近端**输入**步残差 \(g_\lambda(p)=\|p-J_\lambda p\|\)，任何右极限零 gauge 的统一局部 EB 同样失败。
- **Dependencies / Evidence / Status / Related Files**：[VO-PROX](research/topics/examples/volterra_integration.md#vo-prox) 用完整 Volterra 逆、能量式、高频方向及 \(\operatorname{ran}V\) 稠密证明；`derived-checked`。来源 GX-060 已给完整逆像、值域及显式 resolvent；全部有限幂与强收敛是本库新增推导。
- **Counterevidence / Scope**：严格逐点缩短不等于算子范数小于 1；强收敛不声称每条轨道有限长度。步残差与 C104 的原算子输出真残差是不同对象；无界全图的 \(\gamma<1\) RL 不从 \(L=1\) 继承。

## C106-v1 / NC-BRANCH · 负三次完整图碰撞与受限图块反射

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实全域完整 \(F(x)=-x^3\)，每个 \(\lambda>0\) 的完整 \(J_{\lambda F}(0)=\{0,\pm\lambda^{-1/2}\}\) 导致所有正指数全图零消失 all-pairs RL 失败。另固定 \(M>0,3\lambda M^2<1\)，只在 \(G_M=\{(x,-x^3):|x|\le M\}\) 上，Minty 输入覆盖 \(D_M=[-M(1-\lambda M^2),M(1-\lambda M^2)]\)，该图块单值且全对线性反射最小常数为 \((1+3\lambda M^2)/(1-3\lambda M^2)\)。
- **Dependencies / Evidence / Status / Related Files**：[NC-OBJECT/BRANCH](research/topics/examples/negative_cubic_branch.md#nc-branch) 的完整三根和两图点割线计算；来源 9/01 ZIP work/c_gx053_065.md GX-054，`derived-checked`。
- **Counterevidence / Scope**：图块的锐常数不授予完整 \(J\)；完整图的远根不因缩小输入球消失。参数 \(\lambda\) 和 \(M\) 固定在同一图块，旧卡其它二参数分类未核。

## C107-v1 / NC-REGULARITY · 负三次残差、逆像与受限路径

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C106 同一完整图 \(S=\{0\}\)，对全部 \(x\)，\(d(x,S)=r_F(x)^{1/3}\)，固定零目标最大局部幂 \(1/3\) 锐系数 1；完整逆像两目标 \(1/3\)-Hölder 锐全局与原点局部系数 \(2^{2/3}\)。对 C106 的**受限** \(T_M\) 的每个非零合法初值，逐步留在 \(D_M\) 的路径只能有限步延续；零路径恒零。
- **Dependencies / Evidence / Status / Related Files**：[NC-REGULARITY](research/topics/examples/negative_cubic_branch.md#nc-regularity) 的完整真残差、立方差和单调路径反证；`derived-checked`。残差与逆像模也可由已核 EX03 的 \(x^3\) 经符号变换得出；路径和完整图碰撞需另算。
- **Counterevidence / Scope**：受限路径越域不表示完整多值近端每条路径都如此；固定目标系数 1 不等于两目标系数。全图碰撞、局部图块估计与零目标 EB 不能拼成完整 PPA 收敛证书。

## C108-v1 / IP-MINTY · 孤立零图点与极点支的全步长完整纤维

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实数空间、固定 \(0<\varepsilon<1\)，完整关系 \(F(0)=\{0\},F(x)=\{-1/x\}\) 对 \(0<x\le\varepsilon\)、其余为空；定义域 \([0,\varepsilon]\) 连通、完整图闭但零图点孤立。对每个固定 \(\lambda>0\)，\(D_\lambda=(-\infty,\varepsilon-\lambda/\varepsilon]\cup\{0\}\)；当 \(\lambda\le\varepsilon^2\) 时 \(J_{\lambda F}(0)=\{0,\sqrt\lambda\}\)，故任何零消失全对 RL 失败；当 \(\lambda>\varepsilon^2\) 时完整 J 单值、全图锐线性 RL 为 \((\lambda+\varepsilon^2)/(\lambda-\varepsilon^2)\)，锐近端 Lipschitz 模为 \(\varepsilon^2/(\lambda-\varepsilon^2)\)，全图次线性幂 RL 仍失败。
- **Dependencies / Evidence / Status / Related Files**：[IP-MINTY](research/topics/examples/isolated_pole_relation.md#ip-minty) 从全部图点与完整纤维重算，`derived-checked`；来源 9/01 ZIP `work/c_gx053_065.md` GX-055 及同包 `work/b_monotonicity_gaps.md` MGB-05，仅对象和旧断言作线索。
- **Counterevidence / Scope**：\(\lambda<\varepsilon^2\) 有零输入球却同输入碰撞；\(\lambda>\varepsilon^2\) 全对线性模成立却无零输入球。历史“disconnected domain”应为“disconnected graph”；仅限输入的局部 hypomonotonicity 失败与乘积图窗仅有零点的真空条件不得混同。历史命名与先行性未核。

## C109-v1 / IP-RESIDUAL-PATH · 残差逃逸、空目标纤维与路径留域

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C108 的同一完整关系和 \(S=\{0\}\)，每个 \(q>0\)、全部 \(0<x\le\varepsilon\) 有 \(d(x,S)/r_F(x)^q=x^{q+1}\)；固定零目标的每个正幂局部 EB 系数下确界为 0，非退化输入窗不以系数 0 取到。每个充分小的非零目标的完整逆像为空，所以两变量 MR/SMR 均失败。对**每个** \(\lambda>0\) 及每条完整 J 的逐步合法路径，唯一无限路径是恒零路径；任一非零初值及从零迟后选极点支的路径均有限步离自然输入域。
- **Dependencies / Evidence / Status / Related Files**：[IP-RESIDUAL/PATH](research/topics/examples/isolated_pole_relation.md#ip-residual) 由完整残差、逆纤维和逐步输入递增预算证明，依赖 C108 的全部 J 纤维；`derived-checked`。来源 GX-055 只报告固定目标与 LT 观察，路径分类为本库新增推导。
- **Counterevidence / Scope**：\(\lambda>2\varepsilon^2\) 时完整 J 在其自然域锐 Lipschitz 模小于 1，仍非自然域自映射；输出小残差窗口仅见零图点，不能借固定目标零系数断言附近非零轨道收敛。域外 \(+\infty\) 不作 \(0\cdot\infty\) 运算。

## C110-v1 / RS-FIBERS-RL · 算术阶梯的完整近端纤维和锐全对门槛

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实完整关系 \(F_\delta(0)=\{0\}\)、\(F_\delta(x)=\{\operatorname{sgn}(x)c(x)\}\) 对 \(0<|x|<\delta<1/2\)，\(c=1\) 于有理数、\(c=2\) 于无理数，其余点空。对**每个固定** \(\lambda>0\)，完整 \(J\) 的四个非零输入簇和每个纤维由 (RS4)–(RS6) 给出，\(D_\lambda\cap(-\lambda,\lambda)=\{0\}\)。全图全对线性 RL 当且仅当 \(\lambda>\delta\)，锐 \(L=(\lambda+\delta)/(\lambda-\delta)\)；\(0<\lambda\le\delta\) 时任何零消失反射模失败。若 \(0<\lambda<\delta\)，有理步长的完整 J 单值但不连续，无理步长在重叠窗有精确多值碰撞；临界步长单值却有不兼容的遗漏端点极限。
- **Dependencies / Evidence / Status / Related Files**：[RS-OBJECT/FIBERS/RL](research/topics/examples/rational_irrational_staircase.md#gx056-fibers) 以四个算术水平及全部图点对直接证明，`derived-checked`；来源 9/01 ZIP `work/c_gx053_065.md` GX-056，同字节早期 checkpoint 仅是重复证据。历史较松的 \((1+2\delta)/(1-2\delta)\) 是非锐安全界。
- **Counterevidence / Scope**：图在零图点附近的**输入输出联合窗**局部闭、在非零图点不局部闭；这不提供零点输入球或近端连续性。次线性全图常数只由有界尺度继承，未核锐值；历史命名和外部先行性未核。

## C111-v1 / RS-RESIDUAL-PATH · 阶梯的真残差与所有合法路径

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C110 同一完整图，\(S=\{0\}\)，任意 \(q>0\) 与 \(0<\eta\le\delta\)，在 \(|x|<\eta\) 的固定零目标真残差 EB 最小系数是 \(\eta\)，故缩窗下确界 0；邻近非零目标的完整逆像为空，MR/SMR 失败。对每个 \(\lambda>0\)，完整近端**最小步残差** \(s_\lambda(p)=d(p,J_{\lambda F}(p))\) 在自然域上给锐 \(|p|\le(1+\delta/\lambda)s_\lambda(p)\)。每条从非零合法输入出发的完整 J 路径都有限步终止、不能达到零；从零唯一无限路径恒零；\(\lambda\ge\delta\) 时每个非零输入恰有一步。
- **Dependencies / Evidence / Status / Related Files**：[RS-RESIDUAL/PATH](research/topics/examples/rational_irrational_staircase.md#gx056-residual) 的全纤维、取等序列及每步位移 \(\ge\lambda\) 证明；依赖 C110 的完整纤维，`derived-checked`。原稿 GX-056 的真残差与全对模为线索，最小步锐系数和算术路径边界由本库推导。
- **Counterevidence / Scope**：真残差跳跃的零系数下确界与 C78/C79 的绝对值次梯度相似，但此图缺完整目标纤维与近零输入覆盖；步残差、MR 和路径不能由残差跳跃类比转授。端点 \(\pm\delta\) 未包含，C110 已证明非零图点不局部闭；历史二参数区仍待核。

## C112-v1 / PS-ZERO-PATH · 负平方与阶梯完整乘积的残差和路径

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 Euclidean \(\mathbb R^2\)，固定 \(0<\delta<1/2\)，完整乘积 \(F=A\times B\)，其中 \(A(x)=-x^2\) 于 \([0,1/2]\)、\(B\) 是 C110 的有理/无理阶梯，域外均为空，\(S=\{(0,0)\}\)。对**所有**有限真残差点，\(d(z,S)\le r_F(z)^{1/2}\)，系数 1 全域与局部锐，最大局部幂 \(1/2\)；任意小正第一目标或非零小第二目标逆纤维为空，故双变量 MR/SMR 失败。对每个固定 \(\lambda>0\) 的完整乘积 \(J_{\lambda F}=J_{\lambda A}\times J_{\lambda B}\)，任意非零逐步合法初值的每条路径只可有限步延续；唯一无限路径恒零。
- **Dependencies / Evidence / Status / Related Files**：[PS-OBJECT/ZERO-EB/RESOLVENT/PATH](research/topics/examples/product_splice.md#gx057-object) 的完整逆纤维、分量自然域和两坐标位移直接证明，依赖 C100/C101 与 C110/C111 的分量身份但逐乘积验证；`derived-checked`。来源 9/01 ZIP `work/c_gx053_065.md` GX-057，路径全分类及全域 EB 量词由本库加证。
- **Counterevidence / Scope**：全域半阶零目标 EB 的锐点在零轴；临界全对半阶锐点在第一坐标右端，不能拼作零点收敛。目标逆像缺失与完整自然输入留域是独立障碍，域外残差无穷不作字面零系数乘法。

## C113-v1 / PS-RL-PHASE · 完整乘积的全图步长相变

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C112 同一完整图，对每个固定 \(\lambda>0\)、**全部**两图点：若 \(0<\lambda\le\delta\)，阶梯给输入差趋零而反射差不消失；若 \(\delta<\lambda<1\)，全图线性 RL 的锐 \(L^*=\max\{(1+\lambda)/(1-\lambda),(\lambda+\delta)/(\lambda-\delta)\}\)；\(\lambda=1\) 的最大全图幂次为 \(1/2\)；\(\lambda>1\) 第一坐标给精确 Minty 碰撞。全图无有限 hypo 或 cohypomonotone 模，分别由不同坐标见证；自然域和全部 J 纤维为两分量的直积。
- **Dependencies / Evidence / Status / Related Files**：[PS-RESOLVENT/RL-PHASE](research/topics/examples/product_splice.md#gx057-rl-phase) 的全部图点对、Euclidean 直积与取等分量证明，`derived-checked`；C100/C110 是分量证书，乘积量词另证。
- **Counterevidence / Scope**：\(\lambda<\delta\) 有理时 J 可以单值而全对消失模仍失败；\(\lambda>1\) 的乘积远支不可因只看临界局部图窗而删除。两个图几何失败的机制各在不同坐标，不能说一个常数对整个乘积成立。

## C114-v1 / PS-SHARP-WINDOW · 临界全乘积锐常数与图邻域分离

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C112 同一完整图，固定 \(\lambda=1\)。**完整乘积全部图点对**的锐半阶系数 \(L_{1,1/2}^{\rm full}\) 满足 [PS-P15](research/topics/examples/product_splice.md#gx057-sharp-product-half) 的精确单变量最大式，且 \(L_{1,1/2}^{\rm full}\ge\sqrt{265/(4\sqrt{257})}>2\)。在临界图点 \(((1/2,0),(-1/4,0))\) 同时限制第二**输出**到 \(|v_2|<1\) 的非退化端点图窗，锐半阶系数为 2；只限制第一输入到任意固定端点窗且第二输入到任意小非零窗、保留全部输出时，锐系数严格大于 2，但双窗缩小的系数下确界仍为 2。
- **Dependencies / Evidence / Status / Related Files**：[PS-SHARP/WINDOW](research/topics/examples/product_splice.md#gx057-sharp-product-half) 的第二坐标类型分解、第一坐标端点优化与全部取等极限；精确 \(H_\delta\) 驻点多项式、阈值由符号微分另核，`derived-checked`。来源 GX-057 原稿仅给图邻域系数 2 和未定的完整乘积模，(P15) 是本库新增推导。
- **Counterevidence / Scope**：固定图窗的 2 不是仅限输入窗或完整乘积的常数；曲线尖锐处位于右端点，不是零点局部证书。不能用分量锐常数的最大值替换乘积半阶模，也不能从固定目标半阶 EB 推断路径存在。

## C115-v1 / SSQ-FULL-CERT · 完整二值半代数关系的共同局部收敛证书

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 \(\mathbb R^3\)，固定 \(\lambda=1\)，完整闭图二值关系 \(F\) 如 [SS-Q1](research/canonical/solution_selection_rates.md#ss-quadratic-object)，\(S=\mathbb R^2\times\{0\}\)。对**全部**输入，完整 \(J_F=T\) 是单值全域，具体为 (SS-Q3)。对每个固定 \(0<R_0<1\) 和每个有限比较尺度 \(D>0\)，图块 \(0\le y\le R_0^2\) 的**任意两**图点在输入对距离 \(\le D\) 有 \(\gamma=1/2,L=2\sqrt2+(1+4R_0)\sqrt D\) 的全对 RL；所有实际输出的全纤维真残差满足 \(d(u,S)=y\le r_F(u)^4\)。同一个预先固定 \(R=\min\{R_0/2,8/(2\sqrt2+2+4R_0)^4\}\) 给 \(\kappa=1/2\) 严格兼容、完整 coverage、零锚和不变 collar。对全部初值 \(|r_0|<1\) 轨道有限长收敛；在每个 \(V_{R_0}\) 上有对全部初值与 \(k\ge0\) 一致的 \(M_0e^{-c_0 2^k}\) 点尾。
- **Dependencies / Evidence / Status / Related Files**：[SSQ-FULL/CERT/TAIL](research/canonical/solution_selection_rates.md#ss-quadratic-full) 从全部两值图纤维反演、负输入、接点、全对图块、真正最小残差和固定半径逐项证明；`derived-checked`，另经独立逆向审查。来源 SS1 修订 ZIP `research_note.md` 定理 4；旧 S03 仅为摘要。C08 的抽象 SS-TRANSFER 对该共同尾可调用，但模型身份另立。
- **Counterevidence / Scope**：\(|r_0|\ge1\) 不收敛；逐轨道 Q-二次起点可依初值而变，统一的是超几何点尾。图块全对比较尺度 \(D\)、输出 collar 和完整 J 纤维排他不能省，改变参数/关系或仅选一支是新命题。先行性未核。

## C116-v1 / SSQ-BAD-SELECTION · Q-二次点误差与最优根对数选择模并存

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：对 C115 同一完整 \(T\)，每个非驻定收敛初值的实际点误差满足 \(\lim_{k\to\infty}e_{k+1}/e_k^2=1\) 若 \(p_0\le0\)，若 \(p_0>0\) 则为 \(1/\sqrt2\)；这是**每条轨道**的渐近，而非共同进入时间。固定任意足够小 \(0<r_0\le R\) 后，比较 \(x_0=(0,0,r_0),x_\varepsilon=(0,\varepsilon,r_0)\)，\(\varepsilon\downarrow0\)，其极限差有匹配的 \(e^{-C\sqrt{\log(1/\varepsilon)}}\) 上下阶，排除在原点任意邻域的正阶两点 Hölder，亦排除比根对数指数 \(1/2\) 更大的统一伸缩指数。每个有限步 \(T^k\) 半代数，但 \(\Pi\) 在原点任意开邻域非半代数。
- **Dependencies / Evidence / Status / Related Files**：[SSQ-TAIL/SELECTION/NONSEMIALGEBRAIC](research/canonical/solution_selection_rates.md#ss-quadratic-tail) 的饱和时刻上下界、分离的 overshoot 与尾项、逐轨道极限以及代数多项式反证；依赖 C115 的完整对象和共同局部证书，`derived-checked`，另经独立逆向审查。来源 SS1 定理 4 和 §5.1；非半代数的证明不依赖外部增长引理。
- **Counterevidence / Scope**：比较轨道使用相同固定 collar 的 \(r_0\le R\)，不能事后令半径依 \(\varepsilon\) 改变；坏的是**两初值**选择，不否定相对单个固定解点的 anchored calmness，也不否定别的结构条件下的好极限映射。外部新颖性未核；SS1 定理 2/3 已分别另立 C137/C138，359–448 行一般几何族另立 C139，§5.2 三角动力学条件另立 C140；另一超线性族见 C141 的限定 `derived-checked` 版本。

## C117-v2 / SS-GROWTH · 双支 signed-Schur 的表示图证书

- **Status**：`derived-checked`。前驱身份范围见 [SS-VERSION-RECOVERY](research/canonical/signed_schur_growth.md#ss-version-recovery)：来源 S19-SG-v1 不等于未恢复的 C117–C119-v1 卡；当前只调用本 v2。

- **Exact Statement / Objects / Domain / Quantifiers**：有限维 \(\mathbb R^{n-1}\times\mathbb R\)、固定 \(\lambda>0\) 和两支 \(g_\pm:Q=\overline B_R\times[0,T]\to\operatorname{gph}F\)。参数化在 \(Q\) 的开邻域有 \(C^1\) 延拓，**图包含只在 \(Q\) 上**。同一 \(Q\) 的 (SS-2)–(SS-5) 公共接缝、强单调切向导数、Schur 导数界、相反定向凸严格增长及 \(0<r<\mu R-HT\) 合取，给每个 \(z\in B_r,t\in[0,T]\) 的唯一内点切向反演、开输入领圈 (SS-9) coverage、所表示图在切向输入球内无碰撞；该范围**任意两**图点的反射差由 (SS-10)/(SS-11) 控制，模在零点消失。
- **Dependencies / Evidence / Status**：[SS-OBJECT/GROWTH](research/canonical/signed_schur_growth.md#ss-object) 的 Brouwer 内点、隐函数、同支凸增量、跨支预算和剪切恒等式经独立重构与敌对审查，`derived-checked`。仅在另外核 (SS-13) 后于领圈 \(U\) 识别所需完整 \(J_{\lambda F}\)；该条件不转移 \(U\) 外的图点，也不产生真残差 EB、零锚、兼容或留域。
- **版本与反证边界**：S19 原 `thm:signed-schur-growth` 若把“邻域内取图值”作字面强假设，抽象定理可由本版推出，但其平方根原生例在负参数的延拓不满足该读法；本版不默改原命题。失去相反定向、同支增长凸性、切向一致性或完整纤维排他各有[独立反例](research/canonical/signed_schur_growth.md#ss-attacks)。

## C118-v2 / SS-POWER-JET · 幂次预算、匹配改善及最优指数门

- **Status**：`derived-checked`。前驱身份范围见 [SS-VERSION-RECOVERY](research/canonical/signed_schur_growth.md#ss-version-recovery)：来源 S19-SG-v1 不等于未恢复的 C117–C119-v1 卡；当前只调用本 v2。

- **Exact Statement / Objects / Domain / Quantifiers**：在 C117 的**切向输入均位于 \(B_r\)** 的表示图块上，若 \(h_\sigma=c_\sigma t^p,p>1\)，输入直径 \(\le D\) 的全对指数为 \(1/p\)，有效常数是 (SS-24)/(SS-25)；\(p=1\) 有 (SS-26)。不同幂次只比较预算 (SS-27)，不能伪造更高阶 Schur 导数。若同一个修正切向输入 \(z\) 的两支输出匹配至 \(Et^p\)，以共同增长下界 \(c=\min\{c_+,c_-\}>0\) 调用 (SS-30)/(SS-31) 改善跨支预算。若另有固定 \(z_0\) 的 \(O(t^p)\) 输入法向上界与 \(\Omega(t)\) 输出差下界，\(1/p\) 是最大全对指数；\(p>1\) 时已识别的单值近端在接缝不 calm。
- **Dependencies / Evidence / Status**：[SS-POWER/JET/EXPONENT](research/canonical/signed_schur_growth.md#ss-power) 的二维 Hölder 预算、同修正坐标匹配和双边弧证据独立证明，`derived-checked`；\(K_z=0\) 的主系数有 (SS-28) 取等。原参数的同位导数比较、单点 Taylor 阶或仅 (SS-5) 均不足替代附加门。

## C119-v2 / SS-SQRT · 完整平方根图的证书与锐性

- **Status**：`derived-checked`。前驱身份范围见 [SS-VERSION-RECOVERY](research/canonical/signed_schur_growth.md#ss-version-recovery)：来源 S19-SG-v1 不等于未恢复的 C117–C119-v1 卡；当前只调用本 v2。

- **Exact Statement / Objects / Domain / Quantifiers**：固定完整 (SS-33)、\(\lambda=1\)、\(0<r<R-2T\)，在 \(U=(-r,r)\times(-4T^2,4T^2)\) 的全部完整图纤维等于两支 (SS-34)；给 \(\gamma=1/2\) 的 (SS-38) 和同输入匹配后 (SS-39) 常数，收缩领圈的最优渐近系数 2 与最大指数 \(1/2\)。同一完整关系零集 \(S=\mathbb R\times\{0\}\) 的真实**最小**残差另给锐系数 \(1/4\) 的平方界 (SS-41)。
- **Dependencies / Evidence / Status**：[SS-SQUARE-ROOT](research/canonical/signed_schur_growth.md#ss-square-root) 对法向输入 \(\pm4y\) 的全部纤维反演和两支图值最小化独立证明，`derived-checked`；固定领圈的 (SS-38)/(SS-39) 不声称是其最小常数。图包含仅在 \(t\ge0\)；不能作为 S19 可能的“延拓邻域也须在图内”读法的实例，不能由此直接宣布 PPA 收敛或先行性。

## C120-v1 / VAD-GRAPH · 伴随 Volterra 的方向端点与等距身份

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 \(H=L^2(0,1)\) 全域完整 \(V^*x(t)=\int_t^1x(s)ds\)，与 C104 的 \(V\) 通过 \(Uf(t)=f(1-t)\) 满足 \(V^*=UVU\)。全部逆纤维仅在 \(y\in H^1,y(1)=0\) 为 \(\{-y'\}\)，否则为空。完整图极大单调但非严格、非 paramonotone、非 rectangular；任意局部球及残差窗内，固定零目标的任何右极限零 gauge 真残差 EB 失败。
- **Dependencies / Evidence / Status / Related Files**：[AV-OBJECT/GRAPH](research/topics/examples/adjoint_volterra.md#av-object) 的换元、积分分部、直接 rectangular 见证和高频余弦；来源 Z07 GX-061 与 CCA-M10 分别作为方向观察及共轭核对，`derived-checked`。C104 是同一等距例型，不能作独立相位样本重复计数。
- **Counterevidence / Scope**：空逆纤维还否定目标邻域的两变量 MR；旧卡“全部标签通过”不是对未拆属性、外部 BWY 归属或先行性的验收。

## C121-v1 / VAD-PROX · 完整伴随近端的点态强收敛与统一障碍

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C120 同一完整图，每个固定 \(\lambda>0\) 的全域单值 \(J_{\lambda V^*}=UJ_{\lambda V}U\) 有显式反向积分核；全图全对线性 RL 锐 \(L=1\)，无界全图任意 \(0<\gamma<1\) 不存在有限常数。每个有限整数 \(k\ge1\) 的算子范数 \(\|J^k\|=1\)，但每个固定 \(p\) 的 \(J^kp\to0\) 强收敛，且每个非零输入单步范数严格缩短。近端输入步残差的任意局部右极限零 gauge EB 也失败。
- **Dependencies / Evidence / Status / Related Files**：[AV-PROX](research/topics/examples/adjoint_volterra.md#av-prox) 先核全部完整纤维与核公式，再用酉共轭传递 C105 的能量、稠密值域及高频证明；`derived-checked`。来源 GX-061 只给近端公式及 RL 标签，有限幂与点态极限属本库推导。
- **Counterevidence / Scope**：全图常数的取等条件在**图点差**零均值，不能改写成任意输入差。原算子真残差、近端输入步残差及逐点收敛是三个不同断言；有界输入窗的次线性继承不等于无界全图证书。

## C122-v1 / PR-CAYLEY · 完整旋转族的唯一奇点与锐全对尺度

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：实 \(\mathbb R^2\) 全域完整 \(Q_\theta=\cos\theta I+\sin\theta K\)，\(-\pi\le\theta\le\pi,\lambda>0\)。令 \(\Delta=1+2\lambda\cos\theta+\lambda^2,N=1-2\lambda\cos\theta+\lambda^2\)。唯一奇点 \(Q=-I,\lambda=1\) 时自然域 \(\{0\}\)，完整 \(J(0)=\mathbb R^2\)；否则 \(J,R\) 全域线性单值，\(\|J\|=\Delta^{-1/2}\)，反射锐线性模 \(\ell=\sqrt{N/\Delta}\)。在任意 Minty 输入对距不超过 \(R>0\) 的窗内，\(0<\gamma\le1\) 的最小全对常数为 \(\ell R^{1-\gamma}\)；无界全图次线性失败，唯 \(Q=I,\lambda=1\) 的零反射例外。
- **Dependencies / Evidence / Status / Related Files**：[PR-CAYLEY](research/topics/examples/planar_rotation_family.md#pr-cayley) 用矩阵逆、所有可实现差距与完整奇点纤维直接证明，`derived-checked`；来源 Z07 旋转族第 765–839 行。D02 尺度是输入对距，不是球半径。
- **Counterevidence / Scope**：仅在 \(\Delta>0\) 的同参数 signed LT 锐数为 \(-\lambda\cos\theta/\Delta\)，若只允许非负 \(\tau\) 则为 \(\max\{0,-\lambda\cos\theta/\Delta\}\)；仅在 \(\cos\theta\ge0\) 时截为 0。不能把二者写成同一个常数。Voisei v2 Example43的归属/编号已核，见[LIT-VOISEI-2024](research/LITERATURE.md#lit-voisei-2024)；优先性仍未审。

## C123-v1 / PR-CYCLIC · 循环阶与两张取样角的可保留结论

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C122 同一完整图，所有整数 \(n\ge2\) 的精确循环门是 \(|\theta|\le\pi/n\iff\cos\theta\ge\cos(\pi/n)\)，成立时图也极大 \(n\)-循环单调。GX-062 \(Q_{\pi/3}\) 最高 3 阶、GX-063 \(Q_{\pi/4}\) 最高 4 阶；正强单调及 cocoercivity 系数分别 \(1/2,1/\sqrt2\)，完整逆像的普通 MR/MSR/SMR/SMSR 系数均为 1。两角 \(\ell<1\)，全部近端路径由完整全域相似变换给精确有限长度。
- **Dependencies / Evidence / Status / Related Files**：[PR-CYCLIC/TWO-ANGLES](research/topics/examples/planar_rotation_family.md#pr-cyclic) 的离散 Fourier 模对角化、全图极大性双侧扰动和完整逆纤维；`derived-checked`。来源 Z07 第 840–908 行分别核入，外部 Voisei 归属不承重。
- **Counterevidence / Scope**：来源 GX-063 第 902–905 行“循环阶不能由标量强单调模还原”在此旋转族内被 (PR7) **修正**：\(\mu=\cos\theta\) 正好决定所有循环阶。两角只证明相同逆像条件数 1 不决定循环阶；不把该族内关系推广为一般算子定理。

## C124-v1 / SB-GEOMETRY · 斜旋转法锥的图几何

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：在实 \(\mathbb R^2\) 取单位闭盘 \(B\)、\(K=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\) 和完整 \(F=K+N_B\)。对**全部**图点对，(SB6) 的内积非负；图单调、rectangular 而非 paramonotone，正强单调及正 cocoercivity 系数均不存在。Rectangular 的固定点量词是 \(\xi\in\operatorname{dom}F=B,\eta\in\operatorname{ran}F\)，不得扩到盘外 \(\xi\)。
- **Definitions / Dependencies / Evidence / Status / Related Files**：[SB-GEOMETRY](research/topics/examples/skew_ball_inverse.md#sb-geometry) 从全部法向射线计算；极大性是另一个依赖 C125 全域 Minty 输入的结论。`derived-checked`，来源 Z07 `work/c_gx053_065.md` GX-058 第 476–504 行；BWY arXiv v1 Proposition 3.4 / Example 3.5（作者站稿 Proposition 3.6 / Example 3.7）的对象归属已按 [LIT-BWY-2012](research/LITERATURE.md#lit-bwy-2012) 核验，优先权另核。
- **Counterevidence / Scope**：两个不同内点配对为零，排除正系数；内点 \((x,Kx),(0,0)\) 的交叉图点 \((x,0)\) 不存在。Rectangular、paramonotone、C98/C99 的逆像模与 C125 的反射模是不同性质，不从任一标签无条件转授另一项。

## C125-v1 / SB-PROX · 全部近端纤维和锐全图 RL

- **Status**：`derived-checked`。

- **Exact Statement / Objects / Domain / Quantifiers**：C124 的**同一个完整** \(F\)，任意固定 \(\lambda>0\) 与每个 \(p\in\mathbb R^2\)。完整 \(J_{\lambda F}(p)\) 单值满域且由 (SB8) 的内/外两式给出，分界 \(\|p\|=\sqrt{1+\lambda^2}\) 连续一致；结合 C124 单调性，\(F\) 极大单调。对全部输入对 \(R_\lambda=2J_{\lambda F}-I\) 非扩张，锐全图 \(\mathrm{RL}(\lambda,1,1)\) 常数 1；无界全图不存在有限的 \(0<\gamma<1\) 幂常数。
- **Definitions / Dependencies / Evidence / Status / Related Files**：[SB-PROX](research/topics/examples/skew_ball_inverse.md#sb-prox) 逐法向参数反演、完整纤维及 (SB9) 全对恒等式，`derived-checked`；来源同一 GX-058 第 520–537 行。C124 的图单调性用于反射上界，两个内点给常数 1 取等。
- **Counterevidence / Scope**：\(\|Jp\|\le1\) 且 \(R_\lambda p=2Jp-p\) 给无界尺度障碍；有界输入对距窗口可另继承小指数。完整反射 RL 不代表 C98/C99 的 MR，亦不提供小于 1 的统一反射因子或一般 RLEB 动力证书。

<a id="c126"></a>
## C126-v1 / MR-MOMENT · 全有限支撑律的精确矩门

- **Status**：`derived-checked`，本页的两点必要性与矩单调性充分性已重构；外部先行性未核。
- **Exact Statement / Objects / Domain / Quantifiers**：在可测状态集 \(E\) 上取有限非负函数 \(e,c\)、\(1\le p,r<\infty,q>0,0\le K<\infty\)，存在共同零点 \(s\) 和 \(e(a),c(a)>0\) 的 excursion。对**每个有限支撑概率律** \(\mu\)，\(\|e\|_{L^p(\mu)}\le K\|c\|_{L^r(\mu)}^q\) 当且仅当对**每个** \(x\in E\) 有 \(e(x)\le Kc(x)^q\) 且 \(pq\le r\)。Markov 推论另以 \(\mathbb R^d\) 为核和 \(W_p\) 的母空间，固定闭目标支持 \(S\subset\mathbb R^d\)、**全部**目标不变律组成的 \(\mathcal I\subset\mathscr P_p(S)\)、\(\pi\in\mathcal I\) 且 \(\pi P=\pi\)、在 \(\pi\) 上消失的状态残差及某 \(a\in\mathbb R^d\) 的 \(P(a,\cdot)\) 远离 \(S\) 的正 \(p\) 阶矩；若在 \(\mathscr P_p(\mathbb R^d)\) 中 \(\pi\) 的**整个** \(W_p\) 邻域（含 \((1-\varepsilon)\pi+\varepsilon\delta_a\)）有 \(d_{W_p}(\mu P,\mathcal I)\le K\|c\|_{L^r(\mu)}^q\)，则 \(pq\le r\) 必要。仅在 \(\mathscr P_p(S)\) 相对邻域调用须另有 \(a\in S\)。
- **Definitions / Dependencies / Evidence**：[MR-MOMENT](research/topics/random_markov/moment_recoupling.md#mr-moment) 给 Dirac、两点小质量律、矩单调性和 Markov 更新混合的证明。原 CM-M Proposition M 是线索；计算或近端算法身份不是证明前提。
- **Counterevidence / Scope**：没有共同零点或正输出 excursion 时，必要性不由此证明；在 law-space 中换成不在平稳律消失的物理残差也改变命题。\(r\ge pq\) 只消除这项矩障碍，不自动构造原生合法耦合或点态证书。

<a id="c127"></a>
## C127-v1 / MR-RECOUP · 同一近极小 OT 对上的条件线性 EB

- **Status**：`derived-checked`，同一耦合上的 Hilbert 三角式已重构；原生模型验证回耦损失仍是开放门。
- **Exact Statement / Objects / Domain / Quantifiers**：紧欧氏状态集、联合可测随机自映射及指定**同一随机表示**，非空不变律集 \(\mathcal I\)，\(d(\mu)=d_{W_2}(\mu,\mathcal I)\)。在指定律类 \(\mathcal A\) 上对所有 \(\mu\) 有 \(d(\mu P)\le c_0d(\mu)\)、\(0\le c_0<1\)。对每个 \(\mu\) 存在原 \(\Psi\) 定义所要求的输入 \(W_2\)-最优、同噪声对 \((\pi_j,\eta_j)\)，\(D_{\eta_j}\to\Psi(\mu)\)，且同一个 \(0\le\chi<\infty\) 满足 \(\Delta_{\eta_j}=A_{\eta_j}-d(\mu P)^2\le\chi D_{\eta_j}^2\)。则对所有该律类的 \(\mu\)，\(d(\mu)\le(1+\sqrt\chi)\Psi(\mu)/(1-c_0)\)。同一对上的另一门 \(\Delta_{\eta_j}\le\sigma^2d(\mu)^2,c_0^2+\sigma^2<1\) 给系数 \(1/(1-\sqrt{c_0^2+\sigma^2})\)。
- **Definitions / Dependencies / Evidence**：[MR-RECOUP](research/topics/random_markov/moment_recoupling.md#mr-recoupling) 明确定义 \(D_\eta,A_\eta,\Delta_\eta\) 与 \(\Psi\)，逐对使用 Minkowski 和输出边缘 \(\pi P=\pi\)，再在同一 inf 的近极小序列取极限。
- **Counterevidence / Scope**：独立于 C126 的矩门；收缩单独不控制回耦损失，非最优输入运输及条件刷新残差 \(\mathcal R\) 不能替换 \(D_\eta\)。系数仅充分，原生随机多值近端的合法耦合尚未验收。

<a id="c128"></a>
## C128-v1 / SC-BAIRE · σ-紧度量空间的 Baire 诊断

- **Status**：`derived-checked`；双向证明由规范定义重构，并经独立逆向检查。
- **Exact Statement / Objects / Domain / Quantifiers**：任意度量空间 \(Z=\bigcup_{n\ge1}K_n\)，其中每个 \(K_n\) 紧，不要求嵌套。\(Z\) 为 Baire 当且仅当 \(\bigcup_n\operatorname{Int}_ZK_n\) 在 \(Z\) 中稠密。
- **Dependencies / Evidence**：[SC-OBJECT/PROOF](research/canonical/sigma_compact_baire.md#sc-proof) 证明每个紧层闭、正向的开 Baire 子空间反证、反向的稠密开局部紧 Baire 子空间转移；不需历史审计的未写前提。
- **Counterevidence / Scope**：该式只测试**已给定且覆盖同一 \(Z\)** 的紧层；不证明算子类实际有这类覆盖，也不证明 \(\Phi\) 保纲、目标类余稠或总体规模比较。单个局部紧点不必落在某个指定 \(K_n\) 的内部。

<a id="c129"></a>
## C129-v1 / CR-BINARY · 守恒边缘二进制刷新残差的锐界

- **Status**：`derived-checked`；条件耦合、五项等价、退化端点与最佳系数已从规范证明独立逆向核验，外部先行性未核。
- **Exact Statement / Objects / Domain / Quantifiers**：固定标准 Borel \(U\) 与概率边缘 \(\nu\)、有限 \(X=\{0,1\}^m\)、可测 \(b_i(u)\in(0,1),p_i(u)>0\) 且 \(\sum_i p_i(u)\le1\) 几乎处处。对**全部**固定边缘律 \(\mathscr M_\nu\) 使用仅在同一 \(u\) 内运输的 \(\mathsf W_\nu\)、条件重抽样残差 \(\mathcal R\) 和目标 \(\pi_\nu(du,dx)=\nu(du)\beta_u(dx)\)，其中 \(\beta_u=\bigotimes_i\operatorname{Bern}(b_i(u))\)。\(a_*={\rm ess\,inf}_u\min_i p_i(u)\)。精确零集为 \(\{\pi_\nu\}\)，它是此律类唯一不变律。\(a_*>0\) 当且仅当该整个律类有统一线性 \(\mathsf W_\nu/\mathcal R\) EB，当且仅当对目标距离有统一一步严格收缩、某固定块严格收缩或统一相对几何率。最佳 EB 系数 \(a_*^{-1/2}\)，每个固定 \(k\ge1\) 的最佳到目标因子 \((1-a_*)^{k/2}\)，在任意正半径完整目标球仍锐。若 \(a_*=0\)，每条律仍趋于目标，但每个固定 \(k\) 最坏因子为 1。
- **Definitions / Dependencies / Evidence**：[CR1–CR5](research/topics/random_markov/conditional_refresh.md#cr-binary-object) 固定对象、条件 Bernoulli 顺序耦合、条件 Jensen、同步更新及单坐标扰动见证；来源 CM-M Theorem 6 有证明文本，本页不以其 PASS 标签为证据。
- **Counterevidence / Objections / Scope**：\(\mathcal R\ne\Psi\)；结论不赋予不同随机表示、普通联合 \(W_2\) 的最佳必要模，或任意两律间的 Lipschitz 因子。审查限固定边缘的有限 bit 对象，未核外部文献优先性。

<a id="c130"></a>
## C130-v1 / CR-GAUSSIAN · Gaussian Gibbs 条件残差的锐界

- **Status**：`derived-checked`；保持同一两边缘的条件耦合、有限性、谱不等式和局部锐性经独立逆向核验。
- **Exact Statement / Objects / Domain / Quantifiers**：\(Q\in\mathbb R^{m\times m}\) 对称正定、\(\beta=N(m_0,Q^{-1})\)、\(p_i>0,\sum_i p_i=1\)、\(D=\operatorname{diag}(p_i/Q_{ii})\)、\(\zeta=\lambda_{\min}(Q^{1/2}DQ^{1/2})>0\)。每步按 \(p_i\) 使用 \(\beta\) 的全条件律刷新第 \(i\) 位；对**全部有限二阶矩律** \(\mu\)，以 \(Q\) 二次成本的 \(W_{2,Q}\) 和一维条件运输定义的 \(\mathcal R_Q\) 有 \(W_{2,Q}(\mu,\beta)\le\zeta^{-1/2}\mathcal R_Q(\mu)\)、\(W_{2,Q}(\mu P,\beta)\le\sqrt{1-\zeta}\,W_{2,Q}(\mu,\beta)\)。前一系数全局且每个完整正半径目标球上锐；后一因子只称有效。\(\beta\) 是该律类唯一不变律，\(\mathcal R_Q^{-1}(0)=\{\beta\}\)。
- **Definitions / Dependencies / Evidence**：[CR6–CR10](research/topics/random_markov/conditional_refresh.md#cr-gaussian-object) 分开指定目标条件均值/方差、同噪声投影收缩、使用独立均匀数保持两边缘的条件运输迭代及最小特征向量平移见证。来源 CM-M Theorem 8 有证明文本；本轮空白逆向审查逐项重核可测分位数、边缘与锐性，不把来源 PASS 当作证明。
- **Counterevidence / Objections / Scope**：没有守恒 \(\nu\) 或二进制 \(\mathsf W_\nu/\mathcal R\)；不把 EB 系数的锐性转授给收缩因子，也不推出原同步 \(\Psi\) 的 EB、随机近端 PPA 或外部新颖性。

<a id="c131"></a>
## C131-v1 / OS-TOWER · 紧源统一有限长度塔

- **Status**：`derived-checked`；规范正文给出从精确塔不等式到同固定集和一致极限的自足证明。
- **Exact Statement / Objects / Domain / Quantifiers**：非空紧度量 \(K\)，连续 \(T,U:K\to K\)；\(T\) 的每条轨道有限长，\(V_j(x)=\sum_{k\ge j}d(T^{k+1}x,T^kx)\)，且 \(L_j=\sup_K V_j\to0\)。此统一尾已使各 \(V_j\) 连续。对**全部** \(x\in K,j\ge0\)，有 \(d(Ux,x)+V_0(Ux)\le V_0(x)\)、\(V_j(Ux)\le V_{j+1}(x)\)。则 \(S=\operatorname{Fix}T=\operatorname{Fix}U\ne\varnothing\)，\(U\) 的第 \(n\) 步之后全尾长 \(\le V_n(x)\le L_n\)，\(U^n\) 一致收敛至连续回缩 \(\Pi_U:K\to S\)。
- **Dependencies / Evidence**：[OS-TOWER 证明](research/operator_space.md#os-tower-proof) 的固定集、望远镜式及紧完备一致极限；来源 OS-R §1 A.2 是线索而非补前提。
- **Objections / Scope**：逐点有限长度不蕴含统一尾；塔不等式并不生产丰富 \(U\) 族，亦不证明观测映射保纲或总体 RLEB/LT/极大单调规模比较。

<a id="c132"></a>
## C132-v1 / OS-FIBER-EB · 新定义紧输入源的完整纤维 EB

- **Status**：`derived-checked`；对紧逆纤维的真残差极小值及同输入反演已在规范层证明。
- **Exact Statement / Objects / Domain / Quantifiers**：实赋范空间 \(E\) 的非空紧 \(K\)、连续 \(U:K\to K\)、非空 \(S=\operatorname{Fix}U\)、\(\lambda>0\)，非降 \(\psi:[0,\infty)\to[0,\infty)\)。若每个 \(x\in K\) 有 \(d(Ux,S)\le\psi(\|x-Ux\|/\lambda)\)，从头定义 \(F_{U,K}(u)=\{(x-u)/\lambda:x\in K,Ux=u\}\)（无原像则空），则完整近端的自然输入域恰为 \(K\)、\(J_{\lambda F_{U,K}}(x)=\{Ux\}\) 在 \(K\) 上，\(F_{U,K}^{-1}(0)=S\)，且**每个** \(u\in U(K)\) 有 \(d(u,S)\le\psi(r_{F_{U,K}}(u))\)，其中 \(r_{F_{U,K}}(u)=\min_{Ux=u}\|x-u\|/\lambda\)。
- **Dependencies / Evidence**：[OS-FIBER-EB 证明](research/operator_space.md#os-fiber-eb) 的紧纤维极小值；若原 \(\psi\) 不满足 D04 的零点/原点连续约定，(OS6) 从紧子水平集构造 \(\phi\le\psi\) 的 D04 型内生 gauge，并保留真残差界。C131 可另外生成符合其固定集条件的 \(U\)，但本条作为条件引理不依赖塔。来源 OS-R §1 A.3 只作溯源。
- **Objections / Scope**：在紧源上不需假设原 \(\psi\) 连续即可取得最小值；不能把新关系的结论转给有域外输入或额外逆纤维的原关系。已保证输入自然域 \(K\) 的 coverage，**没有自动的环境开邻域 coverage**、统一兼容或总体规模结论。

<a id="c133"></a>
## C133-v1 / OS-SUCCESSOR · 连续轨道后继选择的共同尾

- **Status**：`derived-checked`，仅对**已给定**的连续后继选择证明性质；没有非平凡选择定理。
- **Exact Statement / Objects / Domain / Quantifiers**：非空紧度量 \(K\)，连续 \(T:K\to K\)，\(e_n=\sup_{x\in K,k,\ell\ge n}d(T^kx,T^\ell x)\to0\)。给定连续 \(U:K\to K\)，对**每个** \(x\) 有 \(Ux\in\overline{\{T^mx:m\ge1\}}\)。则 \(U^nx\in\overline{\{T^mx:m\ge n\}}\)，对所有 \(m\ge n\) 有 \(d(U^mx,U^nx)\le e_n\)；\(\operatorname{Fix}U=\operatorname{Fix}T\ne\varnothing\)，\(U^n\) 一致收敛到连续回缩。
- **Dependencies / Evidence**：[OS-SUCCESSOR 自足证明](research/operator_space.md#os-successor-proof) 的闭尾集前向包含、周期点门和统一 Cauchy 极限；来源 OS-R §1 A.4 仅作溯源。
- **Objections / Scope**：\(U=T\) 是平凡选择；没有其它连续选择的存在、自由度或母空间位置定理。共同 Cauchy 尾不是长度尾，真全纤维 EB 若需调用必须另合取 C132 的**新关系**条件。原关系和总体大小比较不随此条关闭。

<a id="c133-v2"></a>
## C133-v2 / OS-SAME-LIMIT · 后继选择保持原极限回缩

- **Status**：`derived-checked`；在 C133-v1 的同一全部前提下新增**极限身份与误差界**，不是对来源旧陈述的静默扩写。
- **Exact Statement / Objects / Domain / Quantifiers**：保持 C133-v1 的非空紧 \(K\)、连续 \(T,U\)、共同 Cauchy 尾 \(e_n\to0\)，以及对每个 \(x\) 的正时刻轨道闭包选择。令 \(\Pi_T=\lim_nT^n\)，则对**每个** \(x\in K,n\ge0\)，\(d(U^nx,\Pi_Tx)\le e_n\)，故 \(\Pi_U=\Pi_T\)；C133-v1 的同固定集和回缩结论仍成立。
- **Dependencies / Evidence**：[OS8](research/operator_space.md#os-successor-proof) 由 C133-v1 的 \(U^nx\in A_n(x)\)、同一 \(\Pi_Tx\in A_n(x)\) 与 \(\operatorname{diam}A_n(x)\le e_n\) 直接推出；新版本来自独立空白逆向证明，来源 OS-R §1 A.4 不承担新增结论。
- **Objections / Scope**：只对**已存在的**连续后继选择；没有构造具有规模意义的新选择、长度尾或原算子真 EB，更没有保纲性。

<a id="c134"></a>
## C134-v1 / OS-ISOMETRY · 紧满射非扩张的等距性

- **Status**：`derived-checked`；规范正文给出紧等度连续迭代与满射回代的证明。
- **Exact Statement / Objects / Domain / Quantifiers**：任意非空紧度量空间 \(K\)，满射 \(h:K\to K\) 满足 \(d(hx,hy)\le d(x,y)\) 对全部 \(x,y\)。则 \(d(hx,hy)=d(x,y)\) 对全部点对成立。
- **Dependencies / Evidence**：[OS-ISOMETRY 证明](research/operator_space.md#os-isometry-proof) 的 Arzelà–Ascoli 相对紧迭代、近单位幂和满射代换；来源 OS-R §6 F.2 仅作溯源。
- **Objections / Scope**：结论只对同一个紧域上的满射全局非扩张映射；未排除轨道点对约束、非满射、非紧域的粗糙变换，也不证明 category-preserving 或 LT/RLEB 总体规模。

<a id="c135"></a>
## C135-v1 / OS-SPECTRUM · 闭预算关系的紧步长谱上半连续

- **Status**：`derived-checked`，仅限抽象闭预算关系的拓扑引理；LT、direct、energy 的预算块闭性和穷尽性尚未在共同中立母空间认证。
- **Exact Statement / Objects / Domain / Quantifiers**：任意拓扑空间 \(X\)，每个 \(j\ge1\) 的紧实步长区间 \(I_j=[1/j,j]\)，给**分别指定**的 \(C\in\{\mathrm{LT},\mathrm{direct},\mathrm{energy}\}\) 与乘积闭集 \(B_{C,j}\subset X\times I_j\)。对每个 \(G\in X\)，\(\Sigma_{C,j}(G)=\{\lambda\in I_j:(G,\lambda)\in B_{C,j}\}\) 为紧集或空集；多值谱（允许空值）上半连续，\(P_{C,j}=\{G:\Sigma_{C,j}(G)\ne\varnothing\}\) 闭。**仅当**某认证存在谓词恰为 \(\bigcup_{j\ge1}P_{C,j}\) 时，它是 \(F_\sigma\)。
- **Dependencies / Evidence**：[OS9 条件证明与下半连续反例](research/operator_space.md#os-spectrum-proof)：紧参数上的闭集投影闭，同一结论应用于避开谱的紧集；\(X=\mathbb R,B=X\times\{0\}\cup\{(0,1)\}\) 的非空纤维仍无下半连续。来源 OS-R §7 G.1–G.2 仅是线索，其损坏的公式字节没有复制。
- **Counterevidence / Objections / Scope**：各认证的完整图、coverage、真实全纤维 EB、留域及参数预算能否在选定拓扑下成为闭关系，须分别证明；必要闭块不能当作等价认证。没有下半连续、谱开窗、保纲、尖锐描述复杂度或总体规模结论。改变对象拓扑或证书穷尽条件须立新版本。

<a id="c136"></a>
## C136-v1 / SS-RLEB-BALL · 局部 RLEB 整球共同尾与完整近端门

- **Status**：`derived-checked`，是已独立重构的单值图块 [C02-v2](#c02-v2) 与 SS-TRANSFER 的条件合成；不把原 C02 的其余稿件范围或具体原关系的全部完整近端分支升级。
- **Exact Statement / Objects / Domain / Quantifiers**：在同一有限维 Euclidean \(E\) 中固定 R01/R02 的 \(F,\mathcal G,S,U,U_R,\lambda,R,L,0<\gamma<1,\psi,\kappa\)，保留**全部**图块覆盖、每输入最近零锚、全对 RL、每个实际输出的完整真残差 EB、gauge 定义域与严格直接兼容。取 \(\bar x\in S\cap U\)、\(B_\rho(\bar x)\subset U\) 和 \(0<\varepsilon\le R\) 且 \(\varepsilon+\mathcal L(\varepsilon)<\rho\)。令 \(W=U_R\cap\overline B_{\varepsilon+\mathcal L(\varepsilon)}(\bar x)\)，\(H=(R^{1-\gamma}+L)/2\)。对**每个** \(x\in B_\varepsilon(\bar x),k\ge0\)，图块轨道在 \(W\)，并有 \(\|J_\mathcal G^kx-\Pi_\mathcal G(x)\|\le H\varepsilon^\gamma\kappa^{\gamma k}/(1-\kappa^\gamma)\)；同球的极限映射有 SS-T2 中 \(\beta=\log(1/\kappa^\gamma)/\log(1/\gamma)\) 的两点模。**充分地，再加** \(J_{\lambda F}(u)=\{J_\mathcal G(u)\}\) 对所有 \(u\in W\)，便把全部轨道与模授予完整 PPA；只在所有球初值的可达输入上逐纤维核同一性也足够。若同球全部实际输出另满足 \(d_{k+1}\le Kd_k^\nu\)、\(K>0,\nu>1\)，缩 \(\varepsilon\) 使 \(K^{1/(\nu-1)}\varepsilon<1\)，则有 SS-B5 的统一超几何尾与 SS-T3 的 \(\alpha=\log\nu/\log(\nu/\gamma)\) 两点模。
- **Dependencies / Evidence**：[SS-B1–B5 自足推导](research/canonical/solution_selection_rates.md#ss-rleb-ball) 从 [C02-v2 的 R01/R02 自足证明](research/rleb_ppa.md#r02-proof) 取同一局部图块及严格留域，再以 [SS-T1–T3](research/canonical/solution_selection_rates.md#ss-transfer) 的共同尾传递；SS1 来源 §1 Corollary 1 的 105–171 行是重写线索。
- **Counterevidence / Objections / Scope**：逐初值尾常数不足以得同球极限模；只在初值球上检查完整纤维相等不足以保证漂移后的轨道。闭完整 \(F(y)=\{y,-y\}\) 与对角图块显示完整 \(J_F(0)\) 可含远支。增长条件仅在真实输出与同一留域下提供附加速率，不蕴含无条件完整 PPA 或总体类别比较。

<a id="c137"></a>
## C137-v1 / SS-GEOMETRIC-CAP · 完整二支图的几何尾与证书分层

- **Status**：`derived-checked`，范围为本对象的完整纤维反演、全对局部模、真 EB、固定兼容半径及共同几何尾；§3 的同图配对下界另立 C138，外部原创性未审。
- **Exact Statement / Objects / Domain / Quantifiers**：在 \(E=\mathbb R^3,\lambda=1\) 固定 [GC-1](research/canonical/selection_geometric_cap.md#gc-object) 的完整闭半代数二支关系；\(S=\mathbb R^2\times\{0\}\)，完整 \(J_F=T\) 在全部输入上唯一且由 (GC-2) 给出。对每个 \(R>0\)，同一完整图在输入对尺度 \(R\) 满足 \(\mathrm{RL}(1,1/2,L_R;R)\)，\(L_R=2\sqrt2+3\sqrt R/2\)；半阶最大、渐近最佳常数为 \(2\sqrt2\)，不声称每个固定 \(R\) 的 \(L_R\) 最小。完整真残差有 \(d(u,S)\le r_F(u)^2/4\)，系数渐近最优。固定 \(0<R<[2(4-2\sqrt2)/5]^2\) 和 \(\bar t\ge(R+L_R\sqrt R)/2\) 后，\(\psi(t)=t^2/4\) 可在 \([0,\bar t]\) 调用，直接兼容常数 \(\kappa_R=(\sqrt R+L_R)^2/16<1\)；全部输入轨道仍直接满足 \(d(Tx,S)=d(x,S)/4\)，每个 \(|r_0|\le R,k\ge0\) 具有 (GC-8) 的共同点尾，故 SS-T2 可取 \(\sigma=1/2,\beta=1\) 的上界。
- **Dependencies / Evidence**：[完整三段反演、全对图与尾界的逐式证明](research/canonical/selection_geometric_cap.md#gc-object)；GC-3 的全对反射模经 GC-3a 给同一完整 \(T\) 的 \(H_R=(\sqrt R+L_R)/2\) 单步半阶模，和显式共同尾**合取**后才调用 SS-TRANSFER。C02-v2 只用于另一个固定小半径的严格证书链；实际轨道率由显式 \(T\) 单独算得。来源 SS1 `research_note.md` §2 定理 2 的 181–293 行只作定位。
- **Counterevidence / Objections / Scope**：负输入选中残差较大一支，EB 必须用全部输出纤维的最小值；\(\kappa_R\) 与实际 \(1/4\) 不等，固定半径不受 \(R\downarrow0\) 的极限替代。本版本的共同尾只给上界；同模型配对锐阶另立 [C138](#c138)，§5.2 应用或全部参数族不纳入。

<a id="c138"></a>
## C138-v1 / SS-GEOMETRIC-SHARP · 几何 cap 图极限选择的匹配劣化

- **Status**：`derived-checked`，仅对显示的同一完整关系和同一配对族的首次切换证明；不判文献原创性。
- **Exact Statement / Objects / Domain / Quantifiers**：固定 C137 的完整 \(F\) 和全域唯一 \(T=J_F\)。对**每个固定** \(0<r_0<1\)，比较 \(x_0=(0,0,r_0)\)、\(x_\varepsilon=(0,\varepsilon,r_0)\)。存在仅依赖 \(r_0\) 的 \(c,C,\varepsilon_0>0\)，使全部 \(0<\varepsilon<\varepsilon_0\) 的完整轨道极限满足 \(c\log\log(1/\varepsilon)/\log(1/\varepsilon)\le\|\Pi(x_\varepsilon)-\Pi(x_0)\|\le C\log\log(1/\varepsilon)/\log(1/\varepsilon)\)。故在此配对处没有任何正阶两点 Hölder 模；它匹配 C137/SS-T2 的 \(\beta=1\) 上阶。若称这是同一个 RLEB 固定半径证书**内**的见证，另选 \(0<r_0\le R<[2(4-2\sqrt2)/5]^2\)；一般 \(r_0<1\) 的动力结论不要求该半径。
- **Dependencies / Evidence**：[GS-1–6 首次切换和精确饱和尾](research/canonical/selection_geometric_sharpness.md#gs-sharp) 从 C137 的同一完整 \(T\) 逐步重建，并保持 \(t2^{-N}=\Theta(N)\) 的两侧门；SS1 来源 §3 定理 3 的 294–358 行只是线索。快速独立逆向审查的范围及异议见本轮接收记录。
- **Counterevidence / Objections / Scope**：只声称匹配阶，不声称归一化比值收敛；不能把 \(r_0\) 随 \(\varepsilon\) 改变还沿用同一常数，也不把 C115/C116 的 Q 二次坏选择当作此下界证明。任意 \(\gamma,q\) 几何族另见 C139；§5.2 与全球优先权不由本条证明。

<a id="c139"></a>
## C139-v1 / SS-PARAMETER-FAMILY · 任意幂指数的完整二支几何尾族

- **Status**：`derived-checked`，仅对固定 \(0<\gamma,q<1\)、\(A,B>0\) 的显示关系、全对证书、严格半径及指定配对的双边阶；文献先行性未核。
- **Exact Statement / Objects / Domain / Quantifiers**：在 Euclidean \(\mathbb R^3,\lambda=1\)，[PF-1](research/canonical/selection_parameter_family.md#pf-object) 定义的完整闭二支 \(F\) 有 \(S=\mathbb R^2\times\{0\}\)，且**每个**输入的完整近端单值为 \(T(z,p,r)=(z+A|r|^\gamma,p+B\min\{p_+,|r|\}^\gamma,q|r|)\)。任意固定 \(R>0\) 的全对输入尺度证书为 \(L_R=2\sqrt{A^2+B^2}+(1+2q)R^{1-\gamma}\)，渐近最佳系数为 \(2\sqrt{A^2+B^2}\)；完整真残差给 \(d(u,S)\le q(r_F(u)/A)^{1/\gamma}\)。若另取 \(B/A<\sqrt{q^{-2\gamma}-1}\)、固定 \(R^{1-\gamma}<[Aq^{-\gamma}-\sqrt{A^2+B^2}]/(1+q)\) 并保证 gauge 评价域，则直接兼容 \(\kappa_R<1\)。全部 \(|r_0|\le R\) 初值有共同 \(q^{\gamma k}\) 点尾。对固定 \(0<r_0<1\) 的 \((0,0,r_0),(0,\varepsilon,r_0)\)，极限差为 \(\Theta[(\log\log(1/\varepsilon)/\log(1/\varepsilon))^\beta]\)，\(\beta=\gamma\log(1/q)/\log(1/\gamma)\)；若同证书内调用，另选 \(r_0\le R\) 及上述严格门。
- **Dependencies / Evidence**：[PF-1–12 自足推导](research/canonical/selection_parameter_family.md#pf-object) 独立重算完整纤维、真残差、同一参数的兼容与首次切换；快速独立逆向核参数范围与不等式。C137/C138 恰为 \(\gamma=1/2,q=1/4,A=B=1\) 的特例；原 SS1 359–448 行只作定位。
- **Counterevidence / Objections / Scope**：\(q\) 是实际法向率，\(\kappa_R\) 是更保守的证书率；本条不证明把证书率固定等于 \(q\) 的更窄类锐，也不证明每个固定 \(R\) 的 \(L_R\) 最小。图半代数只在有理 \(\gamma\) 这里被声明；§5.2 的不同三角动力学充分条件另见 C140，另一超线性参数族另立 C141，已按 SF-1–12 的范围独立接收；外部原创性仍未审。

<a id="c140"></a>
## C140-v1 / SS-TANGENTIAL-DECAY · 衰减切向敏感度的混合稳定性

- **Status**：`derived-checked`，仅对指定的全切向域三角动力学和一致常数；原生完整近端表示及外部先行性未核。
- **Exact Statement / Objects / Domain / Quantifiers**：固定 \(m\ge1,0<R<\infty,0<q<1,C,H,\eta>0,0<\gamma\le1\)，令 \(T(a,r)=(a+B(a,r),qr)\) 在 \(\mathbb R^m\times[0,R]\) 上，\(B(a,0)=0\)，对**每个** \(a,b,r,s\) 有 \(\|B(a,r)-B(b,r)\|\le Cr^\eta\|a-b\|\) 与 \(\|B(a,r)-B(a,s)\|\le H|r-s|^\gamma\)。全部轨道有限长，极限 \(\Pi(a,r)=(\Pi_a(a,r),0)\)；同球共同点尾由 (TC-3) 控制，且 \(\|\Pi_a(a,r)-\Pi_a(b,s)\|\le e^{CR^\eta/(1-q^\eta)}[\|a-b\|+H|r-s|^\gamma/(1-q^\gamma)]\)。在有界输入对尺度 \(D\) 上才可合并为纯 \(\gamma\)-Hölder；\(\gamma=1\) 时全局 Lipschitz。
- **Dependencies / Evidence**：[TC-1–5 离散乘积及统一尾证明](research/canonical/selection_tangential_condition.md#tc-proof)；来源 SS1 §5.2 608–641 行只作定位，快速独立审查核指数与常数。[TC 反向边界](research/canonical/selection_tangential_condition.md#tc-boundary) 证明 C139 的尖点切向增量对固定正法向不能满足所需 Lipschitz 门，C137 是特例。
- **Counterevidence / Objections / Scope**：\(\gamma<1\) 时 \(\Pi_a(a,0)=a\) 阻止无界全域上的纯 \(\gamma\)-Hölder；切向子域版本须另证轨道留域。C137/C139 缺此**充分**门不说明别的条件不能给好选择，也不认证一般曲面、耦合法向或原始签名 Schur 图块的稳定性。

<a id="c141"></a>
## C141-v1 / SS-SUPERLINEAR-FAMILY · 任意超线性法向尾的完整二支图

- **Status**：`derived-checked`，仅限 SF-1–12 固定参数完整关系、图块证书与显示的共同尾及配对指数；[10/05 可追溯空白复读](research/audit/BLIND_RECEIPT_2026-10-05.md)重建了完整纤维、最小真残差、尺度/半径、首次切换和 overshoot，未发现受检证明的致命异议。旧有“两轮”审查的逐项记录未随仓库保存，不能据此扩大受检范围。外部先行性、其它原生关系的纤维桥及全库审查仍未核。
- **Exact Statement / Objects / Domain / Quantifiers**：Euclidean \(\mathbb R^3\)、\(\lambda=1\)、固定 \(0<\gamma<1,\nu>1,A,B>0\)。[SF-1](research/canonical/selection_superlinear_family.md#sf-object) 给完整闭二支关系，零集 \(S=\mathbb R^2\times\{0\}\)，对**每个**输入有完整单值 \(J_F=T\) 如 SF-2。对固定 \(0<R_0<1,0<D<\infty\)，完整输出 collar \(0\le y\le R_0^\nu\) 的任意图点对若输入对距 \(\le D\)，有 \(\mathrm{RL}(1,\gamma,L_{R_0,D};D)\) 的 SF-3 证书；全图真实残差给 \(d(u,S)\le(r_F(u)/A)^{\nu/\gamma}\)。存在仅依赖固定参数与 \(R_0\) 的充分小 \(0<R\le R_0\)，使全域 gauge、同图零锚、完整覆盖和 SF-5 的 \(\kappa_R<1\) 同时成立。对全部 \(|r_0|\le R_0\) 有共同 \(Me^{-c\nu^k}\) 点尾；每个 \(0<|r_0|<1\) 的逐轨道点误差满足 SF-7 的确切 Q-\(\nu\) 比值。对每个固定 \(0<r_0<1\) 的 \((0,0,r_0),(0,\varepsilon,r_0)\)，当 \(\varepsilon\downarrow0\) 时，极限差夹在两个 \(e^{-c(\log(1/\varepsilon))^\alpha}\) 型界之间，\(\alpha=\log\nu/\log(\nu/\gamma)\)。若要把配对放在**同一个**严格证书内，另选 \(r_0\le R\)；有理 \(\gamma,\nu\) 才声明半代数。
- **Definitions / Dependencies / Evidence**：[SF-1–12 的完整反演、全部图值最小残差、兼容、共同尾及双侧首次切换](research/canonical/selection_superlinear_family.md#sf-object)；C02-v2 只用于已经另外核过的固定严格证书，C08/SS-TRANSFER 只传共同尾上界，配对下界在本页独立重算。\(\nu=2,\gamma=1/2,A=B=1\) 给 C115/C116 的同图特例。SS1 修订包 `research_note.md` 557–582 行仅为来源定位。
- **Counterevidence / Objections / Scope / Related Files**：\(\kappa_R\) 不是实际法向率；共同尾与 Q-\(\nu\) 比值的统一起点不能混写。SF-11 分开估计 overshoot \(p_N\) 与饱和尾，不把前者误估为 \(O(r_N^\gamma)\)。本条不覆盖 \(|r_0|\ge1\) 的收敛，也不转移到任意原生多值方程；外部先行性未核。来源去向见 [逐单元表](research/audit/UNIT_DISPOSITIONS.tsv)。

<a id="c142"></a>
## C142-v1 / OS-COMPACT-BARRIER · 紧图不可能是极大单调完整图

- **Status**：`derived-checked`；显式加点证明的独立空白复读范围见[10/05 接收记录](research/audit/BLIND_RECEIPT_2026-10-05.md)，旧有审查的逐项记录未随仓库保存。
- **Exact Statement / Objects / Domain / Quantifiers**：对任意**非零实 Hilbert 空间** \(H\) 和任意非空紧集 \(G\subset H\times H\)，\(G\) 不是极大单调关系的完整图；若它单调，存在与其中全部图点构成严格正内积的一个新图点，故可真单调扩张。特别地，任意非空紧 \(K\subset H\)、连续 \(U:K\to K\)、\(\lambda>0\) 从 (OS3) 定义的完整 \(F_{U,K}\) 不是极大单调，无需 C132 的 \(S\)、步界或 gauge 前提。
- **Definitions / Dependencies / Evidence**：[OS-COMPACT-BARRIER 的 (OS6a)](research/operator_space.md#os-compact-barrier) 从两个坐标的一致界直接构造 \(u=(a+1)e,v=te\)，对任意图点严格满足单调加点不等式。C132 的 (OS3) 给出应用所需紧图；证明不导入 Minty 满值定理，也不将 C132 的 EB 误当成单调性。
- **Counterevidence / Objections / Scope / Related Files**：零维空间不在量词内；若 \(G\) 不单调，结论更直接。只排除**紧图本身**充当极大单调关系，不排除一个更大的共同母空间同时容纳紧图及非紧极大单调图，也不排除加点延拓；一旦加点，完整近端和真最小残差须重核。见 [F41](FAILED_ROUTES.md#f41)；不从此推出 RLEB/LT/极大单调的总体规模比较。

<a id="c143"></a>
## C143-v1 / CM-NO-POWER · 紧可数模型的快率与所有正幂 EB 失败

- **Status**：`derived-checked`；限定于下述同一完整对象，规范逐式重构和独立有理证书复核；不认证来源整篇或新颖性。
- **Exact Statement / Objects / Domain / Quantifiers**：[B5–B6](research/topics/random_markov/compact_residual_boundaries.md#crb-object) 固定紧可数实状态集、每块四点、明确映射 T 与恒等/主动概率 7/8、1/8；不变律集遍历全部平稳律，Ψ 使用全部不变目标和每对边缘的完整平方成本最优计划、同一个噪声。对每个输入律 μ，原 Ψ 恰以不变律集为零集并有严格一般 gauge；d(μP)²≤(3125/3267)d(μ)²。同一显式 Πμ=(T#μ+T#²μ)/2 是极限，统一 C、r₀=√(7/8) 对全部 μ、全部 k 给相对几何尾及律空间有限长度。与此同时，对每个 q>0、K≥0、r>0，在 δ₀ 的 r 球内都有同一系统的 ν 使 d(ν)>KΨ(ν)^q。
- **Definitions / Dependencies / Evidence**：[B13–B20 全域运输证书](research/topics/random_markov/compact_residual_boundaries.md#crb-global-transport)、[B21 exact-zero](research/topics/random_markov/compact_residual_boundaries.md#crb-exact-zero)、[B22–B24 全律统一率](research/topics/random_markov/compact_residual_boundaries.md#crb-rate)、[B25–B28 同序列发散](research/topics/random_markov/compact_residual_boundaries.md#crb-no-power)。来源 CM-M Lemma 3/Theorem 4 仅作溯源，不以脚本 PASS 代替证明。
- **Counterevidence / Scope**：不排除一般 gauge、不反驳固定有限状态 C15、不宣称样本路径有限长度或常数锐。B29–B30 另在完整相对状态邻域上固定有效 almost-firm 参数，只排除其指定严格兼容公式，不排除其它速率证明；对应 CM-M Corollary 5。

<a id="c144"></a>
## C144-v1 / CM-FALSE-ZERO · 原同步 OT 残差的投影假零

- **Status**：`derived-checked`；仅限下述完整正方形对象与原始最优计划域，两个锚点和目标距离已逐式重构。
- **Exact Statement / Objects / Domain / Quantifiers**：G=[0,1]²，T_j(x,y)=(x,j)，每步独立公平 j∈{0,1}。全部不变律为 ν⊗β，β=(δ₀+δ₁)/2；任意 μ 一步平稳，原 Ψ(μ)=W₂(μ_y,β)，其零集 ZΨ 是所有第二边缘 β 的律，且 d_W₂(μ,ZΨ)=Ψ(μ)。对每个 0<t<1/2，μ_t=[δ_(1/2−t,0)+δ_(1/2+t,1)]/2 趋于 π̄=δ_(1/2)⊗β，Ψ(μ_t)=0 而 d_W₂(μ_t,全部不变律)=W₂(μ_t,π̄)=t>0。
- **Definitions / Dependencies / Evidence**：[B31 完整定义及最优提升](research/topics/random_markov/compact_residual_boundaries.md#crb-false-zero-object)、[B32–B33 所有不变目标的下界](research/topics/random_markov/compact_residual_boundaries.md#crb-false-zero-witness)。最近锚 π̄ 和实际极限 μ_tP 各有合法输入最优零残差计划；同共同噪声复合及本文明确定义的逐步位移代价仍为零。来源 CM-M Theorem 2，仅作溯源。
- **Counterevidence / Scope**：任何零处取零的局部不变集 gauge 都失败；到 ZΨ 的线性界却以系数 1 成立。此对象是原始 OT 残差假零，与 C71 删除输入最优约束后的假零不同；不改变条件刷新残差或原算子 r_F。

<a id="c145"></a>
## C145-v1 / BIT-ENVELOPE · 非均匀单 bit 的最小非降模与精确律长度

- **Status**：`derived-checked`；BIT1–18 从同一标量核独立重构；核心可测实现、原子阈值强对偶、端点和精确步长已有另一路逐式复核，最终空白接收的实际范围另记。
- **Exact Statement / Objects / Domain / Quantifiers**：标准 Borel 守恒变量 \(u\) 的固定概率边缘 \(\nu\)，可测 \(0<a(u)\le1\)、\(0<b(u)<1\)。以概率 \(a(u)\) 重抽目标 Bernoulli\((b(u))\)，否则保留 bit；全部条件律 \(\mu_r(du,dx)=\nu(du)\operatorname{Bern}(r(u))(dx)\)，\(r:U\to[0,1]\) 可测，以保持 \(u\) 的 \(\mathsf W_\nu\) 比较。\(h=|r-b|\)、\(M=\max(b,1-b)\)、\(E^2=\int h\)、\(\mathcal R^2=\int ah\)。全律最小非降模恰为 \(\phi(t)^2=\sup_{0\le h\le M,\int ah\le t^2}\int h=\inf_{\ell\ge0}[\ell t^2+\int M(1-\ell a)_+]\)，原问题取得，\(\phi(0)=0\) 且原点连续，最终饱和。对每个初律及 \(k\ge0\)，law-step 平方恰为 \(\mathcal R_k^2=E_k^2-E_{k+1}^2=\int a(1-a)^kh\)；精确律长度为该量平方根的级数，允许∞。全初律最大绝对误差平方为 \(\sup_\mu E(\mu P^k)^2=\int M(1-a)^k\to0\)。
- **Definitions / Dependencies / Evidence**：[BIT1–18 独立正文](research/topics/random_markov/one_bit_envelope.md#bit-object) 给全幅度可测实现、有限测度分位与原子填充对偶、全部初律的精确更新，另给 \(a(u)=u^p\) 的饱和幂模与长度阈值 \(p<1\)，以及 \(a(u)=e^{-1/u}\) 的每个局部正幂 EB 失败；公平 bit 的指定补空间谱身份与最小有界余项也独立证明。现存 CM-M Theorem 7 只作来源，不扩写 C129/C130 身份。
- **Counterevidence / Scope**：\(t=0\) 对偶 inf 未必在有限乘子取得；\(\phi\) 不是全局严格增 gauge。绝对共同尾不等于统一相对几何率；律长度不等于样本路径长度。此条件残差的精确能量等式不移植到多 bit、Gaussian 或原同步 \(\Psi\)。原生连续随机映射实现、弱 Poincaré 文献对照与新颖性另核。


<a id="c146"></a>
## C146-v1 / AGM-GRAPH · 同一 AGM 编码的完整纤维与锐真残差

- **Status**：`derived-checked`，限本页直接完整反演与残差证明；不判先行性。
- **Exact Statement / Objects / Domain / Quantifiers**：欧氏 R²、λ=1，P=[0,∞)²，D={(s,t):s≥t≥0}；G(a,b)=((a+b)/2,√ab)。完整 F=G⁻¹−I 在 D 给 (AGM2) 全部两值、域外空。图闭且半代数，零集 S={(h,h):h≥0}，完整自然输入域恰 P，J_F(p)={G(p)} 对每个 p∈P、域外空。每个 u=(s,t)∈D 的完整真残差为 (AGM5)，d(u,S)≤r_F(u)/√2，系数全域最优且轴上取等。
- **Dependencies / Evidence**：[AGM1–6 逐项证明](research/topics/examples/arithmetic_geometric_mean.md#agm-graph)；关系恒等式直接证明，BMW 只作标准身份的已核文献接口。
- **Objections / Scope**：输入 P 与输出 D 不同，不授予整个 R² 满输入；空纤维不以0·∞处理。绝对值延拓是另一完整关系。

<a id="c147"></a>
## C147-v1 / AGM-SELECTION · 共同几何尾与轴处非任意 Hölder 极限

- **Status**：`derived-checked`，AGM7–16 的直接递推、完整路径及多项式证明；精确渐近常数另以已核 Brent 公式为外部前件。
- **Exact Statement / Objects / Domain / Quantifiers**：对每个固定 R>0，C146 的 G 在 W_R=[0,R]² 自映射且完整路径唯一。全部 p∈W_R,n≥0 有 ‖Gⁿp−Π(p)‖≤|p₁−p₂|2⁻ⁿ；Π=(M,M) 为连续回缩，单步半阶安全系数 H_R=√(3R/√2)。M(1,ε)=Θ(1/log(1/ε)) 由 AGM10–11 直接证明；每个固定 0<c<R 的 (c,0) 处 Π 无任何正阶 Hölder 模，任一相对邻域限制不半代数。固定正下坐标 b₀>0 时实际点误差 eₙ₊₁≤eₙ²/(4b₀)，系数不跨轴统一；轴轨道恰 (c2⁻ⁿ,0)。若另调用 Brent 1976 印刷245–246页 (4.16)–(4.18)，则 M(1,ε)∼π/[2log(1/ε)]。
- **Dependencies / Evidence**：[AGM7–16](research/topics/examples/arithmetic_geometric_mean.md#agm-selection) 的差递推、有限乘积界与非零多项式首项；[可选 Brent 接口](research/LITERATURE.md#lit-brent-1976)。
- **Objections / Scope**：同窗共同几何尾不等于共同超几何尾，正初值Q二次不可授予坏参考轴；有界输入位置窗不是仅输入对距窗。Cox指定Th1.1及正数门已核；本条闭轴和坏模由本页直接证明。

<a id="c148"></a>
## C148-v1 / AGM-COMPATIBILITY · 完整直接编码的严格兼容障碍

- **Status**：`derived-checked`，同窗反射下界、实际输出真EB与非减gauge的直接反证。
- **Exact Statement / Objects / Domain / Quantifiers**：固定 C146 同一完整关系及每个 R>0 的 W_R，C=2G−I。任意固定 0<c<R，全部充分小 δ>0 的同窗输入 (c,δ),(c,0) 强制 ω(δ)≥√(cδ)。任何在全部实际输出上提供真EB的非减 ψ:[0,η)→[0,∞) 满足 ψ(h)≥h/√2（0<h<min(η,R/2)）。每当兼容求值有定义，ψ((δ+ω(δ))/2)/δ≥√c/(2√2√δ)→∞；否则已缺求值域。因此不存在同窗全对模与该真EB gauge满足任何固定 κ<1 的小尺度直接兼容。
- **Dependencies / Evidence**：[AGM17–21](research/topics/examples/arithmetic_geometric_mean.md#agm-compatibility)；反射半阶确实可用，否定不是缺一个上界。失败路线 [F42](FAILED_ROUTES.md#f42)。
- **Objections / Scope**：只排除此对象此窗的直接编码；不排除换变量、提升、新关系或不含轴的另一窗。C147动力结果不经严格兼容推得。

<a id="c149"></a>
## C149-v1 / ST-LIPSCHITZ · 共同增量的 Hölder 极限与辅助迭代接口

- **Status**：`derived-checked`，ST1–6规范证明；两篇已核先例和本页去有界性推导分开。
- **Exact Statement / Objects / Domain / Quantifiers**：非空完备度量空间 X，k>1 的全域 k-Lipschitz 自映射 L，c>0、0<ρ<1；每个 x,n≥0 有 d(Lⁿ⁺¹x,Lⁿx)≤cρⁿ。全部轨道极限 R_L 是到Fix L的连续回缩，尾≤cρⁿ/(1−ρ)；0<δ=d(x,y)<1 时 d(R_Lx,R_Ly)≤[1+2c/(ρ(1−ρ))]δ^θ，θ=log(1/ρ)/(log k+log(1/ρ))。有界X另得全域幂界。辅助版本在完备有界X固定连续T、p>1的p-Lipschitz u、0<A<1、B>0及全部x的ST5；只沿uⁿ收敛，给到FixT=Fixu的回缩及θ=log(1/A)/(log p+log(1/A))。
- **Dependencies / Evidence**：[ST1–6](research/canonical/selection_truncation_prior_tools.md#st-lipschitz) 的有限前缀加两条尾与floor估计；[一手先例](research/LITERATURE.md#lit-common-tail) 的准确版本/辅助对象。
- **Objections / Scope**：辅助u不是T；有界空间先例不被冒称无界原定理。BL00原命题及全球先行性未核；Hölder单步的非幂包络另由C08/SS-TRANSFER承担。

<a id="c150"></a>
## C150-v1 / GX053-GEOMETRY · 负平方的图缺陷、扩图与端点目标

- **Status**：`derived-checked`，NS7–10直接计算；历史Spingarn命名不纳入。
- **Exact Statement / Objects / Domain / Quantifiers**：完整F(x)=−x²在[0,1/2]，域外空。非负hypo锐缺陷1，无有限cohypo；打印的锚/双移动一阶商趋0。NS8给真包含本图的全域1-hypo图，故原图不是该明定类别的极大图。0<λ<1的非负LT锐τ=λ/(1−λ)²，λ≥1无有限τ。固定目标(1/2,−1/4)在输入窗[1/2−η,1/2]、0<η≤1/2的MSR/SMSR锐线性系数1/(1−η)，缩窗下确界1但固定非退化窗不取1；最大固定目标幂1。双侧目标正幂MR/SMR皆因空纤维失败。
- **Dependencies / Evidence**：[图几何](research/topics/examples/bounded_negative_square.md#bns-geometry)、[端点目标](research/topics/examples/bounded_negative_square.md#bns-endpoint)；C100/C101原身份不扩大。
- **Objections / Scope**：固定端点目标不是零目标；缩窗模不当作固定窗系数。普通非单调与1-hypo可扩性分别证明。

<a id="c151"></a>
## C151-v1 / GX054-GEOMETRY · 负三次的全图缺陷与非零逆稳定

- **Status**：`derived-checked`，NC5–9完整纤维及局部目标证明。
- **Exact Statement / Objects / Domain / Quantifiers**：完整全域F=−x³无有限全图hypo/cohypo；每个M>0的[−M,M]图块hypo锐3M²，任意零邻域无有限cohypo。每个λ>0完整J(p)恰三次方程全部实根，自然输入全R；完整碰撞排除有限LT。3λM²<1时图块τ锐3λM²/(1−3λM²)²。每个x₀≠0,y₀=−x₀³，完整逆G=−∛y在不含零的目标窗Vη=[y₀−η,y₀+η]、0<η<|y₀|，锐Lipschitz系数Kη=1/[3(|y₀|−η)^(2/3)]；全部x∈Uη=G(Vη)、y∈Vη给MR/SMR，缩窗模1/(3x₀²)。
- **Dependencies / Evidence**：[NC5–7](research/topics/examples/negative_cubic_branch.md#nc-geometry)、[NC8–9](research/topics/examples/negative_cubic_branch.md#nc-nonzero)；C106/C107零点与图块路径另保留。
- **Objections / Scope**：全图、图块和非零局部目标不混同；完整J非空不推出单值。

<a id="c152"></a>
## C152-v1 / GX058-ZERO · 斜旋转法锥的真零残差与四种局部模

- **Status**：`derived-checked`，SB10–11完整法向纤维证明。
- **Exact Statement / Objects / Domain / Quantifiers**：C98/C124同一完整F=K+N_B，零集{0}；每个x∈B有r_F(x)=‖x‖=d(x,{0})，固定零目标全域MSR/SMSR锐系数1。对任意0<ε<1的共同窗‖x‖,‖y‖<ε，完整F(x)={Kx}、F⁻¹(y)={−Ky}，‖x+Ky‖=‖Kx−y‖，MR/SMR/MSR/SMSR局部锐系数均1。每个λ>0的signed及非负LT锐系数0。完整图非线性关系，因其输入投影B不是线性子空间。
- **Dependencies / Evidence**：[SB10–11](research/topics/examples/skew_ball_inverse.md#sb-zero)；边界法向配对的最小范数直接计算。
- **Objections / Scope**：C99非零边界目标的半阶稳定不被原点线性模覆盖；τ=0不证明正强模或正cocoercivity。

<a id="c153"></a>
## C153-v1 / GX059-UPSTREAM · 对角值域与有限截断的属性边界

- **Status**：`derived-checked`，GP3–4及显式有限块计算。
- **Exact Statement / Objects / Domain / Quantifiers**：实ℓ²完整D(xₙ)=(xₙ/n)，ranD={y∈ℓ²:(nyₙ)∈ℓ²}稠密真且非闭；cocoercivity锐1并rectangular。它不继承C102完整F=D+B的非rectangular性。截取F前K二坐标块：强单调锐1/(2K)、‖F^(K)‖=3/2、逆锐1且rectangular，安全正cocoercivity2/(9K)；无维数统一正强模。有限D截断满射。
- **Dependencies / Evidence**：[GP3–4](research/topics/examples/gx059_065_property_completion.md#gxp-diagonal) 完成平方及块奇异值。
- **Objections / Scope**：D的非闭值域不是D+B的值域；有限维证书不恢复无限维正强模。

<a id="c154"></a>
## C154-v1 / GX059–063-DEFECTS · 非负缺陷与 signed τ 分型

- **Status**：`derived-checked`，同一完整对象的单调配对与锐极限。
- **Exact Statement / Objects / Domain / Quantifiers**：GX059 D+B、GX060 V、GX061 V*的非负hypo缺陷0；每个固定λ>0的signed τ下确界亦0，前者由高块极限，后两者由零均值非零方向。平面旋转Qθ的非负hypo缺陷max(0,−cosθ)；GX062/063两角signed τ<0但非负τ=0，原C122/C123锐式不改变。
- **Dependencies / Evidence**：[非负缺陷](research/topics/examples/gx059_065_property_completion.md#gxp-nonnegative-defects) 与已有完整图证明。
- **Objections / Scope**：非负缺陷0不否定正强单调，signed τ和非负violation不得互换。

<a id="c155"></a>
## C155-v1 / GX064-COMPLETION · 正值正弦的VI类、全纤维与普通SMR

- **Status**：`derived-checked`，GP5–7及类型/空纤维证明。
- **Exact Statement / Objects / Domain / Quantifiers**：完整F=2+sinx在R按PD-GEOMETRY的VI点对定义pseudo且quasi而非普通单调。GP5给每个v∈[1,3]的全部周期逆纤维，域外空。非负hypo锐1、无有限cohypo；0<λ<1的τ锐λ/(1−λ)²。cos x̄≠0时完整局部逆在同一个U中单值且所有附近目标可达，ordinary SMR缩窗模1/|cos x̄|。目标3的固定半阶与双側目标空纤维/下侧两支失败仍按C82。
- **Dependencies / Evidence**：[完整纤维与VI](research/topics/examples/gx059_065_property_completion.md#gxp-sine-inverse)、[缺陷](research/topics/examples/gx059_065_property_completion.md#gxp-sine-hypo)、[局部逆](research/topics/examples/gx059_065_property_completion.md#gxp-sine-regular-points)。
- **Objections / Scope**：原算子目标与Minty临界输入不同；零集为空，不能新增零集PPA结论。

<a id="c156"></a>
## C156-v1 / GX065-COMPLETION · 有界平方的VI分离及亚临界完整近端

- **Status**：`derived-checked`，GP8–11直接全部解与符号计算。
- **Exact Statement / Objects / Domain / Quantifiers**：完整F=x²在[−1,1]、域外空，VI类quasi而非pseudo；GP8给全部原纤维，非负hypo锐2且无有限cohypo。0<λ<1/2时完整自然输入域[λ−1,λ+1]，J恰GP9显示加号根分支，τ锐2λ/(1−2λ)²；域外无输出。0<|x̄|<1时ordinary SMR缩窗模1/(2|x̄|)。零目标的固定半阶、负目标空逆像及两侧路径边界不改变C84。
- **Dependencies / Evidence**：[GP8](research/topics/examples/gx059_065_property_completion.md#gxp-square-inverse)、[GP9–10](research/topics/examples/gx059_065_property_completion.md#gxp-square-subcritical)、[GP11](research/topics/examples/gx059_065_property_completion.md#gxp-square-regular-points)。
- **Objections / Scope**：非零参考点须内点，域端点不获得双侧目标coverage；完整有界图不可当全实线映射。

<a id="c157"></a>
## C157-v1 / SELECTION-INTERFACE-BOUNDARIES · 锚、集合距离与选择模

- **Status**：`derived-checked`，两个完整自映射的直接证明。
- **Exact Statement / Objects / Domain / Quantifiers**：实线有理点x/2、无理点0的完整单值T满足零点锚averaged和全域线性步残差EB，全部轨道趋零，但任意0邻域不满足任何正阶全对Hölder单步模。实平面T(x,0)=(x,0)、T(x,y)=(sgn y,0)（y≠0），在U=[−1,1]²留域；FixT=R×{0}，集合距离一步归零、残差EB系数1、T²=T，第一步起共同点尾零，极限选择Π=T却在原点不连续。
- **Dependencies / Evidence**：[SL完整见证](research/canonical/selection_literature_boundaries.md#sl-witnesses)。外部锚/Th4对象边界在同页，直接证明不依赖文献证明。
- **Objections / Scope**：只证接口不蕴含；没有把见证编码成完整PPA，不认证SS1同图RL或严格兼容，更不反驳SS-TRANSFER的全对前提。

<a id="c158"></a>
## C158-v1 / QUASI-MEAN-TAIL-BOUNDARY · 安全共同尾与精确式阻断

- **Status**：`derived-checked`；P16精确印刷公式身份另为`primary-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：固定K>0、正整数k≥1、共同S_K(I)生成元和初始直径上界R<∞，SL3的指数直径半减与局部平方递推给同一初值类共同实际点尾A exp(−c2^n)；常数依赖冻结的K/R/k，不要求输入位置有界。合法f1=t,f2=exp t、K=1的直径递推log cosh(d/2)在固定N、小d处，解析阻断P16 v1 Th2/正式Th3.3的分母e^{KD}−1精确上界及v1 Th3相应精确近似式。
- **Dependencies / Evidence**：[SL3–SL5及解析证书](research/canonical/selection_literature_boundaries.md#sl-p16)；P16版本/印页在LITERATURE。
- **Objections / Scope**：不否定不变表示F=φ∘M，也不否定安全定性共同尾；AGM轴边界不能冻结K。刊本逐式对应以文献卡实际核得状态为准。

<a id="c159"></a>
## C159-v1 / GD-BOUNDARY · 同 gauge 跨 Minty 坐标失败

- **Status**：`derived-checked`，GD-1–7 的完整显式计算。
- **Exact Statement / Objects / Domain / Quantifiers**：实标量、固定 λ=1，t₀=1/2、tₙ=2^(−2ⁿ)，ψ:[0,1/2)→[0,∞)取ψ(t)=tₙ² 对 tₙ≤t<tₙ₋₁、n≥1，ψ(0)=0。ψ 有限非减且 o(t)，完整紧图 Γ={(0,0)}∪{(−tₙ²,tₙ):n≥1} 的零集 {0}，所有有限真实残差点满足 |y|=ψ(r_F(y))。完整 resolvent 在 D={0}∪{tₙ−tₙ²:n≥1} 唯一；每个零点 graph germ 和每个有限 C 均有 |J_Fx|>Cψ(|x|)，而全 D 上 |J_Fx|≤ψ(2|x|)。ψ(2sₙ)/ψ(sₙ)→∞，sₙ=tₙ/2。
- **Dependencies / Evidence**：[完整 gauge、图和证明](research/canonical/gauge_dilation_boundary.md#gd-theorem)；带重标度正向门为 [IZ-GERM](research/canonical/isolated_zero_flatness.md#iz-germ)。补足最终 foundations §7.2 的阶梯见证。
- **Objections / Scope**：D 不含零点的输入邻域，不认证局部全输入 PPA；ψ 在正点不连续，不反驳额外要求正点连续 gauge 的版本。只证明固定同一 gauge 的失败，不否定重标度 gauge 或额外 dilation 控制。

<a id="c160"></a>
## C160-v1 / QA-TAIL-SELECTION · 正则拟算术均值的共同尾与选择界

- **Status**：`derived-checked`，QA1–13 自足证明；指定原文事实另为 `primary-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：开区间 I、k≥1、K>0、全部生成元 fᵢ∈C²(I)、fᵢ′处处非零、fᵢ″局部有界变差、|fᵢ″/fᵢ′|≤K；完整均值映射 T=(fᵢ⁻¹(k⁻¹∑ⱼfᵢ(xⱼ)))ᵢ。先固定 D>0 和 X_D={x∈Iᵏ:diam x≤D}；令 α=(3+7e)/3、0<ℓ<1/α、q=αℓ、N=max(0,ceil log₂[(e^(KD)−1)/(e^ℓ−1)])。全部 x∈X_D 的唯一对角极限 Π(x)=M(x)1 满足全部 n≥N 的 ‖Tⁿx−Πx‖∞≤diam Tⁿx≤(αK)⁻¹q^(2^(n−N))；全文给全部 n≥0 的共同 A exp(−b2ⁿ) 界。同一凸域的全部初值对满足 ‖Πx−Πy‖∞≤exp[2(e^(KD)−1)]‖x−y‖∞。实际点误差对全部n≥N仅授共同 Q二次上界 eₙ₊₁≤4αKeₙ²，不宣称逐轨道锐因子。
- **Dependencies / Evidence**：[QA-OBJECT](research/canonical/selection_quasi_arithmetic_boundary.md#qa-object)、[非负起步共同尾](research/canonical/selection_quasi_arithmetic_boundary.md#qa-uniform-tail)、[同域两初值界](research/canonical/selection_quasi_arithmetic_boundary.md#qa-selection)。直接 Jensen、Taylor 和全部导数乘积证明不依赖 P16 打印尾公式。原文版本与反例接口见 [规范一手接口](research/canonical/selection_primary_interfaces.md)。
- **Objections / Scope**：D=0 的对角族、K=0 的仿射族另行处理，均不代入 log0 或 1/K。AGM 只在固定正闭窗局部化，K=1/a 不移到含轴窗。未编码完整 PPA 关系或授予 RL、真实 EB、严格兼容与新颖性；任意连续 φ属于复合 φ∘M，不代表 M 可任意粗糙。

<a id="c161"></a>
## C161-v1 / CS-TRANSFER-LSC · 扩展实值函数的局部目标距离转移

- **Status**：`derived-checked`，自足证明及独立逐式复读。
- **Exact Statement / Objects / Domain / Quantifiers**：proper lsc f:ℝⁿ→(−∞,+∞]，x̄∈dom f；在 B_α(x̄) 有 f≥f(x̄)，且每个 y∈Γ∩B_ς(x̄) 有 f(y)≤f(x̄)，Γ=zer ∂f、∂ 为 limiting 次微分。指定 S⊂Γ 且包含所有局部极小点。任取 0<R<min(α,ς)，全部 x∈B_{R/4}(x̄) 有 d(x,S)=d(x,Γ)=d(x,{f≤f(x̄)})。以有限值 stationary 点上的实际二阶次导数定义 Θ₂，则 S=Θ₂ 可用。
- **Dependencies / Evidence**：[CS-TRANSFER-LSC](research/canonical/composite_subregularity.md#cs-transfer-lsc) 证明局部三个集合一致，再以共同点 x̄ 及球外距离隔离证明三个全局距离相等；局部极小的 regular Fermat 条件与非负差商直接写明。
- **Objections / Scope**：C34-v1 的有限连续身份保持不变；此较宽版本不赋予扩展实值复合链式规则、近端 coverage 或轨道结论。距离相等不需要三个集合闭或投影存在；用于后续投影时须另核闭性。外部先行性未核。

<a id="c162"></a>
## C162-v1 / CS-CLARKE · 两种 Clarke PSD 替代标准的反例

- **Status**：`derived-checked`，显式公式及独立逐式复读。
- **Exact Statement / Objects / Domain / Quantifiers**：实标量 a=11/10，g(0)=0、g(x)=x²(a+sin log|x|) 于 x≠0。g∈C^{1,1} 且零点强极小；∂_C g′(0)=[2a−√10,2a+√10] 同时含正负数，而每个 w 有 d²g(0|0)(w)=2(a−1)w²。−g 在零点严格极大，∂_C(−g)′(0) 仍含正数，实际二阶次导数为 −2(a+1)w²。
- **Dependencies / Evidence**：[CS-CLARKE](research/canonical/composite_subregularity.md#cs-clarke) 直接计算 g′、g″、全部相位聚值、导数 Lipschitz 界及达到差商下确界的序列。
- **Objections / Scope**：要求全部 Clarke Hessian PSD 会漏掉真实极小点；要求存在 PSD 会纳入上述极大点。只反驳把这两种标准等同于实际 Θ₂ 的身份，不反驳局部极小的二阶必要条件或附加假设下的二阶充分条件。外部先行性未核。

<a id="c163"></a>
## C163-v1 / PA-LIFT · 全部合法块末点的完整反向编码

- **Status**：`derived-checked`，集合关系的双向代数证明及独立复读。
- **Exact Statement / Objects / Domain / Quantifiers**：X=ℝⁿ，固定长度 m≥1 及块边界相位/记忆规则；B_m(x) 枚举从 x 出发的全部合法长度 m 路径末点。对 Λ>0 定义 F_{m,Λ}(y)={(x−y)/Λ:x∈X,y∈B_m(x)}。在全部输入上完整 J_{ΛF_{m,Λ}}=B_m，zer F_{m,Λ}=Fix B_m，包含空纤维。对 U⊂X、L>0、γ>0，输入位于 U 的全部图点对 AP-RL 等价于全部 y∈B_m(x)、y′∈B_m(x′)、x,x′∈U 的 ‖2(y−y′)−(x−x′)‖≤L‖x−x′‖^γ；因此每个输入至多一个末点。
- **Dependencies / Evidence**：[PA-LIFT](research/canonical/path_atlas.md#pa-lift) 对全部纤维双向替换 v=(x−y)/Λ，不靠指定选择；同输入代入给唯一性。
- **Objections / Scope**：还须另证 U⊂dom B_m 才称 U 上单值映射；末点唯一不保证内部路径唯一。F_{m,Λ} 是新定义关系，不自动等于原生生成关系。B_m=T^m 须完整合法路径枚举；Fix T^m 与 Fix T 及到全局目标的距离各自另核。不同相位/记忆、增广状态或度量必须重新声明。

<a id="c164"></a>
## C164-v1 / PA-CAPTURE · 首块有限进入与后续驻定的分层结论

- **Status**：`derived-checked`，有限前缀归纳及独立复读。
- **Exact Statement / Objects / Domain / Quantifiers**：保留 PA-DEF 的 X,S,V,m 与真实合法转移，给初值 x₀∈V、t₀=d(x₀,S)。首块所有合法前缀均有距离/位移界 D_{w,j},G_{w,j}，在 V 中且距 S<η 的每个可达前缀有下一步，每个允许转移可延成合法完整词。全部 j<m,w 有 D_{w,j}(t₀)<η；L₀=sup_wΣ_{j<m}G_{w,j}(t₀)<dist(x₀,X\V)。若全部合法完整路径末点在 S，则每条轨道能构造到 m，首块留在 V，总长≤L₀，并在至多 m 步进入 S。若每个目标点另有至少一步且全部允许后继等于自身，则以后恒定，极限在 S∩V，总长仍≤L₀。
- **Dependencies / Evidence**：[PA-CAPTURE](research/canonical/path_atlas.md#pa-capture) 的有限归纳及吸收集上两点往返反例；RL 只是步界的一种生产方式，并非本结论所需。
- **Objections / Scope**：吸收性只保持已存在的后续路径在 S，不能代替后续 coverage、驻定、留域、有限长或点收敛。另行规定首次进入即停也可有限停机；这与继续迭代后驻定是两种明确算法含义。内部某步进入 S 不能省掉剩余边的吸收条件。

<a id="c165"></a>
## C165-v1 / CS-LOCAL-TARGET · 同一复合数据上的局部零集替换

- **Status**：`derived-checked`，距离隔离及最近点证明经独立复读。
- **Exact Statement / Objects / Domain / Quantifiers**：保持 C35/CS-EB 的全部同一数据、Γ=zer ∂f、S=c⁻¹(argmin φ)、R,σ,J,r。若闭集 T⊂Γ 满足 T∩B_R(x̄)=S∩B_R(x̄)，则全部 x∈B_{R/4}(x̄) 有 d(x,T)=d(x,S)。J≥σ 给 r≤R/4，故 C35 在 B_r 的 EB 保持同一 gauge/常数。另保持 C36 的全部前提时，x∈B_{r/2} 的任意 p∈P_T(x) 满足 ‖p−x̄‖≤2‖x−x̄‖<r，故为同图块零锚；C36 的轨道结论和留域预算可同样使用 T。
- **Dependencies / Evidence**：[CS-LOCAL-TARGET](research/canonical/composite_subregularity.md#cs-local-target) 以同一球内目标及共同点隔离球外距离，闭性提供投影及极限入集。
- **Objections / Scope**：这是替换的充分条件，不是所有替换的必要条件。保留 T⊂Γ 时，S∩B_R⊂T 已强迫局部相等；删去 T⊂Γ 后，单向包含不足。不能遗漏局部零点、把同域 EB 变成缩小目标的未经证明的 EB，或授予完整 J_F 的全部球外纤维身份。

<a id="c166"></a>
## C166-v1 / OP-PROFILE · 完整图残差剖面的同 gauge 门

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：实Hilbert空间H，完整F，任意输出窗V，非空闭S，有限非减ψ:[0,∞)→[0,∞)。B(t)=sup{d(u,S):u∈V,v∈F(u),‖v‖≤t}，空sup0。B≤ψ逐点等价于全部图值界；有限真残差EB推出二者。反向总得d(u,S)≤ψ(r_F(u)+)，每个有限残差取到或ψ在该值右连续时才由本工具得到同ψ的真EB；不是必要条件宣告。
- **Definitions / Dependencies / Evidence**：[OP1–5完整证明](research/canonical/operator_profile_tools.md#op-profile)及强闭ℓ²完整图反例由独立Astra从定义重算。有限维闭纤维取到的充分门明确；有限gauge上端点另核。
- **Counterevidence / Scope / Related Files**：仅原点连续和Hilbert闭图不足，反例r=1不达且ψ正点右跳。此是图值到inf桥，不与C59窗口缩域混同；不认证RL、coverage、算法留域或总体比较，外部新颖性未核。

<a id="c167"></a>
## C167-v1 / OP-COMPACTNESS · 同一紧对象块的闭约束相容性

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：固定非空紧拓扑对象块𝒦，固定闭子集C_i⊂𝒦(i≥1)，全部交非空当且仅当每个前N项交非空。用于严格认证须在同一实际对象块内预先固定可保留的闭余量条件。
- **Definitions / Dependencies / Evidence**：[OP6及两个边界反例](research/canonical/operator_profile_tools.md#op-compactness)为紧开覆盖证明，独立重构。
- **Counterevidence / Scope / Related Files**：非紧𝒦=ℝ、C_i=[i,∞)或非闭C_i=(0,1/i)均失败；随N改块/退化余量不满足条件。有限可行、闭性、原生身份、全部图点升级须另证；不是总体比较或实际拼接定理。

<a id="c168"></a>
## C168-v1 / OP-HOLE · 鲁棒越界见证与相对孔洞

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：固定紧度量K、非空闭S⊂K，𝔛⊂C(K,K)配一致度量，M≥0；A_M由所有x的d(Tx,x)≤Md(x,S)定义。若U∈𝔛在某x_*有余量a>0，则相对球B𝔛(U,a/2)避开A_M。若另有同c∈(0,1)对所有声明中心T和全部足够小r构造同𝔛中的U,a，使d∞(T,U)+cr≤r且a≥2cr，则B𝔛(U,cr)⊂B𝔛(T,r)\A_M。
- **Definitions / Dependencies / Evidence**：[OP7–9三角证明](research/canonical/operator_profile_tools.md#op-hole)；独立审查同时攻击全中心/全小尺度量词及实际母空间保持门。
- **Counterevidence / Scope / Related Files**：一个鲁棒见证不保证统一孔洞；别的对象度量需独立控制评价误差。本条不认证历史σ-upper/lower-porosity定理，也不提供同尾完整对象构造、LT统一必要常数或总体比较。

<a id="c169"></a>
## C169-v1 / FINITE-POLYHEDRAL-TARGET · 多面体目标的锐嵌套OT证书

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：固定N≥1个互异Euclidean状态、平方距离成本C、固定R≥0且零对角、非空紧凸多面体J⊂Δ_N。对全部μ，Φ_J取外层全部J、内层实际两边缘的C最优计划的最小R成本；E_J=d_W2(μ,J)²。对正规化运输对偶全部tight-edge分支F_k^J及全部顶点V_J，exact-zero Φ_J^-1(0)=J、零R顶点的行边缘在J、全simplex有限线性W2 EB三者等价。
- **Conclusion**：最小平方系数B*=max_{v∈V_J,Rv>0}E_J(rv)/(Rv)，空最大值0；各非空零面上的有限LP可判定目标成员资格。有理C,R及目标约束给有理B*，K*=√B*未必有理。不要求exact-zero时，Φ_J仍全域Lipschitz且连续有限PWA。
- **Dependencies / Evidence**：[FSC1–4及完整证明](research/topics/random_markov/finite_state_completion.md#fsc-polyhedral)；完整计划并、凸E、零顶点及锐下界重构；正则性明确调用C80规范FS9–FS10和已核Hoffman接口，锐证书不依赖Hoffman。来源LF325–327，补目标非空门。
- **Counterevidence / Scope**：J不自动是平稳律集，R不自动有随机映射表示；不承诺多项式算法、跨系统统一系数、动力收敛或非凸目标。不能删除输入最优性或把外层只限E最近目标。C15在J=I时是特例，C80是平稳目标的正则性特例。

<a id="c170"></a>
## C170-v1 / FINITE-SUPPORT-IDENTIFICATION · 三状态支撑识别与最近目标分离

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：完整G=(0,1,2)，确定T=(0,1,0)，全部律μ=(a,b,c)∈Δ3；平方Euclidean运输成本和同映射同步位移残差，外层遍历完整I={(q,1−q,0)}、内层C最优。对全部μ，E=c、Φ=4c、锐K=1/2。
- **Conclusion**：0与1位移签名相同，故不存在全状态R≥c0C的正系数，但原残差仍精确识别完整I。c>0时最近目标(a,b+c,0)与实际一步极限(a+c,b,0)不同。两个状态的R_xy=0迫使每个正概率映射恒等，故三状态在“存在位移碰撞而I是真子集”的意义下最小。
- **Dependencies / Evidence**：[FSC5–6完整证明](research/topics/random_markov/finite_state_completion.md#fsc-support)逐全部目标和耦合算R成本，目标支撑给C下界，显式计划取到；两状态自映射完整枚举。
- **Counterevidence / Scope**：这个例子的识别只靠目标支撑，不需OT限制；C71另证明真正依赖OT的例子。最小状态数仅针对明确碰撞条件，不是所有有限状态模型分类。不同目标、law-step或条件残差不由本结果覆盖。

<a id="c171"></a>
## C171-v1 / LAZY-CYCLE-RATE-COMPATIBILITY · 四循环的真实几何率与标量兼容障碍

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：同C71完整模型G=(0,1,3,4)，循环T，独立新噪声以(1−p,p)选择(I,T)，p∈(0,1)，π公平律，原输入最优同步Ψ与普通W2。γ_p=√((1−p)²+p²)。对全部μ及全部k≥0，W2((P_p^T)^kμ,π)≤4·2^(1/4)γ_p^(k/2)W2(μ,π)。
- **Conclusion**：对全部状态对的E(output差²)+τE(位移差²)≤(1+ε)input差²，任意τ>0的最小非负ε恰为p(15+25τ)。任一π邻域内连续严格递增、ρ(0)=0的可逆局部EB gauge均不可能与同一有效τ,ε使指定式θ(t)²=(1+ε)t²−τ[ρ^-1(t)]²<t²对所有充分小t>0成立。邻接质量族给ρ(r)≥2r/√p，但该式要求ρ(r)<r/(5√p)。
- **Dependencies / Evidence**：[全初律率证明](research/topics/random_markov/finite_state_completion.md#fsc-lazy-rate)、[六对精确参数及局部障碍](research/topics/random_markov/finite_state_completion.md#fsc-compatibility)；Fourier谱、W2²与TV双界、零和范数比较、全部六状态对、唯一有序局部计划。补[全局锐点径向缩放的反算](research/topics/random_markov/finite_state_completion.md#fsc-cell-grid)：前半段平方比3/p而非13/p。
- **Counterevidence / Scope**：C71的线性EB和本条真实收敛仍成立；只阻断显示的特定标量公式及全状态pointwise参数，未排其它metrics/residuals/measure-level dissipation。ρ仅非降时必须另定义广义逆，本条不代猜。p=1不属几何率结论；换同核随机表示也须重算R。该公式外部论文归属仍deferred，直接数学反证不依赖它。

<a id="c172"></a>
## C172-v1 / OP-POWER · 双侧实际剖面的 direct 幂门

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：固定λ>0、0<γ≤1、p>0，所有足够小t,r有正常数双侧界a_Mt^γ≤M(t)≤b_Mt^γ及a_Br^p≤B(r)≤b_Br^p；B为C166同一剖面。对bλ(t)=(t+M(t))/(2λ)，存在固定κ∈(0,1)的全小尺度B(bλ(t))≤κt在γp>1成立、γp<1不可能；γp=1须保系数。
- **Definitions / Dependencies / Evidence**：[OP10–11](research/canonical/operator_profile_tools.md#op-power)逐项双侧幂比较；端点c/λ正好可跨1。
- **Counterevidence / Scope / Related Files**：只有上界阶不提供必要性；真实PPA还需同图/零锚、C166真残差桥、coverage与留域。该函数复合的门不是普适实际轨道阶或完整算子类大小结论。

<a id="c173"></a>
## C173-v1 / CF-GIBBS · 有限相关Gibbs的条件比较与两律收缩

- **Status**：`derived-checked`；有限平稳配对、边缘保持、Neumann比较和显式加权范数证明独立重建。
- **Exact Statement / Objects / Domain / Quantifiers**：X={0,1}^m，m≥1，β为X上的严格正概率律（所有β(x)>0且Σ_(x∈X)β(x)=1），p_i>0，Σp_i≤1，实际随机坐标核按β的full conditional刷新，余概率恒等。非负C、c_ii=0，对全部x,y满足TV(β_i(.|x_-i),β_i(.|y_-i))≤Σ_j c_ij 1_(x_j≠y_j)，ρ(C)<1。对全部概率律μ及任意w>0，r_i=E_μTV(μ_i(.|X_-i),β_i(.|X_-i))，E_w²为加权Hamming最优成本，D_cond,w²=Σp_iw_ir_i。有E_w²≤wᵀ(I-C)^-1r≤K_w²D_cond,w²，K_w²=max_i [wᵀ(I-C)^-1]_i/(p_iw_i)。零集{β}。令B=I-D_p+D_pC，取wᵀ=1ᵀ(I-B)^-1、θ=max_j(w_j-1)/w_j∈[0,1)，则对全部两律μ,η，W_w(μP,ηP)≤√θ W_w(μ,η)。β为唯一不变律。纤维积分只在共同w,K,θ和可测门下成立。
- **Definitions / Dependencies / Evidence**：[CF1–CF5](research/topics/random_markov/conditional_refresh_interfaces.md#cfi-gibbs-object)。条件比较保持同一两边缘的Cesàro平稳配对；收缩权重直接由v=(I-C)^-1 1和加权范数得，无未列外部M-matrix定理调用。
- **Counterevidence / Objections / Scope**：C条件只充分，不声称必要；K_w、θ不声称锐，收缩不是对任意权重；残差为条件TV/Hamming接口，不是Ψ；共同纤维常数不能由逐点有限性推得。外部优先权未核。
- **Related source**：上述519 LF原件§4 270–321。独立敌对审计原件不在此范围。

<a id="c174"></a>
## C174-v1 / CF-COMPACT · 可数连续刷新与锐期望能量常数

- **Status**：`derived-checked`；实际映射的连续性、概率合法性、全纤维能量与最佳常数逐项计算。
- **Exact Statement / Objects / Domain / Quantifiers**：K=({0}∪{2^-n:n≥1})×{0,1}⊂R²。对n,j映射仅在第n纤维将bit置j，概率a_n/2，a_n=2^(-n²-4n-4)，余概率恒等；每步独立。全部映射连续，表示可数。固定ν(2^-n)=2^-n、ν(0)=0，全固定边缘律的公平目标π唯一不变，D_cond²=Σ2^-n a_n|r_n-1/2|，E²=Σ2^-n|r_n-1/2|。最小非降模与精确law-step/积分尾按C145成立；最大绝对误差平方为(1/2)Σ2^-n(1-a_n)^k→0，任意正半径完整条件目标球上无任何正幂EB。同时全部z,z'∈K，同一随机映射T下E[||Tz-Tz'||²+||(z-Tz)-(z'-Tz')||²]≤(1+ε*)||z-z'||²的最小ε*=129/4096（α=1/2约定）。
- **Definitions / Dependencies / Evidence**：[CF6–CF10](research/topics/random_markov/conditional_refresh_interfaces.md#cfi-compact-object)，条件gauge/律长度依赖C145指定单bit接口；常数按同纤维/异纤维异bit/同bit三类全部计算，最坏在n=1,m=2同bit。
- **Counterevidence / Objections / Scope**：来源17/256仍有效但非最优；这里有限地图实现未宣称，不能移植到原Ψ。固定ν不含0，未说全K不变律唯一；不同ν和极限纤维是其它不变类。外部先行性未核。

<a id="c175"></a>
## C175-v1 / CF-TYPED-BOUNDARIES · 条件残差与同步能量及联合拓扑的分离

- **Status**：`derived-checked`；有理数OT上下界、条件概率及显式同边缘运输独立重算。
- **Exact Statement / Objects / Domain / Quantifiers**：第一对象为二bit公平乘积、等概率随机坐标刷新、μ=(1/2,0,1/4,1/4)按00,01,10,11排列：μP=(5/16,3/16,5/16,3/16)，E²=1/4，E+²=1/8，D_cond²=1/4，因此E+²+D_cond²≤E²失败；同一同步坐标/新bit配对的输出+位移差能量恒等式仍成立。边缘公平对角律的坐标边缘距离皆零但D_cond²=1/2，任一刷新即目标。第二对象冻结ν=Leb([0,1])、一步完整公平bit刷新：每个长1/N小区间左半确定0右半确定1的μ_N满足条件Wν²=D_cond²=1/2而普通W2(μ_N,ν⊗fair)≤1/(2N)→0。所有同ν两律普通W2≤条件Wν。另对C144同一两原子μ_t，原Ψ=0而D_cond=1/√2，故该族不存在D_cond≤KΨ的有限K。
- **Definitions / Dependencies / Evidence**：[CF11–CF13](research/topics/random_markov/conditional_refresh_interfaces.md#cfi-boundary-object)，C144只供应已证明的原输入最优Ψ身份和两原子见证。条件拓扑反例显式保持同一ν；三模型在正文分别声明。
- **Counterevidence / Objections / Scope**：不否定C129/C130的条件EB，不否定实际同步配对能量；不把D_cond当Ψ或一般law-step。跨ν不直接定义Wν，绝对尾不等于相对率。没有通用非线性RL结论。

<a id="c176"></a>
## C176-v1 / CONDITIONAL-REAL-PRODUCT · 有限实坐标乘积刷新的条件误差界

- **Status**：`derived-checked`，CF15 的可测分位数、条件混合与实际核证明经独立重构及本轮协调复核；本次补全既有正文/图关系的身份登记。
- **Exact Statement / Objects / Domain / Quantifiers**：固定整数 m≥1、β_i∈𝒫₂(ℝ)、β=⊗ᵢβ_i，以及 p_i>0、Σᵢp_i≤1。核 P 以概率 p_i 独立重抽第 i 坐标为 β_i，余概率保持。对全部 μ∈𝒫₂(ℝᵐ)，以标准Borel常规条件律定义 d_i²=∫W₂(μ_i(·|x₋ᵢ),β_i)²dμ₋ᵢ 和 D_cond²=Σᵢp_id_i²，a_*=minᵢp_i。全部条件成本可测且有限，并有 W₂(μ,β)²≤Σᵢd_i²≤D_cond²/a_*、W₂(μP,β)²≤(1−a_*)W₂(μ,β)²。因此残差零集恰为{β}，β是𝒫₂内唯一不变律，且 W₂(μPᵏ,β)≤(1−a_*)^(k/2)W₂(μ,β)。a_*=1时k=0另取因子1。
- **Definitions / Dependencies / Evidence**：[CF15完整自足证明](research/topics/random_markov/conditional_refresh_interfaces.md#cfi-real-product)：一维共同分位数的可测性、截断/层积分最优性、条件混合保持同β_i第二边缘及顺序耦合给第一界；共享实际重抽给收缩。仅导入标准Borel常规条件概率分解和基本积分事实，不借有限bit的最优常数迁移。
- **Counterevidence / Objections / Scope / Related Files**：这是有限个实坐标、同一个乘积目标和核上的有效常数，不声明锐性、相关非乘积目标、任意纤维或一般Ψ界。D_cond不等于law-step或同步输入最优OT残差Ψ；普通联合W₂是本对象的距离，不与守恒变量下的条件距离混用。来源519LF去向在[条件修复审计](research/audit/CONDITIONAL_REPAIR_FULL_COVERAGE.md)；既有图E273不改变数学范围，新颖性未核。

<a id="c177"></a>
## C177-v1 / NG-GERM · 固定零点连续自映射的germ商：非Polish而仍Baire

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：X={f∈C([0,1],[0,1]):f(0)=0}配一致拓扑，f~g iff某ε>0使二者在[0,ε]相等，Q=X/~配商拓扑。每类在X稠密，Q至少两点且仅空集/全空间为开集；故非T0/T1/Hausdorff/Polish，但Q仍Baire。
- **Definitions / Dependencies / Evidence**：[NG-GERM完整证明](research/canonical/topological_repair_obstructions.md#tr-germ)；近0连续凸拼接保持值域和固定0并一致逼近任意g；每类稠密使非空开饱和集必为全体；平凡拓扑直接核Baire。
- **Counterevidence / Scope / Related Files**：不移植为历史完整图/收敛动力/全时间拓扑或所有germ商；否定非Hausdorff⇒非Baire的过宽读法，不否定全部比较方案。 外部新颖性未核。

<a id="c178"></a>
## C178-v1 / NG-CLOSED-REPAIR · 两个闭集不保证局部线性相交误差界

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：R²中A=R×{0}、B={(t,t²):t∈R}闭且A∩B={0}；对任意r>0和有限κ≥0，存在0<||z||<r使d(z,A∩B)>κ(d(z,A)+d(z,B))，右端换成max亦失败。
- **Definitions / Dependencies / Evidence**：[NG-CLOSED-REPAIR完整证明](research/canonical/topological_repair_obstructions.md#tr-intersection)；z=(t,0)有相交距离t、d(z,A)=0、d(z,B)≤t²，取0<t<r且κt<1。
- **Counterevidence / Scope / Related Files**：只排除闭性单独供应线性相交界；不构造历史fixed-E纤维/父层/1/3修补或Foran递归。距离不达直接复用C166，不计本Claim新结论。 外部新颖性未核。

<a id="c179"></a>
## C179-v1 / AW-FIXED-INPUT · 有限维宽闭图空间的一步可解薄性

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：固定E=R^d、d≥1，全部非空闭完整关系图配AW1距离函数拓扑。固定λ>0,p0∈E，{F:JλF(p0)≠∅}是Fσ第一纲集，补集稠密。另固定非空闭真S⊊E并在zerF=S的相对AW空间中取p0∉S，同样成立；每个有界输出紧切片的hit类相对闭且无处稠密。
- **Definitions / Dependencies / Evidence**：[AW1–AW9及完整证明](research/canonical/attouch_wets_fixed_input_thinness.md#aw-object)；定量有限网逼近误差≤2δ+2^(-R)，保留整个无界S锚、扰网点避输入切片与固定对角线、线性Lλ的完整AW同胚。证据为自足重建及独立逐式复算；源前身LF117–155与历史审查报告分开。
- **Counterevidence / Scope / Related Files**：固定S版本p0∈S时可解类为整个相对空间；预定可数步长的并仍第一纲，但存在任意实步长不能据不可数并推出。相对已良定算法子层也不能自动传薄性。未预设单值、满域、单调、收敛或Polish/Baire；不证明无限维AW、轨道理想、σ孔隙、统一常数或总体RLEB–LT–极大单调比较；C07动态报告仍独立未闭。全球先行性未核。

<a id="c180"></a>
## C180-v1 / UNIFORM-HOLDER-THINNESS · 精确固定集连续母层中的正 Hölder 薄性

- **Status**：`derived-checked`。
- **Exact Statement / Objects / Domain / Quantifiers**：固定有限维实赋范E、非空紧凸K且int_E K非空、非空闭真子集S⊊K且int_E(K\S)非空、非空𝔛={T∈C(K,K):FixT=S}，赋相对一致拓扑。非空S在请求的紧凸非空𝔛情形由Brouwer固定点定理推出，故明列不补额外对象限制。对全部固定α>0、0≤M<∞，全K全部对的M-Hölder-α块闭且无处稠密。所有正Hölder映射恰由H_(1/m,n)、m,n≥1可数耗尽，故第一纲；𝔛本身完全可度量/Baire，因此其补集稠密Gδ。
- **Explicit Interfaces / Conclusion**：同T、同K若存在0<γ≤1、0≤L<∞、R>0，使全部距离≤R的点对满足||2Tx−x−2Ty+y||≤L||x−y||^γ，则全域γ-Hölder预算可取max{(D^(1−γ)+L)/2,D/R^γ}，D=diamK。若同T全部点对满足||ΔT||²+τ||Δ(I−T)||²≤(1+ε)||Δx||²、τ,ε≥0，则T为√(1+ε)-Lipschitz。两种明定不等式的存在参数并类均在本𝔛第一纲。
- **Definitions / Dependencies / Evidence**：[UH1–UH14、UH-B及自足证明](research/canonical/uniform_holder_thinness.md#uht-object)；闭球位移δ、局部凸混合μρ值域余量、双cutoff、幅度预算和反三角cusp比值全部显式，兼容完备度量证明Baire门。来源05_obstruction_audit.md §7.1 LF400–404、§1 LF13–50、有限维门LF390；07_stage_synthesis.md B1 LF97–104。完整源枚举另见[专用审计](research/audit/UNIFORM_HOLDER_FULL_COVERAGE.md#uht-audit-source)。
- **Counterevidence / Scope / Related Files**：K=[−1,1],S=K的单点恒等层反驳删除离S开区域门；同K,S={0},e_0=2,e_n=0(n≥1)的共同尾层只有T=0，全部Hölder且在自身非第一纲，故不自动下传收敛/全时间/共同尾子层。未核全部无速率收敛类的类别、具体原生RLEB/LT认证类是否满足同图同域接口，也未授予AW/germ/变步长/极大单调总体比较、严格包含或比例。全球先行性和历史审查行为未核。
