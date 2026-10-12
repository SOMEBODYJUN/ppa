# 球值方向延拓的有限单纯形预算证书

本页把 [C245](lipschitz_obstruction_budget.md#lob-object) 中尚未认证的方向常数 \(K_e\) 降到有限几何数据。它不声称已经给出 RP² 管的实际剖分；RP² 的边界近似、collar 和每个单纯形的半球余量仍需另行认证。

<a id="ssc-object"></a>
## C258-v1 · 公共半球见证给出的显式 Lipschitz 方向证书

设 \(|K|\) 是带有限仿射三角剖分 \(\mathcal T\) 的紧连通多面体流形，\(W\subset\mathbb R^n\) 是目标光滑管外域，并给定边界保持的双 Lipschitz 参数化 \(\Phi:|K|\to W\)。记 \(C_\Phi=\operatorname{Lip}(\Phi^{-1})\)。对每个顶点 \(v\) 给定 \(y_v\in S^{n-1}\)。下述 \(\sigma=[v_0,\ldots,v_n]\) 始终指 \(n\) 维顶层单纯形；对每个这样的单纯形给定单位见证 \(u_\sigma\in S^{n-1}\) 和 \(\eta_\sigma>0\)，满足
\[
\langle u_\sigma,y_{v_i}\rangle\ge \eta_\sigma
\quad (i=0,\ldots,n).
\tag{SC1}
\]
令
\[
Q_\mathcal T=\max_{\sigma\in\mathcal T^{(n)}}\sum_{i=0}^n\|\nabla\lambda_i^\sigma\|,
\qquad
\eta_\mathcal T=\min_{\sigma\in\mathcal T^{(n)}}\eta_\sigma,
\]
其中 \(\lambda_i^\sigma\) 是物理顶层单纯形上的重心坐标，且 \(Q_\mathcal T,\eta_\mathcal T\) 的最大/最小只取自顶层单纯形集合 \(\mathcal T^{(n)}\)。若 \(G_\mathcal T\) 是该三角剖分的内在路径到欧氏距离的 quasiconvex 常数，则
\[
e_\mathcal T(x)=\frac{\sum_i\lambda_i^\sigma(x)y_{v_i}}
 {\left\|\sum_i\lambda_i^\sigma(x)y_{v_i}\right\|},
\qquad x\in\sigma,
\tag{SC2}
\]
在公共面上定义一致，并满足
\[
\operatorname{Lip}(e_\mathcal T\circ\Phi^{-1};W)
\le C_\Phi G_\mathcal T\frac{Q_\mathcal T}{\eta_\mathcal T}.
\tag{SC3}
\]
以下记 \(\bar e=e_\mathcal T\circ\Phi^{-1}:W\to S^{n-1}\)。

若边界方向数据满足 \(g\circ\Phi|_{\partial|K|}=e_\mathcal T|_{\partial|K|}\)，则 (SC2) 经 \(\Phi^{-1}\) 推回后是 C245 所需的精确边界延拓。若实际内部延拓只在 collar 的界面附近给出，设 \(\Psi:\partial W\times[0,\delta]\to\operatorname{collar}(\partial W)\) 是边界保持参数化，并置 \(\widehat g(x,t)=\bar e(\Psi(x,t))\)。前件必须包括单位值估计 \(\sup_{x,t}\|g(x)-\widehat g(x,t)\|\le\varepsilon<2\)，以及 \(\widehat g\) 在产品坐标中的 Lipschitz 常数 \(K_{\widehat g}\)。在宽度 \(\delta\) 的 collar 中取 \(\chi\) 从 0 变到 1，并置
\[
H(x,t)=N\big((1-\chi(t))g(x)+\chi(t)\widehat g(x,t)\big).
\tag{SC4}
\]
原始凸组合的范数至少为 \(\mu_c=\sqrt{1-\varepsilon^2/4}\)，故 collar 同伦无零；若 \(g,\widehat g\) 的产品坐标 Lipschitz 常数分别为 \(K_g,K_{\widehat g}\)，且 \(\operatorname{Lip}\chi\le1/\delta\)，记 \(C_\Psi=\operatorname{Lip}(\Psi^{-1})\)，并在 \(\Psi(x,t)\) 上定义 \(E=H(x,t)\)，则
\[
\operatorname{Lip}(E|_{\operatorname{collar}})\le C_\Psi\frac{K_g+K_{\widehat g}+\varepsilon/\delta}{\mu_c}.
\tag{SC5}
\]
若边界单纯形的**物理**直径至多 \(h_{\rm phys}\)，且 \(g\) 的 Lipschitz 常数为 \(K_g\)，则归一化重心边界图满足原始误差估计
\[
\|\widetilde g-g\|_\infty\le \frac{2K_g h_{\rm phys}}{1-K_g h_{\rm phys}}
\quad(K_g h_{\rm phys}<1/2),
\tag{SC6}
\]
SC6 只控制 \(t=0\) 的边界迹；若 \(\Psi(x,0)=x\)，并且 \(K_{\widehat g}\) 是产品坐标中的 Lipschitz 常数，则整个 collar 的误差还需满足
\[
\varepsilon_{\rm col}\le\frac{2K_g h_{\rm phys}}{1-K_g h_{\rm phys}}+K_{\widehat g}\delta<2.
\tag{SC7}
\]
只有把 \(\varepsilon=\varepsilon_{\rm col}\) 代入 (SC4)–(SC5)，边界顶点赋值才可能转成 C245 的精确边界 collar。
这个 collar 常数与 (SC3) 一起进入 C245 的 \(G_W\) 和 \(K_e\)，不能省略。
在 \(t=\delta\) 处取 \(\chi=1\)，故 \(E\) 与内部的 \(e_\mathcal T\circ\Phi^{-1}\) 取相同迹；在 \(t=0\) 处取 \(\chi=0\)，故原边界值 \(g\) 被精确保留。

SC4–SC6 的估计如下：对单位向量 \(a,b\) 有
\(\|(1-s)a+sb\|^2=1-2s(1-s)(1-\langle a,b\rangle)\ge1-\varepsilon^2/4\)，得到 \(\mu_c\)。对 collar 坐标中的 \(H\)，原始向量的切向导数由 \(K_g+K_{\widehat g}\) 控制，\(t\) 导数由 \(\varepsilon/\delta\) 控制；归一化导数范数不超过 \(1/\mu_c\)，再乘 \(C_\Psi\) 得 SC5。边界单纯形内，若其顶点标签确实取为原边界数据 \(y_v=g(\Phi(v))\)，并置 \(q=\sum_i\lambda_i g(\Phi(v_i))\)，则 \(\|q-g(x)\|\le K_g h_{\rm phys}\)、\(\|q\|\ge1-K_g h_{\rm phys}\)，且 \(\|q/\|q\|-g(x)\|\le2\|q-g(x)\|/\|q\|\)，得到 SC6。

**证明。** 对 \(x\in\sigma\) 置 \(z(x)=\sum_i\lambda_i^\sigma(x)y_{v_i}\)。由 (SC1) 和重心坐标非负且和为 1，
\[
\|z(x)\|\ge\langle u_\sigma,z(x)\rangle\ge\eta_\sigma\ge\eta_\mathcal T.
\]
归一化映射 \(N(z)=z/\|z\|\) 在 \(\|z\|\ge\eta_\mathcal T\) 上的导数范数不超过 \(1/\eta_\mathcal T\)。同时
\[
\|Dz\|\le\sum_i\|\nabla\lambda_i^\sigma\|=Q_\sigma.
\]
故每个单纯形上的 Lipschitz 常数不超过 \(Q_\sigma/\eta_\sigma\)。公共面上的重心公式相同；沿多面体三角剖分内路径拼接并乘 \(G_\mathcal T\)，再由 \(\Phi^{-1}\) 的 Lipschitz 常数乘 \(C_\Phi\)，得到 (SC3)。

**证书状态。** (SC1) 是有限个内积不等式；\(Q_\mathcal T\) 从顶点坐标直接计算；\(G_\mathcal T\) 和 collar 同伦是独立的几何输入。该 Claim 因而是 `derived-checked` 的条件证书引理，而不是 RP² 的完成存在或原预算结论。
半球条件也可由 \(0\notin\operatorname{conv}\{y_{v_i}:v_i\in\sigma\}\) 通过有限维严格分离得到；这里把分离余量 \(\eta_\sigma\) 作为可直接复核的证书输入。

<a id="ssc-rp2"></a>
## RP² 应用的最小剩余对象

对 C234 的 \(W=\overline B_2\setminus\operatorname{int}N_{1/8}\)，需要提交以下有限对象，才能把 C258 接到 C245：

1. 一个多面体模型 \(|K|\)、边界保持的双 Lipschitz 参数化 \(\Phi:|K|\to W\) 及其 \(C_\Phi\)，再加实际仿射三角剖分和 \(G_\mathcal T,Q_\mathcal T\)；
2. 内边界方向 \(g=D_0/\|D_0\|\) 与外边界方向 \(p/2\) 的共同边界近似，以及保持原边界值的 collar 同伦；
3. 每个单纯形的单位半球见证 \(u_\sigma\) 和统一 \(\eta_\mathcal T>0\)；
4. 将 \(C_\Phi G_\mathcal TQ_\mathcal T/\eta_\mathcal T\) 及 collar 常数代入 C245 的 (LB1)，再与 \(L_0\) 比较。

有限顶点赋值或随机采样通过，若没有真实覆盖、半球余量和 collar 误差，不构成 RP² 的 \(K_e\) 证书，也不能推出 \(L_*=L_0\)。

