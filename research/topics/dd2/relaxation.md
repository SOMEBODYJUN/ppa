# DD2 的方向自适应松弛

## 1. 允许图步和一步估计

设 \(\mathcal K\) 为实 Hilbert 空间，\(\mathcal F:\mathcal K\rightrightarrows\mathcal K\)，\(\varnothing\ne S\subseteq\operatorname{zer}\mathcal F\)。记 \(d=d(\cdot,S)\) 和 \(r_{\mathcal F}(z)=\inf_{q\in\mathcal F(z)}\|q\|\)。指定允许关系 \(\mathcal Q(z)\subseteq\mathcal F(z)\)。对每个受检输入 \(z\) 和每个 \(q\in\mathcal Q(z)\)，记

\[
\widehat z=z-q,\qquad z^+=z-\alpha q,\qquad t=d(z),\qquad a=d(\widehat z),\qquad u=d(z^+),\qquad s=\|q\|.
\]

其中 \(\alpha>0\) 是实际松弛，\(s\) 是所选前向值的范数，实际迭代步长为 \(\alpha s\)。令 \(G=(\mathcal F^{-1}-I)^{-1}\)，则 \(q\in G(\widehat z)\) 且 \(\operatorname{zer}G=\operatorname{zer}\mathcal F\)。输出真误差界 \(a\le\psi(r_G(\widehat z))\) 在 \(\psi\) 非减时推出 \(a\le\psi(s)\)。下文只需要后者。若起点使用原 PPA 的 \(r_A(\widehat z)\) 且 \(q\in\lambda A(\widehat z)\)，则将其模替换成 \(s\mapsto\psi(s/\lambda)\)。

设 \(V\) 是有界自伴算子，\(V\succeq\eta I\) 且 \(\eta>0\)。对 \(q\ne0\) 可取 \(\beta=\langle q,Vq\rangle/s^2\)，也可取 \(\eta\le\beta\le\langle q,Vq\rangle/s^2\)。当 \(q=0\) 取 \(\beta=\eta\)。假设每个允许图步有一个最近锚 \(p\in P_S(z)\)，满足

\[
\langle q,z-p\rangle\ge\langle q,Vq\rangle+\Phi(t) .\tag{1}
\]

Hilbert 空间的非凸闭集未必有最近点。也可直接假设存在 \(p_n\in S\) 使 \(\|z-p_n\|\to t\) 且 \(\liminf_n\langle q,z-p_n\rangle\ge\langle q,Vq\rangle+\Phi(t)\)。对 \(\|z^+-p_n\|^2\) 取上极限以及沿同序列用 Cauchy–Schwarz，就得到下文相同的距离与步长不等式。原 DD2 的 \(\langle q,\widehat z-p\rangle\ge\Phi(t)\) 对应 \(V=I\)。一般 \(V\) 需要在该不等式的右端加入 \(\langle q,(V-I)q\rangle\)。

写 \(D(t)=[-\Phi(t)]_+\)，\(\gamma=2\beta-\alpha\)，\(\delta=\alpha\gamma\)。在 \(0<\alpha\le2\beta\) 时，展开到同一个锚的平方距离可得

\[
u^2\le t^2-2\alpha\Phi(t)-\delta s^2\le t^2+2\alpha D(t)-\delta s^2 .\tag{2}
\]

由 (1) 与距离的三角不等式有

\[
\beta s^2\le ts+D(t),\qquad s\le B_{\beta,D}(t):=\frac{t+\sqrt{t^2+4\beta D(t)}}{2\beta},\qquad t\le a+s .\tag{3}
\]

若 \(a\le\psi(s)\)，其中 \(\psi\ge0\) 连续非减且 \(\psi(0)=0\)，则

\[
u\le\psi_\alpha(s):=\psi(s)+|1-\alpha|s,\qquad s\ge\chi(t):=(I+\psi)^{-1}(t).\tag{4}
\]

\(I+\psi\) 严增且值域为 \([0,\infty)\)，所以 \(0<\chi(t)\le t\) 对 \(t>0\) 成立。若另有输入误差界 \(t\le\psi_{\rm in}(s)\)，还可用它对 \(s\) 的下界。式 (3) 在 \(t=0,D(0)=0\) 时强制 \(s=0\)。式 (4) 给出 \(s=0\Rightarrow t=0\)。若 \(\mathcal Q=\mathcal F\) 在受检输入的整个纤维上成立，则输入真残差满足 \(r_{\mathcal F}(z)\ge\chi(t)\)。一般允许子关系只给所选值的下界，而 \(r_{\mathcal F}(z)\le s\)、\(r_G(\widehat z)\le s\) 两个上界仍成立。

单步距离上包络可取

\[
\varphi_{\alpha,\beta}(t)=\max_{0\le s\le B_{\beta,D}(t)}\min\{\psi_\alpha(s),\sqrt{t^2+2\alpha D(t)-\delta s^2}\}.\tag{5}
\]

