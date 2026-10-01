# 初值稳定性团队综合结果：独立压力审核

日期：2026-09-19。对象：本轮 `01_terminology_map.md` 至 `06_synthesis.md` 六份报告（均完整阅读），以及修订稿 `solution_selection_revised_v1/research_note.md` §5.2。未改动任何研究稿，未重审原 RLEB 无关内容，未委派。

## 0. 终判

**MINOR_REPAIR。** 综合主结论成立，未发现需要推翻的数学错误或“已有研究”对象偷换。普通 hypo/cohypo 的步长方向与常数正确；§6 的两块递推、加权乘积及变系数模型也通过独立算式核验。

需要两项小修：

1. 将“比全局 hypomonotonicity 更弱”限定为“允许某些普通 hypomonotonicity 排除的稳定奇异模型”，不宣称两套完整假设存在逻辑包含。已有报告多处提醒不是强弱总序，但最终解释仍须始终保持这一限制。
2. 若将 §6.2 单独摘录成命题，补全共同坐标、统一常数、全部轨道对与极限落在同一坐标片的量词。当前综合稿靠 §2 的总假设能够读通；脱离上下文的命题版尚不够自含。

这两项不会改变“已有正面理论很多；真正待做的是原算子图到保留奇异性的稳定证书之间的桥接”的判断。§6.2–6.3 是正确的标准充分接口和说明模型，不是已完成的 RLEB 新定理。

## 1. “有人研究过”是否用了错误对象？

### 1.1 直接先例确实存在

本审核再次打开并核对以下原文，而不是仅依赖小组转述：

