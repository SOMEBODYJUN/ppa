# 退化预条件与高阶扰动的独立接口

这里固定两个相邻问题的对象及已能直接证明的边界。它们分别为原关系的值域取得问题和非孤立目标的真残差问题；没有默认的相互蕴含。下述 式 SP1–SP6 是直接推导，来源中的文献范围、优先权及“尚无一般答案”只保留为待核报告。

<a id="sp-preconditioned"></a>
## SP1 · 完整退化步的覆盖量词

设实 Hilbert 空间 \(H,H'\)，有界线性满射 \(C:H\to H'\)，\(Q=C^*C\)，任意完整关系 \(A:H\rightrightarrows H\)。定义
\[
T_Q(x)=\{y:Q(x-y)\in A(y)\},\qquad
F_{\rm red}=(CA^{-1}C^*)^{-1}.
\]
这些都是**完整关系**；\(C\) 不要求单射，\(A\) 不要求单调或有零点。对每个 \(p\in H'\) 有完整纤维恒等式
\[
J_{F_{\rm red}}(p)=C(A+Q)^{-1}C^*p.\tag{SP1}
\]
这里 \(J\) 的步长固定为 1。证明：\(z\in J_{F_{\rm red}}(p)\) 当且仅当 \(z\in CA^{-1}C^*(p-z)\)，即存在 \(y\) 使 \(Cy=z\) 且 \(C^*(p-Cy)\in A(y)\)。这恰是右侧纤维的定义；反向逐步可逆，不把“有某个输出”误写成“所有输出等同”。

因为 \(C\) 满射，\(\operatorname{ran}Q=\operatorname{ran}C^*\)：包含方向显然；反向对任意 \(p\) 选 \(x\) 使 \(Cx=p\)，便有 \(C^*p=Qx\)。故
\[
\operatorname{dom}T_Q=H
\iff \operatorname{ran}Q\subseteq\operatorname{ran}(A+Q)
\iff \operatorname{dom}J_{F_{\rm red}}=H'.\tag{SP2}
\]
最后一个等价中，右侧投影纤维非空当且仅当原纤维非空。另有
\[
\operatorname{zer}F_{\rm red}=C(\operatorname{zer}A),\qquad
\|Cx\|^2=\langle x,Qx\rangle.\tag{SP3}
\]
第一式由 \(0\in F_{\rm red}(z)\iff z\in CA^{-1}(0)\) 直接得到。若原合法路径 \(x^{k+1}\in T_Q(x^k)\)，则 \(c^k=Cx^k\) 满足 \(c^{k+1}\in J_{F_{\rm red}}(c^k)\)。这只记录投影后的路径，既不证明原输出唯一，也不恢复核方向的收敛。换成步长 \(\lambda>0\) 编码须用新关系 \(F_{\rm red}/\lambda\)，不能保持关系名称却改变包含式。

<a id="sp-attainment"></a>
## SP2 · 凸目标的实际取得

设 \(f:H\to(-\infty,+\infty]\) proper、下半连续、凸，\(Q\) 有界线性自伴半正定。对每个固定 \(a\in H\)，
\[
a\in\operatorname{ran}(\partial f+Q)
\iff f(x)+\tfrac12\langle x,Qx\rangle-\langle a,x\rangle
\text{ 取得最小值}.\tag{SP4}
\]
若 \(a-Qx\in\partial f(x)\)，次梯度不等式加半正定二次项立即给全局最小性。反向设 \(x\) 为最小点。对任意 \(y\in\operatorname{dom}f\) 和 \(0<t\le1\)，在 \(x+t(y-x)\) 用最小性，并用凸性 \(f(x+t(y-x))\le(1-t)f(x)+tf(y)\)，得到
\[
f(y)-f(x)\ge\langle a-Qx,y-x\rangle
-\tfrac t2\langle y-x,Q(y-x)\rangle.
\]
令 \(t\downarrow0\) 即得次梯度条件；域外 \(y\) 的不等式自动成立。证明没有用未知的取得性质当假设。

因此仅将 \(\operatorname{ran}Q\) 包含在 \(\operatorname{ran}(\partial f+Q)\) 的**闭包**里，仍不能调用 SP4 的实际最小值。\(\ker Q\) 方向无二次强制；由退化性本身不能推出取得。某个特定文献的 restricted-monotonicity、sri 或 projected-inverse maximality 条件不在 SP1–SP4 的推导前件中，也没有在这里被认证为可用导入。

<a id="sp-perturbation"></a>
## SP3 · 保零集与完整多值抵消

固定任意 \(q>1\)，在 \(H=\mathbb R^2\) 取
\[
S=\mathbb R\times\{0\},\quad a_q(t)=\operatorname{sign}(t)|t|^{1/q},
\quad F_0(s,t)=\{(0,a_q(t))\}.
\]
约定 \(a_q(0)=0\)。完整图连续，零集恰为 \(S\)，并且对全部 \((s,t)\)
\[
d((s,t),S)=|t|=r_{F_0}(s,t)^q.\tag{SP5}
\]
定义单值扰动 \(h(s,t)=(0,t-a_q(t))\) 及完整两值扰动
\[
H_2(s,t)=\{(0,0),(0,t-a_q(t))\}.
\]
两张扰动后关系分别为
\[
G_1=F_0+h=\{(0,t)\},\qquad
G_2=F_0+H_2=\{(0,a_q(t)),(0,t)\}.
\]
二者的完整图均闭，零集仍**恰为**同一非孤立 \(S\)。但对每个 \(0<|t|\le1\)，\(r_{G_1}=r_{G_2}=|t|\)，故
\[
\frac{d((s,t),S)}{r_{G_i}(s,t)^q}=|t|^{1-q}\longrightarrow\infty,
\qquad i=1,2.\tag{SP6}
\]
无论常数 \(K<\infty\) 或邻域半径多小，扰动后同目标的 \(q\)-EB 都失败。同时 \(r_{H_2}=0\) 在全空间成立。因此“局部零集完全保持”和“扰动最小残差为零”均不能替代完整分支的非抵消控制。只查看 \(G_2\) 的 \(F_0\) 好支也不能给完整真残差 EB。

来源 M3 用 \(F(s,t)=a_q(t)\) 的标量值简写，作为 \(\mathbb R^2\to\mathbb R\) 的误差界例本可成立；若要进入本库 \(H\rightrightarrows H\) 的 PPA 约定，必须显式使用上述向量嵌入。这是类型明确的新版本，不声称来源已经给出任意 PPA 的覆盖、RL 或收敛结论。

<a id="sp-open-gates"></a>
## SP4 · 保留的研究问题与文献门

| 问题身份 | 精确尚缺内容 | 已闭内容与不可偷换的范围 |
| --- | --- | --- |
| 退化预条件的原生 actual coverage | 对指定 \(A,Q\) 类，由原生信息证明 \(\operatorname{ran}Q\subseteq\operatorname{ran}(A+Q)\)，而非把它或等价最大性预先写成假设 | SP1 给完整代数桥；SP4 给凸情形的取得等价。它们不产生新充分条件，也不证明某文献仍留公开空白。 |
| 非孤立 ordinary 高阶扰动 | 对指定自然多值类，明确旧目标或新目标，证明全部完整纤维非抵消、同窗 \(q,K,r\)，再与同一关系的 RL/coverage/留域合取 | SP5–SP6 给保零集及最小扰动残差不足的完整反例。已有满秩复合工具见 [C34–C37/C161–C165](composite_subregularity.md)。 |
| M2/M3 历史文献范围 | 每个指定 DOI/arXiv 版本的精确定理、全部假设、访问深度及与本对象的映射 | 原报告称 VERIFIED_SOURCE 不会自动成为本轮 paper fact；最新是否已有覆盖结果和全球先行性均未核。 |

一般幂型 EB 接收敛接口时，仍需 [幂次兼容](../rleb_ppa.md#r03) 或 [指定分支门](named_branch_local.md#nb-power) 的同对象数据；仅 \(q>1\) 不足。强次正则估计到一个点，ordinary 估计到给定零集；对非孤立 \(S\) 不能换名。扰动大小半径与状态邻域半径也分别固定。

<a id="sp-provenance"></a>
## SP5 · 证据与来源身份

SP1–SP6 由本页定义、包含式、凸性与实际完整纤维直接证明；数值复现仅核有限输入，不能替代证明。原来源是 `history/sources/次单调论文研究/M2_Codex_clearance_and_PRO_brief (1).md` 及两个 M3 brief；逐断言位置见 [支持资产裁决](../audit/BATCH_SUPPORT_2026_10_08.md)。旧专家提示词、任务优先级、PASS、期刊判断及“未搜索到”均属于历史行为或待核解释，不进入上述数学前件。
