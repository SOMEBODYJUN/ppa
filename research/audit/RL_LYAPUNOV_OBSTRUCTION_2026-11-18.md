# RL 到 Lyapunov 桥：精确阻塞与 A+B 边界

## 结论

本审查区分三个命题：

1. `RL alone => Lyapunov/H11/H2`：**refuted**。
2. `A+B => 有限长度`：**derived-checked**。
3. `RL+(A+B) => KL 新收敛机制`：KL 对收敛不是必要的，主要是事后重包装。

## RL alone 的 full-graph 反例

在 \(H=\mathbb R^2\) 取 90 度旋转 \(Q\)，令

\[
F(u)=Q^\top u-u,
\qquad \lambda=1.
\]

则

\[
I+F=Q^\top,
\qquad J_F=Q.
\]

因此完整 resolvent 全域单值，且每个 \(x^0\ne0\) 的轨道

\[
x^{k+1}=Qx^k
\]

是四周期，长度发散。

对任意图点差 \(h\)，

\[
\Delta u+\Delta v=Q^\top h,
\qquad
\Delta u-\Delta v=(2I-Q^\top)h.
\]

所以完整图满足全局 \(\mathrm{RL}(1,1,\sqrt5)\)。但任何满足

\[
E(Jx)+a\phi(\|Jx-x\|)\le E(x),
\qquad a>0,
\quad \phi(t)>0\ (t>0),
\]

的单值状态 Lyapunov 函数都不可能存在：沿四周期相加会得到

\[
E(x^0)+4a\phi(\|Qx^0-x^0\|)\le E(x^0),
\]

矛盾。

这不是某个候选 \(E\) 失败，而是任何具有正步长耗散的状态函数都被周期轨道排除。该 \(F\) 也不是标量次梯度图。

## A+B 已经足够

若同一轨道满足

\[
d_{k+1}\le\kappa d_k,qquad 0\le\kappa<1,
\]

以及

\[
\|x^{k+1}-x^k\|\le B d_{k+1},
\]

则

\[
\|x^{k+1}-x^k\|\le B\kappa^{k+1}d_0,
\]

从而

\[
\sum_{k=0}^\infty\|x^{k+1}-x^k\|
\le \frac{B\kappa}{1-\kappa}d_0<\infty.
\]

在完备空间中轨道收敛；若 \(S\) 闭且 \(d_k\to0\)，极限属于 \(S\)。因此 A+B 已经完成旧的绝对步长求和证明，KL 桥并没有增加收敛结论。

B 单独不够，A 单独也不够：B 只给单步相对控制，A 才提供可和的距离尾；A 在非孤立解集上还可能允许沿 \(S\) 漂移。

## 对本轮工作的裁决

本轮没有削弱一般 RL 的 MSR/GMSR，也没有改进 B。实际完成的是：

- exact subgradient PPA 的 KL 有限长度充分条件，不使用传统 MSR；
- 一个带 Lyapunov/H11/H2/H3 假设的条件式 transfer corollary；
- RL-alone 不自动产生该桥的 full-graph 反例；
- A+B 已足够，因此 KL 不能被用来宣称已经改进 B。

下一步的真正目标是寻找一个自然性质 \(\mathcal P\)，满足

\[
\mathcal P\quad\text{弱于旧 RL+GMSR，且强于纯 RL，}
\]

并推出 A+B 或一个真正可望远镜的替代条件。
