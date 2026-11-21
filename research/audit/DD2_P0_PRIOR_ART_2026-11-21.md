# P0 先行性攻击：DD2 与三组 PPA 文献的逐式边界

**审查版本。** 2026-11-21。研究基线为提交 `d6ecad745495ac851d916e79dc9acac0732ac1cf`。

本页只登记已经打开的一手版本、逐式换参和由这些换参得到的项目内推导。文献中的陈述标为 **Paper fact**，换参和差距标为 **Project derivation**。没有把“没有检索到相同标题”解释成全球优先性证明。

## 1. 固定的 DD2 对象

对一个允许边 (x\mapsto y)，记

\[
t=d(x,S),\qquad a=d(y,S),\qquad s=\|x-y\|,
\]

其中 \(S\subseteq\operatorname{zer}F\) 是闭目标，允许关系可以是
\(\mathcal J(x)\subseteq J_{\lambda F}(x)\)。DD2 的一步前件只要求存在一个最近输入锚
\(p\in P_S(x)\)，使

\[
\langle x-y,y-p\rangle\ge-D(t),
\qquad a\le \ell r_F(y),
\qquad r_F(y)=\inf_{v\in F(y)}\|v\|.
\tag{DD2}
\]

写 \(L=\ell/\lambda\)。在固定线性缺陷 \(D(t)=\nu t^2\) 时，平面引理给出

\[
(t-s)_+\le a\le \min\{t+s,\sqrt{t^2+2\nu t^2-s^2}\},
\qquad a\le Ls.
\tag{P}
\]

因此 DD2 的两个候选一步因子是

\[
C_{\rm step}(L,\nu)=L\frac{1+\sqrt{1+4\nu}}2,
\qquad
C_{\rm en}(L,\nu)=L\sqrt{\frac{1+2\nu}{1+L^2}}.
\tag{F}
\]

两者的最小值以及其达到构形是 C285/C400 的几何结论。它们不是同一个文献定理的两个编号。

## 2. Lauster--Luke 2021 的精确内容

