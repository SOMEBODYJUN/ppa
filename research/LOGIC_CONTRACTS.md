# 承重超边的量词与条件契约

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
