# Cantor 完整零集：全轨道有限长度收敛仍不能替代严格 RLEB

**范围。** 以下是一个新构造的标量机制例，未改动主稿、canonical 或 Claim 编号。固定 Euclidean 空间 \(X=\mathbb R\)、普通核 \(v=\mathrm{Id}\)、步长 \(\lambda=1\)、完整目标零集 \(S=\operatorname{zer}F\)，并控制完整近端关系的全部输出。它说明当前 C02-v2/v3、C250-v1 的严格同距离收缩门有实质内容；不声称刻画全部可实现零集，也不将这个分形例称为实际应用。

读入的合同为 `AGENTS.md`、`RESEARCH_PROTOCOL.md`、`research/rleb_ppa.md`、`research/canonical/true_residual_selection_rleb.md`、`research/canonical/physical_rleb_gppa.md` 的 C250 分支，以及 `research/canonical/general_modulus_dynamics.md` 的 C11。证明按 `academic-writing-skills` 的数学审查与选例指南重建。下文全称结论有解析证明；程序只补充精确有理数实例检查。

## 1. 完整对象与真残差

令 \(C\subset[0,1]\) 为 usual ternary Cantor set：每轮删除所有保留闭区间的开中间三分之一。定义完整单值关系

\[
F(y)=
\begin{cases}
y,&y<0,\\
\frac12 d(y,C),&0\le y\le1,\\
y-1,&y>1.
\end{cases}
\tag{CP1}
\]

其图在全空间上定义且闭，完整零集和真实残差分别为

\[
\operatorname{zer}F=C,
\qquad r_F(y)=|F(y)|.
\tag{CP2}
\]

此处没有限制图值、允许子纤维或替换残差。特别是

\[
d(y,C)=2r_F(y)\quad(0\le y\le1),
\qquad d(y,C)=r_F(y)\quad(y\notin[0,1]),
\tag{CP3}
\]

所以完整关系有全局线性真 EB

\[
\boxed{d(y,C)\le2r_F(y).}
\tag{CP4}
\]

Cantor 集的每个互补有界分量是一个开间隙 \((a,b)\)，两端均属于 \(C\)。若 \(\ell=b-a\)，则该间隙内

\[
d(y,C)=\min\{y-a,b-y\}.
\tag{CP5}
\]

因为 \(C\) 在该开区间内没有点，两端给最近点；区间外的 Cantor 点不会更近。这是无限 Cantor 集的精确公式。

## 2. 全空间完整纤维与统一反射界

距离函数是 1-Lipschitz。于是 \(F\) 在 \([0,1]\) 上是 \(1/2\)-Lipschitz，在两个外侧分别斜率为 1，且在 0、1 连续。对跨越 0 或 1 的点对，在这些端点分割并求和，得到 \(F\) 全局 1-Lipschitz。

更关键的是，对任意 \(u<w\)，在 \([0,1]\) 内

\[
F(w)-F(u)\ge-\tfrac12(w-u).
\]

外侧的斜率 1 同样满足此不等式。跨区间点对仍在 0、1 分割后相加。因此 \(F+\frac12\mathrm{Id}\) 全局非减。置 \(H=\mathrm{Id}+F\)，得到对**每个**全空间点对

\[
\boxed{\tfrac12(w-u)\le H(w)-H(u)\le2(w-u).}
\tag{CP6}
\]

故 \(H\) 为连续、\(1/2\)-强单调、2-Lipschitz 的同胚；满射来自外侧公式 \(H(y)=2y\)（\(y<0\)）与 \(H(y)=2y-1\)（\(y>1\)）。因而所有输入的完整纤维是

\[
J_F(x)=\{T(x)\},\qquad T=H^{-1}:\mathbb R\to\mathbb R.
\tag{CP7}
\]

没有遗漏的远端纤维。每个间隙被 \(H\) 单调地映到自身。令
\(m=a+\ell/2\)、\(q=H(m)=a+3\ell/4\)，直接反演两条线段给

\[
T(x)=
\begin{cases}
a+\frac23(x-a),&a<x\le q,\\
b+2(x-b),&q\le x<b.
\end{cases}
\tag{CP8}
\]

两式在 \(q\) 的值同为 \(m\)。其余完整输入分别满足

\[
T(x)=x\ (x\in C),\qquad
T(x)=x/2\ (x<0),\qquad
T(x)=(x+1)/2\ (x>1).
\tag{CP9}
\]

