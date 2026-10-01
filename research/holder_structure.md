# Hölder–RL：整体结构、局部收敛与拓扑条件

本页将原稿重构为数学节点及合取依赖。**审读状态**：本轮独立核读并局部重算了下列 shadow、纤维实现、Dini、对数接缝和回缩的稿内证明，未发现所列内部计算的致命断点；这不等于完成外部引理适用条件、优先权或整篇论文的独立审稿。随机推论另有明确的度量完备性修补。9/25 Lefschetz 模块仍有外部定理核验门槛。

## 来源与版本

- **S23**：[9/23 结构稿 TeX](../history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex)，以及[匹配 PDF](../history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.pdf)。以下 TeX 行号对应原始附件，标签是稳定定位。
- **S19**：[9/19 扩展源码 ZIP](../history/sources/次单调论文研究/RLEB_投稿扩展版_完整源码_2026-09-19.zip)，内文件 `RLEB_投稿扩展版_2026-09-19/sections/extensions_moduli_structure.tex`。本轮读取了解包全文；以下 S19 行号均指该文件。
- **S25**：[9/25 combined PDF](../history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)，§8，印刷页 20–22。该新增节没有同版 TeX；不把 S23 当作其源码。

<a id="h01"></a>
## H01 · 固定参数全图 RL 与 Cayley 表示

令实 Hilbert 空间上非空关系 \(F:H\rightrightarrows H\)，固定 \(\lambda,L>0\)、\(0<\gamma<1\)。对**每对**图点，要求

\[
\|(x-y)-\lambda(v-w)\|\le L\|(x-y)+\lambda(v-w)\|^\gamma.
\]

记 \(R=L^{1/(1-\gamma)}\)、\(D=\{x+\lambda v:(x,v)\in\operatorname{gph}F\}\)。它等价于良定的 \(L\)-Hölder 映射 \(C:D\to H\)，其中

\[
C(x+\lambda v)=x-\lambda v,\qquad
\operatorname{gph}F=\left\{\left(\frac{p+C(p)}2,\frac{p-C(p)}{2\lambda}\right):p\in D\right\}.
\]

在**同一固定参数**下 graph-maximal 当且仅当 \(D=H\)：反向用同输入唯一性，正向用同常数 Hölder 扩张。此扩张在一般 Hilbert 空间成立，稿内通过 Hilbert snowflake 与 Kirszbraun 组合证明。不能将 graph-maximal 改成极大单调。

**证据**：S23 §2，`def:RL`、`lem:cayley`、`lem:holderextension`，222–291 行。坐标代数已独立复核；两个经典扩张定理是外部依赖。局部图块与完整 resolvent 的区别见[定义接口](foundations.md)。

<a id="lift"></a>
<a id="h02"></a>
## H02 · C03：同一个强单调影子控制正反方向

**假设**仅为 H01，不要求原关系 graph-maximal、闭图或有限维。对每个 \(0<\sigma<1\)，存在**一个**强单调双 Lipschitz 同胚 \(A_\sigma:H\to H\)，令

\[
M_\sigma=(1-\gamma)\gamma^{\gamma/(1-\gamma)}R^2
\sigma^{-2\gamma/(1-\gamma)},\qquad
r_\sigma=\sqrt{\frac{M_\sigma}{2(1-\sigma^2)}}.
\]

对全部 \((x,v)\in\operatorname{gph}F\) 同时有

\[
\|v-A_\sigma(x)\|\le r_\sigma/\lambda,
\qquad \|x-A_\sigma^{-1}(v)\|\le r_\sigma.
\]

\(\operatorname{Lip}A_\sigma\le(1+\sigma)/(\lambda(1-\sigma))\)，逆映射常数至多 \(\lambda(1+\sigma)/(1-\sigma)\)，强单调常数至少 \((1-\sigma)/(\lambda(1+\sigma))\)。取 \(\sigma=\sqrt\gamma\) 得 \(r_\sigma=R/\sqrt2\)。

### 承重证明

