# 第二轮原创性与研究价值审核：RLEB 解选择坏类的大小

日期：2026-09-20。角色：独立原创性／价值审核，不承担本轮数学终裁。已完整读完 `01_operator_space.md`—`05_rleb_robustness.md`；本报告仅新建此文件，没有修改用户稿件或五份第一轮报告。下列数学判断以明确写出的量词为准，不重新审查原 RLEB 基础理论。

## 0. 总判

**CONDITIONAL：值得发展为“保多解结构的扰动与分层”研究；目前不够支持一篇已经完成的一般泛性论文。**

- 有价值的设问是真的：从一个坏例推进到一个事先指定、保持同一多解几何及严格收敛证书的空间，问坏选择究竟有多大。
- Baire 空间、相对拓扑、prevalence、半代数分层本身都是现成框架；“把算子放进函数空间”不是新定理。
- 本轮具体新增是**同一零集、共同严格 RLEB 常数、同一真实 min-residual EB、完整二值 resolvent 下的可显式核算相图，以及选择 Hölder 性对保结构极限的不闭合**。这比任意连续函数的平滑逼近有实质约束，但还不是全 RLEB 类的大小定理。
- 目前最合适的用途：给原 solution-selection 稿增添一个“证书保持下的奇异扰动／稳定性退化”命题或小节。要独立成为新的泛性论文，建议再取得一个真正的结构族定理或保结构稠密／开放性定理。这里不是要求一定证明“所有 RLEB 的泛性”，而是要求对象超出一个为了展示结论而定制的二参数公式。
- 上述判断只评价本轮 idea 和新增结果，**不撤销、不重判原 solution-selection 论文的贡献**。

## 1. 哪些部分已有，哪些是本轮新推导

| 内容 | 审核判断 | 准确增量与限制 |
|---|---|---|
| 在 resolvent 空间上使用 Baire 范畴研究典型算子 | 已有成熟先例 | Wang、Planiden–Wang 已做算子／resolvent 完备空间与泛型唯一零点；不能再次作为新思想出售 |
| 固定解集、常数、兼容余量，取闭约束层；用紧性与共同尾界得到极限映射连续依赖 | 标准方法的认真接口实现 | 对非单调、有限值 RLEB 类的精确版本有工具价值，但尚未产生“大／小”结论 |
| 至多二对一为 `G_delta`，正阶 Hölder 好类为 `F_sigma`，坏类为 `G_delta` | 标准拓扑／可数化步骤 | 有助于把任务变成闭集是否无处稠密；`G_delta` 不是 `residual`，也没有完成密度证明 |
| 尖点幅度 \(B>0\) 的一整片严格兼容参数为坏例 | 原稿参数构造的直接加强／整理 | 排除“仅一个精确系数巧合”；不能推出在函数空间中坏类有内点 |
| 切向削圆后好、未削圆坏，同时共同证书全部保留 | 本轮真实显式推导候选 | 局部化、全纤维、min-residual 与 all-pairs RL 同时保留具有技术内容；好端的 Hölder 恢复使用已有截断平衡 |
| 坏集在尖点层满测，而在削圆扩展族余维一、零测 | 上一行的精确推论 | 一旦动力学好／坏判别闭合，维数／测度本身就是基础事实；不能用这些术语让同一例子显得像一般分类 |
| 一致图／resolvent 极限下 Good 不闭，幅度趋零下 Good 不开 | 值得保留的非鲁棒性结论 | 精确地说是所给点与共同证书层中的序列见证；没有得到 Good、Bad 在全空间的所有拓扑性质 |
| 全 RLEB 坏类 meagre／residual／shy／prevalent | 未证明 | 五份报告没有这项结论；现有原始文献也不能直接补上 |

第二行的闭图编码 \(F_T=(T^{-1}-I)/\lambda\) 本身不新；价值不应算在编码公式上，而应算在编码之后仍能保持全部证书并发生奇异选择退化的联合性质上。

## 2. 定理级先行文献对应

以下定理号均按实际读取的原文版本。只有出版摘要的条目明确标为未闭环；没有用检索未命中证明首创。

### P1. 泛型唯一解已经有直接 resolvent 先例，但不能限制到固定多解层

