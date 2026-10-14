# 普通 PPA 的联合原图证书：可计算编译、全部政策与长度等级

日期：2026-10-14。**闭合单元状态：derived-checked；开放题保持 open**。本文固定原算子、步长、完整零集、真实残差和完整近端关系，本轮正文经独立实际全文冷审后登记；不改主稿、摘要或正文编号。已读 `AGENTS.md`、`RESEARCH_PROTOCOL.md`、仓库 `academic-writing-skills` 的 mathematics / mathematical-exposition、C249/C250、C208–C214、C221、C275，以及本日 submonotonicity 的 GU3、双范数盲区和 semimonotone / weak-Minty 审查。正文是自足规范证明；外部优先权未认证。

**本次实质。** 同一输出的方向、分支和真实残差约束先组成有限维联合证书，再编译为距离—物理步长关系。距离上界与步长上界可以作为旧式后端，也可以保持两者的关联，直接认证长度势。JP7 给出完整多值原算子：**任何独立的一步距离/步长最坏包络都不能满足尾和门，而联合证书给出精确总长。** JP8 再证明：精确的一步距离—步长关系仍可能丢失跨步方向，甚至不能认证一个两步终止的完整 PPA；JP9 保留有限个原生特征状态修复这个反例。这严格区分信息结构；望远镜/Caristi 原理本身不是新结果，非几何迭代也已由 C208/C221 覆盖。

<a id="ujc-object"></a>
## JP1-v1：冻结对象与证书语法

令 $X=\mathbb R^n$，$F:X\rightrightarrows X$，$\lambda>0$ 固定，

\[
S=\operatorname{zer}F\ne\varnothing\quad\hbox{闭},\qquad
J=(I+\lambda F)^{-1},\qquad
r_F(y)=\inf_{f\in F(y)}\|f\|.
\tag{JP1}
\]

空纤维残差为 $+\infty$。$U\subset X$ 开，$R>0$，$U_R=\{x\in U:d(x,S)\le R\}$。独立要求 **完整覆盖** $J(x)\ne\varnothing$ 对所有 $x\in U_R$ 成立。以下所有证书必须对每个 $x\in U_R$ 的**每个** $y\in J(x)$ 成立；不能只认证一支。输出认证在证明留域之前成立，不预设 $y\in U$。

对一个完整转移，选取一个最近锚 $p\in P_S(x)$，定义

\[
a=y-p,\quad b=\lambda f=x-y,\quad f\in F(y),\quad
t=d(x,S),\quad q=d(y,S),\quad s=\|b\|,\quad r=r_F(y).
\tag{JP2}
\]

同一个 $p$ 要同时支持所用的全部证书。不同条件各自存在一个最近锚，不能直接合取。基本关系是

\[
\|a+b\|^2=t^2,\qquad q^2\le\|a\|^2,
\qquad 0\le r\le s/\lambda.
\tag{JP3}
\]

最后一式只有此方向；$r$ 不等于选中图值的范数。

### 有限二次提升与保留的原图数据

置 $z=(a,b)\in\mathbb R^{2n}$，记录

\[
Z=zz^T=
\begin{pmatrix}Z_{aa}&Z_{ab}\\Z_{ab}^T&Z_{bb}\end{pmatrix}.
\tag{JP4}
\]

在一个**预先明定的有限证书表**中，容许：

1. 关于 $a,b$ 的二次等式/不等式，用 $\operatorname{tr}(QZ)$ 线性记录；例如原图 semimonotonicity、反射界、投影相等式、正共线条件。
2. 关于 $t,q,r,s$ 及这些二次特征的明定多项式/幂/给定模约束；若声称有限算法可判定，则系数须可计算且数据须有半代数表示。一般任意模仅有解析证书，不声称自动求解。
3. 有限分支标签 $\ell\in\{1,\ldots,L\}$。每个实际转移必须被至少一张表覆盖；同一个标签内全部约束合取，不把一支的上界和另一支的下界任意重配。
4. 目标几何的独立约束。对一般闭 $S$，默认仅用 $q^2\le\operatorname{tr}Z_{aa}$；若 $S=p_0+\ker N$ 是仿射集，$N$ 为其正交法投影，则可合法加入

\[
q^2=\operatorname{tr}(NZ_{aa}),\qquad
\|(I-N)(a+b)\|^2=0.
\tag{JP5}
\]

这些表须从原 $F,S$ 认证，不能把期望结论 $q\le\kappa t$ 或已知轨道收敛本身当“原图数据”。允许的源与参数字典在 JP5，两个完整模型在 JP6–JP7。原图验证本身一般仍是分析工作，编译器不替代这项工作。

实际 $Z$ 为秩至多一的半正定矩阵。有两个清楚分开的计算等级：

- **安全二次外松弛**：只保留 $Z\succeq0$；约束在平方变量 $q^2,r^2$ 中为仿射时，平方距离/步长上界是有限 SDP 的上界问题。
- **保秩半代数版本**：另外保留 $\operatorname{rank}Z\le1$（所有二阶子式为零）以及所需多项式关系。对有理/实代数系数、有限分支和半代数窗，固定实代数 $t$ 的有限上界与全区间多项式证书可由实闭域量词消去判定。此处的“可计算”不是声称实用复杂度，也不是把浮点求解器结果当证明。

安全外松弛可能较松，甚至无界；只要没有封闭的上界证书，就不通过该项测试。一般不声称外松弛值等于原 $F$ 的最坏输出，更不声称它是全部原算子的锐常数。PSD 上界可用精确对偶乘子及矩阵半正定性核验；半代数结论需解析消元、精确算术或经认证的区间论证。

## JP2-v1：先闭真实残差评价窗，再形成联合关系

由基本关系和已认证的原图/几何表构造有限并集 $\mathcal C_0(t)$。其中明确包含

