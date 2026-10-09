# 全尺度结构线：先行攻击与可保留的精确候选

日期：2026-10-09。任务负责人：`structure_prior`。基线：`5726c10083cb2dbaef52e2ec802d89c8fd9d39c1`。本报告只记录独立比较，不改变 CLAIMS、FAILED_ROUTES 或 canonical 的身份/状态。附件中的加强结果另列，不在本轮升级规范结论。

## 判断

**尚不能认证全球首创。** 这次核到的最危险先行足以取消若干宽泛表述：Hilbert Hölder 映射的同常数扩张是经典；Hölder 映射存在有限误差的 Lipschitz 近似是旧结果；由一个收缩近似得到同一个强单调可逆代理、在原输入和原输出两侧有限误差配对，是旧结果的直接 Cayley 推论；任意非空紧非凸集合能够成为 Lipschitz 映射的精确固定集也有明确已发表先例。

目前最值得继续验首创的是 **C04 中精确最小 Hölder 预算的达到性**：任意紧 $K$，在全空间、值域置于 $Q=\overline{\operatorname{conv}}K$、完整固定集恰为 $K$，同时全局 Hölder 常数恰为 $D^{1-\gamma}$，其中 $D=\operatorname{diam}K$。这包括分类的闭边界 $D=R$，而非只有严格余量 $D<R$。C03 可以保留为 **经典 Kirszbraun 的精确提升推论及锐原坐标表述候选**：同一个代理在固定原输入/输出的双向误差均为 $R/\sqrt2$，并有维数一致下界；不能称全新的扩张方法，也不能借 Ciosmak 直接参照失败证明首创。

| 内容 | 本次判断 | 尚可保留的精确差别 |
|---|---|---|
| 同常数 Hölder 扩张；graph-maximal ⇔ Cayley 定义域为全空间 | 经典扩张及直接转写 | 本项目的 RL 对象解释，无独立新扩张原则 |
| 存在同一个双向有限误差强单调可逆影子 | 旧 Lipschitz approximation 加 Cayley 可直接推出 | 新意不能只写“影子存在” |
| C03 的 cross $M_\sigma/2$ 与 $R/\sqrt2$ | 已证明；可由经典 Kirszbraun 加特定正交提升直接推出 | 本次所读先行未显式给出这套 Hölder 包络、原底点双向配对及锐常数；优先性仍待查 |
| 任意紧非凸精确固定集、任意接近 1 的 Lipschitz 常数 | 已发表 Goebel 2016 Claim 1 | 不应作为 C04 宽泛新意 |
| C04 精确 $D^{1-\gamma}$ 全局 Hölder 预算、包括 $D=R$ | 规范证明已核；本次先行未覆盖预算达到性 | 当前最强结构候选 |
| C18 最大根覆盖和固定窗口完整纤维身份 | 已证明；扩张、Brouwer、标量反演的定量推论 | 保留严格半径和全称纤维身份，不把它宣传成独立新满射原则 |
| C19 有限 QP | 附件自己承认经典显式 Kirszbraun 特化 | 有限样本认证/物理坐标包装；不称全新 QP 扩张算法 |
| 附件 `cor:lipschitz_realization` | 候选加强，尚无本轮 canonical 独立入口 | 同一精确 Hölder 预算下单值 Lipschitz 零集实现、任意小投影残差扰动 |

## 1. 固定对象及经典接口

取 $0<\gamma<1$、$\lambda,L>0$，令 $R=L^{1/(1-\gamma)}$。对每个原图点写

\[
p=x+\lambda v,\qquad C(p)=x-\lambda v.
\]

全图全尺度 RL 正好等价于任意子集 $D\subset H$ 上的全局 $L$-Hölder 映射 $C:D\to H$。通过 Hilbert snowflake 的 Schoenberg 嵌入，再用 Kirszbraun–Valentine，$C$ 可扩张到全 $H$，不增 $L$。因此固定参数 graph-maximal ⇔ $D=H$，是扩张加可逆坐标代数；不是 maximal monotone 的新版本。这一点 canonical `holder_extension.md` 自己也明确不从扩张推文献新颖性。

