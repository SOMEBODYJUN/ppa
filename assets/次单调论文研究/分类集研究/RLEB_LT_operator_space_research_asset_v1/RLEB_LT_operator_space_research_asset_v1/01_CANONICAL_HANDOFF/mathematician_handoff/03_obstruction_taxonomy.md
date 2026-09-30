# RLEB–LT 体系比较：障碍分类、严格 no-go 与待补桥梁

日期：2026-09-20。任务：给数学家团队提供可以直接接手的障碍清单。本文独立核对现有工作稿中的最小模型与逻辑承重点，不把已有“PASS”当作新命题的证明，不重新审查未被调用的原 RLEB 主定理。

## 0. 判断先行

**理想方向尚未被否定，但上一阶段建议的“仿射解集＋正常收缩＋非退化漂移”只能是辅助结构层。** 没有证明该层在一个事先确定的中立母空间中的位置，也没有同域、同尾的范畴转移定理时，它不能回答“RLEB 在整个合理 PPA 世界里比 LT 多多少”。

目前遇到的困难分三种，不应混在一起：

1. **已证明不可能的无条件推断。** 例如固定步长切片第一纲不能推出存在步长类第一纲；证书集合第一纲不能推出对象像第一纲；原残差阶和距离阶双侧保真时不能制造无界线性位移。
2. **必须明确选择的数学问题。** 例如比较单步/原图拓扑还是全时间拓扑，固定步长还是存在步长，逐点收敛还是共同尾收敛。没有一个不作这些选择的、与拓扑无关的“占多少”。选择应由研究目的先定，不能由期望的结论倒选。
3. **真正尚未解决的构建定理。** 中立且非退化的 Baire 分母、对象侧同域同尾逼近、完整纤维 EB 的局部粘合、跨层范畴保持。这些没有现成反例一概否定，但也没有被现有结构变形证明。

本文所列反例只用来否定精确的普遍推断；它们不是 RLEB–LT 总体比较的替代品。

## 1. 统一符号与量词底线

有限维状态空间先取 (E=\mathbb R^d)。完整闭图算子为 (F:E\rightrightarrows E)，固定步长 (\lambda>0)，

\[
J_{\lambda F}=(I+\lambda F)^{-1},\qquad
r_F(u)=\inf\{\|v\|:v\in F(u)\},\qquad S=\operatorname{zer}F.
\]

令 (L_\lambda(u,v)=(u+\lambda v,u))。完整 resolvent 图为 (\Gamma=L_\lambda\operatorname{gph}F)。只有在 (\Gamma\cap(U\times E)=\operatorname{gph}T) 时，才称 (T) 是共同开输入域 (U) 上的完整算法，而不是选中分支。

对紧初值/工作域 (K)，单步距离取 (\|T-U\|_K)，全时间距离取

\[
d_{\rm dyn}(T,U)=\sup_{n\ge0}\min\{1,\|T^n-U^n\|_K\}.
\]

非增实际尾预算 (e_n\downarrow0) 的层记为

\[
\mathfrak D_e=
\left\{T:T|_S=I,\ 
\|T^m-T^n\|_K\le e_n\ (m\ge n),\
\sup_{x\in K}d(T^nx,S)\le e_n\right\}.
\tag{1.1}
\]

局部原图版还保留 (F) 坐标和全部域外纤维。标准紧源图版为

\[
F_{T,K}(u)=\{(x-u)/\lambda:x\in K,\ Tx=u\}.
\tag{1.2}
\]

它是一个合法完整闭图算子，完整 resolvent 定义域恰为 (K)；**它不是已有局部原算子的无损替代品。**

## 2. 总表：障碍属于哪一种

