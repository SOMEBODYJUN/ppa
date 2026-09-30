# Baire 泛性、算子空间与初值选择：原始文献核查

日期：2026-09-20。角色：文献与适用范围审核；不修改原 RLEB 或 solution-selection 稿。

## 结论先行

用户提出的“比较好类、坏类有多大”有成熟的泛函分析方法可用，但现成的非扩张／单调算子泛性定理**没有直接回答 RLEB 多解选择的坏类有多大**。原因有二：一是许多结论把典型算子变成唯一解，初值选择因而退化为常值；二是非扩张迭代只要逐点收敛，其极限选择本来就自动 1-Lipschitz。

最重要的实证警示：对同一个无限维 Hilbert 空间上的非扩张映射，bounded-uniform 拓扑下泛型具有唯一固定点，而 pointwise 拓扑下泛型没有固定点。因此不能先说“典型好／典型坏”再补拓扑。

## 1. 共同记号

令 (H) 为实 Hilbert 空间，

\[
\mathcal N(H)=\{T:H\to H:\operatorname{Lip}T\le1\},\quad
\mathcal J(H)=\{T:T\text{ firmly nonexpansive}\},
\]

\[
\mathcal M(H)=\{A:H\rightrightarrows H:A\text{ maximally monotone}\},\quad
J_A=(I+A)^{-1},\ R_A=2J_A-I.
\]

“有界集上一致”使用

\[
\rho_{bu}(T,U)=\sum_{m=1}^{\infty}2^{-m}
\frac{\sup_{\|x\|\le m}\|Tx-Ux\|}
{1+\sup_{\|x\|\le m}\|Tx-Ux\|}.
\]

“逐点”在可分域及非扩张类中可使用稠密序列 ((z_m)) 给出的

\[
\rho_{pt}(T,U)=\sum_{m=1}^{\infty}2^{-m}
\frac{\|Tz_m-Uz_m\|}{1+\|Tz_m-Uz_m\|}.
\]

以下 residual／第一纲均相对于明确写出的空间与拓扑。

## 2. 已直接核到原文的定理

### 2.1 Wang：maximal monotone、resolvent 的泛型唯一零点

