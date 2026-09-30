# 冻结完整原算子图卡内的对象侧分类：闭紧块、跨步长必要层与未决修改引理

日期：2026-09-20。任务边界：不使用“证书空间第一纲，所以遗忘证书后的像第一纲”。本报告从无标签对象 $F$／其一一对应的完整 resolvent $T$ 出发。已读取 `ppa_system_team/03_certificate_embeddings.md`、`07_embedding_math_audit.md`、`01_ambient_axioms.md`、`02_convergence_topology.md` 及上一轮任意步长排除引理的完整证明。本报告没有重新审查原 RLEB 主定理，也没有宣称最终母空间上的 RLEB–LT 大小比较已完成。

## 0. 本轮结论

1. **对象侧编码已完成。** 在 03/07 明确核准的完整紧图卡，direct-RLEB、ordinary-gauge energy-RLEB 和 LT 公共 all-pairs 收敛证书类，都有显式的对象侧连续“最小违约量”。它们是可数个闭紧对象块的并，故不仅是 $F_\sigma$，而且是 $K_\sigma$（σ紧）。这里紧参数只用于消去数值存在量词，未用任何投影保纲规则。
2. **两种拓扑均处理。** 每一证书预算块有共同实际尾界，因而它在单步 AW 拓扑和全轨道 $d_{\rm dyn}$ 拓扑均紧。在预先冻结的共同实际尾层，两种拓扑相同；离开共同尾层，不转移任何范畴结论。
3. **新的必要层桥梁成立。** direct 与 energy 两分支都推出 $d(Tx,S)\le d(x,S)$。因此只要 $S$ 在某 $s\in S$ 附近是仿射片，乃至 $C^1$ 嵌入流形，任意正步长下的 LT 局部 all-pairs 图证书，都迫使原固定步长 $T$ 满足局部线性位移界 $\|Tx-x\|\le C d(x,S)$。这一结论不再需要上一轮预置的超吸引条件。
4. **没有得到中立层的无内点定理。** 精确剩余问题是第 7 节的对象侧局部修改引理：在同一实际尾预算和同一解集下、对任意 RLEB 对象的任意相对邻域，能否保留完整纤维证书并打破给定的线性位移界？
5. **比较分母还有 Baire 检查。** 中立共同尾层是 Baire，不代表 RLEB 子类也是 Baire。若 RLEB 在自身拓扑中第一纲，则“LT 在 RLEB 中第一纲”可能是无鉴别力的真话。不能省略这一检查。

## 1. 精确冻结的原对象与拓扑

固定非空紧 $K\subset\mathbb R^d$、非空闭 $S\subset K$、$\lambda>0$ 和

\[
R\ge\sup_{x\in K}d(x,S),\qquad R>0.
\]

取中立对象图卡

\[
\mathcal A_S=\{T\in C(K,K):T|_S=I\},
\qquad
F_T(y)=\{(x-y)/\lambda:x\in K,\ Tx=y\}.
\tag{1.1}
\]

这是整个原算子的定义，不是从某个已给全局 $F$ 上删掉外部图点。完整恒等式为

\[
\operatorname{dom}J_{\lambda F_T}=K,
\qquad J_{\lambda F_T}|_K=T,
\qquad
r_{F_T}(y)=\frac1\lambda\min_{x\in K:Tx=y}\|x-y\|
\quad(y\in T(K)).
\tag{1.2}
\]

图坐标

\[
(x,Tx)\longmapsto (Tx,(x-Tx)/\lambda)
\tag{1.3}
\]

是可逆线性变换；因此 $T\mapsto F_T$ 一一对应且保留全部逆纤维。

在此图卡内，原算子 AW 图拓扑等价于 $\|T-U\|_\infty$ 拓扑。理由：所有图位于同一个紧集内，AW 与 Hausdorff 图拓扑一致；图收敛到连续图时，极限映射的一致连续性把图距离转成一致函数距离。再用 (1.3)。

**边界。** 下文的完整 $K_\sigma$ 结论目前不包含：任意全局原算子的外部图纤维、可变局部域、存在任意步长的完整认证类、原 LT 矩形 maximality 的完整编码。它证明的是统一体系中的一张合法无标签图卡，不是重新宣布全部原算子问题已解决。若把原全局 $F$ 裁成 (1.1)，便改变了本体，不能借本报告掩盖此事。

