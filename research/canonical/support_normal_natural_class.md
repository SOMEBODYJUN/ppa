# 支撑函数与法锥：完整原图、两条证书及反馈边界

本页从固定来源的全部528 LF独立重建数学，不以其历史“已审”“已执行”标签作证明。C191固定三角原关系；C192固定反馈原关系；C193分别核同对象的证书障碍与退化例外。直接数学状态为 `derived-checked`，外部接触/塑性论文的应用身份及历史执行记录仍未验收。来源、逐单元去向与未闭门见[本次范围记录](../audit/NATURAL_CLASS_COVERAGE_2026_10_07.md)。

<a id="sn-object"></a>
## 对象与统一类型

固定整数 \(m,r\ge1\)，使用 \(E=\mathbb R^m\times\mathbb R^r\) 的Euclidean乘积范数。令 \(D\subset\mathbb R^m\) 非空紧凸，
\[
 \sigma_D(t)=\max_{v\in D}\langle t,v\rangle,\quad
 V_D(t)=\{v\in D:\langle t,v\rangle=\sigma_D(t)\}.
\]
本页的凸次梯度 \(\partial\sigma_D(t)\) 恰为 \(V_D(t)\)。令 \(C\subset\mathbb R^r\) 非空闭凸且 \(0\in C\)，法锥的完整约定是
\[
 N_C(y)=\{n:\langle n,z-y\rangle\le0\ (z\in C)\}\quad(y\in C),
 \qquad N_C(y)=\varnothing\quad(y\notin C).
\]
固定 \(b,\lambda,a>0\)、\(0<\alpha<1\)，矩阵 \(M\) 满足
\((M+M^\top)/2\succeq aI\)。固定 \(f\notin D\)，记
\[
 d_D=d(f,D)>0,\qquad R_D=\max_{v\in D}\|f-v\|,\qquad
 k=(1+\lambda a)^{-1}\in(0,1). \tag{SN1}
\]
这里 \(d_D,R_D\) 是不同的原数据优化量，\(R_D\) 不是RL输入对尺度；\(k\) 不是迭代指标。图点输出记 \((t,y)\)，近端输入记 \((p,\xi)\)。完整 \(J_{\lambda F}\) 始终是集合值纤维；证明全部纤维单点后，以 \(T\) 记其唯一输出。反射是 \(Q=2T-I\)，RL按 \(\mathrm{RL}(\lambda,\alpha,L;\delta)\) 排列。真残差为完整 \(r_F(u)=\inf_{w\in F(u)}\|w\|\)，空纤维取 \(+\infty\)。

<a id="sn-elementary"></a>
## 所用凸几何和近端事实的直接证明

