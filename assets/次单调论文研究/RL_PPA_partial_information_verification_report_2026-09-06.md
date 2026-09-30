# RL–PPA 的部分信息验证演算

**定理级定向研究、数学审计与可执行接入报告**  
版本：2026-09-06  
范围：有限维欧氏空间；固定 λ>0；单值与多值算子；允许非孤立零集。

---

## 0. 执行结论

现有数学已经拥有大量“部分算子信息 → 广义单调性”与“部分算子信息 → 次正则性/误差界”的成熟工具。真正有效的做法不是把它们各列一遍，而是把每项输出保存为同一局部图片上的**可组合证书**，再直接送入 PPA 的一步几何。

本报告完成了以下接入：

1. Jacobian、Clarke generalized Jacobian、graphical derivative、coderivative、prox-regularity、variational convexity、semimonotonicity calculus、sector/SRG/IQC，可输出 γ=1 的 RL 常数、Minty 输入覆盖或更强的原生二次能量。
2. Hölder metric regularity、高阶 inverse/open-mapping 与适当局部闭/紧条件下的半代数 Łojasiewicz 工具，可在唯一性、连续性及输入覆盖另行验证后给出 \(\gamma<1\) 的局部反射预解算子 Hölder 证书。普通 strict/paratingent graphical derivative 主要给一阶两点模量与其失效诊断。
3. 对选定 \(q>0\)，输出幂变换把原算子的 \(q\)-误差界等价改写成变换后算子的普通次正则性。若 slope、径向 coderivative、活动集、Hoffman–Robinson、半代数误差界或增长判据在该变换后对象上验证成功，就得到
   \[
   d(x,S)\le K\,d(0,F(x))^q
   \]
   的指定幂；只有定量 slope/coderivative/Hoffman 条件才自动给可比较的显式 \(K\)，而仅定性 FOSCMS/SOSCMS 通常只保证某个有限常数存在。普通性质本来就允许非孤立零集。
4. 把所有证书纳入一个保留原生信息的可行集编译器。它既能输出一个收缩因子，也能说明失败来自哪里；它不会先把矩阵、分块、切向—法向信息压成单个 \(L\)。
5. 建立跨分支 order quotient、weighted Hölder-chain 拼接、法向 inverse＋切向 Hölder shear、各向异性产品四类可手算接口。
6. 给出多值、闭图、非孤立零集、全域单值 resolvent 的 genuine \(\gamma<1\) 族；其最佳指数、渐近 RL 常数、高阶误差界常数和 PPA 真正收缩率全部可算，并达到修正临界常数。

同时必须修正原材料中的两项核心结论：

- \(\sqrt2\) 阈值只是“energy＋error bound”两标量约束的精确阈值。完整 RL 还给步长上界，非线性临界常数改为 \(2\)。
- \(q\ge1/\gamma\) 是该聚合证书保证固定 Q-linear 的阶数要求，不是实际 PPA 收缩的必要条件；分块或法向信息可以在统一高阶误差界不存在时仍证明收缩。

最强且可辩护的研究贡献，不是发明 Hölder 映射、semimonotonicity 或 higher-order subregularity，而是：

> **把现有微分、图形、组成、活动集、误差界和 inverse 工具统一编译为同一 Minty 图片上的定量 RL–PPA 证书；保留跨分支及切向—法向信息；给出修正的临界常数、适用边界和达到该边界的多值非孤立算子族。**

目前没有证据表明这一理论解决了一个文献中明确命名的开放问题。本报告在所分析的剪切/多分支结构族上，实现了从原生图与微分信息到可比较常数的完整链条；这是针对可验证性的具体推进，但尚未把相关文献所指出的一般困难转成普适可计算程序。

---

## 1. 对象、量词与必须先修正的几何

设 \(F:\mathbb R^n\rightrightarrows\mathbb R^n\)，固定 \(\lambda>0\)。对同一受控图块 \(\Gamma\subset\operatorname{gph}F\) 内的图点差

\[
a=u-v,\qquad b=u^*-v^*,
\]

定义

\[
M_+(u,u^*)=u+\lambda u^*,\qquad
M_-(u,u^*)=u-\lambda u^*.
\]

RL\(_\Gamma(\gamma,L)\) 是 all-pairs 条件

\[
\|a-\lambda b\|\le L\|a+\lambda b\|^\gamma,
\qquad 0<\gamma\le1.
\tag{1.1}
\]

### 定理 1（耦合 Minty 图表等价）

RL\(_\Gamma(\gamma,L)\) 当且仅当 \(M_+|_\Gamma\) 单射，且

\[
Q_\Gamma=M_-\circ(M_+|_\Gamma)^{-1}
\tag{1.2}
\]

在 \(M_+(\Gamma)\) 上为 \((\gamma,L)\)-Hölder。此时

\[
J_\Gamma(x)=\frac{x+Q_\Gamma(x)}2.
\]

这一定理有三个不可省略的量词边界：

- RL 只给图块内单射，不给 \(M_+(\Gamma)\) 包含输入邻域；resolvent existence 仍需 maximality、metric regularity、open mapping 或显式覆盖。
- 多值算子不能把 \(Q_\Gamma\) 写成普通关系复合 \((I-\lambda F)\circ(I+\lambda F)^{-1}\)，因为后者可能在同一 \(u\) 重选另一输出分支。
- branchwise RL 不给 cross-branch RL；必须验证不同活动分支之间没有 Minty collision，且输出在界面一致。

全文所谓“完整 localized inverse”均指：存在输出邻域 (U) 与输入邻域 (V)，使

\[
\operatorname{gph}(I+\lambda F)\cap(U\times V)
=\{(J_\Gamma(x),x):x\in V\},
\qquad J_\Gamma(V)\subset U,
\]

其中

\[
\Gamma=\{(u,u^*)\in\operatorname{gph}F:
u\in U,\ u+\lambda u^*\in V\}.
\]

这不是从多值 inverse 中任意挑出的一个 selection；若原图在局部化之外还有远处分支，另须排除它们对所需输入域的回返。

若输入域直径不超过 \(\delta\)，则

\[
\operatorname{Hol}_\gamma(J_\Gamma)\le K
\Longrightarrow
L\le2K+\delta^{1-\gamma},
\tag{1.3}
\]

反向有 \(K\le(L+\delta^{1-\gamma})/2\)。当 \(0<\gamma<1\) 时，最佳渐近两点模量满足

\[
\operatorname{hol}_\gamma(Q_\Gamma;\bar x)
=2\operatorname{hol}_\gamma(J_\Gamma;\bar x).
\tag{1.4}
\]

### genuine 的正确判据

“某个 \(\gamma<1\) 上界成立”不够，因为任何局部 Lipschitz 映射在缩小的有界域上都满足较低指数的 Hölder 界。本报告采用两个层次：

- **genuine 非线性**：\(Q_\Gamma\) 不局部 Lipschitz；
- **严格幂阶 genuine**：最佳可达到的局部 Hölder 指数严格小于 1。

后者强于前者；存在不 Lipschitz、却对每个 \(\gamma<1\) 都 Hölder 而指数 1 不达到的映射。

---

## 2. 完整一步几何与修正兼容阈值

令 \(S=F^{-1}(0)\cap D\) 非空闭，\(x^+\in J_{\lambda F}(x)\)，取 \(p\in P_S(x)\)。记

\[
d=d(x,S),\quad d_+=d(x^+,S),\quad s=\|x-x^+\|.
\]

解比较 RL 精确写成

\[
\|(x-p)-2(x-x^+)\|\le Ld^\gamma.
\]

置

\[
A(d)=\frac{d^2+L^2d^{2\gamma}}2,\qquad
B(d)=\frac{d+Ld^\gamma}{2}.
\]

因此同时有

\[
d_+^2+s^2\le A(d),\qquad
s\le B(d),\qquad d_+\le B(d),\qquad |d-d_+|\le s.
\tag{2.1}
\]

若 \(\psi:[0,\infty)\to[0,\infty)\) 非降、\(\psi(0)=0\)、\(\psi(t)\to0\)（\(t\downarrow0\)），且 generalized subregularity 给

\[
d(y,S)\le\psi(d(0,F(y))),
\]

则 PPA 包含关系给 \(d_+\le\psi(s/\lambda)\)。只保留前四个直接标量约束中的 energy、两个 \(B\) 上界和 error bound，定义

\[
\widehat R(d)=
\sup_{0\le t\le B(d)/\lambda}
\min\{B(d),\psi(t),\sqrt{A(d)-\lambda^2t^2}\}.
\tag{2.2}
\]

### 定理 2（修正的非线性标量兼容公式）

若 \(0<\gamma<1,L>0\)，令

\[
C_\gamma=\limsup_{t\downarrow0}\frac{\psi(t)}{t^{1/\gamma}}.
\]

则在扩展实数意义下

\[
\boxed{
\limsup_{d\downarrow0}\frac{\widehat R(d)}d
=C_\gamma\left(\frac{L}{2\lambda}\right)^{1/\gamma}.}
\tag{2.3}
\]

证明要点是上界 \(\widehat R(d)\le\psi(B(d)/\lambda)\)，而在 \(t=B(d)/\lambda\) 处，另外两项除以 \(d\) 均趋于 \(+\infty\)，从而得到反向 limsup。它比只保留 energy＋EB 所得到的

\[
C_\gamma(L/(\sqrt2\lambda))^{1/\gamma}
\]

严格更强。

“精确”只指式 (2.2) 所编码的标量可行集；它不等于所有具有这些参数的真实算子都达到该值，也不等于某个具体算子的实际最佳收缩率。

若

\[
d(y,S)\le K\,d(0,F(y))^q
\quad\Longleftrightarrow\quad
d(0,F(y))\ge m\,d(y,S)^a,
\]

其中 \(a=1/q\)、\(K=m^{-q}\)，则：

| 阶数关系 | 该聚合证书给出的结论 |
|---|---|
| \(q>1/\gamma\)（\(a<\gamma\)） | \(d_+=O(d^{\gamma q})\)，故距离超线性 |
| \(q=1/\gamma\)（\(a=\gamma\)） | 临界条件 \(K(L/(2\lambda))^{1/\gamma}<1\)，等价于 \(\lambda m>L/2\) |
| \(q<1/\gamma\)（\(a>\gamma\)） | 该标量证书不能推出固定 Q-linear；不表示算法失败 |

### 线性切片的正确层级

当 \(\gamma=1\)、\(\psi(t)=\rho t\) 时，四标量约束给

\[
\boxed{
\widehat\kappa=
\min\left\{
\sqrt{\frac{1+L^2}{2}}\frac{\rho}{\sqrt{\rho^2+\lambda^2}},
\frac{\rho(1+L)}{2\lambda},
\frac{1+L}{2}
\right\}.}
\tag{2.4}
\]

第一项是原 energy＋EB 子系统的精确因子；其收缩条件

\[
L^2<1+2\lambda^2/\rho^2
\]

代入 Luke–Tam 归一化 \(L^2=1+4\tau\) 后为 \(2\tau\rho^2<\lambda^2\)。但它不是完整 RL 假设下无条件的算子最优因子。

---

