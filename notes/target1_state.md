# 目标一阶段笔记：非线性距离收缩的状态与边界

日期：2026-11-17  
状态：阶段性研究笔记；不新增或升级 CLAIMS.md 中的 Claim。

## 1. 精确对象与目标

先固定度量空间 \((X,d_X)\)、非空目标集 \(S\subset X\)、工作域 \(U\subset X\) 和允许转移关系 \(T(x)\subset X\)。写
\[
d_k:=d_X(x_k,S),\qquad s_k:=d_X(x_{k+1},x_k).
\]
目标一的标量前件是
\[
d_X(y,S)\le \phi\bigl(d_X(x,S)\bigr).\tag{T1}
\]
为了把它用于轨道，必须分开声明：

* **量词**：全部输出是 \(\forall x\in D\;\forall y\in T(x)\)，选定一条轨道只对某个选择 \(y_k\in T(x_k)\) 成立；\(\forall x\,\exists y\) 不足以控制任意选择政策。
* **coverage**：每个已认证输入的 \(T(x)\) 非空，且后继仍在可用域；完整 PPA 还要另外证明完整 resolvent 在该域有非空纤维。
* **标量域**：\(d_0\le R\)、\(\phi:[0,R]\to[0,R]\)。若只在小窗有 (T1)，必须先证明轨道进入并留在该窗。
* **目标闭性**：由 \(d_k\to0\) 推出极限属于 \(S\) 需要 \(S\) 闭。
* **零吸收**：\(\phi(0)=0\) 只保证 \(d_k=0\)，不保证 \(x_{k+1}=x_k\)；若要零点驻定，须另有 \(T(x)=\{x\}\) 或逐转移的零步界。

在 PPA/GPPA 中，(T1) 通常是由真实残差、反射/锚几何和评价窗共同编译出来的标量上界。现有规范接口见 C02-v3、C185、JP3 和 NGK-5；这些文件的完整覆盖、真实残差和留域量词不能被抽象的 (T1) 省略。

## 2. 标量递推的严格结论

先研究
\[
d_{k+1}\le\phi(d_k),\qquad d_0\in[0,R].\tag{T2}
\]
若 \(\phi\) 非减，则归纳给出
\[
d_k\le\phi^k(d_0),\qquad
\phi^0(t)=t,\quad \phi^{k+1}(t)=\phi(\phi^k(t)).\tag{T3}
\]
若 \(\phi\) 非单调，应先换成非减上包络
\(\bar\phi(t):=\sup_{0\le u\le t}\phi(u)\)，并核对
\(\bar\phi([0,R])\subset[0,R]\)；直接迭代原 \(\phi\) 没有 (T3) 的比较义务。

### 2.1 距离趋零

方便而严格的充分条件是
\[
\phi(0)=0,\qquad \phi(t)<t\ (0<t\le R),\qquad
\phi\text{ 在 }[0,R]\text{ 连续}. \tag{T4}
\]
此时 \(t_{k+1}=\phi(t_k)\) 单调下降；若极限为 \(\ell>0\)，连续性给
\(\ell=\phi(\ell)<\ell\)，矛盾。因此 \(\phi^k(t)\to0\)，由 (T3) 得 \(d_k\to0\)。连续性可换成沿所有下降极限点的上半连续性：若 \(t_k\downarrow\ell>0\)，则
\(\ell=\lim\phi(t_k)\le\phi(\ell)<\ell\)。只写逐点严格不等式而不写连续性/上半连续性是不够的。

LMZ 使用了更强、但只需在零点附近的标量条件。对
\(\tau:\mathbb R_+\to\mathbb R_+\)，定义
\[
\tau(0)=0,\qquad
\limsup_{t\downarrow0}
\frac{\displaystyle\sum_{n=0}^{\infty}\tau^n(t)}{t}<\infty.
\tag{T5}
\]
他们称之为 asymptotically shrinking around zero。它包含归一化标量尾和，而不只是 \(\tau^k(t)\to0\)。若 \(\tau\) 非减且
\[
\limsup_{t\downarrow0}\frac{\tau(t)}{t}<1,\tag{T6}
\]
则小窗内可取 \(\tau(t)\le\varepsilon t\)，归纳得
\(\tau^n(t)\le\varepsilon^n t\)，故 (T5) 的比值不超过
\((1-\varepsilon)^{-1}\)。

