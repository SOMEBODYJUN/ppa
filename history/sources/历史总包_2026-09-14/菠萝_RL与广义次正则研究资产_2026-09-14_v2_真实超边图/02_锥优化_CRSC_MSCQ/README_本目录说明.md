# 锥优化 CRSC–MSCQ

> 整理层目录说明 · 2026-09-14

## 建议入口顺序

1. [冻结最小面CRSC与MSCQ_当前论文_v04.pdf](01_论文主稿/冻结最小面CRSC与MSCQ_当前论文_v04.pdf)
2. [冻结CRSC_秩夹逼与MSCQ核心证明审计.md](03_核心证明审计/冻结CRSC_秩夹逼与MSCQ核心证明审计.md)
3. [Nice非Amenable锥_边界反例与必要性审计.md](04_边界反例与优先权/Nice非Amenable锥_边界反例与必要性审计.md)
4. [耦合SOC与PSD_正例及显式常数审计.md](03_核心证明审计/耦合SOC与PSD_正例及显式常数审计.md)
5. [CRSC与MSCQ_优先权及正式版证据矩阵.md](04_边界反例与优先权/CRSC与MSCQ_优先权及正式版证据矩阵.md)
6. [构建报告与版本核对_v04.md](02_可编译源文件/构建报告与版本核对_v04.md)

可编译源位于 `02_可编译源文件`。在复制目录用普通 TeX Live：`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`；或 pdfLaTeX → BibTeX main → pdfLaTeX 直至稳定。保留 main.tex、references.bib、main.bbl 与 author-cjk.{ttf,enc,tfm} 同目录。原 build.sh 专供生产环境，运行会在其目录生成 tex-cache/qa；通常环境优先普通命令。字体再生成可选，需要 PyMuPDF、fontTools 与 ttf2tfm，并非普通构建前提。

本包未重新编译，也没有执行验证脚本。v04 源 ZIP 的 13 个成员中 12 个展开保留；expert-result.yaml 的历史契约被构建报告吸收，不另重复。核心数学状态和最终版优先权必须分开。

## 本目录原件用途

- [冻结最小面CRSC与MSCQ_当前论文_v04.pdf](01_论文主稿/冻结最小面CRSC与MSCQ_当前论文_v04.pdf)：当前最成熟锥论文 PDF。状态 `PROVED`。
- [main.tex](02_可编译源文件/main.tex)：主稿源文件。状态 `REFERENCE`。
- [references.bib](02_可编译源文件/references.bib)：13 条书目记录；含正式版与作者稿分列。状态 `REFERENCE`。
- [main.bbl](02_可编译源文件/main.bbl)：已生成书目，便于离线复现。状态 `REFERENCE`。
- [build.sh](02_可编译源文件/build.sh)：原生产环境构建脚本。状态 `REFERENCE`。
- [author-cjk.ttf](02_可编译源文件/author-cjk.ttf)：中文作者 TrueType 字体子集。状态 `REFERENCE`。
- [author-cjk.enc](02_可编译源文件/author-cjk.enc)：作者字体 TeX 编码。状态 `REFERENCE`。
- [author-cjk.tfm](02_可编译源文件/author-cjk.tfm)：作者字体 TeX metrics。状态 `REFERENCE`。
- [build_author_font.py](02_可编译源文件/build_author_font.py)：可选作者字体再生成；非普通编译前提。状态 `NOT_EXECUTED`。
- [原始构建与数学范围说明.md](02_可编译源文件/原始构建与数学范围说明.md)：原始构建与数学范围说明。状态 `REFERENCE`。
- [构建报告与版本核对_v04.md](02_可编译源文件/构建报告与版本核对_v04.md)：构建报告与版本核对_v04。状态 `REFERENCE`。
- [中文作者字体来源与再生成说明.md](02_可编译源文件/中文作者字体来源与再生成说明.md)：中文作者字体来源与再生成说明。状态 `REFERENCE`。
- [论文证据范围与未闭合门槛台账.md](02_可编译源文件/论文证据范围与未闭合门槛台账.md)：论文证据范围与未闭合门槛台账。状态 `REFERENCE`。
- [冻结CRSC_秩夹逼与MSCQ核心证明审计.md](03_核心证明审计/冻结CRSC_秩夹逼与MSCQ核心证明审计.md)：冻结CRSC_秩夹逼与MSCQ核心证明审计。状态 `PROVED`。
- [Nice非Amenable锥_边界反例与必要性审计.md](04_边界反例与优先权/Nice非Amenable锥_边界反例与必要性审计.md)：Nice非Amenable锥_边界反例与必要性审计。状态 `OBSTRUCTED`。
- [耦合SOC与PSD_正例及显式常数审计.md](03_核心证明审计/耦合SOC与PSD_正例及显式常数审计.md)：耦合SOC与PSD_正例及显式常数审计。状态 `PROVED`。
- [CRSC与MSCQ_优先权及正式版证据矩阵.md](04_边界反例与优先权/CRSC与MSCQ_优先权及正式版证据矩阵.md)：CRSC与MSCQ_优先权及正式版证据矩阵。状态 `PENDING`。
- [锥论文_最终论证架构与依赖链.md](03_核心证明审计/锥论文_最终论证架构与依赖链.md)：锥论文_最终论证架构与依赖链。状态 `PENDING`。
- [验证_SOC与PSD实例常数.py](05_验证程序/验证_SOC与PSD实例常数.py)：验证_SOC与PSD实例常数。状态 `NOT_EXECUTED`。
