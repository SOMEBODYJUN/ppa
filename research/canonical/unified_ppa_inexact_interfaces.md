# 统一 PPA 的可计算非精确接口：联合图证书、方向预算和物理提升

2026-10-14。规范证明，闭合单元为 derived-checked，已限定范围独立实际全文冷读，核心身份注册 C283/C284；末节开放义务保持 open。主稿、摘要和正文编号未改。本文不把通用固定点扰动估计、Caristi 型望远镜原理或已有投影论证重新命名为独立大贡献。真正需要保存的是：原始图结构如何给出可执行的误差预算；哪些预算控制完整接受关系；非单射及移动核的物理提升在哪一步产生、在哪一步失败。

依赖：[C275](../topics/inexact_ppa/real_graph_stopping.md)、[C276](../topics/inexact_ppa/sharp_precision_frontier.md)、[C249/C250](../canonical/physical_rleb_gppa.md)、[C213](../canonical/gppa_inexact_modulus.md)、[GU3](../novelty/2026_10_14_submonotonicity/gauge_unification_review.md)。按仓库 `academic-writing-skills` 的证明审查模式冻结对象、全图量词、零距离、远端输出和评价窗。以下新公式都是本页直接计算，不是外部文献事实或首创认证。

## 1. 冻结对象与第一次尝试的确切失败

除单独声明核的章节外，$X=\mathbb R^n$，$F:X\rightrightarrows X$ 固定，$\lambda>0$，**完整**零集 $S=F^{-1}(0)$ 非空闭，
\[
d(x)=d(x,S),\qquad r_F(y)=\inf_{w\in F(y)}\|w\|.
\tag{UI1}
\]
空纤维的下确界为 $+\infty$。固定明定图块 $\mathcal G\subset\operatorname{gph}F$，包含 $S\times\{0\}$；全图结论必须取 $\mathcal G=\operatorname{gph}F$。算法计算真实图见证 $(y,w)\in\mathcal G$ 及
\[
e=x-y-\lambda w,\quad E=\|e\|,\quad W=\|w\|.
\tag{UI2}
\]
每个停止政策的允许关系是**所有**满足该政策的图见证投影到 $y$ 后的集合，不选择最小范数值、连续支或有利精确根。始终只用 $r_F(y)\le W$；不能倒转。

**尝试 1：直接把精确距离收缩搬到 $x$。** 等式只给 $y\in J_{\lambda F}(x-e)$，不能把认证于 $x$ 的精确输出几何用在 $y$ 上。即使 $\|e\|\ll\lambda W$，非 Lipschitz 近端也不提供 $\|y-Jx\|=O(E)$。C276 已在完整图、全域 coverage 下给反例：固定相对残差可接受常法向距离、无穷切向漂移。把 C213 的外部输出误差卷积重写一次既不能解决这一错误，也没有形成新停止机制。

**尝试 2：回到候选图点并保留耦合。** 对同一个 $p\in S$ 写
\[
a=y-p,\quad b=\lambda w,\quad a+b=x-p-e.
\tag{UI3}
\]
图的零锚不等式必须认证于 $(y,w)$ 的完整候选域，而不只是旧精确输出集。将 $e$ 的方向或范数直接放进这一等式，才有可计算停止预算。下面分别闭合 RL、cohypomonotone、法向/切向和联合长度四种接口；它们共同使用 UI3，但没有用一个损失方向的标量模强行合并。

## 2. 可计算图剖面的通用接口及其有限含义

令 $z=y+\lambda w$。假设可计算描述量 $\xi=\xi(y,w)$ 给出已认证的集合 $D_\xi\subset[0,\infty)$ 和函数 $L_\xi:D_\xi\to[0,\infty)$，满足
\[
q:=d(y)\in D_\xi,\qquad d(z)\ge L_\xi(q).
\tag{UI4}
\]
这些是对同一原图的结构结论；不能把所需 $d(y)\le\kappa d(z)$ 直接当作“原始证书”。给定 $0<\kappa<1$，定义标量预算
\[
M_\kappa(\xi)=\inf_{q\in D_\xi}\{L_\xi(q)-q/\kappa\}.
\tag{UI5}
\]
若原始结构允许可认证地计算非负的 UI5，接受 $E\le M_\kappa(\xi)$ 便有
\[
d(x)\ge d(z)-E\ge L_\xi(d(y))-E\ge d(y)/\kappa.
\tag{UI6}
\]
这条短式本身只是**接口引理**：它不提供 coverage、物理长度、零输入驻定或内层终止，也不保证任意结构的 UI5 可计算。以下三个具体编译才承担这些义务。若 $S$ 未知，UI5 中用于分析的 $q$ 是离线消元变量；运行时不得查询 $d(x)$、$d(y)$ 或精确 $Jx$。

### 2.1 RL：准确恢复 C275，不重新计贡献

