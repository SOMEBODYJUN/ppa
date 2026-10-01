# Generalized monotonicity 与 metric regularity / subregularity：理论图谱

> 版本：2026-09-01（Subagent A 集成稿）  
> 性质：持续维护的事实底稿；不是 monotonicity–regularity “跷跷板”的最终综合。  
> 范围：只整合 A 的既有产物与用户提供的 RL 初稿；未重新做宽泛检索。

## 0. 范围、记号与证据纪律

除特别说明外，monotonicity 部分在实 Hilbert 空间 \(H\) 中讨论可多值映射

\[
A:H\rightrightarrows H,\qquad
(x,u),(y,v)\in\operatorname{gph}A,\qquad
a:=x-y,\quad b:=u-v.
\]

Regularity 部分令 \(X,Y\) 为度量空间，

\[
F:X\rightrightarrows Y,\qquad
(\bar x,\bar y)\in\operatorname{gph}F,\qquad
S:=F^{-1}(\bar y),\qquad
r_F(x):=d(\bar y,F(x)),
\]

并约定 \(d(z,\varnothing)=+\infty\)。涉及 derivative/coderivative 时再明确加强为空间有限维、Banach 或 Asplund，并单列闭图与紧性假设。

### 0.1 证据标签

| 标签 | 含义 | 使用边界 |
|---|---|---|
| **VERIFIED_SOURCE** | A 子稿已从 primary source 全文、作者稿或官方全文页核对 | 可承载定义、定理、精确假设与已核实常数 |
| **VERIFIED_USER_MATERIAL** | 可从用户上传的 RL 初稿直接复核 | 可承载用户已有公式；不自动等于已发表结果 |
| **ALG** | 从显示公式作出的透明代数推导 | 参数换算、Cayley 恒等式、显式代入；不冒充文献 theorem |
| **PENDING_VERIFICATION** | 原文未取得、strict witness 未完成，或 prior-art 尚未穷尽 | 只作为待办或带限定工作假说 |
| **IDX-V3 / IDX-V2** | 算法子稿对 theorem statement 的核验深度 | 只用于 §7 的后续入口；不据此推出统一 trade-off |

本文中的“maximal \(Q\)”一律指：在保持同一公式、同一参数、同一局部化 convention 的图包含偏序下不能真扩张。它不是“参数最大”，也不自动等于 full-domain。

### 0.2 Minty–Cayley 字典

固定 \(\lambda>0\)，令

\[
D_\lambda:=\operatorname{ran}(I+\lambda A),\qquad
J_{\lambda A}:=(I+\lambda A)^{-1},\qquad
R_{\lambda A}:=2J_{\lambda A}-I.
\]

置

\[
d:=a+\lambda b,\qquad r:=a-\lambda b,\qquad
p:=x+\lambda u,\quad q:=y+\lambda v.
\]

则在自然定义域 \(D_\lambda\) 上

\[
p-q=d,\quad
J_{\lambda A}p-J_{\lambda A}q=a,\quad
R_{\lambda A}p-R_{\lambda A}q=r,
\]

以及

\[
4\lambda\langle a,b\rangle=\|d\|^2-\|r\|^2. \tag{Cayley}
\]

