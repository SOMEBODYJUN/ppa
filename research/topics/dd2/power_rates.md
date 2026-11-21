# 原纯幂数据的最坏距离、点误差与实际尾长

本页对应 S06.08。C469–C471 已经三席独立重构及实际终稿、身份和图边复核。
固定全部原数据后，本文求自由闭目标完整类的共同上界，并以实际完整图取等；
两个幂标签本身不决定一个固定算子的唯一速度。

[S06.10的一般函数恢复](functional_power_recovery.md)另以C472从连续非减D和可逆原ψ直接证明混支准确W；纯幂只代本页BR标量渐近，便恢复C470的包络与率。该证明不调用本页WT作前提，也不改C469–C471身份；原预设φ、点Q方向和结构类边界仍按本页合同。

<a id="power-rate-contract"></a>
## 1. 对象、目标和最优性合同

固定 \(p,q,K,\lambda>0,\ M\ge0\)，记
\[
D(t)=Mt^p,\quad\Phi=-D,\quad\psi(\rho)=K\rho^q,\quad
m=1/q,\quad c=\lambda K^{-1/q},\quad h=K/\lambda^q=c^{-q}.
\tag{OR1}
\]
沿用E0：有限维欧氏空间、闭非空 \(S\subseteq\operatorname{zer}F\)，
每条允许边有某个同一最近输入锚，输出使用完整真残差 \(\rho=d(0,F(y))\)。
正向适用于所有受检允许边；锐性类包含二维，取精确零集、完整闭图F、
全域非空的全部 \(J_{\lambda F}\)。反向允许F在非输出点为空，
不转授连续单值或指定S的受限类。先取U=Vψ=H且Dψ=[0,∞)，局部版本另证明首出边预算。

