# PA-EXAMPLES：两个主文正例与定量常数审计

项目：RL-CONIC-2026。路线：理论类。受派 gate：T4/T5 examples gate。日期：2026-09-09。

审计角色：SCI-Skills pre-submission-review；模式 REVIEW / PROMPT。本报告是有界专家返回，不关闭或推进任何阶段。

## 1. 结论与输入边界

建议主文保留且只充分展开两个正例：

| 正例 | 推荐固定数据 | 实际展示作用 | 不应声称的作用 |
| --- | --- | --- | --- |
| E-SOC：耦合双 SOC | 既有 §6.3 的三变量模型，欧氏乘积范数 | 单块严格方向均存在、联合严格方向不存在；共同非线性约束面；联合 CRSC 和可计算角常数 | 不是“单块误差界可直接相交”；不是新型应用模型；不是只有本定理可解 |
| E-PSD：高维 proper face | 既有 §6.4 取任意 k≥3，C₀=[e₁,e₂]、D₀=[e₂,e₃] | S₊^{k+2} 中维数 k(k+1)/2 的非多面 proper face；非零混合项；σ 与 η 的抵消 | 不是新的 PSD amenability 结果；不是随 k 改善的最优常数 |

两个例子均有完整的直接闭像、minimal face、CRSC、amenability 证明，且通用常数全部可计算。另给独立的显式可行点修复，证明指定球半径上的实际误差界。后者防止把通用定理中的“充分小邻域”误报成已计算半径。

四份指定材料已完整审阅：

1. `output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md`，尤其 §2、§4.2–5.2、§6.1–6.4。
2. `output/AUDIT_CRSC_MSCQ_SMOOTH_STRICT_CONES.md`，尤其 §4 的常数与 §6–7 的比较边界。
3. `output/EXTENSION_CRSC_MSCQ_SMOOTH_STRICT_CONES.md`，尤其 §4、§6–8。
4. `output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md`，尤其 §3–6A。

另读取已有 `output/verify_product_cone_crsc_mscq.py` 以确定其核验范围；本次不把“文件记载已运行”冒充本次运行。本报告的新恒等式、具体参数选择与直接修复界均是可逐步复核的数学推导（AI_INFERENCE），不是实验数据。本次未做新的文献搜索，未对既有文件的外部引文作独立来源复核，亦不作优先权结论。

## 2. 全部范数、对象与常数先固定

所有向量采用欧氏范数，矩阵采用 Frobenius 范数，输入和输出乘积均采用正交乘积范数。特别不能把 PSD 独立坐标的未加权向量范数与 Frobenius 范数混用。

令 C 为输出锥，A=DG(0)，

\[
F=F_{\min}(\operatorname{Im}A\cap C),\quad H=F^\perp,
\quad U=\operatorname{Im}(P_HA),\quad D=\overline{P_HC}.
\]

CRSC 的两部分是 A*C* 闭，以及固定 H 上 DG(x)* 的秩在一个开邻域内恒定。正对偶约定为 C*={y:⟨y,c⟩≥0 对所有 c∈C}。

采用已有定理的参数：

\[
\sigma=\sigma_{\min}^+(P_HA),\qquad
\eta=\min_{u\in U,\ \|u\|=1}d(u,D),\qquad
b=\frac4{\sigma\eta},
\]

\[
\tau_F=d_{\operatorname{span}F}(Ad_0,\operatorname{rbd}F),\qquad
c=\frac4{\tau_F},\qquad
\kappa_{\rm th}=b+c\,a_F(1+L_Gb),
\]

其中 d₀ 是共同约束面 M={P_HG=0} 在原点的单位切向量且 Ad₀∈ri F；a_F 只需对应这个 F。

**解释限制：**σ、η、τ_F 是原点量；L_G 必须在一个给定邻域上界定。即使这些量均已闭式算出，通用证明仍需将常秩坐标和路径纳入一个更小邻域。仅给 κ_th 并不自动给出这一更小半径。

