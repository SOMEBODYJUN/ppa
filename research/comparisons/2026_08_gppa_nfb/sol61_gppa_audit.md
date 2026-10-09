# GPPA v1 的第二轮独立敌对审查

日期：2026-10-09。角色：`gpt-6.1-sol` / `ultra` 的 GPPA 独立审查；不投票，不以此前 `PASS` 或 `derived-checked` 标记代替证明。

**事实裁决：C199 的真实物理轨道重合成立；C200-v1 的任意 ASM 核同轨道排除成立。没有找到使这些限定命题失败的致命异议。现有报告的一处重要未闭边界可以加强：完整 cap、C141 指定片及 C10 的同轨道排除实际上只需任意单值核的完整 pair monotonicity，不需 ASM，也不需核连续性。** 本次新加强在 §5 给出完整证明，初次提交时为候选；随后对 [root 的 C204 正文](pair_monotone_barrier.md) 和另一独立审查重构完成交叉核验，没有发现断点，见 §10。本文件不改 C200-v1、不登记新 Claim、不更改中央文件。

**更近的间接覆盖也成立：只删 cap 的负支、保留完整相同零集和全部非负法向输入普通纤维后，可以让源 Theorem 2 证明指定原 cap 普通选择的物理收敛与有限长度，见 §11。** 所以 C204 是“同完整原 F 的核表示障碍”，不是“既有 GPPA 理论不能间接证明该原选择结论”的证据。

随后对 [保零集分支报告](sol61_branch_restriction.md) 实际落盘稿逐项独立核验：cap 的更简单核、C141 小 collar 的 ASM 尾核以及 C10 a>1 的 mere-monotone Dini 尾核均成立，见 §12。它们都能导入明定原选择的物理收敛；因此用这些完整图障碍单独承担收敛结论的新颖性，证据不足。

## 1. 阅读顺序、对象和证据

先读取根 `README.md`、`RESEARCH_STATE.md`、`CLAIMS.md` 的 C199–C203 及 F49/F51/F53，再直接抽取并阅读 GPPA 固定 PDF 全部14页，独立重建 Theorem 1/2、Lemma 3、Theorem 4。随后读取 C02-v2、C09/C10/C11、C137、C141、C191–C193 的规范证明，才核对 `gppa_review.md`、`COMPARISON.md`、`independent_attack.md` 的相关公式。另读 C03/C04/C18/C19/C20-v2 的规范对象和主结论，防止把收敛子类重合扩成结构稿重复。本篇不承担 NFB 原文的全部独立审查；C201–C203 已读取，下面只核其与 GPPA/lift 量词的边界。

在仓库与工作区可见文件清单中查找 `AGENTS.md`，没有发现。只写本文件和专名 `sol61_gppa_check.py`、`sol61_gppa_results.json`，没有 commit/push。

