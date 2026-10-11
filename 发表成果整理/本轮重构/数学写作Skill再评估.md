# 数学写作 Skill 再评估

核验日期：2026-10-11。任务是寻找能支持自然数学叙事、例子选择、双语 LaTeX、证明审查和审稿的单一主 Skill。此次只写评估，不安装候选，不改主稿或现有 Skill。

## 判断

保留仓库内唯一的 `$academic-writing-skills`，在其数学模式中补入一个短的数学行文与例子选择指南。现有版本已经带有完整图/图块、完整纤维、真实残差、局部化和指数的保护规则，也具备中英写作、审稿与 LaTeX 工作模式。新装第二个写作 Skill 会重叠触发和重复约束，不能自动解决数学品味。

此次找到的 **JiahaoLi-creator/mathematical-academic-writing** 是最值得考虑的单独替换候选。它明确面向 Codex 和 theorem-proof 写作，并将作者声音解释为数学对象、证明路线和材料取舍的稳定选择；要求从具体问题引入概念，以关键归约开始证明，例子按对象、计算、后果展开，删除无功能的防御式说明。它比通用写作流程更贴近本次诉求。不过，公开发行未提供完整行为回归和来源语料；目前不能把作者的测试报告当成独立复现的质量保证。此轮保留已验证的主 Skill，采用自己写出的简短领域规则，风险和迁移成本更小。

## 候选对比

下表入口行数由 Python 读取真实 UTF-8 文件计算，并反算核对文件字节数及逐行重建；入口长短只反映指令负担，不能作为质量得分。日期是当前 HEAD 的提交日期，不能单独证明持续维护水平。

| 项目 | 真实入口行数；HEAD 提交日期 | 数学写作与语言覆盖 | Codex 与依赖 | 本次判断 |
|---|---|---|---|---|
| WenyuChiou/academic-writing-skills | 上游入口 243；2026-10-08 | 结构、证据、自然学术 prose、审稿、跨稿同步完整；本仓库已经添加双语与数学审查模式 | 开放 Skill 格式；本地按需参考和 Python 审核脚本；排版仍依赖现有 TeX 引擎；MIT | 保留。大型通用规则需按数学任务裁剪，内部验收记录不能进入正文 |
| JiahaoLi-creator/mathematical-academic-writing | 220；2026-09-01 | 明确 theorem-proof、数学分析、优化；语义保护、反防御叙事、作者声音和文体区分较好；有双语说明，但中文标点及专门中英翻译规范不如现主 Skill 明确 | Codex 元数据与开放格式；公开核心校验用 Python 标准库；来源语料和完整行为验收为私有；MIT | 最强替换备选，暂不安装。若以后替换，应迁移 RLEB 领域规则并重跑实际任务测试 |
| VeryMath/AI4Math-Writing | paper-writing 入口 105；2026-09-10 | 数学证明义务、符号、公式和 LaTeX 模块完整；中英说明，支持请求指定语言；重点是证据与证明覆盖，个人数学行文规则较少 | 按需调用六个嵌套参考模块，没有要求每次全跑；LaTeX 编译依赖引擎；MIT | 适合证据整理和证明审查；不足以因本次 taste 问题替换现主 Skill |
| abinzzz/mathlatex-skill | 51；2026-09-10 | 逐步推导、说明克制、公式编号；默认英文数学解答和中文沟通，可覆盖默认语言；更接近作业及短证明 | Codex 元数据，无 API key；生成 PDF 需要 TeX；当前 checkout 未见 LICENSE | 覆盖不足，不安装。固定 Eq. 引用和对齐形式属于作者个人偏好，不宜强加本稿 |
| Brandon030722/academic-writing-skill | 129；2026-07-29 | 明确中英翻译、LaTeX、审稿、润色；主要写作范例来自 Nature 的 AI/计算研究，证明依赖检查没有专项规则 | Codex 元数据；主要是 Markdown 参考规则；当前 checkout 未见 LICENSE | 双语完整，但不是本稿最需要的数学叙事和证明技术专用方案 |

所有候选的规则本身均不要求外部服务或 API key。没有 LICENSE 的项目可作为已公开网页的考察对象，但不能据此推定可复制再发布其内容；本次没有复制它们到安装目录。

## 真实版本和文件

本次先用 GitHub 搜索核实候选，再用 `git ls-remote` 获取 HEAD，拉取仓库，完整阅读下列真实入口。Python 再核对 checkout SHA 与查询结果一致、frontmatter 存在、入口中的显式相对 Markdown 链接可解析。

