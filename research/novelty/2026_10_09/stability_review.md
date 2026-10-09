# C216 正则化持续误差的敌对审查与可调用逆核分支

日期：2026-10-09。对象基线：`5726c10083cb2dbaef52e2ec802d89c8fd9d39c1`。独立任务范围是 C216 的 RS1–13、C213 误差物理桥及直接相关一级先行；没有审查整个库或所有误差算法。没有改动 canonical C216、总账或提交 Git；后续主代理明确要求的新增 [C220 逆核分支](../../canonical/gppa_regularized_inverse_branch.md) 与本审查自有脚本是本次新增内容。

## 1. 判定与不能升级的地方

**C216 原条件定理没有发现致命数学异议。** 从完整 pair-monotonicity 独立重建了正则化核零值唯一、核卷积、原图残差抵消、残差窗、右上 gauge 和轨道族双极限；原物理误差始终只作用于精确输出之后，原 F 图值始终在 hat x 上。

但其先行性和锐性只能作如下有限判断：

| 判断 | 本次结论 |
| --- | --- |
| 与 2608.01584v1 T4 的印刷预算相比 | C216 的相同前件下抵消预算严格更低（L>0），已逐式确认；这是数学改进 |
| 首次出现 Tikhonov + 持续有界误差 + R-continuity 距离稳定性 | 不成立作为宽机制新颖性表述：已读 2606.01536v2 T3 给直接先行；2010 Zaslavski 官方摘要已有有界不消失误差近端近似解机制 |
| C216 全称定理已由更早同一前件覆盖 | **未证明**。2606 T3 限普通极大单调/Id 核，不能处理 C216 任意非单射 pair-monotone 核 |
| C216 是所有自然重合实例中最好的稳定性管 | 否。已读的 2606 T3 在某些重合实例更紧；显式线性精确管又更紧 |
| C216 单步残差系数 1 最优 | 是，下面法锥一步可取等 |
| C216 渐近残差预算全类最优 | **未证明**；单步取等与卷积稳态取等不能未经证明合并。本次只给两个线性子族的精确锐管 |
| 全球首创、全球不存在等价先行 | 继续开放；本次有限检索不能证明该全称否定 |

严格可 salvage 的内容是：保留 C216 无逆核时的完整物理距离管；追加已有物理反演桥后调用 C220，与 C216 取 min；若核具有非线性向前误差模，按第 5 节更换误差预算。不得把这些简单组合包装成独立全球首次。

## 2. 一级来源与实际阅读范围

本表中的工具 ref 是检索证据标识，URL 与定位供后续独立复核；获取失败没有数学排除意义。只把实际读取的源事实写作先行事实。

