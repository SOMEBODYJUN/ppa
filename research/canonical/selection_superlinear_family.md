# 超线性法向尾的完整二支近端族

<a id="sf-object"></a>
## C141：完整关系和输入纤维

固定 \(E=\mathbb R^3\)、\(\lambda=1\)、\(0<\gamma<1\)、
\(\nu>1\)、\(A,B>0\)。本页的 \(A,B\) 是标量系数，
\(r\) 是近端**输入**的法向坐标；\(y\) 是图点**输出**的法向坐标。
对 \(a\ge0\) 定义
\[
h_a(p)=p+B\min\{p_+,a\}^{\gamma},\qquad \tau_a=h_a^{-1}.
\]
\(h_a\) 连续、严格递增并满射；\(a=0\) 时为恒等映射。
定义完整关系
\[
F(\xi,\eta,y)=
\begin{cases}
\{(-Aa^\gamma,\tau_a(\eta)-\eta,a-y),
(-Aa^\gamma,\tau_a(\eta)-\eta,-a-y)\},
&y\ge0,\quad a=y^{1/\nu},\\
\varnothing,&y<0.
\end{cases}                                                    \tag{SF-1}
\]
\(\tau_a(\eta)-\eta\) 连续且绝对值至多 \(Ba^\gamma\)，
故图闭；\(S=F^{-1}(0)=\mathbb R^2\times\{0\}\)。
若 \(\gamma,\nu\) 均为正有理数，图及其完整近端为半代数；
对一般实指数不作此断言。

