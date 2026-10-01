# 初值—极限稳定性：对象与术语映射

日期：2026-09-19。角色：术语与接口文献组；只读研究稿和原 RLEB 的实际调用接口，未重审或修改旧理论。

## 1. 结论先行

用户说的“这类次单调性”，在当前稿件中最准确的名称是 **Hölder RL 图条件**。它在 \(\gamma=1\) 时回到 Luke–Tam 意义下的 submonotonicity（适当缩放、\(L\ge1\)），也等价于一个平衡参数的 semimonotonicity 截面。但本文关键 \(\gamma<1\) 构造通常不是标准有限模 hypomonotone 算子。

“已有研究吗”的明确答案是有：单步非扩张/统一 Lipschitz 迭代的极限回缩、Lipschitz 单步与共同几何尾的 Hölder 极限，以及光滑解流形的渐近相位，都是相关传统入口。不能仅检索“submonotonicity + stability”，因为这里两个词都存在同名异义。

当前稿件需要的稳定性对象固定为
\[
T=J_{\mathcal G},\qquad \Pi_T(x)=\lim_{k\to\infty}T^kx,
\]
且欲在同一初值邻域上控制任意两点 \(\|\Pi_T(x)-\Pi_T(y)\|\)。完整 PPA 仍须另外有共同轨道区 \(W\) 上 \(J_{\lambda F}=J_{\mathcal G}\)。

## 2. 读稿范围与准确接口

已完整阅读当前修订稿 solution_selection_revised_v1/research_note.md（763 行），并阅读原 RLEB 包 sections/theorem_spine.tex 的 RL 定义、resolvent 等价式、A1–A4、一步估计与局部长度/点尾接口，以及 sections/related_work.tex 的线性端点识别和平方根接缝定向分离。

记 \(a=u-v,\ b=u^*-v^*,\ d=\|a+\lambda b\|\)。原稿 RL 为
\[
\|a-\lambda b\|\le Ld^\gamma,
\quad\text{等价于}\quad
\lambda\langle a,b\rangle\ge\frac{d^2-L^2d^{2\gamma}}4.
\tag{R}
\]
在有 coverage 的图块上，(R) 等价于反射映射 \(2T-I\) 的 all-pairs Hölder 估计。原 RLEB 的 EB 则是 \(d(u,S)\le\psi(d(0,F(u)))\)。两者是不同接口：一个控制输入对的单步传播，一个以残差控制到解集距离；EB 不是 \(\Pi_T\) 的两初值稳定性。

## 3. 术语—公式—检索词对照

| 名称 | 必须核对的定义 | 与本文关系 | 建议检索词 |
|---|---|---|---|
| 本文 Hölder RL | (R)，全部图点对，且以 \(\|a+\lambda b\|\) 限比较尺度 | 真实对象；\(\gamma<1\) 不宜替换成普通 hypomonotonicity | Hölder reflected resolvent; nonlinear generalized monotonicity; limit map regularity |
| Luke–Tam submonotonicity | \(\lambda\langle a,b\rangle\ge-\tau\|a+\lambda b\|^2,\ \tau\ge0\) | 同图块/同对范围下等价于 \(\gamma=1,\ L^2=1+4\tau\) | submonotone resolvent; almost firmly nonexpansive |
| \(h\)-hypomonotonicity | \(\langle a,b\rangle\ge-h\|a\|^2,\ h\ge0\) | \(F+hI\) 单调；\(\lambda h<1\) 给局部 resolvent Lipschitz，强于尖点接口 | hypomonotone; weakly monotone; semiconvex |
| \(\rho\)-comonotonicity | \(\langle a,b\rangle\ge\rho\|b\|^2\) | 是 \(F^{-1}\) 的 \(\rho\)-monotonicity；负 \(\rho\) 为 cohypomonotonicity | cohypomonotone; generalized averaged resolvents |
| \((\mu,\rho)\)-semimonotonicity | \(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\) | \(\gamma=1\) 为其平衡截面；不能据尖点分离整体排除任意参数版本 | semimonotone; preconditioned PPA; restricted monotonicity |
| weak monotonicity | 优化中常指 \(\langle a,b\rangle\ge-h\|a\|^2\)，但用法不统一 | 每篇须落回公式；不能仅据名称认作 RL | weakly monotone operator resolvent |
| weak Minty / star-cocoercivity | \(\langle u-s,u^*\rangle\ge\rho\|u^*\|^2\)，固定 \(s\in S\) | 解点锚定，不是任意两非解点比较 | weak Minty; star-cocoercivity |
| prox-regularity | 局部二次下支撑不等式，限制附近次梯度和函数值 | attentive localization 的次微分导出 hypomonotonicity；任意 \(F\) 未必为 \(\partial f\) | prox-regular; attentive localization |
| Spingarn–Daniilidis–Georgiev submonotonicity | 任意 \(\varepsilon>0\) 缩邻域后 \(\langle a,b\rangle\ge-\varepsilon\|a\|\) | 与 Luke–Tam 同名异义；对应 lower-\(C^1\)/近似凸 | approximate convexity; strictly submonotone; lower-C1 |

