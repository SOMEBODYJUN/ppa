# RLEB 与 Luke–Tam 的算子空间／纲比较：最终综合判定

日期：2026-09-20。范围：综合本轮 `01–08` 的定义翻译、空间构造、独立证明、数学复审、文献优先权与自然性审计；不重新审查原 RLEB 论文中与本问题无关的成果。数学审计 `06` 已在修补后更新为 **PASS**，R1–R4 均已关闭。

## 0. 给作者的直白结论

**你的入手点有意义，而且这次确实已经得到一个算子空间里的定理，不再只是原例子的参数试验。**

已经证明的结果是：在一个明确的、真正无限维的算子层中，RLEB 可以统一认证全部成员；能够在指定解点附近取得 Luke–Tam 2025 的局部 all-pairs 证书的成员，**即使允许为同一个原算子任意选择正步长，也只占第一纲**。新增覆盖包含一个稠密的 \(G_\delta\) 集。这个层具有固定的非单点解集、完整 proximal 解、真实最小残差误差界和共同严格 RLEB 预算，里面也确实有非退化的经典单调／LT 成员。

所以，**新增覆盖不是几个孤立反例；在已建立的这个结构层内，它在范畴意义上是典型的。** 这是可以保留的正成果。

但还不能把它改写成“全部 RLEB 中，Luke–Tam 只有第一纲”。当前层额外规定了法向超线性吸引，尚不是仅由 RLEB 条件本身定义的最大证书层。你真正要问的完整理论覆盖量问题，仍有一条关键桥梁未完成。

最终判定应分开记为：

| 判定对象 | 本轮结论 |
|---|---|
| 下文精确的相对层定理及任意步长加强 | **数学通过** |
| 全部 RLEB 相对全部 Luke–Tam/LTT 的大小 | **尚未完成，且须先区分接口** |
| 精确组合定理的原创性 | **有可辨识的新结果候选；优先权尚未完全清关** |
| 现在是否值得写入研究论文 | **值得，作为准确限定范围的实质增强章节** |

“第一纲”不是百分比或零测；它表示这个例外类包含在可数个闭无处稠密层的并中。这里的补集既稠密又含稠密 \(G_\delta\)，但不代表某种未指定随机模型下的概率一。

## 1. 先把三个 Luke–Tam 口径与两条 RLEB 证书分开

统一使用同一个完整 proximal 接口

\[
T=J_{\lambda F}=(I+\lambda F)^{-1},\qquad
R_T=2T-I,\qquad S=\operatorname{zer}F.
\]

比较局部结果时，须先核对两边使用同一完整图、输出区域、初值邻域和覆盖关系，不能允许一边删去分支而另一边必须检查全图。

| 旧理论口径 | 实际要求 | 与 direct-RLEB 的关系 | 与 energy-RLEB／两通道并集的关系 |
|---|---|---|---|
| **LT all-pairs 几何类** \(\mathcal L_{\rm geom}\) | 同一图块上的有限 submonotonicity；在完整输入坐标中等价于 \(R_T\) Lipschitz | 只是 RL 的 \(\gamma=1\) 几何端点；没有 EB 与兼容条件就不能推出 direct 证书 | 同样不能只由几何性质推出 energy 收敛证书 |
| **LT2025 Theorem 2 收敛类** \(\mathcal L_{\rm cert}\) | 上述几何、线性真实 EB、局部 maximality、覆盖／留域和数值阈值同时成立 | **不包含于 direct 类**；有明确单调线性反例 | 在公共完整接口核准后，证书可送入线性 energy 层，故 \(\mathcal L_{\rm cert}\subseteq\mathcal R_E\subseteq\mathcal R_D\cup\mathcal R_E\) |
| **LTT pointwise／relative 框架** \(\mathcal A_{\rm point}\) | 只相对解点／参考集的 almost-averaged 条件，配相应 EB；可允许多值关系及受限比较域 | 不能整体等同 all-pairs RL，也不能未经限定宣称包含 | 与完整单值 all-pairs RLEB 主定理类一般不可直接排成包含链；须逐一限定量词 |

