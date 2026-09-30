# RL–PPA 高野心研究计划：已核验成果、论文拆分与下一步

日期：2026-09-09  
状态：T3 理论缺口与作者立场已形成；两条独立论文主线进入 T4 论文结构阶段。  
证据口径：`已核实` 表示数学证明与指定原始来源已核；`有限检索未发现直接覆盖` 不等于全球首创证明；期刊判断不是录用预测。

## 一、结论先行

本轮不再只是收集候选问题。经过多轮独立证明、反例、脚本和先行性红队，已经形成两条值得独立成篇的主线，并明确停止了若干不能支撑高影响主张的路线。

| 顺位 | 成果包 | 当前判断 | 现实投稿定位 |
|---|---|---|---|
| 1 | nice 锥上的 A1/A2 删除、amenability–MSCQ 精确分类及 full-CRCQ 反例 | **第一旗舰；数学 PASS** | SIOPT 有力候选；Mathematical Programming 合理主攻/冲刺，仍需终端优先权门 |
| 2 | Markov exact-source 输运差异的有限精确判别、锐常数及无限紧空间边界 | **独立论文 GO；数学 PASS** | SIOPT 候选；MP 条件性冲刺 |
| 3 | 非线性、多值、非孤立解集 RL–PPA 核心理论 | **继续整合** | 方法主稿；不能借前两篇的价值自动抬高期刊层级 |
| 4 | 自适应 Bregman 边界全序列收敛 | **条件进展 PASS** | 纠错/后续定理模块；完整 intended 猜想仍开放 |
| 5 | 随机 RL、随机多值 proximal 的现有正例 | **HOLD** | 保留匹配定理与障碍；暂不作为旗舰 |

最重要的变化是第一项：我们从“单个 SOC 子情形”推进到了一个一般结构分类，而不是继续添加例子。

## 二、第一旗舰：CRSC、非线性面约化与 amenability

### 2.1 精确设定

令 (C\subset E) 为有限维 proper nice 锥，(G:X\to E) 在可行参考点 \(\bar x\) 附近为 (C^1)，经过固定局部约化后满足 (G(\bar x)=0)。记

\[
F=F_{\min}(\operatorname{Im}DG(\bar x)\cap C).
\]

minimal-face CRSC 使用两项原生信息：

1. (DG(\bar x)^*C^\circ) 闭；
2. 固定子空间 (F^\perp) 上的秩
   \[
   \operatorname{rank}(DG(x)^*|_{F^\perp})
   \]
   在一个开邻域内保持常数。

它不预先假设邻近点的闭像 A1，也不预先假设最小面稳定 A2。

### 2.2 三个主结果

**定理 A（nice 锥上的公开缺口）。** 对任意 proper nice 锥，minimal-face CRSC 自动推出整个邻域上的 A1/A2，并给出

\[
G^{-1}(C)=G^{-1}(F)
\quad\text{局部成立。}
\]

证明核心是一个固定面的秩夹逼。Pataki 的闭像判据在参考点给出

\[
DG(\bar x)^*F^\triangle
=DG(\bar x)^*F^\perp.
\]