## 3. E-SOC：联合约束而非单块推理

### 3.1 精确数据与可行集

取 Q₃={(a,b,c):a≥√(b²+c²)}，C=Q₃×Q₃，x=(s,t,u)，参考点为零，

\[
v=(1,1,0),\quad n=(1,-1,0),\quad e=(0,0,1),\quad h=u-st,
\]

\[
G_1=sv+hn+h^2e,\qquad G_2=tv-hn+2h^2e.
\tag{S1}
\]

因 n∈Q₃*=Q₃，⟨n,G₁⟩=2h、⟨n,G₂⟩=−2h。联合可行性强迫 h=0；此时两个约束分别等价于 s≥0、t≥0。因此全局有

\[
\Omega=\{(s,t,u):s\ge0,\ t\ge0,\ u=st\}.
\tag{S2}
\]

这是一片弯曲、非孤立、带相对边界的共同可行集。

### 3.2 minimal face 与闭像：不必在例子中再借助 Pataki

\[
A(\alpha,\beta,\gamma)=(\alpha v+\gamma n,\ \beta v-\gamma n).
\]

同样的 n 配对先给 γ=0，再给 α,β≥0。故

\[
\operatorname{Im}A\cap C=F=\mathbb R_+v\times\mathbb R_+v,
\quad \dim F=2,
\quad F^\triangle=\mathbb R_+n\times\mathbb R_+n.
\]

更强的直接闭像公式为

\[
A^*C^*=\mathbb R_+^2\times\mathbb R.
\tag{S3}
\]

证明：像的前两坐标为 ⟨v,y₁⟩、⟨v,y₂⟩，必非负。反过来给定 a,b≥0 和 z∈R，令 z₊=max{z,0}、z₋=max{−z,0}，取

\[
y_1=(a/2)v+(z_+/2)n,\qquad
y_2=(b/2)v+(z_-/2)n.
\]

二者属于 Q₃，且 A*(y₁,y₂)=(a,b,z)。故像闭。另有

\[
A^*F^\triangle=A^*H=\mathbb R(0,0,1).
\]

### 3.3 CRSC 在完整邻域成立

H=v⊥×v⊥，且

\[
P_HG=(hn+h^2e,\ -hn+2h^2e)=q(h),
\]

\[
q'(h)=(n+2he,\ -n+4he),\qquad
\|q'(h)\|^2=4+20h^2>0.
\]

Dh=(-t,−s,1) 永不为零，所以 D(P_HG)=q′(h)Dh 的秩处处为一。这验证的是联合 normal rank，不是把两个块各自的结果相加。共同约束面为 M={u=st}。

单独第一块在方向 (1,0,1) 上的导数为 v+n=(2,0,0)∈int Q₃；单独第二块可用 (0,1,−1)。联合严格方向不存在：第一块严格可行导数要求 γ>0，第二块要求 γ<0。

### 3.4 amenability 与全部通用参数

用单位正交基 v̂=v/√2、n̂=n/√2、e。单块的 normal 投影闭包是

\[
\overline{P_{v^\perp}Q_3}
=\{a\widehat n+ze:a\ge0,\ z\in\mathbb R\}.
\tag{S4}
\]

这是闭包而不一定是原投影：写完整向量为 λv̂+an̂+ze，SOC 条件为 λ,a≥0 和 2λa≥z²。a>0 时可通过增大 λ 容纳任意 z；a=0 时原投影只能有 z=0，而闭包允许任意 z。

于是 U=span{(n,−n)}，其两个单位方向为 ±(n,−n)/2。到 D 的距离均为 1/√2，而 P_HA 的唯一非零奇异值为 2。因此

\[
\sigma=2,\quad\eta=1/\sqrt2,\quad b=2\sqrt2.
\]

取 d₀=(1,1,0)/√2；它在 ker D(P_HG)(0) 中且为单位向量。Ad₀=(v̂,v̂)，在 span F 的正交坐标中为 (1,1)，因此 τ_F=1、c=4。