ALM 作者 2018 预印本 Theorem 2（pp.3–4）给显式 Kirszbraun 公式；Theorem 8（pp.5–6）给 strongly biLipschitz 同常数扩张及其与 Lipschitz 变换的等价。这加强了“强单调/双 Lipschitz 结构本身是经典坐标代数”的判断，但该文并未在所读范围给一般 Hölder 数据的 sharp simultaneous shadow。注意附件引用 “Theorems 2 and 8” 是预印本编号，canonical 引正式 2021 版 Theorem 1.2；最终文稿须把版本/编号对应写清楚。

## 2. 旧 uniform Lipschitz approximation 已推出原坐标弱 shadow

Levy–Rice 1983 **Lemma 4，印刷 p.258**：具有同常数扩张性质的源/目标对上，较低 Hölder 指数的映射可以一致近似成较高指数映射。其证明直接取最大离散网，扩张网值，再用三角不等式。Hilbert 情况的 **Theorem 3 p.260、Corollary 2 p.261** 进一步给 uniformly continuous 映射的 Lipschitz 一致近似。

下面是该旧证明在当前幂模下的独立定量特化，不是声称原文使用 RL/影子术语。给定 $0<\sigma<1$，取

\[
\delta=(L/\sigma)^{1/(1-\gamma)}.
\]

在 $D$ 取最大 $\delta$-分离网 $S$。在网上

\[
\|C(a)-C(b)\|\le L\|a-b\|^\gamma
\le L\delta^{\gamma-1}\|a-b\|=\sigma\|a-b\|.
\]

Kirszbraun 扩张 $C|_S$ 到全 $H$，得同一个 $N_\sigma$，

\[
\operatorname{Lip}N_\sigma\le\sigma,\qquad
\sup_{p\in D}\|C(p)-N_\sigma(p)\|
\le 2L\delta^\gamma
=E_\sigma:=2R\sigma^{-\gamma/(1-\gamma)}.
\]

定义 $X_N(q)=(q+N(q))/2$、$Y_N(q)=(q-N(q))/(2\lambda)$。双 Banach 反演使二者满射且单射，$A=Y_N\circ X_N^{-1}$ 为强单调双 Lipschitz 同胚。常数是

\[
\operatorname{Lip}A\le\frac{1+\sigma}{\lambda(1-\sigma)},\quad
\operatorname{Lip}A^{-1}\le\frac{\lambda(1+\sigma)}{1-\sigma},\quad
\langle A(x)-A(y),x-y\rangle\ge
\frac{1-\sigma}{\lambda(1+\sigma)}\|x-y\|^2.
\]

**固定原输入。** 对原图点 $(x,v)$，取唯一 $q$ 使 $X_N(q)=x$。于是

\[
p-q=\lambda(v-A(x)),\qquad C(p)-N(q)=-\lambda(v-A(x)).
\]

因此 $\lambda\|v-A(x)\|\le E_\sigma+\sigma\lambda\|v-A(x)\|$，即

\[
\lambda\|v-A(x)\|\le\frac{E_\sigma}{1-\sigma}.
\]

**固定原输出。** 对同一原图点取唯一 $q$ 使 $Y_N(q)=v$。则

\[
p-q=x-A^{-1}(v),\qquad C(p)-N(q)=x-A^{-1}(v),
\]

同样给 $\|x-A^{-1}(v)\|\le E_\sigma/(1-\sigma)$。两边使用同一个 $N$ 和同一个 $A$，无需 graph-maximal、有限维或原图闭。优化 $\sigma=\gamma$ 得有限预算

\[
\max\{\lambda\|v-A(x)\|,\|x-A^{-1}(v)\|\}
\le \frac{2R\gamma^{-\gamma/(1-\gamma)}}{1-\gamma}.
\]

