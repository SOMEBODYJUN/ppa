# 对角线加离散竖支：完整近端任意选择收敛而全对 RL 失败

<a id="ds-object"></a>
## 对象、来源与证明范围

在实直线取完整关系
\[
A=\{0\}\cup\{1/n:n\ge1\},\qquad
F(0)=A,\qquad F(x)=\{x\}\quad(x\ne0).
\tag{DS1}
\]
因此
\[
\operatorname{gph}F=\{(x,x):x\in\mathbb R\}\cup(\{0\}\times A).
\tag{DS2}
\]
两部分均闭，故完整图闭；定义域为整个 \(\mathbb R\)。以下固定任意
\(\lambda>0\)，所有残差均对所写完整纤维取下确界。目标为完整零集
\(S=F^{-1}(0)=\{0\}\)。不存在域外空纤维导致的误差界真空。

历史观察别名 GX-075。精确来源为
[9/01 ZIP](../../../history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip)
内 `work/c_gx066_077.md` 的 GX-075；原稿的项目构造归属只作来源报告，
以下各式由 (DS1) 独立重算。ZIP SHA-256 为
`b40d2aae4eef13ef2df2840df1b74333793e56de112addab7eca67dfc9bdd3ba`；
成员字节 SHA-256 为
`e67b4a09a1d2fb9fcd4c2681f831d740a12989e7a731d884944f4ef1074a7105`。

本卡四个单元 DS-EB、DS-PPA、DS-RL、DS-QUADRATIC 均为 `derived-checked`，
依赖 [D01–D04](../../foundations.md) 的完整图、真残差与全对 RL 定义，
不用外部定理。DS-PPA 的全选择轨道和 DS-EB 的一般消失 gauge 障碍是本次推导；
不把它们标作历史来源已经证明的命题。外部先行性未核。

<a id="ds-eb"></a>
## DS-EB-v1：固定零目标锐线性；目标邻域中没有消失 gauge

### 完整真残差和全部逆纤维

由 (DS1)，对**全部** \(x\in\mathbb R\)，
\[
r_F(x):=\inf_{v\in F(x)}|v|=|x|=d(x,S).
\tag{DS3}
\]
故全域线性真 EB 的最优模为 \(1\)，局部最优模也为 \(1\)。
每个 \(q>1\) 的局部幂 EB 均因 \(|x|/r_F(x)^q=|x|^{1-q}\to\infty\)
而失败；\(0<q<1\) 的邻域收缩最优模为 \(0\)。零点孤立，所以 (DS3)
同时是以点距 \(|x-0|\) 写的强固定目标误差界。

完整逆纤维为
\[
F^{-1}(y)=
\begin{cases}
\{0\},&y=0,\\
\{0,y\},&y\in A\setminus\{0\},\\
\{y\},&y\notin A.
\end{cases}
\tag{DS4}
\]
因此所有逆像都满足 \(|x|\le |y|\)，且负目标 \(y<0\) 取等。
这给完整逆关系在 \((0,0)\) 的线性 calm / isolated calm 精确模 \(1\)。
最近逆点也满足
\[
h(y):=d(0,F^{-1}(y))=
\begin{cases}
0,&y\in A,\\
|y|,&y\notin A,
\end{cases}
\qquad h(y)\le |y|,
\tag{DS5}
\]
最近点版本的局部精确模仍为 \(1\)，由所有负目标取等；这是此处
明确采用的 HREG 量词。

### 更换右端残差后，任意消失 gauge 都失败

取任意 \(\bar t>0\) 与非减函数
\(\psi:[0,\bar t]\to[0,\infty)\)，假设 \(\psi(0)=0\) 且
\(\psi(t)\to0\) 当 \(t\downarrow0\)。不存在有限 \(\kappa\ge0\)、
\(\varepsilon>0\) 使
\[
h(y)\le\kappa\psi\bigl(d(y,F(0))\bigr)
       =\kappa\psi(d(y,A))
\quad\text{对所有 } |y|<\varepsilon,\ d(y,A)\le\bar t.
\tag{DS6}
\]

**证明。** \(\kappa=0\) 时任意负小目标已经反驳 (DS6)。设 \(\kappa>0\)。
令 \(c_n=1/n\)，\(n\ge2\)。由 \(\psi\) 在零处消失，可取
\[
0<\eta_n<\min\left\{\bar t,\frac{c_{n-1}-c_n}{3},\frac{c_n}{n}\right\},
\qquad \kappa\psi(\eta_n)<\frac{c_n}{n}.
\tag{DS7}
\]
取 \(y_n=c_n+\eta_n\)。它严格位于相邻两点 \(c_n,c_{n-1}\) 之间，
而且离 \(c_n\) 最近，所以
\[
y_n\notin A,\quad y_n\to0,\quad d(y_n,A)=\eta_n,\qquad
h(y_n)=y_n>c_n>\kappa\psi(\eta_n).
\tag{DS8}
\]
对所有充分大的 \(n\)，此点在 (DS6) 的目标窗口内，矛盾。\(\square\)

