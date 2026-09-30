# 随机多值 RL 自然应用攻击：可保留压力测试，暂不建立旗舰正类

日期：2026-09-09。任务：`multivalued_random_application`。状态：`PROJECT_PROOF / PROVISIONAL`。

## 0. 冻结判定

**KILL 本轮“已找到新 coupling/pathwise RL 独占、并足够支持旗舰定位的自然随机算法类”这一主张。不是 KILL 随机概率方向。**

本轮确实找到一个原生、持续多值、非孤立不变族的模型：单位球面正常锥的完整 resolvent，公平随机选择两个解。它一步到不变分布，而路径持续跳跃；旧同步输运差异甚至精确识别不变集且线性次正则，却无法与其同步能量产生严格速率。这个模型比“将一个反造的多值 F 随机化”更自然，也给新 law-level 理论一个必要压力测试。

但是其正向解法就是二元素群的对称化/两点条件分布重配对。不能把成熟机制重新命名为 RL 独占成果。其余几条候选或者落入旧 union-averaged/局部谱隙理论，或者随机化只增加标准 pathwise-to-law 积分，并未解决新的原生验证难点。

| 候选 | 真多值/非孤立结构 | 原生证书 | law-level 结论 | 本轮判断 |
|---|---|---|---|---|
| 球面完整正常锥 resolvent | 每个球面输入有两个输出；不变律无限多；持续跳跃 | 完整图显式；源 Ψ 精确线性 EB；旧能量兼容性必失败 | 公平选择一步对称化；可显式重配对 | **保留机制压力测试；KILL 旗舰正类** |
| 有限实 phase-retrieval 随机 Kaczmarz | 全局有 sign ties；解附近正 margin 会消除 ties | 采样 Gram 矩阵给线性 EB 和收缩 | 熟悉的谱隙/条件提升 | **KILL 非线性 RL 独占主张** |
| 随机 sparse active-set prox | 支切换可能持续，解可非孤立 | 许多标准类是有限 convex-branch/union-averaged | 已有确定性全选择理论，再积分 | **KILL 仅随机化的主张** |
| crossing-parabola CDRS | 真 tie；原例固定点孤立且一次识别 | 已审 q=2/5、MSR=5/3、锚点平均能量 | 任意可测选择核均 W2 几何收敛 | **HLS 主定理不能字面套；但旧锚点理论加初等 lifting 足够** |
| distance-profile CDRS | 任意闭 C；真 ties；非孤立/奇异固定集 | 已审精确 gauge；单次 nearest-anchor 识别 | 沿已识别纤维随机时间/参数提升 | **不构成新的随机难点** |

“KILL”仅针对本轮旗舰验收目标，不表示上述数学结果错误或没有附录价值。未证明全球无人做过任何精确公式，也未作投稿录用预测。

## 1. 输入、证据与本轮新增内容

已核查的本地材料：

- `t5_core_theorem.md`：AP-RL 的图点碰撞、允许转换、ordinary EB 与 actual-residual EB 区别。
- `T5_AUDIT_C_MULTIVALUED_M1.md`：M1 不是自动的 PPA/Markov 外迭代桥梁；完整 inverse 与指定 selector 的量词。
- `output/selection_pathwise_outer_transition_RL_upgrade.md`：全部定义、全轨道定理及 Hölder 两分支例。
- `output/ATTACK_CDRS_NATURAL_MODEL.md`：原生集合、完整投影、q=2/5 收缩、tie、MSR 与旧条件失效定位。
- `output/AUDIT_CDRS_NATIVE_CONTACT_CALCULUS.md`：已审 class-level 图、gauge、单次 anchor 识别及旗舰边界。
- `output/ATTACK_MARKOV_CONDITIONAL_REPAIR.md`：条件距离、matched residual 接口及不能混用不同 coupling 的警告。
- `output/AUDIT_MARKOV_NOVELTY_AND_JOURNAL.md`：源 Ψ 的识别问题、旧充分条件及 conditional/fibered 先行性。