1. 标量优化给 \(\sup_{t\ge0}(L^2t^{2\gamma}-\sigma^2t^2)=M_\sigma\)。
2. 将每个 \(p\in D\) 提升为 \((p,re_p)\)，其中 \(r^2=M_\sigma/(2\sigma^2)\)。同常数 Lipschitz 扩张后，限制到基平面得到一个 \(\sigma\)-Lipschitz 映射 \(N\)，满足
   \(\|C(p)-N(q)\|^2\le\sigma^2\|p-q\|^2+M_\sigma/2\)。
3. \(X(q)=(q+N(q))/2\)、\(V(q)=(q-N(q))/(2\lambda)\) 均由 Banach 不动点定理成为双射；取 \(A_\sigma=V\circ X^{-1}\)。
4. 同一交叉估计分别代入相同输入和相同输出来得到两条误差界。

**独立核对**：标量极值、提升距离的因子 2、两次 contraction、强单调常数及 \(\sigma=\sqrt\gamma\) 的优化均已局部重算。证据：S23 §3，`lem:excess`、`lem:crosslift`、`thm:shadow`，313–468 行。

**最优性的精确范围**：正则单纯形半径 \(R\sqrt{n/[2(n+1)]}\) 给所有维数统一常数的下界，令 \(n\to\infty\) 得 \(1/\sqrt2\)。原稿没有证明每个固定维数的最优因子，也没有证明 conditioning 常数最优。指定锚点是另一问题，原稿的最优因子为 1。证据：`thm:sharpness`，506–557 行；`thm:anchor`，561–617 行。

<a id="proper"></a>
<a id="fix"></a>
<a id="h03"></a>
## H03 · C04：有限维完整纤维的精确分类

固定 \(n\ge1\) 及 H01 参数。集合 \(K\subset\mathbb R^n\) 能作为**某个**固定参数 graph-maximal RL 关系的完整 \(F^{-1}(0)\)，当且仅当

\[
K\ne\varnothing,\qquad K\text{ 紧},\qquad\operatorname{diam}K\le R.
\]

完整正向纤维 \(F(0)\) 的阈值为 \(R/\lambda\)。这里的存在量词不是说固定一个 \(F\) 后可任意指定其纤维。

### 必要性与充分性分开

- **必要性**：全域 Cayley 映射的次线性增长使两坐标投影的 homotopy 一致 proper；有限维 Brouwer degree 为 1，给全域、全值域和非空紧纤维。同输出/同输入的 RL 比较给直径界。来源：S23 `lem:diameters` 293–306 行，`thm:finite_geometry` 624–686 行。
- **充分性**：对任意非空紧 \(K\) 构造 \(R_K:H\to\overline{\operatorname{conv}}K\)，使 \(\operatorname{Fix}R_K=K\)，Hölder 常数恰可取 \((\operatorname{diam}K)^{1-\gamma}\)。令 \(C=R_K\) 即实现逆零纤维；令 \(C=-R_{\lambda K}\) 实现正向零纤维。来源：`thm:fixedset` 738–838 行；`thm:fibers` 840–871 行。

固定点构造的关键不是未经证明的“任意紧集是 retract”。先证明凸包余量
\(\sup_{q\in Q}\|p-q\|^2\le D_K^2-d(p,K)^2\)，再用正系数可数 bump 把 \(Q\setminus K\) 上所有点向固定 \(k_0\in K\) 推动，同时保留共同 Hölder 常数；最后复合 \(P_Q\)。本轮核对了 bump 幅度的正性、负指数不等式方向、可数覆盖、级数一致收敛和无额外不动点。来源：`lem:margin` 711–736 行及上述固定点定理。

**范围门槛**：固定点实现本身允许 Hilbert 空间；完整纤维分类的必要性使用有限维紧性与 Brouwer degree。不得整体推广到无限维。非空完整纤维再与 H02 合取，才得到到 singleton 的 Hausdorff 误差界；H02 单独不保证原纤维非空。

<a id="din"></a>
<a id="log"></a>
<a id="r05"></a>
## H04 · 一般模、Dini 门槛与对数反例

