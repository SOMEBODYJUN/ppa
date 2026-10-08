# 8/24 NFB v1 与本库 PPA：逐定理、任意同空间分解及标准升维审查

日期：2026-10-08。固定比较基线 `3dd02110d7666ba77b561bf2ab26641013a79fd3`。本文是专篇审查，不改变根 Claim 的身份，也不把先行性判断扩张为全领域新颖性结论。

**结论先行。** Pesquet–Roldán 的 NFB 确实已经给出非单调包含的收敛及物理范数 R-linear 收敛，而且包含普通 Euclidean PPA 的实质子类。非单调线性 \(F=-I,\lambda=3\) 与 C02-v2 的全部条件、实际算法及几何尾真正重合；纯旋转例也已经被其带负残差平方项的强锚条件覆盖。不能把“非单调”“有限长度”或“R-linear”单独当作本库区别。

另一方面，NFB 的 Assumption 3.1 对**任何**合格同空间分解 \(F=A+C\) 都强迫原完整 \(F\) 满足固定有限二次零锚界。这与非退化 C191/C192 的 C193 障碍、C137 cap 图、C141超线性族和 C10 完整对数图直接冲突，因而排除它们的所有此类分解、所有合法固定核 \(M\) 和正定度量 \(S\)，并排除保留完整原图的 §4 标准 primal-dual product lift。这个排除不依赖把 \(C\) 取成零，也不依赖先证明算法不同。它不排除任意别的 lift、只保留零集的 reformulation、删图值、变动物件或尚未认证的模型。

## 1. 固定证据、实际阅读范围和身份门

