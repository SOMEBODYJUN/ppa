# 真残差 RLEB：允许近端关系的局部有限长度

本页固定 C02-v3 的数学身份。它将 C02-v2 的同一图块全对 RL 改为每个允许输出的最近零点锚比较，结论覆盖同一个允许近端关系的全部选择。C02-v2 的历史陈述与状态保持不变。本文中的 EB 使用完整原关系的真残差；C185 的所选值 EB 是另一身份。

<a id="trs-object"></a>
## TRS-OBJECT · 原关系、真残差及允许输出

固定 Euclidean 空间 \(X=\mathbb R^n\)、\(n\ge1\)，关系 \(F:X\rightrightarrows X\)、\(\lambda>0\)、非空闭集 \(S\subset\operatorname{zer}F\)、开集 \(U\subset X\)。定义
\[
J_{\lambda F}(x)=\{y:(x-y)/\lambda\in F(y)\},\quad
r_F(y)=\inf_{v\in F(y)}\|v\|,\quad
P_S(x)=\{p\in S:\|x-p\|=d(x,S)\}.
\]
到空集的距离与空纤维残差取 \(+\infty\)。非空闭 \(S\) 在有限维空间保证 \(P_S(x)\ne\varnothing\)。目标不必是完整零集。

固定
\[
R,\bar t>0,\quad L\ge0,\quad0<\gamma\le1,\quad0<\kappa<1,
\]
以及有限非减 \(\psi:[0,\bar t]\to[0,\infty)\)，\(\psi(0)=0\) 且在零点连续。令 \(U_R=\{x\in U:d(x,S)\le R\}\)。同一个允许关系 \(\mathcal J\) 满足以下合取前件：

1. 每个 \(x\in U_R\) 有 \(\varnothing\ne\mathcal J(x)\subset J_{\lambda F}(x)\)。
2. 对每个 \(x\in U_R\) 和每个 \(y\in\mathcal J(x)\)，存在可依该输出变化的 \(p\in P_S(x)\)，使
   \[
   \langle y-p,x-y\rangle\ge\frac14\{d(x,S)^2-L^2d(x,S)^{2\gamma}\}.
   \tag{TRS1}
   \]
3. 对每个 \(y\in\mathcal J(U_R)\)，若 \(r_F(y)\le\bar t\)，则
   \[
   d(y,S)\le\psi(r_F(y));\qquad
   (R+LR^\gamma)/(2\lambda)\le\bar t.
   \tag{TRS2}
   \]
4. 对全部 \(0<t\le R\)，有
   \[
   \psi((t+Lt^\gamma)/(2\lambda))\le\kappa t.
   \tag{TRS3}
   \]

锚比较 TRS1 等价于 \(\|2y-x-p\|\le Ld(x,S)^\gamma\)。它不比较同一输入的两个输出。

<a id="trs-theorem"></a>
## C02-v3 · 真残差版全部允许选择的局部收敛

- **Status**：`derived-checked`，范围仅为本页显示前件、结论及自足证明；不整体升级 C02 原稿的其他身份，不认证外部新颖性。
- **Exact Statement**：保留 TRS-OBJECT 的全部对象与共同选择量词。令
  \[
  B(t)=(t+Lt^\gamma)/2,\qquad
  \mathcal L(t)=\frac12\left\{\frac{t}{1-\kappa}
                         +\frac{Lt^\gamma}{1-\kappa^\gamma}\right\}.
  \tag{TRS4}
  \]
  对每个 \(x^0\in U_R\)，记 \(d_0=d(x^0,S)\)，另要求
  \[
  \mathcal L(d_0)<d(x^0,X\setminus U).
  \tag{TRS5}
  \]
  则每条逐步选择 \(x^{k+1}\in\mathcal J(x^k)\) 均可无限继续，全部点属于 \(U_R\)，具有有限长度，收敛到某个 \(x^\infty\in S\cap U\)，并有
  \[
  d_k\le\kappa^k d_0,\quad
  \|x^{k+1}-x^k\|\le B(\kappa^k d_0),\quad
  \sum_{k\ge0}\|x^{k+1}-x^k\|\le\mathcal L(d_0),
  \tag{TRS6}
  \]
  \[
  \|x^\infty-x^k\|\le\mathcal L(d_k)
       \le\mathcal L(\kappa^k d_0).
  \tag{TRS7}
  \]
  常数统一于全部允许选择，极限点可以不同。距离 Q 因子上界为 \(\kappa\)，点误差 R 因子上界为 \(\kappa^\gamma\)；后者不声称逐步 Q 收缩。
