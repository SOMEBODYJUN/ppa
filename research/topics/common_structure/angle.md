# 普通 PPA 的横向角度包络

## 裁决

一个成体系的图几何候选是**将全部原图的零锚法向角度归一化后取闭凸包，并用一个共同半空间分离**。符号与大小是该角度图的实部与模长。对于仿射零集，候选严格介于「零锚符号 + 线性投影残差界」和全部根的 A+B 之间。其与正式一般模 RLEB、C320 在下列明确参数下均不可比。在正 reach 曲零流形上，它允许以旋转或反向法增益替代 C282 的正径向增长，但需要额外核查完整覆盖。半阶曲率、SRG 平移公式和收敛后端已有直接先例。

<a id="bridge-angle"></a>
## 1. 精确定义与定理

\(X\) 有限维欧氏，\(S=F^{-1}(0)\) 非空闭，先取 \(S\) 仿射。固定开集 \(U\)、\(R>0,\lambda>0\)，记 \(d(x)=d(x,S)\) 和 \(U_R=U\cap\{d\le R\}\)。每个输入 \(x\in U_R\) 假定存在完整近端输出。使用 \(x=y+\lambda v,\ v\in F(y)\) 的全部根。共同 P2 为每个完整根的最近输入零锚满足 \(\|2y-x-P_Sx\|\le\omega(d(x))\)，其中 \(\omega\) 非减、零处连续且 \(\omega(0)=0\)。记 \(H(t)=(t+\omega(t))/2\)。P2 单独给正式输入 B，即 \(\|x-y\|\le H(d(x))\)，且零输入所有根停留。这里的 B 不以 \(d(y)\) 为分母。

记仿射法空间为 \(N\)，对完整原图中每个 \(y\notin S\)、\(y+\lambda v\in U_R\) 取
\[
 n=y-P_Sy,\quad u=P_Nv,\quad z(n,u)=\frac{\langle n,u\rangle}{\|n\|^2}
 +i\frac{\|u-\langle n,u\rangle n/\|n\|^2\|}{\|n\|}.
\]
令 \(D\) 为全部 \(z\) 的闭凸包；也可用任何独立核准的原图超集生成 \(D\)。若没有非零输出，A 已成立。否则要求
\[
 \tag{C}\operatorname{dist}(-1/\lambda,D)\ge K/\lambda,\qquad K>1.
\]
闭凸投影使 (C) 等价于存在单位复数 \(e\)，对每个受检原图点有 \(\operatorname{Re}[\bar e(1+\lambda z)]\ge K\)。直接模型验证只需一个共同角度。**这里只取上半平面代表，再凸化**。若将双侧共轭同时凸化，纯斜增益的虚部会相消，破坏下面的旧条件蕴含。单个 \(z\) 在禁圆外只是 A 的等式改写；取闭凸包检验引入了真正的跨图点限制。

由正交投影，\(d(x)=\|n+\lambda u\|=d(y)|1+\lambda z|\)。从而 (C) 给全根 \(d(y)\le K^{-1}d(x)\)。若另有共同 Dini 模，则 \(\Theta(t)=\sum_{j\ge0}H(K^{-j}t)<\infty\)，正因几何区间端点与 Dini 积分相比较。对任何 \(\Theta(d(x^0))<d(x^0,X\setminus U)\) 的初始输入，有限迭代前缀先由 A、B 留域并因覆盖得以延拓，随后求和得有限长度与到 \(S\cap U\) 的点收敛，任意第 \(k\) 步后的尾长至多 \(\Theta(d(x^k))\)。用于同合同的 P3 仍能加回，评价必须取完整 \(F(y)\)，但本证明没有用 P3。

**与符号 + 大小的量化关系。** 对受检原图，\(\langle n,u\rangle\ge0\) 正是 \(\Re z\ge0\)；同窗投影真残差界 \(\inf_{v\in F(y)}\|P_Nv\|\ge m\,d(y)\) 蕴含 \(|z|\ge m\)。于是 \(D\subseteq\{a+ib:a,b\ge0,\ a+b\ge m\}\)。从 \(-1/\lambda\) 到这个区域的最近点是 \((0,m)\)（\(\lambda m\le1\)），或斜边线段上的投影（\(\lambda m\ge1\)）。得到
\[
 K_{\rm hull}(m)=
 \begin{cases}\sqrt{1+(\lambda m)^2},&\lambda m\le1,\\
 (1+\lambda m)/\sqrt2,&\lambda m\ge1.
 \end{cases}
\]
在上述 anchored 符号类中常数对这一证书是锐的：二维 \(F(y)=\{my,mJy\}\)，\(J\) 为 \(90^\circ\) 旋转，两个线性模式分别给出斜边两端点。这一多值原图一般并非两点单调。投影大小和符号在曲窗内也给同一个 \(K_{\rm hull}\)，但法向映射须事后核准曲率。

