# GPPA 推广审查

审查对象：当前 `发表成果整理/RLEB/sections/theorem_spine.tex` 的允许近端关系定理，以及仓库 C209、C210、C218、C221。该报告只审查和提供候选文字，不改主稿，不把一般 GPPA 宣告为已完成推广。

## 裁决

固定正定线性核可以精确转换为普通 PPA，主证明保持不变；但它的条件必须在核对应的度量中重新检验。原来的欧氏 RLEB 实例不能自动变成任意核的 GPPA 实例。退化核需要输出纤维控制，非线性核需要完整坐标及反演桥；物理点收敛、物理有限长度和核坐标收敛应分别陈述。

对新的简单主例 `F(s,t)=(s,-sqrt(|s|))`，正对角核仍有自然的显式收敛公式；一个非对角正定核已经让零输入具有非零、非解输出。因此宜在正文加入最短的固定正定核推论和这个同主例的边界，而不要把论文标题直接改成覆盖一般 GPPA。

## 1. 已有文献与仓库覆盖

本轮联网读取 Le–Mordukhovich–Théra, *Convergence and Stability Analysis of a Generalized Proximal Point Algorithm and Its Inexact Version*, arXiv:2608.01584v1 的 Definition 3、Definition 4、Theorem 2 及其完整证明。arXiv 现有提交历史仅列 v1。定义采用

\[
J^v_{\lambda F}=(v+\lambda F)^{-1}\circ v,
\qquad v(x)-v(y)\in\lambda F(y).
\]

该文允许非线性、非单射核。Theorem 2 的无条件率作用于核坐标；附加逆算子 R-Lipschitz 条件后给物理零集距离的线性上界，没有证明任意完整物理选择的点收敛。来源：https://arxiv.org/html/2608.01584v1 ，Definition 3–4、Theorem 2；元数据：https://arxiv.org/abs/2608.01584 。

另外读到 2026-10-05 发布的 Yang–Lan–Hou–Liang–Toh, *An Inexact Halpern-accelerated Preconditioned Generalized Proximal Point Algorithm for the Maximal Monotone Inclusion Problem*, arXiv:2610.05742v1。它讨论最大单调、Halpern 锚定、松弛和不精确求解。Definition 2.1 的 admissible PSD preconditioner 要求预条件 resolvent 单值且全域定义；其物理提升还使用指定反演条件。它与本报告的非单调完整关系不能按名称直接合并。来源：https://arxiv.org/html/2610.05742v1 ，§2 Definition 2.1、Proposition 2.2、§4。这里只使用这些精确边界，没有评估其全部定理或声称先行性结论。

仓库已有：

| 规范结论 | 已核内容 | 与本次正文的关系 |
|---|---|---|
| C209-v1 / GP-MODULUS | 完整核推前关系、真核残差、三分支标量估计及核有限长度 | 可作一般 GPPA 扩展的规范来源，但比当前直接分支主定理更广 |
| C210-v1 / GP-PHYSICAL | 真物理 EB、向前核模、反演模、物理留域和复合 Dini 门 | 说明物理提升需要什么；本轮固定正定核是其简单特例 |
| C218-v1 | 真残差到输入步残差的桥；线性反射与 almost-averaged 接口 | 避免宣称一切非单调例都在旧理论之外 |
| C221-v1 | 可和标量尾势与已有 Lyapunov/KL 接口 | 不能把“有有限长度证明”本身当作新收敛原理 |

精确定位：`research/comparisons/2026_08_gppa_nfb/gppa_nonlinear_kernel_theorem.md` 的 NGK1–39；`gppa_physical_transfer.md` 的 GP1–27；`research/canonical/gppa_reformulation_boundary.md`；`gppa_almost_averaged_bridge.md`；`gppa_tail_lyapunov_bridge.md`。本轮读了这些正文，没有把历史审稿标签当证明。

当前论文只证明直接兼容分支。若想声称包含文献全部 ASM Theorem 2，须加入 C209 的能量分支：仅直接分支在小 ASM 常数下不能认证收缩，NGK33–34 已给出明确原因。固定正定核推论不包含这项更大的源理论包含声明。

## 2. 固定正定线性核：精确转换与完整证明

令 `M=M^T>0`，`Q=M^{1/2}`。定义