对单条射线 R₊v̂，−v̂ 的 SOC 投影为零。由一维齐次性，在该射线张成的直线上 d(y,R₊v̂)=d(y,Q₃)。正交乘积给出 a_F=1；这不是输入误差界的分块相交论证。

在输入球 B_R 上记 H_R=R+R²/2。由 |h|≤H_R、s²+t²≤R²，以及 (Δs v,Δt v) 与 q′(h)DhΔx 的正交性，

\[
\|DG(x)\|^2\le 2+(4+20H_R^2)(1+R^2).
\tag{S5}
\]

选 R=1/4 时，右侧为 32485/4096<9，因此 L_G=3 是该球上的有效上界。这给出

\[
\boxed{\kappa_{\rm th}=4+26\sqrt2}
\tag{S6}
\]

在某个充分小的球上有效。此处尚未通过通用坐标证明确定该球的数值半径，不能仅据 (S6) 声称半径就是 1/4。

### 3.5 独立的显式半径验证，不冒充最优常数

记 a²=s₋²+t₋²，其中 s₋=max{−s,0}、t₋=max{−t,0}，r=d(G(x),C)。由于 Q₃ 包含在 v̂、n̂ 的两个非负配对半空间的交中，这两方向又相互正交，对两个输出块分别取距离下界得

\[
r^2\ge 2(s_-^2+t_-^2+h^2)=2(a^2+h^2).
\tag{S7}
\]

给出显式可行点 x⁺=(s₊,t₊,s₊t₊)。当 ||x||≤R 时，

\[
|st-s_+t_+|
\le |t|s_-+s_+t_-
\le \sqrt{t^2+s_+^2}\,a\le Ra.
\]

所以三角不等式给

\[
\|x-x^+\|\le \sqrt{a^2+h^2}+Ra
\le(1+R)\sqrt{a^2+h^2}\le\frac{1+R}{\sqrt2}r.
\]

因此在明确的 B_{1/4} 上，

\[
\boxed{d(x,\Omega)\le\frac5{4\sqrt2}d(G(x),C).}
\tag{S8}
\]

(S8) 比通用 (S6) 小，反映通用两次修复常数的保守性，不反驳其有效性。没有声称二者为最优模量，也没有把最近可行点等同于所构造的 x⁺。

## 4. E-PSD：任意高维的非多面 proper face

### 4.1 参数完全固定

令 k≥3，输入空间 X=S^k×R，范数为 √(||B||_F²+u²)。参考点 (0,0)，输出锥 C=S₊^{k+2}。设

\[
C_0=[e_1,e_2],\qquad D_0=[e_2,e_3],\qquad J=\operatorname{diag}(1,-1),
\]

\[
h=u-\operatorname{tr}(B^2)=u-\|B\|_F^2,
\qquad
G(B,u)=\begin{pmatrix}
B & hC_0+h^2D_0\\
hC_0^T+h^2D_0^T & hJ
\end{pmatrix}.
\tag{P1}
\]

对所有 k≥3，||C₀||_F²=||D₀||_F²=2，⟨C₀,D₀⟩_F=0；两个交叉系数均非零。最紧凑的主文实例可选 k=3，即 S₊⁵ 中一个六维 proper face，再注明 k 任意。

下方 2×2 主块的 PSD 性迫使 h=0；反向显然。所以精确可行集为

\[
\Omega=\{(B,u):B\succeq0,\ u=\|B\|_F^2\}.
\tag{P2}
\]

### 4.2 minimal face、闭像与 CRSC

\[
A(E,t)=\begin{pmatrix}E&tC_0\\tC_0^T&tJ\end{pmatrix}.
\]

PSD 性强迫 t=0，故

\[
\operatorname{Im}A\cap C
=F=\left\{\begin{pmatrix}E&0\\0&0\end{pmatrix}:E\succeq0\right\}.
\tag{P3}
\]

