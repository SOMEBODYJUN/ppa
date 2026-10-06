# 有限维闭图空间中固定输入的一步可解薄性

<a id="aw-object"></a>
## C179-v1 / AW-FIXED-INPUT：对象与结论

固定 \(E=\mathbb R^d\)、\(d\ge1\)，令 \(Z=E\times E\) 配 Euclidean 乘积范数。\(\mathrm{CL}_*(Z)\) 指全部**非空闭子集**，不预设单值、满定义域、单调性或算法收敛。对 \(A\in\mathrm{CL}_*(Z)\)，记 \(d_A(z)=\inf_{a\in A}\|z-a\|\)。采用距离函数在每个有界集上一致收敛的 Attouch–Wets（AW）拓扑，其一个度量为
\[
 d_{\rm AW}(A,B)=\sum_{j=1}^{\infty}2^{-j}
 \min\left\{1,\sup_{\|z\|\le j}|d_A(z)-d_B(z)|\right\}. \tag{AW1}
\]
所有距离函数有限；若 AW1 为零，二者距离函数相同，取零集得 \(A=B\)。AW1 收敛当且仅当距离函数在每个球上一致收敛：逐项受总和控制，反向先取有限段再控制尾和。

先把图坐标记作输入／输出 \((p,u)\)。固定任意 \(p_0\in E\)，定义
\[
 \mathcal D_{p_0}=\{\Gamma\in\mathrm{CL}_*(Z):
       \exists u\in E\ (p_0,u)\in\Gamma\}. \tag{AW2}
\]
则 \(\mathcal D_{p_0}\) 是 \(F_\sigma\) 第一纲集，且其补集稠密。更精确地，它是以下闭无处稠密集的可数并：
\[
 C_m=\{p_0\}\times\overline B_E(0,m),\qquad
 H_m=\{\Gamma:\Gamma\cap C_m\ne\varnothing\},\qquad m\ge1. \tag{AW3}
\]

若另固定非空闭真子集 \(S\subsetneq E\)，令
\[
 \Delta_S=\{(s,s):s\in S\},\quad
 \Delta_E=\{(s,s):s\in E\},\quad
 \mathfrak G_S=\{\Gamma\in\mathrm{CL}_*(Z):
                  \Gamma\cap\Delta_E=\Delta_S\}. \tag{AW4}
\]
该空间取 **AW 的相对拓扑**。对每个 \(p_0\notin S\)，\(\mathcal D_{p_0}\cap\mathfrak G_S\) 同样是相对 \(F_\sigma\) 第一纲集，且补集相对稠密。\(\mathfrak G_S\) 非空，因为 \(\Delta_S\) 本身属于它；这里未把相对第一纲擅自提升到某个更小算法子类。

<a id="aw-net"></a>
## 有限网的定量逼近

以下引理明确源证明中“足够大的球”的选择。固定 \(A\in\mathrm{CL}_*(Z)\)、\(a_0\in A\)、整数 \(R\ge1\) 和 \(\delta>0\)，令
\[
 M=2R+\|a_0\|+1.
\]
有限维非空闭集对每个 \(z\) 有最近点：一条距离极小化列可限制在有界球内，取收敛子列后由闭性得到极小值。对 \(\|z\|\le R\)，任一最近点 \(a_z\) 满足
\[
 \|a_z\|\le\|z\|+d_A(z)
 \le R+\|z-a_0\|\le2R+\|a_0\|<M. \tag{AW5}
\]
紧的非空集 \(A\cap\overline B_Z(0,M)\) 因此有非空有限 \(\delta\)-网 \(F\)，网点选在该集合内。于是
\[
 0\le d_F(z)-d_A(z)\le\delta\qquad(\|z\|\le R). \tag{AW6}
\]
下界来自 \(F\subset A\)，上界来自距 \(a_z\) 不超过 \(\delta\) 的网点。

