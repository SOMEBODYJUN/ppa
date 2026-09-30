# RL foundations 独立结构审稿：moving anchor、alignment 与 sharpness

> 审稿任务：RL-FND-REF-STRUCT-06  
> 审查对象：work/rl_foundations_anchor_theorems.md 与
> work/rl_foundations_alignment_sharpness.md  
> 审查边界：不改原文件；不采用原作者的 verdict；不作任何文献或新颖性判断。

## 0. 总结性裁决

**数学总裁决：CONDITIONAL PASS。** 两份稿件的核心代数结构可以保留：

- moving-anchor 的比值界和 reflection-defect 常数正确；
- fixed-anchor 的 power equivalence、rescaled-gauge equivalence 以及
  dilation-stability 限制正确；
- full residual 与 branchwise residual 的逻辑方向正确；
- isolated zero 下的 resolvent \(q\)-flatness、球不变性和 upper
  \(Q\)-recurrence 正确；
- alignment/drift profile 不以目标收敛率定义，因而不是定义性循环；
- gauge composition 与 \(\theta q\) upper exponent 正确；
- joint saturation criterion 正确；
- GX-071、GX-072、GX-073 的核心 verdict 均经独立计算成立。

但是，在并入最终 foundation 前必须修复下列字面定理缺口：

1. Theorem 3.1 的 approximate projection set 必须显式假设非空；
   “\(e=o(t)\) is sufficient” 只能指小量条件 (3.2)，不能自动保证
   \(P_S^{e(t)}(Jx)\ne\varnothing\)。特别地，\(e\equiv0\) 是 \(o(t)\)，
   但非 proximinal 的 \(S\) 未必存在 exact projection。
2. GX-072 必须定义 \(h(0)=0\)，GX-073 必须定义 \(R(0)=0\)；否则两个对象
   在最关键的基点处字面上未定义。
3. 所有 envelope 定理必须统一声明 exact projections 在整个取 supremum 的
   input family 上存在、空 supremum 取 \(0\)、且 gauge 的参数仍在其定义域内。
4. Proposition 4.3 必须在自身陈述中重写 \(q>1\)、轨道来自 Theorem 4.1 的
   invariant branch、\(w_k\to0\)；不能只依赖章节上下文。

未发现推翻核心框架的 critical algebraic error。

## 1. 严重性清单

### 1.1 Critical

无。

### 1.2 Major

| ID | 位置 | 问题 | 为什么是实质问题 | 必需修复 |
|---|---|---|---|---|
| STR-M01 | alignment, Theorem 3.1 及其后一句 | 未假设 \(P_S^{e(\lVert w\rVert)}(Jx)\ne\varnothing\)，却使用 \(a_{J,e}\) 并把 \(e=o(t)\) 称作充分 | 若 \(e(t)=0\) 且 \(S\) 非 proximinal，则集合可为空，\(a_{J,e}\) 为未定义或 \(+\infty\)，而 \(\psi(+\infty)\) 不在局部 gauge 的定义域 | 对每个 attained \(t>0\) 假设该集合非空；一个无需 proximinality 的易检条件是 \(e(t)>0\)。将结论改成：“\(e=o(t)\) 保证 (3.2)；再加非空性才得到 (3.3)” |
| STR-M02 | GX-072 (6.1), GX-073 (7.1) | \(h(x)=|x|^q\sin(|x|^{-\beta})\) 与 \(R(x)=P_\alpha(x)[2+\sin(|x|^{-\beta})]\) 在 \(0\) 未定义 | 后续 homeomorphism、fixed point、solution set 及 orbit 全部以 \(0\) 为基点 | 分别显式增加 \(h(0):=0\)、\(R(0):=0\) |

### 1.3 Moderate

