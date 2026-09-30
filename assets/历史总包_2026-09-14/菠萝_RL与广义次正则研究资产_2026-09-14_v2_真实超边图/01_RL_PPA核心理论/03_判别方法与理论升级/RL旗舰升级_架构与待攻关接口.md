# RL–PPA 旗舰升级架构：保留真实路径，而不是继续扩大标量参数表

日期：2026-09-09。任务：`rl_upgrade_architect`。性质：理论架构与反例审计的中间交付；不作全球首创或投稿通过声明。

证据标记：`PROJECT_PROOF` 为本文给出证明的项目推导；`VERIFIED_SOURCE` 为本轮打开的原始来源；`PROJECT_INPUT` 为当前可读项目稿；`PENDING` 为未完成证明或新颖性核验；`AI_INFERENCE` 为研究投入和期刊竞争力判断。

## 0. 唯一首选，以及必须先纠正的一件事

**首选升级：原生、活动域相容、保留合法路径关联的联合证书演算。**

简称 **联合路径证书**。它不是要求 RL 和次正则性必须由同一个判据产生。已有独立判据继续使用；只在独立取最坏常数丢掉关键位置、符号、分支或相位信息时，保留这些关联到最后一步再作标量化。

其可发表的重心应是

\[
\boxed{\text{原始算子/集合数据}
\longrightarrow\text{真实活动路径及有限类型主项}
\longrightarrow\text{可计算的残差、吸引与位移证书}.}
\]

最后的求和收敛定理只是后端。单独写一个“若每条合法路径都收缩，则轨道收敛”的一般定理，不足以构成用户要求的旗舰。

**新发现的必要纠正：M1 两步捕获模型实际上已经具有一步统一集合距离收缩。** 本文 §2 给出精确因子

\[
\boxed{d(Tz,Z)\le\frac3{\sqrt{10}}d(z,Z)}
\]

及尖锐性。因此它分离的是 T5 的**独立统一标量 RL–EB 组合**，不是 T5 Theorem 3.1 本身，也不能被用作“只有多步升级才能证明”的例子。

这使推荐更明确：首先攻克**原生联合验证**，不要把“二步”本身包装成关键新技术。多步和一般速率是按实际问题需要启用的模块。

---

## 1. 本次审计的输入和不可混淆的层级

主要项目输入：

- `upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md`，尤其 §§2–3、3.5、4–6。
- `output/ATTACK_IRREDUCIBLE_MULTIWEAK.md`。
- `output/ATTACK_CDRS_CODERIVATIVE_VERIFIER.md`。
- `output/ATTACK_CDRS_FINITE_ATLAS_THEOREM.md`。
- `output/ATTACK_CDRS_NATURAL_MODEL.md`。
- `output/MULTISTEP_PATHWISE_RL_RESEARCH_NOTE_2026-09-09.md`。
- `output/selection_pathwise_outer_transition_RL_upgrade.md`，及 multivalued、inexact、warped 的旗舰审计。
- 用户给出的 M1 实际外层障碍及两步捕获证明。

T5 已有三层，任何“升级”必须指明改变哪层：

1. **定义层：** all-pairs RL 是 Minty 图上反射的模量；它强制被覆盖的 resolvent 输入单值，但不保证覆盖。
2. **证书层：** 解比较的 RL 步长界加独立普通/general-gauge 次正则性，可以推出一个充分距离递推。
3. **轨道层：** Theorem 3.1 已明确允许距离收缩来自更强的独立估计；并不要求它一定由标量组合产生。

故下列说法不成立：

> 找到独立统一 RL–EB 组合失败、但直接法向估计成功的例子，就证明了现有 T5 轨道定理不够。

这个例子可能只说明**证书生产方式**不够。T5 §3.5 和 §5.4 本来已经体现这一点。

另外，多值原算子与多值 resolvent 也不同。要容许相同输入的多个实际输出，不能继续要求完整 all-pairs RL；应使用 T5 已有的允许转移量词，或者明确受限的可执行选择策略。

