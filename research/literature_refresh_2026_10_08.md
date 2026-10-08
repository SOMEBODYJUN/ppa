# 2026-10-08 定向文献刷新：Hölder–RL、RLEB 与近端方法

<a id="lr-scope"></a>
## 范围与结论层级

核验截止 **2026-10-08 UTC**。主检索窗口为 2026-08-01 至 2026-10-08，另补查一篇 7 月、与影子构造直接相邻的论文。检索围绕 nonmonotone / generalized / warped / preconditioned proximal point、semimonotonicity / weak Minty、Hölder error bound / metric subregularity、Kirszbraun / Lipschitz shadow / monotone fibres，以及 Luke–Tam 后续与完整算子空间比较。以 arXiv 原稿、研究机构页面和出版社为事实来源。

项目基线为 Git `e9f918c1929831496e4b9caae66a2e7eb597054d`；比较对象取现行规范 C02-v2/C09、C03、C04、C191–C194 及总体规模开放问题，而非历史摘要。此前已经接入的 OpenAI 目录 332 / C181–C184 不重复算作本轮新发现。

**当前判断 / interpretation：** 新文献直接增加了收敛稿和结构稿的比较义务，也提供了复合误差界的候选接口。已核内容尚未显示覆盖我们的完整主定理；这不是全球无先例或创新性已经认证的结论。总体规模问题仍缺同一自然母空间、同域成员谓词及有鉴别力的不变量，本轮没有找到可直接关闭这些门的结果。

本页把 **paper fact**、**本库直接推导**、**interpretation / 待核义务** 分开。未审全篇证明的论文只用于定位和确定适用条件，不能当作已验收的承重工具。

<a id="lr-index"></a>
## 新文献与直接影响