**无限间隙的全对界。** 不需要把无限多段斜率直接求和。对任意 \(x<z\)，将 (CP6) 用于 \(T(x)<T(z)\)，即得

\[
\tfrac12(z-x)\le T(z)-T(x)\le2(z-x).
\tag{CP10}
\]

令反射 \(B=2T-\mathrm{Id}\)。于是

\[
0\le B(z)-B(x)\le3(z-x).
\tag{CP11}
\]

这覆盖所有点对，包括跨越无限多个间隙、Cantor 点对、外侧点对。\(B\) 在左外侧恒等于 0、右外侧恒等于 1，故单调性还给 \(0\le B\le1\)。在每个间隙，\(B\) 两段的斜率分别为 \(1/3\) 和 3，因此 Lipschitz 常数 3 也实际取到。

任意 \(0<\gamma<1\) 和 \(\delta=|x-z|\) 满足

\[
|B(x)-B(z)|\le\min\{3\delta,1\}
\le3^\gamma\delta^\gamma.
\tag{CP12}
\]

最后一步分别在 \(3\delta\le1\) 与 \(3\delta\ge1\) 验算。因而完整图具有全尺度、全点对的有限常数 Hölder 反射界，同时反射全局有界。

## 3. 一个标准弱凸目标的完整近端实现

定义

\[
f(y)=\int_0^yF(t)\,dt.
\tag{CP13}
\]