C275 的全候选零锚反射模给
\[
B(t)=(t+\omega(t))/2,\quad Q(u)=\inf\{t:u\le B(t)\},
\]
\[
D_\xi=[0,\psi(W)],\quad L_\xi(q)=Q(\lambda W),
\quad M_\kappa=Q(\lambda W)-\psi(W)/\kappa.
\tag{UI7}
\]
再合取 $E\le\theta Q(\lambda W)$、残差帽和 C275 的同窗条件，就是 C275 原停止规则。该独立预算负责将 $W,E$ 控制为输入距离的消失模，物理步长 $\|x-y\|\le\lambda W+E$ 随之可和。故这部分是逐条件原样恢复，不是新定理。

<a id="uic-cohypo"></a>
### 2.2 co-hypomonotone：保留能量中的残差项

**UI-COH-v1。** 固定 $\rho\ge0$，设 $\lambda>2\rho$，记
\[
c=\lambda(\lambda-2\rho)>0.
\tag{UI8}
\]
假设对 $\mathcal G$ 的全部点和全部 $p\in S$ 有
\[
\langle y-p,w\rangle\ge-\rho\|w\|^2.
\tag{UI9}
\]
设 $U$ 开，$R,\bar W,K>0$。在所有候选图输出满足 $r_F(y)\le\bar W$ 时有真 EB $d(y)\le K r_F(y)$。每个 $x\in U_R=\{x\in U:d(x)\le R\}$ 有精确图种子。要求
\[
R\le\sqrt c\,\bar W,\qquad
0\le\sigma<\sqrt{K^2+c}-K.
\tag{UI10}
\]
完整停止规则为
\[
W\le\bar W,\qquad E\le\sigma W.
\tag{UI11}
\]
则所有接受输出满足
\[
d(y)\le\kappa d(x),\quad
\|y-x\|\le C d(x),\quad
\kappa=\frac K{\sqrt{K^2+c}-\sigma}<1,\quad
C=\frac{\lambda+\sigma}{\sqrt c-\sigma}.
\tag{UI12}
\]
在严格预算 $Cd(x^0)/(1-\kappa)<d(x^0,X\setminus U)$ 下，全部允许轨道无限延拓、留域、有限长并趋于 $S\cap U$。

**证明。** UI9 给每个零锚
\[
\|z-p\|^2=\|y-p\|^2+2\lambda\langle y-p,w\rangle+
\lambda^2W^2\ge\|y-p\|^2+cW^2.
\]
取下确界得到 $d(z)\ge\sqrt{q^2+cW^2}$。因帽先使 $r_F(y)\le W\le\bar W$，真 EB 才给 $q\le KW$。于是 UI4 的精确保留为
\[
D_\xi=[0,KW],\quad L_\xi(q)=\sqrt{q^2+cW^2}.
\]
函数 $q\mapsto\sqrt{q^2+cW^2}-q/\kappa$ 在 $\kappa<1$ 时递减，所以
\[
M_\kappa=(\sqrt{K^2+c}-K/\kappa)W=\sigma W.
\tag{UI13}
\]
UI6 给收缩；同时 $d(x)\ge d(z)-E\ge(\sqrt c-\sigma)W$，再用 UI2 得步界。UI10 蕴含 $\sigma<\sqrt c$，分母为正。对精确种子，$\sqrt cW\le d(x)\le R$，所以它自动通过帽及停止政策；不从 EB 推 coverage。若 $d(x)=0$，前式迫使 $W=E=0$，而 UI2 给 $y=x$。

逐有限前缀有 $d(x^k)\le\kappa^k d_0$ 及 $\sum_{j=0}^{k}\|x^{j+1}-x^j\|\le Cd_0/(1-\kappa)$。严格预算使下一点留在 $U_R$，因此下一次种子覆盖合法；可和长度和 $S$ 闭给结论。这里没有将未知 $q$ 留在运行时测试中。□

**内层有限接受。** 若 $\sigma>0$，$R<\sqrt c\bar W$，真实图内层 $(y_j,w_j)$ 收敛到某个精确种子，则 $x\notin S$ 蕴含 $W_*>0$。最终 $W_j\ge W_*/2$ 且帽严格成立，$E_j\to0$ 使 UI11 有限步通过。$x\in S$ 时政策强制精确驻定，不能据此宣称浮点零检测或任意逼近序列有限终止。

**同算法 diagonal 优势仍在。** 对 $F=\operatorname{diag}(-1,1/100)$、$S=\{0\}$、$\lambda=3$，完整图取 $\rho=1,K=100,c=3$。所有
\[
0<\sigma<\sqrt{10003}-100\approx0.01499887517
\tag{UI14}
\]
都提供正的真实图误差预算；无须修改 $F$、核、$\lambda$ 或物理范数。此处精确收缩估计较实际 $100/103$ 保守，但原物理 C249/C250 的合法标量反射证书已经失败的同一算子仍被覆盖。不是通过换坐标抹掉该差异。UI14 是上述类证书的充分系数，未证明是这个 diagonal 算子完整误差政策的锐阈值。

**边界。** 在 $\lambda=2\rho$ 时 $c=0$，UI13 不留下正预算；这准确反映本证明缺乏严格余量，不证明所有临界算子发散。UI11 全图版本若只有局部 UI9 或只在旧精确输出上有 EB，必须另作候选域/信任域认证，不能删去这一门。

