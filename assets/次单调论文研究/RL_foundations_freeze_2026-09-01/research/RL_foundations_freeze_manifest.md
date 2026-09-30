# RL 基础理论冻结清单

冻结日期：2026-09-01  
冻结用途：作为后续 RL 定理、例证、算法与文献比较工作的固定数学基线。  
验收裁决：**ACCEPTED AS FIXED MATHEMATICAL FOUNDATION**。  
投稿状态：**NOT READY AS A SUBMISSION MANUSCRIPT**。

## 1. 权威文件

| 角色 | 文件 | SHA-256 |
|---|---|---|
| 固定数学基础稿 | `research/RL_foundations.md` | `0adf8ca1593148bebce576e9659f3da50e61a77880c0b311cbcc35d0dcbb4ebd` |
| 冻结数学源 | `work/RL_foundations_draft.md` | `e24b415afe82ba6a98bd5fd7740bc25f5026da151934cd66d7cfbd22e5924815` |
| 最终独立 proof referee | `work/rl_foundations_final_referee.md` | `2e9e05d789d0a365768281a27332819f9a7daa01c3ce9605e61bcf8779525864` |
| 最终成品级预审 | `work/rl_foundations_presubmission_review.md` | `1ba2142cf964928d2b09bde17e1e2827b6be1be327d00636e104ff600b449071` |
| 润色报告 | `work/rl_foundations_polishing_report.md` | `435bcddeb0a8d5ad63ffeaf658058acfb0c633d4d3284e5fc7bd76cf589f6be0` |
| 锁定内容账本 | `work/rl_foundations_locked_content_ledger.yaml` | `d6b92ec251c5d71e9284b493363f03e7856429100d7c7de368ed0655ee41b016` |
| claim-safe prior-art matrix | `work/rl_foundations_structure_claim_safe_matrix.md` | `ac2ed090bd4f7adad9b081a72ef7cc0c3ad278dc2b59597870bbf75332f4384e` |
| 集成报告 | `work/rl_foundations_integration_report.md` | `a65a86ae664cfac80009093fedad0086347021e814bc8008ae0eb30b31a27f09` |

## 2. 数学验收证据

- 30 个编号对象逐项独立重证：`30 PASS / 0 REPAIR / 0 FAIL`。
- 7 个定理均保留完整证明。
- 125 个 equation tags 完整、无重复、无缺失引用。
- 润色前后 711 个数学片段逐项同序一致；数学片段序列 SHA-256 均为 `cf896959aae5cdcead9d75989e45f8a3efcb7f718d2fffa33f3eacd0a10f5245`。
- 量词、自然域、常数、指数、branch scope、GX-071--GX-073 判决和 claim strength 均已锁定。
- 最终预审未发现固定基线用途的 `BLOCKER`、`MAJOR` 或 `MODERATE` 问题。

这里的“验收”是指：在当前明示假设、定义域、量词与版本哈希下，全部已列定理和证明通过本轮多重独立复核。它不是对未来改写、未列推广或外部文献新颖性的无限保证。

## 3. 已冻结的理论边界

1. RL 的 all-pairs 条件与其内积式、自然 Minty 域上的 reflected-resolvent modulus 精确等价。
2. `gamma=1` 是 tied semimonotonicity / Lipschitz-reflector 参数切片，不作为新概念声称。
3. all-pairs RL 只提供 restricted Minty injectivity；coverage、exclusion 与 branch invariance 必须分开。
4. 局部 PPA 主定理是 named-branch / anchored 结构；不得升级为任意 full-resolvent selection 的收敛。
5. 在 `0<gamma<1, L>0` 的幂型组合中，`gamma q` 是条件性 upper order；退化端点 `L=0` 的 phase 是 `q`。
6. isolated-zero 的 `q`-flatness 与 nonisolated 的 alignment/drift 机制分开；后者的精确组合为条件性 `theta q`，不能由 all-pairs `gamma` 自动替代。
7. upper order、two-sided exact exponent 与 positive exact Q-factor 是三个不同层级。
8. GX-071 只证 attainability，GX-072 只证 all-pairs exponent 可能保守，GX-073 只证 one-step scale 不等于 convergence order。
9. 当前材料不证明普适 monotonicity--regularity 跷跷板。

## 4. 不属于本次冻结的事项

- RL 的正式公开名称。
- 文献优先权、概念新颖性与投稿级贡献定位。
- Wang--Li--Ng 2023、Moursi--Vanderwerff 2025、Luque 1984 的最终 theorem-level 全文重叠核验。
- sufficient constants 的 necessity 或 optimality。
- application-derived natural exact `theta q` witness。
- 完整投稿稿的引言、related work、正文引文、参考文献与期刊格式。

## 5. 版本规则

- 后续工作引用本基线时，应同时引用文件名与 SHA-256。
- 纯排版或语言改动若改变文件哈希，也必须登记新版本。
- 任何改变定义、假设、量词、常数、指数、证明或结论的修改，均不得覆盖此版本；应另开版本并重新经过 bounded proof review。
- 后续 atlas、examples、algorithm 或投稿分支可以引用本基线，但不得反向静默改写本基线。

## 6. 冻结包内容

冻结压缩包应至少包含：固定基础稿、冻结数学源、最终 proof referee、成品级预审、润色报告、锁定账本、结构/先例审计、集成报告以及项目状态文件。压缩包自身的 SHA-256 在生成后单独登记。