F 是一个 proper face：它由 diag(0_k,I₂) 的零配对暴露，并且等距同构于 S₊^k。其维数为 k(k+1)/2。k≥2 时它不是多面锥：rank-one PSD 矩阵沿无穷多方向给出不同极射线；有限生成锥不具此性质。

对于对称块矩阵 Y=(P Z; Zᵀ W)，

\[
A^*Y=(P,\ 2\langle C_0,Z\rangle+\langle J,W\rangle).
\]

若 Y≽0 则 P≽0。给定任意 P≽0、z∈R，选择 Z=0、W=diag(z₊,z₋) 即得 A*Y=(P,z)。因此有直接闭像公式

\[
\boxed{A^*C^*=S_+^k\times\mathbb R.}
\tag{P4}
\]

同时

\[
H=\left\{\begin{pmatrix}0&Z\\Z^T&W\end{pmatrix}\right\},\quad
F^\triangle=\left\{\begin{pmatrix}0&0\\0&W\end{pmatrix}:W\succeq0\right\},
\]

\[
A^*F^\triangle=A^*H=\{0\}\times\mathbb R.
\]

令 q(h)=P_HG，则

\[
q'(h)=\begin{pmatrix}0&C_0+2hD_0\\C_0^T+2hD_0^T&J\end{pmatrix},
\quad \|q'(h)\|_F^2=6+16h^2>0.
\]

Dh(E,t)=t−2⟨B,E⟩，其 u 分量恒为 1。故 D(P_HG)=q′(h)Dh 的秩处处为一，CRSC 全局成立。共同约束面是 M={u=||B||_F²}，而非各矩阵项分开定义的约束面。

### 4.3 角常数需要 projected cone 的闭包

这里有精确公式

\[
D=\overline{P_HS_+^{k+2}}
=\left\{\begin{pmatrix}0&Z\\Z^T&W\end{pmatrix}:W\succeq0,\ Z\in\mathbb R^{k\times2}\right\}.
\tag{P5}
\]

必要性由下主块 PSD 得到。充分性：对任意右侧 Z,W，用 W+εI₂ 代替 W，取顶块 Z(W+εI₂)^{-1}Zᵀ 即得 PSD 完整矩阵；其 H 投影在 ε↓0 时逼近指定矩阵。原投影对于奇异 W 会额外限制 Z，而其闭包不再有该限制。

设

\[
N=q'(0)=\begin{pmatrix}0&C_0\\C_0^T&J\end{pmatrix}.
\]

其 Frobenius 范数平方为 6。P_HA(E,t)=tN，故 σ=√6，U=span{N}。到 D 的投影可完全保留交叉块，只把下方 W 投影至 S₊²；±J 均有且仅有一个模为 1 的负特征值。因此

\[
d(\pm N/\sqrt6,D)=1/\sqrt6,
\quad\eta=1/\sqrt6,\quad b=4.
\tag{P6}
\]

σ 与 η 抵消是这个例子的展示点：交叉 normal 项不能被忽略，但其带来的 normal 长度与归一化角度在 b 中抵消。

### 4.4 amenability、内点余量与 L_G

若 Y∈span F，则 Y=diag(E,0)，其到整个 PSD 锥的投影恰为 diag(E₊,0)∈F。由此直接得 a_F=1。

取单位切向量 d₀=(I_k/√k,0)。Ad₀=diag(I_k/√k,0)，到 F 相对边界的 Frobenius 距离是最小特征值 1/√k。因此

\[
\tau_F=1/\sqrt k,\qquad c=4\sqrt k.
\tag{P7}
\]

在 B_R⊂X 中，|h|≤H_R=R+R² 且 ||Dh||²≤1+4R²。顶块增量 diag(E,0) 与 q′(h)Dh(E,t) 正交，所以

\[
\|DG(B,u)\|^2\le 1+(6+16H_R^2)(1+4R^2).
\tag{P8}
\]

