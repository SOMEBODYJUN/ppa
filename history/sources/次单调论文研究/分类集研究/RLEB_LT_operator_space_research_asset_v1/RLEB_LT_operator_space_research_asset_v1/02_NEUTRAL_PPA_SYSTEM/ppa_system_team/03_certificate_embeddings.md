# RLEB／Luke–Tam 作为统一 PPA 动力系统空间中的证书

日期：2026-09-20。定位：体系搭建中的嵌入与可比较性模块；不以尖点、特选 Hölder 层或有限参数族先行断言两类的纲大小。本文证明的是接口、内生结论、证书规范化及有限维标准图卡内的可测编码；**没有证明两类在最终母空间中谁为第一纲**。

复核状态：LT→energy、direct 规范化、一般 energy 逆模规范化及标准图卡内 $F_\sigma$ 编码，均已通过 07 专项独立数学审核；其文献优先权尚未审定。

已读：原 RLEB 投稿稿主文及 signed-Schur 全附录；Luke–Tam 2025 正式全文；Luke–Thao–Tam 2018《Quantitative…》arXiv v2 全文及《Implicit Error Bounds…》正式全文；comparison 01/09；solution-selection 修订稿的统一尾界与极限模接口。原稿不是本轮重新审判对象。

## 1. 结论：研究顺序应当改成“空间—动力性质—证书像—比较”

用户要求的次序在数学上合理。母对象首先是带步长／策略的完整 PPA，而不是“已满足某个 RLEB 幂次的映射”。其后才问：RLEB、LT 的证书把这个对象送进什么动力学子类。

建议把四件事分离：

1. **原算子** $F$ 与其完整图；
2. **算法实例** $(F,\lambda)$，或变步长策略族 $(F,\Sigma)$；
3. **动力学性质**：适定、所有允许轨道点收敛、共同吸引域、统一尾界、极限选择及稳定性；
4. **可验证证书**：RLEB-direct、RLEB-energy、LT-all-pairs、LTT-pointwise 等。

纲分类最后作用于第 1／2 层的无标签对象，不能在第 4 层数证书标签。一个算子有无穷多个证书，也仍只算一个算子。

本组的实质整理结果有三项：

- 给出这些证书进入同一个“统一点收敛／有限长／回缩”动力系统类的定量翻译；
- 证明 **direct-RLEB 任意单调 gauge 的规范化引理**；并在标准完整紧图卡中，证明普通连续严格增 energy gauge 的有限参数逆模规范化；
- 给出同一结论预算的无偏分层与证书像的可测编码：该固定完整图卡内 direct、energy 及其并均为 $F_\sigma$；更一般 bundle 保留有条件的 analytic 结论，不再先固定方便的 $\gamma<1$ 母层。

## 2. 裸对象与完整 proximal 接口

### 2.1 外层对象必须保留算法策略

外层可取非空闭图 $G=\operatorname{gph}F\subset E\times E$，$E=\mathbb R^n$，再标记策略、初值域和目标集。对每个 $\lambda>0$，

\[
\Gamma_{F,\lambda}
=\{(x,u): (u,(x-u)/\lambda)\in G\}
=\operatorname{gph}J_{\lambda F}.
\tag{2.1}
\]

这只是可逆线性图坐标变换，允许 resolvent 无定义、多值或不连续。不可在外层先要求所有步长均单值全域；那会把本来合法的非单调 PPA 对象删掉。

在这个外层区分以下谓词，不能相互代替：

\[
\begin{array}{ll}
\mathsf C_{\lambda}:&\text{指定 }\lambda\text{ 的每条允许轨道收敛};\\
\mathsf C_{\exists\lambda}:&\exists\lambda>0\ \mathsf C_\lambda;\\
\mathsf C_{\forall\lambda\in I}:&\forall\lambda\in I\ \mathsf C_\lambda;\\
\mathsf C_{\Sigma}:&\forall(\lambda_k)\in\Sigma,\ \text{每条该策略下的允许轨道收敛}.
\end{array}
\tag{2.2}
\]

初值、分支、步长三个量词也须写全。比如“对每个初值存在一条好分支”明显弱于“每条完整 PPA 轨道都收敛”。原 RLEB 主定理与 LT2025 主定理首先是**固定步长、局部算法接口**，不是未经加强的任意变步长定理。

### 2.2 连续单值图卡及其局限

当 $K\subset E$ 紧且 $T\in C(K,K)$，定义

\[
F_{T,K}(u)=\{(x-u)/\lambda:x\in K,\ Tx=u\}.
\tag{2.3}
\]

其图紧，且完整 $J_{\lambda F_{T,K}}(x)=\{Tx\}$ 对 $x\in K$ 成立；输入不在 $K$ 时该 resolvent 为空。于是任何连续自映射都能严格放入一个完整 PPA 图卡，而不需要 RLEB 或 LT。

但把一个既有全局 $F$ 裁成 (2.3)，通常会删掉算子图。**这不能当作原 $F$ 的不变嵌入。** 若要比较原算子而不是只比较局部算法，需保留 $F$，并核查

\[
\Gamma_{F,\lambda}\cap(K\times E)=\operatorname{gph}T.
\tag{2.4}
\]

因此有两个不同的遗忘映射：

- 遗忘证明标签，但保留 $F,\lambda,\Sigma$：统计原算子／算法实例；
- 再遗忘图卡外行为，只保留 $T|_K$：统计局部动力系统。

后者一般不单射，两个不同原算子可产生相同局部动力学。报告“覆盖多少”必须说明使用哪一个。

### 2.3 真实最小残差不是一个分支残差

全局完整单值 resolvent $T:E\to E$ 对应

\[
r_F(u)=\frac1\lambda\inf_{Tx=u}\|x-u\|.
\tag{2.5}
\]

连续 gauge 下，输出 EB 等价于在**整个逆纤维**上的不等式

\[
d(Tx,S)\le\psi(\|x-Tx\|/\lambda).
\tag{2.6}
\]

对 (2.3)，纤维全部在 $K$，所以只量化 $x\in K$ 即完整。对原全局 $F$，若只检查 $x\in K$，则还必须证明所有可能更小残差的逆像也在所检输入域；否则仅得到 transition EB，未得到原 $F$ 的真实 EB。这也是证书 bundle 不能随意丢掉 $F$ 坐标的原因。

