# 随机与 Markov 的独立对象

[固定有限状态顶点证书](finite_state_certificate.md) 为原 C15 摘要补上同一同步 OT 残差的完整 LP 对偶 tight-edge 证明、精确零集与锐全域误差界；同页 [FS-HOFFMAN](finite_state_certificate.md#fs-hoffman) 是非锐备用证明，[C80](finite_state_certificate.md#fs-regularity) 另证 \(\Psi^2\) 连续分片仿射且全域 Lipschitz，**不需要**精确零集条件。调用 [惰性四循环](lazy_cycle_ot.md) 的具体常数前，先核其内层耦合仍为原成本的最优计划。两点翻转说明 C15 的误差界不能直接宣称动力收敛。

[固定目标全局近端的选择接缝](proximal_selection_seam.md)给出吸收律、非乘积二维图、有限长非不变极限及真实 \(W_2\) law-step 的局部 gauge 障碍。它使用**同一个目标函数的全局近端最小解**及指定 Borel 核。

[标量矩提升](scalar_moment_envelope.md)给任意连续非减 gauge 在硬支持下的最坏 \(L^p\) 凹包络和至多双点取等律；临界幂次的“分开聚合”损失是证书量，不是原生随机算法结论。进入实际随机近端前先证合法同耦合、支撑和目标边缘。

[全有限支撑律矩门与同一近极小 OT 回耦](moment_recoupling.md)把 C126 的 \(pq\le r\) 必要充分条件和 C127 的 \(D_\eta,\Delta_\eta\) 条件线性 EB 写成两个完整证明。前者的标量 \(c\) 不是同步成本 \(c_R\)；后者还需同一表示、同一目标、输入最优耦合、共同收缩和对趋近原 \(\Psi\) 下确界的损失界，不能仅凭核的收缩或条件刷新残差调用。

[四状态惰性循环](lazy_cycle_ot.md)在原同步 OT 残差中用最优运输的无交叉约束排除位移签名碰撞，得到精确零集与锐常数 \(\sqrt{13/p}\)；去掉输入 OT 最优性，同一核便出现假零点。它是 C15 固定有限数据框架的具体对象卡，锐常数另有直接证明。

[同核两种随机映射表示](lazy_cycle_representations.md#lcr-object) 固定四状态核与不变律，比较共同 Bernoulli 开关和四个逐状态独立开关的同步位移成本；[C88](lazy_cycle_representations.md#lcr-sharp) 给后者的锐平方系数 \(13/[p(7-6p)]\)。该差异属于表示相关残差，不改变 Markov 核。

[条件二次随机近端](../../canonical/random_proximal.md)的 C22/C23 使用随机切换二次目标与固定守恒边缘；[Markov 同步 OT](../../cone_markov.md)则使用另一个表示相关的残差 \(\Psi\)。新桥若改变核、目标、零集或残差，必须另立 Claim；只有同一对象与完整条件吻合才连接超边。
