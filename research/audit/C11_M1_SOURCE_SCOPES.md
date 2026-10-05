# C11 与 M1：逐断言来源范围和原生身份缺口

<a id="cm-scope"></a>
## 明确枚举的范围

本记录以现有原件的物理 LF 行和字节哈希为分母，不把旧表的一条整节记录当成整节数学验收。
专表按独立定义、结论、外部适用性、来源声明及组织余项给出13字段。
总登记见 [ATOMIC_SCOPE_REGISTRY.tsv](ATOMIC_SCOPE_REGISTRY.tsv)，逐项去向见 [UNIT_DISPOSITIONS.tsv](UNIT_DISPOSITIONS.tsv)。

| 现有物理来源及范围 | 原子专表 | 范围内状态 |
| --- | --- | --- |
| 多步路径与有限捕获札记 §5，LF326–425；全件524 LF，SHA-256 74d9a2b464aba8d9b585b7c30e61b8faca8eab78b23da7f634cac04c5a18b4b4 | [M1_MS_SECTION5_UNITS.tsv](M1_MS_SECTION5_UNITS.tsv)，39项 | 20 rewritten、4 duplicate、6 nonmathematical、9 deferred；100物理LF无缺口 |
| C11复合札记 §8，LF312–337；全件420 LF，SHA-256 d9f9e5c53c41d827a7fd25250fbd5cbee3c3f2d08c41d245dc9b8f552b084619 | [C11_SECTION8_UNITS.tsv](C11_SECTION8_UNITS.tsv)，72项 | 43 rewritten、10 nonmathematical、19 deferred；26物理LF无缺口 |
| 多步路径札记 §6–§9，LF426–524；与§5同一字节原件 | [M1_MS_SECTIONS6_9_UNITS.tsv](M1_MS_SECTIONS6_9_UNITS.tsv)，162项 | 52 rewritten、21 duplicate、6 superseded、38 nonmathematical、45 deferred；99物理LF无缺口 |

物理来源的完整相对路径写在各专表的 source_locator，不用不存在的ZIP入口替换它。
M1 LF326–524连续覆盖§5–§9共199行；1–325未被这些专表枚举。C11只有§8的26行被本表枚举。LF14的来源声明虽作为依赖读过，不计入§5枚举。三范围共273条来源记录，不表示273个独立数学结果。

<a id="cm-native"></a>
## M1：外层已证与原生未给分开

[现行显式映射](../topics/path_dynamics/m1_capture.md#m1-object)定义完整，C38/C39直接证明两步捕获及同球锐一步集合距离因子。
本次补入[粗总长及固定点锚障碍](../topics/path_dynamics/m1_capture.md#m1-point-boundary)、
[两步块残差与局部固定集](../topics/path_dynamics/m1_capture.md#m1-block-residual)的自足短证明。
扩张的是这个已定义外层的直接推论；[新Sign反向实现](../topics/path_dynamics/m1_sign_lift.md#sl-graph)仍是独立新关系，
不认证旧历史方程。

U005–U007明确拆出旧“含Sign的真正多值模型”“已验证原生来源”“选定隐式逆单值”三种身份断言。
U016–U018的原生真残差最优指数及同对象乘积障碍缺完整关系。
U033–U034及U036保留外部定理比较、替代几何和旧验证标签的具体证据门。
源公式的固定点锚发散商只否定对全部固定点成立的降距条件；它不表示相对于每个固定点都增距。
发散的是比例，绝对点距趋零。到集合的收缩和个别固定点的增距可同时发生。

本轮只读检索范围为当前物理历史文本的有关命中及上下文、
11个现有ZIP的157个可解码文本成员（3,698,436字节）、ZIP内8个PDF的文本、
13个物理PDF的提取文本和4个DOCX的段落文本。
未在这些可检索文本中找到能认证该原生Sign捕获模型的完整方程。
这不是对所有扫描图像或未命名公式的逐像素检查，也不是原模型不存在的证明。
同名SO-06/M1、Barroso M1及其它M1标签有不同明确对象，不以字符串相同拼接身份。

要关闭原生桥，须给下列具体材料及证明：

1. 每相位完整包含式、变量、耦合、参数、步长、metric及Sign零值约定。
2. 各实际可达输入的存在性与全部输出纤维，区分指定selector唯一和完整逆排他。
3. 对每个输入，把全部合法内部路径的外层末点集合证明为恰好 \(\{Tz\}\)；仅包含 \(Tz\) 不够。
4. 全部内部前缀的可延拓、留域、共同预算和在目标集上的全选择吸收。
5. 原生零集及完整真残差的目标、实际输出窗、残差窗、上界和同一非终止序列锐性。

它们是[F03完整纤维门](../../FAILED_ROUTES.md)和[M1原生义务](../topics/path_dynamics/m1_capture.md#m1-obligation)的具体实例。
恢复定义之前，重复重算同一外层T的两步捕获不会关闭这些门。

<a id="cm-literature"></a>
## 固定一手事实与旧宽比较

[16张一手入口卡及直接见证](C11_M1_LITERATURE_INTERFACES.md)记录CS8/MP69的指定版本、位置和必要调用门。
rewritten指向收紧后的事实页，不等于旧宽paper-facts验收；摘要仅核主题，
历史“已读/已搜索/已独立审计”不由本次新访问追认。
LPQ/LP特殊二阶目标与实际 \(\Theta_2\) 有自足反例区别，未冒称外部定理反例；
端点收缩不定位内部前缀也有完整两常值映射见证。
旧PROVED打包标签按当前PA-WHOLE/POWER/CYCLES的明确前件替换。
GAO/DTT/TT正文、若干刊本和精确式、具体应用和原生证书继续逐项deferred。
公开问题段落只证明该固定历史版本提出过问题，不证明现在全球无人解决。

<a id="cm-verification"></a>
## 验证能证明什么

机器检查逐表13字段、稳定ID、真实source_locator、原件hash及LF总行数、
覆盖范围并集、状态、规范锚和deferred义务。它只认证枚举与记录完整性，不认证数学真值。
原件字节、来源清单和附件没有更改；没有补造缺失原证明。
全库429个来源位置、346个字节内容的穷尽语义枚举仍未完成，不能按本批记录数推算清洗率。