## 3. 先定义中立动力性质，再放入证书

### 3.1 单值收敛对象的共同性质

对 $T:K\to K$，若每条迭代收敛到固定点，令

\[
\Pi_Tx=\lim_{k\to\infty}T^kx.
\]

这就是 weakly Picard 的基本对象。无需任何 RLEB／LT 定义便有

\[
\Pi_T^2=\Pi_T,\qquad T\Pi_T=\Pi_T T=\Pi_T,
\tag{3.1}
\]

以及内生不变分解

\[
K=\bigsqcup_{s\in\operatorname{Fix}T}\Pi_T^{-1}(s),\qquad
T(\Pi_T^{-1}(s))\subset\Pi_T^{-1}(s).
\tag{3.2}
\]

若收敛在 $K$ 上一致，且 $T$ 连续，则 $\Pi_T$ 连续，因而是到固定点集的连续回缩。反之，只有逐点收敛不能宣称 $\Pi_T$ 连续。

在架构组采用的

\[
d_{\rm dyn}(T,U)=\sup_{k\ge0}\|T^k-U^k\|_{\infty,K}
\tag{3.3}
\]

下，全体一致迭代收敛的连续自映射构成不预设速率的自然完备图卡，且

\[
\|\Pi_T-\Pi_U\|_\infty\le d_{\rm dyn}(T,U).
\tag{3.4}
\]

这里的“完备”是空间结构定理，不是 RL 不等式的推论；其完整证明由母空间／拓扑组提供。固定步长 RLEB 和 LT 在共同完整局部接口上给出的，是进入此图卡的充分证书。

### 3.2 同一结论／同一预算层

在 $\mathfrak A=C(K,K)$ 中预先给定非空闭 $S\subset K$，取一个趋零序列 $e_n\downarrow0$，定义

\[
\begin{split}
\mathfrak C(K,S;e)=\{T\in\mathfrak A:\;&T|_S=I,\\
&\sup_{x\in K}d(T^nx,S)\le e_n,\\
&\sup_{x\in K,\ m\ge n}\|T^mx-T^nx\|\le e_n
\quad(n\ge0)\}.
\end{split}
\tag{3.5}
\]

这是**只由可见动力学结论定义**的层，未规定 Hölder 指数、EB 次数或法向收缩律。有限次 composition 在 $C(K,K)$ 的一致拓扑连续，所以 (3.5) 是闭集，因而完备／Baire。若非空，则自动

\[
\operatorname{Fix}T=S,\qquad T^n\to\Pi_T\ \text{一致},\qquad
\|T^n-\Pi_T\|_\infty\le e_n.
\tag{3.6}
\]

证明固定点集等式：若 $Tx=x$，则 $d(x,S)\le e_n\to0$。一致 Cauchy 条件给统一极限，连续性再给固定点恒等式。

在同一层上

\[
\|\Pi_T-\Pi_U\|_\infty
\le 2e_n+\|T^n-U^n\|_\infty,
\tag{3.7}
\]

故 $T\mapsto\Pi_T$ 对单步一致拓扑连续；同层上的单步拓扑和 (3.3) 拓扑相同。这一事实使两种拓扑的比较可检验，而不是任意更换拓扑制造纲结论。

如果还要同等比较“有限长”这一输出，可附加共同可和序列 $a_n\ge0$，

\[
\|T^{n+1}x-T^nx\|\le a_n\quad(x\in K),\qquad
e_n=\sum_{j\ge n}a_j.
\tag{3.8}
\]

同样得到闭的中立结论层。不要把所有一致收敛映射都自动列入有限长层。

### 3.3 局部定理的共同吸引域必须真的推出

原 RLEB-direct 给

\[
\mathcal L(d)=\frac12\left(\frac d{1-\kappa}
+\frac{Ld^\gamma}{1-\kappa^\gamma}\right).
\tag{3.9}
\]

取 $s\in S\cap U$、$B_\rho(s)\subset U$，再取

\[
0<\varepsilon\le R,\qquad
\varepsilon+\mathcal L(\varepsilon)<\rho.
\tag{3.10}
\]

整个初值球 $B_\varepsilon(s)$ 同时满足原预算，轨道均留在共同紧包络

\[
W=U_R\cap\overline B_{\varepsilon+\mathcal L(\varepsilon)}(s).
\]

其点尾上界对初值统一。完整 PPA 结论还须在整个 $W$，而非仅初值球，验证 $J_{\lambda F}=J_{\mathcal G}$。energy 用

\[
\mathcal L_E(d)=\frac{\sqrt{qV(d)}}{1-\sqrt q}
\]

替代 (3.9)，同理关闭共同域。

但共同紧包络 $W$ 未必对**其所有点**前向不变。不能为套 $C(K,K)$ 擅自宣称 $T(W)\subset W$。两个严谨处理是：

1. 采用共同初值域 $B$／轨道包络 $W$ 的局部 trace 图卡；
2. 对单个系统取 $K_{T,B}=\overline{\bigcup_{n\ge0}T^n(\overline B)}$。若留域有严格余量，则此集紧且 $T$-不变，统一尾界延拓到该集。

第二种 $K_{T,B}$ 随 $T$ 改变，所以还需要变量域图卡或共同空间识别定理，不能将其当作已经嵌入一个固定 $C(K,K)$ 的证明。公平比较时这项域信息须保留。

此外，$\Pi_T:B\to S\cap W$ 是局部极限／相位映射，不一定是 $B\to S\cap B$ 的回缩，因为极限可离开初值球。只有在含目标集的前向不变图卡上，才直接称作回缩。

## 4. 各证书究竟推出哪些内生性质

记 $d=d(x,S)$、$d^+=d(Tx,S)$、$s_x=\|x-Tx\|$。所有原算子 EB 均用全值集最小残差。

### 4.1 RLEB-direct

RL 加完整覆盖给唯一单步映射，并在受控比较尺度上有

\[
\|Tx-Ty\|\le\tfrac12(\delta+L\delta^\gamma),\quad
\delta=\|x-y\|.
\tag{4.1}
\]

direct 兼容给 $d^+\le\kappa d$，且

