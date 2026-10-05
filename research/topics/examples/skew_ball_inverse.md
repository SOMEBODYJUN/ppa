# 斜旋转加圆盘法锥：完整逆像的锐半阶

<a id="sb-object"></a>
## 对象、目标和完整纤维

在 \(\mathbb R^2\) 取 \(K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\)、闭单位盘 \(B\)，定义完整关系 \(F=K+N_B\)。在 \(\|x\|<1\) 时 \(F(x)=\{Kx\}\)，在 \(\|x\|=1\) 时 \(F(x)=\{Kx+\alpha x:\alpha\ge0\}\)，盘外为空。固定边界参考 \(\bar x\in\partial B\) 的目标为 \(\bar y=K\bar x\)，**不是**零目标。来源线索为 9/01 ZIP `work/c_gx053_065.md` §2 的 GX-058；原卡的边界逆像、图几何和近端属性在下文分别重算。BWY arXiv v1 的 Proposition 3.4 / Example 3.5（作者站稿为 Proposition 3.6 / Example 3.7）归属已按[一手文献记录](../../LITERATURE.md#lit-bwy-2012)核验；优先权仍未审。

这不是线性关系：线性图的输入投影必为线性子空间，而此完整图的输入投影是单位盘 \(B\)，不在数乘下封闭。

<a id="sb-inverse"></a>
## C98-v1：完整逆映射与全域两变量模

全部 \(y\in\mathbb R^2\) 有**唯一**原像 \(G(y)=F^{-1}(y)\)：
\[
G(y)=\begin{cases}
-Ky,&\|y\|\le1,\\
\dfrac{(tI-K)y}{\|y\|^2},\quad t=\sqrt{\|y\|^2-1},&\|y\|>1.
\end{cases}                                               \tag{SB1}
\]
证明：盘内满足 \(y=Kx\)；边界满足 \(y=(K+\alpha I)x\)，\(\|y\|^2=1+\alpha^2\) 且 \((K+\alpha I)^{-1}=(\alpha I-K)/(1+\alpha^2)\)。两式在单位目标圆上连续拼接，没有丢掉法向射线的其它点。

任意**两个完整图点** \((x,u),(z,v)\) 满足
\[
\|x-z\|^2\le2\|u-v\|.                            \tag{SB2}
\]
若两点在盘内，\(\|u-v\|=\|x-z\|\)、\(\|x-z\|\le2\)。若 \(\|x\|=1\)、\(\|z\|\le1\)，写 \(z=cx+sKx\)，\(c^2+s^2\le1\)，\(u=Kx+\alpha x\)。当 z 在盘内时
\(u-v=(s+\alpha)x+(1-c)Kx\)，故 \(\|u-v\|\ge1-c\ge\|x-z\|^2/2\)。若两点均在边界，令 \(v=Kz+\beta z\)，\(\beta\ge0\)。其差在 \(x,Kx\) 基下为
\[
u-v=(s+\alpha-\beta c)x+(1-c-\beta s)Kx.
\]
当 \(s\le0\)，它在单位向量 \(Kx\) 上投影至少 \(1-c\)；当 \(s\ge0\)，在单位向量 \(sx-cKx\) 上投影为 \(1-c+\alpha s\)。两者均给 (SB2)，因为边界对有 \(\|x-z\|^2=2(1-c)\)。交换两点涵盖只有 z 在边界的情形。

由于 \(\|x-z\|\le2\)，对每个 \(0<q\le1/2\)，(SB2) 给全局**逆映射**模和原算子**两变量** MR：
\[
\|G(u)-G(v)\|\le 2^{1-q}\|u-v\|^q,\qquad
\|x-G(y)\|\le 2^{1-q}d(y,F(x))^q
\quad(x\in B,\ y\in\mathbb R^2).                 \tag{SB3}
\]
第二式对 \(x\) 的完整闭射线 \(F(x)\) 取最近的 \(v\)，用 \(G(v)=x\) 代入第一式。下面 C99 的 \(\theta=\pi\) 同时使两式取等，故系数 \(2^{1-q}\) 全域锐；所有 \(q>1/2\) 在边界附近失败。盘外 \(F(x)=\varnothing\) 的残差为 \(+\infty\)，这里把 MR 的输入域明确限定为 \(x\in B\)，不借 \(0\cdot\infty\) 约定。

<a id="sb-boundary"></a>
## C99-v1：边界固定目标和共同邻域的锐性

固定任意单位 \(\bar x\)，令 \(\bar y=K\bar x\)。对每个 \(x\in B\)，完整零/目标纤维为 \(F^{-1}(\bar y)=\{\bar x\}\)，(SB2) 给
\[
\|x-\bar x\|^2\le2d(\bar y,F(x)).             \tag{SB4}
\]
此式的固定目标全域系数 \(\sqrt2\) 锐，而且也是 \((\bar x,\bar y)\) 邻域的两变量半阶 MR 和逆映射半阶 Hölder **局部系数下确界**。为同时核这些量词，取 \(0<\theta\le\pi\) 和
\[
z_\theta=\cos\theta\,\bar x+\sin\theta\,K\bar x,
\quad v_\theta=Kz_\theta+\sin\theta\,z_\theta\in F(z_\theta).
\]
沿这个法向射线，\(\sin\theta\) 正好是 \(\bar y\) 到 \(F(z_\theta)\) 的最近点系数，因为
\(\langle\bar y-Kz_\theta,z_\theta\rangle=\sin\theta\)。直接算得
\[
\|z_\theta-\bar x\|^2=2(1-\cos\theta),\qquad
\|v_\theta-\bar y\|=d(\bar y,F(z_\theta))=1-\cos\theta.
\tag{SB5}
\]
\(\theta\downarrow0\) 使半阶比恒为 \(\sqrt2\)，任意 \(q>1/2\) 的比发散。\(\theta=\pi\) 使两种距离均为 2，证 (SB3) 的每个全局锐系数。对 \(0<q<1/2\)，缩小共同邻域中的残差，(SB3) 的半阶版本给局部 \(q\) 阶系数下确界 0（不说在非平凡邻域由系数 0 取到）。

在原点 \((0,0)\) 的足够小输入输出窗口内，\(F(x)=Kx\)，所以通常线性 MR/MSR 的局部系数是 1；边界的半阶断言不能当作零点的同一参考命题。(SB3) 是 \(F^{-1}\) 与**原算子** MR 的模，不是反射 resolvent 的全对 RL。

<a id="sb-geometry"></a>
## C124-v1：完整图的单调、rectangular 与非 paramonotone

任意两图点写成 \((x,Kx+\alpha x),(z,Kz+\beta z)\)，其中 \(x,z\in B\)、\(\alpha,\beta\ge0\)、\(\alpha(1-\|x\|)=\beta(1-\|z\|)=0\)。反对称性给
\[
\langle x-z,(Kx+\alpha x)-(Kz+\beta z)\rangle
=\alpha(\|x\|^2-\langle x,z\rangle)
 +\beta(\|z\|^2-\langle x,z\rangle)\ge0.\tag{SB6}
\]
边界上的两项由 Cauchy–Schwarz 非负；内点的相应系数为零。这证明完整图单调。取两个不同内点，差值为 \(K(x-z)\)，配对为零而 \(\|K(x-z)\|>0\)，所以正强单调与正 cocoercivity 系数都不存在（相应最优非负系数为 0）。

为核 rectangularity，固定 \(\xi\in\operatorname{dom}F=B\)、\(\eta\in\operatorname{ran}F\)。对任意图点 \((z,Kz+\alpha z)\)，
\[
\langle\xi-z,\eta-(Kz+\alpha z)\rangle
=\langle\xi-z,\eta-Kz\rangle+\alpha(1-\langle\xi,z\rangle)
\quad(\alpha>0\Rightarrow\|z\|=1).\tag{SB7}
\]
第一项在紧盘上有统一下界，第二项非负。因此在标准的 \(\xi\in\operatorname{dom}F,\eta\in\operatorname{ran}F\) 量词下，rectangular infimum 有限。这里**没有**把 \(\xi\) 扩到盘外。取任意非零内点 \(x\)，\((x,Kx),(0,0)\) 配对为零，但交叉点 \((x,0)\notin\operatorname{gph}F\)，故 paramonotonicity 失败。

<a id="sb-prox"></a>
## C125-v1：全部近端纤维与锐全图反射模

对每个 \(\lambda>0\) 和每个输入 \(p\in\mathbb R^2\)，完整 \(J_{\lambda F}(p)\) 恰有一个点：
\[
J_{\lambda F}(p)=
\begin{cases}
\dfrac{I-\lambda K}{1+\lambda^2}p,&\|p\|\le\sqrt{1+\lambda^2},\\[2mm]
\dfrac{hI-\lambda K}{\|p\|^2}p,
\quad h=\sqrt{\|p\|^2-\lambda^2},&\|p\|>\sqrt{1+\lambda^2}.
\end{cases}\tag{SB8}
\]
内部方程是 \(p=(I+\lambda K)x\)；其解的范数是 \(\|p\|/\sqrt{1+\lambda^2}\)。外部令 \(\|x\|=1\)、\(p=((1+\lambda\alpha)I+\lambda K)x\)，便有 \(h=1+\lambda\alpha>1\) 和 (SB8) 的第二式。阈值处两式一致，且全部法向 \(\alpha\ge0\) 都已反演，故没有漏掉其它输出。单调图又因 \(I+\lambda F\) 对每个输入满射而极大：若 \((z,w)\) 与所有图点单调相关，取 \(x=J_{\lambda F}(z+\lambda w)\)、\(v=(z+\lambda w-x)/\lambda\)，则 \(\langle z-x,w-v\rangle=-\|z-x\|^2/\lambda\ge0\)，迫使 \((z,w)=(x,v)\) 已在图上。

写 \(R_\lambda=2J_{\lambda F}-I\)。若 \(p=x+\lambda u,q=z+\lambda v\)，(SB6) 给
\[
\|R_\lambda p-R_\lambda q\|^2
=\|p-q\|^2-4\lambda\langle x-z,u-v\rangle\le\|p-q\|^2.\tag{SB9}
\]
两个不同内点有等号，故**全部输入对距**的全图 \(\mathrm{RL}(\lambda,1,1)\) 常数 1 锐，虽完整 \(J\) 全域单值，反射并非严格收缩。由于 \(\|Jp\|\le1\)，取 \(q=0\) 和 \(\|p\|\to\infty\) 得 \(\|R_\lambda p\|\ge\|p\|-2\)，任何全域 \(0<\gamma<1\) 的有限常数都失败。有界成对输入窗可继承较低指数，属于另一个尺度量词。

来源与范围：GX-058 第 476–504、520–537 行给这组图几何/近端线索；(SB6)–(SB9) 为本页对完整图和全部输入的独立推导，不使用旧稿的 `PASS` 标签或外部 BWY 归属。C98/C99 的原算子逆像 MR 属于另一残差坐标，不能从本节反射模推得。

<a id="sb-zero"></a>
## 原算子零目标的全域锐线性界与局部四种模

本节从完整法向纤维补核来源 GX-058 第 534、539–546 行。
原关系的零集 \(S=\{0\}\)，因为 (SB1) 给 \(G(0)=0\)。
对每个 \(x\in B\)，原算子的完整真残差精确满足
\[
r_F(x)=d(0,F(x))=\|x\|=d(x,S).\tag{SB10}
\]
内点只有 \(Kx\)，其范数等于 \(\|x\|\)；边界全部图值为
\(Kx+\alpha x,\alpha\ge0\)，反对称与正交性给
\(\|Kx+\alpha x\|^2=1+\alpha^2\)，最小值在 \(\alpha=0\)
取到。盘外残差无穷，仅对正系数使用此约定。因此固定零目标
MSR/SMSR 的全域锐线性系数是 1，并由任意非零内点取等；
它与 (SB4) 的非零边界目标属于不同参考命题。

取任意 \(0<\varepsilon<1\)，限制 \(\|x\|<\varepsilon\)、
\(\|y\|<\varepsilon\)，完整纤维为 \(F(x)=\{Kx\}\) 和
\(F^{-1}(y)=\{-Ky\}\)，且
\[
\|x-G(y)\|=\|Kx-y\|=d(y,F(x)).\tag{SB11}
\]
所以原点的线性 MR、SMR、MSR、SMSR 四种局部系数都恰为 1；
任意小非零输入或目标给锐性。这里 MR/SMR 含全部附近目标的
量词，而 (SB10) 的全域零目标界不把它们扩到边界。

对任意固定 \(\lambda>0\)，(SB6) 的非负内积还说明打印的
LT 非负违反条件 \(\lambda\langle a,b\rangle
\ge-\tau\|a+\lambda b\|^2\) 的最小系数是 0。
两个不同内点的内积为 0、输入差非零，亦使允许符号的最小
系数等于 0；它不是正强单调或正 cocoercivity 的证书。

本次补项 (SB10)–(SB11) 与 LT 系数为 `derived-checked` 的
完整纤维直接推导；Claim 身份另登记，BWY 归属和源审计评级不承担证明。
