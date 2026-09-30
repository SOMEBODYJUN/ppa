# 第 5 组：RLEB 好坏解选择类的鲁棒性与最小扰动测试

日期：2026-09-20。对象：`solution_selection_revised_v1/research_note.md` 全文与 `initial_value_stability_team/06_synthesis.md` 全文。本报告独立推导下列扰动结论，不改动研究稿、不重审无关的原 RLEB 内容，不以数值试验代替证明。

## 1. 直白结论

用户提出的“坏类到底大不大”是一个真正有内容的问题。但目前不能从一个反例推出坏类泛型，也不能从平滑近似推出坏类是第一纲。

本组得到的精确压力测试是：

1. 原稿的坏例不依靠精确平坦函数。固定 Hölder 指数后，一整片严格兼容的有限维系数开集都是坏例。
2. 另一方面，能在**同一零集、同一实际距离因子、同一组有效 RLEB 常数、同一有限分支数、同一半代数表达复杂度**下，用好的 Hölder 选择模型一致逼近每个该族坏例。
3. 这种逼近甚至使完整算子图的 Hausdorff 距离趋零。因此该坏例在一致 resolvent／图距离拓扑中不是坏类的内点。
4. 两者不矛盾：固定一种尖点模板时坏类很大；允许一个自然“削圆尖点”参数时，坏类在这个扩大后的有限维模型中落在零测的边界层。
5. 本轮没有证明一般 RLEB 算子空间中的坏类 meagre、prevalent、稠密或余维为正。对完整空间作此声明还缺新的扰动与保持定理。

因此最有价值的首步不是猜一个“多数都好／多数都坏”的答案，而是证明**分类依赖哪些结构被固定、允许哪些扰动、采用什么拓扑**。

## 2. 先把 Good/Bad 的量词固定

固定解点 $s$、共同初值邻域及共同轨道区域。定义

\[
\mathrm{Good}_{H,s}=\{T:\exists\rho,C,\theta>0,
\ \|\Pi_Tx-\Pi_Ty\|\le C\|x-y\|^\theta
\ \forall x,y\in B_\rho(s)\}.
\]

此处是完整邻域的**两点 Hölder 连续性**，不是固定 $s$ 的 calmness。再定义

\[
\mathrm{Bad}_{NH,s}=\{T:\Pi_T\text{ 连续，但 }T\notin\mathrm{Good}_{H,s}\}.
\]

Lipschitz 好类应另记 $\mathrm{Good}_{L,s}$。它不是同一个问题。本报告的所有模型都保留 $\gamma<1$ 的法向尖点，因此即便属于 $\mathrm{Good}_{H,s}$，也不属于 $\mathrm{Good}_{L,s}$，见 §7。

另外，在当前严格共同 RLEB 预算所提供的统一消失点尾下，连续单步映射的迭代在共同初值域上一致收敛，所以极限映射连续。**不连续选择类在这个已认证的共同域内为空**。若把“不连续”也混入 Bad，必须另外说明究竟放松了哪项共同域／统一尾条件。

## 3. 现有坏例在系数族内不是孤立点

固定 $0<\gamma,q<1$，考虑原稿已证明的完整 resolvent 家族

\[
T_{A,B,0}(z,p,r)=
\bigl(z+A|r|^\gamma,
p+B\min\{p_+,|r|\}^\gamma,
q|r|\bigr),
\qquad A>0,\ B\ge0.
\tag{3.1}
\]

对于 $B>0$，原稿首次饱和证明给固定实际 $(\gamma,q)$ 下的非任意正阶 Hölder 选择。严格兼容的充分条件是

\[
q\left(1+(B/A)^2\right)^{1/(2\gamma)}<1.
\tag{3.2}
\]

故在有限维参数域

\[
\{(A,B):A>0,\ 0<B<A\sqrt{q^{-2\gamma}-1}\}
\]

中，每一点都是坏例；这是一个真正开集，而非一个需系数精确相等才存在的点。若固定有理 $\gamma$，整个家族保持半代数及同一表达模板，不必让指数在有理／无理之间跳动。

当 $B=0$ 时，极限显式为

\[
\Pi_{A,0,0}(z,p,r)=
\left(z+\frac{A|r|^\gamma}{1-q^\gamma},p,0\right),
\tag{3.3}
\]

