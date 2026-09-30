# RLEB 与 Luke–Tam 的同对象定义翻译及可比较类别

日期：2026-09-20。任务：只翻译、核查和划定比较口径；不修改原研究稿，不以参数微扰族代替算子空间。原 RLEB 投稿包的正文、全部附录，以及 solution-selection 修订稿已完整阅读。Luke–Tam 2025 已核正式全文；Luke–Thao–Tam 2018 两篇已核下列相关原文定义与定理。

## 0. 结论先行

1. **几何层确有严格扩张。** 在同一步长、同一完整输入区域、同一对点量词下，LT 的 all-pairs submonotonicity 恰是完整反射映射的 Lipschitz 条件；RLEB 的 all-pairs RL 恰是该映射的 Hölder 条件。前者是后者的指数一层。
2. **完整收敛证书不可只比这两个几何词。** LT 还要求误差界、数值阈值、局部完整性与留域；RLEB 还要求输出真实残差误差界及兼容条件。固定一个严格非线性 direct-RLEB 层，通常不包含 LT。
3. 若允许原 RLEB 稿件的 **direct 与 energy 两类证书并用**，在共同完整接口下，LT 2025 Theorem 2 的公共数值证书可以送入 RLEB 的线性 energy 层。平方根接缝则属于非线性 RLEB 而不属于任何有限局部 LT all-pairs 几何层。因此可以做严格包含的研究，但必须写清比较的是哪个被输送到共同接口的类别。
4. 不能把“LT 2025 Theorem 2”与“全部 Luke–Thao–Tam 点态 almost-averaged 理论”混成一个类。后者允许完整迭代关系在解点外多值、不连续；all-pairs RLEB 主定理则强制被表示的 resolvent 单值且 Hölder。
5. 类别大小问题最稳健的目标是：在一个独立定义、具完整误差界与收敛证书的母空间中，考察
   \[
   \mathscr R\setminus\mathscr L_{\rm geom},
   \qquad \mathscr L_{\rm geom}=\{T:2T-I\text{ 在指定区域局部 Lipschitz}\}.
   \]
   这个差类中的每个元素都排除了同接口的 LT 2025 all-pairs 收敛证书。但“这个差类 residual/meagre”在本报告中没有证明。

## 1. 统一对象：完整 Minty 输入坐标，而不是选中分支

先固定有限维 Euclidean 空间 \(H=\mathbb R^n\)、步长 \(\lambda>0\)、非空闭目标集 \(S\)，以及共同输入工作区域。若要研究多解选择，应固定非单点 \(S\)。令
\[
T=J_{\lambda F}=(I+\lambda F)^{-1},\qquad
R_T=2T-I,\qquad D_T=I-T.
\]
本报告中的完整单值接口意指：对每个被比较输入 \(x\)，完整包含式 \(x-u\in\lambda F(u)\) 恰有一个输出 \(u=T(x)\)，不是预先挑一个分支。

若从全空间连续单值映射 \(T:H\to H\) 出发，标准逆图编码为
\[
F_T(u)=\{(x-u)/\lambda:x\in H,\ T(x)=u\}.
\tag{1.1}
\]
则完整地有 \(J_{\lambda F_T}=T\)、\(\operatorname{zer}F_T=\operatorname{Fix}T\)。图闭性来自图坐标的可逆线性变换，不是额外假定：
\[
(u,a)\longleftrightarrow (x=u+\lambda a,u).
\]

**局部图块必须另记号。** 对 \(\mathcal G\subset\operatorname{gph}F\)，
\[
J_{\mathcal G}(x)=\{u:(u,(x-u)/\lambda)\in\mathcal G\}.
\]
仅在共同轨道区 \(W\) 上证明 \(J_{\mathcal G}=J_{\lambda F}\)，才能把局部结论作为完整算法结论。solution-selection 修订稿 §0、§1 已正确保留这一接口。LT 的局部裁剪也须遵守相同规则，不能允许一边删分支、另一边必须测试全图。

