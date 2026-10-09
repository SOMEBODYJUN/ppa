# C223-v1：无共同固定点、精确同步残差零集与统一几何律收敛仍无正幂误差界

<a id="fpf-theorem"></a>
## 精确结论与对象

**Status：`derived-checked`，FP1–FP21 的自足推导及两路独立逐门接收已完成；不认证全球发表先行性。**

存在一个固定的非空紧集 \(G\subset\mathbb R^2\)、四个连续自映射和固定正概率，使：

1. 没有共同固定点；
2. 源期望 almost-firm 不等式以 \(\alpha=1/2\)、\(\tau=(1-\alpha)/\alpha=1\)、\(\varepsilon=45/64<1\) 在**全部状态对**上成立；
3. 原同步运输残差的零集恰为全部不变律集；
4. 同一有限 \(C\) 与 \(0<r<1\) 对全部初律及全部整数 \(k\ge0\) 给到其不变极限的相对几何界；
5. 同一个不变律 \(\bar\pi\) 的每个正半径 \(W_2\) 球内，所有正幂误差界均失败：
   \[
   \forall q,K,a>0\ \exists\mu\in\mathscr P(G):\quad
   W_2(\mu,\bar\pi)<a,\qquad
   d_{W_2}(\mu,\mathcal I)>K\Psi(\mu)^q.
   \tag{FP1}
   \]

这是一个新对象，不把 C143/C144 的量词或状态默改为本例。构造思路为删除 C143 的全部固定中点，再加入独立二状态刷新；本文证明自足，不导入 C143 的中点相关运输证书或一步距离收缩常数。

对每个整数 \(n\ge1\)，置
\[
t_n=2^{-n},\qquad \delta_n=2^{-3n-10},\qquad e_n=\delta_n^n,
\]
\[
a_n=t_n,\qquad b_n=t_n+\delta_n,\qquad
c_n=t_n+(2-e_n)\delta_n,
\]
\[
H=\{0\}\cup\bigcup_{n\ge1}\{a_n,b_n,c_n\},\qquad
G=H\times\{0,1\}\subset\mathbb R^2.
\tag{FP2}
\]

