# 固定参数 RL 关系的有限维完整纤维分类

本页重构 [C04](../../CLAIMS.md) 与 [H03](../holder_structure.md#h03) 的同一陈述，供独立验收；证据状态与总账及接收记录同步。有限维必要性与任意实 Hilbert 空间上的不动点集实现分别证明，再合成两种完整纤维分类。历史来源是 S23 `thm:finite_geometry`、`lem:margin`、`thm:fixedset`、`thm:fibers`；下文给出所用论证，不以历史稿替代定义或证明。

<a id="ff-object"></a>
## FF-OBJECT · 对象、参数和精确量词

令 \(H\) 为实 Hilbert 空间，固定
\[
\lambda,L>0,\qquad 0<\gamma<1,\qquad R=L^{1/(1-\gamma)}.
\tag{FF1}
\]
关系 \(F:H\rightrightarrows H\) 的图非空。本文的 **全局 RL** 指对整个图中的每一对 \((x,v),(y,w)\) 都有
\[
\|(x-y)-\lambda(v-w)\|
\le L\|(x-y)+\lambda(v-w)\|^\gamma.
\tag{FF2}
\]
这里没有局部输入窗或被选支的限制。**固定参数 graph-maximal** 指不存在严格包含 \(\operatorname{gph}F\) 且仍满足同一 \((\lambda,L,\gamma)\) 的 (FF2) 的图；这是 RL 类内的图极大性。

完整正向、逆向纤维及集合像分别为
\[
F(x)=\{v:(x,v)\in\operatorname{gph}F\},\qquad
F^{-1}(v)=\{x:(x,v)\in\operatorname{gph}F\},\qquad
F(A)=\bigcup_{x\in A}F(x).
\tag{FF3}
\]
若 \(H=\mathbb R^n\)、\(n\ge1\)，本页证明：

1. **每个**满足上述固定参数图极大性的 \(F\)，对**每个** \(x,v\in\mathbb R^n\)，其 \(F(x)\)、\(F^{-1}(v)\) 均非空紧，且直径分别不超过 \(R/\lambda\)、\(R\)。
2. **每个**非空紧 \(K\subset\mathbb R^n\)，若 \(\operatorname{diam}K\le R\)，则存在**某个**同参数图极大 RL 关系，其完整 \(F^{-1}(0)=K\)。
3. 若同样的 \(K\) 满足 \(\operatorname{diam}K\le R/\lambda\)，则存在**某个**同参数图极大 RL 关系，其完整 \(F(0)=K\)。

后两项为分别存在的关系，不同时指定同一个关系的两种纤维。也不要求实现关系的最小 Hölder 常数必须等于给定上界 \(L\)。

无限维边界现由 [C183](infinite_fiber_boundary.md#if-counterexample) 明确关闭：即使满Minty输入、闭完整图和单点完整零集，也可同时有空的正向与逆向纤维。若同一C另非扩张，[C184](infinite_fiber_boundary.md#if-nonexpansive)恢复任意Hilbert的非空闭凸弱紧纤维；范数紧仍不能一般恢复。这里不改变C04的有限维身份。

<a id="ff-cayley"></a>
## FF-CAYLEY · 全图坐标与固定参数极大性

对图点置
\[
p=x+\lambda v,\qquad q=x-\lambda v,\qquad
\mathcal D=\{x+\lambda v:(x,v)\in\operatorname{gph}F\}.
\]
若两图点的 \(p\) 相同，(FF2) 迫使其 \(q\) 相同；线性方程再迫使两图点相同。因此
\[
C:\mathcal D\to H,\qquad C(x+\lambda v)=x-\lambda v
\]
良定，并满足
\[
\|C(p)-C(p')\|\le L\|p-p'\|^\gamma
\quad(p,p'\in\mathcal D).
\tag{FF4}
\]
反向，任意非空 \(\mathcal D\subset H\) 上满足 (FF4) 的 \(C\) 都定义关系
\[
\operatorname{gph}F_C
=\{\Gamma_C(p):p\in\mathcal D\},\qquad
\Gamma_C(p)=(X(p),V(p))
=\left(\frac{p+C(p)}2,\frac{p-C(p)}{2\lambda}\right).
\tag{FF5}
\]
直接计算给出 \(X(p)+\lambda V(p)=p\)、\(X(p)-\lambda V(p)=C(p)\)，故 (FF4) 恰给 (FF2)，两种构造互逆。

这里使用的规范层输入是 [HE-EXTENSION](holder_extension.md#he-extension)：实 Hilbert 源与目标之间，非空任意子集上的全局 \(L\)-Hölder 映射，在固定 \(0<\gamma<1\) 下有全空间的**同常数**扩张。其源、目标均取本页 \(H\)，子集取 \(\mathcal D\)，映射取上式 \(C\)。若 \(\mathcal D\ne H\)，该扩张的 (FF5) 严格扩张原图，仍满足同一组参数；因此 graph-maximal 蕴含 \(\mathcal D=H\)。

反向，若 \(\mathcal D=H\)，任意拟添加图点 \((x,v)\) 的 \(p=x+\lambda v\) 已有图点 \(\Gamma_C(p)\)。把二者代入 (FF2)，右侧为零，迫使 \(x-\lambda v=C(p)\)，从而 \((x,v)=\Gamma_C(p)\)。故不能严格扩图。于是
\[
F\text{ 在固定 }(\lambda,L,\gamma)\text{ 下 graph-maximal}
\quad\Longleftrightarrow\quad \mathcal D=H.
\tag{FF6}
\]
这个等价使用全图全尺度条件；它本身对任意实 Hilbert 空间成立。

<a id="ff-coercivity"></a>
## FF-COERCIVITY · 有限维的全域、全值域与完整纤维

本节限定 \(H=\mathbb R^n\)、\(n\ge1\)，且 \(C\) 定义在全部 \(\mathbb R^n\) 并满足 (FF4)。由 (FF6)，每个本页的图极大关系都满足此输入。

**次线性增长与有界逆像。** 记 \(c_0=\|C(0)\|\)。由 (FF4)，
\[
\begin{split}
\|C(p)\|&\le c_0+L\|p\|^\gamma,\\
2\|X(p)\|&\ge\|p\|-c_0-L\|p\|^\gamma,\\
2\lambda\|V(p)\|&\ge\|p\|-c_0-L\|p\|^\gamma.
\end{split}
\tag{FF7}
\]
因为 \(\gamma<1\)，后两式的共同右侧在 \(\|p\|\to\infty\) 时趋于 \(+\infty\)。所以 \(X\)、\(V\) 的任一有界目标集的逆像有界。具体地，令 \(T=(2L)^{1/(1-\gamma)}\)，当 \(\|p\|\ge T\) 时有 \(L\|p\|^\gamma\le\|p\|/2\)，故
\[
\begin{split}
\|X(p)\|\le B&\ \Longrightarrow\quad
\|p\|\le\max\{T,4B+2c_0\},\\
\|V(p)\|\le B&\ \Longrightarrow\quad
\|p\|\le\max\{T,4\lambda B+2c_0\}.
\end{split}
\tag{FF8}
\]

**每个目标的存在性。** 本节显式导入有限维 Brouwer 闭球不动点定理：对任意 \(M>0\)，连续自映射 \(T_0:\overline B(0,M)\to\overline B(0,M)\subset\mathbb R^n\) 至少有一个不动点。以下逐项验证其适用前件。

任给目标 \(x_*\in\mathbb R^n\)，取
\[
M\ge\max\{1,\ 2(2\|x_*\|+c_0),\ (2L)^{1/(1-\gamma)}\}.
\]
连续映射 \(T_{x_*}(p)=2x_*-C(p)\) 对 \(\|p\|\le M\) 满足
\[
\|T_{x_*}(p)\|\le 2\|x_*\|+c_0+LM^\gamma
\le M/2+M/2=M.
\]
故它是该闭球的连续自映射；Brouwer 给 \(p=T_{x_*}(p)\)，即 \(X(p)=x_*\)。于是 \(X\) 满射。

任给目标 \(v_*\in\mathbb R^n\)，取
\[
M\ge\max\{1,\ 2(2\lambda\|v_*\|+c_0),\ (2L)^{1/(1-\gamma)}\}.
\]
映射 \(T_{v_*}(p)=2\lambda v_*+C(p)\) 连续，且在该闭球上
\[
\|T_{v_*}(p)\|\le2\lambda\|v_*\|+c_0+LM^\gamma\le M.
\]
它也有不动点，等价于 \(V(p)=v_*\)。于是 \(V\) 满射。因此
\[
\operatorname{dom}F_C=\operatorname{ran}F_C=\mathbb R^n.
\tag{FF9}
\]
这里每次闭球半径可以依赖目标；所得满射性覆盖全部目标。

**Properness 与非空紧纤维。** (FF4) 保证 \(C,X,V,\Gamma_C\) 连续；\(\Gamma_C\) 从 \(\mathbb R^n\) 到 \(\operatorname{gph}F_C\) 的连续逆为 \((x,v)\mapsto x+\lambda v\)，所以它是同胚。连续性和 (FF7) 表明：对任意紧目标集 \(A\)，\(X^{-1}(A)\)、\(V^{-1}(A)\) 都闭且有界，在有限维中因而紧。这就是 \(X,V\) 的 properness（紧集逆像紧）。图的两坐标投影 \(\pi_x,\pi_v\) 满足
\[
\pi_x^{-1}(A)=\Gamma_C(X^{-1}(A)),\qquad
\pi_v^{-1}(A)=\Gamma_C(V^{-1}(A)),
\tag{FF10}
\]
故它们作为定义在整个图上的映射也 proper。具体到点纤维，
\[
F_C(x)=V(X^{-1}(\{x\})),\qquad
F_C^{-1}(v)=X(V^{-1}(\{v\})).
\tag{FF11}
\]
(FF9) 保证这两式的参数集非空，properness 保证其紧，连续性保证式中像紧。因此所有完整正向、逆向纤维都非空紧。

**闭图、局部有界与上半连续。** 若 \((x_j,v_j)\in\operatorname{gph}F_C\) 收敛至 \((x,v)\)，置 \(p_j=x_j+\lambda v_j\to p=x+\lambda v\)。由连续性，
\[
C(p)=\lim_j C(p_j)=\lim_j(x_j-\lambda v_j)=x-\lambda v,
\]
故 (FF5) 给 \((x,v)\in\operatorname{gph}F_C\)，图闭。

当 \(x\) 遍历一个有界集时，(FF8) 控制所有对应参数 \(p\)；再由 \(v=(p-x)/\lambda\) 得所有对应 \(v\) 一起有界。交换坐标，用 (FF8) 的第二式及 \(x=p-\lambda v\)，得逆关系也把有界集映成有界的值的并。这蕴含两关系的局部有界性。

上半连续采用开集定义：对每个 \(x\) 和包含 \(F_C(x)\) 的开集 \(O\)，存在 \(x\) 的邻域 \(U\) 使 \(F_C(U)\subset O\)。若不成立，可取 \(x_j\to x\)、\(v_j\in F_C(x_j)\setminus O\)。局部有界与有限维紧性给子列 \(v_{j_k}\to v\)；闭图给 \(v\in F_C(x)\subset O\)，开性使子列最终位于 \(O\)，矛盾。逆关系的证明交换 \(x,v\) 即得。最后，对紧 \(A\)，(FF10) 的图部分紧，其另一坐标投影分别是 \(F_C(A)\) 或 \(F_C^{-1}(A)\)，所以二者都是紧集。

本节的满射证明导入的是上述 Brouwer 不动点定理；这里没有使用或输出投影的 degree 数值。闭有界集的紧性与 Brouwer 闭球定理是有限维必要性证明的明确依赖，不能由本节推出一般无限维 Hilbert 关系的全部纤维非空紧。

<a id="ff-diameters"></a>
## FF-DIAMETERS · 两种完整纤维的直径门

本节只用 (FF2)，适用于任意实 Hilbert 空间中的任意全局 RL 关系，不需要图极大性。固定 \(v\)，任取 \(x,y\in F^{-1}(v)\)，得
\[
\|x-y\|\le L\|x-y\|^\gamma.
\]
若距离非零，除以其 \(\gamma\) 次幂得到 \(\|x-y\|^{1-\gamma}\le L\)，即距离不超过 \(R\)。固定 \(x\)，任取 \(v,w\in F(x)\)，同理得到
\[
\lambda\|v-w\|\le L(\lambda\|v-w\|)^\gamma,
\]
非零时等价于 \(\|v-w\|\le R/\lambda\)。对任意非空纤维取上确界，因此
\[
\operatorname{diam}F^{-1}(v)\le R,\qquad
\operatorname{diam}F(x)\le R/\lambda.
\tag{FF12}
\]
零距离的点对自动满足不等式；这些比较本身不证明纤维非空或紧。

<a id="ff-margin"></a>
## FF-MARGIN · 任意 Hilbert 空间的严格凸包余量

以下三节令 \(H\) 为任意实 Hilbert 空间，令 \(K\subset H\) 非空紧，记
\[
D=\operatorname{diam}K,\qquad Q=\overline{\operatorname{conv}}K.
\tag{FF13}
\]
\(Q\) 非空、闭、凸且有界。任给 \(k\in K\)，对有限凸组合 \(q=\sum_i\alpha_i k_i\) 有
\(\|k-q\|\le\sum_i\alpha_i\|k-k_i\|\le D\)，取极限得此式对全部 \(q\in Q\) 成立。再对另一坐标取凸组合及极限，得 \(\|p-q\|\le D\) 对全部 \(p,q\in Q\) 成立。因 \(K\subset Q\)，\(\operatorname{diam}Q=D\)。

对每个 \(p\in Q\)，有更严格的余量
\[
\sup_{q\in Q}\|p-q\|^2\le D^2-d(p,K)^2,
\qquad d(p,K)=\inf_{k\in K}\|p-k\|.
\tag{FF14}
\]
证明如下。取有限凸组合 \(p_m=\sum_i\alpha_{m,i}k_{m,i}\to p\)，其中权重非负且和为一。固定 \(q\in Q\)，展开平方并利用 \(\sum_i\alpha_{m,i}(k_{m,i}-p_m)=0\)，得到 Hilbert 方差恒等式
\[
\begin{split}
\|p_m-q\|^2
&=\sum_i\alpha_{m,i}\|k_{m,i}-q\|^2
-\sum_i\alpha_{m,i}\|k_{m,i}-p_m\|^2\\
&\le D^2-d(p_m,K)^2.
\end{split}
\]
距离函数是 \(1\)-Lipschitz，故令 \(m\to\infty\) 得每个 \(q\) 的不等式，再取 \(q\) 的上确界即得 (FF14)。该结论的量词始终是 \(p\in Q\)。

<a id="ff-projection"></a>
## FF-PROJECTION · 所用 Hilbert 投影性质

对非空闭凸 \(Q\subset H\)，度量投影 \(P_Q:H\to Q\) 存在、唯一、非扩张，并固定 \(Q\) 中每点。这里给出后文所需的短证明。

固定 \(x\in H\)，令 \(d=\inf_{q\in Q}\|x-q\|\)，取极小化序列 \(q_j\in Q\) 满足 \(\|x-q_j\|\to d\)。凸性使 \((q_j+q_k)/2\in Q\)，平行四边形恒等式给
\[
\|q_j-q_k\|^2
=2\|x-q_j\|^2+2\|x-q_k\|^2
-4\left\|x-\frac{q_j+q_k}2\right\|^2
\le2\|x-q_j\|^2+2\|x-q_k\|^2-4d^2\to0.
\]
故序列 Cauchy，完备性和闭性给极小点 \(q\in Q\)。同一中点计算应用于两个极小点给唯一性，定义 \(P_Qx=q\)。若 \(x\in Q\)，显然 \(q=x\)。对 \(z\in Q\) 和 \(0<t\le1\)，极小性比较 \(q+t(z-q)\)，展开后令 \(t\downarrow0\)，得
\[
\langle x-q,z-q\rangle\le0.
\]
对 \(q=P_Qx,r=P_Qy\)，分别取 \(z=r,q\) 并相加整理，得
\[
\|q-r\|^2\le\langle x-y,q-r\rangle
\le\|x-y\|\|q-r\|.
\]
距离非零时相除，零时结论直接成立，即 \(\|P_Qx-P_Qy\|\le\|x-y\|\)。整个证明不需要有限维或 \(Q\) 紧。

<a id="ff-fixedset"></a>
## FF-FIXEDSET · 同常数的精确不动点集实现

**命题。** 对任意实 Hilbert 空间中的非空紧 \(K\) 和 \(0<\gamma<1\)，存在
\[
R_K:H\to Q=\overline{\operatorname{conv}}K,
\qquad \operatorname{Fix}R_K=K,
\qquad
\|R_K(x)-R_K(y)\|\le D^{1-\gamma}\|x-y\|^\gamma
\quad(x,y\in H).
\tag{FF15}
\]
\(D=0\) 时系数为零。\(D>0\) 时，任何固定 \(K\) 中每点的全局 \(\gamma\)-Hölder 映射，其常数都至少为 \(D^{1-\gamma}\)。

**单点和凸情形。** 若 \(D=0\)，非空 \(K\) 是单点 \(\{k_0\}\)，取常值 \(R_K(x)=k_0\)，完整不动点集恰为 \(K\)。以下设 \(D>0\)，记 \(L_0=D^{1-\gamma}\)，固定 \(k_0\in K\)。若 \(Q=K\)，取 \(R_K=P_Q\)。投影非扩张和 \(Q\) 的直径给
\[
\|P_Qx-P_Qy\|\le\min\{\|x-y\|,D\}
\le D^{1-\gamma}\|x-y\|^\gamma.
\tag{FF16}
\]
最后一步对 \(h=\|x-y\|\le D\) 用 \(h^{1-\gamma}\le D^{1-\gamma}\)，对 \(h\ge D\) 用 \(D^\gamma\le h^\gamma\)；\(h=0\) 直接成立。投影的完整不动点集是 \(Q=K\)。

**一个局部 bump 的正幅度与全对估计。** 现设 \(Q\setminus K\ne\varnothing\)。对每个 \(p\in Q\setminus K\)，由于 \(K\) 闭，定义
\[
d_p=d(p,K)>0,\qquad E_p=\sqrt{D^2-d_p^2}<D.
\]
(FF14) 保证根号下非负，并保证 \(\|p-q\|\le E_p\) 对全部 \(q\in Q\) 成立。取
\[
0<r_p<\min\{d_p/2,(D-E_p)/2\},\qquad
D_p=E_p+r_p\in(0,D).
\tag{FF17}
\]
在 \(Q\) 上定义
\[
\phi_p(y)=\max\{1-\|y-p\|/r_p,0\},\qquad
H_p(y)=\phi_p(y)(y-k_0),\qquad M_p=1+D/r_p.
\tag{FF18}
\]
\(0\le\phi_p\le1\)，它在 \(K\) 上为零，在相对开球 \(Q\cap B(p,r_p)\) 上严格为正，且 Lipschitz 常数至多 \(1/r_p\)。对全部 \(y,z\in Q\)，
\[
\begin{split}
\|H_p(y)-H_p(z)\|
&\le\phi_p(y)\|y-z\|+|\phi_p(y)-\phi_p(z)|\|z-k_0\|\\
&\le(1+D/r_p)\|y-z\|=M_p\|y-z\|.
\end{split}
\tag{FF19}
\]
选择一个明确的正数
\[
\varepsilon_p=\frac12\min\left\{1,
\frac{L_0D_p^{\gamma-1}-1}{M_p}\right\}>0.
\tag{FF20}
\]
正性来自 \(D_p<D\)、\(\gamma-1<0\)，因此 \(L_0D_p^{\gamma-1}>D^{1-\gamma}D^{\gamma-1}=1\)。同时 \(\varepsilon_p\le1\) 且
\(1+\varepsilon_pM_p\le L_0D_p^{\gamma-1}\)。置
\[
S_p(y)=y-\varepsilon_pH_p(y)
=(1-\varepsilon_p\phi_p(y))y+\varepsilon_p\phi_p(y)k_0.
\tag{FF21}
\]
系数非负、和为一，所以 \(S_p(Q)\subset Q\)，且 \(S_p\) 固定 \(K\) 中每点。

现在核对 **所有点对** 的同一个 Hölder 常数。若 \(\phi_p(y)=\phi_p(z)=0\)，则 \(S_p(y)-S_p(z)=y-z\)，且 \(\|y-z\|\le D\)，故由 (FF16) 的同一标量不等式得到 \(L_0\)-Hölder 估计。否则可交换 \(y,z\) 使 \(\phi_p(y)>0\)，于是
\[
h=\|y-z\|\le\|y-p\|+\|p-z\|<r_p+E_p=D_p.
\]
\(h=0\) 时无需相除；\(h>0\) 时，由 (FF19)–(FF20)，
\[
\|S_p(y)-S_p(z)\|
\le(1+\varepsilon_pM_p)h
\le L_0D_p^{\gamma-1}h
\le L_0h^\gamma.
\tag{FF22}
\]
最后一步用的是 \(0<h<D_p\) 和负指数 \(\gamma-1\)，即 \(D_p^{\gamma-1}\le h^{\gamma-1}\)。因此每个 \(S_p\) 对整个 \(Q\) 都具有共同常数 \(L_0\)，包括仅一个端点落在 bump 中的点对。

**可数覆盖、正权级数与无额外不动点。** 紧度量空间 \(K\) 可分；例如对每个正整数 \(m\) 取有限 \(1/m\)-网，其可数并在 \(K\) 中稠密。这个稠密集的有限有理凸组合是可数的，并在 \(Q\) 中稠密。所以 \(Q\) 可分；以稠密点为中心、有理半径的开球构成可数基，\(Q\setminus K\) 也有可数基。

相对开球 \(Q\cap B(p,r_p)\)、\(p\in Q\setminus K\)，覆盖 \(Q\setminus K\) 且均与 \(K\) 不交。可数基给这个覆盖一个有限或可数子覆盖：对每个被某个覆盖成员包含的非空基元素选择一个这样的成员，所选成员仍覆盖每一点。把对应的映射、参数记为 \(S_j,\varepsilon_j,\phi_j\)。若子覆盖有限、大小为 \(N\)，取 \(a_j=1/N\)；若可数无限，按 \(j\ge1\) 编号并取 \(a_j=2^{-j}\)。在两种情形下都有
\[
a_j>0,\qquad \sum_j a_j=1.
\]
定义
\[
S(y)=\sum_j a_jS_j(y),\qquad
\theta(y)=\sum_j a_j\varepsilon_j\phi_j(y)
\quad(y\in Q).
\tag{FF23}
\]
\(Q\) 有界且 \(S_j(Q)\subset Q\)，故 \(\sup_{j,y\in Q}\|S_j(y)\|\le\|k_0\|+D\)；第一式由权重尾和控制而在 \(Q\) 上一致收敛。第二式因 \(0\le\varepsilon_j\phi_j\le1\) 也一致收敛，且 \(0\le\theta\le1\)。有限部分和补上剩余权重乘 \(k_0\)，
\[
\sum_{j=1}^N a_jS_j(y)+\left(1-\sum_{j=1}^N a_j\right)k_0\in Q;
\]
它们收敛到 \(S(y)\)，闭性给 \(S(Q)\subset Q\)。共同估计 (FF22) 则给
\[
\|S(y)-S(z)\|\le\sum_j a_j\|S_j(y)-S_j(z)\|
\le L_0\|y-z\|^\gamma.
\tag{FF24}
\]
对有限子覆盖，这些级数和极限步骤就是有限和。

把 (FF21) 代入 (FF23)，利用权重和为一，可得精确式
\[
S(y)=y-\theta(y)(y-k_0).
\tag{FF25}
\]
若 \(y\in K\)，所有 \(\phi_j(y)=0\)，所以 \(S(y)=y\)。若 \(y\in Q\setminus K\)，子覆盖保证至少一个 \(\phi_j(y)>0\)，而该项 \(a_j\varepsilon_j>0\)，所以 \(\theta(y)>0\)。又因 \(k_0\in K\)，此时 \(y-k_0\ne0\)，(FF25) 保证 \(S(y)\ne y\)。故在 \(Q\) 上完整地得到 \(\operatorname{Fix}S=K\)，没有额外不动点。

**延至全空间及常数最优性。** 取
\[
R_K=S\circ P_Q:H\to Q.
\]
由 (FF24) 与投影非扩张，
\[
\|R_K(x)-R_K(y)\|
\le L_0\|P_Qx-P_Qy\|^\gamma
\le L_0\|x-y\|^\gamma.
\]
若 \(R_K(x)=x\)，其值域在 \(Q\) 中，故 \(x\in Q\)、\(P_Qx=x\)，于是 \(S(x)=x\) 迫使 \(x\in K\)。反向，\(x\in K\) 同时被 \(P_Q\) 与 \(S\) 固定。因此其完整不动点集确为 \(K\)。

最后，任意固定每个 \(k\in K\) 的映射若有全局 \(\gamma\)-Hölder 常数 \(B\ge0\)，则对不同 \(k,l\in K\)，
\[
\|k-l\|\le B\|k-l\|^\gamma
\quad\Longrightarrow\quad B\ge\|k-l\|^{1-\gamma}.
\]
取点对距离的上确界得 \(B\ge D^{1-\gamma}\)。这证明 (FF15) 的最优常数，完成任意 Hilbert 空间上的不动点集实现。构造的值域包含于 \(Q\)（目标空间为 \(Q\)），不要求落在 \(K\) 中；未声称满射 \(Q\)。

<a id="ff-classification"></a>
## FF-CLASSIFICATION · 双向完整纤维分类

现在恢复 \(H=\mathbb R^n\)、\(n\ge1\) 及 (FF1) 的固定参数。

**必要性。** 对任何同参数 graph-maximal RL 关系，(FF6) 使 Cayley 定义域为全部 \(\mathbb R^n\)；[FF-COERCIVITY](#ff-coercivity) 使每个完整正向和逆向纤维非空紧；(FF12) 给两种直径界。因此 \(F^{-1}(0)\) 必须非空紧且直径不超过 \(R\)，而 \(F(0)\) 必须非空紧且直径不超过 \(R/\lambda\)。

**逆零纤维的充分性。** 给定非空紧 \(K\subset\mathbb R^n\)，设 \(D=\operatorname{diam}K\le R\)。[FF-FIXEDSET](#ff-fixedset) 给全域映射 \(R_K\)，其完整不动点集为 \(K\)，且常数 \(D^{1-\gamma}\le R^{1-\gamma}=L\)。在 (FF5) 中取 \(C=R_K\)，即定义整个图
\[
\operatorname{gph}F
=\left\{\left(\frac{p+R_K(p)}2,
\frac{p-R_K(p)}{2\lambda}\right):p\in\mathbb R^n\right\}.
\tag{FF26}
\]
全域性、(FF4)–(FF6) 保证这个非空关系满足指定 \((\lambda,L,\gamma)\) 的全局 RL 且在这些参数下图极大。其图点输出为零当且仅当 \(p=R_K(p)\)，当且仅当 \(p\in K\)；在这样的点，输入 \((p+R_K(p))/2=p\)。因此一方面每个 \(p\in K\) 都给 \((p,0)\in\operatorname{gph}F\)，另一方面每个 \((x,0)\in\operatorname{gph}F\) 都必须满足 \(x=p\in K\)。这证明**整个** \(F^{-1}(0)=K\)。

**正向零纤维的充分性。** 给定非空紧 \(K\subset\mathbb R^n\)，设 \(D\le R/\lambda\)。令 \(K'=\lambda K=\{\lambda k:k\in K\}\)，则 \(K'\) 非空紧且直径为 \(\lambda D\le R\)。对 \(K'\) 使用 (FF15)，记所得映射为 \(S=R_{K'}\)，其完整不动点集为 \(K'\)，Hölder 常数至多 \(L\)。取 \(C=-S\)，定义
\[
\operatorname{gph}F
=\left\{\left(\frac{p-S(p)}2,
\frac{p+S(p)}{2\lambda}\right):p\in\mathbb R^n\right\}.
\tag{FF27}
\]
负号不改变 Hölder 常数；全域性和 (FF6) 再次给指定参数的图极大 RL 关系。其图点输入为零当且仅当 \(p=S(p)\)，当且仅当 \(p\in\lambda K\)；此时输出为 \(p/\lambda\in K\)。反之每个 \(k\in K\) 取 \(p=\lambda k\) 都产生 \((0,k)\)；因而**整个** \(F(0)=K\)。

**单点、参数余量和非零基点。** 当 \(K=\{k\}\) 时，(FF26) 使用 \(C\equiv k\)，所得关系是 \(F(x)=\{(x-k)/\lambda\}\)；(FF27) 使用 \(C\equiv-\lambda k\)，所得关系是 \(F(x)=\{x/\lambda+k\}\)。它们的 Cayley 常数为零，仍在任意给定 \(L>0\) 的同参数 RL 类中图极大，因为 (FF6) 的证明只要求全域与常数不超过 \(L\)。这也适用于所有 \(D^{1-\gamma}<L\) 的情形。

若要在指定输出 \(v_0\) 实现 \(F^{-1}(v_0)=K\)，把 (FF26) 的图整体变为 \(\{(x,v+v_0):(x,v)\in\operatorname{gph}F\}\)。若要在指定输入 \(x_0\) 实现 \(F(x_0)=K\)，把 (FF27) 的图整体变为 \(\{(x+x_0,v):(x,v)\in\operatorname{gph}F\}\)。两种平移都保留所有图点差和 (FF2)，也保留图极大性：任何平移后严格的兼容扩图逆平移即严格扩张原图。

因此 C04 的两条等价分类分别成立。一般 Hilbert 空间中，把 (FF26)、(FF27) 的参数域 \(\mathbb R^n\) 换成 \(H\)，(FF15) 仍给每个满足直径门的非空紧 \(K\subset H\) 的同参数图极大实现；这是**充分性**。本页对**每个**图极大关系的全部纤维都非空紧的必要性仅在有限维证明，不把该必要性整体推广到无限维。这里也没有推导真实残差误差界、PPA 收敛或零集的邻域回缩。

**来源与接续接口。** 本页与 S23 的上述四项同题，另将有限维存在性改写为显式闭球自映射。唯一跨页数学输入是 [HE-EXTENSION](holder_extension.md#he-extension) 的同常数全域扩张；显式外部定理输入是有限维 Brouwer 闭球不动点定理。所有用于 C04 的其余步骤在本页展开。投影 degree、C03 的 simultaneous shadow、Hausdorff 影子估计及文献新颖性均不属于本页的验收输出。
