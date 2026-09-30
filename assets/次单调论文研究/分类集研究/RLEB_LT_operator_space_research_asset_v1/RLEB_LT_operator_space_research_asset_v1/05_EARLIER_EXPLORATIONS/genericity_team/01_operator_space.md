# 算子空间与 Baire 范畴建模评估

日期：2026-09-20。范围：只评估新研究方向的空间、拓扑与可证明的集合结构；不改现稿，不重审无关 RLEB 结果，不宣布任何尚未证明的泛性结论。

## 结论先行

**可行，而且可以选到一个真正容纳原有完整 resolvent 与多解结构的 Baire 空间。** 最推荐的是：在有限维状态空间上，把完整 resolvent 当作变量，固定解平面、RL/EB 证书和严格兼容余量，采用紧集上一致收敛拓扑。状态空间不必先推广到无限维；连续算子的空间本身已经是无限维的泛函分析对象。

在下面这个具体模型中，可以独立证明：

1. 固定证书层是紧致、完备的度量空间，因此是 Baire 空间；
2. 完整 resolvent、闭图、真实 min-residual EB、同一个非单点零集都保留；
3. “至多二值”虽然不是闭条件，却是 G_delta 条件；加入后仍可完全度量、仍为 Baire 空间；
4. 算子到极限映射的赋值 T ↦ Pi_T 连续；
5. “在固定初值紧集上有某个正阶 Hölder 模”是 F_sigma，“没有任何正阶 Hölder 模”是 G_delta；
6. **尚未证明坏类稠密、余稀、零测或满测。** 真正研究难点是保留完整证书的扰动/嵌入引理，不是给坏类起一个集合论名字。

## 1. 首先固定要比较的对象

本研究不是比较“所有算子的好坏”。应当比较满足同一组收敛证书、具有同一个多解几何的算法，问它们的最终解选择有多稳定。

取状态空间 E = R^d，固定非单点闭仿射子空间 S，平移使 0 ∈ S。固定

\[
\lambda>0,\quad 0<\gamma<1,\quad L\ge0,\quad R>0,
\quad 0<\rho\le R,\quad 0<\kappa<1.
\]

固定连续非降函数 psi : [0,infinity) → [0,infinity)，psi(0)=0，并要求数值兼容条件

\[
\psi\!\left(\frac{d+Ld^\gamma}{2\lambda}\right)
\le\kappa d\qquad(0\le d\le\rho). \tag{1}
\]

这里把严格余量固定为同一个 kappa < 1，而不只写“每个算子分别存在一个小于 1 的常数”。

定义 X 为满足以下条件的连续映射 T : E → E：

\[
T|_S=I, \tag{2}
\]

\[
\|2(Tx-Ty)-(x-y)\|
\le L\|x-y\|^\gamma
\quad (x,y\in E,\ \|x-y\|\le R), \tag{3}
\]

\[
d(Tx,S)\le
\psi\!\left(\frac{\|x-Tx\|}{\lambda}\right)
\quad(x\in E). \tag{4}
\]

这是一个**固定证书层**，不是所有 RLEB 算子的统称。全空间形式的 (4) 比仅局部 EB 强，优点是彻底避免隐藏输入纤维降低最小残差。现有几何显式构造满足全局 EB，可置于该层。以后若希望推广到仅局部 EB，必须另外固定输入/输出 collar 并防止域外纤维闯入，不能直接删掉这里的全空间量词。

## 2. 不丢失完整多值算子的 resolvent 编码

对 T ∈ X 定义整个算子

\[
F_T(u):=\{(x-u)/\lambda:\ x\in E,\ Tx=u\}.
\tag{5}
\]

这里的 T^{-1} 是集合值逆像，因此 F_T = (T^{-1}−I)/lambda，不表示 T 可逆。

逐点直接计算得到

\[
u\in J_{\lambda F_T}(x)
\iff (x-u)/\lambda\in F_T(u)
\iff Tx=u.
\]

所以 **J_{lambda F_T}=T 在整个 E 上成立**，没有局部分支升级问题。图关系是可逆线性坐标变换

