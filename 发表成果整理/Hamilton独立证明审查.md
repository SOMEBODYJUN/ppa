# Hamilton 例独立证明审查

审查对象：原始投稿包/sections/verification_example.tex，以及该例调用的原始投稿包/sections/theorem_spine.tex。只依据原始数学定义独立推导，未读取其他审查报告。

结论：Hamilton 例的主要数学结论成立。原稿的动量 Jacobian 在可微点上的界正确，但“平滑正则化后一致成立并取极限”没有给出正则化、保持条件和收敛论证，属于需要补足的证明步骤。本审查已用原方程的有限差分证明替换它，包含 $p=0$、$x_1=0$ 及跨越这些点的情形。

| 项目 | 独立判断 |
| --- | --- |
| $J_F$ 的全空间存在性、唯一性 | 成立；严格凸且强制的极小化问题直接给出 |
| 完整输入图像块上的 all-pair RL | 成立；无需选择分支、无需只比较零点 |
| 动量 $0.02$-Lipschitz 界 | 成立；有限差分实际上给出小于 $0.015$ 的常数 |
| 原稿的平滑极限论证 | 原稿未证明；本次已删除该依赖 |
| 真残差 $\rho=\|F(x,p)\|$ 的 $d\leq3\rho^2$ | 成立；没有替换为代理残差 |
| $R=10^{-6},L=1/2,\bar t=1,\kappa=1/4$ | 全部满足 (A1)–(A4) |
| 留域条件 | $U=X$，补集为空，条件自动成立 |
| $\gamma=1/2$ 的最优性 | 是最大局部 Hölder 指数；任何 $\gamma>1/2$ 失败 |
| 误差界幂次 $2$ 的最优性 | 不能改成任何更大幂次 |
| $4^{-j}$ 距离和 $2^{-j}$ 尾项因子 | 保守上界，不是轨道的精确渐近速度 |

## 1. 完整图像块及全局近端求解

在 $X=\mathbb R^2\times\mathbb R^2$ 上令

$$
F(x,p)=(-h(p),g(x)+99p),\qquad
h(p)=p/\sqrt{\|p\|}\ (p\ne0),\quad h(0)=0,
$$

$$
g(x)=(\operatorname{sgn}(x_1)\sqrt{|x_1|},0),\qquad
S=\{((0,s),0):s\in\mathbb R\}.
$$

正确且足够的完整局部化是

$$
U=X,\quad U_R=\{z:d(z,S)\leq R\},\qquad
\mathcal G_R=\{(y,F(y)):y+F(y)\in U_R\}.
$$

该定义保留 $U_R$ 中每个近端输入的全部输出，没有删去不方便的点对。

写输入为 $(a,b)$、输出为 $(x,p)$，原方程等价于

$$
x=a+h(p),\qquad b=g(x)+100p.
$$

由于 $k^*(v)=\|v\|^3/3$，考虑

$$
\Phi_{a,b}(u)=\frac13\|u-a\|^3+\frac1{100}f(u)
-\frac1{100}\langle b,u\rangle.
$$

三次范数项严格凸且支配线性项，$f$ 凸且非负，所以 $\Phi_{a,b}$ 严格凸、强制并有唯一极小点 $x$。其一阶条件与
$p=\nabla k^*(x-a)=\|x-a\|(x-a)$ 共同给出原近端方程。这证明 $J_F$ 在整个空间存在且唯一。最近零点为 $((0,a_2),0)$，且每个 $s\in S$ 的零图像点都属于 $\mathcal G_R$，故 (A1) 成立。

## 2. 输出动量确实足够小

输入属于 $U_R$ 时，$|a_1|\leq R$、$\|b\|\leq R$，令 $P=\|p\|$。

若 $p_1g_1(x_1)\geq0$，展开 $\|g(x)+100p\|^2$ 得 $100P\leq\|b\|\leq R$。若符号相反，$x_1=a_1+p_1/\sqrt P$ 与 $p_1$ 异号，因而

