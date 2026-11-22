# DD 中文 LaTeX 讨论稿

唯一源稿为 main.tex 及 sections/，编译稿为 DD_draft.pdf。题目和作者信息留待作者确定。当前为 15 页 A4，含参考文献，正文采用 11pt，页边距 25mm。

## 作者安排与精简范围

顺序为历史式摘要；引言；DD1；DD2；DD3；近端参数选择；结论与展望。存在引理在引言正式陈述，在 DD3 证明。DD2 先给三段补偿与扩张例，再由无限长度例引出比较级数与 F1–F3 耦合长度势。例子跟随相应结果。

本轮按作者的中文与简洁要求改写，不是原英文稿逐句翻译。删除了一般类锐性的完整实现、临界轨道构造、DD2 的精确单步实现及另一版无 F2 势、DD3 的额外不满射反例、选参的附加渐近推论和重复范围说明。这些研究资产仍在原专题；没有修改数学 Claim 的身份或状态。旧英文稿由 Git 历史保留，不另建竞争正文。

## 数学来源

| 源文件 | 保留内容与规范来源 |
| --- | --- |
| sections/frontmatter.tex、introduction.tex | 历史叙事、指标解释、C477 存在引理陈述；文献对应原稿的指定定理。 |
| sections/dd1.tex | DD11/DD12、几何证明与有限长度、完整射线扩张例；见 research/topics/dd2/dd1_recovery.md、C285/C400/C443 及 research/novelty/DD1_PRIOR_ART_2026-11-20.md。 |
| sections/dd2.tex | 一般有符号下界与完整真残差的三段补偿、旋转及剪切例、比较级数和 F1–F3；见 research/topics/dd2/core.md、original_f_conditions.md、operator_separation.md。 |
| sections/dd3.tex | C477 证明、DD3 与 C478 非二次例；见 research/topics/dd2/global_proximal_solvability.md。 |
| sections/parameters.tex | C479–C481 的两支反演、小步障碍、原角度条件下共同覆盖及变参数收敛；见 research/topics/dd2/parameter_selection.md。 |
| sections/conclusion.tex | 实际有限长度的未闭边界与应用条件。 |

## 编译

安装含 CTeX、Fandol 字体、AMS、natbib、enumitem、geometry、fancyhdr 与 hyperref 的 TeX Live，并安装 XeLaTeX、BibTeX、latexmk。在本目录运行：

    bash build.sh

输出 DD_draft.pdf，中间文件留在 build/。源码包包含本目录源文件、参考文献与编译脚本。当前环境使用隔离生成的 CTeX 与 XeLaTeX 格式编译，未改系统安装或另一篇稿件。

## 本轮复核

数学交叉审读重构了 DD1、DD2 的分段条件、端点、完整真残差、零输入、有限前缀留域、旋转与剪切例，以及 DD3/选参的条件衔接。中文冷读核对全部最终源文件的作者章序、句间衔接、术语与冗余。修订补明了普通逆公式的定义域、引言指数有限性及旋转例的比较函数选择。

读取并使用作者指定的 [Less AI Tone v2](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)（fe77df00a27cf94428632ad449a4aecdcb83db41），结合既有中文数学写作与 Humanizer 规范。脚本仅诊断中文措辞，数学条件、姓名列举与必要技术重复保留；不据其统计推断作者身份或检测率。正文不用“窗口、证书、预算、合同”等过程用语。

最终 XeLaTeX 编译得到 15 页，无未定义引文、交叉引用、重复标签、缺字或溢出版面诊断。检查了全部页面缩略图，并放大核查第 1 页中文、第 7 页三段公式、第 14 页长定理及第 15 页参考文献。源码包解压后重新编译，逐页文本与交付 PDF 一致。作者大纲与项目资产校验器通过；机器检查不代替数学审读。

本轮是既有数学的中文成文与选材，未重新认证公开新颖性或期刊投稿合规。一般函数下有限长度的完整刻画与可观察的逐次最优选参仍未解决。
