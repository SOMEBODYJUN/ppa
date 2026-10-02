# 解选择的模传递与完整二次反例：独立证明

本模块为 [C08](../../CLAIMS.md) 和 [S01–S03](../solution_selection.md) 补充可以独立使用的证明。主结果是局部 Hölder 单步与共同尾界的模传递，以及一个完整单值 resolvent 的半代数二值模型：敏感参考轨道自身 Q-二次收敛，初值到极限解却没有正阶两点 Hölder 模。

**来源与证据层级。** 来源为 [SS1 修订包](../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip) 内的 research_note.md，定理 1、定理 4 和 §5.1。本模块是逐项独立重构的 derived-checked 证据；下述证明没有调用来源中的审计结论或外部增长二分引理。全图/图块、输入比较尺度、共同尾界及实际点误差的量词均分别写出。未研究先行性。

<a id="ss-transfer"></a>
## 1. SS-TRANSFER · 局部 Hölder 单步和共同尾界

### 精确对象与结论

设 \(E\) 为实范数空间，\(T\) 在包含 \(V\subset E\) 的域上单值。给定初值集 \(B\subset V\)，假设对每个 \(x\in B\)，所有 \(T^kx\) 都有定义、位于 \(V\)，且在 \(E\) 中有极限 \(\Pi(x)\)。不要求 \(B\) 是开集或有界集。给定 \(H,R>0\)、\(0<\gamma<1\)，假设

\[
\|Tu-Tv\|\le H\|u-v\|^\gamma
\quad
(u,v\in V,\ \|u-v\|\le R).
\tag{SS-T1}
\]

以下尾界中的常数须对 **全部 \(x\in B\) 和全部 \(k\ge0\)** 一致。

1. 若 \(\|T^kx-\Pi(x)\|\le M\sigma^k\)，其中 \(M>0\)、\(0<\sigma<1\)，则存在 \(C,\delta_0>0\)，使 \(x,y\in B\)、\(0<\delta=\|x-y\|<\delta_0\) 时
   \[
   \|\Pi(x)-\Pi(y)\|
   \le C\left(\frac{\log\log(1/\delta)}
                         {\log(1/\delta)}\right)^\beta,
   \qquad
   \beta=\frac{\log(1/\sigma)}{\log(1/\gamma)}.
   \tag{SS-T2}
   \]
2. 若 \(\|T^kx-\Pi(x)\|\le M e^{-c_0\nu^k}\)，其中 \(M,c_0>0\)、\(\nu>1\)，则存在 \(C,c,\delta_0>0\)，使
   \[
   \|\Pi(x)-\Pi(y)\|
   \le C e^{-c[\log(1/\delta)]^\alpha},
   \qquad
   \alpha=\frac{\log\nu}{\log(\nu/\gamma)}\in(0,1).
   \tag{SS-T3}
   \]

常数可依赖 \(H,R,\gamma\) 和各项共同尾常数，不依赖这一对初值。极限存在已在假设中给定，因此不另需完备性。

### 证明：先闭合有限前缀的局部尺度

令
\[
A=\max\{1,H^{1/(1-\gamma)}\},\qquad
t=\log(1/\delta),\qquad
d_j=\|T^jx-T^jy\|.
\]
有 \(HA^\gamma\le A\)。若整数 \(n\ge0\) 满足
\[
A e^{-t\gamma^n}\le R,\qquad t>0,
\tag{SS-T4}
\]
则对所有 \(0\le j\le n\)，
\[
d_j\le A e^{-t\gamma^j}.
\tag{SS-T5}
\]
事实上 \(d_0=\delta\le A\delta\)。由于 \(\gamma^j\ge\gamma^n\)，候选上界不超过 (SS-T4) 的左端。若 (SS-T5) 已证至 \(j<n\)，则 \(d_j\le R\)，两个迭代点又都在 \(V\)，故 (SS-T1) 可用，并给
\[
d_{j+1}\le H A^\gamma e^{-t\gamma^{j+1}}
          \le A e^{-t\gamma^{j+1}}.
\]
这同时证明估计和每次调用的适用性。

