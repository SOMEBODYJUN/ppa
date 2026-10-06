# 跨主题符号与适用域契约

本页用于从一个研究主题调用另一个主题的命题。单篇正文可用局部字母，但**调用时须连同对象、目标、残差及量词**一起带走；只见相同字母不构成同一数学对象。精确定义仍在 [foundations](foundations.md)，各 Claim 的状态与条件以 [总账](../CLAIMS.md) 和正文为准。

## 固定的图与近端坐标

| 记号 | 固定含义 | 禁止的替换 |
| --- | --- | --- |
| \(F:H\rightrightarrows H\), \(\operatorname{gph}F\) | 已声明原关系的**完整图**；图块另记 \(\mathcal G\subseteq\operatorname{gph}F\) | 选中支或局部表示图不自动等于完整图 |
| \(S\) | 每条命题自行声明；通常为非空闭 \(S\subseteq F^{-1}(0)\)，若用完整零集须写 \(S=F^{-1}(0)\) | 锥模块的对偶面子空间和 Markov 不变律集都不默认叫此零集 |
| \(r_F(u)=d(0,F(u))\) | 全纤维真原算子残差，空纤维为 \(+\infty\) | 选中图值 \(\|v\|\)、输入步残差 \(d(p,J_{\lambda F}(p))\)、算法残差 \(\|p-Tp\|\)、law-step 或同步 OT 残差 |
| \(M_\pm(u,v)=u\pm\lambda v\), \(D_\lambda(\mathcal G)=M_+(\mathcal G)\) | 同一个 \(\lambda>0\) 和同一图块的剪切与自然输入域 | \(M_+\) 单射不意味着输入 coverage；换步长须重算域 |
| \(J_{\lambda F}(p)\) | 完整 \(F\) 的**全部**近端输出；\(J_{\mathcal G}\) 只反演指定图块 | 局部单值性不排除图块外的远支 |
| \(C(p)=M_-M_+^{-1}(p)\) | 当同图块满足全对零消失模时的部分定义 Cayley 映射 | 锥约束 \(C\)、运输成本矩阵 \(C\) 都是别的类型 |

