# 目标二：改进 KL 不等式与 PPA 有限长度

## 1. MOR 论文中实际可迁移的框架

Li–Mordukhovich–Zhu 的预印本 2406.13207 v1 将算法写成耦合序列 \((x^k,e_k)\)。其基础条件是：

\[
\begin{aligned}
\text{(H0)}&\quad f(x^{k+1})\le f(x^k),\\
\text{(H1)}&\quad \|x^{k+1}-x^k\|\le c e_k,\quad e_k\to0,\\
\text{(H2)}&\quad \exists w_{k+1}\in\partial f(x^{k+1}),\quad
\|w_{k+1}\|\le b\beta(e_k),\\
\text{(H3)}&\quad x^{k_j}\to\bar x\Rightarrow
\limsup_j f(x^{k_j})\le f(\bar x).
\end{aligned}
\]

Theorem 5.1 使用更强的下降条件

\[
f(x^{k+1})+a\phi(e_k)\le f(x^k),
\tag{H11}
\]

以及 KL 函数 \(\vartheta\)。其关键耦合门是

\[
\limsup_{(s,t)\to(0,0),\,s,t>0}
\frac{\phi^{-1}(\beta(s)t)}{\mu_1s+\mu_2t}\le1,
\qquad \mu_1\in(0,1),\ \mu_2\ge0.
\tag{K1}
\]

定理结论是 \(\sum_k\|x^{k+1}-x^k\|<\infty\) 且整列收敛到 KL 邻域中的一个点。证明先用 KL 斜率估计和 H2 得到

\[
\vartheta'(f_k-f_*)\ge\frac1{b\beta(e_{k-1})},
\]

再用 H11 和 \(\vartheta\) 的凹性，把能量差

\[
\Lambda_k=\vartheta(f_k-f_*)-\vartheta(f_{k+1}-f_*)
\]

转成

\[
\phi(e_k)\le b\beta(e_{k-1})\Lambda_k/a.
\]

由 (K1) 得到 \(e_k\le \ell_1e_{k-1}+\ell_2\Lambda_k\)，再把该递推代入抽象 Theorem 4.3，能量差望远镜与 \(\ell_1<1\) 共同给出有限长度。

<a id="t2-kl-ppa"></a>
## 2. 普通精确 PPA 的逐项映射

设 \(f\) proper、下半连续，且每一步取全局精确近端点

\[
x^{k+1}\in\arg\min_y\left\{f(y)+\frac1{2\lambda}\|y-x^k\|^2\right\}.
\]

令 \(e_k=\|x^{k+1}-x^k\|\)。全局最小性给

\[
f(x^{k+1})+\frac1{2\lambda}e_k^2\le f(x^k),
\]

所以 H11 取 \(a=1/(2\lambda)\)、\(\phi(t)=t^2\)，H1 取 \(c=1\)。Fermat 条件给

\[
w_{k+1}=\frac{x^k-x^{k+1}}\lambda\in\partial f(x^{k+1}),
\qquad \|w_{k+1}\|=\frac1\lambda e_k,
\]

即 H2 取 \(b=1/\lambda\)、\(\beta(t)=t\)。(K1) 由

\[
\phi^{-1}(\beta(s)t)=\sqrt{st}\le\frac{s+t}{2}
\]

成立，取 \((\mu_1,\mu_2)=(1/2,1/2)\)。还需 bounded sublevel、存在聚点以及 H3；连续 \(f\) 自动给 H3，而单纯 l.s.c. 只给 liminf，不能偷换成 H3。于是得到：

**KL–PPA 定理（条件版）。** 若上述精确近端轨道有有界初始次水平集，\(f\) 在某聚点满足 KL，且 H3 成立，则不需要传统 metric subregularity 即可证明有限长度和点列收敛。

变步长 \(\lambda_k\in[\lambda_-,\lambda_+]\) 时，需统一取 \(a=1/(2\lambda_+)\)、\(b=1/\lambda_-\)；没有上下界，H11/H2 的统一常数不存在。

## 3. 这并不等于一般非单调 PPA 已经摆脱正则性

一般 RLEB–PPA 的 \(F\) 可能不是 \(\partial f\)，也可能没有一个随迭代下降的 Lyapunov 函数。KL 性质只对某个函数 \(E\) 的能量差和次梯度距离作关系；没有 H11，不能把能量差转成步长；没有 H2，不能把次梯度距离转成步长或残差。因此不能把“有 KL 函数”直接替换成“有限长度”。

一个严格的抽象反例是

\[
f(u,v)=u^2+(v^2-1)^2,
\qquad x^{2k}=(0,1),\quad x^{2k+1}=(0,-1).
\]

此 \(f\) 是多项式，具有 KL 性质；初始次水平集 \(\{f\le0\}=\{(0,1),(0,-1)\}\) 紧；H0 成立且 H2 可取 \(w_k=0\)，H3 由连续性成立，但轨道交替，\(\sum\|x^{k+1}-x^k\|=\infty\)。失败点是 H11：能量没有提供任何正的步长耗散。故 KL-only 方案不成立。

## 4. 对 \(2\sigma\|x^{k+1}-x^k\|\) 项的实际结论

若旧 PPA 证明中出现

\[
E_{k+1}\le E_k-c\,Q_k+2\sigma\|x^{k+1}-x^k\|,
\]

MOR KL 机制可以处理的形式不是把最后一项凭空删掉，而是先构造新的能量 \(\widetilde E\) 或证明该项被 H11 的下降余量吸收，使

\[
\widetilde E_{k+1}+a\phi(e_k)\le\widetilde E_k
\]

成立；然后再验证 H2、H3 和 (K1)。如果 \(F\) 不是次微分、没有相对误差选择 \(w_{k+1}\)、或步长项无法吸收，则 MOR 定理不能直接迁移。这里仍然需要新的结构正则性，只是它可能是 KL + Lyapunov compatibility，而不是传统 metric subregularity。

## 5. 版本与审查状态

正式出版社记录确认 online 日期为 2026-04-07、作者和摘要与 arXiv 主题一致；当前环境的 PDF 下载被重定向到摘要页，无法逐页对照正式排版。因此预印本中的定理编号和公式已经逐式核对，但“正式版与 v1 的全部差异”保持 `open`。预印本 Remark 5.3 的一个指数表达式在 \(\alpha=1\) 时呈现可疑的退化，报告不将其作为迁移定理；PPA 迁移只使用 Theorem 5.1 的直接证明。

**状态：** KL–PPA 条件版可记为 `derived-checked`；对一般非单调 RLEB–PPA 的无 metric-subregularity 有限长度定理仍为 `open`，所缺是可验证 Lyapunov、相对误差和 H3 的统一桥。