\[
\begin{aligned}
&q,r,s\ge0,\quad Z\succeq0,\quad
\operatorname{tr}(Z_{aa}+2Z_{ab}+Z_{bb})=t^2,\\
&s^2=\operatorname{tr}Z_{bb},\quad
q^2\le\operatorname{tr}Z_{aa},\quad
\lambda^2r^2\le s^2.
\end{aligned}
\tag{JP6}
\]

每个实际转移的 $(q,s,r,Z)$ 属于 $\mathcal C_0(t)$。若另有真实误差界

\[
q\le\psi(r_F(y))\quad
\text{对全部实际输出 $y$、在 $r_F(y)\le\bar r$ 时成立},
\tag{JP7}
\]

则须**先**从 $\mathcal C_0$ 或另一项原图证书证明

\[
\sup_{0\le t\le R}\sup\{r:(q,s,r,Z)\in\mathcal C_0(t)\}
\le\bar r.
\tag{JP8}
\]

较粗而方便的充分门是 $\sup s/\lambda\le\bar r$；若原图提供 $r$ 与方向特征的准确关系，可以直接证明真实 $r$ 的小窗，保留相应优势。不能先用 JP7 排除大残差再反过来证明 JP8。若完全不调用局部 EB，JP8 不必另设。

现在才将 JP7、同窗真实残差下界 $g(q)\le r$ 等合法条件加入，得到 $\mathcal C(t)$，并投影为

\[
\mathcal E(t)=\{(q,s):\exists r,Z,\ell\ (q,s,r,Z)\in\mathcal C(t)\}.
\tag{JP9}
\]

必要时取闭外包络，但必须重新核其有界性和零端点。定义

\[
Q(t)=\sup\{q:(q,s)\in\mathcal E(t)\},\qquad
B(t)=\sup\{s:(q,s)\in\mathcal E(t)\}.
\tag{JP10}
\]

空集上界按零约定，仅用于没有实际输入的标量半径；这不产生 coverage。

**编译结论。** 对同一个完整 PPA，每个实际转移都有

\[
(d(y,S),\|y-x\|)\in\mathcal E(d(x,S)).
\tag{JP11}
\]

证明是将 JP2 的实际量逐项代入；$Z$ 的半正定性与秩条件自动成立，JP8 先验证 JP7 的评价资格，再投影。全部输出和同一最近锚量词由原图认证保留。

**合取与分支规则。** 增加在同一个 $p$ 上有效的约束，只会缩小 $\mathcal C$，因此不能恶化任何上界或长度测试。有限标签分支的距离/步长最坏值为各分支最坏值之最大；联合长度测试为逐支的同一测试。把约束先压成几个独立最坏常数再合取，通常形成更大的外集合；这一步不再是无损编译。将两个不同最近锚支持的表合并，或把完整图的一支删除，则连此充分性也没有。

<a id="ujc-theorem"></a>
## JP3-v1：联合关系的有限长度后端与物理留域

假设由 JP9 算出或解析认证连续非减 $\tau:[0,R]\to[0,R]$，满足

\[
\tau(0)=0,\quad \tau(t)<t\ (t>0),\quad
q\le\tau(t)\quad((q,s)\in\mathcal E(t)).
\tag{JP12}
\]

连续性可以换成保证 $\tau^k(t)\to0$ 的明定条件；本文不以只有逐点 $\tau(t)<t$ 冒充该结论。取有限非负函数 $W:[0,R]\to[0,\infty)$，$W(0)=0$，并从联合证书验证

\[
\sup_{(q,s)\in\mathcal E(t)}\{s+W(q)\}\le W(t)
\quad(0\le t\le R).
\tag{JP13}
\]

这是对**已由原图编译出的有限约束集**的标量优化测试；在具体定理中须展示 $W$ 及其认证，不能用未知实际轨道的长度定义 $W$ 后宣布可计算。

**定理。** 若 $x^0\in U_R$ 且

\[
W(d_0)<d(x^0,X\setminus U),\qquad d_0=d(x^0,S),
\tag{JP14}
\]

则从 $x^0$ 出发的完整 $J$ 的每条政策都可以无限延拓，留在 $U_R$，具有有限物理长度，收敛到某个 $x^\infty\in S\cap U$。并且

\[
\begin{aligned}
d_k&\le\tau^k(d_0),\\
\sum_{j=k}^{m-1}\|x^{j+1}-x^j\|
&\le W(d_k)-W(d_m)\le W(d_k),\\
\|x^\infty-x^k\|&\le W(d_k),\qquad
\sum_{k\ge0}\|x^{k+1}-x^k\|\le W(d_0).
\end{aligned}
\tag{JP15}
\]

如果 $W$ 非减且 $W(t)\to0$ 当 $t\downarrow0$，还得统一显式尾界 $W(\tau^k(d_0))\to0$。此附加性质不是有限长度存在证明所必需，却是该显示模尾界及小邻域统一预算的必要认证。

**证明。** JP11–JP13 对每个已合法输入的每个完整输出给 $d_{k+1}\le\tau(d_k)\le d_k$ 与 $s_k\le W(d_k)-W(d_{k+1})$。任意有限前缀满足

\[
\|x^{m}-x^0\|\le\sum_{j<m}s_j
\le W(d_0)-W(d_m)\le W(d_0)<d(x^0,X\setminus U).
\tag{JP16}
\]

因此新输出仍在 $U_R$，coverage 可以再次使用。此归纳先于无限轨道与无穷求和。$d_0=0$ 时，JP12 给 $q=0$，JP13 给 $s=0$；全部零输入输出驻定，没有零纤维漂移漏洞。$\tau^k(d_0)\to0$ 由连续性、单调性和严格小于恒等得到。非负步长级数由 JP16 有界，故轨道 Cauchy；有限维完备性、$S$ 闭和距离趋零给极限属于 $S$，严格预算保证仍在 $U$。从任意 $k$ 重新望远镜即得 JP15。□