由于 \(\operatorname{span}F^\triangle\subset F^\perp\)，参考点的非零子式在邻域中保持，而 CRSC 从上方限制秩，于是两个限制映射的秩被夹成相等。这个短链条恰好补上原 minimal-face facial-reduction 定理额外使用 A1/A2 的位置。原作者稿明确把一般删除 A1/A2 列为问题；目前有限检索未找到同结论的直接先行定理。[原作者较新稿](https://www.ime.usp.br/~ghaeser/crsc-redcones.pdf)、[Pataki 闭像定理](https://optimization-online.org/wp-content/uploads/2006/12/1556.pdf)

**定理 B（amenable 锥上的非线性误差界）。** 若参考面在 (C) 中 amenable，特别地若 (C) 为 amenable 锥，则 CRSC 推出 MSCQ：

\[
d(x,G^{-1}(C))\le \kappa\,d(G(x),C).
\]

一个有效局部上界是

\[
\kappa=b+c\,a_F(1+L_Gb),
\quad
b=\frac4{\sigma\eta},
\quad
c=\frac4{\tau_F}.
\]

这里第一步用共同法向映射 (P_{F^\perp}G) 的常秩和正角把输入纠正到 (G(x)\in\operatorname{span}F) 的流形；第二步用面 amenability 把锥残差转成面残差，再沿面内严格方向纠正到 (F)。两步作用于同一个耦合映射，不是假设各块分别有误差界后简单取最大。

**定理 C（精确边界）。** 在 proper nice 锥类内，

\[
\boxed{
C\text{ amenable}
\iff
\text{每个在 apex 满足 CRSC 的 }C^1\text{ 系统都满足 MSCQ}.}
\]

反向只需测试各面的线性等距嵌入。利用已发表的四维 nice 但非-amenable 锥，可构造一个线性系统：它满足完整 facial CRCQ、全邻域 A1/A2，却沿显式弧线具有

\[
d(x,\Omega)\asymp t^3,
\qquad
d(G(x),C)=O(t^5),
\]

从而 MSCQ 失败。原锥来自 Lourenço–Roshchina–Saunderson；本工作的新增候选是把该几何转成 CRSC/MSCQ 的精确判别边界，而不是宣称重新构造了该锥。[nice 非-amenable 锥原文](https://bflourenco.github.io/papers/amenable_nice.pdf)

### 2.3 覆盖范围为何足够大

定理 B 直接覆盖：

- 任意有限多面体锥；
- 有限 SOC 与 (p)-norm 锥的耦合乘积；
- 任意阶 PSD/对称锥及其高维非多面体真面；
- proper hyperbolicity cones 在 apex 或经合法固定约化后的情形。

这些锥的 amenability 是已有几何事实，不是本项目的新发明；新结果是它们与非线性 minimal-face CRSC 的结合。[Hyperbolicity cones are amenable](https://link.springer.com/article/10.1007/s10107-023-01958-0)

### 2.4 对 RL–PPA 的准确接口

对约束关系

\[
\mathcal M(x)=G(x)-C,
\]

有

\[
d(0,\mathcal M(x))=d(G(x),C),
\]

所以定理 B 直接生产线性正则性系数 (kappa)。若另一个待分析 RL 算子 (F) 与该系统有相同局部零点，并能**独立**验证

\[
d(G(x),C)\le \chi(d(0,F(x))),
\]

则得到 RL 所需 gauge

\[
\psi_F(t)=\kappa\chi(t).
\]

这正实现“RL 几何参数与正则性参数分别验证，再在主定理中配对”的研究目标。边界也必须保留：本结果不产生 ((\gamma,L))、Minty 覆盖或 genuine \(\gamma<1\) 所需的高阶误差界。

若参考面只有一般面误差界

\[
d(y,F)\le\omega(d(y,C)),
\]

同一证明还给出一般 gauge

\[
d(x,\Omega)
\le br+c\,\omega((1+L_Gb)r),
\qquad r=d(G(x),C).
\]

因此一般广义度量次正则性仍然是必要语言，而不是被幂函数替代。

### 2.5 价值判断

这一包具有顶级优化期刊喜欢的完整形态：一个明确公开缺口、一个简洁但非平凡的一般正定理、一个必要且精确的结构分类、一个击穿更强 facial CRCQ 的显式反例，以及产品锥/PSD/hyperbolicity 的广泛后果。它不是靠加入算法数值实验来凑重要性。

当前最合理的判断是：**SIOPT 有力候选；Mathematical Programming 合理主攻/冲刺。** 这不是录用承诺；最后风险是同假设优先权和编辑对短 rank-sandwich 洞察重要性的评价。

## 三、第二论文：Markov exact-source 输运差异的可识别性

### 3.1 有限状态完整分类

保持原随机迭代理论中的全部量词：外层遍历所有不变律，内层只在输入边缘的平方距离最优输运计划中最小化同步位移差。记该差异为 \(\Psi\)。在固定有限状态空间上，已经证明：

\[
\Psi^{-1}(0)=\operatorname{inv}P
\iff
\exists K<\infty:\quad
d_{W_2}(\mu,\operatorname{inv}P)\le K\Psi(\mu)
\quad(\forall\mu).
\]

而且 \(\Psi^2\) 是连续分片仿射函数；normalized Kantorovich dual 的顶点与 tight-edge 多面体给出有限 LP 的 exact-zero 检验、失败见证和锐平方常数

\[
K_*^2=\max_v\frac{E(rv)}{R\cdot v}.
\]

一般 PWA/Hoffman 的“零点正确即可存在某个误差界”机制是已有工具；候选新增是对原始双层 source discrepancy 保留全部量词后的精确有限表示、锐系数和可证伪验证器。[Hoffman](https://nvlpubs.nist.gov/nistpubs/jres/049/4/v49.n04.a05.pdf)、[Dolgopolik](https://arxiv.org/html/2210.02606v3)

### 3.2 正反边界

四状态 lazy cycle 例给出：

- 点的 displacement signature 有碰撞，逐点 co-Lipschitz 判据失败；
- OT 最优性仍恢复 exact identification，删掉该限制则产生假零；
- 全局锐平方常数为 (13/p)，局部锐平方常数为 (4/p)；
- 链对全部初始律几何混合，但每个稳态邻域仍有一步 (W_2^2) 膨胀，源论文指定的一步标量证书不兼容。

在一个紧致无限状态模型中，exact zeros 和统一几何收敛仍不能推出任何正 Hölder 误差界。这给出“有限结构可精确验证，紧性本身不足”的边界。

源论文已经意识到 identification 与 subregularity 要分别假设，也曾概括有限维线性情形存在 linear gauge；不能声称他们完全没有预见有限误差界。有限检索未发现同一 exact-source 双层对象上的完整分类。[HLS](https://academic.oup.com/imatrm/article/7/1/tnad001/7459406)、[Luke](https://link.springer.com/article/10.1007/s10107-024-02124-w)

### 3.3 与 RL 的关系及论文拆分

该论文与 RL 共享的核心原则是：几何、残差、目标集和实际转移必须匹配；收敛本身不等于某个一步标量证书兼容。但其主定理并不依赖 T5 的 genuine nonlinear RL–EB 定理。因此应独立成篇，不把概率、OT 与 RL 的全部语言强行放入同一主稿。

当前判断：**聚焦论文 GO；SIOPT 候选；MP 条件冲刺。** 不需要再加一个随机 proximal 算法才允许写作。

## 四、T5 RL–PPA 主稿的真实状态

应保留的核心贡献：

- all-pairs RL 与耦合 Minty 反射 Hölder 几何的精确等价；
- 单值性、覆盖性与局部轨道可延拓的严格分离；
- 一般 (omega,psi) 的耦合标量机制，而非只写幂函数；
- 非孤立解集上距离收缩、切向运动、有限长度与点收敛的不同角色；
- 将现有 monotonicity/coderivative/constant-rank/error-bound 工具分别转成 ((\gamma,L)) 与 (psi)，再在同一转移上匹配；
- genuine \(\gamma<1) 的跨分支和最优指数验证障碍。

当前不能宣称的内容：已有自然例子的收敛有时可由更强分块或多步论证直接得到；因此尚不能说 RL 是这些模型不可替代的唯一工具。第一旗舰显著加强了正则性验证侧，却没有自动解决 nonlinear RL 几何侧。

## 五、已经停止的包装路线

### 5.1 随机/多值 RL

保留的数学模块包括：合法驻定参照耦合、源残差与实际 law-step 的区分、质量稀释的必要指数、先组合再积分的临界常数保持，以及满邻域随机局部化会被小质量污染破坏。

暂不作为旗舰，原因是目前正例仍可由更直接的三角结构、群平均或经典 stochastic regularity 解释；尚无一个自然非乘积随机 proximal 模型迫使 nonlinear RL 发挥不可删作用。Markov 论文的价值不需要依赖这项成功。

### 5.2 自适应 Bregman

按目标论文显式列出的条件，解析反例确实使原 adaptive 轨道具有多个最优聚点；但若标题规范吸收经典 Bregman-with-zone 定义中的闭域严格凸，该反例不属于 intended 类。因此只能写作

\[
\texttt{LITERAL\_STATEMENT\_DISPROVED / INTENDED\_CONJECTURE\_OPEN}.
\]

在完整 intended 条件下已经得到经审计的正面进展：episodic 非消失步长条件、边界兼容次梯度的加权 work 捕获，以及边界 (C^1)+步长上界下允许 (gamma_k\to0) 的全序列收敛。完整猜想仍未解决，不作旗舰宣传。

## 六、T3 阶段交付

### 核心论点

部分算子/约束信息并不需要由一个统一判据同时产生全部参数。最有效的路线是：分别用原生图几何工具验证 RL，用 constant-rank/facial/amenability 工具验证广义次正则性，再在同一算子、同一零点集、同一实际转移上匹配。amenability 定理为正则性侧提供了目前最强的结构化供应器；exact-source Markov 分类则显示，在概率提升中 identification、误差界与一步率兼容仍是三个不同问题。

### 理论缺口陈述

1. 原 minimal-face CRSC facial reduction 额外要求 A1/A2；当前结果表明 nice 锥上这两项由 CRSC 自动推出。
2. nice 几何不足以普遍产生线性误差界；amenability 恰好给出 universal CRSC⇒MSCQ 的边界。
3. 有限状态 exact-source discrepancy 缺少保留完整嵌套 OT 量词的精确可验证性与锐模量分类；紧致无限状态又显示 exact identification 与 mixing 不足以产生 Hölder EB。
4. RL 主理论仍缺少一个自然概率/多值模型，其中 nonlinear RL 与独立高阶 EB 均不可由成熟直接机制替代。

### 论证对象与反驳清单

| 可能反驳 | 当前回答 |
|---|---|
| “这只是 Pataki 定理的重述” | Pataki 提供参考点闭像等价；新增链条用固定面 rank sandwich 推出全邻域 A1/A2，再通过共同非线性流形修正得到 MSCQ。|
| “nice 已经足够给误差界” | 错。四维 nice 非-amenable 锥给 full facial CRCQ/no-MSCQ 显式反例。|
| “产品锥只是逐块拼接” | 错。证明控制一个耦合输入映射的共同法向流形；无逐块输入 EB 假设。|
| “有限 Markov EB 是新 Hoffman 原理” | 不是；一般 PWA/Hoffman 机制明确归还先行理论。新候选限于 exact-source 嵌套 OT 的精确表示、锐常数和边界。|
| “随机题材自动提高 RL 价值” | 不是；若概率部分可删而结论不变，就不作为 nonlinear RL 旗舰。|
| “一般 gauge 可自动绕过所有指数障碍” | 不是；稀释与弧线反例约束任何统一 gauge。一般 gauge 只在确有非幂率或面残差函数时使用。|

### 修正后的题目

第一旗舰建议题目：

> **Minimal-Face Constant Rank, Nonlinear Facial Reduction, and Metric Subregularity over Amenable Cones**

第二论文建议题目：

> **Identification and Sharp Error Bounds for Invariant Transport Discrepancies of Finite Markov Systems**

T5 方法稿建议题目：

> **Nonlinear Reflected-Resolvent Geometry and Generalized Subregularity in the Proximal Point Algorithm**

## 七、固定下一步

第一旗舰已经通过数学门，不再增加锥类或算法作为启动条件。下一步仅完成其终端同假设优先权核验，然后把三定理包写成统一 LaTeX 主稿：nice 上删除 A1/A2；amenability 的 universal CRSC⇒MSCQ 分类；full facial CRCQ/no-MSCQ 反例。Markov 稿随后按已经冻结的有限/无限边界独立成篇。