\[
\begin{split}
\|T^{k+1}x-T^kx\|&\le a_k^D(D)
=\tfrac12\big(\kappa^kD+L\kappa^{\gamma k}D^\gamma\big),\\
\|T^kx-\Pi_Tx\|&\le e_k^D(D)
=\tfrac12\left(\frac{\kappa^kD}{1-\kappa}
+\frac{L\kappa^{\gamma k}D^\gamma}{1-\kappa^\gamma}\right)
\end{split}
\tag{4.2}
\]

对共同初值域 $d(x,S)\le D$ 一致。因而它认证：局部全轨道存在唯一、距离 Q-线性、点 R-线性、有限长、一致极限、连续极限映射。**不**认证固定点集凸、唯一解或正 Hölder 阶的两初值稳定性。

它还给一个内生的 retraction-displacement 估计。由

\[
(1-\kappa)d(x,S)\le\|x-Tx\|
\]

可得

\[
\|x-\Pi_Tx\|\le
\mathcal L\!\left(\frac{\|x-Tx\|}{1-\kappa}\right)
\tag{4.3}
\]

在相关尺度内成立。这把 RLEB 送入一个明确的 $\chi$-weakly-Picard 类。该语言及其不变纤维分解已有文献，不能当作新发明；RLEB 在这里的贡献候选是从完整算子图及独立真实 EB 导出这一性质。

### 4.2 RLEB-energy

令

\[
V(r)=r^2+\lambda^2[\psi^{-1}(r)]^2,
\qquad A(r)=\tfrac12(r^2+L^2r^{2\gamma}).
\]

若 $A(r)\le qV(r)$、$0<q<1$，原定理给

\[
V(d_k)\le q^kV(d_0),\qquad
a_k^E(D)=q^{(k+1)/2}\sqrt{V(D)},\qquad
e_k^E(D)=\frac{q^{(k+1)/2}\sqrt{V(D)}}{1-\sqrt q}.
\tag{4.4}
\]

其域、唯一性和单步模与 all-pairs RL 相同；一般 gauge 下认证 $V(d_k)$ Q-线性和点误差 R-线性，**并不自动给距离本身的 Q-线性因子**。在线性 gauge 切片可另行得到距离 Q-线性。

对共同初值域，(4.4) 与 (4.2) 都能映入同一个中立尾预算，只需分别证明 $e_k^C\le e_k$、$a_k^C\le a_k$。不必强迫两份证书使用相同 $\gamma$ 或相同 gauge。

### 4.3 LT2025 all-pairs

在同一完整图卡，LT 的 scaled submonotonicity 等价于

\[
\|R_Tx-R_Ty\|\le L\|x-y\|,\qquad
L=\sqrt{1+4\tau},\qquad R_T=2T-I.
\tag{4.5}
\]

覆盖负责存在，all-pairs 负责唯一性和 Lipschitz，而不是由 maximality 一词凭空得到整个输入空间的完整解。原稿 LT 的矩形图裁剪与原完整 PPA 仍须对齐。

在线性输出 EB $d(u,S)\le\rho r_F(u)$ 下，LT 公共标量条件为

\[
2\tau(\lambda+\rho)^2<\lambda^2,\qquad
q_{LT}^2=1+2\tau-\left(\frac\lambda{\lambda+\rho}\right)^2<1.
\tag{4.6}
\]

用 (4.5) 比较最近解可独立得到

\[
s_x\le b\,d(x,S),\qquad b=\frac{1+L}{2},
\]

因此共同域上可取

\[
a_k^{LT}(D)=bDq_{LT}^k,
\qquad e_k^{LT}(D)=\frac{bDq_{LT}^k}{1-q_{LT}}.
\tag{4.7}
\]

它认证的动力结论与 (4.2) 同属于统一有限长／弱 Picard 层，并额外给有限单步 Lipschitz。maximal submonotonicity 还给局部值集与逆值集的闭性／弱凸函数下水平集表示（LT Theorem 1）；正 violation 不等同凸零集。单调、全域的经典端点则另有闭凸零集。

### 4.4 LT/LTT pointwise，相对 Fix

对允许关系 $\mathcal J$，设对所有允许 $u\in\mathcal J(x)$ 和 $p\in S=\operatorname{Fix}\mathcal J$，

\[
\|u-p\|^2+c\|x-u\|^2\le(1+\epsilon)\|x-p\|^2,
\quad c=\frac{1-\alpha}{\alpha}>0,
\tag{4.8}
\]

并有输入残差 EB

\[
d(x,S)\le\rho_T\inf_{u\in\mathcal J(x)}\|x-u\|.
\tag{4.9}
\]

则在 $0\le q_P^2=1+\epsilon-c/\rho_T^2<1$ 的范围，

\[
d(u,S)\le q_Pd(x,S),\qquad
\|x-u\|\le b_Pd(x,S),\quad
b_P=\frac{1+\sqrt{1+(1+c)\epsilon}}{1+c}.
\tag{4.10}
\]

第二式由 $(1+c)s_x^2-2ds_x-\epsilon d^2\le0$ 解二次式得到。每条允许轨道均有共同有限长和点尾

\[
e_k^P(D)=\frac{b_PDq_P^k}{1-q_P}.
\tag{4.11}
\]

但该证书一般**没有**解点外单值性、两点连续性、唯一极限选择或两点 Hölder 连续性。它只在每个固定点强制 $\mathcal J(p)=\{p\}$，并有相对该固定点的 calmness。

最小量词例是完整 $\mathcal J(x)=\{x/2,x/3\}$：(4.8) 可取 $c=1,\epsilon=0$，(4.9) 可取 $\rho_T=2$，而同一个输入有两个不同输出。这必须进入关系动力系统空间，不能被“所有连续单值映射”母空间默默遗漏。

LTT 的一般环域 gauge 定理（v2 Theorem 2.18／Corollary 2.19）首先保证距离趋零和分环域下降；没有统一 $q<1$ 或其他可和性时，不能从这一句推出全轨道统一有限长／统一点尾。要认证与 (4.2) 相同的结论，须加入实际能推出点尾的参数分支。

### 4.5 稳定性逐项标注