### 独立尾包络是后端的一种特例，绝非全部

若 $b\ge B$ 非减，$\tau$ 如 JP12，且

\[
L(t)=\sum_{j\ge0}b(\tau^j(t))<\infty,
\tag{JP17}
\]

则 $L$ 非减、$L(t)=b(t)+L(\tau(t))$，从而 $s+L(q)\le L(t)$。于是 JP13 可取 $W=L$。这是 C208/C221 已有标量尾和—Caristi 路线，本文只保留同原对象的接口，不重新登记它。几何 $\tau(t)=\kappa t$ 与 Dini/幂型可和性同样直接回收。

联合关系还给一个准确的诊断量。令 $L_0=0$，

\[
L_{N+1}(t)=\sup_{(q,s)\in\mathcal E(t)}\{s+L_N(q)\},\qquad
L_*(t)=\sup_N L_N(t).
\tag{JP18}
\]

此处空集上确界明确约定为零。在 JP12 下所有后继 $q$ 都在 $[0,R]$。$L_N$ 是该标量关系所有长度至多 $N$ 的有限路径成本上界，且递增；交换非负上确界给 $L_*=\sup_{\mathcal E(t)}(s+L_*(q))$。任何满足 JP13 的非负 $W$ 都逐次支配 $L_N$，所以支配 $L_*$。当 $L_*$ 有限时它是最小非负 Bellman 上解。**这不保证无限次迭代可计算，也不保证半代数表示或零处连续。** 实际证明须像 JP6–JP7 那样给有限描述的 $W$；JP18 只用于精确区分独立成本包络与联合成本。

### 已有平方下降—Hölder EB 的壳层机制也能构造联合 $W$

为了不把“独立尾和失败”误写成“C208 的全部长度机制失败”，另作一个具体恢复。假设同一联合表给出

\[
t^2-q^2\ge c s^2,\qquad s\ge\ell q^p,
\quad c,\ell>0,\quad1\le p<2,\quad0\le t\le R.
\tag{JP18a}
\]

例如全零锚/最近零锚 weak Minty 的正平方耗散给第一式，真实 Hölder EB $q\le K r^\alpha$、$1/2<\alpha\le1$ 给 $p=1/\alpha$、$\ell=\lambda K^{-1/\alpha}$。令 $\delta=2-p>0$，取

\[
W(t)=C t^\delta,\qquad
C\ge\max\left\{
\frac{R^{p-1}}{\sqrt c(1-2^{-\delta})},
\frac{2^{p+1}}{c\ell\delta}
\right\}.
\tag{JP18b}
\]

则 JP13 成立。事实上，若 $q\le t/2$，则 $s\le t/\sqrt c\le R^{p-1}t^\delta/\sqrt c\le W(t)-W(q)$。若 $q\ge t/2>0$，利用两式 JP18a 得

\[
s\le\frac{t^2-q^2}{c\ell q^p}
\le\frac{2^{p+1}}{c\ell}t^{1-p}(t-q)
\le W(t)-W(q),
\tag{JP18c}
\]

最后一步用 $t^\delta-q^\delta=\delta\int_q^t u^{1-p}\,du\ge\delta t^{1-p}(t-q)$。距离上界取方程 $u^2+c\ell^2u^{2p}=t^2$ 的唯一非负根，连续非减且严格小于 $t$。因此全部物理留域和有限长由 JP3 得到。

这是 C208/NGK-6 已有壳层 $\alpha>1/2$ 长度机制的**有限维普通物理对象恢复**及一个显式共同势，不是新颖性主张。不能据此宣布回收原 Hilbert 真核像、近极小锚和 $r_A$ 的全部范围；它们保留自己的对象门。本文严格新增比较 JP40 只针对独立一步尾和门，未排除这个既有平方下降机制。

## JP4-v1：点收敛与有限长度分别认证

只有 JP12 而没有 JP13，不足以推出点收敛，更不能推有限长度。完整目标可能有切向漂移；零距离处也可能全部漂移。下面另列一种由原图给出的点收敛门，避免把无穷长度例误判成发散。

假设同一个完整 $J$ 对**每个** $p\in S$、每个认证转移满足

\[
\langle y-p,b\rangle\ge\frac{\sigma-1}{2}\|b\|^2,
\qquad \sigma\ge0.
\tag{JP19}
\]

则精确恒等式给

\[
\|y-p\|^2+\sigma\|b\|^2\le\|x-p\|^2.
\tag{JP20}
\]

这是比“存在最近锚”更强的另一个量词；不能从 JP1 的最近锚版本免费获得。取 $p_0\in S$，$r_0=\|x^0-p_0\|\le R$，并要求 $\overline B(p_0,r_0)\subset U$（或 $U=X$）。JP20 用有限前缀先保留此球，故 coverage 可无限使用。

- 若另有 JP12，则 $d_k\to0$；有界性给子列极限 $p_*\in S$，JP20 对这个同一 $p_*$ 表明 $\|x^k-p_*\|$ 非增，而其子列趋零，故全部序列趋 $p_*$。这里 $\sigma=0$ 也可以。
- 若 $\sigma>0$，可不调用 EB/JP12，而改要求原图在该闭球与图值零附近序列闭。JP20 给 $\sum\|b_k\|^2<\infty$，故 $f_k=b_k/\lambda\to0$；任意收敛子列 $y_{k_j}\to p_*$ 由原图闭性给 $0\in F(p_*)$，再用上一段的 Fejér 论证得到点收敛。

两条均**不**推出 $\sum\|b_k\|<\infty$。本库已有 VO6 的完整反例

\[
F(y)=\|y\|^2Ky,\quad K(u,v)=(-v,u),\quad S=\{0\}
\tag{JP21}
\]

