# 当前 RLEB–GPPA 修订稿

本目录是唯一活跃论文源码，原始投稿包不改。入口main.tex，输出 [RLEB_中文修订稿.pdf](RLEB_中文修订稿.pdf)，作者沿用“菠萝之神”。

正文从Cauchy性、距离趋零与有限长度的标准判定开始；一般核物理父定理C249及能量分支C250控制同一允许关系的全部输出。恒等核准确恢复普通PPA的C02-v3，固定正定度量另用M内积/M距离/M⁻¹真残差。C242三角例展示非Lip切向漂移，C251四次Bregman例展示同目标下三次物理率。第5节以局部吸引零簇的全域完成为问题，给C254指数平衡与C252真实弱凸优化；第6节给参数识别及C253显式能量，恢复单调情形任意正步长。

一般核主定理要求实际相邻转移的物理位移控制；核收敛与物理收敛分开，旧C208–C210核chart身份保持。拓扑结论当前限普通PPA与固定SPD坐标转移。数学与行文独立审查记录见 [GPPA主理论](../GPPA主理论/README.md)；先行性、目标期刊验收与全库历史审计未完成。

原Hamilton、Schur及原扩展比较仍在supplements，日常任务不依赖它们。可选supplement.tex保留旧材料的编译入口。

在本目录运行 `bash build.sh`。XeLaTeX、BibTeX、Fandol；缺中文依赖时tools/tex-support/bootstrap.sh建立隔离环境，来源在dependencies.json。可用PPA_TEX_SUPPORT指定既有环境，编译关闭shell escape。

仓库仍只安装 `.agents/skills/academic-writing-skills`；中文、英文、LaTeX、证明或数学行文按需切换，不要求固定流水线。
