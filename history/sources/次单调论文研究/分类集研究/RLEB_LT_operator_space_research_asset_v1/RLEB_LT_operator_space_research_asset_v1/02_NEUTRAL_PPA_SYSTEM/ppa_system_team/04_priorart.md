# 统一 PPA 动力系统空间：定理级文献与优先权审计

审计日期：2026-09-20。审计范围：中立母空间、长期动力学拓扑、固定多解集、resolvent 家族、可核验证书到动力学性质的接口。**这不是原 RLEB 论文正确性复审，也不以单个反例代替类规模比较。**

## 1. 先给结论

用户提出的“先搭建一个按收敛行为定义的空间，再比较 RLEB 与 LT 在其中的位置”有充分的数学背景，并非只能退回到某个尖点参数族。但其基本语言并非空白：

1. **“所有初值迭代都收敛到某个不动点、不同初值可有不同极限”就是 weakly Picard operator（WPO）思想。**它已有定义、轨道分解、有限长度、残差到选中极限的控制等理论。
2. **固定一个非单点解集、研究算子空间中的泛型极限回缩**，BRZ 2001 已有非常接近的完整定理；不能声称以往只研究唯一解。
3. **“以长期行为定义母空间，并通过所有时间的距离使其成为 Polish 空间”也有直接架构先例**：Tikhonov 的 mixing/leash topology。它不是 PPA 定理，但足以排除“全时间上确界拓扑本身首次提出”的说法。
4. **把不同步长的 resolvent 抽象成相容映射家族**，Leuştean–Nicolae–Sipoş 2018 和 Sipoş 2020/2021 已系统研究；非扩张性加 resolvent identity 的等价定理已存在。
5. 上述工作**没有自动完成**“一个同时容纳非 Fejér 的 RLEB 与 LT、保持完整图和步长身份、以共同动力学不变量作比较的空间理论”，更没有给出其中 RLEB 与 LT 的相对范畴大小。

因此，合理定位不是“从零发明算子空间”，也不是“这些内容全已知”，而是：**用已知语言搭起合适的中立框架，证明完整嵌入与结构定理，最后证明真实的类分离／类规模结论。**这一最后阶段尚不能由现有先例替代。

## 2. 覆盖地图

“固定 S”指母空间定义中事先固定同一个解集，而非每个算子各有一个 Fix(T)；“回缩”不默认连续，连续性另列。