引文定位：Luke–Tam Definition 2、Propositions 3–4、Definition 3；Bauschke–Moursi–Wang Definition 2.3；Evens–Pas–Latafat–Patrinos Definition 4.1、Remark 4.2；Poliquin–Rockafellar Definition 1.1、Theorem 3.2；Daniilidis–Georgiev 式 (1)、Theorem 2。原始文献与链接见 §6。

### 平衡截面的准确常数

展开 (R) 的 \(\gamma=1\) 端点得到
\[
\langle a,b\rangle\ge
\frac{1-L^2}{2\lambda(1+L^2)}\|a\|^2+
\frac{\lambda(1-L^2)}{2(1+L^2)}\|b\|^2.
\]
所以 \(\mu=(1-L^2)/(2\lambda(1+L^2)),\ \rho=\lambda^2\mu\)。
\(L=1\) 是单调端点，\(L>1\) 对应正 violation 的 Luke–Tam submonotonicity。不要把 \(L<1\) 也称作正 violation 的精确同义词。

Otero–Iusem 2011 使用 \(\eta\in(0,1)\)：
\[
\langle a,b\rangle\ge-\frac{\eta}{2}(\|a\|^2+\|b\|^2).
\]
在 \(\lambda=1,L>1\) 时换算为
\[
\eta=\frac{L^2-1}{L^2+1}=\frac{2\tau}{1+2\tau}.
\]
“semimonotone”还须核作者与归一化，不能直接比常数。

## 4. 五种不同的“稳定性”

| 被扰动对象 | 数学映射 | 与本任务是否相同 |
|---|---|---|
| 初值，有限步 | \(x\mapsto T^kx\)，固定有限 \(k\) | 不同；Lipschitz 常数可能随 \(k\) 发散 |
| 初值，无穷步输出 | \(x\mapsto\Pi_T(x)\) | 本任务对象 |
| inclusion 右端/数据 | \(v\mapsto F^{-1}(v)\) 或 \(\theta\mapsto S(\theta)\) | 不同；metric regularity、Aubin property 常研究此项 |
| proximal 输入，单步 | \(x\mapsto J_{\lambda F}(x)\) | 中间接口，不等于极限稳定 |
| 固定解点锚定 | \(\|\Pi_T(x)-s\|\le C\|x-s\|^\gamma\) | calmness 弱于整个邻域任意 \(x,y\) 的 Hölder 性 |

Luke–Tam Assumption 1(d) 标题中的 “Stability” 指 \(I-T\) 的 metric subregularity，不是初值—极限稳定。另一陷阱是 “Fix \(T\) admits a Hölder retraction”：存在某个回缩，不代表这个回缩就是实际 \(\lim T^k\)。Wiśnicki Lemma 1 是实际迭代极限；其主 Theorem 2 通过辅助映射构造回缩，须分开引用。

## 5. 可直接接上本稿的旧机制

以下为既有机制与稿件接口的组合，不申报新定理。

### 5.1 全对 Lipschitz 单步 + 共同几何点尾

若比较轨道始终在同一区域，
\[
\|Tx-Ty\|\le K\|x-y\|,\qquad
\|T^kx-\Pi_T(x)\|\le M\sigma^k,\quad 0<\sigma<1,
\]
则
\[
\|\Pi_T(x)-\Pi_T(y)\|\le K^k\delta+2M\sigma^k.
\]
当 \(K>1\)，平衡两项得到
\[
\|\Pi_T(x)-\Pi_T(y)\|\le C\delta^\theta,\qquad
\theta=\frac{\log(1/\sigma)}{\log K+\log(1/\sigma)}>0.
\tag{H}
\]
这为 Wiśnicki 2014 Lemma 1 的机制；(H) 是本组用当前符号写出的直接推论，不冒称原文使用这些符号。若单步估计仅限距离 \(\le R\)，截断步前的候选界 \(K^j\delta\le K^k\delta=O(\delta^\theta)\) 可趋入 \(R\)，因此本地尺度可闭合。

