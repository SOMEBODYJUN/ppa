# GPT Pro 主研究任务：在 RL 下用 LMSR 加新条件严格弱化 GMSR

普通 PPA 的旧整窗假设与 C315 的严格比较见 [证明和完整图例](../canonical/rleb_residual_filtered_angle.md)。[后续去重](../canonical/rleb_residual_filtered_angle.md#rfa-comparison) 表明 C315 及其见证都可由已有的 C277 联合证书处理。研究目标仍是超出现有联合机制的正则性结论，固定核 GPPA 与独立于原 Dini 假设的 KL 耗散亦未闭合。

## 这次必须研究的唯一问题

当前旧路线是

\[
\mathrm{RL}+\mathrm{GMSR}\Longrightarrow (A)+(B),
\]

其中 RL 是已有的 RL 模次单调/图几何条件，GMSR 是广义度量次正则性，且

\[
\tag{A} d(y,S)\le \kappa d(x,S),\qquad 0\le\kappa<1,
\]

\[
\tag{B} \|x-y\|\le B_0 d(y,S).
\]

旧路线的所有证明都得到 A 和 B。由于在相同 full-graph、coverage、步长和输出量词下可以从 A 推出线性度量次正则性，因此线性 MSR（记为 LMSR）是目标接口的必要条件之一。

本轮不是寻找另一个抽象的“正则性 \(\mathcal R\) 加兼容条件 \(\mathcal C\)”。真正的问题是：

\[
\boxed{
\mathrm{RL}+\mathrm{LMSR}+\mathcal K
\Longrightarrow (A)+(B)
}
\]

或者，在 KL 机制确实闭合时，

\[
\boxed{
\mathrm{RL}+\mathrm{LMSR}+\mathcal K
\Longrightarrow
(A)+B_{\mathrm{KL}},
}
\]

其中 \(B_{\mathrm{KL}}\) 是能量差望远镜接口，能够推出有限长度而不直接假设原始点态 B。

关键要求是：**整体的正则性条件 \(\mathrm{LMSR}+\mathcal K\) 必须严格弱于 GMSR。**

在固定的共同对象类别和共同量词下，必须证明：

\[
\mathrm{GMSR}\Longrightarrow
(\mathrm{LMSR}\land\mathcal K),
\]

并构造严格例：

\[
\mathrm{LMSR}\land\mathcal K
\quad\text{成立，但}\quad
\mathrm{GMSR}\quad\text{失败}.
\]

因此，不能再把“只有 \(\mathcal K\) 弱于 GMSR、但加上额外条件后整体可能更强”作为结论。**本任务比较的是整个新正则性包 \(\mathrm{LMSR}+\mathcal K\) 与 GMSR。**

如果 GMSR 并不推出所选的 \(\mathcal K\)，就不能声称新包弱于 GMSR；必须换候选 \(\mathcal K\)、限制并明确共同的环境类别，或报告该路线失败。

## KL 在这里可能承担什么角色

KL 不是自动替代 GMSR 的口号。要检查它是否能在某个明确的环境类别下，作为 \(\mathcal K\) 的一部分，补足 LMSR 不能提供的收敛机制。

需要严格区分：

1. **A 的问题**：LMSR 加 RL 是否足以给出距离收缩 A？如果不够，\(\mathcal K\) 是否能补上 A 所需的几何/选择/能量信息？
2. **B 的问题**：KL、下降和真实相对误差能否替代原始 B，给出例如
   \[
   s_k\le \rho s_{k-1}+C\Delta\Theta_k,
   \qquad
   s_k=\|x^{k+1}-x^k\|,
   \quad 0\le\rho<1,
   \]
   其中 \(\sum_k\Delta\Theta_k<\infty\)，从而得到
   \[
   \sum_k s_k<\infty?
   \]
3. exact subgradient PPA 的 KL 定理只能作为基准，不能直接扩大为一般 RL/GPPA 结论。
4. 原证明中的 \(2\sigma\|x^{k+1}-x^k\|\) 不能凭空删除；必须证明它被能量、下降余量或可望远镜差吸收。

因此，KL 最有可能先改进 B 的证明接口；它是否还能和 LMSR 一起产生 A，必须逐步证明，不能预设。

## 之前的理解错误，必须明确避免

1. 不要把任务写成“RL + GMSR 推出 A+B”；这是旧路线，不是新问题。
2. 不要寻找“RL alone 的 Lyapunov 桥”；RL alone 的周期反例只说明缺少耗散，不是本任务。
3. 不要把一个新条件单独和 GMSR 比较，而忽略整体包 \(\mathrm{LMSR}+\mathcal K\)。
4. 不要把 exact subgradient KL 结果包装成一般 RL/GPPA 定理。
5. 不要把“旧条件不能推出 B”的反例当成严格弱化例。必须构造“LMSR+K 成立但 GMSR 失败”的例子。
6. 不要混淆 full graph、selected relation、完整真残差、选择残差、局部结论和全局结论。
7. “拆掉绝对值”不是删除有限长度结论；有限长度仍然是
   \[
   \sum_k\|x^{k+1}-x^k\|<\infty.
   \]

已有的 full-graph 例
\[
G(y)=\tfrac32(y+\sin y),\qquad F(y)=G(y)-y
\]
只能说明 A+B 可以脱离传统次单调性；它是否满足或不满足 GMSR，必须按当前 GMSR 的精确定义重新核对，不能直接当作严格弱化例。

## 研究工作流

先读取仓库中的 README.md、RESEARCH_STATE.md、CLAIMS.md、FAILED_ROUTES.md，以及 RL、LMSR、GMSR、目标二 KL 的规范定义。不要从历史聊天补定义。

然后固定：

- 空间、算子图、零集 S、步长和迭代格式；
- RL 的完整量词；
- GMSR 与 LMSR 的精确定义及参数；
- full graph 还是 selected relation；
- full resolvent 还是某个选择策略；
- 全局还是局部；
- 完整真残差还是选择残差；
- A、B 的所有输出量词、coverage 和常数。

对候选 \(\mathcal K\) 必须完成：

1. 给出独立数学定义，不能把 \(\mathcal K\) 定义成 A、B、A+B 或 KL 结论本身。
2. 在相同对象和量词下证明
   \[
   \mathrm{GMSR}\Rightarrow(\mathrm{LMSR}\land\mathcal K).
   \]
3. 构造并逐项验证
   \[
   \mathrm{LMSR}\land\mathcal K\land\neg\mathrm{GMSR}.
   \]
4. 在 RL 下证明
   \[
   \mathrm{RL}+\mathrm{LMSR}+\mathcal K
   \Rightarrow A+B
   \]
   或
   \[
   \mathrm{RL}+\mathrm{LMSR}+\mathcal K
   \Rightarrow A+B_{\mathrm{KL}}.
   \]
5. 分别攻击 RL、LMSR 和 \(\mathcal K\) 被删除后的情形。
6. 检查 full-graph 版本中 A 是否自动推出 LMSR，并说明这不等于 GMSR。
7. 如果只能在局部、轨道或 selected-relation 意义下成立，必须保持原范围，不能升级为 full-graph 定理。

## 最终交付

只提交一个最有希望的 \(\mathcal K\) 和一个主定理候选，不要堆积多个未经验证的猜想。报告必须包含：

- Exact Statement；
- Objects、Domain、Quantifiers、Assumptions；
- GMSR、LMSR、\(\mathcal K\)、RL、A、B 和 \(B_{\mathrm{KL}}\) 的依赖图；
- 整体弱化证明；
- 严格例；
- 主定理或最强可成立版本的逐步证明；
- KL 在其中究竟改进 A、B 还是只改进证明机制；
- full graph / selected relation 量词表；
- 必要性反例和 fatal objections；
- Truth、Value、Novelty、Mechanism、Status 分开判断。

状态只能使用 derived-checked、candidate、refuted、open。若找不到满足整体严格弱化的 \(\mathrm{LMSR}+\mathcal K\)，必须明确报告“本轮未完成”，并写出最关键的 obstruction；不得把 exact subgradient KL 结果或 RL-alone 反例包装成目标完成。