这已否定“只有本项目才能给一个同时在原输入/原输出配对的可逆强单调影子”的宽泛首创说法。错误的偷换是把同参数误差 $E_\sigma$ 直接当原坐标纤维误差；原坐标旧路线要付 $1/(1-\sigma)$ 的条件数损失。

Ajiev 2014 Part II **Lemma 10.1，印刷 p.29（PDF 第25页）** 是更明确的通用模先例：有 $(d,1)$-extension property 时，

\[
\|f-f_\varepsilon\|_\infty\le(1+2d)\omega(\varepsilon),\quad
\operatorname{Lip}f_\varepsilon\le2d\omega(\varepsilon)/\varepsilon.
\]

Hilbert $d=1$、幂模 $\omega(t)=Lt^\gamma$ 给 $E_\sigma\le3\,2^{\gamma/(1-\gamma)}R\sigma^{-\gamma/(1-\gamma)}$，再按上面 Cayley 推导即可。该通用模粗常数弱于幂模网证明；它不是 sharp cross 的先例。

## 3. C03 的 sharp cross 是经典提升的直接推论

记

\[
M_\sigma=\sup_{t\ge0}\{L^2t^{2\gamma}-\sigma^2t^2\}
=(1-\gamma)\gamma^{\gamma/(1-\gamma)}R^2\sigma^{-2\gamma/(1-\gamma)}.
\]

在 $\widetilde H=H\oplus\ell^2(D)$ 把每个 $p$ 提升成 $z_p=(p,\tau e_p)$，其中 $\tau^2=M_\sigma/(2\sigma^2)$。不同点之间的额外平方距离正好为 $2\tau^2$，故 $u(z_p)=C(p)/\sigma$ 是 1-Lipschitz。任意经典 Kirszbraun 扩张 $\widetilde u$ 的底面限制 $N(q)=\sigma\widetilde u(q,0)$ 就有

\[
\|C(p)-N(q)\|^2\le\sigma^2\|p-q\|^2+M_\sigma/2
\quad(p\in D,\ q\in H).
\]

这一步不是全新的扩张原理。Ciosmak 2024 Theorem 1.2(ii) 甚至可取合格参照 $v\equiv0$、闭凸约束集 $K=Y$（整个目标 Hilbert 空间），退回无附加约束的 Kirszbraun，直接用于该提升，同样得到精确 $M_\sigma/2$。所以不能写“Ciosmak 门不同 ⇒ 它及经典方法无法推导 C03”。

再利用上一节同输入/输出恒等式，两边统一得到

\[
\max\{\lambda\|v-A(x)\|,\|x-A^{-1}(v)\|\}
\le\sqrt{\frac{M_\sigma}{2(1-\sigma^2)}}.
\]

以 $\sigma^2=\gamma$ 优化后为 $R/\sqrt2$。这里避免了旧三角路线的 $1/(1-\sigma)$ 损失。正则单纯形完整纤维的最小包围半径为 $R\sqrt{n/[2(n+1)]}$，随维数趋于 $R/\sqrt2$；下界几何本身是经典 simplex/Jung 几何。本次未在实读的 Ciosmak、Levy–Rice、Ajiev 或 ALM 看到该 Hölder 包络加双原底点配对的明确发表陈述。**未见明确陈述不是未能直接推导，更不是优先性证明。** C03 最多保留为精确应用/锐 formulation 候选。

### Ciosmak 的有限保距约束：究竟排了什么

Ciosmak 2024 **Theorem 1.2，预印本 pp.2–3** 的充分门是：对所有有限 $m\le\dim Y$、凸权重 $t_i$，

\[
\left\|v(x_0)-\sum_i t_i v(x_i)\right\|
\le\left\|x_0-\sum_i t_i x_i\right\|.
\]

