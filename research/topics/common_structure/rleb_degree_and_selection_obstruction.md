# 原 RLEB 的近端输入映射可以有任意局部度

<a id="rleb-degree"></a>
## 全部原根覆盖、非线性模和任意局部度

固定任意 \(\lambda>0\)、\(a>1\)、\(b>0\)、\(0<\gamma<1\)，取 \(R>0\) 使
\[
 (1+1/a)R^{1-\gamma}<b(a^\gamma-1).
\]
在原空间 \(X=\mathbb R^2\times\mathbb R\) 上令 \(S=\{0\}\times\mathbb R\)。任取连续满射 \(h:\mathbb S^1\to\mathbb S^1\)，定义 \(g(0)=0\)、\(g(su)=as h(u)\)（\(s>0,\ u\in\mathbb S^1\)），并以完整单值原算子
\[
 F(y,z)=\lambda^{-1}\bigl(g(y)-y,-b(a\|y\|)^\gamma\bigr)
\]
作检验。它连续，完整零集恰为 \(S\)。其近端输入映射
\[
 P(y,z)=(I+\lambda F)(y,z)=(g(y),z-b(a\|y\|)^\gamma)
\]
在全空间满射。对输入 \((u,w)\)，令 \(t=\|u\|\)。全部合法根 \((y,z)\) 恰满足 \(g(y)=u\)、\(z=w+bt^\gamma\)，因而 \(\|y\|=t/a\)。最近锚是 \((0,w)\)。反射差为 \((2y-u,2bt^\gamma)\)，其范数在 \(2bt^\gamma\) 和 \(\omega(t)=(1+2/a)t+2bt^\gamma\) 之间。

完整真残差满足
\[
 \lambda r_F(y,z)=\sqrt{\|g(y)-y\|^2+b^2a^{2\gamma}\|y\|^{2\gamma}}
 \ge ba^\gamma\|y\|^\gamma.
\]
取 \(\psi(s)=(\lambda s/(ba^\gamma))^{1/\gamma}\)。它对全部原输出给出误差界。令 \(H(t)=(t+\omega(t))/2=(1+1/a)t+bt^\gamma\)、\(\bar t=H(R)/\lambda\)，则在 \(0<t\le R\) 有
\[
 \frac{\psi(H(t)/\lambda)}t
 =\frac1a\left(1+\frac{1+1/a}{b}t^{1-\gamma}\right)^{1/\gamma}
 \le \kappa:=\frac1a\left(1+\frac{1+1/a}{b}R^{1-\gamma}\right)^{1/\gamma}<1 .
\]
级数 \(\sum_{j\ge0}H(\kappa^jR)\) 有限，且 \(U=X\) 没有额外留域预算。因此以全部原根作允许关系时满足原投稿 (P1)–(P4)，认证域包含每个 \(0<\|u\|\le R\) 的初值。作为独立核对，法向半径恰为 \(a^{-k}\|u^0\|\)，切向增量恰为 \(b(a^{-k}\|u^0\|)^\gamma\)，故所有原选择均点收敛。反射模的最佳幂是 \(\gamma\)，因为每个允许反射差都至少为 \(2bt^\gamma\)。误差界的最佳幂是 \(1/\gamma\)，因为 \(\|g(y)-y\|\le(a+1)\|y\|\) 给 \(r_F(y,z)=O(\|y\|^\gamma)\)，而所有 \(0<\|y\|\le R/a\) 都出现在被检输出中。

## 局部度与连续选根

以 \(p=(0,w)\in S\) 作输入，\(P^{-1}(p)=\{p\}\)。局部 Brouwer 度 \(\deg_p(P,p)=\deg h\)。把切向剪切项乘以 \(\theta\in[0,1]\) 的同伦在每个 \(\theta\) 下仍只有原像 \(p\)，因而在任一以 \(p\) 为心的球面上均可归一化并保持度。去掉剪切后再把 \(g\) 中的正系数 \(a\) 同伦到 1，球面上的归一化映射就是 \(h\) 的悬挂。南北半球开覆盖的 Mayer–Vietoris 连接同构将球面上的二阶约化同调对应到赤道上的一阶约化同调，自然性给出悬挂保持度。这里用的是 [Hatcher，第 2.2 节和第 2.2 节末的 Mayer–Vietoris 序列](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf)的标准度与同调性质。法向映射 \(g-I\) 在零点的度也等于 \(\deg h\)，因 \(\|g(y)\|=a\|y\|>\|y\|\)，所以 \(g-\theta I\) 在任意正半径圆上无零点。

在任意 \(p\in S\) 的输入邻域，若存在连续的原根选择，则限制到其中某个小圆 \((tu,w)\) 并将根的非零法向分量归一化，可得连续 \(s:\mathbb S^1\to\mathbb S^1\) 满足 \(h\circ s=\operatorname{Id}\)。度的乘法性遂要求 \(\deg h\in\{-1,1\}\)。特别地，\(h(e^{i\theta})=\exp(i\pi\sin\theta)\) 满射且有周期实提升，因此度为 0。对每个非零整数 \(k\)，取 \(h(e^{i\theta})=e^{ik\theta}\) 实现度 \(k\)。所有这些选择共享前节的 \(\lambda,a,b,\gamma,R,\omega,\psi,\kappa\)。

**范围。** 此构造排除把近端输入映射非零度、规定度或局部连续选根作为完整原 RLEB 必然导入的共同结构。它保留了真正非线性且幂最优的两种模、全局原根覆盖和全域连续原算子。它不排除基于不连续选择、无定向关系或额外假设下的度论。单调和正则的两个恢复仍需另外证明。