第一、二行基于 Luke–Tam 的 *Generalized Monotonicity and the Proximal Point Algorithm*，Definition 2、Propositions 3–4、Assumption 2、Theorem 2，DOI [10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863)。第三行的精确 pointwise/gauge 接口见 Luke–Thao–Tam，*Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings*，DOI [10.1287/moor.2017.0898](https://doi.org/10.1287/moor.2017.0898)，本轮所用 Definition 2.3、Proposition 2.4、Theorem 2.18、Corollary 2.19 的编号按 [arXiv v2](https://arxiv.org/abs/1605.05725v2)，不冒称正式刊本编号。

### 1.1 精确的几何与证书字典

对任意图点差 \(a=u-v\)、\(b=u^*-v^*\)，令 \(x-y=a+\lambda b\)。恒等式

\[
4\lambda\langle a,b\rangle
=\|a+\lambda b\|^2-\|a-\lambda b\|^2
\]

给出

\[
\text{LT all-pairs}:
\quad\lambda\langle a,b\rangle\ge-\tau\|a+\lambda b\|^2
\quad\Longleftrightarrow\quad
\|R_Tx-R_Ty\|\le\sqrt{1+4\tau}\|x-y\|;
\tag{1.1}
\]

\[
\text{RL}(\gamma,L):
\quad\|R_Tx-R_Ty\|\le L\|x-y\|^\gamma.
\tag{1.2}
\]

这说明几何层确实由 Lipschitz 端点扩展到 Hölder 模，但不能因此略去 EB 的配对要求。

若线性输出 EB 为 \(d(u,S)\le\rho\,r_F(u)\)，则公共数值证书满足

\[
\begin{array}{ll}
\text{LT2025：}&2\tau(\lambda+\rho)^2<\lambda^2,\\[2pt]
\text{RLEB energy：}&2\tau\rho^2<\lambda^2,
\qquad
\kappa_E^2=(1+2\tau)\dfrac{\rho^2}{\rho^2+\lambda^2}.
\end{array}
\tag{1.3}
\]

第一条件蕴含第二条件。这里比较的是共同接口上的证书，不是宣称原论文的任意局部图块可以自动互换。

### 1.2 两个最小反例保护比较口径

**direct 不包含全部 LT。** 取 \(\lambda=1\)、

\[
F(z,r)=(0,r/2),\quad T(z,r)=(z,2r/3),\quad S=\mathbb R\times\{0\}.
\]

这是 maximal monotone，LT 可取 \(\tau=0,\rho=2\)。切向恒等迫使指数一反射常数 \(L\ge1\)，任何有效 gauge 近零满足 \(\psi(t)\ge2t\)，故 direct 兼容比至少为 \(1+L\ge2\)。energy 则成立。不能为得到大包含而漏掉这一个通道。

**pointwise 不等于 all-pairs。** 取 \(F(u)=\{u,2u\}\)、\(\lambda=1\)，则完整 \(T(x)=\{x/2,x/3\}\)。它满足相对零点的 firmly-quasi-nonexpansive 不等式及线性输入残差界，但同一非零输入有两个不同输出，故任何完整 all-pairs RL 都失败。反过来，已有 RLEB 平方根切向例子在解点处不满足有限 Lipschitz calmness，因此也不能直接归入完整邻域的 pointwise-AA 类。

这不是说整个研究方向已知或不成立，而是先把真正可比较的集合定义清楚。

## 2. 已经成立的主定理：一个真正的无限维相对层

### 2.1 自然语言陈述

固定一个非单点仿射解集，允许所有满足同一小尺度反射 Hölder 上界和法向超吸引预算的连续单步映射。它们构成一个紧致、无限维、凸的 Baire 空间；不要求三角公式，不要求有限参数表达。

每个映射都能实现为某个闭图多值算子的**完整** resolvent，并共用真实最小残差 EB、严格 RLEB 证书和初值管域。在这个空间内，若要求原算子在指定解点附近由 LT2025 的 all-pairs 图条件认证，那么即使允许改变步长，可认证者仍是第一纲。

### 2.2 精确公式

设 \(E=\mathbb R^d\)，\(S\) 是真非单点仿射子空间；平移后令 \(0\in S\)，故 \(1\le\dim S<d\)。固定

\[
\lambda>0,\quad 0<\gamma<1,\quad \nu=1/\gamma,
\quad0<q<1,\quad R>0,\quad A>R^{1-\gamma},
\]

并假设

\[
\kappa_*:=\frac{q}{(1-q)^\nu}
\left(\frac{R^{1-\gamma}+A}{2}\right)^\nu<1.
\tag{2.1}
\]

令 \(\mathcal Y\) 为所有连续 \(T:E\to E\) 满足

\[
T|_S=I,
\tag{2.2}
\]

\[
\|R_Tx-R_Ty\|\le A\|x-y\|^\gamma
\quad\bigl(x,y\in E,\ \|x-y\|\le R\bigr),
\tag{2.3}
\]

\[
d(Tx,S)\le q\min\{d(x,S)^\nu,d(x,S)\}
\quad(x\in E).
\tag{2.4}
\]

赋予紧集上一致收敛拓扑

\[
d_{\rm loc}(T,U)=\sum_{j\ge1}2^{-j}
\min\{1,\|T-U\|_{\overline B_j(0)}\}.
\tag{2.5}
\]

对每个 \(T\in\mathcal Y\)，定义整个算子

\[
F_T(u)=\{(x-u)/\lambda:Tx=u\}.
\tag{2.6}
\]

则下列结论成立。

**（a）空间与完整接口。** \(\mathcal Y\) 非空、凸、无限维，且为紧致 Polish/Baire 空间；\(F_T\) 闭图，

\[
J_{\lambda F_T}=T\quad\text{在整个 }E\text{ 上},
\qquad\operatorname{zer}F_T=\operatorname{Fix}T=S.
\tag{2.7}
\]

**（b）共同真残差证书。** 全部成员满足同一 all-pairs RL、全覆盖，以及

\[
d(u,S)\le\psi(r_{F_T}(u)),\qquad
\psi(t)=q\left(\frac{\lambda t}{1-q}\right)^\nu,
\tag{2.8}
\]

这里的 EB 对 \(u\in\operatorname{dom}F_T=\operatorname{ran}T\) 陈述，其中

\[
r_{F_T}(u)=\operatorname{dist}(0,F_T(u))
=\frac1\lambda\inf_{Tx=u}\|x-u\|
\tag{2.9}
\]

是整个值集的最小范数，非选中分支残差。严格兼容常数正是 (2.1)。还共同满足线性 EB

\[
d(u,S)\le\frac{\lambda q}{1-q}r_{F_T}(u).
\tag{2.10}
\]

因此本层 LT 的不足并非由人为撤掉线性 EB 造成；排除来自其几何要求。

**（c）共同收敛域与尾界。** 对任意 \(0<\rho\le R\)，管域 \(V_\rho=\{x:d(x,S)\le\rho\}\) 对所有成员前向不变，迭代趋于 \(\Pi_Tx\in S\)，且

\[
\|T^kx-\Pi_Tx\|
\le\frac{\rho q^k}{2(1-q)}+
\frac{A\rho^\gamma q^{\gamma k}}{2(1-q^\gamma)}.
\tag{2.11}
\]

这里 \(q\) 是 (2.4) 给出的实际统一法向上界，\(\kappa_*\) 是保守 RLEB 证书，不混作同一数值。

**（d）任意步长的 LT all-pairs 类第一纲。** 固定 \(s\in S\)。令 \(\mathcal L_{\rm any}^{\rm ap}(s)\) 为 \(T\in\mathcal Y\) 中满足下述属性者：存在 \(\mu>0\)、有限 \(\tau\ge0\)、\(s\) 的开邻域 \(U\)、\(0\) 的开邻域 \(W\)，对 \(\mu F_T\) 的全部局部图点

\[
u,v\in U,\qquad a\in\mu F_T(u)\cap W,
\qquad b\in\mu F_T(v)\cap W,
\]

成立

\[
\langle u-v,a-b\rangle
\ge-\tau\|(u+a)-(v+b)\|^2.
\tag{2.12}
\]

则

\[
\boxed{\quad\mathcal L_{\rm any}^{\rm ap}(s)
\text{ 在 }\mathcal Y\text{ 中第一纲。}\quad}
\tag{2.13}
\]

故存在稠密 \(G_\delta\) 子集 \(\mathcal G_s\subset\mathcal Y\)，其中每个 \(F_T\) 在任何正步长下都不满足上述 LT 局部 all-pairs 几何条件。LT2025 的完整收敛证书比 (2.12) 还强，故其可认证类也为第一纲。

这是**固定指定解点 \(s\)** 的定理。它没有把关于每个 \(s\) 分别成立的结果，未经证明变成对不可数多个解点同时成立的一个残集声明。

**（e）固定原步长的 pointwise 边界。** 若 \(T=J_{\lambda F_T}\) 在 \(s\) 的完整输入邻域满足

\[
\|Tx-s\|^2+
\frac{1-\alpha}{\alpha}\|x-Tx\|^2
\le(1+\varepsilon)\|x-s\|^2,
\quad0<\alpha<1,\quad\varepsilon<\infty,
\tag{2.14}
\]

它必有 \(\|Tx-s\|\le\sqrt{1+\varepsilon}\|x-s\|\)。此 **calmness** 类在 \(\mathcal Y\) 中也第一纲。因此固定 \(\lambda\)、完整邻域的 pointwise-AA 类亦第一纲。

这是单独证明的点态结论，不是把 calmness 当成两点 Lipschitz；也不排除任意其他步长下仅锚定单个解点的所有 pointwise-AA 接口。低维受限比较集不含法向测试线时，本定理同样不适用。

### 2.3 不是空比较，也不依赖无限值算子

在最小二维模型 \(E=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\) 中，只要 \(q\nu\le1\)，

\[
T_0(z,r)=\bigl(z,q\operatorname{sgn}(r)
\min\{|r|^\nu,|r|\}\bigr)
\tag{2.15}
\]

就是同层非退化的 firmly nonexpansive 完整 resolvent；对应原算子单值、maximal monotone，并有 (2.10) 的线性 EB。它真正满足 LT 单调情形，不只是几何上 Lipschitz 的样本。

一组已验预算为

\[
\gamma=\tfrac12,\quad\nu=2,\quad q=\tfrac1{16},
\quad R=\tfrac1{16},\quad A=\tfrac{13}{16},
\quad\kappa_*=\tfrac{289}{14400}<1.
\]

同层还可容纳 \(T_*(z,r)=(z+\tfrac14|r|^{1/2},g(r))\)，其中 \(g\) 是 (2.15) 的法向分量；它也是全空间同胚，但在解点附近非 Lipschitz。

另外，报告 `05` 独立构造了

\[
T_h^-(z,r)=\bigl(z+h(r),q\min\{|r|^\nu,|r|\}\bigr),
\quad h(0)=0,\quad[h]_\gamma\le H,
\tag{2.16}
\]

其中 \(h\in C([-1,1])\) 遍历整个锚定 Hölder 函数球，并用 \(h(\max\{-1,\min\{1,r\}\})\) 延拓到全轴。另取预算 \(2H+(1+2q\nu)R^{1-\gamma}\le A\)，便使整个切片落入同一 \(\mathcal Y\)。完整原算子在正法向输出处恰有两值；该切片与无限维紧函数球同胚，固定步长 LT all-pairs 类在其中第一纲。这是该切片内的独立证明，**不是**把 \(\mathcal Y\) 的残集随意限制到所有二值算子。

signed 单纤维切片还有更细的已证结论：实际 LT germ 类在一致拓扑中可以同时稠密且第一纲，且允许任意正步长的 all-pairs 可认证类仍第一纲。稠密不反驳第一纲；邻域会随逼近缩小，不能写成固定共同域的 LT 证书稠密。

## 3. 证明的承重机制：哪些是真的桥，哪些是标准工具

### 3.1 完整图与真实 EB

(2.6) 使

\[
u\in J_{\lambda F_T}(x)\iff Tx=u.
\]

完整图是连续 \(T\) 的图经可逆线性坐标变换所得，故闭。由 (2.4)，对每一个输入都有

\[
\|x-Tx\|\ge(1-q)d(x,S),\qquad
d(Tx,S)\le qd(x,S)^\nu.
\]

于是 (2.8) 对每个输出的全部原像成立，再取整个纤维的下确界。这个量词桥梁不能省略，但其基本代数并不复杂。

### 3.2 空间先成立，再使用 Baire

反射模给共同单步模 \((t+At^\gamma)/2\)；结合 \(T0=0\)，沿线段分段得到每个闭球上的共同有界性。有限维 Arzelà–Ascoli、逐球对角抽取与闭条件给紧致性。\(S\) 仿射使距离函数凸，三项定义因此保持凸组合。

这一步建立的是整个函数空间，不是“挑几个参数再解释其占比”。状态空间虽有限维，映射空间已经无限维。不能原样把紧性证明搬到无限维 Hilbert 状态空间。

### 3.3 任意步长统一排除的关键必要条件

假设 (2.12) 在某 \(\mu>0\) 成立。记

\[
c=\mu/\lambda,\quad u=Tx,\quad a=c(x-u),
\quad z=u+a=cx+(1-c)u,\quad p=P_Sz.
\]

当 \(x\to s\)，图点 \((u,a)\) 与 \((p,0)\) 均进入实际局部图块。由 (2.12)，

\[
\|u-p\|^2+\|a\|^2
\le(1+2\tau)d(z,S)^2,
\]

而

\[
d(z,S)\le[c+|1-c|q]d(x,S).
\]

所以必有

\[
\boxed{
\|Tx-x\|\le
\sqrt{1+2\tau}\frac{c+|1-c|q}{c}\,d(x,S)
\quad(x\text{ 在 }s\text{ 附近}).}
\tag{3.1}
\]

这是本轮值得保留的比较加强：同一个原算子**无论换成哪个正步长**得到 LT 图证书，都必须满足同一种线性位移条件。不要求新步长 resolvent 全局存在或单值，也不要求 \(x\mapsto z\) 可逆。

### 3.4 可数闭层与空内点

令

\[
\mathcal D_{m,j}(s)=\{T\in\mathcal Y:
\|Tx-x\|\le m d(x,S)
\quad\forall x\in\overline B_{1/j}(s)\}.
\]

它们对局部一致拓扑闭。取切向单位向量 \(e\)、法向单位向量 \(n\)，以及

\[
T^\sharp x=P_Sx+b\,d(x,S)^\gamma e,
\quad0<b\le\frac{A-R^{1-\gamma}}2.
\]

它属于 \(\mathcal Y\)。对 \(T\in\mathcal D_{m,j}(s)\)，凸组合 \(T_\theta=(1-\theta)T+\theta T^\sharp\) 保持全部证书并趋近 \(T\)，但沿 \(x=s+tn\)，

\[
\frac{\|T_\theta x-x\|}{d(x,S)}
\ge\theta b t^{\gamma-1}-(1-\theta)m\longrightarrow\infty.
\]

故每个 \(\mathcal D_{m,j}\) 无内点。所有可选步长的 LT 成员都由 (3.1) 落入同一个可数并 \(\bigcup_{m,j}\mathcal D_{m,j}\)，因而第一纲。**没有使用“不可数个第一纲集的并仍第一纲”这一错误推理。**

这里的凸混合是对已建立的全空间做无内点证明的工具，不是从一条参数曲线推断全体算子的比例。Baire 与凸混合本身是经典方法；承重的本项目接口是这些变动仍保持真实 EB、完整算子与共同严格证书。

## 4. 是否已有算子空间与纲分类？有，而且直接相关

不需要从零发明这套语言。以下原始论文的定理已由本轮文献／优先权组核读；详细假设对应及版本编号见 `02`、`07`。

| 原始论文与定理 | 已经做过的事 | 不能由此自动推出的本项目结论 |
|---|---|---|
| Xianfu Wang，*Most Maximally Monotone Operators Have a Unique Zero and a Super-regular Resolvent*，2013；Corollary 3.10，Propositions 2.1、2.3–2.4；[DOI 10.1016/j.na.2013.03.008](https://doi.org/10.1016/j.na.2013.03.008)，[arXiv:1301.6443](https://arxiv.org/abs/1301.6443) | 自然完备的单调算子／resolvent 空间；强单调子类第一纲 | 固定非点 \(S\) 的当前 RLEB 层；其泛型唯一零点不能限制到多解层 |
| Heinz H. Bauschke、Jason Schaad、Xianfu Wang，*On Douglas–Rachford Operators That Fail to Be Proximal Mappings*；Theorem 3.1；[DOI 10.1007/s10107-016-1076-5](https://doi.org/10.1007/s10107-016-1076-5)，[arXiv:1602.05626](https://arxiv.org/abs/1602.05626) | 在对称极大单调线性关系对空间中，产生 proximal DR 映射的子类闭且无处稠密 | 一般非线性 RLEB／LT 的完整覆盖比较 |
| Dan Butnariu、Simeon Reich、Alexander J. Zaslavski，*Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces*，2001；Theorems 2.1、3.1–3.2，Lemma 4.1；[DOI 10.1515/JAA.2001.151](https://doi.org/10.1515/JAA.2001.151)，[作者原稿](https://math.haifa.ac.il/dbutnaru/publications/but-rei-zas-jaa.ps) | 固定可为非单点的闭凸集，建立相对非扩张映射空间；泛型迭代收敛到 retraction，并研究稳定性 | 本文反射 Hölder、全纤维 EB、严格预算、LT 任意步长第一纲组合；在欧氏完整仿射集情形，其相对非扩张性还强迫切向分量不漂移 |
| Davide Ravasini，*Generic Uniformly Continuous Mappings on Unbounded Hyperbolic Spaces*，2024；Theorem 3.3；[DOI 10.1016/j.jmaa.2024.128440](https://doi.org/10.1016/j.jmaa.2024.128440)，[arXiv:2308.15277v2](https://arxiv.org/abs/2308.15277v2) | 固定凹连续模空间中，泛型映射达到允许的全局模；Hölder 层中 Lipschitz 的“小”已有背景 | 指定解点附近的局部粗糙性、固定 \(S\)、RLEB 与纤维约束；环境残集不会自动留在受约束子空间中 |

另一个有用基线是 Planiden–Wang 的 *Strongly Convex Functions, Moreau Envelopes and the Generic Nature of Convex Functions with Strong Minimizers*，Theorems 4.11–4.12：在相应 Moreau／epi 拓扑中，强凸类稠密且第一纲；Theorem 4.16 给强极小值的泛型性。这说明一个有力充分条件占小类，并不使其理论变成差理论。[DOI 10.1137/15M1035550](https://doi.org/10.1137/15M1035550)

尚未闭合的原文缺口包括 Reich–Zaslavski 1999 的 *Convergence of Generic Infinite Products of Nonexpansive and Uniformly Continuous Operators*，DOI [10.1016/S0362-546X(98)00080-7](https://doi.org/10.1016/S0362-546X(98)00080-7)，以及 Strobin 2012 的 *Some Porous and Meagre Sets of Continuous Mappings*。本轮不填造其定理号，也不把未取得全文解释成没有先例。

**正确的优先权结论是两面都保留：**经典空间与范畴方法不是新发明；但已核论文也没有直接给出本轮完整受约束的组合定理。不能因为用了经典工具就把整个结果判成已知，也不能因为检索未见同一句话就宣布首创。

## 5. 当前结果为什么仍没有回答“全 RLEB 多多少”

\(\mathcal Y\) 的法向条件 (2.4) 是额外动力学假设，并非一般 RLEB 的等价重写。普通 LT 映射

\[
T_a(z,r)=(z,ar),\qquad0<a<1,
\]

不在此层，因为近零不可能有 \(a|r|\le q|r|^{1/\gamma}\)。原来的正几何法向率、平方根切向漂移 RLEB 例子也不在这个层。它同时遗漏了双方的其他机制。

而且，(2.4) 加 (2.3) 本身就给出可求和步长及 (2.11) 的收敛。故本节证明的是**两套认证条件在一个规范结构层内的覆盖分离**，不是证明“只有 RLEB 的理论才能证明这些成员收敛”。

同样，本结果不在统计“坏初值选择”。\(T^\sharp\) 一步进入 \(S\)，其极限选择就是 \(\Pi_T=T^\sharp\)，仍有正阶 Hölder 初值稳定性，却不能满足旧 all-pairs 接口。**新增覆盖与解选择失稳是不同的分类问题。**

因此应当收窄的是本章的整体覆盖宣称，不是由此否定原 RLEB 收敛判据或其他已建立成果的新颖性。

## 6. 下一阶段应研究的最大自然证书预算层 \(\mathcal C_P\)

这里“最大”只指**相对于指定共同接口和证书预算**收下全部合格算子，不指所有可能 RLEB 算子的绝对最大空间。

### 6.1 不先规定法向律，直接用证书定义成员

固定 \(E,S,\lambda,R\)。令参数在紧盒 \(P\) 中取值：

\[
\gamma\in[\gamma_0,1],\quad
\theta\in[\theta_0,\theta_1],\quad
0\le L\le L_1,\quad0<K_0\le K\le K_1,
\]

其中 \(0<\gamma_0\le1\)、\(0<\theta_0\le\theta_1\)，gauge 为 \(\psi(t)=Kt^\theta\)；固定 \(0<\bar\kappa,\bar\eta<1\)。保留全部实指数，不能把临界无理指数 \(\gamma\theta=1\) 用有理指数网格删掉。

定义 \(\mathcal C_P\) 为所有连续 \(T:E\to E\)，满足 \(T|_S=I\)，且**存在**一组 \(P\) 内参数，使

\[
\|R_Tx-R_Ty\|\le L\|x-y\|^\gamma
\quad(\|x-y\|\le R),
\tag{6.1}
\]

\[
d(Tx,S)\le K(\|x-Tx\|/\lambda)^\theta
\quad\forall x\in E,
\tag{6.2}
\]

并有下列至少一个分支对 \(0<r\le R\) 成立：

\[
\mathrm D:\quad
K\left(\frac{r+Lr^\gamma}{2\lambda}\right)^\theta
\le\bar\kappa r;
\tag{6.3}
\]

\[
\mathrm E:\quad
\frac{r^2+L^2r^{2\gamma}}2
\le\bar\eta\left(r^2+
\lambda^2K^{-2/\theta}r^{2/\theta}\right).
\tag{6.4}
\]

(6.2) 对所有输入成立，故保留全部逆纤维的真实最小残差 EB。全空间完整接口避免了域外逆像漏检；欲转为纯局部版本，须另建双 collar／全纤维接口，不能直接删掉全空间量词。

共同指数下界、模上界与锚点先给紧的映射包络；联合证书条件闭、参数盒紧，向 **\(T\) 坐标投影**仍紧。因此 \(\mathcal C_P\) 是紧致 Polish/Baire 空间。这里每个算子只算一次，不会把它的多个证书算成多个对象。

预算适当时，\(\mathcal C_P\) 同时容纳普通线性 LT/energy 成员与非线性 direct 成员。收敛保证来自证书本身，而非预先输入一条法向超吸引律。这比 \(\mathcal Y\) 更直接对应用户所问的理论覆盖量。

### 6.2 决定性待证定理

下一轮的强目标应写成：

> 对一组明确、非退化、同时包含线性与非线性机制的预算 \(P\)，在 \(\mathcal C_P\) 中刻画 LT 可认证类与 RLEB 新增覆盖类的相对内部、稠密性和纲；优先检验 LT 类是否第一纲，并考察结论在合理放宽预算后是否保持。

不能对任意预算盒都预设同一答案；也不能预先规定研究必须得出 LT 很小。任意步长、固定步长、固定邻域、可缩小 germ 应分别编码。

真正的难点是**保留证书的局部自由度／开放坐标引理**。一般证书层并不凸：

\[
T_\pm(p,r)=(p\pm\sqrt{|r|},|r|/4),\qquad\psi(t)=t^2/4
\]

各自满足同一严格证书，其平均 \(T_0=(p,|r|/4)\) 却会要求

\[
r/4\le\tfrac14(3r/4)^2
\]

对小正 \(r\) 成立，显然不可能。因此现有凸混合证明不能直接用于 \(\mathcal C_P\)。若能关闭这个桥梁，新增内容就不再主要是标准 Hölder 粗糙性的方便层实现。

### 6.3 成功或失败分别意味着什么

| 经严格证明的结果 | 可以得出的研究含义 |
|---|---|
| 在多组非退化、合理放宽的 \(\mathcal C_P\) 内，LT 第一纲而新增覆盖余稀 | RLEB 的大幅新增覆盖得到**内生证书空间**层面的支持，比当前额外法向层明显更强；仍需优先权与应用意义论证 |
| LT 与新增覆盖都非第一纲，或分别有相对开块 | 两种机制形成真正的结构分区；不支持“一边几乎覆盖全部”的口号，但可能比单一大小排序更有理论内容 |
| 找到自然预算层，其中 LT 占优而新增覆盖第一纲 | 说明优势具有机制／预算依赖；当前 \(\mathcal Y\) 的余稀增量不能代表该层。原来的严格反例与层内定理仍有效 |
| 仅仅无法找到保结构变动或证明密度 | 只是技术问题未解，**不是**已证明 LT 不小或 RLEB 没价值 |

合并无限多个预算层也要重新证明 Baire 性；“每层 Baire”不等于其并为 Baire。任意 gauge、局部图块、无限维状态空间和非凸 \(S\) 均属后续问题，不在当前成果中悄悄计入。

## 7. 原创性、价值与论文定位

**真增量候选**是：在固定非点零集、完整 resolvent、真实 EB、共同严格预算的受约束层中，建立可审计的覆盖分离；任意正步长的统一必要条件 (3.1) 排除了“只是选错 proximal 参数”的解释；有限纤维函数空间实现则排除了“全靠无限值退化”的解释。

**经典工具**包括：Minty/resolvent 图坐标、Arzelà–Ascoli、Baire 定理、闭 Lipschitz 常数层、凸混合，以及 Hölder 空间中更高正则类的小性。它们不能单独列为新贡献。但工具经典并不推出受约束组合已知；要判已知，仍须有对应全部关键假设与结论的原定理或直接推论。

**价值判断：**当前结果是可信、有用的“新增覆盖并非偶然”的证据，适合增强 RLEB 原论文。其全局代表性尚有限，且第一纲证明在凸层建立后较短。因此现在更稳妥的定位是：原 RLEB 主文的一章，或经补足文献与自然性说明后的专业理论短文候选。仅靠当前层内结论，尚不足以支撑高水平综合优化／泛函分析期刊的独立强论文主张，更不能许诺分区或录用。

若下一阶段完成 \(\mathcal C_P\) 的机制分类、预算稳健性，或与独立实际算法／问题族之间的开放、范畴保持联系，独立论文的分量会明显增加。

**“差别大，所以一定是好理论和新理论”需要拆为四问：**是否严格新增覆盖；新增覆盖是否保留有用算法保证；条件是否自然且可核验；精确结论是否已经被既有定理覆盖。目前第一问在 \(\mathcal Y\) 内已有强答案，第二问沿用真实 RLEB 保证，第三问需要 \(\mathcal C_P\) 与应用桥，第四问还有原文缺口。因此现在可说“有实质扩展证据和新结果候选”，不能把两项尚未完成的审查用一个纲标签代替。

## 8. 必须禁止的夸大与仍未解决项

1. 不把 \(\mathcal Y\) 叫全体 RLEB，不把 \(\mathcal C_P\) 叫任意 gauge／任意接口的绝对最大类。
2. 不把 LT 几何、LT2025 收敛证书和全部 LTT pointwise／relative 理论合并成一个未经定义的集合。
3. 不把第一纲等同零测、低概率或某个百分比，也不把稠密误解成非第一纲。
4. 不把固定 \(s\) 的残集直接推广为全部解点同时成立，不把完整邻域结论推广到任意低维不变集。
5. 不将环境残集任意限制到全部二值、半代数或其他子类；有限纤维结论须用其自身空间证明。
6. 不把本轮单步认证覆盖差异解释成“RLEB 的极限选择普遍不稳定”。
7. 不因原始文献部分相关就整体判已知，也不因尚未检出完全相同表述就判首创。
8. 不用新章的价值判断重新否定原 RLEB 中本轮没有审查的结果。

仍未完成的核心数学任务是 \(\mathcal C_P\) 内的相对纲分类和预算稳健性；核心文献任务是补齐上述早期原文，并围绕精确组合继续核查，而不是继续泛搜“收敛”关键词。

---

## 给作者的行动建议（一页内）

**现在应该写进论文，但写成已经证明的相对覆盖结果，不写成完整理论优越性的终局判断。**

建议在原 RLEB 论文的主文增设“固定非点零集下的算子空间与认证覆盖”一节：先用一张表分清 LT 几何、LT2025 收敛和 LTT pointwise 三口径；再陈述 \(\mathcal Y\) 定理、共同真实 EB 和任意步长排除。证明骨架不长，值得放主文，不必把真正结果只放展望。完整二值函数球、strong/little Hölder 拓扑差异、参数编码与修补细节放附录。若放入 solution-selection 稿，必须说明这里比较的是证书覆盖，不是宣称非 Hölder 极限选择泛型，避免另起一条主线冲淡原稿。

主文可用的核心句是：

> 在一个固定非点仿射零集、完整 proximal 接口和共同严格 RLEB 预算的无限维法向超吸引层中，能在指定解点附近由 Luke–Tam 2025 局部 all-pairs 条件认证的原算子，即使允许任意正步长，也只构成第一纲子集。

不建议现在就另写一篇以“全 RLEB 与旧理论的泛型分类”为标题的独立稿。下一轮集中做三件事：

1. 把 \(\mathcal C_P\) 定义、紧性、完整纤维、共同域和 direct/energy 两通道接口整理成可引用命题，选出同时容纳双方普通机制的非退化预算。
2. 在该空间证明或反驳 LT 第一纲；寻找保留真实 EB 的开放坐标／局部自由度引理，若失败则给确切结构障碍，而不是继续堆尖点例子。
3. 独立审计最终范畴结论，并补齐 Strobin 2012、Reich–Zaslavski 1999 等原文的定理级对应。

**最后一句：你的空间化比较方向已经产生了真实成果；现在还差的不是再找一个反例，而是把相对层的强分离推进到由 RLEB 自身证书定义的自然大层。那一步才会直接回答“RLEB 这套理论本身到底多覆盖了多少”。**
