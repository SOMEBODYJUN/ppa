# 全局双向影子：任意实 Hilbert 空间的完整证明

本页重建 [C03](../../CLAIMS.md) 的精确结论：同一个强单调双 Lipschitz 同胚，同时近似原关系的正向和逆向图点；统一因子为 \(1/\sqrt2\)，其最优性针对所有有限维共同的常数。
指定图锚必须被保留时，另有不同的常数 \(1\) 和独立命题。
证明不从有限样本 C19 推广，不使用 C04 的完整纤维分类或 degree，也不要求原关系 graph-maximal。
唯一承重的外部定理是任意 Hilbert 空间之间的同常数 Lipschitz 扩张，准确接口列于 GSH-IMPORT；其余步骤在本页给出。

<a id="gsh-object"></a>
## GSH-OBJECT · 对象、量词与 Cayley 坐标

令 \(H\) 为任意实 Hilbert 空间，允许无限维和非可分。
固定 \(\lambda,L>0\)、\(0<\gamma<1\)，令关系 \(F:H\rightrightarrows H\) 的整个图非空。
假设对**每一对** \((x,v),(y,w)\in\operatorname{gph}F\)，不限制输入对尺度，有
\[
\|(x-y)-\lambda(v-w)\|
\le L\|(x-y)+\lambda(v-w)\|^\gamma. \tag{GSH-1}
\]
这里“整个图”指被声明关系的全部图点，并不意味着图闭、定义域满或值域满。
记
\[
R=L^{1/(1-\gamma)},\qquad
D=\{x+\lambda v:(x,v)\in\operatorname{gph}F\}.
\]
若两个图点的 \(p=x+\lambda v\) 相同，GSH-1 使它们的 \(x-\lambda v\) 相同，求和与求差便使图点相同。因此
\[
C:D\to H,\qquad C(x+\lambda v)=x-\lambda v
\]
良定，且 \(\|C(p)-C(s)\|\le L\|p-s\|^\gamma\) 对全部 \(p,s\in D\) 成立。
反过来，给定这样的部分映射，其 Cayley 图为
\[
\operatorname{gph}F
=\left\{\left(\frac{p+C(p)}2,\frac{p-C(p)}{2\lambda}\right):p\in D\right\}. \tag{GSH-2}
\]
这证明所用坐标的双向等价；\(D\) 仍可为 \(H\) 的真子集。

对每个 \(0<\sigma<1\)，将构造一个 \(A_\sigma:H\to H\)，使后文全部图点和全部比较点共用此映射。
不同 \(\sigma\) 可产生不同映射；不主张扩张或影子的唯一性。

<a id="gsh-excess"></a>
## GSH-EXCESS · 精确二次余量

定义
\[
\begin{aligned}
M_\sigma
&=(1-\gamma)\gamma^{\gamma/(1-\gamma)}
 R^2\sigma^{-2\gamma/(1-\gamma)},\\
t_\sigma&=(\gamma L^2/\sigma^2)^{1/[2(1-\gamma)]}.
\end{aligned} \tag{GSH-3}
\]
则
\[
\sup_{t\ge0}\{L^2t^{2\gamma}-\sigma^2t^2\}=M_\sigma>0. \tag{GSH-4}
\]
在 \(t>0\) 上求导，导数为零等价于
\(\gamma L^2t^{2\gamma-2}=\sigma^2\)，只有解 \(t_\sigma\)。
函数在此前递增、此后递减，原点值为零而无穷远趋负无穷。
用 \(\sigma^2t_\sigma^2=\gamma L^2t_\sigma^{2\gamma}\) 代入，得到 GSH-3。
特别地，所有 \(p,s\in D\) 满足
\[
\|C(p)-C(s)\|^2\le\sigma^2\|p-s\|^2+M_\sigma. \tag{GSH-5}
\]

<a id="gsh-import"></a>
## GSH-IMPORT · 非可分空间也适用的准确扩张接口

本页导入如下定理：若 \(E_1,E_2\) 为实 Hilbert 空间，\(B\subset E_1\) 为任意非空子集，\(T:B\to E_2\) 为 \(k\)-Lipschitz，则存在 \(\widehat T:E_1\to E_2\)，使 \(\widehat T|_B=T\) 且 \(\operatorname{Lip}\widehat T\le k\)。
不要求有限维、可分、\(B\) 闭或 \(B\) 凸。若 \(T\) 为常值，常值扩张即可。

