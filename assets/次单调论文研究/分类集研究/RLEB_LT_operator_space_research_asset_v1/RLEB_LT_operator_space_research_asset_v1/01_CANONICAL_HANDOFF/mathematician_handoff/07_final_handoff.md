# RLEB–Luke–Tam 体系比较：数学家团队正式交接

日期：2026-09-20。用途：研究问题定义、障碍定位、构建路线与团队交接。版本：本轮数学审计修订后的综合稿。

本稿综合本目录 `01–06`，以 `06_math_audit.md` 的独立复核及 `02`、`04` 的随后修订为准。原 RLEB 论文按已经建立的基础使用；仅调用下述完整图、RL、真实 EB、兼容性和局部化接口，不重审无关内容。“已证／已核”不等于已获外部同行评审，也不等于文献首创性已经确认。

## 阅读首页：结论、停点与请团队提供的 idea

### 1. 直接回答作者

**“先完成仿射解集＋正常收缩＋非退化切向漂移层”本身不能完成理想意义下的 RLEB–LT 比较。** 它不是毫无价值的初等例子：已有的是作用于一个函数结构层、保持完整图和真实 EB 的构建工具。但在没有证明该层的母空间位置、代表性与类别转移以前，它仍是局部工具，不能代替“先建立中立体系，再比较两个认证类”的主问题。

目前既没有证明理想方向做不到，也没有证明 RLEB 在中立总空间中泛型地强于 LT。已经严格否定的是若干捷径：用任意最大空间直接数纲、默认 RLEB 自身 Baire、把证书或步长投影当作保纲、把稍放宽尾预算当作同尾、把局部动力学当作完整原图。

### 2. 本轮真正新增、可以接着用的体系结果

在固定非空紧状态空间 \(K\subset\mathbb R^d\)、固定非空闭集 \(S\subseteq K\) 的**完整紧源、T-only** 图卡内，对所有一致收敛到 \(S\) 的连续自映射，内生观测

\[
\Phi(T)=\bigl(\text{实际全时间尾 }w(T),\ \text{实际反射模 }m(T)\bigr)
\]

已经独立证明是 continuous proper 映射；其实际像闭且 Polish，精确纤维紧／Baire，映射到实际像是 perfect／quotient。这里的“新增”只指本轮取得，不是优先权判决。

这推进了真正的体系构建，但还缺两条承重桥：

- **类别桥：**proper、闭、商映射、紧纤维均不自动推出 category-preserving；尚不能将纤维内的“典型”提升为母空间“典型”。
- **全原图桥：**一个局部 \(K\) 上的观测看不见域外图。它不能控制原算子的全部逆纤维和真实 EB，不能无条件将上述 properness 提升到任意完整 \(F\) 的局部 atlas。

### 3. 请数学家团队首先回答

> 在事先固定的中立良定／收敛 PPA 空间中，能否找到由真实轨道、完整反射模和真实残差唯一决定的结构，使其既有可用的 Baire 分解，又能将 RLEB／LT 证书化为对象性质，并合法比较这些对象类？若不能，具体阻断是类别语言分辨率、域外纤维、精确尾刚性，还是分层到母空间的投影失败？

最低有意义正结果不是再找到一个非 LT 算子，而是在一个**未预装漂移、尖点或特定 Hölder 指数**的中立 Baire 图卡 \(X\) 中证明

\[
\mathcal R\setminus\mathcal L_{\rm ap}\text{ 在 }X\text{ 中非第一纲},
\tag{H0}
\]

或给出完整内生分层及保纲提升定理。如果证明两类在该自然空间中都第一纲，应如实得到“这种大小语言无鉴别力”的结论，转向经论证的细尺度剖面；不是强行换一个有利分母。

### 4. 首攻排序

先做 **中立分母的非退化性／局部紧诊断** 与 **\(\Phi\) 的类别保持／全图提升**；同时研究 **联合残差—模表示**。同尾选择、局部替换与仿射漂移变形只作为这些主问题的构建手段。多值全选择与无限维状态推广后置。

---

## 1. 研究目标与比较口径

作者的目标是比较理论覆盖，不是比较几个例子。在独立于证书标签的空间 \(X\) 中定义

\[
\mathcal R=\mathcal R_D\cup\mathcal R_E,\qquad
\mathcal L=\mathcal L_{\rm ap},
\tag{1.1}
\]

分别研究共同部分、真正差集、两者都不能认证的部分。固定共同接口时，LT 公共 all-pairs 证书进入 RLEB-energy 已经有转换；**包含号不是当前主瓶颈**。

“RLEB 比 LT 多”有不同强度，必须分别报告：

| 强度 | 数学含义 | 当前状态 |
|---|---|---|
| 严格多出成员 | \(\mathcal R\setminus\mathcal L\ne\varnothing\) | 已有受核构造 |
| 一个结构层内典型新增 | 在指定结构层中，差集余稀／LT 第一纲 | 已有受限层结果 |
| 中立母空间中有厚度 | (H0)，或一个中立开区域上差集余稀 | 真正未决 |
| 全分层的体系比较 | 统一分类规则＋各层母空间位置＋合法类别转移 | 真正未决 |
| 新增原算子而非步长实例 | 同一 \(F\) 有 RLEB 步长，但任何正步长均无 LT 证书 | 有受限构造；中立母空间大小未决 |

不得作以下替代：

- 层内余稀不等于母空间非第一纲；无限维、闭凸、层自身 Baire 也不能补这个推理。
- 证书空间中的大小不等于原对象像的大小；对象只计一次。
- 实际尾 \(w\) 不等于某份证明给出的保守尾；“实际性能相同”和“认证性能相同”是两道问题。
- 第一纲不是零测、概率零或覆盖百分比；大也不自动等于好、新或可投稿。
- 允许缩域的 germ、固定宏观域、完整紧源图卡必须分开。不能临时缩域或裁图后仍称同一问题。

## 2. 统一符号与对象层

首阶段取有限维状态空间 \(E=\mathbb R^d\)，保留原欧氏几何；其连续映射／闭图算子空间仍是无限维研究对象。

### 2.1 原算子、完整 resolvent 与局部观测

原对象是非空闭图 \(G=\operatorname{gph}F\subset E\times E\)。固定 \(\lambda>0\)，令

\[
L_\lambda(u,v)=(u+\lambda v,u),\qquad
\Gamma_{F,\lambda}=L_\lambda G=\operatorname{gph}J_{\lambda F}.
\tag{2.1}
\]

共同开输入域 \(U\) 上的完整单值连续性是

\[
\Gamma_{F,\lambda}\cap(U\times E)=\operatorname{gph}T_F,\qquad T_F\in C(U,E),
\tag{2.2}
\]

不是仅选取一个满足 \(T_Fx\in J_{\lambda F}(x)\) 的分支。全步长关系满足

\[
y\in J_{\lambda F}(x)
\iff
y\in J_{\mu F}\!\left(\frac\mu\lambda x+
\left(1-\frac\mu\lambda\right)y\right).
\tag{2.3}
\]

全域完整 \(T=J_{\lambda F}\) 唯一恢复原图：

\[
F(u)=\{(x-u)/\lambda:Tx=u\}.
\tag{2.4}
\]

局部 \(T|_U\) 一般不能恢复 \(F\)。另一个合法但不同的对象是：**从一开始**把原算子定义为完整紧源图

\[
F_{T,K}(u)=\{(x-u)/\lambda:x\in K,\ Tx=u\},\qquad T:K\to K.
\tag{2.5}
\]

此时 \(J_{\lambda F_{T,K}}\) 的输入域恰为 \(K\)，且 \(T\) 决定全部原图。不得从已有全局 \(F\) 删除外部图点后，声称 (2.5) 是无损坐标变化。