在此门下可把 Lipschitz 数据 $u$ 延拓并保留 $u-v\in K$，特别保留固定有限统一误差半径。2026 **Theorem 1.1 pp.2–3** 把该门和保距性质的等价扩展到任意 Hilbert 目标、任意 $X$；新证明是 necessity，sufficiency 仍导入 2024。2024 **Theorem 1.3 pp.4–5** 的 monotone 版本要求更强的全凸组合内积门，不能仅从 RL 或普通 pair monotonicity 自动取得。

F50/C198 的 raw Hölder 参照确实失败：$C(p)=\sqrt{(p_1)_+}e_1$，从 $0$ 到 $(0.01,0)$ 输出差 $0.1>0.01$，已违反 $m=1$ 门。但这只排“将原 $C$ 直接当合格参照”。

另选仿射参照 $v=\sigma\operatorname{Id}$ 满足相应缩放后的 barycentric 门，但在全 $H$ 上，固定任意 $p_0$，

\[
\|C(p)-\sigma p\|
\ge\sigma\|p\|-L\|p-p_0\|^\gamma-\|C(p_0)\|\longrightarrow\infty.
\]

因此有限 $\delta$ 的保距定理不能直接应用于无界全域原 $C$；在上述正交提升取参照 $\sigma P_H$ 仍有同样障碍。这不排一切 alternative reference/lift。所读文献没有声称该 affine reference 自动提供 Hölder cross $M_\sigma/2$；而无约束 Kirszbraun 提升已完整提供它。

## 4. 精确固定集：Goebel 先例击中存在性，未击中最小 Hölder 预算达到性

Schirmer 1983 §2 **Lemma，p.168** 已用距离加向固定点的凸混合产生指定 coincidence set；取 identity 给经典指定固定集思路。其 p.167 还明确报告 Robbins 1967 的 Euclidean ball 指定固定集定理。本次没有拿到 Robbins 原文正文，故不能把这当对 Robbins theorem 的一手完整核验。

更危险且已经直接读到的先例是 **Goebel，2016，Claim 1，pp.431–432**。对任意 Banach 空间中的非空闭有界凸 $Q$、非空闭 $K\subset Q$，每个 $\eta>0$ 都有 $T:Q\to Q$，

\[
\operatorname{Lip}T\le1+\eta,\qquad\operatorname{Fix}T=K.
\]

以下取 $0<\eta<1$，原文证明正是

\[
T(y)=y+\frac{\eta\,d(y,K)}{2\operatorname{diam}Q}(k_0-y),\qquad k_0\in K,
\]

并给沿线段迭代收敛；并不要求 $K$ 凸。这已是精确固定集和任意小 Lipschitz 预算超额的正式先例。

Hilbert 取 $Q=\overline{\operatorname{conv}}K$， $D=\operatorname{diam}K=\operatorname{diam}Q>0$，复合投影 $R_\eta=T\circ P_Q:H\to Q$。因为 $R_\eta(H)\subset Q$，$\operatorname{Fix}R_\eta=K$。有 $\operatorname{Lip}R_\eta\le1+\eta$ 和值域直径至多 $D$，所以

\[
\|R_\eta(x)-R_\eta(y)\|
\le\min\{(1+\eta)\|x-y\|,D\}
\le(1+\eta)^\gamma D^{1-\gamma}\|x-y\|^\gamma.
\]

这个经典实例经过 Cayley 已可实现所有 **严格余量** $D^{1-\gamma}<L$ 的紧逆纤维；正向纤维取负 Cayley 并缩放也一样。仅有任意接近最优预算不能自动推出达到最优预算：极限可能增加固定点，而且 $D=R$ 没有参数余量。

C04 的 canonical `FF-FIXEDSET` 真正额外解决的是 **超额因子从 $(1+\eta)^\gamma$ 精确降到 1，同时保留整个固定集恰为 $K$**。其承重几何为

\[
\|y-z\|^2+d(y,K)^2\le D^2\quad(y,z\in Q),
\]

对每个非固定点取严格局部距离余量，构造保持共同 $D^{1-\gamma}$ Hölder 预算的 bump，然后正权组合去掉全部多余固定点。这一达到性才使闭直径门的完整分类成立。固定点对本身还迫使任一 Hölder 常数 $B\ge D^{1-\gamma}$，故预算最小性自足。

