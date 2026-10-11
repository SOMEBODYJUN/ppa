# 同预算完成的严格插值余量、有限证书与对称障碍

本页固定整个局部数据，接续 C233–C237。C238 排除有限点强迫零点的路线；C239 排除 RP² 的一类自然公式；C240 将给定预算的全域保零存在性化成带覆盖和严格余量的有限证书。三者均不证明非单点原预算总能保零，也不认证发表优先。独立重构和攻击范围见[接收记录](../audit/COMPLETION_BUDGET_REVIEW_2026_10_11.md)。

<a id="cbg-lens"></a>
## C238-v1 · 严格雪花插值纤维有内部

**精确对象。** 任意实 Hilbert 空间 H，非空紧集 A⊂H，0<γ<1，L>0；C_A:A→H 满足全部点对的同预算条件
\[
\|C_A(p)-C_A(q)\|\le L\|p-q\|^\gamma.
\tag{BG1}
\]
对任意 x∉A，定义
\[
\mathcal K_L(x)=\bigcap_{p\in A}\overline B(C_A(p),L\|x-p\|^\gamma),\quad
d=d(x,A)>0,\quad R=\max_{p\in A}\|x-p\|,
\]
\[
b=\frac{d^{2\gamma}}{4\Gamma(1-\gamma)(\log4)^\gamma},\qquad
\eta=\frac{Lb}{R^\gamma+\sqrt{R^{2\gamma}-b}}>0.
\tag{BG2}
\]
则存在 v∈H，使闭球 \(\overline B(v,\eta)\subset\mathcal K_L(x)\)。这给所有原锚约束的统一正余量，常数无需最优。

