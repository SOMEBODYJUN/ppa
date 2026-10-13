# 同一单点零集的严格／平坦完整 PPA 对照

运行：`python3 research/code/rleb_same_zero_set_countermodels/verify.py`（仓库根目录）。输出：`results.json`。

环境：Python 3.12.14，标准库；seed `20261013`。平行四边形和能量平方恒等式用有理多项式精确核对；601 个输出、5000 个点对、7 组各 3000 步前缀用 IEEE754 binary64 核验。反演最大相对误差约 `4.30e-16`。

算法：通过严格单调 `H(y)=y+F_flat(y)` 的二分反算取得完整唯一近端。零输入、正负输入、输出趋零、远端输入和跨符号点对都包含在有限测试中。极小输出时真实正位移低于 binary64 分辨率，结果文件逐行标注；舍入得到的比值 1 不能视为新固定点或渐近证明。

一般 coverage、全局反射界、全轨道收敛和任意同算法严格元组排除，由[候选卡](../../candidates/rleb_same_zero_set_countermodels.md)中的解析证明承担。该卡排除的是严格合取证书，不排除真 EB、RL 或经典凸 PPA。
