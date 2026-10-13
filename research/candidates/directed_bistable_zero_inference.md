# 有向双稳态网络：解少量稳定零点，推断未见零点

状态：第四章主候选，解析证书及精确有理复算通过；不登记新 Claim，不改主论文、摘要或编号。它是原生非对称 Nagumo 模型的有限周期、异质载荷实例，参数是可认证基准，不是实测标定。这里的“解”只指完整算子零点；它们不被统称为极小点。

## 1. 原问题、来源及固定对象

原任务是在有偏向的双稳态节点网络上求稳态：

\[
\dot u_i=u_i-u_i^3+a(u_{i+1}-u_i)+c(u_{i-1}-u_i)+b_i,
\qquad i\pmod {13}.
\]

每个节点本身有双稳态反馈，相邻节点按两个不同方向的传输率耦合，$b_i$ 是固定节点输入。Slavík–Stehlík–Volek 的正式论文 *Well-posedness and maximum principles for lattice reaction-diffusion equations*, Adv. Nonlinear Anal. **8** (2019), 303–322，DOI [10.1515/anona-2016-0116](https://doi.org/10.1515/anona-2016-0116)，印刷 p.304 式(1.3)明确容许非对称传输，p.315 Example 4.8／式(4.12)给 $u(1-u^2)$ 的 Nagumo 反应。已读出版社提供的[全文镜像](https://www.researchgate.net/publication/315339838_Well-posedness_and_maximum_principles_for_lattice_reaction-diffusion_equations)，没有依据摘要补推结论。13 节点周期闭合、以下异质输入及隐式求解器是本候选的选择，不冒称源论文已经计算过这个实例。

固定

\[
a=7/25,quad c=11/50,quad
b=(-7,4,2,-3,6,-5,1,8,-4,3,-6,5,-2)/1000.
\]

令 $(Su)_i=u_{i+1}$，$L=2I-S-S^{-1}$，

\[
D=a(I-S)+c(I-S^{-1}),quad
\operatorname{Sym}D=\tfrac14L,quad
K=\operatorname{Skew}D=\tfrac3{100}(S^{-1}-S).
\]

在欧氏 $X=\mathbb R^{13}$ 上取

\[
F(u)=u^{[3]}-u+Du-b,qquad v=I,qquad\lambda=1.
\]

**完整零集**始终是

\[
S_F=\{u\in\mathbb R^{13}:u_i^3-u_i+(Du)_i=b_i, 1\le i\le13\}.
\]

这是完整隐式集合，不是下面已求出的16点。无需列出全部零点坐标才能认证其有限性、净指数、个数下界和位置。$M=\{p_1,\ldots,p_{16}\}\subset S_F$ 是精确小球证书定义的已识别稳定零点集；它是紧零维光滑流形，$\chi(M)=16$，不是全部稳态或全部稳定态。

## 2. 完整更新、所有纤维及最短覆盖证明

同一个原生稳态方程的后向 Euler／普通 PPA 为

\[
u^{k+1}\in J_F(u^k),qquad u^k=u^{k+1}+F(u^{k+1}).
\]

令 $H=I+F=u^{[3]}+Du-b$。完整图具有无遗漏的输出参数化

\[
\operatorname{gph}J_F=\{(u^{[3]}+Du-b,u):u\in\mathbb R^{13}\}.
\]

对任意 $y\ne z$，逐坐标恒等式给

\[
\langle H(y)-H(z),y-z\rangle
\ge\tfrac14\sum_i(y_i-z_i)^4
\ge\frac1{52}\|y-z\|^4>0.
\]

反对称部分在内积中抵消。又 $\langle H(u),u\rangle\ge\|u\|^4/13-\|b\|\|u\|$。对于**每个** $x\in X$，充分大球上 $H(u)-x$ 严格向外，Brouwer 度为1，故有输出；严格单调给唯一性。相同强制界使原像有界，连续性与唯一性给逆连续。因此

\[
J_F(x)=\{T(x)\},quad T=H^{-1}:X\to X
\]

是全部输入上的完整单值关系，并满足 $\operatorname{Fix}T=S_F$。该非对称 $H$ **不是**某凸势的梯度，不将更新叫作 global-min prox；存在唯一性的证明走的是完整单调方程。

上式还给全域 $1/3$-Hölder：

\[
\|T(x)-T(z)\|\le52^{1/3}\|x-z\|^{1/3}.
\]

因 $D\mathbf1=0$，完整公式在一条输入线上为

\[
T(-b+t^3\mathbf1)=t\mathbf1.
\]

所以 $-b$ 处最佳 Hölder 指数恰为 $1/3$，非 Lipschitz。$F(0)=-b\ne0$，故这是**非零点输入**的非 Lipschitz；所有固定点处将另证 $T$ 可微。不能替代 Hamilton／三角例的解点 noncalm 作用。

本例没有简洁的全坐标闭式 $T$ 或全局闭式轨道。最短承重证明就是上一段的严格单调、强制与输出参数化。局部极限则明确是所在小球的唯一 $p_i$；不以数值选择代替完整更新。

## 3. 十六个已求零点的精确认证

[代码](../code/directed_bistable_zero_inference/verify.py)用18个固定种子节点初值，经本网络的显式动力提出中心，再 Newton 反算；这些步骤只用于发现，不冒充被认证的 PPA 轨道。所得16个中心 $z_i\in10^{-12}\mathbb Z^{13}$ 逐个通过**精确 Fraction 算术**：

\[
\|z_i\|_\infty\le101/100,quad
\operatorname{Sym}DF(z_i)\succ(2/5)I,quad
\|F(z_i)\|_1<(1/3)10^{-10},quad
\|z_i-z_j\|^2>1.
\]

正定性以精确 $LDL^\top$ 及重构检查证明；全部有理中心、残差与 pivots 均在 [results.json](../code/directed_bistable_zero_inference/results.json)，浮点特征值不承重。

取 $\rho=1/100$、$\varepsilon=10^{-10}$、$m=1/3$。在 $B_\rho(z_i)$ 上唯一变化的对角项满足

\[
\|\operatorname{Sym}DF(u)-\operatorname{Sym}DF(z_i)\|
\le6(101/100)\rho+3\rho^2=609/10000,
\]

故 $\operatorname{Sym}DF\succeq mI$。在 $B_\varepsilon(z_i)$ 边界，

\[
\langle F(u),u-z_i\rangle
\ge m\varepsilon^2-\|F(z_i)\|\varepsilon>0.
\]

向外同伦到 $u-z_i$ 给该球度1和一个真零点 $p_i$。强单调给整个 $B_\rho(z_i)$ 中唯一性及

\[
\|p_i-z_i\|\le\|F(z_i)\|/m<\varepsilon.
\]

这是非梯度根存在证明，未使用“限制势的极小值”。中心间隔使16根及其下述小球互不相交。Jacobian 的对称部分正定使它们是 $\dot u=-F(u)$ 的局部稳定平衡，但没有被称为优化极小点。

## 4. 同窗、同锚、完整输出的 RLEB–GPPA 证书

取同一组数据

\[
U=\bigcup_{i=1}^{16}B_\delta(p_i),quad
\delta=1/200,quad R=1/10000,quad\lambda=1,quad m=1/3,
\]

\[
a(t)=t,quad\omega(t)=t,quad h(t,q)=q,quad
\psi(t)=3t,quad\bar t=1,quad
\rho_E(q)=q,quad g(q)=q/3,quad
\kappa=3/\sqrt{10}.
\]

允许关系就是**全部** $J_F$；无删分支。因 $\delta+\varepsilon<\rho$，$B_\delta(p_i)$ 位于相同正曲率窗。中心间隔也保证 $p_i$ 是这里输入和输出的唯一物理最近零锚。

**先定位实际输出。** 对 $x\in B_\delta(p_i)$，若完整输出 $y=T(x)$ 沿某射线超过半径 $\delta$，局部强单调给边界处

\[
\langle H(p_i+\delta e)-H(p_i),e\rangle\ge(1+m)\delta.
\]

全域单调性保证越过该边界后同一径向投影不减，而 $H(y)-H(p_i)=x-p_i$ 的投影小于 $\delta$，矛盾。因此所有完整输出先进入同一球；再积分得到

\[
\|y-p_i\|\le\tfrac34\|x-p_i\|.
\]

**反射与真残差。** 写 $A=y-p_i$、$W=F(y)=x-y$，则 $x-p_i=A+W$。用同一锚，

\[
\|2y-x-p_i\|^2=\|x-p_i\|^2-4\langle A,W\rangle
\le d(x,M)^2.
\]

完整 $F(y)$ 为 singleton，按定义 $r_F(y)=\inf_{w\in F(y)}\|w\|=\|F(y)\|$。强单调独立给

\[
d(y,M)=\|y-p_i\|\le3r_F(y).
\]

这是所声明局部输出窗中的真实 EB；不是从某个选中图值的范数偷换而来。因为 $DF(p_i)$ 可逆，局部最佳 EB 幂次为1：沿任意非零微小位移，距离与残差同为一阶，幂大于1不能成立。

**兼容与长度。** $K(t)=H_{\rm step}(t)=t$，$K(R)/\lambda=R<\bar t$。C249 的直接门用上述常数给 $\psi(K(t))=3t$，确实失败，不能硬套 C02-v3。使用规范 **C250 能量分支**，对全部 $0<t\le R$ 及其类型窗中的 $q$，

\[
\rho_E(q)^2+\lambda^2g(q)^2=(10/9)q^2
\le\tfrac12(a(t)^2+\omega(a(t))^2)=t^2
\Longrightarrow q\le\kappa t.
\]

相同物理一步位移 $\|x-y\|\le K(t)=t$ 给

\[
\Theta(t)=\frac{t}{1-3/\sqrt{10}}<20t.
\]

因为 $3/\sqrt{10}<19/20$，所有 $x\in U_R$ 的严格共同预算为

\[
\Theta(d(x,M))\le\Theta(R)<20R=1/500
<49/10000=\delta-R\le d(x,U^c).
\]

C250 的 $M_0=\psi(\bar t)=3$ 只是标量类型窗；该窗中原 EB 合同只调用**实际局部输出**，不声称在半径3物理球上有 EB。距离—反射能量不等式本身闭合全部 $q$ 的门。所有有限前缀留域、全政策可续、物理有限长度及同一尾界成立。零距离输入 $x=p_i$ 的全部输出就是 $p_i$，没有零输入吸收漏洞。

因此任意认证初值的唯一完整轨道收敛到所属球的 $p_i$，距离不超过 $\kappa^k d_0$，第 $k$ 步之后总位移不超过 $20\kappa^k d_0$。局部直接强单调另给更锐的 $(3/4)^k$ 距离界；这里不把保守 RLEB 常数当最佳率。

## 5. 独立拓扑、全局入口和全根正则：无需求完方程

**隔离及目标指数。** 十六个互不相交闭小球都是局部吸引管，$M$ 为16个点，$\chi(M)=16$。还可独立微分核对每点指数：$\operatorname{Sym}DF(p_i)\succ0$，所以 $\det DF(p_i)>0$；$D(I-T)(p_i)=DF(p_i)(I+DF(p_i))^{-1}$，分母 determinant 正，指数各 $+1$。

**全局指数。** 对 $y=T(x)$ 的最大分量，$D_i y=a(y_i-y_{i+1})+c(y_i-y_{i-1})\ge0$；最小分量相反。$\|b\|_\infty=1/125$，故

\[
T([-11/10,11/10]^{13})\subset\operatorname{int}[-11/10,11/10]^{13},
\]

因为 $(11/10)^3=1331/1000>11/10+1/125$。相同极值论证和 $(21/20)^3-21/20=861/8000>1/125$ **独立排除所有** $[-21/20,21/20]^{13}$ 外的零点。紧立方体为可缩 ENR，完整连续 $T$ 总固定点指数为1，边界无固定点。亦可直接在立方体边界用 $I-sT$、$0\le s\le1$ 同伦：$sT$ 始终严格在内，边界无零点，所以度等于 $I$ 的度1。

这是独立重建的物理立方体入口，使用经典固定点指数归一化、局部化和可加性（Benjamin–Gottlieb，[作者 PDF](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf) §2.1）。$C=2T-I$ 在无穷远仍有线性项，**不满足**现有 C254 全尺度次线性反射前件，不能将本例登记为该定理原样实例。

**全根正则的廉价证书。** 令 $\mathcal R=\mathbb Z_{(3)}$。$F_i=u_i^3+\sum_j A_{ij}u_j-b_i$，$A=D-I$ 的所有系数和输入都在 $\mathcal R$。graded 单项式序的首项为两两互素的 monic $u_i^3$。替换 $u_i^3=-\sum_jA_{ij}u_j+b_i$ 降低总次数；两个替换重叠的 product identity 消去全部歧义，所以商环

\[
\mathcal B=\mathcal R[u]/(F_1,\ldots,F_{13})
\]

以 $u^\alpha$、$0\le\alpha_i<3$ 为有限自由基，秩 $3^{13}$。完整自足环上证明见[全根证书附页](graph_quartic_modular_certificate.md)，没有 field-only 除法偷换。

在模3下，$a=c=1$、$D=L$，故

\[
\det DF(u)\equiv\det(L-I)=2\pmod3.
\]

后一个13阶小行列式是唯一需要运行的全局算术检验。证明中“乘以 $\det DF$”在有限自由商环上的矩阵模3为 $2I$，其行列式是单位；伴随矩阵证明 $\det DF$ 在商环中为单位。对任意复零点 evaluation 即得其 Jacobian 非奇异。**不需要**生成 $3^{13}$ 阶矩阵，也不需要逐个求根或对未知复坐标做模3 reduction。由有限自由维数及每个局部代数维数1，恰有 $3^{13}=1594323$ 个不同复根；这不是实根数量。

对任意实零点 $p$，$p\ne0$。$\operatorname{Sym}DH(p)=3\operatorname{diag}(p_i^2)+(1/4)L$ 正定：其 kernel 必是常数且所有非零 $p_i$ 对应坐标为0，故只能为0。因此 $DH(p)$ 可逆、全部特征值实部正、determinant 正，$T$ 在**每个**固定点可微，各点指数是 $\operatorname{sign}\det DF(p)\in\{\pm1\}$。这独立关闭“原算子正则不代表逆正则”的门。

**额外信息。** 指数平衡现在给

\[
i(T,S_F\setminus M)=1-16=-15.
\]

所以至少有15个**不同的未见负指数实零点**；全部未见实零点总数为奇数，完整实零点数至少31且为奇数。它们位于

\[
[-21/20,21/20]^{13}\setminus\bigcup_i B_{1/100}(z_i).
\]

没有得到准确总实根数、全部稳定态数或每点坐标；原方程或可靠求解器仍需用于这些任务。非对称 Jacobian 无 Morse index，不把负指数叫作 index-one saddle。不过 detDF<0 保证存在负实特征值 $h$；因 $\operatorname{Sym}(I+DF)\succ0$，$-1<h<0$，对应 $DT$ 特征值 $(1+h)^{-1}>1$，故这些点对该 PPA 和原连续动力均不稳定。

## 6. 先预测、后核对的闭环与计算成本

代码先完成16个局部根证书、小矩阵模3与共同窗口，保存“净指数−15／至少15个额外根”的推断。**之后**独立随机初值求解产生15个负指数根候选，并逐个用精确有理 Banach–Newton 证书验证：若 $B=DF(c)^{-1}$，在半径 $r=10^{-7}$ 的无穷范数球上，

\[
q=\|B\|_\infty\,3(2\|c\|_\infty r+r^2)<1/2,quad
\|BF(c)\|_\infty+qr<r.
\]

映射 $u\mapsto u-BF(u)$ 严格自映射并收缩，故各有一个真实根；同一 Neumann 界使 $DF$ 沿球保持可逆，中心精确 detDF<0 给该根指数−1。精确中心间隔及与已知根球的距离排除重复。该闭环实际核对了15个独立见证；**不声称这些是全部额外根**，还可能有指数抵消的未见点。

本机 Python 3.12.14／NumPy 2.3.5／SciPy 1.17.0，一次运行18个局部提出步骤约0.024秒、16个精确稳定根证书及小矩阵约0.101秒。这是本机记录，不是速度保证。后核对找到15点用了366个初值；全部 witness 的 Fraction 证书也已通过。完整近端的106个零／跨符号／边界／远端输入和320个局部输入的反算最大相对误差约 $2.3\cdot10^{-16}$，它们是诊断，以上全称结论不依赖样本。

“省事”的明确含义是：条件认证不枚举未知根，成本为少量13阶局部矩阵和一个13阶模行列式；没有做 $1594323$ 路总次数同伦。该数字既不是最佳实根算法成本下界，也不证明端到端算法加速。图递推可以降维，特殊网络还可能有更快求根法；未运行它们的比较，不宣称赢过所有 solver。

## 7. 旧方法的准确关系

1. **普通单调 PPA 门确实不满足。** 常数方向上 $\langle F(t\mathbf1)-F(0),t\mathbf1\rangle=13(t^4-t^2)<0$（$0<|t|<1$）。$H$ 单调不能被当成 $F$ 单调。
2. **对称势 $f_{\rm sym}$ 的普通梯度能量桥确实失效。** $DF$ 非对称，故 $F$ 不是欧氏标量势梯度。自然对称势 $f_{\rm sym}=\sum(u_i^2-1)^2/4+u^TLu/8-b^Tu$ 的梯度为 $F-Ku$。奇数周期的 $\ker K$ 为常数，异质 $b$ 排除常数零点，因此每个 $F$ 零点 $p$ 都有 $\nabla f_{\rm sym}(p)=-Kp\ne0$；在驻定 PPA 步上，ABS 型 $\|\nabla f_{\rm sym}(Tx)\|\le C\|x-Tx\|$ 不成立。仅排该势／该普通导入，不排所有 Lyapunov、merit、后验 KL 桥或坐标变化。
3. **指定的全图 weak-Minty PPPA 门也失败。** Evens–Pas–Latafat–Patrinos，arXiv [2305.03605v2](https://arxiv.org/pdf/2305.03605)，2024-05-06，Definition 2.1／Eq.(2.1)，Theorem 2.4 要求某零点 $p$ 与有限对称 $V$ 对全部图满足 $\langle F(z),z-p\rangle\ge\langle F(z),VF(z)\rangle$。在另一简单零点 $q$ 附近取 $z=q+te$，正负 $t$ 迫 $DF(q)^\top(q-p)=0$，与可逆性和 $q\ne p$ 矛盾。其 Definition 后允许的输出域限制也不救本全域算法：$T$ 满射，$P=I$，限制仍是整个图。Theorem 2.13 另有全零集凸等前件，当前多点有限零集也不满足。只排此准确全局入口，未排局部版本、其它方法或更广理论。
4. **源模型已有方法并不一无所知。** Slavík，*Reaction–diffusion equations on graphs: stationary states and Lyapunov functions*, Nonlinearity **34** (2021), 1854–1879，DOI [10.1088/1361-6544/abd52c](https://doi.org/10.1088/1361-6544/abd52c)，[作者 PDF](https://www2.karlin.mff.cuni.cz/~slavik/papers/reaction-diffusion.pdf)：§2 的简单无耦合分支延拓容许非对称扩散，Theorems 2.2、2.4 给充分小耦合条件下非负分支的分类／数量；未经定量延拓界，不能自动应用到本固定 $a,c$ 和异质载荷。Theorem 3.1（作者稿第16页）则要求对称扩散、同节点反应及分离凸 Lyapunov 导数，当前实例不满足。没有声称原文证明本周期实例不存在其它稳态，或所有传统研究均无法分析它。
5. **经典正面必须保留。** 局部强单调直接给更短收缩证明；经典 Brouwer／固定点度复用相同小球及全根证书，也能得到相同额外根下界。原连续网络还具有合作系统结构。RLEB 不是这些拓扑事实的唯一发现者。真正可承载的差异是同一完整临界非 Lipschitz 求解器、局部真实残差／物理长度证书及未见零点后处理的一体接口；没有外部首创或复杂度定理。

## 8. 攻击、证明准入表与作用边界

| 门／攻击 | 裁决与依据 |
|---|---|
| 原生性 | **通过**：已有非对称 cubic Nagumo 格点方程；有限周期和输入是明确建模选择。参数带算术便利，非实测实例。 |
| 全输入 coverage、全部近端纤维 | **通过**：完整输出参数图、严格单调强制 homeomorphism；唯一输出。 |
| 零输入与固定点吸收 | **通过**：$T(-b)=0$，但 $0\notin S_F$；$T(0)$ 非零；每个 $p\in S_F$ 全纤维仅 $p$。 |
| 跨符号、远端输入 | **通过**：全域四次单调不等式不要求坐标同号；正负大输入同一个完整逆。 |
| 非孤立零集 | **本例无此作用**：mod3证书排除所有正维分支；不得替代非孤立零线／球面专例。 |
| 反射、真 EB、同锚 | **通过**：先完整输出定位，再同球强单调；局部 $\gamma=1$、EB幂1。 |
| 兼容、留域、物理可和性 | **通过 C250**；指定 C249/C02 直接常数组合失败，不能掩盖。 |
| 原 C254 全尺度反射门 | **失败**；采用独立紧立方体指数桥。 |
| 全零点 $DF$ 与 $DH$ 正则 | **分别通过**：有限自由模证书；connected SymDH 正定。 |
| 临界步长 | **通过 $\lambda=1$**；$0<\lambda<1$ 则全域 Lipschitz，$\lambda>1$ 在 $x=-\lambda b$ 至少有 $0,\pm\sqrt{1-1/\lambda}\mathbf1$ 三个完整输出。 |
| 不任意换 GPPA 度量 | **未外推**：本例固定 $v=I$；变成 $v=Pu$ 时须重查全部 $(P+F)^{-1}P$。$P=I/2$ 已使 $x=-2b$ 的完整纤维含 $0,\pm\mathbf1/\sqrt2$，正定不保证单值或同窗。 |
| 模证书失效的参数 | **不能硬用**：偶数周期或系数分母含3时 determinant／integrality 门要另核；证书失败不等于实际退化。 |
| 解点 noncalm／精确全局轨道 | **不提供**：所有固定点 smooth；保留 C241/C242 的不同角色。 |
| 额外信息的独占性 | **不通过独占声称**：经典度给同一推断；当前只认证具体模型、低成本条件与统一接口。 |

模型的自然程度、数学有效性、示例作用与创新性分开判断：原生任务明确；完整证书有效；第四章可以展示“解16个稳定点，知至少15个未求的不稳定点”；与指定梯度／全图 Minty 入口有真实不同；世界首次、最优计算复杂度和解点 noncalm 均没有认证。
