# RLEB–PPA 投稿稿说明

## 稿件

- 题目：*Nonlinear Generalized Monotonicity and Error Bounds for Proximal Point Convergence at Multivalued Graph Junctions*
- 作者：菠萝
- 主文件：`main.tex`
- 编译稿：`RLEB_PPA_投稿稿_菠萝.pdf`

## 文章主线

正文采用内积形式的 RL 条件及其 (J)-side 推论，不以反射预解算子作为叙事框架。论证顺序为：

1. Luke--Tam 型标准局部 range coverage；
2. all-pairs 图上 RL 条件；
3. (J)-side 能量不等式和保留系数 (1/2) 的步长估计；
4. 在实际 proximal output 上使用独立的广义误差界；
5. 距离压缩、有限长度、局部化和整条轨道收敛；
6. 对真正多值 proximal relation 的 selection-uniform 扩展；
7. 二值平方根接缝例子及其最优 (1/2) 阶；
8. 与线性/二次广义单调性理论的精确关系；
9. 当 (J) 无显式公式时使用 signed-Schur 图导数验证器。

## 源文件结构

- `sections/frontmatter.tex`：摘要、引言、贡献和文章结构。
- `sections/theorem_spine.tex`：定义、引理、主收敛定理、幂律阈值及线性切片。
- `sections/verification_example.tex`：二值平方根接缝、完整 (J)、误差界、精确轨道和证书分离。
- `sections/related_work.tex`：与 semimonotonicity、Luke–Tam、Leventhal、Li–Mordukhovich–Zhu 等的关系。
- `sections/native_schur_verifier.tex`：signed-Schur 验证器的正文接口。
- `sections/appendix_signed_schur.tex`：验证器的完整假设、常数和证明。
- `sections/conclusion.tex`：结论与边界。
- `references.bib`：参考文献数据库。
- `数学语义核对与剩余问题.md`：最终数学核对和仍需作者决策的问题。
- `审校验收记录.yaml`：编译、视觉、语义和写作审校记录。

## 中文编辑与编译

本版本已改为 **XeLaTeX + UTF-8**：

- `.tex` 文件中可以直接输入、删除和修改中文，不需要 `CJK` 环境。
- 作者名已从两张 PDF 字形图片改为真正可编辑的 `\author{菠萝}`。
- 中文默认使用 TeX Live / Overleaf 自带的 Fandol 字体，不需要额外携带字体文件。
- 英文论文正文没有翻译或改写，后续中文内容可由作者自行替换。

标准 TeX Live 环境下执行：

```bash
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

也可以使用：

```bash
latexmk -xelatex main.tex
```

在 Overleaf 中请把 Compiler 设为 **XeLaTeX**。

当前交付稿仍使用 A4 `article` 类，尚未套用特定期刊模板。