记

\[
\Delta_T(x)=\|x-Tx\|,
\quad a_T(x)=d(Tx,S),
\quad R_T=2T-I,
\quad Q_R=\{(x,z)\in K^2:\|x-z\|\le R\}.
\tag{1.4}
\]

## 2. 不留任意 gauge 量词的对象侧连续测试

### 2.1 Direct-RLEB

对 $j\ge3$ 令

\[
P_j=\{(\gamma,L,\kappa):
1/j\le\gamma\le1,\ 0\le L\le j,
1/j\le\kappa\le1-1/j\}.
\]

定义联合连续违约函数

\[
\begin{aligned}
G_D(T;\gamma,L,\kappa)=\max\Bigg\{&
\max_{(x,z)\in Q_R}
\big[\|R_Tx-R_Tz\|-L\|x-z\|^\gamma\big],\\
&\max_{x\in K}[a_T(x)-\kappa R],\\
&\max_{x\in K}\left[
\frac{a_T(x)/\kappa+L[a_T(x)/\kappa]^\gamma}{2}
-\Delta_T(x)\right]\Bigg\}.
\end{aligned}
\tag{2.1}
\]

设

\[
g^D_j(T)=\min_{\theta\in P_j}G_D(T;\theta),
\qquad
D_j=\{T\in\mathcal A_S:g^D_j(T)\le0\}.
\tag{2.2}
\]

紧指标集上的最大／最小保持连续，所以 $g^D_j$ 是对象 $T$ 的连续函数，$D_j$ 闭。由于 $x=z$ 的测试给零，事实上 $G_D,g_j^D\ge0$，故也可写成零水平集。

03/07 的规范化恰给

\[
\mathcal R_D=\bigcup_{j\ge3}D_j.
\tag{2.3}
\]

全纤维语义未丢失：(2.1) 的最后一行对每个输出 $y$ 的所有 $x\in T^{-1}(y)$ 同时成立，取最小值才得到真正的规范 EB。第二行是 inverse 的尺度条件，不能删除。此编码没有把临界实指数换成有理指数。

### 2.2 Ordinary-gauge energy-RLEB

令

\[
A_{\gamma,L}(r)=\frac{r^2+L^2r^{2\gamma}}2,
\qquad
u_{\gamma,L,q}(r)
=\frac1\lambda\max_{0\le v\le r}
\sqrt{[A_{\gamma,L}(v)/q-v^2]_+}.
\tag{2.4}
\]

取紧盒

\[
Q_j=\{(\gamma,L,q,\eta):
1/j\le\gamma\le1,\ 0\le L\le j,
1/j\le q\le1-1/j,\ 1/j\le\eta\le j\}.
\]

定义

\[
\begin{aligned}
G_E(T;\gamma,L,q,\eta)=\max\Bigg\{&
\max_{(x,z)\in Q_R}
[\|R_Tx-R_Tz\|-L\|x-z\|^\gamma],\\
&\max_{x\in K}\left[
u_{\gamma,L,q}(a_T(x))+\eta a_T(x)
-\Delta_T(x)/\lambda\right]\Bigg\},
\\
g_j^E(T)&=\min_{\theta\in Q_j}G_E(T;\theta),
\qquad E_j=\{g_j^E\le0\}.
\end{aligned}
\tag{2.5}
\]

把 (2.4) 写成 $v=rt,\ 0\le t\le1$，联合连续性直接成立。因此 $g_j^E$ 连续、$E_j$ 闭，03/07 的规范化给出准确成员资格等式

\[
\mathcal R_E=\bigcup_{j\ge3}E_j.
\tag{2.6}
\]

这里的 energy 类使用普通连续严格增 gauge；规范 inverse 为 $u_{\gamma,L,q}(r)+\eta r$，并非任意不连续广义逆。规范化保留“存在证书”，不保证原证书最优尾常数。

### 2.3 LT 公共 all-pairs 收敛接口

本节编码的是与 RLEB 可直接对齐的公共证书：完整单值接口、all-pairs submonotonicity、真实线性输出 EB 与严格 LT 标量阈值。未把所有 LTT pointwise／多值框架混成此类。

