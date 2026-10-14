# 中文 RLEB–PPA 论文

本目录是唯一活跃论文源码，作者为“菠萝之神”。标题为 *Nonlinear Resolvent Geometry and Error Bounds for Proximal Point Convergence*。

`main.tex` 按当前大纲编排：不编号引言，第一章前置知识，第二章普通 PPA 主定理及固定核 GPPA 推广，第三章广义单调性比较，第四章零集几何，第五章讨论与结论。定义1/2、引理1/2、假设1/2/3和定理1/2/3分别编号；GPPA不重复普通PPA的整组前件，而给出替换条件与物理提升。

正文输出为 [RLEB_中文修订稿.pdf](RLEB_中文修订稿.pdf)。`supplement.tex` 引用同一份主文并接入附录A旋转达到族、附录B完整对数模与Dini边界、附录C Hamilton及固定核例，输出 [RLEB_中文完整稿.pdf](RLEB_中文完整稿.pdf)。两份PDF共享源码，不维护历史副本。

在本目录运行：

```bash
bash build.sh
```

使用 XeLaTeX、BibTeX 与 Fandol 字体，关闭 shell escape。缺中文依赖时使用已有 `tools/tex-support` 隔离环境；也可用 `PPA_TEX_SUPPORT` 指定该环境。源码可在安装相应依赖的 TeX Live 中编译。

数学范围保持完整近端/允许子关系、全部允许输出、完整真实残差、同一残差窗口及物理位移的区分。邻域回缩和Euler指数调用经典理论；参数改善仅对文中所列充分条件作同对象比较，不宣称包含全部既有理论。数学身份以规范层为准，整库优先权和特定期刊要求不属于本次成文验收。

数学行文使用 `.agents/skills/academic-writing-skills`，自然行文复核使用 `.agents/skills/humanizer`；本轮不以文本风格判断作者身份或检测率。复算入口见 [当前大纲与论文复算](../../research/code/author_outline_review/README.md)。原始上传材料保持不改。