这里的完整纤维非空紧的必要性仅已证于有限维；任意 Hilbert 的紧 $K$ 实现是充分性。不能把有限维 Brouwer/properness 的必要性整体推广到无限维。

### 附件更强的 Lipschitz 单值实现只列 candidate

附件 `01-Holder_RL_Formal_Manuscript.tex` **`cor:lipschitz_realization`，lines 875–950** 给在同一精确 Hölder 预算下，有限维每个合法紧 $K$ 可实现为单值全局 Lipschitz $F:\mathbb R^n\to\mathbb R^n$ 的完整零集，且任意 $0<\eta<1$ 可有

\[
\operatorname{Lip}F\le\frac{1+\eta}{\lambda(1-\eta)},\qquad
\sup_u\left\|F(u)-\frac{u-P_Qu}{\lambda}\right\|
\le\frac{\eta D}{\lambda}.
\]

proof 在固定集 bump 中额加 $\varepsilon_p\le\eta/M_p$，使 $R=P_Q+E\circ P_Q$、$\operatorname{Lip}E\le\eta$，然后反演 $G=(\operatorname{Id}+R)/2$。本轮查四个规范页并搜索相关词，没有发现这一加强的独立 canonical 证明入口。它不能被默认为当前 C04 已验收的加强。

Goebel 的距离混合也给 $\operatorname{Lip}(T-\operatorname{Id}_Q)\le\eta$，同样反演可推出类似单值 Lipschitz 实现与投影残差逼近，但其 Hölder 预算是 $(1+\eta)^\gamma D^{1-\gamma}$。因此附件的潜在差别依然是 **精确预算不超额且含边界**，不是单值、Lipschitz 或任意接近 projection residual 的宽泛存在性。

## 5. C18 和 C19/C20 不应承载过宽首创

C18 从每个原图点直接给 $ |s-t|\le L(s+t)^\gamma$，其中 $s=\|x-x_0\|$、$t=\lambda\|v-v_0\|$。最大根 $\rho(t)-t=L(\rho(t)+t)^\gamma$ 满足 $\rho(0)=R$；当 $r>R$ 时 $h(r)\in(0,r)$ 满足 $r-h=L(r+h)^\gamma$。经典扩张加有限维 Brouwer 满射给所有完整逆纤维在目标球 $B(v_0,h(r)/\lambda)$ 中非空且落在输入球。固定窗口相对图极大性再把 completion 的该完整纤维与原窗口纤维对齐。$C(p)=L(p_+)^\gamma$ 给严格门及半径下界。

这是有用的精确定量定理，但其存在性主骨架是扩张、sublinear perturbation of identity、Brouwer 和标量反演。未找到完全同表述先行不能证明独立新满射原则。

C19 的 finite lifted data + 严格凸 QP，与 ALM 显式 extension 路线重合。附件 §finite QP 自己明确其为 constructive Kirszbraun 的 specialization，并非新算法。C20 的同图/同尺度未知点覆盖、真实完整纤维的逐点全称门，及 noise/计算残差/QP gap 合并是实质正确的认证条件；这些条件不能从“全域代理”倒推原关系全域认证，也不能单独制造外部首创。


## 6. 实际一手阅读与未读空白

以下 DOI/URL 是公共出版者、作者或公共数学文献存档。web ref 仅供本次审计回查；parent 若在面向用户正文引用须自行 open 对应公共来源。未把第三方摘要当 theorem 核验。

