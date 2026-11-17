# 三目标整合审查：C309 / C311 / C310 与 PTD、TC

日期：2026-11-17  
身份：`integration review`，只整理跨目标接口与边界；不修改 canonical claims，不新增 Claim，不改变已有状态。

本审查逐项读取：

- `research/canonical/ppa_nonlinear_gauge_and_coupled_obstruction.md`；
- `research/topics/next_stage_2026/README.md`；
- `research/topics/next_stage_2026/target1_nonlinear_contraction.md`；
- `research/topics/next_stage_2026/target2_kl_finite_length.md`；
- `research/topics/next_stage_2026/target3_coupled_structure.md`；
- `research/notes/target1_state.md`、`target2_kl.md`、`target3_coupling.md`；
- `CLAIMS.md` 中 C309、C310、C311 的精确身份。

## 总裁决

1. **目标一与目标二可以在同一条轨道上并列使用，但没有单向逻辑桥。** C309 的距离函数迭代和加权步长尾只提供几何/物理长度证书；C311 的 KL 递推需要下降能量、相对误差、H3、KL 点和 LMZ 的耦合门。尾和不能代替 KL 的能量差，KL 也不能凭自身产生 C309 所需的预指定集合 (S) 的 (Phi)-递推。
2. **PTD 可以条件地接入 C309/T1.1。** 对每个允许转移都有 PTD 时，取
   (Phi_d(t)=kappa t)、(B_d(t)=C t^\alpha)，即可得到 C309 的有限尾；直接的 PTD 望远镜估计更强。这个桥只在允许关系非空、后继 coverage、工作域和闭性另行成立时有效。PTD 当前仍是 candidate，不是 canonical 定理。
3. **​(mathcal P_{\rm TC}) 也可以条件地接入 C309/T1.1。** TC1--TC3 给出
   (kappa_{\rm TC}=\sqrt{1-2\mu}<1)，以及例如
   (B_d(t)=\lambda c\kappa_{\rm TC}t)，从而得到几何尾。TC 本身没有证明 coverage，也没有证明它由“传统次单调性 + MSR”推出；C310 恰好否定后一个蕴含。
4. **完整图和允许子关系必须始终分开。** 若 (A) 对完整 (operatorname{gph}F) 的每个图值成立，T3.1 已推出线性 MSR；只有在严格允许子关系上量化，才可以同时出现允许轨道的 (A)+(B)/PTD 与完整 (F) 的 MSR 失败。
5. **没有发现 canonical ID 的数学重复，但有若干符号和状态的表面冲突。** 需要把距离映射、KL 下降模、长度包络和输出常数改用不重复的记号；PTD、TC、T1.1、T3.1 都是局部报告对象，不能被误写成新的 C309/C310/C311 版本。

## 1. 共同对象的最小对齐

为了同时讨论三条线，先固定同一有限维对象

\[
X=\mathbb R^n,\qquad S\subset X\text{ 非空闭},\qquad d(z)=d(z,S),
\]
固定步长 (lambda>0)，以及允许后继关系

\[
\varnothing\ne\mathcal T(x)\subset J_{\lambda F}(x).
\]

若接入 C311，还必须进一步固定

\[
F=\partial f,
\qquad
\mathcal T(x)\subset P_\lambda(x):=
\operatorname*{argmin}_y\left\{f(y)+\frac1{2\lambda}\|y-x\|^2\right\},
\]
或者明确只选取一条满足全局近端最小性的策略。一般 resolvent 根
(x-y\in\lambda\partial f(y)) 并不自动是 global argmin；没有 global comparison 就不能取得 C311 的充分下降。

对一条选定轨道记

\[
d_k=d(x^k),\qquad s_k=\|x^{k+1}-x^k\|.
\]

C311 的 exact PPA 情形可令其 surrogate (e_k=s_k)，但在 LMZ 抽象框架里 (e_k) 是额外序列，不能在一般算法中无声明地与 C309 的物理步长等同。

若使用 C311 的 stationary 集记号 (Gamma=\{x:0\in\partial f(x)\}\)、(Xi\subset\Gamma)，则还必须声明 (S) 与它们的关系。C311 只保证 KL 极限是某个 stationary point；它不自动保证该点属于 C309 预先固定的 (S)。最安全的共同选择是 (S=\Xi)（并证明闭性），或另行证明 KL 极限属于 (S)。

## 2. C309/T1.1 与 C311 KL 递推：可并列，不能互相替代

### 2.1 C309 的尾和没有 KL 能量信息

C309/T1.1 使用的是

\[
d_{k+1}\le \Phi_d(d_k),\qquad s_k\le B_d(d_k),
\]
以及

\[
\Theta_{\Phi_d}(t)=\sum_{j\ge0}B_d(\Phi_d^{\circ j}(t))<\infty.
\]

