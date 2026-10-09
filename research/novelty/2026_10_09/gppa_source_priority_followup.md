# 2608.01584v1 的来源优先性复核：全纤维归约与固定版本门

日期：2026-10-09 UTC。审查基线：工作树 `94cbbbd`。对象是 Le–Mordukhovich–Théra 的 **2608.01584v1（2026-08-03）**，不是本库一般模结果的全球新颖性宣告。本次只写本报告及 `research/code/gppa_novelty/gppa_source_priority_check.py`；没有更改 canonical、CLAIMS、状态或图，没有自行 commit。第三方 PDF 仅下载到 scratch 临时目录，不发布为新增仓库资产。

## 结论及证据层次

源 T1 本身明确归于 [13,14]；T2 的全部核轨道可以精确归约为经典强单调极大扩张上的普通 PPA；Lemma 3 的核范数比较是既有 Tikhonov 比较的同一内积证明；T4 的正则化、有界不消失误差与 R-continuity 骨架已有 **2606.01536v1（六月）T3**，并非必须借九月 v2 才能确认。

这不等于“整篇没有创新”。最保守的剩余贡献是：**把这一骨架整理为可非单射、可多值的 pair-monotone 原物理对象的定理，并直接以原 F 的逆 R-continuity 回代物理集合距离，不假设 v 的逆存在或有模。** 此表述比 2025 强 pair 定理和六月 Id 核定理的逐字陈述弱前件/不同输出；它仍由本文给出的经典归约与初等原图残差桥推出，不能再称一个新的强单调几何或新的收缩原理。未核到更早完整同表述，不证明该 formulation 的全球优先性。

严格区分：下表是**来源实际陈述**；后面的全纤维商关系、Zorn/Minty 扩张和误差输送是**本轮审计推导**。不能把现代可导性倒写为旧作者已明确发表同一表述，不能以可归约性推断作者动机或来源不当。

## 实际核读的一手版本

“PDF页”为一基物理页。不同网页可能重新生成日期，本次固定版本判断以 PDF 水印和 arXiv submission history 为准。

