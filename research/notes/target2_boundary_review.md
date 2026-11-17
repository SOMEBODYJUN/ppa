# 目标二边界审查：exact global PPA、KL 递推与正式版差异

日期：2026-11-17  
身份：第三席 boundary reviewer；本文件只记录边界、量词和版本审查，不修改或升级 `CLAIMS.md` 中的 C311。  
审查对象：

* `research/topics/next_stage_2026/target2_kl_finite_length.md`；
* `research/notes/target2_kl.md`；
* `research/canonical/ppa_nonlinear_gauge_and_coupled_obstruction.md#c311-kl`；
* LMZ v1 的固定抽取 `mor/paper.txt`（SHA-256 `00cd42f151df9be145541b83274db10e06e616560967d701cdfa02d1053cda92`）与 `lmz-src/main_update.tex`（SHA-256 `6a853b0f04882e5ea8a22d8e07ecdfe8144790e7017e84f097ed649caa120d5f`）。

## 1. 总裁决

没有发现会推翻当前 C311 条件版的 fatal 数学错误。普通 exact global PPA 到 LMZ Theorem 5.1 的逐项映射是成立的，但必须把下列边界持续写在规范版本中：

1. `argmin` 必须是全局精确近端点，且 `f` 使用 LMZ 所用的限制（Mordukhovich/limiting）次微分；任意满足 resolvent 根式的一步不自动提供下降比较。
2. 有界子水平集应明确写成某个实际初值层集，例如 `L(f(x^0))`（或从某个 `k_0` 开始的 `L(f(x^{k_0}))`），不能只写“相关子水平集”。
3. H3 不能由 proper+l.s.c. 自动推出。l.s.c. 给出的是 `f(\bar x)\le\liminf f(x^{k_j})`，而 H3 需要反向的 limsup 不等式；连续性或直接的 H3 检查仍是独立前件。
4. KL 递推中 `e_k` 与 `w^k` 的索引必须从 `k\ge1`（更准确地说，从进入 KL 球且 `e_{k-1}` 可用的尾部）开始。`e_{-1}` 不存在；有限前缀应单独吸收。
5. 局部递推只在 KL 球内成立；从一个聚点获得“最终留在球内”要调用 LMZ Theorem 4.3 的 bootstrap/留域论证，不能只把局部不等式直接当作全序列递推。
6. 正则化步中的第二个 `\sigma` 项确实必须保留。v1 的 A96 到三角不等式后的 A96'、以及 `H_\sigma(t)` 根方程均使用 `2\sigma`；`v=0` 必须先单独处理，不能先除以 `v^{q+1}`。

因此当前状态仍是：`C311-v1 = derived-checked`，但范围限于明确的 exact subgradient PPA 与所列 KL/下降/相对误差/H3/有界层集前件；一般 RLEB/GPPA 或无 Lyapunov 桥的多值 `F` 仍为 open。正式出版全文尚未取得，定理级版本差异不能升级为“已核”。

## 2. exact global PPA 的逐项边界

### 2.1 对象和存在性

固定 `H=R^m`、`lambda>0`、`f:H\to(-\infty,+\infty]` proper、l.s.c. 并有下界，令

\[
x^{k+1}\in P_\lambda(x^k):=\operatorname*{argmin}_y
\left\{f(y)+\frac1{2\lambda}\|y-x^k\|^2\right\}.
\]

这里必须是全局 `argmin`，而不是只满足
`x^k-x^{k+1}\in\lambda\partial f(x^{k+1})` 的任意临界根。若 `f` proper、l.s.c. 且有下界，在有限维空间中二次项使近端目标 coercive，因此每个有限值子问题的全局 minimizer 实际上存在；把“每一步选择一个有限值 global minimizer”写出来仍然有助于防止把对象误读成任意 resolvent 选择。非凸时选择可以多值，但下面的下降和 Fermat 接口对每个所选 global minimizer 都成立。

### 2.2 全局最小性给出的下降

用比较点 `y=x^k`，得到

