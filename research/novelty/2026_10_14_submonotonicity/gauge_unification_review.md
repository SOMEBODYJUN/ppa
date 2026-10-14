# 次单调的一般函数化：精确桥、不可压缩信息及 C250 边界

2026-10-14。独立研究报告；GU1 与 GU3 仅为本报告的候选定位号，均为 **candidate**，等待独立接收；不注册新主贡献。没有改动主稿、CLAIMS 或图，也不声称首创。

**裁决。** 一般二变量耗散预算确实比单个输入模保留更多信息，但“把常数换成函数”本身没有产生新的收敛机制。若该预算的可行集具有有限且原点消失的径向包络，就能编译回 RL；若缺少这个门，可能连近端单值性或局部有界性都没有。能够严格越过现有 C250 的方向是保留法向耗散与切向位移的联动，避免先用全空间范数抹掉方向。§7 给出完整两支关系：全部选择有限长，而任何固定 `v=Id`、同物理目标的 C250 证书都失败。该例的正面机制已经出现在仓库 SC14–SC15 的法向/切向直接估计中，仅保留为 C250 压缩边界诊断。零距离处的完整物理漂移反例见 §6：耗散和真 EB 均不能删除零步门。

## 1. 对象、阅读依据与比较范围

固定实 Hilbert 空间 $H$、$\lambda>0$、图块 $\Gamma\subset H\times H$。全对条件始终量化 $(x,w),(x',w')\in\Gamma$，并固定

\[
a=x-x',\qquad b=\lambda(w-w'),\qquad z=a+b,\qquad c=a-b.
\tag{1}
\]

因而

\[
4\langle a,b\rangle=\Vert z\Vert ^2-\Vert c\Vert ^2,
\quad a=(z+c)/2,\quad b=(z-c)/2.
\tag{2}
\]

