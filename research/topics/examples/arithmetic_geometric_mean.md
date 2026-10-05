# AGM：完整逆图、几何共同尾与严格兼容障碍

本页重构 SS1 `research_note.md` §6.2–6.3 的**同一个**算术–几何平均对象，
而非把正初值轨道与轴上轨道拼成一个速率命题。三个规范单元是
`AGM-GRAPH`、`AGM-SELECTION` 和 `AGM-COMPATIBILITY`。正文证明已完成，
直接证明范围为 `derived-checked`，空白接收范围另记；外部文献事实与本页推导分列在末节。
这些单元不判断解选择稿的全球优先权。

<a id="agm-object"></a>
## 完整对象与约定

空间为欧氏 \(H=\mathbb R^2\)，步长固定为 \(\lambda=1\)。记
\[
P=[0,\infty)^2,\qquad
D=\{(s,t):s\ge t\ge0\},\qquad
G(a,b)=\left(\frac{a+b}{2},\sqrt{ab}\right)\quad((a,b)\in P).
\tag{AGM1}
\]
根号取非负实根。对 \(u=(s,t)\in D\)，令
\[
d=\sqrt{s^2-t^2},\qquad \ell=s-t,
\]
并定义**完整**关系
\[
F(s,t)=\{(d,\ell-d),(-d,\ell+d)\},\qquad
F(u)=\varnothing\quad(u\notin D).
\tag{AGM2}
\]
映射 \(G\) 的图由 \(a,b\ge0\)、\(2u_1=a+b\)、\(u_2\ge0\)、\(u_2^2=ab\)
描述，因而 \(G\) 本身半代数。
集合记号在 \(d=0\) 时只保留一个元素。真残差和完整近端为
\[
r_F(u)=\inf_{v\in F(u)}\|v\|,\qquad
J_F(p)=\{u:p-u\in F(u)\},
\tag{AGM3}
\]
空纤维的残差为 \(+\infty\)。本页所有有限残差结论均明确在 \(D\) 上；
不使用 \(0\cdot\infty\) 的约定。

来源的 \(G\) 和 \(F_{\rm AGM}\) 逐项就是 (AGM1)–(AGM2)。这里没有改变坐标、
增加分支或作有限维提升。输入 \(P\) 与输出 \(D\) 是两个不同的集合。

<a id="agm-graph"></a>
## AGM-GRAPH：完整近端、全部残差与锐线性 EB

**精确结论。** (AGM2) 的图闭且半代数，每个非空纤维至多二值。其完整零集、
自然输入域和全部近端纤维为
\[
S=F^{-1}(0)=\{(h,h):h\ge0\},\qquad
\operatorname{ran}(I+F)=P,\qquad
J_F(p)=\{G(p)\}\quad(p\in P),
\tag{AGM4}
\]
而 \(J_F(p)=\varnothing\) 对 \(p\notin P\)。在 \(u=(s,t)\in D\) 上，
\[
r_F(u)=\sqrt{d^2+(d-\ell)^2},\qquad
\operatorname{dist}(u,S)=\frac \ell{\sqrt2}
\le\frac{r_F(u)}{\sqrt2}.
\tag{AGM5}
\]
最后的全域线性 EB 系数 \(1/\sqrt2\) 最优，并在每个 \((h,0)\)、\(h>0\) 取等。

**证明。** 给定输出 \((s,t)\)，方程 \(G(x,y)=(s,t)\) 等价于
\(x+y=2s\)、\(xy=t^2\)、\(x,y\ge0\)。因此全部逆点恰为
\[
G^{-1}(s,t)=\{(s+d,s-d),(s-d,s+d)\}\quad((s,t)\in D),
\tag{AGM6}
\]
域外为空。减去 \((s,t)\) 就得到 (AGM2)，故作为**关系恒等式**，
\(F=G^{-1}-I\)。对任何 \(p,u\)，
\[
p-u\in F(u)\iff p\in G^{-1}(u)\iff p\in P\text{ 且 }u=G(p).
\]
这给出 (AGM4) 的全部纤维，包含轴和原点；不能把它扩大为 \(\mathbb R^2\) 的满输入覆盖。