记 \(a=\log(1/\sigma)\)、\(b=\log(1/\gamma)\)、\(\beta=a/b\)、\(D=\beta+1\)。几何尾情形取
\[
n=\left\lfloor
       \frac{\log[t/(D\log t)]}{b}
   \right\rfloor .
\]
当 \(t\) 足够大时 \(n\ge0\)，且
\[
t\gamma^n\ge D\log t,\qquad
\sigma^n\le \sigma^{-1}D^\beta(\log t/t)^\beta.
\]
因 \(A t^{-D}\to0\)，可取统一的 \(t_0\) 使 (SS-T4) 成立。于是
\[
\begin{aligned}
\|\Pi(x)-\Pi(y)\|
&\le d_n+\|T^nx-\Pi(x)\|+\|T^ny-\Pi(y)\|\\
&\le A t^{-D}
  +2M\sigma^{-1}D^\beta(\log t/t)^\beta\\
&\le [A+2M\sigma^{-1}D^\beta](\log t/t)^\beta
\end{aligned}
\]
对充分大 \(t\) 成立，即 (SS-T2)。

超几何尾情形取 \(d=\log(\nu/\gamma)\)，并令
\[
n=\left\lfloor\frac{\log t}{d}\right\rfloor .
\]
对 \(t\ge1\)，由 floor 的两侧界直接得
\[
t\gamma^n\ge t^\alpha,\qquad
\nu^n\ge \nu^{-1}t^\alpha .
\]
充分大 \(t\) 时 \(Ae^{-t^\alpha}\le R\)，故有限前缀估计仍合法，并有
\[
\|\Pi(x)-\Pi(y)\|
\le A e^{-t^\alpha}+2M e^{-(c_0/\nu)t^\alpha}
\le (A+2M)e^{-\min\{1,c_0/\nu\}t^\alpha}.
\]
这证明 (SS-T3)。

此定理是 \(T\) 的命题。若 \(T=J_{\mathcal G}\) 来自局部图块，要转成完整 \(J_{\lambda F}\) 的结论，仍须在全部比较轨道的共同输入区域证明两者相等；本证明不产生该额外事实。

<a id="ss-quadratic-object"></a>
## 2. SS-Q2 · 一个完整二值半代数算子

取 \(E=\mathbb R^3\)，使用 Euclidean 范数，固定 proximal 参数 \(\lambda=1\)。对 \(y\ge0\) 定义
\[
D_y(\eta)=
\min\left\{
y^{1/4},
\frac{\sqrt{1+4\eta_+}-1}{2}
\right\},
\qquad \eta_+=\max\{\eta,0\}.
\]
定义完整关系
\[
F(\xi,\eta,y)=
\begin{cases}
\{(-y^{1/4},-D_y(\eta),\sqrt y-y),\
  (-y^{1/4},-D_y(\eta),-\sqrt y-y)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}
\tag{SS-Q1}
\]

两个分支在闭半空间 \(y\ge0\) 上连续，故图闭；它们通过有限段的多项式等式、不等式和指定非负根描述，故图半代数。\(y>0\) 时第三分量之差为 \(2\sqrt y>0\)，恰有两个值；\(y=0\) 时两支都是零；\(y<0\) 时无值。因此完整零集为
\[
S=F^{-1}(0)=\mathbb R^2\times\{0\}.
\tag{SS-Q2}
\]

<a id="ss-quadratic-full"></a>
### 2.1 完整 resolvent：逐纤维反演

对每个输入 \(x=(z,p,r)\in\mathbb R^3\)，完整 \(J_F(x)\) 是单点，等于
\[
T(z,p,r)=
\left(z+\sqrt{|r|},\
      p+\sqrt{\min\{p_+,|r|\}},\
      r^2\right).
\tag{SS-Q3}
\]

证明 \(x-u\in F(u)\)，写 \(u=(\xi,\eta,y)\)。两支第三坐标均要求
\[
r=y+(\pm\sqrt y-y)=\pm\sqrt y.
\]
故必有 \(y=r^2\)，在 \(r\ne0\) 时仅与其符号相符的分支可用。第一坐标随后唯一给出
\(\xi=z+y^{1/4}=z+\sqrt{|r|}\)。

令 \(a=|r|\)。第二坐标要求
\[
p=\Phi_a(\eta):=\eta-
\min\left\{\sqrt a,\frac{\sqrt{1+4\eta_+}-1}{2}\right\}.
\]
若 \(a>0\)，它有以下三段：