**类级临界常数攻击：有实际不收敛端点。** 对 $K\ge\rho\ge0,K>0$，令 $J$ 是平面九十度旋转，$\beta=\sqrt{K^2-\rho^2}$，
\[
A=-\rho I+\beta J,\quad F=A^{-1},\quad S=\{0\},\quad
D=\sqrt{K^2+\lambda(\lambda-2\rho)},\quad\sigma_*=D-K.
\tag{UI14a}
\]
$A$ 可逆，完整单值图可参数化为 $(y,w)=(Aw,w)$。有 $\|y\|=K\|w\|$、$\langle y,w\rangle=-\rho\|w\|^2$，真 EB 与 co-hypo 常数同时取等号；$A+\lambda I$ 可逆，所以完整 coverage 全域。对每步令
\[
z=(A+\lambda I)w,\quad e=-\frac{\sigma_*}{D}z,\quad
x=z+e=\frac K D z.
\tag{UI14b}
\]
则 $\|e\|=\sigma_*\|w\|$，而实际迭代
\[
y=\frac D K A(A+\lambda I)^{-1}x
\tag{UI14c}
\]
是正交变换，因为 $A^*A=K^2I$、$(A+\lambda I)^*(A+\lambda I)=D^2I$ 且两矩阵可交换。它不是恒等：若 $\beta>0$，两个复标量的相角不同；若 $\beta=0$，则 $K=\rho>0,\lambda>2\rho$，UI14c 正是 $-I$。每条非零轨道因此范数恒定、步长恒定正值，不收敛且无限长。任意给定正残差帽及 $R$ 可通过缩放初始点满足，且每步 $W$ 不变。所有 $\sigma\ge\sigma_*$ 都接受这条端点轨道。

故对 $K\ge\rho$ 的这类已声明常数，UI10 的严格系数不能整体扩大；这是同一停止政策的完整图类级锐性，不授予单个 diagonal 算子的锐性，也不声称相对误差 PPA 的公开首创。

## 3. 保留方向的普通 PPA：GU3 的完整非精确关系

固定 $0<\gamma<1$、$\lambda=1$，完整算子
\[
F(u,s)=\{(0,s),(-2^\gamma|s|^\gamma,s)\},\quad
S=\mathbb R\times\{0\},\quad r_F(u,s)=|s|.
\tag{UI15}
\]
取 $0\le\sigma<1$、$\eta\ge0$、$\alpha>0$。对每个真实图见证 $y=(u,s),w=(w_T,s)$ 计算 $e=x-y-w$，接受且仅接受
\[
|e_N|\le\sigma|w_N|=\sigma|s|,\qquad
|e_T|\le\eta|w_N|^\alpha=\eta|s|^\alpha.
\tag{UI16}
\]
这是方向可计算政策，不调用到 $S$ 的距离；此例的 $r_F$ 恰可显式求得，仍未把任意选支 $\|w\|$ 认成真残差。

**UI-GU3-v1。** 每个输入都有精确种子通过 UI16。对全部接受输出，
\[
d(y)=|s|\le\kappa|x_N|,\quad\kappa=(2-\sigma)^{-1}<1,
\tag{UI17}
\]
\[
\|x-y\|\le (1+\sigma)\kappa d(x)+
2^\gamma\kappa^\gamma d(x)^\gamma+
\eta\kappa^\alpha d(x)^\alpha.
\tag{UI18}
\]
故全部轨道全局有限长且收敛到完整 $S$。三个几何级数分别给尾预算，零输入全部驻定。

**证明。** $x_N=2s+e_N$ 给 UI17；法向物理步 $|x_N-s|\le(1+\sigma)|s|$，切向物理步至多 $2^\gamma|s|^\gamma+\eta|s|^\alpha$，得 UI18。各幂为正，沿 UI17 逐项可和。$x_N=0$ 迫使 $s=e_N=0$，图上两支均有 $w_T=0$，第二预算再给 $e_T=0,y=x$。精确种子为 GU3 已显式列出的完整两输出，它们缺陷为零，故全域 coverage 是已证事实。□

**内层终止的精确范围。** 非零法向输入收敛到任一精确图种子时，$|s_*|=|x_N|/2>0$。若 $\sigma>0,\eta>0$，两个预算都最终有固定正下界，因此任意真实图内层逼近有限接受。若取 $\eta=0$ 或 $\sigma=0$，相应方向必须精确求解；不能再对任意逼近序列断言有限接受。

**三次攻击。**

1. 临界 $\sigma=1$，取任意 $s>0$，漂移支 $w=(-2^\gamma s^\gamma,s)$、$e=(0,-s)$。输入及后继的法向坐标都是 $s$，切向每步增加 $2^\gamma s^\gamma$；这是真实完整图的发散轨道，且通过任意 $\eta\ge0$ 的切向预算。故 $\sigma<1$ 对这个完整政策是锐的。
2. 若删掉切向预算，输入在 $S$ 时可取 $w=0$、$e_T=-1$，每步沿 $S$ 漂移。法向收缩和真 EB 都不排除此例。若误把 $|s|^\alpha$ 的零点改为常数，也同样失败。
3. 若将 UI16 改为单个 $E\le\tau\|w\|$，上面的恒法向政策在 $s\downarrow0$ 时有 $E/\|w\|\to0$，任意 $\tau>0$ 最终接受。方向政策因此确实保留了标量残差精度丢失的信息；不是重选一个 Hölder 指数而已。UI16 是全域门，不需要额外帽；对一般仅局部图结构，不能据此删除帽。

