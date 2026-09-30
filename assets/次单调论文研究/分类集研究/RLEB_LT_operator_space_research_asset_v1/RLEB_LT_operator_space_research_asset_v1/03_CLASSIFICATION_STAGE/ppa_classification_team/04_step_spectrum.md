# 同一算子的步长谱：完整性、认证窗口与可数闭块

日期：2026-09-20。任务范围：为中立 PPA 算子体系补上跨步长结构，不用一个尖点例子推断任何类的纲大小。本文的正结果是谱变换定理、条件性开窗口，以及保留原全图的有限参数闭块定理；负例只检验哪些一般断言不成立。

本稿已核查 `ppa_system_team/01、03、06、08、10` 的相关接口。LT 公式另与原始论文 Proposition 4、Assumption 2、Theorem 2 核对。本轮 obstruction 审计线已独立复核 §§4–5 的精确谱及 RLEB 常数、§7 的闭覆盖／全纤维 EB／紧参数投影与退化分支，未见致命错误；其提出的 energy 参数余量和 \(L=0\) 注记已补入。该复核不判定优先权，也不等同于总体 category 定理已经完成。

## 0. 结论与实际瓶颈

1. **可用步长不能当作一个数，也不能默认构成区间。** 即使光滑、半代数、单值、非点零集的算子，完整连续单值 resolvent 步长谱也可不连通，且既不开也不闭。
2. **严格局部 LT 证书不自动给开放步长窗口。** 远处图支可在改步长后进入同一个小输入域；有闭图、半代数例子的局部 LT、direct-RLEB、energy-RLEB 谱恰为一个指定的无理数。更一般，任意非空紧集 \(A\Subset(1,\infty)\) 都可精确实现为这三种谱及完整良定／全选择收敛谱。因此不能无条件以有理步长代替实步长。
3. **完整严格 RLEB 也不自动给开放的单值步长谱。** §5 的完整全局、三值、半代数算子在基准步长满足严格 direct 和 energy 证书，但全域连续单值谱为单点。其所有正步长的完整多值 PPA 却都逐轨道有限长收敛：良定单值谱、所有选择的收敛谱和 all-pairs 认证谱确实不同。
4. **不可数步长不必成为描述集合障碍。** §7 证明：固定解锚点、开工作域和真实输出 EB 域时，完整覆盖、全图 all-pairs 模和真实 EB 在紧参数盒内给闭证书块。步长本身也放进紧盒，投影后仍闭。因此适当定义的局部 germ LT/direct/energy 认证类，以及它们的联合步长图，均可表示为 \(F_\sigma\)，不需要谱开性或有理步长化。
5. **还未解决的是相对纲，而不是“能否定义比较类”。** 闭块表示只把下一步精确缩成：在冻结的中立分母中，逐一判定这些对象侧闭块有没有相对内点。本文不证明它们无处稠密。

## 1. 五种谱与两个必须分开的量词

首先固定有限维状态空间 \(E=\mathbb R^d\)、原闭图 \(F\)、目标零集 \(S=\operatorname{zer}F\)，必要时再固定 \(s\in S\)。始终使用完整关系

\[
J_{\lambda F}=(I+\lambda F)^{-1}.
\]

### 1.1 全域谱

\[
\begin{aligned}
\mathcal W^{\rm gl}(F)
&=\{\lambda>0:J_{\lambda F}:E\to E\text{ 完整、全域、单值、连续}\},\\
\mathcal C^{\rm sv}(F)
&=\{\lambda\in\mathcal W^{\rm gl}(F):
 J_{\lambda F}^{\,n}x\text{ 对每个 }x\text{ 收敛到 }S\},\\
\mathcal C^{\rm all}(F)
&=\{\lambda>0:\text{完整 PPA 非阻塞，且每个初值的每条完整轨道收敛到 }S\}.
\end{aligned}
\tag{1.1}
\]

\(\mathcal C^{\rm all}\) 不要求单值，故不应塞进 \(\mathcal W^{\rm gl}\)。单值条件成立时两种收敛量词一致。

### 1.2 局部谱

固定开输入域 \(U\) 时记 \(\mathcal W_U(F)\)。固定 \(s\) 的 germ 谱为

\[
\mathcal W_s(F)=\{\lambda>0:\exists a>0,
 J_{\lambda F}|_{B_a(s)}\text{ 完整、单值、连续}\}.
\tag{1.2}
\]

\(\mathcal C_s^{\rm sv},\mathcal C_s^{\rm all}\) 还须明列一个共同初值邻域和合法轨道包络；不能把“在某邻域有一个局部分支”换成完整 PPA。

认证谱记为

\[
\mathcal L_s(F),\quad
\mathcal R_{D,s}(F),\quad
\mathcal R_{E,s}(F).
\tag{1.3}
\]

本文的 \(\mathcal L_s\) 是 LT2025 **all-pairs 公共定量证书在完整接口中的像**：完整覆盖、反射 Lipschitz、真实线性输出 EB、严格数值门槛和局部留域。它不是把 LT 原定理的截断分支结论无条件升格成原全图结论，也不是全部较早的 pointwise LTT 类。

在允许缩小 germ、使用同一完整图与真实 EB 的口径下，已有转换给

\[
\mathcal L_s(F)\subseteq\mathcal R_{E,s}(F),
\qquad
\mathcal R_{D,s}(F)\cup\mathcal R_{E,s}(F)
\subseteq\mathcal C_{s,\rm lu}^{\rm sv}(F)
\subseteq\mathcal W_s(F).
\tag{1.4}
\]

若固定一份不可缩小的初值域或尾预算，(1.4) 不能省去对应的域／预算转换证明。