### 1.1 真正 min-residual 的 \(T\)-侧表达

由 (1.1)，
\[
r_{F_T}(u)=\frac1\lambda\inf_{x:T(x)=u}\|x-u\|.
\tag{1.2}
\]
在当前有限维完整连续接口下，只要纤维非空，它是闭集，范数最小值取得。因此，对固定输出区 \(V\)，
\[
d(u,S)\le\psi(r_{F_T}(u))\quad(u\in V\cap\operatorname{ran}T)
\tag{1.3}
\]
等价于
\[
d(Tx,S)\le\psi(\|x-Tx\|/\lambda)
\quad\text{对所有满足 }T(x)\in V\text{ 的 }x\in H.
\tag{1.4}
\]
等价性的关键是 (1.4) 测试了每个输出的**全部输入纤维**。若只测试留在某个输入 collar 的 \(x\)，而省略同一输出的其他较小范数原像，(1.4) 就只能称为 transition EB，不能冒称原算子 min-residual EB。在一般 Hilbert 空间，若最小值不取得，需 \(\psi\) 的右连续性等条件才能用取下确界证明反向。

## 2. 两套几何条件的精确字典

取图点 \((u,u^*),(v,v^*)\)，记
\[
a=u-v,\quad b=u^*-v^*,\quad
p=a+\lambda b=x-y,\quad z=a-\lambda b=R_Tx-R_Ty.
\]
恒等式为
\[
\|p\|^2-\|z\|^2=4\lambda\langle a,b\rangle,
\qquad
\|a\|^2+\lambda^2\|b\|^2=\tfrac12(\|p\|^2+\|z\|^2).
\tag{2.1}
\]

### 2.1 RLEB 的 all-pairs RL

原稿 `def:graph-RL` 在固定尺度 \(R_0>0\) 上要求，对图块中的每一对图点，包括跨分支对，若 \(\|p\|\le R_0\)，则
\[
\lambda\langle a,b\rangle
\ge\tfrac14(\|p\|^2-L^2\|p\|^{2\gamma}),\qquad 0<\gamma\le1.
\tag{2.2}
\]
它与下列两个条件**等价**：
\[
\|R_Tx-R_Ty\|\le L\|x-y\|^\gamma,
\tag{2.3}
\]
\[
\|Tx-Ty\|^2+\|D_Tx-D_Ty\|^2
\le\tfrac12(\|x-y\|^2+L^2\|x-y\|^{2\gamma}).
\tag{2.4}
\]
对多值关系，在 \(x=y\) 时 (2.4) 强制所有被表示输出相同。也因此，不能把只对某个输出选择成立的 (2.3) 叫完整 all-pairs RL。

### 2.2 LT 2025 submonotonicity

Luke–Tam 正式版 **Definition 2** 对 \(\lambda F\) 在固定 \(U\times W\) 图块上的条件，译为
\[
\lambda\langle a,b\rangle\ge-\tau\|a+\lambda b\|^2,
\qquad \tau\ge0,
\tag{2.5}
\]
对该图块每一对点成立。由 (2.1)，精确等价于
\[
\|R_Tx-R_Ty\|\le\sqrt{1+4\tau}\,\|x-y\|.
\tag{2.6}
\]
故 **\(\gamma=1,\ L^2=1+4\tau\)** 是准确归一化。其 **Proposition 3** 是二次能量等价式；**Proposition 4** 给出 resolvent / reflected-resolvent 对应。后者在 \(\tau<1/2\) 下把 resolvent 称为 \(\alpha=1/2\)、violation \(\varepsilon=2\tau<1\) 的 almost firmly nonexpansive 映射。代数等价 (2.5)–(2.6) 对任意有限 \(\tau\ge0\) 成立；\(\tau<1/2\) 不是“有限 Lipschitz”本身的要求，而是其术语及收敛阈值所处范围。

如果某个 \(L<1\) 有效，(2.2) 比单调性还强；它当然满足 LT 的 \(\tau=0\)，但 LT 的非负 violation 记号不记录这部分额外强度。

