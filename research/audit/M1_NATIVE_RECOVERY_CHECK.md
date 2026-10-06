# M1 原生循环模型：现有材料恢复检查

<a id="m1r-result"></a>
## 结论与限定

2026-10-06在本会话可用材料中，**没有恢复出生成有限捕获映射M1的原生循环Sign方程、全部内部选择及完整纤维身份桥**。
现有外层公式、捕获证明、一步锐因子都不是缺件；缺口是外层映射到特定历史原生模型的身份。
这次检查不能把“尚未找到完整模型”扩大成“任何材料里都不存在等价数学内容”。

同时找到了两项具体来源事实：

1. 打包台账明确排除了 `T5_AUDIT_C_MULTIVALUED_M1.md`，并保存其字节数与SHA-256。
   当前全部物理文件、ZIP成员及本轮附件均没有这个内容哈希。这是真正的**已知原文件缺件**，
   但没有证据保证它含有所需有限捕获Sign模型，不能先把它当作必然解锁文件。
2. 历史离线HTML另嵌入一份未展开的Frankowska 1989原始PDF，已从当前HTML读取、核哈希并检索。
   该原件可用于后续一手文献核验，但不是M1原生模型；未把它新增到history或附件中。

本页不修改C38/C39/C64/C65状态，不新增数学Claim，不关闭原生身份deferred。
只新增本恢复说明及两个搜索证据表；所有原件字节、共享总账和规范正文保持不变。

<a id="m1r-search"></a>
## 实际搜索范围与解码方法

[M1_RECOVERY_SEARCH_MANIFEST.tsv](M1_RECOVERY_SEARCH_MANIFEST.tsv)记录433个位置各自的
完整定位、原字节SHA-256、字节数、解码方法、文本行数及各组查询命中数。
这是**检索记录**，不是逐数学断言枚举，不进入已完成语义范围分母。

| 范围 | 位置数 | 实际处理 |
| --- | ---: | --- |
| `history/sources/`全部物理文件 | 251 | 所有字节核哈希；文本扫描，11个ZIP逐成员读取 |
| 11个ZIP的全部非目录成员 | 178 | 每个成员读取、核哈希并按类型处理；无嵌套ZIP成员 |
| 本会话`project_sources/`已下载用户附件 | 4 | 精确指定文件读取；1个TeX、3个PDF |
| 上述合计 | 433 | 不是433个独立字节内容或定理 |

388个位置按UTF-8物理LF扫描。24个PDF出现位置使用Poppler `pdftotext 24.02.0`
的`-layout -enc UTF-8`，均退出0；其中20个有文本，4个无文本的是作者字形PDF，
不是未能抽取的数学正文。4个DOCX扫描全部`word/*.xml`中的普通文字与OMML文字节点，
覆盖文档、表格、页眉页脚及可见公式文字；其中仅`RL_Flagship_Model_Report.docx`含1张媒体图片，
已打开核看为材料应力–应变与速率敏感性相图，不含M1循环方程。
另6个不可按UTF-8阅读的位置是作者PNG、TTF、TFM及其同字节ZIP副本，保留支持资产身份。

搜索按五组进行，覆盖原文、TeX、代码、JSON/YAML/CSV、HTML和解码PDF/DOCX：

| 查询组 | 实际关键模式 |
| --- | --- |
| 身份 | 独立词M1及M-1/M_1；SO-06/SO06；`MULTIVALUED_M1` |
| 符号图 | `Sign`，TeX的`operatorname`/`mathrm`下的sign/sgn/Sgn |
| 捕获与循环 | `two-step capture`、`finite capture`、有限捕获、两步捕获、循环与广义/Sign同句 |
| 公式特征 | `z_1-3z_2`及常见下标变体；`73/96`与TeX分数；96与√10/sqrt邻接 |
| 原生来源 | `T5_AUDIT_C_MULTIVALUED_M1`；M1与cyclic/循环同句 |

这轮机器命中107个位置、390条文本行；命中包含普通sign、另一种M1标签、PDF把指数排成“M 1”等噪声。
对涉及原生身份的关键命中，进一步读取了其定义段、前后假设、审查表与来源合同，而不是仅按文件名判定。
PDF公式排版不是原生LF；搜索表的`text_lf`对PDF/DOCX只表示本次解码文本定位。
没有对所有PDF图片逐页OCR或完成全部来源语义审查，故未命中仅是本次恢复范围的负证据。

### 离线HTML的隐藏载荷也已核对