满足全零锚 $\langle y,F(y)\rangle=0$、完整全域单值覆盖和 $r_F(y)=\|y\|^3$。其近端半径满足 $t^2=q^2+\lambda^2q^6$，所以全部点趋零；实际步 $s_k=\lambda q_k^3\asymp k^{-3/4}$，长度无穷。这里联合编译应接受“点收敛”并拒绝有限 $W$ 的全域长度测试；不能改动目标、度量或算法来掩盖等级差别。完整证明见 [VO6–VO8](../novelty/2026_10_14_submonotonicity/variational_order_review.md)。

## JP5-v1：保留参数的原图入口字典

下面固定 JP2 的 $b=\lambda f$。若条件原来为全图点对型，在 $(p,0)$ 上代入即可，但必须确认此点对落在同一个认证图块/尺度。覆盖仍独立。表中只列同一最近锚的算法证书，不声称这些源条件彼此等价或总体包含。

| 原图条件 | 编译时保留的精确约束 | 可恢复的结论与限制 |
|---|---|---|
| scaled LT：$\langle a,b\rangle\ge-\theta\|a+b\|^2$ | $\operatorname{tr}Z_{ab}\ge-\theta t^2$ | 反射平方 $\le(1+4\theta)t^2$；保留 $\theta$，不提前删能量 |
| 一般 RL：$\|a-b\|\le\omega(\|a+b\|)$ | $\operatorname{tr}(Z_{aa}-2Z_{ab}+Z_{bb})\le\omega(t)^2$ | $s\le[t+\omega(t)]/2$，$q^2+s^2\le[t^2+\omega(t)^2]/2$；普通 C249/C250 全部一步条件原样进入 |
| co-hypomonotone / 零锚 weak Minty：$\langle a,f\rangle\ge-\eta\|f\|^2$ | $\operatorname{tr}Z_{ab}\ge-(\eta/\lambda)\operatorname{tr}Z_{bb}$ | $q^2+(1-2\eta/\lambda)s^2\le t^2$；未松弛严格耗散门 $\lambda>2\eta$，有真 EB 时继续联合消元 |
| scalar semimonotone：$\langle a,f\rangle\ge\mu\|a\|^2+\rho\|f\|^2$ | $C\ge mA+\nu B$，$m=\lambda\mu,\nu=\rho/\lambda$ | 精确保留两个独立参数以及 $C^2\le AB$，不经一个最坏反射常数替代 |
| matrix semimonotone：$\langle a,f\rangle\ge\langle a,Ma\rangle+\langle f,Hf\rangle$ | $\operatorname{tr}Z_{ab}\ge\lambda\operatorname{tr}(MZ_{aa})+\lambda^{-1}\operatorname{tr}(HZ_{bb})$ | 任意对称 $M,H$，不要求交换；有限矩阵直接进入提升，不能随意共同对角化 |
| oblique weak Minty：$\langle a,f\rangle\ge\langle f,Vf\rangle$ | $\operatorname{tr}Z_{ab}\ge\lambda^{-1}\operatorname{tr}(VZ_{bb})$ | 全零锚时回收 $I+2V/\lambda\succ0$ 的 Fejér 点收敛入口；最近锚时仅得局部距离能量 |
| 仿射目标的方向耗散 | $\langle Na,Nb\rangle\ge\lambda m\|Na\|^2$，加 JP5 | 保留法向与物理步长的区别，$q\le t/(1+\lambda m)$；切向成本仍要单独认证 |

对于 RL 与真实 EB $q\le Kr$，设 $L$ 为线性反射常数，联合 SDP 的合法上界至少回收

\[
q\le\sqrt{\frac{1+L^2}{2(1+\lambda^2/K^2)}}\,t,
\qquad s\le\frac{1+L}{2}t.
\tag{JP22}
\]

对于 co-hypo，$\lambda>2\eta$ 时直接回收

\[
q\le\frac{K}{\sqrt{K^2+\lambda(\lambda-2\eta)}}t.
\tag{JP23}
\]

它保留大步长的优势；不能用弱得多的反射三角界消去这个优势。$\eta=0$ 是标准 Minty 能量。$\lambda\le2\eta$ 并不等于每个具体原算子发散，只是此统一耗散系数非正；其他联合原图条件仍可能封闭程序。

### scalar semimonotone 的一维优化，无需先压成反射模

写 $A=\|a\|^2,B=\|b\|^2,C=\langle a,b\rangle$，并令 $k=K/\lambda>0$。全部必要特征满足

\[
A+2C+B=t^2,\quad A\ge q^2,\quad B\ge q^2/k^2,
\quad C\ge mA+\nu B,\quad C^2\le AB.
\tag{JP24}
\]

对 $q>0$，令 $h=\sqrt{B/A}>0$，则仅据这些必要条件可保证

\[
\frac{t^2}{q^2}\ge D(m,\nu,k):=
\inf_{\substack{h>0\\m+\nu h^2\le h}}
\max\{1,(kh)^{-2}\}
\bigl[1+h^2+2\max\{m+\nu h^2,-h\}\bigr].
\tag{JP25}
\]

因此 $D>1$ 时 $q\le t/\sqrt D$。若可行集合为空，JP24 不允许任何正 $q$；若 $D\le1$，此距离测试不通过，不得凭参数名称升级。

**推导。** $C/A\ge\max\{m+\nu h^2,-h\}$，Cauchy 上界要求 $m+\nu h^2\le h$。又 $A/q^2\ge\max\{1,(kh)^{-2}\}$。方括号不小于 $(h-1)^2$，故乘上非负最小比例合法，得到 JP25。反向，对任一可行 $h$，取上述最小 $A/q^2$ 和最小 $C/A$ 就达到特征层的值；二维向量可以实现 $C^2\le AB$。这只说明 **JP24 特征外集合** 的最佳值，不说明存在同一完整原算子实现此最坏值。$q$ 与几何或真实 $r$ 的其他联动可以继续改善它。

