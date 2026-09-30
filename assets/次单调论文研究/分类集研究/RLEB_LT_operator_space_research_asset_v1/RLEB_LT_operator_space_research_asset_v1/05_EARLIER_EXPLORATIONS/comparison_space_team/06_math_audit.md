# 相对算子层比较：敌对数学审计

日期：2026-09-20。审计对象为 `01_exact_translation.md`、`03_holder_lipschitz_category.md`、`04_comparison_space_architecture.md`、`05_meagreness_feasibility.md`，另审根代理随后提交的跨任意步长与 pointwise-AA 两项加强候选。

已完整阅读上述四份报告；独立核对原 RLEB `sections/theorem_spine.tex` 的定义、A1–A4、direct/energy 定理及局部预算；核对修订 `research_note.md` 的完整 proximal 接口；读取 LT2025 正式原文 Definition 2、Propositions 3–4、Assumption 2、Theorem 2，以及 LTT arXiv:1605.05725v2 Definition 2.3、Propositions 2.4、2.6、2.8。此次不重新审查原论文与本比较无关的内容，也不评价检索是否穷尽。

**最终结论：`PASS`（修补后复核）。** 带明示参数余量的核心相对层定理成立；未发现致命数学错误。初审提出的 R1–R4 已在 `03`、`04`、`05` 中全部修补，并由本审计逐项重读关闭：FNE/EB 口径、deadzone 切片闭合、前置正余量与通用尖点见证、乘法排版均通过。跨任意步长的新增排除引理成立，条件与证明见第 7 节；固定步长的 pointwise-AA 排除亦成立，见第 8 节。

## 1. 致命错误

在以下精确范围内没有发现致命错误：有限维状态空间、非单点真仿射解空间、固定共同反射 Hölder 模、法向超线性上界、严格兼容预算，及同一完整 proximal 对象。

这不意味着“全部 RLEB 相比全部 Luke–Tam 的大小”已经证明；现有定理确实只属于一个结构层。

## 2. 可修补漏洞与精确修补（修订后全部关闭）

本节保留初审问题及反例作为审计记录，不表示当前版本仍有这些错误。最终关闭位置：`05` §7.2 的带法向/EB 约束 \(Y_{\rm FNE}\)；`05` §5.2–5.3 的区间函数与全轴 clamp 延拓分离；`03` §5、Y7a 与 `04` §2.1、(2.1a)、§5.2、§11.2 的前置余量及通用尖点见证；`05` (1.3)、(2.3)、(2.6) 的乘法符号。全部已重读复核。

### R1. firmly-nonexpansive 不蕴含 LT2025 的线性误差界

`05` §7.2 的“固定解集上的 firmly-nonexpansive resolvent 母类……LT 是整个空间”若指 LT2025 **收敛证书类**，则不正确。

最小非点解集反例：

\[
F(z,r)=(0,r^3),\qquad S=\mathbb R\times\{0\},\qquad
J_F(z,t)=(z,(I+\mathrm{cube})^{-1}(t)).
\]

这是完整 maximal-monotone 图，其 resolvent firmly nonexpansive；但

\[
d((z,r),S)=|r|,
\qquad r_F(z,r)=|r|^3,
\]

所以任何有限 \(\rho\) 下，\(|r|\le\rho|r|^3\) 都在近零失败。故该对象没有 LT2025 Assumption 2(c) 的线性误差界。

**修补：** 改成“LT all-pairs **几何类**是整个空间”，或在母空间定义中另固定线性 EB 与其共同接口。使用报告 (3.1) 的正常单调模型时 EB 确实成立，但不能把这一特例外推给所有 FNE 映射。

### R2. deadzone 复合的定义域须与 clamp 切片一致

`05` §5 首先规定 \(h\in C([-1,1])\) 后一律 clamp 延拓。若把 §5.2 的 \(h_\epsilon=h\circ s_\epsilon\) 理解为“先全轴 clamp 延拓，再在全轴复合”，新函数一般不再是其 \([-1,1]\) 限制的 clamp 延拓，因此可能离开所声明的函数球切片。