这给出距离趋零、有限长度、工作域留存和尾界。它不产生：

- 一个能量 (E) 或目标函数 (f)；
- 近端下降 (f_{k+1}+a\phi_E(s_k)\le f_k)；
- KL 斜率不等式；
- 相对误差选择 (w_{k+1}\in\partial f(x^{k+1}))；
- LMZ 的 (phi_E^{-1}(\beta_R(s)t)) 耦合门。

因此不能把 (B_d(\Phi_d^k(d_0))) 直接代入 C311 的
(Lambda_{k,k+1}) 递推，也不能说 “(Theta_{\Phi_d}<\infty) 已经证明了 KL 递推”。即使 C309 已经给出有限长度，C311 仍是另一条能量/局部率证明；在这种情况下 KL 递推通常是补充证书，而不是长度证明所必需的环节。

### 2.2 C311 也不能单独产生 C309 的距离接口

C311 的条件版 exact subgradient PPA 结论是：在有界次水平集、聚点、H3、KL 和 (K1) 下，

\[
\sum_k s_k<\infty,
\qquad x^k\to\bar x.
\]

它不自动给

\[
d(x^{k+1},S)\le \Phi_d(d(x^k,S)),
\]
也不自动给固定 (S) 的输出距离率、共同最近锚或工作域 coverage。C311 的 canonical scope 已明确保留“无预指定 (S) 的距离速率”这一缺口；不能用 KL 有限长度反向填入 C309 的 (NG4) 或 T1.1 前件。

### 2.3 合法的联合使用方式

若同一 exact subgradient PPA 轨道同时满足：

1. (F=\partial f)，每一步为全局精确近端选择，且所有允许选择都满足 C309 的 ((\Phi_d,B_d)) 与 coverage；
2. C309 的 (S)、(U_R)、闭性、留域预算成立；
3. C311 的有界次水平集、聚点、H3、KL 和 LMZ 耦合门成立；

则可以**并列**得到：

- C309：(d_k\le\Phi_d^{\circ k}(d_0))、(sum s_k\le\Theta_{\Phi_d}(d_0))、(x^\infty\in S)；
- C311：KL 能量尾、有限长度和 (x^k\to\bar x)。

若 C309 已证明 (x^k\to x^\infty\in S)，它可以为 C311 提供 accumulation point 以及 KL 邻域进入的辅助证据；但仍需直接核对该点的 KL、H3 与下降条件。若 C311 已证明整列收敛，则 C309 的尾界仍可作为预先长度预算；两条结论的极限必须通过 (S) 与 (\bar x) 的关系识别，不能默认是同一点。

## 3. PTD 是否能接 C309/T1.1

### 3.1 条件桥成立

目标三的 PTD 对每个允许转移给出

\[
d_y\le\kappa d_x,
\qquad
s\le C\bigl(d_x^\alpha-d_y^\alpha\bigr),
\quad 0<\alpha\le1.
\]

于是

\[
d_y\le\Phi_d(d_x),\qquad
s\le C d_x^\alpha=:B_d(d_x),
\]
其中 (Phi_d(t)=\kappa t)。在 C309 的标量接口上，

\[
\Theta_{\Phi_d}(t)
\le \sum_{j\ge0}C(\kappa^jt)^\alpha
=\frac{C}{1-\kappa^\alpha}t^\alpha<\infty,
\]

且 (Theta_{\Phi_d}(t)\to0) 当 (t\downarrow0)。因此 PTD 条件一旦对同一个允许关系、同一个工作窗和所有允许输出成立，就真正接入 C309/T1.1，并得到有限长度。

PTD 的直接望远镜估计

\[
\sum_{j=0}^{N-1}s_j
\le C(d_0^\alpha-d_N^\alpha)\le C d_0^\alpha
\]

比 C309 用 (B_d(t)=Ct^\alpha) 得出的几何尾更强；这只是两种证书的不同包装，不能将二者的常数或 sharpness 混写。

### 3.2 不能从 PTD 删除 coverage 和量词

PTD 不保证：

- (mathcal T(x)\ne\varnothing)；
- 后继仍属于 (U_R) 或下一步的评价窗；
- 允许关系真的是某个完整 (J_{\lambda F}) 的子关系；
- 目标 (S) 闭或零输入吸收（除非这些已另加）；
- 可将允许关系扩展到完整图的全部输出。

因此 PTD→C309 是“结构条件 + C309 coverage/留域前件”的条件蕴含，不是目标三原始前件的裸逻辑结论。PTD 的当前状态是 `candidate`，不能以它为依据升级 C309 或新建 canonical claim。

## 4. TC 是否能接 C309/T1.1

