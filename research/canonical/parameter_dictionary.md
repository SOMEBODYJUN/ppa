# RL 参数与正则性字典：对象固定后的可用推理

版本 PD-v1，2026-10-01。本页从 9/01 两个 checkpoint 重新推导，供新增定理、例子、代码调用。
状态为本页明确给出的代数证明和反例已重算；文献命名及先行性未本轮外审。
符号约定与 [foundations](../foundations.md) 一致，但所有关键量词在此重新写明。

<a id="pd-quantifiers"></a>
## PD-QUANTIFIERS · 什么对象满足什么条件

固定实 Hilbert 空间 \(H\)、关系 \(F:H\rightrightarrows H\)、图块 \(\Gamma\subset\operatorname{gph}F\)、\(\lambda>0\)。
对任意 \((u,v),(u',v')\in\Gamma\)，写 \(a=u-u'\)、\(b=v-v'\)。全对 RL 的含义是

\[
\forall (u,v),(u',v')\in\Gamma:\quad
\|a-\lambda b\|\le\omega(\|a+\lambda b\|),
\]

其中 \(\omega:[0,\infty)\to[0,\infty)\) 有限、非减、\(\omega(0)=0\)、原点连续。
幂模为 \(\omega(t)=Lt^\gamma\)，\(L\ge0\)、\(0<\gamma\le1\)。
每张命题卡必须记录以下四个独立坐标：

| 坐标 | 允许值及精确定义 |
|---|---|
| 图量词 | 完整图 \(\Gamma=\operatorname{gph}F\)，或指定图块；图局部通常指 \(\operatorname{gph}F\cap(U\times W)\) |
| 配对量词 | 全对；或 moving 图点与指定 \(S_0\subset F^{-1}(0)\) 的零点锚 \((p,0)\) 配对 |
| 尺度量词 | 全部输入对距离；或只对 \(\|a+\lambda b\|\le R\) 的配对 |
| 输入域 | 自然域 \(D_\lambda(\Gamma)=\{u+\lambda v:(u,v)\in\Gamma\}\)，另列实际覆盖集合 \(E\subset D_\lambda(\Gamma)\) |

“全图”不等于“全输入域”：令 \(F(u)=\{0\}\) 对 \(u\in(0,1)\)，其余为空，则完整图满足 \(\mathrm{RL}(\lambda,1,1)\)，而自然域只有 \((0,1)\)。
空图的全称 RL 真空成立，但不给任何步的存在性。

### 全对、锚定与单值性的严格方向

全对 RL 且 \((p,0)\in\Gamma\) 给相应锚定不等式；若锚未包含在同一图块，不能这样推。
全对 RL 使 \(M_\lambda(u,v)=u+\lambda v\) 在图块上单射：同输入使 Cayley 差为零，求和求差还原图点。
锚定条件没有这个结论：取 \(H=\mathbb R,\lambda=1\)，
\(\Gamma=\{(0,0),(1,0),(0,1)\}\)、\(S_0=\{0\}\)。
相对锚 0 的 \(L=1,\gamma=1\) 条件逐点成立，但输入 1 有输出 1 和 0。
此例只否定所声明的固定锚量词，未声称对完整零集所有锚成立。

限定输入域 \(E\) 上识别完整 resolvent 需要两个条件的合取：
(1) 图块 coverage：每个 \(x\in E\) 有图块 realization；
(2) exclusion：完整图中每个具有 \(M_\lambda(u,v)\in E\) 的点都落入图块。
在此基础上全对 RL 才给完整单值 \(J_{\lambda F}|_E\)。迭代留域仍是第三个独立条件。
来源定位：S1 Definition 0.1–0.5、Theorem 1.1、Proposition 1.4。

<a id="pd-cayley"></a>
## PD-CAYLEY · 精确代数与能量式

在全对 RL 下令 \(x=u+\lambda v\)、\(C(x)=u-\lambda v\)，则

\[
u=\frac{x+C(x)}2,\quad v=\frac{x-C(x)}{2\lambda},\quad J_\Gamma=\frac{I+C}{2}.
\]

由展开和平行四边形恒等式，以下与同图块 RL 精确等价：

\[
\lambda\langle a,b\rangle\ge\frac{t^2-\omega(t)^2}{4},\qquad
\|a\|^2+\lambda^2\|b\|^2\le\frac{t^2+\omega(t)^2}{2},\quad t=\|a+\lambda b\|.
\]

反向任意映射 \(C:D\to H\) 按上式生成图，其 RL 恰等于 \(C\) 的同模连续性。
所以必须另证原图误差界、coverage 和算法条件；它们不会从“Cayley 模”这一改写中出现。
\(L=0\) 时 \(C\) 常值（非空图），指数不可识别。来源定位：S1 Theorem 1.1、Proposition 1.3。