例如 \(h(r)=r\) 于 \([-1,1]\)，\(\epsilon\in(0,1)\)。先延拓再复合在 \(r=1+\epsilon/2\) 给 \(1-\epsilon/2\)，而把新函数在 \([-1,1]\) 的限制再 clamp 延拓给 \(1-\epsilon\)。两者不同。

**修补：** 明确先定义

\[
h_\epsilon(r)=h(s_\epsilon(r))\quad(-1\le r\le1),
\qquad s_\epsilon(r)=\operatorname{sgn}(r)(|r|-\epsilon)_+,
\]

再令

\[
\widehat h_\epsilon(r)=h(s_\epsilon(\operatorname{clamp}_{[-1,1]}r)).
\]

这样 \([h_\epsilon]_\gamma\le H\)、\(h_\epsilon(0)=0\)、\(\|h_\epsilon-h\|_\infty\le H\epsilon^\gamma\) 均保持，局部零平台与所有 LT germ 论证不变。强 little-Hölder 收敛的证明也不变。

### R3. 主定理的非空/尖点余量必须在定理开头出现

`04` 定义层时仅写 \(A>0\) 与 \(\kappa_*<1\)，之后 §5.2 才补 witness 条件；整篇阅读后逻辑可关闭，但不能单独引用早先定义便声称有非空无限维层。

因为 \(T|_S=I\)，在 \(S\) 上选距离恰为 \(R\) 的两点便得必要条件

\[
R\le AR^\gamma,\quad\text{即 }A\ge R^{1-\gamma}.
\]

若 \(A<R^{1-\gamma}\)，即使兼容数值 \(\kappa_*<1\)，层也为空。当前通用尖点证明应明确要求

\[
A>R^{1-\gamma},\qquad
0<c\le\frac{A-R^{1-\gamma}}2.
\]

这比非退化 signed witness 的充分条件更弱，已足以支持核心 Baire 证明。`05` 已在起始参数列出严格余量；最终统一稿应统一写法。

### R4. 公式中的逗号不能代替乘法

`05` 公式 (1.3)、(2.3)、(2.6) 中出现 \(q,m(\cdot)\)、\(c,d(\cdot)^\gamma\)、\(\theta c,t^{\gamma-1}\)。从上下文可知意图是乘法，但这些 TeX 实际表示标点分隔。应改成 \(q\,m(\cdot)\)、\(c\,d(\cdot)^\gamma\)、\(\theta c\,t^{\gamma-1}\)。不影响推导，影响可独立引用的精确性。

## 3. 已独立复核：完整图、空间与证书

以下把 \(S\) 平移为含零的线性子空间，\(1\le\dim S<d\)。设

\[
0<\gamma<1,\quad \nu=1/\gamma,\quad0<q<1,
\quad A>R^{1-\gamma},
\]

\[
\kappa_*=\frac q{(1-q)^\nu}
\left(\frac{R^{1-\gamma}+A}{2}\right)^\nu<1.
\]

令 \(Y\) 由所有连续 \(T:E\to E\) 组成，满足固定 trace、反射模及法向控制：

\[
T|_S=I,
\quad \|2(Tx-Ty)-(x-y)\|\le A\|x-y\|^\gamma\ (\|x-y\|\le R),
\]

\[
d(Tx,S)\le q\min\{d(x,S)^\nu,d(x,S)\}.
\tag{Y}
\]

### 3.1 完整 resolvent 与闭图：通过

对固定 \(\lambda>0\) 定义

\[
F_T(u)=\{(x-u)/\lambda:Tx=u\}.
\]

逐点逻辑是

\[
u\in J_{\lambda F_T}(x)
\iff \exists y:\ Ty=u,\ (x-u)/\lambda=(y-u)/\lambda
\iff Tx=u.
\]

