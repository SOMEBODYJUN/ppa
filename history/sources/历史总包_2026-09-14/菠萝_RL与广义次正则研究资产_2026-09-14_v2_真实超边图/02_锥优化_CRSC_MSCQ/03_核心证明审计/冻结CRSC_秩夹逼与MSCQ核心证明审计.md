# RL-CONIC-2026 — PA-CORE 核心证明逐项审查

日期：2026-09-09。论文族：theoretical。受审阶段：T4/T5 proof gate。任务：PA-CORE。

## 1. 范围、证据与结论

结论：**所指定三条核心链均为 PROVED；未发现需要新数学论证才能补齐的 GAP。** 有五项 NEEDS_REPHRASE，涉及正式定理包装、量词展开和标准局部约化的准确含义。建议 `PASS_CANDIDATE`，最终阶段验收仅属主控。此结论不是新颖性认证、机器形式化证明或投稿通过判断。

本审查使用 SCI-Skills pre-submission-review 的证据/严重度分离规则；没有修改原正文或前次审查。已完整读取：

- `output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md`，以下简称 M，416 行，SHA-256 `0e675fe1aae0b9a2838f25681ae2354461792d5dd3c32fbd77cf3ab726756c37`。
- `output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md`，以下简称 A，490 行，SHA-256 `51607d371b73a6b400a6cf704f130f267be30e499a9ba85e51205223e997284b`。

原始来源直接复核限于：Pataki 原文 Theorem 1.1(ii)/(iii) 与 Proposition 2.1；CRSC 作者公开稿 Definition 3.2、Proposition 5.2、Theorems 5.1–5.2；Lourenço 的 Definition 8 与 Proposition 13。未重新核查世界优先权、完整反例构造或所有应用例。

证据标签：原文件内容为 `VERIFIED_USER_MATERIAL`；上述原始文献定位为 `VERIFIED_SOURCE`；以下证明重建及数学裁定均为 `AI_INFERENCE`，不是外部定理认证。

| 核心命题 | 精确定位 | 裁定 | 主要风险检查 |
| --- | --- | --- | --- |
| 冻结 CRSC ⇒ 两个固定子空间秩相同 | M §3，49–82；A §3，47–83 | PROVED | Pataki 为精确锥像等式；秩半连续方向正确 |
| 冻结 CRSC ⇒ A1/A2 于一个完整邻域成立 | M Thm 4.1，88–121；A §4，105–154 | PROVED | 未先假设附近闭像；非可行点也涵盖 |
| 冻结 CRSC ⇒ 局部非线性面约化 | M Lemmas 4.2–4.3、Cor 4.4，125–192；A §6A，314–364 | PROVED | 控制投影锥闭包；固定公共流形；无 A1/A2 循环 |
| nice + 参考最小面残差性质 ⇒ MSCQ 与显式上界 | M §5，198–238；A §6，245–308，§6A，368–392 | PROVED | 两次修正在同一输入空间；路径统一缩邻域 |
| proper nice 内 amenability ⇔ universal apex C1-CRSC ⇒ MSCQ | M §7，314–325；A 403–409 | PROVED | 反向测试所有面；常数可依赖面/映射；齐次化正确 |

## 2. 冻结设定与 imported theorem 检查

取有限维 Euclidean 空间 X、E，闭、凸、尖、满维锥 C，开集 V 上的 C1 映射 G，且 G(x̄)=0。记 A=DG(x̄)、F=Fmin(range A∩C)、H=F⊥、S=span(C*∩F⊥)。所有正交补、秩和奇异值使用已给定 Euclidean 内积。CRSC 是 **x̄ 处** A*C* 闭，加上 **一个 x̄ 邻域全部点** 上 rank(DG(x)*|H)=rank(A*|H)=r。

`range A∩C` 是非空凸锥，取其相对内点即获得属于 ri F 的线性化可行像。因此 F≠{0} 时存在 d̄，Ad̄∈ri F 且 Ad̄≠0。有限维性不可省略；不需要该交集本身就是面。

