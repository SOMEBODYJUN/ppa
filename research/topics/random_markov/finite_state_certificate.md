# 固定有限状态同步运输残差的精确顶点证书

<a id="fs-object"></a>
## 对象、量词和来源

固定互异点 \(G=\{g_1,\dots,g_N\}\subset\mathbb R^d\)、有限个自映射
\(T_a:G\to G\) 及权重 \(p_a\ge0,\sum_a p_a=1\)。随机映射的核为
\(P_{ij}=\sum_a p_a{\bf1}_{T_ag_i=g_j}\)，不变律的非空凸多面体
\(\mathcal I=\{\pi\in\Delta_N:P^\top\pi=\pi\}\)。定义成本矩阵
\[
C_{ij}=\|g_i-g_j\|^2,\quad
R_{ij}=\sum_a p_a\|(g_i-T_ag_i)-(g_j-T_ag_j)\|^2\ge0.
\tag{FS1}
\]
两个边缘 \(\mu,\pi\) 的 \(C\)-最优运输计划集记
\(\operatorname{Opt}_C(\mu,\pi)\)。固定**同一耦合与同一噪声**的残差、目标距离为
\[
\Phi(\mu)=\Psi(\mu)^2
 =\min_{\pi\in\mathcal I}\min_{\eta\in\operatorname{Opt}_C(\mu,\pi)}R\cdot\eta,
\quad E(\mu)=d_{W_2}(\mu,\mathcal I)^2
 =\min_{\pi\in\mathcal I}\min_{\eta\in\Pi(\mu,\pi)}C\cdot\eta.
\tag{FS2}
\]
内层 \(C\)-最优性不能删除；\(\Phi\) 中的目标 \(\pi\) 也**不必**是
\(E(\mu)\) 的最近不变律。所有结论仅对这组固定数据成立。