### 3.1 同一规则的原算子法向结构版本

GU3 不必作为孤立代入。设完整 $S=p_0+T$ 为仿射集，$N$、$P_T$ 是法向和切向正交投影，$n(y)=N(y-p_0)$。设完整原图上，给定 $m>0,0<M<\infty$ 和有限非减 $h:[0,\infty)\to[0,\infty)$、$h(0)=0$，有
\[
\langle n(y),Nw\rangle\ge m\|n(y)\|^2,\quad
\|Nw\|\le M\|n(y)\|,\quad
\|P_Tw\|\le h(\|n(y)\|).
\tag{UI18a}
\]
这是原图可检查的方向结构，不是预设输出收缩。第一式对完整纤维取下确界给真正的 $r_F(y)\ge m d(y)$；只对选支认证则不能推出这个完整真 EB。算法仍以同一 $F$ 和任意 $\lambda>0$ 运行，接受
\[
\|Ne\|\le\sigma\|Nw\|,\qquad
\|P_Te\|\le\eta\|Nw\|^\alpha,
\quad 0\le\sigma,\quad\sigma M<\lambda m,\quad\eta\ge0,\ \alpha>0.
\tag{UI18b}
\]
与 $n(y)$ 作内积，$n(x)=n(y)+\lambda Nw+Ne$ 给
\[
d(x)d(y)\ge(1+\lambda m-\sigma M)d(y)^2.
\]
因此 $d(y)\le\kappa d(x)$，$\kappa=(1+\lambda m-\sigma M)^{-1}<1$；物理步不超过
\[
H(d(x))=(1+\kappa)d(x)+\lambda h(\kappa d(x))+
\eta M^\alpha\kappa^\alpha d(x)^\alpha.
\tag{UI18c}
\]
在输入管上另证精确种子覆盖，要求 $\sum_j H(\kappa^jR)<\infty$，加同一个严格有限前缀预算，即得全部输出有限长度。$h$ 的 Dini 条件是充分门。零输入先给 $d(y)=0$，UI18a 强制 $w=0$，UI18b 再给 $e=0,y=x$。若 $\sigma,\eta>0$，非解输入的任何精确种子必有 $\|Nw_*\|>0$；否则 UI18a 使 $y_*\in S,w_*=0,x=y_*$。因此趋于该真实图种子的内层最终有限通过两项预算。

这里 $N$ 是已知结构投影；运行时仅计算 $Ne,Nw,P_Te$，不计算最近零锚或到 $S$ 的距离。GU3 取 $m=M=1,h(t)=2^\gamma t^\gamma,\lambda=1$，精确恢复 UI16–17 的门。UI18c 的长度系数比 UI18 更保守；不能据此声称两套步长常数也逐项相同。

## 4. 无几何率时仍保持联合长度：两支原图的非精确版本

与联合父接口协调，取完整 $F:\mathbb R\rightrightarrows\mathbb R$，
\[
F(y)=\{y,y^3\},\quad\lambda=1,\quad S=\{0\},\quad
r_F(y)=\min\{|y|,|y|^3\}.
\tag{UI19}
\]
所有 $x$ 的两个精确根分别由 $x=2y$、$x=y+y^3$ 给出；第二个等式左侧严格递增满射，故完整 coverage。接受全部真实图对满足
\[
|x-y-w|\le\sigma|w|,\qquad 0\le\sigma<1.
\tag{UI20}
\]
若 $y\ne0$，$w$ 与 $y$ 同号，且 $w+e$ 与 $w$ 同号。因此 $x,y$ 同号且 $|y|<|x|$，并有**联合**身份
\[
|x-y|=|x|-|y|.
\tag{UI21}
\]
零输入只能输出自身。对任意完整接受轨道，$|x^k|$ 单调降到某个 $\ell\ge0$，而
\[
|x^k-x^{k+1}|\ge(1-\sigma)
\min\{|x^{k+1}|,|x^{k+1}|^3\}.
\]
若 $\ell>0$，右侧最终有固定正下界，和 UI21 的望远镜有界性矛盾。因此 $x^k\to0$，总物理长度恰为 $|x^0|$。这保留分支之间的距离/步长相关；不需要把慢支收缩和快支步长独立取最坏值后再求级数。$\sigma>0,x\ne0$ 时，趋于任一精确真实图种子的内层序列有限接受。$\sigma=1$ 可取 $e=-w,y=x\ne0$，因而严格常数不可删。

该例只是联合长度机制的可实施非精确扩展；没有将一维单调性或望远镜和授予独立普适贡献。

<a id="uic-projections"></a>
## 5. 非单射 GPPA：第一轮自动提升失败，第二轮图诱导提升闭合