| 文献 | 对象和拓扑 | 固定非单点 S | 极限回缩 | 对本项目的覆盖与边界 |
|---|---|---:|---|---|
| Rus 1993；Rus–Petruşel–Şerban 2006 | WPO；状态空间可重度量，并非 WPO 算子空间的完备拓扑 | 不要求 | 有集合意义的极限选择 | 覆盖收敛母类的行为语言；不提供本项目的统一原几何拓扑 |
| Rus 2016 | 定量 WPO、有限轨道长度、回缩位移界 | 不要求 | 有；一般不预设邻域连续性 | 覆盖证书翻译后的若干动力学性质；不等于 all-pairs RL 或完整纤维 EB |
| BRZ 2001，Th 2.1、3.1、3.2 | 相对 Bregman 非扩张映射；有界集一致拓扑 | **是** | 泛型且有界集一致；连续性有条件 | 最直接的固定多解集算子空间先例；母空间仍预设 Bregman 下降结构 |
| RZ 1999、2014 专著链 | 非扩张／一致连续映射的无限乘积 | 待原文逐项核准 | 文献链涉及回缩 | 不能只凭摘要把其全套假设移植到本项目 |
| Wang 2013，Th 2.13–2.16 | 非扩张／FNE／极大单调三种完备空间；有界集一致 | 否 | 泛型为常值极限、唯一零点 | 覆盖 resolvent 坐标和泛型收敛；严格收缩稠密机制不能直接用于固定多解集 |
| Bauschke–Schaad–Wang 2018，Th 3.1 | 线性单调关系对；resolvent 算子范数 | 否 | 非主题 | 真正的结构类大小比较先例，但局限于线性关系对 |
| Ravasini–Thimm 2025，Th 4.1、4.2、5.3 | 非扩张映射；逐点拓扑 | 否 | 部分几何下为常值极限 | 证明母空间／拓扑改变会改变“泛型”结论 |
| Tikhonov 2013，Th 1 | mixing 群作用；所有时间相关函数的上确界距离 | 不适用 | 不是点轨道回缩 | 直接覆盖“长期行为母类＋全时间 Polish 拓扑”的架构，不覆盖 PPA 图结构 |
| Leuştean–Nicolae–Sipoş 2018，Th 3.13、3.15、5.1 | jointly FNE／jointly(P2) 家族；非算子空间范畴定理 | 共同 Fix，可多解 | 弱／Δ极限；强情形附加假设 | 覆盖抽象 PPA 相容家族和定量模；不覆盖一般非扩张之外的 RLEB |
| Sipoş 2020/2021，Th 3.3、5.3 | 所有正步长 family；resolvent identity | 共同 Fix | 参数趋无穷时得到投影 | identity＋非扩张的表征已知；参数极限不是固定步长迭代极限 |
| Kohlenbach–López-Acedo–Nicolae 2019，Th 4.1、Prop 4.4 | Fejér 序列、regularity modulus、共同收敛率 | 允许多解 | 得到点收敛；无算子空间拓扑 | 证书→共同动力学模的成熟接口；非 Fejér 路线仍需证明 |
| Avigad–Iovino 2013，Th 2.1 |  metric-space sequences 的类及超积 | 不适用 | 无 | 统一 metastability 的逻辑框架；不是统一无限尾界 |

## 3. 已核对原始定理

### 3.1 收敛行为本身：WPO 的真实先例