(DS6) 是本卡所称 UHREG 的明确版本；它失败不依赖名称约定。
更强的两变量不等式
\[
d(x,F^{-1}(y))\le\kappa\psi(d(y,F(x)))
\tag{DS9}
\]
若要求对零点附近**全部** \(x,y\) 成立，也在切片 \(x=0\) 被同一序列反驳。
特别地，每个正指数的两变量 Hölder metric regularity 都失败，
虽然 (DS3) 的固定零目标真残差规律全域锐线性。
此障碍专指每个**以零为参考的目标邻域**，不声称离散集外每个任意中心的邻域都失败。

<a id="ds-ppa"></a>
## DS-PPA-v1：完整近端纤维、真步残差和任意允许轨道

令 \(\tau=(1+\lambda)^{-1}\in(0,1)\)。由 \(p-u\in\lambda F(u)\)
逐一求出所有解：若 \(u\ne0\)，则 \(p=(1+\lambda)u\)；若 \(u=0\)，
则 \(p\in\lambda A\)。所以完整近端关系为
\[
J_{\lambda F}(p)=\{\tau p\}\cup
\begin{cases}
\{0\},&p\in\lambda A,\\
\varnothing,&p\notin\lambda A.
\end{cases}
\tag{DS10}
\]
第一项对全部 \(p\) 存在，故自然 Minty 输入域为整个 \(\mathbb R\)。
在 \(p=0\) 两项重合；在每个 \(p=\lambda/n\) 有两个不同输出。
\(\operatorname{Fix}J_{\lambda F}=\{0\}\)，且完整**最小步残差**严格等于
\[
r_J(p):=\inf_{u\in J_{\lambda F}(p)}|p-u|
=(1-\tau)|p|=\frac{\lambda}{1+\lambda}|p|.
\tag{DS11}
\]
因为对角输出给步长 \((1-\tau)|p|\)，附加的零输出只给较大步长 \(|p|\)。
因此完整近端 fixed-point EB 的精确全域线性模为
\((1+\lambda)/\lambda\)。这与原算子 (DS3) 的模 \(1\) 属于不同残差。

对任意 \(p_0\in\mathbb R\) 和任意合法选择序列
\[
p_{k+1}\in J_{\lambda F}(p_k)\quad(k\ge0),
\tag{DS12}
\]
每一步只能继续取 \(p_{k+1}=\tau p_k\)，或者在
\(p_k\in\lambda A\setminus\{0\}\) 时取 \(p_{k+1}=0\)，之后永久为零。
这些是全部路径，没有未枚举的远端输出。因此
\[
|p_k|\le\tau^k|p_0|,\qquad
\sum_{k=0}^{\infty}|p_{k+1}-p_k|=|p_0|,
\qquad p_k\to0.
\tag{DS13}
\]
第一式由每个输出都满足 \(|p_{k+1}|\le\tau|p_k|\) 归纳。
路径保号直至归零，所以每步有
\(|p_{k+1}-p_k|=|p_k|-|p_{k+1}|\)，望远镜求和给第二式。
始终选择对角输出是对所有初值都合法的路径，并在第一式对每个 \(k\) 取等；
故任意允许选择的统一最坏一步因子恰为 \(\tau\)。

全域覆盖、留在初始半径内、真步残差、有限长度和统一线性收敛在这里都对
**完整近端关系的每一条实际路径**成立，未把一次有利选择当作全部选择。

<a id="ds-rl"></a>
## DS-RL-v1：锐零锚反射与全对零分母碰撞同时存在

完整关系中任意图点 \((u,v)\) 与零锚 \((0,0)\) 都有
\[
|u-\lambda v|\le |u+\lambda v|.
\tag{DS14}
\]
在对角支它化为 \(|1-\lambda||u|\le(1+\lambda)|u|\)；在竖支
\((0,c)\) 两端均为 \(\lambda c\)。因此零锚线性反射最优常数全域为 \(1\)，
在任意包含原点的完整图邻域内仍为 \(1\)，因为 \(c=1/n\to0\)。
等价地，完整反射关系的每个值满足
\[
r\in (2J_{\lambda F}-I)(p)\quad\Longrightarrow\quad |r|\le|p|.
\tag{DS15}
\]