canonical 正文的 (mathcal P_{\rm TC}) 要求同一锚 (p\in P_S(x)\cap P_S(y))、正扇区条件和 selected-fiber calmness：

\[
\langle y-p,x-y\rangle
\ge \mu d(x)^2-\nu\|x-y\|^2,
\qquad
\left\|\frac{x-y}{\lambda}\right\|
\le c\,d(y),
\]

其中 (0<\mu<1/2)、(0\le\nu<1/2)。正文的恒等式给出

\[
(1-2\mu)d(x)^2
\ge d(y)^2+(1-2\nu)s^2.
\]

所以，对每个满足 TC1--TC3 的允许转移，

\[
d_y\le \kappa_{\rm TC}d_x,
\qquad
\kappa_{\rm TC}:=\sqrt{1-2\mu}<1,
\]

并且由 TC3

\[
s\le\lambda c\,d_y
\le \lambda c\kappa_{\rm TC}d_x.
\]

故可以取

\[
\Phi_d(t)=\kappa_{\rm TC}t,
\qquad
B_d(t)=\lambda c\kappa_{\rm TC}t,
\]

得到

\[
\Theta_{\Phi_d}(t)
\le \frac{\lambda c\kappa_{\rm TC}}{1-\kappa_{\rm TC}}t<\infty.
\]

TC4 本身还给出另一个合法线性步长包络

\[
s\le\sqrt{\frac{1-2\mu}{1-2\nu}}\,d_x,
\]

可与 TC3 的包络取较小者；这不改变接入结论。故 **TC⇒C309/T1.1 在条件上成立**。

但必须保留三道门：

1. TC1 是共同最近锚，非凸/非光滑 (S) 上不自动存在；
2. TC3 在 canonical 文字中是所选图值的 calmness，不自动对完整纤维成立；
3. TC1--TC3 不给 coverage、留域或 exact global prox 性质，这些仍需另证。

更不能把 C310 的 refuted 结论理解为 TC 被否定。C310 只否定

\[
\text{传统次单调性 + 线性 MSR}
\Longrightarrow\mathcal P\Longrightarrow(A)+(B)
\]

这一原始链；它没有否定“若另行验证 TC，则 TC⇒(A)+(B)⇒C309”。

## 5. 完整图与允许子关系：三目标共享的决定性量词门

目标三的 T3.1 给出：若 (A) 对完整图的每个 ((y,w)\in\operatorname{gph}F) 成立，且 (x=y+\lambda w)，则

\[
d(y,S)\le
\frac{\kappa\lambda}{1-\kappa}\,r_F(y).
\]

因此完整图版本的 (A) 已蕴含传统线性 MSR；不可能在同一个 full-graph 量词下再声称“严格弱于 MSR 但推出 (A)+(B)”。

允许子关系版本则不同：C309 的 \(\mathcal J\)、目标一的 (T(x))、目标三的 \(\mathcal A) 都可以只量化被选中的输出。此时 PTD/TC/A+B 可以控制允许轨道，而完整 (F) 的额外图值仍使 (r_F) 很小，完整 MSR 仍可能失败。这个版本是算法政策性质，不能升级为完整算子性质。

跨目标使用时必须逐次写出下列量词之一：

\[
\forall x\in U_R\ \forall y\in\mathcal T(x)
\quad\text{（所有允许输出）}
\]

或

\[
\forall x\in U_R\ \exists y\in\mathcal T(x)
\quad\text{（存在一个选取策略）}.
\]

C309/T1.1 的全轨道结论需要前者，除非报告明确把 (T) 定义为一条已固定的单值选择策略。C311 的 exact nonconvex PPA 通常只选取一个 global minimizer；它不能自动供应“所有 prox 输出”的 C309/PTD/TC 量词。

## 6. ID、符号与状态冲突清单

### 6.1 记号冲突（不是数学结论冲突）

| 记号 | 不同文件中的含义 | 整合时的固定写法 |
|---|---|---|
| (\varphi/\Phi) | 目标一的距离收缩映射；C311/LMZ 的下降函数 (phi) 或 (\varphi) | 用 (Phi_d) 表示距离映射，用 (phi_E) 表示能量下降模；不要把二者复合或相等化 |
| (B) | C309 的步长包络 (B_d(t))；目标三的输出相对步长常数 (B_{\rm out}) | 用 (B_d) 与 (B_{\rm out}) 分开；TC3 先给 (B_{\rm out}=\lambda c)，再编译成 (B_d(t)=B_{\rm out}\kappa t) |
| (e_k,s_k) | LMZ 的 surrogate (e_k)；实际步长 (s_k) | 仅在 exact PPA 映射中声明 (e_k=s_k)；一般 LMZ 不作该等同 |
| (S,\Gamma,\Xi,\Omega) | C309 的预指定闭零集 (S)；C311 的 stationary/KL 集 | 明确写 (S=\Xi) 或写出包含关系与极限识别，不默认相等 |
| (mathcal J,T,\mathcal A,P_\lambda) | canonical 允许关系、目标一后继关系、目标三允许转移、完整 prox 集 | 统一先定义 (mathcal T(x)\subset J_{\lambda F}(x))，再说明是否等于 global (P_\lambda(x)) |

