# 强弱补偿：技术筛选与原 PPA 初步试证

本轮任务是沿“方向条件变强时，正则性可以变弱”的现象找技术，并立即做初步推导。已有结构可以成为这里的 M；公开来源、数学作用和新颖性分别判断。本页保存可继续研究的公式及具体断点，不把初步试验当作完整共同结构。

本页在 2026-11-19 从仓库 `44d482b` 接续。两位研究者分别搜索控制补偿与对偶/畸变技术，主研究者核对原对象、重构推导并另做端点储能试验。以下小节的结论只按各自明写的范围成立。

## 首轮得到什么

本轮筛了 **25 个技术入口**，实际展开 **10 项证明试验**。这些入口有亲缘关系，并非 25 个独立理论；检索、摘要核对、正文核读与自足证明在下表分别标明。最有信息的三点是：

- 同一方向上的亏损与增益应保留实际配对；分别取最坏值，可能制造一个原图根本没有的坏组合。
- 在拟对称子类，跨位置方向条件经过畸变定理，确实会产生一般真残差模；不是把误差界另加进去。
- Carlier 型余项与交叉储能提供不同的接法：前者把原/逆信息和实际原弦放在同一个恒等式里，后者让方向补足同时产生残差下界。

这三点值得继续展开。它们目前分别有范围限制，不能合并宣布一般多值 M 已完成。完整目标不变；初试允许只接上一小步。

| 已有实际推导 | 此次接通什么 | 首个仍缺的环节 |
| --- | --- | --- |
| 试验一：联合方向与幅度 | 原步净收益，避免不同方向的最坏常数混配 | 从原一般模低成本生成联合可达集合 |
| 试验二：一般模截断优化 | 方向亏损给定时，正则尺度需要支付多少 | 两个输入为何受同一原图结构制约 |
| 试验三：拟对称 | 跨点方向→畸变→一般模残差→受限原 PPA | 允许一般零纤维与切向移动 |
| 试验四：Carlier 余项 | 原/逆 Bregman 差＋实际原步 | 非单调时有限、可控的接触亏损 |
| 试验五至六：交叉储能、端点 Stein | 同一储能提供方向补足、残差或原步稳定 | 一般非线性、多值与慢尺度 |
| 试验七至十 | 测试变换、尺度重配、小增益、跨步约束 | 逐项见正文，失败只限已试的那一步 |

## 共同对象及老师观察的精确位置

固定有限维欧氏空间、原多值关系 F、非空闭集 S⊆F⁻¹(0) 和 λ>0。原步为
\[
x=y+\lambda v,\qquad v\in F(y),\qquad
r_F(y)=\inf_{w\in F(y)}\|w\|.
\]
每次调用方向估计、误差界时都使用同一工作域。允许选根不改变完整真残差。局部输入覆盖、可续接和留域须另证。

对输入的最近点 p∈P_S(x)，有精确恒等式
\[
d(x,S)^2=\|y-p\|^2+2\lambda\langle y-p,v\rangle
                      +\lambda^2\|v\|^2.
\]
由于 \(\|y-p\|\ge d(y,S)\)，后两项的联合下界可以给距离下降。方向项可以支付亏损，图值平方项可以提供补偿。它们取自同一个实际图点，分别取两个最坏常数可能丢失这种关联。

上述恒等式本身是可用的结构素材。需要研究的是它承载的关系能否发展出两个恢复及原 PPA 定理；“恒等式已知”不构成否决理由。若改用输出最近点，只能得到到该固定点的距离式，不能把输入距离的方向不等式倒过来。

## 技术筛选：25 个入口，证据深度分别记录

以下两张表分别由两位研究者按一手来源整理。主研究者另核了支撑本报告核心结论的 DW shell、Carlier、拟对称、hypocoercivity、一般模小增益及储能资料；不把其余检索层项目写成已精读。

| 技术入口 | 实际核读与可迁移动作 | 本轮判断 |
|---|---|---|
| 1. 耗散性／储能与供给率 | Willems 1972 作者 PDF 已打开，但文本不能提取；仅出版摘要核实“互联约束＋储能相加”的机制。 | 用作发现语言；本轮不借其定理完成证明。 |
| 2. 无源性余量与亏损指标 | 后继文献及 singular-angle 原文 §6 核读。方向损失和幅度收益可放在同一个供给率中。 | 推进为下文一般模截断补偿式。 |
| 3. 非线性 ISS 小增益 | Jiang–Teel–Praly 1994 作者版本 Theorem 2.1，印刷 pp.99–100；同时看了 class-K 定义。 | 可以处理一般函数交换，不限常数乘积。原 RLEB 已有一个此类闭链，不能把该闭链说成新增。 |
| 4. SRG | Ryu–Hannah–Yin v4 Proposition 1、Theorems 3–4、§6 的逆 Lipschitz／次正则说明。 | 保存方向和幅度的联合几何，不先压成两个独立最坏常数。 |
| 5. Davis–Wielandt shell／联合数值域 | Liang–Zhao–Qiu arXiv:2404.05609v1 HTML §II-A、§III-A；其完整 shell 记录实部、虚部和输出平方范数。 | 试验一用其实投影构造原 PPA 的精确联合集合。 |
| 6. Mixed gain–phase | Baron-Prada–Anta–Padoan–Dörfler arXiv:2503.13367 Theorem 3、其邻近的混合条件讨论。 | 不能只说“方向弱则幅度强”；应保留两者是否能在同一图点同时发生。LTI 定理不能原样导入一般 F。 |
| 7. 非线性 singular angle／小角度 | Chen–Zhao–Khong arXiv:2109.01629v2 Theorem 6、§6、Theorem 22。 | 一个系统的角度余量可补另一系统亏损；需要稳定、因果、well-posed 的反馈结构，原 PPA 不自动满足。 |
| 8. IQC 与动态乘子 | Rantzer–Megretski 1997 Part IIa pp.1–2 的三步框架；Lessard–Recht–Packard arXiv:1408.3595 Theorem 4 后关于 hard／ρ-hard IQC 的讨论。 | 比逐步点态估计多保留跨时间信息。试验十实际展开相邻两步。 |
| 9. Zames–Falb 型乘子 | Heath–Carrasco–Altshuller arXiv:2009.09366 Theorem 1 周边与 §III；允许受单调上下界控制的多值非线性。 | 多值并非根本障碍；但其上下界结构并不由一般 RL 自动给出。 |
| 10. S-procedure／S-lemma | Pólik–Terlaky 作者版检索到论文及定理综述；未用其精确等价性。 | 把若干平方约束加权成一个证书；多约束情形一般不能随意声称无损。可作计算探索，不作数学真实性来源。 |
| 11. KYP／频域到储能 | Rantzer 原论文出版页，以及 Boyd 原作者书中 positive-real lemma 段落核读；未导入定理。 | 发现模式是把看似不同的频域限制变为同一储能不等式。原一般 F 没有给定有限维 LTI 实现，因此暂留工具箱。 |
| 12. Secant criterion／对角稳定 | Arcak–Sontag 2006 Theorem 1，印刷 p.1532；加权储能计算在 p.1533。 | 互联的相位和增益共同影响可接受阈值，胜过只看增益乘积。PPA 没有原生循环分块时不强行制造分块。 |