| 来源 | 精确定位及本次实际读范围 | URL / web ref |
|---|---|---|
| Levy–Rice (1983), *The approximation and extension of uniformly continuous Banach space valued mappings*, CMUC 24(2),251–265 | intro251–252；Lemma2及证明253–254；Lemma4及证明258；Thm3及证明260；Cor2与remarks261。没有完整审计所有 Lp approximation proofs | [DML metadata](https://dml.cz/handle/10338.dmlcz/106224)，[原 PDF](https://dml.cz/bitstream/handle/10338.dmlcz/106224/CommentatMathUnivCarol_024-1983-2_6.pdf)；`turn17view0` / `turn75search10` |
| Ajiev (2014), Part II, Eurasian Math J5(2),7–51 | §10.1印刷29–30：Lemma10.1全文及证明、Lemma10.2陈述；后续10.2–10.6只扫描陈述，未审计。Part I只读intro7–12 | [publisher PDF](https://emj.enu.kz/index.php/main/article/download/569/371/908)；`turn32view0`, `turn41view0` |
| Ciosmak (2024), *Continuity of extensions of Lipschitz maps and of monotone maps*, JLMS110(5)e70014 | arXiv v2 intro/theoremspp1–5、Thm1.2 pp2–3、Thm1.3 pp4–5；publisher版Prop4.11 p20陈述与证明概览；未逐页审计整个24页出版版 | [DOI](https://doi.org/10.1112/jlms.70014)，[arXiv v2 PDF](https://arxiv.org/pdf/2402.14699v2)，[publisher PDF](https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/jlms.70014)；`turn12view2`, `turn35view1`, `turn58view0` |
| Ciosmak (2026), *Kirszbraun extensions preserving uniform distance in Hilbert spaces*, arXiv2607.17672v1 | 原PDF正文pp1–8：Thm1.1 pp2–3、Prop2.1 pp3–5、Cor2.2 p5、Lemma3.1 p6、mainproof pp6–8；p8example及applications只扫，pp9–17未逐项审计。web PDF parser refused，普通urllib成功下载并pdftotext实读 | [arXiv PDF](https://arxiv.org/pdf/2607.17672)，[author publications](https://sites.google.com/view/kciosmak/publications)；`turn16academia36`, `turn30view0` |
| ALM, author preprint dated2018-10-01, *Kirszbraun's theorem via an explicit formula* | Theorem2 pp3–4、Def4–Prop7、Theorem8 pp5–6陈述与相关证明；正式2021 PDF本轮超时，正式Thm1.2编号以canonical原定位为线索，不伪装本轮全读出版版 | [author PDF](https://carlosmu.folk.ntnu.no/KirszbraunViaExplicitFormula.pdf)，[2021 DOI](https://doi.org/10.4153/S0008439520000314)；`turn57view0`, `turn58view1` |
| Schirmer (1983), *Coincidence sets of coincidence producing maps*, CMB26(2),167–170 | intro167、§2Lemma168全文及距离凸混合证明；后续topological cases未审计。Robbins1967仅核其publisher metadata/abstract，未读原theorem | [DOI](https://doi.org/10.4153/CMB-1983-027-6)，[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A35B8D5002A3FBE08FF269C3643F8417/S0008439500062949a.pdf/coincidence_sets_of_coincidence_producing_maps.pdf)；`turn48view0` |
| Goebel (2016), *Remarks on fixed point sets*, Stud.Univ.Babeș-Bolyai Math61(4),429–434 | pp429–432：基本nonexpansive门、Claim1 pp431–432、精确公式及证明；pp433–434只扫描例子和references。来源PDF自身2016，搜索snippet的2017时间不取代印刷年份 | [journal original PDF](https://www.cs.ubbcluj.ro/journal/studia-mathematica/journal/article/view/159/pdf)；`turn77view0` |

尚未关闭的关键空白：Grünbaum–Zarantonello1968原文正文（ProjectEuclid返回anti-bot/HTML）；Minty1970原PDF（403）；Robbins1967原两页正文；Goebel–Prus2012 *Shapes and sizes of the fixed point sets* pp75–97 与 Bruck–Goebel1992 *Bizzare fixed point sets* pp67–70 的预算性质。没有把这些未读文献当作“已排除”。Grünbaum–Zarantonello的 [publisher定位](https://projecteuclid.org/journals/michigan-mathematical-journal/volume-15/issue-1/On-the-extension-of-uniformly-continuous-mappings/10.1307/mmj/1028999906.short) 为 DOI10.1307/mmj/1028999906，15(1),65–74；`turn75search0` 只核metadata。

可复现下载的 SHA-256（PDF只在scratch，未放repo）：

```
LevyRice1983 b6e9f7f30b2f26d04ab237da639384d920ee925e73419f5370c8a59734443f72
Ajiev2014II 4efed803f297be1ef6e1c3d8edb1473006c3e10193441eb6f01c0738741e54a0
Ciosmak2024 3a1572424b2638a712d4e512906d445daa37d34d8ec9e774c175fc417973dec1
Ciosmak2026 e2546b6fddf9d52a42619668983752ee1decbca73fd5153d4c9f5be053d7b502
ALM2018 48fac41b8dd88b7a8c17012b9edee62fbc50663d156f70d46bbcb6c17ad68051
Schirmer1983 a6ad0b12522af9114fa9c10ae628675dbe161d2b7314b22e63016342e01d752e
Goebel2016 a06a259d004a971dbfced2cc0ecf233543a828c9844deb7b133672ccf545eaca
```

## 7. 独立算术核验

所有本报告展示的数值以 Python `fractions`/`math` 计算；无 Sympy 依赖。优化恒等式由有理数 $a=\gamma/(1-\gamma)$、$-a/\gamma+1/(1-\gamma)=0$ 验算，解析证明以上面公式为准。有限数值抽查不替代全参数证明。

| $\gamma$ | C03锐预算 /R | 旧幂模net + Cayley预算 /R | Ajiev通用模 + Cayley预算 /R |
|---|---:|---:|---:|
| 1/4 | 0.7071067811865475 | 4.233069471915198 | 8 |
| 1/2 | 0.7071067811865476 | 8 | 24 |
| 3/4 | 0.7071067811865475 | 18.962962962962962 | 227.55555555555554 |

另核：F50的0.01/0.1；$L=\lambda=1,\gamma=1/2,r=2$ 时 $h=(5-\sqrt{17})/2=0.4384471871911697$，满足 $2-h=\sqrt{2+h}$；simplex比值n=1,2,100分别0.5、0.5773502691896257、0.7035975447302919。$\min\{(1+\eta)h,1\}\le(1+\eta)^\gamma h^\gamma$ 在3个gamma、3个eta、5个h抽查通过；解析上由 $\min(a,b)\le a^\gamma b^{1-\gamma}$ 保证。

```python
from fractions import Fraction
from math import sqrt
for gq in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
    a = gq/(1-gq)
    assert -a/gq + 1/(1-gq) == 0
    g = float(gq); sigma = sqrt(g)
    M = (1-g)*g**(g/(1-g))*sigma**(-2*g/(1-g))
    sharp = sqrt(M/(2*(1-sigma*sigma)))
    net = 2*g**(-g/(1-g))/(1-g)
    ajiev = 3*2**(g/(1-g))*g**(-g/(1-g))/(1-g)
    assert abs(sharp-1/sqrt(2)) < 1e-12
    for eta in (.01, .1, .5):
        for h in (.01, .2, 1, 2, 10):
            assert min((1+eta)*h,1) <= (1+eta)**g*h**g + 1e-12
    print(gq, sharp, net, ajiev)
assert sqrt(.01) > .01
h = (5-sqrt(17))/2
assert abs(2-h-sqrt(2+h)) < 1e-12
for n in (1,2,100): print(n, sqrt(n/(2*(n+1))))
```

建议文稿口径：“以经典 Hilbert extension 为工具，证明 fixed-parameter Hölder–RL 类的锐双向原坐标 shadow 与精确预算完整纤维实现。”优先性表述暂写“在本次核读的先行中未见该精确预算达到性/锐双原底点陈述”，不要写“首个”“经典不能推出”或用输入门不同作为新颖性证据。