## 3. 现有部分信息工具：已经能输出什么

下表是定理级定向核验，不宣称覆盖所有数据库。

| 原生部分信息 | 已有工具 | 可导入 RL–PPA 的输出 | 主要限制 |
|---|---|---|---|
| 光滑 Jacobian / Hessian | 对称谱、路径积分、Cayley 变换 | 单调/强单调/hypomonotone；\(\gamma=1,L\)；有时直接 \(L<1\) | 单点矩阵不控制邻域；一阶非退化工具不足以处理临界退化，须使用高阶增长/remainder |
| 局部 Lipschitz、Clarke Jacobian | Clarke 均值定理与 inverse theorem | all-pairs 单调性；凸矩阵外包给 \(L\)、逆常数和覆盖半径 | 必须检查完整凸包，不能只查活动矩阵顶点 |
| 多值图的 coderivative | maximal/local monotonicity criteria；Mordukhovich metric regularity | 局部/极大单调性、输入覆盖、Aubin inverse | positivity、hypomonotonicity、maximality/coverage 的假设不可互换 |
| graphical / strict graphical derivative | 强局部极大单调性；paratingent 两点模量 | \(\gamma=1\) 的渐近最佳 RL 模量与 Minty 横截性 | ordinary contingent 单点信息通常不够 all-pairs |
| prox-regularity、variational convexity | attentive localization、subdifferential continuity、组合演算 | attentive 或普通局部 \(\gamma=1\) RL、proximal 分支存在 | 函数值截断不能悄悄删除 |
| \((\mu,\nu)\)-semimonotonicity | inversion/shift/scale/sum/parallel-sum calculus | 锐通用 \(L\)；更强的加权一步能量 | 极大性与 resolvent 全域存在另查 |
| angle/sector/SRG/pair-SRG/IQC | 几何区域、S-procedure/SDP | \(\gamma=1\) 的 \(L\)，并保留多条二次信息 | 无尺度 SRG 丢掉 \(\gamma<1\) 所需绝对增量尺度 |
| Hölder metric regularity/open mapping | inverse pseudo-Hölder、高阶 inverse theorem | \(J\) 的两点 Hölder；经 (1.3) 得 RL | 多值 inverse 距离估计不自动给唯一分支 |
| 半代数闭图 | Łojasiewicz、semialgebraic error bounds | 固定目标的某个普通 Hölder EB | 不保证 \(q\ge1/\gamma\) 或临界常数 |
| 已知单值连续的半代数 Minty 逆 | 半代数连续映射的 Hölder 正则性 | 局部 all-pairs 某个 Hölder 指数 | 唯一性、连续性与输入覆盖须先证明 |
| 一般 definable 图 | 可定义 gauge/增长分析 | 适当条件下的一般 gauge | 幂型须另核 polynomially bounded 结构或具体增长；不能由 definable 一词直接断言 |
| scalar residual slope | Ekeland/strong slope/nonlocal slope | 普通、非孤立 \(d\le K r^q\)，任意 \(q>0\) | 旧定理中的 \(\varphi'(0)>0\) 版本不能直接用于 \(q>1\) |
| directional coderivative / 活动集 | FOSCMS、SOSCMS、MSCQ | ordinary metric subregularity；用于变换后残差可给高阶 EB | 通常只定性给某个 \(K\)；临界线仍需量化 |
| polyhedral / PLQ / linear constraints | Hoffman–Robinson | 线性 EB 与可计算常数 | 直接只给 \(q=1\)；需作用于去奇异化映射以得到原算子 \(q>1\) |
| 增长、凸复合、Łojasiewicz | growth-to-error-bound、subgradient slope | \(a,q,m,K\) 或一般 gauge | tame/definable 单独不保证幂型或最佳常数 |
| Hölder graphical derivative | higher-order strong subregularity | 孤立点的精确高阶模量 | strong 结论不能直接换成到非孤立 \(S\) 的集合距离 |

结论不是“工具分散所以无用”，而是：多数现成定理已经可以直接成为证书生产器；缺少的是一个保持量词、分支、常数与局部范围的联合接口。

---

## 4. 证书编译器：把现有方法全部接到同一个 PPA 步

这一节是本报告的核心接线层。

对一个合法 PPA 步和投影点 \(p\in P_S(x)\)，置

\[
a=x^+-p,\quad b=(x-x^+)/\lambda,
\]

以及标量

\[
v=\|a\|,\quad w=\|x-x^+\|,\quad
z=\lambda\langle a,b\rangle,\quad e=d(x^+,S).
\]

真实一步必满足

\[
d^2=v^2+w^2+2z,\quad |z|\le vw,\quad
0\le e\le v,\quad |d-e|\le w,\quad e\le\psi(w/\lambda).
\tag{4.1}
\]

RL 再加入

\[
2(v^2+w^2)-d^2\le L^2d^{2\gamma}.
\tag{4.2}
\]

现有理论产生的每条原生信息按原强度加入。先要核验该信息适用于当前所取的同一个 \(p\in P_S(x)\)：AS 证书足够；只有 FS 证书时，不得把固定锚点换成移动投影点，而应另建固定锚点状态与相匹配的误差界。

- semimonotonicity：
  \[
  z\ge\lambda\mu v^2+(\nu/\lambda)w^2;
  \]
- weak-Minty 若其量词覆盖每一步所取的投影点 \(p\in P_S(x)\)（AS 足够）：
  \[
  z\ge(\beta/\lambda)w^2;
  \]
- sector、blockwise、matrix partial monotonicity：保留相应方向/分量变量和二次约束；
- normal growth、active-set relation、Hoffman 比较：保留产生的分量残差约束，而不是只换成最坏统一 \(\psi\)。

令 \(\mathcal C(d)\) 是所有已核实约束构成的有限维可行集，定义

\[
R_{\mathcal C}(d)=\sup\{e:(v,w,z,e,\ldots)\in\mathcal C(d)\}.
\tag{4.3}
\]

### 定理 3（单调证书编译原则）

每个真实受控 PPA 步都满足

\[
d(x^+,S)\le R_{\mathcal C}(d(x,S)).
\]

因此

\[
\limsup_{d\downarrow0}R_{\mathcal C}(d)/d<1
\]

即可推出局部距离收缩。加入任何新的已验证约束只会缩小 \(R_{\mathcal C}\)，不会使证书变差。

这个原则的价值是**避免信息损失**。若先把所有现成方法压成单一 RL 常数 \(L\) 与单一 gauge \(\psi\)，可能失去：

- semimonotonicity 中 \(\|a\|^2\) 与 \(\|b\|^2\) 的不同权重；
- partial monotonicity 的正常/切向差异；
- product operator 的各块指数；
- active branch 的残差下界；
- solution-anchored 不等式虽非 all-pairs RL、却直接足以控制 PPA 步的部分。

必须保留的限制是：\(R_{\mathcal C}\) 是“已编码信息的最强标量后果”，不是完整算子图实现定理；它也不能替代 local resolvent existence。

---

## 5. 广义单调性工具的显式 RL 接口

### 5.1 Semimonotonicity 的锐 Cayley 转换

若同一图片所有差满足

\[
\langle a,b\rangle\ge\mu\|a\|^2+\nu\|b\|^2,
\tag{5.1}
\]

并且

\[
1-4\mu\nu\ge0,\qquad
D_\lambda=1+\lambda\mu+\nu/\lambda>0,
\]

则仅凭 (5.1) 可以保证的最小通用 RL 常数为

\[
\boxed{
L_{\mu,\nu}(\lambda)=
\frac{|\lambda\mu-\nu/\lambda|+\sqrt{1-4\mu\nu}}
{1+\lambda\mu+\nu/\lambda}.}
\tag{5.2}
\]

证明来自完成平方：若 \(z=a+\lambda b,w=a-\lambda b\)，则

\[
\left\|w+\frac{\lambda\mu-\nu/\lambda}{D_\lambda}z\right\|
\le\frac{\sqrt{1-4\mu\nu}}{D_\lambda}\|z\|.
\]

特别地：

- \(h\)-hypomonotonicity（\(\mu=-h,\nu=0\)）及 \(\lambda h<1\) 给
  \[
  L=(1+\lambda h)/(1-\lambda h);
  \]
- \(c\)-cohypomonotonicity（\(\mu=0,\nu=-c\)）及 \(\lambda>c\) 给
  \[
  L=(\lambda+c)/(\lambda-c);
  \]
- \(\gamma=1\) RL 自身正是平衡切片
  \[
  \mu=\frac{1-L^2}{2\lambda(1+L^2)},\qquad \nu=\lambda^2\mu.
  \]

Evens–Pas–Latafat–Patrinos 的 semimonotonicity calculus 已有 inversion、shift、scale、sum、parallel sum 和 maximality/resolvent 结果；这些参数应先按其原规则组合，再进入 (5.2)。

### 5.2 不压缩原生二次信息

若 (5.1) 至少对每一步所取的同一个 \(p\in P_S(x)\) 成立（AS 足够；单独 FS 不足），并且

\[
A_0=1+2\lambda\mu\ge0,\qquad
B_0=1+2\nu/\lambda\ge0,
\]

则

\[
A_0d_+^2+B_0s^2\le d^2.
\tag{5.3}
\]

配合线性误差界 \(d_+\le\rho s/\lambda\)、\(\rho>0\)，只要分母正，直接得到

\[
\boxed{
\kappa_{\mu,\nu}
=\frac{\rho}{\sqrt{(1+2\lambda\mu)\rho^2+\lambda^2+2\lambda\nu}}.}
\tag{5.4}
\]

严格收缩还要求 \(2\lambda\mu\rho^2+\lambda^2+2\lambda\nu>0\)。保留原生信息可以严格改善只经过 \(L\) 的证书，但 (5.4) 与其他分别简化后的公式不具有逐参数的无条件支配关系；最强做法是把全部合法约束同时留在编译器中。两个非负符号条件在非孤立解集上不能删除；已有显式二维反例会使删除后的公式给出虚假收缩。

若 AS weak-Minty 覆盖每一步所取的最近解比较点，且

\[
\langle a,b\rangle\ge-\eta\|b\|^2,
\]

则直接保留

\[
d_+^2+(1-2\eta/\lambda)s^2\le d^2,
\]

在线性 EB 下给

\[
\kappa=\frac{\rho}{\sqrt{\rho^2+\lambda^2-2\eta\lambda}},
\qquad \lambda>2\eta.
\tag{5.5}
\]

这说明 weak-Minty 虽不推出 all-pairs RL，仍可作为编译器里的原生 PPA 证书。

若源定理只有一个固定零点的 FS weak-Minty，则不能代入这里随 \(x\) 变化的 \(p\)。应另建
\(\|x-\bar p\|,\|x^+-\bar p\|\) 的固定锚点 Lyapunov 状态，并使用与该状态匹配的误差界；一般不等于集合距离因子 (5.5)。

### 5.3 Clarke/Jacobian 外包同时输出 \(L\)、逆与覆盖半径

设单值 \(f\) 在开凸集 \(U\) 局部 Lipschitz，且

\[
\partial_Cf(u)\subset\mathcal A\quad(u\in U),
\]

其中 \(\mathcal A\) 凸紧。若

\[
c_\lambda=\inf_{A\in\mathcal A}\sigma_{\min}(I+\lambda A)>0,
\]

则 \(G=I+\lambda f\) 在 \(U\) 单射，\(G^{-1}\) 在 \(G(U)\) 上为 \(c_\lambda^{-1}\)-Lipschitz。并且

\[
L_\lambda=\sup_{A\in\mathcal A}
\|(I-\lambda A)(I+\lambda A)^{-1}\|
\tag{5.6}
\]

给出 all-pairs \(\gamma=1\) RL。若 \(\overline B_r(\bar u)\subset U\)，则

\[
B_{c_\lambda r}(G(\bar u))\subset G(B_r(\bar u)).
\tag{5.7}
\]

只检查每个活动分支不够。例

\[
f(x)=\begin{cases}-2x,&x\le0,\\0,&x\ge0,
\end{cases}
\]

的两个分支分别有有限一阶 RL 常数，但 \(I+f=|x|\) 发生 Minty collision；Clarke 凸包含临界斜率 \(-1\)，正确地拒绝该证书。

### 5.4 Coderivative、graphical derivative 与 attentive 图

现有结果可以如下接线：

- 在非空局部闭图等相应来源假设下，局部 hypomonotonicity 加图邻域内所有相关 limiting/regular coderivative 元素的半正性，可推出局部极大单调；统一强正性给强局部极大单调，因此输出 \(L=1\) 及局部 resolvent 结构。
- strict graphical derivative 的统一正性可以替代部分 coderivative 检查，但 maximal hypomonotonicity、strong regularity 或覆盖条件不能省略。
- prox-regularity 和 variational convexity 通常先输出 \(f\)-attentive 图上的局部单调/hypomonotone 关系。subdifferential continuity 可用于去掉函数值截断，得到普通局部图片；若只证明 PPA 保持 attentive 区域，则应保留 attentive 图来分析该算法，不能由轨道不变性升级为整个普通图的 all-pairs 性质。
- 2026 的 variational-convexity composition calculus 已处理复合和求和的乘子/CQ 条件；RL 不应重复发明这些组合定理，而应提取其参数和图片范围。

### 5.5 Angle、SRG 与 IQC

若

\[
\langle a,b\rangle\ge\cos\theta\|a\|\|b\|,
\qquad 0\le\theta<\pi,
\]

则对任意 \(\lambda>0\)

\[
\boxed{L=\max\{1,\tan(\theta/2)\}.}
\tag{5.8}
\]

这是仅凭 angle bound 且允许维数至少为 2 时的锐通用常数，不宣称等于每个具体算子的最优常数。多个分量/sector/IQC 若给 \(\zeta=(a,b)\) 的二次约束 \(\zeta^TM_i\zeta\ge0\)，可以用标准 S-procedure/SDP 寻找最小 \(\ell=L^2\)；但 SDP 不可行只表示该证书失败。

标准 SRG 和 pair-SRG 是齐次、无尺度表示。对 \(\gamma<1\)，同尺度缩放图 \((u,u^*)\mapsto(cu,cu^*)\) 保持 SRG，却把最小 \(L\) 乘以 \(c^{1-\gamma}\)。所以 genuine RL 必须补充绝对 Minty 增量尺度或非线性变换；现有无尺度 SRG 不能单独输出所需 \((\gamma,L)\)。

---

## 6. Inverse/open-mapping 工具的显式接口

### 6.1 一阶最佳 RL 模量来自 paratingent cone

令 \(T^P_\Gamma(\bar z)\) 为图片的 paratingent cone。以下模量是两图点共同趋向 \(\bar z\) 的比值上极限；参考图点孤立时约定为零，不包含任何输入覆盖结论。其一阶渐近最佳值为

\[
\boxed{
\ell_{RL}(\bar z)=
\sup\{\|a-\lambda b\|:(a,b)\in T^P_\Gamma(\bar z),
\ \|a+\lambda b\|\le1\}.}
\tag{6.1}
\]

有限一阶局部 RL 存在，当且仅当

\[
T^P_\Gamma(\bar z)\cap\{(a,b):a+\lambda b=0\}=\{0\}.
\tag{6.2}
\]

活动集、区间矩阵或 generalized derivative calculus 只要能给一个闭锥外包 \(T^P_\Gamma\subset K\)，就可用 \(K\) 在 (6.1) 中求安全的渐近上界。任意严格大于所得有限模量的 \(L\) 在某个足够小邻域成立；边界模量不一定在任何正半径邻域达到。这比只在一个参考点算普通 contingent derivative 更接近 all-pairs 量词。

设 \(F\) 在 \((\bar u,\bar u^*)\) 局部闭图，令 \(G=I+\lambda F\)、\(\bar x=\bar u+\lambda\bar u^*\)。下面 \(G\) 的两种图微分都取于 \((\bar u,\bar x)\)，\(F\) 的取于 \((\bar u,\bar u^*)\)。线性图变换给

\[
D_*G(h)=h+\lambda D_*F(h),\qquad
D^*G(v)=v+\lambda D^*F(v).
\tag{6.3}
\]

strict derivative 的零核用于两点分离，coderivative 的零核用于 metric regularity/输入覆盖；两者角色不同。

### 6.2 Hölder inverse 的现成路线

若现有定理在同一 localized graph、参考点附近的同一产品邻域上统一给

\[
d(u,G^{-1}(x))\le K\,d(x,G(u))^\gamma,
\]

并且局部 inverse 唯一，则缩小邻域后 \(J\) 为 \((\gamma,K)\)-Hölder，继而由 (1.3) 输出 RL。

可用来源包括：

- 闭半代数映射的“从定义域到像的相对开放性 + 像局部闭”与像内 Hölder metric regularity、inverse pseudo-Hölder 性等价；接到 PPA 时还须验证所需欧氏输入邻域被真实 Minty 像覆盖，并验证对应完整局部 inverse 唯一；
- Frankowska 的 high-order inverse theorem：统一的 \(h^k\) 局部像覆盖给 \(1/k\)-Hölder inverse；
- Hölder Lyusternik–Graves 的 slope/coderivative 条件；
- Robinson generalized equation、Clarke inverse theorem、SCD/semismooth* 路线在非退化时给 \(\gamma=1\)。

半代数紧图片还有一个直接定性结论：若 \(M_+|_\Gamma\) 单射，则对

\[
U(g,h)=\|\Delta M_-\|^2,\quad V(g,h)=\|\Delta M_+\|^2
\]

使用 Łojasiewicz，\(V=0\Rightarrow U=0\) 给某个 all-pairs Hölder RL。它自动覆盖有限多分支之间的配对，但不输出足以判别临界线的最佳指数与小常数。

### 6.3 一个可手算的高阶 inverse 证书

一维下取 \(r,c>0\)、\(p>1\)，令 \(F:(-r,r)\to\mathbb R\) 单值，且
\(g(u)=u+\lambda F(u)\) 在该区间绝对连续、\(g(0)=0\)。若几乎处处

\[
g'(u)\ge c|u|^{p-1},\qquad p>1,
\]

则

\[
|g(u)-g(v)|\ge\frac{c}{p2^{p-1}}|u-v|^p.
\]

因此在任一输入集 \(V\subset(-cr^p/p,cr^p/p)\) 上，inverse 指数 \(\gamma=1/p\)，常数

\[
K=\left(\frac{p2^{p-1}}c\right)^{1/p},
\quad
L=2K+(\operatorname{diam}V)^{1-1/p}.
\tag{6.4}
\]

像至少包含 \((-cr^p/p,cr^p/p)\)。这是真正的“退化导数阶数 → RL 指数、常数、覆盖半径”接口；若没有统一 remainder/增长，只知道任意有限中心 jet，不能排除附近振荡导致的 Minty collision。

---

## 7. 次正则性工具的精确移植

本节始终保留 PPA 所需的同一个目标零集。若原问题使用
\(S=F^{-1}(0)\cap D\)，这里的闭工作域是调用完备性工具时的显式假设或已经验证的局部化；不能把任意 \(D\) 直接换成 \(\overline D\) 并声称目标零集自动不变。验证后可把 \(F\) 限制到该工作域、域外取空值，并把限制简记为 \(F\)。使用 slope/coderivative 充分条件时，另外核验相应的完备性、闭图或残差下半连续性；局部图片截断必须保留所有相关小输出与目标解点。

令

\[
r_F(x)=d(0,F(x)),\qquad S=F^{-1}(0).
\]

### 定理 4（输出幂变换）

对任意 \(q>0\)，定义

\[
T_q(v)=\|v\|^{q-1}v\quad(v\ne0),\qquad T_q(0)=0,
\]

以及 \(H_q=T_q\circ F\)。则

\[
\boxed{
H_q^{-1}(0)=F^{-1}(0),\qquad
d(0,H_q(x))=d(0,F(x))^q.}
\tag{7.1}
\]

于是

\[
d(x,S)\le K r_F(x)^q
\iff
d(x,H_q^{-1}(0))\le K d(0,H_q(x)).
\tag{7.2}
\]

常数完全不变，多值性和非孤立零集完全保留。这意味着所有普通 metric-subregularity 工具都可以作用于 \(H_q\)，成为原 \(F\) 的指定高阶证书生产器。

但 \(q>1\) 时 \(DT_q(0)=0\)，不能据此机械套 coderivative chain rule。例

\[
F(x)=\operatorname{sgn}(x)\sqrt{|x|},\qquad T_2(F(x))=x
\]

说明原图的尖点会抵消外层退化；必须从参数图、非零输出导数极限或有资格条件的 calculus 计算 \(H_q\)。

### 7.1 Slope 证书及显式常数

令 \(h=r_F^q\) 为非负下半连续函数，工作空间完备，\(S=[h=0]\)、\(\bar x\in S\)。若存在 \(R,\eta,c>0\)，使

\[
|\nabla h|(x)\ge c
\quad\text{对所有 }x\in B_R(\bar x),\ 0<h(x)<\eta,
\]

则 Ekeland/strong-slope 误差界给

\[
\boxed{d(x,S)\le c^{-1}r_F(x)^q}
\quad\text{对 }x\in B_{R/2}(\bar x),\ 0<h(x)<\eta.
\tag{7.3}
\]

若要去掉小残差限制，可再把输入半径缩到不超过 \(\eta/c\)；高残差部分由 \(d(x,S)\le\|x-\bar x\|\le h(x)/c\) 自动满足。闭值保证 \([r_F=0]=F^{-1}(0)\)；否则须把该等式单列为假设。

在正残差处可直接检查

\[
|\nabla r_F|(x)\ge b\,r_F(x)^{1-q},
\]

从而 \(K=1/(qb)\)。这允许任意 \(q>0\)，且是普通集合距离结论。需特别注意：Kruger 较早 nonlinear-subregularity 框架中某些 \(\varphi'(0)>0\) 的定理不能直接代入 \(t^q,q>1\)；Cuong–Kruger 的一般 scalar error-bound 定理或先做 (7.1) 则没有此障碍。

若最小残差来自有限个活动分支

\[
r_F(x)^q=\min_i h_i(x),
\]

只需每个邻近非解点存在一个达到最小值的可行活动分支，并沿其分支域内可行曲线或方向以至多单位速度使 \(h_i\) 以至少 \(c\) 下降，即得到 (7.3)。这把分支导数真正转成 \(K\)，而不是只说“可用 slope”。

### 7.2 Coderivative、FOSCMS/SOSCMS、Hoffman

可执行路线是：

1. 构造或外包 \(H_q\) 的图；
2. 用 ordinary subregularity 的 coderivative/slope 条件，而不是误用 strong subregularity 的零核；
3. 对 \(H_q=P-\Lambda\) 使用 directional normal 的 FOSCMS；一阶退化时保留二阶方向项使用 SOSCMS；
4. 对线性/分片多面体辅助残差使用 Hoffman–Robinson 常数；
5. 若只构造了辅助 \(G\)，使用
   \[
   Z=G^{-1}(0)\subset S,\quad
   d(x,Z)\le K_G r_G(x),\quad r_G(x)\le C r_F(x)^q
   \]
   得
   \[
   d(x,S)\le K_GC r_F(x)^q.
   \tag{7.4}
   \]

Li–Mordukhovich 的 ordinary coderivative 下界还可直接用于 \(H_q\)：若在邻域小输出和相应径向对偶方向上，所有 regular coderivative 元素的范数统一不小于 \(c\)，则 \(H_q\) 的 subregularity 模量不超过 \(1/c\)，故原 \(F\) 可取任意 \(K>1/c\)。这比要求完整 metric regularity 弱，也不要求零点孤立。

更贴近原始多值图的形式无需显式写出 \(H_q\)。以下假设 \(F:\mathbb R^n\rightrightarrows\mathbb R^m\) 为闭图映射，\(q>0\)，\(\bar x\in S=F^{-1}(0)\)；局部闭图版本采用保持全部相关小输出和零集的闭图限制。对 \(v\ne0\) 定义归一化的扰动径向对偶邻域

\[
J_\varepsilon(v)=
\left\{
\frac{v/\|v\|+\varepsilon z}{\|v/\|v\|+\varepsilon z\|}:
\|z\|\le1
\right\},\qquad0<\varepsilon<1.
\]

若存在 \(\delta,c_0>0\)、\(\varepsilon_0\in(0,1)\)，使对所有

\[
x\in B_\delta(\bar x)\setminus S,\quad
v\in F(x),\quad0<\|v\|<\delta,\quad
v^*\in J_{\varepsilon_0}(v),
\]

以及所有

\[
u^*\in\widehat D^*F(x,v)(v^*)
\]

都满足

\[
\boxed{q\|v\|^{q-1}\|u^*\|\ge c_0,}
\tag{7.5a}
\]

则

\[
\operatorname{subreg}_qF(\bar x,0)\le1/c_0,
\]

实际邻域中可取任意 \(K>1/c_0\)；模量上界不表示临界 \(K=1/c_0\) 必在某个正半径邻域实现。证明只在 \(v\ne0\) 处使用 \(T_q\) 的局部 \(C^1\) 微分同胚和精确 regular-normal 变换，再调用 Li–Mordukhovich 的径向 ordinary-subregularity 判据；没有在零点偷用退化链式法则。临界 \(q=1/\gamma\) 时，若

\[
c_0>\left(\frac{L}{2\lambda}\right)^{1/\gamma},
\]

便可在 \(1/c_0\) 与允许阈值之间选择实际 \(K\)，闭合收缩证书。

在 (10.1) 的 \(\alpha=1/2,b=2,c=4,\lambda=1\) 基准上，每个光滑输出分支 \(f_\beta=(-2\sqrt y,\beta y)\) 满足

\[
2\|f_\beta\|
\left\|D f_\beta^T\frac{f_\beta}{\|f_\beta\|}\right\|
=4+2\beta^2y\longrightarrow4.
\]

因此，对每个 \(0<c_0<4\)，可以选择依赖于 \(c_0\) 的固定扰动半径 \(\varepsilon_0>0\) 和空间半径 \(\delta>0\)，使 (7.5a) 对全部小输出、全部扰动径向对偶方向和全部 regular coderivative 元素成立。由此输出任意 \(K>1/4\)；直接残差计算又证明最佳模量正是 \(1/4\)。这条链真正实现了

\[
\text{原生小输出图微分信息}
\Rightarrow
\text{既有 coderivative 判据}
\Rightarrow
\text{锐的高阶非孤立 EB}.
\]

### 7.3 增长条件的显式公式

令 \(f=\varphi\circ g\)，其中 \(\varphi\) proper lsc convex、\(g\in C^1\)。取 \(\bar x\in S\) 为驻点，假设 \(Dg(\bar x)\) 满射；取 \(\sigma,M>0\)，使在足够小凸邻域有

\[
\|Dg(x)^Tv\|\ge\sigma\|v\|\quad\text{对所有 }v,
\qquad
\|g(x)-g(z)\|\le M\|x-z\|.
\]

由此 \(\partial f(x)=Dg(x)^T\partial\varphi(g(x))\)，相关局部驻点均为最小点。令 \(S\) 为闭的局部最小点集、\(f_*=f(\bar x)\)，并缩小邻域使 \(P_S(x)\) 留在上述范围。若

\[
f(x)-f_*\ge c\,d(x,S)^p,\qquad c>0,\ p>1,
\]

则对 \(F=\partial f\)

\[
\boxed{
r_F(x)\ge\frac{c\sigma}{M}d(x,S)^{p-1}.}
\tag{7.5}
\]

因此 \(a=p-1\)、\(q=1/(p-1)\)、\(m=c\sigma/M\)。临界 \(p=1+\gamma\) 时可直接与 \(\lambda m>L/2\) 比较。

其常数证明是一行：凸支撑与链式法则给
\(f(x)-f_*\le(M/\sigma)r_{\partial f}(x)d(x,S)\)，再与增长式相除。

### 7.4 非孤立与高阶证书的真实边界

- ordinary \(q\)-subregularity 本来就以 \(d(x,F^{-1}(0))\) 为左侧，允许非孤立零集；Mordukhovich–Ouyang 已明确研究 \(q>1\)。
- strong \(q\)-subregularity 以 \(\|x-\bar x\|\) 为左侧，强制局部孤立；Hölder graphical derivative 的精确 strong 判据不能直接换成普通集合距离。
- 一个紧解块上若每点都有同一 \(q\) 的 ordinary 证书，有限覆盖即可统一常数和邻域。真正困难在指数沿解集退化、解块非紧，或原始信息只有单纤维 strong 结论。
- 若存在 \(x_k\to\bar x\in S\)、\(x_k\notin S\)，且 \(r_F(x_k)\le M d(x_k,S)\)，则在 \(\bar x\) 邻域不可能有任何 \(q>1\) 的 EB。单值 forward-Lipschitz、在 \(S\) 上为零且有非解点逼近边界的算子属于此情形；若整个邻域都是解则 EB 平凡成立。
- graph-distance residual \(d((x,0),\operatorname{gph}F)\) 是 1-Lipschitz 且不大于 \(d(x,S)\)，因此不能被误当成原始 residual 来证明 \(q>1\) EB。

---

## 8. 跨分支、切向—法向和产品证书

### 8.1 全对图表阶数商

设图表族覆盖全部待验证图片，且所有比较均在同一指定参数域内。若每个分支对 \((i,j)\) 有非负比较量 \(\Delta_{ij}\)，以及常数
\(m_{ij}>0,n_{ij}\ge0,p_{ij}>0,q_{ij}>0\)，满足

\[
\|\Delta M_+\|\ge m_{ij}\Delta_{ij}^{p_{ij}},
\qquad
\|\Delta M_-\|\le n_{ij}\Delta_{ij}^{q_{ij}},
\tag{8.1}
\]

则任取

\[
0<\gamma\le\inf_{i,j}\{1,q_{ij}/p_{ij}\}
\]

并且所有所比较的 Minty 输入差满足 \(\|\Delta M_+\|\le\delta\)，则可得

\[
L=\sup_{i,j}n_{ij}m_{ij}^{-q_{ij}/p_{ij}}
\delta^{q_{ij}/p_{ij}-\gamma}
\tag{8.2}
\]

的局部 RL 证书，前提是 (8.2) 的上确界有限。关键是 (8.1) 对**所有分支对**成立；只验证 \(i=j\) 没有解决 cross-branch 问题。

### 8.2 Weighted Hölder-chain 拼接

若各 Minty 像块 \(E_i\) 上有单值反射 \(Q_i\)，它们在界面上取值一致，并且每块满足

\[
\|Q_i(x)-Q_i(y)\|\le L_i\|x-y\|^\gamma,
\qquad x,y\in E_i,
\]

定义

\[
\mathfrak d_\gamma(x,y)=
\inf_{x=z_0\leadsto z_N=y}
\sum_{r=1}^N L_{i_r}\|z_r-z_{r-1}\|^\gamma,
\tag{8.3}
\]

其中每条边位于某一个 \(E_{i_r}\)。若 \(\mathfrak d_\gamma(x,y)\le C\|x-y\|^\theta\)，则得到全对 Hölder 控制。若存在 \(B,\beta>0\)，且每个所需点对都有一条至多 \(N\) 段、总长度不超过 \(B\|x-y\|^\beta\) 的链，则对 \(0<\gamma<1\)，令

\[
\theta=\beta\gamma,\qquad
C=B^\gamma
\sup_{x,y}
\left(\sum_{r\text{ in chosen chain}(x,y)}
L_{i_r}^{1/(1-\gamma)}\right)^{1-\gamma}<\infty.
\tag{8.4}
\]

这里必须取跨所有点对所选链的统一上界；不能让 \(C\) 随 \((x,y)\) 改变。若 \(\gamma=1\)，则取

\[
\theta=\beta,\qquad
C=B\sup_{x,y}\max_{r\text{ in chosen chain}(x,y)}L_{i_r}.
\tag{8.4a}
\]

RL 指数按定义不超过 1：若 \(\theta\le1\)，输出 \((\theta,C)\)；若 \(\theta>1\) 且总输入直径不超过 \(\delta\)，则降为 \((1,C\delta^{\theta-1})\)。

regular separation 可提供 \(\beta\)，但 \(\beta<1\) 会真实降低全局 RL 指数。

### 8.3 法向 inverse＋切向 Hölder shear

令

\[
F(t,z)=\{(-h(z),w):w\in A(z)\}.
\tag{8.5}
\]

固定 \(0<\alpha<1\)。若 \(K=(I+\lambda A)^{-1}\) 单值存在、为 \(k\)-Lipschitz，normal reflection \(2K-I\) 为 \(B\)-Lipschitz，且 \(h\) 为 \((\alpha,H)\)-Hölder，则

\[
J(p,q)=(p+\lambda h(Kq),Kq),
\]

以及在输入直径 \(\delta\) 上

\[
L_\delta=2\lambda Hk^\alpha+\max\{1,B\}\delta^{1-\alpha}.
\tag{8.6}
\]

若闭集 \(Z=\{z:h(z)=0,0\in A(z)\}\ne\varnothing\)，则 \(S=\mathbb R^{\dim t}\times Z\)（局部切向截断时使用相应产品集）。若上述 inverse/Hölder 数据和下式在相关域及附近投影点上一致成立，且

\[
\|h(z)\|\ge m\,d(z,Z)^a,
\]

则得到 \(d((t,z),S)\le m^{-1/a}r_F(t,z)^{1/a}\)。但这里有一个结构限制：若 \(h|_Z=0\) 且同一个 \(h\) 是 \(\alpha\)-Hölder，则又有 \(\|h(z)\|\le H d(z,Z)^\alpha\)，故非平凡邻域强制 \(a\ge\alpha\)。因此仅靠同一个 shear 分量时，真正相关的是临界 \(a=\alpha\)；要实现 \(a<\alpha\)，必须由 normal residual 或其它独立分量给更强下界。

在临界 \(a=\alpha\) 下，把 (8.6) 代入 \(\lambda m>L_\delta/2\) 得

\[
m>Hk^\alpha+
\frac{\max\{1,B\}}{2\lambda}\delta^{1-\alpha}.
\]

所以只要

\[
\boxed{m>Hk^\alpha,}
\tag{8.6a}
\]

就可选

\[
0<\delta<
\left[
\frac{2\lambda(m-Hk^\alpha)}{\max\{1,B\}}
\right]^{1/(1-\alpha)}
\tag{8.6b}
\]

并闭合该聚合收缩证书；失败只表示这组粗常数未认证。若法向零集 \(Z\) 自身非孤立，全空间 Lipschitz 常数 \(k\) 往往至少为 1，且同一 \(h\) 的下界常数满足 \(m\le H\)，使粗式 (8.6a) 可能必然失败。若能直接验证
\(\|h(Kq)-h(Kq')\|\le C\|q-q'\|^\alpha\)，则把 (8.6) 中的 \(Hk^\alpha\) 换成 \(C\)，临界条件变为 \(C<m\)；否则保留法向分块，不能由粗证书失败推出算法不收缩。

若还能从现有 normal-subregularity 工具得到

\[
d(0,A(z))\ge m_Nd(z,Z)^{a_N},
\]

则不要丢掉正交残差，直接保留

\[
r_F(t,z)\ge
g(d(z,Z)),\qquad
g(r)=\sqrt{m^2r^{2a}+m_N^2r^{2a_N}}.
\tag{8.6c}
\]

于是 \(\psi=g^{-1}\)。主导阶为 \(\min\{a,a_N\}\)；若 \(a=a_N\)，有效系数是 \(\sqrt{m^2+m_N^2}\)。只有这种独立 normal growth 才能在 \(a_N<\alpha\) 时给真正的自动阶数兼容。

一个不需要预先解出完整 resolvent 的原生数据推论如下。设 \(c>0\)，只知道 \(b(\bar t)\ne0\) 以及 \(b\) 在闭球 \(\overline B_R(\bar t)\) 的一个邻域内为 \(\ell\)-Lipschitz。当 \(y\ge0\) 时考虑

\[
F(t,y)=\left\{
\left(-y^\alpha b(t),\frac{c-1}{\lambda}y\right),
\left(-y^\alpha b(t),-\frac{c+1}{\lambda}y\right)
\right\}.
\tag{8.7a}
\]

并在 \(y<0\) 时令 \(F(t,y)=\varnothing\)。

令

\[
m=\|b(\bar t)\|-\ell R>0,\qquad
B=\|b(\bar t)\|+\ell R.
\]

若取 \(r>0\) 使

\[
\vartheta=\lambda\ell r^\alpha<1,\qquad
\lambda Br^\alpha\le R/2,
\]

则对
\(V=B_{R/2}(\bar t)\times(-cr,cr)\) 中的输入，法向量由 \(y=|q|/c\) 确定，而切向方程

\[
t=p+\lambda y^\alpha b(t)
\]

是闭球上的压缩映射。这里使用的是 \(t\in\overline B_R(\bar t)\)、\(0\le y\le r\)、Minty 输入属于 \(V\) 的完整受限图；因此该图上的 local resolvent 存在且唯一，而不声称排除图外远处分支。其 Hölder 常数由 \(m,B,\ell,R,r,c\) 显式控制，同时

\[
r_F(t,y)\ge m y^\alpha.
\]

具体令

\[
\delta=\sqrt{R^2+4c^2r^2},
\]

则可取

\[
L_{R,r}=
\frac{2\lambda Bc^{-\alpha}}{1-\vartheta}
+\max\left\{\frac{1+\vartheta}{1-\vartheta},1+\frac2c\right\}
\delta^{1-\alpha}.
\tag{8.7b}
\]

当 \(c>1\) 时，先把 \(R\) 缩到原生数据有效范围内，且使

\[
\ell R(1+c^{-\alpha})+
\frac{1+2/c}{2\lambda}R^{1-\alpha}
<\|b(\bar t)\|(1-c^{-\alpha}).
\]

这正是在 \(r=0\) 的极限常数上留下严格余量 \(\lambda m>L_{R,0}/2\)。再利用 \(L_{R,r}\to L_{R,0}\) 取充分小 \(r>0\)，同时满足压缩、自映射和严格兼容条件。轨道切向漂移有先验界

\[
\sum_k\|t_{k+1}-t_k\|
\le\frac{\lambda B\,d_0^\alpha}{c^\alpha-1},
\]

若再取

\[
\|p_0-\bar t\|\le R/4,\qquad d_0\le r,\qquad
\frac{\lambda B}{c^\alpha-1}d_0^\alpha\le R/4,
\]

则所有后续输入留在 \(\overline B_{R/2}(\bar t)\)，可逐步复用同一局部 inverse。该族输出
\(\gamma=\alpha\)、\(q=1/\alpha\)、\(K=m^{-1/\alpha}\)，并且实际距离因子为 \(\kappa_{\rm actual}=1/c\)。这给出真正的

\[
\{b(\bar t),\operatorname{Lip}b,c,\lambda,\alpha\}
\Rightarrow
(\gamma,L,q,K,\text{existence radius},\kappa)
\]

部分信息证书；不需要事先知道整个图或闭式 \(J\)。

### 8.4 各向异性产品

在 Euclidean 产品范数、产品工作域和 \(S=\prod_iS_i\) 下，对 \(F=\prod_iF_i\)，若各块已经得到

\[
d(x_i^+,S_i)\le\kappa_i d(x_i,S_i),\qquad \kappa_i<1,
\]

则产品 PPA 直接满足

\[
\boxed{d(x^+,S)\le(\max_i\kappa_i)d(x,S).}
\tag{8.7}
\]

无需先寻找共同的最差 \((\gamma,q)\)。例如第一块取 (10.1) 的 \(\alpha=1/2,b=2,c=4,\lambda=1\)，第二块取 \(F_2(z)=3z\)。两块分别具有最佳 RL 指数障碍 \(1/2\) 与最佳误差界指数障碍 \(1\)，所以任何统一幂对至多为 \((\gamma,q)=(1/2,1)\)，聚合条件 \(q\ge1/\gamma\) 失败；但两个 PPA 距离因子都精确为 \(1/4\)，故产品距离也精确乘 \(1/4\)。这证明逐块保留信息可以排除统一压缩造成的假失败；一般产品只保证上界 \(\max_i\kappa_i\)，不把它误称为每个实例的精确因子。

---

## 9. 局部全轨道定理

固定 \(\bar p\in S\)。假设存在输入球、受控图块及距离阈值，使：

1. 每个合法局部状态至少有一个属于受控图块的 PPA 步，且输出仍在合法域；
2. 所需最近解图点都在比较图块中；
3. error bound 或其它原生证书对每个输出有效；
4. 编译器已经证明 \(d_+\le\kappa d\)，其中 \(0<\kappa<1\)。
5. 受控步及所取投影点满足 solution-comparison RL\((\gamma,L)\)，从而有
   \(s\le\tfrac12(d+Ld^\gamma)\)；更一般地，也可直接假设一个沿 \(d_k\le\kappa^kd_0\) 可求和的统一步长上界并相应替换下面的 \(H\)。

则

\[
d_k\le\kappa^kd_0,\qquad
s_k\le\tfrac12(\kappa^kd_0+L\kappa^{\gamma k}d_0^\gamma).
\]

令

\[
H(t)=\frac12\left(\frac{t}{1-\kappa}+
\frac{Lt^\gamma}{1-\kappa^\gamma}\right).
\]

若 \(d_0\) 严格小于编译器收缩有效的距离阈值，且初值到局部域边界的余量严格大于 \(H(d_0)\)，则通过归纳可反复调用局部 resolvent；轨道有限长、Cauchy，并收敛到某个 \(x^\infty\in S\)。尾估计为

\[
\|x^k-x^\infty\|
\le\frac12\left(
\frac{\kappa^kd_0}{1-\kappa}
+\frac{L\kappa^{\gamma k}d_0^\gamma}{1-\kappa^\gamma}
\right).
\tag{9.1}
\]

因此距离的 Q 因子与到最终单点的主导 R 因子通常不同。非孤立零集上的切向运动正是这种差异出现的自然位置。

---

## 10. 两个决定理论边界的多值非孤立算子族

### 10.1 达到修正临界常数的二分支剪切族

固定 \(0<\alpha<1\)、\(b,c,\lambda>0\)、单位切向量 \(e\)，令 \(y\ge0\) 时

\[
F(t,y)=\left\{
\left(-by^\alpha e,\frac{c-1}{\lambda}y\right),
\left(-by^\alpha e,-\frac{c+1}{\lambda}y\right)
\right\},
\tag{10.1}
\]

\(y<0\) 时值为空。则图闭、\(y>0\) 时真二值，且

\[
S=\mathbb R^m\times\{0\}.
\]

两个 Minty 分支的第二输入分别为 \(cy\) 与 \(-cy\)，所以跨分支无碰撞、像为全空间，并且

\[
J(p,q)=\left(p+\lambda bc^{-\alpha}|q|^\alpha e,\frac{|q|}{c}\right).
\tag{10.2}
\]

反射映射为

\[
Q(p,q)=\left(p+2\lambda bc^{-\alpha}|q|^\alpha e,
\frac{2|q|}{c}-q\right).
\]

在每个解输入 \((p,0)\) 附近，其最佳局部幂指数恰为 \(\alpha\)（在 \(q\ne0\) 的普通点处则局部 Lipschitz），渐近最小 RL 常数为

\[
L_0=2\lambda bc^{-\alpha}.
\tag{10.3}
\]

在任一输入直径不超过 \(\delta\) 的实际邻域，可取

\[
L_\delta=L_0+(1+2/c)\delta^{1-\alpha}.
\tag{10.3a}
\]

残差满足

\[
r_F(t,y)=
\sqrt{b^2y^{2\alpha}+((c-1)/\lambda)^2y^2}
\ge by^\alpha,
\]

且 \(b\) 是临界阶的渐近最佳常数。因此

\[
d((t,y),S)\le b^{-1/\alpha}r_F(t,y)^{1/\alpha}.
\tag{10.4}
\]

PPA 距离精确满足

\[
d(J(p,q),S)=c^{-1}d((p,q),S).
\tag{10.5}
\]

修正临界条件

\[
\lambda b>L_0/2
\iff c>1
\]

与真实收敛区间完全一致；这证明常数 \(2\) 在渐近局部模量的统一规律中不可改进。当 \(c>1\) 且从非解点出发时，点极限的切向尾项按 \(c^{-\alpha k}\) 衰减，而集合距离按 \(c^{-k}\) 衰减。

这里没有把渐近模量 \(L_0\) 冒充正半径常数。若 \(c>1\)，选择

\[
0<\delta<
\left[
\frac{2\lambda b(1-c^{-\alpha})}{1+2/c}
\right]^{1/(1-\alpha)},
\tag{10.5a}
\]

便有 \(\lambda b>L_\delta/2\)，所以实际局部 RL＋EB 定理确实适用。

该族也把原生 coderivative 接口完整闭合。记

\[
k_+=(c-1)/\lambda,\qquad k_-=-(c+1)/\lambda,
\]

每个 \(y>0\) 分支 \(f_\sigma(t,y)=(-by^\alpha e,k_\sigma y)\) 的 Jacobian 满足：在精确径向 \(v^*=f_\sigma/\|f_\sigma\|\) 上，取 \(q=1/\alpha\)，有

\[
q\|f_\sigma\|^{q-1}\|Df_\sigma^Tv^*\|
\longrightarrow b^{1/\alpha}.
\tag{10.5b}
\]

有限分支及共同极限方向意味着：对每个 \(0<c_0<b^{1/\alpha}\)，可取依赖于 \(c_0\) 的足够小固定 \(\varepsilon_0\) 与空间半径，使 NRC 的带权下界在全部分支上统一不小于 \(c_0\)。所以任何 \(K>b^{-1/\alpha}\) 都可通过选择 \(c_0\) 得到；并非断言临界下界 \(b^{1/\alpha}\) 在同一固定径向扰动下必然实现。式 (10.4) 证明渐近最优模量正是 \(b^{-1/\alpha}\)。这给出

\[
\text{分支 Jacobian/coderivative}
\Rightarrow(q,K)
\Rightarrow\text{RL 临界收缩}
\]

的完整实算链。

该族不满足任何有信息量的 scalar semimonotonicity 参数：全部可行参数恰落在所有算子都满足的 Young 区

\[
\mu<0,\qquad \nu\le1/(4\mu).
\]

它也违反任意固定解点、任意有限对称矩阵的 oblique weak-Minty 条件。对当前固定步长 \(\lambda\) 的 Euclidean PPA（预条件矩阵 \(P=\lambda^{-1}I\)），任何要求 \(I+\lambda M+R/\lambda\succ0\) 的矩阵 semimonotonicity 证书也失败。这个结论不排除改变非对角预条件器后得到另一个算法。

### 10.2 实际收缩但不存在 \(q>1\) 统一 EB

取 \(t\in\mathbb R\)、\(0<\gamma<1\)、\(b,\lambda>0\)、\(c>1\)。令 \(y\ge0\) 时

\[
F(t,y)=\left\{
\left(-b|t|y^\gamma,\frac{c-1}{\lambda}y\right),
\left(-b|t|y^\gamma,-\frac{c+1}{\lambda}y\right)
\right\},
\tag{10.6}
\]

并令 \(y<0\) 时 \(F(t,y)=\varnothing\)。

在输入条件 \(\lambda b(|q|/c)^\gamma<1\) 的局部区域，resolvent 显式为

\[
J(p,q)=\left(
\frac{p}{1-\lambda b\operatorname{sgn}(p)(|q|/c)^\gamma},
\frac{|q|}{c}
\right).
\tag{10.7}
\]

记 \(a(q)=\lambda b(|q|/c)^\gamma\)。在 \(|p|\le P\)、\(a(q)\le\eta<1\) 的输入盒内，(10.7) 对 \(p\) 的 Lipschitz 常数不超过 \((1-\eta)^{-1}\)，对 \(a\) 的 Lipschitz 常数不超过 \(P(1-\eta)^{-2}\)；因 \(a\) 为 \(\gamma\)-Hölder，反射也为局部 \(\gamma\)-Hölder。反之，在任意 \((0,0)\) 邻域固定一个充分小的 \(h>0\)，比较 \((h,q)\) 与 \((h,0)\)，其反射切向差为

\[
\frac{2h\,a(q)}{1-a(q)}
\sim2h\lambda bc^{-\gamma}q^\gamma.
\]

故任意指数 \(\theta>\gamma\) 的 all-pairs Hölder 界均失败；这证明它是 genuine \(\gamma\)-Hölder。实际距离仍精确乘 \(1/c\)。但沿 \(t=0\)

\[
r_F(0,y)=((c-1)/\lambda)y,
\]

所以在 \((t,y)=(0,0)\) 的任何输入邻域都不存在 \(q>1\) 的统一误差界。此例严格证明：高阶误差界匹配不是实际 genuine RL–PPA 收缩的必要条件；它只是 isotropic 聚合证书的要求。该局部否定不表示远离 \(t=0\) 的每个解点都没有高阶证书。

---

## 11. 竞品理论与精确关系

### 11.1 同算法基线与可直接导入的原生不等式

为避免把不同算法混为一谈，比较采用四种量词：

| 标签 | 证书量词 | 合法用途 |
|---|---|---|
| AP | 图片内任意两图点 | all-pairs RL、resolvent 增量和单射 |
| AS | 任意图点与所有相关零点 | 最近解比较、集合距离 |
| FS | 任意图点与一个固定零点 | 固定锚点 Lyapunov；不能换成移动投影 |
| INF | 对零集取 inf 的耦合表达式 | 原生 partial-distance 能量 |

此外，“同一算法”要求相同 \(\lambda\)、Euclidean 预条件器、图局部化和选择规则；warped resolvent、非线性 kernel、degenerate preconditioner 或 lifting 需要单列。

| 理论 | 已核关键结论 | 对当前 RL–PPA 的精确关系 |
|---|---|---|
| 最大单调＋metric subregularity | Leventhal 给 \(\rho/\sqrt{\rho^2+\lambda^2}\) 的距离因子 | RL 的 \(L=1\) 切片必须恢复此基线 |
| Aragón Artacho–Dontchev–Geoffroy generalized PPA | metric regularity 加小 Lipschitz \(g_n\) 给到指定零点的一个局部线性收敛选择；strong subregularity 给已存在且留域轨道的因子 | 不需要 monotonicity，但前者是选择存在结论，后者对应孤立/strong 层；不能替代普通非孤立 \(S\) 上“任意合法选择”的 RL 结论 |
| Luke–Tam submonotonicity | \(\langle a,\lambda b\rangle\ge-\tau\|a+\lambda b\|^2\)，另有 self-mapping、stability、局部 maximality、Minty 覆盖和 EB；结论针对指定局部选择 | 定义精确等于 \(\gamma=1,L^2=1+4\tau\)；在保留相应局部化与存在性条件后，更紧耦合改善其显示的充分常数 |
| Luke–Thao–Tam almost-averaging＋subregularity | 多值、非孤立 fixed-point 集，允许分环 gauge | 另一套推广非扩张映射的框架；与 genuine RL 不作类包含声明，基准剪切族因 pointwise violation 无界而不满足其有限 almost-averaging 假设 |
| Combettes–Pennanen cohypomonotone PPA | 局部 maximal \(\eta\)-cohypomonotonicity，单算子特例需 \(\lambda>2\eta\) | 原生式 (5.5) 应直接进入编译器；其定理不是广义 EB 的固定 Q-linear 定理 |
| Evens 等 semimonotone/oblique-Minty PPPA | 一般收敛允许指定非空零点子集锚定；局部线性率另有全零集锚定、闭凸零集、连续单值 resolvent 与统一 EB 等条件；另有 scalar calculus 及后续 matrix calculus | linear RL 是 scalar balanced slice；原生矩阵/anchored 信息应按原量词保留，不宣称某个简化因子逐参数支配其他公式 |
| Valkonen partial strong submonotonicity | INF 型 PSM，带测试矩阵、局部可解与轨道假设 | 特例 \((\Xi,N,M)=(\theta I,2\lambda I,(1+\theta)I)\) 直接给 \((1+\theta)d_+^2+s^2\le d^2\) |
| 2026 local oblique-Minty / Spingarn–ProgDec+ | 图子集局部化、矩阵松弛、非孤立比较集、可微参数演算 | 这些特征本身不是 RL 新颖性；所检预印本相关定理未给 subregularity 驱动的固定 Q-linear 结论 |
| 2026 pair-SRG | operator-pair、transformed/warped resolvent 的齐次几何演算 | linear RL 可精确导入；genuine \(\gamma<1\) 的绝对尺度不能由原表示单独恢复 |
| 2026 composite semimonotone splitting | 矩阵 semimonotonicity、shift/inversion、SPD 条件和 Lipschitz resolvent | 已覆盖组成/矩阵 calculus；强制条件主要落在 Lipschitz 层 |
| 2026 nonlinear forward–backward | warped resolvent、memory、kernel、anchored comonotonicity | “nonlinear” 指算法/kernel，不等于非 Lipschitz reflected Euclidean PPA；线性率部分的强条件还推出解唯一 |
| 2026 restricted-monotonicity degenerate PPA | 只要求输出位于 \(\operatorname{ran}Q\) 的图部分 \(\operatorname{gph}A\cap(\mathcal H\times\operatorname{ran}Q)\) 单调；range 收敛与全空间 reconstruction 分开 | 已有成熟分量重建理论；令 \(Q=\lambda^{-1}I\) 时该几何定义退回全图单调，但这不是将要求退化的原定理直接特化到全秩 \(Q\) |

### 11.2 PSM 的原生导入

Valkonen 的 \((\Xi,N,M)\)-partial strong submonotonicity 要求 \(M\succeq0\)，并采用 \(\langle b,a\rangle_N=\langle Nb,a\rangle\)。原定义的比较集是 \(S=F^{-1}(0)\)；若使用截断零集，需另行验证同一截断集合上的耦合性质：

\[
\inf_{p\in S}\{\langle b,u-p\rangle_N+
\|u-p\|_{M-\Xi}^2\}\ge d_M(u,S)^2.
\]

取

\[
\Xi=\theta I,\qquad N=2\lambda I,
\qquad M=(1+\theta)I,\qquad \theta>-1,
\]

就得到

\[
\boxed{(1+\theta)d_+^2+s^2\le d^2.}
\tag{11.1}
\]

在线性 EB 下因子为

\[
\left(1+\theta+\lambda^2/\rho^2\right)^{-1/2}.
\]

这里使用同一个 \(p\) 的恒等式

\[
\inf_{p\in S}\{2\lambda\langle b,x^+-p\rangle+
\|x^+-p\|^2\}=d(x,S)^2-s^2.
\]

上面的距离因子严格小于 1 当且仅当 \(\theta+\lambda^2/\rho^2>0\)。必须保留同一比较集上的原生 INF 耦合，不能分别改变两侧集合，也不能偷换成某个固定零点的 AP/AS 单调性。

### 11.3 严格不可比性，而非“RL 支配所有理论”

当 \(c>1\) 时，正向基准 (10.1) 具有 genuine AP-RL、高阶 ordinary EB、全域单值 resolvent 和精确 Q-linear 收缩，但它：

- 不满足任意固定零点、任意有限矩阵的 oblique weak-Minty；
- 不满足任何有信息量的 scalar semimonotonicity；
- 不满足任一小管状邻域上的有限 pointwise almost-averaging 常数；
- 在二维情形不允许任何固定有限 \((\Xi,N,M)\)-PSM 证书，其中 \(M\succeq0\) 且剪切方向上的 \(N_{11}\ne0\)；特别排除固定正定测试器，但不排除 \(N_{11}=0\) 的退化测试。

这些排除不是标签比较。固定 \(p_*=(\bar t,0)\)，取图点
\(u=(\bar t+he,y)\)、\(u^*=(-by^\alpha e,k_\sigma y)\)。则

\[
\langle u-p_*,u^*\rangle=-bh y^\alpha+O(y^2),
\qquad (u^*)^TVu^*=O(y^{2\alpha}),
\]

所以任何固定有限 oblique-Minty 矩阵均失败。允许 scalar semimonotonicity 后，优化切向位移迫使参数只能落在普遍 Young 区
\(\mu<0,\nu\le1/(4\mu)\)。对 pointwise almost averaging，输入 \((\bar t,q)\) 到比较零点 \((\bar t,0)\) 的距离平方是 \(q^2\)，而 \(J\) 的切向位移平方恰为 \(\lambda^2b^2c^{-2\alpha}|q|^{2\alpha}\)，故其与 \(q^2\) 的比值无界，任何有限 violation 都失败。对二维基准的 PSM，令 \(Q=\operatorname{sym}(M-\Xi)\)、\(K=Q_{11}\)。若 \(N_{11}\ne0\)，关于水平零点坐标取 inf：\(K>0\) 时最小值的主项为 \(-b^2N_{11}^2y^{2\alpha}/(4K)\)，小于右侧非负测试距离；\(K\le0\) 时任意局部范围内也能取到负值。因此该固定测试失败；\(N_{11}=0\) 的退化法向测试不在此排除内。

这里的作用域同样重要：Luke–Thao–Tam 的排除只针对其 relative set \(\Lambda\) 含原始局部输入邻域的使用方式，不排除事后仅把一条已知轨道定义为薄 \(\Lambda\)。对 2026 local oblique-Minty，即使允许薄图子集 \(U\)，若保留其 Assumption I.a4 对同一裸 PPA（\(P=\lambda^{-1}I\)）的完整局部输入覆盖，则取 \(h=y^{\alpha/2}\) 的上述图点有
\(-b y^{3\alpha/2}\) 严格主导 \(O(y^{2\alpha})+O(y^2)\)，且图点与对应 Minty 输入都趋向 \(p_*\)。本例全域单值的 \(J\) 因而迫使这些唯一图点进入 \(U\)，薄 \(U\) 不能删掉反例序列。改变预条件器、lifting 或算法不在此排除范围。

反向取

\[
F_0(x,y)=\{(0,y),(0,2y)\},\qquad S=\mathbb R\times\{0\}.
\tag{11.2}
\]

它对所有零点具有 anchored monotonicity，满足精确线性 EB；\((\Xi,N,M)=(2I,2I,3I)\) 还给 PSM。\(\lambda=1\) 时

\[
J(p,q)=\{(p,q/2),(p,q/3)\},
\]

任意选择都收敛。但两个输出来自同一 Minty 输入而是不同图点，所以任何 \(\gamma>0\)、有限 \(L\) 的 AP-RL 都失败。

因此可安全声称

\[
\boxed{
\text{AP-RL＋高阶集合 EB 与 AS/FS weak-Minty＋EB 一般不可比。}}
\tag{11.3}
\]

对满足上述明确非退化条件的固定 PSM 测试器也有相应双向障碍。不能把它扩大为“所有能证明 PPA 收敛的理论类绝对不可比”，因为竞品可能改变预条件器、选择规则或算法。

### 11.4 文献明确陈述的技术瓶颈

- Luke–Thao–Tam 的 Remark 3.34 指出，即使简单 Douglas–Rachford 问题，迭代映射的 graphical derivative 也难计算，限制 metric subregularity 的实践验证。
- Combettes–Pennanen 的 Remark 4.4(i) 指出，具体问题的 cohypomonotonicity 常数通常难取得，使步长条件常停留在定性层面。

本报告的编译器、原生 coderivative 条件和剪切/分支 calculus 能减轻这些困难，但尚未对上述文献指定的某个公认难例给出原先不可得的完整常数，因此不能宣称“已解决该开放问题”。

---

## 12. 现有理论没有自动解决的精确缺口

现有理论已经解决了很多组成部件，所以下列内容**不是**缺口：

- 由 Jacobian/coderivative 推单调、极大单调或 metric regularity；
- 普通或高阶 metric subregularity 的抽象定义与 slope/coderivative 判据；
- 半代数多值映射的定性 Hölder inverse 与 Hölder EB；
- 非孤立零集本身；ordinary subregularity 本来就允许它；
- semimonotonicity、weak-Minty、partial monotonicity 和 preconditioned resolvent 的一般演算。

本次核验确立了下列具体输入表示的信息不足，并识别出本项目需要实现的联合定量任务；这不是对全部既有理论作不存在性断言。已证明的障碍与在本次定理级定向检索中尚未找到现成一体化输出的部分分别标明：

1. **联合任务：同一原生局部信息的联合量化。** 同时给出两点 inverse 阶数、跨分支唯一性、输入覆盖、可比较的 \(L\)，以及原 \(F\) 到完整非孤立零集的 \((q,K)\)；本次检索未找到自动输出这一整包数据的统一黑箱。
2. **联合任务：genuine 临界退化的定量化。** 一阶横截性/strong metric regularity 成功时通常已经回到 \(\gamma=1\)；本报告调用的高阶 inverse 定理还需额外量化，才能给出 PPA 临界线所需的显式小常数。
3. **已证信息不足：跨分支尺度。** branchwise 导数、monotonicity 或 inverse 性不控制分支间 Minty collision；无尺度 SRG 也不保存 \(\gamma<1\) 常数。
4. **联合任务：非孤立法向统一。** pointwise strong 高阶判据不能自动转成沿整个零流形的 ordinary set-distance EB；需要管状坐标、normal residual、uniform remainder 或 compactness。
5. **已证信息不足：过早聚合。** 把 blockwise、normal/tangential、matrix/sector 信息过早压成一个 \((\gamma,L,q,K)\) 会产生假失败；本文保留这些证书，其收益由产品锐例和原生 weak-Minty 比较具体展示。

这些是“联合可验证性与定量编译”的缺口，不应夸大为其每个构件均无人研究。

### 12.1 实际验证工作流

对一个新算子，不应从猜 \(\gamma\) 开始。按下列顺序执行：

1. **固定图片和量词。** 写明 \(\Gamma\)、输入域、合法 PPA 分支、零集 \(S\)、AP/AS/FS/INF，以及所有局部常数的共同作用域。
2. **先查 Minty existence。** 在 \(G=I+\lambda F\) 上选 maximality、Clarke/Robinson、coderivative MR、high-order open mapping、半代数 invariance-of-domain 或显式分支像。把“覆盖”和“唯一”分开记录。
3. **产生 RL 或更强几何。** 非退化时用 (5.2)、(5.6)、(6.1)；临界时用 high-order inverse、order quotient、cross-branch chain 或 shear。若只得到 AS/FS/INF，不冒充 AP-RL，直接存入编译器。
4. **产生 EB。** 先从 residual 的原生组成、最小输出分支、增长或活动约束尝试直接比较；再依次用 slope、NRC (7.5a)、FOSCMS/SOSCMS、Hoffman 或半代数 exponent。每次输出 \((q,K,\text{radius})\)，不只输出“存在”。
5. **先保持分块。** 对 normal/tangential 或 product 数据分别求 \((\gamma_i,L_i,q_i,K_i)\)；只有确实不损失时才压成单一指数。
6. **编译一步收缩。** 将全部共同作用域的约束放入 \(\mathcal C(d)\)，解析求解或用小规模 SDP/一维上确界估计 \(R_{\mathcal C}\)。证书失败时记录是 collision、coverage、order、constant 还是 lossy compression。
7. **最后做轨道局部化。** 使用 (9.1) 的有限长度预算验证每一步仍有 local resolvent 和全部证书；不能先假设轨道留在邻域。

建议每个验证器返回以下最小记录：

| 字段 | 内容 |
|---|---|
| `graph_patch` / `input_patch` | 被证书控制的图与输入区域 |
| `quantifier` | AP、AS、FS 或 INF |
| `lambda`, norm/metric | 算法与几何是否真为同一对象 |
| `branch_scope` | 分支内、分支对或完整跨分支 |
| `existence_scope` | 无、局部覆盖、全域；唯一还是允许选择 |
| `inequality` | 原生标量/矩阵/分块关系 |
| `orders_constants_radius` | \(\gamma,L,q,K\) 及其有效半径 |
| `source_or_derivation` | 已有定理定位或项目自足证明 |

这套记录使“把现有方法拿过来”变成可审计的数学接口，而不是术语拼盘。

---

## 13. 六个 Goal 的完成核账

| Goal | 本报告的实际交付 | 不能声称什么 | 状态 |
|---|---|---|---|
| 1 | 完成有界、定理级谱系与输入—输出—限制矩阵：微分/余微分、inverse、subregularity、半代数、活动集、Hoffman、SRG/IQC、PPA 竞品 | 不是穷尽式系统综述；两篇 2025 novelty gate 仍只有摘要/元数据级证据 | 完成（范围限定） |
| 2 | 给出 (5.2)、(5.4)、(5.6)、(6.1)–(6.4)、(7.1)–(7.5) 及编译器 (4.1)–(4.3)，明确输出 \((\gamma,L,q,K)\)、覆盖、唯一性和量词 | 不能把定性判据自动升级成显式常数，也不能混用不同图片/投影点 | 完成 |
| 3 | 用碰撞、无尺度、单纤维与产品反例证明具体信息不足，并把“联合任务”与“已证障碍”分开 | 未证明所有既有理论都不存在一体化特例，也不作排他式首创声明 | 完成（证据范围内） |
| 4 | 建立 order quotient、weighted chain、shear lift、输出幂变换、NRC 和 anisotropic 编译接口；完整推导并区分成熟工具搬运与项目推导 | 新颖性主张限于这一组合、量词与定量接口，不主张各组件首创 | 完成（保守 novelty 边界） |
| 5 | 在可解释的剪切/多分支解析模型上验证多值性、非孤立零集、跨分支 collision、产品假失败及指定竞品证书的不可比性 | 尚未把这些模型识别为某个文献应用中的未解实例；不支配改变算法或预条件器的理论 | 完成（结构族与指定竞品范围） |
| 6 | 查明两处文献明确指出的可验证性困难；结论是未发现已解决公认开放问题，并给出最强可辩护贡献 | 不能把实例级常数链称为普适计算程序或开放问题解决 | 完成（否定性调查结论） |

---

## 14. 证据边界

- **已核实来源**：报告所列可访问原始论文中的指定定义/定理；正式卷期与预印本编号不一致时保留版本说明。
- **项目推导**：本报告中的 RL 转换、修正标量包络、编译器、剪切族、产品与反例；均给出自足推导或由独立数学审计复核，不冒充文献原定理。
- **待核实**：两篇 2025 generalized-subsmooth/generalized metric-subregularity 论文未取得足够正文访问；因此本报告不作“点态一般 gauge 判据不存在”的排他性首创声明。
- 本工作是有界、定理级定向检索，不是带完整数据库命中数与双人筛选协议的系统综述。

---

## 15. 核心来源

以下只列实际进入本报告定理、边界或 novelty gate 的原始来源；定理编号对应所链版本。

### 15.1 广义单调性、图微分与 inverse

1. D. T. Luc and S. Schaible, *Generalized Monotone Nonsmooth Maps*, J. Convex Anal. 3(2), 195–205 (1996), Proposition 2.1：[原始全文](https://journalofconvexanalysis.com/articles/jca03013/jca03013.pdf)。
2. F. H. Clarke, *On the inverse function theorem*, Pacific J. Math. 64(1), 97–102 (1976), Theorem 1：[原始全文](https://msp.org/pjm/1976/64-1/pjm-v64-n1-p07-s.pdf)。
3. N. H. Chieu, G. M. Lee, B. S. Mordukhovich and T. T. A. Nghia, *Coderivative Characterizations of Maximal Monotonicity for Set-Valued Mappings*, J. Convex Anal. 23(2), 461–480 (2016), Theorems 3.2, 3.5, 3.7：[原始全文](https://arxiv.org/pdf/1501.00307)。
4. P. D. Khanh, V. V. H. Khoa, B. S. Mordukhovich and V. T. Phat, *Local Maximal Monotonicity in Variational Analysis and Optimization*, Math. Oper. Res. 51(2), 938–955 (2026)：[可访问全文版本](https://arxiv.org/html/2308.14193v1)。
5. J. G. Garrido, *Characterization of Strong Local Maximal Monotonicity through Graphical Derivatives* (2025), Theorem 3.1：[原始全文版本](https://arxiv.org/html/2503.18867v2)。
6. R. A. Poliquin and R. T. Rockafellar, *Prox-Regular Functions in Variational Analysis*, Trans. AMS 348(5), 1805–1838 (1996)：[作者全文](https://sites.math.washington.edu/~rtr/papers/rtr157-ProxRegular.pdf)。
7. R. T. Rockafellar, *Variational Convexity and the Local Monotonicity of Subgradient Mappings*, Vietnam J. Math. 47, 547–561 (2019)：[作者全文](https://sites.math.washington.edu/~rtr/papers/rtr251-LocalMono.pdf)。
8. R. I. Boţ and Z. Wang, *Variational convexity: new characterizations, calculus rules, and applications* (2026)：[原始预印本](https://arxiv.org/html/2606.24545v1)。
9. H. Gfrerer and J. V. Outrata, *On (local) analysis of multifunctions via subspaces contained in graphs of generalized derivatives*, JMAA 508, 125895 (2022), Theorems 2.6–2.7：[原始全文](https://arxiv.org/html/2106.00519v2)。
10. H. Frankowska, *High order inverse function theorems*, Ann. IHP C, S6, 283–303 (1989), Theorem 5.6：[原始扫描](https://www.numdam.org/item/AIHPC_1989__S6__283_0.pdf)。
11. J. H. Lee and T.-S. Pham, *Openness, Hölder Metric Regularity, and Hölder Continuity Properties of Semialgebraic Set-Valued Maps*, SIAM J. Optim. (2022), Theorem 3.1：[原始全文](https://arxiv.org/html/2004.02188v2)、[作者版本](https://optimization-online.org/wp-content/uploads/2020/04/7726.pdf)。

### 15.2 Error bounds 与次正则性

12. G. Li and B. S. Mordukhovich, *Hölder Metric Subregularity with Applications to Proximal Point Method* (2012), Definitions 3.1–3.2, Theorem 5.1：[原始全文](https://optimization-online.org/wp-content/uploads/2012/02/3340.pdf)。
13. B. S. Mordukhovich and W. Ouyang, *Higher-Order Metric Subregularity and Its Applications* (2015)：[原始全文](https://arxiv.org/html/1507.04825v1)。
14. N. D. Cuong and A. Y. Kruger, *Error Bounds Revisited* (2022), Theorems 3.2, 4.1：[原始全文](https://arxiv.org/html/2012.03941v2)。
15. A. Y. Kruger, M. A. López, X. Yang and J. Zhu, *Isolated Calmness and Sharp Minima via Hölder Graphical Derivatives*, Set-Valued Var. Anal. 30(4), 1423–1441 (2022)：[原始全文](https://arxiv.org/pdf/2106.08149)。
16. K. Bai, J. J. Ye and J. Zhang, *Directional Quasi-/Pseudo-Normality as Sufficient Conditions for Metric Subregularity*, SIAM J. Optim. 29(4), 2625–2649 (2019), Theorems 3.1, 4.1：[正式发表全文](https://math.sustech.edu.cn/uploads/20200515/3eccdc6bb121ddf544f8251ca708b1e9.pdf)。
17. G. Li, B. S. Mordukhovich and J. Zhu, *Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods*, Math. Oper. Res. (online 2026)：[已核定理版本](https://arxiv.org/html/2406.13207v1)。

### 15.3 PPA、semimonotonicity、partial geometry 与近期边界

19. D. Leventhal, *Metric Subregularity and the Proximal Point Method*, JMAA 360(2), 681–688 (2009), Theorem 3.1：[原始预印本](https://arxiv.org/pdf/0902.4200)。
20. D. R. Luke and M. K. Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, Math. Oper. Res. (online 2025), Definition 2/(10), Assumption 2, Theorem 2 and proof (28)–(29)：[期刊全文](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)。
21. D. R. Luke, N. H. Thao and M. K. Tam, *Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings*, Math. Oper. Res. 43(4), 1143–1176 (2018), Theorem 2.15, Corollary 2.19, Remark 3.34：[原始全文](https://arxiv.org/html/1605.05725v2)。
22. P. L. Combettes and T. Pennanen, *Proximal Methods for Cohypomonotone Operators*, SIAM J. Control Optim. 43(2), 731–742 (2004), Lemma 2.4, Theorem 3.1, Remark 4.4(i)：[作者全文](https://pcombet.math.ncsu.edu/sicon3.pdf)。
23. B. Evens, P. Pas, P. Latafat and P. Patrinos, *Convergence of the Preconditioned Proximal Point Method and Douglas–Rachford Splitting in the Absence of Monotonicity*, Math. Programming 214, 247–301 (2025), Definition 2.1, Assumption I, Theorems 2.4 and 2.13, Propositions 4.3, 4.7 and 4.12：[原始全文版本](https://arxiv.org/html/2305.03605v2)。
24. T. Valkonen, *Preconditioned Proximal Point Methods and Notions of Partial Subregularity*, J. Convex Anal. 28(1), 251–278 (2021), Definition 3.2 and Theorem 3.5：[原始全文](https://arxiv.org/pdf/1711.05123)。
25. B. Evens, P. Latafat and P. Patrinos, *Spingarn's Method and Progressive Decoupling Beyond Elicitable Monotonicity* (2026), preprint Definition 3.1, Assumption I.a4, Theorem 3.8, Propositions 3.6 and 4.16：[期刊页面](https://link.springer.com/article/10.1007/s10589-026-00812-1)、[核验预印本](https://arxiv.org/pdf/2504.00836)。
26. J. Quan, A. Bodard, K. Oikonomidis and P. Patrinos, *Scaled Relative Graphs for Pairs of Operators Beyond Classical Monotonicity*, v2 (2026-08-21), Definition II.1, Propositions II.3–II.4 and III.1–III.2：[原始全文](https://arxiv.org/html/2511.20209v2)。
27. J. H. Alcantara, M. N. Dao and A. Takeda, *A Splitting Framework for Composite Semimonotone Inclusions* (2026), Theorem 3.5 and Appendix B, Propositions B.1 and B.3：[原始全文](https://arxiv.org/html/2608.16609v1)。
28. J.-C. Pesquet and F. Roldán, *Nonlinear Forward-Backward Algorithm for Solving Non-monotone+Lipschitz Inclusions with Applications to Adjoint Mismatch Problems* (2026), Assumption 3.1, Algorithm 3.7, Proposition 3.6 and Theorem 3.10：[原始全文](https://arxiv.org/html/2608.22687v1)。
29. F. Xue and H. Zhang, *On Degenerate Preconditioned Proximal Point Methods under Restricted Monotonicity*, JOTA 208:74 (2026), Definition 3, Assumptions 2 and 7, Theorems 11, 18, 21 and 23：[核验全文 v5](https://arxiv.org/html/2401.08431v5)。
30. E. K. Ryu, R. Hannah and W. Yin, *Scaled Relative Graphs: Nonexpansive Operators via 2D Euclidean Geometry*, Math. Program. 194, 569–619 (2022)：[原始全文](https://arxiv.org/pdf/1902.09788)。
31. F. J. Aragón Artacho, A. L. Dontchev and M. H. Geoffroy, *Convergence of the Proximal Point Method for Metrically Regular Mappings*, ESAIM Proc. 17, 1–8 (2007), Theorems 3.1, 4.2：[原出版全文副本](https://openresearch.newcastle.edu.au/ndownloader/files/54389543)。
32. J. Peña, J. Vera and L. F. Zuluaga, *An Algorithm to Compute the Hoffman Constant of a System of Linear Constraints* (2018)：[原始全文](https://arxiv.org/html/1804.08418v1)。
33. S. Basu and A. Mohammad-Nezhad, *Improved Effective Łojasiewicz Inequality and Applications*, Forum Math. Sigma 12 (2024)：[原始全文](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/improved-effective-lojasiewicz-inequality-and-applications/022BF859F5714FDA8050F6DC1992E48B)。
### 15.4 未用于排他性结论的 novelty gates

- M. Gao, W. Ouyang, J. Zhang and J. Zhu, *Generalized Metric Subregularity for Generalized Subsmooth Multifunctions in Asplund Spaces*, Set-Valued Var. Anal. 33:14 (2025), [DOI 10.1007/s11228-025-00753-7](https://link.springer.com/article/10.1007/s11228-025-00753-7)：本次仅取得官方摘要/受限预览。
- H. Huang, X. Liu, J. Zhou and J. Zhu, *Point-based characterization of generalized metric subregularity in Asplund spaces*, Optimization (2025), [DOI 10.1080/02331934.2025.2588424](https://www.tandfonline.com/doi/full/10.1080/02331934.2025.2588424)：本次仅保留元数据级证据。

因此，这两项只作为 novelty gate；本报告不声称 generalized-subsmooth 或 point-based 一般 gauge 判据没有覆盖某一子情形。