\[
\|h\|_M=\|Qh\|,\quad d_M(x,S)=d(Qx,QS),\quad
r_{F,M^{-1}}(y)=\inf_{f\in F(y)}\|Q^{-1}f\|.
\]

完整关系

\[
G(z)=Q^{-1}F(Q^{-1}z)
\]

满足逐输入、逐输出的双向身份

\[
M(x-y)\in\lambda F(y)
\iff Qx-Qy\in\lambda G(Qy),
\qquad QJ^M_{\lambda F}(x)=J_{\lambda G}(Qx).
\]

同时 `zer G=Q zer F`，`r_G(Qy)=r_{F,M^{-1}}(y)`；允许子关系及完整输出覆盖都逐项转换。`Q` 是线性同胚，所以 `QS` 闭、`QU` 开；最近零锚和初值到工作域补集的距离恰好在 `M` 度量下对应。

因此，把当前主定理的欧氏距离、范数和残差分别换为 `d_M`、`||.||_M` 和 `r_{F,M^{-1}}`，把普通近端关系换为 `J^M`，并在这个度量下检验所有 B1–B4 和严格长度预算，主定理的每一行证明保持有效。条件尤其包括每个实际输出有输入的最近 `M` 零锚 `p`，使

\[
\|2y-x-p\|_M\le Ld_M(x,S)^\gamma,
\quad d_M(y,S)\le\psi_M(r_{F,M^{-1}}(y)),
\]

以及真实残差窗口和

\[
\psi_M\left((r+Lr^\gamma)/(2\lambda)\right)\le\kappa r.
\]

尾包络仍为

\[
\mathcal L_M(r)=\tfrac12\left(r/(1-\kappa)+Lr^\gamma/(1-\kappa^\gamma)\right).
\]

若 `m=lambda_min(M)>0`，欧氏总长度和点尾至多相应 `M` 范数界除以 `sqrt(m)`。物理零集距离有
`d(x,S)<=d_M(x,S)/sqrt(m)`，但不能据此把 `M` 距离的一步 Q 线性界冒称欧氏距离具有同一个 Q 因子。

若原来的完整真实 EB 是 `d(y,S)<=psi(r_F(y))`，`b=lambda_max(M)`，则在所有所需输出上可取

\[
\psi_M(t)=\sqrt b\,\psi(\sqrt b\,t),\qquad
t\le\bar t_F/\sqrt b.
\]

原因是 `d_M<=sqrt(b)d` 和 `r_F<=sqrt(b)r_{F,M^{-1}}`。这个转移只给 EB，不能自动供应新核 RL、coverage 或兼容。幂 EB 的常数由 `c` 变为 `c*b^{(q+1)/2}`；指数不变，兼容半径可能缩小。正定核的条件数会影响最终物理常数。

### 精确命题身份建议

正文可把这一结果作为“固定正定核的度量推论”，直接引用当前允许近端定理及 C209/C210，不需要把它包装成新的 GPPA 主定理。对象是同一个完整 `F`、固定 `M`、固定 `lambda`、指定允许输出政策；结论只在重新认证后的 `M` 度量窗成立。

如果根 agent 决定单独登记此显式命题，建议语义 ID `GP-SPD-COR-v1`，编号由根 agent 协调分配（本轮读到 `C241` 已被 Hamilton 占用）。候选卡字段如下：

- **Exact Statement**：上述有限维固定 SPD 数据、`M` 度量 B1–B4、严格 `M` 长度预算；每个允许完整 GPPA 选择无限可续、留域、物理有限长并趋向原 `S`。
- **Dependencies**：C02-v3 的已证收敛证明；有限维 SPD 平方根线性代数。不是对源 ASM 理论的全部包含。
- **Evidence**：`Q` 下完整关系、覆盖、真残差、最近锚、零集和预算的双向身份；候选 TeX 给完整证明；Python 作有限矩阵及反算复核。
- **Scope**：固定 SPD；不含 PSD、任意非线性核、变核、松弛、Halpern 或持续误差。新核条件须独立认证。
- **Status recommendation**：根 agent 独立核读后可登记推导特例；本报告不修改 canonical 状态。

## 3. 同主例的正对角成功与非对角失败

固定完整单值关系 `F(s,t)=(s,-sqrt(|s|))`，`lambda=1`，`S={0}xR`。
若 `M=diag(a,b)` 且 `a,b>0`，记 `q=a/(a+1)`，完整反演给