将局部 all-pairs 右侧替换为连续非减 \(\omega\)，\(\omega(0)=0\)。保留局部 range coverage、最近零点比较、真实输出误差界及 gauge 范围；要求

\[
\psi\!\left(\frac{r+\omega(r)}{2\lambda}\right)\le\kappa r,
\quad0<\kappa<1,\qquad
\int_0^R\frac{\omega(t)}t\,dt<\infty.
\]

留域预算为
\(\mathcal L_\omega(d_0)=d_0/[2(1-\kappa)]+\frac12\sum_{k\ge0}\omega(\kappa^kd_0)<d(x^0,U^c)\)。这些条件共同推出有限长度、收敛到零集一点及尾界

\[
\|x^\infty-x^k\|\le\frac12\left[
\frac{\kappa^kd_0}{1-\kappa}+\sum_{j\ge k}\omega(\kappa^jd_0)\right].
\]

Dini 积分与几何采样级数的等价由每段积分的上下界直接给出。来源：S19 `thm:modulus-dini`，32–114 行。不能删掉 EB、coverage、兼容与留域后仍称其为 RL 推出的收敛。

**非幂次完整接缝**：令 \(\ell_a(t)=[\log(e/t)]^{-a}\) 在 \(0<t\le e^{-a}\)，原点取零，其后按切线延伸。原稿构造两支闭图

\[
F_a(\xi,y)=\{(-\ell_a(4y),3y),(-\ell_a(4y),-5y)\}\quad(y\ge0),
\]

而 \(y<0\) 值为空。完整而非选支的 proximal 为
\(J_a(p,q)=(p+\ell_a(|q|),|q|/4)\)。全图一般模可取
\(\Omega_a(t)=\sqrt{(t+2\ell_a(t))^2+9t^2/4}\)。精确最小残差是 \(\sqrt{\ell_a(4y)^2+9y^2}\)，不能以另一支替代最小残差。

轨道距离每步乘 \(1/4\)，水平增量为 \(\ell_a(4^{-k}|q_0|)\)。当 \(q_0\ne0\)，有限长度及点收敛当且仅当 \(a>1\)；\(a\le1\) 时水平坐标趋于正无穷。这证明 **此族中** Dini 门槛精确，反驳“到集合距离几何下降必然点收敛”；不证明每个非 Dini 模都必然失败。来源：S19 `thm:logarithmic-seam`，145–295 行；完整 proximal 解算与级数判别已独立核对。

<a id="ret"></a>
<a id="ob-topo"></a>
## H05 · 连续极限回缩与任意紧零集的条件限制

在 H04 整套局部假设下，令 \(\ell_\omega=\mathcal L_\omega\)，

\[
\mathcal O=\{x\in U:d(x,S)<R,\ \ell_\omega(d(x,S))<d(x,U^c)\}.
\]

\(\mathcal O\) 开、正向不变，包含 \(S\cap U\)。局部 all-pairs 保证 \(J_{\mathcal G}\) 连续；统一尾界保证迭代一致收敛，故 \(\Pi(x)=\lim_kJ_{\mathcal G}^kx\) 是到 \(S\cap U\) 的连续回缩。该零集是 Euclidean neighborhood retract，并具有原稿明确给出的局部收缩性质。来源：S19 `prop:limit-retraction`，322–394 行。

**跨主线关系**：H03 可实现任意非空紧零集，包括 Cantor 型集合；H05 的收敛假设则迫使零集局部可缩。两者并不矛盾：在这类非局部可缩零点附近，H04 的整套附加假设不能全部成立。地图应将此标为“合取假设的拓扑限制”，不能标成 H03 被 H05 否定。

<a id="stoch"></a>
<a id="metric"></a>
<a id="stoch-limit"></a>
<a id="polish-gap"></a>
## H06 · 随机推论的给定度量缺口及修补

S19 `thm:stochastic-rleb`，502–554 行，假设路径留在 \(0\le D_k\le R\) 的不变域，且

\[
s_k\le\tfrac12[D_k+\omega(D_k)],\qquad
\mathbb E[D_{k+1}\mid\mathcal F_k]\le\kappa D_k.
\]

