# 共同尾截断：一手先例与规范调用边界

本页裁决 SS1 `research_note.md` §6.1（646–665 行）的文献和方法断言。
一手事实是下述两个已核引理；其量词均为共同域上的全称条件。
末节登记 §6.4–6.5 的已核比较与具体未闭接口；§6.2–6.3 的数学在
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

下表登记本次固定版本的一手复核去向。具体条件与直接证书在
[选择文献接口](selection_literature_boundaries.md)，版本和印页在
[LITERATURE](../LITERATURE.md#lit-selection-interfaces)。
历史“已读全文”不继承为当前数学认证，指定陈述比较也不替代全球先行性。
LP22/LMZ/P16 的完整前提、精确版本及倒数参数另在[规范补充接口](selection_primary_interfaces.md)；[C160](selection_quasi_arithmetic_boundary.md#qa-selection)还直接给同域两初值 Lipschitz 界，与 C158 的共同尾相容。

| 原件引用及位置 | 当前已核去向 | 准确剩余义务 |
| --- | --- | --- |
| LT，705、755 | [SL-LT](selection_literature_boundaries.md#sl-lt)：六处正式陈述已读；受限图近端、球内选路径和真残差分开；Lemma2尾可独立求和 | T2的邻域/不变窗/精确尾，以及P1严格上端门，均不可无条件导入；两指定选择模未在该正式版主文陈述，非全球首创结论 |
| LTTQ，705、756 | [SL-LTT](selection_literature_boundaries.md#sl-ltt)：v2三号与刊本2.1/2.2/2.3逐陈述跨号已核；固定锚、全部输出及环域条件分开 | 不扩大成一般点尾或共同域全对Hölder；指定三条对应不证明整篇逐字等同 |
| LTTP，705、757 | 作者公开全文Th1–4/Remark1已读；Th1–2强极限的非扩张性由SL2独立传递；Th4仅EB；[C157](selection_literature_boundaries.md#sl-witnesses)给两个接口见证 | 正式issue印页与作者上传版对应未闭；一般φ率的可评价/比较迭代门不授derived；历史访问事件只保留报告 |
| LMZ，707、758、722 | [SL-LMZ](selection_literature_boundaries.md#sl-lmz-lp)：v1 Th4.3/4.4/4.5/4.6已读；4.4确为点误差，4.6直接核完整唯一输出、实际Q2和恒零选择 | 刊本编号/条件增改对应未闭；不删除站立假设，不把惩罚系数当同方向步长，不排除其它坏选择先例 |
| LP22，707、754 | v2 Lem2.2/Prop3.1/Th3.1/Cor3.1已读；闭半代数图紧集EB无需有限纤维；多值continuity为开逆像式 | 刊本逐号/条件对应未闭；存在性不补SS1数值EB或严格兼容，单步图不给无限极限半代数 |
| B93，709、759 | [SL-B93](selection_literature_boundaries.md#sl-b93-chh-kr)：原刊Th2.1–2.2/3.1及式2.1已读；真正局部初值–极限先例，原假设只给C^{k−1}，旧C^k已纠正 | 共同双指数尾须局部收小并冻结常数；不扩到整个零流形，不称同一PPA/坏选择联合定理 |
| P16，709、760 | [C158](selection_literature_boundaries.md#sl-p16)：v1生成元/AGM/不变表示已核；安全共同双指数尾独立重建，精确分母式另有解析阻断 | 刊本Th3.2/3.3、引理/AGM对应已核；Th3.3分母精确界仍受解析阻断，v1 Th3应用单独引用；固定直径R/K不可省，轴上K不统一；任意φ不使固定M任意粗糙 |
| CHH，711、761 | v2 Ass1–3/Prop2/Lem4.9/Th2–3已读；安全接口为局部切初始化束域C1/C2及共同几何点尾 | 高p全C^{p−1}未由指定证明闭合；二阶回缩是初始化导数概念，不等于迭代Q2 |
| KR，711、762 | v1 Prop1/§3.2.2/Prop6/8/Th2已读；连续轨道相位、预设光滑相位、集合距离尾分别记录 | 精确k1/k3支配阈值与L身份仍未闭；只保证连续不是已给坏Hölder例；历史访问日志不作为数学调用门 |
| BL00，665、721、763 | 书目身份和AMS许可Google Books预览已核；W14只称其引理是Prop1.10的variant | 命题/证明原页未取得；任意有限步模、任意共同尾及是否算出两指定非幂模均具体deferred，不能由W14倒推 |
| Chicone–Liu，723 | Asymptotic phase revisited，JDE204(2004)227–246为待比较入口 | [作者2003-12-23预印本](../LITERATURE.md#lit-phase-candidates)全文及指定号已核；余刊本对应、Th2.8 C2余项证明门和SS静止点身份桥 |
| Battelli–Palmer，723 | Smoothness of Asymptotic Phase Revisited为待比较入口 | [机构书目/摘要](../LITERATURE.md#lit-phase-candidates)已核，无关联文件；正文、定理号和精确正则门仍未取得 |

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
