# 复合次正则：满行秩基线、真实残差与增长边界

本文从历史材料重新推导可直接调用的基线。稳定局部身份为 `CS-TRANSFER-v1`、`CS-EB-v1`、`CS-PROX-v1`、`CS-MODEL-v1`；历史任务名 **C11** 是来源别名，与现行总账 **C11 极限回缩** 无关，不复用其编号。

**状态**：下列有限维命题为 `derived-checked`（2026-10-01，重新核验常数、修复迭代留域和最近零点的作用域）；未进行本轮外部文献或全球先行性核查。没有声称解决一般秩亏复合次正则。

<a id="cs-object"></a>
## CS-OBJECT · 定义及共同约定

空间均为有限维 Euclidean 空间，球 `B_R` 为开球，闭球写 `\overline B_R`。距离用同一 Euclidean 范数，空集距离为正无穷。对于有限连续函数，`∂` 表示 limiting subdifferential；本节凸复合在指定邻域是 subdifferentially regular，因此与 regular subdifferential 相同。

\[
F=\partial f,\quad r_F(x)=\inf_{v\in F(x)}\|v\|,
\quad\Gamma=\{x:0\in\partial f(x)\},
\]
\[
\Theta_2=\{x\in\Gamma:d^2f(x\mid0)(w)\ge0\ \forall w\},\qquad
d^2f(x\mid0)(w)=\liminf_{t\downarrow0,w'\to w}
\frac{f(x+tw')-f(x)}{t^2/2}.
\]

误差界始终是到指定集合的 ordinary subregularity，允许非孤立零集；不把距离换成到一个选定零点的距离。gauge 是残差侧函数 `Ψ:[0,∞)→[0,∞)`，非降、`Ψ(0)=0`、`Ψ(t)→0` 当 `t↓0`。

<a id="cs-transfer"></a>
## CS-TRANSFER-v1 · 目标集合转移

设有限连续 `f` 在 `B_α(\bar x)` 满足 `f≥f(\bar x)`，并有弱分离

\[
y\in\Gamma\cap B_\varsigma(\bar x)\implies f(y)\le f(\bar x).
\]

若集合 `S` 包含所有局部极小点且 `S⊆Γ`，则任取 `0<R<min(α,ς)`，对所有 `x∈B_{R/4}(\bar x)`，

\[
d(x,S)=d(x,\Gamma)=d(x,\{f\le f(\bar x)\}).
\]

**证明。** 在 `B_R` 内，驻点由两个相反函数值不等式成为局部极小点；低水平集点也达到邻域最小值，由 Fermat 条件成为驻点。这三个局部集合相等并含 `\bar x`。对指定 `x`，球外点距离大于 `3R/4`，而 `\bar x` 距离小于 `R/4`，故三个全局距离均由相同的球内部分决定。局部极小点的二阶次导数非负，所以 `S=Θ₂` 合法。

**不可删条件。** `f(x,y)=x²` 的零集是整条竖轴；即使弱分离成立，任意缩成 `S={(0,0)}` 都使 `(0,t)` 上残差为零而目标距离正。`f(x)=-x⁴` 说明仅 `\bar x∈Θ₂` 不保证局部最小，不能替代上面的假设。

<a id="cs-eb"></a>
## CS-EB-v1 · 原生外层 EB 到复合真实残差

依次固定以下全部数据：

1. `c:ℝⁿ→ℝᵐ` 连续，且在 `\overline B_R(\bar x)` 的开邻域为 `C^{1,1}`；`Dc` 在闭球上为 `β`-Lipschitz。
2. `A=Dc(\bar x)` 满行秩，`σ₀=σ_min(A)>0`，`βR<σ₀`。
3. `φ:ℝᵐ→ℝ` 有限凸，`C=argmin φ` 非空，`c(\bar x)∈C`；`f=φ∘c`，**全局目标** `S=c^{-1}(C)`。
4. 对每个 `z∈c(B_R)`，外层真残差满足 `d(z,C)≤Ψ_φ(d(0,∂φ(z)))`，其中 `Ψ_φ` 是上述 gauge。

令

\[
\sigma=\sigma_0-\beta R>0,\quad J=\|A\|+\beta R,
\quad r=\frac{R}{2(1+J/\sigma)}.
\]

则对所有 `x∈B_r(\bar x)`，

\[
\boxed{d(x,S)\le\sigma^{-1}\Psi_\phi(r_F(x)/\sigma).}
\]

此外 `Γ∩B_R=Θ₂∩B_R=S∩B_R`。特别地，若外层满足 `r_{∂φ}(z)≥m d(z,C)^a`，`m,a>0`，则

\[
q=1/a,\qquad K=\sigma^{-1-1/a}m^{-1/a},\qquad d(x,S)\le K r_F(x)^q.
\]

### 证明：修复、链式规则、残差的三个独立门

**(i) 几何修复。** 取 `B=A†`，`\|B\|=1/σ₀`，`E=ran Aᵀ`。对固定 `x∈B_r` 取最近外层解 `ẑ∈P_C(c(x))`。在仿射切片 `x+E` 定义

\[
T_x(y)=y-B(c(y)-\hat z),\qquad\theta=\beta R/\sigma_0<1.
\]

对切片内且位于闭球的两点，`BA|_E=I_E` 与积分余项给 `\|T_xy-T_xy'\|≤θ\|y-y'\|`。令 `D=d(c(x),C)/σ`；闭集合 `K_x=(x+E)∩\overline B_D(x)` 全在 `B_R`，因为

\[
\|x-\bar x\|+D\le(1+J/\sigma)\|x-\bar x\|<R/2.
\]

又 `\|T_xy-x\|≤θD+d(c(x),C)/σ₀=D`，故是完备 `K_x` 上的压缩自映射；若 `D=0` 已有 `x∈S`。不动点 `y` 满足 `B(c(y)-ẑ)=0`，而 `B:ℝᵐ→ℝⁿ` 单射，故 `y∈S`。于是 `d(x,S)≤d(c(x),C)/σ`。这一步明确证明自映射，未在得到收敛以后倒推迭代合法。

**(ii) 链式规则及目标。** 有限凸 `φ` 在紧邻域局部 Lipschitz；`c` 一阶展开与凸方向导数给
`f'(x;h)=max_{w∈∂φ(c(x))}〈Dc(x)ᵀw,h〉`。凸支撑不等式给每个 `Dc(x)ᵀw` regular subgradient；反向由所有方向的支撑函数比较得到 regular subdifferential 恰为这同一紧凸集。limiting subgradient 的极限表示中，局部有界外层次梯度可取收敛子列，凸次梯度图闭，故仍在该集合。因此

\[
F(x)=Dc(x)^T\partial\phi(c(x)).
\]

`Dc(x)ᵀ` 的最小奇异值至少 `σ`，于是 `0∈F(x)` 当且仅当 `0∈∂φ(c(x))`，当且仅当 `c(x)∈C`。这些点是全局极小点，故也在 `Θ₂`。

**(iii) 真残差。** 对每个外层 `w` 有 `\|Dc(x)ᵀw\|≥σ\|w\|`，取 inf 得 `r_F(x)≥σ r_{∂φ}(c(x))`。代入 (i) 及非降 gauge 得所述结论。三门是合取；仅链式规则没有误差界。

<a id="cs-prox"></a>
## CS-PROX-v1 · 独立 RL、局部 coverage 及轨道预算

在 CS-EB 全部数据上**再加** `\|w\|≤M` 对每个 `z∈c(\overline B_R)`、每个 `w∈∂φ(z)` 成立，令 `h=βM`。固定 `λ>0` 且 `λh<1`。则对每两个基点 `u,u'∈B_R` 及每个 `v∈F(u),v'∈F(u')`，

\[
\langle u-u',v-v'\rangle\ge-h\|u-u'\|^2,
\quad\|(u-u')-\lambda(v-v')\|
\le\frac{1+\lambda h}{1-\lambda h}\|(u-u')+\lambda(v-v')\|.
\]

每个输入 `x∈B_{R/2}` 有唯一基点位于 `B_R` 的近端输出 `y`；若 `x∈B_{r/2}` 则 `y∈B_r`。这里是**局部图块**，不排除球外的其他近端解。

**证明。** 凸支撑及 `C^{1,1}` 余项给 `f(u')≥f(u)+〈v,u'-u〉-h\|u'-u\|²/2`。交换两点相加得 hypomonotonicity。置 `a=u-u',b=v-v'`，先有 `\|a+λb\|≥(1-λh)\|a\|`，再用
`\|a-λb\|²=\|a+λb\|²-4λ〈a,b〉` 得 RL 常数。

函数 `f(y)+\|y-x\|²/(2λ)` 在闭球上强凸、连续，故唯一极小。其边界值大于 `\bar x` 处的值：利用 `f≥f(\bar x)` 及 `R-\|x-\bar x\|>\|x-\bar x\|`。因此极小点在内部，满足近端包含式；任何内部驻点由强凸性同样唯一。比较 `\bar x` 的目标值得 `\|y-x\|≤\|x-\bar x\|`，从而 `\|y-\bar x\|≤2\|x-\bar x\|`。

对实际输入 `x∈B_{r/2}`，`S` 全局闭且含 `\bar x`。任取最近点 `p∈P_S(x)`，有 `\|p-\bar x\|≤2\|x-\bar x\|<r`，故 `(p,0)` 在同一个图块中，可合法代入 RL。记 `d=d(x,S)`、`b=[λ(1-λh)]^{-1}`，则

\[
\|x-y\|\le\frac{d}{1-\lambda h},\qquad
 d(y,S)\le\Psi_F(bd),\quad\Psi_F(t)=\sigma^{-1}\Psi_\phi(t/\sigma).
\]

若某 `δ>0,0<κ<1` 满足 `Ψ_F(bd)≤κd` 对全部 `0≤d≤δ` 成立，且初值满足

\[
d_0\le\delta,\qquad
\|x^0-\bar x\|+\frac{d_0}{(1-\lambda h)(1-\kappa)}<r/2,
\]

则归纳保持每一步输入在 `B_{r/2}`，`d_k≤κ^kd_0`，步长可和，轨道收敛到 `S`。幂 gauge `Kt^q`、`q>1` 可取 `δ=(κ/(Kb^q))^{1/(q-1)}`，并有 `d_{k+1}≤Kb^q d_k^q`。零距离输入已固定。该结论不声称 `γ<1` 的 genuinely Hölder 机制。

<a id="cs-model"></a>
## CS-MODEL-v1 · 一个曲面，幂与非幂两个不同速率

令 `c(s,t)=t-(s_+)²`，`S={(s,(s_+)²):s∈ℝ}`。`Dc=(-2s_+,1)`，导数 Lipschitz 常数为 2，满行秩处处成立，`c` 是 `C^{1,1}` 而非 `C²`。取连续严格递增且无界的 `η`，`η(0)=0`，令

\[
\phi(z)=\int_0^{|z|}\eta(u)du,\quad
F(s,t)=\eta(|c|)\operatorname{sign}(c)(-2s_+,1).
\]

有 `Γ=Θ₂=S`，`r_F=η(|c|)\sqrt{1+4s_+²}`。竖向修复到 `(s,(s_+)²)` 直接给比通用常数更好的

\[
d((s,t),S)\le\eta^{-1}(r_F(s,t)).
\]

- `η(u)=u^a,0<a<1`：有效最佳指数为 `q=1/a`，常数 1。沿 `(0,t)`、`0<t<1/2`，到平直半轴最近点是原点；到曲面半支的距离平方为 `v+(t-v)²,v≥0`，导数 `1-2t+2v>0`，故 `d=t,r_F=t^a`。因此更大指数以及此指数下更小常数均失败。
- `η(u)=u log(e/u)` 在 `[0,1]`，`η(u)=u` 在 `[1,∞)`：连续严格递增。有效 gauge `η^{-1}(r)∼r/log(1/r)=o(r)`，但沿同一竖线，任意 `q>1` 有 `d/r_F^q=t^{1-q}/[log(e/t)]^q→∞`，没有该幂 EB。

后一例可独立用 CS-PROX 的弱凸/coverage 证明；在 `B_R` 上取 `h=2η(R+R²)`，选择 `λh<1`。用模型 gauge 及相应留域预算，距离收缩半径可取

\[
\delta_\kappa=\min\{1/\kappa,(e/\kappa)e^{-b/\kappa}\}.
\]

因为 `bd≤η(κd)` 正好等价于 `b≤κ log(e/(κd))`。在正竖线上唯一局部输出仍在竖线，满足

\[
t_k=t_{k+1}+\lambda t_{k+1}\log(e/t_{k+1}),\qquad
 t_{k+1}\sim\frac{t_k}{\lambda\log(1/t_k)}.
\]

渐近式可由设 `u=t_{k+1}` 后 `t_k=u[1+λlog(e/u)]` 得 `log(1/t_k)/log(1/u)→1`。所以收敛超线性，但对任意 `p>1`，`t_{k+1}/t_k^p→∞`，没有统一 Q-order `p`。

<a id="cs-objections"></a>
## 攻击、适用边界与下一条可以增长的 Claim

| 障碍 | 明确反例或尚缺义务 | 重启方式 |
| --- | --- | --- |
| 删满行秩 | `c(x)=x²,φ(z)=z²/2,\bar x=0` 保留外层线性 EB 及 `c(\bar x)∈C={0}`，却 `F(x)=2x³`，不存在复合线性 EB；满行秩不能直接删去 | 原生乘子不抵消或临界方向资料，独立证明新的桥 |
| 用 Lipschitz 梯度生产高阶 EB | 若 `F` 单值 ℓ-Lipschitz 且零集闭，则靠近零集 `\|F(x)\|≤ℓd(x,S)`；非零距离趋零时 `d≤K\|F\|^q,q>1` 矛盾 | 保留非 Lipschitz 外层或改速率目标 |
| Clarke Hessian 代替 `Θ₂` | `g(x)=x²(1.1+sin log|x|),g(0)=0` 为 `C^{1,1}` 强极小；二阶导极限区间 `[2.2-√10,2.2+√10]` 含负值；`d²g(0|0)(w)=0.2w²` | 使用实际 second subderivative；“全部 PSD”会漏极小点，“存在 PSD”会把 `-g` 的极大点纳入 |
| 只知局部 EB 就声称所有完整近端轨道收敛 | 球外图支未被本证书检查 | 保持局部输出量词，或另证明完整纤维一致性 |
| 新颖性 | 当前用的是 submersion、凸链式规则与弱凸近端几何；指定一手版本和逐条边界已核；同目标/残差桥与全球先行性另留 | 在确切版本上另做先行性门，不把本推导标为新定理 |

**开放增长口 `CS-OPEN-RANK`。** 对 `f=g+φ∘c`，允许 `g,c∈C^{1,1}`、`Dc` 秩亏、外层活动面变化，从有限活动面资料及所有相关乘子的定量不抵消条件，导出到**指定 `Θ₂`** 的可计算 gauge 和正半径；不得把待证的残差增长直接当作输入。先构造保留完整原生条件且发生秩亏的测试模型，再提出版本；同时验目标一致性与邻域量词。这个开放目标不影响上面的满秩基线被立即使用。

<a id="cs-sources"></a>
## 来源、证据及未覆盖内容

主要原件为 [9/14 复合模块](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/C11复合次正则_定量模块与未解边界.md)：§2→CS-TRANSFER；§3→CS-EB；§4→CS-PROX；§5.1–5.2→CS-MODEL；§6→攻击；§10→开放增长口。

其字节与 [9/09 T4 ZIP](../../history/sources/次单调论文研究/RL_T4_CODEX_HANDOFF_2026-09-09.zip) 成员 `ATTACK_C11_COMPOSITE_GENERALIZED_SUBREGULARITY.md` 完全一致，SHA-256 为 `d9f9e5c53c41d827a7fd25250fbd5cbee3c3f2d08c41d245dc9b8f552b084619`，本轮已比对。它们是同一证据而非两次独立证明。

[历史 T4 量词审计](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/04_证明审计与敌对审稿/定理量词与精确性_独立数学审计_T4.md) §4 提醒 gauge 非降、coverage、全轨道预算必须同时成立；其审计对象不是本复合模块，不能称其直接审定本节。

[历史验证器](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/06_验证程序/验证_C11复合次正则.py) 仅检验有限算例与代数；本文件证明不依赖其运行。后续增量已把历史 §5.3 的满秩真多值尖点 [C40](../topics/composite_regular/cusp_identification.md) 与 §6.2 的目标障碍 [C41](../topics/composite_regular/oscillating_target.md) 独立重写，均有比原观察更明确的范围；§8已在[逐断言范围](../audit/C11_M1_SOURCE_SCOPES.md#cm-scope)枚举；[固定一手卡](../audit/C11_M1_LITERATURE_INTERFACES.md)区分实际二阶目标、prox残差及定理前件，全文/刊本/历史行为和优先权仍有具体未闭门。整件其它内容仍需逐项验收。
