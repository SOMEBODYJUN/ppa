# 当前 RLEB 修订稿

本目录是本轮唯一活跃论文源码，原始输入另存于上级“原始投稿包”。入口为 `main.tex`，输出为 [RLEB_中文修订稿.pdf](RLEB_中文修订稿.pdf)。作者名沿用原稿“菠萝之神”。

原 Corollary 2.7 升为主定理 2.5，完整多值见证说明它确实放宽全对 RL 条件；删去重复的独立假设，全对图块条件压入推论 2.7。第四节已翻译为中文，并按当前第三节的秩亏 Hamilton 例重写比较。摘要、引言、结论与主例对齐；第五节及 signed-Schur 附录保留原有英文，整份文件因此是中英混合修订稿。

在本目录运行：

```bash
bash build.sh
```

脚本使用 XeLaTeX、BibTeX 和 Fandol 字体。已有完整 TeX 环境时直接编译；缺少格式或中文包时可通过 `tools/tex-support/bootstrap.sh` 重建隔离依赖。下载来源、版本和校验在该目录的 `dependencies.json` 与 README 中，首次补齐需要网络。所有编译均关闭 shell escape，生成目录不入版本库。可用 `PPA_TEX_SUPPORT=/绝对路径` 指定已准备好的隔离支持目录。

主定理、Hamilton 证明、第四节文献接口和 Schur 附录分别经过内部独立数学审查；修复后重新编译和查看全部页面。审查、修改理由和最终验证记录在上级目录。当前数学结果不代表穷尽新颖性认证、外部同行审稿或任何尚未指定的期刊格式验收。

仓库根目录仅安装 `.agents/skills/academic-writing-skills`。写作、证明审查或 LaTeX 工作选择对应模式即可，不要求调用其他写作 Skill 或固定流水线。