GPPA 缺陷改为
\[
e=v(x)-v(y)-\lambda w,
\quad w\in F(y).
\tag{UI22}
\]
**失败版本 UI-G-AUTO。** 仅从核误差收缩、真 EB、完整 coverage 推所有物理轨道有限长，是假的。C249 的 $v(t,s)=(t,0),F=v,S=\{0\}\times\mathbb R$ 已给完整纤维 $\{(t/2,q):q\in\mathbb R\}$；即使 $e=0$，核零输入也允许任意物理漂移。核误差为零不能恢复丢失方向，停止规则再精确也不能修复它。

以下第二轮不额外假定抽象物理 $h$，而从同一真实图方程直接计算物理提升。取
\[
F=I\text{ on }\mathbb R^n,\quad S=\{0\},\quad r_F(y)=\|y\|,
\quad v(x)=Px,
\tag{UI23}
\]
其中 $P$ 是任意正交投影，允许秩亏和零投影。对 $\lambda>0$，全部接受输出由
\[
e=Px-Py-\lambda y,\qquad \|e\|\le\sigma\lambda\|y\|
\tag{UI24}
\]
定义。图见证唯一是 $w=y$，真实残差恰为其范数；完整关系和全部误差方向均被保留。

### 5.1 固定秩亏核：全部 $0\le\sigma<1$ 都物理有限长

置 $a=1+\lambda$，$t=\|Px\|$、$u=Py$、$z=(I-P)y$。正交分解精确给
\[
\|Px-au\|^2+\lambda^2\|z\|^2
\le\sigma^2\lambda^2(\|u\|^2+\|z\|^2).
\tag{UI25}
\]
从而
\[
\|Py\|\le A_\sigma\|Px\|,\quad
A_\sigma=(1+\lambda-\sigma\lambda)^{-1}<1,
\tag{UI26}
\]
\[
\|(I-P)y\|\le B_\sigma\|Px\|,\quad
B_\sigma=\frac{\sigma}{\sqrt{(1-\sigma^2)((1+\lambda)^2-\sigma^2\lambda^2)}}.
\tag{UI27}
\]
**UI26 证明：** UI25 删除非负的 $(1-\sigma^2)\lambda^2\|z\|^2$ 得 $\|Px-au\|\le\sigma\lambda\|u\|$，反三角不等式给 $t\ge(a-\sigma\lambda)\|u\|$。

**UI27 证明：** 将右侧剩余项最大化，
\[
\sigma^2\lambda^2\|u\|^2-\|Px-au\|^2
\le\frac{\sigma^2\lambda^2}{a^2-\sigma^2\lambda^2}\,t^2.
\]
此为完成平方；代回 UI25 即得。令 $D_\sigma=\sqrt{A_\sigma^2+B_\sigma^2}$。对每条完整接受轨道，$k\ge1$ 有
\[
\|x^k\|\le D_\sigma A_\sigma^{k-1}\|Px^0\|.
\tag{UI28}
\]
于是点趋零，且 $\sum_k\|x^{k+1}-x^k\|\le\|x^0\|+2D_\sigma\|Px^0\|/(1-A_\sigma)$。物理提升来自 UI25 的完整图耦合，而不是核的逆映射；$P$ 不必单射。

每个输入有完整精确种子 $y_*=Px/a$，故 coverage 全域。$\sigma=1$ 时，任何 $x,y\in\ker P$ 都满足 $e=-\lambda y$ 和 UI24；核维数正时从 $0\in S$ 可以任意逃逸。这是锐的全输出收敛阈值，且零纤维攻击没有被 EB 遮住。

<a id="uic-moving"></a>
### 5.2 随迭代移动的投影核：锐的统一物理门

现在 $P_k$ 可以是任意依赖历史的正交投影；原 $F=I,S=\{0\}$ 和物理范数固定。精确或非精确图条件在每一步取 $P=P_k$。不能把 UI26 跨步迭代，因为下一步看的是 $P_{k+1}x^{k+1}$。但是 UI25 仍有如下**锐的一步全物理**估计。

对 $0\le\sigma<1$，定义
\[
L_\sigma=\begin{cases}
1+\lambda-\sigma\lambda,&0\le\sigma\le\lambda/(1+\lambda),\\
\sqrt{(1+2\lambda)(1-\sigma^2)},&\lambda/(1+\lambda)\le\sigma<1.
\end{cases}
\tag{UI29}
\]
全部接受输出满足 $\|y\|\le\|Px\|/L_\sigma\le\|x\|/L_\sigma$。因此
\[
\boxed{\quad\sigma<\sigma_{\mathrm{move}}:=\sqrt{\frac{2\lambda}{1+2\lambda}}\quad}
\tag{UI30}
\]
时，任意移动投影的全部接受轨道都有统一物理收缩 $\kappa=1/L_\sigma<1$ 及有限长度上界 $(1+\kappa)\|x^0\|/(1-\kappa)$。