例如 $\nu=0,m\ge0$ 时直接算得

\[
D(m,0,k)=1+2m+\max\{m^2,k^{-2}\}.
\tag{JP26}
\]

若 $k^{-1}\le m$，恢复 $q\le t/(1+m)$；若 $k^{-1}\ge m$，保留 EB 与耗散的共同优势 $q\le t/\sqrt{1+2m+k^{-2}}$。这只是原始参数的精确特征消元，不包装成新的强单调收敛原理。对不定混合参数可直接做 JP25 的单变量分段代数优化。

## JP6-v1：GU3 在联合证书中无损通过

取 $0<\gamma<1$，$\lambda=1$，

\[
F(u,v)=\{(0,v),(-2^\gamma|v|^\gamma,v)\},\qquad
S=\mathbb R\times\{0\},\quad r_F(u,v)=|v|.
\tag{JP27}
\]

原图两支直接给每个输入 $(\xi,t_0)$ 的完整输出

\[
(\xi,t_0/2),\qquad(\xi+|t_0|^\gamma,t_0/2).
\tag{JP28}
\]

所以完整覆盖全域。取**输入最近锚** $p=(\xi,0)$，$N$ 为第二坐标投影，$T=I-N$。不把 $q$ 与方向割裂，直接记录原图约束

\[
Na=Nb,\qquad T(a+b)=0,\qquad
q^2=\|Na\|^2,\quad r=q,\quad
\|Tb\|\le2^\gamma q^\gamma.
\tag{JP29}
\]

前两个向量等式可写成范数平方为零的线性提升约束；PSD 外松弛仍保留其零能量后果。结合输入能量得到 $t^2=4q^2$，故

\[
q=t/2,\qquad s\le t/2+t^\gamma.
\tag{JP30}
\]

这里不需要 rank-one 条件来恢复距离。真实残差窗取 $R/2\le\bar r$；它来自 $r=q$，不是把漂移支的巨大选中图值当真实残差。可取

\[
W(t)=t+\frac{t^\gamma}{1-2^{-\gamma}},\qquad \tau(t)=t/2.
\tag{JP31}
\]

逐项有 $W(t)-W(t/2)=t/2+t^\gamma\ge s$，JP3 给全部政策有限长。$U=X$ 时任何有限初值均合法，零输入由 JP29 强制全部驻定。

本例正面机制本库 SC14–SC15 已有，**不是本次新定理**。其用途是证明此证书语法确实保留双范数 $D(\|a\|,\|b\|)$ 所丢失的法向关联。GU3 对固定同物理核 C250 的全部合法模排除及双范数虚假组合，见 [gauge §7](../novelty/2026_10_14_submonotonicity/gauge_unification_review.md) 与 [独立裁决 §4.5](../novelty/2026_10_14_submonotonicity/independent_verdict.md)。这里既不排其他核、其他度量，也不声称总体包含一般核 C250。

<a id="ujc-one-step-loss"></a>
## JP7-v1：严格超过独立最坏包络的完整两支原算子

固定 $X=\mathbb R$，$\lambda=1$，

\[
F(y)=\{y,y^3\},\quad S=\{0\},\quad
r_F(y)=\min\{|y|,|y|^3\}.
\tag{JP32}
\]

两个分量都是原图值；没有删支。完整 PPA 是

\[
J(x)=\{x/2,\ G(x)\},\qquad G(x)+G(x)^3=x.
\tag{JP33}
\]

函数 $y+y^3$ 连续严格递增且满射，所以这是对全部实数输入的完整覆盖。$G$ 奇且保号。对 $0\le t=|x|\le1$，设 $g(t)=G(t)$，有

\[
t/2\le g(t)<t\ (t>0),\qquad
\mathcal E(t)=\{(t/2,t/2),(g(t),t-g(t))\}.
\tag{JP34}
\]

这张联合表由原图方程 $b=a$ 或 $b=a^3$、$p=0$、$a+b=x$ 及同号关系消元得到。不是把收敛结果写回假设。若使用 Gram 语言，要保留一维秩一约束与 $C\ge0$；单独 $C\ge0$ 的 PSD 外松弛不够推出 $t=q+s$。也可直接使用半代数标量分支

\[
\{q,s\ge0:t=q+s,\ (s=q\ \lor\ s=q^3)\}.
\tag{JP35}
\]

对这些输出 $q\le1$，完整真残差为 $r=q^3$，所以 $q=r^{1/3}$ 是准确 EB；其 $r\le1$ 窗由原图分支先保证。两支所有输出的真实残差**相同地**取完整纤维最小值；即使选中快支 $f=y$，也不能把 $r$ 改成 $|y|$。

### 全部政策有限长度与精确长度势

JP34 的 $\tau=g$ 连续非减且严格小于恒等。取 $W(t)=t$，JP35 直接给

\[
s+W(q)=t=W(t).
\tag{JP36}
\]

因此每条完整政策都保号、距离趋零、全局物理长度恰为 $|x^0|$。最后的“恰为”来自有限和 $\sum_{j<k}|x^{j+1}-x^j|=|x^0|-|x^k|$ 后令 $k\to\infty$。虽然以上比较取 $R\le1$，对任意初值仍有 $0<|y|<|x|$，同一望远镜和单调极限论证给全局结论。

### 排除每一组独立上界的可和尾门

考虑任意 $0<R\le1$，任意非负 $\widehat b:[0,R]\to[0,\infty)$、$\widehat\tau:[0,R]\to[0,R]$，只要对完整 $J$ 的全部输入输出满足

\[
|y|\le\widehat\tau(|x|),\qquad
|x-y|\le\widehat b(|x|).
\tag{JP37}
\]

慢支与快支分别强制

