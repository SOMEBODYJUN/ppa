# 有限状态证书的目标推广、支撑例与速率边界

<a id="fsc-object"></a>
## 对象与可调用范围

本页的 \(C\) 是运输成本矩阵，\(R\) 是非负同步位移成本矩阵，
\(\Phi=\Psi^2\) 是**输入运输最优**约束下的残差平方；这些符号不表示
Cayley 映射、RL 成对尺度或条件 law-step 残差。概率向量一律取列向量。
同一个 Markov 核不能确定 \(R\)，因此每个例子同时固定随机映射表示。

[C15 的定义及完整证明](finite_state_certificate.md#fs-object)与
[C80 的正则性证明](finite_state_certificate.md#fs-regularity)可独立调用。
本页补足其来源 §7、§10 尚未进入规范层的数学内容；C169–C171 均为
`derived-checked`，其外部先行性与历史审查行为不是证明前件。

<a id="fsc-polyhedral"></a>
## C169-v1：非空多面体目标与有理证书

固定互异有限状态 \(G=\{g_1,\ldots,g_N\}\subset\mathbb R^d\)、\(N\ge1\)，
\(C_{ij}=\|g_i-g_j\|^2\)，任意固定矩阵 \(R\ge0\) 且 \(R_{ii}=0\)，
以及非空紧凸多面体 \(\mathcal J\subseteq\Delta_N\)。对全部 \(\mu\in\Delta_N\)，定义
\[
 E_{\mathcal J}(\mu)=\min_{\pi\in\mathcal J}W_2^2(\mu,\pi),\qquad
 \Phi_{\mathcal J}(\mu)=\min_{\pi\in\mathcal J}
       \min_{\eta\in\operatorname{Opt}_C(\mu,\pi)}R\cdot\eta.
 \tag{FSC1}
\]
最外层不要求 \(\pi\) 是最近目标；内层最优计划不能换为全部耦合。
这里并不要求 \(R\) 来自某个随机映射，也不把 \(\mathcal J\) 自动称为不变律集。

取 [FS3](finite_state_certificate.md#fs-cells) 中全部正规化运输对偶顶点
及其 tight-edge 集 \(H_k\)，定义
\[
 \mathcal F_k^{\mathcal J}
 =\{\eta\ge0:c\eta\in\mathcal J,
                  \eta_{ij}=0\text{ if }(i,j)\notin H_k\}.
 \tag{FSC2}
\]
令 \(\mathcal V_{\mathcal J}\) 为所有非空 \(\mathcal F_k^{\mathcal J}\) 的顶点并。
以下等价：

1. \(\Phi_{\mathcal J}^{-1}(0)=\mathcal J\)；
2. 每个 \(v\in\mathcal V_{\mathcal J}\) 满足 \(R\cdot v=0\Rightarrow rv\in\mathcal J\)；
3. 存在有限 \(B\ge0\)，使 \(E_{\mathcal J}(\mu)\le B\Phi_{\mathcal J}(\mu)\) 对全部律成立。

成立时最小平方系数为
\[
 B_*^{\mathcal J}
 =\max_{v\in\mathcal V_{\mathcal J},\ R\cdot v>0}
       \frac{E_{\mathcal J}(rv)}{R\cdot v},
 \qquad \max\varnothing=0. \tag{FSC3}
\]

**证明。** 正规化运输对偶无直线；有限值最优面含顶点，零边缘也不例外。
互补松弛逐项给
\[
 \bigcup_k\mathcal F_k^{\mathcal J}
 =\{\eta\ge0:c\eta\in\mathcal J,
             \eta\in\operatorname{Opt}_C(r\eta,c\eta)\}. \tag{FSC4}
\]
每支是总质量为一的闭有界多面体，故紧。任意 \(\mu\) 选一个
\(\pi\in\mathcal J\) 即有合法最优计划；有限分支纤维的极小值取得。
对 \(\mu\in\mathcal J\) 的对角计划给 \(\Phi_{\mathcal J}(\mu)=0\)。
混合两张到 \(\mathcal J\) 的最优计划，凸性使列边缘仍在 \(\mathcal J\)，
所以 \(E_{\mathcal J}\) 凸；紧性与 \(W_2\) 的度量性给
\(E_{\mathcal J}^{-1}(0)=\mathcal J\)。

若第2句成立，分解任意残差极小计划 \(\eta=\sum_v a_vv\)。
非负性保证零成本顶点可用零目标距离，正成本顶点可用 (FSC3)，因此
\[
 E_{\mathcal J}(r\eta)\le\sum_va_vE_{\mathcal J}(rv)
 \le B_*^{\mathcal J}\sum_va_v R\cdot v
 =B_*^{\mathcal J}\Phi_{\mathcal J}(r\eta).
\]
第3句与对角计划给第1句；第1句应用于每张零成本合法顶点计划给第2句。
任何有效 \(B\) 又满足
\(E_{\mathcal J}(rv)\le B\Phi_{\mathcal J}(rv)\le B R\cdot v\)，
故不小于 (FSC3)。这也处理 \(B_*=0\) 与单状态情形。证毕。

**有限 LP 判据。** 写 \(\mathcal J=\{x\in\Delta_N:Ax\le b,\ Hx=h\}\)。
在每个非空零面
\(Z_k=\{\eta\in\mathcal F_k^{\mathcal J}:R\cdot\eta=0\}\)
上分别最大化 \((Ar\eta-b)_i\) 及 \(\pm(Hr\eta-h)_j\)。
所有不等式最大值 \(\le0\)、等式双向最大值 \(\le0\)，当且仅当
\(rZ_k\subseteq\mathcal J\)。零面顶点为原多面体的零成本顶点，故这恰为第2句。
空零面跳过；发现正最大值即产生真实假零律 \(r\eta\)。

若 \(C,R,A,b,H,h\) 全为有理数，对偶和计划顶点为有理数；
每个 \(E_{\mathcal J}(rv)\) 由有理 LP 取得有理最优值，故通过判据时
\(B_*^{\mathcal J}\) 是有理数，\(K_*^{\mathcal J}=\sqrt{B_*^{\mathcal J}}\)
未必有理。此为有限精确证书，不是多项式复杂度或大规模效率保证。
对固定随机自映射表示，有限状态上一共只有 \(N^N\) 种自映射；
任意概率噪声上的随机自映射可按这有限种取值聚合权重，保持同一个 \(P,R\)。

**正则性也保留。** 不以第1–3句为前提，\(\Phi_{\mathcal J}\) 仍在整个
\(\Delta_N\) 上全局Lipschitz且连续有限分片仿射。
[FS9–FS10](finite_state_certificate.md#fs-regularity)对任意两对概率边缘给
同一固定矩阵的最优计划集Hausdorff界；该步与目标集合无关。
于是 \(h(\mu,\pi)=\min_{\operatorname{Opt}_C(\mu,\pi)}R\cdot\eta\)
对两变量有同一个Lipschitz常数。对固定非空紧 \(\mathcal J\) 取极小，
选取旧极小目标作新问题的可行目标再交换方向，得同常数的
\(|\Phi_{\mathcal J}(\mu)-\Phi_{\mathcal J}(\mu')|\) 上界。
(FSC4)每支的线性目标值上图是多面体，有限下包络经各支域边界与仿射片交界
细分后仿射；刚证的连续性将其延到所有胞腔闭包。故正则性部分同样成立。
这里明确调用已核的固定矩阵Hoffman接口；锐EB和有理证书证明本身不依赖它。

<a id="fsc-support"></a>
## C170-v1：支撑识别强于全状态位移可分辨

对任意 C15 固定模型，若 \(R_{ij}\ge c_0C_{ij}\) 对全部状态对成立，
其中 \(c_0>0\)，则每张合法计划都有
\(R\cdot\eta\ge c_0C\cdot\eta\ge c_0E(\mu)\)。
取原残差极小即 \(E\le\Phi/c_0\)。以下完整对象证明此充分门并非必要。

取 \(G=(0,1,2)\)、确定映射 \(T(0)=0,T(1)=1,T(2)=0\)。
它在全部三点上定义，唯一随机分支的概率为1；全部律写成
\(\mu=(a,b,c)\in\Delta_3\)。其完整不变律集与位移签名是
\[
 \mathcal I=\{(q,1-q,0):0\le q\le1\},\qquad d=(0,0,2).
 \tag{FSC5}
\]
对原始嵌套残差有
\[
 \Phi(\mu)=4c,\quad E(\mu)=c,\quad K_*=1/2. \tag{FSC6}
\]
但不存在 \(c_0>0\) 使 \(R_{ij}\ge c_0C_{ij}\) 对全部状态对成立。

**证明。** \(T_\#\mu=(a+c,b,0)\)，所以不变当且仅当 \(c=0\)。
任一不变目标都支撑在 \(\{0,1\}\)。任意到该目标的耦合中，
源0和1的全部质量残差成本为0，源2的全部质量残差成本为4；
因此每个合法最优计划也具有恰为 \(4c\) 的残差成本。
源2质量至少移动距离1，故 \(E\ge c\)；保持0和1的质量，
将2的全部质量送到1，目标为 \((a,b+c,0)\)，费用恰为 \(c\)。
这证明 (FSC6)，任一 \(c>0\) 给锐性。
而 \(R_{01}=0<C_{01}=1\)，否定上述逐对正下界。
取 \(c>0\) 时，最近目标 \((a,b+c,0)\) 与实际一步极限
\((a+c,b,0)\) 不同；两者不能在外层极小化中互换。证毕。

两状态下不会有这种**真子集不变律集且两状态位移签名碰撞**的例子：
若状态为不同向量 \(x,y\)，且 \(R_{xy}=0\)，每个正概率映射都有
\(T_ax-T_ay=x-y\)。在两点自映射的四种可能中，常值给差0，
交换给差 \(y-x\)，只有恒等给差 \(x-y\)。所以每个有效分支都恒等，
全部律不变。三点在这个明确意义下最小；并未分类所有两状态证书。

<a id="fsc-lazy-rate"></a>
## C171-v1：同一惰性四循环的全初律率

固定 [C71 完整模型](lazy_cycle_ot.md#lc-object)：\(G=(0,1,3,4)\)，
循环 \(T:0\mapsto1\mapsto3\mapsto4\mapsto0\)，同噪声随机映射
以概率 \(1-p,p\) 取 \(I,T\)，\(0<p<1\)。全部不变律只有
\(\pi=(1/4,1/4,1/4,1/4)\)，\(d=(-1,-2,-1,4)\)，
\(R_{ij}=p(d_i-d_j)^2\)。保持原来的 \(E=W_2^2(\cdot,\pi)\)
与输入最优同步残差 \(\Phi=\Psi^2\)。

令 \(\gamma_p=\sqrt{(1-p)^2+p^2}\in(0,1)\)。对全部初律及整数 \(k\ge0\)，
\[
 W_2((P_p^\top)^k\mu,\pi)
 \le 4\,2^{1/4}\gamma_p^{k/2}W_2(\mu,\pi). \tag{FSC7}
\]
这是真实核迭代的相对几何界，前因子未声称最优。

**证明。** 循环置换矩阵在复 Fourier 正交基中对角，
\(P_p=(1-p)I+pQ\) 的特征值为
\(1,1-p+ip,1-2p,1-p-ip\)。后三者模不大于 \(\gamma_p\)，
因为 \(\gamma_p^2-(1-2p)^2=2p(1-p)>0\)。在实零和子空间也就有
\(\|(P_p^\top)^kv\|_2\le\gamma_p^k\|v\|_2\)。

对任意两律，任何耦合至少有 \(\operatorname{TV}\) 质量离开对角线，
最小正成本为1；最大耦合只移动 \(\operatorname{TV}\) 质量，最大成本为16。
所以 \(\operatorname{TV}\le W_2^2\le16\operatorname{TV}\)。
若 \(v\) 零和，Cauchy–Schwarz 给
\(\|v\|_1/2\le\|v\|_2\)；正负部分各有质量 \(\operatorname{TV}(v)\)，
故 \(\|v\|_2^2\le2\operatorname{TV}(v)^2\)。于是
\[
 E((P_p^\top)^k\mu)
 \le16\sqrt2\,\gamma_p^kE(\mu),
\]
开平方即 (FSC7)。\(p=1/2\) 时律距离率为 \(2^{-k/4}\)。
\(p=1\) 的确定循环也有锐 EB 系数 \(\sqrt{13}\)，
但上述严格几何率消失；此端点不属 (FSC7)，也不修改C71原有的 \(0<p<1\) 范围。
端点的独立证据是：此时 \(R_{ij}=(d_i-d_j)^2\)，
[C71证明中的显示矩阵](lazy_cycle_ot.md#lc-sharp)
\(H=C-13(d_i-d_j)^2\) 及其有序计划抵消仍逐项成立，故 \(E\le13\Phi\)。
同一律 \(\mu_*=(0,0,3/4,1/4)\) 的完整有序计划给
\(E=13/4,\Phi=1/4\)，证明端点锐性；平稳方程仍只给公平律。

<a id="fsc-compatibility"></a>
## 精确 almost-firm 参数与指定标量公式的障碍

对任意 \(\tau>0\) 考虑全部状态对上的条件
\[
 \mathbb E|T_\xi x-T_\xi y|^2+
 \tau\mathbb E|(x-T_\xi x)-(y-T_\xi y)|^2
 \le(1+\epsilon)|x-y|^2. \tag{FSC8}
\]
该固定随机表示的最小非负违反量恰为
\[
 \epsilon_{\min}(\tau)=p(15+25\tau). \tag{FSC9}
\]
尤其 \(\tau=1\) 时是 \(40p\)：\(p=1/100\) 给 \(2/5<1\)，
\(p=1/2\) 给20。

**逐对证明。** 对六个不同无序状态对，(FSC8) 中超过恒等基线的系数除以 \(p\) 为：

| 状态对 | 系数 |
| --- | --- |
| 0,1 | \(3+\tau\) |
| 0,3 | \(0\) |
| 0,4 | \((-15+25\tau)/16\) |
| 1,3 | \((-3+\tau)/4\) |
| 1,4 | \(4\tau\) |
| 3,4 | \(15+25\tau\) |

最后一项对全部 \(\tau>0\) 最大且为正；相同状态的两边均为0。
所以它既必要又充分，证明 (FSC9)。

现在只讨论一个**明确的标量公式**：\(\rho:[0,r_0]\to[0,\rho(r_0)]\)
连续严格递增，\(\rho(0)=0\)，是 \(\pi\) 某邻域内的 EB gauge，且希望
对全部充分小正 \(t\) 有
\[
 \theta(t)^2=(1+\epsilon)t^2-
       \tau[\rho^{-1}(t)]^2<t^2, \tag{FSC10}
\]
其中同一 \(\epsilon\) 满足 (FSC8)。没有这样的 \(\rho\)。

**证明。** 对 \(0<u\le1/4\)，取
\(\mu_u=(1/4,1/4-u,1/4+u,1/4)\)。
按状态值标记，该完整计划的全部非零条目是
\(\eta_{0,0}=1/4\)、\(\eta_{1,1}=1/4-u\)、
\(\eta_{3,1}=u\)、\(\eta_{3,3}=1/4\)、\(\eta_{4,4}=1/4\)
（端点 \(u=1/4\) 时第二条删除）。它的两边缘恰为 \(\mu_u,\pi\)。
严格Monge交换排除每一对正质量交叉边；无交叉计划由每个累积源区间与累积目标区间的交长唯一决定。
所以这张完整计划是唯一的输入 \(C\)-最优计划，而非为小残差选出的一张任意耦合。
逐条代入两成本得
\[
 E(\mu_u)=4u,\qquad\Phi(\mu_u)=pu. \tag{FSC11}
\]
当 \(u\downarrow0\) 它进入任意 \(\pi\) 邻域。以 \(r=\sqrt{pu}\) 重参数化，
局部 EB 要求 \(\rho(r)\ge2r/\sqrt p\) 对全部充分小正 \(r\) 成立。
将 \(t=\rho(r)\) 代入 (FSC10)，必要条件为
\[
 \rho(r)<\sqrt{\tau/\epsilon}\,r
 \le\frac1{\sqrt p}\sqrt{\frac{\tau}{15+25\tau}}\,r
 <\frac{r}{5\sqrt p},
\]
矛盾。只需严格收缩不等式的必要条件就已矛盾，故无须假定根号右端非负。
这不排除 C71 已存在的线性 EB，更不否定 (FSC7) 的实际收敛。
这里使用可逆 gauge；对仅非降的函数，未先定义广义逆时 (FSC10) 本身无确定含义。
条件律残差、law-step 距离或另一种随机表示不能代入这条证明。

<a id="fsc-cell-grid"></a>
## 35个胞腔顶点与错误局部锐性路线

令累积源质量 \(s_1\le s_2\le s_3\) 落在 \([0,1]\)，目标断点为
\(1/4,1/2,3/4\)。有序耦合条目是两个累积区间交长。
沿所有 \(s_i=j/4\) 切分，交长及其 \(C,R\) 成本在每片仿射。
每片可由盒约束和 \(s_i\le s_{i+1}\) 表示。若一个顶点有非网格坐标，
取包含该坐标的最大相等坐标块；它位于同一开网格区间，且与块外
严格排序的坐标有正间距。将该块所有坐标共同作足够小的正负平移，
仍留在同一片，矛盾。因此全部顶点在四分之一网格上。
反之，任一有序网格三元组在邻接片中由三个独立坐标边界固定，是一个顶点。
它们等价于 \(\mu=z/4\)、\(z\in\mathbb Z_{\ge0}^4\)、\(\sum z_i=4\)，
共有 \(\binom73=35\) 个。仿射不等式在这些顶点成立便在全部胞腔成立。
这是完整有限归约的证明，不代表已经认证任何历史执行记录。

从 \(\pi\) 到 C71 全局取等律 \(\mu_*=(0,0,3/4,1/4)\) 的线段
\(\mu_t=(1-t)\pi+t\mu_*\) 不能保持全局锐比值。
当 \(0<t\le1/2\)，有序计划的完整非对角条目是
\(1\to0:t/4\)、\(3\to1:t/2\)，其余条目在对角线。
因此 \(E(\mu_t)=9t/4\)、\(\Phi(\mu_t)=3pt/4\)，比值为 \(3/p\)，
严格小于全局 \(13/p\)。到 \(t=1\) 才取得后者。
局部障碍使用 (FSC11)，不靠全局最大点作未经核验的径向缩放。

<a id="fsc-source"></a>
## 来源与外部证据边界

来源是既有《有限状态_精确零集与线性误差界等价.md》638 LF，
完整定位、SHA-256及全部逐单元裁决见
[完整范围记录](../../audit/FINITE_STATE_FULL_COVERAGE.md#fst-full)。
本页证明不调用来源中的 PROVED、VERIFIED、程序 PASS 或独立审查自报。
Hoffman 的一手接口已在 [LIT-HOFFMAN-1952](../../LITERATURE.md#lit-hoffman-1952)
登记；C169的正则性补充通过FS9–FS10调用它，锐证书及C170/C171不依赖它。

源稿援引的 Dolgopolik Theorem 5、HLS 式(20)/Theorem 2.6、
Luke、Luke–Schultze–Grubmüller，以及 Robinson/Mangasarian–Shiau/Burke–Ferris
的确切版本、调用范围与历史阅读行为逐项保留外部义务。
这里将 (FSC10) 当作显示给出的数学条件证明其失败，不声称已核其论文出处。
全局先行性和投稿评价继续未定。
