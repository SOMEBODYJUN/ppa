# PPA 研究资产的增长协议

本仓库以数学对象、精确定义和可追查的命题为正文。`history/sources/` 保存原始材料，不能替代正文，也不因被收录而获得可信状态。新研究可从文献、计算、反例或新证明直接产生；历史来源只是其中一种输入。README 是地图，不是证明。

## 新工作放在哪里

| 新资产 | 位置与进入条件 |
| --- | --- |
| 精确定义与约定 | `research/foundations.md` 或 `research/canonical/<topic>.md`。标明空间、参数、局部/全局及依赖；冲突约定并存且各自命名。 |
| 定理、引理、猜想、反例、桥 | 主题模块 `research/*.md` 或 `research/canonical/*.md` 的独立锚点；精确身份另登 `CLAIMS.md`，图中只为真正承重的关系建节点/边。 |
| 独立证明、攻击与义务 | 同一主题模块相邻章节；未闭 obligation 放 `RESEARCH_STATE.md`，失败机制进入 `FAILED_ROUTES.md`。不得以评分或审稿意见代替推理。 |
| 可复现计算 | 新代码放 `research/code/<topic>/`，记录运行命令、环境、参数、seed、精度、误差和输出。[代码登记](research/CODE_REGISTER.md)映射旧验证器与 Claim；历史代码原样留在 `history/sources/`，其执行不自动验证一般命题。 |
| 文献事实 | `research/LITERATURE.md`，给确切版本、定理/页码和假设；解释、猜想与先行性判断另标层级。未读原文时不能写成 paper fact。 |
| 来源追溯和覆盖 | `research/SOURCES.md` 给版本定位；`research/audit/` 给尚未裁决的逐项来源、ZIP 成员和重复关系。原件移入 `history/sources/`，哈希与初始清单保持一致。 |

当前主题模块可继续扩写，只有新对象或一条可独立使用的证明链才新建文件；不要把每轮聊天、审稿标签和重复稿复制进正文。

## 单个 Claim 的身份卡

每个有价值的新 Claim 先写以下字段，缺项写“未定”并保持候选状态：

1. **ID 与版本**：稳定编号；定义域、量词、假设、结论、范围任一改变即新版本，旧版及反例保留。
2. **Exact Statement**：对象/空间、每个自由参数的范围、量词顺序、全图或图块、同一尺度/同一零集、前提和结论。若是条件合取，列出所有输入与额外 side condition。
3. **Definitions / Dependencies**：所用定义版、已用 Claim 版、引用定理的确切适用条件；区分必要、充分、等价、特例、限制、反驳、开放目标。图边必须与文字一致。
4. **Evidence**：逐行证明或定位、可复现计算记录、文献确切位置；每项标明 paper fact、interpretation、hypothesis、observation 或本仓库推导。有限搜索和工具失败均不产生一般真值。
5. **Counterevidence / Objections**：最危险的退化例、量词攻击、遗漏的定理前提，以及是否 fatal。一个未解决的 fatal objection 阻止可靠状态。
6. **Status / Scope / Related files**：见下表；指出正文锚点、历史证据精确路径或 ZIP 成员、代码、反例和未闭义务。

| 状态 | 准入意义 |
| --- | --- |
| `source-report` | 来源文件如此报告；尚未独立重构证明。 |
| `candidate` | 语句固定，有证明草案或推理，但存在待核条件/反驳。 |
| `derived-checked` | 已独立重构关键推导，逐条核假设与边界；记录审查范围和未核外部调用。 |
| `refuted` | 精确版本有反例或逻辑否定；只为修正版本另立新身份。 |
| `open` | 精确问题与尚缺义务；正面有限搜索不能提升状态。 |
| `canonical` | 论证及全部承重引用已核、现存 fatal objection 已关闭；这只说内部可信，不说新颖或已同行评审。 |

`Truth`、`Value`、`Novelty`、`Mechanism`、`Ambition` 分开判断。一个真引理可价值有限；一个重要猜想仍是未证。所谓“内部审计通过”仅是 evidence 的来源与范围。

## 每次进展的路径

1. 固定 Claim 版本与现有图关系；选择最有信息量的 proof obligation，检查对象良定、隐藏假设、量词顺序、退化情形、外部定理的所有适用条件。
2. 从原件重写数学内容，或直接写新的推导。把公式和证明放进可读主题模块，来源位置仅用于追溯。对失败路线诚实提取仍成立的引理、反例和障碍，记录具体断点与重启条件。
3. 更新 `CLAIMS.md`、必要的 `FAILED_ROUTES.md`、`RESEARCH_STATE.md`，再更新 `research/graph.json` 与生成图。README 的数学导航和 File Map 随真实依赖改变，不按日期堆新索引。
4. 运行 `python3 research/build_graph.py`、`python3 research/validate_assets.py`，核新代码复现命令。机器检查只能发现链接/身份/哈希/结构错误，不能替代证明。
5. 对每一批有价值成果建立 `git add`、`commit`、`push` checkpoint 并核对远端。未获得真正认识进展时更新明确障碍即可，不制造新的证明文件。

## 图的逻辑约定

`graph.json` 的 `inputs` 是**合取**，不是一组可分别引用的前提；`relation` 和 `scope` 限定边的语义。`implies` 只在同一对象和整套 side conditions 下使用；`conditional` 必须在 scope 中明列额外前提；`limits/refutes` 不可反向读取成蕴含；`open` 是要证明的目标。缺少正式化的量词和例外时，先写文字契约并保持候选，不用图形外观掩盖逻辑缺口。

历史工作保留可复核性，未来研究从上述正文与 Claim 入口继续生长。新方法和未列出的路线始终可以进入；图是当前知识，不是研究方法白名单。
