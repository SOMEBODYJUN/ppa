# RLEB–Luke–Tam 理想比较计划：给数学家团队的技术交接

日期：2026-09-20。版本：交接初稿，供独立审阅与选题讨论。

本稿完整读取 `ppa_system_team/01–10`、`ppa_classification_team/01–07`、`comparison_space_team/09`。原 RLEB 论文作为已经建立的基础，本次仅使用下述接口，不重新审查无关结果。文内“已核”指既有团队报告给出了证明并经所列交叉审计，不表示外部同行评审或原创性清关已经完成。

## 0. 一页结论：理想问题尚未回答，现有建议只是有条件的支线

作者希望研究的是：**先建立一个不偏向任何证书的 PPA 算子／动力系统空间，再由结构定理比较 RLEB 与 Luke–Tam 的可认证对象类。** 重点不是再得到一个非 Lipschitz 算子，也不是在预先选好的 Hölder 球、尖点层或参数族内证明 Lipschitz 成员很少。

当前准确状态如下。

1. 中立本体、良定图表、轨道、收敛及证书五层体系已有可工作的有限维单值主干；其完备性、Polish 性、完整图坐标与若干嵌入定理经范围内审核。
2. LT 公共 all-pairs 收敛证书进入 RLEB-energy 已经解决。包含号不是当前困难。
3. 中立体系中的总体类位置、差集大小、相对 Baire 性及跨层转移尚未解决。现在不能断言“典型 RLEB 不是 LT”，更不能将特殊层的余稀结论提升为全体系结论。
4. “先做仿射解集＋正常收缩＋非退化切向漂移”的建议只有在同时证明该结构层的母空间位置和跨层桥梁时，才推进理想比较。**若只完成层内构造，即使是无限维函数层，也仍然是受限子类结果；不能作为理想问题的答案。**
5. 目前没有证明理想方向不可能；已经证明的是若干过强的普遍命题或简单路线不成立。有些障碍是比较语言本身需要改进，有些是精确的数学 no-go，有些是尚缺构建引理。必须分别处理。

本次请数学家团队优先解决的不是“怎样再造粗糙算子”，而是：

> 在保留完整原算子、共同算法语义和中立拓扑的前提下，什么结构不变量及非退化分层能有鉴别力地比较两种认证理论？是否存在从局部可构造层到整个中立收敛类的表示、分解或范畴保持定理？若不存在，能否证明并刻画其刚性边界？

“比 LT 多”至少有四种不同强度：严格多出成员；差集在某中立区域非第一纲；某区域中 RLEB 余稀而 LT 第一纲；在一个覆盖性／转移性得到证明的分层族中出现一致优势。目前只有受限结构层达到第三种，尚未获得第四种。

### 状态标记

- **[E] 已证／已核：**准确范围内已有证明和交叉复核。
- **[N] 已证阻断：**具体公式或反例否定了一条明确命题，不等于否定整个研究。
- **[O] 开放：**尚未证明，也未否定。
- **[D] 设计选择：**需给出与科学问题相匹配的数学定义；不能冒称已存在唯一自然答案。

## 1. 研究愿景与不可接受的降级

### 1.1 理想问题

选择一个独立于 RLEB／LT 的空间 \(\mathfrak M\)，其成员是完整 PPA 实例或使其收敛的完整算子。对共同接口定义

\[
\mathcal L=\{F\in\mathfrak M:\text{存在有效 LT 证书}\},\qquad
\mathcal R=\{F\in\mathfrak M:\text{存在有效 RLEB-direct 或 energy 证书}\}.
\tag{1.1}
\]

先证明这两个对象类的结构落位，再研究

\[
\mathcal L,\quad\mathcal R,\quad\mathcal R\setminus\mathcal L,
\quad\mathfrak M\setminus\mathcal R
\tag{1.2}
\]

的内部、闭包、稠密性、纲及性能不变量。结论可以是不同机制分区，可以是双方都第一纲，也可以是 RLEB 差集具有真正厚度；不预设唯一正确答案必须为 LT 第一纲。

### 1.2 不得用以下内容替代主问题

- 不把某个尖点、固定指数 Hölder 球或预置超吸引层改名为总母空间。
- 不把“反例排除了 LT”当成“LT 在总空间占小类”。反例只能否定包含或测试假设。
- 不把一个无标签对象的多份证书、多个步长或多条轨道重复统计。
- 不以裁剪原图实现局部化后，继续声称比较的是同一个原算子。
- 不把局部 germ 证书缩域后的成功，冒充原来固定宏观吸引域、证书域及尾预算上的成功。
- 不为获得 Baire 性任意强化拓扑，再把结论译回原 AW／单步拓扑。
- 不将第一纲理解为零测、零概率或某个覆盖百分比。
- 不将“大”直接等同于“好／新”：算法保证、条件可核验性及优先权仍须分别评价。

允许使用构造、扰动和反例作为证明工具，但它们必须服务于已经冻结的整个空间命题，不能代替空间命题。

## 2. 五层体系与固定符号

首阶段采用 \(E=\mathbb R^d\) 及其原欧氏范数。状态空间有限维并不使算子空间有限维。一般 Hilbert 推广仍有额外障碍，见 §6.10。

| 层 | 对象／性质 | 不可遗忘的数据 |
|---|---|---|
| 本体 | 非空闭图 \(G=\operatorname{gph}F\subset E\times E\) | 全部图点、全部纤维、原零集 |
| 良定图表 | 完整 \(J_{\lambda F}|_U=T_G\in C(U,E)\) | 原全图仍在；\(T_G\) 不是选值标签 |
| 算法与轨道 | \((F,\lambda)\)、\((F,(\lambda_k))\)，或指定策略族 | 初值域、工作域、存在／全部分支、非阻塞 |
| 动力学 | 点收敛、局部一致收敛、实际尾、有限长度、极限选择 | 原范数；共同初值与轨道量词 |
| 证书像 | direct、energy、LT all-pairs、另列 pointwise LTT | 对象一次计数；理论标签不进入母空间定义 |

### 2.1 完整图坐标

对 \(\lambda>0\)，令

\[
L_\lambda(u,v)=(u+\lambda v,u),\qquad
\Gamma_{F,\lambda}=L_\lambda G=\operatorname{gph}J_{\lambda F}.
\tag{2.1}
\]

在共同开输入域 \(U\) 上“完整单值”意味着

\[
\Gamma_{F,\lambda}\cap(U\times E)=\operatorname{gph}T_G,
\tag{2.2}
\]

而非仅有 \(T_G(x)\in J_{\lambda F}(x)\)。

同一原图的全部 resolvent 关系满足

\[
y\in J_{\lambda F}(x)
\iff y\in J_{\mu F}\!\left(
\frac\mu\lambda x+\left(1-\frac\mu\lambda\right)y\right).
\tag{2.3}
\]

全域连续单值 \(T\) 在固定步长唯一恢复完整原图：

\[
F_{T,\lambda}(u)=\{(x-u)/\lambda:Tx=u\}.
\tag{2.4}
\]

纯局部 \(T|_U\) 一般不能恢复原 \(F\)。

### 2.2 冻结的共同规格

采用

\[
P=(E,U,S,\lambda,B,W,H,R),
\tag{2.5}
\]