### 2.2 距离级数与长度级数

\(\phi\) 迭代对每个固定初值趋零并不足以推出可和。例如
\(\phi(t)=t/(1+t)\) 在 \([0,\infty)\) 上连续、非减且严格下降，但
\[
\phi^k(t)=\frac{t}{1+kt}\longrightarrow0,\qquad
\sum_{k\ge0}\phi^k(t)=\infty\quad(t>0).
\]
因此“距离趋零”、“距离级数可和”和“物理步长级数可和”必须分开作为三个独立的 proof obligation。

定义最坏距离尾
\[
H_\phi(t):=\sum_{k=0}^{\infty}\phi^k(t)\in[0,\infty].\tag{T7}
\]
在 \(\phi\) 非减和 (T2) 下，
\[
H_\phi(d_0)<\infty
\Longrightarrow
\sum_{k=0}^{\infty}d_k\le H_\phi(d_0)<\infty. \tag{T8}
\]
对所有满足 (T2) 的标量序列，等号轨道说明 (T7) 是精确的最坏条件；对某条实际轨道，\(H_\phi=\infty\) 只表示标量证书不足，不表示轨道一定发散。

物理步长需要独立的步长模。若
\[
s_k\le b(d_k),\qquad b:[0,R]\to[0,\infty)\text{ 非减},\tag{T9}
\]
则
\[
H_{\phi,b}(t):=\sum_{k=0}^{\infty}b(\phi^k(t))<\infty
\Longrightarrow
\sum_{k=0}^{\infty}s_k\le H_{\phi,b}(d_0). \tag{T10}
\]
当 \(b(t)=Ct\) 时这退化为 (T7)。若存在联合势
\[
s_k+W(d_{k+1})\le W(d_k),\tag{T11}
\]
直接望远镜即可有限长度，不必拆成独立的 \(b(d_k)\)；这是 JP3 的后端，而 (T10) 是其独立步长尾特例。

若
\[
H_{\phi,b}(d_0)<d_X(x_0,X\setminus U),
\]
则有限前缀归纳给出
\[
d_X(x^m,x_0)\le\sum_{k<m}s_k
\le H_{\phi,b}(d_0)<d_X(x_0,X\setminus U).\tag{T12}
\]
这一步必须先于无穷轨道、Cauchy 和极限论证；不能用“轨道已留在 \(U\)”替代它。

### 2.3 基于 \(\Delta(t)=t-\phi(t)\) 的积分/Dini 型可和门

设在 \(0<t\le R_0\) 上
\[
\phi(t)=t-\Delta(t),\qquad
0<\Delta(t)\le\theta t\quad(0<\theta<1),\tag{T13}
\]
且 \(\Delta\) 非减、\(\phi\) 非减。令 \(t_{k+1}=\phi(t_k)\)，并在有限前缀后进入 \((0,R_0]\)。则
\[
\sum_{k\ge K}t_k
\le\frac1{1-\theta}\int_0^{t_K}\frac{u}{\Delta(u)}\,du.\tag{T14}
\]
事实上，在 \([t_{k+1},t_k]\) 上有
\(\Delta(u)\le\Delta(t_k)\) 且
\(t_{k+1}\ge(1-\theta)t_k\)，故
\[
\int_{t_{k+1}}^{t_k}\frac{u}{\Delta(u)}\,du
\ge\frac{t_{k+1}(t_k-t_{k+1})}{\Delta(t_k)}
=t_{k+1}\ge(1-\theta)t_k.
\]
求和即得 (T14)。这是充分条件；没有 \(\Delta\) 的单调/相邻尺度可比时，积分有限不自动控制离散尾。

