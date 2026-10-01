# 初值稳定性：文献综合、可直接使用的基线与下一步研究边界

日期：2026-09-19。综合依据：完整阅读本轮 01–05 五组报告及修订稿 §5.2；额外直接核对 Wiśnicki Lemma 1、Bauschke–Moursi–Wang Proposition 3.13/Corollary 3.14、Combettes–Pennanen Theorem 3.1 的原文。只综合与本任务有关的接口，不修改研究稿、不重新审核原 RLEB 的无关内容。

## 1. 给用户的直白结论

**方向是对的：在保留多解的前提下，加适当的附加条件，可以把 RLEB 已有的快速收敛升级成初值到最终解的 Hölder、Lipschitz，乃至光滑稳定性。这个问题和多条正面机制都已有人研究。**

但不能把“次单调性”当作一个唯一的既定概念。当前的 Hölder RL、普通 hypomonotonicity、cohypomonotonicity，以及早期 submonotonicity 的定义不同，其步长窗口和能推出的结论也不同。

最实用的已有经验是：

1. **非扩张 + 轨道收敛**：极限选择直接为 1-Lipschitz，允许许多解，不需要强单调或唯一性。
2. **单步有限 Lipschitz + 共同几何点尾**：极限选择有某个正 Hölder 阶；这已有直接先例。
3. **每步允许扩张，但所有迭代的总放大有界**：极限仍 Lipschitz；“沿轨道可和扩张”是一个标准充分证书。
4. **要保留 RLEB 的真正非 Lipschitz 法向几何**：应限制沿解集方向的累计放大，并同时控制法切耦合，不能只把整个单步映射强行改为 Lipschitz。

最值得发展的不是“首次研究初值”，而是：**从容易检查的 RLEB 算子图条件中，提取一个弱的切向稳定性证书，保留法向 Hölder 尖点和多解，并超出目前 §5.2 的三角解耦情形。**

这里的“弱”是研究目标，不是已经证明的假设集合包含关系。下述候选与普通 hypomonotonicity 不是简单包含关系，但能保留后者排除的一些法向非 Lipschitz 稳定模型；它是面向当前奇异结构的另一套充分证书。目前没有证明一个不依赖目标稳定阶、解集几何和坐标选择的“绝对最弱条件”。

## 2. 固定对象、共同域和分类含义

本报告只研究固定算法

\[
x_{k+1}=T x_k,\qquad \Pi_T(x)=\lim_{k\to\infty}T^kx,
\]

对同一初值域内任意两点的估计。除非另有说明，先有共同初值邻域 \(U\)、共同轨道区域 \(W\)，所有轨道留在 \(W\) 并点收敛。RLEB 在本次修订稿中提供的可调用接口包括

\[
\sup_{x\in U}\|T^kx-\Pi_Tx\|\le M\sigma^k,\qquad 0<\sigma<1.
\tag{2.1}
\]

\(\sigma\) 是共同**点尾**因子。它不是自动等于到解集距离的实际因子 \(q\)，也不是自动等于保守证书 \(\kappa\)。一般 Hölder 步长传递中可有 \(\sigma=q^\gamma\)。

一般图块接口仍为 \(T=J_{\mathcal G}\)。若写成完整 \(J_{\lambda F}\)，必须在共同轨道区证明完整纤维相同。以下条件都不能代替这一检查。

本报告使用四种证据级别：

- **A：已发表的直接定理**，明确研究实际迭代极限/相位映射的正则性。
- **B：已发表结果的立即组合**，例如先证 resolvent 非扩张，再取迭代极限；不冒称原论文另有同名极限选择定理。
- **C：标准乘积、截断平衡或离散 Gronwall 推论**，推导可直接写出，不申报方法创新。
- **D：仍需研究的桥接**，现有报告没有证明一般定理；不得把候选接口或未找到文献写成新定理。

最新预印本另标“预印本直接结果”，不伪装为 A 类已发表成果。

## 3. 附加条件的层级表

以下是按用途排列的路线，不是所有行两两包含的强弱总序。

