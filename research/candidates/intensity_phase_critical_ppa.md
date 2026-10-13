# 单强度相位拟合的临界普通 PPA：完整近端、圆管真 RLEB 与补偿驻点

- **Status**：`candidate`。下面解析证明已完成，供独立复核；未登记新的 Claim，不修改 C252/C254 身份及主稿。
- **Scope**：原生单复数强度观测的普通 PPA；采用独立的大球指数入口。其反射映射不满足 C254 的全尺度次线性 Hölder 前件。
- **复算**：[代码与说明](../code/intensity_phase_critical_ppa/README.md)。有限复算与以下全称解析证明分开。

## 1. 原始问题与解释

对未知复数振幅 $z\in\mathbb C\cong\mathbb R^2$，一个已标定的强度观测 $b>0$ 给出 $b=|z_*|^2$。采用平方强度失配

\[
f_b(z)=\tfrac14(|z|^2-b)^2.
\]

这是标准强度最小二乘目标的单观测、单复变量特例，系数 $1/4$ 选为使实欧氏梯度写成下式。相位观测本身不辨识绝对相位，故所有拟合极小点自然形成圆，而不是从所需的圆反造目标。这里不声称恢复不可观测的绝对相位，也不把单观测玩具模型当作高维困难相位恢复应用。

