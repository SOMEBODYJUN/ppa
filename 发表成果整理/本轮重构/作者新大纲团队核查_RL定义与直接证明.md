# 作者新大纲团队核查：RL 定义与直接证明

本报告只核查作者本轮大纲中的定义、一步引理和 PPA 前件，不改主稿或总大纲。结论是：**一般模 RL 可以从算子图上的内积不等式定义；一步引理可以只用近端包含、内积展开与 Cauchy–Schwarz 完整证明。** 但全对图 RL 与到最近零点的锚比较不能合并命名；前者强制所表示的近端纤维单值，后者允许严格多值。

采用仓库 `academic-writing-skills` 的数学证明审查模式。数学来源为现行 `research/canonical/true_residual_selection_rleb.md`、`research/canonical/general_modulus_dynamics.md` 与 `发表成果整理/RLEB/sections/theorem_spine.tex`；下文将既有命题改写为直接证明，不登记新命题或作新颖性判断。

## 1. 可直接放入前置知识的一般模算子 RL 定义

固定 $X=\mathbb R^n$（$n\ge1$，Euclidean 内积与范数）、关系 $F:X\rightrightarrows X$、参数 $\lambda>0$、尺度 $R>0$ 及图块 $\mathcal G\subset\operatorname{gph}F$。取有限非减函数 $\omega:[0,R]\to[0,\infty)$，满足 $\omega(0)=0$ 且在零处右连续。

**定义（一般模 RL 次单调性）。** 称图块 $\mathcal G$ 在参数 $\lambda$ 和尺度 $R$ 上满足一般模 RL 条件，若对每一对

\[
(u,u^*),(v,v^*)\in\mathcal G,
\qquad
\delta:=\|u-v+\lambda(u^*-v^*)\|\le R,
\]

均有

\[
\boxed{\quad
\lambda\langle u-v,u^*-v^*\rangle
\ge\frac14\bigl(\delta^2-\omega(\delta)^2\bigr).
\quad} \tag{D-RL}
\]

取 $\mathcal G=\operatorname{gph}F$ 时，称 $F$ 满足该全图条件；否则只能称所给图块满足条件。这里的尺度是显示的**输入组合对距** $\delta$，不能换成 $\|u-v\|$。同一图块内的跨分支点对，以及 $\delta=0$ 的点对，全部在量词中。取 $\omega(t)=Lt^\gamma$（$L\ge0, 0<\gamma\le1$），得到幂次 RL；取 $\omega(t)=t$，得到测试点对上的通常单调性不等式。

此定义既不以近端映射定义理论，也不依赖反射映射。一般模的全局连续性、凹性或严格递增性不是这一定义或下面一步证明的必需前件；零处连续性保留为统一的模约定，后续若需要连续动力学应另核其相应前件。

定义之后再介绍算法对象：

\[
J_{\lambda F}(x):=\{y:(x-y)/\lambda\in F(y)\},
\qquad
r_F(y):=\inf_{q\in F(y)}\|q\|.
\]

空纤维的真残差取 $+\infty$。固定非空闭集 $S\subset\operatorname{zer}F$，令

\[
d(x):=d(x,S),\qquad
P_S(x):=\{p\in S:\|x-p\|=d(x)\}.
\]

有限维、非空及闭性保证每个 $P_S(x)$ 非空；无需 $S$ 是完整零集，也无需最近点唯一。

## 2. 可直接放在定义之后的一步引理与短完整证明

**引理（一般模近端步的一步估计）。** 沿用上述 $X,F,S,\lambda,R,\omega$。取 $x,y\in X$，设

\[
(x-y)/\lambda\in F(y),\quad
0\le d:=d(x)\le R,\quad
s:=\|x-y\|,\quad d^+:=d(y).
\]

假设存在 $p\in P_S(x)$ 使

\[
\boxed{\quad
\langle y-p,x-y\rangle
\ge\frac14\bigl(d^2-\omega(d)^2\bigr).
\quad} \tag{A}
\]

定义 $B(t):=(t+\omega(t))/2$。再设 $\bar t>0$，$\psi:[0,\bar t]\to[0,\infty)$ 有限非减，并且

