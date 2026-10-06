# 当前来源覆盖快照

由 `python research/audit/build_occurrence_index.py` 从来源索引、精确范围登记与逐单元去向生成。机器只汇总已经声明的枚举范围，不审查断言真假、枚举是否充分或文献先行性；[验证器](../validate_assets.py)另核哈希、逐LF覆盖与去向双向一致。

## 固定字节分母

251 个物理文件 + 178 个ZIP成员 = 429 个出现位置，共 346 个不同字节内容组；容器、字体等支持资产也在其中。

| 内容组的枚举状态 | 组数 | 精确含义 |
| --- | ---: | --- |
| 全LF已有登记去向 | 3 | 同字节全部行被已登记范围的并集覆盖；可仍有deferred、source-report、候选或开放义务 |
| 部分LF已有登记去向 | 2 | 尚有未逐断言枚举的行；不能用选定章节推整稿完成 |
| 尚无登记逐断言范围 | 341 | 格式提示、历史阅读、规范链接和标题分段均不能替代全内容枚举 |

## 精确登记范围

| 范围ID | 源文LF | 已声明覆盖 | 原子记录 | 剩余状态 |
| --- | ---: | --- | ---: | --- |
| GX053-065-full | 1219 | 1-1219 | 332 | explicit-deferred-evidence |
| M1-MS-section5 | 524 | 326-425 | 39 | explicit-native-fiber-and-literature-gates |
| CS8-literature-scope | 420 | 312-337 | 72 | specific-primary-source-and-native-gates |
| MP69-literature-scope | 524 | 426-524 | 162 | specific-primary-source-and-native-gates |
| SS1-full | 763 | 1-763 | 400 | explicit-deferred-comparisons |
| FOUNDATIONS-final-full | 2096 | 1-2096 | 282 | explicit-deferred-prior-art-and-optimality |

以上 6 个范围共 1287 条原子记录；范围可能属于同一字节内容，不能当独立成果或文件数。

## 逐单元去向

| 去向 | 行数 |
| --- | ---: |
| rewritten | 811 |
| superseded | 25 |
| duplicate | 118 |
| refuted | 2 |
| nonmathematical | 362 |
| deferred | 125 |

合计 1443 行；同一内容可以有章节、原子断言、版本与重复位置的多种记录。这些行数不是独立成果数，不能除以文件、字节组或节点数报告数学清洗率。

已枚举来源按相同SHA-256回连到全部出现位置，来源角色仍由原位置保留；原件与成员初始清单的 `unreviewed` 是旧文件级关闭门，当前细粒度进度以本页、[登记表](ATOMIC_SCOPE_REGISTRY.tsv)和[逐单元去向](UNIT_DISPOSITIONS.tsv)为准。尚未关闭全库语义分母，也未证明总体规模比较。