现成图条件包括：

1. 共同图块有限 \(h\)-hypomonotonicity、\(\lambda h<1\) 和 coverage 给
   \[
   (1-\lambda h)\|Tx-Ty\|^2\le\langle Tx-Ty,x-y\rangle,
   \]
   从而 \(K\le(1-\lambda h)^{-1}\)。接原 RLEB 共同点尾便得 (H)。
2. 同工作域 \(\gamma=1\) 的 all-pairs RL 给 \(K\le(1+L)/2\)，也可接 (H)。

它们是有答案的旧机制，但可能过强：提升了整个单步映射，而不是只限制沿解集方向的放大。

### 5.2 非扩张／统一幂 Lipschitz

若 \(T\) 非扩张且轨道点收敛，则 \(\|T^kx-T^ky\|\le\|x-y\|\)，取极限即得 \(\Pi_T\) 非扩张，无须误差界来完成这步稳定性传递。一般若 \(\operatorname{Lip}(T^k)\le C\) 对所有 \(k\) 一致，则 \(\Pi_T\) 为 \(C\)-Lipschitz。这是直接动力学条件，但未必易于从算子图验证。

### 5.3 固定 hypomonotonicity 不是必要条件

新几何模型取 \(u_t=(t,0,t)\)、\(u_t^*=(-2\sqrt t,0,3t)\)，与零图点比较：
\[
\frac{\langle u_t,u_t^*\rangle}{\|u_t\|^2}
=-\frac1{\sqrt t}+\frac32\to-\infty.
\]
因此不存在固定有限 \(h\)。

但原二维接缝 \(T_0(z,r)=(z+\sqrt{|r|},|r|/4)\) 也无此有限模，极限却是
\[
\Pi_{T_0}(z,r)=(z+2\sqrt{|r|},0),
\]
在有界尺度具有 \(1/2\)-Hölder 两点稳定性。因此加有限 \(h\) 会排除本来稳定的真实 Hölder 例子。

新 cap 坐标的坏性是未饱和段 \(p\mapsto p+\sqrt{p_+}\) 重复放大微小切向差。§5.2 以沿轨道可求和的切向 Lipschitz 系数抑制它。寻找弱于全空间 hypomonotonicity 的切向／法向分离条件，定位合理；本组未提出超出 §5.2 的新定理。

## 6. 已核原始文献

1. **D. Russell Luke, Matthew K. Tam. _Generalized Monotonicity and the Proximal Point Algorithm_.** Mathematics of Operations Research, online 2025。[DOI 10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)。正式 HTML：Definition 2、式 (10)、Propositions 3–4、Definition 3；§3 明示同名重用。Theorem 2 为局部 PPA 收敛，不是 \(\Pi_T\) 两点正则性定理。