| 附加条件/路线 | 能准确得到什么 | 证据级别与原始入口 | 关键边界 |
|---|---|---|---|
| \(T\) 在共同轨道区非扩张；averaged 是常见来源 | 收敛时 \(\Pi_T\) 为 1-Lipschitz | B；非扩张性取极限是 C，经典 averaged 收敛提供另一接口 | 非扩张本身不保证 Picard 收敛，\(T=-I\) 即反例；无限维 averaged 通常只先给弱收敛 |
| \(\langle u-v,a-b\rangle\ge-\rho\|a-b\|^2\)，且 \(\lambda\ge2\rho\) | \(J_{\lambda F}\) 非扩张；共同轨道收敛后 \(\Pi_T\) 非扩张 | B；BMW Proposition 3.13(iii),(v)、Corollary 3.14；CP Lemma 2.4、Theorem 3.1 | \(\lambda>2\rho\) 才给严格 averaged 参数；边界只能靠另一个收敛证明。局部完整覆盖、maximality 等不能省 |
| 普通 \(\langle u-v,a-b\rangle\ge-\rho\|u-v\|^2\)，\(\lambda\rho<1\)，加 (2.1) | 正阶 Hölder \(\Pi_T\)，指数见 §4 | B；BMW 的单步接口 + Wiśnicki Lemma 1 | 普通 hypo 要小步长，cohypo 要足够大步长；同一 \(\lambda\) 还须满足 RLEB 严格兼容 |
| 单步 \(L\)-Lipschitz + 统一几何增量/点尾 | 正阶 Hölder 的实际极限映射 | A：Wiśnicki 2014 Lemma 1；当前共同局部域版本是其标准局部化/直接计算 | 单步 Lipschitz 单独不够，不能省共同尾界 |
| \(\sup_k\operatorname{Lip}(T^k|_U)\le C\) | \(\Pi_T\) 为 \(C\)-Lipschitz | C，直接取极限 | 条件可以允许某一步扩张；但从图结构验证所有幂的统一界不一定容易 |
| \(W_k=T^kU\) 上 \(\operatorname{Lip}(T|_{W_k})\le1+\epsilon_k\)，\(\sum\epsilon_k<\infty\) | \(\operatorname{Lip}(\Pi_T)\le\exp(\sum\epsilon_k)\) | C，乘积估计 | \(\epsilon_k\) 必须同时控制所有初值对；仍要求全方向 Lipschitz，可能排除正常的 Hölder 尖点 |
| 三角法向收缩 + 切向 Dini/可和缺陷 + 法向 Hölder 输入 | 切向 Lipschitz、法向 \(\gamma\)-Hölder 的混合极限界 | C；当前稿 §5.2 及 §5 下述直接放宽 | 已有可用正面结论；不能扩成全部 signed-Schur 图块 |
| 光滑解流形 + 正常吸引/适当速率支配 | 相位/极限映射可光滑 | A：Beyn 1993 Theorem 2.2；EKR 2018 Corollary 2（连续流） | 连续流不可直接套不可逆离散 resolvent；不能只写“解集光滑”或流形上切向导数为恒等 |
| partial smoothness / finite identification | 提供活动流形约化，不单独给 \(\Pi_T\) 的两初值估计 | 所需桥接属 D；Hare–Lewis Theorem 5.3 是已发表的辨识接口，不是本对象的 A 类定理 | 活动流形未必是解集；逐轨道辨识时刻不自动统一 |
| clean intersection + 特定光滑投影/牛顿结构 | 特定算法已有解点可微、局部相位或光滑回缩结论 | A：Schost–Spaenlehauer Theorems 4.1–4.2；另有 2026 直接预印本 | 解点可微不等于整个邻域两点 Lipschitz；切丛域不等于任意环境初值域 |
| 唯一局部极限、强度量正则、tilt stability 等 | 若全体近初值都收敛到同一点，则 \(\Pi_T\) 常值 | B，但这是多解问题的平凡化，不是理想的新条件 | tilt 文献主要比较数据/右端扰动，不能改名为非唯一解的初值选择 |
| 保留法向 \(\gamma<1\)，从原算子图导出非三角切向增益及回授可和 | 目标为共同域 Hölder/Lipschitz 选择 | D，建议的真正研究任务 | §6 给候选接口；尚未覆盖一般原 RLEB 图块，也未证明最弱性/优先权 |

