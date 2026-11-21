# DD2 任务书验收矩阵（基线 `d6ecad7`）

**适用范围。** 这是前一份交接稿的七项 P0–P3 专项矩阵。当前主任务遵循[作者原版 17 节协议](../topics/dd2/DD2_FINAL_ACCEPTANCE_PROTOCOL.md)，逐问进度见[最终数学验收](DD2_FINAL_ACCEPTANCE.md)。

本文把任务书中的 P0–P3 工作线逐项绑定到规范 Claim、证明文件和剩余义务。`derived-checked` 只表示项目内的推导、量词和反例已经复核；它不表示全球先行性已经穷尽，也不把比较级必要性升级成算子级反例。

## 1. 总体状态

| 优先级 | 验收对象 | 当前状态 | 规范证据 | 仍未闭合的义务 |
|---|---|---|---|---|
| P0 | 对 Lauster–Luke、Alcantara、Hölder PPA 的先行性攻击 | `derived-checked`（项目内逐式审计） | [C410](../../CLAIMS.md#c410)、[P0 报告](DD2_P0_PRIOR_ART_2026-11-21.md) | 全球检索、非英文版本和所有后续版本的优先性不能由有限审计宣称完成；主文必须承认重合。 |
| P1 | 低 \(L<1/2\) 步长支的固定规则动态达到 | `derived-checked`（离散闭集/固定完整图；局部锥和多面体闭凸障碍已证） | [C411](../../CLAIMS.md#c411)、[低 \(L\) 审计](../topics/dd2/lowL_dynamic_sharpness.md) | 一般弯曲闭凸集的可和或非可和链仍未判定；原一般法锥论证有符号缺口。 |
| P1 | 方向自适应 \(\beta_k,\alpha_k\) 的可计算性与临界门 | `derived-checked` | [C407](../../CLAIMS.md#c407)、[参数审计](../topics/dd2/adaptive_parameter_audit.md) | 更一般变化的 \(V\)、非局部观测和算法实现成本仍需逐算法验证。 |
| P2 | 双误差界的完整覆盖锐性与原到约化逆向 | `derived-checked`（精确 lift 门和选支反例） | [C408](../../CLAIMS.md#c408)、[P2 覆盖/矩阵审计](DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-coverage) | 超出近极小 lift 或允许边覆盖的统一全图结论尚无根据；弱核控制和任意坏值选择仍开放。 |
| P2 | 非线性原始—对偶结构的可验证矩阵门 | `derived-checked`（分离块的完成平方/Schur 门） | [C408](../../CLAIMS.md#c408)、[P2 矩阵审计](DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-matrix) | 非分离耦合、最优门的统一闭式和更一般方向自适应尚未证明。 |
| P3 | 非幂势扰动的锐性与物理恢复 | `derived-checked`（比较层预算、二点恢复） | [C412](../../CLAIMS.md#c412)、[P3 审计](DD2_PRO_COMPLETION_2026-11-20.md#dd2-pro-theta)、[独立复核](DD2_P3_REVIEW_2026-11-21.md) | \(\Delta_Theta+\eta\) 的算子级坏例需按具体 \(\Theta\) 构造；一点评估不能替代二点物理长度门。 |
| P3 | FBF、外梯度、FRB 与分布式固定步证书 | `derived-checked`（受限固定步子类） | [其他分裂审计](DD2_OTHER_SPLITTING_AUDIT_2026-11-21.md)、[分裂审计](../topics/dd2/splitting.md#dd2-splitting-open)、[C405](../../CLAIMS.md#c405)、[C412](../../CLAIMS.md#c412) | 统一松弛、非分离多算子、变图/异步和分布式通信恢复仍是开放扩展。 |

## 2. 已完成的可写命题

### 2.1 P0：先行性边界

P0 报告逐式读取 Lauster–Luke 2021 的 (18)–(19)、Theorem 16(b)、Lemma 17、Corollary 19，Alcantara v1 Proposition 3.4/Remark 3.5，以及 Li–Mordukhovich 2012 Theorem 7.2–7.3。可安全写入主文的结论是：比较曲线、输入步残差、全锚半单调能量和 Hölder PPA 的部分有限长度机制已有先例；DD2 的可区分范围必须写成明确量词下的最近输入锚、允许近端子关系、函数缺陷、完整真残差 infimum、反向几何预算和低 (L) 步长分支。不能使用“首次提出一般比较曲线”或“首次证明 Hölder PPA 有限长度”。

### 2.2 P1：固定图低 (L) 动态

令 \(0<L<1/2\)、\(\rho_L=L/(1-L)\)，选 \(r_k=A(t_k)/t_k\in(\rho_L,1)\)，并令 \(s_k=t_{k+1}/L\)。一维锚链
\[
x_{k+1}=x_k-s_k,\qquad p_k=x_k-t_k,\qquad S=\{p_k\}\ \text{（必要时加极限点）}
\]

给出同一闭零集 \(S\)、同一完整闭图 \(J=P_S\cup\{(x_k,x_{k+1})\}\) 和同一反演关系 \(F=(J^{-1}-I)/\lambda\) 上的逐步取等。最近锚、真残差和缺陷分别满足

\[
d(x_k,S)=t_k,\quad d(x_{k+1},S)=t_{k+1},\quad
r_F(x_{k+1})=s_k/\lambda,\quad
D(t_k)=t_k^2r_k(r_k-L)/L^2.
\]

取 \(A(t)=t/(1+t)\) 且初值足够小，得到局部孤立离散零集、距离趋零但 \(\sum s_k=\infty\)。该构造已经排除了“固定规则只能在每一步改变零集”这一担忧；L6a 进一步排除了局部锥、特别是多面体闭凸零集的收敛锚链，但一般弯曲闭凸零集的所有动态仍未判定。

### 2.3 P2/P3：覆盖、矩阵门、扰动与恢复

P2-A 证明：若每个输出点都有任意近极小图值的输入 lift，且这些 lift 边满足允许窗和输出模，则连续性把近极小界传给完整真残差。反例 \(G(y)=\{y,y^3\}\) 表明只控制算法选中的一支不能推出完整 infimum 界。P2-B 通过块算子完成平方给出 \(U,V,W\) 和 Schur 补 LMI，可逐实例检查缺陷吸收与松弛余量；它不自动覆盖任意非线性耦合。

P3-A 把未扰动势预算精确改写为

\[
\ell_k\le C[\Theta(r_k)-\Theta(r_{k+1})]
 +C\bigl[\Theta(r_k+\eta_k)-\Theta(r_k)\bigr]+\eta_k .
\]

因此一般连续势所需的是 \(\sum_k(\Delta_\Theta(r_k,\eta_k)+\eta_k)<\infty\)，而不是孤立地假设普通欧氏误差可和。P3-B 证明二点恢复模能推出物理 shadow 的有限长度；一点评估只能给点识别，不能替代相邻 shadow 控制。P3-C 给出固定连通图、正定预条件、最大单调网络项和 \(P\)-cocoercive 网络项下的前向—后向平方能量；通信误差必须另按可和尾控制。

## 3. 论文写作的硬性修订

1. 在主定理前明确 \(A\) 的连续性、\(A(0)=0\)、\(0\le A(t)<t\) 以及逐轨道比较所需的非减上包络；不能把逐尺度严格下降写成点收敛或有限长度。
2. 每次使用“完整图”“最近锚”“全锚”“真残差”时写出对应量词。近极小 lift 是存在量词，不能支撑允许算法任意选坏值的全轨道结论。
3. 将 P0 已知结果作为相关工作和边界条件，保留 DD2 的反向预算、低 (L) 固定图达到性、函数缺陷和物理恢复分离。
4. 将 C411 的一般闭凸链写为 open/candidate；只有附加自对偶法锥或类似正半空间条件时，才可使用条件性有限长度障碍。
5. 将 P3 的势扰动写成 \(\Delta_\Theta+\eta\) 两项债务，并把一点评估与二点物理恢复分成不同命题。

## 4. 可复现验证

在仓库根目录运行：

```text
python3 research/code/dd2/verify_outline.py
DD2 verified: 6 ordered sections, 7 claim records, 13 local links, 7 exact algebra checks.

python3 research/validate_assets.py
Verified 240 initial-manifest hashes, 251 audited source files, 178 ZIP members, 4827 source units, 4671 atomic records in declared scopes, 954 nodes, 719 edges and 487 Markdown files.

python3 research/build_graph.py
validated 954 nodes and 719 conjunctive edges; generated HYPERGRAPH.md and map.html
```

可视化构建也已通过：`visualization/cosmos/build.py` 生成 954 个节点、719 条精确超边，`visualization/xianxia/build.py` 生成 954 个节点、719 条边、32 个物件和 17 个领域。所有修改已在 `origin/main` 的 checkpoint 中推送。
