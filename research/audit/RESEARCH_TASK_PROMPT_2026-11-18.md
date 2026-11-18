# GPT Pro 主研究任务：RL 基础下严格弱化 GMSR，并连接到收敛接口

## 先固定正确的问题

本任务始终在已有 RL 条件下进行。RL 是算法/图几何基线，不是要寻找的正则性，也不是 KL 的替代品。不要研究“RL alone 能否推出 Lyapunov”；这个问题已经有周期轨道反例，不能作为本轮主结果。

旧理论中的 GMSR 是正则性条件。现在要研究的是：能否找到一个有独立数学意义、可由自然算子或图几何验证的正则性 \(\mathcal R\)，满足

\[
\mathrm{GMSR}\Longrightarrow \mathcal R,
\]

并且存在同一对象类别、同一量词口径下的严格例子

\[
\mathcal R\quad\text{成立，但}\quad \mathrm{GMSR}\quad\text{失败}.
\]

然后再寻找一个独立的兼容条件 \(\mathcal C\)，使得在 RL 下

\[
\mathrm{RL}+\mathcal R+\mathcal C
\Longrightarrow (A)+(B),
\]

或者在目标二的 KL 机制闭合后，推出能够替代点态 \(B\) 的能量望远镜接口。

这里必须分开比较：

- **严格弱于 GMSR 的是正则性组件 \(\mathcal R\)**；
- **整体充分条件 \(\mathcal R+\mathcal C\)** 可能因为加入 \(\mathcal C\) 而比 GMSR 更强，不能把整体条件说成弱于 GMSR；
- \(A+B\) 是收敛接口，不要把它当成一个自动弱于 GMSR 的正则性。

特别地，对 full graph，如果 \(A\) 对所有图点和所有输出全局成立，在输入 coverage、步长和图点关系适用时，\(A\) 本身可能推出线性 metric subregularity。因此必须明确：严格弱化应发生在 \(\mathcal R\) 与 GMSR 的比较上；若使用局部、轨道限制或 selected relation，必须把范围写清楚，不能升级成 full-graph 结论。

## 我们之前的理解偏差，必须在报告开头说明

之前出现过以下误读，不能重犯：

1. 把任务误读成证明“RL + 旧 GMSR \(\Rightarrow A+B\)”；真正目标是寻找新的 \(\mathcal R\) 和独立 \(\mathcal C\)，并证明它们在 RL 下连接到 \(A+B\) 或 KL 接口。
2. 把 RL alone 当成与 KL 同类的正则性；RL 只是基线，\(\mathcal R\) 才是待弱化的正则性。
3. 把 exact subgradient PPA 的 KL 定理扩大成一般非单调 RL/GPPA 定理。
4. 把“换一种有限长度证明机制”说成“已经削弱了 MSR”。只有证明 \(\mathrm{GMSR}\Rightarrow\mathcal R\)、并给出 \(\mathcal R\wedge\neg\mathrm{GMSR}\) 的严格例，才能声称正则性组件被严格弱化。
5. 把“旧条件不能推出 \(B\)”的反例当成“满足新接口但脱离 GMSR”的严格扩张例。两者回答的是不同问题。
6. 混淆 full graph 与 selected subrelation、完整真残差与选择残差、局部结论与全局结论。
7. 把“拆掉绝对值”理解成删除有限长度结论。有限长度结论仍是
   \[
   \sum_k\|x^{k+1}-x^k\|<\infty.
   \]
   KL 路线真正可能改进的是：不再直接假设点态的 \(B\)，而用能量差支付步长。

已有的 RL-alone 四周期反例只说明 RL 不能自动产生耗散 Lyapunov；它不是本任务的正面结果。已有的

\[
G(y)=\tfrac32(y+\sin y),\qquad F(y)=G(y)-y
\]

例子说明 full-graph 的 \(A+B\) 可以脱离传统次单调性，但它仍有线性 MSR，因此也不能冒充 \(\mathcal R<\mathrm{GMSR}\) 的严格弱化例。

## 精确研究对象

先读取当前仓库的 README.md、RESEARCH_STATE.md、CLAIMS.md、FAILED_ROUTES.md，以及 RL、GMSR、目标二 KL 相关规范文件。只使用规范文件中的定义，不从历史聊天补定义。

在开始证明前，逐字固定以下对象：

- 空间、算子/图、零集 \(S\)、步长和迭代格式；
- 图块还是完整图；full resolvent 还是 selected relation；
- 全局还是局部工作域；
- 所有量词、常数和输入 coverage；
- 残差是完整真残差还是选择残差；
- 距离收缩的输出量词，以及步长控制的输出量词。

对同一份固定对象，分别定义：

