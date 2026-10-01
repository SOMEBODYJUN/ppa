# GX-074：紧图、全对 RL 与真 EB 仍无输入覆盖

<a id="dc-object"></a>
## DC-OBJECT · 完整关系及四种域

在 \(H=\mathbb R\) 固定任意 \(\lambda>0\)，令
\[
K=\{0\}\cup\{1/n:n\ge1\},\qquad
F(u)=\begin{cases}\{0\},&u\in K,\\\varnothing,&u\notin K.\end{cases}
\]
这是完整原关系，不是从较大图挑选的支。图 \(K\times\{0\}\) 紧，零集 \(S=K\)，自然 Minty 输入域 \(D_\lambda(F)=K\)。每个 \(x\in K\) 有 \(J_{\lambda F}(x)=\{x\}\)、反射 \(C(x)=x\)；每个 \(x\notin K\) 有 \(J_{\lambda F}(x)=\varnothing\)。虽然 0 是零集的聚点，\(K\) 不包含 0 的任何输入开球。

<a id="dc-gap"></a>
## C47-v1 / DC-GAP · 全对与残差不能补 coverage

对 K 中任意两点 \(x,y\)，输入与反射的差同为 \(|x-y|\le1\)。因此完整图在全部图点对上满足每个 \(0<\gamma\le1\) 的 \(\mathrm{RL}(\lambda,\gamma,1)\)：
\[
|C(x)-C(y)|=|x-y|\le |x-y|^\gamma.
\]
常数 1 在整个 K 上也是最小可用常数，因为 \(x=0,y=1\) 取等。每个图输出 y 的真实残差 \(r_F(y)=0\)，同时 \(d(y,S)=0\)；所以在有限残差输出域上任何取 \(\psi(0)=0\) 的 EB 都成立。域外残差按约定为 \(+\infty\)，不能把域外真空 EB 解释成有 proximal 输出。

然而对任意 \(\varepsilon>0\) 都存在 \(x\in(-\varepsilon,\varepsilon)\setminus K\)，此处没有任何近端步。即使全图紧、完整图全对 RL、真残差 EB 和零集非空闭同时成立，也不能推出 \(B_\varepsilon(0)\subset D_\lambda(F)\)。这是 [局部 PPA](../../rleb_ppa.md) 中输入 coverage 独立性的直接见证；从 K 出发的恒等步也不产生“所有邻近初值”的收敛定理。它不否定已另加 coverage、兼容与留域的局部定理。

<a id="dc-source"></a>
## 来源与范围

从 [9/01 RL_foundations 注 1.5 / GX-074](../../../history/sources/次单调论文研究/RL_foundations.md) 重算，并对照同源 [referee constants 的 GX-074 测试](../../../history/sources/次单调论文研究/RL_foundations_freeze_2026-09-01/work/rl_foundations_referee_constants.md)。历史“fixed-target gauge vacuous”只在目标取完整 \(S=K\) 时可这样理解；若把目标改成 \(\{0\}\)，在 \(1/n\) 处就有 \(r_F=0\) 而距离正，此 EB 立即失败。本卡状态 derived-checked 限于该完整图、量词与阻断方向；不推断别的关系的 coverage。