## 2. 谱是同一闭图的剪切可逆性谱

### 定理 2.1：精确换步长

设 \(\lambda\in\mathcal W^{\rm gl}(F)\)，\(T=J_{\lambda F}\)，\(c=\mu/\lambda>0\)，令

\[
H_c=cI+(1-c)T.
\tag{2.1}
\]

则

\[
J_{\mu F}(z)=\{Tx:H_cx=z\}.
\tag{2.2}
\]

因此：输入全覆盖等价于 \(H_c\) 满射；完整单值等价于 \(H_c\) 单射；完整、全域、单值、连续等价于 \(H_c\) 是同胚。成立时

\[
T_\mu=T\circ H_c^{-1},\qquad
H_c^{-1}z=c^{-1}\{z-(1-c)T_\mu z\}.
\tag{2.3}
\]

**证明。** 若 \(u=Tx\)，则 \((x-u)/\lambda\in F(u)\)，同一图点在步长 \(\mu\) 的输入为 \(z=u+\mu(x-u)/\lambda=H_cx\)。逆向相同。若 \(H_cx_1=H_cx_2\) 且 \(Tx_1=Tx_2\)，则 \(c(x_1-x_2)=0\)，所以非单射必产生两个不同输出。连续逆由 (2.3) 给出；反向由复合连续性给出。证毕。

这一定理在 Hilbert 空间同样成立；有限维还可用 invariance of domain 将连续双射直接升级为同胚。

### 2.2 反射坐标的分式变换

令 \(R=2T-I\)，\(a_c=(1+c)/2\)、\(b_c=(1-c)/2\)，则

\[
H_c=a_cI+b_cR,
\qquad
R_\mu=(b_cI+a_cR)\circ(a_cI+b_cR)^{-1}.
\tag{2.4}
\]

这是同一原算子的坐标变换，不是任意指定的映射族。一般多值 \(T\) 不允许把 (2.2) 写成丢失同一输出耦合的普通关系复合；必须回到完整图剪切。

## 3. 正的局部结构定理：什么时候真的有步长窗口

### 定理 3.1：全局反射 Lipschitz 窗口

设 \(T=J_{\lambda F}\) 完整全域，\(R=2T-I\) 为 \(L\)-Lipschitz。若

\[
m_c:=a_c-|b_c|L>0,
\tag{3.1}
\]

则 \(\mu=c\lambda\in\mathcal W^{\rm gl}(F)\)，且

\[
\operatorname{Lip}(H_c^{-1})\le m_c^{-1},
\qquad
\operatorname{Lip}(R_\mu)
\le L_c:=\frac{|b_c|+a_cL}{a_c-|b_c|L}.
\tag{3.2}
\]

**证明。** 三角不等式给 \(\|H_cx-H_cy\|\ge m_c\|x-y\|\)。对任意 \(z\)，方程 \(H_cx=z\) 等价于
\(x=a_c^{-1}(z-b_cRx)\)，右边的 Lipschitz 常数为 \(|b_c|L/a_c<1\)，故 Banach 不动点定理给唯一解。再用 (2.4) 得反射估计。证毕。

若 \(L>1\)，窗口可明确写为

\[
\frac{L-1}{L+1}<\frac\mu\lambda<\frac{L+1}{L-1};
\tag{3.3}
\]

\(L\le1\) 时 (3.1) 对全部 \(c>0\) 成立。此处是**良定及有限 Lipschitz**窗口，不是自动的收敛窗口。

如果旧证书具有真实线性 EB 常数 \(\rho\)、LT 常数
\(\tau=(\max\{1,L^2\}-1)/4\)，且

\[
2\tau(\lambda+\rho)^2<\lambda^2,
\tag{3.4}
\]

那么令 \(\tau_c=(\max\{1,L_c^2\}-1)/4\)。由 \(L_c\to L\)，(3.4) 在 \(c=1\) 附近保持严格。只要同一真实 EB 输出域和完整性接口仍适用，就得到 LT 认证开窗口和共同的小吸引邻域。

在全域线性 EB 的情形这些接口自动保持；在局部情形它们是下一条定理的实质假设。

### 定理 3.2：受保护局部图表中的窗口

设 \(s\in S\)，完整 \(T=J_{\lambda F}\) 在 \(B_r(s)\) 上为 \(K\)-Lipschitz。另设存在 \(\eta>0,r_0>0\) 与紧集 \(Q\)，使

\[
J_{\mu F}(z)\subseteq Q
\quad\bigl(|\mu-\lambda|<\eta,\ z\in B_{r_0}(s)\bigr).
\tag{3.5}
\]

允许某些集合为空；(3.5) 是对**所有**完整输出的共同有界性，而不是选中分支的有界性。则缩小 \(r_0,\eta\) 后，所有这些完整输出均由 \(B_r(s)\) 中的旧 Minty 输入表示，且在某个共同内球上 \(J_{\mu F}\) 完整单值 Lipschitz，(3.2) 的局部版本成立。

**证明关键。**

1. 若有 \(\mu_n\to\lambda,z_n\to s,u_n\in J_{\mu_nF}(z_n)\) 逃离 \(s\) 的一个固定邻域，(3.5) 让 \(u_n\) 有收敛子列。闭图推出其极限属于完整 \(J_{\lambda F}(s)=\{s\}\)，矛盾。
2. 同一图点的旧输入
   \(x_n=u_n+\lambda(z_n-u_n)/\mu_n\) 也趋于 \(s\)，因此所有新输出的旧输入最终都在 \(B_r(s)\)。没有隐匿域外分支。
