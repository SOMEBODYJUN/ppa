# 低 (L) 步长支的固定图动力学审计

本文固定 (0<L<1/2)、步长 (lambda>0)、(ell=lambda L)，并记

\[
 \rho_L:=\frac{L}{1-L}.
\]

低参数反向包络的步长支在目标比率 (r>\rho_L) 时为

\[
 s=\frac{rt}{L},\qquad a=Ls=rt,qquad
 b:=s-t=\frac{r-L}{L}t>a.
\tag{L1}
\]

这里 (t=d(x,S))、(a=d(y,S))、(s=\|x-y\|)。这份记录区分单步取等、同一闭零集上的逐步取等，以及凸性和局部孤立性施加的限制。

## 1. 低 (L) 步长支的必要几何

设一条边 (x\mapsto y) 以最近锚 (p\in P_S(x)) 取到平面引理中的步长支，并且 (r=a/t>\rho_L)。能量等号和 (s=B=t+b) 同时成立。三角形等号给出

\[
 x=p+t e,\qquad y=p-b e,\qquad \|e\|=1,
\tag{L2}
\]

并且输出最近锚 (q\in P_S(y)) 满足

\[
 y=q+a e',\qquad \|e'\|=1.
\tag{L3}
\]

由于 (b>a)，必有 (q\ne p)。如果 (q=p)，则 (d(y,S)=\|y-p\|=b)，与 (a<b) 矛盾。因此低 (L) 的步长支不是一个固定锚反射，它强制每一步把输入最近锚 (p) 换成输出最近锚 (q)。反解 (L2)--(L3) 得

\[
 p-q=b e+a e'.
\tag{L4}
\]

这条恒等式是后面固定零集审计的唯一几何输入。它没有把 (p,q) 放在同一直线上。

## 2. 同一闭零集上的完整图逐步实现

### 命题 L1（离散锚链的步长支实现）

设 (0<L<1/2)。取一列 (t_k>0)，令

\[
 t_{k+1}=A(t_k),\qquad r_k:=\frac{t_{k+1}}{t_k}\in(\rho_L,1),
 \qquad s_k:=\frac{t_{k+1}}L,
 \qquad b_k:=s_k-t_k.
\tag{L5}
\]

在实直线上递归定义

\[
 x_{k+1}=x_k-s_k,
 \qquad p_k=x_k-t_k.
\tag{L6}
\]

令

\[
 S=\{p_k:k\ge0\}
 \quad\text{若 }\sum_k s_k=\infty,
\tag{L7a}
\]

而在 \(\sum_k s_k<\infty\) 时再加入唯一极限

\[
 x_\infty:=x_0-\sum_{k=0}^{\infty}s_k,
 \qquad S=\{p_k:k\ge0\}\cup\{x_\infty\}.
\tag{L7b}
\]

则 (S\) 是闭集，且

\[
 d(x_k,S)=t_k,
 \qquad P_S(x_k)=\{p_k\},
 \qquad
 x_{k+1}=p_k-b_k,
 \qquad d(x_{k+1},S)=t_{k+1},
 \qquad P_S(x_{k+1})=\{p_{k+1}\}.
\tag{L8}
\]

因此

\[
 \|x_k-x_{k+1}\|=s_k,
 \qquad
 d(x_{k+1},S)=L\|x_k-x_{k+1}\|=A(t_k),
\tag{L9}
\]

并且最近锚能量缺陷恰为步长支的预算

\[
 D(t_k)=s_kb_k
 =t_k^2\frac{r_k(r_k-L)}{L^2}.
\tag{L10}
\]

#### 证明

由 (r_k>\rho_L>L) 得 (s_k>t_k)。又有

\[
 p_k-p_{k+1}=s_k+t_{k+1}-t_k
 =t_k\left(\frac{r_k}{L}+r_k-1\right)>0,
\tag{L11}
\]

所以 (p_k) 严格递减。若总和发散，(p_k\to-\infty)，故 (L7a) 是闭集。若总和收敛，则 (x_k\to x_\infty)、(p_k=x_k-t_k\to x_\infty)，故 (L7b) 是闭集。

对 (j>k)，

\[
 x_k-p_j=\sum_{i=k}^{j-1}s_i+t_j\ge s_k>t_k.
\tag{L12}
\]

