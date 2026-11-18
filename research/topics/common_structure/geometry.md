# 图的投影几何：同一母对象、两种专化和全输出边界

最稳的公共母对象是**同一原图上、相对于指定参考纤维的逆投影模**。单调性在斜向 Minty 投影上是一个精确角度阈值，一般模误差界在残差投影上是零纤维的逆连续性。最近零锚 RL 也由斜投影的同一模表示。这是有标准次横截性来源的表示。两个投影方向、参考集和量词承载独立信息，无法从共同表示推出同时继承旧非线性 RLEB 与 Luke–Tam 的新充分性质。

独立于这个表示，**移动最近零锚的归一化割线极限精确检验线性 MSR**。固定基点图导数中“水平核等于零集切锥”仍不足以得到 MSR，甚至在连续半代数算子、全输入唯一完整近端、仿射非孤立零集下也失败。移动割线的同一数据还可用于检验仿射零集上的近端横向收缩，需要另核远端分支。

<a id="bridge-projection"></a>
## 1. 同一个图投影模及精确专化

设 \(E=\mathbb R^n\)，\(F:E\rightrightarrows E\) 闭图，\(\lambda>0\)，零集 \(S=F^{-1}(0)\ne\varnothing\)，定义
\[
G=\{(y,w):w\in\lambda F(y)\},\quad Z=S\times\{0\},\quad
\Pi_+(y,w)=(y+w)/\sqrt2,\quad \Pi_0(y,w)=w.
\]
图空间取欧氏积范数。物理输入为 \(x=y+w\)。对线性观测 \(\Pi\)、原图点 \(z\in G\) 和非空参考集 \(C\subseteq G\)，考虑同一距离畸变
\[
d(z,C)\le\chi(d(\Pi z,\Pi C)). \tag{P}
\]
当 \(C=G\cap\Pi^{-1}(b)\) 且 \(\Pi\Pi^*=I\)，右端模作用于图点到环境仿射纤维 \(\Pi^{-1}(b)\) 的距离。此时线性 (P) 是受限于第一集合 \(G\) 的次横截距离式。将参考集换成单点是带指定输出的逆稳定性，不能由非单点纤维的距离自动替代。文献对应为 Kruger–Luke–Thao [Propositions 1、3](https://arxiv.org/pdf/1611.04787#page=5)。第 3 命题用最大积范数。下面的平方恒等式和精确常数使用欧氏积范数。

**斜投影、所有单点锚、临界常数。** 对所有 \(z,z'\in G\) 取 \(C=\{z'\}\)，(P) 在 \(\Pi=\Pi_+,\chi(t)=\sqrt2t\) 时等价于 \(F\) 单调，因为
\[
2\|\Pi_+(z-z')\|^2-\|z-z'\|^2=2\langle y-y',w-w'\rangle .
\]
因此同一输入的两个完整图点必相等。若另有全输入 coverage \(E\subseteq (I+\lambda F)(E)\)，则 \(F\) 极大单调。证明是给任意与全图单调相关的 \((y,w)\) 在原图找同一输入的点 \((y',w')\)，有 \(\langle y-y',w-w'\rangle=-\|y-y'\|^2\ge0\)。反向全覆盖是 Minty 定理，见 Bauschke–Moffat–Wang [Fact 1.2](https://arxiv.org/pdf/1101.4688#page=3)。coverage 与角度条件独立。若只在方窗内检验，结论只覆盖该图块。全局传统次单调性可对切变后的图 \((y,w+\lambda\rho y)\) 执行相同测试，表示 \(F+\rho I\) 单调。

**斜投影、两点 RL 和最近零锚 RL。** 写 \(\Pi_-(y,w)=(y-w)/\sqrt2\)。正交分解给 \(\|z-z'\|^2=\|\Pi_+(z-z')\|^2+\|\Pi_-(z-z')\|^2\)。指定同一图块和两点量词，反射差分 \(\sqrt2\|\Pi_-(z-z')\|\le\omega(\sqrt2\|\Pi_+(z-z')\|)\) 等价于 (P) 使用单点锚和 \(\chi_+(t)=\sqrt{t^2+\omega(\sqrt2t)^2/2}\)。最近零锚版本对每个规定输入的每个允许输出取 \(z=(y,x-y)\) 和 \(C_x=P_S(x)\times\{0\}\)。所有 \(p\in P_S(x)\) 都有 \(\|\Pi_+(z-(p,0))\|=d(x,S)/\sqrt2\)，于是同一 \(\chi_+\) 下 (P) 恰等价于存在最近锚 \(p\) 使 \(\|2y-x-p\|\le\omega(d(x,S))\)。闭集欧氏投影的紧性保证最小值实现。这里 \(C_x\) 依赖输入，通常既不是 \(\Pi_+\) 的某一纤维，也不是固定单点。

**残差投影、整个零纤维、GMSR。** 取 \(\Pi=\Pi_0,C=Z\)，则
\[
d(z,Z)^2=d(y,S)^2+\|w\|^2,\qquad d(\Pi_0 z,\Pi_0 Z)=\|w\|.
\]
固定输出域 \(Y\) 和残差帽 \(\bar s\)，对全部 \((y,w)\in G\) 满足 \(y\in Y,\|w\|\le\lambda\bar s\) 实施 (P)，取 \(\chi_0(t)=\sqrt{t^2+\psi(t/\lambda)^2}\)。这恰等价于 \(d(y,S)\le\psi(r_F(y))\) 对每个 \(y\in Y\) 且 \(r_F(y)\le\bar s\) 成立。正向取完整纤维的最小范数图值，非空闭纤维在有限维有最小点。反向用 \(\psi\) 非减。不能只对已选中的图值使用 (P) 然后取完整纤维下确界。参数 \(\psi(s)=Ks\) 对应线性常数 \(\sqrt{1+(K/\lambda)^2}\)。点态图窗和通常真残差 MSR 的局部等价也见 Rockafellar [§1, (7)–(8)](https://serdica-stage.math.bas.bg/index.php/serdica/article/download/32/41/81#page=4)。

| 专化 | 观察方向 | 参考集 | 受检量词 |
| --- | --- | --- | --- |
| 传统单调性 / 两点 RL | \(\Pi_+\) | 任一图点的单点集 | 指定图块内的每一对图点 |
| RLEB 最近零锚 | \(\Pi_+\) | \(P_S(x)\times\{0\}\) | 每一允许输出，锚可依赖输出 |
| 通常 GMSR / MSR | \(\Pi_0\) | 全零纤维 \(Z\) | 指定输出域中每个纤维完整取残差，使用残差帽 |
| 极大单调 | \(\Pi_+\) | 单点 | 全图单调再加所有斜纤维均非空 |

两个方向没有自动传递。在 \(E=\mathbb R^2,S=\mathbb R\times\{0\},\lambda=1\)，\(F(a,b)=(0,b^3)\) 全局极大单调，斜投影覆盖全域，但 \(r_F/d=|b|^2\) 令任何局部线性 MSR 失效。\(F(a,b)=(0,-b/2)\) 全局有线性 MSR，完整 \(J(a,b)=(a,2b)\) 全域唯一，离开 \(S\) 的所有近端轨道发散。

若要求整条非紧零管的统一一般模，极大单调性甚至不给出零处连续的任意误差模。取 \(F=\partial f\)，其中 \(f(a,b)=b^2/(a+1)\) 在 \(a\ge0\) 时成立，其他位置取 \(+\infty\)。在定义域上 \(f=\sup_{c\in\mathbb R}(2bc-(a+1)c^2)\)，故 \(f\) 是闭凸函数，\(S=[0,\infty)\times\{0\}\)。对任意固定 \(b\ne0\) 和 \(a\to+\infty\)，真残差是 \(\|(-b^2/(a+1)^2,2b/(a+1))\|\to0\)，但 \(d((a,b),S)=|b|\)。可在任意给定正宽度的非紧整管内选取这样的高度。这个反例不涉及固定点的有界局部窗。

<a id="bridge-moving"></a>
## 2. 移动最近零锚割线及固定切锥的反例

任取 \(s_0\in S\)。对局部原图定义单位割线极限集
\[
\mathcal K(s_0)=\bigcap_{\delta>0}\overline{\left\{
\frac{(y-p,w)}{\sqrt{d(y,S)^2+\|w\|^2}}:
 (y,w)\in G,\ \|y-s_0\|+\|w\|<\delta,\quad
 p\in P_S(y),\ d(y,S)^2+\|w\|^2>0
\right\}} . \tag{K}
\]
若沿所有小窗都没有非零割线，则 \(\mathcal K(s_0)=\varnothing\)。单位割线随每个图点的最近输出零锚移动，依赖物理原图。第一分量记 \(u\)，第二分量记 \(v\)。

**精确判据。** \(F\) 在 \((s_0,0)\) 对完整原零集有线性 MSR，当且仅当 \(\mathcal K(s_0)\cap(E\times\{0\})=\varnothing\)。若 \(\mathcal K(s_0)\ne\varnothing\)，最优渐近 MSR 常数为
\[
\lambda\,\sup_{(u,v)\in\mathcal K(s_0)}\frac{\|u\|}{\|v\|},
\]
遇到水平单位方向时值为 \(+\infty\)。每个未归一化割线的横向范数为 \(d(y,S)\)、竖向范数为 \(\|w\|\)。有限维单位球的紧性使任何失控比值子列收敛到水平单位方向，反之该方向使比值无界。无水平极限方向时，紧性给出小图窗内竖向单位分量统一正下界，连续比值在该窗缩小时的极限上确界即上式。远离零的值不影响局部最优常数，因为 \(\|w\|\) 有正下界时 \(d(y,S)/\|w\|\le\|y-s_0\|/\|w\|\to0\)。若 \(\mathcal K(s_0)=\varnothing\)，某小图窗没有非零图割线，故渐近常数为零。该判据将模的局部极限紧化并保留可与其他方向联检的数据。

**固定基点的切锥相交等式不足。** 取 \(\lambda=1\)，
\[
F(a,b)=(0,g(a,b)),\qquad
g(a,b)=\operatorname{sgn}(b)(|b|-a^2)_+ + a^2b .
\]
它是连续半代数映射，\(S=\mathbb R\times\{0\}\)，且 \(F\) 在 \((0,0)\) 可微，导数为 \((h,k)\mapsto(0,k)\)。后一结论来自 \(|g(a,b)-b|\le a^2(1+|b|)\)。因此 \(DF((0,0)\mid0)^{-1}(0)=T_S(0)\)。然而对 \(a\to0,a\ne0,b=a^2/2\)，有 \(r_F(a,b)/d((a,b),S)=a^2\to0\)。相应移动锚始终为 \((a,0)\)，故 (K) 含水平单位极限。固定 \(a\) 时 \(b\mapsto b+g(a,b)\) 严格递增满射，所以完整近端全域唯一。正高度 \(b=a^2/2\) 的实际步比 \(d(y,S)/d(x,S)=1/(1+a^2)\to1\)，任意缩小窗口中均没有统一严格 A。固定切锥漏掉了切向趋零速度相对法向速度占优的点列。若 \(s_0\) 孤立，最近锚在小球内恒为 \(s_0\)，(K) 回收经典强次正则性图导数核判据，见 Cibulka–Dontchev–Kruger [Theorem 5.1](https://arxiv.org/pdf/1701.02078#page=14)。

**仿射零集的物理横向检验。** 设 \(S=s_0+L\)，\(N\) 是到 \(L^\perp\) 的正交投影。对 (K) 定义
\[
Q(u,v)=\|u+Nv\|^2-\|u\|^2 .
\]
若 \(Q>0\) 在 \(\mathcal K(s_0)\) 上处处成立，则存在 \(\mu>0\) 使一小图窗内每个原图点满足
\[
d(y+w,S)^2-d(y,S)^2\ge \mu\big(d(y,S)^2+\|w\|^2\big). \tag{T}
\]
理由是 \(u=(y-P_S(y))/\sqrt{d(y,S)^2+\|w\|^2}\)、仿射法投影公式及单位球紧性。若 \(\mathcal K(s_0)\) 为空，小图窗内全是零割线。在同一图窗，(T) 给出
\[
d(y,S)\le (1+\mu)^{-1/2}d(x,S),\qquad
\|x-y\|\le \mu^{-1/2}d(x,S).
\]
水平极限使 \(Q=0\)，故 (T) 蕴含线性 MSR。反之，若小图窗全部图点已满足 A 和线性输入步界，距离平方下降的正余量可同时支付右端两项，遂得某个 \(\mu>0\)，进而在 (K) 上 \(Q>0\)。这提供同一原图芽的几何检验，作为公理与输入版 A+B 的存在量词等价。应进一步从可独立验证的非光滑结构读出 \(\mathcal K(s_0)\)。输出相对步界等价于在一个小图窗的 (K) 上另排竖直极限方向 \((0,v)\)，不由 (T) 给出。

**所有输出、留域和远端根。** 若 \(U\) 为开集，对 \(x\in U_R=U\cap\{d(x,S)\le R\}\) 假设 \(J_{\lambda F}(x)\ne\varnothing\) 且所有完整输出都落在已证 (T) 的图窗，则每个输出满足上两估计。取 \(\kappa=(1+\mu)^{-1/2}\)。当 \(\mu^{-1/2}d(x^0,S)/(1-\kappa)<d(x^0,E\setminus U)\)，有限前缀三角估计让每步留在 \(U_R\)，继而每条完整政策有有限长度并收敛到 \(S\cap U\) 中一点，尾长至多 \(\mu^{-1/2}d(x^k,S)/(1-\kappa)\)。图芽只检验输出和值靠近 \(s_0,0\) 的图块。coverage 与全输出定位须分别核对。将 \(F(y)=y\) 的图在 \(y=1\) 额外添加 \(F(1)\supseteq[-1-\varepsilon,-1+\varepsilon]\) 即得闭图反例。原点图芽不变，\(\lambda=1\) 时所有 \(|x|\le\varepsilon\) 另有远端输出 \(1\)。

## 3. 完整多值实例和界的独立性

取 \(\lambda=1\)，\(F(a,b)=\{(0,b),(0,-3b)\}\)。这是两条线性分支的闭图，非孤立零集为横轴，完整近端在每个输入处恰有 \(J(a,b)=\{(a,b/2),(a,-b/2)\}\)。对任一原图点，尺度未归一化的 (T) 左端为 \(3b^2\)，右端在 \(\mu=3/10\) 时至多 \(3b^2\)。真残差为 \(|b|\)，全局最近锚 \(p=(a,0)\)。两支均可被选择，所有政策均为有限长度。\(F\) 非单调，甚至不存在有限的传统局部次单调常数。取 \((y_1,w_1)=((0,t+\varepsilon),(0,-3(t+\varepsilon)))\) 与 \((y_2,w_2)=((0,t),(0,t))\)（固定小 \(t>0\)，\(\varepsilon\downarrow0\)），内积与 \(\|y_1-y_2\|^2\) 的比为 \(-4t/\varepsilon-3\)。

取 \(F(a,b)=(0,\operatorname{sgn}(b)\sqrt{|b|})\)。它极大单调，原算子在零集不光滑。对 \(|b|\le1\)，同号给 \(d(x,S)^2-d(y,S)^2\ge\|w\|^2\ge(d(y,S)^2+\|w\|^2)/2\)，但 \(\|w\|/d(y,S)=|b|^{-1/2}\to\infty\)。这是 C310 现有一维障碍的非孤立零集直积。

## 4. 核对过的一手文献

| 结果位置 | 范围和重要边界 |
| --- | --- |
| [Chieu–Lee–Mordukhovich–Nghia, Thm. 3.2、3.5](https://arxiv.org/pdf/1501.00307#page=5) | Hilbert 闭图上，全局次单调性与全部图点正半定 Fréchet 余导数联合等价于极大单调。半局部变体另有凸定义域。余导数正半定是在全图验证的符号量。 |
| [Khanh–Khoa–Mordukhovich–Phat, Thm. 3.3](https://arxiv.org/pdf/2308.14193#page=6) | 对文中等价范数和对偶映射，局部极大单调等价于局部单调与 resolvent 连续单值图局部化。远端原图分支仍可能存在。 |
| [Gfrerer–Outrata, Def. 2.5、Thm. 2.6](https://library.utia.cas.cz/separaty/2016/MTR/outrata-0467536.pdf#page=6) | \(\forall u\ne0: [0\in D^*F((s_0,0);(u,0))(v^*)\Rightarrow v^*=0]\) 等价于对小 \(C^1\) 扰动的稳健次正则，因此充分保证通常 MSR。普通 MSR 可无此性质，例如 \(F(a,b)=(0,b)\) 有 MSR，加入任意小 \(C^1\) 扰动 \(h(a,b)=(\varepsilon a^3,0)\) 后在原点没有 MSR。 |
| [Dontchev–Lewis–Rockafellar, §1、Thm. 1.2](https://sites.math.washington.edu/~rtr/papers/rtr180-RadiusMetricReg.pdf#page=3)；[Rockafellar, (7)–(10)、Thm. 1–2](https://serdica-stage.math.bas.bg/index.php/serdica/article/download/32/41/81#page=4) | 普通正则性保所有邻近右端，次正则固定右端。极大单调中正则性推出强正则性。强次正则性的几乎处处结论需要值域有内部，不能用于任意预指定右端。 |
| [Rockafellar, *Variational Convexity and Prox-Regularity*, Thm. 1–2](https://sites.math.washington.edu/~rtr/papers/rtr268-VariProx.pdf#page=3) | 变分 \(s\)-凸、该级统一二次增长与特定函数值截断的局部 \(s\)-极大单调共享同一函数结构。只要求 \(f\)-attentive 局部 \(s\)-单调的分支还需基准次梯度正规性。该支撑机制限制于次梯度，增长对指定图点统一。 |
| [Aragón Artacho–Geoffroy, Thm. 2.1](https://arxiv.org/pdf/1303.3654#page=4)；[Drusvyatskiy–Lewis, Thm. 3.3–3.4](https://arxiv.org/pdf/1602.06661) | 凸次微分的 MSR 等价于到同一整个逆纤维的局部二次增长，允许非孤立解。凸性本身不提供正增长常数。 |
| [Bauschke–Moursi–Wang, Prop. 3.6–3.7](https://cmps-people.ok.ubc.ca/bauschke/Research/127.pdf#page=10) | 全点对 comonotonicity 与 conically nonexpansive resolvent 对应，最大性另加全域。定理未附带水平零纤维的 MSR。 |
| [Leventhal, Thm. 3.1](https://arxiv.org/pdf/0902.4200#page=6)；[Luke–Tam, Assum. 2、Thm. 2、(28)–(29)](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863) | 前者是极大单调加 MSR 的标准到零集线性因子。后者合用 submonotonicity 与 MSR，对 \(J_{\lambda F}(x_n)\cap B_\delta(\bar x)\) 的所有选择证明点级线性收敛。删去球内截断需证明全原图定位。 |

## 5. 查重及未闭义务

- C285 的联合包络已使用 \(\|y-p\|^2+\|w\|^2\le(d(x,S)^2+\omega(d(x,S))^2)/2\)，并保留更细的三角可行域。将预算与原 \(\psi\) 联合优化，或恢复 Leventhal 因子，属于旧数据优化。
- C277 已给同锚有限原图约束的联合编译与全部政策长度后端。把 (T) 录入该语法或复用有限前缀推理没有建立新的幂次兼容。移动割线极限是一个非光滑判据，对一般原图的有限有效计算仍待证明。
- C323 已给光滑单值原算子和光滑零流形的横向最小奇异值条件。这里的仿射测试回收其仿射切片，增量为非光滑多值图芽的极限刻画及反例。对 C288 的曲目标或类级锐门未得到进一步优化。
- C318 已推出全输入管上全部输出的 A 会强制缩管真残差线性 MSR，任何恢复统一 A 的候选均受该门约束。旧非线性 RLEB 的提案还须处理超线性位移模、非孤立非仿射零集和远端分支。
- 投影表示、移动割线判据、原图和近端反例已直接证明，待项目独立接收。一个独立且严格扩大两套基线的普通 PPA 共同 M 仍是 open。值得继续测试原生非光滑图结构能否给出移动割线集或方向化非线性模，同时保留原 RLEB 标量参数无法恢复的信息，保持完整图分支。
