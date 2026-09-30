# Claim Ledger · 精确身份与证据

本页的“稿内证明”指可阅读的证明文本，不代表本次已经重新独立验真；“内部审计”也不是外部同行评审或优先权确认。对同一编号的量词、域、假设或结论作任何改变，须另立版本。

## C01 · 全图 RL 的 Cayley 坐标

- **Exact Statement / Objects / Domain**：非空关系 \(F:H\rightrightarrows H\)，实 Hilbert 空间 \(H\)，\(\lambda,L>0\)，\(0<\gamma<1\)。在**每一对**图点 \((x,v),(y,w)\) 上有 \(\|(x-y)-\lambda(v-w)\|\le L\|(x-y)+\lambda(v-w)\|^\gamma\)，当且仅当 \(D=\{x+\lambda v:(x,v)\in\operatorname{gph}F\}\) 上 \(C(x+\lambda v)=x-\lambda v\) 良定且为 \(L\)-Hölder；反向图重建为 \(((p+C(p))/2,(p-C(p))/(2\lambda))\)。若 \(D=H\) 则图在**同一固定参数**下 maximal。
- **Dependencies / Evidence**：图点求和、求差和同输入唯一性；[9/23 TeX Lemma `cayley`](assets/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 直接给出双向证明。
- **Objections / Status / Scope**：代数事实，易复核；只说固定参数的 graph-maximal，绝不等同于极大单调；局部图块须重新声明量词。

## C02 · 9/18 局部 RLEB–PPA 收敛（原稿版本）

- **Exact Statement / Objects / Domain**：\(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，\(\lambda>0\)，非空闭 \(S\subset F^{-1}(0)\)，图块 \(\mathcal G\)、开域 \(U\)、\(0<\gamma\le1\)、\(L\ge0\)、\(R,\bar t>0\)，非减 \(\psi(0)=0\) 且原点连续，\(0<\kappa<1\)。A1：\(U_R\) 上局部 range coverage 且每个输入有图块中的最近零点；A2：\(\mathcal G\) 在尺度 \(R\) 满足 all-pairs RL；A3：实际输出上的 \(d(y,S)\le\psi(r_F(y))\) 及 gauge domain；A4：对 \(0<t\le R\)，\(\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t\)。初值还需 \(d_0\le R\) 和 \(\mathcal L(d_0)=\tfrac12[d_0/(1-\kappa)+Ld_0^\gamma/(1-\kappa^\gamma)]<\operatorname{dist}(x^0,X\setminus U)\)。
- **Conclusion**：唯一的**局部** \(J_{\mathcal G}\) 轨道无限继续、留域、有限长度、收敛到 \(S\) 中一点；\(d(x^k,S)\le\kappa^kd_0\)，且 \(\|x^\infty-x^k\|\le\tfrac12[\kappa^kd_0/(1-\kappa)+L\kappa^{\gamma k}d_0^\gamma/(1-\kappa^\gamma)]\)。允许多选择版本改用每个合法 transition 的共同 anchored 估计，不能把多值图与单值局部 \(J\) 混同。
- **Dependencies / Evidence**：C01 的局部形式、一步能量和 \(s\le(d+Ld^\gamma)/2\)、真实输出残差、A1–A4、归纳留域；[9/18 原投稿 ZIP 的 `sections/theorem_spine.tex`](assets/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip)。
- **Objections / Status / Scope**：**有稿内证明及内部语义核对；本轮未重审全证明**。\(r_F\) 为全部输出纤维的 inf；没有额外证明 \(J_{\mathcal G}=J_{\lambda F}\) 时，不得把定理写成全算子完整 resolvent 结论。旧稿中的数值兼容常数不能代替实际收缩率。

## C03 · 全局双向 simultaneous shadow（9/23 候选）

- **Exact Statement / Objects / Domain**：C01 的实 Hilbert、非空全图全尺度 RL 假设。存在**一个**强单调双 Lipschitz homeomorphism \(A:H\to H\)，对**每个** \((x,v)\in\operatorname{gph}F\) 有 \(\|v-A(x)\|\le R/(\sqrt2\lambda)\)、\(\|x-A^{-1}(v)\|\le R/\sqrt2\)，\(R=L^{1/(1-\gamma)}\)。稿内还给 \(0<\sigma<1\) 的交叉估计与显式 Lipschitz/强单调常数，\(\sigma=\sqrt\gamma\) 取到所列半径，且因子 \(1/\sqrt2\) 是任意维数统一意义下最优；指定锚点版本改为另一问题、最优因子 1。
- **Dependencies / Evidence**：[9/23 TeX `thm:shadow`, `thm:sharpness`, `lem:crosslift`](assets/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 的 quadratic excess、orthogonal lifting、Banach contraction。匹配 PDF 21 页。
- **Objections / Status / Scope**：**有证明的研究稿候选，尚待独立数学深审**。全图 all-pairs 条件与 C02 的局部条件不同；不据此断言每个精确逆分支稳定，也不据此确定新颖性。

## C04 · 有限维完整纤维分类（9/23 候选）

- **Exact Statement / Objects / Domain**：固定 \(n\ge1\)、\(\lambda,L>0\)、\(0<\gamma<1\)，取 \(\mathbb R^n\) 上**固定这些参数**图极大的 RL 关系。集合 \(K\) 能作为某个这类关系的完整 \(F^{-1}(0)\)，当且仅当它非空、紧、\(\operatorname{diam}K\le R=L^{1/(1-\gamma)}\)；正向 \(F(0)\) 对应阈值 \(R/\lambda\)。量词是“每一个这样的 \(K\) 都存在某个 \(F\)”以及“每个这类 \(F\) 的纤维必要满足条件”，并非固定 \(F\) 可任意变换纤维。
- **Dependencies / Evidence**：C01、同常数的 Hölder Hilbert 扩张、有限维 proper map/degree 得全域纤维非空紧、`thm:fixedset` 的精确不动点实现；[9/23 TeX `thm:fibers`](assets/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex)。
- **Objections / Status / Scope**：**稿内证明候选**；不把有限维 compactness 移到一般 Hilbert，不把 graph-maximal 改成 maximal monotone。扩张和 fixed-set 的适用条件是独立审查重点。

## C05 · 原关系局部值域的有限数据拓扑证书（9/25 新增候选）

- **Exact Statement / Objects / Domain**：\(F:\mathbb R^n\rightrightarrows\mathbb R^n\)，完整闭非空零集 \(S=F^{-1}(0)\)；\(\lambda,L>0\)，\(0<\gamma<1\)，\(q\gamma>1\)，\(\kappa>0\)，\(\phi(r)=(r+Lr^\gamma)/2\)、\(c=\kappa\lambda^{-q}\)。指定的实际 proximal 对应 \(T(p)\) 在相关窗满足 \((p-y)/\lambda\in F(y)\)、\(\|p-y\|\le\phi(d(p,S))\)、\(d(y,S)\le c\|p-y\|^q\) **对每个** \(y\in T(p)\)。紧有限多面体 \(A\subset\operatorname{int}B\) 上 \(T\) upper semicontinuous、非空紧 Čech-\(\mathbb Q\)-acyclic 值；经验证有限样本定义的包络在 A／B 的 collar 满足 PDF (8.4)：\(\sup_Au_E\le u\)、\(\inf_{B\setminus\operatorname{int}A}g_E\ge m>0\)、\(\phi(u)<d(A,B^c)\)、\(\alpha=c\phi(u)^q<m\)。\(H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 对每个 j 满射，且 \(\chi(A)\ne0\)。
- **Conclusion**：\(B(0,(m-\alpha)/\lambda)\subset F(\operatorname{int}A)\)；更一般地，\(\sup_A\|h\|<(m-\alpha)/\lambda\) 的连续 \(h:A\to\mathbb R^n\) 有 \(x\in\operatorname{int}A\) 满足 \(h(x)\in F(x)\)、\(d(x,S)\le\kappa\|h(x)\|^q\)。
- **Dependencies / Evidence**：[9/25 PDF §8 Theorem 8.1](assets/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)，包络、Vietoris–Begle 与有理 morphism Lefschetz theorem 的稿内论证。
- **Objections / Status / Scope**：**PDF-only 候选，新增模块未独立审计**。全文明言它不从全图 RL 自动推出；有限观测不证明整窗 (8.1)–(8.2) 或 \(T\) 的 topology。需核对所引 Lefschetz 定理的图、acyclicity、homotopy 与邻域 retract 条件。

## C06 · 固定紧 T-only 图卡的内生观测

- **Exact Statement / Objects / Domain**：非空紧 \(K\subset\mathbb R^d\)，非空闭 \(S\subset K\)。令 \(X=\{T\in C(K,K):T|_S=I,\ T^n\to\Pi_T\text{一致},\Pi_T(K)\subset S\}\)，全时间度量 \(\rho(T,U)=\sup_{n\ge0}\|T^n-U^n\|_K\)。定义实际尾 \(w_n\) 为迭代后所有步差与到 \(S\) 距离的上确界，实际反射模 \(m_j=\sup_{\|x-y\|\le2^{-j}}\|(2T-I)x-(2T-I)y\|\)。则 \(\Phi:X\to c_0\times c_0\)，\(T\mapsto(w,m)\) 连续 proper；其实际像闭 Polish，非空精确纤维紧/Baire，映射到像 perfect/quotient。
- **Dependencies / Evidence**：[9/20 `06_math_audit.md` §1](assets/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md) 的 Arzelà–Ascoli、共同尾预算及全时间收敛证明；内部独立审计。
- **Objections / Status / Scope**：**仅固定紧源完整 T-only、非空 X 条件下内部已审**；proper/quotient 不推出 category-preserving；局部 \(T\) 不代表完整全局 \(F\)。

## C07 · 原 Baire／多孔性比较量尺的塌缩报告

- **Exact Statement / Objects / Domain**：9/21 包报告在其先前定义的完整图 Polish／普通 \(C^0\) 与动力度量 \((X_D,d_{\rm dyn})\) 中，正 Hölder 类受共同粗糙化影响；特别 \(\mathcal R_D\subseteq\mathcal H_+\in\sigma\mathcal P^-(X_D,d_{\rm dyn})\)，所以 \(\mathcal R_D\setminus(\mathcal L_D\cup\mathcal M_D)\in\sigma\mathcal P^-\subseteq\sigma\mathcal P^+\)。\(\sigma\mathcal P^-\) 是包内的 σ-lower-porous 类。**域 \(D\)、全部图卡与孔隙常数须在原证明恢复后冻结，不由此摘要补造。**
- **Dependencies / Evidence**：[9/21 `02_VERIFIED_CORE.md` §6](assets/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md) 与 [`03_NO_GO_LEDGER.md` N05、N08、N10](assets/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)；v0.9 区分 V-A/V-B、SOURCE-MISSING。
- **Objections / Status / Scope**：**历史总账报告，非本仓库已重构的 canonical proof**；旧目标“差集非 σ-upper-porous”在其所指空间中被报告为假，不是所有合理大小量尺均失败，也不是 RLEB 与 LT 相同。

## C08 · 解选择稳定性（修订身份）

- **Exact Statement / Objects / Domain**：一族在共同区域有轨道与统一尾界的 \(T\)，满足局部 \(\|Tx-Ty\|\le H\|x-y\|^\gamma\)，\(0<\gamma<1\)。若 \(\|T^kx-\Pi(x)\|\le M\sigma^k\) 对全体初值和 \(k\ge0\) 一致成立，则 \(\|\Pi(x)-\Pi(y)\|\le C(\log\log(1/\delta)/\log(1/\delta))^\beta\)，\(\beta=\log(1/\sigma)/\log(1/\gamma)\)；若统一尾界 \(M e^{-c_0\nu^k}\)，\(\nu>1\)，则是 \(C e^{-c(\log(1/\delta))^\alpha}\)，\(\alpha=\log\nu/\log(\nu/\gamma)\)，足够小 \(\delta=\|x-y\|>0\)。修订包给完整 proximal 的显式半代数例说明即使点误差 Q-二次，\(\Pi\) 也无需正阶 Hölder。
- **Dependencies / Evidence**：[原 `research_note.md` §1–4](assets/次单调论文研究/正式后的研究/research_note.md)，[修订审计 ZIP](assets/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)，9/21 `02_VERIFIED_CORE.md` §4。
- **Objections / Status / Scope**：**修订后内部数学审计**。一般 RLEB 推论只能直接用于局部 \(J_{\mathcal G}\)，或另加共同轨道区域 \(J_{\lambda F}=J_{\mathcal G}\)；旧稿无条件升级完整 resolvent 的版本已失效。固定解点的 anchored Hölder calmness 与邻域中任意两初值的 Hölder 连续性不同。