`研究资产统一超边知识图_v2.html`的`asset-payloads` JSON含68项base64资源，
构建脚本`构建_v2.py` LF301–307明确把标为`research_original`的文件内嵌。
[M1_RECOVERY_EMBEDDED_CHECK.tsv](M1_RECOVERY_EMBEDDED_CHECK.tsv)逐项记录解码后的哈希：
67项与433位置中的现有原件完全同字节；唯一没有物理/ZIP匹配的是资源ID `frankowska`。
HTML模板只有占位符，没有另一个待恢复载荷。

嵌入的Frankowska文件为1580010字节，SHA-256：
`a1d05d419913cd9bdb463ca868f705960c96598c5be582fb58908b55111c2892`。
HTML资产元数据给原路径
`05_文献证据与来源快照/01_关键原始论文/Frankowska_1989_逆映射原始论文.pdf`，
原英文名`frankowska_1989_inverse.pdf`。
解码PDF首页为H. Frankowska, *High order inverse function theorems*,
Annales de l’I. H. P., section C, S6 (1989), pp.283–303；有22个PDF页面，
`pdftotext`产生1159 LF，M1/Sign/有限捕获特征无命中。
它只在scratch临时读取，没有作为新历史附件加入库，也没有在本任务核其定理适用性。

## 当前四附件不是新增的M1来源

四文件均与`history/sources/次单调论文研究/最新成果/`对应文件字节完全相同：

| 当前附件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `01-Holder_RL_Formal_Manuscript.tex` | 71218 | `1c7c870d1468a565792aa44b98c95b60031fd7e586c46d1f175f824dd2e92deb` |
| `02-Holder_RL_Formal_Manuscript.pdf` | 460907 | `abecd2595a9731ed17c963ed7d1b7c442cbcc027a6237d4d9bb7c347f5927c8b` |
| `03-2026_09_25_siopt_combined_candidate.pdf` | 483003 | `f515dad127cfeef38a85b7fa39aae31fe7cb644b73fead0b00878cfb26908453` |
| `04-Holder_RL_Pedagogical_Companion_CN.pdf` | 676435 | `eee6d7ac4f9a0bac0493b90cdd776283d8ec7cefe72a3a1b59061817d01388d6` |

TeX唯一相关宽模式命中在LF1514，属于另一个分段sign构造，
没有M1/循环/两步捕获或`z_1-3z_2`身份。三个PDF解码也未给原生M1。
因此当前附件并未补上一个在历史字节集合之外的新模型定义。

<a id="m1r-evidence"></a>
## 关键来源：实际有什么，缺什么

下表各Markdown范围均为**原文件物理LF**。完整路径可沿链接进入；
所有哈希也在搜索清单中逐位置保存。

| 现存来源 | 精确定位与哈希 | 可证内容及边界 |
| --- | --- | --- |
| [多步路径札记](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/多步路径与有限捕获_RL研究札记_2026-09-09.md) | LF330–346定义f、T、Z；LF347来源声明；LF348–386半径/捕获/指数；SHA `74d9a2b464aba8d9b585b7c30e61b8faca8eab78b23da7f634cac04c5a18b4b4` | 外层T完整可读；只称它来自先前cyclic M1含Sign的构造，且**selected implicit inverse**单值。未写生成方程、相位或全输入的全部合法解 |
| [旗舰升级札记](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/RL旗舰升级_架构与待攻关接口.md) | LF36–46输入，其中LF46为“用户给出的M1实际外层障碍及两步捕获证明”；LF64–125重算外层T一步因子；SHA `c346477dc8ed1f372e94adafbc98f5d39249fbcce9a94654f9e014d8d1560c09` | 提供T的进一步证明，没有打印更早用户材料或原生Sign方程。ZIP `RL_T4_CODEX_HANDOFF_2026-09-09.zip!/RL_FLAGSHIP_UPGRADE_ARCHITECTURE.md`是同字节副本，不能补缺 |
| [T5F总体审稿](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/04_证明审计与敌对审稿/总体敌对审稿_修复清单与PRO导入许可_T5F.md) | LF244–289；SHA `c8051e2b5c6b8aba640bdda54dc873b33476c7c99d4719e854a4cadada67945e` | 把M1标为SO-06的隐式coverage任务；只显示一般Φτ与Λ，并明确要求先固定A,B,P,R,ℒ,𝔮,Ω等全部对象。没有给有限捕获例的这些具体数据 |
| [结构化公开问题](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/04_公开问题与未来攻关/01_原始公开问题/结构化算子公开问题_用户原始材料.md) | LF191–213 SO-06；SHA `646ab1a29819c8b6a96dff9508082e1e264632226241a1efe7c1366d555fad3b` | 同样是一般composite inverse的公开问题摘要，不是有限捕获Sign实例的完整方程；其外部引文未在此重新验证 |
| [T5E实例审稿](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/04_证明审计与敌对审稿/最终合稿_实例常数与反例重审_T5E.md) | LF83–110；SHA `20002ded0e0acfa115c3303b040f00399695f29a3573f06480d49f216529f428` | 确实给完整两分支F与direct-Minty范围，但明确称coverage回归benchmark，未匹配SO-06全部假设；它也不是有限捕获T，下面直接排除同一性 |
| [随机多值应用稿](../../history/sources/次单调论文研究/ATTACK_MULTIVALUED_RANDOM_RL_APPLICATION.md) | LF24–33、382；SHA `f6d361e1ff0990e5e34aae4cbdb6e6cb7be76528d1a6dd8b46829f8a1bf39a02` | 引用`T5_AUDIT_C_MULTIVALUED_M1.md`，说明M1不自动桥到PPA/Markov及完整inverse与selector量词；没有复制所引文件的完整模型 |