其中 \(S\subset U\) 非空闭、通常非单点；\(\operatorname{zer}F=S\)；\(B\subset W\Subset U\)，\(B,W\) 紧；\(B\) 是初值块而非默认前向不变域；\(W\) 是所有 B-轨道的共同工作区。

对 all-pairs 与最近解比较，取

\[
H=W\cup\bigcup_{x\in W}P_Sx,\qquad
R\ge\max_{x\in W}d(x,S).
\tag{2.6}
\]

有限维下 \(H\Subset U\) 紧。定义

\[
\mathfrak A_P=
\{G:\text{满足 (2.2)、}\operatorname{zer}F=S\},
\]

\[
\mathfrak A_P^{B\rightsquigarrow W}=
\{G\in\mathfrak A_P:T_G^n(B)\subset W\quad\forall n\ge0\}.
\tag{2.7}
\]

若使用前向不变的紧自映射模型 \(T:K\to K\)，须声明完整原算子就是

\[
F_{T,K}(u)=\{(x-u)/\lambda:x\in K,Tx=u\}.
\tag{2.8}
\]

这是合法但不同的原对象图卡。不能从既有全局 \(F\) 删除外部图点后冒称 (2.8) 是无损坐标。

### 2.3 真残差

\[
r_F(u)=\inf\{\|v\|:(u,v)\in G\}.
\tag{2.9}
\]

有限维非空闭纤维时 inf 取得；空纤维取 \(+\infty\)。全域坐标中

\[
r_F(u)=\lambda^{-1}\inf_{Tx=u}\|x-u\|.
\tag{2.10}
\]

对某一个输入有 \(r_F(Tx)\le\|x-Tx\|/\lambda\)，但这不许可把后者当成前者。真实 EB 对整个纤维取 inf。

## 3. RLEB 与 LT 进入体系的最小完整接口

以下均配共同完整性与留域接口，所有域和尺度如 (2.5)–(2.6) 固定。记

\[
R_T=2T-I,\quad d=d(x,S),\quad d^+=d(Tx,S),\quad s_x=\|x-Tx\|.
\]

### 3.1 RLEB 两条证书通道

all-pairs RL：存在 \(0<\gamma\le1,L<\infty\)，使

\[
\|R_Tx-R_Ty\|\le L\|x-y\|^\gamma
\quad(x,y\in H,\ \|x-y\|\le R).
\tag{3.1}
\]

真实输出 EB：在被声明的输出域内，

\[
d(u,S)\le\psi(r_F(u)).
\tag{3.2}
\]

Direct 兼容：

\[
h(r)=\frac{r+Lr^\gamma}{2\lambda},\qquad
\psi(h(r))\le\kappa r,\quad0<\kappa<1.
\tag{3.3}
\]

Energy 兼容：\(\alpha=\psi^{-1}\) 为普通连续严格增逆 gauge，

\[
A(r)=\frac{r^2+L^2r^{2\gamma}}2,\qquad
V(r)=r^2+\lambda^2\alpha(r)^2,\qquad
A(r)\le qV(r),\quad0<q<1.
\tag{3.4}
\]

共同最近解比较给

\[
s_x\le\frac{d+Ld^\gamma}{2},\qquad
(d^+)^2+s_x^2\le A(d).
\tag{3.5}
\]

Direct 推出 \(d^+\le\kappa d\)；energy 推出 \(V(d^+)\le qV(d)\)。两者都推出距离非增，但一般 energy gauge 不自动给距离本身的 Q-线性因子。

共同初值距离 \(d(x,S)\le D\) 下，点尾可取

\[
e_n^D=\frac12\left(
\frac{\kappa^nD}{1-\kappa}
+\frac{L\kappa^{\gamma n}D^\gamma}{1-\kappa^\gamma}
\right),\qquad
e_n^E=\frac{q^{(n+1)/2}\sqrt{V(D)}}{1-\sqrt q}.
\tag{3.6}
\]

这些是保守认证尾，不一定等于系统真实尾。

### 3.2 LT 公共 all-pairs 口径

此处 LT 指 Luke–Tam 2025 的公共定量接口，不把所有早期 pointwise／relative-to-Fix／多值 LTT 合并进来。完整接口下几何为

\[
\|R_Tx-R_Ty\|\le\sqrt{1+4\tau}\|x-y\|,
\quad d(u,S)\le\rho r_F(u),
\tag{3.7}
\]

配严格门槛

\[
2\tau(\lambda+\rho)^2<\lambda^2.
\tag{3.8}
\]

可将负 violation 放宽到 \(\tau=0\)；\(\rho=0\) 的一步终止情形单列或按严格余量放宽成正常数。

取 \(\gamma=1,L^2=1+4\tau,\alpha(r)=r/\rho\) 得

\[
q_E=(1+2\tau)\frac{\rho^2}{\rho^2+\lambda^2}<1.
\tag{3.9}
\]

故同一完整自映射接口或已经对齐留域的固定规格中，

\[
\mathcal L_P\subseteq\mathcal R_{E,P}
\subseteq\mathcal R_{D,P}\cup\mathcal R_{E,P}=:\mathcal R_P.
\tag{3.10}
\]

该转换不自动逐项支配 LT 原先最优尾、最大初值域或所有历史 LTT 假设。它已经足够关闭本项目的主要包含问题，不应再把包含问题列为核心瓶颈。

## 4. 已证基础：哪些可以直接接着用

| 编号 | 已证命题 | 精确范围／依据 |
|---|---|---|
| E1 | 非空闭图 AW 空间完备；有限维时 Polish | `system/06` §3；`system/08` §3.2 |
| E2 | 完整原图、任一步长完整关系、相容全 resolvent 族同胚 | (2.1)–(2.3)；`system/06` §1–3 |
| E3 | 开输入域的完整连续单值原图类在原 AW 拓扑为 Polish／\(G_\delta\) | 不靠附加独立 T 标签强化拓扑；`system/01` §10、`system/08` §2.3 |
| E4 | exact-S 为 \(G_\delta\)；共同留域层相对闭；有限轨道评价连续 | `classification/01` §2、4 |
| E5 | 标准全时间拓扑下，逐初值收敛层完备／Baire；局部一致收敛层 Polish | 点态层可非可分；`system/02` §6 |
| E6 | 局部一致层有内生连续极限；前向不变且含 S 时为回缩，并给闭不变纤维商 | 纯初值 trace 只称局部极限映射；`system/01` §6 |
| E7 | 同一实际尾层相对闭／Polish；其 AW 和全时间拓扑相同 | `classification/01` §4–5 |
| E8 | direct／普通 energy gauge 可规范化；完整紧源图卡的认证像为 \(K_\sigma\) | 每块有共同模与尾；不是任意局部全图的无条件结论；`classification/03` §2–4 |
| E9 | 固定锚点、允许缩域的完整原图 germ 中，LT/direct/energy 存在实步长认证类均为 \(F_\sigma\) | 用实参数紧投影，不作有理步长替代；`classification/04` §7 |
| E10 | RLEB 距离非增＋S 局部仿射或 \(C^1\) 流形时，任意步长 LT 必有原步长线性位移界 | `classification/03` §5；没有给其必要层无内点 |
| E11 | 完整图受控共轭保持算法身份；有尾预算损失的运输定理 | `classification/02` §1–2 |
| E12 | 仿射非退化漂移层可变形为严格 RLEB 且任意步长非 LT | 仅局部突破；尾放宽和证书缩域尚未闭合，见 §7 |

