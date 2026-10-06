# 指定近端分支：近似零点锚与局部幂次门

此模块从历史 `RL_foundations.md` §4–§5 重新证明一条与 [R02](../rleb_ppa.md#r02) 不同的接口。这里的空间可以是实 Hilbert 空间，零集不预设闭或有最近点；比较只对每个输入与**近似最近零点**进行，不要求图块全对 RL。结论只涉及指定分支，不能换成完整 resolvent 的任意选择。历史原稿是来源，不是本模块的证明。

<a id="nb-object"></a>
## NB-OBJECT · 对象与整个输入家族的量词

令 \(H\) 为实 Hilbert 空间，\(F:H\rightrightarrows H\)，\(S=F^{-1}(0)\ne\varnothing\)，\(\lambda>0\)，\(\bar x\in S\)，\(U=B(\bar x,R)\)。固定 \(L\ge0,0<\gamma\le1,\delta>0\)，并记 \(A_\delta=\{x\in U:d(x,S)\le\delta\}\)。设 \(\psi:[0,\eta)\to[0,\infty)\) 有限、非减、\(\psi(0)=0\)、在零点连续，且

\[
 h(\delta):=\frac{\delta+L\delta^\gamma}{2\lambda}<\eta.
\]

要求如下三项**同时**成立：

1. **B：指定输入覆盖。** 对每个 \(x\in U\)，固定同一映射 \(T:U\to H\)，使 \(v_x=(x-Tx)/\lambda\in F(Tx)\)。这不排除 \(F\) 的其他图点。
2. **A：近似最近锚。** 对每个 \(x\in A_\delta\)，存在可随 \(x\) 改变的序列 \(p_n\in S\)，\(\|x-p_n\|\to d(x,S)\)，且对**每个** \(n\)，
   \(\|2Tx-x-p_n\|\le L\|x-p_n\|^\gamma\)。\(d(x,S)=0\) 的输入也在量词内。
3. **E：实际输出的真残差误差界。** 对每个 \(x\in A_\delta\)，\(r_F(Tx)<\eta\) 且 \(d(Tx,S)\le\psi(r_F(Tx))\)，其中 \(r_F(y)=\inf_{v\in F(y)}\|v\|\)。

<a id="nb-local"></a>
## C53-v1 · 指定分支的有限长度与局部闭零集

置 \(b(t)=(t+Lt^\gamma)/2\)、\(\Phi(t)=\psi(b(t)/\lambda)\)。在 NB-OBJECT 下，对每个 \(x\in A_\delta\)，令 \(r=d(x,S)\)，有

\[
 \|x-Tx\|\le b(r),\qquad r_F(Tx)\le b(r)/\lambda,
 \qquad d(Tx,S)\le\Phi(r). \tag{NB-1}
\]

若 \(c=\limsup_{t\downarrow0}\Phi(t)/t<1\)，取 \(c<\theta<1\) 及 \(0<\delta_\theta\le\delta\)，使所有 \(0<t\le\delta_\theta\) 满足 \(\Phi(t)\le\theta t\)。给定 \(x^0\in U\)、\(r_0=d(x^0,S)\le\delta_\theta\)，再要求严格留域预算

\[
 \|x^0-\bar x\|+B(r_0,\theta)<R,\quad
 B(r,\theta)=\frac12\left(\frac r{1-\theta}
 +\frac{Lr^\gamma}{1-\theta^\gamma}\right). \tag{NB-2}
\]

则 \(x^{k+1}=T(x^k)\) 全程合法，留在 \(U\cap A_{\delta_\theta}\)，并且

\[
 r_k\le\theta^kr_0,\quad
 \sum_{k\ge0}\|x^{k+1}-x^k\|\le B(r_0,\theta),\quad
 \|x^k-x^\infty\|\le B(r_k,\theta),\quad x^\infty\in S.
\]

**证明。** 对 A 中的 \(p_n\) 使用

\(2(x-Tx)=(x-p_n)-(2Tx-x-p_n)\)，再令 \(n\to\infty\)，得第一界。B 给 \(v_x\in F(Tx)\)，从而得真残差的上界；E 与单调 \(\psi\) 给最后一界。若 \(r=0\)，第一界直接给 \(Tx=x\)，再由 B 得 \(x\in S\)。特别地，对每个 \(x\in U\cap\overline S\)，A 仍适用，所以

\[
 U\cap\overline S=U\cap S. \tag{NB-3}
\]

现在逐步应用 (NB-1)，得到 \(r_{k+1}\le\theta r_k\) 以及 \(\|x^{k+1}-x^k\|\le b(\theta^kr_0)\)。几何级数和 (NB-2) 逐步保证下一个点严格留在 \(U\)；距离界保证其仍在 \(A_{\delta_\theta}\)。有限总长使轨道在完备的 \(H\) 内收敛，严格预算使极限仍在 \(U\)。距离趋零，(NB-3) 给极限属于 \(S\)。从第 \(k\) 步重新求同一几何级数给尾界。□

闭性结论只在 \(U\) 内；它来自 A 在**零距离输入**也成立和 B，不应将零距离输入从 A 删掉。若需完整 \(J_{\lambda F}\) 的所有选择满足相同结论，还须对其全部相关输入纤维另证排他或逐选择统一界。

<a id="nb-power"></a>
## C54-v1 · 幂次证书的三个端点

在 C53 的共同条件中令 \(\psi(t)=\rho t^q\)，\(\rho,q>0\)，并保持实际输出的窗口门。下表只表示能由 (NB-1) **充分**获得的局部收缩；每行仍需 B、A、E 和 (NB-2)。

| 参数 | 一步上界 | 可缩半径的充分条件 | 临界系数 |
| --- | --- | --- | --- |
| \(0<\gamma<1,L>0\) | \(r_+\le \rho(2\lambda)^{-q}(r+Lr^\gamma)^q\)，上阶 \(p=\gamma q\) | \(p>1\)，或 \(p=1\) 且 \(\kappa=\rho(L/(2\lambda))^q<1\) | \(p=1\) 时比值 limsup \(\le\kappa\) |
| \(\gamma=1,L\ge0\) | \(r_+\le A r^q, A=\rho((1+L)/(2\lambda))^q\) | \(q>1\)，或 \(q=1,A<1\) | \(q=1\) 时 limsup \(\le A\) |
| \(L=0,0<\gamma\le1\) | \(r_+\le A_0r^q, A_0=\rho/(2\lambda)^q\) | \(q>1\)，或 \(q=1,A_0<1\) | 与打印的 \(\gamma\) 无关 |

**证明及界限。** 第一行把 \(r+Lr^\gamma=r^\gamma(r^{1-\gamma}+L)\) 代入 (NB-1)；其余两行直接代入。正幂上界除以 \(r\) 后趋零，或在临界情形趋向表中的常数，于是可先缩 \(\delta_\theta\)，再调用 C53。若指数小于 1，单靠这些上界不能推出收缩，也不能推出发散。所述 \(O(r_k^p)\) 只为上阶；要称双边精确阶或正 Q 因子，须分别补同一非终止轨道的正有限下界或归一化正极限。\(L=0\) 时切忌沿用 \(\gamma q\) 标签。□

<a id="nb-oscillation"></a>
## C55-v1 · 锚定条件严格弱于同参数全对 RL 的例子

取 \(H=\mathbb R,\lambda=1,S=\{0\}\)，并定义 \(T(0)=0\)，\(T(x)=a(x)x\)（\(x\ne0\)），其中 \(a(x)=3/10+(1/10)\sin(x^{-2})\)。令**完整关系**

\[
 F(y)=\{x-y:T(x)=y\}.
\]

由于 \(1/5\le a(x)\le2/5\)，\(T\) 连续、proper、满射，故 \(F\) 有闭完整图且 \(F^{-1}(0)=\{0\}\)。每个 \(y\ne0\) 和 \(x\in T^{-1}(y)\) 同号，\( |x|\ge(5/2)|y|\)，故 \(r_F(y)\ge(3/2)|y|\)。因此 \(\psi(t)=2t/3\) 是全图真 EB；指定图点 \(v_x=x-Tx\) 给 B。对唯一零点锚 \(p=0\)，

\[
 |2Tx-x|=|2a(x)-1||x|\le(3/5)|x|.
\]

故 A 在任意小球上以 \(\gamma=1,L=3/5\) 成立，E 也成立；\(\Phi(r)= (8/15)r\)，C53 适用。实际还有 \( |Tx|\le(2/5)|x|\)。但是 Cayley 反射 \(C(x)=2T(x)-x=[-2/5+(1/5)\sin(x^{-2})]x\) 在任何零邻域内都**非 Lipschitz**：其在 \(x\ne0\) 的导数含 \( -(2/5)x^{-2}\cos(x^{-2})\)，沿 \(x_n=(2\pi n)^{-1/2}\) 无界。若同图上 \(\gamma=1\) 全对 RL 在零邻域成立，\(C\) 必为 Lipschitz，矛盾。

这个反例只分离上述指定 \(L,\gamma=1\) 锚条件与全对线性 RL；不排除该图另有较弱指数的全对模，也不把 \(T\) 的单值性推广为任意其他原关系的完整 resolvent 单值性。

**来源与审查范围。** 旧 `history/sources/次单调论文研究/RL_foundations.md` §4.1–4.3、§5.1–5.4 是本页重写的来源输入；C53/C54 的推导和 C55 的新反例在本页独立计算。与 [R02/R03](../rleb_ppa.md) 的合取条件和 [孤立零点](isolated_zero_flatness.md) 的强阶结论各自保持原对象及量词。未做文献先行性核验，亦未核旧稿全部其他章节。