| 编号 | 类型 | 已有严格结论 | 对理想方向的含义 | 判级 |
|---|---|---|---|---|
| O1 | 逻辑量词 | 存在选择、全选择、固定步长、存在步长、所有策略不等价 | 先写清对象与量词，不能混合统计 | 必须规范问题；可绕过 |
| O2 | 最外层拓扑 | 最大 AW 闭关系空间中固定非解输入的一步可解类已第一纲 | 最外层类别比较会同时淹没两套理论 | 对该比较口径是真 no-go；须选无标签良定层 |
| O3 | 拓扑 | 单步接近不控制全时间或极限；即使 exact (S) 和一致收敛都保持 | (d_{\rm dyn}) 中的结论不能冒充 AW/(C^0) 结论 | 真 no-go；共同尾给条件性桥梁 |
| O4 | 相对纲 | 一个合法一步回缩层中 RLEB 并类可自第一纲 | “LT 在 RLEB 中第一纲”可能完全空洞 | 真 no-go；需非退化 Baire 分母 |
| O5 | 描述集合 | (F_\sigma/K_\sigma) 只给可描述性，不给大小；证书投影不保第一纲 | 编码成功不是分类完成 | 真 no-go；需对象侧内点定理或饱和转移 |
| O6 | 动力学/几何 | 逐点收敛不保证连续回缩；固定共同尾层可能为空或边界层 | “所有 PPA 收敛”比“统一回缩”更大 | 必须明确问题；部分有拓扑不可能性 |
| O7 | 同尾闭合 | 任意小全时间扰动可打破固定尾；近恒等共轭通常仅保 ((1+\varepsilon)e) | 现有变形不是固定分母内稠密性定理 | 真稳定性反例＋未解决构建瓶颈 |
| O8 | 步长谱 | 具有严格局部证书的原算子可实现任意非空紧良定谱 | 不可用“严格所以开”或有理步长代替所有实步长 | 真 no-go；紧参数闭块编码可绕过 |
| O9 | 局部/全图 | 相同局部全轨道不决定真实最小残差 | 单看局部 (T) 会丢掉 EB 信息 | 真 no-go；保留 (F) 与双 collar 可绕过 |
| O10 | 残差几何 | 双侧残差/距离保真共轭不能爆破线性位移；粗糙证书需更强残差阶 | 不能只“插尖点”而宣称仍在 RLEB | 真代数 no-go；需新残差几何机制 |
| O11 | 层位置 | 结构层内开/稠密不传到中立母空间 | 现有结构变形仍只是条件性工具 | 未解决的核心比较桥梁 |
| O12 | 维数/紧性 | Hilbert 中范数最小值、AW 可分性、复合连续性均可失败 | 当前有限维状态结论不能符号替换成 Hilbert 版 | 真反例；须另建无限维框架 |

## 3. O1：量词错误不是技术细节

### 3.1 存在一条收敛轨道不等于所有合法 PPA 轨道收敛

令

\[
F(0)=\mathbb R,\qquad F(u)=\{-u/2\}\quad(u\ne0).
\]

图是一条直线与一条竖线的并，闭图，零集为 ({0})，而

\[
J_F(x)=\{0,2x\}.
\tag{3.1}
\]

每步选 (0) 一步终止，每步选 (2x) 对非零初值发散。故“使 PPA 收敛的算子”必须明确完整选择量词。

### 3.2 每个固定步长都收敛，不等于任意正步长策略都收敛到解

取 (F=I)。每个固定 (\lambda>0) 的 resolvent 为 (x/(1+\lambda))。但变步长时

\[
x_n=x_0\prod_{k=0}^{n-1}(1+\lambda_k)^{-1}.
\]

若 (\lambda_k=2^{-k-1})，无穷乘积严格为正，非零初值不趋于零。要求任意正步长策略会排除最基本的强单调例子。若研究统一策略，需事先给步长下界或适当累积条件。

### 3.3 每个步长切片第一纲，不推出存在步长并第一纲

最小逻辑模型是 (\mathbb R=\bigcup_{a\in\mathbb R}\{a\})。每片第一纲，总并不是。对 (\bigcup_{\lambda>0}\mathcal L_\lambda) 必须作对象侧可数闭块编码，或找不依赖步长的必要条件；不能直接取不可数并。

**判级。** 上述无条件推断均被否定；不阻止定义精确体系，但必须先冻结量词。

## 4. O2：最大 AW 空间的类别尺度已被可解性占满

令 (\mathcal H=\mathrm{CL}_*(E\times E)) 为非空闭 resolvent 关系的 Attouch–Wets 空间。固定输入 (x_0)，定义

\[
\mathcal A_{x_0}=\{\Gamma:\Gamma(x_0)\ne\varnothing\},\qquad
C_m=\{\Gamma:\Gamma\cap(\{x_0\}\times\overline B_m)\ne\varnothing\}.
\]

则

\[
\mathcal A_{x_0}=\bigcup_{m\ge1}C_m,
\qquad C_m\text{ 闭且无处稠密}.
\tag{4.1}
\]

**闭性。** 被命中的集合为固定紧集，命中点可抽收敛子列并进入极限闭图。

**无内点。** 有限点关系在有限维 AW 空间稠密：对有限个观察球，取所有影响距离函数的有界图点的有限网；观察球以外的高权项由 AW 级数尾控制。再将有限个输入坐标任意微移以避开 (x_0)。这样得到任意近但不属于 (C_m) 的闭关系。

若固定精确解集 (S) 且 (x_0\notin S)，以

\[
\Delta_S\cup\{\text{有限个近似图点}\}
\]

作逼近，微移有限点同时避开输入纤维 (x_0) 和额外对角点，结论仍成立。