| 标识、作者与一手链接 | 时间与版本 | 本次实读范围 | 对项目的影响 |
| --- | --- | --- | --- |
| GPPA：Le / Mordukhovich / Théra，[Convergence and Stability Analysis of a Generalized Proximal Point Algorithm and Its Inexact Version](https://arxiv.org/abs/2608.01584) | 2026-08-03 提交，v1；PDF 日期 8/04 | 14 页原稿，正文 pp.1–12；重点 Definition 3、Theorem 2 pp.7–8、Theorem 4 pp.9–11；Example 1 p.4 另目读核矩阵 | 收敛路线的优先比较对象；核坐标收敛与原变量点收敛必须分开 |
| NFB：Pesquet / Roldán，[Nonlinear Forward-Backward Algorithm for Solving Non-monotone+Lipschitz Inclusions with Applications to Adjoint Mismatch Problems](https://arxiv.org/abs/2608.22687)；[机构页面](https://www.ci2ma.udec.cl/publicaciones/prepublicaciones/prepublicacion.php?id=633) | 2026-08-24 提交，v1 | 35 页 arXiv 原稿的问题设置、半单调定义 p.4、Assumption 3.1 p.6、Algorithm 3.7 p.8、Theorem 3.10 pp.12–13；未审全部应用及证明 | 半单调 / warped resolvent 比较；伴随算子近似造成非单调性的应用方向 |
| Spingarn：Evens / Latafat / Patrinos，[Spingarn’s method and progressive decoupling beyond elicitable monotonicity](https://link.springer.com/article/10.1007/s10589-026-00812-1)；[预印本](https://arxiv.org/abs/2504.00836) | 刊本 2026-08-27；预印本 v1 首发 **2025-04-01** | 刊本日期与摘要；27 页预印本 v1 的 Definition 3.1、Assumption I pp.6–7、Lemma 3.7、Theorem 3.8 pp.10–12 | 补入局部非单调预条件 PPA 比较；不是最近两个月才出现的理论，刊本与 v1 逐条差异未穷尽 |
| KKT：Jiani Li / Qingna Li，[Primal-Dual Error Bounds and KKT Metric Subregularity in Convex Composite Optimization](https://arxiv.org/abs/2610.08587) | 2026-10-06 提交，v1 | 53 页原稿 pp.1–5、Corollaries 3.17–3.20 pp.16–17；未审完整附录 | 候选真 EB / 残差转移工具；不自动解决一般非凸、秩亏的复合支线 |
| 保距扩张：Ciosmak，[Kirszbraun extensions preserving uniform distance in Hilbert spaces](https://arxiv.org/abs/2607.17672) | 2026-07-20 提交，v1，**窗口外补查** | 17 页原稿 Theorem 1.1 pp.2–3 及核心证明 pp.3–8；后续全部应用未验收 | C03 影子主线的优先先行性比较；不能由一般 Hölder 参照自动调用 |
| 单调纤维：Ciosmak，[Measure contraction property on isometric leaves and monotone fibres](https://arxiv.org/abs/2609.21510) | 2026-09-18 提交，v1；稿内日期 9/08 | 38 页原稿 pp.1–5、Theorems A–C 与路线；未审完整证明 | 测度分解 / 纤维几何候选旁支；普通极大单调与本库固定参数图极大不同 |
| HVP-EB：Liu / Wang / Shao / Li，[Convergence rate analysis of nonconvex nonmonotone descent methods under the Hölderian value proximity error bound condition](https://www.sciencedirect.com/science/article/pii/S0167637726000854) | *Operations Research Letters* 2026 年 9 月期，DOI 10.1016/j.orl.2026.107488；首次在线日期未确认 | 出版社摘要和公开预览的 H1/H2；未取得完整定理与证明 | 多步下降 / EB 速率的候选比较；“目标值非单调下降”不等于“算子非单调” |

<a id="lr-gppa"></a>
## GPPA：优先比较，先固定收敛的变量

**Paper fact。** GPPA 用核映射 \(v:H\to H\) 与步长 \(\eta>0\)，更新为
\[
v(x_k)-v(x_{k+1})\in\eta F(x_{k+1}),
\qquad J^v_{\eta F}=(\eta F+v)^{-1}\circ v.
\]
这里将原稿步长字母改为 \(\eta\)，不与本库 Hölder 指数 \(\gamma\) 混用。Theorem 2 还要求零集非空、\(\operatorname{ran}v\subseteq\operatorname{ran}(\eta F+v)\)，以及全图点对的条件
\[
\langle f-g,v(x)-v(y)\rangle\ge\epsilon\|v(x)-v(y)\|^2,
\quad f\in F(x),\ g\in F(y),\quad\epsilon>0.
\]
它控制核坐标到零锚的平方距离，因子为 \((1+2\eta\epsilon)^{-1}\)；加 \(F^{-1}\) 在 0 的 R-Lipschitz 性后，给到原零集距离的线性下降。Theorem 4 针对 \(F+\epsilon v\) 的正则化问题，要求其零集非空、核 Lipschitz 和逆关系 R-continuity；误差预算取 \(\delta=\epsilon^2\)，得到到原零集的渐近邻域界及 \(\epsilon\downarrow0\) 时界趋零，不能读成固定持续误差下精确收敛。

<a id="lr-gppa-physical"></a>
### C197-v1 / LR-GPPA-PHYSICAL：原变量不必点收敛

**完整对象与本库直接证明。** 取 \(H=\mathbb R^2\)、\(F(x_1,x_2)=v(x_1,x_2)=(x_1,0)\)、\(\eta=\epsilon=1\)。零集为 \(S=\{0\}\times\mathbb R\)。任意点对的上式两边均为 \((x_1-y_1)^2\)；\(\operatorname{ran}v=\operatorname{ran}(F+v)=\mathbb R\times\{0\}\)。若输出 \(w=(a,0)\)，则 \(F^{-1}(w)=\{a\}\times\mathbb R\)，每点到 S 的距离为 \(|a|=\|w\|\)；其他输出的逆纤维为空。因此逆关系在 0 全局满足 R-Lipschitz 常数 1。

每个整数 \(k\ge0\) 的
\[
x_k=(2^{-k},(-1)^k)
\]
都满足同一完整 GPPA 更新，因为第一坐标差恰为 \(2^{-k-1}\)，第二坐标不受核约束。于是 \(d(x_k,S)=2^{-k}\)、\(v(x_k)\to0\)，但原轨道有两个不同聚点 \((0,1),(0,-1)\)，且每步范数至少 2，所以不点收敛、长度无限。

**边界。** 这是对“仅凭该文 Theorem 2 前提便得到原变量点收敛 / 有限长度”的反例，**不是**对其 Theorem 2 已述结论的反驳。它也不证明 GPPA 类与 RLEB 类的总体包含或不可比。其机制与本库 [C194 的非单射压缩边界](canonical/secondary_problem_interfaces.md#sp-preconditioned) 一致。

**校勘记录 / 独立有限反证。** v1 Example 1 p.4 所印矩阵
\(B=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}\)、\(v(x)=(x_1,0,0)\)，和
\(F(x)=(\operatorname{Sign}x_1,\operatorname{Sign}x_3,\operatorname{Sign}x_2)+Bx\)，不能产生其声称的单调 pair：取 \(x=(2,1,1),y=(1,2,1)\)，所有 Sign 为 1，得 \(F(x)=(8,20,32)\)、\(F(y)=(9,21,33)\)，内积为 \(-1\)。已目读原 PDF 排除文本抽取的矩阵行列误读。此错误只定位该例，不能据此否定后续抽象定理；未来修订版须重核。

<a id="lr-splitting"></a>
## NFB / Spingarn：扩大比较对象与保留同对象门

**Paper fact。** NFB 的 Assumption 3.1 明确要求 \((M+A)^{-1}\) 单值且满定义域、\(A+C\) 图的 weak–strong 顺序闭性、正定度量中 C 的 cocoercivity，以及 A 相对解锚的 comonotonicity。核与度量的差还须小 Lipschitz 常数。Theorem 3.10 在额外正下降系数下给弱收敛；再加正的半单调参数，给唯一解及 R-linear 点收敛。不能从摘要的“without monotonicity”删除这些条件。

Spingarn 的 v1 Theorem 3.8 用局部图集 U、非空凸 \(S_*\subseteq\operatorname{zer}T\)、固定矩阵 V 的 oblique weak Minty 锚界、T 的外半连续性、正定可交换预条件 / 松弛矩阵和局部输入 coverage。它给留域、残差趋零、最佳迭代残差速率及聚点为零；\(S_*=W\cap\operatorname{zer}T\) 时给点收敛。其局部算法实际只选 U 内的图点；原完整近端的全部选择不能自动继承。

**Interpretation / 已有内部反证的准确映射。** 本库 [C193](canonical/support_normal_natural_class.md#sn-failures) 已证明：非退化 C191 原图或 C192 原图在任意零锚附近，不满足任何固定有限矩阵的残差二次锚下界。故在有限维、**同一原算子、同一零锚、完整图邻域**的直接代入下，Spingarn 的固定 V 锚条件不能由我们的自然类证书推出。对 NFB 的 \(C=0,A=F\) 直接特例，其 \(\rho S^{-1}\) 锚界同样被排除（符号可并入 C193 的任意矩阵）。这不是对所有核、所有分裂、局部选支或升维表示的排除；那些表示须重新核同一原关系、零集、完整纤维、残差及算法轨道身份。

**具体义务。** 收敛稿不能只与 Luke–Tam 比较，至少还要与 adaptive / warped GPPA、semimonotone NFB、oblique weak Minty PPPA 作逐定理对照。优先核假设互推、变量、原残差、全部选择、点 / 集合收敛、长度及留域。伴随近似提供应用候选；本轮没有把具体 inverse problem 自动认证为 RLEB 模型。

<a id="lr-kkt"></a>
## 10/06 KKT 预印本：复合误差界的候选工具

**Paper fact。** 原稿的对象是有限维凸复合问题 \(\min f_1(z)+f_2(Az+b)\)：\(f_1\) 处处有限、凸且 Fréchet 可微，\(f_2\) proper、闭、凸，并保留原始 / 对偶可解及强对偶的设置。Corollary 3.18 在 A 满行秩、\(\nabla f_1\) 局部 Lipschitz 下，联系原始局部 EB 与 reduced KKT metric subregularity；3.19 在 \(f_1\) 强凸下联系对偶 EB 与 KKT 次正则；3.20 合并相应条件。原始 prox-gradient 残差、对偶次梯度残差和 KKT 残差各有准确身份。

**Interpretation / 导入门。** 可帮助本库 [复合模块](canonical/composite_subregularity.md) 认证应用中的实际 EB，尤其提醒把残差和目标解集逐项映射。满行秩推论不能填补一般秩亏门；文中的特殊秩亏应用也不能未经核验推广为任意非凸秩亏定理。先审拟调用的完整证明、精确链式规则及局部残差比较，再进入承重链。本轮不升级 C35 或其他复合 Claim。

<a id="lr-kirszbraun"></a>
## 7 月保距扩张：影子主线的优先比较

**Paper fact。** Ciosmak v1 Theorem 1.1 对实 Hilbert 子集 X 和参照映射 \(v:X\to Y\)，刻画以下性质：任意子集上的 1-Lipschitz 数据，只要在半径 \(\rho\) 内贴近 v，就能以同一 Lipschitz 常数扩张到 X，并保持同一偏差预算。充要门是目标维数允许的有限重心不等式；特别是其 \(k=1\) 门已经要求 v 为 1-Lipschitz。2026 稿补出先前一般设置下的必要性；相关 2024 稿 [Continuity of extensions of Lipschitz maps and of monotone maps](https://arxiv.org/abs/2402.14699) 仍须纳入正式先行性核验，本轮只核其元数据和摘要。

<a id="lr-holder-reference"></a>
### C198-v1 / LR-HOLDER-REFERENCE：Hölder 参照不自动满足该门

**完整对象与本库直接证明。** 对全部 \(p\in\mathbb R^2\)，令
\[
h(t)=\min\{1,\max\{0,t\}\},\qquad C(p)=(\sqrt{h(p_1)},0).
\]
h 为 1-Lipschitz，且非负 a,b 满足 \(|\sqrt a-\sqrt b|^2\le|a-b|\)，所以对全部 p,q 有
\[
\|C(p)-C(q)\|^2\le|p_1-q_1|\le\|p-q\|.
\]
因此 C 有全局 \(\gamma=1/2,L=1\) Hölder 证书。令完整图
\[
\operatorname{gph}F=\{((p+C(p))/2,(p-C(p))/2):p\in\mathbb R^2\},
\]
则其 Minty 输入恰为 p，故是固定 \(\lambda=1\) 的全图、全尺度 Hölder–RL 对象。取 \(p=(1/100,0),q=0\)，输入距为 \(1/100\)，C 的输出距为 \(1/10\)，违反上述 \(k=1\) 门。

**边界。** 这只否定“把一般 Hölder–RL 的 C 直接当作该文参照 v，便自动获得其扩张性质”。它不否定存在本库 C03 的 Lipschitz 影子，也不排除选择另一参照或增加结构条件后导入该文。

**Interpretation / 待核对照。** [C03](canonical/global_shadow.md#gsh-object) 从 Hölder 数据构造同一个全域收缩 N，承重的是 \(C(p)-N(q)\) 的跨点估计；再形成同一个强单调双 Lipschitz 影子，正反纤维误差均在原基点测量。保距扩张 theorem 的量词、数据和参照门与此不同。但两者确有 Kirszbraun、球交和偏差控制的机制接点，故必须逐项比较前提、跨点式、正反同时性与锐常数，不能由上面一个反例便宣称 C03 新颖。

<a id="lr-secondary"></a>
## 次级结果的准确边界

**Paper fact。** 9/18 的 monotone fibres 稿在有限维、凸支撑和绝对连续有限测度、ambient measure contraction property 等条件下，声称普通极大单调关系几乎处处的逆纤维条件测度继承 MCP，且分解不依赖所选 Borel 支。本轮仅核陈述与路线，没有验收核心证明。

**Interpretation。** 它关注给定测度的几乎处处分解；本库 C04 是固定 \((\lambda,L,\gamma)\) 图极大类的每个纤维及任意紧形状实现。极大性类别、量词和测度假设不同，因此不存在从标题直接得出的矛盾或覆盖。若以后研究 Markov / 概率在纤维上的条件化，再审这一接口。

**Paper fact / limited access。** 9 月 ORL 的 HVP-EB 稿摘要报告非凸目标在窗口最大值下降与相对误差条件下的多步速率，含部分指数区间的超线性 / 线性 / 次线性情形。

**Interpretation。** 这可能改变多步收敛稿的比较表，但尚未核其完整 EB 定义、定理及全部条件，不能把它的 value proximity EB 写成本库 \(r_F\) EB，更不能把目标值非单调窗口当作非单调算子类。

<a id="lr-actions"></a>
## 优先级与未闭义务

1. **收敛定位：** 对 GPPA / NFB / Spingarn 建立逐定理、同对象对照；本次已有核方向振荡见证和 C193 的直接固定二次锚排除，剩下的是非平凡核、分裂或升维能否保原对象并覆盖本库条件。
2. **结构定位：** 优先读 2024 / 2026 Ciosmak 的全部相关扩张与单调映射结论，核 C03 的跨点式、正反同影子及统一锐性是否已有相同身份的先例。
3. **应用工具：** 为一个具体凸复合模型核 KKT 论文的完整残差桥，再判断能否给我们需要的真实 EB；非凸或秩亏不能凭题名导入。
4. **总体规模：** 本轮不改“开放”状态。新认证框架的存在增加比较集合，但不能代替自然母空间和非退化量尺的构造。

本次刷新不改变原有主 Claim 身份，不关闭来源覆盖任务，也不宣告投稿新颖性已通过。C197/C198 只是两条明确的文献接口反例，有完整初等证明；未在图中新增外部定理导入边。

<a id="lr-repro"></a>
## 复现与证据边界

从仓库根运行：

```bash
python research/code/literature_refresh/check_scope.py --output research/code/literature_refresh/results.json
python research/validate_assets.py
```

[检查代码](code/literature_refresh/check_scope.py) 仅用标准库，整数 / Fraction 精确算术、无随机 seed、无浮点容差；[结果](code/literature_refresh/results.json) 给运行环境、日期差、上述有限配对、GPPA 有限前缀和 Example 1 的负内积。[原稿版本与 SHA-256](code/literature_refresh/sources.json) 固定本次取得的六份 PDF；原文仍通过一手链接访问，不把第三方全文重复提交到仓库。

**一般结论由本页证明承担。** 有限前缀、有限点对、链接 / 哈希检查都不是对无限轨道、全部 Hölder 点对、整篇外部证明或全球文献穷尽的验证。SHA-256 只识别本次取得的字节；arXiv 未来修订或下载封装变化需重新记录。