因此 **每个输入有且只有这个完整输出**。不要求 \(T\) 满射；输出点没有原像时 \(F_T(u)=\varnothing\)，这不损害 \(J_{\lambda F_T}\) 的全输入定义。

映射 \((x,u)\mapsto(u,(x-u)/\lambda)\) 是可逆线性同胚，故 \(\operatorname{gph}F_T\) 是闭集。这里正确使用的是完整图的可逆变换；若只说连续像保持闭集，论证将是错的，但四份报告并未犯此错。

由法向收缩，\(Tx=x\) 蕴含 \(d(x,S)\le qd(x,S)\)，所以

\[
\operatorname{zer}F_T=\operatorname{Fix}T=S.
\]

### 3.2 真 min-residual EB：通过，方向无误

记 \(a=d(x,S)\)。对所有输入有

\[
\|x-Tx\|\ge a-d(Tx,S)\ge(1-q)a,
\]

\[
d(Tx,S)\le qa^\nu
\le\frac q{(1-q)^\nu}\|x-Tx\|^\nu.
\]

因此同一

\[
\psi(t)=q\left(\frac{\lambda t}{1-q}\right)^\nu
\]

对输出 \(u\in\operatorname{ran}T\) 的 **每个** 原像成立。对非空纤维取下确界得

\[
d(u,S)\le\psi(r_{F_T}(u)),\qquad
r_{F_T}(u)=\lambda^{-1}\inf_{Tx=u}\|x-u\|.
\]

方向正确：左端是同一输出距离，右端的全部值均在其上方，故其下确界仍在其上方。\(\psi\) 连续，亦可选逼近最小残差序列。有限维中非空纤维闭，范数 coercive，最小值取得。不存在把 selected residual 当最小残差的漏洞。

另外，\(Y\) 其实还共同满足线性 EB

\[
d(u,S)\le \frac{\lambda q}{1-q}\,r_{F_T}(u),
\]

因为先用 \(d(Tx,S)\le qa\)。非线性 EB 主要用于 strict direct-RLEB 匹配，而不是因层内完全缺线性 EB。

### 3.3 RL、兼容、覆盖与共同初值域：通过

任意两个图点对应输入 \(x=u+\lambda u^*\)、\(y=v+\lambda v^*\)。写 \(a=u-v,b=u^*-v^*\)，则

\[
a+\lambda b=x-y,\qquad a-\lambda b=R_Tx-R_Ty,
\]

\[
4\lambda\langle a,b\rangle
=\|a+\lambda b\|^2-\|a-\lambda b\|^2.
\]

故 (Y) 的反射约束与原 RL 精确等价，涵盖整个图的跨分支量词。取最近点 \(s=P_Sx\)，\(r=d(x,S)\le R\)，有

\[
\|Tx-x\|\le\frac{r+Ar^\gamma}{2},
\]

\[
\frac1r\psi\left(\frac{r+Ar^\gamma}{2\lambda}\right)
=\frac q{(1-q)^\nu}
\left(\frac{r^{1-\gamma}+A}{2}\right)^\nu
\le\kappa_*<1.
\]

\(\gamma\nu=1\) 已正确使用，步长抵消正确。原稿的 finite \(\bar t\) 可取任意不小于 \((R+AR^\gamma)/(2\lambda)\) 的数，并将此全局 \(\psi\) 限制到该区间。

取原稿 \(U=E\)、\(\mathcal G=\operatorname{gph}F_T\)，coverage 全局，解图点齐全，域边界距离为 \(+\infty\)，原局部预算自动通过。对共同管域 \(d(x,S)\le\rho\le R\)，实际法向因子给

\[
d(T^kx,S)\le q^k\rho,
\]

\[
\|T^kx-\Pi_Tx\|\le
\frac{\rho q^k}{2(1-q)}+
\frac{A\rho^\gamma q^{\gamma k}}{2(1-q^\gamma)}.
\]

该共同管域虽因切向无界而非紧，尾界仍只依赖法向上界，完全合法；若初值限定于紧集，求和长度再给统一有界轨道区。实际 \(q\) 与证书 \(\kappa_*\) 未被混用。