**证明：雪花中的严格凸包间隙。** 用 [HE-SNOWFLAKE](holder_extension.md#he-snowflake) 的 Hilbert 嵌入 J，令 \(\|Jp-Jq\|^2=\|p-q\|^{2\gamma}\)。对任意有限概率权重 α_i 和 p_i∈A，设 z=Σα_iJp_i。方差恒等式给
\[
\|Jx-z\|^2=\sum_i\alpha_i\|x-p_i\|^{2\gamma}
-\frac12\sum_{i,j}\alpha_i\alpha_j\|p_i-p_j\|^{2\gamma}.
\tag{BG3}
\]
HE2 的 Laplace 表示把右端化为
\[
\frac{c_\gamma}{2}\int_0^\infty E_t t^{-1-\gamma}\,dt,
\quad c_\gamma=\frac\gamma{\Gamma(1-\gamma)},
\quad E_t=1-2\sum_i\alpha_i e^{-t\|x-p_i\|^2}
+\sum_{i,j}\alpha_i\alpha_j e^{-t\|p_i-p_j\|^2}.
\tag{BG4}
\]
Gaussian 核正定，故 E_t≥0。对 t≥(log4)/d²，第二项绝对值≤1/2，末项非负，故 E_t≥1/2。积分得到 BG3≥b。有限和的积分收敛来自 HE2，不需交换无限概率积分。

令 Q=闭凸包 J(A)。取闭包后仍有 \(h^2=d(Jx,Q)^2\ge b>0\)。Hilbert 投影 a=P_QJx 满足，对全部 p∈A，
\[
\|a-Jp\|^2\le\|Jx-Jp\|^2-h^2.
\tag{BG5}
\]
C_A 在 J(A) 上是 L-Lipschitz；[HE-EXTENSION](holder_extension.md#he-extension) 的 Kirszbraun 导入给 G 在雪花 Hilbert 空间上的同常数延拓。置 v=G(a)，则
\[
\|v-C_A(p)\|\le L\sqrt{\|x-p\|^{2\gamma}-b}.
\tag{BG6}
\]
因为 Q 包含 J(A)，h²≤d^{2γ}，根号良定。函数 u−√(u²−b) 在 u≥√b 上递减；BG6 到每个约束球边界的径向余量至少
\(L(R^\gamma-\sqrt{R^{2\gamma}-b})=\eta\)。三角不等式完成证明。固定同一个 G 后，x↦G(P_QJx) 本身是全域同 L、同 γ 的 Hölder 延拓：P_Q 非扩张，J 是雪花等距，且原锚 Jp∈Q。这个特定延拓具有 BG6 的严格原锚余量，但没有保证全域无新增固定点；任意逐点选择的可行中心仍不自动成对兼容。

**有限点推论。** 任意有限 S⊂H\A，可按任意次序逐点选择严格内点，保持全部 A↔S、S↔S 的同 L 约束，并令 C(x)≠x (x∈S)。每一步锚集仍紧、距新点正，且 H 非零；可从正半径球内避开指定单点。再经 HE-EXT 得全域同预算延拓。有限点值还可全部取严格兼容：对有限 S 存在统一 σ>0，使
\[
\|w_i-C_A(p)\|\le L\|x_i-p\|^\gamma-\sigma
\quad(p\in A),
\qquad \|w_i-w_j\|<L\|x_i-x_j\|^\gamma\quad(i\ne j).
\tag{BG7}
\]
每步选到球内距边界正，紧锚与有限步使最小余量正。推论不保证整个管外没有固定点。γ=1、L=0 或非紧锚集不能直接套 BG2。

<a id="cbg-symmetry"></a>
## C239-v1 · RP² 的符号共轭对称迫使新增固定点

固定 C234 的原数据：H=Sym₀(3) (Frobenius 范数)，M={qqᵀ−I/3:||q||=1}，ρ=1/8，N=闭ρ管，
\[
T_0(p)=\Pi(p)+d(p,M)^2(p-\Pi(p)),\qquad C_0=2T_0-\operatorname{Id}.
\tag{BG8}
\]
令 K={diag(ε₁,ε₂,ε₃):ε_i=±1,Πε_i=1}，通过正交共轭作用。任意保整个 C₀ 的全域有限 γ-Hölder 完成 Ĉ，若满足 K-等变，则其 T=(Id+Ĉ)/2 必有管外固定点。

**证明。** 固定空间 E=H^K 是二维无迹对角平面，等变性使 Ĉ(E)⊂E。在闭管内投影唯一；对角矩阵的最近秩一投影取最大特征值的坐标轴。因此
\[
N\cap E=\bigcup_{i=1}^3\overline B_\rho^E(m_i),\quad
m_i=e_ie_i^\top-I/3,\quad \|m_i-m_j\|=\sqrt2\ (i\ne j).
\tag{BG9}
\]
三盘分离；盘内 \(\Pi(p)=m_i\)，限制位移为
\[
\operatorname{Id}-T_0=(1-\|p-m_i\|^2)(p-m_i).
\tag{BG10}
\]
每盘的平面内局部指数是 +1。限制到 E 的有限 γ-Hölder 完成是次线性的，故足够大平面圆周上位移次数为 1。删去三盘后的总次数为 1−3=−2，非零次数迫使额外固定点。若新增平面固定点有限，它们的 **E 内**指数之和为 −2；没有五维环境指数 −2 的声称。

**公式禁区。** 若固定单个实对称矩阵 B，并要求模板同时共轭协变
\[
\Phi(QpQ^\top;QBQ^\top)=Q\Phi(p;B)Q^\top,\qquad Q\in SO(3),
\quad\widehat C(p)=\Phi(p;B),
\tag{BG11}
\]
B 的稳定子包含某个共轭 K。原 N、C₀ 具有全部共轭对称；在旋转后的固定平面重复 BG9–10，仍强迫新增零点。允许再增大有限 L 也无效。全部 SO(3) 对称更直接迫使 Ĉ(0)=0。

经典固定子空间不变性可见 [Golubitsky–Schaeffer 1982 Lemma 1.3，印页84](../LITERATURE.md#lit-gs-1982)；本页将其与指定整管和次线性次数合同组合，不声称该机制首创。

**尚未排除的结构。** 两个矩阵如 B₁=diag(1,2,−3)、B₂ 对角为0且全部非对角元为1，共同正交稳定子仅 {±I}，其共轭作用平凡；这只移除上述障碍。一个有向向量在 SO(3) 下的稳定子是 SO(2)：其平凡子群的 M 固定集为 RP²；C₂ 的固定集为轴点⊔RP¹；C_m (m≥3) 或 SO(2) 的固定集为轴点，Euler 特征全为1。必要 Euler 门没有排除它，亦没有证明等变完成存在。若要求 O(3) 协变且向量为普通极向量，其稳定子 O(2) 包含与 K 相同的有效符号共轭作用：取轴为 e₃，diag(ε₁,ε₂,1) 固定该极向量，必要时把 K 的成员换成负矩阵，其共轭作用不变。不能从 BG11 推“至少两个偏置”。

<a id="cbg-certificate"></a>
## C240-v1 · 给定预算保零完成的有限网证书等价

固定 C233 的整管合同于 H=Rⁿ (n≥2)：非空紧无边界 C² 嵌入流形 M，0<ρ<reach(M)，N=闭ρ管，T₀ 固定 M 且 d(T₀p,M)≤θd(p,M)，0≤θ<1。给定 0<γ<1、L>0 且 [C₀]_(γ,N)≤L，C₀=2T₀−Id。**这里不预设 χ(M)=1 或管外连通。** 选择任意 m∈M 和
\[
a=2(1-\theta)\rho,\quad
R>\max\{\max_{p\in N}\|p-m\|,\ L^{1/(1-\gamma)}\},\quad
s>0\text{ 使 }s+Ls^\gamma<a,
\]
\[
\mathcal A=\{x:\|x-m\|\le R,\ d(x,N)\ge s\}.
\tag{BG12}
\]
A 是有限维紧管外过渡集。以下三个条件等价：

1. 存在全域 Ĉ 保整个 C₀、[Ĉ]_γ≤L 且 Fix((Id+Ĉ)/2)=M。
2. 存在 h>0、A 中去重复的真实有限 h-网 {x_i} 和值 v_i，满足全部原锚约束及全部新点对约束
   \[
   \|v_i-C_0(p)\|\le L\|x_i-p\|^\gamma\quad(p\in N),\qquad
   \|v_i-v_j\|\le L\|x_i-x_j\|^\gamma,
   \]
   \[
   \min_i\|x_i-v_i\|>h+Lh^\gamma.
   \tag{BG13}
   \]
3. 存在 h,δ>0、A 的真实有限 h-网 {x_i}、N 的真实有限 δ-网 {p_j} 和值 v_i，满足新点对约束及 BG13 的位移下界，并满足有限锚条件
   \[
   \|v_i-C_0(p_j)\|\le L\|x_i-p_j\|^\gamma-2L\delta^\gamma
   \quad\text{对全部 }i,j.
   \tag{BG14}
   \]
若 A=∅，2、3 用空新点证书；BG13 的最小值条件不适用。任取 N 的有限 δ-网即可。有限证书仍要求真实几何覆盖和给定 C₀ 的可靠求值，不是随机样本的名称。

**2⇒1：三块覆盖。** HE-EXT 给在 N∪{x_i} 上同 L 数据的全域延拓。固定点 x 满足 Ĉ(x)=x，而 Ĉ(m)=m，因此 x≠m 时
\(\|x-m\|^{1-\gamma}\le L\)，所以全部固定点在半径 R 内。管外 d(x,N)=t≤s 时，最近 p∈∂N；距离函数的1-Lipschitz性给
\[
\|p-C_0(p)\|=2\|p-T_0(p)\|\ge a,
\quad \|x-\widehat C(x)\|\ge a-t-Lt^\gamma>0.
\tag{BG15}
\]
其余可能的新增固定点在 A。取距离≤h 的网点，三角不等式给
\(\|x-\widehat C(x)\|\ge\|x_i-v_i\|-h-Lh^\gamma>0\)。N 中除 M 外没有固定点，由严格距离收缩直接得到。三块排除全部新增零点，且结论对任何该数据的同预算延拓成立。

**1⇒2。** A≠∅ 时，连续位移在紧 A 上的最小值 μ>0。选 h 使 h+Lh^γ<μ，再取真实有限 h-网及 v_i=Ĉ(x_i)，得到 BG13。有限维紧性是此步的承重条件。

**3⇒2：两项锚误差。** 任意 p∈N，选 ||p−p_j||≤δ。原数据 Hölder 模贡献 Lδ^γ；雪花距离差满足
\(|\|x_i-p_j\|^\gamma-\|x_i-p\|^\gamma|\le\delta^\gamma\)，再贡献 Lδ^γ。BG14 的 2Lδ^γ 正好消去两项误差，得到全部 p∈N 的 BG13。

**1⇒3：严格化有限数据，而非极限偷换。** 在 1⇒2 中先选 h，使 h+Lh^γ<μ/2。用 C238 的有限点推论构造 w_i 满足 BG7 的统一严格原锚余量 σ>0 与新点对严格兼容。置 v'_i=(1−ε)v_i+εw_i。范数凸性保持全部新旧同预算约束，并给原锚余量 εσ。取足够小 ε>0，仍有 min_i||x_i−v'_i||>h+Lh^γ。最后选 δ 使 2Lδ^γ<εσ，任意真实有限 δ-网给 BG14。这个凸混只修改有限新增点值；原整个 C₀ 未改变。证毕。

**范围。** 等价没有保证证书必存在：χ 或逐分量缺额不兼容时三项全假。BG14 在存在性层面把无限原锚约束变成有限严格证书；取得覆盖、预算上界、求值误差和求解非凸位移约束的算法仍需另做。某个粗网求解失败、浮点不可行或普通有限点可避零，均不能证明原预算完成失败。无限维紧集 A、γ=1、L=0 不在本命题内。

<a id="cbg-next"></a>
## 下一门：下确界、达到与严格预算缺口分开

用 C234 的 **同一** RP²、ρ=1/8 和整个 T₀ 作压力测试。固定 γ (可先取1/2)，记 L₀=[C₀]_(γ,N)，定义
\[
L_* = \inf\{[\widehat C]_\gamma:\widehat C|_N=C_0,
\ \operatorname{Fix}((\operatorname{Id}+\widehat C)/2)=M\}.
\tag{BG16}
\]
C233 保证此集合非空且 L_* 有限，限制给 L_*≥L₀。首攻门是：是否对每个 ε>0 有预算 L₀+ε 的 BG14 证书？这等价 L_*=L₀，**不等价端点达到**。端点达到还需 L₀ 证书或独立的保正余量极限证明；保零条件不随一致极限自动保持。若主攻失败，须给同一整管数据的解析严格 gap 或一个有可认证预算的新常数构造，不把求解器停滞称为反例。

结构支线只有在预算/位移不等式或可计算模型明确时启动：可试 SO(3) 有向向量或双矩阵，但先排除 BG11 模板。C235 要求任何 RP² 次线性保零完成留下管外无固定点紧不变动力；不能顺手加全域距离趋零合同。一般 ENR、精确 L₀ 数值、单点 forced-zero 搜索和仅换论文标题暂不承担主线。
