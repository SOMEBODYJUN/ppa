# 算子空间比较：优先权与研究价值独立审计

审计日期：2026-09-20。审计范围：`comparison_space_team/01–05`（包括 04 新增 §11 的任意步长加强）与 `genericity_team/07_value_priorart.md`。本报告只评价新提出的空间／纲比较；不重新审判已建立的原 RLEB 论文。

## 1. 直白结论

**这条路线值得做，但不是“从零建立算子空间与纲分类”。** 非扩张映射、完整 resolvent、极大单调算子、proximal 映射，以及固定一个非单点解集后研究泛型极限 retraction，都已有直接先例。不能把这些语言及 Baire 方法本身列为新贡献。

另一方面，已读先例**没有直接推出**当前的精确组合：

> 固定真实非点仿射零集 $S$，在一个无限维、闭凸、具有完整 resolvent、真实最小残差 EB 和共同严格 RLEB 证书的法向超吸引层内，能在指定解点得到 Luke–Tam 2025 局部 all-pairs 图块证书的算子，即使允许任意正步长，也只构成第一纲集合；另有恰二值算子的完整 Hölder 函数球实现。

当前新增部分主要是**受约束的实现与精确覆盖分离**，不是新的 Baire 原理。任意步长版本比固定步长版本明显更有意义：它排除了“换一个 proximal 参数就重新落回 LT”这一具体反驳。

原创性风险分级：

| 被主张的内容 | 风险 | 当前审稿判断 |
|---|---|---|
| “首次用算子空间／纲比较收敛理论” | HIGH | 明确有早期先例，不应主张 |
| “固定多解集及其极限 retraction 的泛型理论” | HIGH | Butnariu–Reich–Zaslavski 2001 已有直接定理 |
| “固定 Hölder 模层内 Lipschitz 类很小”的一般机制 | HIGH | 现象已有，当前凸混合引理本身很初等 |
| 上述完整 RLEB／LT 受约束组合，尤其任意步长排除与二值实现 | MEDIUM | 有可辨识的新结果候选；不是已读文献的直接推论，但尚无完整优先权清关 |
| “因此整个 RLEB 比整个 Luke–Tam 体系大很多／更好” | HIGH | 当前结论不足以支持这种全局比较 |

期刊级判断：**适合作为原 RLEB 或 solution-selection 论文的实质性增强章节；也有发展成专业短论文的可能。仅以当前空间层和标准 Baire 证明独立支撑高水平综合优化／泛函分析论文，证据不足。** 这是研究价值判断，不是录用概率或期刊分区承诺。

## 2. 原始文献核查：什么已覆盖，什么没有

下列“已读”指实际打开原论文正文并核对相应位置，不以搜索摘要代替定理。

### 2.1 固定非点解集的空间早已有之