一手定位是 Azagra–Le Gruyer–Mudarra，*Kirszbraun’s Theorem via an Explicit Formula*，*Canadian Mathematical Bulletin* **64** (2021), 142–153，印刷页 **144，Theorem 1.2**，DOI [10.4153/S0008439520000314](https://doi.org/10.4153/S0008439520000314)，[出版社正式 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/15797B44C630B0E2A4BB12547759929D/S0008439520000314a.pdf/kirszbrauns_theorem_via_an_explicit_formula.pdf)。
已核原文定理的任意 Hilbert 源、目标和任意子集量词；印刷页 142 的引言亦明确讨论非可分情形。
这里只导入扩张存在与常数不增，不使用该文的显式公式、凸包求值或其它正则性。
同一导入见 [LIT-ALM-2021](../LITERATURE.md#lit-alm-2021)。

<a id="gsh-lift"></a>
## GSH-LIFT · 任意指标集提升与同一交叉估计

令 \(\ell^2(D)\) 为任意指标集 \(D\) 上有限支撑实函数空间的 Hilbert 完备化，内积为有限支撑向量的坐标乘积之和再连续延拓。
其坐标向量 \(e_p\) 满足 \(\langle e_p,e_s\rangle=0\) 当 \(p\ne s\)，且 \(\|e_p\|=1\)。
此定义允许任意基数的 \(D\)，不需要对 \(D\) 排成序列或为它选可数稠密集。
置
\[
\mathcal H=H\oplus\ell^2(D),\qquad
\tau^2=\frac{M_\sigma}{2\sigma^2},\qquad
B=\{(p,\tau e_p):p\in D\}.
\]
在 \(B\) 上定义 \(T(p,\tau e_p)=C(p)\)。
对不同 \(p,s\)，正交性和 GSH-5 给
\[
\begin{aligned}
\|T(p,\tau e_p)-T(s,\tau e_s)\|^2
&\le\sigma^2\|p-s\|^2+M_\sigma\\
&=\sigma^2\bigl(\|p-s\|^2+2\tau^2\bigr)\\
&=\sigma^2\|(p,\tau e_p)-(s,\tau e_s)\|_{\mathcal H}^2.
\end{aligned} \tag{GSH-6}
\]
相同点时两边都为零。因此 \(T\) 为 \(\sigma\)-Lipschitz。
GSH-IMPORT 的对象逐项对应如下：

| 外部前提 | 本页对象与验证 |
| --- | --- |
| Hilbert 源 \(E_1\) | \(\mathcal H=H\oplus\ell^2(D)\)，两完备 Hilbert 空间的正交和 |
| Hilbert 目标 \(E_2\) | 原空间 \(H\) |
| 任意非空子集 \(B\) | 上述提升集合；原图非空给 \(D\ne\varnothing\) |
| 全部点对的 Lipschitz 估计 | GSH-6 及相同点情形，常数至多 \(\sigma\) |

于是存在**一个**扩张 \(\widehat T:\mathcal H\to H\)。固定它，并定义
\[
N(q)=\widehat T(q,0)\qquad(q\in H).
\]
同一扩张立即使 \(N\) 全域 \(\sigma\)-Lipschitz。
对任意 \(p\in D,q\in H\)，比较提升点和基平面点，得到
\[
\|C(p)-N(q)\|^2
\le\sigma^2\|p-q\|^2+\frac{M_\sigma}{2}. \tag{GSH-7}
\]
量词为“存在一个 \(N\)，对所有 \(p,q\) 成立”；不能以逐查询分别选球交点替代此步骤。
这里只扩张提升后的 Lipschitz 数据，并未先假设 \(D=H\)，也未使用 Hölder 雪花嵌入。

<a id="gsh-shadow"></a>
## GSH-SHADOW · 两次全域反演与强单调常数

定义
\[
X(q)=\frac{q+N(q)}2,\qquad
Y(q)=\frac{q-N(q)}{2\lambda}. \tag{GSH-8}
\]
对于任意 \(x\in H\)，\(X(q)=x\) 等价于 \(q=2x-N(q)\)。
右侧的 Lipschitz 常数至多 \(\sigma<1\)。从任意 \(q_0\) 迭代得到
\(\|q_{j+1}-q_j\|\le\sigma^j\|q_1-q_0\|\)，故尾差被收敛的几何级数控制。
完备性给极限，连续性使它为固定点；两个固定点的距离至多其自身的 \(\sigma\) 倍，故唯一。
对任意 \(v\in H\)，相同论证用于 \(q=2\lambda v+N(q)\)，得到 \(Y(q)=v\) 的唯一解。
因此 \(X,Y\) 均为双射，定义
\[
A_\sigma=Y\circ X^{-1},\qquad
A_\sigma^{-1}=X\circ Y^{-1}. \tag{GSH-9}
\]

对 \(q_1,q_2\in H\)，记 \(h=q_1-q_2\)、\(k=N(q_1)-N(q_2)\)，则 \(\|k\|\le\sigma\|h\|\)，而
\[
(1-\sigma)\|h\|\le\|h\pm k\|\le(1+\sigma)\|h\|.
\]
应用到 \(X,Y\) 的差，得
\[
\operatorname{Lip}A_\sigma\le\frac{1+\sigma}{\lambda(1-\sigma)},\qquad
\operatorname{Lip}A_\sigma^{-1}\le\frac{\lambda(1+\sigma)}{1-\sigma}. \tag{GSH-10}
\]
故 \(A_\sigma\) 是双 Lipschitz 同胚。再算
\[
\begin{aligned}
\langle X(q_1)-X(q_2),Y(q_1)-Y(q_2)\rangle
&=\frac{\|h\|^2-\|k\|^2}{4\lambda}\\
&\ge\frac{1-\sigma^2}{4\lambda}\|h\|^2\\
&\ge\frac{1-\sigma}{\lambda(1+\sigma)}
 \|X(q_1)-X(q_2)\|^2.
\end{aligned} \tag{GSH-11}
\]
由于 \(X\) 满射，GSH-11 给 \(A_\sigma\) 在全部 \(H\) 上的强单调常数
\((1-\sigma)/(\lambda(1+\sigma))>0\)。

<a id="gsh-paired"></a>
## GSH-PAIRED · 原坐标交叉式、同时配对与最优参数

固定任意原图点 \((x,v)\) 与任意 \(z\in H\)，置
\[
p=x+\lambda v\in D,\qquad q=z+\lambda A_\sigma(z)=X^{-1}(z).
\]
写 \(d=x-z\)、\(e=v-A_\sigma(z)\)，则
\(p-q=d+\lambda e\)、\(C(p)-N(q)=d-\lambda e\)。
GSH-7 及平方差恒等式
\(\|d+\lambda e\|^2-\|d-\lambda e\|^2=4\lambda\langle d,e\rangle\)
给
\[
\langle x-z,v-A_\sigma(z)\rangle
\ge\frac{1-\sigma^2}{4\lambda}
 \|x-z+\lambda(v-A_\sigma(z))\|^2
-\frac{M_\sigma}{8\lambda}. \tag{GSH-12}
\]
分别取 \(z=x\) 和 \(z=A_\sigma^{-1}(v)\)，左侧都为零，故**同一个** \(A_\sigma\) 满足
\[
\lambda\|v-A_\sigma(x)\|\le r_\sigma,
\qquad \|x-A_\sigma^{-1}(v)\|\le r_\sigma,
\qquad
r_\sigma^2=\frac{M_\sigma}{2(1-\sigma^2)}, \tag{GSH-13}
\]
对 \(\operatorname{gph}F\) 中每个图点同时成立。

令 \(u=\sigma^2\in(0,1)\)。除去正的常数因子，\(r_\sigma^2\) 为
\(u^{-\gamma/(1-\gamma)}(1-u)^{-1}\)，其对数导数为
\[
-\frac{\gamma}{(1-\gamma)u}+\frac1{1-u}.
\]
只有在 \(u=\gamma\) 为零；函数在两端都趋无穷，此点为唯一最小点。
此时 \(M_{\sqrt\gamma}=(1-\gamma)R^2\)，于是
\[
\|v-A(x)\|\le\frac{R}{\sqrt2\lambda},\qquad
\|x-A^{-1}(v)\|\le\frac{R}{\sqrt2},
\qquad A=A_{\sqrt\gamma}. \tag{GSH-14}
\]
这完成 C03 的存在、同一性、全图量词及其显示常数证明。
对一个已经非空的完整纤维，逐点界可改写成到该 singleton 的 Hausdorff 界；本证明不保证未给出的原纤维非空。

<a id="gsh-sharp"></a>
## GSH-SHARP · 任意维数统一因子的下界

固定同一 \(\lambda,L,\gamma\)，因而固定 \(R\)。对每个整数 \(n\ge1\)，在
\(H_n=\{t\in\mathbb R^{n+1}:\sum_i t_i=0\}\cong\mathbb R^n\)
中取
\[
u_i=\frac{R}{\sqrt2}\left(e_i-\frac1{n+1}{\bf1}\right)
\quad(i=0,\ldots,n),\qquad
K_n=\operatorname{conv}\{u_0,\ldots,u_n\}.
\]
则 \(\sum_i u_i=0\)、\(\|u_i-u_j\|=R\) 当 \(i\ne j\)，且
\[
\|u_i\|^2=r_n^2=\frac{nR^2}{2(n+1)},\qquad
\frac1{n+1}\sum_{i=0}^n\|u_i-b\|^2=r_n^2+\|b\|^2
\quad(b\in H_n). \tag{GSH-15}
\]
所以任何单一中心 \(b\) 至少距某个顶点 \(r_n\)。

为使下界证人还具有全域 Cayley 参数和固定参数 graph-maximal 性，取欧氏投影 \(P_{K_n}\)。
这里不调用完整纤维分类：\(K_n\) 非空紧凸，平方距离在其上有唯一极小点；
沿任意凸线段的单侧导数给
\(\langle p-P_{K_n}p,z-P_{K_n}p\rangle\le0\) 对所有 \(z\in K_n\) 成立。
在两投影点处互用此式，得到
\(\|P_{K_n}p-P_{K_n}q\|^2\le\langle P_{K_n}p-P_{K_n}q,p-q\rangle\)，故投影非扩张。
凸组合和三角不等式说明 \(\operatorname{diam}K_n\le R\)，顶点对取等。
于是
\[
\|P_{K_n}p-P_{K_n}q\|
\le\min\{\|p-q\|,R\}
\le R^{1-\gamma}\|p-q\|^\gamma
=L\|p-q\|^\gamma. \tag{GSH-16}
\]
最后一个不等式在 \(\|p-q\|\le R\) 和 \(\|p-q\|\ge R\) 两区分别直接成立。

用 \(D=H_n\)、\(C=-P_{K_n}\) 在 GSH-2 定义关系 \(F_-\)。
它满足全图全尺度 GSH-1。其 \(x=0\) 恰当且仅当 \(p=P_{K_n}p\)，即 \(p\in K_n\)，故
\[
F_-(0)=K_n/\lambda.
\]
任何单值映射在输入零处只能选一个中心 \(A(0)\)，所以
\[
\sup_{v\in F_-(0)}\|v-A(0)\|\ge r_n/\lambda. \tag{GSH-17}
\]
同理，\(C=P_{K_n}\) 定义的 \(F_+\) 有
\(F_+^{-1}(0)=K_n\)。对任何在零处有单一逆像中心 \(A^{-1}(0)\) 的映射，
\[
\sup_{x\in F_+^{-1}(0)}\|x-A^{-1}(0)\|\ge r_n. \tag{GSH-18}
\]
两关系的 graph-maximal 性也直接成立：全部 \(p\in H_n\) 已有图点，任何兼容新点与同 \(p\) 的旧点比较，GSH-1 迫使 \(C\) 值相同，故新点并不新。

因此，若常数 \(c\) 在所有有限维上保证 GSH-14 的任一对应方向（或同一影子的双向保证），就必须对每个 \(n\) 有
\(c\ge r_n/R=\sqrt{n/[2(n+1)]}\)。令 \(n\to\infty\)，得 \(c\ge1/\sqrt2\)。
GSH-14 给相同上界，故任意维数统一的因子恰为 \(1/\sqrt2\)。
下界已针对任意单一中心成立，不依赖影子的连续性、单调性或条件数。
正反两方向可使用不同证人；任一证人就排除更小的共同因子。
这不确定每个固定维数的最优因子，也不证明 GSH-10–11 的 conditioning 常数最优。

<a id="gsh-anchor"></a>
## GSH-ANCHOR · 保留指定图锚是不同的命题

另固定一个已给定图点 \((x_0,v_0)\in\operatorname{gph}F\)，并要求
\(A_{\sigma,0}(x_0)=v_0\)。记 \(p_0=x_0+\lambda v_0\)、\(c_0=x_0-\lambda v_0\)。
对每个 \(0<\sigma<1\)，仍在 \(H\oplus\ell^2(D)\) 中提升全部 \(p\in D\)，但现在取
\(\tau_0^2=M_\sigma/\sigma^2\)，并增加基平面数据 \((p_0,0)\mapsto c_0\)。
不同提升点的附加平方距离为 \(2\tau_0^2\)，提供 \(2M_\sigma\ge M_\sigma\) 的余量。
任意提升点与新增锚之间，GSH-5 给
\[
\|C(p)-c_0\|^2
\le\sigma^2\|p-p_0\|^2+M_\sigma
=\sigma^2\|(p,\tau_0e_p)-(p_0,0)\|^2. \tag{GSH-19}
\]
这也涵盖 \(p=p_0\)，此时两个源点不同而指定的目标相同。
所以全部数据仍为 \(\sigma\)-Lipschitz；GSH-IMPORT 扩张后限制到基平面，得到一个 \(N_0\)，满足
\[
N_0(p_0)=c_0,\qquad
\|C(p)-N_0(q)\|^2\le\sigma^2\|p-q\|^2+M_\sigma. \tag{GSH-20}
\]
用 GSH-8–11 的构造和证明得到同一类强单调双 Lipschitz 同胚 \(A_{\sigma,0}\)，常数仍为 GSH-10–11。
因为 \(X_0(p_0)=x_0,Y_0(p_0)=v_0\)，它保留指定锚。
GSH-12 的平方差计算现在给
\[
\langle x-z,v-A_{\sigma,0}(z)\rangle
\ge\frac{1-\sigma^2}{4\lambda}
 \|x-z+\lambda(v-A_{\sigma,0}(z))\|^2
-\frac{M_\sigma}{4\lambda}. \tag{GSH-21}
\]
因此对每个原图点同时有
\[
\lambda\|v-A_{\sigma,0}(x)\|,
\ \|x-A_{\sigma,0}^{-1}(v)\|
\le\sqrt{\frac{M_\sigma}{1-\sigma^2}}. \tag{GSH-22}
\]
仍在 \(\sigma=\sqrt\gamma\) 最小化，得到半径 \(R\)，即正向界 \(R/\lambda\)、逆向界 \(R\)。

锚条件下的因子 \(1\) 已在一维最优：令 \(K=[0,R]\)，分别取 \(C=-P_K\) 和 \(C=P_K\)。
GSH-16 的证明照用，两者均全域、graph-maximal。
前者有 \(F(0)=[0,R/\lambda]\)，锚 \((0,0)\) 强制 \(A_0(0)=0\)，故最坏正向误差至少 \(R/\lambda\)。
后者有 \(F^{-1}(0)=[0,R]\)，同一锚和单值逆强制 \(A_0^{-1}(0)=0\)，故最坏逆向误差至少 \(R\)。
这证明加锚版本的最优因子，并不改变无锚 C03 的因子 \(1/\sqrt2\)。

<a id="gsh-scope"></a>
## 依赖、来源身份和验收边界

本页主链为 GSH-1–7 → GSH-8–13 → GSH-14–18；加锚命题为另加指定图点后的 GSH-19–22。
先依据规范陈述独立重建提升、双反演及配对，再核 [S23 原 TeX §3](../../history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 的
`lem:excess`、`lem:crosslift`、`thm:shadow`、`thm:sharpness`、`thm:anchor`；所列量词、常数和指定锚身份一致。
原稿的 enlargement 推论和其它章节不作为本页的证明依赖；这里未据来源标题推定新颖性。

GSH-1–14 的上界构造没有使用 \(H\) 可分、原图闭、原图 graph-maximal、原纤维非空覆盖、有限维紧性或 C04。
GSH-SHARP 的有限维投影证人只为下界，不能反过来限制 GSH-LIFT 的任意 Hilbert 上界。
局部成对 RL、有限样本兼容、逐查询代理、真实逆分支选择稳定、每维最优因子与有限计算复杂度均不是此结论。
定理的证据状态由 Claim 总账和独立审查登记决定；本页只提供可逐式重建的证明。