核版以 $a=v(x)-v(x')$ 替换第一项；这只识别核图点，核非单射时不自动识别物理点。算法锚比较则取 $a=v(y)-v(p)$、$b=v(x)-v(y)$，其中同一个 $p\in P_S(x)$，不再量化两个任意输出。下文每次切换均显式说明。

已读取仓库 AGENTS、RESEARCH_PROTOCOL 及 academic-writing-skills 的 mathematics、mathematical-exposition、execution-and-acceptance、universal-integrity。未发现另名 `mathskill` 的本地文件，数学门按上述仓库指定 skill 执行。承重既有正文为：

- [C249/C250](../../canonical/physical_rleb_gppa.md#prg-energy)：同物理锚、完整真残差、一般核能量与物理提升。
- [C02-v3](../../canonical/true_residual_selection_rleb.md#trs-theorem)：全部允许选择、严格留域预算。
- [一般模 GPPA](../../canonical/generalized_ppa_modulus.md#gpm-theorem)：核标量证书与物理提升分开。
- [C89–C91](../../canonical/non_tied_cayley.md)：非 tied 二参数的精确平移球、锐步长门和全局极大性覆盖；这些不是本轮新增。
- [参数字典](../../canonical/parameter_dictionary.md)：全对/锚定、图块/完整纤维、步长变换的既有区别。

**一手文献实读。** Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, DOI [10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)，正式在线版 2025-11-21，读取 Definition 2、Propositions 3/4/6、Assumption 2 与 Theorem 2。其全对条件是对截断图的 $\lambda F$ 使用二次 Minty 输入缺陷；局部覆盖另列在 Assumption 2(d)(ii)，最终轨道取指定局部输出。本文只用这些比较事实，不导入其整套收敛定理。以下一般函数公式及锐边界均为本报告推导；不能归作 LT 原文定理。

## 2. 四种 gauge 的准确双向桥

令 $r=\Vert a\Vert ,s=\Vert b\Vert ,t=\Vert z\Vert $。允许 signed 预算时，正耗散与负耗散均保留；若一律要求预算非负，会丢掉 $\omega(t)<t$ 所代表的正耗散。

| 条件 | 精确反射坐标形式 | 保留的信息 |
| --- | --- | --- |
| Input gauge：$\langle a,b\rangle\ge-d(t)$ | $\Vert c\Vert ^2\le t^2+4d(t)$ | 纯输入径向模；取 $d(t)=[\omega(t)^2-t^2]/4$ 与 RL 双向等价 |
| Primal gauge：$\langle a,b\rangle\ge-h(r)$ | $\Vert c\Vert ^2\le t^2+4h(\Vert z+c\Vert /2)$ | 反射未知量仍在右端，不能直接当输入模 |
| Dual gauge：$\langle a,b\rangle\ge-k(s)$ | $\Vert c\Vert ^2\le t^2+4k(\Vert z-c\Vert /2)$ | 原始值方向与 primal 交换；同样是隐式约束 |
| 二变量预算：$\langle a,b\rangle\ge-D(r,s)$ | $\Vert c\Vert ^2\le t^2+4D(\Vert z+c\Vert /2,\Vert z-c\Vert /2)$ | 依赖输入与反射的相对方向，通常不能用一个径向模双向恢复 |

四行均只是 (2) 的展开，量词和图块完全相同。一般图方向预算 $\mathcal D(a,b)$ 的精确右端是 $t^2+4\mathcal D((z+c)/2,(z-c)/2)$。此坐标双射永远成立；存在单值 Cayley 映射是额外命题。

原算子若满足 $\langle\Delta x,\Delta w\rangle\ge-\phi(\Vert \Delta x\Vert )$，表中的 $h=\lambda\phi$。若满足 $\langle\Delta x,\Delta w\rangle\ge-\chi(\Vert \Delta w\Vert )$，则 $k(s)=\lambda\chi(s/\lambda)$。省略这两次缩放会直接把临界步长写错。

### 可以反向恢复什么

二变量条件在交换 $a,b$ 时精确变成 $D^{\rm op}(r,s)=D(s,r)$。对应原关系取逆还需同步把步长换成 $1/\lambda$ 并缩放两侧；不能把“逆关系对称”读作“同关系对所有步长不变”。

Input 条件本身不恢复有限二次 primal 或 dual 缺陷。例如已有完整受限平方根图 $F(u)=-\sqrt u$、$0\le u\le1/16$、$\lambda=1$，有反射 $L=3$，却无有限 quadratic primal 缺陷；原文 Example 2 与仓库的 [受限根图](../../topics/examples/restricted_root_graph.md)分别给来源与精确对象。一般输入预算若另有同图 $s\le Kr$，且其非负部分可由非减 $d_+$ 控制，才可推出 $h(r)=d_+((1+K)r)$；反向 dual 类似。这个附加图斜率界承担信息恢复，不是形式改名。

## 3. GU1-v1：一般二变量预算可编译为 RL 的精确门

**Status：candidate。对象与量词。** 固定 $\dim H\ge2$、$R>0$、有限函数 $D:[0,\infty)^2\to\mathbb R$、$D(0,0)\ge0$。对每个 $0\le t\le R$ 定义

\[
\mathcal E_D(t)=\{(u,r,s):0\le u\le t,\ r,s\ge0,
 |r-s|\le u\le r+s,\ r^2+s^2-2D(r,s)\le u^2\},
\]
\[
\Omega_D(t)=\sup_{(u,r,s)\in\mathcal E_D(t)}
\sqrt{2(r^2+s^2)-u^2}.
\tag{3}
\]

平方根因三角条件非负，集合含零三元组，允许上确界 $+\infty$。则对任意有限非减 $\omega:[0,R]\to[0,\infty)$、$\omega(0)=0$，以下等价：

1. 每张满足 $\langle a,b\rangle\ge-D(r,s)$ 的非空图，都在输入对尺度 $R$ 上满足同一个全对 RL 模 $\omega$。
2. 对每个 $0\le t\le R$，有 $\Omega_D(t)\le\omega(t)$。

因此整个 $D$-类具有一个共同有限、原点连续的 RL 模，当且仅当 $\Omega_D(R)<\infty$、$\Omega_D(0)=0$ 且 $\Omega_D(t)\to0$ 当 $t\downarrow0$。这里的“整个类”包含所有二点图；不是断言每张具体图都必须满足该普适包络的必要性。

**证明。** 任意实际图差的 $(\Vert z\Vert ,r,s)$ 属于 $\mathcal E_D(t)$，且 $\Vert c\Vert ^2=2(r^2+s^2)-\Vert z\Vert ^2$，故 2 推出 1。反向，对任意可行三元组，三角条件保证存在 $a,b\in H$ 满足其三个范数；当 $r,s>0$，取夹角余弦 $(u^2-r^2-s^2)/(2rs)\in[-1,1]$，零范数端点直接实现。由 $(0,0),(a,b/\lambda)$ 生成二点图；正反有序差与自身配对均满足预算。应用 1，再用 $u\le t$ 及 $\omega$ 非减即得 2。最后 $\Omega_D$ 本身非减，满足所列三门时就是所求模。□

这把“是否只是 RL 包装”变成一个可攻击的标量问题。但若只把 $\Omega_D$ 定义为最坏图差而没有求出它或验证有限/消失门，仍没有增加可用理论。

### 单值性门与紧性门不可混合

同输入时 $u=0,r=s=q$，预算变为 $q^2\le D(q,q)$。所以

\[
D(q,q)<q^2\quad(q>0)
\tag{4}
\]

是整个类统一排除 Minty 碰撞的充要条件。必要性由 $a=-b\ne0$ 的二点图证明，充分性由 (2) 证明。它没有保证 $\Omega_D(t)\to0$。

**远端攻击。** 取连续非负预算

\[
D(r,s)=rs\left(1-\frac1{1+(r+s)^4}\right).
\tag{5}
\]

它严格满足 (4)。然而令 $r=s=N$，取 $u_N^2=2N^2/(1+16N^4)$，则 $(u_N,N,N)$ 可行，$u_N\to0$，反射长度 $\sqrt{4N^2-u_N^2}\to\infty$。故每个 $t>0$ 都有 $\Omega_D(t)=+\infty$。这是**同一预算类中二点图族**的普适失败，不伪称已构造单张满足全部跨对约束的坏图。

若额外限制 $0\le r,s\le M<\infty$，$D$ 在该方块连续并满足 (4)，则受限包络有限且原点消失：反设有 $u_j\to0$ 但 $r_j^2+s_j^2\not\to0$，取紧子列得 $r=s=q>0$，极限预算迫 $q^2\le D(q,q)$，矛盾。这个短证明准确说明为什么 local graph block 的有界领圈可能够用，而完整图的 remote branch 仍需排除。

## 4. Primal/dual 一般函数门及临界参数

对 primal 条件，Cauchy 不等式直接给

\[
r t\ge\langle a,z\rangle\ge r^2-h(r),\qquad
t\ge r-\frac{h(r)}r\quad(r>0).
\tag{6}
\]

若使用范围内存在严格递增 $m$、$m(0)=0$，使 $r-h(r)/r\ge m(r)$，且 $h$ 非减，则

\[
r\le m^{-1}(t),\qquad
\Vert c\Vert \le\sqrt{t^2+4h(m^{-1}(t))}.
\tag{7}
\]

逆函数须在实际输入窗可评价；不覆盖的范围不能写进结论。Dual 交换 $r,s$ 得同式。若 $h$ 非单调，可使用在已证 $r$-区间内的上包络；正负部分及有限性需另核。

二次情形 $h(r)=\alpha r^2$、$0\le\alpha<1$ 给锐普适界

\[
L_C=\frac{1+\alpha}{1-\alpha},\qquad
\tau=\frac{\alpha}{(1-\alpha)^2}.
\tag{8}
\]

取完整线性图 $b=-\alpha a$ 达等；$\alpha\ge1$ 的类含 $b=-a$，连单值性都不能统一保证。原始 quadratic hypo 是 $\alpha=\lambda h_0$，故小步长门为 $\lambda h_0<1$；quadratic co-hypo 是 $\beta=k_0/\lambda<1$，故大步长门为 $\lambda>k_0$。这些是固定类别的普适保证门，不是每个算子的必要门。式 (8) 是已有 C89 的特例；LT Proposition 6 给的显示充分范围不应与此锐普适门混写。

一般幂 $h(r)=A r^p$ 的零尺度性质不同：$p<2,A>0$ 时所有充分小 $r$ 都允许 $a=-b$；$p>2$ 则在足够小的 **primal 差范围** 内变成 subcritical quadratic 门。最值得区分的是二次临界首项：仅知道 $h(r)/r^2\to1$ 不够。

例如 $\lambda=1,F(x)=-x+x^3$ 的图块 $|x|\le\varepsilon<1/2$。对所有点对，令 $r=|x-x'|$，有

\[
\langle a,b\rangle\ge-r^2+r^4/4,
\qquad |z|=|x^3-x'^3|\ge r^3/4.
\tag{9}
\]

因为 $x^2+xx'+x'^2\ge(x-x')^2/4$。该图的 Minty 输入是 $x^3$，自然域为 $[-\varepsilon^3,\varepsilon^3]$，反射连续且为 $1/3$-Hölder；取 $x'=0,x\to0$ 排除 Lipschitz。与 $F=-I$ 的全碰撞相比，二者 quadratic 临界系数相同，高阶余量才决定可逆性。此例不认证 PPA 收敛：此处近端为立方根，零附近非零轨道反而向外。

## 5. Semimonotonicity：已有精确结构不能降格成一个模

原始二参数条件 $\langle\Delta x,\Delta w\rangle\ge\mu\Vert \Delta x\Vert ^2+\rho\Vert \Delta w\Vert ^2$ 在 (1) 中写成

\[
\langle a,b\rangle\ge m r^2+\sigma s^2,
\qquad m=\lambda\mu,\quad\sigma=\rho/\lambda.
\]

置 $A=1+m+\sigma$、$B=m-\sigma$、$\Delta=1-4m\sigma$。与之精确等价的是

\[
A\Vert c\Vert ^2+2B\langle z,c\rangle\le(1-m-\sigma)\Vert z\Vert ^2.
\tag{10}
\]

当 $A>0,\Delta\ge0$ 时，进一步等价于平移球

\[
\left\Vert c+\frac BA z\right\Vert \le\frac{\sqrt\Delta}{A}\Vert z\Vert .
\tag{11}
\]

所以一般 semimonotone 类与**平移后的** Cayley Lipschitz 类双向等价，而只与未平移 $C$ 的径向模单向关联。$A\le0$ 时类含 $F=-I/\lambda$，故任意原点消失模都不能统一成立。正正 $\mu\rho>1/4$ 的退化单点类及负负 $\mu\rho\ge1/4$ 的无约束类须另分，不允许在 $\sqrt\Delta$ 不实或 $A=0$ 时硬套公式。

一个最短不可恢复证据：$\lambda=1,\mu=1,\rho=0$；$F_-(x)=3x$、$F_+(x)=x/3$ 的 $C$ 分别为 $-I/2,+I/2$，同一个最优输入径向模 $t/2$，但只有前者满足 $\langle a,b\rangle\ge\Vert a\Vert ^2$。因此不是把常数调得更精细就能恢复方向。以上恒等式、锐性、临界门和例子全部已经由 C89–C91 承担；本报告将其用于路线裁决，不再包装成新结果。

## 6. Coverage、完整纤维和核非单射的三道门

**Coverage 独立。** $F(x)=\{0\}$ 于 $x\ge0$、其余为空，完整图单调且所有输入模门成立，但自然 Minty 域只有 $[0,\infty)$，原点没有双侧输入邻域。更强的“完整定义域、闭图、全对 Hölder RL、真 EB 仍缺覆盖”已见 [TRS-COVERAGE-GAP](../../canonical/true_residual_selection_rleb.md#trs-coverage-gap)。GU1 不产生原生 coverage。

**完整纤维独立。** 取 $\lambda=1$、$M>2$，令完整图为 $F(x)=\{x\}$ 加入额外图点 $(M,-M)$。局部 identity 图块覆盖零输入邻域、单调且单值；完整真残差仍为 $|x|$，零集仍为 $\{0\}$。然而完整 $J_F(0)=\{0,M\}$，局部图块结论不能控制完整输出。零输入吸收失败已经足以击穿严格小盆地结论，无需模拟长轨道。

**核物理门独立。** 在 GPPA 中即使核差满足任意强的反射模，$v(x)=v(y)$ 也未必给 $x=y$。C249 的物理提升 $h$ 与在零输入处的消失条件不能删除；既有 $v(t,s)=(t,0)$、完整核纤维自由移动的反例已经覆盖此问题。一般 D 同样不会修复核不可见方向。

**完整零输入漂移：比距离收缩更硬的物理攻击。** 取 $\lambda=1,v=\operatorname{Id}$，

\[
F(u,v)=\{(u,0),(u,-1)\},\qquad S=\{0\}\times\mathbb R.
\]

这里第二坐标变量 $v$ 与核名称不同；核始终固定为恒等映射。完整真残差为 $r_F(u,v)=|u|$，且

\[
J_F(a_0,b_0)=\{(a_0/2,b_0),(a_0/2,b_0+1)\}.
\]

完整覆盖与全部选择的距离 $1/2$ 收缩同时成立；但从零点 $(0,0)$ 每次选第二支，就有 $x^k=(0,k)$，既不收敛也无有限物理长度。该图还满足一个连续非负 intrinsic 预算：图差 $a=(\Delta u,\Delta v)$、$b=(\Delta u,\Delta e)$，其中 $e\in\{0,-1\}$，故

\[
\langle a,b\rangle=(\Delta u)^2+\Delta v\Delta e
\ge-\Vert a\Vert\min(\Vert b\Vert,1).
\]

即 $D(r,s)=r\min(s,1)$。该预算在 $0<q\le1$ 有 $D(q,q)=q^2$，准确允许同输入差碰撞。锚输入在零集时，漂移支物理步长恰为 1；任何要求 $B(0)=0$ 的统一步长包络、C249 的 G2–G3、以及 SC15 的切向上界零处消失都排除此例。因此，规范的可行集父证书必须同时输出距离收缩和原点消失的物理步长；只输出距离收缩不够。这个反例由本轮独立评判提供，公式在此逐项重算。

全局同参数极大性在 C91 的二次平移球范围确实可借 Hilbert 同常数扩张给满域。一般 D 未给出对应扩张定理；不能把“存在极大扩张”与“每个极大图满 Minty 域”混为一谈。LT 的局部覆盖前提也没有被它的极大性标签替代。

## 7. 已有法向/切向机制与 C250 压缩诊断

[已有结构稿 SC14–SC15](../../candidates/coupled_holder_structural.md) 已证明：法向强耗散给完整输出距离收缩，切向上界给几何级数长度；SC15 明确允许删除切向下界。因而下面的两支模型复用了已有机制，不注册新的投影父定理。该稿针对 direct G5 的常数门作了精确排除；下面另把固定 C250 的标量能量压缩也排除，仍只作短诊断。

其承重估计可压成一行：若正交法向投影 $N$ 满足 $\langle Ny,Nw\rangle\ge m\Vert Ny\Vert^2$，近端包含就给 $\Vert Nx\Vert\Vert Ny\Vert\ge(1+\lambda m)\Vert Ny\Vert^2$。再有切向步长上界 $h(\Vert Ny\Vert)$ 与可和性，便获得物理长度。完整 coverage 与零输入 $h(0)=0$ 仍是独立前提。

### GU3-v1：固定物理 C250 的严格盲区

**Status：candidate。完整对象。** 任取 $0<\gamma<1$，在 $X=\mathbb R^2$ 固定 $\lambda=1,v=\operatorname{Id}$、完整关系

\[
F(u,s)=\{(0,s),(-2^\gamma|s|^\gamma,s)\},
\qquad S=\mathbb R\times\{0\}.
\tag{15}
\]

它的完整零集为 $S$，完整真残差恰为 $r_F(u,s)=|s|$。逐支解方程给每个输入 $(x,r)$ 的完整输出

\[
J_F(x,r)=\{(x,r/2),(x+|r|^\gamma,r/2)\}.
\tag{16}
\]

故 coverage 全域；零输入全部驻定；每条选择有 $|r_k|=2^{-k}|r_0|$，且

\[
\Vert x^{k+1}-x^k\Vert \le |r_k|^\gamma+|r_k|/2,
\qquad
\sum_{k\ge0}\Vert x^{k+1}-x^k\Vert
\le\frac{|r_0|^\gamma}{1-2^{-\gamma}}+|r_0|.
\tag{17}
\]

因此完整选择均有限长且收敛；SC15 的直接机制也适用。这里两点 uncertainty 纤维不凸，未导入 SC3 的 Kakutani 覆盖定理；coverage 是由 (16) 直接验证的。完整全对 RL 则因任意非零输入的两输出不同而失败，这只是 all-pairs 的零输入差碰撞，不妨碍实际解点吸收。

**C250 排除的精确量词。** 对该固定 $F,S,v=\operatorname{Id},\lambda=1,U=\mathbb R^2$、任意 $R,\bar t>0$、任意 $0<\kappa_*<1$，不存在满足 C249 G1–G4 以及 C250 标量兼容门的有限非减 $a,\omega,\psi$ 与允许的 $\rho,g$。允许关系必须等于 (16) 的完整输出；不是任意核或任意目标的排除。

**证明。** 反设存在。对输入 $(0,t)$、$0<t\le R$，最近物理锚唯一为 $p=(0,0)$，所以 G2 强制 $a(t)\ge t$。漂移支输出为 $(t^\gamma,t/2)$，其反射是 $(2t^\gamma,0)$，故 $\omega(t)\ge2t^\gamma$。

对每个充分小 $q>0$，考虑输入 $(0,2q)$ 的直支输出 $(0,q)$。它也是同一允许关系中的实际输出，且残差为 $q\le\bar t$。C250 的同锚下界与完整残差下界分别强制

\[
\rho(q)\le q,\qquad g(q)\le q.
\tag{18}
\]

G4 在某个正 $q_0$ 的实际输出上又强制 $M_0=\psi(\bar t)\ge q_0>0$。现令 $q=t^\gamma$，取 $t>0$ 足够小使 $2q\le R,q\le\bar t,q\le M_0$。由 $\omega$ 非减，

\[
\rho(q)^2+g(q)^2\le2t^{2\gamma}
\le\frac{a(t)^2+\omega(a(t))^2}{2}.
\tag{19}
\]

C250 的全称 scalar gate 必须推出 $q\le\kappa_*t$，但 $t^{\gamma-1}\to\infty$，矛盾。证明不依赖为 C250 选择“最优”还是“粗糙”模；全部合法选择都被排除。□

**信息为何丢失。** 漂移支在同一最近锚上有 $a=(t^\gamma,t/2),b=(-t^\gamma,t/2)$，故

\[
\langle a,b\rangle=t^2/4-t^{2\gamma},
\qquad\langle Na,Nb\rangle=t^2/4.
\]

全空间能量把巨大的切向相消计入反射上界；另一条直支又把全图真残差压回线性。C250 先把两类信息分别压成 $\omega$ 与 $\rho,g$，再允许任意组合的标量 $q$，遂出现实际图上不存在的“巨大反射且弱法向耗散”组合。保留 $Na=Nb$ 和切向预算可直接给 $2q=t$，没有这个虚假组合。

这没有证明法向/切向框架总体包含 C250：一般非仿射零集与一般核仍有不同对象门。准确关系是 SC15 已有直接机制的一张完整实例落在固定 `v=Id` C250 之外；这个边界不构成新的主贡献。

## 8. 对一般统一能量证书的评价

对 GPPA 的一个允许锚转移，把 $\delta=\Vert v(x)-v(p)\Vert $、$r=\Vert v(y)-v(p)\Vert $、$s=\Vert v(x)-v(y)\Vert $、$q=d(y,S)$ 同时保留，则基本能量只是

\[
r^2+s^2+2\langle a,b\rangle=\delta^2.
\tag{20}
\]

若以 $\langle a,b\rangle\ge-D(r,s)$ 代入，并合取 $\delta\le a_0(t)$、$\rho(q)\le r$、$\lambda g(q)\le s$、真 EB 评价域及物理位移界，便得到一个 $(q,r,s,\delta)$ 可行集。要求其中所有点满足 $q\le\kappa t$，再证步长可和，就给同样的有限前缀收敛证明。它可以保留比 C250 更多耦合，但如果最终仍只用了 $r^2+s^2\le[a_0(t)^2+\omega(a_0(t))^2]/2$，结论完全回到 C250，没有新机制。

更危险的是把“该可行集内 $q\le\kappa t$”直接当新条件：它可能只是把所需收缩改写成假设。要产生独立价值，应像 SC14–SC15 那样先给可由原算子验证的结构，证明它排除不可实现组合，并给完整实例显示旧压缩失败。GU3 提供这个最小见证；其数学机制简单，不够单独支撑首创性叙事。

**建议路线。** 不建议以“所有次单调概念统一为 $D$”作为主贡献。可以把 GU1 用作检查器，把 C89–C91 作为现成双向变换，把 SC14–SC15 与 GU3 用作 C250 方向信息缺失的例子。进一步研究的有意义对象是曲零集的可验证法向/切向耗散、非单射核的受控纤维运动，或能够保持全图可行集而不丢联动的算法证书。新对象仍要逐项给真残差、全输出覆盖及零输入吸收。

## 9. 有限复算、交付检查及未闭义务

执行：`python3 research/code/submonotonicity_routes/gauge_verify.py`。代码只使用 Python 标准库；Fraction 部分精确、无 seed，轨道前缀浮点容差 $10^{-12}$。有限复算覆盖 (2)、(10) 配方、临界三次图、远端预算、GU3 矛盾参数，以及 $\gamma=1/2,r_0=1/16$ 的全部 4096 个 12 步分支前缀。有限枚举不替代 §3、§7 的全称证明，也不声称枚举全部长轨道。

本轮实际输出为 finite_checks_passed：恒等式 2401 对、semimonotone 展开 1225 组、临界三次图 441 对全部精确通过；4096 个轨道前缀中最大长度 0.8432287289440467，小于解析无限尾界 0.916053390593274，法向误差为零。另 147 组零纤维漂移预算检验通过；漂移支 20 步到达 $(0,20)$，每步长度 1。后一失败的无限性由 §6 的显式轨道承担。

交付前按数学技能检查对象、图量词、真 residual 和证明衔接：§3 的“整个预算类”与“单张图”已经区分；§7 只排除固定物理核及固定目标的 C250，不排除其他坐标、其他核、KL 或三角系统的经典证明。本文为 Markdown 内部报告，无期刊版式或图像渲染要求。正确的 GPPA 引用入口为 [GPM 定理](../../canonical/generalized_ppa_modulus.md#gpm-theorem)。

待独立接收的具体义务：GU1 的二点图充要量词与带界 compactness；GU3 的“任意合法 $a,\omega,\psi,\rho,g$”排除量词。全部暂存 candidate，不登记新 canonical Claim。外部先行性未穷尽；尤其 SC14–SC15 的投影/三角机制应视为熟知结构，不能以本报告命名冒充新理论。
