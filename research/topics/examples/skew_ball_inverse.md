# 斜旋转加圆盘法锥：完整逆像的锐半阶

<a id="sb-object"></a>
## 对象、目标和完整纤维

在 \(\mathbb R^2\) 取 \(K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\)、闭单位盘 \(B\)，定义完整关系 \(F=K+N_B\)。在 \(\|x\|<1\) 时 \(F(x)=\{Kx\}\)，在 \(\|x\|=1\) 时 \(F(x)=\{Kx+\alpha x:\alpha\ge0\}\)，盘外为空。固定边界参考 \(\bar x\in\partial B\) 的目标为 \(\bar y=K\bar x\)，**不是**零目标。来源线索为 9/01 ZIP `work/c_gx053_065.md` §2 的 GX-058；原卡所称“边界平方根转角”在下文重算为完整全局和局部锐常数。其它单调性标签及外部优先权未审。

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