Pataki 的原始定理明确给出 A*F△=A*F⊥ 为闭像的必要条件；当 C*+F⊥ 闭时也是充分条件，并等价于严格核乘子与像交等式。全锥 niceness 保证其局部再应用时的充分性；这里不是把闭包等式误读为精确像等式。[Pataki, Theorem 1.1 与 Proposition 2.1](https://optimization-online.org/wp-content/uploads/2006/12/1556.pdf)

作者稿的冻结面 CRSC 与 M 的设定对应，且其 Theorem 5.2 把 A1/A2 写成整邻域假设；在当前读取版本中确实提出删除这些假设的问题。此项只验证命题接口，不能据此推断截至今日仍无后续解决。[CRSC 作者稿，Definition 3.2、Theorems 5.1–5.2](https://www.ime.usp.br/~ghaeser/crsc-redcones.pdf)

## 3. PROVED：秩夹逼及 A1/A2

### P1. 固定子空间秩夹逼

定位：M 67–76；A 56–83。

由 A*F△=A*H，取线性张成得 A*S=A*H。由于 S⊂H，rank(DG(x)*|S)≤r；参考点的 r 阶非零子式在一个邻域中保持非零，故反向不等式成立。r=0 时无需子式。两像具有包含关系且同维，因此 DG(x)*S=DG(x)*H。没有用到 x≠x̄ 处闭像，因而没有循环。

### P2. 严格乘子和线性化最小面的统一稳定性

定位：M 97–110；A 105–138。

F 为真面时，nice ⇒ facially exposed；F△ 为非零锥，且 C* 尖，所以 ri F△ 中的 Y0 非零。Pataki 给出 Y0∈ker A*。固定 S 内的常秩核正交投影连续，因此

Y(x)=Pker(DG(x)*|S)Y0 →Y0，且 Y(x)∈S。

ri F△ 在 S 中开；一个固定球包含于 ri F△，故在同一缩小邻域内所有 Y(x) 都为严格乘子。对 v∈range DG(x)∩C，⟨v,Y(x)⟩=0。因为 Y(x)∈ri F△，任意 y∈F△ 都可用 Y(x)−εy∈F△ 进行检验，得到 ⟨v,y⟩=0；因此 v∈F△△=F。这补全 M 103 的暴露面推理。

F≠{0} 时投影 d̄ 到 ker(P_HDG(x))，连续性保证 d(x)→d̄。像 DG(x)d(x) 始终位于 span F，并收敛到 ri F 内点。因此进一步缩小同一个邻域后，所有这些像均属于 ri F。包含关系加上 ri F 交点，恰好推出附近最小面等于 F，而不只是包含在 F 内。

F={0} 时上面的包含关系已足够。F=C 时取一个固定严格线性化方向 d̄；其像在 int C 中的正半径球可统一保留。

### P3. 附近闭像 A1

定位：M 112–121；A 140–154；满面分支 M 95。

P_SDG(x) 与 P_HDG(x) 的核具有包含关系且秩相同，故核相等。于是对任何表示为 DG(x)d 的向量，其在 S⊥ 内当且仅当在 H⊥=span F 内。这给出 Pataki 的第二项。P2 已先识别 **同一 F 确实是 x 处最小面**；再与 Y(x) 合用 Pataki，即得 DG(x)*C* 闭。不存在先用 A1 推 A2 再倒推 A1 的循环。

满面分支中的“bounded dual lifts”也可直接补成三行：取 δ>0 使 B(DG(x)d̄,δ)⊂C。任意 y∈C* 满足 δ||y||≤⟨DG(x)d̄,y⟩=⟨d̄,DG(x)*y⟩。若 DG(x)*y_k 收敛，则 y_k 有界；取收敛子列得到闭像。固定 d̄ 和缩小后的共同 δ 对整个邻域有效。无需假设 DG(x) 满射。

## 4. PROVED：公共法向流形及常数 b

### P4. 关键分离对投影闭包成立

定位：M 125–139；A 316–323。

设 U=range(P_HA)、D=cl(P_HC)。若 u=P_HAd∈D，则任意 y∈F△ 满足 ⟨u,y⟩≥0。任取 h∈H，由 **精确**像等式选 y_h∈F△ 使 A*y_h=A*h，于是 ⟨u,h⟩=⟨u,y_h⟩≥0。对 −h 单独重新选择乘子，得到反向不等式。因 u∈H，最终 u=0。

这里既不要求 h↦y_h 连续，也不要求同一个 y 同时服务 h 与 −h；不要求 P_HC 闭。D 本身闭，故当 r>0 时，U 的紧单位球面与 D 分离，η=min{d(u,D):u∈U,||u||=1}>0。

### P5. C1 坐标图、纤维独立与法向修正

定位：M 141–182；A 327–362。

令 φ=P_HG，N=ker Dφ(x̄)。映射 Θ(x)=(P_Uφ(x),P_N(x−x̄)) 的微分把 N⊥ 同构至 U、把 N 恒等映至 N，故可逆。其局部 C1 逆 θ(u,z) 可限制到以 (0,0) 为中心的凸乘积小球 Q_U×Q_N。

恒等式 P_Uφ(θ(u,z))=u 保证该复合映射的秩至少 r；CRSC 又使 φ 的秩恰为 r。故 φ∘θ 的全部 z 导数为零。每条 z 纤维连通，剩余 H∩U⊥ 分量只依赖 u，写成 β(u)。由 G(x̄)=0 和 range Dφ(x̄)=U 得 β(0)=Dβ(0)=0。

参考点处 ||D_uθ||=1/σ，其中 σ=σmin+(P_HA)。C1 连续性允许统一约束 ||D_uθ||≤2/σ 与 ||Dβ||≤η/2。沿 (tu,z) 积分可得

\[
\|\beta(u)\|\le(\eta/2)\|u\|,\qquad
d(\phi(x),D)\ge d(u,D)-\|\beta(u)\|\ge(\eta/2)\|u\|.
\]

取 x̂=θ(0,z)，则 x̂∈M={φ=0} 且 ||x−x̂||≤2||u||/σ。对每个 c∈C，投影不增距给 d(φ(x),D)≤||G(x)−c||；取下确界得到原锥残差。于是

\[
\|x-\widehat x\|\le\frac4{\sigma\eta}d(G(x),C).
\]

**裁定：b=4/(ση) 正确，未漏坐标变换常数。** 其原因是这里只控制 D_uθ，而不是粗暴地把完整逆图范数都估计成 1/σ。

r=0 时在连通小球上 Dφ=0，φ≡φ(x̄)=0，可取 x̂=x、b=0；此时不定义 σ 或 η。r=0 的后续流形坐标可直接取恒等图。

### P6. 局部非线性面约化

定位：M 184–192；A 364。

若 x 可行，d(φ(x),D)=0，P5 强制 u=0、φ(x)=0。因任意锥面满足 C∩span F=F，得 G(x)∈F。反向显然。r=0 分支同样成立。这条直接证明不使用附近 A1/A2，因而独立于来源 Proposition 5.2 的证明细节。

## 5. PROVED：参考面残差性质、切向修正及 MSCQ

### P7. 相对内点方向与 c=4/τ_F

定位：M 198–210；A 368–376。

F≠{0} 时由最小面性质选 Ad̄∈ri F，正数归一化 d̄ 得单位 d0；P_HAd0=0，故 d0∈T_M(x̄)。F 为非零尖锥，所以其相对边界非空（含 0），且

0<τ_F=d_spanF(Ad0,rbd F)≤||Ad0||<∞。

在 M 图中取固定 w0 实现 D_zθ(0,0)w0=d0。无需令 ||w0||=1：连续性直接控制输入方向导数为 ≤2，及输出方向导数与 v0=Ad0 的误差 ≤τ_F/4。设 q=G(x̂)∈span F、p=P_Fq、r_F=||q−p||，对 r_F>0 取 t=2r_F/τ_F。输出终点可写为 p+t v0+e，且

\[
\|e\|\le r_F+t\tau_F/4=3r_F/2<2r_F=t\tau_F.
\]

由相对球 B_spanF(v0,τ_F)⊂F、锥缩放及 F+F⊂F，终点属于 F。输入路径长 ≤2t=4r_F/τ_F。r_F=0 时取 x+=x̂，不使用严格不等式。**c=4/τ_F 正确。**

### P8. 邻域不是随每个点临时选择

定位：M 171、210、219–234；A 348–392。

一个完整的统一化方案是：先固定具有所有导数界的较大乘积图；再选闭包包含于其中的小乘积图作为 x̂ 的落点区域；它到大图边界有正余量。q→0 保证 r_F=d(q,F)→0，因此最后缩小 x 的一个统一邻域，使所有 t||w0|| 小于该余量，同时使 x̂ 落入小图。正常修正 (u,z)↦(0,z) 全程保持在乘积图内。另先取包住这些点的凸输入球，在其上固定 L_G。上述限制只有有限多个，交集仍含 x̄ 的开邻域。

因此两步修正、G 的 Lipschitz 界、面残差界和最终不等式 **可在一个共同邻域对所有 x 同时成立**。原文“nesting neighborhoods”是标准可补展开，不是尚缺的数学假设。

### P9. 仅需参考面在原锥中的 amenability

定位：M 219–234；A 245、293–308、392。

所用性质是存在 a_F>0，使 d(y,F)≤a_F d(y,C) 对每个 y∈span F 成立。这是 **F 相对于 C** 的性质，不是仅说 F 作为独立锥是 amenable。全锥 amenable ⇒ nice，并对所有面给出该性质；相关定义不要求 a_F 在各面间一致。[Lourenço，Definition 8、Proposition 13](https://optimization-online.org/wp-content/uploads/2017/11/6348.pdf)

先以 P5 修正到 M，再以参考面性质转移残差：

\[
d(G(\widehat x),F)
\le a_Fd(G(\widehat x),C)
\le a_F\{d(G(x),C)+L_G\|x-\widehat x\|\}
\le a_F(1+L_Gb)d(G(x),C).
\]

再用 P7 并相加，得到

\[
\boxed{\kappa=b+\frac4{\tau_F}a_F(1+L_Gb).}
\]

**无遗漏常数；没有将面约化的集合等式错误当成残差比较。** F={0} 时 x̂ 已可行，可用 κ=b；b=0 的情形局部全可行，可选任意 κ>0。F=C 时 H={0}、b=0、a_F=1，P7 即给严格方向误差界。E={0} 单独按局部全可行处理，避免 τ_F、σ、单位球的空对象。

### P10. 非 apex 原约束的残差转移

定位：M 36、236–238；A 417–423。

在“局部约化”采用标准输出空间含义时结论成立：取 g(x̄)=ȳ、开输出邻域 W、Lipschitz 的 Ξ:W→E，使 Ξ(ȳ)=0 且 K∩W={y∈W:Ξ(y)∈C}，并令 G=Ξ∘g。K 闭凸时 y↦P_Ky 连续，故可以缩小输入邻域，确保 g(x)、P_Kg(x) 同时处于一个 Ξ 的 Lipschitz 邻域。于是

\[
d(G(x),C)\le\|\Xi(g(x))-\Xi(P_Kg(x))\|
\le L_\Xi d(g(x),K).
\]

原可行集和约化可行集在修正点所在邻域相同，故最终误差界常数为 κL_Ξ。只需这一方向，不需逆残差比较；该转移步骤本身也不使用 DΞ 满射或 C2 性。

## 6. PROVED：proper nice 范围内的精确普遍量词

定位：M 314–325；A 173–180、403–409。

对一个固定 proper nice 锥 C，定义 U(C) 如下：对于 **每一个**有限维 Euclidean 输入空间 X、开集 V⊂X、C1 映射 G:V→E，以及 **每一个**满足 G(x̄)=0 和冻结 CRSC 的 x̄∈V，存在依赖于该系统与参考点的 κ>0、δ>0，使所有 x∈B(x̄,δ) 都满足 d(x,G⁻¹(C))≤κd(G(x),C)。

则 C amenable ⇔ U(C)。正向由 P9。反向固定任意面 J，取 X=span J，G 为 Euclidean 等距包含映射。其线性化最小面为 J，normal rank 恒为 0；且 nice 给 C*+J⊥ 闭，等价于 P_spanJ(C*) 闭，因此确实满足 CRSC 的闭像项。**不能仅凭 DG 常值就宣称这项成立。**

此时 G⁻¹(C)=J，普遍性质给出 κ_J、δ_J 及 span J 内零点附近的面残差不等式。任意 y∈span J\{0}，选 λ>0 使 ||λy||<δ_J；锥距离齐次，除以 λ 得 d(y,J)≤κ_Jd(y,C)。y=0 平凡成立。对每个 J 重复即为 amenability。

不需要共同的 κ_J 或 δ_J；普遍量词必须允许输入维数随面变化，或等价地允许足够大的固定输入空间来实现所有面包含测试。此审查不把它扩大到所有非 nice 锥；在该范围外，面包含映射的闭像 CRSC 项不自动成立。

## 7. NEEDS_REPHRASE：精确定位及最小修订建议

| ID | 定位与严重度 | 证据、后果 | 最小修订 | 理想修订 |
| --- | --- | --- | --- | --- |
| NR-1 | M 212–234；A 245、392；MODERATE | M 的正式定理仅写全锥 amenable，参考面版本主要在 A 中；如摘要直接说“amenable minimal face”可能误指 F 自身作为锥 amenable | 单列“C proper nice，且参考面 F 满足 d(y,F)≤a_Fd(y,C)”的命题，并保留同一 κ | 以参考面定理为主，全锥版本为推论；不扩大当前锥类 |
| NR-2 | M 318–325；A 403–409；MODERATE | “every C1 map”省略了输入空间、参考点和局部常数的依赖 | 用 §6 的 U(C) 定义明确 ∀(X,G,x̄)∃(κ,δ)∀x | 给出三者等价：amenability、U(C)、所有线性面包含满足 MSCQ |
| NR-3 | M 36、236–238；A 417–423；MODERATE | 仅有输入可行集相等并不蕴含所需输出残差传递；A 已写出关键输出映射性质 | 明示输出邻域 W 上的锥约化、Ξ Lipschitz 与 Ξ(ȳ)=0 | 独立列一个残差转移引理，区分 g 的输出锥 K 与约化锥 C |
| NR-4 | M 171、210、224；A 376、392；MINOR | “缩小邻域”及路径保留原理正确，但“effective”可能被误读为已给出可计算半径 | 写明常数是可显式表达的局部上界，半径存在而未显式计算 | 增补 §5/P8 的嵌套图段落；若将来声称数值可实施，再给 DG/图导数连续模 |
| NR-5 | M 95、198–210；A 138、362–376；MINOR | 满面闭像证明与 r=0 时使用流形图略写；不影响有效性 | 添入 P3 的有界提升证明；r=0 使用恒等图；r_F=0 不移动 | 把 E=0、F=0、F=C、r=0 分支汇成定理后一个短说明 |

这些项不构成核心数学失败，也不要求制造额外假设。尤其不能把 A1/A2 重新加回主定理，也不能把“所有面有共同 amenability 常数”加为条件。

## 8. GAP、三重审查、修订优先级

**GAP：在受审三条证明链内无已发现条目。** 不应为制造“严格审查”印象而把可直接写出的标准局部化步骤标为未解缺口。

- CONTRIBUTION：优先权未评估；原文对应问题及 imported tools 已分离，不将来源的 amenability、闭像定理或常秩定理计为新成果。
- METHODS：核心结论、C1 充分性、闭投影锥、双向秩界、相对内点、正常/切向修正、所有退化分支和量词已独立重建，数学就绪度 `READY`。
- COMMUNICATION：正式论文包装 `CONDITIONALLY_READY`；NR-1/2/3 应在摘要和正式定理定稿前清理，NR-4/5 为短证明展开。

最高风险不在当前代数，而在把“参考面相对于 C 的残差性质”简写为“F amenable”，把 universal 理解成统一 κ，以及把任意输入层面的可行集重写当成输出锥约化。修订只需一个有界的定理包装任务，不需要新增实验或数值模拟。

## 9. 执行、交付与限制

- 已执行：两文件完整读取、行号定位、哈希记录、三篇原始公开资料定理定位及本审查 Markdown 写入。
- 未执行：外部 API、数值验证、符号软件验证、Lean/其他形式化验证、源正文改稿、全文优先权检索、阶段状态修改。
- 交付：`output/conic_paper/CORE_PROOF_AUDIT.md`。主控负责本轮所有新交付的统一有序保存；本子任务未单独上传或改变既有文件身份。
- 作者新增输入：当前核心证明检查不需要；摘要/贡献措辞的定稿由主控与作者决定。

## 10. 标准 SCI expert contract

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review
project_id: RL-CONIC-2026
paper_family: theoretical
stage_id: T4/T5
task_id: PA-CORE
task_status: COMPLETE
inputs_reviewed:
  - output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md, all 416 lines, hash recorded above
  - output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md, all 490 lines, hash recorded above
  - Pataki original Theorem 1.1 and Proposition 2.1
  - CRSC author-hosted paper, Definition 3.2, Proposition 5.2, Theorems 5.1 and 5.2
  - Lourenco amenable-cone paper, Definition 8 and Proposition 13
outputs:
  - output/conic_paper/CORE_PROOF_AUDIT.md
evidence_status:
  - VERIFIED_USER_MATERIAL: supplied theorem package and prior audit inspected in full
  - VERIFIED_SOURCE: imported closed-image criterion, CRSC definition and A1/A2 source interface
  - VERIFIED_SOURCE: amenability definition and amenability implies niceness
  - AI_INFERENCE: full-neighborhood A1/A2 and nonlinear facial reduction proved
  - AI_INFERENCE: reference-face MSCQ constants and uniform neighborhood construction checked
  - AI_INFERENCE: universal apex equivalence and all quantifiers checked
  - EXECUTED_LOCAL: local reads, hashes and audit artifact creation
  - NOT_EXECUTED: numerical or machine-formal proof validation; source manuscript edits; standalone upload
  - PENDING_VERIFICATION: worldwide priority and complete publication positioning, outside PA-CORE
assumptions:
  - finite-dimensional Euclidean spaces and proper nice output cone in the frozen scope
  - C1 map on an open neighborhood with zero reduced reference value
  - fixed reduction, minimal face and normal subspaces
  - standard output-local cone reduction for the non-apex residual transfer
author_input_needed: []
manual_actions: []
quality_checks:
  - exact Pataki cone-image equality versus closure distinguished
  - fixed-subspace rank semicontinuity and no circular use of A1/A2
  - common full neighborhood, kernel projections and ri persistence
  - closure of projected cone controlled in angle argument
  - C1 chart invertibility, fiber connectedness and derivative bounds
  - b equals 4/(sigma eta), c equals 4/tau_F and kappa formula checked
  - same input map and common manifold used for both corrections
  - E=0, F=0, F=C, rank=0 and zero face-residual branches checked
  - non-apex residual direction and local projection containment checked
  - universal quantifiers, face-inclusion closedness and cone homogeneity checked
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: orchestrator to incorporate NR-1 through NR-5 into a bounded theorem-packaging revision while preserving the frozen mathematical scope
stage_acceptance_recommendation: PASS_CANDIDATE
```

唯一下一行动：由主控据 NR-1 至 NR-5 发起一次不扩大数学范围的定理表述与证明展开修订。
