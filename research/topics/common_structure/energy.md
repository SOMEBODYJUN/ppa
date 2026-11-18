# 非孤立原 PPA 中的凸复合增长、单调性与 KL

<a id="support-composite"></a>
## 1. 一个可计算的母对象与证明

取 \(g:\mathbb R^n\to\mathbb R^m\) 为 \(C^{1,1}\)，导数的全局 Lipschitz 常数 \(L\)，且 \(Dg(\bar x)\) 满射。取有限凸 \(\ell\)-Lipschitz \(\phi:\mathbb R^m\to\mathbb R\)，\(K=\arg\min\phi\) 含 \(g(\bar x)\)，\(m_*=\min\phi\)。模型以外层的法向增长轮廓为数据，即在 \(g(\bar x)\) 的邻域有
\[
  \phi(u)-m_*\ge c\,d(u,K)^p,\qquad p\ge1,\quad c>0 .
\]
令 \(f=\phi\circ g,\ F=\partial f,\ S=g^{-1}(K)\)，\(J_\lambda=(I+\lambda F)^{-1}\)，\(0<\lambda,\ \lambda\ell L<1\)。这里 \(\partial\) 是 limiting 子微分，\(J_\lambda\) 是不删枝的代数近端。\(S\) 可以非孤立、非凸、弯曲。满秩窗口内 \(F^{-1}(0)\) 与 \(S\) 一致。

