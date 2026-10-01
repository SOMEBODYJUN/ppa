# 无标签 PPA 动力系统母空间：公理、表示与完备化架构

日期：2026-09-20。角色：本轮基础架构。本文完整阅读了上一轮 `comparison_space_team/01、04、08、09`、原 RLEB 投稿稿的全部正文与附录、`solution_selection_revised_v1/research_note.md`。本轮不重新审查原 RLEB 已建立结果，也不把上一轮尖点层的纲结论搬到新母空间。

## 0. 本轮必须改的不是一个包含式，而是研究的逻辑顺序

用户的校正成立。上一轮最后建议的 \(\mathcal C_P\) 仍然先按 RLEB 证书选母类；它比法向超吸引层更贴近 RLEB，却依旧没有完成用户要求的“先建立无标签的 PPA 算子体系，再放入各理论”。

本报告采取以下顺序：

\[
\text{完整 PPA 实例}
\longrightarrow\text{中立动力系统空间}
\supset\text{全轨道收敛者}
\supset\text{局部一致收敛者},
\]

然后才研究 RLEB、LT 及其他条件分别落入哪些结构子类。母空间定义里没有 RL、Hölder 指数、误差界、单调性、法向下降律或“新理论必须占大类”的要求。

目前可以严格建立三件基础事实：

1. 无单调性约束时，任意连续单步映射都可表示成一个闭图关系的完整 resolvent；所以最外层本来就是连续动力系统空间，而不是一种未找到的特殊“RLEB 算子空间”。
2. 全部逐初值收敛者，在单步一致拓扑下一般不闭；但在不带证书标签的**全时间轨道度量**下，它们本身就是完备 Baire 空间。
3. 其中紧集上一致收敛到极限回缩的成员，在同一轨道拓扑下是 Polish 空间；它可以表示为一个标准连续映射空间的闭子集。共同尾界只是在这个空间中后置选择的闭层，不是先挑某种收敛证明。

这些是组织和表示定理，不在本报告中主张文献首创。它们也没有证明任何 RLEB／LT 的范畴大小。

## 1. 先锁定“一个对象到底是什么”

### 1.1 固定步实例与原算子不是同一个比较单位

主对象是固定步算法实例

\[
\mathsf A=(F,\lambda),\qquad \lambda>0,
\qquad T=J_{\lambda F}=(I+\lambda F)^{-1}.
\tag{1.1}
\]

以下“单步映射”始终指完整 proximal inclusion 在工作输入域上的全部解恰为一个值，不是选择某一分支。

固定 \(\lambda\) 后，全空间完整 \(T\) 唯一决定 \(F\)。但是不同 \(\lambda\) 表示同一 \(F\) 时，迭代动力学可以不同，不能预先取商并把收敛性视为商上的属性。

若 \(c=\mu/\lambda>0\)，同一原算子的另一步长输入满足

\[
z=cx+(1-c)Tx=:A_c^T(x),\qquad Tx\in J_{\mu F}(z).
\tag{1.2}
\]

在全空间连续单值接口中，\(J_{\mu F}\) 也是全定义连续单值映射，当且仅当 \(A_c^T\) 是同胚；此时

\[
T_\mu=T\circ(A_c^T)^{-1}.
\tag{1.3}
\]

证明反向也不需额外可逆性假定：若 \(J_{\mu F}\) 全定义单值连续，则
\(x=[z-(1-c)J_{\mu F}(z)]/c\) 恰给 \((A_c^T)^{-1}\)。因此跨步长应组织成**部分坐标变换图谱**，不是默认每个步长都有效的群作用。

变步长策略 \(\boldsymbol\lambda=(\lambda_k)\) 另属对象 \((F,\boldsymbol\lambda)\)，对应非自治复合 \(T_{\lambda_{n-1}}\cdots T_{\lambda_0}\)。本报告的表示与完备性主定理先对固定步成立。存在完整 resolvent 族既不意味着每个固定步收敛，也不意味着任意策略收敛。

### 1.2 保留原有欧氏几何

主状态空间取 \(E=\mathbb R^d\)，保留其原范数和原 proximal inclusion。不允许为了让某个映射变成压缩，另造一个改变原收敛几何的底空间度量，再称已比较原问题。

函数空间已无限维；不必先把状态空间也无限维化。无限维 Hilbert 推广另需处理局部紧性、compact-open 的可度量性、最近点和最小残差是否取得，不能直接复制下文的 Polish 论证。

## 2. 最小公理：基础公理与动力学层公理分开

| 编号 | 内容 | 作用层 |
|---|---|---|
| P0 对象公理 | 固定原几何、完整 \((F,\lambda)\) 及固定步／策略口径；不同原对象不因某张局部证书而合并 | 所有层 |
| P1 完整性公理 | 在声明输入域上，\(J_{\lambda F}=T\) 是完整关系恒等式；保留整个逆纤维 | 所有层 |
| P2 状态公理 | 声明共同闭前向不变域 \(D\)、非空闭目标集 \(S\subset D\)，且 \(T|_S=I\) | 固定目标层 |
| P3 有限时间公理 | 选定使有限次迭代连续的单步拓扑；先证明母空间的 Polish／Baire 性 | 基础空间 A |
| P4 收敛公理 | 对每个 \(x\in D\)，\(T^n x\) 在原范数下收敛到 \(S\) 中一点 | 收敛空间 B 的定义，不放进 A |
| P5 一致轨道公理 | 上述收敛在 \(D\) 的每个紧子集上一致；极限记为唯一内生映射 \(\Pi_T\) | 空间 C，不放进 B 的定义 |
| P6 预算公理 | 如需定量比较，另指定共同 Cauchy 尾预算；不指定证明该预算的理论 | C 的后置闭层 |
| P7 认证公理 | 各理论仅给出到上述空间／结构子类的嵌入命题；证书遗忘后每个算法对象只算一次 | 后续比较 |
| P8 传递公理 | 换拓扑、投影证书、换步长或限制到子层时，必须证明相应同胚或范畴保持桥梁 | 所有纲结论 |