稿内用截断阈值 \(R\kappa^{k/2}\) 与 Markov 不等式证明 \(\sum_k\mathbb E\omega(D_k)<\infty\)，再由 Tonelli 得几乎处处有限长度。该计算不要求 \(\omega\) 凹，已核对。

**缺口**：第 504 行仅写度量空间“Polish”，第 550 行直接用完备性。若 Polish 仅指拓扑可完备，不保证所指定的度量完备，则极限存在结论错误。

**独立反例**：取 \(\mathsf X=(0,2)\) 配通常距离，\(S=\{2^{-n}:n\ge1\}\) 在该空间中闭；确定性过程

\[
X_k=2^{-(k+2)}+4^{-(k+2)},\qquad
D_k=d(X_k,S)=4^{-(k+2)}.
\]

于是 \(D_{k+1}=D_k/4\)，且

\[
s_k=2^{-(k+3)}+3\cdot4^{-(k+3)}
\le\tfrac12(D_k+4\sqrt{D_k}).
\]

取 Dini 模 \(\omega(r)=4\sqrt r\)、\(R=1/16\)；所有显示的路径条件成立，\(\mathsf X\) 拓扑 Polish，但 \(X_k\to0\notin\mathsf X\)。有限长度仍成立，空间内收敛结论失败。

**规范修补版本**：明确要求“给定度量 \(d_{\mathsf X}\) 完备”，可写 complete separable metric space，再用 \(S\) 闭得到极限在 \(S\)。本页将原稿标为待修条件，将修补版标为本轮推导；不静默改写原文。S19 的确定性 `prop:complete-metric-transfer`（404–435 行）已经明确要求 complete，不受此措辞问题影响。

<a id="sample"></a>
<a id="window"></a>
<a id="h07"></a>
## H07 · C05：有限数据原关系局部值域证书

此节是独立假设层。令 \(S=F^{-1}(0)\subset\mathbb R^n\) 非空闭，\(T(p)\) 是指定的实际 proximal 输出族：

\[
y\in T(p)\Rightarrow(p-y)/\lambda\in F(y),\qquad
\|p-y\|\le\phi(d(p,S)),\qquad d(y,S)\le c\|p-y\|^q,
\]

其中 \(\phi(r)=(r+Lr^\gamma)/2\)，\(c=\kappa\lambda^{-q}\)，\(0<\gamma<1\)、\(q\gamma>1\)。**T 可以是完整 resolvent 的指定子关系**，但其所有声明值及整窗性质须成立。来源：S25 §8，页 20–21，(8.1)–(8.2) 及 Theorem 8.1 后的明确限定。

经独立验证的有限观测 \((p_i,y_i)\) 给

\[
\rho_i=\phi^{-1}(\|p_i-y_i\|),\quad e_i=c\|p_i-y_i\|^q,
\quad g_E(z)=\max_i(\rho_i-\|z-p_i\|),\quad
u_E(z)=\min_i(\|z-y_i\|+e_i).
\]

由距离的 1-Lipschitz 性，\(g_E\le d(\cdot,S)\le u_E\)。取紧有限多面体 \(A\subset\operatorname{int}B\)，假设：