**UI29 证明。** $y=0$ 平凡。否则写 $q=\|y\|$、$r=\|Py\|/q\in[0,1]$。UI25 要求 $r^2\ge1-\sigma^2$，并由反三角不等式给
\[
\frac{\|Px\|}{q}\ge (1+\lambda)r-
\lambda\sqrt{r^2-(1-\sigma^2)}.
\tag{UI31}
\]
右侧在 $r\in[\sqrt{1-\sigma^2},1]$ 上最小化。导数为
$1+\lambda-\lambda r/\sqrt{r^2-(1-\sigma^2)}$，二阶导数非负。若驻点落在区间内，其平方为 $r^2=(1+\lambda)^2(1-\sigma^2)/(1+2\lambda)$，给第二分支；否则最小值在 $r=1$，给第一分支。驻点在区间内恰当 $\sigma\ge\lambda/(1+\lambda)$，两个值在边界吻合。当 $n\ge2$ 且 $0<\operatorname{rank}P<n$ 时，方向共线和相应核分量同时实现这些下界，所以这是该混合秩类完整关系的锐一步系数。对任意 $n,P$ 它都是有效上界；第二分支不声称在 $P=0$、$P=I$ 或一维类达到。UI30 等价于 $L_\sigma>1$。□

**临界全输出反例，不只是估计失败。** 在 $\mathbb R^2$ 取单位初值 $x^0$，令
\[
\cos\vartheta=\frac{1+\lambda}{1+2\lambda}\in(0,1),\quad
x^{k+1}=R_\vartheta x^k,\quad
P_k=\text{投影到 }\operatorname{span}\{x^k\}.
\tag{UI32}
\]
各点范数恒为 1、相邻位移恒为 $2\sin(\vartheta/2)>0$。见证 $w=x^{k+1}$，且直接正交分解给
\[
\|P_kx^k-P_kx^{k+1}-\lambda x^{k+1}\|^2
=\lambda^2\frac{2\lambda}{1+2\lambda}.
\tag{UI33}
\]
所以 $\sigma=\sigma_{\mathrm{move}}$ 及任何更大值都接受整条不收敛、无限长轨道。原 $F$、完整 $S$、真残差和全域种子覆盖完全不变，输出也没有远端遗漏。对任意初始半径作同样缩放，反例任意接近零。因此 UI30 是 $n\ge2$ 且允许任意秩一移动投影这一整个类的锐门；一维投影只有 $0,I$，其完整关系在所有 $\sigma<1$ 下仍物理收缩，不属于这个锐性断言。固定核的 $\sigma<1$ 优势不能不付代价地推广到任意移动核。

### 5.3 内层有限接受暴露了一个不可删除的新门

对 UI24，若 $\sigma>0$ 且 $Px\ne0$，则精确种子 $y_*=Px/a\ne0$，任意真实图内层 $y_j\to y_*$ 最终有限接受。如果 $Px=0$，即使 $x\notin S$，UI25 在 $\sigma<1$ 下也强制唯一接受输出 $y=0$。任意始终非零的序列 $y_j\to0$ 永远不被接受。

这反驳“非零物理输入 $x\notin S$ 自动保证 GPPA 内层有限接受”的版本：非单射核可以把非解输入映到解核值。该模型有可检查的修复：测试 $Px=0$ 时直接返回已知图对 $(0,0)$，否则使用上述逼近内层。因此模型的全输入内层实现是完整的；对一般 $F,v$，不能假设存在同样的已知零图对。若没有精确零输出证书或另一个明确终止机制，只能保留非零见证条件，不能把“接受关系非空”写成“任意内层方法有限停止”。

<a id="uic-moving-spd"></a>
### 5.4 强单调原算子也不能免除移动核条件：零误差指数发散

UI23–33 固定 $F=I$，不能推广为“强单调 $F$ 配任意移动半正定核都安全”，甚至把核加强为一致正定也不成立。以下完整反例保留同一物理范数、强单调原 $F$、完整 coverage、唯一输出及零吸收，误差严格为零。

在平面上仍令 $J$ 为九十度旋转，取
\[
A=I+3J,\quad F(y)=Ay,\quad S=\{0\},\quad
r_F(y)=\sqrt{10}\|y\|,\quad\lambda=1/10.
\tag{UI33a}
\]
$\langle Ay-Az,y-z\rangle=\|y-z\|^2$，故强单调系数为 1，真线性 EB 常数 $1/\sqrt{10}$ 全域成立。

**移动秩一核。** 每个非零 $x^k$ 处令 $P_k$ 投影到 $\operatorname{span}\{x^k\}$。在正交基 $(x^k/\|x^k\|,Jx^k/\|x^k\|)$ 中，完整精确方程是
\[
(P_k+\lambda A)y=P_kx^k,\qquad
P_k+\lambda A=\begin{pmatrix}11/10&-3/10\\3/10&1/10\end{pmatrix}.
\]
矩阵行列式为 $1/5>0$，全部输入唯一覆盖；实际更新
\[
x^{k+1}=(\tfrac12 I-\tfrac32J)x^k,\qquad
\|x^{k+1}\|=\frac{\sqrt{10}}2\|x^k\|>\|x^k\|.
\tag{UI33b}
\]
任意非零初值指数逃离零点。每个固定秩一 $P$ 的完整线性步矩阵在相应基中为 $\left(\begin{smallmatrix}1/2&0\\-3/2&0\end{smallmatrix}\right)$，特征值为 $1/2,0$，所以每个固定核单独稳定；变动核才破坏收敛。