取紧参数集

\[
H_j=\left\{(\tau,\rho):0\le\tau\le j,\quad
1/j\le\rho\le j,\quad
2\tau(\lambda+\rho)^2\le\lambda^2(1-1/j)\right\}.
\tag{2.7}
\]

有限负 violation 可无损放宽为 $\tau=0$；真实 EB 常数为零时，可放大成充分小的正数。定义

\[
\begin{aligned}
G_L(T;\tau,\rho)=\max\Bigg\{&
\max_{(x,z)\in Q_R}
[\|R_Tx-R_Tz\|-\sqrt{1+4\tau}\|x-z\|],\\
&\max_{x\in K}[a_T(x)-(\rho/\lambda)\Delta_T(x)]\Bigg\},\\
g_j^L(T)&=\min_{\theta\in H_j}G_L(T;\theta),
\qquad L_j=\{g_j^L\le0\}.
\end{aligned}
\tag{2.8}
\]

于是

\[
\mathcal L_{\rm pub}=\bigcup_{j\ge3}L_j
\subset\mathcal R_E
\subset\mathcal R:=\mathcal R_D\cup\mathcal R_E.
\tag{2.9}
\]

包含 (2.9) 使用 03/07 已核准的 LT→energy 转换。原 LT 的全部额外图块条件若另行要求，只会进一步缩小此公共接口类；本报告没有宣称 (2.8) 等价于每个原文 formulation 的全部假设。

## 3. 从 $F_\sigma$ 加强为对象侧 $K_\sigma$

**定理 3.1。** $D_j,E_j,L_j$ 都在单步一致／原算子 AW 图拓扑下紧。

**证明。** 所有值均在固定紧 $K$ 内。对 direct／energy 盒中的映射，当 $0<\delta=\|x-z\|\le\min\{R,1\}$ 时，

\[
\|Tx-Tz\|
\le\frac{\delta+j\delta^{1/j}}2.
\tag{3.1}
\]

这给整个盒像共同等度连续性。LT 盒同样有共同 Lipschitz 模。Arzelà–Ascoli 给相对紧性；第 2 节已证闭性，故紧。由于 (1.3) 是本图卡的同胚，原算子对象块也紧。证毕。

因此

\[
\boxed{\mathcal R_D,\ \mathcal R_E,\ \mathcal R,
\ \mathcal L_{\rm pub}\text{ 均为对象侧 }K_\sigma.}
\tag{3.2}
\]

这比仅说 analytic 或 $F_\sigma$ 更强，但它仍不是第一纲结论。其紧性来自共同函数模和固定紧域，不是证书标签空间的纲大小。

### 3.1 全轨道拓扑中的紧性也成立

每个 $D_j$ 有共同几何点尾。可取

\[
\sigma_j^D=(1-1/j)^{1/j}<1,
\qquad
\sup_{T\in D_j}\|T^n-\Pi_T\|_\infty
\le C_j^D(\sigma_j^D)^n.
\tag{3.3}
\]

常数有限，因为 $\kappa\le1-1/j$、$\gamma\ge1/j$，而 $R^\gamma,L$ 及各求和分母在紧参数盒上统一受控。

对 $E_j$，$V(R)=R^2+\lambda^2[u_{\gamma,L,q}(R)+\eta R]^2$ 在盒上有统一有限上界，故

\[
\sup_{T\in E_j}\|T^n-\Pi_T\|_\infty
\le C_j^E(\sqrt{1-1/j})^n.
\tag{3.4}
\]

LT 盒也有统一尾，因为

\[
q_{LT}^2=1+2\tau-\frac{\lambda^2}{(\lambda+\rho)^2}
\le1-\frac{\lambda^2}{j(\lambda+j)^2}<1.
\tag{3.5}
\]

同一个参数盒内，单步收敛结合共同尾即推出全时间一致轨道收敛；具体不等式见第 4 节。因此上述对象块在 $d_{\rm dyn}$ 下也紧，(3.2) 在一致点收敛的 $d_{\rm dyn}$ 图卡仍成立。

