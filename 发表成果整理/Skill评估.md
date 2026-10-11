# 单入口数学学术写作 Skill 评估

检索、实际拉取和检查日期：2026-10-11。检查固定提交中的真实 SKILL.md、目录、许可证及脚本。维护日期来自GitHub API；星数不作质量证明。

| 项目 / 固定版本 | 入口复杂度 | 功能与缺口 | Codex及依赖 | 决定 |
|---|---|---|---|---|
| WenyuChiou/academic-writing-skills / edc5ede61a7900ae51a9959ad35a5fffab296c66 | 主243行；另有未安装的paper-review | 论证、证据、润色、审稿、全文同步完整；数学量词与双语模式需补 | 开放Skill格式；Python标准库审计；排版另需TeX | 选一个主入口，适度补数学路由 |
| haruhisa-enomoto/math-paper-skills / f681d8bb37f4b851298270751822ea00bbed54de | 写作47行、阅读31行及较长指南 | 数学叙事强；reader排除证明核验；每次小修也要求独立回归 | 成对Skill及强制审阅增加负担 | 不安装 |
| hameefy/claude-latex-skill / 2ea88ee9d69425d77b019dde6707238e0ddd5790 | 单文件1755行 | 数学LaTeX/Beamer丰富；中文审稿不足，规定较多模板与宏 | 需要完整TeX与多种包，可能冲突现有前导区 | 不安装 |
| jmf-enigma/or-ms-writing-skill / 51af4a7e693676595c32025fee3405348f535e6e | 268行及参考资料 | 英文OR/MS叙事、定理呈现强；完整证明依赖外部Skill | Python工具；特定领域、英文倾向 | 不安装 |
| voidful/academic-skills / 71e9c42c60636602e87985f4306d134a3b63809e | 根94行+7子入口，子入口311–732行 | 繁中讨论、正式英文、证明/审稿都有；跨任务指定pipeline、触发词重叠 | 标称Codex兼容，整体会出现8个SKILL.md | 不符合单稳定入口原则 |
| Brandon030722/academic-writing-skill / 531fde1aff669eb6c8cd7ede0d2fe044ef24d339 | 129行 | 原生中英/LaTeX编辑；专门数学证明契约不足；未发现许可证 | 可移植指令，资料较轻 | 不作再分发安装基底 |

选中上游最近推送2026-10-09，许可证MIT。仅复制 skills/academic-writing-skills 和许可证；未装同仓paper-review或任何候选的第二个Skill。候选clone在扫描目录外。

## 实际安装与调用

仓库级位置：`.agents/skills/academic-writing-skills`；当前恰有1个SKILL.md，253行。加入按需mathematics.md，覆盖双语、LaTeX保全、真残差、全对/锚定、图块/完整纤维、覆盖/唯一性、留域及精确文献映射。移除不属于本项目的survey-paper-wcvx依赖。只选当前任务所需模式，不强制串联。

从ppa目录启动Codex，调用：

```
$academic-writing-skills 请将第四节改为简洁中文，保留公式、量词与引用。
$academic-writing-skills Polish this LaTeX paragraph without changing its mathematical claims.
$academic-writing-skills 审查这个定理：逐项核假设，给出证明缺口或反例。
```

官方文档：https://learn.chatgpt.com/docs/build-skills ，显式调用支持 `$`/`/skills`，description支持隐式选择。当前环境没有Codex CLI，实际调用通过三名新上下文子代理显式加载验证；不能把这等同于CLI/IDE自动发现与自然语言自动触发的实测。

## 依赖和验证

指令不要求API key、第三方账号或MCP。Python审计只用标准库；完整排版使用当前稿TeX引擎。基础校验通过，安装副本脚本回归27项通过。上游pytest是开发测试依赖；三类行为结果、编译验证与具体限制见skill_tests。静态PASS不代表数学真值或期刊格式认证。