---

## 2. 新的 M1 审计结论：两步捕获例子已经一步严格距离收缩

`PROJECT_PROOF`。设

\[
c=\frac23,\quad
f(r)=\operatorname{sign}(r)
\left[\frac32(|r|-c)_+\right]^{1/3},
\]
\[
T(z_1,z_2)=(z_1-f(z_1-3z_2),0),\qquad
Z=[-c,c]\times\{0\},\qquad z_*=(c,0).
\]

沿用已有的明确半径

\[
R=\frac1{96\sqrt{10}}.
\]

### 命题 2.1：尖锐的一步因子

对所有 \(z\in B_R(z_*)\)，

\[
\boxed{d(Tz,Z)\le\frac3{\sqrt{10}}d(z,Z).}\tag{2.1}
\]

这个局部统一因子不能改善。

**证明。** 写 \(z=(c+a,b)\)，令

\[
s=a-3b,\qquad h=\left(\frac32s_+\right)^{1/3}.
\]

由 \(|s|\le\sqrt{10}R=1/96\)，有 \(c+s>0\) 及 \(0\le h\le1/4\)。所以

\[
Tz=(c+a-h,0),\qquad c+a-h>0>-c,
\]

从而 \(d(Tz,Z)=(a-h)_+\)。若 \(a\le0\) 或 \(h\ge a\)，该距离等于零，结论成立。其余情形为 \(a>h\ge0\)，此时输入的最近解恰是 \(z_*\)，故

\[
d(z,Z)^2=a^2+b^2.
\]

若 \(s\le0\)，则 \(h=0\)、\(b\ge a/3\)，于是

\[
d(Tz,Z)=a\le\frac3{\sqrt{10}}\sqrt{a^2+b^2}.
\]

若 \(s>0\)，有

\[
b=\frac{a-(2/3)h^3}{3}.
\]

直接计算

\[
\begin{aligned}
9(a^2+b^2)-10(a-h)^2
&=h\left(20a-10h-\frac43ah^2+\frac49h^5\right)\\
&\ge ah\left(10-\frac43a^2\right)\ge0,
\end{aligned}
\]

这里使用 \(0<h<a\le R\)。故仍有 (2.1)。最后沿

\[
z_t=(c+3t,t),\qquad t\downarrow0,
\]

有 \(s=0\)、\(Tz_t=(c+3t,0)\)，距离比恰是 \(3/\sqrt{10}\)。证毕。

### 意义及正确的严格性声明

- 这个模型的最佳反射指数仍是 \(1/3\)，实际输出 EB 最佳指数仍是 \(1\)。上述推导没有与两条结论冲突。
- 失败的是把“最坏反射”与“最弱输出 EB”分别统一后代入同一标量上界。
- 其实际的一步几何保留了接缝关系 \(s=a-3b\)，由此得到严格距离收缩。
- 反射有局部 Hölder 模，故步长满足 T5 的可和几何预算；在一个进一步缩小的正初始邻域内，**T5 Theorem 3.1 已能直接应用**。
- 不能把上面的验证半径 \(R\) 未经预算计算直接称为 T5 的整个初始吸引半径；可选择更小正半径使预算留在 \(B_R(z_*)\)。已有两步直接证明则另给较大明确捕获域。

因此，先前将本例作为“多步轨道理论严格强于整个 T5”的证据必须撤回；它确实是**联合活动数据比独立统一标量组合强**的严格证据。

---

## 3. 五项候选升级的选择结果

