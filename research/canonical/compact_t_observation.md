# 固定紧源的实际尾与反射模观测

<a id="ct-object"></a>
## C06 的精确对象

固定非空紧 \(K\subset\mathbb R^d\)、非空闭 \(S\subset K\)。在 \(C(K,K)\) 中取

\[
X=\{T:T|_S=I_K|_S,\quad T^n\to\Pi_T\text{ 于 }K\text{ 一致},\quad\Pi_T(K)\subset S\},
\qquad d_{\mathrm{all}}^K(T,U)=\sup_{n\ge0}\|T^n-U^n\|_K.
\tag{CT1}
\]

\(d_{\mathrm{all}}^K\) 有限，且 \(n=1\) 项使它是度量；若 \(X=\varnothing\)，下述 proper 断言仍可作空函数理解，但“非空纤维”不产生任何结论。事实上 \(X\ne\varnothing\) 当且仅当 \(S\) 是 \(K\) 的连续回缩像：若 \(T\in X\)，则 \(\Pi_T:K\to S\) 是回缩；反过来取任一回缩为 \(T\)，其迭代从第一步起恒定。这里观测的是**整个紧源上的单值动力系统**，不是原多值关系 \(F\) 的局部图块。

定义 \(R_T=2T-I_K\)（\(R_T:K\to\mathbb R^d\)，不要求值仍在 \(K\)）及对所有整数 \(n,j\ge0\)

\[
w_n(T)=\max\left\{\sup_{k,\ell\ge n}\|T^k-T^\ell\|_K,
\quad\sup_{k\ge n}\sup_{x\in K}d(T^kx,S)\right\},\quad
m_j(T)=\sup_{\substack{x,y\in K\\\|x-y\|\le2^{-j}}}\|R_Tx-R_Ty\|.
\tag{CT2}
\]

第一项是所有**尾部两迭代差**，不是相邻位移。\(\Phi:X\to c_0\times c_0\)，\(\Phi(T)=(w(T),m(T))\)，目标取上确界范数的乘积。每个 \(T\in X\) 迭代一致 Cauchy，\(R_T\) 在紧域上一致连续，故两列均非负、非增且趋零。

<a id="ct-proper"></a>
## 连续、proper、闭像与纤维

**结论。** \((X,d_{\mathrm{all}}^K)\) 是 Polish，\(\Phi\) 连续且紧集逆像紧。像 \(\Phi(X)\) 在 \(c_0\times c_0\) 中闭，因而是 Polish；\(\Phi:X\to\Phi(X)\) 是闭的 perfect/quotient 映射，每个非空纤维紧且 Baire。这里 proper 指**紧集逆像紧**。这些结论都不说 \(\Phi\) 保纲或开，也不恢复完整原关系的域外图值。

**Polish 门。** \(B=C(K,K)\) 取一致度量，是可分完备空间。令 \(c(B)\) 为所有在 \(B\) 中收敛的序列，取序列上确界度量；它也可分完备：一个一致 Cauchy 序列的各坐标极限仍一致地有尾极限，且用可数稠密集的有限前缀和最终常尾序列可逼近任意元素。\(T\mapsto(T^n)_{n\ge0}\) 是 \(X\) 到 \(c(B)\) 的等距嵌入。其像由 \(f_0=I_K\)、\(f_{n+1}=f_1\circ f_n\)、\(f_1|_S=I_K|_S\) 及序列极限 \(f_\infty(K)\subset S\) 刻画；有限复合在一致拓扑连续，极限映射 \(c(B)\to B\) 连续，\(S\) 闭，因此这些约束均闭。\(X\) 因而 Polish。

**连续门。** 对各 \(k,\ell\)，\(\|T^k-T^\ell\|_K\) 在 \(T,U\) 间变化至多 \(2d_{\mathrm{all}}^K(T,U)\)，尾部到 \(S\) 的距离变化至多 \(d_{\mathrm{all}}^K(T,U)\)；取上确界及最大值给 \(\|w(T)-w(U)\|_\infty\le2d_{\mathrm{all}}^K(T,U)\)。又 \(R_T-R_U=2(T-U)\)，所以 \(\|m(T)-m(U)\|_\infty\le4d_{\mathrm{all}}^K(T,U)\)。

**紧预算门。** 任取非负非增且趋零的列 \(e,h\)。在 \(C(K,K)\) 内令 \(D_{e,h}\) 是 \(T|_S=I\)、全部有限 \(k,\ell\ge n\) 的 \(\|T^k-T^\ell\|_K\le e_n\)、全部 \(k\ge n\) 的 \(\sup_xd(T^kx,S)\le e_n\) 和各 \(m_j(T)\le h_j\) 的交。约束在一致拓扑下闭。反射模给共同等度连续性：若 \(\|x-y\|\le2^{-j}\)，
\(\|Tx-Ty\|\le(h_j+2^{-j})/2\)。Arzelà–Ascoli 使 \(D_{e,h}\) 在单步一致拓扑紧；尾部约束又强迫每个极限映射的迭代一致 Cauchy、其极限在闭 \(S\)，故 \(D_{e,h}\subset X\)。若 \(T_i\to T\) 单步一致，有限次迭代亦一致，且对 \(n\ge N\)
\[
\|T_i^n-T^n\|_K\le2e_N+\|T_i^N-T^N\|_K.
\tag{CT3}
\]
由此精确地有
\[
d_{\mathrm{all}}^K(T_i,T)\le\max\left\{\max_{0\le n<N}\|T_i^n-T^n\|_K,\;2e_N+\|T_i^N-T^N\|_K\right\}.
\tag{CT4}
\]
给定误差阈值，先选 \(N\) 使 \(2e_N\) 足够小；有限次迭代的一致收敛同时控制 \(0\le n<N\) 的全部前缀和第 \(N\) 项。再令 \(i\) 足够大，得 \(d_{\mathrm{all}}^K(T_i,T)\to0\)。因此 \(D_{e,h}\) 在**全时间**度量亦紧。

若 \(Q\subset c_0\times c_0\) 紧，有限 \(\varepsilon\)-网及每个网点的零尾给 \(e_n:=\sup_{(a,b)\in Q}\sup_{k\ge n}|a_k|\to0\) 与 \(h_j:=\sup_{(a,b)\in Q}\sup_{i\ge j}|b_i|\to0\)。于是 \(\Phi^{-1}(Q)\subset D_{e,h}\)，又因 \(Q\) 闭和 \(\Phi\) 连续，它在该紧层中闭，故紧。**只给坐标有界或逐坐标紧不够**：\(a^{(N)}_j=1_{j\le N}\) 各在 \(c_0\)，但没有共同零尾。

若 \(y_i=\Phi(T_i)\to y\) 且 \(T_i\) 落在 \(X\) 的某个闭集 \(A\)，则 \(\{y\}\cup\{y_i\}\) 紧，其原像紧；取收敛子列并用连续性得到 \(y\in\Phi(A)\)。所以 \(\Phi\) 闭、像闭；每个单点纤维紧，闭满射到像即 quotient。非空紧纤维是 Baire。证毕。

## 可调用边界

上述 \(d_{\mathrm{all}}^K\) 记录**所有**时间的整个 \(K\) 输入；把 \(T\) 只在局部窗观测、把 \(c_0\) 的紧集弱化为坐标有界，或把这个 \(T\)-only 图卡称为完整 \(F\) 的类，都改变了前提。尤其 proper 不推出 category-preserving，见[算子空间反例](../operator_space.md#cat-gap)。原来源的审计与本页重构为两层证据；本页内部证明不判定该观测在最终参数中立母空间是否非退化或新颖。
