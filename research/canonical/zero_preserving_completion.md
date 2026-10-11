# 保零集完成的充分性与全局吸引的不同障碍

本模块接续 [C231](topological_completion_balance.md#tcb-balance)，基线为 `68278d15ef5268dbc4f95c49a761c80a21d01766`，日期 2026-10-11。C233–C235 在下述精确范围为 `derived-checked`，三路独立重构和最终正文接收均未发现现存 fatal objection；审查范围见[接收记录](../audit/ZERO_PRESERVING_COMPLETION_REVIEW_2026_10_11.md)。三个合同始终分开：保整个局部完整近端映射；保全部零集；全部初值趋近零集。允许增加有限 Hölder 常数与保原常数也分开。经典 Hopf 延拓和流形同调不是新发现；这里记录它们在完整关系合同中的推导。

<a id="zpc-data"></a>
## 共享对象

沿用 TC1–TC3：有限维 \(H=\mathbb R^n\)、步长 \(\lambda>0\)，非空紧嵌入无边界 \(C^2\) 流形 \(M\)，闭投影管
\[
N_\rho=\{p:d(p,M)\le\rho\},\quad0<\rho<\operatorname{reach}(M).
\]
指定连续 \(T_0:N_\rho\to N_\rho\)，逐点固定 \(M\)，满足
\(d(T_0p,M)\le\theta d(p,M)\)，\(0\le\theta<1\)。
整管 \(C_0=2T_0-\operatorname{Id}\) 为某个 \(L>0,0<\gamma<1\) 的 Hölder 映射。固定整管而不是缩小管，也不是仅固定零集或轨道。令 \(D_0=\operatorname{Id}-T_0=(\operatorname{Id}-C_0)/2\)，其管内零集恰 \(M\)。

每个全域 Cayley 完成对应完整原关系
\[
\widehat T=(\operatorname{Id}+\widehat C)/2,\qquad
\operatorname{gph}\widehat F
=\{(\widehat T(p),(p-\widehat T(p))/\lambda):p\in H\}. \tag{Z1}
\]
图点的 Minty 输入唯一等于 \(p\)，所以完整 \(J_{\lambda\widehat F}=\widehat T\)，且 \(\operatorname{zer}\widehat F=\operatorname{Fix}\widehat T\)。没有要求 \(\widehat F\) 单值。

<a id="zpc-sufficiency"></a>
## C233-v1 · 连通管外时，Euler 条件足以完成（允许新常数）

**精确陈述。** 在共享对象下，增加 \(n\ge2\)：存在大闭球 \(\overline B_R\) 包含 \(N_\rho\) 于其内部，且
\(W=\overline B_R\setminus\operatorname{int}N_\rho\)
连通。则以下等价：

1. \(\chi(M)=1\)。
2. 存在全域 \(\gamma\)-Hölder \(\widehat C\)，有某个有限常数 \(\widehat L\)，满足 \(\widehat C|_{N_\rho}=C_0\)，且 \(\operatorname{Fix}\widehat T=M\)。
3. 存在上述完成，且 \(\widehat C\) 紧支撑。

不声称 \(\widehat L=L\)，也不声称给出最佳或可计算的新常数。每个分量余维至少二时满足连通管外条件，包括不连通的 \(M\)。不将总次数条件用于不连通的 \(W\)。

**明确导入。** Hopf degree-zero extension theorem：紧、连通、定向 \(n\) 维带边界流形 \(W\) 的连续边界映射 \(g:\partial W\to S^{n-1}\) 可延拓到 \(W\)，当且仅当整个边界按诱导定向计算的总次数为零。边界不必连通。Tammo tom Dieck, *Differential Manifolds*, §2.10(2.10.1)，印页 74 / PDF p.74–75，[作者 PDF](https://www.uni-math.gwdg.de/tammo/GT03.pdf)；连续边界数据用同伦和边界 cofibration 保持原值。A. Freire, *Notes on Manifolds*, “Extension Theorem”，印页 74–75，[作者 PDF](https://web.math.utk.edu/~afreire/teaching/m562s26/notes_on_manifolds.pdf)，明确写出 continuous / smooth 和 connected \(W\)。\(C^2\) 管的带边界流形可使用同胚平滑模型，不改边界映射和次数。球值延拓是单一外部接口，不依赖未写清的 obstruction 猜测。

**证明。**

**必要性。** 2⇒1 是 C231；3⇒2 显然。

**球值延拓。** 在 \(\partial W=\partial B_R\sqcup(-\partial N_\rho)\) 上给定
\[
g(p)=
\begin{cases}
D_0(p)/\|D_0(p)\|,&p\in\partial N_\rho,\\
p/R,&p\in\partial B_R.
\end{cases} \tag{Z2}
\]
边界位移非零。欧氏环境的固定点指数等于位移 \(p-T_0p\) 的 Brouwer 次数；C231 的局部指数为 \(\chi(M)\)。管边界无固定点，故该次数可在整个 \(N_\rho\) 计算。外球次数为 1，内边界在 \(W\) 的定向反转，因此
\[
\deg(g|_{\partial W})=1-\chi(M)=0. \tag{Z3}
\]
\(W\) 是紧连通定向 \(n\) 流形，\(S^{n-1}\) 与边界维数相同，全部 Hopf 条件成立。得到连续 \(e:W\to S^{n-1}\)，原样取边界值 \(g\)。

**正幅度。** 边界指定 \(a=\|D_0\|\) 于内边界、\(a=R/2\) 于外边界，有正最小值。延拓连续 \(\log a\) 到 \(W\)，再取指数，得正连续 \(a\)。于是 \(D=ae\) 在 \(W\) 无零，内边界等于 \(D_0\)，外边界等于 \(p/2\)。记 \(m=\min_W\|D\|>0\)。

**Hölder 提升且原样保管。** 不能假定任意连续 \(e\) 自动 Hölder。调用既有 [HE-EXT](holder_extension.md#he-extension)，取得整管 \(C_0\) 的全域同常数 Hölder 延拓 \(C_b\)，置 \(D_b=(\operatorname{Id}-C_b)/2\)。在内边界 \(D_b=D\)；在外边界 \(p/2=D\)。由紧性和连续性，选两个不交的薄边界 collar，在内 collar 有 \(\|D_b-D\|<m/4\)，在外 collar 有 \(\|p/2-D\|<m/4\)。

紧 \(W\subset\mathbb R^n\) 上的连续向量函数 \(D\) 可由光滑向量函数 \(A\) 一致逼近到 \(\|A-D\|<m/4\)（逐坐标多项式逼近即可）。取分别支撑在两个 collar 的 Lipschitz cutoff \(\eta_i,\eta_o\)，各在相应边界的更薄邻域为 1，支撑不交。置
\[
D_h=\eta_iD_b+\eta_o(p/2)+(1-\eta_i-\eta_o)A. \tag{Z4}
\]
每个被加权函数在权重非零处距 \(D\) 小于 \(m/4\)，所以此凸混合满足 \(\|D_h-D\|<m/4\)，\(\|D_h\|\ge3m/4>0\)。它在内边界邻域精确等于 \(D_b\)，外边界邻域精确等于 \(p/2\)。定义
\[
\widehat C(p)=
\begin{cases}
C_0(p),&p\in N_\rho,\\
p-2D_h(p),&p\in W,\\
0,&p\notin B_R.
\end{cases} \tag{Z5}
\]
接缝两侧在一个邻域已有同一 Hölder 公式：内侧是 \(C_b\)，外侧是零。紧区域上，Lipschitz cutoff 乘有界 Hölder 函数仍 Hölder；光滑 \(A\) 和线性函数在紧集也为同指数 Hölder。有限邻域覆盖给 Lebesgue 数 \(\delta>0\)，小于 \(\delta\) 的点对有统一局部界，更远点对由 \(2\sup\|\widehat C\|\delta^{-\gamma}\) 控制。因此全域有限 \(\widehat L\) 存在，且紧支撑。在整管保存动力和固定点 \(M\)；在 \(W\) 位移为 \(D_h\ne0\)，外部为 \(p/2\ne0\)。得 1⇒3。

**余维二的连通性。** 每个分量余维至少二时，球内路径可一般位置扰动到不碰 \(M\)：路径维数 1 与 \(M\) 维数之和小于 \(n\)。在管内把非零法向半径向外推到 \(\rho\)，得 \(\overline B_R\setminus M\to W\) 的连续回缩；这一步完全在球内部的管中进行。因此 \(W\) 路径连通。证毕。

**量词边界。** 对每个给定整管数据的存在结论。逼近依赖该次连续延拓的正余量 \(m\)，不是全体数据的统一常数。若 \(W\) 不连通，必须逐分量满足次数零。

<a id="zpc-rp2"></a>
## C234-v1 · 不可缩但可保零完成的真实 RLEB 模型

取 \(H=\operatorname{Sym}_0(3)\)，实对称无迹三阶矩阵，Frobenius 内积，维数 5。令
\[
M=\{qq^\top-I/3:q\in S^2\}. \tag{Z6}
\]
映射恰识别 \(q\sim-q\)。导数 \(h\mapsto qh^\top+hq^\top\)，\(h\perp q\)，平方范数 \(2\|h\|^2\)，给商流形 \(\mathbb{RP}^2\) 的单射浸入；紧性给光滑嵌入。每点平方范数 \(2/3\)。standard cellular chain 在 0,1,2 维各一个胞腔，\(\partial_2=2,\partial_1=0\)，所以
\[
\chi(M)=1-1+1=1,\qquad H_1(M;\mathbb Z)=\mathbb Z/2.
\]
\(M\) 不可缩。接口见 Hatcher, *Algebraic Topology*, Example 2.42，印页 144 / PDF p.153；也见 Example 2.4，印页 106–107。

**显式投影窗。** Rayleigh 原理给
\[
\|p-(qq^\top-I/3)\|_F^2=\|p\|_F^2+2/3-2q^\top p q. \tag{Z7}
\]
若 \(d(p,M)<1/2\)，写 \(p=qq^\top-I/3+E\)，\(\|E\|_F<1/2\)。最大与次大特征值之差至少 \(1-2\|E\|_{op}>0\)：最大/次大 Rayleigh 极值各改变不超过 \(\|E\|_{op}\)。唯一最大特征线给唯一最近投影
\(\Pi(p)=q_{max}q_{max}^\top-I/3\)，光滑依赖 \(p\)。故 \(\operatorname{reach}(M)\ge1/2\)，只给下界，不称精确 reach。

固定 \(\rho=1/8\)。整个 \(N_\rho\) 上置
\[
T_0(p)=\Pi(p)+d(p,M)^2[p-\Pi(p)]. \tag{Z8}
\]
法向射线在 reach 管保持同一投影，所以
\[
\Pi(T_0p)=\Pi(p),\qquad d(T_0p,M)=d(p,M)^3\le\rho^2d(p,M). \tag{Z9}
\]
\(C_0\) 光滑于稍大管，在紧管 Lipschitz，故每个 \(0<\gamma<1\) 有有限全管 Hölder 常数。余维 3 给连通管外；C233 提供紧支撑全域完成，完整零集精确为不可缩 \(M\)。这是存在式全域完成，不宣称已经算出球值延拓的闭式公式。

**完整真残差，不能只用局部所选值。** 固定任意 \(\lambda>0\) 和任一上述完成，令 \(r_{\widehat F}(y)=\inf\{\|v\|:v\in\widehat F(y)\}\)。每个 \(y\in N_{\rho^3}\) 写 \(s=d(y,M)\)、\(r=s^{1/3}\le\rho\)。\(s>0\) 时管内唯一输入为
\[
p_{loc}=\Pi(y)+s^{-2/3}[y-\Pi(y)],\qquad
\|p_{loc}-y\|=r-r^3. \tag{Z10}
\]
\(s=0\) 时输入为 \(y\)。任意管外输入 \(p\notin N_\rho\)，即使映到 \(y\)，仍有
\[
\|p-y\|\ge d(p,M)-d(y,M)>\rho-s\ge r-r^3. \tag{Z11}
\]
所以没有域外图点能降低残差，精确得
\[
r_{\widehat F}(y)=(r-r^3)/\lambda,\qquad
d(y,\operatorname{zer}\widehat F)
\le\left(\frac{\lambda}{1-\rho^2}\right)^3 r_{\widehat F}(y)^3. \tag{Z12}
\]
这对完整输出纤维成立，允许增加大残差值。每个 \(q>3\) 的正系数同窗 EB 失败：沿非零法向 \(r\downarrow0\)，比值 \(r^3/[(r-r^3)/\lambda]^q\to\infty\)。因此指数 3 匹配且锐。

取 \(\gamma>1/3\)，\(q\gamma>1\)。同一完整关系有全对 RL、满输入覆盖、零锚和完整真 EB；有限 \(\widehat L\) 与三次 EB 在足够小尺度给既有直接兼容。也可不导入收敛定理：管内全部初值的完整唯一 PPA 保持投影，法向半径
\[
r_k=r_0^{3^k},\qquad p_k\to\Pi(p_0).
\]
步长沿同一法向单调，长度总和精确 \(r_0\)。这是真实非孤立零流形上的局部完整 PPA。

<a id="zpc-global"></a>
## C235-v1 · 加上全局趋近后，零流形必须可缩

**精确陈述。** 连续 \(T:H\to H\) 在整个管等于 \(T_0\)。若全部 \(x\in H\) 满足
\[
d(T^kx,M)\to0, \tag{Z13}
\]
则 \(M\) 可缩。无需逐点极限、有限长度或预给统一收敛率，也无需 Hölder/次线性。非空紧无边界光滑流形于是只能是单点：正维闭流形有非零顶维模二同调；非单点零维流形不连通。

**自足证明。** 取包含 \(M\) 的紧凸球 \(B\)。每个 \(x\in B\) 有时间 \(k_x\) 使 \(T^{k_x}x\in\operatorname{int}N_\rho\)。连续性给相对开邻域 \(U_x\subset B\)，其全部点同刻进入管。管前向不变，有限子覆盖的最大时间 \(N\) 给 \(T^N(B)\subset N_\rho\)。所以
\[
R=\Pi\circ T^N:B\to M
\]
是连续回缩，因为 \(T^N|_M=\operatorname{Id}\)。固定 \(b\in B\)，
\(H(m,t)=R((1-t)m+tb)\)
把恒等映射连续收缩到 \(R(b)\)。证毕。顶维模二同调接口见 Hatcher Theorem 3.26，印页 236。

**次线性完成的额外结论。** 若 \(M\) 不可缩，且 \(T=\widehat T\) 是全域有限次线性 Hölder 完成，则存在轨道永不进入 \(N_\rho\)：否则再一步由严格管收缩进入内管，同一有限覆盖证明成立。所有轨道有界：\(\|\widehat Tp\|\le(\|p\|+a+\widehat L\|p\|^\gamma)/2\)，大球不变，球外范数严格减小。该轨道有非空紧 \(\omega\)-极限集
\(K_\omega\subset\{d(\cdot,M)\ge\rho\}\)，正向包含由连续性给出；反向包含取趋向某个极限点的时间子列，再对前一时刻取有界收敛子列，故 \(T(K_\omega)=K_\omega\)。若极限集碰到闭管边界，下一步严格进入内管，亦与不变性及距离下界矛盾；故实际上 \(K_\omega\cap N_\rho=\varnothing\)，两紧集有正距离。若完整固定点集就是 \(M\)，则 \(K_\omega\) 不含固定点。不能据此声称存在周期点或混沌。

**C234 的组合。** 射影平面能同时保局部 RLEB 动力和完整零集；任何这样的有限次线性完成都留下某条管外有界非收敛轨道及无固定点的紧不变极限集。全局吸引是新加的合同，不能当作原 Q-TC 的反例。

<a id="zpc-frontier"></a>
## 已闭与仍开放

- 已闭：\(n\ge2\)、连通管外、允许某个有限新常数时的 Euler 必要充分性；RP² 的完整局部 RLEB；仅全域距离趋近就强迫可缩的独立合同。
- 开放：同一数据原常数 \(L\) 的精确保零完成；最小新常数与可计算无零余量；不连通管外的逐分量次数合同及定量实现；一般紧 ENR 的替代条件。
- 不能升级：存在式完成不等于可执行全局求解器；非收敛不等于存在周期；经典机制不授予发表优先；全图 RL 不授予全局 EB/兼容。

有限几何、矩阵投影、三次残差、边界与常数反算见 [复算入口](../code/zero_preserving_completion/README.md)。计算不证明 Hopf 定理、无限域量词或一般无零完成。