| 技术 | 原文核读位置与事实 | 本项目初筛 |
|---|---|---|
| 13. Young 函数/互补增长 | Bačák–Kohlenbach, arXiv:1709.04700v3，§1式(2)–(3)，§3 Theorem3.10：允许一般 Young 代价并定量给出近端映射的连续模 | 保留其“互补函数求最优代价”动作；论文更换近端代价，不能原封不动替换本项目原步 |
| 14. 一致凸性与对偶光滑性 | 同文§3 Theorems3.12–3.13列明幂型及一般复合的一致凸性；其证明讨论凸性—光滑性对偶 | 单势子类里真正把方向与逆尺度联系；本轮未得到任意多值RL导入 |
| 15. Fitzpatrick 全图间隙 | Bauschke–Wang–Yao arXiv:0802.1375，Definition1.1/Fact1.2：全图凸代表及反算子交换变量 | 已有C324，继承而不重发 |
| 16. 自共轭与 proximal average | 同文Fact1.5及引言：自共轭代表的接触图最大单调；两种构造有不同适用条件 | 可保留原/逆共同语言；直接强制凸代表接触即单调，不能照搬一般非单调RL |
| 17. Carlier 的 Fenchel–Young 余项 | Bauschke–Singh–Wang arXiv:2206.14872，式(6)、§2/§4：同一个gap直接下界原近端位移平方；§4 Theorem4.5研究对偶 | 进入试验四；比只比较两个切片多了实际原弦 |
| 18. 循环单调阶数与余项级数 | 同文§7、Corollary7.4：利用更高阶循环单调/Fitzpatrick函数强化为平方范数级数下界 | 可研究链式补偿；该文级数使用固定x及递推对偶锚，不是本项目原PPA轨道，不能直接搬来其可和性；任意RL也没有循环单调 |
| 19. Ekeland/strong slope | Azé–Corvellec 2004 Theorem2.1、Proposition3.1、Theorems5.1–5.2：斜率下界产生误差界，凸函数斜率等于最小次梯度范数 | 误差模可以从局部下降产生；尚须证明方向几何提供所需斜率，不能把该结论另行假设 |
| 20. EB–KL 的 moderate growth 转换 | Bolte–Nguyen–Peypouquet–Suter arXiv:1510.08234v3 Theorem5/Corollary6：适度增长下误差界转去奇异化不等式，极平坦时逆向可能失败 | 机制是对尺度函数求导；已知势子类支持，任意F缺统一能量与链式关系 |
| 21. hypocoercivity 交叉项 | Dolbeault–Mouhot–Schmeiser arXiv:1005.1495v1 §1.3、Theorem2：H1微观耗散、H2宏观控制、H3–H4兼容，通过修改能量闭合 | 进入试验五；应保留原离散步，不能由连续耗散自动推广 |
| 22. δ单调→拟对称畸变 | Kovalev–Maldonado–Wu arXiv:math/0611110v2 Definition1.2、Theorem1.3；刊本Theorem1.3：n≥2、非恒定、局部球内δ单调产生η拟对称 | 进入试验三；方向产生逆模的真正范本。需参考幅度校准；原条件单值单射，不能假装覆盖完整多值RL |



主研究者补充三项：

| 技术入口 | 原文依据与本轮动作 | 试验去向 |
| --- | --- | --- |
| 23. 实际端点 Stein/Lyapunov | 经典离散储能；本页给自足谱、级数和合同变换证明 | 试验六；保留大步长负方向 |
| 24. T-coercivity / inf–sup 测试变换 | Ciarlet–Jamelot arXiv:2410.14444v1 §2 Definition 1 / Theorem 1 | 试验七；同一方向测试给完整误差界，原步兼容仍缺 |
| 25. 供给函数重标度 | Sontag–Teel 1995 Theorems 1–2 / §II，W=ρ∘V；离散版本仅定位未核正文 | 试验八；直接证明离散版本的一个有限接口 |

## 试验一：保留方向与幅度的联合集合

### 线性、单零点版本——精确完成

设 F(y)=Ay，S={0}，A 为实 n×n 矩阵，λ>0。定义实联合数值集合

\[
\mathcal W(A)=\{(\langle u,Au\rangle,\|Au\|^2):\|u\|=1\}.
\]

它是复 Davis–Wielandt shell 的实投影类比；这里不借用复 shell 的任何凸性定理。对每个非零 y，令 u=y/||y||，则原输入 x=y+λAy 满足

\[
\frac{\|x\|^2}{\|y\|^2}
=1+2\lambda\langle u,Au\rangle+\lambda^2\|Au\|^2.
\]

所以原一步的欧氏距离严格收缩，具有统一因子 κ<1，当且仅当

\[
\inf_{(a,b)\in\mathcal W(A)}\{2\lambda a+\lambda^2b\}>0.
\]

严格正性使 I+λA 单射，有限维方阵遂可逆，coverage 在此线性版本自动成立。取 m 为上述净收益下确界，则 ||y||≤(1+m)^(-1/2)||x||，原 PPA 从所有初值线性收敛到0。