**含义。** 固定步长、必须能从 (x_0) 开始的 RLEB 和 LT 类都会因为共同的可解性门槛第一纲。该结论不能区分理论强弱，也不否定它们在良定子空间中的巨大差异。

**判级。** 在这个固定口径中真的是无鉴别力障碍。合理修复是将闭图空间保留为本体层，实际比较转入事先规定、无 RLEB/LT 标签的完整良定图表。不能声称原 AW 最外层上的泛型优势已得证。

## 5. O3：单步拓扑与全时间拓扑确实回答不同问题

先看闭性：(K=[0,1]\times[-1,1])、(S=[0,1]\times\{0\})，

\[
T_j(s,r)=(s,-(1-1/j)r)\longrightarrow T(s,r)=(s,-r).
\]

每个 (T_j) 的轨道一致趋于 (S)，极限却有二周期。所有映射精确固定同一个 (S)。这只证明单步度量不完备/类不闭，**不证明该类不 Baire**。

更强的反例可把极限也保留在一致收敛类。令 (K=[0,1]^2)、(S=[0,1]\times\{0\})，(0<\varepsilon<1/4)，

\[
f_\varepsilon(r)=
\begin{cases}
(1-\varepsilon^2)r,&0\le r\le\varepsilon,\\
\varepsilon-\varepsilon^3+\varepsilon^2(r-\varepsilon),&\varepsilon\le r\le2\varepsilon,\\
r/2,&2\varepsilon\le r\le1,
\end{cases}
\]

\[
T_\varepsilon(s,r)=\bigl(\min\{1,s+\varepsilon r\},f_\varepsilon(r)\bigr),
\qquad T_0(s,r)=(s,r/2).
\tag{5.1}
\]

连接点连续，(0<f_\varepsilon(r)\le(1-\varepsilon^2)r) 对 (r>0) 成立。每个 (T_\varepsilon) 精确固定 (S)，且法向尾与切向剩余总和分别受

\[
(1-\varepsilon^2)^n,\qquad
\varepsilon^{-1}(1-\varepsilon^2)^n
\]

统一控制，所以每个映射均一致收敛。但是

\[
\|T_\varepsilon-T_0\|_K\le\frac{\sqrt5}{2}\varepsilon\to0.
\]

从 ((0,\varepsilon)) 出发，切向累计增量为

\[
\sum_{n\ge0}\varepsilon^2(1-\varepsilon^2)^n=1.
\]

故 (\Pi_{T_\varepsilon}(0,\varepsilon)=(1,0))，而 (\Pi_{T_0}(0,\varepsilon)=(0,0))，从而 (d_{\rm dyn}(T_\varepsilon,T_0)=1)。

**可用条件桥。** 在同一个实际尾层 (\mathfrak D_e) 内，单步收敛给每个有限次迭代收敛，且对 (n\ge N)，

\[
\|T_j^n-T^n\|_K
\le 2e_N+\|T_j^N-T^N\|_K.
\tag{5.2}
\]

先取 (N) 再取 (j)，便得到全时间收敛。所以共同尾层上可以比较同一个拓扑；没有共同尾则不行。

**判级。** 真 no-go，不是“尚未找到巧妙证明”。可以选一种拓扑，或证明专门的桥，但不能称两者天然等价。

## 6. O4：RLEB 相对类可能自第一纲

令

\[
K=[-1,1]\times[0,1],\qquad S=[-1,1]\times\{0\},
\]

考虑所有连续一步回缩

\[
\mathscr M=\{T\in C(K,S):T|_S=I\}.
\]

它是非空闭凸完备 (C^0) 空间；所有对象都满足相同的一步终止尾。用完整源图 (1.2) 实现：全部非空输出纤维都落在 (S)，所以真实 EB 左端为零。

在该图卡中，存在 all-pairs RLEB-direct/energy 证书的对象类正好是具有某个正 Hölder 指数的回缩类 (\mathscr H)。必要性来自 reflector RL；充分性来自真实 EB 恒为零，可以把规范 gauge 常数选得足够小以达到严格兼容。

令

\[
H_{m,n}=\{T\in\mathscr M:\|Tz-Tw\|\le n\|z-w\|^{1/m}\ \forall z,w\in K\}.
\]

适当放大常数可得 (\mathscr H=\bigcup_{m,n\ge1}H_{m,n})。每个 (H_{m,n}) 闭，却在 (\mathscr H) 中没有相对内点：