对步长模 \(b(t)=t^\alpha\)（\(\alpha>0\)），同一证明及
\(t_k^\alpha\le(1-\theta)^{-\alpha}t_{k+1}^\alpha\) 给出
\[
\sum_{k\ge K}t_k^\alpha
\le C_{\alpha,\theta}\int_0^{t_K}\frac{u^\alpha}{\Delta(u)}\,du.\tag{T15}
\]
一般 \(b\) 需要 \(b(t)/b((1-\theta)t)\) 在零点附近有界。

若 \(\Delta(t)\asymp c t^p\)，则
\[
\int_0^\varepsilon\frac{u}{\Delta(u)}\,du
\asymp\int_0^\varepsilon u^{1-p}\,du
\begin{cases}
<\infty,&p<2,\\
=\infty\text{（对数）},&p=2,\\
=\infty,&p>2.
\end{cases}\tag{T16}
\]
相应地，\(\int_0^\varepsilon u^\alpha/\Delta(u)\,du<\infty\) 当且仅当
\(\alpha>p-1\)。等号标量轨道在常规正则变差条件下满足
\(t_k\asymp k^{-1/(p-1)}\)，所以这些阈值是等号族的 sharp 边界；一般上界只授予充分性。

这里的 Dini 积分针对收缩缺口 \(\Delta\)，而 C09 的 Dini 条件针对步长模 \(\omega\)，两者不能互换。在线性距离收缩 \(\phi(t)=\kappa t\) 下，
\(\Delta(t)=(1-\kappa)t\)，(T14) 自动给几何距离尾；C09 另需
\[
\int_0^R\frac{\omega(u)}u\,du<\infty
\]
来保证 \(b(u)=(u+\omega(u))/2\) 沿几何采样的步长级数可和。C09 的采样等价
\[
\int_0^R\frac{\omega(u)}u\,du<\infty
\Longleftrightarrow
\sum_{j\ge0}\omega(\kappa^j r)<\infty
\]
见 general_modulus_dynamics.md 的 GM10--GM14；它不要求把 \(\omega\) 写成 \(t-\phi(t)\)。

### 2.4 非线性率的可复用边界

以下均指等号标量轨道，且初值限制在使 \(\phi\) 单调并映回工作窗的区间。

| \(\phi(t)\)（小窗） | 距离尾典型阶 | \(\sum d_k\) | 对 \(b(t)=t^\alpha\) 的长度尾 |
|---|---:|---:|---:|
| \(\kappa t\), \(0<\kappa<1\) | \(\kappa^k\) | 有限 | 对所有 \(\alpha>0\) 有限 |
| \(t/(1+a t^r)\), \(a,r>0\) | \(k^{-1/r}\) | 当且仅当 \(r<1\) 有限 | 当且仅当 \(\alpha>r\) 有限 |
| \(t-c t^p\), \(p>1\) | \(k^{-1/(p-1)}\) | 当且仅当 \(p<2\) 有限 | 当且仅当 \(\alpha>p-1\) 有限 |
| \(q t^p\), \(0<q<1,p>1\) | 超几何（\(\log d_k\asymp p^k\)） | 有限 | 对所有 \(\alpha>0\) 有限 |

对第二行，令 \(t_{k+1}=t_k/(1+a t_k^r)\)。当 \(t_k\) 足够小时，
\[
t_{k+1}^{-r}-t_k^{-r}
=t_k^{-r}\bigl((1+a t_k^r)^r-1\bigr)\asymp ar,
\]
故 \(t_k\asymp k^{-1/r}\)。第三行可用
\(t_{k+1}^{-(p-1)}-t_k^{-(p-1)}\asymp c(p-1)\) 得到相同结论。临界指数给调和尾，不能把距离趋零升级成距离或步长可和。