因而是局部 $\gamma$-Hölder。令 $B\downarrow0$，坏例趋向好例；在固定有界比较域 $K$ 上甚至有

\[
\|T_{A,B,0}-T_{A,0,0}\|_{C^\gamma(K)}\le C_K B\to0.
\tag{3.4}
\]

所以在任何包含此系数扰动的 $C^\gamma$ 或更弱环境中，Good 在该好例处不开放，Bad 不闭。**这不证明坏类在全算子空间中有内点、稠密或 residual。** 开集结论目前仅针对上述系数参数域。

## 4. 同证书、同零集的“好逼近坏”家族

固定满足严格余量的 $A,B>0,\gamma,q$，引入参数 $\varepsilon\ge0$：

\[
h_\varepsilon(s)=(s+\varepsilon)^\gamma-\varepsilon^\gamma,
\qquad s\ge0,
\]

\[
b_\varepsilon(p,a)=\min\{h_\varepsilon(p_+),a^\gamma\},
\]

\[
T_\varepsilon(z,p,r)=
\left(z+A|r|^\gamma,
p+B b_\varepsilon(p,|r|),q|r|\right).
\tag{4.1}
\]

这里 $T_0$ 就是原稿坏例。$\varepsilon>0$ 只削圆**切向** $p$ 的尖点，不削掉法向 $r$ 的真正 $\gamma<1$ 奇异性。

### 4.1 完整二值算子及零集没有改变

对每个 $a\ge0$，

\[
f_{a,\varepsilon}(p)=p+B b_\varepsilon(p,a)
\]

连续、严格递增且满射到 $\mathbb R$：增加的项单调且介于 $0$ 和 $Ba^\gamma$ 之间。记其全逆为 $\tau_{a,\varepsilon}$。对 $y\ge0$、$a=y/q$，定义

\[
F_\varepsilon(\xi,\eta,y)=
\left\{
\begin{pmatrix}-Aa^\gamma\\ \tau_{a,\varepsilon}(\eta)-\eta\\a-y\end{pmatrix},
\begin{pmatrix}-Aa^\gamma\\ \tau_{a,\varepsilon}(\eta)-\eta\\-a-y\end{pmatrix}
\right\};
\quad F_\varepsilon=\varnothing\ (y<0).
\tag{4.2}
\]

两支法向输入分别为 $r=\pm a$，由符号唯一确定分支；其余输入分别为 $z=\xi-Aa^\gamma$、$p=\tau_{a,\varepsilon}(\eta)$。因此完整全空间 resolvent 精确为 $J_{F_\varepsilon}=T_\varepsilon$，没有只挑一支的遗漏。

逆函数关于参数连续；例如固定 $\varepsilon$ 时，严格单调的主项 $p$ 给

\[
|\tau_{a,\varepsilon}(\eta)-\tau_{a',\varepsilon}(\eta')|
\le|\eta-\eta'|+B|a^\gamma-a'^\gamma|.
\]

这也给闭图。$y>0$ 恰二值，$y=0$ 一值，且

\[
\operatorname{zer}F_\varepsilon=S=\mathbb R^2\times\{0\}
\]

对所有 $\varepsilon$ 完全相同。有理 $\gamma$ 时，整个参数家族由一套固定有限半代数公式给出：通过有限辅助变量消去有理幂和逆函数即可。其分支／公式复杂度不随 $\varepsilon\downarrow0$ 增长。

### 4.2 同一 all-pairs RL、真实 min-residual 和严格兼容证书

凹性及次可加性给所有 $\varepsilon\ge0$ 的共同估计

\[
|h_\varepsilon(s)-h_\varepsilon(t)|\le|s-t|^\gamma.
\]

因为 min 对最大范数为 1-Lipschitz，故

\[
|b_\varepsilon(p,a)-b_\varepsilon(p',a')|
\le\max\{|p-p'|,|a-a'|\}^{\gamma}.
\]

与原稿完全同一 all-pairs 证明给共同常数

\[
L_R=2\sqrt{A^2+B^2}+(1+2q)R^{1-\gamma}.
\tag{4.3}
\]

这里包括异号 $r,r'$ 和所有 cap 分支。整个多值算子的最小残差满足精确式