1. 任意 Hölder 回缩 (T) 可由保持底边恒等和值域 (S) 的分片仿射回缩 (G) 一致逼近。
2. 与 (P_0(x,y)=((1-y)x,0)) 作任意小凸混合，在内点 ((0,1/2)) 附近留出输出不碰 (S) 端点的余量。
3. 在该内点附近第一输出坐标加入 (\eta\chi(x,y)|x|^\beta)，其中 (0<\beta<1/m)、(\chi) 为支集离开底边的 Lipschitz cutoff。小振幅保持回缩、值域和邻域；所得映射仍 (\beta)-Hölder，但沿水平线不再 (1/m)-Hölder。

故

\[
\mathscr H\text{ 在自身相对 }C^0\text{ 拓扑中第一纲}.
\tag{6.1}
\]

于是它的每个子集都在它里面第一纲，包括 LT、RLEB 全体及 RLEB\(\setminus\)LT。某集合及其补集甚至可同时第一纲、同时余稀。

**这没有证明整个研究的所有 RLEB 对象必自第一纲。** 它严格否定的是“只要 RLEB 是 (F_\sigma)，证明 LT 在其中第一纲就足够”。

**判级。** 对无条件相对纲解释是真 no-go。可绕过方式是先证明所用 RLEB 分母非空且 Baire，或在中立 Baire 母空间内同时判定 (\mathscr R,\mathscr L,\mathscr R\setminus\mathscr L) 的绝对类别。

## 7. O5：描述集合编码和投影的极限

### 7.1 可描述性不等于大小

(\mathbb R=\bigcup_n[-n,n]) 是 (K_\sigma)，但非第一纲；(\mathbb Q) 是 (F_\sigma)，但自第一纲。所以对象侧 (F_\sigma/K_\sigma) 编码只把问题化为闭/紧块的内点问题，没有自动解决它。

一个有用诊断定理是：若度量空间 (Z=\bigcup_n K_n)、每个 (K_n) 紧，且 (Z) 是 Baire，则

\[
\bigcup_n\operatorname{Int}_ZK_n
\quad\text{在 }Z\text{ 中开且稠密}.
\tag{7.1}
\]

否则某非空开集会被可数个相对闭无处稠密集覆盖。因此 (K_\sigma) 的 Baire 对象类必须在稠密开集上局部紧。反过来，若 (K_\sigma) 类处处非局部紧，则它自第一纲。这是可交给数学家团队优先检查的结构判据；当前尚未证明目标中立 RLEB 类满足哪一边。

### 7.2 即使投影连续且开放，也不保持任意见证子集的第一纲

令 (p:\mathbb R^2\to\mathbb R)、(p(x,y)=x)。横轴 (C=\mathbb R\times\{0\}) 闭无处稠密，但 (p(C)=\mathbb R)。这精确模拟“每个算子至少一个证书，但证书关系在总空间很薄”。

若 (p:X\to Y) 是 Polish 空间间连续开放满射，且 (A\subset Y) 有 Baire 性质，才有

\[
A\text{ 第一纲}\iff p^{-1}(A)\text{ 第一纲}.
\tag{7.2}
\]

这里必须是完整饱和逆像，不是任意满足关系 (C\subset X)。仅有连续满射也不够：取 (X=\mathbb R\sqcup\{*\})，令 (p|_{\mathbb R}=I,p(*)=0)。底层 ({0}) 第一纲，其逆像包含孤立开点而非第一纲。

### 7.3 所有初值逐点收敛的复杂度尚未精确解决

在单步 Polish 空间里，局部一致收敛可写成

\[
\bigcap_m\bigcup_N\bigcap_{p,q\ge N}
\{T:\|T^p-T^q\|_K\le1/m\},
\]

即 (\Pi^0_3) 上界；对全部初值逐点收敛直接只有 coanalytic 上界，因为再加了不可数 (\forall x)。这不是非 Borel 或 coanalytic-complete 的证明。

**判级。** 编码路线可继续，但其成功验收是“给出了真正的对象类”，不是“证明覆盖更大”。需另证内点、密度、范畴保持或复杂度下界。

## 8. O6：统一收敛层有真实的解集拓扑限制

若 (T^n\to\Pi_T) 在 (K) 上一致，(T|_S=I) 且极限落在 (S)，那么 (\Pi_T:K\to S) 是连续回缩。因此 (S) 必须是 (K) 的连续回缩像。

最小模型：(K=[0,1])、(S=\{0,1\})。没有连续回缩，故任何 (e_n\to0) 的共同尾层都为空。然而

\[
T(x)=2x-x^2
\]

精确固定 (S)，所有轨道逐点收敛：(0) 固定，(x>0) 趋向 (1)。故逐点收敛世界非空，而统一回缩世界为空。

即使 (S) 凸且非单点，逐点极限也可不连续。在 (K=[0,1]^2) 上

\[
T(s,r)=\bigl(\min\{1,s+r\},r/(1+r)\bigr)
\]

