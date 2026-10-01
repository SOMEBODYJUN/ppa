# 闭图、Minty 自然域与输入覆盖

版本 CG-v1，2026-10-01。这里的对象是**同一图块**，所有结论均针对该图块的自然输入域。结论由 Cayley 坐标独立推导；原稿中的闭性例子只是问题来源，不是证明。

<a id="cg-object"></a>
## CG-OBJECT · 固定对象与局部模

令 \(H\) 为实 Hilbert 空间，\(\lambda>0\)，\(\varnothing\ne G\subset H\times H\)。写

\[
M_+(u,v)=u+\lambda v,\qquad M_-(u,v)=u-\lambda v,\qquad D=M_+(G).
\]

假设存在 \(R>0\) 和有限函数 \(\omega:[0,R)\to[0,\infty)\)，使得

\[
\omega(0)=0,\quad\lim_{t\downarrow0}\omega(t)=0,\quad
\|M_-(z)-M_-(z')\|\le\omega(\|M_+(z)-M_+(z')\|)
\quad(z,z'\in G,\ \|M_+(z)-M_+(z')\|<R).
\tag{CG-1}
\]

全尺度的全对 Hölder–RL \(Lt^\gamma\)（\(L\ge0,\gamma>0\)）满足这些条件；这里只用对角线附近的成对条件，不需要 EB、零集或输入 coverage。

<a id="cg-closure"></a>
## C58-v1 / CG-CLOSURE · 闭图当且仅当自然域闭

**精确结论。** 在 CG-OBJECT 的全部假设下，\(M_+|_G\) 单射，因而有 \(C=M_-\circ(M_+|_G)^{-1}:D\to H\)。它唯一连续延拓为 \(\overline C:\overline D\to H\)，而且

\[
\overline G
=\left\{\left(\frac{x+\overline C(x)}2,
                 \frac{x-\overline C(x)}{2\lambda}\right):x\in\overline D\right\}.
\tag{CG-2}
\]

因此 \(G\) 在 \(H\times H\) 闭 **当且仅当** \(D\) 在 \(H\) 闭。特别地，若 \(G\) 闭且 \(D\) 在 \(H\) 稠密，则 \(D=H\)：这个额外的稠密性与闭性合取是一个满输入覆盖判据。

**证明。** 若两个图点有相同 \(M_+\)，(CG-1) 及 \(\omega(0)=0\) 迫使 \(M_-\) 相同；两个剪切坐标又唯一决定 \((u,v)\)。在 \(D\) 上，(CG-1) 使 \(C\) 在小尺度一致连续。给 \(x\in\overline D\) 和任意 \(x_n\in D,x_n\to x\)，对充分大的 \(m,n\) 有 \(\|x_m-x_n\|<R\)，故 \(C(x_n)\) 为 Cauchy 列。\(H\) 的完备性给极限；交错两条逼近列证明极限与列无关。这定义了 \(\overline C(x)\)，且同样的近对角线估计证明其在 \(\overline D\) 连续。

线性剪切 \(z\mapsto(M_+z,M_-z)\) 有连续逆映射

\[
(x,c)\longmapsto\left((x+c)/2,(x-c)/(2\lambda)\right).
\]

于是 \(G\) 的闭包正是 \(C\) 的图在该逆映射下的像，即 (CG-2)。若 \(G\) 闭，任一 \(x\in\overline D\) 在 (CG-2) 的图点已属 \(G\)，所以 \(x\in D\)。反向若 \(D\) 闭，则 \(C=\overline C\) 连续且 (CG-2) 给 \(G=\overline G\)。稠密与闭性合取立即给 \(D=H\)。□

**模的边界。** (CG-2) 的闭包结论只用 \(\omega(t)\to0\)。若原条件是全尺度 \(Lt^\gamma\)，或全尺度且 \(\omega\) 在每个正 \(t\) 连续，则对逼近的两点取极限，闭包保留同一全对模。一般在正尺度有跳跃的 \(\omega\) 不能仅凭此证明声称闭包保留跳跃点的**同一个**常数；本结论不作该升级。

<a id="cg-boundary"></a>
## CG-BOUNDARY · 哪些条件不能省

1. **闭图不单独给 coverage。** 在 \(H=\mathbb R\) 取 \(K=[0,1]\)、\(G=K\times\{0\}\)。它闭，\(D=K\) 也闭；全对 \(\mathrm{RL}(\lambda,1,1)\) 成立，但没有任何包含 \(0\) 的开输入球被 \(D\) 覆盖。若用任意有界闭真子集 \(K\subsetneq H\)，在直径为 \(\Delta>0\) 时还可取 \(0<\gamma<1\) 及 \(L=\Delta^{1-\gamma}\)。
2. **零点处模消失是承重条件。** 取 \(H=\mathbb R,\lambda=1\)，\(G=\{(t,-t):0<t<1\}\)。其 \(D=\{0\}\) 闭而 \(G\) 不闭；\(M_+|_G\) 非单射，不能定义上面的 \(C\)。任何满足 (CG-1) 的消失模都排除此图块。

对完整关系 \(G=\operatorname{gph}F\)，本定理的 \(D\) 是完整 \(\operatorname{ran}(I+\lambda F)\)；对图块 \(G\subsetneq\operatorname{gph}F\)，它只证明图块输入域闭，不使完整 resolvent 单值或排除图块外纤维。Hilbert 完备性在 Cauchy 极限处使用；不把定理未经证明搬到任意不完备范数空间。

<a id="cg-source"></a>
## 来源、状态与再使用

- 历史来源：[RL_foundations.md §1.1–§1.4](../../history/sources/次单调论文研究/RL_foundations.md) 的剪切恒等式、pullback 与非闭域例；[参数字典 PD-CAYLEY](parameter_dictionary.md#pd-cayley) 固定同一图块的坐标。C58 的闭图—闭域推论是本库的独立推导，并不声称文献新颖。
- 状态：derived-checked，仅为实 Hilbert 空间、CG-1 量词、\(H\times H\) 范数拓扑的内部论证；未查文献先行性。
- 使用时先核 \(G\) 是**所需的完整图还是指定图块**、模在零点消失、图闭性以及 \(D\) 的稠密性。闭图本身不能代替局部输入球 coverage、真实残差 EB 或留域。
