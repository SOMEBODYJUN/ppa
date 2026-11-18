# RL–KL 目标二：三席独立审查与收口

## 最终裁决

本轮只审查目标二：能否把 LMZ/Zhu 的 KL 有限长度机制接到 PPA/RL。三席独立复核得到同一结论：

| 对象 | 状态 | 精确结论 |
| --- | --- | --- |
| exact subgradient PPA | `derived-checked` | 在 LMZ v1 的 H3、有限次水平、聚点 KL 和 H11/H2 条件下，不需传统 metric subregularity 即得有限长度和整列收敛。 |
| 抽象 RL–KL transfer corollary | `derived-checked`（条件式） | 若同一状态空间已有 Lyapunov \(E\)、H11、真实相对误差、H3、KL、level boundedness 和物理步兼容，则可直接调用 LMZ。 |
| 一般非单调 RLEB/GPPA 自动桥 | `refuted`（RL alone） | 90 度旋转 full-graph 例子满足 RL 但有四周期，排除正耗散 Lyapunov；弱于旧 RL+GMSR 的替代条件仍 open。 |

## 已核对的关键公式

固定步长 exact PPA 取

\[
 e_k=\|x^{k+1}-x^k\|,\quad a=\frac1{2\lambda},\quad \phi(t)=t^2,\quad b=\frac1\lambda,\quad \beta(t)=t.
\]

近端下降和 Fermat 条件给出 H11/H2。KL 望远镜差

\[
\Lambda_{k,k+1}=\vartheta(f_k-f_*)-\vartheta(f_{k+1}-f_*)
\]

满足

\[
\Lambda_{k,k+1}\ge\frac{e_k^2}{2e_{k-1}}.
\]

直接 AM–GM 给

\[
 e_k\le\frac{e_{k-1}+\Lambda_{k,k+1}}{\sqrt2}.
\]

若使用 LMZ 的混合门，\(\sqrt{st}\le(s+t)/2\) 在代入 \(t=2\Lambda\) 后给的是 \(e_k\le e_{k-1}/2+\Lambda\)；两条递推不能混写。

## RL–Lyapunov 阻塞

在 \(H=\mathbb R^2\) 取 90 度旋转 \(Q\)，令 \(F(u)=Q^\top u-u\)、\(\lambda=1\)。则 \(J_F=Q\) 全域单值，完整图满足全局 \(\mathrm{RL}(1,1,\sqrt5)\)，而非零轨道 \(x^{k+1}=Qx^k\) 是四周期。任何满足

\[
E(Jx)+a\phi(\|Jx-x\|)\le E(x),
\qquad a>0,\quad \phi(t)>0\ (t>0),
\]

的状态 Lyapunov 函数都会在四周期求和时矛盾。因此 RL alone 不推出 Lyapunov/H11/H2。

## A+B 边界

若同一轨道满足

\[
d_{k+1}\le\kappa d_k,\quad 0\le\kappa<1,qquad \|x^{k+1}-x^k\|\le B d_{k+1},
\]

则

\[
\sum_{k=0}^\infty\|x^{k+1}-x^k\|\le\frac{B\kappa}{1-\kappa}d_0<\infty.
\]

所以 A+B 已经完成旧的绝对步长求和证明，KL 在此不是必要机制；B 单独不能求和。

## 纠正与范围

原报告中的交替点反例不满足 LMZ H1 的 \(e_k\to0\)，已替换为单位圆轨道 \(e_k\sim1/k\)、\(\sum e_k=\infty\) 的 KL-only 反例。它不是 exact PPA 轨道；失败点是 H11 正步长耗散。

本轮没有削弱一般 RL 的 MSR/GMSR，也没有改进 B。实际完成的是 exact subgradient PPA 的 KL 充分条件、条件式 transfer corollary，以及 RL-alone 桥的精确阻塞。下一步必须寻找严格介于旧 RL+GMSR 与纯 RL 之间的自然性质，推出 A+B 或真正的能量望远镜替代条件。