### 3.4 非空、无限维、闭凸紧 Polish：通过（须有 R3 余量）

\(P_S\in Y\)，因为其反射 \(2P_S-I\) 是等距映射。正余量还允许

\[
T_*(x)=P_Sx+c\,d(x,S)^\gamma e,
\qquad e\in S,\ \|e\|=1,
\]

其中 \(2c+R^{1-\gamma}\le A\)。它的像在 \(S\)，故法向条件自动成立；距离函数 1-Lipschitz 与幂函数的 Hölder 性给反射约束。

固定一个法向坐标，允许任意锚定 \(\gamma\)-Hölder 函数球中的小切向函数，即嵌入无限维函数球。这里“无限维”是函数空间维数，不是要求状态空间无限维。

三条 (Y) 对局部一致极限闭合。凸性关键是 \(S\) 仿射，从而 \(d(\cdot,S)\) 凸；若随意换为非凸零集，该证明失效。

共同模为 \(h(t)=(t+At^\gamma)/2\) 于 \(0\le t\le R\)。由 \(T0=0\)，对闭球 \(\overline B_j\) 把 \([0,x]\) 分成固定 \(N_j\) 段，\(j/N_j\le R\)，得到

\[
\sup_{T\in Y,\ \|x\|\le j}\|Tx\|\le N_jh(j/N_j).
\]

有限维闭球紧，共同值界与等度连续给每球 Arzelà–Ascoli，逐球对角抽取给局部一致收敛子列，闭性保留 (Y)。故 \(Y\) 在 compact-open 度量下紧、Polish、Baire。未把全值域误认为有界，也未把该论证未经条件延伸到无限维 Hilbert 状态空间。

## 4. 已独立复核：LT 比较与 Baire 证明

### 4.1 几何翻译与 direct/energy 区别：通过

LT2025 Definition 2 在相同步长的 scaled 图上给

\[
\lambda\langle a,b\rangle\ge-\tau\|a+\lambda b\|^2.
\]

反射常数正是 \(\sqrt{1+4\tau}\)，故完整输入上的

\[
\operatorname{Lip}T\le\frac{1+\sqrt{1+4\tau}}2.
\]

这只是一向包含所需条件，不等于所有 Lipschitz 映射都具有 LT 收敛证书。`01` 保留 maximality、EB、局部完整性与阈值的做法正确。

原 energy 线性证书为

\[
\kappa_E^2=(1+2\tau)\frac{\rho^2}{\rho^2+\lambda^2},
\quad 2\tau\rho^2<\lambda^2.
\]

LT 阈值 \(2\tau(\lambda+\rho)^2<\lambda^2\) 确实更强。`01` 的差值公式 (3.11) 正确。不能据此跳过局部 graph/coverage 的共同接口，但报告明确保留了该前提。

direct 不包含 LT 的线性模型 \(T(z,r)=(z,2r/3)\) 有效：切向恒等强制 \(L\ge1\)，最小线性 EB 常数为 \(2\lambda\)，故 direct 比值至少为 \(2\)，而 energy 有效。

### 4.2 Lipschitz germ 第一纲：通过

固定 \(s\in S\)，\(B_j=\overline B_{r_j}(s)\)，\(r_j\downarrow0\)。

\[
L_{m,j}=\{T\in Y:\|Tx-Ty\|\le m\|x-y\|\ \forall x,y\in B_j\}
\]

逐点评价连续，故每层闭。任取 \(T\in L_{m,j}\)，凸组合 \(T_\theta=(1-\theta)T+\theta T_*\) 在 \(Y\) 且趋向 \(T\)。沿法向单位向量 \(n\)，

\[
\frac{\|T_\theta(s+tn)-T_\theta(s)\|}{t}
\ge\theta c t^{\gamma-1}-(1-\theta)m\to\infty.
\]