\[
\operatorname{gph}F_T
=\{(Tx,(x-Tx)/\lambda):x\in E\}.
\tag{6}
\]

因为 gph T 闭且该坐标变换是全空间线性同胚，gph F_T 闭。并且

\[
\operatorname{zer}F_T=\operatorname{Fix}T=S.
\tag{7}
\]

其中 Fix T ⊂ S 来自 (4) 与 psi(0)=0，反向包含来自 (2)。

对所有逆纤维取下确界，(4) 给出

\[
d(u,S)\le\psi(r_{F_T}(u)),\qquad
r_{F_T}(u)=\lambda^{-1}\inf_{Tx=u}\|x-u\|,
\tag{8}
\]

只要 F_T(u) 非空；空纤维的残差按 infinity 处理。这里用到 psi 连续非降，**不是只控制某个选中残差**。同样，(3) 与 F_T 的全部图点对 RL 只是输入坐标的同一公式。

这不是新的 inverse-graph 原理；新工作如果做成，应当在后续稠密性/范畴结论上体现增量。

## 3. 空间完备性、紧性与共同收敛区

### 3.1 度量和完备性

在 C(E,E) 上取

\[
d_{\rm loc}(T,U)=
\sum_{j=1}^{\infty}2^{-j}
\min\{1,\sup_{\|x\|\le j}\|Tx-Ux\|\}.
\tag{9}
\]

该度量刻画紧集上一致收敛。其 Cauchy 序列在每个闭球上一致 Cauchy，局部极限相容并连续，因此完备。条件 (2)–(4) 均可逐点取极限，故 X 是闭子空间，因而完备。

更强地，X 是紧的：(3) 给出共同局部模

\[
\|Tx-Ty\|\le h(\|x-y\|),\qquad
h(t)=\tfrac12(t+Lt^\gamma),\quad t\le R.
\tag{10}
\]

又有 T0=0。把从 0 到任一 x 的线段拆成长度至多 R 的有限段，即得每个闭球上所有 T 的共同有界性。Arzela–Ascoli 加可数对角线取子列证明局部一致序列紧性。因此 X 紧致且可度量，特别是 Polish 和 Baire。非空性必须另核；第 6 节给出同层的好、坏实例。

### 3.2 共同吸引域不是额外猜测

令 V = {x : d(x,S) ≤ rho}。对 x ∈ V，取最近点 s ∈ S，由 (3)

\[
\|Tx-x\|\le h(d(x,S)).
\]

结合 (1)、(4)，有 d(Tx,S) ≤ kappa d(x,S)，因此 T(V) ⊂ V。所有 T ∈ X 与 x ∈ V 都满足

\[
d(T^kx,S)\le \rho\kappa^k,
\]

\[
\|T^kx-\Pi_Tx\|\le
\frac{\rho\kappa^k}{2(1-\kappa)}
 +\frac{L\rho^\gamma\kappa^{\gamma k}}
 {2(1-\kappa^\gamma)}=:E_k\longrightarrow0.
\tag{11}
\]

这同时给出每条轨道收敛、统一尾界、同一个工作管域。初值落在固定有界集时，整个轨道还留在一个共同更大的有界集内。

### 3.3 T ↦ Pi_T 连续

若 T_n → T 局部一致，固定有限 k 时 T_n^k → T^k 在 V 的每个紧集上一致。这可由有限次复合、共同轨道有界性及 (10) 归纳得到。随后用

\[
\|\Pi_{T_n}-\Pi_T\|_B
\le 2E_k+\|T_n^k-T^k\|_B
\tag{12}
\]

先固定大 k，再令 n → infinity。于是

\[
X\longrightarrow C_{\rm loc}(V,S),\quad T\longmapsto\Pi_T
\]

连续。Pi_T|S=I，因此它是连续回缩。若不用仿射 S，而任意指定 K、S，则必须先确保 S 是 K 的回缩：例如不能要求球连续回缩到球面。随便固定一个多解集合可能把模型空间变成空集。