R=1/4 时右侧为 669/64<(13/4)²，故 L_G=13/4 是给定球上的有效上界。代入通用公式，

\[
\boxed{\kappa_{\rm th}=4+56\sqrt k.}
\tag{P9}
\]

与 SOC 一样，(P9) 仅通过通用定理保证某个充分小球；必须区分 L_G 的计算球与最终修复路径的有效球。

### 4.5 显式可行点修复核验半径

写 B=B₊−B₋ 为正负谱部分，a=||B₋||_F，r=d(G(B,u),S₊^{k+2})。对任意完整 PSD 比较矩阵 Y，其上主块和下主块均为 PSD。丢掉非负的交叉块距离项后取下确界，得

\[
r^2\ge d(B,S_+^k)^2+d(hJ,S_+^2)^2=a^2+h^2.
\tag{P10}
\]

构造 (B⁺,u⁺)=(B₊,||B₊||_F²)∈Ω。谱部分正交，所以

\[
u-u^+=h+a^2,\qquad
\|(B,u)-(B^+,u^+)\|=\sqrt{a^2+(h+a^2)^2}.
\]

若 ||(B,u)||≤R，则 a≤R。因此

\[
\sqrt{a^2+(h+a^2)^2}
\le\sqrt{a^2+h^2}+a^2
\le(1+R)\sqrt{a^2+h^2}\le(1+R)r.
\]

所以不依赖任何未量化坐标半径，在 B_{1/4} 上明确成立

\[
\boxed{d((B,u),\Omega)\le\frac54d(G(B,u),S_+^{k+2}).}
\tag{P11}
\]

此界对本例所有 k≥3 有效。它说明 (P9) 的 √k 增长属于所选一般内点方向与证明常数，不是本例已证明的必要维度障碍。没有宣称 (P11) 最优。

## 5. 常数的主文速查表

| 量或结论 | E-SOC | E-PSD，k≥3 |
| --- | --- | --- |
| 输入范数 | R³ 欧氏范数 | S^k Frobenius × R |
| minimal face | R₊v×R₊v | diag(S₊^k,0₂) |
| face 维数 | 2 | k(k+1)/2 |
| normal rank | 1，处处成立 | 1，处处成立 |
| A*C* | R₊²×R | S₊^k×R |
| a_F | 1 | 1 |
| σ | 2 | √6 |
| η | 1/√2 | 1/√6 |
| b | 2√2 | 4 |
| τ_F | 1 | 1/√k |
| c | 4 | 4√k |
| B_{1/4} 上的 L_G 上界 | 3 | 13/4 |
| 通用 κ_th，充分小邻域 | 4+26√2 | 4+56√k |
| 直接证明、明确在 B_{1/4} 上成立的 κ | 5/(4√2) | 5/4 |

建议正文列 σ、η、τ_F、a_F 和 κ_th；直接修复证明可紧接成一段“calibration remark”，或放附录。它们验证定理常数的可计算性与非最优性，不构成另外两个主要定理。

## 6. 哪些只应列为直接推论；双曲锥 gate

### 6.1 p-cone 与产品覆盖

“有限 amenable cone 产品”和“所有 PSD face 的 a_F=1”是已有一般定理加已知/自证锥几何的直接推论，不能按锥的数量累计新贡献。

可在 E-SOC 后加一条不展开的变体：把两个 SOC 换成 C_p³×C_q³，1<p,q<∞，仍用 (S1)，例如 p=4、q=3/2。轴向向量 v,n 同时属于相应 primal 和 positive dual cones，因此最小面、闭像 (S3)、恒秩和精确可行集证明均保留；两个垂直半空间仍给 (S7)，所以直接误差界 (S8) 同样保留。这是 nonsymmetric/nonsmooth-second-order 范围的展示，而非新证明机制。