| 输出第二坐标 \(\eta\) | \(\Phi_a(\eta)\) | 输入像 |
| --- | --- | --- |
| \(\eta\le0\) | \(\eta\) | \((-\infty,0]\) |
| \(0\le\eta\le a+\sqrt a\) | \(v^2\)，其中 \(\eta=v^2+v\)、\(0\le v\le\sqrt a\) | \([0,a]\) |
| \(\eta\ge a+\sqrt a\) | \(\eta-\sqrt a\) | \([a,\infty)\) |

各段严格递增，在接点连续匹配，且像覆盖 \(\mathbb R\)。所以唯一逆为
\[
\eta=p+\sqrt{\min\{p_+,a\}}.
\]
\(a=0\) 时 \(\Phi_0(\eta)=\eta\)，同一逆式仍成立，两个法向分支合为一个零图点。这证明所有符号、接点及整个 proximal 纤维的唯一性。显式式 (SS-Q3) 也给出 \(T\) 半代数。

<a id="ss-quadratic-certificate"></a>
### 2.2 全对 RL、整个纤维的 EB、固定兼容证书

先固定 \(0<R_0<1\)。在输入 collar
\[
V_{R_0}=\mathbb R^2\times[-R_0,R_0]
\]
上，\(T(V_{R_0})\subset V_{R_0}\)。对每个有限 **输入对尺度** \(D>0\)，反射 \(C=2T-I\) 满足
\[
\|Cx-Cx'\|
\le L_{R_0,D}\|x-x'\|^{1/2},
\qquad
L_{R_0,D}=2\sqrt2+(1+4R_0)\sqrt D,
\tag{SS-Q4}
\]
当 \(x,x'\in V_{R_0}\)、\(\|x-x'\|\le D\) 时成立。