| 候选 | 可严格定义的改动 | 对现有 T5 的精确关系 | 结论 |
|---|---|---|---|
| 原生联合、活动域相容证书 | 保留同一个状态、分支、投影参数和符号的可行关系；最后再取包络 | 严格加强证书生产力；一步结论可能仍直接用 T5 3.1 | **唯一首选** |
| 真正多步/相位路径证书 | 保留真实可执行词、完整前缀与宏步输出；允许一步增距 | 可严格扩张固定算法的一步 Q 收缩假设；不是研究 \(T^m\) 的首创 | 首选架构的按需模块 |
| 非 Q 线性/general-gauge 速率 | 用一般 \(r_{k+1}=\Theta(r_k)\) 及长度预算代替固定 \(\kappa\) | 严格扩张现有固定 Q 轨道范围；抽象证明短，已有成熟比较理论 | 必备后端模块，不单独立旗舰 |
| 变度量/退化/warped RL | 同一算法的测试度量、真正改变近端算子的预条件器、商空间与 lift 分别处理 | 固定 SPD 多为共轭；退化升维要另证 kernel 重建 | 暂缓，除非公开问题迫使使用 |
| 可执行集合值选择稳定性 | 明确 existential、策略全部输出、完整映射全部输出三个量词 | T5 已容许非空允许子关系；新处须是原生选择器及其稳定性 | 并入联合路径，不另建空泛总定理 |

**不保留的升级口号：**“允许任意 \(\psi\)”“加向量”“加历史”“加一般度量”“把一步换成 \(m\) 步”。这些可用，但没有新的原生验证生产定理时，只是形式扩展。

---

## 4. 首选升级的严格对象：联合路径证书

设 \(X=\mathbb R^n\)，目标 \(S\) 非空闭，\(T:X\rightrightarrows X\) 是**实际实施**的转移关系。若原算法是 PPA，仍要求每条允许边

\[
x_{j+1}=x_j-\lambda v_j,\qquad v_j\in F(x_{j+1}).
\]

若是 splitting，先写出其精确投影/预解算子调用，不把替代算法和原算法混合。对 \(T\) 的形式重构

\[
\mathcal F_T(y)=\{x-y:y\in T(x)\}
\]

可以保留，但不充当原生验证。

### 4.1 合法路径与特征