\[
f(x^{k+1})+\frac1{2\lambda}e_k^2\le f(x^k),
\qquad e_k:=\|x^{k+1}-x^k\|.
\]

这正是 LMZ 的 `(H1')`，参数为

\[
a=\frac1{2\lambda},\qquad c=1,\qquad
\varphi(t)=t^2,
\]

其中 `\varphi` 是 increasing admissible。因为 `f` 有下界，下降式还给出
`\sum_k e_k^2<\infty`，从而 `e_k\to0`；这只供应 H1' 所需的 surrogate 极限，不供应有限长度。

### 2.3 Fermat/limiting-subgradient 接口

令

\[
h_k(y):=f(y)+\frac1{2\lambda}\|y-x^k\|^2.
\]

全局 minimizer 是局部 minimizer，因此 limiting Fermat rule 给出
`0\in\partial h_k(x^{k+1})`。对 C1 二次项使用 limiting-subdifferential 的光滑和规则，得到

\[
w_{k+1}:=\frac{x^k-x^{k+1}}\lambda\in\partial f(x^{k+1}),
\qquad
\|w_{k+1}\|=\frac1\lambda e_k.
\]

这里的 `\partial` 必须与 LMZ Definition 2.1 的 limiting/Mordukhovich 次微分一致；若换成未声明的 regular/Fréchet 次微分，边界点的 Fermat 结论不应默认为同一接口。于是 H2 可逐步取

\[
b=1/\lambda,\qquad \beta(t)=t.
\]

恒等函数 `\beta` 是 increasing admissible。该步骤只需要局部最优性加上光滑和规则，但下降式仍依赖全局比较，所以不能把 Fermat 根式替代 global PPA。

### 2.4 level-set 与 H3 的独立性

LMZ Theorem 5.1 的有界性前件是存在 `k_0` 使
`L(f(x^{k_0}))` 有界。exact PPA 的单调下降把所有后继点留在该层集；规范陈述最好直接写 `L(f(x^0))` 有界（若 `x^0\in\operatorname{dom}f`），以免“相关层集”遗漏起点或把局部 KL 层集误当作全局算法层集。

若某个迭代子列 `x^{k_j}\to\bar x`，下降性给出 `f(x^k)\downarrow\ell`。l.s.c. 只能推出

\[
f(\bar x)\le\liminf_j f(x^{k_j})=\ell.
\]

H3 才给出 `\ell\le f(\bar x)`，两者合起来才得到
`f(\bar x)=\ell`，这是 KL 证明中把能量差写成
`\vartheta(f(x^k)-f(\bar x))` 并保证非负的关键。全局连续性（或至少在相关聚点沿子列的上半连续不等式）可以验证 H3；proper+l.s.c. 本身不能替代它。

有界闭层集还保证至少存在聚点；若定理仍显式指定一个 KL 聚点 `\bar x`，应保留“该聚点处 KL”而不能把任意层集上的 KL 或某一候选驻点偷换进去。

## 3. KL 递推的索引和局部前件

### 3.1 有效索引

定义

\[
e_k=\|x^{k+1}-x^k\|,
\qquad
w^k=\frac{x^{k-1}-x^k}{\lambda}\in\partial f(x^k)
\quad(k\ge1).
\]

在进入 KL 邻域、且 `e_k>0` 的尾部，H3 与下降式先给
`f(\bar x)\le f(x^{k+1})<f(x^k)<f(\bar x)+\eta`。KL 不等式和 H2 因而给

\[
\vartheta'(f(x^k)-f(\bar x))
\ge \frac1{\|w^k\|}
\ge \frac1{b\beta(e_{k-1})}.
\]

这一步只对 `k\ge1` 有意义，并且需要 `e_{k-1}>0`。若 `e_k=0`，所需递推左侧为零而直接成立；若 `e_k>0` 但 `e_{k-1}=0`，则 exact PPA 给 `w^k=0`，与 KL 区域内 `f(x^k)>f(\bar x)` 的 KL 斜率不等式矛盾。因此在非平凡尾部可以合法除以 `e_{k-1}`，但应把这个分支写明。