### 2.2 共同规格与真实残差

固定零集 \(S=\operatorname{zer}F\)，通常非单点；固定紧初值块 \(B\)、紧工作块 \(W\Subset U\)，要求

\[
B\subset W,\qquad T_F^n(B)\subset W\quad(n\ge0).
\tag{2.6}
\]

\(B\) 不默认前向不变。RL 的共同测试域取包含 \(W\) 与其最近解点的紧集 \(H\Subset U\)；真实 EB 另固定输出域 \(V\)。所有半径、域、步长组成规格 \(P\)，不得在证明中暗改。

\[
r_F(u)=\inf\{\|v\|:(u,v)\in G\},\qquad
r_F(u)=\lambda^{-1}\inf_{Tx=u}\|x-u\|\quad\text{（全域完整坐标）}.
\tag{2.7}
\]

空纤维取 \(+\infty\)。有限维非空闭纤维的 inf 取得。某条 transition 只给

\[
r_F(Tx)\le\|x-Tx\|/\lambda;
\]

不能反过来把所选残差当成整个多值算子的最小残差。

### 2.3 层次与量词

| 层 | 对象 | 主要拓扑／信息 |
|---|---|---|
| 本体 | 完整闭图 \(F\) | Attouch–Wets（AW）图拓扑 |
| 良定算法 | 完整连续单值 \(J_{\lambda F}\restriction_U\) | 原图保留；非任选分支 |
| 轨道／策略 | \(F,\lambda,x_0\)，或 \(F,(\lambda_k),x_0\) | 固定步长／存在步长／所有策略分开 |
| 动力学 | 逐点收敛、局部一致收敛、有限长度、极限映射 | 原范数、全部初值、实际尾 |
| 证书像 | direct、energy、LT all-pairs、LTT pointwise | 无标签对象一次计数 |

“固定 \((F,\lambda)\)”比较算法实例；“同一个 \(F\) 存在某步长”比较原算子。完整多值时，还须区分存在选择与全部合法选择。当前成熟主干是固定步长、完整单值、有限维状态，不是无条件覆盖所有 PPA。

## 3. 两理论进入体系的共同接口

记 \(R_T=2T-I\)、\(d=d(x,S)\)、\(d^+=d(Tx,S)\)、\(s_x=\|x-Tx\|\)。以下都配完整覆盖、共同局部化与留域接口。

### 3.1 RLEB-direct 与 RLEB-energy

\[
\|R_Tx-R_Ty\|\le L\|x-y\|^\gamma,\quad0<\gamma\le1,
\qquad d(u,S)\le\psi(r_F(u)).
\tag{3.1}
\]

RL 是所声明测试域和尺度上的 **all-pairs** 条件；EB 对全部原纤维成立。Direct 兼容为

\[
h(r)=\frac{r+Lr^\gamma}{2\lambda},\qquad
\psi(h(r))\le\kappa r,\quad\kappa<1.
\tag{3.2}
\]

Energy 取普通连续严格增 gauge 的逆 \(\alpha=\psi^{-1}\)，要求

\[
A(r)=\frac{r^2+L^2r^{2\gamma}}2,\qquad
V(r)=r^2+\lambda^2\alpha(r)^2,\qquad A(r)\le q_E V(r),\quad q_E<1.
\tag{3.3}
\]

接口导出 \(s_x\le(d+Ld^\gamma)/2\)、\((d^+)^2+s_x^2\le A(d)\)。因此 direct 给 \(d^+\le\kappa d\)，energy 给 \(V(d^+)\le q_EV(d)\)。一般 energy gauge 不自动给距离自身的固定 Q-线性因子。

共同初值距离不超过 \(D\) 时，保守点尾可取

\[
e_n^D=\frac12\left(\frac{\kappa^nD}{1-\kappa}+
\frac{L\kappa^{\gamma n}D^\gamma}{1-\kappa^\gamma}\right),
\qquad e_n^E=\frac{q_E^{(n+1)/2}\sqrt{V(D)}}{1-\sqrt{q_E}}.
\tag{3.4}
\]

### 3.2 LT 的比较基准

\(\mathcal L_{\rm ap}\) 指 Luke–Tam 2025 公共 all-pairs 定量接口，不自动代表全部早期 LTT pointwise／多值框架：

\[
\|R_Tx-R_Ty\|\le\sqrt{1+4\tau}\|x-y\|,\qquad
d(u,S)\le\rho r_F(u),\qquad
2\tau(\lambda+\rho)^2<\lambda^2.
\tag{3.5}
\]

取 \(\gamma=1\)、\(L^2=1+4\tau\)、\(\alpha(r)=r/\rho\)，可得

\[
q_E=(1+2\tau)\frac{\rho^2}{\rho^2+\lambda^2}<1.
\tag{3.6}
\]

故在完整接口和域已对齐的口径中，\(\mathcal L_{\rm ap}\subseteq\mathcal R_E\subseteq\mathcal R\)。一步终止或负 violation 可按相应退化情形单列／放宽处理。

此转换不承诺逐项保存 LT 最优尾、最大初值域或所有历史 LTT 假设。较早 pointwise almost-averaged 类另记 \(\mathcal L_{\rm pt}\)；不作其无条件包含于强 all-pairs 单值 RLEB 的宣称。

## 4. 四状态清单：哪些可用，哪些绝不能提前宣布

| 状态 | 项目 | 已达到的准确范围 |
|---|---|---|
| **已证／已核** | 完整图—resolvent 坐标、开输入良定 atlas | 有限维原图框架；良定原图类的 AW Polish／\(G_\delta\) 结构已有基础证明 |
| **已证／已核** | 全时间收敛空间 | 逐初值层可完备／Baire但不必可分；局部一致层 Polish；局部原图版本保留基图坐标 |
| **已证／已核** | 共同实际尾层 | 相对闭／Polish；同层单步与全时间拓扑一致 |
| **已证／已核** | 对象侧证书编码 | 完整紧源图卡的认证像 \(K_\sigma\)；固定锚点、允许缩域 germ 的存在实步长类 \(F_\sigma\) |
| **已证／已核** | LT→energy | 共同 all-pairs 完整接口，见 (3.5)–(3.6) |
| **已证／本轮独立复核** | \(\Phi=(w,m)\) | 紧 T-only、全时间拓扑下 continuous proper；闭 Polish 实际像、紧 Baire 纤维、perfect／quotient |
| **严格 no-go** | 无条件的纲与投影推断 | 最大闭图可解性退化、自第一纲反例、任意 witness 投影不保纲、proper 不自动保纲 |
| **严格 no-go** | 若干简单构建捷径 | 精确尾不开放、实步长不能普遍有理化、局部轨道不决定真实 EB、保残差阶的共轭不能任意爆破位移 |
| **候选已审** | Lyapunov 塔／后继选择 | 充分的保尾与真 EB 种子引理正确；丰富选择、母空间覆盖、strict RLEB 闭合未证 |
| **候选已审** | \(\sigma\)-紧 Baire 诊断、紧域非扩张满射 | 种子定理正确；没有替目标空间判定答案 |
| **候选已审** | 仿射非退化漂移变形 | 受限结构层中保真 EB、严格 RLEB、任意步长 LT 排除；同尾、宏观同域、母空间位置仍缺 |
| **真正未决** | 理想差距 | 中立空间中的绝对类别／非第一纲差集、全剖面分类及合法提升 |
| **真正未决** | 全原图／类别桥 | \(\Phi\) 是否保纲、怎样加入域外图、实步长对象投影的类别 |

“候选已审”表示**工具的种子命题已核准**，不是整条路线或目标分类已经成立。原稿中把 \(\Phi\) 的紧纤维、Polish 像也列为未知的旧句，已由本轮定理关闭；不能继续作为瓶颈重复报告。