<a id="pd-tied"></a>
## PD-TIED · \(\gamma=1\) 的精确 tied 参数曲线

固定同一图块与步长，定义

\[
\theta=\frac{1-L^2}{2(1+L^2)},\quad \mu=\frac\theta\lambda,\quad \rho=\lambda\theta.
\]

平方 RL 后整理得等价式

\[
\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2,
\qquad \rho=\lambda^2\mu.
\]

**推导。** 展开两边给
\((1-L^2)(\|a\|^2+\lambda^2\|b\|^2)\le2\lambda(1+L^2)\langle a,b\rangle\)，除以正分母即可。
反向同样展开。有限 \(L\ge0\) 对应 \(-1/2<\theta\le1/2\)，
\(L=\sqrt{(1-2\theta)/(1+2\theta)}\)。上端 \(\theta=1/2\) 对应 \(L=0\)，不得从字典删除。

| 参数 | 严格可用含义 |
|---|---|
| \(L=1\) | 同配对量词下的单调性 |
| \(0\le L<1\) | tied 的两个系数均正；分别给强单调、余强制，但合取精确式更强 |
| \(L>1\) | 两系数均负；不能把负 \(\rho\|b\|^2\) 删除而声称 hypomonotonicity |

若 \(L\ge1\)，另有精确式
\(\lambda\langle a,b\rangle\ge-\tau\|a+\lambda b\|^2\)，\(\tau=(L^2-1)/4\)。
能量式中标准非负 violation 为 \(\varepsilon=(L^2-1)/2\)。
\(L<1\) 时可使用 signed 系数计算，但不能冒称满足采用非负 violation 参数的同一命名定义。
这里仅证明代数对应；完整二参数 \((\mu,\rho)\) 类不等于这条固定 \(\lambda\) 曲线。
来源定位：S1 Theorem 2.1(a)；S2 `work/a_rl_position.md` §2。

<a id="pd-step"></a>
## PD-STEP · 同一个图换步长

固定图块 \(\Gamma\) 在 \(\lambda\) 下的 Cayley 映射 \(C:D\to H\)。令新步长 \(\eta>0\)，
\(t=\eta/\lambda\)、\(\alpha=(1+t)/2>0\)、\(\beta=(1-t)/2\)。
对相同图点求坐标得

\[
x_\eta=\alpha x+\beta C(x)=:Q(x),\qquad
r_\eta=\beta x+\alpha C(x).
\]

因此新自然域精确为 \(Q(D)\)。存在新 Cayley **映射**当且仅当 \(Q\) 单射；单射时

\[
C_\eta=(\beta I+\alpha C)\circ Q^{-1}.
\]

**必要性细节。** 若 \(Q(x)=Q(y)\) 且新反射相同，矩阵
\(\begin{pmatrix}\alpha&\beta\\\beta&\alpha\end{pmatrix}\) 的行列式为 \(t>0\)，强迫 \(x=y\)。
故不同旧输入折叠为同新输入必然造成新反射多值，任何原点为零的模都失败。

若旧 \(C\) 为 \(L\)-Lipschitz，且 \(m=\alpha-|\beta|L>0\)，则

\[
\|Q(x)-Q(y)\|\ge m\|x-y\|,\qquad
\operatorname{Lip}(C_\eta)\le\frac{|\beta|+\alpha L}{\alpha-|\beta|L}.
\]

这是充分界，未宣称一般最优。即使 \(D=H\)，单靠图块的上述下界尚未在此证明 \(Q(D)=H\)；coverage 应保留为单独义务。
旧模若为 \(L s^\gamma\)、\(\gamma<1\)，只能直接得到
\(\|\Delta Q\|\ge\alpha s-|\beta|Ls^\gamma\)，它在小尺度可能为负，不提供局部单射。

### 显式换步反例：Hölder 常数不能原样搬运

