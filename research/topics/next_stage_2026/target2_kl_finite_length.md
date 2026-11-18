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

即 H2 取 \(b=1/\lambda\)、\(\beta(t)=t\)。KL 斜率估计与 H11 给出

\[
\Lambda_{k,k+1}\ge\frac{e_k^2}{2e_{k-1}},
\qquad
 e_k\le\sqrt{2e_{k-1}\Lambda_{k,k+1}}
\le\frac{e_{k-1}+\Lambda_{k,k+1}}{\sqrt2}.
\]

这里最后一步是直接的 AM--GM 估计。若按 LMZ 的 (K1) 书写，则

\[
\phi^{-1}(\beta(s)t)=\sqrt{st}\le\frac{s+t}{2}
\]

可取 \((\mu_1,\mu_2)=(1/2,1/2)\)，但代入 \(t=(b/a)\Lambda=2\Lambda\) 得到的是
\(e_k\le e_{k-1}/2+\Lambda\)，不能把这两个递推式混写。还需 bounded sublevel、存在聚点以及 H3；连续 \(f\) 自动给 H3，而单纯 l.s.c. 只给 liminf，不能偷换成 H3。于是得到：

**KL–PPA 定理（条件版）。** 若上述精确近端轨道有有界初始次水平集，\(f\) 在某聚点满足 KL，且 H3 成立，则不需要传统 metric subregularity 即可证明有限长度和点列收敛。

变步长 \(\lambda_k\in[\lambda_-,\lambda_+]\) 时，需统一取 \(a=1/(2\lambda_+)\)、\(b=1/\lambda_-\)；没有上下界，H11/H2 的统一常数不存在。

## 3. 这并不等于一般非单调 PPA 已经摆脱正则性

一般 RLEB–PPA 的 \(F\) 可能不是 \(\partial f\)，也可能没有一个随迭代下降的 Lyapunov 函数。KL 性质只对某个函数 \(E\) 的能量差和次梯度距离作关系；没有 H11，不能把能量差转成步长；没有 H2，不能把次梯度距离转成步长或残差。因此不能把“有 KL 函数”直接替换成“有限长度”。

一个满足 H0--H3 且 \(e_k\to0\) 的严格抽象反例是

\[
f(u,v)=(u^2+v^2-1)^2,
\qquad
\theta_k=\sum_{j=1}^k\frac1j,
\qquad
x^k=(\cos\theta_k,\sin\theta_k).
\]

这是多项式 KL 函数，且 \(f(x^k)=0\)，初始次水平集 \(\{f\le0\}=S^1\) 紧。令

\[
e_k=\|x^{k+1}-x^k\|=2\sin\frac1{2(k+1)}\sim\frac1{k+1}.
\]

于是 H0 成立，H1 取 \(c=1\) 且 \(e_k\to0\)，圆上 \(0\in\partial f(x^k)\) 给出 H2（取 \(w_k=0\)、\(\beta(t)=t\)），H3 由连续性成立，但 \(\sum_k e_k=\infty\)。失败点正是 H11 的正步长耗散；该序列不是 exact PPA 轨道，因为 exact PPA 的下降不允许等能量的非零步。

## 4. 一个真正非次梯度、但仍依赖 MSR 的闭合类

取 \(H=\mathbb R^n\)、\(A=S+K\)，其中 \(S=S^\top\succeq0\)、\(K^\top=-K\)，并假设 \(A\) 可逆。令 \(F(x)=Ax\)。对任意图点差 \(h\)，

\[
\|(I+\lambda A)h\|^2-\|(I-\lambda A)h\|^2
=4\lambda\langle h,Sh\rangle\ge0,
\]

所以完整图满足全局 \(\mathrm{RL}(\lambda,1,1)\)。同时 \(I+\lambda A\) 可逆，故完整 resolvent \(J=(I+\lambda A)^{-1}\) 满输入且单值。

对 \(x^{k+1}=Jx^k\)，取 \(E(x)=\frac12\|x\|^2\)、\(e_k=\|x^{k+1}-x^k\|\)，并写 \(y=x^{k+1}\)。则

\[
E(x^k)-E(y)=\lambda\langle y,Sy\rangle+\frac12e_k^2\ge\frac12e_k^2,
\]

而 \(\xi_{k+1}=y\in\partial E(y)\) 且

\[
\|\xi_{k+1}\|\le\frac{\|A^{-1}\|}{\lambda}e_k.
\]

因此 H11、H2、H3、有界次水平集和 \(E\) 在 \(0\) 的 KL 性质全部成立，LMZ transfer 给出有限长度与 \(x^k\to0\)。当 \(K\ne0\) 时，\(F\) 不是标量函数的次梯度图；例如 \(A=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\) 时，\(F\) 是非强单调的最大单调旋转，\(J\) 的收缩因子为 \((1+\lambda^2)^{-1/2}\)。

这证明 RL--KL 桥确实能在一个自然的非次梯度类中闭合，但 \(A\) 可逆已经给出全局线性 metric subregularity。因此它是迁移的正面基准，不是弱于 MSR 的新定理。

## 5. 对 \(2\sigma\|x^{k+1}-x^k\|\) 项的实际结论

若旧 PPA 证明中出现

\[
E_{k+1}\le E_k-c\,Q_k+2\sigma\|x^{k+1}-x^k\|,
\]

MOR KL 机制不能把最后一项凭空删掉。可用的闭合形式是：存在 \(0<\rho<1\) 和修正项 \(\Psi_k\)，使

\[
2\sigma\|x^{k+1}-x^k\|
\le \rho a\phi(e_k)+\Psi_k-\Psi_{k+1},
\]

从而以 \(\widetilde E=E+\Psi\) 得到

\[
\widetilde E_{k+1}+a'\phi(e_k)\le\widetilde E_k,
\qquad a'=(1-\rho)a>0.
\]

另一种可接受的证明是直接把该项转化为已有的能量差。固定 \(\sigma>0\) 的线性项不能仅靠 \(c\|x^{k+1}-x^k\|^2\) 或 Young 不等式吸收；若 \(F\) 不是次微分、没有真实相对误差选择，或物理步长与 \(e_k\) 不兼容，则 MOR 定理不能直接迁移。

## 6. 版本与审查状态

正式出版社记录确认 online 日期为 2026-04-07、作者和摘要与 arXiv 主题一致；当前环境的 PDF 下载被重定向到摘要页，无法逐页对照正式排版。因此预印本中的定理编号和公式已经逐式核对，但“正式版与 v1 的全部差异”保持 `open`。预印本 Remark 5.3 的一个指数表达式在 \(\alpha=1\) 时呈现可疑的退化，报告不将其作为迁移定理；PPA 迁移只使用 Theorem 5.1 的直接证明。

**状态：** exact subgradient PPA 条件版可记为 `derived-checked`；抽象的 RL--KL transfer corollary 仅在额外给出同一 Lyapunov、H11、真实相对误差和物理步兼容时成立。对一般非单调 RLEB--PPA 的无 metric-subregularity 有限长度定理仍为 `candidate/open`，所缺是从 RL/图几何实际验证这条桥。

