# 强弱补偿的第二批技术储备

本页从 `ba456bb` 的[首批 25 项技术和 10 项初试](compensation_trials.md)继续。当前任务是扩大技术储备，并把每项技术变成能够接着试证的具体问题；不是本轮就把全部技术彻底穷尽。已有数学结构可以成为本领域的 M，是否已知与是否有用分开判断。

本批由四位研究者分线搜索、主研究者重构关键证明，合并为 **28 张技术卡和 12 项初试**。技术卡中包括经典端点、旧家族的进一步展开和新检索接口，不是 28 套彼此独立的新理论。I1–I6、A–G、V1–V7、D2–D8、R1–R2 是卡片定位符；V5 与 D1 去重后不另列。完整 M 仍未找到。

阅读顺序：先看端点的精确含义和技术表，再按具体证明义务进入某一初试。每张卡保留一手来源、实际核读深度、原 PPA 接口和首个缺口；摘要层入口不得作为已核定理导入。

## 端点想法应当怎样继续研究

固定原多值关系 F，有限维欧氏空间上的非空闭集 S⊆zer F，步长 λ>0。始终保留
\[
x=y+\lambda v,\qquad v\in F(y),\qquad
r_F(y)=\inf_{w\in F(y)}\|w\|.
\]
空纤维残差记为 +∞。每个试验中进一步缩小对象类时，都在该处明说。

**一个端点已经很明确。** F 极大单调、S=zer F 非空时，每个固定正步长的原 PPA 都有全域唯一根，有限维中点收敛，不要求预先指定误差界。它依靠到每个零点的 Fejér 下降、步长渐消和闭图识别，并不要求统一的距离收缩率。若 S 只是完整零集的真子集，不能保证极限落在该指定子集。经典原文是 Rockafellar 1976 的 Proposition 1 / Theorem 1，见卡 A。

**另一端可以做出一个受限的准确版本。** 原 F 的局部逆映射若单值 Lipschitz，常数为 κ，则 λ>2κ 保证可选出留域、收敛的原 PPA。没有单调性要求，但局部零点孤立。这是下文 C378 的实际证明结果。

