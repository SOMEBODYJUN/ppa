# C11/M1的固定文献接口与直接边界

本页接纳专表中收紧后的固定版本事实和本页自足直接证明。完整范围及统计见
[C11/M1来源范围](../audit/C11_M1_SOURCE_SCOPES.md#cm-scope)；
逐项记录见[C11 §8](../audit/C11_SECTION8_UNITS.tsv)与[M1 §6–§9](../audit/M1_MS_SECTIONS6_9_UNITS.tsv)。
一手卡只给已经读到的指定声明/摘要与调用边界，不接纳原历史宽paper-facts；
全文、版本、原生桥和先行性各门保留。文献字母在每张卡重新绑定，不与项目参数拼接。
以下直接边界各有本页完整证明。文献卡提供已核的目标、条件及调用边界；未打印完整前件、结论和所用定义的外部定理，不由本页授予可直接套用的收敛或速率结论。未读正文仍须恢复准确接口后再调用。

## 3. 可用规范锚及直接数学修订

| 接口 | 当前锚 | 本次固定范围复核用途与限制 |
|---|---|---|
| 实际 Θ2 / limiting ∂ / ordinary distance | [CS-OBJECT](composite_subregularity.md#cs-object) | 文献目标和 residual 必须逐个对齐；题名中的 SOS 不证明同目标。 |
| 复合转移/EB/prox | [CS-TRANSFER](composite_subregularity.md#cs-transfer) / [CS-EB](composite_subregularity.md#cs-eb) / [CS-PROX](composite_subregularity.md#cs-prox) / [CS-OBJECTIONS](composite_subregularity.md#cs-objections) | 本次固定范围复核不新增 C34–C37 定理，仅防止删除 rank、同域、目标一致及局部图门。 |
| 外部来源边界 | [CS-SOURCES](composite_subregularity.md#cs-sources) / [PA-SOURCE](path_atlas.md#pa-source) | 属定位/证据边界锚，不声称其中已接纳本次固定范围复核每个 paper fact。 |
| every legal prefix 与存在性选择 | [PA-DEF](path_atlas.md#pa-def) | 全路径量词；existential selection 另立命题；原生 graph 到 coverage 未自动完成。 |
| 整轨道留域 | [PA-WHOLE](path_atlas.md#pa-whole) | uniform D/G、延拓、H(d0)<dist(x0,Vc)；端点收缩不替代这些前件。 |
| 块 RL/output EB | [PA-BLOCK](path_atlas.md#pa-block) | 只产生终点界；zer Fm=Fix Tm 的目标一致门保留。 |
| 合法词公式/统一半径 | [PA-POWER](path_atlas.md#pa-power) | 有限词或 inf A>1 / sup C<∞ 门；逐词 A>1 不够。 |
| phase cycles | [PA-CYCLES](path_atlas.md#pa-cycles) | 另证端点收敛 + prefix 连续；不从 whole 有限总长定理推出非平凡周期。 |
| 给定显式 T 的捕获/一步因子 | [M1-CAPTURE](../topics/path_dynamics/m1_capture.md#m1-capture) / [M1-SHARP](../topics/path_dynamics/m1_capture.md#m1-sharp) | C38/C39 只关于给定单值 T；一步 distance 因子 3/√10<1。 |
| 点锚与块残差 | [M1-POINT-BOUNDARY](../topics/path_dynamics/m1_capture.md#m1-point-boundary) / [M1-BLOCK-RESIDUAL](../topics/path_dynamics/m1_capture.md#m1-block-residual) | 本次固定范围复核固定点量词/无界比承接；块残差 EB 常数 1 不补 native F 身份。 |
| 原生图未闭桥 | [M1-OBLIGATION](../topics/path_dynamics/m1_capture.md#m1-obligation) | genuinely multivalued Sign、全部选择与显式 T 的同一性仍未证明。 |

<a id="cm-direct-1"></a>
### 3.1 “every fixed point” 与“without bound”两个原量词不成立

对应 MP69-U011（旧行431）和 MP69-U020（旧行433）。仅用当前规范的给定 T，不声明原生多值广义方程身份：

\[
c=\frac23,\quad z_*=(c,0),\quad
z_t=(c+t,0),\quad h_t=\left(\frac32t\right)^{1/3},
\quad Tz_t=(c+t-h_t,0).
\]

对充分小 t>0，t<h_t<1/4，Tz_t∈Z=[−c,c]×{0}，故 T²z_t=Tz_t。于是

\[
\frac{\|Tz_t-z_*\|}{\|z_t-z_*\|}
 =\frac{h_t-t}{t}\longrightarrow\infty,
\qquad
\|Tz_t-z_*\|=h_t-t\longrightarrow0.
\]

对 T² 同一个商。第一步位移 h_t 也趋0。因此无界的是**相对扩张比**，不是绝对点距、位移或距离增量。旧行433的字面“distance increase without bound”需改写。

这在 p=z* 处的一个反例足以否定相对于**整个 Z**的 Fejér 条件、以及要求对每个 fixed point 严格缩距的 paracontraction；不推出每个 fixed point 都增距。为直接看原∀p越界，固定任意 p=(p1,0)∈Z、p1<c，令 a=c−p1>0。充分小 t 可取 h_t<a，此时

\[
\|z_t-p\|=a+t,\qquad
\|Tz_t-p\|=a+t-h_t<a+t.
\]

所以同一序列对这个 p 的距离下降。旧行431应改为“对固定点集 Z 的 Fejér 条件失败”，不能保留“relative to every fixed point”的失败量词。

还可固定 \(p=(0,0)\in Z\)，对原初值球的每个 \(z=(c+a,b)\)，捕获证明给
\(0<c+a-h<c+a\)（\(h>0\)时）；若 \(h=0\)，两者相等。
因此
\[
\|Tz-p\|^2=(c+a-h)^2\le(c+a)^2\le(c+a)^2+b^2=\|z-p\|^2.
\]
非固定输入有 \(h>0\) 或 \(b\ne0\)，至少一个不等式严格。
所以在此整个输入球中，相对于这个特定固定点的降距确实成立，
更直接排除“每个个别固定点的Fejér条件都失败”的读法；相对于整个固定集的Fejér条件仍失败。

若具体文献在同一 Euclidean patch、同一锚 z* 的 almost-averaged / almost-α-firm 条件蕴含某个有限 ε 的

\[
\|Tx-z_*\|^2\le(1+\varepsilon)\|x-z_*\|^2,
\]

该直接前件由无界商排除；T² 也排除。此结论不扩成某论文整体绝不覆盖、所有坐标/metric/算子变换均失败、或整个 native class 超越所有一步理论。相反 C39 已给 T 的一步目标距离收缩 3/√10<1。边界区别需保持。

<a id="cm-direct-2"></a>
### 3.2 端点 contraction 不自动保留内部局部域

对应 MP69-U016/U041，原行432/441。取开域 V=(−1,1)，定义全局连续单值映射 T0(x)=10、T1(y)=0，块端点 C=T1∘T0≡0 为 Lipschitz 常数0的 contraction。x0=0 的每个块端点为0，首个内部前缀却为10，不在 V。故 endpoint contraction/EB 无法单独推出 internal localization。PA-WHOLE 的实际前缀覆盖、延拓和边界预算有独立内容；也不声称只有 G 这一表达形式能证明定位。

<a id="cm-direct-3"></a>
### 3.3 目标区别的独立例，不是外部收敛定理反例

对应 CS8-U022/U051。在 R 中取 f(x)=−x²、g(x)=2x²，则 g proper closed convex、F=f+g=x² coercive/lower bounded，数据 C²。F 的实际 second-subderivative SOS 目标为 Θ2(F)={0}，因为唯一 stationary point 为0且 d²F(0,0)(w)=2w²。

LPQ v4 Eq4 中 prox_g(z)=z/5、∇²f(0)=−2。其要求所有 z 上

\[
\langle \operatorname{prox}_g(z)-0,
 \nabla^2 f(0)(\operatorname{prox}_g(z)-0)\rangle\ge0
\]

但 z≠0 时左侧为 −2(z/5)²<0，故 X*=∅。LP 2024 的 f=ψ(Ax−b) 可取 A=1,b=0,ψ=−x²；其 X* 的 ∇²ψ PSD 门也失败。

此例只说明特殊目标可与 Θ2 不同，**不**反驳 LPQ Th12 或 LP Lemma2：barx∈X* / distX* EB 等前件不满足。若需要非孤立 Θ2，可在 R²取 f(x,y)=−x²、g(x,y)=2x²，得到 Θ2={0}×R、LPQ X*=∅；这个二维例不具 coercivity，不用于 LP Ass1。

<a id="cm-direct-4"></a>
### 3.4 旧 PROVED 打包标签

superseded 六项：

- MP69-U011：旧 Fejér“每个点均失败”量词。
- MP69-U020：绝对距离“无界”字面。
- MP69-U089：旧 Th3.1 标签必须按当前 PA-WHOLE 的修订前件调用。
- MP69-U091：phase 不是 whole 有限总长的无条件推论。
- MP69-U094：无限词逐词 A_w>1 不证明共同半径。
- MP69-U098：native M1 class、scalar γ/q 接口和给定 T 的捕获不能一起标为已验。

这些处置不把已核 algebra/capture 撤掉；它们分别由当前规范锚承接。MP69-U096 保留 scalar-interface 未闭门：如果旧声称意指没有一步 distance contraction，则 C39 已反证；若意指 native γ=1/3、q=1 的某个 RL scalar 判别门，则须恢复原生全部图再逐项核。

## 4. 一手调用卡：C11 §8

以下只核指定版本、指定声明的调用条件。HTML 没有稳定印刷页时用版本/定理号/HTML 行；未凭题名或转引猜页。一个入口的一手摘要核验不升级为全文定理核验。正式刊本与 preprint 未做版本比较的保持门。

<a id="cm-lit-bap"></a>
### BAP

[Bodard–Ahookhosh–Patrinos arXiv2506.22332v1](https://arxiv.org/html/2506.22332v1)，2025-06-27。Def2.2 HTML186–196；Ass1 57–71；Ass3(i)276–286；Th3.6 393–398。Def2.2 确用实际 d²φ 的 SOS 对象。Th3.6 在 critical point、∇²f 邻域存在连续、g 的 prox-regular/twice epi-differentiable/generalized-quadratic 第二次次导数门以及小 γ 下给相应 FBE Hessian PSD 等价。不能把 Th3.2/Ass4 的更强邻域 C² FBE 结论混入。CS8-U005–U009；可接受有限正例，非全球目标定义优先权。

<a id="cm-lit-wx"></a>
### WX

[Wu–Xie arXiv2605.02754v1](https://arxiv.org/html/2605.02754v1)。Def4 135–146；Th3.1 256–258；Th5.1 580–582。Th3.1 ambient slope / manifold EB 对象是全局 minimizer set；f 闭、subdifferentially continuous，M 对0∈hat∂f可识别，Def4 的 M及 f|M 为 C²。Th5.1 的 C1,Lips∇g+λ||x||1、ri stationarity 和零坐标 M 是另一路应用，不误附前一 C² 门。未要求 minimizer 孤立。CS8-U010–U015；“PDF Th7”版本映射未验，保留 deferred。

<a id="cm-lit-lpq"></a>
### LPQ

[Liu–Pan–Qian arXiv2311.06871v4](https://arxiv.org/html/2311.06871v4)。Ass1 70–80；Eq4/§2.1 141–146；Ass2 325–329；Th12 576–581。f C² 在覆盖 cl domg 的开集，g proper lsc convex，F lower bounded；r=||x−prox_g(x−∇f(x))||。X* 是所有 prox_g(z)−x Hess-f 方向 PSD 的特殊 stationary 子集。Th12 假定 X* 的 Hölder EB；q∈(2,3]、γ>1/(q−1)、inexactness 界、有界 generated iterates及 Hessian strict continuity 均保留，非孤立允许。CS8-U016–U023。SIAM DOI10.1137/23M1618697 的正式刊本版本比较未做；不因入口相同即移植精确式。

<a id="cm-lit-ldz"></a>
### LDZ

[Liao–Ding–Zheng arXiv2312.16775v2](https://arxiv.org/html/2312.16775v2)，Th3.1/Table1 HTML201–215。proper closed ρ-weak convex f、非空全局 argmin、同一正 level window 上 SC⇒RSI⇒EB⇔PL⇒QG。QG 反推其余需要 μq>ρ。Table1 给显式常数，但本次固定范围复核只核存在/方向与门，不导入数值公式。残差/目标不能默换为 Θ2。CS8-U024–U029。[期刊 DOI10.1007/s10898-025-01585-3](https://link.springer.com/article/10.1007/s10898-025-01585-3) 的定理/常数与 v2 同一性未比较。

<a id="cm-lit-wang"></a>
### WANG

[Wang–Li–Hu–Li–Li official arXiv PDF](https://arxiv.org/pdf/2308.08735)，第一页 stamp v1 2023-08-17；印刷 p3 Def2.1–2.3，p6 Th3.1。Ω 非空紧、f|Ω 常值；u-LSEB/u-HEB 目标是共同低 level set，非 Ω/Θ2。前向 uKL⇒uLSEB⇒uHEB 指数明确。逆向要每个 Ω 点 prox-regular；γ3∈[1,2)，γ3=2 的二次临界另需 ρ/2<1/μ3。CS8-U030–U036。保留共同窗口、exact target及逆向门；generic supporting machinery 是项目判断。

<a id="cm-lit-ma"></a>
### MA

[Ma–Ouyang–Ye–Zhang arXiv2507.12682v1](https://arxiv.org/html/2507.12682v1)，Th4.4 HTML532–546，Cor4.5 580–595。setup f/g C²、K closed、Φ=g^-1K，§1 Eq2 的增长只在 feasible Φ∩ball 上定义。Th4.4 保留 relative tangent/normal 方向、stationarity、strict multiplier sign及 Lagrange Hessian−support margin。可接纳非孤立 S 的条件二次增长正例，不自动给 residual EB。式37/Cor结论的字面 all-ball 域本次固定范围复核不导入；Cor4.5(ii) HTML 操作数若要用精确式还需 typeset 核验。CS8-U037–U041；不扩成作者原文整体错误判断。

<a id="cm-lit-gao"></a>
### GAO

[Gao–Ouyang–Zhang–Zhu publisher](https://link.springer.com/article/10.1007/s11228-025-00753-7)，2025-04-11，官方摘要 HTML36–40。摘要自述 Asplund generalized-subsmooth multifunction 的 generalized/Hölder subregularity 及 GE/quasi-Newton 应用。页面为 subscription preview/institution login，全文定理未读。CS8-U042–U046：主题/元数据可核；精确定义、no-abnormal 条件、gauge/指数/常数、同域及验证方向全部 deferred，generic graph verifier 非覆盖不能凭摘要关闭。

<a id="cm-lit-lp"></a>
### LP

[Liu–Pan2024 publisher full HTML](https://link.springer.com/article/10.1007/s10589-024-00560-0)，Ass1 75–87，§2.1 155–161，Lemma2 269–271。f=ψ(Ax−b)，ψ C²；g convex、relative-dom 连续，F coercive。X* 为 stationary 且 Hess ψ PSD；r 是单位步 proximal residual。Lemma2 barx∈X*、KL1/2及独立 quadratic growth 前件推出同 ball∩domg 的线性 X* EB。CS8-U047–U052；限定有限正例，不能概称任意实际 d²F SOS 的 KL+growth EB 都已覆盖。目标区别见3.3。

<a id="cm-lit-lw"></a>
### LW

[Lee–Wright Optimization Online official PDF](https://optimization-online.org/wp-content/uploads/2026/02/degeneratePN_new.pdf)，第一页日期 2026-02-11，印刷 p1 Eq1.1–1.5及摘要。Hilbert GE 0∈A+B、A C1、B maximal monotone、S 非空闭；setup 用 resolvent residual R 并**假定**小残差 tube 的 Hölder EB。弱 Jacobian 的具体 rate theorem 全门本次固定范围复核未读。CS8-U053–U058：setup 条件已读，精确 superlinear rate/各 variant Jacobian 假设仍 deferred；旧“abstract/excerpt”审计行为另保留 source-report。

## 5. 一手调用卡：多步札记 §6–§9

<a id="cm-lit-bll"></a>
### BLL

[Bërdëllima–Lauster–Luke official2022 PDF](https://link.springer.com/content/pdf/10.1007/s11784-021-00919-4.pdf)。Def1 p5；Th11 p12；Cor13 pp12–13；Th30 pp21–22；Eq53 p25；§6 pp27–28。Th11保留 FixT 非空、FixT1∩FixT2 非空及同patch pointwise firm 门。Cor13 表面未复述共同 Fix，proof 调用 Th11；本次固定范围复核保守调用保留它，不扩大到 inconsistent common-Fix 空类。Th30另要 invariant D、boundedly compact T(D)、全S同α及由可求和θ定义的ρ；Eq53是块固定集 residual EB。§6确问无common Fix的普通/convex composition preservation以及更易验证gauge characterization。对应 MP69-U001–U006/U057–U066/U101–U104；非全球 priority。

<a id="cm-lit-klan"></a>
### KLAN

[Kohlenbach–López-Acedo–Nicolae author public manuscript](https://www2.mathematik.tu-darmstadt.de/~kohlenbach/Modulus-regularity.pdf)，日期2019-04-28，Th4.1印刷p13。Fejér w.r.t zerF、近零迭代 bound、regularity modulus给Cauchy modulus；complete X/closed zer才给点收敛。finite termination 另需式4.16 residual gap。cyclic Cor4.9 p16/PPA p22应用存在，但全部应用门本次固定范围复核未核完，MP69-U009 deferred。对应 U007–U011/U103。作者稿与期刊全文不自动视为逐式同版本。

<a id="cm-lit-fm"></a>
### FM

[Fullmer–Morse arXiv1703.05233 official PDF](https://arxiv.org/pdf/1703.05233)，Th1印刷p3、paracontraction定义p4。有限family、same given norm、continuous strict shrink toward every own fixed point、common Fix非空。任意词趋向无限频繁出现子family的共同点；若要全family共同点需各map反复出现。Th1是正文引用已知[1]，不作FM最早来源判断。分布式主Th2 control条件未核，本表只按Th1收紧旧“broad control”。MP69-U017–U021/U100/U102。给定T在z*失败足证直接paracontraction门失败，不声称任意norm/其它model均失败。

<a id="cm-lit-ltt"></a>
### LTT

[Luke–Thao–Tam official arXiv PDF](https://arxiv.org/pdf/1605.05725)，第一页stamp v2 2017-03-25、cover2017-03-28。Def2.3印刷p5是有限all-values almost-nonexpansive/averaged界；Th2.18 pp14–15 / Cor2.19 pp15–16结合patch-relative metric regularity、ε/α匹配及gauge线性上控。一般Th2.18还有S、TS、region/gauge门，不能只凭两个名词调用。未来calmness/convergent selection讨论p6；cyclic entanglement/length-orientation讨论p24；RAAR “usually” metric-subregular问题p37已读。对应 U022–U024/U043–U044/U071–U074/U080。具体cyclic/DRS application全门不由abstract接纳；这些是指定版本的历史公开问题，不证明2026仍全球open。

<a id="cm-lit-djl"></a>
### DJL

[Dinh–Jansen–Luke official arXiv PDF](https://arxiv.org/pdf/2502.12285)，v1 2025-02-17。Ass1印刷p21：closed nonempty Aj、Λj/Uj 的 ε-superregular-at-distance、reflector image patches/Λ 跨相位包含。Eq73–76 p23；Ass2 p24：θ满足(76)，另需(a)θ迭代趋0且actual序列Fejér，或(b)θ迭代可求和。Th3 pp26–27：Fix非空、actual patch的gauge EB；点收敛依上述额外门，linear rate再加任意小violation和linearρ。MP69-U025–U029；非convex/inconsistent范围可核，但“only matters for non-Lipschitz”是价值判断，不能验成数学必要性。

<a id="cm-lit-dtt"></a>
### DTT

[Durea–Tron–Théra arXiv2608.06858v1](https://arxiv.org/abs/2608.06858v1)。本次固定范围复核官方 abs/versioned/unversioned HTML/PDF 多次 retrieval InternalError；搜索命中官方摘要，但没有定理原文。标题/摘要只支持 nonlinear/orbital directional regularity 与 fixed-point 应用主题。MP69-U030/U050–U051/U135–U140 及 U033–U037 的 exact theorem、summable geometric sequence、closed graph/completeness与preassigned algorithm/RL noncoverage均 deferred。旧稿“verified theorem”不沿用；不靠摘要重建定理。

<a id="cm-lit-tt"></a>
### TT

[Tron–Théra official publisher](https://link.springer.com/article/10.1007/s10203-026-00568-7)，published2026-04-20。官方摘要支持 n-tupled regularity/pseudo-Lipschitz与exact/approx cyclic fixed-point existence，包括complete/noncomplete setting；全文subscription preview，无theorem text。MP69-U031/U141–U142与U033–U037 保留正文访问门。不能从摘要证明其结果只有existential construction、没有prescribed PPA/RL/generalψ/intermediate budget；不能把DTT的minimal-time归类自动加到此文。

## 6. 真正未闭门、历史行为与组织项

外部未闭门有四类，分别留在每项 remaining_obligation：

1. **全文访问**：GAO、DTT、TT；exact definitions、定理量词/方向、同域/共同尾、目标/残差、正则及非覆盖比较未闭。
2. **版本/精确公式**：WX “PDF Th7”；LPQ SIAM刊本；LDZ正式刊本；MA Cor4.5精确式/可行域；这些不能拿已读preprint/HTML或题名补齐。
3. **局部调用尚未完全读完**：LW各rate theorem；KLAN cyclic/PPA applications；LTT具体cyclic/DRS applications与一般Th2.18全部set/region前件；FM distributed Th2。本表收紧到完整已读声明，不声称已经核其全部理论。
4. **项目原生数学**：native multivalued M1/Sign到给定T的完整输入输出与每条selection覆盖；actual projector/reflector/RAAR active-stratum certificates；合法word统一常数/半径、target identity、full prefix localization与continuation。这些没有因文献正例而关闭。

CS8-U001/U003–U004/U057/U059–U065 与 MP69-U115–U124 是历史日期、查询、使用来源、去重/版本聚合、访问观察的自述；本次固定范围复核新读取不证明旧日期上已运行搜索/独立agent审计。查询字符串拆成独立项以免漏记，不验为已执行 search evidence。CS8-U066 / MP69-U133 的“有限检索阴性不能证全球不存在/新颖性”逻辑边界可保留。

Fit、flagship、closest、strongest、supporting machinery、only matters、proposed class及inclusion/exclusion rule等分别以 nonmathematical 或具体待证方向记录。公开问题的一手段落核验只支持其**历史明确提问**，不判其在当前世界仍无人解决，也不把“计划攻击”升级为“已解决”。五个问题完整解决仍 NOT PROVED；exact nonlinear branch-adjacency RL atlas 新颖性仍 PENDING_VERIFICATION。

Spingarn/selection 已核事实不重做，不扩大相关文献范围。块 resolvent identity 只作为现规范关系级 algebra duplicate，未新增外部 paper facts。有限核验没有全球最早/唯一/不存在/全面优先权判断。