若总和收敛，(x_k-x_\infty=\sum_{i=k}^{\infty}s_i\ge s_k>t_k)。对 (j<k)，由锚点递减，最可能竞争的是 (p_{k-1})，而

\[
 p_{k-1}-x_k=s_{k-1}-t_{k-1}
 =t_k/L-t_{k-1}>t_k
\tag{L13}
\]

其中最后一个严格不等式等价于 (r_{k-1}>L/(1-L))。因此 (p_k) 是 (x_k) 的唯一最近点。把 (k) 换成 (k+1) 得第二组结论。最后，(x_{k+1}=x_k-s_k=p_k-(s_k-t_k)=p_k-b_k)，所以 (L10) 来自

\[
 \langle x_k-x_{k+1},x_{k+1}-p_k\rangle=-s_kb_k.
\]

证毕。

### 命题 L2（完整闭图和真残差）

在命题 L1 的 (S) 上定义

\[
 J(x):=P_S(x)\cup
 \begin{cases}
 \{x_{k+1}\},&x=x_k,\\
 \varnothing,&x\notin\{x_k:k\ge0\}.
 \end{cases}
\tag{L14}
\]

则 \(\operatorname{gph}J\) 是闭集，(J) 全域非空，且

\[
 F(y):=\{(x-y)/\lambda:y\in J(x)\}
\tag{L15}
\]

是闭图完整关系并满足 (J=J_{\lambda F})、\(\operatorname{zer}F=S\)。对附加轨道边

\[
 F(x_{k+1})=\{s_k/\lambda\},
 \qquad r_F(x_{k+1})=s_k/\lambda,
\tag{L16}
\]

因此真误差界在每一步取等

\[
 d(x_{k+1},S)=\lambda L\,r_F(x_{k+1}).
\tag{L17}
\]

#### 证明

闭集上的欧氏投影图闭。附加边集合 \(\{(x_k,x_{k+1})\}\) 没有有限聚点，或在总和收敛时唯一聚点是 \((x_\infty,x_\infty)\)，而该点已经属于 \(\operatorname{gph}P_S\)。所以 (L14) 的图闭。由 (L15) 的反演定义，(J=J_{\lambda F}) 是恒等式。零点满足 (0\in F(y)\) 当且仅当 (y\in J(y))，这在 (L14) 中当且仅当 (y\in S)。附加边的唯一入边是 (x_k\to x_{k+1})，投影边的输出在 (S) 上真残差为零，故 (L16)--(L17) 成立。证毕。

命题 L2 给出同一 (S)、同一完整固定规则 (J) 和同一 (F) 上的逐步取等。若需要严格违反给定比较曲线，只需把 (L5) 中的实际比率 (r_k) 取为 (A(t_k)/t_k+\varepsilon_k)，并在 (L10) 使用实际比率。步长支的失败仍然逐步发生，所需条件只是实际比率保持大于 \(\rho_L\)。

若假设要求缺陷函数在整个工作半径上连续，可在离散点 (t_k) 上先规定 (L10) 的值，再在相邻 (t_k) 之间作非负线性插值，并令 (D(0)=0)。因为 (0\le r_k<1)，有 (D(t_k)=O(t_k^2))，故当 (t_k\downarrow0) 时该插值在零点连续。投影边的缺陷为零，因而同一个延拓同时覆盖所有图边。

### 例 L3（局部孤立零点和无限长度）

取

\[
 A(t)=\frac{t}{1+t},
 \qquad t_k=\frac1{t_0^{-1}+k}.
\tag{L18}
\]

选 (t_0<(1/\rho_L)-1)，则 (r_k=(1+t_k)^{-1}>\rho_L) 对所有 (k) 成立。此时

\[
 s_k=\frac{t_{k+1}}L\sim\frac1{Lk},
 \qquad \sum_k s_k=\infty.
\tag{L19}
\]

命题 L1 的 (S=\{p_k\}) 向 (-\infty) 发散，因此是离散闭集，每个零点都是局部孤立的。命题 L2 给出同一离散闭零集上的完整图无限轨道，且

\[
 d(x_k,S)=t_k\downarrow0,
 \qquad \sum_k\|x_{k+1}-x_k\|=\infty.
\tag{L20}
\]