| ID | 位置 | 问题 | 修复 |
|---|---|---|---|
| STR-D01 | alignment, Definitions 1.1--1.2 与 Theorem 2.1 的 envelopes | pointwise exact projection existence 与整个 supremum family 上的 uniform existence 没有完全区分 | 在定义 \(\mathcal A_J,\Delta_J,\chi_J,\Omega_J\) 前声明：对所有被取 supremum 的 \(x\)，相应 \(P_S(x),P_S(Jx)\) 非空 |
| STR-D02 | alignment, (2.4) | \(\mathcal A_J(r)=+\infty\) 或 \(2\mathcal A_J(r)/\lambda\) 超出局部 gauge 定义域时，右端无意义；\(\Omega_J\) 的 empty-sup convention 未打印 | 局部缩小到 \(\mathcal A_J(r)<\lambda\eta/2\)，并规定所有非负 envelope 的空 supremum 为 \(0\) |
| STR-D03 | anchor, Proposition 3.2 | \(q\) 未在命题自身声明 | 写明 \(q>0\)；若只服务于 higher-order 章节可写 \(q>1\) |
| STR-D04 | anchor, Proposition 4.3 | \(q>1\)、\(w_k\to0\)、invariant named branch 仅从上下文继承 | 把这些假设写回命题；否则 (4.16) 不能单独推出 \(\lVert x^{k+1}-p\rVert=o(\lVert w_k\rVert)\) |
| STR-D05 | GX-072 | (6.6)--(6.7) 的 two-scale exact constant 只被宣告，没有给出序列；若把该例作为 sharpness 证据，foundation 中证据链不完整 | 打印 phase sequences 及一行渐近计算；见第 8.2 节 |
| STR-D06 | GX-073 | full residual exact linear modulus \(1\)、finite escape、(7.4)--(7.5) 中只有 finite escape 写了证明，其余关键 exactness 主要是宣告 | 并入第 8.3 节的 uniform preimage/residual argument 与 phase-sequence calculation |
| STR-D07 | GX-072 作为 regularity witness 时 | 稿件证明了 \(Jz\asymp\lVert z\rVert^q\)，但没有显式把它转成 generated \(F=J^{-1}-I\) 的 full \(q\)-subregularity | 若最终文稿给 GX-072 加 full-MSR 标签，补 \(w=z-Jz=z+o(\lVert z\rVert)\) 的两行证明；见第 8.2 节 |

### 1.4 Minor

| ID | 位置 | 问题 | 修复 |
|---|---|---|---|
| STR-N01 | GX-071--073 | 未在每个例子处重申 \(P_a(t)=\operatorname{sgn}(t)|t|^a\)；GX-071 的 generated \(F=J^{-1}-I\) 隐含 \(\lambda=1\) | 例子节首统一定义 signed power，并打印“本节 \(\lambda=1\)” |
| STR-N02 | anchor, Proposition 3.1 gauge form | 局部 gauge 只在 residual window 内定义，但命题文字看似对任意 branch value | 加 \(\lVert w\rVert<\eta\) 或声明 gauge 全局延拓 |
| STR-N03 | alignment, approximate drift prose | “proof gains only \(\varepsilon_x\)” 是正确提纲，但不是一个完整 theorem；还需 \(\varepsilon_x>0\) 或 exact projection existence | 最终 foundation 中要么删除该段，要么独立列命题并补全量词 |
| STR-N04 | GX-072/073 | “adjacent extrema” 可被误读为函数的精确临界点 | 改成“adjacent phase-extremum points”，或定义真正临界点并说明同一渐近常数 |

## 2. Moving-anchor theorem：独立重证

令

\[
a:=y-p,\qquad t:=\lambda w,\qquad
x-p=a+t,\qquad \widehat x-p=a-t.
\]

由 full residual error bound、\(r_F(y)\le\lVert w\rVert\)、\(\psi\) 单调以及
\(\varepsilon\)-nearest 条件，

\[
\lVert a\rVert\le\psi(\lVert w\rVert)+e(\lVert w\rVert)
=\delta_w\lVert t\rVert,
\qquad
\delta_w=
\frac{\psi(\lVert w\rVert)+e(\lVert w\rVert)}
{\lambda\lVert w\rVert}.
\]

若 \(\delta_w<1\)，则

\[
(1-\delta_w)\lVert t\rVert
\le\lVert a\pm t\rVert
\le(1+\delta_w)\lVert t\rVert.
\]

因此原稿 (1.5) 的上下界均正确。又

\[
\widehat x-(2p-x)=2a,
\qquad
\lVert x-p\rVert\ge(1-\delta_w)\lVert t\rVert,
\]

从而

\[
\frac{\lVert\widehat x-(2p-x)\rVert}{\lVert x-p\rVert}
\le\frac{2\delta_w}{1-\delta_w}.
\]

若 \(\psi(t)=o(t)\)、\(e(t)=o(t)\)，则 \(\delta_w\to0\)，所以 norm ratio
趋于 \(1\)，且 vector defect 为 \(o(\lVert x-p\rVert)\)。这里没有用到投影
映射的连续性、唯一性或可测性。

### 2.1 Projection existence 核查

- 若 \(e(\lVert w\rVert)>0\)，由距离的 infimum 定义必能选到
  \(\lVert y-p\rVert\le d(y,S)+e(\lVert w\rVert)\)；无需 \(S\) 闭或
  proximinal。
- 若 \(e(\lVert w\rVert)=0\)，则必须另有 \(P_S(y)\ne\varnothing\)。
- 原 anchor theorem 已经使用“choose \(p\)”作为存在性假设，且其 projection
  clause 正确；这里没有隐藏漏洞。

### 2.2 Power constants 核查