\[
\frac{B(R)}\lambda\le\bar t,\qquad
r_F(y)\le\bar t\ \Longrightarrow\ d(y)\le\psi(r_F(y)). \tag{W-EB}
\]

则

\[
\boxed{
(d^+)^2+s^2\le\frac{d^2+\omega(d)^2}{2},\qquad
(2s-d)^2\le\omega(d)^2,\qquad s\le B(d),
} \tag{E}
\]

以及

\[
0\le r_F(y)\le s/\lambda\le B(d)/\lambda\le\bar t,
\qquad
\boxed{\ d^+\le\psi(r_F(y))\le\psi(s/\lambda)
\le\psi(B(d)/\lambda).\ } \tag{R}
\]

若进一步对全部 $0<t\le R$ 有 $\psi(B(t)/\lambda)\le\kappa t$，其中 $0<\kappa<1$，则 $d^+\le\kappa d$。当 $d=0$ 时，全部满足前件的输出均为 $y=x$。

**证明。** 因为 $\|x-p\|=d$，内积展开与 (A) 给

\[
\|y-p\|^2+s^2
=d^2-2\langle y-p,x-y\rangle
\le\frac{d^2+\omega(d)^2}{2}.
\]

结合 $d^+\le\|y-p\|$，得到能量估计。另一方面，Cauchy–Schwarz 给

\[
s^2+\frac{d^2-\omega(d)^2}{4}
\le s^2+\langle y-p,x-y\rangle
=\langle x-p,x-y\rangle\le ds.
\]

乘以 $4$ 后配方，得到 $(2s-d)^2\le\omega(d)^2$，因而 $s\le B(d)$。真实近端包含给

\[
r_F(y)\le\|(x-y)/\lambda\|=s/\lambda
\le B(d)/\lambda\le B(R)/\lambda\le\bar t.
\]

故真残差误差界适用于这个实际输出；$\psi$ 非减给 (R)。当 $d>0$ 时再用标量兼容。若 $d=0$，则 $p=x$，(A) 直接成为 $-s^2\ge0$，故 $y=x$、$d^+=0$。□

这个证明没有把真残差与所选图值范数相等同，也没有要求真残差下确界取到。引理仅以当前输入 $x$ 为合法点；不预先假设输出 $y$ 留在输入工作域。

## 3. 全对图定义如何验证锚前件，以及不能省略的范围差别

若 $\mathcal G$ 满足 (D-RL)，某输出的实际近端图点

\[
\bigl(y,(x-y)/\lambda\bigr)\in\mathcal G,
\]

且存在最近零点 $p\in P_S(x)$ 使 $(p,0)\in\mathcal G$，则这对图点的测试尺度为

\[
\|y-p+\lambda((x-y)/\lambda)\|=\|x-p\|=d(x)\le R.
\]

将该点对代入 (D-RL) 就得到 (A)。这是一条充分验证桥；近端覆盖、真 EB、评价窗、兼容、可和长度与留域预算仍须另核。锚点须是**当前输入**的最近零点；换成输出的最近零点，便不能直接得到测试尺度 $d(x)$。

全对图条件还比较同一个输入所对应的两个输出。若

\[
(u,(x-u)/\lambda),(v,(x-v)/\lambda)\in\mathcal G,
\]

则 $\delta=0$，(D-RL) 的左端为 $-\|u-v\|^2$，右端为零，因此 $u=v$。这是图块内唯一性；它既不保证该输入有输出，也不排除完整图在图块之外有其他输出。

因此大纲应明确采用下列一种主定理身份：

| 主定理前件 | 覆盖的对象与结论 | 严格多值是否可能 |
| --- | --- | --- |
| 同一图块全对 (D-RL)，加近端输入覆盖、图块内最近零锚及其余同窗前件 | 所表示图块的唯一近端轨道 | 图块内不可能；完整图在图块之外仍可能 |
| 同一个允许近端关系的每个输出满足 (A)，加 coverage 及其余同窗前件 | 每条允许选择的轨道 | 可能 |
| 完整 $J_{\lambda F}$ 的每个输出直接满足 (A)，加完整 coverage 及其余同窗前件 | 完整 PPA 的全部选择 | 可能 |