因此在固定有界比较尺度上，若不限制常数大小，
\[
\mathscr L_{\rm geom}
=\{T:R_T\text{ Lipschitz}\}
=\{T:T\text{ Lipschitz}\}
\subsetneq
\{T:R_T\text{ 为某一指定 }\gamma<1\text{ 的 Hölder 映射}\}.
\tag{2.7}
\]
Lipschitz 到 Hölder 使用 \(d\le R_0^{1-\gamma}d^\gamma\)。这是**几何类**包含，不是已加 EB 与兼容的证书类包含。

### 2.3 Almost-averaged 的点态与全对版本不能混用

LTT 2018 的 arXiv v2 **Definition 2.3、Proposition 2.4**（正式版不同编号）要求
\[
\|Tx-Ty\|^2+
\frac{1-\alpha}{\alpha}\|D_Tx-D_Ty\|^2
\le(1+\varepsilon)\|x-y\|^2.
\tag{2.8}
\]
如果 \(y\) 遍历整个工作域，就是 all-pairs；如果只遍历解集 \(S\)，就是相对解集的 pointwise 条件。对多值 \(T\)，每个输入/输出对仍须全量词测试。

在 \(\alpha=1/2\) 时，all-pairs (2.8) 与 (2.6) 对应 \(L^2=1+2\varepsilon\)、\(\varepsilon=2\tau\)。一般 \(\alpha\ne1/2\) 不是同一个数值切片；若 (2.8) 对全对成立，它蕴含 \(T\) Lipschitz，进而 \(R_T\) Lipschitz，但这样转换通常损失常数。

**LT 2025 Theorem 2 本身假设 all-pairs。** 正式 **Assumption 2(d)(i)** 是 maximal submonotonicity on \(U\) in \(W\)。其证明只实际调用解点比较，不能因此把该定理的假设改写为只需 pointwise。另一条不同入口是 LT **Assumption 1 / Proposition 1** 以及 LTT **Theorem 2.18 / Corollary 2.19**（v2）：它们确实允许只在解点处 pointwise almost-averaged。

最小量词反例：令
\[
F(u)=\{u,2u\},\quad\lambda=1,
\quad T(x)=\{x/2,x/3\},\quad S=\{0\}.
\tag{2.9}
\]
图闭。每个输出 \(t=ax\)、\(a\in\{1/2,1/3\}\) 都满足
\[
|t|^2+|x-t|^2\le |x|^2,
\qquad d(x,S)\le2\,d(0,(I-T)x).
\]
所以它有相对 \(S\) 的 firmly-quasi-nonexpansive 条件与线性残差界，所有轨道都几何收敛。可是同一非零输入存在两个不同输出，任何 all-pairs RL 均失败。这说明较大的 pointwise 框架不能整体包含于“完整单值 all-pairs RLEB 主定理类”；原 RLEB 的 selection-uniform 扩展是另一个需要单独命名的类。

### 2.4 Semimonotonicity 不是另一个 Luke–Tam 同义词

Evens–Pas–Latafat–Patrinos 的 **Definition 4.1**（arXiv:2305.03605v2）是
\[
\langle a,b\rangle\ge\mu\|a\|^2+\nu\|b\|^2.
\tag{2.10}
\]
RLEB \(\gamma=1\) 的平衡切片是
\[
\mu=\frac{1-L^2}{2\lambda(1+L^2)},\qquad\nu=\lambda^2\mu.
\tag{2.11}
\]
但全部 \((\mu,\nu)\) 半单调性不能未经参数限制就拿来与 RLEB 比大小。例如 \(\mu=\nu=-1/2\) 时，
\[
\langle a,b\rangle\ge-\tfrac12(\|a\|^2+\|b\|^2)
\]
对所有向量都成立。该文 **Proposition 4.3(i)** 明确说明，负参数足够大时所有算子都满足定义。“存在一些 semimonotonicity 参数”因此可能是空洞属性。