下降和凹性再给

\[
\begin{aligned}
\Lambda_{k,k+1}
&:=\vartheta(f(x^k)-f(\bar x))-
  \vartheta(f(x^{k+1})-f(\bar x))\\
&\ge \vartheta'(f(x^k)-f(\bar x))\,[f(x^k)-f(x^{k+1})]\\
&\ge \frac{e_k^2}{2e_{k-1}}.
\end{aligned}
\]

于是

\[
e_k\le\sqrt{2e_{k-1}\Lambda_{k,k+1}}
\le\frac{e_{k-1}+\Lambda_{k,k+1}}{\sqrt2}.
\]

这确实给出 `\ell_1=1/\sqrt2<1`，并且 `\sum\Lambda_{k,k+1}` 在尾部望远镜。总和结论要写成“尾部 `k\ge K` 可和，再吸收有限前缀”，而不是把 `k=0` 代入含有 `e_{-1}` 的局部式。LMZ v1 Theorem 5.1 原文从 `k=1` 求和；canonical 版本若写 `\sum_{k\ge0}e_k`，应补上这个有限前缀说明。

### 3.2 局部 KL 球的留域

Theorem 5.1 的证明先由聚点、连续的 `\vartheta` 和 `e_k\to0` 选出 `K`，使能量差和前一步 surrogate 小，并在 `x^K` 附近启动 Theorem 4.3 (`s_k=0`) 的 bootstrap。只有在该 bootstrap 后，才能断言所有更大 `k` 都留在 KL 球中并求和。当前目标二报告已经把 LMZ Theorem 4.3 作为后端；审查建议在 canonical proof reconstruction 中明示这一层，而不要让读者误以为“有一个 KL 聚点”就自动使整个轨道从该时刻起留在球内。

该边界是 nonfatal 的证明展开问题，因为 LMZ Theorem 5.1 已提供留域框架；若删除 Theorem 4.3 的引用并直接把局部递推写成全局递推，则会成为 fatal 量词缺口。

### 3.3 (5.1) 的 PPA 专化

LMZ 的条件

\[
\limsup_{(s,t)\to(0,0)}
\frac{\varphi^{-1}(\beta(s)t)}{\mu_1s+\mu_2t}\le1
\]

在 `\varphi(t)=t^2,\ \beta(t)=t` 下由
`\sqrt{st}\le(s+t)/2` 给出 `\mu_1=\mu_2=1/2`。用 `s=e_{k-1}`、
`t=(b/a)\Lambda_{k,k+1}` 时，(5.2) 的 `\delta` 选择要求两者都进入小窗；LMZ 源码中的式 (5.5) 正是在控制第二个量。报告中若省略这一小量控制，会把 (5.1) 误用在 KL 球外，但现有 `target2_kl.md` 已记录该条件。

## 4. `2\sigma` 项的边界复核

LMZ v1 `lmz-src/main_update.tex` 的 Lemma L3.3 明确给出

\[
\frac{\sigma}{q+1}u^q\|z-\widecheck x\|
\le \frac{L_2}{q+1}v^{q+1}
 +\frac{\sigma}{q+1}u^qv+L_2uv^q,
\]

其中 `u=\|z-x\|`、`v=\|x-\widecheck x\|`。三角不等式
`\|z-\widecheck x\|\ge u-v` 给出的下界是

\[
\frac{\sigma}{q+1}u^{q+1}-\frac{\sigma}{q+1}u^qv
\le \frac{\sigma}{q+1}u^q\|z-\widecheck x\|.
\]

与 A96 右侧原有的 `\sigma u^qv/(q+1)` 相加后，必须得到