- **Definitions / Dependencies**：完整关系与真残差采用本页定义，与 [D01/D04](../foundations.md) 的对象一致。证明仅用锚比较、真实近端包含、真 EB、标量兼容、严格预算、有限维最近点和完备性。C185 是既有允许转移机制的对照，不是本证明的缺失步骤；[C02-v2](../rleb_ppa.md#r02) 是较强全对图块的特例。
- **Evidence**：下一节逐行证明；论文对应正文为 `发表成果整理/RLEB/sections/theorem_spine.tex` 的 `thm:selection-RLEB`，旧 `cor:selection-extension` 仅为兼容标签。
- **Scope / Objections**：允许子关系与完整近端关系严格区分；若要控制完整 PPA 的全部选择，必须取 \(\mathcal J(x)=J_{\lambda F}(x)\) 于全部使用输入上，并逐完整输出核前件。没有原生 coverage、全纤维排他或同半径球自映射的自动结论。

<a id="trs-proof"></a>
## TRS-PROOF · 一步代数、有限前缀留域与尾和

取合法输入 \(x\) 和任意允许输出 \(y\)，按 TRS1 取 \(p\)，记 \(a=y-p\)、\(b=x-y\)、\(d=d(x,S)\)、\(s=\|b\|\)、\(d_+=d(y,S)\)。有 \(a+b=x-p\)，TRS1 因而给 \(\|a-b\|\le Ld^\gamma\)。平行四边形恒等式及反三角不等式分别给
\[
d_+^2+s^2\le\|a\|^2+\|b\|^2
      \le(d^2+L^2d^{2\gamma})/2,
\qquad |2s-d|\le\|2b-(a+b)\|\le Ld^\gamma.
\tag{TRS8}
\]
所以 \(s\le B(d)\)。真实近端包含只给
\[
r_F(y)\le\|(x-y)/\lambda\|=s/\lambda
\le B(d)/\lambda\le B(R)/\lambda\le\bar t.
\]
TRS2 因此可用于实际输出；\(\psi\) 非减与 TRS3 给 \(d_+\le\kappa d\)。当 \(d=0\) 时，TRS8 强制 \(s=0,y=x\)，故零距离输入的全部允许选择均驻定。

初值 coverage 给第一步。若已构造到 \(x^k\in U_R\)，上述估计与归纳前缀给
\[
d_{k+1}\le\kappa^{k+1}d_0,\qquad
\|x^{k+1}-x^0\|\le\sum_{j=0}^kB(\kappa^j d_0)
\le\mathcal L(d_0)<d(x^0,X\setminus U).
\]
因此 \(x^{k+1}\in U\)，距离又不超过 \(R\)，coverage 可再次调用。这证明无限继续和 TRS6，不预先假设全轨道合法。可和长度给 Cauchy 性；完备性、\(S\) 闭及 \(d_k\to0\) 给极限属于 \(S\)。同一严格预算使极限留在 \(U\)。从 \(k\) 起求和得到 TRS7。□

<a id="trs-fullgraph"></a>
## TRS-FULLGRAPH · 全对图块的验证桥与完整纤维门

若同一 \(\mathcal G\subset\operatorname{gph}F\) 对每个 \(x\in U_R\) 有输出及图块内最近零锚，且在 Minty 输入对距尺度 \(R\) 上满足全对 RL，则输出图点与该零锚的比较供应 TRS1。对同输入的两个图点比较，全对 RL 强制 \(J_{\mathcal G}\) 单值。再合取本页真 EB、兼容与预算，即得到 C02-v2 的唯一图块轨道结论。

\(J_{\mathcal G}\subset J_{\lambda F}\) 仅是包含关系；同一输入还可能有完整图的其他输出。调用 C02-v3 控制全部完整输出须另证等式或直接全纤维验证，不能凭图块单值性获得。

Luke–Tam 覆盖前提的精确复用如下。取 \(U_{\rm LT},U'_{\rm LT},W_{\rm LT}\)，定义
\[
\bar F(u)=F(u)\cap(W_{\rm LT}/\lambda),\quad
\mathcal G_{\rm LT}=\{(u,v)\in\operatorname{gph}F:
u\in U_{\rm LT},\ \lambda v\in W_{\rm LT}\}.
\]
若已验证 \(U_R\subset U'_{\rm LT}\subset(I+\lambda\bar F)(U_{\rm LT})\)，取 \(\mathcal J=J_{\mathcal G_{\rm LT}}\) 即供应输入 coverage。若 \(\mathcal G_{\rm LT}\subset\mathcal G\)，则也供应该图块的 coverage 部分。最近零锚、TRS1–TRS3 与预算仍须对同一对象另核。这是复用正式版 [Assumption 2(d)(ii)](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863) 的一个前提，不是无条件导入其完整收敛定理。

<a id="trs-selected-boundary"></a>
## TRS-SELECTED-BOUNDARY · C185 的不同 EB 身份

对所选 \(v=(x-y)/\lambda\)，本页真 EB 蕴含 \(d(y,S)\le\psi(\|v\|)\)，故可接入 [C185 的允许转移证书](allowed_transition_local.md#at-theorem)。逆向不成立：取 \(F(y)=\{y,3y\}\)、\(\lambda=1\)、\(S=\{0\}\)，只允许 \(y=x/4,v=3x/4\)，\(\psi(t)=t/3\)。所选值 EB 取等，完整真残差却为 \(|y|\)，其真 EB 对所有非零 \(y\) 失败。即使 gauge 连续且完整残差取到，也不能用所选子纤维替代全部完整纤维的下确界。

<a id="trs-witness"></a>
## TRS-WITNESS · 严格多值的完整近端实例

在 \(\mathbb R\) 取 \(F(y)=\{2y,3y\}\)、\(\lambda=1\)、\(S=\{0\}\)、\(U=\mathbb R\)、\(R=\bar t=1\)、\(\gamma=1,L=1/2\)、\(\psi(t)=t/2\)、\(\kappa=3/8\)。完整 \(\mathcal J=J_F\) 为 \(\{x/3,x/4\}\)，coverage 全域成立。锚反射绝对值分别为 \(|x|/3\) 或 \(|x|/2\)，真残差为 \(2|y|\)，每个合法输入的输出残差不超过 \(2/3\)。窗口上界 \(3/4\le1\)，直接组合恰 \(3d/8\)，严格留域自动成立。因此 C02-v3 控制全部完整选择。

但是任意非零输入的两个输出不同。它们的 Minty 输入对距为零，全对 RL 会强制相等，故包含这两者的图块不可能满足任何全对 RL。该例证明锚定条件比全对验证器严格更宽；不认证任何整体文献框架的包含或优越性。

<a id="trs-basin"></a>
## TRS-BASIN · 独立初值邻域

给定 \(\bar x\in S\cap U\)，取有限 \(a>0\) 使 \(B_a(\bar x)\subset U\)。因为 \(\mathcal L(t)\to0\)，存在 \(0<\delta\le R\) 使 \(\delta+\mathcal L(\delta)<a\)。若 \(x^0\in B_\delta(\bar x)\)，则
\[
d_0\le\|x^0-\bar x\|<\delta,\quad
d(x^0,X\setminus U)\ge a-\|x^0-\bar x\|>
a-\delta>\mathcal L(\delta)\ge\mathcal L(d_0).
\]
所以全部允许轨道存在，并留在外层 \(B_a(\bar x)\)，极限也在该外球。此处两个半径有不同作用；没有同半径内球自映射声称。

C02-v3 已登记到根账本、状态与关系图；C02/C02-v2/C185 保留各自的版本身份。


<a id="trs-coverage-gap"></a>
## TRS-COVERAGE-GAP · 完整定义域也不能替代近端输入覆盖

令 \(F:\mathbb R\rightrightarrows\mathbb R\) 为
\[
F(u)=\begin{cases}\{u-1\},&u<0,\\\{-1,0,1\},&u=0,\\\{u+1\},&u>0.\end{cases}
\]
其图闭，完整定义域为 \(\mathbb R\)，完整零集为 \(S=\{0\}\)。取 \(\lambda=1,\gamma=1/2,L=\sqrt2\)。Minty 输入域为
\[
D=(-\infty,-1]\cup\{0\}\cup[1,\infty),
\]
反射坐标 \(C(x)=u-v\) 在左半域等于 \(1\)，在 \(0\) 等于 \(0\)，在右半域等于 \(-1\)。同侧点对的反射差为零；异侧输入对距至少 \(2\)，反射差为 \(2\)；一端为零时输入对距至少 \(1\)，反射差为 \(1\)。故每一对完整图点满足
\(\|C(x)-C(x')\|\le\sqrt2\,|x-x'|^{1/2}\)。

对 \(u\ne0\)，完整真残差为 \(|u|+1\)，所以全域有
\(d(u,S)=|u|\le r_F(u)^3\)；零点也满足该式。因而 \(q\gamma=3/2>1\)，但任意零邻域都包含不在 \(D\) 的输入，完整近端关系在那里为空。完整原算子的定义域、闭图、全对 RL、高阶真 EB 与相对连续性均不能代替输入 coverage。这补强 [F16](../../FAILED_ROUTES.md#f16) 的离散域反例，而不改变其逻辑门。