若要保留任意非空闭锚集 \(A_0\subset A\)，同一估计对 \(A_0\cup F\) 成立。对每个 \(f\in F\) 选 \(f'\) 满足 \(\|f'-f\|<\delta\)，记有限非空集 \(F'=\{f':f\in F\}\)。逐点配对给
\[
 |d_{F'}(z)-d_F(z)|\le\delta
 \quad\text{对全部 }z\in Z.
\]
带锚时用 \(d_{A_0\cup F}=\min\{d_{A_0},d_F\}\)，同样得到
\[
 \sup_{\|z\|\le R}|d_{A_0\cup F'}(z)-d_A(z)|\le2\delta,
 \qquad d_{\rm AW}(A_0\cup F',A)\le2\delta+2^{-R}. \tag{AW7}
\]
无锚时把 \(A_0\cup F'\) 换成 \(F'\)，仍成立。取 \(R\) 足够大、再取 \(\delta\) 足够小，便得到任意给定 AW 邻域内的逼近。有限集非空且闭；带锚并集也是非空闭集。证明既未截掉锚集的远端，也未假定原图有界。

<a id="aw-proof"></a>
## 闭性和无处稠密性

**紧切片的击中类闭。** 固定 \(m\)，若 \(\Gamma_n\to\Gamma\) AW 且 \(z_n\in\Gamma_n\cap C_m\)，\(C_m\) 紧，故可取子列 \(z_n\to z\in C_m\)。在含这些点的共同球上，
\[
 d_\Gamma(z)\le\|z-z_n\|+
 \sup_{w\in C_m}|d_\Gamma(w)-d_{\Gamma_n}(w)|\longrightarrow0.
\]
\(\Gamma\) 闭，所以 \(z\in\Gamma\cap C_m\)。AW 可度量，因此序列闭性即闭性。这一步用的是**有界输出切片**；击中整个无界纤维的类未因此被证明闭。

**全部闭图中的稠密补集。** 给定任意 \(A\) 及其 AW 邻域，用 AW7 的无锚版本。有限个网点的输入坐标可以各作任意小移动，使全部输入均不等于 \(p_0\)。所得 \(F'\) 仍在给定邻域，并且完全避开 \(\{p_0\}\times E\)，故它同时不属于任何 \(H_m\)。因此 \(\mathcal D_{p_0}\) 的补集稠密；每个闭集 \(H_m\) 内部为空，即无处稠密。AW2 显然等于 \(\bigcup_{m\ge1}H_m\)，得所称 \(F_\sigma\) 第一纲。

**固定精确 \(S\) 的相对版本。** 对 \(A\in\mathfrak G_S\)，用锚集 \(A_0=\Delta_S\) 的 AW7。对每个网点 \((p,u)\)，先把 \(p\) 任意小移动为 \(p'\ne p_0\)，再把 \(u\) 任意小移动为 \(u'\ne p'\)。\(d\ge1\) 保证两个选择均可作，总移动量可取小于 \(\delta\)。于是有限网点避开输入纤维及整条对角线。由于 \(p_0\notin S\)，锚集也避开该输入纤维。因此
\[
 A'=\Delta_S\cup F'\in\mathfrak G_S,
 \qquad A'\cap(\{p_0\}\times E)=\varnothing.
\]
它可以任意 AW 接近 \(A\)。每个 \(H_m\cap\mathfrak G_S\) 相对闭且内部空；可数并即相对结论。证毕。

<a id="aw-shear"></a>
## 固定步长的完整原算子图版本

固定 \(\lambda>0\)。对任意完整关系 \(F:E\rightrightarrows E\)，约定
\[
 J_{\lambda F}(p)=\{u:(u,(p-u)/\lambda)\in\operatorname{gph}F\}.
\]
线性双射
\[
 L_\lambda(u,v)=(u+\lambda v,u),\qquad
 L_\lambda^{-1}(p,u)=(u,(p-u)/\lambda) \tag{AW8}
\]
把完整图 \(\operatorname{gph}F\) 送到完整 resolvent 关系图；空纤维、多值及远端图点全部保留。它把 \(S\times\{0\}\) 送到 \(\Delta_S\)，所以精确零集 \(F^{-1}(0)=S\) 等价于 AW4 的精确固定集条件。

**线性坐标变换在 AW 下诱导同胚。** 对任意可逆线性 \(L:Z\to Z\)，先证明 \(A_n\to A\) AW 推出 \(LA_n\to LA\) AW。选 \(a\in A\)；由 \(d_{A_n}(a)\to0\) 可选 \(a_n\in A_n\) 使 \(a_n\to a\)。对任意固定 \(R\)，点 \(La_n\) 给出 \(d(y,LA_n)\) 在 \(\|y\|\le R\) 上的统一上界，\(La\) 同样控制 \(d(y,LA)\)。因此这些球中每个 \(y\) 到 \(LA_n\) 或 \(LA\) 的最近点，及其 \(L^{-1}\) 原像，全都落在一个共同有限半径 \(M\) 的球中（丢去有限个 \(n\) 不影响极限）。

令 \(\varepsilon_n=\sup_{\|z\|\le M}|d_{A_n}(z)-d_A(z)|\to0\)。若原像最近点在 \(A\)，它到 \(A_n\) 的距离至多 \(\varepsilon_n\)；若在 \(A_n\)，它到 \(A\) 的距离也至多 \(\varepsilon_n\)。分别把这种近点送入 \(L\)，得到两个方向的距离估计，故
\[
 \sup_{\|y\|\le R}|d(y,LA_n)-d(y,LA)|
 \le\|L\|\varepsilon_n\longrightarrow0.
\]
逆向对 \(L^{-1}\) 应用同一证明。线性像为非空闭集，故这是所称 hyperspace 同胚，也限制为精确零集／固定集空间间的相对同胚。

因此，对所有非空闭原算子图，固定 \(\lambda,p_0\) 的可解类
\[
 \mathcal W_{\lambda,p_0}=\{F:J_{\lambda F}(p_0)\ne\varnothing\}
\]
是 \(F_\sigma\) 第一纲。若限制到非空闭图且精确零集为给定非空闭真子集 \(S\) 的相对空间，并取 \(p_0\notin S\)，同样成立。其原坐标的具体紧切片为
\[
 C_{\lambda,p_0,m}
 =\{(u,(p_0-u)/\lambda):\|u\|\le m\}. \tag{AW9}
\]
它们穷尽线性仿射切片 \(u+\lambda v=p_0\)。所以这里没有把“固定输入的 proximal 解存在”误换成“某个原输出纤维非空”。

<a id="aw-boundary"></a>
## 可调用后果及不得删除的量词

任何一类关系，只要其定义要求**同一个固定步长** \(\lambda\) 下、在包含指定点 \(p_0\) 的共同初值域上完整 PPA 一步可解，它就包含在 \(\mathcal W_{\lambda,p_0}\) 中，从而在上述宽 AW 空间中第一纲。这条共同障碍不使用 RLEB、LT 或极大单调的特有条件，不能据此比较三者优势。

- 固定精确 \(S\) 的版本必须取 \(p_0\notin S\)。若 \(p_0\in S\)，锚点本身保证可解，所讨论集合就是整个相对空间。
- 对一个**预先固定的可数**步长集，可解类的并仍第一纲；对“存在任意实数步长 \(\lambda>0\)”不能用不可数并推出此结论。要求所有正步长可解当然蕴含任取一个预定步长可解，但不等于存在步长的量词。
- 若将母空间再限制成固定 \(\lambda,p_0\) 已经良定的算法类，AW2 的相对集合变成整个该类。本页的第一纲结论不能直接转移为该算法子类内的比较。
- 有限维在紧切片、最近点、有限网中都实际使用。本页未证明无限维 AW 版本，也未证明任何 \(\sigma\)-porosity、统一孔洞常数、全时间拓扑或 orbit-small 理想结论。
- 本页没有引入原报告的 \(\mathcal X_D\)、\(d_{\rm dyn}\)、固定 \(E\) 修补或 Poisson 纤维，不能替代它们缺失的定义和完整证明。

<a id="aw-source"></a>
## 恢复来源与证据身份

C179-v1 的证据为 `derived-checked`：以上命题全部在明确有限维非空闭图对象上直接证明，不作全球新颖性声明。定性源证明位于 F11 的 [09_value_audit.md](../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/02_NEUTRAL_PPA_SYSTEM/ppa_system_team/09_value_audit.md) LF117–155，解释和审查报告位于 LF157–161；源文件20049字节、285物理LF行，SHA-256 `f1c791bbb4a14c1bb12982e465feb4629922c3ebfb6e31317213362b3bb45ab5`。本页补足量化有限网、闭性／非空性、原图线性切片和 AW 同胚证明；源中“独立复核”是历史行为报告，不由本次数学重证追认。

全源断言的处置见 [VALUE_AUDIT_UNITS.tsv](../audit/VALUE_AUDIT_UNITS.tsv)，恢复范围与 N05/N08/N10 未闭门见 [MOTHER_SPACE_PROOF_RECOVERY.md](../audit/MOTHER_SPACE_PROOF_RECOVERY.md)。C179 仅闭合准确匹配的固定步长 AW 原子；9/21 C07 的整体规模、共同塌缩及孔隙报告不因此升格。