建议保留一般模算子全对 RL 为前置定义，主定理2则明确以逐允许输出的锚条件 (A) 为前件，并将全对 RL 放在其后作为充分验证条件。这样既保持算子图为理论起点，也保留现有真残差多选择定理的数学范围。若作者决定主定理2仅采用全对 RL，则严格多值实例只能归于另外陈述的锚版本，不能作为该全对定理的实例。

## 4. 主定理2必须保留的全部 PPA 前件与有限前缀步骤

为便于大纲直接采用，下面列出同一对象上的完整合取；其中每个“全部输出”都指同一个允许近端关系 $\mathcal J$。

1. **对象与参数。** $X=\mathbb R^n$，$n\ge1$，$F:X\rightrightarrows X$，$\lambda>0$，$S\subset\operatorname{zer}F$ 非空闭，$U\subset X$ 开，$R,\bar t>0$，$0<\kappa<1$。$U_R:=\{x\in U:d(x)\le R\}$。空集距离为 $+\infty$，所以 $U=X$ 时留域距离无限。
2. **两个模。** $\omega:[0,R]\to[0,\infty)$、$\psi:[0,\bar t]\to[0,\infty)$ 有限非减、零处连续且零处为零。定义 $B(t)=(t+\omega(t))/2$。
3. **近端输入覆盖。** 对每个 $x\in U_R$，$\varnothing\ne\mathcal J(x)\subset J_{\lambda F}(x)$。覆盖由前件供应，不能从 RL、单值性、闭图或原算子全定义域推出。
4. **逐输出最近零锚。** 对每个 $x\in U_R$ 及每个 $y\in\mathcal J(x)$，存在 $p\in P_S(x)$ 使 (A) 成立；$p$ 可以随输出变化。
5. **完整原关系的真输出 EB 与评价窗。** 对每个 $y\in\mathcal J(U_R)$，若 $r_F(y)\le\bar t$，则 $d(y)\le\psi(r_F(y))$；并有 $B(R)/\lambda\le\bar t$。这里 EB 须覆盖实际输出，即使其留在 $U$ 仍未证明。若只在 $U$ 上有 EB，应先另证输出落入 EB 域，不可循环援引后续留域结论。
6. **同尺度标量兼容。** $\psi(B(t)/\lambda)\le\kappa t$ 对每个 $0<t\le R$ 成立。
7. **可和长度。** $\Theta(R)<\infty$，其中 $\Theta(t):=\sum_{j\ge0}B(\kappa^jt)$。在上述有限非减模下，这等价于 Dini 条件 $\int_0^R\omega(t)\,dt/t<\infty$；不需要另加幂次上界。
8. **初值与严格留域预算。** $x^0\in U_R$，$d_0=d(x^0)$，且 $\Theta(d_0)<d(x^0,X\setminus U)$。

主定理证明可以直接调用第2节一步引理，但必须保留下面的有限前缀归纳：coverage 先产生当前一步；一步引理给 $d_{k+1}\le\kappa d_k$ 与步长 $\le B(d_k)$。对已构造的任意有限前缀，

\[
d_{k+1}\le\kappa^{k+1}d_0,
\qquad
\|x^{k+1}-x^0\|
\le\sum_{j=0}^k B(\kappa^jd_0)
\le\Theta(d_0)<d(x^0,X\setminus U).
\]

因此新的输出确实属于 $U_R$，coverage 可再次使用，轨道得以无限继续。随后才由可和步长、完备性与 $S$ 闭性推出有限长度、Cauchy 性及 $x^\infty\in S\cap U$，并从第 $k$ 步起求和得到

\[
\|x^\infty-x^k\|\le\Theta(d_k)
\le\Theta(\kappa^k d_0).
\]

若取 $\mathcal J=J_{\lambda F}$，以上量词必须逐完整输出核查；若采用图块关系，则不能只凭包含 $J_{\mathcal G}\subset J_{\lambda F}$ 把结论扩大为完整 PPA 的全部选择。幂次推论取 $\omega(t)=Lt^\gamma$ 后，$\Theta(t)=\tfrac12[t/(1-\kappa)+Lt^\gamma/(1-\kappa^\gamma)]$，再接补充假设3与 GPPA；一般核或新度量的前件不应提前隐含进入本引理。

