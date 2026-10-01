# Research State · 2026-10-01

## 当前新增前沿：规范层继续生长

当前远端基线为 4bd3290。本批将 9/09 两份来源按**数学单元**重写为 [合法路径](research/canonical/path_atlas.md) C31–C33 和 [复合次正则](research/canonical/composite_subregularity.md) C34–C37；[逐单元去向](research/audit/UNIT_DISPOSITIONS.tsv) 明记哪些旧节被改写、哪些仍未审。历史 C11 复合任务与现 C11 极限回缩保持不同身份。两条新链都可以供未来研究调用，但不宣称旧文件全覆盖或文献新颖性。

路径链的承重条件是每条实际选择的前缀延拓、统一终点收缩、可求和的**块内**位移及初值边界预算。旧札记的无限词逐词幂条件缺统一余量，非平凡周期也不能从整轨道有限总长定理推出；[F12](FAILED_ROUTES.md#f12) 给反例。下一步从原生多值广义方程重核 M1 的合法分支、两步捕获半径和“每条/存在”量词，完成后才能给实例升级状态。

复合链的承重条件是满行秩修复、凸链式规则和真实残差外层 EB 的合取；局部 PPA 还要全部乘子界、步长、gauge 兼容和留域。[F13](FAILED_ROUTES.md#f13) 的秩亏例阻止无条件传递。下一步研究带原生非抵消条件的秩亏版本，先重算历史真多值分支与振荡弱分离例，再核外部定理先行性。任何新结果按 [增长协议](RESEARCH_PROTOCOL.md) 直接进入正文及新 Claim 版本，不需等历史区清空。

数学定义、精确命题与来源分别见 [foundations](research/foundations.md)、[CLAIMS](CLAIMS.md)、[SOURCES](research/SOURCES.md)。数学状态以本仓库的精确证据为准。
## 活跃目标 A：RLEB–LT–极大单调的总体规模比较

**Exact gap**：给自然、参数中立、保留完整原图与真实残差的对象空间 \(\mathfrak X\)，明定计数单位 \(F\) 或 \((F,\lambda)\)、合法选择及局部域量词，再选一个不把目标类一齐压小的大小不变量 \(\mathcal I\)，证明同一母空间中 RLEB、LT 公共 all-pairs 和极大单调类的规模关系。当前没有该总体定理。

**已知组件**：完整全域 \(T=J_{\lambda F}\) 的图反演；匹配接口下 LT→RLEB 能量证书；固定紧 T-only 图卡 \(\Phi=(w,m)\) proper；有受限严格分离构造。均不能单独解决总体问题。[operator_space](research/operator_space.md)

**承重障碍**：

1. proper/quotient 不推出 category-preserving；单一局部 \(T\) 观测不保全局 \(F\) 和 \(r_F\)。
2. 9/21 总账报告 N05/N08/N10 的共同塌缩与 N09 远端自由度；其中 I-097–099 原孔隙审计及 I-102 正式表示稿未在当前盘点的原件名中发现，保留“来源包报告”而非重构证明。
3. 同时，9/21 旧 SOURCE-MISSING 是**当时**状态：I-001 已恢复 100/101 的历史展开内容（受限第三方 PDF 未入库）；I-002、I-003–005、I-059 已恢复；I-075 的 73 文件专题包以展开内容恢复，原重复 ZIP 未保留。I-005 实为审计**任务书**，不能当审计通过记录。解选择的实际修补证据在 I-059 内 revision_math_audit 与 revision_math_closure。

**下一判别**：写一页 \((\mathfrak X,\mathcal I,\mathcal R,\mathcal L,\mathcal M)\) 规格，先找 N05/N08/N09/N10 的反塌缩反例；若量尺共同塌缩，换表示或不变量，而非在特殊层追加成员例。

## 活跃目标 B：局部 RLEB 与结构稿的精确边界

- **S19 局部 PPA**：coverage + 同图块全对 RL + 真实输出 EB + gauge 兼容 + 留域，给有限长及尾界；一般模还需 Dini。该组合的缺一条件不能静默删除。[R01–R04](research/rleb_ppa.md)
- **9/19 新资产**：对数二支完整图 \(a\le1\) 显示几何距离收缩而切向漂移发散；\(a>1\) 收敛。统一尾与同图块全对连续性给局部极限回缩。这使“任意紧零集可实现”和“额外收敛条件下零集为邻域回缩”形成可检验的条件限制。[H04/H05](research/holder_structure.md)
- **9/19 随机措辞**：原稿写 Polish，证明用给定 \(d_{\mathsf X}\) 完备；\((0,2)\) 上的确定性序列满足其他假设却收敛到空间外。原命题若按拓扑 Polish 解释为假；修订版本明确 complete metric。[H06](research/holder_structure.md)、[FAILED F07](FAILED_ROUTES.md)
- **S23 全局结构**：同一个强单调双 Lipschitz 影子及有限维完整纤维分类的证明已局部独立重算，未见内部计算致命断点；经典 Hilbert 扩张、有限维 degree 的调用及同对象先行性仍是独立门。固定维数的最优因子仍开放。
- **S23 值域与有限数据**：最大根定位给全局与相对 maximal 窗口的**整个纤维**锐覆盖；有限兼容样本的 QP 给全局一致 \(A_m\)，但未知图点只在 Cayley 参数覆盖下认证。可验证 gap、噪声和求值误差叠加成三项界；有限总查询在无界 Hölder 类不能全空间认证。[range_finite_data](research/range_finite_data.md)。这条链原八条 Claim 未记录，现立 C18–C21。
- **S25 局部值域**：指定 \(T\) 可以是完整 resolvent 的子关系；有限数据包络和整窗 usc/Čech-acyclic/topological 条件是不同层。Theorem 8.1 的外部引用 [6, Theorem 6.2] 需逐条核适用条件，当前为 PDF-only 候选。[H07](research/holder_structure.md)

## 独立旁支与依赖门

| 链 | 当前可使用的精确成果 | 不得越过的门 |
| --- | --- | --- |
| 锥 | nice + 冻结 CRSC 的秩夹逼、面稳定，参考面 amenability 与法向/切向修正给 MSCQ；nice 非 amenable 的普遍量词边界 | 原锥残差到 \(r_F\) 的桥、同一零集、反射和 coverage 另证；文献正式版优先权待核 |
| Markov | 紧连续同步 OT \(\Psi\) 的 exact-zero⇔一般 gauge；有限状态顶点测试⇔线性 EB；条件 bit/Gaussian 修复 | 表示依赖、同耦合、守恒边缘、recoupling；不能由快收敛反推原 \(\Psi\) EB |
| 解选择 | 统一尾 + 局部 Hölder → 对数/超几何极限模；完整显式例的两点非 Hölder | 只对 \(J_{\mathcal G}\) 直接导入；完整 \(J_F\) 须全纤维一致；经典 AGM 先例已覆盖较宽现象 |
| 不一致随机近端 | 固定守恒边缘与活跃均方谱隙给条件 \(W_2\) 收缩、完整混合核 law-step 的线性 EB 和有限长度；逐分支残差的零集则是共同定点支持律，标量例使统一 EB 系数锐 | C22/C23 的证明和反例在 [RP 模块](research/canonical/random_proximal.md)；不改成普通联合 \(W_2\)、同步缺陷或物理步长；外部优先权、无限维/变参数仍待审 |

各链的定义、量词与反例在 [cone_markov](research/cone_markov.md) 和 [solution_selection](research/solution_selection.md)。

## 证据与下一阶段

现有独立工作只对各模块明确标注的公式、证明链和反例进行了重算；未逐行 referee 全部 251 个来源记录，也未完成外部文献精确适用条件与全球新颖性。历史 HTML/JSON 的 35 条边是搜索种子；当前 76 条边经版本和范围重组，数目不是数学质量指标。数值代码和审计 PASS 仍保持原证据层。

**覆盖边界**：原件 251 个、ZIP 11 个及成员 178 个已清点，其中 41 个成员与展开件字节相同；这不是数学验收数。新增 14 个逐单元去向仅覆盖 C31–C37 所列章节；GX 余项、随机其他支线、M1 具体常数、复合真多值/振荡例均保持待核。十个历史验证器的退出码与环境记录在审计 JSON，不能证明一般命题。
**例库首批**：C24–C26 的 EX01 旋转、EX02 正紧对角、EX03 三次映射已给完整对象、真实残差和直接证明。尤其 EX02 排除任何趋零 gauge 的统一局部 EB，却保留每个初值的 PPA 强收敛；EX03 将固定目标常数 1、两变量 \(2^{2/3}\) 与算法残差下确界 \(\lambda^{-1/3}\) 分开。此三例只关闭对应 GX-004/009/021 的本轮数学单元，原卡其他性质和其余 GX 尚待重写。

**定义/参数首批**：[PD 字典](research/canonical/parameter_dictionary.md)重写了全对/锚定、全图/图块、coverage/exclusion、同图换步、线性 RL tied 曲线、有界尺度指数及真残差方向，C27–C30 分别固定数学身份。若要比较不同步长，先核新 Minty 输入 \(Q(D)\) 的单射与 coverage；若要把选中步界写成真 EB，先核全纤维最小残差的方向。这些是当前可直接复用的基础，旧 checkpoint 的完整定义和全部示例尚未逐项关门。

下一阶段先补证据门：追 I-097–099/I-102；核 9/25 [6] 原文；正式修随机完备性；再让总体比较的一个精确空间/量尺接受反塌缩攻击。若没有新证据，不新增“已证”节点。