若 \(\lVert a\rVert\le A\lVert w\rVert^q\)、\(q>1\) 且
\(A\lVert w\rVert^{q-1}/\lambda\le1/2\)，则

\[
\lVert x-p\rVert\ge\frac\lambda2\lVert w\rVert,
\]

故

\[
\lVert a\rVert
\le A(2/\lambda)^q\lVert x-p\rVert^q,
\]

以及

\[
\lVert\widehat x-(2p-x)\rVert
\le 2A(2/\lambda)^q\lVert x-p\rVert^q
=\frac{2^{q+1}A}{\lambda^q}\lVert x-p\rVert^q.
\]

原稿 (1.10)--(1.11) 的 safe constants 正确，且未错误声称最优。

**Verdict：PASS。**

## 3. Fixed-anchor power/gauge equivalence：独立重证

固定 \(p\in S\)。恒等式

\[
x-p=(y-p)+\lambda w,
\qquad
\widehat x-(2p-x)=2(y-p)
\tag{3.1}
\]

是全部等价的核心。

### 3.1 Power case

若 \(\lVert y-p\rVert\le C_B\lVert w\rVert^q\)、\(q>1\)，在 graph germ
上缩小到 \(C_B\lVert w\rVert^{q-1}\le\lambda/2\)，得到

\[
\lVert x-p\rVert
\ge\lambda\lVert w\rVert-\lVert y-p\rVert
\ge\frac\lambda2\lVert w\rVert,
\]

所以 \(C_J=C_B(2/\lambda)^q\) 可用。反向若
\(\lVert y-p\rVert\le C_J\lVert x-p\rVert^q\)，缩小到
\(C_J\lVert x-p\rVert^{q-1}\le1/2\)，则

\[
\lambda\lVert w\rVert
\ge\lVert x-p\rVert-\lVert y-p\rVert
\ge\frac12\lVert x-p\rVert,
\]

所以 \(C_B=C_J(2\lambda)^q\) 可用。由 (3.1)，reflection constant 恰为
\(2C_J\)。原稿 Theorem 2.1 正确。

### 3.2 General gauge 与 dilation stability

若 \(\lVert y-p\rVert\le\beta(\lVert w\rVert)\)、\(\beta(t)=o(t)\)，则局部
\(\beta(t)\le\lambda t/2\)，从而

\[
\lVert w\rVert\le(2/\lambda)\lVert x-p\rVert,
\quad
\lVert y-p\rVert
\le\beta((2/\lambda)\lVert x-p\rVert).
\]

反向若 \(\lVert y-p\rVert\le\alpha(\lVert x-p\rVert)\)、
\(\alpha(t)=o(t)\)，则

\[
\lVert x-p\rVert\le2\lambda\lVert w\rVert,
\quad
\lVert y-p\rVert\le\alpha(2\lambda\lVert w\rVert).
\]

因此 arbitrary gauge 的正确结论确实是“rescaled gauge”，而非同一 gauge。
若 \(\psi(ct)=O(\psi(t))\) 对相关 fixed dilations 成立，才可在乘法常数意义下
恢复 same-gauge equivalence。若 dilation \(c\le1\)，单调性已给
\(\psi(ct)\le\psi(t)\)，所以只需检查大于 \(1\) 的 relevant factors。

Counterexample 2.3 也成立：其阶梯 gauge 满足 \(\psi=o(\mathrm{id})\)，而

\[
\psi(t_n)=t_{n+1},\qquad
\psi(t_n-t_n^2)=t_{n+2},\qquad
\frac{t_{n+1}}{t_{n+2}}\to\infty.
\]

在 \((y_n,w_n)=(-t_n^2,t_n)\) 上，
\(|y_n|=\psi(|w_n|)\) 但
\(|y_n|/\psi(|x_n|)\to\infty\)。该例确实排除了 arbitrary same-gauge
constant。

**Verdict：PASS。**

## 4. Full residual 与 branchwise residual：独立重证

### 4.1 Full \(\Rightarrow\) every selected branch

若 \(p\) 局部孤立，取 \(R>0\) 使
\(S\cap B(p,R)=\{p\}\)。当 \(\lVert y-p\rVert<R/2\) 时，对任意
\(s\in S\setminus\{p\}\)，

\[
\lVert y-s\rVert
\ge R-\lVert y-p\rVert
>\lVert y-p\rVert,
\]

故 \(d(y,S)=\lVert y-p\rVert\)。再由
\(r_F(y)\le\lVert w\rVert\) 得到每个 branchwise bound。Proposition 3.1
正确；gauge 版本只需把 residual window 写清。

### 4.2 Residual-complete converse