**Xianfu Wang**, *Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent*, Nonlinear Analysis 87 (2013), 69–82。DOI [10.1016/j.na.2013.03.008](https://doi.org/10.1016/j.na.2013.03.008)；[arXiv:1301.6443v1 原文](https://arxiv.org/pdf/1301.6443)。本轮独立读取 Propositions 2.1、2.3、2.4，Theorem 2.13 及 Theorems 2.14–2.16、Corollary 2.17。

相关假设为实 Hilbert 空间中的非扩张／firmly nonexpansive／最大单调空间，使用有界集上一致距离；Theorem 2.13 要求完整子空间内严格收缩稠密。结论为典型迭代在每个有界球上一致趋于一个点。

**已覆盖：**算子空间、resolvent 度量、Baire 典型收敛与唯一零点这一整条方法线。

**未覆盖：**固定非单点 \(S\) 的 Hölder RLEB 层，以及 \(\Pi_T\) 对初值的非 Hölder 性。若 \(T|_S=I\)，任意 \(s\ne t\in S\) 满足

\[
\|Ts-Tt\|=\|s-t\|,
\]

严格收缩根本不在此层内；核心稠密前提失效。外部 residual 唯一解集与固定多解层完全不交，并不构成矛盾。另有更直接的障碍：非扩张迭代若存在点极限，则 \(\Pi_T\) 自动 1-Lipschitz，坏类在该经典收敛类内为空。

### P2. 凸 proximal 空间的版本也已建立

**Chayne Planiden、Xianfu Wang**, *Most Convex Functions Have Unique Minimizers*，[arXiv:1410.1078v1](https://arxiv.org/pdf/1410.1078)。本轮核读 Corollary 3.5 与 Theorems 4.2、4.6–4.8。

对象是 \(\mathbb R^n\) 上 proper lsc convex 函数的 proximal 映射；唯一极小点与 proximal super-regularity 对应，唯一 fixed point／zero／minimizer 在相应完备空间中泛型。

**已覆盖：**真正凸 prox 类中的 ambient generic 唯一解。

**未覆盖：**非势、非单调、尖点型完整 resolvent，以及固定多解选择。把本轮模型叫 proximal 不会使其落入该凸函数空间；也不能把此有限维结果未经补证扩大到无限维函数类。

### P3. 固定共同连续模的典型饱和已有更贴近 Hölder 的文献

**Davide Ravasini**, *Generic uniformly continuous mappings on unbounded hyperbolic spaces*, J. Math. Anal. Appl. 538(1) (2024), 128440。DOI [10.1016/j.jmaa.2024.128440](https://doi.org/10.1016/j.jmaa.2024.128440)；[arXiv:2308.15277v2 原文](https://arxiv.org/pdf/2308.15277)。本轮独立核读 §2 的空间与度量、Theorem 3.3 及其保模扰动证明开头。

在完备无界双曲度量空间 \(X\) 上，固定凹、非零、非降且在零点取零的共同模 \(\omega\)，以 bounded-uniform 拓扑研究 \(\mathcal C_\omega(X)\)。Theorem 3.3 给典型映射的**一步**全局模等于 \(\omega\)。

**已覆盖：**不仅非扩张，连固定 Hölder／凹模空间中“典型对象达到允许的最坏正则性”也有直接先例。

**未覆盖：**固定解平面、统一 RLEB 预算、二对一限制、轨道收敛及无限迭代极限选择。它的全局模饱和可能由远处输入对见证，不能变成本任务中每个小初值邻域的两点失稳。\(T_{\mathrm{good}}(z,p,r)=(z+\sqrt{|r|},p,|r|/4)\) 已说明一步存在真正平方根尖点，并不妨碍极限选择具有 \(1/2\)-Hölder 性。

Ravasini 原文追溯到 **Filip Strobin**, *Some porous and meager sets of continuous mappings*, J. Nonlinear Convex Anal. 13(2) (2012), 351–361。Strobin 原文和定理号本轮未直接取得，因此只保留为历史线索；上述定理级判断直接依据已读 Ravasini 原文，不冒充已逐页核过 Strobin。

### P4. 拓扑改变真的会改变典型 fixed point 结论

**Davide Ravasini、Daylen K. Thimm**, *Generic nonexpansive Hilbert space mappings*，[arXiv:2407.03881v2](https://arxiv.org/pdf/2407.03881)。本轮核读 §2、Theorems 3.4、4.1、4.2、5.3。

在可分无限维 Hilbert 空间闭凸域上的非扩张自映射空间，采用**逐点拓扑**：somewhat bounded 域与 totally unbounded 域的典型 fixed point 存在性不同；特别地全 Hilbert 空间的典型映射无 fixed point。这与 P1 的 bounded-uniform 结论没有冲突。

**覆盖与缺口：**它给“典型性依赖明确环境”的一手证据，但不证明当前参数相图，更不处理 RLEB 固定多解层。当前无需为了使用泛函分析而先把状态空间推广成无限维。

### P5. “一步 Lipschitz＋统一几何尾 ⇒ 极限 Hölder”不是本轮新引理

**Andrzej Wiśnicki**, *Hölder continuous retractions and amenable semigroups of uniformly Lipschitzian mappings in Hilbert spaces*, Topol. Methods Nonlinear Anal. 43(1) (2014), 89–96；[arXiv:1204.6464v2](https://arxiv.org/pdf/1204.6464)，**Lemma 1**。本轮直接核读该引理及证明。

其有界完备域上的 Lipschitz 单步与共同几何增量给实际极限回缩的 Hölder 性，证明为有限步差和两条尾界的截断平衡。

**已覆盖：**04 中 \(h\ne0\) 的切向子系统，以及 05 中 Hölder 法向换元后的 Lipschitz 系统，其恢复正 Hölder 阶所用的核心机制。

**未覆盖：**将削圆放进同一严格 RLEB、真实 residual、完整二值 resolvent 族，同时保留未平滑的法向奇异并证得好坏退化。这个联合接口不是由“引理已知”就被整体覆盖。

### P6. 半代数 Sard／generic optimization 是右端或问题参数的定理

**A. D. Ioffe**, *A Sard Theorem for Tame Set-Valued Mappings*, J. Math. Anal. Appl. 335 (2007), 882–901；DOI [10.1016/j.jmaa.2007.01.104](https://doi.org/10.1016/j.jmaa.2007.01.104)；[arXiv:math/0607697v1](https://arxiv.org/html/math/0607697v1)，**Theorem 1**。本轮独立核读定理及相关临界值定义。tame 局部闭图映射的度量临界值 \(\sigma\)-porous；可定义时进一步低维。

**Dmitriy Drusvyatskiy、A. D. Ioffe、Adrian S. Lewis**, *Generic Minimizing Behavior in Semialgebraic Optimization*, SIAM J. Optim. 26(1) (2016), 513–534；DOI [10.1137/15M1020770](https://doi.org/10.1137/15M1020770)；[arXiv:1504.07694v1](https://arxiv.org/html/1504.07694v1)，**Theorems 3.7、4.16**。本轮独立核读这两条：小维图多值映射对一般右端值有局部解析逆支；半代数优化经一般线性扰动后具有有限临界点及非退化结构。

**已覆盖：**“有限几何中临界值薄，非退化参数一般”这一框架。

**未覆盖：**保持 \(S\) 不被打散的受限扰动，以及 \(T_\theta^k\to\Pi_\theta\) 的无限动力学正则性。每个有限迭代半代数不推出极限半代数，故不能把 \(\{\theta:\Pi_\theta\text{ 非 Hölder}\}\) 自动交给半代数维数理论。有限几何判别集与极限选择坏集之间的动力学桥梁，是潜在新工作。

### P7. 相关 VI 优先权仍有一项全文门

**Jae Hyoung Lee、Gue Myung Lee、Tiến-Sơn Phạm**, *Genericity and Hölder Stability in Semi-Algebraic Variational Inequalities*, JOTA 178 (2018), 56–77；DOI [10.1007/s10957-018-1234-4](https://link.springer.com/article/10.1007/s10957-018-1234-4)。本轮核到正式出版页与摘要，全文订阅受限，**不提供未核实的定理号**。

摘要对象是参数化 VI 的解映射及典型有限非退化解，不是固定算法的初值极限选择。此差异足以说明不能立即套用，但不足以声称全文没有任何可迁移定理。若发展成论文，此项仍须取得原文并完成精确比对。

### P8. Prevalence 是标准工具，而且本轮候选 compact 证书层在外部已经 shy

**Brian R. Hunt、Tim Sauer、James A. Yorke**, *Prevalence: a Translation-Invariant “Almost Every” on Infinite-Dimensional Spaces*, Bull. Amer. Math. Soc. 27 (1992), 217–238；[arXiv:math/9210220 原文](https://arxiv.org/pdf/math/9210220)，**§2 Definitions 1–2、Facts 3″、8**。本轮直接核读。

它要求完整度量线性环境，测试测度对例外集的**所有平移**都给零；Fact 8 说明无限维环境中的紧集 shy。有限参数一次抽样不满足“每个背景”的量词。

本轮可立即得出一个比笼统“prevalence 不自然”更明确的判断：若采用 01 的已证明紧证书层 \(\mathcal X\subset C_{\mathrm{loc}}(\mathbb R^d,\mathbb R^d)\)，则该外部空间是无限维完整度量线性空间，故

\[
\mathcal X\text{ shy},\qquad
\mathrm{Good}\subset\mathcal X,\quad
\mathrm{Bad}\subset\mathcal X.
\]

于是两类在外部都包含在 shy 集中，**外部零测型结论完全不能比较内部多少**。这是 P8 与 01 紧性的直接推论，不是新的 prevalence 定理。若要继续使用测度，应先使用明确的有限参数概率，或重新设计有理由的相对测度结构。

## 3. 相对 Baire 空间设计是否足够自然

01 的设计是合格起点：固定非单点仿射 \(S\)，固定 \(\gamma,L,\psi,\lambda,R,\rho,\kappa<1\)，把 \(T\) 当变量。先保住收敛与完整图接口，再研究选择。它并不是根据“好／坏”结果反向定义空间，因此不是循环定义。

但它仍有必须对读者交代的模型取舍：

1. 全空间 min-residual EB 比原来的局部理论更强；这是避免隐藏纤维的清洁模型，不是“全部 RLEB”。
2. 固定同一个精确常数层会影响允许扰动。严格兼容留余量，不等于每个 all-pairs 不等式都留了可用的自由度；某些映射可能饱和固定 RL 上界。
3. 固定 \(\mathcal X_{\le2}\) 不等于固定半代数类。半代数成员不在任意一致极限下闭合；若定理只在连续 resolvent 层成立，不能把结论自动限制到半代数成员。
4. 完整 `C^gamma` 范数和 compact-open／图拓扑是不同研究对象。05 的削圆序列只证后者、以及较低 Hölder 范数的逼近，不能据它宣判强 `C^gamma` 中的内点或范畴。

这些取舍并不否定空间自然性；它们说明需要在研究开始前声明“允许什么误差和扰动”，不能证明后选择能得到漂亮结论的母空间。

## 4. 满测尖点层与余维一扩展族：价值有多大

以 04 的族为例，令

\[
T_{b,h}(z,p,r)=\left(z+\sqrt{|r|},\ p+b[\sqrt{c(p,r)+h^2}-|h|],\ |r|/4\right),
\quad c(p,r)=\min\{p_+,|r|\}.
\]

在报告指定参数域内，候选分类是

\[
\mathrm{Bad}\cap\Theta=\{h=0\},\qquad
\mathrm{Bad}\cap\Theta_0=\Theta_0,
\quad \Theta_0=\Theta\cap\{h=0\}.
\]

**它解决的不是“全球多少”，而是两个更具体的问题：**

- 坏机制不是幅度系数必须精确等于一个值才存在；在保持尖点类型的结构层内，它持续存在。
- 对同样满足严格 RLEB 的自然切向削圆，它可以消失；RLEB 常数并不记录这种正则化差别。

这两条足以给当前论文增加一个有用的“鲁棒性边界”。第一条不能被一个光滑定理推翻；第二条也不能用“坏层满测”掩盖。它们共同解释应该控制哪个切向结构。

不过，**余维一并非已识别的普遍机制**。这里是自己引入一个削圆参数，然后精确在它取零时保留尖点；这种超平面形状在参数设置里已经有明显来源。要把它升格为一般理论，必须说明在预先定义的更广族里如何生成退化判别式，并证明其与坏无限动力学的关系，而不是仅重复“\(h=0\) 是零测”。

另有一个需要严格保留的量词：04 的

\[
\alpha(b,h)=\min\!\left\{\tfrac12,
\frac{\log4}{\log4+\log(1+b/(2|h|))}\right\}
\]

只是已证明的**可保证阶**。它随 \(h\to0\) 趋零，不自动证明每个模型的最佳 Hölder 阶趋零。共同正阶与共同常数不可能跨越坏极限，这一点可由一致极限论证得到；但“没有共同阶和常数”与“最佳阶一定坍缩”不同。若能独立求得匹配上下界，定量退化价值会明显提高。

## 5. 我认为最小可成立的研究交付包

### 路径 A：作为现有 solution-selection 稿的加强，当前已有良好候选

一个紧凑命题包即可：

1. 固定同一多解 \(S\)、实际法向速率 \(q\)、共同严格 RLEB 常数、完整二值及 min-residual 证书；
2. 证明坏模型可被好模型在 uniform-resolvent 与完整图 Hausdorff 距离中逼近；
3. 证明幅度趋零使坏模型趋向好模型，并明确所用拓扑；
4. 得到选择 Hölder 性不由这些共同证书及所选弱拓扑稳定控制，给出有限参数相图与非一致退化说明。

标题宜围绕“证书保持的奇异扰动”，不是“RLEB 泛型稳定”。数学通过独立审核且相关工作补齐后，适合并入原稿；不必为此先解决全类的 Baire 大小。

### 路径 B：独立的新论文方向，仍缺一个主体定理

建议下面二选一，而非全部强制完成：

**B1. 结构族定理。** 先于结论确定一个非平凡固定复杂度、保多解与法向奇异的图族。由可检查的切向非退化／可和放大条件，证明判别集外极限选择 Hölder，并估计指数或常数随到判别集距离的退化；同时用坏层给必要性或匹配下界。仅再使用一次标准 Lipschitz 截断引理，不足以组成该主体。

**B2. 相对扰动定理。** 在 01 的某个明确 Baire 层或有自然理由的各向异性子层，证明真正的密度、无处稠密、相对开放、porosity，或稳定／坏机制共存的结构性结论。关键是对任意给定背景算子的小扰动保持完整纤维、二值数、真实 residual、all-pairs RL 与共同预算。一个具体模型的削圆序列不替代“任意背景”。

这种“最小包”是当前研究价值建议，不是保证期刊接受的数学阈值。若只做到 A，最合理选择是强化已有论文，而不是为了增加篇数拆出一篇小泛性文章。

## 6. 不能声称的结论

- “RLEB 坏类整体零测／第一纲”或“整体满测／余稀”。
- “坏类是 `G_delta`，所以典型”。还缺稠密性。
- “ambient generic 唯一解，所以固定多解层通常稳定”。量词不允许这样限制。
- “有限维参数满测，所以在无限维上 prevalent”。缺所有平移／任意背景的测试条件。
- “半代数数据，所以好坏参数集自动半代数”。无限迭代极限不能自动量词消去。
- “削圆可以逼近本例，所以所有坏算子都可由好算子逼近”。后者未证。
- “证书阶趋零，所以最佳阶已被证明趋零”。未取得匹配上界。
- “共同常数”指该族可用的共同认证预算，不是每个模型已经求得的最小 RL 常数或最优 EB 常数。
- “此路线已有基础框架，所以原 solution-selection 方向没有原创性”。P1–P8 没有覆盖原稿的整个联合贡献，也没有本轮新增联合接口的精确覆盖证明。

## 7. 尚未闭合的优先权和价值问题

1. 没有取得 Lee–Lee–Phạm 2018 全文；不能以摘要完成终极优先权排除。
2. Strobin 2012 原文未直接核到；已读 Ravasini 2024 给足了当前方法先例，但若文章讨论固定模典型性应补历史原文。
3. 还需定向比对正常吸引／稳定叶及有奇异接缝的分段动力系统中“平滑参数趋零导致极限回缩正则性退化”的结果。这些可能覆盖削圆机制的一部分；当前不能宣布精确构造世界首创。
4. 目前没有一般的、保持全部 RLEB 证书的保结构拼接／稠密扰动引理。
5. 当前参数族的自然性可以由“只削圆切向尖点且不改变收敛认证”说明，但还不等于来自一个实际优化算法族的参数扰动。若能找到这样的算法来源，独立论文价值会更强。

**给总审的最终建议：批准一次有边界的结构族研究，不批准直接宣称全类大小，也不建议首先投入无限维 prevalence。先保留本轮相图作为已有研究的可审核加强；下一里程碑应是 B1 或 B2 的一个清晰主体定理。**
