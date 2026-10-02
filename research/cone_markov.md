# 锥优化与 Markov：两条独立的残差研究链

本页从证明包重构数学内容。来源报告的内部审计与本轮阅读分开：本轮核对主要定义、结论和依赖，没有重新完成一般锥定理的全部拓扑细节、全部运输多面体计算或全球优先权审计。这里的结论不能自动接入确定性 RLEB–PPA。

<a id="c-rank"></a>
<a id="c-mscq"></a>
<a id="c-amen"></a>
<a id="c-normal"></a>
<a id="c-univ"></a>
<a id="c-nonamen"></a>
## 1. 锥：冻结最小面的精确对象

有限维欧氏空间 \(X,E\)，闭、尖、满维凸锥 \(C\subset E\)，\(G:V\to E\) 为 \(C^1\)，\(G(\bar x)=0\)。令

\[
\Omega=G^{-1}(C),\ A=DG(\bar x),\ \mathfrak F=F_{\min}(\operatorname{Im}A\cap C),\quad
H=\mathfrak F^\perp,\ S_{\rm dual}=\operatorname{span}(C^*\cap\mathfrak F^\perp).
\]

此处 \(\mathfrak F\) 是锥的最小面，\(S_{\rm dual}\) 是对偶面子空间；两者都不是 PPA 的原算子或零集。冻结面 CRSC 要求 \(A^*C^*\) 闭，且 \(\operatorname{rank}(DG(x)^*|_H)\) 在一个完整邻域恒定。锥 nice 指每个面 \(J\) 的 \(C^*+J^\perp\) 闭；amenable 指每个面存在有限 \(a_J\) 使
\(d(y,J)\le a_Jd(y,C)\) 对全部 \(y\in\operatorname{span}J\) 成立。[CM-C §2]

<a id="c-face"></a>
### CM-RANK → CM-FACE → CM-MSCQ

| 超边 | 联合前件 | 结论与证明作用 |
|---|---|---|
| CM-RANK | nice + 冻结 CRSC + Pataki 闭像判据 | \(\operatorname{rank}(DG(x)^*|_{S_{\rm dual}})=\operatorname{rank}(DG(x)^*|_H)\)：参考点像相等、非零子式持续、包含夹逼 |
| CM-FACE | CM-RANK + 连续核投影 | 邻域闭像与最小面稳定；局部 \(G^{-1}(C)=G^{-1}(\mathfrak F)\) |
| CM-NORMAL | 同上 + 常秩坐标及正法向夹角 | 修正到共同流形 \(M=\{P_HG=0\}\)，\(\|x-\hat x\|\le b d(G(x),C)\) |
| CM-MSCQ | CM-NORMAL + 参考面 amenability + 同流形切向修正 | \(d(x,\Omega)\le\kappa d(G(x),C)\)，原锥残差 MSCQ |

非退化时可取
\(b=4/(\sigma\eta)\)，\(\sigma=\sigma_{\min}^+(P_HA)\)，
\(\eta=\min_{u\in\operatorname{Im}(P_HA),\|u\|=1}d(u,\overline{P_HC})>0\)。若 \(\mathfrak F\ne\{0\}\)，取单位切向方向的像 \(v_0\in\operatorname{ri}\mathfrak F\)，\(\tau_{\mathfrak F}=d(v_0,\operatorname{rbd}\mathfrak F)>0\)，则

\[
\kappa=b+\frac4{\tau_{\mathfrak F}}a_{\mathfrak F}(1+L_Gb)
\]

是局部上界，未声称最佳常数或指定数值半径。秩零、零面、全面、零维约化需分支处理，不能套正奇异值公式。[CM-C §§3–5]

**普遍量词与反例。** 对固定 proper nice 锥，amenability 等价于每个在顶点满足冻结 CRSC 的 \(C^1\) 系统都有 MSCQ；逆向只需测试各面线性等距嵌入。nice 非 amenable 的来源锥上，线性导数使 full facial CRCQ 全局恒定，但构造路径的输入距离为 \(\Theta(t^3)\)、锥残差至多 \(O(t^5)\)，MSCQ 失败。该锥本身来自既有文献，不能作为新构造计功。[CM-C §7]

**实例的数学作用。** 耦合双 SOC 的可行集为 \(s,t\ge0,u=st\)；PSD 例可行集为 \(B\succeq0,u=\operatorname{tr}(B^2)\)。它们检验共同法向修正和高维非多面体面，未从各块 MSCQ 推联合 MSCQ。PSD 参考面 amenability 常数为 1，有限乘积常数取各面的最大值。[CM-C §6]

<a id="m-psi"></a>
## 2. Markov：必须保留的双层最小化