LMZ 的 (T5) 比“每个固定初值的 \(H_\tau(t)<\infty\)”更强：例如 \(\tau(t)=t/(1+a t^r)\) 在 \(0<r<1\) 时每个小初值的距离级数有限，但
\(H_\tau(t)/t\asymp t^{-r}\to\infty\)，所以不满足 (T5)。这不是冲突，而是不同用途：LMZ 需要统一的线性归一化尾来闭合局部点列和速率；C185/JP3 可只要求给定初值的有限标量预算。

### 2.5 标量 PPA 例：\(F(y)=y^2\) 的 \(p=2\) 距离边界

在非负分支 \(y\ge0\) 上取 \(F(y)=y^2\)、\(\lambda=1\)，并从 \(x_0>0\) 开始。令 \(x_{k+1}=y_k\) 为近端方程
\[
x_k=x_{k+1}+x_{k+1}^2
\]
的唯一非负根：
\[
x_{k+1}=\frac{\sqrt{1+4x_k}-1}{2}.\tag{T17}
\]
（若需全局单调原图，可改取 \(F(y)=y|y|\)；正半轴轨道完全相同。）这里 \(S=\{0\}\)、\(d_k=x_k\)，且
\[
\Delta(d_k)=d_k-d_{k+1}=d_{k+1}^2\asymp d_k^2.
\]
又
\[
\frac1{x_{k+1}}-\frac1{x_k}
=\frac1{1+x_{k+1}}\longrightarrow1,
\]
故 \(x_k\sim k^{-1}\)。于是
\[
d_k\to0,\qquad \sum_k d_k=\infty
\]
（正好是 (T16) 的 \(p=2\) 对数边界），而
\[
s_k=x_k-x_{k+1}=x_{k+1}^2\asymp k^{-2},\qquad
\sum_k s_k=x_0<\infty.
\]
该例严格区分距离级数和物理步长级数：PPA 点列收敛且有限长，但距离不可和。用 \(\Delta\) 的积分判据时，应把实际步长模 \(b(d)=\Delta(d)\) 代入 \(\int b/\Delta\)，不能只检查 \(\int d/\Delta\)。

## 3. 四种收敛概念不能互换：显式反例

### 3.1 距离收敛但点列不收敛，且长度发散

取
\[
X=\mathbb R^2,\quad S=\mathbb R\times\{0\},\quad
T(a,b)=(-a,b/2).
\]
则
\[
d(T(a,b),S)=\tfrac12d((a,b),S)
\]
全域成立，即 \(\phi(t)=t/2\)。从 \(x_0=(1,1)\) 得
\[
x_k=((-1)^k,2^{-k}),\qquad d_k=2^{-k}\to0,
\]
但第一坐标交替，故 \(x_k\) 不收敛；且 \(s_k\ge2\)，总长度发散。即使 \(\sum d_k<\infty\)，也不能推出 \(\sum s_k<\infty\) 或点列收敛。这里的机制是 \(S\) 有切向自由度且 \(T|_S\) 不吸收。

### 3.2 步长可和、点列收敛，但距离不可和

取 \(X=\mathbb R\)、\(S=\{0\}\)、\(T(x)=x/(1+|x|)\)、\(x_0=1\)。则
\[
x_k=\frac1{k+1},\qquad
d_{k+1}=\frac{d_k}{1+d_k}=\phi(d_k),
\quad \phi(t)=\frac{t}{1+t}.
\]
所以 \(d_k\to0\) 但 \(\sum d_k=\infty\)；另一方面
\[
s_k=\frac1{(k+1)(k+2)},\qquad \sum s_k=1.
\]
有限长度不是距离级数有限的必要条件。

### 3.3 点列收敛但长度发散

仍取 \(X=\mathbb R,S=\{0\}\)，令
\[
T(x)=-\frac{x}{1+|x|},\qquad x_0=1.
\]
则 \(x_k=(-1)^k/(k+1)\to0\)，同样有
\(d_{k+1}=d_k/(1+d_k)\)，但
\[
s_k=\frac1{k+1}+\frac1{k+2}\asymp k^{-1},
\]
故 \(\sum s_k=\infty\)，而 \(\sum d_k=\infty\)。点列收敛本身也不等于有限长度。