若 \(\Gamma\) 包含所有 \(y\in U\)、\(\lVert w\rVert<\eta\) 的 graph
values，且 \(\lVert y-p\rVert\le C\lVert w\rVert^q\)，则当
\(r_F(y)<\eta\) 时，可选 \(w_n\in F(y)\) 使
\(\lVert w_n\rVert\downarrow r_F(y)\)，故

\[
\lVert y-p\rVert\le C r_F(y)^q.
\]

当 \(r_F(y)\ge\eta\) 时，在 \(\lVert y-p\rVert<d_0\) 内用
\(d_0\eta^{-q}r_F(y)^q\) 即可。若 \(0\in F(y)\)，residual completeness
把 \((y,0)\) 纳入 \(\Gamma\)，branchwise bound 强制 \(y=p\)。故 isolation
确实是结论。只需补写 \(q>0\)。

Counterexample 3.3 也正确：good branch 给 \(y=|w|^q\)，但 full residual
选取 \(y^2\)，从而

\[
\frac{d(y,S)}{r_F(y)^q}=y^{1-2q}\to\infty.
\]

**Verdict：PASS after minor quantifier repair。**

## 5. Isolated-zero \(q\)-flatness、invariance 与 exact order

令 \(y=T(x)\)、\(w=(x-y)/\lambda\)。由 full \(q\)-error bound 和
isolation，

\[
\lVert y-p\rVert\le\rho\lVert w\rVert^q.
\]

若 \(\rho\lVert w\rVert^{q-1}\le\lambda/2\)，则

\[
\lVert x-p\rVert
\ge\lambda\lVert w\rVert-\lVert y-p\rVert
\ge\frac\lambda2\lVert w\rVert,
\]

所以

\[
\lVert T(x)-p\rVert
\le\rho(2/\lambda)^q\lVert x-p\rVert^q.
\tag{5.1}
\]

若 named branch 覆盖 \(\overline B(p,\delta)\)，且
\(C_q\delta^{q-1}\le\theta<1\)，则 (5.1) 直接给

\[
T(\overline B(p,\delta))
\subset B(p,\theta\delta)
\subset\overline B(p,\delta).
\]

因此 coverage 加 (5.1) 足以建立 self-map；无需 \(T\) 连续。归纳得

\[
r_{k+1}\le C_qr_k^q,
\qquad
r_k\le C_q^{(q^k-1)/(q-1)}r_0^{q^k}.
\]

这只是 upper \(Q\)-recurrence。

若 nonterminating orbit 还满足

\[
\frac{r_{k+1}}{\lVert w_k\rVert^q}
\to\mu\in(0,\infty),
\]

并明确 \(q>1\)、\(w_k\to0\)，则
\(r_{k+1}=o(\lVert w_k\rVert)\)，而

\[
x^k-p=(x^{k+1}-p)+\lambda w_k
\]

给出 \(r_k/(\lambda\lVert w_k\rVert)\to1\)。于是

\[
\frac{r_{k+1}}{r_k^q}\to\frac\mu{\lambda^q}.
\]

原结论正确，但 Proposition 4.3 必须把上述 inherited assumptions 打印在
命题内。finite termination 必须继续单列；终止后 normalized ratio 通常成为
\(0/0\)，不能被 exact-order statement 覆盖。

Gauge 版同理：

\[
\lVert T(x)-p\rVert\le\psi(\lVert w\rVert),
\quad
\lVert w\rVert\le2\lVert x-p\rVert/\lambda,
\]

故 \(\Phi(r)=\psi(2r/\lambda)=o(r)\)，小球不变且非终止轨道满足
\(r_{k+1}/r_k\to0\)。

**Verdict：PASS after standalone-assumption repair。**

## 6. Alignment/drift profile 是否循环

对 exact projections，

\[
a_J(x)=d(x,P_S(Jx)),
\qquad
\delta_J(x)=d(P_S(x),P_S(Jx))
\]

只使用 \(S,x,Jx\) 的几何，不使用 \(q\)、\(\theta q\) 或
\(d(Jx,S)^{1/q}\)，所以不是定义性循环。

独立验证 pointwise equivalence。记 \(r=d(x,S)\)。

1. \(P_S(Jx)\subset S\)，故 \(r\le a_J(x)\)。
2. 取近似达到 \(\delta_J(x)\) 的
   \(p_x\in P_S(x),p_y\in P_S(Jx)\)，则
   \(a_J(x)\le r+\delta_J(x)\)。
3. 取近似达到 \(a_J(x)\) 的 \(p_y\in P_S(Jx)\) 和任意
   \(p_x\in P_S(x)\)，则
   \(\delta_J(x)\le r+a_J(x)\)。

于是

\[
r\le a_J(x)
\le r+\delta_J(x)
\le3a_J(x).
\]

取相同 input family 的 cumulative suprema 得
\(\mathcal A_J\le\chi_J\le3\mathcal A_J\)。常数 \(3\) 安全；未声称最优。

