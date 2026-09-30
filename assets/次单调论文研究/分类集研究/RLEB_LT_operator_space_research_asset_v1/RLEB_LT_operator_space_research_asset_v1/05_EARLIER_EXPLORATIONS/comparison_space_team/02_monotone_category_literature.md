# 算子空间与纲分类：定理级文献审计

日期：2026-09-20。范围：只审计“在自然算子／映射空间内比较子类大小”这条路线，以及它对 RLEB 与 Luke–Tam 比较的可迁移性。不重新审查原 RLEB 论文，不替代团队对两套条件的精确翻译。

## 一、结论先行

1. **这条研究语言有成熟先例，不必从零发明。** 已有完整的极大单调算子空间、resolvent 空间、非扩张映射空间和凸函数空间，以及强单调、严格压缩、强凸、proximal 等子类的第一纲、无处稠密或多孔性定理。下面均区分母空间和拓扑。
2. **最接近用户想法的既有类比较，不只是“泛型唯一解”。** Bauschke–Schaad–Wang 的 Theorem 3.1 在完备算子对空间中证明：产生 proximal Douglas–Rachford 算子的算子对构成闭且无处稠密集。另由 Wang 的定理，可严格推出：固定 hypomonotonicity 预算的自然完备空间中，monotone 子类闭且无处稠密。
3. **尚未识别到已完成本项目“精确 RLEB 条件 vs 精确 Luke–Tam 条件”纲比较的原始论文。** 这不是已经证明没有先例，更不是首创证明。RLEB 的新命名不能排除已有定理在等价坐标下覆盖它；仍须完成条件翻译、共同母空间构建和相对纲定理。
4. **不能把“大”直接等同于“好理论、新理论”。** 第一纲的充分条件仍可能产生稳定、可计算的高质量证书；更大的覆盖范围只有同时保持有效收敛结论、自然空间与非人为限制，才构成有内容的增益。

## 二、已阅读原文并定位的定理

### 2.1 极大单调、firmly nonexpansive 与非扩张空间：Wang