### 3.4 零距离不等于零步

对 3.1 的 \(T(a,b)=(-a,b/2)\)，若从
\((1,0)\in S\) 出发，则所有 \(d_k=0\)，但点列在
\((1,0)\) 与 \((-1,0)\) 之间跳动。任何声称“距离递推自动给零输入驻定”的定理都缺少零吸收前件。

### 3.5 仅逐点严格 \(\phi(t)<t\) 仍可能停在正距离

在 \([0,2]\) 上定义
\[
\phi(0)=0,\quad \phi(t)=t/2\ (0<t\le1),\quad
\phi(t)=(t+1)/2\ (1<t\le2).
\]
它非减且每个 \(t>0\) 都满足 \(\phi(t)<t\)，但从 \(t_0=2\) 开始
\[
t_k=1+2^{-k}\longrightarrow1>0.
\]
缺口是 \(t=1\) 处的向上跳跃；连续性或沿下降极限的上半连续性正是排除该例的条件。

## 4. 可直接复用的点列定理候选

以下不是新的 Claim，而是把 C185/JP3 的后端压缩为目标一接口。

**定理候选 T1-S（scalar-to-point）。** 设 \(X\) 完备、\(S\subset X\) 非空闭、\(U\subset X\) 开，允许关系在
\(D_R=U\cap\{x:d(x,S)\le R\}\) 上有 coverage。对每个允许转移 \(x\mapsto y\)，同时有
\[
d(y,S)\le\phi(d(x,S)),\qquad
\|y-x\|\le b(d(x,S)),\tag{T18}
\]
其中 \(\phi,b\) 非减，\(\phi:[0,R]\to[0,R]\)，并且 \(\phi^k(t)\to0\)。若
\[
H_b(d_0):=\sum_{k=0}^{\infty}b(\phi^k(d_0))
<d(x_0,X\setminus U),\tag{T19}
\]
则每条允许选择政策都可无限延拓、留在 \(U_R\)，满足
\[
d(x_k,S)\le\phi^k(d_0),\qquad
\sum_{k\ge0}\|x_{k+1}-x_k\|\le H_b(d_0),\tag{T20}
\]
并收敛到 \(x_\infty\in S\cap U\)。尾界为
\[
\|x_\infty-x_k\|
\le\sum_{j=k}^{\infty}b(\phi^j(d_0)).\tag{T21}
\]
证明只用 (T3)、有限前缀三角不等式、严格预算、完备性和闭性；不使用 PPA 的单调性名称。若只知 (T1) 而无第二个步长/势条件，T1-S 的点列和长度结论不可得。若用联合势 (T11) 代替 (T18)，则由 JP3 的望远镜证明得到同样结论，且可能严格优于独立 \(b\) 包络。

在 Hilbert/有限维 PPA 中，(T18) 的 \(b\) 可由反射模给出
\(B(t)=(t+\omega(t))/2\)，而 \(\phi\) 可取直接、能量或零锚分支的最小标量上界；这正是 NGK-15--17 和 TL1--TL9 的编译。真实残差评价窗、完整纤维和留域门必须在进入 T1-S 前独立关闭。

## 5. LMZ（MOR 2026）的原文核对

### 5.1 来源身份

Guoyin Li, Boris Mordukhovich, Jiangxing Zhu,
Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods,
Mathematics of Operations Research, DOI 10.1287/moor.2024.0570, published online 2026-04-07；arXiv:2406.13207（2024-06-19 提交）。论文第 4 节是抽象收敛框架；第 7 节把它用于带动量的高阶正则化 Newton。这里只记录可逐字定位的 paper fact，不把其算法条件自动转成一般 PPA/GPPA 条件。

### 5.2 \(\tau\) 的原文定义与充分门