本轮新增的完整直接推导是第 2 节球面正常锥模型、第 3 节一致投影/真 prox 的线性锚点障碍、第 4 节 finite phase-retrieval 原生局部证书，以及第 5 节不需 Feller 的 elementary law lifting。项目旧结果仅在其已声明范围内使用，没有重新声称全部独立审计。

文献采用 SCI-Skills literature-search 的原生网页及一手文献核验边界：本轮是定向 reconnaissance，不是系统综述；未调用第三方 API。

## 2. 一个真正原生的随机多值模型：球面正常锥，而不是 metric projector

### 2.1 完整原始图与 resolvent

令 d≥2，C=S^{d−1}⊂R^d，F=N_C 为光滑流形的 limiting normal cone：

\[
N_C(y)=\mathbb R y\quad(y\in C),\qquad N_C(y)=\varnothing\quad(y\notin C).
\]

固定 λ>0。对 x≠0，完整 inclusion

\[
x-y\in\lambda N_C(y)
\]

等价于 y∈C 且 x=(1+λα)y。因此

\[
\boxed{J_{\lambda N_C}(x)=\{x/\|x\|,-x/\|x\|\}.}
\tag{2.1}
\]

对 x=0，全部 y∈C 都是解；后文状态空间直接取 C，不涉及该输入。式 (2.1) 已给出每个相关输入的全部解，绝不是 favorable branch 或事后反造 F。

**关键算法边界：**当 x≠0 时 metric projection P_C(x) 只有正向解 x/||x||。负向解是距离平方在球面上的另一个驻点，不是 proximal minimization 的最小点。故本节是正常锥 inclusion-PPA 的完整求解选择，不能称为“随机精确最近点投影”。

原始零集 S=F^{-1}(0)=C 非孤立。每个 x∈S 的完整 resolvent 仍有两个输出 ±x。因此完整 AP-RL 在每个状态发生同输入碰撞；现有 static-/transported-anchor pathwise RL 也在 S 上失败：其 ω(0)=χ(0)=0 会强制全部允许输出等于 x，而 −x 是实际允许输出。

普通 state EB 并不能救它。对 y∈dom F=C，有 d(y,S)=0 且 d(0,F(y))=0，所以任何 gauge EB 在域内均真但完全无信息；域外 F 为空，扩展残差为 +∞，也不能给有限证书。这是完整原始图、目标和残差的真实结论，不是证明遗漏。

### 2.2 原生随机选择、整个不变族与路径行为

在 C 上独立公平选择两个 resolvent 解：

\[
X_{k+1}=\xi_kX_k,\qquad \mathbb P(\xi_k=\pm1)=1/2.
\]

记 A(x)=−x，A_# 为 pushforward，则