**不能反推：** 每个块内部两种拓扑相同，不表示可数并 $\mathcal R$ 上两种拓扑相同；参数预算和尾常数可能沿序列逃逸。

## 4. 先冻结中立尾层，再做两拓扑间合法转移

预先固定 $e_n\downarrow0$，定义只由实际动力学输出给出的层

\[
\begin{split}
\mathfrak D_e=\{T\in\mathcal A_S:
&\sup_{x\in K}d(T^nx,S)\le e_n,\\
&\sup_{x\in K,\,m\ge n}\|T^mx-T^nx\|\le e_n
\quad(n\ge0)\}.
\end{split}
\tag{4.1}
\]

它是 $C(K,K)$ 的闭子空间，故 Polish／Baire；自动有 $\operatorname{Fix}T=S$ 与一致极限。它未写入 RLEB、LT、Hölder 或任何预定下降律。

若 $T,U\in\mathfrak D_e$，则对任意 $N\ge0$，

\[
d_{\rm dyn}(T,U)
\le\max_{0\le k\le N}\|T^k-U^k\|_\infty+2e_N.
\tag{4.2}
\]

因为 $n\ge N$ 时，分别把 $T^n,U^n$ 与 $T^N,U^N$ 比较即可。有限次迭代对单步拓扑连续，先固定 $N$、再令 $e_N\to0$，证明

\[
\boxed{\tau_{AW}|_{\mathfrak D_e}
=\tau_\infty|_{\mathfrak D_e}
=\tau_{\rm dyn}|_{\mathfrak D_e}.}
\tag{4.3}
\]

所以在同一个 $\mathfrak D_e$ 及其同一子集上的闭包、内部、稠密性与第一纲结论可以转移。没有共同尾的整个一致收敛空间上，$d_{\rm dyn}$ 更强；不得转移。

令

\[
\mathcal R_e=\mathcal R\cap\mathfrak D_e,
\qquad
\mathcal L_e=\mathcal L_{\rm pub}\cap\mathfrak D_e.
\tag{4.4}
\]

二者都是相对 $K_\sigma$，且 $\mathcal L_e\subset\mathcal R_e$。注意 (4.4) 是“对象实际达到该尾预算，并具有某份证书”，不要求这份证书的保守尾界也逐项支配 $e_n$。若研究的是后者，应另记为性能认证类，不能把两种问题混为一谈。

## 5. LT 固定／任意步长的对象侧线性位移必要层

### 5.1 固定步长：无需解集光滑性

对固定 $s\in S$、$m,j\ge1$ 定义

\[
\mathcal C_{m,j}(s)=\left\{T\in\mathcal A_S:
\|Tx-x\|\le m\,d(x,S)
\quad\forall x\in K\cap\overline B_{1/j}(s)\right\}.
\tag{5.1}
\]

每个集合由固定输入上的连续不等式定义，故单步 AW 闭，也在更强 $d_{\rm dyn}$ 拓扑闭。

同一步长的 all-pairs RL 端点 $\gamma=1$ 比较 $x$ 与最近解 $p\in P_Sx$，给

\[
\|Tx-x\|\le\frac{1+L}{2}d(x,S).
\tag{5.2}
\]

因此固定步长的完整邻域 LT all-pairs 证书类落在

\[
\mathcal C_{\rm germ}(s)
=\bigcup_{m,j\ge1}\mathcal C_{m,j}(s).
\tag{5.3}
\]

局部图块情形，只须缩小 $x\to s$ 的邻域，使实际图点及近邻零图点均落在该图块；不可假设任意删枝后的测试集仍包含这些点。

### 5.2 RLEB 两分支都有距离非增性

Direct 已给 $d(Tx,S)\le\kappa d(x,S)$。Energy 给

\[
V(d(Tx,S))\le qV(d(x,S)),
\quad V(r)=r^2+\lambda^2\alpha(r)^2,
\quad0<q<1.
\]

$V$ 严格递增，所以两分支共同推出

\[
\boxed{d(Tx,S)\le d(x,S)\quad(T\in\mathcal R).}
\tag{5.4}
\]

这不是预加超吸引结构，而是原 RLEB 证书的内生结论。

### 5.3 任意正步长：仿射片版本