第 4 节式 (4.3)（预印本 PDF 第 7 页附近）定义
\[
\tau(0)=0,\qquad
\limsup_{t\downarrow0}
\frac{\sum_{n=0}^{\infty}\tau^n(t)}{t}<\infty.\tag{LMZ-4.3}
\]
原文称此为 asymptotically shrinking around zero，并明确
\(\tau(t)=\alpha t\)（\(0<\alpha<1\)）满足，而 \(\tau(t)=t\) 不满足。

紧接着的 Lemma 4.2 给出易检验充分条件：\(\tau\) 非减、\(\tau(0)=0\)，且
\[
\limsup_{t\downarrow0}\tau(t)/t<1.\tag{LMZ-4.2}
\]
证明在小窗内取 \(\tau(t)\le\varepsilon t\)，归纳得
\(\tau^n(t)\le\varepsilon^n t\)。这比 (T4) 的“每个正点严格下降”更强，因为它要求零点附近线性归一化尾。

### 5.3 Theorem 4.3：抽象点列—长度框架

LMZ 先固定基本条件 (H0)--(H3)：

* (H0) \(f(x_{k+1})\le f(x_k)\)；
* (H1) 辅助量 \(e_k\) 控制真实步长：当 \(e_k\to0\) 时，
  \(\|x_{k+1}-x_k\|\le c e_k\)；
* (H2) 存在 \(w_{k+1}\in\partial f(x_{k+1})\) 满足
  \(\|w_{k+1}\|\le b\,\beta(e_k)\)；
* (H3) 对收敛子列满足
  \(\limsup f(x_{k_j})\le f(\widetilde x)\)。

Theorem 4.3（第 4 节式 (4.4)--(4.7)）取非减且满足 (LMZ-4.3) 的 \(\tau\)，以及非负序列 \(s_k\to0\)，局部要求
\[
s_k\le\tau(s_{k-1}),\tag{LMZ-4.4}
\]
\[
e_k\le \ell_1e_{k-1}+\ell_2\Lambda_{k,k+1}+\ell_3s_k,\qquad
\Lambda_{k,k+1}
=\xi(f(x_k)-f(\bar x))-\xi(f(x_{k+1})-f(\bar x)),\tag{LMZ-4.5--4.6}
\]
其中 \(\ell_1<1\)、\(\xi\) 非减连续。若某个次水平集有界，并把局部邻域的首次进入/留域闭合，则
\[
\sum_{k=0}^{\infty}e_k<\infty,\qquad
\sum_{k=1}^{\infty}\|x_{k+1}-x_k\|<\infty,\qquad
x_k\to\bar x\in\Xi.\tag{LMZ-4.7}
\]
因此点列/长度结论依赖 \(e_k\) 的望远镜控制；(LMZ-4.4) 单独不足。

### 5.4 Theorem 4.4：\(\tau\) 的非线性收缩来源

Theorem 4.4 假设广义 metric subregularity（式 (4.13)）
\[
\psi\bigl(d(x,\Xi)\bigr)\le\gamma\,d\bigl(0,\partial f(x)\bigr)
\quad\text{在 }B(\bar x,\eta)\text{ 内},\tag{LMZ-4.13}
\]
以及 surrogate-to-target 界（式 (4.14)）
\[
e_k\le\ell\,d(x_k,\Xi).\tag{LMZ-4.14}
\]
令 \(\beta\) 为 (H2) 的误差模，定义
\[
\tau(t):=\psi^{-1}\!\left(\gamma b\,\beta(\ell t)\right),\tag{LMZ-4.15a}
\]
并要求
\[
\limsup_{t\downarrow0}\tau(t)/t<1.\tag{LMZ-4.15b}
\]
证明先得到精确距离递推（式 (4.16)）
\[
d(x_k,\Xi)\le\tau\bigl(d(x_{k-1},\Xi)\bigr).\tag{LMZ-4.16}
\]
再把 Theorem 4.3 应用于 \(s_k=d(x_k,\Xi)\)，得到
\[
x_k\to\bar x\in\Xi,\qquad
\|x_k-\bar x\|=O\!\left(\tau(\|x_{k-1}-\bar x\|)\right).\tag{LMZ-4.15}
\]
Remark 4.5 说明，对固定参数 proximal methods，取
\(e_k=\|x_{k+1}-x_k\|\) 时 (4.14) 在其所引用算法类中自动成立；这只是该算法及其假设下的 paper fact，不是对本库所有完整非单调 PPA 的自动桥。