所以闭层无内点，\(\bigcup_{m,j}L_{m,j}\) 第一纲。原 Lipschitz 项只有 \(O(t)\)，确实不能抵消非零 \(t^\gamma\) 尖点。

用 \(m t^\beta\)、\(\beta>\gamma\) 代替 \(mt\) 亦成立；对一列 \(\beta_n\downarrow\gamma\) 和可数半径/常数取并，排除任意更高 Hölder 阶。每个成员本来有 \(\gamma\) 阶局部上界，故 sharp-exponent 说法准确。

### 4.3 一般固定 direct 证书层不凸：反例通过

`03` 的 \(T_\pm(p,r)=(p\pm\sqrt{|r|},|r|/4)\)、\(\psi(t)=t^2/4\) 具有完整闭图和真 EB；平均 \(T_0(p,r)=(p,|r|/4)\) 在正小 \(r\) 的 EB 将要求

\[
\frac r4\le\frac14\left(\frac{3r}4\right)^2,
\]

失败。反射界 \(2\sqrt\delta+\tfrac32\delta\) 与示例兼容数值 \(0.31640625\) 均正确。因此不能把当前凸层方法直接移植为全部 direct-RLEB 的分类。

## 5. 已独立复核：拓扑、二值与 signed 切片

### 5.1 strong/little Hölder 结论：通过

局部 \(C^{0,\gamma}\) 半范数族组成完整 Fréchet 拓扑；\(Y\) 在其中闭且凸，不再以紧性为依据。令

\[
a_s(T)=\lim_{r\downarrow0}[T]_{\gamma;\overline B_r(s)}.
\]

该极限由单调性存在，且对于固定较大球有

\[
|a_s(T)-a_s(U)|\le[T-U]_{\gamma;\overline B_r(s)}.
\]

故 \(Z_s=\{a_s=0\}\) 强闭。局部 Lipschitz germ 在其内；sharp witness 凸混合满足 \(a_s(T_\theta)\ge\theta c\)，所以 \(Z_s\) 无内点，LT/Lipschitz germ 为 nowhere dense 子集。

little-Hölder 子空间中这个闭容器等于整个子空间，不能再据此推出 nowhere dense。取 \(\gamma<\eta<1\) 的 \(d(x,S)^\eta\) witness，并保证 \(2c_\eta R^{\eta-\gamma}+R^{1-\gamma}\le A\)，可重新证明第一纲。报告正确区别了两者。

### 5.2 至多二值子类为 \(G_\delta\)：通过，但不自动继承范畴结论

对每个有界球与三点最小间距，考察紧元组集

\[
K_{j,m}=\{(x_1,x_2,x_3)\in\overline B_j^3:\min_{a\ne b}\|x_a-x_b\|\ge1/m\}.
\]

“不存在三点同像”等价于在每个非空 \(K_{j,m}\) 上，连续函数
\(\max_{a,b}\|Tx_a-Tx_b\|\) 的最小值严格为正。这给开条件可数交。因此 \(Y_{\le2}\) Polish；但 inherited compact-open 距离未必完备，且大空间第一纲不可任意下推。这些边界在报告中保留正确。

### 5.3 abs 二值函数球：完整核验通过

以 \(\lambda=1\) 记

\[
g_-(r)=q\min\{|r|^\nu,|r|\},\quad
T_h^-(z,r)=(z+h(r),g_-(r)).
\]

\(y>0\) 的两个全部原像为 \(r=\pm a(y)\)、\(z=u-h(\pm a(y))\)，其中

\[
a(y)=(y/q)^{1/\nu}\ (0<y\le q),\qquad a(y)=y/q\ (y\ge q).
\]

故图值确为

\[
(-h(a),a-y),\quad(-h(-a),-a-y).
\]

二者法向差 \(2a>0\)，故恰二值；\(y=0\) 唯一零值；\(y<0\) 空。cap 点 \(y=q\) 两公式一致。真残差的两个分支都至少为 \((1-q)a(y)\)，没有选支漏洞。

