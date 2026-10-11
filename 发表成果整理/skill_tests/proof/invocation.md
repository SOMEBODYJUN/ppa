# academic-writing-skills 实际调用记录

日期：2026-10-11。任务：只审查指定数学命题与证明，给出解析反例或完整证明，并写本目录的 review.md 与 invocation.md。

## 所选模式

**轻量模式（lightweight mode）／Theorem or proof review。** 对象是单个定理及其短证明，采用数学合约固定、逐前提核验、边界反例攻击、缺口定位及局部交付核验。没有进入全稿管理模式，也没有初始化项目状态、运行完整论文审计或调用独立代理。

## 实际读取的 Skill 与参考

| 路径 | 本次用途 |
| --- | --- |
| /workspace/scratch/15cd717a5884/ppa/.agents/skills/academic-writing-skills/SKILL.md | 选择证明审查与轻量模式；限定来源、语义变更和交付范围。 |
| /workspace/scratch/15cd717a5884/ppa/.agents/skills/academic-writing-skills/references/mathematics.md | 固定数学对象、域与量词；区分真残差与图值、相对连续性与输入覆盖；逐项解析核验反例。 |
| /workspace/scratch/15cd717a5884/ppa/.agents/skills/academic-writing-skills/references/reviewer-red-team-and-release.md | 确认有效性阻断项；给出严重性及功能完整性回顾，避免将假命题标为已证。 |
| /workspace/scratch/15cd717a5884/ppa/.agents/skills/academic-writing-skills/references/execution-and-acceptance.md | 在报告交付前检查证据次序、读者衔接、术语及明确的核验边界。 |
| /workspace/scratch/15cd717a5884/ppa/.agents/skills/academic-writing-skills/references/universal-integrity.md | 写作前检查报告段落功能；核验精确候选的结论范围、语义、符号和推理衔接。 |

数学来源仅为 /workspace/scratch/15cd717a5884/ppa/发表成果整理/skill_tests/proof/input.tex。没有读取其他既有报告、fixtures、研究文件或整个研究仓库，没有进行网络检索或引入外部论文。

## 验证范围和实际结果

1. 读取完整 input.tex，并用行号定位第 6–11 行命题及第 14 行证明。
2. 固定完整图上的全称量词、参数条件、真残差定义，以及双侧邻域包含于值域的目标。
3. 解析核验主反例的非空闭图、零点集合、全部参数条件、所有图点对不等式、定义域上每个残差误差界，以及结论失败；包含零差和端点情况。
4. 对自然输入域上的 Cayley 映射，证明单值性与 Hölder 连续性；区分相对连续和域覆盖，并核验闭图能推出的域闭性及误差界的正确使用方向。
5. 解析核验全定义域反例，穷尽 Cayley 输入对类型，确认仅加入全定义域不足以修复命题。
6. 明确提出新增双侧连续图选取的加强版本，并给出连续单射及介值定理证明；新增假设的范围在报告第 5 节显式标注，未修改 input.tex。
7. 读取并核对最终 review.md：公式符号和 Markdown 数学分隔符完整；表格内绝对值改用 \lvert、\rvert 以避免单元格分隔；核对从原命题、反例、缺口到加强版本的证据次序。
8. 复核 input.tex 的前后 SHA-256 相同；最终报告候选的 SHA-256 记录如下。

未执行 Skill 脚本、数值模拟或 LaTeX 编译；本次结论来自完整的解析核验。未请求 PDF 或版式修改，渲染、期刊要求、引用核对、作者元数据、统计和实验适配不适用。

## 精确文件与变更范围

输入（未修改）：

- 路径：/workspace/scratch/15cd717a5884/ppa/发表成果整理/skill_tests/proof/input.tex
- SHA-256：236f4ba5701ed7cc530b142666dc660cbe7f89e4d4fbc996606437a1078e124a

最终审查报告：

- 路径：/workspace/scratch/15cd717a5884/ppa/发表成果整理/skill_tests/proof/review.md
- SHA-256：2f28afae5a0620f746c2f943aa7cd9c033f90bea75be4cb476f78333a3c7b0c9

本次仅写 review.md 与 invocation.md。原命题存在 1 个已确认的 S4 数学有效性阻断项；审查报告完成，原命题尚未修复。这里没有声称整篇稿件或所有 Skill 检查通过。