一个可核的非退化转换为：设 \(A=\lambda\mu\)、\(B=\nu/\lambda\)，且 \(1+A+B>0\)。将 (2.10) 写进 (2.1) 得
\[
\left\|z+\frac{A-B}{1+A+B}p\right\|^2
\le\frac{1-4\mu\nu}{(1+A+B)^2}\|p\|^2.
\tag{2.12}
\]
若右侧允许非平凡输入对，就得到有限反射 Lipschitz 常数
\[
L\le\frac{|A-B|+\sqrt{1-4\mu\nu}}{1+A+B}.
\tag{2.13}
\]
在 \(1+A+B\le0\) 的退化区，不能从此推出 Lipschitz 反射。预条件、矩阵 weak-Minty、相对图量词还会改变比较对象；不能与 (2.5) 混成一个“次单调类”。

## 3. 两套 EB 的位置与量词

### 3.1 LT 2025

正式 **Assumption 2(c)** 是原算子在输出邻域上的线性误差界
\[
d(u,S)\le\rho\,r_F(u).
\tag{3.1}
\]
其 **Lemma 1** 转移为输入残差界
\[
d(x,S)\le(1+\rho/\lambda)\|x-Tx\|.
\tag{3.2}
\]
证明只使用 \(r_F(Tx)\le\|x-Tx\|/\lambda\) 以及三角不等式，不需要把原算子最小残差误认成选中残差。

LTT 2018 v2 **Definition 2.17** 已允许 gauge metric subregularity，而且 **Theorem 2.18 / Corollary 2.19** 可在环域上用不同 gauge/常数。因此“把线性 EB 改成一般 gauge”本身不是 RLEB 相对全部 LTT 文献的首次内容。RLEB 的接口差异在于把原算子**输出** EB 与非线性 all-pairs 反射阶数做明确匹配。

### 3.2 RLEB direct 证书

原稿 Assumption `ass:local-rleb` 是：

- coverage：共同近解输入 \(U_{R_0}\) 都有被表示的完整或明确局部 proximal 输出，且可选最近解图点 \((p,0)\)；
- all-pairs (2.2)；
- 输出区域真实 min-residual EB (1.3)，及 gauge 定义域预算；
- 存在共同 \(0<\kappa<1\)，使
  \[
  \psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right)\le\kappa r
  \quad(0<r\le R_0).
  \tag{3.3}
  \]

它先给
\[
\|x-Tx\|\le\tfrac12(d(x,S)+Ld(x,S)^\gamma),
\tag{3.4}
\]
然后给距离收缩，并以
\[
\mathcal L(d)=\tfrac12\left(\frac d{1-\kappa}
 +\frac{Ld^\gamma}{1-\kappa^\gamma}\right)
\tag{3.5}
\]
与到工作域边界距离的严格不等式关闭留域。局部化预算不能被“每条轨道都收敛”替代。

若 \(\psi(t)=Kt^\theta\)、\(L>0\)、\(0<\gamma<1\)，direct 兼容的临界分类是
\[
\gamma\theta>1:\ \text{缩小半径可过关};\quad
\gamma\theta=1:\ K(L/(2\lambda))^\theta<1;\quad
\gamma\theta<1:\ \text{该证书失败}.
\tag{3.6}
\]
因此固定 \(\gamma<1\) 的严格层要求比线性输出 EB 强得多的近零增长；它不是“放宽 LT 的几何而保持其他条件不动”。

### 3.3 原 RLEB energy 证书不可遗漏

