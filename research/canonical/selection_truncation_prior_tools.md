# 共同尾截断：一手先例与规范调用边界

本页裁决 SS1 `research_note.md` §6.1（646–665 行）的文献和方法断言。
一手事实是下述两个已核引理；其量词均为共同域上的全称条件。
末节另枚举 §6.4–6.5 的未闭比较接口；§6.2–6.3 的数学在
[AGM 独立对象卡](../topics/examples/arithmetic_geometric_mean.md)。
`ST-LIPSCHITZ` 的规范推导写全，以便调用不依赖历史目录。
正文推导为 `derived-checked`，空白接收范围另记；一手原文访问范围与未取得原页另列。
该记录不构成任意阴性检索或全球优先权结论。

<a id="st-literature"></a>
## 已核的一手事实及版本

| 来源 | 已核位置与准确内容 | 调用边界 |
| --- | --- | --- |
| Andrzej Wiśnicki, *Hölder continuous retractions and amenable semigroups of uniformly Lipschitzian mappings in Hilbert spaces* | [arXiv:1204.6464v2](https://arxiv.org/abs/1204.6464v2)，已读 PDF 首页明示 2013-01-15 的 v2，Lemma 1，PDF pp.2–3；[正式刊本 PDF](https://www.tmna.ncu.pl/static/published/2014/v43n1-06.pdf)，TMNA 43 (2014), pp.89–96，Lemma 2.1，印刷 p.91。完备有界度量空间，单步 \(k\)-Lipschitz 自映射，共同增量 \(c\rho^n\)、\(0<\rho<1\)，给 Hölder 极限；证明显式使用 \(k^n\delta+2c\rho^n/(1-\rho)\) | 这是单步 Lipschitz 条件；本文题目中的 Hilbert/semigroup 条件不是该度量引理的假设。来源所写 Lemma 1 是预印本编号，正式版已改号 |
| Víctor Pérez García and Helga Fetter Nathansky, *Fixed points of periodic mappings in Hilbert spaces* | [正式刊本 PDF](https://journals.umcs.pl/a/article/download/3985/2887)，Annales UMCS Sectio A 64(2) (2010), pp.37–48，Lemma 2.1，印刷 pp.38–40，特别 (c)。完整假设在下文 (ST5)；\(p>1\) 时要求 \(\operatorname{diam}X<\infty\)，并给 \(\log(1/A)/(\log p+\log(1/A))\) 指数 | 收敛的是辅助映射 \(u\) 的迭代。该引理本身不要求 \(T\) 周期；周期条件属于后续应用，不能误加入，也不能把 \(u^n\) 换成 \(T^n\) |

Wiśnicki 的 [DOI](https://doi.org/10.12775/TMNA.2014.006) 与正式 PDF 的卷页一致。
PGF 原 PDF 首页 DOI 是 [10.2478/v10062-010-0013-y](https://doi.org/10.2478/v10062-010-0013-y)，
[期刊网页](https://journals.umcs.pl/a/article/view/3985/0) 另列
[10.17951/a.2010.64.2.37-48](https://doi.org/10.17951/a.2010.64.2.37-48)。
网页的 2016 上线字段不改变 PDF 的 2010 卷年。此次核验日期为 2026-10-05。

<a id="st-lipschitz"></a>
## ST-LIPSCHITZ：有限前缀加两尾的完整推导

设 \((X,d)\) 为非空完备度量空间，\(L:X\to X\) 是 \(k\)-Lipschitz 自映射，
\(k>1\)。给定 \(c>0,0<\rho<1\)，假设对**每个** \(x\in X\) 和整数 \(n\ge0\)，
\[
d(L^{n+1}x,L^nx)\le c\rho^n.
\tag{ST1}
\]
则全部轨道有极限 \(R_L(x)\in X\)，满足
\[
d(L^nx,R_Lx)\le\frac{c\rho^n}{1-\rho},
\qquad
d(R_Lx,R_Ly)\le k^nd(x,y)+\frac{2c\rho^n}{1-\rho}
\quad(n\ge0).
\tag{ST2}
\]
令
\[
\theta=\frac{\log(1/\rho)}{\log k+\log(1/\rho)}\in(0,1).
\]
对 \(0<\delta=d(x,y)<1\)，有
\[
d(R_Lx,R_Ly)\le
\left(1+\frac{2c}{\rho(1-\rho)}\right)\delta^\theta.
\tag{ST3}
\]
因此 \(R_L\) 连续，且是到 \(\operatorname{Fix}L\) 的回缩。
本规范结论甚至不需有界性；共同增量 (ST1) 已有一个全域常数。
若另有 \(\operatorname{diam}X=D<\infty\)，(ST3) 可把 \(\delta\ge1\) 的点对也
用 \(D\delta^\theta\) 控制，从而成为全域 Hölder 界。
这个强化来自下述证明，不冒称 Wiśnicki 原引理删去了有界性。

**证明。** 对任意 \(m>n\)，三角不等式和 (ST1) 给
\(d(L^mx,L^nx)\le c\rho^n/(1-\rho)\)。完备性给极限和第一条尾界。
单步 Lipschitz 的全域量词允许迭代为 \(k^n\delta\)，再加两条共同尾即为 (ST2)。
取
\[
n=\left\lfloor\frac{\log(1/\delta)}{\log k+\log(1/\rho)}\right\rfloor.
\tag{ST4}
\]
floor 的两侧分别给 \(k^n\delta\le\delta^\theta\) 和
\(\rho^n\le\rho^{-1}\delta^\theta\)，证明 (ST3)。
\(L\) 连续，故 \(L(R_Lx)=\lim_nL^{n+1}x=R_Lx\)。若 \(Lx=x\)，轨道恒定，
故 \(R_Lx=x\)。这证明回缩身份，没有要求 Hilbert 几何。
若单步 \(k\le1\)，直接在 (ST2) 令 \(n\to\infty\) 给非扩张极限；
若 \(k<1\)，还给全部初值的同一极限。

<a id="st-auxiliary"></a>
## 辅助迭代接口：为什么 PGF 的 \(T\) 不是迭代器

设 \(X\) 非空完备且有界，\(D=\operatorname{diam}X<\infty\)，
\(T:X\to X\) 连续，\(u:X\to X\) 为 \(p\)-Lipschitz，\(p>1\)。
给定 \(0<A<1,B>0\)，要求全部 \(x\in X\) 满足
\[
d(Tu(x),u(x))\le A\,d(Tx,x),\qquad
d(u(x),x)\le B\,d(Tx,x).
\tag{ST5}
\]
令 \(x_n=u^nx\)，则
\[
d(Tx_n,x_n)\le A^nd(Tx,x),\qquad
d(x_{n+1},x_n)\le BA^nd(Tx,x)\le BD A^n.
\tag{ST6}
\]
ST-LIPSCHITZ 以 \(L=u,k=p,c=BD,\rho=A\) 给 \(R_u=\lim_nu^n\) 的共同尾和
指数 \(\log(1/A)/(\log p+\log(1/A))\)。若 \(D=0\)，结论由单点空间直接成立。
\(T\) 连续与 (ST6) 另外给 \(TR_ux=R_ux\)。
\(Tx=x\) 时 (ST5) 第二式给 \(ux=x\)，故 \(R_ux=x\)；
因而 \(R_u\) 是到 \(\operatorname{Fix}T\) 的回缩。
它也是到 \(\operatorname{Fix}u\) 的回缩，两固定集由 (ST5) 相等。

这些式子全部沿 \(u\) 迭代，没有给 \(T^n\) 的共同尾。
规范调用采用本页 (ST6) 和 \(u^n\) 的直接证明，
不能从一篇讨论周期映射的标题推断周期 \(T\) 自身迭代收敛。

<a id="st-disposition"></a>
## SS1 §6.1 的逐项去向与剩余义务

| 源范围 | 去向 | 精确理由与下一步 |
| --- | --- | --- |
| 646–650、749 | `rewritten` 至 [ST-LIPSCHITZ](#st-lipschitz)；一手版本见 [文献表](#st-literature) | 原文已有相同前缀加两尾方法。新增规范证明把指数及回缩身份写清；不判断最优性 |
| 652–657、750 | `rewritten` 至 [辅助接口](#st-auxiliary) | 保留 \(T\) 与 \(u\) 的不同对象；所有增量、前缀和极限只沿 \(u^n\) |
| 659–664 | 方法判断由上述一手引理支持；两个非幂包络 `duplicate` 至 [SS-TRANSFER](solution_selection_rates.md#ss-transfer) | 现有 SS-T4–T5 已闭合局部尺度，SS-T2–T3 已独立算出指定非幂上界；不再复制第二份证明 |
| 665 | 两篇已读引理未陈述指定非幂量级的有限原文判断；一般先行性保持 `deferred` | 已核引理的单步前提是 Lipschitz。它们未直接给 SS 的 Hölder 有限步包络，不代表任何旧一般命题也没有这一内容 |
| 665、721、763 | BL00 Proposition 1.10 保持 `deferred` | Wiśnicki 只把它列为先例，不能由转引恢复其条件。此次 AMS 书目与预览入口未取得命题原页；仍需原页核有限步模/尾函数的一般性及是否显式计算相同量级 |

SS1 的 `research_note.md` 成员 SHA-256 为
`91ad4b0948a21443fc557b5ea579e692650399504e735223d72347ba86bea1b8`；
在 [SS1 修订 ZIP](../../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)
中可按上述行定位。所有外部原文均只在线核验，没有新增历史原件或附件。

<a id="st-open-comparisons"></a>
## §6.4–6.5：精确来源报告与未闭的比较接口

下表区分 SS1 来源报告与当前实际核过的准确接口。LP22、LMZ 和 P16 的全部条件、对象映射和指定版本位置已移入[规范一手接口页](selection_primary_interfaces.md)，不必读取审计区补定义。其余来源声称“已读全文”仍只是历史访问报告，不继承已核状态。

| 原件引用及位置 | 来源所报告的独立断言 | 准确未闭义务 |
| --- | --- | --- |
| LT，705 行；755 行书目 | Lemma 2 / Theorem 2 给局部 PPA 收敛与点尾，未给本稿指定的两初值极限模 | 当前 [LIT-LT-2025](../LITERATURE.md#lit-lt-2025) 已核的是 Definition 2 / (10)，不是这两个收敛结论；须核其完整假设、尾式和与 SS-TRANSFER 的对象比较 |
| LTTQ，705、756 行 | arXiv:1605.05725v2 Theorems 2.15、2.18、Corollary 2.19 的 almost-averaged/次正则率；正式版相应为 2.1、2.2、2.3 | 对两版本逐号核陈述；另判断点态条件与共同域全对 Hölder 条件的差异，不凭术语相近就作替换 |
| LTTP，705、757 行 | Theorems 1–2 的非扩张/averaged 极限继承非扩张；Theorem 4 不要求非扩张；来源声称已读全文且没有坏选择结论 | 三项分别核全文和 Theorem 4 的实际假设；历史“全文缺口已关闭”不证明任何当前断言已验收 |
| LMZ，707、758、722 行 | arXiv:2406.13207v1 Theorems 4.3–4.4、Remark 4.5、Example 4.6；高阶实际点收敛，例的 PPA Q-二次但唯一极限 0；正式 DOI 版差异未闭 | v1 4.3/4.4/Remark4.5/Example4.6已按[规范接口](selection_primary_interfaces.md)逐项核；4.3有限长与4.4实际点率分开，例的λ_L为项目步长倒数。全实域恒定选择为另行直接证明；正式版差异U090仍未闭 |
| LP22，707、754 行 | 一元半代数增长与有限图正则性工具 | v2 Lemma2.2及Prop3.1/Th3.1/Cor3.1已按[规范接口](selection_primary_interfaces.md)核；有限图只读作有限维闭半代数关系，存在性界不授指定常数。刊本数学跨号/全文差异未闭 |
| B93，709、759 行 | 满秩光滑零流形上 Gauss–Newton 有共同二次点尾与 \(C^k\) 初值–极限映射 | Theorems 2.1–2.2、3.1、(2.1) 的完整假设及一致范围未核；把它定位为精确同对象前身仍需原文证明 |
| P16，709、760 行 | 正则拟算术均值的共同双指数尾；生成元导数不退化且 \(| v1及指定正式跨号已核；完整S_K含f″局部有界变差，导数处处非零不等于统一下界。指定打印负n0尾有F44解析反例；[C158](selection_quasi_arithmetic_boundary.md#qa-uniform-tail)独立修复共同尾与同域选择界，正AGM窗不移到轴，φ段不归无对应段的刊本 |
| CHH，711、761 行 | clean intersection 和切法向导数条件给光滑极限回缩；二阶回缩不等于点误差 Q-二次 | arXiv:2605.17384v2 的全文、Assumptions 1–3、Proposition 2、Theorems 2–3、Lemma 4.9 的身份及定义均未在本页核；不能从标题补导数/速率假设 |
| KR，711、762 行 | 一般 NHIM 先给连续相位；逆向构造预设光滑相位并用法向支配保持正则性 | arXiv:1608.08442v1 Proposition 1、§3.2.2、Propositions 6、8、Theorem 2 的原文未在本页核。一个定理只保证连续，不等于已经构造非任意 Hölder 的反例 |
| BL00，665、721、763 行 | Proposition 1.10 是可能覆盖截断一般性的更早入口 | 命题与证明原页未取得；检查任意有限步模和任意共同尾的允许范围、以及是否算出指定非幂量级，不能以 W14 的特例反推 |
| Chicone–Liu，723 行 | *Asymptotic phase revisited*，JDE 204 (2004), 227–246 是未排除入口 | 书目原始身份、DOI、全文及实际定理号未核；不把候选入口叫作已证相同先例 |
| Battelli–Palmer，723 行 | *Smoothness of Asymptotic Phase Revisited* 是未排除入口 | 作者原文、准确版本、定理号和覆盖范围未核；不从标题补光滑性条件 |

来源 717–719 行的 NO-EXACT-PRIOR-FOUND 仅是一个带 2026-09-19 截止日的
有限阴性检索报告。本页没有复核其全部检索过程，更没有把它变成全球首创证明。
旧原件的“最小贡献包”可以逐条映射到 SS-TRANSFER、C139 和 C141 的数学证明；
是否是新的联合贡献仍是独立文献义务。投稿等级及录用判断（726 行）不是数学结论。

<a id="st-open-questions"></a>
## 724 行的开放目标：已枚举，答案仍开放

1. 固定保守 \(\kappa\) 的认证类内是否仍有同量级锐性：须先冻结同一完整图类及
   其它预算常数，不能从固定实际 \(q\) 的 C139 直接改名得到。
2. 在 C139/C141 的指定完整模型、固定参数、同一输出 collar 和输入对尺度内，
   求反射 Hölder 比值上确界，从而确定有限尺度最小 \(L\)；渐近系数不自动等于这个值。
3. 在同一超几何模型与配对下确定 stretched-log 指数前最佳常数；
   C141 的指数不能提高不回答最佳系数。
4. 对具体 signed-Schur 完整图研究初值–极限稳定性；先认证共同输入、全部纤维和尾，
   不能仅凭增长 jet 证书授予一般稳定性。
5. AGM 的提升、换变量和其它增强实现须先给完整关系及与 AGM 的身份桥；
   [AGM-COMPATIBILITY](../topics/examples/arithmetic_geometric_mean.md#agm-compatibility)
   只否定直接编码，没有穷尽这些新对象。

<a id="st-enumeration"></a>
## 本批枚举范围和非覆盖缺口

[SS1_SECTION6_UNITS.tsv](../audit/SS1_SECTION6_UNITS.tsv) 按独立定义、数学断言、
外部事实、检索/访问报告、开放目标和组织余项列出精确去向。主范围为原成员
**642–727 物理 LF 行**（完整 §6，包括所有空行）；引用记录范围为
**745–763 物理 LF 行**（§8 和全部本节书目）。同一物理行包含多个独立断言时，
允许多个单元共享定位，不用拆行制造数学进度。原成员有 763 个 LF、末尾 LF、无 CR；
文件总计 763 物理行，哈希见前文。

本表自身不覆盖 1–641 或 728–744 行；这些行现已由
[SS1_CORE_UNITS.tsv](../audit/SS1_CORE_UNITS.tsv) 全部独立枚举，
两表并集为 **1–763**。整体范围、数值版本边界及证明对应见
[SS1_FULL_COVERAGE](../audit/SS1_FULL_COVERAGE.md#ss1-full)。
完整枚举表示每项有去向，不表示全部文献原页、优先权、原生模型桥
或全库来源分母已经关闭。