## 5. 严格多值实例的直接核算与拒绝全对 RL 的见证

沿用既有实例 $F(y)=\{2y,3y\}\subset\mathbb R$、$\lambda=1$、$S=\{0\}$、$U=\mathbb R$，完整近端为

\[
J_F(x)=\{x/3,x/4\}.
\]

取 $R=\bar t=1$、$\omega(t)=t/2$、$\psi(t)=t/2$、$\kappa=3/8$。最近零点为 $p=0$。令 $y=cx$，两分支 $c=1/3,1/4$ 分别有

\[
\langle y,x-y\rangle=c(1-c)x^2
=\frac29x^2\quad\hbox{或}\quad\frac3{16}x^2
\ge\frac3{16}x^2
=\frac14\bigl(d^2-\omega(d)^2\bigr).
\]

因此逐完整输出的锚条件成立。完整真残差为 $r_F(y)=2|y|$，EB 取等；合法输出真残差不超过 $2/3$。评价窗上界为 $B(1)=3/4\le1$，标量组合为 $\psi(B(t))=3t/8$。覆盖全域、留域预算自动成立。

然而对同一非零输入 $x$，图点 $(x/3,2x/3)$ 与 $(x/4,3x/4)$ 的测试对距为零，且

\[
\left\langle\frac{x}{3}-\frac{x}{4},\frac{2x}{3}-\frac{3x}{4}\right\rangle
=-\frac{x^2}{144}<0.
\]

任何满足 $\omega(0)=0$ 的全对 (D-RL) 在这对点上要求左端非负，故失败。这是精确的严格多值见证；其有效性属于锚条件版本，不属于全对 RL 版本。

## 6. 反算记录、来源层级与本次验收范围

**一般证明。** 第2节由内积恒等式、Cauchy–Schwarz、非减性及真实近端包含逐行推出，属于现有一步结论的直接改写；第4节保留现有 PPA 的覆盖、有限前缀和留域逻辑。没有外部定理导入。

**机器反算。** 系统 Python 与主运行时 Python 初始均未发现 SymPy；共享环境 `/workspace/scratch/cabc4e00b63a/ppa_math_deps` 提供 SymPy 1.14.0 后，实际执行

```bash
PYTHONPATH=/workspace/scratch/cabc4e00b63a/ppa_math_deps python3 - <<'PY'
import sympy as sp
x1,x2,y1,y2,p1,p2=sp.symbols('x1 x2 y1 y2 p1 p2', real=True)
x=sp.Matrix([x1,x2]); y=sp.Matrix([y1,y2]); p=sp.Matrix([p1,p2])
inner=(y-p).dot(x-y)
d2=(x-p).dot(x-p); s2=(x-y).dot(x-y)
print(sp.expand((y-p).dot(y-p)+s2-d2+2*inner))
print(sp.expand((x-p).dot(x-y)-s2-inner))
d,s,w=sp.symbols('d s w', nonnegative=True)
print(sp.expand(4*(s**2-d*s)+d**2-w**2-((2*s-d)**2-w**2)))
PY
```

三个输出均为 `0`。独立用 Python `Fraction` 对多项式系数精确展开及多值例有理系数反算：两分支锚式裕量分别为 $5/144$、$0$；同输入对距为 $0$；全对左端系数为 $-1/144$；窗口上界 $3/4$、真残差系数 $2/3,1/2$、兼容因子 $3/8$。这些计算核验恒等式和指定例的常数，不代替第2节一般证明。

**独立代数审读。** 子代理独立确认两项直接推导、$d=0$ 驻定、真残差仅需上界而不需取到，以及 EB 必须覆盖尚未证明留域的实际输出。其审读没有扩大到外部文献或任意 Hilbert 空间。

**本次候选核查。** 对第1–5节的实际候选核过对象先于定义、定义先于调用、全对与锚条件量词、当前输入最近点、空纤维残差、完整纤维门、零距离、有限前缀和严格预算。第2节证明只使用原始点、近端包含、内积及范数，没有辅助反射对象。报告不涉及主稿版式、期刊格式或 GPPA 后续结论的数学验收。