原自由类共同小窗的严格降距门是
\[
\mathcal G:\quad M=0\quad\text{或}\quad p>2/q\quad\text{或}\quad
\begin{cases}
p=2/q,\ M<c^2/2,&q<1,\\
p=2,\ M<T(K/\lambda),&q=1,\\
p=2/q,\ M<c^2,&q>1.
\end{cases}
\tag{OR2}
\]
其中 \(T(L)=(1-L)/L^2\) 于L≤1/2，\(T(L)=1/(2L^2)\) 于L≥1/2。
这是[WR1/CK](../../canonical/dd2_power_defect_finite_length.md#dd2-power-condition-weakening)的同一合同。
M=0时p退出。坏侧已有同图任意小保距轨道，不能保证共同趋零率。
更强固定Φ、更紧的额外目标或具体好图仍须按自己的合同判断。

固定好门后，取使下述估计成立的小窗[0,R]。把数据导出的最坏一步记作
\(\mathcal M_D\)，与预设目标φ分开。若φ由这份数据对整个自由完整类认证，
必有 \(\mathcal M_D\le\varphi\)，其必要性由C469的完整图实现证明。
全部匹配图都保这样的原目标；若另加更紧φ作为图约束，必要性须另验。

分别使用
\[
t_k=d(x^k,S),\quad e_k=\|x^k-x^\infty\|,\quad
\mathcal L_k=\sum_{j\ge k}\|x^{j+1}-x^j\|.
\tag{OR3}
\]
实际尾允许扩展值+∞；点误差只在点极限已经证明后评价。
对所讨论的非零误差序列u（t、e或实际尾），Q阶及系数指
\(\limsup u_{k+1}/u_k^\omega\)，Q线性比指ω=1的比，
R底数指 \(u_k=O(r^k)\)。终止轨道更快，零初值驻定，不对零分母取比。
最优性属于固定数据类的共同保证，不是每个图都必须按最坏率运行。
同一参数、原Φ/ψ与已认证φ下，完整J=P_{\{0\}}、F=(J⁻¹−I)/λ
使所有输入一步到0，全部边锚积0、输出真ρ0，故通过原合同。
C469从同一正初距却给无穷匹配链，这直接证明固定图速度并不由p、q唯一指定。


<a id="power-greedy-realization"></a>
## 2. C469-v1：精确一步包络的同图逐步实现

设 \(G_m(a)=a^2+c^2a^{2m}\)，定义
\[
B(t)=\frac{t+\sqrt{t^2+4D(t)}}2,\quad
\mathcal M_E(t)=G_m^{-1}(t^2+2D(t)),\quad
\mathcal M_B(t)=hB(t)^q,\quad
\mathcal M_D(t)=\min\{\mathcal M_E(t),\mathcal M_B(t)\}.
\tag{GR1}
\]
在好门小窗，\(\mathcal M_D\)连续严格增，零处为零，正尺度有
\(0<\mathcal M_D(t)<t\)。原边满足
\(ca^m\le s,\ a^2+s^2\le t^2+2D,\ s(s-t)\le D\)，故 \(a\le\mathcal M_D(t)\)。
这里只对原非减纯幂模合法使用 \(\rho\le s/\lambda\)。
严格门亦可在本页直接核：令u=ct^m，则
\(\mathcal M_E(t)<t\iff 2D(t)<u^2\)，
\(\mathcal M_B(t)<t\iff u>t\ \text{且}\ D(t)<u(u-t)\)。
两条件取并，再按u/t于q<1、q=1、q>1分别趋0、恒c、趋∞，
就得到OR2的全部好侧；q=1的准确系数为
\(\max\{c^2/2,c(c-1)\}=T(K/\lambda)\)。


固定任意 \(0<t_0\le R\)，令
\[
r_0=t_0,\quad r_{j+1}=\mathcal M_D(r_j),\quad
\sigma_j=c r_{j+1}^m,\quad X_0=0,\quad X_{j+1}=X_j+\sigma_j,\quad x_j=(X_j,0).
\tag{GR2}
\]
连续严格下降给 \(r_j\downarrow0\)。按活动分支放置锚：
\[
(P_j,Y_j)=
\begin{cases}
\left(\sigma_j-D(r_j)/\sigma_j,\;
\sqrt{r_j^2-(\sigma_j-D(r_j)/\sigma_j)^2}\right),&
\mathcal M_D(r_j)=\mathcal M_E(r_j),\\
(r_j,0),&\mathcal M_D(r_j)=\mathcal M_B(r_j),
\end{cases}
\qquad z_j=(X_j+P_j,Y_j).
\tag{GR3}
\]
交界两式一致。在能量支，\(\sigma_j\le B(r_j)\)，且
\[
r_{j+1}^2-(r_j-\sigma_j)^2
=2[D(r_j)-\sigma_j(\sigma_j-r_j)]\ge0.
\]
加上D≥0、\(r_{j+1}<r_j\)，得
\(\sigma_j/2<P_j\le\sigma_j,\ P_j\le r_j\)。
所以根号为实数，锚到输入和输出分别恰距 \(r_j,r_{j+1}\)。
在步帽支，\(\sigma_j=B(r_j)\)，且
\[
r_{j+1}\le B(r_j)-r_j.
\tag{GR4}
\]
这是由 \(\mathcal M_B\le\mathcal M_E\) 和
\(r_j^2+2D(r_j)-B(r_j)^2=(B(r_j)-r_j)^2\) 得到。
该锚到输入距 \(r_j\)，到输出距不小于 \(r_{j+1}\)。
两支都有 \(0<P_j\le\sigma_j\)，锚的水平坐标严格增。

若 \(\sum\sigma_j<\infty\)，将极限 \(z_\infty=(\sum\sigma_j,0)\) 加入
\(S=\{z_j\}\cup\{z_\infty\}\)；否则取 \(S=\{z_j\}\)。
前者的锚只累积到已加入的极限，后者的锚水平趋无穷，故S均非空闭。

**全体最近性。** 对轴上(X,0)，相邻锚平方距差
\[
\|(X,0)-z_{j+1}\|^2-\|(X,0)-z_j\|^2
\tag{GR5}
\]
是斜率严格负的一次函数。能量支在 \(X_{j+1}\) 打平；
步帽支在 \(X_j\) 为正、在 \(X_{j+1}\) 非正，交点落于该步区间。
在 \(X=X_k\) 逐个相邻比较，即排除全部早锚和晚锚。
有限情形再取晚锚的极限，排除极限锚更近。
于是 \(z_k\in P_S(x_k)\)，真实距离为 \(r_k\)。
最近锚可并列；每边选 \(z_k\)，未加强为全锚条件。

完整定义
\[
J=P_S\cup\{(x_j,x_{j+1}):j\ge0\},\qquad
F=\lambda^{-1}(J^{-1}-I).
\tag{GR6}
\]
投影全域非空且闭，附加边若有有限积点，只能是已有的
\((z_\infty,z_\infty)\)。故J/F闭图，\(J=J_{\lambda F}\)完整，
精确 \(\operatorname{zer}F=S\)，零输入驻定。
每个 \(x_{j+1}\notin S\) 只有前像 \(x_j\)，所以
\[
\rho_{j+1}=\sigma_j/\lambda,\qquad
r_{j+1}=K\rho_{j+1}^q,\qquad
\langle x_j-x_{j+1},x_{j+1}-z_j\rangle=-D(r_j).
\tag{GR7}
\]
投影边取其输出作最近输入锚，锚积、输出距和真ρ皆为零。
全部完整边符合原数据，所有距离窗对全部输出不变。
所有轨道要么沿链，要么某次投影后驻定。

因此每个初距 \(t_0\) 可选一个图，同一实际轨道同时在所有j达到
\(t_j=\mathcal M_D^j(t_0)\)。图可依赖 \(t_0\)，不随j更换，
也未声称一个图对所有连续初距同时取等。
有限长度时实际点沿同向直线走，
\[
e_j=\mathcal L_j=\sum_{\ell\ge j}\sigma_\ell .
\tag{GR8}
\]
若和发散，点沿直线无界而距离仍趋零。逐尺度取 \(t_0=t\) 也证明：
原数据对完整自由类认证的φ必支配 \(\mathcal M_D\)。


<a id="power-complete-fibers"></a>
### 2.1 S06.09：把完整关系逐点写成原算子

C469的F不是仅在选定边上指定图值。令 \(V=\{x_j:j\ge1\}\)，
全部顶点互异且 \(V\cap S=\varnothing\)。GR6等价于下面的逐点公式：
\[
F(y)=
\begin{cases}
\{v\in H:2\lambda\langle v,z-y\rangle\le\|z-y\|^2
                \ \text{对全部 }z\in S\},&y\in S,\\
\{(x_{j-1}-x_j)/\lambda\},&y=x_j,\ j\ge1,\\
\varnothing,&y\notin S\cup V .
\end{cases}
\tag{FX1}
\]
第一行是一个完整闭凸纤维，含0；它只描述此构造的投影底图原值，
不把S假设为凸集。事实上，对任意x=y+λv，展开平方距离给
\[
y\in P_S(x)
\iff y\in S\ \text{且}\quad
2\lambda\langle v,z-y\rangle\le\|z-y\|^2\quad(\forall z\in S).
\tag{FX2}
\]
第二行来自正输出恰有唯一链前像，且不可能收到投影边；
第三行排除了所有未列明的值。反代 \(x-y\in\lambda F(y)\)，
第一行精确恢复P_S，第二行精确恢复所列链边，除此没有任何额外近端根。
特别F在初链点x₀为空，完整J(x₀)仍有投影和链输出；
近端方程评价的是F(y)，不能把“原图处处有值”误当成近端覆盖的必要条件。
原ψ只在实际输出真残差上评价，不在这些空纤维处代入无穷。

完整闭性亦不是逐个纤维闭就足够：P_S的图由S闭和距离连续性直接闭；
GR6的附加边若有有限积点只在可和情形落到 \((x_\infty,x_\infty)\)，
已在投影底图。再经线性同胚
\((x,y)\mapsto(y,(x-y)/\lambda)\) 得到F全图闭。
零图值只可能在S，且S全含0值，故零集精确；
正输出真残差恰 \(s/\lambda\)，S上真残差为0。

这个固定图的全部选择也能逐点列出：从链外输入先投影后驻定；
从x_j可投影后驻定，也可继续x_(j+1)；
若始终选择链后继，整条轨道就是已构造无限链的后缀。
没有在不同k更换F、S或工作窗。全空间全部输入均有完整输出，
任意距离窗不变；有限W的局部位置结论只按WT5的严格预算调用，
不把全空间例直接宣称为任意预定位置窗内不变。

因此S06.09中“达到”的范围是：
C469在每个初距给一个真实算子，同时达到全部时刻的最坏距离；
q>1/2时还同时达到点误差、实际尾及RT按相应误差量定义的全部最佳常数。
q≤1/2的同向链实现的是准确距离率和无穷实际长度，点本身逃逸；
原统一类没有共同点收敛率可供达到。
C471的最佳点Q系数用QB2的另一完整变号链达到，
其投影底图和唯一正输出纤维同样由FX1核验；
τ≥1/2时用一族图排除有限共同系数，未捏造一个“无穷最优点比”图。

<a id="power-active-branches"></a>
## 3. 活动分支及标量递推

足够小窗可使活动分支固定。准确步帽条件为
\[
\mathcal M_B\le\mathcal M_E
\quad\Longleftrightarrow\quad hB^{q+1}\le D .
\tag{BR1}
\]
等号任选一支。

| OR2好参数情形 | 足够小窗的活动分支 |
|---|---|
| M=0，任意q | 能量 |
| 0<q<1 | 能量 |
| q=1，M>0，p>2 | 能量 |
| q=1，p=2，M>0 | 令L=K/λ、b=(1+sqrt(1+4M))/2；(1−L)b≥1时步帽，否则能量 |
| q>1，M>0，p<q+1 | 步帽 |
| q>1，M>0，p>q+1 | 能量 |
| q>1，M>0，p=q+1 | M>h时步帽，M≤h时能量 |

M=h的末行仍为能量，因为B>t。q>1且p≤2时用B的幂主项判BR1；
p>2时用B/t→1比较Mt^p和ht^(q+1)。其余由q<1的零端量级或q=1齐次式得出。
全表始终保OR2，未把坏参数列成正面。

在 \(0<q<1\)，令
\[
\nu=2m-2,\quad
M_*=\begin{cases}M,&p=2m,\\0,&M=0\text{ 或 }p>2m,\end{cases}
\qquad \gamma_*=c^2/2-M_*>0 .
\]
根方程先给 \(\mathcal M_D/t\to1\)，再由
\((t-a)(t+a)=c^2a^{2m}-2D(t)\) 得
\[
\mathcal M_D(t)=t-\gamma_*t^{1+\nu}+o(t^{1+\nu}),\qquad
r_j\sim(\nu\gamma_*j)^{-1/\nu}.
\tag{BR2}
\]
后一式来自负ν次幂增量趋于 \(\nu\gamma_*\)。
M>0时p≥2m，所以 \(\sum D(r_j)<\infty\)，因p/ν≥m/(m−1)>1。

在q=1，设L=K/λ，并记
\[
b_\sigma=\frac{1+\sqrt{1+4\sigma}}2,\qquad
\kappa_\sigma=\min\{Lb_\sigma,\;
L\sqrt{(1+2\sigma)/(1+L^2)}\}.
\tag{BR3}
\]
p=2给 \(\mathcal M_D(t)=\kappa_Mt\)。
M=0或p>2时零端系数为 \(\kappa_0=L/\sqrt{1+L^2}\)；
M>0,p>2有 \(\mathcal M_D(t)/t=\kappa_0[1+O(t^{p-2})]\)。

在q>1的非临界好侧M=0或p>2/q，定义
\[
(\beta,b_*)=
\begin{cases}
(1,1),&M=0\text{ 或 }p>2,\\
(1,b_M),&M>0,\ p=2,\\
(p/2,\sqrt M),&M>0,\ 2/q<p<2,
\end{cases}
\qquad\omega=q\beta>1 .
\]
则
\[
B(t)\sim b_*t^\beta,\qquad \mathcal M_D(t)\sim h b_*^q t^\omega .
\tag{BR4}
\]
能量活动时必M=0或p>2，根方程给同一首项ht^q；
相同首项不等于相同活动分支。

在q>1好临界p=2/q、0<M<c²，记
\[
\tau=\sqrt M/c,\qquad r_*=\tau^q .
\]
步帽支给
\[
\mathcal M_D(t)=r_*t[1+O(t^{1-1/q})],\qquad B(t)\sim\sqrt M\,t^{1/q}.
\tag{BR5}
\]
q≥1好侧先有共同几何κ<1，因此 \(\sum D(r_j)<\infty\)。
M=0时该和直接为零。

BR3/BR5的正次修正不丢失准确R底数：若
\(\mathcal M_D(t)=rt[1+O(t^\delta)]\)，先以任意κ∈(r,1)缩窗给
\(r_j\le\kappa^jt_0\)，再以
\[
\prod_j(1+C r_j^\delta)\le
\exp\!\left(\frac{Ct_0^\delta}{1-\kappa^\delta}\right)
\tag{BR6}
\]
控制乘积。全部实际距为O(r^j)；相对修正绝对可和、各项正，
故匹配递推的 \(r_j/r^j\) 趋正有限常数。并非每个正尺度都可删除a≤rt中的次项。

<a id="power-exact-tail"></a>
## 4. C470-v1：准确全尾、点误差包络与局部化

在固定活动分支的小窗定义
\[
W(t)=\sum_{j\ge0}c[\mathcal M_D^{j+1}(t)]^m,\qquad W(0)=0 .
\tag{WT1}
\]
BR2–BR5给W(t)<∞（t>0）当且仅当q>1/2。
低半阶的匹配链实际长无穷，不能据此宣称一般点收敛。
有限侧W非减且连续、W(0)=0；每项连续，整个窗由可和的W(R)逐项支配。

**能量支的全部有限前缀。** 固定N步受检前缀，实距为d₀,…,d_N，
d₀=t。逐步比较给 \(d_j\le r_j=\mathcal M_D^j(t)\)，且d不增。
仅为数列比较，令 \(\widehat d_j=d_j\)（j≤N），此后为0。
不要求人工跳零是原近端步。置
\[
Z_j=\widehat d_j^2-\widehat d_{j+1}^2+2D(r_j),\qquad
G_j=r_j^2-r_{j+1}^2+2D(r_j)=c^2r_{j+1}^{2m}.
\tag{WT2}
\]
D非减给已受检步 \(s_j^2\le Z_j\)。
Z≥0，G非增，两列具有同一有限总和 \(t^2+2\sum D(r_j)\)，且
\[
\sum_{j<n}(Z_j-G_j)=r_n^2-\widehat d_n^2\ge0 .
\tag{WT3}
\]
任意z>0，由G非增，
\[
\sum(G_j-z)_+=\sup_n\sum_{j<n}(G_j-z)\le\sum(Z_j-z)_+ .
\]
等总和遂给 \(\sum\min(Z_j,z)\le\sum\min(G_j,z)\)。
直接恒等式 \(\sqrt v=\frac14\int_0^\infty\min(v,z)z^{-3/2}\,dz\)
和非负求和换序给
\[
\sum_{j<N}s_j\le\sum\sqrt{Z_j}\le\sum\sqrt{G_j}=W(t).
\tag{WT4}
\]
这重构C458的零缺陷比较机制；没有把原C458的身份悄悄改为负缺陷版本。

**步帽支及首出边。** 纯步帽时 \(c r_{j+1}^m=B(r_j)\)，
直接用 \(s_j\le B(d_j)\le B(r_j)\) 也得WT4。
在有限W侧，若位置域为开U，取x⁰∈U_R，先保U_R输入非空覆盖、
所有允许边（含拟出界输出）的原锚/输出真模合同，并取
\[
W(t_0)<d(x^0,U^c).
\tag{WT5}
\]
对含第一条拟出界边的有限前缀先用WT4，严格预算排除末输出离开U，
此后才继续调用覆盖。于是全部选择无限续接、留域、有限长，
距离趋零、闭S识别极限；严格预算使含整轨及极限的闭球仍在U，
故 \(x^\infty\in S\cap U\)。
若已经知道路径全程合法，尾估计无需把WT5再当必要条件。

全空间自由完整类中，C469从每个给定初距给实际同图取等。
故W是最小共同全尾界；有限侧同图e=实际尾，W亦是以当前距为自变量的最小共同点误差界。
全空间低半阶的无限续接另由覆盖及下降保距窗保证。
固定初距t₀时所有合法轨道的距离均有下式第一界；其余界限于W有限侧：
\[
t_k\le\mathcal M_D^k(t_0),\qquad
e_k\le\mathcal L_k\le W(t_k)\le W(\mathcal M_D^k(t_0)),
\tag{WT6}
\]
且一个依赖t₀的完整图同时在每个k取等。
这不是每个固定图都达到最坏界，也不是更紧目标的必要性。

WT4仅用标量约束。将一条受检边接上从a出发的匹配标量尾，
仍能比较，故有限W侧另得 \(s+W(a)\le W(t)\)。
该最优距离支付限于本页的单调纯幂预算、好门及固定活动支，
不外推为任意原函数或任意有限长度图的必要证书。

<a id="power-sharp-rates"></a>
## 5. C470-v1：三种误差量的准确共同速率

以下固定全部原数据和OR2好门。所有上界同时适用于全部合法允许选择，
锐性由C469为给定初距构造的一个完整图、同一条无限轨道给出。
有限步终止与零初值按更快情形处理；低半阶只写已经定义的距离率。

### 5.1 次线性模：0<q<1

沿用BR2的 \(\nu=2m-2,\gamma_*>0\)。对全部轨道，
\[
\limsup_{k\to\infty} k^{1/\nu}t_k
 \le(\nu\gamma_*)^{-1/\nu}.
\tag{RT1}
\]
C469的距离极限恰等右侧，所以指数和该归一渐近常数均不能提高。
当 \(q>1/2\) 时，令 \(\alpha=2-m>0\)。由
\[
\frac{c\,\mathcal M_D(t)^m}
 {t^\alpha-\mathcal M_D(t)^\alpha}
 \longrightarrow C_*:=\frac{c}{\alpha\gamma_*}
\]
逐项夹住尾和并望远镜求和，得
\[
W(t)\sim C_*t^\alpha,\qquad
\limsup k^{\alpha/\nu}e_k
 \le \limsup k^{\alpha/\nu}\mathcal L_k
 \le C_*(\nu\gamma_*)^{-\alpha/\nu}.
\tag{RT2}
\]
C469同图同时达到两种末端常数。距离指数与点/尾指数分别是
\(q/[2(1-q)]\) 与 \((2q-1)/[2(1-q)]\)。
当 \(q\le1/2\) 时W为无穷；不得把RT2的正α公式延到该域，
也没有一般点收敛率。旧PR7剪切仍证明相同指数，未被改写成最优常数见证。

### 5.2 线性模：q=1

令 \(\sigma_*=M\)（p=2），其余好侧即M=0或p>2取0，
并记
\[
\kappa_*=\kappa_{\sigma_*},\qquad
C_*=\frac{\kappa_*}{L(1-\kappa_*)},\qquad L=K/\lambda .
\tag{RT3}
\]
M=0或p=2时准确有 \(\mathcal M_D(t)=\kappa_*t,\ W(t)=C_*t\)；
M>0,p>2时 \(W(t)\sim C_*t\)。后者由
\(\sigma_j=c r_{j+1}\)、BR6的几何控制及每个固定j的极限求和得到。
因此距离、点误差、实际尾均为
\[
t_k,e_k,\mathcal L_k=O(\kappa_*^k).
\tag{RT4}
\]
这里保留准确R底数，而不是只写任意大于它的底数。
匹配链 \(t_k/\kappa_*^k\) 趋正有限常数，
且 \(e_k=\mathcal L_k\sim C_*t_k\)，证明这三个R底数都不能缩小。

距离有 \(\limsup t_{k+1}/t_k\le\kappa_*\)；
实际尾也有 \(\limsup\mathcal L_{k+1}/\mathcal L_k\le\kappa_*\)。
证明后一条时使用
\(\mathcal L_{k+1}\le W(t_{k+1})\le(C_*+o(1))L s_k\)
及 \(\mathcal L_k=s_k+\mathcal L_{k+1}\)。
齐次M=0或p=2情形这两个比在每步就至多κ*，且同图取等。
点误差的R结论不能一概升级为每步Q线性，见C471的具体反例；
这里没有声称每一个固定L、M都缺少点Q保证。

### 5.3 强幂模的非临界好侧：q>1，M=0或p>2/q

沿用BR4的 \(\beta,b_*,\omega=q\beta>1\)。有
\[
\limsup\frac{t_{k+1}}{t_k^\omega}\le h b_*^q,
\qquad W(t)\sim b_*t^\beta .
\tag{RT5}
\]
后式从首项 \(c\mathcal M_D(t)^m\sim b_*t^\beta\) 得到；
记匹配步函数σ(u)=c M_D(u)^m；由BR4，σ(M_D(u))/σ(u)→0。
所有后继尺度u≤t，故零端上确界比ε(t)→0统一控制整尾，
后项和相对首项至多ε(t)/(1−ε(t))→0。
对一般实际轨道，由真残差界及原步帽，
\[
s_{k+1}\le B(t_{k+1})
 \le (b_*h^\beta+o(1))s_k^\omega .
\tag{RT6}
\]
取足够小尾段先给固定严格几何步比，再以RT6强化：
\(\sum_{j>k}s_j=O(s_k^\omega)=o(s_k)\)。
三角不等式的上下界于是给
\(e_k/s_k\to1,\ \mathcal L_k/s_k\to1\)，并推出
\[
\limsup\frac{e_{k+1}}{e_k^\omega}\le b_*h^\beta,\qquad
\limsup\frac{\mathcal L_{k+1}}{\mathcal L_k^\omega}
 \le b_*h^\beta .
\tag{RT7}
\]
C469的匹配步在能量支或步帽支都达到RT5–RT7的常数，
因此这里的距离、点和实际尾的共同Q阶均是最优的ω。
M>0时 \(\omega=q\min\{1,p/2\}\)，M=0时ω=q；
不能从模指数q单独推所有正缺陷情形的Q阶为q。

### 5.4 强幂模的正缺陷好临界：q>1，p=2/q，0<M<c²

沿用 \(\tau=\sqrt M/c,\ r_*=\tau^q\)。BR5–BR6与步帽尾和给
\[
W(t)\sim\frac{\sqrt M}{1-\tau}t^{1/q},\qquad
t_k=O(r_*^k),\quad e_k,\mathcal L_k=O(\tau^k).
\tag{RT8}
\]
例如对每个固定j，
\(B(\mathcal M_D^j(t))/t^{1/q}\to\sqrt M\,\tau^j\)；
缩窗先取任意κ∈(r*,1)，由 \(B(u)\le C u^{1/q}\)
得到可和的几何支配，故该极限可求和。
C469同图有 \(t_k/r_*^k\) 趋正有限常数、
\(e_k=\mathcal L_k=W(t_k)\)，三个底数与尾函数首项均准确。
距离的limsup Q比至多r*；实际尾的limsup Q比至多τ，
后者可由 \(\mathcal L_{k+1}\le W(t_{k+1})
 \le[\tau/(1-\tau)+o(1)]s_k\) 求得。
点误差的逐步比有额外几何边界，不能把τ直接当其共同Q比。

### 5.5 速率表的量词和范围

| 原数据好侧 | 准确共同距离率 | 准确共同点误差/实际尾率 |
|---|---|---|
| 0<q≤1/2 | \(k^{-q/[2(1-q)]}\) 及RT1常数 | 无一般点收敛或有限长保证 |
| 1/2<q<1 | \(k^{-q/[2(1-q)]}\) | \(k^{-(2q-1)/[2(1-q)]}\)，常数见RT2 |
| q=1 | R底数κ*，距离Q比κ* | R底数κ*；尾Q比κ*，点Q另核 |
| q>1，M=0或p>2/q | Q阶ω、系数 \(h b_*^q\) | Q阶ω、系数 \(b_*h^\beta\) |
| q>1，p=2/q，0<M<c² | R底数τ^q、距离Q比τ^q | R底数τ；尾Q比τ，点Q另核 |

表中多项式率指共同上界及匹配图的实际等价量，不声称每个固定图都相等。
每个好侧最强的共同结论其实是WT6的准确全时刻包络，
本表是其渐近表达。p、q之外还必须固定M、K、λ、原下界、预设目标与对象类；
坏侧已有实际不趋零图，较强给定φ或指定凸目标不能继承这些反向结论。
S12的残差、最佳迭代及遍历复杂度尚按原清单另验。

<a id="power-point-q-boundaries"></a>
## 6. C471-v1：准确R速度与逐步点误差的边界

### 6.1 强幂好临界的点Q系数

固定RT8的全部数据和自由完整类。若 \(0<\tau<1/2\)，由
\[
e_{k+1}\le W(t_{k+1})
 \le\left[\frac{\tau}{1-\tau}+o(1)\right]s_k,\qquad
e_k\ge s_k-e_{k+1}
\]
得到
\[
\limsup_{k\to\infty}\frac{e_{k+1}}{e_k}
 \le\frac{\tau}{1-2\tau}.
\tag{QB1}
\]
此为最佳共同limsup系数。若τ≥1/2，整个类没有有限共同limsup系数。
因此全类共同保证点Q线性的准确门为τ<1/3。
所有 \(0<\tau<1\) 仍保RT8的准确R底数τ，二者不矛盾。

**完整有符号直线链。** 取 \(0<g<1/2,\ g\le\tau\)，令
\[
t_j=g^{qj}t_0,\quad s_j=gc\,t_j^m,\quad
x_0=0,\quad x_{j+1}=x_j+\varepsilon_j s_j,\quad
p_j=x_j+\varepsilon_j t_j,\quad
\varepsilon_j\in\{-1,1\}.
\tag{QB2}
\]
s的比恰为g，链有极限x∞。令
\(\delta=(1-2g)/(1-g)>0\)，缩小t₀使 \(\delta s_0>3t_0\)。
因为m<1，该严格不等式逐步保持。任意i<j（含j=∞）有
\[
|x_j-x_i|\ge s_i-\sum_{\ell>i}s_\ell=\delta s_i .
\tag{QB3}
\]
取 \(S=\{p_j:j\ge0\}\cup\{x_\infty\}\)。
对当前x_j，旧锚i<j距至少δs_i−t_i>2t_i≥2t_j；
新锚i>j距至少δs_j−t_i>2t_j，极限距大于3t_j。
所以p_j是唯一最近锚，d(x_j,S)=t_j>0。S非空紧，链顶点互异。

定义完整 \(J=P_S\cup\{(x_j,x_{j+1})\},\quad
F=\lambda^{-1}(J^{-1}-I)\)；可沿轴嵌入二维，底图仍为整个平面的P_S。
附加边只积到已有恒等边，故完整F/J闭、精确零集S、全域近端非空，
零输入唯一驻定。正输出有唯一链前像，因此
\[
\rho_{j+1}=s_j/\lambda,\qquad
t_{j+1}=K\rho_{j+1}^q,\qquad
\langle x_j-x_{j+1},x_{j+1}-p_j\rangle
 =-s_j(s_j-t_j)\ge-Mt_j^{2m}.
\tag{QB4}
\]
最后用 \(g^2c^2\le M\)；投影边原合同直接成立。
原φ由自由数据认证时支配 \(\mathcal M_D\)，故本图仍保同一φ，
而非把其更小实际比g^q改名为预设共同目标。
所有轨道要么沿有限尾长的链，要么投影后驻定；距离窗全输出不变。

选稀疏整数 \(n_\ell=\ell^2+\ell\)，仅令这些位置ε为−1，其他为+1。
相邻负号间距趋∞，在负号位置有
\[
\frac{e_{n_\ell}}{s_{n_\ell}}\to\frac{1-2g}{1-g},\qquad
\frac{e_{n_\ell+1}}{s_{n_\ell}}\to\frac{g}{1-g},\qquad
\limsup_k\frac{e_{k+1}}{e_k}=\frac{g}{1-2g}.
\tag{QB5}
\]
上界也由几何步尾与QB3直接给出。
τ<1/2取g=τ就达到QB1；
τ≥1/2让不同图的g上趋1/2，排除任何有限共同系数。
此论证没有声称某一个图具有无穷limsup。
τ≥1/3统一可取g=1/3，实际limsup为1，排除任何最终κ<1；
τ<1/3则由QB1选略大的κ<1，给共同点Q线性。

### 6.2 q=1时点R线性仍不必点Q线性

给出一个连续单值完整例，不把此例的结论转授每组固定线性参数。
取 \(H=\mathbb R^2,\lambda=1,K=4,q=1,M=0\)，p任意正，
\(S=\mathbb R\times\{0\}\)，r=4/5。
在正结点 \(t=r^k\) 令连续函数δ的值按k模3依次为
\(2/5,-2/5,-2/5\)，相邻结点间线性插值，t>1固定取2/5。
不要求δ自身在0有极限，δ有界使δ(|v|)|v|连续趋0。置
\[
T(u,v)=(u+\delta(|v|)|v|,rv),\qquad F=T^{-1}-I .
\tag{QB6}
\]
v=0时水平增量定义为0。由纵坐标先反解v，再反解u，
T是全域同胚，F全域连续单值，完整 \(J_F=T\)、精确零集S。
每条完整边和它的唯一最近输入锚满足
\[
a=rt,\quad s=t\sqrt{1/25+\delta(t)^2},\quad \rho=s,\quad
a\le4\rho,\quad
\langle x-y,y-P_Sx\rangle=[4/25-\delta(t)^2]t^2\ge0 .
\tag{QB7}
\]
零输入驻定、任意距离窗覆盖不变；步被常数倍rt几何和控制。
取原预设 \(\varphi(t)=99t/100\)，
因 \(99/100>4/\sqrt{17}=\kappa_0\)，同一原数据先已认证该目标。

从纵坐标1开始，实际 \(t_k=r^k\)。在k模3为0的位置，
水平有符号余尾除以t_k为−22/61，
下一位置的水平余尾除以t_{k+1}为−58/61。
纵向点误差分别是t_k及t_{k+1}，故
\[
\frac{e_{k+1}^2-e_k^2}{t_k^2}
 =r^2\left[1+(58/61)^2\right]-\left[1+(22/61)^2\right]
 =\frac{27}{305}>0.
\tag{QB8}
\]
无穷多个点误差上升排除点Q线性，点R线性和有限尾均保持。
同一图沿后缀给任意小初尺度，无需换图或放松完整残差。
这是一次错误加强的具体反证，不是线性分支全部参数的点Q分类。