这里确实把同一图方向的方向项 a 与幅度项 b 放在一起；当 a 为负时，需要 b>−2a/λ。a 越不负，需要的 b 越小。此半平面是原步产生的，不是 Young 放缩参数产生的。

若分别取 μ=inf a、ν=inf b，再检查 2λμ+λ²ν>0，相当于用包含联合集合的矩形代替真实集合。这个替换可能严格损失信息：取 A=diag(−10,1)，λ=1：两端净收益为80和3，实际下确界为3>0；独立最坏数为 μ=−10、ν=1，合并得到−19，失败。原 PPA 却分别有因子 −1/9 与1/2。

**所得认识。** “最坏单调性”与“最坏正则性”可能出现在不同方向。真实补偿集合可以证明，而两个最坏常数的简单组合证明不了。这是 joint geometry 的实际价值。

**范围。** 此处没有一般非线性模，也没有非孤立 S。它是成功的精确线性试验；可作为 M 的一个模型截面，不能据此说完整 M 已完成。

### 一般闭 S 的原量词版本——代数完成，结构生成未完成

固定工作输入域 D 及非空允许原近端关系 \(\mathcal J(x)\subset J_{\lambda F}(x)\)。对合法原边 x=y+λv、y∈𝒥(x)，令 t=d(y,S)>0；取 p∈P_S(x)，注意是**输入 x 的最近点**。定义

\[
\gamma=\frac{\|y-p\|^2}{t^2},\quad
\alpha=\frac{\langle y-p,v\rangle}{t^2},\quad
\beta=\frac{\|v\|^2}{t^2}.
\]

令 \(\mathcal W_{F,\mathcal J,\lambda}(t)\) 为全部此类三元组的集合。则 γ≥1，并且逐边精确有

\[
\frac{d(x,S)^2}{d(y,S)^2}
=\gamma+2\lambda\alpha+\lambda^2\beta.
\]

故该集合不只记录零锚图值的方向与大小，还记录最近输入锚相对输出距离的几何差额 γ−1。丢掉此项、把 p 误换成输出最近点，会改变恒等式，不能这样做。

上述距离恒等式对相同合法边中的任意输入最近点成立。若证书只要求存在一个输入最近点，选择一个即可；左侧不依选择。不需要 S 凸。

它能精确描述一步强弱补偿，却还没有从容易验证的原始信息生成该联合集合的便宜方法；从它恢复一般两点单调性需要保留任意两图点的数据，而非只有零集锚。它与本库 C277／C285／angle.md 的联合图语法有重叠。这里的价值是找到外部成熟技术所保留的信息，以及在哪一步独立取最坏会损失补偿，不主张新颖性。

<a id="truncated-compensation"></a>
## 试验二：一般模的“截断补偿”精确计算

### 假设、计算与结论

沿用 F,S,λ,D,\(\mathcal J\)。在所用正输出距离区间上，a 为有限非负函数，χ 为有限正函数。设每条受检边 x=y+λv、\(y\in\mathcal J(x)\)、t=d(y,S)>0，有一个 p∈P_S(x) 满足

\[
\langle y-p,v\rangle\ge-a(t)\|v\|,
\qquad a(t)\ge0.
\]

这里 a(t) 是可按尺度变化的方向亏损；量词只约束相同原边和同一个输入最近锚。另设对**整个原 F 纤维**有

\[
r_F(y)\ge\chi(t)>0.
\]

χ 可以是一般正函数。原形式 d(y,S)≤ψ(r_F(y)) 若在所用域内成立，可在适用域内通过合适广义下逆导出该残差下界；本推导不把所选 ||v|| 当作完整 r_F。

设 s=||v||。由完整残差下界有 s≥χ(t)，展开原步且用 ||y−p||≥t 得

\[
d(x,S)^2\ge t^2+\lambda^2s^2-2\lambda a(t)s
\ge t^2+\Delta(t),
\]

其中一维最小化**精确**给出

\[
\begin{aligned}
\Delta(t)
&=\inf_{s\ge\chi(t)}\{\lambda^2s^2-2\lambda a(t)s\}\\
&=\big[\lambda\chi(t)-a(t)\big]_+^2-a(t)^2.
\end{aligned}
\]

因此当 a(t)>0 时，严格正收益的充分且对这个标量放松必要的门为

\[
\lambda\chi(t)>2a(t).
\]

a(t)=0 时，只要 χ(t)>0 就有 Δ(t)>0。a,χ 同时允许非线性，未固定成二次或线性误差界。

**真正的试证成果。** 若先把 s² 的收益与 s 的亏损分别作粗界，可能得到无界或者方向错误的估计；在正则性给出的下截断区间上直接最小化，能计算“多少残差幅度足以支付当前方向亏损”。这个一维 profile 可以进一步换成非线性代价 \(\ell_t(s)\)：只需研究 inf_{s≥χ(t)}[λ²s²−2λℓ_t(s)]，无需先猜统一幂次。

一个可直接读出的**幂尺度边界**是：若 a(t)=A t^p、χ(t)=c t^q，A,c>0，则局部门为 λc t^q>2A t^p。当 q<p 时，每个固定 λ>0 在足够小的尺度都满足；q=p 时需要 λc>2A；q>p 时该充分门在任意小邻域都不能统一成立。特别 p>q>1 时，χ(t)=c t^q 比线性残差下界弱，仍能由更小的负方向亏损支付。这是一般非线性模的实际补偿结论。后一句 q>p 只否定此标量充分证书，不能据此判原 PPA 不收敛。

### 原 PPA 尚缺什么

若一条轨道已无限存在，且 Δ 连续、在每个闭区间 [ε,R] 上有正下界，且每一步输出距离不超过 R，则上述距离下降式推出 d_k 递减且趋零。证明：d_k→l≥0；若 l>0，Δ(d_{k+1})有统一正下界，与 d_k²−d_{k+1}²→0 矛盾。

对非孤立 S，这只证明距离趋零。它没有控制沿 S 的漂移，也没有独立证明 coverage、留域或点收敛。因此本轮没有把这些结论补成未证明的定理。

### 原 RL 的导入义务

