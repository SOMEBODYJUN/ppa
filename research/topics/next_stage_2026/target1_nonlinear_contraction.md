# 目标一：从固定线性收缩到函数复合收缩

## 1. 精确问题与现有接口

固定线性条件是

\[
d_{k+1}\le \kappa d_k,\qquad 0\le \kappa<1,
\]

其中 \(d_k=d(x^k,S)\)。现有 RLEB–PPA 证明还给出一个步长上界

\[
s_k:=\|x^{k+1}-x^k\|\le B(d_k),
\qquad B(t)=\frac{t+\omega(t)}2,
\]

并通过残差模得到

\[
d_{k+1}\le \psi\!\left(\frac{B(d_k)}\lambda\right).
\]

因此自然的函数收缩是

\[
\varphi(t):=\psi\!\left(\frac{B(t)}\lambda\right),
\qquad d_{k+1}\le \varphi(d_k).
\]

但 \(\varphi^{\circ k}(t)\to0\) 只给距离到 \(S\) 的收敛，不能单独给点列收敛或有限长度。

**LMZ paper fact。** Li–Mordukhovich–Zhu 的抽象框架把这一层写成 asymptotically shrinking 的递推：\(\tau(0)=0\)，并要求
\[
\limsup_{t\downarrow0}\frac{\sum_{j\ge0}\tau^{\circ j}(t)}{t}<\infty.
\]
论文还给出 \(\tau\) 非减且 \(\limsup_{t\downarrow0}\tau(t)/t<1\) 的充分条件。其 Theorem 4.4 通过广义 metric subregularity、相对误差和 surrogate 误差构造这种 \(\tau\)；该标量递推仍须和 Theorem 4.3 的能量差/步长递推及 H0–H3 配合，不能把它误读成“函数迭代趋零自动给有限长度”。

<a id="t1-interface"></a>
## 2. 可直接证明的非线性长度定理

**命题 T1.1（函数收缩—长度接口）。** 设 \(X\) 完备，\(S\subset X\) 非空闭，\(U\subset X\) 开，且对每个认证输入 \(x\in U_R:=\{x\in U:d(x,S)\le R\}\)，有非空允许后继集 \(\varnothing\ne T(x)\subset X\)，并且所选后继仍满足 coverage。固定 \(R>0\)，令 \(B:[0,R]\to[0,\infty)\) 与 \(\varphi:[0,R]\to[0,R]\) 连续非减，并满足 \(B(0)=\varphi(0)=0\)。对每个合法输入 \(x\in U_R\) 和每个允许输出 \(y\in T(x)\)，假设

\[
d(y,S)\le \varphi(d(x,S)),\qquad \|y-x\|\le B(d(x,S)).
\tag{T1.1}
\]

若 \(\varphi^{\circ k}(r)\to0\)，则所有 \(d_0=r\) 的合法轨道满足 \(d_k\to0\)。若

\[
\mathcal L_\varphi(r):=\sum_{j=0}^{\infty}B(\varphi^{\circ j}(r))<\infty,
\tag{T1.2}
\]

则每条从 \(d_0=r\) 出发的轨道具有有限长度，且

\[
\sum_{k=0}^{\infty}s_k\le \mathcal L_\varphi(r),
\qquad
\|x^m-x^\infty\|\le
\sum_{j=m}^{\infty}B(\varphi^{\circ j}(r)).
\tag{T1.3}
\]

若 \(\mathcal L_\varphi(R)<\infty\)，则 \(r\le R\) 的所有初值有统一长度预算。若只在 \(U\) 内有这些条件，要求

\[
\mathcal L_\varphi(d_0)<\operatorname{dist}(x^0,X\setminus U)
\tag{T1.4}
\]

并先验证后继覆盖，则每个有限前缀仍在 \(U\)，从而条件可继续使用。

**证明。** 由 \(\varphi\) 非减性归纳得到 \(d_k\le\varphi^{\circ k}(d_0)\)。将步长估计求和得到 (T1.3)。严格预算下，任意有限前缀离 \(x^0\) 的距离小于 \(\operatorname{dist}(x^0,X\setminus U)\)，所以每一步仍在 \(U\)；\(d_k\le R\) 保证下一次 coverage。若级数有限，点列 Cauchy；完备性和 \(d_k\to0\) 再给极限属于闭集 \(S\)。

该命题不要求固定 \(\kappa<1\)，也不要求 \(\varphi\) 是幂函数。它把“距离衰减”和“物理长度”明确分开。若量词只有“每个输入存在一个输出”，则它只控制一条选定策略，不能推出对所有选择的结论。

## 3. 迭代趋零的强度与可和性

仅有 \(\varphi^{\circ k}(r)\to0\) 不足以推出 (T1.2)。一个精确的抽象边界是

\[
\varphi(t)=t-t^p\quad (0<t\le R),\qquad p>1,
\tag{T1.5}
\]

其中 \(R\) 取小到使 \(\varphi\) 非减。其迭代满足 \(d_k\asymp k^{-1/(p-1)}\)。若只有 \(B(t)=t\) 的粗步长上界，则

\[
\sum_k B(d_k)\asymp\sum_k k^{-1/(p-1)},
\]

