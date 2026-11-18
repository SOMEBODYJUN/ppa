# RL–KL 目标二：三席独立审查与收口

## 最终裁决

本轮只审查目标二：能否把 LMZ/Zhu 的 KL 有限长度机制接到 PPA/RL。三席独立复核得到同一结论：

| 对象 | 状态 | 精确结论 |
| --- | --- | --- |
| exact subgradient PPA | `derived-checked` | 在 LMZ v1 的 H3、有限次水平、聚点 KL 和 H11/H2 条件下，不需传统 metric subregularity 即得有限长度和整列收敛。 |
| 抽象 RL–KL transfer corollary | `derived-checked`（条件式） | 若同一状态空间已有 Lyapunov \(E\)、H11、真实相对误差、H3、KL、level boundedness 和物理步兼容，则可直接调用 LMZ。 |
| 一般非单调 RLEB/GPPA 自动桥 | `candidate/open` | RL 只控制 Cayley 图差分；尚未推出 \(E\)、H11 或真实相对误差，不能声称一般理论已完成。 |

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

## 纠正与反例

原报告中的交替点反例不满足 LMZ H1 的 \(e_k\to0\)，已替换为

\[
f(u,v)=(u^2+v^2-1)^2,\quad
\theta_k=\sum_{j=1}^k\frac1j,\quad
x^k=(\cos\theta_k,\sin\theta_k).
\]

它满足 H0/H1/H2/H3、紧次水平集和 KL，但 \(e_k\sim1/k\)、\(\sum e_k=\infty\)。它是抽象 KL-only 反例，不是 exact PPA 轨道；失败点是 H11 的正步长耗散。

旧估计中的 \(2\sigma\|\Delta x_k\|\) 不能删除。必须证明它被正下降余量吸收、被增广能量修正吸收，或变成可望远镜的能量差。

## 已闭合的非次梯度基准类

若 \(F(x)=Ax\)、\(A=S+K\)、\(S=S^\top\succeq0\)、\(K^\top=-K\)、且 \(A\) 可逆，则完整图满足全局 \(\mathrm{RL}(\lambda,1,1)\)。取 \(E(x)=\frac12\|x\|^2\) 可验证 H11、H2、H3 和 KL，故 LMZ transfer 给出有限长度。\(K\ne0\) 时这不是标量次梯度图；但 \(A\) 可逆已经带来全局线性 metric subregularity，所以这是迁移基准，不是弱于 MSR 的新定理。

## 下一步

只允许一个主义务：选定一个自然的非次梯度 RL 类，直接证明 RL \(\Rightarrow\) 同一 \(E\) 上的 H11、真实 H2、H3 和物理步兼容。未闭合前，保留 `candidate/open`，不把 exact PPA 结果升级为一般 RLEB–PPA 定理。