一手文献：Jean-Christophe Pesquet–Fernando Roldán, *Nonlinear Forward-Backward Algorithm for Solving Non-monotone+Lipschitz Inclusions with Applications to Adjoint Mismatch Problems*, [arXiv:2608.22687v1](https://arxiv.org/abs/2608.22687v1)，2026-08-24。审查使用[固定原 PDF](sources/nfb_2608.22687v1.pdf)，SHA-256 为 `14db75596189d898d97aa9389b3e1a50bbe2ed70e207a3257d681cb4d01077b9`；与 [manifest](sources/manifest.json) 一致。下文页码均为该 PDF 的印刷页码，和 PDF 页序相同。文本抽取只是定位工具，关键公式另渲染 p8、p13、p24、p25 核对；特别是 §4 的 \(\underline\chi,\overline\chi\) 不得被抽取文本合并。

已读规范层：`README.md` 的 Research Goal、Definition/Claim Map；`RESEARCH_STATE.md` 的活跃义务与近期文献入口；`CLAIMS.md` 中 C02-v2、C09/C10、C137、C191–C193 的精确身份；`FAILED_ROUTES.md` 的 F01–F03、F18–F20、F25、F42 等对象/纤维/锚/兼容边界；[C02-v2 正文](../../rleb_ppa.md)、[一般模正文](../../canonical/general_modulus_dynamics.md)、[自然类全文](../../canonical/support_normal_natural_class.md)、[C137 全文](../../canonical/selection_geometric_cap.md)。上述受审正文与固定比较基线无差异。

外文实际范围：§1–2 的问题和半单调定义；§3 p6–17 的 Assumption 3.1、Propositions 3.3/3.6/3.8/3.11、Algorithm 3.7、Theorem 3.10、Corollary 3.12及其证明；§4 p17–29 的产品算子、全部假设、Propositions 4.3–4.8、Algorithm 4.9、Theorem 4.10、特殊情形 4.12/4.14/4.17及证明；§5 p29–31 的应用假设、两种分解、Huber signal recovery 的对象及数值设置。p31–33 的其余图表是数值展示；它们没有新增可替代上述假设的收敛定理。本文核的是这篇 v1 的相关证明和适用接口，未逐篇重审其所有参考文献，未复现作者随机矩阵实验，也没有查遍全部旧文献。

为了消除记号碰撞，下文：原关系叫 \(F\)，NFB 前向部分叫 \(C_{\rm fb}\)，自然类的闭凸法向集合叫 \(K\)，NFB 固定度量叫 \(S_m\)，NFB 的下降常数 (3.8) 叫 \(\Delta\)，本库普通 PPA 步长仍叫 \(\lambda\)。源论文把下降常数也记成 \(\lambda\)，它不是本库的步长。

## 2. 原文 §3 的完整适用门和实际结论

### 2.1 Assumption 3.1 / Algorithm 3.7 / Theorem 3.10

Assumption 3.1 在 p6；半单调的量词定义 (2.3) 在 p4。其锚定版本的含义是：每个指定解图点都与**全部** \(A\) 图点比较，不只是轨道图点之间比较，也不只是接近某个解的点比较。

| 原文门 | 精确对象与量词 | 本库对应/差别 |
| --- | --- | --- |
| 固定实 Hilbert 空间 | 可无限维；\(S_m\in\mathcal B(H)\) 有界、自伴、strongly monotone；因此 \(S_m^{-1}\) 有界，两种范数等价 | C02-v2/C09 的已证范围是 Euclidean 有限维；不能从此自动增加无限维身份 |
| \(C_{\rm fb}:H\to H\) | 在全部 \(H\) 上、相对 \(S_m\) 的 \(\beta\)-cocoercive，\(\beta>0\)；(2.1) 是对任意两个输入 | 完整真 EB \(r_F\)、RL 模与此条件不是同一残差/几何轴 |
| 3.1(i) | \((M+A)^{-1}\) 在全部 \(H\) 有定义且单值 | 相当于该 warped resolvent 的完整 coverage+单值，不等于 \(J_{\lambda F}\) 的完整纤维门 |
| 3.1(ii) | 完整 \(\operatorname{gph}\(A+C_{\rm fb}\)\) sequentially weak–strong closed | 原文 p12–13 (3.35)–(3.36) 用它识别弱 cluster point 为解；不能只核 \(A\) 或一条选择图 |
| 3.1(iii) | \(A\) 在 \(\{(z,-C_{\rm fb}z):z\in\operatorname{zer}F\}\) 上 \(\rho S_m^{-1}\)-comonotone；\(\rho>-\beta\) | 不是一般 \((\mu,\rho)\) 允许任意负 \(\mu\) 的条件。此处 \(\mu=0\) 的锚门已经产生 §3 必要二次界 |
| 3.1(iv) | \(\zeta\in[0,1/2)\)，\(\tau> -\zeta\widehat\rho/(\beta+\widehat\rho)\)，\(\tau M-S_m\) 相对 \(S_m\) 为 \(\zeta\)-Lipschitz；\(\widehat\rho=\min\{\rho,0\}\) | 任意合法核被允许，但必须携全部这些条件；不能以“nonlinear kernel”名称免检 |
| Algorithm 3.7 | 任意 \((x_0,u_0)\in H^2\)，\(0<\theta<2\)；三式 (3.6a–c) 定义 warped implicit step、memory、relaxation | 它通常不是普通 PPA；但 §6 给真实相同及非零前向/非零 memory 相同例，不能作假 iff |
| Theorem 3.10(i) | 还要 (3.8) 的 \(\Delta>0\)；结论是 \(x_n\) 弱收敛到某个解 | 在本库有限维中，弱收敛就是范数收敛；该部分没有统一几何点尾或有限长结论 |
| Theorem 3.10(ii) | 同一 \(A\) 在同一全部解锚上满足 \((\mu S_m,\rho S_m^{-1})\)-semimonotonicity，\(\mu>0\) | 结论是到**唯一**解的物理范数 R-linear 收敛；“不要求强单调”不等于没有强锚项 |

Algorithm 3.7 精确为
\[
p_{n+1}=(M+A)^{-1}(Mx_n-C_{\rm fb}x_n+u_n/\tau),\quad
u_{n+1}=(\tau M-S_m)p_{n+1}-(\tau M-S_m)x_n,
\]
\[
x_{n+1}=(1-\theta)x_n+\theta p_{n+1}. \tag{N1}
\]
源 (3.7) 取 \(\eta=1\) 当 \(\theta\ge1\) 且 \(S_m-\tau M\) monotone，否则 \(\eta=1+|1-\theta|\)。记 \(\zeta_M\) 为 \(M\) 的相应 Lipschitz 模，源 (3.8) 为
\[
\Delta=2-\theta-2\eta\zeta
-\frac{(\tau+2\widehat\rho)^2}{2\tau[\beta+\widehat\rho(1+\zeta/\tau)]}
+2\widehat\rho\tau\left[(\zeta/\tau+\zeta_M)^2+4\zeta/\tau\right]>0. \tag{N2}
\]
最后一项在 \(\widehat\rho<0\) 时为非正；例子计算不能漏掉它。

### 2.2 原证明的承重步骤

p9–12 的 Proposition 3.8 由 (3.14) 的真实 warped inclusion，和**同一**解图点 \((z,-C_{\rm fb}z)\) 得 (3.16)/(3.17)。memory 的界使用 (3.20)，前向差用 cocoercivity 和 Young 界 (3.28)。3.1(iv) 保证消去 \(\|C_{\rm fb}x_n-C_{\rm fb}z\|^2\) 时分母正；不是可以省略的步长装饰。由 (3.31) 的 relaxation 恒等式得到
\[
a_{n+1}\le a_n-\theta\Delta\|p_{n+1}-x_n\|_{S_m}^2,
\quad a_n\ge(1-\theta\zeta)\|x_n-z\|_{S_m}^2. \tag{N3}
\]
这里源 (3.9) 的 \(\lambda_1\ge0\)，源 (3.10) 的 \(a_n\) 含 \(\|x_n-z\|^2_{S_m}\)、memory 交叉项以及 \(\theta\lambda_1\|p_n-x_{n-1}\|^2_{S_m}\)；不能把它当作本库的 \(V(d(x_n,S))\)。

p12–13 的 Theorem 3.10(i) 先给平方可和的**算法步**、boundedness、\(u_n\to0\)，再由 (3.33)–(3.35) 构造趋零的完整 \(F\) 图值，借 3.1(ii) 识别 cluster points；每个解锚的距离有极限，最后用 Opial。平方可和本身不推出有限长。这里未发现承重代数反例；Opial 和外部 range/averagedness 引文仍是作者明确导入的标准工具，本文没有把其所有来源重新证明。

Theorem 3.10(ii) 的唯一性已经由 p8 Proposition 3.6 的 (3.3)–(3.5) 证明：两个零点的比较给
\(0\ge\mu\|z-z'\|^2_{S_m}+(\rho+\beta)\|C_{\rm fb}z-C_{\rm fb}z'\|^2_{S_m^{-1}}\)，于是相等。p13 的 (3.37)–(3.40) 将强锚项加入 N3，得到某个 \(\vartheta_2>0\) 下
\[
a_n\ge(1+\vartheta_2/2)a_{n+1}.
\]
源 \(\vartheta_1=\theta\min\{\tau\mu,\Delta/3\}\)，\(\vartheta_2=\vartheta_1\min\{1,1/\lambda_1\}\) 若 \(\lambda_1>0\)，否则为 \(\vartheta_1\)。通过 N3 的下界和范数等价，明确得到普通物理范数几何点尾；不是只有能量线性下降。式子从 \(n\ge1\) 开始只改变有限初始常数。

p14–17 的 Proposition 3.11 和 Corollary 3.12 把 \(\Delta>0\) 改写成 cubic/特殊区间，没有删除 Assumption 3.1。3.12(i) 的 \(\tau M=S_m\) 给 FB；3.12(ii) 的 \(C_{\rm fb}=0\) 利用零算子对任意 \(\beta>0\) cocoercive 并令 \(\beta\to\infty\)，给 comonotone 情形；3.12(iii) 给 monotone+cocoercive。它们没有建立任意非 Hölder RL+EB 的 PPA 定理。

## 3. 决定性必要条件：量化全部合格同空间分解

**命题 N-ANCHOR（本文从源假设直接推导）。** 假设完整原关系恰为 \(F=A+C_{\rm fb}\)，且 3.1 的 \(C_{\rm fb}\) 与 anchored \(A\) 条件成立。对**每个** \(z\in\operatorname{zer}F\)、**每个** \((x,w)\in\operatorname{gph}F\)，必有
\[
\langle x-z,w\rangle\ge q\|w\|^2_{S_m^{-1}},\qquad
q=\frac{\beta\rho}{\beta+\rho}\in\mathbb R. \tag{N4}
\]
因此存在固定有界 PSD 算子
\[
V=\max\{0,-q\}S_m^{-1}
\quad\text{使}\quad
\langle x-z,w\rangle\ge-\langle w,Vw\rangle. \tag{N5}
\]

**严格证明。** 令 \(c=C_{\rm fb}x-C_{\rm fb}z\)。完整图等式保证 \(a=w-C_{\rm fb}x\in Ax\)，解锚给 \(-C_{\rm fb}z\in Az\)。所以源 (2.3)/3.1(iii) 和 (2.1) 分别给
\[
\langle x-z,w-c\rangle\ge\rho\|w-c\|^2_{S_m^{-1}},\qquad
\langle x-z,c\rangle\ge\beta\|c\|^2_{S_m^{-1}}.
\]
相加并完成平方：
\[
\rho\|w-c\|^2_{S_m^{-1}}+\beta\|c\|^2_{S_m^{-1}}
=\frac{\beta\rho}{\beta+\rho}\|w\|^2_{S_m^{-1}}
+(\beta+\rho)\left\|c-\frac{\rho}{\beta+\rho}w\right\|^2_{S_m^{-1}}.
\tag{N6}
\]
由于 \(\rho>-\beta\)，末项非负，N4/N5成立。这里源 Lemmas 2.1–2.2 p5 给相同平方配方；它们的全对结论在本题只需要逐锚的版本，量词仍完整。没有使用 \(M\)、\(\tau\)、\(\theta\)、resolvent 单值性、\(\Delta\)，因此不存在通过另选合法核解除此必要门的路径。

结论形式必须是：若某个完整原图在某解锚的**每个图邻域**都违反所有固定有限 \(V\) 的 N5，则**不存在**任何合格同空间 \(A+C_{\rm fb}\) 分解。\(\beta,\rho,S_m,M\) 可以依赖候选分解；每个合法分解仍会生成某个固定有限 \(V\)，故全被排除。对有限维任意 SPD 矩阵，包括有交叉项和病态但有限的矩阵，均有效。\(\rho=-\beta\) 的边界、退化/非有界度量、iteration-dependent 度量不在源假设中，不能拿来制造本定理内的反例。

这比只检查 \(C_{\rm fb}=0\) 强。若 \(C_{\rm fb}=0\)，源条件本身就给有限 \(\rho S_m^{-1}\) 锚界；3.12(ii) 令 \(\beta\to\infty\) 的表述也没有移除它。

## 4. 逐对象排除及不能删除的退化门

### 4.1 C191/C192 的非退化完整自然类

[C191/C192](../../canonical/support_normal_natural_class.md) 的完整关系分别是
\[
F_A(t,y)=\{(b\|y\|^\alpha(v-f),Ny+n):v\in V_D(t),\ n\in N_K(y)\},
\]
\[
F_B(t,y)=\{(by^\alpha(v-f),a(t)y+n):v\in V_D(t),\ n\in N_{\mathbb R_+}(y)\}.
\]
这里 \(f\notin D\)、\(0<\alpha<1\)；C191 必须加 \(K\ne\{0\}\)。零集为整个切向平面 \(\mathbb R^m\times\{0\}\)。它们是完整原图，不是只选中一条合法法向支。

C193 的严格见证如下。固定任意解锚 \(\bar u=(\bar t,0)\)，令 \(v_0=P_Df\)、\(e=(f-v_0)/d_D\)。投影分离给 \(\langle e,v-f\rangle\le-d_D\) 对**全部**面值。取 \(0<\eta<\alpha\)、\(t_\epsilon=\bar t+\epsilon^\eta e\)，C191 取 \(y_\epsilon=\epsilon h\)，其中固定 \(0\ne h\in K\)；C192 取 \(y_\epsilon=\epsilon\)。法锥图值可以取零，任取同点支撑面值。因此
\[
\langle u_\epsilon-\bar u,w_\epsilon\rangle
\le-c\epsilon^{\alpha+\eta}+O(\epsilon^2),\qquad
\|w_\epsilon\|^2=O(\epsilon^{2\alpha}),\quad c>0.
\]
由于 \(\alpha+\eta<2\alpha<2\)，配对与残差平方之比趋向 \(-\infty\)。两坐标图点和图值均趋于 \((\bar u,0)\)，任意固定 \(V\) 的二次项至多 \(\|V\|\|w_\epsilon\|^2\)，所以每个局部图邻域也失败。由 N-ANCHOR，**全部同空间分解/固定合法度量/核排除**，连 Theorem 3.10(i) 的前件都无法满足；无需先用 source(ii) 的唯一性区分。

自然类确实有可调用的非退化 C02-v2 实例，不是仅有“EB+Hölder”而兼容空缺。C191 SN8/SN9 给完整全对 RL 与真 EB，SN10 的同实例门 \(R_D(1+\lambda a)^{-\alpha}<d_D\) 加小尺度严格半径给 \(\kappa<1\)，全输入 coverage 与完整纤维单值已证。C192 要保留 SN14 的小条带唯一、SN15 的图块模及完整条带排他；全域存在/全部选择有限长是另一个直接结论，不能把它写成全域单值。二者独立的法向/切向长度证书不要求 SN10。

**真实退化重合。** C191 若 \(K=\{0\}\)，完整关系精确为 \(F_A(t,0)=\{0\}\times\mathbb R^r\)，域外为空，就是切向平面的 normal cone。普通 PPA 是正交投影 \((p,\xi)\mapsto(p,0)\)。取 \(A=F_A,C_{\rm fb}=0,S_m=I,M=I/\tau,\theta=1,u_0=0\)，任意固定正 \(\tau\) 给完整单值 warped inverse；锚配对非负，闭图、\(\rho=0\)，选足够大有限 \(\beta\) 使 \(\Delta>0\)，source(i) 适用，算法一步到解。source(ii) 的唯一性门不满足非孤立零集，但实际特殊算法仍有限长。不能删去 C193 的非零集合门。

### 4.2 C137 完整 cap 图

固定任意 \(\bar u=(\bar\xi,\bar\eta,0)\)。对 \(0<\eta<1/2\) 取
\(u_\epsilon=(\bar\xi+\epsilon^\eta,\bar\eta,\epsilon)\)，选择 GC-1 的正法向图值
\(w_\epsilon=(-2\sqrt\epsilon,-D_\epsilon(\bar\eta),3\epsilon)\)。这是原**完整**图中的合法值，且 \(0\le D_\epsilon\le2\sqrt\epsilon\)。于是
\[
\langle u_\epsilon-\bar u,w_\epsilon\rangle
=-2\epsilon^{\eta+1/2}+3\epsilon^2,
\quad\|w_\epsilon\|^2\le8\epsilon+9\epsilon^2.
\tag{N7}
\]
负项阶 \(\eta+1/2<1\) 支配任何有限二次项；图值与点都趋零锚。因此 C137 也违反所有 N5，排除全部合格同空间分解/固定核/固定度量。负法向支不是必须使用的反例，但它仍必须保留在算法完整纤维里。

C137 的 GC-2 已反演全部正负输入；GC-3/4 是完整全对模/完整最小残差，GC-5/6 给同窗严格兼容，所以它是 C02-v2 的完整普通 PPA 实例。GC-8 的同一非孤立零集几何点尾并没有靠 source(ii) 的强锚+唯一解取得。此处最有意义的差别是**假设及完整对象**，不是有限长度结果的字样。

### 4.3 C10 完整对数图及 C09 的非幂 Dini 实例

对任意固定 \(a>0\)，GM29 的完整关系为
\(F_a(\xi,y)=\{(-\ell_a(4y),3y),(-\ell_a(4y),-5y)\}\)（\(y\ge0\)）。固定任意锚 \((\bar\xi,0)\)，写 \(h=\ell_a(4y)\) 并取图点
\(u_y=(\bar\xi+\sqrt h,y)\)、图值 \(w_y=(-h,3y)\)。则
\[
\frac{\langle u_y-\bar u,w_y\rangle}{\|w_y\|^2}
=\frac{-h^{3/2}+3y^2}{h^2+9y^2}\longrightarrow-\infty. \tag{N8}
\]
理由：\(h\downarrow0\)，而对数幂 \(h\) 比任意正幂 \(y^\gamma\) 慢趋零，故 \(y^2=o(h^2)\)。图点/图值趋锚。因此对**每个 \(a>0\)**，全部合格同空间分解/固定度量/核均排除。

这包含两种不同动力结论：\(a>1\) 的完整图满足同尺度兼容和 Dini，是 C09 的真实非幂有限长度实例，但 GM39 的点尾是多项式阶 \(k^{1-a}\)，没有几何点尾；\(0<a\le1\) 的轨道切向发散而到零集距离仍按 \(4^{-k}\) 下降。源 Theorem 3.10 的前件在整个族中均失败；C10 没有构成对源定理的反例。此族的 Dini 阈值不代表所有非 Dini 模都发散。

### 4.4 C141 的完整超线性法向族

本轮补读 [C141-v1身份与SF-1–12全文](../../canonical/selection_superlinear_family.md)。它固定 \(\lambda=1\)、\(0<\gamma<1,\nu>1,A_s,B_s>0\)，完整图在 \(y\ge0\) 处令 \(a=y^{1/\nu}\)，两个值为
\[
(-A_sa^\gamma,\tau_a(\eta)-\eta,a-y),\qquad
(-A_sa^\gamma,\tau_a(\eta)-\eta,-a-y),
\]
其中 \(|\tau_a(\eta)-\eta|\le B_sa^\gamma\)，零集仍为整个切向平面。系数 \(A_s,B_s\) 与 NFB 算子 \(A\) 不同。

固定任意零锚 \(\bar u=(\bar\xi,\bar\eta,0)\)，取 \(0<\delta<\gamma/\nu\) 及
\[
u_\epsilon=(\bar\xi+\epsilon^\delta,\bar\eta,\epsilon),\qquad
w_\epsilon=(-A_s\epsilon^{\gamma/\nu},
\tau_{\epsilon^{1/\nu}}(\bar\eta)-\bar\eta,
\epsilon^{1/\nu}-\epsilon).
\]
这属于完整正支；第二坐标位移为零，所以即使 \(\bar\eta>0\) 也不贡献pairing。直接得到
\[
\langle u_\epsilon-\bar u,w_\epsilon\rangle
=-A_s\epsilon^{\gamma/\nu+\delta}
+\epsilon^{1+1/\nu}-\epsilon^2,\qquad
\|w_\epsilon\|^2=O(\epsilon^{2\gamma/\nu}). \tag{N8a}
\]
这里 \(2/\nu>2\gamma/\nu\)，且 \(1+1/\nu>2\gamma/\nu>\gamma/\nu+\delta\)。负项支配所有固定有限二次项，完整图点/图值都趋锚。因此全部C141参数及每个解锚均违反N5；全部合格同空间分解和标准full-graph product lift同样排除。若只取 \(\bar\eta\le0\)，第二图值分量还精确为零，但此额外限制不是必要的。

SF-2的完整近端为 \((z+A_s|r|^\gamma,p+B_s\min\{p_+,|r|\}^\gamma,|r|^\nu)\)。它在充分小的共同输入collar有SF-3/4/5的完整纤维、真EB和严格兼容，并在 \(|r_0|<1\) 有共同超几何尾；本文没有把这条局部收敛范围扩成全部初值收敛。N8a序列最终位于任意固定正collar，因此局部限制也不会消除这个原图锚障碍。

## 5. §4 标准 primal-dual lift：完整图保真时仍被排除

原文 Notation 4.1 p17 的算子是
\[
\mathbf A(x,u)=((A_0+D)x+L^*u)\times(B^{-1}u-Lx),\qquad
\mathbf C(x,u)=(C_0x,0).
\tag{N9}
\]
原 primal 关系为完整 Minkowski sum
\[
F(x)=(A_0+D+C_0)x+L^*BLx. \tag{N10}
\]
**标准全图 lift 排除命题。** 若 N10 恰为所比较的完整原关系，且 N9 满足 NFB Assumption 3.1，则原 \(F\) 仍满足一个固定有界 PSD 二次零锚界。

证明：给任意 \(w\in F(x)\)，完整和的含义提供实现这个值的 \(u\in BLx\) 及 \(a\in A_0x\)，因此
\[
((x,u),(w,0))\in\operatorname{gph}(\mathbf A+\mathbf C).
\]
给任意 \(z\in\operatorname{zer}F\)，同样可选实现零值的 \(v\in BLz\)，于是 \((z,v)\) 是 product 零点。对 product N4 应用，若 \(I_H:w\mapsto(w,0)\)，得到
\[
\langle x-z,w\rangle
\ge q\langle w,Qw\rangle,\qquad
Q=I_H^*\mathbf S_m^{-1}I_H\in\mathcal B(H).
\tag{N11}
\]
所以 \(V_H=\max\{0,-q\}Q\) 固定、有界、PSD。product 度量允许任意合法固定交叉块；对偶残差恰为零使 pairing 无对偶项。所选 \(u\) 可能离 \(v\) 很远也不影响：源条件对**全部图点**与解锚全局量化，根本不要求 lifted 点在局部邻域。这堵住“原图反例局部但 lift 变量不局部”的逃口。

因而 §4 原样的 full-graph product split 不能覆盖 §4 上述 C191/C192非退化、C137、C141、C10 原图。结论只使用完整图等式及源 §3必要门，不需要假定任意 primal-dual 更新就是原 PPA。

### 5.1 逐结果核对 §4 的额外门

| 原文结果/页码 | 必须同时携带的门及证明用途 | 覆盖判断 |
| --- | --- | --- |
| Assumption 4.2, p17 | \(\nu_A,\nu_B\ge0\)；两组 \(\mu\)/\(\rho\) 和非负，零和时分量都零；\(A_0+D\)、\(B\) 分别在全部 product 解诱导的锚上有指定半单调矩阵项；\(J_{\tau A_0},J_{\sigma B^{-1}}\) 全域单值，两个非空步长集合；完整 product \(\mathbf A+\mathbf C\) weak–strong 闭 | 不能只核 primal 的可解性或强法向收缩；这里没有把任意自然法锥母类免费带入 |
| Proposition 4.3, p19 | mismatch \(D=K\widetilde D T\) 或有界线性 \(D\)；分别有残差平方模的正和门/矩阵 monotonicity；所得 \(\nu_A\) 还需非负才进入 4.2 | 给特定 mismatch 数据的半单调证书；不包含任意非 Lipschitz cusp |
| Proposition 4.5, p20–21 | 指定符号条件下只有 resolvent 在 range 上单值；full domain 还保留明确 range 条件，或该命题最后指定的 maximal 子情形 | “maximal”字样不保证所有半单调组合自动满域 |
| Propositions 4.6/4.7, p21–24 | completion of squares 得 \(\widehat\mu\ge0,\widehat\rho\le0\)；\(\sigma\tau\|L\|^2<1\)；固定 block \(S_m\) 为 (4.12)；正模乘 \(\underline\chi=(1+\sqrt{\sigma\tau}\|L\|)^{-1}\)，负模乘 \(\overline\chi=1+\sqrt{\sigma\tau}\|L\|\) | 这正把 product 前件送入源 §3；不能省略负模的更大系数 |
| Proposition 4.8 / Algorithm 4.9, p24 | 特定核 (4.19) 消去 \(D\)，block triangular inverse (4.20)；实际更新 (4.21) 有 reflected/memory \(D\) 项、两次 resolvent及 relaxation | 普通 primal PPA 的轨道等式仍需另证；对象满足不等于算法同一 |
| Theorem 4.10, p24–25 | 全部 4.2 + \(\kappa=1-\sigma\tau\|L\|^2>0\)、\(\beta\kappa+\overline\chi\widehat\rho(1+\vartheta/\kappa)>0\)、(4.23)；证明以 \(\zeta=\tau\vartheta/\kappa\)、\(\rho=\overline\chi\widehat\rho\)、前向常数 \(\beta\kappa\) 还原 3.7，(4.23) 确保 \(\Delta>0\) 及 \(\zeta<1/2\) | (i) product 弱收敛；(ii) 还需 \(\nu_A>0,\nu_B>0\)，给唯一 product 解的物理范数 R-linear；N11排除表列原全图 |
| Proposition 4.12 / Corollary 4.14, p26–27 | \(D=0\) 的 Condat–Vũ；保留 product 闭性、源对应符号/maximal/resolvent门，及 (4.28)/(4.29) 的步长限制；\(C_0=0\) 的 CP 通过 \(\beta\to\infty\) 简化 | 仍是 §3链下的标准 product；没有绕过 N11 |
| Assumption 4.16 / Proposition 4.17, p27–29 | \(B=L=0\)，\(A_0+D\) anchored \((\nu_A,\rho_A)\)，\(\nu_A\ge0\)；\(J_{\tau A_0}\)全域单值，完整和闭；(4.35) 正和及 (4.36) quadratic；反射记忆式 (4.34) | (i)弱收敛；(ii) \(\nu_A>0\) 唯一解R-linear；把 \(A=A_0+D\) 代入N4即可排除对应原图 |

上述重构未发现与本比较有关的 fatal 证明断口。源 §4 的 kernel/metric 正定性与 Lipschitz估计部分显式引用 [48]；本审查核其后续参数替换及全部逻辑门，并以 N11 完整必要条件作排除，而不是把未逐篇重读 [48] 当作支持新颖性的证据。

### 5.2 不能从 N11 推出的结论

没有证明“任何升维都不可能”。若新模型只与原 \(F^{-1}(0)\) 等价，或把原图值删除/改变，或残差 lift 不是固定 \((w,0)\)，或换了原空间/完整关系/步长/轨道，就不能直接应用 N11。对任意新 lift 的最小义务是：完整图值如何提升；哪些 product 零点投影到原零集；pairing 和残差平方如何回到原坐标；metric/核是否固定有界；product 迭代投影是否逐步等于原普通 PPA。只证明解集相同不足以把 source 定理称为覆盖本库原算法。

## 6. 真实重合：包含非单调 PPA，且非零前向项也可能完全同一

### 6.1 一般相同判据，避免错误的“仅 \(C=0\)”判断

标准充分还原门是 \(C_{\rm fb}=0,S_m=I,\tau M=I,\theta=1,u_0=0\)，于是 N1 精确为 \(x_{n+1}=J_{\tau F}x_n\)。这只是一个充分门，不是固定实例的必要条件。

逐状态精确判据：给定目标 \(q\in J_{\lambda F}x\)，令 \(p=x+(q-x)/\theta\)。因 \((M+A)^{-1}\) 单值，当前 NFB 步等于这个 PPA 步，当且仅当
\[
Mx-C_{\rm fb}x+u/\tau-Mp\in Ap. \tag{N12}
\]
要得到完整轨道同一，还必须从授权初始 memory 开始逐步验证 N12 和 (3.6b) 的不变关系；不是只检一个目标零点。在 \(\theta=1\)、\(F(q)\) 单值的情形，判据化为
\[
Mx-Mq-(C_{\rm fb}x-C_{\rm fb}q)+u/\tau=(x-q)/\lambda.
\]

### 6.2 完整同一例和所有门

| 固定原对象/普通 PPA | 合格 NFB 参数及全部关键门 | 精确重合及本库身份 |
| --- | --- | --- |
| **非单调** \(F=-I\) on \(\mathbb R^n\)，\(\lambda=3\)；\(J_{3F}x=-x/2\) | \(A=F,C_{\rm fb}=0,S_m=I,M=I/3,\tau=3,\theta=1,u_0=0\)；\(\rho=-11/10,\mu=1/10,\beta=100,\zeta=0,\zeta_M=1/3\)。完整 \(M+A=-2I/3\) 可逆；完整图闭；anchored半单调式为 \(-\|h\|^2=(\mu+\rho)\|h\|^2\)；\(\rho>-\beta\)，步长门成立，N2为 \(0.2655881361644759>0\) | source 3.10(ii) 与 C02-v2 真正相交：\(\gamma=1,L=2,\psi(s)=s,\kappa=1/2,U=H\)；完整纤维、零锚、gauge、全部尺度兼容与无边界预算全满足。到唯一0的因子为1/2；有符号振荡，不是 monotone 偷换 |
| 纯旋转 \(F=R:(x_1,x_2)\mapsto(-x_2,x_1)\)，\(\lambda=1\)；\(J_F=(I+R)^{-1}\) | \(A=F,C_{\rm fb}=0,S_m=M=I,\tau=\theta=1,u_0=0\)，\(\mu=1/4,\rho=-1/4,\beta=1,\zeta=0,\zeta_M=1\)。\(\langle h,Rh\rangle=0=(\mu+\rho)\|h\|^2\)；full inverse及closed graph；N2 = \(1-1/6-1/2=1/3>0\) | 普通PPA物理范数因子 \(1/\sqrt2\) 已由source(ii)覆盖，虽 \(F\) 无强单调性；对应本库C24旋转例的速率先例。它的 \(\gamma=1,L=1,\psi(s)=s\) 在该步长给兼容比1，故不能误写为C02严格兼容的重合 |
| \(F=2I,\lambda=1\)，**非零** \(C_{\rm fb}=I/2\) | \(A=3I/2,M=3I/2,S_m=3I/2,\tau=\theta=1,u_0=0\)；\(\beta=3,\rho=0,\mu=1,\zeta=0,\zeta_M=1\)，N2=5/6；所有线性full inverse和闭图门均成立 | \((M+A)^{-1}(Mx-C_{\rm fb}x)=x/3=J_Fx\)，memory恒0。前向部分可被核和度量吸收；不能因 \(C_{\rm fb}\ne0\) 就说算法不同 |
| \(F=I,\lambda=1\)，非零memory补偿 | \(C_{\rm fb}=I/10,A=M=9I/10,S_m=I,\tau=\theta=1,u_0=x_0/10\)；\(\beta=10,\rho=0,\mu=9/10,\zeta=1/10,\zeta_M=9/10\)，N2=3/4；full inverse/closed graph和所有锚门成立 | 归纳 \(u_n=x_n/10\)，N1得 \(p_{n+1}=x_n/2\)，\(u_{n+1}=p_{n+1}/10\)；所以同一步长、同物理坐标的普通PPA完全相同，尽管 \(\tau M\ne S_m\) |
| C191的 \(K=\{0\}\) | 见 §4.1 的normal-cone参数；源(i)不要求唯一零点 | 普通PPA一步投影，真实退化重合；不能把source(ii)唯一性套到整个平面零集 |

这些线性例的完整图、完整 inverse 和闭性都是直接矩阵等式；表中用真实原图的最小残差，没有删去支值。非单调 \(F=-I\) 可以选不同强锚模；所列数值仅给一个完整、可重算的证书，不宣称最优步长区间。

更一般，若 \(C_{\rm fb}(x)=Hx+c\)、\(M(x)=\lambda^{-1}x+C_{\rm fb}(x)+m_0\)、\(S_m=\tau(\lambda^{-1}I+H)\) 正定，另取 \(\theta=1,u_0=0\)，且所有source几何门另核，那么 \(\tau M-S_m\) 是常值、memory从0保持0，N1精确为 \(J_{\lambda F}\)。固定线性实例还可能通过 relaxation 重标步长：\(F=aI,C_{\rm fb}=0,M=I/\tau,S_m=I,u_0=0\) 时，只要 \(1+\tau a(1-\theta)>0\)，实际映射是步长 \(\lambda=\tau\theta/[1+\tau a(1-\theta)]\) 的PPA。这里也不能把 \(\theta=1\) 写成一切固定实例的必要条件。对于 §4 的排除对象，无论出现哪种算法补偿，N4仍先行排除全部合格分解。

## 7. §5 应用的逐对象核对

p29–30 的 §5.1 对象是单值
\(0=Gx+KTx\)，其中 \(G\) 为 \(\rho_G\)-cocoercive、\(\rho_G>0\)，\(KT\ne0\)，有界线性 \(KT\) 满足
\(KT-\widetilde\rho\,T^*K^*KT\) monotone及 \(\widetilde\rho+\rho_G>0\)。源 Proposition 4.3(ii) 把和认证为 \(\widetilde\rho\rho_G/(\widetilde\rho+\rho_G)\)-comonotone。两种实际分解都已列出：

1. \(A_0=G,C_0=0,D=KT\)：原文调用 Lemma 2.3 的 closed-graph门、\(G\) 的完整最大单调resolvent，并在 Remark 4.18(ii) 的 reflected 更新和步长区间下给弱收敛。
2. \(A_0=0,C_0=G,D=KT\)：仍要 (4.42)、\(\widehat\rho=\min\{0,\widetilde\rho\}\)、\(\beta=\rho_G\)、\(\vartheta=\|KT\|\) 和 (4.43) 区间，调用 Proposition 4.17。

两种方案证明“同一目标存在不止一种合格分解”是真实存在的；本审查因此从完整和的必要界做排除。它们的 reflected 算法不能仅凭相同零集就改叫本库普通PPA；若某个特例重合，须给N12或其他逐步恒等式。

§5.2 p30 的 signal recovery 在 adjoint mismatch 后的真实对象为
\[
0=\lambda_H W^*\nabla H_\delta(Wx)+K(Tx-r),
\]
这里 \(\lambda_H\) 是regularization权重，不能混成本库PPA步长；\(W\) orthonormal，\(H_\delta\) 的梯度 Lipschitz模 \(1/\delta\)，故 \(G=\lambda_H W^*\nabla H_\delta W-Kr\) 的 cocoercivity常数为 \(\delta/\lambda_H\)。本文直接核了这个缩放。原文选有限随机 \(T\)、rank-one adjoint perturbation、矩阵最小特征值和步长；相对步差阈值与PSNR是数值展示，既不证明全部模型/所有数据满足门，也不把非单调 mismatch inclusion自动当成原凸目标的最优性条件。

该应用类是全域单值/Lipschitz前向、固定线性 mismatch 的明确类。本库自然类含真实支撑面/法锥完整纤维和 \(\|y\|^\alpha\) 耦合，C193已严格排除原图的任何合格NFB分解。不能从模型都出现“法锥”“逆问题”推工程身份相同；也不能把这里的排除移到尚未给完整方程的工程/PDE模型。

## 8. 结论强弱、有限长度和逐 Claim 裁定

若已有物理范数 R-linear \(\|x_n-z\|\le Kr^n\)，\(0<r<1\)，则
\[
\sum_{j\ge n}\|x_{j+1}-x_j\|
\le\sum_{j\ge n}K(r^{j+1}+r^j)
=\frac{K(1+r)}{1-r}r^n.
\tag{N13}
\]
所以源3.10(ii)/4.10(ii)/4.17(ii) 已含物理有限长度这个直接推论。仅因作者没有把“finite length”单列成 theorem，不构成本库原创空间。源(i)只得到平方可和步骤；有限维弱=强仍不能自动升级为有限长或R-linear。C09的Dini机制可给非几何点尾及可和步长，这是一种不同条件结果；C10中 \(1<a\le2\) 的 \(k^{1-a}\) 点尾本身不必可和。

| 本库现行身份 | 和 NFB v1 的准确关系 | 本轮结论 |
| --- | --- | --- |
| C02-v2：同图块RL+coverage+真EB+全部尺度兼容+严格留域 | 源不含这条假设蕴含链；但有真实非单调线性全条件重合，并允许PPA子类 | 不被本篇作为一般定理全部覆盖；也不能将所有非单调RLEB实例写成与本篇不交 |
| C09：同图块一般模+Dini+同窗其他门 | 源(i)有限维给点收敛但另一套前件；C10中 \(a>1\) 是完整非幂Dini见证，N4失败 | 本篇不能直接代入这张完整原图；任意一般模类的总体先行性未判 |
| C10：完整log双支图、Dini边界 | 全部 \(a>0\) 违反N4；\(a\le1\)发散不反驳源，因为前件失败 | 原图同空间/标准full-graph product排除已闭 |
| C137：完整cap图、真EB、兼容、非孤立零集几何点尾 | N7排除任何合格分解，source(ii)唯一性另也与零集不同；有限长结果标签无独立区别 | 原图及标准product排除已闭；任意lift、其他对象和全球先行性未闭 |
| C141：完整超线性法向族、局部严格RLEB、共同超几何尾 | N8a排除全部固定参数的任何合格分解 | 原图及标准product排除已闭；完整近端全域存在不扩张其局部收敛范围 |
| C191/C192：完整自然原图、独立法向/切向动力 | 非退化C193排除任何合格分解；C192全域多选择不被条带单值代替 | 保留完整原图/小条带及全选择不同量词；工程模型身份未闭 |
| C193：固定有限二次锚失败 | N4把“仅排除直接C=0代入”强化为**所有合格同空间拆分**，N11再覆盖标准full-graph产品 | 这是本次已证接口强化，不是任意lift不可行定理 |
| C191退化 \(K=\{0\}\)、线性/旋转例 | 投影及表列普通PPA均有真正源覆盖 | 必须承认先例；不把完整自然类的非零门删除 |

## 9. 独立复算、证据等级及精确未闭义务

[nfb_check.py](nfb_check.py) 只用Python标准库；[nfb_results.json](nfb_results.json) 可从仓库根重建：

```bash
python research/comparisons/2026_08_gppa_nfb/nfb_check.py
```

已实际执行，所有断言通过。脚本用精确有理数核 1200 个带非对角SPD度量的 N6 等式及下界；四个线性重合例分别做20步完整PPA/NFB恒等式，其中rotation的 \(\Delta=1/3\) 和非单调 \(-I\) 的 \(\Delta=0.2655881361644759\) 独立重算；15个带可很大dual变量的非对角product压缩等式；以及自然类/cap/超线性/log图局部合法序列的有限数值趋势。源码核验了固定PDF字节指纹。

**一般结论靠 N6、N7、N8、N11 的严格论证。** 有限随机/网格计算只是独立算术及见证检查，不证明“所有分解不存在”，不认证全部步长可行性，不穷尽核或升维，不复现外文随机信号实验。

本次确实关闭：全部同空间合格 \(A+C_{\rm fb}\) 分解的必要锚接口；非退化C191/C192、C137、C141、C10原图排除；标准§4 full-graph primal-dual lift 的压缩排除；以及表列普通PPA的真实重合、物理R-linear到有限长度的直接蕴含。没有找到足以否定本篇 Theorem3.10/4.10相关证明的fatal objection。

仍未关闭的义务应精确保留：

1. 任意其他lift或reformulation，必须逐完整图/零集/残差pairing/固定度量及实际PPA投影轨道核保真；本文只给标准N9–N10的排除。
2. C02-v2/C09一般条件在更早全部文献中的先行性；本篇单篇反包含不证明全球新颖性，且表列交集的结果已经有真实先例。
3. 本库原生应用模型/M1/工程/PDE身份、共同可达输入完整纤维以及源论文条件是否适配这些实际方程；显式数学模型不能代替缺失的原生方程。
4. C02原稿多选择推广、无限维扩展，以及总体RLEB/LT/极大单调大小比较；本文未改变现行candidate/open身份。
5. 若声称任何新算法“覆盖普通PPA”，还须给全部合法初值/选择下的逐步算法等式，或精确说明只覆盖某个初始化、某个branch或某个线性重标子类。仅目标对象符合不完成算法覆盖。

可安全用于摘要的精确说法是：**NFB v1 与本库在真实非单调PPA子类和几何点尾结论上相交；它的全部合格同空间拆分和标准保完整图primal-dual拆分都强迫固定二次零锚界，而本库明确的非退化自然类、cap、超线性族及log完整图局部违反这个界。因此这些原对象/原PPA实例不能由该篇直接推出；任意新lift及全球先行性仍须独立核验。**