本库原 RL 锚式是相对**输入距离**的反射模：\(\|2y-x-p\|\le\omega(d(x,S))\)。它允许由输入距离计算步长预算；本试验的方向亏损式却要按输出距离 t 给方向亏损 a(t)。原 RL 加完整残差 EB 目前没有给出这样的便宜 a(t)，也不能先使用待证距离收缩反推 a，否则循环。故该技术的下一义务是：直接用原反射模和同一条边的可达关系，生成截断 profile，不提前独立截断输入和输出。它是一个明确任务，并非“非线性所以做不了”。


### 非二次亏损的同一优化动作

固定 S={0}，t=‖y‖、s=‖v‖，原步 x=y+λv。假设方向估计与完整残差下界为
\[
\langle y,v\rangle\ge m(t)-c t^\alpha\|v\|^\beta,
\qquad r_F(y)\ge\rho(t),
\qquad c>0,\ \alpha\ge0,\ 0<\beta<2.
\]
这里 m(t)≥0 是方向余量，ρ(t)>0 是在同一输出域内的完整残差下界。对每个实际 v∈F(y)，都有
\[
\|x\|^2\ge t^2+2\lambda m(t)
 +\min_{s\ge\rho(t)}\{\lambda^2s^2-2\lambda c t^\alpha s^\beta\}.
\]
直接求导，极小点及受限极小点分别是
\[
s_*=(c\beta t^\alpha/\lambda)^{1/(2-\beta)},\qquad
s_{\min}=\max\{\rho(t),s_*\}.
\]
当 ρ(t)≤s_* 时，最小值为
\[
-\frac{2-\beta}{\beta}\lambda^2
       (c\beta t^\alpha/\lambda)^{2/(2-\beta)};
\]
当 ρ(t)≥s_* 时，直接在 ρ(t) 处评价。因目标函数从 s_* 后严格增加，m=0 时该标量放松保证严格正收益恰需
\[
\rho(t)>(2c/\lambda)^{1/(2-\beta)}t^{\alpha/(2-\beta)}.
\]
m>0 可以进一步降低 ρ 的要求。这是所给标量包的精确优化，不是整个算子类的锐界；达到最小值的图值未必能由一个全局兼容的 F 实现。

**收获与缺口。** 已有非二次、一般模的可计算补偿曲线，适合比较技术究竟减少了多少幅度要求。方向估计与完整残差在这里仍是独立输入；下一步要寻找使它们受同一原图约束的跨位置机制。

<a id="distortion-residual"></a>
## 试验三：从三点相对畸变直接产生一般真残差模

暂限单值 G:Ω→ℝⁿ，Ω 是包含闭球 B̄(0,R) 的开集，G(0)=0。假设 G 在这个闭球上是 η-拟对称单射：η 是 [0,∞) 到自身的严格递增同胚，对三个不同点，像距离之比由原距离之比的 η 控制。若由所引 δ 单调定理供应这一性质，另要求 Ω 为凸域、n≥2、G 非恒定、0<δ≤1，以及 B̄(0,2R)⊂Ω，并且在 Ω 中对任意 y,z 有
\[
\langle G(y)-G(z),y-z\rangle
 \ge\delta\|G(y)-G(z)\|\|y-z\|,\qquad\delta>0.
\]
原文依据是 Kovalev–Maldonado–Wu Theorem 1.3；它引用更早的 Kovalev 结果。

取一个实际参考点 z，‖z‖=R，m=‖G(z)‖>0。对 0<‖y‖=t≤R，以 0 为三点比较的基点，得到
\[
\frac{m}{\|G(y)\|}\le\eta(R/t),\qquad
r_G(y)=\|G(y)\|\ge\rho(t):=\frac{m}{\eta(R/t)},\quad\rho(0):=0.
\]
y=z 时单独用 η(1)≥1 即可。ρ 是一般连续递增残差模，不要求幂型。绝对幅度来自一个非零参考值 m；把 G 整体乘任意小正数不改变角度，故无量纲角度不能独自决定绝对幅度。

再用 δ 单调给出的径向估计，对原步 x=y+λG(y) 有
\[
\|x\|^2\ge t^2+2\lambda\delta t\rho(t)+\lambda^2\rho(t)^2.
\]
这里的残差模从跨点方向经畸变定理产生，并未另列误差界。

若 G 全域连续、非恒定且 δ 单调，则 G 单调而零点唯一，I+λG 强单调；由 G(0)=0 有 ⟨y,y+λG(y)⟩≥‖y‖²。连续性、有限维强制增长与 Brouwer 定理给原根全域存在，强单调性给唯一。上式保证 ‖xᵏ‖ 递减且选中残差平方可和；有界轨道的每个聚点由连续性识别成唯一零点，因此整列趋零。局部版本只对认证闭球中的图点作上述推导，不预先断言完整原根必然留在该球。

还可得到一个明确的非孤立子类：取 F(z,y)=(0,G(y))，S=ℝᵐ×{0}。完整真残差仍为 ‖G(y)‖，z 沿原 PPA 不动，所以模与点收敛保持。这允许产品型非孤立目标，尚不涵盖一般弯曲零集、多值纤维或切向搬运。

**下一义务。** 研究允许零纤维的相对/商空间畸变，同时保留完整纤维下确界；任取单射分支后，不能把其残差当作 r_F。

<a id="carlier-original-step"></a>
## 试验四：同一个 Fenchel gap 的三项精确分解

设 f:ℝⁿ→(−∞,+∞] 为 proper、下半连续凸函数，λ>0，f(x)、f*(u) 有限。令
\[
y=\operatorname{prox}_{\lambda f}(x+\lambda u),\qquad
v=u+(x-y)/\lambda\in\partial f(y).
\]
两个带指定次梯度的 Bregman 差为
\[
\begin{aligned}
D_f(x,y;v)&=f(x)-f(y)-\langle v,x-y\rangle,\\
D_{f^*}(u,v;y)&=f^*(u)-f^*(v)-\langle y,u-v\rangle.
\end{aligned}
\]
由 Fenchel 等式 f(y)+f*(v)=⟨y,v⟩，直接展开得到
\[
f(x)+f^*(u)-\langle x,u\rangle
 =D_f(x,y;v)+D_{f^*}(u,v;y)+\frac{\|x-y\|^2}{\lambda}.
\]
三项非负；最后一项是实际原近端位移。u=0 时就是原次梯度 PPA。原侧、逆侧与实际原弦出现在同一个恒等式中。Carlier 余项的文献依据见 Bauschke–Singh–Wang 的式 (6)、§2、§4；本页精确分解另由代数重构。