\[
\widehat\tau(t)\ge g(t),\qquad
\widehat b(t)\ge t/2\quad(0\le t\le R).
\tag{JP38}
\]

假设 $\widehat\tau$ 的迭代保持在该窗（否则连此尾门都未定义）。对任何 $t_0>0$，令 $r_{k+1}=g(r_k)$。由 $g$ 非减及 JP38，逐步有 $\widehat\tau^k(t_0)\ge r_k$，不需要假设 $\widehat\tau$ 本身单调。又

\[
r_k=r_{k+1}(1+r_{k+1}^2),\qquad
r_{k+1}^{-2}-r_k^{-2}
=\frac{2+r_{k+1}^2}{(1+r_{k+1}^2)^2}\le2.
\tag{JP39}
\]

故 $r_k\ge(r_0^{-2}+2k)^{-1/2}$，于是

\[
\sum_{k\ge0}\widehat b(\widehat\tau^k(t_0))
\ge\frac12\sum_{k\ge0}r_k=+\infty.
\tag{JP40}
\]

这量化**所有合法独立最坏包络**，不只是某组选得粗的 $\omega,\psi$。最好的独立二元信息 $(Q,B)=(g,t/2)$ 也不能通过 JP17，而精确联合表通过 JP13，且 $L_*(t)=t$。独立化把“慢收缩但小步”和“快收缩但大步”重复拼成实际政策无法实现的无限总成本。该严格性针对尾和充分门的信息表示，不排除经典 Minty/一维顺序/Caristi 方法，也不声称 C208 所有可能重新认证或其他 Lyapunov 定理都失效。

它同样排除任意 $\kappa<1$ 的同距离严格几何收缩门，因为 $g(t)/t\to1$。因而这个完整对象不可能通过同算法同目标的 C249/C250 严格几何结论；JP7 的新增作用是比该简单事实更强的 JP40。

<a id="ujc-distance-state"></a>
## JP8-v1：只保距离状态的完备性已被完整两步终止模型否定

