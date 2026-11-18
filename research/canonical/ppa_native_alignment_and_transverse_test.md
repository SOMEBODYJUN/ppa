# 从原算子出发：全隐式速度对齐与横向线性化的锐判据

## 问题与范围

本页把两个任务分开。第一，用已有自然模型检验 [C320](ppa_two_step_and_directional_residual.md#td-directional) 能否比标量残差提供实际信息，同时直接从原动力学证明收敛。第二，在光滑问题上判定 C320 究竟有没有提供超出原算子横向稳定性的新条件。以下 PPA 都是 \(x-y\in\lambda F(y)\)、固定 \(\lambda>0\) 的原欧氏更新。

<a id="native-alignment"></a>
## 1. C322：原 Cucker–Smale 场上的完整全隐式 PPA

取 \(N\ge2\) 个粒子、每个位置速度属 \(\mathbb R^d\)。记 \(P=(\mathbb R^d)^N\)、\(P_0=\{p\in P:\sum_i p_i=0\}\)，研究移动到质心速度后得到的相对状态 \(X=P\times P_0\)。令 \(\phi:[0,\infty)\to(0,\infty)\) 连续非增，定义原始速度对齐 Laplacian
\[
 (L(q)p)_i=\frac1N\sum_{j=1}^N\phi(\|q_i-q_j\|)(p_i-p_j).
\]
Cucker–Smale 连续系统在此坐标为 \(\dot q=p,\ \dot p=-L(q)p\)。其后退 Euler 恰为固定步长普通 PPA，取
\[
 F(q,p)=(-p,L(q)p),\quad
 S=P\times\{0\},\quad
 (a,b)=(q,p)+\lambda F(q,p).
 \tag{C1}
\]
因此 \(d((q,p),S)=\|p\|\)；位置真实进入下一步的通信权重。F 没有通过任何预解式反演构造出来。

**每一步都有完整输出，且以下估计适用于所有根。** 写 \(D(q)=\max_{i,j}\|q_i-q_j\|\)。由对称性
\[
 \langle p,L(q)p\rangle
 =\frac1{2N}\sum_{i,j}\phi(\|q_i-q_j\|)\|p_i-p_j\|^2,
 \qquad
 \phi(D(q))I\preceq L(q)|_{P_0}\preceq \phi(0)I.
 \tag{C2}
\]
最后使用 \((2N)^{-1}\sum_{i,j}\|p_i-p_j\|^2=\|p\|^2\) 在 \(P_0\) 上成立。(C1) 等价于 \(q=a+\lambda p,\ b=(I+\lambda L(a+\lambda p))p\)。连续自映射
\[
p\mapsto (I+\lambda L(a+\lambda p)|_{P_0})^{-1}b
\]
把半径 \(\|b\|\) 的闭球送入自身，Brouwer 给其不动点（球半径为零时直接取 \(p=0\)）。任一输出都必须解此方程。由 (C2)，每个根满足
\[
 \|b\|\ge(1+\lambda\phi(D(q)))\|p\|,
 \qquad \|q-a\|=\lambda\|p\|.
 \tag{C3}
\]

**一个原模型的耗散预算。** 任取初值 \(x^0=(q^0,p^0)\)，写 \(u_k=\|p^k\|\)、\(D_0=D(q^0)\)、\(s_0=0\)、\(s_k=\lambda\sum_{j=1}^k u_j\)。任意允许轨道都满足 \(u_{k+1}\le u_k\)、\(s_{k+1}-s_k\le\lambda u_0\) 和 \(D(q^{k+1})\le D_0+\sqrt2 s_{k+1}\)。最后一式由 \(\max_{i,j}\|p_i-p_j\|\le\sqrt2\|p\|\) 逐步求和。于是
\[
 u_k-u_{k+1}\ \ge\
 \phi(D_0+\sqrt2 s_{k+1})(s_{k+1}-s_k)
 \ \ge\ \int_{s_k}^{s_{k+1}}\phi(D_0+\sqrt2(r+\lambda u_0))\,dr .
 \tag{C4}
\]
第二不等号因区间内 \(r+\lambda u_0\ge s_{k+1}\)，用 \(\phi\) 非增即可。这个移位处理了全隐式权重取在**后端点**的问题。

若
\[
 \int_0^\infty\phi(D_0+\sqrt2(r+\lambda u_0))\,dr>u_0,
 \tag{C5}
\]
则各轨道的 \(s_k\) 被同一个有限数 \(s_*\) 控制。可取唯一满足左端积到 \(s_*\) 等于 \(u_0\) 的数。由 (C3) 取得统一 \(g=\phi(D_0+\sqrt2 s_*)>0\) 和 \(\eta=(1+\lambda g)^{-1}<1\)。所以对所有 \(k\)，\(u_{k+1}\le\eta u_k\)，且
\[
 \|x^{k+1}-x^k\|
 =\lambda\|F(x^{k+1})\|\le\lambda\sqrt{1+\phi(0)^2}\,u_{k+1}.
\]
总长度至多为 \(\sqrt{1+\phi(0)^2}s_*\)，尾长由 \(\lambda\sqrt{1+\phi(0)^2}\eta u_k/(1-\eta)\) 控制。由完备性，\(x^k\to(q^\infty,0)\)；不同选择可有不同极限。若 \(\int_0^\infty\phi=\infty\)，(C5) 对所有初值及所有固定步长成立。标准 \(\phi(r)=(1+r^2)^{-\beta}\) 的 \(0\le\beta\le1/2\) 属这一情形。该证明无需预先限制位置、步长大小或选定一条近端支。

[Cucker–Smale](https://people.mpi-inf.mpg.de/~mehlhorn/SeminarEvolvability/CuckerSmale.pdf) 给出原模型与通信权重；[Ha–Liu §3](https://sites.math.duke.edu/~jliu/pdf/Ha_Liu_CMS_2009.pdf) 在连续模型中用速度与通信原函数给出 flocking 判据，包括临界指数。这里保留这一经典机制，用移位原函数适配全隐式步及全部根。没有核定全隐式 flocking 的先行性。

<a id="native-sharp"></a>
### 对全体初值的精确通信核边界

对每个 \(N\ge2,d\ge1\) 和固定 \(\lambda>0\)，上述模型中“所有平均速度为零的初值、所有允许根轨道皆有限长收敛”等价于 \(\int_0^\infty\phi(r)\,dr=\infty\)。充分性已证。为证必要性，把粒子分成两簇，每簇内部同位置、同速度，沿一条直线运动。取初始分离 \(a_0\ge0\)，向外相对速度 \(b_0>\int_{a_0}^\infty\phi\)，调整共同速度使加权均值零。两簇质量之和归一为 1，故簇间隐式等式精确为
\[
 a_+-a=\lambda b_+,\qquad b-b_+=\phi(a_+)(a_+-a).
\]
对每个 \(b>0\)，连续函数 \(s\mapsto(s-a)(1+\lambda\phi(s))\) 在 \(s=a\) 为零且趋于无穷，故存在 \(a_+>a\) 的簇保持根。由 \(\phi\) 非增，
\[
 b-b_+\le\int_a^{a_+}\phi(r)\,dr .
\]
沿这些根求和即得 \(b_k\ge b_0-\int_{a_0}^\infty\phi>0\)，位置分离无界，因而点列不收敛。这个必要性是针对全初值、全策略的保证。

甚至对**同一个原模型和初值**，根选择也可能决定是否聚集。取 \(N=2,d=1,\ \phi(r)=(1+r^2)^{-1},\ \lambda=100\)，初始差 \(a_0=0,b_0=1/3\)（个体速度均值为零）。首步分离 \(s\) 解
\[
 \frac{s}{100}+\frac{s}{1+s^2}=\frac13 .
\]
左端在 \(0,1/2\) 分处 \(1/3\) 两侧，在 \(30,31\) 也分处两侧，故有小根 \(s_-\in(0,1/2)\) 和大根 \(s_+\in(30,31)\)。

- 小根得到 \(a_1=s_-,b_1=s_-/100\)，故 \(a_1+100b_1<1\)。若 \(a+100b\le1\)、\(a\ge0,b>0\)，则每个后继都有 \(0<b_+\le b\)、\(a_+\le1\)、\(\phi(a_+)\ge1/2\)，从而 \(b_+\le b/51\)，且 \(a_++100b_+=a+200b_+\le a+100b\)。故所有后继轨道保持在该区域并有限长收敛。
- 大根得到 \(a_1>30,b_1>0.3\)，而 \(\int_{a_1}^{\infty}\phi<1/30\)。上述必要性证明中的速度下界适用于每个后续根，两粒子的分离因此无界。

两粒子连续模型在同一初值下则沿 \(b(a)=1/3-\arctan a\) 趋于有限分离。这由 \(db/da=-\phi(a)\) 得到。此对照说明全隐式离散的全选结论不是连续模型稳定性的直接继承。

<a id="native-strict"></a>
## 2. C322 的 PPA 比较：方向结构提供了什么

在 \(U=\{(a,b):D(a)<D_{\max}\}\)、\(\|b\|\le R\) 的输入窗，任一输出由 (C3) 保证 \(D(q)\le D_{\max}+\sqrt2\lambda R\)。因而取 \(g_R=\phi(D_{\max}+\sqrt2\lambda R)\) 得 A，因子 \(\kappa_R=(1+\lambda g_R)^{-1}\)。步长至多 \(C_Rd(x)\)，其中 \(C_R=\lambda\sqrt{1+\phi(0)^2}\kappa_R\)，故最近零锚反射式可取 \(\omega(t)=(1+2C_R)t\)，满足 Dini。真实残差给出 \(d(y)\le r_F(y)\)，因为 \(F\) 的位置分量正好是 \(-p\)。

同一恒等式直接给 C320 的完整逆像检验。取
\[
K_t=\{v:\|P_qv\|\le\kappa_Rt\}\cap\overline B(0,H(t)/\lambda),
\qquad H(t)=(t+\omega(t))/2.
\]
实际图值都在 \(K_t\) 内；对每个原图值 \(v=F(y)\)，\(\|P_qv\|=d(y)\)。所以完整逆像排除立即成立，无须先估一个全范数的最坏界再倒推速度。

### 同一原图击破最紧的标量残差半径

固定 \(N=3,d=1,\ \phi(r)=(1+r^2)^{-1/2},\ \lambda=1/20\)，取零状态 \(y_*=(q_*,0)\)，\(q_*=(-1,0,1)\)。在 \(P_0\) 上 \(L(q_*)\) 的两特征值为
\[
 g=\tfrac13(1/\sqrt2+2/\sqrt5),\qquad G=1/\sqrt2 ,
\]
对应反对称向量与 \((1,-2,1)\)；取单位向量 \(e_g,e_G\)。对任意充分小 \(t>0\)，输出 \(y=(q_*,t e_G/(1+\lambda G))\) 的合法输入 \(x=y+\lambda F(y)\) 有 \(d(x)=t\)，真残差为
\[
 r(t)=\frac{\sqrt{1+G^2}}{1+\lambda G}\,t.
\]
另一合法输出 \(\widetilde y=(q_*,r(t)e_g/\sqrt{1+g^2})\) 具有同一个真残差，但
\[
 d(\widetilde y)=\frac{\sqrt{1+G^2}}{(1+\lambda G)\sqrt{1+g^2}}\,t>t .
\]
例如 \(G<0.71,g<0.54\) 给分母的平方小于 \(1.4<1.5=1+G^2\)。两条输入输出都趋于同一零状态。任何包含实际图值 \(V_t\) 的原欧氏中心球，至少要容纳第一条图值的范数 \(r(t)\)，因而也纳入第二条。这排除了**所有**该尺度的标量球逆像认证，包括直接用实际图值最大范数、允许另选旧 \(\omega,\psi\) 或收缩因子的方案。这个失效源于不同速度特征方向，而非 \(H\) 的三角不等式过粗。C320 的 \(K_t\) 不混淆这两个方向。

### 另外两项可比旧前提与全部根的实际意义

- **Luke–Tam 同窗参数门失败。** 任意有效线性真残差常数 \(K\) 至少为 \(1/\sqrt{1+g^2}>0.87\)，取固定 \(q_*\) 的弱特征向量方向即得。比较原图点 \(y_*=(q_*,0)\) 与 \(y_\varepsilon=(q_*+\varepsilon e_g,\varepsilon e_g)\)，有
  \[
  \lim_{\varepsilon\downarrow0}
  \frac{-\lambda\langle y_\varepsilon-y_*,F(y_\varepsilon)-F(y_*)\rangle}
       {\|(I+\lambda F)(y_\varepsilon)-(I+\lambda F)(y_*)\|^2}
  =\frac{\lambda(1-g)}{(1-\lambda)^2+(1+\lambda g)^2}>0.011 .
  \]
  因而 Luke–Tam 图块的违约常数 \(\tau>0.011\)，而其同窗参数门 \(\tau(1+K/\lambda)^2<1/2\) 要求 \(\tau<0.0015\)。这里只排除同一步长的这套充分条件。[Luke–Tam，Definition 2 与 Assumption 2(d)](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863)
- **固定零锚的斜弱 Minty 也失败。** 任意固定零锚 \((q_0,0)\) 和小 \(\delta>0\)，令 \(y=(q_0+\delta e,\varepsilon e)\)，单位 \(e\in P_0\)。则 \(\langle F(y),y-(q_0,0)\rangle=-\delta\varepsilon+O(\varepsilon^2)\)，而任意固定对称矩阵 \(V\) 的 \(\langle F(y),VF(y)\rangle=O(\varepsilon^2)\)。因此任一全邻域上的固定零锚 \(V\)-斜弱 Minty 均失败。[Evens–Pas–Latafat–Patrinos，Def. 2.1](https://arxiv.org/pdf/2305.03605)
- **同一模型确实可以多值。** 在上述 \(N,d,\phi,\lambda\) 中令两粒子同位置、同速度，第三个为另一团。给输入团间位置差 \(a=160\) 和速度差 \(b=-3320\)，速度按团大小配成均值零。保持该团对称的输出中，若 \(s\) 为输出位置差，则速度差为 \((s-a)/\lambda\)，方程化为 \((s-a)(1+\lambda/\sqrt{1+s^2})=\lambda b=-166\)。左端在 \(-5,-2,-1,1\) 依次小于、大于、小于、大于 \(-166\)。连续性给至少三个根。每个根决定唯一平均位置固定、平均速度为零的团对称输出。故同一全隐式模型在固定步长下有真实多分支输入，§1 的全选收敛包含这些初值。

<a id="native-transverse"></a>
## 3. C323：光滑零流形上，一个横向检验决定什么

设 \(F:\mathbb R^n\to\mathbb R^n\) 单值，在 \(s_0\) 附近 \(C^1\)。闭目标零集 \(S\) 在 \(s_0\) 附近是 \(C^1\) 嵌入流形，无边界。令切空间 \(E=T_{s_0}S\)、法空间 \(N=E^\perp\ne\{0\}\)、\(D=DF(s_0)\)、\(A=D|_N\)、\(B=P_N A\)，记
\[
 G=I_N+\lambda B,\qquad m=\sigma_{\min}(G).
\]
此处“局部全部根”指所有输出 \(y\) 在指定小的 \(s_0\) 邻域内的真实近端关系。若要覆盖未截断的完整预解式，还需核对无窗外输出；这不能从 Jacobian 推出。

**单一检验。** 存在局部全部根的统一 A 因子 \(\kappa<1\)，当且仅当 \(m>1\)。此时局部输出唯一，且取任何 \(\kappa>1/m\)（\(\kappa<1\)），充分缩窗后同一个条件自动给最近零锚 RL、线性真残差界、C320、几何距离收缩和有限长度。尤其不需要把这几件事逐条当作前件。

**证明。** 以 \(s_0\) 为原点写 \(S\) 的局部图 \(s+h(s)\)，其中 \(s\in E\)、\(h(s)\in N\)、\(h(0)=Dh(0)=0\)。定义 \(\xi(y)=P_Ny-h(P_Ey)\)。充分缩窗时有 \(d(y,S)\le\|\xi(y)\|\le(1+o(1))d(y,S)\)，这里的 \(o(1)\) 对缩窗中的所有 \(y\) 一致。后一不等式由图的 Lipschitz 常数 \(o(1)\) 和与最近零点的正交坐标差得到。由于 \(F=0\) 在图上，沿法向线段的 Taylor 估计给
\[
 F(y)=A\xi(y)+o(1)\|\xi(y)\|,\qquad
 \xi(x)=G\xi(y)+o(1)\|\xi(y)\|\quad (x=y+\lambda F(y)).
 \tag{T1}
\]
第二式中切坐标引起的 \(h\) 变化至多为 \(o(1)\|x-y\|\)。若 \(m>1\)，则 \(B\) 可逆，且 \(I+\lambda D\) 在 \(E\oplus N\) 中分块上三角、对角为 \(I_E,G\)。逆函数定理给唯一局部分支。由 (T1) 得 \(d(y)\le(m^{-1}+o(1))d(x)\)，且 \(\|x-y\|=O(d(x))\)，后一式给线性最近零锚模及其 Dini 可和性。\(A\) 单射，故 \(r_F(y)=\|F(y)\|\ge(\sigma_{\min}(A)-o(1))d(y)\)。

取固定线性观察 \(L=GB^{-1}P_N\)。由 (T1)，\(LF(y)=G\xi(y)+o(1)\|\xi(y)\|\)，故同一窗口内
\[
 \|LF(y)\|\ge(m-o(1))d(y),\qquad
 \|LF(y)\|\le(1+o(1))d(x).
\]
与 P2 的外球相交的观察柱体 \(K_t=\{v:\|Lv\|\le(1+o(1))t\}\cap\overline B(0,H(t)/\lambda)\) 于是验证 C320，因子可任意接近 \(1/m\)。覆盖、A 及线性步界给有限长度和通常的严格初值留域。必要性是在每个单位 \(u\in N\) 上取 \(y=s_0+\varepsilon u,\ x=y+\lambda F(y)\)，这些都是受检局部步。距离对切空间的一阶极限给 \(1\le\kappa\|Gu\|\)，所以 \(m\ge1/\kappa>1\)。

<a id="native-hierarchy"></a>
### 三层锐的收缩因子

在 \(m>1\) 时定义 \(a=\sigma_{\min}(A)>0\)、\(b=\|AG^{-1}\|\)，以及
\[
 c=\|(2(I+\lambda D)^{-1}-I)|_N\|.
\]
以下“锐下确界”是相应比例不等式的最佳缩窗极限。先允许比例上界大于等于 1；能作为严格收缩证书还要求该极限严格小于 1。缩窗极限不保证在某个正半径上达到。

| 检验 | 比例上界的锐下确界 |
|---|---|
| A 或 C320 的图值集合 | \(m^{-1}\) |
| 包含实际 \(V_t\) 的最紧原欧氏中心球，再对完整相关输出作逆像检验 | \(b/a\) |
| 正式 RLEB 的最近零锚反射加标量整窗兼容 | \((1+c)/(2\lambda a)\) |

第二行：由 (T1) 得 \(F(y)=AG^{-1}\xi(x)+o(1)d(x)\)。球半径 \((b+\varepsilon)t\) 足以包含实际 \(V_t\)，且 \(\|F(y)\|\ge(a-\varepsilon)d(y)\)，故可认证任何大于 \(b/a\) 的因子。反向沿输入法向的最大奇异方向逼出半径至少 \((b-\varepsilon)t\)，再沿 \(A\) 的最小奇异方向取输出 \(y=s_0+[(b-\varepsilon)/(a+\varepsilon)]t\,u\)，它在球内且到 \(S\) 的距离趋近所述比例。必要时略缩小正参数保证球的严格纳入。

第三行：任取近窗输入的最近零点 \(p\)。相对 \(p\) 对局部反射展开，因 \(x-p\in N_p S\) 且 \(N_p S\to N\)，可取 \(\omega(t)=(c+\varepsilon)t\)；上面的误差界可用 \(\psi(s)=s/(a-\varepsilon)\)。反向先用达到 \(c\) 的法向单位向量取 \(x=s_0+t u\)，最近点 \(p=s_0+o(t)\) 且 \(d(x)\le t\)，故任何有效非减 \(\omega(t)\) 在全部充分小尺度至少为 \((c-\varepsilon)t\)。再沿 \(A\) 的最小奇异方向以距离近似 \(s/(a+\varepsilon)\) 的合法输出检验 \(\psi(s)\)，得到 \(\psi(s)\ge (1-o(1))s/(a+\varepsilon)\)。两者相乘收紧窗，给第三行下确界。因此若任一个后两行的下确界达到或超过 1，对应方法无法给任何严格收缩因子。

三层关系为
\[
 \frac1m\le\frac ba\le\frac{1+c}{2\lambda a}.
\]
第一式由 \(\|AG^{-1}u\|\ge a\|G^{-1}u\|\)；第二式由 \(\lambda DG_{\rm full}^{-1}=I-G_{\rm full}^{-1}\)、\(G_{\rm full}=I+\lambda D\)，限制到法向输入后 \(DG_{\rm full}^{-1}|_N=AG^{-1}\)，再用反射与单位输入的三角不等式。

**含义。** 光滑的这一类问题上，C320 与普通横向收缩实际上是同一个局部判据；因此不能把这里的 \(M\) 包装成超出横向稳定性的新机制。上面的锐比较量化了两次信息损失：第一次压缩为原欧氏残差范数，第二次再用锚定反射推出的外球。Cucker–Smale 例已在第一次失败，而非只在旧的三角不等式失效。

<a id="native-breadth"></a>
## 4. 外部路线与取舍

| 路线 | 可复用的思路 | 与本页的关系 |
|---|---|---|
| [Ha–Liu 的 flocking 分析](https://sites.math.duke.edu/~jliu/pdf/Ha_Liu_CMS_2009.pdf)，§3 | 从速度耗散和通信原函数构造组合量，解决位置增长削弱谱隙的循环。 | 已移植到全部根的后退 Euler；原动力学与耗散思想有明确先例。 |
| [Zeng 的非孤立解 Newton 法](https://arxiv.org/pdf/2101.09180)，arXiv v4，§4 | 识别零流形的横向 Jacobian，使用秩截断 Newton 得局部速率。 | 借其横向观点，但 PPA 不作伪逆更新；C323 的门是 \(I+\lambda B\) 的最小奇异值。 |
| [Goebel 的逐点渐近稳定](https://webpages.math.luc.edu/~rgoebel1/publications/journals/Goebel13submission.pdf)，§2–3 | 区分趋于平衡集与趋于其中一个点，对多值离散系统用逐点稳定或集合 Lyapunov。 | 用于避免把距离趋零当作点列收敛；C322 由物理位移预算直接选择极限。 |
| [Evens 等的斜弱 Minty](https://arxiv.org/pdf/2305.03605)，§2.1 | 对某个零锚保留带矩阵权重的残差二次型。 | C322 的位置搬运与速度对齐不能压成这一固定锚二次式；§2 提供直接障碍。 |
| [Maddison 等的 Hamiltonian descent](https://optimization-online.org/wp-content/uploads/2018/09/6826.pdf)，§3.1 式 (33) | 从动力学与能量出发构造全隐式算法。 | 研究库已有自由粒子和秩亏模型；本轮优先保留位置真实反作用于耗散的 Cucker–Smale 例，避免把已有三角模型改参数当推进。 |

本页把 C320 的可用性检验和抽象统一问题分开。原对齐模型证明一个具体机制能同时处理输入覆盖、距离衰减和物理位移；C323 在光滑层给出单一可核原算子门。两者均未证明存在一个原生性质，既容纳全部旧非线性 RLEB，又严格强于 A+B。该主命题仍开放。Astra Max 与主代理分别推导了全隐式对齐预算和标量球严格分离。主代理另逐项复核了代理提供的光滑横向判据、临界核的完整分支与同初值分歧。外部优先性未裁定。