给 (r_n=r/(1+nr))；当 (r>0) 时切向累计和发散，极限为 ((1,0))，当 (r=0) 时极限为 ((s,0))。

到解集收敛也不等于点收敛：在 (K=\overline{\mathbb D}\times[0,1])，

\[
T(z,r)=(e^{ir}z,r/(1+r))
\]

的法向距离趋零，但 (z\ne0,r>0) 时角增量趋零、总角无界，轨道绕行不收敛。

**判级。** 连续回缩的几何阻碍是真不可能定理。若理想分母是所有逐点收敛 PPA，不能不说明就替换为局部一致收敛/连续极限回缩类；二者应为体系内不同层。

## 9. O7：同尾与同域，不是共轭运输的附赠品

### 9.1 固定尾对任意小全时间扰动也不开放

取 (K=[-1,1]\times[0,1])、(S) 为底边，(P(x,y)=(x,0))。定义

\[
T_{\varepsilon,a}(x,y)=(x,a\min\{y,\varepsilon\}),\qquad0<a<1.
\]

所有映射都精确固定 (S)，一致收敛，而且

\[
d_{\rm dyn}(T_{\varepsilon,a},P)\le\varepsilon,\qquad
\sup_Kd(T_{\varepsilon,a}^nz,S)=\varepsilon a^n\quad(n\ge1).
\tag{9.1}
\]

给定任意尾 (e_n\downarrow0)，选 (N) 使 (e_N<\varepsilon/2)，再选 (a^N>1/2)，就得到 (T_{\varepsilon,a}\notin\mathfrak D_e)。因此“全时间很近”仍不意味着保持同一坐标逐项尾预算。

### 9.2 现有共轭只给放宽尾

完整图共轭

\[
G^h=L_\lambda^{-1}(h\times h)L_\lambda G,
\qquad T^h=hTh^{-1}
\]

在 (h) 保持初值域、工作域并固定 (S) 时精确运输轨道。如果 (\operatorname{Lip}h\le1+\eta)，只可普遍推出

\[
\mathfrak D_e\longrightarrow\mathfrak D_{(1+\eta)e}.
\tag{9.2}
\]

从较小层 (\mathfrak D_{e/(1+\eta)}) 出发可以落回 (\mathfrak D_e)，但“较小层稠密”没有证明，且无条件版本甚至可能为空：取 (e_0=\sup_Kd(x,S)>0)，(e_n=0) 对 (n\ge1)，投影 (P) 可在 (\mathfrak D_e) 中；而 (\mathfrak D_{e/(1+\eta)}) 因 (n=0) 的距离约束不可能满足而为空。去掉初段约束或允许有限时间移位已改变原命题，必须显式说明。

### 9.3 原工作域与缩小 germ 不是同一认证类

若新构造只能在依赖扰动尺度的小邻域满足严格 RL/EB，就证明了“存在某局部 germ 的认证”，没有证明预先固定宏观工作域上的认证。现有原图实步长 (F_\sigma) 编码也主要是固定锚点、允许缩域的 germ 口径；不能将其当作冻结大域、同一实际尾、全部输出迹的完整分类。

**判级。** 尾稳定性反例是真 no-go；所需“有余量对象的适当稠密性”或“同尾局部替换”仍可能在非退化分层成立，是构建性瓶颈。应提交给数学家团队，而非默认已经解决。

## 10. O8：步长谱可任意紧，不是缺少一条连续性估计

任给非空紧集 (A\subset(0,\infty))，取 (C>\max\{1,\max A\})，令

\[
\operatorname{gph}F_A=\{(u,u):u\in\mathbb R\}\cup H_A,
\]

\[
H_A=
\left\{\left(
\frac{Ct(1+t)}{d(t,A)},
-\frac{C(1+t)}{d(t,A)}
\right):t>0,\ t\notin A\right\}
\cup\{(0,-C/\min A)\}.
\tag{10.1}
\]

**闭图。** (t\to A) 时图点逃向无穷；(t\to\infty) 时第一坐标趋无穷；(t\downarrow0) 的唯一有限极限已加上。零集精确为 ({0})。

对共同输入域 (U=(-1,1))：

- 若 (\lambda\in A)，额外分支输入的绝对值为
  \[
  C(1+t)\frac{|t-\lambda|}{d(t,A)}\ge C>1,
  \]
  端点输入绝对值也至少为 (C)，故完整 (J_{\lambda F_A}(x)=x/(1+\lambda)) 在 (U) 上成立。
- 若 (\mu\notin A)，取 (t=\mu)，额外分支输入为零、输出非零；基线同时给输出零，故 (J_{\mu F_A}(0)) 多值。

因此