此反例由[独立冷审](../novelty/2026_10_14_unified/independent_review.md#ir-distance-state-refutation)提出，以下已从完整图逐项重建。固定 $X=\mathbb R^2$、$\lambda=1$，定义

\[
F(0,u)=\{(u+u^3,\xi):\xi\in\mathbb R\},\qquad
F(y_1,y_2)=\varnothing\quad(y_1\ne0).
\tag{JP41}
\]

这是闭半代数完整图，$S=\{(0,0)\}$，在其非空纤维有

\[
r_F(0,u)=|u+u^3|.
\tag{JP42}
\]

对输入 $x=(x_1,x_2)$，完整近端方程迫使 $y=(0,u)$、$x_1=u+u^3$，而第二图值唯一选为 $\xi=x_2-u$。以下 $g$ 表示 $u\mapsto u+u^3$ 在整个 $\mathbb R$ 上的奇逆，其非负限制就是 JP7 的 $g$。因此

\[
J(x)=\{T(x)\},\qquad T(x_1,x_2)=(0,g(x_1)),
\quad g+g^3=\operatorname{Id}.
\tag{JP43}
\]

完整 coverage 全域，不受 $\operatorname{dom}F$ 是直线影响。这里没有另假设 $F$ 自身处处非空；若额外要求全域连续单值 $F$，这个反例不满足该更窄对象，不能用于排除那一子类的完备性。$T^2(x)=0$，所以全部轨道两步终止，任意闭球不变，且总长有统一零消失预算

\[
\|x-Tx\|+\|Tx\|\le\|x\|+2\|Tx\|\le3\|x\|.
\tag{JP44}
\]

又 $d(Tx,S)=|g(x_1)|\le g(\|x\|)<\|x\|$ 对非零输入成立；每个紧的正距离壳层有严格统一下降。真实 EB $d(y,S)\le r_F(y)$ 全域成立。没有隐去 coverage、残差或零吸收门。

令 $\mathcal E_{\rm exact}(t)$ 是**全部实际完整转移**在输入距离 $t$ 上的精确 $(q,s)$ 集，不作任何 Gram/PSD 松弛。输入 $x=(t,0)$ 给

\[
\bigl(g(t),\sqrt{t^2+g(t)^2}\bigr)\in\mathcal E_{\rm exact}(t).
\tag{JP45}
\]

假设存在任一有限非负 $W$ 满足 JP13，哪怕不要求它单调、连续或半代数。则对 $r_{k+1}=g(r_k)$，反复用 JP45 有

\[
W(r_0)\ge\sum_{k<N}\sqrt{r_k^2+r_{k+1}^2}+W(r_N)
\ge\sum_{k<N}r_k.
\tag{JP46}
\]

JP39 证明右侧随 $N\to\infty$ 发散，矛盾。故在任意正窗不存在这样的有限 $W$。**即使精确知道一步全部距离—步长对，也不能保证存在径向长度势。** 实际第一步输出已落在竖轴，下一步必到零；只保距离的关系忘掉竖轴身份，错误地允许每次重新扮演水平输入 $(r_k,0)$。

这否定了“半代数闭图 + 完整覆盖 + 联合有界输出 + 全部政策统一有限长 + 严格壳层距离下降，必有只依赖距离的有限长度势”的一般完备性猜想。输出在紧输入球上联合有界；所有这些前件在同一个完整原模型成立。它不否定 JP3 的充分性，只否定把 JP3 的单一距离状态称为普遍必要或完备。

<a id="ujc-state-theorem"></a>
## JP9-v1：保留有限原生状态的父版本

JP8 说明，分支标签须在需要时升级为可传递的**输入状态**。取原模型上预先定义的有限状态函数 $\chi:X\to\{1,\ldots,m\}$，例如一个半代数方向分区；它只读取当前物理 $x$，不读取未来轨道或人为选中的输出。对每个 $i,j$，按 JP1–JP2 的原图证书认证联合关系 $\mathcal E_{ij}(t)$，满足：

\[
x\in U_R,\ y\in J(x),\ \chi(x)=i,\ \chi(y)=j
\ \Longrightarrow\ (d(y,S),\|x-y\|)\in\mathcal E_{ij}(d(x,S)).
\tag{JP47}
\]

每个完整实际输出仍被其真正的状态对覆盖。状态转移不可能性必须来自原图；不能为了降低上界而删去可能的 $(i,j)$。有限状态分支可与前述 Gram/半代数约束联合，必要时在原变量中认证状态谓词，再把其结论列为有限表。

假设一条共同的连续非减 $\tau$ 满足 JP12 的零与严格门，且所有 $\mathcal E_{ij}$ 中 $q\le\tau(t)$。给出有限非负 $W_i:[0,R]\to[0,\infty)$，每个 $W_i(0)=0$，并逐状态认证

\[
\sup_{\substack{j\in\{1,\ldots,m\}\\(q,s)\in\mathcal E_{ij}(t)}}
\{s+W_j(q)\}\le W_i(t).
\tag{JP48}
\]

若 $W_{\chi(x^0)}(d_0)<d(x^0,X\setminus U)$，则完整原 PPA 的所有政策存在、物理留域、有限长度与趋 $S$，而且

\[
\sum_{k=N}^{\infty}\|x^{k+1}-x^k\|
\le W_{\chi(x^N)}(d_N),\qquad
d_N\le\tau^N(d_0).
\tag{JP49}
\]

**证明。** 沿实际状态 $i_k=\chi(x^k)$，JP48 给 $s_k\le W_{i_k}(d_k)-W_{i_{k+1}}(d_{k+1})$。有限前缀望远镜、严格物理预算、coverage、零吸收、距离趋零及闭目标极限的证明逐行同 JP16；被望远镜消去的是同一实际后继状态的势，不能换成另一个状态的最坏值。若各 $W_i(t)\to0$，有限 $m$ 给统一零消失尾模 $\max_iW_i(\tau^N(d_0))$（此显示上界还要求各 $W_i$ 非减）。□

**JP8 的两状态修复。** 取 $\chi(x)=0$ 当 $x_1\ne0$，$\chi(x)=1$ 当 $x_1=0$（标签可平移为 $1,2$）。原图保证只会发生 $0\to1$ 和 $1\to1$；后者 $q=0,s=t$。前者 $q\le g(t)\le t$、$s\le t+q$。于是

\[
W_0(t)=3t,\qquad W_1(t)=t,\qquad \tau(t)=g(t).
\tag{JP50}
\]

给 $s+W_1(q)\le t+2q\le3t$ 和 $s+W_1(0)=t$，JP48 全部成立。同一个 $F,\lambda,S,r_F$ 与全部输出被保留，物理总长仍为 JP44 的统一上界。这里 $\chi$ 不连续没有造成问题：它是原图可检验的有限状态，有限前缀证明不需要其连续性。

JP9 仍是可验证充分合同；自动寻找有限状态及其势的完备性没有证明。实际原图中方向可能需要连续状态或无限记忆，不能用本反例的两状态成功宣布所有模型均可有限化。

## 三轮攻击记录与已修正的失败路线

**第一轮：只有两个范数和真实 EB。** 初拟将 $\langle a,b\rangle\ge-D(\|a\|,\|b\|)$、三角能量和 $q\le\psi(r)$ 联合优化。GU3 漂移支允许 $\|a\|=\|b\|\asymp t^\gamma$，直支又迫使独立 EB 下界仅线性，虚假选择 $q\asymp t^\gamma$ 无法排除。该路线不能包含 GU3；修正为 JP4–JP5 保留投影与 $q$ 的关联，且每个分支内合取。零输入漂移 $F(u,v)=\{(u,0),(u,-1)\}$ 表明 $Q(0)=0$ 仍不足，JP13 的 $W(0)=0$ 或显式 $B(0)=0$ 必须保留。

**第二轮：PSD 即精确、EB窗和只写 $\tau<t$。** 初拟只保留 $2\times2$ Gram PSD 与 $C\ge0$，试图在 JP7 得到 $s=t-q$。反例特征 $A=B=1,C=0,t=\sqrt2,q=1,s=1$ 已满足这些约束，却有 $s>t-q$。修正为正共线秩约束/原图半代数分支；SDP一律仅作安全外松弛。另删除了“先 EB 后估残差窗”的循环，改为 JP8。逐点 $\tau(t)<t$ 若缺连续/上半连续等门，可能迭代趋正值；现用明确连续单调 $\tau$。最后，单独 Caristi 下降可能停在非零固定点，故 JP13 与独立 JP12 合取，或在点级使用 JP19–JP20 加真实零图闭性。

**第三轮：完整半代数图也未必容许只看距离的势。** JP8 的两步终止反例否定了最初 OPEN-JP-A 的强形式。第一步标签保真并不足以保真下一步可达性；$\mathcal E_{\rm exact}$ 已经完全准确，却仍因忘记方向而制造无限成本路径。修正为 JP9 的原生有限状态标签在相邻步传递。未将修正包装成普遍完备性；剩余问题必须明确允许并刻画保留的状态。

这些修正均在正文承担证明，不靠程序、历史文件或“审查通过”标签补前提。

## 精确 6pro 交接：仍未证明的高价值问题

### OPEN-JP-A：保留原生状态后的可计算完备性

**对象/量词。** 固定有限维普通 PPA、非空闭完整 $S$、同一正实代数 $\lambda$；$F$ 的完整图和认证紧输入窗 $K$ 由有理/实代数系数的有限半代数公式给定，所有完整输出联合有界，coverage 在 $K$ 成立，且每个输出留在 $K$。不容改 $F,S,\lambda$、选支或加入已知轨道收敛作证书。

**期望结论。** 假设存在有限 $\overline W:[0,R]\to[0,\infty)$、$\overline W(0)=0$、$\overline W(t)\to0$ 当 $t\downarrow0$，使每个 $x^0\in K$、每条完整政策均有 $\sum_k\|x^{k+1}-x^k\|\le\overline W(d(x^0,S))$，且在每个非零紧距离壳层有统一严格距离下降。是否必存在可有效枚举的有限半代数原生状态分区 $\chi$ 与实代数系数半代数非负 $W_i$，每个 $W_i(0)=0$、$W_i(t)\to0$，使 JP47–JP48 在缩小但正宽的同一窗通过？若有限分区不够，允许一个**预先指定、由原模型计算**的有限维连续方向特征 $\zeta(x)$ 与半代数势 $W(d(x,S),\zeta(x))$，能否证明一个自然受限原算子类的充分/必要边界？不能以完整物理状态任意重命名为“标量特征”宣称已完成压缩。

**已试路线和断点。** JP18 给抽象最小预算，但无限上确界不保证半代数、连续或可计算。有限松弛层级可以认证单步多项式上界，却不自动给无限尾固定点。对 rank-one 去除的 SDP，JP7 已有精确断点；只扩大 $D(r,s)$ 又被 GU3 否定。只依赖距离的强完备性已由 JP41–JP46 **明确反驳**，不再作为开放题。JP9 的两状态修复只对那个原模型成立，尚没有一般有限状态完备定理。

**可行缩弱。** 已知一个有限方向自动机且各状态有共同径向顺序；先证明给定状态分区、固定 degree 的可认证性而不宣称完备；或者额外给定一个半代数势模板及可检验的 strict margin。下一步应寻找“任意有限半代数状态分区仍失败、但某个连续原生特征成功”的完整原图，或证明在自然受限算子类中有限分区已足够；不得再重做已被 JP8 解决的 distance-only 猜想。

### OPEN-JP-B：从方向原图规则自动得到覆盖

**对象/量词。** 对某个明确有限方向/多项式预算类 $\mathfrak G$，定义保持同一预算和完整零集的包含极大图。询问每个这样的极大图是否满足 $\operatorname{ran}(I+\lambda F)=X$。

**断点。** 上界 SDP 或非空标量可行集不产生真实图点。一般非线性/分支预算没有证明保持参数的单点扩张性质。已有 semimonotone 的特定二次平移球扩张不能自动搬到任意方向半代数表。本文 JP1 诚实保留 coverage，未宣称该问题解决。

**可行缩弱。** 找到等价于欧氏或一个固定 Hilbert 范数 Lipschitz 图的有限参数子类，并证明扩张保持原预算及零集；或者只对一个原生多项式模型用强制性/度数证明覆盖。独立 coverage 分工另有专文，合并时应保留其反例量词。

### OPEN-JP-C：一般核/曲目标/误差的统一精确接口

**对象。** 对固定可能非单射 $v$，原始物理更新 $v(x)-v(y)\in\lambda F(y)$；或真实图缺陷 $x=y+\lambda f+e$。要求同原 $F,S$、真实残差、全部完整/接受输出以及物理长度。

**断点。** 本文 $b=x-y=\lambda f$ 的同一变量同时承担图耗散和物理步，在一般核中不成立；非单射核可有完全不可见的物理漂移。曲目标也不能把 $q$ 写成固定投影范数，必须输入可验证的曲率/最近点桥。误差扩展需在同一个提升里保留 $a,b,e$ 的全部交叉项，且认证新接受关系的覆盖和零吸收；不能从精确输出证书直接推所有近似输出。

**已得缩弱/下一步。** 固定核加入由原模型单独证明的物理提升，并对 $(a,b,e)$ 作有限提升；曲目标使用局部 reach/法丛证书；误差用独立 inexact 分工的 co-hypo/GU3 精确停止门。这些属于分别有额外前件的接口，不计为本文已证明的一般统一定理。JP7 的一维双支在 $|e|\le\sigma|f|,\sigma<1$ 下仍保号且望远镜，独立分工正在写定完整接受量词。

## 复算范围、边界与交付

运行 `python3 research/code/unified_ppa/joint_verify.py`。程序用标准库 `Fraction` 核二次提升、Cauchy相关、LT/semimonotone缩放、JP25/JP26指定参数、JP39 的精确有理式和 JP41 的完整图实例；浮点部分只枚举指定有限政策前缀及壳层势样本。实际运行通过：625 个精确 Gram 实例、22620 个 semimonotone 特征不等式、12 个特征极值点、2080 个慢支有理式、544 个 GU3 方向实例、1089 个两步终止原图实例，以及 32764 次两支前缀转移、19209 个壳层势浮点样本。无随机 seed，浮点容差 $2\cdot10^{-12}$，最大望远镜误差 $4.45\cdot10^{-16}$ 以下。程序不证明一般图条件、coverage、无限可和性、SDP完备或外部优先权。

本轮接收的闭合单元是：原图有限联合证书的明确计算合同；全部政策的联合/有限状态长度后端；JP32–JP40 对**所有独立最坏尾包络**的严格排除；JP41–JP46 对**精确一步距离状态完备性**的完整两步终止反例与 JP50 的同原图状态修复。独立审查已冷读 JP1–JP9、重算 JP18a–c、JP25–JP26、JP39–JP50，并复跑验证器，未报致命缺口；闭合单元注册 C277/C278；末节 OPEN-JP-A/B/C 仍为 open，不因同页规范化而升级。C208/C221 的非几何/Caristi后端、SC14–SC15/GU3的方向正面机制和 weak-Minty Fejér 收敛均明确作为已有机制恢复。没有宣布“所有次单调”的完备分类，也没有证明任何一个仍标开放的问题。