原稿 `prop:energy-certificate` 对连续严格递增 \(\psi\) 使用
\[
V(r)=r^2+\lambda^2[\psi^{-1}(r)]^2,
\qquad
A(r)=\tfrac12(r^2+L^2r^{2\gamma}),
\tag{3.7}
\]
要求 \(\sup_{0<r\le R_0}A(r)/V(r)<1\)，并有自己的留域预算。在线性 \(\gamma=1,\psi(t)=\rho t\) 切片上，
\[
\kappa_E^2=\frac{1+L^2}{2}\frac{\rho^2}{\rho^2+\lambda^2}.
\tag{3.8}
\]
LT 归一化 \(L^2=1+4\tau\) 给
\[
\kappa_E^2=(1+2\tau)\frac{\rho^2}{\rho^2+\lambda^2}<1
\iff 2\tau\rho^2<\lambda^2.
\tag{3.9}
\]
LT 正式 **Assumption 2(d)(ii) / Theorem 2** 的显示条件与因子为
\[
2\tau(\lambda+\rho)^2<\lambda^2,
\qquad
\kappa_{LT}^2=1+2\tau-\left(\frac\lambda{\lambda+\rho}\right)^2.
\tag{3.10}
\]
(3.10) 蕴含 (3.9)，而非反向。对同一 \(\tau,\rho,\lambda\)，
\[
\kappa_{LT}^2-\kappa_E^2
=\lambda^2\left[\frac{1+2\tau}{\rho^2+\lambda^2}
-\frac1{(\lambda+\rho)^2}\right]>0
\quad(\rho>0,\tau\ge0).
\tag{3.11}
\]
这是共同过渡不等式上的代数比较；它不自动比较不同局部化区域、不同截断 graph 或所有可用替代证明。

## 4. 精确包含与不包含

预先固定完整接口、解集、工作域及留域方式，再命名：

| 类 | 定义核心 | 不得删去的部分 |
|---|---|---|
| \(\mathscr L_{\rm geom}\) | 有限 LT all-pairs submonotonicity，等价反射局部 Lipschitz | 固定步长、图块、全对量词 |
| \(\mathscr L_{\rm cert}\) | 共同接口上的 (2.5)、(3.1)、(3.10) | coverage、输出域、留域 |
| \(\mathscr L_{\rm paper}\) | LT 2025 Theorem 2 实际实例输送到同一完整接口 | 原有 maximality/self-map 条件以及局部完整纤维识别 |
| \(\mathscr R_H\) | all-pairs RL + 真 EB + direct (3.3) | 一致半径与 (3.5) |
| \(\mathscr R_E\) | all-pairs RL + 真 EB + energy (3.7) | energy 自己的预算 |
| \(\mathscr R_{DE}\) | \(\mathscr R_H\cup\mathscr R_E\) | 不许遗漏指数一层 |
| \(\mathscr A_{\rm point}\) | 相对解集的 pointwise almost-averaged + 对应 EB | 可多值，不是连续映射母空间的天然子类 |

在同一局部接口经必要缩域后，安全关系是
\[
\mathscr L_{\rm paper}\subseteq\mathscr L_{\rm cert}
\subseteq\mathscr R_E\subseteq\mathscr R_{DE}.
\tag{4.1}
\]
这里第一步指已经验证完整接口一致的 LT 实例，不能从任意裁剪 LT 轨道推成完整 PPA。后两步由 (3.9)–(3.10) 及共同 coverage/预算得到。

**几何扩大严格的原有证据。** 原 RLEB 二维例子
\[
F(\xi,y)=\{(-2\sqrt y,3y),(-2\sqrt y,-5y)\}\ (y\ge0),
\quad T(p,r)=(p+\sqrt{|r|},|r|/4)
\tag{4.2}
\]
具有完整图和真实 \(d(u,S)\le r_F(u)^2/4\)，严格 direct 兼容。可是取 \(x_t=(0,t),s=(0,0)\)，
\[
\frac{\|Tx_t-Ts\|}{\|x_t-s\|}
=\frac{\sqrt{t+t^2/16}}t\longrightarrow\infty.
\tag{4.3}
\]
故它既不在 \(\mathscr L_{\rm geom}\)，也不在相同完整邻域的任何有限 pointwise-Lipschitz-at-\(s\) almost-averaged 层。它证明非空差类；**不证明差类稠密或余稀**。

