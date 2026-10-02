# σ-紧度量空间的 Baire 诊断

<a id="sc-object"></a>
## C128：对象与等价式

令 \(Z\) 为度量空间，\(Z=\bigcup_{n\ge1}K_n\)，各 \(K_n\subset Z\) 紧；不要求 \(K_n\) 递增。记

\[
D=\bigcup_{n\ge1}\operatorname{Int}_ZK_n.
\tag{SC1}
\]

则

\[
Z\text{ 是 Baire 空间}\quad\Longleftrightarrow\quad
D\text{ 在 }Z\text{ 稠密}.
\tag{SC2}
\]

这里 Baire 指每列稠密开集的交仍稠密；这是**给定 σ-紧度量空间的拓扑测试**，没有判定任何 RLEB、LT 或极大单调算子类的具体空间满足哪一侧。

<a id="sc-proof"></a>
## 双向证明

度量空间 Hausdorff，所以每个紧 \(K_n\) 在 \(Z\) 中闭。若 \(Z\) 为 Baire 而 \(D\) 不稠密，取非空开 \(U\subset Z\) 与 \(\overline D\) 不交。每个 \(K_n\cap U\) 在 \(U\) 内闭且内点为空；它们可数覆盖 \(U\)。但 Baire 空间的开子空间仍为 Baire，故非空 \(U\) 不可能是可数个无处稠密闭集的并，矛盾。

反向，\(D\) 是开且稠密的局部紧 Hausdorff 空间：任取 \(z\in\operatorname{Int}_ZK_n\)，在 \(Z\) 中取足够小的开球，使其闭包位于 \(\operatorname{Int}_ZK_n\)；其闭包是 \(K_n\) 的闭子集，故紧。局部紧 Hausdorff 空间为 Baire。为明确从 \(D\) 传回 \(Z\) 的量词，若 \(G_j\subset Z\) 是任意可数列稠密开集，则 \(G_j\cap D\) 在 \(D\) 中也稠密开；其交在 \(D\) 中稠密。因此 \(Z\) 的每个非空开 \(U\) 都与 \(D\cap\bigcap_jG_j\) 相交，\(\bigcap_jG_j\) 在 \(Z\) 中稠密。

<a id="sc-scope"></a>
## 适用边界

各 \(K_n\) 的内点并不必包含全部局部紧点：\(Z=[0,1]\)，\(K_1=[0,1/2]\)、\(K_2=[1/2,1]\) 时 \(1/2\) 局部紧，却不属于两个 \(K_n\) 任一个的 \(Z\)-内部。若只知道某研究对象空间“有紧层”，必须先证明**这些层的并覆盖同一个 \(Z\)**，并检查内点是否稠密；(SC2) 本身不提供保纲观测、完整算子空间的紧层或目标类的总体规模比较。历史审计对应的证明只作溯源，本页的定义和推导可独立使用。
