# 可独立调用的算法与算子例卡

本目录按**完整对象和残差坐标**开卡，不按历史 GX 编号决定数学身份。[EX01–EX03](../../canonical/example_atlas.md) 是先前重写的算子例；[正值正弦图](positive_sine_phase.md) 从 GX-064 分开临界全对模、非零目标 EB 与无零集路径；[身份与平方并图](identity_square_branch_union.md) 从 GX-068 分开真算子残差、指定步和完整步残差及跨支碰撞；[DR 切触与横截](dr_tangency_transversality.md) 是同一 Douglas–Rachford 算法残差 \(G=I-T\) 的两种几何机制。[对角线加离散竖支](diagonal_spike_relation.md) 从 GX-075 重算完整近端的每选择收敛、双真残差和全对跨支碰撞。[分段抛物映射](hemiregular_piecewise_parabola.md) 从 GX-076 分开两变量半阶、固定目标半阶与最近逆点线性模，且不将异维数映射强塞入 RL 坐标。[绝对值次梯度](absolute_value_subgradient.md) 从 GX-077 分开原算子残差跳跃与近端步残差。使用例卡时先核输入域、零集、全纤维和局部窗口，不把算法残差的模授给法锥和。

新对象另建短文件；旧卡新增属性时只在逐项证明后修正文及 Claim 身份。外部先行性和其余 GX 卡继续按 [覆盖审计](../../audit/SOURCE_RECONSTRUCTION_AUDIT.md)处理。

[身份与平方并图的两变量半阶](identity_square_branch_union.md#is-mr) 已补 GX-068 的完整正负目标窗 C92；同图 [二参数区域](identity_square_branch_union.md#is-semimono) C95 允许且只允许 \(\mu,\rho<0,\mu\rho\ge1/4\)，与 C89 的正 \(A\) 门不交。它们与最近逆点的线性律及全对 RL 碰撞并存。[闭球法锥](ball_normal_cone.md) 从 GX-067 重写锐投影反射、全图二参数区以及固定零目标真空 EB 与两变量逆像失稳；修改目标或域外残差语义时另立身份。

[有界平方图](bounded_square_minty.md) 从 GX-065 分开左端点的全图 Minty 相变、零点半阶真残差和正负两侧的实际路径；全图锐性见证在端点，两界在零点小窗仍可同用，但粗指数不构成收缩兼容。
[有界负恒等图](bounded_negative_identity.md) 从 GX-066 固定同一有界完整图的步长相变：\(\lambda=1\) 同输入多值，\(\lambda>2\) 近端收敛却反射扩张；路径结论始终逐步核自然输入域。
[斜旋转加盘法锥](skew_ball_inverse.md) 从 GX-058 的全部法向纤维证明完整逆像和两变量 MR 的全域锐半阶，并用同一边界射线核局部锐模；它的非零目标与原点局部线性命题须分开。
[斜等距加紧正对角](skew_compact_diagonal.md) 从 GX-059 给完整锐逆像、直接非 rectangular 见证和全域近端严格收缩而反射锐模 1；不依赖旧稿的外部等价引用。
[有界负平方图](bounded_negative_square.md) 从 GX-053 重算固定完整图的临界全对半阶、零目标真残差半阶与正侧有限步越自然域；两个锐性位置不同，不能拼成零点 PPA 收敛。

[Volterra 积分图](volterra_integration.md) 从 GX-060 分开全域极大单调和反射锐非扩张、逐初值强收敛、每个有限幂范数 1、以及真残差和步残差的统一消失 gauge 障碍；[伴随方向卡](adjoint_volterra.md) 从 GX-061 与 CCA-M10 核右端点逆像、完整近端和时间反射酉共轭，两方向只计一个等距不变量机制，旧目录其它属性仍须逐项裁决。[负三次图](negative_cubic_branch.md) 从 GX-054 区分完整近端的远支碰撞与受限图块的锐线性 RL，固定/两目标的 \(1/3\) 模来自已核正三次 EX03 的符号对应，图块合法非零路径则有限步离域。
[孤立零点极点支](isolated_pole_relation.md) 从 GX-055 区分连通定义域与断开的完整图、零输入纤维的步长门、任意幂真残差零下确界模和只有零路径可无限延续；严格近端 Lipschitz 模也不填补留域。[有理无理符号阶梯](rational_irrational_staircase.md) 从 GX-056 精确区分有理步长的单值不连续、无理步长的精确碰撞、全图锐 RL、原算子真残差与近端最小步残差。两例的“图点孤立”与“只限输入局部”不是同一个窗。
[负平方×阶梯的完整乘积](product_splice.md) 从 GX-057 按全对象重算 Euclidean 直积的残差、完整近端与临界半阶常数：两个分量的线性模可取最大，但完整乘积半阶锐系数严格超过临界图点输出窗的 2；只限输入窗也不同。它不是把 GX-053/056 两张卡的常数机械并列。
[负平方根短图与母图](restricted_root_graph.md) 从 GX-032 拆开两种完整关系；短图有锐全对常数和真二次 EB 却无第二步，母图另有远支及发散路径。

[平面旋转族](planar_rotation_family.md) 从 GX-062/063 和共同公式独立重算全部步长 Minty 纤维、输入对距锐 RL、循环阶门与两角的同逆像模差异；来源末句将族内循环阶说成不由强单调系数决定已由 C123/F34 修正。外部 Voisei 例号及优先性待一手核。