\[
J^M_F(s,t)=(qs,t+\sqrt{q|s|}/b).
\]

每个输入有唯一输出。正常坐标是 `s_k=q^k s_0`，切向增量是 `q^{(k+1)/2}sqrt(|s_0|)/b`，所以所有初值点收敛、物理有限长，极限为

\[
(0,t_0+\sqrt{q|s_0|}/[b(1-\sqrt q)]).
\]

总长度不超过 `|s_0|+sqrt(q|s_0|)/[b(1-sqrt(q))]`。这不是总长度等式。

它也可与度量推论完全对接：输入 `M` 零距离 `r=sqrt(a)|s|`；最近零锚为 `(0,t)`；

\[
\|2J^M_F(s,t)-(s,t)-(0,t)\|_M^2
=(2q-1)^2r^2+\frac{4q}{b\sqrt a}r.
\]

在 `0<=r<=R` 取

\[
L_R^2=(2q-1)^2R+4q/(b\sqrt a),\qquad \gamma=1/2.
\]

真实核度量残差为

\[
r_{F,M^{-1}}(s,t)^2=s^2/a+|s|/b,
\quad d_M((s,t),S)\le b\sqrt a\,r_{F,M^{-1}}(s,t)^2.
\]

因此直接兼容因子的上界为
`b*sqrt(a)*(sqrt(R)+L_R)^2/4`，当 `R` 趋零时趋于 `q<1`。任何固定正对角核都存在充分小认证半径。该计算用完整 `F` 真残差；没有删分支或选小图值。

而对非对角正定矩阵

\[
M=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}
\]

其特征值为 `1/2,3/2`，输入零的完整纤维为

\[
J_F^M(0)=\{(0,0),(-4/49,16/49)\}.
\]

证明：第一方程 `2s+t/2=0` 给 `t=-4s`；第二方程 `s/2+t-sqrt(|s|)=0` 给 `-(7/2)s=sqrt(|s|)`，只有 `s=0` 或 `s=-4/49`。第二点不在 `S`。从零开始的任意完整近端选择因此不必吸收，零输入反射条件立刻失败。正定性只提供坐标转换，不消除这些额外完整输出。

原普通近端 `M=I` 全部良好与这个失败不矛盾：它们是不同的完整算法。这个反例最适合正文，因为直接复用主例；无需增加另一个人造关系。

## 4. 原理论不能不加条件提升：一维独立攻击

取完整 `F(x)=-3x`、`lambda=1`、`S={0}`、`U=R`。
普通近端映射 `T=-Id/2`，反射 `C=-2Id`，所以 `gamma=1,L=2`；完整真 EB 恰为 `psi(t)=t/3`。直接兼容恰为 `1/2`，全输入 coverage、唯一性及无穷工作域预算均成立。

改用正定标量核 `v(x)=ax`，完整方程是 `(a-3)y=ax`：

- `a=2` 时输出 `y=-2x`，完整覆盖和唯一性存在，非零轨道发散。
- `a=3` 时非零输入无输出，coverage 失败；零输入的输出是整个实轴。
- 一般 `a>0,a!=3` 的轨道因子为 `a/(a-3)`，严格收缩恰好要求 `0<a<3/2`。

该例留在报告用于攻击量词，正文可省略。这说明任何“原 PPA 结论对任意 SPD GPPA 仍成立”的版本都是假的。

## 5. 退化核：核收敛不足以控制物理方向

取 `F(t,s)=v(t,s)=(t,0)`、`lambda=1`。完整零集 `S={0}xR`，真物理残差 `r_F=|t|=d((t,s),S)`；`(F,v)` 是 1-ASM，核反射为零，全核输入覆盖成立。完整 GPPA 只要求 `t^+=t/2`，第二坐标任意，所以合法轨道

\[
x_k=(2^{-k},(-1)^k)
\]

核坐标收敛、物理零集距离几何趋零，但物理点不收敛且长度无限。这是 C209/C210 已有完整反例，不能通过把范数写成退化半范数修复。

要得到物理结论，至少需要对全部允许转移控制丢失纤维，例如 `||x-y||<=eta(||v(x)-v(y)||)`，或认证固定截面及其反演模。固定截面只给这个输出政策的结论，不给任意完整选择。退化预条件文献的 admissible 条件是额外内容，不能从 PSD 本身猜出。

