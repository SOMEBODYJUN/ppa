# 有限 proximal 观测的距离包络与内域余量

本页只重建 9/25 稿 §8 的**度量部分**。它可独立于 Lefschetz 定理调用；所得包络和内域余量也不能建立整窗对应的非空性、上半连续性或有理 acyclicity。原稿为 [S25 §8，印刷页 20–21，(8.1)–(8.4)、(8.7)](../../history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)。

<a id="fsc-object"></a>
## 对象与量词

令 \(S\subset\mathbb R^n\) 非空闭，\(F^{-1}(0)=S\)，\(\lambda,L,c>0\)，\(0<\gamma<1\)，\(q>0\)，\(\phi(r)=(r+Lr^\gamma)/2\)。指定关系 \(T\) 的每个声明值须满足
\[
y\in T(p)\ \Longrightarrow\ (p-y)/\lambda\in F(y),\quad
\|p-y\|\le\phi(d(p,S)),\quad d(y,S)\le c\|p-y\|^q.
\tag{1}
\]
以下有限样本 \(E=\{(p_i,y_i)\}_{i=1}^N\) 非空且每个样本的 (1) 已由独立方式核定。后面的内域结论另要求 (1) 对**整个** \(p\in A,y\in T(p)\) 成立；样本核定本身不提供这个全称量词。证明包络无需 \(q\gamma>1\)、RL 或拓扑条件。

<a id="fsc-envelope"></a>
## C70-v1a：全空间双侧距离包络

记 \(\rho_i=\phi^{-1}(\|p_i-y_i\|)\)、\(e_i=c\|p_i-y_i\|^q\)，并定义
\[
g_E(z)=\max_i\{\rho_i-\|z-p_i\|\},\qquad
u_E(z)=\min_i\{\|z-y_i\|+e_i\}.
\tag{2}
\]
则对**每个** \(z\in\mathbb R^n\)，
\[
g_E(z)\le d(z,S)\le u_E(z).
\tag{3}
\]
\(g_E\) 可以为负；它只给下界，不是距离。两函数都是 1-Lipschitz。

**重算证明。** \(\phi\) 在 \([0,\infty)\) 严格增且满射自身，故由样本步界得 \(\rho_i\le d(p_i,S)\)。距离函数的 1-Lipschitz 性给 \(d(z,S)\ge d(p_i,S)-\|z-p_i\|\ge\rho_i-\|z-p_i\|\)。再由样本输出界得 \(d(y_i,S)\le e_i\)，故 \(d(z,S)\le\|z-y_i\|+e_i\)。分别取最大和最小即 (3)；有限个共同 1-Lipschitz 函数的最大/最小仍为 1-Lipschitz。没有把选中输出的残差当作完整 \(r_F\)。

有限覆盖可以保守认证极值：若闭集 \(K\) 被半径至多 \(\varepsilon_j\) 的中心球 \(B(z_j,\varepsilon_j)\) 覆盖，则所有 \(z\in K\) 满足
\(\sup_K u_E\le\max_j(u_E(z_j)+\varepsilon_j)\) 和
\(\inf_K g_E\ge\min_j(g_E(z_j)-\varepsilon_j)\)。实际浮点计算还须把范数和函数求值误差向外取整；未经这些控制的数值网格不是认证。

<a id="fsc-collar"></a>
## C70-v1b：由包络到整窗输出余量

令 \(A\subset\operatorname{int}B\) 为非空紧集，\(B\subset\mathbb R^n\) 为紧集，\(T(p)\) 对每个 \(p\in A\) 非空且 (1) 对**所有**这些输出成立。假设已认证
\[
\sup_Au_E\le u,\quad
\inf_{B\setminus\operatorname{int}A}g_E\ge m>0,\quad
\phi(u)<d(A,B^c),\quad
\alpha:=c\phi(u)^q<m.
\tag{4}
\]
那么每个 \(p\in A,y\in T(p)\) 满足
\[
[p,y]\subset B,\qquad y\in\operatorname{int}A,\qquad
d(y,A^c)\ge m-\alpha.
\tag{5}
\]
从而对任意连续 \(h:A\to\mathbb R^n\)，只要 \(\lambda\|h\|_{\infty,A}<m-\alpha\)，所有 \(y\in T(A)\) 及 \(0\le t\le1\) 都有 \(y+t\lambda h(y)\in\operatorname{int}A\)。这个结论只说变形**有定义并留域**，不说有某个 \(p=y+\lambda h(y)\)；后者还需另行证明 coincidence。

**重算证明。** 对 \(p\in A\)，(3) 与 (4) 给 \(d(p,S)\le u\)；(1) 给 \(\|p-y\|\le\phi(u)<d(A,B^c)\)，故线段在 \(B\) 内，并有 \(d(y,S)\le\alpha<m\)。若 \(y\notin\operatorname{int}A\)，则 \(y\in B\setminus\operatorname{int}A\)，与 (3)、(4) 的 \(d(y,S)\ge m\) 矛盾。对每个 \(z\in\partial A\subset B\setminus\operatorname{int}A\)，1-Lipschitz 性给 \(\|y-z\|\ge d(z,S)-d(y,S)\ge m-\alpha\)。从 \(y\in\operatorname{int}A\) 到任意 \(z\in A^c\) 的线段先触及 \(\partial A\)，所以同一下界适用于 \(d(y,A^c)\)。严格扰动界由开球余量推出。

<a id="fsc-boundary"></a>
## 证据、边界与后续接口

- **证据层**：上述两段是从 S25 的公式独立重算的分析命题 `derived-checked`；其数学身份合记 C70-v1，(3) 可单独调用，(5) 还需 (4) 和整窗 (1)。有限网格只是带外向误差控制的可认证计算接口，本文没有执行某个数据集。
- **不蕴含**：有限样本包络 C70-v1a 不能认证 \(T\) 在 \(A\) 的整窗非空、usc、紧图或 acyclic；C70-v1b 的整窗非空已作为**额外前提**给定，结论仍不推出其余拓扑条件或任何原关系值域球。后者的[原稿 C05-v1 候选](../holder_structure.md#h07) 与[条件拓扑链 C05-v2](local_range_without_supercriticality.md#lr-theorem) 还分别保留其明确的多面体、上同调、Euler、Vietoris–Begle 与 Lefschetz 合取条件。C70 的结论不要求 \(T=J_{\lambda F}\) 的完整纤维。
- **审查范围**：逐式核了 (8.3)、(8.4) 到 (8.7) 的度量论证及页 21 排版；C05-v2 的**条件**拓扑步骤已在其独立正文重算，但这里并未认证原生整窗模型或新颖性，不能据此升级 C05-v1。