**只用 direct 则不包含 LT。** 令 \(\lambda=1\)，
\[
F(z,r)=(0,r/2),\quad T(z,r)=(z,2r/3),\quad S=\mathbb R\times\{0\}.
\tag{4.4}
\]
这是 maximal monotone；LT 可取 \(\tau=0\)、最佳线性 EB \(\rho=2\)。由于反射在切向是恒等，\(\gamma=1\) 时任何全对 RL 常数都满足 \(L\ge1\)。任何有效 gauge 在近零须 \(\psi(t)\ge2t\)，因此 direct 比值至少为 \(1+L\ge2\)，不能小于一。\(\gamma<1,L>0\) 时该比值更趋于无穷。故 (4.4) 属于 LT 而不属于任何 local direct-RLEB 证书；energy 则给 \(\kappa_E=2/\sqrt5<1\)。

**Maximality 的边界。** 如果完整 \(T:H\to H\) 的 \(R_T\) 在全空间 Lipschitz，且其对应 \(F_T\) 全图满足 (2.5)，那么 \(F_T\) 在相同 violation 下全局 maximal：假设可添加 \((u,a)\)，与已有同 Minty 输入 \(x=u+\lambda a\) 的图点比较，(2.5) 的右侧为零而左侧为 \(-\|u-Tx\|^2\)，故新增点必与已有点相同。局部“内 collar 完整”不自动证明 LT 所要求的整个 \(U\times W\) 上 maximality；若用 maximal extension 补足，须说明扩展及其保持原内部纤维的证明，不能悄悄换对象。

**不能由 Lipschitz 直接推出 LT 可认证。** 对任意有限反射 Lipschitz 常数可以定义 \(\tau\)，但它可能 \(\ge1/2\)，导致 (3.10) 无法成立，或缺少 EB。于是 \(\mathscr L_{\rm cert}\subsetneq\mathscr L_{\rm geom}\) 的限制是实质性的。若要比较“旧理论覆盖量”，不能把整个 Lipschitz 类冒称 LT Theorem 2 覆盖类；不过以 Lipschitz 作旧类的上界，能给更强的差类排除。

## 5. 可数化与可测性：必须保留临界指数

本节不替空间架构组选择拓扑；只提供在 \(C_{\rm loc}(H,H)\) / 固定紧域 uniform 拓扑下可复用的编码。

### 5.1 Lipschitz 层

对固定紧输入块 \(K\)，
\[
\mathscr L_m(K)=\{T:\|R_Tx-R_Ty\|\le m\|x-y\|\ (x,y\in K)\}
\tag{5.1}
\]
是闭集。因此 \(\bigcup_m\mathscr L_m(K)\) 是 \(F_\sigma\)。若要求在 \(H\) 上处处局部 Lipschitz，可用紧球耗尽得到 \(\bigcap_j\bigcup_m\mathscr L_m(K_j)\)。若要求只在固定解点的某邻域存在同一常数，则是对半径与常数的可数并。三种量词产生的集合不应混用。

### 5.2 固定幂指数的证书层

预先固定 \(\gamma,\theta,\lambda\)，对 \(L,K,R_0,\kappa\) 及域/预算做带严格余量的可数包络通常可行，因为略增 \(L,K\)、略缩 \(R_0\)、略放宽 \(\kappa<1\) 可保持严格证书。然而不要把这个事实扩张为所有指数都能取有理数。

若真实最佳指数为无理 \(\gamma_0\)，真实最高 EB 幂为 \(\theta_0=1/\gamma_0\)，则临界兼容 \(\gamma_0\theta_0=1\)。降低 \(\gamma\) 或 \(\theta\) 会破坏兼容；提高任一指数又可能破坏 RL 或 EB。因此有理指数对的并集可能遗漏真实临界成员。

### 5.3 保留全部实指数的 power 证书可数编码

固定共同完整接口与域，取有理半径 \(R_j\)。令
\[
P_n=\{(\gamma,\theta,L,K,\kappa):
1/n\le\gamma\le1,\ 1/n\le\theta\le n,
0\le L\le n,\ 1/n\le K\le n,
0\le\kappa\le1-1/n\}.
\tag{5.2}
\]
在 \(\mathscr X\times P_n\) 上联合要求：