## 5. 三个真正的主问题

### Q-AW：原图观测下，认证类位于哪里？

在预先固定、非空的中立良定 atlas \(\mathfrak A_P\) 或共同留域层中，采用原 AW 相对拓扑，求

\[
\operatorname{int}\mathcal R,\quad\overline{\mathcal R},\quad
\operatorname{int}\mathcal L,\quad\overline{\mathcal L},\quad
\operatorname{Cat}(\mathcal R\setminus\mathcal L).
\tag{5.1}
\]

这里不预设收敛，两理论各自认证哪些良定实例进入收敛层。如果目标集有 Baire property，可用其模第一纲的唯一 regular-open 代表 \(\mathsf U_C\) 表示局部类别覆盖支撑。对 \(\mathcal L\subseteq\mathcal R\)，

\[
\mathsf U_{\mathcal L}\ne\mathsf U_{\mathcal R}
\iff \mathcal R\setminus\mathcal L\text{ 非第一纲}.
\tag{5.2}
\]

这是标准 Baire 代数，不是原创主张。如果两类都第一纲，支撑同时为空；应承认该尺度不能分辨。

### Q-DYN：全部约定收敛者中，两理论认证了哪些系统？

在同一规格中定义 \(\mathfrak C_{\rm pt}(P)\) 与 \(\mathfrak C_{\rm lu}(P)\)：前者全部初值点收敛到 \(S\)，后者还在共同紧初值块上一致。局部原图版本采用

\[
\rho_{\rm dyn}(F,G)=\rho_{\mathfrak A}(F,G)+
\sup_{n\ge0}\min\{1,\|T_F^n-T_G^n\|_B\},
\tag{5.3}
\]

保留完整原图。全域 T-only 版本可用紧耗尽的全时间距离。

这最接近“所有使 PPA 收敛的算子空间”，但必须声明当前包含的是哪一种收敛、哪一种选择量词。母空间已经假定的收敛，不能再当作 RLEB 单独取得的优势。须在母空间同时判定 \(\mathcal R,\mathcal L,\mathcal R\setminus\mathcal L\)，而非先默认 \(\mathcal R\) 自身是 Baire 分母。

### Q-PROFILE：内生全分层怎样给总体比较？

对固定非空紧 \(K\)、固定非空闭集 \(S\subseteq K\)，令

\[
X=\{T\in C(K,K):T|_S=I, T^n\to\Pi_T\text{ 一致},\ \Pi_T(K)\subseteq S\},
\qquad \rho(T,U)=\sup_{n\ge0}\|T^n-U^n\|_K.
\tag{5.4}
\]

若 \(S\) 不是 \(K\) 的回缩像，\(X\) 可能为空。以下非空 Baire 主张均保留非空前提。定义

\[
w_n(T)=\max\left\{
\sup_{k,\ell\ge n}\|T^k-T^\ell\|_K,
\sup_{k\ge n}\sup_{x\in K}d(T^kx,S)\right\},
\tag{5.5}
\]

\[
m_j(T)=\sup_{\substack{x,y\in K\\\|x-y\|\le2^{-j}}}
\|(2T-I)x-(2T-I)y\|,\qquad \Phi(T)=(w(T),m(T))\in c_0\times c_0.
\tag{5.6}
\]

两份 \(c_0\) 使用上确界范数。这些是对象自身唯一确定的实际量，不是任意可选证书标签。对全部非增非负零列 (e,h) 取预算层

\[
D_{e,h}=\{T:T|_S=I, w(T)\le e, m(T)\le h\}.
\tag{5.7}
\]

研究的是**全部**实际尾—模层的认证类别剖面及其转移，而非看到 Hölder 层有利以后只选 \(h_j=L2^{-j\gamma}\)。还应加入完整原图上的残差包络

\[
b_{F,V}(t)=\sup\{d(u,S):u\in V,\ r_F(u)\le t\},
\tag{5.8}
\]

空上确界取零。原始包络未必是合法普通 gauge；连续性、半连续性、majorant 重构和兼容条件均需证明。

### 5.4 已证观测定理：proper 的基底与紧纤维

**定理 P（本轮独立复核）。** 对 (5.4)–(5.6)，\(X\) Polish，\(\Phi:X\to c_0\times c_0\) 连续且 compact-preimage proper；\(Z=\Phi(X)\) 闭且 Polish；\(\Phi:X\to Z\) 是 perfect／quotient；每个非空精确纤维紧且 Baire。

**证明骨架。** \(T\mapsto(T^n)_{n\ge0}\) 把 \(X\) 表示为一致收敛序列空间 \(c(C(K,K))\) 的闭子空间：\(f_0=I\)、\(f_{n+1}=f_1\circ f_n\)、\(f_1|_S=I\)、极限落在 \(S\) 都是闭条件。因此 \(X\) Polish。直接估计给

\[
\|w(T)-w(U)\|_{c_0}\le2\rho(T,U),\qquad
\|m(T)-m(U)\|_{c_0}\le4\|T-U\|_K\le4\rho(T,U).
\tag{5.9}
\]

每个 \(D_{e,h}\) 的有限迭代约束闭，而

\[
\|Tx-Ty\|\le\tfrac12(h_j+2^{-j})\quad(\|x-y\|\le2^{-j})
\tag{5.10}
\]

给共同等度连续性；Arzelà–Ascoli 给单步紧性。共同尾给

\[
\|T_i^n-T^n\|_K\le2e_N+\|T_i^N-T^N\|_K\quad(n\ge N),
\tag{5.11}
\]

所以单步紧性提升为全时间紧性。若 \(Q\subset c_0\times c_0\) 紧，有限 \(\varepsilon\)-网给统一趋零包络

\[
e_n=\sup_{(a,b)\in Q}\sup_{k\ge n}|a_k|\to0,\qquad
h_j=\sup_{(a,b)\in Q}\sup_{i\ge j}|b_i|\to0.
\tag{5.12}
\]

故 \(\Phi^{-1}(Q)\) 是某个紧 \(D_{e,h}\) 的闭子集。度量空间间这个 compact-preimage 性给闭映射：对收敛像序列，用该序列及其极限组成的紧集抽取原像子列即可。闭像、紧纤维、perfect／quotient 随之得到。完整证明见 `06_math_audit.md` §1。

**两条不可删的边界。**

1. proper 不自动保纲。例如
   \[
   p:[-1,1]\to[0,1],\quad p(x)=\max\{x,0\}
   \tag{5.13}
   \]
   连续、proper、闭满射、紧纤维，但 \(p^{-1}(\{0\})=[-1,0]\) 有内点，而目标单点无处稠密。它否定一般推理，不是已经反证具体 \(\Phi\) 保纲。
2. 此定理限于完整紧源／T-only 图卡。原全局 \(F\) 的局部 \(\Phi_K\) 纤维可不紧，见 O9。向完整原图 atlas 的提升必须另证。

仅尾坐标 \(w\) 的精确纤维已经闭、Polish／Baire；缺少反射模时，不能据此证明紧纤维或闭像。**下一步未知的是保纲和全图提升，不再是这里的 Polish 基底是否存在。**

## 6. O1–O12：障碍类型、最小公式与可绕过边界

### O1｜量词阻碍：算法实例、原算子和策略不是同一集合

取闭图 \(F(0)=\mathbb R\)、\(F(u)=\{-u/2\}\ (u\ne0)\)，则

\[
J_F(x)=\{0,2x\}.
\tag{O1a}
\]

存在一步终止选择，也存在发散选择。另取 \(F=I\)，每个固定正步长收敛，但

\[
x_n=x_0\prod_{k<n}(1+\lambda_k)^{-1},\qquad\lambda_k=2^{-k-1}
\tag{O1b}
\]