在 superlinear error bound 下，令 \(y=Jx\)、
\(w=(x-y)/\lambda\)。对任意 output-nearest \(p\)，

\[
\big|
\lVert x-p\rVert-\lambda\lVert w\rVert
\big|
\le\lVert y-p\rVert=d(y,S).
\]

取 infimum 后

\[
|a_J(x)-\lambda\lVert w\rVert|
\le d(y,S)
\le\psi(\lVert w\rVert)
=o(\lVert w\rVert).
\]

因此 \(a_J(x)/(\lambda\lVert w\rVert)\to1\)。这说明 profile 虽非循环定义，
但加上 superlinear EB 后解析上与 step scale 等价；原稿对此限制的表述正确。

**Verdict：PASS，前提是 exact projection existence 对整个 profile domain 明示。**

## 7. Gauge composition、\(\theta q\) 与 joint saturation

### 7.1 Exact-output-anchor composition

由上式和 \(\psi(t)\le\lambda t/2\)，

\[
a_J(x)
\ge\lambda\lVert w\rVert-d(Jx,S)
\ge\frac\lambda2\lVert w\rVert.
\]

所以

\[
d(Jx,S)
\le\psi(\lVert w\rVert)
\le\psi\left(\frac{2a_J(x)}\lambda\right).
\]

再用 \(a_J(x)\le d(x,S)+\delta_J(x)\) 得 drift 版本。若
\(\mathcal A_J(r)\le Kr^\theta\) 且
\(\psi(t)=\rho t^q\)，则对每个 \(x\)，取 \(r=d(x,S)\)，得到

\[
d(Jx,S)
\le\rho(2K/\lambda)^q d(x,S)^{\theta q}.
\]

这是 uniform upper exponent；当 \(\theta q\le1\) 时它并不自动给收缩，
原稿没有越界声称收敛。

### 7.2 Approximate-output-anchor composition

若 \(P_S^{e(t)}(Jx)\ne\varnothing\)，对其每个 \(p\)，

\[
\lVert x-p\rVert
\ge\lambda t-d(Jx,S)-e(t)
\ge(1-\kappa)\lambda t.
\]

取 infimum 得

\[
t\le
\frac{a_{J,e}(x)}{(1-\kappa)\lambda},
\quad
d(Jx,S)
\le
\psi\left(
\frac{a_{J,e}(x)}{(1-\kappa)\lambda}
\right).
\]

公式本身正确；Major issue STR-M01 仅是集合非空量词漏写。建议最终陈述：

> 假设每个 attained \(t>0\) 都有
> \(P_S^{e(t)}(Jx)\ne\varnothing\)，并且
> \(\psi(t)+e(t)\le\kappa\lambda t\)。若希望不假设 proximinality，可取
> \(e(t)>0\) 且 \(e(t)=o(t)\)。

### 7.3 Joint saturation

若同一序列上

\[
a_n\asymp r_n^\theta,
\qquad
t_n\asymp a_n,
\qquad
s_n\asymp t_n^q,
\]

直接相乘得到 \(s_n\asymp r_n^{\theta q}\)。若三个 normalized ratios
分别趋于 \(A,B,C\in(0,\infty)\)，则

\[
\frac{s_n}{r_n^{\theta q}}
=\frac{s_n}{t_n^q}
 \left(\frac{t_n}{a_n}\right)^q
 \left(\frac{a_n}{r_n^\theta}\right)^q
\longrightarrow CB^qA^q.
\]

所以 marginal sharpness 在不同序列上确实不足；必须 joint saturation。

**Verdict：Theorem 2.1、Corollary 2.2、Proposition 4.1 PASS；Theorem 3.1
在修复非空性后 PASS。**

## 8. GX-071--073 独立 verdict

以下统一记 \(P_a(t)=\operatorname{sgn}(t)|t|^a\)，并取生成步长
\(\lambda=1\)。

### 8.1 GX-071：PASS，确为 exact \(\gamma q\) joint-saturation witness

令 \(\alpha=\gamma q>1\)，

\[
J(t,z)=(t+|z|^\gamma,P_\alpha z).
\]

其三角 inverse 为

\[
J^{-1}(s,u)
=(s-|u|^{1/q},P_{1/\alpha}u),
\]

故 \(F=J^{-1}-I\) 正是

\[
F(s,u)
=(-|u|^{1/q},P_{1/\alpha}u-u),
\quad
S=\mathbb R\times\{0\}.
\]

若 \(r=|z|\)，则

\[
a_J
=\sqrt{r^{2\gamma}+r^2},
\quad
\lVert w\rVert^2
=r^{2\gamma}+|z-P_\alpha z|^2,
\quad
d(Jx,S)=r^\alpha.
\]

