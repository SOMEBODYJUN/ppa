# DD 英文 LaTeX 初稿

唯一编译入口为 main.tex。题目和作者信息留待作者确定；当前封面上的 DD 仅标识工作稿。

正文严格采用作者确定的次序：摘要；Introduction；DD1；DD2；DD3；近端参数选择；结论与展望。存在引理完整陈述在引言，证明在 DD3。例子跟随对应定理，没有另设预备知识、定理恢复或例子章。

## 编译

在本目录运行 bash build.sh。需要含 AMS、natbib、enumitem、microtype、geometry、fancyhdr 和 hyperref 的 TeX Live，以及 latexmk、BibTeX。输出为 DD_draft.pdf，中间文件保存在 build/。公式、引文及交叉引用由 LaTeX/BibTeX 生成。

## 正文与数学来源

| 文件 | 内容及来源 |
| --- | --- |
| sections/frontmatter.tex | 按历史与问题发展写成的摘要；比较范围与正文对应。 |
| sections/introduction.tex | 经典 PPA、Luke–Tam、Alcantara、Brito–Lara–Yuan；数值指标；存在引理 C477 的完整陈述。 |
| sections/dd1.tex | DD11/DD12 的双向分段计算、几何证明、留域与有限长度、完整射线图例。对应 research/topics/dd2/dd1_recovery.md、C285、C400、C443；文献比较见 research/novelty/DD1_PRIOR_ART_2026-11-20.md。 |
| sections/dd2.tex | 一般有符号下界和原真残差模的三段补偿；非几何有限长、次二次负缺陷和无限长边界；比较级数；F1–F3 长度势及无 F2 的充分版本。对应 C430、C453、C474 和 research/topics/dd2/core.md、original_f_conditions.md、operator_separation.md。 |
| sections/dd3.tex | C477 存在引理证明；同一实际允许关系的局部覆盖与 DD3；C478 的固定参数反例及非二次二维例。来源 research/topics/dd2/global_proximal_solvability.md。 |
| sections/parameters.tex | C479–C481：两支步长反演、小步障碍、原算子角度与线性误差界下的共同可用参数及变步长有限长度。来源 research/topics/dd2/parameter_selection.md。 |
| sections/conclusion.tex | 已证补偿、长度、可解性与选参范围；一般长度边界及应用仍待研究。 |
| references.bib | 七项一手文献。精确比较采用指定定理及固定 arXiv v1；不声明查新穷尽或世界范围优先性。 |

本次为写作整合，未改变上述 Claim 的数学身份或提升其研究状态。正文中的充分条件不宣称是每个固定算子的必要条件；全局可解性与局部收敛分别陈述。

## 写作与复核

保留定理假设、量词、真残差、允许关系与完整预解式的区别，以及有限前缀留域证明。面向读者的正文使用 neighborhood、bound、admissible 等惯用表达；不使用 window、certificate、budget、gate 等研究过程用语。

本轮读取并参考了已下载的写作资料：

- 作者指定的 [Lieflat Less AI Tone v2](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)，版本 fe77df00a27cf94428632ad449a4aecdcb83db41。其统计与脚本主要针对中文，不将其输出解释为英文数学论文的 AI 率，也不自动改写公式、引文或外语段落。作者已授权本轮直接清理，无需另等一轮确认。
- [Humanizer](https://github.com/blader/humanizer)，版本 a32f24407364c74c812b43c15926d638bee1e072，用于英文中空泛判断、重复铺垫和不必要的修辞。
- [LaTeX Mathematics Writing](https://github.com/amelieloher/math-paper-skills)，版本 4ec9c7bf76f0bdf931a00134cefe1f8ab7548e02，用于精确陈述、证明与排版；作者的章序优先。
- [Mathematical Academic Writing](https://github.com/JiahaoLi-creator/mathematical-academic-writing)，版本 39090de79c9b7bdd1203cb583d313995abad039a，本轮克隆并阅读其数学完整性、论文写作、反复防御性表述和成品核验规范。
- 仓库既有的数学写作及论文结构规范。

## 独立复核与编译

六路独立审读分别覆盖 DD1、DD2、DD3、步长选择、全篇英文及作者安排与一手文献。数学审读核对实际算子、完整真残差、量词、分支端点、零输入、有限前缀留域及轨道结论；英文审读与结构审读另行冷读全部最终源文件。当前受检范围内未留下实质性异议。此处记录内部检查范围，不代表期刊同行评审或新颖性认定。

本轮修订明确了 DD1 的全局二次锐性与逐尺度实现的区别；在扩张例后补入已有 C285 的临界不收敛构造；补明 DD2 普通逆的初始区间与非连续原模的端点；明确 DD3 和无 F2 长度推论的初值所属集合；将 Li--Mordukhovich 的比较限于其完整零集、局部 Hölder 前件、固定参数及 Theorem 7.3(i)。这些是已有结果的成文与适用范围核准，没有新增或提升 Claim。

最终源码通过 `bash build.sh` 编译。正文为 32 页，七项参考文献，无未定义引文或交叉引用、无重复标签、无编译警告或溢出版面诊断。已检查全部页面缩略图及分段公式、长定理、例子和参考文献的放大图。作者大纲验证器及项目资产验证器通过；机器检查不替代上述数学审读。
