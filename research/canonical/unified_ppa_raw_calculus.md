# 固定物理对象的 raw operator 证书演算

2026-10-14。规范证明，闭合单元状态 derived-checked；实际独立冷审范围另见本批 audit。主稿、摘要和正文编号保持原样。按照 `AGENTS.md`、`RESEARCH_PROTOCOL.md` 与 `academic-writing-skills` 的证明审查模式执行。已读 C89–C91、C249–C250 及本日 semimonotone/inverse/gauge 三份报告。以下内部编号用于定位；注册身份见 C279/C280，公开首创未认证。

**结果。** 不先求完整 $J$，可以从原图的向量不等式、线性等式及非线性余项直接编译全部纤维的物理距离与步长证书；固定仿射零目标上，有限个二次约束给可计算的充分 LMI。矩阵半单调的同参数完整域扩张在 $Q\succ0,H\succeq0$ 下可闭合，允许 $H$ 奇异且不要求参数交换。全域线性算子加上相对有界的非线性多值扰动还有独立的完整覆盖证明。两条闭子类回收 `diag(-1,.01), lambda=3` 和 GU3 的方向优势。一般 signed budget 的局部覆盖和非仿射零集编译仍未闭；精确交接题见 §9。

## 1. 固定对象；不要把分析权重改成另一个算法

除 §4 的全对图扩张外，本稿固定物理 Euclidean 空间 $X=\mathbb R^n$、完整关系 $F:X\rightrightarrows X$、步长 $\lambda>0$ 与**普通**完整近端关系
\[
J=(I+\lambda F)^{-1},\qquad
r_F(y)=\inf_{w\in F(y)}\|w\|.
\tag{RC1}
\]
空值残差取 $+\infty$。若只声明允许子关系，必须另外写出其身份；本稿的两个基准均保留原完整 $J$。`Fix J=zer F` 是 (RC1) 的代数事实，不能把图剪切后的零集当原零集。

本稿距离和步长编译的已证适用范围为非空仿射物理目标
\[
S=s_0+\ker N\subset\operatorname{zer}F,
\quad N=N^\top=N^2.
\tag{RC2}
\]
对输入 $x$，最近物理零锚唯一：$p=P_Sx$。任意完整输出 $y\in Jx$ 给原图值 $w=(x-y)/\lambda\in F(y)$，定义
\[
a=y-p,\quad e=x-p=a+\lambda w,
\quad t=\|e\|=d(x,S),\quad q=d(y,S)=\|Na\|,
\quad s=\lambda\|w\|=\|x-y\|.
\tag{RC3}
\]
同一个最近物理锚被保留，且 $(I-N)e=0$。对一般闭零集，只能先得 $q\le\|a\|$，不能直接套用 $q=\|Na\|$。非仿射几何由联合母稿处理，本稿不宣称全 Hilbert 或全部 C249 对象已被这个 LMI 子类包含。

<a id="urc-lmi"></a>
## 2. 第一轮：原图不等式 → 联合可行集 → LMI

### RC-A-v1：带 signed remainder 的 raw 编译（已直接证明）

用一个有限维提升变量 $z$ 保存 $a,w$ 及原模型需要的辅助图值。固定线性读出矩阵
\[
a=Az,\qquad w=Bz,\qquad e=Ez=(A+\lambda B)z.
\tag{RC4}
\]
设每个受检输入的**全部完整输出**都产生满足同一组约束的 $z$：
\[
z\in\mathcal L,\qquad z^\top Q_i z+R_i(z)\ge0\quad(i=1,\ldots,m),
\tag{RC5}
\]
其中 $\mathcal L$ 是已声明线性子空间，包含 $(I-N)Ez=0$ 及原模型线性等式；$Q_i$ 对称；$R_i$ 可以有任意符号。对每个 $t\in[0,R]$，假设在同一可行块上有可证明的上界 $R_i(z)\le\eta_i(t)$，其中 $\|Ez\|=t$。上界不从有限采样获得。

若存在 $\alpha_i\ge0$、$0\le\kappa_0<1$ 使
\[
\kappa_0^2E^\top E-A^\top NA-\sum_i\alpha_iQ_i\succeq_{\mathcal L}0,
\tag{RC6}
\]
则对每个完整输出都有
\[
q^2\le\kappa_0^2t^2+\sum_i\alpha_i\eta_i(t).
\tag{RC7}
\]
记号 $K\succeq_{\mathcal L}0$ 指在该子空间上非负；计算时取列满秩基矩阵 $Z$ 后检查 $Z^\top KZ\succeq0$。若存在 $\kappa<1$ 满足
\[
\sum_i\alpha_i\eta_i(t)\le(\kappa^2-\kappa_0^2)t^2
\quad(0<t\le R),
\tag{RC8}
\]
则 $q\le\kappa t$。负余项可以改善耗散；并不必须先将每个余项改为非负缺陷。

