# Claim Ledger · 精确身份与证据

本页的“稿内证明”指可阅读的证明文本，不代表全部已重新独立验真；“内部审计”也不是外部同行评审或优先权确认。对同一编号的量词、域、假设或结论作任何改变，须另立版本。依赖和合取关系见 [超边图](research/HYPERGRAPH.md)；原稿路径与版本见 [SOURCES.md](research/SOURCES.md)。C01–C08 保留初始身份；后续版本按新的精确对象逐项进入，历史同号不得直接合并。

## C01 · 全图 RL 的 Cayley 坐标

- **Exact Statement / Objects / Domain**：非空关系 \(F:H\rightrightarrows H\)，实 Hilbert 空间 \(H\)，\(\lambda,L>0\)，\(0<\gamma<1\)。在**每一对**图点 \((x,v),(y,w)\) 上有 \(\|(x-y)-\lambda(v-w)\|\le L\|(x-y)+\lambda(v-w)\|^\gamma\)，当且仅当 \(D=\{x+\lambda v:(x,v)\in\operatorname{gph}F\}\) 上 \(C(x+\lambda v)=x-\lambda v\) 良定且为 \(L\)-Hölder；反向图重建为 \(((p+C(p))/2,(p-C(p))/(2\lambda))\)。若 \(D=H\) 则图在**同一固定参数**下 maximal。
- **Dependencies / Evidence**：图点求和、求差和同输入唯一性；[9/23 TeX Lemma `cayley`](history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 直接给出双向证明。
- **Objections / Status / Scope**：代数事实，易复核；只说固定参数的 graph-maximal，绝不等同于极大单调；局部图块须重新声明量词。

## C02 · 9/18 局部 RLEB–PPA 收敛（原稿版本）

- **Exact Statement / Objects / Domain**：\(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，\(\lambda>0\)，非空闭 \(S\subset F^{-1}(0)\)，图块 \(\mathcal G\)、开域 \(U\)、\(0<\gamma\le1\)、\(L\ge0\)、\(R,\bar t>0\)，非减 \(\psi(0)=0\) 且原点连续，\(0<\kappa<1\)。A1：\(U_R\) 上局部 range coverage 且每个输入有图块中的最近零点；A2：\(\mathcal G\) 在尺度 \(R\) 满足 all-pairs RL；A3：实际输出上的 \(d(y,S)\le\psi(r_F(y))\) 及 gauge domain；A4：对 \(0<t\le R\)，\(\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t\)。初值还需 \(d_0\le R\) 和 \(\mathcal L(d_0)=\tfrac12[d_0/(1-\kappa)+Ld_0^\gamma/(1-\kappa^\gamma)]<\operatorname{dist}(x^0,X\setminus U)\)。
- **Conclusion**：唯一的**局部** \(J_{\mathcal G}\) 轨道无限继续、留域、有限长度、收敛到 \(S\) 中一点；\(d(x^k,S)\le\kappa^kd_0\)，且 \(\|x^\infty-x^k\|\le\tfrac12[\kappa^kd_0/(1-\kappa)+L\kappa^{\gamma k}d_0^\gamma/(1-\kappa^\gamma)]\)。允许多选择版本改用每个合法 transition 的共同 anchored 估计，不能把多值图与单值局部 \(J\) 混同。
- **Dependencies / Evidence**：C01 的局部形式、一步能量和 \(s\le(d+Ld^\gamma)/2\)、真实输出残差、A1–A4、归纳留域；[9/18 原投稿 ZIP 的 `sections/theorem_spine.tex`](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip)。
- **Objections / Status / Scope**：**有稿内证明及内部语义核对；本轮未重审全证明**。\(r_F\) 为全部输出纤维的 inf；没有额外证明 \(J_{\mathcal G}=J_{\lambda F}\) 时，不得把定理写成全算子完整 resolvent 结论。旧稿中的数值兼容常数不能代替实际收缩率。

## C03 · 全局双向 simultaneous shadow（9/23 候选）

- **Exact Statement / Objects / Domain**：C01 的实 Hilbert、非空全图全尺度 RL 假设。存在**一个**强单调双 Lipschitz homeomorphism \(A:H\to H\)，对**每个** \((x,v)\in\operatorname{gph}F\) 有 \(\|v-A(x)\|\le R/(\sqrt2\lambda)\)、\(\|x-A^{-1}(v)\|\le R/\sqrt2\)，\(R=L^{1/(1-\gamma)}\)。稿内还给 \(0<\sigma<1\) 的交叉估计与显式 Lipschitz/强单调常数，\(\sigma=\sqrt\gamma\) 取到所列半径，且因子 \(1/\sqrt2\) 是任意维数统一意义下最优；指定锚点版本改为另一问题、最优因子 1。
- **Dependencies / Evidence**：[9/23 TeX `thm:shadow`, `thm:sharpness`, `lem:crosslift`](history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 的 quadratic excess、orthogonal lifting、Banach contraction。匹配 PDF 21 页。
- **Objections / Status / Scope**：**有证明的研究稿候选，尚待独立数学深审**。全图 all-pairs 条件与 C02 的局部条件不同；不据此断言每个精确逆分支稳定，也不据此确定新颖性。

## C04 · 有限维完整纤维分类（9/23 候选）

- **Exact Statement / Objects / Domain**：固定 \(n\ge1\)、\(\lambda,L>0\)、\(0<\gamma<1\)，取 \(\mathbb R^n\) 上**固定这些参数**图极大的 RL 关系。集合 \(K\) 能作为某个这类关系的完整 \(F^{-1}(0)\)，当且仅当它非空、紧、\(\operatorname{diam}K\le R=L^{1/(1-\gamma)}\)；正向 \(F(0)\) 对应阈值 \(R/\lambda\)。量词是“每一个这样的 \(K\) 都存在某个 \(F\)”以及“每个这类 \(F\) 的纤维必要满足条件”，并非固定 \(F\) 可任意变换纤维。
- **Dependencies / Evidence**：C01、同常数的 Hölder Hilbert 扩张、有限维 proper map/degree 得全域纤维非空紧、`thm:fixedset` 的精确不动点实现；[9/23 TeX `thm:fibers`](history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex)。
- **Objections / Status / Scope**：**稿内证明候选**；不把有限维 compactness 移到一般 Hilbert，不把 graph-maximal 改成 maximal monotone。扩张和 fixed-set 的适用条件是独立审查重点。

## C05 · 原关系局部值域的有限数据拓扑证书（9/25 新增候选）

- **Exact Statement / Objects / Domain**：\(F:\mathbb R^n\rightrightarrows\mathbb R^n\)，完整闭非空零集 \(S=F^{-1}(0)\)；\(\lambda,L>0\)，\(0<\gamma<1\)，\(q\gamma>1\)，\(\kappa>0\)，\(\phi(r)=(r+Lr^\gamma)/2\)、\(c=\kappa\lambda^{-q}\)。指定的实际 proximal 对应 \(T(p)\) 在相关窗满足 \((p-y)/\lambda\in F(y)\)、\(\|p-y\|\le\phi(d(p,S))\)、\(d(y,S)\le c\|p-y\|^q\) **对每个** \(y\in T(p)\)。紧有限多面体 \(A\subset\operatorname{int}B\) 上 \(T\) upper semicontinuous、非空紧 Čech-\(\mathbb Q\)-acyclic 值；经验证有限样本定义的包络在 A／B 的 collar 满足 PDF (8.4)：\(\sup_Au_E\le u\)、\(\inf_{B\setminus\operatorname{int}A}g_E\ge m>0\)、\(\phi(u)<d(A,B^c)\)、\(\alpha=c\phi(u)^q<m\)。\(H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 对每个 j 满射，且 \(\chi(A)\ne0\)。
- **Conclusion**：\(B(0,(m-\alpha)/\lambda)\subset F(\operatorname{int}A)\)；更一般地，\(\sup_A\|h\|<(m-\alpha)/\lambda\) 的连续 \(h:A\to\mathbb R^n\) 有 \(x\in\operatorname{int}A\) 满足 \(h(x)\in F(x)\)、\(d(x,S)\le\kappa\|h(x)\|^q\)。
- **Dependencies / Evidence**：[9/25 PDF §8 Theorem 8.1](history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)，包络、Vietoris–Begle 与有理 morphism Lefschetz theorem 的稿内论证。[LIT-GRN-2002](research/LITERATURE.md#lit-grn-2002) 已逐项核一手 [6, Theorem 6.2] 的 retract、Vietoris span、紧 morphism \(\subset CAC\) 与 Lefschetz 数导入；这只关闭引文适用门。
- **Objections / Status / Scope**：**PDF-only 候选，整条新增模块尚未逐行独立审计**。全文明言它不从全图 RL 自动推出；有限观测不证明整窗 (8.1)–(8.2) 或 \(T\) 的存在、usc 和 acyclicity。稿件的紧度量值 Čech cohomology/homology 等价及其余包络推理继续按明示范围核，不因外部定理导入核验而自动升级 C05。

## C06 · 固定紧 T-only 图卡的内生观测

- **Exact Statement / Objects / Domain**：非空紧 \(K\subset\mathbb R^d\)，非空闭 \(S\subset K\)。令 \(X=\{T\in C(K,K):T|_S=I,\ T^n\to\Pi_T\text{一致},\Pi_T(K)\subset S\}\)，全时间度量 \(\rho(T,U)=\sup_{n\ge0}\|T^n-U^n\|_K\)。定义实际尾 \(w_n\) 为迭代后所有步差与到 \(S\) 距离的上确界，实际反射模 \(m_j=\sup_{\|x-y\|\le2^{-j}}\|(2T-I)x-(2T-I)y\|\)。则 \(\Phi:X\to c_0\times c_0\)，\(T\mapsto(w,m)\) 连续 proper；其实际像闭 Polish，非空精确纤维紧/Baire，映射到像 perfect/quotient。
- **Dependencies / Evidence**：[9/20 `06_math_audit.md` §1](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md) 的 Arzelà–Ascoli、共同尾预算及全时间收敛证明；内部独立审计。
- **Objections / Status / Scope**：**仅固定紧源完整 T-only、非空 X 条件下内部已审**；proper/quotient 不推出 category-preserving；局部 \(T\) 不代表完整全局 \(F\)。

## C07 · 原 Baire／多孔性比较量尺的塌缩报告

- **Exact Statement / Objects / Domain**：9/21 包报告在其先前定义的完整图 Polish／普通 \(C^0\) 与动力度量 \((X_D,d_{\rm dyn})\) 中，正 Hölder 类受共同粗糙化影响；特别 \(\mathcal R_D\subseteq\mathcal H_+\in\sigma\mathcal P^-(X_D,d_{\rm dyn})\)，所以 \(\mathcal R_D\setminus(\mathcal L_D\cup\mathcal M_D)\in\sigma\mathcal P^-\subseteq\sigma\mathcal P^+\)。\(\sigma\mathcal P^-\) 是包内的 σ-lower-porous 类。**域 \(D\)、全部图卡与孔隙常数须在原证明恢复后冻结，不由此摘要补造。**
- **Dependencies / Evidence**：[9/21 `02_VERIFIED_CORE.md` §6](history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md) 与 [`03_NO_GO_LEDGER.md` N05、N08、N10](history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)；v0.9 区分 V-A/V-B、SOURCE-MISSING。
- **Objections / Status / Scope**：**历史总账报告，尚非本仓库重构的原孔隙证明**；I-097–099 原审计和 I-102 正式表示稿未在盘点文件名中找到。总账另标 SOURCE-MISSING 的 I-001/I-002/I-003–005/I-059/I-075 已以原包或展开件恢复，但这不能替代 N10 原证明。旧目标“差集非 σ-upper-porous”只在其所指空间中被报告为假，不是所有合理量尺均失败。

## C08 · 解选择稳定性（修订身份）

- **Exact Statement / Objects / Domain**：一族在共同区域有轨道与统一尾界的 \(T\)，满足局部 \(\|Tx-Ty\|\le H\|x-y\|^\gamma\)，\(0<\gamma<1\)。若 \(\|T^kx-\Pi(x)\|\le M\sigma^k\) 对全体初值和 \(k\ge0\) 一致成立，则 \(\|\Pi(x)-\Pi(y)\|\le C(\log\log(1/\delta)/\log(1/\delta))^\beta\)，\(\beta=\log(1/\sigma)/\log(1/\gamma)\)；若统一尾界 \(M e^{-c_0\nu^k}\)，\(\nu>1\)，则是 \(C e^{-c(\log(1/\delta))^\alpha}\)，\(\alpha=\log\nu/\log(\nu/\gamma)\)，足够小 \(\delta=\|x-y\|>0\)。修订包给完整 proximal 的显式半代数例说明即使点误差 Q-二次，\(\Pi\) 也无需正阶 Hölder。
- **Dependencies / Evidence**：[原 `research_note.md` §1–4](history/sources/次单调论文研究/正式后的研究/research_note.md)，[修订审计 ZIP](history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)，9/21 `02_VERIFIED_CORE.md` §4。
- **Objections / Status / Scope**：**修订后内部数学审计**。一般 RLEB 推论只能直接用于局部 \(J_{\mathcal G}\)，或另加共同轨道区域 \(J_{\lambda F}=J_{\mathcal G}\)；旧稿无条件升级完整 resolvent 的版本已失效。固定解点的 anchored Hölder calmness 与邻域中任意两初值的 Hölder 连续性不同。

## C09 · 9/19 一般模 RL 的 Dini 点收敛（新增版本）

- **Exact Statement / Objects / Domain / Quantifiers**：\(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，非空闭 \(S\subset F^{-1}(0)\)，同图块 \(\mathcal G\)，\(U\) 开、\(R,\bar t,\lambda>0\)，连续非减 \(\omega:[0,R]\to[0,\infty)\)、\(\omega(0)=0\)、非减原点连续 \(\psi\)、\(0<\kappa<1\)。对**每个** \(x\in U_R\) 假设图块输入覆盖与最近解点 \((p,0)\in\mathcal G\)；对**每对**图点在输入尺度 \(R\) 有 \(\|\Delta u-\lambda\Delta v\|\le\omega(\|\Delta u+\lambda\Delta v\|)\)；在全部实际输出有真实 \(r_F\) EB；\((R+\omega(R))/(2\lambda)\le\bar t\)；对每个 \(0<t\le R\) 有 \(\psi((t+\omega(t))/(2\lambda))\le\kappa t\)；且 \(\int_0^R\omega(t)dt/t<\infty\)。
- **Conclusion**：若 \(d_0\le R\) 且 \(d_0/[2(1-\kappa)]+\frac12\sum_{j\ge0}\omega(\kappa^jd_0)<d(x^0,X\setminus U)\)，则唯一图块轨道全程存在、有限长并收敛于 \(S\)；\(d_k\le\kappa^kd_0\)，步长与尾界按同一模级数。量词不自动覆盖完整 \(J_F\)。
- **Dependencies / Evidence / Objections / Status / Related Files**：R01 一步估计的一般模版、Dini 等价几何采样求和、闭 \(S\) 与留域归纳；[rleb_ppa](research/rleb_ppa.md)、[holder_structure H04](research/holder_structure.md)。9/19 S19 extensions_moduli_structure.tex 的 thm:modulus-dini 稿内证明，本轮局部重算。C02 是幂次版，C09 改变模与额外条件，不能覆盖旧编号。

## C10 · 完整对数接缝的 Dini 边界

- **Exact Statement / Objects / Domain / Quantifiers**：对**每个** \(a>0\)，\(\ell_a(0)=0\)，在 \(0<t\le e^{-a}\) 为 \([\log(e/t)]^{-a}\)，以后用接点切线延伸。\(F_a(\xi,y)=\{(-\ell_a(4y),3y),(-\ell_a(4y),-5y)\}\) 当 \(y\ge0\)，其余空。步长 1，\(S=\mathbb R\times\{0\}\)。
- **Conclusion**：完整 \(J_a(p,q)=(p+\ell_a(|q|),|q|/4)\)，整图有非幂次模 \(\Omega_a(t)=\sqrt{(t+2\ell_a(t))^2+9t^2/4}\) 且真实残差 \(r_{F_a}(\xi,y)=\sqrt{\ell_a(4y)^2+9y^2}\)。对每个 \(|q_0|>0\) 距离按 \(4^{-k}\) 收缩，轨道有限长且收敛于一点当且仅当 \(a>1\)；若 \(a\le1\)，切向坐标趋 \(+\infty\)。
- **Dependencies / Evidence / Objections / Status / Related Files**：完整双支反演、全对模、对数级数判别；S19 thm:logarithmic-seam，[holder_structure H04](research/holder_structure.md)。稿内证明且本轮核了关键公式。必要性只对**此族**，不是“非 Dini 必发散”的一般断言。

## C11 · 统一尾给连续极限回缩

- **Exact Statement / Objects / Domain / Quantifiers**：C09 整套局部假设在 \(U_R\) 成立，置 \(\ell_\omega(r)=r/[2(1-\kappa)]+\frac12\sum_{j\ge0}\omega(\kappa^jr)\)，\(\mathcal O=\{x\in U:d(x,S)<R,\ell_\omega(d(x,S))<d(x,X\setminus U)\}\)。
- **Conclusion**：\(\mathcal O\) 开且正向不变，包含 \(S\cap U\)；每个 \(x\in\mathcal O\) 的极限 \(\Pi(x)\) 构成连续回缩 \(\mathcal O\to S\cap U\)，所以 \(S\cap U\) 为 Euclidean neighborhood retract，并满足原稿所述局部收缩性。
- **Dependencies / Evidence / Objections / Status / Related Files**：C09 的统一尾、全对输入连续性和精确长度递推；S19 prop:limit-retraction，[holder_structure H05](research/holder_structure.md)。稿内证明及局部重算。C04 的任意紧零集实现未附 C11 假设；Cantor 型零集不能在相应点满足整套条件。

## C12-v0 / C12-v1 · 随机推论的度量版本

- **Original exact statement C12-v0**：S19 thm:stochastic-rleb 取 \((\mathsf X,d)\) “Polish”、闭 \(S\)、适应过程留在 \(0\le D_k\le R\) 的不变域、非减 Dini \(\omega\)、\(0<\kappa<1\)，逐路径 \(s_k\le(D_k+\omega(D_k))/2\) 和 \(\mathbb E[D_{k+1}\mid\mathcal F_k]\le\kappa D_k\)。结论 \(\sum s_k<\infty\) 且 \(X_k\to X_\infty\in S\) 几乎处处。
- **Counterevidence / Status**：若 Polish 只保证拓扑可完备，结论**错误**。\((0,2)\) 的通常距离、闭 \(S=\{2^{-n}\}\)、确定性 \(X_k=2^{-(k+2)}+4^{-(k+2)}\)、\(\omega(t)=4\sqrt t\)、\(R=1/16,\kappa=1/4\) 满足前件而 \(X_k\to0\notin\mathsf X\)。求和部分不受影响。[FAILED F07](FAILED_ROUTES.md)。
- **Repaired exact statement C12-v1**：同对象、过程与逐路径/条件期望量词，另明示**给定度量 \(d\) 完备**（可要求 complete separable metric space）。则原求和证明加 Cauchy 与闭 \(S\) 得全部结论。本轮推导修补，尚未改原稿。不得把 v0 的假设悄悄写成 v1。[holder_structure H06](research/holder_structure.md)。

## C13 · 冻结面 CRSC 与 MSCQ（锥旁支）

- **Exact Statement / Objects / Domain / Quantifiers**：有限维 \(X,E\)、闭尖满维 nice 凸锥 \(C\)、\(C^1\) 映射 \(G\) 在 \(\bar x\) 满足 \(G(\bar x)=0\)。设 \(A=DG(\bar x)\)，\(F=F_{\min}(\operatorname{Im}A\cap C)\)，\(H=F^\perp\)，\(S_{\mathrm{dual}}=\operatorname{span}(C^*\cap F^\perp)\)。假设 \(A^*C^*\) 闭、\(\operatorname{rank}(DG(x)^*|_H)\) 在完整邻域恒定，且参考面 \(F\) amenable；保留原包的闭像与常秩局部条件。
- **Conclusion**：冻结秩夹逼使面稳定，经共同法向流形与切向修正，存在邻域和 \(\kappa<\infty\)，对其中每个 \(x\) 有 \(d(x,G^{-1}C)\le\kappa d(G(x),C)\)。对固定 proper nice 锥，“每个在顶点冻结 CRSC 的 \(C^1\) 系统均 MSCQ”与 amenability 等价；逆向测试是各面的线性嵌入。
- **Dependencies / Evidence / Objections / Status / Related Files**：[cone_markov §1](research/cone_markov.md)，S14C 主稿及 CM-C 证明包。内部审计与承重步骤重读；正式版文献和退化常数分支待独立核。该锥距离残差不是 \(r_F\)，不能自动迁移 RLEB。

## C14 · 紧 Markov 同步残差的 exact-zero 门槛

- **Exact Statement / Objects / Domain / Quantifiers**：紧状态集 \(G\subset\mathbb R^d\)，满足 CM-M §1 的 a.e. 连续联合可测随机自映射，独立新噪声定义核 \(P\)，不变律集合 \(\mathcal I\ne\varnothing\)。\(\Psi(\mu)^2=\inf_{\pi\in\mathcal I}\inf_{\eta\in\operatorname{Opt}_{W_2}(\mu,\pi)}\int\mathbb E\|(x-T_\xi x)-(y-T_\xi y)\|^2d\eta\)；两侧**同噪声**，内层必须为该两边缘的平方成本最优耦合。
- **Conclusion**：在该紧连续设置下，极小值取得、\(\Psi\) 下半连续，且 \(\Psi^{-1}(0)=\mathcal I\) 当且仅当存在严格一般 gauge \(\rho\) 使 \(d_{W_2}(\mu,\mathcal I)\le\rho(\Psi(\mu))\) 对每个概率律成立。没有自动幂次或速率兼容。
- **Dependencies / Evidence / Objections / Status / Related Files**：紧性与零集包络，CM-M Theorem 1，[cone_markov §2](research/cone_markov.md)。内部证明包和本轮关键定义核读；\(\Psi\) 表示依赖，不是 \(W_2(\mu,\mu P)\)。

## C15 · 固定有限状态的顶点判定

- **Exact Statement / Objects / Domain / Quantifiers**：固定有限状态几何、随机映射与概率，C14 的同一 \(\Psi\)；枚举最优运输对偶 tight-edge 图产生的有限计划多面体，令 \(\mathcal V\) 为全部顶点，\(E(\mu)=d_{W_2}(\mu,\mathcal I)^2\)，\(R\cdot v\) 为同步残差成本。
- **Conclusion**：\(\Psi^{-1}(0)=\mathcal I\) 当且仅当每个 \(v\in\mathcal V\) 且 \(R\cdot v=0\) 的行边缘在 \(\mathcal I\)，当且仅当存在 \(B<\infty\) 对**所有**律有 \(E(\mu)\le B\Psi(\mu)^2\)；最佳平方系数为 \(\max_{v:R\cdot v>0}E(r(v))/(R\cdot v)\)，空集最大值 0。
- **Dependencies / Evidence / Objections / Status / Related Files**：CM-M Theorem F、有限 LP 对偶分支与凸性；[cone_markov CM-FINITE](research/cone_markov.md)。内部证明包；只针对固定有限数据，不承诺多项式算法或无限状态推广。

## C16 · 匹配公共接口下的 LT→RLEB 能量证书

- **Exact Statement / Objects / Domain / Quantifiers**：有限维完整原图且全域单值 \(T=J_{\lambda F}\)，同一目标 \(S\)、同一 coverage/测试域/真实残差和留域接口；公共 all-pairs LT 假设 \(\operatorname{Lip}(2T-I)\le\sqrt{1+4\tau}\)、\(d(u,S)\le\rho r_F(u)\) 和 \(2\tau(\lambda+\rho)^2<\lambda^2\)。
- **Conclusion**：在此接口中取 \(\gamma=1,L^2=1+4\tau,\psi(t)=\rho t\)，能量分支的 \(q_E=(1+2\tau)\rho^2/(\rho^2+\lambda^2)<1\)，故公共 LT 证书类包含于相应 RLEB 能量证书类。不是完整 LTT 框架全部版本的包含，也不保存最佳常数或最大域。
- **Dependencies / Evidence / Objections / Status / Related Files**：R03 的能量式及归一化代数，[operator_space §2](research/operator_space.md)，S20 OS-H §3.2。内部证明；不推出两类在自然母空间的大小差异。

## C17 · 固定紧 T-only 图卡的 proper \(\Phi\)（C06 的范围细化）

- **Exact Statement / Objects / Domain / Quantifiers**：C06 的非空固定紧 \(K\)、闭 \(S\subset K\) 和全时间度量空间 \(X\)；尾 \(w_n\) 同时看所有 \(k,\ell\ge n\) 的迭代差与到 \(S\) 距离，反射模 \(m_j\) 看输入尺度 \(2^{-j}\) 的 \(2T-I\)。
- **Conclusion**：\(\Phi=(w,m):X\to c_0^2\) 连续 proper，像闭 Polish，非空精确纤维紧；这与 C06 同一数学身份，是释义细化，**不另造较强定理**。
- **Dependencies / Evidence / Objections / Status / Related Files**：[operator_space §3](research/operator_space.md)，S20 OS-A §1。Arzelà–Ascoli 需紧参数集在 \(c_0\) 中的一致趋零预算；proper/quotient 不推出 category-preserving，局部图卡不恢复完整全局 \(F\)。

## C18 · 有限维固定窗口的全纤维值域覆盖

- **Exact Statement / Objects / Domain / Quantifiers**：\(F\) 为 \(\mathbb R^n\) 上固定 \((\lambda,L,\gamma)\)、\(0<\gamma<1\) 的全局 graph-maximal RL 关系，取任一图锚 \((x_0,v_0)\)，\(R=L^{1/(1-\gamma)}\)。对任意 \(r>R\)，唯一 \(h(r)\in(0,r)\) 解 \(r-h=L(r+h)^\gamma\)。
- **Conclusion**：对每个 \(v\in B(v_0,h(r)/\lambda)\)，完整 \(F^{-1}(v)\ne\varnothing\) 且整个纤维包含于 \(B(x_0,r)\)，从而该输出球包含于 \(F(B(x_0,r))\)。相对 maximal 窗口 \(G\subset U\times W\) 在原稿的锚、开球包含和 \(s>0\) 条件下，半径变为 \(\min\{s,h(r)/\lambda\}\)；统一半径及严格 \(r>R\) 在一维反例下锐。
- **Dependencies / Evidence / Objections / Status / Related Files**：C04 的有限维 properness/full range、标量最大根 \(\rho\)、同常数 completion 和相对 maximal 的窗口等式。[range_finite_data W01](research/range_finite_data.md)，S23 lem:rho/thm:coverage/thm:window/prop:coveragesharp。稿内证明与本轮关键计算核读；不是任意非 maximal 子图的 coverage，亦与 S25 的有限观测局部值域不同。

## C19 · 有限样本的全局一致二次规划影子

- **Exact Statement / Objects / Domain / Quantifiers**：有限 \(m\ge1\) 个 \(\mathbb R^n\) 图样本，\(p_i=x_i+\lambda v_i,c_i=x_i-\lambda v_i\)，固定 \(0<\sigma<1\) 和 S23 的 \(M_\sigma,a^2=M_\sigma/2\)。对所有样本对有 \(\|c_i-c_j\|^2\le\sigma^2\|p_i-p_j\|^2+M_\sigma\)。按 S23 (6.3)–(6.6) 的 \(Q,d(q),\Delta_m\) 定义唯一 QP 最小解 \(\theta(q)\) 与 \(N_m(q)=V\theta(q)\)。
- **Conclusion**：同一个 \(N_m:\mathbb R^n\to\mathbb R^n\) 全局 \(\sigma\)-Lipschitz，对每个 \(i,q\) 有 \(\|c_i-N_m(q)\|^2\le\sigma^2\|p_i-q\|^2+a^2\)；其 Cayley 代理 \(A_m\) 为强单调双 Lipschitz 同胚，对全部**样本点**有统一正反误差。对未知原图点还须 C20 的参数 coverage。
- **Dependencies / Evidence / Objections / Status / Related Files**：严格凸 QP、正交抬升、变分不等式、同一性 contraction。[range_finite_data Q01](research/range_finite_data.md)，S23 thm:finite_qp。稿内证明及关键代数核读；全球定义的代理不等于全球认证原关系。

## C20 · 参数覆盖与三项可认证误差

- **Exact Statement / Objects / Domain / Quantifiers**：C19 样本来自完整或明确图块 RL，未知图点 \(p=x+\lambda v\) 到样本参数集距离至多 \(\delta\ge0\)，\(b=L\delta^\gamma\)，\(K_\delta\) 为 S23 (6.7) 的显式正根上界。对某一非空完整纤维要求它的**每个图点**参数满足该 coverage；对反演目标 \(v\) 的观测 \(\widetilde v\) 有 \(\|\widetilde v-v\|\le\eta\)，代理求值 \(\widehat x\) 有已认证误差 \(e\)。
- **Conclusion**：每个被覆盖图点有 \(\lambda\|v-A_m(x)\|,\|x-A_m^{-1}(v)\|\le K_\delta\)；覆盖整个纤维才得对应 Hausdorff singleton 界。对每个 \(x\in F^{-1}(v)\)，\(\|x-\widehat x\|\le K_\delta+\lambda(1+\sigma)\eta/(1-\sigma)+e\)。可行 QP 解的 Frank–Wolfe gap \(G\) 给 \(\|V\widehat\theta-N_m(q)\|\le\sqrt G\)，浮点 gap 需验证容差。
- **Dependencies / Evidence / Objections / Status / Related Files**：C19、原图 Hölder、同输入/同输出交叉估计、逆代理 Lipschitz 常数。[range_finite_data Q02/Q03](research/range_finite_data.md)，S23 thm:covered、cor:coveredfibers、prop:evaluation、cor:totalerror。稿内证明；\(\delta\)-网的获得和维数复杂度不在定理自动保证内。

## C21 · 有限总查询的全空间信息障碍

- **Exact Statement / Objects / Domain / Quantifiers**：\(n\ge1,L>0,0<\gamma<1\)。对**任何**仅有限次（可自适应）点查询未知全局 \(L\)-Hölder \(C:\mathbb R^n\to\mathbb R^n\)、随后输出单值 \(A\) 且不再访问 oracle 的确定性程序，存在允许的 \(C\) 使 \(A\) 对其 RL 关系没有全空间统一有限正向纤维误差。
- **Dependencies / Evidence / Counterevidence / Status / Related Files**：零图的有限查询集 \(E\) 与 \(C_1(p)=L d(p,E)^\gamma e\) 给同 transcript 而远端偏差无界。[range_finite_data Q04](research/range_finite_data.md)，S23 prop:information。稿内反例与本轮推理核读。结论不覆盖固定紧域、持续 oracle、随机保证或已知解析映射；它是精确查询模型的障碍。

## C22-v1 / RP-EB · 有限维不一致二次近端的条件律误差界

- **Exact Statement / Objects / Domain / Quantifiers**：固定有限维欧氏空间 \(H\)、有限个正权重 \(p_i\)、\(\lambda>0\)，每支 \(T_i=\operatorname{prox}_{\lambda f_i}\)，其中 \(f_i(x)=\langle x,H_i x\rangle/2-\langle b_i,x\rangle\)、\(H_i=H_i^*\succeq0\)、\(b_i\in\operatorname{range}H_i\)。逐步使用与当前状态独立、同分布的新索引。令 \(U=\cap_i\ker H_i,V=U^\perp\ne\{0\}\)；在 \(V\) 上 \(A_i=(I+\lambda H_i)^{-1}\)、\(c=\sqrt{\lambda_{\max}(\sum_i p_i A_i^*A_i|_V)}<1\)。对**每一个固定** \(\nu\in\mathscr P_2(U)\) 和**所有**守恒边缘为 \(\nu\) 的 \(\mu\in\mathscr M_\nu\)，用同一条件距离 \(\mathsf W_\nu^2=\int W_2(\mu_u,\eta_u)^2d\nu\) 及**完整混合核** \(P\) 的真实 law-step 残差 \(\mathcal R_\nu(\mu)=\mathsf W_\nu(\mu,\mu P)\)。
- **Conclusion**：活跃核有唯一 \(\pi\in\mathscr P_2(V)\)，所有联合有限二阶矩不变律恰为 \(\{\nu\otimes\pi:\nu\in\mathscr P_2(U)\}\)。置 \(E_\nu(\mu)=\mathsf W_\nu(\mu,\nu\otimes\pi)\)，则 \((1-c)E_\nu\le\mathcal R_\nu\le(1+c)E_\nu\)，\(E_\nu(\mu P^k)\le c^kE_\nu(\mu)\)，且 \(\sum_{k\ge0}\mathsf W_\nu(\mu P^{k+1},\mu P^k)\le\mathcal R_\nu(\mu)/(1-c)\)。
- **Definitions / Dependencies / Evidence**：[规范证明 RP-OBJECT→RP-GAP→RP-CONTRACTION→RP-EB](research/canonical/random_proximal.md#rp-eb) 给矩阵谱隙、同步耦合、不变律分类和三角不等式。9/14 [历史相关性感知报告](research/canonical/random_proximal.md#rp-object) 是来源线索；本轮重算关键步骤。标量子族证明统一 EB 系数 \(1/(1-c)\) 的类内尖锐性。
- **Counterevidence / Objections / Status / Scope / Related Files**：本轮推导 `derived-checked`，未核外部优先权。不能把 \(\mathcal R_\nu\) 换成逐支推前残差、同步 OT 缺陷、物理步长或普通联合 \(W_2\) 的同名量词。\(V=0\)、无限维、权重或参数随守恒坐标变化均是新版本义务。历史脚本运行仅属有限观察；精确路径和输出在[审计](research/audit/SOURCE_RECONSTRUCTION_AUDIT.md)。

## C23-v1 / RP-BRANCH · 分支残差的零集边界

- **Exact Statement / Objects / Domain / Quantifiers**：有限个 firmly nonexpansive \(S_i:H\to H\)，每支有固定点，所有 \(p_i>0\)；对**每一个** \(\mu\in\mathscr P_2(H)\)，\(\sum_i p_i W_2(\mu,(S_i)_\#\mu)^2=0\) 当且仅当 \(\mu(\cap_i\operatorname{Fix}S_i)=1\)。\(H\) 是有限维欧氏空间；该命题不要求 \(S_i\) 为同一个目标的近端。
- **Dependencies / Evidence**：firm nonexpansiveness 的定点平方不等式，分别积分并利用有限二阶矩与推前律相等。[规范证明](research/canonical/random_proximal.md#rp-branch)；标量不一致双近端给混合不变律存在而分支残差严格正的实例。
- **Counterevidence / Status / Scope / Related Files**：本轮 `derived-checked`；对象是逐支残差的零集，不能推出混合核不变律的零集判据。若取消每支固定点或换成同步缺陷，必须另立版本。[反例与尖锐例](research/canonical/random_proximal.md#rp-scalar)。历史 C11 复合次正则与现 C11 回缩同号，均不得占用 C22/C23 身份。

## C24-v1 / EX01 · 旋转 resolvent 收缩不蕴含强单调

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R^2\) 取 \(K(x_1,x_2)=(-x_2,x_1)\)，固定任意 \(\omega,\lambda>0\)，\(F=\omega K\)。完整 \(J_{\lambda F}=(I-\lambda\omega K)/(1+(\lambda\omega)^2)\) 在全空间的 Lipschitz 常数为 \((1+(\lambda\omega)^2)^{-1/2}<1\)，但 \(\langle x-y,Fx-Fy\rangle=0\) 对**全部** \(x,y\) 成立，故无正强单调常数。反射 \(2J-I\) 是等距映射，固定步长全图 RL \(\gamma=1\) 的锐常数为 1；任意 \(0<\gamma<1\) 的无界全图 RL 无有限常数。
- **Definitions / Dependencies / Evidence**：完整原图、同一步长及全对尺度；直接矩阵反演和正交范数计算，见[规范例卡 EX01](research/canonical/example_atlas.md#ex01)，历史别名 GX-004。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；只否定没有额外假设的 “完整 J 严格收缩 ⇒ F 强单调”。\(r_F(x)=\omega\|x\|\) 的真 EB 与此失败并存；变步长或有界尺度必须另标范围。

## C25-v1 / EX02 · 正紧对角的任意趋零 gauge 障碍

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(H=\ell^2\)，\((Fx)_n=x_n/n\) 满域，\(S=\{0\}\)、\(r_F(x)=\|Fx\|\)。对**任意** \(\psi:[0,\varepsilon)\to[0,\infty)\) 满足 \(\psi(t)\to0\) 当 \(t\downarrow0\)，**不存在** \(C,\delta>0\) 使 \(\|x\|\le C\psi(r_F(x))\) 对所有 \(\|x\|<\delta\) 成立。与此同时 \(F\) 严格单调、1-cocoercive、极大单调；每个固定 \(\lambda>0\) 的完整 PPA 对每个初值强收敛到 0，但每个有限迭代的算子范数 \(\|J_{\lambda F}^k\|=1\)。
- **Dependencies / Evidence**：固定 \(0<t<\delta\) 用 \(x=te_n\) 让真残差 \(t/n\to0\)；逐坐标乘子 \(n/(n+\lambda)\) 及受控尾部证明逐点收敛。[规范例卡 EX02](research/canonical/example_atlas.md#ex02)，历史别名 GX-009。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；无限维尾方向是障碍，有限维截断不属于同一 Claim。没有统一 EB 不推出某条特定轨道不收敛；也不反驳加闭值域等前提后的命题。

## C26-v1 / EX03 · 三次映射的三种精确模

- **Exact Statement / Objects / Domain / Quantifiers**：\(F:\mathbb R\to\mathbb R, F(x)=x^3\)，\(S=\{0\},r_F(x)=|x|^3\)。固定目标 \(q=1/3\) EB 对全部 \(x\) 恒等且最佳常数 1；两变量 \(|x-F^{-1}(y)|\le2^{2/3}|Fx-y|^{1/3}\) 对全部 \(x,y\) 成立，且最佳局部和全局常数均 \(2^{2/3}\)。对每个固定 \(\lambda>0\)，算法残差 \(G_\lambda=I-J_{\lambda F}\) 的固定目标 \(q=1/3\) **局部常数下确界**为 \(\lambda^{-1/3}\)，但该值在任何含非零邻点的固定邻域不取到。
- **Dependencies / Evidence**：\(4(a^2+ab+b^2)-(a-b)^2=3(a+b)^2\ge0\) 且 \(a=-b\) 取等；\(p=u+\lambda u^3\) 直接算 \(G_\lambda(p)=\lambda u^3\)。见[规范例卡 EX03](research/canonical/example_atlas.md#ex03)，历史别名 GX-021。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；\(F\)、\(G_\lambda\) 与 \(\eta F\) 是不同观察对象。固定目标与移动目标的常数不能互换；\(q<1\) 的逆 Hölder 不等于普通 Lipschitz 强正则。原卡其他属性尚未逐项重写。

## C27-v1 / PD-STEP · 固定同图换步的单射门

- **Exact Statement / Objects / Domain / Quantifiers**：固定 Hilbert 关系的指定图块 \(\Gamma\)，若在 \(\lambda>0\) 下全对 RL 使旧 Cayley \(C:D_\lambda(\Gamma)\to H\) 良定，对**任意指定**新步长 \(\eta>0\) 置 \(t=\eta/\lambda,\alpha=(1+t)/2,\beta=(1-t)/2\) 与 \(Q=\alpha I+\beta C\)。新 Minty 输入域恰为 \(Q(D_\lambda)\)；相同图块在新步长具有单值 Cayley **当且仅当** \(Q\) 单射，此时 \(C_\eta=(\beta I+\alpha C)\circ Q^{-1}\)。若旧 \(C\) 为 \(L\)-Lipschitz 且 \(m=\alpha-|\beta|L>0\)，新映射在新自然域的 Lipschitz 常数至多 \((|\beta|+\alpha L)/m\)。
- **Dependencies / Evidence**：同一图点的正反射二坐标线性变换，矩阵行列式 \(t>0\)；下界 \(\|\Delta Q\|\ge m\|\Delta x\|\)。[PD-STEP 证明及尖锐反例](research/canonical/parameter_dictionary.md#pd-step)；历史 GX-015 只作来源别名。
- **Counterevidence / Status / Scope / Related Files**：`derived-checked`；\(C(s)=\operatorname{sgn}(s)|s|^\gamma\) 表明 \(\eta>\lambda\) 可折叠，\(\eta<\lambda\) 可变 Lipschitz 且失去所有全局次线性指数。即使单射，另须核新目标输入的 coverage；这不是对不同关系缩放或取逆的陈述。

## C28-v1 / PD-TIED · 线性 RL 与 tied 双参数的精确等价

- **Exact Statement / Objects / Domain / Quantifiers**：固定同一图块、步长 \(\lambda>0\)、全部指定配对及其尺度，\(L\ge0\)，\(a=u-u',b=v-v'\)。对每一对，\(\|a-\lambda b\|\le L\|a+\lambda b\|\) 当且仅当 \(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\)，其中 \(\theta=(1-L^2)/(2(1+L^2)),\mu=\theta/\lambda,\rho=\lambda\theta\)。有限 \(L\ge0\) 的精确范围为 \(-1/2<\theta\le1/2\)，上端 \(L=0\) 被包含。
- **Dependencies / Evidence / Status**：平方展开、分母正性及反向同一步；[PD-TIED](research/canonical/parameter_dictionary.md#pd-tied) 直接证明，`derived-checked`。若 \(L>1\)，\(\mu,\rho<0\) 不可删负项；完整独立二参数类不等同这条 tied 曲线。命名和先行性另核。

## C29-v1 / PD-SCALE · 有界降指数与无界反向障碍

- **Exact Statement / Objects / Domain / Quantifiers**：固定同一 Cayley 输入域 \(D\)、同一 \(C:D\to H\)。若 \(\operatorname{diam}D\le\Delta<\infty\)，\(0<\gamma_1\le\gamma_2\le1\) 且 \(C\) 是 \((L_2,\gamma_2)\)-Hölder，则它在同一域是 \((L_2\Delta^{\gamma_2-\gamma_1},\gamma_1)\)-Hölder。无界 \(D\) 上没有这条一般包含：\(C(s)=s\) 的更小指数全局失败；\(C(s)=\operatorname{sgn}(s)|s|^\gamma\) 在零点对更大指数、无穷远对更小指数失败。
- **Dependencies / Evidence / Counterevidence / Status**：尺度幂代数及相反数给凹幂的全局锐常数 \(2^{1-\gamma}\)，见[PD-SCALE](research/canonical/parameter_dictionary.md#pd-scale)；`derived-checked`。单点域真空，局部下界配对只给远离对角线的估计，不冒充邻域 Lipschitz。

## C30-v1 / PD-RESIDUAL · 完整最小残差的推理方向

- **Exact Statement / Objects / Domain / Quantifiers**：任意关系 \(F\) 的非空零集 \(S\)，\(r_F(u)=\inf_{v\in F(u)}\|v\|\)，固定合法步 \(x=u+\lambda v\)。总有 \(r_F(u)\le\|v\|\)。若 \(\psi\) 非减，**已有**对实际输出的 \(d(u,S)\le\psi(r_F(u))\) 才可推出 \(d(u,S)\le\psi(\|v\|)\)；反向不成立。若对该纤维**每个** \(v\) 有 \(d(u,S)\le\kappa\|v\|^q\)，\(q>0\)，取 inf 可得真残差幂 EB；一般非减 gauge 需额外右连续性或实际下确界可取。
- **Dependencies / Evidence / Counterevidence / Status**：infimum 定义及趋近序列；\(F(u)=\{u,u^2\}\) 选 \(v=u\) 时有选中值线性界，而在零附近 \(r_F(u)=u^2\) 不支持真线性 EB。[PD-RESIDUAL](research/canonical/parameter_dictionary.md#pd-residual)，`derived-checked`。零点、输出窗口与空纤维约定随新问题重新固定；不能从算法步长推回完整图条件。

## C31-v1 / PA-WHOLE · 合法块收缩与整条轨道

- **Exact Statement / Objects / Domain / Quantifiers**：X=R^n，非空闭 S、开 V、块长 m、半径 r,η>0；对每个 V 中距离 S≤r 的块起点、每个合法前缀和每个允许转移，都有可延拓合法词及非减前缀距离界 D_{w,j}、步位移界 G_{w,j}。所有 w,j<m,t∈[0,r] 有 D_{w,j}(t)<η；统一终点包络 Θ(t)=sup_w D_{w,m}(t)≤κt，0≤κ<1；统一块位移 G(t)=sup_w Σ_j G_{w,j}(t) 满足 H(t)=Σ_{q≥0} G(κ^q t)<∞。
- **Conclusion / Scope**：若 x₀∈V、d₀≤r 且 H(d₀)<dist(x₀,X\V)，每条合法轨道都可无限延拓并留在 V，块端点 d(x_{qm},S)≤κ^q d₀，整轨道总长≤H(d₀)，收敛到 S 中一点。量词为每条实际选择，不是存在一条。
- **Definitions / Dependencies / Evidence**：[PA-DEF、PA-WHOLE 完整证明](research/canonical/path_atlas.md#pa-whole)；闭 S、指定度量完备、实际前缀 coverage、统一可求和预算。状态 derived-checked；由 9/09 札记重新推导，外部先行性未核。
- **Counterevidence / Objections / Related Files**：终点收缩不管中间留域；非平凡周期不满足可求和步长。原札记周期推论不能作为本 Claim 的推论。[F12](FAILED_ROUTES.md#f12)。M1 特定捕获半径未独立重建。

## C32-v1 / PA-POWER · 无限合法词的统一性门

- **Exact Statement / Objects / Domain / Quantifiers**：固定 m，对每个合法词 w=(σ₀,…,σ_{m−1}) 逐边有 d_{j+1}≤c_{σ_j}d_j^{α_{σ_j}}，正系数与正指数。则 d_m≤C_w d₀^{A_w}，其中 A_w=Π_j α_{σ_j}，C_w=Π_j c_{σ_j}^{Π_{ℓ>j}α_{σ_ℓ}}。有限词集的全体 A_w>1 给共同小半径；无限词集的充分条件是 inf_w A_w>1 与 sup_w C_w<∞，才可对预设 0<κ<1 给统一小半径收缩。
- **Dependencies / Evidence / Status**：逐次代入及 m=1、A_j=1+1/j、C_j=1 的反例见 [PA-POWER](research/canonical/path_atlas.md#pa-power)；状态 derived-checked。
- **Counterevidence / Scope**：A_w<1 只说明分离上界不能证收缩；联合路径仍可能有限捕获。A_w=1 还要统一控制 C_w。[F12](FAILED_ROUTES.md#f12)。

## C33-v1 / PA-CYCLES · 相位极限独立陈述

- **Exact Statement / Objects / Domain / Quantifiers**：确定性周期映射 T₀,…,T_{m−1}；C=T_{m−1}∘⋯∘T₀，P_j=T_{j−1}∘⋯∘T₀。若某初值另已证 C^q x₀→x̄₀∈Fix C，且每个 P_j 在 x̄₀ 连续，则 x_{qm+j}→P_j x̄₀；整轨道收敛当且仅当这些相位极限相等。
- **Dependencies / Evidence / Status / Related Files**：[PA-CYCLES](research/canonical/path_atlas.md#pa-cycles) 直接使用连续性；状态 derived-checked。T(x)=1−x 有 Fix T²≠Fix T，表明块固定点不是原算法固定点。该命题不由 C31 的有限总长定理推出。[F12](FAILED_ROUTES.md#f12)。

## C34-v1 / CS-TRANSFER · 局部目标集合一致性

- **Exact Statement / Objects / Domain / Quantifiers**：有限连续 f:ℝⁿ→ℝ；在 B_α(x̄) 有 f≥f(x̄)，且每个 Γ=zer ∂f 中 B_ς(x̄) 的点满足 f(y)≤f(x̄)。指定 S⊆Γ 且包含全部局部极小点。对每个 0<R<min(α,ς) 及每个 x∈B_{R/4}(x̄)，d(x,S)=d(x,Γ)=d(x,{f≤f(x̄)})。
- **Dependencies / Evidence / Status**：局部三集合一致、球外距离隔离、Fermat 及局部极小的二阶必要条件；[CS-TRANSFER](research/canonical/composite_subregularity.md#cs-transfer) 完整证明。状态 derived-checked；历史复合 C11 是来源别名，与现 C11 不同。
- **Counterevidence / Scope**：S 若随意缩小到一个零点，f(x,y)=x² 即失败；仅 x̄∈Θ₂ 不替代局部最小，f=−x⁴ 为反例。目标集合的身份先于残差界。

## C35-v1 / CS-EB · 满行秩复合真实残差界

- **Exact Statement / Objects / Domain / Quantifiers**：c:ℝⁿ→ℝᵐ 在闭球 B̄_R(x̄) 的开邻域 C^{1,1}，Dc 的 β-Lipschitz 预算；A=Dc(x̄) 满行秩，σ₀=σ_min(A)>βR，σ=σ₀−βR>0，J=||A||+βR，r=R/[2(1+J/σ)]。φ:ℝᵐ→ℝ 有限凸，C=argmin φ 非空、c(x̄)∈C；f=φ∘c，S=c^{-1}(C)，F=∂f。对每个 z∈c(B_R) 外层有 d(z,C)≤Ψφ(d(0,∂φ(z)))，Ψφ 非减并趋零。则对每个 x∈B_r(x̄)，d(x,S)≤σ^{-1}Ψφ(r_F(x)/σ)，且局部 Γ=Θ₂=S。
- **Dependencies / Evidence / Status**：[CS-EB](research/canonical/composite_subregularity.md#cs-eb) 分开证明满秩切片修复的闭球自映射、凸链式规则、最小奇异值对全部次梯度的下界。状态 derived-checked；外部先行性未审。
- **Counterevidence / Scope**：c(x)=x²,φ(z)=z²/2 使原生线性 EB 不传递为复合线性 EB；秩亏版本是独立开放问题。若外层幂增长 r_{∂φ}(z)≥m₀d(z,C)^a，才取得 q=1/a 与 K=σ^{-1-1/a}m₀^{-1/a}。历史验证脚本不是证明。

## C36-v1 / CS-PROX · 复合的局部 RL 与近端轨道

- **Exact Statement / Objects / Domain / Quantifiers**：保留 C35 全部前提，再对每个 z∈c(B̄_R)、每个 w∈∂φ(z) 设 ||w||≤M。令 h=βM、λ>0、λh<1。对每对 u,u'∈B_R 和每个 v∈F(u),v'∈F(u')，有〈u−u',v−v'〉≥−h||u−u'||²，故同图块、同 λ 的全对 RL 指数 1、常数 (1+λh)/(1−λh)。每个 x∈B_{R/2} 有唯一 B_R 内局部近端输出，x∈B_{r/2} 则输出在 B_r；不声称完整 J_F 无其他球外纤维。
- **Conditional convergence / Evidence**：再加 Ψ_F(bd)≤κd 对 0≤d≤δ，b=1/[λ(1−λh)]、0<κ<1，以及 d₀≤δ、||x⁰−x̄||+d₀/[(1−λh)(1−κ)]<r/2，才有每条该局部轨道 d_k≤κ^kd₀、有限总长、极限在 S。[CS-PROX](research/canonical/composite_subregularity.md#cs-prox) 的弱凸、最近零点、覆盖和位置预算证明；状态 derived-checked。
- **Objections / Scope**：满秩 EB 单独不提供轨道结论；删除乘子上界或留域、把局部输出升级完整 resolvent 均是新 Claim。

## C37-v1 / CS-MODEL · 曲面上幂与非幂的不同速率

- **Exact Statement / Objects / Domain / Quantifiers**：c(s,t)=t−(s_+)²，S={(s,(s_+)²):s∈ℝ}；对连续严格增无界 η、η(0)=0 取 φ(z)=∫₀^{|z|}η(u)du，F=∂(φ∘c)。每点 r_F=η(|c|)√(1+4s_+²)，d((s,t),S)≤η^{-1}(r_F)。η(u)=u^a、0<a<1 时，幂 q=1/a 的最佳常数 1；η(u)=u log(e/u) 于 0≤u≤1、随后 η(u)=u 时有趋零 gauge η^{-1}(r)∼r/log(1/r)，但任何 q>1 的幂 EB 失败。
- **Dependencies / Evidence / Status**：[CS-MODEL](research/canonical/composite_subregularity.md#cs-model) 逐点公式、竖线锐性和标量近端方程；状态 derived-checked。对后一模型的局部轨道还需 C36 的 λh<1、gauge 兼容和留域；其收敛为超线性但无任意固定 p>1 的 Q-order。
- **Objections / Scope**：这里 c 为 C^{1,1} 而非 C²；源文的其他真多值变体未纳入本命题，外部新颖性未审。

## C38-v1 / M1-CAPTURE · 显式外层映射的两步捕获

- **Exact Statement / Objects / Domain / Quantifiers**：在 Euclidean \(\mathbb R^2\)，令 \(c=2/3\)、\(f(r)=\operatorname{sign}(r)[3(|r|-c)_+/2]^{1/3}\)、\(T(z_1,z_2)=(z_1-f(z_1-3z_2),0)\)、\(Z=[-c,c]\times\{0\}\)、\(z_*=(c,0)\)、\(R=1/(96\sqrt {10})\)。对**每个** \(z\in B_R(z_*)\)，\(T^2z\in Z=\operatorname{Fix}T\)，以后轨道固定。不存在分支选择量词；这是明确给出的单值 \(T\) 的命题。
- **Definitions / Dependencies / Evidence**：同一状态的 \(s=a-3b\) 与 \(h=(3s_+/2)^{1/3}\)，先证明第一步在 \((-c,c+R)\times\{0\}\)，再对第一步超出 \(c\) 的量 \(0<\delta<R\) 直接计算第二步。[对象和完整证明](research/topics/path_dynamics/m1_capture.md#m1-capture)；历史 9/09 多步札记 §5 只作来源线索。
- **Counterevidence / Objections / Status / Scope / Related Files**：`derived-checked`，仅此映射与球；原生多值 `Sign` 广义方程、它的全部允许选择、完整 resolvent 和真正残差尚未恢复，不能用此条给它们认证。[未闭桥](research/topics/path_dynamics/m1_capture.md#m1-obligation)。外部新颖性未审。

## C39-v1 / M1-SHARP · 同一映射的锐一步距离收缩

- **Exact Statement / Objects / Domain / Quantifiers**：保留 C38 的**同一** \(T,Z,z_*,R\)。对每个 \(z\in B_R(z_*)\)，\(d(Tz,Z)\le(3/\sqrt {10})d(z,Z)\)。常数 \(3/\sqrt {10}<1\) 为这个球上统一距离因子的最小值：\(z_t=(c+3t,t)\)、\(t\downarrow0\) 实现该距离比。
- **Definitions / Dependencies / Evidence**：用完整活动关系 \(s=a-3b\) 而不是分别放大两个标量模；分 \(s\le0\) 和 \(s>0\) 的代数证明在 [M1-SHARP](research/topics/path_dynamics/m1_capture.md#m1-sharp)。`derived-checked`；历史较晚的旗舰架构札记 §2 指出这项修正，本轮重新核算。
- **Counterevidence / Objections / Scope / Related Files**：这**不**直接给出全对 RL、真残差 EB 或局部无限轨道留域；C38 独立地给有限捕获。旧例仍可说明独立最坏标量组合失真，却不能作为“一步距离收缩不存在”的反例。[F14](FAILED_ROUTES.md#f14)。

## C40-v1 / CI-IDENTIFY · 真多值次梯度的局部一步识别

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R^2\) 固定 \(c(s,t)=t-(s_+)^2\)、\(\nu>0\)、连续严格增无界 \(\eta:[0,\infty)\to[0,\infty)\) 且 \(\eta(0)=0\)，令 \(\phi_\nu(z)=\nu|z|+\int_0^{|z|}\eta(u)du\)、\(F_\nu=\partial(\phi_\nu\circ c)\)、\(S=c^{-1}(0)\)。在 S 上 F 的纤维为 \(Dc^T[-\nu,\nu]\) 而且真多值，在 S 外 \(r_{F_\nu}\ge\nu\)。任取 \(0<R<1/2\)，令 \(M=\nu+\eta(R+R^2),h=2M,r=R(1-2R)/4\)，固定 \(\lambda>0\) 且 \(\lambda h<1\)。对**每个** \(x\in B_{r/2}(0)\) 满足 \(d(x,S)<\lambda\nu(1-\lambda h)\)，唯一基点在 \(B_R(0)\) 的局部近端输出 \(y\) 属于 S，随后相同局部规则固定于 y。
- **Definitions / Dependencies / Evidence**：[CI-OBJECT 和 CI-IDENTIFY 完整计算](research/topics/composite_regular/cusp_identification.md#ci-identify)；需要 [C36](research/canonical/composite_subregularity.md#cs-prox) 的**局部** coverage、满秩、全部乘子界和同图步长估计。其外层 gauge 可取 \(\eta^{-1}((q-\nu)_+)\)。状态 `derived-checked`，从历史复合稿 §5.3 的观察补上输入半径、步长和真实残差门。
- **Counterevidence / Objections / Scope / Related Files**：图多值不等于局部近端输出多值；没有核远端完整 resolvent，也不处理秩亏或所有初值。与一般 Hölder–RL 路线的优劣和外部新颖性未核。

## C41-v1 / OT-MAXIMA · 弱分离缺失时二阶目标 EB 的障碍

- **Exact Statement / Objects / Domain / Quantifiers**：对 \(f(0)=0\)、\(f(x)=e^{-1/x^2}(2+\sin(1/x^4))\) \((x\ne0)\)，令 \(\Gamma=\{f'=0\}\)、\(\Theta_2=\{x\in\Gamma:d^2 f(x\mid0)(w)\ge0\ \forall w\}\)。存在 \(x_k\downarrow0\) 使 \(f'(x_k)=0,f''(x_k)<0\)，故 \(d(x_k,\Theta_2)>0\)。对**任意** \(\Psi\) 满足 \(\Psi(0)=0\)，不存在包含 0 的邻域使 \(d(x,\Theta_2)\le\Psi(|f'(x)|)\) 在整个邻域成立。
- **Definitions / Dependencies / Evidence**：[OT-MAXIMA](research/topics/composite_regular/oscillating_target.md#ot-maxima) 的 \(u=x^{-4}\) 区间变号及负二阶导证明；\(f\in C^\infty\)，0 是严格全局极小点但近邻驻点函数值为正。状态 `derived-checked`；历史复合稿 §6.2 是来源线索。
- **Counterevidence / Objections / Scope / Related Files**：只否定没有目标一致/弱分离前件时**到完整 \(\Theta_2\)** 的误差界；不否定到 \(\Gamma\) 的界或 [C34](research/canonical/composite_subregularity.md#cs-transfer) 在完整前提下的正向结论。[F15](FAILED_ROUTES.md#f15)。

## C42-v1 / PS-RATE · 幂次剪切的可达速率校准

- **Exact Statement / Objects / Domain / Quantifiers**：\(0<\gamma<1\)、\(q>1/\gamma\)、\(\alpha=\gamma q>1\)，在 \(\mathbb R^2\) 固定 \(\lambda=1\) 与 \(J(t,z)=(t+|z|^\gamma,P_\alpha z)\)，\(F=J^{-1}-I\)、\(S=\mathbb R\times\{0\}\)。对全部 \((s,u)\)，\(d((s,u),S)\le r_F(s,u)^q\)，而 \(q\) 在 \(u\to0\) 不可增大。对全部 \(0<|z|<1\) 的实际轨道一步，有 \(d(J(t,z),S)=d((t,z),S)^{\gamma q}\)，且 \(d(Jx,S)/\|x-Jx\|^q\to1\) 当 \(|z|\downarrow0\)。每个**有界**且含法向邻域的输入矩形上反射 \(2J-I\) 有全对 \(\gamma\)-Hölder 界，此指数不能增大。
- **Definitions / Dependencies / Evidence**：[PS-OBJECT、PS-RATE 与有界窗口证明](research/topics/path_dynamics/power_shear.md) 直接反演完整图、比较真残差、算沿法向比例和切向位移预算；状态 derived-checked，历史 GX-071 / 9/01 foundations §9.2 是来源别名。
- **Counterevidence / Objections / Scope / Related Files**：无界全图不继承次线性全对 RL；整个有界矩形不自动不变，单条轨道需正切向余量。只证明 \(\gamma q\) 在此反向校准族**可达到**，不是普适精确速率、必要条件或有界窗最优 RL 常数。[C43](research/topics/path_dynamics/oscillatory_shear.md) 是不同对象的保守指数对照。

## C43-v1 / OS-SCALING · 粗全对指数与双边实际阶分离

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R^2\) 固定 \(q>1,0<\gamma<1,\beta=q/\gamma-1\)，\(h(0)=0,h(x)=|x|^q\sin(|x|^{-\beta})\) 非零时，\(J(x,y)=(P_qx,P_qy+h(x))\)，\(F=J^{-1}-I,\lambda=1\)。对**全部** \(z\)，\(2^{-1-q/2}\|z\|^q\le\|Jz\|\le\sqrt5\|z\|^q\)。对足够小的球内全部非零轨道，局部零集为 \(\{0\}\)，距离有统一双边 \(q\)-阶；完整 \(F\) 的真实残差有局部 \(q\)-EB 而无任何更大幂指数。反射 \(2J-I\) 在每个有界输入窗为全对 \(\gamma\)-Hölder，在含零邻域无更高指数。
- **Definitions / Dependencies / Evidence**：[OS-OBJECT / SCALING / REFLECTION](research/topics/path_dynamics/oscillatory_shear.md) 的双边范数、局部固定点、两尺度 Hölder 与相位极值序列的直接证明；状态 derived-checked，来源别名 GX-072 / 9/01 foundations §9.3。
- **Counterevidence / Objections / Scope / Related Files**：实际阶 \(q>\gamma q\) 说明全对最坏指数可能保守，不反驳 C42 的可达构造；归一化 Q 因子未证明有极限。零集只在原点附近孤立，完整图在其他远端仍有零点；无界全图次线性 RL 不成立。外部先行性未核。

## C44-v1 / DE-ESCAPE · 自然 Minty 域上一步尺度不等于收敛阶

- **Exact Statement / Objects / Domain / Quantifiers**：取 \(0<\alpha<1,\beta>0,0<\delta<1,\lambda=1,D=[-\delta,\delta]\)，\(C(0)=0,C(x)=P_\alpha(x)[2+\sin(|x|^{-\beta})]\) 非零时，\(J=(I+C)/2\) 仅在 D 定义，\(\operatorname{gph}F=\{(Jx,x-Jx):x\in D\}\)。\(S=\operatorname{zer}F=\{0\}\)。对**每个**非零初值 \(x_0\in D\)，迭代 \(x_{k+1}=Jx_k\) 有有限的首次 \(x_k\notin D\)；一步 \(r_+=\Theta(r^\alpha)>r\)。零点锚定反射最大指数为 \(\alpha\)、局部常数 3；全对反射最大指数为 \(\alpha/(\beta+1)\)。对所有充分小非零输出 u 的完整纤维，\(d(u,S)/r_F(u)\to1\)，线性 EB 常数的缩域下确界 1，任何 \(q>1\) 幂 EB 失败。
- **Definitions / Dependencies / Evidence**：[DE-OBJECT / EXPONENT / ESCAPE / RESIDUAL](research/topics/path_dynamics/domain_escape.md) 的两尺度证明、单调半径与多原像一致残差比；状态 derived-checked，历史 GX-073 / 9/01 foundations §9.4 是来源别名。
- **Counterevidence / Objections / Scope / Related Files**：只给原关系**自然域**内轨道的有限逃逸，不谈未定义延拓后的动力；不能由一步指数声称收敛。把选中残差比提升到真实 infimum 依赖所有原像一致趋零及非空紧纤维；改变 D 须另立版本。外部先行性未核。

## C45-v1 / IZ-PPA · 孤立零点上指定分支的上阶

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间 \(H\)、\(\lambda>0,q>1,\rho>0\)，\(p\in S=F^{-1}(0)\) 局部孤立。指定单值 \(T:V\to H\)，每个 \(x\in V\) 都有 \(Tx\in J_{\lambda F}(x)\)，\(T(p)=p\)。存在 \(V_0\subset V\)、输出球 U 和 \(\eta>0\)，使每个 \(x\in V_0\) 的 \(Tx\in U,\|(x-Tx)/\lambda\|<\eta\)，且这些输出满足真实 EB \(\|Tx-p\|\le\rho r_F(Tx)^q\)、\(\rho\eta^{q-1}\le\lambda/2\)。则 \(\|Tx-p\|\le\rho(2/\lambda)^q\|x-p\|^q\)。若闭输入球 \(\overline B(p,\delta)\subset V_0\) 且 \(C_q\delta^{q-1}<1\)，其中 \(C_q=\rho(2/\lambda)^q\)，该球内每条由 T 生成的轨道留域、趋 p，满足 \(r_{k+1}\le C_qr_k^q\)。
- **Definitions / Dependencies / Evidence**：[IZ-GERM/FIBERS/PPA](research/canonical/isolated_zero_flatness.md#iz-ppa) 给逐图点剪切、真实残差方向、小步门、球不变与完整归纳。状态 derived-checked；旧 RL_foundations §7.1–7.5 是来源，现版本明确输出 EB 的残差窗口和所有输入的分支门。
- **Counterevidence / Objections / Scope / Related Files**：这是 upper \(q\)-order，不含正 Q 因子；只对指定 T，不升级为完整多值 resolvent 的全部选择。选中图值的幂界不能无条件倒推真实 EB，见 [IZ-FIBERS 双值反例](research/canonical/isolated_zero_flatness.md#iz-fibers)。外部优先性未核。

## C46-v1 / IZ-FACTOR · 精确因子的额外归一化门

- **Exact Statement / Objects / Domain / Quantifiers**：在 C45 的不终止轨道上令 \(w_k=(x^k-x^{k+1})/\lambda\)。如果另有 \(\|x^{k+1}-p\|/\|w_k\|^q\to\mu\in(0,\infty)\)，则 \(\|x^{k+1}-p\|/\|x^k-p\|^q\to\mu/\lambda^q\)。
- **Definitions / Dependencies / Evidence**：[IZ-FACTOR](research/canonical/isolated_zero_flatness.md#iz-factor) 的三角双边界与 \(q>1\)；derived-checked，从旧 §7.6 重新核算。
- **Counterevidence / Objections / Scope / Related Files**：归一化极限是额外假设，C45 的上界自身不产生它；不对有限终止或完整 resolvent 的其他分支声称正因子。

## C47-v1 / DC-GAP · GX-074 的独立 coverage 障碍

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R\) 令 \(K=\{0\}\cup\{1/n:n\ge1\}\)、\(\lambda>0\)、\(F(u)=\{0\}\) 对 \(u\in K\)，域外空值；\(S=K\)。完整紧图在全部图点对上对**每个** \(0<\gamma\le1\) 满足 \(\mathrm{RL}(\lambda,\gamma,1)\)，常数 1 在整个 K 上锐；全部有限残差输出有 \(d(u,S)=r_F(u)=0\)。但是自然输入域恰为 K，任何以 0 为心的开球均不被覆盖。
- **Definitions / Dependencies / Evidence**：[DC-OBJECT/GAP](research/topics/path_dynamics/discrete_coverage.md#dc-gap) 逐对计算 Cayley、完整纤维、EB 的作用域与域外无步；derived-checked，旧 GX-074 / foundations 注 1.5 是来源。
- **Counterevidence / Objections / Scope / Related Files**：若把目标换成 \(\{0\}\)，在 \(1/n\) 上真 EB 就失败；不能偷换目标以声称更强结论。反例只否定从 RL 和有限残差 EB 推出输入 coverage，不否定额外假设 coverage 的 PPA 定理。[F16](FAILED_ROUTES.md#f16)。

## C48-v1 / NA-DRIFT · 输出锚距离与最近点漂移的包络

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间，非空 \(S\subset F^{-1}(0)\)、固定 \(\lambda>0\) 与指定 \(J:D\to H\) 的每个 \(x\in U\subset D\)，取 \(y=Jx\)、\(w=(x-y)/\lambda\in F(y)\)。对整个 \(0<d(x,S)\le r_0\) 家族，假设 \(P_S(x),P_S(y)\ne\varnothing\)。置 \(r_x=d(x,S),a(x)=d(x,P_S(y)),\delta(x)=d(P_S(x),P_S(y))\)。对每个 x，\(r_x\le a(x)\le r_x+\delta(x)\le3a(x)\)，相应非负上包络满足 \(\mathcal A(r)\le\chi(r)\le3\mathcal A(r)\)。
- **Definitions / Dependencies / Evidence**：[NA-OBJECT/DRIFT](research/canonical/nonisolated_alignment.md#na-drift) 用任意近似实现两集合间 infimum 的点对证明；derived-checked，从旧 foundations §8.1 重写。非空实际距离趋零时 \(\mathcal A(r)\le Kr^\theta\) 必有 \(\theta\le1\)。
- **Counterevidence / Objections / Scope / Related Files**：未声称投影集合间最近点对取到；定义本身不保证锚包络有幂界。若投影集合不保证非空，用 NA-APPROX 的另一陈述，不把两种前提混写。

## C49-v1 / NA-COMPOSE · 非孤立零集的条件 gauge 合成

- **Exact Statement / Objects / Domain / Quantifiers**：在 C48 同一全体输入家族上，要求每个实际步 \(t=\|w(x)\|<\eta_\psi\)，输出的真实 EB \(d(Jx,S)\le\psi(r_F(Jx))\)，\(\psi\) 有限非减且 \(\psi(t)=o(t)\)，全部达到的 t 有 \(\psi(t)\le\lambda t/2\)。若 \((2/\lambda)[r_x+\delta(x)]<\eta_\psi\)，则 \(d(Jx,S)\le\psi((2/\lambda)a(x))\le\psi((2/\lambda)[r_x+\delta(x)])\)。若对全部 \(0<r\le r_0\) 有 \(\mathcal A(r)\le Kr^\theta\) 且缩域使 \((2K/\lambda)r_0^\theta<\eta_\psi\)，则输出距离包络至多 \(\psi((2K/\lambda)r^\theta)\)；\(\psi(t)=\rho t^q\) 时为上指数 \(\theta q\)。
- **Definitions / Dependencies / Evidence**：[NA-COMPOSE](research/canonical/nonisolated_alignment.md#na-compose) 的 \(|a(x)-\lambda t|\le d(Jx,S)\) 是承重引理；同一实际输出的真 infimum 与 gauge 单调性给结论。状态 derived-checked，旧 §8.2 的近锚界重算。
- **Counterevidence / Objections / Scope / Related Files**：这是指定 J 的逐点/包络上界，未给全轨道留域、完整 resolvent 任意选择或指数最优。无 proximinality 用 [NA-APPROX](research/canonical/nonisolated_alignment.md#na-approx) 的正容差和额外预算；不得省略。外部先行性未核。

## C50-v1 / NA-SHARP · 同序列饱和才能得到 \(\theta q\) 见证

- **Exact Statement / Objects / Domain / Quantifiers**：在 C48 的同一序列 \(x_n\) 上，令 \(r_n=d(x_n,S)\downarrow0,a_n=a(x_n),t_n=\|w(x_n)\|,s_n=d(Jx_n,S)\)。若 \(a_n/r_n^\theta\to A>0,t_n/a_n\to B>0,s_n/t_n^q\to C>0\)，则 \(s_n/r_n^{\theta q}\to CB^qA^q\)；同序列双边 \(\asymp\) 前提给双边阶。在 C49 的小步超线性 EB 下，必有 \(B=1/\lambda\)。
- **Definitions / Dependencies / Evidence**：[NA-SHARP](research/canonical/nonisolated_alignment.md#na-sharp) 的比值乘积及 NA-COMPOSE 的步长误差 \(o(t_n)\)；derived-checked，从旧 §9.1 重算。
- **Counterevidence / Objections / Scope / Related Files**：分别在不同序列取得两个最坏指数不足以给 \(\theta q\) 的锐性；C49 的上界不自动提供此序列或正 Q 因子。GX-071 只是一个具体可达构造，不代表普适必要性。

## C51-v1 / MA-REFLECT · 输出近锚的渐近反射

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间、\(\lambda>0,S\subset F^{-1}(0)\) 非空，任意实际图点 \((y,w)\)、\(0<t=\|w\|<\eta\)，真残差输出 EB \(d(y,S)\le\psi(r_F(y))\)，\(\psi\) 有限非减且 \(o(t)\)。逐点选 \(p\in S\) 满足 \(\|y-p\|\le d(y,S)+e(t)\)，\(e(t)\ge0,e(t)=o(t)\)，\(e(t)>0\) 时不需投影取到，\(e(t)=0\) 时需取到。置 \(x=y+\lambda w,\widehat x=y-\lambda w,\delta_t=(\psi(t)+e(t))/(\lambda t)\)。当 \(\delta_t<1\) 有 MA-1 的双边反射比及相对缺陷界；沿任何 \(t_n\to0\) 的合法序列，比值趋 1。
- **Definitions / Dependencies / Evidence**：[MA-OBJECT/REFLECT](research/canonical/moving_anchor_reflection.md#ma-reflect) 以同一图点和 p 的三角双边界直接证明；derived-checked，从旧 foundations §6.1 重算。
- **Counterevidence / Objections / Scope / Related Files**：p 可随图点移动；不能改成固定零点、所有图点对的 reflector 模，或集合距离收缩。[MA-LIMIT](research/canonical/moving_anchor_reflection.md#ma-limit) 给完整具体反例；外部先行性未核。

## C52-v1 / MA-POWER · 移动锚幂型缺陷

- **Exact Statement / Objects / Domain / Quantifiers**：在 C51 的同一图点和 p 上，若 \(q>1,\rho,c\ge0\)、真 EB \(d(y,S)\le\rho r_F(y)^q\)、\(\|y-p\|\le d(y,S)+c\|w\|^q\)，令 \(A=\rho+c\)。当 \((A/\lambda)\|w\|^{q-1}\le1/2\)，有 \(\|\widehat x-(2p-x)\|\le2^{q+1}A\lambda^{-q}\|x-p\|^q\)。
- **Definitions / Dependencies / Evidence**：[MA-POWER](research/canonical/moving_anchor_reflection.md#ma-power) 的 \(\|x-p\|\ge\lambda\|w\|/2\) 和缺陷恒等式；derived-checked，从旧 §6.2 重算。
- **Counterevidence / Objections / Scope / Related Files**：常数为充分界，未证最优；\(A=0\) 的零缺陷单独由恒等式得出。结论只相对逐点 output-near p，不提供 branch existence、全对 RL 或 PPA 留域。

## C53-v1 / NB-LOCAL · 近似零点锚下指定分支的有限长度

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert \(H\)、完整关系 \(F\)、\(S=F^{-1}(0)\ne\varnothing\)、\(U=B(\bar x,R)\)、\(\bar x\in S\)、\(\lambda>0\)。对所有 \(x\in A_\delta=\{x\in U:d(x,S)\le\delta\}\)，指定同一个 \(T:U\to H\) 的图值 \((Tx,(x-Tx)/\lambda)\)，要求存在可随 \(x\) 变化的近似最近 \(p_n\in S\) 满足 \(\|2Tx-x-p_n\|\le L\|x-p_n\|^\gamma\)，以及实际 \(Tx\) 的真残差窗口 EB；零距离输入亦包括在内。对有限非减零点连续 \(\psi:[0,\eta)\to[0,\infty)\)，若 \((\delta+L\delta^\gamma)/(2\lambda)<\eta\) 且 \(\limsup_{t\downarrow0}\psi((t+Lt^\gamma)/(2\lambda))/t<1\)，则每个满足 C53 留域预算的指定初值产生全程合法、有限长度、趋于 \(S\) 的 named 轨道及明确尾界；还得到 \(U\cap\overline S=U\cap S\)。
- **Definitions / Dependencies / Evidence**：[NB-OBJECT/NB-LOCAL](research/canonical/named_branch_local.md#nb-local) 从逐图点恒等式、真残差方向、全家族量词和 Hilbert 完备性独立证明；旧 foundations §4 是来源。状态 derived-checked，文献先行性未核。
- **Counterevidence / Objections / Scope / Related Files**：A 只是 anchored，不是全对 RL；没有最近点、全局闭 \(S\) 的要求。不能将指定 \(T\) 的结论升级为完整 \(J_{\lambda F}\) 的任意选择；若 A 排除零距离输入，局部闭性及极限归属的论证失效。需对完整纤维另证统一条件。

## C54-v1 / NB-POWER · 幂次上界与退化端点

- **Exact Statement / Objects / Domain / Quantifiers**：在 C53 同一 \(F,T,U,S\) 和所有输出窗口假设下令 \(\psi(t)=\rho t^q\)，\(\rho,q>0\)。当 \(0<\gamma<1,L>0\)，充分门是 \(\gamma q>1\)，或 \(\gamma q=1\) 且 \(\rho(L/(2\lambda))^q<1\)；当 \(\gamma=1\)，充分门是 \(q>1\)，或 \(q=1\) 且 \(\rho(1+L)/(2\lambda)<1\)；当 \(L=0\)，不论打印的 \(\gamma\)，充分门是 \(q>1\)，或 \(q=1\) 且 \(\rho/(2\lambda)<1\)。每种情况还需缩半径及 C53 的实际初值留域预算；结论是相应一步 upper order、C53 有限长度，以及临界系数的 ratio limsup 上界。
- **Definitions / Dependencies / Evidence**：[NB-POWER](research/canonical/named_branch_local.md#nb-power) 对 C53 的 \(\Phi(r)\) 分别展开并核退化参数；derived-checked，与 R03 的非退化门槛相容，但 C53 的对象与量词不同。
- **Counterevidence / Objections / Scope / Related Files**：指数低于 1 时此上界不判定收敛或发散；系数只为该证明证书的充分量，不是一般必要界。Upper order 不给双边精确阶或正 Q 因子；\(L=0\) 时不能沿用 \(\gamma q\) 标签。

## C55-v1 / NB-OSCILLATION · 锚定线性 RL 不推出全对线性 RL

- **Exact Statement / Objects / Domain / Quantifiers**：在 \(\mathbb R,\lambda=1\) 取 \(T(0)=0,T(x)=x[3/10+(1/10)\sin(x^{-2})]\)（\(x\ne0\)），完整定义 \(F(y)=\{x-y:T(x)=y\}\)。对唯一 \(S=\{0\}\) 及每个输入，A 以 \(\gamma=1,L=3/5\) 成立，且真 EB 为 \(|y|\le(2/3)r_F(y)\)，故 C53 的 \(\Phi(r)=(8/15)r\)；但任何零邻域上此完整图的全对 \(\gamma=1\) RL 均失败。
- **Definitions / Dependencies / Evidence**：[NB-OSCILLATION](research/canonical/named_branch_local.md#nb-oscillation) 以 \(1/5\le a(x)\le2/5\) 控制所有原像的真残差，并以 Cayley 导数沿明确序列无界证明不蕴含；新构造，derived-checked。
- **Counterevidence / Objections / Scope / Related Files**：只排除全对线性指数，不排除其他较弱 Hölder 指数。不能以这个例子的完整 \(J_F=T\) 反推任意原关系的完整 resolvent 同一性；外部优先性未核。

## C56-v1 / AV-BRIDGE · 全对图块到指定锚接口

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert \(H\)、完整 \(F\)、\(S=F^{-1}(0)\ne\varnothing\)、\(G\subset\operatorname{gph}F\)、\(\lambda>0\)。若 \(G\) 对任意两图点满足同一 \(L\ge0,0<\gamma\le1\) 的全对 RL，\(U\subset M_+(G)\)，且对 active set \(A\subset U\) 的每个输入 \(d(x,S_G)=d(x,S)<\infty\)，其中 \(S_G=\{p\in S:(p,0)\in G\}\)，则图块唯一指定分支在 \(U\) 上存在；对所有 \(x\in A\) 可取近似最近 \(p_n\in S_G\) 满足 C53 的锚界，且反射在 \(U\) 的任意两输入间有全对 Hölder 模。
- **Definitions / Dependencies / Evidence**：[AV-OBJECT/BRIDGE](research/canonical/all_pairs_verifier.md#av-bridge) 使用剪切单射、覆盖、同图块零锚及距离 infimum 重算旧 foundations §3.1；derived-checked。若要调用 C53，另加对实际输出的真残差 E、兼容和初值留域预算。
- **Counterevidence / Objections / Scope / Related Files**：不要求 \(S_G=S\)，但保距离的 (AV-2) 不可凭 RL 与 coverage 删除，见 C57。完整 \(J_{\lambda F}\) 的任意输出还需对完整输入纤维排他；不提供全局 closedness 或算法不变性。

## C57-v1 / AV-GAP · 失去零锚保距离的完整关系反例

- **Exact Statement / Objects / Domain / Quantifiers**：\(H=\mathbb R,\lambda=1,F(y)=\{0,y\}\)、\(G=\{(y,y):y\in\mathbb R\}\)。全图块任意两点以 \(L=0\) 满足每个 \(0<\gamma\le1\) 的 RL，且 \(M_+(G)=\mathbb R\)，但完整 \(S=\mathbb R\)、\(S_G=\{0\}\)，对每个 \(x\ne0\) 有 \(d(x,S_G)=|x|>0=d(x,S)\)。指定 \(T(x)=x/2\) 不固定这些零距离输入；完整 \(J_F(x)\) 还同时含 \(x\) 与 \(x/2\)。
- **Definitions / Dependencies / Evidence**：[AV-GAP](research/canonical/all_pairs_verifier.md#av-gap) 直接计算全部图值、自然域、反射与零集；新反例，derived-checked。
- **Counterevidence / Objections / Scope / Related Files**：否定“全对图块 RL + coverage 自动产生 C53 的 A”及“图块单值自动给完整排他”，不是对 C56 的反例；其 (AV-2) 不成立。即使真输出 EB 在本例成立，仍不能替代零锚保距离。

## C58-v1 / CG-CLOSURE · 闭图与自然 Minty 域的闭性

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert 空间 \(H\)、\(\lambda>0\)、非空图块 \(G\subset H\times H\)；存在 \(R>0\) 及有限 \(\omega:[0,R)\to[0,\infty)\)，满足 \(\omega(0)=0\)、\(\lim_{t\downarrow0}\omega(t)=0\)，且对 **每一对** Minty 输入差小于 \(R\) 的图点有 \(\|\Delta M_-\|\le\omega(\|\Delta M_+\|)\)。则 \(D=M_+(G)\) 上 Cayley \(C\) 单值并唯一连续延拓至 \(\overline D\)；图的闭包是该延拓的 Cayley pullback。特别地，\(G\) 闭 iff \(D\) 闭；若还知 \(D\) 稠密，则 \(D=H\)。
- **Definitions / Dependencies / Evidence**：[CG-OBJECT/CLOSURE](research/canonical/closed_graph_minty_domain.md#cg-closure) 从同一图块的剪切逆映射、近对角线模和 Hilbert 完备性独立证明，derived-checked。旧 foundations §1.1–§1.4 只是坐标与闭性例的来源；该闭域定理不是旧稿状态的升级。
- **Counterevidence / Objections / Scope / Related Files**：闭图单独不足以 coverage，\(G=[0,1]\times\{0\}\) 有完整反例；没有零点消失模时闭域亦不保闭图。一般跳跃模只保证延拓/闭性，不声称闭包在跳跃尺度仍保同一模。图块结论不排除完整关系中图块外的纤维；文献先行性未核。[CG-BOUNDARY](research/canonical/closed_graph_minty_domain.md#cg-boundary)。

## C59-v1 / RW-POSITIVE · 一般 gauge 的窗口到邻域转换

- **Exact Statement / Objects / Domain / Quantifiers**：实 Hilbert \(H\)、完整 \(F:H\rightrightarrows H\)、\(S=F^{-1}(0)\ni\bar u\)、真残差 \(r_F=d(0,F(u))\)。有限非减 \(\psi:[0,\eta)\to[0,\infty)\)、\(\psi(0)=0\)、原点连续。若存在 \(U\ni\bar u\)、\(0<\delta<\eta\)，对 **每个** \(u\in U\) 且 \(r_F(u)<\delta\) 有 \(d(u,S)\le\psi(r_F(u))\)，并且 \(\psi(\delta)>0\)，则在 \(V=U\cap B(\bar u,\psi(\delta))\) 对 **每个** \(r_F(u)<\eta\) 的 \(u\) 成立同一界。若 gauge 另有全域非减延拓，可将无窗口量词扩大至全部可评价的有限残差（空纤维按 \(+\infty\) 约定）。
- **Definitions / Dependencies / Evidence**：[RW-OBJECT/POSITIVE](research/canonical/residual_window_bridge.md#rw-positive) 用 \(d(u,S)\le\|u-\bar u\|\) 与阈值以上的 gauge 单调性直接证明；derived-checked。旧 foundations 定义0.4 只给正幂特殊情形；本页一般充分门为独立推导。
- **Counterevidence / Objections / Scope / Related Files**：正阈值不是普遍必要条件；没有它时闭图完整关系也可窗口版真而邻域版假，见 [RW-FLAT](research/canonical/residual_window_bridge.md#rw-flat)。有限定义域外 \(\psi(r_F(u))\) 无定义，不能把受限可评价量词暗写成所有 \(u\)；文献先行性未核。

## C60-v1 / DR-TAN · 切触线与抛物线的算法残差

- **Exact Statement / Objects / Domain / Quantifiers**：\(C=\mathbb R\times\{0\},D=\{(s,s^2):s\in\mathbb R\}\subset\mathbb R^2\)，\(U=\{(a,b):b>-1/2\}\)，\(T=I-P_C+P_DR_C\)、\(G=I-T\)。\(P_DR_C\) 在整个 \(U\) 单值，\(S=G^{-1}(0)=\{(0,b):b>-1/2\}\)。对原点附近 **所有** \(z=(a,b)\in U\)，若 \(a=s+2s(s^2+b)\)，则 \(d(z,S)=|a|\le(1+2|b|+2s^2)\|Gz\|^{1/2}\)；半阶局部最优模为 1，任何 \(q>1/2\) 的相同目标幂 EB 失败。不存在原点邻域上统一 \(\rho<1\) 的 \(d(Tz,S)\le\rho d(z,S)\)。
- **Definitions / Dependencies / Evidence**：[DR-TAN](research/topics/examples/dr_tangency_transversality.md#dr-tangent) 从全管唯一投影及 \(G=(2s(s^2+b),-s^2)\) 重算；\(z_s=(s,-s^2)\) 达成半阶模 1 和一步距离比 1。状态 `derived-checked`；来源为 9/01 ZIP `work/c_gx066_077.md` GX-069，详见正文哈希。
- **Counterevidence / Objections / Scope**：这是算法残差，不是 \(N_C+N_D\) 的 EB；\(D\) 非凸、投影唯一只在所列管上。管不变不保证每条轨道留在某个小邻域或有指定渐近率。文献优先性未核。

## C61-v1 / DR-TRANS · 横截线的精确线性模

- **Exact Statement / Objects / Domain / Quantifiers**：\(C,D\subset\mathbb R^2\) 为过原点且夹角 \(0<\theta<\pi/2\) 的直线；全空间同一 \(T=I-P_C+P_DR_C\)、\(G=I-T\)。令 \(c=\cos\theta,s=\sin\theta\)，某旋向的 \(Q_\theta\) 使 \(T=cQ_\theta\)、\(G=I-cQ_\theta\)。对 **所有** \(z,z'\)，\(\|Gz-Gz'\|=s\|z-z'\|\)；\(G^{-1}\) 全局 Lipschitz、MR/MSR 精确模 \(1/s\)，\(\|T^kz\|=c^k\|z\|\) 对每个 \(k\ge0\)。
- **Definitions / Dependencies / Evidence**：[DR-TRANS](research/topics/examples/dr_tangency_transversality.md#dr-transverse) 的平面反射复合和奇异值恒等式；状态 `derived-checked`。来源为同一 9/01 ZIP GX-070，不将它和 C60 当作同一算子的改参。
- **Counterevidence / Objections / Scope**：法锥和 \(N_C+N_D\) 的定义域和残差不同；横截构造不能给任意两集合的普遍模。外部先行性未核。

## C62-v1 / PS-ABSORPTION · 固定全局近端的平稳律吸收

- **Exact Statement / Objects / Domain / Quantifiers**：有限维 \(\mathbb R^n\)、\(\lambda>0\)、同一个 proper Borel \(f:\mathbb R^n\to(-\infty,+\infty]\)。对每个 \(x\in\operatorname{dom}f\)，全局最小解集合 \(P_\lambda f(x)\ne\varnothing\)；Borel 核 \(K(x,P_\lambda f(x))=1\)。令 \(A_K=\{x\in\operatorname{dom}f:K(x,\{x\})=1\}\)。对 **每个** 支撑于 \(\operatorname{dom}f\) 的概率律 \(\pi\)，\(\pi K=\pi\) 当且仅当 \(\pi(A_K)=1\)，不要求 \(f\) 可积或二阶矩。若有限多值集合的各最小解均获正选择概率，则 \(A_K=\{x:P_\lambda f(x)=\{x\}\}\)。
- **Definitions / Dependencies / Evidence**：[PS-ABSORPTION](research/topics/random_markov/proximal_selection_seam.md#ps-absorption) 以同律下有界严格递增 \(\arctan f\) 避免 \(\int|f|\) 的隐藏门，再用平方罚项的严格下降。`derived-checked`；来源 9/14 非乘积近端稿 §3，已重构而非继承标题。
- **Counterevidence / Objections / Scope**：仅对同一个目标的**全局**近端最小解和域内平稳律；非凸 limiting-subdifferential 的完整 resolvent 可含非最小驻点，随机切换目标亦另需证明。外部新颖性未核。

## C63-v1 / PS-SEAM · 闭近端图与非不变极限的 law-step 障碍

- **Exact Statement / Objects / Domain / Quantifiers**：\(\lambda=1,H=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right),b=(3,3)\)，\(f(y)=\tfrac12y^THy-b^Ty+4\mathbf1_{y\ne0}\)，\(Q=H+I\)、\(t(x)=Q^{-1}(b+x)\)、\(g(x)=\tfrac12(b+x)^TQ^{-1}(b+x)\)。完整全局近端图按 \(g<4,=4,>4\) 分别为 \(\{0\},\{0,t(x)\},\{t(x)\}\)；在 tie 各支选概率 \(1/2\) 的核 \(K\) 有唯一平稳律 \(\delta_0\)。沿 \(v=(1,1),a_0>1\) 的真实轨道 \(a_k=1+(a_0-1)4^{-k}\) 有有限总长度却趋向非平稳 \(\delta_v\)。对 **每个** \(W_2\) 邻域 \(B_r(\delta_0)\)，存在固定 \(\epsilon>0\) 与 \(\mu_k=(1-\epsilon)\delta_0+\epsilon\delta_{a_kv}\) 全部在邻域，使 \(W_2(\mu_k,\mu_kK)\to0\) 而 \(W_2(\mu_k,\delta_0)\to\sqrt{2\epsilon}>0\)；故该完整邻域上不存在任何零点消失的 law-step gauge EB。
- **Definitions / Dependencies / Evidence**：[PS-SEAM/NO-EB](research/topics/random_markov/proximal_selection_seam.md#ps-example) 的全图比较、C62 吸收律和射线上显式最优运输；历史 V10 的有理有限恒等式本轮复跑只作观察。`derived-checked`；来源 9/14 非乘积近端稿 §5，外部优先性未核。
- **Counterevidence / Objections / Scope**：零残差仍恰为不变律；问题是**一致消失模**和核的接缝连续性。闭多值图不保证所选核 Feller；这不是 C22/C23 的不一致随机二次近端，亦不是同步 OT \(\Psi\)。

## C64-v1 / SL-LIFT · M1 显式映射的新完整 Sign 图实现

- **Exact Statement / Objects / Domain / Quantifiers**：\(c=2/3\)、\(A(h)=c\operatorname{Sign}(h)+2h^3/3\)，\(\operatorname{Sign}(0)=[-1,1]\)。新关系 \(F_{\rm lift}(u,v)=\varnothing\) 当 \(v\ne0\)；当 \(v=0\)，其**全部**值是 \(\{(h,q):u+h-3q\in A(h)\}\)。对每个 \(z=(p,q)\in\mathbb R^2\)，完整单位步长 resolvent \(J_{F_{\rm lift}}(z)=\{(p-f(p-3q),0)\}=\{Tz\}\)，自然 Minty 域全为 \(\mathbb R^2\)，零集为 \([-c,c]\times\{0\}\)。对 \(0<\delta<1\)，\(r_{F_{\rm lift}}(c+\delta,0)=\delta/3\) 且到零集距离 \(\delta\)，端点线性 EB 常数 3 锐利；左端对称。
- **Definitions / Dependencies / Evidence**：[SL-INCLUSION/GRAPH/ZERO](research/topics/path_dynamics/m1_sign_lift.md#sl-inclusion) 从 Sign 单调包含的三分支唯一反演并对全部残差纤维取 infimum；`derived-checked`。这是**新构造**，可将 C38/C39 对显式 \(T\) 的结论调用到此新关系的完整 resolvent。
- **Counterevidence / Objections / Scope**：历史多步 §5 只给外层 \(T\) 与来源声明，不给原生循环方程全部允许分支；本构造绝不认证历史原生图身份。另一同名 M1/SO-06 是不同算子。新图的全对 RL、历史算法路径对应及外部优先性均未核。