然而固定任意 \(\lambda>0\)，对 \(c_n=1/n\) 取两个完整图点
\[
(u_n,v_n)=(0,c_n),\qquad
(u'_n,v'_n)=\left(\frac{\lambda c_n}{1+\lambda},
                       \frac{\lambda c_n}{1+\lambda}\right).
\tag{DS16}
\]
两个图点均趋于 \((0,0)\)，Minty 输入完全相等：
\[
u_n+\lambda v_n=u'_n+\lambda v'_n=\lambda c_n.
\]
但反射输出差为
\[
\left|(u_n-\lambda v_n)-(u'_n-\lambda v'_n)\right|
=\frac{2\lambda c_n}{1+\lambda}>0.
\tag{DS17}
\]
所以在原点任何完整图邻域中，都不存在全对模
\[
|(u-\lambda v)-(u'-\lambda v')|
\le\omega(|(u+\lambda v)-(u'+\lambda v')|),\qquad\omega(0)=0.
\tag{DS18}
\]
尤其每个 \(L<\infty,\gamma>0\) 的完整图 Hölder–RL 均失败。
这个反例直接使用输入差等于零，不是仅证明某个指数不够大。

(DS3)、(DS10)–(DS13) 与 (DS17) 合在一起否定如下逆向推断：
“完整图闭、全域输入覆盖、真算子和真步残差均有线性 EB，且完整近端的每条选择路径
统一线性收敛并有有限长度，因此完整图必有全对 RL”。
它与全对 RL 加其他条件推出收敛的充分定理相容。
这里还有对**完整图**成立的锐零锚证书 (DS14)，但零锚不控制同输入的不同输出。

<a id="ds-quadratic"></a>
## DS-QUADRATIC-v1：局部与全域都只有普遍的负负参数区

定义全对二参数区域
\[
\Sigma(F)=\{(\mu,\rho):ab\ge\mu a^2+\rho b^2
\text{ 对全部完整图点对的差 }(a,b)\},
\tag{DS19}
\]
并令局部版本只测试任意固定的 \((0,0)\) 图邻域。两种版本都精确等于
\[
\Sigma(F)=\{(\mu,\rho):\mu<0,\rho<0,\mu\rho\ge1/4\}.
\tag{DS20}
\]

**必要性。** 跨支点 \((0,c),(x,x)\) 的差满足
\(a=-x,b=c-x\)，所以 \(b/a=1-c/x\)。对每个固定 \(t\ne1\)，
取 \(x=c/(1-t)\) 并令 \(c=1/n\to0\)，就在每个局部图邻域内实现斜率 \(t\)；
对角点对实现 \(t=1\)。于是 (DS19) 必须满足
\[
\rho t^2-t+\mu\le0\qquad\text{对所有 }t\in\mathbb R.
\tag{DS21}
\]
\(\rho\ge0\) 时不可能；\(\rho<0\) 时二次式最大值为
\(\mu-1/(4\rho)\)，故恰要求 \(\mu\le1/(4\rho)<0\)，等价于 (DS20)。

**充分性。** (DS20) 使 (DS21) 对全部实数成立，所以对所有 \(a\ne0,b\)
都有 (DS19)；\(a=0\) 时 \(0\ge\rho b^2\) 同样成立。这事实上是对任意实数差
\((a,b)\) 均有效的二次不等式，不额外揭示本图的几何。

两种单参数有符号下模都为 \(-\infty\)。沿同一跨支差，分别取
\(x=c^2\) 与 \(x=c-c^2\)，得到
\[
\frac{ab}{a^2}=1-\frac1c\longrightarrow-\infty,
\qquad
\frac{ab}{b^2}=1-\frac1c\longrightarrow-\infty.
\tag{DS22}
\]
所有这些图点都趋零，故不存在有限的局部 hypo- 或 cohypomonotonicity 下界。
边界 \(\mu\rho=1/4\) 已包含，不可误删。

<a id="ds-boundary"></a>
## 调用边界与自审

本对象把四类量词放在同一完整图上：

| 量词与残差 | 精确结论 |
| --- | --- |
| 固定目标零点，原算子真纤维残差 | 全域 \(d(x,S)=r_F(x)\)，锐线性模 \(1\) |
| 中心为零，全部逆像 / 最近逆像，右端 \(|y|\) | 两者锐线性模均为 \(1\) |
| 中心为零，最近逆像，右端 \(d(y,F(0))\) | 任意消失 gauge 的局部界均失败 |
| 完整近端最小步残差 | 全域锐线性模 \((1+\lambda)/\lambda\) |
| 完整近端任意允许路径 | 锐统一因子 \((1+\lambda)^{-1}\)，总长 \(|p_0|\) |
| 完整图对零点锚 | 锐反射线性常数 \(1\) |
| 完整图全部点对 | 任意 \(\omega(0)=0\) 的模均失败 |

本卡已检查 \(p=0\) 的重复输出、正离散输入的附加输出、所有负输入的唯一输出、
每个固定 \(\lambda>0\)、完整输出纤维和目标窗口的量词。
独立复核还检查了一般 gauge 序列的量词和二次参数区的边界。
无数值网格充当证明，无外部来源定理被静默导入；历史 GX-075 之外的卡片未据此裁决。
