# 固定核一般模 GPPA：核心先行性逐定理反查

日期：2026-10-09 UTC。独立任务范围：C208–C217 中的核关系、一般模反射/真残差、标量收敛与物理提升。基线为 `5726c10083cb2dbaef52e2ec802d89c8fd9d39c1`；本记录不改 Claim 总账、不 commit/push。只使用仓库及公共一级来源，未检索 Library 或其它会话文件。

## 裁决

**不能认证全球首创；但本轮没有读到覆盖 C209 完整非线性模范围的一条先行定理。** 已有明确的无目标函数、非单调、真残差误差界、一般 gauge、可和尾及 warped resolvent 先例。因此这些词或机制单独不能作为创新点。最强反新颖性路线是把核关系看作普通 PPA，将反射条件转为 almost-firm 能量，并把输出真 EB 转为输入步残差 gauge 后对接 Luke–Thao–Tam / Luke–Tam。

这条路线在固定有限线性反射模下有精确桥。在真正非 Lipschitz 的完整 SF 见证上，源定理要求的**整零集邻管上有限 violation**失败；环域有限常数不修补该门。其失败只排除已核定理对**同一映射、同一坐标、同一域合同**的直接调用，不证明任何改写都不能导入，更不证明不存在其它先行框架。

最有希望仍需查证的精确命题是：任意 Hilbert 空间、完整 fixed-kernel union relation、一般连续反射模、完整真残差评价域下的 C209 三分支标量证书，尤其允许实际 resolvent 在零锚不 calm 的情形，加上 C210 的复合 Dini 物理长度接口。C214 的完整非幂模 spiral 锐边界则比“warp/一般 gauge”本身更有可识别性。这里的“有希望”是研究排序，不是新颖性判定。

## 实际阅读与来源

仓库实际读取：README 的 Research Goal、Definition Map、Claim Map/本轮入口；RESEARCH_STATE 全文；CLAIMS C208–C217；FAILED_ROUTES F55–F58；`generalized_ppa_modulus.md` 全文；`gppa_nonlinear_kernel_theorem.md` NGK1–11 全文。另读取本轮既有 priority audit 作为检索线索，未把它当作外文定理证明。

下表“页”均为本次下载 PDF 的一基页号；需要时括注印刷页。可公开复核的正文 URL 是主证据，web refs 仅保留本轮检索路由。