一个有限状态 \(\sigma\) 记录活动面、投影选择、算法相位及需要的有限历史。边 \(e:\sigma\to\sigma'\) 只在原生方程与活动比较全部成立时可执行。

每条长度 \(m\) 的真实路径 \(w\) 有内部变量

\[
\xi_w=(x_0,x_1,\ldots,x_m,\text{所有实际投影/算子输出}).
\]

从原始图关系、分块增长、法向方程、余项界、活动不等式产生一个显式外证书关系

\[
\mathcal C_w\ni
(d_0,d_m,s_0,\ldots,s_{m-1},\zeta_0,\ldots,\zeta_m),\tag{4.1}
\]

其中 \(d_j=d(x_j,S)\)、\(s_j=\|x_{j+1}-x_j\|\)，\(\zeta_j\) 是保留的活动/正常/间隙特征。

最重要的 soundness 要求是：**每条被宣称允许的真实路径都映入一个 \(\mathcal C_w\)**。关系可以是外包络；若要称最优或充要，另须实现性/紧性证明。

边连接必须共享同一个 \(\zeta_j\)，不能把前一边的最坏输出与后一边另一个不可兼容输入随意拼起来。

### 4.2 联合包络

定义

\[
\Theta(t)=\sup\{d_m:\text{某个合法 }w\text{ 的 (4.1) 成立， }d_0\le t\},\tag{4.2}
\]
\[
G(t)=\sup\left\{\sum_{j=0}^{m-1}s_j:
\text{同一条合法路径证书成立， }d_0\le t\right\}.\tag{4.3}
\]

还应保留前缀距离界 \(D_j(t)\) 和前缀位移界，供局部覆盖复用。

独立 RL 与 EB 是一种合法生成方法：在每条边的关系中加入

\[
s_j\le\frac{d_j+\omega_j(d_j)}2,\quad
d_{j+1}\le\psi_j(s_j/\lambda),
\]

必要时加入能量约束。使用独立证书不需统一其来源。本次真正的升级是还保留诸如

\[
s=a-3b,\qquad
b=(a-(2/3)h^3)/3
\]

这样的原生关联，而不是把它们在取模时消掉。

**避免循环定义。** (4.2) 本身只是规格。若使用者必须预先输入待证的实际距离收缩、完整 residual EB 或未知 Lyapunov 函数，便没有解决验证问题。旗舰生产定理必须从更低层的原生数据构造 (4.1)，并真正求出 (4.2)–(4.3) 的可用上界。

---

## 5. 应有的后端主定理：一般比较递推与局部全过程

下面是已经可证明、但本身不宜作为主要新颖性卖点的后端。

### 定理 5.1：同一目标的联合路径收敛

`PROJECT_PROOF`。设实际允许关系在开集 \(V\) 的有效距离管内逐边非空。设有限 \(m\) 的证书覆盖每条允许路径及其前缀；由原生数据导出的 \(\Theta,G,D_j\) 非减并在零消失。这里明确要求：对于每条已经存在的长度 \(j\le m\) 的允许前缀，均能直接验证前缀距离界 \(D_j(t)\) 及累计位移不超过 \(G(t)\)，不以该前缀将来已能延长到长度 \(m\) 为前提。令

\[
r_0=d(x_0,S),\qquad r_{k+1}=\Theta(r_k).
\]

假设 \(r_k\to0\)，所有 \(D_j(r_k)\) 留在有效距离域内，并且

\[
H(r_0)=\sum_{k\ge0}G(r_k)
<d(x_0,X\setminus V).\tag{5.1}
\]

则每条允许轨道都可无限继续，整条轨道留在 \(V\)，且

\[
d(x_{km},S)\le r_k,\qquad
\sum_{j\ge0}\|x_{j+1}-x_j\|\le H(r_0).
\]

轨道收敛到一个 \(S\) 中的点。

**证明。** 使用证书的前缀界逐边归纳。已构造前缀的位移小于 (5.1) 的部分和，因此输出仍位于 \(V\)，而前缀距离条件让 coverage 可以再次使用。在宏步端点应用 (4.2) 得到 \(d(x_{km},S)\le r_k\)；(4.3) 控制每个宏步长度。总长有限给 Cauchy，闭目标及端点距离趋零识别极限。证毕。

对 \(m=1\)、\(\Theta(t)=\kappa t\) 和 T5 的 \(G=B\)，这就是现有轨道定理。它保留一般 \(\psi\)，没有把所有问题约化为临界幂函数。

### 可计算的非 Q 线性长度条件

若 \(\Theta(t)=t-\delta(t)\in[0,t)\)，\(\delta\) 连续且在正轴严格正，则比较序列趋于零。若

\[
w(t)=\frac{G(t)}{\delta(t)}
\]

在 \((0,r]\) 非增，且 \(\int_0^r w(t)\,dt<\infty\)，那么

\[
\sum_kG(r_k)\le\int_0^{r_0}\frac{G(t)}{\delta(t)}\,dt.\tag{5.2}
\]

证明：在 \([r_{k+1},r_k]\) 上 \(w(t)\ge w(r_k)\)，故每段积分至少等于 \(w(r_k)\delta(r_k)=G(r_k)\)。求和即可。

例如 \(\delta(t)=ct^{1+a}\)、\(G(t)=Ct^b\)，其中 \(a>0\)，则在比例函数非增的通常范围 \(b\le1+a\) 内，\(b>a\) 保证

\[
H(r_0)\le\frac{C}{c(b-a)}r_0^{b-a},
\qquad r_k=O(k^{-1/a}).\tag{5.3}
\]

这里的 \(b\) 是实际路径位移阶，不能未经证明用反射最佳指数替代。CDRS 高阶接触例恰显示：一般 RL 的位移上界可能比实际有符号的位移弱得多。

### 该可和门槛的反例

`PROJECT_PROOF`。在小的 \(t\ge0\) 上令

\[
T(s,t)=(s+t^b,t-ct^{1+a}),\qquad S=\mathbb R\times\{0\}.
\]

则 \(t_k\asymp k^{-1/a}\)。当 \(b\le a\) 时，切向总位移 \(\sum t_k^b\) 发散，轨道不收敛到单点。故“距离趋零加任意趋零步长”不够。这是纯边界验收例，不是自然应用或首创主张。

---

## 6. 多步的真正严格扩张，以及它不能证明的事

### 一个确实不能由一步距离 Q 收缩覆盖的验收例

`PROJECT_PROOF`。取 \(0<\alpha<1\)，在 \(\mathbb R^3\) 令

\[
T(s,u,v)=\left(s+|u|^\alpha,\sqrt{|v|},0\right),
\qquad S=\mathbb R\times\{0\}\times\{0\}.
\]

则

\[
T^2(s,u,v)=
\left(s+|u|^\alpha+|v|^{\alpha/2},0,0\right)\in S.
\]

但沿 \((s,0,t)\) 有

\[
\frac{d(T(s,0,t),S)}{d((s,0,t),S)}=t^{-1/2}\to\infty.
\]

故任何满邻域的一步 Q 距离收缩都失败；两步路径定理适用，且首块长度为 \(O(d^{\alpha/2})\)。通过 \(\mathcal F_T\) 可精确重构成 PPA。

这个例子证明**逻辑严格性**，但它是刻意设计的三角模型，不能作为旗舰自然应用。要使多步模块升格为主贡献，必须在真正原生、不可分离 splitting 类中发现同样的必要性；M1 现有两步例子不够，见 §2。

### 三个多步止错反例

1. **假周期：** \(T(x)=1-x\) 有 \(T^2=I\)，但 \(\operatorname{Fix}T=\{1/2\}\)。块重构的零点是 \(\operatorname{Fix}T^m\)，不能自动换回 \(\operatorname{Fix}T\)。
2. **中途逃域：** 一阶段 \(T_0(x)=Mx\)、下一阶段 \(T_1(y)=y/(2M)\) 的宏步为 \(x/2\)。宏步收缩本身不保证初始半径内的第一阶段有效；必须给前缀界和缩小半径。
3. **选择不稳定：** 宏步端点唯一不意味着全部 shadow 选择收敛；可令第一阶段在 \(\{-1,1\}\) 任意选、第二阶段固定回到零。端点总为零，但第一阶段可永远交替。不能从端点收敛直接推出所有内部选择收敛。

---

## 7. 不相容 CDRS 必须升级“相位对象”，不能要求错误的有限长度

若一个真实极限循环有不同相位 \(p_0,\ldots,p_{m-1}\)，则原始交错序列中的相邻步长一般趋向 \(\|p_{j+1}-p_j\|>0\)。因此其原始总长度必为无穷。

这不是算法失效；正确的收敛对象是：

- 每个固定相位的子序列；或
- 整个循环提升状态 \(\mathbf x^k=(x_{km},\ldots,x_{km+m-1})\)。

联合路径证书在不相容问题中必须比较**相邻宏周期的相同相位**，而不是把非零极限 gap 计作误差。

一个可用的提升条件是：对实际允许相位输出及同一极限 cycle，有

\[
\|x_{km+j}-p_j\|\le\chi_j(d(x_{km},S_0)),\qquad\chi_j(t)\to0.
\]

若要提升到循环状态的有限长度，则需要逐周期相位变化的可和模量，而不是仅有点态连续性。存在选择、指定策略与全部选择的量词依然分别验证。固定相位映射单值且连续只是一个充分情形；多值 tie 要另证合流或稳定选择。

**正文风险：** `ATTACK_CDRS_CODERIVATIVE_VERIFIER.md` §1 对一般多值公式写“必须复用”，而 `ATTACK_CDRS_FINITE_ATLAS_THEOREM.md` 正确区分了完整 Minkowski 关系与复用实现。两者应统一；凸高阶接触例的投影单值，因此其具体公式不受此冲突影响。

---

## 8. 为什么另外三类升级目前不是首选

### 8.1 固定/可变正定测试度量

固定 SPD 度量常是线性共轭，给 RL 常数和距离常数乘以条件数即可；这不够独立创新。可变度量需要一致上下界以及控制相邻度量变化，例如乘性变化的可和性；还必须区分改变分析范数与改变实际近端映射。

**不可救反例：** 若实际线性 \(T\) 有特征值 \(\lambda_T>1\)，任何范数都满足 \(\|T\|\ge\lambda_T\)。因此 multiweak 的大步长惯性障碍不能通过固定等价度量消除。统一等价的可变度量同样不可能把实际指数发散轨道变成趋零轨道。

若允许度量本身趋于零，例如对 \(T(x)=2x\) 取 \(P_k=16^{-k}I\)，则 \(\|x_k\|_{P_k}=2^{-k}\|x_0\|\to0\)，而 \(\|x_k\|\to\infty\)。这种“收敛”不具有原变量意义。

所以 multiweak 应另开**算法设计/符号修复**路线；不能把调整测试几何当成已救回同一个算法。

### 8.2 Warped/退化图

商空间 reflected chart 可严格定义，kernel lift 的 Hölder/Dini 模可提升速率和长度。然而固定 warp 下常只是把 T5 用于一个精确变换后的算子。只有原生 coverage、误差界与不可见 kernel 恢复来自实际问题结构时才有新作用。

**不可省条件：** shadow 收敛不强制 kernel 分量收敛；连续 lift 提升点收敛，定量模才提升速率/总长。不能把这些基础事实当作已解决一般 nonlinear warped 公开问题。

### 8.3 选择稳定性

T5 的允许关系已经足以书写“所有允许输出收敛”。新增主定理必须生产一个**可执行**策略，而不是假定好输出集合非空后调用选择公理。

反例 \(T(x)=\{x/2,2x\}\)：存在全局收敛选择不意味着任意选择收敛。静态解锚条件在 \(d=0\) 且模量为零时又会迫使所有被认证输出固定，所以它仍限制被认证子关系在解集上吸收；不能宣称完全消除了 strong-fixed-point 问题。

上述选择规则应放入联合路径的合法边/策略域。何时选择可计算、何时所有选择都成功，才是实际内容。

---

## 9. 应攻击的生产主定理，不是已经证明的主定理

### 目标定理 N：原生有限类型 → 相容路径证书

`PENDING`。优先针对 CDRS 的一个明确有限类型结构类，而不是任意闭集合。

**输入必须来自原生层：**

1. 原始集合/算子有限参数定义，以及实际 projector/resolvent 的完整最近点/图分支验证；
2. 可执行路径的活动比较，包含 tie、完整分支和策略范围；
3. 正常方向或接触参数的首个非零阶、系数及共同余项界；
4. 实际零周期的修复/参数化，不能把环境分支零集误当实际固定集；
5. 可核验的循环主项不消去条件；若消去，自动转入更高阶；
6. 非孤立目标的真实对称方向或零方向，不能仅取 \(\ker(I-DT)\)。

**输出应同时明确但不强求来自同一个输入判据：**

- 各分支的 ordinary/general-gauge 残差证书，及到真实目标的转换常数；
- 实际联合漂移/吸引包络，允许比独立 RL–EB 标量组合强；
- 位移、相位或 shadow 变化的有效模与共同正半径；
- 同一原算法的全选择、指定策略或存在选择结论；
- 存在可实现坏弧线时输出失败原因，不把不确定当成功。

**有限阶边界：** 已有 CDRS 高阶接触族说明，没有预先次数/有限类型上界时，任意固定 pointwise jet 阶数都不可能完备。因此“自适应”必须允许读取更高阶或邻域信息；泛称一阶 coderivative 黑箱不可能完成全部任务。

**为什么仍可能有较高价值：** 它把真正阻碍应用的“固定点映射次正则性需自行验证”移到原始集合参数上，并且能看到光滑谱方法、低阶 jet 和一般半代数存在论看不到的有效阶数、分支域修复和循环消去。

**为什么现在还不能宣称已有：** 现有有限 atlas 定理仍把最难的零周期修复留作输入；高阶接触族仍是二维可消元模型；真实多值曲线 CDRS 例子在一周期后识别活动支。三者尚未构成该生产定理。

---

## 10. 与公开问题及已知机制的对应

1. **CDRS 原生残差判据：最直接。** Dinh–Jansen–Luke 的 2026 正文明确没有给出保证固定点映射次正则性的假设。其应用背景包含不相容成像约束。该缺口值得做，但官方 2026-05-21 报告已公布 smooth/spectral、shape-operator 和 analytic Hölder 路线，因此不能把这些重做算新贡献。[JOTA 原文](https://link.springer.com/article/10.1007/s10957-026-02996-2)、[官方报告](https://math.ac.vn/serminar/on-the-metric-subregularity-for-cyclic-relaxed-douglas-rachford-operators-via-spectral-theory-and-differentiability)

2. **弱 almost-averaged/收敛选择：第二用途。** Luke–Thao–Tam 在 §2.1 明确留下从 calmness 而非 all-values strong calmness 出发的选择理论方向。联合路径可容纳这一量词，但必须真正生产原生可执行选择器；仅重写允许关系没有解决该方向。[原始论文](https://arxiv.org/html/1605.05725v2)

3. **多弱块 aDR：不能靠本升级救回已经发散的参数族。** 原文 §6 的 multiweak 问题适合先用惯性障碍划清边界，再研究改变更新符号、lifting 或步骤分支的算法。它可能是有价值的独立负向/算法设计论文；不应强迫其每个结果都叫 nonlinear RL 应用。[原文](https://arxiv.org/html/2506.22928v1)

4. **一般误差界/积分收敛：不是待发现的新后端。** 2026 的通用 EB 框架已有一般模、确定性基准和积分型有限长度机制；近期 orbital-regularity 也研究构造收敛选择。这些来源是排重门槛，不能把 abstract gauge recurrence 当首创。[一般 EB 框架](https://arxiv.org/html/2603.17438v2)、[orbital regularity 原文](https://arxiv.org/html/2608.06858v1)

这里的公开问题状态仅以已访问资料为边界；“尚未核验更晚解决”不等于“截至今日完全无人解决”。

---

## 11. Codex 证明攻击清单与停止条件

### 唯一主攻击：原生、活动域相容的有限类型 CDRS 联合证书

1. **对象冻结。** 锁定一个实际 CDRS 实施、有限类型结构类、状态/phase 目标和允许输出量词。交付精确调用式，不容许 Minkowski/复用规则漂移。
2. **覆盖先行。** 从原始集合方程证明完整最近点图，含所有 tie；给明确共同查询半径。
3. **真实零周期。** 求出非孤立固定周期及活动域相容修复。若只能假定所需 residual EB 或未知修复常数，停止宣称解决验证。
4. **生成联合主项。** 计算所有可实现路径的接触主项、间隙和符号；不将不可实现路径拼成“精确”最坏情况。
5. **主动反例攻击。** 搜索跨支取消、相同低阶 jet 不同 EB、宏步固定但伪周期、shadow 不收敛、内部逃域。
6. **先试一步联合。** 如 M1 审计所示，先检查原生关联是否已经给一步距离收缩。只有存在真实一步增距见证，再把多步写成必要升级。
7. **输出可复用参数。** 至少给指数、有效常数、共同半径、完整选择范围和相位速率；仅存在某个 \(q\) 不通过。
8. **高压力自然验收。** 至少一个不可分离、非多面体、非孤立且保留活动竞争的参数族；不能靠自由直积制造全部非孤立性，也不能仅靠一次识别后退化成单支光滑算法。
9. **近邻等价审计。** 逐式检查是否只是现有常秩、Hoffman、半代数量词消去、partial descent 或 generalized Lyapunov 的直接已知实例。抽象后端被覆盖不等于原生生产定理没价值；但必须准确定位新增部分。

### 停止或降级条件

- 只得到“假定真实路径收缩”而没有原生生产定理：降为工具引理。
- 原生定理仍以同一待证 residual MSR、零集修复 EB 或未知 Lyapunov 函数为假设：未解决问题。
- 例子只有直和、单支识别、孤立固定点 SVD 或预设 resolvent：降为验收例。
- 光滑谱/shape operator/解析存在论与官方报告重合：不得保留为主创新。
- 找到实际扩张谱或坏周期：对该算法成员停止正向收敛证明，改写为障碍；若改变算法需独立标记。
- 高阶解析求根只是通用量词消去换名，既无有效常数也无结构优势：不立旗舰。

---

## 12. 期刊竞争力判断

`AI_INFERENCE`，不是期刊邀请、评级或录用保证。

**当前抽象升级本身：不足以支持独立 SIOPT/Mathematical Programming 级主张。** 其归纳/求和证明短，与比较函数、有限步 Lyapunov、partial/Fejér 和 gauge EB 理论有明显交集。

**以下完整包有理由竞争 SIOPT：**

- 一个从原始非凸多集合数据实际输出证书的可复用定理；
- 覆盖真实分支域、非孤立零周期、高阶接触与循环消去；
- 已有低阶方法给不了的明确指数、常数、半径及算法率；
- 自然参数族和严格失效/最优性反例；
- 与最近公开工作的逐定理排重。

**Mathematical Programming 或更高的竞争力需要更大增量：** 例如对一大类真实非凸 feasibility/splitting 给出具有泛型或近充要意义的原生判据，或者从障碍导出新算法并给出广泛收敛/复杂度优势。只有少数精心设计模型加抽象包装，不足以作这种定位。

不要用作者名气、预印本时间、论文源期刊代替上述证明验收。也不必强迫所有成果成为 RL 的独占应用：一个真正重要的惯性障碍或原生 verifier 可以有独立价值；RL 作为可移植的证书后端仍然有作用。

## 13. 返回契约

```yaml
contract_version: "1.0"
expert_skill: sci-skills
project_id: RL-PPA-HIGH-AMBITION
paper_family: T
stage_id: T2
task_id: rl_upgrade_architect
task_status: COMPLETE
outputs:
  - output/RL_FLAGSHIP_UPGRADE_ARCHITECTURE.md
evidence_status:
  - PROJECT_PROOF: M1 capture example has sharp one-step distance factor 3/sqrt(10)
  - PROJECT_PROOF: general-gauge finite-path backend and integral length criterion
  - PROJECT_PROOF: strict multistep witness and counterexamples for missing assumptions
  - VERIFIED_SOURCE: public CDRS, selection and multiweak problem passages and recent overlap
  - PENDING: native finite-type joint certificate production theorem
  - AI_INFERENCE: flagship priority and journal competitiveness
quality_checks:
  - independent certificate production preserved
  - current T5 trajectory theorem not weakened for comparison
  - full algorithm, target, phase and selection scopes distinguished
  - no convergence claimed for actual expanding multiweak dynamics
  - abstract backend separated from proposed main novelty
conflicts:
  - M1 two-step example is not a strict separation from all of T5 Theorem 3.1
  - general multivalued CDRS reuse versus Minkowski formula needs unification
conflict_resolution_status: UNRESOLVED
merge_permission: orchestrator_only
recommended_next_action: Independently verify Proposition 2.1, then launch only the native finite-type CDRS joint-certificate production attack with the stop conditions in Section 11.
stage_acceptance_recommendation: NOT_ASSESSED
```

**唯一下一行动：**主代理复核命题 2.1，并据此把主攻击冻结为 §11 的“原生有限类型联合证书”，而不是继续以 M1 两步捕获作为多步升级必要性的依据。