这把低 (L) 的单步步长支提升为固定规则的逐步无限长度见证。

## 3. 局部孤立零集的有限长度障碍

### 命题 L4（任意闭集上的聚点障碍）

设 (S\subset\mathbb R^n) 闭，且一条无限轨道满足步长支 (L2)--(L3)、(t_k\downarrow0) 和 \(\sum_k s_k<\infty)。若极限零点 \(x_\infty=\lim x_k\) 在 (S) 中孤立，则不可能从某个指标起始终满足 (b_k>a_k)。

#### 证明

有限总长和闭性给出 (x_k\to x_\infty\in S)。因为 (t_k\to0)，所有最近锚 (p_k,q_k) 也趋于 (x_\infty)。若 (x_\infty) 孤立，存在 \(\delta>0) 使 (S\cap B(x_\infty,\delta)=\{x_\infty\})。故充分大的 (k) 有 (p_k=q_k=x_\infty)。但 (L2)--(L3) 此时给出 (d(x_{k+1},S)=\|x_{k+1}-p_k\|=b_k)，与 (a_k<b_k) 矛盾。证毕。

因此局部孤立零集并没有一般性的低 (L) 无限长度障碍。它只排除总长度可和的步长支链。例 L3 的非可和曲线绕开了这个障碍。

## 4. 闭凸集和仿射集

### 命题 L5（仿射集上一条步长支边都不可能）

若 (S) 是闭仿射集，则低 (L) 步长支的任何边都不可能满足 (a<b)。

#### 证明

写 (x=p+t e)、(y=p-b e)，其中 (p=P_Sx) 且 (e\perp\operatorname{lin}S)。因为 (y) 与 (p) 的法向分量同向，(P_Sy=p)，故 (d(y,S)=b)。这与步长支要求 (a=Lb<b) 矛盾。等价地，在 (L4) 中 (p,q\in S) 且 (p-q\in\operatorname{lin}S)，而两边的法向分量迫使 (p=q)。证毕。

### 命题 L6a（局部锥和多面体闭凸集的收敛锚障碍）

设 \(S\) 是闭凸集，\(p_\infty\in S\)，并设存在闭凸锥 \(C\) 使得在 \(p_\infty\) 的某个邻域内

\[
 (S-p_\infty)\cap U=C\cap U,
\]