根号在整个区间上实值。它的平方在右端点等于 \((t-\alpha B_{\beta,D}(t))^2\)。当 \(t>0\) 且 \(\gamma>0\)，设 \(m=\min\{B_{\beta,D}(t),\sqrt{2D(t)/\gamma}\}\)。则 \(\varphi_{\alpha,\beta}(t)<t\) 当且仅当 \(\psi_\alpha(m)<t\)。这是因为根式至少为 \(t\) 的区间恰为 \([0,m]\)，且另一个分支在此区间非减。当 \(\gamma=0\)，同一包络的严格下降条件是 \(\psi_\alpha(B_{\beta,D}(t))<t\)。已知 (4) 时可进一步把最大值区间缩成 \([\chi(t),B_{\beta,D}(t)]\)。这些判据针对给定标量包络。包含输出锚的精确几何上界见[双误差界](dual_eb.md#dd2-dual-envelope)。松弛点和影子点共享同一实际几何构形，不能把两个独立估计的最大值直接认作算子类的可达最坏因子。

若 \(D,\psi\) 连续、全部 \((\alpha,\beta)\) 取自固定紧集 \(K\subset\{(\alpha,\beta):\eta\le\beta\le\|V\|,\ 0<\alpha\le2\beta\}\)，可把 \(s\) 写成 \(v B_{\beta,D}(t)\)，\(v\in[0,1]\)。于是 \(\overline\varphi(t)=\max_{(\alpha,\beta)\in K}\varphi_{\alpha,\beta}(t)\) 连续。若 (5) 对每个 \(t\in(0,R]\) 及每个 \((\alpha,\beta)\in K\) 均严格小于 \(t\)，则 \(\overline\varphi(t)<t\)。在已经续接的轨道上，\(t_{k+1}\le\overline\varphi(t_k)\) 使距零集趋零。对变量松弛逐步独立核严格性无法替代这个统一性，§5 的松弛边界例给出正距离极限。

<a id="dd2-adaptive-length"></a>
## 2. 一般函数耗散与有限长度

**定理。** 设 \(S\) 非空闭，\(U\subseteq\mathcal K\) 开，\(R>0\)。对 \(z\in U\) 且 \(t=d(z)\le R\) 假设允许关系非空，(1) 和输出误差界对每个允许步成立，\(D(0)=0\)。对每个 \(t>0\) 的允许步规定 \(0<\alpha\le2\beta\) 且 \(\gamma\ge g(t)\)，其中 \(0<g(t)\le2\|V\|\)。假设

\[
\mu(t):=g(t)-\frac{2D(t)}{\chi(t)^2}>0\qquad(0<t\le R).
\tag{6}
\]

若 \(h(t)=2t/[\mu(t)\chi(t)]\) 在 \((0,R]\) 有非增的可积上包络 \(\overline h\)，定义 \(\Theta(t)=\int_0^t\overline h(v)\,dv\)。每个受检图步满足

\[
t^2-u^2\ge\alpha\mu(t)s^2,\qquad \alpha s\le\Theta(t)-\Theta(u)\quad(t>0).\tag{7}
\]

当 \(t=0\) 时 \(s=u=0\)。若 \(t_0\le R\) 且 \(\Theta(t_0)<d(z^0,U^c)\)，任意允许选择可以一直续接，且

\[
\sum_{j=k}^\infty\|z^{j+1}-z^j\|\le\Theta(t_k),\qquad \|z^k-z^\infty\|\le\Theta(t_k).\tag{8}
\]

若再有 \(\sum_k\alpha_k=\infty\) 且对每个 \(0<c\le R\) 有 \(\inf_{t\in[c,R]}\mu(t)>0\)，则 \(t_k\to0\)，\(z^\infty\in S\cap U\)，且 \(\widehat z^k\to z^\infty\)。若迭代有限步到达 \(S\)，此识别无需发散和的假设。

**证明。** 在 (2) 中代入 \(2D(t)\le[g(t)-\mu(t)]\chi(t)^2\le[\gamma-\mu(t)]s^2\)。对 \(t>0\)，于是 \(u<t\) 且

\[
(t+u)(t-u)\ge\alpha\mu(t)s^2,\qquad \alpha s\le\frac{2t}{\mu(t)\chi(t)}(t-u)\le\int_u^t\overline h(v)\,dv.
\]

对任意有限前缀望远镜求和，所有新点距 \(z^0\) 不超过 \(\Theta(t_0)\)，且到 \(S\) 的距离不增。这使覆盖假设可归纳使用。该闭球包含于 \(U\)，故有限长度使极限落在 \(U\)。若 \(t_k\downarrow t_*>0\)，在 (7) 中 \(\mu(t_k)s_k^2\ge (\inf_{[t_*,R]}\mu)\chi(t_*)^2>0\)，与 \(\sum_k\alpha_k=\infty\) 矛盾。闭性给出 \(z^\infty\in S\)。由 (6) 得 \(D(t)\le \|V\|t^2\)，再用 (3) 得

\[
s\le M t,\qquad M=\frac{1+\sqrt{1+4\eta\|V\|}}{2\eta}.
\tag{9}
\]

因此 \(s_k\to0\)，\(d(\widehat z^k)\le(1+M)t_k\)，且 \(\|\widehat z^k-z^\infty\|\le\Theta(t_k)+Mt_k\)。如输出误差界只在 \(\widehat z\in U\) 成立，可先用 (3) 的步长界校准输出所在区域。一个充分窗口是预先有 \(D(t)\le\varepsilon t^2\)，并用相应的 \(M=m_\varepsilon(\eta)\) 令 \(\Theta(t_0)+Mt_0<d(z^0,U^c)\)。这一步使用的 (3) 来自锚定，与输出误差界无关。\(\square\)

**直接后果。** 一步净耗散还给 \(\sum_{k:t_k>0}\alpha_k\mu(t_k)s_k^2\le t_0^2\)，并允许用所累积的 \(\alpha\) 衡量距离率。令 \(L(t)=\mu(t)\chi(t)^2/(2t)\)，则 \(t_{k+1}\le t_k-\alpha_k L(t_k)\)。若 \(L\) 有正的非减下包络 \(\underline L\)，令 \(H(t)=\int_t^R dv/\underline L(v)\)。在到达零前有 \(H(t_k)\ge H(t_0)+\sum_{j<k}\alpha_j\)。若 \(\inf_k\alpha_k>0\)，(8) 还给 \(\sum_k s_k<\infty\)。这时约化影子的总长亦有限，因为相邻影子步可由相邻迭代步与 \(s_k+s_{k+1}\) 相加控制。

**直接积分的另一条件。** 若 \(\mu(t)\chi(t)\) 有正的非减下界 \(m(t)\)，且 \(2t/m(t)\) 可积，则可取 \(\Theta(t)=\int_0^t2v/m(v)\,dv\)。从 (7) 的平方耗散得 \(\alpha s\le(t^2-u^2)/[\mu(t)\chi(t)]\le\Theta(t)-\Theta(u)\)。固定比例吸收和下文的 \(\gamma\ge\chi^\kappa\) 分别可用 \(m=\theta g_0\chi\) 和 \(m=\theta\chi^{1+\kappa}\)。

**保留正锚项。** 若 \(\gamma\ge g(t)\ge0\)，在可行的正距离上定义

\[
\omega(t)=\inf_{\chi(t)\le s\le B_{\eta,D}(t)}\left[g(t)s+\frac{2\Phi(t)}s\right].
\]

由 (2) 得 \(t^2-u^2\ge\alpha s\omega(t)\)。若 \(\omega(t)>0\) 且 \(2t/\omega(t)\) 有非增可积上包络，以上有限长度证明仍适用。极限识别所需的远离零条件改为 \(\chi(t)\omega(t)\) 在相应闭区间有正下界，仍需 \(\sum_k\alpha_k=\infty\)。当 \(\Phi=-D\) 时 \(\omega=\mu\chi\)。当 \(\Phi(t)>0\) 且 \(g(t)=0\) 时有 \(\omega(t)\ge2\Phi(t)/B_{\eta,D}(t)\)，因而正锚项可以在松弛上限提供净耗散。

**与原一般函数条件的关系。** 取默认 \(V=I,\alpha=1\)，并设 \(\psi_\lambda(s)=\psi(s/\lambda)\) 来吸收普通 PPA 参数。附件的逆模 \(b(t)=\lambda\psi^{-1}(t)\) 在 \(b(t/2)\le t/2\) 时满足 \(b(t/2)\le (I+\psi_\lambda)^{-1}(t)\)，因为 \(\psi_\lambda(b(t/2))=t/2\)。原 F2 保证前一不等式在小窗成立。原 F1 即给 \(2D(t)\le\tfrac12\chi(t)^2\)，原 F3 给 (7) 的可积上包络。直接用 \(\chi\) 可以涵盖线性及混合模，并省去 F2 和两种下降幅度的分类。对归一化模 \(\psi(s)=K s^\vartheta\)，\(1/2<\vartheta<1\)，有 \(\chi(t)\sim K^{-1/\vartheta}t^{1/\vartheta}\)。固定间隙 \(\gamma\ge g_0>0\) 时，若 \(D(t)\le Ct^p\)，条件为 \(p>2/\vartheta\)，或 \(p=2/\vartheta\) 且 \(2C<g_0K^{-2/\vartheta}\)。长度势可取常数倍 \(t^{2-1/\vartheta}\)。普通 PPA 再把 \(K\) 换成 \(K/\lambda^\vartheta\)，得到 C399-v1 的严格临界常数。

**可执行的近上限松弛。** 对 \(s>0\)，取 \(\alpha=2\beta-\min\{s^\kappa,\eta\}\)，\(\kappa>0\)。在缩小后的小窗，由 (9) 可用 \(\gamma=s^\kappa\ge\chi(t)^\kappa\)。若 \(2D(t)\le(1-\theta)\chi(t)^{2+\kappa}\) 且 \(0<\theta<1\)，则 (6) 有 \(\mu(t)\ge\theta\chi(t)^\kappa\)。对于 \(\psi(s)=K s^\vartheta\)，\(1/2<\vartheta<1\)，取 \(0<\kappa<2\vartheta-1\)，长度势为常数倍 \(t^{2-(1+\kappa)/\vartheta}\)。由于 \(\alpha\ge\eta\)，距离及点误差上界是

\[
t_k=O(k^{-1/\nu}),\qquad
\|z^k-z^\infty\|+\|\widehat z^k-z^\infty\|=O(k^{-[2-(1+\kappa)/\vartheta]/\nu}),\qquad
\nu=\frac{2+\kappa}{\vartheta}-2.
\tag{10}
\]

从 (7) 先得 \(t_k-t_{k+1}\ge c\alpha_k t_k^{1+\nu}\)，再用凸函数 \(t^{-\nu}\) 得 (10)。\(D(t)\le Ct^p\) 时，上述缺陷门在 \(p>(2+\kappa)/\vartheta\) 成立。在临界指数，严格常数 \(2C<K^{-(2+\kappa)/\vartheta}\) 即可缩窗满足。该规则可以使 \(\alpha_k\to2\beta_k\) 且 \(\delta_k\to0\)，其耗散无需 \(\inf_k\delta_k>0\)。

<a id="dd2-all-anchor"></a>
## 3. 全锚 Fejér、平方和与遍历界

设对每个允许步与每个 \(w\in S\) 有

\[
\langle q^k,z^k-w\rangle\ge\beta_k s_k^2+L_w(z^k)-e_k,\qquad L_w\ge0,\ e_k\ge0,
\tag{11}
\]

其中 \(e_k\) 与 \(w\) 无关。展开同一个固定锚的平方距离得

\[
\|z^{k+1}-w\|^2\le\|z^k-w\|^2-\delta_k s_k^2-2\alpha_k L_w(z^k)+2\alpha_k e_k.
\tag{12}
\]

在 \(e_k=0\) 或 \(2\alpha_k e_k\le(1-\theta)\delta_k s_k^2\) 的情况下，迭代对 \(S\) Fejér 单调。后一情况的净平方和权重可用 \(\theta\delta_k\)。在只知道 \(\sum_k\alpha_k e_k<\infty\) 时，迭代是有界的并且对 \(S\) 拟 Fejér。加上误差的尾和后，(12) 表明每个固定锚的平方距离收敛。还得到

\[
\sum_{k=0}^N \bigl[\delta_k s_k^2+2\alpha_k L_w(z^k)\bigr]\le\|z^0-w\|^2+2\sum_{k=0}^N\alpha_k e_k .\tag{13}
\]

若 \(\liminf\delta_k>0\)，则 \(s_k\to0\)。若此外 \(\mathcal F\) 在零处 demiclosed，则所有弱聚点属于 \(\operatorname{zer}\mathcal F\)。如果这些弱聚点属于 \(S\)，例如 \(S=\operatorname{zer}\mathcal F\)，则固定锚距离都有极限，弱聚点唯一。具体地，若 \(w,w'\in S\) 为两个弱聚点，沿相应子序列代入 \(\|z^k-w\|^2-\|z^k-w'\|^2\) 的共同极限，得到 \(\|w-w'\|^2=0\)。有界 Hilbert 序列有弱收敛子序列，故全序列弱收敛。

若已知 \(t_k\to0\)，还有不依赖 demiclosedness 的强收敛估计。设 \(E_k=2\sum_{j\ge k}\alpha_j e_j\)。对 \(m\ge k\)，从 (12) 得

\[
\|z^m-z^k\|\le t_k+\sqrt{t_k^2+E_k}.
\tag{14}
\]

证明是先以同一 \(w\in S\) 用三角不等式估计，再取 \(\|z^k-w\|\) 的下确界。闭性使极限属于 \(S\)。在 Fejér 情形可直接取 \(E_k=0\)。这个估计给点误差，单凭它无法推出有限长度。

令 \(L_w(z)=\|U^{1/2}(z-w)\|^2\) 且 \(U\succeq0\)。由 (13) 得 \(\sum_k\alpha_k L_w(z^k)<\infty\)。若 \(\liminf\alpha_k>0\)，则 \(U^{1/2}(z^k-w)\to0\)。若 \(U\succeq\xi I\)、\(\xi>0\)，则在 \(\sum\alpha_k=\infty\) 时，固定锚距离极限和该和式给 \(z^k\to w\)。当误差全部吸收到残差项或 \(e_k=0\)，(12) 又给 \(\|z^{k+1}-w\|^2\le(1-2\xi\alpha_k)\|z^k-w\|^2\)，所以 \(\liminf\alpha_k>0\) 给点的 Q 线性率。任意可和误差只保留前面的强收敛推论。例如 \(\alpha_k=1\)，\(\mathcal F(z)=z|z|/(1+|z|)\)，\(S=\{0\}\)，\(z^0=1\) 时有 \(z^k=1/(k+1)\)。式 (11) 对 \(\beta=1,L_0(z)=\xi|z|^2,e_k=\xi|z^k|^2\) 成立。此时 \(\sum e_k<\infty\) 而点误差仅按幂次下降。

如果全锚条件写的是缺陷 \(D(\|z^k-w\|)\)，它通常只在取最近锚时变成 \(D(t_k)\)。将此代入每个固定锚的误差项需要另有一致估计。仅最近锚时 (2) 可替代固定锚估计来控制标量平方和。只要 \(W_N=\sum_{k=0}^N\delta_k>0\)，就有

\[
\min_{0\le k\le N}s_k^2\le\frac{t_0^2+2\sum_{k=0}^N\alpha_kD(t_k)}{W_N} .\tag{15}
\]

同一右端控制 \(\sum_{k=0}^N\delta_k s_k^2/W_N\)。若缺陷以固定比例吸收，则右端可换成 \(t_0^2/(\theta W_N)\)。若 \(\sum\delta_k s_k^2<\infty\) 且 \(W_N\to\infty\)，从任意固定索引后的尾段应用相同最小值不等式，得到 \(\min_{k\le N}s_k=o(W_N^{-1/2})\)。这也给输入和影子的相应真残差的最佳前缀上界。当 \(\inf\delta_k>0\)，算术平均的残差范数和残差向量平均范数都为 \(O(N^{-1/2})\)，由尾段 Cauchy–Schwarz 还能得 \(o(N^{-1/2})\)。

松弛加权的残差向量另外满足恒等式

\[
\frac{\sum_{k=0}^N\alpha_kq^k}{\sum_{k=0}^N\alpha_k} = \frac{z^0-z^{N+1}}{\sum_{k=0}^N\alpha_k}.
\tag{16}
\]

Fejér、拟 Fejér 或有限长度都可以给分子所需的有界性。在 \(\liminf\alpha_k>0\) 时得到 \(O(N^{-1})\) 的向量平均率。向量平均允许抵消，(16) 单独没有范数平均、最后残差或平均迭代点真残差的含义。

## 4. 线性误差界与距离率

令 \(D(t)\le\varepsilon t^2\)。仍可用最近锚来证明如下两个一步因子。

| 误差界 | 记号 | 一步平方距离估计 |
| --- | --- | --- |
| 输入 \(t\le c s\)，\(c>0\) | \(\Delta=\delta-2\alpha\varepsilon c^2\) | \(u^2\le(1-\Delta/c^2)t^2\) |
| 影子 \(a\le\widehat c s\) | \(b=\widehat c+|1-\alpha|\)，\(\Delta=\delta-2\alpha\varepsilon b^2\) | \(u^2\le(1-\Delta/(b^2+\delta))t^2\) |

第一行把 \(s\ge t/c\) 代入 (2)。第二行由 \(u\le bs\) 与 (2) 消去 \(s\)。当 \(b=0\) 时 \(u=0\)，无需除法。若所有允许选择的 \(\Delta\ge\kappa_0>0\)，由于 \(\delta\le\|V\|^2\)、\(b\le\widehat c+1+2\|V\|\)，可取一个统一 \(\rho<1\) 使 \(u\le\rho t\)。计算因子若为负，只可能是该参数下没有正距离允许步，可以取零作为因子。由 (3) 得 \(s\le m_\varepsilon(\beta)t\)，其中 \(m_\varepsilon(v)=(1+\sqrt{1+4v\varepsilon})/(2v)\)。令 \(M=m_\varepsilon(\eta)\) 和 \(\Gamma=2\|V\|M/(1-\rho)\)。则总长和尾长分别至多 \(\Gamma t_0\)、\(\Gamma t_k\)，且

\[
\|z^k-z^\infty\|\le\Gamma t_k,\qquad \|\widehat z^k-z^\infty\|\le[\Gamma+m_\varepsilon(\beta_k)]t_k ,\qquad t_k\le\rho^kt_0 .
\tag{17}
\]

留域由有限前缀的几何级数证明。在锚定、覆盖和输入误差界都在 \(B_R(z^\star)\)、\(z^\star\in S\) 成立时，取 \((1+\Gamma)\|z^0-z^\star\|<R\) 即可。若误差界要求影子也留在该球，改取 \((1+\Gamma+M)\|z^0-z^\star\|<R\)。闭 \(S\) 使极限属于 \(S\)。若 \(S\) 可能非闭，但在极限处有允许值且锚定 (1) 对逼近最近点仍成立，那么 (3) 的 \(t=0\) 结论仍可识别到 \(\operatorname{zer}\mathcal F\)。当 \(\varepsilon=0\) 且全锚成立，(14) 的 Fejér 估计可将 (17) 中的点误差系数再取与 2 的较小值。一般最近锚版本给 Q 线性距离和 R 线性点误差。

<a id="dd2-adaptive-examples"></a>
## 5. 适用边界的完整算子例子

**最近锚与全锚。** 取 \(S=\{-1,1\}\subset\mathbb R\)，\(\mathcal F(z)=z-P_S(z)\)，\(\alpha=1\)。最近锚 (1) 可取 \(V=I,\Phi=0\)，影子就在 \(S\)。从 \(z^0=1/2\) 到 \(1\) 的一步增大到另一零点 \(-1\) 的距离。

**最近锚与有界性。** 在 \(\mathbb R^2\) 取原图算子 \(G(u,v)=(-v^2,v^3)\)，\(S=\mathbb R\times\{0\}\)，\(\mathcal F=I-(I+G)^{-1}\)。由于 \(I+G\) 由 \(v\mapsto v+v^3\) 加切向平移组成，它是全域同胚。对每个影子 \((u,v)\)，输入是 \((u-v^2,v+v^3)\)，最近锚 \(p=(u-v^2,0)\)。于是 \(\langle q,\widehat z-p\rangle=0\)，\(a=|v|\le\sqrt{s}\)。完整步轨道满足 \(v_k=v_{k+1}+v_{k+1}^3\) 和 \(u_{k+1}-u_k=v_{k+1}^2\)。从 \(v_0>0\) 出发，\(v_k\downarrow0\) 且

\[
v_{k+1}^{-2}-v_k^{-2}=\frac{2+v_{k+1}^2}{(1+v_{k+1}^2)^2}\longrightarrow2.
\]

故 \(v_k^2\sim1/(2k)\)，已选残差平方可和且距离趋零，切向坐标仍按 \(\tfrac12\log k\) 发散。式 (16) 的向量平均率为 \(\asymp\log N/N\)。

<a id="dd2-bounded-circular-ppa"></a>
**C447-A：有界圆聚点的完整普通 PPA 证书。** 以下把有界最近锚反例直接写回原算子，不使用方向图残差或影子残差替代它。固定 \(0<c\le1\)，取
\[
H=\mathbb R^2\times\mathbb R,\quad S=\mathbb R^2\times\{0\},\quad
\lambda=1,\quad h(v)=v+v^3,
\]
\[
f(v)=c(\cos\log|v|,\sin\log|v|)\quad(v\ne0),\qquad
b(v)=f(h(v))-f(v)\quad(v\ne0),\qquad b(0)=0,
\]
\[
F(u,v)=(b(v),v^3).
\tag{PC1}
\]
\(f\) 无需在零点定义；真正进入算子的 \(b\) 连续，因为
\[
\|b(v)\|=2c\left|\sin\!\left(\tfrac12\log(1+v^2)\right)\right|
\le c\log(1+v^2)\le cv^2.
\tag{PC2}
\]
所以 \(F\) 全域连续单值。\(h\) 是全域严格递增同胚，且
\[
(I+F)(u,v)=(u+b(v),h(v)),\qquad
J_F(U,V)=\bigl(U-b(h^{-1}(V)),h^{-1}(V)\bigr).
\tag{PC3}
\]
故完整近端全域单值连续，是一个同胚，未删任何输出；精确零集是 \(S\)，零输入驻定。对任意输出 \(y=(u,v)\)，其唯一输入是 \(x=(u+b(v),h(v))\)，最近输入锚唯一且为 \(p=(u+b(v),0)\)。因此
\[
t=h(|v|),\quad a=|v|,\quad
s=\rho=r_F(y)=\sqrt{\|b(v)\|^2+v^6},\qquad
\langle x-y,y-p\rangle=v^4-\|b(v)\|^2\ge(1-c^2)v^4\ge0 .
\tag{PC4}
\]
完整纤维只有 \(F(y)\) 这一个向量，故这里确实是真残差，不是仅给 \(\rho\le s\)。令 \(A(t)=h^{-1}(t)\) 于 \(t\ge0\)，则每条边恰有 \(a=A(t)<t\)（\(t>0\)）；任意距离窗 \(\{d(\cdot,S)\le R\}\) 对全部完整选择不变，位置窗可取 \(U=H\)。

全域有效的输出真误差模可显式取
\(\psi(r)=2\sqrt{r/c}\)。在 \(0<|v|\le1\) 时，置 \(z=\tfrac12\log(1+v^2)\)，有
\(0<z<1\)、\(\sin z\ge z/2\)、\(\log(1+v^2)\ge v^2/2\)，所以
\(\rho\ge\|b(v)\|\ge cv^2/4\)。在 \(|v|\ge1\) 时，
\(\rho\ge|v|^3\ge v^2\)，而 \(2/\sqrt c\ge2\)。零点直接成立。因此 \(a\le\psi(\rho)\) 在全部输出成立，原 E0 可取 \(\Phi=0\)。同一个图还满足更强的有符号下界
\(\Phi_c(t)=(1-c^2)A(t)^4\)；\(0<c<1\) 时它在全部正尺度为正。这是有效下界，不宣称为最佳下界。

对任意 \(v_0>0,u_0\in\mathbb R^2\)，完整唯一轨道满足
\[
v_k=v_{k+1}+v_{k+1}^3,\qquad
u_k-f(v_k)=u_0-f(v_0),\qquad
v_k\downarrow0 .
\]
后一个极限由 \(v_k\) 递减及极限方程直接得到。该轨道有界：切坐标始终在以 \(u_0-f(v_0)\) 为心、半径 \(c\) 的圆上，法坐标不超过 \(v_0\)。给定有限距离窗时只需 \(0<v_0\le R\)。

令 \(\theta_k=\log v_k\)。它严格趋于 \(-\infty\)，且
\(\theta_k-\theta_{k+1}=\log(1+v_{k+1}^2)\to0\)。对任意相位 \(\theta\)，逐个选首次越过 \(\theta-2\pi m\) 的时刻；越过误差不超过该步的相位差，故趋零。反向所有聚点的法坐标为零、切坐标在同一圆上。因此强聚点集恰为
\[
\left\{\bigl(u_0-f(v_0)+c(\cos\theta,\sin\theta),0\bigr):
0\le\theta<2\pi\right\}\subset S.
\tag{PC5}
\]
半径 \(c>0\)，所以点列不收敛，尽管到 \(S\) 的距离趋零、轨道有界、完整图和允许图都闭，且所有强聚点均在 \(S\)。

还可定量核实际步：
\[
v_{k+1}^{-2}-v_k^{-2}
=\frac{2+v_{k+1}^2}{(1+v_{k+1}^2)^2}\to2,\qquad
v_k^2\sim\frac1{2k},\qquad
s_k=r_F(x^{k+1})\sim\frac{c}{2k}.
\tag{PC6}
\]
最后一式用 (PC2) 的精确正弦式在零处给 \(\|b(v)\|\sim cv^2\)。因此实际步和完整真残差都趋零，总长仍无限；平方步和有限，也可直接由 \(\Phi\ge0\) 的同锚能量得到
\(\sum_k s_k^2\le d(x^0,S)^2\)。这个例子排除“有界、渐近正则、全部聚点入 \(S\)”在一般最近锚类中自动给点收敛。它不是对全锚 Fejér、单调算子或优化近端子类的反例；C402 的原长度定理身份不变，线性真误差界下的另一个有界完整图见 [C447-B](core.md#dd2-bounded-linear-trajectory)；两分支的算子、目标和误差模不同。半阶误差模的长度积分条件并未在本例成立：\(t=\chi(t)+2\sqrt{\chi(t)/c}\) 给 \(\chi(t)\le ct^2/4\)，所以 \(\int_0^R t/\chi(t)\,dt=\infty\)。未认定公开新颖性。

**松弛边界。** 取 \(\mathcal F(z)=z\) 和 \(S=\{0\}\)。此时 \(\Phi=0,V=I\)，影子恒为零。若 \(\alpha_k=2-2^{-k-2}\)，则 \(z^{k+1}=(-1+2^{-k-2})z^k\)，对于 \(z^0\ne0\) 模长收敛到正值，且迭代不收敛。这表明严格的逐步距离下降、\(\alpha_k<2\beta_k\) 以及 \(\sum_k\alpha_k=\infty\) 可以同时成立，而衰减的间隙不足以识别零点。若改取 \(\alpha_k=2^{-k-2}\)，虽有一致的间隙和有限长度，极限仍非零，说明 (8) 的极限识别还需要累积松弛量。

**近上限松弛的长度阈值。** 给定 \(1/2<\vartheta<1\)、\(\beta>1/2\) 和 \(\kappa>0\)。在平面写 \(r=\|z\|\)，\(e_r=z/r\)，\(e_\theta=Je_r\)，其中 \(J\) 为直角旋转。取 \(s(r)=c r\min(r,\epsilon)^{1/\vartheta-1}\)，并定义单值前向值

\[
q(z)=\frac{\beta s(r)^2}{r}e_r+s(r)\sqrt{1-\left(\frac{\beta s(r)}r\right)^2}\,e_\theta,qquad q(0)=0.
\]

取 \(c,\epsilon>0\) 使 \(\beta c\epsilon^{1/\vartheta-1}<1\) 且 \((2\beta-1)c^2\epsilon^{2/\vartheta-2}<\vartheta\)。于是 \(\|q(z)\|=s(r)\)，\(\langle q(z),z\rangle=\beta s(r)^2\)，\(T=I-q\) 的输出半径为 \(\sqrt{r^2-(2\beta-1)s(r)^2}\)。它在 \((0,\epsilon)\) 严增，在 \([\epsilon,\infty)\) 与输入半径成正比。每个圆上 \(T\) 是一次旋转和缩放，故 \(T\) 为全域同胚，原算子 \(G=T^{-1}-I\) 连续单值且完整 resolvent 为 \(T\)。唯一零点为 \(0\)，小窗影子真误差界为 \(a\le r=c^{-\vartheta}s^\vartheta\)。

令小窗内 \(\alpha=2\beta-s^\kappa\)。非驻定轨道满足 \(r_+^2=r^2-\alpha c^{2+\kappa}r^{(2+\kappa)/\vartheta}\)。从足够小的非零初值出发，\(r_k\downarrow0\)。记 \(\nu=(2+\kappa)/\vartheta-2\)，则 \(r_{k+1}^{-\nu}-r_k^{-\nu}\to\nu\beta c^{2+\kappa}\)。因此 \(r_k\asymp k^{-1/\nu}\)，实际步长 \(\alpha_k s_k\asymp k^{-1/(2+\kappa-2\vartheta)}\)。长度有限当且仅当 \(\kappa<2\vartheta-1\)。在阈值及其上，即使缺陷为零且具有优于半阶的误差界，轨道仍可能收敛而无限长。取 \(\beta=2\) 并加第三坐标 \(q_3(z)=z_3/2\)，可用 \(V=\operatorname{diag}(2,2,1)\)。完整 \(I-q\) 仍为同胚，且在小窗的影子误差界仍为 Hölder 阶 \(\vartheta\)。在平面不变子空间上，松弛趋于 \(4>2\eta\)，其中 \(\eta=1\)。

**近上限松弛的缺陷常数取等。** 在上一个平面构造中，把位移的径向系数换为 \(b(r)=\beta-s(r)^\kappa/2\)（外延区固定为 \(b(\epsilon)\)），保持矩阵 \(V=\beta I\)。缩小窗口使 \(b>1/2\)，影子半径平方变为 \(r^2-(2\beta-1)s^2+s^{2+\kappa}\)。其内窗导数为 \(2r+o(r)>0\)，外窗仍是正比例的径向映射，因此对应同一个完整单值连续原算子。选 \(\alpha=2\beta-s^\kappa\) 后有 \(\langle q,z\rangle=b(r)s^2=\alpha s^2/2\)，更新精确保半径。该例取 \(2D=s^{2+\kappa}=K^{-(2+\kappa)/\vartheta}t^{(2+\kappa)/\vartheta}\)，并保留输出 Hölder 界。因此 (10) 之前的严格临界缺陷常数不能统一放宽到等号。

**最后残差没有普适幂率。** 选严格正的可和数列 \(a_k\)，并让 \(a_{2^{j^2}}\ge j^{-2}\)。设 \(t_k=\sum_{i\ge k}a_i\)，在正半轴分段线性连接 \(\mathcal F(t_k)=a_k\)、\(\mathcal F(0)=0\)。在负半轴令 \(\mathcal F(z)=z/2\)，在 \(z\ge t_0\) 令 \(\mathcal F(z)=a_0+(z-t_0)/2\)。于是 \(\mathcal F\) 连续，\(z\mathcal F(z)\ge\mathcal F(z)^2\)，且 \(I-\mathcal F\) 连续严格递增并满射。取 \(S=\{0\},V=I,\Phi=0,\alpha=1\)，从 \(t_0\) 开始的完整轨道恰为 \(t_k\)。其长度有限，但最后残差 \(s_k=a_k\) 和点误差 \(t_k\ge a_k\) 都不存在普适的正幂上界。

**线性距离与点误差的区别。** 取 \(\rho=9/10\)、\(v_k=\rho^k\)，将 \(f(v_k)=3v_k/5\)（偶 \(k\)）和 \(f(v_k)=21v_k/25\)（奇 \(k\)）分段线性连接，令 \(f(0)=0\)，在左、右两端常值延拓。设 \(T(u,v)=(u+f(\rho v)-f(v),\rho v)\)。这是全域同胚，\(|f(\rho v)-f(v)|\le (3/10)|v|\)，因为对相邻的网格端点直接成立，端点之间的两项都线性，常值延拓区也保持该界。对 \(\mathcal F=I-T\)、\(S=\mathbb R\times\{0\}\)，最近锚内积至少为 \(\rho(1-\rho)v^2-(3v/10)^2=0\) 且 \(a\le9s\)。完整步轨道 \((f(v_k),v_k)\) 收敛到 \((0,0)\)，其距离精确满足 \(t_{k+1}=\rho t_k\)。在每个偶数步到下一步，点误差的平方却增大，因为 \(\rho^2[1+(21/25)^2]>1+(3/5)^2\)。

**迭代有限长度与影子路径。** 在平面取 \(S=\{0\}\)，\(\mathcal F(z)=\{z/2+Jz/2,z/2-Jz/2\}\)，\(V=I\)，\(\Phi=0\)。两支都满足 \(a=s=\|z\|/\sqrt 2\)。令 \(\alpha_k=1/(k+2)\)，交替取两支。则 \(t_{k+1}/t_k=\sqrt{1-\alpha_k+\alpha_k^2/2}\)，故 \(t_k\asymp k^{-1/2}\) 且迭代长度有限。相邻影子差的范数至少为 \(t_k-\|z^{k+1}-z^k\|\)，因为垂直分量交替反向且 \(\|z^{k+1}+z^k\|\ge2t_k-\|z^{k+1}-z^k\|\)。因此影子总长发散。\(\sum\alpha_k=\infty\) 和影子点收敛在这个例子都成立。

## 6. 文献定位与推论范围

Alcantara 的 Proposition 3.1（v1，pp. 7–8，式 (7)–(9)）假设相对于 \(S\) 的全锚 \((U,V)\)-半单调，且 \(U\succeq0\)、\(V\succeq\eta I\)。令 (11) 的 \(L_w(z)=\langle z-w,U(z-w)\rangle\) 且 \(e_k=0\)，便得到这里的对应 Fejér、残差平方和、遍历界和强收敛。Prop. 3.1 后的说明明确给出 \(\beta_k=\langle q^k,Vq^k\rangle/\|q^k\|^2\) 与可超过 \(2\eta\) 的松弛。将方向系数放入 DD2 最近锚需要 (1)。[Alcantara，arXiv:2611.20523v1，§3.1](https://arxiv.org/html/2611.20523v1#S3.SS1)

Proposition 3.4（v1，pp. 8–11，式 (10)–(16)）的全零集相对半单调与 \(U\succeq-\varepsilon I\) 蕴含局部最近锚上的 (1)，或经近似最近锚得到 (2)–(3)。其两种 metric subregularity 分别给 §4 的输入和影子线性误差界。上述两个平方因子来自同一展开。非线性输出误差界、按同一步耗散的长度势、可趋近方向上限的条件与相应锐例由本文推导。尚未比较所有相关公开先例，也未验证具体 Chambolle–Pock 或 Douglas–Rachford 模型具备这些函数条件。[Alcantara，arXiv:2611.20523v1，§3.2](https://arxiv.org/html/2611.20523v1#S3.SS2)

退化 PPPA 中，上文的 \(z\) 与 \(\widehat z\) 是 Proposition 4.2 的约化迭代和约化影子。闭零集或极限处覆盖负责约化识别。若对原图零点有局部锚定 Lipschitz recovery，则 \(\|\bar x^k-x^\infty\|\) 受 (8) 或 (17) 的约化点误差控制。要把路径长度传到完整影子，还需可用于相邻步的恢复估计，或独立的可和点误差上界。研究附件中的原空间传递与具体分裂模型需逐项核对允许图、零集投影和恢复条件。[Alcantara，arXiv:2611.20523v1，§§4.1、4.3–4.5、5.1](https://arxiv.org/html/2611.20523v1#S4)