- \(T\) 在 \(A\) 邻域 usc，取非空紧 Čech–\(\mathbb Q\)-acyclic 值，前述 proximal 和数值估计对 \(A\) 全部输出成立。
- \(\sup_Au_E\le u\)，\(\inf_{B\setminus\operatorname{int}A}g_E\ge m>0\)，\(\phi(u)<d(A,B^c)\)，\(\alpha=c\phi(u)^q<m\)。
- 包含诱导 \(H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 每阶满射，且 \(\chi(A)\ne0\)。

则

\[
B(0,(m-\alpha)/\lambda)\subset F(\operatorname{int}A).
\]

更一般地，每个连续 \(h:A\to\mathbb R^n\) 且 \(\sup_A\|h\|<(m-\alpha)/\lambda\)，存在 \(x\in\operatorname{int}A\) 使 \(h(x)\in F(x)\)、\(d(x,S)\le\kappa\|h(x)\|^q\)。

**证明结构与核验门槛**：collar 不等式先给 \(T(A)\subset\operatorname{int}A\) 且所有输出距 \(A^c\) 至少 \(m-\alpha\)。紧图 \(\Gamma\) 第一投影 \(\pi\) 的 acyclic 纤维给 Vietoris–Begle 同构；线段在 B 内的同伦与上同调满射给 \(e^*=\pi^*\)。在同一个图 span 上改为 \(e_h(p,y)=y+\lambda h(y)\)，Lefschetz 数为 \(\chi(A)\)，得到 coincidence。原稿没有假定非线性像 \(e_h(T(p))\) 仍 acyclic，此点处理正确。

已按[一手文献卡 LIT-GRN-2002](LITERATURE.md#lit-grn-2002) 核原引文 [6, Theorem 6.2]：\(A\) 为 Euclidean neighborhood retract；\(\Gamma\) 与 \(\pi\) 是紧 Vietoris span；\(e_h(\Gamma)\subset A\) 为紧 morphism，故属原文的 \(CAC(A)\)；同伦和上同调满射给非零 Lefschetz 数。这关闭**该引文的适用条件门**，不把 C05 升为已独立审完的定理。有限观测不能建立整窗估计、usc 或 acyclicity；紧度量值的 Čech cohomology/homology 等价限于本范围，外部新颖性未核；也不存在 H02 → H07 的无条件蕴含。来源：S25 页 21–22，Theorem 8.1 证明及其后范围说明。

## 数学超边总表

每行左侧是必须共同出现的前提，不是多个可替代的理由。

| 超边 | 联合输入 | 输出 | 关系性质 |
|---|---|---|---|
| HE-H01 | 全图 RL；图和坐标同输入唯一性 | Hölder Cayley 表示 | 代数等价 |
| HE-H02 | Cayley 表示；同常数 Hölder 扩张 | maximal iff 全输入；存在 completion | 外部扩张支撑 |
| HE-H03 | 二次 excess；正交提升；Kirszbraun | 单个 cross-lift N | 稿内构造，已局部重算 |
| HE-H04 | Cayley；cross-lift；Banach contraction | C03 同时正反 shadow | 合取蕴含 |
| HE-H05 | 单纯形半径；投影 Hölder 模；全域重建 | 维数统一最优因子 | 反向下界 |
| HE-H06 | maximal；次线性增长；有限维；degree | 非空紧纤维、properness | 维数限制 |
| HE-H07 | 凸包余量；正 bump；投影 | 任意紧集精确固定点实现 | 构造 |
| HE-H08 | properness；直径界 | C04 必要性 | 必要条件 |
| HE-H09 | 固定点实现；Cayley 重建 | C04 充分性 | 存在性 |
| HE-H10 | 局部 coverage；RL 模；输出 EB；兼容；Dini；留域 | 有限长度及点收敛 | 条件收敛 |
| HE-H11 | 全对连续性；统一尾界；不变开域 | 连续极限回缩 | 拓扑限制 |
| HE-H12 | 对数完整接缝；a≤1；非零初始高度 | 距离收缩而点发散 | 反例 |
| HE-H13 | 随机期望收缩；路径步长包络；Dini；给定度量完备；S 闭 | 几乎处处收敛于 S | 修补版本 |
| HE-H14 | 验证样本；proximal/EB 估计；距离 Lipschitz | 距离上下包络 | 数值证书层 |
| HE-H15 | 包络 collar；整窗估计；acyclic usc T；上同调满射；χ≠0；Lefschetz | C05 原关系局部值域球 | 独立局部假设层 |

## 下一步证明工作

1. 查核并冻结 H01 所用经典扩张定理与 H07 所引 rational morphism 定理的原文适用条件。
2. 在随机推论正式版本中补上给定度量完备性，并保留反例作为修订原因。
3. 用 H05 的拓扑限制逐个审查 H03 中病态紧零集实现能满足哪些 EB/coverage 条件，避免把结构存在性误读为 PPA 收敛。
