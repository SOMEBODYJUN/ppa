# 基础稿、解选择成果与原始输入

这些源包原样保留，以便团队离开当前工作区仍能复核调用接口。没有把全部旧旁支展开成多个“最终稿”。

## 先用哪份

| 文件 | 角色 | 应怎样阅读 |
| --- | --- | --- |
| [RLEB_PPA_submission_assets_2026-09-18.zip](source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip) | 本次实际调用的 RLEB 基础投稿稿，含 PDF、分章 TeX、文献与锁定台账 | 先查 `sections/theorem_spine.tex` 的实际接口；原稿按既有基础使用，不重审无关内容 |
| [solution_selection_revised_v1_delivery.zip](solution_selection_revised_v1_delivery.zip) | 已修订 solution-selection 研究稿及复现/关闭记录 | 解包后先读 `research_note.md`、`revision_math_closure.md`、`revision_priority_closure.md`、`final_package_QA.md`；再读 PDF/源代码 |
| [solution_selection_final_audit.md](solution_selection_final_audit.md) | 修订前新稿的最终审计、精确问题与先例边界 | `ABC_PASS_AFTER_REPAIR` 不是原稿无条件通过；后续修订包的 closure 决定修订后状态 |
| [RL_generalized_subregularity_assets_2026-09-14_v2.zip](source_inputs/RL_generalized_subregularity_assets_2026-09-14_v2.zip) | RL＋锥＋Markov 的历史总资产及离线超边导航 | 追溯来源和旁支时读；不作为当前 PPA 比较接口的优先基础稿 |

9/14 与 9/18 包内容不同，后者不全面替代前者。原上传 ZIP 的哈希和工作区文件名见 [PROVENANCE](../PROVENANCE.md)。

## 修订稿的冻结身份

solution-selection 交付 ZIP 的 SHA256：

`cae4a31c80b5c29c21af3444a66e6a4de007cfac24db21ffd5a5f261fbb037f6`

包内内容权威为 `research_note.md`，TeX/PDF 为同源呈现。独立范围审查核对的冻结值：

| 包内文件 | SHA256 |
| --- | --- |
| `research_note.md` | `91ad4b0948a21443fc557b5ea579e692650399504e735223d72347ba86bea1b8` |
| `solution_selection_revised.tex` | `b0c750a8235ecfe2c1959f5b6da37bc2b539afe0f7ace618c26243ea33ee2a56` |
| `output/pdf/solution_selection_revised.pdf` | `0bd11b6c3e8c246842151a0190928b0bc02c3f1662405d0d0771c4687d418c03` |

`REVISION_MATH_PASS`、`REVISION_CLAIMS_PASS` 与 `PACKAGE_QA_PASS` 分别对应数学范围、宣告范围和文件构建，不共同构成全球首创证明；U1–U3 等未决优先权事项仍应按原记录保留。

## 为什么不重复展开

当前主包聚焦算子空间比较与交接。三个子 ZIP 原样纳入，保留其内部源、PDF、审计与构建关系；需要研究相应稿件时再解压一次，避免同名 `research_note.md` 和不同轮次审计相互混淆。没有删除或修改任何工作区原件。
