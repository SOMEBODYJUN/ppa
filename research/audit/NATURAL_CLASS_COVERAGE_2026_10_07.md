# 支撑函数与法锥来源：全部528 LF的实际枚举与重构

<a id="sn-audit"></a>
本记录只覆盖下面一个固定内容组，不宣布全库来源或全部研究地基完成。2026-10-07实际完整阅读原件528 LF，重构[规范正文](../canonical/support_normal_natural_class.md)，对实质断言、证明、例子、应用解释、文献报告、旧执行及组织项给出明确去向。没有读取历史聊天，没有新增附件或外部原件，没有通过旧VERIFIED标签导入外部定理。

| 项 | 固定值 |
| --- | --- |
| source_locator | history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/05_实例与反例/支撑函数与法锥_自然类推导.md |
| 字节数 / LF | 23025 / 528 |
| SHA-256 | abe082412883506ab76bdcc2b653f7971ecacb82205dd7cbe632186c84e8c2c9 |
| 完整覆盖 | 1–528，无重叠、无遗漏；141个去向行，包含独立标记的排版间隙 |
| 原子表 | [NATURAL_CLASS_UNITS_2026_10_07.tsv](NATURAL_CLASS_UNITS_2026_10_07.tsv) |
| 注册范围 | NATURAL-CLASS-full；由父级写入共享范围注册表，构建器不生成注册表 |
| 可复现构建 | python3 research/audit/NATURAL_CLASS_BUILD_2026_10_07.py |

原子表直接保存所覆盖LF的原文，不只保存摘要。构建器核定源hash/字节数/LF数，并验证全部行恰好按连续不相交区间分配。行数不是独立成果数，也不是全库清洗率；enumerated-with-dispositions不把deferred的文献、应用或旧执行改成数学验收。

## 已完成的直接数学

- C191-v1固定紧凸支撑集合、完整法锥与非对称强法向恢复矩阵，重建全部原图、全输入唯一完整近端、全活动面对的RL、完整真残差EB、严格聚合半径、独立全域有限长度及圆盘/多面体实例。支撑面、凸近端和正常锥逆都由本页投影/最小化/几何Cauchy级数证明。
- C192-v1固定反馈原图，恢复小载荷双侧条带上的完整纤维唯一性及全部输入对常数。另由同一原方程的标量中间值论证补出全输入非空紧纤维；给三输出反例阻止全域唯一性的扩大；对完整全部选择直接证明全域有限长度。
- C193-v1准确固定二次锚不等式SN17，证明非退化A与B在每个解图邻域失败；最大局部RL指数为α，不calm。退化A的C={0}却有1-Lipschitz完整投影、τ=0证书。光滑筛选的独立辅助引理补出双侧局部逆量词和初等Lipschitz证明，不认证任意KKT模型。

父级与一个独立子代理已读全文直接复算；子代理接受A/B纤维、RL、真EB、全选择长度、三输出反例及C193边界，指出的SN13 quad拼写已修。最终空白接收由父级另行记录，本页不预写其尚未返回的判断。外部新颖性、历史代理是否实际执行、工程身份都独立保留。

## 精确修订与新增认识

| 原源位置 | 断点 / 精确门 | 当前处置 |
| --- | --- | --- |
| LF21；对照LF59与LF121 | 摘要一概说两类排除固定旧锚证书，但A允许C={0}；原定理A第6项正确携带C≠{0} | C193明写非零门。C={0}时F(t,0)={0}×R^r，完整J(p,ξ)={(p,0)}，反射为(p,−ξ)；SN17用V=0、τ=0≥0成立 |
| LF429–441 | 证明选择非零w∈C，必须携带该可行性；不能据名称排除任何未定义旧证书 | 保留明确SN17的全部图点量词；只排除固定有限残差二次项，partial/变参数类另核 |
| LF338与LF375 | 原证明只在θ<1条带保证唯一；不能扩大为全输入唯一 | C192用标量IVT补全域存在，三输出同输入例否定全域唯一。新增推导单列，不当作原稿已写出的结论 |
| LF397–404，特别400 | 完整双侧输入允许y0<0，0≤y1≤ky0不可能 | 修为0≤y_{j+1}≤k(y_j)_+；负初值一步到零载荷后驻定。全域完整存在使每种选择可无限延续 |
| LF449 | 反馈B只在t冻结时有法向单调结构；不自动具有联合全对退化度量单调性 | 以a(t1)=1、a(t2)=9、y1=2、y2=1给法向配对−7；只调用实际法向更新与切向步长界，不导入未定义PSM命名 |
| LF455–457 | 局部单值逆若只读成右逆，不能推出J(G(u))=u | 辅助引理明确双侧局部逆与同一局部零流形；直接证明DG(p)可逆和局部Lipschitz |
| LF388的J_F/Q_F | 源步长λ一般正数，不能混成单位步长记号 | 规范统一完整J_{λF}、单点输出T和Q=2T−I；RL(λ,α,L;δ) |