这不是将九个条件一次性强加给全部算子。A 只要求基础合法性；B、C 逐层添加真正动力学性质。RLEB 和 LT 不出现在公理里。

## 3. 表示定理：合法完整 PPA 与连续映射的关系

### 定理 A0：全空间完整表示

给定 \(\lambda>0\)、\(T\in C(E,E)\)，定义

\[
F_{T,\lambda}(u)
=\{(x-u)/\lambda:x\in E,\ Tx=u\}.
\tag{3.1}
\]

则

\[
J_{\lambda F_{T,\lambda}}=T,
\qquad \operatorname{zer}F_{T,\lambda}=\operatorname{Fix}T,
\tag{3.2}
\]

且 \(F_{T,\lambda}\) 闭图。反之，任何全定义连续单值的完整 \(J_{\lambda F}\) 都通过 (3.1) 恢复原 \(F\)。

证明：

\[
u\in J_{\lambda F_{T,\lambda}}(x)
\iff (x-u)/\lambda\in F_{T,\lambda}(u)
\iff Tx=u.
\]

图通过线性同胚
\((x,u)\mapsto(u,(x-u)/\lambda)\)
互相转换，故闭图性保持。对任意 \((u,v)\in\operatorname{gph}F\)，输入 \(x=u+\lambda v\) 必有 \(Tx=u\)，所以没有遗漏原图点。