其中标准表示、WPO、Baire、全时间拓扑原则有既有文献支点；当前不把这张表等同于十二项原创主定理。E8、E9、谱实现及变形的精确版本尚未完成独立优先权清关。

### 4.1 共同尾闭层及拓扑桥的精确形式

固定非增 \(\omega_n\downarrow0\)，在 (2.7) 中定义

\[
\mathfrak D_\omega(P)=
\{G:\|T_G^m-T_G^n\|_B\le\omega_n
\quad\forall m\ge n\ge0\}.
\tag{4.1}
\]

其统一极限属于 \(S\cap W\)，并有 \(\|T_G^n-\Pi_G\|_B\le\omega_n\)。对同层对象，

\[
\sup_{k\ge N}\|T_G^k-T_{G'}^k\|_B
\le2\omega_N+\|T_G^N-T_{G'}^N\|_B.
\tag{4.2}
\]

以原图兼容完备距离 \(\rho_{\mathfrak A}\) 加全时间轨道差，

\[
\rho_{\mathrm{dyn}}(G,G')=
\rho_{\mathfrak A}(G,G')+
\sup_{n\ge0}\min\{1,\|T_G^n-T_{G'}^n\|_B\},
\tag{4.3}
\]

得到保留完整本体的动态距离。(4.2) 保证它在同一 \(\mathfrak D_\omega(P)\) 上与 AW 同拓扑。不能删去基图项，否则局部动力完全相同的不同原图距离会变零。

## 5. 理想主问题的三个精确版本

三个版本不是相互替换的表述。请团队决定以哪一个为主，并为另两个给桥梁或不可转移结论。

### Q-AW：原算子图／单步几何中的类位置

在预先确定、非空的 \(\mathfrak A_P^{B\rightsquigarrow W}\) 中，用原 AW 相对拓扑比较 (1.2)。RLEB、LT 的定义不以已知收敛为前提；它们各自认证进入收敛层。

首先求

\[
\operatorname{int}\mathcal R_P,\quad
\overline{\mathcal R_P},\quad
\operatorname{int}\mathcal L_P,\quad
\overline{\mathcal L_P},\quad
\operatorname{Cat}(\mathcal R_P\setminus\mathcal L_P).
\tag{5.1}
\]

同样可以先不加留域，用更大的良定层作为总表，再后置动力分层。已知某些大 \(C^0\) 良定层中两者皆第一纲，故不能预设 (5.1) 必给单一优势。

有力的正目标是：存在**由中立内生性质确定**的非空相对开区 \(O\) 或有严格母空间定位的层 \(Z\)，使

\[
\mathcal R_P\cap O\text{ 非第一纲，}\qquad
\mathcal L_P\cap O\text{ 第一纲}.
\tag{5.2}
\]

若 (5.2) 不可能，也应证明其原因，并比较闭包、性能谱或其他细分类，不倒选有利空间。

### Q-DYN：全部收敛 PPA 中的认证覆盖与动力结构

在共同规格下定义

\[
\mathfrak C_{\mathrm{pt}}(P)=
\{G\in\mathfrak A_P^{B\rightsquigarrow W}:\forall x\in B,
\ T_G^n x\to\Pi_Gx\in S\},
\]

\[
\mathfrak C_{\mathrm{lu}}(P)=
\{G\in\mathfrak C_{\mathrm{pt}}(P):T_G^n|_B\to\Pi_G
\text{ 一致}\}.
\tag{5.3}
\]

以 (4.3) 的全时间拓扑为主；紧 B 时 lu 表示一致初值收敛，全局版用紧耗尽。分别比较 \(\mathcal R_P\)、\(\mathcal L_P\) 和差集在 (5.3) 中的绝对类别。若在 \(\mathcal R_P\) 内比较，先证明它自身非空 Baire或至少非自第一纲。

这一版本最接近“所有使 PPA 收敛的算子空间”，不预先规定收敛速度。但它研究的是**已收敛系统的可认证覆盖和结构**，不能再把母空间已经假定的收敛算成 RLEB 单独获得的优势。完整多值全选择版本尚未具有同等成熟的主干，不能把单值版说成无条件覆盖所有 PPA。

### Q-PROFILE：无标签、跨尾尺度的类别／性能剖面

在 \(\mathfrak C_{\mathrm{lu}}(P)\) 中定义唯一内生实际尾

\[
w_n(G)=\max\left\{
\sup_{k,\ell\ge n}\|T_G^k-T_G^\ell\|_B,
\sup_{k\ge n}\|d(T_G^k\cdot,S)\|_B
\right\}.
\tag{5.4}
\]

它非增趋零；在非截断轨道 sup 范数意义下有

\[
\|w(G)-w(G')\|_{\ell^\infty}
\le2\sup_{n\ge0}\|T_G^n-T_{G'}^n\|_B.
\tag{5.5}
\]

这里不用带 \(\min\{1,\cdot\}\) 的有界距离冒写全局 2-Lipschitz 数值；在该距离下保留连续性即可。对 (4.1) 的非增预算，\(w(G)\le\omega\) 与该尾层条件等价。

可记录

\[
\operatorname{Prof}_C(\omega)=
\left(
\operatorname{int}_{\mathfrak D_\omega}\mathcal C_C,
\overline{\mathcal C_C\cap\mathfrak D_\omega}^{\mathfrak D_\omega},
\operatorname{Cat}_{\mathfrak D_\omega}(\mathcal C_C\cap\mathfrak D_\omega)
\right),
\tag{5.6}
\]

同时登记 \(\mathfrak D_\omega\) 是否非空、非退化、在总收敛空间处于何种位置。\(\operatorname{Cat}\) 只是已证类别状态，不是新的数值测度。

需要的新定理是：这种剖面在 \(\omega\mapsto c\omega\)、有限时间平移、局部域变换下怎样迁移，哪些迁移足以涵盖实际关注的全部机制。仅仅列出 (5.6) 的记号尚未建立分类理论。

### 5.4 每个版本都必须固定的量词

“固定 \(\lambda\)”“存在某个 \(\mu>0\)”“每个 \(\mu\in I\)”“任意允许变步策略”是四个不同对象问题。存在步长的公平类可定义为同一个 F、同一域和尾条件下

\[
\mathcal C_{C,\exists\mu}(P)=
\{F:\exists\mu>0,
\ F\in\mathfrak D_\omega^{\mu}(P),
\ \text{在 }\mu\text{ 有 }C\text{ 证书}\}.
\tag{5.7}
\]

两理论均允许相同选择自由度时才直接比较。若专门给 LT 更多自由，则应比较
\(\mathcal R_{\lambda}\cap\mathcal C_{LT,\exists\mu}\)
在 \(\mathcal R_{\lambda}\) 中的位置，不写错误包含号。

## 6. 障碍清单：类型、精确公式及影响

### B1 [N／D] 最大闭图空间的可解性退化：不是“空间越大越公平”

在所有闭 resolvent 关系的 AW 空间中固定非解输入 \(x_0\)，

\[
\{\Gamma:\Gamma(x_0)\ne\varnothing\}
=\bigcup_{m\ge1}
\{\Gamma:\Gamma\cap(\{x_0\}\times\overline B_m)\ne\varnothing\}
\tag{6.1}
\]

是 \(F_\sigma\) 第一纲。各命中固定紧集的块闭；有限局部网可逼近原图，把有限输入坐标轻移避开 \(x_0\)，证明无内点。固定 exact-S 且 \(x_0\notin S\) 时，保留 \(\Delta_S\) 后结论仍成立。

因此固定步长下两理论在此最外层会共同因“一步有解”而变小，不能用这个标签排序。已证的是最外层不适合单独担当比较分母，**不是中立体系不可能**。良定层的必要性由算法语义支持。

### B2 [N／D] 大 \(C^0\) 层可使双方皆第一纲；相对 RLEB 又可自第一纲

在有内点的紧凸域 K、\(\operatorname{int}(K\setminus S)\ne\varnothing\) 的 exact-S 连续自映射层中，每个固定正 Hölder 指数及常数块闭无处稠密。故所有正 Hölder 映射、从而固定域上 all-pairs RLEB 和 LT 都第一纲。该结论未自动转移到收敛／同尾层。

更强警报来自完整中立的一步回缩层。令

\[
K=[-1,1]\times[0,1],\quad S=[-1,1]\times\{0\},\quad
\mathfrak M_{\rm ret}=\{T\in C(K,S):T|_S=I\}.
\tag{6.2}
\]

它是闭凸 Baire 空间，所有成员一步终止；完整原算子取 (2.8)，输出 EB 左端恒零。在该层中 RLEB 类恰为

\[
\mathfrak H=\bigcup_{m,n\ge1}
\{T:\|Tx-Ty\|\le n\|x-y\|^{1/m}\quad\forall x,y\in K\}.
\tag{6.3}
\]

每一块在 \(\mathfrak H\) 自身中无处稠密：先保持 S-trace 分片线性逼近，再在内点小区加入任意小、指数 \(\beta<1/m\) 的 Hölder 增量，仍在 \(\mathfrak H\) 但出该块。因此 \(\mathfrak H\) **自第一纲**。

在这样的分母内，每个子集都相对第一纲，“LT 在 RLEB 中第一纲”不能说明 LT 特别小。该反例不证明所有 RLEB 类均自第一纲；它证明默认相对 Baire 性是实际逻辑漏洞。

结构诊断：若 \(Z=\bigcup_jK_j\) 为 \(\sigma\)-紧 Baire 空间，则 \(\bigcup_j\operatorname{int}_ZK_j\) 稠密，因而 Z 在稠密开集上局部紧。若欲将 E8 的整个 RLEB \(K_\sigma\) 并类作为 Baire 分母，必须解释这种局部紧结构在哪里；不能只说“各预算块都紧，所以总并 Baire”。

### B3 [N／O] 精确尾预算不是无害 bookkeeping；任意慢率阻止可数穷尽

首先并非任意 \((K,S,\omega)\) 可实现。\(K=[0,1]\)、\(S=\{0,1\}\) 不存在连续回缩，所以一致收敛尾层为空，尽管 \(T(x)=2x-x^2\) 的每条轨道点收敛。

其次同尾约束可在统一收敛类内部处于边界。对 (6.2) 令

\[
P(x,y)=(x,0),\qquad
T_{\varepsilon,a}(x,y)=(x,a\min\{y,\varepsilon\}),\quad0<a<1.
\tag{6.4}
\]

其 exact-S 相同，且全时间距离至多 \(\varepsilon\)；但

\[
\sup_K d(T_{\varepsilon,a}^n z,S)=\varepsilon a^n\quad(n\ge1).
\tag{6.5}
\]

给定任意 \(\omega_n\to0\)，可选 N、a 使 \(\varepsilon a^N>\omega_N\)。所以即使离一步终止映射全时间任意近，也未必处于同一尾预算层。

给定任意严格下降 \(b_n\downarrow0\)，在节点上规定 \(f(b_n)=b_{n+1}\)，线性插值并令 \(f(0)=0\)，则 \(f\) 连续增、\(0<f(r)<r\)，且 \(\sup_{[0,b_0]}f^n=b_n\)。对任意预列可数尾表都可用对角化选一个不被其任一有限倍数最终支配的 \(b_n\)。

因此“每个对象有一个尾”不能变成“可数常用尾层穷尽全部对象”。跨尺度比较需要新桥，不是把 \(1+\varepsilon\) 忽略即可。

### B4 [N／O] RL、真实 EB 与严格兼容非独立，普通粗化／凸混合不保类

对 \(\gamma<1,L>0\)，direct 兼容迫使小尺度

\[
\psi(t)\le Ct^{1/\gamma},\qquad
r_F(u)\ge c\,d(u,S)^\gamma.
\tag{6.6}
\]

Energy 也由 \(r^{2\gamma}\) 主导 \(r^2\) 推出相同残差下界。因此若保留一列

\[
u_j\to S,\quad d(u_j,S)>0,\quad r_F(u_j)\le C d(u_j,S),
\tag{6.7}
\]

则任何 \(\gamma<1\) 严格兼容不可能。简单把 Lipschitz 变粗而保留线性残差阶，可能同时离开 LT 和 RLEB。

固定证书也不对凸混合封闭。取 \(\lambda=1\)，

\[
T_\pm(p,r)=(p\pm\sqrt{|r|},|r|/4),\qquad\psi(t)=t^2/4.
\tag{6.8}
\]

两者在充分小尺度有同一严格 RL/EB 证书。其平均
\(T_0(p,r)=(p,|r|/4)\) 若保留该 gauge，对正输入 r 就须有

\[
\frac r4\le\frac14\left(\frac{3r}4\right)^2,
\tag{6.9}
\]

近零不成立。这里只否定**固定证书块的凸性**；没有据此声称 \(T_0\) 不可能拥有另一份 energy 证书。

缺的不是“插入非 Lipschitz 点对”本身，而是同时保持整个输入纤维几何、兼容预算及无限复合动力学的操作。

### B5 [N／O] 局部动力学不能决定原算子真实 EB

令 \(E=\mathbb R^2,\lambda=1,S=\mathbb R\times\{0\}\)、\(U=\mathbb R\times(-1,1)\)，

\[
F_0(p,r)=\{(0,-19r/9)\},\qquad
G_1=\operatorname{gph}F_0\cup\{((0,4/5),(0,3/10))\}.
\tag{6.10}
\]

新增图点的输入为 \((0,11/10)\notin U\)，故两者在 U 的完整 resolvent 同为

\[
T(p,r)=(p,-9r/10).
\tag{6.11}
\]

在共同 \(B=W=[-1,1]\times[-9/10,9/10]\) 上轨道、解集、几何尾均相同；但实际输出 \(u_0=(0,4/5)\) 满足

\[
r_{F_0}(u_0)=76/45,\qquad r_{F_1}(u_0)=3/10.
\tag{6.12}
\]

所以尾、极限、甚至全部局部轨道都不足以恢复认证所需残差。

已有局部补救：若 \(V\Subset U\)、\(\delta=\operatorname{dist}(V,E\setminus U)>0\)，则

\[
u\in V,\ (u,v)\in G,\ \|v\|<\delta/\lambda
\Longrightarrow u+\lambda v\in U.
\tag{6.13}
\]

这能定位所有小残差纤维；较大残差用输出半径补界。Germ 编码已经使用此双 collar。未解决的是与固定宏观域、统一尾和局部修改的同时闭合。

### B6 [N／E／O] 步长谱可以任意紧：有理化失败，编码已有替代

给定非空紧 \(A\Subset(1,\infty)\)，令 \(a_- =\min A,a_+=\max A\)、\(C>\max\{1,a_+\}\)，以一维原图

\[
G_A=\{(u,u):u\in\mathbb R\}
\cup\left\{\left(
\frac{Ct(1+t)}{d(t,A)},-
\frac{C(1+t)}{d(t,A)}\right):t>0,t\notin A\right\}
\cup\{(0,-C/a_-)\}
\tag{6.14}
\]

并乘自由切向维。图闭、非点零集固定。在 \(\lambda\in A\) 时，额外图点的 Minty 输入模至少 C，所以小输入的完整 resolvent 恰为基线压缩；在 \(\mu\notin A\) 时取 t=μ，输入零增加非零输出。额外残差模大于一，所以近零真实 EB 与基线相同。

在指定解点的局部口径下，完整良定、LT、direct、energy 及全选择收敛谱均恰为 A。A 可以是无理单点或 Cantor 集；任意 A 版本仅声称闭图，A 半代数时才可相应说图半代数。

这否定“严格局部证书必有开步长窗口”“存在实步长可由有理步长检验”。但不能据此说认证类不可测。E9 已将实步长直接放进紧参数块并证明闭投影，关闭了固定锚点 germ 的描述集合问题。剩余困难是固定宏观规格及范畴，而非单纯不可数性。

### B7 [N／D／O] 全时间拓扑合法但改变“典型”的含义

单步接近不控制长期选择，即使 exact-S 和一致收敛均保持。取 \(K=[0,1]^2,S=[0,1]\times\{0\}\)，令

\[
f_\varepsilon(r)=
\begin{cases}
(1-\varepsilon^2)r,&0\le r\le\varepsilon,\\
\varepsilon-\varepsilon^3+\varepsilon^2(r-\varepsilon),&\varepsilon\le r\le2\varepsilon,\\
r/2,&2\varepsilon\le r\le1,
\end{cases}
\]

\[
T_\varepsilon(s,r)=(\min\{1,s+\varepsilon r\},f_\varepsilon(r)),
\quad T_0(s,r)=(s,r/2),\quad0<\varepsilon<1/4.
\tag{6.15}
\]

各映射一致收敛、精确固定 S，且 \(\|T_\varepsilon-T_0\|_\infty\to0\)。但从 \((0,\varepsilon)\) 出发，切向总位移
\(\sum_{n\ge0}\varepsilon^2(1-\varepsilon^2)^n=1\)，故

\[
\|\Pi_{T_\varepsilon}-\Pi_{T_0}\|_\infty=1.
\tag{6.16}
\]

因此全时间距离不趋零。两拓扑在 lu 层具有相同 Borel 集，也不能推出相同第一纲集。E7 只在共同实际尾层闭合；总空间间的保纲桥尚无。

### B8 [N／O] 证书、轨道和结构切片的遗忘投影不保纲

即使连续开放满射

\[
p:\mathbb R^2\to\mathbb R,\quad p(x,y)=x
\]

也将无处稠密的 \(\mathbb R\times\{0\}\) 映为全部 \(\mathbb R\)。开放映射可用于底集 A 与**饱和逆像** \(p^{-1}(A)\) 的类别比较，而不是任意见证子集与其像。

这同样阻止把结构层自身的余稀结论提升到母空间。横轴在自身中全体、在平面中无处稠密，是最小提示；真正缺口是层分解／开放坐标／范畴保持定理。

### B9 [N／O] 保真共轭与制造非线性位移之间有真实张力

对完整图定义

\[
G^h=L_\lambda^{-1}(h\times h)L_\lambda G,
\qquad T^h=hTh^{-1}.
\tag{6.17}
\]

若 h 保持 S、B、W 且 \(\operatorname{Lip}h\le1+\varepsilon\)，有

\[
T\in\mathfrak D_\omega\Longrightarrow
T^h\in\mathfrak D_{(1+\varepsilon)\omega}.
\tag{6.18}
\]

这不是同一个冻结空间中的密度结论。严格尾余量对象是否稠密未证明。

若还为保真 EB 要求

\[
\|h(z)-z\|\le\varepsilon
\min\{d(z,S),\|z-Tz\|,\lambda r_F(z)\},
\tag{6.19}
\]

则全纤维残差和法向距离保持双侧比较，但也有

\[
\frac{\|T^h(hx)-hx\|}{d(hx,S)}
\le\frac{1+2\varepsilon}{1-\varepsilon}
\frac{\|Tx-x\|}{d(x,S)}.
\tag{6.20}
\]

所以原线性位移有界时不能通过这种双侧保真制造无界位移来排除 LT。绕过它必须改变残差阶并重新证明真 EB，不是再缩小扰动幅度即可。

### B10 [N／O] 一般解集及无限维推广另有结构障碍

任意闭 S 未必为共同域的连续回缩像；仿射正常分裂和非退化漂移也不自动出现在一般 RLEB 中。局部 \(C^1\) 解流形已有 LT 必要界，但保 RLEB 的变形尚未推广。

无限维时闭纤维不必有最近点，例如
\(\{(1+1/n)e_n:n\ge1\}\subset\ell^2\)
到零距离为一而不取得；AW hyperspace 可有不可数一致分离闭集
\(\{0\}\cup\{e_n:n\in A\}\)；连续映射在有界集未必一致连续，有限次复合也可能不连续。因此现有有限维 Polish 证明不能只换符号推广。这不是当前必须先攻的门槛。

## 7. 仿射非退化漂移定理：准确保留其价值，也准确限制其代表性

该工具不是孤立公式模型，而是作用于整个函数结构层。取

\[
E=\mathbb R^m\times\mathbb R^n,\quad m\ge n\ge1,
\quad S=\mathbb R^m\times\{0\},
\]

\[
T(y,z)=(y+A(y,z),B(y,z)),\quad
\|A(y,z)\|\ge c\|z\|,\quad
\|B(y,z)\|\le q\|z\|,
\tag{7.1}
\]

配共同局部 \(C^{1,1}\) 导数预算，包括
\(\|D_zA\|\le M\)、\(\|D_yA\|\le C_A\|z\|\)
等。对 \(0<\gamma<1,p=1/\gamma\)，在很小法向管内令

\[
h(y,z)=(y,\|z\|^{p-1}z),
\tag{7.2}
\]

并以径向过渡使其在外部为恒等且 \(\operatorname{Lip}h\le1+\varepsilon\)。得到完整共轭 \(T'=hTh^{-1}\)，满足

\[
\|T'x-x\|\ge c,d(x,S)^\gamma,
\qquad d(T'x,S)\le q^p d(x,S),
\tag{7.3}
\]

以及真正全纤维 EB

\[
d(u,S)\le\left(\frac{\lambda q}{c}r_{F'}(u)\right)^p.
\tag{7.4}
\]

小工作块上 all-pairs RL 常数可取

\[
L_D=2MC_\gamma+C_0D^{1-\gamma}.
\tag{7.5}
\]

若 \(qMC_\gamma/c<1\)，缩小工作块即可得到严格 direct 兼容和真正共同小初值邻域；(7.3) 的无界线性位移比排除同一个 \(F'\) 在任何正步长的局部 LT all-pairs 认证。

尚欠的三条逻辑桥不能删除：

1. 当前只保 \(\omega\mapsto(1+\varepsilon)\omega\)，不是完全相同 \(\omega\)。
2. 新证书可能只在随变形缩小的 germ 成立，未保持原宏观证书域。
3. 未知 (7.1) 的层及其变形像在中立母空间的类别地位；在加权导数拓扑有内部，不等于在 AW／全时间母空间有内部。光滑源层经粗化后还可能离开源层，所以不能把它当作源层内部稠密性证明。

故该结果是**一个可复用的局部建设模块**。它不足以单独说理想差距已得到比较，也不足以证明继续沿该层推进必会到达理想目标。

## 8. 已尝试的路线与停止点

| 路线 | 已获得什么 | 为什么没有完成主问题 |
|---|---|---|
| 固定 Hölder／超吸引 \(\mathcal Y\) | 真正无限维紧 Baire 层内，任意步长 LT 第一纲 | 预设法向律，母空间本已收敛；遗漏双方其他机制；没有代表性转移 |
| 最大证书预算层 \(\mathcal C_P\) | 可构造紧参数投影；能研究 RLEB 内部 | 由证书定义，不是中立总分母；并类非凸、Baire 性不自动 |
| 所有闭图 AW 空间 | 本体与全步长统一 | 一步可解性已第一纲，比较退化 |
| 大连续 exact-S 空间 | Polish／自然图表；可测编码 | 正 Hölder 类本已小，双方同时第一纲 |
| 全时间收敛空间 | 不预设速度；pt Baire、lu Polish | 变更“邻近”语义；未得认证像类别与单步保纲桥 |
| 固定实际尾层 | 闭 Baire且两拓扑等价 | 层可能退化／薄；精确预算限制局部自由；不可数尾族无现成汇总 |
| 普通凸混合／粗化 | 单步正则性逃逸容易 | 真实 EB、严格兼容、exact-S 与无限复合尾不同时保持 |
| 双侧保真共轭 | 完整图、零集、EB 运输 | (6.20) 禁止其制造所需无界位移 |
| 法向幂共轭 | 在 (7.1) 层中重建真 EB 并任意步长排除 LT | 同尾、同域及母空间位置未证 |
| 开步长／有理化 | 全局 Lipschitz 或 no-escape 图表有窗口 | 局部严格证书本身可有任意紧谱；普遍路线已被反证 |
| 实步长紧投影 | 固定锚点 germ 认证像 \(F_\sigma\) 已完成 | 描述集合地位不是第一纲；不是固定宏观全部规格的统一定理 |

## 9. 给数学家团队的开放问题清单

### OP1：有鉴别力的中立比较结构应是什么？[D／O，首优先]

在 Q-AW、Q-DYN 中，找出不以任何证书名称、指定 Hölder 指数或非退化漂移形式定义的内生不变量／分解，能够区分两种认证机制。候选数据是完整反射模 \(\Omega_{F,\lambda}\)、真残差剖面 \(\mathcal E_F\)、实际尾 w、极限纤维和步长谱，而不是只有尾。

需要给出可证的表示、分解或重构关系，例如该结构怎样控制认证成员资格，以及各层如何覆盖预定主空间。不能仅命名“类别剖面”。

成功：比较分母与结构语言不再随预期结论变化。失败／反定理：说明某组动力坐标不能决定证书；需保留额外图不变量，或承认只能分机制比较。

### OP2：RLEB 的无标签并类何时有非退化 Baire 结构？[O，首优先]

在一个明确、规则的 K、非点 S、共同域及拓扑下，判定

\[
\mathcal R=\bigcup_j(D_j\cup E_j)
\]

是否自第一纲、是否在中立收敛层中第一纲、是否存在中立内生定义的非第一纲区域。E8 的 \(K_\sigma\) 与 §6.2 的局部紧诊断应作为可用工具，而非忽略。

成功：相对“典型 RLEB”有真正数学内容。相反结论：禁止单押“LT 在 RLEB 内第一纲”，改用绝对类别、闭包、机制分区或其他已定义不变量；不是否定 RLEB 收敛定理。

### OP3：中立收敛层中的绝对类位置是什么？[O]

对规则共同几何，在 \((\mathfrak C_{\mathrm{lu}}(P),\rho_{\mathrm{dyn}})\) 判定 \(\mathcal R_P,\mathcal L_P,\mathcal R_P\setminus\mathcal L_P\) 的闭包、内部和纲。首先允许答案为两者皆小；不能把大 \(C^0\) 层的结论自动下传。

成功：直接回应作者“全部收敛算子中的位置”。失败的准确形式应是证明某目标结论不成立并找出阻断区域，而非研究者暂时未能构造扰动。

### OP4：同域、同尾、全纤维的对象修改或刚性定理能否成立？[O]

令 \(Z\subset\mathfrak D_\omega(P)\) 是已经证明非退化的比较层，且 \(s\in S\)。定义闭必要块

\[
C_{m,j}(s)=\{T:\|Tx-x\|\le m,d(x,S)
\quad\forall x\in K\cap\overline B_{1/j}(s)\}.
\tag{9.1}
\]

需要证明或否定：对每个 \(T\in Z\cap\mathcal R\cap C_{m,j}\) 及任意对象邻域，存在 U 仍在同一个 Z、同一 \(\mathfrak D_\omega\)、同一宏观证书接口、完整 RLEB 中，且 U 违反 (9.1)。允许重选证书参数，但不允许改分母或改原图语义。

若 S 局部仿射／\(C^1\)，E10 将所有正步长 LT 都放入 \(\bigcup_{m,j}C_{m,j}\)。所以修改引理一旦成立，闭块无处稠密与 Baire 步骤很短。难点是前提闭合，不是最后的 Baire 定理。

成功：可得真正对象层类别判决。失败：若能证明哪类 Z 有刚性／LT 开块，便得到有内容的分类；若只在特殊漂移层能做，仍属支线，需 OP5。

### OP5：局部建设层如何上升到母空间？[O，决定路线是否降级]

对 §7 的源层 N 及变形像 \(\widetilde N\)，分别证明在冻结的中立空间中的闭包、相对内部、稠密性／非第一纲性，或建立一个覆盖性、局部乘积、开放坐标、饱和投影、范畴保持定理。

不得把 N 的加权 \(C^1\) 拓扑与母空间 AW 混用，也不得把 \(N\to\widetilde N\) 当成 \(N\to N\)。

成功：受限定理有代表性，可以支撑理想比较。失败／证明 N 薄：应将此路线降为例证和技术模块，主资源回到 OP1–3；不能继续把更多同类构造叫总体推进。

### OP6：跨尾尺度是否存在保纲／局部厚度转移？[O]

研究 \(\mathfrak D_\omega\hookrightarrow\mathfrak D_{c\omega}\) 与受控共轭作用，而非只研究集合包含。一个关键子问题是

\[
\bigcup_{0<c<1}\mathfrak D_{c\omega}
\quad\text{在 }\mathfrak D_\omega\text{ 是否稠密，在哪些非退化规格下？}
\tag{9.2}
\]

即使 (9.2) 成立，也须检查该收紧操作保留真实 RLEB 与宏观证书域。若要直接处理所有尾，需无速率总空间上的定理或真正覆盖的分层汇总机制；不可用预列可数尾清单替代。

这里不能对所有规格无条件期待 (9.2)：任一收敛至 S 的系统都满足 \(w_0(G)\ge D_B:=\sup_{x\in B}d(x,S)\)。若 \(D_B>0\) 且已冻结 \(\omega_0=D_B\)，则每个 \(\mathfrak D_{c\omega}\)（\(c<1\)）为空。因此可研究的修订必须声明初段存在余量，或仅从某个 N 以后收紧尾预算；不能把这个直接几何阻断当成尚缺技术证明。

成功：把 (6.18) 的任意小 slack 转为有意义的类比较。失败：精确尾可能带不可消除的刚性，须将跨尺度性能谱作为独立结果，并停止同尾宣称。

### OP7：固定宏观原图 atlas 的认证像能否获得统一内生表示？[O]

将 E8 的完整紧源图卡、E9 的允许缩域 germ 与 (2.5) 的固定宏观原图规格统一。要保留全部外部纤维和实际输出域，明确可测复杂度；不把已完成的 germ \(F_\sigma\) 误作尚未完成的宏观定理。

建议先定义

\[
\Omega_{F,\lambda}(r)=
\sup_{\substack{x,y\in H\\\|x-y\|\le r}}
\|R_Tx-R_Ty\|,
\quad
\mathcal E_{F,V}(t)=
\sup_{\substack{u\in V\\r_F(u)\le t}}d(u,S),
\tag{9.3}
\]

研究半连续性、重构证书的充要条件及预算最优化。空测试集约定须声明。

成功：将“存在证明”转为对象本身的结构判别，给比较和算法验证共同接口。失败：应精确指出哪个宏观域／纤维量词造成更高复杂度，不退回选中残差。

### OP8：跨步长性能比较与 no-escape 结构是什么？[O]

E9 处理了某类存在量词，E6 型谱实现已否定普遍开窗口。新的问题是：哪些中立图紧性／properness 或残差剖面条件保证完整局部步长窗口；这些条件在主空间处于什么位置；LT 与 RLEB 在相同条件下给什么性能谱。

若每步 energy 不同，不能直接串接 \(V_{\lambda_k}\)；需要共同 Lyapunov 或可控比较因子。\(F=I\)、\(\sum\lambda_k<\infty\) 给非零乘积极限，说明“所有固定步长都收敛”不蕴含任意正步序列收敛。

成功：类大小之外得到真正算法参数结构。失败：完整谱可不规则，应保留谱而非强迫区间；不将狭窄认证谱说成实际 PPA 不收敛。

### OP9：一般解几何与多值／Hilbert 推广的边界在哪？[O，后置]

先确定仿射、\(C^1\)、prox-regular 或任意闭 S 是否必须分层；再研究完整多值全选择收敛的路径空间投影，而非把单值极限映射结论强塞进去。无限维需重新指定拓扑、复合连续性与 Baire／Polish 要求。

成功：体系覆盖性扩大。失败：给出清楚几何／量词分区仍有价值，不能以“有限维状态”否认算子空间研究，也不能以“泛函分析语言”掩盖未证无限维推广。

### OP10：哪项精确新定理真正超出既有工具？[O，数学完成后验收]

在 OP1–9 形成确定主结果后，再逐定理核查原始文献。重点不是再次证明 WPO 命名或 Minty 图坐标，而是完整图、真实 EB、共同动力学及类别转移同时成立的具体桥梁。

成功：能够精确拆分已知底座与可保留原创部分。发现先例：应保留未覆盖的量词、范围或定量结果，不把局部重合判成整体已知。检索未见不能作为首创证明。

## 10. 建议的数学家团队分工与阶段验收

| 工作组 | 首要任务 | 交付物 |
|---|---|---|
| 泛函／描述集合与 Baire 组 | OP1–3；审查 \(K_\sigma\) 与自第一纲的真实分母 | 一个中立空间中绝对类别定理，或严谨退化／不可比较定理 |
| 动力系统／拓扑组 | OP5–6；分层代表性、全时间与图拓扑、跨尾桥 | 类别保持／局部乘积／层位置定理，或明确反定理 |
| 变分分析／PPA 组 | OP4、OP7；全纤维 EB、RL、宏观域与尾同时闭合 | 对象修改／延拓／刚性引理，所有量词可核 |
| 谱与策略组 | OP8；同一原图的可用谱、性能谱与 no-escape | 固定／存在／全策略的结构定理，避免有理化 |
| 独立审计与文献组 | 横向检查范围，完成 OP10 | 定理号对应、最小反例、每条主张已证／未证状态表 |

建议先完成一次概念性会议，冻结：主比较是 Q-AW 还是 Q-DYN；比较对象是否固定步长；主规格是否宏观同域；接受什么类型的“结构差异”作为有价值终判。该会议不是让作者选择希望出现的答案，而是确定正在问的数学问题。

首个里程碑不要求证明 LT 小，只要求：

1. 主分母非空且 Baire／可描述；其科学含义明确。
2. 两认证类在对象侧被准确表示。
3. 证明一项真正的总体／代表性结构定理，或证明预期类别目标在该分母中退化。
4. 如继续使用 §7 的变形，必须同步验收 OP5；没有母空间位置报告，不将支线完成记为主线进度。

## 11. 文献接口与已知工具边界

以下是既有团队原文审查记录的交接，不是本稿新作的优先权认定。完整假设与版本编号以索引文件为准。

| 原始工作 | 可借部分 | 没有自动解决的部分 |
|---|---|---|
| Rus–Petruşel–Şerban, *Weakly Picard operators: equivalent definitions, applications and open problems* (2006), Definition 1.6、Theorems 6.2、8.1 | 收敛母类、极限纤维、部分定量 WPO／有限长度语言 | 原欧氏图拓扑中的全部 PPA、真残差 EB 与证书类比较。[原文](https://www.math.ubbcluj.ro/~nodeacj/download.php?f=061rus.pdf) |
| Butnariu–Reich–Zaslavski, *Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces* (2001), Theorems 2.1、3.1–3.2 | 固定非点集、完备算子空间、泛型极限回缩、投影混合 | 母类预设 Bregman 下降；不覆盖任意非 Fejér RLEB。[DOI](https://doi.org/10.1515/JAA.2001.151) |
| Wang, *Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent* (2013), Propositions 2.1、2.3–2.4、Theorem 2.13 | 单调／resolvent 空间、完备拓扑、泛型论证 | 固定多解 S 后严格压缩稠密机制不能照搬。[DOI](https://doi.org/10.1016/j.na.2013.03.008) |
| Bauschke–Schaad–Wang, *On Douglas–Rachford operators that fail to be proximal mappings* (2018), Theorem 3.1 | 同一完备结构空间内的真实闭无处稠密子类比较 | 限于线性关系对，不是一般 RLEB–LT。[DOI](https://doi.org/10.1007/s10107-016-1076-5) |
| Tikhonov, *Complete metric on mixing actions of general groups* (2013), Theorem 1 | 全时间拓扑建立长期行为空间的完备可分性 | 不是 PPA 点轨道收敛或图证书比较。[DOI](https://doi.org/10.1007/s10883-013-9162-y) |
| Leuştean–Nicolae–Sipoş, *An abstract proximal point algorithm* (2018), Theorems 3.13、3.15、5.1；Sipoş, *Revisiting jointly firmly nonexpansive families of mappings*, Theorem 3.3 | 相容 resolvent family、joint FNE、抽象 PPA | 非单调完整图与类规模不由其自动给出。[DOI](https://doi.org/10.1007/s10898-018-0655-9)、[arXiv](https://arxiv.org/abs/2006.02167) |
| Ravasini, *Generic uniformly continuous mappings on unbounded hyperbolic spaces* (2024), Lemma 3.2、Theorem 3.3 | 固定凹模、局部压平、泛型模饱和 | 不保固定 S、实际尾与真实 EB；不能直接限制残集。[DOI](https://doi.org/10.1016/j.jmaa.2024.128440) |
| Azagra–Le Gruyer–Mudarra, *Kirszbraun’s theorem via an explicit formula*, Theorems 2、8；相关 Whitney 延拓 | trace、单步 Lipschitz／FNE 或 jet 延拓 | 精确固定集、整个逆纤维 EB 与指定无限尾均需另证。[arXiv](https://arxiv.org/abs/1810.10288) |
| Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, Proposition 4、Assumption 2、Theorem 2 | (3.7)–(3.9) 的准确公共接口 | 局部截断分支必须另对齐完整图；不是全部历史 LTT。[DOI](https://doi.org/10.1287/moor.2025.0863) |

尚未完成原始全文链：Reich–Zaslavski 1999 *Convergence of Generic Infinite Products of Nonexpansive and Uniformly Continuous Operators*、Strobin 2012 *Some Porous and Meagre Sets of Continuous Mappings*，以及与本次精确谱实现／规范化／变形组合完全对应的后续原文审查。应列“待核”，不编定理号，不用缺全文证明无人做过。

## 12. 可复现文件索引与阅读顺序

根目录为 `/workspace/scratch/bf20ae56bc4b/`。下文 `system/` 是 `ppa_system_team/` 的简记，`classification/` 是 `ppa_classification_team/` 的简记，不是新目录。历史稿中“未完成”的旧句若已由后续证明关闭，以最终审计注明的版本为准；不能把所有报告的时间状态直接取并。

### 第一遍：主问题、已核范围与真实停止点

1. [10_final_blueprint.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/10_final_blueprint.md)：P0–P10、五层体系、T1–T15 与三大目标。
2. [07_stage_synthesis.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_classification_team/07_stage_synthesis.md)：最近一阶段完成项、三桥缺口；其中首攻仿射层的建议是待评估路线，不是已证明代表性。
3. [05_obstruction_audit.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_classification_team/05_obstruction_audit.md)：自第一纲、尾退化、谱、全纤维与交叉审计。

### 第二遍：按问题查证明

| 文件 | 内容／本稿对应 |
|---|---|
| [01_ambient_axioms.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/01_ambient_axioms.md) | 中立本体、A/B/C 层、开输入局部 atlas、回缩结构 |
| [02_convergence_topology.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/02_convergence_topology.md) | 全时间拓扑、pt/lu 完备性、Polish、非可分、同 Borel 不同 category |
| [03_certificate_embeddings.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/03_certificate_embeddings.md) | LT→energy、规范 gauge、标准紧图卡编码与共同尾 |
| [04_priorart.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/04_priorart.md) | 原始文献定理级覆盖，已读与未读边界 |
| [05_stress_test.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/05_stress_test.md) | 量词、收敛、拓扑和投影的压力测试 |
| [06_resolvent_family.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/06_resolvent_family.md) | 完整关系 family、AW、通用轨道 incidence、步长迁移 |
| [07_embedding_math_audit.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/07_embedding_math_audit.md) | direct/energy 规范化及 LT 转换的独立复核 |
| [08_architecture_audit.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/08_architecture_audit.md) | 架构终审、投影修复、良定原图 Gδ、固定 S 拓扑反例 |
| [09_value_audit.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/09_value_audit.md) | 已知底座与真正待证主结果；部分早期未完成句已由后续关闭 |
| [01_frozen_denominator.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_classification_team/01_frozen_denominator.md) | 原图固定规格、真实残差、留域和实际尾闭层；局部 T 不能恢复原 F |
| [02_structural_deformation.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_classification_team/02_structural_deformation.md) | 全图共轭、(1+ε) 尾、非退化漂移层变形及其 no-go |
| [03_object_category.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_classification_team/03_object_category.md) | 对象违约量、Kσ、任意步长线性位移必要层、OLM、Baire 诊断 |
| [04_step_spectrum.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_classification_team/04_step_spectrum.md) | 谱实现、单值与全选择谱分离、实步长闭块投影、germ Fσ |
| [06_priorart_tools.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_classification_team/06_priorart_tools.md) | 延拓／局部替换／共轭工具的原始定理与缺失闭合 |
| [09_final_synthesis.md](sandbox:/workspace/scratch/bf20ae56bc4b/comparison_space_team/09_final_synthesis.md) | 历史超吸引层 \(\mathcal Y\) 的真实定理；仅作测试案例，不能升级成总体比较 |

### 第三遍：外部团队首次复核的建议清单

- 从 (2.1) 重新验证完整图与真残差，不只核正向分支。
- 核 E3 的逆连续性确实使用开域与有限维球面紧性。
- 核 E5/E7 使用哪个全时间距离及共同域，不混数值等距和同拓扑。
- 将宏观、germ、完整紧源图卡三种证书口径分开逐项核对。
- 重证 §6.2 的自第一纲与 §6.6 的谱实现；它们决定主目标怎样改写。
- 对 §7 只验其声明范围，另将 OP5 列为不可省略的代表性任务。

## 13. 交接后的判断原则

当前需要数学家团队提供的是**结构性 idea 或反定理**，不是替一个已有反例调参数。尤其欢迎三种方向：

1. 一个解释认证类为何具有某种结构的表示／分解定理，使两类在共同体系中可比较；
2. 一个把局部构造或函数层推向中立母空间的真实保纲／覆盖桥梁；
3. 一个证明理想化单一纲排序在自然空间内必然退化的定理，并提出经论证更有鉴别力的内生不变量。

最后应如实区分：**尚未找到证明**不等于**已经证明不可能**；**层内定理正确**不等于**层有总体代表性**；**两类皆第一纲**不等于**两类相同或理论没有价值**。

这正是本次交接的停点：底座可以继续用，局部工具可以保留，但理想比较所需的代表性、非退化性与类别转移尚未闭合。不能靠增加同类构造掩盖这三项缺口。
