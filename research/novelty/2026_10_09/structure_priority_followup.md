# C03/C04 精确先行追踪与平方距离边界构造

日期：2026-10-09 UTC。基线：`94cbbbd9bacb61787eeee583e0282b890455849a`。本轮先读 `RESEARCH_PROTOCOL.md`、`global_shadow.md`、`finite_fiber_classification.md`、`holder_extension.md`、既有 `structure_prior_art.md`，再按同一全图、全尺度、固定参数合同继续攻击。未改 CLAIMS、graph、RESEARCH_STATE 或任何旧证明状态。父任务随后授权把新独立证明写入 [C222 候选正文](../../canonical/sharp_holder_lipschitz_realization.md)，全局身份登记由父任务负责。

## 本轮判断

1. **C03 的全部显示存在性与锐常数证明可由经典 Hilbert 扩张、两次 Banach 反演、Cayley 恒等式及单纯形/Jung 几何直接重建。** 在本轮实际核读的旧源中未定位到完全相同的已发表双原底点定理；这不提供“经典不能推出”的隔离，也不认证全球优先。
2. **C04 的精确最小 Hölder 预算达到性也有一个短的初等构造。** Goebel 的旧线性距离混合只直接给超额预算；把混合改成平方距离，并与 Hilbert 凸包余量配对，即可精确达到闭边界。这是本轮推导，不能谎称 Goebel 2016 已陈述该边界定理。
3. **正式附件的单值全域 Lipschitz 实现加强正确。** 本轮独立核完其 corollary 的余下证明，并以平方距离构造给出任意实 Hilbert 上、原 compact K 范围内的自足规范证明。正确参照为 `(Id−P_Q)/λ`。

因此适宜保留的精确比较问题，是旧公开版本是否已经包含同样的 sharp paired formulation 或 exact-budget realization；不是扩张、零集存在或可逆代理本身是否全新。

## 1. C03：精确组合的经典可导出性

固定 `λ,L>0`、`0<γ<1`、`R=L^(1/(1−γ))`。Cayley 坐标把整个图的 RL 条件等价成部分 Hölder 映射 `C:D→H`。对 `σ∈(0,1)` 记
\[
M_\sigma=\sup_{t\ge0}(L^2t^{2\gamma}-\sigma^2t^2)
=(1-\gamma)\gamma^{\gamma/(1-\gamma)}R^2\sigma^{-2\gamma/(1-\gamma)}.
\]
提升点 `p` 为 `(p,τe_p)`，其中 `τ²=Mσ/(2σ²)`。不同点的正交附加平方距离是 `2τ²`，故提升后的数据为 `σ`-Lipschitz。一次普通 Kirszbraun 扩张在零切片上的限制 `N` 满足
\[
\|C(p)-N(q)\|^2\le\sigma^2\|p-q\|^2+M_\sigma/2
\quad(p\in D,q\in H).
\]
这正是 C03 的 cross 界，没有使用现代带参照约束的额外机制。

令 `X=(Id+N)/2`、`Y=(Id−N)/(2λ)`。两次 Banach 反演给 `A=Y∘X⁻¹`，其 Lipschitz 和强单调常数就是规范页所列比值。对一个原图点，分别选择 `X(q)=x`、`Y(q)=v`，两种情形都使 cross 中两个差的范数等于对应原坐标误差，因此同一 `A` 满足
\[
\max\{\lambda\|v-A(x)\|,\|x-A^{-1}(v)\|\}
\le\sqrt{M_\sigma/[2(1-\sigma^2)]}.
\]
标量优化 `σ²=γ` 给 `R/√2`。下界由边长 R 的 n 维正则单纯形半径 `R√(n/[2(n+1)])` 和投影 Cayley 完整纤维给出。此处逐步都是经典定理的显式应用；新颖性若要保留，只能是精确量词、配对表述和预算组合的发表优先问题。

新增的 Jung 先行核验为 Huuskonen–Väisälä (2002) Theorem 1.11，印刷 p.34，以及 Proposition 2.12，p.36 起：其 nearisometry 逼近常数正好等于 Jung 常数，有限维 `√(2n/(n+1))`、无限维 `√2`，按直径 2 归一化。该文使用双侧加性距离误差并逼近仿射等距；不覆盖当前平方单侧 defect 与 C03 双向纤维。它直接限制“单纯形极限产生锐 Hilbert 常数”本身的新颖性。

## 2. C04：一个平方距离混合达到闭预算边界

