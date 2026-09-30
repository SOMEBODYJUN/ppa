# RLEB 算子类的测度大小：prevalence、概率模型与适用边界

日期：2026-09-20。角色：第 3 组，测度／概率泛性独立评估。本文不重新审查原 RLEB 论文，不修改任何已有稿件。内部依据为 `solution_selection_revised_v1/research_note.md` 的 §1、(3.6)–(3.8)、§5.2；这些接口以此前通过的数学审计为前提。

## 0. 结论先行

用户的想法是有意义的：从“存在坏选择反例”升级为“坏选择在一个明确的算子族中到底多大”，是不同而可能有价值的问题。但应当区分三句话：

1. **给定拓扑下，坏算子是 residual／meagre。** 这是 Baire 纲论问题。
2. **给定随机生成模型下，坏算子具有多大概率。** 这是模型依赖的概率问题。
3. **给定完整线性／群结构下，坏算子 prevalent／shy。** 这是平移意义的测度泛性问题。

三者不能互相替代。尤其目前的“闭图、至多二值、RLEB、完整 resolvent、非唯一零集”类不是天然的向量空间或 Polish 群，没有现成的“全体 RLEB 算子的均匀分布”。

**建议的第一步是固定解集与统一证书裕量后的有限参数概率／相对开集问题，暂不直接宣称无限维 prevalence。** 一个很具体的事实已经可以从现有参数族推出：在稿件 (3.6) 的自然 cap 系数参数区间内，坏选择是相对开稠密且 Lebesgue 满测度的；这仍不等于它在所有 RLEB 算子中是典型的。

## 1. 首先明确是在给谁测大小

记固定工作域上的允许算子类为 \(\mathscr C\)，每个算子通过已验证的完整 resolvent 给出 \(T\)，并具有共同初值域上的极限选择 \(\Pi_T\)。例如研究

\[
\mathscr B=\{T\in\mathscr C:\Pi_T\text{ 在指定初值域上没有任何正阶两点 Hölder 模}\}.
\]

这里测量的是“坏**算子**的集合”，不是单个算子下“坏**初值**的集合”。也不是“在解点的 Hölder calmness 失败”：本稿的坏模型仍具有解点处的 calmness，只是在完整邻域上缺乏统一两点 Hölder 性。

完整问题至少须先固定：维数、工作域、解集（或允许的解集分层）、步长、Hölder 指数、完整 resolvent 约束、统一收敛／局部化预算，以及算子之间的距离。若这些对象跟随抽样不受控制，所谓“坏类大小”可能只是吸引域消失或解集坍缩的结果。

## 2. 不能使用无限维 Lebesgue 测度

在无限维可分 Banach 空间 \(E\) 上，不存在非零、平移不变、局部有限的 Borel 测度，可以扮演有限维 Lebesgue 测度的角色。