$$
|p_1|\leq R\sqrt P,\qquad |p_2|=|b_2|/100\leq R/100,
\qquad P^2\leq R^2P+R^2/10000.
$$

如果 $P>R$，则
$P^2-R^2P>R^2(1-R)>R^2/10000$，矛盾。故 $P\leq R$。这里 $R=10^{-6}$；负号情形必有 $P>0$，其他情形已包含 $p=0$。原稿给出的动量范围成立，但“仍推出”的一步宜展开上述二次不等式。

## 3. 原稿 Jacobian 界及缺口

在 $p=(q,r)\ne0$ 时，

$$
A=\partial_qh_1=\frac{q^2+2r^2}{2(q^2+r^2)^{5/4}},\qquad
B=\partial_rh_1=-\frac{qr}{2(q^2+r^2)^{5/4}}.
$$

若 $\|p\|\leq R$，则

$$
A\geq\frac1{2\sqrt R},\qquad
\frac{|B|}{A}=\frac{|qr|}{q^2+2r^2}
\leq\beta:=\frac{\sqrt2}{4}.
$$

在 $x_1\ne0$ 时，隐式求导的分母是 $100+g_1'(x_1)A>0$，给出

$$
|\partial_{a_1}q|\leq2\sqrt R,\qquad
|\partial_{b_1}q|\leq1/100,\qquad
|\partial_{b_2}q|\leq\beta/100.
$$

$p_2=b_2/100$，其余无关导数为零。可微点上的 Jacobian 范数至多为

$$
K_R=\sqrt{4R+\frac{2+\beta^2}{10000}},\qquad
K_R^2=0.0002165<0.015^2<0.02^2.
$$

这些计算本身正确。但原稿没有指定平滑函数，也没有证明平滑问题的动量范围、导数界、唯一性及极限返回原近端解。特别是在 $p=0$、$x_1=0$ 处不能直接套用经典隐式求导。以下有限差分论证完整恢复结论，不必假定某种平滑满足全部条件。

## 4. 不作平滑的有限差分证明

对于球 $\|p\|,\|\widetilde p\|\leq R$ 中两点，若
$\Delta q=q-\widetilde q\geq\beta|r-\widetilde r|$，则有割线不等式

$$
h_1(p)-h_1(\widetilde p)
\geq\frac{\Delta q-\beta|\Delta r|}{2\sqrt R}.
$$

证明沿原动量线段 $p_\tau=\widetilde p+\tau(p-\widetilde p)$ 使用已展示的 $A,B$ 公式。球的凸性保证 $\|p_\tau\|\leq R$，非零点上有

$$
\frac d{d\tau}h_1(p_\tau)=A\Delta q+B\Delta r
\geq\frac{\Delta q-\beta|\Delta r|}{2\sqrt R}.
$$

若线段经过原点 $\tau_0$，写 $v=p-\widetilde p\ne0$，则原函数本身满足精确公式

$$
h_1(p_\tau)=\operatorname{sgn}(\tau-\tau_0)
\sqrt{|\tau-\tau_0|}\,\frac{v_1}{\sqrt{\|v\|}}.
$$

因此它连续，原点两侧微积分基本定理的差分可直接拼接。具体地，先删去原点附近长度为 $\varepsilon$ 的区间，再用精确公式让端点值趋于零，得到完整线段上的不等式。端点为原点时只删去一侧区间；两个端点均为原点时显然。这个极限是原函数的明确端点计算，不是平滑正则化或未证收敛。

用 $g_1$ 的严格递增性比较两个近端方程。若 $\Delta q>0$ 同时严格大于
$|\Delta b_1|/100$ 和 $2\sqrt R|\Delta a_1|+\beta|\Delta p_2|$，割线不等式给出 $\Delta x_1>0$，故 $\Delta g_1>0$。但第二近端方程又给出
$\Delta g_1=\Delta b_1-100\Delta q<0$，矛盾。交换两点处理负号，并用 $\Delta p_2=\Delta b_2/100$，得到