固定一手原文是 [GPPA 2608.01584v1 PDF](sources/gppa_2608.01584v1.pdf)，SHA-256 为 `5f07147a258e441193dd918452909ddc2fec8781257d6005348f233016653e91`。本次独立算出的哈希与 [manifest](sources/manifest.json) 一致。2026-10-09 直接打开 [arXiv 固定版本页面](https://arxiv.org/abs/2608.01584v1)，页面仍只列 v1，提交时间为 2026-08-03 01:37:27 UTC；PDF p.1 的稿内日期为 August 4, 2026。本文全部原文页码是 PDF 印刷页码，和文件页序一致。

外部步长记为 \(h>0\)，本库普通 PPA 步长记为 \(\lambda>0\)。ASM 常数记为 \(\varepsilon>0\)，Theorem 4 的正则化参数另记 \(e>0\)，避免把它们或 RL 指数混合。

## 2. 原文的全部结果，不跳过弱核和 inexact 分支

原文 p.2 Eq.(5)–(6)、p.5 Definition 4 是

\[
J^v_{hF}(x)=(hF+v)^{-1}(v(x)),\qquad
v(x_k)-v(x_{k+1})\in hF(x_{k+1}). \tag{A1}
\]

核 \(v:H\to H\) 单值且全域，允许非线性和非单射。Definition 4 明列 \(\operatorname{ran}v\subseteq\operatorname{ran}(hF+v)\)。这不是普通 Minty coverage。

原文 p.4 Definition 1 及 p.5 Definition 3 按完整集合值的 all-pairs 量词分别要求

\[
\langle f-g,v(x)-v(z)\rangle\ge0,\qquad
\langle f-g,v(x)-v(z)\rangle\ge\varepsilon\|v(x)-v(z)\|^2
\quad((x,f),(z,g)\in\operatorname{gph}F). \tag{A2}
\]

不能只在零锚或实际轨道所选值上核验。ASM 的右端是核差，原文 p.5 Definition 2 的传统 pair strong monotonicity 右端则是原变量差。

| 结果及精确原文定位 | 完整前件与结论 | 重建与比较裁决 |
| --- | --- | --- |
| Theorem 1(a), p.6 | 非空 \(S=\operatorname{zer}F\)、pair monotone、coverage；每条合法 GPPA 轨道核增量趋零 | 对零锚 \(s\) 的极化给 \(\|v(x_{k+1})-v(s)\|^2+\|v(x_{k+1})-v(x_k)\|^2\le\|v(x_k)-v(s)\|^2\)。求和即得核步平方可和，因此步差趋零。没有物理步可和。 |
| Theorem 1(b), p.6 | 另加图关于图值 strong、位置 weak 的闭性；每个物理弱聚点在 S | A1 的选中图值趋零，沿任意弱收敛子列直接用闭图。并不保证聚点存在、唯一或全轨道点收敛。 |
| Theorem 1(c), p.6 | 另加 \(F^{-1}\) 在0 R-continuous；\(d(x_k,S)\to0\) | 选中值最终进入 Definition 5 的残差窗，逆像包含给距离趋零。非单射核仍不控制纤维内物理选择。§5 候选加强说明，不能因此让完整 cap 的指定普通轨道成为该 theorem 的轨道。 |
| Theorem 2(a), pp.7–8, Eq.(11) | 非空 S、ASM、coverage；对每个零锚，核误差平方因子 \((1+2h\varepsilon)^{-1}\)，核步平方由降幅控制 | §3 独立重建。原文的量纲和符号正确；无隐藏核连续/可逆前件。 |
| Theorem 2(b), p.7 statement / p.8 proof | 另加 \(F^{-1}\) 在0 R-Lipschitz；集合距离 R-linear 上界 | 最终 \(d(x_{k+1},S)\le(L/h)\|v(x_k)-v(x_{k+1})\|\)。不是每步距离 Q-linear 比值，也不是物理点范数率。 |
| Remark 3, p.8 | 物理轨道有界且 \(H=\mathbb R^n\) | 闭包紧，可固定一个 K，在 Definition 6 的 compactly R-Lipschitz 条件内替代普通 R-Lipschitz。无限维有界不够。 |
| Lemma 3, pp.8–9 | pair monotone；\(x_1\in\operatorname{zer}F\)、\(x_2\in\operatorname{zer}(F+ev)\) | \(\|v(x_2)\|\le\|v(x_1)\|\)。直接由两个图值配对得到。取全部 \(x_1\) 后可取 inf；不需极小点存在。原文没有 Theorem 3。 |
| Theorem 4, pp.9–11, Eq.(12) | pair monotone、全局 L-Lipschitz 核、原及正则化零集非空、原逆像 R-continuous、足够小 e；对 \(F+ev\) 的合法 IGPPA，物理加性误差上界 \(\delta=e^2\) | 只给到原零集的 limsup 邻近界及一族可行 e 问题的双极限0。§6 重建现有修复。不是固定 e 的点收敛，不是一条变化 \(e_k\) 的轨道。 |
| Remark 4, p.12 | L>0 时可将核除以 L 使其 Lipschitz 常数为1 | 保持 pair monotonicity 的确成立；若还要保持算法身份，必须重标步长：\(J^{v/L}_{hF}=J^v_{LhF}\)。正则化 \(F+e(v/L)\) 的参数也改变。不能归一化后原样搬用物理步长及误差常数。 |

Definition 5，p.5 Eq.(10)，要求 \(F^{-1}(f)\subset S+\rho(\|f\|)B\) 对所有小 \(f\) 成立；这包括整个空间所有完整逆像，不只是一个零点附近的实际输出。在无限维、非闭或非 proximinal S 上，距离估计和实际闭球和集包含也须区分。本文明确例的 S 是 Euclidean 闭平面，最近点取得，故无此问题。高阶连续 EB gauge 在小残差窗内可以给 R-Lipschitz；“EB 指数大于1”不是排除 Theorem 2(b) 的理由。

## 3. Theorem 2 的独立证明与无物理桥的边界

令 \(z_k=v(x_k)-v(s)\)，\(s\in S\)。A1 的实际选中值与零图值代入 ASM 得

\[
\langle z_k-z_{k+1},z_{k+1}\rangle\ge h\varepsilon\|z_{k+1}\|^2.
\tag{A3}
\]

极化恒等式给源 p.7 的两项估计：

\[
(1+2h\varepsilon)\|z_{k+1}\|^2+
\|v(x_{k+1})-v(x_k)\|^2\le\|z_k\|^2. \tag{A4}
\]

因此核误差及核步差 R-linear。又由 Cauchy，可用更强因子

\[
\|z_{k+1}\|\le(1+h\varepsilon)^{-1}\|z_k\|. \tag{A5}
\]

这与 `gppa_review.md` GR4–GR6、`independent_attack.md` §6 一致。两个零图值代入 ASM 还给 \(v(s)=v(s')\) 对全部 \(s,s'\in S\) 成立。若普通 \(J_{\lambda F}(s)=\{s\}\) 而 S 非单点，所有 S 都属于 \(J^v_{hF}(s)\)，故完整算法纤维不可能逐输入相等。这不阻止某条指定选择。

C197 的反例也直接成立：\(F(x_1,x_2)=v(x_1,x_2)=(x_1,0)\)，\(h=\varepsilon=1\)，warped 纤维是 \(\{x_1/2\}\times\mathbb R\)。合法轨道 \(x_k=(2^{-k},(-1)^k)\) 的核和集合距离几何趋零，物理步至少2，无点极限、无有限长。它不反驳源 theorem，只反驳擅自增加物理结论。

反过来，若已有物理点尾 \(\|x_k-x_*\|\le M r^k\)，\(0<r<1\)，则

\[
\sum_{j\ge k}\|x_{j+1}-x_j\|
\le \frac{M(1+r)}{1-r}r^k. \tag{A6}
\]

故 GPPA 在能反演物理点率的同轨道子类内，有限长度已经随附，不能另作相对于它的创新主张。

## 4. C199：全部边界保留后的真实重合

取 \(a,c,\lambda,h>0\)、\(0<\alpha<1\)，完整关系

\[
F(t,y)=\{(-cy^\alpha,ay+n):n\in N_{\mathbb R_+}(y)\}\quad(y\ge0),
\qquad F(t,y)=\varnothing\quad(y<0). \tag{A7}
\]

完整边界 \(F(t,0)=\{0\}\times(-\infty,0]\) 保留。设

\[
q=(1+\lambda a)^{-1},\quad K=\frac{\lambda c q^\alpha}{1-q^\alpha},\quad
w=\frac h\lambda,
\quad v(t,y)=w(-K(y_+)^\alpha,y_+). \tag{A8}
\]

这是 C191 的合法单点支撑数据；普通完整近端唯一且全域，

\[
T(t,y)=(t+\lambda c(qy_+)^\alpha,qy_+). \tag{A9}
\]

独立检查四个承重门如下。

1. **完整 ASM。** 对正法向两点，配对为 \(w[cK(\Delta y^\alpha)^2+a(\Delta y)^2]\)。正点与边界 n≤0 比较时，额外正常项 \(-wny\ge0\)。两边界核差0。故 \(\varepsilon=\min\{\lambda c/(hK),\lambda a/h\}>0\) 对完整图 all-pairs 成立；域外 F 空不产生义务。
2. **warped 全纤维与 coverage。** 正法向方程给 \(z=qy_+\)，切向方程因 K 定义自动满足，t 自由。输入 y≤0 时 v=0，任何正输出 z>0 的正常分量 \((ha+w)z>0\) 不可能，故 z=0、n=0、t 自由。因此恰有 \(J^v_{hF}(t,y)=\mathbb R\times\{qy_+\}\)。这证明全部输入 coverage 及全部普通物理轨道包含，且证明两个完整算法不相等。
3. **原逆像门。** y>0 的每个图值正常分量是 ay，故 \(y\le\|f\|/a\)；边界距离0。投影 \((t,0)\) 给 Definition 5 的实际包含，\(F^{-1}\) 全局 R-Lipschitz 常数 \(1/a\)。
4. **物理结论桥。** y₀≥0 时，一步 A9 已给 \(I=t_k+Ky_k^\alpha=t_0+Ky_0^\alpha\)。预先固定 \(x_*=(I,0)\in S\)，于是 \(v(x_k)-v(x_*)=w(x_k-x_*)\)。A4 或 A5 直接推出同一物理点 R-linear 及 A6 的有限长；没有先使用收敛来定义锚。y₀<0 的第一步普通输出是 \((t_0,0)\)，以后驻定；它在 warped 算法内可以选择边界图值0，而普通首步所选图值是 \((0,y_0/\lambda)\)。物理序列相同，不需两算法首步所选图值也相同。

严格 RLEB 门也独立满足。完整反射在输入对尺度 R 可取

\[
L_R=R^{1-\alpha}+2\lambda c q^\alpha,\qquad
\psi(s)=(s/c)^{1/\alpha},\qquad
\kappa_R=\left(q^\alpha+\frac{R^{1-\alpha}}{\lambda c}\right)^{1/\alpha}.
\tag{A10}
\]

选 \(R^{1-\alpha}<\lambda c(1-q^\alpha)\)，则 \(\kappa_R<1\)。完整真残差至少 \(cy^\alpha\)，全域 gauge 可评价；最近零锚、完整单点纤维和全空间留域都已在同对象核验。具体 \(\alpha=2/3,a=7,c=2,\lambda=1,h=3/10,R=1/8\) 给 \(K=2/3,\varepsilon=10,L_R=3/2,\kappa_R=1/(2\sqrt2)\)。完整 F 非单调，T 零法向非 calm；这两种标签没有排除 GPPA。

**范围判定：** `gppa_review.md` §5、`COMPARISON.md` §3 和独立攻击 §3 所说的物理重合成立。仅用源 theorem 自动得到任意 warped 选择物理收敛则不成立；这里不可省去普通选择的不变量。标题“带任意非单射核”仍宜改为“带显式非线性非单射核”。一般 C191/C192 原数据的全部核分类没有由这个例关闭。

## 5. C200 及新的弱核加强候选

### 5.1 原 C200-v1 证明没有断点

C137 的完整定义是 [GC-1](../../canonical/selection_geometric_cap.md#gc-object)。在 \(\eta\le0\) 片上，

\[
f_+(y)=(-2\sqrt y,0,3y),\qquad f_-(y)=(-2\sqrt y,0,-5y).
\tag{A11}
\]

同 y 同支相同图值，ASM 确实迫使整个核在切向片上常值，写作 V(y)。同支比较再给 \(\|V(y)-V(z)\|\le\varepsilon^{-1}\|f_+(y)-f_+(z)\|\)。在任意 \([a,b]\subset(0,\infty)\) 上是 Lipschitz，而不是偷加核正则性。两次跨支比较给 \(|V_3(y)-V_3(z)|\le C_a|y-z|^2\)，细分相加迫使 V₃ 恒定。A1 的正常更新必须是 \(h\cdot3y_{k+1}\) 或 \(-h\cdot5y_{k+1}\)，两者非零，所以指定普通轨道不能表示。证明不使用 coverage；另选完整另一支没有逃口。

GC-2–GC-6 给同一完整近端全部唯一纤维、完整真残差和严格 RLEB；\(R=1/16\) 的兼容数 \((2\sqrt2+5/8)^2/16\approx0.7453849316<1\)。初值 \((0,-1,1/64)\) 的普通轨道保持 \(\eta=-1\)、\(y_k=4^{-k}/64\)、\(\xi_{k+1}-\xi_k=\sqrt{y_k}\)。这是正面 RLEB 定理结论成立的完整对象，随后才证明它不满足任何保持同轨道的 GPPA ASM 表示。

### 5.2 新候选：mere pair monotonicity 已经足够

以下量词比 C200-v1 强。这里不预设 v 连续、可测、局部有界、可微、单射、Lipschitz 或 ASM。

**候选引理 M-CAP。** 令 \(I\subset(0,\infty)\) 是任意非空开区间，\(W\subset\mathbb R^2\) 是任意非空切向集合。完整图在 \(W\times I\) 包含 A11 的两支。对任何单值 \(v:W\times I\to\mathbb R^3\)，若 A2 的第一式对这个片内所有两个完整图点（两支任意搭配）成立，则 v₃ 在 \(W\times I\) 上是一个常量。因此任意相邻物理点 \(x,x'\in W\times I\) 都不可能满足 \(v(x)-v(x')\in hF(x')\)，\(h>0\)，只要 x' 处完整 F 正是 A11 的两值。

**第一步，仅折叠正常分量。** 固定 y∈I、任取 p,p'∈W，比较 \(((p,y),f_+(y))\) 与 \(((p',y),f_-(y))\)，又交换两支而不交换位置，得到

\[
8y[v_3(p,y)-v_3(p',y)]\ge0,
\qquad -8y[v_3(p,y)-v_3(p',y)]\ge0. \tag{M1}
\]

故 v₃ 与 p 无关，记为 b₃(y)。这里不能声称整个 v 折叠；mere monotonicity 在同支相同图值上只给0≥0。

**第二步，获得标量切向分量的单调性。** 固定任意 p₀∈W，记 \(b_1(y)=v_1(p_0,y)\)。对 y,z∈I，设

\[
d=b_3(y)-b_3(z),\quad D=b_1(y)-b_1(z),\quad
s=\sqrt y-\sqrt z,\quad A=3y+5z>0,\quad B=5y+3z>0.
\]

两次完整跨支比較严格是

\[
Ad\ge2sD,\qquad -Bd\ge2sD. \tag{M2}
\]

将第一式乘 B、第二式乘 A，相加消去 d，得到

\[
0\ge2(A+B)sD. \tag{M3}
\]

因此 y>z 时 D≤0，b₁ 在 I 上非增。这个推导不要求同支 Lipschitz 控制；单调性来自加权的**跨支**配对。核第二分量完全不参与 A11 的配对。

**第三步，利用有限总变差细分，不假定没有跳跃。** 固定任何 \([a,b]\subset I\)，a>0。在 M2 中按 d 正负选正常项不利的一式，得

\[
\min(A,B)|d|\le2|s|\,|D|.
\]

因为 \(\min(A,B)\ge8a\)、\(|s|\le|y-z|/(2\sqrt a)\)，

\[
|b_3(y)-b_3(z)|\le\frac{|y-z|\,|b_1(y)-b_1(z)|}{8a\sqrt a}
\quad(y,z\in[a,b]). \tag{M4}
\]

令 \(y_j=a+j(b-a)/N\)。三角不等式、M4 及 b₁ 的非增性给

\[
\begin{aligned}
|b_3(b)-b_3(a)|
&\le\frac{b-a}{8a\sqrt a\,N}
\sum_{j=0}^{N-1}|b_1(y_{j+1})-b_1(y_j)|\\
&=\frac{(b-a)[b_1(a)-b_1(b)]}{8a\sqrt a\,N}\longrightarrow0.
\end{aligned} \tag{M5}
\]

端点值是有限实数，故总变差有限；即使 b₁ 在网格点有任意跳跃，最后一个等号仍是有限和的精确望远镜恒等式。没有交换不当极限，也没有隐含连续性。每个正紧子区间的端点正常值相同，故 b₃ 在连通 I 上恒定，M1 再给整个片的 v₃ 恒定。引理成立。

**同轨道结论的全部量词。** 对 C137，选 W 为包含轨道切向点的 \(\eta\le0\) 片、I=(0,∞)。任何全域单值核只要与完整 F pair monotone，其限制满足引理；沿任意正法向普通轨道，A1 左边正常分量0，而右边只能从 \(h\{3y_{k+1},-5y_{k+1}\}\) 中选。这排除任意 h>0、任意核、允许每步另选完整另一支；coverage 和逆像正则性都无法补救。故源 **Theorem 1**（p.6）的同原图同普通轨道表示也被排除。原文的 Theorem 1 没有被反驳，因为所需 pair-monotone 表示并不存在。

### 5.3 仅在标量严格递增共同剖面上推广

以上加强可推广到

\[
f_+(y)=(-c\phi(y),0,\ldots,0,a(y)),\qquad
f_-(y)=(-c\phi(y),0,\ldots,0,b(y)),\quad c>0,\ a(y)>0>b(y),
\tag{M6}
\]

其中 I 为连通正区间，\(\phi\) 严格递增且在每个正紧区间 Lipschitz，a,b 连续。图值与切向位置无关；v 为任意单值 pair-monotone 核。固定 y 两支差强迫正常分量切向无关。跨支系数 \(A=a(y)-b(z)>0\)、\(B=a(z)-b(y)>0\)，同样加权消去正常差给 \([\phi(y)-\phi(z)]\Delta v_1\le0\)，所以 v₁ 非增。紧区间上 A、B 的正下界及 \(\operatorname{Lip}\phi\) 给 \(|\Delta v_{\rm normal}|\le C|y-z||\Delta v_1|\)，M5 相同。**不推广到任意向量值共同 H(y)**，因为 \(\langle\Delta H,\Delta v_{\rm tangent}\rangle\le0\) 不能直接给各坐标有限总变差。

* C141 的 [SF-1–SF-2](../../canonical/selection_superlinear_family.md#sf-object)，在 \(\eta\le0\)、I=(0,1) 片上取 \(\phi(y)=y^{\gamma/\nu}\)、c=A、\(a(y)=y^{1/\nu}-y>0\)、\(b(y)=-y^{1/\nu}-y<0\)。全部条件成立。p₀≤0、0<r₀<1 的普通轨道始终在此片；任意 pair-monotone 核的正常差0，两支正常值均非零，故不能保持。同符号仅在 I=(0,1) 使用，未夸大至 y≥1。
* C10 的 [GM26–GM30](../../canonical/general_modulus_dynamics.md#gm-log-object)，取 \(\phi(y)=\ell_a(4y)\)、c=1、正常值3y/−5y。对每个参数 a>0，\(\ell_a\) 全域严格递增且在正轴局部 C¹，包括切线接点，所以 M6 适用 I=(0,∞)。所有非驻定正法向普通轨道均被排除；a>1 的轨道是 C09 正面有限长实例，a≤1 的轨道不是，仍不能混用。

### 5.4 应更新的精确边界

新候选没有推翻 C200-v1；它补强了此前“mere pair-monotone 且无核正则性未被排除”的门。对应待修文字在 `gppa_review.md` §6/§8、`COMPARISON.md` §4、`independent_attack.md` §2/§5/§7/最后登记，以及 C200 的 scope 和 `RESEARCH_STATE.md` 的同框架活跃门。若交叉审查通过，可登记一个独立新身份（例如无冲突时 C204），保留 C200-v1 为已证的较弱 ASM 版本。

局部版本必须保留完整两支的产品片 W×I、中间全部正法向图点及待比较的相邻物理点。仅沿离散轨道点核条件不能使用 M5。删支、按 Minty 输入正负截掉另一支、换图值或改变物理图都失去该证明门；这不是“原 F 没有合格核”的断言。常量核仍 pair monotone/ASM，并可以把另一算法一步送入 zer F。

## 6. Theorem 4 的独立重建：打印证明可修复

源 p.9 Eq.(12) 的对象是 \(\widetilde F=F+ev\)。pair monotonicity 给 \((\widetilde F,v)\) e-ASM；这改变原关系。写 \(x_k=u_k+y_k\)、\(\|y_k\|\le\delta=e^2\)，固定 \(x_*\in\operatorname{zer}\widetilde F\)，源 p.10 核递推是

\[
A_{k+1}\le\kappa(A_k+L\delta),\quad
A_k=\|v(u_k)-v(x_*)\|,\quad\kappa=(1+2he)^{-1/2}. \tag{A12}
\]

源打印的 \(\kappa/(1-\kappa)\le2/(he)\) 恰在 he≤4 成立；固定 h、e“充分小”足够，但不能作全 he>0 恒等式。y₀ 未定义可以取0或从1开始，不改变渐近结论。p.11 最终 inverse 包含要进入 Definition 5 的 σ 窗，不能一开始无条件使用。

另一处是真正的证明步骤欠缺：Definition 5 只保证 \(\rho\) 在0右连续，源 p.11 不能从 \(\rho(B_e+o(1))\) 直接得到 \(\limsup\le\rho(B_e)\)。比如在正点 B 取 \(\rho(t)=t\)（t≤B）、\(\rho(t)=2+t\)（t>B），它满足原点和非减条件，但该推理失败。

现有两份报告的修补独立成立。A5 可把 A12 的因子换为 \(q=(1+he)^{-1}\)，故

\[
\limsup A_k\le\frac{qL\delta}{1-q}=\frac{Le}{h}. \tag{A13}
\]

Lemma 3 给 \(\|v(x_*)\|\le a_0:=\inf_{s\in S}\|v(s)\|\)。实际原图值

\[
f_{k+1}=\frac{v(x_k)-v(u_{k+1})}{h}-ev(u_{k+1})\in F(u_{k+1})
\]

满足

\[
\limsup\|f_{k+1}\|\le\widehat B_e
=\frac{Le^2+2Le/h}{h}+e(Le/h+a_0).
\tag{A14}
\]

原 theorem 打印的输入为

\[
B_e=\frac{Le^2+4Le/h}{h}+e(2Le/h+a_0),\quad
B_e-\widehat B_e=2Le/h^2+Le^2/h>0\quad(L>0). \tag{A15}
\]

足够小 e 使 B_e<σ，严格裕度则使实际值最终≤B_e，只用 \(\rho\) 非减就给

\[
\limsup_k d(x_k,S)\le e^2+\rho(B_e),\qquad
\lim_{e\downarrow0}\limsup_k d(x_k,S)=0. \tag{A16}
\]

L=0 时 v≡c，\(a_0=\|c\|\)，实际原图值精确为 −ec；直接用包含得 e²+ρ(ea₀)，等于原打印界，无须正裕度。e=0 不在这个正正则化 theorem 的范围，不能把 q=1 代入 A13。

还必须区分两个存在量词。要保证**每个初值**能生成全部迭代，需正则化 coverage \(\operatorname{ran}v\subset\operatorname{ran}(h(F+ev)+v)\)。两个零集非空本身不推出它。例如 v=Id、\(\operatorname{gph}F=\{(0,0)\}\) 满足 pair monotone、Lipschitz、两个零集非空及原逆像 R-continuity，却没有非零输入的 warped 输出。若 theorem 只对已合法生成的无限轨道陈述，可按条件性轨道定理读。双极限还需一族趋零的 admissible e 问题满足正则化零集/轨道存在；“只给某一个小 e 有零点”字面上不提供整族极限。

因此原打印 proof 有可说明的技术和存在量词门，但没有构成 Theorem 4 稳定性结论的致命反例。它确实具有本库精确 PPA 定理没有陈述的非消失均匀误差稳定性范围。M-CAP 不能被用来否定它在**改变后的** \(F+ev\) 上的适用性；改变后的两支正常值和核差项须重新核验。

## 7. 与本库相关主定理的全部关系

| 本库精确身份及规范公式 | 与 GPPA 全部四个结果的关系 | 可陈述和不能陈述的结论 |
| --- | --- | --- |
| C02-v2 / R01、R02-budget | 有限维同图块 all-pairs RL、完整真残差输出 EB、coverage/零锚、同尺度严格兼容及留域给物理几何尾 | C199 有 genuine overlap；C137 有同完整图同轨道排除。不能因此宣布完整一般类包含、不可比或大小排序。 |
| R03 的 energy certificate（`research/rleb_ppa.md`） | 同图块、严格 \(A(d)/V(d)<1\) 与另一个留域预算，也给能量/物理几何尾 | 物理率下长度已经随附；源 Theorem 2 没有给这套能量/反射证书等价。线性强单调简单子类仍有同轨道重合。当前主报告未单列此分支，可补比较表。 |
| C09 / GM1–GM18 | 一般零消失模、Dini 采样可和、同窗兼容和严格预算，给真实物理尾及有限長 | 源 Theorem 1/2 的集合距离不能代替物理 Dini 尾。具体 C10 双支有源前件排除，不能由此推成所有一般模都无 GPPA 表示。 |
| C10 / GM26–GM39 | 完整双支真实 inf 残差，全部法向距离乘1/4；a>1 有限长、点尾 \(\asymp k^{1-a}\)，a≤1 切向发散 | §5 新候选把其指定普通轨道对源 Theorem 1/2 都排除。a≤1 不是 C09 正面实例；1<a≤2 点尾本身不可和，实际步长可和。 |
| C11 / GM19–GM25；C136/C137/C141 共同尾和两点模 | 相同 T 的不变开域、共同尾、连续极限回缩；特定 cap/超线性族另有同图配对锐阶 | 源 theorem 没有这些定量解选择输出。有限维弱收敛或单轨道点率不自动给共同两点模，但合适额外连续性/统一尾理论可能推导它们，全球先行性未核。 |
| C137 / GC-1–GC-8 | 完整跨支 RL、真实 inf EB、全输入单点纤维、严格窗及共同几何尾 | 原 C200 任意 ASM 核排除有效；M-CAP 进一步排任意 pair-monotone 核，物理同轨道/完整图门不可删除。但 §11 保零集删支可间接导入源 Theorem 2 证明指定原选择的同一物理结论。 |
| C141 / SF-1–SF-12 | 完整双支；局部输出 collar 上 RL/严格 EB，超几何共同尾、逐轨道 Q-ν 及锐两点阶 | 对 p₀≤0、0<r₀<1 的轨道，§5 明定片上排除。没有排其所有轨道或任意别的表示；慢一些 R-linear 上界不解决更新身份。 |
| C191/C192/C193 / SN6–SN17 | 完整自然关系及全部纤维，真 EB、局部模，法向/切向直接有限长；反馈全域可能多值 | C199 是 C191 真实子类。一般数据核分类仍开放；C193 固定矩阵二次锚失败不是 GPPA 必要条件，不能用于任意核排除。 |
| C03 / GSH-1–GSH-22 | 同一个强单调双 Lipschitz 同胚 A 同时近似完整图正反方向，统一因子 \(R/\sqrt2\)（值方向再除 λ），并有维数统一锐性 | GPPA 没有构造该 A、同图双方向统一近似或锐常数。把 PPA 换成影子 A 的算法不保原 F/原轨道。源收敛子类重合不重复这个结构定理。 |
| C04 / FF1–FF27 | 固定参数 graph-maximal 的有限维完整正/逆纤维非空紧、直径门 R/λ 与 R；全部满足直径门的非空紧集实现 | GPPA 没有证明这一必要/充分分类或 graph-maximal 完成。其非常宽的 pair kernel 条件也不暗含有限维完整纤维分类。 |
| C18 / FC1–FC12 | 明确最大根定位、全域及固定窗的全部完整纤维覆盖与统一锐性 | GPPA 的 \(F^{-1}\) R-continuity 是输入假设，不证明该全部纤维的覆盖输出；更不能由 warped coverage 换成正/反原纤维 coverage。 |
| C19 / FD-1–FD-12；C20-v2 / FD-13–FD-18 | 同一有限 QP 给一个全局代理；同图同尺度网络覆盖及完整纤维门下给覆盖、噪声、独立反演误差三项界 | Theorem 4 的均匀物理误差/正则化距离稳定性是另一种对象和量词，不是该有限数据代理或三项证书。当前只判没有同身份结果，全球新颖性仍开放。 |

对 C03/C04/C18/C19/C20-v2，本审查核的是“这篇 GPPA 有没有同身份结论”的比较；并未重新完成这些结构定理全部内部证明或全球外文先行性。两条证据义务不可混合。

还存在明确的**假设类差别**。正式结构稿的完整全图、全部尺度、\(0<\gamma<1\) 条件在两个零图值上给
\[
\|s-s'\|\le L\|s-s'\|^\gamma\quad\Longrightarrow\quad
\operatorname{diam}(\operatorname{zer}F)\le L^{1/(1-\gamma)}=R.
\tag{A17}
\]
而 C199/C137/C141/C191/C192 的完整零集是无界切向平面，所以这些见证不属于正式结构稿的全图全尺度次线性类。它们的局部输入对尺度 RL 不能替代那个全尺度前件。C202 的 −Id 重合使用 \(\gamma=1\)，其线性 Cayley 映射也没有任意有限常数的全尺度 \(\gamma<1\) 上界。故它们说明项目**收敛线**的重合/不涵盖，没有直接检验正式结构主定理在自己前件类内的先行性。另一审查者已从真实附件定理及讨论中独立核对了这点，本篇 A17 是直接从规范定义推导。

## 8. 局部截断、lift、regularization 的真正范围

同完整 F 的 GPPA 排除依赖完整 all-pairs 图。若仅取 cap 正普通输入对应的正支，则保留轨道并不保完整原图；正常值 −5y 的支被删除，M2 的一半也随之丢失。若局部截断保留原图某近零产品片内的完整两支，则 M-CAP 在片内仍成立，尾轨道被排除。全图与产品片条件应写清，不能把任意离散轨道拟合算成 source theorem 的完整 ASM/pair-monotone 核。

任意其它升维、非线性坐标、拆分、加入记忆或压缩，当前没有总排除。GPPA 原文也没有提供覆盖这些表示的总定理。需要逐项核：提升关系完整图是否保真、每个原图值如何提升、原残差/零集、源的完整配对条件、算法投影是否逐步等于明定普通 PPA，以及源输出如何回代物理结论。

C203 的 **NFB 标准** full-graph product 以 `(f,0)` 输出和 product 零锚压回原图二次锚，属于指定条件性标准 lift 的另一证明；它不是 GPPA 任意 lift 的必要条件。C201 的二次锚也不是 GPPA 任意核必要条件，C199 已明确反例。本文没有把这两个排除错误移植过来。

若重写 \(F=G+ev\)，pair monotone 的 \((G,v)\) 会使 \((F,v)\) e-ASM，此时与同 F 的精确 warped 更新仍须满足 C200 障碍。若从同 F 改成 \(F+ev\)，就是原文 Theorem 4 的新关系，现有同 F 排除不直接适用。误差只要允许不消失，保持物理点序列还必须给出逐步合法误差和其界；不能以“inexact”这个词自动取得原普通轨道身份。

## 9. 独立有限复算及事实裁决

[sol61_gppa_check.py](sol61_gppa_check.py) 已执行，结果在 [sol61_gppa_results.json](sol61_gppa_results.json)。检查包括两组不同 α/λ/h 的有理数幂实例（α=2/3、α=1/2），边界法锥全部选取样例、36步精确普通/warped 身份及不变量、负输入首步的不同合法图值、cap 固定严格 κ、跨支系数消去和带跳跃标量单调剖面的分割望远镜界、Theorem 4 正裕度和 he=4/5 边界。这些只是公式/边界校验；M5、任意核量词和无限轨道结论完全由正文证明承担。

可以据现有证明直接保留的裁决是：**GPPA 有真实物理结论重合，在固定完整原图的表示合同下没有涵盖全部明定普通 PPA 轨道；有限长度在已有物理几何点尾的子类中已经随附。C199/C200-v1 和 T4 修复没有本次发现的致命数学断点。** M-CAP/M6 关闭了这些 scalar 双支实例的无核正则性 mere-monotone 门。§11 又说明，同一原 cap 指定选择的物理收敛结论可以通过保零集子关系从旧 theorem 导入；不得把原图前件排除升级为该结论本身不受旧理论支持。

仍然没有闭合：一般 C191/C192 的任意核分类、任意其它保真 lift、其余既有论文和源 [13]/[14] 的所有历史版本、结构稿的全球先行性、总体自然母空间规模比较。一个源前件排除见证不能认证全球创新，更不能证明 RLEB 在自然母空间中更大。M-CAP 的中央登记由 root 负责，只能按其完整 scalar 双支片和同轨道量词登记。

## 10. 对新正文的独立交叉接收

写完本篇直接证明后，另读 [pair_monotone_barrier.md](pair_monotone_barrier.md) 全文、[pair_monotone_results.json](pair_monotone_results.json) 和 [另一独立审查](sol61_independent_audit.md) 中的新加强重构。

root 的 PM4 只折叠正常分量，正确。PM5 使用5/3加权的同支配对消去正常项，对 cap 正确；我的 M2–M3 使用 A/B 加权跨支配对，得到相同标量单调结论。PM6–PM8 的常数与 M4–M5 相同，端点跳跃不会影响望远镜总变差。root 的标量推广改用 CROSS 消去，恰避开 C141 的 \(y^{1/\nu}-y\) 可能变导数符号；只要求正常异号/连续、共同标量剖面严格递增且正紧区间 Lipschitz，没有偷加 a₊ 的单调性。PM3 允许逐步任取 \(h_k>0\) 也成立，因为每一步正常差都是0，两支正常值非零。

root §scope 的换图反表示也正确：对固定初值，I=1/4，\(G(\xi,\eta,y)=(\xi-I,\eta+1,3y)\) 的 \(J_G\) 恰复制该一条 cap 物理轨道，但它只有一个零点，改变了完整 F 的零集和其余纤维。不能据原图障碍宣称“该物理序列在任意算子下均无法用旧 PPA 证明”。

本篇原候选标记记录的是初始提交状态；这次交叉接收后，完整 scalar 双支同轨道加强的证明义务已在受检范围内闭合，适合独立登记 C204，保留 C200-v1 的原 ASM 身份。没有把交叉接收变成任意核分类、任意 lift 总排除或全球新颖性判断。

## 11. 保零集删支：Theorem 2 可间接证明原 cap 指定选择

root 转来另一独立审查者的构造后，按原图重新核验如下。令 D_y 是 GC-1 原函数，只删除负正常支，得到完整子关系
\[
F_+(\xi,\eta,y)=\{(-2\sqrt y,-D_y(\eta),3y)\}\quad(y\ge0),
\qquad F_+=\varnothing\quad(y<0).
\tag{B1}
\]
它闭，完整边界 \(F_+(\xi,\eta,0)=\{0\}\)，故完整零集仍是 \(S=\mathbb R^2\times\{0\}\)，没有变为单点。对每个普通输入 r≥0，正常方程 r=4y 给唯一正支输出，另外两坐标和 GC-2 完全相同。因此 \(J_{F_+}(z,p,r)=J_F(z,p,r)\) 对**全部 r≥0 输入的完整纤维**成立。r<0 的原完整 F 有负支输出，而 F₊ 没有普通输出，不能声称整个算法全输入相等。

取全域核、外部步长和 ASM 常数
\[
v(\xi,\eta,y)=(-2\sqrt{y_+},-D_{y_+}(\eta),y_+),\qquad h=1,\quad\varepsilon=1.
\tag{B2}
\]
对 B1 内任意两个完整图点，前两分量 F₊ 与 v 相同，正常分量分别为3y、y，故
\[
\langle\Delta F_+,\Delta v\rangle
=4(\Delta\sqrt y)^2+(\Delta D)^2+3(\Delta y)^2
\ge4(\Delta\sqrt y)^2+(\Delta D)^2+(\Delta y)^2
=\|\Delta v\|^2.
\tag{B3}
\]
全部图值正常分量是3y，所以 \(F_+^{-1}\) 在0全局 R-Lipschitz 常数1/3；投影 \((\xi,\eta,0)\) 给实际闭球和集包含。边界 y=0 全部位置都是真零点，残差/逆像门没有漏量词。

全输入 warped coverage 也可以解出。给任意输入 \((z,p,r)\)，写 \(R=r_+\)、\(d=D_R(p)\in[0,2\sqrt R]\)。输出正常方程给 y=R/4，切向第一式自动为 \(-4\sqrt y=-2\sqrt R\)，ξ 自由；第二式只要求
\[
2D_{R/4}(\eta')=d. \tag{B4}
\]
若 R=0，d=0，整个 S 都是 warped 输出。若 R>0，\(D_{R/4}\) 的值域正是 [0,√R]，所以 B4 总可解。具体：d=0 时任何 η'≤0 可行；0<d<2√R 时唯一 η'=d/2+d²/4；d=2√R 时任何 η'≥√R+R 可行。这逐输入证明了源 Definition 4 的 coverage，不是由零集非空推测。

对 η₀≤0、r₀>0 的原 cap 普通轨道，η_k=η₀，y_{k+1}=y_k/4，ξ_{k+1}=ξ_k+√y_k；B4 可选 η'=η₀，所选普通输出也满足第一/正常方程，因此全过程是 B1 的合法 GPPA。一步不变量 \(I=\xi_k+2\sqrt{y_k}\) 给预先确定的零锚 \(x_*=(I,\eta_0,0)\in S\)，沿该选择
\[
v(x_k)-v(x_*)=(-2\sqrt{y_k},0,y_k)=x_k-x_*.
\tag{B5}
\]
源 Theorem 2(a)，pp.7–8，核因子 \(1/\sqrt3\) 遂给同一原 cap 物理点 R-linear；A6 直接给有限长度。Theorem 2(b) 的逆像条件也已满足。对 root 的固定 \((0,-1,1/64)\) 初值，I=1/4，和 PM9 完全相同。

这个 explicit 核**不保持所有正 η 普通轨道**：例如输入 r=1、p=2，\(D_1(2)=1\)，原普通输出 η'=3、y'=1/4，\(D_{1/4}(3)=1\)，与 B4 要求值1/2不同。不能因普通 F₊/F 纤维在全部 r≥0 输入相等，就声称它们的所有选择都进入这个 GPPA 核。上述物理桥限 η₀≤0、r₀>0 的共同轨道片；这已经覆盖 C204 所排除的指定普通轨道结论。

因此更精确的裁决是：**同完整原 F 的配对条件失败，但旧 theorem 通过同零集、保原选择的子关系可以导入物理收敛结论。** 删除另一支毁掉原图障碍，并不必然改变研究者关心的这条普通轨道或求解目标。C204 作为完整原关系的类/表示障碍仍正确；如果创新主张只是“这条 cap 普通序列的点收敛或有限长度无法由 GPPA 推出”，B1–B5 就是致命异议。其全初值共同模、完整原关系的所有物理选择和解选择锐阶，仍须按各自量词独立比较，不能由这一子片覆盖自动得到。

独立脚本新增 B1–B5 的256组 exact pair 样例、16个包括 cap 端点的 warped 输入构造、24步负 η 普通选择及物理桥、正 η 不包含反例，结果全通过；无限量词证明是上面的 B3–B5 代数，不是这些有限样例。

## 12. 对分支限制报告实际版本的独立审查

读取 `sol61_branch_restriction.md` 全文后，分别按它的实际 kernel/domain 参数重建，而不是把我先前输出高 R 的不同 collar 版本当作它的证明。没有找到以下三个构造的数学断点。

### 12.1 cap 的简化核

报告把 B2 改成 \(v=(-2\sqrt{y_+},0,y_+)\)。完整 F₊ 的第二图值虽随 η/y 改变，但核第二分量0，所以配对精确为 \(4(\Delta\sqrt y)^2+3(\Delta y)^2\ge\|\Delta v\|^2\)。这是完整 all-pairs 1-ASM。

给任意输入 r，输出 y=r₊/4，第一/正常方程自动，第二式只需 D_y(η')=0。因此 r>0 的完整 warped 纤维为 \(\mathbb R\times(-\infty,0]\times\{r/4\}\)，r≤0 时整个零平面 S；coverage 全域。源逆像常数1/3、原普通 η₀≤0 的物理桥和有限负初值前缀转移同 §11。这个简化核更清楚地显示没有用非零第二 kernel 坐标补充物理信息；它不能保持 η₀>0 的普通轨道。本篇 B2 的较复杂核同样正确，但报告选用的简化核已经足够得到核心反覆盖。

### 12.2 C141：输入 clip R、输出图高 R^ν 的实际常数

报告取
\[
0<R<\min\{1,\nu^{-1/(\nu-1)}\},\quad
0\le y\le R^\nu
\tag{C1}
\]
作为正支完整子关系 G 的输出图 collar，保留全部切向位置/该支图值。定义
\[
E(s)=\sum_{j\ge0}s^{\gamma\nu^j}\quad(0\le s<1),\quad
b(s)=\min\{R,\max\{s,0\}\},\quad
v=(-hA E(b(y)),0,hb(y)),\quad h>0.
\tag{C2}
\]
E(s)≤s^γ/[1−R^{γ(ν−1)}] 对 s≤R 成立，因 \(\nu^j\ge1+j(\nu-1)\)。因此级数有限且0处连续，无需先假设物理轨道收敛。\(E(s)-E(s^\nu)=s^\gamma\) 是同一个正项级数的指标移位恒等式。

在**图输出** y≤R^ν 上，b(y)=y。令 \(t=\phi(y)=y^{\gamma/\nu}\le R^\gamma\)，则 \(E(y)=\sum_{j\ge1}t^{\nu^j}\)。其对 t 的 derivative 系列在闭区间上由
\[
K_R=\sum_{j\ge1}\nu^j R^{\gamma(\nu^j-1)}<\infty
\tag{C3}
\]
控制，相邻上界项的比为 \(\nu R^{\gamma(\nu-1)\nu^j}\to0\)，故一致收敛，包括 t=0。这正是报告的 K_R；不存在遗漏 γ/ν 或从输入 R 错搬至输出 R 的因子。于是 \(|\Delta E|\le K_R|\Delta\phi|\)，两差同号。

正支正常函数 g(y)=y^(1/ν)−y 在 0<y≤R^ν 上的 derivative 下界为
\[
m_R=R^{1-\nu}/\nu-1>0.
\tag{C4}
\]
零端点由连续极限延伸，\(\Delta g\Delta y\ge m_R(\Delta y)^2\)。故对完整 G 所有点对，
\[
\langle\Delta f,\Delta v\rangle
\ge\frac1{hK_R}(hA\Delta E)^2+\frac{m_R}{h}(h\Delta y)^2
\ge\min\{1/(hK_R),m_R/h\}\|\Delta v\|^2.
\tag{C5}
\]
第二 kernel 分量0 使原 τ 图值的变化无需额外符号假设。源 Definition 3 的完整 ASM 门闭合。

对任意输入正常 r，令 c=b(r)∈[0,R]，输出 y=c^ν∈[0,R^ν]。正常式 \(hc=hy+h(y^{1/\nu}-y)\) 成立，第一式由 E(c)=c^γ+E(c^ν) 成立，第二式可选 η'≤0。ξ 自由；c=0 的输出是整个零平面。因此全输入 warped coverage 真实成立，虽普通子关系只在有限输入 collar 有输出。G 的零集仍是整个原零平面；\(g(y)\ge m_Ry\) 给完整逆像全局 R-Lipschitz 1/m_R，不需所选残差等于完整 inf。

对原普通 η₀≤0、0<r₀≤R 的轨道，I=ξₖ+A E(rₖ) 是一步不变量，\(x_*=(I,η_0,0)\) 预先由初值确定，\(v(x_k)-v(x_*)=h(x_k-x_*)\)。源 Theorem 2(a) 因而导入物理 R-linear 和有限长。任意 η₀≤0、0<|r₀|<1 的原轨道有有限前缀后进入固定 R collar，可从该时刻导入；不声称初始负/大输入那一步就是 G-GPPA。

独立精确参数检查取 γ=1/2、ν=2、R=1/4、h=1，则输出图高1/16、m_R=1。C3 为 \(\sum_{j\ge1}2^j2^{-(2^j-1)}\)，前四项和及余项几何比上界给 1<K_R<2，故 ε=1/2 是安全正证书。R=1/2 时 m_R=0，严格门确实丢失。脚本又以平方有理初值检查 E 的匹配截断移位和 y=c²∈[0,1/16] 的正常式；这些只检有限公式，C3/C5 的无限全称依上面分析。

### 12.3 C10 a>1：Theorem 1 加实际 Dini 尾桥

正支完整关系为 \(F_{a,+}(t,y)=\{(-\ell_a(4y),3y)\}\)，y≥0，域外空。它保留整个原零线，在 r≥0 的全部普通输入完整纤维和原 Fₐ 相同。对 a>1，
\[
E_a(s)=\sum_{j\ge0}\ell_a(4^{-j}s),\qquad
v(t,y)=(-E_a(y_+),y_+),\quad h=1.
\tag{C6}
\]
正项系列对每个有限 s 都有限：远处仅有限个切线延伸项，最终所有项进入规范对数区域。若 \(A=\log(e/s)\) 足够大、b=log4，积分夹逼给
\[
\frac{A^{1-a}}{b(a-1)}\le E_a(s)
\le A^{-a}+\frac{A^{1-a}}{b(a-1)}.
\tag{C7}
\]
所以 E_a(0)=0 连续，且 E_a 严格递增。完整配对为 \([\Delta\ell_a(4y)][\Delta E_a(y)]+3(\Delta y)^2\ge0\)。正常 warped 输出 y=r₊/4，第一式由 \(E_a(r)-E_a(r/4)=\ell_a(r)\) 成立，t 自由，故全输入 coverage；完整逆像 R-Lipschitz 1/3。

源 Theorem 1(c)，p.6，给 y_k=d(x_k,S)→0。普通正轨道的 I=tₖ+E_a(yₖ) 不变量和 E_a 在0连续性才把距离结论转成物理点收敛，\(v(x_k)-v(I,0)=x_k-(I,0)\)。切向增量非负且望远镜总和 E_a(y₀)，正常变差 y₀，故物理长度≤E_a(y₀)+y₀。这一步**确实需要额外尾身份和坐标单调几何**，不是打印 Theorem 1 自带有限长；Dini 可和性已经编码在 E_a 的有限定义里。负初值仍可先完成一个原 Fₐ 的有限步再导入正尾。

这个 kernel 非 ASM 的断言正确。与零点比较的配对/核范数平方比趋于 \(b(a-1)/A\to0\)：C7 给 E_a(s) 的渐近，\(\ell_a(4s)\sim A^{-a}\)，s 相对两者可忽略。a≤1 时 E_a(s) 对每个 s>0 发散，构造不存在；没有把原发散轨道称作有限长覆盖。

### 12.4 更新后的最终范围裁决

实际落盘稿的三条保零集 subrelation/tail 转移全部通过上述独立证明核验。它们没有绕过原完整 F 的 all-pairs 障碍，而是换成具有同零集、在相关 basin/tail 上保持原普通纤维的完整子关系。对 cap/C141 的指定轨道，源 Theorem 2 配物理桥确实给相同点收敛和有限长；对 log a>1，源 Theorem 1 配 Dini 尾桥给相同点收敛和有限长。

因此 **C200/C204 的前件排除并不等于这些原物理收敛结论不能从 GPPA 理论导入**。cap 的简单 algebra kernel 不依赖未知极限；C141/log 的尾 kernel 用显式原数据系列定义、有限性独立证明，未循环假设物理收敛。它们可能并不是高效可计算的通用求解方法，也没有代替一般 RLEB 合取机制；但作为逐定理先行性比较，不能忽略这条证明导入。源 theorem 本身没有给全初值共同尾、精确 Q-ν、连续解选择两点模/锐下界或独立结构稿结果。那些输出及全球先行性须另审，不能仅凭完整图障碍获准新颖性。