## 4. 至多二值：不闭，但仍可以保留 Baire 性

F_T(u) 的元素与 T^{-1}(u) 的元素一一对应。因此“F_T 每点至多二值”等价于“T 至多二对一”。

对整数 j,m ≥ 1，设

\[
Q_{jm}=\{(x_1,x_2,x_3)\in\overline B_j^3:
\min_{a<b}\|x_a-x_b\|\ge1/m\}.
\]

该集合紧。定义

\[
a_{jm}(T)=\min_{Q_{jm}}
\max_{a<b}\|Tx_a-Tx_b\|,
\]

空的 Q_{jm} 对应自动满足的条件。函数 a_{jm} 对闭球上一致范数连续，故 U_{jm}={T:a_{jm}(T)>0} 开。于是

\[
X_{\le2}=X\cap\bigcap_{j,m\ge1}U_{jm}. \tag{13}
\]

因为任何三个不同同像点都落在某个 Q_{jm}，(13) 精确刻画至多二值，并非充分近似。它是 X 中的 G_delta。

G_delta 子空间可以用等价完备度量：把 U_{jm} 枚举为 U_n，令 f_n(T)=1/dist(T,X\\U_n)，忽略空补集，并取

\[
d'(T,U)=d_{\rm loc}(T,U)+
\sum_n2^{-n}\min\{1,|f_n(T)-f_n(U)|\}.
\tag{14}
\]

d'-Cauchy 序列首先在 X 中收敛；每个 f_n 的 Cauchy 性阻止极限落到 X\\U_n，随后逐项与尾项估计证明 d' 收敛。故 X_{≤2} 可完全度量且 Baire。**不能从“不闭”就推断“不能做 Baire”。**

原来的 d_loc 限制度量未必完备；这可以在第 6 节的同一个严格证书层内验证。取 q_n=1/(4n)，令

\[
T_n(z,p,r)=(z+\sqrt{|r|},\ p,\ q_n|r|)
\longrightarrow T_0(z,p,r)=(z+\sqrt{|r|},\ p,\ 0).
\tag{14a}
\]

收敛在每个有界集上一致。每个 T_n 的逆纤维至多两点；T_0 在任意 (z,p,0) 处的逆纤维却包含全部

\[
\{(z-\sqrt{|r|},p,r):r\in\mathbb R\}.
\]

共同证书核验如下：S=R^2×{0}、lambda=1、gamma=1/2、psi(t)=t^2/4，且 q_n≤1/4。反射第三坐标 2q_n|r|−r 的 Lipschitz 常数至多 3/2，所以对 delta=||x−y||≤R，

\[
\|2(T_nx-T_ny)-(x-y)\|
\le2\sqrt\delta+\tfrac32\delta
\le(2\sqrt2+\tfrac32\sqrt R)\sqrt\delta.
\]

全空间输出 EB 也使用同一个 psi，因为

\[
d(T_nx,S)=q_n|r|\le\tfrac14|r|
\le\tfrac14\|x-T_nx\|^2.
\]

取第 6 节相同的小 R，严格兼容因子仍为 kappa_R<1；T_0 也满足这些共同证书。因此 X_{≤2} 在此 X 中确实不闭，d_loc 的限制确实可能不完备。以上 G_delta 论证依赖有限维有界闭球紧性；无限维 Hilbert 空间不能原样照搬。

“恰好二值于某个指定开集、接缝处恰好一值”是更细的分支结构条件，不能自动用 (13) 代替。若非研究所必需，第一轮不必强行固定这种精确分支计数。

## 5. 好类与坏类的 Borel 结构

为研究本稿的局部解选择，以下取 S 为真仿射子空间，固定 s∈S，并取实际的完整初值邻域

\[
B=\overline B_\varepsilon(s),\qquad
0<\varepsilon\le\min\{\rho,1/2\}.
\tag{14b}
\]

于是 B⊂V，且 diam(B)≤1；它包含法向和切向初值，不只包含解点。下面的 Borel 表达式对任意紧 B 也成立，但不能把退化的 B 当作稠密性挑战：特别是 B⊂S 时 Pi_T|B=I，对每个 T 都 Lipschitz，故 Bad(B)=empty。对 alpha > 0 和整数 m ≥ 1 定义