$$
|\Delta p_1|\leq
\max\left\{\frac{|\Delta b_1|}{100},
2\sqrt R|\Delta a_1|+\frac\beta{100}|\Delta b_2|\right\}.
$$

这里只需 $g_1$ 严格递增，在 $x_1=0$ 和跨越零点时完全适用。再用 Cauchy–Schwarz 得

$$
\|\Delta p\|\leq K_R\|(a,b)-(\widetilde a,\widetilde b)\|
\leq0.02\|(a,b)-(\widetilde a,\widetilde b)\|.
$$

## 5. All-pair RL、真残差 EB、相容与留域

动能梯度具有全局界
$\|h(p)-h(\widetilde p)\|^2\leq2\|p-\widetilde p\|$。
完全代数的证明如下：写 $u=h(p),v=h(\widetilde p)$，则
$p=\|u\|u$、$\widetilde p=\|v\|v$，并有

$$
\langle p-\widetilde p,u-v\rangle
=\frac{\|u\|+\|v\|}{2}
\left(\|u-v\|^2+(\|u\|-\|v\|)^2\right)
\geq\frac12\|u-v\|^3.
$$

Cauchy–Schwarz 立即给出所需界，包括零向量。

记 $C=2J_F-I$，则 $C(a,b)=(a+2h(p),2p-b)$。对任意两个 $U_R$ 中输入，距离 $\delta\leq R$ 时，

$$
\|\Delta C\|\leq2\sqrt{0.04\delta}+1.04\delta
\leq0.40104\sqrt\delta\leq\frac12\delta^{1/2}.
$$

RL 图像定义恰好等价于该反射预解式界，因此 (A2) 对全部允许图像点对成立，不限于轨道点或零点比较。

$F$ 单值，真残差准确地是

$$
\rho^2=\|p\|+\|g(x)+99p\|^2.
$$

由 $\|p\|\leq R$ 得 $\|p\|\leq\rho^2$、
$\|g(x)\|\leq(1+99\sqrt R)\rho$，于是

$$
d((x,p),S)=\sqrt{|x_1|^2+\|p\|^2}
\leq|x_1|+\|p\|
\leq((1+99\sqrt R)^2+1)\rho^2
=2.207801\rho^2\leq3\rho^2.
$$

零残差时输出属于 $S$，不等式仍成立。另因
$g(x)+99p=b-p$，整个输出块满足 $\rho^2\leq R+4R^2<1$。
残差区间条件是 $(R+L\sqrt R)/2=0.0002505<\bar t=1$。直接相容性为

$$
\sup_{0<r\leq R}\frac{\psi((r+L\sqrt r)/2)}r
=\frac34(0.501)^2=0.18825075<\frac14.
$$

故 (A3)–(A4) 均成立。$U=X$、
$d(z^0,\varnothing)=+\infty$，留域条件自动满足；距离递推保证每一步继续属于 $U_R$。

## 6. 指数最优性与实际速度

取 $w_t=((0,0),(0,t))$，$0<t\leq R$。有

$$
J_F(w_t)=((0,\sqrt{t/100}),(0,t/100)),\qquad
\|C(w_t)-C(0)\|^2=t/25+(49t/50)^2.
$$

对任何 $\gamma>1/2$，

$$
\frac{\|C(w_t)-C(0)\|}{\|w_t\|^\gamma}
\geq\frac15t^{1/2-\gamma}\longrightarrow+\infty.
$$

所以 $\gamma=1/2$ 是最大指数，不仅是排除了 Lipschitz。
$1/2$ 阶统一常数的极限下界至少是 $1/5$；本审查不主张
$L=1/2$ 或 $L=1/5$ 是固定半径上的最佳常数。

误差界幂次也最优：取输出 $y_t=((t^2,0),0)$，则
$\rho=t$、$d=t^2$。对应输入 $((t^2,0),(t,0))$ 在充分小 $t$ 时属于 $U_R$，故不能把 $3\rho^2$ 改成 $K\rho^{2+\varepsilon}$。

