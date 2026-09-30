# 结构性变形定理与三项真实瓶颈

日期：2026-09-20。定位：构建性工作稿；不声明文献优先权。

复核状态：独立障碍审计代理已在两项补全后给出 **范围内 PASS**：完整图共轭／尾放宽、真实全纤维 EB、all-pairs RL、严格兼容、小初值 germ 留域闭合、任意正步长 LT 排除均复核成立。该 PASS **不扩展**到同一个宏观 \(\mathfrak D_e\)、被冻结的宏观证书域或整体相对纲判决。

## 0. 可直接汇报的结论

本次得到两个不同层次的结构工具：

1. **整个良定 atlas 上的图共轭运输定理。** 对完整原图作用，保留全部 resolvent 纤维、精确零集、共同轨道及实际尾；尾预算只乘任意接近 1 的因子。额外的小位移条件还可保留真实最小残差的双侧乘法比较。
2. **正常收缩—非退化切向漂移层上的幂次变形定理。** 对该结构层的任意映射而非单个公式模型，近恒等法向重标定同时产生严格 RLEB 和无界 linear-displacement，从而排除同一个新原算子在任意正步长下的 LT all-pairs 证书。

仍未证明三个关键桥梁：

- 将 \(D_e\to D_{(1+\varepsilon)e}\) 变成严格同一个冻结尾层内的变形；
- 上述正常收缩—切向漂移层在中立母空间中的稠密性／相对纲；
- 将仿射解流形推广到一般闭解集，或无需管状／分裂结构的整 atlas 版本。

因此已经有了结构性工具，但**没有得到中立母空间中 RLEB 对 LT 的总体纲判决**。

## 1. 整个完整图上的共轭作用

令 \(E=\mathbb R^d\)、\(\lambda>0\)、\(G=\operatorname{gph}F\) 非空闭，
\[
L_\lambda(u,v)=(u+\lambda v,u),\qquad
\Gamma=L_\lambda G=\operatorname{gph}J_{\lambda F}.
\]
假定在共同开输入域 \(U\)，完整 resolvent 为连续单值 \(T\)。给定同胚 \(h:E\to E\)，定义
\[
G^h=L_\lambda^{-1}(h\times h)L_\lambda G.
\tag{1.1}
\]
这不是通常意义下的 \(hFh^{-1}\)，不可混同。

### 定理 1：完整图与动力学精确运输

若 \(h(U)=U\)，则
\[
J_{\lambda F^h}(x)=h(J_{\lambda F}(h^{-1}x)),\qquad
T^h=hTh^{-1}.
\tag{1.2}
\]
闭图被保留，且 \(\operatorname{zer}F^h=h(\operatorname{zer}F)\)。若 \(h|_S=I\)，精确零集 \(S\) 被保留。

若共同初值域 \(B\)、工作域 \(W\) 分别被 \(h\) 保持，则所有轨道留域与收敛量词精确对应：
\[
(T^h)^n=hT^nh^{-1},\qquad \Pi^h=h\Pi h^{-1}.
\tag{1.3}
\]
若极限在 \(S\)，则 \(\Pi^h=\Pi h^{-1}\)。

若 \(\sup_E|h-I|\le a\)，有
\[
d_H(G,G^h)\le \sqrt2\|L_\lambda^{-1}\|a,
\tag{1.4}
\]
故在原图 AW 拓扑中任意接近。若 \(T\) 在有关共同紧区上 \(M\)-Lipschitz，
\[
\|T^h-T\|_\infty\le (1+M)a.
\tag{1.5}
\]

**证明。** 将 \((x,u)\in\Gamma^h\) 反变换即得 (1.2)；同胚保持闭图与对角点。迭代式归纳即得。每个图点及其同胚像的两坐标各移动至多 \(a\)，得到 (1.4)。又 \(\|h^{-1}-I\|_\infty=\|h-I\|_\infty\)，得到 (1.5)。□

### 定理 2：共同实际尾预算

