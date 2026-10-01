# 定义与接口：先固定对象，再谈蕴含

本页是重构的数学定义层。它不把任何稿件的证明状态自动提升；来源键及版本见 [SOURCES.md](SOURCES.md)。本文中的“完整”总是指被声明的关系的**整个图**，而不是一次迭代中选中的支。

<a id="d01"></a>
## D01 · 原关系、残差与图剪切

在实 Hilbert 空间 \(H\) 上令 \(F:H\rightrightarrows H\)，
\(\operatorname{gph}F=\{(u,v):v\in F(u)\}\)，\(S\subset F^{-1}(0)\)。若讨论距离收敛，通常另要求 \(S\ne\varnothing\) 闭；仅有 \(S\subset F^{-1}(0)\) 不等于 \(S=F^{-1}(0)\)。固定 \(\lambda>0\)：

\[
M_+(u,v)=u+\lambda v,\quad M_-(u,v)=u-\lambda v,\quad
J_{\lambda F}(p)=\{u:p-u\in\lambda F(u)\},\quad
r_F(u)=\inf_{v\in F(u)}\|v\|.
\]

空纤维的残差为 \(+\infty\)。若 \(\mathcal G\subset\operatorname{gph}F\)，则 \(J_{\mathcal G}\) 只反演 \(\mathcal G\)；它一般不等于完整 \(J_{\lambda F}\)。在固定步长且**完整输入和完整输出纤维**已知时，\(T=J_{\lambda F}\) 反向决定整个图：

\[
F(u)=\{(p-u)/\lambda:u\in T(p)\}.
\]

局部 \(T|_U\) 则不决定域外图、完整逆纤维或 \(r_F\)。这一缺口贯穿 [算子空间比较](operator_space.md) 与 [解选择](solution_selection.md)。来源：S19 `theorem_spine.tex` 定义与 `ass:local-rleb`；S20 `07_final_handoff.md` §2。

<a id="d02"></a>
## D02 · 同一图块、同一尺度的全对 RL

对 \((u,v),(u',v')\in\mathcal G\) 置 \(a=u-u'\)，\(b=v-v'\)。局部参数 \(R>0,L\ge0,0<\gamma\le1\) 的 \(\mathrm{RL}(\lambda,\gamma,L;R)\) 是在**所有**满足 \(\|a+\lambda b\|\le R\) 的图点对上

\[
\|a-\lambda b\|\le L\|a+\lambda b\|^\gamma.
\tag{D02}
\]

它等价于 \(\lambda\langle a,b\rangle\ge[\|a+\lambda b\|^2-L^2\|a+\lambda b\|^{2\gamma}]/4\)。固定解点的 anchored 比较是较弱的**不同命题**；局部输入球半径 \(r\) 内的任意两点可能相距 \(2r\)，不能把中心半径当作成对尺度。S19 `def:graph-RL`。全局结构稿 S23 使用非空完整图、\(L>0,0<\gamma<1\)，对所有图点对和所有尺度成立；它不包含局部 coverage、EB 或 PPA 的结论。

<a id="d03"></a>
## D03 · Cayley 坐标与 coverage 是两件事

若 D02 成立，则 \(M_+|_{\mathcal G}\) 单射。写 \(D=M_+(\mathcal G)\)、\(C=M_-\circ(M_+|_{\mathcal G})^{-1}:D\to H\)，则 \(C\) 在测试尺度内为 \(L\)-Hölder，并有

\[
u=(p+C(p))/2,\qquad v=(p-C(p))/(2\lambda),\qquad
J_{\mathcal G}(p)=(p+C(p))/2.
\tag{D03}
\]

反向也成立，但 D02 **不推出** \(D=H\)，甚至不推出所需局部输入集包含于 \(D\)。取 \(p=p'\) 时得到同输入唯一性，只对 \(\mathcal G\) 的纤维有效。完整结构问题中“graph-maximal”固定 \((\lambda,L,\gamma)\)：不能在保留 D02 的条件下真扩图；它不是极大单调。全局 \(D=H\) 蕴含该意义的 graph-maximal；反向借同常数 Hölder 扩张在**实 Hilbert 空间**也成立，不限有限维。有限维限制始于后续 properness/degree 的完整纤维分类，见 [结构稿](holder_structure.md)。S23 `lem:cayley`，S19 `lem:minty-equivalence`。

<a id="d04"></a>
## D04 · 真误差界、兼容和留域

\(\psi:[0,\bar t]\to[0,\infty)\) 非减、\(\psi(0)=0\)、原点连续。输出集合 \(V\) 上的真实 gauge EB 是
\(d(y,S)\le\psi(r_F(y))\) 对 \(y\in V,r_F(y)\le\bar t\) 成立。它独立于 D02 和 coverage；把已选图值 \(v\) 的范数代入只能凭 \(r_F(y)\le\|v\|\) 与 \(\psi\) 非减推**上界**，不能把两种残差混为定义。

局部收敛还需对实际输出的 EB、\(U_R\subset M_+(\mathcal G)\)、解点图比较、\(\psi((r+Lr^\gamma)/(2\lambda))\le\kappa r\) 与轨道总步长小于离开 \(U\) 的距离。缺任一项不能从 RL 单独推出 PPA。详细量词见 [RLEB–PPA](rleb_ppa.md)。

## Definition map 与禁止的偷换

| 接口 | 所需额外数据 | 错误的跳跃 |
| --- | --- | --- |
| D02 → D03 | 同一图块、步长、输入对尺度 | 单射 → 输入覆盖 |
| D03 → 完整 \(F\) | 所有输入与完整 \(T(p)\) 纤维 | 局部 \(J_{\mathcal G}\) → 全局 \(J_{\lambda F}\) |
| D02 + D04 → PPA | coverage、实际输出 EB、兼容、留域 | 全局 RL → 任意初值收敛 |
| 全局 RL → 结构影子 | 另一组全图全尺度假设 | 影子近似 → 真实逆分支选择 |
| 特殊有限维纤维实现 → 局部回缩 | 须另加 EB、Dini、留域及邻域覆盖 | 任意紧零集 → 自动为邻域回缩 |

数学节点的合取关系与版本边界登记在 [超边图](HYPERGRAPH.md)。