假设在 $s\in S$ 的某邻域，$S$ 与某仿射子空间 $A$ 一致。此条件包含闭凸 $S$ 的任一相对内点。设同一原算子 $F_T$ 对某 $\mu>0$，在 $(s,0)$ 的完整局部图块满足 LT all-pairs 不等式

\[
\langle u-v,a-b\rangle
\ge-\tau\|(u+a)-(v+b)\|^2,
\qquad a\in\mu F_T(u),\ b\in\mu F_T(v),
\tag{5.5}
\]

其中 $\tau\ge0$ 有限。令

\[
c=\mu/\lambda,\quad u=Tx,\quad a=c(x-u),
\quad z=u+a=cx+(1-c)u,\quad p=P_Az.
\]

当 $x\to s$ 时，各点与残差进入实际局部图块，且 $p\in S$。把 (5.5) 与 $(p,0)$ 比较，得到

\[
\|u-p\|^2+c^2\|x-u\|^2
\le(1+2\tau)d(z,S)^2.
\tag{5.6}
\]

利用局部仿射结构及 (5.4)，

\[
d(z,S)
\le c\,d(x,S)+|1-c|d(u,S)
\le(c+|1-c|)d(x,S).
\]

故

\[
\boxed{\|Tx-x\|
\le\sqrt{1+2\tau}\frac{c+|1-c|}{c}\,d(x,S)
\quad(x\text{ 充分靠近 }s).}
\tag{5.7}
\]

没有要求新步长 resolvent 全局存在、单值或 $x\mapsto z$ 可逆；只使用原完整图提供的图点及 LT 实际局部量词。

因此，定义 $\mathcal L_{\exists\mu}^{\rm geom}(s)$ 为“某正实步长下在 $(s,0)$ 有完整局部 LT all-pairs 图几何”的对象类，有

\[
\boxed{
\mathcal R\cap\mathcal L_{\exists\mu}^{\rm geom}(s)
\subset\mathcal R\cap\mathcal C_{\rm germ}(s).
}
\tag{5.8}
\]

原 LT 收敛证书类当然是左侧几何类的子类。所有实 $\mu>0$ 一起进入同一个可数闭必要层族，故不存在不可数并第一纲集合的错误，也不需要把步长谱有理化。

### 5.4 $C^1$ 流形解集版本

结论 (5.8) 可扩到 $S$ 在 $s$ 附近为 $C^1$ 嵌入流形。给出完整吸收估计。

平移旋转后，局部写成 $S=\{(\xi,f(\xi))\}$，其中 $f(0)=0,Df(0)=0$。缩小邻域可使 $\|Df\|\le\delta$，$\delta>0$ 任意小。对 $x,u=Tx$ 的近邻投影 $p,q\in S$，记

\[
a_0=d(x,S),\quad a_1=d(u,S)\le a_0,
\quad b_0=\|x-u\|.
\]

对于固定 $c>0$，足够小的局部图域包含横坐标的仿射组合。由均值估计，

\[
d(cp+(1-c)q,S)\le2c\delta\|p-q\|.
\]

于是

\[
\begin{aligned}
d(cx+(1-c)u,S)
&\le c a_0+|1-c|a_1
 +2c\delta(a_0+a_1+b_0)\\
&\le(c+|1-c|+4c\delta)a_0+2c\delta b_0.
\end{aligned}
\tag{5.9}
\]

设 $M=\sqrt{1+2\tau}$。LT 的 (5.6) 只需选 $p_z\in P_Sz$，给 $cb_0\le M d(z,S)$。选择 $\delta\le1/(4M)$ 并吸收右端 $2M\delta b_0$，得到

\[
b_0\le
\left[2M\frac{c+|1-c|}{c}+8M\delta\right]a_0.
\tag{5.10}
\]

所以同样落入 (5.3)。这是一条对象侧几何桥梁，尚无优先权判断，不应即刻称作首创。

**不外推的情形。** 任意闭／分形 $S$ 未证明 (5.9)；未含实际近邻图点的测试集合也不适用。若 $S=\{s\}$，(5.4) 自身已给 $\|Tx-x\|\le2d(x,S)$，因此整类都在 $\mathcal C_{2,j}$ 中，位移层方法不可能给严格类大小分离。非点解集与其切向结构在这里确实是数学条件，而非措辞。