### 有明确字节身份的缺件

[纳入与排除台账.csv](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/00_从这里开始/纳入与排除台账.csv)
本身83928字节、SHA-256
`8717065f1e87eb08dabb2a28424869fa16a5d064a78a03122050980088b99e58`，LF7给：

```text
T5_AUDIT_C_MULTIVALUED_M1.md
bytes = 33580
sha256 = 86812a2ca69b138db4f5bfd501886b64e4c4bcdc311c60b51a6619fbdbd984d2
status = EXCLUDED
reason = 中间代理 / 旧排序 / 旁支冗余；当前综合、最终审计及边界摘要优先
```

该文件名在可读来源中有引用，但433位置与68项HTML载荷都没有这个哈希。
这给出一个比“缺某份M1证明”更准确的恢复目标。
不过多步稿没有明确说其LF347“先前验证”指的就是这份T5C文件，
旗舰LF46也没有给先前用户材料的文件名；所以不能保证恢复T5C就恢复了有限捕获Sign实例。
台账排除理由是打包选择，不是该数学内容已被后稿完全吸收的证明。

### 当前repo的既有Git历史也未恢复该路径

以本次检查时HEAD `360b42f6f4ccd62f86363e43486ca82447a8cef3` 为定位，
`git rev-parse --is-shallow-repository`返回`false`，本地`--all`可达提交共105个。
对这些已有Git引用执行只读路径历史检查：

```text
git log --all --full-history --format='commit %H' --name-only -- '**/T5_AUDIT_C_MULTIVALUED_M1.md' 'T5_AUDIT_C_MULTIVALUED_M1.md' '**/*T5*MULTIVALUED*M1*' '**/*T5C*' '**/*T5_C*'
git log --all --full-history --format='commit %H' --name-only -- '**/*MULTIVALUED*M1*' '**/*cyclic*M1*' '**/*CYCLIC*M1*' '**/*M1*Sign*' '**/*M1*SIGN*'
```

两次命令均退出0且无路径/提交输出。因此**当前repo已有历史中未见这些候选路径**。
没有从旧提交找到可读取的该原件，也没有据此加入新history文件。
这不声称远端未获取的引用、仓库之外的上游或未知改名路径不存在它，
更不把它的内容预判成有限捕获Sign原生证明。

<a id="m1r-identity"></a>
## 同名M1材料不能补身份：两个直接论证

### 现存direct-Minty benchmark不是有限捕获映射

T5E给出的完整关系是
\[
 F_b(t,y)=\{(-\sqrt y,y),(-\sqrt y,-3y)\}\quad(y\ge0),
 \qquad F_b(t,y)=\varnothing\quad(y<0).
\]
对单位步长输入\((p,q)\)，正q只可能来自第一支，负q只来自第二支；
q=0时两支均只有y=0。于是全部近端纤维恰为
\[
 J_{F_b}(p,q)=\{(p+\sqrt{|q|/2},|q|/2)\}.
\]
这是其完整纤维计算，不是选一支所得。它的完整零集是\(\mathbb R\times\{0\}\)。