因此

\[
\frac{a_J}{r^\gamma}\to1,
\quad
\frac{\lVert w\rVert}{a_J}\to1,
\quad
\frac{d(Jx,S)}{\lVert w\rVert^q}\to1,
\quad
\frac{d(Jx,S)}{d(x,S)^{\gamma q}}=1.
\]

这是同一 normal ray 上的 joint saturation，不只是三个 unrelated witnesses。
PPA normal recurrence 为 \(r_{k+1}=r_k^\alpha\)，故 normalized limit 恰为
\(1\)。

Reflected map 为

\[
R(t,z)
=(t+2|z|^\gamma,\,2P_\alpha z-z).
\]

在 bounded tube 上它是 \(\gamma\)-Hölder；与 \((t,0)\) 比较时

\[
\frac{\lVert R(t,z)-R(t,0)\rVert}{|z|^\gamma}
\to2,
\]

所以 maximal all-pairs exponent 确为 \(\gamma\)。

不变窗也正确。因为 \(r_k=r_0^{\alpha^k}\) 且
\(\alpha^k\ge1+k(\alpha-1)\)，

\[
\sum_{k\ge0}r_k^\gamma
\le
\frac{r_0^\gamma}
{1-r_0^{\gamma(\alpha-1)}}.
\]

初始 tangential margin 大于该和即可保持 tube；整个 rectangle 并非
self-map。

**限制 verdict：** 该例证明 attainability/minimax sharpness，不证明
genericity、necessity 或自然算法中普遍存在 \(\gamma q\)。原稿的 claim
boundary 正确。

### 8.2 GX-072：PASS after definition/proof insertion；实际 order 为 \(q\)，不是 \(\gamma q\)

先补 \(h(0)=0\)。令

\[
h(x)=|x|^q\sin(|x|^{-\beta}),
\quad
\beta=q/\gamma-1,
\quad
J(x,y)=(P_qx,P_qy+h(x)).
\]

三角结构使 \(J\) 为 global homeomorphism；局部 fixed set 仅有 \(0\)。令
\(A=|x|^q,B=|y|^q\)，则 \(|h(x)|\le A\)。若 \(B\ge2A\)，
\(|P_qy+h(x)|\ge B/2\)；若 \(B<2A\)，first coordinate \(A\) 至少是
\(\max\{A,B\}/2\)。故

\[
2^{-1-q/2}\lVert(x,y)\rVert^q
\le\lVert J(x,y)\rVert
\le\sqrt5\lVert(x,y)\rVert^q.
\]

小球不变后，每条 nonzero orbit 都满足 uniform two-sided \(Q\)-order \(q\)。
不能从这里推出 normalized ratio 存在极限，原稿没有误称。

若最终还要标注 generated \(F=J^{-1}-I\) 的 full \(q\)-MSR，则令
\(z=(x,y)\)、\(u=Jz\)、\(w=z-u\in F(u)\)。上述 upper bound 给
\(\lVert u\rVert=O(\lVert z\rVert^q)=o(\lVert z\rVert)\)，所以
\(\lVert w\rVert/\lVert z\rVert\to1\) uniformly；上述 lower bound 给
\(\lVert u\rVert\ge c\lVert w\rVert^q\)，upper bound 给相反方向。
phase-zero inputs \((x_n,0)\) 证明没有任何 exponent \(>q\)。

为补齐 all-pairs sharpness proof，可取 positive phase points

\[
s_n=2\pi n+\pi/2,
\quad
t_n=s_n+\pi,
\quad
x_n=s_n^{-1/\beta},
\quad
y_n=t_n^{-1/\beta}.
\]

则

\[
|x_n-y_n|
\sim(\pi/\beta)s_n^{-1/\beta-1},
\qquad
h(x_n)-h(y_n)
\sim2s_n^{-q/\beta}.
\]

由于 \(\gamma(1+1/\beta)=q/\beta\)，且 \(R\) 的 oscillatory coordinate
含 \(2h\)，

\[
\frac{
\lVert R(x_n,0)-R(y_n,0)\rVert
}{
|x_n-y_n|^\gamma
}
\to4(\beta/\pi)^\gamma.
\]

其余 identity 与 \(P_q\) increments 是低阶项。标准 amplitude/derivative
two-scale bound 给 \(h\in C^{0,\gamma}\)，所以 maximal exponent 正是
\(\gamma\)。

由于 \(S=\{0\}\) 局部，\(\delta_J=0\)、\(a_J=d(x,S)\)，alignment exponent
为 \(1\)。因此该例严格证明：all-pairs exponent \(\gamma\) 可以比 alignment
exponent 差，而 orbit order 为 \(q>\gamma q\)。

### 8.3 GX-073：PASS after basepoint definition/proof insertion；只是 one-step exponent