## 4. 两条已经足够直接回答“次单调性下有人研究吗”的路线

### 4.1 普通 hypomonotonicity：小步长，一步 Lipschitz，再组合统一尾界

设 \((u,a),(v,b)\) 是两条轨道调用的同一受控图域中的图点，\(x=u+\lambda a\)、\(y=v+\lambda b\)。由

\[
\langle u-v,a-b\rangle\ge-\rho\|u-v\|^2
\]

得到

\[
(1-\lambda\rho)\|u-v\|^2\le\langle u-v,x-y\rangle.
\]

所以 \(\lambda\rho<1\) 时，存在性/覆盖另外成立的 resolvent 有

\[
\|Tx-Ty\|\le L\|x-y\|,\qquad L=(1-\lambda\rho)^{-1}.
\tag{4.1}
\]

结合 (2.1)，

\[
\|\Pi_Tx-\Pi_Ty\|\le L^n\delta+2M\sigma^n,
\quad\delta=\|x-y\|.
\]

若 \(L>1\)，平衡得

\[
\|\Pi_Tx-\Pi_Ty\|\le C\delta^\theta,
\qquad
\boxed{\theta=\frac{\log(1/\sigma)}{\log L+\log(1/\sigma)}>0.}
\tag{4.2}
\]

这正是 Wiśnicki Lemma 1 的证明机制。其原文要求完备有界空间上的统一几何增量；这里已知点尾，直接作同一计算即可。局部 Lipschitz 只对小比较尺度有效时，可取截断步 \(n\) 使所有 \(j\le n\) 都有 \(L^j\delta\le O(\delta^\theta)\)，闭合比较尺度；还须由原预算保证两条轨道留在共同图域。[Wiśnicki 原文 Lemma 1](https://arxiv.org/pdf/1204.6464v2)

**这条路线是现成的正面基准，不是新的抽象定理。** 当前 cap 反例以及一些本来稳定的平方根图都不存在有限普通 hypo 常数，所以这条路线会排除它们；这不意味着普通 hypo 与 §6 候选的整套假设存在逻辑包含关系。

不能省掉统一尾界的一个精确反例是：\(f(u)=(u^2-1)^2/4\)、\(0<\lambda<1\)，完整 prox 是 \(h(u)=(1-\lambda)u+\lambda u^3\) 的逆，故单步全局 Lipschitz。然而其极限选择为 \(\Pi(x)=\operatorname{sgn}(x)\)（\(\Pi(0)=0\)），在零点不连续。取 \(x_n=h^n(1/2)\downarrow0\)，有 \(T^nx_n=1/2\)、\(\Pi(x_n)=1\)，故零点的任意共同邻域均无一致消失点尾。它不反驳已建立的严格 RLEB 共同预算，而是说明“单步好”与“无穷步好”之间确实需要桥梁。

### 4.2 Cohypomonotonicity：大步长，非扩张，所以多解选择也稳定

若改为

\[
\langle u-v,a-b\rangle\ge-\rho\|a-b\|^2,
\]

则恒等式给

\[
\|x-y\|^2\ge\|u-v\|^2+\lambda(\lambda-2\rho)\|a-b\|^2.
\tag{4.3}
\]

因此 \(\lambda\ge2\rho\) 时 \(T\) 非扩张；\(\lambda>2\rho\) 时 averaged 参数为

\[
\alpha=\frac{\lambda}{2(\lambda-\rho)}<1.
\]

共同域内轨道一旦收敛，取极限即有

\[
\boxed{\|\Pi_Tx-\Pi_Ty\|\le\|x-y\|.}
\]

这保留多解，不需要强单调。BMW Proposition 3.13、Corollary 3.14 给 resolvent 对应；Combettes–Pennanen Theorem 3.1 直接研究局部 cohypomonotone PPA，在其共同局部域、参数余量和误差预算等条件下给轨道收敛。这里的两初值结论是该类结果加 (4.3) 的立即推论，不冒称原文另有同名定理。[BMW 原文](https://arxiv.org/html/1902.09827v1)，[CP 原文](https://pcombet.math.ncsu.edu/sicon3.pdf)

必须保留边界：在无限维只得到弱收敛时，不能称强收敛；非扩张极限估计仍可由范数弱下半连续性得到，但用户当前有限维/强收敛语境没有此歧义。最大性和局部完整纤维的作用也不能由 (4.3) 一条估计代替。

此外，改变步长以满足 hypo/cohypo 窗口后，必须在该同一步长重新核实 RLEB 兼容及覆盖，不能沿用旧常数。全域 maximal cohypomonotone 在上述非扩张窗口还有闭凸零集结论（BMW Corollary 3.15），所以这也不是免费覆盖任意弯曲解流形的弱条件。

## 5. 当前稿 §5.2 已经具有的“弱而自然”正面内容

当前稿明确研究

\[
T(a,r)=(a+B(a,r),qr),\quad B(a,0)=0,
\]

以及切向缺陷 \(\operatorname{Lip}_aB(\cdot,r)\le Cr^\eta\) 和法向 \(\gamma\)-Hölder 输入。它已经在原反例之外给出严格正面答案，不是只有负面结果。

将正幂 \(Cr^\eta\) 放宽为非减模 \(\omega(r)\)，并要求

\[
\boxed{\sum_{k\ge0}\omega(Rq^k)<\infty,}
\tag{5.1}
\]

同一标准证明给

\[
\|\Pi_a(a,r)-\Pi_a(b,s)\|
\le e^{\sum_k\omega(Rq^k)}
\left(\|a-b\|+\frac{H}{1-q^\gamma}|r-s|^\gamma\right).
\tag{5.2}
\]

对非减模，(5.1) 与零点附近 Dini 可积性

\[
\int_0^R\frac{\omega(t)}t\,dt<\infty
\]

通过几何分段互相控制；例如 \(\omega(t)=1/\log(e/t)^{1+\varepsilon}\)（小尺度）可用，远不必要求正幂衰减。这只是 **C 类标准放宽**，仍是三角模型，不是已经完成一般 RLEB 创新。

其直观含义是：轨道越来越靠近解集时，沿解集方向每次允许有一点额外放大，但**一生累计的额外放大必须有限**。

这还解释为何“快一点”不能替代结构：再快的法向收敛也不能自动给两条轨道的切向增益预算。

## 6. 建议的研究候选：法向 Hölder 坐标中的可和切向增益及可和回授

### 6.1 先给准确定位

建议优先考察：**共同尾半径 \(r_k\) 下的切向增益 \(\omega(r_k)\) 可和，且法向扰动反馈到切向、切向反馈到法向的总效应可以闭合。**

不能只写 \(\sum\omega(r_k)<\infty\) 就宣布任意非三角耦合的极限稳定；它只限制一个块，另一个块仍可能反复产生敏感度。下面给一个完全可检查的充分接口，说明目标可以允许非三角耦合。它不是“绝对最弱条件”，其最后乘积证明也不新；真正待研究的是从 RLEB 的原始图几何验证它或进一步弱化它。

### 6.2 一个不以未知 \(\Pi_T\) 为假设的块估计

本接口预先固定同一初值域 \(U\)、同一工作域 \(W\) 和一张法切坐标图 \(\Phi:x\mapsto(a(x),n(x))\)。假设对所有 \(x\in U\) 和所有 \(k\ge0\)，\(T^kx\in W\)，且轨道已知收敛到 \(\Pi_Tx\in S\cap W\)；同一张图覆盖全部 \(\bigcup_{k\ge0}T^kU\) 及其极限。\(\Phi\) 和 \(\Phi^{-1}\) 在这一共同范围上分别具有统一 Lipschitz 常数 \(L_\Phi,L_{\Phi^{-1}}\)，而非仅逐点局部常数；\(S\cap W\) 恰对应 \(n=0\)。设预先给定 \(r_k\downarrow0\)，并对全部 \(x\in U,k\ge0\) 有 \(\|n(T^kx)\|\le r_k\)。可用 RLEB 距离预算获得 \(r_k\)，但坐标与真实距离的比较须另外核验。若只有更弱的坐标正则性，最终 Euclidean 稳定阶也必须按坐标模重新换算。

法向变换 \(\chi\) 固定、与所求 \(\Pi_T\) 无关，满足 \(\chi(0)=0\)，并在上述共同法向范围上有统一估计 \(\|\chi(n)-\chi(m)\|\le H_\chi\|n-m\|^\gamma\)，其中同一 \(H_\chi<\infty\) 和 \(0<\gamma\le1\) 适用于全部法向坐标对。以下称 \(w=\chi(n)\) 为坐标时，另要求 \(\chi\) 在该法向范围内是到其像的同胚；继承估计本身只使用前述统一 Hölder 性。一维典型选择是

\[
\chi(n)=\operatorname{sgn}(n)|n|^\gamma,\qquad0<\gamma<1.
\tag{6.1}
\]

它在有界尺度为 \(\gamma\)-Hölder，保留法向尖点，不是先假设整个 \(T\) 在原 Euclidean 坐标 Lipschitz。记两个状态在此坐标中的差

\[
u=\|a-b\|,\qquad v=\|w-z\|.
\]

对每个 \(k\ge0\) 及每一对 \(x,y\in T^kU\)，以 \(u,v\) 表示其上述坐标差、\(u_+,v_+\) 表示 \(Tx,Ty\) 的坐标差，要求以下**两点**块条件使用相同的 \(A,\vartheta,\omega,b\)，不依赖所选轨道对：

\[
\begin{aligned}
u_+&\le[1+\omega(r_k)]u+A v,\\
v_+&\le\vartheta v+b(r_k)u,
\end{aligned}
\qquad
0\le\vartheta<1,\quad 0\le A<\infty,
\tag{6.2}
\]

其中 \(\omega,b\ge0\)，并要求

\[
\sum_k[\omega(r_k)+b(r_k)]<\infty.
\tag{6.3}
\]

这里 \(b\) 可以非零：法向演化可以依赖切向变量，所以不是 \(r_+=qr\) 那种三角解耦。假设同时比较两条轨道，不能换成逐轨道或解点锚定估计。也不能将 \(v\) 不加检查地改成 \(\|n-m\|^\gamma\)：后者与坐标差 \(\|\chi(n)-\chi(m)\|\) 不同，随意替换会给反馈块增加不真实的超一阶限制。

选 \(c>0\) 满足 \(A+c\vartheta\le c\)，令 \(d_*=u+cv\)。直接有

\[
d_{*,+}\le[1+\omega(r_k)+cb(r_k)]d_*.
\]

于是

\[
d_{*,k}\le
\exp\!\left(\sum_j[\omega(r_j)+cb(r_j)]\right)d_{*,0}.
\tag{6.4}
\]

取极限，因全部极限仍在同一坐标片且 \(\chi(0)=0\)，法向坐标消失。解集参数化 \(a\mapsto\Phi^{-1}(a,0)\) 有统一 Lipschitz 常数 \(L_S\le L_{\Phi^{-1}}\)，故 (6.4) 给出

\[
\|\Pi_T(a,n)-\Pi_T(b,m)\|
\le C\bigl(\|a-b\|+\|\chi(n)-\chi(m)\|\bigr)
\le C'\bigl(\|a-b\|+\|n-m\|^\gamma\bigr).
\tag{6.5}
\]

准确地，令 \(E=\sum_j[\omega(r_j)+cb(r_j)]\)，对任意原始初值 \(x,y\in U\) 和 \(\delta=\|x-y\|\)，有

\[
\|\Pi_Tx-\Pi_Ty\|
\le L_Se^E\bigl(L_\Phi\delta+cH_\chi L_\Phi^\gamma\delta^\gamma\bigr).
\]

在共同有界比较尺度 \(\delta\le D\) 上，再用 \(\delta\le D^{1-\gamma}\delta^\gamma\) 得到 Euclidean \(\gamma\)-Hölder 结论。既有轨道收敛、共同留域和全部统一常数均是本接口的假设，不由块估计自动替代。

**(6.2)–(6.5) 是标准加权乘积/小增益推论，属于 C；从原算子图、最小残差与全对 RL 推出 (6.2) 的可操作新定理，才属于 D。** 它没有预先假设 \(\Pi_T\) 正则，但仍须承认验证 (6.2) 可能不容易。

### 6.3 它确实允许非三角与法向非 Lipschitz：一个标准说明模型

考虑

\[
T(a,n)=\bigl(a+B(a)|n|^\gamma,\ q(a)|n|\bigr),
\quad 0<q_-\le q(a)\le q_+<1,
\tag{6.6}
\]

其中 \(B\) 有界 Lipschitz，\(q\) Lipschitz；为避免留域问题，可先取全切向域上的这些统一假设。只要 \(q\) 真依赖 \(a\)，它便不是三角法向迭代。

在 (6.1) 坐标中，

\[
(a,w)\longmapsto
\bigl(a+B(a)|w|,\ q(a)^\gamma|w|\bigr).
\]

若 \(|n|,|m|\le r_k\)，可取

\[
\omega(r_k)=\operatorname{Lip}(B)r_k^\gamma,\quad
A=\|B\|_\infty,\quad
\vartheta=q_+^\gamma,
\quad b(r_k)=\operatorname{Lip}(q^\gamma)r_k^\gamma.
\]

法向幅度满足 \(r_k=Rq_+^k\)，故 (6.3) 成立；输出由 (6.5) 稳定。\(B\ne0\) 时原坐标单步通常仍在 \(n=0\) 非 Lipschitz。常数 \(B,q\) 的平方根特例包含原二维稳定接缝的机制。

这是用于说明候选条件不空、不强制解唯一、不强制原坐标全方向 Lipschitz的**稳定性模型**；本轮没有为 (6.6) 的任意变系数版本证明完整多值 resolvent、全部 RL 常数和严格残差兼容，不能把它列为已经完成的新 RLEB 构造。

### 6.4 为什么排除当前坏例，而不排除正常的法向 Hölder

坏例在固定 \(r>0\)、\(0<\varepsilon<r\) 比较 \((z,\varepsilon,r)\) 和 \((z,0,r)\)，法向差为零，但切向 \(p\) 差满足

\[
u=\varepsilon,\qquad
u_+=\varepsilon+\sqrt\varepsilon,
\qquad \frac{u_+}u=1+\varepsilon^{-1/2}\to\infty.
\tag{6.7}
\]

所以任何有限 \(\omega(r)\) 都无法满足 (6.2) 的第一行。这针对的正是 cap 的切向重复放大。

而 \(T_0(z,r)=(z+\sqrt{|r|},|r|/4)\) 在原坐标并非 Lipschitz，却有

\[
\Pi_{T_0}(z,r)=(z+2\sqrt{|r|},0),
\]

满足正阶两点 Hölder。法向重参数化后的估计保留了它。因此这一候选并非用“删掉所有 \(\gamma<1\) 情形”换稳定性。

## 7. 文献的准确对应与尚未核完之处

以下是最影响决策的原始文献。定理号按所链接版本；早期原页未取得的单列，不用转引冒充直接阅读。

| 作者、准确题名 | 标识与定位 | 已覆盖/未覆盖 |
|---|---|---|
| Andrzej Wiśnicki, *Hölder Continuous Retractions and Amenable Semigroups of Uniformly Lipschitzian Mappings in Hilbert Spaces* | TMNA 43 (2014), 89–96；[DOI 10.12775/TMNA.2014.006](https://doi.org/10.12775/TMNA.2014.006)；[arXiv:1204.6464v2](https://arxiv.org/pdf/1204.6464v2)，Lemma 1 | A：Lipschitz 迭代、统一几何增量导出实际极限 Hölder。主 Theorem 2 另构造辅助回缩，不能混同任意原算法极限 |
| Heinz H. Bauschke, Walaa M. Moursi, Xianfu Wang, *Generalized Monotone Operators and Their Averaged Resolvents* | Math. Programming 189 (2021), 55–74；[DOI 10.1007/s10107-020-01500-6](https://doi.org/10.1007/s10107-020-01500-6)；[arXiv:1902.09827v1](https://arxiv.org/html/1902.09827v1)，Proposition 3.13、Corollary 3.14、Proposition 6.3(iv) | 单步 resolvent 的非扩张/averaged 及弱凸 prox 的 Lipschitz；与收敛组合为 B。不是单独给全部 \(\Pi_T\) 的定理 |
| Patrick L. Combettes, Teemu Pennanen, *Proximal Methods for Cohypomonotone Operators* | SICON 43(2) (2004), 731–742；[DOI 10.1137/S0363012903427336](https://doi.org/10.1137/S0363012903427336)；[原文](https://pcombet.math.ncsu.edu/sicon3.pdf)，Lemma 2.4、Theorem 3.1 | 直接研究该类局部 PPA 收敛；固定精确算法再加非扩张继承即得 B 类多初值结论 |
| Wolf-Jürgen Beyn, *On Smoothness and Invariance Properties of the Gauss-Newton Method* | NF&AO 14(5–6) (1993), 503–514；[DOI 10.1080/01630569308816536](https://doi.org/10.1080/01630569308816536)；[原始扫描全文](https://noah.nrw/ubbihs/download/pdf/5114560)，Theorems 2.1–2.2、3.1 | A：\(F\in C^{k+1}\)、满行秩零流形，GN 的共同局部极限映射 \(C^k\)，有稳定叶；非唯一解。不是一般 proximal 或退化 Hölder 图 |
| Jaap Eldering, Matthew Kvalheim, Shai Revzen, *Global Linearization and Fiber Bundle Structure of Invariant Manifolds* | Nonlinearity 31 (2018), 4202–4245；[DOI 10.1088/1361-6544/aaca8d](https://doi.org/10.1088/1361-6544/aaca8d)；[arXiv:1711.03646v3](https://arxiv.org/pdf/1711.03646v3)，Theorem 1、Corollary 2、式 (11) | A：正常吸引流形的相位投影，在足够光滑流及速率支配下 \(C^k\)。流形全为平衡点时对应静态解选择；连续流不可不经论证用于不可逆离散映射 |
| Éric Schost, Pierre-Jean Spaenlehauer, *A Quadratically Convergent Algorithm for Structured Low-Rank Approximation* | FoCM 16 (2016), 457–492；[DOI 10.1007/s10208-015-9256-x](https://doi.org/10.1007/s10208-015-9256-x)；[arXiv:1312.7279](https://arxiv.org/pdf/1312.7279)，Theorems 4.1–4.2 | A 的有限范围：二次点收敛，极限在每个解点可微，导数为切空间投影；不能升级为完整邻域 \(C^1\) |
| Warren L. Hare, Adrian S. Lewis, *Identifying Active Constraints via Partial Smoothness and Prox-Regularity* | J. Convex Anal. 11(2) (2004), 251–266；[原文](https://journalofconvexanalysis.com/articles/jca11017/jca11017.pdf)，Theorem 5.3；未列 DOI | 已发表辨识接口，不是 A 类两初值结论；共同辨识时刻、解流形与后续敏感度均需另验 |
| Dmitriy Drusvyatskiy, Adrian S. Lewis, *Tilt Stability, Uniform Quadratic Growth, and Strong Metric Regularity of the Subdifferential* | SIOPT 23(1) (2013), 256–267；[DOI 10.1137/120876551](https://doi.org/10.1137/120876551)；[原文](https://people.orie.cornell.edu/aslewis/publications/13-tilt.pdf)，Theorem 3.3 | 数据/倾斜扰动的孤立局部解稳定；不是保留非孤立解集的 \(\Pi_T\) 定理 |
| R. A. Poliquin, R. Tyrrell Rockafellar, *Prox-Regular Functions in Variational Analysis* | TAMS 348 (1996), 1805–1838；[DOI 10.1090/S0002-9947-96-01544-9](https://doi.org/10.1090/S0002-9947-96-01544-9)；[原文](https://sites.math.washington.edu/~rtr/papers/rtr157-ProxRegular.pdf)，Theorems 3.2、4.4 | attentive 局部化与单步 prox 正则；再加共同点尾才可走 B 类路线；不能直接升级完整纤维 |
| R. Tyrrell Rockafellar, *Characterizing Firm Nonexpansiveness of Prox Mappings Both Locally and Globally* | JNCA 22(5) (2021), 887–899；[原文](https://sites.math.washington.edu/~rtr/papers/rtr254-ProxMaps.pdf)，Theorems 2–3；未核到 DOI | 局部变分凸性与 localized prox firm nonexpansive 的直接结构接口；迭代极限为 B 类组合 |

需列入相关工作但不能写成已发表结论的两项：

- Shixiang Chen, Yixiao He, Wen Huang, *Retractions by Alternating Projections*，[arXiv:2605.17384v2](https://arxiv.org/html/2605.17384v2)，Theorems 2–3：clean intersection 加明确导数/逼近条件，得到切丛零截面邻域上的 \(C^1/C^2\) 极限回缩；**该定理的输入域不是任意环境初值邻域**。
- Dengyu Zheng, Shixiang Chen, *A Regularized Newton-Type Method for Manifold–Affine Intersection Problems under Intrinsic Transversality*，[arXiv:2606.31738v3](https://arxiv.org/pdf/2606.31738v3)，Theorems B.1–B.2，2026-09-17 版本：固定正则化参数情形给仿射初值域上的 \(C^1/C^2\) 极限；**不能将主文另一超线性参数情形直接附加同样结论**。

尚未直接取得原页、不得作已闭环优先权结论：Spingarn 1982 *Submonotone Mappings and the Proximal Point Algorithm*，[DOI 10.1080/01630568208816109](https://doi.org/10.1080/01630568208816109)；Pennanen 2002 *Local Convergence of the Proximal Point Algorithm and Multiplier Methods without Monotonicity*，[DOI 10.1287/moor.27.1.170.331](https://doi.org/10.1287/moor.27.1.170.331)；Fenichel 1977 Theorem 5 与 HPS 原始稳定叶书页。部分后续原文明确转引它们，但这不是最早优先权的第一手关闭。

## 8. 应加入当前论文，还是另立未来定理？

**当前论文宜加入简洁的“已有正面基线”，而不是把这些经典结果包装成新主定理。** 本轮没有改稿；建议作者后续授权时作下列范围明确的增补：

1. 加一条“Lipschitz 单步 + RLEB 共同尾界”的推论，写出 (4.2)，引 Wiśnicki；说明普通 hypo、\(\gamma=1\) 的 RL 是可检查来源。
2. 加一段 cohypomonotonicity/非扩张的多解正面例，强调不必强单调或唯一解。
3. 保留 §5.2；如果扩成 Dini 缺陷，只标标准 Gronwall 放宽。
4. 在讨论中列出光滑回缩先例及适用域，说明本文反例没有否定这些更强结构。

**未来研究才以“图几何 → 非三角各向异性累计稳定性”为主目标。** 至少应同时达到：

- 条件从原始图/残差、已知局部坐标或可计算广义导数验证，不直接假设未知 \(\Pi_T\) 的正则性；
- 有共同初值域和共同轨道预算，不只逐轨道或锚定 calmness；
- 覆盖真正 \(\gamma<1\)、非全方向 Lipschitz、非三角耦合的新模型；
- 与完整 resolvent、真实 min-residual、全对 RL 和严格兼容一起闭合；
- 比较 §5.2、经典加权乘积估计、光滑稳定叶/投影回缩，准确指出新增桥接或可验证性，不以“换名字”作为贡献。

终结判断：**已有正面理论很多，可以立即帮助补齐当前论文的平衡叙述；最有价值的下一步不是再证明标准乘积估计，而是把“累计切向放大有限”真正变成保留 RLEB 奇异优势、又能在原算子上检查的条件。该桥接目前仍未完成。**
