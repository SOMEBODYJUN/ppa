# DD1–DD2 最终数学验收

**当前主任务进行中。** 逐题完成[作者原版最终验收协议](../topics/dd2/DD2_FINAL_ACCEPTANCE_PROTOCOL.md)的 §1–§17，交齐第九部分要求的资产，并用证据回答第八部分的 28 问和最终六问。原协议逐字节保留，是验收要求的唯一准绳。

在远端基线 `12ded0c` 上，[上一轮矩阵](DD2_TASK_ACCEPTANCE_MATRIX_2026-11-21.md)逐项审计的是[原交接稿](../manuscripts/dd2/DD2_outline_and_pro_handoff.md)的 P0–P3，共七条任务。其证据可用于新版协议的对应问题。矩阵没有 §1–§17 的逐问裁决，也没有交付第九部分的完整证据链。Git 和静态检验的成功只确认各自检查的范围。以下为逐节初诊，供接续者定位证据和缺口。当前尚无整节签收。

## 逐节初诊

| 节 | 已定位的证据 | 首要待验收义务 |
| --- | --- | --- |
| §1 数学身份 | [C400–C401](../topics/dd2/core.md)、[原 A/B](../canonical/ppa_ab_necessary_bounds.md) | 交出统摄版本的精确定理，核对 A、旧 $B_\omega$、新 $B_\Phi$、输出相对步长与同一步耗散的关系。逐条核 Hilbert 投影存在、截断、全边与选支覆盖。 |
| §2 一般函数补偿 | [一步精确几何](../topics/dd2/core.md#dd2-geometry)、[保留有符号模的几何](../topics/dd2/dual_eb.md#dd2-dual-envelope) | 统一有符号 $\Phi$、不连续及振荡模、平台的单侧反演、可行域为空、上确界不取到、比较迭代与整窗算子实现。固定尺度与整窗的充分、必要、充要分别证明。 |
| §3 恢复 DD1 | [C285](../canonical/rleb_sharp_linear_frontier.md#rsl-threshold)、[反向补偿](../topics/dd2/core.md#dd2-reverse)、[C411](../../CLAIMS.md#c411)、[C413](../../CLAIMS.md#c413) | 对齐 DD1 全部旧假设、反射换参、评价窗、步长和统一收缩。分别签收精确一步因子、严格下降边界、临界完整图和固定目标的动态范围。 |
| §4 收敛层级 | [距离、点与长度](../topics/dd2/core.md#dd2-trajectory)、[迭代边界](../topics/dd2/relaxation.md#dd2-adaptive-examples) | 给出带局部留域、停滞和集合识别量词的完整蕴含关系。特别核对不连续比较模、渐近正则、完整真残差和实际算法残差。 |
| §5 长度势 | [C401](../topics/dd2/core.md#dd2-general-gauge)、[非线性长度与耦合障碍](../canonical/ppa_nonlinear_gauge_and_coupled_obstruction.md) | 对原稿 F1–F3 逐条重构或指出断点。分清积分充分性与何种类中的必要性，核势的最弱正则性、振荡与对数模、有限长但不满足候选判据的例子，以及最优尾预算。 |
| §6 幂次分区 | [C399](../canonical/dd2_power_defect_finite_length.md#dd2-power-defect)、[常数与半阶见证](../canonical/dd2_power_defect_finite_length.md#dd2-power-witnesses) | 交叉验收 $q>1$、$q=1$、$q<1$ 与 $pq\gtreqless 2$，逐区给严格下降、可续、有限长、最优率和同量词取等或反例。C399 的正面定理范围为 $1/2<q<1$。 |
| §7 真实类扩张 | [C399 非单调例](../canonical/dd2_power_defect_finite_length.md#dd2-power-witnesses)、[C400 构造](../topics/dd2/core.md#dd2-trajectory) | 逐例验证完整预解式与真残差，对照旧 DD1、完整 RLEB 和经典路线的具体失效假设。补齐或裁决一般函数形状、非孤立零集、多值及非凸例的分离证据。 |
| §8 不可加强 | [F138–F143](../../FAILED_ROUTES.md#f138)、[双误差界覆盖反例](DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-coverage) | 把原协议的八个猜想逐条固定量词并匹配严格反例，重点核固定阶与有限长度的独立性及换松弛后的反例范围。 |
| §9 约化表示 | [C404](../topics/dd2/pppa_recovery.md)、[双残差剪切](../topics/dd2/dual_eb.md#dd2-dual-transfer) | 对照 Alcantara 原式逐项验收 $P=CC^*$ 的值域与闭性、非满射处的定义域和图等价、全核纤维、最近锚及二次版本回收。 |
| §10 Shadow 恢复 | [投影识别](../topics/dd2/pppa_recovery.md#dd2-pppa-recovery)、[二点恢复](DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-verification) | 按实际 shadow、投影与选择分别验收九类结论。明确非唯一纤维的极限集、最弱可验证条件、Hölder 两点长度与尾误差的界限。 |
| §11 双残差 | [C403](../topics/dd2/dual_eb.md#dd2-dual-envelope)、[近极小 lift](DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-coverage) | 补齐逻辑关系图、共同包络确实严格改善的完整原图、各模的传递及 DD1 和 Proposition 3.4 的逐式回收。 |
| §12 迭代分析 | [松弛与速率](../topics/dd2/relaxation.md)、[幂次长度和点率](../canonical/dd2_power_defect_finite_length.md#dd2-power-defect) | 给每种残差平均、点态、最佳迭代、实际点与距离率的精确适用窗。核复杂度、尖锐性及没有统一 A 时的保留结论。 |
| §13 自适应与非精确 | [C407 自适应](../topics/dd2/adaptive_parameter_audit.md)、[C406 真图扰动](../topics/dd2/inexact.md)、[P3 复核](DD2_P3_REVIEW_2026-11-21.md) | 核 $\alpha_k\to0$、逼近边界、超松弛与扰动联立时的可行域。分别完成真图、近似图和扩大算子的量词及保率、恢复或反例。 |
| §14 实际算法 | [CP/DR 应用](../topics/dd2/splitting.md)、[其他分裂固定步](DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md) | 对每个声称覆盖的算法逐一核原始问题、子问题覆盖、实际步、余项、两类变量的长度/收敛与相对已有定理的严格增量。只有固定步证书的范围按证书陈述。 |
| §15 先例恢复 | [C410 文献审计](DD2_P0_PRIOR_ART_2026-11-21.md)、[文献索引](../LITERATURE.md)、[DD1 先行核查](../novelty/DD1_PRIOR_ART_2026-11-20.md) | 逐一对旧 RLEB、Luke–Tam、Alcantara、Hölder/gauge、KL、Lyapunov 和 splitting 的同对象同窗条件作完整回收、特例或不可比较裁决。 |
| §16 新颖性 | [P0 先行性边界](DD2_P0_PRIOR_ART_2026-11-21.md) | 按协议 A–H 各自给出精确命题和独立证据，尤其核算子类严格包含、反向刻画及临界现象。有限检索只能支持其核查范围内的表述。 |
| §17 独立审查 | [Claim 身份总账](../../CLAIMS.md)、[旧矩阵](DD2_TASK_ACCEPTANCE_MATRIX_2026-11-21.md) | 为所有承重 Claim 逐条重构关键证明，执行原协议的 15 项攻击，登记确切反例、错误和未消除的致命异议。 |

## 已确认的主线缺口

- **有符号下界。** 固定 $t=1$、$\Phi(t)=1/4$、$\psi(s/\lambda)=s$。由锚定下界与 Cauchy–Schwarz，$1/4\le s(1-s)$，故 $s=1/2$。有符号能量给 $a\le 1/2$，中点构形取等。取 $D=[-\Phi]_+=0$ 后，旧包络为 $1/\sqrt{2}$。截断可以给安全放宽，但不会给原有符号假设的精确值。
- **不连续误差界。** 固定 $t=1,D=0$，取 $\psi(s/\lambda)=0$ 当 $s\le1/2$，其余为 $1$。原一维优化在 $s\downarrow1/2$ 的右侧趋向 $\sqrt{3}/2$，却无最大值。该侧的值满足准确几何的 $(1-s)_+\le a$，故即使保留最近点约束，也须处理上确界不取到。
- **幂次覆盖。** C399 在 $1/2<q<1$ 给出正面定理，已有 $q\le1/2$ 反例和 $0<q<1$ 的临界常数见证。协议要求的全分区、最优率和整窗构造须逐区提交证据。
- **低 $L$ 闭凸达到边界。** [C413 的证明](../topics/dd2/lowL_dynamic_sharpness.md#dd2-low-l-convex) 解决上一轮留下的可和链问题。任意有限维闭凸目标上，严格步长支逐步取等迫使锚不收敛。两支交界可有可和链，一般闭凸目标上的锚不收敛链仍待分类。

## 执行与完成判据

1. 按原协议的节号和题号维护本页的验收轨迹。先按主题定位既有证明；每个小问最终给出精确版本、正文锚点、证明或反例、适用域、独立审查及原协议第十部分的状态。已有证据能直接重构时引用即可。遇到缺口就继续推导、构造或攻击，不以补齐表格代替数学工作。
2. 每轮恢复、每个 checkpoint、准备结束前，都重新核对原协议。接着处理最早尚无实质证据的核心义务，直到需要改换路线时仍保持原命题身份。优先完成 §1–§6，再完成真实图验证、算法迁移、文献和全链审查。各步骤保留可恢复的 Git checkpoint。
3. 每个结论分别裁决。`Partial` 或 `Open` 必须写明已做推导或排除范围、精确剩余义务、障碍和下一条可检验路线，在相应证明义务上保持未通过。严格反例能够回答原问题时，裁决对应原命题为 `Refuted`。
4. 最终交付的停止门是 §1–§17 的每个小问已经得到有证据的数学裁决，第八部分逐问作答，第九部分交付物均可定位，并用证据回答最终六问。阶段 checkpoint、脚本通过和单个定理可成文均不能触发全任务完成声明。确有客观阻塞时保存进度并报告为中途状态，明确未完成的题号及还能推进的部分。