- WenyuChiou：`edc5ede61a7900ae51a9959ad35a5fffab296c66`，[skills/academic-writing-skills/SKILL.md](https://github.com/WenyuChiou/academic-writing-skills/blob/edc5ede61a7900ae51a9959ad35a5fffab296c66/skills/academic-writing-skills/SKILL.md)。另读本地已安装的 `references/mathematics.md`、`references/prose-and-citation-editing.md` 和 `references/upstream.md`。
- JiahaoLi：`db948c44a5015f8ba2fd1950b949b850d6ab6465`，[SKILL.md](https://github.com/JiahaoLi-creator/mathematical-academic-writing/blob/db948c44a5015f8ba2fd1950b949b850d6ab6465/SKILL.md)。承重参考为 `references/genre_profiles.md`、`research_article_workflows.md`、`mathematical_integrity.md`、`anti_defensive_audit.md`、`artifact_verification.md`、`corpus_manifest.md`、`MAINTENANCE.md` 和 `provenance/public-release.v1.json`。
- VeryMath：`418eb2e0c9cad7f259d114d7acfe6043971f4b94`，[skills/paper-writing/SKILL.md](https://github.com/VeryMath/AI4Math-Writing/blob/418eb2e0c9cad7f259d114d7acfe6043971f4b94/skills/paper-writing/SKILL.md)。另读包内 README、`skills/registry.yaml` 及结构、证明义务、公式、LaTeX 模块。
- abinzzz：`e35ad802e5354cfa55ecb9447c01dbd692c4d228`，[SKILL.md](https://github.com/abinzzz/mathlatex-skill/blob/e35ad802e5354cfa55ecb9447c01dbd692c4d228/SKILL.md)。另查中英 README、Codex 元数据和目录。
- Brandon030722：`531fde1aff669eb6c8cd7ede0d2fe044ef24d339`，[academic-writing/SKILL.md](https://github.com/Brandon030722/academic-writing-skill/blob/531fde1aff669eb6c8cd7ede0d2fe044ef24d339/academic-writing/SKILL.md)。另读 `references/core-writing-standard.md`、`references/top-journal-patterns.md`、README 和 Codex 元数据。

## 核验结果与边界

- Wenyu 上游：在现有测试环境运行 `python -B -m pytest tests -q -p no:cacheprovider`，125 项通过。又用 Python 启动 `--collect-only`，逐项计数核对为 125。主要覆盖规则结构、审核工具和可移植包完整性，不能据此证明每次输出都有数学品味。
- JiahaoLi：运行 `python3 -B scripts/verify_public_core.py`，公开绑定核验通过，核对了 16 个核心文件及显式内部链接。`tests/` 中 JSON 是 `notice_only`，不是可执行的公开行为测试；原文明确说明完整私有测试、语料和盲测不在发行包内。公开校验只能证明发行内容和绑定一致。
- VeryMath：`python3 -B -m unittest discover -s tests -v` 的 7 项通过，但全部属于 math-beamer，不能用于宣称 paper-writing 行为通过。
- 其余两个候选：入口和文件阅读完成；未发现公开测试套件，此轮未做候选安装和新会话行为测试。
- 所有五个上游入口的显式相对 Markdown 链接存在。该检查不涵盖代码字体中的路径、外部 URL 的内容真实性或抽象写作质量。

因此本报告的结论是源码和依赖评估，不是“五个 Skill 实际写作能力均验证通过”。现有主 Skill 的实际调用验证由本轮主任务另行记录。

## 建议写入现主 Skill 的短规则

以下为针对本稿写出的领域规则，不复制候选作者的特定句子或格式偏好。宜作为一个按需参考文件，由现主 Skill 的数学写作模式读取；不建立新 Skill，不要求所有任务加载。

1. **先让读者认出问题。** 从已有数学对象、算法和要证明的性质开始；概念确有反复使用的作用时再命名。为收敛论文先呈现标准接口：轨道为柯西列，且到闭不动点集的距离趋零，于是收敛到该集合中的一点。再解释反射估计和误差界如何供给这两项性质。
2. **引言按问题组织文献。** 将已有工作分为真实解决不同问题的路线，写清各路线的结论和所需条件，再引出本稿要放宽或连接的那一项。不要逐篇排队复述，不声称有限检索覆盖整个方向。摘要集中陈述对象、结果和必要范围；方向综述放引言。
3. **让证明显露关键想法。** 先写关键恒等式、归约或构造，解释承重的一步；读者可直接补出的代数合并书写。保留量词、存在性、残差和局部化的承重步骤，不把它们当冗余删掉。
4. **例子先说它解决哪个疑问。** 优先取自常见函数、几何对象或算法模型；只有构造必要时才使用专门拼接模型。正文给对象、核心计算和明确后果，重复估计及最优常数放附录。一个例子承担一个主要数学任务。
5. **搜索例子时先冻结目标。** 列出必须保住的性质、允许改变的贡献和退化情形。分别检查自然性、计算透明度、一般性及对主定理的解释力，不以“显式”或随机检验成功代替这些判断。
6. **保持数学力度。** 更舒服的单调/Lipschitz 例子未必能替代非 Lipschitz 例子；更深刻的拓扑例子未必展示同一适用范围。替换必须比较精确属性；若贡献改变，同步修改摘要、引言和结论。
7. **保留作者的取舍和节奏。** 让段落长度随数学内容变化；用稳定术语和直接动词。删除重复预告、再总结、泛泛的重要性和内部验收语言。必要的失败逆命题、反例和条件界限就近保留一次。
8. **验收具体文本。** 将改稿与定理条件和邻段逐项核对，模拟正常数学讲述；读者应能指出每段增加了什么信息。排版改动编译并检查成品，验证记录放报告，不放论文正文。

这些规则可以帮助模型持续作出更好的数学写作选择；不存在一个仅凭名称或安装就能保证作者 taste 的 Skill。作者给出的成熟范文、明确的对象选择和经过核实的数学内容，仍是行文判断的依据。