\[
r_{F_\varepsilon}(u)^2
=A^2a^{2\gamma}
+|\tau_{a,\varepsilon}(\eta)-\eta|^2
+(1-q)^2a^2.
\]

于是所有 $\varepsilon$ 共用同一个 EB gauge

\[
d(u,S)\le\psi(r_{F_\varepsilon}(u)),
\qquad \psi(t)=q(t/A)^{1/\gamma}.
\tag{4.4}
\]

同一个有效严格兼容上界为

\[
\kappa_R=q\left[
\frac{\sqrt{A^2+B^2}+(1+q)R^{1-\gamma}}A
\right]^{1/\gamma}<1,
\tag{4.5}
\]

只需预先选择

\[
R^{1-\gamma}<
\frac{Aq^{-\gamma}-\sqrt{A^2+B^2}}{1+q}.
\]

它不依赖 $\varepsilon$。实际法向距离因子也对全族严格等于 $q$。故本例不是通过让证书退化到边界来获得好的近似；所固定的是共同的有效认证常数，不冒称已求出每个模型全部有限尺度最小常数。

### 4.3 每个 $\varepsilon>0$ 都有正阶两点 Hölder 选择

对 $\varepsilon>0$，

\[
\operatorname{Lip}(h_\varepsilon)=\ell_\varepsilon
=\gamma\varepsilon^{\gamma-1}<\infty.
\]

作与极限选择无关的固定法向换元

\[
w=\operatorname{sgn}(r)|r|^\gamma,qquad \sigma=q^\gamma.
\]

变换后的迭代为

\[
\widehat T_\varepsilon(z,p,w)=
\left(z+A|w|,
p+B\min\{h_\varepsilon(p_+),|w|\},
\sigma|w|\right).
\tag{4.6}
\]

它对 $\ell^1$ 范数是全局 Lipschitz，可取

\[
\Lambda_\varepsilon=
\max\{1,1+B\ell_\varepsilon,A+B+\sigma\}.
\]

并且在 $ |r_0|\le R$ 上共用几何点尾

\[
\|\widehat T_\varepsilon^kx-
\widehat\Pi_\varepsilon x\|_1
\le
\left(1+\frac{A+B}{1-\sigma}\right)R^\gamma\sigma^k.
\tag{4.7}
\]

有限前缀与两尾平衡直接推出变换坐标中的 Hölder 指数

\[
\theta_\varepsilon=
\frac{\log(1/\sigma)}
{\log\Lambda_\varepsilon+\log(1/\sigma)}>0.
\]

原坐标到新坐标在有界比较尺度为 $\gamma$-Hölder，极限法向坐标为零，故

\[
\|\Pi_\varepsilon x-\Pi_\varepsilon y\|
\le C_\varepsilon\|x-y\|^{\gamma\theta_\varepsilon}.
\tag{4.8}
\]

这已经是完整邻域两点估计，不是锚定 calmness。因而每个 $\varepsilon>0$ 属于 Good，而 $\varepsilon=0$、$B>0$ 属于 Bad。

### 4.4 一致拓扑、图距离与强 Hölder 拓扑不同

次可加性给

\[
0\le s^\gamma-h_\varepsilon(s)\le\varepsilon^\gamma,
\]

从而甚至全空间有

\[
\sup_x\|T_\varepsilon x-T_0x\|
\le B\varepsilon^\gamma.
\tag{4.9}
\]

利用完整图参数化

\[
\operatorname{gph}F_\varepsilon
=\{(T_\varepsilon x,x-T_\varepsilon x):x\in\mathbb R^3\},
\]

给两图中相同 $x$ 的点配对，得到

\[
d_H(\operatorname{gph}F_\varepsilon,
\operatorname{gph}F_0)
\le\sqrt2B\varepsilon^\gamma.
\tag{4.10}
\]

这里即使图非紧，所写双向 Hausdorff 距离仍是有限的。于是该特定 Bad 点在一致／图距离拓扑内没有全 Bad 邻域。

对任意 $0<\gamma'<\gamma$，共同 $C^\gamma$ 界与一致收敛给有界域上的插值估计