有限捕获稿则定义\(c=2/3\)、
\(f(r)=\operatorname{sign}(r)[(3/2)(|r|-c)_+]^{1/3}\)及
\(T(p,q)=(p-f(p-3q),0)\)，固定集是\([-c,c]\times\{0\}\)。
对任意充分小\(\varepsilon>0\)，在同一端点附近输入\((c,\varepsilon)\)，
\[
 T(c,\varepsilon)=(c,0),\qquad
 J_{F_b}(c,\varepsilon)
 =\{(c+\sqrt{\varepsilon/2},\varepsilon/2)\}.
\]
二者连端点的任意小完整输入邻域也不一致，零集也不同。
因此不能以已找到T5E的完整图，宣布有限捕获T的原生图恢复；
未给出的坐标变换、metric、组合相位或投影桥也不能凭相同M1名称补入。

### 单个selector只确定子图，完整近端纤维才确定原图

设给定空间H、同一步长\(\lambda>0\)、输入集U及确定映射\(T:U\to H\)。定义由观测确定的配对集
\[
 G_T^U=\{(Tz,(z-Tz)/\lambda):z\in U\}.
\]
如果只知道\(Tz\in J_{\lambda F}(z)\)对全部z∈U成立，则只能得到
\[
 G_T^U\subseteq\operatorname{gph}F\cap
     \{(y,v):y+\lambda v\in U\}. \tag{M1R1}
\]
如果已证明每个输入的**完整**纤维为\(J_{\lambda F}(z)=\{Tz\}\)，才有等号。

**证明。** 选择条件逐z就是\((z-Tz)/\lambda\in F(Tz)\)，给包含。
若完整纤维已知，取右侧任意\((y,v)\)，令\(z=y+\lambda v\in U\)，
则\(y\in J_{\lambda F}(z)\)，所以\(y=Tz\)、\(v=(z-Tz)/\lambda\)，给反包含。
反之等号也立即给完整纤维等式。
全域U=H时等号唯一确定完整原图；只有局部U时，U以外Minty输入对应的图点仍不确定。证毕。

源LF347只说“selected implicit inverse”单值，并没有给\(\lambda\)、空间、metric和该逆到一个完整J的身份。
若外层T还是多个隐式相位的组合或投影，(M1R1)的单步前提也尚未认证。
[现有新Sign实现](../topics/path_dynamics/m1_sign_lift.md#sl-graph)
已经证明某个新定义\(F_{\mathrm{lift}}\)的完整J₁=T；它解决的是存在性构造，
不是所缺的历史身份。这里没有把新反向图改名为历史原生F。

<a id="m1r-minimal-gap"></a>
## 最小恢复目标与尚需证明的门

缺件与未证明身份分开保留：

| 类型 | 精确缺口 | 达标后应核什么 |
| --- | --- | --- |
| 已知原文件缺件 | 33580字节、hash `86812a2c…d984d2` 的T5C审查文件 | 先检查是否真的含有限捕获Sign实例；若只讨论SO-06一般问题，不得据此关闭toy模型身份 |
| 来源未定位 | 多步LF347所称先前cyclic M1构造，以及旗舰LF46所称用户外层障碍/捕获证明的原始模型定义 | 最少需要原生广义方程/图、所有变量空间、相位/参数、Sign(0)约定、允许输入和完整输出；无需恢复无关旧对话 |
| 现有公式未证明身份 | 现成T、一般Φτ、direct-Minty benchmark、新F_lift彼此没有历史原模型识别桥 | 明确到底是完整J、指定selector、多个相位组合，还是投影后的外层状态；逐输入证等式，不能只证一个好解存在 |
| 全选择与路径桥 | 原生每相位的全部合法选择和相邻步骤可继续性没有定义 | 从B_R(z*)每个输入出发，量化全部允许内部解；第二轮必须覆盖第一轮全部实际输出，不能仅核初值球；再核Z吸收是全选择还是指定策略 |
| 真实残差与指数 | 原生r_F、原生零集与输出窗口未确定，故q_EB,max=1和同对象γq=1/3仍是来源报告 | 恢复完整图后对全部纤维取inf，核零集/metric/步长；独立证EB上界与排除q>1的同一非零序列；不得拿新F_lift残差顶替 |

可直接继续的任务是恢复一个最小而完整的“原生模型定义页”，
或从确切T5C原文件追出该页的位置；没有必要再次证明已核外层T的捕获与一步因子。
如果最终确认历史只定义了一个selector，应把该历史命题明确降为指定策略的外层结论，
而不是强求不存在证据的全选择结论。

这次恢复检查没有找到可以诚实关闭上述原生桥的原始方程。
新增433位置搜索表、68载荷哈希对账与具体缺件线索，使下一轮可以从准确位置接续，
而不是把“未打印定义”“文件缺失”“未证完整身份”“外部原文未核”混成一个笼统待办。