**Xianfu Wang**, *Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent*, Nonlinear Analysis 87 (2013), 69–82。DOI：[10.1016/j.na.2013.03.008](https://doi.org/10.1016/j.na.2013.03.008)；[原文 arXiv:1301.6443](https://arxiv.org/pdf/1301.6443)。

取非零实 Hilbert 空间 $H$，记 $\mathcal N,\mathcal J,\mathcal M$ 分别为非扩张映射、firmly nonexpansive 映射、极大单调算子全体。令 $J_A=(I+A)^{-1}$、$R_A=2J_A-I$，并记

$$
d_{\rm bu}(T,U)=\sum_{m=1}^{\infty}2^{-m}
\frac{\sup_{\|x\|\le m}\|Tx-Ux\|}{1+\sup_{\|x\|\le m}\|Tx-Ux\|}.
$$

在 $\mathcal M$ 上用 $d_{\mathcal M}(A,B)=d_{\rm bu}(R_A,R_B)$。Propositions 2.1、2.3、2.4 给出相应完备性和等距对应；Lemma 2.8 给出强单调算子的稠密性；**Corollary 3.10：强单调算子在 $\mathcal M$ 中第一纲**。Corollaries 3.9、3.11 给出严格压缩、强 firmly nonexpansive 子类的相应结论。Theorem 2.16 与 Corollary 2.17 给出泛型唯一零点及 super-regular resolvent。

适用判断：这是共同算子空间内“更强充分条件稠密但第一纲”的直接先例。Theorem 2.13 的一般模板要求**严格压缩在研究空间内稠密**；固定两个以上解点时，此前提不成立。注意 $d_{\rm bu}$ 是有界集上一致拓扑，不能在无限维将它改称逐点拓扑。

### 2.2 真正的 proximal／非 proximal 类分离：Bauschke–Schaad–Wang

**Heinz H. Bauschke, Jason Schaad, Xianfu Wang**, *On Douglas–Rachford operators that fail to be proximal mappings*, Mathematical Programming 168 (2018), 55–61。DOI：[10.1007/s10107-016-1076-5](https://doi.org/10.1007/s10107-016-1076-5)；[作者原文](https://cmps-people.ok.ubc.ca/bauschke/Research/104.pdf)；[arXiv:1602.05626](https://arxiv.org/abs/1602.05626)。下述编号采用作者 PDF。

取 $H=\mathbb R^n,n\ge2$。$\mathcal L$ 为极大单调线性关系，$\mathcal S$ 为闭凸函数次微分。母空间

$$
\mathcal X=(\mathcal L\cap\mathcal S)^2,\qquad
d((A,B),(A',B'))=\|J_A-J_{A'}\|_{\rm op}+\|J_B-J_{B'}\|_{\rm op}
$$

完备。Proposition 2.8 将此拓扑与图收敛／resolvent 收敛对应。设

$$
T_{A,B}=\tfrac12(I+R_BR_A),\qquad
\mathcal D=\{(A,B)\in\mathcal X:T_{A,B}\text{ 是 proximal 映射}\}.
$$

**Theorem 3.1：$\mathcal D$ 闭且无处稠密。** 核心判别是线性 firmly nonexpansive 映射为 proximal 当且仅当对称（Corollary 2.6）；在这里等价于 $R_AR_B=R_BR_A$。

适用判断：它展示了用户要求的“先构造合理空间，再证明特殊结构占小类”。但母空间是**对称线性关系的算子对**，不是全部非线性 firmly nonexpansive 映射，更不是 RLEB 空间。论文 Remark 3.3 本身将向一般次微分算子推广列作问题；$n=1$ 时所有 DR 映射均 proximal，见 Remark 3.2。

### 2.3 强凸类的纲，以及弱凸空间的现成入口：Planiden–Wang

**Chayne Planiden, Xianfu Wang**, *Strongly convex functions, Moreau envelopes and the generic nature of convex functions with strong minimizers*, SIAM Journal on Optimization 26(2) (2016), 1341–1364。DOI：[10.1137/15M1035550](https://doi.org/10.1137/15M1035550)；[原文 arXiv:1507.07144](https://arxiv.org/pdf/1507.07144)。

母空间为 $\Gamma_0(\mathbb R^n)$，通过 Moreau 包络 $e_1f$ 的有界集上一致距离度量；这是完备空间，拓扑与 epi-convergence 相容。**Theorem 4.11：强凸函数稠密；Theorem 4.12：强凸函数第一纲。Theorem 4.16：具有强极小点的函数构成剩余集。** 固定强凸模下限的层为闭集，所有强凸函数形成其可数并。

适用判断：强凸这一充分条件可拓扑上很小，而它保障的良好极小值性质却很大；因此“小充分条件”不意味着其理论没有价值。通过 $f\mapsto f+\rho\|\cdot\|^2/2$，可以自然建模固定 $\rho$-弱凸函数；不能将这一全局 weakly convex 结论不加证明地扩张到任意局部 prox-regular 函数。

### 2.4 比第一纲更强的“小”：Bargetz–Dymond

**Christian Bargetz, Michael Dymond**, *σ-porosity of the set of strict contractions in a space of non-expansive mappings*, Israel Journal of Mathematics 214 (2016), 235–244。DOI：[10.1007/s11856-016-1372-z](https://doi.org/10.1007/s11856-016-1372-z)；[原文 arXiv:1505.07656](https://arxiv.org/pdf/1505.07656)。

母空间为 Banach 空间中有界闭凸非单点集 $C$ 上全部非扩张自映射，距离为 $\|T-U\|_\infty$。**Theorem 2.1：严格压缩子类 σ-多孔。Theorem 2.2：若底空间可分，则除去一个 σ-多孔集后，每个映射在 $C$ 的剩余点集上局部 Lipschitz 常数等于 1。**

适用判断：可以比较证书“严格余量”的普遍性，但该文研究的是 Lipschitz 上界 1 内的结构，不是任意 Hölder 映射。多孔性依赖具体度量，不像第一纲只依赖拓扑，不能在换坐标后未经控制直接转移。

### 2.5 拓扑选择可使泛型结论反转：Ravasini–Thimm

**Davide Ravasini, Daylen K. Thimm**, *Generic nonexpansive Hilbert space mappings*, Studia Mathematica 283 (2025), 281–301。DOI：[10.4064/sm240722-12-3](https://doi.org/10.4064/sm240722-12-3)；[原文 arXiv:2407.03881](https://arxiv.org/pdf/2407.03881)。

母空间为可分无限维 Hilbert 空间的闭凸集 $C$ 上非扩张自映射，使用**逐点收敛拓扑**及其完备度量。**Theorem 4.1：当 $C$ totally unbounded 时，无不动点的映射构成剩余集；特别适用于 $C=H$。Theorem 4.2：有不动点的映射集合要么第一纲，要么包含稠密开集。** “totally unbounded”是 Definition 3.1 的专门概念，不能只理解成通常无界。

适用判断：同一无限维非扩张映射全体，在逐点拓扑中泛型无解，与 Wang 的有界集上一致拓扑中泛型唯一解不冲突。这是不能为了得到预期纲结论随意选择拓扑的具体警示。

### 2.6 带共同不动点的序列空间：Reich–Zaslavski

**Simeon Reich, Alexander J. Zaslavski**, *Generic convergence of infinite products of nonexpansive mappings with unbounded domains*, Frontiers in Applied Mathematics and Statistics 1:4 (2015)。DOI：[10.3389/fams.2015.00004](https://doi.org/10.3389/fams.2015.00004)；[原文](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2015.00004/pdf)。

研究完备 hyperbolic 空间闭凸子集上的非扩张映射序列。拓扑对输入有界集一致、且对全部序列下标一致；取“成员具有共同不动点”的序列类的闭包。**Theorem 1.1** 在其中给出剩余类：各成员有共同的唯一不动点，并有带误差迭代乘积的稳定收敛结论。

适用判断：“存在一个共同不动点”不是“预先固定整个非单点不动点集”。原文用于构造稠密集的向某个不动点收缩，会改变多解集；不能据此宣布固定多解 RLEB 比较已解决。

## 三、独立推出的已知理论基线：固定 hypomonotone 母空间中的 monotone 子类

以下是由 Wang 现成定理与 Minty/resolvent 对应得到的**直接推论**。这里给出完整核验；不将其包装成本项目新主定理，也不声称已定位到以完全同样标题陈述它的论文。

### 命题

令 $H\ne\{0\}$ 为实 Hilbert 空间，固定 $\rho>0$。定义

$$
\mathcal H_\rho
=\{A:H\rightrightarrows H:A+\rho I\text{ 极大单调}\},\qquad
\Phi_\rho(A)=A+\rho I,
$$

$$
d_\rho(A,C)=d_{\mathcal M}(\Phi_\rho A,\Phi_\rho C).
$$

则 $(\mathcal H_\rho,d_\rho)$ 完备，且其中的单调算子全体 $\mathcal M(H)$ 为**闭且无处稠密**子集。因此非单调部分是开稠密集。

这里的 hypomonotonicity 固定为全图条件

$$
\langle u-v,x-y\rangle\ge-\rho\|x-y\|^2
\quad((x,u),(y,v)\in\operatorname{gph}A),
$$

并要求移位后的极大性。它不是“submonotone”一词所有可能含义的合并，更不是自动等同于 RLEB 的 RL 条件。

### 证明

**1. 完备性。** $\Phi_\rho:\mathcal H_\rho\to\mathcal M(H)$ 是双射，按定义等距；后者完备。

**2. 单调子类的像。** 对 $A\in\mathcal H_\rho$，$A$ 单调当且仅当 $B=A+\rho I$ 是 $\rho$-强单调。若 $A$ 单调但有真单调扩张 $A'$，则 $A'+\rho I$ 是 $B$ 的真单调扩张，与 $B$ 极大性矛盾，故 $A$ 自动极大单调。反向包含 $\mathcal M(H)\subset\mathcal H_\rho$ 由连续全域单调扰动／Minty 对应得到。

**3. 闭性。** $B\in\mathcal M(H)$ 为 $\rho$-强单调，等价于

$$
\langle a-b,J_Ba-J_Bb\rangle
\ge(1+\rho)\|J_Ba-J_Bb\|^2
\quad\forall a,b\in H.\tag{3.1}
$$

这是把图上两点写成 $(J_Ba,a-J_Ba)$ 后的恒等变形。resolvent 逐点收敛保持 (3.1)，故固定 $\rho$-强单调层闭。

**4. 无处稠密。** 该闭层包含于全部强单调算子类。后者由 Wang Corollary 3.10 第一纲；完备度量空间中的闭第一纲集无内点，因而无处稠密。通过 $\Phi_\rho^{-1}$ 转回即得结论。□

### 这不是任意强行搬来的拓扑，但它有明确覆盖边界

设 $\lambda=(1+\rho)^{-1}$，直接解 resolvent 方程得到

$$
J_{A+\rho I}(x)=J_{\lambda A}(\lambda x).\tag{3.2}
$$

所以 $d_\rho$ 的拓扑等价于实际完整 resolvent $J_{\lambda A}$ 的有界集上一致收敛，具有算法含义。与此同时，

$$
\operatorname{Lip}(J_{\lambda A})\le\lambda^{-1}=1+\rho.
$$

因此，这个母空间**不能自动容纳完整 resolvent 非 Lipschitz 的 RLEB 例子**。它是必须超越／区分的已有理论基线，不是已经选定的 RLEB-vs-LT 共同母空间。此外，移位后 $B$ 的唯一零点解决的是 $0\in A(x)+\rho x$，不是 $0\in A(x)$，不能把 Wang 的泛型唯一零点结论错误移回。

### 平行的弱凸基线

在有限维令

$$
\mathcal W_\rho=\{f:f+\tfrac\rho2\|\cdot\|^2\in\Gamma_0\},
$$

由 $f\mapsto f+\rho\|\cdot\|^2/2$ 拉回上述 Moreau／epi 拓扑。在此完备空间，凸函数对应固定 $\rho$-强凸层；该层 epi 闭，且由 Planiden–Wang Theorem 4.12 第一纲，故凸子类同样闭且无处稠密。这仍是现成定理的直接推论；它既不处理任意局部 prox-regular 图，也不处理本项目的固定多解集与统一 RLEB 预算。

## 四、为什么不能直接套用到固定非单点解集

若研究空间内每个 $T$ 都固定预先给定的 $S$，且 $a,b\in S,a\ne b$，严格压缩根本不存在，因为

$$
\|a-b\|=\|Ta-Tb\|\le c\|a-b\|,\qquad c<1
$$

矛盾。因此，“严格压缩稠密 $\Rightarrow$ 泛型 super-regular”的常见证明模板不能使用。super-regular 在这些文献中指各有界初值集上的迭代一致收敛到**同一个唯一不动点**，不是泛指收敛到随初值变化的 retraction。

更根本地，环境空间的剩余性不传到任意子空间。例如 $\mathbb R\setminus\{0\}$ 在 $\mathbb R$ 开稠密，但与子空间 $\{0\}$ 交集为空。环境中“多个零点”的算子类即便第一纲，在我们刻意固定的多解层中也可能就是整个空间。

还须检查研究空间自身的 Baire 性。单纯要求 $\operatorname{Fix}T=S$ 未必得到闭空间：$T_n=(1-1/n)I$ 在有界集上一致收敛到 $I$，但 $\operatorname{Fix}T_n=\{0\}$、$\operatorname{Fix}I=H$。若采用“至少固定 $S$”则常有闭性，但必须另用统一 EB／排除额外零点的结构确保研究对象没有变。

## 五、哪些语言可以直接借，哪些结论还不能借

| 现成工具／结论 | 可直接用于本项目的部分 | 尚须独立证明的部分 |
|---|---|---|
| resolvent 坐标与完备度量空间 | 为全图算子提供自然拓扑，不必只选一条分支 | 本项目的多值完整 resolvent 是否适合该坐标；共同母空间是否包含两类 |
| 固定常数闭层、可数并 | 将“存在某个有限证书常数”的量词转成 Borel／第一纲分析 | 两套条件的精确量词、局部半径与解集约束；不能擅自把 LT 等同于所有 Lipschitz 映射 |
| 王氏强单调第一纲、弱凸移位推论 | 已有强／弱结构之间巨大纲差别的校准基线 | 固定多解集、固定统一 RLEB 预算后的相对大小 |
| Bauschke–Schaad–Wang 闭无处稠密 | “特殊可积结构在自然算子空间中是小类”的论证范式 | 非线性全图条件和 RLEB／LT 差集，不能靠类比获得 |
| 泛型收敛／唯一解 | 说明哪些空间会使初值选择问题退化 | 保留非单点解集时的极限 retraction 与相对纲 |
| σ-porosity | 比第一纲更定量的候选结论 | 换坐标的度量控制与满足统一预算的孔洞构造 |

一个有意义的目标应形如：先由条件本身确定同一自然 Baire 空间 $\mathcal X$，再研究 $\mathcal R,\mathcal L\subset\mathcal X$ 及 $\mathcal R\setminus\mathcal L$ 的相对内部、纲或多孔性。若只能证明“某个人为参数曲线上的 LT 参数很少”，不能将其称为算子空间中的普遍性结论。

仅写出 $F_\sigma$ 或 $G_\delta$ 复杂度也不够：一个 $G_\delta$ 集未必稠密，一个 $F_\sigma$ 集未必第一纲。密度、闭层内点为空等仍是实质工作。

## 六、prevalence／测度的审计边界

**Brian R. Hunt, Tim Sauer, James A. Yorke**, *Prevalence: A Translation-Invariant “Almost Every” on Infinite-Dimensional Spaces*, Bulletin of the American Mathematical Society 27 (1992), 217–238；[原文 arXiv:math/9210220](https://arxiv.org/pdf/math/9210220)，Definitions 1–2。

其标准母空间是完备度量**线性**空间；Borel 集 $E$ 为 shy 要有非零、可限于紧支撑的见证测度 $\mu$，满足

$$
\mu(v+E)=0\quad\text{对每个 }v\text{ 成立}.
$$

所以在一条例子曲线上随机采样，不是 prevalence 证明。固定不动点集、全图 RL 与严格兼容预算后的类通常不是向量空间；不能直接给它安上平移 prevalence。即便两类在某个更大的线性空间里都 shy，也没有比较出两者内部覆盖能力。本轮尚未取得一个可直接比较本项目两类的 prevalence 定理；此处不作“没有人做过”的结论。

## 七、必须保留的未解决文献线索

以下已确认书目信息和相关性，但没有取得足以核定全部假设的原始全文，故**不提供猜测的定理号，不将摘要转写成已核定理**。

1. **Simeon Reich, Alexander J. Zaslavski**, *Convergence of generic infinite products of nonexpansive and uniformly continuous operators*, Nonlinear Analysis 36 (1999), 1049–1065，DOI：[10.1016/S0362-546X(98)00080-7](https://doi.org/10.1016/S0362-546X(98)00080-7)。作者后续章节介绍该线包含向 nonexpansive retraction 收敛的结论；须取得全文，核对是否保留给定非单点共同不动点集、使用何种母空间和拓扑。
2. **Dan Butnariu, Simeon Reich, Alexander J. Zaslavski**, *Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces*, Journal of Applied Analysis 7(2) (2001), 151–174，DOI：[10.1515/JAA.2001.151](https://doi.org/10.1515/JAA.2001.151)。这是 Bregman 相对非扩张映射空间中的泛型轨道收敛的重要邻近线；全文／定理号尚待核验。不能因为其他已读论文偏重唯一解，就断言“固定多解 retraction 的 Baire 理论从未做过”。
3. **Simeon Reich, Alexander J. Zaslavski**, *Genericity in Nonlinear Analysis*, Springer (2014)，DOI：[10.1007/978-1-4614-9533-8](https://doi.org/10.1007/978-1-4614-9533-8)。[Chapter 5](https://link.springer.com/chapter/10.1007/978-1-4614-9533-8_5) 和 [Chapter 6](https://link.springer.com/chapter/10.1007/978-1-4614-9533-8_6) 是上述原始论文及 accretive resolvent 乘积理论的检索入口；本次只使用可见的作者章节简介／书目定位，不以其替代原定理证明。

关于“submonotone”“prox-regular”精确局部图类、固定 RLEB 证书层的描述集合复杂度，本轮没有核到能够直接结案的定理。术语不唯一、局部化方式与拓扑不同，不能由未检出直接宣告新领域。

## 八、给主协调者的三项可执行结论

1. **Wang Corollary 3.10 + resolvent 完备坐标**：作为已知基线和共同空间设计检查器；第三节给出的 fixed-hypomonotone 推论现已可直接引用为推论并附证，不应宣称它本身就是 RLEB 新发现。
2. **Bauschke–Schaad–Wang Theorem 3.1**：最接近“结构化算子空间中比较不同类有多大”的直接先例；它证明用户设想的研究范式成立，但同时限制“我们首次把算子放进空间用纲比较”的创新表述。
3. **Planiden–Wang Theorem 4.12（配合 4.11、4.16）**：给出弱凸入口及一个价值评判反例——强条件第一纲、强条件保障的结论却泛型。因此最终论文需要同时报告覆盖分离和保留的算法保证，不能只据纲大小判优劣。

最终直答：**有人已经专门研究算子空间与纲分类，并证明相当强的单调／非扩张／proximal 子类大小定理；本项目不是在发明这种语言。尚未核到本项目精确的 RLEB-vs-Luke–Tam 相对纲定理，但是否真正新，仍取决于条件翻译后能否归入已有定理，以及在自然共同母空间中是否证明了新的非平凡分离。搜索空白不能替代这两步。**