步长编译完全相同：若 $\beta\ge0,\nu_i\ge0$ 且
\[
\beta^2E^\top E-\lambda^2B^\top B-\sum_i\nu_iQ_i\succeq_{\mathcal L}0,
\tag{RC9}
\]
则 $s^2\le\beta^2t^2+\sum_i\nu_i\eta_i(t)$。非线性切向约束也可单独给步界 $s\le b(t)$，无需强迫其成为一个常参数 LMI。

**证明。** (RC6) 给 $\kappa_0^2\|Ez\|^2-\|NAz\|^2\ge\sum_i\alpha_i z^\top Q_i z$。由 (RC5)，右侧至少为 $-\sum_i\alpha_iR_i(z)\ge-\sum_i\alpha_i\eta_i(t)$。移项即得 (RC7)；(RC9) 同理。对全部实际完整输出逐一成立，故不需要单值性。

这里的 LMI 是充分证书；多个约束时没有证明 S-procedure 无损。SDP 不可行只排除该次充分编译，不排除原对象收敛，也不排除另一个提升或非二次证书。

### 可行 profile；保留 true EB 的正确方向

令 $\mathcal K_t$ 为 (RC5)、所有非线性原数据约束、$\|Ez\|\le t$ 及合法评价窗的联合可行集，定义
\[
Q(t)=\sup_{z\in\mathcal K_t}\|NAz\|,
\qquad B(t)=\sup_{z\in\mathcal K_t}\lambda\|Bz\|.
\tag{RC10}
\]
上确界允许 $+\infty$；这里是原图的**外证书可行集**，不能把其中每一点称为实际可实现输出。只要它包含所有实际 raw roots，便有全部输出的 $q\le Q(t),s\le B(t)$。其价值取决于原数据认证和可计算性；定义一个上确界本身没有解决近端根求解。

若已在所有需要的物理输出上认证真 EB $q\le\psi(r_F(y))$，且 $\psi$ 非减，则合法方向是
\[
r_F(y)\le\|w\|\quad\Longrightarrow\quad q\le\psi(\|w\|).
\tag{RC11}
\]
使用有限残差窗前，先证 $\|w\|\le\bar t$，或给独立的残差窗认证。若原图结构给**每个** $w\in F(y)$ 的下界 $\|w\|\ge g(d(y,S))$，取真正 inf 后才得到 $r_F(y)\ge g(d(y,S))$。只核算法选中值的下界不能产生 true EB。

若 $Q(t)\le\kappa t$、$B(0)=0$、$\sum_jB(\kappa^jt)<\infty$，且所有受检输入均有完整输出，那么严格物理留域预算与有限前缀归纳给全部轨道有限长度。此处覆盖、零输入全部驻定、评价窗仍是独立合取条件；LMI 距离收缩不能替代它们。联合母稿的更细势预算可以超出独立 $Q/B$ 尾和，本稿不把尾和写成有限长度的必要条件。

## 3. 原始 operator 演算：保留提升变量，必要时再消元

### 全对矩阵半单调与逆耗散

原物理图差 $a=y-y',b=w-w'$ 的矩阵半单调条件是
\[
\langle a,b\rangle\ge a^\top M_0a+b^\top R_0b,
\quad
Q_{M_0,R_0}=\begin{pmatrix}-M_0&I/2\\ I/2&-R_0\end{pmatrix}.
\tag{RC12}
\]
它直接是一个 raw 二次约束。对原逆耗散
$\langle a,b\rangle\ge-\rho\|b\|^2+\delta(a,b)$，取 $M_0=0,R_0=-\rho I,R=-\delta$ 即纳入 signed remainder；正的高阶耗散必须保留符号。

