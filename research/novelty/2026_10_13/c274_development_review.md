# C274 与 C249：按理论发展问题进行的独立新颖性审查

日期：2026-10-13。审查对象：C274-v1 `research/canonical/mixed_power_kernel_structural.md`；C249 `research/canonical/physical_rleb_gppa.md`。本文件是独立审查，不修改规范命题，也不把检索范围内未发现相同公式当作优先权证据。

## 判断

C274 是正确且可复核的模型级结构验证；但本次没有识别出足以支持“新的收敛原理”的证据。其完整近端与全局点收敛直接处于经典 Bregman 理论内；非强凸核、非孤立解集并不构成经典理论的排除条件。显式极限是到仿射解集的 Bregman 投影。将守恒的切向对偶变量消去后，模型就是具有平坦径向核的普通法向 Bregman PPA。更强地，对于整个 SPD 二次目标子类，对偶化并作线性变换后恰好是普通欧氏 PPA；已有增长条件定理给出其 `q−1` 上阶。保留下来的较具体内容是显式有限物理长度、切向漂移、锐两侧渐近式、谱系数，以及把这些量完整代入 C249 的证书。这些目前更合理地归类为常规但有用的定量扩展，精确公式的文献优先权仍未决。

C249 的抽象范围比凸 Bregman PPA 广，不能由 C274 的经典归属推出 C249 全部已知。然而，其证明主线是一步核增量估计、误差界复合、物理位移可和性、有限前缀留域的组合。当前证据支持“接口明确、量词审查有价值”，尚不支持新的普遍机制或已证明的明显理论跃迁。

| 内容 | 本次分类 | 依据与界限 |
| --- | --- | --- |
| 非二次、非强凸的 Legendre/Bregman 核 | 已知理论对象 | 范数幂的总凸性和 Bregman 迭代理论已经直接处理它们；Hessian 退化不排除严格凸性或总凸性。 |
| C274 完整近端存在唯一、全局点收敛 | 经典定理直接推论 | BBC 2003 的完整映射与收敛框架；下文给出逐项映射。 |
| 极限由切向对偶守恒决定且不依赖步长和法向目标 | 已知概念的直接推导 | 仿射约束 Bregman 投影的最优性条件；显式公式来自代入当前核。 |
| `q−1` 超线性上阶，整个 SPD 二次子类 | 等价变换后的已知定理推论 | 精确化为欧氏 PPA；Oikonomidis 等 v3 Theorem 3.6。不是仅作不同算法间的类比。 |
| 一般光滑强凸法向目标的锐 `q−1` 阶 | 常规局部渐近扩展 | 约化核梯度的首项与目标 Hessian 的逆相乘。 |
| 全局物理长度、尾长等价、谱系数 | 模型级定量扩展 | 径向核的一步标量预算与特征空间比值；没有查到逐字相同定理，但这不自动构成实质概念新意。 |
| 中心层与非中心层不同阶 | 首项次数变化的直接结果 | 约化核在零切向对偶层为 `p` 次，非零层的法向首项为 `q` 次。 |
| C249 的一般非势、非单射、多值接口 | 尚未完成先行性裁决 | 比当前凸模型宽；需另给一个旧理论实质失效而接口仍有非平凡效果的自然问题。 |

## 1. 先问经典理论已经解决了什么

20 世纪末至 2000 年前后的相关问题，并非只研究“核 Hessian 有统一正下界时怎样收敛”。已读的一手文献明确研究了：一般 Bregman 近端的存在性；从 Bregman 距离下降到原空间收敛需要什么几何条件；总凸性、序列一致性和范数幂之间的关系；以及用非线性模把核梯度差转换成物理误差。因此，把物理空间误差与核几何分开核验是合理做法，但不能仅凭术语改变就视为新研究问题。

