# 承重超边的量词与条件契约

## E84–E87：孤立零点的分支、正因子与输入覆盖

E84 在同一实 Hilbert 关系 F、局部孤立零点 p、\(q>1,\lambda>0\) 下使用 IZ-GERM 的逐图点剪切和 IZ-FIBERS 的真实 EB 到实际图值方向。此外对输入邻域每个 x 必须指定 \(Tx\in J_{\lambda F}(x)\)，全部实际输出属于同一 EB 输出球，\(\|(x-Tx)/\lambda\|<\eta\) 且 \(\rho\eta^{q-1}\le\lambda/2\)。闭输入球在该邻域中并使 \(C_q\delta^{q-1}<1\) 才有整轨道上阶。IZ-FIBERS 的反向需要全部小残差纤维 (IZ-1)，一条好分支不够；它不自动提供 T 的输入 coverage。[C45](canonical/isolated_zero_flatness.md#iz-ppa)。

E85 对同一非终止轨道另加 \(\|x^{k+1}-p\|/\|w_k\|^q\to\mu\in(0,\infty)\)，只在此门下得到正 Q 因子 \(\mu/\lambda^q\)。不能由 E84 的 upper bound 反推 \(\mu\) 存在。[C46](canonical/isolated_zero_flatness.md#iz-factor)。

E86 的全部输入使用一张完整紧图 \(\operatorname{gph}F=K\times\{0\}\)，\(S=K=\{0\}\cup\{1/n\}\)。在自然输入域 K 上全对 RL 与在实际输出上的真实 EB 同时成立；E87 用其限制 COV：这些前件并不蕴含零点的输入开球 coverage。E87 不是把 COV 结论判假，而是显示它在一般局部收敛定理中必须独立给出。若目标换为 \(\{0\}\)，EB 本身不再成立。[C47](topics/path_dynamics/discrete_coverage.md#dc-gap)、[F16](../FAILED_ROUTES.md#f16)。

## E88–E91：非孤立解集的锚点、近似点和锐性

E88 固定同一个 \(S\subset F^{-1}(0)\)、指定 \(J\) 和整个 \(0<d(x,S)\le r_0\) 的输入家族；对家族每个 x 同时要求 \(P_S(x),P_S(Jx)\ne\varnothing\)。集合间漂移的 infimum 不需取到，用近似点对即可得 \(r\le a\le r+\delta\le3a\)。E89 还需在**同一家族每个实际输出**的真 EB、非减超线性 gauge、全部实际步的 \(\psi(t)\le\lambda t/2\)、重标度在定义域内；包络版另需统一 \(\mathcal A(r)\le Kr^\theta\)。只得 upper \(\theta q\)，不含全轨道留域。[C48/C49](canonical/nonisolated_alignment.md)。

E90 不以 E88 的 proximinality 为前提：正的 \(e(t)\) 或另证近似投影非空，并对每个实际 \(t>0\) 有 \(\psi(t)+e(t)\le\kappa\lambda t,\kappa<1\)，才把同一真 EB 写成近似锚的 gauge 界。近似点的存在不提供 Minty 输入 coverage。[NA-APPROX](canonical/nonisolated_alignment.md#na-approx)。

E91 需要 E89 的共同上界环境和**同一**合法输入序列上三个正有限归一化极限；它不能用不同序列分别达到的 \(\theta,q\) 拼接。此时正因子为 \(CB^qA^q\)，而 \(\psi=o(t)\)、\(t_n\to0\) 强制 \(B=1/\lambda\)。若三重饱和没有证据，只保留 C49 的 upper bound。[C50](canonical/nonisolated_alignment.md#na-sharp)、[F17](../FAILED_ROUTES.md#f17)。

## E92–E94：移动输出锚只约束同一图点

E92 固定一个实际 \((y,w)\in\operatorname{gph}F\)、\(t=\|w\|>0\)、步长 \(\lambda\)，输出 y 有真 EB \(\psi(r_F(y))\) 且 \(\psi=o(t)\)；所选 \(p\in S\) 满足 \(\|y-p\|\le d(y,S)+e(t)\)，\(e=o(t)\)，若 \(e=0\) 需最近点存在。双边比与缺陷只关于这个随点变化的 p。E93 再用同一个 p 和幂型 \(d(y,S)\le\rho r_F(y)^q\)、\(e(t)=ct^q\)、\(q>1\)、\((\rho+c)t^{q-1}/\lambda\le1/2\) 给充分常数。二者均不需全对 RL，也不供输入 coverage。[C51/C52](canonical/moving_anchor_reflection.md)。

E94 的完整关系具有线性零集并在每个零点均含 0 及趋零的非零图值；取 y 固定、p=y 给移动锚零缺陷，但固定 \(p_0=0\) 的相对缺陷趋 2，反射前后到 S 距离相等。它限制把 E92 读成固定锚或集合距离收缩，不反驳 E92 自身。[MA-LIMIT](canonical/moving_anchor_reflection.md#ma-limit)、[F18](../FAILED_ROUTES.md#f18)。

本页按 [graph.json](graph.json) 的边 ID 解释合取输入。图只存摘要；调用一个 Claim 时必须读 [总账](../CLAIMS.md) 与对应证明。`∧` 表示**同一对象、同一参数及同一合法区域上的同时成立**，不允许用不同稿件各取一半前提。`source-report`、`candidate`、`derived-checked` 不能因画了箭头自动升为 `canonical`。

## E02→E03：局部 RLEB 的完整收敛链

固定 \(F:\mathbb R^n\rightrightarrows\mathbb R^n\)、图块 \(\mathcal G\subset\operatorname{gph}F\)、闭非空 \(S\subset F^{-1}(0)\)、开 \(U\)、\(\lambda>0\)、\(R>0\)、\(0<\gamma\le1\) 与 \(L\ge0\)。在 \(U_R=\{x\in U:d(x,S)\le R\}\) 上，对**每个**输入 \(x\) 同时要求图块输出 \(x^+\) 存在、可选最近零点 \(p\in P_S(x)\) 且 \((p,0)\in\mathcal G\)；全对 RL 对这个**同一图块内每对**图点、输入对尺度 \(R\) 成立。对**每个实际输出**要求 \(d(x^+,S)\le\psi(r_F(x^+))\) 与 gauge 取值范围。所得 R01 的 \(s=\|x-x^+\|\) 仅给 \(r_F(x^+)\le s/\lambda\)，不是等号。

R02 还要求 **每个** \(0<t\le R\) 的 \(\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t\)、\(0<\kappa<1\)，以及所选初值 \(x^0\) 的 \(d_0\le R\) 与严格长度预算 \(\mathcal L(d_0)<d(x^0,\mathbb R^n\setminus U)\)。结论是该图块的唯一局部轨道存在、留域、有限长、趋于 \(S\) 的一点。要改写成完整 \(J_{\lambda F}\) 的**每条**轨道，另需证明共同轨道区域每个完整纤维只含图块选择；[F03](../FAILED_ROUTES.md) 已反驳无条件升级。来源证明与常数见 [R01/R02](rleb_ppa.md)。

## E06、E11、E12：Dini 和纤维实现的条件限制

一般模版本在上一链把 \(Lt^\gamma\) 一致替换为非减连续 \(\omega(t)\)，额外要求 \(\int_0^R\omega(t)dt/t<\infty\)、同一 coverage、输出真 EB、兼容及严格留域。于是每个合法初值的步长可求和，且在由统一长度预算定义的开域 \(\mathcal O\) 上迭代极限 \(\Pi:\mathcal O\to S\cap U\) 连续并为回缩。这个拓扑结论依赖 **整套** 局部收敛假设。

另一命题 H03 的量词是：对每个有限维非空紧 \(K\) 且 \(\operatorname{diam}K\le L^{1/(1-\gamma)}\)，**存在某个**固定参数 graph-maximal RL 关系以 \(K\) 为完整零纤维。它没有断言该实现满足前段的局部 EB/Dini/coverage。对非局部可缩的 Cantor 型 \(K\)，所有这些局部前提不能在其非孤立点同时成立；这是一条合取限制，不是 H03 与 H05 的冲突。见 [H03–H05](holder_structure.md)。

## E17–E19：认证包含不是总体规模比较

在同一有限维完整原图 \(F\)、固定 \(\lambda\)、全域单值 \(T=J_{\lambda F}\)、同一 \(S\)、同一测试域、真实 \(r_F\)、coverage 和留域接口上，LT 公共 all-pairs 证书若满足 \(\operatorname{Lip}(2T-I)\le\sqrt{1+4\tau}\)、\(d(u,S)\le\rho r_F(u)\)、\(2\tau(\lambda+\rho)^2<\lambda^2\)，则该**匹配接口中的** RLEB 能量证书取 \(L^2=1+4\tau,\gamma=1,\psi(t)=\rho t\) 后 \(q_E=(1+2\tau)\rho^2/(\rho^2+\lambda^2)<1\)。这是证书类的包含，不保最佳常数，不包含 LT 的所有 pointwise/多值版本。[OS §2](operator_space.md)。

固定紧 T-only 图卡上的 proper \(\Phi=(w,m)\) 不推出它保 Baire category，也不恢复域外 \(F\)。因此 E19 的总体规模目标还缺参数中立的完整对象空间、计数单位 \(F\) 或 \((F,\lambda)\)、合法选择、三类共同域，以及不把三类一同判小的量尺。不能从 E17 或 proper 直接推出 E19。[OS §3–5](operator_space.md)。

## E13：有限观测与整窗拓扑是不同量词层

9/25 的有限样本 \((p_i,y_i)_{i=1}^m\) 只给到 \(d(\cdot,S)\) 的可验证上下包络。结论还需要**指定的整个** \(T\) 在 \(A\) 邻域 usc、各值非空紧且 Čech–\(\mathbb Q\)-acyclic、每个输出满足 proximal 与误差估计，另有 collar、上同调满射与 Euler 特征条件。\(T\) 可是完整 resolvent 的子关系；不能暗换成全纤维。外部 Lefschetz [6, Theorem 6.2] 的适用条件未独立关门，故 C05 仍是 PDF-only 候选。[H07](holder_structure.md)。

## E54–E58：随机近端中的三种残差

RP-OBJECT 固定有限维二次近端、正权重、共同核 \(U\)、非零活跃空间 \(V\) 和与当前状态独立的新噪声；RP-GAP 仅在 \(V\) 上给 \(c<1\)。对**每个固定**守恒边缘 \(\nu\in\mathscr P_2(U)\)、**所有** \(\mu\in\mathscr M_\nu\)，RP-CONTRACTION 给完整混合核的条件 \(\mathsf W_\nu\) 收缩。RP-EB 才使用 \(\mathcal R_\nu(\mu)=\mathsf W_\nu(\mu,\mu P)\) 推出 \((1-c)E_\nu\le\mathcal R_\nu\le(1+c)E_\nu\) 与有限长度。[完整证明](canonical/random_proximal.md)。

RP-BRANCH 的对象更宽：每支 firmly nonexpansive、有不动点且正权重，则 \(\sum_i p_iW_2(\mu,(S_i)_\#\mu)^2=0\) 等价于 \(\mu\) 支持于**所有**分支的共同固定点。RP-SCALAR 在一个不一致近端子族同时实现混合不变律、严格正物理步长及统一 EB 系数的尖锐性。分支残差、物理步长和完整核 law-step 各有不同零集或量纲；E57 是阻断替换的限制边，E58 只证明整个模型类的统一常数不能降低。[F09](../FAILED_ROUTES.md)。

## E59–E67：例子、参数及方向

E59–E61 的输入是**三个不同对象**，其历史 GX 号仅作观察别名：[EX01](canonical/example_atlas.md#ex01) 对每个 \(\omega,\lambda>0\) 的旋转完整 J 严格收缩但 \(F\) 无正强单调常数；[EX02](canonical/example_atlas.md#ex02) 是**无限维同一个**正紧对角 \(F\)，对任意趋零 \(\psi\) 都没有局部统一 EB，仍可对每个初值逐点收敛；[EX03](canonical/example_atlas.md#ex03) 的三个常数属于 \(F\) 固定目标、\(F\) 两变量和派生 \(G_\lambda\)，分别为 1、\(2^{2/3}\)、\(\lambda^{-1/3}\) 的局部下确界。不能因同属“正则性”就混同对象与量词。

E62–E64 固定同一图块 \(\Gamma\) 后，先区分全对/锚定及自然输入域与 coverage，再在同一步长用 Cayley 代数。E63 仅在 \(\gamma=1\)、相同配对范围上得到 tied \(\rho=\lambda^2\mu\)；\(L=0\) 是允许端点。E64 改**同一图的步长**时 \(Q=\alpha I+\beta C\)；新单值 iff \(Q\) 单射，Lipschitz 上界另需 \(\alpha-|\beta|L>0\)，新目标输入 coverage 不随之自动获得。[PD-STEP](canonical/parameter_dictionary.md#pd-step) 的 \(\eta>\lambda\) 折叠反例阻断无条件换步。

E65 的高指数→低指数只在同一**有界**输入域有统一常数。E66 的方向是“真残差 EB + 非减 gauge → 选中值界”；\(F(u)=\{u,u^2\}\) 阻断逆向。E67 的 MR 是移动目标、MSR 是固定目标；MR→MSR，但 MR 与 strong MSR 无条件互推都被显式反例否定。[PD 字典](canonical/parameter_dictionary.md)逐项证明，不把命名惯例当作推理。

任何新版本若改空间、残差、边缘、噪声条件或量词，应修改对应 Claim 版本及图边，保留旧反例；不要通过放宽 `scope` 文本暗中扩大原命题。

## E68–E71：路径图集的合取和两个不同的收敛结论

固定 X=ℝⁿ、闭非空 S、开 V、块长 m、r,η>0。E68 对**每个**块起点、每个合法前缀及每个允许的下一步同时要求可延拓、同一词的前缀距离/位移界；对所有合法词的终点上确界 Θ(t)≤κt，0≤κ<1；块长包络 G 给 H(t)=Σ_{q≥0}G(κ^q t)<∞。再对特定初值要求 H(d₀)<dist(x₀,X\V)，才可宣称**每条**实际轨道在 V 中有限长并收敛到 S。[C31](canonical/path_atlas.md#pa-whole) 的证明保持这些量词。E69 的块 RL 和实际输出 EB 只给终点 ρ；实际中间状态的延拓、位移预算和 ρ≤κt 仍须独立提供。

E70 的逐边幂次只证明**终点**上界。有限合法词的全体指数大于 1 给共同半径；若允许无限词，需 uniform inf A_w>1 与 sup C_w<∞。它绝不产生中间 G 的可求和性。E71 的相位连续性只在另已知块迭代趋于 Fix C 后给各相位极限；非平凡周期与 E68 的整轨道有限总长相斥。[F12](../FAILED_ROUTES.md#f12) 给逐词量词和周期的显式反例。

## E77–E78：M1 显式映射与原生多值桥的边界

两边只用同一个**单值** \(T(z_1,z_2)=(z_1-f(z_1-3z_2),0)\)，\(c=2/3\)、\(Z=[-c,c]\times\{0\}\)、\(R=1/(96\sqrt {10})\)。E77 对球内**每个**初值给 \(T^2z\in Z\)，并用 \(T|_Z=I\) 得有限捕获；E78 对同一球的**每个**初值给 \(d(Tz,Z)\le(3/\sqrt {10})d(z,Z)\)，而 \(z_t=(c+3t,t)\) 给锐性。二者从对象出发是不同结论，不能从“两步捕获”本身推出“一步收缩”。[C38/C39 的完整计算](topics/path_dynamics/m1_capture.md) 不包含历史原生 `Sign` 广义方程的全部输出关系；“真多值”身份、完整图 EB 和全对 RL 的箭头尚未建立。[F14](../FAILED_ROUTES.md#f14) 说明为何最坏标量证书失效不能替代此箭头。

## E72–E76：复合次正则的目标、秩与近端预算

E72 先把目标固定为 S⊆Γ 且包含所有局部极小点，配合 f 在 B_α(x̄) 局部最小与 Γ∩B_ς 的弱分离，才在 B_{R/4} 得三个**同一目标**的距离等式。不能因 S⊆Γ 就随意缩 S。E73 是另一个有自己目标 S=c^{-1}(C) 的命题；在同一 B̄_R 上需要 c∈C^{1,1}、βR<σ_min(Dc(x̄))、φ 有限凸、外层真残差 gauge。满秩同时用于切片修复与 Dcᵀ 的全部乘子下界，才给 r_F 的复合 gauge。[CS-EB](canonical/composite_subregularity.md#cs-eb)。

E74 再加所有相关外层次梯度的 M 界及 λβM<1，只先得局部全对线性 RL 和局部输出 coverage。收敛版本还要 Ψ_F(bd)≤κd 对共同半径内每个 d、最近零点属于同一图块及初值的严格长度预算；不能将其改成完整 resolvent 的所有球外纤维。E75 的曲面是 E73 的特殊对象；其非幂模型反驳“所有满秩复合都具有某个固定 q>1 幂 EB”的过强命题，而不否定一般 gauge 定理。E76 的 c=x²、φ=z²/2 仅否定删除满秩后的**同阶线性传递**，并未排除较弱非线性 gauge。[F13](../FAILED_ROUTES.md#f13)。

## E79–E80：真多值图与目标错误的分离

E79 对 [CI-OBJECT](topics/composite_regular/cusp_identification.md#ci-object) 增加 **CS-PROX 的局部版本**：同一曲面 \(c=t-(s_+)^2\)、\(\nu>0\)、\(\eta\) 连续严格增无界、\(0<R<1/2\)，\(M=\nu+\eta(R+R^2)\)、\(h=2M\)、\(\lambda h<1\)。还需输入 \(x\in B_{r/2}(0)\) 且 \(d(x,S)<\lambda\nu(1-\lambda h)\)，\(r=R(1-2R)/4\)。此时图在 S 上多值、S 外真残差至少 \(\nu\)，但唯一**球内**近端步的选中残差小于 \(\nu\)，所以一步到 S；并未认证完整 \(J_{\lambda F}\) 的远端纤维。[C40](topics/composite_regular/cusp_identification.md#ci-identify)。

E80 是独立反例关系：[OT-MAXIMA](topics/composite_regular/oscillating_target.md#ot-maxima) 的驻点严格极大序列有 \(|f'|=0\)、\(d(x,\Theta_2)>0\)。它只否定删除目标一致条件后对完整 \(\Theta_2\) 的全邻域 EB；函数虽在零点严格局部最小，弱分离被 \(f(x_k)>f(0)\) 破坏。不能将箭头倒读为 C34 错误，也不能悄然将目标换成 \(\Gamma\)。[F15](../FAILED_ROUTES.md#f15)。

## E81：幂次剪切的可达性而非普遍速率

固定 \(\lambda=1\)、\(0<\gamma<1\)、\(q>1/\gamma\)、\(\alpha=\gamma q\)，由 [PS-OBJECT](topics/path_dynamics/power_shear.md#ps-object) 的**完整**三角图可反演 F，并对所有点给真残差 \(q\)-EB。对实际轨道的法向距离恰为 \(r_+=r^\alpha\)。反射全对 \(\gamma\) 的范围限于**有界输入矩形**，单条轨道留在该矩形还要切向余量覆盖整个漂移和；它不表示无界全图 RL，更不能推出所有满足同指数证书的轨道都按 \(\gamma q\) 精确收敛。[C42](topics/path_dynamics/power_shear.md#ps-rate) 只是反向校准例的可达见证。

## E82：同指数输入而实际阶更高

[OS-OBJECT](topics/path_dynamics/oscillatory_shear.md#os-object) 是**另一**完整三角图：\(q>1,0<\gamma<1,\beta=q/\gamma-1\)，\(h(x)=|x|^q\sin(|x|^{-\beta})\)。其全域 \(J\) 双边 \(q\)-缩放和邻域真残差 \(q\)-EB 与有界窗最大全对反射指数 \(\gamma\) 同时成立；每条充分小非零轨道有双边 \(q\)-阶，而 \(q>\gamma q\)。这里的零集仅在原点附近为单点，远端仍有固定点；归一化 Q 因子的极限未证。[C43](topics/path_dynamics/oscillatory_shear.md#os-scaling) 限定了与 E81 比较的对象差异。

## E83：自然域与全纤维残差

[DE-OBJECT](topics/path_dynamics/domain_escape.md#de-object) 只在 \(D=[-\delta,\delta]\) 定义原图，\(0<\alpha<1,\beta>0,0<\delta<1\)。在同一图上锚定反射指数 \(\alpha\)、全对指数 \(\alpha/(\beta+1)\)，但所有非零合法轨道半径严格增，有限步离开 D。[C44](topics/path_dynamics/domain_escape.md#de-escape) 的局部线性 EB 用的是每个原像上的一致残差比再对完整纤维取最小，不是挑一个好分支。输入域 coverage 和不变性不能从一步指数或 EB 自动得到；域外没有原算法轨道。

## E95–E97：指定分支与全对图条件的分界

E95 在实 Hilbert 空间固定完整 \(F\)、\(S=F^{-1}(0)\ne\varnothing\)、球 \(U\)、同一个 \(T:U\to H\) 和 \(\lambda>0\)。B 对整个 \(U\) 提供实际图点；A 对整个 \(A_\delta\)，**包括 \(d(x,S)=0\)**，提供每个输入自己的近似最近零点序列和相同 \(L,\gamma\) 的锚定不等式；E 对每个实际输出给真残差窗口 EB。先要 \(h(\delta)<\eta\)，再要 \(\limsup_{t\downarrow0}\Phi(t)/t<1\) 和**给定初值**的严格留域预算，才能推出指定轨道有限长度。零距离点用 A、B 证 \(U\cap\overline S=U\cap S\)；不需要在整个 Hilbert 空间假设闭 \(S\) 或最近点取到。A 不比较两个非零输入，且没有排除完整 resolvent 其他输出。

E96 在**同一** B/A/E、同一输出窗口上把 \(\psi(t)\) 换为 \(\rho t^q\)。\(0<\gamma<1,L>0\) 的主指数是 \(\gamma q\)，\(\gamma=1\) 的主指数是 \(q\)，\(L=0\) 的主指数也是 \(q\) 而不论所打印的 \(\gamma\)；临界系数见 [C54](canonical/named_branch_local.md#nb-power)。这些是上界给出的充分门，正 Q 因子和下阶另需沿同一轨道的额外极限。

E97 是反驳边而非把 C53 推向 D02：[C55](canonical/named_branch_local.md#nb-oscillation) 同时有完整图、指定锚定线性 RL、真 EB 与局部收缩，但 Cayley 在每个零邻域非 Lipschitz。故 R02 的全对输入不可由 C53 回填；较弱的全对 Hölder 指数仍未由此例排除。[F19](../FAILED_ROUTES.md#f19) 保存失败机制。

## E98–E100：全对图块进入指定分支所需的零锚距离门

E98 的 AV-OBJECT 在同一 \(G\subset\operatorname{gph}F\) 上对所有图点对给全对 RL，并在指定 \(U\) 给自然输入 coverage；对 active set \(A\) 的**每个** \(x\) 另需 \(d(x,S_G)=d(x,S)<\infty\)，\(S_G=\{p\in S:(p,0)\in G\}\)。只有这项保距离，才能在 \(G\) 内取近似零锚并使用成对不等式。C56 只产出 C53 的 B/A 和图块反射的双输入模，不产出 E。

E99 需将 \(U\) 取成开球、\(A=A_\delta\) 且覆盖 \(d=0\) 输入；另对同一实际 \(Tx\) 证窗口化真残差 EB、标量兼容以及所给初值的严格长度预算，才调用 C53 的有限长度结论。D04 是残差定义入口，不能代替具体输出 EB 的证明。图块内单值也不能自动变成完整 \(J_{\lambda F}\) 的所有选择。

E100 的 [C57](canonical/all_pairs_verifier.md#av-gap) 同时有 \(L=0\) 全对、全输入 coverage 和真实输出 EB，却有 \(S_G=\{0\}\ne S=\mathbb R\)，因此零距离输入不固定。完整 resolvent 的另一分支说明排他性也是独立门；[F20](../FAILED_ROUTES.md#f20) 保存两个缺口的区别。