**独立的误差余量。** 固定 \(y\)，\(u\mapsto z(n,u)\) 是 \(1/d(y)\)-Lipschitz，因为实部为平行坐标、虚部为垂直投影的范数。若新图每个受检点在同一个 \(y\) 都有旧图值见证，且法投影偏差至多 \(\varepsilon d(y)\)，则新凸包落在旧凸包加半径 \(\varepsilon\) 的圆中，\(K\) 最多损失 \(\lambda\varepsilon\)。图扰动的覆盖、P2 与留域仍各自核查。

<a id="bridge-angle-comparisons"></a>
## 2. 严格性及 C320/C323

以下 \(\lambda=1,U=X,S=\{0\}\)，所有例子能共用 \(\omega(t)=3t\) 与任意 \(R>0\)。

1. **符号 + 误差界严格推出证书。** \(F(y)=(-I+kJ)y,\ k>1\)，完整输入映射 \(kJ\) 是双射，\(D=\{-1+ik\}\) 且分离量 \(K=k\)。唯一近端步的反射比为 \(\sqrt{1+4/k^2}<3\)。其锚定符号恒负。如需同目标 \(K\)，选 \(k=K_{\rm hull}(m)\)。
2. **证书严格推出 A+B。** 一维 \(F(y)=\{(k-1)y,(-k-1)y\}\)，完整根为 \(x/k,-x/k\)，均有 A（精确收缩因子 \(1/k\)）及 P2（反射上界 \(1+2/k\)）。但凸包 \([-k-1,k-1]\) 含 \(-1\)。而在光滑单值 \(F=\operatorname{diag}(k-1,-k-1)\) 上，两坐标轴同样给这两个端点，且 \(I+DF=\operatorname{diag}(k,-k)\)。故 C323 的横向最小奇异值精确判据完整通过，本证书仍失败。旋转前的普通 PPA 在这里有 A，角度包络是一项更强、独立的模式一致性。
3. **证书不推出 C320 或正式旧 RLEB。** 二维令 \(k=\sqrt5/2\)，\(F(y)=\{(-I+kJ)y,kJy\}\)。两个完整输入映射为 \(kJ,I+kJ\)，均双射。\(D=[-1,0]+ik\)，分离量恰为 \(k\)。两支反射比为 \(\sqrt{1+4/k^2}\)、\(1\)；第一支为锐。\(r_F(y)=k\|y\|\)。任何合法真残差模 \(\psi(s)\) 在小尺度都至少为 \(s/k\)，而最小 P2 给 \(H(t)/t\ge (1+\sqrt{1+4/k^2})/2>3/2>k\)，故旧兼容不可能给任何 \(\kappa<1\)。在同一精确目标 \(\kappa=1/k\) 下，首支实际图值在输入尺度 \(t\) 时填满半径 \(\sqrt{1+k^2}t/k\) 的球。次支图值 \(v=kJy\) 在 \(\|y\|=\sqrt{1+k^2}t/k^2=6t/5>t\) 时仍入球。取 \(t\) 足够小则 \(y\) 已由首支进入 C320 的受检输出窗，因而完整逆纤维检查失败。该输出距离甚至超过 \(t\)，故此反例对所有 \(\kappa<1\) 均否证 C320。
4. **旧 RLEB 或 C320 不推出证书。** 第 2 例取两支输入倍率 \(k=6\)，并取比较目标 \(\kappa=2/\sqrt5\)，仍取共同模 \(3t\)。此时 \(H(t)=2t\)，\(r_F(y)=5|y|\)，\(\psi(s)=s/5\) 给兼容 \(2t/5<\kappa t\)。C320 由旧条件推出，但角度包络含 \(-1\)。