Candès–Li–Soltanolkotabi 的作者稿 §2.1 Eq.(2.1) 使用平方强度失配；其算法 Eq.(2.2) 是 Wirtinger 梯度迭代，本页改为普通 PPA，不能把该文算法定理直接移植。来源：[arXiv:1407.1065v3，PDF 第3页](https://arxiv.org/pdf/1407.1065)。

## 2. 完整原关系、核、步长与零集

所有梯度均按 $\mathbb R^2$ 的实欧氏结构取。设

\[
F_b(z)=\nabla f_b(z)=(|z|^2-b)z,\qquad v=\operatorname{Id},
\qquad\lambda>0,\quad\alpha=\lambda b.
\]

其完整零集与极小点集分别为

\[
S=F_b^{-1}(0)=\{0\}\cup M_b,\qquad
M_b=\{z:|z|=\sqrt b\}=\operatorname{argmin}f_b.
\]

目标零簇选 $M=M_b$，始终保留原关系完整真残差

\[
r_{F_b}(y)=\|F_b(y)\|=\bigl||y|^2-b\bigr||y|.
\]

## 3. 完整更新公式与临界步长

完整预解式方程为

\[
x=(1-\alpha+\lambda|y|^2)y. \tag{IP1}
\]

当 $0<\alpha<1$ 时，近端目标

\[
\lambda f_b(y)+\tfrac12\|y-x\|^2
=\tfrac\lambda4|y|^4+\tfrac{1-\alpha}{2}|y|^2-\langle x,y\rangle
 +\tfrac{\lambda b^2}{4}+\tfrac{|x|^2}{2}
\]

是强凸、强制函数。IP1 对每个输入恰有一个解，完整 stationary resolvent 与完整 global-min prox 相同。其方向保持，输出半径是严格增满射 $s\mapsto(1-\alpha)s+\lambda s^3$ 的逆。

临界步长 $\alpha=1$，即 $\lambda=1/b$，近端目标成为严格凸强制四次式，仍然全域恰有一个驻点和极小点。因此

\[
T(x)=J_{\lambda F_b}(x)=
\begin{cases}
b^{1/3}|x|^{-2/3}x,&x\ne0,\\
0,&x=0.
\end{cases} \tag{IP2}
\]

这是完整关系，不是径向方程的一条所选支。其唯一非 Lipschitz 输入是原点；在拟合圆附近它是光滑的。特别地，该例不提供极小点处的非 calm 机制。

## 4. 全输入覆盖、所有输出与越临界失效

对 $0<\alpha\le1$，上述强制严格凸计算同时证明全空间输入覆盖、输出存在、唯一及全纤维排他；所有输出均已列尽。弱凸性的独立核验为

\[
\nabla^2f_b(y)=2yy^\mathsf T+(|y|^2-b)I\succeq-bI.
\]

当 $\alpha>1$，完整 stationary resolvent 在零输入已经多值：

\[
J_{\lambda F_b}(0)=\{0\}\cup
\{y:|y|=\sqrt{b-1/\lambda}\}. \tag{IP3}
\]

完整 global-min prox 在该输入仅取 IP3 中的圆；它仍然多值。因此 C254 所需的全域连续单值完整 $T$ 失效，选择某一方向不能恢复同一完整算法。不能混淆 IP3 的驻点纤维与 global-min 纤维。

更强的局部失败发生于 $\alpha\ge4$：取拟合零点 $p\in M_b$，写 $y=qp$，完整方程化为

\[
\alpha q^3+(1-\alpha)q-1
=(q-1)(\alpha q^2+\alpha q+1)=0.
\]

除 $q=1$ 外，$\alpha=4$ 有 $q=-1/2$，$\alpha>4$ 有两个负根。因此完整 stationary 关系甚至从目标零输入 $p$ 跳到远输出，直接破坏零锚吸收。$1<\alpha<4$ 不据此判圆管动力失败；它已经不能用本页的单值全局指数入口。

## 5. 紧目标圆与隔离域

以下固定 $b=\lambda=1$，以避免缩放常数掩盖同窗认证。目标 $M=S^1$ 是紧 $C^\infty$ 无边界嵌入流形，$\chi(M)=0$。选

\[
U=\{x:3/4<|x|<5/4\},\qquad R=1/16,
\qquad U_R=\{x:||x|-1|\le R\}.
\]

$U$ 中完整固定点仅有圆；补偿原点不在 $U$。对全部 $x\in U_R$，最近点唯一，$p=x/|x|$。设输入半径 $r=|x|$、输出半径 $s=r^{1/3}$，则 $y=sp$，且 $9/10<s<11/10$。输出定位先由完整公式认证，无预先留域假设。

## 6. 四项同窗真 RLEB 证书

取同一个完整允许关系 $\mathcal J=T$，并固定

\[
\gamma=1,\quad L=2/5,\quad\bar t=1,\quad
\psi(q)=\tfrac{100}{171}q\ (0\le q\le1),\quad\kappa=1/2.
\tag{IP4}
\]

**反射与同一最近锚。** 置 $u=s-1\in[-1/10,1/10](、)t=r-1$。由 $r=s^3$，

\[
t=u(3+3u+u^2),\qquad
2s-r-1=-u(1+3u+u^2).
\]

该窗内 $1+3u+u^2>0$，而 $3u^2+9u-1\le-7/100<0$，故

\[
\|2y-x-p\|
\le\tfrac25|t|=L\,d(x,M)^\gamma.
\tag{IP5}
\]

**完整真残差。** 对每一个实际输出，

\[
r_F(y)=s(s+1)|u|\ge\tfrac{171}{100}|u|,\qquad
d(y,M)=|u|\le\psi(r_F(y)). \tag{IP6}
\]

IP6 使用完整单值 $F$ 的精确范数，未用所选步代替真残差。它在全部输出成立，故尤其在 $r_F(y)\le\bar t$ 的评价窗内成立。

**评价窗与直接兼容。** 令 $B(t)=(t+Lt)/2=7t/10$，则

\[
B(R)/\lambda=7/160<1=\bar t,\qquad
\psi(B(t)/\lambda)=\tfrac{70}{171}t<\tfrac12t=\kappa t

\quad(0<t\le R). \tag{IP7}
\]

**位移可和及严格留域。** C02-v3 的同窗长度函数为

\[
\mathcal L(t)=\frac{(1+L)t}{2(1-\kappa)}=\tfrac75t.
\]

对每个 $x\in U_R$，$d=d(x,M)\le1/16$，

\[
\mathcal L(d)\le7/80<3/16
\le1/4-d=d(x,\mathbb R^2\setminus U). \tag{IP8}
\]

所以 [C02-v3](../canonical/true_residual_selection_rleb.md#trs-theorem) 对整 $U_R$ 内完整 PPA 统一适用：轨道无限延拓、留域、有限长度、趋向 $M$，并有 $d_k\le2^{-k}d_0$、总长至多 $7d_0/5$。同一对象亦是 [C249](../canonical/physical_rleb_gppa.md#prg-object) 的 $v=I,a(t)=t,\omega(t)=2t/5,h(t,q)=q$ 特例。

## 7. 全局增长与独立的大球指数入口

反射映射 $C=2T-I$ 在远处有

\[
C(re)= (2r^{1/3}-r)e,\qquad
\frac{\|C(re)-C(0)\|}{r^{\gamma_*}}\longrightarrow\infty
\quad(0<\gamma_*<1).
\tag{IP9}
\]

因此**本例不满足 C254 的全尺度反射 Hölder 前件**。$T$ 自身的立方根增长不能冒充 $C$ 的增长。

本例另有更直接的物理入口：$\|T(x)\|=\|x\|^{1/3}$。于是 $T(\overline B_2)\subset B_2$，并且对每个 $0\le a\le1$，边界上的 $x-aT(x)$ 不为零。固定点指数的同伦不变性将 $I-T$ 变为 $I$，给

\[
i(T,B_2)=1. \tag{IP10}
\]

这使用的是“完整连续 $T$+大球严格内向”的独立桥，未改变或声称直接套用 C254。所有固定点在 $\overline B_1$ 内，可由 IP2 的固定点半径方程核验。

圆管 $N_\delta$，$0<\delta\le R$，由 IP4–IP7 严格映入自身内部；它形变回缩到圆，$T|_M=I$，故局部指数为 $\chi(M)=0$。也可直接按平面环域计算：外边界 $I-T$ 正向径向，度为1；内边界 $I-T$ 反向径向，按逆时针参数的度仍为1；环域边界的相减给 $1-1=0$。

所用经典指数接口为 Benjamin–Gottlieb 作者原文 §2.1：localization、additivity、normalization、commutativity、homotopy invariance；PDF 第3–4页。[作者 PDF](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf)。圆管到环境指数可逐字复用 [C254 证明的换空间步骤](../canonical/rleb_kernel_topology_interfaces.md#rkt-local-index)，仅替换其全局增长环节。

## 8. 未发现零点：存在、指数、数量与位置

IP10 与圆管指数零，由可加性先推出管外完整固定点簇的总指数为 $1\ne0$，故额外驻点必存在。这一步不需要先解完整零点方程。

准确数量与位置则需要独立直接核验。原梯度方程

\[
(|z|^2-1)z=0
\]

给出完整额外簇恰为单点 $0$。在小圆 $|x|=\varepsilon<1$ 上，$I-T=(\varepsilon-\varepsilon^{1/3})x/\varepsilon$ 是反向径向映射，其平面度为 $+1$，与缺额吻合。此处 $T$ 在0不可微，不能套 $\operatorname{sign}\det(I-DT$0$)$；必须用边界度或上述径向同伦。

每个非零初值的半径有完整闭式 $r_k=r_0^{3^{-k}}$，方向恒定，因此趋向圆且从不命中0；只有初值0得到驻定中心轨道。有限迭代点云不能认证整个圆，圆的拓扑由原目标及圆管另行认证。准确数量“一点”和准确位置“0”不是指数自动给出的结论。

## 9. 与经典理论的准确关系

- $F$ 全局非单调，因其在0的 Hessian 为 $-I$。它不属于极大单调算子的经典 PPA；局部径向标量关系和弱凸近端仍有直接经典分析。
- 临界步 $\lambda=1$ 超出单靠“弱凸性使近端子问题强凸”的严格门 $\lambda<1$，但本例四次式的严格凸性直接恢复唯一完整 prox。Davis–Grimmer 作者稿 §3, PDF 第8页列近端子问题强凸常数 $\gamma^{-1}-\rho$，仅引用这个前件事实。[arXiv:1707.03505](https://arxiv.org/pdf/1707.03505)。
- 完整 global-min prox 的比较点 $x$ 给 $f(y)+\|y-x\|^2/2\le f(x)$，最优性给 $\|\nabla f(y)\|=\|x-y\|$。原目标是连续、强制、半代数多项式；轨道由下降有界，故 ABS 的 H1/H2/H3 与 KL 都有正面入口。Attouch–Bolte–Svaiter 2010-12-15 作者稿 §2.3, H1–H3 印页8、Theorem2.9 印页12：[作者 PDF](https://optimization-online.org/wp-content/uploads/2010/12/2864.pdf)。
- 更短的轨道证明直接来自 $r_k=r_0^{3^{-k}}$，总径向长度恰为 $|r_0-1|$（非零初值）。因此不得声称 RLEB 独占收敛或经典能量/KL 无法处理。
- 指数缺额属于经典固定点度及 Morse–Bott 几何。此例的作用是展示局部真 RLEB 认证如何接入未发现零点推断，及全局反射条件与实际大球条件的差别；不宣称新的相位恢复算法或第二种强创新机制。

## 10. 证明长度、隐藏条件与失效边界

主文所需证明约为四段：完整 quartic prox、圆管同窗元组、大球/圆管指数、原方程核验中心。参数攻击 IP3/IP9 可置例后备注。它比现行 C252 的分段目标更贴近标准强度失配，但需要一个独立大球指数桥，不能在保留原 C254 前件不变时直接替换为其应用。

承重条件已显式核验：实梯度约定、$b>0$、固定临界步、完整 stationary/global-min 身份、全部输入、全部输出、同一最近锚、完整真残差、评价窗、整窗兼容、严格预算、紧圆拓扑、球/管边界无固定点及非微分中心的指数。$b=0$ 无圆；越临界多值、全尺度反射增长和极小点非 calm 的诉求均不能从此例获得。全球优先性与实际设备参数未认证。

### 八轴筛选（0–3，评价不是证明）

| 自然性 | 完整近端可认证性 | 局部 RLEB 可认证性 | 全局指数入口 | 额外零点信息 | 证明简洁性 | 与已有理论真实差异 | 应用解释力 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 3 | 3 | 3（独立大球桥） | 1（原点本来显然；指数和位置范围另认证） | 3 | 1 | 2 |

总分19/24，按第四章实际信息增益评分；它是短结构对照，未认证困难相位恢复任务的收益。

### 交付检查范围

数学读者路线为“真实失配 → 完整原算法 → 同窗证书 → 全局入口 → 未发现点读出 → 经典正面与失败边界”。各段公式的对象一致；IP9 紧邻大球桥，IP8 保留有限前缀留域所需严格不等式，IP8/IP10 不凭数值升级全称证明。没有修改主稿、摘要、Claim 总账或 canonical 编号。
