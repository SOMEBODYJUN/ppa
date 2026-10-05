# 局部值域的条件拓扑证书：去除超临界幂假设

<a id="lr-object"></a>
## 身份、范围与原稿版本

9/25 PDF §8 Theorem 8.1（印刷页 20–22）在其整窗假设之外写了
\(0<\gamma<1,\ q\gamma>1\)。本页是 **C05-v2，新命题版本**：
仅把这个幂条件改成 \(q>0\)，其余对象、每个输出的全称条件、有限样本
collar 和拓扑条件均保留。原稿 C05-v1 仍按原文记录。下述证明是条件定理：
有限样本不能验证整窗的非空、usc、acyclic 和两项输出估计。

设 \(F:\mathbb R^n\rightrightarrows\mathbb R^n\) 的完整零集
\(S=F^{-1}(0)\) 非空闭；固定 \(\lambda,L,\kappa>0\)、
\(0<\gamma<1,\ q>0\)，令
\[
\phi(r)=\tfrac12(r+Lr^\gamma),\qquad c=\kappa\lambda^{-q}.
\]
取两个非空紧有限多面体 \(A,B\subset\mathbb R^n\)，且
\(A\subset\operatorname{int}B\)，及在 \(A\) 某邻域上 upper semicontinuous 的指定对应 \(T\)，
其在该邻域的每个值非空紧且有理 Čech-acyclic；本页该词指非空且所有约化有理 Čech **上同调**为零。对 **所有** \(p\in A,y\in T(p)\)，假设
\[
(p-y)/\lambda\in F(y),\quad
\|p-y\|\le\phi(d(p,S)),\quad
d(y,S)\le c\|p-y\|^q. \tag{1}
\]
从实际 proximal 对组成非空有限样本 \(E\)，每个样本各自核定 (1)，
并按 [C70](finite_sample_collar.md#fsc-envelope) 定义
\(\rho_i,e_i,g_E,u_E\)。另外 **独立核定** 实数 \(u,m>0\) 满足
\[
\sup_Au_E\le u,\quad
\inf_{B\setminus\operatorname{int}A}g_E\ge m,\quad
\phi(u)<d(A,B^c),\quad
\alpha:=c\phi(u)^q<m. \tag{2}
\]
设包含 \(b:A\hookrightarrow B\) 在每一阶诱导
\(b^*:H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 满射，
且 \(\chi(A)\ne0\)。这些是同一组 \(A,B,T,F,E\) 的合取条件。

<a id="lr-theorem"></a>
## C05-v2：条件值域与连续扰动

在上述条件下，对每个连续 \(h:A\to\mathbb R^n\) 且
\(\lambda\|h\|_{\infty,A}<m-\alpha\)，存在 \(x\in\operatorname{int}A\)
满足
\[
h(x)\in F(x),\qquad d(x,S)\le\kappa\|h(x)\|^q.
\]
特别地，
\[
B(0,(m-\alpha)/\lambda)\subset F(\operatorname{int}A).
\]
这里 \(T\) 可以是完整 \(J_{\lambda F}\) 的指定子关系；
结论不声称全部 resolvent 纤维非空或具拓扑性质。

**外部定理的完整导入接口。** [Górniewicz–Rozpłoch-Nowakowska,
Theorem 6.2](../LITERATURE.md#lit-grn-2002) 对 Klee-admissible 拓扑向量空间
\(E\) 中一个开集的回缩 \(X\) 使用 morphism
\(X\xleftarrow{p}\Gamma\xrightarrow{e}X\)：\(p\) 须为 perfect 满射，
各纤维在带紧载体的有理 Čech 同调下 acyclic，\(e\) 连续。
若该 morphism 属于 \(CAC(X)\) 且 Lefschetz 数非零，则存在
\(z\in X\) 与 \(\omega\in p^{-1}(z)\)，使 \(z=e(\omega)\)。
该文的紧 morphism 属于 \(CAC(X)\)，所以本页只需核紧性，
不另假设输出像的每个纤维 acyclic。此处 \(E=\mathbb R^n\)
是 Klee-admissible，紧有限多面体 \(A\) 是欧氏开邻域的回缩；
\(p=\pi:\Gamma\to A\)，\(e=e_h\)。下证逐项核 compact/Vietoris、
自映射和非零 Lefschetz 数。文献卡记录了原文的定义、页码与版本；
这些导入条件不由有限样本本身保证。

**证明。** C70 的独立度量推导仅需 \(q>0\)；
(1)–(2) 给每个 \(p\in A,y\in T(p)\) 的
\([p,y]\subset B,\ y\in\operatorname{int}A\) 和
\(d(y,A^c)\ge\delta:=m-\alpha>0\)。
令 \(\Gamma=\{(p,y)\in A^2:y\in T(p)\}\)；
usc 和紧值使其为紧图。投影 \(\pi:\Gamma\to A\) 满射，
各纤维同胚于 \(T(p)\)。对紧纤维 \(K\)，带紧载体的有理 Čech 同调等于普通 Čech 同调，且
\(\check H_j(K;\mathbb Q)\cong\operatorname{Hom}_{\mathbb Q}(\check H^j(K;\mathbb Q),\mathbb Q)\)
自然成立（Górniewicz 1976，I.§1 Theorem (1.1)，p.8；I.§3，p.12）。故上同调 acyclicity 给所需的同调 acyclicity。
紧 Hausdorff 图到 \(A\) 的连续满射 \(\pi\) 为闭映射且有紧纤维，因而是 GRN2002 Definition 1.1（p.315）的 Vietoris 映射。
对 \((\Gamma,\varnothing)\to(A,\varnothing)\) 应用同文 Theorem 1.2（p.316），得 \(\pi_*\) 在上述有理 Čech 同调的每一阶均为同构。
准确来源、紧载体识别及对偶方向见[导入卡](../audit/VIETORIS_IMPORT.md)；不把任意无限维向量空间与其双对偶识别，也不把紧图同调换成奇异同调。

线段同伦 \((p,y)\mapsto(1-t)p+ty\) 位于 \(B\)，
故 \(b_*\pi_*=b_*e_*\)，其中 \(e(p,y)=y\)。
有限多面体 \(A,B\) 的有理同调逐阶有限维；
\(b^*\) 满射等价于 \(b_*\) 单射，因此 \(e_*=\pi_*\)。
令 \(e_{th}(p,y)=y+t\lambda h(y)\)。余量 \(\delta\) 与严格扰动界
使整个 \(t\in[0,1]\) 同伦留在 \(\operatorname{int}A\)，所以
\((e_h)_*=\pi_*\)。于是紧 span
\(A\leftarrow^\pi\Gamma\to^{e_h}A\) 所诱导的 Lefschetz 数为
\(\chi(A)\ne0\)。[LIT-GRN-2002](../LITERATURE.md#lit-grn-2002)
所核的 rational morphism Lefschetz 定理用于此
Euclidean neighborhood retract 上的紧 Vietoris/CAC morphism，
得到 coincidence \(p=e_h(p,y)=y+\lambda h(y)\)。
由 (1) 得 \(h(y)\in F(y)\)、
\(d(y,S)\le c\lambda^q\|h(y)\|^q=\kappa\|h(y)\|^q\)；
取 \(x=y\in\operatorname{int}A\)。常值 \(h\) 给值域球。
每一步仅用 \(q>0\)，未用 \(q\gamma>1\)。证毕。

<a id="lr-feasible"></a>
## 非空的次临界实例与审查边界

去掉 \(q\gamma>1\) 并未使 (2) 变成空条件。取 \(n=1\)，
\(\lambda=L=1,\gamma=1/2,q=1,\kappa=c=10^{-4}\)，
\(F(x)=10^4x,\ S=\{0\},\ T(p)=\{p/10001\}\)，
\(A=[-1/100,1/100],B=[-7/100,7/100]\)。取 1401 个样本
\[
(p_k,y_k)=(k/10000,k/(10000\cdot10001)),\quad -700\le k\le700.
\]
全部 \(p\in A\) 及样本有 \(|p-y|=(10000/10001)|p|
\le|p|\le\phi(|p|)\)（\(|p|\le7/100<1\)），且
\(|y|=c|p-y|\)。零样本与三角不等式给 \(u_E(z)=|z|\)；
取 \(u=1/100\)。在 shell \(B\setminus\operatorname{int}A\)
的每个点 \(z\) 可找到格点 \(|z-p_k|\le1/20000\) 且
\(|p_k|\ge1/100\)。由于
\(\phi(1/5000)<1/125<(10000/10001)/100\)，
相应 \(\rho_k>1/5000\)，所以
\(g_E(z)>3/20000\)；可取 \(m=1/10000\)。
最后 \(\phi(u)=11/200<3/50=d(A,B^c)\)，
\(\alpha=11/2000000<m\)。
\(T\) 连续单值，区间 \(A,B\) 可缩，\(b^*\) 同构，
\(\chi(A)=1\)；但 \(q\gamma=1/2\)。

本页独立重算 C70 以后拓扑链的条件应用，并经反例攻击幂次门。
状态为 derived-checked **conditional theorem**：原生模型是否能在
给定问题中产生整个窗上的 (1)–(2) 与 acyclic \(T\) 仍开放；
外部新颖性未审。若未来发现所导入的 Čech homology 约定或
CAC morphism 适用条件有实质异议，应暂停此状态而保留
C70 度量部分和上面的精确可行实例。
