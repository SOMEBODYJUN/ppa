# 来源谱系与规范节点定位

这里的 S 键只解决“哪个版本、哪个位置支持哪种叙述”。数学身份及状态写在模块和 [CLAIMS.md](../CLAIMS.md)。原件仍保留在 history/sources/ 作审计依据；它们不因被收录而成为 canonical truth。[INGEST_MANIFEST.tsv](../INGEST_MANIFEST.tsv) 给出逐文件校验和。下列路径均从仓库根起算，链接指向可追溯原件。

| 键 | 精确仓库路径与内容 | 何时读、对应节点 |
| --- | --- | --- |
| S14H | [history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/00_从这里开始/资产关系数据.json](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/00_从这里开始/资产关系数据.json) 与同目录 研究资产统一超边知识图_v2.html、解释图执行契约_v2.json | 历史语义图：149 entities、35 hyperedges、101 assets 元数据。当前仓库保留原 101 文件中的 100 个展开件；受限的 Frankowska 1989 第三方 PDF 未入库。其边是重建搜索种子，不自动证明新版本。 |
| S14R | [history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/01_论文主稿/RL与广义次正则_当前论文源.tex](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/01_论文主稿/RL与广义次正则_当前论文源.tex) 与该树的 02_核心推导、04_证明审计 | 固定锚／沿轨道／全对条件的早期区分、T4/T5 审计与反例；遇到旧结论与 S19 不一致时先核具体量词和版本。 |
| S14C | [history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/02_锥优化_CRSC_MSCQ/02_可编译源文件/main.tex](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/02_锥优化_CRSC_MSCQ/02_可编译源文件/main.tex) 与同树 03_核心证明审计、04_边界反例与优先权、05_验证程序 | 冻结最小面 CRSC/MSCQ 的证明、耦合 SOC–PSD 和非 amenable 边界；研究锥命题时读原证明和代码，避免把 MSCQ 自动接成 RL 残差。 |
| S14M | [history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/](../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/) | 有限状态精确零集与 EB、惰性四循环、无限状态障碍、相关性和条件残差修复；分别核 proof/audit/verification，不能由有限状态推出一般状态。 |
| S18 | [history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip](../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip) 内 sections/theorem_spine.tex 等 | 早期投稿骨架；C02 的原位置。需要比对 9/19 新增模、Dini、回缩与验证器时解包阅读，不能把两个稿件视为同版。 |
| S19 | [history/sources/次单调论文研究/RLEB_投稿扩展版_完整源码_2026-09-19.zip](../history/sources/次单调论文研究/RLEB_投稿扩展版_完整源码_2026-09-19.zip) 内 sections/theorem_spine.tex、extensions_moduli_structure.tex、verification_example.tex、appendix_signed_schur.tex | R01–R04 与 Dini/对数接缝/回缩的完整 9/19 源码。随机 corollary 的指定度量完备性异议以此版为准；后续不能把它暗中写成 S18 已有。 |
| S20 | [history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md](../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md)、[06_math_audit.md](../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md)、02_NEUTRAL_PPA_SYSTEM/ppa_system_team/10_final_blueprint.md、03_CLASSIFICATION_STAGE/ppa_classification_team/07_stage_synthesis.md | 参数中立对象空间问题、完整 \(F\) 与局部 T 的信息边界、紧 T-only 的 \(\Phi\)、LT 嵌入及受限分离。研究规模比较时还须逐读这几个文件所索引的小审计文件。 |
| S21 | [history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md](../history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md)、[03_NO_GO_LEDGER.md](../history/sources/提纯总账_2026-09-21_v0.9/03_NO_GO_LEDGER.md)、[05_INTERNAL_INDEX.md](../history/sources/提纯总账_2026-09-21_v0.9/05_INTERNAL_INDEX.md)、[08_SOURCE_AND_CLAIM_POLICY.md](../history/sources/提纯总账_2026-09-21_v0.9/08_SOURCE_AND_CLAIM_POLICY.md) | N05/N08/N10 等量尺塌缩的**历史总账报告**。I-001/002/003–005/059/075 的原包或展开件现已恢复，I-097–099/I-102 仍未见原件名；恢复来源不等于重构孔隙证明。 |
| S23 | [history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex](../history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 与同目录匹配的 21 页 PDF 和中文讲稿 | 全图全尺度 Hölder–RL 的影子、有限维纤维分类、§5 锐值域定位、§6 有限样本 QP/覆盖/信息障碍、§7 deadband；以 TeX 标签定位原证明，中文讲稿用于理解，不替代证明。当前轮附同名 TeX/PDF 可独立比对。 |
| S25 | [history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf](../history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf) §8 Theorem 8.1，印刷页 20–22 | 较 S23 新增的有限 proximal 数据拓扑值域候选，指定 \(T\) 可为子关系；只有 PDF。[6, Theorem 6.2 的适用门](LITERATURE.md#lit-grn-2002)已逐项核；[C70](canonical/finite_sample_collar.md) 与 [C05-v2](canonical/local_range_without_supercriticality.md) 分别重算度量层和条件拓扑链。原生模型的整窗假设、Čech 同调约定的精确导入与新颖性仍另审。 |
| SS0/SS1/SS2 | [history/sources/次单调论文研究/正式后的研究/research_note.md](../history/sources/次单调论文研究/正式后的研究/research_note.md)、[solution_selection_revised_v1_delivery.zip](../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip)、[solution_selection_final_audit.md](../history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_final_audit.md) | 先读修订包 SOURCE_MAP、revision_math_closure 和 final audit，再用原稿追源；局部／完整接口漏洞与明确反例不可遗漏。 |

## 版本与文件使用准则

1. 历史超边图是本次重构的**输入证据**，不是当前图的自动权威。其具体边在 [HYPERGRAPH.md](HYPERGRAPH.md) 重新命名、补齐或降级；新边必须有精确来源。
2. 嵌套 ZIP 中的 TeX、MD、审计、代码可通过压缩包成员名定位；没有把相似 PDF/TeX 的页码当同一版本，也没有将受限制外部论文原文复制进仓库。
3. 计算验证需回到原脚本、参数和输出；来源中声称 PASS、已证、全球首创之处在本地图中只按实际证据层叙述。
4. 全量逐项来源校验仍用 [INGEST_MANIFEST.tsv](../INGEST_MANIFEST.tsv)；本页按数学节点选读，不以原文件树替代研究地图。

## 9/21 历史缺件与本轮恢复

| 内部 ID | 当前确切位置 | 证据身份 |
| --- | --- | --- |
| I-001 | S14H 所在 9/14 展开树；同树 00_从这里开始/manifest.json | 100/101 项历史证明语料。缺第三方 PDF，不能称原 ZIP 完整恢复。 |
| I-002 | S18 ZIP 的 sections/theorem_spine.tex | 9/18 局部 RLEB 源，附内部审校；全局完整 \(J_F\) 一致性仍独立。 |
| I-003/I-004 | [旧 selection ZIP](../history/sources/次单调论文研究/正式后的研究/RLEB_solution_selection_2026-09-18.zip) 与 SS0 Markdown | 原稿二者同字节；一般局部→完整推论有错误。 |
| I-005 | [Codex_independent_audit.md](../history/sources/次单调论文研究/正式后的研究/Codex_independent_audit.md) | 标题和内容是审计**任务书**，只证明检查要求曾被提出，不能作审计通过证据。 |
| I-059 | SS1 修订 ZIP 中 research_note.md、revision_math_audit.md、revision_math_closure.md | 修补版本和内部数学关闭证据；优先权 U1–U3 未关闭。 |
| I-075 | S20 9/20 已展开专题包、FILE_REGISTER.json 和 PROVENANCE.md | 73 文件内容已恢复；重复原 ZIP 未保留。 |
| I-097–099/I-102 | 当前逐项盘点未找到相应原孔隙审计／正式表示稿 | N10 等暂保持历史报告，待原文或独立重构。 |