**一般非孤立类还不能预先画成连接两个标量最强点的一条曲线。** 原图 F(a,b)=(c b,0)、S=ℝ×{0} 有精确全局误差界 d=r_F/c，c 可以任意大，完整近端却是 J(a,b)=(a−λc b,b)。非解轨道沿解集方向漂移。此计算继承 [F128](../../../FAILED_ROUTES.md#f128) 的剪切机制，本页扩为任意幅度作端点诊断，不再登记为新障碍。

它告诉我们要寻找的补偿边界可能同时依赖步长、方向以及零集结构；它不否定端点搜索。下面优先收集能把这些信息放进同一数学对象的办法，不要求先知道边界必为线段、凸曲线或幂律。

## 技术卡：具体怎样拼接

### 插值与可优化的尺度亏损（6 张）

| 编号 | 技术及一手来源（实际核读位置） | 拼接动作，以及原 PPA 的接口 | 第一缺口 |
|---|---|---|---|
| I1 | Chill–Sharma–Srivastava, *Real interpolation of functions with applications to accretive operators on Banach spaces*, arXiv:2206.13400v1；Example 3.3、§3.1、Theorem 4.1(a) 及证明，PDF pp.6、7、16–17。正式版 JDE 2024。[原文](https://arxiv.org/pdf/2206.13400) | 插值的一端就是完整纤维最小范数。K_F(x,λ)=inf_z[‖x−z‖+λr_F(z)] 与原近端位移可以双侧比较；方向结构进入比较证明，正则性进入同一个包络的下剖面。下文实际推了全对一般 RL 版本。 | 文献讨论 m-accretive/type-ω 及时间正则性，不能把它直接称为一般非单调 PPA 收敛定理；原库仅零锚 RL 时还缺跨图点控制。 |
| I2 | Andrieu–Lee–Power–Wang, *Comparison of Markov chains via weak Poincaré inequalities…*, arXiv:2112.05605，Definition 4、Definition 6、Lemma 7、Theorem 8，PDF pp.4–6。[原文](https://arxiv.org/pdf/2112.05605) | 用一整族 E≤sD+β(s)Φ 保留每个尺度的亏损，而不是硬要一个统一 E≤CD。优化 s 后得凸共轭耗散 profile。已直接代入原 PPA 的端点净收益，见试验2。 | 必须从原图推出该族不等式；若直接把已知下降写成 β，就只是表示工具。Markov 定理的 P*P 不能认作原 F。 |
| I3 | Gentil–Maheux, *Super-Poincaré and Nash-type inequalities for Subordinated Semigroups*, arXiv:1105.3095v2，Proposition 2.2 及证明、Appendix §8，PDF pp.7–9、20–22。[原文](https://arxiv.org/pdf/1105.3095) | 正则/归一化侧 E≤sD+β(s)B 与耗散侧 E·N(E)≤D 由 Legendre 型极值互译。把“各尺度准许多少亏损”与“实际净耗散多大”变成同一 profile 的两种读法。 | 与 I2 同族；原定理假定非负对称算子和 L1 归一化。只有其一维极值动作可不加区别移植，PPA 的 B 必须另有原对象含义。 |
| I4 | Bégout–Soria, *A generalized interpolation inequality and its application to the stabilization of damped equations*, JDE 240(2007),324–356；原 Theorems 2.1–2.2。实际核读作者 HDR 重印 Chapter 7：Theorem 7.2.1 的条件与证明、Example 7.2.9，印刷 pp.124–129（PDF pp.148–152）。[原文](https://www.math.univ-toulouse.fr/~begout/HDR/HDR_Begout.pdf) | 非齐次权重也可拼接：若点态 1≤Φ(w1)Ψ(w2)，且 Φ、Ψ 非负凹，则同一状态的两个加权平均仍满足乘积不等式。能把极弱、甚至指数退化的方向观测与较强的另一观测连接，不限幂型插值。 | 必须找到原 F 的自然联合分解及第二观测的轨道上界。随手制造一个权重分解不能解释原一般 RL。 |
| I5 | Ammari–Ouzahra, *Feedback stabilization for a bilinear control system under weak observability inequalities*, arXiv:1906.11952v1，§2 式(4)、Theorem 2.1(1)–(2)、证明式(14)–(15)，PDF pp.2–4。[原文](https://arxiv.org/pdf/1906.11952) | 弱观测控制较弱范数，较强范数由轨道先验控制；插值把两者拼成能量衰减。一般 H 也有函数型版本。PPA 可试“若干原步的净收益”和“完整残差的窗口观测”，不必每一步统一收缩。 | 需实际证明原 PPA 的窗口关系及强观测上界；原文连续受控系统的反馈不是原算法，不能偷换。 |
| I6 | Cipriani–Grillo, *Hypercontractivity, Nash inequalities and subordination for classes of nonlinear semigroups*, arXiv:0704.3527v2，Lemma 2.8 末尾与 Theorem 2.9，PDF pp.4–6。[原文](https://arxiv.org/pdf/0704.3527) | 非线性半群的正则化/积分尺度通过对数微分及次齐次性，产生生成元方向能量的 Nash 控制，后者再经 Cauchy–Schwarz产生生成元最小范数下界。与“分别加方向和正则假设”不同，它从跨尺度作用产生两侧联系。 | 有严格正性、hypercontractivity、p>2 次齐次性；任意多值 RL 不自动满足。半群和固定步长原 PPA 的一致导入仍须证。 |

### 逆映射、图交截与原根生成（7 张，A 是经典端点）

| 入口 | 一手证据与实际核读位置 | 拼接动作及原步接口 | 第一缺口 |
|---|---|---|---|
| A. Minty 全域覆盖＋Fejér＋闭图识别 | Rockafellar 1976，*Monotone Operators and the Proximal Point Algorithm*，引言(1.6)、Proposition 1、Theorem 1及证明(2.11)–(2.16)。[原文](https://www.ceremade.dauphine.fr/~carlier/Rockafellar1976.pdf) | 覆盖由极大性供给；到每个零点的距离下降给有界和渐近正则；图闭性识别聚点。不要求定量误差界。可把“定量收缩支付”和“无速率的紧性识别”放进同一个候选的退化端点。 | 这是已有端点，新增任务是允许负方向后保住哪种准Fejér结构；不能只保留 d(x,S) 下降而丢掉到每个零点的信息。 |
| B. 强度量正则＝局部逆映射单值 Lipschitz；反向 Banach 修正 | Dontchev–Rockafellar 2004，*Regularity and Conditioning…*，§4 Definition4.1/Theorem4.2。[作者稿](https://sites.math.washington.edu/~rtr/papers/rtr191-RegularityConditioning.pdf) | 从逆侧解原方程 y=M((x−y)/λ)。正则性足够强、相对 λ 足够好时，完全不要求单调性仍能解原根并收敛。下文给自足局部证明。 | 逆单值使局部零点孤立；非孤立零集只能期待商/法向逆映射，须控制切向漂移。一般 Hölder 逆模不再自动使修正为压缩。 |
| C. 扰动半径／Lyusternik–Graves／非线性 Eckart–Young | Dontchev–Lewis–Rockafellar，*The Radius of Metric Regularity*，Theorem3.3；[作者稿](https://people.orie.cornell.edu/aslewis/publications/03-radius.pdf)。同时核 Dontchev–Rockafellar §4 Theorem4.3。 | 正则余量 1/κ 支付 Lipschitz 扰动 L，精确形状 κ/(1−κL)。将 F+(1/λ)I 视为原根方程，直接获得根的局部覆盖，且强逆单值时给原 resolvent 的模。 | 仅次正则不能无条件调用普通正则的稳定半径；原图是否具强逆结构或可用替代需证明。扰动半径首先是可解性/条件数结论，仍须检查其模是否 <1。 |
| D. 倾斜稳定—凸化图识别—局部强单调性 | Drusvyatskiy–Lewis 2013，*Tilt Stability, Uniform Quadratic Growth, and Strong Metric Regularity of the Subdifferential*，Theorem3.3（刊本pp.263–264），并核 Examples3.4–3.5。[作者稿](https://people.orie.cornell.edu/aslewis/publications/13-tilt.pdf) | 在局部极小点且次微分连续的 lsc 势函数类，强正则、prox-regular＋tilt-stable、统一二次支撑、局部强/极大单调图等价。关键是原次梯度图局部等于截断凸包的次梯度图，故两种性质真的由同一局部图产生。 | 局部极小与次微分连续不可删；局部势图不能覆盖任意多值 RL。这是恢复方式范本，非本项目完整定理。与上一批一致凸/对偶光滑有关，但凸化后图的精确保持是额外可迁移动作。 |
| E. 图与零截面的次横截／移动近端平面的横截 | Bui–Cuong–Kruger，*Geometric and Metric Characterizations of Transversality Properties*，§3式(16)、Theorems4–5，特别Theorem4(ii)。[作者上传全文](https://optimization-online.org/wp-content/uploads/2019/07/7275.pdf) | 把 EB 写成 gph F 与 X×{0} 的交截几何；原近端覆盖则是同一 gph F 与仿射平面 {y+λv=x} 的交截。两种要求放到同一图的不同截面，适合找可移动测试平面、法向角和非线性横截模。 | 两套交截条件目前仍可能相互独立；需找到能把它们联系起来的原图性质。不能把输出最近点偷换成输入最近点。 |
| F. 分片线性法向映射／一致定向 | Robinson 1992，*Normal Maps Induced by Linear Transformations*，[出版原文页](https://pubsonline.informs.org/doi/10.1287/moor.17.3.691)。本轮仅核出版摘要，未核全文定理。 | 对多面体C和 F(y)=Ay+N_C(y)，原近端根等价于解 N(z)=(I+λA)Π_Cz+z−Π_Cz=x，然后 y=Π_Cz。同一分片几何的非零同号行列式可供给全域根与逆 Lipschitz。 | 只核摘要，不能据此导入详细参数或泛化到任意分片映射；一致定向给可解性，不自动给迭代稳定。 |
| G. 非线性稠密性定理／逐次修正到精确覆盖 | Ioffe 2013，*Nonlinear Regularity Models*，Theorem1、Theorem4式(5)及Corollary1。[一手作者论文PDF](https://citeseerx.ist.psu.edu/document?doi=422ebd68eb6f547e82ac3c07ff47299bacff367a&repid=rep1&type=pdf) | 近似覆盖＋足够便宜的修正，提升成精确覆盖及一般函数模；候选模满足 ν⁻¹(t)−ν⁻¹(θt)≥μ⁻¹(t)。对 Hλ=I+λF 使用，能把原根存在性与非线性误差模一并从同一图修正机制产生。 | 原 RL 是否产生“残差下降且修正可和”的局部图移动尚缺。工具邻近上轮 Ekeland/strong slope，但这里关注一般多值图的覆盖构造与稠密→精确升级。 |

### 变分支撑、定向凸化与识别（6 张）

| 接口及亲缘关系 | 核读的一手位置 | 可迁移动作和原步接口 | 首个缺口 / 对 Pro 的具体任务 |
|---|---|---|---|
| V1. Variational convexity：在相关局部图块上与凸支撑模型相接 | Rockafellar 2019 [作者稿](https://sites.math.washington.edu/~rtr/papers/rtr251-LocalMono.pdf)，Definition 2、Theorem 1，PDF pp.3–4 | 找一个凸下模型 h≤f，要求有关 `(y,v)` 上图一致且 f(y)=h(y)。由同一模型提供方向支撑与逆映射的变分意义，避免全域凸化丢掉有用图块 | 图块只保留低函数值、低图值；不能将截断图的残差冒作完整纤维残差。任务：在原完整纤维上控制未截断部分的最小范数，并检查原步留在共同图块 |
| V2. Moreau 包络曲率：将变分方向性质转为平滑能量 | Khanh–Mordukhovich–Phat [arXiv:2208.14399v2](https://arxiv.org/pdf/2208.14399)，Proposition 2.2、Theorems 3.2、4.4 | 在原文条件下，variational convexity 对应小 λ 的包络局部凸性；强版本的模为 `σ/(1+λσ)`。原步上 `∇e_λf(x)=(x-y)/λ`，因而方向、位移、能量出自同一原构造 | V1 的同一家族，不另装成独立机制。原文的 f-attentive localization 需保留；一般非势 F 没有 f，原 RL 也不自动给包络凸性。任务：先在弱凸势子类验证两个恢复是否无需另加 EB，再检查是否有非势替代 |
| V3. Elicitable monotonicity：只向缺失方向付出凸化代价 | Rockafellar 2019 [作者稿](https://sites.math.washington.edu/~rtr/papers/rtr252-Decoupling.pdf)，Definition 1、式(1.10)–(1.11)，PDF pp.4–5；Theorem 2 p.8 | 给定约束子空间 N，以 `T+e P_{N⊥}` 激发单调性；约束解满足 `P_{N⊥}z=0`，故解不变。定向罚参数与切向可逆程度之间出现 Schur 补阈值，见试验6 | 原文算法经 partial inverse、localization、rescaling 得到。解不变不等于原 PPA 轨道不变。任务：直接从原端点找补偿项，不能把加罚或 partial inverse 算法当原步 |
| V4. Sharpness × weak convexity：用增长支付负曲率 | Davis–Drusvyatskiy–MacPhee–Paquette [arXiv:1803.02461v1](https://arxiv.org/pdf/1803.02461)，式(2.2)、Assumption A、Lemma 2.1，PDF pp.3、5 | 同一二次支撑式给出无额外驻点的管域 `d<2μ/ρ`；主导增长越强，容许的负曲率或工作域越大。试验5把它代入原 PPA，得到完整残差下界和一步识别 | 原文主算法是 subgradient methods，不能冒称原 PPA 定理。本页原 PPA 结论另有自足证明。下一步将线性 sharpness 换成一般增长 g，并检查何种曲率模可以随尺度变化 |
| V6. Partial smoothness / identification：先消除法向亏损，再在流形上保留弱尺度 | Hare–Lewis 2007 [作者稿](https://people.orie.cornell.edu/aslewis/publications/07-identifying.pdf)，Theorem 1、§3.3 Theorem 4，PDF pp.3–4、6 | 法向 sharpness/nondegeneracy 使轨道有限识别活动流形；流形内可另有慢的单调尺度。试验7给非凸法向、慢切向、非孤立零集的原步完整算例 | 原文 Theorem 4 假设 PPA 已收敛，故不能倒过来拿它证明收敛。任务：用原端点先独立证明留域和法向识别，再建立流形内收敛；两阶段机制还不等于一个 M |
| V7. 增长模与二次代价的 infimal convolution | 包络定义核于 [Khanh 等原文](https://arxiv.org/pdf/2208.14399) 式(2.13)–(2.14)；下面 profile 完全另行证明 | 不先把一般增长压成幂次，直接计算 `inf_t[g(t)+(D-t)_+²/(2λ)]`，保留“能量高度/距离/原位移”同一优化结构，见试验8 | 与上一轮 Young/对偶家族有亲缘，但此处算法没有改成 Young proximal。一般非势 F 缺标量增长，且 profile 下界未必可达。任务：先证明何时由完整图生成一个可达的共同 profile |

### 跨步窗口、未来点与集合储能（7 张）

| 入口 | 核读事实、准确位置与一手来源 | 放回原 PPA 的动作 | 首个缺口与和旧批的关系 |
|---|---|---|---|
| D2. Paracontraction，无统一严格余量 | Elsner–Koltracht–Neumann, 1992, §2 Definition 1、§3 Theorem 1（印刷 pp.306、309–310）；[作者机构存档](https://noah.nrw/ubbihs/download/pdf/5106549)。连续映射相对任一固定点严格缩短距离，除非当前点已固定；有限映射池公用固定点时，适当出现顺序的迭代收敛。 | 对原 resolvent 的一个连续合法选择 T，检验 ‖Tx−z‖<‖x−z‖，允许余量随 x→S 任意趋零。方向与残差合成后的收益不必有统一正比例。 | 单步严格性加连续性仍需稳定根选择；一般多值 J 的连续选择并不存在。与卡 A 的 Fejér 端点同一家族，不计作独立统一结构。 |
| D3. 有限步 Lyapunov／窗口可观测性 | Geiselhart–Wirth, arXiv:1406.3224v2，Definition 3.8、Theorem 4.1（PDF pp.8–9），[原文](https://arxiv.org/pdf/1406.3224)。能量只需在 M 步后下降，配合全局 K 有界性可推出 ISS；M 必须确定。 | 原恒等式沿 M 条合法边求和，检查方向亏损和残差收益的窗口总账；允许单步扩张。下文二分支全图例验证两步才收缩。 | 窗口中的中间根必须可续接并留域；存在选择结论和所有根结论不同。与旧 IQC／动态乘子相邻，新增明确的有限窗口接口。 |
| D4. Matrosov 辅助函数层级 | Nešić–Teel, *Matrosov theorem for parameterized families of discrete-time systems*, Automatica 40 (2004), 1025–1034，[论文出版页](https://doi.org/10.1016/j.automatica.2004.01.016)。本轮只核摘要及引言：多个一阶差分半负定的辅助函数可以检验一致渐近稳定。正文未取得，不借用其具体定理。 | 第一个能量只控制某些方向时，在其零耗散集合上用第二个观测排除非解运动，再逐层缩小坏集合。可避免一开始就要求残差对全状态定量控制。 | 每层零耗散集合的传递要从原图推出。它和 hypocoercivity 都会用多个观测，但不是随意加一个正权重就结束。暂为值得 Pro 深读的入口。 |
| D5. 集值 Lyapunov／点态渐近稳定 | Goebel, *Set-valued Lyapunov functions for difference inclusions*, 作者稿 Theorems 3.1、3.3、Definition 2.2，[原文](https://webpages.math.luc.edu/~rgoebel1/publications/GoebelSVLF.pdf)。Theorem 3.1 的严格嵌套条件为 W(J(x))+α(x)B⊂W(x)；Theorem 3.3 允许非严格嵌套但需连续候选、J 外半连续局部有界，等号只能在平衡集发生。 | 用包住后继可能位置的集合 W(x)，同时记录法向缩小和切向落点，弥补标量 d(x,S) 完全不记录沿 S 漂移的问题。 | 从原 F 的廉价局部数据构造 W，而非把全部未来可达集直接命名为 W。文中 Example 2.6 自己指出可达集嵌套不足以推出点态稳定；不能跳过严格性／不变性门。 |
| D6. 自收缩曲线／未来点法向几何 | Daniilidis–David–Durand-Cartagena–Lemenant, *Rectifiability of Self-contracted curves...*, Theorem 3.3、Proposition 4.16，[作者存档](https://arxiv.org/pdf/1211.3227)。有界自收缩曲线在有限维有有限长度，凸近端序列形成自收缩折线。 | 以所有未来迭代点为比较点，角度控制直接产生长度。凸次梯度 PPA 在非空 argmin 时可这样证明，不需指定 EB／KL 模。下文展开原步证明。 | 一般非单调 F 没有凸次水平集；需找松弛自收缩结构或有界转角预算。该几何方法超出旧“先估残差衰减再求长度”的思路。 |
| D7. 非相切性／连续平衡集的半稳定 | Bhat–Bernstein, SIAM JCO 42(5), 2003，Proposition 4.1、Proposition 5.2、Corollaries 5.1–5.2，[作者 PDF](https://www.aero.iitb.ac.in/~bhat/siam_nontangency.pdf)。核读的是连续时间：用方向锥与不变极限集合的切锥关系排除多点极限集合。 | 原步可分法向／切向时，尝试用法向总变差支付切向位移；无需先有法向线性速率。下文产品型完整多值例自足证明。 | 连续流的方向锥定理不等于离散原 PPA 定理。对弯曲 S、一般多值法向和无符号抵消，需另建离散结构。 |
| D8. IOSS 检测性与两储能供给重配 | Laila–Nešić，2002 IFAC 会议稿，§3 Lemma 3.1、Theorems 3.1–3.2、§4.1，[原文](https://skoge.folk.ntnu.no/prost/proceedings/ifac2002/data/content/00713/713.pdf)；后续 [2003 作者存档](https://eprints.soton.ac.uk/203209/)。会议稿已核读文本，部分公式字符损坏，故不逐符号导入定理。它通过重标度两个辅助 IOSS 能量后相加，建立单个能量没有的稳定性质。 | 一个观测提供半正耗散，另一个提供“看见残差便看见状态”的动态检测性；再调供给率使共同观测项相消。可研究以窗口残差替代点态 EB。 | 须由原图给出两个观测之间的兼容测量，不能把两旧条件简单命名为两个能量。是旧第25项供给重标度的离散、双能量推进，明确不计作全新无亲缘理论。 |

### 线性化余量与积分覆盖（2 张）

| 入口 | 一手来源与核读层级 | 拼接动作 | 原 PPA 首个义务 |
|---|---|---|---|
| R1. Kantorovich 一般控制函数／majorant | Ferreira–Svaiter, 2006 作者稿，Theorem 2 的(1)–(2)、h1–h4，[PDF](https://webdoc.sub.gwdg.de/ebook/serien/e/IMPA_A/434.pdf)，正文已核。 | 把逆条件数、初始缺口、导数变化编入同一个标量控制函数；标量可行区同时给根存在、唯一性和定位。下文只迁移其余量组织动作，另作原 PPA 自足试验。 | 应作用于 Hλ=I+λF 的求根；Newton 只是内层找原根的工具，不能把 Newton 轨道当原 PPA。一般多值/非光滑版须另核条件。 |
| R2. Hadamard–Lévy 积分逆定理／路径提升 | Plastock, *Homeomorphisms between Banach spaces* (1974)，[作者机构摘要](https://researchwith.njit.edu/en/publications/homeomorphisms-between-banach-spaces/)，本轮只到摘要层；原 PDF 未能取得。 | 局部可逆性加随半径变化的逆条件数积分，提升为全局可逆；不是强求一个统一全局最小奇异值。 | 对 Hλ 验局部可逆和积分发散可研究 coverage；即使 Hλ 是全局同胚，原反复近端是否趋稳仍须另证。未核正文，不导入定理。 |

## 十二项原对象初试

前四项分别研究同一变分包络、一般尺度耗散、逆侧端点和精确覆盖。随后四项在势算子子类里拆解实际拼接，最后四项检验窗口、锥、未来点和余量。子类试证只按其对象成立，不替代一般多值非线性目标。

<a id="k-functional"></a>
## 试验 1 / C377：完整残差的 K 包络



### 对象

H=R^n，F:H⇉H 为非空图关系，r_F(z)=inf{‖w‖:w∈F(z)}，空纤维记 +∞。固定 λ>0，定义

\[
K_F(x,\lambda)=\inf_{z\in\operatorname{dom}F}
   \{\|x-z\|+\lambda r_F(z)\}
 =\inf_{(z,w)\in\operatorname{gph}F}
   \{\|x-z\|+\lambda\|w\|\}.
\]

第二个等号只是下确界交换，不要求纤维最小范数达到。K 同时惩罚到试验图点的距离和原完整纤维的残差，是独立于迭代收敛的变分对象。它不需要凸势、孤立零点或线性模。

**另一独立身份。** K_F(·,λ) 是 λr_F 的最大 1-Lipschitz 下包络：K 有限、非负且 1-Lipschitz，并且 K≤λr_F；若实值 1-Lipschitz 函数 g≤λr_F，则 g(x)≤g(z)+‖x−z‖≤λr_F(z)+‖x−z‖，对 z 取下确界即 g≤K。K 的 Lipschitz 性由三角不等式逐点取下确界得。若 gph F 闭，则 K_F(x,λ)=0 当且仅当 0∈F(x)：K=0 给 z_j→x、w_j∈F(z_j)、w_j→0，闭图识别；反向取 z=x。闭图不可略去，例如所有纤维为 (0,1) 时 r_F=0 而没有零点。

### 1A. 最大单调端的自足 Hilbert 比较

暂假设 F 单调且 I+λF 全域可逆，J=(I+λF)^−1。定义 D(x)=‖x−Jx‖。则对所有 x∈H，

\[
\boxed{D(x)\le K_F(x,\lambda)\le2D(x).}
\]

这与文献 Theorem 4.1(a) 同一机制；原文 Banach/type-ω 常数较粗。本页的 Hilbert 常数由 firm 性质直接得到。

证明右界：令 y=Jx、v=(x−y)/λ∈F(y)，在 K 中只选 z=y 即得 K≤‖x−y‖+λr_F(y)≤2D。

证明左界：T=I−J 在 Hilbert 范数下为 1-Lipschitz。事实上对两个输入之差 a、输出之差 b，单调性给 <b,a−b>≥0，故 ‖a−b‖²≤‖a‖²。对任意 z∈dom F，另由单调性比较 (Jz,(z−Jz)/λ) 和任意 (z,w) 得 ‖Tz‖≤λ‖w‖，所以 ‖Tz‖≤λr_F(z)。因此

\[
D(x)=\|Tx\|\le\|x-z\|+\lambda r_F(z).
\]

对 z 取下确界即证。完整残差从纤维下确界进入，没有把选中 v 当作 r_F(y)。

### 1B. 全对一般 RL 的非线性版——原 PPA 保持不变

暂假设 I+λF 的完整逆关系全域非空，并对任意 (y,v),(z,w)∈gph F 有

\[
\|(y-z)-\lambda(v-w)\|
\le\omega(\|(y-z)+\lambda(v-w)\|),
\]

其中 ω:[0,∞)→[0,∞) 连续、非减、ω(0)=0。比较相同输入时右侧为零，故完整逆关系自动单值，记 J。

T=I−J 的模满足

\[
\|Tx-Tx'\|\le H(\|x-x'\|),\qquad
H(s)=\tfrac12(s+\omega(s)).
\]

对任意 (z,w)∈gph F，取 x'=z+λw，则 Jx'=z、Tx'=λw。因此若 c=‖x−z‖+λ‖w‖，有

\[
D(x)\le H(\|x-z-\lambda w\|)+\lambda\|w\|
\le H(c)+c.
\]

取完整图下确界，利用 H 连续，得到

\[
\boxed{\frac12K_F(x,\lambda)\le D(x)
\le\frac{3K_F(x,\lambda)+\omega(K_F(x,\lambda))}{2}.}
\]

左界 K≤2D 不需要 RL。这个结论保留一般非线性 ω、多值纤维和完整真残差；但全对 RL 迫使固定 λ 的完整近端单值。它不能由仅零锚的 RL 自动得到，也没有自行证明收敛。

**精确断点。** 原项目当前若仅有锚式反射模，无法比较 x 与任意试验点 z+λw，故上述上界证明在这一行缺条件。不能把对整个图点可比较的假设悄悄加入原定理。下一任务是寻找仅用锚式版本仍可用的相对 K 包络，而非据此淘汰技术。

### 1C. 同一包络如何读完整真残差的正则性

设非空闭 S⊆F^−1(0)，χ:[0,∞)→[0,∞) 连续、非减、χ(0)=0。若在**整个试验域**中

\[
r_F(z)\ge\chi(d(z,S)),
\]

则对任何 x 有

\[
c_\lambda(d(x,S))\le K_F(x,\lambda)\le d(x,S),
\quad
c_\lambda(t)=\inf_{0\le b\le t}
   \{t-b+\lambda\chi(b)\}.
\]

证明：置 a=‖x−z‖、b=d(z,S)，由距离函数 1-Lipschitz 有 a+b≥t=d(x,S)。若 b≤t，则 a+λr_F(z)≥t−b+λχ(b)≥cλ(t)；若 b≥t，则 a+λr_F(z)≥λχ(t)≥cλ(t)。上界在 K 中取最近零点即可。

反过来，若对 x∈dom F 已知 K_F(x,λ)≥h(d(x,S))，则选 z=x 直接给

\[
\lambda r_F(x)\ge h(d(x,S)).
\]

所以一般非线性真残差正则性，与同一 K 包络的距离下剖面可以双向转译；前向多了一次精确的一维 inf-convolution。局部版本必须限制试验 z 的范围并核对最近零点是否可用，不能把局部 EB 当全局 EB 使用。

### 1D. 方向恢复：所有值平移的包络比较能恢复两点单调性

假设对每个 λ>0，完整 J_{λF} 全域存在且单值。则以下两条等价：

1. F 极大单调；
2. 对每个 a∈H、λ>0、x∈H，令 G=F−a，均有 D_G(x)≤K_G(x,λ)。

这里完整 coverage 与单值假设已经固定在该命题的对象类中，因而方向恢复应表述为“极大单调”。1⇒2 由 1A；值平移保持单调性和全域原根。

2⇒1：任取 (y,v),(z,w)∈gph F，取 a=w 和 x=y+λ(v−w)。因 J_{λ(F−w)}x=y，且 0∈(F−w)(z)，有

\[
\lambda\|v-w\|=D_{F-w}(x)
\le K_{F-w}(x,\lambda)
\le\|y-z+\lambda(v-w)\|.
\]

平方并消去 λ²‖v−w‖²，得

\[
0\le\|y-z\|^2+2\lambda\langle y-z,v-w\rangle.
\]

λ→∞ 得 <y−z,v−w>≥0，所以 F 单调。全域 coverage 使它极大：若 (z,w) 与整图单调相关，选 λ>0 并由 z+λw=y+λv、v∈F(y) 解原根，则 <z−y,w−v>=−λ‖w−v‖²≥0，故 z=y、w=v。这证明极大性，无需在此偷用尚未验证的定理。

**价值与边界。** 这是一种可复核的变分表达：方向性质通过“所有值平移、所有尺度的原近端实现”恢复；正则性通过相同 K 的距离下剖面恢复。它源自经典 resolvent/插值机制，不主张新颖性。固定 λ 的比较、没有值平移的比较，都不能冒充这个方向恢复。全 λ 全域单值条件也会排除原任务要覆盖的许多非单调情形；因此尚不能将本页拼成一般非线性原 RL 的完整 M。

### 1E. 独立攻击：固定 λ 的所有值平移比较仍可容纳非单调稳定图

取 H=R²、Q 为 90 度旋转、A=−I/4+Q、F(y)=Ay、λ=1。则 <h,Ah>=−‖h‖²/4，F 非单调；但 I+A=(3/4)I+Q 的每个奇异值为 5/4，故完整 J 全域唯一且收缩因子 4/5，原 PPA 从所有初值收敛到零。又 ‖Az‖=(√17/4)‖z‖，所以

\[
K_F(x,1)=\inf_z[\|x-z\|+(\sqrt{17}/4)\|z\|]=\|x\|,
\qquad D_F(x)=\frac{\sqrt{17}}5\|x\|\le K_F(x,1).
\]

等号 K=‖x‖ 由三角不等式及取 z=0 得。对任意值平移 F−a，令 z_a=A⁻¹a，K、D 分别等于 ‖x−z_a‖、(√17/5)‖x−z_a‖，故所有值平移的固定 λ 比较仍成立。于是 1D 的“所有 λ”确实不可删除；同时，固定步的包络比较并非只允许单调算子。这个例子把该技术接到了一个真实非单调稳定区间，没有改变算法。


<a id="weak-profile"></a>
## 试验 2：任意尺度亏损与净收益 profile



这里先限 S={0}。固定 λ>0，设每个原输入都有合法原根；对每个受检图点 (y,v) 定义原端点净收益

\[
Q_\lambda(y,v)=2\lambda\langle y,v\rangle+\lambda^2\|v\|^2,
\quad x=y+\lambda v,
\quad\|x\|^2-\|y\|^2=Q_\lambda(y,v).
\]

设有 β:(0,∞)→[0,∞)，β(s)→0 (s→∞)，以及有限、非负、在有界集上有界的 Φ:H→[0,∞)，使对所有受检 (y,v)、所有 s>0 有

\[
\|y\|^2\le sQ_\lambda(y,v)+\beta(s)\Phi(y).
\tag{W}
\]

若 y≠0，取 s 足够大即知 Qλ>0；y=0 时 Qλ=λ²‖v‖²≥0。故任何合法轨道的范数不增。在初始球上取 M≥sup Φ>0。令

\[
B(u)=u\beta(1/u),\quad B(0)=0,
\qquad B^*(a)=\sup_{u\ge0}\{ua-B(u)\}.
\]

将 (W) 除以 s，并用 Φ(y)≤M，逐步优化得

\[
\|x^k\|^2-\|x^{k+1}\|^2
\ge M B^*(\|x^{k+1}\|^2/M).
\tag{D}
\]

B* 非减，且对 a>0 严格正：选 s 大到 β(s)<a/2，u=1/s 即得 ua−B(u)>0。若范数极限 l>0，则 (D) 的每步下降至少 M B*(l²/M)>0，矛盾。因此每条无限原轨道趋 0。这里不要求统一比例收缩，也未改原算法。

若 β(s0)=0，则直接恢复统一收缩：‖y‖²≤s0Qλ，所以 ‖y‖²≤s0/(1+s0)‖x‖²。若 β(s)=c s^−p，p,c>0，则

\[
B^*(a)=p(p+1)^{-(p+1)/p}c^{-1/p}a^{1+1/p},
\]

得到慢尺度的非线性下降递推。幂型只是示例，方法本身不限幂型。

**首个真实缺口。** 目前没有从原一般 RL 和完整残差 EB 自动导出 (W) 的低成本办法。Qλ 虽把方向和幅度放在一起，若把 (W) 直接假设下来，它本身已含严格端点净收益，不能据此说共同来源被发现。该技术的新增价值是用可优化的整族尺度亏损组织研究，而不是预先固定一个收缩常数。非孤立 S 时还须改用合法输入最近锚并另外处理切向漂移。


<a id="inverse-endpoint"></a>
## 试验 3 / C378：局部逆侧的原 PPA 端点



**精确局部命题。** 设 F:ℝⁿ⇉ℝⁿ，0∈F(s)。存在开邻域 U∋s、V∋0，使

\[
M(w):=F^{-1}(w)\cap U
\]

对每个 w∈V 恰为一个点，M(0)=s，且 ‖M(w)−M(w′)‖≤κ‖w−w′‖，κ>0。固定 λ>2κ。则存在 R>0，使每个 x⁰∈B̄(s,R) 存在一条原合法 PPA 轨道，所有点留在该球，且

\[
\|x^{k+1}-s\|\le q\|x^k-s\|,
\qquad q=\frac{\kappa}{\lambda-\kappa}<1.
\]

这是局部选出的原根结论；不声称域外其他原根也收敛。

**证明。** 取 R>0 使 B̄(s,R)⊂U、B̄(0,2R/λ)⊂V。固定任意 x∈B̄(s,R)，在该闭球上令

\[
T_x(y)=M((x-y)/\lambda).
\]

由 M(0)=s，‖T_x(y)−s‖≤κ‖x−y‖/λ≤2κR/λ<R，且 T_x 的 Lipschitz 常数 κ/λ<1。Banach 定理给唯一球内不动点 y。设 v=(x−y)/λ，则 y=M(v) 意味 v∈F(y)，所以没有改变算法。再用

\[
\|y-s\|\le\frac{\kappa}{\lambda}\|x-y\|
\le\frac{\kappa}{\lambda}(\|x-s\|+\|y-s\|)
\]

得所述 q。球内留域、无限续接和点收敛随之成立。□

**完整残差边界。** 缩小 R，还可令 R≤κη，其中 B̄(0,η)⊂V。对任意球内 y 和任意 w∈F(y)，若 ‖w‖≤η，则 y=M(w)，故 ‖y−s‖≤κ‖w‖；若 ‖w‖>η，则 ‖y−s‖≤R≤κη<κ‖w‖。对完整纤维取 inf 得 ‖y−s‖≤κr_F(y)。因此本命题没有以选值残差假装完整残差。

**阈值为何有意义。** 取 F(y)=−ay，a>0，s=0，κ=1/a。原步是 y=x/(1−λa)，其全部非零轨道趋零当且仅当 λa>2，正是 λ>2κ。λa=2为二周期；0<λa<2且λa≠1时发散；λa=1时非零输入无根。这说明“正则侧单独足够强”确实存在，但须说明相对步长和逆结构，不能只说正则性越强越好。

**方向与幅度接回同一图的下一步。** 若在同一局部图上还有 hypomonotonicity
⟨y−z,v−w⟩≥−ρ‖y−z‖²，则原步差的平方直接给

\[
\|x-x'\|^2\ge(1-2\lambda\rho+\lambda^2/\kappa^2)\|y-z\|^2.
\]

逆侧幅度和方向余量在此明确共同支付。此公式本身与上一批联合数值几何同源，不另计为新理论；新价值在于 B/C 还供给局部根，避免只证明“若已有根则收缩”。


<a id="graph-correction"></a>
## 试验 4：近似图修正产生精确原根



以下自足引理抽取 G 的修正动作，并不冒称原RL自动满足其假设。

令 H:ℝⁿ⇉ℝⁿ 图闭；固定目标 x，0<θ<1，a:[0,r₀]→[0,∞)非减，且

\[
\Psi(r)=\sum_{j\ge0}a(\theta^jr)<\infty.
\]

假设在所用闭工作域内，每个图点 (y,h) 满足 0<‖x−h‖≤r₀ 时，都能找到另一个同域图点 (z,g) 使

\[
\|x-g\|\le\theta\|x-h\|,
\qquad \|z-y\|\le a(\|x-h\|).
\]

则从任意起始图点 (y₀,h₀)出发，该修正产生 Cauchy 序列 y_j，h_j→x，闭图给 x∈H(y∞)，且 ‖y∞−y₀‖≤Ψ(‖x−h₀‖)。证明只是将两条估计逐次代入并求和；若r_j=0则停止。局部版本须保证Ψ预算留在工作域，不能省略。

取 H(y)=y+λF(y)，它的图由原F图经可逆线性变换得到，故F闭图时H闭图。得到的 x∈H(y∞) 就是原近端根。a(r)=Cr^α、α>0时，Ψ(r)=Cr^α/(1−θ^α)，直接保留非线性误差模。这项技术先解决 coverage；它不自动证明原PPA跨步收敛。


<a id="sharp-capture"></a>
## 试验 5 / C380：同一弱凸支撑给完整残差与原步捕获



**对象、范围。** 有限维欧氏空间上，f 为 proper lsc、ρ-弱凸函数，ρ≥0，且 f 有有限全局最小值 f_*，非空闭最小点集 S。设在 `0<d(z,S)<R` 内有

\[
f(z)-f_*\ge g(d(z,S)),\qquad g(t)\ge0.
\]

令 F=∂f 为 limiting subdifferential，并取 λ>0、λρ<1。本试验允许完整多值纤维、非孤立 S、一般 g；但明确仅为势算子子类。

因为 `f+ρ‖.‖²/2` 凸，函数 `f(z)+‖z-x‖²/(2λ)` 强凸且因 f 下有界而 coercive；每个 x 有唯一全局近端最小点 y。对原 F 的任意根 `x-y∈λ∂f(y)`，一阶条件也是这个强凸问题的充分条件，故原完整 resolvent 就是该唯一最小点。这里没有改变原 PPA。

**同一支撑产生完整残差。** 弱凸性对每个 `w∈∂f(y)` 及每个 z 给

\[
f(z)\ge f(y)+\langle w,z-y\rangle-\frac\rho2\|z-y\|^2.
\]

取 `p_y∈P_S(y)`、t=d(y,S)∈(0,R)，得到

\[
\langle w,y-p_y\rangle\ge g(t)-\frac\rho2t^2,
\qquad
r_F(y)\ge\left[\frac{g(t)}t-\frac\rho2t\right]_+.
\]

这对整个原纤维成立，最后才取 inf，并非用选中图值替换真残差。注意它使用**输出**最近点，目的仅是证明残差下界，不用于输入距离恒等式。

**原近端最小化给距离/步长。** 记 D=d(x,S)、s=‖x-y‖。取输入最近点 `p_x∈P_S(x)` 比较近端目标：

\[
f(y)-f_*+\frac{s^2}{2\lambda}\le\frac{D^2}{2\lambda}.
\]

若 t<R，因而

\[
D^2\ge 2\lambda g(t)+s^2.
\]

两条公式使用同一原 f 的支撑与实际最小化，不需要额外假设 EB。

**线性 sharpness 的一步捕获。** 若 g(t)=μt，μ>0，则对所有

\[
d(x,S)<\min\left\{\frac R2,\frac{\lambda\mu}{1+\lambda\rho}\right\}
\]

的输入，其唯一原输出 y∈S，从而原 PPA 一步到 S 并固定。

证明：因 f(y)≥f_*，上述近端比较给 s≤D；距离函数 1-Lipschitz，t≤D+s≤2D<R。若 t>0，完整残差式给 `r_F(y)≥μ−ρt/2≥μ−ρD`，而实际 v=(x-y)/λ 满足

\[
\frac D\lambda\ge\|v\|\ge r_F(y)\ge\mu-\rho D.
\]

这与 `D<λμ/(1+λρ)` 矛盾。于是 y∈S。下一步以 y 为输入，近端目标在 y 唯一达到最小值，故保持不动。□

**它改变了什么认识。** 增长强度 μ、负曲率 ρ、步长 λ 在同一捕获半径中显式耦合；原完整纤维和非孤立 S 不妨碍这个结论。不能据此说一般 RL 目标已经被势算子替代。这个半径是所给证书的充分半径，未证全算子类锐性。


<a id="schur-compensation"></a>
## 试验 6：Schur 补给精确定向补偿门



设 `N=R^m×{0}`，在 R^(m+l) 上

\[
f(z,w)=\tfrac12\langle Hz,z\rangle+\langle z,Bw\rangle
       +\tfrac12\langle Cw,w\rangle,
\quad H=H^\top\succ0,\ C=C^\top.
\]

加入定向罚项 `e‖w‖²/2` 的 Hessian 为

\[
\begin{pmatrix}H&B\\ B^\top&C+eI\end{pmatrix}.
\]

完成平方恒等式为

\[
\langle Hz,z\rangle+2\langle z,Bw\rangle+\langle(C+eI)w,w\rangle
=\|H^{1/2}(z+H^{-1}Bw)\|^2
 +\langle(C+eI-B^\top H^{-1}B)w,w\rangle.
\]

故严格凸化恰需 `C+eI−BᵀH⁻¹B≻0`，即

\[
e>\lambda_{\max}(B^\top H^{-1}B-C).
\]

这是精确的“切向强度越弱，法向补偿越贵”的门；所有符号为原 block 数据，不靠自由 Young 参数。它是数学家如何实施拼接的清楚范本，但 e 是定向凸化代价，不能直接等同于原 F 的 metric subregularity 模。

**原步阻断。** 取 `F(z,w)=(z,-w)`，`λ=1/2`。此 F+eP_(N⊥) 在 e≥1 时最大单调、e>1 时强单调，但原 PPA 为

\[
(z^{k+1},w^{k+1})=(2z^k/3,2w^k),
\]

非零 w 发散。因而“可被激发出单调性”本身不能证明原步稳定。后续要利用原端点真实产生的项支付 e，而不是直接运行加罚后/partial-inverse 算法。


<a id="identification"></a>
## 试验 7：有限识别与慢尺度同处原步



在 R^3 的坐标 (u,z,w) 上取 μ,ρ>0，`0<R<μ/ρ`，

\[
f(u,z,w)=z^4+\mu|w|-\frac\rho2w^2+\delta_{[-R,R]}(w),
\quad F=\partial f,
\quad S=\mathbb R\times\{0\}\times\{0\}.
\]

f 为 proper lsc、ρ-弱凸且非凸，S 正是全部最小点，亦为 zer F：在 w∈(0,R] 的 subgradient 全为正，在 w∈[-R,0) 全为负；z 坐标为 4z³。取 λρ<1，每个输入唯一原根。

u 坐标固定；z 坐标满足 `z_k=z_(k+1)+4λ z_(k+1)^3`，因同号及模递减，极限满足 4λl³=0，故 z_k→0。这个尺度没有线性 EB：在 w=0 处完整真残差是 `4|z|³`，距离是 |z|。

w 坐标为原二次最小化的唯一解：

\[
w_{k+1}=\operatorname{clip}_{[-R,R]}
 \left(\frac{\operatorname{sign}(w_k)(|w_k|-\lambda\mu)_+}{1-\lambda\rho}\right).
\]

若 |w_k|≤R，非零未捕获时（例如 w_k>λμ）有

\[
w_k-w_{k+1}=\frac{\lambda(\mu-\rho w_k)}{1-\lambda\rho}
\ge\frac{\lambda(\mu-\rho R)}{1-\lambda\rho}>0.
\]

截断实际不激活，因为这个候选在 [0,w_k) 中。因此有限步之后 |w_k|≤λμ，下一步 w=0，此后保持零。原轨道收敛到 `(u_0,0,0)∈S`。

**意义与界限。** 它示范“不同方向使用不同尺度”，比一个最坏常数更有信息；法向非凸由 sharpness 支付，切向最大单调允许很弱的残差。它是完整算例，但可分结构过强，尚不是完整 M，也没有解释一般非可分耦合。向弯曲流形扩展时，曲率引起的交叉项正是下一 proof obligation。


<a id="growth-profile"></a>
## 试验 8：一般增长与原二次代价的共同 profile



设 f proper lsc、下有界且 S=argmin f≠∅，并对所有 z 有 `f(z)−f_*≥g(d(z,S))`，g:[0,∞)→[0,∞) 非减、g(0)=0。对包络的定义直接用 `‖x−z‖≥[d(x,S)−d(z,S)]_+`，得到

\[
e_\lambda f(x)-f_*
\ge\inf_{t\ge0}\left\{g(t)+\frac{(D-t)_+^2}{2\lambda}\right\}
=:h_\lambda(D),\quad D=d(x,S).
\]

这只是 infimal convolution 的一维下 profile，未暗用 f 凸性或近端最小点存在；若包络值为−∞将与下有界假设矛盾。对径向精确模型 `f(z)=g(‖z‖)`、g 凸非减且 g(t)>0(t>0)，有 S={0}；此时该下界可达：取 z 在 x 的射线上且 ‖z‖=t≤D。若 g 可微且在正轴递增，最优 t 在适用的内部情形满足

\[
D=t+\lambda g'(t),\qquad
r_F(y)=g'(t),\qquad
\langle y,F(y)\rangle=tg'(t).
\]

因此方向、完整残差和原近端输出来自同一个 g；不是把残差界额外加进方向式。一般 g 不必预设为幂函数。对幂函数 `g(t)=c t^p/p, p>1`，关系是 `D=t+λc t^(p−1)`，p>2 的弱残差照样能点收敛。

本试验提供可理解的共同结构子模型，仍需扩展到非势、多值非径向、非孤立 S 和原一般 RL；不能以径向模型替换这些目标。


<a id="finite-window"></a>
## 试验 9：两条各自不稳定的合法分支在窗口中补偿



取 λ=1、y∈R²，

\[
B_1=\operatorname{diag}(-1/2,4),\quad
B_2=\operatorname{diag}(4,-1/2),\qquad
F(y)=\{B_1y,B_2y\},\quad S=\{0\}.
\]

每个输入有两支原根

\[
J_1=\operatorname{diag}(2,1/5),\qquad
J_2=\operatorname{diag}(1/5,2).
\]

完整纤维残差为

\[
r_F(y)=\min\{\|B_1y\|,\|B_2y\|\}\ge\tfrac12\|y\|.
\]

所以这里完整 F 甚至有全局线性次正则性。每一支 J_i 都有欧氏扩张方向，固定永远选择该支会产生发散轨道。但是选择原合法根的周期策略 J_1,J_2,J_1,J_2,... 给

\[
x^{2k}=(2/5)^k x^0,
\qquad
x^{2k+1}=J_1(2/5)^k x^0,
\]

故从每个初值至少存在一条收敛原 PPA 轨道。两步欧氏能量因子为4/25，而单步最大能量因子为4。

**范围与解释。** 这是同一个原 F 上的根选择，没有修改迭代。它显示“每步都支付亏损”并非存在一条收敛轨道的必要机制。法向空间乘上恒等的切向坐标即可得到非孤立零集版本。这个例子仍是线性分支与线性真残差，不覆盖原一般模；与旧 Stein 范数更换试验的区别，是在一个多值图中用两条各自不稳定的分支在时间上补偿，结论仅为存在策略，绝非所有根。


<a id="cone-variation"></a>
## 试验 10 / C379：有符号变差支付原空间位移



### 精确对象与结论

取 m≥1，原空间 R^m×R，点记为 (a,b)。取连续 g:R→R，满足 g(0)=0 且 bg(b)>0（b≠0）。不要求 g 单调。取 L≥0，给每个 b 一个非空集合 H(b)⊂R^m，且

\[
\|h\|\le L|g(b)|\qquad(h\in H(b)).
\]

定义完整算子和完整零集

\[
F(a,b)=\{(h,g(b)):h\in H(b)\},\qquad
S=R^m\times\{0\}.
\]

固定任意 λ>0。从每个初值出发，原 PPA 可无限续接；**每条**合法轨道均具有有限长度并收敛到 S，且

\[
\sum_{k\ge0}\|x^{k+1}-x^k\|
\le\sqrt{1+L^2}\,|b_0|.
\]

### 原根存在和留域

法向原步是 b_k=b_{k+1}+λg(b_{k+1})。连续函数 q(b)=b+λg(b) 满足 q(b) 与 b 同号，且 |q(b)|≥|b|，因此 q 在两端趋于相应无穷，由中间值定理满射。对每个输入 b_k 可选法向根 b_{k+1}，再任取 h_{k+1}∈H(b_{k+1})，令 a_{k+1}=a_k−λh_{k+1}，即得到完整合法原根。

当 b_k≠0，任一法向根与 b_k 同号且 |b_{k+1}|<|b_k|；b_k=0 时只有 b_{k+1}=0 且 h=0。因此不会越过零集。全域对象无需额外局部留域条件。

### 收敛和长度，不调用 EB

固定一条轨道，b_k 同号单调，故有极限 ℓ。由连续性，b_k−b_{k+1}=λg(b_{k+1})→λg(ℓ)，左边趋0，故 g(ℓ)=0，ℓ=0。并且精确有

\[
λ\sum_k|g(b_{k+1})|
=\sum_k|b_k-b_{k+1}|=|b_0|.
\]

切向—法向锥约束给

\[
\|x^{k+1}-x^k\|
=λ\sqrt{\|h_{k+1}\|^2+|g(b_{k+1})|^2}
\le λ\sqrt{1+L^2}|g(b_{k+1})|.
\]

求和得到所述长度界，整列 Cauchy，极限为 (a_∞,0)∈S。这里多值根可以任意选择，纤维不需最小范数元达到。

### 完整残差与原 RL 校验

完整真残差是

\[
r_F(a,b)=\sqrt{|g(b)|^2+\inf_{h\in H(b)}\|h\|^2},
\]

所以 |g(b)|≤r_F(a,b)≤√(1+L²)|g(b)|，从未把某个所选 h 当成下确界。

若输入 x=(a_k,b_k)，其唯一最近点 p=(a_k,0)。输出 y=(a_{k+1},b_{k+1})，有

\[
2y-x-p=(-2λh_{k+1},2b_{k+1}-b_k).
\]

利用 |2b_{k+1}−b_k|≤|b_k|、λ‖h_{k+1}‖≤L|b_k−b_{k+1}|≤L|b_k|，得到完整原近端锚式

\[
\|2y-x-p\|\le\sqrt{1+4L^2}\,d(x,S).
\]

这验证了一个线性有效反射模；没有据此声称满足全对 RL 的任意版本。

### 任意平坦的正规尺度

例如 g(b)=sgn(b)e^{−1/b²}（b≠0），g(0)=0，H(b)={c g(b)}，其中 c∈R^m、‖c‖≤L。此时完整残差为 √(1+‖c‖²)e^{−1/b²}；任何指数 θ>0 的局部 Hölder EB |b|≤K r_F(a,b)^θ 都失败，因为 |b|e^{θ/b²}→∞。上面的有限长度证明依然成立。

这不等于不存在任何一般误差模：逆对数模当然可以存在。实际收获是证明完全不需要预先给定该模，而是由法向符号和切向锥直接支付长度。若选 c≠0，F 通常不是单调算子；允许非单调、非势、多值纤维和非孤立零集，但仍是明确的产品锥子类。

**下一缺口。** 将“有符号的一维法向总变差”推广到多维法向、有曲率零集和切向抵消。不能把此受限定理替代一般非线性 RL 目标，也不能据此宣布两个恢复已完成。主研究者需核对仓库是否已有同一锥机制，再决定它是继承、扩展还是新资产。


<a id="self-contracted"></a>
## 试验 11：未来点几何直接产生长度



取 proper、lsc、凸函数 f:R^n→R∪{+∞}，argmin f 非空，F=∂f，λ>0 固定。原 PPA 是唯一的完整次梯度近端，所有初值都有无限轨道。对 k≥0，写 v_{k+1}=(x^k−x^{k+1})/λ∈∂f(x^{k+1})。

近端最小化给 f(x^{k+1})≤f(x^k)（初值不在 dom f 时从 x¹ 开始）。对任何未来点 z=x^j，j≥k+1，凸次梯度式给

\[
\langle v_{k+1},z-x^{k+1}\rangle
\le f(z)-f(x^{k+1})\le0.
\]

该式也对所有未来线段上的 z 成立，因为它们属于当前凸次水平集。沿当前段 q(t)=x^{k+1}+t(x^k−x^{k+1})，0≤t≤1，有

\[
\frac d{dt}\|q(t)-z\|^2
=2\langle x^{k+1}-z,x^k-x^{k+1}\rangle
 +2t\|x^k-x^{k+1}\|^2\ge0.
\]

于是沿前进方向，距离任何未来曲线点都不增加；同一当前线段内的未来点由共线性直接处理，逐段拼接正是自收缩性。固定一个极小点 p，单调性给 ‖x^{k+1}−p‖≤‖x^k−p‖，所以折线有界。现在只调用上述文献 Theorem 3.3：折线长度有限。由此 x^k→x_*，实际图值 v_{k+1}→0；∂f 图闭给 x_*∈argmin f。

**可迁移动作。** 对每个未来点的方向估计生成几何长度界；这里没有先求残差下降速度，再把速度积分为长度。它是一个真正的“方向极好而不指定正则模”的端点范本。

**未完成处。** 两点单调性对未来点只给与未来图值的差分信息，不直接给上式。任意 maximal monotone F 不必是凸势次梯度，不能把本试验的有限长度结论扩到整个极大单调端点。一般 RL 若要沿此法深入，须找到替代凸次水平集的原图未来点几何。



<a id="self-contracted-tail-boundary"></a>
### C463：凸原近端的几何尾界与维数障碍

**身份与来源。** 这是上述试验的定量转接和边界补证，已经三席实际终稿复核，登记为 derived-checked；不认定公开新颖性。
文献事实只取 Daniilidis–David–Durand-Cartagena–Lemenant
[arXiv:1211.3227v1](https://arxiv.org/pdf/1211.3227) 的
§2 式(2.2)、Definition 2.1（印页5）、Definition 2.5（印页6）及
Theorem 3.3、式(3.5)（印页9）：曲线可不连续，其长度按总变差计；
有界自收缩曲线满足 \(\ell(\gamma)\le C_n W(K)\)，
\(K=\overline{\operatorname{conv}}\gamma(I)\)，\(W\) 为归一化平均宽度。
该定理的证明用未来凸包宽度差；本路线不用 DD2 的距离积分模板，
但不能称为排除一切势或望远镜机制。下面两部分为本库逐步重构。

**SC1 · 有限维合同。** 对每个 \(n\ge1\)、proper lsc 凸函数
\(f:\mathbb R^n\to(-\infty,+\infty]\)，固定
\(S=\operatorname{argmin}f\ne\varnothing\)、\(\lambda>0\)。
取完整 \(F=\partial f\) 和任意 \(x^0\in\mathbb R^n\) 的全部精确近端迭代。
每个子问题因 \(f\ge\min f\) 而强制，且强凸，故全域存在唯一
\[
x^{k+1}=\operatorname*{argmin}_z
 \{f(z)+\|z-x^k\|^2/(2\lambda)\},\qquad
v_{k+1}=(x^k-x^{k+1})/\lambda\in\partial f(x^{k+1}).
\tag{SC1}
\]
因此这里确为完整 resolvent，不是从驻点中挑一个好分支。
记 \(t_k=d(x^k,S)\)、\(s_k=\|x^{k+1}-x^k\|\)，
\(K_k=\overline{\operatorname{conv}}\{x^i:i\ge k\}\)。结论为
\[
\sum_{i\ge k}s_i\le C_n W(K_k)
 \le C_n\operatorname{diam}\{x^i:i\ge k\}\le2C_n t_k,\qquad
x^k\longrightarrow x_*\in S .
\tag{SC2}
\]
常数只依赖维数；没有假设 \(\psi\)、KL 或某个距离积分可积。
目标在此是完整极小点集，不能自动替换为它的真子集。

**SC2 · 到所有未来点的比较。** 对 \(j\ge i+1\)，
子梯度不等式及函数值下降给
\[
\langle x^i-x^{i+1},x^{i+1}-x^j\rangle
 \ge\lambda[f(x^{i+1})-f(x^j)]\ge0,
\quad
\|x^i-x^j\|^2\ge\|x^{i+1}-x^j\|^2+s_i^2.
\tag{SC3}
\]
从 i 累加到任意中间下标即得三点自收缩。
初点不在 \(\operatorname{dom}f\) 也不妨碍此式：比较的函数值均从 \(x^1\) 起有限。
同样对任意 \(p\in S\) 有
\(\|x^{i+1}-p\|^2+s_i^2\le\|x^i-p\|^2\)。
在尾起点取 \(p\in P_S(x^k)\)，全尾落在半径 \(t_k\) 的同一个球内。

现在直接取阶梯曲线 \(\gamma_k(u)=x^{k+\lfloor u\rfloor}\)，\(u\in[0,\infty)\)。
它满足原文的区间参数定义和三点不等式。任意有限剖分的跳跃由原步的
三角不等式控制，而整数剖分取回全部有限前缀，故其总变差恰为
\(\sum_{i\ge k}s_i\)。定理3.3遂给 SC2 的长度界：
每个方向的投影宽度不超过直径，闭凸包不增加直径。
这里无需从离散自收缩擅自推断任意插值自收缩。
有限长给点极限；固定 \(\lambda\) 给 \(v_{k+1}\to0\)，而对固定 \(p\in S\)
\[
0\le f(x^{k+1})-f(p)
 \le\langle v_{k+1},x^{k+1}-p\rangle\longrightarrow0 .
\]
由 lsc 得 \(x_*\in S\)。完整真残差还满足
\(\sum_{i\ge k}r_F(x^{i+1})\le\lambda^{-1}\sum_{i\ge k}s_i\)。
不导入旧稿 Theorem 4.17 的更宽表述；有界性已由本合同的非空极小集独立证明。

**SC3 · 比距离积分多用了什么。** SC3 比每边存在一个最近输入锚强：
它控制全部未来轨道点，来自同一个凸函数的次水平集结构。
[C456](../dd2/finite_length_countermodels.md#dd2-sharp-gauge-finite-length-pair)
的 \(f(x)=\|x\|^{m+1}/(m+1)\)、\(m\ge2\) 已给精确真模
\(\psi(\rho)=\rho^{1/m}\)：所有正可测有效实际步下界的默认积分发散，
真实尾仍恰为 \(t_k\)。故绕过积分模板具有实际收益；
该径向例本身仍有距离势 t，不能用它否定全部距离势。
任意单调原图、任意驻点分支或一般 Hilbert 空间不属于 SC1 的长度结论。

**SC4 · Hilbert 空间的完整凸反例。** 令 \(H=\ell^2\)，
\(A=\operatorname{diag}(2^{-j})_{j\ge1}\)，
\[
f(x)=\tfrac12\langle Ax,x\rangle
 =\tfrac12\sum_{j\ge1}2^{-j}x_j^2,\quad
F(x)=\partial f(x)=\{Ax\},\quad S=\{0\},\quad\lambda=1 .
\tag{SC4}
\]
A 有界、正、自伴且核为零；f 全域连续可微凸，零点和极小点都精确为0。
对每个 \(x\in\ell^2\)，令 \(q_j=(1+2^{-j})^{-1}\)、\(y_j=q_jx_j\)。
则 \(y\in\ell^2\)、\((I+A)y=x\)，且对每个 z，近端目标差恰为
\(\tfrac12\langle(I+A)(z-y),z-y\rangle\ge\tfrac12\|z-y\|^2\)。
所以完整近端在全域存在且唯一；不是形式坐标迭代。

取 \(x_j^0=1/j\)，则 \(x_j^k=q_j^k/j\)。逐坐标趋零及
\(|x_j^k|^2\le j^{-2}\) 的支配收敛给 \(x^k\to0\)。
但置 \(m_j=2^j\)，互不相交的时间块 \(m_j\le k<2m_j\) 满足
\[
\sum_{k=m_j}^{2m_j-1}\|x^{k+1}-x^k\|
 \ge \frac{q_j^{m_j}-q_j^{2m_j}}j
 =\frac{q_j^{m_j}(1-q_j^{m_j})}j
 \ge\frac1{2ej}.
\tag{SC5}
\]
末式来自 \(2\le(1+1/m_j)^{m_j}\le e\)；下界用二项式，
上界用 \(\log(1+u)\le u\)。对这些时间块求和，真实总长无限。
因此即使全域光滑凸二次、固定正步长、完整唯一近端、强点收敛和自收缩
都成立，仍不能删掉 SC1 的有限维前件。

此例不反驳带有零端消失原误差模的 DD2：固定 \(a>0\)，输出 \(ae_j\)
的真残差为 \(a2^{-j}\to0\)，而距离始终为 a；
其输入为 \((1+2^{-j})ae_j\)，取 \(a\le2R/3\) 即在整个 R 窗内。
故该完整 Hilbert 图没有这样的统一零端误差模。
要反驳“全锚 Fejér 加原零模就够有限长”，应使用 C456 的二维旋转，
而不能把本维数反例偷换到不同数据类。

<a id="majorant-original-step"></a>
## 试验 12：用线性端点余量支付非线性变化

这里是 R1 的自足有限维原步试验，不是直接导入 Newton 收敛定理。取单值原 F，在闭球 B̄(s,R) 连续，F(s)=0。设有实矩阵 B 和连续 E，使
\[
y+\lambda F(y)=s+B(y-s)+E(y),\quad E(s)=0,
\quad \|E(y)-E(z)\|\le\epsilon\|y-z\|.
\]
所有 y,z 都在该球。若 σ=σ_min(B)>1+ε，则对球内每个输入 x，原根在球内唯一，且
\[
\|y-s\|\le\frac1{\sigma-\epsilon}\|x-s\|.
\]
因此从球内每个初值存在留在球内、几何收敛到 s 的原 PPA 轨道。

证明：B 可逆，原根等价于
\[
y=s+B^{-1}(x-s-E(y)).
\]
右侧在球内的 Lipschitz 常数至多 ε/σ<1，范数距 s 至多 (R+εR)/σ<R。Banach 定理给球内唯一根。代回原式得 ‖x-s‖≥(σ−ε)‖y-s‖，故球内续接和所述收敛。没有假定域外无其他原根。□

同一原数据还能产生方向和完整残差的界：若 B=I+λA，F(y)=A(y-s)+N(y)，N(s)=0，Lip N≤ε/λ，则对球内两点
\[
\langle y-z,F(y)-F(z)\rangle
\ge\left[\lambda_{\min}\left(\frac{A+A^\top}2\right)-\frac\epsilon\lambda\right]\|y-z\|^2,
\]
而
\[
r_F(y)=\|F(y)\|\ge
\left(\sigma_{\min}(A)-\frac\epsilon\lambda\right)_+\|y-s\|.
\]
方向、逆幅度和原步可解性都由同一个线性化余量模型读出，判据只需矩阵和变化预算。σ>1+ε 越有余量，允许的非线性变化越大。它与已有 [C323](../../canonical/ppa_native_alignment_and_transverse_test.md#native-transverse) 的光滑局部端点检验有亲缘；此处补的是显式有限球、原根构造及稳健预算，不主张新颖性。

首个缺口是非孤立零集和真正非 Lipschitz 原图：这个受限试验不能用来线性化原一般 RL 后宣布覆盖。一般控制函数可以继续研究随尺度变化的余量，但要重新证明自映射、原根和留域，不是把 ε 改成函数就完成了。

<a id="pro-workbench"></a>
## 给 Pro 的逐项深试入口

赞成先积累技术，再逐项充分尝试。深试时应以“要补哪条数学联系”分组，相关技术可以合用，不要求把同一家族的每个别名各做一篇相同报告。以下次序是阅读便利，不是唯一首攻或方法白名单。

| 深试组 | 起点与已接通的部分 | 接下来必须实际证明什么 | 验证成本与边界 |
|---|---|---|---|
| K 包络和完整纤维 | 试验1已有方向比较、一般模下剖面、值平移恢复及固定步长严格见证 | 找局部／最近零锚仍可用的比较，保留原 ω 与完整纤维；由同一包络给原根和点收敛，而非先假定已收缩 | 当前 K 是全图 inf，成本较高。优先寻找原数据的显式上下界；不默认全 λ 覆盖 |
| 端点与图修正 | 试验3–4分别给强逆侧收敛和非线性精确覆盖 | 在相同图关系中允许逆模退化而由方向接管；补非孤立目标，不额外强制连续选根 | 强逆版易查但范围窄；逐次图修正的单步费用须从原 F 产生 |
| 共同变分支撑 | 试验5–8已有增长支付负曲率、一般 profile 和图不变的文献范本 | 研究一般增长／曲率模，并寻找非势替代；若用凸化，证明保留原相关图点和完整小残差 | 显式势容易验证；未知势存在式可能很贵。强势子类不能替代一般目标 |
| 时间窗口与集合储能 | 试验9证明合法原分支可在两步补偿；D5记录落点而非只有距离 | 从原图提供可续接的窗口策略和廉价集合储能，避免把“未来会收敛”直接编码为条件 | 存在好轨道与所有根分别记录；中间输出须有留域证明 |
| 弱尺度耗散与未来几何 | 试验2、10–11不要求统一收缩率，可容纳极平坦残差 | 让整族亏损、未来点夹角或变差预算由一般原 RL 产生；在两种恢复中调用同一关系 | 任意慢模不等于任意一般 F；几何分解只作试验工具，不要求最终判据依赖未知投影场 |
| 线性化与积分覆盖 | 试验12、R2分别提供有限球余量和非统一条件数的覆盖线索 | 给一般非线性版本实际控制函数及覆盖证明；再检查方向与残差能否由其统一恢复 | R2仍只摘要层，先取得正文；Hλ 的正则性不能代替 F 的完整真次正则 |

每份深试报告先说一句实际结论，再写：确切对象与量词、文献原定理的条件、原步中的代入、承重推导、成功范围、首个未闭义务和下一种可试修改。一个技术第一次失败只限定已试的那一步；保留独立有用的公式，继续其他方向。计算不能替代证明。遇到仍有信息价值的具体缺口可以补搜，不以“已收集够多”为由禁用外部材料。

完整目标保持：同一个有独立含义的 M，在两组有意义的附加条件下分别恢复单调／次单调和一般真残差正则性，并由各纳入组合的原假设与参数导入 M，推出每个认证非解初值至少有一条可无限续接、点收敛的原 PPA 轨道。当前十二项初试没有合起来证明这件事。

## 来源和证据边界

技术表中的 URL 和位置是本批可追查的主要来源。正文中称自足证明的结论由原图、代数、有限维紧性或明确的基础定理重构，不以论文标题代替条件。四线材料已去重；不把检索数量当数学真值或新颖性。

- K 插值的文献承重点为 Chill–Sharma–Srivastava arXiv:2206.13400v1 Theorem4.1(a)，不是一个一般非单调 PPA 收敛定理。本页 Hilbert 常数、全对 RL 版本及真残差 profile 另有直接证明。
- 逆端点只调用强正则的“局部单值 Lipschitz 逆”含义，原 PPA 构造另证。普通次正则不能冒充具有同样扰动半径的强正则。
- 自收缩只使用有界曲线的 Theorem3.3 与凸原步几何。所核旧文 Theorem4.17 的宽泛表述不导入；这里明确要求 argmin 非空并先证明有界。一般极大单调 F 不自动是次梯度，也不自动获得该有限长度结论。
- 卡 F（一致定向）、D4（Matrosov）、R2（Hadamard–Lévy）本轮未核正文，只保存摘要级入口。D8 部分公式编码损坏，未逐式导入。其他卡的实际位置按表分别记录。
- I4 是原作者 HDR 中重印原论文的完整证明，不把非原作者综述当一手证据。Schilling–Wang arXiv:1105.3082 的 Bernstein 传递另定位，但会换算子，本轮不计入28卡或原 PPA 成果。

本页的数学推导状态仅按各段范围成立；公开首创性没有认证。完整 M 开放，技术储备和有限初试这一批工作已经形成可继续使用的报告。