对任意原关系 F，还可定义有符号全图量
\[
\Gamma_F(x,u)=\sup_{(z,w)\in\operatorname{gph}F}
                   \langle x-z,w-u\rangle.
\]
若存在原根 x=y+λ(v−u)，则竞争点 (y,v) 直接给 Γ_F(x,u)≥‖x−y‖²/λ，不需要单调性。但在原图上处处为零的性质恢复全对单调性，属于已有 C324 的资产。

**立即反测。** 在 ℝ 上取 F(y)=−by、b>0，即使 λb>2 使原 PPA 稳定，仍有 Γ_F(x,0)=sup_z(−bxz+bz²)=+∞。因此这个未惩罚全图量不提供有限证书；下一步可研究有限尺度接触亏损。

若直接强制凸 H≥⟨x,u⟩ 且全部原图点都接触等号，在任意两图点中点处应用凸性，就已强迫全对单调性，排掉所需非单调图。应研究有符号亏损怎样受控，或高阶链式余项怎样保留原弦。原文 Corollary 7.4 的平方和递推固定 x、更新对偶锚，并非本项目原 PPA，不能直接搬来其可和性。

<a id="cross-energy"></a>
## 试验五：交叉能量让未直接耗散方向获得控制

先在可完整计算的原场中试证。取
\[
F(y)=Ay,\qquad
A=\begin{pmatrix}0&-1\\1&a\end{pmatrix},\quad a>0,\quad S=\{0\}.
\]
欧氏对称部分 diag(0,a) 没有第一坐标的严格耗散。取含交叉项的显式矩阵
\[
P=\begin{pmatrix}1/a+a/2&1/2\\1/2&1/a\end{pmatrix}.
\]
主子式为正，det P=1/a²+1/4，直接相乘得 AᵀP+PA=I。于是对原步 x=y+λAy，
\[
\|x\|_P^2=\|y\|_P^2+\lambda\|y\|^2+\lambda^2\|Ay\|_P^2
\ge\left(1+\frac{\lambda}{\lambda_{\max}(P)}\right)\|y\|_P^2.
\]
这里 ‖y‖²_P=yᵀPy。det(I+λA)=1+aλ+λ²>0 给每个输入的唯一原根，所以上式证明任意 λ>0 的原 PPA 收敛。

同一矩阵关系还给
\[
\|y\|^2=2\langle Py,Ay\rangle
 \le2\|P\|\|y\|\|Ay\|,\qquad
r_F(y)\ge\frac{\|y\|}{2\|P\|}.
\]
方向补足与逆幅度从同一交叉能量产生，误差界没有另加。a→0 或 a→∞ 时，P 的量级变差，可量化统一尺度的退化。这是经典技术的明确迁移；与 DMS hypocoercivity 借交叉项传递耗散的动作相近，不将这个矩阵算例冒作该文定理的普遍导入。

其局限是连续 Lyapunov 的严格条件会错过负线性大步长稳定。下一项只检验实际端点，修复这个具体范围问题；两项技术的适用条件须区分。

<a id="endpoint-storage"></a>
## 试验六 / C373-v1 · 只在实际步端点寻找储能

**问题。** C370 的全分数弦条件会排除大步长下稳定的负线性图。若借用离散 Stein/Lyapunov 技术，只检查实际端点，能否修复这个具体问题？

**受限对象。** n≥1，A 为实 n×n 矩阵，F(y)={Ay}，S={0}，λ>0，先要求 I+λA 可逆。这里每个输入都有唯一原根，完整残差就是 \(\|Ay\|\)。

**精确结论。** 下列三项等价：

1. 对每个初值，唯一原 PPA 轨道趋于 0；
2. A 的每个复特征值 a 都满足 \(|1+\lambda a|>1\)；
3. 存在实对称 P≻0，使
\[
(I+\lambda A)^\top P(I+\lambda A)-P\succ0.
\]

这不是新发现的线性稳定性定理，而是已知技术在原步上的完整试证。

**证明。** 记 J=(I+λA)⁻¹，则原轨道是 Jᵏx⁰。有限维矩阵幂对全部初值趋零，当且仅当 J 的谱半径小于 1，这等价于第 2 项。若谱半径小于 1，级数
\[
P=\sum_{k=0}^{\infty}(J^\top)^kJ^k
\]
收敛且 P≻0，并满足 P−JᵀPJ=I。左右分别乘 (I+λA)ᵀ 和 I+λA，得到上述端点矩阵不等式。反之，该矩阵不等式 经 Jᵀ、J 合同变换给 P−JᵀPJ≻0；紧单位球上的严格余量给统一的 P-范数收缩，从而 Jᵏ→0。□

展开端点矩阵不等式，同一条件就是
\[
2\lambda\langle Py,Ay\rangle+\lambda^2\|Ay\|_P^2>0
\quad(y\ne0).
\]
这使方向亏损与图值增益保留在同一度量、同一端点中；改变的是证明使用的储能，原 PPA 没有改动。

**初试收获。** A=−aI、a>0 时，取 P=I，端点支付条件恰为 λa>2；小步长不稳定而大步长稳定被同一条件读出。全分数弦要求则会在任意小的分数步失败。

对非正规矩阵
\[
A=\begin{pmatrix}-1&K\\0&-1\end{pmatrix},\quad\lambda=3,
\quad
P=\frac13\begin{pmatrix}4&2K\\2K&4+5K^2\end{pmatrix},
\]
直接相乘得 P−JᵀPJ=I，且 det P=16(1+K²)/9>0。K=4 时欧氏一步可能放大，但这个显式 P 仍证明全部原轨道收敛。

**首个缺口。** 这里的严格正定全空间条件自动排除非零核，并给几何速度。它不能直接容纳一般非孤立零集、多值纤维及本库慢收敛原 RL；须研究商空间、状态变化储能或非二次端点代价。仅把端点支付条件命名为 M，并没有完成两个恢复。不能由本试验反推原连续场稳定。