取 \(C(s)=\operatorname{sgn}(s)|s|^\gamma\)、\(D=\mathbb R\)、\(0<\gamma<1\)，用 PD-CAYLEY 在步长 \(\lambda\) 生成完整图。
若 \(\eta>\lambda\)，则 \(\beta<0\)，正数
\(s_0=(|\beta|/\alpha)^{1/(1-\gamma)}\) 满足 \(Q(s_0)=Q(0)=0\)，图在新步长不满足任何全对消失模 RL。
若 \(0<\eta<\lambda\)，则 \(\alpha,\beta>0\)，\(Q\) 严格递增且满射。
对 \(s>s'\)，令 \(A=s-s'>0,B=C(s)-C(s')>0\)，新反射斜率为
\((\beta A+\alpha B)/(\alpha A+\beta B)\le\alpha/\beta\)。
在零附近取 \(s'=0,s\downarrow0\)，比值趋于 \(\alpha/\beta\)，故该 Lipschitz 常数锐。
然而无穷远新反射与输入之比趋于 \(\beta/\alpha>0\)，所以任何全局 \(\gamma'<1\) 证书都失败。
原步长的全局 Hölder 指数因此可随换步变成 Lipschitz 或完全失效。
来源定位：S2 `research/gap_examples.md` GX-015、`work/b_scalar_nonlinear.md` EX-11；本节统一坐标公式及界为本轮独立推导。

### 逆关系、输出缩放不是“同图换步”

对 \(\Gamma^{-1}=\{(v,u):(u,v)\in\Gamma\}\)，两侧范数各提出 \(1/\lambda\) 得

\[
\Gamma\in\mathrm{RL}(\lambda,\gamma,L)
\iff\Gamma^{-1}\in\mathrm{RL}(\lambda^{-1},\gamma,L\lambda^{\gamma-1}).
\]

对 \(c>0\)，\(c\Gamma=\{(u,cv):(u,v)\in\Gamma\}\)，则
\(\Gamma\in\mathrm{RL}(\lambda,\gamma,L)\iff c\Gamma\in\mathrm{RL}(\lambda/c,\gamma,L)\)，因为乘积 \((\lambda/c)(cv)\) 不变。
这两条改变了关系本身，不能充当同图换步不变性的证明。来源定位：S1 Theorem 2.1(b,c)。

<a id="pd-scale"></a>
## PD-SCALE · 有界与无界尺度的方向

若旧自然域直径至多 \(0<\Delta<\infty\)，且 \(0<\gamma_1\le\gamma_2\le1\)，则

\[
L_2s^{\gamma_2}\le L_2\Delta^{\gamma_2-\gamma_1}s^{\gamma_1}
\quad(0\le s\le\Delta).
\]

因此较大指数证书可降为较小指数，常数按上式改变。单点域单独真空处理。
无界域无该统一方向：\(C(s)=s\) 全局 Lipschitz，但 \(|s|/|s|^\gamma\to\infty\)；
\(P_\gamma(s)=\operatorname{sgn}(s)|s|^\gamma\) 全局 \(\gamma\)-Hölder，零附近不满足任何更大指数。
其全局常数 \(2^{1-\gamma}\) 可直接核验：同号由凹幂的次可加性，异号由
\(a^\gamma+b^\gamma\le2^{1-\gamma}(a+b)^\gamma\)；相反数取等号。
任何更小指数又在无穷远失败。按 PD-CAYLEY 拉回，这些都是原图反例。

若额外有 \(\operatorname{Lip}(C)\le K\) 且 \(\operatorname{diam}C(D)\le M\)，其中 \(K,M>0\)，则
\(\|\Delta C\|\le\min\{Ks,M\}\le K^\gamma M^{1-\gamma}s^\gamma\)。
这种“有界值域＋Lipschitz”继承证书不说明 \(\gamma<1\) 是最佳指数。
若配对距离还下界为 \(\delta>0\)，幂模可在该远离对角线的配对集上给线性上界 \(L\delta^{\gamma-1}s\)；这不是完整邻域 Lipschitz 性。
来源定位：S2 `work/a_rl_position.md` §3。

<a id="pd-residual"></a>
## PD-RESIDUAL · 真残差、选中值和窗口

固定非空零集 \(S=F^{-1}(0)\)，令 \(r_F(u)=\inf_{v\in F(u)}\|v\|\)，空纤维取 \(+\infty\)。
对一次合法步 \(x=u+\lambda v\)，只得到
\(r_F(u)\le\|v\|=\|x-u\|/\lambda\)。
若已有真残差 EB \(d(u,S)\le\psi(r_F(u))\) 且 \(\psi\) 非减，才能向上替换成选中值；反向不成立。
例：\(F(u)=\{u,u^2\}\) 在 \(\mathbb R\) 上，零集为 \(\{0\}\)。选中 \(v=u\) 时 \(|u|\le|v|\)，但小 \(|u|\) 时 \(r_F(u)=u^2\)，不存在局部线性 EB。

若对每个 \(v\in F(u)\) 都有 \(d(u,S)\le\kappa\|v\|^q\)，\(q>0\)，取趋于 infimum 的序列并用连续性才得真残差幂 EB；不要求最小范数值取得。
任意非减 gauge 在正残差点可能有右跳，不能未经右连续性就把“对每个值”改为“在 infimum 取值”。

本页采用残差窗口版 EB：固定 \(\bar u\in S\)，存在输入邻域 \(U\ni\bar u\)、\(\delta>0\)，对 \(u\in U\) 且 \(r_F(u)<\delta\) 有界。
正幂 \(\kappa r^q\) 可缩至 \(U\cap B(\bar u,\kappa\delta^q)\) 得邻域版，因为窗口外
\(d(u,S)\le\|u-\bar u\|<\kappa\delta^q\le\kappa r_F(u)^q\)。
一般仅局部定义的 gauge 不作这个无条件等同。来源定位：S1 Definition 0.4、Lemma 4.1。

<a id="pd-regularity"></a>
## PD-REGULARITY · MR/MSR 的方向和强版本

本节允许一般有限维欧氏空间间的关系 \(F:X\rightrightarrows Y\)，以免把正则性定义误限为同空间算子。固定 \((\bar u,\bar v)\in\operatorname{gph}F\)，普通线性定义为：

| 身份 | 完整量词 |
|---|---|
| MR | 存在 \(\kappa,U,W\)，对每个 \(u\in U,v\in W\)，\(d(u,F^{-1}(v))\le\kappa d(v,F(u))\) |
| MSR | 存在 \(\kappa,U\)，对每个 \(u\in U\)，\(d(u,F^{-1}(\bar v))\le\kappa d(\bar v,F(u))\) |
| strong MSR | 存在 \(\kappa,U\)，对每个 \(u\in U\)，\(\|u-\bar u\|\le\kappa d(\bar v,F(u))\) |
| strong MR | \(F^{-1}(v)\cap U\) 对全部 \(v\in W\) 是非空单值，且所得逆分支在 \(W\) Lipschitz |

MR 固定 \(v=\bar v\) 即得 MSR。strong MSR 给 MSR 并强迫局部孤立逆纤维；反向若另有局部孤立性可缩邻域，使最近逆点来自 \(\bar u\)，从而得到 strong MSR。
MR 与 strong MSR 互不蕴含：\(F(x)=|x|\) 在 \((0,0)\) strong MSR 常数 1，但负目标无原像，MR 失败；
\(F(x,y)=x\) 全局 MR 常数 1，但零纤维是一条直线，strong MSR 失败。
这些也分别说明“固定目标”不等于“两变量扰动”、“regular”不等于“逆单值”。

RL 与上述原关系正则性没有无条件替代：
\(F(x)=x^3\) 单调，故任意步长满足全图 \(\gamma=1,L=1\) RL，但在原点 \(|x|\le\kappa|x|^3\) 失败，MSR 失败；
\(F(x)=-x/\lambda\) 是线性同构、全局 MR 和 strong MSR，却在这个固定步长使全部 Minty 输入为零，全对 RL 失败。
后一例只否定固定步长推理，不否定“存在另一步长”的命题。

将残差取 \(q\) 次幂时必须标注 \(q\)-MR 或 \(q\)-MSR 并保存目标量词。
在残差 \(r\le\delta\) 的固定窗口，\(q_2\ge q_1>0\) 的 EB 给
\(\kappa r^{q_2}\le\kappa\delta^{q_2-q_1}r^{q_1}\)：较大残差指数更强；这与 PD-SCALE 的模连续性指数使用位置不同，不能只凭“指数变大”叙述。
来源定位：S2 `work/a_regularity.md` 的定义表与 implication map；此处所有反例独立直接代入。

## PD-SOURCES · 逐条溯源与下一步

- **S1**：[9/01 foundations checkpoint](../../history/sources/次单调论文研究/RL_novelty_boundary_checkpoint_2026-09-01.zip)，成员 `research/RL_foundations.md`，Definition 0.1–0.5，Theorem 1.1，Propositions 1.3–1.4，Theorem 2.1，Lemma 4.1。
- **S2**：[9/01 monotonicity checkpoint](../../history/sources/次单调论文研究/RL_monotonicity_regularity_research_checkpoint_2026-09-01.zip)，成员 `work/a_rl_position.md` §§1–4、`work/a_regularity.md`，`research/gap_examples.md` GX-015，`work/b_scalar_nonlinear.md` EX-11。
- **本轮证据**：实际读取上述 ZIP 成员后重新推导本页公式；不把 checkpoint 的 `VERIFIED` 标记当成本轮数学审查。
- **未吸收范围**：一般二参数 semimonotonicity 的最优换算、coderivative 判据、完整 GX 例库的所有锐常数，未在本页重新证明，保持来源报告层，不能由本字典批准。
- **增长义务 PD-O1**：任一新参数转换卡先写清“同图换步”还是“改关系坐标”；记录域像、单射、coverage 与尺度，分别证明。
- **增长义务 PD-O2**：每个新残差引用必须指定完整目标集、infimum 范围、窗口与 gauge 正则性；改变任一项须新版本及零集反例检查。