此变体的射线特意选在坐标轴方向，故 v̂ 也在对偶锥中，可有 a_F=1。**不能**推广成一般 p-cone 边界射线均有 a_F=1；原材料的 δ_v=d(−v,C_p) 因子对一般非自对偶射线仍不可删除。本报告不借此变体提出 C² reduction 的声明；apex 下固定 identity reduction 足够。

原单 p-cone 抛物线 g=(0,h,h²) 适合留在假设比较附注，说明非 cone-concave 与既有 sequential 条件的边界。它的 MSCQ 可由等价等式直接得到，且已有材料明确撤回“首次 facial/sequential separation”的优先权说法；不宜再把它当第二个核心正例。

### 6.2 双曲锥不进入当前主文例子清单

四份已核验输入没有提供一个具体的非 PSD 双曲锥实例、完整面描述、给定非线性 G、闭像证据以及该 face 的可用 a_F。故本次不接受泛称“所有双曲锥”或泛称“适用双曲优化”的额外推论。

若未来要保留一个双曲锥例子，必须另开有界任务并返回以下闭合证据：确切双曲多项式及方向；正确的 pointed/full-dimensional reduced cone；固定 minimal face；niceness 或等价闭像依据；CRSC 的完整邻域证明；该 face 的 amenability 不等式和 a_F；如非 apex，还需固定 reduction 及原始残差转移。不得只凭“它是双曲锥”补齐任何一项。

这一删除是证据包的范围决定，不是断言某类双曲锥不 amenable，也不是新的负面定理。PSD 正例已独立闭合，不必另贴“双曲”标签虚增应用家族。

## 7. 三个审稿视角、风险与最小修补

| 视角 / 位置 | 证据与问题 | 严重性 | 最小修补 | 理想修补 |
| --- | --- | --- | --- | --- |
| Contribution：既有 §6.1–6.4 | 类别覆盖与两个模型均可直接应用总定理，不能分别充当独立新定理 | MODERATE | 称为 corollaries / illustrations；保留真正新增的联合 normal 修复接口 | 与具体外部模型建立经核验的接口；本任务不扩大此范围 |
| Methods：既有 §6.4 常数未固定 | 任意 C₀,D₀ 与矩阵范数未固定时，数值参数不可唯一复现 | MODERATE | 采用 (P1) 和 Frobenius 规范 | 允许参数化附件，但明确范数和交叉内积 |
| Methods：通用 κ 之后 | 原点几何量不给自动数值有效半径 | MAJOR，若误报完整半径 | 写“some sufficiently small neighborhood” | 保留 (S8)/(P11) 给本例显式半径证明 |
| Methods：D 的计算 | SOC 和 PSD 的原 normal 投影通常非闭 | MAJOR，若删闭包 | 使用 (S4)/(P5)，包括逼近构造 | 附一段说明闭包为何是角定义不可缺少的一部分 |
| Communication：维度增长 | κ_th 的 √k 不能解释成问题的必要维度恶化 | MODERATE | 并列直接界 5/4 | 若研究 sharp modulus，另开任务而非暗示已完成 |
| Contribution：hyperbolic scope | 本次材料中没有具体闭合证据 | MAJOR，若加入普遍推论 | 不纳入当前主文 | 在新任务下逐项满足 §6.2 checklist |

总体 examples readiness：**CONDITIONALLY_READY**。数学数据和两组常数可合并为 PASS_CANDIDATE；条件在于正文必须保留上述主文口径，不从例子推出新颖性、全局结论、最优模量、RL 高阶指数或未核验锥类覆盖。阶段裁决只归 orchestrator。

## 8. 证明任务状态与执行证据