\[
H_{\alpha,m}(B)=
\{T:\ \|\Pi_Tx-\Pi_Ty\|\le m\|x-y\|^\alpha
\ \text{for all }x,y\in B\}. \tag{15}
\]

由 (12)，每个 H_{alpha,m}(B) 在 X（以及相对 X_{≤2}）中闭。故

\[
\mathrm{Lip}(B)=\bigcup_m H_{1,m}(B)
\]

是 F_sigma；

\[
\mathrm{Hol}_{>0}(B)=\bigcup_{n,m\ge1}H_{1/n,m}(B)
\tag{16}
\]

也是 F_sigma。使用指数 1/n 足够：任何 alpha > 0 都控制某个更小的 1/n。其补集

\[
\mathrm{Bad}(B)
=\bigcap_{n,m}(X\setminus H_{1/n,m}(B))
\tag{17}
\]

是 G_delta。

如果研究“在解点 s 的每个完整邻域内都无任意正阶两点 Hölder 性”，取 B_j=closed ball(s,epsilon_j) ⊂ V、epsilon_j ↓ 0，再对 j 可数交即可，同样是 G_delta。

注意，这里坏的是**完整邻域上的两点正则性**。固定 s ∈ S 的锚定 calmness 仍由 RLEB 长度界成立，不能把它改成“Pi_T 在解点完全不连续”。

对 (14b) 这种实际完整初值邻域，下一步若能证明每个闭集 H_{1/n,m}(B) 都没有相对内点，则它们全为无处稠密，Bad(B) 为余稀稠密 G_delta。当前报告只证明集合表达式，**没有证明这条扰动结论**。稠密也不等于余稀；G_delta 也不自动等于稠密。

## 6. 同一证书层可同时容纳稳定与不稳定选择

以现稿几何例子为基准，S=R^2×{0}、lambda=1、gamma=1/2、psi(t)=t^2/4，使用共同的

\[
L_R=2\sqrt2+\tfrac32\sqrt R.
\]

取充分小 rho=R，使

\[
\kappa_R=\frac{(2\sqrt2+\frac52\sqrt R)^2}{16}<1.
\]

坏模型是已经审核的

\[
T_{\rm bad}(z,p,r)=
\left(z+\sqrt{|r|},\ p+\sqrt{\min\{p_+,|r|\}},\ |r|/4\right).
\tag{18}
\]

相同证书层中有去掉 cap 切向增益的模型

\[
T_{\rm good}(z,p,r)=
\left(z+\sqrt{|r|},\ p,\ |r|/4\right),
\qquad
\Pi_{\rm good}(z,p,r)=
\left(z+2\sqrt{|r|},\ p,\ 0\right).
\tag{19}
\]

该 Pi_good 在有界集上 1/2-Hölder，且多解并未消失。其完整算子纤维为 y≥0 时

\[
F_{\rm good}(\xi,\eta,y)=
\{(-2\sqrt y,0,3y),\ (-2\sqrt y,0,-5y)\},
\]

y<0 时为空。反射差上界不大于 (18) 的共同 L_R；残差平方至少 4y，故同一个 psi 生效。因此这并不是通过把所有算法改成“唯一解/常值选择”来制造好类。它也说明已有反例只证明坏类非空，并不判定该类大不大。

## 7. 候选拓扑比较