紧状态集 \(K_{\rm state}\subset\mathbb R^d\)，几乎处处连续、联合可测的随机自映射 \(T_\xi:K_{\rm state}\to K_{\rm state}\)，实际更新使用独立新噪声。设 \(\mu P=\mathbb E(T_\xi)_\#\mu\)，不变律集 \(\mathcal I\ne\varnothing\)，\(d(\mu)=d_{W_2}(\mu,\mathcal I)\)。此处状态集与 §1 的约束映射 \(G:V\to E\) 不同。定义

\[
c_R(x,y)=\mathbb E\|(x-T_\xi x)-(y-T_\xi y)\|^2,
\]
\[
\Psi(\mu)^2=\inf_{\pi\in\mathcal I}\inf_{\eta\in\operatorname{Opt}_{W_2}(\mu,\pi)}\int c_R d\eta.
\]

内层必须是该输入/目标对的完整平方欧氏成本最优耦合，且两边共用同一噪声；\(\Psi\) 不是 \(W_2(\mu,\mu P)\)。核 \(P\) 本身也不决定表示依赖的 \(c_R\)。[CM-M §1]

<a id="m-exact"></a>
### CM-GAUGE：紧性与 exact-zero

上述紧连续设置保证极小值取得、\(\Psi\) 下半连续，并有

\[
\Psi^{-1}(0)=\mathcal I
\iff\exists\text{严格一般 gauge }\rho:\ d(\mu)\le\rho(\Psi(\mu))\quad\forall\mu.
\]

证明先用紧性推出 \(\omega(s)=\sup_{\Psi(\mu)\le s}d(\mu)\to0\)，再作连续严格增大函数包络；不需要轨道收敛假设，不给可计算或速率兼容 gauge。[CM-M Theorem 1]

<a id="m-fin"></a>
### CM-FINITE：有限状态 exact-zero ⇔ 全局线性 EB

固定有限状态几何、随机映射及其概率，令 \(C_{ij}=\|g_i-g_j\|^2\)、\(R_{ij}=c_R(g_i,g_j)\)。最优运输对偶顶点的 tight-edge 图产生有限多面体 \(\mathcal F_k\)，其并精确覆盖“不变列边缘＋该对边缘最优运输”的所有计划。记其顶点并为 \(\mathcal V\)，\(E(\mu)=d(\mu)^2\)。

\[
\Psi^{-1}(0)=\mathcal I
\iff r(v)\in\mathcal I\quad\forall v\in\mathcal V\text{ 满足 }R\cdot v=0
\iff \exists B<\infty:E\le B\Psi^2.
\]

完整的固定系统证明、空零面与非空零面分支及动力反例已在独立的 [C15 有限状态证书](topics/random_markov/finite_state_certificate.md#fs-theorem) 重写；[C80 正则性](topics/random_markov/finite_state_certificate.md#fs-regularity) 另证分片仿射与 Lipschitz，此处仅保留路线摘要。

最优平方系数为
\(B_* =\max_{v\in\mathcal V,R\cdot v>0}E(r(v))/(R\cdot v)\)，空最大值为 0。证明靠精确有限分支与凸性；不需要混合性、唯一不变律或 almost-firmness。只对固定数据给有限判定，不承诺多项式时间或跨系统统一常数。[CM-M Theorem F]

<a id="m-false"></a>
<a id="m-nopower"></a>
<a id="fast-eb"></a>
<a id="power-eb"></a>
### CM-FALSE-ZERO 与 CM-NO-POWER：两个独立反例

| 模型 | 同时成立 | 排除的推理 |
|---|---|---|
| \(T_j(x,y)=(x,j)\)，公平 \(j=0,1\) | 一步变成不变律；\(\Psi(\mu)=W_2(\mu_y,\mathrm{Bern}(1/2))\)；相关律可有 \(\Psi=0,d>0\) | 轨道快速收敛 ⇒ 此残差识别不变律 |
| 紧可数状态的二映射模型 | exact-zero、统一相对几何率、law-space 有限长度；对每个 \(q>0,K<\infty,r>0\) 都有 \(W_2(\nu,\delta_0)<r,d(\nu)>K\Psi(\nu)^q\) | exact-zero ＋ 快收敛 ⇒ 正 Hölder EB |

第二例仍由 CM-GAUGE 保证一般 gauge。来源的更窄 Corollary 5 固定有效的期望 almost-firm 参数 \(0<\alpha<1\)、\(\varepsilon_f\ge0\)、\(\tau=(1-\alpha)/\alpha\)，其图点对界为
\(\mathbb E\|T_\xi x-T_\xi y\|^2+\tau c_R(x,y)\le(1+\varepsilon_f)\|x-y\|^2\)，并取定义在局部值域上可逆的严格增 gauge \(\rho\)。它只排除该例在一个完整状态邻域上有效的**固定参数**与局部 \(d\le\rho(\Psi)\) 同时满足
\(\Theta_\rho(t)^2=(1+\varepsilon_f)t^2-\tau[\rho^{-1}(t)]^2\ge0\)、\(\Theta_\rho(t)<t\) 对所有足够小的正 \(t\)。此处保持来源报告状态，不能说所有速率证书均失败。[CM-M Theorems 2、4，Corollary 5]

<a id="m-cond"></a>
<a id="ob-res"></a>
<a id="m-binary"></a>
<a id="m-gauss"></a>
<a id="m-moment"></a>
<a id="m-recoup"></a>
<a id="cond-eb"></a>
## 3. 条件残差修复与随机提升边界

固定守恒边缘 \(\nu\)，二进制纤维 \(X=\{0,1\}^m\)，\(\mu(du,dx)=\nu(du)\mu_u(dx)\)。条件运输
\(\mathsf W_\nu^2(\mu,\eta)=\int W_2^2(\mu_u,\eta_u)d\nu\)
只允许保持 \(u\) 的耦合；纤维平方欧氏成本即 Hamming 成本。取可测 \(b_i(u)\in(0,1)\)、\(p_i(u)>0\)，并要求 \(\sum_i p_i(u)\le1\) 几乎处处，剩余概率执行恒等更新。刷新第 \(i\) 坐标时独立抽 \(\operatorname{Bern}(b_i(u))\)；目标 \(\pi_\nu(du,dx)=\nu(du)\bigotimes_i\operatorname{Bern}(b_i(u))(dx)\)。定义保持 \((u,x_{-i})\) 不变的条件残差
\[
d_i(u;\mu)^2=\sum_{x_{-i}}\mu_u(x_{-i})
\left|\mu_u(X_i=1\mid x_{-i})-b_i(u)\right|,\qquad
\mathcal R(\mu)^2=\int\sum_i p_i(u)d_i(u;\mu)^2\,\nu(du).
\]
零概率条件事件上的版本不影响积分。这是条件重抽样残差，不是 §2 的同步运输 \(\Psi\)。

**CM-BINARY：**\(a_* =\operatorname{ess\,inf}_u\min_i p_i(u)>0\) 当且仅当存在统一线性 EB／一步严格收缩／某固定块严格收缩／统一相对几何率；最佳 EB 常数 \(a_*^{-1/2}\)、最佳 \(k\) 步因子 \((1-a_*)^{k/2}\)。若 \(a_*=0\)，每条律仍收敛，但每个固定 \(k\) 的最坏相对因子为 1。[CM-M Theorem 6]

单 bit 时，记当前条件成功概率为 \(r(u)=\mu_u(X_1=1)\)、目标概率 \(b(u)=b_1(u)\)、\(a(u)=p_1(u)\)、\(h(u)=|r(u)-b(u)|\)、\(M(u)=\max\{b(u),1-b(u)\}\)。这里 \(0\le h\le M\) 可测，且下列积分均对 \(\nu\)；精确最小非降模满足

\[
\phi(t)^2=\sup_{0\le h\le M,\int ah\,d\nu\le t^2}\int h\,d\nu
=\inf_{\lambda\ge0}\left[\lambda t^2+\int M(1-\lambda a)_+\,d\nu\right].
\]

这是有饱和区的模，不能当成全局严格增 gauge；精确长度为 \(\sum_k[\int a(1-a)^kh\,d\nu]^{1/2}\)。[CM-M Theorem 7]

**CM-GAUSSIAN：**目标 \(\beta=N(m_0,Q^{-1})\)、\(Q\succ0\)，Gaussian Gibbs 概率 \(p_i>0,\sum_i p_i=1\)，\(D=\operatorname{diag}(p_i/Q_{ii})\)，\(\zeta=\lambda_{\min}(Q^{1/2}DQ^{1/2})\)。这里 \(W_{2,Q}\) 的运输成本为 \((x-y)^TQ(x-y)\)，而原生条件残差是
\[
\mathcal R_Q(\mu)^2=\sum_i p_iQ_{ii}\int
 W_2\!\left(\mu_i(\cdot\mid x_{-i}),\beta_i(\cdot\mid x_{-i})\right)^2
 \,\mu_{-i}(dx_{-i}).
\]
每步按 \(p_i\) 选坐标，用目标 \(\beta\) 的 Gaussian 全条件律重新抽样；上式的条件距离是**一维通常** \(W_2\)，外层才用 \(Q\)-运输成本。在全部有限二阶矩律上，\(\mathcal R_Q\) 有
\(W_{2,Q}(\mu,\beta)\le\zeta^{-1/2}\mathcal R_Q(\mu)\)，常数局部、全局均锐；收缩因子 \(\sqrt{1-\zeta}\) 有效但原文未宣称锐。[CM-M Theorem 8]

**CM-MOMENT / C126：**[自足陈述与证明](topics/random_markov/moment_recoupling.md#mr-moment) 令非负有限状态函数 \(e,c\) 有共同零点 \(s\) 与 \(e(a),c(a)>0\) 的非零 excursion，\(1\le p,r<\infty,q>0,K<\infty\)。对**全部有限支撑概率律**的
\(\|e\|_{L^p}\le K\|c\|_{L^r}^q\)
恰等价于同一 \(K\) 的全部状态点态界 \(e(x)\le Kc(x)^q\) 与 \(pq\le r\)。小质量混合给必要性。故 \(p=r=2,q>1\) 的直接 RMS 提升会失败；要保留高阶幂，可另用 \(r\ge2q\) 的矩或先在合法耦合上复合证书。law-space 必要性还要求不变目标支持于闭 \(S\)、残差在平稳律上为零和更新 excursion 的输出远离 \(S\)；不是任意 Markov 残差的普遍 no-go。[CM-M Proposition M]

## 4. 跨线超边：需要什么才能接上

本节的原算子另记 \(F_{\mathrm{PPA}}:X\rightrightarrows X\)，\(r_{F_{\mathrm{PPA}}}(x)=d(0,F_{\mathrm{PPA}}(x))\)。下列第一行只在局部明确识别 \(F_{\mathrm{PPA}}^{-1}(0)=\Omega=G^{-1}(C)\) 后使用；上文的最小面 \(\mathfrak F\) 不参与该残差。

| 拟连接 | 必须额外输入 | 当前状态 |
|---|---|---|
| 锥 MSCQ → RLEB 的 EB | 同一局部零集，\(d(G(x),C)\le\chi(r_{F_{\mathrm{PPA}}}(x))\) | 才得 \(\psi_{F_{\mathrm{PPA}}}=\kappa\chi\)；反射、步长、coverage、留域独立 |
| 条件残差 → 普通 \(W_2\) EB | \(d_{W_2}\le\mathsf W_\nu\) | 只传充分界；必要性、锐性、相对率不自动传 |
| 同步耦合能量 → 随机 RL | 同一耦合实现几何、实际目标与残差 | 原生匹配仍是额外假设；不能造概率反射 \(2\mu P-\mu\) |
| 收缩 → 原 \(\Psi\) 的 EB | [C127](topics/random_markov/moment_recoupling.md#mr-recoupling) 的同一紧状态随机表示、同一不变律集及指定律类中 \(d(\mu P)\le c_0d(\mu)\)、\(c_0<1\)；趋近原 \(\Psi\) inf 的**输入最优**耦合满足 \(\Delta_{\eta_j}\le\chi D_{\eta_j}^2\) | \(D_\eta\) 是同噪声同步位移差，\(\Delta_\eta=A_\eta-d(\mu P)^2\) 是回耦损失；仅在这些合取条件下给系数 \((1+\sqrt\chi)/(1-c_0)\)，非无条件逆定理 |

条件残差一般不满足原同步能量式：二 bit 公平目标、等概率坐标刷新、状态按 \(00,01,10,11\) 排列，输入律为 \((1/2,0,1/4,1/4)\) 时，\(E=d_{W_2}(\mu,\pi)\)、\(E_+=d_{W_2}(\mu P,\pi)\) 满足 \(E^2=1/4,E_+^2=1/8,\mathcal R^2=1/4\)。这是针对 \(E_+^2+\mathcal R^2\le E^2\) 的反例；不能把 \(D_\eta\) 静默替换为 \(\mathcal R\)。[CM-C §10；CM-M §§7–8]

## 5. 来源与开放门

| 别名 | 路径／定位 |
|---|---|
| CM-C | [锥证明包](../history/sources/次单调论文研究/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md)，§§2–10 |
| CM-M | [Markov 定理包](../history/sources/次单调论文研究/MARKOV_PAPER_THEOREM_PACKAGE.md)，Definitions §1、Theorems 1/F/2/4/6–8、Propositions 9/10/M |
| CM-H | `history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/` 下 `02_锥优化_CRSC_MSCQ/03_核心证明审计/` 和 `03_随机与Markov理论/` 的逐题审计 |
| CM-N | [9/21 总账](../history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md)，§§2–3；[no-go](../history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)，N03/N04/N13 |

开放门包括锥正式版及近邻定理的逐条优先权核查、随机原生匹配接口、同核不同表示的严格证书分离。9/21 另报告更强 Markov 模型及结构性恢复并停止继续升级反例；相关后期原证明未附全，不在本页补造。已有组件不新不等于整个联合命题不新；内部 PASS 也不等于原创性已证。