先补 \(R(0)=0\)。对 \(0<r=|x|\le\delta<1\)，记
\(c(r)=2+\sin(r^{-\beta})\in[1,3]\)。则

\[
R(x)=P_\alpha(x)c(r),
\qquad
r_+=|Jx|
=\frac{r+c(r)r^\alpha}{2}.
\]

由于 \(\alpha<1\)，

\[
\tfrac12r^\alpha
\le r_+
\le2r^\alpha,
\qquad
r_+>r.
\]

尽管 \(J\) 在 primal output coordinate 中可折叠，以 Minty input \(x\)
参数化的 graph 对每个 input 只有一个 \(Jx\)，所以它确为 natural domain
上的 exact single-valued resolvent，而非随意 selection。

Full residual 的 exact linear modulus \(1\) 可如下补证。每个 graph
representation 都满足

\[
|y|
=\frac{r+c(r)r^\alpha}{2},
\qquad
|w|
=\frac{c(r)r^\alpha-r}{2},
\]

从而 uniformly in \(c\in[1,3]\)，

\[
\frac{|y|}{|w|}
=
\frac{c(r)+r^{1-\alpha}}
{c(r)-r^{1-\alpha}}
\to1.
\]

对同一 \(y\) 的所有 local preimages 该收敛是 uniform，取 infimum
\(r_F(y)\) 后仍有 \(|y|/r_F(y)\to1\)。因此 maximal fixed-target power
exponent 是 \(1\)，endpoint modulus 是 \(1\)。

Finite escape 也成立。若 nonzero orbit 永远留在
\([-\delta,\delta]\)，其 radii 严格增加并趋于某
\(\ell\in(0,\delta]\)。因 scalar radius map 在 \(\ell>0\) 连续，必有
fixed point，亦即

\[
\ell^{1-\alpha}=c(\ell)\ge1,
\]

这与 \(\ell\le\delta<1\) 矛盾。故必在有限步离开；不存在任意小的
invariant symmetric neighborhood。不能把
\(r_+=\Theta(r^\alpha)\) 叫作 convergence order。

最后，取与第 8.2 节相同 phase points，改用 exponent \(\alpha\)。令
\(\eta_*=\alpha/(\beta+1)\)，则

\[
R(x_n)-R(y_n)
\sim2s_n^{-\alpha/\beta},
\quad
|x_n-y_n|^{\eta_*}
\sim(\pi/\beta)^{\eta_*}s_n^{-\alpha/\beta},
\]

故 normalized difference 趋于
\(2(\beta/\pi)^{\eta_*}\)。two-scale upper bound 给 maximal all-pairs
exponent \(\eta_*\)，而 anchored exponent 为 \(\alpha\)，endpoint
anchored constant 为 \(3\)。原稿 verdict 正确。

## 9. PASS 表

| 文件位置 | 独立 verdict | 合并前条件 |
|---|---|---|
| Anchor Theorem 1.1 | PASS | 保留 explicit anchor choice |
| Anchor Corollary 1.2 | PASS | \(c=0\) 时保留 projection existence clause |
| Anchor Theorem 2.1 | PASS | graph germ 必须趋于 \((p,0)\) |
| Anchor Theorem 2.2 | PASS | 保留 rescaled gauges |
| Anchor Counterexample 2.3 | PASS | 无 |
| Anchor Proposition 3.1 | PASS | gauge residual window 写清 |
| Anchor Proposition 3.2 | PASS-MINOR | 补 \(q>0\) |
| Anchor Counterexample 3.3 | PASS | 无 |
| Anchor Theorem 4.1 | PASS | named branch coverage、return window、self-map 分开 |
| Anchor Theorem 4.2 | PASS | 同上；finite termination 单列 |
| Anchor Proposition 4.3 | PASS-MODERATE | 重写 standalone assumptions |
| Anchor stress tests 5.1--5.6 | PASS | 5.6 保留 two-scale proof 或引用内部 lemma |
| Alignment Lemma 1.3 | PASS | exact projection family 非空 |
| Alignment Lemma 1.4 | PASS | \(t>0,t\to0\)；exact output projection 非空 |
| Alignment Theorem 2.1 | PASS-MODERATE | uniform projection/gauge-domain/empty-sup conventions |
| Alignment Corollary 2.2 | PASS | 只称 upper exponent |
| Alignment Proposition 2.3 | PASS | named zero branch 与 \(p_x\) coverage 明示 |
| Alignment Theorem 3.1 | REPAIR-THEN-PASS | 必修 STR-M01 |
| Alignment Proposition 4.1 | PASS | joint sequence，不得换成 marginal sequences |
| GX-071 | PASS | 明示 \(\lambda=1\) |
| GX-072 | REPAIR-THEN-PASS | \(h(0)=0\)；插入 two-scale proof |
| GX-073 | REPAIR-THEN-PASS | \(R(0)=0\)；插入 residual 与 two-scale proof |