给定**任意** \(x=(z,p,r)\in E\)，剪切方程 \(x=u+v\)
先给 \(r=\pm a\)，故 \(a=|r|,y=|r|^\nu\)；非零 \(r\)
决定唯一一支，零处两支合一。其余坐标依次给
\(\xi=z+A|r|^\gamma\)、\(\eta=h_{|r|}(p)\)。因此
\[
J_F(x)=\{T(x)\},\quad
T(z,p,r)=\bigl(z+A|r|^\gamma,
p+B\min\{p_+,|r|\}^\gamma,|r|^\nu\bigr).          \tag{SF-2}
\]
这逐输入穷尽完整纤维，包括负输入和零处接缝；没有把一条
选中支当成完整 \(J_F\)。\(\nu=2,\gamma=1/2,A=B=1\)
是 [C115/C116](solution_selection_rates.md#ss-quadratic-object) 的同图特例。

<a id="sf-certificates"></a>
## 全对模、真残差与固定兼容半径

先固定 \(0<R_0<1\)，取完整输出图块
\(\mathcal G_{R_0}=\operatorname{gph}F\cap\{0\le y\le R_0^\nu\}\)。
其自然输入域恰为 \(\mathbb R^2\times[-R_0,R_0]\)，且
\(T\) 保持这一输入 collar。对该图块的任意两点，
其输入对距 \(\delta\le D<\infty\) 时，
\(C=2T-I\) 的非线性前两坐标差至多
\(2\sqrt{A^2+B^2}\,\delta^\gamma\)；
第三坐标 \(2|r|^\nu-r\) 在 collar 上的 Lipschitz
常数至多 \(1+2\nu R_0^{\nu-1}\)。于是
\[
\mathrm{RL}(1,\gamma,L_{R_0,D};D),\quad
L_{R_0,D}=2\sqrt{A^2+B^2}
 +(1+2\nu R_0^{\nu-1})D^{1-\gamma}.              \tag{SF-3}
\]
这是**限输出 collar 的全对图块**结论，不宣称完整全图在
任意输入上有统一此常数。取输入 \((0,t,t),(0,t,0)\)
并令 \(t\downarrow0\)，证明全对指数不能大于 \(\gamma\)，
局部系数下确界趋于 \(2\sqrt{A^2+B^2}\)；(SF-3) 不宣称
每个固定 \(D\) 的常数最优。

在 \(u=(\xi,\eta,y)\)、\(y\ge0\)、\(a=y^{1/\nu}\) 处，
两图值第三坐标绝对值的最小值是 \(|a-y|\)，故**完整**真残差为
\[
r_F(u)^2=A^2a^{2\gamma}+(\tau_a(\eta)-\eta)^2
 +(a-y)^2\ge A^2a^{2\gamma},\qquad
d(u,S)=y\le(r_F(u)/A)^{\nu/\gamma}.              \tag{SF-4}
\]
后式取全域 gauge \(\psi(s)=(s/A)^{\nu/\gamma}\)，
没有把选中图值范数冒充 \(r_F\)。沿 \(\eta\le0,a\downarrow0\)
指数及系数渐近取到。

为检查 C02-v2 的**同一个**局部接口，取开放域
\(U=\mathbb R^3\)，选 \(0<R\le R_0\) 作为
初值法向球半径、零锚输入对距及 (SF-3) 的比较尺度
\(D=R\)。此时 \(U_R=\mathbb R^2\times[-R,R]\) 的
每个输入都有完整纤维，且整纤维位于上述图块；最近零锚
\((z,p,0;0)\) 也在图块中。记
\(L_R=L_{R_0,R}\)。对于 \(0<d\le R\)，零锚反射界给
选中图值范数 \(\|v\|\le(d+L_Rd^\gamma)/2\)，而全域
\(\psi\) 在这个数上可评价；直接兼容商不超过
\[
\kappa_R
=R^{\nu-1}\left(\frac{R^{1-\gamma}+L_R}{2A}
\right)^{\nu/\gamma}\longrightarrow0\quad(R\downarrow0). \tag{SF-5}
\]
故对**任意固定**上述参数与 \(R_0\)，可先取充分小的
\(R>0\) 令 \(\kappa_R<1\)，再取
\(\bar t\ge(R+L_RR^\gamma)/2\)。全域 gauge 在此可评价，
\(U=\mathbb R^3\) 的 R02 留域预算右边是 \(+\infty\)；
亦可直接看到 \(|r|\le R<1\) 在 \(T\) 下不变。因此
可在同一 collar 应用
[R01/R02 的单值图块证明](../rleb_ppa.md#r02-proof)。
这给严格局部 RLEB 证书；数值 \(\kappa_R\) 是保守证书率，
不是实际的超线性法向递推 \(r\mapsto |r|^\nu\)。

<a id="sf-tail"></a>
## 共同超几何尾与逐轨道 Q-\(\nu\)

对每个初值 \(0<|r_0|<1\)，全部 \(k\ge0\) 有
\(|r_k|=|r_0|^{\nu^k}\)，并且从 \(k=1\) 起
\(r_k>0\) 且 \(r_k\downarrow0\)。对于任意固定 \(R_0<1\)，
全部 \(|r_0|\le R_0\) 和全部 \(k\ge0\) 的切向尾满足
\[
\sum_{j\ge k}\|(z_{j+1},p_{j+1})-(z_j,p_j)\|
\le\frac{\sqrt{A^2+B^2}\,R_0^{\gamma\nu^k}}
{1-R_0^{\gamma(\nu-1)}}.                       \tag{SF-6}
\]
因此完整轨道有限长，\(\Pi(x)=(z_\infty,p_\infty,0)\)，
共同点尾 \(e_k=\|T^kx-\Pi(x)\|\) 不超过 (SF-6)
加 \(R_0^{\nu^k}\)。这是 \(M e^{-c\nu^k}\) 的同球界，
\(c=\gamma\log(1/R_0)>0\)；从 (SF-3) 可单独接
[SS-TRANSFER](solution_selection_rates.md#ss-transfer) 的
两点上界，指数
\(\alpha=\log\nu/\log(\nu/\gamma)\)。

更强的**逐轨道**断言如下。若 \(p_0\le0\)，则 \(p_k=p_0\)；
若 \(p_0>0\)，\(p_k\) 单调增加而 \(r_k\downarrow0\)，
故最终总处于 \(p_k\ge r_k\) 的饱和段。于是令
\(c_*=A\) 或 \(\sqrt{A^2+B^2}\)，分别对应这两种情形，
有 \(e_k\sim c_* r_k^\gamma\)，并且
\[
\lim_{k\to\infty}\frac{e_{k+1}}{e_k^\nu}=c_*^{1-\nu}.
                                                               \tag{SF-7}
\]
共同尾不提供共同的 Q-\(\nu\) 渐近起点；\(r_0=0\)
为驻点，不对 \(0/0\) 定义比值。\(|r_0|\ge1\) 不在此
收敛论断的域内。

<a id="sf-sharp"></a>
## 同一完整图的固定初值配对

固定 \(0<r_0<1\)，比较
\(x_0=(0,0,r_0),x_\varepsilon=(0,\varepsilon,r_0)\)
（若同时要求上节的严格证书，先固定 \(r_0\le R\) 且
\(\kappa_R<1\)）。令 \(t=\log(1/\varepsilon)\)、
\(a=-\log r_0>0\)，取第一次 \(p_N\ge r_N\) 的
\(N\)。对 \(k<N\)，
\(p_{k+1}=p_k+Bp_k^\gamma\) 且
\[
\log p_k=-t\gamma^k+O(1)\quad(0\le k\le N),       \tag{SF-8}
\]
其中误差由 \(\log(B+p_k^{1-\gamma})\) 的有界几何和控制，
不依赖 \(\varepsilon\)。固定 \(k\) 后令 \(\varepsilon\to0\)
知 \(N\to\infty\)。比较 \(p_N\ge e^{-a\nu^N}\) 和
\(p_{N-1}<e^{-a\nu^{N-1}}\)，分别使用 (SF-8) 的
上、下误差，得到
\[
t\gamma^N\le a\nu^N+O(1),\qquad
t\gamma^{N-1}>a\nu^{N-1}-O(1).                  \tag{SF-9}
\]
因此 \(t(\gamma/\nu)^N\) 有正的上下界，
\[
N=\frac{\log t}{\log(\nu/\gamma)}+O(1),\quad
t\gamma^N=\Theta(\nu^N)=\Theta(t^\alpha).        \tag{SF-10}
\]
之后 \(p_k\) 非降而 \(r_k\) 严格下降，故一直饱和；
但**不能**把 \(p_N\) 无证地改写为 \(O(r_N^\gamma)\)。
分别由 (SF-8) 与超几何级数得到
\[
p_N=e^{-\Theta(t^\alpha)},\qquad
B r_N^\gamma\le B\sum_{j\ge N}r_j^\gamma
\le\frac{B r_N^\gamma}{1-r_0^{\gamma(\nu-1)}}
=e^{-\Theta(t^\alpha)}.                          \tag{SF-11}
\]
两条比较轨道第一坐标极限相同，第二坐标之差为
\(p_N+B\sum_{j\ge N}r_j^\gamma\)。所以存在
仅依赖固定参数及 \(r_0\) 的 \(0<c<C\)，使充分小的
\(\varepsilon>0\) 满足
\[
e^{-C[\log(1/\varepsilon)]^\alpha}
\le\|\Pi(x_\varepsilon)-\Pi(x_0)\|
\le e^{-c[\log(1/\varepsilon)]^\alpha}.           \tag{SF-12}
\]
这是指数层面的匹配阶，排除该配对处正阶两点 Hölder
以及统一采用更大伸缩指数的上界；不声称指数前常数的最优性。

**来源和边界。** SS1 修订包 `research_note.md` 557–582 行
给出推广线索；(SF-1–12) 在规范层重建全纤维、图块尺度、
最小残差、固定兼容门、共同尾、逐轨道比值和两项分开的
配对下界。C115/C116 是特例，C139 的几何法向族是另一
递推，不能把前者的 \(\nu\) 当作后者的 \(q\)。
外部先行性与具体原生模型的额外表示不由本页判断。
