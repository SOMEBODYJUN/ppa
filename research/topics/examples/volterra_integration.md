# Volterra 积分：逐点近端收敛与统一误差界的分离

<a id="vo-object"></a>
## 完整对象与来源

取实 Hilbert 空间 \(H=L^2(0,1)\)，在**整个** \(H\) 上定义
\[
(Vx)(t)=\int_0^t x(s)\,ds. \tag{VO1}
\]
这是有界、单值、单射的完整关系，\(S=V^{-1}(0)=\{0\}\)，
\(r_V(x)=\|Vx\|_2\)。其全部逆纤维为
\[
V^{-1}(y)=
\begin{cases}
\{y'\},&y\in H^1(0,1),\ y(0)=0,\\
\varnothing,&\text{否则}.
\end{cases} \tag{VO2}
\]
这里 \(y(0)\) 是绝对连续代表的迹。特别地，
\(C_c^\infty(0,1)\subset\operatorname{ran}V\)，所以值域稠密；
常函数 1 不在值域，故值域是真且非闭的线性子空间。

对象来自 9/01 ZIP 的 work/c_gx053_065.md §2 GX-060；精确
成员路径见[逐源去向](../../audit/UNIT_DISPOSITIONS.tsv)。
以下只裁决这张卡的指定单元；GX-061 的伴随图和外部 BWY
归属仍未审。同包 CCA-M10 给 \(V^*=UVU\)，
\((Uf)(t)=f(1-t)\)，两例不应不加说明地计为独立不变量。

<a id="vo-graph"></a>
## C104-v1：完整图几何与任意消失 gauge 的障碍

令 \(Y=Vx\)。分部积分给
\[
\langle x,Vx\rangle
=\tfrac12Y(1)^2
=\tfrac12\left(\int_0^1x(t)\,dt\right)^2\ge0. \tag{VO3}
\]
故 \(V\) 单调且定义域为全空间。若 \((z,v)\) 与全部图点单调
相关，取图点 \((z+th,Vz+tVh)\)，令 \(t\) 从两侧趋零便得
\(\langle h,v-Vz\rangle=0\) 对所有 \(h\) 成立；所以 \(v=Vz\)，
图极大单调。取 \(h(t)=t-\tfrac12\)：它非零、零均值而 \(Vh\ne0\)，
故不是严格单调，正强单调和正 cocoercivity 模都不存在。
同一零配对与 \((h,0)\notin\operatorname{gra}V\) 否定
paramonotonicity。

在本卡采用 rectangular 的完整图定义
\[
\inf_{z\in H}\langle x-z,v-Vz\rangle>-\infty
\quad(x\in\operatorname{dom}V,\ v\in\operatorname{ran}V). \tag{VO4}
\]
取 \(x=0,v=V1=t,z=\alpha h\)，则
\(\langle h,Vh\rangle=0\) 且
\(\langle h,t\rangle=1/12\)，所以左式中的配对等于
\(-\alpha/12\to-\infty\)。这是直接的非 rectangular 见证，
来源 GX-060 已给同一直线见证；这里从完整定义重新核算，
不导入外部等价定理。

对每个 \(n\ge1\) 令 \(e_n(t)=\sqrt2\cos(n\pi t)\)。则
\[
\|e_n\|=1,\qquad \|Ve_n\|=\frac1{n\pi}. \tag{VO5}
\]
因此对于**任意** \(\eta>0\)、任意
\(\psi:[0,\eta)\to[0,\infty)\) 满足
\(\lim_{s\downarrow0}\psi(s)=0\)，以及任意 \(C,\delta>0\)，
总存在 \(\|x\|<\delta,\|Vx\|<\eta\) 使
\[
\|x\|>C\psi(\|Vx\|). \tag{VO6}
\]
证明是固定 \(0<a<\delta\) 并取 \(x=ae_n\)，令 \(n\to\infty\)。
这里是真实**原算子残差**的全邻域失败，不要求 \(\psi\) 单调。
也可令 \(a_k\downarrow0\)，逐项选 \(n_k\) 令
\(\psi(a_k/(n_k\pi))<a_k/k\)，得到趋零输入上的见证。
全部正指数固定零目标 Hölder EB 失败。两目标 MR 另被任意
小而不在 \(\operatorname{ran}V\) 的目标击穿：逆纤维为空而
\(d(y,V(0))\) 有限。

<a id="vo-prox"></a>
## C105-v1：完整近端、锐反射与逐点强收敛

固定每个 \(\lambda>0\)。对 \(p\in H\) 定义
\(w(t)=\int_0^t e^{-\lambda(t-s)}p(s)\,ds\)。它满足
\(w'+\lambda w=p,w(0)=0\)。于是**完整** resolvent 在全空间
单值，且
\[
J_\lambda p=p-\lambda w,\qquad
(I+\lambda V)J_\lambda p=p,\qquad R_\lambda=2J_\lambda-I. \tag{VO7}
\]
齐次 Volterra 方程只有零解，保证这不是只选一支。
对任意两图点差 \(a\in H\)，
\[
\|(I+\lambda V)a\|^2-\|(I-\lambda V)a\|^2
=2\lambda\left(\int_0^1a\right)^2\ge0. \tag{VO8}
\]
所以全图、全部输入的 all-pairs 线性 RL 锐 \(L=1\)，
等号由任意非零零均值**图点差** \(a\) 取到。
对应 Minty 输入差是 \((I+\lambda V)a\)；不能把等号条件
错写成“任意零均值输入差”。缩放非零图点差又使任意
\(0<\gamma<1\) 的无界全图 Hölder RL 常数不可能有限。

对 \(p=(I+\lambda V)u\)，能量恒等式为
\[
\|p\|^2-\|J_\lambda p\|^2
=\lambda\left(\int_0^1u\right)^2+\lambda^2\|Vu\|^2. \tag{VO9}
\]
因此 \(J_\lambda\) 非扩张，对每个非零输入还**严格缩短**
范数。严格逐点不表示有统一常数小于 1。事实上
\(I-J_\lambda=\lambda J_\lambda V\)，故固定任意整数 \(k\ge1\)，
\[
\|J_\lambda^ke_n-e_n\|
\le k\lambda\|Ve_n\|=\frac{k\lambda}{n\pi}\to0,
\qquad \|J_\lambda^k\|_{\rm op}=1. \tag{VO10}
\]
每个有限幂的范数是 1，且非零向量不能取到它。

然而每个固定 \(p\) 的轨道仍强收敛于零。令
\(p_n=J_\lambda^np\)。由 (VO9) 和
\(p_{n-1}-p_n=\lambda Vp_n\) 得
\(\sum_n\|p_{n-1}-p_n\|^2\le\|p\|^2\)，
故步差趋零。\(V\) 与 \(J_\lambda\) 交换，因而对每个 \(y\in H\)
\[
J_\lambda^nVy
=\lambda^{-1}(J_\lambda^{n-1}y-J_\lambda^ny)\to0. \tag{VO11}
\]
\(\operatorname{ran}V\) 稠密且 \(\|J_\lambda^n\|\le1\)，遂有
\(J_\lambda^np\to0\) 对每个 \(p\in H\) **强收敛**。
这里没有证明每条路径有限长度或单位球上的统一趋零率。

最后，完整近端的定点集是 \(\{0\}\)，而
\(g_\lambda(p)=\|p-J_\lambda p\|\) 满足
\[
0<g_\lambda(ae_n)
\le\lambda a\|Ve_n\|
=\frac{\lambda a}{n\pi}\to0 \quad(a>0). \tag{VO12}
\]
把 \(a<\delta\) 固定即如 (VO6) 一样否定输入距离
\(d(p,\operatorname{Fix}J_\lambda)=\|p\|\) 对**近端步残差**
的任何统一局部消失 gauge EB。它与 (VO6) 是两个残差对象
的独立断言。

本卡说明“每个非零输入严格缩短”“每条轨道强收敛”
与“任意有限步均无统一严格收缩、任意消失 gauge EB 均失败”
可以在同一个完整极大单调图上并存。