统一写 \(\mathrm{RL}(\lambda,\gamma,L;R)\)：**步长、指数、系数、输入对距离上界**依次排列。无 \(R\) 只在正文已明示全尺度时省略；\(L=0\) 允许，局部窗的 \(R\) 不是输入球半径。对任意两图点，\(\|\Delta M_-\|\le L\|\Delta M_+\|^\gamma\) 只在所列尺度成立。[参数字典](canonical/parameter_dictionary.md#pd-quantifiers) 的同图换步、逆关系、缩放与 [非 tied 二参数](canonical/non_tied_cayley.md#nt-object) 是不同变换；\(\gamma=1\) 的 tied 曲线不能代替任意 \((\mu,\rho)\) 区域。

## 局部重绑定必须写明的对象

总体算子空间比较若需记尚待选择的大小不变量，用 \(\mathfrak I\)；Markov 的 \(\mathcal I\) 专指不变律集。二者既不同型也没有默认桥。

跨模块的 \(\rho\) 也须带类型：LT 公共接口的 \(\rho_{\rm EB}>0\) 是真残差线性 EB 系数；非 tied 二参数条件的 \(\rho_{\rm quad}\) 可带符号，乘 \(\|v_1-v_2\|^2\)；有限数据的 \(\rho_{\rm loc}(t)\) 是随半径变化的根函数。正文沿各自旧记号 \(\rho\)，跨页推理时用这些下标重绑定，不能把同形字母代入另一式。算子空间 §2 的 \(\mathcal R_D\) 是指定共同接口上的 direct 认证类；§5 引述的旧 \((X_D,d_{\rm dyn})\) 是**历史空间及来源报告**，不因下标同形而获当前母空间身份。

| 模块 | 局部记号 | 跨模块调用时的类型与桥 |
| --- | --- | --- |
| [全局影子 C03](canonical/global_shadow.md#gsh-object) | \(R=L^{1/(1-\gamma)}\) 是全尺度 RL 的结构长度，\(M_\sigma\) 是平方 excess，\(N\) 是先固定的一张全局 \(\sigma\)-Lipschitz 扩张；\(X,Y\) 是代理的两个坐标映射，\(A_\sigma=Y\circ X^{-1}\) | 此 \(R\) 不是局部输入对距上限；\(X\) 不代表环境空间，\(Y\) 不代表原关系值域。正反界须共用这个 \(A_\sigma\)；不同 \(\sigma\) 或扩张可给不同影子 |
| [完整纤维 C04](canonical/finite_fiber_classification.md#ff-object) | \(\mathcal D\) 是同参数 Cayley 输入域，\(X,V\) 是原图的坐标映射；\(R_K\) 是为给定紧 \(K\) 构造的 Hölder 不动点映射，\(Q=\overline{\operatorname{conv}}K\) | \(V\) 不是有限样本列矩阵，\(Q\) 不是 QP 矩阵；这里原图坐标不能换成 C03 的代理坐标。\(R_K(H)\subseteq Q\)，不写等于；正向、逆向紧纤维分别存在的实现不默认是同一个关系 |
| [全纤维覆盖 C18](canonical/full_fiber_coverage.md#fc-root) | \(\rho(t)\) 是定位方程的最大根，\(\rho(0)=R\)；\(h(r)>0\) 只在 \(r>R\) 定义，且 \(\rho(h(r))=r\)；\(G\subset U\times W\) 是固定窗口图 | 跨页记 \(\rho_{\rm loc}\)、\(h_{\rm cov}\)，不当作零点消失的 EB gauge 或一般模步长上界。\(G\) 不是锥约束映射或 Markov 状态域；窗口完成后的完整纤维等式只在正文显示的目标球上成立 |
| [有限代理 C19/C20-v2](canonical/finite_data_proxy.md#fd-object) | \(q\in\mathbb R^n\) 是 Cayley 查询，\(P,V\) 是样本列矩阵，\(Q\) 是严格凸 QP 矩阵，\(a>0\) 是抬升余量；\(N_m,A_m\) 由固定样本共同定义 | \(q\) 不是 EB 幂或法向几何率。只有同时取 \(a^2=M_\sigma/2\)、\(\sigma=\sqrt\gamma\) 才可调用显示的 \(K_0=R/\sqrt2\)；相同常数不使 \(A_m\) 自动等于 C03 的某个影子 |
| [一般模动力 C09/C10/C11](canonical/general_modulus_dynamics.md#gm-data) | \(\omega\) 是同图块输入对上的连续零消失模，\(h_\omega=(\mathrm{id}+\omega)/2\) 为实际步长上界，\(\ell_\omega\) 是几何采样长度预算，\(\mathcal O\) 为严格剩余预算开域；C10另取对数剖面\(\ell_a\)、完整真残差\(\chi_a\)与逆gauge\(\psi_a\) | \(\ell_\omega=h_\omega+\ell_\omega\circ\kappa\) 是预算恒等式，实际\(s+\ell_\omega(d^+)\le\ell_\omega(d)\)只为上界。C09/C11给图块T，C10经全支反演才给完整J；这些\(h,\ell\)不等于C18覆盖函数、C05扰动场或Markov子水平gauge，不同残差亦不互换 |
| [锥](cone_markov.md#c-rank) | \(G:V\to E\) 为约束映射；\(\mathfrak F\) 为最小面；\(S_{\rm dual}\) 为对偶面子空间；\(C\) 为锥 | MSCQ 的 \(d(x,G^{-1}C)\le\kappa d(G(x),C)\) 只有另引原关系 \(F_{\rm PPA}\)、局部零集等同 \(F_{\rm PPA}^{-1}(0)=G^{-1}C\) 及 \(d(G(x),C)\le\chi(r_{F_{\rm PPA}}(x))\)，才给它的真 EB |
| [Markov](cone_markov.md#m-psi) | \(K_{\rm state}\) 为紧状态集；\(\mathcal I\) 为不变律集；\(\Psi\) 为同噪声且输入 OT 最优的同步残差。C129 的 \(\mathcal R\) 属固定守恒边缘的有限 bit \(\mathsf W_\nu\)；C130 的 \(\mathcal R_Q\) 属 Gaussian \(W_{2,Q}\)，其中条件律用一维通常 \(W_2\)。C126 的 \(e,c\) 是另起的标量函数；C127 的 \(c_0\) 是 law-space 收缩系数，\(D_\eta,\Delta_\eta\) 是同一运输对的位移与回耦损失 | 同一个转移核也可有不同随机表示和不同 \(\Psi\)；\(W_2(\mu,\mu P)\)、\(\Psi\)、\(\mathcal R\)、\(\mathcal R_Q\) 不互换；[条件刷新](topics/random_markov/conditional_refresh.md) 与 [同步回耦](topics/random_markov/moment_recoupling.md) 各有对象 |
| [Markov 边界 C143/C144](topics/random_markov/compact_residual_boundaries.md#crb-object) | C143 的 δ_n 是块尺度、δ_x 是 Dirac 律；Π 是该核的显式极限，d 是到全部不变律距离。C144 重新绑定 G=[0,1]²、β 为公平 bit，ZΨ 是原残差零集 | 两对象各自定义 Ψ、P、全部不变律；一般 gauge、正幂界、law-space 尾和样本路径长度分别量化。C144 原最优计划假零不能与 C71 放松 OT 的假零合并 |
| [单 bit C145](topics/random_markov/one_bit_envelope.md#bit-object) | \(a(u)\) 是刷新概率，\(b(u)\) 是目标 bit 概率，\(h=\lvert r-b\rvert\) 是幅度，\(M=\max(b,1-b)\) 是容量；\(\ell\) 是对偶乘子，\(c\) 是刷新概率阈值，\(p\) 是例子的刷新剖面指数 | \(\ell\) 不写成 PPA 步长；\(h,M,c\) 不移作一般模、图代理或 law-space 收缩系数。\(\phi\) 是饱和的最小非降模，\(\mathcal R\) 专指本单 bit 条件残差；law-step 能量等式只在此核成立 |
| [非 tied 图](canonical/non_tied_cayley.md#nt-object) | \(A=1+\lambda\mu+\rho/\lambda\)、\(\Delta=1-4\mu\rho\) 是该页系数 | 与导数 \(A=DG(\bar x)\)、集合 \(A\) 或其它判别式无身份关系；引用 C89/C91 时连同 \(A>0,\Delta\ge0\) 门 |
| [有限数据 Q03](range_finite_data.md#q-eval) | \(e_N\) 是某候选参数 \(q\) 处的 \(N_m(q)\) 求值误差；\(e_x\) 是 \(\widehat x\) 到 \(A_m^{-1}(\widetilde v)\) 的反演误差上界 | QP gap 只给 \(e_N\)；若从该次查询生成反演证书，须合并候选参数固定点残差并除以 \(1-\sigma\)。也可另给独立的 \(e_x\)；两种误差不能同称 \(e\) |
| [解选择](canonical/solution_selection_rates.md#ss-transfer) | \(T\) 是指定同一映射，\(\Pi\) 是它的极限选择 | 要赋给原关系的全部路径，须另证 \(T=J_{\lambda F}\) 的完整纤维和共同留域 |
| [参数几何尾族](canonical/selection_parameter_family.md#pf-object) | \(A,B>0\) 均为标量增量系数，\(q\in(0,1)\) 为实际法向率；\(R\) 在 PF-3 是输入对尺度 | \(q^\gamma\) 才是共同点尾率，\(\kappa_R\) 是另一保守证书率；这里的 \(B\) 不是下行的向量值函数 |
| [三角切向充分门](canonical/selection_tangential_condition.md#tc-triangle) | \(B(a,r)\in\mathbb R^m\) 是切向增量，\(R\) 是法向域上界；\(qr\) 只在非负法向域上定义 | C139 的全符号 \(q\lvert r\rvert\) 须限制到 \(r\ge0\) 才能比较；(TC-1) 是充分条件，不从尖点例的失败推出必要性 |
| [超线性法向族](canonical/selection_superlinear_family.md#sf-object) | \(\nu>1\) 是法向递推的幂，\(\gamma\in(0,1)\) 是全对反射的局部指数；\(A,B>0\) 是标量增量系数；输入 \(r\)、图点输出 \(y=\lvert r\rvert^\nu\) | \(\nu\) 不是 C139 的几何率 \(q\)；局部图块全对模依赖输出 collar 和输入对距 \(D\)，真残差取完整两值纤维的最小值；\(\kappa_R\) 不等于实际超线性递推 |
| [固定紧源观测](canonical/compact_t_observation.md#ct-object) | \(d_{\mathrm{all}}^K(T,U)=\sup_n\|T^n-U^n\|_K\) 是整个紧源的全时间度量；\(\Phi=(w,m)\) 是实际尾和反射模 | 此度量不写成 LT 线性 EB 系数 \(\rho\)，也不是旧孔隙性账本的 \(d_{\rm dyn}\)；其 proper 证明不授予完整原关系 \(F\) 的空间 |
| [紧源塔与后继](operator_space.md#os-tower-proof) | \(V_j,L_j\) 是 \(T\) 的长度尾及全源上确界；\(e_n\) 是成对迭代的共同 Cauchy 尾；\(U\) 是同一紧 \(K\) 上已给定的连续自映射 | C131 的长度尾与 C133 的 Cauchy 尾不互换；C133 不产生非平凡连续选择；\(F_{U,K}\) 是由全输入源 \(K\) **新定义**的关系，不代表历史或既有原关系 \(F\) |
| [紧源真纤维](operator_space.md#os-fiber-eb) | 原 \(\psi\) 仅为非降逐输入传递上界；\(\phi\) 是从紧子水平集取得的 D04 型内生 gauge；\(\operatorname{dom}F_{U,K}=U(K)\)，\(r_{F_{U,K}}\) 只在该域调用 | 原 \(\psi\) 不自动满足 \(\psi(0)=0\) 和原点连续；\(J_{\lambda F_{U,K}}\) 的自然输入域是 \(K\)，不自动覆盖环境开邻域 |
| [紧图极大障碍](operator_space.md#os-compact-barrier) | C142 的 \(G\) 是**非零实 Hilbert** 中任意非空紧完整图，结论与 C132 的步界、零集及 gauge 无关 | C132 的紧源新图不可直接作为极大单调类成员；加点延拓后它不再是同一完整图，纤维和残差必须重核 |
| [紧预算步长谱](operator_space.md#os-spectrum-proof) | \(I_j=[1/j,j]\) 是实步长的紧参数域；\(B_{C,j}\subseteq X\times I_j\) 是**逐认证类**声明的闭预算关系，\(\Sigma_{C,j}\) 允许空值 | 闭关系给上半连续和闭存在投影，但不自动给下半连续；LT/direct/energy 三类各自的实际闭性、耗尽性及类别比较尚须证明 |
| [例库](topics/examples/README.md) | \(F,K,B,G,R\) 在每张卡内重新绑定 | 必须携带空间、完整/受限图、目标、步长、输入/输出窗、真实或算法残差；GX 编号只标来源观察 |
| [AGM C146–C148](topics/examples/arithmetic_geometric_mean.md#agm-object) | P=[0,∞)²是完整近端输入域，D={s≥t≥0}是输出/原算子域，G是AGM自映射；R是W_R的位置窗上界，M是AGM标量极限 | P不是Markov核，D不是数据尺度，R不是仅对距上限；d=√(s²−t²)是该页标量，r_F仍取完整纤维inf。Π轴处坏模与正初值Q二次不统一 |
| [共同尾 C149](canonical/selection_truncation_prior_tools.md#st-lipschitz) | L:X→X是映射，k是其Lipschitz常数，ρ是共同增量的几何率；辅助版本T和u为不同映射 | L不代入RL系数，ρ不是EB系数；只沿uⁿ收敛，不将其尾换成Tⁿ |
| [GX 图缺陷 C150–C156](canonical/parameter_dictionary.md#pd-geometry) | hypo/cohypo为非负单参数缺陷，signed τ另允许负数；每卡λ固定，MR目标重新指定 | inner product/范数写法覆盖Hilbert；标量才简写ab。固定窗锐系数与缩窗下确界分开，非零原算子目标不默认零集PPA |
| [选择文献 C157/C158](canonical/selection_literature_boundaries.md) | LT的τ是非负标量；LMZ的τ(t)是误差率函数；KR的τ(q)是相位支配指标；P16的α=(3+7e)/3，与averaged参数α无关 | 每节独立绑定，跨节写τ_LT、τ_LMZ、τ_KR和α_P16。LMZ惩罚系数μ与标准步长h=1/μ为倒数；C157每个见证分别定义T/Π，不合并成同一算子 |
| [Spingarn作者版本](canonical/spingarn_author_definitions.md#sp-first-order) | SP80-A固定输入仍量化全部锚输出，SP80-S只令两输入趋近；SP81-H每bounded K另取k_K | 输出不要求共同趋一图点；图闭/凸值是SP80声明类门。SP81全类极大性允许变局部系数，不等于固定σ或固定LT窗口极大性 |

## 统一验收问题

本轮三条接口另固定如下绑定，引用时连同窗口和身份携带：

| 模块 | 固定绑定 | 跨页使用门 |
| --- | --- | --- |
| [signed-Schur](canonical/signed_schur_growth.md#ss-interface) | 参数片 Q、全表示图 G_rep、切向输入片上的 Γ=G_rep∩X⁻¹(B_r×ℝ)、原完整关系 F 及领圈 U 分开；一般模 ω 与附加幂增长 p 的 RL 指数 1/p 分开 | 切向输入片内表示图点对的一般模不自动成为幂型 RL；转给完整 J 须 U 上全部纤维同一。仅选中输出在图册重叠处一致只支持该选择 |
| [块路径 C163/C164](canonical/path_atlas.md#pa-lift) | B_m 是全部合法末点关系，B(t) 是标量步界；Λ 是新关系的块编码步长；G 是块长度包络、H 是级数预算 | 记忆/相位规则及空间度量固定；新定义 F_{m,Λ} 不等于原生生成 F。有限进入、吸收、首次进入即停、全部后继驻定分别使用 |
| [复合 C161/C162/C165](canonical/composite_subregularity.md#cs-local-target) | Γ=zer ∂f，Θ₂ 使用实际 second subderivative；S=c⁻¹(argmin φ)，T 是闭 stationary 子目标；A=Dc(x̄)，B=A† | T 不是近端映射，Γ 不是随意图块；Clarke PSD 不替代 Θ₂。局部集合相等经球外隔离才给实际窗内全局距离相等 |

引用一条边前依次检查：同一完整对象或明确图块？同一 \(\lambda\) 和成对尺度？目标是完整零集还是指定子集？残差取 inf、选中值、步长还是概率耦合？前提对**所有**图点/输出/初值还是仅存在一个选择？条件是在同一窗口合取，还是来自不同稿件的可比实例？最后查 [条件契约](LOGIC_CONTRACTS.md) 与 [现存失败机制](../FAILED_ROUTES.md)。相同字母和相近指数都不能省掉这些问题。

本页由 2026-10-02 跨文件核对建立：早先出现过的 `RL(λ,L,γ)` 现已统一为 `RL(λ,γ,L)`；锥面 \(F\) 与 \(r_F\) 的错位、条件 Markov 摘要缺定义及 C16 的 \(\rho=0\) 端点也已修正。本轮另将 Q03 的 \(e_N/e_x\) 分型。此核对覆盖入口及部分承重链；不是对全部 346 个内容组或全部证明的穷尽审稿。

## 同 gauge 与文献算法参数的新增接口

[C159](canonical/gauge_dilation_boundary.md#gd-theorem) 的 ψ 是固定逐点函数，ψ(2t) 不能无条件换为 Cψ(t)；其离散自然输入域 D不含邻域 coverage，正点不连续不得混入要求连续 gauge 的定理。[C160](canonical/selection_quasi_arithmetic_boundary.md#qa-object) 的 D 是均值初值直径预算、K 是生成元对数导数界、q=αℓ是修复尾的辅助系数；都不等于RLEB的输入对尺度、RL常数或实际法向率。N是非负起步，不能使用负迭代次数。QA使用∞范数，转Euclidean点尾须乘√k。

[LMZ接口](canonical/selection_primary_interfaces.md) 的 λ_L 乘在目标二次项上，项目 prox 步长 h=1/λ_L。其 ψ(d)≤γr 是距离侧函数方向，与本库残差侧 d≤ψ(r) 比较时须先求逆并核定义域，不能直接同形代入。P16的 φ 是固定 M 的外层复合函数；QA-COMPARISON中的 F为不变标量函数，与PPA完整集值关系 F 不同型，跨页调用时重命名为 f_inv。
## 完整母空间工具与条件刷新新增绑定

[C166–C168/C172](canonical/operator_profile_tools.md#op-profile)的 \(\mathcal B_{F,V,S}\) 是完整图值剖面，真残差仍为inf；\(\psi(r+)\) 不默认等于 \(\psi(r)\)。\(\mathcal K\) 是实际对象的统一紧块，不是状态域；\(C_i\) 是闭约束；\(\mathcal A_M\) 是固定评价必要层，\(M\) 不代入RL系数。C172的\(p\)是剖面阶，兼容量词为存在正\(\kappa<1\)和共同小窗。

[C169–C171](topics/random_markov/finite_state_completion.md#fsc-object)的 \(\mathcal J\) 是明确给定的紧凸多面体目标，可不同于不变律集；\(E_{\mathcal J}\) 和 \(\Phi_{\mathcal J}\) 都是平方量，\(B_*\) 是平方EB系数、\(K_*=\sqrt{B_*}\)。概率列向量的更新是\(P^\top\mu\)。真实核率和显示的almost-firm标量充分公式分别判断。

[C173–C175](topics/random_markov/conditional_refresh_interfaces.md#cfi-gibbs-object)的 \(C\) 是非负影响矩阵，\(w\) 是状态差成本权重；CF3的任意\(w>0\)与CF4的特定构造权重不得互换。\(D_{\rm cond}\)只是在各明确模型里重绑定的条件残差，不是同步\(\Psi\)；\(\epsilon_*\)固定同一随机映射表示和Euclidean成本。[C177](canonical/topological_repair_obstructions.md#tr-germ)的\(Q\)是germ商，不是Gaussian正定矩阵；商Baire性和Polish性分别判断。