| 空间/拓扑 | 完备或 Baire 情况 | 对本问题的评价 |
|---|---|---|
| 固定紧域 K 上 C(K,K) 的一致范数 | 目标 K 闭则完备；固定证书闭层仍完备；固定 Hölder 常数时常可用 Arzela–Ascoli 得紧性 | 最简单的局部版本；必须先证明 K 对所有允许算子共同不变。若只编码 K 中输入，其完整 resolvent 仅在 K 满域，不能伪称全空间 PPA |
| 本报告的 C_loc(R^d,R^d) 固定证书层 | 已给出紧、完备、Baire 证明；加入至多二值后为可完全度量 G_delta | **最推荐**；保留全空间完整纤维和原几何构造 |
| 用完整 resolvent 定义的 metric | 在逆图编码类中与上一行完全等价 | 自然算子距离。若只比较局部 resolvent，则两个不同全局图可能距离 0，需要取商，不能冒称图空间的 metric |
| 全部闭图的 Attouch–Wets/PK 图收敛 | 有限维闭图全空间有完备度量；但 full single-valued resolvent 子类不自动闭 | 适合图几何解释，单独使用太弱；应固定统一 RL、coverage 和 EB 层 |
| 固定紧域 K 上 C^{0,gamma}(K,R^d) 的范数，或全空间 C_loc^{0,gamma} 的局部半范数 | 前者是 Banach；后者用逐紧集 Hölder 半范数构成完备 Fréchet 空间；相应闭约束子类完备 | 全空间 T|S=id 在 S 无界时不属于通常的全局有界 C_b^{0,gamma}，不能直接称本报告的 X 是该 Banach 空间子集。也可明确选定参考 T_* 后研究仿射差空间 T_*+C_b^{0,gamma}，但这是另外限定的扰动类。强拓扑的范畴结论与 compact-open 不等价 |
| little-Hölder 空间（光滑映射闭包） | 是闭 Banach 子空间，常有可分性优势 | 会排除真正的 sharp gamma 尖点，如 |r|^gamma；可能预先排除本稿特色，不宜默认选用 |
| Mosco/凸 epi/Moreau-envelope topology | 在凸函数/最大单调适当类有成熟完备性与 resolvent 收敛定理 | 一般 F_T 未必为 subdifferential，更不一定 maximal monotone；强行放进凸 epi 类改变了问题 |
| 无限维 Hilbert 上 uniform-on-bounded-sets | 固定有界性/连续性类可做完备空间；但不再有有限维紧性和上述有限纤维 G_delta 的紧元组证明 | 可作第二阶段，不是检验当前 idea 的必要起点 |

在本报告 X 中，图拓扑并非另一个随意的选择。线性变换 (6) 把 resolvent 图和算子图对应起来；统一 RL 带来共同等度连续，输入满域且锚点固定，因此局部一致收敛与该层中的有限维图收敛相容。也可以直接利用 X 紧、图空间 Hausdorff 以及图编码连续且单射，得到其像上的同胚。离开固定层不能套用此结论。

## 8. 不能漏掉的失稳机制/最小例子

**完整 resolvent 不是任意图极限的闭性质。** 令 F_n(u)=(-1+1/n)u，lambda=1，则 J_{F_n}(x)=nx 全空间单值；图极限 F(u)=−u 却有 J_F(0)=R，x≠0 时为空。固定 RL 常数与 coverage 的作用是排除此类退化。

**“每个算法都有几何收敛”不等于共同尾界。** T_n(x)=(1−1/n)x 都收敛到 0，但极限 T=I 不再具有相同零集或共同衰减率。固定 kappa<1 而非允许 kappa_n ↑1 是必要的建模决定。

**非唯一零点不能只写存在量词。** F_n(u)=u(u−1/n) 有两个零点，极限 u^2 只剩一个；未固定分离尺度的“至少两个零点”不是闭条件。直接固定 S 并通过 EB 排除额外零点更干净。

**半代数性不随任意一致极限保持。** 多项式可一致逼近非半代数连续函数。不能因此直接判半代数子空间非 Baire，但必须单独证明所选固定格式/度数/参数层的拓扑性质。若坚持“全部半代数、全部次数”，未经分析的可数并不是一个自动合法的完备环境。第一轮建议先在 X_{≤2} 中做 category；半代数构造负责给出显式 witness，另设有限参数模型讨论 Lebesgue 几乎处处。

**Baire 与概率不是同义词。** 在 X 上可以指定很多概率测度，但没有未说明的“均匀随机 RLEB 算子”。范畴结果不能直接翻译成零概率/概率一，也不能从有限维参数取样推出整个 X 的范畴大小。