| 一级来源/版本 | 实际读到的位置与可确认事实 | 未读/不可调用范围 |
|---|---|---|
| Li–Mordukhovich, *Hölder Metric Subregularity with Applications to Proximal Point Method*, 作者修订稿 [PDF](https://web.maths.unsw.edu.au/~gyli/papers/lm-subreg12final.pdf), web `turn1view3` / `turn2view5` | §7，T7.2、证明中的 (7.7)–(7.8) 与残差平方递推，PDF26–27；T7.3，PDF28–29（印27–28）。对象为极大单调 Hilbert PPA；q-subregular 真残差已用于多项式/线性零集距离率。 | §1–6 的 coderivative 充分条件未重审；未从它推导一般非单调反射模、物理 warp 或有限长度原文结论。 |
| Luke–Thao–Tam, [1605.05725v2](https://arxiv.org/pdf/1605.05725v2), 2017-03-25；无版本 URL 本轮实际返回 v2，web `turn2view0` | Def2.3、Prop2.4，PDF5–6；T2.15/证明与 C2.16，PDF11–13；Def2.17、T2.18、C2.19，PDF14–16。无目标函数 almost-averaged + functional gauge；输出为零集距离进展。Def2.3 的 violation 为 ε∈[0,1)。 | 应用 §3 未逐项重审；不能把本文视为 arbitrary infinite violation / 一般 ω 定理。没有假称已核后续 journal 版本全部编号。 |
| Li–Mordukhovich–Zhu, [2406.13207v1](https://arxiv.org/html/2406.13207v1), [PDF](https://arxiv.org/pdf/2406.13207v1), web `turn1view0` | Def3.1及非幂例3.3，PDF3–4；BA H0–H3、L4.1–4.2，PDF7–8；T4.3及证明 PDF8–10；T4.4、Remark4.5、例4.6 PDF10–11。其目标是有限维 objective/subdifferential；一般模与可和 surrogate 尾已有先例。 | §5–9 未完整重审；T4.3 要 bounded level set 和 asymptotically shrinking 的统一比率门，不能替换成任意逐初值可和尾。 |
| Le–Théra, [2408.09139v1](https://arxiv.org/html/2408.09139v1), [PDF](https://arxiv.org/pdf/2408.09139v1), web `turn1view1` | Def1–2 与 §4 T11、L12–13、T14及相邻证明，PDF4、10–12。T11为极大单调算子+global inverse R-Lipschitz；T14为凸 subdifferential+一般 R-continuity，给选中残差/步长及集合距离率。 | §3 的全部 R-continuity calculus 未重审；T14不能删除 subdifferential/凸性，T11不是一般非单调定理。 |
| Bùi–Combettes, [1908.07077](https://arxiv.org/pdf/1908.07077), [作者版本](https://buinhutminh.github.io/papers/jmaa1.pdf), web `turn7view6` | Def1.1，PDF1；P3.8–3.10，PDF5–7；T4.2/证明、Remark4.3–4.4，PDF9–10；T4.8/证明，PDF12–13。kernel、coverage、warped inclusion、uniform continuity/strong monotonicity 输出已有精确先例。 | §5 复杂 splitting 应用未逐条重审。T4.2/4.8采用极大单调原 M 与外逼近更新，不能把 warped output y_n 自动认成下一原物理迭代 x_{n+1}。 |
| Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, 2025, [publisher HTML](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863), [PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863), web `turn53view1` / `turn59view2` | §2 Def1/Assumption1；§3 P3–4；§4 L1、L2、Assumption2、T2及证明，PDF5、9–12。原非单调 PPA、原算子真 residual EB、局部 coverage、自映射/留域与任意合法局部选择的 R-linear 点收敛均已存在。 | §3 所有 hypomonotone/comonotone 例子的参数未独立全复算；没有将 T2 扩大为一般 nonlinear gauge T2。 |
| Lauster–Luke, 2021, [publisher](https://link.springer.com/article/10.1186/s13663-021-00698-0), [PDF](https://fixedpointtheoryandalgorithms.springeropen.com/counter/pdf/10.1186/s13663-021-00698-0.pdf), web `turn53view0` / `turn55view2` | Def13、Def15、(18)–(19)、T16、L17及证明，PDF8–12。一般 summable gauge monotonicity、无目标函数、点收敛与显式尾和已存在。L17证明的步界与(18)(iii)直接给有限长度；不是把陈述的point结论误当长度。仍要求固定有限 almost α-firm violation、compactness 门。 | T25 应用未逐条重审；不能删除 almost-firm 或 bounded compactness。 |
| Bërdëllima–Lauster–Luke, *α-Firmly nonexpansive operators on metric spaces*, [publisher](https://link.springer.com/article/10.1007/s11784-021-00919-4), web `turn53view2` / `turn55view5` | 本次只浏览 T30 陈述和 proof 开头的 gauge/step-residual 识别。 | 全文、前置 standing assumptions 未重审；只作为明确下一文献门，不承担完整导入判断。 |

七份 PDF 与提取文本仅用于临时阅读，不随本报告发布；公式有限检查脚本见 [core_prior_art_check.py](../../code/gppa_novelty/core_prior_art_check.py)。来源的实际字节 SHA-256 为：LM2012 `d04141ba3f8e0e239ea53443f03a1c5690745a35b9719bb3f91893b62b35f01f`；LTT-v2 `e7c92b857fddcbbe08818c4a77379bd092e2e24294741ad0bb630656b7a49fa8`；LMZ-v1 `617600f7d27a1fb35d6b4ace5d9ce0f91cc780dbd1cd5758f495cdbb9ff6b820`；Le–Théra-v1 `75101f40771b675f14bdfd428a6809a9601cf7352626dc5b53729c74f273b5fe`；Bùi–Combettes `1f54b61d7f6e510ab3d7d9af1bc94e2a6ed58db74d2b6091e770fc4ef4b2d1cb`。工具抓取/传输失败只是一条获取记录，没有数学排除力。

补充下载SHA-256：Luke–Tam2025 `be07710dc13e8dcf6d19de36cb8a450a53df64f528dc7e5a232f8a9768cb4583`；Lauster–Luke2021 `8ba347f5ed1fd2078dea376933e69a75c70e270677a85f956b5cac10babb8603`。第三方全文只作临时核查证据，不随研究资产发布。

## 已闭的最强残差桥：输出真 EB 到输入步残差

以下是本轮独立推导，不冒称来源原文含同一 nonlinear 公式。设 C209 的合法步为 y=Tz、s=||z−y||，并已由该定理打开 s/λ≤t̄ 的评价域。则

\[
d(z,Z)\le s+d(y,Z)\le s+\psi(r_A(y))\le s+\psi(s/\lambda)=:h(s).
\]

h 在 [0,λt̄] 连续严格增加、h(0)=0；故 s≥h^{-1}(d(z,Z))。在合法窗口外可线性续接 h 成为连续严格增且无界的 LT gauge；续接本身不给域外 EB。

若还核 `Fix T∩Λ` 与 Z 的同一目标/保距离身份，且 T:Λ→Λ，则 Φ=T−Id 满足 LT 意义的 input step-residual gauge EB，μ=h。C209允许 Z⊂zerA、coverage只在Q∩U；因此**保目标距离、自映射、共同有效域仍须独立列出**。不能只用这一式自动导入整条源定理。

当 ψ(t)=Kt，h(s)=(1+K/λ)s，恰为 Luke–Tam2025 L1 的线性 bridge 机制；source T2并非没有原算子真残差。故“我们的 residual在输出、他们在输入”不是永久的创新边界。

## 线性反射模的精确重合与门

核图两点写成 Δy、λΔf，输入差 Δz=Δy+λΔf。C209 的平行四边形式为

\[
\|\Delta T\|^2+\|\Delta(I-T)\|^2
\le\frac{\|\Delta z\|^2+\omega(\|\Delta z\|)^2}{2}.
\]

若 ω(t)≤Lt，则 α=1/2、ε=max{0,(L²−1)/2} 给 LT Prop2.4 的同形 almost-firm 不等式。LTT-v2 Def2.3 限 ε<1，所以 **L<√3** 才自动落在该原定义；L≥√3只有代数同形，不能称原文已准入。L<1取ε=0只是放松为非扩张反射，不保留较强常数。

Luke–Tam2025 P3 的 scaled-relation submonotonicity 常数可取 β=max{0,(L²−1)/4}，因为其平方能量常数为1+2β。若还取线性真EB ψ(t)=Kt，source的充分预算为

\[
\beta(1+K/\lambda)^2<1/2.
\]

maximal submonotonicity、local truncated coverage、self-mapping和共同target还须逐项核；C209不自动给全部。另一面，C209 inverse-energy 条件是

\[
\tfrac12(1+L^2)<1+(\lambda/K)^2.
\]

两者不是同一个参数预算。精确比较价值可能是较弱预算或完整域处理，而非首次出现非单调 PPA+真 EB。两不等式的推导只需上述平方能量与EB；它们不构成对全球文献的穷尽比较。

## γ<1/一般模：环域攻击能走多远

零锚输入距离 a=||z−p||>0 的形式 violation 为

\[
\varepsilon(a)=\max\{0,(\omega(a)^2/a^2-1)/2\}.
\]

对 r_-≤a≤r_+，连续ω确给有限 supremum。若 ω(a)=La^γ、γ<1，该证书的 supremum 在 a↓0 发散；**证书发散不代表实际T必定非calm**，宽松ω可能覆盖本来Lipschitz的T。

LTT-v2 T2.18(a)/C2.19(a)要求almost-averaged在整个 S_{θ^iδ}，而其 gauge/contractivity 条件(b)才在 annulus R_i。T2.15也要求O是S的邻域，并把(a)放在O∩Λ。因此仅在正环得到ε_i不能直接穿过源(a)；删去内管后加回S会丢掉源的邻域/relative-interior门。允许修改映射或重新证明环域版定理是另一任务，不能记成源原文直接包含。

实际非calm见证用 C215 的完整二维 SF，λ=1：

\[
F(\xi,y)=\{(-Ay^{\gamma/\nu},\ y^{1/\nu}-y),
(-Ay^{\gamma/\nu},\ -y^{1/\nu}-y)\},\quad y\ge0,
\]
\[
T(\xi,r)=(\xi+A|r|^\gamma,|r|^\nu),\quad
Z=\mathbb R\times\{0\},\quad\nu>1,\ 0<\gamma<1.
\]

取p=(ξ,0)、z=(ξ,r)、r>0，则

\[
\frac{\|Tz-p\|}{\|z-p\|}
=\frac{\sqrt{A^2r^{2\gamma}+r^{2\nu}}}{r}
\ge Ar^{\gamma-1}\longrightarrow\infty.
\]

任意固定α∈(0,1)、任何有限ε的almost-averaged均蕴含零锚 Lipschitz 上界，故失败；对每个包含该零锚的整邻管，改变有限ε_i或α_i也不能修补。全图真残差满足 r_F(ξ,y)≥Ay^{γ/ν}，所以 d(y,Z)≤A^{-ν/γ}r_F(ξ,y)^{ν/γ}；与此同时 C209 的direct小窗兼容成立。这明确隔开**已核有限violation母类**与至少一条本库原映射。

它不排除 C215 已有homeomorphism共轭，也不排除更一般的objective-free非calm文献。引入v为全域双Lipschitz非线性核的完整拉回，只保持这一固定核证书；不能由“非线性核”三个字重新制造创新。

## 其它反新颖性路径及未闭桥

| 本库部分 | 最强已确认先例/攻击 | 本轮仍未闭的精确门 |
|---|---|---|
| C208 kernel relation A(z)=∪_{v(x)=z}F(x) | warped inclusion先例和基本fiber-union坐标恒等式；任意固定核本质上是A上的普通PPA。 | 非单射完整物理纤维及真实r_A≤r_F的仔细账本可能有整理价值，不能独立标“首个warped理论”。 |
| C209 energy/anchor branches | LM2012 T7.2的残差平方递推；LT/Luke–Tam非单调平方能量；ASM锐因子是同前提初等强化。 | nonlinear ω允许的非calm原T、inverse端点/评价域、三上界择小与完整留域的统一定理，尚未读到同一或等价整体结果。 |
| C209 scalar envelope/Dini | Lauster–Luke2021 T16/L17已有一般summable gauge与tail率；LMZ T4.3已有surrogate可和留域。 | 源Lauster–Luke固定有限almost-firm与bounded compactness；LMZ objective/finite-dimensional/统一shrinking比率。不同门不能互补删除。 |
| C210 physical lifting | uniform-continuity inverse输送端点Cauchy、summable transformed steps输送长度，是一般度量推理；warped P3.10有核正则性先例。 | 与完整非单射政策、核zero-set不闭、相邻政策和端点政策的精确共同域合取需要另核；不把常规inverse推理单独称创新。 |
| C211 arbitrary Q-ν | LMZ Remark4.5的高阶subregular proximal结论已给超线性阶，不能用“ν>2”或“高于二次能量”攻击其它PPA框架。 | 该双支完整原图、指定物理误差的精确常数、任意无正则性配对核排除是特定构造命题；其全球先例仍未核。 |
| C212 monotone shell q>1/2 | 既有 monotone真EB和平方耗散已提供原材料；scalar sgn(x)|x|^p 的轨道有限长由单调标量望远镜，极弱novelty witness。 | shell全时间分割对一般Hilbert原PPA的 q>1/2有限长是否已在KL/Fejér先例中明确或等价出现，本轮尚未读到决定性源。 |
| C213 inexact convolution | 几何收缩+误差卷积、δ/(1−θ)稳态管是经典离散递推；warped可处理误差的思想已有。 | 真实kernel/physical模与定义域预算有组合价值；不能把卷积本身新命名。 |
| C214 sharp spiral / C215 reformulation | 各为明确构造，首创检索必须追构造/不变量而非只查GPPA标题。 | 本轮无同一完整spiral与a=2校准先例；也没有充分覆盖所有“twist inverse modulus/finite length”文献。 |
| C216 regularized constants / C217 | 此独立任务未重审源2608.01584 T4全部公式；既有canonical保持其精确身份。 | 不据这里的core检索认可C216全球新颖；C217改写族/目标/量词未冻结，不能判总体优越。 |

两个有用的严格区分：

1. LM2012固定步长距离上界 d_k=O(k^{-q/[2(1-q)]})若直接对距离求和，只在q>2/3认证有限长；C212 shell幂为2−1/q，q>1/2已可和。取q=3/5，两个幂分别为3/4与1/3。这显示shell并非只把该距离率相加；**不证明shell首次出现**。
2. LMZ T4.3的asymptotically shrinking为limsup_{s↓0}∑χ^j(s)/s<∞。以纯log包络B(t)=log(1/t)^{-a}、a>1、τ(t)=e^{-c}t作比较，诱导χ(s)=(s^{-1/a}+c)^{-a}。每个正初值的尾可和，但积分下界给∑χ^j(s)/s≥s^{-1/a}/[c(a−1)]→∞。因此C209允许的逐初值log-Dini可和性不能自动调用该统一比率门。这只否定这条自然代换；其它ξ/objective/auxiliary序列仍待构造，不能称任何LMZ表示均失败。

Lauster–Luke的有限长度位置须精确说：T16/L17陈述为点收敛与尾率；L17正文给出
\[
d(x^k,x^{k+1})\le
\left(\frac{2\bar\alpha(1+\epsilon)}{c(1-\bar\alpha)}\right)^{1/p}\theta^{(k)}(t_0).
\]
(18)(iii)把右端相加即有限长。该步界没有objective；它正面覆盖“线性step-to-distance + 任意summable distance gauge”的机制。它的bounded-compactness门不影响这个代数长度估计；任意Hilbert/不取到最近点的本库处理可能是技术修补，不能仅靠这一差异认定创新。其固定有限almost-firm步界又确实不能用于上述实际非calm SF原映射。

## 检索合同与可复算记录

搜索服务使用两系统在不同调用中交叉搜索。检索式包括：

```text
Li Mordukhovich 2012 q-subregularity proximal point algorithm convergence rates PDF
Luke Thao Tam 1605.05725 quantitative convergence analysis expansive set-valued mappings
Li Mordukhovich Zhu 2406.13207 Le Thera 2408.09139
Bui Combettes Warped Proximal Iterations 2019 2020 pdf
"proximal point" "Dini" "error bound"
"almost averaged" "nonlinear" "convergence" gauge residual modulus
"proximal point" "Hölder" "nonmonotone" convergence reflected
"Fejer" "finite length" "error bound" nonlinear
"Dini" "proximal point"
"gauge monotonicity" Luke Thao
"finite length" "metric subregularity" monotone q
"nonlinear" "almost averaged" mapping convergence
"Generalized Monotonicity and the Proximal Point Algorithm" pdf Luke Tam
```

本轮primary正文之外命中的二手聚合只用于发现来源，不承担任何paper fact。有限检索不能证明未公开工作、非英文索引或其它等价框架不存在。

运行 `python research/code/gppa_novelty/core_prior_art_check.py`：Fraction验证L=3/2给ε=5/8、β=5/16，L=2给ε=3/2不落LTT-v2原定义；Decimal70位对A=1、γ=1/2、ν=3，r=10^{-2},10^{-4},10^{-8},10^{-12}输出anchor比约10、100、10⁴、10⁶，所需α=1/2 violation约200、2×10⁴、2×10⁸、2×10¹²；并核q=3/5和log比率下界。**这些有限值只佐证上述解析证明，不承担全称非calm或全球首创的证明。**

## 可直接用于下一轮的措辞

可用：已证明一个固定核、完整残差的条件统一定理；它含传统能量接口，并处理若干在原坐标零锚非calm、从而不能直接满足已核almost-averaged文献前件的完整关系。此次定向一级来源审查尚未找到覆盖其一般非幂模范围的同一或等价完整定理，全球先行性仍开放。

不可用：首次无目标函数非单调PPA、首次一般误差界、首次warped kernel、首次有限长度/尾和、首次超二次收敛；或者完整SF使任何合法改写均无法导入先前框架。最优先的后续是查非Lipschitz固定点模与KL/Fejér抽象有限长框架的等价桥，并分别检验C214的具体锐构造先例。