\[
\tag{A} d(y,S)\le \kappa d(x,S),\qquad 0\le\kappa<1,
\]

\[
\tag{B} \|x-y\|\le B_0 d(y,S).
\]

若研究 selected relation，必须把选择映射、允许的输出和选择残差单独写出；不能用选择关系的结论替代完整图结论。

## 目标二提供的改进接口

目标二的 exact subgradient PPA KL 结果可以作为已核对的基准，但不能自动推广到一般 RL/GPPA。对一般对象，只有在明确构造并验证 Lyapunov 函数 \(E\)、下降条件、真实相对误差、H3、聚点和 KL 条件后，才可使用 KL 望远镜。

研究一个真正替代点态 \(B\) 的接口，例如证明某个明确版本的

\[
s_k\le \rho s_{k-1}+C\,\Delta\Theta_k,
\qquad 0\le\rho<1,
\]

其中 \(s_k=\|x^{k+1}-x^k\|\)，\(\Delta\Theta_k\ge0\) 是可望远镜的能量差。然后由

\[
\sum_k\Delta\Theta_k<\infty
\]

推出 \(\sum_k s_k<\infty\)。如果仍然证明原始点态 \(B\)，也必须说明 KL 机制没有因此自动变成更弱假设。

原证明中出现的 \(2\sigma\|x^{k+1}-x^k\|\) 不能凭空删除。必须证明它被扩充能量吸收、被下降余量吸收，或被改写为可望远镜的能量差；否则报告为未闭 proof obligation。

## 对每个候选正则性 \(\mathcal R\) 的强制验收

对每个候选，只保留以下完整链条：

1. **正式定义**：对象、定义域、局部/全局范围、全部量词和常数。
2. **弱化证明**：在同一口径下证明 \(\mathrm{GMSR}\Rightarrow\mathcal R\)。
3. **严格例**：构造同一对象类别中 \(\mathcal R\wedge\neg\mathrm{GMSR}\) 的例子，并逐项验证；不能只证明脱离次单调性。
4. **独立兼容条件**：定义 \(\mathcal C\)，解释其算子、图几何或能量意义；禁止把 \(\mathcal C\) 偷换成 GMSR、\(A+B\) 或 KL 结论的同义改写。
5. **连接证明**：逐步证明
   \[
   \mathrm{RL}+\mathcal R+\mathcal C\Rightarrow A+B,
   \]
   或证明它推出严格定义的 KL 望远镜接口。若只能得到轨道级、局部级或 selected-relation 版本，必须按原范围报告。
6. **必要性攻击**：分别去掉 RL、\(\mathcal R\) 或 \(\mathcal C\)，构造反例或说明尚未能构造；检查退化、非孤立解集、非凸、非单值和周期情况。
7. **边界审查**：核对 full graph/selected relation、完整/选择残差、局部/全局、距离收敛/点列收敛、绝对可和/能量望远镜的区别。
8. **MSR 边界**：检查全图版的 \(A\) 是否自动推出线性 MSR；若是，不能把该版本说成严格弱于 full-graph MSR，应改报局部/轨道/选择版本或记录 obstruction。

候选 \(\mathcal R\) 不得直接定义成 \(A+B\)、KL 望远镜接口或它们的符号改写。必须说明它为何是可独立验证的正则性，而不是把目标结论包装成假设。

## 最终交付格式

只提交一个最有希望的候选主路线；不要并列堆积许多未经验证的猜想。报告必须包含：

- Exact Statement：Objects、Domain、Quantifiers、Assumptions、Definitions、Conclusion；
- \(\mathrm{GMSR}\)、\(\mathcal R\)、\(\mathcal C\)、RL、(A)、(B) 和 KL 接口的依赖图；
- \(\mathrm{GMSR}\Rightarrow\mathcal R\) 的证明；
- \(\mathcal R\wedge\neg\mathrm{GMSR}\) 的严格例及逐项验证；
- \(\mathrm{RL}+\mathcal R+\mathcal C\Rightarrow A+B\) 或 KL 望远镜接口的完整证明；
- 每个额外假设的必要性反例或明确未闭义务；
- full graph / selected relation 的量词表；
- 与旧 RL+GMSR 理论的准确比较：比较的是 \(\mathcal R\)，不是未经证明的整体 \(\mathcal R+\mathcal C\)；
- Truth、Value、Novelty、Mechanism、Ambition、Status 分开判断。

状态只能使用：derived-checked、candidate、refuted、open。如果严格弱于 GMSR 的 \(\mathcal R\) 尚未找到，必须明确写“本轮未完成”，并给出最关键的 obstruction 和最强可成立的修正版；不得把 exact subgradient KL 结果或一个非次梯度 MSR 例子包装成目标完成。