| 证明任务 | 状态 | 定位 |
| --- | --- | --- |
| E-SOC exact feasible set、minimal face、joint closed image | 已完成数学推导 | (S2)–(S3) |
| E-SOC 全邻域 CRSC、两块独立 strict / 联合 non-strict | 已完成数学推导 | §3.3 |
| E-SOC amenability、σ、η、τ_F、L_G | 已完成数学推导 | §3.4 |
| E-SOC explicit-radius direct bound | 已完成数学推导 | (S7)–(S8) |
| E-PSD exact feasible set、proper nonpolyhedral face、closed image | 已完成数学推导 | (P2)–(P4) |
| E-PSD normal closure 与角常数 | 已完成数学推导 | (P5)–(P6) |
| E-PSD a_F、τ_F、L_G 与显式半径 | 已完成数学推导 | (P7)–(P11) |
| 常数有理算术及固定矩阵关系复算 | 已实际执行 | `verify_examples_constants.py` |
| 有限点 SOC residual / feasible repair sanity checks | 已实际执行，非证明替代 | 257 个固定有理网格点 |
| 对角 PSD direct-bound algebra sanity checks | 已实际执行，非一般 PSD 数值投影 | 617 个固定有理组合 |
| 最优模量、全球文献优先权、双曲锥额外覆盖 | 未执行，不在本任务结论内 | 保持开放 |

实际运行命令：

```text
python3 output/conic_paper/verify_examples_constants.py
```

退出码 0。脚本使用 Python 标准库；未安装软件、未调用第三方 API。精确断言核对 SOC 的 32485/4096<9 与 PSD 的 669/64<(13/4)²，并检查 normal 长度、参数抵消等恒等式。有限点检查只作 sanity check；闭包、所有邻域点和任意维数的结论依赖本报告的证明。

并行核心证明审计者 `/root/conic_core_proof_audit` 已独立交叉核验并同意两个例子的 σ、η、b、τ_F、c 计算，尤其确认 PSD 投影闭包的交叉块自由性与 Frobenius 权重。这是推导复核记录，不是外部文献或数值实验。

## 9. 标准专家返回

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review
project_id: RL-CONIC-2026
paper_family: theoretical
stage_id: "T4/T5 examples gate"
task_id: PA-EXAMPLES
task_status: COMPLETE
inputs_reviewed:
  - output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md
  - output/AUDIT_CRSC_MSCQ_SMOOTH_STRICT_CONES.md
  - output/EXTENSION_CRSC_MSCQ_SMOOTH_STRICT_CONES.md
  - output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md
  - output/verify_product_cone_crsc_mscq.py
outputs:
  - output/conic_paper/EXAMPLES_AND_CONSTANTS_AUDIT.md
  - output/conic_paper/verify_examples_constants.py
evidence_status:
  - VERIFIED_USER_MATERIAL: four assigned source reports read completely
  - AI_INFERENCE: explicit closed images, minimal faces, CRSC and amenability proofs
  - AI_INFERENCE: SOC and PSD normal-angle constants and theorem constants
  - AI_INFERENCE: explicit feasible repairs prove radius-one-quarter bounds
  - EXECUTED_LOCAL: standard-library exact constants and deterministic sanity checks; exit code zero
  - PENDING_VERIFICATION: worldwide priority and any separate hyperbolic-cone extension
assumptions:
  - fixed apex representation at zero
  - Euclidean vector norms and Frobenius matrix norms with orthogonal products
  - SOC data as S1
  - PSD data as P1 with k at least three
author_input_needed: []
manual_actions: []
quality_checks:
  - two positive examples with different face geometry
  - no blockwise input-error-bound intersection inference
  - exact closed adjoint images proved without a new literature dependency
  - cone-projection closure retained in angle computation
  - theorem constants distinguished from explicit-radius direct bounds
  - no optimal-constant or numerical-experiment claim
  - corollaries separated from proposed novelty
  - unclosed hyperbolic-cone claims excluded
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: merge E-SOC and E-PSD with the norm conventions and the theorem-constant versus direct-radius distinction intact
stage_acceptance_recommendation: PASS_CANDIDATE
```

唯一下一步：由 orchestrator 将 E-SOC 与 E-PSD 合入例子节，并保留“通用局部常数”与“显式半径直接界”的区别。