C320 凸化的是绝对图值，并检验逆纤维的输出距离层；这里凸化的是已锚定的归一化法向夹角。一个保留径向层和原纤维，另一个测试跨模式共同角度。取其形式析取可保旧蕴含，但缺乏单一结构解释；第 2 例的 \(k=2,\kappa=1/2\) 同时否证两种证书，而满足 A+B。对此例，C320 的实际图值半径为 \(3t/2\)，较小正支图值等于 \(y\)，故越过 \(\kappa t\) 的纤维会被纳入。C323 仍优先用于可微局部单值合同，本条件主要适用于多值模式或易于核准共同夹角的原生结构。

## 3. 曲法向转移与 C282/C277

取 \(S\) 为具有正常管半径 \(\rho>0\) 的闭子流形，局部投影在共同管内为 \(L_P\)-Lipschitz。对相关 \(p,q\in S\) 假设 \(\|P_{N_pS}(q-p)\|\le C\|q-p\|^2\)；比较 \(p+t\nu\) 到 \(p,q\) 的平方距离，取正反法向及 \(t\uparrow\rho\)，得 \(C=1/(2\rho)\)。令 \(u=P_{N_{p_y}S}v\)，其中 \(p_y=P_Sy\)，照前定义 \(z\) 和共同包络。P2 已全根成立时，缩小输入窗可保证全部输出位于固定管内，因为 \(d(y)\le d(x)+H(d(x))\)。

令 \(t=d(x)>0\)，\(y\notin S\)，插入 \(p_x=P_Sx\)：
\[
 Kd(y)\le\|P_{N_{p_y}S}(x-p_y)\|
 \le d(x)+C\|p_x-p_y\|^2\le t+CL_P^2H(t)^2.
\]
因此当 \(D_R^{\rm curv}=CL_P^2\sup_{0<t\le R}H(t)^2/t<K-1\) 时，全部根 A 的因子为 \((1+D_R^{\rm curv})/K\)。\(H(t)=o(\sqrt t)\) 足以通过缩窗验证；半阶时须检查常数。若直接得到 \(\|P_T(x-y)\|\)，C282 的空球法可用 \(\|P_T(x-y)\|^2/[2(\rho-\|n+\lambda u\|)]\) 替代整步误差，并在 \(\|n+\lambda u\|<\rho\) 时应用。

**完整覆盖的临界失败例。** \(S=\mathbb S^1,\ \lambda=1,\ 0<R<\min(1,1/K)\)，对 \(y=(1+s)p,\ p\in S,\ 0<s\le R\) 定义唯一图值
\[
 v=-(K+1)s p+\sqrt{(1+s)^2-(1-Ks)^2}\ Jp.
\]
在 \(p\in S\) 取 \(F(p)=\{-c p:0\le c\le R\}\)，其他点取空纤维。外支连续延拓至 \(v=0\)，整个图闭，零集恰为 \(S\)。外支每一半径上的输入是同一半径的一次旋转，盖住所有外侧输入，圆上的图纤维盖住所有内侧输入。零输入只能零步。外支 \(\|v\|^2=2(K+1)(s+s^2)\)，故由 \(\|2y-x-P_Sx\|\le d(x)+2\|v\|\) 可取 \(\omega(t)=[\sqrt R+2\sqrt{2(K+1)(1+R)}]\sqrt t\)。非零输出的法向归一化为 \(z=-(K+1)\)，所以有 \(K>1\) 的形式法向余量，但所有外侧合法步恒距，A 失败。

原项目曲几何是 **C282**。UC2、UC7 及 §3 已有曲率半阶、临界系数、覆盖障碍及圆弦补偿。本报告只是把正径向前端泛化为共同角度分离，给在此合同下的覆盖齐备的负法向恒距例。C282 可通过连续原始分支和整个恒等同伦上的边界排除，自行给覆盖，本报告把覆盖作为前提；反向法增益可能让该同伦中途退化。**C283** 属于 co-hypomonotone 真图 inexact 预算问题。**C277** 已有有限原生状态、曲线收缩和长度势的后端，本方法只提供一个感知方向的原图证书，可作为其半代数前端（必须保留虚部非负的平方根支），并未改变其后端或状态完备性问题。

## 4. 一手资料及失败路线