函数球一致拓扑与此映射切片的 compact-open 拓扑互为连续：反向只需读取 \((0,r)\) 的第一坐标。切片不是全部二值算子的空间，报告对此限定正确。

### 5.4 signed 切片与实际 LT germ 稠密性：通过（采用 R2 修补）

令

\[
g(r)=q\operatorname{sgn}(r)\min\{|r|^\nu,|r|\},\qquad q\nu\le1.
\]

它连续、严格增、满射、1-Lipschitz；\(T_h^+(z,r)=(z+h(r),g(r))\) 是完整同胚，故 \(F_h\) 单值闭图。

R2 修补后的 deadzone \(h_\epsilon\) 在 \(|r|<\epsilon\) 为零。在输出带
\(U=\mathbb R\times(-g(\epsilon),g(\epsilon))\) 上，

\[
F_{h_\epsilon}(u,y)=(0,g^{-1}(y)-y).
\]

一维函数 \(g^{-1}-I\) 连续且单调。若在 \(U\) 增加一个与现有全部图点单调相关的值，用 \(v+td\in U\) 并令 \(t\to0^\pm\)，得到新值等于旧值，故所需局部 maximality 真实成立。\((I+F)(U)=\mathbb R\times(-\epsilon,\epsilon)\)，覆盖也精确成立；全局线性 EB 可用第 3.2 节的常数，\(\tau=0\)。因此此处是实际 LT2025 germ，而非仅 Lipschitz 上界类。

一致逼近 \(\|h_\epsilon-h\|_\infty\le H\epsilon^\gamma\) 证明稠密。little 情形的小尺度增量由 \(2\omega_h(\delta)\) 控制，大尺度由 \(2\|h_\epsilon-h\|_\infty/\delta^\gamma\) 控制，强收敛证明正确。邻域随 \(\epsilon\) 缩小，故不能升级为固定共同域的 LT 证书稠密性。

## 6. 已独立复核：signed 切片的任意步长公式

此项为审计中追加候选。固定 \(T=J_{\lambda_0F}(z,r)=(z+h(r),g(r))\)，\(c=\mu/\lambda_0>0\)，令

\[
H_c(r)=cr+(1-c)g(r).
\]

对 \(r>t\)，\(0\le g(r)-g(t)\le r-t\)，因而无论 \(c\le1\) 或 \(c>1\)，都有

\[
\min\{c,1\}(r-t)\le H_c(r)-H_c(t)
\le\max\{c,1\}(r-t).
\tag{6.1}
\]

特别在容易误判的 \(c>1\) 情况，正确下界是
\(c\Delta r-(c-1)\Delta g\ge\Delta r\)。故 \(H_c\) 全局双 Lipschitz、严格增且满射。

直接解全部 inclusion 得

\[
J_{\mu F}(p,s)=
\bigl(p+c\,h(H_c^{-1}(s)),\ g(H_c^{-1}(s))\bigr).
\tag{6.2}
\]

\(h\) 在 0 的某邻域 Lipschitz，当且仅当 (6.2) 在某个完整解点邻域 Lipschitz。逆向取切向输入为常数并与双 Lipschitz 的 \(H_c\) 复合即可。因此 signed 切片的非-Lipschitz germ 类同时排除所有 \(\mu>0\)，不是对不可数多个第一纲集直接取并。条件 \(q\nu\le1\) 不可从此证明中无说明删除。

## 7. 已独立复核：全 \(Y\) 的跨任意步长排除引理

此加强候选成立，而且不必假设 \(J_{\mu F}\) 在全局满域或单值。所需的是该 \(\mu\) 的 **局部完整图 all-pairs 几何**，或下面明确的相对近邻零集几何。

固定 \(s\in S\)，\(T=J_{\lambda F_T}\in Y\)。设存在某 \(\mu>0\)，使 \(\mu F_T\) 在 \((s,0)\) 的邻域图块满足有限 violation 的 all-pairs submonotonicity。置 \(c=\mu/\lambda\)。对 \(x\to s\)，令