| 可见性质 | all-pairs RLEB | LT all-pairs | pointwise LT/LTT |
|---|---|---|---|
| 输入域内完整存在 | 需 coverage＋完整纤维核对 | 同样需核对 | 非空允许关系另给 |
| 解点外唯一单步 | 是 | 是 | 不保证 |
| 近解零集 | 完整 EB 作用区内等于目标 $S$ | 同接口下同样成立 | 以实际 Fix 为目标；解点吸收 |
| $S$ 凸 | 不保证 | 正 violation 不保证；经典全域单调端点另论 | 不保证 |
| 共同吸引域 | 严格长度预算推出 | 原局部定理／同一预算推出 | self-map／留域须单列 |
| 点收敛及统一尾 | direct／energy 严格分支有 | 严格线性分支有 | 统一严格线性分支有；一般 gauge 不自动有 |
| 初值极限连续 | 共同尾＋单步连续给 | 是 | 集合值／不连续情形不能称单值连续回缩 |
| 正阶两点 Hölder | $\gamma<1$ 不保证 | 有共同几何尾时保证某个正阶 | 仅解点 calmness 不能替代 |
| 算子扰动后的极限连续 | 共同尾层内有；离开层不保证 | 同样 | 需相应关系拓扑及图连续性，未由本表自动推出 |
| 改步长后沿用证书 | 不可默认 | 不可默认；完整全局 Lipschitz 图卡有窗口 | 不可默认 |

对连续单值情形，若单步 $K_1$-Lipschitz 且共同点尾 $M\sigma^n$，截断平衡给

\[
\operatorname{Hol}_{\theta}(\Pi_T)<\infty,
\quad\theta=\frac{\log(1/\sigma)}{\log K_1+\log(1/\sigma)}
\quad(K_1>1).
\tag{4.12}
\]

$K_1\le1$ 时极限非扩张。若只有 $0<\gamma<1$ 的单步 Hölder，则修订稿传递定理给

\[
\|\Pi_Tx-\Pi_Ty\|
\lesssim\left(\frac{\log\log(1/\delta)}{\log(1/\delta)}\right)^\beta,
\quad\beta=\frac{\log(1/\sigma)}{\log(1/\gamma)},
\tag{4.13}
\]

局部尺度须按修订稿截断归纳闭合。该保证比某个特定算子实际正则性可能弱得多，不能把最坏证书模当作每个成员的精确模。

## 5. 共同的证书 calculus：包含关系怎样才算真的证明

### 5.1 一个不以理论名称定义的过渡模板

让单步关系满足

\[
\|u-p\|^2+a\|x-u\|^2\le A(d),\quad a>0,\quad p\in P_Sx.
\tag{5.1}
\]

则步长上界为

\[
s_x\le b_A(d):=
\frac{d+\sqrt{(1+a)A(d)-ad^2}}{1+a}
\tag{5.2}
\]

（在有允许转移的尺度上根号自然非负）。有三个独立证书通道：

1. **输出 direct**：$d^+\le\psi(s_x/\lambda)$，以及 $\psi(b_A(d)/\lambda)\le\kappa d$；
2. **输出 energy**：$V_a(r)=r^2+a\lambda^2[\psi^{-1}(r)]^2$，以及 $A(r)\le qV_a(r)$；
3. **输入 residual**：$d\le\chi(s_x)$，以及 $A(d)-a[\chi^{-1}(d)]^2\le\kappa^2d^2$。

再配相同的覆盖、全选择量词、共同域和可和步长，就得到相同的点收敛输出。RLEB 对应 $a=1,A=(d^2+L^2d^{2\gamma})/2$；pointwise AA 对应 $a=(1-\alpha)/\alpha,A=(1+\epsilon)d^2$。这是一套标准不等式／求和推导的证书语言，不能仅凭新记号申报新理论。

### 5.2 LT2025 进入原 RLEB-energy：不需要改存在量词

原 RLEB 已有 energy 分支。在同一完整、自映射工作图卡，令

\[
\gamma=1,\quad L^2=1+4\tau,\quad\psi(t)=\rho t.
\]

这里取 $\rho>0$。若原 EB 常数为零，则实际输出已经落在 $S$；可单列一步终止，或利用 LT 严格阈值的余量将 $\rho$ 放大成足够小的正数，不能对零 gauge 使用普通逆函数。

则

\[
q_E=(1+2\tau)\frac{\rho^2}{\rho^2+\lambda^2}<1
\quad\Longleftrightarrow\quad2\tau\rho^2<\lambda^2.
\tag{5.3}
\]

(4.6) 蕴含 (5.3)。所以公共完整接口上

\[
\mathsf{LT}_{\rm ap,cert}\longrightarrow
\mathsf{RLEB}_{E,\gamma=1}
\tag{5.4}
\]

是一条已有原稿公式能证明的**证书转换**。若工作域不是自映射图卡，应同时转换／缩小局部化预算；不能据标量阈值比较就宣称相同大初值域自动成立。允许缩域的 germ 包含与固定初值域的证书支配是两种命题。

只使用 direct 分支时，确实不包含全部 LT；但这属于证书通道选择问题，不应充当新母空间搭建的主要障碍。若将“RLEB 框架”明确定义为原稿 direct 或 energy 至少一种证书存在，(5.4) 不需要新的收敛原理。

### 5.3 包含完整 LTT pointwise 需要的改变

仅调整存在性／coverage 不能把多值 pointwise 关系变成 all-pairs RL；上文 $\{x/2,x/3\}$ 的同输入冲突已经说明逻辑差别。

如要在一个统一 RLEB 总框架中包含它，应明列：允许关系分支；把 all-pairs 几何推广为相对最近解的 (5.1)；允许一般 $a>0$；增加输入 EB 通道。原稿 selection-uniform corollary 已提供其中一部分。

此时“包含 LTT”是统一模板的短转换定理；把 LTT 证书作为额外标签直接取并集则只是定义。真正有意义的成果应是：统一模板带来此前不显然的性质、最优模、闭包／泛型结构或可验证新覆盖，而不只是重新命名并集。

### 5.4 包含与不可比的逻辑边界

以下只核准类之间的逻辑关系，**不把反例当作类大小的依据**。