Dan Butnariu, Simeon Reich, Alexander J. Zaslavski, *Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces*, Journal of Applied Analysis 7(2) (2001), 151–174，DOI **10.1515/JAA.2001.151**。已读作者站原稿主要定理及证明；[作者原稿](https://math.haifa.ac.il/dbutnaru/publications/but-rei-zas-jaa.ps)。

该文固定非空闭凸集 $F\subset K$，用 Bregman 距离 $D_f$ 定义满足

\[
D_f(z,Tx)\le D_f(z,x)\qquad(z\in F, x\in K)
\]

的映射空间及其连续、在有界集上一致连续的子空间，采用有界集上一致收敛拓扑；不要求 $F$ 是单点。Theorem 2.1 在其 A(i)–A(iv)、$P\in M_u$ 及条件 (2.1) 下给出残集：迭代在有界集上一致收敛到 $F$ 上的 retraction，并对附近算子给出一致的最终误差控制。A(i)–A(iv) 包括 Bregman 小距离控制范数、到固定点的 Bregman 距离有界当且仅当输入有界、$D_f(z,\cdot)$ 凸且下半连续，以及 Bregman 投影存在；(2.1) 是有界输入上范数小距离反向控制 Bregman 距离。Theorems 3.1–3.2改用 $D_f$ 在有界 $F\times K$ 上一致连续等条件，给出相应收敛与稳定性；Lemma 4.1已明确使用与投影的凸混合保留共同 $F$。

**对应：**固定多解集、完备映射空间、Baire、凸混合、极限 retraction、定性稳定性，这整组思路不是新东西。**未覆盖：**当前反射映射 Hölder 条件、最小残差 EB、RLEB 严格预算、二值完整图、LT all-pairs 的相对第一纲分离。

还有一个必须说明的假设差异，以下是本审计的直接推导，不是该文的新定理：当 $f=\|\cdot\|^2$、$F=S$ 为完整仿射子空间时，上述相对非扩张性强迫

\[
P_STx=P_Sx.
\]

理由是把 $z\in S$ 沿任意切向方向移到任意远处，平方距离不等式中关于 $z$ 的线性项必须消失。因此当前 $T(z,r)=(z+c|r|^\gamma,g(r))$ 的非零切向漂移不在这个欧氏相对非扩张子类中。这说明“2001 年已有固定 $S$”**不能**被误用成“2001 年已经覆盖本构造”。本审计未证明不存在其他适配的 Bregman 几何，不能再扩大排除范围。

### 2.2 Reich–Zaslavski 1999：重要先例，但全文核查尚有缺口

Simeon Reich, Alexander J. Zaslavski, *Convergence of Generic Infinite Products of Nonexpansive and Uniformly Continuous Operators*, Nonlinear Analysis: Theory, Methods & Applications 36 (1999), 1049–1065，DOI **10.1016/S0362-546X(98)00080-7**；[出版社原始页面](https://www.sciencedirect.com/science/article/abs/pii/S0362546X98000807)。

出版社摘要涉及有界闭凸 Banach 域上的泛型算子序列、随机无限乘积、弱遍历性、共同不动点与 retraction 收敛。**本轮未取得可读完整原稿，故不提供伪造的定理号，不把摘要扩张为精确假设对应。** 这项缺口须保留在优先权清单。它并不影响上一项 BRZ2001 的已读直接证据。

还须避免文献混名：作者站一个标作 1999 年 *Generic power convergence of operators in Banach spaces* 的链接实际返回后来含 “NONLINEAR” 的综述稿，不能将后者定理号冒充 1999 原刊定理号。

### 2.3 固定连续模空间：Strobin／Ravasini 已覆盖一般“粗糙映射典型”现象

Davide Ravasini, *Generic Uniformly Continuous Mappings on Unbounded Hyperbolic Spaces*, Journal of Mathematical Analysis and Applications 538(1) (2024), 128440，DOI **10.1016/j.jmaa.2024.128440**，arXiv **2308.15277**。已读 [v2 原文](https://arxiv.org/html/2308.15277v2)。

Theorem 3.3：$X$ 完备、无界、hyperbolic，$\omega$ 非零、非减、凹，$\omega(0)=0$；在所有 $\omega_f\le\omega$ 的自映射组成的空间中，取有界集上一致收敛拓扑，典型映射满足 $\omega_f=\omega$。取 $\omega(t)=Mt^\gamma,\ 0<\gamma<1$，即排除全局 Lipschitz。Theorems 4.1、5.2分别讨论有界映像／另一拓扑及逐点拓扑；不可混用。

该结论**不直接推出**本文定理：

1. 全局模达到上界，可以由逃向无穷远的点对实现；它不保证某个指定解点附近不 Lipschitz 或不 calm。
2. 没有固定非点 $S$、法向收缩、真实 EB、纤维数限制。ambient 残集与闭子空间相交不一定在子空间内残留。
3. 本文反射映射只在尺度 $\|x-y\|\le R$ 上受纯幂模约束。纯全局 $Mt^\gamma$ 模与固定一个无界非点仿射 $S$ 本就不相容：对 $x,y\in S$，要求 $\|x-y\|\le M\|x-y\|^\gamma$ 会在大尺度失败。

因此，**不能说 Ravasini 的原定理已经自动包含本文；也不能把其已知的一般粗糙性机制包装成新的大原理。**

更早相关文献是 Filip Strobin, *Some Porous and Meager Sets of Continuous Mappings*, Journal of Nonlinear and Convex Analysis 13(2) (2012), 351–361。Ravasini 原文明确归功于该文的 Hilbert 无界闭凸域版本。本轮只有作者发表信息与其后作者原文的引用，**未读到 Strobin 全文、未核实定理号，也没有已核实 DOI/arXiv**。正式稿应补这篇，而不是把首次出现年份写成 2024。

### 2.4 单调算子／resolvent 的范畴空间并非空白

Xianfu Wang, *Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent*, Nonlinear Analysis 87 (2013), 69–82，DOI **10.1016/j.na.2013.03.008**，arXiv **1301.6443**；已读 [原文](https://arxiv.org/pdf/1301.6443)。

Propositions 1.3、2.1、2.3、2.4建立非扩张映射、极大单调图、完整 resolvent 的对应与完备拓扑；有限维时相应图收敛一致。Lemma 2.8给强单调类稠密，Corollary 3.10给其第一纲；Theorem 2.16／Corollary 2.17给典型唯一零点／super-regularity。

**对应：**“先找规范算子空间，再研究好条件的类有多大”已有直接示范。**未覆盖：**固定非点 $S$ 的当前层；强压缩逼近会破坏多解集，不能把其唯一零点残集移植到固定多解集层。

本审计从其 Corollary 3.10直接得到一个相关但不值得冒充新理论的推论。固定 $\rho>0$，令

\[
\mathcal H_\rho=\{A:A+\rho I\text{ 是极大单调}\},
\]

并从 $B=A+\rho I$ 拉回 Wang 的拓扑。那么

\[
A\text{ 单调}\iff B\text{ 为 }\rho\text{-强单调}.
\]

右侧是闭集，且包含于第一纲的全部强单调类，故闭且无处稠密。也就是说，**“单调类在固定 hypomonotone 层内很小”至少已是已发表定理的短推论**，无需从零开发。此处不声称找到了以此为题单独发表的原定理。

但这不完成 RLEB/LT 比较：取 $\lambda=(1+\rho)^{-1}$，

\[
J_{A+\rho I}(x)=J_{\lambda A}(\lambda x),
\]

所以该层的完整 $J_{\lambda A}$ 仍都是 Lipschitz；它没有承载本文要比较的非 Lipschitz resolvent。

### 2.5 proximal 类的相对纲分离确有先例，但域不能扩大

Heinz H. Bauschke, Jason Schaad, Xianfu Wang, *On Douglas–Rachford Operators That Fail to Be Proximal Mappings*, Mathematical Programming 168 (2018), 55–61，DOI **10.1007/s10107-016-1076-5**，arXiv **1602.05626**；已读 [作者原稿](https://cmps-people.ok.ubc.ca/bauschke/Research/104.pdf)。

Theorem 3.1在 $\mathbb R^n,\ n\ge2$ 的对称极大单调线性关系对的空间内，证明 DR 映射仍为 proximal 的子类闭且无处稠密。关键是反射 resolvent 的交换性障碍。Remark 3.3明确把扩展至一般次微分算子的情形留作问题。

**对应：**一种算法算子落入更窄 proximal 类“很少”，已有真正相对空间定理；还有凸组合式的逼近证明。**未覆盖：**非线性的 RLEB/LT 层或所有 proximal 算子的全空间分类。

Chayne Planiden, Xianfu Wang, *Strongly Convex Functions, Moreau Envelopes and the Generic Nature of Convex Functions with Strong Minimizers*, SIAM Journal on Optimization 26(2) (2016), 1341–1364，DOI **10.1137/15M1035550**，arXiv **1507.07144**；已读 [原文](https://arxiv.org/pdf/1507.07144)。Theorems 4.11–4.12给出 Moreau-envelope／epi 拓扑下强凸函数稠密且第一纲；Theorem 4.16给强极小值的泛型性。这又表明“较强可用假设稠密却第一纲”并不是反常或自动代表较弱理论更优的事实。

### 2.6 Ravasini–Thimm 2025 的空间分类不能省略拓扑

Davide Ravasini, Daylen K. Thimm, *Generic Nonexpansive Hilbert Space Mappings*, Studia Mathematica 283 (2025), 281–301，DOI **10.4064/sm240722-12-3**，arXiv **2407.03881**。已读 [v2 原文](https://arxiv.org/pdf/2407.03881) 的空间定义及对应定理。

其母空间是可分无限维 Hilbert 空间闭凸集上的非扩张自映射，采用**逐点收敛拓扑**。Theorem 3.4在 somewhat bounded 域给出稠密开集上的不动点存在；Theorem 4.1在 totally unbounded 域给出典型无不动点；Theorem 4.2总结相应 0–1 分类。这不是本文固定非点解集／Hölder 反射／RLEB 层的先例定理，但直接表明：选拓扑和选域，足以实质改变“典型”的结论。不能把另一空间里的泛型结论无说明地拿来排名理论。

## 3. 新组合到底多出了什么

先固定 $1\le\dim S<d$、$\lambda>0$、$0<\gamma<1$、$\nu=1/\gamma$、$0<q<1$。本组报告研究的完整空间层由以下性质定义，不只是某个一参数例子：

\[
T|_S=I,
\quad\|(2T-I)x-(2T-I)y\|\le A\|x-y\|^\gamma
\quad(\|x-y\|\le R),
\]

\[
d(Tx,S)\le q\min\{d(x,S)^\nu,d(x,S)\}.
\tag{Y}
\]

在具有尖锐 Hölder 见证的非空预算区间内，完整层 $\mathcal Y$ 是闭凸、无限维且在 compact-open 拓扑中为 Baire；其所有成员具有同一真零集。

### 3.1 完整 resolvent 的存在是自动编码，不应单独拔高

对连续单值 $T$，定义

\[
F_T(u)=\{(x-u)/\lambda:Tx=u\}.
\]

则完整 $J_{\lambda F_T}=T$，且图是连续图的可逆线性坐标变换。它正确解决“只验证了选中分支”的漏洞，但数学上是标准反构，不是新的存在定理。真正需要复核的是：约束能否同时保留、最小残差是否是全部逆像的 infimum、二值性是否完整而非任意删支。

### 3.2 真实 EB 与严格预算是有内容的联合接口，但证明不深

对每个逆像 $Tx=u$，由 (Y) 得

\[
\|x-Tx\|\ge(1-q)d(x,S),
\qquad
d(u,S)\le\frac{q}{(1-q)^\nu}\|x-u\|^\nu.
\]

对完整纤维取 infimum，才得到

\[
d(u,S)\le\frac{q}{(1-q)^\nu}
\bigl(\lambda\operatorname{dist}(0,F_T(u))\bigr)^\nu.
\]

与反射 Hölder 模合并后，共同严格预算是

\[
\kappa=
\frac{q}{(1-q)^\nu}
\left(\frac{R^{1-\gamma}+A}{2}\right)^\nu<1.
\]

这些不等式把抽象函数空间的粗糙性真正接到了 RLEB 证书上，优于随便展示非 Lipschitz 函数；但基本步骤是两次距离估计与取下确界，不应宣传成难度很高的新泛函分析工具。

### 3.3 当前第一纲证明的本体是标准移植

固定 $s\in S$，闭层取局部 Lipschitz 常数和半径的可数编码。若 $T$ 属于某一闭层，而 $T_*$ 在 $s$ 有非零 $t^\gamma$ 切向位移，则

\[
T_\theta=(1-\theta)T+\theta T_*
\]

仍在 $\mathcal Y$、趋于 $T$，且 $O(t)$ 不能抵消非零 $t^\gamma$。闭层遂无内点。**只要闭凸层与见证已造好，Baire 结论几乎是形式上的。** 不应说整个方向已知；也不应把这个引理本身称为突破。

真正新增工作集中在：这个层不是空的；确含非退化 maximal-monotone/LT 成员；完整 EB 与预算统一；恰二值子层另有独立的完整函数球实现；不同拓扑与局部／全局量词清楚。

### 3.4 任意步长加强是真正值得保留的比较内容

已核对 04 §11。若同一个 $F_T$ 在某个 $\mu>0$ 下满足 LT2025 局部 all-pairs 图块条件，置

\[
c=\mu/\lambda,\quad u=Tx,\quad a=c(x-u),\quad
z=u+a,\quad p=P_Sz.
\]

当 $x\to s$ 时，$(u,a)$ 与 $(p,0)$ 均进入实际局部图块。submonotonicity 给

\[
\|u-p\|^2+\|a\|^2\le(1+2\tau)\|z-p\|^2,
\]

从而

\[
\|Tx-x\|\le
\sqrt{1+2\tau}\frac{c+|1-c|q}{c}\,d(x,S)
\quad(x\text{ 在 }s\text{ 附近}).
\tag{N}
\]

因此所有“存在某个正步长可以得到 LT 图块”的成员，一次性落入线性位移的同一可数闭层并；不存在不可数第一纲集合取并的漏洞。证明还不需要假设另一个步长的完整 resolvent 全域单值。

这一必要条件明确使用**移动的零点** $p=P_Sz$，不能偷换成只锚定一个解点的 pointwise 条件。04 §11.4 对固定原步长、完整输入邻域上的 pointwise-AA 另行使用 calmness 闭层，逻辑是不同的。两个版本都不能无条件排除任意低维比较集上的所有 Luke–Thao–Tam 理论。

目前已读原文没有给出 (N) 加当前受约束残集的这个组合。它比只说“RLEB 允许 Hölder 而 LT 要 Lipschitz”更精确，宜作为比较节的核心。

## 4. “RLEB 多很多”到底证明到了哪一步

当前能够严谨表达的是

\[
\mathcal Y\subset\mathsf{RLEB},
\qquad
\{T\in\mathcal Y:\exists\mu>0\text{ 可获指定 }s\text{ 的 LT2025 图块证书}\}
\text{ 在 }\mathcal Y\text{ 中第一纲}.
\]

它说明：**新覆盖不是孤立例子；在一个确定、无限维、包含旧理论成员的结构层里，新覆盖在拓扑上占优。** 这是比“找一个反例”更强的结论。

它没有证明以下结论：

- 在“全部 RLEB”上有一个已建立的完备自然母空间，使全部 LT 为第一纲。
- RLEB 新增者具有某个概率、百分比、prevalence 或 Lebesgue 体积。
- 工程／优化中典型数据生成出的算子大多位于该层。
- 较小的理论没有独立价值，或算法收敛速度／数值稳定性因类更大而更好。
- 所有解点、所有步长、所有局部选择和所有受限比较集上的 Luke–Thao–Tam 理论均失效。

还要把包含关系和相对分离分开证明。01 已指出，若只取 RLEB 的 direct 分支，就不能把所有 LT 线性证书包含进来；全局包含需保留 energy 分支与 LT 完整假设的实际接口。因此不能用一句“LT 是 RLEB 的端点”略去证书差异。

## 5. 空间自然性：优点与人为选择

### 5.1 有根据的优点

固定 $S$ 能防止“泛型唯一解”把多解选择问题消掉；固定模与预算使完备性、统一尾界和比较有明确含义；采用完整图／resolvent 而非选中分支也有算法意义。层中还容许非三角依赖，并非只有手写的一串参数。

这些理由使 $\mathcal Y$ 成为**可辩护的局部研究层**，不是完全任意的拓扑游戏。

### 5.2 不能掩饰的偏置

但 (Y) 强制法向超线性吸引 $d(Tx,S)=O(d(x,S)^\nu),\ \nu>1$。普通线性法向 LT 映射 $T(z,r)=(z,ar),\ 0<a<1$ 不在其中，因为 $a|r|\le q|r|^\nu$ 在 $r\to0$ 时不可能成立。原来几何法向的某些 RLEB 反例也被排除。

因此该层已经预选了一个有利于“法向很强、切向可粗糙”的区域。它含非退化 LT 成员，可排除“比较类为空”的最坏问题；但**含有旧类样本不等于这个层已被证明代表两套完整理论**。

更重要的是，(Y) 本身已很强。令 $d_k=d(x_k,S)\le R$，则

\[
d_{k+1}\le qd_k,
\qquad
\|x_{k+1}-x_k\|\le\frac{3d_k+A d_k^\gamma}{2}.
\]

右侧可求和，故点收敛可不经严格 RLEB 预算而直接推出。这是本审计的直接估计。它不损害 RLEB 证书真实有效，但表明**这节不是在证明另一种“只有 RLEB 才能看见”的基本收敛机制**；它证明的是原 RLEB 已有条件在规范层中比特定 LT 证书覆盖得多。

Baire 理论是一种相对拓扑大小，而非理论优劣排行榜。强单调／强凸在其经典大空间里已可能稠密且第一纲，并未因此变成差理论。此处应保持同样标准。

## 6. 怎样编排才有可发表的实际价值

建议题旨放在“共同非点零集下的受约束 resolvent 空间及收敛证书覆盖分离”，不放在“新建算子空间分类学”或“证明 RLEB 优于现有理论”。

保留的最小有内容定理包应为：

1. 自然层的完整构造、完备性、共同解集、共同最小残差 EB 和严格预算，给出非退化 LT 交集。
2. 所有正步长的局部 LT 图块统一落入 (N)，再证明该必要条件类第一纲。这是最干净的量词加强。
3. 恰二值完整函数球的独立实现；不得用 ambient 残集直接限制到有限纤维子空间。
4. 清楚交代 compact-open、强 Hölder、little-Hölder 层各自结论；拓扑改变不能省略。
5. 固定非点解集先例、已知固定连续模泛型定理及其不适用原因，提前向读者说明。

若目标是独立、分量更重的论文，最有价值的下一步不是继续加一种尖点公式，而是证明一个更少预选法向动力学的 **RLEB 证书空间**也有此分离；或者给出实际算法／问题族到该空间的开放、范畴保持坐标联系。强拓扑／porosity 的定量增强也可研究，但不自动解决代表性问题。

当前定稿建议：把它作为原研究的“非偶然扩展性”证据，适度主张。普通专业期刊短文是可讨论目标；高等级独立论文需比现有凸层移植更重的结构定理、适用族或概念后果。不要根据既有相近文章刊于某刊，推断本稿也已达到同一门槛。

## 7. 仍未解决与可追溯状态

| 项目 | 状态 | 不能据此声称什么 |
|---|---|---|
| BRZ2001 固定非点 $F$ 的原文定理及稳定性 | 已读并核对 Theorems 2.1、3.1–3.2，Lemma 4.1 | 不能再称固定多解集 Baire 框架首次出现 |
| Ravasini2024 固定模结论 | 已读 Theorems 3.3、4.1、5.2 | 既不能直接吞并本文，也不能忽视其方法先例 |
| Wang2013 算子／resolvent 完备空间与强单调第一纲 | 已读 | hypomonotone 平移推论不应冒充新大定理 |
| Bauschke–Schaad–Wang2018 DR／proximal 相对分类 | 已读 Theorem 3.1、Remark 3.3 | 不能扩张为所有非线性 proximal 类已有完整分类 |
| Planiden–Wang2016 Moreau／强凸第一纲 | 已读对应定理 | 类小不等于理论差 |
| Reich–Zaslavski1999 全文与精确定理号 | 未闭合：有正式书目信息和原始摘要，未获完整正文 | 不提供臆造定理号；不以检索不到证明没有覆盖 |
| Strobin2012 全文与精确定理号 | 未闭合 | 不把 Ravasini 的转述标成独立阅读 |
| 精确“RLEB + 全部纤维 EB + 二值 + 固定 $S$ + 任意步长 LT 第一纲”组合的完整优先权 | 未清关 | 只能称当前未见同一结论，不能称已证明首创 |
| 全部 RLEB 的规范 Baire 母空间及全局相对大小 | 未建立 | 层内结论不能自动提升 |

**最终裁定：组合层面的原创性风险 MEDIUM；若以全新空间分类框架或全面理论优越性宣传，风险 HIGH。数学上是可信且有用的研究增强，价值来自准确保留联合约束与跨步长量词，不来自 Baire 技巧本身。**
