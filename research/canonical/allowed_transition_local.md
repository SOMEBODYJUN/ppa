# 允许转移的共同证书：多选择有限长度与实际幂半径

本页重构 T4 核心终审中已经写定、但现行正文尚未展开的允许转移接口。它不要求某个单值图块；每一步可在同一个允许转移集合中任意选择。这里的 EB 评价的是**所选图值**，不是完整纤维的下确界。与 [C02-v2](../../CLAIMS.md#c02-v2)、[C53](named_branch_local.md#nb-local) 的不同对象和量词保持分开。

<a id="at-object"></a>
## AT-OBJECT · 同一目标、输入域与全部允许转移

固定 Euclidean 空间 \(X=\mathbb R^n\)、\(n\ge1\)、关系 \(F:X\rightrightarrows X\)、\(\lambda>0\)、非空闭集 \(S\subset F^{-1}(0)\)、开集 \(V\subset X\)、\(\eta>0\)，以及

\[
\mathcal A\subset\{(x,y,v):x=y+\lambda v,\ v\in F(y)\},\qquad
\mathcal A(x)=\{(y,v):(x,y,v)\in\mathcal A\}.
\tag{AT1}
\]

令 \(V_\eta=\{x\in V:d(x,S)<\eta\}\)。固定有限非减函数
\(\omega:[0,\eta)\to[0,\infty)\)、\(\psi:[0,\infty)\to[0,\infty)\)，且 \(\omega(0)=\psi(0)=0\)。在同一 \(F,S,V,\lambda,\eta,\mathcal A\) 上合取：

1. 对全部 \(x\in V_\eta\)，\(\mathcal A(x)\ne\varnothing\)。
2. 对全部 \(x\in V_\eta\) 及全部 \((y,v)\in\mathcal A(x)\)，存在可依该转移变化的 \(z\in P_S(x)\)，使
   \[
   \|(y-z)-\lambda v\|\le\omega(d(x,S)),\qquad
   d(y,S)\le\psi(\|v\|).
   \tag{AT2}
   \]

最近点存在由非空闭 \(S\) 和有限维性保证。\(z\) 表示零点锚，不沿用 Minty 输入的字母 \(p\)。这里不要求 \(\omega\) 或 \(\psi\) 连续；不要求 \(S\) 是完整零集。

<a id="at-theorem"></a>
## C185-v1 · 所有允许选择的有限长度定理

- **Status**：`derived-checked`；范围为上述共同证书和下列统一收缩、严格留域预算。

置 \(B(t)=(t+\omega(t))/2\)。对每个上述允许步，有

\[
\|x-y\|\le B(d(x,S)),\qquad
d(y,S)\le\psi(B(d(x,S))/\lambda).
\tag{AT3}
\]

另假设存在 \(0<\kappa<1\)，对**全部同一批转移**有 \(d(y,S)\le\kappa d(x,S)\)。该收缩可由 (AT3) 的标量组合验证，也可由同对象的更强原生估计验证。对 \(0\le t<\eta\) 定义允许取 \(+\infty\) 的非减函数 \(H(t)=\sum_{j=0}^\infty B(\kappa^jt)\)。给定 \(x^0\in V_\eta\)，记 \(d_0=d(x^0,S)\)，要求

\[
H(d_0):=\sum_{j=0}^\infty B(\kappa^j d_0)<\infty,
\qquad H(d_0)<d(x^0,X\setminus V).
\tag{AT4}
\]

约定到空集的距离是 \(+\infty\)。则任意逐步选择 \((x^{j+1},v^j)\in\mathcal A(x^j)\) 都能无限继续，并满足

\[
d(x^j,S)\le\kappa^jd_0,\quad
\sum_{j\ge0}\|x^{j+1}-x^j\|\le H(d_0),\quad
x^j\longrightarrow x^\infty\in S\cap V,
\tag{AT5}
\]
\[
\|x^\infty-x^k\|\le H(d(x^k,S))\le H(\kappa^kd_0)
=\sum_{j=k}^\infty B(\kappa^jd_0).
\tag{AT6}
\]

**一步证明。** 由 \(x=y+\lambda v\) 与 (AT2)，
\(2\lambda v=(x-z)-[(y-z)-\lambda v]\)，所以
\(2\lambda\|v\|\le d(x,S)+\omega(d(x,S))\)。再用 \(\psi\) 非减，即得 (AT3)。若 \(d(x,S)=0\)，该式强制 \(v=0,y=x\)，所以全部允许选择在目标上驻定。

**留域归纳。** 初值的 coverage 给第一步。已合法构造至 \(x^k\in V_\eta\) 时，用同一收缩和 \(B\) 非减得到
\(d_{k+1}\le\kappa^{k+1}d_0\) 及 \(\|x^{k+1}-x^k\|\le B(\kappa^kd_0)\)。故
\(\|x^{k+1}-x^0\|\le H(d_0)<d(x^0,X\setminus V)\)，从而 \(x^{k+1}\in V_\eta\)，可再调用 coverage。这样没有先假设整条轨道留域。可和总长给 Cauchy 性；Euclidean 完备性、\(S\) 闭和 \(d_k\to0\) 给极限属于 \(S\)。同一个严格预算使极限仍在 \(V\)。从第 \(k\) 步求和给 (AT6)，右端是已收敛级数的尾，趋零。□

若 \(\psi\) 只定义于 \([0,\zeta)\)，另要求 \(B(d_0)/\lambda<\zeta\)，或给整个使用距离窗上同一门；由于 \(B\) 非减，此门覆盖全部后继评价。不能将定义域外值默认为可用。

<a id="at-power"></a>
## 实际幂半径与两个不同的率

保留 C185 全部选择量词，取 \(0<\gamma<1\)、\(L,K,q>0\)，\(\omega(t)=Lt^\gamma\)、\(\psi(s)=Ks^q\)。则

\[
d_+\le\frac{K}{(2\lambda)^q}d^{\gamma q}(d^{1-\gamma}+L)^q.
\tag{AT7}
\]

当 \(\gamma q\ge1\)，对任意 \(0<r<\eta\) 置
\(\beta(r)=K(2\lambda)^{-q}r^{\gamma q-1}(r^{1-\gamma}+L)^q\)。若 \(\beta(r)<1\)，则全部 \(d\le r\) 的允许步满足 \(d_+\le\beta(r)d\)。因此：

- \(\gamma q>1\) 时存在这样的正半径。
- \(\gamma q=1\) 时存在这样的正半径，当且仅当 \(K(L/(2\lambda))^q<1\)；实际选定半径仍须检查 \(\beta(r)<1\)。
- \(\gamma q<1\) 时这组上界的比值随 \(d\downarrow0\) 发散，因而本标量上界不能认证统一严格收缩；不能据此判定实际算法发散。

这里的实际半径证书只控制 \(d\le r\)，不控制全部 \(V_\eta\)。应用时要求 \(d_0\le r\)，选 \(\beta(r)\le\kappa<1\)，并核相同严格预算；C185 的逐步归纳限制在 \(V\cap\{d(\cdot,S)\le r\}\) 即可，因为收缩使每个后继继续满足该距离窗。不能仅凭 \(\beta(r)<1\) 宣称原来更大距离窗内的统一收缩。

给定合法 \(0<\kappa<1\)，预算为
\[
H(t)=\frac12\left(\frac{t}{1-\kappa}
+\frac{Lt^\gamma}{1-\kappa^\gamma}\right).
\tag{AT8}
\]
距离有 Q 因子上界 \(\kappa\)；点误差由 (AT6)/(AT8) 得 R 因子上界 \(\kappa^\gamma\)。不能把点误差的 R 上界改称 Q 因子。\(\gamma=1\) 的正确常数须保留 \(1+L\)，见 [C54 的独立端点](named_branch_local.md#nb-power)。本页不重述旧来源“分母 2 锐”而略去其可达见证。

<a id="at-boundaries"></a>
## 与完整图、真残差及旧自然类的接口边界

完整真 EB \(d(y,S)\le\psi(r_F(y))\) 在其评价域内可推出 (AT2) 的所选值 EB。反向必须先保证该界控制**全部完整纤维图值**，才可使用残差取到或 gauge 在真残差处右连续的门，见 [C166](operator_profile_tools.md#op-profile)；也可明确给出满足该界、范数趋近真残差的允许值序列并核右连续，或直接给出允许的范数极小值。只对允许子纤维成立时，完整纤维另处取到残差并不够。

更强的完整闭图反例满足 C185 的全部假设：在 \(\mathbb R\) 取 \(\lambda=1\)、\(F(y)=\{y,3y\}\)、\(S=\{0\}\)、\(V=\mathbb R\)、\(\eta=1\)，只允许 \(\mathcal A(x)=\{(x/4,3x/4)\}\)。取 \(\omega(t)=t/2\)、\(\psi(s)=s/3\)、\(\kappa=1/4\)。零锚估计与所选值 EB 都取等，coverage 全域成立，\(B(t)=3t/4\)、\(H(t)=t\)，严格留域自动成立。可是完整真残差取到为 \(r_F(y)=|y|\)，所以每个 \(y\ne0\) 都有 \(d(y,S)>\psi(r_F(y))\)，尽管 gauge 连续。这只反驳省略全纤维量词的逆向接口，不反驳 C185 的所选值定理。

同图块全对模若能与该转移的最近零图点比较，可供应 (AT2) 的锚估计；只控制存在一个好分支不供应全部允许转移的估计。要转给完整 \(J_{\lambda F}\) 的任意选择，必须令 \(\mathcal A(x)\) 包含相关输入的**全部**完整近端输出，且所有前件逐选择成立。C185 不整体验收原稿 C02 的其他版本，也不提供原生 coverage 或纤维排他。

源稿 §4 的“自然屈服集”没有在该来源就地定义完整 \(F\)、normal inverse 与参数化 prox。现已另从支撑函数/法锥来源恢复[C191的完整原图与参数化prox](support_normal_natural_class.md#sn-triangular)：同一数据的 \(L_\delta,K\)、全域coverage、同尺度严格匹配、非零C的最佳指数及带 \(\tau\ge0\) 门的圆盘解析轨道都有独立推导。C192另处理反馈条带及全域多值边界。这些实例经明定原图接入C185；旧章节编号或历史审查身份不因公式匹配而自动核定。输入对尺度 \(\delta\) 与状态到目标的距离半径 \(r\) 是不同量；当使用半径 \(r\) 整球的全部点对时，对距上界为 \(2r\)。

来源完整范围、具体 deferred 与证据层见 [核心终审全文去向](../audit/CORE_TRANSITIONS_FULL_COVERAGE.md#at-source)。正文证明仅使用显示的条件、三角不等式、级数与 Euclidean 完备性，不依赖历史稿补步骤；外部新颖性未核。