来源为 Lauster--Luke, *Convergence of proximal splitting algorithms in \(\operatorname{CAT}(\kappa)\) spaces and beyond*, Fixed Point Theory Algorithms Sci Eng 2021:13，开放全文 [Springer HTML](https://link.springer.com/article/10.1186/s13663-021-00698-0)。下列公式按网页正文编号。

### 2.1 Paper fact：比较曲线和反演公式

文中式 (18) 要求一个函数 \(\theta\) 满足

\[
\theta(0)=0,\qquad 0<\theta(t)<t\ (t>0),\qquad
\sum_{j=1}^{\infty}\theta^{\circ j}(t)<\infty\quad(t\ge0).
\tag{LL18}
\]

式 (19) 固定 \(\tau>0\)，并以函数 \(\mu\) 隐式定义操作曲线

\[
\mu\!\left(\left(\frac{(1+\varepsilon)t^p-\theta(t)^p}{\tau}\right)^{1/p}\right)=t
\iff
\theta(t)=\left((1+\varepsilon)t^p-\tau(\mu^{-1}(t))^p\right)^{1/p}.
\tag{LL19}
\]

对线性 \(\mu(t)=\kappa t\)、\(p=2\)，文中给出

\[
\theta(t)=\sqrt{1+\varepsilon-\tau/\kappa^2}\,t,
\qquad
\sqrt{\tau/(1+\varepsilon)}<\kappa<\sqrt{\tau/\varepsilon},
\tag{LL20}
\]

其中 \(\tau=(1-\bar\alpha)/\bar\alpha\)。

定理 16(b) 的量词是：\((G,d)\) 完备 \(p\)-一致凸，\(D\subseteq G\)，\(T:D\to D\)，\(T(D)\) 在有界集上相对紧，\(S=\operatorname{Fix}T\cap D\ne\varnothing\)，并且 (T) 在每个 (y\in S) 上以同一个 \(\bar\alpha\) 和违背量 \(\varepsilon\) 点态 almost \(\alpha\)-firmly nonexpansive。若

\[
d(x,S)\le \mu(d(x,Tx))\qquad(\forall x\in D),
\tag{LL24}
\]

且 \(\mu\) 与 \(\theta\) 按 (LL19) 配对，则

\[
d(Tx,S)\le \theta(d(x,S))qquad(\forall x\in D).
\tag{LL25}
\]

于是所有初值的迭代满足 gauge-monotone 收敛，并以
\(s_k(t)=\sum_{j=k}^{\infty}\theta^{\circ j}(t)\) 控制尾误差。

### 2.2 Paper fact：有限长度和线性特例

Lemma 17 在同一 (p)-一致凸、boundedly compact、自映射框架下，从 (LL25) 和点态 almost firm 不等式推出

\[
\|x^{k+1}-x^k\|
\le
\left(\frac{2\bar\alpha(1+\varepsilon)}{c(1-\bar\alpha)}\right)^{1/p}
\theta^{\circ k}(t_0),
\qquad t_0=d(x^0,S).
\tag{LL-step}
\]

由于 (LL18) 的迭代和可和，三角不等式给 Cauchy 性和有限总长度。这里 (S) 是整个固定点集，步残差是 (|x-Tx|)。

Corollary 19(b) 将 (LL24) 取为线性误差界 (d(x,S)\le\mu d(x,Tx))，并要求

\[
\sqrt[p]{\frac{1-\bar\alpha}{\bar\alpha(1+\varepsilon)}}
<\mu<
\sqrt[p]{\frac{1-\bar\alpha}{\bar\alpha\varepsilon}}.
\]

其 (R)-线性因子为

\[
\gamma=\left(1+\varepsilon-
\frac{1-\bar\alpha}{\bar\alpha\mu^p}\right)^{1/p}.
\tag{LL-linear}
\]

### 2.3 与 DD2 的严格边界

**Project derivation 1.** 在 Hilbert 情形 (p=2)（保留文中的一致凸模常数 (c)），令 (y=Tx)、(p\in S)，则 LL 的点态 almost-firm 估计等价于

\[
\|y-p\|^2\le(1+\varepsilon)\|x-p\|^2-\tau\|x-y\|^2,
\qquad \tau=\frac{1-\bar\alpha}{\bar\alpha}.
\tag{LL-energy}
\]

利用恒等式

\[
2\langle x-y,y-p\rangle
=\|x-p\|^2-\|y-p\|^2-\|x-y\|^2,
\]

得到

\[
\langle x-y,y-p\rangle
\ge -\frac{\varepsilon}{2}t^2+\frac{\tau-1}{2}s^2.
\tag{LL-to-angle}
\]

因此只有在 \(\tau=1\)（特别是标准 firm 情形 \(\bar\alpha=1/2\)）时，LL 直接给 DD2 形式的固定函数缺陷 (D(t)=\varepsilon t^2/2)。当 \(\tau<1) 时，还需一个步长上界把 \((1-\tau)s^2/2\) 吸收进 (D(t))。当 \(\tau>1) 时可丢弃非负项得到同一上界。DD2 的最近锚量词和一般函数 (D(t)) 没有在 LL 中出现。

**Project derivation 2.** 反向方向也不成立。DD2 只对每条允许边提供一个最近输入锚，并只对实际输出使用真残差下界。它不提供 LL 所需的全部 (x\in D)、全部固定点锚 (y\in S)、单值自映射 (T:D\to D) 或相对紧性。DD2 的 (A(t)<t) 也没有 (LL18) 的迭代可和性。故 DD2 允许距离趋零而长度发散的例子，LL 的 Lemma 17 不适用。

**Project derivation 3.** 若额外假设一个完整单值 (T=J_{\lambda F})、(S=\operatorname{Fix}T)、所有固定点的 (LL-energy)、全域 (LL24)、自映射留域和 (LL18)，则 LL25 是 DD2 的一个特殊距离递推。此时它只提供一个由 (mu) 反解的 (A=\theta)，不会给 C400 的反向缺陷充要条件，也不会给两支 (C_{\rm step})、(C_{\rm en}) 的几何达到性。

## 3. Alcantara 2026 Proposition 3.4 与 Remark 3.5

来源为 Jan Harold Alcantara, *Degenerate Preconditioned Proximal Point Algorithms as Forward Methods for Nonmonotone Inclusions*, arXiv:2611.20523v1，固定版本 [PDF](https://arxiv.org/pdf/2611.20523v1)，[HTML](https://arxiv.org/html/2611.20523v1)。

### 3.1 Paper fact：全锚半单调和两个误差界

Proposition 3.4 取集合值 \(F:K\rightrightarrows K\)，解集 \(\operatorname{zer}F\ne\varnothing\)，相对 \((U,V))-半单调条件

\[
\langle q,z-w\rangle
\ge \langle q,Vq\rangle-\langle z-w,U(z-w)\rangle
\tag{A-sem}
\]

对每个 \(w\in\operatorname{zer}F\) 和每个 \(q\in F(z)\) 成立，(U\succeq-\varepsilon I)、(V\succeq\eta I)。迭代是

\[
z^{k+1}=z^k-\lambda_k q^k,qquad q^k\in F(z^k),
\]

并取方向系数 \(\beta_k\) 满足
\(\langle q^k,Vq^k\rangle\ge\beta_k\|q^k\|^2)、(0<\lambda_k\le2\beta_k)。

其式 (10) 的余量为

\[
\Delta_k=
\begin{cases}
\lambda_k(2\beta_k-\lambda_k-2\varepsilon\chi^2),&F\text{ 的误差界},\\
\lambda_k[2\beta_k-\lambda_k-2\varepsilon(\widehat\chi+|1-\lambda_k|)^2],&G=(F^{-1}-I)^{-1}\text{ 的误差界},
\end{cases}
\]

并要求存在统一 \(\kappa>0) 使 \(\Delta_k\ge\kappa)。前件是全锚、全图值的量词。(G) 版本使用 (q\in G(z-q))，因此其误差界作用在输出 (z-q) 上。

式 (11) 给出

\[
\langle q^k,z^k-w\rangle
\ge \beta_k\|q^k\|^2-\varepsilon\|z^k-w\|^2.
\tag{A11}
\]

Cauchy--Schwarz 解出的式 (12) 为

\[
\|q^k\|\le m_\varepsilon(\beta_k)d_k,
\qquad
m_\varepsilon(t)=\frac{1+\sqrt{1+4\varepsilon t}}{2t},
\qquad d_k=d(z^k,\operatorname{zer}F).
\tag{A12}
\]

式 (14) 是平方能量递推

\[
d_{k+1}^2\le(1+2\lambda_k\varepsilon)d_k^2
-\lambda_k(2\beta_k-\lambda_k)\|q^k\|^2.
\tag{A14}
\]

Remark 3.5 对普通 PPA 令 (y=J_{t\mathcal A}z)、(q=z-y)、(F_0=I-J_{t\mathcal A})、(G=t\mathcal A)、迭代松弛参数 \(\lambda_k=\beta_k=1)。若 \(\mathcal A\) 的局部 submonotonicity 缺陷为 \(\nu\)，则 (F_0) 满足 (A11) 的 \(\varepsilon=\nu)。令

\[
a=\chi_{\mathcal A}/t
\]

为 (G=t\mathcal A) 的输出误差界常数。Remark 3.5 明确给出

\[
\rho_{\mathrm A}^2
=\frac{(1+2\nu)a^2}{1+a^2},
\qquad 2\nu a^2<1.
\tag{A-R35}
\]

它同时比较了另一篇文献的较保守因子，但明确指出两套收敛定理的图量词和局部存在性不同。

### 3.2 逐式换参到 DD2

**Project derivation 4.** 在 DD2 的普通 PPA 记号中令

\[
x=z,\quad y=J_{t\mathcal A}z,\quad q=x-y,
\quad p=w\in P_S(x),\quad t_0=\|x-p\|,
\quad D(t_0)=\nu t_0^2.
\]

由于 \(q\in t\mathcal A(y)\)，输出真误差界
\(d(y,S)\le\ell r_{\mathcal A}(y)) 给出

\[
d(y,S)\le(\ell/t)\|q\|=L\|q\|.
\tag{A-to-DD2-EB}
\]

由 (A11) 有

\[
\langle q,x-p\rangle\ge\|q\|^2-\nu t_0^2,
\]

所以

\[
\langle x-y,y-p\rangle
=\langle q,x-p\rangle-\|q\|^2
\ge-\nu t_0^2.
\tag{A-to-DD2-angle}
\]

式 (A12) 因而给出 DD2 的步长支

\[
\frac{d(y,S)}{t_0}
\le L\frac{\|q\|}{t_0}
\le Lm_\nu(1)
=C_{\rm step}(L,\nu).
\tag{A-step-map}
\]

在 (G)-误差界分支下，式 (A14) 的 (b_k=\widehat\chi+|1-\lambda_k|) 在普通 PPA 变为 (b=L)，\(\delta_k=1\)，\(\Delta_k=1-2\nu L^2\)。因此

\[
\frac{d(y,S)^2}{t_0^2}
\le 1-\frac{1-2\nu L^2}{1+L^2}
=C_{\rm en}(L,\nu)^2.
\tag{A-energy-map}
\]

这证明 Alcantara 的证明中确实含有 DD1 的两个代数构件。它没有把二者取最小作为一个全参数锐定理，也没有在 \(0<L<1/2\) 的额外区间给出步长支的完整闭图达到性。Proposition 3.4 的收敛门在该固定参数下是

\[
1-2\nu L^2\ge\kappa>0,
\]

即 \(2\nu L^2<1\)，这是能量支的门。DD1 的低 (L) 步长支可以在能量门失效后仍给严格下降，属于额外几何优化，而非 Alcantara Proposition 3.4 的已陈述结论。

### 3.3 量词差异

Alcantara 要求 (A-sem) 对所有零锚 (w\in\operatorname{zer}F) 和所有 (q\in F(z)) 成立，并要求 (F) 在整个局部球内非空、每一步的选择满足统一 \(\Delta_k\ge\kappa\)。DD2 对每一条允许边只要求一个最近输入锚，允许 \(\mathcal J(x)\) 是完整预解式的子关系，并把真残差取为完整 (F(y)) 的下确界。两者的条件既不相互蕴含，也不只是符号重命名。

## 4. Li--Mordukhovich 2012 的 Hölder PPA

来源为 Li--Mordukhovich, *Hölder Metric Subregularity with Applications to Proximal Point Method*, 作者修订稿 [PDF](https://web.maths.unsw.edu.au/~gyli/papers/lm-subreg12final.pdf)，§7，印刷页 24--29。该版本实际读取到 Theorem 7.2、Theorem 7.3 和证明。

### 4.1 Paper fact：固定步长的距离率

设 (T:H\rightrightarrows H) 是 Hilbert 空间上的极大单调算子，\(\bar x\in T^{-1}(0)\)，并存在 (c,\delta>0)、\(q_{\rm LM}\in(0,1]) 使

\[
d(x,T^{-1}(0))\le c\,d(0,T(x))^{q_{\rm LM}}
\qquad(x\in B(\bar x,\delta)).
\tag{LM-EB}
\]

其 PPM 为 (x^{k+1}=(I+\lambda_kT)^{-1}x^k)。Theorem 7.2 的核心递推是

\[
d_{k+1}^2
\le d_k^2-c^{-2/q_{\rm LM}}\lambda_k^2d_{k+1}^{2/q_{\rm LM}},
\qquad d_k=d(x^k,T^{-1}(0)).
\tag{LM-7.9}
\]

Theorem 7.3(i) 在固定 \(\lambda_k\equiv\lambda>0\)、\(0<q_{\rm LM}<1\) 时给

\[
d_k=O\!\left(k^{-q_{\rm LM}/(2(1-q_{\rm LM}))}\right),
\]

而 (q_{\rm LM}=1) 给 (R)-线性率。定理还分别处理多项式增长步长和 (q_{\rm LM}=1) 的超线性情形。

### 4.2 Project derivation：2012 定理推出的有限长度范围

对固定零锚 (p\in T^{-1}(0))，firm resolvent 恒等式给

\[
\sum_{k=N}^{2N-1}\|x^{k+1}-x^k\|^2\le d_N^2.
\]

块内 Cauchy--Schwarz 和 Theorem 7.3(i) 得

\[
\sum_{k=N}^{2N-1}\|x^{k+1}-x^k\|
\le \sqrt N,d_N
\le C N^{1/2-q_{\rm LM}/(2(1-q_{\rm LM}))}.
\]

对二进制块求和可得有限总长度，只要

\[
\frac12-\frac{q_{\rm LM}}{2(1-q_{\rm LM})}<0
\iff q_{\rm LM}>\frac12.
\tag{LM-length}
\]

这是旧定理和两行 dyadic 推论，不是 Theorem 7.3 中另列的 finite-length theorem。(q_{\rm LM}\le1/2) 时该上界不决定真实轨道一定发散。(q_{\rm LM}=1) 的线性距离率直接给可和的块估计。

### 4.3 与 DD2 的对象差异

令 DD2 的输出误差界为 (d(y,S)\le K r_F(y)^q)，则在 (q=q_{\rm LM}) 的极大单调、零缺陷 (D=0) 特例中，(r_F(y)=\|x-y\|/\lambda)，所以

\[
d(y,S)\le K\lambda^{-q}\|x-y\|^q,
\]

并且 DD2 的平方能量递推退化为 (LM-7.9) 的同一标量形式。这个重合解释了 C399 的 (q>1/2) 长度阈值已有明确经典来源。

LM2012 的前件是极大单调完整图、全图真残差的局部 Hölder 次正则，且 PPM resolvent 在整个 Hilbert 空间有定义。它没有函数缺陷 (D(t))、最近输入锚选择、允许子关系、固定/非固定目标 (A(t)) 或低 (L) 步长支。DD2 的非单调严格例和同一指定 (A) 的反向预算不由 LM2012 推出。

## 5. P0 结论及论文措辞

1. **可直接承认的等价部分。** Lauster--Luke 的 (LL18)--(LL19)、Theorem 16(b)、Lemma 17 和 Corollary 19 已给出“固定点输入步残差误差界 + almost-firm 能量 + 可和比较曲线 → gauge 收敛和有限长度”的完整框架。Alcantara Proposition 3.4/Remark 3.5 已给出 DD1 两个平方估计所需的全锚半单调代数，并在普通 PPA 变量下逐式恢复 (C_{\rm step}) 和 (C_{\rm en}) 的两个因子。Li--Mordukhovich 2012 已给极大单调 Hölder PPA 的距离率，且 (q>1/2) 的有限长度可由其递推作 dyadic 推论。

2. **仍然保留的 DD2 差距。** 在本次实际读取的版本中，没有找到把 (F) 的最小值写成最近输入零锚量词下的反向缺陷充要条件，或给出低 (L) 步长支在同一完整闭图上的达到性。也没有找到把一般连续 (A(t)<t)（不要求 (LL18) 可和）与函数缺陷 (D(t)) 联立的全图定理。这个结论是“已核版本中未定位”，不是全球优先性认证。

3. **主文必须改用的限定语。** 将 DD2 的贡献写为“在选定允许关系、最近输入零锚和真实输出残差的明确量词下，给出同一步平面可行域的精确反向预算，并区分距离下降、点收敛和有限长度”。不要写“首次提出补偿机制”“首次证明 Hölder PPA 有限长度”或“文献只处理线性 (A)”。普通极大单调 (D=0) 和 (q>1/2) 长度角应引用 Li--Mordukhovich 2012，并说明 DD2 的新增范围是缺陷函数、允许关系和锐几何达到性。

4. **未关闭的优先性义务。** 仍需逐篇检查未取得全文的相关 PPA/Hölder/semimonotone 文献，以及同一几何门的非英文和后续版本。有限检索和论文内部的代数重合不能替代这项外部审查。