## 9. 已核到的原始/权威文献与精确适用范围

1. **Xianfu Wang, “Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent,” Nonlinear Analysis 87 (2013), 69–82, arXiv:1301.6443.** 本轮直接读了原文。Propositions 2.1、2.3、2.4 建立 nonexpansive/resolvent/maximal-monotone 的完备度量空间；Theorems 2.15、2.16 给 resolvent super-regular 和唯一零点的 residual 结论。[原文](https://arxiv.org/pdf/1301.6443)

   对应：这是“在算子空间用 Baire 比较性质大小”的直接先例。未覆盖：保留指定多解 S 的 gamma<1 RLEB 子类及 Pi_T 的非 Hölder 泛性。尤其其唯一零点结论会让极限选择退化成常值，不能当作本问题的答案。

2. **R. T. Rockafellar and Roger J.-B. Wets, Variational Analysis (1998).** 本轮直接核到 Theorem 4.42（非空闭集的完备 set-distance）；Theorem 5.50（有限维闭图映射的可分、完备、局部紧图距离）；Theorem 12.32（最大单调图收敛与 resolvent 收敛）；Theorem 12.35（凸函数 epi 收敛、subgradient 图收敛及规范化条件的对应）。[作者公开原书](https://sites.math.washington.edu/~rtr/papers/rtr169-VarAnalysis-RockWets.pdf)

   对应：说明 AW/PK 与 resolvent metric 的标准来路。未覆盖：任意非单调多值算子的一步满域/唯一性、共同 RLEB 余量或无限次极限选择稳定性；这些在本报告中另作证明。

3. **Chayne Planiden and Xianfu Wang, “Strongly convex functions, Moreau envelopes and the generic nature of convex functions with strong minimizers,” arXiv:1507.07144.** Theorem 3.2 和 Proposition 3.5 给 Moreau-envelope/凸函数度量的完备性。[原文](https://arxiv.org/html/1507.07144v1)

   对应：可参考其“先做完备环境，再做 category”的路线。未覆盖：本稿的非势函数 inverse-graph 算子，不能因形式上写了 proximal 就转入这个凸函数空间。

文献 1–3 是方法与边界先例，不是本报告 category 新定理的优先权认证。上面 compactness、全纤维、G_delta 与 F_sigma 的陈述均给了独立证明；尚未声称其中标准拓扑步骤具有原创性。

## 10. 可行性与推荐的下一项具体任务

**可行：** 固定非单点 S、固定 gamma/L/psi/lambda 与 kappa<1，使用 X_{≤2} 和 compact-open resolvent topology；先问 Bad(B) 是否稠密、是否余稀。这个问题不是空泛口号，闭层 (15) 把目标拆成可以逐个攻击的命题。

**高风险：** 同时要求全空间完整纤维、至多二值、严格 EB、固定 RL 常数、半代数性与任意小扰动。现有局部坏模型未必能植入任意基准算子，拼接可能破坏 all-pairs RL 或引入更小残差纤维。证明密度需要真正的新保结构拼接，不是把一个坏例缩小后粘上去。

**现阶段不可宣称：** “RLEB 坏类是第一纲/余稀/零测/满测”；“在全部算子空间得到泛性就能限制到 RLEB 或半代数子类”；“只要选择某个弱拓扑就能证明坏类大”。

最有价值的下一步是一个明确的扰动挑战：固定第 5 节 (14b) 的实际完整初值邻域 B（不允许退化为 B⊂S），给定 T_0 ∈ X_{≤2}、任意 compact-open 邻域 U、整数 n,m，能否找到 T ∈ U∩X_{≤2} 及 x,y ∈ B，使

\[
\|\Pi_Tx-\Pi_Ty\|>m\|x-y\|^{1/n}?
\]

若能对全部 n,m 和全部 U 做到，就得到真正的坏选择余稀定理；若做不到并能识别非空开稳定层，则得到同样有内容的结构分区。两种结局都比“存在一个坏例，所以坏类很大”严谨，也都切合用户提出的 idea。