\[
\Lambda_{\rm wp}^{U}(F_A)=A.
\tag{10.2}
\]

额外残差范数满足

\[
\frac{C(1+t)}{d(t,A)}\ge\frac C{\max\{1,\max A\}}>1,
\]

故近零 (r_{F_A}(u)=|u|)。每个 (\lambda\in A) 都有原 (F=I) 的严格局部 LT 接口；若 (A\subset(1,\infty))，也有 (\gamma=1,L=1,\psi(t)=t,\kappa=1/\lambda<1) 的严格 direct 接口。取直积 (widehat F(p,u)=\{0\}\times F_A(u)) 可令零集为非点仿射线。

选择 (A=\{\sqrt2\}) 即得到只有无理良定步长；选择 Cantor 紧集即得到无区间的谱。

**精确范围。** 这是共同局部输入域上的完整良定谱，不是全空间全输入的良定谱，也不是全部选择收敛谱。

**判级。** “局部严格证书自动给开步长窗口”已被否定。可通过实步长紧参数闭块投影绕过有理化；若确需谱开性，必须加入一致 properness/远端纤维排除等新结构。它不自动证明存在步长认证类非 Borel。

## 11. O9：局部算法与完整残差之间存在信息缺口

### 11.1 完全相同的局部全时间动力学，不同真实残差

取 (E=\mathbb R^2\)、(\lambda=1\)、(S=\mathbb R\times\{0\}\)、(U=\mathbb R\times(-1,1)\)。令

\[
F_0(p,r)=\{(0,-19r/9)\},
\]

\[
\operatorname{gph}F_1=\operatorname{gph}F_0
\cup\{((0,4/5),(0,3/10))\}.
\tag{11.1}
\]

新增图点的 proximal 输入为 ((0,11/10)\notin U)，故两者在整个 (U) 的完整 resolvent 都是 (T(p,r)=(p,-9r/10))，所有局部轨道与实际尾完全相同。但在实际输出 (u_0=(0,4/5)=T(0,-8/9)) 上，

\[
r_{F_0}(u_0)=76/45,\qquad r_{F_1}(u_0)=3/10.
\tag{11.2}
\]

因此 (F\mapsto T|_U) 不单射，并丢失真正的 EB 信息。只有全域完整 (T) 才能用全逆纤维唯一恢复 (F)。

反过来，局部原图 germ 也不决定完整局部 resolvent：(F_0=I) 与 (\operatorname{gph}F=\operatorname{gph}I\cup\{(1,-1)\}) 在 ((0,0)) 小图邻域一致，但 (J_F(0)=\{0,1\})。

### 11.2 可用的最弱 collar 修复

若 (V\Subset U\)、(\delta=d(V,E\setminus U)>0\)，则对 (u\in V)，

\[
(u,v)\in\operatorname{gph}F,\quad\|v\|<\delta/\lambda
\quad\Longrightarrow\quad u+\lambda v\in U.
\tag{11.3}
\]

所以影响内侧输出域上最小残差的所有足够小纤维都在完整输入图表中；较大残差可以用有限输出半径补界。无需禁止全部远端纤维，但必须保留原图或证明这个小残差覆盖。

**判级。** 信息缺口是真 no-go；双 collar 是可绕过工具。全纤维 EB 粘合仍须对新算子重新证明，不能只看选中轨道残差。

## 12. O10：保留残差阶与破坏 LT 的目标可能代数不相容

### 12.1 双侧保真共轭不能爆破线性位移

若同胚 (h) 固定 (S)，完整 transition 与解集距离满足

\[
\|h(x)-h(Tx)\|\le b\|x-Tx\|,
\qquad d(hx,S)\ge a\,d(x,S),\quad a>0,
\]

则 (T^h=hTh^{-1}) 满足

\[
\frac{\|T^h(hx)-hx\|}{d(hx,S)}
\le\frac ba\frac{\|Tx-x\|}{d(x,S)}.
\tag{12.1}
\]

若 (T) 为 Lipschitz 且固定 (S)，右侧至多 (\frac ba(1+\operatorname{Lip}T))，因可与最近解点比较。现有小位移保真条件给 (a=1-\varepsilon,b=1+2\varepsilon)。因此这种变形不能制造用于排除任意步长 LT 的无界 linear-displacement。

这只否定“使用该位移判据的此种保真变形”，不否定其他非 LT 机制。

### 12.2 (gamma<1) 严格兼容本身要求非线性残差下界

设 (L>0,0<\gamma<1)。direct 兼容式

\[
\psi\!\left(\frac{t+Lt^\gamma}{2\lambda}\right)\le\kappa t
\]

