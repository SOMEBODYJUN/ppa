# 一般模 GPPA 的集中证明稿

[gppa_modulus.pdf](gppa_modulus.pdf)与[gppa_modulus.tex](gppa_modulus.tex)集中证明 C208–C214 的核心机制。中文判断、完整三维 cap/SF/log 例子与全部比较边界从[统一入口](../../canonical/generalized_ppa_modulus.md)可直接进入。

本稿另从零证明二维 SF 简化完整关系，没有把有限轨道当作完整图。核三分支、源全部正 ASM 核包含、物理端点与相邻步的不同条件、精确物理 Q-ν、无正则性配对核障碍、半阶逆螺旋和输出误差管均显式列前件。

重建 PDF：

```bash
python3 research/manuscripts/gppa_modulus/render_note.py
```

作用域 renderer 依赖 ReportLab、Matplotlib 和 Pillow；它解析这份固定 TeX 的段落、内联与显示公式，公式解析失败即报错，不冒充完整 LaTeX 编译器。生成时数学位图只作临时文件，PDF 自包含。源稿仍是标准数学 TeX，可在完整 LaTeX 环境编译。

[render_verification.json](render_verification.json)保存实际内联公式/显示行、缩放及 renderer 范围；[pdf_qa.json](pdf_qa.json)保存源稿/PDF 指纹、实际页数、页边界检查及逐页面读结果。渲染检查不证明数学正确；[独立数学接收](../../audit/GPPA_MODULUS_RECEPTION_2026_10_09.md)另行记录实际阅读。