\(\delta_n\) 是尺度，\(\delta_x\) 是 Dirac 律。定义完整自映射
\[
T0=0,\qquad Ta_n=b_n,\qquad Tb_n=a_n,\qquad Tc_n=b_n.
\tag{FP3}
\]
令 \(\beta=(\delta_0+\delta_1)/2\)、\(p=1/8\)，四个实际随机映射为
\[
F_{i,j}(x,z)=(T^i x,j),\qquad (i,j)\in\{0,1\}^2,
\]
\[
p_{0,0}=p_{0,1}=7/16,\qquad
p_{1,0}=p_{1,1}=1/16.
\tag{FP4}
\]
每步独立抽取此四值指标，独立于初状态和此前全部指标。两分量指标相互独立，主动更新概率为 \(p\)，刷新为公平二状态。\(\mu_x\) 表示第一边缘；在 \(H\) 上写 \(R\nu=T_\#\nu\)、\(Q=(1-p)I+pR\)。完整核满足
\[
\mu P=(\mu_xQ)\otimes\beta.
\tag{FP5}
\]

全文距离为平方 Euclidean 成本的 \(W_2\)。取**全部**不变律 \(\mathcal I=\{\pi:\pi P=\pi\}\)，并始终取
\[
\Psi(\mu)^2=\inf_{\pi\in\mathcal I}
\inf_{\eta\in\operatorname{Opt}_{W_2}(\mu,\pi)}
\int c_R(u,v)\,d\eta(u,v),
\]
\[
c_R(u,v)=\sum_{i,j}p_{i,j}
\|(u-F_{i,j}u)-(v-F_{i,j}v)\|^2.
\tag{FP6}
\]
外层没有改为某个指定目标；内层没有删除输入最优性。

<a id="fpf-geometry"></a>
## 紧性、连续性及无共同固定点

各三点块不同且分离，唯一聚点为 0，故 \(H\) 与 \(G\) 紧。有
\(0<e_n<1/100\)、\(\delta_{n+1}=\delta_n/8\)、\(t_n/\delta_n=2^{2n+10}\ge4096\)。块内 \(T\) 的最大绝对割线斜率为 \(1/(1-e_n)\le100/99<5/4\)，并且 \(|Tx-x|\le\delta_n\)。

若 \(n<m\)、\(x\) 属第 \(n\) 块、\(y\) 属第 \(m\) 块，则
\[
|x-y|\ge t_n/2-\delta_n/4
\ge4(\delta_n+\delta_m).
\]
第一步使用 \(t_m\le t_n/2\) 与 \((2-e_m)\delta_m\le\delta_n/4\)；第二步由 \(t_n\ge4096\delta_n\)、\(\delta_m\le\delta_n/8\) 给出。于是
\[
|Tx-Ty|\le|x-y|+\delta_n+\delta_m\le(5/4)|x-y|.
\]
与 0 配对时由 \(|x|\ge t_n\ge4\delta_n\) 得同一界。因此 \(T\) 在整个 \(H\) 上为 \(L=5/4\)-Lipschitz；四个 \(F_{i,j}\) 连续。\(F_{0,0}\) 的固定点第二坐标只能为 0，\(F_{0,1}\) 的只能为 1，所以四映射无共同固定点。

<a id="fpf-source"></a>
## 期望 almost-firm 的参数与源适用域

**Paper Fact。** Luke–Schultze–Grubmüller 的 [2026 正式刊本](https://link.springer.com/article/10.1007/s10107-025-02319-9)，Assumption 3(b)、式 (16)，要求某个 \(\varepsilon\in[0,1)\)、\(\alpha\in(0,1)\)，对全部 \(u\in G\) 和全部 \(v\in\bigcup_{\pi\in\mathcal I}\operatorname{supp}\pi\) 满足期望 almost-firm 不等式。式 (15) 使用全部不变目标和给定输入两边缘的 \(W_2\)-最优计划。本例使用相同残差，且不等式在更强的全部 \(G\times G\) 上成立。该文 Assumption 3(c)、式 (10)/(17) 是额外的兼容误差界前件，并非本条所验证的期望不等式；本文不把它当作已知假设。

令 \(D(x)=x-Tx\)。对 \(u=(x,z),v=(y,w)\)，直接按四个指标求和，得
\[
c_R(u,v)=p|D(x)-D(y)|^2+|z-w|^2,
\tag{FP7}
\]
\[
\mathbb E\|F_\xi u-F_\xi v\|^2
=(1-p)|x-y|^2+p|Tx-Ty|^2.
\]
由 \(T\) 的 \(L\)-Lipschitz 性，\(|D(x)-D(y)|\le(1+L)|x-y|\)。因此
\[
\begin{aligned}
\mathbb E\|F_\xi u-F_\xi v\|^2+c_R(u,v)
&\le[1-p+pL^2+p(1+L)^2]|x-y|^2+|z-w|^2\\
&=\frac{109}{64}|x-y|^2+|z-w|^2\\
&\le\frac{109}{64}\|u-v\|^2.
\end{aligned}
\tag{FP8}
\]
故 \(\alpha=1/2,\tau=1,\varepsilon=45/64\) 合法。这里验证的是**期望**性质，未声称每个主动分支单独以同一 \(\varepsilon<1\) almost-firm。

<a id="fpf-zero"></a>
## 全部不变律与原残差精确零集

由 (FP5)，不变律必为 \(\nu\otimes\beta\)，其中 \(\nu Q=\nu\)，等价于 \(R\nu=\nu\)。\(T\) 没有任何点映到 \(c_n\)，故不变 \(\nu\) 在各 \(c_n\) 质量为零；端点交换迫使两端质量相等。反向这些条件足够。因此
\[
\mathcal I=
\left\{\left(s_0\delta_0+
\sum_{n\ge1}\frac{s_n}{2}(\delta_{a_n}+\delta_{b_n})\right)\otimes\beta:
 s_n\ge0,\ \sum_{n\ge0}s_n=1\right\}.
\tag{FP9}
\]
尤其 \(\bar\pi=\delta_0\otimes\beta\in\mathcal I\)。

位移标签为
\[
D(0)=0,\quad D(a_n)=-\delta_n,\quad
D(b_n)=\delta_n,\quad D(c_n)=(1-e_n)\delta_n.
\]
负标签互异；各正标签落在 \([(99/100)\delta_n,\delta_n]\)，不同块区间因八倍尺度分离而不交；同块两正标签因 \(e_n>0\) 不同。零标签只有 0。因此 \(D:H\to\mathbb R\) 单射；由 (FP7)，\(c_R(u,v)=0\) 当且仅当 \(u=v\)。

必须另核下确界取得：紧 \(G\) 上概率律与计划集紧；有限连续映射使 \(P\) 连续，故 \(\mathcal I\) 闭紧；连续平方输入成本与 \(W_2\) 的连续性使条件
\(\int\|u-v\|^2d\eta=W_2(\mu,\pi)^2\) 对联合变量 \((\pi,\eta)\) 闭。固定 \(\mu\) 的联合可行集非空紧，连续 \(c_R\) 取到最小值。因此 \(\Psi(\mu)=0\) 时存在合法不变目标和**输入最优**计划，使其非负成本积分为零。计划只能支撑在对角线上，故 \(\mu=\pi\in\mathcal I\)。反向，不变律的对角计划输入最优且成本为零。遂
\[
\Psi^{-1}(0)=\mathcal I.
\tag{FP10}
\]
标签在聚点附近无统一分离常数并不妨碍取得后的支持论证。

<a id="fpf-rate"></a>
## 对全部初律、全部时间的同一相对几何率

由 (FP3)，\(T^3=T\)、\(R^3=R\)。在基空间定义
\[
A\nu=\tfrac12(R\nu+R^2\nu),\qquad
\Pi\mu=(A\mu_x)\otimes\beta.
\tag{FP11}
\]
\(RA=A\)，所以 \(\Pi\mu\in\mathcal I\)。\(A\) 固定全部基空间不变律，并且同步推前、混合计划给
\[
W_2(A\nu,A\sigma)^2
\le\tfrac12(L^2+L^4)W_2(\nu,\sigma)^2
\le L^4W_2(\nu,\sigma)^2.
\tag{FP12}
\]
令 \(d_H(\nu)=\inf_{R\sigma=\sigma}W_2(\nu,\sigma)\)。最近基空间不变律存在；(FP12) 与三角不等式给
\[
W_2(\nu,A\nu)\le(1+L^2)d_H(\nu).
\tag{FP13}
\]

令 \(a_k=(7/8)^k\)、\(b_k=(3/4)^k\)。独立主动更新次数的零次、奇数次、正偶数次概率给，对每个整数 \(k\ge0\)，
\[
\nu Q^k=a_k\nu+\tfrac{1-b_k}{2}R\nu+
\left(\tfrac{1+b_k}{2}-a_k\right)R^2\nu.
\tag{FP14}
\]
系数皆非负且总和为 1，包括 \(k=0\)。若 \(a_k\le1/2\)，用 \(b_k\le a_k\) 改写为非负混合
\[
\nu Q^k=(1-2a_k)A\nu+a_k\nu+
(a_k-b_k/2)R\nu+(b_k/2)R^2\nu.
\]
后三项总质量为 \(2a_k\)。分别耦合到同一个 \(A\nu\)，并使用 \(R A\nu=R^2 A\nu=A\nu\)，得
\[
W_2(\nu Q^k,A\nu)^2\le2a_kL^4W_2(\nu,A\nu)^2.
\tag{FP15}
\]
若 \(a_k>1/2\)，直接用 (FP14) 的总质量 \(1\le2a_k\) 与同一耦合界，仍得 (FP15)。因此
\[
W_2(\nu Q^k,A\nu)\le C r^k d_H(\nu),\qquad
C=\sqrt2 L^2(1+L^2),\quad r=\sqrt{7/8}<1.
\tag{FP16}
\]

任意初律可有两坐标相关性；(FP5) 仍给 \(\mu P^k=(\mu_xQ^k)\otimes\beta\) 对 \(k\ge1\) 成立。投影为 1-Lipschitz，故 \(d_H(\mu_x)\le d_{W_2}(\mu,\mathcal I)\)。同一公平第二边缘的两个乘积律满足
\(W_2(\nu\otimes\beta,\sigma\otimes\beta)=W_2(\nu,\sigma)\)：投影给下界，基空间最优计划乘上第二坐标对角计划给上界。由 (FP16)，完整几何界对所有 \(k\ge1\) 成立。

最后 \(\Pi\) 是 \(L^2\)-Lipschitz 且固定 \(\mathcal I\)。取最近 \(\pi\in\mathcal I\)，得
\[
W_2(\mu,\Pi\mu)\le(1+L^2)d_{W_2}(\mu,\mathcal I)
\le C d_{W_2}(\mu,\mathcal I).
\]
这补上 \(k=0\)。同一 \(C,r\) 因此对**全部** \(\mu,k\ge0\) 满足目标假设，且 \(\mu P^k\to\Pi\mu\) 是不变极限。

<a id="fpf-no-power"></a>
## 同一个不变律附近，全部正幂误差界失败

固定见证序列
\[
\mu_n=\tfrac12(\delta_{a_n}+\delta_{c_n})\otimes\beta,
\qquad
\pi_n=\tfrac12(\delta_{a_n}+\delta_{b_n})\otimes\beta\in\mathcal I.
\tag{FP17}
\]
所有不变律第一坐标支撑在
\(S=\{0\}\cup\bigcup_m\{a_m,b_m\}\)。\(c_n\) 到 \(S\) 的最近点为 \(b_n\)，距离为 \((1-e_n)\delta_n\)：同块另外一点更远；所有其它块的间隙至少 \(4(\delta_n+\delta_m)>\delta_n\)；到 0 的距离至少 \(t_n>\delta_n\)。

因此任何不变目标、任何耦合都必须为第一坐标 \(c_n\) 的总质量 \(1/2\) 支付至少 \((1-e_n)^2\delta_n^2/2\)。将 \((a_n,z)\) 保持原位、\((c_n,z)\) 送到 \((b_n,z)\)，每个 \(z=0,1\) 的两条边各有质量 \(1/4\)，恰到 \(\pi_n\)，并达到下界。所以
\[
d_{W_2}(\mu_n,\mathcal I)
=W_2(\mu_n,\pi_n)=\frac{(1-e_n)\delta_n}{\sqrt2}.
\tag{FP18}
\]
这个计划达到全体不变目标的下界，故特别是固定输入两边缘 \((\mu_n,\pi_n)\) 的**输入 \(W_2\)-最优计划**；若该对边缘另有更廉计划就与下界矛盾。这是代入 (FP6) 的合法性证书。

此计划保持第二坐标。唯一非零位移标签差为
\(D(c_n)-D(b_n)=-e_n\delta_n\)，总质量 \(1/2\)，主动概率 \(1/8\)。故
\[
0<\Psi(\mu_n)\le\frac{\delta_ne_n}{4}
=\frac{\delta_n^{n+1}}4.
\tag{FP19}
\]
严格正性来自 (FP10) 与 (FP18)，上界足够，不需要证明该计划另外最小化残差。

令 \(\bar\pi=\delta_0\otimes\beta\)。保持第二坐标并把第一坐标送到 0 的计划给
\[
W_2(\mu_n,\bar\pi)^2=\tfrac12(a_n^2+c_n^2)
\le(t_n+2\delta_n)^2\longrightarrow0.
\tag{FP20}
\]
等号由第一边缘投影下界与上述计划成立。对每个固定 \(q>0\)，(FP18)–(FP19) 给
\[
\frac{d_{W_2}(\mu_n,\mathcal I)}{\Psi(\mu_n)^q}
\ge\frac{4^q(1-e_n)}{\sqrt2}\,
\delta_n^{1-q(n+1)}\longrightarrow\infty,
\tag{FP21}
\]
因为
\[
\log_2\!\left(\delta_n^{1-q(n+1)}\right)
=(3n+10)\big(q(n+1)-1\big)\longrightarrow+\infty.
\]
给定任意 \(q,K,a>0\)，取同一个充分大的 \(n\)，使 \(W_2(\mu_n,\bar\pi)<a\) 并使 (FP21) 大于 \(K\)。这证明 (FP1)，从而否定所述必要性命题。

<a id="fpf-boundary"></a>
## 机制、失败路线与可调用边界

**Mechanism。** 同一三点块的主动转移概率保持固定，因此到所选不变极限的几何率不随 \(e_n\) 退化；而 \(c_n\) 与 \(b_n\) 的位移标签差为超平坦的 \(\delta_ne_n\)。它们在输入空间距离约为 \(\delta_n\)，但同步位移几乎相同。独立刷新移除共同固定点；删除原固定中点则使位移标签单射，排除刷新与守恒坐标相关性产生的假零。

**失败路线。** 直接把完整 C143 与公平刷新作乘积仍有假零：任取两个不同基空间固定点 \(x_1,x_2\)，令 \(\mu=(\delta_{(x_1,0)}+\delta_{(x_2,1)})/2\)，\(\pi=\delta_{x_1}\otimes\beta\)。保持二状态、送第一坐标到 \(x_1\) 的计划达到第一边缘投影下界，故输入最优；所有主动位移标签都为零、二状态也相同，故原残差为零，但 \(\mu\) 非不变。这一 fatal objection 是删除中点的数学理由，不能仅凭乘积核有快率而忽略它。

**Truth / Value / Novelty / Scope。** 本例关闭无共同固定点且 exact-zero 的正幂必要性版本；给出保留输入最优性的显式机制。它不否定紧连续 exact-zero 类的一般 gauge 存在性，不宣称常数最优、状态集连通/凸、每个分支单独 almost-firm 或随机样本路径收敛；不引入源兼容误差界作为假设。全球发表先行性未核，本文仅记录内部数学推导。C143/C144 原有身份保持。

**复算。** [精确有理验证代码](../../code/fixed_point_free_no_power/verify.py) 与 [运行和证据范围](../../code/fixed_point_free_no_power/README.md) 检查有限状态对、几何/位移、概率矩阵与混合恒等式、见证最优成本和全部正幂失败的指数反算；无限域与全律空间结论由上述证明承担。

**实际接收范围。** 两路独立审查完整读取本文 FP1–FP21 与 `verify.py`，其中源审查另完整读取复算 README 并重新核一手源式 (15)–(17)。均实际运行精确验证。独立攻击覆盖源参数/全部状态对、任意相关初律、联合输入最优可行集取得、全部不变目标支撑下界、两种概率混合区间、k=0 和同一锚点全部 q/K/a 量词；未发现承重缺口。根审查修正局部半径的平方措辞和“遍历”表述。接收不涉及全球新颖性、常数最优、凸/连通状态集或样本路径；没有从 C143 导入 B8。