因此“任意闭图关系允许的连续完整固定步 PPA”与 \(C(E,E)\) 是一一对应，而不是新造的一小类算子。标准逆图身份见 Bauschke–Moursi–Wang 的 Fact 2.1；本处把完整性、步长与闭图证明写全。[原文](https://arxiv.org/pdf/1902.09827)

整个原算子的残差在此坐标中是

\[
r_{F_{T,\lambda}}(u)
=\frac1\lambda\inf_{x:Tx=u}\|x-u\|.
\tag{3.3}
\]

有限维中非空纤维闭，距离最小值取得。后续 EB 不得把 (3.3) 换成某一个输入产生的残差。

### 紧自映射版本及其边界

若 \(K\subset E\) 非空紧、\(T:K\to K\) 连续，仍可用 (3.1) 但只让 \(x\in K\)。得到闭图关系，并且其**整个** resolvent 的定义域恰为 \(K\)，在 \(K\) 上等于 \(T\)。这是一种合法局部 PPA 模型。

但是，不能把一个已有全空间算子裁剪成该模型，再宣称其真实最小残差未变。原有 \(T^{-1}(u)\) 可能含 \(K\) 外的输入。紧域模型是独立的合法对象；已有原算子进入紧域算法图谱时，必须仍保留其完整图或全空间 \(T\)。

## 4. 空间 A：不预设收敛的中立母空间

### 4.1 全局连续完整 resolvent 层

在

\[
\mathcal A=C(E,E)
\]

上取紧集上一致度量

\[
d_0(T,U)=\sum_{j=1}^{\infty}2^{-j}
\min\{1,\sup_{\|x\|\le j}\|Tx-Ux\|\}.
\tag{4.1}
\]

这是可分完备度量空间。Cauchy 序列在每个闭球一致 Cauchy，局部极限相容且连续；可分性来自有限维连续函数空间的逐紧集多项式／分片线性逼近。有限次迭代

\[
T\mapsto T^n
\tag{4.2}
\]

连续：紧集的有限次极限轨道位于一个紧集，局部一致逼近与极限映射的连续性逐次闭合。

给定闭 \(D\subset E\)、非空闭 \(S\subset D\)，定义

\[
\mathcal A_{D,S}
=\{T\in\mathcal A:T(D)\subset D,\ T|_S=I\}.
\tag{4.3}
\]

它是闭子空间，因而 Polish／Baire；这里允许 \(D\setminus S\) 有额外固定点。若要求

\[
\operatorname{Fix}T\cap D=S,
\tag{4.4}
\]

得到 \(G_\delta\) 子空间，仍 Polish。具体对紧集

\[
C_{j,m}=D\cap\overline B_j\cap\{d(x,S)\ge1/m\}
\]

要求 \(\min_{C_{j,m}}\|Tx-x\|>0\)；空集条件忽略。每项是开条件。原限制度量不必完备，但存在等价完备度量。

此处没有共同 Hölder 模，因此通常不紧；**完备/Baire 不要求 Arzelà–Ascoli 紧性**。

### 4.2 标记步长与“所有合法”的范围

若步长也变化，取 \(\mathcal A\times(0,\infty)\)，对应全部标记实例 \((F_{T,\lambda},\lambda)\)，仍 Polish。固定 \(S,D\) 可同样切片。

这一层只覆盖连续、完整单值的 PPA。若“所有合法”包括多值 proximal 关系，必须使用更大的关系空间，不能把单值性叫成纯合法性。§11 给出紧域闭关系的中立扩张。

## 5. 空间 B：所有逐初值收敛的完整 PPA

定义

\[
\mathcal B_{D,S}
=\{T\in\mathcal A_{D,S}:\forall x\in D,
\ T^n x\to\Pi_T(x)\in S\}.
\tag{5.1}
\]

这里不要求 \(\Pi_T\) 连续、不要求统一尾界、不要求有限长度。它正对应“全部这样的 PPA 收敛者”。在固定点理论中，这类逐点收敛映射已有 **weakly Picard operator** 术语；Rus–Petruşel–Şerban 2006 Definition 1.6 允许极限随初值变化。本文不重新发明这个名称，也不调用该文允许改变原度量的等价刻画替代原欧氏问题。[原文](https://www.math.ubbcluj.ro/~nodeacj/download.php?f=061rus.pdf)

### 5.1 单步拓扑下不闭，但不能据此断言“不是 Baire”

取

\[
K=[0,1]\times[-1,1],\quad S=[0,1]\times\{0\},
\quad T_j(z,r)=(z,(-1+1/j)r),\quad j\ge2.
\]

各 \(T_j\) 都有精确固定集 \(S\)，且迭代在 \(K\) 上一致收敛到 \((z,0)\)。但

\[
T_j\to T_\infty(z,r)=(z,-r)
\]

一致，而 \(T_\infty\) 仍有精确固定集 \(S\)，非零法向轨道却为二周期。因此即使先固定精确解集，收敛者在单步拓扑下仍不闭。

这只诊断完备性障碍，不用于断言 RLEB／LT 哪个类大。不闭也不蕴含非 Baire：需另行证明 Baire 性，或选择有独立动力学意义的完备拓扑。

在单步 Polish 母空间中，(5.1) 至少有 coanalytic 上界：固定 \((T,x)\) 的“轨道 Cauchy 且到 \(S\) 距离趋零”是 Borel 条件，然后对全部 \(x\in D\) 取量词。本报告不声称已确定其精确描述集合复杂度。

### 定理 B1：无速率的全时间轨道度量使 B 完备

先在紧自映射模型 \(T:K\to K\) 中，定义

\[
d_{\rm orb}(T,U)
=\sup_{n\ge0}\sup_{x\in K}\|T^n x-U^n x\|.
\tag{5.2}
\]

在 \(\mathcal B_{K,S}\) 上，(5.2) 是完备度量，因此该空间是 Baire。

证明：设 \((T_j)\) 为 (5.2)-Cauchy。对每个 \(n\)，连续映射 \(T_j^n\) 一致趋于某 \(U_n\in C(K,K)\)，且这个逼近对全部 \(n\) 一致。置 \(T=U_1\)，利用紧域上复合的连续性得

\[
U_0=I,\qquad U_{n+1}=T\circ U_n,
\]

故 \(U_n=T^n\)。固定任意 \(x\in K\) 和 \(\varepsilon>0\)，先取 \(j\) 使
\(\sup_n\|T_j^n-T^n\|_\infty<\varepsilon\)，再用 \(T_j^n x\) 的收敛性，便知 \((T^n x)_n\) Cauchy。其极限属于闭集 \(S\)，并且 \(T|_S=I\)。所以 \(T\in\mathcal B_{K,S}\)，且 \(d_{\rm orb}(T_j,T)\to0\)。证毕。

全空间完整对象、只要求在共同闭域 \(D\) 收敛的版本为

\[
d_{{\rm orb},D}(T,U)=d_0(T,U)+
\sum_{j\ge1}2^{-j}\min\left\{1,
\sup_{n\ge0}\sup_{x\in D\cap\overline B_j}
\|T^n x-U^n x\|\right\}.
\tag{5.3}
\]

同样完备。\(d_0\) 保留整个原算子，而轨道部分只测试声明的共同初值域。证明按每个初值紧集逐项重复即可。

### 5.2 代价：B 一般不 Polish，而且换了拓扑

取 \(K=[0,1]\)、\(S=\{0,1\}\)，对每个 \(a>1\) 令 \(T_a(x)=x^a\)。全部轨道收敛到 \(S\)，但极限映射在 \(1\) 不连续。

若 \(a>b>1\)，取

\[
x_n=\exp[-1/\sqrt{a^n b^n}],
\]

则 \(T_a^n x_n\to0\)、\(T_b^n x_n\to1\)，所以

\[
d_{\rm orb}(T_a,T_b)=1.
\]

存在不可数个两两距离为 1 的对象，故这个一般 B 空间不必可分。这不妨碍 Baire 定理，但会影响标准 Borel／Polish 工具。

轨道拓扑同时测试所有时间，严格强于单步拓扑。因此“在 B 的轨道拓扑中第一纲”不是“在 \(C^0\) 或图拓扑中第一纲”的同义句。这个代价必须在任何论文中明示。

## 6. 空间 C：无速率标签的局部一致收敛空间

定义

\[
\mathcal C_{D,S}
=\{T\in\mathcal B_{D,S}:T^n\to\Pi_T
\text{ 在 }D\text{ 的每个紧集上一致}\}.
\tag{6.1}
\]

没有指定几何率、Hölder 率或任何证书；允许任意慢的一致尾。

### 定理 C1：轨道紧化的闭表示与 Polish 性

令 \(\widehat{\mathbb N}=\mathbb N_0\cup\{\infty\}\) 为自然数的一点紧化。对 \(T\in\mathcal C_{D,S}\) 定义

\[
\mathcal O_T(x,n)=T^n x,\qquad
\mathcal O_T(x,\infty)=\Pi_T(x).
\tag{6.2}
\]

则 \(\mathcal O_T\in C(D\times\widehat{\mathbb N},E)\)。反之，这种轨道延拓连续，恰等价于紧初值集上一致收敛。

在 Polish 空间

\[
\mathcal A\times C(D\times\widehat{\mathbb N},E)
\tag{6.3}
\]

中施加下列闭条件：

\[
T(D)\subset D,\quad T|_S=I,\quad
\Phi_0=I_D,\quad\Phi_{n+1}=T\circ\Phi_n,
\quad\Phi_\infty(D)\subset S.
\tag{6.4}
\]

得到的闭子空间恰是 \(T\mapsto(T,\mathcal O_T)\) 的像。因此

\[
\boxed{\ (\mathcal C_{D,S},d_{{\rm orb},D})
\text{ 为 Polish／Baire 空间。}\ }
\tag{6.5}
\]

证明承重点有三项：

- \(D\) 是有限维闭集，故局部紧、可数紧耗尽；\(D\times\widehat{\mathbb N}\) 同样如此，对应 compact-open 连续函数空间 Polish。
- 复合条件对局部一致极限闭合：对一个固定紧初值块，\(\Phi_n\) 的像紧，逼近像最终位于共同紧集，可逐次通过极限。
- 连续 \(\Phi\) 在紧集 \(K\times\widehat{\mathbb N}\) 上一致连续，故 \(\Phi_n\to\Phi_\infty\) 在 \(K\) 上一致；反向由有限步连续与紧集一致尾得到联合连续。

在紧自映射模型中，这简化为 \(C(K\times\widehat{\mathbb N},K)\) 的闭子空间，并且 (5.2) 就是轨道图的 sup 距离。

这项构造没有增加证书重数：\(\Pi_T\) 和整个 \(\mathcal O_T\) 都由 \(T\) 唯一决定。

### 定理 C2：极限回缩、稳定纤维与商结构

对 \(T\in\mathcal C_{D,S}\)，

\[
\Pi_T|_S=I,
\qquad T\Pi_T=\Pi_TT=\Pi_T,
\qquad \Pi_T^2=\Pi_T.
\tag{6.6}
\]

因此 \(\Pi_T:D\to S\) 是连续回缩，且

\[
\operatorname{Fix}T\cap D=S.
\tag{6.7}
\]

令 \(x\sim_T y\) 当且仅当 \(\Pi_Tx=\Pi_Ty\)。则每个等价类是一个闭吸引纤维、对 \(T\) 前向不变，并有

\[
D/\!\sim_T\ \cong\ S,
\qquad [Tx]=[x].
\tag{6.8}
\]

证明：(6.6) 来自极限和连续性，(6.7) 来自固定轨道。连续回缩是商映射：若 \(\Pi_T^{-1}(V)\) 在 \(D\) 中开，则与 \(S\) 相交即得 \(V\) 在 \(S\) 中开；反向来自连续性。因此纤维商与 \(S\) 同胚。

这给出了真正可供分类的结构：每个算法既有单步图几何，也有吸引纤维分解及其在解集上的商结构。RLEB／LT 可以分别对这些结构推出额外定理，而不只是比较某个正则性形容词。

### 定理 C3：迭代与极限对算法对象连续

紧域版本满足

\[
\|T^n-U^n\|_\infty\le d_{\rm orb}(T,U),
\qquad
\|\Pi_T-\Pi_U\|_\infty\le d_{\rm orb}(T,U).
\tag{6.9}
\]

故所有有限时间评价及极限评价连续；全空间版本逐初值紧集成立。这里不是说 \(\Pi_T\) 关于初值 Lipschitz，而是说**算法对象的轨道拓扑**控制其极限映射。

对固定 \(T\)、紧自映射域 \(K\)，还总有中立的截断不等式

\[
\omega_{\Pi_T}(\delta)
\le\inf_{n\ge0}\{\omega_{T^n}(\delta)+2e_n(T)\},
\quad e_n(T)=\|T^n-\Pi_T\|_\infty.
\tag{6.10}
\]

各理论可向 (6.10) 提供不同的有限步模和尾界。它是结构接口，不声称截断思想新颖。

## 7. 共同尾界作为后置闭层：连接强、弱两种拓扑

### 定理 C4：不带理论标签的动力学预算层

固定紧 \(K\)、闭非空 \(S\subset K\)，以及非增序列 \(\varepsilon_n\downarrow0\)。在 \(C(K,K)\) 中定义

\[
\mathcal E_{\varepsilon,S}=\left\{T:
\begin{array}{l}
T|_S=I,\\
\sup_{x\in K}\sup_{m,\ell\ge n}
\|T^m x-T^\ell x\|\le\varepsilon_n\quad(\forall n),\\
\sup_{x\in K}d(T^n x,S)\le\varepsilon_n\quad(\forall n)
\end{array}\right\}.
\tag{7.1}
\]

则：

1. \(\mathcal E_{\varepsilon,S}\) 对单步 sup 拓扑闭，故完全可度量、Polish／Baire。
2. 它包含于 \(\mathcal C_{K,S}\)，并有 \(\|T^n-\Pi_T\|_\infty\le\varepsilon_n\)。
3. 单步 sup 拓扑与全时间轨道拓扑在该层上**相同**。

证明第一项：对每个有限 \(m,\ell,n\)，显示不等式是有限复合的闭条件；取可数交仍闭。第二项由统一 Cauchy 判据和闭目标集。第三项只需证明较弱收敛推出较强收敛。若 \(T_j\to T\) 一致，固定 \(N\)，则对 \(n\ge N\)

\[
\|T_j^n-T^n\|_\infty
\le2\varepsilon_N+\|T_j^N-T^N\|_\infty.
\tag{7.2}
\]

先选大 \(N\)，再用前 \(N\) 步的连续性即可。

这是非常重要的公平桥梁：在同一**实际动力学尾预算**上，强轨道拓扑的类别大小与单步拓扑的类别大小可以比较，且母层不问预算由 LT、RLEB 还是别的方法证明。

不要求共同连续模，所以这些层不必紧；如应用另给等度连续与有界性，可再得到紧性，但它不属于基础公理。

### 7.1 所有一致尾率无须强行压成可数证书层

每个 \(T\in\mathcal C_{K,S}\) 都属于某个 (7.1)：取其真实轨道尾直径和到 \(S\) 的距离上界即可。所有趋零序列在逐项／最终控制下没有一个可数共尾族；简单对角化即可构造比任意预列速率都沿无穷子序列更慢的尾。

因此不能把可数几何／多项式预算层的并宣称为所有收敛动力系统。空间 C 的轨道紧化表示正好无须这种错误可数化。

### 7.2 带 \(\Pi\) 和尾 witness 的增强空间

如果审计需要显式尾界，可取

\[
\mathcal W=\{(T,\Pi,\epsilon):
T\in C(K,K),\ T|_S=I,\ \Pi\in C(K,S),
\ \epsilon\in c_0^{\downarrow,+},
\ \|T^n-\Pi\|_\infty\le\epsilon_n\ \forall n\}.
\tag{7.3}
\]

其中 \(c_0^{\downarrow,+}\) 为非负非增趋零序列的闭锥，使用 sup 范数。(7.3) 是三个 Polish 空间乘积中的闭集，故 Polish；它的遗忘投影连续地落入 C 的轨道拓扑。

多个合法 \(\epsilon\) 仍会重复同一 \(T\)。若需要一对象一次，可选内生唯一尾

\[
\epsilon_n^*(T)=\sup_{k\ge n}\|T^k-\Pi_T\|_\infty.
\tag{7.4}
\]

它满足

\[
\|\epsilon^*(T)-\epsilon^*(U)\|_{c_0}
\le2d_{\rm orb}(T,U),
\tag{7.5}
\]

故其规范图与 C 同胚。真实尾 (7.4) 可能无法有效计算，这不妨碍它作为分类坐标；可计算上界另作为证书附加，不改变对象身份。

## 8. RLEB／LT 怎么进入体系：先证明结构后果，不改母空间

### 8.1 中立局部俘获引理

设 \(s_0\in S\)、\(T\) 在开工作域 \(U\) 上是完整连续单步映射，某非降连续 \(b:[0,R]\to[0,\infty)\)、\(b(0)=0\) 满足

\[
d(Tx,S)\le R,
\qquad
\|Tx-x\|+b(d(Tx,S))\le b(d(x,S))
\tag{8.1}
\]

对所需输入成立。若闭球 \(\overline B_\rho(s_0)\subset U\)，则

\[
K_b=\{x:d(x,S)\le R,
\ \|x-s_0\|+b(d(x,S))\le\rho\}
\tag{8.2}
\]

是紧前向不变集；它包含 \(s_0\) 的足够小初值邻域。证明只用三角不等式与 (8.1)。若另有 \(d(T^n x,S)\to0\)，则轨道有限长并收敛；统一距离／预算衰减进一步给出 (7.1) 的尾预算。

(8.1) 是一个实际的动态长度预算接口，没有单调、RL 或 Hölder 字样。它不是收敛性的必要条件，不能把它放进最外层 A 或全部 B 的定义。

### 8.2 原 RLEB 的 direct 分支提供一个 witness

原稿已证明

\[
d^+\le\kappa d,\qquad
s\le a(d):=\tfrac12(d+Ld^\gamma),
\]

以及

\[
b_H(d)=\tfrac12\left(
\frac d{1-\kappa}+\frac{Ld^\gamma}{1-\kappa^\gamma}\right),
\qquad b_H(d)-b_H(\kappa d)=a(d).
\tag{8.3}
\]

所以 \(s+b_H(d^+)\le b_H(d)\)，确实进入 (8.1)。整块统一 \(d_0\le R\) 后得到

\[
\|T^n x-\Pi_Tx\|\le b_H(\kappa^nR).
\tag{8.4}
\]

这是“RLEB 证书 \(\Rightarrow\) 中立的局部一致收敛／有限长度／可量化尾结构”的嵌入定理，而不是先用 RLEB 定义母空间。

### 8.3 Energy／LT 提供另一类 witness

原 energy 接口给

\[
V(d^+)\le qV(d),\qquad s\le\sqrt{qV(d)},\qquad 0<q<1.
\]

取

\[
b_E(d)=\frac{\sqrt{qV(d)}}{1-\sqrt q},
\tag{8.5}
\]

便有 \(s+b_E(d^+)\le b_E(d)\)，并得到共同尾

\[
\|T^n x-\Pi_Tx\|
\le\frac{q^{(n+1)/2}\sqrt{V(R)}}{1-\sqrt q}.
\tag{8.6}
\]

LT 的公共收敛实例也通过其尾界进入同一结构层；是否先用线性 energy 包含，属于证书转换，不影响母空间。两条通道可在相同 K、相同尾预算下比较；若俘获域依赖不同证书，则先按共同域对齐，不把不同域的结论直接计数。

### 8.4 原局部图块不自动等于完整 PPA

如果原定理只给 \(T=J_{\mathcal G}\)，必须另证

\[
J_{\lambda F}(x)=J_{\mathcal G}(x)
\]

在全部共同轨道工作区成立，才能进入本报告的完整 PPA 层。只在初值球上相等不够。原解选择修订稿 §1 已明确了这个接口。

因此，本报告不是声称每个局部图块定理都自动给全空间连续 resolvent。全球定义对象进入 A；只局部有效的完整对象进入 §10 的局部图谱；被裁剪的选择算法需要另外标记，不能冒充完整算法。

## 9. 固定 S 与可变 S：都可做，不必预设一个方便仿射面

固定 S 是一个解几何层；主体系不要求 S 仿射或凸。是否存在连续回缩本身就是 C 层的结构限制：若给定 \(D,S\) 不存在连续回缩，则 \(\mathcal C_{D,S}\) 为空，不能通过证书绕过这个拓扑障碍。

在紧 K 上，可把非空紧目标集 \(S\in\mathcal K(K)\) 也作为变量，使用 Hausdorff 度量。关系

\[
\{(T,S):T|_S=I\}
\]

是闭的；再加 \(\operatorname{Fix}T=S\) 是 \(G_\delta\) 条件：存在额外固定点且与 S 距离至少 \(1/m\) 的坏关系为闭集，因 K 紧。

在一致收敛空间中 S 实际由对象决定：

\[
S_T=\Pi_T(K)=\operatorname{Fix}T,
\qquad
d_H(S_T,S_U)\le\|\Pi_T-\Pi_U\|_\infty.
\tag{9.1}
\]

因此可先建立可变解集的无标签 orbit-Polish 空间，再按 S、连通型、维数或其他解几何分类。固定非点 S 只是其中一种后置切片。要求“非单点”即 \(\operatorname{diam}S>0\)，在紧目标集 Hausdorff 空间中是开条件；更多几何层是否 Baire 要另证。

## 10. 局部 germ 版本：用图谱，不先做危险的商

### 定理 L1：共同开输入域上的完整局部图表是闭 Polish 空间

固定非空开集 \(U\subset E=\mathbb R^d\) 与 \(\lambda>0\)。令 \(\mathrm{CL}_*(E\times E)\) 为全部非空闭关系图，使用 Attouch–Wets（AW）拓扑，即图的距离函数在有界集上一致收敛的拓扑。有限维中该 hyperspace 是 Polish；\(C(U,E)\) 使用 compact-open 拓扑，同样 Polish。

对原图点定义线性同胚

\[
L_\lambda(u,v)=(u+\lambda v,u).
\tag{10.1}
\]

它把整个原算子图变成完整 resolvent 关系图。定义

\[
\mathscr L_{U,\lambda}
=\left\{(G,T)\in\mathrm{CL}_*(E\times E)\times C(U,E):
(L_\lambda G)\cap(U\times E)=\operatorname{gph}T\right\}.
\tag{10.2}
\]

则 \(\mathscr L_{U,\lambda}\) 在 AW \(\times\) compact-open 中闭，因而 Polish。它保留整个原图 G，不需要裁掉域外图点，也不需要把局部 T 人工延拓为全空间连续映射。

**双向图极限证明。** 设 \((G_j,T_j)\to(G,T)\)，且每个 \((G_j,T_j)\) 满足 (10.2)。AW 收敛给闭图的内、外 Painlevé–Kuratowski 极限；有限维线性同胚 \(L_\lambda\) 保持这两个图极限，记 \(H_j=L_\lambda G_j\)、\(H=L_\lambda G\)。

第一方向，任取 \(x\in U\)。有 \((x,T_jx)\in H_j\) 且 \((x,T_jx)\to(x,Tx)\)，故图外极限给 \((x,Tx)\in H\)。所以 \(\operatorname{gph}T\subset H\cap(U\times E)\)。

第二方向，任取 \((x,y)\in H\) 且 \(x\in U\)。由图内极限，可选 \((x_j,y_j)\in H_j\) 趋于 \((x,y)\)。因为 U 开，可取 \(r>0\) 使 \(\overline B_r(x)\subset U\)；最终 \(x_j\in\overline B_r(x)\)，所以 \(y_j=T_jx_j\)。于是

\[
\|y_j-Tx\|
\le \sup_{z\in\overline B_r(x)}\|T_jz-Tz\|
   +\|Tx_j-Tx\|\longrightarrow0.
\]

故 \(y=Tx\)，得到反向包含。两方向合并证明闭性。

这里 AW hyperspace 的 Polish 性也可直接由距离函数说明：嵌入 \(G\mapsto d(\cdot,G)\in C_{\mathrm{loc}}(E\times E,\mathbb R)\)。有限维 proper 性保证距离函数的局部一致极限仍为某非空闭集的距离函数：近似最近点在有界球中有收敛子列，既给零点存在，也给正反距离不等式。因此其像闭；可分与完全可度量性随之成立。

### 补充：添加局部 T 坐标没有改变良定对象的原 AW 拓扑

令 \(\mathscr P_{U,\lambda}\) 为所有在 U 上具有完整连续单值 resolvent 的 G。遗忘映射

\[
p:\mathscr L_{U,\lambda}\to\mathscr P_{U,\lambda},
\qquad (G,T)\mapsto G
\]

是同胚，其中右侧使用原 AW 子空间拓扑。因此 \(\mathscr P_{U,\lambda}\) 本身 Polish，且作为 AW Polish 空间的子集为 \(G_\delta\)。这一点消除了“只因增添一个 T 标签才变成好空间”的疑问。

证明逆映射连续：设 \(G_j\to G\)，且所有对象均在该良定局部类。若 \(T_j\not\to T\) compact-open，则取紧 \(K\subset U\)、\(x_j\in K\)、\(\varepsilon>0\) 使 \(\|T_jx_j-Tx_j\|\ge\varepsilon\)。抽子列后 \(x_j\to x\in U\)。图内极限另给 \(z_j\to x\)、\(T_jz_j\to Tx\)。由 T 连续，最终 \(\|T_jx_j-Tx\|\ge3\varepsilon/4\) 而 \(\|T_jz_j-Tx\|<\varepsilon/4\)。短线段 \([z_j,x_j]\) 最终位于 U 的一个内球中；\(T_j\) 连续，故存在 \(w_j\in[z_j,x_j]\) 使

\[
\|T_jw_j-Tx\|=\varepsilon/2.
\]

有限维球面紧性给子列 \(T_jw_j\to y\) 且 \(\|y-Tx\|=\varepsilon/2\)。而 \(w_j\to x\)，图外极限迫使 \((x,y)\in L_\lambda G\)，违背 G 在 x 的完整单值性。矛盾证明局部一致收敛。这里使用了开域内短线段与有限维球面紧性，不向任意闭域或无限维 Hilbert 无条件推广。

### 开输入域与严格内 collar 的必要性

若 U 只要求闭，(10.2) 可以不闭。取 \(E=\mathbb R\)、\(D=[0,1]\)，在 resolvent 坐标中令

\[
H_j=D\times\{0\}\ \cup\ \{(-1/j,1)\},
\qquad T_j\equiv0\text{ on }D.
\tag{10.3}
\]

每个 \(H_j\cap(D\times E)\) 都恰是 \(\operatorname{gph}T_j\)，但 Hausdorff、从而 AW 极限为

\[
H=D\times\{0\}\ \cup\ \{(0,1)\},
\]

在边界输入 0 多出一个完整分支。取 \(G_j=L_\lambda^{-1}H_j\) 即得原算子图版本。失效机制是域外分支进入闭域边界；最弱修复为共同开输入域，或将实际比较输入固定在严格内 collar 中。

### 局部轨道图谱与 germ 属性

纯局部问题宜标记初值闭块 B、轨道闭工作 collar \(W\subset U\) 与原图 G；如证书另用输出／残差 collar，也一并标记。对每个固定 B 和 W，要求所有比较轨道留在 W；不要求 B 本身前向不变。在 (10.2) 的完整局部图表上，另记录

\[
\Phi_n:B\to W,\quad \Phi_0=I_B,
\quad\Phi_{n+1}=T\circ\Phi_n,
\quad\Phi_\infty(B)\subset S.
\tag{10.4}
\]

当 \(B,W,S\) 是固定的相应闭集、\(B,S\subset W\subset U\)，并保留 \(T|_S=I\) 时，上述闭轨道表示与一致尾层证明仍成立：有限轨道像落在 W 内的紧块，T 的 compact-open 收敛足以通过复合极限。若 B 紧，可直接使用 \(C(B\times\widehat{\mathbb N},E)\)；闭而不紧的 B 使用逐紧集版本。整个 G 坐标继续保留，故域外逆纤维没有被遗忘。

关于某个固定解点的 germ 性质写成“存在某个有理半径／内 collar 使性质成立”。这允许按可数半径组织证书，但**不自动保证这些层的并 Baire**。

不要先按“某个更小邻域相等”把全体映射取 germ 商，再假定该商 Hausdorff 或 Polish。更不能因两个映射在输入 germ 相同，就认为其原算子最小残差相同；同一输出的域外逆像仍可能不同。推荐保留带区域标记的图谱与显式限制映射，比较时说明是完整原算子还是局部算法行为。

## 11. 更大备选：完整集合值 PPA 关系空间

为了容纳完整 resolvent 真正多值的 LTT／selection-uniform 框架，可从紧域闭关系出发。令 \(\mathcal K(K\times K)\) 为非空紧子集的 Hausdorff hyperspace，定义

\[
\mathcal A_{\rm rel}(K,S)
=\{G\in\mathcal K(K\times K):\pi_1G=K,
\ \{(s,s):s\in S\}\subset G\}.
\tag{11.1}
\]

这是紧 Polish 空间：全覆盖和指定对角图点包含在紧 hyperspace 中均为闭条件。坐标变换

\[
(x,u)\mapsto(u,(x-u)/\lambda)
\]

仍给完整 PPA 关系。

(11.1) 只要求解点处允许驻定选择，仍可能允许其他输出。若要把单值 P2 的“到解即驻定”改成**所有选择都驻定**，须再要求 \(G(s)=\{s\}\) 对每个 \(s\in S\) 成立；它是这里的 \(G_\delta\) 子条件，而不是自动包含在 (11.1) 中。其补可按输出距 s 至少 \(1/m\) 的坏图点写成可数个闭集。

其中每个输入纤维为单点的子类是 \(G_\delta\)：对每个 \(m\) 要求不存在同输入的两个输出相距至少 \(1/m\)。由于 K 紧，“存在此坏三元组”的关系闭。单值闭关系在紧域上连续，其 Hausdorff 图拓扑与一致映射拓扑对应。

集合值层须另外区分：

- 所有可选轨道均收敛；
- 每个初值存在某条收敛轨道；
- 所有选择是否收敛到同一点。

它们不是同一类别。多值层的收敛性可通过路径空间编码，但本报告没有完成其对应的 B、C 的 Polish 定理；不能把单值证明不加修改套用。这是有内容的备选扩张，不是当前主比较的先决任务。

## 12. 接下来可以问的真正结构问题

选定上述中立空间后，各理论可放进同一张结构分类表，而不立即预设谁第一纲：

| 结构坐标 | 中立定义／问题 | RLEB／LT 应回答什么 |
|---|---|---|
| 完整单步几何 | 图、完整纤维、单步或反射连续模 | 哪种理论推出哪种正则类，是否只给充分性 |
| 收敛与尾谱 | 属于 B、C 或哪些 \(\mathcal E_\varepsilon\) | 推出何种统一尾、是否允许任意慢率 |
| 有限长度 | \(\sum_n\|T^{n+1}x-T^nx\|<\infty\) | 给出点态或共同长度预算 |
| 极限回缩 | \(\Pi_T\)、其连续模、可定义性 | 额外条件如何约束极限映射 |
| 稳定纤维 | \(\Pi_T^{-1}(s)\)、\(D/\!\sim_T\cong S\) | 是否有正则层叶、同胚稳定性或退化 |
| 算子扰动 | 单步拓扑与全轨道拓扑 | 两套理论在何种预算下给对象稳定性 |
| 可认证覆盖 | 认证 witness 关系投影后的对象集合 | 在已定母空间内比较内部、稠密性、纲、相对边界 |

把某个理论条件投影成“可认证对象类”之后再研究大小。若两套理论给出的动力学保证不同，应先在共同保证层上比较，再研究它们分别进入哪些更强结构层。

所有范畴结论必须写明母空间与拓扑。连续嵌入或普通遗忘投影不足以传递 residual／meagre；需要同胚、明确的范畴保持映射，或独立的密度证明。尤其不能把先前尖点层的 residual 直接限制到本报告的 C，也不能反向推广。

## 13. 推荐架构与两个备选

### 最推荐：A 主空间 + C 内生动力学空间 + 共同尾预算桥

1. 以全部连续完整 fixed-step PPA 的 \(\mathcal A\) 为主空间，使用原始单步 compact-open 拓扑。这里不先假定收敛。
2. 把“全部逐点收敛者”B、“紧集上一致收敛者”C 作为中立动力学子类；C 通过轨道紧化获得不带速率标签的 Polish 架构。
3. 把共同实际尾层 \(\mathcal E_\varepsilon\) 作为强弱拓扑的桥。在这些层内做严格 category 比较，不让证书编码决定对象重数。
4. 各理论通过完整接口和共同域嵌入到这套结构中；先问其结构后果，再问认证类的纲。

这最接近用户要求的“先有体系，再换视角比较”，同时保留可操作的 Baire 工具。没有理由把 \(\mathcal C_P\) 升为这套体系的总母空间；它只能是后置的一个认证预算子类。

### 备选一：直接以全部 B 为母空间

若用户坚持“所有逐初值 PPA 收敛者，一律不排除不连续极限”，可以直接使用 \((\mathcal B_{D,S},d_{{\rm orb},D})\)。它完备 Baire，覆盖目标最广；代价是一般非可分，且其 category 不等于单步拓扑的 category。适合先研究收敛性与吸引纤维，描述集合工具较少。

### 备选二：从闭集合值关系开始

若优先统一完整多值 LTT 与 selection-uniform RLEB，则从 (11.1) 的紧关系母空间起步，再建立路径空间上的收敛与极限关系。它覆盖最全，但“极限映射”可能变成集合值极限关系，工作量显著增加。应把所有选择／存在选择的量词作为第一层公理，不能延后。

## 14. 已证明、未证明与应提交审核的承重命题

本报告已给出独立证明：完整 resolvent 表示；A 的 Polish 性与精确固定集 G_delta；B 在轨道度量下的完备性；B 可非可分；C 的闭轨道紧化表示与 Polish 性；极限回缩和商结构；共同尾预算层闭性以及两拓扑等价；中立俘获预算引理；固定／可变 S 的基本处理。

其中 B 的完备性、非可分例子、C 的 Polish 表示及共同尾层拓扑等价，已送 `axiom_system_stress` 独立核对，反馈通过。二轮架构审计进一步核准承重定理，并要求补成 §10 的共同开输入域完整局部图表闭性；本版已给出双向图极限证明及闭域边界反例。最终统稿仍应逐项核对各理论实例的完整身份和共同域，不得把图表存在性误作某个具体证书已通过。

没有证明的事项：RLEB／LT 在任何新母空间中的第一纲或余稀；全部连续局部图块到全空间完整算子的无损延拓；全部多值选择收敛空间的 Polish 性；无限维 Hilbert 原样推广；跨步长 existential 投影的范畴保持；本报告组织定理的文献优先权。

**建议本轮的结论是：已建立可供后续比较的中立母体系及其数学基础；没有资格在体系内的认证类比较尚未完成前，给 RLEB／LT 的总大小或价值下终判。**
