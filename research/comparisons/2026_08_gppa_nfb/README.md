# 2026 年 8 月 GPPA / NFB 与 PPA 的逐定理比较

此目录固定比较两篇外部原稿与本库当前数学身份。原文、版本指纹、逐篇审查和独立攻击分开保存，方便多人接续。比较基线为 `3dd02110d7666ba77b561bf2ab26641013a79fd3`。

## 比较对象

- [8/3 GPPA v1 原文](sources/gppa_2608.01584v1.pdf)：Le–Mordukhovich–Théra，arXiv:2608.01584v1。
- [8/24 NFB v1 原文](sources/nfb_2608.22687v1.pdf)：Pesquet–Roldán，arXiv:2608.22687v1。
- [来源、下载地址与 SHA-256](sources/manifest.json)：字节身份，不是证明验收。
- 本库 [C02-v2](../../rleb_ppa.md)、[C09/C10 一般模](../../canonical/general_modulus_dynamics.md)、[C191–C193 自然原图](../../canonical/support_normal_natural_class.md)及 [C137 完整几何尾图](../../canonical/selection_geometric_cap.md)。结构稿 C03/C04 与收敛稿分开比较。

## 需要完成的判别

1. 固定原关系、完整纤维、零集、步长与算法轨道；GPPA 的任意核、NFB 的任意合格同空间分解都须检查。
2. 重合须给出具体变换与全部适用条件；排除须给必要条件或完整反例，不能凭术语差异。
3. 分开外文已证明结果、本库直接推导、定位解释与尚未解决的先行性问题。有限长度若由点范数 R-linear 收敛直接推出，不能单独作创新标识。
4. 原文相关证明、边界模型和计算复核完成后，汇总结论并更新根研究状态；当前源文件检查点不代表比较已验收。

文本抽取只在工作区使用，可复建：

```bash
pdftotext -layout research/comparisons/2026_08_gppa_nfb/sources/gppa_2608.01584v1.pdf research/comparisons/2026_08_gppa_nfb/sources/gppa_2608.01584v1.txt
pdftotext -layout research/comparisons/2026_08_gppa_nfb/sources/nfb_2608.22687v1.pdf research/comparisons/2026_08_gppa_nfb/sources/nfb_2608.22687v1.txt
```