## 6. 内部、闭包与第一纲的准确判据

取任何待比较对象分母 $Z\subset\mathfrak D_e$，例如 $Z=\mathfrak D_e$、$Z=\mathcal R_e$，或已后置选定的闭对象块。下面的所有拓扑均是同一相对拓扑，因 (4.3) 无 AW／动力学混用。

### 6.1 闭块的对象侧无内点等价式

对 $B\subset Z$ 相对闭，以下等价：

\[
\operatorname{Int}_Z B=\varnothing
\iff
\forall T\in B,\ \forall\varepsilon>0,
\ \exists U\in Z:\|U-T\|_\infty<\varepsilon, U\notin B.
\tag{6.1}
\]

若 $B=L_j\cap Z$，可等价写成 $g_j^L(U)>0$；若 $B=\mathcal C_{m,j}(s)\cap Z$，等价写成存在 $x\in K\cap\overline B_{1/j}(s)$ 使

\[
\|Ux-x\|>m d(x,S).
\tag{6.2}
\]

这是直接对象判据，不涉及证书空间大小。

### 6.2 闭包需要逼近所有邻域，不由参数逸出猜测

例如

\[
\overline{\mathcal L_e\cap Z}^{\,Z}=Z
\iff
\forall T\in Z,\ \forall\varepsilon>0,
\ \exists U\in Z,\ \exists j:
\|U-T\|_\infty<\varepsilon,\quad g_j^L(U)=0.
\tag{6.3}
\]

每个 $L_j\cap Z$ 闭并不意味着可数并闭，也不意味着并集稠密或无处稠密。没有对象侧逼近定理时，(6.3) 的右侧仍是未决数学问题。

### 6.3 可核准的条件性范畴定理

若对全部 $m,j$，(6.1) 对 $B=\mathcal C_{m,j}(s)\cap Z$ 成立，则这些闭块无处稠密。因而 $Z\cap\mathcal C_{\rm germ}(s)$ 在 $Z$ 中第一纲。

若同时 $Z\subset\mathcal R_e$，且 $S$ 满足第 5 节几何条件，则

\[
Z\cap\mathcal L_{\exists\mu}^{\rm geom}(s)
\text{ 在 }Z\text{ 中第一纲}.
\tag{6.4}
\]

若 $Z$ 还非空且 Baire，则其补集含稠密 $G_\delta$，才得到有通常“典型对象”含义的结论。此条件定理的证明已完成；其关键前提 (6.1) 在整个中立尾／RLEB 对象层尚未证明。

## 7. 真正欠缺的 object-side local modification lemma

欲以 $Z=\mathcal R_e$ 完成 (6.4)，精确需要下述命题。

**OLM（尚未证明）。** 固定 $K,S,e,s$。对每个 $m,j\ge1$、每个

\[
T\in\mathcal R_e\cap\mathcal C_{m,j}(s)
\]

和每个 $\varepsilon>0$，存在 $U\in C(K,K)$ 满足：

1. $U|_S=I$，且整个原算子确为 $F_U$，不能只给一条有利分支；
2. $U\in\mathfrak D_e$：同一实际尾预算对所有初值、所有后续时刻成立；
3. $U\in\mathcal R_D\cup\mathcal R_E$：允许重选有限参数，但完整 all-pairs RL、整个逆纤维的真 EB 和严格兼容全部重证；
4. $\|U-T\|_\infty<\varepsilon$；
5. 存在 $x\in K\cap\overline B_{1/j}(s)$ 使 (6.2) 成立。

由第 2、4 项与 (4.2)，这一个引理即可同时完成 AW 与 $d_{\rm dyn}$ 下的无内点，不需另造动态扰动证明。但若第 2 项只有“某个尾界”，不是同一个 $e$，便不能作此转移。

**为什么旧的尖点混合不足以证明 OLM。** 旧空间预先被做成闭凸、共同 RL／EB／法向预算层，凸混合的可行性已经是其特殊结构。当前 $\mathfrak D_e$ 的条件涉及任意长复合 $U^n$，而全纤维 EB 与 strict compatibility 也不是一般凸条件；把 $T$ 与一个坏模型线性混合，未证明以上第 2、3 项。仅在某个参数族或某个曲线方向上找到越界对象，不等于每个相对邻域中都能找到合法修改。