第 7 节 Theorem 7.7 对高阶正则化 Newton 使用同一接口：广义 subregularity 为式 (7.23)，\(\tau\) 在式 (7.24) 取
\[
\tau(t)=\psi^{-1}\!\left(
\frac{3(1+\gamma L_1)L_2\ell}{q+1}\,t^{q+1}
\right),
\]
并再次要求 \(\limsup_{t\downarrow0}\tau(t)/t<1\)。这说明论文中的 nonlinear contraction 是由误差模 \(\beta\)、subregularity gauge \(\psi\) 和 surrogate 常数 \(\ell\) 复合而来；它不是一个单独对任意 PPA 输出距离的定义。

### 5.5 与目标一的准确关系与限制

LMZ 的式 (4.16) 形式上对应目标一的 \(d(y,S)\le\phi(d(x,S))\)，其中
\(S=\Xi\)、\(y=x_k\)、\(x=x_{k-1}\)、\(\phi=\tau\)。但有四个不可删的差别：

1. 它是**局部**框架：基本条件和 (4.4) 只在 \(B(\bar x,\eta)\) 且充分大 \(k\) 使用；全局 PPA 初值留域与 coverage 不由此给出。
2. 它先由 (H2)、(4.13)、(4.14) 导出 (4.16)；不能把 (4.16) 反过来当作原图的 subregularity 或 residual 证书。
3. 点列/长度结论还用 Theorem 4.3 的 \(e_k\) 递推和下降函数条件；单独距离递推不够（§3.1、§3.4）。
4. \(\Xi\) 是包含所有聚点的闭目标集合，且论文已先得到聚点
\(\bar x\in\Omega\)；这不是“任意初值必收敛到预先指定零集”的全局结论。

## 6. 与现有 C09/C10 结果的精确对照

### C09：一般模 \(\omega\) + 线性距离因子

C09 的完整前件在同一图块上给
\[
s_k\le h_\omega(d_k):=\frac{d_k+\omega(d_k)}2,\qquad
d_{k+1}\le\kappa d_k,\quad0<\kappa<1.
\]
这里距离尾是几何的：
\[
d_k\le\kappa^k d_0,
\]
而步长可和需要
\[
\sum_k h_\omega(\kappa^k d_0)<\infty.
\]
线性项总是可和，剩余正是
\(\sum_k\omega(\kappa^k d_0)\)；C09 的
\(\int_0^R\omega(t)\,dt/t<\infty\) 与该几何采样级数等价（GM10--GM14）。因此 C09 的 Dini 门是**步长模**门，距离收缩已由独立的 \(\kappa\) 给出；它不是 \(\Delta=t-\phi(t)\) 的积分门。

### C10：距离几何下降但点列/长度的非 Dini 边界

C10 的完整对数双支关系具有
\[
d_{k+1}=\frac14d_k,\qquad
d_k=4^{-k}d_0,
\]
同时切向步长满足
\[
s_k\asymp\ell_a(4^{-k}d_0)
=[\log(e/d_0)+k\log4]^{-a}.
\]
所以
\[
\sum_k s_k<\infty\quad\Longleftrightarrow\quad a>1,
\]
而 \(d_k\to0\) 对所有 \(a>0\) 都成立。\(a=1\) 是调和边界，\(0<a\le1\) 时点列甚至不收敛（切向坐标发散），尽管集合距离几何下降。其 Dini 判别
\[
\int_0\ell_a(t)\,\frac{dt}{t}<\infty
\Longleftrightarrow a>1
\]
恰是步长模的积分门。该例是 §3.1 的结构化 PPA 见证：没有独立步长模/联合势，距离递推不产生点收敛。

### 与 \(\Delta\)-门的关系

