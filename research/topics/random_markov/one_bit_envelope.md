# 非均匀单 bit 刷新：最小非降模与精确律空间长度

本页独立重构 CM-M Theorem 7 的标量核结论，不把它隐含在 C129 的多 bit 证书中。这里的距离、残差和长度均在固定守恒边缘的条件律空间；它们不是原同步 OT 残差 \(\Psi\)，也不是样本路径的长度。来源的弱 Poincaré 文献解释另属待核事实，不参与下文证明。

<a id="bit-object"></a>
## BIT-OBJECT · 同一核、全部初律与可实现幅度

取标准 Borel 空间 \(U\)、概率律 \(\nu\)，可测
\(b:U\to(0,1)\)、\(a:U\to(0,1]\)，条件可按 \(\nu\)-几乎处处理解。
状态为 \(U\times\{0,1\}\)。核保留 \(u\)：以概率 \(a(u)\)
独立重抽 \(\operatorname{Bern}(b(u))\)，否则保留旧 bit。
律类与目标为
\[
\mathscr M_\nu=\{\mu_r(du,dx)=\nu(du)\operatorname{Bern}(r(u))(dx):
r:U\to[0,1]\text{ 可测}\},\qquad \pi_\nu=\mu_b.
\tag{BIT1}
\]
保持 \(u\) 的条件距离和残差为
\[
\begin{aligned}
\mathsf W_\nu(\mu_r,\mu_s)^2&=\int |r-s|\,d\nu,\\
E(\mu_r)^2&=\int |r-b|\,d\nu,\\
\mathcal R(\mu_r)^2&=\int a|r-b|\,d\nu.
\end{aligned}\tag{BIT2}
\]
两个 Bernoulli 律的平方运输成本是参数差的绝对值：任何耦合的错位质量至少为边缘差，共同部分留原位、余量跨 bit 搬动取到此值。因此 BIT2 正是 C129 的 \(m=1\) 对象。

令 \(M(u)=\max\{b(u),1-b(u)\}\)。所有初律的幅度
\(h=|r-b|\) 都满足 \(0\le h\le M\)。反过来，**每个**可测这样的 \(h\) 都可实现：取
\[
r(u)=\begin{cases}b(u)+h(u),&b(u)\le1/2,\\b(u)-h(u),&b(u)>1/2.\end{cases}
\tag{BIT3}
\]
两分支均落在 \([0,1]\)，且可测。这个全幅度实现门不能由存在一条扰动律代替。

<a id="bit-modulus"></a>
## BIT-MODULUS · 全律最小非降包络

对 \(t\ge0\) 定义
\[
\phi(t)^2=\sup\left\{\int h\,d\nu:
h\text{ 可测},\ 0\le h\le M,\ \int ah\,d\nu\le t^2\right\}.
\tag{BIT4}
\]
则 \(\phi\) 是满足 \(E(\mu)\le\phi(\mathcal R(\mu))\) 对所有
\(\mu\in\mathscr M_\nu\) 成立的**最小非降**函数。
确实，BIT4 的可行集随 \(t\) 扩大，且 BIT2 给这一误差界。
若另一非降函数 \(g\) 给相同全律界，对任意 BIT4 可行 \(h\)，
BIT3 给一条 \(\mathcal R\le t\) 的律，于是
\((\int h)^{1/2}\le g(\mathcal R)\le g(t)\)。取上确界即 \(\phi(t)\le g(t)\)。

完整对偶等式是
\[
\phi(t)^2=
\inf_{\ell\ge0}\left[\ell t^2+\int M(1-\ell a)_+\,d\nu\right].
\tag{BIT5}
\]
这里 \(\ell\) 是标量对偶乘子，不是 PPA 步长；\(\lambda\) 留给原关系的步长。

**弱对偶。** 对任何可行 \(h\) 和 \(\ell\ge0\)，
\(h(1-\ell a)\le M(1-\ell a)_+\)，故
\[
\int h\,d\nu\le\ell t^2+\int M(1-\ell a)_+\,d\nu.
\tag{BIT6}
\]

**端点和原子层的强对偶。** 记 \(B=t^2\)、\(A=\int aM\,d\nu>0\)。
若 \(B\ge A\)，取 \(h=M\) 和 \(\ell=0\)，两边均为 \(\int M\)。
若 \(B=0\)，因为 \(a>0\) 几乎处处，任何可行 \(h\) 为零；
另一方面，当 \(\ell\to\infty\)，有界控制收敛给
\(\int M(1-\ell a)_+\to0\)。所以该端点也是 BIT5，
但不主张对偶 inf 在有限 \(\ell\) 取得。