由 (\psi) 单调可推出小尺度 (\psi(r)\le C r^{1/\gamma})。配合真实 EB (d(u,S)\le\psi(r_F(u)))，得到

\[
r_F(u)\ge c,d(u,S)^\gamma.
\tag{12.2}
\]

energy 兼容式

\[
\tfrac12(t^2+L^2t^{2\gamma})
\le q_E\{t^2+\lambda^2[\psi^{-1}(t)]^2\}
\]

也因 (t^{2\gamma}\gg t^2) 给同样的下界。若存在 (u_j\to S)、(d(u_j,S)>0)，且

\[
r_F(u_j)\le C_0d(u_j,S),
\tag{12.3}
\]

则 (12.2) 不可能：(d^{1-\gamma}\to0)。

最小模型是 (T(y,z)=(y,qz))、(0<q<1)，其完整算子为

\[
F(y,w)=\{(0,(1-q)w/(\lambda q))\},\qquad
r_F=\frac{1-q}{\lambda q}d(\cdot,S).
\]

只保留这个线性残差阶、同时把单步粗化到非 Lipschitz，可能同时失去 LT 和所有 (gamma<1) 的严格 RLEB 证书。现有正常幂压缩构造能越过此障碍，正因为它放弃距离/残差阶双侧保真，并利用非退化切向漂移重新建立全纤维 EB；不是因为插入任意尖点都有效。

**判级。** 这是真结构不相容定理。若坚持同一残差阶又依靠位移爆破，路线应停止；若允许内生残差几何改变，则需建立其与中立层位置、共同尾的联系。

## 13. O11：结构层的“多数”不是母空间的“多数”

