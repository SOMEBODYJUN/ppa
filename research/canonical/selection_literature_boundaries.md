# 选择研究的一手接口、量词边界与独立证书

本页接续 [共同尾先例](selection_truncation_prior_tools.md)。文献的指定陈述身份为
`primary-checked`；这只认证原文写了什么。下述 C157/C158 的完整直接证明为
`derived-checked`。带 `candidate/deferred` 的调用门不进入已证明主链。
当前访问不追溯认证旧稿的访问日志，也不认证全领域先行性。
版本、原文入口和印页见 [LITERATURE](../LITERATURE.md#lit-selection-interfaces)。

<a id="sl-lt"></a>
## LT：截取图、完整路径和真残差分开

正式版为 DOI 10.1287/moor.2025.0863 的 13 页正文。Proposition 4（p.5）
用的是 \(F_W=(F\cap W)|_U\)，自然输入域 \(D=(I+F_W)(U)\)。

\[
0\le\tau<1/2\quad\Longrightarrow\quad
C=2J_{F_W}-I\text{ 的全对 Lipschitz 系数 }\sqrt{1+4\tau},
\quad \operatorname{Lip}J_{F_W}\le\frac{1+\sqrt{1+4\tau}}2.
\]

它不供应指定环境邻域的 coverage，也不把 \(J_{F_W}\) 等同完整 \(J_F\)。
固定步长 \(h>0\) 时对关系 \(hF\) 调用，输出窗也须随之绑定。
Example 2（p.8）的 \(F(u)=-\sqrt u,U=[0,1/16]\) 仅给结构上的
violation 2；不满足这条亚临界门，也没有共同近端自映射窗。

Lemma 2（pp.9–10）的安全接口可以独立重证：在完备赋范空间中，闭非空集 \(S\)，
同一轨道满足
\[
\|x^{n+1}-x^n\|\le\eta d(x^n,S),\qquad
d(x^{n+1},S)\le qd(x^n,S),\quad0\le\eta<\infty,\quad0\le q<1.
\]
则对 \(m>n\) 求和得 \(\|x^m-x^n\|\le\eta q^n d(x^0,S)/(1-q)\)。
完备性和距离连续性给 \(x^*\in S\)，因此
\[
\|x^n-x^*\|\le\frac{\eta q^n}{1-q}d(x^0,S).
\tag{SL1}
\]

共同尾另需全初值共同的 \(\eta,q\) 和有界初始距离；逐初值 R 线性不够。
当 \(q=0\)，第一步后驻定，\(n=0\) 的式子按 \(0^0=1\) 解释。

Assumption 2（p.10）分别要求：闭非空 \(S=\operatorname{zer}F\cap D\)；
完整 \(J_{hF}:D\rightrightarrows D\)；邻域 \(N\) 上真残差 EB

\[
d(x,S)\le\bar\rho d(0,F(x)),\quad x\in N\cap D,
\qquad N'=\{x\in D:J_{hF}(x)\subset N\cap D\}\ne\varnothing;
\]

以及 \(hF\) 在 \(U\times W\) 上固定参数的 maximal LT 条件、

\[
U'\subset(I+h\bar F)(U),\quad
\bar F=F\cap(W/h),\qquad \tau(1+\bar\rho/h)^2<1/2.
\]

Theorem 2（pp.10–11）陈述的是选取

\[
x^{n+1}\in J_{hF}(x^n)\cap B_\delta(\bar x)
\]

的球内路径；不是全部完整输出都留球。有效导入仍为 `candidate/deferred`：
(i) 前提仅 \(N'\ne\varnothing\)，证明称其为邻域，须独立闭合全纤维定位；
(ii) 证明的 \(B_\delta\to B_r,r=2\delta\sqrt{1+2\tau}\) 不自给 \(B_r\) 不变；
(iii) 印刷尾前因子 \(4\delta\sqrt{1+2\tau}/(1-\kappa)\)、

\[
\kappa=\sqrt{1+2\tau-(h/(h+\bar\rho))^2}
\]

须另闭合，不能用 `SL1` 直接授予。另 Proposition 1（p.3）的非严格上端

\[
\rho\le\sqrt{(1-\alpha)/(\epsilon\alpha)}
\]

在 \(\epsilon>0\) 的等号处给收缩因子 1；严格收缩调用必须用严格上端。
这些是具体接口义务，不是 Theorem 2 的反例或整篇论文裁决。

<a id="sl-ltt"></a>
## LTTQ / LTTP：固定点锚与全部输入对

LTTQ 固定 v2 的 2.15/2.18/2.19 对应正式版 2.1/2.2/2.3。
它们在有限维 Euclidean 空间用固定闭集 \(S\subset\operatorname{ri}\Lambda\)
作锚，要求 \(T:\Lambda\rightrightarrows\Lambda,TS\subset\operatorname{Fix}T\cap S\)，
以及锚点 almost averaged。固定锚仍比较全部输出，不意味着第二个输入遍及整个域。
2.1 另在邻域环域对全部 \(x^+\in Tx,y^+\in Ty,y\in S\) 要求

\[
d(x,S)\le\kappa\|(x-x^+)-(y-y^+)\|,
\quad c^2=1+\epsilon-(1-\alpha)/(\alpha\kappa^2)<1.
\]

2.2/2.3 另冻结 \(S_{\gamma^i\delta}=(S+\gamma^i\delta B)\cap\Lambda\)、
固定集外环、相对 gauge regularity/subregularity 及逐环严格阈值；
2.2 还要求投影残差像的距离比较。所述结论为到固定集的距离率，
不自动给强点尾或 [SS-T1](solution_selection_rates.md#ss-transfer) 的全对输入模。
本项目没有移植这些定理为无条件算法结论。

LTTP 的 Th1–2 用闭凸 \(D\) 上全部输入对的非扩张/averaged 自映射，
非空固定集及每个有界集的残差 EB；Th1 另需渐近正则。
Th2 使用 gauge \(\kappa\) 并要求

\[
\phi(t)=\sqrt{t^2-\gamma[\kappa^{-1}(t)]^2},\quad
\phi^n(t)\to0\ (t\ge0),\qquad
\|T^nx-x^*\|\le2\phi^n(d(x,\operatorname{Fix}T)).
\]

这是核得的印刷陈述。一般 \(\phi\) 率证明不能省略可评价与迭代范围；
原陈述未另列 \(\phi\) 非减，不能以 \(d_{n+1}\le\phi(d_n)\) 未经论证就迭代上界。
裸全域 Hölder gauge 对大 \(t\) 甚至可能给负根号。本项目不授该一般率 `derived-checked`。
Th1–2 的强极限加全对非扩张却直接给非扩张回缩：

\[
\|T^nx-T^ny\|\le\|x-y\|\quad\Longrightarrow\quad
\|\Pi x-\Pi y\|\le\|x-y\|.
\tag{SL2}
\]

Th4 只需 `H` 上单值 \(T\)、非空固定集、有界 \(U\) 含固定点和
上半连续 \(c:[0,\infty)\to[0,1]\)，在 \(0<t\le\operatorname{exc}(U,\operatorname{Fix}T)\)
严格 \(c(t)<1\)，以及 \(d(Tx,\operatorname{Fix}T)\le c(d(x,\operatorname{Fix}T))d(x,\operatorname{Fix}T)\)。
它给 EB，没有非扩张前件。Prop3 另需 \(T(U)\subset U\) 才给集合距离趋零；
不据此补出连续选择。

<a id="sl-witnesses"></a>
## C157：两项完整逻辑见证

**固定点锚不足以供应全对单步 Hölder。** 在 \(\mathbb R\) 定义

\[
T(x)=\begin{cases}x/2,&x\in\mathbb Q,\\0,&x\notin\mathbb Q.\end{cases}
\]

固定集为 \(\{0\}\)。\(2T-I\) 在有理点为 0、无理点为 \(-x\)，故

\[
|(2T-I)x-(2T-I)0|\le|x|,
\qquad d(x,\operatorname{Fix}T)\le2|x-Tx|.
\]

这是锚 0 的 averaged 条件及线性真步残差 EB。全部轨道以因子至多 \(1/2\)
趋零。但任意 0 邻域含非零有理 \(a\)，无理 \(x_j\to a\) 给

\[
|Tx_j-Ta|=|a|/2>0.
\]

因此该邻域没有任何正阶、有限系数的全对 Hölder 界；并未反驳 SS-TRANSFER。

**集合距离收缩、EB 和一步驻定仍容许不连续极限选择。** 在 `H=\mathbb R^2`，

\[
T(x,y)=\begin{cases}(x,0),&y=0,\\(\operatorname{sgn}y,0),&y\ne0,\end{cases}
\qquad U=[-1,1]^2.
\]

固定集 \(S=\mathbb R\times\{0}\) 闭，\(T(U)\subset U\)，\(T^2=T\)。
取 \(c\equiv0\) 满足上述 Th4 全部条件，且

\[
d(T(x,y),S)=0,\quad d((x,y),S)=|y|\le\|(x,y)-T(x,y)\|.
\]

其有界集残差包络恰为 \(\kappa(t)=\min(t,1)\)：上界由上述不等式，
下界用 \(x=1,0\le y\le1\)。全部路径第一步后驻定，极限 \(\Pi=T\)，
从第 1 步起共同点尾为零；初步尾在 \(U\) 也一致有界。
然而 \(\Pi(0,1/j)=(1,0)\)、\(\Pi(0,-1/j)=(-1,0)\)、\(\Pi(0,0)=(0,0)\)，
所以选择在原点不连续。这两个对象只认证接口不蕴含，未编码成完整 PPA 反例，
也不声称满足 SS1 同图 RL/严格兼容前提。

<a id="sl-lmz-lp"></a>
## LMZ 与 LP22：点误差、参数倒数与有限图

LMZ v1 Th4.4（p.10）在其 `H0`–`H3`、有界 level set、闭

\[
\Omega\subset\Xi\subset\{0\in\partial f\},\quad
\psi(d(x,\Xi))\le\gamma d(0,\partial f(x)),\quad
e_k\le\ell d(x_k,\Xi),\quad
\tau(t)=\psi^{-1}(\gamma b\beta(\ell t)),\quad
\limsup_{t\downarrow0}\tau(t)/t<1
\]

等全部门下确给实际点误差 \(\|x_k-\bar x\|=O(\tau(\|x_{k-1}-\bar x\|))\)。
这是指定轨道门，不含全初值共同常数。本项目不将其抽离站立假设调用。
Example4.6（p.11）为 \(f(t)=|t|^{3/2}\) 的固定惩罚系数 \(\mu>0\)：

\[
t_{k+1}=\arg\min_t\{f(t)+\tfrac\mu2(t-t_k)^2\},\qquad
\text{标准步长 }h=1/\mu.
\]

严格凸性给完整唯一输出，唯一零点 0。对任意实初值，输出同号；令

\[
u_k=|t_k|,\quad a=3/(4\mu),\qquad
u_{k+1}=(\sqrt{u_k+a^2}-a)^2
=\frac{u_k^2}{(a+\sqrt{u_k+a^2})^2}.
\]

非零轨道严格递减，极限方程给 0，且 \(u_{k+1}/u_k^2\to4\mu^2/9\)。
全部初值选择恒为零；这一步是本项目直接计算，不是全球坏选择先例排除。

LP22 v2 Lem2.2 给一元半代数非零函数的有理幂首项，指数未预设为正。
Prop3.1 对**闭半代数图**、每个 \(y_*\in\operatorname{ran}F\)、每个紧集 \(K\)，
给存在 \(c,\alpha>0\) 的固定目标 Hölder EB；不要求有限纤维。
Th3.1 的 regularity/inverse pseudo-Hölder 等价还需相对开和 range 局部闭。
Cor3.1 的开逆像式多值 continuity 是 lower semicontinuity，另需 dom 局部闭。
这些存在性不给 SS1 指定数值系数或严格 RLEB 兼容，也不给无限极限的半代数性。
LMZ/LP22 刊本书目已核，刊本与上述固定 arXiv 号/条件的逐条对应仍未闭。

<a id="sl-b93-chh-kr"></a>
## 光滑先例：阶数、束域和相位对象

**B93。** 开 \(\Omega\subset\mathbb R^{m+p}\)，\(F\in C^k,G\in C^{k-1}\)，

\[
N=I-GF,\quad F'(x)G(x)=I_m\text{ 对全部零点},\quad k\ge2.
\]

Th2.1–2.2 在局部不变邻域给到所选零点的二次尾；转成共同双指数尾还需
收小邻域使 \(\sup2\lambda\|x_0-x_\infty\|<1\)。Th3.1 的初值极限为

\[
\Phi\in C^{k-1},\quad\Phi|_{\operatorname{zer}F}=I,\quad\Phi\circ N=\Phi,
\quad D\Phi(x)=I-G(x)F'(x)\ (F(x)=0).
\]

旧稿的同假设 \(C^k\) 已改正；要该阶必须提高 \(F/G\) 前件一阶。

**CHH v2。** Ass1–3 的 clean intersection、\(C^{p,1}\) 流形、consistent
投影近似、切法向残差和导数 Lipschitz 门不能删除。Prop2 的共同几何点尾
在紧局部块 \(K\) 的切初始化束域 \(x_0=x+\eta,\eta\in T_xM\) 上；
Th2 给 \(C^1\)，Th3 在 \(p\ge3\) 门下证明 \(C^2\)/二阶回缩。
安全导入只取 \(p=2/3\) 对应阶；指定证明不补 \(p>3\) 的全 \(C^{p-1}\)。
二阶回缩指初始化曲线 \(t\mapsto\psi(x,t\eta)\) 在 0 的协变加速度为零，
不等同迭代点误差 Q2。

**KR v1。** Prop1/AppendixF 在紧 \(C^r\) 不变流形的法向收缩/支配门
下给连续轨道相位，另 \(\tau(q)<1/m\) 给 \(C^m,1\le m\le r-1\)。
相位比较的是两条流轨道，通常不是到静止点的极限。
逆向构造 §3.2.2 **预设** \(C^r\) 相位；还需紧模板、全域 submersion、

\[
T_xB=\ker DP_x\oplus\ker DG_x
\]

及完备性门。Prop6 的逐纤维不变仅用于法向流；完整流随模板动力学置换纤维。
Prop8 给到流形的集合距离指数尾。Th2 的印刷数值条件

\[
k_4>r(2k_2/k_1)L,\quad\mu=k_4k_3/(2k_2)
\]

自身不推出证明所用 \(\mu>rL\)，除非另闭合 \(k_3/k_1\) 等关系；

\[
L=\max_M\|Df\|=\max_M\|Df_0\|
\]

的对象也须澄清。本项目只登记结构事实，不导入该数值预算；
扰动相位仅记正向不变 \(B_g\) 上的局部结论，不扩为原盆全域。

<a id="sl-p16"></a>
## C158：P16 的安全共同尾及阻断精确印刷式

取正整数 \(k\ge1\)，固定 v1 中 \(f_1,\ldots,f_k\in S_K(I)\)，\(K>0\)：\(f_i\in C^2,f_i'\ne0\)，

\[
f_i''\text{ 局部有界变差},\qquad\sup_I|f_i''/f_i'|\le K.
\]

导数逐点非零不等于全域统一正下界。令 \(Q\) 为这些拟算术均值的积，

\[
D(x)=\max_i x_i-\min_i x_i,\quad\alpha=(3+7e)/3.
\]

**安全共同尾的独立证明。** 以下从函数类直接推出递推；与P16引理相符，
不依赖精确印刷尾式。\(D(x)=0\) 时驻定，以下取 \(d=D(x)>0\)。
在当前坐标区间 \(J=[a,b]\subset I\) 上，递减生成元换成 \(-f_i\) 不改均值，
故可令全部导数正。写 \(P_f=f''/f'\)，\(E_{\pm K}\) 为log-exp均值。
对 \(g_+(t)=e^{Kt},g_-(t)=-e^{-Kt}\)，

\[
(f\circ g^{-1})''=\frac{f'}{(g')^2}(P_f-P_g).
\]

因 \(-K\le P_f\le K\)，两个符号的凸/凹性及Jensen给

\[
E_{-K}(x)\le A_f(x)\le E_K(x).
\]

令 \(w_j=e^{Kx_j}\in[m,M]\)，\(m=e^{Ka},M=e^{Kb}\)，
\(A=k^{-1}\sum_jw_j,B=k^{-1}\sum_j1/w_j\)。
\((w_j-m)(M-w_j)\ge0\) 给 \(A+mMB\le m+M\)，再由平方非负得

\[
AB\le\frac{(m+M)^2}{4mM}=\cosh^2(Kd/2).
\]

因此对缩放直径 \(\delta_n=KD(Q^nx)\)，

\[
\delta_{n+1}\le K(E_K-E_{-K})
=\log(AB)\le2\log\cosh(\delta_n/2),
\]
\[
e^{\delta_{n+1}}-1
\le\sinh^2(\delta_n/2)
=\tfrac12(\cosh\delta_n-1)\le\tfrac12(e^{\delta_n}-1).
\]

局部平方界也直接可证。令 \(\bar x=k^{-1}\sum_jx_j\)，
\(m_f=\min_J f'>0,M_f=\max_Jf'\)。积分 \((\log f')'=P_f\) 给
\(M_f/m_f\le e^{Kd}\)，且 \(\sup_J|f''|\le KM_f\)。
二阶Taylor与线性项均值零、逆函数的 \(1/m_f\) 界给

\[
|A_f(x)-\bar x|
\le\frac{Ke^{Kd}}{2k}\sum_j(x_j-\bar x)^2
\le\frac{Ke^{Kd}}8d^2.
\]

末步方差界由
\(k^{-1}\sum_j(x_j-a)(b-x_j)\ge0\) 得
\(\operatorname{Var}(x)\le(\bar x-a)(b-\bar x)\le d^2/4\)。
把所有生成元相对于同一算术均值的界相加，

\[
D(Qx)\le\tfrac14Ke^{Kd}d^2.
\]

故在 \(0<\delta_n<1\) 时有
\(\delta_{n+1}\le(e/4)\delta_n^2\le\alpha\delta_n^2\)。
合起来得到

\[
e^{\delta_{n+1}}-1\le\tfrac12(e^{\delta_n}-1),
\qquad \delta_{n+1}\le\alpha\delta_n^2\quad(0<\delta_n<1).
\tag{SL3}
\]

固定初始直径上界 \(R<\infty\)，选择 \(0<l<1/\alpha\)，再选整数 \(N\ge0\)，

\[
2^{-N}(e^{KR}-1)<e^l-1.
\]

对全部 \(D(x)\le R\)，\(\delta_N<l\)，`SL3` 归纳得

\[
D(Q^{N+j}x)\le\frac1{\alpha K}(\alpha l)^{2^j}\quad(j\ge0).
\tag{SL4}
\]

每次均值在原坐标最小最大之间；最小递增、最大递减，直径趋零，故全部坐标
收敛到同一 \(M(x)\)，且实际 Euclidean 点误差不超过 \(\sqrt{k}D(Q^nx)\)。
`SL4` 加有限前缀给全初值共同 \(A\exp(-c2^n)\) 尾，\(A,c\) 可依赖

\[
K,R,k,l,N,\quad c=2^{-N}\log(1/(\alpha l))>0.
\]

不要求初值位置有界；必须冻结直径和 \(K\)。\(R=0\) 单独为驻定轨道。
这不是对 v1 Th2/Th3 精确式的验收。

**精确印刷式的解析阻断。** v1 p.4 Th2 定义

\[
\mu=\min_{0<l<1}(\alpha l)^{(e^l-1)/2}\in(0,1),\quad
\xi\text{ 为一个取最小值的内点},\quad
n_1(D)=\log_2(e)KD-\log_2(e^\xi-1)+1,
\]

其最小值存在且 \(0<\mu<1\)：该正连续函数在 \(l\downarrow0\) 趋1，
在 \(l=1\) 的连续延拓大于1，而取 \(0<l<1/\alpha\) 时小于1，故正最小值在内部。
并印刷 \(D(Q^nx)<B_n(D(x))\)（\(n\ge n_1(D(x))\)），其中

\[
B_n(D)=\frac1{\alpha K}\mu^{\,2^n/(e^{KD}-1)}.
\tag{SL5-printed}
\]

取合法 \(I=\mathbb R,K=1,k=2,f_1(t)=t,f_2(t)=e^t\)。两函数 \(C^\infty\)，
导数处处非零，二阶导数局部有界变差，且两导数商分别为 0 和 1。
两均值的直径精确递推

\[
d_{j+1}=\log\cosh(d_j/2)=d_j^2/8+O(d_j^4).
\]

固定整数 \(N\ge1\)，归纳给

\[
d_N=8^{-(2^N-1)}d^{2^N}(1+o(1))\quad(d\downarrow0).
\]

选固定 \(N>1-\log_2(e^\xi-1)+1\)，则小 \(d>0\) 时 \(N>n_1(d)\)。
但 `SL5-printed` 的对数为

\[
\log B_N(d)=\frac{2^N\log\mu}{d}+O(1).
\]

它比任意正幂更快趋零，因此 \(d_N/B_N(d)\to\infty\)，阻断所印全量词精确界。
极限身份还直接给 \(M(Qx)=M(x)\)；夹逼 \(\min x\le M(x)\le\max x\) 保证对角连续。
Th3（p.5）的精确近似式也受阻：取不变函数 \(F=M\)、\(\varphi=I\)，
两坐标若各距 \(M\) 至多 \(B_N\)，必有 \(d_N\le2B_N\)，同样矛盾。
这里只否定这两个显示式；Th3 的 \(F=\varphi\circ M\) 身份和上述安全共同尾未被否定。
Th1 的起点需另作非负截断，不能在 \(D=0\) 求 \(\log0\)。
**固定有限证书。** 还可取 \(d=1/10000,N=8\)，用有理数界避免浮点或求解 \(\mu\)。
有 \(1<\alpha=(3+7e)/3<8\)。最小化函数的对数导数为
\[
\frac12\left[\frac{e^l-1}{l}+e^l\log(\alpha l)\right].
\]
当 \(0<l\le e^{-2}/\alpha\) 时，\((e^l-1)/l\le e^l\) 且
\(\log(\alpha l)\le-2\)，导数严格负，故任一最小化点
\(\xi>e^{-2}/\alpha>1/64\)（用 \(e^2<8,\alpha<8\)）。
于是 \(n_1(d)<7+2d<8\)。另取 \(l=1/(2\alpha)\)，得
\(\mu\le2^{-1/(4\alpha)}\le2^{-1/32}\)；由 \(e^d-1\le2d\) 得
\[
B_8(d)\le2^{-40000}.
\]
对 \(0\le t\le1\)，函数 \(\log\cosh(t/2)\) 的二阶导数
\(1/(4\cosh^2(t/2))\ge1/8\)，其值和一阶导数在0均为0，
故 \(\log\cosh(t/2)\ge t^2/16\)。此递推保持 \(0<d_j\le1\)，因而
\[
d_8\ge16^{-(2^8-1)}d^{2^8}>2^{-4604}>2B_8(d).
\]
同一固定合法输入及固定迭代数同时阻断印刷直径界和每坐标精确界。
这补充上述渐近证明，不改变安全共同尾的结论。

本次另读 [IM PAN官方刊本](https://www.impan.pl/shop/publication/transaction/download/product/91474)：
v1 Th1/Th2对应正式Th3.2/Th3.3（p.219），Lem4.3/4.4分别p.224/p.225，
正AGM应用在§5 pp.226–227。正式Th3.3仍印同一分母与 \(n_1\)，
所以上述非恒定合法初值的解析证书同样阻断这条正式精确界。
正式前置条件已排除恒定初值，不能把v1的 \(D=0\) 缺口移过去。
正式证明p.226用 \(n^*\) 的代换链，区别于v1；此处不混用两版本证明步骤。
v1 Th3的不变函数应用只按v1引用，未找到刊本相应定理，不擅编号对应。

AGM 正坐标应用（v1 §3.2 pp.6–7）用 \(t,\log t\)，\(K=1/x_{\min}\)。
轴不在该函数域；\(x_{\min}\downarrow0\) 不能给共同 \(K\)。任意连续

\[
\varphi\circ M
\]

只改变复合函数，不能任意指定固定生成元已经决定的 \(M\)。
