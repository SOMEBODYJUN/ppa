# 从全对图块到指定分支：零锚保距离的门

这条桥从历史 foundations §3.1 重写，接入 [C53](named_branch_local.md#nb-local) 的 B/A 接口。它只制造指定图块的分支和锚条件；实际输出的真残差 EB、兼容和留域仍是独立前提。

<a id="av-object"></a>
## AV-OBJECT · 图块与两种零集

实 Hilbert 空间 \(H\)，\(F:H\rightrightarrows H\)，\(S=F^{-1}(0)\ne\varnothing\)，\(\lambda>0\)。取 \(G\subset\operatorname{gph}F\)，固定 \(L\ge0,0<\gamma\le1\)，假设对**所有** \(z=(u,v),z'=(u',v')\in G\)

\[
 \|(u-u')-\lambda(v-v')\|
 \le L\|(u-u')+\lambda(v-v')\|^\gamma. \tag{AV-1}
\]

记 \(D=M_+(G)\)、\(S_G=\{p\in S:(p,0)\in G\}\)。给定 \(U\subset D\) 与 active set \(A\subset U\)，要求

\[
 d(x,S_G)=d(x,S)<\infty\quad\text{对每个 }x\in A. \tag{AV-2}
\]

这里 (AV-2) 只在所需输入族上保**距离**，不要求 \(S_G=S\)；但 \(S_G\) 对该族必须非空。若目标是 C53，则须取 \(U\) 为相应开球、\(A=A_\delta\)，并保留其中全部零距离输入。

<a id="av-bridge"></a>
## C56-v1 · 全对验证器的精确输出

AV-OBJECT 给图块上唯一的 \(T:U\to H\)，使 \((Tx,(x-Tx)/\lambda)\in G\)。对任意 \(x\in A\)，存在 \(p_n\in S_G\) 使 \(\|x-p_n\|\to d(x,S)\)，且

\[
 \|2Tx-x-p_n\|\le L\|x-p_n\|^\gamma\quad\text{对所有 }n. \tag{AV-3}
\]

此外，对任意 \(x,y\in U\)，\(\|(2T-I)x-(2T-I)y\|\le L\|x-y\|^\gamma\)。

**证明。** 若两图点有同一个 Minty 输入，则 (AV-1) 使两个 Cayley 输出相同，剪切的逆公式给图点相同；故 \(M_+|_G\) 单射。\(U\subset D\) 给每个输入的存在性，因而定义 \(T\)。由 (AV-2) 的 infimum 定义取 \(p_n\in S_G\) 接近距离；不需最近点取到。比较 \((Tx,(x-Tx)/\lambda)\) 与 \((p_n,0)\) 得 (AV-3)；比较两个任意输入图点得最后的全对模。□

要调用 C53，还需对**同一实际输出**核真实 \(r_F(Tx)\) 的残差窗口 EB、标量兼容和留域。即使 \(G\) 内单值，完整 \(J_{\lambda F}\) 在 \(U\) 上可能有额外输出；若要唯一完整步，另证 \(\{z\in\operatorname{gph}F:M_+(z)\in U\}\subset G\)。以上每个范围均不能由 (AV-1) 单独推出。

<a id="av-gap"></a>
## C57-v1 · 零锚距离等式不能由全对与 coverage 删除

取 \(H=\mathbb R,\lambda=1\)，完整关系 \(F(y)=\{0,y\}\) 对所有 \(y\in\mathbb R\)，故 \(S=\mathbb R\)。取图块 \(G=\{(y,y):y\in\mathbb R\}\)。其自然输入域 \(D=\mathbb R\)，图块反射恒为零，因而 (AV-1) 对任意 \(0<\gamma\le1\) 以 \(L=0\) 成立。图块唯一分支为 \(T(x)=x/2\)，而 \(S_G=\{0\}\)，所以对 \(x\ne0\)，

\[
 d(x,S_G)=|x|>0=d(x,S).
\]

任取包含非零点的开输入族，其点 \(x\in S\) 却有 \(Tx\ne x\)；C53 的零距离锚定 A 在这些点不成立。完整 resolvent 同时有 \(x\)（来自零图值）与 \(x/2\)（来自 \(G\)），说明完整步的排他门也未满足；这是**另一个**条件缺口。本例的真实输出残差为零、到 \(S\) 距离也为零，故加上 E 仍修不回 A。此反例不否定 C56，因为它明确违反 (AV-2)。

**来源与证据。** 旧历史稿 RL_foundations.md §3.1 的条件桥经上面的单射、近似 infimum 与图对比较重算；C57 是本次给出的完整关系反例。它只判定零锚保距离的必要性相对于此证明接口，不宣称 (AV-2) 是任何收敛定理的普遍必要条件，也未核文献先行性。