设原对象在共同初值域上满足
\[
\|T^mx-T^nx\|\le e_n\quad(m\ge n),\qquad
d(T^nx,S)\le e_n.
\]
若 \(\operatorname{Lip}(h)\le1+\varepsilon\)、\(h|_S=I\)，则
\[
T\in\mathfrak D_e\Longrightarrow T^h\in\mathfrak D_{(1+\varepsilon)e}.
\tag{1.6}
\]
共同单步有限长预算 \(a_n\) 同样乘 \(1+\varepsilon\)。若原对象本就位于 \(\mathfrak D_{e/(1+\varepsilon)}\)，新对象才由此保持在原冻结的 \(\mathfrak D_e\)。

**重要限制：** (1.6) 本身不是同一个空间内的稠密性定理。严格尾余量对象是否稠密，需要单独证明。

## 2. 全纤维残差运输与一条 no-go

令
\[
r_F(u)=\inf\{\|v\|:(u,v)\in G\},\qquad \inf\varnothing=+\infty.
\]
有限维闭图保证 \(r_F\) 下半连续，且 \(u\notin S\Rightarrow r_F(u)>0\)。

若 \(h\) 支持于 \(U\setminus S\)，并满足
\[
|h(z)-z|\le\varepsilon
\min\{d(z,S),\,|z-Tz|,\,\lambda r_F(z)\},
\qquad z\in U,\quad 0<\varepsilon<1/4,
\tag{2.1}
\]
而在 \(E\setminus U\) 令 \(h=I\)，故无需在那里定义 \(T\)。
则每一个完整图 transition \((x,u)\in\Gamma\) 都满足
\[
(1-2\varepsilon)|x-u|
\le |h(x)-h(u)|
\le(1+2\varepsilon)|x-u|.
\tag{2.2}
\]
因为移动输入时 \(u=Tx\)；移动输出时 \(\lambda r_F(u)\le|x-u|\)。

完整逆纤维双射后取下确界，得到
\[
(1-2\varepsilon)r_F(u)\le r_{F^h}(h(u))
\le(1+2\varepsilon)r_F(u).
\tag{2.3}
\]
另外
\[
(1-\varepsilon)d(u,S)\le d(h(u),S)
\le(1+\varepsilon)d(u,S).
\tag{2.4}
\]
故原真实 EB \(d(u,S)\le\psi(r_F(u))\) 运输为
\[
d(h(u),S)\le
(1+\varepsilon)\psi\!\left(
\frac{r_{F^h}(h(u))}{1-2\varepsilon}\right).
\tag{2.5}
\]
这里没有把选中分支残差冒充最小范数残差，域外逆像也被保留。

### no-go：这种双侧保真不能制造无界 linear-displacement

由 (2.2)–(2.4)，
\[
\frac{|T^h(hx)-hx|}{d(hx,S)}
\le\frac{1+2\varepsilon}{1-\varepsilon}
\frac{|Tx-x|}{d(x,S)}.
\tag{2.6}
\]
若原 \(T\) 为 Lipschitz 且固定 \(S\)，右侧有界。因此要排除所有步长 LT，不能一边要求这种距离／残差双侧保真，一边要求新的 linear-displacement 无界。

下一节故意放弃 (2.1) 的法向距离保真，并**重新独立证明整个真实 EB**。

## 3. 任意正常收缩—非退化切向漂移对象的构造

本节固定
\[
E=\mathbb R^m\times\mathbb R^n,\quad m\ge n\ge1,
\qquad S=\mathbb R^m\times\{0\}.
\]
可以在有足够共同 collar 的局部管状图表中使用；为保证没有遗漏远端原像，主定理先采用全域单值完整 resolvent 坐标。

这不是要求三角独立性：\(B\) 可以依赖 \(y\)，\(A\) 可以同时依赖两个变量。对仿射 \(S\)，取原欧氏度量下的正交切向投影 \(P\)、法向投影 \(Q\)，条件可坐标不变地写成
\[
c\,d(x,S)\le\|P(Tx-x)\|,\qquad
\|Q(Tx)\|\le q\,d(x,S).
\]
构造是沿正常纤维作径向幂压缩；没有通过更换原度量来制造收缩。

令 \(T:E\to E\) 连续，具有结构
\[
T(y,z)=\big(y+A(y,z),\,B(y,z)\big).
\tag{3.1}
\]
假定：