\[
\frac{\sigma}{q+1}u^{q+1}
\le \frac{L_2}{q+1}v^{q+1}
 +\frac{2\sigma}{q+1}u^qv+L_2uv^q.\tag{A96'}
\]

当 `v>0` 时令 `t=u/v`，得到

\[
H_\sigma(t)=\sigma t^{q+1}-2\sigma t^q-L_2(q+1)t-L_2\le0.
\]

在论文 Assumption A3.1 的 `L_2>0`、`q\in(0,1]` 下，L4.4 的唯一根满足 `t(\sigma)>2`，从而
`u\le t(\sigma)v`。当 `v=0` 时不能先除以 `v^{q+1}`；直接使用 A96' 的右侧为零，推出 `u=0`。因此 `target2_kl.md` 对“第二个 `\sigma` 不可删除”和“`v=0` 单独处理”的记录是正确的，没有需要改写的数学结论。

其适用域仍需保留：该 `2\sigma` 推导属于 LMZ 高阶正则化子问题，要求选定的 `z=y_\sigma(x)`、投影点 `\widecheck x` 及相关集合满足 A3.1 的域条件；它不是普通 exact PPA 的额外自动估计，不能把 `t(\sigma)` 直接塞入 C311 的 `e_k=\|x^{k+1}-x^k\|` 映射。

## 5. 正式出版版差异的边界

当前本地 `mor/official.pdf` 经文件类型核验是 INFORMS cookie/HTML 页面而非 PDF，不能用于逐页 diff。已能确认的只是正式页面的元数据和摘要层变化：online 日期显示为 2026-04-07，摘要将 v1 的 “over-parameterized compressed sensing model” 改为 “Hadamard reparameterized compressed sensing model”，并更新资助信息。这些不触及 Definition 2.2、H1'、H2、H3、Theorem 5.1/5.2 或 Remark 5.3 的公式。

因此必须把下列项目保持为 `unknown`：

* 正式版是否改动 Definition 2.1/2.2 的次微分和 KL 约定；
* Theorem 5.1 的索引、(5.1)、(5.6)–(5.7) 或留域证明是否改写；
* Theorem 5.2/Remark 5.3 的速率表达式是否修正；
* Section 7 的 KL 推论是否改变前件或常数。

v1 Remark 5.3 的一般尾率打印为

\[
k^{-\alpha(1-\alpha)/((1+\alpha)\theta-\alpha)},
\]

而同段前面由 `\xi(t)=Ct^r`、`r=\alpha/((1+\alpha)\theta)` 直接得到的标准尾和指数为

\[
\frac{r}{1-r}=\frac{\alpha}{(1+\alpha)\theta-\alpha}.
\]

这仍应标为 v1 文字率式的疑似笔误/待正式版核对，不能把正式版未知误写成已修正或已确认。

## 6. 可执行修订清单与状态门

1. 在 C311 与目标二报告中把“相关子水平集有界”改成明确的 `L(f(x^0))`（或 `L(f(x^{k_0}))`）有界，并保留 prox 轨道起点在 `dom f` 的条件。
2. 在 canonical proof reconstruction 的 KL5/KL6 旁注明 `k\ge K\ge1`、`w^k` 对应 `e_{k-1}`，尾部可和加有限前缀。
3. 说明局部递推通过 LMZ Theorem 4.3 的 `s_k=0` bootstrap 留在 KL 球内；若未来改写成独立证明，必须复现该留域步骤。
4. 保留 H3 为单独前件；只能在额外连续性假设下删除它，不能由 l.s.c. 或 global argmin 自动删除。
5. 保留 A96' 中的 `2\sigma`、`H_\sigma` 根式和 `v=0` 分支；普通 exact PPA 转移不要复用该高阶正则化估计。
6. 正式出版全文取得前，不修改“formal-version theorem-level differences = unknown”的状态，也不把 v1 Remark 5.3 速率当作正式定理。

上述项目属于精度和边界加固，不构成对 C311 条件版的反例。除非未来发现 H3/level-set/留域前件被错误省略，否则当前 `derived-checked` 范围可保持不变；一般非单调 RLEB–PPA 仍需独立 Lyapunov、relative-error 和 H3 桥。
