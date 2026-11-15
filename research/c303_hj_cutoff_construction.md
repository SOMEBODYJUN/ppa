# C303：HJ cutoff 的可复核支撑构造门

状态：**source-conditional / candidate**。本页把 HJ 原始构造中 cutoff 的文字条件与 C303 所需的整个尾管分离放在同一坐标约定下。它证明一个满足已读条件的显式构造；仍需逐字确认原文没有未摘录的额外归一化或能量排序要求。

## 1. 原始条件与记号分离

HJ 的构造在公式 (8) 中使用
\[
f(x,y)=e^{-(\theta+2p\pi)^2}\,\phi(x,y)\,(1-\Pi_{\rm cut}(x,y)).
\]
原文对 \(\Pi_{\rm cut}\) 明确写出的条件是：其 support 连通，包含
\(\gamma_1(0)\)、\(\gamma_2(0)\) 作为内点，并且在足够大的角度上两条
\(\gamma_i\) 曲线不属于该 support。这里把 cutoff 记为 \(\Pi_{\rm cut}\)，把物理投影另记为
\[
\mathcal P(r,\theta)=r(\cos\theta,\sin\theta),
\]
避免把支撑条件与尾管的投影单射条件混为同一个 \(\Pi\)。

## 2. Connected compact dumbbell 构造

令
\[
0<\eta_0<\frac12\min\{\gamma_1(0)-1,\gamma_2(0)-1\}.
\]
两初始点都位于开环带 \(r>1+\eta_0\) 内。取一条完全落在该开环带中的紧连通光滑路径，连接两个初始点；取其足够小的闭管邻域 \(K\) 使
\[
K\Subset\{(x,y): |(x,y)|>1+\eta_0\}.
\]
由标准 bump 构造，存在
\[
\Pi_{\rm cut}\in C_c^\infty(\mathbb R^2,[0,1]),
\qquad \operatorname{supp}\Pi_{\rm cut}=K'
\]
其中 \(K'\) 是包含该路径的紧连通闭集，且两个初始点是 support 的内点。这个构造满足 HJ 已明确列出的 support 条件，并把 support 置于一个固定的物理外环带。

再取 \(\theta_0\) 足够大，使
\[
\gamma_2(\theta)<1+\eta_0/2
\qquad(\theta\ge\theta_0).
\tag{HC1}
\]
因为 \(\gamma_2(\theta)\to1\)，这是可能的。于是两条尾部边界曲线以及其间的归一化尾条带都可与 \(K'\) 分离。

更具体地，令
\[
\widetilde D_\eta
 =\{(r,\theta):\theta\ge\theta_0,
                    |q(r,\theta)|\le\beta+\eta\},
\qquad 0<\eta<1-\beta.
\]
由 \(q_r=2/((\mu-1)e^{-\theta})\) 和 \(q\)-条带宽度为常数，增大 \(\theta_0\) 后有
\[
\overline{\widetilde D_\eta}\subset\{r<1+\eta_0/2\}.
\tag{HC2}
\]
因此
\[
\operatorname{supp}\Pi_{\rm cut}\cap
\mathcal P(\overline{\widetilde D_\eta})=\varnothing,
\qquad
\Pi_{\rm cut}=0
\quad\text{on }\mathcal P(\overline{\widetilde D_\eta}).
\tag{HC3}
\]
在整个 normalized outer strip 上，HJ 公式精确简化为
\[
f=h(\theta)F(q(r,\theta)).
\]

## 3. 对全局延拓的影响

\(\Pi_{\rm cut}\) 为紧支撑 \(C^\infty\) bump，且 HJ 的 \(F\) 在两端平坦。因而该 cutoff 不破坏 HJ 逐阶平坦延拓，只在固定初始外环带内改变函数。结合 HJ 的全局 \(C^\infty\) 论证，所得 \(f\)、\(\chi_a\) 与全局 normal-error/resolvent 引理的有限导数界相容。

## 4. 仍然开放的 source gate

本页的构造把“仅排除两条尾边界曲线”强化为“整个闭 normalized outer strip 与 cutoff support 分离”，但它仍依赖两项逐字核对：

1. HJ 原文对 \(\Pi\) 没有额外值域、能量排序或指定支撑形状条件；
2. 所选 bump 的初始局部化仍保留原文后续 \(\theta_0,\theta_1\) 选择和不收敛证明所需的全部性质。

在这两项未从原始构造逐条核完前，(HC1)--(HC3) 是 source-conditional evidence，而不是已认证的 HJ theorem import。C303 的整体裁决仍为 **continue validation**。
