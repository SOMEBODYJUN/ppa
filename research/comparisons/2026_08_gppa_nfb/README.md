# 2026 年 8 月 GPPA / NFB 与 PPA 的逐定理比较

此目录固定比较两篇外部原稿与本库当前数学身份。原文、版本指纹、逐篇审查和独立攻击分开保存，方便多人接续。比较基线为 `3dd02110d7666ba77b561bf2ab26641013a79fd3`。

**已完成的限定裁决：实质重合存在，全部涵盖不成立。** 先读 [COMPARISON.md](COMPARISON.md)，再按证明进入 [GPPA逐篇报告](gppa_review.md)、[NFB逐篇报告](nfb_review.md)、[独立攻击与交叉审查](independent_attack.md)。数学身份、附件对应及同问题/同轨道/完整算法/排除四层量词在 [BASELINE.md](BASELINE.md)。

| 本次可调用接口 | 证明与范围 |
| --- | --- |
| [C199](../../../CLAIMS.md#c199) | GPPA显式非线性核覆盖同一非单调自然子类全部普通轨道，并通过不变量恢复物理率；完整两个算法纤维不相等 |
| [C200](../../../CLAIMS.md#c200) | 完整cap及指定双支普通轨道无法由任何ASM核保持；不排mere-monotone无核正则性或任意lift |
| [C201](../../../CLAIMS.md#c201) | 任意合格同空间NFB拆分强迫原图固定二次锚；非退化自然类、cap、超线性、log原图均违反 |
| [C202](../../../CLAIMS.md#c202) | 非单调负恒等普通PPA与NFB完整同一；旋转和非零forward/memory实例亦有真实覆盖 |
| [C203](../../../CLAIMS.md#c203) | 标准full-graph primal–dual lift将同一必要二次锚压回原图；任意其它lift仍待核 |

物理几何点尾已蕴含有限长度，不能在覆盖子类单独作创新。结构/纤维正式稿的全球先行性另核，不因收敛子类相交被判重复。

## 比较对象

- [8/3 GPPA v1 原文](sources/gppa_2608.01584v1.pdf)：Le–Mordukhovich–Théra，arXiv:2608.01584v1。
- [8/24 NFB v1 原文](sources/nfb_2608.22687v1.pdf)：Pesquet–Roldán，arXiv:2608.22687v1。
- [来源、下载地址与 SHA-256](sources/manifest.json)：字节身份，不是证明验收。
- 本库 [C02-v2](../../rleb_ppa.md)、[C09/C10 一般模](../../canonical/general_modulus_dynamics.md)、[C191–C193 自然原图](../../canonical/support_normal_natural_class.md)及 [C137 完整几何尾图](../../canonical/selection_geometric_cap.md)。结构稿 C03/C04 与收敛稿分开比较。

## 已执行的判别与未闭门

1. 固定原关系、完整纤维、零集、步长与算法轨道；GPPA 的任意核、NFB 的任意合格同空间分解都须检查。
2. 重合须给出具体变换与全部适用条件；排除须给必要条件或完整反例，不能凭术语差异。
3. 分开外文已证明结果、本库直接推导、定位解释与尚未解决的先行性问题。有限长度若由点范数 R-linear 收敛直接推出，不能单独作创新标识。
4. 原文相关证明、边界模型、独立复算及交叉审查现已按三份报告的实际范围完成；根Claim、状态和依赖图登记限定结论。一般C191/C192核分类、任意其它lift、其它外文及全球先行性仍开放，不以source归档或有限PASS替代。

<a id="reproduce"></a>
## 可复现计算

三份脚本只用Python标准库，从仓库根运行：

```bash
python3 research/comparisons/2026_08_gppa_nfb/gppa_check.py
python3 research/comparisons/2026_08_gppa_nfb/nfb_check.py
python3 research/comparisons/2026_08_gppa_nfb/independent_attack_checks.py
```

结果分别在 [GPPA JSON](gppa_check_results.json)、[NFB JSON](nfb_results.json)、[独立精确结果](independent_attack_results.txt)。[集成复跑记录](verification.json) 保存执行环境、脚本哈希、原文指纹和退出状态。有限计算核常数、合法图点、线性/warped算法等式及SPD平方配方；任意核、任意拆分和无限轨道结论由正文证明承担。

文本抽取只在工作区使用，可复建：

```bash
mkdir -p tmp/comparison
pdftotext -layout research/comparisons/2026_08_gppa_nfb/sources/gppa_2608.01584v1.pdf tmp/comparison/gppa.txt
pdftotext -layout research/comparisons/2026_08_gppa_nfb/sources/nfb_2608.22687v1.pdf tmp/comparison/nfb.txt
```