**移动一致正定核。** 令 $M_k$ 在上述当前点基中为 $\operatorname{diag}(1,1/10)$，定义全域线性核 $v_k(z)=M_kz$。统一有
\[
\tfrac1{10}I\preceq M_k\preceq I.
\tag{UI33c}
\]
完整精确步 $M_k(x^k-y)=\lambda Ay$ 的矩阵为
\[
(M_k+\lambda A)^{-1}M_k
=\frac1{31}\begin{pmatrix}20&3\\-30&11\end{pmatrix}.
\tag{UI33d}
\]
因为当前 $x^k$ 沿该基第一轴，每步仍有
\[
x^{k+1}=\frac{20I-30J}{31}x^k,\qquad
\|x^{k+1}\|=\frac{\sqrt{1300}}{31}\|x^k\|>\|x^k\|.
\tag{UI33e}
\]
矩阵迹为 1，行列式为 $10/31$，判别式 $1-40/31<0$，故每个**固定** $M$ 的两个特征值模均为 $\sqrt{10/31}<1$。自适应旋转谱不变的核却产生 UI33e 的指数发散。由于 $A$ 与所有平面旋转可交换，这些在当前基中的公式确实是同一个原 $F$ 的物理轨道，并未每步替换算子。

零输入可任取上述核方向，完整方程仍唯一输出零；所有非零输入也完整唯一覆盖，且没有远端分支或选支问题。故“一致 SPD 界 + 强单调 $F$ + 精确步就足够”已经被否定，不能继续列成待证猜想。一般移动核接口必须额外控制跨步核变化或给能直接推出共同物理耗散的原图条件；每步固定核各自收敛与一致谱界不够。

<a id="uic-membership"></a>
## 6. 近似图成员资格：有证书的扰动可闭合，裸距离说法不够

先给准确的同输出点版本。内层返回 $y,\widetilde w,\delta$，$\delta\ge0$，附带**可检查证明**
\[
\mathcal G_y\cap\overline B(\widetilde w,\delta)\ne\varnothing,\qquad\mathcal G_y:=\{w:(y,w)\in\mathcal G\}.
\tag{UI34}
\]
全图版本的 $\mathcal G_y$ 正是 $F(y)$；图块版本必须认证见证属于同一 $\mathcal G$，不能只在完整 $F(y)$ 中存在。残差仍评价完整 $F$。这不是假定求得真实残差；图可以多值，见证也无须是最小范数。证书必须来自原图的可核结构，例如有限显式分支中给出一个分支编号和受保证计算误差界。仅报告“近似属于图”或求解器残差小，不等于 UI34。

计算
\[
\widetilde e=x-y-\lambda\widetilde w,\quad
E_+=\|\widetilde e\|+\lambda\delta,\quad
W_-=(\|\widetilde w\|-\delta)_+,\quad
W_+=\|\widetilde w\|+\delta.
\tag{UI35}
\]
任意 UI34 见证满足 $W_-\le\|w\|\le W_+$、$E\le E_+$。因此 UI-COH 可以实现为
\[
W_+\le\bar W,\qquad E_+\le\sigma W_-;
\tag{UI36}
\]
一旦通过，输出 $y$ 就属于原 UI11 允许关系，前述全部结论逐项保留。UI19–20 也可用同样标量保守测试。GPPA 中只需把 $\widetilde e$ 改为 $v(x)-v(y)-\lambda\widetilde w$；物理提升仍须先独立认证，UI34 不会产生它。

C275 的可计算保守版本为
\[
\lambda W_+\le\bar u,\qquad
E_+\le\min\{\theta Q(\lambda W_-),
Q(\lambda W_-)-\psi(W_+)/\kappa\}.
\tag{UI37}
\]
因为 $Q,\psi$ 非减，它蕴含每一个 UI34 见证的原停止规则。若内层趋于严格帽内的非零精确种子，$\delta_j\to0$，缺陷趋零，UI36 在 $\sigma>0$ 时有限通过。

UI37 的有限接受也不需要 $\psi$ 在正点连续。理由是 $B(t+h)\ge B(t)+h/2$，故其广义逆 $Q$ 在所用有限区间满足 $|Q(u)-Q(v)|\le2|u-v|$。严格证明可取实现 $u\le B(t)$ 的近极小 $t$，以 $t+2(v-u)$ 为 $v$ 的候选；若超过右端点，则直接用 $Q(v)\le\rho$，再令近极小误差趋零。由 C275 的同窗兼容 $\psi(W_+)\le\kappa_0Q(\lambda W_+)$，UI37 的第二预算趋于至少 $(1-\kappa_0/\kappa)Q(\lambda W_*)>0$；第一预算同样正。故误差最终通过。

