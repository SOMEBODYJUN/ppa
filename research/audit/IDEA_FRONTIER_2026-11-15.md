# PPA/GPPA idea frontier · 2026-11-15

本索引对应仓库 main@54991cf，当前稿件入口为 发表成果整理/RLEB/README.md。它记录本轮实际接收、去重和淘汰的候选，供下一次会话恢复；candidate 不等于定理，major-potential 不等于已达到四大期刊标准。

## 待深挖主线

| ID | 精确问题 | 状态 | 最接近旧项 | 决定性下一步 |
|---|---|---|---|---|
| C307 | 强对数凸总权重下，\(\sum M_{j-1}/M_j\) 的准解析分界是否对所有 \(\lambda_k\in[\lambda_-,\lambda_+]\) 保持；非准解析侧能否对每个 schedule 和任意紧连通 \(K\) 构造 schedule-specific 的完整 global-min PPA | candidate / major-potential conditional | C302 固定步；C297–C299 固定算法 | 先闭任意两步周期、任意 \(K\) 的 Whitney/Beurling 插值与统一 Hessian margin；再攻任意振荡 schedule |
| C308 | 周期 SPD 变度量 PPA 在 monodromy multiplier 1 时，离散中心流形首个非零高阶 jet 是否给出收敛/排斥/单侧逃逸的 sharp 判据 | candidate / major-potential conditional; second line | C284/UI33 线性旋转发散；现有二维 Jury 相图 | 写出一般周期 cocycle 定理、非线性强单调全局例和 finite-order/flat remainder 条件；不能声称“所有系数为零必周期” |

## 本轮已去重或淘汰

| 候选 | 处理 | 原因 |
|---|---|---|
| O(n) 等变径向临界步长—球面分岔 | 保留为条件性备选 | 局部 Hölder、球面固定集和指数计算成立，但若只做径向逆函数分类偏增量；需类级全局纤维/指数/非径向稳健性 |
| 连续非乘积 proximal-Gibbs 的 JSR ⇔ law-level EB | 淘汰 | 三点有限状态 Ising 可有有限维残差 EB 而绝对影响矩阵谱半径大于1，否定原 iff；可另改 signed influence，但那是新题 |
| 多值 GPPA 吸引指数—原值域鲁棒桥 | 淘汰为主贡献 | 一般 acyclic/CAC/Lefschetz 固定点理论已覆盖拓扑部分；连续非单射核下的图值 degree/值域球量词未闭，C05-v2 仍是最近条件结果 |
| 有向网络博弈 Perron 三分界 | 淘汰 | 两节点 PPA 特征值遗漏了整体因子 \((1+\lambda)^{-1}\)，因此 \(\kappa=2\) 的 period-2 阈值错误；一般图还需全谱而非 Perron 半径 |
| Bernstein 非幂矩阵图 completion | 与既有结果重复 | research/canonical/unified_ppa_coverage.md 的 UC-EXT 已有 Bernstein 表示、Schoenberg/Kirszbraun 扩张与 graph-maximal 判据 |
| \(L^p\) Jung 常数影子半径 | 淘汰 | 候选 \(J_{\rm rel}(L^p)=\max\{2^{1/p-1},2^{1-1/p}\}\) 在 \(p=4\) 已超过可行外接半径；\(E_X\) 也未固定规范和强单调类 |
| 周期标量步长的二维 hypomonotone 乘积 | 不进入队列 | 可交换复数 resolvent，公开 variable-step 机制已覆盖，增量不足 |

## 当前判断

C307 是本轮最有希望改变论文主贡献的候选，但其反向构造尚未证明；C308 有精确根式的非线性中心系数，是可并行的第二主线。若 C307 的两步周期门失败，优先转向 C308 的 PPA-specific Floquet theorem；若两者均不能闭合，应诚实保留本索引并报告未找到已独立审查的四大级结果。

