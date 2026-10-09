# 2026 年 8 月 GPPA / NFB 与 PPA 的逐定理比较

此目录固定比较两篇外部原稿与本库当前数学身份。原文、版本指纹、逐篇审查和独立攻击分开保存，方便多人接续。初轮比较基线为 `3dd02110d7666ba77b561bf2ab26641013a79fd3`；本轮指定 gpt-6.1-sol / ultra 的三份独立审查从 main `007ce8cb4b86601c3bf6af45a90601fcd871ca74` 接续。

**裁决：有实质重合；完整原图输入条件不同；但原轨道收敛还可通过明确子关系导入。** 先读 [COMPARISON.md](COMPARISON.md)，再进入 [6.1-sol GPPA审查](sol61_gppa_audit.md)、[6.1-sol NFB审查](sol61_nfb_audit.md)、[独立反向审查](sol61_independent_audit.md)。完整数学身份与初轮报告入口在 [BASELINE.md](BASELINE.md)。

| 本次可调用接口 | 证明与范围 |
| --- | --- |
| [C199](../../../CLAIMS.md#c199) | GPPA显式非线性核覆盖同一非单调自然子类全部普通轨道，并通过不变量恢复物理率；完整两个算法纤维不相等 |
| [C200](../../../CLAIMS.md#c200) | 原完整双支的ASM证明身份保持；无核正则性加强另登C204 |
| [C201](../../../CLAIMS.md#c201) | 任意合格同空间NFB拆分强迫原图固定二次锚；非退化自然类、cap、超线性、log原图均违反 |
| [C202](../../../CLAIMS.md#c202) | 非单调负恒等普通PPA与NFB完整同一；旋转和非零forward/memory实例亦有真实覆盖 |
| [C203](../../../CLAIMS.md#c203) | 标准full-graph primal–dual lift将同一必要二次锚压回原图；任意其它lift仍待核 |
| [C204](../../../CLAIMS.md#c204) | 完整标量双支→任意无正则性配对单调核也不能保持指定原轨道；[总变差分割完整证明](pair_monotone_barrier.md) |
| [C205](../../../CLAIMS.md#c205) | 保零集cap正支→简单显式ASM核与物理桥，T2可证明同一指定原轨道的点率/有限长 |
| [C206](../../../CLAIMS.md#c206) | 保零集超线性截断正支→clip尾和ASM核，T2可导入同一原尾的几何上界/有限长；不自动给精确超线性输出 |
| [C207](../../../CLAIMS.md#c207) | a>1对数正支→尾和配对单调核，T1加额外可和尾桥给原物理点收敛/长度；非ASM，a≤1不成立 |

物理几何点尾已蕴含有限长度，不能在覆盖子类单独作创新。**完整图不涵盖不是收敛不可导入**；C205–C207的 [反向证明](sol61_branch_restriction.md) 必须与C204一起读。附件全尺度次线性结构类有有界零纤维，而这里主要例子有无界零片；结构/纤维稿的全球先行性另核，不因收敛子类相交被判重复。

## 比较对象

- [8/3 GPPA v1 原文](sources/gppa_2608.01584v1.pdf)：Le–Mordukhovich–Théra，arXiv:2608.01584v1。
- [8/24 NFB v1 原文](sources/nfb_2608.22687v1.pdf)：Pesquet–Roldán，arXiv:2608.22687v1。
- [来源、下载地址与 SHA-256](sources/manifest.json)：字节身份，不是证明验收。
- [2026-10-09 原文重新取得记录](source_refresh_2026_10_09.json)：两份PDF与既存归档逐字节相同。
- 本库 [C02-v2](../../rleb_ppa.md)、[C09/C10 一般模](../../canonical/general_modulus_dynamics.md)、[C191–C193 自然原图](../../canonical/support_normal_natural_class.md)及 [C137 完整几何尾图](../../canonical/selection_geometric_cap.md)。结构稿 C03/C04 与收敛稿分开比较。

## 已执行的判别与未闭门

1. 固定原关系、完整纤维、零集、步长与算法轨道；GPPA 的任意核、NFB 的任意合格同空间分解都须检查。
2. 重合须给出具体变换与全部适用条件；排除须给必要条件或完整反例，不能凭术语差异。
3. 分开外文已证明结果、本库直接推导、定位解释与尚未解决的先行性问题。有限长度若由点范数 R-linear 收敛直接推出，不能单独作创新标识。
4. 原文相关证明、边界模型、独立复算及交叉审查现已按三份报告的实际范围完成；根Claim、状态和依赖图登记正反限定结论。固定核统一RL+真EB条件理论已由本轮C208–C214完成；一般C191/C192核/子关系分类、任意其它lift、其它外文及全球先行性仍开放，不以source归档或有限PASS替代。

<a id="reproduce"></a>
## 可复现计算

初轮三份脚本只用Python标准库，从仓库根运行：

```bash
python3 research/comparisons/2026_08_gppa_nfb/gppa_check.py
python3 research/comparisons/2026_08_gppa_nfb/nfb_check.py
python3 research/comparisons/2026_08_gppa_nfb/independent_attack_checks.py
```

结果分别在 [GPPA JSON](gppa_check_results.json)、[NFB JSON](nfb_results.json)、[独立精确结果](independent_attack_results.txt)。[集成复跑记录](verification.json) 保存执行环境、脚本哈希、原文指纹和退出状态。有限计算核常数、合法图点、线性/warped算法等式及SPD平方配方；任意核、任意拆分和无限轨道结论由正文证明承担。

本轮新增独立脚本与 [复跑记录](sol61_verification.json)：

```bash
python3 research/comparisons/2026_08_gppa_nfb/pair_monotone_checks.py
python3 research/comparisons/2026_08_gppa_nfb/sol61_gppa_check.py
python3 research/comparisons/2026_08_gppa_nfb/sol61_nfb_check.py
python3 research/comparisons/2026_08_gppa_nfb/sol61_independent_checks.py
python3 research/comparisons/2026_08_gppa_nfb/sol61_branch_checks.py
```

输出保存为相邻JSON。Fraction负责精确代数、参数及有限更新；超线性/对数无限级数由正文给严格尾界，数值截断与趋势不承担无限证明。原文主要承重页另外渲染目读。

文本抽取只在工作区使用，可复建：

```bash
mkdir -p tmp/comparison
pdftotext -layout research/comparisons/2026_08_gppa_nfb/sources/gppa_2608.01584v1.pdf tmp/comparison/gppa.txt
pdftotext -layout research/comparisons/2026_08_gppa_nfb/sources/nfb_2608.22687v1.pdf tmp/comparison/nfb.txt
```

## 本轮完成的一般模 GPPA 研究扩展

当前明确任务已完成：[统一中文入口](../../canonical/generalized_ppa_modulus.md)、[完整核三分支定理](gppa_nonlinear_kernel_theorem.md)、[物理提升及锐螺旋](gppa_physical_transfer.md)、[非线性完整严格例](gppa_strict_extension_examples.md)、[持续误差](../../canonical/gppa_inexact_modulus.md)、[集中完整稿](../../manuscripts/gppa_modulus/gppa_modulus.pdf)、[独立受检记录](../../audit/GPPA_MODULUS_RECEPTION_2026_10_09.md)和[复算](../../code/gppa_modulus/README.md)。C208–C214 新立身份，不覆盖 C199–C207 的正反比较。前述“统一 RL+真EB涵盖尚待核”现由固定核条件定理关闭；当前另见[C215改写合同](../../canonical/gppa_reformulation_boundary.md)与[C216正则化补充](../../canonical/gppa_regularized_stability.md)：源T4距离管/双极限包含已闭；任意改图/lift饱和类分离与全球先行性仍开放，实际范围见[有界审查](../../audit/GPPA_PRIORITY_AUDIT_2026_10_09.md)。