为证此式，令 \(\delta=\|x-x'\|\)，并写
\[
h_1=\sqrt{|r|}-\sqrt{|r'|},\qquad
h_2=\sqrt{\min\{p_+,|r|\}}
    -\sqrt{\min\{p'_+,|r'|\}}.
\]
正部、绝对值及 \(\min\) 对无穷范数均为 1-Lipschitz，且
\(|\sqrt u-\sqrt v|\le\sqrt{|u-v|}\) 对 \(u,v\ge0\) 成立，所以
\(|h_1|,|h_2|\le\sqrt\delta\)。函数 \(g(r)=2r^2-r\) 在
\([-R_0,R_0]\) 上的导数绝对值至多 \(1+4R_0\)。于是
\[
Cx-Cx'=(\Delta z,\Delta p,\Delta g)
       +2(h_1,h_2,0)
\]
的范数不超过
\((1+4R_0)\delta+2\sqrt2\sqrt\delta\)，即 (SS-Q4)。
这个估计包含法向输入异号的比较。

具体地，取图块
\[
\mathcal G_{R_0}
=\operatorname{gph}F\cap\{0\le y\le R_0^2\}.
\]
其输入像 \(\{u+v:(u,v)\in\mathcal G_{R_0}\}\) 恰为
\(V_{R_0}\)。对图块中的任意两点，令 \(x=u+v\)、\(x'=u'+v'\)，
则 \(u=Tx\)、\(u'=Tx'\)，且
\[
\|(u-u')-(v-v')\|=\|Cx-Cx'\|.
\]
因此 (SS-Q4) 正是该图块上、在输入比较尺度 \(D\) 的
all-pairs \(\mathrm{RL}(1,1/2,L_{R_0,D})\)。

对所有 \(u=(\xi,\eta,y)\in\operatorname{dom}F\)，**完整最小残差**满足
\[
\begin{aligned}
r_F(u)^2
&=\inf_{v\in F(u)}\|v\|^2\\
&=\sqrt y+D_y(\eta)^2+(\sqrt y-y)^2\\
&\ge\sqrt y.
\end{aligned}
\tag{SS-Q5}
\]
确为第一支取到最小值，因为两支平方差是 \(4y^{3/2}\ge0\)。
所以全域输出 EB 为
\[
d(u,S)=y\le r_F(u)^4,\qquad \psi(t)=t^4.
\tag{SS-Q6}
\]
这也适用于负输入所选的第二支；没有用被选残差代替完整最小残差。

严格兼容可用以下 **预先固定** 的半径，不依赖敏感初值：
\[
K_0=2\sqrt2+2+4R_0,\qquad
R=\min\left\{\frac{R_0}{2},\frac8{K_0^4}\right\}>0.
\tag{SS-Q7}
\]
取 \(U=\mathbb R^3\)、比较尺度 \(D=R\)，并记
\(L_R=2\sqrt2+(1+4R_0)\sqrt R\)。则 \(R\le R_0\)、\(R<1\)，且
\[
\begin{aligned}
\sup_{0<t\le R}
\frac{\psi((t+L_R\sqrt t)/2)}t
&=\frac{R[2\sqrt2+(2+4R_0)\sqrt R]^4}{16}\\
&\le \frac{RK_0^4}{16}\le\frac12<1.
\end{aligned}
\tag{SS-Q8}
\]
因此可取兼容因子 \(\kappa=1/2\)。
\(U_R=\{x:d(x,S)\le R\}\) 的每个完整纤维都在
\(\mathcal G_{R_0}\) 中；最近零点 \((z,p,0)\) 对应的零图点也在该图块。
对 \(x\in U_R\)，令 \(s=(z,p,0)\)、\(d=\|x-s\|=|r|\)。
由 \(Ts=s\) 和 (SS-Q4)，
\(\|2Tx-x-s\|\le L_R\sqrt d\)，因此
\[
r_F(Tx)\le\|Tx-x\|\le\tfrac12(d+L_R\sqrt d).
\]
取 \(\bar t\ge(R+L_R\sqrt R)/2\) 即满足 gauge 定义域要求。
\(U=\mathbb R^3\) 没有出界预算，且完整/图块 resolvent 在整个
\(V_{R_0}\) 一致。于是 coverage、nearest-zero comparison、
finite-scale all-pairs RL、真实残差 EB 和严格兼容属于同一个实例。

<a id="ss-quadratic-tail"></a>
### 2.3 共同超几何尾与逐轨道的确切 Q-二次比值

完整轨道收敛且有限长的初值域恰为
\(\Omega=\mathbb R^2\times(-1,1)\)。\(r_0=0\) 时初值已在 \(S\)，轨道驻定。
对 \(0<a_0=|r_0|<1\)，记
\[
a_k=|r_k|=a_0^{2^k},\qquad b_k=\sqrt{a_k}.
\]
从 \(k=1\) 起 \(r_k=a_k>0\)，而 \(b_{k+1}=b_k^2\)。
第一切向步长为 \(b_k\)，第二切向步长在 \([0,b_k]\)。
定义
\[
\mathscr S(b)=\sum_{j=0}^\infty b^{2^j}
\quad (0<b<1).
\]
因为 \(2^j\ge j+1\)，
\[
b\le\mathscr S(b)\le\frac b{1-b},\qquad
0\le\mathscr S(b)-b\le\frac{b^2}{1-b}.
\tag{SS-Q9}
\]
切向总长度有限；法向从第 1 步起单调下降，初始符号转换也只有一步，
故整条轨道有限长。若 \(|r_0|\ge1\)，则 \(a_k\ge1\)，第一切向坐标
每步增加至少 1，轨道不收敛；这说明上述域是精确边界。

令 \(\Pi(x)=\lim_kT^kx\)、\(e_k(x)=\|T^kx-\Pi(x)\|\)。
第一切向尾精确为 \(\mathscr S(b_k)\)，第二切向尾至多此值，
法向极限为 0。对全部 \(x\in V_{R_0}\)、全部 \(k\ge0\)，
\[
e_k(x)
\le\left(\frac{\sqrt2}{1-\sqrt{R_0}}+1\right)b_k
\le M_0 e^{-c_0 2^k},
\quad
M_0=\frac{\sqrt2}{1-\sqrt{R_0}}+1,\quad
c_0=-\tfrac12\log R_0>0.
\tag{SS-Q10}
\]
这包括负 \(r_0\) 的 \(k=0\)，因为该步法向误差的绝对值仍为
\(a_0\le b_0\)。\(r_0=0\) 时左端为零。

若 \(p_0\le0\)，第二切向坐标恒定。若 \(p_0>0\)，它单调不减且
至少为 \(p_0\)，而 \(a_k\to0\)，故某个有限时刻起满足
\(p_k\ge a_k\)；此后第二切向每步也增加 \(b_k\)。
对充分大 \(k\ge1\)，因此有精确公式
\[
e_k^2=m\mathscr S(b_k)^2+b_k^4,\qquad
m=\begin{cases}1,&p_0\le0,\\2,&p_0>0.\end{cases}
\tag{SS-Q11}
\]
由 \(\mathscr S(b)/b\to1\) 和 \(b_{k+1}=b_k^2\)，
\[
\lim_{k\to\infty}\frac{e_{k+1}}{e_k^2}
=\frac1{\sqrt m}
=
\begin{cases}
1,&p_0\le0,\\
1/\sqrt2,&p_0>0.
\end{cases}
\tag{SS-Q12}
\]
所以每条非驻定的收敛轨道具有确切 Q-二次点误差；包括下节产生坏稳定性的
\(p_0=0\) 参考轨道。第二切向坐标的最终饱和起点可依赖初值，
并未断言整个 collar 共用一个 Q-二次渐近起点。(SS-Q10) 则确实是共同尾界。

<a id="ss-quadratic-selection"></a>
### 2.4 初次饱和时刻与不能提高的根对数指数

固定 \(0<r_0<1\)，比较；以下切换下界本身在此全范围成立。若要同时调用上节**同一个**固定 RLEB collar 证书，则再选 \(0<r_0\le R\)（因而 \(r_0\le R_0\)）：
\[
x_0=(0,0,r_0),\qquad x_\varepsilon=(0,\varepsilon,r_0),
\qquad 0<\varepsilon<r_0.
\]
两轨道的第一、第三坐标完全相同。参考轨道第二坐标恒为零。
另一条轨道满足
\[
p_{k+1}=p_k+\sqrt{\min\{p_k,r_k\}},\qquad
p_0=\varepsilon,\qquad r_k=r_0^{2^k}.
\]
令 \(t=\log(1/\varepsilon)\)、\(a=-\log r_0>0\)、\(h=\log4\)，并定义
\[
N=\min\{k:p_k\ge r_k\}.
\]
\(N\) 有限，因为 \(p_k\ge\varepsilon\) 而 \(r_k\to0\)。
在 \(k<N\) 时 \(0<p_k<r_k<1\)，所以
\(\sqrt{p_k}\le p_{k+1}\le2\sqrt{p_k}\)。
取对数并迭代这一递推，得到 **包括产生切换的第 \(N\) 步** 的共同界
\[
e^{-t2^{-k}}\le p_k\le4e^{-t2^{-k}}
\qquad(0\le k\le N).
\tag{SS-Q13}
\]
在 \(N\) 使用上界、在 \(N-1\) 使用下界：
\[
t\le a4^N+h2^N\le(a+h)4^N,\qquad
t>a4^{N-1}.
\]
因此
\[
\sqrt{\frac t{a+h}}\le2^N<2\sqrt{\frac ta},\qquad
\frac{\sqrt a}{2}\sqrt t<t2^{-N}
\le\sqrt{a+h}\sqrt t.
\tag{SS-Q14}
\]
特别地 \(N=(\log t)/\log4+O(1)\)，且 \(N\to\infty\)。

从 \(N\) 起 \(p_k\) 不减、\(r_k\) 递减，所以永远饱和，且
\[
p_\infty=p_N+\mathscr S(b_N),\qquad
b_N=e^{-(a/2)2^N}.
\tag{SS-Q15}
\]
必须分别估计切换 overshoot \(p_N\) 和饱和尾；
不需也不使用 \(p_N=O(\sqrt{r_N})\)。
由 (SS-Q13)–(SS-Q14)，
\[
p_N\le4e^{-(\sqrt a/2)\sqrt t}.
\]
由 (SS-Q9) 与 (SS-Q14)，
\[
e^{-\sqrt a\sqrt t}
\le b_N\le\mathscr S(b_N)
\le\frac{e^{-[a/(2\sqrt{a+h})]\sqrt t}}
           {1-\sqrt{r_0}}.
\]
故若
\[
c_*=\min\left\{\frac{\sqrt a}{2},
                \frac{a}{2\sqrt{a+h}}\right\}>0,\qquad
K_*=4+\frac1{1-\sqrt{r_0}},
\]
则
\[
e^{-\sqrt a\sqrt t}
\le \|\Pi(x_\varepsilon)-\Pi(x_0)\|
=p_\infty
\le K_*e^{-c_*\sqrt t}.
\tag{SS-Q16}
\]
充分大 \(t\) 时，可将上界写成 \(e^{-(c_*/2)\sqrt t}\)。
同时，(SS-Q4) 给 \(T\) 在 \(V_{R_0}\) 上的局部 \(1/2\)-Hölder 界，
(SS-Q10) 给 \(\nu=2\) 的共同超几何尾；SS-TRANSFER 的指数正是
\(\alpha=\log2/\log4=1/2\)。

对任意 \(\theta>0\)，由下界
\[
\frac{\|\Pi(x_\varepsilon)-\Pi(x_0)\|}
     {\|x_\varepsilon-x_0\|^\theta}
\ge e^{\theta t-\sqrt a\sqrt t}\longrightarrow\infty.
\tag{SS-Q17}
\]
所以任何包含原点的开邻域都不具有正阶两点 Hölder 模：在该邻域里先固定
足够小的 \(0<r_0\le R\)，再令 \(\varepsilon\downarrow0\)。
同一下界排除把共同上界的指数 \(1/2\) 换成任何
\(\alpha'>1/2\)，即排除统一的 \(C'e^{-c't^{\alpha'}}\)，
其中 \(C',c'>0\) 固定。这里未优化指数前常数。

<a id="ss-quadratic-nonsemialgebraic"></a>
### 2.5 结构性推论：极限选择不是半代数

由有限步 \(T\) 的显式式，\(T^k\) 均半代数。然而 \(\Pi\) 在原点的
任何开邻域上都不是半代数映射。此结论可直接用多项式证明，不需增长二分定理。

设反面成立，取充分小的固定 \(r_0>0\)，并限制到直线切片
\[
f(\varepsilon)=\pi_2\Pi(0,\varepsilon,r_0),\qquad
0<\varepsilon<\varepsilon_0 .
\]
半代数映射在该切片及坐标投影下保持半代数，故 \(f\) 的图半代数。
(SS-Q16) 给 \(f(\varepsilon)\to0\)、\(f>0\)，且
\[
\frac{f(\varepsilon)}{\varepsilon^\theta}\to\infty
\quad\text{对每个 }\theta>0.
\tag{SS-Q18}
\]

一个平面中的非空半代数函数图必满足某个非零多项式方程
\(P(\varepsilon,f(\varepsilon))=0\)：取描述其图的有限组非零多项式；
若某图点上它们都非零，所有符号在该点某邻域固定，Boolean 描述也固定，
该图便含有二维开集，矛盾。因此它们的乘积在整图上为零。

从 \(P\) 提出最大的 \(\varepsilon\) 因子，得到非零
\(Q(\varepsilon,y)\)，其中 \(q(y)=Q(0,y)\) 不恒为零，
且仍有 \(Q(\varepsilon,f(\varepsilon))=0\)。
若 \(q(y)=c y^m+O(y^{m+1})\)，\(c\ne0\)、\(m\ge0\)，
则在充分小的正 \(\varepsilon\) 上
\[
|q(f(\varepsilon))|\ge c_1f(\varepsilon)^m,\qquad
|Q(\varepsilon,f(\varepsilon))-q(f(\varepsilon))|\le C_1\varepsilon,
\]
后式因差为 \(\varepsilon\) 乘以一个在原点附近有界的多项式。
所以 \(c_1f(\varepsilon)^m\le C_1\varepsilon\)。
\(m=0\) 时已矛盾；\(m>0\) 时给
\(f(\varepsilon)\le C_2\varepsilon^{1/m}\)，与 (SS-Q18) 矛盾。

结论只涉及半代数性，未判定在其它 o-minimal 结构中的可定义性。

## 3. 可使用的范围

- SS-TRANSFER 需要同一初值集合上的共同轨道区域和共同点尾常数；逐初值的尾估计不足以代入。
- SS-Q2 的 \(T\) 是全空间完整 inclusion resolvent。收敛域为 \(|r_0|<1\)，共同尾和 RLEB 证书分别在预先固定的 collar 与尺度中给出。
- (SS-Q12) 是每条非驻定轨道的确切 Q-二次比值；(SS-Q10) 是包含敏感参考轨道的整 collar 共同超几何尾，二者量词不同。
- (SS-Q17) 反驳任意邻域内的两点 Hölder 稳定性。它不反驳以某个固定解点为锚点的 Hölder calmness。
- 本模块重构了 SS1 的定理 1、定理 4 及其 §5.1 二次模型推论；几何模型的有限尺度最小 RL 常数、保守证书下的锐性及一般切法向稳定性没有由这些证明解决。