\[
u=Tx,\qquad z=cx+(1-c)u,\qquad w=P_Sz.
\]

因为 \((x-u)/\lambda\in F_T(u)\)，有

\[
(z-u)/\mu=(x-u)/\lambda\in F_T(u).
\]

又 \(T(s)=s\) 且 \(T\) 连续，所以 \(u,z,w\to s\)、\(z-u\to0\)。对足够近的 \(x\)，两个图点 \((u,z-u)\)、\((w,0)\) 必落在假设的 \(U\times W\) 图块内。只用这两个图点便得到

\[
\|u-w\|\le M\|z-w\|=M d(z,S),
\quad M=\frac{1+\sqrt{1+4\tau}}2.
\tag{7.1}
\]

记 \(a=d(x,S)\)。由于 \(d(u,S)\le qa\)，

\[
d(z,S)\le(c+|1-c|q)a.
\tag{7.2}
\]

线性正交投影的关键恒等式为

\[
P_S(u-w)=P_Su-P_Sz=cP_S(u-x).
\tag{7.3}
\]

法向位移另有

\[
\|P_{S^\perp}(u-x)\|\le(1+q)a.
\tag{7.4}
\]

合并 (7.1)–(7.4) 得

\[
\boxed{
\|Tx-x\|\le
\left[\frac{M(c+|1-c|q)}c+1+q\right]d(x,S)
\quad(x\text{ 足够近 }s).
}
\tag{7.5}
\]

架构组随后增补的更短能量证明也已逐式独立核验：令 \(a_\mu=c(x-u)\)，则

\[
\|u-w\|^2+\|a_\mu\|^2
=\|z-w\|^2-2\langle u-w,a_\mu\rangle
\le(1+2\tau)d(z,S)^2.
\]

直接舍掉第一项，得到比 (7.5) 更紧且无需切/法向位移拼接的界

\[
\boxed{\|Tx-x\|\le
\sqrt{1+2\tau}\frac{c+|1-c|q}{c}\,d(x,S).}
\tag{7.6}
\]

`04` 新增 §11.1–11.4 的局部量词、(11.3) 能量式、(11.4) 法向估计及可数位移层证明均通过。最终稿宜采用 (7.6)。

所有常数可依赖 \(T,\mu\) 与局部证书；这不妨碍用可数半径与整数上界编码。定义

\[
C_{m,j}=\{T\in Y:\|Tx-x\|\le m d(x,S)\ \forall x\in\overline B_{r_j}(s)\}.
\]

每层局部一致闭。若 \(T\in C_{m,j}\)，与第 3.4 节 witness 作凸混合，在 \(x=s+tn\) 有

\[
\frac{\|T_\theta x-x\|}{d(x,S)}
\ge\theta c_0t^{\gamma-1}-(1-\theta)m\to\infty.
\]

故每层无内点，\(C_s=\bigcup_{m,j}C_{m,j}\) 第一纲。**凡存在任意 \(\mu>0\) 的上述局部 all-pairs 图证书者，全都被包含在同一个 \(C_s\) 内。** 因而可以合法升级为“同一原算子任意步长的局部 LT all-pairs 证书类在 \(Y\) 中第一纲”。这一步没有使用错误的不可数并规则。

边界必须保留：若所谓 LT 证书只测试经过人为删减的非完整图块、或只测试不含这些近邻图点的轨道子集合，(7.1) 不必可用。本引理排除的是原算子在 \((s,0)\) 的真实局部图条件，不是任意换对象或删枝后的算法。

## 8. 已独立复核：pointwise-AA 的可证明扩展与边界

LTT v2 Proposition 2.4(iii), equation (19)，在 \(s\in\operatorname{Fix}T\) 处给

\[
\|Tx-s\|^2+\frac{1-\alpha}{\alpha}\|x-Tx\|^2
\le(1+\varepsilon)\|x-s\|^2.
\tag{8.1}
\]

