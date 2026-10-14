# 原变量侧次单调性审查：定义、一般模与近端可解性的分界

日期：2026-10-14。范围：独立分报告，不修改主稿、CLAIMS、图或摘要。下列新推导仅在本报告中作局部身份登记；有限计算不代替全称证明。已读仓库 AGENTS、RESEARCH_PROTOCOL、academic-writing-skills 及 mathematics / mathematical-exposition。已核原模型为 `research/canonical/free_particle_rleb.md` 的完整自由粒子。

**判断。** 用户关于同名异义的怀疑正确；原变量次单调与 approximate convexity 的关系比 LT 条件具有更直接的函数结构解释。但“给这种次单调换一般函数模”已有明确先行，不能作为新概念卖点。更关键的是，它一般不控制 (I+\lambda F) 的抵消，不能单独产生完整近端覆盖、单值性或稳定性。值得保留的正路线是**二次正则化后的函数具有一般一致凸性**，等价地检查 (I+\lambda F) 的一致单调性；它确能在临界曲率处给非 Lipschitz 近端，却不覆盖本库非梯度自由粒子。因而本次证据支持把原变量结构作为可验证充分模块，并不支持用它整体取代 RL 与真误差界主线。

## 1. 实读一手文献与阅读边界

| 版本与 DOI | 本次实读内容 | 不作的推断 |
|---|---|---|
| Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, MOR Articles in Advance 2025, pp.1–13, [10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863), [出版社全文](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863) | §3开头、Definition 2、Propositions 3–4、Definition 3；作者明确说重新使用同名术语。P4在截断图自然输入域上表述，文中 almost-firm 参数要求 τ<1/2 | 不从名称或P4取得全输入覆盖；本分报告不复审其Theorem 2全部收敛证明 |
| Daniilidis–Georgiev, *Approximate convexity and submonotonicity*, JMAA291(2004),292–301, [10.1016/j.jmaa.2003.11.004](https://doi.org/10.1016/j.jmaa.2003.11.004), [作者12页全文](https://www.arisdaniilidis.at/DG_ac.pdf) | 作者稿p1式(1)、p2 Definition1、pp3–4 Theorem2/Corollary3；Definition7/Th13亦已定位 | 不将有限维 lower-C¹ 等价外推到所有Banach空间；作者稿页码不是刊本页码 |
| Spingarn 1981-06 作者研究报告，*Mathematical Programming with and without Differentiability*, [机构全文](https://repository.gatech.edu/server/api/core/bitstreams/d80188ab-cc04-4e34-8139-528b8e3052fd/content) | 物理pp16–17/印刷pp10–11已看扫描；strict submonotonicity、strict hypomonotonicity和全类极大性明确不同。印刷p15分别列出1981 TAMS和待刊mapping论文 | 此报告不是1982刊本。正式 *Submonotone mappings and the proximal point algorithm*, NFAO4(1982),123–150, [10.1080/01630568208816109](https://doi.org/10.1080/01630568208816109) 的公开PDF返回403；不导入其未读定理 |
| Poliquin–Rockafellar, *Prox-regular functions in variational analysis*, TAMS348(1996),1805–1838, [10.1090/S0002-9947-96-01544-9](https://doi.org/10.1090/S0002-9947-96-01544-9), [作者42页全文](https://sites.math.washington.edu/~rtr/papers/rtr157-ProxRegular.pdf) | Definition1.1、Definition3.1、Theorem3.2及相邻证明；Remark3.3、Proposition4.8。函数值敏感的图局部化不可省 | 不将单个(\(\bar x,\bar v\))处prox-regular直接改成整个输入邻域全部次梯度hypo |
| Daniilidis–Malick, *Filling the Gap Between Lower-C¹ and Lower-C² Functions*, JCA12(2)(2005),315–329, [现官方DOI10.68381/jca12022](https://doi.org/10.68381/jca12022), [刊本全文](https://journalofconvexanalysis.com/articles/jca12022/jca12022.pdf?v=2) | Definitions2.1/2.2/2.4、Theorems3.1–3.2，pp317–321 | α是正幂参数；不冒充本库RL指数。Def2.4正文将T的值写成∂f的值，按上下文是排印滑误；Th3.1实际仅对∂f使用 |
| Rolewicz, *On α(·)-monotone multifunctions and differentiability of γ-paraconvex functions*, Studia Math133(1)(1999),29–37, [10.4064/sm-133-1-29-37](https://doi.org/10.4064/sm-133-1-29-37), [出版社公开扫描](https://www.impan.pl/shop/en/publication/transaction/download/product/111120) | 印刷pp29–31已目读，式(1)–(7)、Proposition1；PDF为5个双页扫描，网页reader502但正常公开HTTP200 | 一般模原变量条件已存在；本次不审后续残余可微性定理 |
| Mokhtar-Kharroubi, *Characterizations and Classification of Paraconvex Multimaps*, Control and Cybernetics51(3)(2022),303–325, [10.2478/candc-2022-0019](https://doi.org/10.2478/candc-2022-0019), [公开刊本](https://bibliotekanauki.pl/articles/2183481.pdf) | pp304–305定义一般模paraconvex；§2.2 p315式(15)与pp315–316 Theorem3明列一般α(·)-hypomonotonicity | 仅引用该定义与已核(i)⇒(ii)⇒(iii)的相加证明，不整体认证所有后续分类结论 |
| Liu–Moursi–Vanderwerff, *Strongly nonexpansive mappings revisited: uniform monotonicity and operator splitting*, [arXiv2205.09040v1,2022-05-18](https://arxiv.org/pdf/2205.09040v1), 正式SIOPT33(4)(2023),2570–2597, [10.1137/22M1501696](https://doi.org/10.1137/22M1501696) | v1式(8)–(9)、Fact2.3、§3 standing assumption(14)、Theorem4.5及证明。全射和连续逆的结论保留**maximal monotonicity** standing assumption | 该文的A应对应本文的M=I+λF；不是说原F单调，也不是给任意图块全射 |

另检索到 Ngai–Penot 2007 *Approximately convex functions and approximately monotonic operators*, Nonlinear Analysis66,547–564；全文未成功取得，故不把其中定理作本次事实。Rolewicz1999已足以否定“一般模原变量次单调首次提出”的叙事。

## 2. 四种量词和三种同名对象

本节空间为实Hilbert空间；涉及DG函数等价时保留其原文空间条件。固定图点 \((x,u),(y,v)\)，写

\[
d=x-y,\quad e=u-v,\quad s=\|d\|,\quad q=d+\lambda e,\quad r=d-\lambda e.
\]

**DG / Spingarn的一阶strict条件。** 在给定输入点 \(\bar x\)，
\[
\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in B_\delta(\bar x)\ \forall u\in F(x),v\in F(y):\quad
\langle d,e\rangle\ge-\varepsilon\|d\|.\tag{DG}
\]
只要求两个输入趋近；**不要求输出共同趋向一个指定图值，不限制输出有界**。DG正文脚注明确其用法对应Spingarn的“strictly submonotone”。DG Theorem2把局部Lipschitz函数的该性质与近似凸性等价；有限维Corollary3再对应lower-C¹。它没有给PPA覆盖或收敛。

**Spingarn1981报告的strict hypo。** 对每个有界 \(K\subset\mathbb R^n\)，存在可依赖K的 \(k_K\ge0\)，使 \(F+k_KI\) 在K上单调。maximal表示整个strict-hypo类中的完整图包含极大；扩张可有另一组系数。它既不是DG的一阶小量，也不是固定σ的hypo极大性，更不是LT固定窗固定τ极大性。报告p11明确将近端单值的修正和小步长，与额外强正则性下的局部线性收敛分开；不能只留下“maximal”一词。

**LT尺度化条件。** 对固定图块 \(\mathcal G=\operatorname{gph}F\cap(U\times W)\)，对其**全部图点对**要求
\[
\lambda\langle d,e\rangle\ge-\tau\|q\|^2.\tag{LT}
\]
这对应Definition2对 \(\lambda F\) 和图值窗 \(\lambda W\) 的条件。它的预算来自Minty输入差，不是原变量差。由
\[
\|r\|^2=\|q\|^2-4\lambda\langle d,e\rangle\tag{I}
\]
可逆地得到 \(\|r\|\le\sqrt{1+4\tau}\|q\|\)。等价只在同一对族成立。若另限 \(\|q\|\le R\)，所得是受限对族性质；不是自动满足原文全部图点对。

**Prox-regular局部化。** 作者定义同时截取x邻域、v邻域及f值邻域。Theorem3.2(b)还要求锚v是proximal subgradient，然后相应f-attentive localization加 \(rI\) 单调。函数值局部化在subdifferential continuity等另外条件下才可去掉。既不能把有限图值窗误读为DG的全部输出，也不能用任意一个零锚代替完整图窗。

## 3. 一般原变量模：已有对象与可核桥

固定图块及原变量尺度 \(0\le s\le a\)，最自然的候选是
\[
\langle d,e\rangle\ge-H(s),\qquad H(0)=0,\quad H\ge0.\tag{PH}
\]
Rolewicz1999在 \(H(s)/s\to0\) 下给出一般 \(\alpha(\cdot)\)-monotonicity；取其测试函数族 \(\Phi=X^*\)，式(3)即(PH)。其式(2)的一般模支撑不等式相加，得到Prop1的 \(2H\) 预算。2022刊本式(15)更直接使用“α(·)-hypomonotone”名称。常数和模函数命名不是新概念。

若 \(H(s)=\sigma s^{1+\alpha}\), \(0<\alpha\le1\)，正是DM2005 Definition2.4的局部量级；Th3.1/3.2把它与α弱凸、lower-C¹,α等价。\(\alpha=1\)是二次hypo。对于 \(0<\alpha<1\)，缺陷虽是o(s)，却比s²更大；这正是二次近端核不能自动压住的量级。

**自含原函数解释，PR-PH-v1（derived-checked）。** 在凸邻域V中设
\(f(x)=\max_{i\in I}g_i(x)\)，I紧、g和梯度联合连续；设全部相关梯度满足
\(\|\nabla g_i(x)-\nabla g_i(y)\|\le\omega(\|x-y\|)\)，其中ω非降、连续、ω(0)=0。
令 \(A(x)=\operatorname{co}\{\nabla g_i(x):g_i(x)=f(x)\}\)。则
\[
f(y)\ge f(x)+\langle u,y-x\rangle-\int_0^{\|y-x\|}\omega(t)\,dt\quad(u\in A(x)),
\]
进而
\[
\langle x-y,u-v\rangle\ge-2\int_0^{\|x-y\|}\omega(t)\,dt.\tag{PH-model}
\]
证明：对x处每个active i，沿线段积分 \(g_i(y)-g_i(x)-\langle\nabla g_i(x),y-x\rangle\)，绝对值不超过积分预算；以 \(f(y)\ge g_i(y)\) 再取凸组合，交换x,y相加。该最大值模型的Clarke次梯度身份亦在DM Th3.2证明中明确调用。ω(t)=Ct^α给预算 \(2C s^{1+\alpha}/(1+\alpha)\)。这是真正原数据条件，但属于已知结构的直接定量化，不在此声称新颖。

**PH并不等价于RL。** 恒等式(I)只给
\[
\|r\|^2\le\|q\|^2+4\lambda H(s).
\]
右边还有未知输出差s。为了去掉它，必须有额外逆控制。仅用Cauchy–Schwarz可得
\[
\|q\|\ge s-\lambda H(s)/s\quad(s>0).\tag{Gap}
\]
若右侧能由正的严格递增函数m(s)下控，并且m(0)=0，就有 \(s\le m^{-1}(\|q\|)\)；这才给反射模。对于 \(H=\sigma s^2\)、\(\lambda\sigma<1\)，反射Lipschitz常数可取
\[
L=\frac{1+\lambda\sigma}{1-\lambda\sigma},\qquad
\tau=\frac{\lambda\sigma}{(1-\lambda\sigma)^2}.
\]
该推导是图块上的估计，仍不供覆盖。要直接落入LT P4的τ<1/2表述，还须 \(\lambda\sigma<2-\sqrt3\)；Definition2允许更大的有限τ。若 \(H=Cs^{1+\alpha}\)、\(\alpha<1\)，(Gap)右侧在任意小正s上为负，因此这条消元路径没有内容。

仅在单点成立的DG，其δ随ε及基点变化，不能不加说明地宣称在一个固定邻域上存在单一“仅依点距”的全对模。固定邻域上的均匀PH是明确的加强；紧性、全基点局部性质与适当有界性可另供统一化证明。

## 4. 同名概念不互相替代：完整反例

### 4.1 DG甚至strict maximal hypo，不保证任何零消失反射模

固定λ=1，完整 \(F(x)=-x\) 于R。它是C∞势函数 \(f=-x^2/2\) 的梯度，全域1-hypo，且对任意ε，取输入邻域直径≤ε即满足DG。它还是Spingarn报告意义的maximal strictly hypomonotone：若一个strict-hypo扩张在x₀多加u，则在有界小区间使用扩张自己的k，和原图点 \((x_0+th,-x_0-th)\) 比较，除以t并令t↓0，对h=±1推出u=−x₀。

然而 \(I+F\equiv0\)：\(J_F(0)=\mathbb R\)，\(J_F(z)=\varnothing\) 对z≠0。任意零点附近有限输出窗仍含一段完整纤维，所以连 \(\omega(0)=0\) 的RL都不可能。这同时否定“全类极大hypo自动补全range”的无步长版本。另若只检查任意图块，即使monotone也不保证覆盖：\(F(x)=0\) 于x>0而其余空，其自然输入域仅为(0,∞)。

### 4.2 LT有限τ也不保证DG的全输出量词

令 \(F(x)=1\) 当x<0，\(F(0)=\{-1,1\}\)，\(F(x)=-1\) 当x>0。取 \(U=[-\delta,\delta]\)，\(W=[-1,1]\)，0<δ<1；此图闭但在0处非凸值。相同支比较内积为0；跨支若s=|x−y|，则内积为−2s，Minty差模为2−s。因为0≤s≤2δ，
\[
2s/(2-s)^2\le\delta/(1-\delta)^2.
\]
故LT成立，δ=1/10时τ=10/81<1/2。可是比较x=t、y=−t，DG归一化内积恒为−2，故DG失败。该反例不冒充Spingarn1980稿声明的闭凸值类别；它只比较LT与DG2004给出的算子不等式。若W只保留一个分支，可把坏对删掉，但那已改变被比较对象。自然Minty输入域是分离的两块，不覆盖0邻域。

两例说明：脱离窗口、输出量词及步长，不能画一条“DG比LT更弱/更强”的总蕴含箭头。

## 5. 更有内容的正路线：正则化后的一致凸性

**PR-UM-v1（derived-checked，标准机制的独立推导）。** 设固定图块 \(\mathcal G\)，λ>0，m:[0,a]→[0,∞)连续严格递增、m(0)=0；要求图块输入坐标x的投影直径≤a（全域版可令a=∞）。对图块全部图点对假设
\[
\langle d,d+\lambda e\rangle\ge s\,m(s).\tag{UM}
\]
则Minty变换在该图块上单射，且对自然输入域D上对应输出、输入差≤m(a)的点对有
\[
\|J_\mathcal G(z)-J_\mathcal G(w)\|\le m^{-1}(\|z-w\|),\qquad
\|R_\mathcal G(z)-R_\mathcal G(w)\|\le 2m^{-1}(\|z-w\|)+\|z-w\|.\tag{UM-R}
\]
当输入差超出m(a)时不调用该局部逆。证明：若s>0，Cauchy–Schwarz给 \(s\|q\|\ge s m(s)\)；q=0则s=0，从而e=0。第二式来自r=2d−q。**其结论只在D上；它不凭空产生D的覆盖。** 零锚版只能控制到锚，不能产生全对单值。

若 \(F=\nabla f\)，令 \(g_\lambda=f+\|x\|^2/(2\lambda)\)。原数据充分门为
\[
g_\lambda(y)\ge g_\lambda(x)+\langle\nabla g_\lambda(x),y-x\rangle+\Psi(\|y-x\|).
\]
交换相加得到(UM)，其中 \(s m(s)=2\lambda\Psi(s)\)。例如 \(\Psi(s)=c s^p\)、p>2给 \(J\) 的 \(1/(p-1)\) 阶模。若在整个Rⁿ上gλ为C¹，并且每个线性扰动 \(g_\lambda-\langle z,\cdot\rangle/\lambda\) 都强制趋∞，则连续强制函数取得最小点；其一阶条件给完整输入覆盖，(UM)保证唯一，故该最小点就是**完整**近端输出。对一般关系可另用已核的maximal uniform-monotone理论，但极大性不可删。

这种门更准确的解释是“临界二次负曲率被更高阶正恢复抵消”。它是作用在M=I+λF上的一致单调机制，不是任意小负缺陷模。Liu–Moursi–Vanderwerff已系统研究一般模一致单调及逆连续性；此处不能仅因接到RL就认定新定理。

### 完整成功模型及其失败边界

取λ=1，\(f(x)=-x^2/2+x^4/4\)，\(F=f'=-x+x^3\)。完整 \(I+F=x^3\) 是双射，
\[
J_F(z)=\{\operatorname{sgn}(z)|z|^{1/3}\},\quad R_F(z)=2\operatorname{sgn}(z)|z|^{1/3}-z.
\]
对所有x,y，
\[
(x-y)(x^3-y^3)=\tfrac14(x-y)^4+\tfrac34(x-y)^2(x+y)^2\ge\tfrac14|x-y|^4.
\]
因此m(s)=s³/4，\(J\) 全域1/3-Hölder，\(R\)有模 \(2(4t)^{1/3}+t\)，在有限输入对距尺度上可转纯1/3阶。正规化函数g=x⁴/4的所有线性扰动强制，因此覆盖亦有独立优化证明。势函数C∞、全域1-hypo、DG、prox-regular均成立；**更复杂的原变量负模不是产生非Lipschitz近端的必要条件**。

LT在任意0图邻域仍失败：取图点t与0，
\[
\frac{-\langle t,F(t)\rangle}{|t+F(t)|^2}=t^{-4}-t^{-2}\to\infty.
\]
所有图值与输入都趋0，故任何固定有限图值窗不能删除见证。反射对0比率为2t⁻²−1→∞，最大局部指数恰1/3。

完整零集S={−1,0,1}，真残差 \(r_F(x)=|x^3-x|\)。完整PPA唯一且
\[
x_k=\operatorname{sgn}(x_0)|x_0|^{3^{-k}}\quad(x_0\ne0),
\]
故趋sign(x₀)，x₀=0时恒零。轨道单调，**总长度恰为** \(|x_0-\operatorname{sgn}(x_0)|\)；没有选择或远支遗漏。

然而0是不可稳定吸引的驻点，任意正小初值最终离开0的小邻域。虽在|x|≤δ<1/2有 \(d(x,S)=|x|\le r_F(x)/(1-δ^2)\)，也不能由RL+这一EB断言局部收敛到0：近端一步使x变为x¹ᐟ³，距离反而增大。其λ=1为临界曲率；λ<1时近端恢复Lipschitz，λ>1时0输入的完整stationary resolvent已有三个输出。该模型证实逆模路线的结构价值，也明确它不是现成的PPA稳定性定理。

## 6. 对仓库原模型的最强解释与同家族反证

取完整族
\[
F_\Gamma(x,p)=(-h(p),\Gamma p),\qquad h(p)=\operatorname{sgn}(p)\sqrt{|p|}.
\]
由于 \(|h(p)-h(q)|\le\sqrt{2|p-q|}\)，在任意完整图点对上、记s为原变量距离，
\[
\langle\Delta(x,p),\Delta F_\Gamma\rangle
\ge-\sqrt2 s^{3/2}-\max\{0,-\Gamma\}s^2.\tag{FP-PH}
\]
所以Γ=15的主例不仅属于DG，而且有全图一般模hypo；它不属于任何有限二次hypo（取d=(t,t)，内积除以||d||²为 \(15/2-1/(2\sqrt t)\)）。Γ=15时M=I+F也**不是单调**：同一对上内积 \(17t^2-t^{3/2}<0\) 当0<t<1/289。故上一节一致单调路线无法解释该原模型的完整非Lipschitz近端；F的交叉依赖亦不具有欧氏梯度结构，不能把它误称lower-C¹函数的次梯度。

真正供应可解与稳定的是三角结构：若Γ≠−1，每个输入(a,b)的全部输出恰为
\[
p=b/(1+\Gamma),\qquad x=a+h(p).
\]
Γ=15给完整全空间唯一近端、p_k=16⁻ᵏp₀与可和位置增量；原文RL/真EB计算精确记录这种非Lipschitz耦合。

反之，Γ=−1/2仍满足(DG)、(FP-PH)，在s≤1时还与Γ=15共用 \(H(s)=(\sqrt2+1/2)s^{3/2}\)。同样完整全空间唯一近端，零集均为R×{0}，真残差满足
\[
r_{F_\Gamma}(x,p)^2=|p|+\Gamma^2p^2\ge|p|=d((x,p),S).
\]
但p_k=2ᵏp₀，对任何p₀≠0发散；也有完整反射局部Hölder估计，只是其常数与真EB不满足收敛兼容。Γ=−1更直接：b≠0无输出，b=0有任意p及相应x，故没有覆盖与单值。所有例均为完整原关系，不是任取坏支。

这些反证显示：原变量PH连同真EB也不能筛出阻尼的符号，更不能替代同窗、全输出、兼容和留域条件。原模型的强解释应优先写“三角耦合/阻尼→完整反演→反射模”，而不是只换一个泛化次单调名称。

## 7. 真值、价值、先行性分判

| 说法 | Truth | Value | Prior/Novelty |
|---|---|---|---|
| LT与DG/Spingarn同名不同定义 | 已核，量词和预算变量不同 | 必须在相关工作澄清 | LT原文本已明说 |
| PH为原函数的lower-C¹/一般凸性缺陷提供解释 | 在所列模型及量词下已证 | 可作为自然模型验证模块 | Rolewicz1999、DM2005等已有直接前驱 |
| PH自动给完整近端覆盖、单值、收敛 | 已反驳 | 不宜作为主线承重门 | 非新颖性问题，是数学错误 |
| 正则化后一般一致凸→非线性逆模→RL | 指定图和覆盖门下已证 | 对临界曲率的梯度模型有实际结构价值 | 标准一致单调/凸共轭机制；本轮无原创性认证 |
| 上述原变量路线比RL更本质，因此应整体替换现主线 | 未成立；原自由粒子阻断UM路线，PH过弱 | 更合理的是补充原数据判据、明示适用子类 | 不存在一个由当前证据支持的全类严格优越结论 |

## 8. 计算与交付核验

先运行算式、逆代入和轨道，再写全称证明；代码为 `research/code/submonotonicity_routes/primal_verify.py`，仅Python标准库，seed=20261014。运行命令：

```bash
python3 research/code/submonotonicity_routes/primal_verify.py
```

输出：1681个有理点对精确核四次恒等式；10000个四次逆代入最大误差3.56e−15；每个Γ的10000个三角逆代入误差≤2.23e−16；484个有理LT跳跃例点对通过；显示两类精确轨道与坏商增长。这些只验证所执行有限样本和实现；章节4–6的所有forall结论由所列解析证明提供。初次尝试sympy不可用后改用Fraction精确算式，无依赖安装。

有限范围回顾：定义、同名量词、原函数结构、双向非蕴含、一个完整成功模型、原族完整失败模型和先行性均已覆盖。Spingarn1982正式全文、Ngai–Penot2007全文仍未读；没有将这些未读内容导入。未作全库审计、全球优先权判断或主稿修改。没有commit/push。