任何 \(J_{\lambda A},R_{\lambda A}:H\to H\) 的陈述都还需 \(D_\lambda=H\)。来源：[Minty 1962](https://projecteuclid.org/journals/duke-mathematical-journal/volume-29/issue-3/Monotone-nonlinear-operators-in-Hilbert-space/10.1215/S0012-7094-62-02933-2.short)；[Bauschke–Moffat–Wang 2011, Facts 1.1–1.2 and Theorem 2.1](https://arxiv.org/pdf/1101.4688)。

---

## 1. Monotonicity atlas

### 1.1 核心 pairwise graph classes

| 类别 | 定义 / graph inequality | 空间、值型、local/global | inverse | resolvent / reflected resolvent | maximality 与主要边界 |
|---|---|---|---|---|---|
| monotone | \(\langle a,b\rangle\ge0\) | Hilbert；可多值；默认 all-pairs global，局部版须写 graph window | 自对偶 | \(J\) FNE、\(R\) nonexpansive，先只在 \(D_\lambda\) | maximally monotone \(\Leftrightarrow D_\lambda=H\) |
| strictly monotone | \(x\ne y\Rightarrow\langle a,b\rangle>0\) | 可多值；不排除同一点多值 | 不自动保持；at most single-valued 时可传给 inverse | 对 max monotone 有严格 firm inequality；不是单一 Lipschitz 常数 | strong \(\Rightarrow\) strict \(\Rightarrow\) monotone，均严格 |
| uniformly monotone | \(\langle a,b\rangle\ge\phi(\|a\|)\)，\(\phi\uparrow\)、只在 0 为 0 | 可多值；可有 local modulus | 变成以 \(\|b\|\) 为尺度的 uniform co-monotonicity | \(\langle Jp-Jq,(I-J)p-(I-J)q\rangle\ge\lambda\phi(\|Jp-Jq\|)\) | 一般不等于固定 quadratic modulus |
| \(\mu\)-strongly monotone | \(\langle a,b\rangle\ge\mu\|a\|^2,\ \mu>0\)；即 \(A-\mu I\) monotone | Hilbert；可多值；local/global | \(A^{-1}\) \(\mu\)-cocoercive；故在 range 上单值、\(1/\mu\)-Lipschitz | \((1+\lambda\mu)J_{\lambda A}\) FNE；\(\operatorname{Lip}J\le(1+\lambda\mu)^{-1}\) | maximally \(\mu\)-monotone 通常指 \(A-\mu I\) max monotone；strong 本身不保证 maximal |

来源：[Bauschke–Moffat–Wang 2011, Theorems 2.1, 4.3–4.4 and Corollary 4.7](https://arxiv.org/pdf/1101.4688)。必须保留两个 non-converses：

- \(J_{\lambda A}\) 是 contraction 不推出 \(A\) strongly monotone。二维 \(90^\circ\) skew rotation \(K\) 满足 \(\langle z,Kz\rangle=0\)，但 \(\|(I+\lambda K)^{-1}\|=(1+\lambda^2)^{-1/2}<1\)。
- \(A\) strongly monotone 一般不保证 \(R_{\lambda A}\) contraction。对 max monotone \(A\)，\(R_A\) contraction 的正确结构是 \(A\) 与 \(A^{-1}\) 都 strongly monotone；见同文 Theorem 4.4 / Corollary 4.7。

#### Signed monotonicity / hypomonotonicity / weak monotonicity

\[
\langle a,b\rangle\ge\rho\|a\|^2,\qquad \rho\in\mathbb R. \tag{M\(_\rho\)}
\]

- \(\rho>0\)：strong；\(\rho=0\)：monotone；\(\rho=-\sigma<0\)：\(\sigma\)-hypomonotone，即 \(A+\sigma I\) monotone。
- 在现代优化的 all-pairs convention 下，“\(\sigma\)-weakly monotone”常与同参数 hypomonotone 逐式相同；weak Minty/star condition 只固定解端点，不能合并。
- Hilbert、可多值；local restricted-graph 版与“存在全局 hypomonotone extension”的 local convention 不同。
- \(A^{-1}\) 变成 \(\rho\)-comonotone；maximally \(\rho\)-monotone 指 \(A-\rho I\) maximally monotone。
- 若 \(\rho=-\sigma\) 且 \(\lambda\sigma<1\)，

\[
\operatorname{Lip}J_{\lambda A}\le\frac1{1-\lambda\sigma},\qquad
\operatorname{Lip}R_{\lambda A}\le\frac{1+\lambda\sigma}{1-\lambda\sigma},
\]

且 \(A=-\sigma I\) 达到界。

来源：[Bauschke–Moursi–Wang 2019](https://arxiv.org/pdf/1902.09827)；weakly monotone 显示定义见 [Liu–Rafique–Lin–Yang, Definition 1](https://arxiv.org/pdf/1810.10207)。

#### Comonotonicity、cocoercivity、cohypomonotonicity

\[
\langle a,b\rangle\ge\rho\|b\|^2,\qquad \rho\in\mathbb R. \tag{C\(_\rho\)}
\]

\[
A\text{ is }\rho\text{-comonotone}
\Longleftrightarrow A^{-1}\text{ is }\rho\text{-monotone},\qquad
A\mapsto\lambda A:\ \rho\mapsto\rho/\lambda.
\]

| 参数区 | 名称 / 值型 | resolvent | maximality |
|---|---|---|---|
| \(\rho>0\) | \(\rho\)-cocoercive / inverse strongly monotone；自动 at most single-valued、monotone、\(1/\rho\)-Lipschitz | conically averaged，\(\alpha=\lambda/[2(\lambda+\rho)]\le1/2\) | 在 admissible 区间，maximality对应 full-domain |
| \(\rho=0\) | monotone | \(R\) nonexpansive | Minty |
| \(\rho=-\eta<0\) | global pairwise \(\eta\)-cohypomonotone；等价 \(A^{-1}\) hypomonotone | 若 \(\rho>-\lambda\)，\(J\) conically averaged；\(R\) 可 expansive | local extension/maximality convention 必须另写 |

若 \(\rho>-\lambda\)，

\[
\|Rp-Rq\|^2\le\|p-q\|^2-
\frac{\rho}{\lambda}\|(I-R)p-(I-R)q\|^2. \tag{1.1}
\]

来源：[Bauschke–Moursi–Wang 2019](https://arxiv.org/pdf/1902.09827)。Strong monotonicity 与 cocoercivity 互不蕴含：\(\mu I+N_C\) 可 max strong 且多值；\(\operatorname{diag}(0,1)\) 是 1-cocoercive 但非 strong。单值、monotone、Lipschitz 也不保证 cocoercive，skew rotation 是反例。额外有“\(\mu\)-strong + \(L\)-Lipschitz”才推出 \(\mu/L^2\)-cocoercive；凸梯度结构给 Baillon–Haddad 的 \(1/L\)，见 [Bauschke–Combettes 2010, Theorem 2.1](https://www.heldermann-verlag.de/jca/jca17/jca0932_b.pdf)。

### 1.2 两参数 semimonotonicity

#### Evens–Pas–Latafat–Patrinos convention

在基点 \((x',y')\in\operatorname{gph}A\)：

\[
\langle x-x',y-y'\rangle
\ge\mu\|x-x'\|^2+\rho\|y-y'\|^2
\quad\forall(x,y)\in\operatorname{gph}A. \tag{S\(_{\mu,\rho}\)}
\]

对每个图点作基点成立才是 all-pairs/global \((\mu,\rho)\)-semimonotone。可 set-valued。原文的 maximal-transform、outer-semicontinuity 与算法结论在有限维 \(\mathbb R^n\) 陈述。

\[
A^{-1}:(\mu,\rho)\mapsto(\rho,\mu),\qquad
\lambda A:(\mu,\rho)\mapsto(\lambda\mu,\rho/\lambda). \tag{1.2}
\]

\((\mu,0)\) 是 signed monotonicity；\((0,\rho)\) 是 signed comonotonicity。若 \([\mu]_{-}[\rho]_{-}\ge1/4\)，条件对任意图自动成立；若 \([\mu]_{+}[\rho]_{+}>1/4\)，不存在含两个不同图点的非退化图。

当 \(\mu\rho<1/4\) 时，令

\[
\xi=\frac{\rho}{\sqrt{1-4\mu\rho}},\quad
\nu=\frac{2\mu}{1+\sqrt{1-4\mu\rho}},\quad
\mathcal M=(A-\nu I)^{-1}-\xi I.
\]

在原文设置中，\(A\)（maximally）\((\mu,\rho)\)-semimonotone iff \(\mathcal M\)（maximally）monotone。对 admissible \(\lambda\)

\[
\lambda\in\left(
\frac{2[-\rho]_+}{1+\sqrt{1-4\mu\rho}},
\frac{1+\sqrt{1-4\mu\rho}}{2[-\mu]_+}
\right), \tag{1.3}
\]

maximality 对应 full-domain resolvent。令 \(m=\lambda\mu,s=\rho/\lambda\)，reflected 几何一般含交叉项

\[
(1-m-s)\|d\|^2-(1+m+s)\|r\|^2
-2(m-s)\langle d,r\rangle\ge0. \tag{1.4}
\]

故一般二参数类不能按单个 \(R\)-Lipschitz 常数无损排序。来源：[Evens–Pas–Latafat–Patrinos, Definition 4.1, Remark 4.2 and Proposition 4.12](https://arxiv.org/pdf/2305.03605)。

#### Otero–Iusem convention

对 \(0<\theta<1\)，

\[
\langle a,b\rangle\ge-\frac{\theta}{2}(\|a\|^2+\|b\|^2). \tag{OI\(_\theta\)}
\]

它恰是 \((-\theta/2,-\theta/2)\)-semimonotonicity，自对偶；\(\theta\ge1\) 时失去区分力。原文还给 explicit monotone transform 与 shifted-resolvent 区间；见 [Otero–Iusem, 2010 report / 2011 publication, Definition 2](https://webdoc.sub.gwdg.de/ebook/serien/e/IMPA_A/672.pdf)。同文 premonotone 的负项是基点依赖、一次阶且不对称，不能合并。

### 1.3 “Submonotone”同名异义

| 传统 | 显示公式 | 量词 / 空间 | resolvent / maximality | 证据 |
|---|---|---|---|---|
| Spingarn pointwise | \(\displaystyle\liminf_{x'\to\bar x}\inf_{y\in T(\bar x),y'\in T(x')}\frac{\langle y-y',\bar x-x'\rangle}{\|x'-\bar x\|}\ge0\) | 原始有限维；一端固定；一次阶渐近负偏差 | 非固定 quadratic violation；原始 maximal convention 待逐页核对 | [Spingarn 1981](https://www.jstor.org/stable/1998411) |
| Spingarn strictly submonotone | \(\displaystyle\liminf_{x_1,x_2\to\bar x}\frac{\langle y_1-y_2,x_1-x_2\rangle}{\|x_1-x_2\|}\ge0\) | 两端移动；后期作者有时简称 submonotone | 与上一行及 LT 类都不等价 | [Zajíček 2008](https://www.heldermann-verlag.de/jca/jca15/jca0651_b.pdf) |
| Luke–Thao–Tam 2017/18 | \(-\tau\|(u+z)-(\bar v+w)\|^2\le\langle z-w,u-\bar v\rangle\) | 有限维；base point 固定；pointwise | 对应 pointwise almost-FNE；不是 all-pairs | [Definition 2.9 and Proposition 2.8](https://arxiv.org/html/1605.05725v2) |
| Luke–Tam 2025 | \(\langle a,b\rangle\ge-\tau\|a+b\|^2\) | 有限维；restricted \(U\times W\)；all-pairs；\(\tau\ge0\) | \(R\) Lipschitz \(\sqrt{1+4\tau}\) on \(D=(I+F_W)(U)\)；maximality绑定 \(U,W,\tau\) | [Definition 2 and Propositions 3–5](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863) |

Luke–Tam 的平方展开

\[
\langle a,b\rangle\ge-\tau\|a+b\|^2
\Longleftrightarrow
\|R_Ap-R_Aq\|\le\sqrt{1+4\tau}\|p-q\| \tag{1.5}
\]

对任意 \(\tau\ge0\) 代数成立；引用其 Proposition 4 时仍须保留 \(\tau<1/2\)、有限维和 restricted-domain 假设。Luke–Tam 原文的定义、restricted operator、maximality与算法命题均在 finite-dimensional Euclidean setting；本文在任意实 Hilbert 空间使用的只有相同 graph inequality 与 Cayley 恒等式的 **ALG** 延伸，其 maximal extension、restricted-resolvent existence 和 PPA theorem 不自动延伸。若 \(A\) 是 \(\sigma\)-hypomonotone、\(\sigma<1/2\)，则它是 LT-submonotone，

\[
\tau=\frac{\sigma}{1-2\sigma}. \tag{1.6}
\]

反向严格失败。Luke–Tam Example 2 取

\[
F(x)=
\begin{cases}
\{-\sqrt x\},&x\ge0,\\
\varnothing,&x<0,
\end{cases}
\qquad
U=[0,1/16],\quad W=\mathbb R.
\]

原文在这一精确 restriction 上给 LT violation \(\tau=2\)；本项目直接计算又表明 \(\tau_*=2\) 为 infimal valid violation，并给 sharp reflected-resolvent constant \(L=\sqrt{1+4\tau_*}=3\)。另一方面，hypomonotonicity 所需比值
\[
\frac{-(u-v)(F(u)-F(v))}{|u-v|^2}
=\frac1{\sqrt u+\sqrt v}
\]
在 \(u,v\downarrow0\) 时无界，所以在 \(0\) 的任何右邻域均无 finite hypomonotonicity modulus。故 \(\sigma\)-hypomonotone \(\Rightarrow\) LT-submonotone 是严格蕴含。证据：printed object/restriction/\(\tau=2\) 及原文的 nonhypomonotonicity 结论为 [Luke–Tam, Example 2, equations (19)–(21)](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863) 的 **VERIFIED_SOURCE**；\(\tau_*=2\)、\(L=3\) 与上述 quantitative no-finite-modulus proof为显示计算 **ALG**。

Spingarn 1981/82 关于 mapping / proximal-point / maximality 的具体 convention 是第三个历史节点；在取得全文前标 **PENDING_VERIFICATION**，不得用摘要把 pointwise 与 strictly submonotone 两个定义重新合并。

### 1.4 VI-sign、multi-point 与 graph-wide refinements

对单值 \(F:C\to H\)，一种 VI convention 是

\[
\begin{aligned}
\text{pseudomonotone}:&\quad
\langle F(x),y-x\rangle\ge0\Rightarrow\langle F(y),y-x\rangle\ge0,\\
\text{quasimonotone}:&\quad
\langle F(x),y-x\rangle>0\Rightarrow\langle F(y),y-x\rangle\ge0.
\end{aligned}
\]

在此 convention 下 monotone \(\Rightarrow_{\rm strict}\) pseudomonotone \(\Rightarrow_{\rm strict}\) quasimonotone；见 [Aussel et al. 2020](https://optimization-online.org/wp-content/uploads/2020/02/7602.pdf)。Brézis pseudomonotonicity是 reflexive Banach 空间中的弱收敛序列性质，不能与上述 VI 定义互换；见 [Papageorgiou–Rădulescu–Repovš 2018](https://arxiv.org/pdf/1810.03995)。

对 \(n\ge2\)，\(n\)-cyclic monotonicity是

\[
\sum_{i=1}^{n}\langle x_i-x_{i+1},u_i\rangle\ge0,\qquad x_{n+1}=x_1. \tag{N\(_n\)}
\]

\(n=2\) 即 monotone；\(m\ge n\Rightarrow m\)-cyclic \(\Rightarrow n\)-cyclic；取逆保持。Planar rotation 的精确阈值 \(|\theta|\le\pi/n\) 与严格层级见 [M. D. Voisei, General monotonicity, Example 43](https://arxiv.org/html/2411.04212v2)。Maximal cyclically monotone 恰为 proper lsc convex \(f\) 的 \(\partial f\)，见 [Rockafellar 1966](https://msp.org/pjm/1966/17-3/pjm-v17-n3-p08-p.pdf) 与 [Rockafellar 1970](https://msp.org/pjm/1970/33-1/pjm-v33-n1-p19-s.pdf)。

在先假设 monotone 后：

\[
\text{paramonotone: }\ \langle a,b\rangle=0
\Rightarrow(x,v),(y,u)\in\operatorname{gph}A; \tag{Para}
\]

\[
\text{rectangular / 3*: }\ 
\inf_{(z,w)\in\operatorname{gph}A}\langle x-z,v-w\rangle>-\infty
\quad(x\in\operatorname{dom}A,v\in\operatorname{ran}A). \tag{Rect}
\]

二者取逆自对偶；其 resolvent 刻画见 [Bauschke–Moffat–Wang 2011, Theorem 2.1(xv)–(xvii)](https://arxiv.org/pdf/1101.4688)。即使在 max monotone 类中二者仍互不蕴含；[Bauschke–Wang–Yao 2012](https://arxiv.org/pdf/1201.4220) 给出两个单向缺口及 neither 的对象。3-cyclic 与 3* / rectangular 完全不同。

### 1.5 Banach accretivity 与 prox-regularity 连接

对实 Banach 空间 \(X\)，\(A:X\rightrightarrows X\) accretive 指

\[
\|x-y+\lambda(u-v)\|\ge\|x-y\|
\quad\forall\lambda>0,\ (x,u),(y,v)\in\operatorname{gph}A. \tag{Acc}
\]

Duality-map 形式是：对每对图点，存在 \(j\in J_X(x-y)\) 使 \(\langle u-v,j\rangle\ge0\)；不能误写成对所有 \(j\)。m-accretive 再加 range condition。Accretive 使 resolvent在其 range 上 single-valued nonexpansive；m-accretive 使其 full-domain。一般 Banach 中 \(2J-I\) nonexpansive、maximal accretive \(=\) m-accretive 都不能无条件照搬；Hilbert/Riesz 识别下才恢复 monotone/maximally monotone。来源：[Browder 1967](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-73/issue-3/Nonlinear-accretive-operators-in-Banach-spaces/bams/1183528868.full)、[Browder 1968](https://www.pnas.org/doi/10.1073/pnas.61.2.388)、[Pischke, Definition 2.2](https://nicholaspischke.github.io/papers/metatheorems_accretive_monotone.pdf)。

Proper lsc \(f\) 在 \((\bar x,\bar v)\in\operatorname{gph}\partial f\) prox-regular 的核心局部支持式是

\[
f(x')\ge f(x)+\langle v,x'-x\rangle-\frac r2\|x'-x\|^2, \tag{PR}
\]

带 base、subgradient 与 \(f\)-attentive level localization。交换两点得受限 subgradient graph 的

\[
\langle x_1-x_2,v_1-v_2\rangle\ge-r\|x_1-x_2\|^2. \tag{1.7}
\]

有限维完整 iff 还要求 \(\bar v\) 是 proximal subgradient。若 \(\lambda r<1\)，localized proximal resolvent single-valued Lipschitz，粗界 \(1/(1-\lambda r)\)。见 [Poliquin–Rockafellar 1996, Theorem 3.2](https://doi.org/10.1090/S0002-9947-96-01544-9) 与 [Theorems 2.1–2.2](https://www.heldermann-verlag.de/jca/jca17/jca0849_b.pdf)。对 prox-regular set，normal cone 还必须截断 normal norm；完整锥图通常不满足有限 hypomonotonicity modulus。

---

## 2. Regularity atlas

### 2.1 四个核心 mapping-side 性质

| 性质 | 完整局部量词与距离式 | exact modulus | inverse-side 精确性质 | 结构 |
|---|---|---|---|---|
| metric regularity (MR) around \((\bar x,\bar y)\) | \(\exists U\ni\bar x,V\ni\bar y,\kappa\ge0\)，\(\forall x\in U,\forall y\in V\)：\(\displaystyle d(x,F^{-1}(y))\le\kappa d(y,F(x))\) | \(\operatorname{reg}F(\bar x\mid\bar y):=\inf\kappa\) | \(F^{-1}\) Aubin around \((\bar y,\bar x)\) | two-variable；uniform in nearby target |
| metric subregularity (MSR) at \((\bar x,\bar y)\) | \(\exists U\ni\bar x,\kappa\ge0\)，\(\forall x\in U\)：\(\displaystyle d(x,S)\le\kappa r_F(x)\) | \(\operatorname{subreg}F(\bar x\mid\bar y):=\inf\kappa\) | \(F^{-1}\) calm at \((\bar y,\bar x)\) | fixed target；MR \(\Rightarrow\) MSR |
| strong metric regularity (SMR) | \(\exists U\ni\bar x,V\ni\bar y\)，\(s(y):=F^{-1}(y)\cap U\) 对每个 \(y\in V\) 恰为一个点、取值于 \(U\)，且 \(s\) Lipschitz | 所有充分小 inverse localizations 的 local Lipschitz constants 的下确界等于 \(\operatorname{reg}F\)；每个 \(\ell>\operatorname{reg}F\) 可缩小邻域取得 | single-valued Lipschitz inverse localization | \(\mathrm{SMR}\iff\mathrm{MR}+\) graphical localization 对所有近邻右端单值 |
| strong metric subregularity (SMSR) at \((\bar x,\bar y)\) | \(\exists U\ni\bar x,\kappa\ge0\)，\(\forall x\in U\)：\(\displaystyle d(x,\bar x)\le\kappa r_F(x)\) | \(\operatorname{subreg}_{\rm strong}F(\bar x\mid\bar y):=\inf\kappa\) | \(F^{-1}\) isolatedly calm at \((\bar y,\bar x)\) | \(\mathrm{SMSR}\iff\mathrm{MSR}+\bar x\) isolated in \(S\) |

定义适用于 single- 或 set-valued maps 和一般 metric spaces；locally closed graph 在本文中是判据假设，不并入定义。来源：[Durea–Strugariu, Definition 2.1 and Proposition 2.2](https://arxiv.org/html/1102.0415v2)、[Cibulka–Dontchev–Kruger, pp. 1–3 and Proposition 1.2](https://arxiv.org/html/1701.02078v1)、[Gfrerer–Outrata, Definition 2](https://arxiv.org/html/1611.08260v1)。

MR 精确等价于 \(F^{-1}\) Aubin，也等价于 around linear openness：存在 \(U,V,\varepsilon,c>0\)，对所有

\[
(x,y)\in\operatorname{gph}F\cap(U\times V),\quad0<t<\varepsilon,
\qquad B(y,ct)\subset F(B(x,t)). \tag{LO}
\]

\[
\operatorname{reg}F(\bar x\mid\bar y)
=\operatorname{lip}F^{-1}(\bar y\mid\bar x)
=\operatorname{lop}(F;\bar x\mid\bar y)^{-1}. \tag{2.1}
\]

这是定义级等价，不需闭图、Banach 或凸性。只在中心要求 covering 的 punctual openness 是另一性质。来源：[Dontchev–Quincampoix–Zlateva, Definition 1.1 and equation (6)](https://www.heldermann-verlag.de/jca/jca13/jca0526_b.pdf)；[Ioffe, Definition 2.1 and Proposition 2.2](https://arxiv.org/pdf/1505.07920)。

### 2.2 Inverse-side stability 与 semiregularity

对 \(G:P\rightrightarrows X\)、\((\bar p,\bar x)\in\operatorname{gph}G\)：

\[
G(p_1)\cap U\subset G(p_2)+L\,d(p_1,p_2)\mathbb B
\quad\forall p_1,p_2\in V \tag{Aubin}
\]

定义 Aubin around；

\[
G(p)\cap U\subset G(\bar p)+L\,d(p,\bar p)\mathbb B
\quad\forall p\in V \tag{calm}
\]

定义 calm at；

\[
G(p)\cap U\subset \bar x+L\,d(p,\bar p)\mathbb B
\quad\forall p\in V \tag{icalm}
\]

定义 isolated calm at。Aubin \(\Rightarrow\) calm；isolated calm \(\Rightarrow\) calm；Aubin 与 isolated calm 互不包含。

Hemiregularity / metric semiregularity 固定 \(x=\bar x\)：

\[
d(\bar x,F^{-1}(y))\le\kappa d(y,\bar y)\quad\forall y\in V. \tag{HREG}
\]

它等价于 punctual linear openness及 \(F^{-1}\) 的 Lipschitz lower semicontinuity。更强的 uniform hemiregularity 是

\[
d(\bar x,F^{-1}(y))\le\kappa d(y,F(\bar x)). \tag{UHREG}
\]

MR \(\Rightarrow\) UHREG \(\Rightarrow\) HREG；MSR 与 HREG 互不包含。来源：[Uderzo](https://arxiv.org/html/1703.10552v2) 与 [Durea–Strugariu](https://arxiv.org/html/1102.0415v2)。

### 2.3 Hölder、higher-order 与 gauge regularity

本项目采用 residual-exponent convention

\[
d(x,S)\le\kappa r_F(x)^q. \tag{R-q}
\]

在局部小残差下，\(0<q<1\) 是 Hölder/fractional，\(q=1\) 是 ordinary MSR，\(q>1\) 是非平凡的 higher-order MSR，且 \(q\) 越大越强。另一传统写

\[
\tau d(x,S)^p\le r_F(x), \tag{D-p}
\]

两者换算 \(q=1/p\)、\(\kappa=\tau^{-q}\)。任何 \(\gamma q\) 比较前必须统一 convention。来源：[Mordukhovich–Ouyang, Definition 3.1](https://arxiv.org/html/1507.04825v1)；[Kruger et al.](https://arxiv.org/html/2106.08149v2)。

\[
\begin{aligned}
q\text{-MR}:&\quad d(x,F^{-1}(y))\le\kappa d(y,F(x))^q
&&\forall x\in U,\forall y\in V,\\
q\text{-MSR}:&\quad d(x,S)\le\kappa r_F(x)^q
&&\forall x\in U,\\
q\text{-SMSR}:&\quad d(x,\bar x)\le\kappa r_F(x)^q
&&\forall x\in U.
\end{aligned} \tag{2.2}
\]

Inverse-side 分别是 \(q\)-Hölder Aubin、\(q\)-calm、\(q\)-isolated calm，upper moduli相同。对 \(0<q\le1\)，\(q\)-MR 还等价于

\[
B(y,c\,t^{1/q})\subset F(B(x,t)),\qquad
\operatorname{reg}_qF=(\operatorname{lop}_{1/q}F)^{-q}
=\operatorname{lip}_qF^{-1}. \tag{2.3}
\]

在 normed spaces 等具有适当线段/路径结构的 setting，two-variable \(q>1\) MR 的 inverse pairwise estimate可由路径细分迫使 localization 局部常值；任意 metric spaces 中该退化结论为假（snowflake metric 是反例）。Fixed-target \(q>1\) MSR/SMSR 可非平凡。若 \(q_2>q_1>0\)，缩小到 residual \(<1\) 的邻域后

\[
q_2\text{-MSR/SMSR}\Rightarrow_{\rm strict}q_1\text{-MSR/SMSR}. \tag{2.4}
\]

\(F_p(x)=\operatorname{sgn}(x)|x|^p\) 的 sharp largest residual exponent 是 \(q_*=1/p\)。来源：[Li–Mordukhovich](https://optimization-online.org/wp-content/uploads/2012/02/3340.pdf)、[Mordukhovich–Ouyang](https://arxiv.org/html/1507.04825v1)、[Lee–Pham](https://optimization-online.org/wp-content/uploads/2020/04/7726.pdf)。

给定单调递增 gauge \(\varphi\)、\(\varphi(0)=0\)、\(\varphi(t)>0\) for \(t>0\)，

\[
d(x,S)\le\kappa\varphi(r_F(x))\qquad\forall x\in U. \tag{\(\varphi\)-MSR}
\]

\[
{}^sr_\varphi[F](\bar x,\bar y)
=\liminf_{\substack{x\to\bar x\\x\notin S}}
\frac{\varphi(r_F(x))}{d(x,S)}. \tag{2.5}
\]

若近零 \(\varphi_1(t)\le C\varphi_2(t)\)，则 \(\varphi_1\)-MSR \(\Rightarrow\varphi_2\)-MSR；互不支配时一般不可比。Gauge 放在 solution-distance 一侧的 convention 只有在可反演时才能无损转换。来源：[Kruger](https://arxiv.org/html/1502.06159v2)；[Luke–Thao–Tam, Definition 2.17](https://arxiv.org/html/1605.05725v2)。

### 2.4 Error bounds 与 exact rates

对 \(f:X\to\mathbb R\cup\{+\infty\}\)、\(S_f=\{x:f(x)\le0\}\)，local EB 是

\[
d(x,S_f)\le\kappa[f(x)]_+\quad\forall x\in U. \tag{EB}
\]

Mapping MSR 正是 residual EB。本文把 strong EB 固定为 isolated 版本

\[
d(x,\bar x)\le\kappa[f(x)]_+\quad\forall x\in U, \tag{SEB}
\]

对应 SMSR。SMSR 的 exact steepest displacement rate 是

\[
|F|^{\downarrow}(\bar x\mid\bar y)
:=\liminf_{\substack{x\to\bar x\\x\ne\bar x}}
\frac{r_F(x)}{d(x,\bar x)},\qquad
\mathrm{SMSR}\iff |F|^{\downarrow}>0,\quad
\operatorname{subreg}_{\rm strong}F
=\frac{1}{|F|^{\downarrow}}. \tag{2.6}
\]

这里采用扩展实数倒数约定 (1/(+\infty)=0)、(1/0=+\infty)；特别地，
不能把 (2.6) 改写成未定义的字面乘积 (0\cdot(+\infty)=1)。

普通 MSR 的 exact ratio 是

\[
{}^sr[F](\bar x,\bar y)
=\liminf_{\substack{x\to\bar x\\x\notin S}}
\frac{r_F(x)}{d(x,S)}. \tag{2.7}
\]

Complete spaces + locally closed graph/lsc model 下有 exact nonlocal-slope characterization；缺这些假设时不能无条件套用。\(r_F\) 即使 graph closed 也未必 lsc。来源：[Kruger](https://arxiv.org/html/1502.06159v2)、[Cibulka–Dontchev–Kruger](https://arxiv.org/html/1701.02078v1)。

### 2.5 Directional、relative、partial、uniform 与 set variants

| 变体 | 完整对象 | 关系 / 警告 |
|---|---|---|
| graph-direction DMR | 测试 \((\bar x+tu',\bar y+tv')\)，\((u',v')\) 接近 \((u,v)\)，并带 distance-to-graph cutoff | 此处仅为 schematic 路由，不承载 iff 边；完整方向锥、\(t\)、cutoff 与邻域量词须逐字取自 [Definition 7, Lemma 8, Theorem 9](https://arxiv.org/html/1611.08260v1) |
| output-residual directional MR | 只测试特定 output residual cone | 与 graph-direction 不同；此处同样降级为 schematic，完整量词见 [Huynh–Théra](https://arxiv.org/html/1304.7748v1) |
| relative MR | \(\displaystyle d(x,F^{-1}(y)\cap\overline{V_y})\le\kappa d(y,F(x))\) | 同时限制测试点与 inverse solutions；ordinary MR 不能对任意 \(V\) 机械推出 |
| partial MR uniformly in \(p\) | 对 \(F_p(x)\)，\(\displaystyle d(x,F_p^{-1}(y))\le\kappa d(y,F_p(x))\) 对所有近邻 \(x,p,y\) | 标准 product metric 下 partial-uniform MR \(\Rightarrow\) full MR in \((x,p)\)，反向由 \(F(x,p)=p\) 否定 |
| Robinson stability | \(\displaystyle d(x,\Gamma(p))\le\kappa d(g(p,x),C)\) 对所有近邻 \(p,x\) | uniform-in-\(p\) subregularity/EB；RS \(\Rightarrow\) partial MSCQ；[Gfrerer–Mordukhovich](https://arxiv.org/html/1609.02238v2) |
| MSR/SMSR around | 同一 \(\kappa\) 在邻近每个 graph point 成立 | 强于 at-reference；[Gfrerer–Outrata](https://arxiv.org/pdf/2208.01331) |

闭集合族的 global/bounded/local linear regularity用

\[
d(x,\cap_i\Omega_i)\le\kappa\max_i d(x,\Omega_i) \tag{LR}
\]

分别在全空间、每个 bounded set或参考点邻域量化。对两个集合，local LR 即 subtransversality，等价于标准 set mapping 的 MSR；对所有小平移 uniform 的 transversality 对应该 mapping 的 MR，并严格蕴含 subtransversality。见 [Kruger–Luke–Thao](https://arxiv.org/html/1611.04787v2) 与 [Set Regularities and Feasibility Problems](https://arxiv.org/html/1602.04935v1)。

### 2.6 Derivative / coderivative 判据

| 目标 | 安全判据 | 必须保留的假设 | 禁止简写 |
|---|---|---|---|
| MR | \(0\in D^*F(\bar x\mid\bar y)(y^*)\Rightarrow y^*=0\)，即 \((D^*F)^{-1}(0)=\{0\}\) | finite-dimensional \(X,Y\)，locally closed graph | \(D^*F(\bar x\mid\bar y)(0)=\{0\}\) 是 \(F\) 自身 Aubin criterion |
| MR infinite-dimensional | 对 \(G=F^{-1}\) 使用 Aubin criterion：closed graph、PSNC\((G)\) 与对应 inverse mixed-coderivative kernel；或使用邻近 graph-point derivative bounds | Asplund、closed graph、PSNC\((F^{-1})\) / normal compactness，按 theorem 版本 | 不得无定理地把 PSNC\((F^{-1})\) 换成 PSNC\((F)\)，也不可搬运 finite-dimensional point iff |
| MSR | ratio (2.7) exact；complete + locally closed 时有 nonlocal-slope iff；directional/outer coderivatives给条件 | lsc、complete、Asplund、convex依判据而变 | 一般非凸 multifunction 无简单 limiting-coderivative single-point iff；MR test过强 |
| SMSR | finite-dimensional domain 时 \(DF(\bar x\mid\bar y)^{-1}(0)=\{0\}\) iff；两边有限维时 modulus equality | domain finite-dimensional；exactness再需两边有限维 | Fréchet coderivative通常只给上界；局部凸图才 equality |
| power SMSR | \(D_pF(\bar x,\bar y)^{-1}(0)=\{0\}\) | finite dimensions；原文 distance-exponent \(p\)，本项目代 \(p=1/q\) | 不可复制同字母 exponent |
| SMR | MR criterion 加 inverse single-valued graphical localization | 邻近右端 existence + uniqueness | MR coderivative nonsingularity不检测 branch uniqueness |

有限维 MR：[Mordukhovich 1993](https://www.ams.org/journals/tran/1993-340-01/S0002-9947-1993-1156300-4/)。Banach 边界：[Dontchev–Quincampoix–Zlateva](https://www.heldermann-verlag.de/jca/jca13/jca0526_b.pdf)。SMSR：[Cibulka–Dontchev–Kruger, Theorems 5.1–5.2](https://arxiv.org/html/1701.02078v1)。无限维 PSNC/SNC 细分标 **PENDING_VERIFICATION**，具体使用时回原 theorem。

对 bounded linear \(A:X\to Y\)：MR iff \(A\) surjective；MSR iff range closed；SMSR iff injective且 range closed；SMR iff boundedly invertible。有限维 finite-union polyhedral graph在每个 graph point有 MSR/calmness；SMSR还需 inverse point isolated；MR/SMR仍需 surjectivity/local uniqueness。有限维 semialgebraic multifunction通常有某个局部 Hölder exponent，但不是 universal number。

---

## 3. RL 条件的精确定位

### 3.1 Restricted graph、单值性与三种等价表示

固定

\[
\Gamma\subset\operatorname{gph}F,\qquad
D_\Gamma:=\{u+\lambda u^*:(u,u^*)\in\Gamma\}.
\]

对 \(x=u+\lambda u^*\in D_\Gamma\)，先把受限 Cayley relation 写作 \(R_\Gamma x:=u-\lambda u^*\)。RL-\((\lambda,L,\gamma)\) 是

\[
\boxed{\|a-\lambda b\|\le L\|a+\lambda b\|^\gamma},\qquad0<\gamma\le1. \tag{RL}
\]

以下三项精确等价（**VERIFIED_USER_MATERIAL / ALG**）：

1. (RL) 对 \(\Gamma\) 中所有图点对成立；
2. \(R_\Gamma:D_\Gamma\to H\) 单值，且
   \[
   \|R_\Gamma x-R_\Gamma y\|\le L\|x-y\|^\gamma; \tag{RL-Cayley}
   \]
3. 内积式
   \[
   \boxed{\lambda\langle a,b\rangle\ge\frac14
   \big(\|a+\lambda b\|^2-L^2\|a+\lambda b\|^{2\gamma}\big)}. \tag{RL-IP}
   \]

RL 自身强迫受限 resolvent 单值：相同 Minty input 给 \(a+\lambda b=0\)，RL 再给 \(a-\lambda b=0\)，故 \(a=b=0\)。令 \(J_\Gamma=(I+R_\Gamma)/2\)，还等价于

\[
\|J_\Gamma x-J_\Gamma y\|^2+
\|(I-J_\Gamma)x-(I-J_\Gamma)y\|^2
\le\frac12\big(\|x-y\|^2+L^2\|x-y\|^{2\gamma}\big). \tag{RL-AFNE}
\]

因此用户初稿的“多值时 selection-wise”应改成：RL 在 restricted graph 上已经强迫 \(J_\Gamma,R_\Gamma\) 单值；若 \(\Gamma=\operatorname{gph}F\)，自然定义域仍只是 \(D_\lambda\)。RL 不推出 full-domain、maximality、邻域覆盖、branch exclusion 或 self-map/invariance。

### 3.2 \(\gamma=1\)：精确换参

令

\[
\theta_L:=\frac{1-L^2}{2(1+L^2)}\in(-1/2,1/2).
\]

则

\[
\mathrm{RL}(\lambda,L,1)
\iff
\langle a,b\rangle\ge
\mu_L\|a\|^2+\rho_L\|b\|^2, \tag{3.1}
\]

\[
\boxed{
\mu_L=\frac{1-L^2}{2\lambda(1+L^2)}=\frac{\theta_L}{\lambda},\qquad
\rho_L=\frac{\lambda(1-L^2)}{2(1+L^2)}=\lambda\theta_L,\qquad
\rho_L=\lambda^2\mu_L.} \tag{3.2}
\]

所以 \(\lambda F\) 恰为 equal-parameter \((\theta_L,\theta_L)\)-semimonotone；RL 是一般二参数类的一条 tied curve。

| \(L\) | graph side | Cayley side | 最近邻类 |
|---|---|---|---|
| \(0<L<1\) | \(\mu_L,\rho_L>0\)：同时 strong monotone 与 cocoercive | contraction，constant \(L\) | positive symmetric semimonotonicity；不属于 LT 非负 violation 命名 |
| \(L=1\) | \(\mu_L=\rho_L=0\) | nonexpansive | ordinary monotonicity |
| \(L>1\) | \(\mu_L,\rho_L<0\) | Lipschitz，constant \(L\) | scaled Luke–Tam；亦是 Otero symmetric slice |

当 \(L\ge1\)，对 \(\lambda F\) 的 Luke–Tam 参数是

\[
\boxed{\tau=\frac{L^2-1}{4},\qquad
L=\sqrt{1+4\tau},\qquad
\varepsilon_{\rm aFNE}=2\tau=\frac{L^2-1}{2}.} \tag{3.3}
\]

若引用 Luke–Tam Proposition 4，仍须加 \(\tau<1/2\)，即 \(1\le L<\sqrt3\)，以及有限维和 restricted-domain 假设。与 Otero 参数的换算是

\[
\theta=\frac{L^2-1}{L^2+1},\qquad
\tau=\frac{\theta}{2(1-\theta)}. \tag{3.4}
\]

更一般地，若 \(F\) 有 \((\mu,\rho)\)-semimonotonicity certificate，令 \(m=\lambda\mu,s=\rho/\lambda\)。在 \(\mu\rho<1/4\) 且 \(1+m+s>0\) 时，类级 sharp 的 \(\gamma=1\) RL 保证为

\[
L_{\mu,\rho}(\lambda)
=\frac{|m-s|+\sqrt{1-4ms}}{1+m+s}. \tag{3.5}
\]

这是由交叉项作 sharp Cauchy bound 得到的 **ALG** sufficient guarantee，不把 tied curve 外的二参数类与 RL 等同。

### 3.3 Inversion、scaling 与 \(\gamma<1\) 尺度反转

\[
\boxed{
F\in\mathrm{RL}(\lambda,L,\gamma)
\iff
F^{-1}\in\mathrm{RL}(\lambda^{-1},L\lambda^{\gamma-1},\gamma).} \tag{3.6}
\]

当 \(\gamma=1\)，\(L\) 在 inversion 下不变；当 \(\gamma<1\)，\(L\) 带尺度，跨单位比较数值没有意义。另有

\[
F\in\mathrm{RL}(\lambda,L,\gamma)
\iff cF\in\mathrm{RL}(\lambda/c,L,\gamma),\qquad c>0. \tag{3.7}
\]

令 \(t=\|a+\lambda b\|>0\)。RL-IP 可写成

\[
\lambda\langle a,b\rangle\ge-\tau_\gamma(t)t^2,\qquad
\tau_\gamma(t)=\frac14\big(L^2t^{-2(1-\gamma)}-1\big). \tag{3.8}
\]

当 \(0<\gamma<1\)：

- \(t\downarrow0\)：\(\tau_\gamma(t)\to+\infty\)，所以通常邻域上不推出 fixed finite LT/hypomonotone/almost-NE violation；
- \(t=L^{1/(1-\gamma)}\)：signed violation 过零；
- \(t\to\infty\)：\(\tau_\gamma(t)\to-1/4\)，大尺度反而强迫正 inner-product geometry。

若 \(\operatorname{diam}D\le\Delta\)，\(K\)-Lipschitz \(R\) 推出 \(\gamma\)-Hölder，常数 \(K\Delta^{1-\gamma}\)；更大 exponent在固定 bounded window 上更强。Global unbounded domain 上发生反转：

- \(R=I\) 全局 Lipschitz，却不是任何 \(\gamma<1\) 的 global Hölder bound；
- \(R(t)=\operatorname{sgn}(t)|t|^\gamma\) 全局 \(\gamma\)-Hölder，却在 0 非 Lipschitz；经
  \[
  \Gamma_R=\left\{\left(\frac{x+Rx}{2},\frac{x-Rx}{2\lambda}\right):x\in D\right\} \tag{3.9}
  \]
  生成 RL graph。

因此 global RL\(_1\) 与 global RL\(_\gamma\)（\(\gamma<1\)）互不包含；不同 subunit exponents 也受小尺度/大尺度相反控制。RL\(_\gamma\) 只在 \(\|x-y\|\ge\delta\) 的 annulus 上给 Lipschitz 常数 \(L\delta^{\gamma-1}\)，不能用于通常邻域。

额外 **ALG** 限制：

- 两个零点 \(p,q\) 满足 \(\|p-q\|\le L\|p-q\|^\gamma\)，故 global RL\(_\gamma\) 的零集直径至多 \(L^{1/(1-\gamma)}\)；
- 若 graph differences 可沿无界射线同比缩放，RL\(_\gamma\) 强迫对应 \(a-\lambda b=0\)；对 full-domain linear Cayley graph，退化为 \(R=0\)，即 \(A=\lambda^{-1}I\)。

### 3.4 RL 与邻近理论的判定

| 比较对象 | 安全结论 | strictness / caveat |
|---|---|---|
| RL\(_1,L\ge1\) vs LT | 对 \(\lambda F\) 公式精确等价，参数 (3.3) | Published Prop. 4 的 \(\tau<1/2\) 与 restricted domain 不可删 |
| RL\(_1\) vs \((\mu,\rho)\)-semi | 精确等于 tied curve \(\rho=\lambda^2\mu\) | 一般二参数类不是同一节点；(3.5) 仅 sufficient |
| RL\(_1\) vs RL\(_\gamma\), \(\gamma<1\) | global unbounded 上互不包含；bounded window 上前者蕴含后者 | \(R=I\) 与 power-Hölder Cayley graph |
| monotone vs RL\(_\gamma\) | global unbounded 上互不包含；bounded \(D\) 上 monotone \(\Rightarrow\) RL\(_\gamma\) | 反向可用 bounded \(R=2I\)；完整 operator/regularity交 C 重算 |
| hypo/cohypo vs RL\(_1\) | \(\lambda\sigma<1\) 时 hypomonotone 给 sharp bound \((1+\lambda\sigma)/(1-\lambda\sigma)\)；inverse 对称 | converse严格失败：\(-\sqrt x\) 在 \(U=[0,1/16]\)、\(W=\mathbb R\) 上有 sharp LT \(\tau_*=2\)、RL constant \(L=3\)，但在 0 的任何右邻域均非 finite-hypomonotone；inverse给dual缺口 |
| comonotone / conically averaged \(J\) vs RL\(_1\) | admissible comonotonicity充分给 Lipschitz \(R\) | converse fails：\(R=2I\) 的 Cayley graph |
| all-pairs RL vs anchored/pointwise | all-pairs 推出每个 base 的统一 Hölder calmness | 单 base不推出 all-pairs；自然显式见证 **PENDING_VERIFICATION** |
| RL vs MR/MSR/SMSR | 坐标与量词不同；目前无可写成普遍蕴含的 theorem | 四象限交 B/C；完成前不把“互不包含”升级为 verified theorem |

### 3.5 \(\gamma q\) 的证据边界

令 \(S=F^{-1}(0)\ne\varnothing\)、\(x^+=J_{\lambda F}x\)、\(r=d(x,S)\)。一般 Hilbert 空间中的非凸闭集未必有最近点，故不能默认存在 \(p\in S\) 使 \(\|x-p\|=r\)。

对每个 \(\varepsilon>0\)，按距离下确界的定义取 \(p_\varepsilon\in S\) 使

\[
\|x-p_\varepsilon\|\le r+\varepsilon. \tag{3.10a}
\]

必须另外要求图点对

\[
\left(x^+,\frac{x-x^+}{\lambda}\right),\qquad(p_\varepsilon,0)
\]

以及 MSR 评估点 \(x^+\) 对一列 \(\varepsilon\downarrow0\) 统一落在同一个 restricted graph / regularity window。置
\[
a_\varepsilon=x^+-p_\varepsilon,\qquad s=x-x^+.
\]
RL 给
\[
\|a_\varepsilon-s\|
\le L\|a_\varepsilon+s\|^\gamma
=L\|x-p_\varepsilon\|^\gamma.
\]
由 \(2s=(a_\varepsilon+s)-(a_\varepsilon-s)\)，

\[
\|x-x^+\|
\le\frac12\big((r+\varepsilon)+L(r+\varepsilon)^\gamma\big),\qquad
d(0,F(x^+))
\le\frac{(r+\varepsilon)+L(r+\varepsilon)^\gamma}{2\lambda}. \tag{3.10b}
\]

若 \(d(u,S)\le\rho d(0,F(u))^q\) 在同一 window 以统一 \(\rho\) 成立，则

\[
d(x^+,S)
\le\frac{\rho}{(2\lambda)^q}
\big((r+\varepsilon)+L(r+\varepsilon)^\gamma\big)^q.
\]

令 \(\varepsilon\downarrow0\)，得到

\[
d(x^+,S)\le\frac{\rho}{(2\lambda)^q}(r+Lr^\gamma)^q
=O(r^{\gamma q}). \tag{3.11}
\]

同理，若 gauge \(\psi\) 连续（或至少在相关点右连续；否则保留相应右极限），则

\[
d(x^+,S)\le
\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right). \tag{3.12}
\]

若显式假设 \(S\) proximinal，则可直接取最近解并跳过 \(\varepsilon\)-极限；例如 Hilbert 空间中的非空闭凸集、或有限维 Euclidean 空间中的非空闭集均属此情形。局部 restricted graph 的 two-radius / branch 条件仍不可省。

\(\gamma q\) 只是这条证明中 \(r^\gamma\) 与 \(t^q\) 的函数复合，不是已证 universal compensation law。把 (3.11) 提升为 PPA convergence theorem 还需：branch exclusion、resolvent existence/range coverage、self-map/invariance、uniform solution-tube MSR、two-radius localization、所有 selections量词、zero-set closedness、finite-length 后极限归属及 fixed/variable stepsize 区分。因此 (3.10)–(3.12) 标 **ALG**；用户初稿中的 convergence theorem 暂标 **PENDING_VERIFICATION**。

### 3.6 Gauge threshold 的审计补丁

令

\[
\Phi(r):=\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right).
\]

形式上的局部 contraction 条件是 \(\limsup_{r\downarrow0}\Phi(r)/r<1\)。方便的 sufficient threshold 必须分开：

\[
0<\gamma<1:\quad
\limsup_{t\downarrow0}\frac{\psi(t)}{t^{1/\gamma}}
<\left(\frac{2\lambda}{L}\right)^{1/\gamma}; \tag{3.13a}
\]

\[
\gamma=1:\quad
\limsup_{t\downarrow0}\frac{\psi(t)}{t}
<\frac{2\lambda}{1+L}. \tag{3.13b}
\]

用户初稿中的 \(2\lambda/L\) 阈值只适用于 \(0<\gamma<1\)，不能用于 \(\gamma=1\)。

---

## 4. 严格关系边表

符号：\(\Leftrightarrow\) 为 exact equivalence；\(\Rightarrow_s\) 为已有 strict witness 的严格蕴含；\(\perp\) 为双向见证完备的互不包含；**pending** 不进入事实图。

### 4.1 Monotonicity / graph geometry

| From | 关系 | To | 假设 / 参数 | strictness、见证或 locator |
|---|---:|---|---|---|
| maximally monotone | \(\Leftrightarrow\) | \(J_{\lambda A}:H\to H\) full-domain FNE | Hilbert，\(\lambda>0\) | [Minty 1962](https://projecteuclid.org/journals/duke-mathematical-journal/volume-29/issue-3/Monotone-nonlinear-operators-in-Hilbert-space/10.1215/S0012-7094-62-02933-2.short)；[BMW Fact 1.2](https://arxiv.org/pdf/1101.4688) |
| monotone | \(\Leftrightarrow\) | \(R_{\lambda A}\) nonexpansive on \(D_\lambda\) | 不声称 full-domain | Cayley identity |
| \(\mu\)-strong | \(\Rightarrow_s\) | strict monotone | \(\mu>0\) | \(x^3\) strict但非 strong |
| strict monotone | \(\Rightarrow_s\) | monotone |  | \(A=0\) 非 strict |
| \(\mu\)-strong \(A\) | \(\Leftrightarrow\) | \(\mu\)-cocoercive \(A^{-1}\) | natural ranges | inversion |
| \(R_{\lambda A}\) contraction | \(\Leftrightarrow\) | \(A\) 与 \(A^{-1}\) 都 strong | max monotone；scaled moduli | [BMW Corollary 4.7](https://arxiv.org/pdf/1101.4688) |
| \(\beta\)-cocoercive | \(\Rightarrow_s\) | monotone and \(1/\beta\)-Lipschitz | single-valued on domain | skew rotation否定 converse |
| strong monotone | \(\perp\) | cocoercive | 一般 set-valued Hilbert maps | \(\mu I+N_C\)；\(\operatorname{diag}(0,1)\) |
| \(\rho\)-monotone \(A\) | \(\Leftrightarrow\) | \(\rho\)-comonotone \(A^{-1}\) | signed parameter | definition |
| \(\sigma\)-hypomonotone | \(\Leftrightarrow\) | monotone after \(+\sigma I\) |  | definition |
| \(\sigma\)-hypomonotone | \(\Rightarrow_s\) | LT-\(\tau\)-submonotone | \(\sigma<1/2,\ \tau=\sigma/(1-2\sigma)\) | strict witness: \(F(x)=-\sqrt x\), \(U=[0,1/16]\), \(W=\mathbb R\), sharp \(\tau_*=2\), no finite local hypo modulus at 0；[Luke–Tam Example 2](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863) + ALG sharpness |
| \((\mu,\rho)\)-semi \(A\) | \(\Leftrightarrow\) | \((\rho,\mu)\)-semi \(A^{-1}\) | same pointwise/all-pairs convention | [Evens et al. Def. 4.1](https://arxiv.org/pdf/2305.03605) |
| Otero \(\theta\)-semi | \(=\) | \((-\theta/2,-\theta/2)\)-semi | \(0<\theta<1\) | parameter identification |
| RL\(_{1,L\ge1}\) for \(\lambda A\) | \(=\) | LT-\(\tau\)-submonotone formula | \(\tau=(L^2-1)/4\) | Published finite-dimensional theorems retain their scope |
| RL\(_1\) | \(=\) | tied \((\mu_L,\rho_L)\)-semi | \(\rho_L=\lambda^2\mu_L\) | equations (3.1)–(3.2) |
| global RL\(_1\) | \(\perp\) | global RL\(_\gamma\), \(0<\gamma<1\) | unbounded domain | \(R=I\)；power-Hölder \(R\) |
| maximally cyclic | \(\Rightarrow_s\) | maximally monotone |  | nonzero skew rotation |
| \((n+1)\)-cyclic | \(\Rightarrow_s\) | \(n\)-cyclic | \(n\ge2\) | planar rotation thresholds；[Voisei, Example 43](https://arxiv.org/html/2411.04212v2) |
| paramonotone | \(\perp\) | rectangular | max monotone universe | [Bauschke–Wang–Yao 2012](https://arxiv.org/pdf/1201.4220) |
| VI monotone | \(\Rightarrow_s\) | VI pseudomonotone | single-valued same convention | positive nonmonotone scalar example |
| VI pseudomonotone | \(\Rightarrow_s\) | VI quasimonotone | same convention | \(x^2\) on \([-1,1]\) |
| Hilbert accretive | \(=\) | monotone | Riesz identification | Browder |
| Hilbert m-accretive | \(=\) | maximally monotone | standard range convention | Minty/Browder |
| prox-regular support geometry | \(\Rightarrow\) | attentive/value-truncated local hypomonotonicity | Hilbert algebra | converse只按 finite-dimensional theorem + proximal-subgradient等假设使用 |

需保留的 non-edges：

- maximality 与 strongness 正交；
- \(J_A\) contraction 不等于 strong monotonicity；
- 3-cyclic 与 3* / rectangular 无一般等价；
- VI pseudomonotone 与 Brézis pseudomonotone无无条件同一性；
- Spingarn、LTT 2017、LT 2025 的 submonotone节点不得合并；
- 一般 Banach中 maximal accretive与m-accretive、以及 reflected nonexpansiveness均不能照搬Hilbert结论。

### 4.2 Regularity / inverse stability

| From | 关系 | To | 假设 | strict witness / locator |
|---|---:|---|---|---|
| MR\((F)\) | \(\Leftrightarrow\) | Aubin\((F^{-1})\) | standard around definitions | exact moduli equal |
| MR\((F)\) | \(\Leftrightarrow\) | linear openness around | same balls | modulus reciprocal |
| MSR\((F)\) | \(\Leftrightarrow\) | calm\((F^{-1})\) | at reference | exact moduli equal |
| SMSR\((F)\) | \(\Leftrightarrow\) | isolated calm\((F^{-1})\) | at reference | exact moduli equal |
| SMSR | \(\Leftrightarrow\) | MSR + isolated reference solution |  | definition |
| SMR | \(\Leftrightarrow\) | MR + single-valued inverse localization | nearby targets | reference-fiber singleton不够 |
| SMR | \(\Rightarrow_s\) | MR |  | projection \(F(x_1,x_2)=x_1\) is MR not SMR |
| SMR | \(\Rightarrow_s\) | SMSR |  | \(F(x)=|x|\) is SMSR not SMR |
| MR | \(\Rightarrow_s\) | MSR |  | \(F=|x|\) MSR not MR |
| SMSR | \(\Rightarrow_s\) | MSR |  | \(F\equiv0\) MSR not SMSR |
| MR | \(\perp\) | SMSR | general multifunctions | \(F(x_1,x_2)=x_1\)；\(F=|x|\) |
| MR + SMSR | \(\not\Rightarrow\) | SMR | set-valued | \(F(x)=\{-x,x\}\) |
| Aubin | \(\Rightarrow_s\) | calm |  | \(t\sin(1/t)\) calm not Aubin |
| isolated calm | \(\Rightarrow_s\) | calm |  | constant interval map calm not isolated |
| Aubin | \(\perp\) | isolated calm |  | constant interval vs oscillatory single-valued |
| MR | \(\Rightarrow\) | UHREG | standard definitions | strictness witness仍待固化 |
| UHREG | \(\Rightarrow_s\) | HREG |  | \(F(0)=\{0,1/n\}\), \(F(x)=\{x\}\) for \(x\ne0\) |
| MSR | \(\perp\) | HREG |  | \(F=|x|\)；\(F(x)=\{x,x^2\}\) |
| MSR + HREG | \(\not\Rightarrow\) | MR |  | \(F(x)=\{x,0\}\) |
| \(q_2\)-MSR/SMSR | \(\Rightarrow_s\) | \(q_1\)-MSR/SMSR | residual convention；\(q_2>q_1>0\) | \(F_p(x)=\operatorname{sgn}(x)|x|^p\) |
| partial-uniform MR | \(\Rightarrow_s\) | full MR in product variable | standard product metric | converse fails for \(F(x,p)=p\) |
| Robinson stability | \(\Rightarrow\) | partial MSCQ | same constraint system | converse一般因缺uniformity失败；strict witness待B |
| transversality | \(\Rightarrow_s\) | subtransversality | standard set encoding | identical line sets |

对 strictly differentiable single-valued \(f\) 且 derivative range closed：MR iff derivative surjective，SMSR iff injective，SMR iff invertible；所以该子类中 MR + SMSR \(\Rightarrow\) SMR。不能外推到 general multifunctions。

### 4.3 Pending edges，不进入事实图

| 候选边 | 当前状态 | 需要什么 |
|---|---|---|
| RL 与 MR/MSR/SMSR 的任一普遍蕴含或互不包含 | **PENDING_VERIFICATION** | 同一 local/global convention 下的四象限显式对象与独立重算 |
| anchored RL、pointwise aFNE、all-pairs RL 的严格层级 | **PENDING_VERIFICATION** | 至少两个自然、可计算、branch量词完整的见证 |
| directional MR 的 zero-direction iff / every-direction implications | **PENDING_FULL_DEFINITION** | 逐字补入原文方向锥、cutoff、邻域与量词 |
| infinite-dimensional MR single-point coderivative iff | **PENDING_THEOREM_SELECTION** | 明确 \(G=F^{-1}\)、PSNC\((G)\)、mixed coderivative版本 |
| Spingarn mapping maximality与 resolvent convention | **PENDING_PRIMARY_FULLTEXT** | 1981/82 PPA 论文全文 |

---

## 5. 同名异义与参数 convention 警告

| 名称 | 不得静默合并的对象 |
|---|---|
| submonotone | Spingarn pointwise；Spingarn strictly；LTT 2017 anchored quadratic；LT 2025 two-point \(U,W\)-relative quadratic |
| weak monotonicity | all-pairs hypomonotonicity；weak Minty/star condition；函数 weak convexity；PDE/序理论其他概念 |
| cohypomonotone | global pairwise negative comonotonicity；Combettes–Pennanen local extension/maximality convention |
| semimonotone | Otero symmetric one-parameter；Evens two-parameter；complementarity matrices；PDE structures |
| comonotone | operator \(\rho\)-comonotonicity；概率论/经济学 random-variable comonotonicity |
| inverse strong monotonicity | RHS 系数 \(\alpha\)；以 reciprocal Lipschitz parameter 命名的 convention |
| pseudomonotone | VI sign implication；Brézis weak-topology sequential property |
| 3-monotone | 3-cyclic；3* / rectangular；其他少数 convention |
| strong regularity | modern SMR localization；Robinson generalized-equation strong regularity；Robinson stability |
| semiregularity | hemiregularity / fixed-\(x\) punctual property；其他书中同名性质 |
| Hölder / higher-order order | residual exponent \(q\)；distance-growth exponent \(p=1/q\) |
| gauge regularity | \(d(x,S)\le\varphi(r)\)；\(\psi(d(x,S))\le r\)；无可逆 gauge 时不可互换 |
| strong error bound | isolated local EB；global或uniform EB 的其他作者 convention |
| directional regularity | graph direction；output residual cone；relative-to-set |
| local maximality | local图本身无扩张；与某个global maximal extension局部一致 |

命名规则：先打印公式，再给名称；local至少区分 anchored、two-point neighborhood、\(U\times W\) graph restriction、global extension和relative-to-set；\(\lambda F\) 的参数不得无说明地复制给 \(F\)。

---

## 6. 初步二维 / partial-order map（仅作下一阶段工作假说）

当前事实不支持把所有节点压成一条“monotonicity strength”轴或一条“regularity strength”轴。更安全的坐标是多分量 signature：

| Graph geometry coordinates | 可能取值 |
|---|---|
| pairwise signed defect | strong / monotone / hypo；coco / cohypo；two-parameter semimonotone；scale-dependent RL |
| Cayley modulus | contraction / nonexpansive / Lipschitz expansive / Hölder / gauge |
| multi-point integrability | \(n\)-cyclic、cyclic、subdifferential representability |
| graph-wide refinements | paramonotone、rectangular；二者不可比 |
| closure / coverage | partial graph、maximality、full-domain resolvent |
| locality | anchored、two-point local、relative、global |

| Inverse stability coordinates | 可能取值 |
|---|---|
| target uniformity | MSR（fixed target）vs MR（nearby targets）vs semiregularity（fixed \(x\)） |
| isolation | ordinary vs strong / isolated |
| exponent / gauge | linear、Hölder、higher-order、incomparable gauges |
| parameter uniformity | at-reference、around、directional、relative、partial-uniform、Robinson stability |

核心 partial order 可概括为：

~~~mermaid
flowchart TD
  SMR["SMR"] --> MR["MR"]
  SMR --> SMSR["SMSR"]
  MR --> MSR["MSR"]
  SMSR --> MSR
  Q2["q₂-MSR, q₂>q₁"] --> Q1["q₁-MSR"]
~~~

以及 graph side 的多分支：

~~~mermaid
flowchart TD
  Strong["strong monotone"] --> Strict["strict monotone"]
  Strict --> Mono["monotone"]
  Coco["cocoercive"] --> Mono
  Cyclic["maximal cyclic"] --> MaxMono["maximal monotone"]
  RLsub["global RL, gamma<1"] -. scale-dependent .- Mono
~~~

虚线不是蕴含边；它表示 global unbounded 类不可排序、bounded/local window 又有不同方向的尺度关系。

如果后续需要二维可视化，建议把横轴暂定为 Cayley/graph defect signature，把纵轴暂定为 inverse stability signature，并把 maximality、multi-point integrability、locality作为点的标签，而不是强迫投影成单个实数。此图只是数据收集坐标；不构成“跷跷板存在”或“不存在”的结论。

---

## 7. 算法 theorem index（仅供后续进入原定理）

此表只索引 theorem-level evidence；不同 residual、不同 rate object、不同 selection/local-global 量词不得直接比较。

| ID | 算法 / graph geometry | regularity target | 结论入口 | 证据与限制 |
|---|---|---|---|---|
| PPA-01 | max monotone PPA | \(F\) MSR | local Q-linear distance；\(\lambda_k\to\infty\) distance-superlinear | [Leventhal, Theorem 3.1](https://arxiv.org/abs/0902.4200)，**IDX-V3**；正确 factor为 \(\bar\rho/\sqrt{\lambda_k^2+\bar\rho^2}\) |
| PPA-02 | relaxed max monotone PPA | \(F\) MSR | local Q-linear distance | [Shen–Pan, Theorem 3.1](https://arxiv.org/abs/1508.05156)，**IDX-V3** |
| PPA-03 | max monotone PPA | residual-exponent \(q\)-MSR | constant-step Hölder polynomial；\(q=1\) linear / growing proximal parameter superlinear | [Li–Mordukhovich, Theorems 7.2–7.3](https://optimization-online.org/wp-content/uploads/2012/02/3340.pdf)。Theorem 7.3(ii)–(iii) 的 \(\lambda_k=O(k^s)\) 与证明所用 lower growth冲突，标 **SOURCE-TYPO / PENDING_REPAIR**；在正式勘误或独立证明前不得作为 V3 rate。Proof-audited修正版应至少用 \(\Omega(k^s)\) 或 \(\Theta(k^s)\) 并明确不是原文逐字陈述 |
| PPA-04 | generalized implicit PPA，无 monotonicity | MR 或 SMSR | existence-selected local linear/superlinear | [publisher page](https://www.esaim-proc.org/articles/proc/abs/2007/02/proc071701/proc071701.html)，降为 **V1 / PENDING_SOURCE_CAPTURE**；恢复V2前需取得 Theorems 3.1/4.2全文与量词 |
| PPA-05 | local maximal LT-submonotone PPA | \(F\) MSR，uniform relevant zeros | local R-linear；coupling \(\tau(1+\bar\rho/\lambda)^2<1/2\) | [Luke–Tam, Assumption 2, Theorem 2, Corollary 1](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)，**IDX-V3**；有限维、restricted branch |
| FXP-01 | pointwise almost averaged fixed-point map | \(\Phi=T-I\) MSR | local linear；\(c^2=1+\varepsilon-(1-\alpha)/(\alpha\kappa^2)<1\) | [Luke–Thao–Tam, Theorem 2.15 and Corollary 2.19](https://arxiv.org/abs/1605.05725)，**IDX-V3** |
| FB-01 | max monotone + cocoercive forward–backward | \(A+C\) MSR | local Q-linear distance | [Shen–Pan, Theorem 3.2](https://arxiv.org/abs/1508.05156)，**IDX-V3** |
| FB-02 | local hypo/submonotone nonconvex FB | \(T_{\rm FB}-I\) MSR, uniform in step | local linear | [Luke–Thao–Tam, Proposition 3.21 and Theorem 3.24](https://arxiv.org/abs/1605.05725)，**IDX-V3** |
| PG-01 | convex prox-gradient | prox-gradient EB | objective Q-linear、iterates R-linear | [Drusvyatskiy–Lewis, Theorems 3.2–3.3](https://arxiv.org/abs/1602.06661)，**IDX-V3** |
| PG-02 | convex linesearch FB | \(\partial(f+g)\) MSR | iterates Q-linear | [Bello-Cruz–Li–Nghia, Proposition 4.1 and Theorem 4.2](https://arxiv.org/abs/1806.06333)，**IDX-V3** |
| DR-01 | two max monotone + one Lipschitz component | \(A+B\) MSR | local Q-linear shadow distance | [Shen–Pan, Theorem 3.3](https://arxiv.org/abs/1508.05156)，**IDX-V3**；不覆盖 pure PRS endpoint |
| DR-02 | convex DR/ADMM | branch (i) strong convexity+cocoercivity；或 branch (ii) \(I-T\) MSR | 同一问题框架的两条 local-linear sufficient branches | [Aspelmeier–Charitha–Luke, Theorems 1.6 and 2.3](https://arxiv.org/abs/1508.04468)，**IDX-V3**；是候选替代机制，不是必要trade-off |
| DR-03 | manifold / linear-quadratic almost-firm DR | \(T_{\rm DR}-I\) MSR relative to affine set | local linear | [Luke–Thao–Tam, Theorem 3.33](https://arxiv.org/abs/1605.05725)，**IDX-V3** |
| PRS-01 | one term strongly convex + smooth | 无 EB | global contraction，覆盖 pure PRS | [Davis–Yin, Theorem 4.1](https://arxiv.org/abs/1407.5210)，**IDX-V3**；与DR-local-EB结果不是同量词 |
| FBF-01 | max monotone + cocoercive/Lipschitz pieces；conditioned metric | full inclusion MSR | local Q/R-linear；FBF/extragradient specializations | [Giselsson, Theorems 3–4](https://arxiv.org/abs/1908.07449)，**IDX-V3**；存在第三轴 metric conditioning |
| AP-01 | elemental set geometry / almost averaged projections | subtransversality-type product mapping regularity | local linear cycles/fixed points | [Luke–Thao–Tam, Theorem 3.14](https://arxiv.org/abs/1605.05725)，**IDX-V2**；长 product definitions需回原文 |
| NEW-01 | generalized Newton，无 monotonicity | strong (power) subregularity | conditional superlinear / order | [Cibulka–Dontchev–Kruger, Theorems 6.1–6.3](https://arxiv.org/abs/1701.02078)，**IDX-V3**；不自动给step存在唯一性 |
| NEW-02 | semismooth Newton | all linearizations SMSR | conditional superlinear | [same source, Theorem 6.4](https://arxiv.org/abs/1701.02078)，**IDX-V3** |
| KL-01 | composite descent，无operator monotonicity要求 | Luo–Tseng EB \(\Rightarrow\) KL-\(1/2\) | prox-gradient / iPiano local linear | [Li–Pong, Theorem 4.1, Proposition 5.1, Theorem 5.1](https://arxiv.org/abs/1602.02915)，**IDX-V3** |

禁止跨表误比：

1. \(F\)、\(A+B\)、\(T-I\)、prox-gradient residual与set-intersection mapping的MSR不是同一性质；
2. objective Q-linear、distance Q-linear、iterates R-linear、residual linear不是同一rate object；
3. existence-selected sequence与all legal selections不同；
4. local、relative与global contraction不同；
5. sufficient compatibility式不等于sharp或necessary trade-off curve；
6. 用户RL-PPA的(3.10a)–(3.12)目前是代数入口，不进入verified theorem index；
7. B catalog 的 CP-01 / CP-02 是反向校准的 example constructions，不是算法 theorem 或 primary-source 条目；它们保持在 example/C-stage 流程，不进入本算法 index 或来源 ledger。

---

## 8. 核心来源 locator（去重入口）

| 主题 | Primary / authoritative locator | 本稿使用范围 |
|---|---|---|
| maximal monotone / resolvent | [Minty 1962](https://projecteuclid.org/journals/duke-mathematical-journal/volume-29/issue-3/Monotone-nonlinear-operators-in-Hilbert-space/10.1215/S0012-7094-62-02933-2.short)；[Bauschke–Moffat–Wang 2011](https://arxiv.org/pdf/1101.4688) | full-domain、FNE、strong/coco/paramono/rectangular/cyclic |
| signed mono/comono | [Bauschke–Moursi–Wang 2019](https://arxiv.org/pdf/1902.09827) | \(\rho\)-mono/comono、conical averagedness |
| two-parameter semimonotonicity | [Evens et al., Definition 4.1 / Proposition 4.12](https://arxiv.org/pdf/2305.03605) | definitions、inversion/scaling、resolvent range |
| symmetric semimonotonicity | [Otero–Iusem, 2010 report / 2011 publication](https://webdoc.sub.gwdg.de/ebook/serien/e/IMPA_A/672.pdf) | \(\theta\)-slice、transform |
| LT submonotonicity | [Luke–Tam, Definition 2 / Propositions 3–5 / Example 2, equations (19)–(21)](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863) | finite-dimensional restricted graph、R characterization；\(-\sqrt x\) 的 \(U=[0,1/16]\)、\(W=\mathbb R\)、printed \(\tau=2\) |
| finite cyclic hierarchy | [M. D. Voisei, General monotonicity, Example 43](https://arxiv.org/html/2411.04212v2) | planar rotation iff threshold \(|\theta|\le\pi/n\)；不得误归因给 Bauschke et al. |
| Spingarn definitions | [Spingarn 1981](https://www.jstor.org/stable/1998411)；[Zajíček 2008](https://www.heldermann-verlag.de/jca/jca15/jca0651_b.pdf) | anchored vs strictly-two-point naming |
| prox-regularity | [Poliquin–Rockafellar 1996](https://doi.org/10.1090/S0002-9947-96-01544-9)；[full treatment](https://www.heldermann-verlag.de/jca/jca17/jca0849_b.pdf) | finite-dimensional converse与local proximal map |
| MR / openness / Aubin | [Ioffe survey, Proposition 2.2](https://arxiv.org/pdf/1505.07920)；[Dontchev–Quincampoix–Zlateva](https://www.heldermann-verlag.de/jca/jca13/jca0526_b.pdf) | metric-space equivalence、Banach derivative criteria |
| SMSR | [Cibulka–Dontchev–Kruger](https://arxiv.org/html/1701.02078v1) | definitions、inverse isolated calm、derivative/coderivative |
| nonlinear / gauge MSR | [Kruger](https://arxiv.org/html/1502.06159v2) | exact rates、slope、gauge |
| higher-order MSR | [Mordukhovich–Ouyang](https://arxiv.org/html/1507.04825v1) | residual exponent任意 \(q>0\) |
| set regularity | [Kruger–Luke–Thao](https://arxiv.org/html/1611.04787v2) | subtransversality / transversality |

### 8.1 Atlas acceptance / unresolved ledger

- 核心定义、Cayley 字典、\(\gamma=1\) RL 换参、核心 MR/MSR/SMR/SMSR 等价及有限维 derivative/coderivative 边：**PROVISIONAL_PASS_FOR_DOWNSTREAM_RECOMPUTATION**。
- PPA-03 growth-step branches：**BLOCKED AS VERIFIED RATE**，已按 source internal inconsistency 降级。
- PPA-04：**PENDING_SOURCE_CAPTURE**，不承载精细 theorem 量词。
- Spingarn mapping/maximality、directional完整定义、infinite-dimensional mixed-coderivative版本、RL–regularity四象限：均显式 pending。Hypomonotone-to-LT strictness 已由 Luke–Tam \(-\sqrt x\) 例核实，不再列 pending。
- 本稿没有作任何 seesaw synthesis；所有 cross-axis判断留给 B/C 数据与最终 integrator。

---

## 9. 供 Subagent B 读取的 gap-pair queue

下表的任务不是再证明一条 implication，而是尽可能填满 \(A\wedge B\)、\(A\wedge\neg B\)、\(\neg A\wedge B\)、尤其 \(\neg A\wedge\neg B\)，并为每个对象保留 graph、inverse、resolvent、zero set与参数。

| 优先级 | Gap pair / phase gap | 必填逻辑区域 | 首选显式 seeds | B 的最低交付 |
|---:|---|---|---|---|
| 1 | all-pairs RL\(_\gamma\) vs MSR / SMSR / MR | 四象限；local与global分开 | \(F=0\)；linear slopes \(cx\)；power maps；Cayley power-Hölder graph；normal cones | 每象限至少两个本质不同对象；不得用“坐标不同”代替反例 |
| 2 | RL\(_1\) vs RL\(_{\gamma<1}\) | global四区；bounded/local strictness | \(R=I\)、\(R=P_\gamma\)、bounded \(R=2I\)、\(R=0\) | sharp Hölder/Lipschitz exponent与domain diameter依赖 |
| 3 | anchored solution-relative RL vs pointwise aFNE vs all-pairs RL | 所有单向缺口 | 构造branch crossing、只在zero fiber良好的图 | 明确base点量词、restricted graph和resolvent selections |
| 4 | hypomonotone vs LT-submonotone | strict implication 已核实；继续填两者皆满足、hypo非LT、两者皆非及多样化对象 | verified LT Example 2 \(-\sqrt x\)；线性 \(-kx\)；critical \(-x^2\)；inverse family | 保留 canonical witness 的 \(U=[0,1/16]\)、\(W=\mathbb R\)、sharp \(\tau_*=2\)、non-hypo proof；再补不同机制对象，不重复计同一restriction |
| 5 | strong monotone vs cocoercive | 四象限 | \(\mu I+N_C\)、diag\((0,1)\)、skew+shift、zero | exact moduli、single/multivalued与inverse |
| 6 | \(J\) contraction vs strong \(A\) vs strong \(A^{-1}\) | 三属性全部可行区域 | rotations、SPD、normal-cone shift、diagonal maps | \(J,R\) exact operator norms与inner products |
| 7 | paramonotone vs rectangular | 四象限且max monotone | BWY skew+\(N_B\)、\(\ell^2\) diagonal+skew、Volterra、subdifferential | 把文献对象改写成可复核独立条目；至少一个有限维和一个无限维 |
| 8 | \(n\)-cyclic vs \((n+1)\)-cyclic vs rectangular | adjacent strict gaps与cross gaps | rotations \(R_\theta\)、subdifferentials、skew maps | exact threshold与3-cyclic/3*防混淆 |
| 9 | Spingarn pointwise vs strictly submonotone vs LT | anchored-only、two-point-only、neither | scalar cusps、locally bounded multifunctions、LT examples | 先取得/核对定义量词；1981/82 maximality仍pending时不得补猜 |
| 10 | MR vs SMSR vs SMR | 四象限及 MR+SMSR-not-SMR | \(F=|x|\)、projection \(x_1\)、\(F=\{\pm x\}\)、\(F=0\) | exact moduli；single/set-valued各一套 |
| 11 | MSR vs HREG / UHREG | 四象限及 conjunction failure | \(F=|x|\)、\(\{x,x^2\}\)、\(\{x,0\}\)、\(F(0)=\{0,1/n\}\) | 完整邻域量词、closedness、exact/asymptotic ratios |
| 12 | Aubin vs isolated calm | 四象限 | constant interval、\(t\sin(1/t)\)、linear bijection、bad multifunction | inverse-side图和exact modulus |
| 13 | residual exponent \(q_2\) vs \(q_1\)；incomparable gauges | strict hierarchy与neither | \(F_p=\operatorname{sgn}(x)|x|^p\)、log/oscillatory gauges | sharp exponent、exact modulus、gauge domination test |
| 14 | at-reference MSR vs MSR around / Robinson stability | pointwise-only与uniform | modulus blow-up families、parametric constraints | 展开统一邻域/统一modulus失败机制 |
| 15 | local/bounded/global set linear regularity | 各strict gap | lines/subspaces、convex sets、infinite-dimensional subspaces、nonconvex tangencies | set mapping编码、transversality/subtransversality modulus |
| 16 | prox-regularity vs truncated / untruncated normal hypomonotonicity | truncation必要性与converse条件 | \(S^1\)、\(f=-|x|\) at \((0,1)\)、smooth manifolds | proximal-subgradient、attentive level与normal bound全部打印 |
| 17 | maximality vs strong graph inequality | 两轴四区 | graph singleton、restricted \(\mu I\)、\(N_C\)、\(\mu I+N_C\) | maximal extension与range分开验证 |
| 18 | strong graph geometry with weak regularity；weak graph geometry with strong regularity | cross-phase cloud四象限 | skew invertible map、singular PSD、\(\partial|x|\)、normal cones、nonmonotone bijections | 同一reference处同时计算 inner product、RL、MR/MSR/SMSR |
| 19 | algorithmic residual mismatch | \(F\)-MSR vs \(T-I\)-MSR vs prox-gradient EB | low-dimensional linear/quadratic models | 不做theorem综述；构造同一问题下 residual properties可分离的对象 |
| 20 | RL–power MSR sharp composition | 达到或严格优于 \(r_{k+1}\asymp r_k^{\gamma q}\) | Cayley power map + scalar residual profile；isolated与nonisolated zeros | 验证所有local branch/invariance条件；区分ALG上界与sharp rate |

B 读取规则：任何使用 **PENDING** 边的条目必须把“待核实内容”留在证明栏；不得把候选 seed 的标签当作已经验证的性质。所有例子最终仍须交给 C 独立重算。
