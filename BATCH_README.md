# 初始化分批阅读与来源纪律

**时间与用途范围：本页只记录初始导入的来源组织和当时阅读范围。** 下表的“本次／本轮”、待核条件与未运行记录属于初始化时点，不能作为当前 Claim 状态或后续工作的指令。当前定义、独立证明与证据边界以 [README](README.md)、[RESEARCH_STATE](RESEARCH_STATE.md)、[CLAIMS](CLAIMS.md) 及规范正文为准；已经重构的命题不要求回历史原稿补定义或证明。

本次以用户上传的一个外层 ZIP 为唯一原始文件输入；四个独立附件是 ZIP `最新成果/` 四件的**逐字节重复**，已比 SHA-256，没有重复入库。ZIP 有 183 个目录／文件条目、158 个实文件，展开约 37.1 MB。读取方式是：先完整枚举目录和嵌套 ZIP，按目录读各批的 README、状态、摘要、定理目录和承重陈述，再对关键论证及冲突版本逐段核查。没有逐页独立审稿所有 158 件、所有嵌套 PDF 或全部外部文献。下表限定本次实际核查的范围。

| 批次 | 已读入口／关键部分 | 初始化认知及后续审查 |
| --- | --- | --- |
| 总目录早期 RL | `RL_foundations.md` 定义 0.1–0.4 和摘要；`RL_Submonotonicity初稿.md` 目录；`01-RL_PPA_T5_core_manuscript_2026-09-07.md` 章目录；`theory_atlas.md` 证据标签；交接和高野心组合稿开篇 | all-pairs、anchored、full/restricted、coverage／留域须区分；9/07–9/10 的研究判断属于历史版本，不能压过 9/20–9/25 的精确修订。完整主定理须回原稿。 |
| 总目录相邻主线 | `ATTACK_PRODUCT_CONE_CRSC_MSCQ.md` 设定和结果；`MARKOV_PAPER_THEOREM_PACKAGE.md` claim ledger；随机多值攻击及 SO-07/M2/M3 的结构目录；四个 docx 开篇 | 锥与 Markov 是独立论文候选；随机多值旗舰、退化预条件 coverage 都有单独边界。有限先行性审计不等于全球新颖性。 |
| 9/14 历史总包与 9/18 RLEB 投稿包 | 9/14 内部导航／类型清单；9/18 ZIP 的 `README_投稿包说明.md`、`数学语义核对与剩余问题.md`、`sections/theorem_spine.tex` 的定义、A1–A4、收敛定理和证明骨架 | C02 的精确局部条件以 9/18 原稿为准；9/14 对研究谱系有用而非其全面替身。9/14 某第三方论文 PDF 不复制到仓库。 |
| 分类集研究 9/20 | `README.md`、`00_START_HERE/QUICK_HANDOFF.md`、`READING_ROUTES.md`、`STATUS.md`、`OPEN_PROBLEM.md`、`04_AUDITS_AND_PRIOR_ART/CLAIM_BOUNDARY_REGISTER.md`、`ASSET_SCOPE_AUDIT.md`，并读 `07_final_handoff.md` 的对象和问题、`06_math_audit.md` 的结论／\(\Phi\) 证明及中立 `10_final_blueprint.md` 开篇 | 固定紧 T-only 的 \(\Phi\) proper 已内部复核，但保纲和全图提升未闭。包内 `FILE_INDEX` 的 CANONICAL/HISTORICAL/SUPERSEDED 标签继续有效；不是新的全证明复审。 |
| 9/21 提纯包 | `README`、`01_CURRENT_MAP`、`02_VERIFIED_CORE`、`03_NO_GO_LEDGER`、`04_OPEN_GATES`、`07_NEXT_SYSTEM_BRIEF` | 在 9/20 之后报告 Baire／多孔性等正式负路线；自称 v0.9，V-B 和 SOURCE-MISSING 表示部分原证明未随该包出现，不得升级。 |
| 最新成果 9/23 与 9/25 | 对四件逐字节校验；读 9/23 TeX 的定义、图坐标、shadow、有限维几何、精确纤维、覆盖定理；PDF 摘要／目录；9/25 PDF §8 全部定理与证明及讨论 | 9/23 是 21 页可编辑源码主稿；9/25 是 24 页 PDF-only 合并候选，新加独立局部 Lefschetz 模块，具体适用条件待核。中文 PDF 是讲授稿，不能替代正式证明。 |
| 正式后的研究 9/18 | `research_note.md` 的定理 1、推论、显式 F 与完整 resolvent；`Codex_independent_audit.md` 的任务目录；修订 ZIP 文件清单与 9/21 对漏洞的复核总结 | 原稿的完整 resolvent 泛化有漏洞，修订包收窄一般命题；显式构造仍可保留。本轮未运行 ZIP 内数值脚本，数值结果不作为证明。 |
| 相似研究与外文 PDF | 核对两个相似研究 PDF 的首页题名、出版标识和授权标注，以及总目录若干外部论文首页 | 仅当定位资料和查重线索；未进行定理级原文比对，不作 Paper Fact 结论。外部 PDF 不进入公开仓库。 |

## 纳入与排除

`history/sources/次单调论文研究/`尽量保留原目录及用户研究稿原件；`history/sources/历史总包_2026-09-14/`将嵌套总包展开；`history/sources/提纯总账_2026-09-21_v0.9/`为方便检索而展开的小包。未导入的有带再分发限制的第三方论文、一个无法确认项目相关性的个人报告、空文件、非研究工具包及可由目录原件恢复的重复 ZIP。逐文件原因与校验值在 [INGEST_MANIFEST.tsv](INGEST_MANIFEST.tsv)。原始整个上传 ZIP 含这些材料，故只存 [整体 SHA-256](UPLOADED_ARCHIVE.sha256)，未推到仓库。没有篡改入库原研究文本；本仓库根目录的状态文件是新的导航记录。

若以后增加外文事实，先在确切版本和页码处核对原文；若把旧 V-B 升级成 canonical proof，先取回对应原证明文件或独立重构。图片、PDF、脚本的存在本身不代表实验已复现或证明已审定。