横轴在 (\mathbb R^2) 中无处稠密，却在横轴自身中为全体。更一般，连续嵌入 (Y\hookrightarrow X) 不会将 (Y) 中余稀集合自动变成 (X) 中非第一纲集合。连续包含 (\mathfrak D_e\subset\mathfrak D_{e'}) 也一样。

现有正常收缩—非退化漂移层的条件形如

\[
c,d(x,S)\le\|P_S(Tx-x)\|,
\qquad d(Tx,S)\le q,d(x,S),\qquad q<1.
\tag{13.1}
\]

在其加权导数拓扑中有开函数族，并不推出它在中立 AW、(C^0) 或共同尾空间中开、稠密、非第一纲。尤其正常收缩本身已经提供一部分动力学信息，比较时必须说清这一后置层被何种内生性质选出。

**这就是当前最接近理想目标、但尚未补上的桥：**

- 判定结构层在事先冻结中立空间中的闭包、内部与类别；或
- 不依赖该结构层，直接对中立空间的每个相关开集给对象侧修改；或
- 给一个明确的范畴保持投影/开放映射，使合法饱和类的结论可转移；或
- 证明转移不可能，改为体系内分区分类，而不再追求一句全局排序。

**判级。** 尚未解决，不是已证明不可做。继续制造结构层内的反例不会自动补上这条桥。

## 14. O12：有限维状态与无限维算子空间不能混同

状态空间 (E=\mathbb R^d) 已经产生无限维的函数/算子空间，足以开展泛函分析和 Baire 分类。若把状态空间进一步换成 Hilbert，现有证明有真正失效点：

### 14.1 闭纤维的最小范数未必取得

在 (ell^2) 中，

\[
C=\{(1+1/n)e_n:n\ge1\}
\]

范数距离到零为一，但无最小范数点。可令一个闭图关系的某纤维为 (C)。因此必须保留 (r_F=\inf)，不能直接选最小范数图点。对连续单调 gauge，取 inf 的极限仍可处理一些 EB 不等式。

### 14.2 AW 闭集空间通常不再可分

对每个 (A\subset\mathbb N)，令 (C_A=\{0\}\cup\{e_n:n\in A\})。若 (A\ne B)，在某个 (e_n) 上二者距离函数相差一。单位球上存在不可数一致分离族，所以有限维 Polish 论证不能原样使用。

### 14.3 有界一致收敛不保证有限迭代连续

取 (delta_n\downarrow0)，在 (a_n=e_n+\delta_ne_1) 的半径 (\delta_n/3) 小球上放高度一的连续 bump，支集两两分离且局部有限，得到连续有界 (f:ell^2\to[0,1])，满足 (f(e_n)=0,f(a_n)=1)。设

\[
T(x)=x+f(x)e_1,\qquad T_n(x)=T(x)+\delta_ne_1.
\]

则 (T_n\to T) 甚至全域一致，但

\[
T^2(e_n)=e_n,\qquad T_n^2(e_n)=e_n+(1+2\delta_n)e_1.
\]

所以平方迭代在有界一致拓扑下不连续。有限维中的紧球和统一连续性承担了实际工作。

**判级。** 无条件 Hilbert 推广被反例否定；若要推广，需要在有界集上统一连续/有界性、不同图拓扑或弱紧机制下重新建空间。这不应阻塞有限维状态、无限维算子空间上的主比较。

## 15. 给数学家团队的可验收问题，而非继续试零散尖点

### Q1：先判定目标分母是否有实质 Baire 性

在事先指定的无标签良定/收敛空间 (X) 中，定义实际 RLEB 对象像 (\mathscr R\) 和 LT 对象像 (\mathscr L)。接受 energy 嵌入已解决可比接口后，问：

\[
\mathscr R\text{ 是否 Baire，或是否在某非空开 }O\subset X\text{ 内非第一纲？}
\]

如已知 (K_\sigma)，优先检查局部紧结构 (7.1)。若 (\mathscr R) 自第一纲，应报告这一体系结论，而不是继续把相对纲用作强弱分数。

### Q2：对象侧同层修改引理，或其失败分类

对一个已冻结且非退化的中立层 (X=\mathfrak D_e)，每个 LT 必要闭块 (L_j)，能否对所有

\[
T\in\mathscr R\cap L_j,quad\varepsilon>0
\]

找到 (U\in\mathscr R\cap X\setminus L_j)、(d_X(T,U)<\varepsilon)，同时保完整图、exact (S)、同实际初值域、同尾、真实全纤维 EB 与严格兼容？这才是无内点定理需要的量词。

若不能，应找使 (L_j\cap\mathscr R) 有相对内点的动力学结构；该反定理同样是理想体系的成果。

### Q3：跨尺度范畴转移

已能做到 (\mathfrak D_e\to\mathfrak D_{(1+\varepsilon)e})。能否建立开放/范畴保持的尺度组织，而非普通连续包含？实际尾可用内生坐标

\[
w_n(T)=\max\left\{
\sup_{k,\ell\ge n}\|T^k-T^\ell\|_K,
\sup_{k\ge n}\sup_Kd(T^k\cdot,S)
\right\},
\]

并有 (\|w(T)-w(U)\|_{\ell^\infty}\le2\sup_n\|T^n-U^n\|_K)。但连续坐标本身仍不保证类别转移，所需映射性质必须另证。

### Q4：不把残差几何视为附属估计

能否从内生图/轨道不变量识别哪些中立层允许 (12.2)，哪些强制 (12.3)，并据此分区比较 LT 与 RLEB？这会把“为什么 RLEB 能认证粗糙动力学”上升成结构判别，而不是事后挑一个尖点例子。

### Q5：步长与局部域投影的范畴，而不仅是 Borel 编码

已知紧参数编码可避免错误有理化。剩余问题是：存在实步长、存在局部域的对象像是否有可用的内点/范畴保持定理？不允许将每个固定步长切片的结论直接取并。

**总终判。** 没有证明理想目标做不到；已经证明几条最直接的“从局部构造跳到总体大小”的捷径做不到。需要数学家介入的主要是中立空间的相对 Baire 结构、同层逼近/反逼近、完整残差几何与范畴投影四类问题，而不是再补几条孤立反例。

## 16. 已核对的内部来源及边界

- `ppa_system_team/01_ambient_axioms.md`：完整 resolvent 表示、局部图表、两种拓扑与后置层。
- `ppa_system_team/02_convergence_topology.md`：单步/全时间差异、逐点/局部一致复杂度、共同尾桥。
- `ppa_system_team/06_resolvent_family.md`：选择与策略量词、全族相容、局部图块问题。
- `ppa_system_team/08_architecture_audit.md` §4：最大 AW 空间一步可解第一纲、同一一致收敛层内拓扑反例。
- `ppa_classification_team/01_frozen_denominator.md` §3：相同局部算法不同真实残差。
- `ppa_classification_team/02_structural_deformation.md` §§1–2、8–9：完整共轭、双侧保真 no-go、残差阶约束与范围。
- `ppa_classification_team/03_object_category.md` §§7–8：对象侧修改引理、(K_\sigma)–Baire 诊断。
- `ppa_classification_team/04_step_spectrum.md`：任意紧局部谱与实步长闭块编码的口径。
- `ppa_classification_team/05_obstruction_audit.md` §§1–9：尾层、RLEB 自第一纲、任意紧谱、双 collar、Hilbert 反例。

本报告独立复算了上述最小模型和逻辑推断；没有因此重证所有基础架构、所有 RLEB/LT 证书转换或文献优先权。尤其“(F_\sigma/K_\sigma) 已完成”的引用范围必须维持原稿的固定紧图卡或局部 germ 条件，不可扩大成全部宏观原图认证类。