基本证明很短：若某个球的测度有限，无限维性允许在其中放入无穷多个等半径互不相交小球；平移不变性迫使这些小球测度为零；可分性又使全空间被可数个同半径球覆盖，于是测度恒零。这个论证见 Hunt–Sauer–Yorke 的引言。[原始论文](https://arxiv.org/pdf/math/9210220)

因此“随机选一个 RLEB 算子，问坏选择的概率”需要**先给随机模型**；“在某个 Banach 空间里几乎处处”也必须说明其准确含义。

## 3. Prevalence／shy／Haar-null 的准确接口

### 3.1 定义与量词

设 \(E\) 是完整度量线性空间。Borel 集 \(B\subset E\) 称为 shy，如果存在紧支撑 Borel 概率 \(\mu\)，满足

\[
\boxed{\quad \forall v\in E,\qquad \mu(v+B)=0.\quad}
\tag{P}
\]

补集称为 prevalent。更一般集合通过 Borel shy 包络定义。Christensen 的 Haar-null 在 abelian Polish 群上使用相同的“所有平移均为零”的思想；它不要求向量空间，但要求明确的群运算。

这里不是只检查 \(\mu(B)=0\)，而是**同一个**测试测度须消灭 \(B\) 的**全部**平移。Hunt–Sauer–Yorke §2，Definitions 1–2 给出上述定义；有限维情形与 Lebesgue 零集一致。[HSY 原文](https://arxiv.org/pdf/math/9210220) Christensen 1972 的出版记录、题名与 DOI 已核；可直接读到的作者本人 1973 文说明定义及群结构要求。[1972 记录](https://doi.org/10.1007/BF02762799)、[1973 作者原文，pp.29–31](https://www.numdam.org/item/PDML_1973__10_2_29_0.pdf)

### 3.2 有限维 probe 是充分工具，不是全部定义

若找到有限维线性子空间 \(P\subset E\)，使

\[
\forall v\in E,\qquad
\mathcal L_P\{p\in P:v+p\in B\}=0,
\tag{FP}
\]

则 \(B\) 是 shy；取 \(P\) 中球上的归一化 Lebesgue 测度即可。**不能把“只在一个参数族里随机抽取，几乎总是好”误当成 (FP)：(FP) 要求每个背景 \(v\)。** 也不能把 finite-dimensional probe 当作 prevalence 的必要条件；一般的见证测度可以具有无限维支撑。

### 3.3 为什么不能直接放在“全部 RLEB 算子”上

闭图多值映射的集合没有天然的加法逆元；Minkowski 和改变值数，且一般不形成所需群。单调映射、具有误差界的映射或具有指定零集的映射也不是任意平移封闭的线性空间。

可以先在连续单值映射空间 \(C(K,\mathbb R^d)\) 或某个 Hölder／光滑函数空间中研究 \(T\)，再用

\[
F_T(u)=\{x-u:T(x)=u\}
\]

编码完整 \(J_{F_T}=T\)。但这只自动给出完整 resolvent 关系以及连续图的闭性；至多二值需要 \(T\) 的每个逆纤维至多有两个点，RLEB 与真实 min-residual EB 仍须另证。把随机 \(T\) 编码成 \(F_T\) 不能跳过这些约束。

如果固定解集 \(S\)，较合理的环境是仿射空间

\[
T_0+E_0,\qquad E_0=\{h\in C(K,\mathbb R^d):h|_S=0\},
\]

而不是整个函数空间。即便如此，保持 \(T(K)\subset K\)、有限逆纤维、严格 RLEB 与共同轨道预算，仍是额外非线性约束。

**重要的条件化陷阱：**若 \(\mathscr C\) 本身是某个较大空间 \(E\) 的 shy 子集，则 \(\mathscr B\subset\mathscr C\) 和 \(\mathscr C\setminus\mathscr B\) 都可能在 \(E\) 中 shy。这不会告诉我们“在 RLEB 内哪类更多”。必须研究相对空间／明确参数图册，而非拿外部零测结论冒充内部比较。将 \(E\setminus\mathscr C\) 全部记为“好”，也可能使所谓 prevalence 完全来自不满足 RLEB 的对象。

### 3.4 所有原性质在随机扰动下都需要逐项保护

| 性质 | 一般随机扰动是否自动保留 | 精确障碍／修复 |
|---|---|---|
| 闭图 | 某些表示下可以 | 对同一个闭图 \(F\) 加连续单值扰动 \(h(x)\)，图变换 \((x,y)\mapsto(x,y+h(x))\) 是同胚，闭图保留；这不保证其他性质。 |
| 至多二值 | 加同一单值扰动可以 | 每个值集仅平移，值数不变；直接扰动 resolvent 则须重新核对逆纤维。 |
| 半代数 | 有限半代数参数化可以 | 一般 Gaussian 随机级数没有这种保证；不要随机连续抽取幂指数后仍默认半代数。 |
| 单调性 | 不可以 | \(F=0\) 加 \(\theta I\)，只有 \(\theta\ge0\) 时单调。单调锥没有加法逆元。 |
| 完整单值 resolvent | 不可以 | 图平移或系数扰动后，\(I+\lambda F\) 的满射性与逆唯一性必须重证。直接以 \(T\) 逆图编码可保护此项。 |
| 固定非唯一零集 | 不可以 | \(T(a,n)=(a,qn)\) 改为 \((a+\varepsilon,qn)\)，扰动任意小却没有固定点；在固定点集上消失的扰动只是起点。 |
| 严格 RLEB、真实 EB、共同尾界 | 不可以 | 必须有统一裕量并证明扰动稳定性；不能仅以“原条件严格”推定在所选范数中开。 |

另一个容易误导的随机模型是 \(F(x)=B^TBx\)，其中 \(B\) 是方形 Gaussian 矩阵：几乎必然可逆，所以零集几乎必然唯一，极限选择常值。这不回答当前“保留多解与 Hölder 奇异接缝”的问题。

## 4. Gaussian 概率不是无偏的无限维体积

在可分 Hilbert 空间取

\[
X=\sum_{j\ge1}\sqrt{\lambda_j}\,\xi_j e_j,
\qquad \xi_j\stackrel{\mathrm{iid}}\sim N(0,1),\quad
\lambda_j>0,\quad\sum_j\lambda_j<\infty,
\]

便得到真正的 Hilbert 值 Gaussian 随机元。协方差特征值、基以及所在函数空间的正则性都是模型选择；“所有方向方差相等”的 \(\lambda_j=1\) 不能给出该 Hilbert 空间内的随机元。

Gaussian 测度只沿其 Cameron–Martin 子空间准不变，而不是沿全部方向准不变。可访问的作者讲义精确给出这一结论及 Hilbert 谱表示：Hairer，*An Introduction to Stochastic PDEs*，Exercise 4.37、Theorem 4.44。[作者原文](https://www.hairer.org/notes/SPDEs.pdf)

所以：

- “一个特定 Gaussian 模型下概率为 1”不等于 prevalent。
- “对所有非退化 Gaussian 测度均为零”的 Gaussian-null 是更强且另需准确约定的概念，不等于“对我挑选的一个 Gaussian 测度为零”。
- 若随机扰动在某个 \(s\in S\) 的取值具有非退化连续分布，则保持 \(T(s)=s\) 的概率已经是零；应先把扰动支撑放在 \(h|_S=0\) 的空间，不能事后对零概率事件作朴素条件化。
- 对约束集合 \(\mathscr C\) 做 \(\mu(\cdot\mid\mathscr C)\)，首先必须证明可测且 \(\mu(\mathscr C)>0\)；若为零，就不能用这个表达式来宣称“随机 RLEB 算子”。

### 一个比“Gaussian 有偏”更强的警告

在无限维可分 Banach 空间里，对任意 Borel 概率 \(\mu\)，都存在 shy 集 \(A\) 使 \(\mu(A)=1\)。直接证明：概率紧性给出紧集 \(K_n\) 满足 \(\mu(K_n)>1-2^{-n}\)，而无限维空间的紧集 shy，shy 集对可数并封闭，因此

\[
A=\bigcup_nK_n\text{ 是 shy},\qquad\mu(A)=1.
\]

于是其 prevalent 补集却具有 \(\mu\)-概率零。这说明 prevalence 是“可用同一随机扰动击穿每个平移的例外集”的性质，绝不是对任意事先指定抽样规律都几乎必然。

上面的短证明只调用已核过的 HSY §2 Fact 3″、Fact 8。Stinchcombe 的 *The Gap between Probability and Prevalence: Loneliness in Vector Spaces*，Proc. AMS 129 (2001), 451–457，DOI 10.1090/S0002-9939-00-05543-X，正面讨论这个差距；本轮已核题名／出版记录，出版社全文未取得，不冒称逐定理读过该篇。[出版记录](https://www.jstor.org/stable/2668704)

## 5. Baire residual 与满测度互不蕴含

可以在 \([0,1]\) 内直接看见差别，无须无限维难例。枚举有理点 \(q_j\)，对每个 \(n\) 取包含全部 \(q_j\) 的相对开稠密集 \(U_n\)，总长度小于 \(2^{-n}\)。则

\[
G=\bigcap_{n\ge1}U_n
\]

是 residual，但 Lebesgue 测度为零；\([0,1]\setminus G\) 是 meagre，却测度为一。在具有正密度的 Gaussian／其他绝对连续分布下也一样。故“Baire 意义典型”不能译作“随机抽到的概率为一”。这也给出 residual 与 prevalence 在有限维已不一致的例子。

更不应预设任一坏类必然是 residual 或 meagre，或必然 prevalent 或 shy；集合完全可能两边都不是。Haar-null 测试测度本身的复杂性，见 Dodos *Dichotomies of the set of test measures of a Haar-null set*，Theorems A–C。[原始论文](https://arxiv.org/html/1006.2673v1)

## 6. 可立即执行的两个概率模型

这两族用来说明“相对大小”如何严谨落地，以及随机生成机制的重要性。它们不是对整个 RLEB 类的结论，也不将下面基础推导宣称为新的研究定理。

### 模型一：现有 cap 构造中的坏选择满参数测度

固定 \(0<\gamma,q<1\)、\(A>0\)，取

\[
0<B_0<A\sqrt{q^{-2\gamma}-1},\qquad B\in[0,B_0],
\]

并定义稿件现有族

\[
T_B(z,p,r)=
\left(z+A|r|^\gamma,
p+B\min\{p_+,|r|\}^\gamma,
q|r|\right).
\tag{M1}
\]

取共同尺度

\[
R^{1-\gamma}<
\frac{Aq^{-\gamma}-\sqrt{A^2+B_0^2}}{1+q}.
\tag{M1-R}
\]

由现有 (3.7) 的完整反演、真实最小残差和常数公式，整个参数区间同时满足严格 RLEB，共同零集为 \(S=\mathbb R^2\times\{0\}\)；有理 \(\gamma\) 时每个成员半代数且至多二值。这里参数 \(A,B,q\) 无须有理。

对每个固定 \(B>0\)，稿件的首次饱和分析给出无正阶两点 Hölder 模。对 \(B=0\)，直接求和得到

\[
\Pi_{T_0}(z,p,r)=
\left(z+\frac{A|r|^\gamma}{1-q^\gamma},p,0\right),
\]

它在有界区域上为 \(\gamma\)-Hölder。因此在这个参数区间中，坏参数集恰为

\[
(0,B_0],
\]

它相对开、稠密、满 Lebesgue 测度。若 \(B\) 的分布对 Lebesgue 绝对连续，坏选择概率就是 1；若分布在 \(0\) 有原子，概率为 \(1-\mathbb P(B=0)\)。

**含义：**坏现象不是此显式结构内只有一个精确系数点才会发生的偶然性；改变 cap 强度仍存在。

**不能推的结论：**(M1) 是一个刻意保留 cap 机制的一维族，可能是大函数空间中极薄的子集。它没有证明对一般结构扰动稳健，更没有证明在整个 RLEB 类中 residual／prevalent。\(B\downarrow0\) 时，坏模下界常数与可观察敏感尺度也可能退化，不能声称强度一致。

### 模型二：保留奇异法向和多解，但全部稳定的对照族

固定同样的 \(\gamma,q\)，令 \((A,C)\in[1,2]\times[-1,1]\) 随机，定义

\[
T_{A,C}(z,p,r)=
\left(z+A|r|^\gamma,p+C|r|^\gamma,q|r|\right).
\tag{M2}
\]

它的极限是

\[
\Pi_{A,C}(z,p,r)=
\left(z+\frac{A|r|^\gamma}{1-q^\gamma},
p+\frac{C|r|^\gamma}{1-q^\gamma},0\right),
\]

故全部在有界区域 \(\gamma\)-Hölder，且多解平面未坍缩，法向仍非 Lipschitz。令 \(a=y/q\ge0\)，定义

\[
F_{A,C}(\xi,\eta,y)=
\{(-Aa^\gamma,-Ca^\gamma,a-y),
(-Aa^\gamma,-Ca^\gamma,-a-y)\},
\]

在 \(y<0\) 为空。直接代入并由 \(r=\pm a\) 反演，得到全空间完整 \(J_F=T_{A,C}\)。它闭图、至多二值，零集仍是该平面，有理 \(\gamma\) 时半代数。

记 \(D=\sqrt{A^2+C^2}\ge1\)，则全值集的最小残差满足

\[
r_F(u)^2=D^2a^{2\gamma}+(1-q)^2a^2,
\quad d(u,S)=y\le q(r_F(u)/D)^{1/\gamma}.
\]

由 \(2T-I\) 的显式式子得到 all-pairs RL 常数

\[
L_R=2D+(1+2q)R^{1-\gamma}.
\]

对应兼容因子可以取

\[
\kappa_R=q\left(1+
\frac{(1+q)R^{1-\gamma}}D\right)^{1/\gamma}.
\]

选择 \(R^{1-\gamma}<(q^{-\gamma}-1)/(1+q)\)，即可对整个参数矩形统一保证

\[
\kappa_R\le\bar\kappa_R
:=q\left(1+(1+q)R^{1-\gamma}\right)^{1/\gamma}<1.
\]

**证书层的限定：**此处得到的是共同尺度与共同严格兼容上界 \(\bar\kappa_R\)，但使用的 RL／EB 配对

\[
L_R(D)=2D+(1+2q)R^{1-\gamma},\qquad
\psi_D(t)=q(t/D)^{1/\gamma}
\]

随 \(D=\sqrt{A^2+C^2}\) 变化。因此本矩形族尚不能据此称为“同一个固定 \((L,\psi)\) 证书层”；它与第 4／5 组另行核验的共同固定证书结论不同。不能分别取最大的 \(L\) 与最弱的 \(\psi\)，却仍不经重算地沿用上述依赖配对的兼容因子。下面的参数概率结论只需要各成员满足严格 RLEB 及上述共同裕量，不依赖这个更强的固定证书声明。

所以此模型不是通过“改成唯一解”得到稳定；它保留完整算子、真实残差、严格 RLEB、多解及奇异法向，但去掉切向 cap 放大。

在此参数族上任意概率分布都给稳定选择概率 1。与模型一的对照说明：**选定哪种结构做随机化，本身决定问题，不能在结果出来后换抽样模型来证明想要的结论。**

## 7. 如果继续做到真正的无限维泛性，最低工作清单

1. 先固定不坍缩的解流形／解集和一个容纳法向奇异的环境函数空间；明确用 resolvent 坐标还是算子图坐标。两个坐标未必保存所选测度／prevalence。
2. 证明统一证书子类在选定拓扑中的完整性／Baire 性，或给出明确参数图；不能因其是较大 Banach 空间的子集，就直接认为它也是 Baire 空间。
3. 建立保持完整 resolvent、值数与真实残差的扰动引理。有限维 cap 族中的全参数结论不代替这个引理。
4. 证明坏性质可测。一个方便方案是固定紧初值域、共同单步模和统一尾界，使 \(T\mapsto\Pi_T\) 在对应一致拓扑中连续。随后“某个 \(1/n\) 阶、常数 \(m\) 的 Hölder 条件”可通过可数稠密点对表达成闭条件，其可数并给出“存在正阶 Hölder”的 Borel 事件。若没有这些统一条件，必须另做可测性证明。
5. 若做 finite-dimensional probes，写出并证明“对**每个**允许背景”的量词；若只做随机系数，诚实报告“该生成模型下”的概率，不升级为 prevalence。
6. 最好先证明一个非平凡的相对开坏区或相对开好区。若两者都存在于同一 Baire 结构空间，则两类都不是 meagre；若对同一全支撑概率两者均有非空开区，则两者均有正概率。此时目标应是相图／阈值，而不是勉强求“几乎全好或全坏”。

## 8. 最终建议

**值得做，但题目应先落成：在保留非唯一解集及统一严格 RLEB 证书的某个自然结构空间中，稳定／坏解选择对允许扰动是开、稠密还是稀薄？**

第一篇可行增量是“同一结构模型的参数相图＋坏性质的相对稳健性”，随后再考虑 Baire 纲分类。无限维 prevalence 可以成为后续加强，不宜作为第一步的默认语言。

当前可确认：存在一个保持原完整几何约束的有限参数族，其坏选择满测度；也存在另一保持这些约束的非平凡族，其稳定选择满测度。**目前不能判定全 RLEB 类中的坏算子大或小。**

## 9. 核验过的主要文献与读取边界

- B. R. Hunt, T. Sauer, J. A. Yorke, *Prevalence: a translation-invariant “almost every” on infinite-dimensional spaces*, Bull. Amer. Math. Soc. 27 (1992), 217–238；arXiv:math/9210220。核读引言、§2 定义及 Facts 3″、8。原始论文链接：https://arxiv.org/pdf/math/9210220 。
- J. P. R. Christensen, *On sets of Haar measure zero in abelian Polish groups*, Israel J. Math. 13 (1972), 255–260；DOI **10.1007/BF02762799**。出版社题名／摘要／出版记录核到，原全文未取得。定义及群结构由其本人 1973 论文核读，不将后者伪称为 1972 正文。
- J. P. R. Christensen, *Measure Theoretic Zero Sets in Infinite Dimensional Spaces and Applications to Differentiability of Lip-Schitz Mappings*, Publications du Département de Mathématiques de Lyon 10(2) (1973), 29–39。核读 pp.29–31；https://www.numdam.org/item/PDML_1973__10_2_29_0.pdf 。
- M. B. Stinchcombe, *The Gap between Probability and Prevalence: Loneliness in Vector Spaces*, Proc. Amer. Math. Soc. 129(2) (2001), 451–457；DOI 10.1090/S0002-9939-00-05543-X。核到出版记录；全文访问失败，所以正文中的概率／prevalence 反差另给了完整短证明。
- P. Dodos, *Dichotomies of the set of test measures of a Haar-null set*；arXiv:1006.2673。核读定义和 Theorems A–C；https://arxiv.org/html/1006.2673v1 。
- M. Hairer, *An Introduction to Stochastic PDEs*，作者讲义；核读 Gaussian 空间定义、Exercise 4.37、Theorem 4.44 的适用范围。https://www.hairer.org/notes/SPDEs.pdf 。这不是对 Cameron–Martin 1944 原文逐页核查的声明。

没有发现或主张“RLEB 坏选择类已经有现成测度分类”的文献。本报告只评估工具适用性并给出受限参数模型，不把检索未命中当作原创性证明。