**可执行的分解。** 下一轮应分别攻克：

- 全纤维证书保持的局部粘合／替换定理；
- 同一中立实际尾预算保持的轨道控制引理，尤其处理预算饱和对象；
- 两者同时成立时的可局部化非线性位移插入。

需要的是上述一般引理或其失败结构定理，而不是继续生产更多孤立例子。

## 8. Baire 分母的第二个瓶颈

### 8.1 $F_\sigma$／σ紧不自动 Baire

$\mathfrak D_e$ 是 Polish，并不推出其 $F_\sigma$ 子类 $\mathcal R_e$ 是 Baire。更强地，若某空间在自身拓扑下第一纲，则它的每个子集都在其中第一纲；此时“LT 在 RLEB 中第一纲”不能说明 LT 特别小。

因此最终结论必须至少明确其中一种：

1. 已证 $\mathcal R_e$ 自身为 Baire；或
2. 在中立 Baire 分母 $\mathfrak D_e$ 中，证明 RLEB 非第一纲而 LT 第一纲；或
3. 在后置选择、明确标注的闭 Baire 对象层中作条件比较，且承认尚未得到总类判决。

### 8.2 σ紧给出的结构性诊断

若一个度量空间 $Z=\bigcup_n K_n$，各 $K_n$ 紧，而且 $Z$ 是 Baire，则

\[
\bigcup_n\operatorname{Int}_Z K_n
\quad\text{在 }Z\text{ 中开且稠密}.
\tag{8.1}
\]

证明：若某非空开集避开所有这些内部，则它被可数个相对闭无处稠密 $K_n$ 覆盖，违背 Baire。每个 $\operatorname{Int}_ZK_n$ 内的点有紧邻域，因此 σ紧 Baire 空间必须在稠密开集上局部紧。

应用于 (3.2)：若 $\mathcal R_e$ 被证明 Baire，就必须存在大量具有固定预算紧对象块邻域的成员；若反而证明其处处非局部紧，则它在自身中第一纲。这是需要实做的结构判定，不是措辞修正。

类似地，若中立 $\mathfrak D_e$ 处处非局部紧，则其每个紧子集都无内点，于是 (3.2) 立刻给 RLEB 与 LT **同时**在该中立层第一纲。这个判据成立，但本报告没有证明任意 $K,S,e$ 的 $\mathfrak D_e$ 都处处非局部紧；不同预算可产生完全不同的空间。

## 9. 审计式结论表

| 项目 | 本轮状态 | 精确边界 |
|---|---|---|
| 任意 gauge 存在量词的对象侧消去 | 已完成 | 03/07 核准的完整紧图卡，energy 为普通连续严格增 gauge |
| 对象类 $F_\sigma$ 与 $K_\sigma$ | 已证明 | direct、energy、LT 公共接口；不是任意外层原图的无条件结论 |
| AW／$d_{\rm dyn}$ 紧块 | 已证明 | 每个固定数值参数盒有共同尾 |
| 中立共同尾层两拓扑相同 | 已证明 | 固定同一个实际 $e_n$；离层不转移 |
| 任意实步长 LT→线性位移必要层 | 已证明 | RLEB 距离非增，且 $S$ 局部仿射或 $C^1$；真实完整局部图量词 |
| LT 在全部 $\mathcal R_e$ 中第一纲 | 未证明 | 欠 OLM 和有意义的 Baire 分母检查 |
| LT／RLEB 在中立母层的闭包与稠密性 | 未证明 | 欠对象侧逼近／非逼近定理 |
| 原全局图、可变域、存在实步长完整类的编码 | 此报告不承包 | 必须保留外部纤维和域边界；与步长谱模块衔接 |

**给监督者的直白结论：** 当前不缺一个用户替我们猜出的条件，缺的是可证明的对象侧局部粘合与尾预算保持定理，以及比较分母是否 Baire 的判定。可以继续建设性推进；但现有材料只支持本报告的表示、闭紧块和必要层桥梁，不支持宣布“中立体系中 LT 已第一纲”。