1. 固定输入块的 all-pairs (2.3)；
2. 全纤维版本的 \(d(Tx,S)\le K(\|x-Tx\|/\lambda)^\theta\)；
3. 对所有 \(0<r\le R_j\)，
   \[
   K\left(\frac{r+Lr^\gamma}{2\lambda}\right)^\theta\le\kappa r.
   \tag{5.3}
   \]

这些是关于 \((T,\gamma,\theta,L,K,\kappa)\) 的闭条件（在本段固定的完整域接口上）。\(r=0\) 不产生额外条件；正 \(r\) 上各函数连续。因 \(P_n\) 紧，闭证书关系对 \(T\) 的投影仍闭；再对 \(n,j\) 可数并，可得该固定接口下 power direct 证书类的相对 \(F_\sigma\) 描述。**这是紧实实参数投影，不是把无理指数删掉。**

局部化时，必须把输入块、输出区、完整纤维、gauge 阈值及留域预算一并纳入编码。对固定开输出区 \(V\)，全输入条件“\(Tx\in V\Rightarrow\) EB”具有适当的闭极限性质：若 \(T_n\to T\) 且 \(Tx\in V\)，则最终 \(T_nx\in V\)。但随 \(T\) 改变的任意 graph localization、任意未知轨道域不能直接套用本段结论。全空间 EB 版本或事先规定的双 collar 证书层最清楚。

### 5.4 任意 gauge

如果先限制连续 gauge，可以用 \(C([0,\bar t])\) 的 Polish 参数空间作 witness。若联合 RL/EB/兼容/域条件可证明 Borel，则其存在量词投影是 analytic，因而具有 Baire 性质；它未必就是 \(F_\sigma\)。

原稿 gauge 只要求单调、在零点趋零，并不处处连续。要把全体此类 gauge 无损变成连续 witness 类，应独立证明“存在保兼容余量的连续 majorant”或给出单调函数的标准 Borel 编码。本报告不把这一步当作已经完成。选一个可数的幂/对数 gauge 字典能给可控子体系，但不能称之为全部 RLEB。

## 6. 对“在纲分类下多多少”的直接意义

现在至少能把目标写清楚，而不靠单个反例的参数爆破：
\[
\boxed{\text{在预先合理给定的 Baire 母空间 }\mathscr X\text{ 中，研究 }
\mathscr X\cap(\mathscr R_{DE}\setminus\mathscr L_{\rm geom})\text{ 的范畴大小。}}
\tag{6.1}
\]
还应同时比较 \(\mathscr X\cap\mathscr R_{DE}\)、\(\mathscr X\cap\mathscr L_{\rm cert}\)、以及未被二者认证的剩余类。

必要的研究边界：

- 不能选择一个只收 \(\gamma<1\)+固定 superlinear EB 的母层，再把普通 LT 线性 EB 例子排除，最后宣布 LT 小；那是定义筛选。
- 也不能只在所有连续函数中套“Lipschitz 小”就称为 RLEB 新定理，因为 all-pairs RL 本身就是反射 Hölder 的坐标翻译。承重部分是**完整 operator fibers、真实 min-residual EB、兼容与共同留域预算约束下**的范畴结论。
- 算子有多少个证书，不等于有多少个不同算子。若使用 \((T,\gamma,L,\psi,\ldots)\) 的带标签空间，最后必须说明遗忘标签投影后还剩什么结论。
- 若 \(\mathscr R\setminus\mathscr L\) 是 residual，只能说在所声明的拓扑与母类中新增覆盖是范畴意义上典型。它不等于概率一、数值上常见、自然应用必多，更不单独完成优先权证明。
- 进入 Hilbert 空间可以是下一步，但原稿的闭集最近点、有限维紧性、min-residual 达到、全纤维编码和拓扑完备性不能不核就照搬。

## 7. 已读原始文献与精确对应