Xianfu Wang, *Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent*, Nonlinear Analysis 87 (2013), 69–82；DOI **10.1016/j.na.2013.03.008**；[原始预印本 arXiv:1301.6443](https://arxiv.org/pdf/1301.6443)。以下编号按预印本。

- **Propositions 2.1、2.3、2.4**：((\mathcal N,\rho_{bu}))、((\mathcal M,\rho_{bu}(R_A,R_B)))、((\mathcal J,\rho_{bu}(2T-I,2U-I))) 完备，后两者与前者等距。
- **Theorems 2.14、2.15、2.16；Corollary 2.17**：分别得到泛型 (T)、(J_A)、(R_A) super-regular；后一联合结论同时控制 (J_A,R_A)，且 (A^{-1}(0)) 为单点。super-regular 指迭代在每个有界球上一致收敛到同一个点。
- **Corollaries 3.9、3.10**：严格收缩、强单调算子分别是第一纲，尽管它们稠密。
- **Theorem 2.13** 的可迁移前提是完备子空间、度量支配 (ho_{bu})，且严格收缩在该子空间稠密。

适用判断：它回答经典单调／非扩张大空间的泛性；不回答固定多解 RLEB 相对类。编号及上述假设已直接核到正文。

### 2.2 Planiden–Wang：真正 proximal 映射空间，而不只是所有 resolvent

Chayne Planiden、Xianfu Wang, *Most Convex Functions Have Unique Minimizers*；[arXiv:1410.1078](https://arxiv.org/pdf/1410.1078)。

空间为有限维

\[
\mathcal P=\{\operatorname{prox}_f:f\in\Gamma_0(\mathbb R^n)\},
\]

配 (ho_{bu})。**Corollary 3.5** 证明完备；**Proposition 3.6** 将它与凸次微分空间及“凸函数模加常数”空间等距对应。**Theorem 4.2**：prox super-regular 当且仅当 (f) 有唯一极小点。**Theorems 4.6–4.8**：唯一 fixed point／唯一 zero／唯一 minimizer 分别泛型。

适用判断：凸 proximal 版本的“泛型唯一解”已经是现有结果；仅将同一句话换成 PPA 术语，不是新贡献。本文限 (mathbb R^n)，不能据此无条件宣称无限维一般 proximal 空间结论。

### 2.3 Reich–Zaslavski：泛型适定性，不止存在唯一解

Simeon Reich、Alexander J. Zaslavski, *Convergence of Iterates of Typical Nonexpansive Mappings in Banach Spaces*, C. R. Math. Rep. Acad. Sci. Canada 27(4) (2005), 121–128；[作者原始预印本 ESI 1668](https://www.esi.ac.at/preprints/esi1668.pdf)。

设 (K\subset X) 非空、有界、闭、凸。空间

\[
\mathcal M_0=\{A:K\to X:\operatorname{Lip}A\le1,
\ \inf_{x\in K}\|x-Ax\|=0\}
\]

在 (d(A,B)=\sup_K\|Ax-Bx\|) 下为完备空间的闭子空间。**Theorem 1.1**：除去一个 (sigma)-porous 集，每个 (B) 有唯一 fixed point (x_B)；给定 (arepsilon>0)，存在 (delta>0)、邻域 (U(B)) 和有限步数 (q)，使附近算子的 (delta)-近似 fixed point 都位于 (x_B) 的 (arepsilon)-邻域，留在 (K) 的长度 (q) 轨道也进入该邻域。

注意 (A:K\to X) 未必是 self-map：对无限迭代的陈述必须保留“轨道有定义且留在 (K)”限制。它的适定性主要是近似 fixed point／算子扰动，不能冒充多解极限选择的 Hölder 定理。

### 2.4 Ravasini–Thimm：更换拓扑会反转结论

Davide Ravasini、Daylen K. Thimm, *Generic nonexpansive Hilbert space mappings*；[arXiv:2407.03881v2](https://arxiv.org/pdf/2407.03881)，核查版本日期 2025-08。

对无限维可分 Hilbert 空间中的闭凸 (C)，(mathcal N(C)) 配上面的 (ho_{pt}) 是完备可度量空间（§2）。(C) 称 somewhat bounded，是指存在 (x_0\in C)、有限维子空间 (F) 及 (alpha>0)，满足 (alpha B_F\subset C-x_0)，且 (F^perp\cap(C-x_0)) 有界（Definition 3.1）。

- **Theorem 3.4**：somewhat bounded 时，存在 fixed point 的映射包含稠密开集。
- **Theorem 4.1**：不满足该性质时，泛型没有 fixed point；特别适用于 (C=H)。
- **Corollary 3.7**：再有严格凸性时，泛型 fixed point 唯一。
- **Theorem 5.3**：闭、somewhat bounded、LUR 集上，泛型唯一 fixed point 且所有 Picard 轨道收敛。

适用判断：它不是 Wang 结论的反例，因为拓扑不同；却直接排除了“与拓扑无关的典型初值稳定”说法。

### 2.5 Bargetz–Dymond：强充分条件很小，不代表好行为很小

Christian Bargetz、Michael Dymond, *σ-porosity of the set of strict contractions in a space of non-expansive mappings*, Israel Journal of Mathematics 214 (2016), 235–244；DOI **10.1007/s11856-016-1372-z**；[arXiv:1505.07656](https://arxiv.org/pdf/1505.07656)。

设 Banach 空间的 (C) 有界、闭、凸且至少两点。非扩张 self-map 空间配一致距离完备。**Theorem 2.1**：所有严格收缩组成 (sigma)-porous 集。若 (X) 可分，**Theorem 2.2**：除去一个 (sigma)-porous 例外集，({x:\operatorname{Lip}(T,x)=1\}) 在 (C) 中 residual。

适用判断：这是“某充分条件本身的集合大小”和“结论成立的集合大小”不同的现成示范。不能因可和切向证书很特殊，就直接断言稳定选择稀少；也不能反向推断。

### 2.6 Medjic：多值映射与初值泛性的量词已有直接研究

Emir Medjic, *On Successive Approximations for Compact-Valued Nonexpansive Mappings*；DOI **10.1007/s11228-023-00684-1**；[arXiv:2203.03470v4](https://arxiv.org/pdf/2203.03470)。

令 (C) 为 Banach 空间中的非空、有界、闭、凸集。研究紧值 Hausdorff-nonexpansive (F:C\to\mathcal K(C))，配 (sup_x H(F(x),G(x)))，空间完备。算法为最近点 successive approximation：(x_{k+1}\in P_{F(x_k)}(x_k))。**Corollary 5.4**：每个给定初值对应 residual 算子集，具有唯一的逐步最近点轨道并收敛。**Theorem 5.5**：可分情形有 residual 算子集，其每个算子对应 residual 初值集，轨道逐步唯一。

它不等于“对每个初值同时给统一 Hölder 极限选择”，算法也不是任意多值 resolvent 分支迭代。不得交换这些量词后直接用于 RLEB。

## 3. 独立适用性检查与最小反例

以下是本次审核的直接数学推论，不宣称新定理。

### 3.1 非扩张空间会提前排除用户的坏类

若 (T) 非扩张且 (T^k x\to\Pi_T(x))、(T^k y\to\Pi_T(y))，则

\[
\|\Pi_T(x)-\Pi_T(y)\|
=\lim_k\|T^kx-T^ky\|\le\|x-y\|.
\]

此结论不需要解唯一。故在“收敛的非扩张映射”中，非 Hölder 极限选择类是**空集**。若用户要保留 (gamma<1) 的 RLEB 新构造，比较空间不能直接换成此空间并仍声称研究同一类坏行为。

### 3.2 泛型唯一解会使初值问题退化

若每条轨道都收敛至唯一 fixed point (s_T)，则 (Pi_T\equiv s_T)。这给出对初值的最佳稳定性，却没有回答多解问题。注意映射 (T\mapsto s_T) 的稳定性是另一件事：不能由 (Pi_T) 对初值常值自动推出。

### 3.3 固定多解集后，原泛型定理不能直接限制

令 (S) 至少两点，考虑 (T|_S=I) 的相对类。任何这类 (T) 均不可能严格收缩，因为对不同 (s,t\in S)，

\[
\|Ts-Tt\|=\|s-t\|.
\]

因此 Wang Theorem 2.13 的“严格收缩稠密”核心前提直接失效。ambient 唯一 fixed point 的 residual 集与该类完全不交，也不构成矛盾。最小拓扑类比：(mathbb R^2\setminus(mathbb R\times\{0\})) 在平面开且稠密，但与横轴相交为空。

### 3.4 “固定点集恰为 (S)”并不自动给完备空间

在 ([-1,1]) 上取 (T_n(x)=(1-1/n)x)。每个 (T_n) 的 fixed point 集恰为 ({0})，但一致极限为 (I)，fixed point 集变成整个区间。因此仅写

\[
\{T:\operatorname{Fix}T=S\}
\]

并不能自动得到一致范数下的闭类或完备性。闭性失败也不等于已经证明“不是 Baire”；若要用 Baire 定理，须另证完备可度量性／Baire 性。

### 3.5 无限维中两种拓扑的具体区别

在 (ell_2) 上令 (P_n) 为前 (n) 个坐标的正交投影。则每个 (P_n) 非扩张，且 (P_nx\to x) 对每个固定 (x) 成立，但

\[
\sup_{\|x\|\le1}\|P_nx-x\|=1.
\]

故逐点收敛不是有界集上一致收敛。Wang 预印本在公式 (2) 后有将二者混写的措辞；其实际度量和完备性证明明确使用 bounded-uniform，不能沿用该措辞把定理解释成无限维 pointwise 定理。

## 4. 对下一阶段的建议与尚未解决项

推荐把问题定义为：**在保留同一个非单点解集 (S)、共同轨道区域及 RLEB 预算的一个明确 Baire 算子空间中，极限选择非 Hölder 的算子集是否第一纲、residual、porous，或二者皆非？**

必须分别记清：

1. 算子集中的坏类大小；
2. 一个固定算子的坏初值集大小；
3. “坏”指完整邻域两点 Hölder 失败，还是单一解点处 calmness 失败。

还须证明所选扰动保持完整 resolvent、同一零集、min-residual EB、all-pairs RL 和严格兼容；仅对算法映射做任意 (C^0) 扰动，不能自动宣称得到 RLEB 算子的扰动。

本组没有得到、也没有在以上原文中找到“固定非单点 (S) 的 Hölder RLEB 相对空间中非 Hölder 选择类是 residual／第一纲”的现成定理。**这只是未被本次已核文献覆盖，不是首创证明。**

历史线索仍待直接原页核验：De Blasi–Myjak 1976、1979、1989；Reich–Zaslavski 2000 的 Krasnoselskii–Mann 原文。本报告对其历史地位仅按已读原始研究论文的明确引文记载，不伪造这些早期文献的定理号。已有替代的一手证明是上面完整可读的 Reich–Zaslavski 2005 与 Wang 2013。

额外已核的一手延伸入口：Bargetz–Reich–Thimm, *Generic properties of nonexpansive mappings on unbounded domains*, DOI **10.1016/j.jmaa.2023.127179**, [arXiv:2204.10279](https://arxiv.org/pdf/2204.10279)，Corollary 3.8 在其特定完备的 bounded-uniform 度量下给唯一 fixed point 与 Picard 收敛泛性，并研究更细的广义 porosity；不可把该 porosity 结论随意搬到仅拓扑等价的另一个度量。

## 5. 给总审的短结论

“把坏例升级成坏类大小研究”值得推进，数学工具与先例充分；真正的问题不是有没有 Baire 方法，而是能否找到**既保留多解 RLEB 新现象、又允许可验证扰动、且具 Baire 性的自然相对空间**。现有经典大空间结果既提供技术模板，也提示最容易把问题做空的陷阱。当前应批准空间设计与小规模定理试验，不应预判坏类一定很小或一定很大。