对非零初值有非零极限。每个固定步长切片小，也不能对不可数步长取并后断言小。**类型：严格逻辑 no-go；修复：先固定全部量词。**

### O2｜最大空间退化：一步有解已第一纲

在最大非空闭 resolvent 关系 AW 空间中，固定非解输入 \(x_0\)，

\[
\{\Gamma:\Gamma(x_0)\ne\varnothing\}
=\bigcup_{m\ge1}\{\Gamma:\Gamma\cap(\{x_0\}\times\overline B_m)\ne\varnothing\}.
\tag{O2}
\]

每个命中固定紧集的块闭；有限图网的输入微移可避开 \(x_0\)，故无处稠密。固定 exact-\(S\)、\(x_0\notin S\) 时保留 \(\Delta_S\) 仍成立。两理论先被共同可解性一起压成小类。**类型：该口径下严格无鉴别力；修复：最大空间保留作本体，比较转入无标签良定层。**

### O3｜拓扑阻碍：单步接近不控制全时间

在 \(K=[0,1]^2,S=[0,1]\times\{0\}\)，令

\[
f_\varepsilon(r)=\begin{cases}
(1-\varepsilon^2)r,&r\le\varepsilon,\\
\varepsilon-\varepsilon^3+\varepsilon^2(r-\varepsilon),&\varepsilon\le r\le2\varepsilon,\\
r/2,&r\ge2\varepsilon,
\end{cases}
\quad T_\varepsilon(s,r)=(\min\{1,s+\varepsilon r\},f_\varepsilon(r)).
\tag{O3a}
\]

\(T_0(s,r)=(s,r/2)\)。全部 exact-\(S\)、一致收敛，且 \(T_\varepsilon\to T_0\) 单步一致；但从 \((0,\varepsilon)\) 的累计切向位移为 \(\sum_n\varepsilon^2(1-\varepsilon^2)^n=1\)，故

\[
\|\Pi_{T_\varepsilon}-\Pi_{T_0}\|_\infty=1.
\tag{O3b}
\]

共同实际尾时 (5.11) 才给同拓扑。**类型：真 no-go；尚缺总空间保纲／不可转移定理。**

### O4｜相对纲退化：RLEB 并类可以自第一纲

在中立一步回缩空间

\[
K=[-1,1]\times[0,1],\ S=[-1,1]\times\{0\},\quad
\mathscr M=\{T\in C(K,S):T|_S=I\},
\tag{O4a}
\]

全部系统一步终止，完整紧源 EB 左端为零。RLEB 对象类恰为具有某个正 Hölder 指数的回缩并类

\[
\mathscr H=\bigcup_{m,n\ge1}\{T:\|Tx-Ty\|\le n\|x-y\|^{1/m}\}.
\tag{O4b}
\]

每块在 \(\mathscr H\) 自身中闭无处稠密：保 \(S\)-trace 的分片仿射逼近后，在内部加入更低指数的小 Hölder 增量即可。故 \(\mathscr H\) 自第一纲；其中每个子集都相对第一纲。**类型：严格反例；没有证明所有 RLEB 分母都退化。必须先验证所选分母 Baire／非自第一纲。**

### O5｜描述与投影阻碍：可编码不等于有大小判决

连续开放投影 \(p:\mathbb R^2\to\mathbb R\) 将无处稠密横轴映为全部底空间。保纲规则针对饱和逆像 \(p^{-1}(A)\)，不是任意 witness 子集及其像。

本轮独立核准的诊断是：若度量空间 \(Y=\bigcup_nK_n\)、各 \(K_n\) 紧，则

\[
Y\text{ Baire}\iff\bigcup_n\operatorname{Int}_Y K_n\text{ 在 }Y\text{ 稠密}.
\tag{O5}
\]

等价地，内生局部紧点集稠密。若中立空间处处非局部紧而两个认证像都是 \(K_\sigma\)，两者必第一纲；但现有 \(K_\sigma\) 定理不能无证外推到未控域外原图。**类型：严格逻辑阻断＋可用诊断；目标类实际满足哪一边仍未决。**

### O6｜解集与收敛几何：统一回缩不等于所有点收敛

一致极限 \(\Pi:K\to S\)、\(T|_S=I\) 强迫 \(S\) 为 \(K\) 的连续回缩像。取 \(K=[0,1]\)、\(S=\{0,1\}\)，无连续回缩，但

\[
T(x)=2x-x^2
\tag{O6}
\]

每条轨道点收敛：零固定，正初值趋一。故 pt 层非空、lu 层为空。距离到 \(S\) 趋零还可以不点收敛，见 `03` §8 的旋转模型。**类型：真几何阻断；必须分层，不可把 lu 偷换成全部收敛者。**

### O7｜同尾同域闭合：小改变仍可能越过精确预算

对 O4 的底边投影 \(P(s,r)=(s,0)\)，

\[
T_{\varepsilon,a}(s,r)=(s,a\min\{r,\varepsilon\}),\quad
\rho(T_{\varepsilon,a},P)\le\varepsilon,\quad
\sup_Kd(T_{\varepsilon,a}^nx,S)=\varepsilon a^n.
\tag{O7a}
\]

对任意指定零尾 \(e\)，可取 (N,a) 使 \(\varepsilon a^N>e_N\)。近恒等完整共轭一般只给

\[
\mathfrak D_e\longrightarrow\mathfrak D_{(1+\eta)e},
\tag{O7b}
\]

不是同一分母内稠密性。若 \(e_0=\sup_Bd(x,S)>0\)，所有 \(\mathfrak D_{ce}\ (c<1)\) 甚至为空。仅收紧后段或加初段 slack 是不同的明确修订。

也不存在支配所有实际零尾的可数速率表：给任意严格下降 \(b_n\downarrow0\)，插值 \(f(b_n)=b_{n+1}\) 可实现 \(\sup f^n=b_n\)，再对可数表作对角化。**类型：稳定性 no-go＋未决的同层构建／跨尺度桥。缩小 germ 不能冒充原宏观域。**

### O8｜步长谱：严格局部证书不保证开窗口

给非空紧 \(A\Subset(1,\infty)\)、\(C>\max\{1,\max A\}\)，定义

\[
G_A=\{(u,u):u\in\mathbb R\}\cup
\left\{\left(\frac{Ct(1+t)}{d(t,A)},-\frac{C(1+t)}{d(t,A)}\right):t>0,t\notin A\right\}
\cup\{(0,-C/\min A)\}.
\tag{O8}
\]

这是闭图；在共同小输入域，\(\lambda\in A\) 时额外分支输入模至少 \(C\)，完整 resolvent 是 \(x/(1+\lambda)\)，且有严格 LT/direct/energy 接口。\(\mu\notin A\) 时取 \(t=\mu\) 使输入零出现额外输出，完整单值良定失败。乘自由切向维可得非点解集。

因此局部完整良定谱可为无理单点或 Cantor 集；不声称其全域全输入谱相同，也不把所有多值全选择谱混为一谈。**类型：严格 no-go；实步长紧参数闭块已能绕过错误有理化，类别投影仍未决。**

### O9｜局部观测与完整 \(F\)：真实残差和紧性都可丢失

第一种丢失：在 \(U=\mathbb R\times(-1,1)\)、\(\lambda=1\) 上，令

\[
F_0(p,r)=\{(0,-19r/9)\},\qquad
\operatorname{gph}F_1=\operatorname{gph}F_0\cup\{((0,4/5),(0,3/10))\}.
\tag{O9a}
\]

新增输入为 \((0,11/10)\notin U\)，所以两者局部完整 resolvent 都是 \(T(p,r)=(p,-9r/10)\)，全部局部轨道相同；但在实际输出 \(u_0=(0,4/5)\)，真实残差分别为 (76/45) 和 (3/10)。

