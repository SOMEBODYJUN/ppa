# 同常数 Hölder 扩张与固定参数 graph-maximal

<a id="he-object"></a>
## HE-OBJECT · 要扩张的精确对象

令 `H,Y` 为实 Hilbert 空间，`D⊂H` 非空，`0<γ<1`，`L≥0`，且 `C:D→Y` 满足

\[
\|C(p)-C(q)\|_Y\le L\|p-q\|_H^\gamma\quad(p,q\in D). \tag{HE1}
\]

**结论**：存在 `Ĉ:H→Y`，在 `D` 上等于 `C`，并对**所有** `p,q∈H` 满足同一个 `L,γ` 的 (HE1)。`γ=1` 直接是 Hilbert 到 Hilbert 的同常数 Lipschitz 扩张；空 `D` 可任取常值，`L=0` 时非空 `D` 上的 `C` 本来是常值。这不是保持一个预先指定的像集、单调性或其他图性质的扩张。

<a id="he-snowflake"></a>
## HE-SNOWFLAKE · Hilbert 雪花的显式正性检查

固定 `o∈H`。对 `0<γ<1`，`r^γ` 有正权 Laplace 表示

\[
r^\gamma=c_\gamma\int_0^\infty(1-e^{-tr})t^{-1-\gamma}\,dt,
\qquad c_\gamma=\frac{\gamma}{\Gamma(1-\gamma)}>0. \tag{HE2}
\]

对任意有限 `x_i∈H` 和实系数 `a_i` 满足 `Σ_i a_i=0`，Gaussian 核 `K_t(x,y)=e^{-t\|x-y\|^2}` 是正定的：把它写为 `e^{-t\|x\|²}e^{-t\|y\|²}Σ_{k≥0}(2t)^k⟨x,y⟩^k/k!`，每项都是张量幂 Gram 核。于是 (HE2) 给

\[
\sum_{i,j}a_i a_j\|x_i-x_j\|^{2\gamma}
=-c_\gamma\int_0^\infty\sum_{i,j}a_i a_jK_t(x_i,x_j)t^{-1-\gamma}\,dt\le0. \tag{HE3}
\]

可先对有限和截断积分，再取极限；近零的 `1−e^{-tr}` 抵消了奇性。故 `d_γ(x,y)^2=\|x-y\|^{2γ}` 是条件负定核。把形式差 `δ_x−δ_o` 的有限线性组合按

\[
\langle\delta_x-\delta_o,\delta_y-\delta_o\rangle
=\tfrac12\bigl(d_\gamma(x,o)^2+d_\gamma(y,o)^2-d_\gamma(x,y)^2\bigr) \tag{HE4}
\]

赋半内积，除去零向量并完备化得 Hilbert 空间 `E` 和 `J:H→E`，使 `\|J(p)-J(q)\|_E=\|p-q\|_H^γ`。这一步不需要 `H` 可分或 `D` 闭。

<a id="he-extension"></a>
## HE-EXTENSION · Kirszbraun 导入与 RL 图的范围

`G:J(D)→Y, G(Jp)=C(p)` 良定且 `L`-Lipschitz。Hilbert 间 Kirszbraun–Valentine 同常数扩张给 `Ĝ:E→Y`；令 `Ĉ=Ĝ∘J` 即得结论。此处的**一手导入**是 [LIT-ALM-2021](../LITERATURE.md#lit-alm-2021) 所列正式出版版 Theorem 1.2，其前提允许任意 Hilbert 源/目标和任意子集；(HE2)–(HE4) 是本页的自足雪花嵌入核验。没有从扩张定理推文献新颖性。

对 [H01](../holder_structure.md#h01) 的特例，取 `Y=H`、固定 `λ>0,L,γ`，`D=M_+(gph F)`，`C(M_+(x,v))=M_-(x,v)`。**全对** RL 使 `C` 在 `D` 上良定并满足 (HE1)。对 `Ĉ` 的 Cayley pullback

\[
\widehat G=\left\{\left(\frac{p+\widehat C(p)}2,
\frac{p-\widehat C(p)}{2\lambda}\right):p\in H\right\} \tag{HE5}
\]

是在**相同** `(λ,γ,L)` 下包含原图的完整图；若 `D≠H`，这是严格扩张。反向若 `D=H`，任一兼容新图点与原图中相同 `p=M_+` 的点比较，输入差为零，全对 RL 迫使 `M_-` 相同，所以无法真扩张。因此固定参数 graph-maximal 当且仅当 `D=H`。

**逻辑边界**：这只定义 RL 类中的 graph-maximal，不声称单调算子意义的 maximal monotone、完整近端轨道收敛或局部输入 coverage；若原条件只在图块或有限输入窗口成立，不能在未证明全局 (HE1) 时调用全域扩张。

**来源和证据状态**：原稿 [S23 `lem:holderextension`](../../history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 给雪花 + Kirszbraun 的证明提示；本页重写正性、同常数扩张和图极大性的量词，`derived-checked`。文献本身仅导入 Hilbert Lipschitz 扩张定理，历史稿其他结构定理仍各有证明义务。