**来源。** Stein/Lyapunov 判据属于经典线性理论；本页证明自足。Boyd–El Ghaoui–Feron–Balakrishnan 的 [LMI 专著](https://stanford.edu/~boyd/lmibook/lmibook.pdf)，§5.1 提供共同二次储能的体系及“单系统/一般包含族”范围区分。独立复核已确认上述合同变换、负线性门和严格条件的范围限制。

<a id="test-transform"></a>
## 试验七：T-coercivity 能把方向转成真误差界，但还须接原步

**可迁移技术。** T-coercivity 不强求直接用原方向测试，而寻找一个有界可逆的测试变换。Ciarlet–Jamelot 的 [2024 arXiv v1](https://arxiv.org/pdf/2410.14444)，§2 Definition 1 / Theorem 1 回顾它与线性变分问题适定性的关系；这篇论文不是该理论的首创来源。

**直接初试。** 在某一受检输出域内，假设有线性 T、常数 c>0，使每个 y∉S、每个 v∈F(y)，都能选 p∈P_S(y) 满足
\[
\langle v,T(y-p)\rangle\ge c\,d(y,S)^2.
\]
由 Cauchy–Schwarz，\(c d^2\le\|v\|\|T\|d\)。对完整纤维取下确界，严格得到
\[
d(y,S)\le\frac{\|T\|}{c}\,r_F(y).
\]
更一般地，若测试条件的右边是 \(d(y,S)\chi(d(y,S))\)，则 \(r_F(y)\ge\chi(d(y,S))/\|T\|\)。这里误差界确由同一方向测试推出，并未被独立假设。

**为什么暂时接不上。** 原平方恒等式使用 \(\langle y-p,v\rangle\)，而该测试条件使用变换后的方向。T=−I、F(y)=−y、S={0} 满足 c=1 的测试条件，但 λ=1/2 的原 PPA 是 xᵏ⁺¹=2xᵏ。因此该测试条件单独不能保证原步收敛。若把 F 改成 TF 再证明算法，已经换了原问题。

**保留范围。** 继续寻找 T 与原步端点储能之间的兼容关系；不把上述失败扩大成 T-coercivity 技术整体无用。可见的下一义务是将变换后的测试量合法放回原端点差，而不改算法。

<a id="supply-rescaling"></a>
## 试验八：改变供给函数，能调配尺度，不能凭空改变下降符号

**Paper fact。** Sontag–Teel，[Changing Supply Functions in Input/State Stable Systems](https://sontaglab.org/FTPDIR/tn950112.pdf)，1995，Theorems 1–2 通过 W=ρ∘V 改变供给对；自由度有明确的零附近或无穷远阶条件。原文是连续时间，不能直接当作离散 PPA 定理。

**原离散步的自足试验。** 若已知 V(x)−V(y)≥G(x,y)−L(x,y)≥0，而 ρ 是可微、递增凸函数，则
\[
\rho(V(x))-\rho(V(y))
\ge\rho'(V(y))\,[G(x,y)-L(x,y)].
\]
这是凸函数支撑不等式的直接结果。它可把已有下降换到一般模的尺度；若只有一个标量 V，ρ 递增也意味着差的符号完全不变。因此不能靠这种重标度把一个实际扩张步变成下降步。

**断点及保留。** 该技术在两种已识别的能量/观测之间调配亏损有用；先要找到两者对原图的独立意义，不能从一个已有收敛证书经重标度便宣布完成共同来源。Nešić–Teel 的 2001 离散版本已定位，但本轮未取得可核读正文；只保留为待核技术，不导入其定理。

<a id="nonlinear-small-gain"></a>
## 试验九：一般模小增益与加权合成

**Paper fact。** Dashkovskiy–Rüffer–Wirth，[arXiv:0901.1842v2](https://arxiv.org/html/0901.1842v2)，§5 Definition 8 / Theorems 9–10，在指定增益矩阵条件下构造满足 Γ(σ(r))<σ(r) 的路径，再用最大加权能量构造总 Lyapunov 函数。这里记录的是原文的连续时间系统结果，不省略它对子系统 Lyapunov 函数的假设。

**离散接口的初试。** 设两个已由原对象导出的非负观测 V₁,V₂ 对每条允许原步满足
\[
V_i(y)\le\max_j\gamma_{ij}(V_j(x)),\quad i=1,2,
\]
其中各 γ 单调，且有从 [0,∞) 到自身的连续严格递增同胚 σ₁,σ₂ 和连续非减 h，满足 h(0)=0、h(r)<r (r>0) 以及
\[
\gamma_{ij}(\sigma_j(r))\le\sigma_i(h(r))\quad(i,j=1,2).
\]
令 V(x)=maxᵢ σᵢ⁻¹(Vᵢ(x))。逐项代入立即得 V(y)≤h(V(x))。连续性使 h 的反复迭代趋零。这里没有调用连续时间链式法则。

**首个缺口。** 若两个观测只是把旧 RL 和 EB 各自改名，合成仍未增加两侧关系；需要从 F 的同一图关系实际构造两个相互约束的观测。即使 V→0，点收敛仍须零集识别、续接和切向位移控制。本试验只建立可复用的一般模合成接口。


### 对原 RLEB 的直接代入

这项试验核对成熟工具怎样接上我们现有成果。设 ω 是所用输入距离区间上的有限非负非减反射模，ω(0)=0；ψ 是所用完整残差区间上的非减误差模。假设同一工作域内完整残差已落入 ψ 的定义域，且以下实际步长上界也落在该域中。对原近端步及同一输入最近锚，要求

\[
\|2y-x-p\|\le\omega(d(x,S)).
\]

反三角／三角不等式给

\[
\lambda\|v\|=\|x-y\|
\le\frac{d(x,S)+\omega(d(x,S))}{2}.
\]

若完整真 EB 为 d(y,S)≤ψ(r_F(y))，ψ 非减，则

\[
d(y,S)\le
\psi\!\left(\frac{d(x,S)+\omega(d(x,S))}{2\lambda}\right).
\]

这正是非线性 gain composition，而非一定要用常数乘积。方向模变好，即 ω 变小，可以容许更大的 ψ；ψ 变小则可以容许更大的 ω。补偿边界在函数偏序上定义，不限 Hölder。

**结果。** 该技术成功解释当前理论为何出现强弱交换，并保留一般模；它没有自动增加两侧间的新约束。这个组合估计已在本库原主链里，不新增 Claim。若沿这个路线继续，信息价值应来自联合可达域或跨尺度约束，而非再证明一次组合小于恒等。

## 试验十：动态乘子究竟能从原 RL 读取什么

### 实际跨步公式

设已有两个连续原步

\[
x^k=x^{k+1}+\lambda v_k,\quad
x^{k+1}=x^{k+2}+\lambda v_{k+1},
\]

其中 v_k∈F(x^{k+1})、v_{k+1}∈F(x^{k+2})。对相邻这两个**原图点**若能用全对一般 RL

\[
\|(y-z)-\lambda(v-w)\|
\le\omega(\|(y-z)+\lambda(v-w)\|),
\]

则代入 y−z=λv_{k+1}，直接得到

\[
\lambda\|2v_{k+1}-v_k\|
\le\omega(\lambda\|v_k\|).
\]

这是真正跨步的数据，不能由两个独立零锚残差界直接读出。交叉项为相邻步图值的内积；平方展开为

\[
4\|v_{k+1}\|^2-4\langle v_{k+1},v_k\rangle
\le\frac{\omega(\lambda\|v_k\|)^2}{\lambda^2}-\|v_k\|^2.
\]

这可作为两抽头动态乘子的约束原料，而不是先给任意能量加交叉项。

若有全对 β-弱单调性，相同代入另得

\[
\langle v_k,v_{k+1}\rangle
\ge(1-\beta\lambda)\|v_{k+1}\|^2.
\]

β=0 时直接推出 ||v_{k+1}||≤||v_k||；这是实际可验证的符号交叉作用。这里仅展示继承的经典机制，不声称新。

### 首次尝试的断点

从相邻原图约束最粗直接读出

\[
\|v_{k+1}\|\le\frac12\left[\|v_k\|+
\frac{\omega(\lambda\|v_k\|)}{\lambda}\right].
\]

若 ω(s)=Ls^γ，0<γ<1，则充分小的 s 上 ω(s)>s，所以该上包络的右侧比当前步残差更大。这个动态约束本身不能证明残差衰减。不能把“记忆项出现了”当作已有稳定性。

另一方面，完整真残差 r_F(x^{k+1})可能严格小于所选 ||v_k||；原 EB 只给 d(x^{k+1},S)≤ψ(||v_k||)，并不允许反向用真残差替换相邻原图约束中的 v_k。若当前只有原 C02-v3 的锚式而没有相邻两图点的全对 RL，则相邻原图约束也不能自动使用。

**保留的信息。** 原全对 RL 确实提供跨步相位／幅度约束，动态乘子不是凭空加条件。下一次应把相邻约束的平方展开与距离状态、完整残差下界一起做联合可达分析，寻找能同时望远镜相消的项；当前上包络失败只排除了“仅用这个残差上包络”证明衰减，不排除其他动态乘子，更不排除共同 M。

## 接下来继续试什么

下面是依这批公式得到的具体问题，允许按信息价值更换，没有唯一首攻。

1. **联合补偿集合。** 将原反射模与完整残差限制放在同一输入—输出可达域内优化；先比较是否优于各自取最坏，再检验两个恢复。试验一与二已给计算接口。
2. **带零纤维的畸变。** 从试验三的产品型非孤立零集出发，尝试相对/商空间版本。首个义务是完整纤维残差，不是选中分支的残差。
3. **有限尺度的 Carlier 亏损。** 试验四的未惩罚全图 gap 对负线性图会无穷；尝试限制尺度或控制接触亏损，保留原步的余项，同时检查凸化是否丢失完整残差。
4. **原步的跨时间补偿。** 将试验十的相邻原图关系与距离状态同算，寻找能望远镜消去的交叉项。只读残差上包络在次线性 Hölder 模下失败，不能据此否定所有动态乘子。

本轮的报告任务已完成一批实际初试；寻找完整 M 的长期任务仍在继续。本页没有宣称搜尽技术，也没有将先前路线判为唯一出路。

## 一手来源、证据层级与核读范围

下面保留可复查的 URL 和具体位置。以“检索/摘要”为层级的项目尚不能用于导入定理；正文中的有限维初试有自足证明。原文中算法、递推与本项目原步不同处均须保留。

- Ryu–Hannah–Yin, *Scaled Relative Graphs*, v4: [原文](https://arxiv.org/pdf/1902.09788) 。核读 Proposition 1、Theorems 3–4、§6。支持 SRG 的联合几何、交并、平移逆运算及逆 Lipschitz／次正则区别，不支持完整 M 已被解决。
- Liang–Zhao–Qiu, *Feedback Stability Under Mixed Gain and Phase Uncertainty*, v1: [原文](https://arxiv.org/html/2404.05609v1) 。核读 §II-A、§III-A。支持用 DW shell 保留同方向增益与相位信息；本页试验一的实联合集合另行直接推导，未导入其复杂矩阵定理。
- Baron-Prada et al., *Mixed Small Gain and Phase Theorem*, v1: [原文](https://arxiv.org/pdf/2503.13367) 。核读 Theorem 3 及上下文。该结果对象是稳定 LTI 系统，不能说直接给一般非线性多值原 PPA 定理。
- Chen–Zhao–Khong, *The Singular Angle of Nonlinear Systems*, v2: [原文](https://arxiv.org/pdf/2109.01629) 。核读 Theorem 6（PDF p.5）、§6 与 Theorem 22。给定因果、稳定、well-posed 互联系统的小角度补偿，及乘子扩展。
- Jiang–Teel–Praly, *Small-Gain Theorem for ISS Systems and Applications*: [原文](https://web.ece.ucsb.edu/~teel/ECE236/jiang-teel-praly-1994) 。核读 Theorem 2.1，印刷 pp.99–100；class-K定义在 p.97。不要把其全部 detectability／observability 条件略去后直接导入。
- Rantzer–Megretski, *System Analysis via Integral Quadratic Constraints, Part II*: [原文](https://lucris.lub.lu.se/ws/files/4671110/8768760.pdf) 。核读 Part IIa pp.1–2，说明多值反馈、IQC 与 homotopy／well-posedness 门。
- Lessard–Recht–Packard, *Analysis and Design of Optimization Algorithms via IQCs*: [原文](https://arxiv.org/pdf/1408.3595) 。核读 Theorem 4 后 pp.10–11，特别是 hard IQC（ρ=1）只给有界、不能自动收敛的说明。
- Heath–Carrasco–Altshuller, *Multipliers for nonlinearities with monotone bounds*: [原文](https://arxiv.org/pdf/2009.09366) 。核读 Theorem 1 周边及 §III 的多值／上下界机制。
- Arcak–Sontag, *Diagonal stability...secant criterion*: [原文](https://www.sontaglab.org/FTPDIR/arcak_sontag_automatica06.pdf) 。核读 Theorem 1（p.1532）及储能相加计算（p.1533）。
- Quan–Bodard–Oikonomidis–Patrinos, *Scaled relative graphs for pairs of operators beyond classical monotonicity*, v2: [原文](https://arxiv.org/pdf/2511.20209) 。核读 Propositions III.1–III.3 与 transformed／warped resolvent。只保留未来技术入口。
- Willems, *Dissipative Dynamical Systems I*: [原文](https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Articles/JournalArticles/1972.1.pdf) 。作者 PDF 打开但没有可读文本，本轮仅出版摘要层，不报虚构页码。
- Pólik–Terlaky, *A Survey of the S-Lemma*: [原文](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/Mprime/pdf/Tamas/S-lemma_SIREV.pdf) 。仅检索层，未借定理。
- Rantzer, *On the KYP lemma*: [原文](<https://doi.org/10.1016/0167-6911(95)00063-1>) 。仅出版摘要层，未借定理。


- Bačák–Kohlenbach, On proximal mappings with Young functions in uniformly convex Banach spaces, arXiv:1709.04700v3, [原文](https://arxiv.org/pdf/1709.04700) 。
- Bauschke–Wang–Yao, Autoconjugate representers for linear monotone operators, arXiv:0802.1375v1, [原文](https://arxiv.org/pdf/0802.1375) 。
- Bauschke–Singh–Wang, On Carlier’s inequality, arXiv:2206.14872v1, [原文](https://arxiv.org/pdf/2206.14872) ；正式发表J.Convex Analysis30(2)(2023),499–514，[原文](https://journalofconvexanalysis.com/articles/jca30029/) 。Carlier原论文发表元数据核于 [原文](https://epubs.siam.org/doi/10.1137/22M150839X) ，未冒称已核其全文；公式细节用Bauschke等一手研究论文复核。
- Azé–Corvellec, Characterizations of error bounds for lower semicontinuous functions on metric spaces, ESAIM COCV10(2004),409–425，[原文](https://numdam.org/item/10.1051/cocv:2004013.pdf) 。
- Bolte–Nguyen–Peypouquet–Suter, From error bounds to the complexity of first-order descent methods for convex functions, arXiv:1510.08234v3, [原文](https://arxiv.org/pdf/1510.08234) 。
- Dolbeault–Mouhot–Schmeiser, Hypocoercivity for linear kinetic equations conserving mass, arXiv:1005.1495v1, [原文](https://arxiv.org/pdf/1005.1495) 。
- Kovalev–Maldonado–Wu, Doubling measures, monotonicity, and quasiconformality, arXiv:math/0611110v2, [原文](https://arxiv.org/pdf/math/0611110) ；刊本 [原文](https://www.math.ksu.edu/~dmaldona/papers/mathz.pdf) 。Theorem1.3的角度→拟对称结论在此文引用Kovalev前作，本文为核读载体而非首创归属。
- Kruger, Error bounds and metric subregularity, arXiv:1405.1130v1, [原文](https://arxiv.org/pdf/1405.1130) ，本轮只核定义和引言框架，未导入其未逐条核条件的定理。

- Ciarlet–Jamelot, *Explicit T-coercivity for the Stokes problem*, arXiv:2410.14444v1，§2 Definition 1 / Theorem 1，[原文](https://arxiv.org/pdf/2410.14444) 。本页只借测试变换的动作，方向测试到残差界为直接推导。
- Sontag–Teel, *Changing Supply Functions in Input/State Stable Systems*, 1995，Theorems 1–2 及 §II，[原文](https://sontaglab.org/FTPDIR/tn950112.pdf) 。连续时间供给变换有明确阶条件；本页不把它直接当离散算法定理。
- Dashkovskiy–Rüffer–Wirth, arXiv:0901.1842v2，§5 Definition 8 / Theorems 9–10，[原文](https://arxiv.org/html/0901.1842v2) 。原文的 Ω-path 与合成储能用于系统互联；本页离散接口另证。
- Boyd–El Ghaoui–Feron–Balakrishnan, *Linear Matrix Inequalities in System and Control Theory*, 1994，§5.1、§8，[原文](https://stanford.edu/~boyd/lmibook/lmibook.pdf) 。支持储能、S-procedure 与 IQC 的体系定位；C373 的离散结论由本页级数证明给出，不将书中连续公式冒作相同定理。
- Nešić–Teel, *Changing supply functions …: the discrete-time case*, IEEE TAC 46(6), 960–962 (2001)，[原文](https://ieeexplore.ieee.org/document/928607/) 。本轮仅元数据及摘要层；作者 PDF 被访问页拦截，未导入其正文定理。访问失败没有数学否定含义。

**有用的新文献接口。** Carlier 余项是本轮新定位的可迁移支线。Corollary 7.4 的平方和递推保持原 x 不动、更新对偶锚，不能直接认作本项目 PPA 轨道。拟对称原文 Theorem 1.3 引用了更早的 Kovalev 结果；不把本次核读载体当作首创者。本轮未认证任何全球新颖性。

**本页复核。** 主研究者重构了联合集合恒等式、截断最小化、非二次极小点、Fenchel 三项分解、拟对称三点估计、两份显式矩阵及相邻全对 RL 代入。另一位研究者独立重构了 C373；拟对称域边界已修成含闭球的开域。有限符号相乘仅核对矩阵实例，不代替一般证明。阅读顺序按“所得认识→共同对象→技术表→十项实际试证→下一义务”组织，重复的小增益条目合并为一项；源论文事实与本页推导分别标明。