第二种丢失直接限制定理 P 的外推：

\[
T_N(s,r)=\bigl(s,-\min\{1,N(r-2)_+\}\bigr),\qquad K=[-1,1]^2.
\tag{O9b}
\]

全体在 \(K\) 上同为投影、全域两步终止、固定相同 \(S=\mathbb R\times\{0\}\)；故局部 \(\Phi_K\) 完全相同。但 \(T_N(0,2)=(0,0)\)、\(T_N(0,2+1/N)=(0,-1)\)，没有局部一致收敛子列；完整图极限在该输入出现多输出。局部 \(\Phi_K\) 的全图纤维不紧。

可用修复是保留全图，或在全紧耗尽记录尾／模并另证相容性。双 collar 只保证

\[
V\Subset U,\ \delta=d(V,E\setminus U)>0,\quad
u\in V,\ \|v\|<\delta/\lambda\Longrightarrow u+\lambda v\in U.
\tag{O9c}
\]

**类型：严格信息 no-go；全图内生表示和宏观粘合仍是构建瓶颈。**

### O10｜残差耦合：粗化不能只改正则性

对 \(0<\gamma<1,L>0\)，strict direct 或普通 energy 兼容要求小尺度

\[
r_F(u)\ge c\,d(u,S)^\gamma.
\tag{O10a}
\]

若保留一列 \(u_j\to S\)、\(d(u_j,S)>0\)、\(r_F(u_j)\le C d(u_j,S)\)，即与之冲突。线性法向压缩 \(T(y,z)=(y,qz)\) 的真实残差正是线性阶，所以“只插尖点、保原残差阶”可能同时离开 LT 和 RLEB。

双侧保真的共轭还满足

\[
\frac{\|T^h(hx)-hx\|}{d(hx,S)}
\le\frac ba\frac{\|Tx-x\|}{d(x,S)}
\tag{O10b}
\]

只要 transition 长度至多乘 \(b\)、距离至少乘 (a>0)。故原线性位移比有界时，此路线不能使其无界。固定证书块也不凸：\(T_\pm(p,r)=(p\pm\sqrt{|r|},|r|/4)\)、\(\psi(t)=t^2/4\) 在小尺度可有共同严格证书，但平均映射保该 gauge 要求 \(r/4\le(3r/4)^2/4\)，近零失败。这里只否定固定证书凸性，不否定平均映射可能有其他 energy 证书。

**类型：真结构不相容；应研究联合模—残差几何，而非仅正则指数。**

### O11｜层位置：仿射漂移定理是工具，不是总体判决

取 \(E=\mathbb R^m\times\mathbb R^n\)、\(S=\mathbb R^m\times\{0\}\)。当前工具在 \(c>0\)、\(0<q<1\) 及

\[
T(y,z)=(y+A(y,z),B(y,z)),\quad
\|A(y,z)\|\ge c\|z\|,\quad\|B(y,z)\|\le q\|z\|,
\tag{O11a}
\]

及共同局部导数预算下，用法向幂共轭 \(h(y,z)=(y,\|z\|^{p-1}z)\)、\(p=1/\gamma>1\)，得到