3. 对 \(c\) 近 1，解 \(x=c^{-1}[z-(1-c)Tx]\)。取闭球 \(\overline B_{r'}(s)\Subset B_r(s)\)，\(T(s)=s\)，并令
   \(\|z-s\|+|1-c|Kr'<cr'\)。该压缩映射把闭球送入自身，给存在和唯一的局部输出；第 2 步升级为完整唯一性。

线性 EB 若在一个含 \(s\) 的开输出域上成立，缩域后同样适用。LT 的严格标量门槛因参数连续而保留。故有理步长替代实步长只在这种已证明开放性的谱内合法。

### 3.3 一个一般光滑局部判据

若 \(F=f\) 在 \(s\) 附近单值 \(C^1\)，\(f(s)=0\)，且完整图满足上述 no-escape 条件，则

\[
\det(I+\lambda Df(s))\ne0
\tag{3.6}
\]

给一个 \(C^1\) 完整局部 resolvent 图表。若进一步

\[
\rho\big((I+\lambda Df(s))^{-1}\big)<1,
\tag{3.7}
\]

则某个共同内邻域内逐轨道指数收敛到 \(s\)，该结论对 \(\lambda\) 在一个小窗口内一致成立。

证明由参数化逆函数定理，加上在等价向量范数中把严格稳定线性化变成压缩，再用导数连续性给局部压缩；等价范数只用于证明，结论仍是原欧氏范数的指数收敛。这里未主张把这种换范数变成新的 RLEB/LT 证书。

若 \(A=Df(s)\) 可逆，(3.7) 等价于

\[
2\operatorname{Re}z+\lambda|z|^2>0
\quad(z\in\sigma(A)),
\tag{3.8}
\]

所以线性化给一条可计算的稳定射线。这是一般非线性局部定理，不是只算标量线性算例。非点固定流形的中性切向方向不能直接套 (3.7)，需要正常吸引的单独版本。

## 4. 光滑半代数校准：良定谱不连通，收敛边界可被包含

取 \(0<\varepsilon<1\)，在 \(\mathbb R^2\) 上令

\[
F(p,r)=\left(0,-2r+\frac{\varepsilon r}{\sqrt{1+r^2}}\right),
\qquad S=\mathbb R\times\{0\}.
\tag{4.1}
\]

这是光滑、单值、闭图、半代数算子。记 \(a=2-\varepsilon\)。法向 Minty 映射为

\[
A_\lambda(r)=(1-2\lambda)r+
\frac{\lambda\varepsilon r}{\sqrt{1+r^2}},
\quad
A_\lambda'(r)=1-2\lambda+
\frac{\lambda\varepsilon}{(1+r^2)^{3/2}}.
\tag{4.2}
\]

因此精确地

\[
\boxed{\mathcal W^{\rm gl}(F)
=(0,1/2)\ \cup\ [1/a,\infty).}
\tag{4.3}
\]

- \(0<\lambda<1/2\)：严格递增、满射。
- \(\lambda=1/2\)：有界值域，不满射。
- \(1/2<\lambda<1/a\)：导数变号，不单射。
- \(\lambda=1/a\)：除零点外导数严格负，仍严格递减满射；逆函数在零点为三分之一次量级，非 Lipschitz。
- \(\lambda>1/a\)：严格递减、双 Lipschitz。

所以此谱既不开、也不闭、也不是区间。

完整单值 PPA 的全初值收敛谱是

\[
\boxed{\mathcal C^{\rm sv}(F)=[2/a,\infty).}
\tag{4.4}
\]

证明：在上方良定支，法向幅值由递增函数

\[
M_\lambda(r)=(2\lambda-1)r-
\frac{\lambda\varepsilon r}{\sqrt{1+r^2}},\qquad r\ge0
\]

的逆更新。\(\lambda\ge2/a\) 时 \(M_\lambda(r)>r\) 对 \(r>0\) 成立，故幅值单调降到零；边界 \(\lambda=2/a\) 也成立。若 \(1<\lambda<2/a\)，存在 \(r_*>0\) 使 \(M_\lambda(r_*)=r_*\)，产生法向二周期。若上方良定支中 \(\lambda\le1\)，则 \(M_\lambda(r)<r\)，幅值发散。下方良定支的逆映射同样严格扩张非零幅值。证毕。

在 \(s=(p,0)\) 处，严格 direct 和 energy 公共证书谱均恰为

\[
\boxed{\mathcal R_{D,s}(F)=\mathcal R_{E,s}(F)=(2/a,\infty).}
\tag{4.5}
\]

对 \(z=\lambda a>2\)，真实 EB 最佳局部常数为 \(\rho=1/a\)，完整反射 Lipschitz 常数可取

\[
L=\frac{z+1}{z-1}.
\]

direct 因子为 \(1/(z-1)<1\)，energy 因子为 \(1/(z-1)^2<1\)。在边界 \(z=2\)，法向导数为 \(-1\)，非零小轨道的点误差比趋于 1，故其误差的 \(n\) 次根趋于 1；不能有严格 RLEB 证书所推出的局部几何点尾，故边界不属于这两个谱。

若采用 (3.4) 的 LT 公共门槛，则其精确局部认证谱为

\[
\mathcal L_s(F)=(z_*/a,\infty),
\quad z_*>3\text{ 是 }z^3-4z^2-3z-2=0\text{ 的唯一正根}.
\tag{4.6}
\]

因为最小 \(\tau=z/(z-1)^2\)，将最佳局部 \(\rho\) 代入 (3.4) 正好得到该多项式不等式。此处只是可核的性能谱校准，不据它判定总体类的大小。

## 5. 严格完整 RLEB 仍可只有一个单值步长

这条反例排除“加上真实 EB 和严格兼容，纯 Hölder 的换步长困难就会消失”的猜测；不是用来替代总体分类。

令

\[
h(p)=\min\{\sqrt{|p|},1\},\qquad q=1/100,
\]
\[
T(p,r)=\bigl(p+\sqrt{|r|}(1+h(p)),qr\bigr),
\qquad F=T^{-1}-I.
\tag{5.1}
\]

\(T\) 是全空间连续、满射、半代数映射，故 \(F\) 闭图、半代数，且完整 \(J_F=T\)。其值数至多为三，不冒称二值。零集精确为 \(S=\mathbb R\times\{0\}\)。

### 5.1 独立 all-pairs 与真实 EB 核验

在工作条带 \(|r|\le1\) 中，对 \(\delta=\|(p,r)-(p',r')\|\le1\)，令 \(f(p,r)=\sqrt{|r|}(1+h(p))\)。利用 \(h\) 的 \(1/2\)-Hölder 常数 1，

\[
|f(p,r)-f(p',r')|
\le2\sqrt{|r-r'|}+\sqrt{|r'|}\sqrt{|p-p'|}
\le3\sqrt\delta.
\]

\(R_T=(p+2f,(2q-1)r)\)，而 \(\|\operatorname{diag}(1,2q-1)\|=1\)，故

\[
\|R_Tx-R_Ty\|\le\delta+6\sqrt\delta\le7\sqrt\delta.
\tag{5.2}
\]

这是真正跨所有输入对的 RL：\(\gamma=1/2,L=7\)。

对任意输出 \(u=T(p,r)\)，每条逆纤维的法向输入都满足 \(u_r=qr\)，且其残差第一坐标的绝对值至少 \(\sqrt{|r|}\)。所以对**整个多值算子的最小范数**有

\[
d(u,S)=q|r|\le q\,r_F(u)^2.
\tag{5.3}
\]

取 \(\psi(t)=qt^2\)，则对 \(0<d\le1\)，

\[
\psi\left(\frac{d+7\sqrt d}{2}\right)
=\frac q4d(\sqrt d+7)^2\le16q\,d=\frac4{25}d.
\tag{5.4}
\]

direct 严格兼容成立。energy 同样成立：

\[
V(d)=d^2+100d,\quad A(d)=\frac{d^2+49d}{2},
\quad\sup_{0<d\le1}\frac{A(d)}{V(d)}=\frac{25}{101}<1.
\tag{5.5}
\]

条带在 \(T\) 下前向不变；完整性来自全局逆图定义，不存在选中分支替代问题。

### 5.2 单值步长谱恰为单点

令 \(c=\mu>0\)。同一 \(F\) 的换步长映射为

\[
H_c(p,r)=\bigl(p+(1-c)\sqrt{|r|}(1+h(p)),
 [q+c(1-q)]r\bigr).
\tag{5.6}
\]

法向系数始终正。固定 \(r\ne0\)，若 \(c\ne1\)，切向函数为
\(g_b(p)=p+b(1+h(p))\)，\(b\ne0\)。它在 \(|p|>1\) 处斜率为 1，但若 \(b>0\) 则在 \(0^-\) 导数趋于 \(-\infty\)，若 \(b<0\) 则在 \(0^+\) 导数趋于 \(-\infty\)。连续实函数单射必须严格单调，故 \(g_b\) 不单射。于是

\[
\boxed{\mathcal W^{\rm gl}(F)=\{1\}.}
\tag{5.7}
\]

这些折返点随 \(r\to0\) 向 \((0,0)\) 聚集，所以固定 \(s=(0,0)\) 时还有

\[
\mathcal W_s(F)=\mathcal R_{D,s}(F)
=\mathcal R_{E,s}(F)=\{1\},\qquad\mathcal L_s(F)=\varnothing.
\tag{5.8}
\]

最后一式：在 \(\mu\ne1\) 时完整关系已经局部多值；在 \(\mu=1\) 时 \(T\) 在任意含 \((0,0)\) 的完整邻域上都不是 Lipschitz。

### 5.3 然而所有正步长的所有完整轨道都收敛

记 \(k_\mu=q+\mu(1-q)>0\)、\(q_\mu=q/k_\mu\in(0,1)\)。对每个完整 proximal 输出，法向更新唯一为

\[
r^+=q_\mu r,
\]

切向增量满足

\[
0\le p^+-p\le\frac{2\mu}{\sqrt{k_\mu}}\sqrt{|r|}.
\tag{5.9}
\]

每个输入均有输出：\(g_b\) 是连续满射，虽然通常不单射。因此任意选择下

\[
\sum_n|p_{n+1}-p_n|
\le\frac{2\mu\sqrt{|r_0|}}
{\sqrt{k_\mu}(1-\sqrt{q_\mu})}<\infty.
\tag{5.10}
\]

法向也有限长并趋零，故

\[
\boxed{\mathcal C^{\rm all}(F)=(0,\infty).}
\tag{5.11}
\]

这一结构同时显示：某个认证谱狭窄，不等于算法实际收敛谱狭窄；改步长后单值性丢失，也不等于所有轨道失去收敛。

## 6. 局部严格 LT 谱也可能是无理单点：远支侵入

本例由本轮 obstruction 审计线提供，本文独立核查其完整图和轨道量词。

取 \(\lambda_0=\sqrt2,C=4\)，定义一维闭图

\[
G=\{(u,u):u\in\mathbb R\}
\ \cup\
\left\{\left(
\frac{Ct(1+t)}{|t-\lambda_0|},
-\frac{C(1+t)}{|t-\lambda_0|}\right):
t>0,\ t\ne\lambda_0\right\}
\ \cup\ \{(0,-C/\lambda_0)\}.
\tag{6.1}
\]

唯一有限参数端点是 \(t\downarrow0\)，已补入；\(t\to\lambda_0\) 或 \(t\to\infty\) 时图点范数发散。故图闭，且为半代数集。零点集为 \(\{0\}\)。所有额外残差值的模至少 \(C/\lambda_0>1\)，故在 \(|u|\le1\) 上

\[
r_G(u)=|u|.
\tag{6.2}
\]

在步长 \(\lambda_0\)，额外图点的 Minty 输入为

\[
u+\lambda_0v=\pm C(1+t),
\]

不进入 \((-1,1)\)。因此完整

\[
J_{\lambda_0G}(x)=\frac{x}{1+\lambda_0}\qquad(|x|<1).
\tag{6.3}
\]

将自由切向维乘进去：\(F(p,u)=\{0\}\times G(u)\)，零集便为非点直线 \(S=\mathbb R\times\{0\}\)。同一局部域上 LT 可取 \(\tau=0,\rho=1\)，direct 可取 \(\gamma=1,L=1,\kappa=1/\sqrt2\)，energy 可取因子 \(1/3\)。所有都是严格证书。

但对任意 \(\mu>0,\mu\ne\lambda_0\)，在额外图中令 \(t=\mu\)，便有 \(u+\mu v=0\)、\(u>0\)。所以 \(J_{\mu F}(0)\) 同时含基线零输出和非零输出；在 \(s=(0,0)\) 的任何完整输入邻域均非单值。因此

\[
\boxed{\mathcal W_s(F)=\mathcal L_s(F)
=\mathcal R_{D,s}(F)=\mathcal R_{E,s}(F)=\{\sqrt2\}.}
\tag{6.4}
\]

此外，\(\mu\ne\lambda_0\) 时所有轨道收敛也失败。额外图在步长 \(\mu\) 的输入函数

\[
z_\mu(t)=\frac{C(1+t)(t-\mu)}{|t-\lambda_0|}
\]

满足 \(z_\mu(\mu)=0\)、\(z_\mu'(\mu)=C(1+\mu)/|\mu-\lambda_0|>0\)。故每个足够小的正输入都有一个接近固定正数 \(Y_\mu\) 的远输出。反复使用基线压缩 \(x\mapsto x/(1+\mu)\) 降回小区，再选择远输出，可得在小值与至少 \(Y_\mu/2\) 间反复跳动的不收敛轨道。

这个例子精确说明：若没有 (3.5)，局部严格证书本身不足以证明步长开放，更不能把 \(\exists\mu>0\) 改成 \(\exists\mu\in\mathbb Q_+\)。

### 6.1 更强的精确实现：任意非空紧步长集

给定非空紧集 \(A\subset(0,\infty)\)，记 \(a_-=\min A,a_+=\max A\)，取 \(C>\max\{1,a_+\}\)。将 (6.1) 的额外图换为

\[
\left\{\left(
\frac{Ct(1+t)}{d(t,A)},-
\frac{C(1+t)}{d(t,A)}\right):t>0,\ t\notin A\right\}
\ \cup\ \{(0,-C/a_-)\},
\tag{6.5}
\]

并保留整条基线 \((u,u)\)。再乘自由切向维，得 \(F_A\) 与固定非点零集 \(S=\mathbb R\times\{0\}\)。该推广由 obstruction 审计线提出，以下为本模块独立核验。

1. **闭图。** \(t\to A\) 时额外残差模发散；\(t\to\infty\) 时输出坐标发散；\(t\downarrow0\) 的唯一有限端点已补入。因此没有遗漏有限图极限。
2. **真实 EB。** \(d(t,A)\le t+a_+\le\max\{1,a_+\}(1+t)\)，故额外残差模均大于 1；补入端点亦然。于是 \(|u|\le1\) 上真实最小残差仍为 \(|u|\)。
3. **精确良定谱。** 若 \(\lambda\in A\)，则额外图的输入模
   \[
   |u+\lambda v|
   =\frac{C(1+t)|t-\lambda|}{d(t,A)}\ge C>1.
   \]
   故 \((-1,1)\) 上完整 resolvent 仍是 \(x/(1+\lambda)\)。若 \(\mu\notin A\)，令 \(t=\mu\) 即在输入 0 产生额外非零输出。
4. **精确全选择收敛谱。** \(\lambda\in A\) 时小输入唯一地沿基线压缩；\(\mu\notin A\) 时
   \[
   z_\mu(t)=\frac{C(1+t)(t-\mu)}{d(t,A)}
   \]
   连续，且在 \(t=\mu\) 处有正的差商极限 \(C(1+\mu)/d(\mu,A)\)。介值定理保证所有足够小正输入都有接近固定 \(Y_\mu>0\) 的远输出，重复上一段的降回—远跳构造得到不收敛轨道。此处只需介值性质，不要求距离函数处处可微。
5. **证书。** \(\lambda\in A\) 时 \(\tau=0,\rho=1,L=1\)；energy 因子 \(1/(1+\lambda^2)<1\)。direct 最佳线性因子为 \(1/\lambda\)，故恰在 \(\lambda>1\) 时严格。\(\gamma<1\) 不能救回其余步长，因为法向原图在零点附近具有真实线性残差阶，而切向恒等强制 \(L>0\)，direct 商随 \(r^{\gamma-1}\) 发散。

所以在 \(s=(0,0)\) 处，精确地

\[
\boxed{
\mathcal W_s(F_A)=\mathcal L_s(F_A)=\mathcal R_{E,s}(F_A)
=\mathcal C_s^{\rm all}(F_A)=A,
\qquad
\mathcal R_{D,s}(F_A)=A\cap(1,\infty).
}
\tag{6.6}
\]

特别地，\(A\Subset(1,\infty)\) 时五谱全等于 \(A\)。它可以是无内点 Cantor 紧集，不能以开区间谱的语言穷尽。

对任意紧 \(A\) 这里只声称闭图；当 \(A\) 本身半代数时，距离函数及所构造的图才可相应断言半代数。不能把 Cantor 版冒称为半代数反例。

## 7. 构建性修复：完整原图的紧证书投影

### 7.1 一个通用闭块引理

本节固定非空闭目标集 \(S\) 和锚点 \(s\in S\)，不令 \(S\) 随原图无控制地变化。令 \(\mathfrak X_s\) 为所有含 \((s,0)\) 的非空闭图，配有限维 AW 拓扑；比较真实零集时再限制到 \(\operatorname{zer}F=S\) 的原图子空间。固定开球

\[
U=B_a(s),\quad V=B_b(s),\qquad a,b>0,
\]

以及紧参数集 \(K\)。参数含

\[
0<\lambda_-\le\lambda\le\lambda_+,
\quad0<\gamma_-\le\gamma\le1,
\quad0\le L\le L_+,
\tag{7.1}
\]

以及连续依赖参数的有限个 EB／兼容参数。令证书谓词包括：

1. \(U\subseteq\operatorname{ran}(I+\lambda F)\)，即原全图的完整覆盖；
2. 对原图每一对 \((u,v),(u',v')\)，只要 \(x=u+\lambda v\in U\)、\(x'=u'+\lambda v'\in U\)，便有
   \[
   \|(u-\lambda v)-(u'-\lambda v')\|
   \le L\|x-x'\|^\gamma;
   \tag{7.2}
   \]
3. 在整个开输出域 \(V\) 内，对**原图全部** \((u,v)\) 测试真实 EB，例如
   \[
   d(u,S)\le\psi_\theta(\|v\|)
   \quad\text{或}\quad
   \alpha_\theta(d(u,S))\le\|v\|,
   \tag{7.3}
   \]
   其中相应函数对有限参数与自变量联合连续；
4. 连续的非严格参数约束，编码严格门槛的统一余量，并要求
   \[
   B_\theta(a):=\tfrac12(a+La^\gamma)\le b-\eta,
   \qquad\eta>0\text{ 固定}.
   \tag{7.4}
   \]

**定理 7.1。** 满足以上条件的 \((F,\theta)\in\mathfrak X_s\times K\) 构成闭集，其到原算子 \(F\) 坐标的投影亦闭。

**证明。** 设 \((F_n,\theta_n)\to(F,\theta)\)。

- 对任意固定的两个极限图点，AW 的内极限给近似图点；其 Minty 输入收敛，因 \(U\) 开，最终仍属于 \(U\)。故 (7.2) 通过极限。取相同输入立即得到完整输出唯一。
- 对任意固定 \(x\in U\)，完整覆盖给 \(u_n\in J_{\lambda_nF_n}(x)\)。与锚点 \((s,0)\) 比较 (7.2)，得
  \[
  \|u_n-s\|\le\tfrac12(\|x-s\|+L_n\|x-s\|^{\gamma_n})
  \le\sup_KB_\theta(a)<\infty.
  \]
  \(\lambda_n\ge\lambda_->0\) 又给 \(v_n=(x-u_n)/\lambda_n\) 有界。有限维中取收敛子列，AW 外极限给 \((u,v)\in F\) 且 \(x=u+\lambda v\)，故覆盖保留。
- 对任何极限图点 \((u,v)\) 且 \(u\in V\)，近似图点的输出最终仍在开集 \(V\)，由联合连续性保留 (7.3)。这一量词没有删去任何域外逆纤维。
- 参数约束闭；(7.4) 保证覆盖输出落入 EB 开域。由 (7.2) 得到连续唯一完整 resolvent。
- 最后参数集紧：若投影中的 \(F_n\to F\)，任选其证书参数并取收敛子列，闭性给 \(F\) 仍在投影中。

证毕。该证明没有假设同一个 \(F\) 在临近步长也良定；它与 §6 的 singleton 谱完全相容。

**尺度边界。** 若原 RL 只在输入差 \(\le R_0\) 时成立，先选 \(2a<R_0\)。这样所有被测试输入对都在严格内尺度，不会在 AW 近似时越过距离边界。

### 7.2 LT：实步长直接作为紧见证

取 \(\gamma=1,L=\sqrt{1+4\tau}\)，EB 为 \(d(u,S)\le\rho\|v\|\)。将

\[
\lambda\in[1/m,m],\quad
\tau\in[0,m],\quad \rho\in[1/m,m],
\]

以及

\[
2\tau(\lambda+\rho)^2\le(1-1/n)\lambda^2
\tag{7.5}
\]

放入紧参数块，工作球、输出球和留域内球按有理半径穷尽。若原 \(\rho=0\)，可利用严格余量放大为小的正 \(\rho\)，或单列一步终止块。

由定理 7.1，每个对象投影块闭。于是固定锚点的完整 LT 公共 germ 类

\[
\{F:\mathcal L_s(F)\ne\varnothing\}
\quad\text{是 }F_\sigma.
\tag{7.6}
\]

保留 \(\lambda\) 坐标，仅投影其余参数，同样得到

\[
\{(F,\lambda):\lambda\in\mathcal L_s(F)\}
\quad\text{是 }F_\sigma.
\tag{7.7}
\]

这里保留无理临界步长；不是以有限或有理采样近似存在量词。

### 7.3 Direct：规范 gauge 在整个开 EB 域上的修补

已有规范化令

\[
h_\theta(r)=\frac{r+Lr^\gamma}{2\lambda},\qquad
\widehat\psi_\theta(t)=\kappa h_\theta^{-1}(t).
\tag{7.8}
\]

原条件 \(\psi(h_\theta(r))\le\kappa r\) 在 \(0\le r\le R\) 上给
\(\psi(t)\le\widehat\psi(t)\) 仅在 \(t\le h_\theta(R)\) 上成立。不能忽略这个范围，直接宣称全输出域 EB 已规范化。

**补强引理。** 若把开输出球选得 \(b\le\kappa R\)，则 (7.8) 在整个 \(V=B_b(s)\) 上保留原真实 EB。

证明：小残差 \(t\le h(R)\) 时由上述支配；大残差时
\(\widehat\psi(t)\ge\kappa R\ge b>d(u,S)\)。因此对 \(V\) 中原图每个值都成立；规范 gauge 连续，取全纤维下确界即可得到真实最小残差 EB。证毕。

任一已有局部 direct 证书都可先取 \(R<R_0\)，再缩 \(V\)，最后缩工作球 \(U\)，使

\[
B_\theta(a)<b<\kappa R,
\quad2a<R_0.
\tag{7.9}
\]

缩域合法性来自完整连续 resolvent 在固定解点的连续性，以及原留域预算的小初值版本；没有改动原 \(F\)。所以这不是仅保留实际输出的弱替代，而是完整原图 germ 的等价规范化。

在 \(\lambda,\gamma,L,\kappa\) 的紧盒（\(\gamma\ge1/m\)、\(\kappa\in[1/m,1-1/m]\)）中，\(h^{-1}\) 对参数与自变量联合连续。用 (7.8) 作为 (7.3)，定理 7.1 遂给

\[
\{F:\mathcal R_{D,s}(F)\ne\varnothing\},
\qquad
\{(F,\lambda):\lambda\in\mathcal R_{D,s}(F)\}
\quad\text{均为 }F_\sigma.
\tag{7.10}
\]

严格兼容由 \(\widehat\psi(h(r))=\kappa r\) 自动保留。这个结论是 germ 口径，不承诺原来那份大初值域或最优因子不变。

### 7.4 Energy：有限参数逆 gauge 的完整图版本

调用上一轮已复核的有限参数规范化：

\[
A(r)=\tfrac12(r^2+L^2r^{2\gamma}),\qquad
g_q(r)=\lambda^{-1}\sqrt{[A(r)/q-r^2]_+},
\]
\[
\widehat\alpha(r)=\max_{0\le t\le r}g_q(t)+\eta r,
\qquad0<q<1,\quad\eta>0.
\tag{7.11}
\]

这里原 energy 因子记为 \(q_0\)，规范化一般须放松为 \(q_0<q<1\)，不能宣称保留原最优因子。若 \(L=0\) 而原来选了 \(\gamma<1\)，先无损改取 \(\gamma=1\)：RL 几何仍是零反射模，\(A(r)=r^2/2\) 完全未变。规范化在某个 \([0,R]\) 上满足 \(\widehat\alpha\le\alpha\)，且自动给

\[
A(r)\le q\{r^2+\lambda^2\widehat\alpha(r)^2\}.
\tag{7.12}
\]

取开输出球 \(b<R\)。原 EB 于是对 \(V\) 中**全部图点**推出
\(\widehat\alpha(d(u,S))\le\|v\|\)，不需截取逆纤维。若规范化的特殊 \(L<1,\gamma=1\) 分支使用了线性逆 gauge，可直接把那一有限参数分支并入，而不假设其估计在非实际输出上自动成立。

对特殊分支的完整原图补强如下：缩 \(V\) 使 \(u\in V\)、\(\|v\|\) 足够小时 \(x=u+\lambda v\in U\)。\(T\) 在 \(U\) 为严格压缩，故其在 \(U\) 的唯一固定点为 \(s\)，并有
\(\|u-s\|\le K\|x-s\|\le K(\|u-s\|+\lambda\|v\|)\)，其中 \(K=(1+L)/2<1\)。因此小残差图点满足
\(\|v\|\ge(1-K)\|u-s\|/(K\lambda)\)；这里 \(K\ge1/2\)，没有除零问题。大残差可通过进一步缩 \(V\) 被一个足够小正的线性逆 gauge 控制。于是整个 \(V\) 上存在 \(\eta_0d(u,S)\le\|v\|\)，而 \(A(r)<r^2\) 已给严格 energy 门槛。该分支同样可用有限参数完整图块编码。

在 \(\lambda,\gamma,L,q,\eta\) 的紧盒内，(7.11) 的 running maximum 联合连续：把 \(t=rz\)、\(z\in[0,1]\)，在固定紧集上使用一致连续性即可。于是同样有

\[
\{F:\mathcal R_{E,s}(F)\ne\varnothing\},
\qquad
\{(F,\lambda):\lambda\in\mathcal R_{E,s}(F)\}
\quad\text{为 }F_\sigma.
\tag{7.13}
\]

这里假设原 energy gauge 是其已有定理所用的普通连续严格增 gauge；未把更一般不连续广义逆函数无证明并入。

### 7.5 这比“有理步长化”更弱、更可靠

紧参数投影不要求 \(\mathcal L_s(F)\) 非空时含区间，不要求 \(F\) 满足参数邻域 no-escape，也不重新标记算子。它直接计数原 \(F\)，并保留所有实步长见证。

但若要求在**每个**解点、整个非紧解集、固定大吸引域、同一尾预算下同时认证，必须重新写量词。上述固定锚点 germ 的 \(F_\sigma\) 不可无条件升级为这些更强类；可数穷尽后通常只先得到较高阶 Borel 编码。

## 8. 其他谱的可描述性与真正的 category 承重点

### 8.1 良定谱的联合图

在有限维 AW 原图空间中，\((F,\lambda)\mapsto\operatorname{gph}J_{\lambda F}\) 联合连续。上一轮完整开输入图表定理给：固定开 \(U\) 的

\[
\{(F,\lambda):\lambda\in\mathcal W_U(F)\}
\]

为 \(G_\delta\)。其在任一良定 atlas 内恢复的 \(T_{F,\lambda}\) 对 \((F,\lambda)\) 连续（compact-open）。但 \(G_\delta\) 谱图的步长投影一般只自动为 analytic，不能因步长轴一维就宣称 Borel。

### 8.2 收敛谱

在共同合法自映射／轨道 atlas 中：

- 逐初值收敛条件 \(\forall x\,[T^nx\text{ Cauchy 且 }d(T^nx,S)\to0]\) 自动有 coanalytic 上界；本文不主张其精确复杂度或 Borel 性。
- 在紧初值耗尽上局部一致收敛，可写为
  \(\forall j,\ell\ \exists N\ \forall n,m\ge N\) 的连续有限迭代不等式，故为 Borel；固定 atlas 中可取 \(\Pi^0_3\) 上界。
- 共同实际尾 \(\omega\) 已冻结时，相应全部有限迭代闭不等式给相对闭谱图。

这说明“所有逐初值收敛者”和“严格有限参数证书存在者”的集合论复杂度不应混作同一件事。

### 8.3 稳定性不能省略拓扑

即使某个 \(F\) 有全局严格 LT 证书，原 AW 拓扑下也可添入一个逃向无穷的图点 \((u_n,-u_n/\lambda)\)，使输入 0 产生额外解，同时新图 AW 收敛回原图。因此严格标量余量不意味着证书在最大原图空间中为开性质。受保护 atlas、共同输出界或更强的模拓扑承担了真实工作。

把 §7 的对象侧闭块记为 \(B_j^{LT}\)、\(B_j^D\)、\(B_j^E\)，则在冻结的中立空间 \(\mathfrak M\) 中可以严格研究

\[
\mathcal C_{LT}=\bigcup_j(B_j^{LT}\cap\mathfrak M),
\quad
\mathcal C_{RLEB}=\bigcup_j((B_j^D\cup B_j^E)\cap\mathfrak M).
\tag{8.1}
\]

下一项需证明的是这些**无标签对象闭块**在 \(\mathfrak M\) 或明确的相对 RLEB 层中的内点结构。以下推断仍不合法：

1. 每个固定步长 LT 切片第一纲，所以存在步长的并第一纲；
2. 证书参数空间中 LT 见证稀少，所以原算子像第一纲；
3. \(F_\sigma\) 所以第一纲；
4. 某个 RLEB 构造的 LT 谱为空，所以总体 LT 类小。

本模块解决的是 1、2 的量词与对象编码准备，没有冒充已完成 3、4 所欠缺的对象侧稠密性证明。

## 9. 文献定位：哪些部分已经有前人基准

以下只列实际读到的对应，不声称已完成这些谱定理的文献优先权审计。

- **Heinz H. Bauschke, Walaa M. Moursi, Xianfu Wang, _Generalized monotone operators and their averaged resolvents_**, arXiv:1902.09827。Fact 2.1 已有任意映射 \(T\) 与 \(T^{-1}-I\) 的 resolvent 对应；Corollary 2.13、Theorem 2.16 给广义单调假设下的全域性、单值性和 Minty 表示。本文不把逆图表示本身当新结果。[原文](https://arxiv.org/pdf/1902.09827)
- **Brecht Evens, Pieter Pas, Puya Latafat, Panagiotis Patrinos, _Convergence of the Preconditioned Proximal Point Method and Douglas–Rachford Splitting in the Absence of Monotonicity_**, arXiv:2305.03605。Proposition 4.12 给 \((\mu,\rho)\)-semimonotone 算子的显式允许步长区间、全域性及 Lipschitz 常数；其区间是有结构假设的保证区间，不是任意闭图算子的精确步长谱。本文的 §3 应与该结果比较，不应将“存在步长窗口”笼统宣布首创。[原文](https://arxiv.org/pdf/2305.03605)
- **D. Russell Luke, Matthew K. Tam, _Generalized Monotonicity and the Proximal Point Algorithm_**, DOI 10.1287/moor.2025.0863。Proposition 4 是反射 Lipschitz 与 submonotonicity 的准确对应；Assumption 2(d)(ii) 的门槛为 \(\tau(1+\rho/\lambda)^2<1/2\)；Theorem 2 是局部截断输出序列的收敛定理。本文只比较已对齐完整接口的公共证书像。[正式原文](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)

## 10. 给总协调的直接建议

现在不需要用户额外补一个数学假设来“救出”有理步长路线。正确推进是：

1. 冻结比较的是固定初值域的算法实例，还是允许缩域的原算子 germ；这会决定 §7 的 \(F_\sigma\) 是否就是目标类。
2. 采用实步长紧参数闭块，避免无根据的谱开放断言；LT/RLEB 的步长谱作为对象内生的子集保留。
3. 把主要证明资源集中于冻结中立分母中的对象侧闭块内点／无处稠密判据。
4. 将 §4–§6 放在体系的谱校准与反例章节，显示公理区分了真正不同的算法性质；不让它们替代总类大小定理。

本稿的潜在新增贡献是 **完整原图 germ 的闭证书块＋实步长投影桥** 及 **严格 RLEB 的单值谱与全选择收敛谱分离**。是否具有发表级原创性仍须独立原始文献核查，当前不作优先权承诺。