| 一级来源、版本与 URL | 实际读取的位置 | 可承担的结论与边界 |
| --- | --- | --- |
| Le–Mordukhovich–Théra, [2608.01584v1](https://arxiv.org/html/2608.01584v1), Aug 2026；工具 `turn8view3`, `turn22view6`, PDF `turn56view0` | 本地归档 PDF 印页 8–11 的 Lemma 3 和 T4 陈述/完整证明；HTML 同段；在线 PDF 印页 9 视觉读式（`turn61view2`）；参考文献 [12],[16],[17] | 本次 C216 同前件直接比较目标。印式是 `4Lε/λ²+3Lε²/λ+εa`。不宣称其整篇所有定理已涵盖 |
| Le–Mordukhovich–Théra, [2606.01536v2](https://arxiv.org/html/2606.01536v2), **2026-09-08**；工具 `turn27view0`, `turn33view1` | §2 强单调 resolvent 因子和 Definition 1；§3 Theorem 3 全陈述、完整证明，HTML L166–256；引言与参考文献 [24] | 普通极大单调/Id 核的 Tikhonov 持续误差物理管已存在，见第 3 节。v1 正文 PDF/HTML 本次获取失败，不把 v2 的具体公式未经核对追溯到 2026-06-01 v1 |
| B. K. Le, [2311.13096v1 PDF](https://arxiv.org/pdf/2311.13096), 2023-11-22；JCA 31 (2024), 243–254；工具 `turn11view1`, `turn22view4` | PDF 物理页 7、Theorem 1 及完整证明，Eq. (12)–(17)；该页视觉核对 `turn56view1` | 普通极大单调 Tikhonov 零点范数与 `d(xε,S)≤ρ(εa)` 的直接先行，含 truncated R-continuity 门。本次没读整篇全部 DC 结果 |
| Le–Théra, [2408.09139v1](https://arxiv.org/html/2408.09139v1), 2024-08-17；工具 `turn8view1`, `turn22view5`, `turn63view0` | Introduction 与 Definition 1；§4 T11、Lemmas 12–13、T14 的陈述和完整显示证明 | 完整逆像一般 gauge 到精确 PPA 距离率不是新机制。此处为精确 PPA、极大单调/凸次梯度类，没有给本次任意 warped 持续误差预算 |
| A. J. Zaslavski, [SIAM DOI 10.1137/090766930](https://epubs.siam.org/doi/10.1137/090766930), online 2010-06-11；工具 `turn61view0` | 官方摘要、元数据、题名、页码；**没有读取定理正文** | 已足以否定宽泛“首个允许有界不消失误差的近端机制”。不足以判断同一 C216 前件/预算的定理覆盖 |

检索使用 `R-continuity Tikhonov nondiminishing/nonsummable errors`、源编号和完整题名，沿源 T4 参考文献 [12],[16],[17] 追溯。没有穷尽其它名称、语言、未索引结果或未公开工作。明确只采用一级源的已读内容；搜索引擎偶然返回的非数学页面没有用于结论。

## 3. 更早物理分支已经在重合子类给更紧管

已读 2606.01536v2 T3 假设 A 极大单调，S=zer A 非空，A⁻¹ 在 0 R-continuous。固定 λ,ε,δ>0，

\[
x_{k+1}=J_{\lambda(A+\epsilon I)}x_k+e_{k+1},\qquad\|e_{k+1}\|\le\delta,
\]

给预算

\[
P_{\epsilon,\delta}=
\delta\left(1+\frac1{\lambda\epsilon}\right)+\rho(\epsilon a),
\quad a=\inf_{s\in S}\|s\|.
\tag{SR1}
\]

它直接将扰动迭代的物理距离与正则化零点偏移相加，免去对最终噪声残差再应用 ρ；对于 εa 的真实固定残差，其局部 σ 窗须最终合法。该机制正是新 C220 在 Id 核下的既有子例。

对完整 F(x)=x−2、v=Id、λ=1、ε=1/10、δ=1/100、ρ(t)=t、a=2：

\[
\text{C216 管}=0.32,\qquad
\text{已读先行 T3 管}=0.31,\qquad
\text{同对象精确锐管}=\frac{221}{1100}\approx0.200909.
\tag{SR2}
\]

因此 C216 较源 Aug T4 印预算更紧，不意味着对所有已知稳定性分支都更紧。不同 ρ/λ 也能使残差分支更紧，正确接口是取已认证分支的 min。

从 RS7 的 q=(1+λε)⁻¹ 和追加逆 Lipschitz 门 `||x−y||≤||v(x)−v(y)||/m`，对固定 sε 得

\[
\limsup_kd(x_k,S)
\le\delta+\frac{L\delta}{m\lambda\epsilon}+\rho(\epsilon a).
\tag{SR3}
\]

这里物理误差 δ 在 hat 回代后只收费一次，比先放大为 Lδ/m 的 actual 分支更紧；完整证明、窗口、局部点对量词及与 C216 的 min 已写入 [C220 正文 RI1–12](../../canonical/gppa_regularized_inverse_branch.md)。该追加门排除全域非单射核，因此没有以先行覆盖偷换 C216 的完整范围。全域逆控制不能自动给满射或 warped coverage。

## 4. 单步锐性与两个精确线性子族

### 4.1 C216 的单步抵消系数 1 可取等

取 H=R、v=Id、完整 F=N_[s,∞)，s≥0，S=[s,∞)，Sε={s}、cε=s、a=s。输入 x=s−D，D≥0，精确输出 hat x=s 合法，选中原图值

\[
f=\frac{x-s}{\lambda}-\epsilon s=-\frac D\lambda-\epsilon a\in F(s).
\]

所以 `|f|=D/λ+εa`，C216 的 RS9 单步系数不能在完全相同范围内降低。取 s=0 也使 εa=0 而保留系数 1 取等。此例的后续稳态 D 只有 δ 量级，**不是**核卷积稳态 `Lδ/(1−q)` 与 residual 同时取等例；不能据此称 C216 渐近 budget 已锐。

### 4.2 标量完整仿射关系的锐距离和锐残差

H=R、v=Id、F(x)=μ(x−s)，μ>0；S={s}，全 coverage、pair monotone 和完整全域 ρ(t)=t/μ 均成立。置

\[
s_\epsilon=\frac{\mu s}{\mu+\epsilon},\quad
p=\frac1{1+\lambda(\mu+\epsilon)}.
\]

所有合法扰动轨道满足 `xk+1−sε=p(xk−sε)+ek+1`，故

\[
\limsup_k|x_k-s|\le
\underbrace{\frac{\epsilon|s|}{\mu+\epsilon}
+\frac{\delta(1+\lambda(\mu+\epsilon))}{\lambda(\mu+\epsilon)}}_{\text{锐距离管}},
\tag{SR4}
\]

真实 hat 输出原值 f=μ(hat x−s) 同时有

\[
\limsup_k|f_{k+1}|\le
\underbrace{\frac{\mu\epsilon|s|}{\mu+\epsilon}
+\frac{\mu\delta}{\lambda(\mu+\epsilon)}}_{\text{锐原残差管}}.
\tag{SR5}
\]

证明：几何卷积给 `limsup|xk−sε|≤δ/(1−p)`，hat 偏差再乘 p；三角相加给以上两式。令全部误差恒为 `δ sign(sε−s)`（s=0 任取一号），则物理极限为 `sε+δ sign(sε−s)/(1−p)`，两三角项同号，SR4–5 均取等。该计算是任意 μ,λ,ε,δ 的严格解析证明。

### 4.3 二维完整斜对称线性族的锐放大率

取 H=R²，J 为 π/2 旋转，v=Id、F=βJ，β>0。F 为全域连续极大单调（pair 内积恒为 0），S=Sε={0}、a=0，全 coverage，真实全域 R-continuity gauge `ρ(t)=t/β`。识别 R² 与 C，置

\[
\alpha=1+\lambda\epsilon>1,\quad
t=(\alpha+i\lambda\beta)^{-1}=r\zeta,
\quad r=(\alpha^2+(\lambda\beta)^2)^{-1/2},\quad|\zeta|=1.
\]

迭代就是 `xk+1=t xk+ek+1`。全部 |e|≤δ 给物理管 δ/(1−r)，hat 原残差 `f=βJt xk` 给

\[
\limsup_k\|f_{k+1}\|
\le\frac{\beta r\delta}{1-r}
=\frac\delta\lambda\,
\frac{\lambda\beta}{\sqrt{\alpha^2+(\lambda\beta)^2}-1}.
\tag{SR6}
\]

两式可在**同一无限合法轨道**精确取等：令 X=δ/(1−r)，`xk=X ζ^k`、`ek+1=δ ζ^(k+1)`，则 `t xk+ek+1=X ζ^(k+1)`。原图值、正则化更新和误差界逐步精确成立。

进一步在 β>0 的这一指定族中求最坏原残差：令 b=λβ，函数 `h(b)=b/(sqrt(α²+b²)−1)` 的导数符号是 `α²/sqrt(α²+b²)−1`。唯一最大点

\[
\lambda\beta_* =\alpha\sqrt{\alpha^2-1},\qquad
\boxed{\sup_{\beta>0}\sup_{\|e\|\le\delta}
\limsup\|f\|
=\frac\delta\lambda\frac\alpha{\sqrt{\alpha^2-1}}.}
\tag{SR7}
\]

C216 的 a=0 预算为 `δ α/(λ(α−1))`，严格大于 SR7。对 δ=ε²、固定 λ，SR7 是 `O(ε^(3/2))`，C216 是 `O(ε)`；这里 β* 随 ε 改变，是族最坏值渐近，不能冒充同一固定 F 的 ε 双极限阶。每个固定 β 的 SR6 对 ε→0 反而是 O(ε²)。

SR7 是这个二维斜对称族的锐性，**不是任意非线性完整单调关系的通用锐性定理**；本次没有证明一般关系也满足 SR7。它证明自然重合线性类有真实、可校准的更紧预算，说明进一步研究全类锐常数有价值。

## 5. 非线性向前误差模与 gauge 端点

C216 中 Lδ 只用于从物理误差得到核误差。可准确降成所用点对上的向前模：若 τ:[0,∞)→[0,∞) 非减，τ(0)=0，且所有实际点对满足

\[
\|v(\widehat x_{k+1}+e_{k+1})-v(\widehat x_{k+1})\|
\le\tau(\|e_{k+1}\|),
\tag{SR8}
\]

则原 RS5–7 与抵消不变，核卷积中仅把 Lδ 换成 h=τ(δ)。严格得到

\[
b^{\tau}_{\epsilon,\delta}
=\frac{\tau(\delta)(1+\lambda\epsilon)}{\lambda^2\epsilon}+\epsilon a,
\quad
\limsup d(x_k,S)\le\delta+\rho(b^{\tau}_{\epsilon,\delta}+)
\tag{SR9}
\]

前提仍是 `bτ<σ`。证明只重用 RS7 的 q 收缩、物理核误差 h 和真实 hat 原图值；不要求 v 单射，也不要求 ρ 在正点连续。如果先用 Lipschitz L 得 b，再另有更小真实 h≤Lδ，可用更小 residual 预算；不能把核误差范数 h 误写成物理距离误差 δ 的替代品，最终 δ 项仍保留。

固定数据和一族已存轨道，若 δ(ε)→0 且 τ(δ(ε))/ε→0，则 bτ→0，由 ρ(0+)=0 得正则化距离双极限 0。τ(t)=Ct^γ、δ=ε^p 时条件 pγ>1 是这一包络证明的充分门；不宣称它对所有实际轨道必要。单凭连续 τ 不能普遍保留 `δ=ε²`，因为 τ(ε²)/ε 未必趋 0。

若再有全端点连续非减逆模 η（η(0)=0），并对实际 hat 与固定 sε 合法，则同一 C220 机制还给

\[
\limsup d(x_k,S)\le
\delta+\eta\!\left(\frac{\tau(\delta)}{\lambda\epsilon}\right)+\rho(\epsilon a).
\tag{SR10}
\]

η 在该正端点连续是 limsup 穿过 η 的门；若只非减，则端点应为 η((τ(δ)/(λε))+)，和 ρ(b+) 完全同一量词问题。为让 C220 保持最小可复核身份，canonical 只收录 m-Lipschitz 逆版本，SR8–10 作为本次独立审查的严格可延伸内容。

正点 + 不能一般删：纯标量层面若 `rk=b+1/k`、ρ(b)=0 而 ρ(t)=1 对 t>b（在原点附近保持 0），则 `limsup ρ(rk)=1>ρ(limsup rk)=0`。这只反驳从“ρ非减”推出端点交换，不冒充一个已构造的完整 F 轨道反例。C216 对源印 Bε 的包含用严格 residual 预算裕度来最终落在 Bε 以下，数学上充分；L=0 恒核直接原图值分支也有效。

## 6. 实际复算与剩余义务

运行：`python research/code/gppa_novelty/stability_review.py`，退出码 0。脚本用 Fraction 反代抵消平方、法锥单步取等、完整仿射关系的精确恒误差轨道、先行 T3 与 C216 同对象预算及 actual/hat 噪声差；另用复数逐步反代 SR6–7 的无限轨道定义，并抽样最大点两侧和极端 α 校验解析最大公式。它没有用有限样本证明任意关系定理。

剩余义务：任意完整单调/配对单调类的最佳渐近 residual 常数尚未求出；原点及正点 gauge 的跳跃必须按真实残差窗处理；C220 的局部 inverse 门须先认证相应全部实际点对；任何全初值存在声明须另核 coverage；全球先行性继续是开放检索/等价桥义务。本次有可引用位置的一级先行已足以收窄宽泛创新措辞，但不足以确认或否定 C216 全称精确命题的全球首次。