且充分靠近 \(p_\infty\) 的锚点 \(p_k,p_{k+1}\) 的外法向 \(e_k,e'_k\) 属于 \(C^\circ\)（极锥）。若低 \(L\) 步长边满足

\[
 p_k-p_{k+1}=b_k e_k+a_k e'_k,
 \qquad b_k>a_k>0,
\]

则不存在 (p_k\to p_\infty) 的非平凡尾链。特别地，有限维多面体闭凸集满足此条件：取 (C=T_S(p_\infty))，则 (C^\circ=N_S(p_\infty))，而 (p_k) 足够接近 (p_\infty) 时的活跃约束集合是 (p_\infty) 处活跃约束集合的子集，故 (N_S(p_k)\subset C^\circ)。

#### 证明

令 \(z_k=p_k-p_\infty\)。由局部锥条件 \(z_k\in C\)，而

\[
 d_k:=p_k-p_{k+1}=b_k e_k+a_k e'_k\in C^\circ .
\]

极性给出 \(\langle z_k,d_k\rangle\le0\)。因此

\[
 \|z_{k+1}\|^2
 =\|z_k-d_k\|^2
 =\|z_k\|^2-2\langle z_k,d_k\rangle+\|d_k\|^2
 \ge \|z_k\|^2+\|d_k\|^2.
\]

锚点距离沿尾部严格递增，除非 \(d_k=0\)。但 \(b_k>a_k\) 且 \(e_k,e'_k\) 为单位向量时不可能有 \(d_k=0\)。这与 \(z_k\to0\) 矛盾。多面体的活跃约束说明了最后的包含关系，故多面体情形成立。证毕。

### 候选 L6（一般闭凸集上的有限长度步长链）

设 (S\subset\mathbb R^n) 是非空闭凸集。不存在无限轨道满足 (L2)--(L3)、(a_k<b_k)、(t_k\downarrow0) 且 \(\sum_k s_k<\infty\)。

#### 当前审计状态

有限总长给出 (x_k\to\bar x\in S)，且 (p_k=P_Sx_k\to\bar x)、(q_k=p_{k+1}\to\bar x)。令 (M=\operatorname{aff}S)，并把 (S) 视为 (M) 中的全维闭凸集。若 \(\bar x\) 属于 (S) 的相对内部，则充分大 (p_k) 有相对邻域。此时输入法向量的 (M)-分量为零，且同一相对坐标的 (y_k) 的最近点仍为 (p_k)，从而 (a_k=b_k)，矛盾。因此 \(\bar x\) 是相对边界。

取非零 (n\in\operatorname{ri}N^M_S(\bar x))。相对法锥在全维 (M) 中是尖的。设

\[
 u_k=P_M e_k\in N^M_S(p_k),
 \qquad v_k=P_M e'_k\in N^M_S(q_k).
\]

闭法锥图和 (p_k,q_k\to\bar x) 表明，除去等于零的向量，任意归一化聚点属于 (N^M_S(\bar x)\)。因为 (n) 在法锥相对内部，充分大 (k) 有

\[
 \langle n,u_k\rangle\ge0,
 \qquad
 \langle n,v_k\rangle\ge0,
\tag{L21}
\]

且至少一项严格为正。否则 (u_k=v_k=0)，由 (L4) 的 (M)-分量得 (p_k=q_k)，再由 (a_k<b_k) 矛盾。原稿在此处接着使用的符号推理目前不能接受。一般尖闭凸锥并非自对偶，(n\in\operatorname{ri}N^M_S(\bar x)) 不保证 (\langle n,u\rangle\ge0) 对所有 (u\in N^M_S(\bar x))。因此下面的单调标量论证尚未证明闭凸集的命题。若能另外提供 (n\in N^M_S(\bar x)\cap(N^M_S(\bar x))^*) 以及近端法向最终落入其正半空间，该论证才可作为条件性障碍。对充分大的 (k)，(L4) 给出

\[
 \langle n,p_k-p_{k+1}\rangle
 =b_k\langle n,u_k\rangle+a_k\langle n,v_k\rangle>0.
\tag{L22}
\]

另一方面 (n\in N^M_S(\bar x)) 意味着

\[
 \langle n,p_k-\bar x\rangle\le0
\quad\text{对所有 }k.
\tag{L23}
\]

故标量序列 (h_k=\langle n,p_k\rangle) 从某个指标起严格递减，且 (h_k\le\langle n,\bar x\rangle)。在附加的锐法锥条件下，这与 (p_k\to\bar x) 矛盾。当前一般闭凸锥不满足该附加条件，因此这里保留为条件性障碍，不能写成一般命题的证明。

候选 L6 只给出一个需要补强的法锥障碍。命题 L6a 已经闭合局部锥（特别是多面体）闭凸集的可和尾障碍；对一般弯曲或非局部锥的闭凸集，是否允许同一完整规则的低 (L) 步长链仍需额外研究。命题 L5 已经排除了仿射子类。离散锚链命题 L1--L2 说明任意闭集和局部孤立闭集仍可实现非可和版本。

## 5. 研究结论和论文措辞

1. 低 (L) 步长支的逐尺度锐性可以在同一完整图和同一闭零集上逐步实现，前提是轨道比率始终满足 (A(t_k)/t_k>\rho_L)。这不需要每一步更换算子。
2. 轨道若非可和，可以选取 (A(t)=t/(1+t)) 的离散闭零集，得到局部孤立零点、距离趋零和物理长度发散。
3. 任何局部孤立零集只排除可和步长链。不能把局部孤立性写成低 (L) 动态尖锐性的普遍障碍。
4. 闭仿射集甚至不能产生一条 (a<b) 的低 (L) 步长支边；命题 L6a 进一步排除了局部锥、特别是多面体闭凸集的收敛锚链。一般弯曲闭凸集的可和/非可和链仍保持未决，不把局部锥结论外推到整个凸类。
5. 因此主文应把“固定闭零集的动态达到”写成任意闭集的构造性结果，并同时注明凸性范围的上述边界。不能把单步二维充分性直接表述为固定仿射或固定凸零集上的无限轨道达到。

