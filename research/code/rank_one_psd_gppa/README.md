# 秩一 PSD 候选的有限复算

对应候选正文：[rank_one_psd_gppa.md](../../candidates/rank_one_psd_gppa.md)。

从仓库根目录运行：

```bash
python3 research/code/rank_one_psd_gppa/verify.py --output research/code/rank_one_psd_gppa/results.json
```

依赖 Python 3 和 NumPy。固定 seed 为 20261013。任意矩阵右端的 SVD 三次逆检查 1000 个实例；完整物理圆管检查 4000 个实例，包含任意第二行方向。结果记录 Python/NumPy 版本、统一常数、恒等式最大误差、证书最大正超额以及采样比值。

另外检查核不可见第二行的明确反例、原目标二次下降失败见证、原点非 Lipschitz 比值、同目标普通 PPA 的正常收缩比趋一以及步长 4 的远输出门。参数根用数值多项式求根仅作解析结论复算，不由其授予完整根数证明。指数栏只是正文解析整数的算术，不是数值 degree 计算。

该验证器不证明一般全称条件、ENR 固定点指数接口或外部先行性。实际证明在候选卡中。
