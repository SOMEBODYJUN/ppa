# 下一轮 GPT Pro 主研究任务：先闭合 RL–KL，再寻找中间结构性质

## 任务背景

当前 PPA 项目有三个方向。前一轮已经确认：

- 仅有函数复合距离收缩不能自动给有限长度，必须同时控制步长尾；
- LMZ/Zhu 的 KL 框架在 exact subgradient PPA 中可以替代传统 metric subregularity 的一个有限长度接口；
- 目标三的重点不是证明旧假设推出 (A)+(B)，而是寻找满足 (A)+(B) 或其 KL 改进版、同时脱离传统次单调性或传统 MSR 的严格扩张结构。

必须区分：完整图/full resolvent、允许子关系/固定选择策略、局部工作域、真实完整残差和所选图值。

## 总优先级

优先完成目标二。目标一只作为技术基础，目标三在目标二形成新的有限长度接口后再推进。

---

## 目标二：构造 RL–KL 有限长度转接引理

### 精确问题

从 Li–Mordukhovich–Zhu arXiv v1 的 Theorems 4.3–5.1 出发，研究是否能把传统的绝对步长求和

\[
\sum_k \|x^{k+1}-x^k\|<\infty
\]

替换为 KL 能量差的望远镜控制，从而在不依赖传统 metric subregularity、也不依赖固定几何步长包络的情况下证明有限长度。

### 必须逐项重构的 LMZ 接口

固定 exact PPA 或允许 PPA 轨道，逐项核对：

- H0：下降；
- H1/H1'：步长 surrogate 与充分下降；
- H2：相对误差；
- H3：聚点子序列的函数值上半连续；
- bounded level set；
- 聚点存在；
- KL 不等式；
- \(\varphi^{-1}(\beta(s)t)\) 的混合条件。

标准 exact subgradient PPA 的基准映射为

\[
e_k=\|x^{k+1}-x^k\|,
\quad a=\frac1{2\lambda},
\quad \varphi(t)=t^2,
\quad \beta(t)=t,
\quad b=\frac1\lambda.
\]

必须重构

\[
\Lambda_{k,k+1}
\ge \frac{e_k^2}{2e_{k-1}},
\qquad
 e_k\le \frac{e_{k-1}+\Lambda_{k,k+1}}{\sqrt2},
\]

并证明望远镜求和给出有限长度。

### RL 到 KL 的关键桥

不能直接把任意 \(F\) 当成 \(\partial f\)。必须研究一个明确的 Lyapunov/能量函数 \(E\)，并验证：

\[
E(x^{k+1})+a\,\varphi(e_k)\le E(x^k),
\]

以及某个真实的相对误差对象

\[
\xi_{k+1}\in\mathcal R_E(x^{k+1}),
\qquad
\|\xi_{k+1}\|\le b\,\beta(e_k).
\]

同时验证 H3、level-set、聚点、KL 和目标集合身份。

原证明中出现的

\[
2\sigma\|x^{k+1}-x^k\|
\]

不能直接删掉。必须证明它：

1. 被扩充 Lyapunov 函数吸收；或
2. 被下降余量吸收；或
3. 被改写成可望远镜的能量差。

### 目标二的输出

必须给出一个明确的 RL–KL theorem candidate，分成：

- exact subgradient PPA 的已闭条件版；
- 一般非单调 PPA 的所需额外桥；
- GPPA 的核空间/物理空间对象分离；
- 所有未闭 proof obligations；
- 至少一个说明 KL alone 不够的反例。

如果无法从 RL 结构推出 Lyapunov/relative-error 桥，必须明确停止，不得把 exact subgradient 结果冒充一般 PPA 结果。

---

## 目标一：为目标二提供非线性距离接口

保留并继续完善一般函数复合递推

\[
d_{k+1}\le \varphi(d_k),
\qquad
s_k\le B(d_k).
\]

必须区分：

- \(\varphi^{\circ k}(t)\to0\)；
- \(\sum_k B(\varphi^{\circ k}(t))<\infty\)；
- 物理有限长度；
- 点列收敛。

继续保留 \(F(y)=y|y|\) 的完整 PPA 例作为固定 \(\kappa\) 和线性 MSR 都失败、但实际步长望远镜可和的正面模型。不要把粗 RLEB 步长上界和实际步长混为一谈。

---

## 目标三：寻找严格介于旧理论和新有限长度接口之间的结构性质

### 正确研究目标

不是证明

\[
\text{旧 RL 次单调性+MSR}\Rightarrow(A)+(B).
\]

真正目标是寻找一个独立可验证的结构性质 \(\mathcal P\)，使它在明确量词下：

- 能产生 (A)+(B)，或产生它们的 KL/望远镜改进版；
- 不需要完整传统次单调性，或者不需要传统 MSR；
- 不是把 (A)+(B) 原样重新命名；
- 可以由自然算子/图几何/Lyapunov 结构验证；
- 严格覆盖旧理论无法覆盖的例子。

### 已有严格扩张基准

完整 full-graph/full-resolvent 的基准例为

\[
G(y)=\frac32(y+\sin y),
\qquad
F(y)=G(y)-y,
\qquad
J_F=G^{-1},
\qquad
S=\{0\}.
\]

它满足全局 (A)+(B)，但不存在有限 Luke–Tam 型传统次单调性 violation 常数。这个例子证明：

\[
(A)+(B)\quad\text{可以脱离传统次单调性}.
\]

它仍满足线性 MSR；完整图的 (A) 自动推出线性 MSR，因此不应声称它同时脱离完整 MSR。

允许子关系的基准例 \(F(y)=\{y,y^2\}\) 只选 \(w=y\) 的分支，可以得到 (A)+(B) 但完整真残差不满足 MSR；必须明确这是选择策略/允许子关系性质，不能升级成完整 resolvent 结论。

### 优先研究的候选

1. **KL–telescoping transport**：
   \[
   \|x-y\|
   \le C\bigl(\Theta(E(x))-Theta(E(y))\bigr)
   \]
   或
   \[
   \|x-y\|
   \le C\bigl(d(x,S)^\alpha-d(y,S)^\alpha\bigr).
   \]
   它直接给有限长度，并可能比 (B) 更适合 KL 望远镜。

2. **锚定扇区—相对平静性**：共同最近锚、正扇区和选中图值 calmness。必须证明它来自自然算子类，而不是人为包装。

3. **统一中间性质**：在目标二闭合 RL–KL 桥后，寻找一个弱于完整旧 RL+MSR、强于纯距离接口的结构条件，并明确旧条件如何导入它、它如何导出新的有限长度接口。

### 必须严格区分的量词

- full graph vs selected subrelation；
- all resolvent outputs vs one policy；
- local coverage vs global coverage；
- true residual inf over full fiber vs selected residual；
- distance convergence vs point convergence；
- absolute summability vs telescoping summability。

---

## 最终交付标准

本轮只接受以下状态标签：

- derived-checked：证明和量词已闭；
- candidate：结构固定但自然验证/桥仍未闭；
- refuted：某个精确版本有反例；
- open：尚缺关键 proof obligation。

不得把：

- exact subgradient KL 结果写成一般非单调 PPA 定理；
- selected-subrelation 严格扩张写成 full-graph 结果；
- PTD 写成 (A)+(B)；
- KL-only 写成有限长度；
- 一条反例误读为整个目标三失败。

优先交付目标二的 RL–KL transfer theorem candidate；目标三只在该桥明确后再提出统一中间性质。
