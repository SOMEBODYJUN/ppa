# 矩门与回耦损失：两个不同的概率接口

这两条命题使用不同对象。第一条是非负标量函数的矩不等式及一个 Markov 律空间反例；第二条是同一随机表示、同一输入最优运输对上的回耦条件。它们均不能从条件刷新残差 \(\mathcal R\) 自动转给同步残差 \(\Psi\)。原始线索是 [CM-M 的 Proposition M 与 Propositions 9–10](../../SOURCES.md)；以下陈述和证明可不打开历史原件而核对。

<a id="mr-moment"></a>
## C126-v1 · 全部有限支撑律的精确矩门

令 \(E\) 为可测状态集，\(e,c:E\to[0,\infty)\) 均有限可测，\(1\le p,r<\infty\)、\(q>0\)、\(K<\infty\)。假设存在 \(s,a\in E\) 使 \(e(s)=c(s)=0\) 且 \(e(a)>0,c(a)>0\)。则

\[
\|e\|_{L^p(\mu)}\le K\|c\|_{L^r(\mu)}^q
\quad\hbox{对每个有限支撑概率律 }\mu
\tag{MR1}
\]

当且仅当 **\(pq\le r\)** 且对每个 \(x\in E\) 有 \(e(x)\le Kc(x)^q\)。这里 \(c\) 是抽象非负状态残差，不预设等于 \(c_R\)、\(\mathcal R\) 或 \(\Psi\)。

**证明。** 取 Dirac 律给逐点条件；取 \((1-\varepsilon)\delta_s+\varepsilon\delta_a\) 给
\(\varepsilon^{1/p}e(a)\le K\varepsilon^{q/r}c(a)^q\)，\(\varepsilon\downarrow0\) 强迫 \(1/p\ge q/r\)。反过来，先在每个状态用逐点界，再对概率律用矩单调性：
\(\|e\|_p\le K(\int c^{pq}d\mu)^{1/p}=K\|c\|_{pq}^{q}\le K\|c\|_r^q\)。即使 \(pq<1\)，最后一步仍是非负随机变量的矩单调性，并未把它当作范数三角不等式。证毕。

**律空间障碍的精确版本。** 另令 \(S\subset\mathbb R^d\) 非空闭，\(\mathcal I\subset\mathscr P_p(S)\)，固定 \(\pi\in\mathcal I\) 和满足 \(\pi P=\pi\) 的 Markov 核 \(P\)。设非负有限状态残差 \(c\) 在 \(\pi\)-几乎处处为零；某个 \(a\) 有 \(0<c(a)<\infty\)、\(P(a,\cdot)\in\mathscr P_p\)，且
\(e(a)=(\int d(y,S)^pP(a,dy))^{1/p}>0\)。令 \(\mathcal R_r(\mu)=\|c\|_{L^r(\mu)}\)，并假设所用律均有有限的该矩。若在 \(\pi\) 的整个 \(W_p\) 邻域有
\(d_{W_p}(\mu P,\mathcal I)\le K\mathcal R_r(\mu)^q\)，则必有 \(pq\le r\)。事实上 \(\mu_\varepsilon=(1-\varepsilon)\pi+\varepsilon\delta_a\to\pi\) 于 \(W_p\)，而左边至少 \(\varepsilon^{1/p}e(a)\)，右边是 \(K\varepsilon^{q/r}c(a)^q\)。这是上述条件下的**必要性**；不声称对任意 Markov 残差、任意不变律支持或任意物理步长的普遍否定。充分性须另证实际状态上的逐点界与合法目标匹配。

<a id="mr-recoupling"></a>
## C127-v1 · 同一近极小运输对上的条件回耦界

令紧 \(K_{\rm state}\subset\mathbb R^d\)，随机自映射 \(T_\xi\) 联合可测、共享同一新噪声，核 \(P\) 的不变律集 \(\mathcal I\ne\varnothing\)。在 \(\mathscr P_2(K_{\rm state})\) 的指定类 \(\mathcal A\) 上记 \(d(\mu)=\inf_{\pi\in\mathcal I}W_2(\mu,\pi)\)，并假设**同一类**有 \(d(\mu P)\le c_0d(\mu)\)、\(0\le c_0<1\)。对每个 \(\pi\in\mathcal I\)、\(\eta\in\operatorname{Opt}_{W_2}(\mu,\pi)\)，定义

\[
D_\eta^2=\int\mathbb E\|(x-T_\xi x)-(y-T_\xi y)\|^2\,d\eta,
\quad A_\eta=\int\mathbb E\|T_\xi x-T_\xi y\|^2\,d\eta,
\quad\Delta_\eta=A_\eta-d(\mu P)^2\ge0.
\tag{MR2}
\]

此处 \(\Psi(\mu)=\inf_{\pi,\eta}D_\eta\) 正是[同步 OT 残差](../../cone_markov.md#m-psi)；输出耦合的第二边缘因 \(\pi P=\pi\) 而留在不变律集。假设对**每个** \(\mu\in\mathcal A\) 都存在这一类合法对 \((\pi_j,\eta_j)\)，使 \(D_{\eta_j}\to\Psi(\mu)\) 且对所有 \(j\) 有同一个有限 \(\chi\ge0\) 的 \(\Delta_{\eta_j}\le\chi D_{\eta_j}^2\)。则

\[
d(\mu)\le\frac{1+\sqrt\chi}{1-c_0}\,\Psi(\mu)
\quad(\mu\in\mathcal A).
\tag{MR3}
\]

**证明。** 在同一 \((x,y,\xi)\) 上拆分 \(x-y\) 为同步位移差和同步输出差，\(L^2\) 三角不等式给
\(d(\mu)\le W_2(\mu,\pi)\le D_\eta+\sqrt{A_\eta}\)。更新后的同步输出是 \((\mu P,\pi)\) 的耦合，故 \(A_\eta\ge d(\mu P)^2\)。在指定近极小对上，
\(d(\mu)\le D_{\eta_j}+\sqrt{d(\mu P)^2+\Delta_{\eta_j}}\le(1+\sqrt\chi)D_{\eta_j}+c_0d(\mu)\)。移项并令 \(j\to\infty\) 即得 (MR3)。证毕。

若在**同一**近极小对上改有 \(\Delta_{\eta_j}\le\sigma^2d(\mu)^2\) 且 \(c_0^2+\sigma^2<1\)，则同一证明给 \(d(\mu)\le\Psi(\mu)/(1-\sqrt{c_0^2+\sigma^2})\)。这不是无条件从收缩推出 EB：回耦损失必须随趋近**同一个 \(\Psi\) 下确界**的合法对受控；从别的运输对得到的损失界不能移植。\(\mathcal R\) 的条件刷新定义与 \(D_\eta\) 不同，也不得替换。上述常数是充分上界，未声称锐。

## 证据与适用边界

两项代数证明已在本页重构；CM-M 原 Proposition M/10 仅作来源谱系，外部先行性与所有原生模型中回耦门是否可验证仍未核。C126 的小质量构造与 C127 的**最优输入耦合加同噪声**是不同的概率操作；C127 不证明由固定核唯一确定 \(\Psi\)，也不把 law-space 收缩当成原算子 RL。