- 固定完整接口、允许缩小局部化域时，LT2025 公共收敛证书可转入 RLEB-energy。direct 单独不是上位类：在 $\lambda=1$，$F(p,r)=(0,r/2)$ 是 maximal monotone，线性真实 EB 最佳常数为 $2$。切向恒等迫使 $\gamma=1$ 时 $L\ge1$，故任意有效 gauge 的 direct 商至少 $1+L\ge2$；$\gamma<1$ 时该商发散。energy 则给距离因子 $2/\sqrt5<1$。
- 完整 pointwise-AA 关系类不包含于 all-pairs RLEB：$F(u)=\{u,2u\}$ 的完整 resolvent $\{x/2,x/3\}$ 已给出同输入两个输出。
- all-pairs RLEB 也不包含于完整邻域上的 pointwise-AA 类。原稿平方根接缝在 $\lambda=1$ 为

\[
F(\xi,y)=\{(-2\sqrt y,3y),(-2\sqrt y,-5y)\}\quad(y\ge0),
\qquad T(p,r)=(p+\sqrt{|r|},|r|/4).
\]

  在 $y<0$ 取 $F(\xi,y)=\varnothing$。其完整真实 EB 为 $d((\xi,y),S)\le r_F(\xi,y)^2/4$；all-pairs RL 可取 $\gamma=1/2$、$L_R=2+\tfrac32\sqrt R$，direct 兼容因子为 $\kappa_R=(2+\tfrac52\sqrt R)^2/16<1$（$0<R<16/25$）。但在 $s=(0,0)$，

\[
\frac{\|T(0,t)-s\|}{\|(0,t)-s\|}
=\frac{\sqrt{t+t^2/16}}{t}\longrightarrow\infty.
\]

  因此不可能满足同一完整输入邻域、锚定 $s$、有限 $\epsilon$ 的 (4.8)。这说明 all-pairs RLEB 与完整 pointwise-AA 关系框架没有未经限定的包含链；改步长、限制比较域或更换算法量词后需另作命题。

## 6. direct 与 energy 的规范 gauge 定理

本节两项规范化已经过 [07_embedding_math_audit.md](sandbox:/workspace/scratch/bf20ae56bc4b/ppa_system_team/07_embedding_math_audit.md) 的独立数学复核。该审核确认数学正确性，不判定文献首创性。

### 6.1 Direct：保留原兼容常数

**命题 6.1（实际输出预算上的无损规范化）。** 给定原 direct-RLEB 数据 $\lambda>0,0<\gamma\le1,L\ge0,R>0,0<\kappa<1$。设

\[
h(r)=\frac{r+Lr^\gamma}{2\lambda},\qquad0\le r\le R.
\tag{6.1}
\]

若原单调 gauge 满足 $\psi(h(r))\le\kappa r$，则可在 gauge 区间 $[0,h(R)]$ 上无损换成

\[
\widehat\psi(t)=\kappa h^{-1}(t).
\tag{6.2}
\]

它连续、严格递增、零点为零，保留所有实际覆盖输出上的真实 EB，并以同一个 $\kappa$ 满足 direct 兼容。

**证明。** $h$ 连续严格递增。令 $t=h(r)$，则

\[
\psi(t)\le\kappa h^{-1}(t)=\widehat\psi(t).
\]

所有覆盖输出 $u=J_{\mathcal G}(x)$ 已由原 RL step bound 满足 $r_F(u)\le h(R)$，故

\[
d(u,S)\le\psi(r_F(u))\le\widehat\psi(r_F(u)).
\]

同时 $\widehat\psi(h(r))=\kappa r$。缩小 gauge 定义域到 $h(R)$ 不遗漏任何实际输出。证毕。

这个命题并不把原来在更大输出域上成立的外部 EB 全部保留下来；其等价范围正是原局部定理实际调用的输出。它也不声称验证规范 gauge 比验证原独立 EB 更容易。

**意义。** 对固定完整工作接口，direct “存在某个任意单调 gauge 证书”可化为只存在 $\gamma,L,\kappa$ 等有限实参数；无理临界指数完整保留。因此不能再泛泛说 direct 类必须因任意 gauge 投影而可能非 Borel。

### 6.2 Energy：允许放宽因子的有限参数规范化

**定理 6.2（已独立复核，固定完整紧图卡）。** 固定非空紧 $K\subset\mathbb R^n$、非空闭 $S\subset K$、$\lambda>0$、$R>0$ 且 $R\ge\sup_Kd(\cdot,S)$。取 $T\in C(K,K)$、$T|_S=I$，源算子确为 (2.3) 的完整 $F_{T,K}$。设 all-pairs RL 参数为 $0<\gamma\le1,L\ge0$，普通连续严格增 gauge 的逆 $\alpha=\psi^{-1}$ 在 $[0,R]$ 上有定义，且

\[
\alpha(d(y,S))\le r_F(y)\quad(y\in T(K)),\qquad
A(r)\le q\{r^2+\lambda^2\alpha(r)^2\},
\quad A(r)=\frac{r^2+L^2r^{2\gamma}}2,\quad0<q<1.
\tag{6.3}
\]

则可以用有限参数逆 gauge