一般的编码事实也不需要单调性。对非空输入集 \(Q\subset H\) 上的单值
\(T:Q\to H\)，图变换 \((p,u)\mapsto(u,p-u)\) 是 \(H\times H\) 的可逆线性变换，
逆为 \((u,v)\mapsto(u+v,u)\)。它把 \(\operatorname{gra}T\) 变为
\(\operatorname{gra}(T^{-1}-I)\)，所以保持闭图，并以线性代入保持半代数性。
对每个固定 \(u\)，平移 \(p\mapsto p-u\) 还是 \(T^{-1}(u)\) 到完整图值的双射，
所以值数相等，包括空集和无穷纤维。这只是编码恒等式，不附送任何 RL 或 EB 常数。

函数 \(d\) 在闭集 \(D\) 上连续，图由两个连续分支的图组成，故闭。
每个分支可用 \(d\ge0,d^2=s^2-t^2\) 及线性等式表示，故半代数。
当 \(s=t\) 时两个值均为零；当 \(s>t\) 时 \(d>0\)，任一值均非零。
这证明零集的精确身份。

因 \(\ell,d\ge0\)，\((\ell-d)^2\le(\ell+d)^2\)，所以第一支给完整纤维的最小范数。
又 \(d^2=(s-t)(s+t)\ge(s-t)^2=\ell^2\)。到非负对角线的最近点为
\(((s+t)/2,(s+t)/2)\)，从而 (AGM5) 成立。若 \((s,t)=(h,0)\)，
则 \(\ell=d=h\)、\(r_F(h,0)=h\)、\(\operatorname{dist}((h,0),S)=h/\sqrt2\)，
给出锐性。这是完整 \(F\) 的真残差，不是某一选中分支的步残差。

<a id="agm-selection"></a>
## AGM-SELECTION：半阶单步、共同几何尾与坏极限选择

固定 \(R>0\)，取共同输入域 \(W_R=[0,R]^2\)。映射 \(G\) 把 \(W_R\) 映入自身。
对每个 \(p\in W_R\)，全部完整 PPA 路径都是唯一的 \(G^np\)，有极限
\[
\Pi(p)=(M(p),M(p))\in S,
\qquad
\|G^np-\Pi(p)\|\le |p_1-p_2|2^{-n}\le R2^{-n}
\quad(n\ge0).
\tag{AGM7}
\]
\(\Pi\) 是 \(W_R\) 到 \(S\cap W_R\) 的连续回缩。
在同一域的全部输入对上，若 \(\delta=\|p-q\|\)，则
\[
\|Gp-Gq\|\le H_R\sqrt\delta,
\qquad H_R=\sqrt{3R/\sqrt2}.
\tag{AGM8}
\]
这是一个显式安全常数，不声明有限 \(R\) 的最优系数。
对每个 \(0<c<R\)，\(\Pi\) 在 \((c,0)\) 处没有任何正阶 Hölder 模；
其在该点任一相对邻域的限制也不半代数。

### 共同尾与半阶单步

先取 \(a_0\ge b_0\ge0\)。由算术–几何平均不等式，
\(a_n\downarrow\)、\(b_n\uparrow\)，且所有项在 \([b_0,a_0]\) 内。
差 \(d_n=a_n-b_n\) 满足无零分母恒等式
\[
d_{n+1}=\frac12(\sqrt{a_n}-\sqrt{b_n})^2\le\frac12d_n.
\tag{AGM9}
\]
因此两序列有同一个极限 \(M\in[b_n,a_n]\)。对任意 \(m\in[b_n,a_n]\)，
\((a_n-m)^2+(b_n-m)^2\le d_n^2\)，所以 (AGM7) 成立。
无序初值交换坐标后第一步和全部后续步均相同，初始点到极限的距离仍
不超过 \(|a_0-b_0|\)，故结论覆盖整个 \(W_R\)。原点也在证明范围内。
各 \(G^n\) 连续且共同尾趋零，故 \(\Pi\) 连续；对角线上 \(G=I\)，故是回缩。

对 \(p=(a,b),q=(a',b')\in W_R\)，
\[
\left|\frac{a+b-a'-b'}2\right|^2\le\frac{\delta^2}2,
\quad
|\sqrt{ab}-\sqrt{a'b'}|^2\le |ab-a'b'|
\le\sqrt2 R\delta.
\]
因为 \(\delta\le\sqrt2R\)，合并即得 (AGM8)。这里 \(R\) 是输入位置的有界窗，
不是仅对输入对距设上限；在整个无界 \(P\) 上不能沿用同一 \(H_R\)。

### 直接递推证明对数坏模