1. **D. Russell Luke, Matthew K. Tam, _Generalized Monotonicity and the Proximal Point Algorithm_**, Mathematics of Operations Research，2025 online，DOI [10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)。已核正式 13 页原文：Definition 2，Propositions 3–4，Lemma 1，Assumptions 1–2，Theorem 2。定义/编号基于当前工作区 `c01_luke_tam.pdf` 和原刊页面。它提供 all-pairs 二次几何与局部 PPA 收敛，并非算子类的 Baire 大小定理。
2. **D. Russell Luke, Nguyen H. Thao, Matthew K. Tam, _Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings_**, Mathematics of Operations Research 43 (2018), 1143–1176，DOI [10.1287/moor.2017.0898](https://pubsonline.informs.org/doi/10.1287/moor.2017.0898)，[arXiv:1605.05725v2](https://arxiv.org/abs/1605.05725v2)。已核 v2 Definition 2.3，Propositions 2.4、2.6、2.8，Definition 2.17，Theorem 2.18，Corollary 2.19；本报告不把 v2 号码冒称正式刊本号码。其 gauge regularity 与 pointwise AA 框架须与 LT 2025 的完整局部 all-pairs 定理分开。
3. **同三位作者，_Implicit Error Bounds for Picard Iterations on Hilbert Spaces_**, Vietnam Journal of Mathematics 46 (2018), 243–258，DOI [10.1007/s10013-018-0279-x](https://link.springer.com/article/10.1007/s10013-018-0279-x)，[作者上传正式全文](https://www.researchgate.net/profile/Hieu-Thao-Nguyen/publication/323317906_Implicit_Error_Bounds_for_Picard_Iterations_on_Hilbert_Spaces/links/5a8eb28eaca27214055d9692/Implicit-Error-Bounds-for-Picard-Iterations-on-Hilbert-Spaces.pdf)。本轮直接核 Definition 1、Theorems 1–4 及相关证明。Theorems 1–2 用非扩张/averaged 与函数/规范 gauge EB；Theorem 4 不假设非扩张，从 bounded-set 上一致严格距离下降推出输入残差 EB。这是已有抽象 EB 接口，不是新的类别包含证据。
4. **Brecht Evens, Pieter Pas, Puya Latafat, Panagiotis Patrinos, _Convergence of the Preconditioned Proximal Point Method and Douglas–Rachford Splitting in the Absence of Monotonicity_**，[arXiv:2305.03605v2](https://arxiv.org/abs/2305.03605v2)，正式 DOI [10.1007/s10107-024-02182-0](https://doi.org/10.1007/s10107-024-02182-0)。本报告公式与号码按已读 v2 Definition 4.1、Remark 4.2、Proposition 4.3；正式 DOI 仅作书目信息，未将版本号强行对齐。无参数限制的 semimonotone 并集会退化为全部算子。

## 8. 尚未解决与移交其他组

1. 合理母空间的最终选择及 Baire 性，交架构组；不能由本报告的 \(F_\sigma\) 编码替代完备性证明。
2. 差类 residual / meagre / dense / nowhere dense 的任一个结论，均需在最终母空间单独证明。本报告只证明几何身份、严格非空差与公共数值证书包含。
3. 原 LT 矩形局部 maximality 与指定完整 collar 的精确互换，须在具体母空间定义后关闭。
4. 任意不连续单调 gauge 的无损 Polish witness 编码或连续 majorant 引理，未在本轮完成。
5. 无限维 Hilbert 版本的最近点、residual 达到与 compact-open / bounded-uniform 区别，未在本轮完成。
6. 不能把本报告的公共证书比较当作“RLEB 已严格包含 Luke–Tam 所有理论”；若目标改为全体 LTT pointwise 算法关系，应另建集合值迭代关系空间，并纳入原 RLEB selection-uniform 版本。

**组内终判：精确定义转换 PASS；全体系不加限定的 LT⊂RLEB 声明不通过；在完整共同接口、direct+energy 双证书及指定 LT2025 all-pairs 口径下，有可用于后续纲比较的严格扩张。**
