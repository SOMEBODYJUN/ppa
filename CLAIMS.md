# Claim Ledger · 精确身份与证据

本页的“稿内证明”指可阅读的证明文本，不代表全部已重新独立验真；“内部审计”也不是外部同行评审或优先权确认。对同一编号的量词、域、假设或结论作任何改变，须另立版本。依赖和合取关系见 [超边图](research/HYPERGRAPH.md)；原稿路径与版本见 [SOURCES.md](research/SOURCES.md)。C01–C08 保留初始身份，新增 C09–C17 记录原账遗漏的研究资产。

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
- **Dependencies / Evidence**：[9/25 PDF §8 Theorem 8.1](history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)，包络、Vietoris–Begle 与有理 morphism Lefschetz theorem 的稿内论证。
- **Objections / Status / Scope**：**PDF-only 候选，新增模块未独立审计**。全文明言它不从全图 RL 自动推出；有限观测不证明整窗 (8.1)–(8.2) 或 \(T\) 的 topology。需核对所引 Lefschetz 定理的图、acyclicity、homotopy 与邻域 retract 条件。

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
