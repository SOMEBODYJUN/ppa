# 矩形一步回缩的正 Hölder 并类自第一纲

<a id="rht-object"></a>
## C186-v1 / RELATIVE-HOLDER-THINNESS：准确对象

- **Status**：`derived-checked`。证据为 (RH1)–(RH11) 的独立直接推导：逐项核验值域、底边、精确固定集、同一实际尾、有限正 Hölder 常数和反三角越界估计。空白接收另逐式复算并修正了 (RH7) 的标量字母；历史 PASS 或审查者同意不是证明依据。
- **范围**：只取欧氏平面、固定矩形 \(K=[-1,1]\times[0,1]\) 及底边 \(S=[-1,1]\times\{0\}\)，不量化任意闭 \(S\)。
- **依赖**：一致极限、初等 Hölder 估计及 Baire 完备度量空间定理；完整源图代数复用 [C180 的固定步长图卡](uniform_holder_thinness.md#uht-source-card)。不调用 C180 的母空间范畴结论。

令
\[
\mathscr M=\{T\in C(K,S):T(s)=s\quad(s\in S)\},\qquad
 d_\infty(T,U)=\sup_{z\in K}\|T(z)-U(z)\|_2,
\tag{RH1}
\]
并定义
\[
\mathscr H_{\alpha,M}=\{T\in\mathscr M:
\|T(z)-T(w)\|_2\le M\|z-w\|_2^\alpha\quad(z,w\in K)\},
\quad
\mathscr H_+=\bigcup_{\alpha>0,\,0\le M<\infty}\mathscr H_{\alpha,M}.
\tag{RH2}
\]
所有相对类别都注明环境。结论是：每个 \(\mathscr H_{\alpha,M}\) 在 **\(\mathscr H_+\) 的相对一致拓扑**中闭且无处稠密；\(\mathscr H_+\) 是非空的自第一纲空间。于是每个 \(A\subseteq\mathscr H_+\) 都在环境 \(\mathscr H_+\) 中第一纲。这不表示每个 \(A\) 在自身拓扑中第一纲。

<a id="rht-retractions"></a>
## 回缩、精确固定集、共同尾与极限映射

任意 \(T\in\mathscr M\) 都可唯一写成 \(T(x,y)=(f(x,y),0)\)，其中 \(f:K\to[-1,1]\) 连续且 \(f(x,0)=x\)。因为值域位于 \(S\) 且固定 \(S\)，
\[
\operatorname{Fix}T=S,\qquad T^n=T\quad(n\ge1),\qquad
\Pi_T=\lim_{n\to\infty}T^n=T.
\tag{RH3}
\]
这里自映射、精确固定集和回缩全部同时成立；本页扰动必须保持全部三项。

若在全部 \(T\in C(K,K)\) 中同时要求 \(T|_S=I\)，并取 \(e_0=\operatorname{diam}K=\sqrt5\)、\(e_n=0\ (n\ge1)\)，以
\[
\|T^m-T^n\|_\infty\le e_n\quad(m\ge n\ge0),\qquad
\sup_{z\in K}d(T^n z,S)\le e_n\quad(n\ge0)
\tag{RH4}
\]
定义尾层，则此尾层恰为 \(\mathscr M\)。正向由 \(n=1\) 距离条件得 \(T(K)\subseteq S\)；逆向用 (RH3)，而 \(n=0\) 的两式由直径上界成立。因此这是一个固定预算的真实一步尾层，不是给每次扰动另选尾预算。

在该层，\(d_{\rm all}(T,U)=\sup_{n\ge0}\|T^n-U^n\|_\infty=d_\infty(T,U)\)，因为零次迭代都是恒等，其余均为自身。因此本页结论也适用于这个**相同一步层**的全时间度量和其极限映射集合。它不涉及一般多步映射 \(T\mapsto\Pi_T\) 的像、连续性或范畴转移。

\(\mathscr M\) 在 \(C(K,\mathbb R^2)\) 中闭：一致极限仍取值于闭集 \(S\) 并固定 \(S\)。故一致距离完备；它非空，因为 \(P(x,y)=(x,0)\) 属于它；它亦为凸集，因为 \(S\) 凸且两个回缩在底边都等于恒等。Baire 定理因此适用于 \(\mathscr M\)。这一事实不授予子空间 \(\mathscr H_+\) Baire 性。

<a id="rht-countable"></a>
## 闭块和可数耗尽

每个 \(\mathscr H_{\alpha,M}\) 在 \(\mathscr M\) 中闭，因为对每个固定 \(z,w\) 可在一致极限中传递 (RH2) 的不等式。因此它在 \(\mathscr H_+\) 中也闭。底边恒等排除 \(\alpha>1\)：对底边上距离为 \(t>0\) 的两点，不等式要求 \(1\le Mt^{\alpha-1}\)，当 \(t\downarrow0\) 矛盾。因此这些块为空，不产生例外。

记 \(D=\sqrt5\)。若 \(0<\alpha\le1\) 且 \(T\in\mathscr H_{\alpha,M}\)，选整数 \(m\ge1\) 使 \(1/m\le\alpha\)，再选整数 \(n\ge\max\{1,MD^{\alpha-1/m}\}\)。对 \(0<t\le D\)，\(t^\alpha\le D^{\alpha-1/m}t^{1/m}\)。所以
\[
\mathscr H_+=\bigcup_{m,n\ge1}\mathscr H_{1/m,n}.
\tag{RH5}
\]
可数化保留直径系数，未把不可数并直接当成第一纲。

<a id="rht-perturbation"></a>
## 保持正 Hölder 资格的一步回缩扰动

固定 \(0<\alpha\le1\)、\(M<\infty\)、\(T\in\mathscr H_{\alpha,M}\) 和任意 \(\varepsilon>0\)。只须从块内点构造任意接近的块外点来排除相对内点，无须先逼近任意连续映射。

令 \(a=(0,1/2)\)、\(r=1/8\)。闭球 \(\overline B(a,3r)\) 在 \(\operatorname{int}K\) 内且不接触底边。令 Lipschitz cutoff
\[
\theta(z)=\max\{0,\min\{1,(3r-\|z-a\|_2)/r\}\},\qquad
\chi(z)=\max\{0,\min\{1,(2r-\|z-a\|_2)/r\}\}.
\tag{RH6}
\]
于是 \(\theta=1\) 于 \(\overline B(a,2r)\)，\(\chi=1\) 于 \(\overline B(a,r)\)，且 \(\chi\ne0\) 只可能发生在 \(\theta=1\) 的区域。

写 \(T=(f,0)\)，取
\[
0<\mu<\min\{1/2,\varepsilon/2\},\qquad
0<\beta<\alpha,\qquad
0<c(2r)^\beta<\min\{\mu/2,\varepsilon/2\}.
\]
定义
\[
g(z)=(1-\mu\theta(z))f(z),\qquad
u(z)=g(z)+c\chi(z)\|z-a\|_2^\beta,\qquad
U(z)=(u(z),0).
\tag{RH7}
\]
逐项验证如下。

1. **值域与底边。** \(|g(z)|\le1\)。若尖点项非零，则 \(\theta(z)=1\)，故 \(|g(z)|\le1-\mu\)，而尖点振幅小于 \(\mu/2\)，所以 \(|u(z)|<1\)。其余点 \(u=g\in[-1,1]\)。两 cutoff 在底边均为零，故 \(U(x,0)=(x,0)\)。因此 \(U\in\mathscr M\)，(RH3)–(RH4) 的精确固定集、同一尾和极限身份均保留。
2. **一致距离。** 由 \(|f|\le1\)，
\[
d_\infty(U,T)\le\mu+c(2r)^\beta<\varepsilon.
\tag{RH8}
\]
3. **仍属于 \(\mathscr H_+\)。** 函数 \(f\) 为 \(\beta\)-Hölder，常数不超过 \(MD^{\alpha-\beta}\)。若 \(L_\theta,L_\chi\) 为两个 cutoff 的有限 Lipschitz 常数，\(t=\|z-w\|_2\le D\)，则
\[
|g(z)-g(w)|\le MD^{\alpha-\beta}t^\beta+\mu L_\theta t
\le\bigl(MD^{\alpha-\beta}+\mu L_\theta D^{1-\beta}\bigr)t^\beta.
\]
又由 \(0<\beta<1\)、\(|u^\beta-v^\beta|\le|u-v|^\beta\) 及距离函数的 1-Lipschitz 性，\(q(z)=\|z-a\|_2^\beta\) 为 1-\(\beta\)-Hölder 且有界于 \(D^\beta\)。于是
\[
|\chi(z)q(z)-\chi(w)q(w)|
\le t^\beta+D^\beta L_\chi t
\le(1+DL_\chi)t^\beta.
\]
这些估计给 \(U\) 一个有限全域 \(\beta\)-Hölder 常数，所以 \(U\in\mathscr H_+\)。
4. **退出固定指数块。** 对 \(0<t<r\) 取 \(z_t=a+(t,0)\)。两 cutoff 在 \(a,z_t\) 均为 1，故
\[
\frac{\|U(z_t)-U(a)\|_2}{t^\alpha}
\ge ct^{\beta-\alpha}-(1-\mu)M\longrightarrow+\infty.
\tag{RH9}
\]
所以 \(U\) 不具有任何有限 \(\alpha\)-Hölder 常数，特别地不属于 \(\mathscr H_{\alpha,M}\)。反三角估计排除了原增量抵消尖点的问题。

这证明每个非空块在 **\(\mathscr H_+\) 内**没有内点；结合闭性及空块情形，所有固定块在该相对空间内无处稠密。由 (RH5)，\(\mathscr H_+\) 在自身中第一纲。它非空，因为 \(P\in\mathscr H_{1,1}\)。证明完毕。

<a id="rht-boundary"></a>
## 类别后果与严禁的拓扑替换

若 \(A\subseteq\mathscr H_+\)，则 \(A=\bigcup_{m,n}(A\cap\mathscr H_{1/m,n})\)；每项在 \(\mathscr H_+\) 中的闭包包含于闭无处稠密块 \(\mathscr H_{1/m,n}\)。因此 \(A\) 及其相对补集都在 \(\mathscr H_+\) 中第一纲，也都余稀。这直接解释为什么仅说“LT 子类在该 Hölder 分母里第一纲”不能区分类覆盖量。

“每个子集都自第一纲”则是错误推论：\(A=\{P\}\) 在自己的单点拓扑中是 Baire，唯一无处稠密子集是空集。源文“其中任何子集”必须解释为在环境 \(\mathscr H_+\) 中。

同样不能从 C180 的宽层结论推出本页。C180 的扰动允许输出离开 \(S\)，且未要求扰动还具有某个正 Hölder 指数。本页 (RH7) 同时留在 \(S\) 并由明确有限的 \(\beta\)-Hölder 常数留在 \(\mathscr H_+\)，这两个门才给相对定理。反过来也不能把本页推广到任意 \(K,S\)：当 \(K=[-1,1]\)、\(S=\{0\}\) 时，唯一回缩 \(T=0\) 具有所有正 Hölder 指数，正 Hölder 回缩类是非空单点，非自第一纲。该反例正是 [C180 的一步尾边界](uniform_holder_thinness.md#uht-boundary) 的相同对象。

<a id="rht-graph"></a>
## 完整源图接口与 RLEB 名称的剩余门

对固定 \(\lambda>0\) 和 \(T\in\mathscr M\)，完整关系
\[
F_{T,K}(u)=\{(z-u)/\lambda:z\in K,\ T(z)=u\}
\tag{RH10}
\]
的图紧闭；完整 \(J_{\lambda F_{T,K}}\) 在 \(K\) 上等于 \(T\)，在域外为空；精确零集为 \(S\)。这些等式由 [C180 的已证图卡](uniform_holder_thinness.md#uht-source-card) 逐字专门化，未从先给原图删除任何纤维。所有非空输出纤维的 \(u\) 都属于 \(S\)，且因底边恒等有 \(0\in F_{T,K}(u)\)，故真实残差 \(r_{F_{T,K}}(u)=0\) 且 \(d(u,S)=0\)。D04 型真实 EB 的左端确实恒零。

在此**相同整个紧输入域**，正 Hölder 与反射正 Hölder 完全等价：若 \(T\) 为 \(\gamma\)-Hölder、常数 \(M\)、\(0<\gamma\le1\)，则
\[
\|(2T-I)z-(2T-I)w\|_2
\le(2M+D^{1-\gamma})\|z-w\|_2^\gamma.
\tag{RH11}
\]
反向由 \(2T=I+(2T-I)\) 得常数 \((D^{1-\gamma}+L)/2\)。若反射条件只要求 \(\|z-w\|\le R\) 且 \(R>0\)，远点使用 \(\|Tz-Tw\|\le D\) 即得全域常数；这是 [UH12–13](uniform_holder_thinness.md#uht-interfaces) 的准确同对象接口。

由此恢复的类别命题是正 Hölder 回缩类自身第一纲，另恢复明定反射模类与之相同。来源 B2 还把该类直接称作全部 “RLEB 成员”。**这一名称等价保留具体未闭义务**：须指定 direct/energy 原生证书的精确定义、允许的 gauge 类、共同输入/输出域及边界 coverage，并证明与 (RH10)–(RH11) 等价。D04 允许零 gauge，它在输出上给真 EB 和零兼容左端，但这个观察本身不认证任意来源的规范 gauge、能量接口或环境开邻域 coverage；尤其 \(J\) 在 \(\mathbb R^2\setminus K\) 为空。改变 \(\lambda\) 重定义 (RH10) 也会改变原关系，不能写成同一既有原图的任意步长结论。

全体 RLEB 分母、全体连续极限回缩、原 \((X_D,d_{\rm dyn})\) 的孔隙性、所有步长粗糙化和总体 RLEB–LT–极大单调比较继续开放。它们不由本矩形一步层的恢复结案。

<a id="rht-source"></a>
## 来源与重构边界

直接来源为 [07_stage_synthesis.md](../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/03_CLASSIFICATION_STAGE/ppa_classification_team/07_stage_synthesis.md) B2，物理 LF105–117；14130 字节、202 LF、SHA-256 `ba894d3dee5fabcdc29a312cf01f5383d53d7dbdda9028c511f185c8d164f906`。来源只汇总结论；相邻 [05_obstruction_audit.md](../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/03_CLASSIFICATION_STAGE/ppa_classification_team/05_obstruction_audit.md) LF146–205 给插值加低阶尖点的草证。本页改从固定块内点直接扰动，省去不必要的 Lipschitz 插值，但完整保留其矩形/底边/回缩/相对一致拓扑身份。

本页证明只用规范定义与上列估计，不依赖历史稿补条件。全202 LF独立断言的枚举去向见 [本次全源审计](../audit/RELATIVE_HOLDER_COVERAGE_2026_10_07.md)。历史审查行为、源报告的其他结构定理及全球先行性与本页数学状态分开。