令 \(m(\varepsilon)=M(1,\varepsilon)\)，\(0<\varepsilon\le e^{-1}\)，
并记 \(T=\log(1/\varepsilon)\ge1\)。正初值使所有 \(a_n,b_n\) 正。
设 \(z_n=\log(a_n/b_n)\)，则
\[
z_{n+1}=\log\cosh(z_n/2),\qquad
2^{-n}T-2\log2\le z_n\le2^{-n}T,
\tag{AGM10}
\]
因为 \(x-\log2\le\log\cosh x\le x\) 对 \(x\ge0\) 成立。
取 \(N=\lfloor\log_2 T\rfloor\)。此时 \(z_N<2\)，且
\[
a_N=2^{-N}\prod_{k=0}^{N-1}(1+e^{-z_k})\ge2^{-N}\ge1/T.
\]
故 \(m(\varepsilon)\ge b_N=a_Ne^{-z_N}\ge e^{-2}/T\)。另一方面，
以 \(j=N-k\) 重编号并使用 (AGM10)，
\[
\sum_{k=0}^{N-1}e^{-z_k}
\le4\sum_{j=1}^{\infty}e^{-2^j}
\le4\sum_{j=1}^{\infty}e^{-2j}=
\frac4{e^2-1}.
\]
于是 \(\log(1+x)\le x\) 给出
\[
\frac{e^{-2}}{T}\le m(\varepsilon)
\le\frac{2\exp(4/(e^2-1))}{T}.
\tag{AGM11}
\]
空乘积 \(N=0\) 也符合这些界。这个两侧阶估计只用 AGM 递推，没有导入椭圆积分或
半代数增长定理。尤其 \(m(\varepsilon)\to0=M(1,0)\)。

同次性 \(G(cp)=cG(p)\) 给 \(M(c,c\varepsilon)=c\,m(\varepsilon)\)。
对 \(p_0=(c,0),p_\varepsilon=(c,c\varepsilon)\)，初值距为 \(c\varepsilon\)，而
\[
\|\Pi(p_\varepsilon)-\Pi(p_0)\|
=\sqrt2c\,m(\varepsilon)\asymp\frac c{\log(1/\varepsilon)}.
\tag{AGM12}
\]
任意 \(\alpha>0\) 下，(AGM12) 除以 \((c\varepsilon)^\alpha\) 趋于无穷，
证明指定参考点的非任意 Hölder 性。取 \(c<R\) 保证这些点全在同一 \(W_R\)。

非半代数性也可直接证明。若 \(m\) 的一个 \((0,\varepsilon_0)\) 图段半代数，
用有限个非零多项式的符号条件描述该图。在任何图点，至少一个描述多项式为零：
否则所有符号在一个开球上不变，图便含有开球，违反它是函数图。
取 \(Q(x,y)\) 为全部有限描述多项式的乘积。因各因子非零，多项式环无零因子，
故 \(Q\ne0\)；每个图点至少有一因子为零，故 \(Q\) 在整个图段消失。写
\(Q(x,y)=\sum_{i=i_0}^I x^i q_i(y)\)，其中 \(q_{i_0}\ne0\)。
设 \(j\ge0\) 是 \(q_{i_0}\) 在零处的消失阶。由 (AGM11) 及 \(m\to0\)，
\(|q_{i_0}(m(e^{-T}))|\ge C T^{-j}\) 对充分大 \(T\) 成立；其它系数保持有界。
而所有 \(i>i_0\) 的项在除以 \(e^{-i_0T}\) 后均为 \(O(e^{-T})\)。
它们不能抵消这个至少为 \(C T^{-j}\) 的首项，矛盾。
若 \(\Pi\) 在 \((c,0)\) 的一个相对邻域半代数，把其图沿
\((c,c\varepsilon)\) 和对角输出作线性代入就会得到上述半代数图段，故也矛盾。

### 可选的精确渐近常数：一手公式与本页积分估计

