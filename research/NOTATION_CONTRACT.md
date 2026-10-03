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

| 模块 | 局部记号 | 跨模块调用时的类型与桥 |
| --- | --- | --- |
| [锥](cone_markov.md#c-rank) | \(G:V\to E\) 为约束映射；\(\mathfrak F\) 为最小面；\(S_{\rm dual}\) 为对偶面子空间；\(C\) 为锥 | MSCQ 的 \(d(x,G^{-1}C)\le\kappa d(G(x),C)\) 只有另引原关系 \(F_{\rm PPA}\)、局部零集等同 \(F_{\rm PPA}^{-1}(0)=G^{-1}C\) 及 \(d(G(x),C)\le\chi(r_{F_{\rm PPA}}(x))\)，才给它的真 EB |
| [Markov](cone_markov.md#m-psi) | \(K_{\rm state}\) 为紧状态集；\(\mathcal I\) 为不变律集；\(\Psi\) 为同噪声且输入 OT 最优的同步残差。C129 的 \(\mathcal R\) 属固定守恒边缘的有限 bit \(\mathsf W_\nu\)；C130 的 \(\mathcal R_Q\) 属 Gaussian \(W_{2,Q}\)，其中条件律用一维通常 \(W_2\)。C126 的 \(e,c\) 是另起的标量函数；C127 的 \(c_0\) 是 law-space 收缩系数，\(D_\eta,\Delta_\eta\) 是同一运输对的位移与回耦损失 | 同一个转移核也可有不同随机表示和不同 \(\Psi\)；\(W_2(\mu,\mu P)\)、\(\Psi\)、\(\mathcal R\)、\(\mathcal R_Q\) 不互换；[条件刷新](topics/random_markov/conditional_refresh.md) 与 [同步回耦](topics/random_markov/moment_recoupling.md) 各有对象 |
| [非 tied 图](canonical/non_tied_cayley.md#nt-object) | \(A=1+\lambda\mu+\rho/\lambda\)、\(\Delta=1-4\mu\rho\) 是该页系数 | 与导数 \(A=DG(\bar x)\)、集合 \(A\) 或其它判别式无身份关系；引用 C89/C91 时连同 \(A>0,\Delta\ge0\) 门 |
| [有限数据 Q03](range_finite_data.md#q-eval) | \(e_N\) 是某候选参数 \(q\) 处的 \(N_m(q)\) 求值误差；\(e_x\) 是 \(\widehat x\) 到 \(A_m^{-1}(\widetilde v)\) 的反演误差上界 | QP gap 只给 \(e_N\)，必须加候选参数固定点残差并除以 \(1-\sigma\) 才能传给 \(e_x\)；不能把它们叫同一个 \(e\) |
| [解选择](canonical/solution_selection_rates.md#ss-transfer) | \(T\) 是指定同一映射，\(\Pi\) 是它的极限选择 | 要赋给原关系的全部路径，须另证 \(T=J_{\lambda F}\) 的完整纤维和共同留域 |
| [固定紧源观测](canonical/compact_t_observation.md#ct-object) | \(d_{\mathrm{all}}^K(T,U)=\sup_n\|T^n-U^n\|_K\) 是整个紧源的全时间度量；\(\Phi=(w,m)\) 是实际尾和反射模 | 此度量不写成 LT 线性 EB 系数 \(\rho\)，也不是旧孔隙性账本的 \(d_{\rm dyn}\)；其 proper 证明不授予完整原关系 \(F\) 的空间 |
| [紧源塔与后继](operator_space.md#os-tower-proof) | \(V_j,L_j\) 是 \(T\) 的长度尾及全源上确界；\(e_n\) 是成对迭代的共同 Cauchy 尾；\(U\) 是同一紧 \(K\) 上已给定的连续自映射 | C131 的长度尾与 C133 的 Cauchy 尾不互换；C133 不产生非平凡连续选择；\(F_{U,K}\) 是由全输入源 \(K\) **新定义**的关系，不代表历史或既有原关系 \(F\) |
| [紧源真纤维](operator_space.md#os-fiber-eb) | 原 \(\psi\) 仅为非降逐输入传递上界；\(\phi\) 是从紧子水平集取得的 D04 型内生 gauge，\(r_{F_{U,K}}\) 只在 \(u\in U(K)\) 调用 | 原 \(\psi\) 不自动满足 \(\psi(0)=0\) 和原点连续；\(J_{\lambda F_{U,K}}\) 的自然输入域是 \(K\)，不自动覆盖环境开邻域 |
| [例库](topics/examples/README.md) | \(F,K,B,G,R\) 在每张卡内重新绑定 | 必须携带空间、完整/受限图、目标、步长、输入/输出窗、真实或算法残差；GX 编号只标来源观察 |

## 统一验收问题

引用一条边前依次检查：同一完整对象或明确图块？同一 \(\lambda\) 和成对尺度？目标是完整零集还是指定子集？残差取 inf、选中值、步长还是概率耦合？前提对**所有**图点/输出/初值还是仅存在一个选择？条件是在同一窗口合取，还是来自不同稿件的可比实例？最后查 [条件契约](LOGIC_CONTRACTS.md) 与 [现存失败机制](../FAILED_ROUTES.md)。相同字母和相近指数都不能省掉这些问题。

本页由 2026-10-02 跨文件核对建立：早先出现过的 `RL(λ,L,γ)` 现已统一为 `RL(λ,γ,L)`；锥面 \(F\) 与 \(r_F\) 的错位、条件 Markov 摘要缺定义及 C16 的 \(\rho=0\) 端点也已修正。本轮另将 Q03 的 \(e_N/e_x\) 分型。此核对覆盖入口及部分承重链；不是对全部 346 个内容组或全部证明的穷尽审稿。