**共同支撑式。** 有限凸外层的链式规则给 \(F(y)=Dg(y)^T\partial\phi(g(y))\)。取 \(v=Dg(y)^Tw\)、\(w\in\partial\phi(g(y))\)，凸支撑与 Taylor 余项直接给
\[
 f(z)\ge f(y)+\langle v,z-y\rangle-\tfrac L2\|w\|\|z-y\|^2 .\tag{1}
\]
将两点互换相加，在全图给 \(\langle v-v',y-y'\rangle\ge-\ell L\|y-y'\|^2\)。在 \(\bar x\) 的小窗取 \(\sigma>0\) 使 \(\|Dg(y)^Tw\|\ge\sigma\|w\|\)，则有更强的
\[
 \langle v-v',y-y'\rangle\ge-\tfrac{L}{2\sigma}(\|v\|+\|v'\|)\|y-y'\|^2 .\tag{2}
\]
这是以图值大小支付坐标曲率的次单调性。

**原近端的全覆盖。** 写 \(\rho=\ell L\)。由 (1)，\(f+\rho\|\cdot\|^2/2\) 每点有全域仿射支撑，因此凸。每一近端目标强凸且由 \(f\ge m_*\) 强制，故存在唯一全局最小点，恰为完整代数近端根。若 \(x_i=y_i+\lambda v_i\)，配对得 \((1-\lambda\rho)\|y_1-y_2\|\le\|x_1-x_2\|\)。反射恒等式
\[
 \|(2y_1-x_1)-(2y_2-x_2)\|^2
 =\|x_1-x_2\|^2-4\lambda\langle v_1-v_2,y_1-y_2\rangle
\]
给全对反射 Lipschitz 常数至多 \((1+\lambda\rho)/(1-\lambda\rho)\)。

**真实残差与 KL。** 局部满秩图表 \((g,h)\) 是微分同胚，在小矩形有 Lipschitz 逆。对 \(y\) 足够近，保持 \(h(y)\) 不动，把 \(g(y)\) 替换为 \(P_Kg(y)\)，故 \(d(y,S)\le C d(g(y),K)\)。记 \(\Delta=f(y)-m_*\)，\(d_g=d(g(y),K)\)，\(r_\phi=d(0,\partial\phi(g(y)))\)。同一个外层凸支撑给 \(\Delta\le r_\phi d_g\)，增长给 \(c d_g^p\le\Delta\)，满秩给 \(r_F(y)\ge\sigma r_\phi\)。因此
\[
 r_F(y)\ge \sigma c^{1/p}\Delta^{1-1/p}\quad(\Delta>0),\qquad
 r_F(y)\ge\sigma c\,C^{1-p}d(y,S)^{p-1}\quad(d(y,S)>0).
\]
前者是 KL，后者是完整纤维的真实余量界。\(p=1\) 的第二式是阈值 \(r_F\ge\sigma c\)，无需声称 \(t^0\) 是零连续模。满秩也意味着近处 \(0\in F(y)\iff0\in\partial\phi(g(y))\iff y\in S\)。一般闭的 \(S\) 用完备性，\(\partial f\) 的最小范数无需用于约束某个选出来的值。

**原 PPA 的局部结论和更强直接耗散。** 对任一输入 \(x\) 与其完整输出 \(y=J_\lambda(x)\)，在实际最小化目标中代入最近零点 \(z\in P_S(x)\) 得 \(s=\|x-y\|\le d(x,S)\)。这比从 \(\rho\)-次单调性单独推出的上界更紧。它只使用输入距离，输出距离版 \(B\) 可以在下一步恰好落入 \(S\) 时失败。又由 (1) 以 \(z\) 为比较点，
\[
 d(x,S)^2 \ge
 \big(1-\lambda L\|v\|/\sigma\big)\|y-z\|^2+2\lambda\Delta+\lambda^2\|v\|^2 ,
 \qquad v=(x-y)/\lambda .
\]
这里仅需 \(y\) 落入满秩和增长窗，\(z\) 可任意近点。令 \(c'=cC^{-p}\)。缩窗让 \(d(y,S)\le1,\ \lambda L\|v\|/\sigma\le \min\{1/2,\lambda c'\}\)。又 \(\Delta\ge c'd(y,S)^p\)，所以当 \(1\le p\le2\)，有 \(d(y,S)\le (1+\lambda c')^{-1/2}d(x,S)\)。步长输入界与几何级数给出留域、有限总长与点收敛。证明留域时先取一个估计球，选初值使 \(\|x^0-\bar x\|+d(x^0,S)/(1-\kappa)\) 严格小于球半径，其中 \(\kappa=(1+\lambda c')^{-1/2}\)。第 \(k\) 个输出的位置事先用输入步长界检查，然后才应用该步的距离收缩。若 \(1<p<2\)，直接由真余量与 \(s\le d(x,S)\) 得 \(d(y,S)\le C_1d(x,S)^{1/(p-1)}\)。若 \(p=1\)，\(d(x,S)<\lambda\sigma c\) 强迫 \(y\in S\)，且 \(y=P_S(x)\)；多投影与全近端唯一性矛盾。\(p>2\) 可用原 PPA 的充分下降、相对误差与上述 KL 推局部有限长，但一般无统一线性距离收缩，例如一个法向 \(|t|^p\)。

**原理论标量兼容的严格见证。** 取 \(\mathbb R^3\) 坐标 \(a,b,c\)，\(g(a,b,c)=(b-a^2/2,c)\)，\(\phi(u,v)=h(u)+|v|\)，\(h(u)=m u^2/2\) 对 \(|u|\le1\)，外面按切线延拓，\(m>0\)。于是 \(L=1,\ \ell=\sqrt{m^2+1}\)，取 \(0<\lambda<1/\ell\)，也有 \(\lambda m<1\)。\(S=\{(a,a^2/2,0)\}\)。令 \(u=q>0\) 小、\(c=0\)，取 \(v_c=0\) 的两图值以不等的 \(a,a'\) 比较，内积为 \(-m q(a-a')^2<0\)，故局部不单调。它确实非凸非光滑，原算子的纤维在 \(c=0\) 真多值。

在任何参考点 \(0\) 的局部缩窗内，纯 \(c\) 输入 \(x=(0,0,t)\) 对 \(t>0\) 小于 \(\lambda\) 有完整输出 \(y=0\)，所以任一项目 P2 模 \(\omega(t)\ge t\)，\(H(t)=(t+\omega(t))/2\ge t\)。同一窗口的 \(y=(0,b,0)\)、\(0<b<1\) 小为输入 \((0,(1+\lambda m)b,0)\) 的实际输出，其真余量 \(m b\)，且 \(d(y,S)=b\)，因为到抛物线的范数平方为 \(b^2+(1-b)a^2+a^4/4\)。于是任一合法真余量模 \(\psi(s)\ge s/m\) 对所有小 \(s>0\)。因而任一合法 \(\omega,\psi\) 都给 \(\psi(H(t)/\lambda)\ge t/(\lambda m)>t\)，旧标量兼容在任意缩窗均失败。另一方面上面的增长支撑在所有完整近端根上直接给收缩。本例严格区分的是旧整窗标量兼容的覆盖和增长支撑的覆盖。真 GMSR 在两边均成立。

**与项目 C34–C37 的重合及增量。** 项目已有满秩局部零集识别 C34、真余量拉回 C35、局部弱凸和 RL/近端 C36，以及曲面幂次/非幂次模型 C37。上面重复推导这些重合部分，是为明确模型使用的是原完整代数近端，且保持同一满秩对象。C36 的收敛前件另保 \(\Psi_F(bd)\le\kappa d\)，\(b=1/[\lambda(1-\lambda h)]\)。本文可与此分辨的量是小值曲率 \(O(\|v\|+\|v'\|)\)、基于能量增长的直接距离耗散，以及一个失败于任何旧标量真余量模的弯曲非光滑完整例。这个小值曲率来自已有 Taylor 支撑的乘子项，不能据此宣称新凸复合结构。严格见证排除的也包括 C36 以该系数的标量相容，因为纯平面法向强迫 \(\Psi_F(s)\ge s/m\)。本节未证明母对象包含一般 RLEB 或一般 KL 算子，未证明弱于任意模的 GMSR，也未给外部原创性判断。 [项目 C34–C37](../../canonical/composite_subregularity.md#cs-transfer)

## 2. 朱江醒论文与目标识别

中文名与 Jiangxing Zhu 的匹配可从厦门大学报告核实，且项目 C320 附件亦指向此文。文章为 Guoyin Li、Boris Mordukhovich、Jiangxing Zhu，*Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods*，期刊 *Mathematics of Operations Research*，DOI 10.1287/moor.2024.0570。下列定理编号依 arXiv v1。 [厦门大学](https://tianyuan.xmu.edu.cn/cn/info/1211/13275.htm) · [期刊](https://pubsonline.informs.org/doi/10.1287/moor.2024.0570) · [arXiv v1](https://arxiv.org/html/2406.13207v1)

- 定义 3.1 对 proper lsc \(f\)、\(\Gamma=(\partial f)^{-1}(0)\) 与指定 \(\bar x\in\Xi\subseteq\Gamma\)，要求 \(\psi(d(x,\Xi))\le C d(0,\partial f(x))\) 在参考点球内成立，或常数统一于目标集整管。\(\psi(0)=0\) 且 \(\psi(t_j)\to0\Rightarrow t_j\to0\)。项目常用其反函数作模，不能换错指数。Lemma 3.6 与 Thm. 3.7 对 proper lsc 凸外层、\(C^1\) 内层及参考点满秩给局部驻点皆是全局极小点。若增长模 \(\psi\) 凸、\(\psi'_+(0)=0\) 且在 \(0\) 右连续，则 GMSR 模可取 \(\psi'_+(t/2)\)，反向增长模为 \(\int_0^t\overline\psi(s)\,ds\)。该桥已包含主要满秩复合增长推正则性。 [§3](https://arxiv.org/html/2406.13207v1#S3)
- Theorem 4.3 是算法层递推。下有界 proper lsc \(f\)、有界下水平集与 BA(H0–H3) 下，代理 \(e_k\) 控制实际增量且趋于零，辅助 \(s_k\to0\)。局部有 \(s_k\le\tau(s_{k-1})\)，且 \(e_k\le\ell_1e_{k-1}+\ell_2[\xi(f_k-f_*)-\xi(f_{k+1}-f_*)]+\ell_3s_k\)，\(\ell_1<1\)。\(\tau(0)=0\)，非减并满足 \(\limsup_{t\downarrow0}\sum_{j\ge0}\tau^j(t)/t<\infty\)。望远镜给留域、有限长度及点收敛。Thm. 4.4 是 GMSR 分支，另需代理输入距离界 \(e_k\le\ell d(x_k,\Xi)\) 以及模复合 \(\tau(t)=\psi^{-1}(\gamma b\beta(\ell t))\) 的严格收缩。在 H2 后以 \(s_k=d(x_k,\Xi)\) 调 4.3。 [§4](https://arxiv.org/html/2406.13207v1#S4)
- Theorem 5.1 是 KL 分支，另有充分下降 \(f(x_{k+1})+a\varphi(e_k)\le f(x_k)\)、代理上界、H2/H3、KL 聚点和有界下水平集。再要求 (5.1) 的 Young 型兼容 \(\limsup_{(s,t)\to(0,0)}\varphi^{-1}(\beta(s)t)/(\mu_1s+\mu_2t)\le1\) 且 \(0<\mu_1<1\)。KL 与凹性给 \(e_k\le\ell_1 e_{k-1}+\ell_2\Delta\vartheta_k\)，Thm. 4.3 取 \(s_k=0\)。普通近端的 \(\varphi(t)=t^2,\ \beta(t)=t\) 用 AM–GM；一般代数近端没有原论文的充分下降保证。Example 4.6 与 Remark 5.3 的 \(f(t)=|t|^{3/2}\) 在固定步长 PPA 的真阶为二次，GMSR 分支达到二次，取 KL 指数 \(1/3\) 的通用结论只保 \(3/2\) 次。 [§5](https://arxiv.org/html/2406.13207v1#S5)
- Prop. 6.2–6.3、Thm. 6.4 和 Cor. 6.5 才是直接对象层桥。\(C^2\) 函数在二阶驻点 \(\bar x\) 若满足文中的 strict-saddle 性质，则为局部最小点。KL 与相对于 \(\operatorname{dom}\partial f\) 的连续性排除附近更高能量驻点，即 WSP。局部极小 + WSP 使小球内 \(d(x,[f\le f(\bar x)])=d(x,\Gamma)=d(x,\Theta)\)，\(\Theta=\{\nabla f=0,\nabla^2f\succeq0\}\)。对于 \(0<\theta<1\)，先由 KL 得 \(d(x,[f\le f(\bar x)])\lesssim(f-f(\bar x))^{1-\theta}\)，再代入 \(f-f(\bar x)\lesssim\|\nabla f\|^{1/\theta}\)。凸有限外层与在参考点满秩的光滑内层之 \(C^2\) 复合是 Cor. 6.5 的另一组假设。 [§6](https://arxiv.org/html/2406.13207v1#S6)
- **两种指数的原文核查。** arXiv v1 HTML 与 PDF p.17 均在 Cor. 6.5 的陈述给出距离侧 \(\psi(t)=t^{\theta/(1-\theta)}\)，证明最后一行给出余量侧 \(d\lesssim r^{(1-\theta)/\theta}\)。按 Definition 3.1，两式等价。Example 6.6 的 \(\theta=3/4\) 对应 \(\psi(t)=t^3\)。检验 \(f(t)=t^4\) 的真余量 \(4|t|^3\) 与该方向一致，并排除把 \(1/3\) 放到距离侧的误读。 [arXiv v1 HTML §6](https://arxiv.org/html/2406.13207v1#S6) · [arXiv v1 PDF p.17](https://arxiv.org/pdf/2406.13207v1#page=17)

<a id="support-kl-gmsr"></a>
## 3. 可脱离凸复合的结构转换

设 \(f\) proper lsc，\(\bar x\in(\partial f)^{-1}(0)\)。固定一空间球、一个图值截断 \(\epsilon>0\) 及 \(\gamma\ge0\)，假定对球内 \(y,z\) 与所有 \(v\in\partial f(y)\cap\overline B(0,\epsilon)\) 有
\[
 f(z)\ge f(y)+\langle v,z-y\rangle-\gamma\|v\|\|z-y\|^2 .\tag{3}
\]
式 (3) 直接导出小余量片的两点次单调性 (2)；令 \(v=0\) 又迫使球内任一零点都是同值局部极小点。特别地，\(\bar x\) 本身使 \(f\ge m_*=f(\bar x)\) 在球内成立。记 \(S=(\partial f)^{-1}(0)\)。小窗内 \(S\) 与 \(C=[f\le m_*]\) 一致（局部极小点满足 Fermat），因此通过参考点与边界的距离隔离，二者在更小窗口的距离相同，最近点可在局部闭的 \(C\) 取得。

固定 \(q>0\)。在同一对象类的这一结构下，有
\[
 {\rm KL}\big(q/(1+q)\big)\quad\Longleftrightarrow\quad
 d(y,S)^q\lesssim r_F(y)
\]
在适当缩窗成立。右到左可用 (3) 比较最近零点 \(z\)。取范数趋近 \(r_F(y)\) 的图值，若 \(r_F(y)<\epsilon/2\)，则 \(\mathrm{gap}\le r_F(y)d(y,S)[1+\gamma d(y,S)]\lesssim r_F(y)^{1+1/q}\)；若 \(r_F\ge\epsilon/2\)，正值带上的 KL 下界自动可取得。左到右先用 Ekeland 得值误差界。具体地，令 \(\theta=q/(1+q)\)，\(\chi(s)=s^{1-\theta}/[c(1-\theta)]\) 其中 \(r_F\ge c\,s^\theta\)。在原球的闭子球上应用于 \(E(y)=\chi(f(y)-m_*)\)，对 \(0<E(x)<d(x,C)\) 取位移半径严格夹在两者之间且不出闭子球内部，小能量、近输入保证存在该半径。得 \(y\notin C\)、\(E(y)\le E(x)\)，且加在 \(E\) 上的范数扰动 Lipschitz 常数小于 1。Fermat、Lipschitz 和规则、正值点的光滑复合规则给 \(r_E(y)<1\)，与 KL 矛盾。故在正值窄带有 \(d(x,C)\le\chi(f(x)-m_*)\)。与 KL 合成，给 \(d(x,S)^q\lesssim r_F(x)\)。完整缩窗中的能量过滤可由 (3) 自身得到。若 \(r_F(y)<\epsilon/2\)，取 \(\|v\|<\epsilon\)，用 \(z=\bar x\) 得
\[
0\le f(y)-m_*\le\epsilon\big(\|y-\bar x\|+\gamma\|y-\bar x\|^2\big).
\]
故足够近的这类点自动进入 KL 能量带或最小水平。若 \(r_F(y)\ge\epsilon/2\)，缩小空间球后直接用 \(d(y,S)\le\|y-\bar x\|\) 给所需幂余量界。空纤维按 \(r_F=+\infty\) 处理。

该条件是一条控制曲率的同一函数支撑不等式。它既能看成两点图不等式的来源，也能看成两类误差界的转换条件。它不承诺任意指定 \(q\) 的正则性本身。§1 的一个带增长满秩凸复合证书建立了具体 \(q\)，并解决完整近端覆盖。一般 (3) 下，大余量根的排除和完整覆盖必须另查。若 \(f\) 在 \(y\) 可微，分别取 \(z=y+th\) 和 \(z=y-th\) 后让 \(t\downarrow0\)，则任何被接纳的 \(v\) 都必等于 \(\nabla f(y)\)。因而不能把 (3) 直接改写成任意原图 \(F\) 搭配一个光滑势，并指望覆盖纯斜算子（如项目 C313 的相关分支）。这里的成立机制确实使用一阶可积性。

### 同一桥的文献坐标

| 原文定位 | 精确结论或范围 |
|---|---|
| Bolte–Daniilidis–Ley–Mazet，*Characterizations of Łojasiewicz inequalities*, Theorem 2、Corollary 4、Remark 5、Lemma 43 | 对完备度量空间上的 lsc \(f\)，在非空正能量带，去奇异后 epigraph 映射的 metric regularity、正下水平集映射对于 \(d_\chi(r,s)=|\chi(r)-\chi(s)|\) 的 Hausdorff Lipschitz 性、去奇异能量的 strong slope 下界等价。对 semiconvex，strong slope 等于到次微分的距离。一般 lsc 属于 slope 版本，需要额外理由改成 limiting-subgradient 版本。这里映射的逆像随能量水平移动，有别于 \(\partial f\) 的固定零逆像。 [AMS 原文](https://www.ams.org/journals/tran/2010-362-06/S0002-9947-09-05048-X/S0002-9947-09-05048-X.pdf) |
| Bolte–Nguyen–Peypouquet–Suter，*From error bounds…*, Theorem 5、Corollary 6、§6 | 对可达最小值零的 proper lsc 凸 \(f\)，KL 去奇异函数给同窗值误差界 \(d(x,S)\le\chi(f(x))\)。反向的条件含 \(\chi\) moderate，即 \(s\chi'(s)\ge c\chi(s)\)，及原定理指定的层集/空间量词。幂次满足 moderate；§6 的极平例排除任意值误差界的裸反向。 [作者稿](https://optimization-online.org/wp-content/uploads/2015/10/5176.pdf) |
| Pan–Liu，*Subregularity… and KL property of exponent 1/2*, Thm. 3.1、Prop. 3.1–3.2、Thm. 3.2 | 凸情形点态 MSR ↔ QG → KL(1/2)，参考点连续时反向也成立。连续局部极小点的 KL(1/2) 给 QG 与 MSR，无需预设 prox-regularity。非凸反方向的支持条件为 uniform prox-regular，且附近相应驻点能量不高于参考值（Assumption 3.1）。最近驻点 \(z\) 给 \(\mathrm{gap}\le r\,d+(\rho/2)d^2\)，线性 MSR 给二次余量上界。局部最小点集和全临界集版本的等价各有自身条件。 [v3 原文](https://arxiv.org/pdf/1812.00558v3) |
| Drusvyatskiy–Lewis，*Error bounds, quadratic growth, and linear convergence of proximal methods*, Thm. 3.3–3.4 | 闭凸 \(h\) 同一初始下水平集内，QG 系数 \(\alpha/2\) 给次梯度 EB 常数 \(2/\alpha\)，EB 常数 \(L\) 给任意 \(0<\alpha\le1/L\) 的 QG。次梯度 EB 给 \(d(x,S)\le(L+t)t^{-1}\|x-\mathrm{prox}_{t h}(x)\|\)，逆向取近端 EB 的系数。这里的确有极大单调原近端。 [期刊文本](https://sites.math.washington.edu/~ddrusv/error_bound_sub.pdf) |
| Drusvyatskiy–Ioffe，*Quadratic growth and critical point stability of semi-algebraic functions*, Thm. 3.1、Examples 3.2–3.3 | 半代数 lsc 局部极小点，强 MSR 给强 QG，逆向附加在 \((\bar x,0)\) 的次微分连续性。Example 3.2 的高低层函数说明条件的必要性；该定理的点距离不能直接替换成非孤立集距离。 [期刊文本](https://sites.math.washington.edu/~ddrusv/second_order_MPA.pdf) |
| Khanh–Mordukhovich–Phat，*Variational Convexity…*, Lemma 3.1、Thm. 3.2、Prop. 2.9 | 变分凸通过带值过滤的局部次微分单调性刻画；对 lsc prox-bounded \(f\)，等价于在 \((\bar x,\bar v)\) 的 prox-regularity 加小步 Moreau envelope 在 \(\bar x+\lambda\bar v\) 附近的凸性。对连续 prox-regular 的 \(f\)，强变分凸、同模局部强单调及 tilt stability 等价。普通变分凸容许非孤立解但内部不携带增长率，强版本的局部唯一性排除参考点是零集聚点。 [arXiv v2 pp. 8–10](https://arxiv.org/pdf/2208.14399v2) |
| Drusvyatskiy–Lewis，*Tilt stability…*, Thm. 3.3、Examples 3.4–3.5 | 在局部极小点并对 \(0\) 次微分连续时，强 metric regularity ↔ prox-regularity+tilt stability ↔ graph-localized uniform quadratic growth；还有 prox-regularity+stable strong local minimum 的等价。两个紧邻反例分别划出次微分连续性与 prox-regularity 的范围。 [原文](https://arxiv.org/pdf/1204.5794) |

<a id="support-boundaries"></a>
## 4. 三个边界核对

**高层与完整原近端。** 取 \(x=(a,s,t)\)，\(f(a,s,0)=s^2\)，\(f(a,s,t)=1+t^2\) 对 \(t\ne0\)。全局定义限制在闭条带 \(|s|\le1/2\)，条带外取 \(+\infty\)，于是函数 proper lsc、半代数。以下计算在条带内部进行。边界 \(|s|=1/2\) 上在 \(t=0\) 的切向分量是 \(2s+N_{[-1/2,1/2]}(s)\)，不含零，故无边界零点。任一边界输出都要求输入 \(s\) 坐标绝对值至少为 \(1/2\)，不为附近输入引入远根。完整 limiting 子微分在 \(t=0\) 为 \(\{(0,2s,w):w\in\mathbb R\}\)，离面为 \(\{(0,0,2t)\}\)。平面切向差商固定前两坐标，法向正跳跃使第三坐标任意；limiting 定义的值连续序列不允许从高层添加图值。目标 \(S=\{(a,0,0)\}\) 非孤立，原点的精确 KL 指数 \(1/2\) 只看低层。对 \(0\) 的值过滤 prox-regularity 仍成立：基点只在平面，切向用凸平方支持，离面重估点有固定正跳跃覆盖小图值与位移的内积。在任意缩窗固定小 \(s\ne0\)，令 \(t\to0\)，则 \(r_F=2|t|\to0\) 而 \(d(x,S)\to|s|\)。任意零连续模的完整 GMSR 失败。

该例的完整代数近端有平面根 \((a,s/(1+2\lambda),0)\)，对 \(t\ne0\) 还有离面根 \((a,s,t/(1+2\lambda))\)。两枝对最近零锚 \(p=(a,0,0)\) 都满足 \(\|2y-x-p\|\le\|x-p\|\)，即项目 P2 可取 \(\omega(t)=t\)。离面政策从 \(s\ne0\) 趋于非零 \((a,s,0)\)，且 H3 也在该点失败。小窗的实际全局近端最小解只留低层根。同一输入两根排除了 \(\omega(0)=0\) 的全对反射控制。与 Drusvyatskiy–Ioffe Example 3.2 同源，新增此比较中真正需要的全指定模失败与完整代数近端反例。

**全对 RL、连续性与下层。** 令 \(f(a,s,t)=|s|+g(t)\)，其中 \(g=t^2\) 对 \(t\ge0\)，\(g=-e^{-1/t^2}\) 对 \(t<0\)。\(g'\) 全局 Lipschitz，故 \(f\) 弱凸，小步完整近端单值且反射 Lipschitz。\(S=\{(a,0,0)\}\)。正能量处 \(s\ne0\) 有 \(r_F\ge1\)，\(s=0\) 的正能量点只能取 \(t>0\)，此处给 KL 精确指数 \(1/2\)。沿 \(s=0,t<0\) 余量比任何距离正幂小，故没有幂次 GMSR。此例保留闭图，仍可能有非幂次 GMSR。事实上，在有限维紧子窗，完整单值连续 \(J_\lambda\) 保证零余量极限的闭性：\(y_j\to y,\ v_j\in F(y_j),\ v_j\to0\) 给 \(J_\lambda(y_j+\lambda v_j)=y_j\to J_\lambda(y)=y\)。适当缩在输入窗内，紧性排除固定正目标距离上的零余量序列，因此存在某个无预指定速率的局部零连续逆模。该定性紧性命题没有定量兼容结论。

**指数反向与二次支撑。** 给定 \(q>1\)，令 \(b(u)=\sin^2(\pi u)\)，并设
\[
 f(a,t)=\int_0^{|t|}\big[u b(\log_2u)+u^q\big]\,du,\qquad |t|<1 .
\]
它在原点附近 \(C^{1,1}\) 且弱凸，\(S=\{(a,0)\}\)。每个 \([r/2,r]\) 上 \(\log_2 u\) 跑完整周期，故 \(f\asymp |t|^2\)。余量 \(r_F\ge|t|^q\)，在 \(t_j=2^{-j}\) 恰等于 \(|t_j|^q\)，故最强距离侧 GMSR 指数恰 \(q\)。若 \(1<q<2\)，最小 KL 指数恰 \(q/2\)。若 \(q\ge2\)，也没有连续到零的凹去奇异函数：能量 \(E_j=A t_j^2+t_j^{q+1}/(q+1)\)，其中 \(A>0\) 由换元与周期性计算。凹性让 \(\chi'(s)\ge\chi'(E_j)\ge t_j^{-q}\) 在 \([E_{j+1},E_j]\) 内成立，而 \(E_j-E_{j+1}\ge (3A/4)t_j^2\)，故求和强迫去奇异函数在零附近无穷。若允许非凹去奇异，则严格增的法向原函数的逆仍奏效。一般二次亏损支撑与 \(d^q\lesssim r\) 仅给 \(\mathrm{gap}\lesssim r^{1+1/q}+r^{2/q}\)，本例表明后项会主导。式 (3) 把它降成 \(O(r^{1+2/q})\)，恢复理想指数 \(q/(q+1)\)。Bolte–Daniilidis–Ley–Mazet 的 Theorem 36 则用无穷 Hausdorff 变差的嵌套凸下水平集给 \(C^2\) 凸反例，零集为圆盘且正带无共同 KL，排除极大单调本身足以保证共同 KL。 [AMS Theorem 36](https://www.ams.org/journals/tran/2010-362-06/S0002-9947-09-05048-X/S0002-9947-09-05048-X.pdf)

<a id="support-sharp"></a>
## 5. 保持理想 KL 指数所需的曲率衰减

**精确结论。** 设 \(f:\mathbb R^n\to(-\infty,+\infty]\) proper lsc，\(\bar x\in S=(\partial f)^{-1}(0)\)。在 \(\bar x\) 的某空间球内，对所有 \(y,z\) 和 \(v\in\partial f(y)\cap\overline B(0,\epsilon)\) 要求
\[
 f(z)\ge f(y)+\langle v,z-y\rangle-\gamma\|v\|^\alpha\|z-y\|^2,
 \qquad \epsilon>0,\quad \gamma\ge0,\quad \alpha>0.
 \tag{4}
\]
对于固定 \(q>0\)，令 \(r=d(0,\partial f(y))\) 为完整纤维真残差，\(d=d(y,S)\)。在必要缩窗后，

1. KL \(\big(q/(q+1)\big)\) 推出 \(d^q\le K r\)，对任意 \(\alpha>0\) 成立。
2. 若 \(d^q\le K r\)，则当 \(\alpha\ge\max(0,1-1/q)\) 时推出同一个 KL 指数 \(q/(q+1)\)。更一般地，只要 \(\alpha+2/q>1\)，可推出
\[
\theta_*=\max\left\{\frac{q}{q+1},\ \frac{1}{\alpha+2/q}\right\}.
\]
3. 该指数在这一类的保证意义下最小。当 \(q>1,\ 0<\alpha<1-1/q,\ \alpha+2/q\le1\) 时，甚至不能保证存在凹的 KL 解奇异函数。反例有非孤立零集，原算子是连续梯度。

**证明。** 交换 (4) 中两点给小值图上的次单调亏损 \(\gamma(\|v\|^\alpha+\|v'\|^\alpha)\|y-y'\|^2\)。因为 \(\alpha>0\)，在 \(v=0\) 恢复共同极小水平。第 3 节的 KL 到距离误差界证明照用。缩窗时，小残差点能进入 KL 能量带，因为以 \(\bar x\) 为比较点，在 \(\|v\|\le\epsilon\) 下有 \(f(y)-f(\bar x)\le\epsilon\|y-\bar x\|+\gamma\epsilon^\alpha\|y-\bar x\|^2\)。大残差点直接由 \(d\le\|y-\bar x\|\) 处理。

反向比较最近零点并令小图值范数趋近 \(r\)，得
\[
 f(y)-f(\bar x)\le r d+\gamma r^\alpha d^2
       \le C\left(r^{1+1/q}+r^{\alpha+2/q}\right).
\]
最近零点存在于共同窗口，理由同第 3 节。若 \(r\ge\min(1,\epsilon/2)\)，在有限正能量带内直接调整 KL 常数。若 \(r\) 更小，支配项的指数是 \(\min(1+1/q,\alpha+2/q)\)。它大于 1 时取倒数，得到声称的幂指数。若要取理想指数 \(q/(q+1)\)，从 \(\alpha+2/q\ge 1+1/q\) 得阈值。对于 \(\alpha=0\) 的固定亏损，\(v=0\) 不再自动识别共同最小水平。可在另加该识别后使用同一上界和下述反例，将 \(r^0\) 的亏损约定为常数。

**下界。** 当 \(\alpha\ge\max(0,1-1/q)\)，一维法向的凸函数 \(f(a,t)=|t|^{q+1}/(q+1)\) 满足 (4)，且正则和 KL 的指数恰取等。对于 \(q>1,\ 0\le\alpha<1-1/q\)，置 \(p=1+q\alpha<q\)，取在 \(|t|<1\) 的
\[
 f(a,t)=h(t),\qquad
 h(t)=\int_0^{|t|}\big[u^q+u^p\sin^2(\pi\log_2 u)\big]\,du .
\]
可用接合斜率的外侧凸二次延拓将 \(h\) 定义在全实轴，局部计算不受影响。其零集为横轴，\(h\) 为 \(C^{1,1}\)。由 \(t\) 到 \(t/2\) 的积分覆盖一个完整振荡周期，\(h(t)\asymp |t|^{p+1}\)。正则余量 \(|h'(t)|\ge |t|^q\)，在 \(t_j=2^{-j}\) 取等。令 \(y\) 的法向坐标为 \(t\ne0\)。当 \(z\) 的法向坐标 \(s\) 满足 \(|s-t|\le |t|/2\)，Taylor 线上 \(|h''|\le C|t|^{p-1}\)；当 \(|s-t|>|t|/2\)，直接用 \(h(s)\ge0\)、\(h(t)\le C|t|^{p+1}\)、\(|h'(t)|\le C|t|^p\) 给
\[
h(t)+h'(t)(s-t)-h(s)\le C'|t|^{p-1}|s-t|^2 .
\]
在 \(t=0\) 用 \(h(s)\ge0\)。又 \(p-1=q\alpha\)，所以 \(|t|^{p-1}\le |h'(t)|^\alpha\)（\(\alpha=0\) 按常数约定）。这验证 (4)。把 \(t_j\) 代入 KL，任何可取幂指数须满足 \(\theta\ge q/(p+1)=1/(\alpha+2/q)\)。

若 \(\alpha+2/q\le1\)，令 \(E_j=h(t_j)\)。任一假定的凹解奇异函数 \(\vartheta\) 须有 \(\vartheta'(E_j)\ge t_j^{-q}\)。由凹性及一整周期的正积分，
\[
\vartheta(E_j)-\vartheta(E_{j+1})
  \ \ge\ t_j^{-q}(E_j-E_{j+1})\ \ge\ c t_j^{p+1-q}.
\]
当 \(p+1-q\le0\) 时求和发散，与 \(\vartheta(0)=0\) 且有限连续矛盾。

**适用范围。** 这个阈值刻画支撑亏损在哪个精确速率下能保留真残差到 KL 的指数。它不在一般非势 \(F\) 上给出能量。若 \(f\) 光滑，把 \(z=y\pm th\) 代入 (4) 并令 \(t\downarrow0\)，每个参与的 \(v\) 必须等于 \(\nabla f(y)\)。因此不能原样施加给纯斜算子。此处的独立可解义务是找保留此阈值意义的向量图或对偶结构。公开先行性待审。

<a id="support-curved-c320"></a>
## 6. 弯曲非光滑原问题同时严格分离 C320

保留第 1 节的 \(g(a,b,c)=(b-a^2/2,c)\)、外层 \(\phi(u,v)=h(u)+|v|\)。把 \(h\) 改成不对称的两侧二次，在 \([-1,0]\) 为 \(u^2/8\)，在 \([0,1]\) 为 \(u^2/2\)，两侧外部按端点切线延拓。取 \(\lambda=1/2\)。仍有 \(\ell=\sqrt2,\ L=\sigma=1,\ \lambda\ell L<1\)，且外层近零有二次增长。完整 \(\partial(\phi\circ g)\) 在 \(c=0\) 多值，近端目标全域强凸，各输入的完整代数根恰有一个。全图反射有线性模，真实残差满足局部线性次正则。第 1 节的直接支撑证明给所有足够近的输入局部距离收缩、留域及原空间有限长度。正 \(u\) 切片的原图负配对仍排除局部单调性。

设 \(b>0\) 充分小。输入 \(x_+=(0,3b/2,0)\) 达到输出 \(y_+=(0,b,0)\)，实现原图值 \(w_+=(0,b,0)\)。距离尺度 \(t=d(x_+,S)=3b/2\)。所以 C320 在尺度 \(t\) 的每个合格对称包络都含 \(-w_+\)。另一输出 \(y_-=(0,-4b,0)\) 的完整纤维含 \(-w_+\)，因为负支斜率为 \(u/4\)。这个输出由 \(x_-=(0,-9b/2,0)\) 的完整原步达到。把 \(b\) 缩小，两输入同时落在参考原点的任意工作窗。沿法向轴，当高度 \(s<1\)，到抛物线的距离平方为 \(s^2+\min_a[(1-s)a^2+a^4/4]=s^2\)。因此
\[
d(y_-,S)=4b>\frac{3b}{2}=t>\kappa t\qquad(0<\kappa<1).
\]
两个图值违反 C320 的全纤维逆像排除，与模和缩窗无关。旧标量兼容蕴含 C320，同图也排除旧兼容。该例把中心对称性的已知失效机制放到了曲零集、非光滑、非单调的原能量问题里。支撑条件是否包含整个 C320 或整个原 RLEB 是另一命题。
