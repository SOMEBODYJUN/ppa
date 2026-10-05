# C05-v2 的 Vietoris 同调同构导入卡

审计日期：2026-10-05。对象为
[C05-v2](../canonical/local_range_without_supercriticality.md#lr-theorem)
中 `Vietoris–Begle 定理使 π_* 为同构` 这一步，以及
[LIT-GRN-2002](../LITERATURE.md#lit-grn-2002) 的系数与纤维条件。
本卡不改定理假设、状态或其他全局登记。

**结论：该同构可由 GRN2002 自身的 Theorem 1.2 直接导入。**
该文使用的是带紧载体的有理 Čech **同调**，不能把上同调定理的
`π^*` 偷换为 `π_*`。原引 [15] 的定义和对偶定理还足以把本项目
紧纤维的 Čech 上同调 acyclicity 接到该同调版本；这一接口未发现
实质缺口。当前缺的是精确定理号与来源定位，以及对初始
“有理 Čech-acyclic”一词的明确约定。

## 1. 实际核过的一手版本

**GRN2002。** L. Górniewicz and D. Rozpłoch-Nowakowska,
“The Lefschetz Fixed Point Theory for Morphisms in Topological Vector Spaces,”
*Topological Methods in Nonlinear Analysis* **20** (2002), 315–333，
[期刊原版 PDF](https://www.tmna.ncu.pl/static/files/v20n2-07.pdf)，
DOI [10.12775/TMNA.2002.039](https://doi.org/10.12775/TMNA.2002.039)。
已核正文及 PDF 页面图像，非只看摘要或转引。

| 印刷页 / PDF 页序（从 1 起） | 可导入内容 |
| --- | --- |
| 315 / 1，§1 首段 | 系数为 \(\mathbb Q\)，\(H\) 是带紧载体的 Čech 同调。acyclic 要求非空、正阶同调为零、\(H_0\cong\mathbb Q\)。 |
| 315 / 1，Definition 1.1 | 在 Hausdorff 空间中，Vietoris 映射是 perfect 满射，各纤维 acyclic；对映射还要求 \(\Gamma_0=p^{-1}(X_0)\)。perfect 的定义包含连续、闭映射和紧纤维。 |
| 316 / 2，Theorem 1.2 | 这样的 \(p:(\Gamma,\Gamma_0)\to(X,X_0)\) 诱导同调线性同构 \(p_*:H(\Gamma,\Gamma_0)\to H(X,X_0)\)。 |
| 319 / 5，Theorem 2.4 | morphism 的诱导映射为 \(q_*p_*^{-1}\)，与 C05-v2 后续 Lefschetz 计算所用方向一致。 |

**G1976（GRN2002 的原参考文献 [15]）。** L. Górniewicz,
“Homological methods in fixed-point theory of multi-valued maps,”
*Dissertationes Mathematicae* **129** (1976)，
[机构目录](https://pldml.icm.edu.pl/pldml/element/bwmeta1.element.zamlynska-a7876602-92ed-4af8-a848-74505a8155d6)，
[机构扫描 PDF](https://pldml.icm.edu.pl/pldml/element/bwmeta1.element.zamlynska-a7876602-92ed-4af8-a848-74505a8155d6/c/rm129_01.pdf)。
已下载并逐页目视核以下内容；相关印刷页比该扫描的 PDF 页序大 1。
原件只作临时阅读，未添加到仓库的历史源文件。

| 印刷页 / PDF 页序 | 可导入内容 |
| --- | --- |
| 7 / 6，I.§1 | \(\widetilde C\) 是紧 Hausdorff 对及其连续映射的范畴；\(H_*\)、\(H^*\) 分别为 \(\mathbb Q\) 系数 Čech 同调、上同调。 |
| 8 / 7，I.§1 Theorem (1.1) | 在 \(\widetilde C\) 上，\(H_*\cong\operatorname{Hom}_{\mathbb Q}\circ H^*\) **自然同构**。方向是同调等于上同调的代数对偶。 |
| 11–12 / 10–11，I.§3 | 带紧载体的 \(H\) 由所有紧子对的普通 Čech 同调作直接极限定义。p.12 明说：紧对以及紧对之间的映射上，\(H=H_*\)。 |
| 13–14 / 12–13，I.§4 | p.13 给 proper 与逐纤维 acyclicity 条件；p.14 (4.2) 为紧空间的 **Vietoris–Begle Mapping Theorem**（同调同构），(4.3) 为紧对版，(4.4) 为带紧载体版。 |

版本复核的辅助来源是同一作者的
[2006 年 LNNA 8 讲义](https://www.tmna.ncu.pl/static/files/LNNA_08.pdf)，
“Homological methods in fixed point theory of multivalued mappings,” pp.11–66：
p.13 Theorem (1.1)、pp.16–17 紧载体定义、pp.18–19 Theorems
(1.14)–(1.16) 与上述接口一致。本卡的核心导入不依赖将此讲义
误记为 1976 原文或 1999 专著；不同版本的定理编号不可互换。

## 2. 本项目的逐条件核对

统一以 \(H^c_j\) 表示 GRN2002 的带紧载体同调，以
\(\check H_j,\check H^j\) 表示普通 Čech 同调、上同调，均取
\(\mathbb Q\) 系数。以下是本项目的应用推导，不是来源对
本项目对象作出的断言。

| 外部条件 | C05-v2 中的落实 |
| --- | --- |
| Hausdorff 源、靶与连续映射 | \(A\subset\mathbb R^n\)，\(\Gamma\subset A\times A\)，\(\pi(p,y)=p\) 为限制投影。 |
| 紧图 | collar 推导先给全部 \(y\in T(p)\) 位于 \(\operatorname{int}A\)。usc 与紧值给图在 \(A\times A\) 中闭；\(A\times A\) 紧，故 \(\Gamma\) 紧。无需假设 \(\Gamma\) 是多面体或 ANR。 |
| 满射与 perfect | 每个 \(T(p)\ne\varnothing\) 给满射。紧源到 Hausdorff 靶的连续映射闭，纤维闭于紧源，故 \(\pi\) perfect。不能仅用“有紧纤维”代替闭映射条件。 |
| 每一纤维同调 acyclic | \(\pi^{-1}(p)=\{p\}\times T(p)\cong T(p)\)。紧性及下一节的对偶桥给 \(H^c_0\cong\mathbb Q\)、\(H^c_j=0\ (j\ge1)\)。这是所有 \(p\in A\) 的假设。 |
| 对的逆像条件 | 使用 \((\Gamma,\varnothing)\to(A,\varnothing)\)，于是 \(\pi^{-1}(\varnothing)=\varnothing\)。 |
| 定理结论 | GRN2002 Theorem 1.2 给每阶 \(\pi_{*,j}:H^c_j(\Gamma)\to H^c_j(A)\) 同构；因源靶紧，它同时是普通有理 Čech 同调的同构。 |

输出映射 \(e_h\) 的纤维在此表中从未出现。\(\pi_*\) 的同构不要求
\(e_h(T(p))\) acyclic，也不要求 \(T(p)\) 可缩、局部可缩或有奇异同调
acyclicity。不能由有限样本取代整窗的非空、usc 和逐纤维 acyclicity。

## 3. 同调与上同调的桥接方向

对每个非空紧纤维 \(K=T(p)\)，G1976 p.12 和 p.8 Theorem (1.1) 给
\[
H^c_j(K;\mathbb Q)
\cong\check H_j(K;\mathbb Q)
\cong\operatorname{Hom}_{\mathbb Q}
       (\check H^j(K;\mathbb Q),\mathbb Q). \tag{VB-dual}
\]
因此，明确的上同调假设
\(\check H^0(K;\mathbb Q)\cong\mathbb Q\)、
\(\check H^j(K;\mathbb Q)=0\ (j\ge1)\) 就给所需的同调条件。
等价地，可写 \(K\ne\varnothing\) 且所有约化有理 Čech 上同调为零。
此步不要求未知纤维或 \(\Gamma\) 的同调预先有限维。

当前正文用有限 nerve 对偶与
\(\operatorname{Hom}(\varinjlim V_i,\mathbb Q)
\cong\varprojlim\operatorname{Hom}(V_i,\mathbb Q)\)
说明这一方向，方向正确；但该恒等式本身尚未写明带紧载体版本与
普通 Čech 同调的识别。直接注明 (VB-dual) 的两个原始来源可使接口
完整。不要无条件把 (VB-dual) 反写为
\(\check H^j(K)\cong\operatorname{Hom}(\check H_j(K),\mathbb Q)\)：
任意无限维代数向量空间没有这样的双对偶识别。

对正文另一处 \(b:A\hookrightarrow B\)，上述自然性把
\(b_*\) 识别为 \(\operatorname{Hom}_{\mathbb Q}(b^*,\mathbb Q)\)。
故 \(b^*\) 满射确实给 \(b_*\) 单射；\(A,B\) 为有限多面体还保证
之后的 Euler–Lefschetz 交错迹是有限和。无需把任意紧图的 Čech
同调换成奇异同调。

## 4. 可直接回填的最小文本

**假设处的约定句（若保留上同调表述）：**

> 本页“有理 Čech-acyclic”指非空且所有约化有理 Čech 上同调为零。

**替换证明中从同/上同调桥到“Vietoris–Begle 定理使 \(\pi_*\) 为同构”的文本：**

> 对紧纤维，带紧载体的有理 Čech 同调等于普通 Čech 同调；且
> \(\check H_j(K;\mathbb Q)\cong\operatorname{Hom}_{\mathbb Q}(\check H^j(K;\mathbb Q),\mathbb Q)\)
> 自然成立（Górniewicz 1976，I.§1 Theorem (1.1)，p.8；I.§3，p.12）。
> 所以上同调 acyclicity 给出所需的同调 acyclicity。
> 紧 Hausdorff 图到 \(A\) 的连续满射 \(\pi\) 是闭映射且有紧纤维，
> 因而是 GRN2002 Definition 1.1（p.315）的 Vietoris 映射。
> 对 \((\Gamma,\varnothing)\to(A,\varnothing)\) 应用同文
> Theorem 1.2（p.316），得 \(\pi_*\) 在上述有理 Čech 同调的每一阶均为同构。

**LITERATURE 卡的最小补句：**

> 同文 p.316 Theorem 1.2 明确保证 Vietoris 映射在所用的带紧载体
> 有理 Čech 同调上诱导同构；紧纤维的上同调假设经原引 [15]
> p.8 Theorem (1.1) 的自然对偶及 p.12 的紧载体识别转为该同调条件。

## 5. 缺口与审查边界

本次未发现使 C05-v2 的 \(\pi_*\) 同构失效的数学缺口。应修复的是
仅报定理名的引用精度、初始 acyclicity 约定的歧义，以及紧载体
识别在原正文中的省略。两个一手原文已覆盖这些接口。

本卡没有从该拓扑导入推出指定 \(T\) 的存在，也没有验证任何具体
原生模型满足全窗假设；没有重审 C70 数值不等式、其他外部定理
或新颖性。GRN2002 Theorem 6.2 的 Lefschetz 导入仍按既有文献卡
管理。以上结论限定于当前紧 Hausdorff 图、\(\mathbb Q\) 系数和
所有纤维 acyclic 的情形，不向任意非紧空间、其他系数或奇异同调扩张。