非空闭凸集的最近点存在：将距离极小序列限制在有界球，有限维紧性给极小点；平方范数严格凸给唯一性。沿任意线段的一侧导数给
\[
 z=P_Cx\iff z\in C,\quad\langle x-z,w-z\rangle\le0\ (w\in C).
\tag{SN2}
\]
将两个投影不等式相加，得
\(\|P_Cx-P_Cx'\|^2\le\langle P_Cx-P_Cx',x-x'\rangle\)，故投影非扩张。相同相加法给法锥单调性。

支撑函数的次梯度定义是 \(\sigma_D(z)\ge\sigma_D(t)+\langle v,z-t\rangle\) 对全部 \(z\) 成立。取 \(z=0,2t\) 得 \(\langle v,t\rangle=\sigma_D(t)\)；进而 \(\langle v,z\rangle\le\sigma_D(z)\) 对全部 \(z\) 成立。若 \(v\notin D\)，令 \(v_0=P_Dv\)、\(h=v-v_0\ne0\)，SN2给 \(\langle h,v\rangle>\max_{w\in D}\langle h,w\rangle\)，矛盾。因此次梯度恰为上述非空紧面 \(V_D(t)\)。任意两次梯度不等式相加给其单调性。

对 \(s\ge0\) 定义 \(T_s(p)\) 为下面严格凸问题的唯一最小点：
\[
 \min_t\left\{\tfrac12\|t-p\|^2+\lambda s[\sigma_D(t)-\langle f,t\rangle]\right\}.
\tag{SN3}
\]
线性增长的支撑函数使目标强制增长，故极小点存在。还可直接构造：若 \(s>0\)，置 \(u=p+\lambda sf\)、\(z=P_{\lambda sD}u\)、\(t=u-z\)。SN2说明 \(v=z/(\lambda s)\in V_D(t)\)，于是
\[
 t+\lambda s(v-f)=p. \tag{SN4}
\]
反过来SN4与次梯度不等式使SN3的任意其它点目标至少增加 \(\|t'-t\|^2/2\)，所以它精确表征全部解。\(s=0\) 时 \(T_0(p)=p\)，可任取 \(v\in V_D(p)\)。这证明了完整近端公式，不依赖未声明的凸次微分存在性定理。

同一 \(s\) 的两式SN4相减，以次梯度单调性得
\[
 \|T_sp-T_sp'\|^2\le\langle T_sp-T_sp',p-p'\rangle,
 \quad\|(2T_s-I)p-(2T_s-I)p'\|\le\|p-p'\|.
\]
同一 \(p\) 的两式按 \(s(v-v')+(s-s')(v'-f)\) 分解，得
\[
 \|T_s(p)-T_{s'}(p)\|\le\lambda R_D|s-s'|,\qquad
 \|T_s(p)-p\|\le\lambda sR_D. \tag{SN5}
\]
第一式对 \(s=0\) 也成立，不除以 \(s\)。这些估计量化全部活动面。

<a id="sn-triangular"></a>
## C191-v1：三角原图的全输入纤维、全对模和真误差界

定义完整关系
\[
 F_A(t,y)=\{(b\|y\|^\alpha(v-f),My+n):v\in V_D(t),\ n\in N_C(y)\}
 \quad(y\in C), \qquad F_A(t,y)=\varnothing\quad(y\notin C). \tag{SN6}
\]
其完整零集为 \(S_A=\mathbb R^m\times\{0\}\)。法向逆
\[
 K_A=(I+\lambda(M+N_C))^{-1}:\mathbb R^r\to C
\]
在全部输入唯一存在，并满足 \(K_A0=0\)、\(\operatorname{Lip}K_A\le k\)。完整纤维为
\[
 J_{\lambda F_A}(p,\xi)=\{T_A(p,\xi)\},\qquad
 T_A(p,\xi)=\bigl(T_{b\|K_A\xi\|^\alpha}(p),K_A\xi\bigr).
\tag{SN7}
\]
对每个 \(\delta>0\)，同一完整图的全部图点对在Minty输入对距 \(\le\delta\) 时满足
\[
 \mathrm{RL}(\lambda,\alpha,L_\delta;\delta),\qquad
 L_\delta=\delta^{1-\alpha}+2\lambda bR_Dk^\alpha.
\tag{SN8}
\]
这不是无界全尺度的有限次线性Hölder常数；\(m\ge1\) 时沿 \(\xi=0\) 的切向恒等输入已阻止该误读。完整原算子残差独立满足
\[
 d((t,y),S_A)=\|y\|\le\psi(r_{F_A}(t,y)),\qquad
 \psi(s)=(bd_D)^{-1/\alpha}s^{1/\alpha}. \tag{SN9}
\]
SN9在有限残差域 \(\mathbb R^m\times C\) 上成立；域外可按 \(\psi(+\infty)=+\infty\) 解释。没有用选中图值替代inf。

**法向全部输入的证明。** 置 \(B=I+\lambda M\)、\(c=1+\lambda a\)，取 \(0<\eta<2c/\|B\|^2\)。由SN2，映射
\(z\mapsto P_C[z-\eta(Bz-\xi)]\) 的Lipschitz系数至多 \(\rho=(1-2\eta c+\eta^2\|B\|^2)^{1/2}<1\)。从任一点反复应用，相邻差按 \(\rho^j\) 控制；几何级数使序列Cauchy，闭集 \(C\) 中的极限为不动点，距离收缩又给唯一性。SN2把不动点等价为 \(\xi\in z+\lambda(Mz+N_C(z))\)。两解相减，用强单调性得 \(\|z-z'\|\le k\|\xi-\xi'\|\)。零输入的解为0。另用普通单调性得到 \(2K_A-I\) 非扩张。

**完整纤维、图闭性及RL。** 法向方程唯一给 \(z=K_A\xi\)，然后SN4处理完整切向面，得到SN7及其逆向，故未漏分支。SN6图闭：收敛图点序列的面值 \(v_j\in D\) 可抽收敛子列，极限仍在同一支撑面；\(n_j=w_{j,\mathrm{normal}}-My_j\) 收敛，SN2的法锥不等式取极限即可。
对两输入 \(x=(p,\xi),x'=(p',\xi')\)，先把参数 \(s'=b\|K_A\xi'\|^\alpha\) 固定，切向与法向两个非扩张反射的乘积仍非扩张；再用SN5及
\(\big|\|K_A\xi\|^\alpha-\|K_A\xi'\|^\alpha\big|\le k^\alpha\|\xi-\xi'\|^\alpha\)。得到
\[
 \|Q_Ax-Q_Ax'\|\le\|x-x'\|+2\lambda bR_Dk^\alpha\|x-x'\|^\alpha,
\]
即SN8。全部输入唯一性使该式正好对应全部图点对。

**零集与EB。** 每个面值都在 \(D\)，故每个完整图值的切向范数至少为 \(bd_D\|y\|^\alpha\)，对全部图值取inf即得SN9。\(y\ne0\) 时不可能有零图值；\(y=0\) 时切向为零、法向可取 \(n=0\)，故零集精确等于 \(S_A\)。此EB推导不使用 \(M,a,K_A\) 或近端单值性。

<a id="sn-compatible"></a>
## 同一实例的临界兼容与定量半径

若 \(R_Dk^\alpha<d_D\)，置 \(\Delta=d_D-R_Dk^\alpha>0\)，先取
\[
 0<\delta<(2\lambda b\Delta)^{1/(1-\alpha)},\qquad
 0<r\le\delta,\quad r^{1-\alpha}<2\lambda bd_D-L_\delta.
\]
同一全域gauge与同一RL尺度在 \(0<d\le r\) 给
\[
 \psi\left(\frac{d+L_\delta d^\alpha}{2\lambda}\right)\le\kappa_r d,
 \qquad\kappa_r=\left(\frac{r^{1-\alpha}+L_\delta}{2\lambda bd_D}\right)^{1/\alpha}<1.
\tag{SN10}
\]
全部最近零点 \((p,0)\) 属于同一完整图，coverage为全输入，gauge全域；可取开域 \(E\)，留域预算无有限边界。于是这是C02-v2/C185的可调用完整实例。若另截局部图块，仍须按该图块重新检查全纤维与长度留域，不能继承全图的名称。

若取 \(r=\delta\)，SN10的严格门化为 \(r^{1-\alpha}<\lambda b(d_D-R_Dk^\alpha)\)，不能只检先选δ的较弱条件。若声称半径r输入球的全部点对，安全取 \(\delta=2r\)，并检 \(r^{1-\alpha}+(2r)^{1-\alpha}+2\lambda bR_Dk^\alpha<2\lambda bd_D\)。只与最近解输入比较时，\(r\le\delta\) 已足够。这些 \(L_\delta\) 与gauge系数是安全上界，未宣称每个锚的最优系数。

圆盘例：\(D=\overline B_1(0), C=\mathbb R_+, M=7, \|f\|=3,b=\lambda=1,\alpha=2/3\)。此时 \(d_D=2,R_D=4,k=1/8,k^\alpha=1/4\)，完整输出为
\[
 z=\xi_+/8,\quad s=z^{2/3},\qquad
 T_A(p,\xi)=(\operatorname{shrink}(p+sf,s),z),\quad
 \operatorname{shrink}(u,s)=\begin{cases}(1-s/\|u\|)u,&\|u\|>s,\\0,&\|u\|\le s.\end{cases}
\]
这是SN3投影公式在球上的直接计算，包含静止面全部图值。取 \(\delta=r=1/8\)，SN8/SN9/SN10分别给 \(L_\delta=5/2\)、gauge系数 \(2^{-3/2}\)、\(\kappa_r=(3/4)^{3/2}<1\)。

该圆盘例的同一完整轨道还有一条带方向门的解析式：令 \(f=3e_1\)、\(t_0=\tau e_1\)、\(\tau\ge0\)、\(y_0>0\)，则全部 \(j\ge0\) 有
\[
 y_j=8^{-j}y_0,\qquad
 t_j=\left[\tau+\tfrac23 y_0^{2/3}(1-4^{-j})\right]e_1.
\tag{SN-CIRCLE}
\]
确实，归纳得到 \(t_j\) 的系数非负，当前载荷 \(s=y_{j+1}^{2/3}=4^{-(j+1)}y_0^{2/3}>0\)，故 \(t_j+3se_1\) 始终在同一正方向且范数大于s。shrink给 \(t_{j+1}=t_j+2se_1\)；对几何增量求和就是显示公式。没有 \(\tau\ge0\) 时活动方向可能改变，这条解析式不予沿用。
若 \(D=\operatorname{conv}\{v_i\}_{i=1}^N\)，支撑面恰为最大内积顶点的凸包，\(R_D=\max_i\|f-v_i\|\)，\(d_D\) 是到该凸包的投影距离。这些是C191的不同数据形态，不是独立新定理。

<a id="sn-direct"></a>
## 独立的法向与切向收敛证明

C191任意初值 \(x_0=(t_0,y_0)\in E\) 的完整轨道都存在，且
\[
 \|y_{j+1}\|\le k\|y_j\|,\qquad
 \|t_{j+1}-t_j\|\le\lambda bR_D\|y_{j+1}\|^\alpha. \tag{SN11}
\]
因此对全部 \(j\ge0\)，
\[
 \sum_{i\ge j}\|t_{i+1}-t_i\|\le
 \frac{\lambda bR_D k^{\alpha(j+1)}}{1-k^\alpha}\|y_0\|^\alpha,\quad
 \sum_{i\ge j}\|y_{i+1}-y_i\|\le
 \frac{1+k}{1-k}k^j\|y_0\|. \tag{SN12}
\]
和的上界来自两坐标步长之和，控制真实Euclidean路径长度。轨道趋于某个 \((t_\infty,0)\)；距离Q因子上界为 \(k\)，点误差R因子上界为 \(k^\alpha\)，不声称点误差Q比值或锐因子。该证明不要求SN10，甚至允许 \(f\in D\)：此时仍按最大距离定义 \(R_D\)，法向强单调性及 \(\langle n,y\rangle\ge0\) 独立强迫零图值的 \(y=0\)。但 \(d_D>0\) 的高阶EB和下文障碍不能随之保留。

<a id="sn-feedback"></a>
## C192-v1：反馈原图、全输入存在与小载荷唯一性

本节法向维数为1，\(C=\mathbb R_+\)。重新固定全局 \(\ell\)-Lipschitz函数 \(a(t)\ge a_0>0\)、\(\ell\ge0\)，并令 \(k=(1+\lambda a_0)^{-1}\)。保留相同 \(D,f\notin D,b,\alpha,\lambda\)，完整关系为
\[
 F_B(t,y)=\{(by^\alpha(v-f),a(t)y+n):v\in V_D(t),\ n\in N_{\mathbb R_+}(y)\}\quad(y\ge0),
\tag{SN13}
\]
域外为空。它闭，零集仍为 \(S_B=\mathbb R^m\times\{0\}\)，真EB仍为SN9；闭性与EB同C191，使用 \(a\) 连续。

**全输入存在（由原方程补出的独立论证）。** 输入 \((p,\xi)\) 的任何法向解必须为 \(y=\xi_+/(1+\lambda a(t))\)。若 \(\xi\le0\)，唯一完整输出是 \((p,0)\)。若 \(\xi>0\)，在紧区间 \(0\le z\le k\xi\) 定义连续函数
\[
 h(z)=z[1+\lambda a(T_{bz^\alpha}(p))].
\]
SN5保证连续，\(h(0)=0\)，\(h(k\xi)\ge\xi\)，故中间值性质给 \(h(z)=\xi\)。配上 \(t=T_{bz^\alpha}(p)\) 即为完整输出；反过来每个完整输出都如此产生。根集非空紧，故完整 \(J_{\lambda F_B}(p,\xi)\) 非空紧。此结论是全域存在，不是全域单值。

固定 \(Q>0\)，令
\[
 \theta=\alpha\lambda^2 bR_D\ell k^{\alpha+1}Q^\alpha,
 \qquad\beta=\lambda\ell k^2Q.
\tag{SN14}
\]
若 \(\theta<1\)，对整个双侧输入条带 \(E_Q=\{(p,\xi):\xi_+\le Q\}\) 的全部完整近端纤维唯一，记唯一映射 \(T_B\)。定义认证图块
\(\mathcal G_Q=\{(u,w)\in\operatorname{gph}F_B:u+\lambda w\in E_Q\}\)；因此输入条带内的完整排他已核，条带外并未断言单值。
对任意 \(\delta>0\)，该图块在输入对距 \(\le\delta\) 满足
\[
 \mathrm{RL}(\lambda,\alpha,L_{\delta,Q};\delta),\qquad
 L_{\delta,Q}=\frac{2\lambda bR_Dk^\alpha(1+\beta)}{1-\theta}
 +\left[\frac{2(1+\beta)}{1-\theta}+2k+1\right]\delta^{1-\alpha}.
\tag{SN15}
\]

**全部纤维的唯一性和比较证明。** 对候选切向点 \(t\)，置
\[
 z(t,\xi)=\frac{\xi_+}{1+\lambda a(t)},\quad
 s(t,\xi)=b\xi_+^\alpha(1+\lambda a(t))^{-\alpha},\quad
 \Phi_{p,\xi}(t)=T_{s(t,\xi)}(p).
\]
完整方程等价为 \(t=\Phi_{p,\xi}(t)\)。标量函数 \(u\mapsto(1+\lambda u)^{-\alpha}\) 在 \(u\ge a_0\) 上的Lipschitz常数为 \(\alpha\lambda k^{\alpha+1}\)。SN5使整个 \(\mathbb R^m\) 上的 \(\Phi\) 为系数 \(\le\theta\) 的收缩，几何级数构造给其唯一不动点。两组输入的完整输出由同一比较得到
\[
 \|t-t'\|\le\frac{\|p-p'\|+\lambda bR_Dk^\alpha|\xi-\xi'|^\alpha}{1-\theta},
 \quad |z-z'|\le k|\xi-\xi'|+\beta\|t-t'\|.
\tag{SN16}
\]
最后 \(\|(2T_B-I)x-(2T_B-I)x'\|\le2(1+\beta)\|t-t'\|+(2k+1)\|x-x'\|\)，给SN15。固定 \(R_Dk^\alpha<d_D\) 时，先缩 \(Q\)，再缩 \(\delta\)，使 \(L_{\delta,Q}<2\lambda bd_D\)，最后按SN10选距离窗 \(r< Q\)。取开输入域 \(\xi<Q\)，轨道的法向输出在 \(0\le y\le k\xi_+<Q\)，切向无边界；要直接调用一般局部定理可再检其严格长度预算。不能仅凭条带RL写成完整全图RL。

**全部选择的全域直接收敛。** 全域存在已证；对任意完整合法选择都满足
\(0\le y_{j+1}\le k(y_j)_+\)，切向步仍由SN5控制。于是任意初值、任意全部近端选择的轨道均有限长，并有用 \(\|y_0\|=|y_0|\) 表示的SN12上界。它们可收敛到不同切向极限；全选择收敛不意味着全域单值。若从 \(E_Q\) 出发则全过程在条带，成为唯一完整轨道。此证明独立于SN15和临界兼容。

**全域单值性的明确反例。** 取 \(m=1,D=[-1,1],f=2,b=\lambda=1,\alpha=1/2\)，并令
\[
 a(t)=\begin{cases}9,&t\le1,\\17-8t,&1\le t\le2,\\1,&t\ge2.\end{cases}
\]
此函数全局8-Lipschitz且 \(a\ge1\)。输入 \((p,\xi)=(0,9)\) 的正切向输出满足 \(t=\sqrt y\)（面值为1），以及 \(t^2[1+a(t)]=9\)。有根 \(t=3/\sqrt{10}<1\)、\(t=3/\sqrt2>2\)；中间段左端取值10、右端取值8，又有一个根在 \((1,2)\)。三者均给完整图值 \((-t,9-t^2)\)，Minty输入正是 \((0,9)\)。因此此处完整近端至少三值，全图任何零消失全对模也失败。这不反驳小条带的SN14–16。

对负法向初值，第一步即到 \((t_0,0)\) 并驻定；所以来源双侧输入范围内的 \(y_{j+1}\le ky_j\) 须改为上述正部版本，或另限 \(y_0\ge0\)。此外本反馈关系的“法向信息可用”不等于联合变量上的全对部分单调性：取上例 \(t_1=2,t_2=1,y_1=2,y_2=1\)，法向配对为 \((2-1)(1\cdot2-9\cdot1)=-7\)。本页只使用已经证明的法向更新界，未赋予任何未定义的PSM命名证书。

<a id="sn-failures"></a>
## C193-v1：固定二次锚证书、最佳指数与不可删除的例外

在C191另加 \(C\ne\{0\}\)，C192保持其半直线法向。每个解输入 \((p,0)\) 附近，完整唯一局部映射 \(T\) 和反射 \(Q\) 都不calm；任意 \(\gamma>\alpha\) 的局部锚Hölder界、因而全对Hölder界均失败。

对C191取 \(0\ne w\in C\)、\(y_\varepsilon=\varepsilon w\)（\(0<\varepsilon\le1\)，凸性保证属于 \(C\)）、\(\xi_\varepsilon=(I+\lambda M)y_\varepsilon\)。法锥可取0，故 \(K_A\xi_\varepsilon=y_\varepsilon\)。由SN4，切向输出相对 \(p\) 的差至少为 \(\lambda bd_D\|y_\varepsilon\|^\alpha\)，而输入差为 \(O(\varepsilon)\)。反射切向差是两倍同一差。C192取固定 \(p\)、\(\xi\downarrow0\)，SN5先给 \(t-p=O(\xi^\alpha)\)，故 \(a(t)\to a(p)\)、\(y\sim\xi/(1+\lambda a(p))\)，再用同一切向下界。结合SN8/SN15，最大局部指数精确为 \(\alpha\)。

固定任意解锚 \(\bar u=(\bar t,0)\) 和任何有限矩阵 \(V\)。下列明确的二次锚不等式不能在其任何图邻域对全部图点成立：
\[
 \langle u-\bar u,w^*\rangle\ge-\langle w^*,Vw^*\rangle,
 \qquad (u,w^*)\in\operatorname{gph}F. \tag{SN17}
\]
这包含 \(V=\tau I\)、任意固定有限 \(\tau\ge0\)，也包含任意有界符号矩阵；只排除此精确定义，不据“weak-Minty/partial/averaged”等文献名称排除未核版本。

**证明。** 令 \(v_0=P_Df\)、\(e=(f-v_0)/d_D\)。SN2给 \(\langle e,v-f\rangle\le-d_D\) 对全部 \(v\in D\)。取 \(0<\eta<\alpha\)、\(t_\varepsilon=\bar t+\varepsilon^\eta e\)，C191取 \(y_\varepsilon=\varepsilon w\)（固定非零 \(w\in C\)）；C192取 \(y_\varepsilon=\varepsilon\)。任取支撑面值，法锥取0，所得完整图值满足
\[
 \langle u_\varepsilon-\bar u,w_\varepsilon^*\rangle
 \le-c\varepsilon^{\alpha+\eta}+O(\varepsilon^2),\qquad
 \|w_\varepsilon^*\|^2=O(\varepsilon^{2\alpha}),\quad c>0.
\]
C192的 \(a(t_\varepsilon)\) 局部有界。由于 \(\alpha+\eta<2\alpha<2\)，左端负项支配任何固定矩阵二次项，SN17失败。图点和图值同时趋于 \((\bar u,0)\)，不是远端反例。

**退化例外 \(C=\{0\}\)。** C191的合法原数据允许此集合，但此时完整关系精确为 \(F_A(t,0)=\{0\}\times\mathbb R^r\)，域外为空。故完整 \(T_A(p,\xi)=(p,0)\)、\(Q_A(p,\xi)=(p,-\xi)\) 均1-Lipschitz；SN17以 \(V=0\)（即 \(\tau=0\ge0\)）成立。来源摘要不加此门便宣称两类都排除旧锚证书，是过宽概括；来源定理A第6项的 \(C\ne\{0\}\) 门必须携带。SN11–12又说明即使非退化时，法向收缩加切向增量也能独立证明同一Euclidean PPA收敛，不能宣称一切旧partial分析失效。

<a id="sn-smooth"></a>
## 光滑筛选引理及其准确范围

令单值 \(F:\mathbb R^n\to\mathbb R^n\) 在零点 \(p\) 附近 \(C^1\)，完整零集在该处与嵌入 \(C^1\) 流形 \(S\) 一致；令 \(G=I+\lambda F\)。假设有输出邻域 \(V\ni p\)、输入邻域 \(U\ni p\) 及单值 \(J:U\to V\)，满足 \(G(Jx)=x\)，且 \(J(G(u))=u\) 对所有充分近 \(p\) 的 \(u\in V\) 成立。只要求一个右逆不足。若同一输入邻域还有 \(d(Jx,S)\le\kappa d(x,S)\)、\(0\le\kappa<1\)，则 \(DG(p)\) 可逆，因而该局部逆Lipschitz。

若 \(DG(p)v=0\)、\(v\ne0\)，则 \(DF(p)v=-v/\lambda\)。沿流形曲线求导，\(DF(p)\) 在 \(T_pS\) 上为0，故 \(v\notin T_pS\)。流形写成其切空间上的 \(C^1\) 图，余项为 \(o(\|h\|)\)，直接取近点和近似极小点得到
\(d(p+tv,S)=|t|d(v,T_pS)+o(|t|)\)。而 \(G(p+tv)=p+o(t)\)，用已声明的双侧逆和距离收缩，得到左端正一阶距离 \(\le\kappa o(|t|)\)，矛盾。有限维单射线性映射即可逆。最后写 \(G(p+h)=p+Ah+R(h)\)、\(A=DG(p)\)，缩球使 \(\operatorname{Lip}R\le1/(2\|A^{-1}\|)\)。对足够近输入 \(x\)，\(h\mapsto A^{-1}(x-p-R(h))\) 在该闭球自映射且收缩；唯一解的差满足 \(\|h-h'\|\le2\|A^{-1}\|\|x-x'\|\)。这给局部Lipschitz，不借未核外部逆函数定理。该筛选引理不为任意光滑KKT模型核流形、全输入coverage或双侧逆门。

<a id="sn-source"></a>
## 来源与未闭义务

来源固定为历史总包中的 `01_RL_PPA核心理论/05_实例与反例/支撑函数与法锥_自然类推导.md`，SHA-256为 `abe082412883506ab76bdcc2b653f7971ecacb82205dd7cbe632186c84e8c2c9`。本页没有把来源§2所报Carpick、Gfrerer–Outrata–Valdman、Carstensen或Kanno的访问/建模断言升级为已核paper fact；这些外部身份及完整工程/PDE模型匹配仍需另行一手核验。本页不需调用那些论文来成立。来源数值及代理审查日志只留来源报告；显示常数由本页精确代数重算。源§7的筛选论证在上节明确了双侧局部逆与同一零流形量词，但不替原生模型验证它们。