Brent 1976 的作者站原文，印刷页 245–246、(4.16)–(4.18)，对
\(a_0=1,b_0=\cos\varphi>0\) 的 AGM 给出
\(M(1,\cos\varphi)=\pi/[2F(\varphi)]\)，其中
\(F(\varphi)=\int_0^{\pi/2}(1-\sin^2\varphi\sin^2\theta)^{-1/2}\,d\theta\)。
取 \(\cos\varphi=\varepsilon\)，得到
\[
m(\varepsilon)=\frac\pi{2K_\varepsilon},\qquad
K_\varepsilon=\int_0^{\pi/2}
\frac{d\theta}{\sqrt{\cos^2\theta+\varepsilon^2\sin^2\theta}}.
\tag{AGM13}
\]
这是唯一外部数学导入；正参数条件由 \(0<\varepsilon<1\) 满足。
出处为 [Brent 作者站 PDF](https://maths-people.anu.edu.au/~brent/pd/rpb034.pdf)，
[DOI](https://doi.org/10.1145/321941.321944)。以下渐近为本页推导。

作 \(x=\cot\theta\) 代换，
\[
K_\varepsilon=\int_0^\infty
\frac{dx}{\sqrt{(1+x^2)(x^2+\varepsilon^2)}}.
\]
\((0,\varepsilon)\) 与 \((1,\infty)\) 两段的积分各不超过 1。
对 \(\varepsilon\le x\le1\)，用
\(1-(1+u)^{-1/2}(1+v)^{-1/2}\le(u+v)/2\)，得
\[
0\le\frac1x-
\frac1{\sqrt{(1+x^2)(x^2+\varepsilon^2)}}
\le\frac x2+\frac{\varepsilon^2}{2x^3}.
\]
右边积分不超过 \(1/2\)。因此 \(K_\varepsilon=\log(1/\varepsilon)+O(1)\)，
与 (AGM13) 合取后有
\[
m(\varepsilon)\sim\frac\pi{2\log(1/\varepsilon)}.
\tag{AGM14}
\]
没有用未取得的 Cox 原页支持此系数；去掉 (AGM13)–(AGM14) 后，
前面的完整对象、共同尾、坏模和非半代数证明仍自足。

### 正初值 Q-二次与坏参考轴的速率分别量化

若固定 \(a_0\ge b_0>0\)，由 (AGM9) 还可写
\[
d_{n+1}=\frac{d_n^2}{2(\sqrt{a_n}+\sqrt{b_n})^2}
\le\frac{d_n^2}{8b_0}.
\]
记实际点误差 \(e_n=\|(a_n,b_n)-(M,M)\|\)，则
\(d_n/\sqrt2\le e_n\le d_n\)，故
\[
e_{n+1}\le\frac{e_n^2}{4b_0}.
\tag{AGM15}
\]
系数依赖固定正初值的 \(b_0\)，在 \(b_0\downarrow0\) 时不统一。
对坏参考点 \((c,0)\)，全部轨道和误差恰为
\[
G^n(c,0)=(c2^{-n},0),\qquad e_n=c2^{-n},
\qquad e_{n+1}/e_n^2=2^{n-1}/c\longrightarrow\infty.
\tag{AGM16}
\]
任何包含这个点的初值集合，都不存在共同 \(A e^{-b\nu^n}\) 点尾
（\(A,b>0,\nu>1\)）。所以正初值的 (AGM15) 不能授给 (AGM12) 的轴上参考轨道。

<a id="agm-compatibility"></a>
## AGM-COMPATIBILITY：同一完整编码不满足严格 RLEB 兼容

固定同一 \(R>0,W_R\)。完整图在该输入窗对应的 Cayley 反射为
\[
C(p)=2G(p)-p,\qquad C(a,b)=(b,2\sqrt{ab}-b).
\tag{AGM17}
\]
任取 \(0<c<R\)，以及 \(0<\delta\le\min\{c,R\}\)。同窗输入对
\(p=(c,\delta),q=(c,0)\) 给
\[
\|p-q\|=\delta,
\qquad
\|C(p)-C(q)\|
=\sqrt{\delta^2+(2\sqrt{c\delta}-\delta)^2}
\ge\sqrt{c\delta}.
\tag{AGM18}
\]
因 \(\delta\le c\)，最后一个不等式成立。
所以任何覆盖该窗**全部图点对**的模 \(\omega\) 都必须满足
\(\omega(\delta)\ge\sqrt{c\delta}\)。特别地，最大可用 Hölder 指数至多 \(1/2\)；
由 (AGM8) 和 \(C=2G-I\)，指数 \(1/2\) 确实可用，安全系数为
\(2H_R+\sqrt{\sqrt2R}\)。

令 \(\psi:[0,\eta)\to[0,\infty)\) 非减，并在此窗的全部实际输出上提供真残差 EB。
因为 \((h,0)=G(2h,0)\) 对 \(0\le h\le R/2\)，(AGM5) 强制
\[
\psi(h)\ge h/\sqrt2
\quad\left(0<h<\min\{\eta,R/2\}\right).
\tag{AGM19}
\]
对任何充分小的 \(\delta>0\)，若兼容式的 gauge 求值
\((\delta+\omega(\delta))/2\) 在定义域内，设
\(h_\delta=\sqrt{c\delta}/2\)。它趋零，且由 (AGM18) 不超过该求值。
非减性与 (AGM19) 因而给出
\[
\frac{\psi((\delta+\omega(\delta))/2)}\delta
\ge\frac{\psi(h_\delta)}\delta
\ge\frac{\sqrt c}{2\sqrt2\sqrt\delta}\longrightarrow\infty.
\tag{AGM20}
\]
故不存在 \(\kappa<1\) 和一个正半径，使该完整直接编码在此工作窗满足
\[
\psi((\delta+\omega(\delta))/2)\le\kappa\delta
\quad\text{对每个足够小的 }\delta>0.
\tag{AGM21}
\]
若求值越出 \([0,\eta)\)，它本来就不是可用的兼容证书。
该否定甚至无需先假定 \(\omega(\delta)\to0\)；只用同窗全对界、真实输出 EB、
非减 gauge 及求值有定义。

这是一条同对象障碍：闭半代数完整图、唯一完整近端、真线性 EB、半阶全对 RL、
共同几何点尾可以同时成立，严格兼容仍失败。它不排除 AGM 的换变量、提升或其它新关系，
也不否定不含坏轴的另一工作窗；这些改动均须重新定义对象和验证全部纤维。

<a id="agm-source"></a>
## 来源逐单元去向与文献边界

来源为 SS1 修订 ZIP 的 `research_note.md`，成员 SHA-256：
`91ad4b0948a21443fc557b5ea579e692650399504e735223d72347ba86bea1b8`。
原件定位：
[solution_selection_revised_v1_delivery.zip](../../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)
内 `research_note.md`。哈希只识别来源版本，不赋予数学状态。

| 原件范围 | 独立断言 | 本页去向及证据 |
| --- | --- | --- |
| 669–677 | 完整 AGM 定义、统一几何尾和轴 | (AGM1)、(AGM7)、(AGM9)、(AGM16)，直接证明全部边界 |
| 679–684 | 有界单步半阶、极限对数坏模和非半代数 | (AGM8)、(AGM10)–(AGM12) 及多项式证明；这些不依赖外部引文 |
| 679–682、751 | Brent 的 AGM—椭圆积分关系 | (AGM13) 的明确外部接口；作者站原文印刷页 245–246 已核；(AGM14) 的积分渐近在本页证明 |
| 679–682、752 | Cox Theorem 1.1 和原刊版本 | 官方分章原刊§1 pp.276–283、Th1.1 p.278及证明现已核，条件正实数a≥b>0；本页闭轴/坏模仍由自证，不能将正实数定理外推到轴 |
| 684 | 绝对值延拓到全欧氏输入域 | 若只谈连续半代数单步、共同尾和坏选择，可定义 \(\widetilde G(x,y)=G(|x|,|y|)\)：第一步后在 \(P\)，每个有界输入窗继承相应常数与尾。它对应的 \(\widetilde G^{-1}-I\) 是另一完整关系，不是 (AGM2)；不授予其 RLEB |
| 686 | 正初值 Q-二次与坏参考轴不统一 | (AGM15)–(AGM16)；真实点误差分别量化，不能拼接 |
| 688–690、753 | 逆图 resolvent 编码的标准身份 | BMW 的 arXiv:1902.09827v1，PDF 标明 2019-02-26，Fact 2.1、PDF pp.3–4：非空 \(D\subset H\)、单值 \(T:D\to H\)、\(A=T^{-1}-I\) 给 \(J_A=T\)。本页 (AGM6) 已直接证明同一身份；不需要单调或全域假设 |
| 692–701 | 至多二值完整编码、真残差及严格兼容失败 | (AGM2)–(AGM6)、(AGM17)–(AGM21)，完整直接证明；保留所有提升/改造未被排除的范围 |

BMW 一手全文为 [arXiv PDF](https://arxiv.org/pdf/1902.09827)，
对应书目为 [DOI](https://doi.org/10.1007/s10107-020-01500-6)。本页只核上述恒等式，
不把它的单调性/极大单调性等价条件套给 AGM。
Cox 原刊目录为 [E-Periodica](https://www.e-periodica.ch/digbib/view?lang=en&pid=ens-001%3A1984%3A30%3A%3A436)，
指定Th1.1/§1的一手定位及正数门在[LIT-COX](../../LITERATURE.md#lit-cox-1984)；未声称全56页逐命题审结。
访问与核对日期为 2026-10-05；未保存、追加或改写历史原件。