若 \(0<B<A\)，令
\(F(s)=\int_{\{a\le s\}}aM\,d\nu\)，\(0\le s\le1\)。
这是有限测度 \(aM\,d\nu\) 下 \(a\) 的分布函数，非降右连续，
\(F(0)=0\)、\(F(1)=A\)。取
\(c=\inf\{s\in[0,1]:F(s)\ge B\}\)。原点右连续保证 \(c>0\)；
有限测度的上下连续性保证
\[
F(c-)=\int_{\{a<c\}}aM\,d\nu\le B\le F(c).
\tag{BIT7}
\]
在 \(a<c\) 上取 \(h=M\)，在 \(a>c\) 上取 \(h=0\)。
若 \(F(c)>F(c-)\)，在 \(a=c\) 上取
\(h=\theta M\)，\(\theta=(B-F(c-))/(F(c)-F(c-))\in[0,1]\)。
若两者相等，则它们都等于 \(B\)，取 \(\theta=0\) 即可。
所得 \(h\) 可测且成本恰为 \(B\)。取 \(\ell=1/c\)：
在三种区域，BIT6 的逐点不等式都取等，成本不等式也取等。
因此原问题取到最大值且对偶等号成立，包含有原子环境。

\(\phi(0)=0\)，且对任何 \(\epsilon>0\)，把积分分成 \(a>\epsilon\) 和 \(a\le\epsilon\)，得到
\[
\phi(t)^2\le\frac{t^2}{\epsilon}
+\int_{\{a\le\epsilon\}}M\,d\nu.
\tag{BIT8}
\]
先令 \(t\downarrow0\)，再令 \(\epsilon\downarrow0\)，因为 \(a>0\) 几乎处处，第二项趋零。
故 \(\phi(t)\to0\)。当 \(t\ge\sqrt A\)，\(\phi(t)=\sqrt{\int M}\) 饱和；
这个最小非降模不是全局严格增的 gauge。

<a id="bit-length"></a>
## BIT-LENGTH · 逐初律的精确步长和全初律绝对尾

刷新一次后 \(r_1-b=(1-a)(r-b)\)，逐次有
\(r_k-b=(1-a)^k(r-b)\)。这里 \(k=0\) 时统一取 \((1-a)^0=1\)，也包括 \(a=1\)。
由 BIT2，对每条初律及每个 \(k\ge0\)，
\[
\begin{aligned}
E(\mu_rP^k)^2&=\int(1-a)^kh\,d\nu,\\
\mathcal R(\mu_rP^k)^2
&=\mathsf W_\nu(\mu_rP^{k+1},\mu_rP^k)^2
=\int a(1-a)^kh\,d\nu\\
&=E(\mu_rP^k)^2-E(\mu_rP^{k+1})^2.
\end{aligned}\tag{BIT9}
\]
这是同一核下保持守恒变量的 law-step 精确等式；一般多 bit 或原同步 \(\Psi\) 没有由它获得这个等式。
因 \(a>0\)，控制收敛给每条初律趋于 \(\pi_\nu\)。
初律 \(h=M\) 同时实现每个时间的最大绝对误差，所以
\[
\sup_{\mu\in\mathscr M_\nu}E(\mu P^k)^2
=\int M(1-a)^k\,d\nu\longrightarrow0.
\tag{BIT10}
\]
这项**绝对**共同尾不声称在 \(\operatorname{ess\,inf}a=0\) 时有统一相对几何率；C129 的最坏相对因子仍为 1。

对指定初律，有限前缀逐项相加再取非降极限给
\[
\sum_{k\ge0}\mathsf W_\nu(\mu_rP^{k+1},\mu_rP^k)
=\sum_{k\ge0}\left[\int a(1-a)^kh\,d\nu\right]^{1/2}.
\tag{BIT11}
\]
两边都允许 \(+\infty\)；点收敛不能替代此级数的有限性。

<a id="bit-examples"></a>
## BIT-EXAMPLES · 无统一刷新下的长度与非幂边界