| 来源 | 日期/版本与实际核读范围 | 对源 GPPA 的准确关系 |
|---|---|---|
| [2608.01584v1](https://arxiv.org/pdf/2608.01584v1) | arXiv提交 2026-08-03 01:37:27 UTC；PDF题头 2026-08-04。归档14页全部读取，尤其 D1–D6 pp4–6、T1 p6、T2 pp7–8、Lemma3 pp8–9、T4 pp9–11。 | 本次被审查对象；T1标 `[13,14]`，新陈述重点是 ASM 和 T4。 |
| [2501.13637v1](https://arxiv.org/pdf/2501.13637v1)；出版 DOI [10.1007/s10957-025-02770-w](https://doi.org/10.1007/s10957-025-02770-w) | arXiv 2025-01-23 13:10:44 UTC；PDF题头 Jan24。实读 D3.1/P3.2 pp6–7、P3.4 p7、P3.6 p8、T4.2及证明 pp9–10、Remark4.3 p11、T4.5/4.6 pp11–12。正式2025出版版全定理编号未复核。 | P3.4已有 transformed resolvent 单值/firm；T4.2强 pair+Lip v已有核线性率；Remark4.3(ii)仅在 v 可逆时写 F∘v⁻¹。没有把本轮全纤维扩张冒称该文原文。 |
| [2601.12738v1](https://arxiv.org/pdf/2601.12738v1) | arXiv 2026-01-19 05:37:49 UTC；PDF题头 Jan21。实读 D2.4 p5、§4 Assumption1/1′ p11、Lemma4.1/4.2 pp11–12、T4.3及(i)/(ii)证明 pp13–14。 | 惯性参数取0给残差/闭图/R-continuity输出，但原定理仍要求**线性 v、γF+v injective**。不能逐字宣称其假设自动覆盖 Aug T1 任意 v/多值输出。 |
| [2606.01536v1](https://arxiv.org/pdf/2606.01536v1) | arXiv **2026-06-01 01:33:52 UTC**；PDF题头 June2。实读D1/2 pp4–5、T3完整陈述与证明 pp5–7；其余Tseng部分不承担本报告判断。 | 六月已有Id核、极大单调原A、Tikhonov、持续δ误差、一般ρ以及 ε²误差政策。 |
| [2606.01536v2](https://arxiv.org/pdf/2606.01536v2) | arXiv **2026-09-08 08:59:24 UTC**；PDF题头 Sep9。T3及完整证明 pp6–7，逐词归一化比较v1。 | T3条件、预算、κ与关键证明同v1；新增引用/讨论不改变本轮所用先行定理。九月版本本身不能作为8月3日前先行，六月相同内容可以。 |
| Rockafellar (1976), [DOI](https://doi.org/10.1137/0314056)，[实际核读原文PDF](https://www.cs.cmu.edu/~suvrit/teach/papers/1976_rockafellar_monotone_operators_proximal_point_algorithm.pdf) | August1976, 14(5),877–898。实读 pp878–881（PDF2–5），尤其(1.13)–(1.15)强单调收缩；P1 p881；T1及证明 pp883–885（PDF7–9）；T2 pp885–886。 | 普通极大单调PPA、firm耗散、强单调 q=(1+γα)⁻¹ 已明确陈述。其T2 inverse-Lip要求唯一零点，不能逐字当作原F多零物理EB定理。 |
| Le (2024), [正式JCA PDF](https://journalofconvexanalysis.com/articles/jca31014/jca31014.pdf?v=2)，[metadata](https://journalofconvexanalysis.com/articles/jca31014/) | JCA31(1),243–254；received2021-11-15、accepted2023-05-24；预印本[2311.13096](https://arxiv.org/abs/2311.13096)于2023-11-22。实际读正式PDF p243–244、T3.1及证明印pp248–249（PDF6–7）。未以accepted日期冒称公开日期。 | T3.1已有正则化根范数不增及 d(xε,S)≤ρ(εa)；Lemma3的Id版先例直接可核。 |
| Le–Théra [2408.09139v1](https://arxiv.org/pdf/2408.09139v1) | 2024-08-17。实读D1/2 p4、T11及证明p10、T14及证明pp11–12。 | 真原算子选中残差→集合距离率已有明确机制；T11是极大单调/全局R-Lip且γ>2L，不能当任意pair定理。 |
| Bùi–Combettes [1908.07077v1](https://arxiv.org/pdf/1908.07077v1) | 2019-08-20预印本；正式JMAA491(2020),124315。实读D1.1 p2与后续已知特例段。 | warped resolvent名称/核机制早于2026；原D1.1有极大单调M、K+M单调且injective门，不覆盖任意原F非单调全文。 |

2025 HTML网页本次题头显示“August24,2026”，但其固定v1 PDF明确题头Jan24,2025、水印Jan23,2025；因此不以HTML动态题头裁定优先日。arXiv2606/2608网页经web工具多次DisabledError，普通HTTPS实际下载成功并读全文；获取错误没有数学排除力。

本次 web routes（供主代理再次open后引用）：2501固定PDF `turn39view3`；2501 metadata `turn48view2`；2601 HTML `turn3view3` / `turn60view5`；2608 metadata `turn74academia9`；Rockafellar原PDF `turn48view0` / `turn60view4`；Le2024原PDF `turn60view3` / `turn67view0`；正式JCA metadata `turn57view1`。六月/九月T3的证据是上述精确PDF下载，web无法正常解析该两PDF，不能给一个虚假的成功web ref。

## 1. 全纤维关系与ASM的精确身份（本轮推导）

设H实Hilbert，F:H⇉H，v:H→H任意单值全域。**取全部纤维和全部F值**：

\[
Q=\operatorname{ran}v,\qquad A(z)=\bigcup_{x:v(x)=z}F(x)\quad(z\in H),
\]

空并集为空。于是 domA⊂Q，且

\[
\operatorname{gra}A=\{(v(x),f):x\in H,f\in F(x)\},\quad
A^{-1}(f)=v(F^{-1}(f)),\quad \operatorname{zer}A=v(\operatorname{zer}F).
\]

对所有原图点(x,f),(y,g)的源ASM

\[
\langle f-g,v(x)-v(y)\rangle\ge\epsilon\|v(x)-v(y)\|^2
\]

**当且仅当** A 为ε-强单调关系。两个方向都只需分别选取纤维代表/取像，不删除原图分支、不选单值截面、不假设v injective。mere pair-monotonicity同样等价于A monotone。物理半度量d_v(x,y)=||v(x)−v(y)||也只是这一商几何；ASM标签是否更早出现未完成术语穷尽，但它对应的operator geometry确为经典强单调。

固定γ>0时，任意合法原步满足

\[
x^+\in(v+\gamma F)^{-1}v(x)
\iff v(x)-v(x^+)\in\gamma F(x^+),
\]

故 z=v(x),z⁺=v(x⁺) 满足 z⁺∈J_{γA}(z)。反向若z⁺∈J_{γA}(z)，A的**并集定义**提供一个原物理代表x⁺和合法原值，因而给合法物理步。不同代表可能有不同物理行为，但kernel输出由A单调性唯一。更完整地，

\[
\operatorname{ran}(v+\gamma F)=\operatorname{ran}(I+\gamma A),\qquad
v\circ(v+\gamma F)^{-1}=J_{\gamma A}
\]

在共同定义域上成立。这也解释2025 P3.4的firm输出，而无需v逆。

<a id="source-classic"></a>
## 2. 强单调极大扩张使T2核轨道成为经典PPA

不能默把A称作maximal：原文只给coverage于Q。下面显式补全经典导入门。

若A为ε-强单调，B=A−εId为单调关系。按图包含排序，任一单调扩张链的并集仍单调；Zorn给极大单调扩张B̂。令

\[
M=\widehat B+\epsilon\operatorname{Id}\supset A.
\]

M是ε-强单调。其maximality可用Minty逐项核：对于每个γ>0、任意p∈H，

\[
p\in(I+\gamma M)(z)
\iff \frac p{1+\gamma\epsilon}
\in\left(I+\frac\gamma{1+\gamma\epsilon}\widehat B\right)(z).
\]

右边由B̂极大单调的Minty resolvent满域性有唯一解；左边因此满域，Minty给M极大单调。这里仅导入Rockafellar原文p878明确调用的经典Minty事实，不偷补A原图maximal。

源coverage Q⊂ran(v+γF)=ran(I+γA)保证JγA在Q上存在。由A⊂M，任何JγA值也是JγM值；后者单值，故

\[
\boxed{J_{\gamma A}(z)=J_{\gamma M}(z)\in Q\quad(z\in Q).}
\]

这保留**每条**合法原物理选择的kernel轨道。设S=zerF非空，则p=v(s)是A与M零点。强单调性使这两个关系的零点均唯一，故zerM=zerA={p}；所有s∈S有相同v(s)。不需要Q闭、v连续、v逆或最近点。

现在Rockafellar1976 (1.13)–(1.15)直接给

\[
\|z_{k+1}-p\|\le q\|z_k-p\|,\qquad q=(1+\gamma\epsilon)^{-1}.
\]

因为q²<(1+2γε)⁻¹，此结果严格蕴含源T2(a)第一估计。源第二估计也由同一个强单调内积展开给出：设 f⁺=(z−z⁺)/γ∈A(z⁺)，则

\[
\langle z-z^+,z^+-p\rangle\ge\gamma\epsilon\|z^+-p\|^2,
\]

\[
\|z-z^+\|^2+(1+2\gamma\epsilon)\|z^+-p\|^2\le\|z-p\|^2.
\]

这是经典PPA强单调耗散的代数式，不是只有一个相似rate比较。源平方是能量估计，不能当二次Q阶。

**T2(b)物理门保持原F。** R-Lipschitz of F⁻¹ at0具有半径σ、常数L。所选原值

\[
f_{k+1}=(z_k-z_{k+1})/\gamma\in F(x_{k+1})
\]

指数趋0，因此最终||f||≤σ。完整inverse inclusion给

\[
d(x_{k+1},S)\le L\|f_{k+1}\|\le L(1+q)q^k\|z_0-p\|/\gamma.
\]

这闭合全部原物理集合距离，而非只kernel distance。它是经典核收缩加原图EB桥；不能因为M有唯一kernel零点就说原F只有一个物理零点，也不能把集合距离提升为物理点收敛。

一个完整反退化例：H=R²，v(r,s)=(r,0)，F(r,s)={(ar,0),(ar,−s)},a>0。F非单调，v非单射，强物理pair失败，而ASM常数a成立；A在Q=R×{0}恰为aId+N_Q，为极大/a强单调。原S={0}×R，F⁻¹有globalR-Lip常数1/a。每步r⁺=r/(1+γa)，第二坐标可任意选；取s_k=(−1)^k k，物理点不收敛、距S仍线性趋0。该例说明剩余物理 formulation 的区别真实，却也说明kernel全轨道仍是经典PPA。

## 3. T1各输出的来源与量词

源T1 p6标明 `[13,14]`，所以其作为该论文的新结果本已不成立。实际核到的固定先行版本有额外门：2025 T4.2(i)需v inverse及其弱连续；Jan2026 T4.3需线性v与γF+v injective，惯性参数置0恢复相同输出。不能仅引用其标题删掉这些前件。

但任意mere-pair版本也可由本轮全纤维A再取**任意极大单调扩张M⊃A**闭合核结论：coverage仍保证JγM|Q=JγA，且原非空零点保留。Rockafellar P1(c)/T1给平方耗散与||z_{k+1}−z_k||→0。此时M可以有新增零点，**不宣称zerM=zerA或核弱极限可物理提升**。

对原物理输出另用真实 f_k∈F(x_k)：f_k→0，加F的强输出/弱输入闭图给每个原物理弱聚点属S。给F⁻¹ R-continuity则最终 d(x_k,S)≤ρ(||f_k||)→0。这两个桥不需kernel弱极限或v逆。后者距离桥已见Jan2026 T4.3(ii)和更早普通PPA R-continuity文献；本轮没有找到完全相同任意v/全部物理选择的更早逐字定理。

## 4. 六月v1与九月v2的T3逐项对照

两版共同T3条件为：A极大单调，S=zerA非空，A⁻¹ at0 R-continuous withρ；x_{k+1}=J_{γ(A+εId)}x_k+y_{k+1}，||y||≤δ，固定γ,ε,δ>0。**六月v1已经给**

\[
\limsup_k d(x_k,S)\le\delta(1+1/(\gamma\epsilon))+\rho(\epsilon a),
\qquad a=\|P_S0\|,
\]

以及δ=ε²后的 ε²+ε/γ+ρ(εa)→0。共同证明用q=(1+γε)⁻¹、精确输出w_k=x_k−y_k、qδ/(1−q)=δ/(γε)、正则化根范数不增，以及三角距离回代。

归一化T3文本比对发现的变化只有页码、`it`→`this`、原 `[8]` 改编号 `[14]`、提取时ε²上下标布局。没有新的T3预算或假设。九月新增Zaslavski讨论和更长references不能被搬到六月；**本报告只追溯六月实际已出现的T3**。

## 5. T4：旧收缩骨架与原物理回代的精确门

设pair(F,v) monotone，v全域L-Lip，S和Sε非空。Aε=A+εId正好是完整纤维关系对应F+εv。先取M⊃A极大单调，再Mε=M+εId极大/ε强；任意已有合法精确物理输出 x̂_{k+1} 的核值 w_{k+1}=v(x̂_{k+1}) 恰为 JγMε(v(x_k))。选sε∈Sε，其cε=v(sε)是Mε唯一零点。原pair内积（同Le2024 T3.1(16)）给||cε||≤inf_{s∈S}||v(s)||=:a，无需a取到。

物理误差x_{k+1}=x̂_{k+1}+e_{k+1}，||e||≤δ，造成kernel误差η=v(x_{k+1})−v(x̂_{k+1})，||η||≤Lδ。因而kernel是标准inexact PPA：

\[
z_{k+1}=J_{\gamma M_\epsilon}z_k+\eta_{k+1},\quad
D_{k+1}\le qD_k+L\delta,\quad
\limsup D_k\le\frac{L\delta}{1-q},\quad q=(1+\gamma\epsilon)^{-1}.
\]

这与JuneT3证明中的收缩/稳态管同型，且无需假定M⁻¹ R-continuity。不能直接引用JuneT3的完整距离结论来获得原物理距离：原F⁻¹ EB不自动成为一个任意maximal扩张M⁻¹的EB，也没有v inverse将kernel距离拉回物理距离。这里必须单独保留原F图上的值。

为看清回代，设u=z_k−cε，w=w_{k+1}−cε。原F值为

\[
f_{k+1}=\frac{u-(1+\gamma\epsilon)w}{\gamma}-\epsilon c_\epsilon\in F(\widehat x_{k+1}).
\]

原pair与(sε,−εcε)比较给 ⟨u−(1+γε)w,w⟩≥0，故

\[
\|u-(1+\gamma\epsilon)w\|^2\le\|u\|^2,
\quad\limsup\|f_{k+1}\|\le
b_{\epsilon,\delta}:=\frac{L\delta(1+\gamma\epsilon)}{\gamma^2\epsilon}+\epsilon a.
\]

如果b<σ，所有b<t<σ最终打开F⁻¹半径门：limsup d(x_k,S)≤δ+ρ(t)，故可写δ+ρ(b+)。非减ρ未必在b正点右连续，不可凭limsup把ρ(b+)无门改成ρ(b)。这是独立复算；与当前C216一致，不标记为本报告新增Claim。

δ=ε²时b=Lε/γ²+Lε²/γ+εa。源印刷预算B=4Lε/γ²+3Lε²/γ+εa。若L>0，B>b严格，选ε足够小使B<σ，则最终真实残差≤B，恢复源印刷 ε²+ρ(B)，无需ρ正点连续。L=0时v恒定，原值直接−εv，单独得ε²+ρ(εa)。这说明源结论可由旧收缩与同原图桥完整恢复，其印刷proof的几个省略门可严格补齐，不能夸大为致命错误。

还需明确两点：

* 原T4没有明列regularized coverage；“sequence generated”可理解为对已有无限合法轨道的条件定理。若宣称全部初值/误差政策都有轨道，需另核 Q⊂ran(v+γ(F+εv))。Sε非空不自动保证这项。
* 源κ=(1+2γε)⁻¹ᐟ²下使用 κ/(1−κ)≤2/(γε)，等价于γε≤4，必须纳入“ε sufficiently small”（γ固定）。标准q的q/(1−q)=1/(γε)无此门。双极限要求同一F,v,γ,ρ下对每个足够小ε存在合法轨道族；它不是一条ε_k随k变化轨道的定理。

## 6. 优先性可用/不可用的最终口径

可用：源AugGPPA用非单射kernel与完整pair假设，把经典monotone/strong-monotone核收敛和Tikhonov稳定性输送到原非单调物理关系。T2核部分有完整经典归约；T4的Id核骨架及更紧Id距离管在Junev1已出现。原物理集合距离桥的任意kernel formulation仍有组织/应用价值，其确切全球首次陈述尚未认证。

不可用：ASM创造新的算子强单调几何；T2 kernel linear rate不是经典PPA的特例；首次warped kernel；首次Tikhonov+持续有界误差+R-continuity；物理点必线性收敛；只因原F非单调就超出所有普通单调PPA；或者“全文非原创/没有任何贡献”。现代逐项归约与先行逐字陈述是不同强度的证据。

未核空白：2025正式出版版相对arXiv v1的定理扩展；pair ASM同形条件在η-monotonicity/cocoercivity/semimetric文献中的首次明确发表；Zaslavski2010/2012原文的全部前件（仅相关metadata/线索，未承担本报告定理导入）；原[1]2024 pair概念更早术语链。2011 H(·,·)-cocoercivity与2008 f-monotonicity搜索命中只提供线索，实际核到2008 Definition1.2的rhs是原物理距离，不是ASM；不能靠术语相近宣称同一结果。

## 可复现记录

脚本：`python3 research/code/gppa_novelty/gppa_source_priority_check.py`，Python stdlib/Fraction，确定性、无随机数。26,244个值对核查上述二维ASM例、原F非单调性、kernel输出相等；核q²与源平方因子、γε≤4门、b/B差额；展示物理第二坐标发散而集合距离收缩。有限检查仅佐证正文解析推导，不证明全参数结论或全球优先性。

临时PDF SHA-256：

| 固定文件 | SHA-256 |
|---|---|
| 2608.01584v1（仓库既有归档） | `5f07147a258e441193dd918452909ddc2fec8781257d6005348f233016653e91` |
| 2501.13637v1 | `a9eb3f93ece5a8a0b847bee76df7e5aabd3764d03e2da35cd6b816049d3c704d` |
| 2601.12738v1 | `425012dd5a8942e53ce8dc62741a4a9428e94e869412c0dc89e3d523edb75387` |
| 2606.01536v1 | `69749d7af6ca91181da20612c28471aaa585b04d1d0f3aa4f9cd7e14ccc0ba99` |
| 2606.01536v2 | `808442bda977e38509dead3c5d66af0f0299afbe04f51053f0efcc0e2a151d8e` |
| 2408.09139v1 | `75101f40771b675f14bdfd428a6809a9601cf7352626dc5b53729c74f273b5fe` |
| 1908.07077v1 | `567d5d7a31a26b2cd27862a0ea405ffae30b6a1a08507d083403a425303e0172` |
| Rockafellar1976实际读取扫描 | `a9a65b8ee3cff2a0c5b4a93da925388522ea49f674c8d52c421508d5009456f3` |
| Le2024正式JCA PDF | `8b8e4201da9d3ece9682690fe9ba93e773766dfa059756aef7b42be173665745` |

第三方PDF和提取文本保留于scratch临时目录 `gppa_priority_tmp`，不进仓库、不作为报告不可见证明的一页；核心公式与全部导入门已在正文重写。


## 追加独立接收：C221 与幂 EB 的旧耗散推论

本节接收时间同2026-10-09，范围只及新页 `research/canonical/gppa_tail_lyapunov_bridge.md` TL1–TL20，以及Li–Mordukhovich2012旧PPA耗散的dyadic consequence。接收不修改该页状态，不替代其作者的全原文审查；本报告起初GPPA source priority判断保持上述独立对象。

**C221：未发现fatal数学异议。** 独立逐式核到：由单个初始r的可和正项上界得到[0,r]上Weierstrass均匀收敛，故L连续且L(t)=b(t)+L(τ(t))；TL7用严格长度预算建立每个有限前缀的共同不变集，随后继续coverage，没有先假定无穷轨道；ambient H完全性与closed Z给精确目标，即使Q不闭也不丢limit。all-pairs RL给小输入距离上的共同连续模，因而K闭包上的唯一连续扩张成立，且扩张不冒充Q域外原coverage。若仅zero-anchor RL，则不调用这一单值闭包接口。

TL10–11亦正确：B²≤Cω≤qV，在R≤M下cap不启动，V(τ(t))≤qV(t)，所以B(τʲr)≤q^{(j+1)/2}√V(r)；这确实闭合先前NGK5文字没有自行宣称的标量尾，且没有用实际轨道长度定义L。

SF→ABS接口也通过：完整两分支由输入符号选定，H1需要β≤2γ，H2需要ν(β−1)≥γ，其交集非空当且仅当γ≥ν/(2ν−1)；等号可取β=2γ=1+γ/ν。f=|r|^β是C¹且KL product精确为1，实数β无需通过semialgebraic术语补门。由显式r_{k+1}=|r_k|^ν和几何主控先得boundedness及function-attentive cluster，满足H3，然后可调用ABS，而不预先使用ABS点收敛。实际本次读ABS作者稿D2.4 PDF7、H1–H3 PDF8、Lemma2.6及关键proof PDF8–11、T2.9完整陈述与证明PDF12（web `turn107view1` / `turn108view3`）。

ABS实际所读一手作者稿：[Optimization Online PDF](https://optimization-online.org/wp-content/uploads/2010/12/2864.pdf)；Li–Mordukhovich实际所读一手作者修订稿：[UNSW PDF](https://web.maths.unsw.edu.au/~gyli/papers/lm-subreg12final.pdf)。以下页码对应这两个固定下载文件，不对应可能后续重排的网页版本。

**Li–Mordukhovich2012 fixed-step PPA的q>1/2有限长度是明确的旧结果推论。** 本次实际读其作者修订稿October12,2012的§7，(7.7)/(7.9) PDF26（印26），T7.3(i) PDF28（印28）；web `turn107view0` / `turn108view0` / `turn108view1`。设S=zerT、s_k=||x_{k+1}−x_k||、d_N=d(x_N,S)。对每个固定零锚p∈S，从N到2N−1相加(7.7)得

\[
\sum_{k=N}^{2N-1}s_k^2\le\|x_N-p\|^2.
\]

取inf_p（极大单调时也可直接取P_Sx_N）即∑s²≤d_N²。Cauchy–Schwarz于是给

\[
\sum_{k=N}^{2N-1}s_k\le\sqrt N\,d_N.
\]

旧T7.3(i)对固定λ>0与0<q<1给d_N≤C N^{-a}，a=q/[2(1−q)]。在N=2ʲ上相加，

\[
\sum_{k\ge1}s_k\le C\sum_{j\ge0}2^{j(1/2-a)}<\infty
\quad\text{当且仅当此上界指数条件 }q>1/2.
\]

有限长度给H中strong Cauchy limit，再由d_N→0与S闭给limit∈S。q=1时旧指数距离率直接给可和块。这里“当且仅当”只判断这条上界的几何级数，不是所有原PPA轨道长度的必要门；q≤1/2不能据此推发散。旧源并未在所读位置逐字陈述这个finite-length corollary，所以应写**旧定理+两行dyadic推论**，不能写“2012原文已直接发表同一C212定理”。

C212自身的局部/非maximal kernel对象不必调用新增零集M的EB。只要原零锚对和原真实EB的合法窗口门已逐步认证，其( NGK27 )给

\[
d_k^2-d_{k+1}^2\ge s_k^2
\ge\lambda^2K^{-2/q}d_{k+1}^{2/q}.
\]

这就是旧LM(7.9)的同一原目标Z标量递推；可复用LM scalar-sequence证明得到相同幂距离率，再作上述time-block推论，始终保持原Z。**仍须先给coverage及留域，或对每个合法有限前缀建立统一小于collar的预算后归纳继续。** 单凭一条“已经无限留域”的轨道不能反授予任意初值存在或留域。C212现有壳层证书恰给所有合法有限前缀的通用gauge统一长度预算，因此其完整自足门保留；其幂q>1/2角的finite length/point convergence不宜再承载新的宽机制优先性。

复算 `python3 research/code/gppa_novelty/noncalm_coverage_followup_check.py` 通过；这是已有作者脚本的独立运行，26,244值对GPPA source脚本也通过。ABS临时PDF SHA-256=`f116b2cba2b3f3f42e3b901f8b02040b7f1bdc9398d25dad3ad11618179028b0`；LM2012=`d04141ba3f8e0e239ea53443f03a1c5690745a35b9719bb3f91893b62b35f01f`。没有新增第三方PDF到仓库。

## 追加独立接收：C222 精确边界与 Cayley 反演

本次实际读 `research/canonical/sharp_holder_lipschitz_realization.md` SHLR1–21 全文；审查任务限数学可接受性，没有新增外部来源检索。**未发现fatal数学异议。** 下述判断不认证C222或平方混合的公开优先性，也不把本轮推导倒标成Goebel旧文的逐字结果。

* **任意实Hilbert：** SHLR4 对有限凸组合用Hilbert方差恒等式，并以距离函数连续取极限；无维数或紧凸包的隐藏前件。投影只需Q非空闭凸，闭凸包确有这些性质。K紧性保证闭及有界，足够本页全部步骤。d(y)>0 在Q\\K上与y≠k₀共同保证E(y)≠0，故没有额外固定点。
* **直径预算边界：** SHLR7 的3αh与SHLR8 的2α(D²−h²)/D分别成立，后者同时对(y,z)和(z,y)使用SHLR4。t≤1/2时3t≤6t(1−t)；t≥1/2时2(1−t²)≤6t(1−t)。凸函数t^{−(1−γ)}在1的切线给SHLR11，6α≤1−γ于是直接获得D^{1−γ}界，没有严格L余量。所有k,l∈K被固定又强迫任何γ-Hölder常数≥sup||k−l||^{1−γ}=D^{1−γ}。所以D=L^{1/(1−γ)}的等号情形确实包括，而不是只有逼近边界。
* **全域单值F与graph-max：** G的强单调模c=(1−η)/2、Lipschitz界M=(2+η)/2正确；0<t<2c/M²使SHLR15的全H映射成为收缩，Banach给每个u的唯一逆像，无需有限维紧性或额外Minty门。由u±λF(u)=a,R(a)，每个p=a∈H已有一个原图点；任何同参数RL扩张中的点以相同p比较时右侧为0，故其Cayley第二坐标也相同，再由线性反解(x,v)唯一。这是所称RL graph-maximal，证明没有偷用monotone极大性。
* **投影残差符号与统一界：** 投影法向射线恒等式给P_Q(2u−P_Qu)=P_Qu，故G₀⁻¹u=2u−P_Qu。SHLR17于是以正号(u−P_Qu)/λ为参照。LipG₀⁻¹≤2与G−G₀=E∘P_Q/2给||a−a₀||≤||E(P_Qa)||≤αD，因此误差≤αD/λ≤ηD/λ；没有遗漏额外因子或符号反转。F的Lipschitz预算也正确：Lip(Id−R)≤1+η，与LipG⁻¹≤2/(1−η)及1/(2λ)相乘得SHLR2。
* **D=0：** 非空K必为{k₀}，R≡k₀的最小Hölder常数为0；G(a)=(a+k₀)/2可逆，F(u)=(u−k₀)/λ，零集准确、参照误差0、LipF=1/λ落在声明预算内。同参数L>0的graph-max证明仍适用，不调用含D分母的平方混合。

独立运行已有 `python3 research/code/gppa_novelty/structure_priority_check.py` 得PASS：102,710 scalar checks、55,945 square checks；数值仅复核算术实现，正文全参数论证承担结论。本接收没有改canonical页、主图或claim状态。