\[
\|T_\varepsilon-T_0\|_{C^{\gamma'}(K)}
\le C_K\varepsilon^{\gamma-\gamma'}\longrightarrow0.
\]

但这列近似**不在强 $C^\gamma$ 范数中收敛**。固定小 $r_*>0$，比较 $(0,p,r_*)$ 与 $(0,0,r_*)$，令 $p\downarrow0$，两项均处于未饱和段，则

\[
\frac{B|h_\varepsilon(p)-p^\gamma|}{p^\gamma}
\longrightarrow B.
\]

故

\[
[T_\varepsilon-T_0]_{C^\gamma(K)}\ge B.
\tag{4.11}
\]

本组的削圆论证因此不能直接裁定 Bad 是否在强 $C^\gamma$ 拓扑有内点。不能把“不满足这一条近似”反过来当作开放性证明。

所有 $\varepsilon$ 具有共同单步 Hölder 界和共同点尾，所以有限步一致比较再加尾界还给

\[
\Pi_\varepsilon\to\Pi_0
\quad\text{在共同有界初值域上一致收敛}.
\]

若这些 Good 近似另有共同正 Hölder 指数和共同常数，就可取极限迫使 $\Pi_0$ 也满足该估计，矛盾。因此不能从“每个削圆模型都好”得到对削圆参数统一的稳定性证书。

## 5. 同一坏例如何在两种自然有限参数统计里变大／变小

固定 $A,q,\gamma$，选 $B_{\max}>0$ 满足严格兼容余量，并用同一个更保守的 $L_R,\kappa_R$ 覆盖 $0\le B\le B_{\max}$。

| 参数空间与允许扰动 | Good/Bad 的精确集合 | 可作出的大小判断 |
|---|---|---|
| 只改尖点幅度：$B\in[0,B_{\max}]$，固定 $\varepsilon=0$ | Good={0}，Bad={$B>0$} | Bad 相对开放稠密、参数 Lebesgue 满测；Good 相对闭且 nowhere dense |
| 同时允许削圆：$(B,\varepsilon)\in[0,B_{\max}]\times[0,E]$ | Bad={$B>0,\varepsilon=0$}；其他为 Good | Bad 相对 nowhere dense、二维 Lebesgue 零测；Good 含开稠密集 {$\varepsilon>0$} |

两行都固定零集、多值支数、法向指数、实际速率及统一严格兼容预算；有理 $\gamma$ 时也不需放开半代数表达复杂度。

第二行中“余维一”只描述所选参数矩形里的边界层，不是无限维算子空间中已证明的余维。参数化在 $B=0$ 上有重复表示，如需避免可另固定 $B\in[B_{\min},B_{\max}]$、$B_{\min}>0$；Bad 仍是 $\varepsilon=0$ 面。

若所选概率分布在 $\varepsilon=0$ 有原子，Bad 甚至可以有任意指定的正概率；所以这里没有一个与扰动模型无关的“坏算子百分比”。

## 6. “泛型唯一解所以好类很大”不能无检查地使用

如果共同域内只有一个可能极限，$\Pi_T$ 当然为常值。但一个使解集离散化的常见小扰动可能已经离开严格 RLEB 类。

对坏模型加切向线性阻尼，$0<\eta<1$：

\[
T^{(\eta)}(z,p,r)=
\bigl((1-\eta)z+A|r|^\gamma,
(1-\eta)p+B\min\{p_+,|r|\}^\gamma,
q|r|\bigr).
\tag{6.1}
\]

由于切向输入是被稳定线性递推驱动的几何衰减项，所有轨道都趋零；固定点唯一，选择为常值。完整逆图依旧可以定义。但是在输出 $u=(\xi,\zeta,0)$ 上，完整 residual 恰为

\[
r_F(u)=c_\eta\|u\|,
\qquad c_\eta=\frac{\eta}{1-\eta}.
\]

所以任何到新零集 {0} 的有效 gauge 都必须满足

\[
\psi(s)\ge s/c_\eta\quad(s\downarrow0).
\]

同时法向反射尖点还在：输入 $(0,0,d)$、$0$ 迫使全对反射模 $\omega(d)\ge2Ad^\gamma$。因此

\[
\frac{\psi((d+\omega(d))/2)}d
\ge\frac{A}{c_\eta}d^{\gamma-1}\longrightarrow\infty.
\tag{6.2}
\]

它无法满足同一类严格 RLEB 标量兼容条件。此处的好性质是真实的，但不能据此宣称在“严格 $\gamma<1$ RLEB 算子类内部”好类泛型。

若要利用泛型孤立解结果，必须证明相应扰动保持研究中的全对 RL、真实 residual EB、严格兼容、共同域与完整纤维；不能把外部光滑映射空间的泛型结论直接拉进来。

## 7. 目标好性质也会改变答案

上述整个家族均有

\[
\pi_1\Pi_\varepsilon(z,p,r)
=z+\frac{A|r|^\gamma}{1-q^\gamma}.
\]

取 $x_t=(0,0,t)$、$s=0$，则

\[
\frac{\|\Pi_\varepsilon x_t-\Pi_\varepsilon s\|}{\|x_t-s\|}
\ge\frac A{1-q^\gamma}t^{\gamma-1}\to\infty.
\]

因此在同一有限参数空间里：

- 若 Good 指“存在某个正 Hölder 阶”，削圆后是 Good；
- 若 Good 指“Lipschitz”，全族都不是 Good；
- 若 Good 指“至少某个预定阶 $\theta_0$ 且常数有统一预算”，又是第三个问题。

同样，应区分“在指定解点 $s$ 的某邻域好”“在每个解点好”“至少某处坏”。平移坏接缝可能改变第一种判定而不消除第三种，不能在证明中切换量词。

## 8. 对下一阶段的具体建议与未解决项

### 可直接作为研究起点的事实

- 把现有算子放进固定 $\gamma,q,S$ 和共同严格预算的 resolvent 类，首先比较 $C^0$、局部图距离、强 $C^\gamma$ 三种拓扑。
- 把“同模板系数扰动”与“允许削圆／改变接缝结构的扰动”分层。§5 已有一个公式级示范，说明大小判断确实会反转。
- 优先研究稳定子类的相对开放性：例如固定法切坐标与 Dini／可和增益预算，赋予能控制该预算的各向异性范数。这样的子类可能有可验证的稳定性余量，但必须证明相对开放，而不是把所求结论写进范数定义。
- 对有限维半代数家族，先给参数 Lebesgue／维数结论；对无限维类，再讨论 Baire residual。prevalence 不能直接给一个非线性、非平移封闭的 RLEB 集合贴标签。

### 要成为一般大小定理仍缺什么

1. 指定真正的 Baire 环境：严格不等式、完整覆盖、固定零集、半代数限制的交集不自动是完备空间。
2. 建立保持 RLEB 的稠密扰动定理：需同时保持完整 resolvent、最小残差 EB 和严格兼容，不能仅扰动任意连续极限函数。
3. 若想证明 Good residual，需要对所有定量坏集控制闭包和内点；本报告只有特定家族的剖面结论。
4. 若想证明 Bad prevalent/shy，需要在线性环境中构造对**所有平移**都有效的探针测度，并解释与受约束 RLEB 子类的关系；在一个参数面抽到概率零远远不够。
5. 目前没有证明强 $C^\gamma$ 下该坏点的开放性；§4.4 只排除一种特定削圆近似，不排除其他小扰动。

作为概念入口，Hunt–Sauer–Yorke 的原始论文明确把 residual 与测度型 prevalence 区分，并要求后者的探针对所有平移有效：*Prevalence: a Translation-Invariant “Almost Every” on Infinite-Dimensional Spaces*, Bull. AMS 27 (1992), 217–238，§2 Definitions 1–2、Fact 2′，原文 [arXiv:math/9210220](https://arxiv.org/pdf/math/9210220)。该文不是 RLEB 大小结论；这里只据其定义说明为何不能用有限参数随机测试代替 prevalence 证明。

## 9. 本组终判

**值得研究，且可从现有成果出发；但不能预设坏类小。** 目前已有严格证据表明：同一个 RLEB 坏选择机制既能在固定尖点模板的参数空间中占开放满测部分，也能在允许自然削圆的扩大参数空间中成为 nowhere-dense 零测边界层。

这不是语言上的“看你怎么定义”，而是 §4 的完整图、真实 residual、统一 RLEB 证书与 Hölder 恢复证明所支撑的实质数学区别。它恰好说明新研究应从“哪些扰动结构被保留”入手，而不宜直接跳到整个 RLEB 类的泛型宣判。