## 6. 非线性核：能转换，但物理提升改变条件和率

若全域核 `v:H->H` 是 homeomorphism，定义完整 `A(z)=F(v^{-1}(z))`。则完整 GPPA 与 `A` 的普通 PPA 逐步共轭；`zer A=v(zer F)`、`r_A(v(y))=r_F(y)` 恰好成立。若 `v` 非单射，必须换成完整联合关系

\[
A(z)=\bigcup_{v(y)=z}F(y),\qquad r_A(v(y))\le r_F(y),
\]

此时残差等号一般失败，`v(S)` 也不自动闭。不能把所选物理 EB 套到这个全部纤维残差上。

全域双 Lipschitz 核：在核坐标中重新认证 RL、EB、coverage 和留域后，物理点与长度由 Lipschitz 逆传回，幂指数保留，常数变化。若只在局部有可逆性，所有实际输出必须先属于同一个认证输出领圈，否则反演与留域会循环证明。

有 `alpha` 阶 Hölder 逆时，若核反射是幂模 `Lr^gamma` 且核距离按 `kappa` 收缩，物理步尾可按 `kappa^{alpha*gamma*k}` 求和，有限长度仍成立，但物理率上界改变。一般连续逆只给点收敛，不自动给物理有限长度。C210 的复合 Dini 门是

\[
\int_0^R\eta\!\left((r+\omega(r))/2\right)\frac{dr}{r}<\infty.
\]

仓库 C214 的逆 Hölder 螺旋证明核有限长而物理长度无限可以实际发生；其核反射为对数模，不能拿幂模自动可和性覆盖它。闭物理目标的真实 EB 或完整图闭性还负责把物理极限放进原零集。

固定核之外的 `v_k`、松弛、Halpern 和非消失误差需要共同条件、偏差预算及相应全输出桥。当前固定核推论不供应这些内容。

## 7. 欧拉结构结论的 GPPA 边界

固定正定线性坐标变换保持零流形的欧拉示性数和固定点指数，因此在核坐标中完整认证相同的全域次线性反射条件和局部严格吸引管后，可回代指数结论。一般非线性 homeomorphism 也保持拓扑身份，但不自动保 Hölder 常数、光滑管或全尺度次线性控制；非单射核甚至不能保持零流形身份。

同一个 `F` 换核会改变完整迭代，不能只从旧普通 PPA 的管收缩推得新 GPPA 的管收缩。候选推论只解决收敛主链的固定 SPD 度量转换；全局完成结果的逐项核化应作为独立模块，不应在摘要中宣称所有技术已经同时推广。

## 8. 核验与交付范围

解析证明覆盖完整关系转换、真实残差、零集、锚、覆盖、预算、固定正定常数、同主例正对角显式解、非对角零输入全部纤维和退化反例。有限 Python 核验含 SPD 非对角、很小正特征值、正对角参数、零初值、正负初值、退化边界、标量失覆盖及反算；结果文件为`research/code/rleb_spd/results.json`，脚本为 `research/code/rleb_spd/verify.py`。有限计算不证明一般定理。

候选可编译正文：`/workspace/scratch/15cd717a5884/scratch/gppa_upgrade_proposal.tex`。它只加入固定 SPD 推论、同主例的具体成功/失败和最短纤维边界，没有把所有规范 GPPA 模块搬入论文。编译核验用当前稿的工作导言区和主定理；主稿自身未由本 agent 修改。

写作检查：候选先定义度量及残差，再给推论和逐项转换证明，随后用同主例说明核选择的实质作用。每段作用依次不同，没有把报告式标签写入正文。暂未进行独立新颖性认证、一般非线性核主定理扩稿、所有全局完成技术核化或投稿格式认证；这些不是本次固定 SPD 推论的结论。

本轮有限检查计数为 5212，运行状态 PASS。候选与当前主定理在复用工作导言区的独立包装稿中经 XeLaTeX 编译成功，日志没有未定义引用、缺字或 overfull 项。此处仅核可编译性与提取文字，没有把该包装稿当作最终论文布局验收。候选 TeX SHA-256：`6a8f80c8b5c97efa2adcee265cff001c2d9fb82b922ffe20b3e0b02df193da99`。主稿若整合后改变定义、标签或叙事，仍须对整合后的精确稿重新核验。
