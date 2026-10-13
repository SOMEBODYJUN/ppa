# Astra 论文制图：技能来源与数学任务

本轮按作者要求下载一个论文制图技能，并交给 GPT-6 Astra（ultra）实际制作独立示意图。范围限于图件、图注、复现代码与技能来源记录；没有改动主论文、摘要、规范命题或定理编号。

## 下载的技能

使用 K-Dense 的 **scientific-visualization**：

- 原始仓库：<https://github.com/K-Dense-AI/scientific-agent-skills>。
- 固定版本：`a1043ef544e3a100c28e70a736b6cf32554d0677`。
- 上游正文：<https://github.com/K-Dense-AI/scientific-agent-skills/blob/a1043ef544e3a100c28e70a736b6cf32554d0677/skills/scientific-visualization/SKILL.md>。
- 本地入口：[`SKILL.md`](../../.agents/skills/scientific-visualization/SKILL.md)。下载完整技能目录，保留原文和 MIT 许可。
- 校验清单：[`UPSTREAM_SOURCE.json`](../../.agents/skills/scientific-visualization/UPSTREAM_SOURCE.json)，记录所有原始文件的 SHA-256、字节数及固定提交；本轮逐文件核对通过。

选择理由是本任务需要可复现的数学矢量示意图，以及成图后的字体、物理尺寸、配色和裁切检查。这个技能支持 Matplotlib 的论文导出与审查。数学形状及箭头由已核公式确定；一般科学配图模板不能替代数学证明。本轮不调用额外绘图服务，不下载其它技能，也不执行上游目录中的程序来代替对本图的内容审查。

期刊专属要求尚未在本任务中确定，因此制作通用论文图稿；不把尺寸、配色或格式称为投稿合规认证。

## 交给 Astra 的数学契约

图的中心结论是：在局部 RLEB、连续单值完整物理近端映射，以及统一消失的物理长度尾界等条件下，所认证的零簇 \(M\) 是某个开邻域 \(U\) 的连续回缩，

\[
P:U\longrightarrow M,\qquad
P(x)=\lim_{k\to\infty}T^k(x),\qquad P|_M=\operatorname{id}_M.
\]

这里的 \(M\) 未必是算子的全部零点集。仅锚定多值 RLEB 不自动给出这个连续回缩结论；没有从回缩直接推断变形回缩、同伦等价或 \(\chi(U)=\chi(M)\)。

绘图任务包含三个读图功能：

1. 以厚圆环收回圆周说明连续极限落点和零点驻定。该具体模型的径向公式可以证明，但不把径向运动作为一般算子的轨道或连续时间变形。环心不属于局部输入管。
2. 示意允许的孤立点、有限分叉和有角点区域，强调外形可以不凸、不光滑。各形状来自不同模型，不把它们拼成一个已经认证的完整零集。
3. 示意整套连续性与统一尾条件排除的无限局部积聚，例如 Cantor 尘、孤立点向零点积聚、缩小的本质环圈。有限绘图片段代表无限形状；有限片段自身不被禁。

欧拉示性数与额外零点补偿需要独立的局部指数桥和全局指数前提，不混入本图的邻域回缩结论。

承重依据是 [`general_modulus_dynamics.md` 的 C11](../../research/canonical/general_modulus_dynamics.md#gm-retraction)；连续完整近端版本、开域修补及几何排除见 [`rleb_zero_geometry_intrinsic.md`](../../research/candidates/rleb_zero_geometry_intrinsic.md)。有限分叉的完整机制验证见 [`rleb_cross_zero_set.md`](../../research/candidates/rleb_cross_zero_set.md)。候选卡保持其原有未注册身份。

## 检查与交付约定

Astra 制作英文论文图与可复算 Python 源码，条件允许时同时制作中文解释版。导出 PDF、SVG 与 PNG 预览，保存到本轮图件目录。必须先运行、检查并修复后交付。

检查包括：环形输入域内外边界、零距离输入驻定、坐标原点被域排除、径向一步公式与反算、箭头在管内且指向极限，以及图件的文字裁切、物理尺寸、矢量内容和配色。全称性质以解析论证为依据，有限计算检查只发现实现错误。

## 软件来源说明

本轮制图使用上述技能的排版与审查指导。按上游归属要求，在这份软件来源记录中列出：Timothy Kassis, Vinayak Agarwal, Yuhuan He, Darshil Patel, and Aubrey M. Brueckner (2026), *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents*, <https://doi.org/10.48550/arXiv.2609.00065>。2026-10-13 核对 arXiv 元数据，当前记录为 2026-09-02 修订的 v2；没有由此增加主论文的数学引用或主张该工具证明了本图的数学结论。

## 已完成的图稿

Astra 已制作并冻结 [英文论文图 PDF](图件/rleb-neighborhood-retraction.pdf)、[英文 SVG](图件/rleb-neighborhood-retraction.svg) 及 [中文解释预览](图件/rleb-neighborhood-retraction-cn.png)。[双语独立图注](RLEB邻域回缩示意图_图注.md) 包含完整近端关系、原点完整纤维、真残差、同窗参数、精确轨道及适用边界。[完整源码](../../research/code/rleb_neighborhood_retraction/draw_figure.py) 无网络调用，也不依赖上游技能中的辅助程序。

主代理独立重跑两种语言，另用有理数检查完整近端反算与认证窗预算，并核对最终输出哈希、PDF 实际字体、尺寸、无栅格内容和 PNG 不透明性；直接观看两版 PDF 的渲染及灰度预览，没有发现文字重叠、缺字、裁切或箭头错位。定位记录见 [parent-review.json](../../research/code/rleb_neighborhood_retraction/parent-review.json)。英文论文 PDF 嵌入 TrueType 字体；可选中文 PDF 使用 Type 3 矢量字形，避免现有 CJK CFF 字体与 TrueType 导出模式不匹配。后者不是期刊字体规范声明。

图稿保持独立，本轮没有嵌入主论文。论文中的实际排版与具体期刊检查属于另一步，不由独立图稿的通过代替。