9/14 [有限状态来源](../../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/02_有限状态分类/有限状态_精确零集与线性误差界等价.md)
的 §§1–4、§7 报告此一般机制；先前 [CM-FINITE](../../cone_markov.md#m-fin)
与 C15 只有摘要。此页对**同一 C15 版本**重新给完整证明，
不审该来源的所有例子、优先权或复杂度说法。

<a id="fs-cells"></a>
## 有限 tight-edge 多面体恰好覆盖合法计划

考虑无固定边缘的运输对偶可行集
\[
D=\{(u,v):u_i+v_j\le C_{ij}\ (i,j=1,\dots,N),\ u_1=0\}.
\tag{FS3}
\]
它非空且没有直线：若 \((a,b)\) 为双向可行方向，则所有
\(a_i+b_j=0\)，再由 \(a_1=0\) 得全部为零。有限不等式给 D
有限多个顶点 \((u^k,v^k)\)；即使 D 无界，每个有有限最优值的
对偶最优面仍有顶点。令
\(H_k=\{(i,j):u_i^k+v_j^k=C_{ij}\}\)，并令 \(\mathcal F_k\) 是满足
\[
\eta\ge0,\quad\sum_{ij}\eta_{ij}=1,\quad
(P^\top-I)c(\eta)=0,\quad
\eta_{ij}=0\quad((i,j)\notin H_k)
\tag{FS4}
\]
的计划多面体，其中 \(r(\eta),c(\eta)\) 为行、列边缘。
每个非空 \(\mathcal F_k\) 紧且有有限顶点；记这些顶点的并为
\(\mathcal V\)。

**覆盖证明。** 若 \(\eta\in\mathcal F_k\)，其列边缘平稳，且
\(C\cdot\eta=u^k\cdot r(\eta)+v^k\cdot c(\eta)\)，对偶下界取等，
所以它是自身两边缘的 \(C\)-最优计划。反之，任意列边缘平稳的
\(C\)-最优计划有一个对偶顶点最优解；互补松弛使其正支撑落在
该顶点的 tight edges，故属于某个 \(\mathcal F_k\)。特别是
\[
\Phi(\mu)=\min_k\min_{\eta\in\mathcal F_k, r(\eta)=\mu}R\cdot\eta
\tag{FS5}
\]
（空分支忽略），极小值取得。\(\mathcal I\ne\varnothing\)：任意初律
的 Cesàro 平均在紧单纯形有子列极限，且其 \(P^\top\)-不变性误差
至多 \(2/n\)。对 \(\pi\in\mathcal I\)，对角计划 \(\eta_{ii}=\pi_i\)
最优，且 \(R_{ii}=0\)，因此 \(\Phi(\pi)=0\)。

<a id="fs-theorem"></a>
## C15-v1：精确零集、全域线性界和锐常数等价

以下三句等价：

1. \(\Phi^{-1}(0)=\mathcal I\)；
2. 对每个 \(v\in\mathcal V\)，\(R\cdot v=0\Longrightarrow r(v)\in\mathcal I\)；
3. 存在有限 \(B\ge0\)，对**全部** \(\mu\in\Delta_N\) 有
   \(E(\mu)\le B\Phi(\mu)\)。

若成立，精确的最小平方系数（\(W_2\le K\Psi\) 的 \(K^2\)）为
\[
B_* =\max_{v\in\mathcal V, R\cdot v>0}
             \frac{E(r(v))}{R\cdot v},
\qquad K_*=\sqrt{B_*},
\tag{FS6}
\]
空集的最大值约定为 0。可允许 \(N=1\) 或 \(\mathcal I=\Delta_N\)。

**证明。** 对固定 \(\mu\)，\(E(\mu)\) 是 \(C\)-成本在行边缘
\(\mu\)、列边缘属于凸集 \(\mathcal I\) 的计划上的最小值。
混合两个可行计划证明 \(E\) 在**整个** \(\Delta_N\) 上凸；
因互异状态的 \(W_2\) 是度量，\(E(\mu)=0\iff\mu\in\mathcal I\)。
注意没有断言 \(\Phi\) 凸。

取 \(\Phi(\mu)\) 的最优计划 \(\eta\in\mathcal F_k\)，写成该
多面体顶点的凸组合 \(\eta=\sum_v\alpha_vv\)。因为 \(R\ge0\)，
零成本顶点的 \(E(r(v))=0\) 由第二句保证；对正成本顶点用 (FS6)。
由 \(E\) 的凸性，
\[
E(\mu)\le\sum_v\alpha_v E(r(v))
\le B_*\sum_v\alpha_v R\cdot v=B_*\Phi(\mu).
\tag{FS7}
\]
这证第二句推出第三句；第三句与 \(\Phi|_{\mathcal I}=0\)
给第一句。若第一句成立，任意零成本顶点本身是 (FS5) 的合法
计划，\(\Phi(r(v))=0\)，故其行边缘在 \(\mathcal I\)：回到第二句。
最后任何可行系数 \(B\) 对每个正成本顶点满足
\(E(r(v))\le B\Phi(r(v))\le B R\cdot v\)，故 \(B\ge B_*\)。
当 \(B_*>0\) 时最大比顶点与 (FS7) 合成，实际
\(\Phi(r(v_*))=R\cdot v_*\)，从而取等；\(B_*=0\) 时
\(E\equiv0\)，\(\mathcal I=\Delta_N\)。证毕。

<a id="fs-boundary"></a>
## 意义和未跨越的门

若第二句失败，那个零成本顶点的行边缘就是一张**明确的假零律**证书；
这比有限随机搜索未找到反例强。若成立，得到的是固定有限系统的
全局 \(W_2\)-残差界，不是跨系统统一 \(K\)、收敛速度或平稳律唯一性。
例如 \(G=\{0,1\}\)、唯一自映射交换两个状态：\(\mathcal I\)
仅含公平律，\(E(\mu)=|\mu_0-1/2|\)，\(\Phi(\mu)=4E(\mu)\)，
所以 \(K_*=1/2\)；非公平律的迭代在它与翻转律之间周期振荡。
因此不能由 C15 的误差界直接推随机动力收敛。

本页证明有限顶点覆盖与锐常数，不依赖 Hoffman 界或 \(\Phi\) 的
连续性；来源中其它性质及外部新颖性仍待核。

<a id="fs-hoffman"></a>
## 同一 C15 的备用证明：零面与空零面分开处理

令 \(D=\max_{i,j}\|g_i-g_j\|\)，对每个非空分支 \(\mathcal F_k\)
置 \(Z_k=\{\eta\in\mathcal F_k:R\cdot\eta=0\}\)。假设 C15 的零顶点
判据成立。若 \(Z_k\ne\varnothing\)，[LIT-HOFFMAN-1952](../../LITERATURE.md#lit-hoffman-1952)
应用到定义 \(Z_k\) 的**固定系数矩阵且一致**的线性系统；对已经
属于 \(\mathcal F_k\) 的计划，唯一新增的等式违反量是非负的
\(R\cdot\eta\)。存在只依赖该固定分支数据的 \(H_k<\infty\)，使
\(\operatorname{dist}_1(\eta,Z_k)\le H_k R\cdot\eta\)。取最近的
\(\eta_0\in Z_k\)，零成本顶点判据及凸分解给
\(r(\eta_0)\in\mathcal I\)。有限状态的最大耦合及边缘化的
\(\ell^1\) 收缩给
\[
 E(r(\eta))\le W_2^2(r(\eta),r(\eta_0))
 \le {D^2\over2}\|r(\eta)-r(\eta_0)\|_1
 \le {D^2H_k\over2}R\cdot\eta .                 \tag{FS8}
\]
若 \(Z_k=\varnothing\)，**不可**对这个不一致系统调用 Hoffman；
紧性给 \(m_k=\min_{\eta\in\mathcal F_k}R\cdot\eta>0\)，且
\(E\le D^2\)，所以用 \(D^2/m_k\) 作该分支的系数。有限分支的
最大值再用于 (FS5) 的取到的最优计划，独立地证明 C15 中系数
**存在**，但通常不给 (FS6) 的锐值。\(D=0\) 的单状态情形两边
恒为零；无须除以 \(D\)。

<a id="fs-regularity"></a>
## C80-v1：固定有限系统的残差平方全局正则性

在 (FS1)–(FS2) 的固定数据下，\(\Phi=\Psi^2\) 在整个
\(\Delta_N\) 上是全局 Lipschitz 的连续分片仿射函数，**不要求**
零顶点判据、唯一不变律或 Markov 动力收敛；因此 \(\Psi\) 至少
全局 \(1/2\)-Hölder。此处的常数可以依赖所有固定状态、核和成本。

为逐项验证，先令 \(b=(\mu,\pi)\in\Delta_N^2\)，
\(w(b)=\min_{\eta\in\Pi(\mu,\pi)}C\cdot\eta\)。把旧最优计划的
两个坐标分别经最大耦合的转移核改成 \(\mu',\pi'\)：任一坐标
改变的概率不超过两项 total variation 之和，在改变事件上成本
变化绝对值至多 \(D^2\)。交换旧新方向得到
\[
 |w(b)-w(b')|\le {D^2\over2}\|b-b'\|_1.       \tag{FS9}
\]
最优计划集 \(\mathsf S(b)=\{\eta\ge0:A\eta=b,\ C\cdot\eta=w(b)\}\)
对每个 \(b\) 非空、紧。其不等式的**左端系数矩阵固定**，例如
堆叠为 \([-I;A;-A;C;-C]\)，右端只含 \(b,w(b)\)。对任意
\(\eta\in\mathsf S(b)\)，将 Hoffman 界
应用于一致的目标系统 \(\mathsf S(b')\)，得一个不依赖两对边缘
的有限常数 \(H\)，满足
\[
 \operatorname{dist}_1(\eta,\mathsf S(b'))
 \le H\bigl(\|b-b'\|_1+|w(b)-w(b')|\bigr)
 \le H(1+D^2/2)\|b-b'\|_1.                     \tag{FS10}
\]
反向同理。由于 \(R\cdot\eta\) 的 \(\ell^1\) Lipschitz 常数为
\(\|R\|_\infty\)，
\(h(\mu,\pi)=\min_{\eta\in\mathsf S(\mu,\pi)}R\cdot\eta\)
具有常数至多 \(L=\|R\|_\infty H(1+D^2/2)\)。对**同一个**紧
集合 \(\mathcal I\) 取 \(\min_\pi h(\mu,\pi)\)，给
\(|\Phi(\mu)-\Phi(\mu')|\le L\|\mu-\mu'\|_1\)；平方根不等式
给 \(|\Psi(\mu)-\Psi(\mu')|\le\sqrt L\|\mu-\mu'\|_1^{1/2}\)。

每个 (FS5) 分支是定义在多面体投影上的线性规划值函数：在其
有限定义域内为凸分片仿射函数。有限分支的逐点下包络在含
各分支定义域边界、仿射片边界及片间相等超平面的有限细分
的相对开胞腔上仿射；刚证得的全局连续性把它延到
胞腔闭包，得到有限的连续分片仿射表示。**不能**从每支凸性
推 \(\Phi\) 凸，也不能只因它是嵌套最小化便假设连续。

来源是 9/14 同一有限状态稿 §5–§6；上面的 Hoffman 证明是 C15
的替代证据，C80 是独立的正则性命题。Hoffman 的原文只提供
固定矩阵、**有解**右端的距离界；(FS10) 逐目标核有解，(FS8)
对空零面改用紧性。外部优先权、无限状态极限与跨固定系统的
统一 Lipschitz 系数未由此验收。

来源全件638 LF的逐单元覆盖与未闭证据见
[完整范围记录](../../audit/FINITE_STATE_FULL_COVERAGE.md#fst-full)。
同一主题的 [C169多面体目标与有理证书](finite_state_completion.md#fsc-polyhedral)、
[C170支撑识别例](finite_state_completion.md#fsc-support)和
[C171真实核速率及标量兼容障碍](finite_state_completion.md#fsc-lazy-rate)
已另给完整证明；它们不改变本页C15/C80的数学身份。
