# C303：HJ cutoff 的可复核支撑构造门

状态：**source-conditional / candidate**。本页把 HJ 原始构造中 cutoff 的文字条件与 C303 所需的整个尾管分离放在同一坐标约定下。它证明一个满足已读条件的显式构造；仍需逐字确认原文没有未摘录的额外归一化或能量排序要求。

## 1. 原始条件与记号分离

HJ 的构造在公式 (8) 中使用
\[
f(x,y)=e^{-(\theta+2p\pi)^2}\,\phi(x,y)\,(1-\Pi_{\rm cut}(x,y)).
\]
原文对 \(\Pi_{\rm cut}\) 明确写出的条件是：先固定
\(\theta_{\rm supp}\in(0,2\pi)\)，其 support 连通，包含
\(\gamma_1(0)\)、\(\gamma_2(0)\) 作为内点，并且对
\(\theta>\theta_{\rm supp}\) 两条 \(\gamma_i\) 曲线不属于该 support。
这里把 cutoff 记为 \(\Pi_{\rm cut}\)，把物理投影另记为
\[
\mathcal P(r,\theta)=r(\cos\theta,\sin\theta),
\]
避免把支撑条件与尾管的投影单射条件混为同一个 \(\Pi\)。原文随后把显式梯度公式记为
\(X:=\nabla f\)，但公式中的径向项实际是 \(-2hF'/\Delta\)，与
\(Y=-\nabla f\) 一致；边界符号导入 C303 时按显式公式和
\(Y=-\nabla f\) 解释，详见 [HJ source audit](audit/C303_HJ_SOURCE_AUDIT_2026-11-15.md)。

## 2. Connected compact dumbbell 构造

原文的非重叠条件在
\(\gamma_1(\theta)=1+e^{-\theta}\)、\(\gamma_2(\theta)=1+\mu e^{-\theta}\)
下给出 \(1<\mu<e^{2\pi}\)。取足够小的
\(0<\delta<2\pi\)，令 \(\theta_{\rm supp}=2\pi-\delta\)，并选择
\[
\sup_{\theta\in[2\pi-\delta,2\pi]}\gamma_2(\theta)<R<2.
\tag{HC0}
\]
这一步可行，因为 \(\gamma_2(2\pi)=1+\mu e^{-2\pi}<2\)。
两初始点位于正实轴、半径分别为 \(\gamma_1(0)=2\) 与
\(\gamma_2(0)=1+\mu\)，因而都落在 \(r>R\) 中。取一条完全落在
\(\{r>R\}\) 内、连接两个初始点的紧连通光滑路径，并将其限制在一条
足够窄的正实轴角锥内；取其足够小的闭管邻域 \(K\) 使
\[
K\Subset\{(x,y): |(x,y)|>R\}.
\]
由标准 bump 构造，存在
\[
\Pi_{\rm cut}\in C_c^\infty(\mathbb R^2,[0,1]),
\qquad \operatorname{supp}\Pi_{\rm cut}=K'
\]
其中 \(K'\) 是包含该路径的紧连通闭集，且两个初始点是 support 的内点。
对 \(\theta\in(\theta_{\rm supp},2\pi)\)，(HC0) 给出
\(\gamma_i(\theta)<R\)；对 \(\theta\ge2\pi\)，
\(\gamma_2(\theta)\le\gamma_2(2\pi)<R\)。因此全部满足
\(\theta>\theta_{\rm supp}\) 的边界曲线都与 \(K'\) 分离，且原文的
support 条件得到满足。

再取尾部阈值 \(\theta_{\rm tail}\) 足够大，使
\[
\gamma_2(\theta)<1+\eta_0/2
\qquad(\theta\ge\theta_{\rm tail}),
\tag{HC1}
\]
其中 \(0<\eta_0<R-1\)。因为 \(\gamma_2(\theta)\to1\)，这是可能的。

更具体地，令
\[
\widetilde D_\eta
 =\{(r,\theta):\theta\ge\theta_{\rm tail},
                    |q(r,\theta)|\le\beta+\eta\},
\qquad 0<\eta<1-\beta.
\]
由 \(q_r=2/((\mu-1)e^{-\theta})\) 和 \(q\)-条带宽度为常数，增大 \(\theta_{\rm tail}\) 后有
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

\(\Pi_{\rm cut}\) 为紧支撑 \(C^\infty\) bump，且 HJ 的 \(F\) 在两端平坦。因而该 cutoff 不破坏 HJ 逐阶平坦延拓，只在固定初始外环带内改变函数。结合 HJ 的全局 \(C^\infty\) 论证，所得 \(f\)、\(\chi_a\) 与全局 normal-error/resolvent 引理的有限导数界相容。尾管内的边界符号必须使用显式公式对应的 \(Y=-\nabla f\)，不能按原文“\(X=\nabla f\)”的字面号导入。

## 4. 仍然开放的 source gate

本页的构造把“仅排除两条尾边界曲线”强化为“整个闭 normalized outer strip 与 cutoff support 分离”，但它仍依赖两项逐字核对：

1. HJ 原文对 \(\Pi\) 没有额外值域、能量排序或指定支撑形状条件；
2. 所选 bump 的初始局部化仍保留原文后续 \(\theta_{\rm tail},\theta_1\) 选择和不收敛证明所需的全部性质。

在这两项未从原始构造逐条核完前，(HC1)--(HC3) 是 source-conditional evidence，而不是已认证的 HJ theorem import。C303 的整体裁决仍为 **continue validation**。