## 仍未结案的具体单元

来源LF27/29/31/33及LF473–475报告Carpick、Gfrerer–Outrata–Valdman、Carstensen、Kanno原文或摘要。此次未重新取得和读取原页，故这些paper facts、确切公式/版本及所谓构件自然性保留source-report/deferred，不是新正文定理的承重输入。

LF37–44、417、480、528的完整接触/塑性/PDE身份仍需选定一份不改方程的实际模型，并核变量、量纲、边界条件及所有耦合。LF461–468、476–479和合同中旧访问/审查/执行字段仍属来源报告；本次精确重算常数不回溯认证旧程序运行。没有把新原件或附件需求写成已完成的数学。

## 已集成身份与边界

本范围已经接入共享Claim总账、E309–E323、[范围登记](ATOMIC_SCOPE_REGISTRY.tsv)及[逐单元去向](UNIT_DISPOSITIONS.tsv)。下面三张身份保留原始来源的修订原因。

| Claim | 精确主身份与可调用锚 | 当前状态 |
| --- | --- | --- |
| C191-v1 | SN-A-COMPLETE；[sn-triangular](../canonical/support_normal_natural_class.md#sn-triangular)、[sn-compatible](../canonical/support_normal_natural_class.md#sn-compatible)、[sn-direct](../canonical/support_normal_natural_class.md#sn-direct) | derived-checked，仅固定原生数学关系及完整证明 |
| C192-v1 | SN-B-COMPLETE；[sn-feedback](../canonical/support_normal_natural_class.md#sn-feedback) | derived-checked；全域存在/全选择长度和小条带唯一/RL分开 |
| C193-v1 | SN-ANCHOR-BOUNDARY；[sn-failures](../canonical/support_normal_natural_class.md#sn-failures) | derived-checked；A必须C≠{0}，SN17准确命名，C={0}为明确例外 |

实际合取关系按E309–E323登记；其承重点为：

1. SN-OBJECT → SN-A-FIBERS（完整法向逆、支撑面凸近端及全部图值合取）。
2. SN-A-FIBERS ∧ SN-SUPPORT-COMPARE → SN-A-RL；SN-OBJECT ∧ f∉D → SN-TRUE-EB。两条独立证书不能合并参数d_D/R_D。
3. SN-A-RL ∧ SN-TRUE-EB ∧ SN-MATCH → C185/R02的完整局部实例；scope保留同δ/r、完整零锚、实际gauge、coverage/留域。
4. SN-A-FIBERS → SN-DIRECT-TAIL，不以SN-MATCH为前件。
5. SN-B-OBJECT → SN-B-FULL-EXISTENCE；再加θ<1、同E_Q条带 → SN-B-UNIQUE-RL；不得将后一边写成全图。
6. SN-B-FULL-EXISTENCE ∧ 原图逐选择更新界 → SN-B-ALL-TAIL；全局三输出反例的refutes目标应是新错误节点“B全域单值自动成立”，不指向已带θ<1门的结果。
7. SN-OBJECT ∧ A的C≠{0}（或B半直线） → SN-ANCHOR-FAIL；退化C={0}节点limits无门的摘要，不反驳C193。

该hash组现已登记完整枚举且有去向；外部/应用/执行deferred仍保留。表有精确Claim、目标锚、理由和剩余义务；原件未改。圆盘τ≥0解析轨道的后续恢复见SN-CIRCLE，已独立复算。