- \(A(y,0)=B(y,0)=0\)；
- 存在 \(c>0\)、\(q\in(0,1)\)，对所有全域输入
  \[
  |A(y,z)|\ge c|z|,\qquad |B(y,z)|\le q|z|;
  \tag{3.2}
  \]
- 在每个所用有限切向 collar 和法向小管上，\(A,B\) 为 \(C^{1,1}\)，并有
  \[
  \|D_zA\|\le M,\quad
  \|D_yA\|\le C_A|z|,\quad
  \|D_zB\|\le M_B,\quad
  \|D_yB\|\le C_B|z|.
  \tag{3.3}
  \]

后两个带 \(|z|\) 的界来自一致 \(C^{1,1}\) 和 \(A(y,0)=B(y,0)=0\)，但为避免隐藏常数，仍明确列出。在整个小管有一致常数时，下面的结论对整个切向片统一成立。

由 \(|B|\le q|z|\)，精确固定点集为 \(S\)。由 \(|A|\le M|z|\)，共同 collar 的轨道留域可按
\[
\sum_{k\ge0}|A(y_k,z_k)|\le \frac{M|z_0|}{1-q}
\tag{3.4}
\]
核查。当前研究本就在实际收敛层中，本节不把 (3.4) 当成 RLEB 新得到的收敛结论。

### 法向近恒等幂压缩

固定 \(\gamma\in(0,1)\)、\(p=1/\gamma>1\)。取很小的 \(\rho>0\)，满足 \(p\rho^{p-1}<1\)。在法向球 \(|z|\le\rho\) 定义
\[
\phi(z)=|z|^{p-1}z.
\tag{3.5}
\]
在 \(\rho\le |z|\le R\) 用严格递增径向线性函数连接半径 \(\rho^p\) 与 \(R\)，在 \(|z|\ge R\) 恢复恒等。选择 \(R\) 使
\[
\frac{R-\rho^p}{R-\rho}\le1+\varepsilon,
\tag{3.6}
\]
例如 \(R=2(1+\varepsilon)\rho/\varepsilon\) 在 \(\rho\) 足够小时即可。

则 \(\phi\) 是全局同胚，\(\operatorname{Lip}(\phi)\le1+\varepsilon\)，且
\[
\sup_z|\phi(z)-z|\le R\longrightarrow0.
\]
令
\[
h(y,z)=(y,\phi(z)),\qquad T'=hTh^{-1}.
\tag{3.7}
\]
它保持 \(S\)，也保持半径至少为 \(R\) 的以零为中心法向球及其与切向初值块的乘积，并满足定理 1–2。特别是可以把支撑管放在预先冻结的法向初值半径之内。半径小于 \(R\) 的球一般不被保持，不能省略此范围。

在 \(|w|\le\rho^p\)，有 \(z=f_\gamma(w):=|w|^{\gamma-1}w\)，且
\[
T'(y,w)=
\left(y+A(y,f_\gamma(w)),
\,|B(y,f_\gamma(w))|^{p-1}B(y,f_\gamma(w))\right).
\tag{3.8}
\]

### 定理 3：无界 linear-displacement 与正常收缩同时成立