完整全参数证明见 [SHLR-MARGIN–SHLR-RESIDUAL](../../canonical/sharp_holder_lipschitz_realization.md#shlr-margin)。核心只需以下估计。

对非空紧 `K⊂H`，令 `D=diamK>0`、`Q=clconvK`、`d(y)=dist(y,K)`，固定 `k₀∈K`。Hilbert 方差恒等式给
\[
\|y-z\|^2+d(y)^2\le D^2\qquad(y,z\in Q).
\]
取 `0<α≤min{(1−γ)/6,η/3}`，定义
\[
E(y)=-\alpha\frac{d(y)^2}{D^2}(y-k_0),\qquad S(y)=y+E(y).
\]
它是向 k₀ 的凸混合，完整固定集恰为 K。`d` 的非扩张性给 `LipE≤3α≤η`，而凸包余量给
\[
\|E(y)-E(z)\|\le \frac{2\alpha}{D}(D^2-h^2),\qquad h=\|y-z\|.
\]
于是
\[
\|S(y)-S(z)\|
\le h+\alpha\min\{3h,2(D^2-h^2)/D\}
\le D^{1-\gamma}h^\gamma,
\]
最后一步来自
\[
\min\{3t,2(1-t^2)\}\le6t(1-t),\qquad
t^\gamma-t\ge(1-\gamma)t(1-t),\quad0\le t\le1.
\]
因此 `R=S∘P_Q` 是全域 Lipschitz 映射，完整固定集 K，值域包含于 Q，最小全局 γ-Hölder 常数恰为 `D^(1−γ)`。固定 K 的点对本身迫使该下界。`D=0` 用常值映射即可。

这一构造直接到达边界，没有让 `η→0`，也不需要局部 bump、可数子覆盖或凸组合极限。因而“边界只能由特殊的新扩张工具处理”不成立。但平方距离替换及对应预算估计是本轮独立推导：已读 Goebel 原文的因子为 d(y) 而不是 d(y)²。

独立子代理 `square_distance_attack` 对上述公式及正式 corollary 检查未发现数学错误；提醒值域应写 `ranR⊆Q`，不能写等于 Q；`G` 不必为梯度映射，其满射性由显式收缩迭代证明。正文已按此写定。该初等证明事实上不需要紧性以外的全部特征，但本轮 C222 保留 compact K 的固定身份，没有扩展集合范围或无限维必要性。

## 3. 正式 TeX corollary 的独立复核

附件 `01-Holder_RL_Formal_Manuscript.tex` 与仓库 S23 原 TeX 的 SHA-256 相同：
`1c7c870d1468a565792aa44b98c95b60031fd7e586c46d1f175f824dd2e92deb`。
本次准确核读 lines **875–944**，`cor:lipschitz_realization` 陈述与 proof。

给 `R=P_Q+E∘P_Q`、`LipE≤η<1`，置 `G=(Id+R)/2`。它强单调模至少 `(1−η)/2`，Lipschitz 模至多 `(2+η)/2`。对任意目标 u，`a↦a−t(G(a)−u)` 在 `0<t<2c/M²` 下是收缩，故任意实 Hilbert 上 G 双射、`LipG⁻¹≤2/(1−η)`。恢复
\[
F(u)=\frac{G^{-1}(u)-u}{\lambda}.
\]
投影残差非扩张给
\[
\operatorname{Lip}F\le\frac{1+\eta}{\lambda(1-\eta)}.
\]
`u+λF(u)=a`、`u−λF(u)=R(a)` 证明 Cayley 全域与 fixed-parameter graph-maximal，`F(u)=0⇔a=R(a)` 给完整零集 K。`G₀=(Id+P_Q)/2` 有逆 `G₀⁻¹(u)=2u−P_Qu`。强单调反演估计给
\[
\sup_u\left\|F(u)-\frac{u-P_Qu}{\lambda}\right\|
\le\frac{\sup_Q\|E\|}{\lambda}
\le\frac{\eta D}{\lambda}.
\]
正文中的平方距离选择还给较小附带界 `αD/λ`，不声称其最优。此加强的数学差别仍是同一精确 Hölder 预算，包括 D=R；单值 Lipschitz 与投影残差任意小扰动的宽泛存在性也可由 Goebel 超额构造及同一反演得到。

## 4. 本轮实际阅读、版本和未读义务

表中 “read” 是有限定位阅读，不意味着整篇无遗漏审计。外部源陈述与本轮推导分开。

| 一手来源 / 版本 | 本轮准确实读 | 比较结论 / URL / web ref |
|---|---|---|
| Goebel, *Remarks on fixed point sets*, Stud. Univ. Babeș-Bolyai Math.61(4),2016,429–434，期刊 PDF | 本人 pp.430–432 的 Claim1、证明及 pp.434 references | 原因子 d¹，只显式给 `(1+ε)`-Lipschitz fixed-set realization。本文 d² 精确预算不能归给旧定理。[PDF](https://www.cs.ubbcluj.ro/journal/studia-mathematica/journal/article/view/159/pdf)，`turn36view0`, `turn101view0` |
| Barroso, arXiv2207.03057 **v3，2022-12-19**，22页 | 本人 intro pp.2–3；Proposition4.1(4) p.9、其构造 p.10；下载文本同核 | 已有保持给定非扩张映射 fixed set 的 `ε+diam(K)^(1−α)` Hölder 转换。前提是既有非扩张映射、且预算仍有 ε；不直接实现任意非凸 compactK 的精确预算。[v3](https://arxiv.org/pdf/2207.03057v3)，可解析 [current PDF（正文标v3）](https://arxiv.org/pdf/2207.03057)，`turn97view0`, `turn102view1`。发表版 JMAA528(2023)127521，DOI10.1016/j.jmaa.2023.127521 本轮只核 metadata，不偷换其编号 |
| Levy–Rice, CMUC24(2),1983,251–265，数字化发表版 | 子代理 printed pp.258–261：Lemma4、Theorem3、Corollary2、Remarks；既有报告已有本人上一轮阅读 | 网与同常数扩张给 uniform Lipschitz approximation，未在这些定位找到 M/2 cross 或 paired theorem。[PDF](https://dml.cz/bitstream/handle/10338.dmlcz/106224/CommentatMathUnivCarol_024-1983-2_6.pdf)，子代理 `turn23view0`, `turn27view0` |
| Huuskonen–Väisälä, *Hyers–Ulam constants of Hilbert spaces*, Studia Math.153(1),2002,31–40，DOI10.4064/sm153-1-3 | 子代理 pp.31–36；本人重新 open 并 find Definition/Thm1.11/Prop2.12 | Jung 等距稳定常数；hypotheses 与 C03 不同，不作 exact prior match。[publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/89477)，本人 `turn102view0`,`turn104view0–2` |
| Vestfrid, *Hyers–Ulam stability of isometries and non-expansive maps between spaces of continuous functions*, Proc.AMS145(6),2017,2481–2494；**作者上传稿，稿内占位分页** | 子代理 manuscript pp.1–8，Prop2.1 与 Lemma2.5 | ε/2 的 `ℓ∞` additive-norm nonexpansive approximation 及 Hilbert target 的无有限误差 nonexpansive近似反例；不是平方 defect cross。[author upload](https://www.researchgate.net/publication/305485135_Hyers-Ulam_stability_of_isometries_and_non-expansive_maps_between_spaces_of_continuous_functions)，子代理 `turn83view0`,`turn84view3`。本人未重复全文核读 |

仍未获得正文并不能作为否定匹配证据：

- **Grünbaum–Zarantonello1968**，Michigan Math.J.15,65–74，正确 DOI **10.1307/mmj/1028999906**。[ProjectEuclid PDF](https://projecteuclid.org/journals/michigan-mathematical-journal/volume-15/issue-1/On-the-extension-of-uniformly-continuous-mappings/10.1307/mmj/1028999906.pdf) 本轮子代理收到 Incapsula challenge。未读原文；只能报告 Levy–Rice 对其 uniform-extension/subadditive-modulus 结果的引用。
- **Minty1970**，Bull.AMS76,334–339，DOI **10.1090/S0002-9904-1970-12466-1**。[AMS PDF](https://www.ams.org/journals/bull/1970-76-02/S0002-9904-1970-12466-1/S0002-9904-1970-12466-1.pdf) 返回403；ProjectEuclid identifier1183531485也未取得正文。
- **Goebel–Prus2012**，*Shapes and sizes of the fixed point sets*，NACA2011 proceedings I,75–97；**Bruck–Goebel1992**，*Bizzare fixed point sets*,67–70；**Robbins1967**。本轮未取得一手正文，具体预算性质仍待逐定理比较。元数据或 Goebel2016 reference list 不关闭这些义务。

Barroso v3 下载文件只保留 scratch：`/workspace/scratch/1113ab853b9a/priority_sources/barroso2207v3.pdf`，SHA-256 `c4a86aa298768d4c3f62b5f18e09e4d3221cf3b6d39373ee47174d4abe579419`。PDF 和 `pdftotext -layout` 文本未加入仓库。

## 5. 可复算结果和接收边界

运行：
```
python3 research/code/gppa_novelty/structure_priority_check.py
```
Python standard library，seed222031004，binary64。精确 Fraction 抽查 SHLR10；浮点抽查 SHLR11、幂预算；非凸四顶点 K 的全域平方距离实现、Cayley 重构、G 收缩反演、原 F Lip 界和 projection-residual 误差。

结果：**PASS**，102710 个 scalar checks、55945 个 square/reconstruction checks，167个点，`γ=.5,η=.1,λ=1.7,α=.03333333333333333`。最大观测统一误差 `.0025162268727155434`，本构造证明界 `.0277296776935901`。代码 SHA-256 `1b78c0efa443434bd566782851bdaecf85e7aceadec776fcb6881a8299649ccd`。这些有限检查只确认计算与实现，承重结论由规范页全参数证明承担。

没有全球新颖认证。下一精确义务是取得上述旧正文并比较 **同一预算达到性**，以及 C03 的 **同一个代理、原输入/原输出配对、维数统一锐因子** 的公开陈述；不能把未检出、访问失败或 “未单列该 corollary” 写成无先行证明。

## 6. 按父任务追加的 C221 跨模块独立接收

实际阅读：[C221 candidate 正文](../../canonical/gppa_tail_lyapunov_bridge.md) TL1–TL7；[NGK 规范证明](../../comparisons/2026_08_gppa_nfb/gppa_nonlinear_kernel_theorem.md) NGK1–24；ABS 2010-12-15 原 PDF 的 H1–H3（印刷 p.8）、Theorem2.9（p.12），以及 C218 的 true-residual/input-step 接口。没有更改 C221 的数学身份或状态。

**受检范围未发现 fatal 问题。** 各承重门如下。

- **真实残差评价域保持。** 核步骤的选中值只用来打开窗口：`r_A(y)≤s/λ≤B(d)/λ≤B(R)/λ≤tbar`。真正 EB 仍评价完整核 union `A`，不是删支或选中残差，且不假设 inf 取得。非单射 v 下没有把 `r_A(vx)≤r_F(x)` 偷换成等号。
- **标量势能不循环定义。** `L(t)=Σb(τ^j(t))` 只依赖初始半径 r 的有限标量级数；在 `[0,r]` 由单调 domination 获 uniform convergence。`K` 中的预算 `||z−z0||+L(d(z,Z))≤L(r)` 先证位于 U，再调用 coverage 与一步 descent 保持 K。输出先由距离上界进入 Φ 的定义域，再证其在 U，不要求预先留域。
- **能量到 tail 的转换成立。** `B(t)²≤Cω(t)` 是平方恒等式；`R≤M`、`t<R`、`Cω(t)≤qV(t)<V(M)` 使逆 cap 不活跃。于是 scalar `τ≤τE` 给 `V(τt)≤qV(t)`，迭代得 `B(τ^j r)≤q^((j+1)/2)√V(r)`。这直接证明标量级数收敛，没有从实际轨道有限长倒推上界级数。t=0 由两边为零处理；如需闭端点 R 的 strict contraction，由连续性把能量不等式延至 R。
- **完整域 Caristi 门明确。** Q 可以不闭；`clK` 的完备来自 ambient H。只有 all-pairs NGK12 给唯一连续核 T 及一致模，足以独立于逼近序列地扩张到 `clK`。此扩张只是外部旧定理接口，不制造 Q 外 GPPA coverage。只有零锚条件时没有授予该单值扩张。
- **signed SF/ABS 门正确。** 完整两支解出 `T(ξ,r)=(ξ+A₀|r|^γ,|r|^ν)`；负输入使用原负支，不是删支。H1 要 `β≤2γ`，H2 要 `ν(β−1)≥γ`，共同可行门恰为 `γ≥ν/(2ν−1)`。边界等号通过；β介于1与2，power objective为 C¹。H3只用 normal几何界和 tangential有界给子列，未借目标收敛。`φ(s)=s^(1/β)` 的 KL乘积恒等于1；ABS Theorem2.9的源门与此对应。

ABS 原文：[primary PDF](https://optimization-online.org/wp-content/uploads/2010/12/2864.pdf)，本人 `turn111view0`,`turn112view1`；原 H3 要 function-attentive cluster，Theorem2.9由该 cluster 的 KL性质推出收敛和有限长度。本轮仅为 C221 所显示接口接收，不把一般 scalar-tail势自动升级为 KL/ABS objective，也不把 SF sector 扩成每个 C209 实例。