| 原文 | 核到的机制及迁移界限 |
|---|---|
| Ryu–Hannah–Yin, [Scaled Relative Graphs](https://arxiv.org/pdf/1902.09788), v4 §3、Theorem 4、§6 | 既有 SRG 通过图弦的模、夹角刻画单调半平面，并给平移、逆运算，另论及次正则。这里的 \(|1+\lambda z|\) 是既有原理在零锚法投影后的特例。可能的独立内容是上半锚定数据先凸化和全部根的严格比较，全球优先未核。 |
| Evens–Pas–Latafat–Patrinos, [arXiv:2305.03605](https://arxiv.org/pdf/2305.03605), Definition 2.1、Theorem 2.4、Definition 4.1；Gorbunov et al., [arXiv:2210.13831](https://arxiv.org/pdf/2210.13831), §1.1 Eq. (2)、§2 | 静态证书 \(\langle n,u\rangle+\alpha\|u\|^2\ge b\|n\|^2\) 精确属于 \((b,-\alpha)\)-semimonotonicity。斜 weak Minty 的预条件 PPA 具有半空间 Fejér 证明，部分点列收敛断言需投影目标覆盖、连续单值预解式及松弛范围。星形负共单调的普通 PPA 在 \(\lambda>2\rho\) 下有残差耗散。此类扇区不能列为原创。 |
| Leventhal, [arXiv:0902.4200](https://arxiv.org/pdf/0902.4200), Theorem 3.1；Bauschke–Moffat–Wang, [arXiv:1101.4688](https://arxiv.org/pdf/1101.4688), §1–2 | 最大单调给覆盖和 firm nonexpansiveness，MSR 给逆增益，合起来给局部线性收缩。Minty 变换只重表示。\(F(y)=y^3\) 显示单调没有线性 MSR。\(-2I\) 具有完整覆盖和线性 MSR，仍有翻转周期。 |
| Solodov–Svaiter, [Error Bounds for Proximal Point Subproblems](https://w3.impa.br/~benar/docs/solodov/err-bound.pdf), Eq. (11)–(13)、Theorem 2；Solodov–Tseng, [D-Gap](https://pages.cs.wisc.edu/~solodov/soltse00gap.pdf), §2、Theorem 1 | Enlargement/Fitzpatrick 型缺陷加方程缺陷构成最大单调下固定输入的强凸子问题 merit。它在所有精确 PPA 步上为零，不能作为不同精确步的下降势。VI 自然残差需要其投影结构及强单调或适当 P 条件。全空间可逆纯斜 \(F(y)=Jy\) 的对偶 Fitzpatrick gap 在每个 \(x\ne0\) 为 \(+\infty\)，因 \(\sup_y\langle x-y,Jy\rangle=\sup_y\langle x,Jy\rangle\)，实际 PPA 却线性收缩。 |
| Marcotte–Zhu, [Weak Sharp Solutions of Variational Inequalities](https://www.iro.umontreal.ca/~marcotte/ARTICLES/1999_SIAM.pdf), §§3–4；Combettes–Hirstoaga, [Equilibrium Programming](https://pcombet.math.ncsu.edu/jnca1.pdf), Condition 1.1、Lemmas 2.12, 2.15 | VI 弱锐是对偶间隙的线性增长几何，有具体连续性、广义单调性及紧性假设。标准平衡双函数用反向和符号与第二变量凸性、下半连续性获得 firm nonexpansiveness，能恢复最大单调包含，定义未自动供同窗真残差率。 |
| Lessard–Recht–Packard, [IQC](https://arxiv.org/pdf/1408.3595), Theorem 4；Robinson, [Normal Maps](https://pubsonline.informs.org/doi/10.1287/moor.17.3.691), 主定理；Dontchev–Rockafellar, [Regularity and Conditioning](https://sites.math.washington.edu/~rtr/papers/rtr191-RegularityConditioning.pdf), §§2–4 | IQC 以互联系统和硬二次约束产生 LMI 收敛证书，不能默认 LMI 是原算子的物理结构。多面体 normal map 的 coherent orientation 给 Lipschitz 同胚，不能给增益大于 1。反例 \(I+\lambda F=\tfrac12 I\) 有光滑可逆且正定的完整输入方程，全部根仍扩张。 |

## 5. 研究状态

数学推导与反例均可独立复核，公开先行性为 open，尚未提升规范 Claim。该候选的价值是可证明的、对投影图值误差稳定的共同角度机制，超出已有 C320 的一部分图。它没有解决从任意正式 RLEB 出发的统一非析取桥。下一项有效检验是从一个来源独立的多值原模型直接核准共同角度与全部根覆盖，以及检查是否已有同样的锚定上半 SRG 凸分离。