- Andrzej Wiśnicki, *Hölder Continuous Retractions and Amenable Semigroups of Uniformly Lipschitzian Mappings in Hilbert Spaces*, Lemma 1，[arXiv:1204.6464v2](https://arxiv.org/pdf/1204.6464v2)，[DOI 10.12775/TMNA.2014.006](https://doi.org/10.12775/TMNA.2014.006)。该引理直接研究原迭代的极限，要求 Lipschitz 单步与所有初值统一的几何增量界；并非只证明固定点集上“存在某回缩”。
- Wolf-Jürgen Beyn, *On Smoothness and Invariance Properties of the Gauss-Newton Method*, Theorems 2.1–2.2，[原始扫描件](https://noah.nrw/ubbihs/download/pdf/5114560)，[DOI 10.1080/01630569308816536](https://doi.org/10.1080/01630569308816536)。本审核直接查看 p.505 的定理原页：正则零点、足够光滑时，共同初值邻域上的原 Gauss–Newton 极限映射为相应光滑阶。

因此回答“初值到最终解稳定性是否有人直接研究过”为**是**，已有第一手定理证据，结论无需依赖任何题名相似的参数稳定论文。

### 1.2 综合报告正确区分的三种间接证据

1. BMW 的 resolvent 正则性是单步接口；接共同轨道收敛/尾界后才给极限稳定。综合稿将其归为组合推论，正确。
2. Wiśnicki 主 Theorem 2 使用辅助平均映射得到回缩；综合稿没有把它偷换成任意原 Picard 极限，正确。
3. tilt stability、强度量正则、partial smoothness/finite identification 本身不直接给所问的非唯一解选择。报告均保留了这个区别。

2026 年文献亦作了必要域限制。本审核再次核对 [Chen–He–Huang v2 Theorem 2](https://arxiv.org/html/2605.17384v2)：输入是切丛零截面附近的 `(x,η)`；核对 [Zheng–Chen v3 Theorems B.1–B.2](https://arxiv.org/pdf/2606.31738v3)：固定正则化情形、仿射初值域。综合稿没有把两者扩成任意环境域、任意 RLEB 算子的结论。

### 1.3 必须保留的最小反例

“单步 Lipschitz ⇒ 极限连续”不成立。报告中的双井例正确：

\[
f(u)=\tfrac14(u^2-1)^2,\qquad 0<\lambda<1,
\]

完整 prox 为严格递增满射

\[
h(u)=(1-\lambda)u+\lambda u^3
\]

的逆，故单步为 `(1-λ)^{-1}`-Lipschitz，但

\[
\Pi(x)=\operatorname{sgn}x\quad(x\ne0),\qquad\Pi(0)=0.
\]

取 `x_n=h^n(1/2)→0`，则 `T^n x_n=1/2` 而 `Π(x_n)=1`。这精确排除了共同初值域上的一致消失点尾。此例不能称作严格 RLEB 共同预算的反例；综合稿没有这样做。

## 2. hypo/cohypo 参数：独立推导与阈值压力测试

以下取 `λ>0`、`ρ≥0`，并固定同一算法和图域。

### 2.1 普通 hypomonotonicity：小步长

令 `x=u+λa, y=v+λb`，若

\[
\langle u-v,a-b\rangle\ge-\rho\|u-v\|^2,
\]

则

\[
(1-\lambda\rho)\|u-v\|^2
\le\langle u-v,x-y\rangle.
\]

所以 `λρ<1` 给

\[
\operatorname{Lip}T\le (1-\lambda\rho)^{-1}.
\]

该式只能证明受控图域的至多单值及 Lipschitz 性，存在性、满射性、完整图纤维仍须另外核验。

阈值不能随便取等号：`F(u)=-ρu` 在 `λρ=1` 时有 `(I+λF)(u)=0`，输入 0 的完整 resolvent 为整条直线，非零输入无解。

再与共同点尾 `Mσ^n` 平衡，令

\[
L=(1-\lambda\rho)^{-1}>1,\quad
\theta=\frac{\log(1/\sigma)}{\log L+\log(1/\sigma)},
\]

得到正阶 Hölder。指数与方向均正确。局部尺度若是关于**输入对**的 Lipschitz 尺度，`L^jδ≤L^nδ=O(δ^θ)` 闭合；若从只限**输出图点距离**的 hypo 不等式出发，还要先用既有 RL 连续接口保证输出图点进入该尺度，不能将输入距离和图点距离混称。综合稿 §4.1 的输入尺度写法可保留。

### 2.2 Cohypomonotonicity：足够大步长

若改为

\[
\langle u-v,a-b\rangle\ge-\rho\|a-b\|^2,
\]

则

\[
\|x-y\|^2\ge\|u-v\|^2+
\lambda(\lambda-2\rho)\|a-b\|^2.
\]

故 `λ≥2ρ` 给非扩张；`λ>2ρ` 给

\[
\alpha=\frac{\lambda}{2(\lambda-\rho)}\in[1/2,1)
\]

的 averaged 参数。再次核对 [Bauschke–Moursi–Wang Proposition 3.13、Corollary 3.14](https://arxiv.org/html/1902.09827v1)：令其算子为 `λF`，其带符号参数为 `-ρ/λ`，即得到上述阈值。

阈值压力测试：取 `F(u)=-u/ρ`、`ρ>0`。该图恰好 `ρ`-cohypomonotone，

\[
J_{\lambda F}=(1-\lambda/\rho)^{-1}I.
\]

当 `ρ<λ<2ρ` 时映射扩张；`λ=2ρ` 时为 `-I`，非扩张但非零轨道不收敛；`λ>2ρ` 时严格收缩。于是综合稿正确保留“边界仍须另有收敛证明”。

本审核亦核对 [Combettes–Pennanen Theorem 3.1](https://pcombet.math.ncsu.edu/sicon3.pdf)：其 proximal 步长记为 `γ_n`、松弛系数记为 `λ_n`。固定精确不松弛取 `λ_n=1` 时，其余量条件确实要求 `γ_n>2ρ`。不能将两个不同的 λ 记号混淆；综合稿当前换元正确。

## 3. 原 §5.2 与 Dini 放宽

原命题

\[
T(a,r)=(a+B(a,r),qr)
\]

及 `Lip_a B(·,r)≤Cr^η`、统一法向 `γ`-Hölder 条件，确实给有限长度和稿中的混合估计。证明不需要额外的全方向 Lipschitz 性。

将 `Cr^η` 替换为非减 `ω(r)` 且

\[
S_\omega=\sum_{k\ge0}\omega(Rq^k)<\infty
\]

后，两轨道差满足

\[
u_{k+1}\le(1+\omega(Rq^k))u_k+Hq^{\gamma k}|r-s|^\gamma,
\]

故

\[
u_\infty\le e^{S_\omega}
\left(u_0+\frac{H}{1-q^\gamma}|r-s|^\gamma\right).
\]

Dini 对应也正确，因为

\[
\log(1/q)\sum_{k\ge1}\omega(Rq^k)
\le\int_0^R\omega(t)\,\frac{dt}{t}
\le\log(1/q)\sum_{k\ge0}\omega(Rq^k).
\]

这里要求 `ω(R)<∞`。这是标准充分放宽，不是必要条件：例如 `B≡0` 时解选择已稳定，与人为选取的上界 `ω` 是否可和无关。现有报告未声称必要，正确。

## 4. 非三角块条件：推导通过，小修量词

### 4.1 加权估计逐行复核

记 `ω_k=ω(r_k), b_k=b(r_k)`。假设同一共同轨道层上的所有两点满足

\[
u_+\le(1+\omega_k)u+Av,
\qquad
v_+\le\vartheta v+b_k u,
\]

其中 `A≥0, 0≤ϑ<1`，`ω_k,b_k≥0` 且两和有限。选

\[
c>0,\qquad c\ge A/(1-\vartheta).
\]

则

\[
\begin{aligned}
u_++cv_+
&\le(1+\omega_k+cb_k)u+(A+c\vartheta)v\\
&\le(1+\omega_k+cb_k)u+cv\\
&\le(1+\omega_k+cb_k)(u+cv).
\end{aligned}
\]

所以

\[
u_k+cv_k\le e^E(u_0+cv_0),\quad
E=\sum_j(\omega_j+cb_j)<\infty.
\]

这是正确的加权乘积估计；无需要求反馈 `b_k` 恒为零，亦无需小到某一统一常数，只需其累计预算有限。

### 4.2 摘成正式命题时应补的准确句子

建议补明：

> 存在同一初值域 `U`、同一轨道域 `W` 和一张预先指定的坐标图 `Φ:x↦(a,n)`，覆盖所有 `T^kU` 及其极限。图与解集参数化在这一共同范围有统一 Lipschitz 常数；`S∩W` 对应 `n=0`。映射 `χ` 固定、与所求 `Π_T` 无关，`χ(0)=0`，并满足统一 `γ`-Hölder 估计。所有轨道已知收敛到 `S∩W`。对每一 `k` 及每一对 `x,y∈T^kU`，块估计使用相同 `A,ϑ,ω_k,b_k`。

若称 `χ` 为“坐标”，再要求它在法向范围内为单射/同胚；单纯继承估计本身只需上述统一 Hölder 性。多法向维度不能直接写一维 `sgn(n)`，应给具体径向或逐坐标版本并验证其模。

假设坐标前向常数为 `L_Φ`、解集切向参数化常数为 `L_S`、`χ` 的 Hölder 常数为 `H_χ`，则取极限明确给

\[
\|\Pi_Tx-\Pi_Ty\|
\le L_S e^E\bigl(L_\Phi\delta+cH_\chi L_\Phi^\gamma\delta^\gamma\bigr).
\]

在 `δ≤D` 上由 `δ≤D^{1-γ}δ^γ` 得 Euclidean `γ`-Hölder。若所有图常数只是逐点有限而无共同上界，这一步不能照写。

这是**正则性继承**接口；既有轨道收敛和留域预算不能在摘录时被删除。它也不需要再次假设几何点尾：共同收敛与可和块系数已经足够完成上述极限传递；RLEB 的作用是给这些输入之一。

### 4.3 非三角说明模型通过

对综合稿

\[
T(a,n)=(a+B(a)|n|^\gamma,\ q(a)|n|),
\quad0<q_-\le q(a)\le q_+<1,
\]

在固定 `w=sgn(n)|n|^γ` 中是

\[
(a,w)\mapsto(a+B(a)|w|,\ q(a)^\gamma|w|).
\]

`B` 有界 Lipschitz、`q` Lipschitz，故在 `|n|,|m|≤r_k` 上

\[
\omega_k=\operatorname{Lip}(B)r_k^\gamma,\quad
A=\|B\|_\infty,\quad\vartheta=q_+^\gamma,
\quad b_k=\operatorname{Lip}(q^\gamma)r_k^\gamma.
\]

`q_->0` 确保 `q^γ` 的 Lipschitz 常数有限。`r_k=Rq_+^k` 给可和性，且切向总漂移

\[
\sum_k\|a_{k+1}-a_k\|
\le\frac{\|B\|_\infty R^\gamma}{1-q_+^\gamma}<\infty.
\]

因此模型本身的留域（全切向域版本）、收敛和稳定性均成立。`q` 依赖 `a` 时是真正法向回授，不是固定 `r_+=qr`。

但是：这仍未独立建立相应完整多值算子的全部 RL、min-residual 与严格兼容。综合报告对此已明确保留，不能在给用户的简报里省掉。

## 5. “更弱”、排除坏例与标准性

### 5.1 它确实排除当前坏例的致坏机制

在原自然法切坐标中，固定 `r>0` 比较 `(z,ε,r)` 与 `(z,0,r)`，`0<ε<r`。法向差为 0，而切向差满足

\[
u=\varepsilon,\qquad u_+=\varepsilon+\sqrt\varepsilon.
\]

故任何有限 `ω(r)` 都无法满足第一块。综合稿的计算正确。该计算直接排除的是**指定自然坐标**；若讨论任意重新参数化，必须另证坐标正则性及共同常数。不能仅凭这个算式宣称排除一切坐标选择。

### 5.2 确实保留普通 hypo 排除的稳定模型

二维模型

\[
T_0(z,r)=(z+\sqrt{|r|},\ |r|/4)
\]

的实际极限为

\[
\Pi_{T_0}(z,r)=(z+2\sqrt{|r|},0).
\]

它符合候选的法向 Hölder 坐标机制。完整逆图算子在输出 `(u,v),v≥0` 上为

\[
F(u,v)=\{(-2\sqrt v,3v),\ (-2\sqrt v,-5v)\}.
\]

取 `U_t=(t,t)`、`A_t=(-2√t,3t)` 与零图点比较：

\[
\frac{\langle U_t,A_t\rangle}{\|U_t\|^2}
=\frac32-\frac1{\sqrt t}\longrightarrow-\infty.
\]

所以不存在有限普通 hypo 常数，而极限仍有正阶 Hölder。这足以说明：候选不要求回到全方向 Lipschitz/普通 hypo 的范围。

### 5.3 但“不要求 hypo”不等于“逻辑上弱于 hypo”

最简单的反向提醒是 `F(a,n)=(0,n^3)`：它全局单调，极限选择为 `(a,0)`，但 `J_F` 的法向导数在解集处为 1，固定幂坐标下没有 `ϑ<1` 的法向两点收缩。该例不具有所用几何 RLEB 预算，故只能说明在不统一背景假设时不能排强弱总序。

即使保留几何收敛背景，指定坐标块条件也并非自动由单调性推出。下面给可解析核验的反例，避免只靠上述背景不一致的例子。

令 `r_j=4^{-j}`，`j∈Z`。在每个正区间 `[r_j/4,r_j]` 定义

\[
t(x)=
\begin{cases}
r_j/16,&r_j/4\le x\le13r_j/16,\\
x-3r_j/4,&13r_j/16\le x\le r_j,
\end{cases}
\]

并作奇延拓、`t(0)=0`。它连续、非减、1-Lipschitz，并且 `|t(x)|≤|x|/4`。故 `T(a,n)=(a,t(n))` 是全空间 firmly nonexpansive；由标准逆图编码 `F=T^{-1}-I` 为 maximal monotone，完整 resolvent 正是 T。

令输出为 `(a,v)=T(a,n)`、残差为 `(0,n-v)`。因 `|n|≥4|v|` 且同号，

\[
\operatorname{dist}((a,v),S)=|v|
\le\tfrac13|n-v|.
\]

此式对整个逆图成立，所以也对真实 min-residual 成立。all-pairs reflected RL 可取 `γ=1,L=1`，`λ=1, ψ(s)=s/3` 的原严格兼容因子为 `1/3<1`；实际距离因子为 `1/4`。

但每个邻域内都有斜率为 1 的 ramp。对于固定幂坐标 `χ(n)=sgn(n)|n|^γ`，在正 ramp 内

\[
\frac{d\chi(t(n))}{d\chi(n)}
=\left(\frac{t(n)}n\right)^{\gamma-1}\ge1
\quad(0<\gamma\le1).
\]

比较同一切向坐标的两点时 `u=0`，所以反馈项完全消失；无法满足任何 `v_+≤ϑv`、`ϑ<1`。这证明**在指定坐标中**，候选块条件不是即使带严格几何 RLEB 的整个单调类的逻辑弱化。此例不半代数；本任务并未证明或需要半代数子类中的全包含/非包含。

因此建议最终措辞精确改为：

> “它与普通 hypo 条件不是简单包含关系，但能保留后者排除的一些法向非 Lipschitz 稳定模型；它是面向当前奇异结构的另一套充分证书。”

### 5.4 是否仅为标准？

是：§5 的 Dini 放宽与 §6.2 的加权乘积是标准分析机制。候选模型证明条件非空、允许多解和非三角，并不能单独建立发表增量。综合稿正确把真正待证内容放在“从原始算子图/残差可验证条件导出这些块界，同时闭合完整 resolvent 和 RLEB 接口”。该待证桥接未完成，不能替它补写首创声明。

## 6. 当前稿与未来工作的分界

综合建议合理：

- 当前稿可以补已有正面基线、准确引 Wiśnicki 与非扩张/resolvent 文献，平衡“坏例”叙述。
- 原 §5.2 保留；Dini 放宽可作为标准备注，不能包装新主定理。
- §6.2–6.3 可作为研究备忘录/未来工作接口，暂不当作已经审完的新 RLEB 结果塞进主贡献。
- 将来若要形成新增主定理，应同时证明共同域、完整纤维、真实残差、全对 RL 与可验证切向证书；不能仅证明一次标准 Gronwall 然后宣称创新。

本次仅审核，不授权或实施论文修订。未重新启动新的原创提案。

## 7. 关闭清单

| 检查项 | 判定 |
|---|---|
| 实际 Picard 极限与其他稳定性对象的区分 | PASS |
| hypo/cohypo 归一化、步长方向、等号边界 | PASS |
| 三角命题与 Dini 放宽 | PASS，标准推论 |
| 非三角块估计及加权乘积 | PASS |
| 变系数说明模型 | PASS，仅稳定性模型，非完整 RLEB 构造验收 |
| 指定自然坐标下排除 cap 坏例 | PASS |
| “严格更弱/最弱”解释 | MINOR_REPAIR：改为不要求 hypo、非包含比较 |
| 单独摘录命题的坐标与共同量词 | MINOR_REPAIR：按 §4.2 补全 |
| 当前稿补基线、真正桥接留未来 | PASS |

**最终状态：MINOR_REPAIR；两项小修后可作为可信的文献—研究方向综合答复，不足以宣称已经找到最弱条件或已经完成新 RLEB 正面定理。**