这里 \(0<\alpha<1\)，残差项非负；Proposition 2.6 保证参考点 \(T(s)=\{s\}\)。舍掉非负项合法，因此 pointwise-AA 在固定参考解点确实蕴含 Lipschitz calmness

\[
\|Tx-s\|\le\sqrt{1+\varepsilon}\|x-s\|.
\tag{8.2}
\]

固定步长下，定义闭层

\[
A_{m,j}=\{T\in Y:\|Tx-s\|\le m\|x-s\|\ \forall x\in\overline B_{r_j}(s)\}.
\]

同一个法向尖点凸混合使比值发散，故 \(\bigcup_{m,j}A_{m,j}\) 第一纲。于是主层内的相对结论可以超出 all-pairs：**固定步长、固定参考解点、完整邻域输入的 pointwise-AA 类也第一纲。** 这不是把 calmness 当成两点 Lipschitz，而是为 calmness 另设了闭层并独立证明。

跨任意步长则须再分清量词：

- 若 \(J_{\mu F}\) 的 pointwise-AA 以共同有限常数对近邻的 **每个** \(w\in S\) 成立，且输入区包含完整邻域，则可取第 7 节的 \(w=P_Sz\)，(8.2) 代替 (7.1)，跨步长第一纲结论仍成立。
- 若只知道 \(J_{\mu F}\) 在一个固定 \(s\) 处的 calmness，不能据此把 (7.1) 的变动 \(w=P_Sz\) 换成 \(s\)，也不能未经证明转回 \(J_{\lambda F}\) 的 calmness。
- 若原 theorem 的 relative 域是低维 \(\Lambda\)、环域或某个只包含特殊轨道的集合，而不包含法向测试线，则上述完整邻域范畴排除不适用。允许尺度依赖且无共同有限上界的 violations 也需另审。

所以可扩大相对排除范围，但仍不应写成“整个 Luke–Thao–Tam 所有体系均第一纲”。

## 9. 过度主张与仍未解决

### 需要禁止的过度主张

1. 从 \(Y\) 的相对结论推出全体 RLEB 的内在/绝对 category 大小。
2. 把 LT几何类、LT2025 收敛证书类与全体 LTT pointwise/relative 理论混称一个集合。
3. 把第一纲等同零测、低概率、百分比少；或把 residual 等同实际应用丰富。
4. 把 signed germ 的稠密性改成固定共同域、共同 LT 预算的稠密性。
5. 将大空间的 residual 结论限制到全部有限纤维、半代数或任意子空间而不重证。
6. 由当前 Baire 证明本身宣布优先权或高论文等级。其 category 核心是标准凸性机制；新价值必须来自结构层与真实接口的内容。

### 仍未解决的数学问题

- 去掉法向超线性上界后的更大 RLEB 层；其真 EB 证书集合一般不凸。
- 合并全部指数、gauge、局部化与余量后，算子对象本身的自然 Baire 模型；证书标签不交并不能替代这一问题。
- 整个 \(Y_{\le2}\) 中的 LT 大小，而非固定 normal 函数球切片。
- 固定输入域、固定 LT 参数预算下的稠密性与内部结构。
- 任意非凸解集和无限维 Hilbert 状态空间版本。
- 本审计未完成 theorem-level 优先权排除；文献检索与自然性/创新价值应由相应审稿线评定。

## 10. 最终审稿判定

**`PASS`：核心相对层定理及列明加强通过。** R1–R4 已全部落实并逐项关闭。`03` Y7a、`04` (2.1a) 的通用见证现适用于全部允许参数，后续空内点证明不再隐含依赖 signed 构造的额外预算。全 \(Y\) 的跨任意步长排除和固定步长 pointwise-AA 排除均经本审计独立验证，但须保留第 7–8 节的完整图、完整邻域与相对零集量词。

本判定只说明上述精确数学陈述成立；不把“已有一个可证的结构层”升级为“已经完成全 RLEB 与全 Luke–Tam 的总覆盖量评判”。