由 (3.2)、(3.8)，
\[
|T'(y,w)-(y,w)|\ge c|w|^\gamma,
\qquad
d(T'(y,w),S)\le q^p|w|.
\tag{3.9}
\]
因此
\[
\frac{|T'x-x|}{d(x,S)}
\ge c\,d(x,S)^{\gamma-1}\longrightarrow+\infty
\tag{3.10}
\]
在每个解点附近均成立，同时正常距离严格收缩。

这是整个函数结构层的结果，不是某一个选定的 \(A,B\) 公式。

## 4. 全部逆纤维上的真实幂次 EB

由连续全域映射 \(T'\) 定义完整原算子
\[
F'(u)=\{(x-u)/\lambda:T'x=u\}.
\tag{4.1}
\]
即定理 1 的 \(F^h\)，图闭且完整 \(J_{\lambda F'}=T'\)。

### 定理 4：真实 EB，不是 transition-only EB

对所有满足 \(d(u,S)\le q^p\rho^p\) 的输出，
\[
d(u,S)\le
\left(\frac{\lambda q}{c}\,r_{F'}(u)\right)^p.
\tag{4.2}
\]

**证明。** 任取完整逆像 \(x=(y,\phi(z))\)，满足 \(T'x=u\)。因为 \(h\) 不改切向坐标，
\[
|x-u|\ge |A(y,z)|\ge c|z|.
\tag{4.3}
\]
若 \(|z|\le\rho\)，则 \(|B(y,z)|\le q\rho<\rho\)，
\[
d(u,S)=|\phi(B(y,z))|
=|B(y,z)|^p\le q^p|z|^p
\le(q/c)^p|x-u|^p.
\]
若 \(|z|>\rho\)，则由输出局部化条件
\[
d(u,S)\le q^p\rho^p
\le(q/c)^p|x-u|^p.
\]
所以同一估计对**所有**逆像成立；对整个纤维取下确界即得 (4.2)。空纤维时右侧为无穷，EB 自动成立。□

若只在局部 atlas 而非全域 (3.1) 中操作，必须额外证明远端逆像残差隔离；本定理不能无证忽略它们。可采用共同紧输出 collar 和小残差将输入强制留在已检管区，但阈值与最终 EB 工作域须重新量化。

## 5. all-pairs RL 与严格兼容

取任意有效常数 \(C_\gamma\) 使
\[
|f_\gamma(w)-f_\gamma(\widetilde w)|
\le C_\gamma|w-\widetilde w|^\gamma.
\tag{5.1}
\]
为不依赖最佳常数，可统一取 \(C_\gamma=5\)。直接验证：记较大半径为 \(r\)、差距为 \(\delta\)。若 \(\delta\ge r/2\)，三角不等式给出 \(2r^\gamma\le2^{1+\gamma}\delta^\gamma\le4\delta^\gamma\)；否则连接线段距原点至少 \(r/2\)，导数范数不超过 \((r/2)^{\gamma-1}\)，从而给出常数不超过 2。更佳常数可减少阈值，但不是本定理所需。

设
\[
N(y,w)=|B(y,f_\gamma(w))|^{p-1}B(y,f_\gamma(w)).
\]
在 \(w\ne0\) 处，由链式法则
\[
\|D_wN\|\le p q^{p-1}M_B,\qquad
\|D_yN\|\le p q^{p-1}C_B|w|.
\tag{5.2}
\]
因此 \(N\) 在小凸管区中 Lipschitz，并连续延拓到 \(w=0\)。这一步不能只用未经检查的“幂复合保持 Lipschitz”替代。

对直径不超过 \(D\) 的小凸输入块，由 (3.3)、(5.1)–(5.2)，完整反射映射 \(R'=2T'-I\) 满足
\[
|R'x-R'\widetilde x|
\le L_D|x-\widetilde x|^\gamma,
\qquad
L_D=2M C_\gamma+C_0D^{1-\gamma},
\tag{5.3}
\]
其中 \(C_0<\infty\) 取决于该 collar 的导数界，而非两点的选择。证明是将切向 \(2A\) 的法向变化用 (5.1) 控制，其余 Lipschitz 项用 \(\delta\le D^{1-\gamma}\delta^\gamma\) 控制。

真实 EB gauge 为
\[
\psi(r)=\left(\frac{\lambda q}{c}r\right)^p.
\tag{5.4}
\]
在距离尺度 \(0<t\le r_0\)，direct 兼容左侧除以 \(t\) 至多
\[
\left[
\frac q{2c}
\left(r_0^{1-\gamma}+L_D\right)
\right]^p.
\tag{5.5}
\]

### 定理 5：整个结构层的严格 RLEB 变形

若
\[
\boxed{\ q M C_\gamma/c<1\ },
\tag{5.6}
\]
则可取足够小的共同局部工作块（\(D,r_0\) 小），使 (5.5) 严格小于 1。于是 \(F'\) 满足完整局部覆盖、all-pairs RL、真实幂次 EB 及严格 direct RLEB 兼容。

该结论不是“发现一条好分支”。完整 \(J_{\lambda F'}\) 已由图作用给出；真实 EB 已对整个逆纤维证明；all-pairs RL 是 (5.3) 的任意两点估计。

**小初值轨道的留域闭合。** 先围绕任意解点 \(s\) 选工作球 \(B_r(s)\)，使上述 RL、真实 EB 与严格兼容在所需完整工作图块上成立，令其兼容因子为 \(\kappa<1\)、RL 常数为 \(L\)。再取共同初值半径 \(\eta>0\)，满足
\[
\eta+\frac12\left[
\frac{\eta}{1-\kappa}
+\frac{L\eta^\gamma}{1-\kappa^\gamma}
\right]<r,
\tag{5.7}
\]
并使 \(\eta\) 不超过选定的法向／兼容工作阈值（工作球本身已取在 \(|w|\le\rho^p\) 及 EB 的有效 collar 内）。原 RLEB 的局部化预算即保证从 \(B_\eta(s)\) 出发的整条轨道留在该完整工作图块。全域完整 resolvent 覆盖在整个工作球成立，因此没有只核查初值而漏掉后续输入。此处认证的是一个真正共同的小初值邻域，不是仅一条轨道。

**预算边界。** 新 RLEB 证书的有效局部块可能依赖变形尺度。共同实际初值域与真实尾仍由共轭保留到 \(1+\varepsilon\) 倍；不能无证声称新证书也在预先固定的同一宏观 RL/EB 工作块上成立。若最终分类冻结的是“存在某个局部证书”，此构造适用；若冻结证书域和常数，则需额外同域化论证。

## 6. 同一原算子在任意正步长下均不满足 LT all-pairs

### 定理 6：排除 \(\exists\mu>0\)

上述 \(F'\) 不可能在任何 \(\mu>0\) 的完整局部 resolvent 图表中满足 LT all-pairs 必需的局部 Lipschitz 条件。

**证明。** 取 \(x=(y,w)\)、\(u=T'x\)、\(v=(x-u)/\lambda\)。同一个原图在步长 \(\mu\) 的输入是
\[
x_\mu=u+\mu v=
\frac\mu\lambda x+
\left(1-\frac\mu\lambda\right)u.
\tag{6.1}
\]
记 \(\alpha=\mu/\lambda>0\)。由 (3.9) 及 \(S\) 仿射，
\[
d(x_\mu,S)\le
\{\alpha+|1-\alpha|q^p\}|w|,
\tag{6.2}
\]
但
\[
|x_\mu-u|=\alpha|x-u|
\ge\alpha c|w|^\gamma.
\tag{6.3}
\]
当 \(w\to0\) 时，\(x_\mu,u\to(y,0)\)。若完整 \(J_{\mu F'}\) 在该点某邻域是 \(L_\mu\)-Lipschitz 且固定 \(S\)，则以 \(x_\mu\) 的法向投影 \(s_\mu\in S\) 比较，
\[
|x_\mu-u|\le(1+L_\mu)d(x_\mu,S),
\tag{6.4}
\]
与 (6.2)–(6.3) 矛盾。若它根本不良定，则更不可能提供该完整 LT 证书。□

这里排除的是 all-pairs Lipschitz 型 LT 接口，不自动排除所有更早的 relative-to-Fix、仅点态或多值理论。

## 7. 此结构层并非空，也不限于单个公式族

条件 (3.2)–(3.3)、(5.6) 对具有共同加权 \(C^1\)/\(C^{1,1}\) 预算的函数扰动具有严格余量。例如 \(n=1\)，
\[
A(y,z)=a z\,e_1+\widetilde A(y,z),\qquad
B(y,z)=q_0z+\widetilde B(y,z),
\]
只要 \(\widetilde A(y,0)=\widetilde B(y,0)=0\)，且其正常导数足够小，就仍有 \(c>0\)、\(M<\infty\)、\(q<1\) 及 (5.6)。允许任意满足这些预算的函数，不仅是有限个参数。

该层包含 LT 原对象。取未扰动的 \(a=q_0=0.01\)，反射 Lipschitz 常数可用 \(L\le1+2a=1.02\)，线性真实 EB 可取 \(\rho_{\rm EB}=\lambda q_0/a=\lambda\)。故
\[
2\tau(\lambda+\rho_{\rm EB})^2
\le 8(1.02^2-1)\lambda^2/4
=0.0808\lambda^2<\lambda^2,
\]
其中 \(\tau=(L^2-1)/4\)。同时即便用粗常数 \(C_\gamma=5\)，也有 \(q_0 M C_\gamma/c=0.05<1\)。

这说明定理能从一整个带严格余量的普通 LT 结构层出发，经任意小 AW 变形得到严格 RLEB 且所有步长 LT 不可认证的对象。

**但必须保留限定：** 这里的“开放”是该结构层的加权导数拓扑中的开放性；没有证明该结构层在中立 AW/实际尾空间中开放、稠密或余稀。

## 8. 为什么保持线性残差阶的粗化不够

这给出了另一个精确瓶颈。若 \(\gamma<1\)、\(L>0\)，direct 条件
\[
\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t
\]
强迫小尺度 \(\psi(r)\le Cr^{1/\gamma}\)，故真实 EB 强迫
\[
r_F(u)\ge c_0d(u,S)^\gamma.
\tag{8.1}
\]
证明：令 \(a=L/(2\lambda)\)、\(t=(r/a)^{1/\gamma}\)，用 \(\psi\) 单调性。

energy 条件
\[
\tfrac12(t^2+L^2t^{2\gamma})
\le q_E\{t^2+\lambda^2[\psi^{-1}(t)]^2\}
\]
同样强迫 \(\psi^{-1}(t)\ge c_0t^\gamma\)，因为 \(t^{2\gamma}\) 主导 \(t^2\)，故也得到 (8.1)。

若有输出序列 \(u_j\to S\) 满足
\[
0<d(u_j,S)\to0,\qquad r_F(u_j)\le C\,d(u_j,S),
\tag{8.2}
\]
则任意 \(\gamma<1\) 的严格兼容都不可能。

最小例子是 \(T(y,z)=(y,qz)\)，其完整算子
\[
F(y,w)=\{(0,(1-q)w/(\lambda q))\}
\]
满足 \(r_F=(1-q)d/(\lambda q)\)。若只作第 2 节残差/距离双侧保真的非 Lipschitz 粗化，则 (8.2) 仍在；粗化后 \(\gamma=1\) 又失败，因而可能同时离开 LT 与 RLEB。

第 3–6 节的新构造能够越过此障碍，正因为它利用非退化切向漂移，在法向压缩后重新生成了 (8.1)，而没有声称保留原残差阶。

## 9. 当前未解决事项与建议下一步

| 已完成 | 尚缺的精确桥梁 |
|---|---|
| 完整原图共轭及真实尾运输 | 冻结 \(\mathfrak D_e\) 内的同层化；严格尾余量是否稠密 |
| 正常收缩／非退化切向漂移层中的任意对象变形 | 该结构层在中立空间中的位置，而非在自身参数空间中的位置 |
| 幂次真实 EB 与 all-pairs RL 的独立证明 | 预先固定宏观证书工作域时的同域化 |
| 同一原算子所有 \(\mu>0\) 的 LT 排除 | 一般弯曲 \(C^1\) 解流形及退化切向漂移结构推广 |
| 原图 AW 任意接近、共同初值域与尾的小 slack | 上述变形是否足够击穿每个闭 LT 常数层的相对内部 |

另须确认相对纲的分母自身具有足够 Baire 性。若所比较的 RLEB 并类在自身拓扑中已经第一纲，则“LT 在它里面第一纲”可能没有鉴别力；本构造没有解决这一问题。

最有价值的下一工作包不是再造孤立例子，而是：

1. 在无标签动力学层中定义“非退化切向漂移”的坐标不变版本，并确定它何时具有稳定分裂／管状图表。
2. 证明该层的覆盖、稠密或至少非第一纲性质；若不成立，给出排除该层的开放动力学区域。
3. 处理实际尾预算和证书域的同层化。没有这一步，只能得到任意接近的跨层变形，不能得到最终相对纲。

最后，整个最大 atlas 上无条件破坏 LT 不可能：例如 \(S=\{s\}\)、\(e_1=0\) 的共同尾层强迫 \(T\equiv s\)，或 \(K=S\) 强迫 \(T=I\)。这些合法刚性层说明最终定理必须有动力学／解几何分层，而不是无条件“LT 处处第一纲”。