## 10. 对最终 foundation 的最小合并指令

1. 可直接采用 moving-anchor theorem、power corollary、fixed-anchor power
   equivalence、rescaled-gauge theorem、residual-complete converse、isolated
   \(q\)-flatness、gauge-PPA、alignment/drift equivalence、exact-anchor gauge
   composition、power \(\theta q\) corollary与 joint-saturation criterion。
2. approximate-anchor theorem 必须先按 STR-M01 改写，不能原样并入。
3. exact projection 与 \(\varepsilon\)-projection 必须各有独立量词；不得用
   “take a projection” 掩盖 infinite-dimensional nonproximinality。
4. 所有 PPA 结论按“branch existence/coverage \(\to\) graph return
   \(\to\) self-map/invariance \(\to\) convergence”排序；arbitrary
   full-resolvent selection 另需 branch exclusion。
5. upper recurrence、two-sided exact order、positive normalized limit 保持三个
   不同术语。
6. GX-071 保留为 exact \(\gamma q\) sharpness witness；GX-072 保留为
   all-pairs \(\gamma\) 与 alignment \(1\) 的 separation witness；GX-073
   只作 domain/invariance guard，不得作为 convergence witness。

## Expert Contract 1.0

~~~yaml
contract_version: "1.0"
expert_skill: independent-mathematical-referee
project_id: monotonicity-regularity-seesaw-2026-09
paper_family: T
stage_id: T5
task_id: RL-FND-REF-STRUCT-06
task_status: COMPLETE
inputs_reviewed:
  - work/rl_foundations_anchor_theorems.md
  - work/rl_foundations_alignment_sharpness.md
outputs:
  - work/rl_foundations_referee_structure.md
evidence_status:
  - VERIFIED_ALG: moving-anchor ratios and reflection-defect constants independently derived
  - VERIFIED_ALG: fixed-anchor power/gauge transfers and dilation counterexample independently checked
  - VERIFIED_ALG: full-versus-branchwise residual implications independently checked
  - VERIFIED_ALG: isolated-zero flatness, invariance, gauge convergence, and exact-order criterion independently checked
  - VERIFIED_ALG: alignment/drift equivalence, gauge composition, theta-times-q, and joint saturation independently checked
  - VERIFIED_ALG: GX-071--073 formulas, branches, exponents, and invariance or escape independently checked
  - NOT_ASSESSED: literature novelty, priority, and publication placement
assumptions:
  - H is a real Hilbert space and lambda is strictly positive
  - local gauges are finite and nondecreasing on every argument actually used
  - named Minty branches return graph points inside the printed localization
  - exact projection claims are used only where the relevant projection sets are nonempty
author_input_needed: []
manual_actions: []
quality_checks:
  - did not modify either reviewed source file
  - did not trust source verdict labels
  - recalculated every displayed moving-anchor and power-transfer constant
  - stress-tested proximinality and approximate-projection existence
  - separated full residual from selected residual
  - separated branch coverage, self-map, and arbitrary-selection exclusion
  - checked empty-supremum and local-gauge domain conventions
  - separated finite termination, upper Q-order, two-sided order, and normalized limits
  - supplied explicit phase sequences for GX-072 and GX-073 sharpness
conflicts:
  - conflict_id: STR-M01
    conflict_type: missing_hypothesis
    claim: e(t)=o(t) by itself is sufficient for approximate-anchor composition without proximinality
    source_or_locator: work/rl_foundations_alignment_sharpness.md, Theorem 3.1 and following sentence
    competing_interpretations:
      - smallness condition alone also guarantees approximate-anchor existence
      - smallness guarantees inequality (3.2), while nonemptiness needs e(t)>0 or exact projection existence
    recommended_resolution: adopt the second interpretation and print nonemptiness explicitly
  - conflict_id: STR-M02
    conflict_type: basepoint_definedness
    claim: GX-072 and GX-073 formulas define maps at the zero basepoint as printed
    source_or_locator: work/rl_foundations_alignment_sharpness.md, equations (6.1) and (7.1)
    competing_interpretations:
      - zero values are implicitly understood by continuity
      - a foundational definition must explicitly set h(0)=0 and R(0)=0
    recommended_resolution: explicitly add both zero-value definitions
conflict_resolution_status: UNRESOLVED
merge_permission: orchestrator_only
recommended_next_action: repair STR-M01 and STR-M02, add the moderate quantifier clauses, then merge only the PASS rows into the first RL foundation draft
stage_acceptance_recommendation: PASS_AFTER_REPAIR
~~~
