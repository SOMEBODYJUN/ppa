# 承重超边的量词与条件契约

## E42–E43：两种条件刷新不能共用残差节点

E42 固定同一标准 Borel 守恒变量的边缘 \(\nu\)、有限 bit 纤维、正的坐标刷新概率及余概率恒等更新。\(\mathsf W_\nu\) 只在同一 \(u\) 内作 Hamming 成本运输，\(\mathcal R\) 是保留 \((u,x_{-i})\) 的条件 Bernoulli 残差。只有对**全部固定边缘律**及同一目标 \(\pi_\nu\)，\(a_*={\rm ess\,inf}_u\min_i p_i(u)>0\) 才与统一线性 EB／到目标的严格率等价；最佳系数与每步因子见 [C129](topics/random_markov/conditional_refresh.md#cr-binary-theorem)。等价不指任意两律间的 Lipschitz 性。

E43 另取 \(\mathbb R^m\) 上 \(Q\succ0\) 的 Gaussian 目标 \(\beta\) 和常数正概率 \(p_i\)，\(W_{2,Q}\) 的成本是 \(Q\) 二次型，\(\mathcal R_Q\) 在**一维条件律**中用普通 \(W_2\)。\(\zeta=\lambda_{\min}(Q^{1/2}\operatorname{diag}(p_i/Q_{ii})Q^{1/2})>0\) 给所有有限二阶矩律的锐 EB \(\zeta^{-1/2}\) 和仅称有效的到目标收缩因子 \(\sqrt{1-\zeta}\)；见 [C130](topics/random_markov/conditional_refresh.md#cr-gaussian-theorem)。它没有 \(\nu\)、二进制 \(\mathsf W_\nu/\mathcal R\) 或原同步 \(\Psi\)。旧 E43 将 `M-COND` 与 Gaussian 合取属于**对象类型错接**，现用 `G-COND` 独立节点。

## E44–E45：概率矩门与同一回耦对

E44 的 \(e,c\) 是同一状态集上的非负有限函数；存在共同零点及两者都正的 excursion，\(1\le p,r<\infty,q>0\)。[C126/MR1](topics/random_markov/moment_recoupling.md#mr-moment) 的等价式量化**全部有限支撑律**，且点态系数必须是同一 \(K\)。law-space 必要性另需闭支持目标、平稳律在该目标上、状态残差在该律上零，以及非零更新输出离目标；它不把 \(\Psi\) 或条件残差 \(\mathcal R\) 直接等同于标量 \(c\)。

E45 的输出是 [C127/MR3](topics/random_markov/moment_recoupling.md#mr-recoupling) 的**线性 EB**，不是 CM-GAUGE 的 exact-zero ⇔ 一般 gauge。必须同时在同一随机表示及指定律类上有 \(d(\mu P)\le c_0d(\mu)\)、\(c_0<1\)，并对每个 \(\mu\) 用输入 \(W_2\)-最优、同噪声的近极小序列 \((\pi_j,\eta_j)\) 逼近原 \(\Psi\) 下确界；同一个 \(\chi\) 控制这些对的 \(\Delta_{\eta_j}\le\chi D_{\eta_j}^2\)。不能从别的运输对、不同表示或条件刷新残差移植损失界；原生模型尚须单独认证这些量词。

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

在同一有限维完整原图 \(F\)、固定 \(\lambda>0,\tau\ge0,\rho>0\)、全域单值 \(T=J_{\lambda F}\)、同一 \(S\)、同一测试域、真实 \(r_F\)、coverage 和留域接口上，LT 公共 all-pairs 证书若满足 \(\operatorname{Lip}(2T-I)\le\sqrt{1+4\tau}\)、\(d(u,S)\le\rho r_F(u)\)、\(2\tau(\lambda+\rho)^2<\lambda^2\)，则该**匹配接口中的** RLEB 能量证书取 \(L^2=1+4\tau,\gamma=1,\psi(t)=\rho t\) 后 \(q_E=(1+2\tau)\rho^2/(\rho^2+\lambda^2)<1\)。这里 \(\rho>0\) 保证 \(\alpha(t)=t/\rho\) 可用；这是证书类的包含，不保最佳常数，不包含 signed LT 或所有 pointwise/多值版本。[OS §2](operator_space.md)。

E18 的输入只是一张固定非空紧 \(K\)、非空闭 \(S\subset K\)、全时间度量下的单值 T-only 图卡；[\(\Phi=(w,m)\) proper 的完整证明](canonical/compact_t_observation.md#ct-proper) 还要求尾列比较**所有**两迭代，\(c_0^2\) 的紧参数集提供共同零尾。此 properness 不推出保 Baire category，也不恢复域外 \(F\)。因此 E19 的总体规模目标还缺参数中立的完整对象空间、计数单位 \(F\) 或 \((F,\lambda)\)、合法选择、三类共同域，以及不把三类一同判小的量尺。不能从 E17 或 proper 直接推出 E19。[OS §3–5](operator_space.md)。

## E13：有限观测与整窗拓扑是不同量词层

9/25 的有限样本 \((p_i,y_i)_{i=1}^m\) 只给到 \(d(\cdot,S)\) 的[可验证上下包络 C70-v1a](canonical/finite_sample_collar.md#fsc-envelope)。另有**指定的整个** \(T\) 对每个 \(p\in A,y\in T(p)\) 的步界/输出 EB，加上经验证的 collar 数值，才给 [C70-v1b 内域余量](canonical/finite_sample_collar.md#fsc-collar)；这个结果没有 fixed point 结论。C05-v1 还需要 \(T\) 在 \(A\) 邻域 usc、各值非空紧且 Čech–\(\mathbb Q\)-acyclic，以及上同调满射与 Euler 特征条件。\(T\) 可是完整 resolvent 的子关系；不能暗换成全纤维。外部 Lefschetz [6, Theorem 6.2] 的适用条件已在[一手文献卡](LITERATURE.md#lit-grn-2002)按紧图/Vietoris/CAC 逐项核对；它不建立任何整窗模型假设，原稿 C05-v1 仍是 PDF-only 候选。[H07](holder_structure.md#h07)。保留全部这些合取前提而将 \(q\gamma>1\) 放宽成 \(q>0\) 的独立新版本见 [C05-v2](canonical/local_range_without_supercriticality.md#lr-theorem)。

固定惰性四循环的 [C71](topics/random_markov/lazy_cycle_ot.md#lc-sharp) 使用唯一不变律 \(\pi\) 与输入 \(\mu\) 之间的 **\(C\)-最优计划**，并在这些计划上才最小化同步残差成本 \(R\)。位移签名 \(d_0=d_3\) 本身不能识别 \(\mu=\pi\)，但最优运输的无交叉交换排除零成本跨边；去掉内层 OT 约束的 [LC-RELAX](topics/random_markov/lazy_cycle_ot.md#lc-relax) 则有非不变输入残差零。核 \(P_p\)、边缘、成本和最优计划域都须保持相同，才能调用锐 \(\sqrt{13/p}\) 界。

<a id="e51"></a>
## E50–E51：有限数据的同图尺度门与反演求值门

E50/C20-v2 的样本与待认证未知点必须在**同一** RL 认证图中，且每个用于 Hölder 比较的 Cayley 参数点对落在证书的**成对尺度**内：全图全尺度自动满足；局部 \(R_0\) 版以 \(\delta\le R_0\) 为充分门，或逐对另核 \(\|p-p_i\|\le R_0\)。若结论关于完整 \(F^{-1}(v)\)，其中的每个图点都须属于该认证图并逐个满足点对条件。仅有 \(\delta\)-覆盖而把 RL 用在尺度外的旧 C20-v1 已被 [F36](../FAILED_ROUTES.md#f36) 的两点完整图反驳；S23 的全尺度原稿不受影响。

E51 的真实输出 \(v\) 必须有**整个非空逆纤维**的 Cayley 参数 \(\delta\)-覆盖，并有 \(\|\widetilde v-v\|\le\eta\)。三项总界里的 \(e_x\) 是已认证的 \(\|\widehat x-A_m^{-1}(\widetilde v)\|\) 上界；可行 QP 的 Frank–Wolfe gap \(G\) 只给同一候选参数 \(q\) 处 \(e_N=\sqrt G\) 的 \(N_m(q)\) 输出误差。若 \(\widehat x=q-\lambda\widetilde v\) 且打算**从该次 QP 求值**生成证书，可取充分上界 \(e_x=(\|q-2\lambda\widetilde v-\widehat N(q)\|+e_N)/(1-\sigma)\)；也可对 \(e_x\) 作其它独立认证。只给 gap、没有候选点的固定点残差或另一独立反演认证，就不能调用 [Q03](range_finite_data.md#q-eval) 的三项界；这两种 \(e\) 在原稿 prop:evaluation 与 cor:totalerror 中是不同类型。

## E105–E112：三组新对象的互不替代条件

E105/E106 的共同名称 Douglas–Rachford 只固定公式 \(T=I-P_C+P_DR_C\)、算法残差 \(G=I-T\)：**切触**的 \(D\) 是抛物线，只在 \(b>-1/2\) 统一投影并于零附近有半阶 MSR；**横截**的 \(D\) 是直线，对所有输入有可逆线性 \(G\) 和精确模 \(1/\sin\theta\)。二者不是同一算子的参数版本。E107 的取等输入 \((s,-s^2)\) 只反驳“半阶 EB 自动给统一一步严格距离收缩”；并未否定全投影管不变或判定每条局部轨道。[对象卡](topics/examples/dr_tangency_transversality.md)。

E108 的全称量词是：**每个**支撑于同一 \(f\) 的 \(\operatorname{dom}f\) 的平稳概率律，在核只选全局近端最小解时必吸收。E109 的新二维模型另有 fair tie 核；对**每个**完整 \(W_2\) 零点邻域可选固定 \(\epsilon>0\) 并有一列律，真实 law-step 趋零、到**唯一**不变律的距离不趋零。完整多值近端图闭不替所选核的 Feller 性，且 C22/C23 的随机二次目标与同步 OT \(\Psi\) 都是别的残差。[固定目标正文](topics/random_markov/proximal_selection_seam.md)。

E110/E111 从**新定义** \(F_{\rm lift}\) 的全部图值分别推出完整单位步长 \(J_F=T\) 和端点真实残差 \(\delta/3\)；后一个结论要重新取完整纤维 infimum，不从动力率推出。E112 只有在这个新关系与已核显式 \(T\) 逐输入同一时，才把 C38/C39 的两项动力结论应用到它。历史“原生循环 Sign 方程”没有给可识别的完整图与允许相位，所以没有从 E110 到该历史方程的边。[Sign 新构造](topics/path_dynamics/m1_sign_lift.md)。

## E113–E114：Hilbert 雪花、引文与固定参数图极大

E113 对任意非空子集 \(D\subset H\) 及**全部配对**的相同 \(L,0<\gamma<1\) 建立 \(C:D\to Y\)。[HE-SNOWFLAKE](canonical/holder_extension.md#he-snowflake) 的 Gaussian 正定性给 \(\|Jx-Jy\|=\|x-y\|^\gamma\)，[LIT-ALM-2021](LITERATURE.md#lit-alm-2021) 的正式 Theorem 1.2 只导入**Hilbert 间**同常数 Lipschitz 扩张；二者合取才给同参数 Hölder 扩张。E114 再把它施于 **完整** RL 图的 Cayley \(C\)，固定 \(\lambda,L,\gamma\)，使用剪切反演和同输入唯一性才得到 `graph-maximal ⇔ Minty 域 H`。图块局部模、预定像集或极大单调性不在结论内；该边只支撑 H01 这一子命题，不审 C03 全篇影子证明。

## E184–E187：signed-Schur 的闭域、全纤维与应用门

E184 在固定有限维、同一 \(\lambda\) 与闭参数块 \(Q\) 上合取公共接缝、强单调切向导数、Schur 控制、两侧相反凸严格增长以及 \(0<r<\mu R-HT\)。参数化只需在邻域有 \(C^1\) **延拓**，图包含仅在 \(Q\) 上要求。输出是切向输入在 \(B_r\) 的所表示图的覆盖、无碰撞与全对零消失模，不能延及球外。[SS-GROWTH-v2](canonical/signed_schur_growth.md#ss-growth)。

E185 另以 (SS-13) 核 \(U\) 上**全部**活动图点纤维，才赋予局部 \(J_{\mathcal G}\)；赋予完整 \(J_{\lambda F}\) 须 \(\mathcal G=\operatorname{gph}F\)。真实残差 EB、目标零锚、兼容与留域仍独立，故不把 E185 画成直接的 PPA 收敛箭头。旧 E05 现显式合取 SG-POWER 的同参数幂次/尺度预算、COV 的最近零点图锚、实际输出真 EB、\(\kappa<1\) 与留域，才可调用 R02；一般 signed-Schur 几何本身不直接推出收敛。E186 另固定完整平方根图、幂次预算、同修正输入输出匹配和全纤维检验，区分有效常数与收缩领圈的渐近锐常数 2；同图的真残差独立取全部图值最小范数。E187 的碰撞、删凸性及添远支分别测试不同门，所表示图性质不能替完整纤维排他。[C117–C119](canonical/signed_schur_growth.md#ss-obligations)。原 S19-SG-v1 的邻域图包含读法比 v2 强，平方根例的负参数延拓不满足强读法。

## E180–E183：解选择的共同尾、完整纤维与同一初始 collar

E180 固定一个单值 \(T\) 与全部指定初值的共同工作域，**局部** Hölder 单步仅在输入对距离 \(\le R\) 使用；共同几何或超几何点尾的常数对全部初值和全部步数一致。有限前缀逐步验证局部尺度后，才可平衡尾界得到相应对数–对数或指数根对数选择模。若 \(T\) 起于图块 \(J_{\mathcal G}\)，完整 \(J_{\lambda F}\) 的同一轨道区域全纤维一致性是另一个门，不能由共同尾替代。[SS-TRANSFER](canonical/solution_selection_rates.md#ss-transfer)。

E183 对 **SS-Q1 同一个完整二值关系** 从两支及负输入全部反演；固定 \(0<R_0<1\)、有限比较尺度 \(D\)，图块内 all-pairs RL、真实最小残差、零锚、预先固定的 \(R\le R_0/2\)、严格兼容和不变 collar 要逐项同时成立，才赋予 C115 的共同尾。E181 还加入在 **固定 \(0<r_0\le R\)** 上的切换时刻上下界，获得 C116 的根对数双边模；每轨道 Q 二次比值与共同超几何尾是不同量词。E182 使用同一选择下界与代数图的多项式恒等式，排除该极限选择的局部半代数性；有限步半代数并不足以推出极限同性质。SS1 定理 2/3、§5.2 和外部新颖性不在这些边内。[完整证明](canonical/solution_selection_rates.md#ss-quadratic-object)。

## E115–E118：并图三残差与新 Sign 图局部指数

E115–E117 **同一完整** \(F(x)=\{x,x^2\}\)，但残差的下确界不同：E115 的全局公式是 \(r_F(x)=d(0,F(x))=\min\{|x|,x^2\}\)，在 \(|x|\le1\) 的零点局部窗才简化为 \(x^2\)；E116 是 \(r_J(p)=\inf_{u\in J_{\lambda F}(p)}|p-u|\)，必须保留平方分支的近平根与远根；身份指定分支 \(J_1(p)=p/(1+\lambda)\) 的线性界不能替代完整 \(r_J\)。E117 以同输入的**两**图点阻断所有正 Hölder 全对指数；这与 E115 的半阶真 EB 不构成蕴含。历史 GX-068 的两变量 MR 现由 E157/C92 单列，二参数全对区域另由 E160/C95 核定。[IS 卡](topics/examples/identity_square_branch_union.md)。

## E157–E159：完整逆像、真空误差界与反射的不同量词

E157 保持 E115 的**同一完整并图**，但目标也在 \((-\delta,\delta)\) 全称变化；\(0<\delta\le1/3\) 上每对 \((x,y)\) 的完整逆像距离被**完整输出残差**平方根控制，系数 1 的最大对称开窗口为 \(1/3\)。它比 E115 固定 \(y=0\) 的结论量词更广；最近逆点的线性律与指定近端线性步界不能代替其所有逆分支。逆 Hölder–Aubin 仅对落在局部输入窗内的逆像点全称；同对象完整 RL 仍被 E117 碰撞否定。[IS-MR](topics/examples/identity_square_branch_union.md#is-mr)。

E158 固定 \(m\ge1\) 的完整闭球法锥及任意步长，以全部图点对得到二参数区域 \(\mu,\rho\le0\) 与全域锐线性反射模 1；不能因单调把正强单调或正 cocoercive 参数画进来。E159 在**同一完整关系**上把固定零目标 \(S=B\) 的真空 MSR 系数下确界 0 与所有参考零点的扰动目标 MR/HREG 失败分开；全邻域 \(\kappa=0\) 的写法不预设 \(0\cdot\infty\)。[BN 卡](topics/examples/ball_normal_cone.md#bn-object) 与 [F29](../FAILED_ROUTES.md#f29) 给域外语义和边界反向目标见证。

## E160：并图二参数签名不满足正 Cayley 球门

E160 同时固定 [C95 的完整并图](topics/examples/identity_square_branch_union.md#is-semimono) 与 [C89 的二参数定义](canonical/non_tied_cayley.md#nt-object)，不从一个结果“推出”另一个定理。跨支图点对在每个原点图窗实现全部实斜率，因而 \(\Sigma(F)\) **恰**为 \(\mu<0,\rho<0,\mu\rho\ge1/4\)。对每个 \(\lambda>0\)，同图有效参数有 \(A\le0,\Delta\le0\)，故 C89/C91 的 \(A>0,\Delta\ge0\) 联合充分门不可用于此图；这并不反驳 C89 在其自身门内的命题。等号边界与 C68 的同输入跨支碰撞由正文独立核算。

E118 对另一个**新定义**的 \(F_{\rm lift}\) 使用 C64 的全域完整 \(J_F=T\)；固定 \(\lambda=1\)、端点 Minty 输入球 \(U=B_\rho((2/3,0))\)、\(0<\rho<\min\{1/2,(2/3)/(2\sqrt{10})\}\)。球内任意两完整图点的反射差有 \(1/3\) Hölder 界，端点正向输入序列排除更高指数；任何无界全域版本和历史循环 Sign 方程都没有这条边。[SL-RL](topics/path_dynamics/m1_sign_lift.md#sl-rl)。

## E119–E122：所有概率律的包络与原生可实现耦合

E119 固定 \(p,R,\varphi\) 的连续非减硬支持对象，取**所有**概率空间、全部 \(0\le D\le R\) 且 \(\|D\|_p\le t\) 的最坏情形；上确界等于最小凹上包络并存在至多两点幅度的取等律。E120 对幂函数的凹/凸包络给两个锐分支；若还要将 \(S\le CD^\gamma,D_+\le KS^q\) 用于真实更新，必须先在**同一**合法耦合上同时证两条逐点界与真实支撑。E121 以 `limits` 关系记录 F24 的**正确障碍**：临界 \(\gamma q=1\) 下两次各自取等的标量包络不是同耦合锐界；它并非反驳该障碍。E122 的稀薄双点律证明只知道小 \(L^p\) 并不能替代 \(D\le r\) 的逐点门。以上没有核具体 Markov 核的目标边缘或其可实现选择。[SME 正文](topics/random_markov/scalar_moment_envelope.md)。

## E54–E58：随机近端中的三种残差

RP-OBJECT 固定有限维二次近端、正权重、共同核 \(U\)、非零活跃空间 \(V\) 和与当前状态独立的新噪声；RP-GAP 仅在 \(V\) 上给 \(c<1\)。对**每个固定**守恒边缘 \(\nu\in\mathscr P_2(U)\)、**所有** \(\mu\in\mathscr M_\nu\)，RP-CONTRACTION 给完整混合核的条件 \(\mathsf W_\nu\) 收缩。RP-EB 才使用 \(\mathcal R_\nu(\mu)=\mathsf W_\nu(\mu,\mu P)\) 推出 \((1-c)E_\nu\le\mathcal R_\nu\le(1+c)E_\nu\) 与有限长度。[完整证明](canonical/random_proximal.md)。

RP-BRANCH 的对象更宽：每支 firmly nonexpansive、有不动点且正权重，则 \(\sum_i p_iW_2(\mu,(S_i)_\#\mu)^2=0\) 等价于 \(\mu\) 支持于**所有**分支的共同固定点。RP-SCALAR 在一个不一致近端子族同时实现混合不变律、严格正物理步长及统一 EB 系数的尖锐性。分支残差、物理步长和完整核 law-step 各有不同零集或量纲；E57 是阻断替换的限制边，E58 只证明整个模型类的统一常数不能降低。[F09](../FAILED_ROUTES.md)。

## E59–E67：例子、参数及方向

E59–E61 的输入是**三个不同对象**，其历史 GX 号仅作观察别名：[EX01](canonical/example_atlas.md#ex01) 对每个 \(\omega,\lambda>0\) 的旋转完整 J 严格收缩但 \(F\) 无正强单调常数；[EX02](canonical/example_atlas.md#ex02) 是**无限维同一个**正紧对角 \(F\)，对任意趋零 \(\psi\) 都没有局部统一 EB，仍可对每个初值逐点收敛；[EX03](canonical/example_atlas.md#ex03) 的三个常数属于 \(F\) 固定目标、\(F\) 两变量和派生 \(G_\lambda\)，分别为 1、\(2^{2/3}\)、\(\lambda^{-1/3}\) 的局部下确界。不能因同属“正则性”就混同对象与量词。

E62–E64 固定同一图块 \(\Gamma\) 后，先区分全对/锚定及自然输入域与 coverage，再在同一步长用 Cayley 代数。E63 仅在 \(\gamma=1\)、相同配对范围上得到 tied \(\rho=\lambda^2\mu\)；\(L=0\) 是允许端点。E64 改**同一图的步长**时 \(Q=\alpha I+\beta C\)；新单值 iff \(Q\) 单射，Lipschitz 上界另需 \(\alpha-|\beta|L>0\)，新目标输入 coverage 不随之自动获得。[PD-STEP](canonical/parameter_dictionary.md#pd-step) 的 \(\eta>\lambda\) 折叠反例阻断无条件换步。

E65 的高指数→低指数只在同一**有界**输入域有统一常数。E66 以 `limits` 指向正确障碍“选中步残差不能倒推真 EB”：正方向是“真残差 EB + 非减 gauge + 选中范数**在该 gauge 定义域内** → 选中值界”；\(F(u)=\{u,u^2\}\) 阻断逆向，而非反驳障碍本身。例如 \(F(u)=\{u,2\}\)、\(\psi:[0,1]\to[0,\infty),\psi(t)=t\) 时，\(u=1/2,v=2\) 的真残差表达式可评价，\(\psi(\|v\|)\) 未定义。E67 的 MR 是移动目标、MSR 是固定目标；MR→MSR，但 MR 与 strong MSR 无条件互推都被显式反例否定。[PD 字典](canonical/parameter_dictionary.md)逐项证明，不把命名惯例当作推理。

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

## E101–E102：闭图、闭自然域、稠密性是三个不同层次

E101 固定**同一非空图块** \(G\subset H\times H\)、同一步长 \(\lambda>0\) 与完备实 Hilbert \(H\)。对所有 Minty 输入差小于一个共同 \(R>0\) 的**两图点**，要求 \(\|\Delta M_-\|\le\omega(\|\Delta M_+\|)\)、\(\omega(0)=0\) 及 \(\omega(t)\to0\)；既不要求输入球 coverage，也不要求 EB。Cayley pullback 在 \(\overline D\) 有唯一连续延拓，得到 \(G\) 闭 iff \(D=M_+(G)\) 闭。若用一般有正尺度跳跃的模，闭包保持模的精确常数另需核；本边只断言闭包表示与闭性。[C58](canonical/closed_graph_minty_domain.md#cg-closure)。

E102 **另加**同一 \(G\) 的闭图和 \(D\) 在整个 \(H\) 稠密，才由闭 \(D\) 推出 \(D=H\)。取 \(G=[0,1]\times\{0\}\subset\mathbb R^2\) 可同时满足闭图与全对线性 RL，但没有零点邻域输入球，所以不能删除稠密性。即使图块已满输入，完整 \(F\) 在图块外的纤维仍需另证排他；这一边不提供 PPA 的真实残差 EB、兼容或留域。[F16](../FAILED_ROUTES.md#f16) 是更强的无 coverage 见证。

## E103–E104：残差阈值以上的 gauge 值

E103 固定**完整** \(F\)、\(S=F^{-1}(0)\ni\bar u\) 与对完整 \(F(u)\) 取 infimum 的 \(r_F(u)\)。窗口版在同一个 \(U\) 只要求 \(r_F(u)<\delta\)，其中 \(0<\delta<\eta\) 且 \(\psi:[0,\eta)\to[0,\infty)\) 有限非减。再加 \(\psi(\delta)>0\)，才可用 \(d(u,S)\le\|u-\bar u\|\) 在 \(U\cap B(\bar u,\psi(\delta))\) 控制 **所有可评价的** \(r_F(u)<\eta\)；若要对 \(r_F(u)\ge\eta\) 或 \(+\infty\) 写原式，须另给全域扩展或约定。正阈值只是充分条件，不能标作必要。[C59](canonical/residual_window_bridge.md#rw-positive)。

E104 的闭完整图在零点纤维 \(\{0,1\}\)、其余纤维 \(\{1\}\)，故窗口 \(r_F<1/2\) 只见零点；扁平 gauge 却在 \(r_F=1\) 仍为零。它反驳无条件去窗口，不反驳窗口版，也没有声称满足全对 RL。[RW-FLAT](canonical/residual_window_bridge.md#rw-flat)、[F21](../FAILED_ROUTES.md#f21)。

## E127–E128：C05 的新版本与次临界可行性

E127 合取 **同一** 完整 \(F,S,\lambda,L,\kappa,\gamma,q\)、有限样本 E、两非空紧有限多面体 \(A\subset\operatorname{int}B\)、指定 \(T\) 的整窗每个输出 (1)、C70 的四项 collar、在 \(A\) 邻域的非空紧 usc 有理 acyclic 值、每阶包含上同调满射及 \(\chi(A)\ne0\)。这套条件只要求 \(q>0\)；由 C70 内域余量到紧 span 的 Vietoris–Begle、同伦和 Lefschetz coincidence 给连续 \(h\) 的原关系值域结论。它是 [C05-v2](canonical/local_range_without_supercriticality.md#lr-theorem)，**不是**将原稿 C05-v1 的 \(q\gamma>1\) 偷换为来源事实。E128 的 \(q\gamma=1/2\) 单值区间模型逐项满足同一版本及精确 collar，只证明这个放宽非空，不证明一般原生 \(T\) 的整窗认证。

## E129–E133：完整近端全选择收敛仍不逆推全对 RL

E129–E132 都使用 **同一个** 闭完整实关系 \(F(0)=\{0\}\cup\{1/n\}\)、\(F(x)=\{x\}\) (\(x\ne0\)) 和固定任意 \(\lambda>0\)。E129 的算子真残差 \(r_F=|x|\) 与目标正确 EB 不可换为以 \(d(y,F(0))\) 为右端的两变量残差；后者对所有零消失 gauge 失败。E130 解出完整 \(J(p)=\{p/(1+\lambda)\}\cup(\{0\}\text{ if }p\in\lambda A)\)，因而最小步线性 EB 与 **每条** 允许轨道的保号望远镜总长成立。E131 比较完整图的任意两点：零锚常数 1 不防止离散输入 \(\lambda/n\) 的同输入双输出，故全对零消失模失败。E132 用趋零跨支图差实现任意实斜率，给局部与全域同一个负负二参数区。E133 将 E129–E131 的**同对象**证书合取，以 `limits` 指向 [F25](../FAILED_ROUTES.md#f25) 的正确障碍“动力收敛不逆推全对 RL”；它没有反驳该障碍，也没有把充分的全对收敛定理反向判错。[对象卡](topics/examples/diagonal_spike_relation.md#ds-object) 保存每个完整纤维和端点证明。

## E23、E134–E141：有限状态顶点与两种正则例卡

E134 固定**一个**互异有限状态几何、随机映射、权重和同噪声同步成本 \(R\)；对每对边缘先以 \(C\) 取**最优**运输，再在全部不变目标律 \(\pi\in\mathcal I\) 中最小化 \(R\)。对偶顶点 tight-edge 分支的并恰覆盖这些合法计划。E23 的 C15 只在该固定系统上由全部零成本顶点行边缘不变得到精确零集和锐全域 \(W_2/\Psi\) 常数；凸性属于目标距离平方 \(E\)，**不属于**残差 \(\Phi=\Psi^2\)。C71 是独立可计算实例。E135 的两点翻转在 C15 成立且 \(K=1/2\) 时仍不收敛，故不能把 C15 当动力定理。[FS-THEOREM/BOUNDARY](topics/random_markov/finite_state_certificate.md#fs-theorem)。

E136/E137 固定 \(\Theta:\mathbb R^2\to\mathbb R\) 的完整异维数图。C76 的最近逆点 HREG 线性和固定目标 MSR 半阶是不同量词；C77 对共同 \(|a|,|b|,|y|\le1/4\) 的**两变量** MR 半阶，负目标纤维开放端点只可用于计算距离，不能添入实际图。E138 记录原点连续而参考产品邻域图不局部闭，所以本证明直接用纤维，不能调用缺条件的闭图定理，也不能把此例放到 RL/Cayley 坐标。[HP-MR](topics/examples/hemiregular_piecewise_parabola.md#hp-mr)。

E139/E140 固定同一 \(F=\partial|\cdot|\)，但分别以原算子完整 \(r_F(x)\) 和全输入完整近端 \(|p-J_{\lambda F}(p)|\) 作残差。C78 的局部线性系数下确界为 0，C79 在 \(|p|<\lambda\) 的最优固定点步系数为 1；E141/F27 是**不蕴含边**，不是从一个估计推出另一个估计。全图 \(\gamma=1,L=1\) 的 RL 与无界域 \(\gamma<1\) 的失败仍分别有量词，有限输入窗上的继承幂界不是全图证书。[AV-PROX](topics/examples/absolute_value_subgradient.md#av-prox)。

## E142：固定有限状态残差的正则性与 EB 分离

E142 保持 C15 的**同一**有限互异状态、核、\(C,R\) 与所有不变目标律。对每对边缘，\(C\)-最优计划集非空；[Hoffman 的固定矩阵、一致右端版本](LITERATURE.md#lit-hoffman-1952) 加最大耦合的 \(C\)-成本变化界，控制最优计划集的 Hausdorff 变化。再对同一紧 \(\mathcal I\) 取小，得到 \(\Phi=\Psi^2\) 在**整个** \(\Delta_N\) 全局 Lipschitz；有限 tight-edge 分支与该连续性合取才给连续分片仿射。此边不以 exact-zero 或顶点判据为输入，也不推出 C15 的 EB；图中的 FS-CELLS 输入表示可用于有限分片表示的已核代数，而非把 C15 的结论当作正则性假设。空零面时 [FS-HOFFMAN](topics/random_markov/finite_state_certificate.md#fs-hoffman) 另用正成本下界，不把不一致系统送入外部定理。

## E153：同核不同随机表示的残差身份

E153 固定 C71 的四状态核、\(\pi,C,0<p<1\)，但**新增**一次噪声中的四个逐状态独立 Bernoulli 开关。对不同输入状态同步使用同一四位噪声，成本为 \(p^2(d_i-d_j)^2+p(1-p)(d_i^2+d_j^2)\)；同输入使用同一位，成本为零。对**每个**输入律仍只在 \(\operatorname{Opt}_C(\mu,\pi)\) 内最小化；共同开关的 C71 不等式 \(C\le13A\) 与新无交叉不等式 \(7C\le13B\) 合取，得到 [C88](topics/random_markov/lazy_cycle_representations.md#lcr-sharp) 的精确零集和锐系数。核相同只保持边缘转移与不变律，不能替换残差成本或其锐常数。

## E154–E156：非 tied 二参数图的三种不同门

E154 固定实 Hilbert、同一 \(\Gamma\)、\(\lambda>0,\mu,\rho\) 及**任意两**图点的 (NT1)。无符号门的展开先给 (NT3)；仅在 \(A=1+\lambda\mu+\rho/\lambda>0,\Delta=1-4\mu\rho\ge0\) 时才配方为平移 Cayley 球、图块内单值与普适锐模。\(\Delta>0\) 下 NT9 是**整个参数类**的统一步长开区间；\(A\le0\) 的碰撞例不称每个特定图必坏。E155 另以 \(\Delta>0\) 给整个 \(H\times H\) 的可逆 \((x,v)\mapsto(w,z)\)，全图包含与单调性逐点等价；不需要选步长，却不能代入 \(\Delta=0\)。E156 要 **E154 的满图同参数条件**、\(A>0,\Delta\ge0\) 与 [HE-EXT](canonical/holder_extension.md#he-extension) 的 Hilbert 同常数 Lipschitz 扩张合取，才有图极大当且仅当完整 Minty 域 \(H\)。这三个结论不提供原完整母关系的额外纤维、零点、真残差或动力结论。[NT 正文](canonical/non_tied_cayley.md#nt-object)。

## E143–E145：同一正弦图的局部模不可跨目标合成

E143 在完整 \(F=2+\sin x\) 上固定**每个单独的**步长。\(0<\lambda<1\) 有全图线性全对模；\(\lambda=1\) 的奇数 \(\pi\) 附近才有全对最高 \(1/3\) 阶，且全对与固定基点的**缩窗**锐常数分别为 \(4\sqrt[3]3\)、\(2\sqrt[3]6\)；\(\lambda>1\) 的同输入不同反射输出排除完整全图任意零消失模，不排除较小局部分支。无界全图的次线性失败用周期平移，另于局部证书。

E144 保持同一对象却换到 \((\bar x,\bar y)=(\pi/2,3)\) 的**非零目标**固定目标误差界，最高半阶及缩窗模 \(\sqrt2\)；目标双侧扰动含 \(y>3\) 空逆像，不能声明两变量 MR。E145 只表示这两条估计**不可作为同一零目标 PPA 的合取输入**：E143 临界图点的值为 2，E144 目标为 3，且完整 \(F^{-1}(0)=\varnothing\)。[SN6](topics/examples/positive_sine_phase.md#sin-boundary) 还直接给每条完整近端选择路径趋 \(-\infty\)；不应把“无零集”误画成 C81 或 C82 各自的反例。

## E146–E148：有界平方图的端点与零点窗口

E146 只在完整有界图 \(F(x)=\{x^2\}\) (\(|x|\le1\)) 和固定步长 \(\lambda\) 上陈述全图所有图点对的反射模。\(\lambda=1/2\) 的**锐性见证**来自 \(x=-1\) 的 Minty 平坦端点；\(\lambda>1/2\) 的完整图碰撞阻断任意零消失模。这些都是**自然输入域**上的陈述，不是 \(J\) 满全实定义。E147 在同一图上以 \(S=\{0\}\) 的完整原算子真残差 \(r_F(x)=x^2\) 给零点半阶 EB；其路径部分固定 \(\lambda=1/2\) 且每步输入须仍在 \([-1/2,3/2]\)。E148 是限制边：两项半阶证书**可以在零点同一小窗同时成立**，但其乘积 \(q\gamma=1/4\) 未给局部收缩兼容，负初值又有限步越域；全图最坏锐性位置不能充当零点局部最优指数。[BS 卡](topics/examples/bounded_square_minty.md#bs-object) 给全部公式。

## E149–E152：负平方根受限图的身份与续步门

E149/E150 固定**受限完整关系** \(F_U(x)=\{-\sqrt x\}\) 当 \(0\le x\le1/16\)，其余为空，\(\lambda=1\)；前者只比较该短图内任意图点对，后者用该关系**全部**输出的真残差与自然输入域 \([-3/16,0]\)。E151 改为**另一关系** \(F_\infty(x)=\{-\sqrt x\}\) 当 \(x\ge0\)，其余为空，须另算远支；它不是从 E149 推出的同对象结论。E152 是限制边：短图的全对 \(L=3\)、\(q=2\) 真 EB 和二次一步比值不能给无第二步的短图无限路径，也不能授给有同输入双输出的母图。[F28](../FAILED_ROUTES.md#f28) 保留断点与重启条件。

## E169–E172：完整 Volterra 与负三次的量词隔离

E169 固定**完整** \(V:L^2(0,1)\to L^2(0,1)\)、\(S=\{0\}\)；对每个局部输入半径、残差窗、右极限为零的 gauge 和系数，零均值/高频方向分别用于图几何与**原算子真残差**障碍。其非 rectangular 见证独立于任何外部 BWY 等价。E170 另固定每个 \(\lambda>0\) 的全域完整 \(J_{\lambda V}\)：\(\|J^k\|=1\) 对**每个有限整数** \(k\)，但 \(J^kp\to0\) 对**每个固定** \(p\) 强成立；后一结论需能量式和稠密值域。近端**输入步残差**无消失 gauge EB 用高频输入重新证明，不能从 E169 原算子残差的失败形式迁移。[VO-GRAPH/PROX](topics/examples/volterra_integration.md#vo-graph)。

E171 固定完整 \(F(x)=-x^3\) 和每个固定 \(\lambda>0\)：完整 \(J(0)\) 的三根直接否定零消失全图 RL。**另定义** \(G_M\)、要求 \(3\lambda M^2<1\)，才有该图块内任意两点的锐线性模和仅在 \(D_M\) 上的指定单值 \(T_M\)；图块结论不能改名为完整 \(J\)。E172 的固定零目标真残差与两目标完整逆像是全图命题，其系数分别为 1 与 \(2^{2/3}\)；路径结论却只覆盖 \(T_M\) 的非零逐步合法输入，有限步离开 \(D_M\)。正三次 EX03 的符号对应只传递残差和逆像模，不传递 Minty 分支或轨道。[NC-BRANCH/REGULARITY](topics/examples/negative_cubic_branch.md#nc-branch)。

## E188–E189：伴随 Volterra 的方向与同构范围

E188 固定实 \(L^2(0,1)\) **完整全域** \(V\) 与 \(V^*\)，同一个等距时间反射 \(U\) 满足 \(V^*=UVU\)。它给等距不变图属性和零目标局部 gauge 失败的精确传递；另逐纤维核 \(V^*\) 的右端点 \(y(1)=0\) 与直接非 rectangular 见证。不能把两方向当两次独立等距机制的计数；也不能以来源“标签通过”代替未拆目录属性和外部先行性核验。[AV-GRAPH](topics/examples/adjoint_volterra.md#av-graph)。

E189 再固定**同一个** \(\lambda>0\) 与全输入的完整 \(J\)，而非选定分支或不同参数比较。\(J_{\lambda V^*}=UJ_{\lambda V}U\) 使 C105 的每个固定输入强收敛及每个有限幂范数 1 转移；近端输入步残差的消失 gauge 失败仍有独立高频见证。全图线性 RL 的锐性取等需要零均值**图点差**，不能任意改成零均值输入差；逐点强收敛也不授予单位球统一速率。[AV-PROX](topics/examples/adjoint_volterra.md#av-prox)。

## E190–E192：旋转族的完整参数窗、奇点与取样解释

E190 固定**同一** \(\theta\in[-\pi,\pi]\)、\(\lambda>0\) 的完整实平面旋转图。先用 \(\Delta=1+2\lambda\cos\theta+\lambda^2\) 划开唯一奇点 \(Q=-I,\lambda=1\) 的多纤维与 \(\Delta>0\) 的全域单值完整 \(J\)。仅后者对所有输入对距 \(t\le R\) 给锐 \(L^*=\sqrt{N/\Delta}R^{1-\gamma}\)；输入对距 \(R\) 与各输入球半径 \(R\) 不能互换。无界全图次线性另需排除零反射 \(Q=I,\lambda=1\)。[PR-CAYLEY](topics/examples/planar_rotation_family.md#pr-cayley)。

E191 在同一完整图、每个整数 \(n\ge2\) 的循环量词上逐个 Fourier 模验算，首尾模共同给 \(|\theta|\le\pi/n\)，再由全图极大单调给极大 \(n\)-循环；此证明不依赖外部例号。E192 只取 \(\pi/3,\pi/4\) 两角，合用 C122 的同参数矩阵和 C123 的循环门：逆像系数同为 1、循环阶不同，强单调系数也不同。历史“强模不能决定循环阶”在该族内被 \(\mu=\cos\theta\) 否定，详情 [F34](../FAILED_ROUTES.md#f34)；这条反向纠错不宣称一般算子类也可还原。[PR-TWO-ANGLES](topics/examples/planar_rotation_family.md#pr-two-angles)。

## E173–E174：极点支的完整近端、残差与逐路径门

E173 对**同一完整关系** \(F(0)=\{0\},F(x)=\{-1/x\}\)（\(0<x\le\varepsilon\)）及每个固定 \(\lambda>0\)，分别检查全部 Minty 纤维和任意两图点。\(\lambda\le\varepsilon^2\) 时 \(J(0)=\{0,\sqrt\lambda\}\)，即使 \(\lambda<\varepsilon^2\) 有零输入球，也没有零消失全对模；\(\lambda>\varepsilon^2\) 时全图锐线性 RL 成立，但零输入是自然域孤立点。输入局部 hypo 失败不等于零图点附近的**乘积图窗**失败，后者只有一个图点。[IP-MINTY](topics/examples/isolated_pole_relation.md#ip-minty)。

E174 另用同一完整图的真全纤维残差 \(r_F(x)=1/x\)、小目标的**全部空逆纤维**和完整 J 的逐步合法路径证明 C109；任意 \(q>0\) 的固定目标局部 EB 系数 0 只是缩窗下确界。即使 \(\lambda>2\varepsilon^2\) 时 \(J\) 在自然域上的锐 Lipschitz 模小于 1，所有非零初值仍不能无限留在该域；算子压缩与算法留域不是一条蕴含。[IP-RESIDUAL/PATH](topics/examples/isolated_pole_relation.md#ip-residual)。

## E175–E176：阶梯图的算术纤维、完整残差与缺失覆盖

E175 固定完整 \(F_\delta(0)=\{0\}\)、正负支各有有理/无理两个输出水平、\(0<\delta<1/2\)，要求**所有**同一 \(\lambda\) 的完整图点对。\(\lambda>\delta\) 给锐全图线性模；\(\lambda\le\delta\) 的反射差不随输入差趋零。\(\lambda<\delta\) 的有理步长虽然 J 单值，跨算术类型仍不连续；无理步长有真正同输入双输出。不能用“无精确碰撞”代替全对零消失模，也不能由零图点局部闭推出输入覆盖。[RS-FIBERS/RL](topics/examples/rational_irrational_staircase.md#gx056-fibers)。

E176 对同一原算子的真零残差 \(r_F(x)=c(x)\) 与**完整近端输入最小步残差** \(s_\lambda(p)\) 分别作 EB：前者任意正幂的局部系数下确界 0，后者在整个自然域的锐线性系数 \(1+\delta/\lambda\)。后者必须对每个输入取**全部近端输出**的最小距离，不能只挑一级分支；每个非零合法步使绝对输入至少降 \(\lambda\)，最终因空纤维终止，而零输入是唯一无限轨道。与 C78/C79 只共享残差跳跃，逆像/coverage/路径不同。[RS-RESIDUAL/PATH](topics/examples/rational_irrational_staircase.md#gx056-residual)。

## E177–E179：乘积图的全图、图窗和残差分别量词

E177 固定 **同一** 完整 \(A\times B\subset\mathbb R^2\times\mathbb R^2\)、Euclidean 乘积范数与 \(0<\delta<1/2\)，所有两图点使用同一步长 \(\lambda\)。分量线性锐模在 \(\delta<\lambda<1\) 可取最大；端点 \(\lambda=1\) 的全图半阶以及两侧碰撞须另按直积平方和核算。[PS-PHASE](topics/examples/product_splice.md#gx057-rl-phase)。

E178 固定 \(\lambda=1\)，完整乘积的**所有图点对**半阶锐系数由 (P15) 给出且 \(>2\)。若改成临界参考图点的**输入与输出共同图窗**，第二坐标被 \(|v_2|<1\) 剪去，锐系数才是 2；只限输入而允许全部输出时，每个固定非零窗都严格 \(>2\)，尽管双窗缩小的下确界是 2。这是同一关系的三个不同范围，不是 Claim 数值冲突。[PS-SHARP/WINDOW](topics/examples/product_splice.md#gx057-sharp-product-half)。

E179 的真零残差 EB 使用乘积关系的**全部纤维**，在整个有限残差域的半阶锐系数 1；双侧目标空逆像和每一步完整 J 的合法域另查。第一坐标非零无限迭代将单调增到正极限却违方程；第二坐标非零每步绝对输入至少降 \(\lambda\)。两个机制合取才给唯一无限恒零路径，不能由 EB 或 E178 的 RL 单独推出。[PS-ZERO/PATH](topics/examples/product_splice.md#gx057-zero-eb)。
## E193–E194：同一盘法锥的图几何与完整近端

E193 固定 \(\mathbb R^2\) 单位闭盘上的**完整** \(F=K+N_B\)；对全部图点的法向参数式给单调性，任意两个内点令强单调及 cocoercivity 正系数失败。Rectangular 的固定 \(\xi\) 只在 \(\operatorname{dom}F=B\)，\(\eta\in\operatorname{ran}F\)；不能把紧盘下界写成任意盘外输入。非 paramonotone 用同一零配对的内点交叉见证。极大性还依赖下一条的满 Minty 输入，不由标签推出。

E194 在同一完整关系上对**每个** \(\lambda>0\) 与每个 \(p\in\mathbb R^2\) 反演全部法向射线；内外闭式在 \(\sqrt{1+\lambda^2}\) 连续接合，给全域完整单值 \(J_{\lambda F}\) 及极大单调。由 E193 的单调性，\(R=2J-I\) 对全部输入对非扩张；两个不同内点取等，故全图线性 RL 锐常数 1。\(Jp\in B\) 且输入无界否定任意全域次线性幂模；有界输入对距窗口不受此否定。C98/C99 的逆像 MR 使用原算子目标残差，不能从反射模互换。[SB 卡](topics/examples/skew_ball_inverse.md#sb-prox)。

## E203：紧预算谱只在已闭关系上半连续

E203 固定**一种**认证 \(C\in\{\mathrm{LT},\mathrm{direct},\mathrm{energy}\}\)、拓扑对象空间 \(X\)、正整数 \(j\)、紧实步长区间 \(I_j\) 与**在 \(X\times I_j\) 中闭**的实际预算关系 \(B_{C,j}\)。同一闭关系的纤维 \(\Sigma_{C,j}(G)\) 可空，仍在开集定义下上半连续；非空投影闭。仅当这些预算块**等价穷尽**该认证的真实存在谓词，可数闭投影的并才给 \(F_\sigma\)。[OS9](operator_space.md#os-spectrum-proof) 给抽象证明和下半连续反例。对 LT、direct、energy 各自的完整图、真残差、coverage、留域与证书参数闭性仍是独立义务；本边既不推出三类谱间包含，也不赋予总体大小量尺。

## E204–E205：同一图块的共同整球尾与完整近端门

E204 只在 [R01/R02](rleb_ppa.md#r01) **同一**有限维图块、最近零锚、真残差、gauge 评价域、输入 coverage、直接兼容与严格留域上，选 \(\bar x\in S\cap U\)、\(B_\rho(\bar x)\subset U\)、\(0<\varepsilon\le R\) 及 \(\varepsilon+\mathcal L(\varepsilon)<\rho\)。全部初值 \(B_\varepsilon(\bar x)\) 的轨道进入共同 \(W\)；局部全对 RL 给**该同一个** \(J_{\mathcal G}\) 的 \(H\)-Hölder 单步，逐点距离率和实际步长求和给 SS-B3 的统一**点尾**，才调用 SS-TRANSFER 的 SS-T2。附加超几何距离递推才调用 SS-T3。逐初值不同尾常数不能拼作这一边。

E205 采用充分门 \(J_{\lambda F}(u)=\{J_{\mathcal G}(u)\}\) 对**全部** \(u\in W\)；于是 E204 的整球图块轨道、尾和极限模逐步成为完整 PPA 结论。整窗等式并非逻辑必要：仅在所有球初值的实际可达输入上核全部纤维同一性也足够；但只在初值球上核不覆盖后来输入。[F03](solution_selection.md#f03) 的闭完整并图 \(F(y)=\{y,-y\}\) 给 \(J_F(0)=\mathbb R\) 而图块 \(J_{\mathcal G}(0)=0\)。[C136 正文](canonical/solution_selection_rates.md#ss-rleb-ball) 给明确 \(W,H,M,\sigma\) 及附加速率常数。

## E206–E207：完整几何尾图的证书与实际速率

E206 的对象固定为 [GC-1 完整二支图](canonical/selection_geometric_cap.md#gc-object)，\(\lambda=1\)、Euclidean \(\mathbb R^3\)、完整零集 \(S=\mathbb R^2\times\{0\}\)。所有输入及正负图支由唯一完整 \(J_F=T\) 反演；对任意输入对尺度 \(R>0\) 才给 \(L_R=2\sqrt2+3\sqrt R/2\) 的全对半阶 RL 和完整最小残差 \(d(u,S)\le r_F(u)^2/4\)。\(\kappa_R<1\) 另要求**固定** \(0<R<[2(4-2\sqrt2)/5]^2\)，以及选中步的范数在 \(\psi:[0,\bar t]\) 定义域内；最优渐近 RL 常数不声称每个有限 \(R\) 的 \(L_R\) 最优。[GC 证书](canonical/selection_geometric_cap.md#gc-certificates) 逐式区分这三个尺度。

E207 在**同一**完整 \(T\) 上对所有 \(|r_0|\le R\) 取统一 \(M=2\sqrt2\sqrt R+R\) 和 \(\sigma=1/2\) 的点尾，再以 [SS-TRANSFER](canonical/solution_selection_rates.md#ss-transfer) 得 \(\beta=1\) 的两点**上界**。实际法向率 \(1/4\)、兼容证书 \(\kappa_R\to1/2\) 和由证书导出的保守尾指数是三种不同数据；旧 §3 的配对下界未审，不能把 \(\beta=1\) 标作已证锐性。C137 与 SS-Q2 是不同完整关系，不能拼它们的证书。