取 \(U=(0,1)\)、Lebesgue 概率、\(b=1/2\)、\(a(u)=u^p\)、\(p>0\)。
这里 \(p\) 是刷新剖面的指数，不是查询或 PPA 输入。
因 \(a\) 严格增，BIT7 的填充区为 \((0,s)\)，
\(s=[2(p+1)t^2]^{1/(p+1)}\)。在 \(0\le t\le[2(p+1)]^{-1/2}\)，
\[
\phi(t)=2^{-p/[2(p+1)]}(p+1)^{1/[2(p+1)]}t^{1/(p+1)};
\quad t\ge[2(p+1)]^{-1/2}\text{ 时 }\phi(t)=1/\sqrt2.
\tag{BIT12}
\]
对最远端点初律 \(h=1/2\)，对所有整数 \(k\ge1\)，
\[
E_k^2\asymp k^{-1/p},\qquad
\mathcal R_k^2\asymp k^{-1-1/p}.
\tag{BIT13}
\]
下界：对第一式只积分 \(0<u<(2k)^{-1/p}\)；
对第二式只积分 \((4k)^{-1/p}<u<(2k)^{-1/p}\)。
这些区域上 \((1-u^p)^k\ge1-ku^p\ge1/2\)，
第二个区域还满足 \(u^p\ge1/(4k)\)，给所示正下界。
上界用 \((1-u^p)^k\le e^{-ku^p}\)，换元 \(z=ku^p\)
并将积分区放大到 \((0,\infty)\)；所需的
\(\int_0^\infty z^{1/p-1}e^{-z}dz\) 和
\(\int_0^\infty z^{1/p}e^{-z}dz\) 均有限。
因此最远端点初律的律长度有限当且仅当 \(p<1\)；
因为任何其它 \(h\le1/2\)，全部初律的最大长度也恰由该律实现。

另取 \(a(u)=e^{-1/u}\)，同样 \(b=1/2\)。令
\(h_s=(1/2)1_{(0,s)}\)，\(0<s<1\)，明确取 Bernoulli 参数
\(r_s=b+h_s\)，BIT3 给合法初律 \(\mu_{r_s}\)，且
\[
E(\mu_{r_s})^2=s/2,\qquad
\mathcal R(\mu_{r_s})^2\le(s/2)e^{-1/s}.
\tag{BIT14}
\]
对每个 \(q>0\) 与有限 \(K\ge0\)，
\[
\frac{E(\mu_{r_s})}{\mathcal R(\mu_{r_s})^q}
\ge(s/2)^{(1-q)/2}e^{q/(2s)}\longrightarrow\infty.
\tag{BIT15}
\]
这些律趋于 \(\pi_\nu\)，故每个固定正半径条件距离球上的正幂 EB 都失败，
但 BIT4–8 的零点消失非降模仍成立。这是可测非均匀标量核，不声称已有有限连续随机映射的原生实现。

<a id="bit-spectrum"></a>
## BIT-SPECTRUM · 公平 bit 的指定子空间谱身份

另固定 \(b=1/2\)，令 \(\pi=\nu\otimes\operatorname{Bern}(1/2)\)。
\(L^2(\pi)\) 中逐纤维均值为零的子空间恰为
\(\mathcal H_0=\{g(u,x)=q(u)(2x-1):q\in L^2(\nu)\}\)。
条件重抽的均值为零，恒等更新概率为 \(1-a\)，故
\(Pg(u,x)=(1-a(u))g(u,x)\)。对一个初律幅度 \(0\le h\le1/2\)，取
\[
g_h(u,x)=\sqrt{2h(u)}(2x-1)\in\mathcal H_0.
\tag{BIT16}
\]
逐纤维平方与内积给
\[
\|g_h\|_2^2=2E_0^2,\qquad
\langle g_h,(I-P)g_h\rangle=2\mathcal R_0^2,\qquad
\tfrac12\|P^kg_h\|_2^2=E_{2k}^2.
\tag{BIT17}
\]
在 \(\mathcal H_0\) 上、对所有 \(\|g\|_\infty\le1\) 的函数，
指定 \(\ell\ge0\) 后的最小加性余项恰为
\[
\sup_{\substack{g\in\mathcal H_0\\\|g\|_\infty\le1}}
\{\|g\|_2^2-\ell\langle g,(I-P)g\rangle\}
=\int(1-\ell a)_+\,d\nu.
\tag{BIT18}
\]
因为左侧等于 \(\sup_{|q|\le1}\int(1-\ell a)q^2d\nu\)，
取 \(q=1_{\{1-\ell a>0\}}\) 达到右侧。
这是指定不变补空间的有界谱余项，不能省略子空间限制：
只依赖 \(u\) 的非零函数在守恒核下不衰减，属于另一个不变分量。
这些代数身份不承担外部文献比较或优先权结论。

## 身份与来源边界

C145-v1 单独登记本页 BIT1–18；C129/C130 的身份不扩写。
来源是现存 `MARKOV_PAPER_THEOREM_PACKAGE.md` Theorem 7 的 (5.8)–(5.13) 与紧邻非幂例。
本页逐项重新证明，不使用该包内部审计标签。
来源的弱 Poincaré 文献对照、外部先行性、到原 \(\Psi\) 的桥及原生连续表示仍不在本页验收范围。