任意可逆线性图坐标变换 $z'=Tz$ 将原证书精确变为 $Q'=T^{-\top}QT^{-1}$、$R'(z')=R(T^{-1}z')$。这是证书演算，若变换后直接迭代，算法和零集需要另桥。逆关系是交换两图坐标，故 (RC12) 中 $M_0,R_0$ 交换；$cF,c>0$ 给 $(cM_0,R_0/c)$；图 shift $F+Ky$ 是三角线性变换。完整纤维和图包含被坐标双射保留，但 $\operatorname{zer}F^{-1}=F(0)$ 通常不等于 $\operatorname{zer}F$。

### 和与 Cartesian product：锚点也必须一起提升

设 $F=F_1+F_2$。对目标锚 $p\in\operatorname{zer}F$，必须选一个真实分解 $b_{10}\in F_1(p),b_{20}\in F_2(p),b_{10}+b_{20}=0$。两项并不必须各自以零图值为锚。对任意实际 sum 图值 $w=w_1+w_2$，保存 $z=(a,w_1-b_{10},w_2-b_{20})$，把每项的原证书拉回同一 $z$，并将总值读成 $Bz=(w_1-b_{10})+(w_2-b_{20})$。任何依赖两项图值相关性的 signed remainder 都留在提升空间。若锚认证只对某个分解成立，必须证明每个需要的最近锚都有这样的分解。

纯矩阵消元可回收已知和规则。若 $W=R_1+R_2\succ0$，则对 $b=b_1+b_2$
\[
b_1^\top R_1b_1+b_2^\top R_2b_2
=b^\top(R_1\mathbin{\Box}R_2)b
 +(b_1-W^{-1}R_2b)^\top W(b_1-W^{-1}R_2b),
\tag{RC13}
\]
其中 $R_1\Box R_2=R_2-R_2W^{-1}R_2$。因此得到 $M=M_1+M_2,R=R_1\Box R_2$，即使 $R_i$ 各自不定。若 $W\succeq0$，还必须满足矩阵 parallel-summable 的 range 条件，再用伪逆；不能只看 $W\succeq0$。若 $W$ 有负方向，分解能量的 inf 可以是 $-\infty$，原提升证书仍可有用，但不能套用该消元式的下界。

Cartesian product 的状态和图值均按块保留，证书矩阵直接做 block diagonal，余项相加；原对象的完整图恰是各项完整图的乘积。零集是各零集乘积，完整普通 PPA 的覆盖须各因子都覆盖。

### Linear composition：值核中的残差不是物理残差

对 $G=L^\top FL$，原提升变量为 $(a,u)$，原图差为 $(La,u)$，新图值差为 $L^\top u$。因此原证书直接在 $(La,u)$ 上评价。若要压为矩阵证书，可取
\[
M_G=L^\top M_FL,\qquad LR_GL^\top\preceq R_F,
\tag{RC14}
\]
因为 $\langle a,L^\top u\rangle=\langle La,u\rangle$，而 $u^\top R_Fu\ge(L^\top u)^\top R_G(L^\top u)$。完整零锚需要 $u_0\in F(Lp)$、$L^\top u_0=0$，不要求 $u_0=0$。

`zer G`、coverage 与 $r_G(x)=\inf_{u\in F(Lx)}\|L^\top u\|$ 必须重新认证。若 $L^\top$ 有核，原 $\|u\|$ 下界不产生 $\|L^\top u\|$ 下界。例如非零常值 $u_0\in\ker L^\top$ 的原 $F$ 没有零，$G\equiv0$ 却处处为零。没有 angle/restricted injectivity 门，就不能继承原 true EB。

<a id="urc-matrix"></a>
## 4. RC-M-v1：非交换矩阵的 same-class Minty completion（闭证明）

本节限全部点对的完整原图 $\Gamma\subset\mathbb R^n\times\mathbb R^n$，不把零锚条件混进来。固定 (RC12) 与 $\lambda$，定义 scaled 参数
\[
M=\lambda M_0,\quad R=R_0/\lambda,\quad
Q=I+M+R,\quad D=M-R,\quad
H=I-M-R+DQ^{-1}D.
\tag{RC15}
\]
假设 $Q\succ0$；不要求 $M,R$ 交换。对两图点令
\[
p=a+\lambda b,\qquad c=a-\lambda b.
\]
直接展开得到 (RC12) 等价于
\[
c^\top Qc+2p^\top Dc\le p^\top(I-M-R)p,
\quad
\|Q^{1/2}c+Q^{-1/2}Dp\|^2\le p^\top Hp.
\tag{RC16}
\]
这里不是更换物理 PPA；$Q$ 是证明中的图二次型参数。

**精确结论。** 若另有 $H\succeq0$，每个非空满足同一 $(M_0,R_0)$ 全对条件的图都有保持同参数的完整 Minty 域扩张；原图在该同参数全图类中包含极大，当且仅当原自然输入域 $\mathcal D=\{y+\lambda w:(y,w)\in\Gamma\}$ 等于全部 $X$。这个结论允许 $H$ 奇异。

**证明。** (RC16) 在输入差为零时强制 $c=0$，因此原图的 Cayley $C:\mathcal D\to X$ 良定。置
\[
G(p)=Q^{1/2}C(p)+Q^{-1/2}Dp.
\]
则 $\|G(p)-G(q)\|\le\|H^{1/2}(p-q)\|$。若 $H^{1/2}p=H^{1/2}q$，右侧为零，故 $G(p)=G(q)$。因而在 $H^{1/2}\mathcal D\subset\operatorname{ran}H^{1/2}$ 上良定一个 1-Lipschitz 映射 $g(H^{1/2}p)=G(p)$。使用仓库已经核过的 Hilbert Kirszbraun 同常数扩张，将 $g$ 扩张到整个 $\operatorname{ran}H^{1/2}$，记为 $\widehat g$。定义
\[
\widehat C(p)=Q^{-1/2}\bigl[\widehat g(H^{1/2}p)-Q^{-1/2}Dp\bigr]
\quad(p\in X).
\tag{RC17}
\]
它在原域等于 $C$，满足同一 (RC16)，故 Cayley 拉回
\[
\widehat\Gamma=
\left\{\left(\frac{p+\widehat C(p)}2,
\frac{p-\widehat C(p)}{2\lambda}\right):p\in X\right\}
\tag{RC18}
\]
满足原未缩放 $(M_0,R_0)$，包含原图并有完整输入域。若原域缺输入，这一扩张严格，否定极大；若原域完整，任意兼容新点有相同输入的旧点，(RC16) 在零输入差强制图点相同，故不可严格扩张。

**$H\succeq0$ 的作用。** 完整输入域必有所有 $p$ 的差，(RC16) 强迫 $p^\top Hp\ge0$，所以此门不可删。具体取 $\lambda=1,M_0=R_0=\operatorname{diag}(1,0)$，则 $Q=\operatorname{diag}(3,1),D=0,H=\operatorname{diag}(-1,1)$。原图
\[
\Gamma=\{((0,t),(0,0)):t\in\mathbb R\}
\tag{RC19}
\]
满足半单调条件，但自然域只是 $\{0\}\times\mathbb R$。若添加输入 $p=(p_1,p_2)$ 且 $p_1\ne0$，与旧输入 $q=(0,p_2)$ 比较会要求非负平方 $\le-p_1^2<0$，不可能；若 $p_1=0$，旧输入已有唯一点。所以 (RC19) 已是同矩阵全图极大，却不覆盖。这里的 $\operatorname{dom}F$ 也只是直线，不能悄悄改成全域算子。

这是本轮独立完成的代数/扩张证明，外部输入仅为本库 [HE-EXTENSION](../canonical/holder_extension.md#he-extension) 已明确导入的 Hilbert 同常数扩张。它回收 C91 的标量门并修复半单调报告留给矩阵 coverage 的义务；没有据有限阅读宣称文献首创。一般非二次 Hilbert profile 扩张由 [coverage 前沿稿](unified_ppa_coverage.md) 承担。

<a id="urc-uncertainty"></a>
## 5. RC-P-v1：原模型 nonlinear uncertainty 的完整覆盖与全部输出

固定完整原关系
\[
F(y)=Dy+\mathcal E(y),
\tag{RC20}
\]
其中 $D\in\mathbb R^{n\times n}$，$\mathcal E$ 全域 upper semicontinuous，非空紧凸值，并且每个 $e\in\mathcal E(y)$ 都有 $\|e\|\le\varepsilon\|y\|$。这是原图的结构假设，不从指定 $J$ 反造关系；$\mathcal E(y)$ 可依赖全部状态且真正多值。令 $V=I+\lambda D$，假设
\[
\sigma_{\min}(V)>\lambda\varepsilon.
\tag{RC21}
\]
则完整 $J$ 全域有输出，且每个完整输出满足
\[
\|y\|\le\frac{\|x\|}{\sigma_{\min}(V)-\lambda\varepsilon}.
\tag{RC22}
\]
若 $\varepsilon<\sigma_{\min}(D)$，则原完整零集为 $\{0\}$，并且
\[
r_F(y)\ge(\sigma_{\min}(D)-\varepsilon)\|y\|.
\tag{RC23}
\]
因此 (RC22) 的分母 $>1$ 时，全部完整选择全局有限长度并收敛到零，距离因子 $\kappa=1/[\sigma_{\min}(V)-\lambda\varepsilon]$，物理步至多 $(1+\kappa)\|x\|$。零输入所有输出为零。

**独立覆盖证明。** (RC21) 保证 $V$ 可逆且 $c=\lambda\|V^{-1}\|\varepsilon<1$。固定输入 $x$，取
$R_x=\|V^{-1}\|\|x\|/(1-c)$。对应 $\Phi(y)=V^{-1}(x-\lambda\mathcal E(y))$ 在闭球 $\overline B_{R_x}(0)$ 上非空紧凸值、upper semicontinuous，且
$\|\Phi(y)\|\le\|V^{-1}\|\|x\|+cR_x=R_x$。Kakutani 给 fixed point，其等式就是原完整近端包含。$x=0$ 时 $\mathcal E(0)=\{0\}$，零直接是输出。对任意可能远 root，$x=Vy+\lambda e$ 给 $\|x\|\ge[\sigma_{\min}(V)-\lambda\varepsilon]\|y\|$，所以 (RC22) 控制全部 root，不只构造出的 root。最后 (RC23) 对全部原图值成立再取 inf；若零值存在，它强迫 $y=0$。

这调用标准 finite-dimensional Kakutani fixed-point theorem，逐项映射如上；该输入与仓库 [SC3](../candidates/coupled_holder_structural.md) 的同类型 coverage 证明一致。非凸 uncertainty 纤维时不得照搬 Kakutani；GU3 在下一节用显式逐支覆盖，不伪称此定理包含它。

方向可进一步由 raw LMI 保留。令 $z=(a,w),A=[I\ 0],B=[0\ I],E=A+\lambda B$，原 (RC20) 给
\[
z^\top Q_\varepsilon z\ge0,
\quad Q_\varepsilon=\varepsilon^2A^\top A-(B-DA)^\top(B-DA).
\tag{RC24}
\]
只需找到 $\tau\ge0$ 使 $\kappa^2E^\top E-A^\top A-\tau Q_\varepsilon\succeq0$，就可不计算 $J$ 而认证全部 root 的固定物理收缩。这里 scope 是 singleton affine full zero；未宣称该 SDP 会给 coverage。

## 6. 两个基准：方向关联被原样回收

### `diag(-1,.01), lambda=3`

原 $D=\operatorname{diag}(-1,1/100)$，原目标 $S=\{0\}$。不先求 $J$，原 graph 等式 $w=Da$ 将 raw LMI 限到 $z=(a,Da)$。它变成
\[
\kappa^2(I+3D)^\top(I+3D)-I\succeq0.
\tag{RC25}
\]
$I+3D=\operatorname{diag}(-2,103/100)$ 可逆给原完整覆盖。取 $\kappa=100/103$，(RC25) 的矩阵恰是 $\operatorname{diag}(29391/10609,0)\succeq0$，故达到锐的原物理因子；第二坐标取等。原 true EB 为 $\|a\|\le100r_F(a)$。原 inverse certificate 也直接给 $\|y\|^2+3\|Dy\|^2\le\|x\|^2$，但其 scalar EB 合并得到的因子 $100/\sqrt{10003}$ 更松。

同一参数还容许所有 $0\le\varepsilon<1/100$ 的 (RC20) 非线性紧凸 uncertainty：$\sigma_{\min}(V)=103/100$，因此 $\sigma_{\min}(V)-3\varepsilon>1$，完整覆盖、全部输出、全零吸收、物理 true EB 一起成立。这不是只认证未扰动线性例。

可复核的有理数 LMI 实例：$\varepsilon=1/200,\kappa=99/100,\tau=600$。将 (RC24) 的 LMI 按两个坐标重排，两个 $2\times2$ 块分别为
\[
\frac1{10000}
\begin{pmatrix}5999651&6029403\\6029403&6088209\end{pmatrix},\qquad
\frac1{10000}
\begin{pmatrix}251&-30597\\-30597&6088209\end{pmatrix}.
\tag{RC26}
\]
首主元为正，行列式分别是 $3468573573/2000000$、$11839281/2000000$，故严格正定。简单 raw bound 其实更锐，为 $200/203$，真 EB 系数为 200；(RC26) 只证明 SDP 编译确实可实施，不声称数值优化最优。

这同时回收旧报告的严格差异：固定原 Id 核、原物理零集与完整关系的 C249 直接门最小因子 50，C250 任意合法独立 scalar gauge 仍被 $25000/10009>1$ 排除。该排除不是否定全部 RL 分析，只说明提前分别取最坏反射/残差丢失方向关联。

### GU3：法向 dissipativity 与切向物理步一起保留

原 $0<\gamma<1,\lambda=1,S=\mathbb R\times\{0\}$ 及完整
\[
F(u,s)=\{(0,s),(-2^\gamma|s|^\gamma,s)\}.
\tag{RC27}
\]
取 $N=\operatorname{diag}(0,1)$。对任意 raw graph 值及最近物理锚，**原数据直接**给
\[
Nw=Na,\qquad
\|(I-N)w\|\le2^\gamma\|Na\|^\gamma.
\tag{RC28}
\]
包含的法向部分为 $Ne=Na+Nw=2Na$，故每个完整 root 的距离 $q=t/2$。切向输入差 $ (I-N)e=0 $ 给 $ (I-N)a=-(I-N)w $，所以
\[
s=\|w\|\le t/2+t^\gamma,
\quad
\sum_ks_k\le t_0+\frac{t_0^\gamma}{1-2^{-\gamma}}.
\tag{RC29}
\]
零输入时 (RC28) 强迫 $Na=0,w=0,a=0$，所以全部零纤维驻定。两个 branch 的法向方程唯一给 $s=r/2$，再分别给 $(x,r/2)$、$(x+|r|^\gamma,r/2)$，逐支构成全部完整 $J(x,r)$，验证全域 coverage。原 full true residual 是 $|s|$，因为直支存在、全部图值法向量相同；故物理 true EB 系数 1。

这回收 GU3 的实际 $1/2$ 因子与全部物理长度，同时保留完整多值关系；没有换 metric。固定 Id 核 C250 的全部合法 scalar gauge 排除由本日 [GU3-v1](../novelty/2026_10_14_submonotonicity/gauge_unification_review.md) 的精确量词承担。这里的正面机制本来已在 SC14–SC15；本稿的增益是与 raw LMI/演算共用同一物理接口，不将该例重新宣布为新定理。

## 7. 第二轮：临界点、零纤维、远输出与 variable metric 攻击

### 正高阶耗散 + true linear EB 仍不保证有限长度

取完整 $F=B^{-1}$，其中 $B(w)=w^3-w/2$，原 $\lambda=1,S=\{0\}$。原近端方程
\[
x=w^3+w/2,\qquad y=w^3-w/2
\tag{RC30}
\]
第一式严格递增且满射，所以原完整 $J$ 全域单值。原 raw 零锚 energy 是精确式
\[
x^2-y^2=2w^4>0\quad(w\ne0).
\tag{RC31}
\]
除此以外还有**真正局部线性 EB**：若 $\|y\|\le1/8$，对每个 $w\in F(y)$，当 $|w|\le1/4$ 时 $\|y\|=|w|(1/2-w^2)\le|w|/2$；当 $|w|>1/4$ 时 $|w|\ge2\|y\|$。故 $r_F(y)\ge2\|y\|$，即 $d(y,S)\le r_F(y)/2$。此证明对全部三个可能 inverse 图值取真正 inf，不用选中近端值替代残差。

由 (RC31)，$|x_k|$ 非增且 $\sum_kw_k^4<\infty$，故 $w_k\to0$；(RC30) 第一式再给 $x_k\to0$。但小非零初值的符号交替。反解第一式：$w=2x-16x^3+O(x^5)$，故 $Jx=-x+16x^3+O(x^5)$。令 $a_k=|x_k|>0$，则
$a_{k+1}=a_k-16a_k^3+O(a_k^5)$，从而 $a_{k+1}^{-2}-a_k^{-2}\to32$，$a_k\sim(32k)^{-1/2}$。步长为 $a_k+a_{k+1}$，其总和发散。这里全域 coverage、全部输出、闭图、零吸收与同窗真 linear EB 均成立；失效的是将任何正耗散一概提升为有限长度。一般非线性余项必须另给实际可和势/步预算。

### 距离收缩 + true EB 不能删零步门

完整 $F(u,v)=\{(u,0),(u,-1)\}$，$\lambda=1$，有 $S=\{0\}\times\mathbb R$、$r_F(u,v)=|u|$、$J(a,b)=\{(a/2,b),(a/2,b+1)\}$。每个输出距离收缩 $1/2$，但从零输入每次选第二支会无限切向漂移。原物理 $B(0)=0$ 或等价完整零步门是必需合取，不能从 $Q(0)=0$ 推出。

### Local raw certificate 不认证远端完整 root

完整原图
$\operatorname{gph}F=\operatorname{gph}I\cup\{(10,p-10):|p|\le1\}$
在零附近的状态/图值窗口与 Id 完全一样，局部强单调和局部 inverse regularity 原样成立，原完整图闭且满输入，但 $10\in J(0)$。若 raw cert 只在小 graph block 里认证，它编译的是块内 root，不能把全部完整 root 塞进 $\mathcal K_t$。可用修复是独立 raw root confinement、证明原图与扩张在全部需要 fiber 上相等，或明定允许子关系；不能先假定输出留域。

### Arbitrary SPD kernel 改算法；branch-specific metrics 不能望文望义地拼接

对原 diag 基准，若把 Id 核改为 $v(x)=2x$，$\lambda=3$ 时新第一坐标 factor 为 $-2$，会发散；改为 $v(x)=3x$ 时 $v+3F$ 第一坐标为零，许多输入无输出、零输入反而有任意第一坐标输出。这些 SPD 核仍保普通代数式的零集与 fixed point 身份，但不保原覆盖、原 outputs 或原算法的收敛。

只作分析权重也必须有共同比较。取原完整
\[
F(y)=\{D_1y,D_2y\},\quad\lambda=1,\qquad
J(x)=\{A_1x,A_2x\},
\]
\[
A_1=\begin{pmatrix}1/2&2\\0&1/2\end{pmatrix},
A_2=A_1^\top,
D_i=A_i^{-1}-I.
\tag{RC32}
\]
原零集为 $\{0\}$，完整 coverage 与零吸收成立；$\sigma_{\min}(D_i)>0$ 给原 physical true linear EB。每支分别在 $P_1=\operatorname{diag}(1,100)$、$P_2=\operatorname{diag}(100,1)$ 的固定 SPD 范数中具有同一 contraction $ (\sqrt{26}+1)/10\approx0.60990195<1$。但交替选择 $A_1,A_2$ 的两步乘积最大特征值 $ (9+4\sqrt5)/4\approx4.48606798>1$，故有发散的完整轨道。每一步“存在一个好 SPD”不足以同一个全输出 physical theorem。若采用时变 metric，必须显式携带 metric 比较因子或可和 variation；还须桥接 physical distance、physical true residual 和物理步长。

## 8. 一手事实、实际阅读与可复现范围

读过并用来核具体事实的固定版本：

| 来源 | 实读位置 | 本稿仅使用的事实 |
| --- | --- | --- |
| [Evens–Pas–Latafat–Patrinos 2305.03605v2](https://arxiv.org/html/2305.03605v2) | Definition 4.1、Proposition 4.5、Proposition 4.7；原 weak Minty 定义 2.1 | 已有 anchored/all-pair scalar semimonotone、linear LMI 与有 sign/range 门的 sum 演算。收敛不是只凭名称导入。 |
| [Evens–Latafat–Patrinos 2312.06540v1](https://arxiv.org/pdf/2312.06540v1) | Definition 1.2 p.3；Proposition 4.2/4.3 p.14；Corollary 4.6、Definition 4.7、Proposition 4.8 p.15 | 已有对称可不定矩阵定义、inverse/scaling/product、linear LMI、线性 composition 和 parallel-summable sum。最新版本编号不同，本文不混写。 |

矩阵 Minty completion (RC-M) 和 uncertainty 全部 root 证明在本稿重建；不将前一行论文的线性 LMI 冒称为覆盖定理，也不声称上述既有演算是新概念。原文中不定 matrix parallel sum 的 range 门已核，本文严格保留。

验证器 [raw_verify.py](../code/unified_ppa/raw_verify.py) 只依赖 Python 3 与 NumPy，运行命令：
```
python3 research/code/unified_ppa/raw_verify.py
```
它用 `fractions.Fraction` 精确验证非交换二次型恒等式、diag 锐 raw LMI、uncertainty 的有理矩阵 principal minors、signed sum 完平方及临界 polynomial energy；另作 GU3 两支 graph/真 inf、critical 渐近、SPD 切换的有限数值检查。数值范围与全部结果随 stdout 输出，模拟不承担一般证明。2026-10-14 当前环境 Python 3、NumPy 2.3.5，验证器全部通过。

## 9. 未闭高价值题：两轮后交接 6pro 的精确 prompt

### RC-O1：原图 signed remainder 的局部完整覆盖

**已证最强子类。** 全对 quadratic (RC15) 的 $Q\succ0,H\succeq0$ 同类图极大性给 full Minty；全域 (RC20) 的 $\sigma_{\min}(I+\lambda D)>\lambda\varepsilon$ 给完整 coverage 和 raw confinement；非二次 mixed Hilbert input profile 由 coverage 同伴稿另闭。任意矩阵或零锚 signed remainder 不默认继承这些结论。

**尝试 1。** raw (RC5) 可用 SDP 保全部已存在 root 的距离/步几何；完全不能证明任何 root 存在。即便 “极大”只在局部 graph block 定义，也缺完整远端 fiber 排除。

**尝试 2。** 用 graph shift 与 nonlinear Hölder envelope 猜 coverage：quadratic 部分由 (RC-M) 闭；普通 Hölder/Bernstein 输入预算可按同伴稿的 Hilbert embedding 完成；一般依赖两图坐标的 signed budget 未变成保证可交的 input balls，所以未闭。remote (RC31 后的图) 和 $H\not\succeq0$ 的 (RC19) 限制任何无门升级。

**6pro prompt。** 固定有限维 Euclidean 普通 $J_{\lambda F}$，不改 $F,\lambda,S,r_F$。从全对原 graph 条件
\[
z^\top Qz+R(a,b)\ge0,
\quad z=(a,b),\quad R(0,0)=0,
\]
及明确的全图或局部图最大性提出**可从原数据检查**的 completion/coverage 门。要求给准确参数与 scope，使每个认证输入有原完整 root，并且所有原完整 root 落在认证窗；若只能给允许块内选择，明确不能宣称 full fiber。不得把可行集非空当原 graph root 非空，不得以反射模的 existence 代替 extension proof。先判断是否存在最小的 genuinely joint nonquadratic signed remainder 子类，可超出单个 transformed-Hilbert input profile，同时容纳 critical inverse 而不宣称其有限长度；给一条闭 theorem 或两个点/有限图的确切 obstruction。对提出的门必攻 $a+\lambda b=0$、remote root、$Q$ 的核和 $H$ 负特征。输出须包括 strongest proved subclass、仍缺命题和一手先行范围；不宣称全部 semimonotone 已被统一。

### RC-O2：自然全域原图的非仿射全部远端 root 准入

**已证最强子类。** (RC-A) 在 fixed affine physical $S$ 上保最近锚、向量相关性、true residual 与完整零吸收，回收 diag 与 GU3。[曲零认证稿](unified_ppa_curved_geometry.md) §2 的完整闭管图已从法/切向原始场、reach 曲率门及 continuous mode 给覆盖、全部输出收缩、真 EB 和有限长度，§4 另给圆上根式补偿模型；这些曲率编译不是本轮仍开放的题。该稿从一开始将原完整 $F$ 的 domain 限在闭管、管外取空值；尚未给任意自然全域原 $F$ 的远端 root 排除。

**尝试 1。** 在非仿射目标把法向 $N$ 冻结为 $N_p$，以 curvature remainder 控制 $d(y,S)-\|N_pa\|$；闭管原图或另有排远门时可用。对全域原图，只在小管内认证的这些界不能排除管外 root，remote 反例仍通过全部局部条件。

**尝试 2。** 让 $N=N_p$ 或 SPD 随锚变化，仍需统一 raw root confinement、angle 和 metric transition 比较；(RC32) 证明每步存在好 metric 不够。单凭 pointwise LMI 没有共同物理 theorem，因此暂不声称包含非仿射 C249 或全 Hilbert 父定理。

**6pro prompt。** 固定 $X=\mathbb R^n$、一个预先由自然原始数据定义且管外也有图值的全域完整 $F$、原普通 $J_{\lambda F}$、compact $C^2$ zero submanifold $S$ 的局部目标。读本稿 (RC-A) 及曲零认证稿 §2 已闭的完整管图定理；**不要重证已闭管内曲率编译，也不要以将管外图值改为空来完成任务**。给已认证 reach $\rho>0$、uniform curvature bound $K$，管内 graph 数据允许 raw lift $z=(y-p,w,\xi)$。目标是从自然原 graph 的 coercivity、拓扑次数、法向 growth 或其他明确数据，在**尚未假定输出留管**之前，独立认证近零输入的原完整 coverage 和全部管外 root 排除，然后将每个完整 root 接入 uniform LMI/signed curvature remainder 的物理距离或联合可和势；真残差必须评价该全域原 $F$。不得更换 $F,S,\lambda$ 或把最近锚改成任意 Lyapunov 锚；state-dependent metric 须写完整比较门。若 general entry 不成立，给 full coverage 保持但局部数据完全相同且远 root/zero-fiber 失败的反例，并提出最小可检查修复。benchmark 回收 affine GU3、diag λ3 及至少一个自然全域曲面实例；不退回独立最坏 scalar $L/K$，不按名称宣称包含。最终输出 strongest proved class、剩余全称义务和精确先行范围。

## 10. 本轮状态边界

RC-A、RC-M、RC-P 的逐行证明与两个基准已经落在本文；已由独立读者实际全文冷审，核心身份注册 C279/C280；末节义务仍为 open。critical/zero/remote/SPD 攻击给具体对象与量词；不会因有限数值通过而升级一般命题。RC-O1/RC-O2 是两轮后仍未闭的研究义务，交接 prompt 已固定；同伴稿的联合势、nonlinear completion 和作者优先性审查各保其独立身份。