### 6.2 ID 与版本状态

- `C309-v1` 是 canonical 的 `derived-checked` 允许转移定理。目标一报告的 `T1.1`、`T1.6` 是局部命题编号，不是新的 C-ID；报告末尾“可作为 derived-checked 候选进入接收”应理解为接收建议，不能覆盖 canonical 已有状态。T1.1 的局部陈述还以逐初值的 (mathcal L_\varphi(r)<\infty) 为主，而 canonical C309 另显式要求 (Theta_\Phi(t)\to0)；两者不要宣称逐字等价。
- `C311-v1` 是 `derived-checked`，但范围严格是 exact subgradient PPA 加列出的 KL/下降/相对误差/H3 条件。目标二报告与 canonical 一致；一般非单调 RLEB/GPPA 仍是 `open`。
- `C310-v1` 是 `refuted`，被否定的是目标三原始前件蕴含，不是所有后续候选。目标三的 `T3.1` 是 `derived-checked` 引理；PTD 是 `candidate`；canonical 的 (mathcal P_{\rm TC}) 是“修正版候选”，没有独立 C-ID。不得把 PTD/TC 的条件桥写成 C310 已证的新定理。
- 目标三报告标题中的“`candidate` / `derived-checked`”同时描述候选和已核引理；整合时以每一对象的局部状态为准，不能把整个目标三升格为 `derived-checked`。

## 7. 可共享与不可共享的 lemma

| 结果 | 可跨目标共享的内容 | 不可直接共享的内容 |
|---|---|---|
| C309/T1.1 | 在共同 (mathcal T,S,U_R) 和 coverage 下，把 PTD/TC 编译为 (Phi_d,B_d)；提供留域、尾界和预先长度预算 | 不提供 (f)、KL、H11/H2/H3、相对误差或完整图 MSR |
| C311 exact PPA | global prox 最小性给 H11；Fermat 给 selected (w_{k+1}) 和 (e_k/\lambda)；KL 递推给有限长度 | 不给 C309 的距离收缩、预指定 (S)、共同锚或所有 prox 选择量词 |
| PTD | 直接望远镜有限长度；经 (B_d(t)=Ct^\alpha) 接入 C309 | 不给 LMZ 能量下降、KL、完整图 coverage 或传统 MSR 的弱化蕴含 |
| TC1--TC3 | 通过 TC4/TC5 给 A+B，再接 C309 的几何级数 | 不由 C310 的传统 SM+MSR 自动推出；不自动对完整纤维或所有 prox 根成立 |
| T3.1 | 固定 full-graph 与 selected-subrelation 的量词分界 | 不能用于把允许子关系的结论升级为完整算子结论 |

一个合法但未被 canonical 新增的“联合命题”只能写成：

> 在同一有限维 exact subgradient PPA 轨道上，若另行验证 C309 的 (Phi_d,B_d) 接口和 C311 的 KL–PPA 全部前件，则两套结论并列成立；若 PTD 或 TC 进一步验证并编译出该接口，则可用它们作为 C309 的来源。

这是一条条件合取说明，不是 C309、C311 或 C310 的新升级。

## 8. 后续最小义务

1. 若要做真正的三目标联合定理，先固定一个 (mathcal T)：是所有 global prox 输出，还是一条选取策略；然后逐项核 coverage、工作域、零输入吸收和 (S) 的闭性。
2. 对 exact subgradient PPA，另证 (S) 与 C311 的 (Xi/\Gamma) 的关系，并分别核 KL 点和 C309 极限是否为同一点。
3. 对 PTD/TC，保留 `candidate` 状态；先构造满足完整 coverage 的原生算子/近端例，再决定是否值得申请新的 canonical Claim。
4. 任何后续正文都应避免把 (Theta_{\Phi_d})、(Lambda_{k,k+1})、KL desingularizer 或 LMZ 的 (	au) 互换；它们分别是距离/步长尾、能量差、能量函数和误差递推。

**最终整合判断：** PTD/TC→T1/C309 是条件成立的几何编译；T1/C309↔C311 只有在同一 exact subgradient PPA 轨道和两套独立前件同时成立时才能并列，不能相互推出；C310 的 full-graph 量词障碍仍然阻止把目标三包装成传统 MSR 的严格弱化。