**Ioan A. Rus, “Weakly Picard mappings”, Commentationes Mathematicae Universitatis Carolinae 34(4) (1993), 769–773。**未查到 DOI；原文永久入口：[DML-CZ](https://dml.cz/handle/10338.dmlcz/118632)，[原始 PDF](https://dml.cz/bitstream/handle/10338.dmlcz/118632/CommentatMathUnivCarolRetro_34-1993-4_14.pdf)。已读定义和 Theorem 1、2。

Definition 2 使用如下行为：连续自映射 f 的每条轨道 fⁿx 收敛，极限是不动点，且允许依赖 x；“strictly”版本增加一致收敛。Theorem 1 则研究是否存在**某个**完备度量使给定集合自映射成为 WPO，以不出现非平凡周期及存在不动点等集合论条件刻画，并联系轨道图收缩。Theorem 2 允许不同吸引域间距离为无穷的广义度量。

**边界：**存在一个重选的度量，不意味着在原 Hilbert 范数下有 PPA 收敛、原始误差界或初值稳定性。该文也没有证明“原几何下全部 WPO”在通常单步拓扑中是完备／Polish。因此它是命名和结构先例，不能替代本项目拓扑定理。

**Ioan A. Rus, Adrian Petruşel, Marcel Adrian Şerban, “Weakly Picard operators: equivalent definitions, applications and open problems”, Fixed Point Theory 7(1) (2006), 3–22。**未核到 DOI；[期刊原始 PDF](https://www.math.ubbcluj.ro/~nodeacj/download.php?f=061rus.pdf)。已读 Definition 1.6、Theorem 6.2、8.1、9.1。

Theorem 8.1 给出 WPO、轨道图收缩、有限长度、Caristi 型函数和不变分割等多种等价刻画，但其中若干项允许改变空间结构／度量。Theorem 6.2 在完备 K-metric 的 closed Q-graph contraction 条件下给出 WPO 及定量尾界

\[
d(A^n x,A^\infty x)\le (I-Q)^{-1}Q^n d(x,Ax).
\]

**覆盖：**按最终选择解的纤维划分空间、再分析纤维内收敛，已有系统理论。**未覆盖：**本项目完整多值图的 RL 条件、不同步长来自同一个图、统一算子空间中的证书类比较。

### 3.2 有限长度与残差—选择极限控制

**Ioan A. Rus, “Relevant Classes of Weakly Picard Operators”, Annals of West University of Timisoara—Mathematics and Computer Science 54(2) (2016), 131–147。**[DOI: 10.1515/awutm-2016-0019](https://doi.org/10.1515/awutm-2016-0019)；已读作者公开全文的 §0–2、Theorem 1.1、1.2、2.1。

记 Π(x)=lim fⁿx；该文使用 ψ-WPO：

\[
d(x,\Pi x)\le\psi(d(x,fx)),
\]

以及轨道长度 W(x)=Σₙd(fⁿx,fⁿ⁺¹x)。Theorem 1.1：WPO 且 W(x)≤c d(x,fx) 推出 c-WPO；1<c<3/2 时还能推出朝自身选中极限的纤维收缩，系数为 (c−1)/(2−c)。Theorem 2.1 从轨道图收缩和轨道连续性推出有限长度及相应误差界。

**必须区分三者：**dist(x,Fix f)、d(x,Πx)、dist(0,A(x))。前两个分别是到整个解集与到选中解的距离，第三个是原多值图的最小残差。文献的纤维内 well-posedness 也不等于跨纤维初值稳定。RLEB 若能推出这些性质，应作为“嵌入已有动力学结构”的定理，不应把 WPO 语言重新命名为原创。

### 3.3 固定多解集与泛型极限回缩：BRZ 2001

**Dan Butnariu, Simeon Reich, Alexander J. Zaslavski, “Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces”, Journal of Applied Analysis 7(2) (2001), 151–174。**[DOI: 10.1515/JAA.2001.151](https://doi.org/10.1515/JAA.2001.151)，[作者原始 PS](https://math.haifa.ac.il/dbutnaru/publications/but-rei-zas-jaa.ps)。已逐项核对 Assumption A、Theorem 2.1、3.1、3.2 及其证明接口。

固定非空闭凸 F⊂K⊂X，以及 Bregman 距离 D_f。母空间为

\[
\mathcal M(f,K,F)=\{T:K\to K:\ D_f(z,Tx)\le D_f(z,x)\quad(x\in K,z\in F)\}.
\]

假设 A 含：小 Bregman 距离控制范数距离、有界性相容、D_f(z,·) 凸且下半连续、存在 Bregman 投影 P。拓扑为有界集上一致收敛；连续映射和有界集一致连续映射分别构成闭子空间 M_c、M_u。

Theorem 2.1 在 P∈M_u 及额外距离相容性下给残余集：Bⁿ 在有界集上一致趋于回缩 P_B onto F；并对附近算子 S 的充分晚迭代统一逼近 P_B。Theorem 3.1 在 D_f 的有界集一致连续假设下给 M／M_c 中相应结论；Theorem 3.2 给初值与算子联合扰动稳定。

**结论：**固定多解集、泛型连续回缩不是空白。**边界：**该母空间预先要求共同的相对 Bregman 下降，不是全部可收敛 PPA。欧氏平方距离相对整个仿射 F 的下降已强烈限制切向漂移，但不能据此断言所有可能 Bregman 几何都排除 RLEB；包含性须另证。

### 3.4 三种经典算子空间：Wang 2013

**Xianfu Wang, “Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent”, Nonlinear Analysis 87 (2013), 69–82。**[DOI: 10.1016/j.na.2013.03.008](https://doi.org/10.1016/j.na.2013.03.008)，[arXiv:1301.6443](https://arxiv.org/pdf/1301.6443)。已核 Prop 2.1、2.3、2.4、Th 2.13–2.16、Cor 3.9–3.10。

非扩张映射 N、FNE 映射 J、极大单调图 M，经 R_A=2J_A−I 联系。距离以

\[
\rho(T,U)=\sum_{m\ge1}2^{-m}
\frac{\sup_{\|x\|\le m}\|Tx-Ux\|}{1+\sup_{\|x\|\le m}\|Tx-Ux\|}
\]

为核心；适当拉回后空间完备且对应同胚／等距。Th 2.13 的机制是严格收缩在指定完备子空间中稠密，由此得到泛型 super-regular：所有初值在有界集上一致趋于同一不动点。Cor 3.10 则说明强单调类第一纲。

**边界：**不固定非单点 S；固定多解集时严格收缩不存在，不能直接复用稠密论证。无限维中有界集一致拓扑严格强于逐点拓扑，不能将二者混写。强单调第一纲也绝不等于“有强单调证书的全部方法没有价值”。

### 3.5 一个真正的结构类规模比较

**Heinz H. Bauschke, Jason Schaad, Xianfu Wang, “On Douglas–Rachford operators that fail to be proximal mappings”, Mathematical Programming 168 (2018), 55–61。**[DOI: 10.1007/s10107-016-1076-5](https://doi.org/10.1007/s10107-016-1076-5)，[作者原文](https://cmps-people.ok.ubc.ca/bauschke/Research/104.pdf)，arXiv:1602.05626。

在 Rⁿ、n≥2 上，L 为极大单调线性关系，S 为凸函数次微分。母空间 (L∩S)²，距离为两项 resolvent 算子范数之和；Prop 2.8 验证相关图收敛／resolvent 收敛等价，空间完备。Th 3.1 证明其中产生 proximal Douglas–Rachford 映射的算子对集合是**闭无处稠密**。

该工作展示了用户所要求的范式：先定同一个有结构的完备母空间，再比较一个可辨认的结构子类，而不是只列一对反例。其结论严格属于线性算子对空间，不能扩大到本项目的一般非线性 PPA。

### 3.6 拓扑不是可忽略的技术细节：Ravasini–Thimm

**Davide Ravasini, Davide K. Thimm, “Generic nonexpansive Hilbert space mappings”, Studia Mathematica 283 (2025), 281–301。**[DOI: 10.4064/sm240722-12-3](https://doi.org/10.4064/sm240722-12-3)，[arXiv:2407.03881](https://arxiv.org/pdf/2407.03881)。已核 §2、Th 4.1、4.2、5.3。

在可分无限维 Hilbert 空间的闭凸 C 上，N(C) 使用逐点拓扑，可用稠密点列的截断加权距离完备度量化。Th 4.1：C 若满足文中 **totally unbounded** 的特定几何条件，泛型映射无不动点。Th 4.2：有不动点的类或者第一纲，或者包含稠密开集。Th 5.3：somewhat bounded 且 LUR 的 C 上，泛型有唯一不动点且所有迭代收敛。

**边界：**这不反驳 Wang，因为拓扑不同；也不反驳固定 S 母空间，因为对象不同。任何 RLEB/LT “大多少”必须同时报告母空间、拓扑、初值域、步长与选择规则。

### 3.7 最贴近“长期行为母空间＋全时间拓扑”的先例

**Sergei V. Tikhonov, “Complete metric on mixing actions of general groups”, Journal of Dynamical and Control Systems 19 (2013), 17–31。**[DOI: 10.1007/s10883-013-9162-y](https://doi.org/10.1007/s10883-013-9162-y)，[arXiv:1207.5255](https://arxiv.org/pdf/1207.5255)。已读 §1–2、Lemma 1、2、Theorem 1。其前身为 Tikhonov 2007 “A complete metric in the set of mixing transformations”, Sb. Math. 198(4), 575–596；2007 原文定理未在本轮逐页核准，不猜 DOI。

固定标准概率空间与可数无限群 G，直接以 mixing 长期性质定义母类 M_G。对描述有限观测差异的距离 a 和通常作用距离 d，定义

\[
m(T,S)=d(T,S)+\sup_{g\in G}a(T^g,S^g).
\]

Th 1：该 mixing 母空间完备且可分。证明以全时间一致控制保持长期 mixing，再用每个对象的尾部性质证明可分。原文同时指出：同一距离放在全部群作用上一般**不可分**，甚至 G=Z。

**准确对应：**“先按长期性质定义母类，再通过轨道的全时间距离获得完备可分结构”已有直接先例。**不能混同：**mixing 是测度相关函数的渐近性质，不是每个点轨道收敛；文中没有完整 proximal 图、固定几何零集和 RLEB/LT。拟建的 PPA 动态拓扑须独立证明，不能只改符号搬用。

### 3.8 抽象 PPA 家族：joint firm nonexpansiveness

**Laurenţiu Leuştean, Adriana Nicolae, Andrei Sipoş, “An abstract proximal point algorithm”, Journal of Global Optimization 72 (2018), 553–577。**[DOI: 10.1007/s10898-018-0655-9](https://doi.org/10.1007/s10898-018-0655-9)，[arXiv:1711.09455](https://arxiv.org/pdf/1711.09455)。已核 Definition 3.6、Th 3.5、3.13、3.15、5.1。

Definition 3.6：若 (1−α)γ_n=(1−β)γ_m，则

\[
d(T_nx,T_my)\le d((1-\alpha)x+\alpha T_nx,
(1-\beta)y+\beta T_my).
\]

Th 3.13 在完备 CAT(0) 空间、共同不动点非空、Σγ_n²=∞、jointly(P2) 条件下给 x_{n+1}=T_nx_n 的 Δ 收敛；Hilbert 版 Th 3.15 为弱收敛。Th 5.1 增加共同 uniform(P2) 模等条件给共同强收敛率，此处局部共同不动点唯一。

**覆盖：**把不同优化问题的 resolvent 统一成公理化 family，属于成熟先例。**边界：**不构造全部收敛 family 的算子空间，不研究其中 RLEB/LT 的类规模；其核心仍是 firm/nonexpansive 结构。序言明确把非凸弱单调及多值 resolvent 作为待发展方向，不能据此声称截至今天仍无人研究。

### 3.9 resolvent identity 的已知表征与两个“极限”

**Andrei Sipoş, “Revisiting jointly firmly nonexpansive families of mappings”, arXiv:2006.02167v3 (2021；首版 2020)。**[原始 PDF](https://arxiv.org/pdf/2006.02167)。本轮未独立核准期刊 DOI，引用 arXiv 即可。已读 Theorem 3.3、5.3 及相应证明。

Th 3.3：在 CAT(0) 空间，正步长家族 jointly FNE 等价于每个 T_γ 非扩张且满足

\[
T_{(1-t)\gamma}((1-t)x+tT_\gamma x)=T_\gamma x.
\]

使用时写 0≤t<1；原文写闭区间而家族仅定义 γ>0，端点应补 T_0=I 或排除，不影响核心表征。Th 5.3 在所列有界性条件下给 γ→∞ 时 T_γx 趋于共同固定点集的最近点投影。

**边界：**γ→∞ 的 resolvent 曲线极限与固定 γ 后 n→∞ 的 T_γⁿx 是两个不同问题。完整非单调图的 representation、不同步长拓扑与选择规则不能从 joint FNE 原样推出。

其后续 **“Abstract strongly convergent variants of the proximal point algorithm”**，[arXiv:2108.13994v4](https://arxiv.org/html/2108.13994v4)，DOI [10.1007/s10589-022-00397-5](https://doi.org/10.1007/s10589-022-00397-5)，Th 3.4 给 Halpern-PPA 到 P_Fu 的强收敛，Th 4.10 给统一 metastability；这些是修改后的迭代，不是未经修改的 PPA。

### 3.10 证书到共同动力学模：regularity modulus

**Ulrich Kohlenbach, Genaro López-Acedo, Adriana Nicolae, “Moduli of regularity and rates of convergence for Fejér monotone sequences”, Israel Journal of Mathematics 232 (2019), 261–297。**[DOI: 10.1007/s11856-019-1870-x](https://doi.org/10.1007/s11856-019-1870-x)，[arXiv:1711.02130](https://arxiv.org/pdf/1711.02130)。已核 Definition 3.1、Th 4.1、Prop 4.4、PPA 应用。

Regularity modulus 写作 |F(x)|<φ(ε)⇒dist(x,zer F)<ε。Th 4.1：若序列关于 zer F 是 Fejér 的，并有

\[
\forall\eta>0\quad\exists n\le\alpha(\eta):|F(x_n)|<\eta,
\]

则 α(φ(ε/2)) 是 Cauchy 模；空间完备且零集闭时给点收敛率。共同 α、φ 和初值范围给共同率。PPA 应用使用 F(x)=dist(0,A(x))，是**完整纤维**残差。Prop 4.4 反向说明：非扩张 T 的共同初值收敛率 ψ 导出 φ(ε)=ε/[2ψ(ε/2)] 的正则模。

**边界：**这是“图证书→中立动力学模”的强先例，不是所有 RLEB 轨道自动 Fejér 的证明；要覆盖非 Fejér 路线必须用其真实有限长度／尾界接口重建桥梁。

### 3.11 统一见证不必是统一无限尾界：metastability

**Jeremy Avigad, José Iovino, “Ultraproducts and metastability”, arXiv:1301.3063v4 (2013)。**[原始全文](https://arxiv.org/html/1301.3063v4)。已核 Theorem 2.1。

对一类度量空间序列，统一 metastability 指

\[
\forall\varepsilon,F\quad\exists b\quad\forall (a_n)\text{ 属于该类}\quad
\exists n\le b\quad\forall i,j\in[n,F(n)]:d(a_i,a_j)<\varepsilon.
\]

Th 2.1 将它与每个相应超积序列的 Cauchy／收敛性质等价联系。这提供把“收敛见证”作为研究结构的已有逻辑框架。它不要求存在统一无限尾界，但也**不能推出**初值连续性或统一收敛率；不同量词次序必须保留。

## 4. 仍需要补齐的原文链与检索边界

### 4.1 RZ 1999 与专著链：不能把未取得全文说成已审完

- **Simeon Reich, Alexander J. Zaslavski, “Convergence of generic infinite products of nonexpansive and uniformly continuous operators”, Nonlinear Analysis 36 (1999), 1049–1065。**[DOI: 10.1016/S0362-546X(98)00080-7](https://doi.org/10.1016/S0362-546X(98)00080-7)。已核出版信息与摘要，**本轮没有取得可逐项审计的原始全文**，故不编定理号与精确固定 S 假设。
- 同作者 **“Generic Convergence of Infinite Products of Nonexpansive Mappings in Banach and Hyperbolic Spaces”**，Optimization and Related Topics，Applied Optimization 47 (2001), 371–402；[DOI: 10.1007/978-1-4757-6099-6_18](https://doi.org/10.1007/978-1-4757-6099-6_18)。本轮核到章节与引用链，未完成逐定理全文审计。
- 同作者 **Genericity in Nonlinear Analysis**，Springer (2014)；[DOI: 10.1007/978-1-4614-9533-8](https://doi.org/10.1007/978-1-4614-9533-8)。相关章为第 2 章 powers、第 4 章 convex Lyapunov、第 5 章 Bregman relative nonexpansiveness、第 6 章 infinite products。仅目录不能证明本项目已被其覆盖。

### 4.2 拓展线：本轮只取直接相关部分

**Tanja Eisner, András Serény, “Category theorems for stable operators on Hilbert spaces”**，[arXiv:0805.1016](https://arxiv.org/pdf/0805.1016)。已核 Th 2.4、3.5、4.3：分别在酉算子的 strong*、等距算子的 strong、线性收缩算子的 weak operator topology 中比较弱稳定与 almost weak stability 的范畴。对象及收敛模式不同于非线性 PPA，只能作为“稳定类比较必须指定拓扑”的校准。

**Constantinos Daskalakis, Christos Tzamos, Manolis Zampetakis, “A Converse to Banach’s Fixed Point Theorem and its CLS Completeness”**，[arXiv:1702.07339](https://arxiv.org/html/1702.07339v3)，[DOI: 10.1145/3188745.3188968](https://doi.org/10.1145/3188745.3188968)。Th 1 在 proper 完备空间、唯一全局吸引不动点、某邻域统一吸引等条件下将状态空间重度量化为收缩，并控制原度量对应；证明使用 supₙd(fⁿx,fⁿy)。这是**单个系统的状态空间度量**，不是不同算子之间的全时间距离，不能误认成完全相同定理。

对于“原单步 compact-open 拓扑中全部逐点收敛系统的精确 Borel／投影复杂度”，本轮没有找到并读到可直接匹配的原始定理。**这只是未解决项，不是首创证据。**若论文以此作为主结果，需要另开针对 descriptive dynamics 的完整审计。

## 5. 对新框架的具体优先权判定

| 拟写内容 | 本轮判定 | 投稿时应如何处理 |
|---|---|---|
| 所有初值收敛、极限依赖初值的母类 | WPO 思想已知 | 直接承认先例，精确说明增加了哪种共同域与算法身份 |
| 极限 Π 是回缩；按 Π 的纤维分轨道 | 基础结构已知 | 可作为基本引理，不包装为主要创新 |
| 固定非点 S 的算子空间及泛型回缩 | BRZ 已有直接结果 | 对照其相对 Bregman 公理，不声称“首次固定多解集” |
| 全时间上确界距离保存长期性质 | 架构先例明确 | 引 Tikhonov；证明自己的 PPA／C_loc 版本和必要限制 |
| resolvent 坐标、单调图与 FNE 对应 | 经典且已有空间理论 | 作为校准，不计原创主贡献 |
| 全步长非扩张族＋resolvent identity | Sipoş Th 3.3 已知 | 引用或简证，再明确非单调推广是否真正超出 |
| 可核验 RLEB/LT 图条件→同一母空间的完整嵌入 | 未被以上结果自动覆盖 | 应列为核心待证接口，保留全图、域、步长、选择量词 |
| RLEB 与 LT 的相对内部／闭包／第一纲／残余性 | 本轮未得现成定理 | 在中立母空间建立后真正证明；不能从既有参数片得出全局结论 |
| 所有 PPA 收敛系统中“RLEB 大很多” | 目前未建立 | 不能宣称百分比、泛型优势或普遍理论优越 |

## 6. 可执行的后续问题，而非预先宣判

1. 先选“固定状态域、固定 S、固定或相容步长、完整 resolvent 或明示选择器”的算法对象；RLEB 和 LT 都不能在定义母空间时获特殊待遇。
2. 区分 C_pt（逐初值收敛）、C_lu（局部一致收敛）、带共同尾界的层。WPO 命名不消除这三者的差别。
3. 对单步拓扑与全时间拓扑分别说明数学和算法含义。更强拓扑可以合法地保持极限选择，但其中的范畴结论不能无条件推回单步拓扑。
4. 把 RLEB／LT 分别送到同一组动力学不变量：轨道长度、共同吸引域、距离下降、点误差尾界、极限选择模、步长稳健性。应证明，不以证书名字代替性质。
5. 只有在这个框架中完成结构性分离定理，才能回答“RLEB 多多少”。即便两个类都第一纲，也未必无法比较；需继续看相对拓扑、闭包、局部厚度或其他明确定义的不变量。

**本轮审计的最终边界：**已有工作为用户要求的路线提供了坚实支点；它们没有替本项目证明 RLEB 比 LT 大，也没有证明两者无实质差别。本轮能负责任地给出的，是把已有语言、可借定理和真正缺口分开，而非宣告整个方向已知或全新。