\(F\) 连续且全局 1-Lipschitz，故 \(f\in C^{1,1}(\mathbb R)\)、\(f'=F\)。由 \(F+\frac12\mathrm{Id}\) 非减，\(f(y)+y^2/4\) 凸，因此 \(f\) 是 \(1/2\)-弱凸函数。在两侧

\[
f(y)=y^2/2\quad(y<0),\qquad
f(y)=f(1)+(y-1)^2/2\quad(y>1),
\tag{CP14}
\]

故 \(f\) 强制。每个长度 \(\ell\) 的间隙贡献积分 \(\ell^2/8\)。第 \(n\) 层有 \(2^{n-1}\) 个长度 \(3^{-n}\) 的间隙，因此

\[
f(1)=\frac18\sum_{n\ge1}2^{n-1}3^{-2n}
=\frac18\frac{1/9}{1-2/9}
=\boxed{\frac1{56}}.
\tag{CP15}
\]

剩余 Cantor 集上被积函数等于 0；所以这不是有限阶段间隙面积的近似等式。

对每个输入 \(x\)，近端目标

\[
G_x(y)=f(y)+\tfrac12(y-x)^2
\]

的导数为 \(H(y)-x\)，由 (CP6) 为 \(1/2\)-强单调，所以 \(G_x\) 是 \(1/2\)-强凸且强制的函数。其唯一驻点就是唯一全局极小点。因此

\[
\boxed{T(x)=\operatorname*{argmin}_{y\in\mathbb R}
\{f(y)+\tfrac12(y-x)^2\}.}
\tag{CP16}
\]

**目标含义。** \(C\) 是 \(f\) 的完整驻点集，\(\partial f=\{F\}\)，不是 \(f\) 的极小点集合。因为 Cantor 集无内点，每个 \([0,1]\) 的非退化区间都含一段间隙，\(f\) 在 \([0,1]\) 严格递增；连同 (CP14)，其唯一全局极小点为 0。RLEB 本来允许目标零集，不能将这里的 stationary-set 结论改写成 minimizer-set 结论。

## 4. 全部 PPA 轨道收敛且有有限长度

完整映射单值，故“全部轨道”就是每个 \(x^0\in\mathbb R\) 的唯一轨道。它们没有输入存在性或留域障碍。

* \(x^0\in C\)：轨道驻定。
* \(x^0<0\)：\(x^k=2^{-k}x^0\uparrow0\)，总长度 \(|x^0|\)。
* \(x^0>1\)：\(x^k=1+2^{-k}(x^0-1)\downarrow1\)，总长度 \(x^0-1\)。
* \(x^0\in(a,b)\)：(CP8) 给 \(a<T(x)<x<b\)。轨道严格递减且下界为 \(a\)。连续性使其极限成为固定点，而 \([a,x^0]\cap C=\{a\}\)，故极限为 \(a\)，总长度精确为 \(x^0-a\)。

于是极限选择 \(P(x)=\lim_kT^kx\) 有完整公式

\[
P(x)=
\begin{cases}
0,&x<0,\\
x,&x\in C,\\
a,&x\in(a,b)\text{ 为 Cantor 间隙},\\
1,&x>1,
\end{cases}
\qquad
\sum_{k\ge0}|x^{k+1}-x^k|=|x-P(x)|.
\tag{CP17}
\]

每条间隙轨道最终进入左线性段，随后误差以 \(2/3\) 收缩。问题出在进入这段之前没有统一的短暂期，而非轨道自身不收敛。

## 5. 排除任意同物理距离的严格 C02/C250 认证

固定任意间隙 \((a,b)\)、\(\ell=b-a\)，取
\(0<\varepsilon<\ell/4\)，置 \(x=b-\varepsilon\)。它的唯一最近零点为 \(b\)，而 (CP8) 给

\[
Tx=b-2\varepsilon,\qquad
d(x,C)=\varepsilon,\qquad d(Tx,C)=2\varepsilon,
\qquad r_F(Tx)=|x-Tx|=\varepsilon.
\tag{CP18}
\]

所以对任何 \(\kappa<1\)，\(d(Tx,C)\le\kappa d(x,C)\) 均失败。若 \(U\) 是包含 \(C\) 的开集且 \(R>0\)，取 \(\varepsilon\) 足够小，\(x\) 与 \(Tx\) 都在 \(U_R\)；故失败不能靠缩小统一领圈避免。事实上 Cantor 的基本闭区间任意小，任何 Cantor 点的开邻域内都有这样的间隙右端，所以同一完整目标距离的局部统一收缩在每个 Cantor 点附近也失败。

**任意 gauge 的直接攻击。** 假设 C02-v3 存在某组 \(L,\gamma,\psi,\kappa,R,\bar t\)，并对同一个完整 \(T\)、同一个 \(C\) 成立。输入 \(x=b-\varepsilon\) 的锚比较强制

\[
L\varepsilon^\gamma\ge|2Tx-x-b|=3\varepsilon,
\qquad B(\varepsilon)=\tfrac12(\varepsilon+L\varepsilon^\gamma)
\ge2\varepsilon.
\]

真实输出 EB 又强制 \(\psi(\varepsilon)\ge2\varepsilon\)。由于评价窗口是前件的一部分，单调性和直接兼容遂要求

\[
2\varepsilon\le\psi(\varepsilon)
\le\psi(B(\varepsilon))\le\kappa\varepsilon,
\tag{CP19}
\]

矛盾。这排除的是全部符合合同的 gauge，不仅是自然线性 gauge \(\psi(t)=2t\)。全对 C02-v2 是较强前件，也随之被排除。

对于 C250-v1，任何符合其同锚下界和标量能量门的 \(\rho,g\) 都必须沿实际输出推出同一个 \(d(Tx,C)\le\kappa d(x,C)\)。可直接看到其标量前件在实际值 \(t=\varepsilon,q=2\varepsilon\) 必成立：最近锚 \(b\) 的真实能量是

\[
|Tx-b|^2+|x-Tx|^2=5\varepsilon^2,
\]

而 \(\rho(q)^2+g(q)^2\) 不超过此真实能量，锚反射上界提供的能量右端不小于它。标量门却强制 \(2\varepsilon\le\kappa\varepsilon\)，仍矛盾。这里固定 \(v=\mathrm{Id}\)、\(\lambda=1\)、物理距离 \(d(\cdot,C)\)；改变核、目标子集或算法是另一个对象，未被这项排除覆盖。

## 6. 非 ENR、极限跳跃与统一尾的断点

Cantor 集完全不连通：若 \(c<d\) 均属于 \(C\)，选 \(3^{-n}<d-c\)，它们位于第 \(n\) 轮不同基本区间，被一个删除间隙隔开。因此 \(C\) 的每个连通子集为单点。Cantor 集还是完美集：在任意足够长的 0/2 三进制前缀后改动一个更远位，得到任意接近的不同 Cantor 点。

若存在开集 \(O\supset C\) 与连续回缩 \(r:O\to C\)，在任意 \(c\in C\) 处取开区间 \(I\subset O\)；完美性保证其中有另一 Cantor 点 \(d\ne c\)。\(r(I)\) 连通，故为单点，但回缩要求 \(r(c)=c,r(d)=d\)，矛盾。因此 \(C\) 不是 Euclidean neighborhood retract；局部非空 Cantor 邻域也不能满足 C11 的局部可缩量词。

这个障碍在实际迭代极限中可见：每个间隙右端 \(b\) 满足

\[
\lim_{x\uparrow b,\ x\in(a,b)}P(x)=a\ne b=P(b).
\tag{CP20}
\]

极限选择在每个这样的 \(b\) 不连续。尽管所有有限迭代 \(T^k\) 都连续，它们不会在任何包含 \(C\) 的邻域上一致趋于 \(P\)。例如取
\(x_k=b-\ell/2^{k+4}\)，前 \(k\) 次均使用右分段，所以

\[
T^kx_k=b-\ell/16,\qquad P(x_k)=a,
\qquad |T^kx_k-P(x_k)|=15\ell/16.
\tag{CP21}
\]

\(x_k\to b\)，故最终属于任意给定的开邻域。并且由 (CP17)–(CP18)

\[
d(b-\varepsilon,C)=\varepsilon\to0,
\qquad \sum_{k\ge0}|x^{k+1}-x^k|=\ell-\varepsilon\to\ell>0.
\tag{CP22}
\]

所以任何满足 \(\Theta(t)\to0\) 的共同初始距离长度界
\(\sum_{k\ge0}|x^{k+1}-x^k|\le\Theta(d(x^0,C))\)
都失败。此例恰好缺失 C11 将有限轨道连续性传到极限的共同尾前件。

## 7. 总指数仍为 1

\(T([-2,2])=[-1,3/2]\subset(-2,2)\)，且全部固定点正是 \(C\)。对一维映射 \(x-Tx\)，左边界值为 \(-1\)、右边界值为 \(1/2\)。因此

\[
i(T,(-2,2))=\deg(\mathrm{Id}-T,(-2,2),0)=1.
\tag{CP23}
\]

亦可将 \(T\) 在该闭区间内同伦到常值 \(1/2\)；同伦像始终严格在区间内部，所以边界无固定点，最终常值映射的指数为 1。总指数 1、完整紧零集、全局 Hölder 反射和全轨道收敛可以与非 ENR 零集并存。不能从这些条件反向授予严格 RLEB 或把 \(C\) 当作有限同调 ENR 使用 Euler 特征公式。

## 8. 可复现的无限 Cantor 有理数算法

`research/code/rleb_cantor_zero_geometry/verify.py` 仅用 Python 标准库和 `Fraction`。在当前基本区间 \([a,a+w]\) 内令归一化坐标 \(z=(x-a)/w\)。若 \(1/3<z<2/3\)，立即得到当前实际间隙两端 \(a+w/3,a+2w/3\)；否则进行左变换 \(z\mapsto3z\) 或右变换 \(z\mapsto3z-2\)。0、1、1/3、2/3 是精确 Cantor 端点。

对初始有理数 \(p/q\)，每个归一化状态的分母都整除 \(q\)，分子在 0 与 \(q\) 之间。状态总数有限；若在未进入中间三分之一时重复，它将永久循环只含 0/2 的三进制位，故属于实际无限 \(C\)。算法总终止且不会把周期点误作未知；例如 \(1/4=0.020202\ldots_3\in C\)。

势函数的有理数值也精确计算。令 \(A=f(1)=1/56\)，自相似性给

\[
f(x)=\tfrac19f(3x)\ (x<1/3),\qquad
f(x)=\tfrac89A+\tfrac19f(3x-2)\ (x>2/3).
\]

中间三分之一由二次式直接积分。归一化状态重复时，解一个精确的仿射循环方程，无截断余项。例如 \(f(1/4)=1/560\)。

验证覆盖第 1–6 层所有 63 个真实间隙的端点、切换阈值、两段内部样本、负和远端输入、周期 Cantor 点、完整反演 \(H(Tx)=x\) 与 \(T(Hy)=y\)、跨间隙成对强单调/反射界、真 EB、每个间隙的任意小近右端距离加倍、轨道前缀的精确长度恒等式，以及近端目标的有限点比较。面积和为 20 层精确部分和加解析几何级数尾。一般结论由上文证明，有限检查不替代它们。

运行命令：

```bash
python3 research/code/rleb_cantor_zero_geometry/verify.py
```

输出登记到`research/code/rleb_cantor_zero_geometry/results.json`；环境为 Python 3，无随机数或 binary64 判定。

## 9. 附加的目标依赖比较：四次目标

若需更自然的有限零集示例，可另用 \(F_4(y)=y^3-y\)、\(\lambda=1\)。完整近端目标

\[
\tfrac14y^4-\tfrac12y^2+\tfrac12(y-x)^2
=\tfrac14y^4-xy+\tfrac12x^2
\]

有唯一全局极小点 \(T_4(x)=\sqrt[3]{x}\)，完整零集为 \(S_4=\{-1,0,1\}\)。针对 \(M_+=\{1\}\) 取

\[
U_+=(3/4,5/4),\quad R=1/4,\quad\bar t=1,
\quad\gamma=1,\quad L=1/2,\quad
\psi(t)=\tfrac{100}{171}t,\quad\kappa=1/2.
\tag{CP24}
\]

对该输入窗，\(9/10<T_4(x)<11/10\)。反射导数
\(2/(3y^2)-1\) 的绝对值不超过 \(1/2\)，由均值定理给同窗全对反射界（与零锚 1 的比较也在此窗）。实际输出满足

\[
|F_4(y)|=|y-1|y(y+1)\ge\tfrac{171}{100}|y-1|.
\]

故真 EB 成立，残差窗口预算 \((R+LR)/2=3/16<1\)，直接兼容系数为
\(\frac{100}{171}\frac34=25/57<1/2\)。全部局部门闭合；严格初始长度预算 \(\mathcal L(d)=3d/2\) 在 \(|x^0-1|<1/10\) 成立。负目标 \(M_-=\{-1\}\) 由奇对称给同样认证。

但针对同一完整 \(S_4\)，取 \(x=t^3\)、\(0<t<1/2\)，则

\[
\frac{d(T_4x,S_4)}{d(x,S_4)}=\frac{t}{t^3}=t^{-2}>1.
\tag{CP25}
\]

完整三点目标在 0 附近没有任何严格同距离 C02/C250 认证。这里的差异是同一算法的目标依赖；它不具备主 Cantor 例的全局有界反射条件，也不应替代主例。

## 独立攻击结果与结论边界

另一研究代理独立检查了全局强单调、间隙反演、反射有界性、面积 \(1/56\)、非 ENR 证明、极限跳跃与共同长度界失败，未发现 fatal objection，并明确指出 Cantor 零集不能称为 minimizer 集。该检查与精确验证器都未触碰主稿或规范身份。

已经证实的分离是：**全域连续唯一普通 PPA + 全局有界 Hölder 反射 + 完整真线性 EB + 全部轨道有限长度趋零集**，仍可具有非 ENR 的完整紧零集，并失败于 C02/C250 的任意同距离严格 \(\kappa<1\) 合同。C11 的连续回缩来自其更强的统一尾合取前件；本例没有反驳它。对其他核、其他目标、其他收敛机制或所有零集的完整分类，本文没有结论。


## 证明准入表

| 门 | 结果 | 全部对象范围 |
|---|---|---|
| 完整零集、真实残差 | 通过 | $S=C,\ r_F=|F|$；驻点集与唯一 minimizer 0 区分 |
| 完整 coverage、远端／跨间隙纤维 | 通过 | 全域强单调 $H$ 的唯一逆，等于完整 argmin |
| 全对反射、真线性 EB | 通过 | 无限间隙与外侧的所有点对，反射有界；$d\le2r_F$ |
| 同一最近锚 | 近右端明确为 $b$ | 不选其他零点以规避距离扩张 |
| 任意同距离严格 C02/C250 门 | fatal、排除 | $d(T(b-\varepsilon),C)=2\varepsilon$ 是解析全称机制 |
| 全部轨道有限长度、存在和留域 | 通过 | 全域单值迭代，完整极限与长度公式 |
| 共同消失尾／连续极限／ENR | 失败 | 右间隙端极限跳跃，总长不随起始距离趋零 |
| 全局总指数 | 通过 | 完整固定点集的区间总指数 1；不可套 ENR Euler 公式 |
| 应用解释／外部优先性 | 机制对照／未认证 | 精确分形构造，不推荐作自然应用 |

本轮总入口：[RLEB 零集几何分类研究](../../发表成果整理/本轮重构/RLEB零集几何分类研究.md)。此卡只存候选证明与内部检查，不改变规范命题身份。