\[
\|T'x-x\|\ge c\,d(x,S)^\gamma,\qquad
d(T'x,S)\le q^p d(x,S),\qquad
d(u,S)\le\left(\frac{\lambda q}{c}r_{F'}(u)\right)^p.
\tag{O11b}
\]

在原定理导数假设下，若 \(qMC_\gamma/c<1\)，有小域 strict RLEB，并利用已证 LT 必要线性位移界排除同一算子任意正步长 all-pairs LT。

缺口仍是同尾、固定宏观域和母空间位置。源层的加权 \(C^1\) 内部不等于 AW／全时间母空间内部；变形像甚至不必留在光滑源层。若 \(A\) 在 \(z=0\) 可微，则 \(|D_zA(y,0)z\|\ge c\|z\|\)，强迫切向维数至少法向维数。因此它也不是所有余维的默认模型。

**类型：核心未决桥；不是已证不可能。连续嵌入和层内余稀均不足以提升。**

### O12｜无限维状态：有限维证明不能符号替换

在 \(\ell^2\) 中，闭集

\[
C=\{(1+1/n)e_n:n\ge1\}
\tag{O12a}
\]

到零距离为一而不取得；\(C_A=\{0\}\cup\{e_n:n\in A\}\) 给 AW 有界距离函数中的不可数分离族。连续映射也未必有界集上一致连续：取局部分离 bump 使 \(f(e_n)=0,f(e_n+\delta_ne_1)=1\)，令 \(T(x)=x+f(x)e_1\)、\(T_n=T+\delta_ne_1\)，则

\[
T_n\to T\text{ 一致},\quad T^2(e_n)=e_n,\quad
T_n^2(e_n)=e_n+(1+2\delta_n)e_1.
\tag{O12b}
\]

复合在有界一致拓扑不连续。**类型：无条件 Hilbert 推广的真反例；须另建统一连续／弱紧等结构。它不妨碍有限维状态、无限维算子空间的主研究。**

### 6.1 最小公式索引

| 要复核的推断 | 最短见证 | 原始详细证明 |
|---|---|---|
| 存在选择／固定步长不能代全选择／变步策略 | O1a–O1b | `03` §3 |
| 最大 AW 空间失去鉴别力 | O2 | `03` §4 |
| 单步与全轨道拓扑不同 | O3a–O3b | `03` §5 |
| RLEB 可自第一纲 | O4a–O4b | `03` §6 |
| \(K_\sigma\)–Baire 诊断；投影不保纲 | O5、(5.13) | `06` §§1.6、6.1；`03` §7 |
| lu 层可空但 pt 非空 | O6 | `03` §8 |
| 精确尾与 slack 不能混用 | O7a–O7b | `03` §9；`01` §6.3 |
| 步长谱不必开或含有理点 | O8 | `03` §10 |
| 局部动力不决定 EB；局部观测不 proper | O9a–O9c | `03` §11；`06` §2 |
| RL–EB 兼容与保真共轭相冲突 | O10a–O10b | `03` §12 |
| 漂移层范围、维数与代表性 | O11a–O11b | `01` §7；`04` §0 |
| Hilbert 的紧性／复合问题 | O12a–O12b | `03` §14 |
| 塔单点不等于同尾层刚性 | (7.4) 以下投影例 | `06` §4 |

## 7. 七条可交给团队的建设性 idea 与验收线

以下是候选路线，不是七条已完成的主定理。顺序按对理想目标的承重程度排列。

### Idea 1｜从已证 proper 观测走向类别分解

从定理 P 出发，判定 \(\Phi:X\to Z\) 是否 category-preserving，或在哪些**中立定义**区域上具有该性质。可检验目标是：每个非空开 \(O\subset X\)，\(\Phi(O)\) 在实际像 \(Z\) 中非第一纲；开放满射是更强充分条件。

现成工具为 Melleray–Tsankov Appendix A 的 Proposition A.3、Theorem A.5：在恰当 Polish 与 Baire-property 假设下，连续 category-preserving 映射可用纤维版 Kuratowski–Ulam，把母空间余稀与余稀基点上的纤维余稀联系起来。

**验收：**证明具体观测的保纲或给开区域落入基底薄片的反例；同时交代加入完整域外图后哪些结论仍成立。只重复 proper／Polish／紧纤维不算新增完成。

### Idea 2｜先找内生 Baire 核心，不先证明 LT 小

用 (O5) 对对象侧 \(K_\sigma\) 认证像作局部紧诊断。关键对象问题是：是否存在原相对拓扑开邻域 \(O\) 与一个紧预算块 \(K_j\)，使

\[
\mathcal R\cap O\subseteq K_j?
\tag{7.1}
\]

这是认证预算是否局部有界，不是给每个对象附标签。可用 Choquet 方法研究原拓扑的完全可度量性，但不能借附证书强拓扑替换原对象。

**验收：**得到非退化 Baire 核心及其母空间位置，或证明相对类自第一纲并明确停止空洞排序。发现某个方便预算块紧本身不够。

### Idea 3｜内生 Lyapunov 塔、轨道后继与全纤维选择

在完整紧源图卡中，设 \(T\in C(K,K)\)、\(\operatorname{Fix}T=S\)。若 \(T\) 有一致有限长度尾，定义

\[
V_j^T(x)=\sum_{k\ge j}\|T^{k+1}x-T^kx\|,\qquad
L_j(T)=\sup_KV_j^T\to0.
\tag{7.2}
\]

已独立核准：若连续 \(U:K\to K\) 满足所有 \(j\ge0\)

\[
\|Ux-x\|+V_0^T(Ux)\le V_0^T(x),\qquad
V_j^T(Ux)\le V_{j+1}^T(x),
\tag{7.3}
\]

则 \(\operatorname{Fix}U=S\)，且 \(\sum_{k\ge n}\|U^{k+1}x-U^kx\|\le V_n^T(x)\)。再取连续非降 \(\psi\)、\(\psi(0)=0\)，对每个输入要求

\[
d(Ux,S)\le\psi(\|x-Ux\|/\lambda)
\tag{7.4}
\]

并在完整输出纤维取 inf，即得真实 EB。只有 Cauchy 尾时，连续选择 \(Ux\in\overline{\{T^mx:m\ge1\}}\) 也保持原 Cauchy 尾；丰富选择存在性并未证明。

**关键更正：充分可行对应 \(Q_{T,\psi}\) 单点，只证明这一工具刚性，不证明同尾层刚性。** 对 \(P(s,r)=(s,0)\)，(7.3) 强迫 \(U=P\)；但

\[
U_a(s,r)=\bigl(s+a r(1-r)(1-s^2),0\bigr),\quad0<a\le1
\tag{7.5}
\]

仍一步终止，\(w(P)=w(U_a)=(1,0,0,\ldots)\)，最小一致长度尾也相同，却不满足投影的逐点塔约束。若想从工具刚性推出层刚性，必须另证必要性或给独立反定理。

**验收：**非空、丰富连续／Hölder 选择＋同域真 EB＋统一 strict RL 兼容＋母空间非第一纲覆盖。不能直接套 Michael 选择定理：可行值通常非凸，且未证下半连续。

### Idea 4｜统一紧块中的有限相容性／逆极限

将同尾、边界匹配、完整覆盖、全图 EB、all-pairs RL、exact-\(S\) 及带余量 LT 越界写为同一紧对象块 \(\mathcal K\) 中的闭约束 \(C_i\)。目标是

\[
\bigcap_{i\le N}C_i\ne\varnothing\quad(\forall N),
\tag{7.6}
\]

且所有有限层共用同一个模、同一个 strict compatibility 余量、同一宏观域。紧性交定理随后给完整对象；真正新工作是受约束 extension／amalgamation 引理。

**验收：**对任一对象邻域和有界 LT 必要块都能完成，或定位一个有限子系统的矛盾。\(L_N\to\infty\)、\(\gamma_N\downarrow0\)、\(\kappa_N\uparrow1\) 或遗漏域外纤维，都不是有效紧性论证。有限约束矛盾最初只否定这个构建系统；升级为母空间刚性还需必要性。

### Idea 5｜联合反射模—真残差剖面及几何秩分层

研究 (5.8) 与完整反射模，而非只谈“允许 Hölder”。在具有双侧幂阶的可实现层中，若

\[
M_F(t)\asymp t^\gamma,\qquad b_{F,V}(r)\asymp r^p,
\tag{7.7}
\]

direct 小尺度兼容要求 \(\gamma p\ge1\)：严格大于一可争取缩域余量，等于一必须检查常数，小于一不可兼容。没有双侧增长时不能把上界指数当必要条件；慢变因子和振荡 gauge 须保留。

可沿 \(C^1\) 解流形研究法向／切向共同承担残差的秩条件，突破 O11 中切向单独承担所需的维数限制。

**验收：**对象侧可测／半连续表示、合法 gauge 重构、剖面可实现性，以及剖面区域原像的母空间位置。只有一张 \(\gamma,p\) 图不算总体比较。

### Idea 6｜受控原图箭头与跨尾尺度

完整图共轭 \(G^h=L_\lambda^{-1}(h\times h)L_\lambda G\) 保算法身份。应研究这些受控部分箭头的局部满性／保纲性，而非只再选一个 \(h\)。

已独立核准的 no-go：紧度量 \(K\) 上满射、1-Lipschitz 的 \(h:K\to K\) 必等距。因此用“全局不扩张满射共轭”无损保尾，不能制造想要的粗糙化。可尝试仅对同一轨道尾点对限制

\[
\|h(T^mx)-h(T^nx)\|\le e_n,
\tag{7.8}
\]

并另证全部 transition 的真实 EB。若只能 \(e\mapsto ce\)，必须给层间类别定理。

**验收：**有覆盖位置的受控箭头体系和保纲结论，或精确说明哪些尾饱和／残差约束迫使刚性。单向 Lipschitz 控制一般不对取逆封闭，不能无证称为一个作用群。

### Idea 7｜原算子的步长谱及可解释的细分类

对相同原 \(F\) 和固定宏观／germ 口径定义 \(\Sigma_C(F)\)。区分

\[
\begin{aligned}
G_{\rm step}&=\{F:\Sigma_{\mathcal R}(F)\setminus\Sigma_{\mathcal L}(F)\ne\varnothing\},\\
G_{\rm object}&=\{F:\Sigma_{\mathcal R}(F)\ne\varnothing,\ \Sigma_{\mathcal L}(F)=\varnothing\},\\
G_{\rm window}&=\{F:\operatorname{Int}(\Sigma_{\mathcal R}(F)\setminus\Sigma_{\mathcal L}(F))\ne\varnothing\}.
\end{aligned}
\tag{7.9}
\]

以紧步长—闭预算块定义紧集值 \(\Sigma_{C,j}(F)\)，先研究 hyperspace 上半／下半连续、no-escape 和对象投影的类别。共同第一纲后，可另做认证谓词的尖锐 Borel 复杂度或固定度量下相对孔隙；二者分别衡量判定难度或定量逃逸，不冒充原来的总体占比。

**验收：**新增原算子、额外步长、稳健窗口明确分开；不存在有理化偷换。若做孔隙，必须在每个半径 \(r\) 邻域有同域同尾越界对象，且越界余量 \(a\ge cr\)；一个稠密越界点不够。

## 8. OP1–OP10：可分配、可证明或反证的正式任务

| 编号 | 要交付的明确问题 | 完成标准与边界 |
|---|---|---|
| **OP1** | 冻结 Q-AW／Q-DYN 主分母及内生观测结构 | 非空、拓扑科学含义、原对象量词清楚；定理 P 是已有起点，不重复当未知 |
| **OP2** | RLEB 对象并类的 Baire／局部紧核心 | 应用 O5，判定是否自第一纲、是否有中立非第一纲区域；正反结果均有效 |
| **OP3** | 中立收敛空间中的绝对类别 | 同时报 \(\mathcal R,\mathcal L,\mathcal R\setminus\mathcal L\) 的闭包、内部、纲；不预设必须 LT 小 |
| **OP4** | 同域、同尾、全纤维对象修改或刚性 | 对每个对象邻域、每个有界 LT 必要闭块，保同一分母和 strict RLEB 后越界；或给该命题的反定理 |
| **OP5** | 从纤维／结构层到母空间的桥 | 判定 \(\Phi\) 保纲；全图提升；或结构层的真实位置。无限维／闭凸／层内余稀不是替代品 |
| **OP6** | 跨尾尺度的类别／厚度转移 | 研究后段 slack、时间平移和 \(e\mapsto ce\)；规避 O7 的初段硬下界，不能只给集合包含 |
| **OP7** | 固定宏观全图的内生证书表示 | 联合 \(M_F,b_{F,V},w\) 的可描述性、gauge 重构和完整纤维粘合；不混 tight-source 与 germ |
| **OP8** | 存在实步长的原算子比较与谱结构 | 判定 \(G_{\rm object}\) 等的对象类别、no-escape 条件和窗口；变步长另需共同 Lyapunov |
| **OP9** | 解几何、多值与 Hilbert 的扩展边界 | 仿射／\(C^1\)／一般闭集与全选择分开；无限维另建紧性与复合连续条件，后置 |
| **OP10** | 确定主定理后的优先权审计 | 原始论文、版本、定理号、假设对应、已覆盖与未覆盖；搜索未见不算首创证明 |

OP4 的一个具体落点是：在已证非退化的中立层 \(Y\subseteq\mathfrak D_e\) 中，研究 LT 必要闭块

\[
C_{M,j}(s)=\{T:\|Tx-x\|\le M d(x,S)
\quad\forall x\in K\cap\overline B_{1/j}(s)\}.
\tag{8.1}
\]

在适用的仿射／\(C^1\) 解几何及距离非增接口下，所有正步长 LT 落入这些必要块的可数并。真正困难是对任意对象邻域的同层修改，最后的 Baire 步骤并不难。塔或后继集只是可能的充分构建工具，不是 (8.1) 修改命题的必要参数化。

**建议首攻顺序：**OP1、OP2、OP5 并行冻结主干；OP7 提供真残差坐标；随后 OP3 与 OP4／OP6 相互反馈；OP8 从一开始保留量词，但不抢占全部构建资源；OP9 后置；OP10 随确立的主张逐项同步，不用文献状态替代数学正确性。

## 9. 团队分工与“90 天”阶段节奏

这里的 90 天仅是可压缩、可延长的研究组织模板，**不是证明完成期限或成功承诺**。每阶段允许产出反定理、精确未决命题或止损结论。

| 团队 | 主责 | 必交材料 |
|---|---|---|
| 泛函分析／描述集合 | OP1、OP2、OP5；局部紧、Baire、类别保持 | 一份主分母定义；一条类别桥或严格阻断；状态表 |
| 动力系统／拓扑 | OP3、OP6；尾、极限纤维、orbit funnels | 同层／跨层结构定理，明确实际尾与长度尾 |
| 变分分析／PPA | OP4、OP7；完整纤维、RL–EB 兼容 | 带全部常数、域和图点量词的闭合或刚性引理 |
| 构造／延拓 | Idea 3–4，与前两组配合 | 有统一余量的有限相容性／选择定理，或最小不相容子系统 |
| 谱与策略 | OP8 | 固定／存在／全策略分别编码；谱的对象级比较 |
| 独立审计／文献 | 横向复核、OP10 | 不沿用“PASS”标签代证明；每条新增定理重证和文献对应 |

| 阶段 | 参考窗口 | 阶段验收，不是时间承诺 |
|---|---|---|
| A：冻结语义 | 第 1–15 天 | 决定 Q-AW／Q-DYN 主口径；保留另一路的解释；复核定理 P 与 O4/O9；写明主空间和 LT 版本 |
| B：先判分辨率 | 第 16–35 天 | OP2 局部紧诊断；\(\Phi\) 类别保持的首个结果；全图观测候选；可证明两类皆小而转向 |
| C：攻一条承重桥 | 第 36–60 天 | 选类别纤维化、联合残差表示、同层选择或有限相容性中的一条主攻；仿射工具必须配位置任务 |
| D：形成主定理或反定理 | 第 61–75 天 | 明确总体／全分层结论的范围；如只得结构层结论，标题与摘要据实限缩 |
| E：外部复核与定位 | 第 76–90 天 | 独立证明、最小反例、版本追踪、定理级优先权；提交可发表结果与仍未解决清单 |

停止／转向线：

1. 若两类在指定中立层共同第一纲且 RLEB 又自第一纲，停止把相对第一纲作为强弱分数，转做有依据的全剖面／定量结构。
2. 若某塔对应单点，只停止该充分工具，不宣布同尾层不可能；需另证必要性。
3. 若仿射漂移层的位置持续未定，它仍可保留为工具，但不计作总体分类完成。
4. 若找到具体中立非第一纲区域、类别桥、同域全纤维闭合三者的组合，才进入理想差距主定理阶段。

## 10. 文献边界：已有语言与尚缺桥梁

下表根据 `05_priorart_boundary.md` 的原文核对记录及 `04` 的类别分解工具组织。不是穷尽性优先权判决。

| 原始文献与已核位置 | 已覆盖 | 本项目仍须补什么 |
|---|---|---|
| I. A. Rus, *Weakly Picard mappings* (1993), Definition 2、Theorems 1–2；[原文](https://dml.cz/bitstream/handle/10338.dmlcz/118632/CommentatMathUnivCarolRetro_34-1993-4_14.pdf) | 全初值迭代趋向可依赖初值的不动点；WPO 语言 | 保原欧氏几何的 PPA 图证书与类别比较；不靠重选状态度量 |
| I. A. Rus, A. Petruşel, M. A. Şerban, *Weakly Picard operators: equivalent definitions, applications and open problems* (2006), Definition 1.6、Theorems 6.2、8.1；[原文](https://www.math.ubbcluj.ro/~nodeacj/download.php?f=061rus.pdf) | 有限长度、极限纤维及定量 WPO | 非 Fejér 完整原图的内生表示和认证像比较 |
| D. Butnariu, S. Reich, A. J. Zaslavski, *Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces* (2001), Assumption A、Theorems 2.1、3.1–3.2；[DOI 10.1515/JAA.2001.151](https://doi.org/10.1515/JAA.2001.151) | 固定非点目标集、完备算子空间、泛型回缩、投影混合 | 母类预装共同 Bregman 下降；一般非 Fejér RLEB 不自动进入 |
| X. Wang, *Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent* (2013), Propositions 2.1、2.3–2.4、Theorems 2.13–2.16；[DOI 10.1016/j.na.2013.03.008](https://doi.org/10.1016/j.na.2013.03.008) | 极大单调／FNE／非扩张空间和泛型结构 | 固定非点 \(S\) 后严格压缩稠密机制不能照搬；第一纲不是低价值 |
| H. H. Bauschke, J. Schaad, X. Wang, *On Douglas–Rachford operators that fail to be proximal mappings* (2018), Proposition 2.8、Theorem 3.1；[DOI 10.1007/s10107-016-1076-5](https://doi.org/10.1007/s10107-016-1076-5) | 同一结构空间内真正的闭无处稠密子类比较 | 对象是有限维线性关系对，不是一般 RLEB–LT |
| S. V. Tikhonov, *Complete metric on mixing actions of general groups* (2013), Lemmas 1–2、Theorem 1；[DOI 10.1007/s10883-013-9162-y](https://doi.org/10.1007/s10883-013-9162-y) | 长期行为母类与全时间型 Polish 拓扑 | 非 PPA 点轨道；不保证 AW 与动态拓扑保同一纲 |
| L. Leuştean, A. Nicolae, A. Sipoş, *An abstract proximal point algorithm* (2018), Definition 3.6、Theorems 3.13、3.15、5.1；[DOI 10.1007/s10898-018-0655-9](https://doi.org/10.1007/s10898-018-0655-9) | joint FNE／P2、相容 resolvent family 与抽象 PPA | 非单调完整关系、局部域和类大小不能直接得到 |
| A. Sipoş, *Revisiting jointly firmly nonexpansive families of mappings* (2022), arXiv v3 Theorems 3.3、5.3；[DOI 10.1080/02331934.2021.1915312](https://doi.org/10.1080/02331934.2021.1915312) | 非扩张加 resolvent identity 的等价表征 | 参数趋无穷的极限不是固定步长反复迭代极限 |
| U. Kohlenbach, G. López-Acedo, A. Nicolae, *Moduli of regularity and rates of convergence for Fejér monotone sequences* (2019), Definition 3.1、Theorem 4.1、Proposition 4.4；[DOI 10.1007/s11856-019-1870-x](https://doi.org/10.1007/s11856-019-1870-x) | Fejér、真实残差、共同模与部分反向表征 | 非 Fejér RLEB 的双向表示及保纲不是现成结果 |
| J. Melleray, T. Tsankov, *Generic representations of abelian groups and extreme amenability*, Appendix A Proposition A.3、Theorem A.5；[作者稿](https://math.univ-lyon1.fr/~melleray/ext-amenability.pdf) | category-preserving 判据与纤维版 Kuratowski–Ulam | 要证明本项目具体 \(\Phi\) 符合假设；标准转移工具本身不算创新 |
| D. Ravasini, *Generic uniformly continuous mappings on unbounded hyperbolic spaces* (2024), Lemma 3.2、Theorems 3.3、4.1、5.2；[DOI 10.1016/j.jmaa.2024.128440](https://doi.org/10.1016/j.jmaa.2024.128440) | 固定凹模的泛型模饱和与局部替换 | 不保 exact-\(S\)、同尾、真实 EB；见证点对可逃向无穷 |
| D. Ravasini, D. K. Thimm, *Generic nonexpansive Hilbert space mappings* (2025), Theorems 4.1、4.2、5.3；[DOI 10.4064/sm240722-12-3](https://doi.org/10.4064/sm240722-12-3) | 逐点拓扑和域几何影响泛型固定点行为 | 不可和有界集一致拓扑的泛型结论混用 |
| D. R. Luke, M. K. Tam, *Generalized Monotonicity and the Proximal Point Algorithm* (2025 online), Definition 2、Propositions 3–4、Lemma 1、Assumption 2、Theorem 2；[DOI 10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863) | submonotonicity／resolvent 几何与局部线性 PPA | 不是算子空间 Baire 比较论文；完整域接口仍需对齐 |
| D. R. Luke, N. H. Thao, M. K. Tam, *Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings* (2018), arXiv v2 Definition 2.3、Theorem 2.18、Corollary 2.19；[DOI 10.1287/moor.2017.0898](https://doi.org/10.1287/moor.2017.0898) | pointwise almost-averaged、gauge subregularity、多值迭代 | 与 LT 2025 all-pairs 单值接口不同，不能整体用同一包含号排除 |

仍须专门查原文链：Reich–Zaslavski 1999 *Convergence of generic infinite products of nonexpansive and uniformly continuous operators*（[DOI](https://doi.org/10.1016/S0362-546X(98)00080-7)）、其 *Genericity in Nonlinear Analysis*（2014，[DOI](https://doi.org/10.1007/978-1-4614-9533-8)）相关章节、Strobin 2012 *Some porous and meagre sets of continuous mappings*、WPO 算子空间后续、局部 resolvent 谱和类别保持的精确先例。目前未全文核定的地方不补造定理号。

本项目可能有实质新内容的部位是：**完整非单调原图的内生证书表示；同尾同域全纤维闭合；中立分层的 RLEB–LT 覆盖及合法提升；局部步长谱的实现／限制。** 定理 P、谱实现与结构变形的精确优先权仍需单独清关。既不能因外层语言已有就否定组合结果，也不能因暂未检索到就宣布首创。

## 11. 文件索引与外部复核顺序

### 11.1 本次交接包

| 文件 | 定位 |
|---|---|
| `README.md` | 阅读入口和版本优先级 |
| `07_final_handoff.md` | 本综合主稿；可直接交给数学家团队 |
| `06_math_audit.md` | 本轮承重命题独立复核；定理 P、全图边界、塔刚性修正、种子证明 |
| `02_ideal_problem_formulation.md` | 中立 atlas、全剖面、原对象步长覆盖；已同步定理 P 的加强 |
| `03_obstruction_taxonomy.md` | O1–O12 的详细反例与 no-go |
| `04_research_ideas.md` | 建设路线的完整推导；已修订塔单点和局部观测边界 |
| `05_priorart_boundary.md` | 原始论文、定理级覆盖与尚未清关文献链 |
| `01_full_handoff_draft.md` | 历史集成底稿和详细基础证明索引；状态冲突时以后续审计与本主稿为准 |

### 11.2 既有证明资产

以下位于同一工作区，不表示新增证明：

| 路径 | 需要时查什么 |
|---|---|
| `ppa_system_team/10_final_blueprint.md` | P0–P10、五层体系、基础定理总表 |
| `ppa_system_team/01_ambient_axioms.md` | 完整本体、良定 atlas、原图 \(G_\delta\) |
| `ppa_system_team/02_convergence_topology.md` | pt／lu、全时间、同尾拓扑桥 |
| `ppa_system_team/03_certificate_embeddings.md` | direct／energy、LT 转换、规范 gauge |
| `ppa_system_team/06_resolvent_family.md` | 跨步长完整关系、轨道与策略量词 |
| `ppa_system_team/07_embedding_math_audit.md` | 证书转换独立审计 |
| `ppa_system_team/08_architecture_audit.md` | 基础空间终审和最大 AW 退化 |
| `ppa_classification_team/01_frozen_denominator.md` | 固定宏观规格、全部原纤维、共同留域／尾 |
| `ppa_classification_team/02_structural_deformation.md` | 完整共轭、非退化漂移及准确停止点 |
| `ppa_classification_team/03_object_category.md` | \(K_\sigma\)、LT 必要块、对象修改目标 |
| `ppa_classification_team/04_step_spectrum.md` | 任意紧局部谱与实步长闭块编码 |
| `ppa_classification_team/05_obstruction_audit.md` | 同尾、自第一纲、谱、collar 的交叉复核 |
| `ppa_classification_team/06_priorart_tools.md` | 延拓／共轭工具及不保量 |
| `ppa_classification_team/07_stage_synthesis.md` | 上一阶段终判；仿射优先建议现已降为工具路线 |
| `comparison_space_team/09_final_synthesis.md` | 历史超吸引层 \(\mathcal Y\)；仅测试案例，不代表总体 |

建议外部团队首轮独立重证：定理 P、O4 自第一纲、O8 完整局部谱、O9 的双重信息缺口，以及 (7.3)–(7.5) 的充分／必要边界。它们决定主问题应怎样继续，而不是先重审全部历史材料。

## 12. 最终交接判断

现在值得交给数学家团队的是**空间结构与类别转移的问题**，不是请他们替旧例子再调参数。仿射漂移是可用局部工具；是否能帮助理想比较，要看它能否参与 OP5 的代表性桥，不能由其层内定理漂亮与否决定。

本轮已经补上一块真正的体系底座：紧 T-only 图卡中的内生观测具有 proper Polish 基底和紧纤维。尚未补上的是：**该分解是否保纲、怎样保留全部原图、各认证类在中立空间中是否有可辨认的厚度，以及同尾同域全纤维的构建自由度。**

没有证明理想方向不可能；也没有完成理想比较。接受一条证明某种纲排序必然退化的反定理，和接受一条真正的新增覆盖定理，同样忠于研究目标。研究应由这些可检验问题推进，不再用更多受限层构造替代总体结论。