\[
\widehat\alpha(r)=u_{q'}(r)+\eta r,\qquad
u_b(r)=\max_{0\le s\le r}g_b(s),\qquad
g_b(s)=\lambda^{-1}\sqrt{[A(s)/b-s^2]_+},
\quad r\ge0,
\tag{6.4}
\]

其中 $q<q'<1$、$\eta>0$，得到同一 $T$ 的严格 energy 证书。$L=0$ 时可先无损改取 $\gamma=1$。所有函数在 (6.4) 中直接定义于**全部 $r\ge0$**；于是 $\widehat\alpha$ 连续严格增、从零开始且无界，

\[
\widehat\psi=\widehat\alpha^{-1}:[0,\infty)\to[0,\infty)
\]

完整有定义，覆盖所有实际残差，不存在只给 inverse 小定义域后越界调用的问题。

该定理保持“存在 energy 证书”的成员资格；不承诺保留原 $q$、原 gauge、最优尾模或原局部化长度预算。

**证明。** 由 (6.3) 得 $\alpha\ge g_q$，再由 $\alpha$ 单调得 $\alpha(r)\ge u_q(r)$，$0\le r\le R$。分三支。

1. 若 $0<\gamma<1,L>0$，任取 $q'\in(q,1)$。对每个 $r>0$，$g_{q'}(s)>0$ 在足够小的正 $s$ 成立，所以 $u_{q'}(r)>0$。在其正最大点 $s_*$ 比较，$g_q(s_*)>g_{q'}(s_*)$，故 $u_q(r)>u_{q'}(r)$。近零时两函数的 running maximum 等于自身，并且

\[
\frac{u_q(r)-u_{q'}(r)}r
\sim \frac{L}{\lambda\sqrt2}
\left(q^{-1/2}-(q')^{-1/2}\right)r^{\gamma-1}
\longrightarrow+\infty.
\]

因此连续性与紧性给

\[
c_*=\inf_{0<r\le R}\frac{u_q(r)-u_{q'}(r)}r>0.
\tag{6.5}
\]

取 $0<\eta\le c_*$，则 $\widehat\alpha\le u_q\le\alpha$ 在 $[0,R]$ 成立，故保留真实 EB；同时 $\widehat\alpha\ge g_{q'}$，所以

\[
A(r)\le q'\{r^2+\lambda^2\widehat\alpha(r)^2\},
\qquad0\le r\le R.
\tag{6.6}
\]

2. 若 $\gamma=1$ 且 $a=(1+L^2)/2>q$，则

\[
\frac{u_q(r)-u_{q'}(r)}r
=\lambda^{-1}\left(\sqrt{a/q-1}
-\sqrt{[a/q'-1]_+}\right)>0.
\]

再次取足够小的 $\eta>0$，同样得到真实 EB 与 (6.6)。

3. 若 $\gamma=1$ 且 $a\le q<1$，不能假设 running-max 间隙为正。此时 $L<1$，令 $c=(1+L)/2<1$。与最近解比较 RL，再用距离函数的 1-Lipschitz 性，独立得到

\[
d(Tx,S)\le c\,d(x,S),\qquad
\|x-Tx\|\ge(1-c)d(x,S).
\]

对每个输出 $y$ 的**全部纤维**取最小值，才得到真 EB

\[
d(y,S)\le\frac{\lambda c}{1-c}r_F(y).
\tag{6.7}
\]

取 $q'\in(q,1)$，有 $u_{q'}=0$。令 $\eta=(1-c)/(\lambda c)$，则 $\widehat\alpha(r)=\eta r$ 满足真实 EB 及 (6.6)。这一支的新 inverse 未必小于旧 $\alpha$；正确性来自完整纤维下独立重证的 (6.7)，不来自旧 gauge 的逐点放大。

最后，$L=0$ 时 RL 右端恒零，且 $A(r)=r^2/2$，均与 $\gamma$ 无关；改为 $\gamma=1$ 后归入线性两支。$\eta>0$ 保证 (6.4) 的全域 inverse 性质。证毕。

**范围。** 非退化分支的标量规范化可以在更一般接口单独使用，但本定理及后面的统一 $F_\sigma$ 结论固定的是完整 $F_{T,K}$。特别是 (6.7) 不能在删掉外部残差纤维后冒称原全局算子的 EB。

## 7. Certificate bundle 与像集的可测结构

### 7.1 定义及两种统计对象

令 $\mathfrak X$ 为选定的无标签 PPA 系统空间。证书型 $C$ 的 witness 参数空间为 $P_C$，其中保留局部域、完整性证明所需数据、策略量词和数值参数。定义

\[
\mathfrak B_C=\{(\xi,c)\in\mathfrak X\times P_C:
c\text{ 是 }\xi\text{ 的有效 }C\text{ 证书}\},
\qquad \pi_C(\xi,c)=\xi.
\tag{7.1}
\]

真正比较的是

\[
\mathfrak R_C=\pi_C(\mathfrak B_C),
\quad\mathfrak R_C\cap\mathfrak C(K,S;e),
\tag{7.2}
\]

不是 $\mathfrak B_C$ 的标签数量或纲。

若 $\mathfrak X,P_C$ 是标准 Borel／Polish 且有效证书关系 Borel，则像是 analytic，因而在 Polish 母空间具有 Baire 性质。**连续投影本身不保留第一纲或残集**。即使投影开放，也不能把任意 witness 子集的第一纲直接传到像；开放满射的相应范畴桥梁适用于底层集合与其饱和逆像，还需相应 Baire 性质。本文的 $F_\sigma$ 论证使用闭证书关系与紧参数投影，不使用“投影保纲”。

### 7.2 标准紧完整图卡下的 $F_\sigma$ 结论

这里给一条完全可核、但范围明确的编码：固定非空紧 $K$、非空闭 $S\subset K$、$R>0$ 且 $R\ge\sup_Kd(\cdot,S)$、$\lambda>0$，使用 (2.3) 的完整源算子。令

\[
P_j=\{(\gamma,L,\kappa):1/j\le\gamma\le1,
0\le L\le j,\ 1/j\le\kappa\le1-1/j\}.
\]

在 $C(K,K)\times P_j$ 上要求 $T|_S=I$，all-pairs RL 对 $\|x-y\|\le R$ 成立，以及对全部 $x\in K$

\[
d(Tx,S)\le\kappa R,
\qquad
\frac{d(Tx,S)/\kappa+L[d(Tx,S)/\kappa]^\gamma}{2}
\le\|x-Tx\|.
\tag{7.3}
\]

(7.3) 正是规范 gauge 的全部纤维 EB；第一式负责 inverse 的尺度。所有条件联合闭：参数有正指数下界，避免 $0^0$ 极限；固定测试尺度和域避免边界量词漂移。参数盒紧，所以遗忘参数后的像闭。对 $j$ 可数并，得到

\[
\boxed{\text{该标准完整图卡的全部 direct-RLEB 可认证类是 }F_\sigma.}
\tag{7.4}
\]

这里没有把实指数近似成有理数。对临界 $\gamma\theta=1$，这种有理网格替代可能丢失成员。若某证书允许 $\kappa=0$，可将它放大成任意正的 $\kappa<1$，不丢失可认证对象。

这些闭片都由统一参数预算给出一致有限长，故已在中立一致迭代收敛空间内。由于 $d_{\rm dyn}$ 强于单步一致拓扑，同一可认证类在该中立 $d_{\rm dyn}$ 图卡中也为 $F_\sigma$；与任意共同结论层 (3.5) 相交后仍是相对 $F_\sigma$。这是可测性结论，不蕴含其为第一纲、第二纲或稠密。

相同接口下，LT 公共 all-pairs 几何＋线性 EB＋严格标量阈值也可用紧实常数盒和可数严格余量编码成 $F_\sigma$。一般连续严格增 energy gauge 在本固定完整图卡中也能升级为 $F_\sigma$，见下一节；这不是仅限 power gauge 的结论。

**边界：**(7.4) 不是对任意外层原图 $F$、任意可变局部图块、所有步长策略的无条件 $F_\sigma$ 声明。若 $F$ 还有图卡外残差纤维，必须补完整图量词；若把 LT 原论文矩形 maximality 原样放入 bundle，也须独立编码该条件，不能把公共 transition 证书的 $F_\sigma$ 无证外推。

### 7.3 全部普通 energy gauge 的 $F_\sigma$ 编码

定理 6.2 及其反向给出准确等价：存在普通连续严格增 gauge 的 energy 证书，当且仅当存在

\[
0<\gamma\le1,\quad L\ge0,\quad0<q<1,\quad\eta>0
\]

使 all-pairs RL 成立，并且

\[
u_q(d(Tx,S))+\eta d(Tx,S)
\le\frac{\|x-Tx\|}{\lambda}\qquad(\forall x\in K).
\tag{7.5}
\]

反向证明不是仅检查选中残差：对每个 $y$ 的全部逆纤维取最小值，得到 $\widehat\alpha(d(y,S))\le r_F(y)$；再由 $\widehat\alpha\ge g_q$ 得 energy 兼容。全域 $\widehat\psi=\widehat\alpha^{-1}$ 保证残差定义域完整。

取紧参数盒

\[
Q_j=\{(\gamma,L,q,\eta):
1/j\le\gamma\le1,\ 0\le L\le j,\
1/j\le q\le1-1/j,\ 1/j\le\eta\le j\}.
\tag{7.6}
\]

令 $s=rt$，可写

\[
u_q(r)=\lambda^{-1}\max_{0\le t\le1}
\sqrt{\left[\frac{(rt)^2+L^2(rt)^{2\gamma}}{2q}-(rt)^2\right]_+}.
\]

被最大化函数在紧参数盒、$0\le r\le R$、$0\le t\le1$ 上联合连续，故最大值也联合连续。于是 $T|_S=I$、RL 与 (7.5) 定义联合闭证书关系。紧参数投影闭，可数并给出

\[
\boxed{\mathfrak R_E\text{ 及 }\mathfrak R_D\cup\mathfrak R_E
\text{ 在该标准完整紧图卡内均为 }F_\sigma.}
\tag{7.7}
\]

每个盒中 $q\le1-1/j$，且

\[
V(R)=R^2+\lambda^2[u_q(R)+\eta R]^2
\]

有共同有限上界；由 (4.4) 得真正共同的有限长与点尾。因此这些闭片确实位于中立一致迭代收敛空间，非仅形式上闭的伪证书。按 §7.2 的恒等嵌入论证，(7.7) 在 $d_{\rm dyn}$ 图卡以及任意共同结论预算层中仍为相对 $F_\sigma$。

这没有证明类的纲大小，也没有证明新证书支配原尾预算。一般外层 certificate bundle 若没有这里的完整紧图卡与规范化条件，仍只保留 §7.1 的有条件 analytic 上界。

### 7.4 一致收敛类及策略量词的描述复杂度

在固定紧 $K$ 的单步一致拓扑，$T^n$ 一致 Cauchy 的量词形式是

\[
\bigcap_{j\ge1}\ \bigcup_{N\ge1}\ \bigcap_{m,n\ge N}
\{T:\|T^m-T^n\|_\infty\le1/j\}.
\tag{7.8}
\]

所以该裸动力学类本身是 Borel；它不需由 RLEB 或 LT 的证书定义。

“存在步长／存在证书”通常再加一个实参数投影，安全结论可到 analytic；“每个步长／每个无限策略均有某种证书”含不可数全称量词，不能一概断言仍 analytic。若用**同一个共同证书**控制一整个策略族，则其有限字转移不等式可以另外做可数／紧量词编码；这与每条策略各自存在证书并不相同。

## 8. 步长变化和变步长策略

### 8.1 同一原算子的步长变化不是任意重新选映射

若 $T=J_{\lambda F}$ 是完整单值图表示，令 $c=\mu/\lambda$，

\[
Q_c=cI+(1-c)T.
\]

逐图点计算得到精确关系

\[
\operatorname{gph}J_{\mu F}
=\{(Q_cx,Tx):x\in\operatorname{dom}T\},
\qquad J_{\mu F}=T\circ Q_c^{-1}
\tag{8.1}
\]

其中逆是关系逆，不能先假定单值或满射。对局部图块，(8.1) 只表示该块，除非完整纤维另行成立。

若全空间 $R_T$ 为 $L$-Lipschitz，则

\[
Q_c=\frac{1+c}{2}I+\frac{1-c}{2}R_T.
\]

当 $1+c>|1-c|L$ 时，Banach 不动点论证给 $Q_c$ 全域双 Lipschitz，因而新步长完整 resolvent 存在唯一，且

\[
\operatorname{Lip}(R_{J_{\mu F}})
\le\frac{|1-c|+(1+c)L}{(1+c)-|1-c|L}.
\tag{8.2}
\]

右侧在 $c\to1$ 时趋于 $L$。配严格数值余量可在适当共同域保持证书，但纯局部 Lipschitz 不排除远处图纤维侵入新输入邻域；故不能默认整个原 $F$ 有同一完整窗口。对纯 Hölder $\gamma<1$ 图几何，(8.2) 的线性逆下界一般不成立。

### 8.2 从固定步长提升到一整个策略族，需要什么

若所有 $\lambda\in I$ 的完整 resolvent 在共同轨道区有统一覆盖，同一 $S$、$\gamma,L$、输出 EB 及统一 $0<\kappa<1$，且

\[
\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right)\le\kappa r
\quad(\lambda\in I,0<r\le R),
\tag{8.3}
\]

还须使 gauge 尺度 $(R+LR^\gamma)/(2\lambda)\le\bar t$ 对全部 $\lambda\in I$ 成立，并用同一个严格长度余量关闭整个策略族的留域预算。在这些条件下，同一个距离／步长求和证明逐步适用于任意 $\lambda_k\in I$；(4.2) 仍是所有策略和允许轨道共同的尾界。这是可直接证明的 uniform-certificate 扩展，非固定步长定理自动包含的量词。

energy 若随 $\lambda_k$ 使用不同 $V_\lambda$，不能直接把 $V_{\lambda_{k+1}}$ 和 $V_{\lambda_k}$ 的收缩串起来；需要同一个 Lyapunov 函数，或明确的可和比较因子。LT 的共同距离因子 $q<1$、共同线性步长界则可直接串接。

即使每个固定步长都收敛，也不保证任意变步长收敛到零集。对 $F=I$ 的

\[
x_{k+1}=\frac{x_k}{1+\lambda_k}
\]

取 $\lambda_k>0$、$\sum_k\lambda_k<\infty$，非零初值的乘积极限仍非零。公平比较必须固定例如 $I=[\lambda_-,\lambda_+]$、$\lambda_->0$，或另行指定允许策略预算。

不同策略还可能选出不同解。一般只能得到 $\Pi_{F,\boldsymbol\lambda}$ 或策略相关极限关系，不能宣称一个不依赖策略的 $\Pi_F$。

## 9. 建议使用的公平比较定义

预先给出结论预算

\[
b=(\text{状态域／初值域},S,\Sigma,
\text{完整分支量词},e_n,a_n,\text{可选极限稳定模}).
\tag{9.1}
\]

先由这些**动力学输出**定义 $\mathfrak X_b$，再定义

\[
\mathfrak R_C(b)=\{\xi\in\mathfrak X_b:
\exists\,C\text{ 证书，其推出的输出逐项不劣于 }b\}.
\tag{9.2}
\]

这样可以同时比较四个区域：两者都认证、仅 RLEB、仅 LT、两者都未认证。若 (5.4) 在该固定预算上保输出成立，“仅 LT”区可能为空；若证书域预算不同，就须先处理该差异，不能强画包含箭头。

对原算子 $F$，还可记录可认证的**性能集合**

\[
\mathcal P_C(F)=\{b:F\text{ 在策略预算 }b\text{ 下有 }C\text{ 证书}\}.
\tag{9.3}
\]

这比“存在某个常数所以覆盖／不覆盖”更有区分力：可能两理论都覆盖某个算子，却给出不同共同吸引域、步长范围、尾模或解选择稳定性。后续范畴研究可考察 $\mathfrak R_R(b)\setminus\mathfrak R_{LT}(b)$ 的相对内部、闭包和纲；**本报告没有预设其答案必为 residual。**

可作为证书无关内生坐标的还有：完整反射振荡模 $\Omega_{F,\lambda}(r)$、真实输出残差剖面 $\mathcal E_{F,V}(t)$、最坏轨道尾 $\tau_{F,\Sigma,B}(n)$ 与极限回缩模。RL／LT／EB 只是这些内生剖面的不同上界证书。先建这些坐标的稳定性、下半连续性及表示定理，再做类的大小比较，符合“空间结构先行”的研究目标。

## 10. 文献定位与仍待完成

### 已核对的原始入口

1. Luke–Tam，*Generalized Monotonicity and the Proximal Point Algorithm*，DOI [10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863)：Definition 2、Propositions 3–4、Theorem 1、Lemma 1、Assumption 2、Theorem 2。本文的 (4.5)–(4.7) 是同接口独立推导；未将其局部选取轨道冒充全局完整 PPA。
2. Luke–Thao–Tam，*Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings*，DOI [10.1287/moor.2017.0898](https://doi.org/10.1287/moor.2017.0898)，[arXiv:1605.05725v2](https://arxiv.org/abs/1605.05725v2)：本报告 Definition 2.3、Propositions 2.4／2.6／2.8、Theorem 2.18、Corollary 2.19 按 v2 编号。其 pointwise、相对域、环域 gauge 结构不能缩成 all-pairs Lipschitz 一句话。
3. 同三位作者，*Implicit Error Bounds for Picard Iterations on Hilbert Spaces*，DOI [10.1007/s10013-018-0279-x](https://doi.org/10.1007/s10013-018-0279-x)：Theorems 1–2 将正则模传到强收敛；Theorem 4 从共同距离下降推出输入残差模。这里已有“把动力性质转为误差界”的体系化先例；它不等同原算子真实输出 EB，也不直接覆盖 RLEB 的非 Fejér 动力。
4. Ioan A. Rus，*Relevant Classes of Weakly Picard Operators*，54(2), 131–147 (2016)，DOI [10.1515/awutm-2016-0019](https://doi.org/10.1515/awutm-2016-0019)，[作者全文](https://www.researchgate.net/publication/312565303_Relevant_Classes_of_Weakly_Picard_Operators)：§0 定义 WPO、$\psi$-WPO 及极限纤维分解；Theorem 1.1 的有限长到 retraction-displacement 桥、Lemma 4.1 的 Caristi／总长联系。本文 (4.3) 是原 RLEB 数据送入已有结构的直接推导，不主张先造出 WPO 理论。

### 本轮可保留的结论

- 已建立正确的 certificate-bundle／forgetful-map 比较口径；
- 已给 RLEB／LT／pointwise LTT 的定量动力性质翻译和同结论预算比较；
- 已证 direct 任意单调 gauge 的规范化，保留原兼容常数；
- 已独立复核普通连续严格增 energy gauge 的有限参数逆模规范化；在标准完整紧图卡内，direct、energy 及其并均为 $F_\sigma$；
- 已分清 fixed／existential／universal／switching 步长量词；
- 已明确 LT2025 公共证书进入原 RLEB-energy 的条件，不再把这件小事当主要研究障碍。

### 还没有完成

1. 外层全闭图空间内“每条完整 PPA 都点收敛”的最终拓扑／描述复杂度；
2. 局部完整图卡与变量吸引域之间的全局 atlas／范畴保持嵌入；
3. 各 $\mathfrak R_C(b)$ 在选定中立母空间的实际纲分类；
4. 将已证固定完整图卡规范形式推广到原全局图、变量域／解集／步长的统一编码，以及规范化引理的文献优先权；
5. 对所有变步长策略的共同 Lyapunov 证书与极限选择结构；
6. 内生剖面坐标的表示、连续性、闭包和结构定理。

**最终判断：体系化方向可以推进，而且已经能把原 RLEB 的结论准确送入既有弱 Picard／统一迭代极限语言。下一承重问题是中立母空间上的表示、嵌入和类结构；当前不能再用某个特选尖点层的第一纲结论代替它。**