若证书只保证某个邻近点 $(y_*,w_*)\in\mathcal G$，且 $\|y-y_*\|\le\delta_y,\|\widetilde w-w_*\|\le\delta_w$，则原输出 $y$ 未必是原图点，不能声称已满足 UI2。普通 PPA 的剖面接口可保守修复：继承 UI-COH 的全部候选图前件，另要求 $W_+\le\bar W$，并独立认证该允许关系的种子覆盖。令 $E_+=\|\widetilde e\|+\delta_y+\lambda\delta_w$，以 $\delta_w$ 定义 $W_\pm$，在 UI13 预算中要求
\[
E_++\delta_y/\kappa\le(\sqrt{K^2+c}-K/\kappa)W_-.
\tag{UI38}
\]
对见证 $q_*=d(y_*)$，有 $d(x)\ge\sqrt{q_*^2+cW_*^2}-E_+$ 及 $d(y)\le q_*+\delta_y$，与 UI38 合并给 $d(y)\le\kappa d(x)$。长度也由同一预算控制：记 $\sigma=\sqrt{K^2+c}-K/\kappa\in[0,\sqrt c)$，因 $W_-\le W_*$ 且 $\kappa<1$，有 $E_++\delta_y\le E_++\delta_y/\kappa\le\sigma W_*$。又 $d(x)\ge(\sqrt c-\sigma)W_*$，所以 $\|x-y\|\le\lambda W_*+E_++\delta_y\le(\lambda+\sigma)d(x)/(\sqrt c-\sigma)$，与 UI12 的物理长度常数相同。这定义了另一个明确允许关系，不能冒称所有物理输出仍在真图上。一般 GPPA 的点误差还必须有 $\|v(y)-v(y_*)\|$ 的可检查界，非连续或只局部认证的核不自动提供它。

## 7. 仍未闭合的 6pro 交接题及两轮尝试记录

这里的 `6pro` 指**待交接的问题规格**，不声称已调用或获得该模型的证明。已完成两轮：第一轮试图从精确输出或核范数自动搬运，被 C276、核纤维漂移和零见证有限接受反例否定；第二轮回到完整图耦合，闭合了 UI-COH、方向 GU3、联合一维长度、固定/移动投影核及有证书的同点近似成员资格。一般曲零集、非线性非单射核的可实施统一仍开放。

**6pro-I：非线性方向图证书到可计算停止规则。** 固定同一 $F,S=\operatorname{zer}F,\lambda$ 和明定完整候选图/允许关系，给出一类可由算子组成项检验的有限方向/Gram 不等式；目标是消去未知零锚及 $d(x),d(y)$ 后，产生仅用 $(x,y,w,e)$ 和已认证常数的停止不等式。必须同时满足：(i) 真残差为完整下确界；(ii) 所有接受输出都有限长；(iii) 所有认证输入有精确种子通过，帽不排掉全部种子；(iv) 非零见证的严格内层余量可证；(v) 对 GU3 保留方向优势，对 diagonal 保留 UI14 的正预算，对两支 UI19 保留联合长度而不要求几何率。不能以 UI4 自身或“所有可行点已经收缩”充当唯一原始假设。当前障碍是一般曲零集的锚依赖和实际图相关性在消元中的丢失。

**6pro-II：非单射且移动的非线性核。** 固定同一原 $F,S$，允许 $v_k$，求可检查条件同时控制：(a) 可见方向的耗散；(b) 核纤维内运动；(c) 跨步核变化。不能假设 $v_k^{-1}$、不能把 $v_k(x)-e$ 当成有物理原像、不能只证明核距离。须包含 UI23–33 的尖锐边界：固定投影允许 $\sigma<1$，任意移动投影最多允许 UI30；若一般定理给更宽范围，须指出额外跨步条件排除了 UI32。还必须排除 UI33a–e：一致 SPD 界及强单调原图即使在零误差下也不够，这一版本已反驳而非开放。物理提升应由原图条件推导，而非仅重写 C249-G3；共同 Lyapunov 结构、可和核变动或具有原图耦合的跨步限制是待检查输入，不能仅列出名字便视为已证。若只能获得一个抽象 $h$，应标为 C249 接口而非已解决这一题。

**6pro-III：完整输入与可认证近似图 oracle 的有限终止。** 在 UI34 或邻近真图证书下，给非线性/多值结构的有限代价证书生成算法，说明证书域覆盖全部接受输出。必须区分 $x\notin S$ 与 $w_*\ne0$：UI5.3 已否定二者对 GPPA 的自动等价。问题应允许明确的精确零证书分支，或证明另一个能处理零见证种子的终止机制；不得声称任意始终非零逼近序列能通过一个强制零吸收的相对预算。若没有这样的机制，全输入有限接受的目标应降为开放，不能靠“存在精确种子”结束证明。

## 8. 复算与接收边界

运行 `python3 research/code/unified_ppa/inexact_verify.py`。脚本使用标准库，对 UI13 的系数、UI14 的 diagonal、GU3 临界发散、两支长度身份、UI29 的标量极值、UI32–33 的移动核端点以及 UI33a–e 的强单调移动核发散作独立数值/有理恒等式复算。有限网格只发现公式实现错误，不代替上面的全称解析证明。独立审查已冷读 UI1–38，并另行重构新增 UI18a–c、UI14a–c 和 UI33a–e；UI13 的剖面极小化、UI29 的分支临界点、UI33 的临界旋转及移动 SPD 的矩阵公式均已复算。审查提出的一维/满秩锐性量词已按 §5.2 修正；后续复读未发现新的数学必修项。这是限定范围的内部审查，闭合单元注册 C283/C284；不认证外部首创，末节一般非线性核义务保持 open。数学范围、工程可实施性、机制价值和公开新颖性分开判定。
