# 原始证据区

`sources/` 保留初次导入的目录、文件和字节。它包括草稿、重复版本、审计任务、压缩包和验证脚本；名称中的“终稿”“通过”或“定理”不授予规范地位。规范数学正文从根 [README](../README.md) 进入。

- [初始文件清单](../INGEST_MANIFEST.tsv) 记录来源路径、大小、SHA-256、纳入或省略原因，以及本区精确路径。
- 初始清单覆盖 240 个导入条目；本区另有 9/21 提纯总账的 11 个展开文件。完整 251 文件的逐字节审计见 [来源文件清单](../research/audit/SOURCE_FILE_INVENTORY.tsv)，178 个 ZIP 成员另见[成员清单](../research/audit/ZIP_MEMBER_INVENTORY.tsv)。
- [来源谱系](../research/SOURCES.md) 按版本与数学位置定位重要原稿；[重构覆盖审计](../research/audit/SOURCE_RECONSTRUCTION_AUDIT.md) 区分已读取、已重写、待裁决。
- 历史验证程序原样留在 `sources/`；新的复现代码进入 `research/code/`。运行成功只证明本次有限程序可执行，不证明一般命题。

需要引用这里的材料时，给出精确文件或 ZIP 成员与节/页/标签、版本、证据层，接着在规范模块独立陈述对象和结论。修订数学命题时不修改原件；另立 Claim 版本并解释差异。