**BBC 2003**：Bauschke–Borwein–Combettes, *Bregman Monotone Optimization Algorithms*, SIAM J. Control Optim. 42(2), 596–636, DOI [10.1137/S0363012902407120](https://doi.org/10.1137/S0363012902407120)。已读[作者全文](https://pcombet.math.ncsu.edu/sicon2.pdf)。所用定位为 Theorem 3.13、Corollary 3.14、Proposition 3.22、Corollary 3.25、Proposition 4.13、Theorem 4.14、Conditions 4.3–4.4、Example 4.6。作者稿页码与正式期刊页码不同；定理号是本次稳定定位。

**Butnariu–Iusem–Resmerita 2000**：*Total Convexity for Powers of the Norm in Uniformly Convex Banach Spaces*, J. Convex Anal. 7(2), 319–334，DOI [10.68381/jca07016](https://doi.org/10.68381/jca07016)。已读[出版方全文](https://journalofconvexanalysis.com/articles/jca07016/jca07016.pdf?v=2)，Theorem 2.1（p.321）及 Corollary 2.4（p.324）。范数幂 `||·||^r, r>1` 在一致凸空间中总凸，且有相应有界性与序列一致性。这直接包括当前有限维块 `ℓ_q` 范数的 `p` 次幂。该文后面的投影可行性算法不是当前 PPA，不用它冒充 PPA 收敛定理。

**Butnariu–Iusem–Zălinescu 2003**：*On Uniform Convexity, Total Convexity and Convergence of the Proximal Point and Outer Bregman Projection Algorithms in Banach Spaces*, J. Convex Anal. 10(1), 35–61，DOI [10.68381/jca1002](https://doi.org/10.68381/jca1002)。已读[全文](https://www.heldermann-verlag.de/jca/jca10/jca0345.pdf)，§4.5、Theorem 4.5、式(37)，pp.54–56。该结果用总凸性模的逆控制原空间误差，说明这种转换本身已有明确研究。其目标函数须总凸且有效域闭；故不能直接套在完整空间的平坦目标 `f(u,z)=g(u)`。消去切向变量后，闭有效域的强凸 `g` 子类符合这一障碍；一般 lsc `g` 的有效域未必闭，仍不能过度覆盖。全体 C274 的直接经典覆盖由 BBC 框架给出。

### BBC 对整个 C274 的映射

为避免符号冲突，下文用当前模型的 `h` 表示 BBC 的核，用 `f(u,z)=g(u)` 表示其目标。所有论证都针对完整关系，不选择近端分支。

1. `X` 有限维，故反身。`h` 全域、`C^1`、严格凸、超强制，因而是全域 Legendre 核且共轭也全域。`F=∂f` 是极大单调；`dom F⊂int dom h=X`。Theorem 3.13 / Corollary 3.14 的映射条件成立。
2. `f` proper、lsc、凸且由 `g(0)` 下界控制；`dom f` 与 `int dom h` 相交。Proposition 3.22 / Corollary 3.25 给完整 Bregman argmin、核预解式、固定点集和单值性；无需给 `h` 加局部二次强凸常数。
3. 对任意 `s∈S`，标准三点恒等式及单调性给

   `D_h(s,x_{k+1})+D_h(x_{k+1},x_k)≤D_h(s,x_k)`。

   这是 Proposition 4.13 的下降关系。取 `s=0`，由 Euler 齐次恒等式有 `D_h(0,x)=(p−1)h(x)`，于是全部轨道有界。
4. 因而 `D_h(x_{k+1},x_k)→0`。当前有限维紧集上的 `C^1` 严格凸性足以推出 `||x_{k+1}−x_k||→0`：否则取间距有正下界的收敛子列，连续性给出两个不同点之间的 Bregman 距离为零，矛盾。这里不需要假定二次下界。
5. `∇h` 在有界集上一致连续，所以所选完整包含值 `(∇h(x_k)−∇h(x_{k+1}))/λ→0`。`∂f` 的闭图性使每个聚点属于 `S`。
6. `S` 凸，`h|S` 严格凸，有限维梯度连续；Example 4.6 验证 Condition 4.3。上述紧性论证验证 Condition 4.4。Theorem 4.14 给出点收敛；有限维中强弱收敛相同。

这证明的是**全局点收敛已有直接覆盖**。仅有 Bregman 增量可和并不自动给出欧氏路径长度可和；C274 的物理长度仍有单独计算内容。

## 2. 一个消去非孤立解集的精确约化

本节是本次直接数学推导，不声称在上述文献中出现了相同公式。

置 `κ=P_T∇h(x_0)`，其中 `P_T` 为切向块投影。完整包含式立即给 `P_T∇h(x_k)=κ`。定义

\[
\phi_\kappa(u)=\inf_z\{h(u,z)-\langle\kappa,z\rangle\}.
\]

由于 `h` 严格凸且超强制，对每个 `u` 有唯一内层极小点 `zκ(u)`；它满足 `∇_z h(u,zκ(u))=κ`。唯一性与包络求导给

\[
\nabla\phi_\kappa(u)=\nabla_u h(u,z_\kappa(u)).
\]

`φκ` 有限、严格凸、可微且强制。将完整近端目标先对 `z` 极小化，得到完全相同的法向迭代：

\[
u_{k+1}=\arg\min_u\{\lambda g(u)+\phi_\kappa(u)
-\langle\nabla\phi_\kappa(u_k),u\rangle\},
\qquad z_k=z_\kappa(u_k).
\tag{R1}
\]

这是普通法向 Bregman PPA，其目标有唯一极小点 `u=0`。所以当前非孤立解集不是一个必须发展全新收敛机制才能处理的困难：其切向自由度被守恒对偶变量固定，精确地成为一个参数。

记 `p*=p/(p−1), q*=q/(q−1)`。块范数的对偶范数及共轭定义给

\[
\phi_\kappa^*(\xi)=h^*(\xi,\kappa)
=\frac1{p^*}\bigl(\|\xi\|^{q^*}+\|\kappa\|^{q^*}\bigr)^{p^*/q^*}.
\tag{R2}
\]

确切地，`sup_u(<ξ,u>−inf_z[h−<κ,z>])=sup_{u,z}(<ξ,u>+<κ,z>−h)`。没有隐藏的对偶交换条件。

若 `κ≠0`，设 `t∞=||κ||^{1/(p−1)}`。当前约化核是径向的，且

\[
\phi_\kappa(u)=\phi_\kappa(0)+\frac{t_\infty^{p-q}}q\|u\|^q+o(\|u\|^q),
\quad
\nabla\phi_\kappa(u)=t_\infty^{p-q}\|u\|^{q-2}u+o(\|u\|^{q-1}).
\tag{R3}
\]

这是 C274 的 `t(r)=t∞+O(r^q)` 与法向梯度公式的直接积分结果。若 `κ=0`，则 `zκ(u)=0`，并且**精确地** `φ0(u)=||u||^p/p`。所谓分层就是约化核首项次数从 `q` 改为 `p`，并不是未知的多值动力学现象。

## 3. 显式极限其实是 Bregman 投影

任意已收敛轨道的极限满足 `u∞=0` 与 `∇_z h(0,z∞)=κ`。另一方面，到仿射解集的 Bregman 投影是

\[
\arg\min_{(0,z)\in S}D_h((0,z),x_0)
=\arg\min_z\{\|z\|^p/p-\langle\kappa,z\rangle\}.
\]

它有唯一解，最优性条件恰为同一方程。因此

\[
x_\infty=P_S^h(x_0),\qquad
z_\infty=\|\kappa\|^{(2-p)/(p-1)}\kappa
\quad(\kappa\ne0).
\tag{R4}
\]

代入 κ 即得 C274 的 `z∞=[1+(r0/t0)^q]^{−(q−p)/(q(p−1))}z0`。不依赖 λ、g 的现象是投影与对偶守恒的直接后果。

作为明确的一手概念参照，Gunasekar–Lee–Soudry–Srebro, *Characterizing Implicit Bias in Terms of Optimization Geometry*, ICML 2018/PMLR 80， [正文](https://proceedings.mlr.press/v80/gunasekar18a/gunasekar18a.pdf) Theorem 1 与[补充材料](https://proceedings.mlr.press/v80/gunasekar18a/gunasekar18a-supp.pdf) Appendix A.1，已经用“对偶增量在约束法空间内 + 投影 KKT”刻画仿射可实现问题的镜像下降极限。其原定理假设强凸势、显式镜像下降且条件于收敛，故不是对 C274 的直接套用。这里的评价是**同一已知投影概念、同一短证明机制**；当前隐式迭代和严格凸核的扩展由上面的完整推导完成，而不是偷换文献假设。

## 4. 整个 SPD 二次子类精确化为欧氏 PPA

设 `g(u)=<Au,u>/2`，`A` 任意 SPD。置

\[
w_k=\nabla\phi_\kappa(u_k),\quad
\eta_k=A^{-1/2}w_k,\quad
\Psi_\kappa(\eta)=\phi_\kappa^*(A^{1/2}\eta).
\]

由 (R1)，`w_k−w_{k+1}=λAu_{k+1}`；由 (R2) 的共轭梯度，`∇Ψκ(η)=A^{1/2}u`。因此**精确地**

\[
\eta_k-\eta_{k+1}=\lambda\nabla\Psi_\kappa(\eta_{k+1}),
\quad
\eta_{k+1}=\arg\min_\eta\{\Psi_\kappa(\eta)+(2\lambda)^{-1}\|\eta-\eta_k\|^2\}.
\tag{R5}
\]

`Ψκ` 有限、严格凸、强制，唯一极小点为 0。若 `κ≠0`，Taylor 展开得

\[
\Psi_\kappa(\eta)-\Psi_\kappa(0)
=\frac{\|\kappa\|^{p^*-q^*}}{q^*}\|A^{1/2}\eta\|^{q^*}
+o(\|\eta\|^{q^*}).
\tag{R6}
\]

于是局部增长条件的指数为 `ν=q*∈(1,2)`，并有正的统一局部增长常数。

Oikonomidis–Bodard–Laude–Patrinos, *Global Convergence Analysis of the Power Proximal Point and Augmented Lagrangian Method*, [arXiv:2312.12205v3](https://arxiv.org/html/2312.12205v3)，版本 2025-10-01，§3.3 Theorem 3.6，研究精确的距离幂近端算法；目标 proper lsc 凸、解集非空紧、解集附近有 `ν>1` 次增长，且其幂参数 `p_lit>ν−1` 时，距离上阶为 `p_lit/(ν−1)`。取该文 `p_lit=1`（普通欧氏 PPA）、`ν=q*`、目标 `Ψκ`，全部条件满足，所得上阶正是 `q−1`。

还须明确做物理坐标转换，而不能说“坐标变换自动保阶”。由 (R3)，存在正数 `c,C`，使充分小时

\[
c\|u\|^{q-1}\le\|\eta\|\le C\|u\|^{q-1}.
\]

将 `||η_{k+1}||≤M||η_k||^{q−1}` 代入上下界，再取 `1/(q−1)` 次幂，得 `||u_{k+1}||≤M'||u_k||^{q−1}`。又 `||z_k−z∞||=O(||u_k||^q)`，故完整物理误差也有相同上阶。

这比“另一种高阶近端也有类似指数”更强：**当前任意 SPD 二次耦合子类本身就精确变成了该已知算法的一个实例。** 同一原点层上 `Ψ0(η)=||A^{1/2}η||^{p*}/p*`；当当前参数 `p>2` 时，上述定理给 `p−1` 上阶。当前 `p=2` 时是二次目标欧氏 PPA，呈线性；`1<p<2` 不满足该超线性定理的参数条件，不应外推。

根任务另核查的 [arXiv:2505.20484v2](https://arxiv.org/html/2505.20484v2) Theorem 34(d) 也给距离幂近端在增长条件下的指数比。这说明指数平衡是一条成熟问题线；但它的算法与固定原点 Bregman 近端不同，不用它声称全体 C274 的直接覆盖。当前真正的直接覆盖来自 (R5)。

## 5. 剩下的定量内容有多少独立难度

### 5.1 有限长度有一个更一般的短径向引理

设一个可微严格凸径向核 `φ(u)=ρ(||u||)` 满足 `ρ'(0)=0`，并记 `n(r)=ρ'(r)`。假定 `n` 严格增加、`g` μ-强凸且 `0∈∂g(0)`。对于完整法向近端一步，在非零输出处向 `u+/||u+||` 取内积，得

\[
n(r)\ge n(r_+)+\lambda\mu r_+.
\tag{R7}
\]

零输出也满足式子。严格增加性给 `r+≤r`。逐步相加便得到

\[
\sum_{j\ge1}r_j\le\frac{n(r_0)}{\lambda\mu},\qquad
\sum_{k\ge0}\|u_{k+1}-u_k\|\le r_0+\frac{2n(r_0)}{\lambda\mu}.
\tag{R8}
\]

这里没有已知先行文献的优先权断言；这是本次给出的完整一般推导。C274 是此径向引理加上单调的切向重构，因此切向长度恰为 `t0−t∞`。这是真实可用的公式；但证明难度与机制更符合“简单定量推广”，不能只凭全局长度比一般点收敛强就推断重大新颖性。

### 5.2 锐阶与谱常数

对一般 `C^2` 强凸 `g`，`∇g(u)=Au+o(||u||)`。结合 (R3) 与近端方程，得到

\[
u_{k+1}=\frac{t_\infty^{p-q}}\lambda A^{-1}\|u_k\|^{q-2}u_k
+o(\|u_k\|^{q-1}).
\]

这一步比增长条件定理多给两侧锐阶和方向信息，但它是局部线性化与核首项的直接运算。二次目标的精确常数由对称正定矩阵的特征空间比值递推得到，径向核对正交变换不变，所以“任意 SPD 耦合”不会阻止谱分解。C274 的具体常数和物理尾长等价仍值得保存；当前最合适的称谓是可复用的模型级精确分析，而不是新的收敛范式。

## 6. 不能采用的弱比较

Azizian–Iutzeler–Malick–Mertikopoulos, *The Rate of Convergence of Bregman Proximal Methods: Local Geometry Versus Regularity Versus Sharpness*, SIAM J. Optim. 2024，DOI [10.1137/23M1580218](https://doi.org/10.1137/23M1580218)，[作者全文](https://polaris.imag.fr/panayotis.mertikopoulos/files/BregmanRates.pdf)，Definition 1、Assumptions 1–2、Theorems 1–2。该文采用强凸正则势、Lipschitz 算子、局部二阶条件，并研究显式镜像类方法，故确实不能直接覆盖当前退化核与完整非孤立解集。但这只能说明**该特定速率定理不适用**，不能对抗上面 BBC、部分对偶约化和欧氏 PPA 等更强比较。

同理，不能仅把 C274 同 separable scalar toy 比较，就视作对整个既有 Bregman 理论的实质拓展。当前非可分核的切向依赖可由部分对偶消元完整吸收；真正需要评价的是约化后的算法和定理，而不是原坐标公式看起来是否耦合。

## 7. C249 的地位及下一项有意义的研究义务

C249 的同一物理最近锚反射条件，并不是一般 Bregman firmly nonexpansive 的同义语。它在 `v` 的像中用欧氏范数作反射估计，而经典 Bregman 三点关系在原空间变量与梯度之间配对；不能无证明互换。因此，本审查不把 C249 宣布为 BBC 某一条定理的重命名。

另一方面，C249 的当前证明在已认证 G1–G5 后，核心是

`核步≤K(d) → 真残差≤K(d)/λ → 距离≤ψ(K(d)/λ)≤κd → 物理步≤H(d) → 长度预算与留域`。

最近锚、真残差 inf、全部允许输出、前缀留域等处理避免了真实的逻辑错误，属于好的定理工程。若要主张更强的概念新意，应展示至少一个自然的原始模型，使：① v 或 F 的结构确实超出凸 Bregman/已知预条件单调 PPA；② 完整输出可从原始数据验证；③ G2–G5 的认证不比直接求解动态本身更难；④ 得到旧理论没有的可定量效果。C274 对“验证链可以完整闭合”提供证据，但对这四项中的第一、第四项不提供排除经典理论的证据。

## 8. 未决事项与使用边界

1. 尚未找到也未排除一个早已发表、逐项包含全部 C274 显式系数和尾长公式的定理。检索未命中不证明其精确形式新颖。
2. Chen–Teboulle 1993、Eckstein 1993、Iusem–Teboulle 1995 及 Luque 的早期 nonlinear PPA 是历史链条中的重要线索；本轮对部分原文未能取得完整可读版本，因此不写未经全文核对的覆盖断言。已读文献中的引文只作为追索线索。
3. 此次强覆盖结论已不依赖拿到所有更早论文：BBC 的定性结论、精确约化 (R1)–(R6)、已核 Theorem 3.6 足以限制当前可支持的新颖性主张。
4. 结论不是“C274 没有数学价值”。其价值是完整可验证实例、明确的量化公式与反例边界。判断为“实质概念创新尚未证明”与判断命题真假不同，也与判断精确公式是否首次写出不同。

本次仅新增审查文件；未更改规范状态、正文、图资产或仓库历史。