主定理给出

$$
d(z^j,S)\leq4^{-j}d_0,\qquad
\|z^j-z^\infty\|\leq\frac23 4^{-j}d_0+\frac12 2^{-j}\sqrt{d_0}.
$$

这些确实是上界，不能被描述为每条轨道精确的线性收敛因子或尾项阶。例如初值 $z^0=w_t$ 的整条轨道为

$$
z^j=\left(\left(0,\frac{\sqrt t}{9}(1-10^{-j})\right),
(0,100^{-j}t)\right),\qquad z^\infty=((0,\sqrt t/9),0).
$$

实际距离为 $100^{-j}t$，实际尾项是

$$
\left(\frac{t}{81}100^{-j}+t^2 10000^{-j}\right)^{1/2},
$$

明显快于一般定理给出的估计。

## 7. 本次文件与验证

已新写两个论文文件，没有修改原始投稿包或其他 agent 的文件：

- RLEB/sections/verification_example.tex：明确完整图像块、补齐动量范围、使用有限差分、说明真残差与留域，注明速度只是上界，并增加最大 Hölder 指数结论。
- RLEB/sections/appendix_hamilton.tex：完整有限差分证明、零点处理、动能梯度 Hölder 界、两类幂次最优性及显式轨道。

整合时请在 RLEB/main.tex 的附录部分加入
$\verb|\input{sections/appendix_hamilton}|$。本 agent 按分工未修改 main.tex。

已完成标签、引用和花括号的静态检查，两个论文文件内部引用均可解析且没有重复标签。尝试用 XeLaTeX 编译独立检查稿时，系统缺少 xelatex.fmt，且 latex.ltx、fontspec.sty、xeCJK.sty 也不可检索；因此本 agent 未完成排版编译验证。

第一轮审查只独立验证了能量比值发散、局部 Lipschitz 失败两个代数事实；随后为规范正文补核了外部原文，见下一节。本次论文正文只保留直接可证的条件比较，不借这些比较宣称排除了文献中的所有方法。

## 8. 规范正文与版本补核（2026-10-11）

新增可独立重建的规范正文 research/canonical/rank_deficient_hamilton_rleb.md，准备以 C241 登记。它在同一页补齐全部定义、全局覆盖、两点有限差分及零点细节、全部点对 RL、真残差 EB、标量相容、留域和有限长度证明，并明确幂次最优性与实际轨道速度的区别。四个固定锚点是 hrl-object、hrl-proof、hrl-sharpness、hrl-comparison。

已直接核读以下原文：

- Maddison、Paulin、Teh、O'Donoghue、Doucet，Hamiltonian Descent Methods，[arXiv:1809.05042v1](https://arxiv.org/abs/1809.05042v1)。提交日期 2018-09-13，PDF 题页日期 2018-09-14。隐式更新是 §3.1 式 (33)–(34)，能量配对是 B.1 式 (35)，隐式收敛结果是 Proposition 3.2。它另要求 Assumptions A 中的唯一最小点和 $(0,1)$ 内阻尼，并限制步长及零初始动量；本例的秩亏最小点直线、阻尼 99 和可允许非零初始动量均不能被忽略。结论是该固定版本的命题不能直接应用，不是所有 Hamilton 研究均失效。
- Luke、Tam，Generalized Monotonicity and the Proximal Point Algorithm，[DOI 10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863)，Articles in Advance 版，2025-11-21 发布，pp. 1–13。Definition 2 式 (10) 是二次 Minty 条件，Proposition 3 给出二次能量等价式，Proposition 4 对其受限图像和输入域在 $\tau<1/2$ 下给出反射预解式 Lipschitz 等价性。规范正文只在相同完整图像上排除明确写出的有限二次能量、固定零点近端 Lipschitz、有限二次 Minty 三种证书。

规范正文没有作新颖性认证，也不修改根 CLAIMS、state、graph。本轮没有再修改已进入终审的两个论文 TeX 文件。
