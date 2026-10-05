# 平面旋转族：完整 Cayley、循环阶与两个取样角

<a id="pr-object"></a>
## 完整对象、来源与尺度

在实 \(H=\mathbb R^2\) 取 \(K(x_1,x_2)=(-x_2,x_1)\)，
\(Q_\theta=cI+sK\)，\(c=\cos\theta,s=\sin\theta\)，
\(-\pi\le\theta\le\pi\)。每个算子都是**全域单值完整图**、
双射、等距，零集 \(\{0\}\)，逆为 \(Q_{-\theta}\)。
本页全图 RL 的尺度是两 Minty **输入的距离** \(\|p-q\|\le R\)，
包括零距离的全部图点对；只有计算锐常数比值时取 \(0<t\le R\)。
若改成两输入各在半径 \(R\) 球内，最大对距会变成 \(2R\)。

来源 Z07 `work/c_gx053_065.md` 第 765–839 行给旋转族，
840–876、877–908 行分别为 GX-062、GX-063。它们是同一参数族的
两个角度，不是两个不相关的算法。以下直接证明代数和循环性；
Voisei v2 Example43的归属/编号已核于[LIT-VOISEI-2024](../../LITERATURE.md#lit-voisei-2024)；LT非负参数命名见[LIT-LT-2025](../../LITERATURE.md#lit-lt-2025)。这些不承担本页直接证明，先行性未审。

<a id="pr-cayley"></a>
## C122-v1：所有步长的完整 Minty 纤维与锐尺度

固定 \(\lambda>0\)，令
\[
\Delta=1+2\lambda c+\lambda^2,
\qquad N=1-2\lambda c+\lambda^2. \tag{PR1}
\]
因 \(K^2=-I\)、\(K^*=-K\)，任意图点差 \(a\) 满足
\[
\|(I+\lambda Q_\theta)a\|^2=\Delta\|a\|^2,
\quad\|(I-\lambda Q_\theta)a\|^2=N\|a\|^2. \tag{PR2}
\]
\(\Delta=0\) 的**唯一**参数是 \(Q_\theta=-I,\lambda=1\)
（\(\theta=\pi\) 与 \(-\pi\) 同一矩阵）。此时 Minty 自然域
\(D=\{0\}\)，完整 \(J(0)=H\)、其它输入的纤维为空；
同输入对应不同反射输出，任何在零点消失的全图反射模都失败。

若 \(\Delta>0\)，全部 Minty 纤维由矩阵逆穷尽，自然域为 \(H\)：
\[
J_{\lambda Q_\theta}
=\frac{(1+\lambda c)I-\lambda sK}{\Delta},\qquad
R_{\lambda Q_\theta}
=\frac{(1-\lambda^2)I-2\lambda sK}{\Delta}, \tag{PR3}
\]
\[
\|Jp-Jq\|=\Delta^{-1/2}\|p-q\|,\qquad
\|Rp-Rq\|=\ell\|p-q\|,
\quad\ell=\sqrt{N/\Delta}. \tag{PR4}
\]
因 \(I+\lambda Q_\theta\) 满射，每个输入差 \(t>0\) 可实现。
故在输入**对距**不超过 \(R>0\) 的窗内，任意 \(0<\gamma\le1\)
的最小全对常数恰是
\[
L^*_{\lambda,\gamma;R}=\ell R^{1-\gamma}. \tag{PR5}
\]
对无界全图，\(\gamma=1\) 的锐常数为 \(\ell\)；
任意 \(0<\gamma<1\) 无有限常数，**唯一**例外是
\((\theta,\lambda)=(0,1)\)，此时 \(R\equiv0\)、最小常数 0。
本结论不把有界窗继承的次线性指数称为临界全图幂。

在 \(\Delta>0\) 时，若采用 \(\lambda\langle a,Q_\theta a\rangle
\ge-\tau\|(I+\lambda Q_\theta)a\|^2\) 的同参数 LT 约定，
最小**有符号** \(\tau\) 为 \(-\lambda c/\Delta\)；
若定义只许 \(\tau\ge0\)，最小值为
\(\max\{0,-\lambda c/\Delta\}\)。两个数不能混用。

<a id="pr-cyclic"></a>
## C123-v1：循环单调阶与两张例卡的精确解释

对每个整数 \(n\ge2\)，采用
\(\sum_{j=0}^{n-1}\langle z_j-z_{j+1},Q_\theta z_j\rangle\ge0\)、
\(z_n=z_0\) 的循环约定。把 \(H\) 识别为复平面并对
\((z_j)\) 作离散 Fourier 分解，二次型的各模系数（忽略正的
共同归一化因子）为
\[
2\sin(\pi k/n)\sin(\pi k/n-\theta),
\quad k=1,\ldots,n-1. \tag{PR6}
\]
任意单模都可取为真实平面向量循环
\(z_j=e^{2\pi i k j/n}z\)，所以所有系数非负是必要且充分的。
首尾两个模给精确门槛，其余模随之非负：
\[
Q_\theta\text{ 是 }n\text{-循环单调}
\quad\Longleftrightarrow\quad |\theta|\le\pi/n
\quad\Longleftrightarrow\quad c\ge\cos(\pi/n). \tag{PR7}
\]
该范围内它单调；若一个图点与全部图点单调相关，用
\(z+th\) 的正负 \(t\to0\) 即迫其等于 \(Q_\theta z\)。
所以完整图极大单调，也无真 \(n\)-循环单调扩张。

普通单调当且仅当 \(c\ge0\)；\(\langle a,Q_\theta a\rangle
=c\|a\|^2\)、\(\|Q_\theta a\|=\|a\|\)，故两个正系数
（强单调、cocoercivity）在 \(c>0\) 时均锐等于 \(c\)。
这时等号配对只可能 \(a=0\)，从而 paramonotone；
rectangular 的定义中关于变量 \(z\) 的二次型有正主项
\(c\|z\|^2\)，其下确界有限。对每个角度
\[
\|x-Q_{-\theta}y\|=\|Q_\theta x-y\|, \tag{PR8}
\]
故普通 MR/MSR/SMR/SMSR（以完整算子逆纤维）全局锐系数
都是 1，即使某个算法步长的 Minty 对应不单值也不变。

<a id="pr-two-angles"></a>
## GX-062 与 GX-063：同逆条件数、不同循环阶

| 对象 | \(Q_{\pi/3}\)（GX-062） | \(Q_{\pi/4}\)（GX-063） |
| --- | --- | --- |
| 最高循环阶；下一阶 | 3；非 4 | 4；非 5 |
| 强单调与 cocoercivity 锐系数 | \(1/2\) | \(1/\sqrt2\) |
| \(\Delta\) | \(1+\lambda+\lambda^2\) | \(1+\sqrt2\lambda+\lambda^2\) |
| \(\ell^2\) | \((1-\lambda+\lambda^2)/\Delta\) | \((1-\sqrt2\lambda+\lambda^2)/\Delta\) |
| signed \(\tau^*\)；非负 \(\tau^*\) | \(-\lambda/(2\Delta)\)；0 | \(-\lambda/(\sqrt2\Delta)\)；0 |
| 全算子逆像模 | 1 | 1 |

两角在每个 \(\lambda>0\) 有 \(0<\ell<1\)，完整近端和反射
都是全域线性严格收缩；若要写轨道，固定初值后
\(\|J^kp\|=\Delta^{-k/2}\|p\|\)，
\(\sum_{k\ge0}\|J^{k+1}p-J^kp\|
=\lambda(\sqrt\Delta-1)^{-1}\|p\|\)。
这使用该同一角的完整线性 \(J\)，不从一般 RL–EB 模套用。

来源 GX-063 末句称“循环阶不由标量强单调模还原”，
在**这一个旋转族内**与 (PR7) 矛盾，因为正强单调系数
\(\mu=c\) 恰给 \(n\)-循环阶门 \(\mu\ge\cos(\pi/n)\)。
可保留的准确比较是：两角的**逆像条件数都为 1**，却有
不同循环阶与不同强单调系数。这不声称一般算子族中只靠
强单调系数便能决定循环阶；Voisei例号已在上述一手卡按v2核定，新颖性仍待核。