在 \(p\ge2\) 时发散；\(p=2\) 是谐和临界线。距离级数发散只说明这个抽象长度证书不足，不能反推实际 PPA 轨道发散。

<a id="t1-dini"></a>
在先行有限前缀后进入的零邻域内，令 \(\Delta(t)=t-\varphi(t)>0\)，并假设 \(B(t)/\Delta(t)\) 在 \((0,r_0]\) 非增，则有 Dini 型充分门

\[
\int_0^r\frac{B(t)}{\Delta(t)}\,dt<\infty
\quad\Longrightarrow\quad
\sum_{k\ge0}B(\varphi^{\circ k}(r))<\infty.
\tag{T1.6}
\]

令 \(t_0=r\)、\(t_{j+1}=\varphi(t_j)\)。进入 \(r_0\) 后，等号标量轨道满足
\[
\int_{t_{j+1}}^{t_j}\frac{B(u)}{\Delta(u)}\,du\ge
\frac{B(t_j)}{\Delta(t_j)}(t_j-t_{j+1})=B(t_j).
\]
求和得到 \(\sum_{j\ge N}B(t_j)\le\int_0^{t_N}B/\Delta\)，前缀有限；实际不等式轨道由 \(d_j\le t_j\) 和 \(B\) 非减性比较到等号轨道。对 (T1.5) 和 \(B(t)=t\)，(T1.6) 正好给出 \(p<2\)。

LMZ 的 asymptotically shrinking 条件比“每个固定初值的 \(\sum_j\varphi^{\circ j}(r)\) 有限”更强：它要求归一化尾和在 \(r\downarrow0\) 时统一有界。这个区别是局部统一收敛率与单条轨道有限长度之间的边界。

## 4. 严格超出固定 \(\kappa\) 的真实 PPA 例

取 \(X=\mathbb R\)，

\[
F(y)=y|y|,\qquad S=\{0\},\qquad \lambda=1.
\]

这是单调关系，\(r_F(y)=|y|^2\)，所以传统线性 metric subregularity \(d(y,S)\le K r_F(y)\) 在 \(0\) 附近失败。全局近端映射为

\[
T(x)=\operatorname{sgn}(x)\frac{\sqrt{1+4|x|}-1}{2},
\qquad T(0)=0.
\]

令 \(d_k=|x^k|\)。在任一非零轨道上符号保持不变，且

\[
d_{k+1}=\frac{\sqrt{1+4d_k}-1}{2}<d_k,
\qquad \frac{d_{k+1}}{d_k}\longrightarrow1.
\]

故不存在任何固定 \(\kappa<1\) 使 \(d_{k+1}\le\kappa d_k\) 对所有足够小的 \(d_k\) 成立。然而

\[
s_k=d_k-d_{k+1}=d_{k+1}^2,
\qquad
\sum_{k=0}^{N-1}s_k=d_0-d_N\le d_0.
\]

因此轨道有限长并收敛。这是一个完整的、单调的标量例子，证明“固定线性收缩”和“有限长度”不是同一层条件；它也证明非线性函数收缩可以覆盖传统 metric subregularity 不能覆盖的模型。另有 \(d_k\sim k^{-1}\) 和 \(\sum_k d_k=\infty\)，所以距离级数与物理步长级数再次分离。

## 5. 距离收敛而点列不收敛的精确机制

在 \(X=\mathbb R^2\)、\(S=\{0\}\times\mathbb R\) 上，局部允许转移可取

\[
T(r,z)=(r-r^2,z+r),\qquad0<r\le R<1/2,
\]

并令 \(T(0,z)=(0,z)\)。则 \(d(T(r,z),S)=r-r^2\)，所以距离按 \(\varphi(t)=t-t^2\) 趋零；但

\[
\|T(r,z)-(r,z)\|=\sqrt{r^4+r^2}\sim r,
\]

而 \(r_k\asymp1/k\)，故切向位移级数发散，\(z_k\to+\infty\)。把每个允许边写成 \(x=y+w\)（\(\lambda=1\)）即可得到一个局部 PPA 图关系；它是非单调的，但完全说明了 (T1.1) 中不能删去长度级数条件。该例是 obstruction，不是对所有单调 PPA 的反例。

## 6. 与既有 C09/C10 的关系

既有 C09 使用 \(\varphi(t)=\kappa t\) 和 \(B(t)=(t+\omega(t))/2\)，并以 \(\int_0^R\omega(t)\,dt/t<\infty\) 保证几何采样级数；C10 的对数接缝给出精确族
\[
d_{k+1}=d_k/4,\qquad s_k\asymp[\log(e/d_0)+k\log4]^{-a},
\]
其中距离对所有 \(a>0\) 都趋零，但有限长度和点列收敛当且仅当 \(a>1\)。这说明 C09 的 \(\omega\)-Dini 步长门与 \(\Delta(t)\) 的 \(p=2\) 收缩缺口门是不同的条件，不能互换。

**状态：** T1.1、T1.6 及标量 \(F(y)=y|y|\) 例可作为 `derived-checked` 候选进入接收；二维漂移例的图关系闭性、完整 resolvent coverage 和是否使用局部图块仍需独立接收，暂不升级为全局定理。