\[
\mu K=\tfrac12(\mu+A_\#\mu),\qquad K^2=K,
\]
\[
\boxed{\operatorname{inv}K=\{\pi:A_\#\pi=\pi\},\qquad\mu K^k=\mu K\quad(k\ge1).}
\tag{2.2}
\]

每个 antipodal orbit {x,−x} 上的公平分布都是不变律；这些轨道由实射影空间参数化，并允许任意混合。因此不变族绝不孤立。

路径却不收敛。事件 ξ_k=−1 独立且概率 1/2，几乎必然发生无限次，每次 ||X_{k+1}−X_k||=2。因此步长不趋零、路径长度无限。即使初值已经服从不变律，也保持这些实际跳跃。

这严格区分了“PPA 求零点”“Markov 求不变分布”“stationary samples 不动”三件事；后两者绝不等价。

### 2.3 源同步 Ψ 不是假零点问题：它有精确线性 EB

对任意 x,y∈C，使用同一个随机符号。Hilbert 同步差异为

\[
\begin{aligned}
\mathbb E\|[x-T_\xi x]-[y-T_\xi y]\|^2
 &=\tfrac12\cdot0+\tfrac12\|2(x-y)\|^2\\
 &=2\|x-y\|^2.
\end{aligned}
\]

按 HLS 原定义，内层只允许到不变律的 W2 最优 coupling；上式对每个 coupling 成立，所以没有优化次序问题：

\[
\boxed{\Psi(\mu)=\sqrt2\,d_{W_2}(\mu,\operatorname{inv}K).}
\tag{2.3}
\]

不变集是紧状态 C 上的闭集。因而 Ψ 准确识别整个不变集，且具有精确常数 1/√2 的全局线性 EB。它与旧 parallel-projection 相关性假零点是**不同失效机制**。

### 2.4 旧同步能量与任何严格 gauge rate 均不兼容

记 c=(1−α)/α>0。当前两个原生 maps 在 C 上都是等距，因此

\[
\mathbb E\|T_\xi x-T_\xi y\|^2=\|x-y\|^2.
\]

HLS 型同步能量要求

\[
\|x-y\|^2\le(1+\epsilon)\|x-y\|^2-2c\|x-y\|^2,
\]

对不同 x,y 成立的必要条件恰为

\[
\boxed{\epsilon\ge2c.}
\tag{2.4}
\]

式 (2.3) 的最小线性 EB 常数 κ=1/√2，故其 scalar factor 满足

\[
1+\epsilon-c/\kappa^2=1+\epsilon-2c\ge1.
\]

更换一般 gauge 也不能改善实际尺度：若 e=d(μ,inv K)，任何合法 EB gauge ρ 必须满足 e≤ρ(√2 e)，从而其 generalized inverse 在这些尺度不大于 √2 e。同步下降式中可减项至多 2ce²，仍不可能得到小于 e² 的统一上界。

所以本例满足完整模型可解、连续原生 maps、非空不变集、Ψ 识别及精确线性次正则；却不能让这组同步几何与同步残差产生严格收敛因子。算法事实上一步收敛。失败是**同步 coupling 没看见随机分支之间的混合抵消**，不是 Ψ 不识别目标。

本段是针对源公式的直接推导，不声称反驳 HLS 的充分定理。其假设本来就包含严格 gauge compatibility。[HLS，Theorem 2.6 与 Corollary 2.7](https://arxiv.org/html/2206.05213v3)

### 2.5 正确 coupling 很简单，也因此不足以主张旗舰新意

先取 X∼μ，独立公平符号 σ，令 Y=σX，则 Y∼μK。再取独立公平 η，对第一条链取 X⁺=ηX，对第二条链取更新符号 η′=ησ。即使条件于 (X,Y)，η′ 仍公平，故第二个边缘确实执行 K；同时

\[
Y^+=\eta'Y=(\eta\sigma)(\sigma X)=\eta X=X^+.
\]

这是合法的 branch-rematching coupling，不是强行令两条链使用相同标签。它不需要预先认定该初始 coupling 是 ordinary W2 最优 coupling；若要以其代价取代 W2，必须明确改用保留 antipodal orbit 的条件距离。

不应把这个机制称作全新：uniform orbit randomization 已是成熟的 symmetry/orbital Markov 思路，例如 [Niepert，Markov Chains on Orbits of Permutation Groups，2012](https://arxiv.org/abs/1206.5396)。此引文只是机制近邻，不冒称该文已有本节正常锥或源 Ψ 的精确公式。

**验收：**保留为新 stochastic RL/coupling 的最小强制测试；它暴露的障碍不同于假零点。KILL 将本身作为高水平主定理的应用，除非能推广到不依赖群对称化、不能降成条件两态链的真实算法类，并完成原生证书。

## 3. 两个一般自然性筛选：真正 projector/prox 不自动产生 Hölder 非 calm 优势

### 3.1 一致非凸 projector 自带线性锚点界

设 C 闭、p∈C，y∈P_C(x)。全局最优性给

\[
\|x-y\|\le\|x-p\|,
\quad
\|y-p\|\le2\|x-p\|,
\quad
\|2y-x-p\|\le3\|x-p\|.
\tag{3.1}
\]

若 S⊂C 是共同可行集，取 p∈P_S(x) 即得 uniform linear anchored reflection。多个 projection ties 仍可能存在；(3.1) 不声称 global Lipschitz/Aubin 或非扩张，也不单独证明收敛。但它排除了“这些真实最近点 branches 在共同可行点必有无穷线性 violation，只有 γ<1 才能控制”的说法。

有限长度的 consistent projection composition 也保持某个有限线性锚点常数（逐步使用同一个共同 p）；反射、平均和有限 composition 同样只能把常数放大，不自动创造 genuinely non-calm solution-anchored 模量。

### 3.2 真正 proximal minimization 在共同极小点附近同样如此

若 p 是 f 的全局最小点，且

\[
y\in\operatorname*{argmin}_z\{f(z)+\|z-x\|^2/(2\lambda)\},
\]

则 f(y)≥f(p)，比较候选 p 得 ||y−x||≤||p−x||，故仍有 (3.1)。若仅为局部极小点，需要同时保证实际输出 y 位于同一 f(y)≥f(p) 的局部最小邻域，且实际 prox 子问题确实可与 p 比较；不能自动外推到任意 stationary solution。

因此，想要项目中两分支 Hölder 漂移例那种“所有 selector 均不 calm”，必须从不一致内部接触、非 minimization inclusion、或不同于共同极小点的目标结构寻找；不能只写一个非凸 prox 名称。

## 4. Phase retrieval 与 sparse active sets：分别核对原生几何和 EB

### 4.1 有限实 phase retrieval 的局部原生计算

令 ||a_i||=1，b_i=|a_i^T x_*|，

\[
C_i=\{x:|a_i^Tx|=b_i\},\quad p_i>0,\quad\sum_i p_i=1.
\]

全局 P_{C_i} 在 a_i^T x=0、b_i>0 时有真实两个值。若所有正 b_i 有 margin，取

\[
0<r<\min_{i:b_i>0}b_i.
\]

则 B_r(x_*) 内正幅值的正确 sign 固定；b_i=0 的约束本来就是单个 hyperplane，无不同 sign 输出。于是该球内每个原生 projector 恰为

\[
T_i(x)=x-a_i a_i^T(x-x_*).
\tag{4.1}
\]

设 A 的行为 a_i^T，V=(ker A)^⊥，G=Σ_i p_i a_i a_i^T，η=λ_min(G|_V)>0（V={0} 时无待消除误差）。局部解集 S_loc 是该 sign chart 的 affine solution set x_*+ker A 与局部域的对应部分。为避免截断目标的人造边界，以下距离使用完整 affine chart S_aff=x_*+ker A，并将输入限于保持 margin 的球。

令 e=P_V(x−x_*)。原生 RMS constraint residual 为

\[
\mathcal R(x)^2=\sum_i p_i d(x,C_i)^2=e^TGe,
\]

故得到真实、可计算的线性 EB

\[
\boxed{d(x,S_{\rm aff})\le\eta^{-1/2}\mathcal R(x).}
\tag{4.2}
\]

每个 update 保持 ker A 分量，且投影到包含 x_* 的正确 hyperplane，不离开初始球。勾股分解直接给

\[
\mathbb E[d(X^+,S_{\rm aff})^2\mid X=x]
=\|e\|^2-e^TGe\le(1-\eta)d(x,S_{\rm aff})^2.
\tag{4.3}
\]

非孤立解集并不使这个类新颖：其正常块是随机 affine projections，切向块守恒。law-level 结论是这种局部谱隙的条件/纤维提升。若希望研究无限 fresh measurements，没有统一 margin 是真问题，但随机 Kaczmarz 的 wedge/概率分析已有一手研究，不能把它描述成未经研究的方向。[Tan–Vershynin，2019，原文 §1.2 与 §2](https://arxiv.org/html/1706.09993v2)

复杂信号的 global-phase circle 也不证明局部多值困难尚无人处理；针对 complex-valued phaseless equations 的随机 Kaczmarz 线性收敛已有论文。[Huang–Wang，arXiv:2109.11811](https://arxiv.org/abs/2109.11811)

**判定：**本轮有限 margin 模型完整验证了原始选择与 residual，但没有 γ<1、真实局部 sign ties 或新 law-level 难点。KILL 作为 RL 独占应用。无 margin/noisy case 尚未完成，不能填上一个未经验证的 generalized subregularity 假设后宣称成功。

### 4.2 稀疏 active-set 的真实多值并不等于新几何

对 C_s={x:||x||_0≤s}，原生 projector 是选取绝对值最大的 s 个坐标、保留其值，其余置零。并列可产生多值。每个固定 support 的分支是 coordinate-subspace orthogonal projection，因而 firmly nonexpansive。

在一个 strong fixed point 的局部有效支持族上，多个支可以持续出现；但这正是 union-averaged 既有理论覆盖的对象之一。min-convex prox、凸支并集、其 composition/convex combination 已有明确演算和 strong-fixed-point 局部收敛。[Dao–Tam，2019，Proposition 4.2 及应用部分](https://arxiv.org/html/1807.05810v2)

本轮没有为一般 noisy sparse nonconvex model 验出新的 ordinary generalized EB。只说“半代数”至多支持某种存在性 gauge 的进一步调查，不能代替实际 residual、解集和允许支完整性的证明。

**判定：**KILL “有限 active-set + 随机支标签”本身作为新应用；保留非 prox-regular、无 uniform chart、持续且影响不变律的真实模型为未完成方向。

## 5. 已有 CDRS 随机化为什么不够：一个精确 law lifting 及 HLS 范围更正

### 5.1 初等 lemma：全允许支收缩立即产生 law 收敛，不需 Feller

设 B 是以 p 为中心的不变闭球，T(x) 非空，且

\[
\|y-p\|\le q\|x-p\|\quad(y\in T(x)),\qquad q<1.
\]

任何可测 Markov kernel K(x,·) 若支持在 T(x)，均满足

\[
\boxed{W_2(\mu K^k,\delta_p)^2
\le q^{2k}\int\|x-p\|^2\mu(dx).}
\tag{5.1}
\]

证明只需条件期望并迭代，最后用到 δ_p 的 transport 唯一。δ_p 是不变律；若 π 是其他不变概率，在有界球上对 ||x−p||² 积分得 E_π||X−p||²≤q²E_π||X−p||²，因此只能等于 δ_p。完全不需要 continuity/Feller。

还自动有 ordinary fixed-point residual EB

\[
\|x-p\|\le(1-q)^{-1}d(x,T(x)),
\]

及锚点 averaged energy

\[
\|y-p\|^2+\frac{1-q}{1+q}\|y-x\|^2\le\|x-p\|^2.
\tag{5.2}
\]

这不证明 T 对所有 input pairs averaged；它只说明确定性 q 收缩足以处理任意随机选择。

### 5.2 Crossing-parabola CDRS

项目现有原生模型已给 q=2/5、半径 1/16、ordinary MSR=5/3，直接代入 (5.1) 即可。因此随机 tie、任意可测 state-dependent tie policy 均可处理，但新增 proof 只有条件期望，且原例一次整周期后支识别。

**必须保留的一处准确更正：不能说 HLS Theorem 2.6 字面直接覆盖这个真实 kernel。** 原定理要求连续 T_i 和所有 x,y 的 expected pair inequality。在非零 tie 的两侧，实际允许输出各自唯一并趋向两个不同极限；任何只在 tie 处混合的 policy 不能消除该两侧跃迁，因此实际 kernel 一般不是 Feller，也没有全对 finite-L Lipschitz bound。原定理不能在删去这些假设后使用。[HLS，Theorem 2.6](https://arxiv.org/html/2206.05213v3)

正确 novelty 结论更窄：它不在该 HLS 主定理的字面范围，却已由已知 pointwise-averaged 思路/项目已完成确定性 verifier 与初等 lifting 解决，尚不足以证明新的 stochastic coupling 主定理必要。

### 5.3 Distance-profile CDRS

已审的 native class 可以给非孤立甚至奇异 C 和真正 generalized gauge，这是实质确定性 verifier。但其 scalar radial/vertical dynamics 对 nearest-point branch 独立；一次沿严格 nearest segment 更新后 anchor 唯一，随后保持不变。

若只是随机化初始 tie，极限 law 就是“初始随机 nearest anchor 的 pushforward”；若随机化一些保持同一个 fixed-height/anchor 的参数，只需进一步检查 uniform scalar bounds，随后仍为标准纤维/随机时间提升。本轮没有证明非共用 profile 或不同 fixed-height 的随机 cycles 的完整 invariant law，因此不能称为持续跨纤维的新结果。

## 6. Law-level 接口的额外刹车：q>1 state EB 不能直接提升为 full-law EB

同轮 `stochastic_rl_theory_attack` 提供了这个关键 no-go；本节独立重述其简单缩放证明。假设单点目标 0、state residual r(0)=0，且某个 a≠0 有 0<r(a)<∞。取

\[
\mu_\varepsilon=(1-\varepsilon)\delta_0+\varepsilon\delta_a.
\]

则

\[
W_2(\mu_\varepsilon,\delta_0)=\sqrt\varepsilon\|a\|,
\quad
\left(\int r(x)^2\mu_\varepsilon(dx)\right)^{1/2}=\sqrt\varepsilon r(a).
\]

所以任何 q>1 的统一 full-law EB

\[
W_2(\mu,\delta_0)\le K\left(\int r^2d\mu\right)^{q/2}
\]

均因 ε^{(1−q)/2}→∞ 而失败，哪怕原 state EB ||x||≤K_0r(x)^q 完全正确。

因此真正 γ<1、q>1 的 RL 应先在 state/conditional 层复合两张证书，再积分实际 contraction/length estimate；不能把确定性 exponent 原封不动搬到整个 W2 空间。这也是为什么“套一个 Markov 外壳”不是自动得到强新定理。

## 7. 仍值得做的唯一应用验收目标，而不是宽泛选题列表

下一轮若继续，建议只接受下面这个收紧目标：

> 从一个明确的、非群平均/非单次 branch-identification 的不一致随机 splitting 或正常锥算法出发；其持续分支选择影响非孤立不变族；用原生投影/正常锥数据验证允许图、coverage、目标识别和与 branch-rematching 相容的一般 residual gauge；对同一算法证明旧同步证书不能给出该结论，而新 coupling 产生可计算速率。

必须逐项拿出：

1. 算法是真实既有模型或明确合理的算法，不是为想要的 x↦x±|r|^γ 反造 F；正常锥 stationary output 与真实 nearest-point/prox-min output 不混淆。
2. 真多值/非孤立结构在有效收敛区域内存在，不只在之后被删去的远处；支持 switching 不是只在第一个时刻。
3. generalized EB 从原生参数算出；不是命名一个到未知 invariant law 的距离当“可计算 residual”。
4. 同一个合法 coupling 同时承担能量、目标 marginal、residual 与 rate，或显式计入 rematching loss。
5. 证明相对于 HLS、deterministic pointwise-averaged、standard conditional lifting、finite-group symmetrization 的严格新增；不能只指出某一旧 theorem 的非必要假设不满足。

本轮没有满足这五项的类。应如实留在“待构造/待证”而非把候选升格为结果。

## 8. 定向检索记录与证据边界

日期：2026-09-09。平台原生 web；仅采用已打开的作者 arXiv、正式出版社页、作者论文页面。未检索商业数据库完整引文网络，未取得可信 hit counts。

核心 queries：

```text
randomized Kaczmarz phase retrieval nonconvex projection global phase Tan Vershynin
random function iterations Markov pointwise almost averaged fixed points HLS expansive Markov operators
nonconvex sparse projection union averaged mappings Dao Tam 2019
orbital Markov chains symmetries uniform orbit sampling Niepert 2012 arxiv
conditional expectation compact group Haar averaging projection invariant measures Markov kernel
```

| 原始来源 | 本轮实际核查范围 | 用途与限制 |
|---|---|---|
| HLS, arXiv:2206.05213v3 | Theorem 2.6、Corollary 2.7、Definition 3.1、Theorem 3.7 | 精确竞争定理的连续性/全对量词与 gauge compatibility；页面动态页眉日期不当成版本日期 |
| Dao–Tam, arXiv:1807.05810v2 | 正文 Proposition 4.2、strong fixed point 及 union-averaged 应用定位 | 精确相邻：有限活动支不是新对象；不声称覆盖所有 nonconvex sparse algorithms |
| Tan–Vershynin, arXiv:1706.09993v2 | 正文随机 Kaczmarz 更新与 wedge 分析 | 真正 phase-retrieval 算法及先行性，不把本轮局部 margin 推导冒归作者 |
| Huang–Wang, arXiv:2109.11811 与 SIAM 正式摘要 | bibliographic record/abstract | complex phase 已有收敛研究；没有全文逐定理排除全部新模型 |
| Niepert, arXiv:1206.5396 | 原始记录/摘要 | orbit-sampling 机制近邻；未核对其是否包含本节源 Ψ 公式，因而不作精确优先权裁定 |

非原始聚合页面、无关 Haar 随机矩阵条目、通用 Markov 教学结果未作为技术证据。搜索未发现精确题名不能推导“没人做过”。

## 9. Specialist return contract

```yaml
contract_version: "1.0"
expert_skill: sci-skills-literature-search
project_id: null
paper_family: T
stage_id: null
task_id: multivalued_random_application
task_status: PROVISIONAL
inputs_reviewed:
  - t5_core_theorem.md, targeted graph and EB scope
  - T5_AUDIT_C_MULTIVALUED_M1.md, M1 and selector interfaces
  - output/selection_pathwise_outer_transition_RL_upgrade.md
  - output/ATTACK_CDRS_NATURAL_MODEL.md
  - output/AUDIT_CDRS_NATIVE_CONTACT_CALCULUS.md
  - output/ATTACK_MARKOV_CONDITIONAL_REPAIR.md, targeted stochastic interface
  - output/AUDIT_MARKOV_NOVELTY_AND_JOURNAL.md
  - primary sources listed in Section 8
outputs:
  - output/ATTACK_MULTIVALUED_RANDOM_RL_APPLICATION.md
evidence_status:
  - AI_INFERENCE / PROJECT_PROOF: sphere normal-cone full resolvent, invariant class, exact source Psi, and incompatibility
  - AI_INFERENCE / PROJECT_PROOF: consistent projection and true prox anchored linear bounds
  - AI_INFERENCE / PROJECT_PROOF: finite-margin phase-retrieval native local spectral EB
  - AI_INFERENCE / PROJECT_PROOF: elementary law lifting without Feller
  - VERIFIED_USER_MATERIAL: existing CDRS quantitative constants and one-step anchor identification
  - VERIFIED_SOURCE: HLS literal assumptions and union-averaged / phase-retrieval precedents
  - PENDING_VERIFICATION: worldwide priority of source-Psi sphere calculation
  - PENDING_VERIFICATION: any natural class meeting the exclusive stochastic-RL flagship target
assumptions:
  - finite-dimensional Euclidean spaces
  - sphere normal cone is limiting manifold normal cone, not metric projection
  - law lifting uses measurable supported transition kernels
author_input_needed: []
manual_actions: []
quality_checks:
  - full resolvent outputs distinguished from proximal minimizers
  - actual AP-RL collision checked
  - state EB and law invariant identification kept separate
  - pathwise convergence not inferred from distributional convergence
  - HLS continuity and all-pairs assumptions not silently removed
  - conditional and full-Wasserstein metrics not conflated
  - old group averaging and elementary lifting not relabelled as new
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: Independently audit Section 2 as a mandatory source-Psi / branch-rematching stress test; do not promote the present natural applications to a flagship positive theorem
stage_acceptance_recommendation: REPAIR
```

唯一下一步：独立攻击第 2 节球面模型的完整正常锥图、源 Ψ 定义与同步 gauge incompatibility；通过后只把它纳入新随机理论的压力测试，不把该附录型正解当成旗舰应用。
