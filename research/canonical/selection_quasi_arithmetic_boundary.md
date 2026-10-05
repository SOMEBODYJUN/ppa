# 正则拟算术均值：非负起步的共同尾与极限选择界

本页给 C158-v1 的独立证明。P16 指定打印公式的小直径问题只作为
移植边界记录；这里的共同尾和两初值 Lipschitz 界不依赖该公式的正确性。
一手版本与条目核验见 [PRIMARY_SELECTION_IMPORTS](selection_primary_interfaces.md)。

<a id="qa-object"></a>
## QA-OBJECT：对象、函数类和固定量词

取非空开区间 \(I\subset\mathbb R\)、整数 \(k\ge1\)。采用 P16 的完整函数类：
\[
\begin{split}
\mathcal S(I)&=\{f\in C^2(I): f'(t)\ne0\ (t\in I),\quad
 f''\text{ 在每个紧子区间上有界变差}\},\\
\mathcal S_K(I)&=\{f\in\mathcal S(I):
 \sup_{t\in I}|f''(t)/f'(t)|\le K\},\qquad K>0.
\end{split}
\tag{QA1}
\]
本页选开区间避免端点微分约定；其上任意闭工作窗均在证明范围内。
导数处处非零意味着每个生成元严格单调，但不要求全 \(I\) 上另有
同一正下界 \(|f_i'|\ge c\)。给定 \(f_1,\ldots,f_k\in\mathcal S_K(I)\)，定义
\[
A_i(x)=f_i^{-1}\!\left(\frac1k\sum_{j=1}^k f_i(x_j)\right),\qquad
T(x)=(A_1(x),\ldots,A_k(x)),\quad x\in I^k.
\tag{QA2}
\]
每个均值属于 \([\min x,\max x]\)，所以 \(T:I^k\to I^k\) 完整单值，
且迭代始终位于同一初值的坐标区间内。记
\[
d(x)=\max x-\min x,\quad d_n(x)=d(T^n x),\quad
X_D=\{x\in I^k:d(x)\le D\}.
\tag{QA3}
\]
\(X_D\) 是凸的不变域，可以无界。以下先固定 \(I,k,K,f_1,\ldots,f_k,D\)，
再选辅助数 \(0<\ell<1/\alpha\)，其中
\(\alpha=(3+7e)/3\)。全部常数随后一次确定，对每个 \(x\in X_D\)
与每个声明范围内的整数 \(n\) 同时成立。

<a id="qa-first-round"></a>
## QA-FIRST-ROUND：打印公式的负起步边界

P16 arXiv:1412.2997v1 Theorem 1（PDF/印刷 p.4）以及正式版 Theorem 3.2
（PDF p.5／印刷 p.219）均打印
\[
n_0=\left\lceil\log_2\frac{e^{Kd(x)}-1}{e^\ell-1}\right\rceil,
\qquad
d_n(x)<\frac1{\alpha K}(\alpha\ell)^{2^{n-n_0}}
\quad(n\ge n_0),\quad 0<\ell<1.
\tag{QA4-print}
\]
这里没有把 \(n_0\) 夹到非负整数。正式版虽已排除常向量，小的非零直径仍可使
\(n_0<0\)。因此不能把 (QA4-print) 按其打印量词作为通用尾直接导入。

**严格反证，不依赖浮点。** 取 \(I=\mathbb R,k=2,K=1\)，
\(f_+(t)=e^t,f_-(t)=e^{-t}\)。二者均属于 \(\mathcal S_1(I)\)。对
\(x=(d/2,-d/2)\)、\(d>0\)，每步仍关于零对称，且
\[
d_0=d,\qquad d_{n+1}=2\log\cosh(d_n/2),\qquad
d_1\sim d^2/4\quad(d\downarrow0).
\tag{QA5}
\]
固定任一 \(\ell\in(0,1/\alpha)\)，令 \(q=\alpha\ell\in(0,1)\)、
\(a=e^\ell-1>0\)。对充分小的 \(d>0\)，打印的 \(n_0\le1\)，所以
\(n=1\) 已是其允许步数。由 \(\lceil u\rceil<u+1\) 得
\[
2^{1-n_0}>\frac{a}{e^d-1},\qquad
\frac1\alpha q^{2^{1-n_0}}
<\frac1\alpha\exp\!\left(-\frac{-a\log q}{e^d-1}\right)=o(d^2).
\tag{QA6}
\]
这与 (QA5) 矛盾。v1 Theorem 2／正式 Theorem 3.3 的优化包络同样不能
无条件沿用。其参数为
\(\mu=\min_{0<\ell<1}(\alpha\ell)^{(e^\ell-1)/2}\)，在 \(\ell=\xi\) 达到；
端点极限及 \(\ell<1/\alpha\) 的值说明可取
\(0<\xi<1/\alpha\)、\(0<\mu<1\)。在当前 \(K=1\) 的例中，其打印阈值是
\(n\ge n_1(d)=(\log_2e)d-\log_2(e^\xi-1)+1\)。
先取固定整数 \(n>1-\log_2(e^\xi-1)\)，再取充分小的 \(d>0\)，则该步数合法；
(QA5) 给 \(d_n\sim4^{1-2^n}d^{2^n}\)，而打印的
\((\alpha K)^{-1}\mu^{2^n/(e^{Kd}-1)}\) 为 \(\exp(-c/d)\) 级，
\(0<\mu<1\)。v1 Theorem 3 的定量近似式继承该包络问题。
这些判断限于所列公式和小非零直径量词，不是对论文全部结论的否定，也不声称已有正式勘误。

<a id="qa-uniform-tail"></a>
## QA-UNIFORM-TAIL：修复后的统一超几何点尾

**定理。** 在 (QA1)–(QA3) 下，先设 \(D>0,K>0\)，固定
\(0<\ell<1/\alpha\)，令
\[
a_D=e^{KD}-1,\quad q=\alpha\ell\in(0,1),\quad
N=\max\left\{0,\left\lceil\log_2\frac{a_D}{e^\ell-1}\right\rceil\right\}.
\tag{QA7}
\]
每条轨道有唯一对角极限
\(\Pi(x)=M(x)\mathbf1\)，且对全部 \(x\in X_D\)，
\[
\begin{split}
d_n(x)&\le \frac1K\log(1+a_D2^{-n})\quad(n\ge0),\\
\|T^n x-\Pi(x)\|_\infty&\le d_n(x)
\le\frac1{\alpha K}q^{2^{n-N}}\quad(n\ge N).
\end{split}
\tag{QA8}
\]
特别地，取
\[
b=2^{-N}\log(1/q)>0,\qquad
A=\max\{1/(\alpha K),D/q\},
\]
则 \(\|T^n x-\Pi(x)\|_\infty\le A e^{-b2^n}\) 对所有 \(x\in X_D,n\ge0\)
同时成立。欧氏范数下把右边乘以 \(\sqrt k\) 即可。
这先固定参数再全称量化初值；对任意 \(\varepsilon>0\)，可选择只依赖
\(K,D,\ell,\varepsilon\) 的共同步数，使整个 \(X_D\) 的尾不超过 \(\varepsilon\)。

**证明。** 将每个生成元乘以其导数的符号，不改变均值，因而可在下面的计算中取
\(f_i'>0\)。令
\(E_{\pm K}(x)=(\pm K)^{-1}\log(k^{-1}\sum_j e^{\pm Kx_j})\)。
\(|f_i''/f_i'|\le K\) 说明
\(u\mapsto f_i(\log u/K)\) 凹，而
\(u\mapsto f_i(-\log u/K)\) 凸。Jensen 不等式分别给
\[
E_{-K}(x)\le A_i(x)\le E_K(x).
\]
把坐标升序排列，忽略下面和式的负项，可得
\[
\begin{split}
e^{K d(Tx)}-1
&\le e^{K(E_K(x)-E_{-K}(x))}-1\\
&=\frac1{k^2}\sum_{i,j}(e^{K(x_i-x_j)}-1)\\
&\le\frac{k(k-1)}{2k^2}(e^{Kd(x)}-1)
\le\frac12(e^{Kd(x)}-1).
\end{split}
\tag{QA9}
\]
迭代 (QA9) 给 (QA8) 第一式，特别地 \(d_n\to0\)。各步坐标最小值非减、
最大值非增，因此夹出的公共极限 \(M(x)\) 存在，且每个坐标到它的距离不超过
\(d_n\)。这也证明了极限身份。

下面直接证明局部平方递推，不调用 P16 有问题的尾公式。写
\(\bar x=k^{-1}\sum_jx_j\)、\(d=d(x)\)。在 \([\min x,\max x]\) 上，
\(|(\log f_i')'|\le K\)，故 \(\sup f_i'/\inf f_i'\le e^{Kd}\)。
在 \(\bar x\) 展开二阶 Taylor 公式，求平均后一次项抵消，再对逆函数用均值定理，得
\[
|A_i(x)-\bar x|
\le\frac K2 e^{Kd}\frac1k\sum_j(x_j-\bar x)^2
\le\frac K2e^{Kd}d^2.
\]
因此，当 \(Kd\le1\) 时，
\[
d(Tx)\le K e^{Kd}d^2\le eK d^2\le\alpha K d^2.
\tag{QA10}
\]
此证明仅用 (QA1) 中的 \(C^2\) 与对数导数界；有界变差条件保留是为对齐所核模型，
不是另加不可见依赖。

(QA7) 保证 \(a_D2^{-N}\le e^\ell-1\)，故
\(d_N\le\ell/K<1/K\)。轨道直径非增，所以 (QA10) 在全部 \(n\ge N\)
成立。令 \(u_n=\alpha Kd_n\)，则 \(u_N\le q\) 且 \(u_{n+1}\le u_n^2\)，
归纳给 \(u_n\le q^{2^{n-N}}\)，证明共同尾。
\(N=0\) 时首轮恰为 \(d_0\le\ell/K=q/(\alpha K)\)，没有负步数，也没有漏掉首轮系数。
对 \(n<N\)，用 \(\|T^nx-\Pi x\|_\infty\le D\) 及
\(e^{b2^n}\le e^{b2^N}=1/q\)，得到所述全步数 \(Ae^{-b2^n}\) 界。

同一共同尾还给实际点误差 \(e_n=\|T^nx-\Pi x\|_\infty\) 的共同 Q-二次上界：
\(d_n\le2e_n\) 与 (QA10) 推出
\[
e_{n+1}\le4\alpha K e_n^2\quad(n\ge N).
\tag{QA11}
\]
它是上界，不声明每条轨道的精确 Q 阶或非零渐近系数。

**退化情形。** 单个初值 \(d(x)=0\) 的轨道从第零步即固定，(QA8) 当然成立。
若整个初值族选 \(D=0\)，直接使用 \(\Pi(x)=x\)，不计算 \(\log0\) 或 (QA7)。
(QA1)、(QA7) 的定理约定 \(K>0\)；若实际对数导数界为零，可任取正的安全上界
来用定理，或单独观察 \(f_i''=0\)，每个生成元仿射且全部 \(A_i\) 为算术均值：
第一步就到对角，\(e_n=0\) 对 \(n\ge1\)，不代入含 \(1/K\) 的式子。

<a id="qa-selection"></a>
## QA-SELECTION：两初值极限映射的共同 Lipschitz 界

在上述固定 \(K>0,D>0\) 的凸域 \(X_D\) 上，
\[
|M(x)-M(y)|=\|\Pi(x)-\Pi(y)\|_\infty
\le L_D\|x-y\|_\infty,
\qquad L_D=\exp\bigl(2(e^{KD}-1)\bigr).
\tag{QA12}
\]
这是本页的直接推导，不归作 P16 Theorems 1–3 的原陈述。

**证明。** 隐函数求导给
\[
\frac{\partial A_i}{\partial x_j}(x)
=\frac{f_i'(x_j)}{k f_i'(A_i(x))}>0,
\qquad \|DT(x)\|_{\infty\to\infty}\le e^{Kd(x)}.
\]
对任意 \(z\in X_D\)，链式法则及 (QA8) 给
\[
\begin{split}
\|D(T^n)(z)\|_{\infty\to\infty}
&\le\exp\left(K\sum_{j=0}^{n-1}d_j(z)\right)\\
&\le\exp\left(\sum_{j=0}^{n-1}\log(1+a_D2^{-j})\right)
\le\exp(2a_D)=L_D.
\end{split}
\tag{QA13}
\]
和式从 \(j=0\) 开始，\(\sum_{j=0}^\infty2^{-j}=2\)；漏掉首步会给错误的更小常数。
线段 \([x,y]\subset X_D\)，沿它积分导数即得全部 \(T^n\) 的同一 Lipschitz 界。
令 \(n\to\infty\) 得 (QA12)。此外 \(\Pi\) 在对角上恒等，故是到
\(\{t\mathbf1:t\in I\}\) 的连续回缩。\(D=0\) 时该回缩为恒等，系数 1；
\(K=0\) 的独立仿射情形中 \(M\) 为算术均值，同样系数 1。

<a id="qa-comparison"></a>
## QA-COMPARISON：AGM、任意复合与适用边界

AGM 的生成元为 \(f_1(t)=t,f_2(t)=\log t\)，其对数导数分别为 0 和 \(-1/t\)。
将以上证明限制在固定闭工作域 \([a,b]^2\)、\(a>0\)，全部轨道、Taylor 区间及
连接初值的线段均留在此域，窗内可取共同 \(K=1/a\)，故同样得到共同点尾与
Lipschitz 选择界；这里不声称某个包含 \([a,b]\) 的开区间上仍有此同一 \(K\)。
在含轴窗上 \(\log t\) 不定义，且 \(a\downarrow0\)
时这个 \(K\) 无界，所以这里没有授予包含坏轴的统一证书。
这与 [AGM-SELECTION](../topics/examples/arithmetic_geometric_mean.md#agm-selection)
的轴上对数坏模相容，不把正窗结论拼给轴。

若 \(F:I^k\to\mathbb R\) 在每个对角线点作为 \(I^k\) 上的函数连续，并且
\(F\circ T=F\)，则
\[
F(x)=\lim_nF(T^nx)=F(M(x)\mathbf1)=\varphi(M(x)),
\quad\varphi(t)=F(t\mathbf1).
\]
反之，每个连续 \(\varphi\) 给出连续不变函数 \(\varphi\circ M\)。
这里必须是在对角线点处的连续性；仅仅 \(F|_\Delta\) 连续不足以沿轨道取极限。
若 \(\varphi\) 在有关坐标窗有模 \(\omega_\varphi\)，则由 (QA8) 对同一初值得
\[
|\varphi(M(x))-\varphi([T^nx]_i)|
\le\omega_\varphi\!\left((\alpha K)^{-1}q^{2^{n-N}}\right)
\quad(n\ge N).
\]
任意 \(\varphi\) 的自由度属于复合函数，不能改称 \(M\) 的任意粗糙性；
本页反而在同一固定域上直接给 (QA12)。

本页没有编码具体完整 PPA 关系，也没有赋予其 RL、EB、严格兼容或新颖性。
它只闭合正则拟算术均值模型的共同速率与选择接口；全图认证若另作编码，仍是独立任务。