2. **Heinz H. Bauschke, Walaa M. Moursi, Xianfu Wang. _Generalized Monotone Operators and Their Averaged Resolvents_.** [DOI 10.1007/s10107-020-01500-6](https://doi.org/10.1007/s10107-020-01500-6)；[arXiv:1902.09827v1](https://arxiv.org/html/1902.09827v1)。Definition 2.3、Remark 2.4、Lemma 2.5 给 \(\rho\)-monotone/comonotone、正负参数与逆算子对应；Fact 2.1 给标准 resolvent 编码。

3. **Brecht Evens, Pieter Pas, Puya Latafat, Panagiotis Patrinos. _Convergence of the Preconditioned Proximal Point Method and Douglas–Rachford Splitting in the Absence of Monotonicity_.** Mathematical Programming 214 (2025), 247–301。[DOI 10.1007/s10107-024-02182-0](https://doi.org/10.1007/s10107-024-02182-0)；[arXiv:2305.03605v2](https://arxiv.org/html/2305.03605v2)。已核 Definition 4.1、Remark 4.2（编号按 v2）：单个图点条件与全图条件分开，weak Minty 为锚定解点特例。

4. **Rolando Gárciga Otero, Alfredo Iusem. _Regularity Results for Semimonotone Operators_.** Computational & Applied Mathematics 30(1) (2011), 5–17。[DOI 10.1590/S1807-03022011000100002](https://doi.org/10.1590/S1807-03022011000100002)；[原刊 PDF](https://www.scielo.br/j/cam/a/TDWFt7WPXgSTwXPnCt8rYdy/?format=pdf&lang=en)。已核 Definition 2、Theorem 3、Remark 3。论文的 \((F+\lambda I)^{-1}\) 与本稿 \((I+\lambda F)^{-1}\) 必须缩放后比较。

5. **R. A. Poliquin, R. Tyrrell Rockafellar. _Prox-Regular Functions in Variational Analysis_.** Transactions of the AMS 348(5) (1996), 1805–1838。[DOI 10.1090/S0002-9947-96-01544-9](https://doi.org/10.1090/S0002-9947-96-01544-9)；[作者全文](https://sites.math.washington.edu/~rtr/papers/rtr157-ProxRegular.pdf)。已读 Definition 1.1、Theorem 3.2、Theorem 4.4；attentive localization 和局部 proximal 正则性有实质假设，不能应用于未证为次微分的任意 \(F\)。

6. **Aris Daniilidis, Pando Georgiev. _Approximate Convexity and Submonotonicity_.** Journal of Mathematical Analysis and Applications 291 (2004), 292–301。[DOI 10.1016/j.jmaa.2003.11.004](https://doi.org/10.1016/j.jmaa.2003.11.004)；[作者全文](https://www.arisdaniilidis.at/DG_ac.pdf)。已核式 (1)、Theorem 2、Definition 7；其 \(-\varepsilon\|a\|\) 是一阶小模，非上述两种二次不等式。

7. **Andrzej Wiśnicki. _Hölder Continuous Retractions and Amenable Semigroups of Uniformly Lipschitzian Mappings in Hilbert Spaces_.** Topological Methods in Nonlinear Analysis 43 (2014), 89–96。[DOI 10.12775/TMNA.2014.006](https://doi.org/10.12775/TMNA.2014.006)；[arXiv:1204.6464v2](https://arxiv.org/pdf/1204.6464v2)。已完整读 Lemma 1 及主 Theorem 2 的回缩构造；前者直接研究实际迭代极限，是最便于移植的入口。

## 7. 下一轮直接相关的六个理论入口

1. **非扩张/averaged resolvent 的真实 Picard 极限。** Lipschitz 基准已有；核 all-pairs 与仅相对解集条件。
2. **Luke–Tam / Otero–Iusem 的单步 Lipschitz 窗口 + Wiśnicki Lemma 1。** 直接恢复正 Hölder 指数，应作为强条件基准，不重新包装为创新。
3. **Prox-regularity／hypomonotonicity。** 图几何证单步 Lipschitz；检查 attentive localization、参数窗口与完整纤维。
4. **Uniformly Lipschitzian iterates / product bounds / discrete Gronwall。** 允许单步扩张而总放大有界，更贴近 §5.2。
5. **Smooth limit retractions / Gauss–Newton / asymptotic phase。** Beyn 1993 [DOI 10.1080/01630569308816536](https://doi.org/10.1080/01630569308816536) 是稿件已列直接对象先例；本组未重审全部定理，交动力系统组核适用假设。
6. **Stable foliations / normal domination / bunching / partial smoothness。** 可能保留法向 Hölder 接缝、只补切向控制；须区分存在稳定叶与算法实际 \(\Pi_T\)。

## 8. 仍不确定的术语与范围

- 中文“次单调性”不唯一，建议持续用 “Hölder RL” 和 “Luke–Tam submonotonicity 端点”双标签。
- Spingarn 1981 _Submonotone Subdifferentials of Lipschitz Functions_ 原定理页本组未取得，不称已核原页；已通过 Daniilidis–Georgiev 的原论文式 (1) 确认命名区别。[原刊记录](https://www.jstor.org/stable/1998411)。
- Spingarn 1982 _Submonotone Mappings and the Proximal Point Algorithm_，[DOI 10.1080/01630568208816109](https://doi.org/10.1080/01630568208816109)，仅确认入口，全文被拒，不能据题名判为两初值极限先例。
- “弱且自然”无脱离目标正则阶和几何结构的单一最小条件。全步 Lipschitz 是已有充分条件；用户更值得比较的是保留 \(\gamma<1\) 法向几何，只补可验证切向条件。
- 本报告不是优先权终判；不把未发现结果当作首创，也不把一步或数据稳定文献直接算作极限选择先例。
