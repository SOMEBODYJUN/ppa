# GPPA 2608.01584v1 与 RLEB–PPA 的独立逐定理比较

**2026-10-09 接续审查修正范围。** 本文保留原ASM证明身份；[C204无正则性配对单调证明](pair_monotone_barrier.md)另关闭所述标量双支缺口。[C205–C207保零集删支证明](sol61_branch_restriction.md)已给指定原轨道的GPPA导入，所以本文完整图不涵盖不可解释成收敛无法借GPPA证明。当前裁决以[综合比较](COMPARISON.md)为准。

审查对象：Ba Khiet Le–Boris S. Mordukhovich–Michel A. Théra, *Convergence and Stability Analysis of a Generalized Proximal Point Algorithm and Its Inexact Version*, [arXiv:2608.01584](https://arxiv.org/abs/2608.01584)，v1 的 arXiv 首日为 2026-08-03，所存 PDF 首页另印 August 4, 2026。本文只审查仓库存档 v1，不推测后续版本。原件：[PDF](sources/gppa_2608.01584v1.pdf)。以下页码是 PDF 印刷页码，和文件页序一致。

本审查独立读取 README、RESEARCH_STATE、CLAIMS、FAILED_ROUTES 的相关身份与异议，以及 C02-v2、C09/C10/C11、C137、C141、C191–C193 的规范正文。数值与有限精确代数先用 [gppa_check.py](gppa_check.py) 复算，结果在 [gppa_check_results.json](gppa_check_results.json)；一般包含与排除由下文证明承担，计算不能替代这些证明。PDF pp. 5、7、9–11 已另渲染目读关键原式。

## 1. 审查结论及比较的对象合同

不能把这篇论文概括成“仅允许 identity kernel”，也不能宣称我们的非单调/非 calm 实例一概不在其范围。Theorem 2 真正允许任意定义在整个 Hilbert 空间上的非线性、非单射核；C191 的一个非单调、非 calm 的严格 RLEB 子类确实可以在**同一完整 F、同一物理普通 PPA 轨道**上满足它的全部条件，详见 §5。另有线性强单调子类连完整 resolvent 都相等。

但这并非完全重合。完整 cap 图 C137 有严格 RLEB 证书，并有一条普通 PPA 轨道不能被**任何** adaptive-strongly-monotone 核及任意正 GPPA 步长保持；证明使用完整两支，允许在 GPPA 内重新选另一图值，仍得矛盾，详见 §6。该排除也推广到 C141 的指定正法向轨道和 C10 的完整对数接缝，详见 §7。

Theorem 2 的无条件定量对象是核坐标及到完整零集的距离，而 C02-v2/C09 的对象是同一图块的物理点轨道及长度。非单射核下前者没有自动推出后者。另一方面，“有限长度”不能在已有物理点 R-linear 尾界时单独充当新增结论：它是三角不等式的直接推论。§4 给出精确边界。

严格区别以下四种关系：

1. **完整 resolvent 相等**：同一完整 F、同一物理变量，两个算法的全部纤维逐输入相等。
2. **同轨道包含**：同一完整 F，某条或全部普通 PPA 轨道是 GPPA 的合法选择，但 warped 纤维可能更大。§5 的非线性例属于这里。
3. **删支或换图**：保留一条轨道但改变完整 F，不能用于原图的类包含。§6 的排除恰依赖不可删去的另一支。
4. **升维、压缩、分裂或更换算子**：需要另证算法、零集、全部纤维及物理回代。这篇论文与本审查都未提供覆盖所有这种表示的总排除定理。

“同一 F 根本不存在合格 kernel”这个字面命题通常是假的：只要 zer F 非空，常量核 v≡c 对任意 ε>0 满足 adaptive strong monotonicity，且 ran v⊂ran(hF+v)，其 warped resolvent 是 zer F。这是一步跳入零集的另一算法。本文排除的精确命题是**保持明定非驻定普通 PPA 物理轨道的合格 kernel 不存在**。

## 2. 原文定义、量词、变量及算法

为防止原文步长 γ 与本库 RL 指数 γ 混淆，以下把原文 GPPA 步长记为 h>0，adaptive 常数记为 ε>0；本库普通 PPA 步长仍记 λ。

原文 p. 2 Eq. (5) 及 p. 5 Definition 4 定义

\[
x_{k+1}\in J^v_{hF}(x_k)=(hF+v)^{-1}(v(x_k)),
\qquad v(x_k)-v(x_{k+1})\in hF(x_{k+1}).
\tag{GR1}
\]

v:H→H 在整个 H 上单值，允许非线性、非单射；定义本身携带 ran v⊂ran(hF+v)。普通 PPA 是 v=Id 的特例。一般 kernel 下不能把核差换成 x_k−x_{k+1}，也不能把固定 warped 步长 h 自动视为普通步长 λ。

原文 p. 4 Definition 1 的 pair monotonicity，以及 p. 5 Definition 3 的 adaptive strong monotonicity，按集合值算子的标准 all-pairs 读法分别是

\[
\langle f-g,v(x)-v(y)\rangle\ge0,
\qquad
\langle f-g,v(x)-v(y)\rangle\ge\epsilon\|v(x)-v(y)\|^2
\tag{GR2}
\]

对全部 (x,f),(y,g)∈gph F 成立，包括完整纤维的不同分支，不只零锚或实际选中值。Definition 2 的传统 pair strong monotonicity 右端是 α||x−y||²，和 Definition 3 不是同一个前件。原文不存在核 inverse-Lipschitz、连续性或可逆性这一隐藏前件。

原文 p. 5 Definition 5 的 R-continuity 精确为：对某 σ>0、非减 ρ:[0,∞)→[0,∞)，ρ(0)=lim_{r↓0}ρ(r)=0，

\[
A(z)\subset A(\bar z)+\rho(\|z-\bar z\|)B
\quad(z\in B(\bar z,\sigma)).
\tag{GR3}
\]

R-Lipschitz 是 ρ(r)=Lr；R-Hölder 允许任意 θ>0，不是只 θ≤1。Definition 6, p. 6 的 compactly R-continuity 先与任意紧 K 相交，再可选 σ、ρ。在 Theorem 2 的 F⁻¹ 处，这意味着对**所有位置上的**小图值 f，完整逆点 x∈F⁻¹(f) 靠近完整零集 S=F⁻¹(0)，并非仅对近某个零点、某图块实际输出的 EB。Definition 5 只保证 ρ 在 0 右连续，没有保证在每个正点右连续。

数值距离 EB 与 (GR3) 的闭球集合包含也须区分：无限维非凸 S 不一定有最近点，d(x,S)≤ρ(||f||) 不总给实际的 S+ρB 表示。本库 C02-v2 取有限维闭 S，所以下述具体实例无此取到问题。残差 inf 及阈值边界同样需要门：由所有 ||f||<σ 的估计推真残差 EB 时，可安全缩为 r_F<σ；不能在 r_F=σ、inf 未取到时凭空使用窗口外图值。

## 3. 原文逐定理核验

| 原文位置 | 完整前件 | 实际结论与速率 | 对本库的精确关系 |
| --- | --- | --- | --- |
| Theorem 1，p. 6，引用 [13,14] | S=zer F 非空；完整 pair monotone；全输入 ran v⊂ran(hF+v)；完整 GPPA 选择 | (a)核步差→0；(b)另加 F 图 strong–weak closed 时，每个物理弱聚点在 S；(c)另加 F⁻¹ 在0 R-continuous 时 d(x_k,S)→0。没有点收敛、速率或物理长度结论 | 这是引用的定理，v非单射允许物理方向失控；和 C09 的 Dini 物理点结论不是同一个结果。全文未在此重证 [13,14] 的一般情形，本审查不将其所有历史变体升级为已核。 |
| Theorem 2(a)，pp. 7–8，Eq. (11) | 上述非空S与coverage；完整 pair ε-adaptively strongly monotone | 对每个 x*∈S，核误差平方因子≤(1+2hε)⁻¹，核步差平方由误差平方降幅控制；所以核误差和核步差 R-linear。没有物理范数误差声明 | 当 v=Id 时直接是点 R-linear，并自动有限长；非单射核下不自动转成物理点结论。§5有真实覆盖子类，§6有任意核同轨道排除。 |
| Theorem 2(b)，p. 7 statement/p. 8 proof | 2(a)前件，再加 F⁻¹ 在0 R-Lipschitz | 最终 d(x_{k+1},S)≤(L/h)||v(x_{k+1})−v(x_k)||，故集合距离 **R-linear 上界**。并未证明一步 Q-linear 距离比值 | 与 C02 的距离收缩有交集，量词/位置局部性不同；不能把 R-linear bound 说成每步 Q-linear。 |
| Remark 3，p. 8 | 物理序列有界且 H=Rⁿ | 可把 F⁻¹ R-Lipschitz 换成 compactly R-Lipschitz | 有限维有界序列闭包紧，选同一K即可；无限维有界不够。 |
| **Lemma 3**，pp. 8–9 | 完整 pair monotone；x₁∈zer F、x₂∈zer(F+εv) | ||v(x₂)||≤||v(x₁)|| | 原文没有“Theorem 3”；编号3是Lemma。证明完整、只用这两个图值。取所有x₁后得||v(x₂)||≤inf_{S}||v||，不需要inf取到。 |
| Theorem 4，pp. 9–11，Eq. (12) | 完整 pair monotone；v全局L-Lipschitz；zer F及zer(F+εv)非空；ε充分小；F⁻¹在0R-continuous；对 **F+εv** 的完整warped IGPPA有无限合法轨道；物理加性误差||y_k||≤δ=ε² | 固定ε只控制 limsup d(x_k,S)≤ε²+ρ(B_ε)，B_ε=(Lε²+4Lε/h)/h+ε(2Lε/h+a)，a=inf_S||v||；对一族ε问题，lim_{ε→0}limsup_k d(x_k,S)=0 | 不是同一未正则化普通PPA的精确点收敛，也不是一条ε_k→0轨道。它新增了允许不消失的均匀误差这一稳定性范围，本库列举的精确C02/C09等不包含它。 |

### 3.1 Theorem 2 的证明及可直接推得的更强核因子

令 c=v(x*)、z_k=v(x_k)−c。普通 all-pairs ASM 作用于实际选中值 f_{k+1}=(v(x_k)−v(x_{k+1}))/h 与零锚，给

\[
\langle z_k-z_{k+1},z_{k+1}\rangle\ge h\epsilon\|z_{k+1}\|^2.
\tag{GR4}
\]

极化恒等式给原文

\[
(1+2h\epsilon)\|z_{k+1}\|^2
\le\|z_k\|^2-\|v(x_{k+1})-v(x_k)\|^2.
\tag{GR5}
\]

原文这一推导成立；其中把恒等式写为一次“≤”是排版宽松，不构成数学问题。令 r=(1+2hε)⁻¹/²，则 ||z_k||≤r^k||z₀||、核步差≤r^k||z₀||。2(b)应用 R-Lipschitz 的 σ 窗须在选中值范数最终小于σ之后，GR5已保证这一点；早期项不影响R-linear渐近上界。

同一个 GR4 还由 Cauchy 给

\[
(1+h\epsilon)\|z_{k+1}\|^2
\le\langle z_k,z_{k+1}\rangle
\le\|z_k\|\|z_{k+1}\|,
\quad
\|z_{k+1}\|\le q\|z_k\|,
\quad q=(1+h\epsilon)^{-1}.
\tag{GR6}
\]

这里“更强”只指原证明已有前件下一个更小的核上界，不是本库先行性主张。它也便于补齐Theorem 4的两个小证明门。

另外，S内取两个零图值给 ε||v(x*)−v(y*)||²≤0，所以核在**全部完整零集**上取同一个c。多物理解在核下可以全部重合。

### 3.2 Theorem 4 原证明中的边界与可核修补

原文 p. 10 取 u_k=x_k−y_k，u_{k+1}∈J^v_{h(F+εv)}(x_k)，并取 κ=(1+2hε)⁻¹/²。正则化确实使 (F+εv,v) ε-adaptively strongly monotone；这是完整图all-pairs的逐值恒等式。核递推为

\[
A_{k+1}\le\kappa(A_k+L\delta),
\qquad A_k=\|v(u_k)-v(x^*)\|,
\quad x^*\in\operatorname{zer}(F+\epsilon v).
\tag{GR7}
\]

需明确的门如下。

* 原文 p. 10 的 κ/(1−κ)≤2/(hε) 等价于 hε≤4，因为该比值=(sqrt(1+2hε)+1)/(2hε)。在固定h、ε“充分小”的陈述中可补成 hε≤4，不是致命反例，也不是其一般算法失效。
* y₀未定义却使用u₀；设y₀=0或从k=1开始递推即可，无实质障碍。
* p. 11 对 F⁻¹ 使用R-continuity须最终保证实际残差在σ内；ε充分小使B_ε→0可补此门。
* p. 11 由有限时 ρ(B_ε+o(1)) 直接得到limsup≤ρ(B_ε)，若只按Definition 5读，正点右连续没有被假设。单纯引用“ρ非减”不足以证明这一步。但是结论可以用原有前件修补，无需新增右连续假设：把GR7的κ换成GR6的q，有
  \[
  \limsup A_k\le\frac{L\delta}{h\epsilon}=\frac{L\epsilon}{h}.
  \tag{GR8}
  \]
  Lemma3给||v(x*)||≤a，所以选中原算子图值
  \[
  f_{k+1}=\frac{v(x_k)-v(u_{k+1})}{h}-\epsilon v(u_{k+1})\in F(u_{k+1})
  \]
  满足
  \[
  \limsup\|f_{k+1}\|
  \le \widehat B_\epsilon
  :=\frac{L\epsilon^2+2L\epsilon/h}{h}
       +\epsilon(L\epsilon/h+a)
  <B_\epsilon.
  \tag{GR9}
  \]
  L>0、h,ε>0保证严格裕度。因此最终||f_{k+1}||≤B_ε<σ，直接用ρ非减即可得原印界ε²+ρ(B_ε)。ρ在0的连续性再给双极限0。这里没有从一个可能跳跃的正点取ρ右极限。
  若允许L=0，v恒等于某c，a=||c||。此时正则化warped更新直接给u_{k+1}∈F⁻¹(−εc)，实际残差正好εa；ε充分小后直接应用Definition5，得到d(x_{k+1},S)≤ε²+ρ(εa)，也就是原印B_ε=εa的界。此退化边界不需要严格裕度。
* warped resolvent的coverage是Definition4隐含条件；若“let a sequence be generated”只解释为已存在无限轨道，则定理可按轨道条件读。若要保证每个初值皆可无限迭代，须显式检查 ran v⊂ran(h(F+εv)+v)。零集非空本身不提供该全输入coverage。

因此这些是需要说明的证明/存在量词门，不足以宣称Theorem4的稳定性结论整体错误。原文也没有承诺物理范数收敛、有限长度或一个固定ε的误差趋零；不能因这些缺席把其正确距离稳定性结论说成失败。

## 4. 点收敛、物理长度与先行性边界

非单射核允许失控的物理选择：取H=R²、完整F(x₁,x₂)=v(x₁,x₂)=(x₁,0)，h=ε=1。完整pair是1-adaptive、ran v=ran(F+v)，F⁻¹全局R-Lipschitz常数1。完整GPPA纤维为 {x₁/2}×R，故

\[
x_k=(2^{-k},(-1)^k)
\tag{GR10}
\]

是合法轨道。它到S={0}×R距离Q因子1/2，核范数误差也Q因子1/2，却不点收敛且每步物理长度至少2。这个初等证明重建了C197/F49边界；不反驳原文只声明的核和距离结论，更不排除另一合格核/选择条件能控制物理方向。

若某算法已给物理点尾界 ||x_k−x∞||≤Mq^k，0<q<1，则

\[
\sum_{j\ge k}\|x_{j+1}-x_j\|
\le\sum_{j\ge k}(Mq^{j+1}+Mq^j)
=\frac{M(1+q)}{1-q}q^k.
\tag{GR11}
\]

所以“R-linear **物理范数** ⇒ 有限长度”无需新算法定理。当v=Id时Theorem2已给这一结论；任意核若另有可达轨道上的inverse-Hölder控制||x_k−x∞||≤C||v(x_k)−c||^θ，也立刻给物理R-linear尾和有限长度。不能把所有kernel-coordinate线性收敛误说成已有这一逆控制。

C02-v2 的幂次物理尾同样R-linear，有限长度不应在既有物理范数R-linear定理已覆盖的子类单独作为创新点。C09的Dini一般模可以有非几何物理尾，C10明确显示距离Q-linear与物理长度之间的缺口；这构成不同的定理内容，但不是全球新颖性结论。

## 5. 真实重合：完整F、同一普通PPA物理轨道可代入Theorem2

### 5.1 完整纤维也相等的简单子类

取F(x)=ax，a>0，λa=1，H=Rⁿ。普通完整J_{λF}=I/2、Cayley反射为0。RL可取L=0、任意0<γ≤1；真EB为d(x,{0})=r_F(x)/a，C02直接兼容因子1/2，全输入coverage、完整纤维、零锚及U=H留域均成立。外部取v=Id、h=λ，pair adaptive常数a，F⁻¹全局R-Lipschitz1/a，两个完整resolvent完全相等，Theorem2覆盖同一物理点R-linear结论，有限长度随之而来。这已足以否定“所有核心收敛结论均避开GPPA”的过宽表述。

### 5.2 非单调、非 calm 且带任意非单射核的非平凡子类

取C191的原数据m=r=1、D={0}、b f=c>0、C=R₊、M=a>0。完整关系是

\[
F(t,y)=\{(-c y^\alpha,ay+n):n\in N_{\mathbb R_+}(y)\}\quad(y\ge0),
\qquad F(t,y)=\varnothing\quad(y<0),
\quad0<\alpha<1.
\tag{GR12}
\]

这里完整边界纤维为F(t,0)={0}×(−∞,0]，不能只取n=0。零集S=R×{0}。令q=(1+λa)⁻¹；普通全部完整近端纤维唯一：

\[
T(t,y)=\bigl(t+\lambda c(qy_+)^\alpha,qy_+\bigr).
\tag{GR13}
\]

**严格RLEB的全部门。** C191的SN8/SN9取d_D=R_D=f，得到在输入对尺度R上的完整all-pairs RL

\[
L_R=R^{1-\alpha}+2\lambda c q^\alpha,
\qquad \psi(s)=(s/c)^{1/\alpha}.
\]

真残差不小于c y^α，故此gauge对完整inf成立；普通完整J全输入唯一，最近零锚为(t,0)，U=R²。直接兼容商

\[
\kappa_R=\left(q^\alpha+\frac{R^{1-\alpha}}{\lambda c}\right)^{1/\alpha}<1
\quad\text{只须 }R^{1-\alpha}<\lambda c(1-q^\alpha).
\tag{GR14}
\]

gauge可取全域，或选bar t≥(R+L_R R^α)/(2λ)。留域预算右边是∞；全部输出位于完整图，未遗漏边界支。

**合格的非线性、非单射核。** 对任意外部步长h>0取

\[
w=h/\lambda,
\qquad u=\frac{h c q^\alpha}{1-q^\alpha}>0,
\qquad v(t,y)=(-u(y_+)^\alpha,w y_+).
\tag{GR15}
\]

完整pair adaptive可取ε=min(c/u,a/w)>0。若y,z>0，逐值计算

\[
\langle F(t,y)-F(s,z),v(t,y)-v(s,z)\rangle
=cu(y^\alpha-z^\alpha)^2+aw(y-z)^2
\ge\epsilon\|v(t,y)-v(s,z)\|^2.
\tag{GR16}
\]

若z=0、完整边界值n≤0，正常项改成(ay−n)wy≥aw y²；两边均在边界则核差0。域外F空，不增加不等式义务。由此没有删掉完整法锥纤维。

全部warped纤维可精确求出：

\[
J^v_{hF}(t,y)=\mathbb R\times\{qy_+\}.
\tag{GR17}
\]

对y_+>0，正常方程w y_+=(ha+w)z先给z=q y_+；切向方程u y_+^α=(hc+u)z^α由u定义满足，输出t完全自由。对y≤0，输入核为0，z=0、n=0是唯一法向解，t仍自由。这既证明全输入coverage，也证明每条普通PPA轨道GR13都是同一完整F的合法GPPA选择。

F⁻¹在0甚至全局R-Lipschitz常数1/a：y>0处任何图值正常分量是ay，故d((t,y),S)=y≤||f||/a；边界距离0。这给Definition5实际S+(||f||/a)B表示，所有前件闭合。

该F不是普通单调：取y>0与零锚(t₀,0)，其配对为−c(t−t₀)y^α+ay²，选t−t₀大即可为负，而且可用t−t₀=y^η、0<η<α构造局部趋零的负配对。普通T在解输入附近的切向变化为λc q^α y^α，不calm。GR15的核本身也在0非Lipschitz，所以不能直接调用Theorem4；Theorem2没有此限制。

**可复算参数。** α=2/3、a=7、c=2、λ=1、h=3/10，取R=1/8，则q=1/8、q^α=1/4、u=1/5、w=3/10、ε=10、L_R=3/2、κ_R=1/(2sqrt2)<1。Python以有理数立方初值逐步精确验证8步普通/warped更新及边界值抽样，无浮点身份误差。

**诚实的物理结论范围。** GR17比普通单点纤维GR13大；不能把它写成完整算法相等。Theorem2适用于这些普通PPA选择，并覆盖其到S的线性距离结论，但单靠它无法决定任意GPPA选择的自由t方向。对被选中的普通轨道，可以先用一步代数验证不变量，而无需预先假设收敛：令K=λc q^α/(1−q^α)，则I=t_k+K y_k^α在y₀>0的轨道上恒定。取预先确定的x*=(I,0)∈S，有

\[
v(x_k)-v(x^*)=(h/\lambda)(x_k-x^*).
\tag{GR18a}
\]

所以**Theorem2加这个精确普通选择不变量，已经推出同一物理点R-linear及有限长度**。这是真实的物理结论重合，不能只把它说成距离重合。直接求和还可读出更细的实际尾：正初值y₀有

\[
y_k=q^k y_0,
\quad t_\infty-t_k
=\frac{\lambda c q^\alpha}{1-q^\alpha}y_k^\alpha,
\tag{GR18}
\]

GR18给实际物理R-linear尾及长度，GR18a则是无循环的同轨道核反演桥；因此该子类不宜宣称本库结果与外部方法彻底不重合。y₀≤0的普通轨道一步进入S，单独显然；任意warped选择仍无这项不变量保证。

## 6. 严格完整RLEB见证：任意核均不能保留cap普通PPA轨道

这里固定C137的**完整**关系

\[
F(\xi,\eta,y)=\{(-2\sqrt y,-D_y(\eta),3y),
(-2\sqrt y,-D_y(\eta),-5y)\}\quad(y\ge0),
\tag{GR19}
\]

域外为空，D_y按C137原定义，λ=1。全部完整纤维在GC-2已穷尽，T(z,p,r)=(z+sqrt|r|,p+sqrt(min(p_+,|r|)),|r|/4)。真残差GC-4为r_F²=4y+D_y²+9y²，完整S=R²×{0}。

选R=1/16、bar t≥(R+L_R sqrt R)/2，L_R=2sqrt2+(3/2)sqrt R。Python复算

\[
L_R=3.2034271247461903,
\quad \kappa_R=(\sqrt R+L_R)^2/16
=0.7453849316207962<1,
\]

且R< [2(4−2sqrt2)/5]²=0.21961328032487662。同一完整图的all-pairs RL、真gaugeψ(s)=s²/4、全输入coverage、完整唯一纤维、最近零锚及U=R³严格留域全部由GC-2–6闭合。因此这是C02-v2的实际完整实例，不是只写孤立Hölder模。

取x₀=(0,−1,1/64)，满足d₀≤R。普通唯一完整轨道

\[
\eta_k=-1,
\qquad y_k=4^{-k}/64>0,
\qquad \xi_{k+1}-\xi_k=\sqrt{y_k}
\tag{GR20}
\]

全程在η≤0；其切向/法向尾几何、物理有限長与点收敛在C137已证明。以下排除允许**任意**v:R³→R³、任意h>0、任意ε>0，且不预设v连续、可逆或Lipschitz。

**第一步：ASM本身迫使核在各切向平面上折叠。** 在η≤0，D_y=0，完整两支只依赖y，记

\[
f_+(y)=(-2\sqrt y,0,3y),
\quad f_-(y)=(-2\sqrt y,0,-5y).
\]

同y、同支、任意两个(ξ,η)比较时Δf=0，GR2强迫Δv=0。因此存在q(y)使v(ξ,η,y)=q(y)对全部ξ、η≤0成立。注意q是核剖面，此处和§5的标量收缩q不是同一记号。

**第二步：同支ASM给局部Lipschitz控制。** 对y,z>0，令Δ=q(y)−q(z)。同正支GR2和Cauchy给

\[
\|\Delta\|\le\epsilon^{-1}
\sqrt{4(\sqrt y-\sqrt z)^2+9(y-z)^2}.
\tag{GR21}
\]

若Δ=0平凡；否则从ε||Δ||²≤||Δf||·||Δ||除以||Δ||即可。这一连续控制来自ASM，不是把kernel regularity偷加为前件。

**第三步：完整跨支迫使正常核变化为二阶小量。** 比较f_+(y)与f_-(z)，以及f_-(y)与f_+(z)，得

\[
-2(\sqrt y-\sqrt z)\Delta_1+(3y+5z)\Delta_3
\ge\epsilon\|\Delta\|^2,
\]
\[
-2(\sqrt y-\sqrt z)\Delta_1-(5y+3z)\Delta_3
\ge\epsilon\|\Delta\|^2.
\tag{GR22}
\]

按Δ₃正负选择有不利正常项的式子，丢掉非负右端，得

\[
\min(3y+5z,5y+3z)|\Delta_3|
\le2|\sqrt y-\sqrt z|\,|\Delta_1|.
\tag{GR23}
\]

对任意固定0<a≤y,z≤b，||sqrt y−sqrt z||≤|y−z|/(2sqrt a)、两个正常系数≥8a。再用GR21，

\[
|q_3(y)-q_3(z)|
\le K_a|y-z|^2,
\quad K_a=\frac{\sqrt{1/a+9}}{8a\sqrt a\,\epsilon}.
\tag{GR24}
\]

将[a,b]均分为N段并把GR24求和，

\[
|q_3(b)-q_3(a)|\le K_a(b-a)^2/N\longrightarrow0.
\tag{GR25}
\]

所以q₃在(0,∞)恒定。若需要识别该常量，可与零锚比较GR21式，得到||q(y)−c||≤ε⁻¹sqrt(4y+9y²)→0，其中c是全部S的核值；故q₃=c₃。排除实际轨道只需要正常分量恒定，不需要这一步极限。

**第四步：即使GPPA另选完整另一支也失败。** 沿GR20，核正常差恒为0。但GPPA必要包含式GR1要求

\[
v(x_k)_3-v(x_{k+1})_3
\in h\{3y_{k+1},-5y_{k+1}\},
\tag{GR26}
\]

右边两个数都非零，矛盾。外部步长h任意正；允许完整纤维改选另一支已经包含在GR26内。因此该普通物理轨道不能代入Theorem2的任何合格kernel，甚至无需继续检查range条件。严格排除的力量来自完整graph的跨支量词，不是v=Id的某个负配对。

**局部及其它kernel条件的范围。** 同一分割证明只须一个切向开片W⊂{η<0}和连接正法向区间I上的产品邻域W×I保留完整两支，并包含待比较的相邻物理轨道点；同y比较仅在W内进行，不要求整个切向平面。也可沿重叠产品片传播正常核常值。仅沿离散轨道点声明ASM而漏掉中间完整图点，不能使用GR25，也不符合原文全图ASM。对mere pair monotone而无核连续门，本节ASM证明没有GR21；接续[C204](pair_monotone_barrier.md)改用标量单调性与总变差，另排除所述同完整图Theorem1表示。若pair monotone且v全局Lipschitz，则在固定切向点上已有||Δv||≤L|y−z|，GR22–25仍把正常分量迫成常数；可排除这样的核保持GR20为**未正则化**GPPA，但不能借此否定Theorem4更换为F+εv后的算法。

删去−5y支会删掉GR22之一，排除失效；保留正输入轨道不等于保存完整F。升维、改变算子或新增selection规则也超出GR26的同对象结论，需要独立桥。

## 7. C09/C10/C141/C191–C193逐项边界

### 7.1 一个可复用、仍严格限域的完整双支排除引理

令某个切向区域的完整双支图值仅依赖y>0，为

\[
f_+(y)=(H(y),a(y)),\qquad f_-(y)=(H(y),b(y)),
\quad a(y)-b(y)>0,
\tag{GR27}
\]

H,a,b在正轴局部Lipschitz，切向变量不出现在两支值中。任意ε-ASM核同y同支比较迫使它在该切向区域只依赖y；同支比较给||Δv||≤ε⁻¹||Δf_+||=O(|Δy|)。对任意正法向紧区间，间隙g(y)=a(y)−b(y)有正下界；取足够小|y−z|，两次跨支的正常系数a(y)−b(z)、b(y)−a(z)分别≥g_min/2、≤−g_min/2。按正常Δv的符号选择不利式，得|Δv_normal|≤(2/g_min)||ΔH||·||Δv_tangent||=O(|Δy|²)。用足够细的均分求和，正常核分量恒定。这个证明只对所述完整双支区域成立，不是一般所有multivalued F的分类。

* **C141：** 在η≤0，τ_{y^{1/ν}}(η)=η，故H(y)=(-A y^{γ/ν},0)，a(y)=y^{1/ν}−y、b(y)=−y^{1/ν}−y。正法向间隙2y^{1/ν}>0，全部剖面在y>0局部光滑。取p₀≤0、0<r₀≤R<1，SF-5的严格小半径可选、完整纤维等式已核，普通轨道r_k=r₀^{ν^k}。任一输出y∈(0,1)处a(y)>0、b(y)<0；所以同GR26任意ASM核不能保持该同F物理轨道。SF-6/7给超几何共同尾及逐轨道Q-ν率，原Theorem2未提供这些物理率和解选择两点模；仅“它也有某个R-linear上界”不能消除同轨道表示的必要条件。
* **C10：** H(y)=−ℓ_a(4y)，a(y)=3y、b(y)=−5y，GM26–29显示正轴局部C¹，间隙8y>0。完整轨道正常每步乘1/4，两个图值正常分量均非零，所以同一排除适用全部非驻定正法向轨道。a>1时GM32/35给严格兼容及Dini，物理点尾为对数几何采样级数的多项式阶，长度有限；a≤1时距离仍Q-linear、切向和发散。不能把a≤1称作C09有限长度实例：它恰违反Dini。
* **C137：** §6已给最简明确固定参数和初值完整见证，不依赖这条推广引理来闭合主排除。

### 7.2 与其它规范Claim的逐项关系

| 本库身份 | 精确新增/不同的内容 | 必须保留的反向限制 |
| --- | --- | --- |
| C02-v2 / R01–R02 | 有限维、同图块all-pairs RL、coverage、最近零锚、完整真残差输出EB、同尺度兼容及严格留域，给物理有限长/点尾；可为局部图块 | 完整J量词需另证全部可达输入完整纤维一致；原C02多选择版本仍候选。§5真实重合，§6真实同轨道分离；不能由一个例子推出总体类大小或一切表示不可比。 |
| C09 | 一般连续非减反射模、Dini采样可和及同窗预算给物理尾与点收敛，物理尾未必几何 | GPPA的核压缩可有不同物理选择，不自动提供同一反射模或Dini；反向也不自动给全图pair核和全域coverage。 |
| C10 | 完整对数图、真实inf残差、Dini门槛a=1及距离/点收敛分离，见GM26–39 | a≤1不满足C09；其距离Q-linear本身不证明能代入Theorem2，GR27已针对同完整F/同轨道排除ASM核。 |
| C11及C137/C141的解选择结果 | 共同尾、有限时单步模→连续回缩及量化两点极限模；C137/C141另有同图配对锐阶 | 原文没有这些输出，但“未写”不等于全球首创。许多给定算法的连续极限映射也可由另外理论推导，须另逐定理检索。 |
| C191 | 完整自然支撑面/法锥图、全部近端纤维、局部RL及真EB，另有独立法向/切向收敛机制 | §5已证明其中一个合法子类被任意核框架实质覆盖。不能以“非calm/非单调”作GPPA总排除；一般D非单点等原数据尚未分类全部kernels。 |
| C192 | 完整feedback关系全输入存在，任意选择直接有限长；仅小条带完整单值/RL，明确全域三值反例 | Theorem2允许warped多值，并不因普通J多值就被排除。一般feedback的任意核同轨道表示仍待核；普通全图all-pairs RL也不能由小条带扩大。 |
| C193 | 同完整图每个解附近的最佳Hölder指数α及指定固定矩阵二次锚失败 | 仅排除SN17及确能推出calm的前件，不排除任意nonlinear/noninjective kernel。§5正是反例说明这种“SN17失败⇒不能用GPPA”推断不成立。 |

## 8. 可执行判断、fatal objections与剩余缺口

对“完全重合”的强说法有严格反例：§6的C137完整F和普通轨道满足严格RLEB全部门，却不存在任何符合Theorem2 ASM的kernel保持它；§7还给了相同机制的C141/C10扩展。对“完全不重合”的强说法也有严格反例：§5的非单调、非calm子类所有普通PPA轨道是合格GPPA选择，并有全部inverse-R-Lipschitz与coverage；线性子类完整算法更完全相等。

以下异议足以阻止相应过宽升级：

* 只证明v=Id失败，不能排除任意kernel；只证明一个表示失败，不能排除删支之外的保真升维/分裂方法。
* 省略另一完整纤维分支会毁掉§6的全图证明；把选中范数当真残差会毁掉RLEB对象，F48已有明确反例。
* 把Theorem2核R-linear或集合距离R-linear称作物理点R-linear/有限长，GR10直接反驳；若物理范数尾确实已R-linear，有限长度则由GR11随附，不能单独创新。
* 把Theorem4的F+εv误差稳定性移植给同一未正则化F的精确PPA，是换算法；双极限不是一条变ε轨道收敛。
* 把C193固定二次锚排除当所有GPPA核排除，§5直接反驳。
* 把本文一个完整分离例升级为总体RLEB类更大、自然母空间的Baire/测度规模比较或全球创新性，证据不足。

剩余门：一般C191支撑面与C192 feedback是否有其它保真同轨道kernel，尚无全分类；§6原ASM证明之外的标量双支mere-monotone表示已由C204排除，但C205–C207子关系导入成立；任意lift/分裂/压缩的物理回代需要独立桥；原文[13,14]被引用的所有历史定理未在本文逐篇审查；这两个2026年方向以外的全球先行性检索没有完成。Theorem4所指出的技术漏门有上文严格修补，不把它们夸大为致命数学错误。

复现：在仓库根运行 `python research/comparisons/2026_08_gppa_nfb/gppa_check.py`。本稿及脚本为独立比较文件，不更改任何原Claim状态，不commit/push。