* C09/C10 的 \(\phi(t)=\kappa t\) 属于 \(\Delta(t)\asymp t\)；\(\int t/\Delta(t)\,dt\) 自动有限，故距离级数无障碍。
* C10 的失败来自 \(b(t)=\ell_a(t)\) 的非 Dini 尾，而不是距离 \(\Delta\) 的临界。
* \(F(y)=y^2\) 例属于 \(\Delta(t)\asymp t^2\) 的 \(p=2\) 边界：距离级数发散，但实际 PPA 步长 \(b(t)=\Delta(t)\) 可和。
* 因而“C09 的 Dini 条件”“C10 的对数发散”和“\(\Delta\) 的 \(p=2\) 边界”是三个不同位置：前两者控制几何步长模，后一者控制从非线性距离缺口本身得到的距离级数。

## 7. 已闭合内容、objection 与下一步

### 已经闭合的可复用内容

1. 在完整量词、coverage、闭目标、标量窗和严格留域预算下，(T3)、(T8)、(T10)--(T12) 是直接的标量—几何后端，与 C02-v3、C185、JP3、NGK-5 的现有证明一致。
2. 距离趋零、距离级数有限、物理步长级数有限、点列收敛是四个不同层级；第 3 节的显式连续映射分别阻断了不允许的蕴含。
3. \(\Delta\)-积分门 (T14)--(T16) 给出可审计的充分条件和幂次 \(p=2\) 边界；\(F(y)=y^2\) 的正半轴 PPA 是该边界的解析见证。
4. LMZ 的 (LMZ-4.3)、(LMZ-4.16) 给出非线性 \(\tau\) 的一手定义和位置；其 point/length 结论需要额外 surrogate、descent/subgradient 条件。

### 仍未闭的 proof obligations

* 从具体非单调/多值 PPA 或固定核 GPPA 原图推导同一个全纤维 \(\phi\)，并证明它在真实残差评价窗内有效；仅控制所选图值不能升级为完整 resolvent。
* 证明 coverage 与严格留域预算，再调用标量递推；不能以 \(\phi(t)<t\) 替代输入存在性。
* 若目标是点列而非距离，给出步长模 \(b\)、联合势 \(W\)、或相应的 Fejér/Opial 结构；物理核还需核逆模和物理步长可和。
* 对仅有 \(\phi^k(t)\to0\) 的非线性率，检查 \(H_\phi\) 或 \(H_{\phi,b}\)；LMZ 的归一化尾门不能无条件替代给定初值的有限尾门。
* 对 \(\Delta\)-积分门若要去掉 \(\Delta\) 单调性，需另给离散尺度比较；目前仅保留 (T13)--(T15) 的明确范围。

### 研究状态裁决

本笔记没有把“非线性距离收缩”升级为一般定理或新颖性主张；它固定了可复用的标量后端、LMZ 的精确 paper fact 及四类独立缺口。下一步应针对一个具体完整原图，先完成 coverage、true residual window、all-output \(\phi\) 三项，再选择 (T10) 独立尾或 (T11) 联合势；缺任一项则保持 candidate/open，不能把数值轨道或有限搜索当作证明。

## 8. 来源与仓库交叉索引

* LMZ 预印本：https://arxiv.org/abs/2406.13207；正式 MOR 页面：https://pubsonline.informs.org/doi/10.1287/moor.2024.0570。
* 普通 RLEB–PPA 真残差接口：research/rleb_ppa.md、C02-v3。
* 允许转移、全部政策和实际幂半径：research/canonical/allowed_transition_local.md。
* 联合距离—步长后端：research/canonical/unified_ppa_joint_certificates.md。
* 固定核一般模与物理提升：research/canonical/generalized_ppa_modulus.md、research/comparisons/2026_08_gppa_nfb/gppa_nonlinear_kernel_theorem.md。
* 标量尾势与 GPPA：research/canonical/gppa_tail_lyapunov_bridge.md。
* C09/C10 一般模与对数边界：research/canonical/general_modulus_dynamics.md。

