# 联合预算的完整覆盖：极大反例、可扩张核及临界方向次数

2026-10-14。规范证明。闭合单元经实际全文冷审为 derived-checked，解析证明与有限复算分开；C280/C281 登记其身份。不改主稿、摘要或正文编号，不认证公开首创。共同问题是：在**固定原预算**中 graph-maximal，是否足以使完整普通近端关系处处非空？

结论分三层。连续、非负、碰撞安全且具有良好 RL 包络的联合预算，仍可有显式极大图缺失所有非整数 Minty 输入。保留一个可嵌入 Hilbert 空间的输入差核，则能在仿射方向中心及固定椭球目标范数下同预算扩张。完整 Minty 域之后，原关系的正、逆纤维非空和紧性还需另一个次数门；临界线性方向可以由次线性恢复场补回，但这类方向条件不会由普通 Kirszbraun 扩张自动保留。

读者路线：§1 固定对象；§2 给真正极大反例；§3–4 构造保方向的非线性扩张类及其完整纤维；§5 攻击奇异线性部并给可行恢复；§6 将一般覆盖问题缩成有限锚检查；§7 固定下一轮尚未证明的高价值目标。这里的“完整纤维”指原关系的全部图点，真残差始终为 infimum。

<a id="uc-object"></a>
## 1. 对象和已有边界

固定实 Hilbert 空间 $H$、$\lambda>0$、非空图 $G\subset H\times H$。对图差记

\[
 a=x-y,\qquad b=\lambda(v-w),\qquad z=a+b,\qquad c=a-b.
 \tag{UC1}
\]

Minty 坐标为 $p=x+\lambda v$，反射坐标为 $C(p)=x-\lambda v$。只要同输入排他成立，图与部分映射通过

\[
 (x,v)=\left(\frac{p+C(p)}2,\frac{p-C(p)}{2\lambda}\right)
 \tag{UC2}
\]

双向对应。原完整 $J_{\lambda F}$ 的定义域恰为 $D=\{x+\lambda v:(x,v)\in\operatorname{gph}F\}$。固定预算 graph-maximal 是不能再增加满足该**同一预算**的图点，既不是任意更大类的极大性，也不是极大单调。

已有 [GU1](../novelty/2026_10_14_submonotonicity/gauge_unification_review.md) 给一般径向联合预算

\[
 \langle a,b\rangle\ge-D(\|a\|,\|b\|)
 \tag{UC3}
\]

的普适 RL 包络，却不提供保持原 $D$ 的扩张。[HE-EXTENSION](../canonical/holder_extension.md#he-extension) 保持的是固定 Hölder 预算；[FC-GLOBAL/WINDOW](../canonical/full_fiber_coverage.md#fc-global) 的完整逆纤维与固定窗身份，另外使用次线性增长和有限维存在性。[C249/C250](../canonical/physical_rleb_gppa.md#prg-object) 直接把完整允许输入覆盖列为前件，不从误差界取得存在性。

<a id="uc-maximal-hole"></a>
## 2. UC-HOLE-v1：近线性、非负联合预算中的显式极大缺口

- **Status**：`derived-checked`，完整解析反例，经独立实际全文冷读，注册 C281。
- **Exact statement**：每个 $n\ge1,\lambda>0$，存在连续、对称、非负 $D:[0,\infty)^2\to[0,\infty)$，满足 $D(q,q)<q^2$ 对全部 $q>0$，其普适输入包络有限且原点连续，甚至有全局反射 Lipschitz 上界 $\sqrt2$。但该固定 $D$-类有闭的 graph-maximal 完整关系 $F:\mathbb R^n\rightrightarrows\mathbb R^n$，其完整近端域只有 $\mathbb Z\times\mathbb R^{n-1}$。零集闭凸，真线性 EB 全域成立，仍不存在任何原点双侧输入邻域。

定义

\[
 \omega(t)=t\sqrt{1+\min(t^2,1)},\qquad t\ge0,
 \tag{UC4}
\]
\[
 f(W)=
 \begin{cases}
 \sqrt{1+2W}-1,&0\le W\le3/2,\\
 2W/3,&W\ge3/2,
 \end{cases}
 \qquad D(r,s)=\frac{r^2+s^2-f(r^2+s^2)}2.
 \tag{UC5}
\]

函数 $f$ 是严格增函数 $u\mapsto2u+\min(u^2,u)$ 对输入 $2W$ 的逆，即

\[
 2f(W)+\min(f(W)^2,f(W))=2W.
 \tag{UC6}
\]

它在 $W=3/2$ 两支共同取值 $1$，故连续。第一支有

\[
 \frac{f(W)}W=\frac2{\sqrt{1+2W}+1}\in[2/3,1]\quad(0<W\le3/2),
\]

因此 $0\le D(r,s)\le(r^2+s^2)/6$；$f(W)>0$ 对 $W>0$，也给 $D(q,q)=q^2-f(2q^2)/2<q^2$。

**同一预算的精确等价。** 置 $W=\|a\|^2+\|b\|^2$、$u=\|z\|^2$。由 $u=W+2\langle a,b\rangle$，(UC3) 恰等于 $u\ge f(W)$。借 (UC6) 与严格单调性，它又恰等于

\[
 2W\le2u+\min(u^2,u)
 \iff\|c\|^2\le u+\min(u^2,u)
 \iff\|c\|\le\omega(\|z\|).
 \tag{UC7}
\]

这里没有把原 $D$ 换成较宽的 Lipschitz 类。每个 $t$ 的两点图可取共线 $z,c$，其中 $\|z\|=t,\|c\|=\omega(t)$，故 GU1 的最小普适包络正是 $\omega$。它有限、非减、原点连续，并且

\[
 t\le\omega(t)\le\sqrt2t,\qquad \omega(t)/t\longrightarrow1\quad(t\downarrow0).
 \tag{UC8}
\]

**极大图。** 写 $p=(k,u)\in\mathbb Z\times\mathbb R^{n-1}$，令

\[
 C(k,u)=(\sqrt2k,u).
 \tag{UC9}
\]

同层 $k=k'$ 时反射差等于输入差；异层时输入差范数至少 $1$，而反射差平方 $2(k-k')^2+\|u-u'\|^2\le2\|p-p'\|^2$。故全部图点对满足 (UC7)。

设可增加某点 $p=(t,u)$。若 $t\in\mathbb Z$，同输入的 $\omega(0)=0$ 强制反射已是 (UC9)。若 $k<t<k+1$，取两个已有锚 $(k,u),(k+1,u)$，其反射中心间距为 $\sqrt2$。令 $\alpha=t-k\in(0,1)$。任何新反射必须同时属于两个半径为 $\omega(\alpha),\omega(1-\alpha)$ 的闭球。但

\[
 \omega(\alpha)+\omega(1-\alpha)
 <\sqrt2\alpha+\sqrt2(1-\alpha)=\sqrt2,
 \tag{UC10}
\]

两球不交。故无法增加任何图点，(UC9) 已在固定原 $D$ 中 graph-maximal，不需 Zorn 或未显式的 completion。

由 (UC2)，完整关系是

\[
 F(x_1,u)=
 \begin{cases}
 \{(\beta x_1,0)\},&x_1\in\frac{1+\sqrt2}{2}\mathbb Z,\\
 \varnothing,&\text{其他},
 \end{cases}
 \qquad \beta=-\frac{3-2\sqrt2}{\lambda}.
 \tag{UC11}
\]

其图闭，完整零集 $S=\{0\}\times\mathbb R^{n-1}$。在非空原纤维上真残差是 $r_F(x_1,u)=|\beta x_1|$，空纤维取 $+\infty$。所以全部点满足扩展实数意义的全域真 EB

\[
 d(x,S)\le\lambda(3+2\sqrt2)r_F(x).
 \tag{UC12}
\]

原点零输入纤维唯一且驻定，但完整 $J(p)$ 在每个非整数第一坐标输入上为空。这个反例隔离的是**存在性**，没有借零集非凸、残差伪造或零输入漂移制造失败。原 $F$ 不具有处处非空原定义域；定理并未假设这个独立门。

**扩张失效的有限核证据。** 对源点 $p_0=1/2,p_1=0,p_2=1$ 和系数 $(-1,1/2,1/2)$，有

\[
 \sum_{i,j=0}^2 a_i a_j\omega(|p_i-p_j|)^2=3/8>0.
 \tag{UC13}
\]

故这个平方输入核不是条件负定。原点消失、近线性上界和全局有限 RL 包络，没有替它补出 Hilbert 输入嵌入。放宽预算到 $\sqrt2t$ 确可补成 $C(p)=(\sqrt2p_1,p_\perp)$，但那已经改变固定预算身份。

<a id="uc-hilbert-profile"></a>
## 3. UC-EXT-v1：保留方向和混合非线性核的同预算扩张

- **Status**：`derived-checked`，自足核推导加已核 Kirszbraun 接口；不是新扩张机制的优先性声明。
- **Exact statement**：固定 Hilbert $H$，有限个有界线性 $P_j:H\to H_j$，有界线性 $A:H\to H$，有界可逆线性 $Q:H\to H$。固定非负有限函数（下面的 $\mu_j$ 为非负 Borel 测度）

\[
 \phi_j(s)=a_js+\int_{(0,\infty)}(1-e^{-ts})\,\mu_j(dt),
 \quad a_j\ge0,\quad \int\min(1,t)\mu_j(dt)<\infty.
 \tag{UC14}
\]

令

\[
 K(p,q)=\sum_j\phi_j(\|P_j(p-q)\|^2).
 \tag{UC15}
\]

每张非空图只要对全部图点对满足

\[
 \|Q(c-Az)\|^2\le K(p,q),\qquad z=p-q,
 \tag{UC16}
\]

就有一个全域扩张保持**同一** $A,Q,P_j,\phi_j,\lambda$。该固定类中 graph-maximal 当且仅当完整 Minty 域为 $H$，且完整普通近端处处单值。

这保留了固定椭球范数、仿射方向中心、不同投影及不同非线性尺度。取 $\phi_j(s)=L_j^2s^{\gamma_j}$, $0<\gamma_j\le1$，即保留混合 Hölder 幂；取 $\log(1+s)$ 或 $1-e^{-s}$ 可得到非幂例。投影可以有共同核；这只使输入嵌入成为 pseudometric，不破坏同预算扩张。

**核证明。** 对任意有限点 $p_i$ 和实系数 $\alpha_i$ 满足 $\sum_i\alpha_i=0$，线性项给

\[
 \sum_{i,l}\alpha_i\alpha_l\|P_j(p_i-p_l)\|^2
 =-2\Big\|\sum_i\alpha_iP_jp_i\Big\|^2\le0.
\]

每个 Gaussian 核 $e^{-t\|P_j(p_i-p_l)\|^2}$ 正定；可按 [HE-SNOWFLAKE](../canonical/holder_extension.md#he-snowflake) 的张量幂展开逐项证明。因此积分项的零和二次型为该正定二次型的负值。由于每对的 (UC14) 积分有限，有限和可先截断积分再取极限，得到

\[
 \sum_{i,l}\alpha_i\alpha_l K(p_i,p_l)\le0.
 \tag{UC17}
\]

固定基点 $o$，以内积

\[
 \langle\delta_p-\delta_o,\delta_q-\delta_o\rangle
 =\tfrac12[K(p,o)+K(q,o)-K(p,q)]
 \tag{UC18}
\]

赋半内积、商去零向量并完备化，得 Hilbert $E$ 及映射 $J:H\to E$，满足 $\|Jp-Jq\|^2=K(p,q)$。这一步不借核名称省掉证明。

**扩张证明。** (UC16) 在相同 $p$ 时强制 $c=0$，故部分 $C:D\to H$ 良定。令

\[
 N(p)=Q(C(p)-Ap).
 \tag{UC19}
\]

它对输入度量 $\sqrt K$ 为 1-Lipschitz；若 $Jp=Jq$，则 $N(p)=N(q)$，所以 $N\circ J^{-1}:J(D)\to H$ 良定。Hilbert 间 Kirszbraun 同常数扩张给 $\widehat N:E\to H$。置

\[
 \widehat C(p)=Ap+Q^{-1}\widehat N(Jp),\qquad p\in H,
 \tag{UC20}
\]

并按 (UC2) 反剪切，即得到保持完整原预算的图扩张。若 $D\ne H$，加入新 $p$ 是真扩张；若 $D=H$，兼容新图点与相同 $p$ 的旧点比较，(UC16) 迫使反射相同。因此极大性与满 Minty 域等价。

**与纯矩阵路线去重。** [原生预算演算稿](unified_ppa_raw_calculus.md) 已给二次矩阵配方 $Q_m\succ0,H_m\succeq0$，在 $H_m$ 商空间同预算扩张，包括奇异 $H_m$。它是本节全线性输入核的有限维实例；本页不把纯二次配方另列新发现。这里真正补的是一般正权非线性输入核、混合尺度及其后续完整纤维门。

**边界。** 同参数极大性必须指 (UC16) 这个完整类；如果另外要求指定零集、真 EB、切向预算、critical restoring cone、势函数或某个像集，扩张证明没有保持这些附加条件。只知道某个普通 RL 上界，不能反推同 (UC16) 的扩张，更不能反推原 (UC3) 的扩张。

<a id="uc-full-fibers"></a>
## 4. UC-DEG-v1：仿射加次线性 profile 的正、逆完整纤维

- **Status**：`derived-checked`。固定 $H=\mathbb R^n$，取 §3 的同预算 graph-maximal 完整关系。另要求每个 $\phi_j(s)/s\to0$ 当 $s\to\infty$，以及 $I+A,I-A$ 都可逆。
- **Conclusion**：每个原输入 $x$ 的完整 $F(x)$ 和每个原输出 $v$ 的完整 $F^{-1}(v)$ 都非空紧。完整零集非空紧。两坐标映射的全局 Brouwer 次数分别为 $\operatorname{sgn}\det(I+A)$ 和 $\operatorname{sgn}\det(I-A)$。

固定任一图锚 $p_0=x_0+\lambda v_0$，定义

\[
 \eta(r)=\|Q^{-1}\|\left[\sum_j\phi_j(\|P_j\|^2r^2)\right]^{1/2}.
 \tag{UC21}
\]

函数 $\eta$ 有限、非减、原点连续、$\eta(r)=o(r)$。由同预算有

\[
 C(p)-C(p_0)=A(p-p_0)+e(p),\qquad
 \|e(p)\|\le\eta(\|p-p_0\|).
 \tag{UC22}
\]

因此 $T_\pm(p)=p\pm C(p)$ 满足

\[
 T_\pm(p)-T_\pm(p_0)=(I\pm A)(p-p_0)\pm e(p).
 \tag{UC23}
\]

记 $m_\pm=\sigma_{\min}(I\pm A)>0$。对每个目标 $b$ 及充分大球半径 $R$，$m_\pm R-\eta(R)>\|b-T_\pm(p_0)\|$。所以从 (UC23) 到其线性部的同伦在球边界不经过 $b$。Brouwer 次数的同伦不变性和可逆线性映射归一化给 $\deg(T_\pm,B_R(p_0),b)=\operatorname{sgn}\det(I\pm A)\ne0$，故目标有原像。下界 $\|T_\pm(p)-T_\pm(p_0)\|\ge m_\pm\|p-p_0\|-\eta(\|p-p_0\|)\to\infty$ 又给 properness；目标原像闭且有界，因而紧。完整原纤维是相应原像经 (UC2) 的连续像，不是选中一支。

这一步明确使用有限维 Brouwer 次数的三条经典接口：边界避目标时的同伦不变性、可逆线性映射的次数为 determinant 符号、非零次数迫使目标原像非空。可以用 Brouwer 闭球不动点替代非空性证明，但那不会自动显示方向次数。

**全部逆纤维定位。** 定义

\[
 R_-(q)=\sup\{r\ge0:m_-r-\eta(r)\le2\lambda q\},\qquad q\ge0.
 \tag{UC24}
\]

集合非空，$R_-(q)<\infty$。对每个 $\|v-v_0\|\le q$，该完整非空逆纤维的**每个**点满足

\[
 \|p-p_0\|\le R_-(q),\qquad
 \|x-x_0\|\le X(q):=
 \frac{\|I+A\|R_-(q)+\eta(R_-(q))}{2}.
 \tag{UC25}
\]

该界只由同一原预算及锚决定，独立于选用哪个同预算 completion。固定窗 $G\subset U\times W$ 若在同 (UC16) 中相对极大，则任何同预算 completion $\widehat F$ 满足 $G=\operatorname{gph}\widehat F\cap(U\times W)$。若 $B(x_0,r)\subset U$、$B(v_0,s)\subset W$，并有某个 $q<s$ 满足 $X(q)<r$，则对 $\|v-v_0\|\le q$，

\[
 \varnothing\ne G^{-1}(v)=\widehat F^{-1}(v)\subset B(x_0,r).
 \tag{UC26}
\]

这给原窗口全部纤维的同预算身份。缺少 $X(q)<r$ 时，不能只凭窗口相对极大性获得窗口覆盖。原标量 $A=0,Q=I,\eta(r)=Lr^\gamma$ 时，(UC24) 的最大根是 $r-Lr^\gamma=2\lambda q$，(UC25) 恢复 [FC5–FC10](../canonical/full_fiber_coverage.md#fc-root) 的相同根几何。

**零几何边界。** 这里得到非空、紧和总次数，没有得到零集凸、全输出零吸收或轨道收敛。若全部零点对应 $T_-$ 的有限个 isolated regular 原像，则原像 Jacobian 符号之和必须等于 $\operatorname{sgn}\det(I-A)$。一般零簇的 Euler/固定点指数比较须另核吸引、ENR 或法向结构，不能把总次数直接读成零点数量。

**奇异门的最短攻击。** $A=I,C(p)=p+h$、$h\ne0$ 保持 §3 的零输入核预算，并且 Minty 域已是全空间；原 $F(x)=\{-h/(2\lambda)\}$ 没有零点。取 $A=-I,C(p)=-p+h$，则 Minty 域同样全空间，却只有 $x=h/2$ 的原纤维非空。故满 Minty 域和原两个坐标的满值域必须分开。

<a id="uc-critical-degree"></a>
## 5. UC-CRIT-v1：奇异线性方向可由 Hölder 恢复补回

- **Status**：`derived-checked`。这是第二轮正面攻击；没有把上一节的可逆性门当作理论极限。
- **Exact statement**：设有限维正交分解 $H=K\oplus E$，两块非零，$A=I_K\oplus A_E$，$B_E=I_E-A_E$ 可逆。固定 $0<\gamma<1,c>0,0\le\varepsilon<c,L,C_0\ge0$。假设一个**已经全域定义的连续** $C=Ap+N(p)$ 满足，写 $p=(k,e)$，

\[
 N_K(k,e)=-c\|k\|^{\gamma-1}k+R_K(k,e),
 \qquad\|R_K(k,e)\|\le\varepsilon\|k\|^\gamma+L\|e\|^\gamma+C_0,
 \tag{UC27}
\]
\[
 \|N_E(k,e)\|\le L(\|k\|^\gamma+\|e\|^\gamma)+C_0.
 \tag{UC28}
\]

零处径向恢复场取值 $0$。则 $T_-=I-C$ proper、满射，且

\[
 \deg(T_-)=\operatorname{sgn}\det B_E.
 \tag{UC29}
\]

因此原关系的全部逆纤维非空紧，虽然 $I-A$ 奇异。若另有 $I_E+A_E$ 可逆，则正向原纤维亦非空紧，因为 $N(p)=o(\|p\|)$ 且 $I+A$ 可逆。

**证明：两个尺度的边界。** 记 $m_E=\sigma_{\min}B_E>0$，选 $M>L/m_E$，令

\[
 \Omega_R=\{(k,e):\|k\|<R,\|e\|<MR^\gamma\}.
 \tag{UC30}
\]

把 $T_-$ 同伦到 $T_0(k,e)=(c\|k\|^{\gamma-1}k,B_Ee)$，即让 $R_K,N_E$ 同时乘 $\tau\in[0,1]$。在 $\|k\|=R$ 的边界，第一块范数至少

\[
 (c-\varepsilon)R^\gamma-LM^\gamma R^{\gamma^2}-C_0\longrightarrow\infty.
 \tag{UC31}
\]

在 $\|e\|=MR^\gamma$ 的边界，第二块范数至少

\[
 (m_EM-L)R^\gamma-LM^\gamma R^{\gamma^2}-C_0\longrightarrow\infty.
 \tag{UC32}
\]

二者统一于全部 $\tau$，因为 $\gamma^2<\gamma$。任一固定目标最终都不在同伦边界像内。径向 $k\mapsto c\|k\|^{\gamma-1}k$ 是方向保持同胚，其次数为 $1$；与 $B_E$ 的乘积给 (UC29)，继而满射。

**Properness 不只沿所选边界。** 若目标像保持有界，第二块先给 $m_E\|e\|\le L\|k\|^\gamma+L\|e\|^\gamma+C_1$。吸收次线性 $\|e\|^\gamma$ 后，$\|e\|\le C_2(1+\|k\|^\gamma)$。第一块再给

\[
 (c-\varepsilon)\|k\|^\gamma
 \le C_3+C_4\|k\|^{\gamma^2}.
\]

故 $k$ 有界，再得 $e$ 有界；连续性使有界目标集合的闭原像紧。

**可行的完整实例。** 在 $\mathbb R^2$ 取 $A=\operatorname{diag}(1,0)$、$\gamma=1/2$、$C(k,e)=(k-\operatorname{sgn}(k)\sqrt{|k|},0)$。则 $T_-=(\operatorname{sgn}(k)\sqrt{|k|},e)$ 是全域同胚，正逆全部纤维非空；$C-Ap$ 满足同常数 $\sqrt2$ 的标量 $1/2$-Hölder 预算，因而也属于 §3 的正核 profile。临界输入坐标上的零方程由次线性项恢复，不是靠 invertible $I-A$。原完整 PPA 动力学需要另外分析；本例仅认证覆盖与纤维。

**仍未解决的接口。** (UC27)–(UC28) 是额外的原生方向渐近条件。§3 的 Hilbert 扩张只保持差核，不自动保持这些条件；所以不能把 UC-EXT 与 UC-CRIT 直接合并成“任意此类局部图都有全部原纤维”。这正是继续研究的高价值门。

<a id="uc-helly-gate"></a>
## 6. UC-HEL-v1：凸截面的极大覆盖等价于有限锚准入

- **Status**：`derived-checked`，使用有限维 Helly 的标准机制；不认证新意。
- **Exact statement**：固定 $\mathbb R^n$，对每个输入差 $z$ 给非空紧凸反射增量截面 $\mathcal K_z\subset\mathbb R^n$，要求 $\mathcal K_0=\{0\}$、$\mathcal K_{-z}=-\mathcal K_z$。部分映射 $C$ 合法是 $C(p)-C(q)\in\mathcal K_{p-q}$ 对全部点对。以下三条等价：

1. 每个合法部分 $C$ 都能保持同一全部截面扩张到 $\mathbb R^n$。
2. 每个非空 graph-maximal 合法部分 $C$ 都具有全输入域。
3. 对每个 $1\le m\le n+1$、每个输入锚 $p_1,\ldots,p_m$、每组合法反射锚 $c_i-c_j\in\mathcal K_{p_i-p_j}$，以及每个新输入 $p$，都有

\[
 \bigcap_{i=1}^m[c_i+\mathcal K_{p-p_i}]\ne\varnothing.
 \tag{UC33}
\]

**证明。** 1⇒2 与前面的同输入排他相同。2⇒1：合法图按包含关系用 Zorn 得极大扩张；链之并的任何点对都位于一个链成员中，故仍合法；2 使该扩张全域。1⇒3 直接限制其全域扩张到新 $p$。最后 3 使任意部分图的每个新输入所对应的闭凸族 $c_q+\mathcal K_{p-q}$ 满足 Helly 的有限 $n+1$ 相交门，故每个有限子族相交。固定其中一个紧截面，紧性的有限交性质给全部截面共同相交，从而可加新点。再以 Zorn/逐点扩张完成全域。这证明 3⇒1。

这里的有限维 Helly 接口是：$\mathbb R^n$ 中有限闭凸族若每 $n+1$ 个有公共点，则整个有限族有公共点。紧截面负责从有限族转到无限族；若允许非紧截面，需要另外的 coercivity/有界锚，不能省略。

对 §2 的预算，$\mathcal K_z=\overline B(0,\omega(\|z\|))$，(UC33) 在 $m=2,p=1/2,p_1=0,p_2=1,c_1=0,c_2=\sqrt2$ 就失败。对 §3 的 profile，各截面为固定椭球和平移，Hilbert 核扩张证明 (UC33) 对所有锚成立。一般联合/方向预算若其反射截面并不凸或有空截面，则该有限 Helly 缩减不适用；不能直接套到一般半代数 feasibility certificate。

本等价把“每个极大图是否满域”变为原预算的有限新点准入性质。它不是把算法目标收缩写成假设：输入是原预算截面和有限原图兼容性，结论是真正的全图存在性。它也还不是一个便宜的算法；(UC33) 对锚位置和反射值都是全称量词。

<a id="uc-next"></a>
## 7. 已攻击仍未闭的高价值问题

### UC-Q1 · 平移不变凸方向预算的可扩张性分类

固定 $n\ge2$。设 $\mathcal K_z$ 是随 $z$ 连续的非空紧凸半代数集，$\mathcal K_0=\{0\},\mathcal K_{-z}=-\mathcal K_z$，并有 $\sup_{c\in\mathcal K_z}\|c\|\le L\|z\|^\gamma$，$0<\gamma\le1$。**问题**：刻画哪些这样的族满足 (UC33)，特别是是否每个可扩张族都能由 Hilbert 输入核、固定线性 target change、仿射中心和凸像投影组成。后一个表示目前没有证明，也没有用有限搜索冒充排除；若该表示不完备，要求一个不属于这些机制且满足 (UC33) 的精确族。

第一轮直接把 $\Omega_D$ 的有限/消失门当答案被 §2 否定；第二轮 Hilbert profile 给充分子类，但未证明必要。最小下一步是在 $n=2$ 检查三锚而非只检查两锚；纯径向类尚须分清平方核条件负定与实际向量可实现距离，不能把一个不条件负定的核自动判作不可扩张。

### UC-Q2 · 同预算扩张并保持临界恢复方向

固定 §3 的 mixed-power profile，$A=I_K\oplus A_E$，$I-A_E$ 可逆。给一张合法部分图，假设其 $N=C-Ap$ 在已表示域上满足 (UC27)–(UC28)，参数 $\varepsilon<c$。**问题**：给可由部分原图及有限锚验证的充要/可用充分条件，使存在一个全域同差核扩张，同时在全域满足同 $c,\varepsilon,L,C_0$（或精确可计算的最小放宽）恢复方向界。

目标不是仅造任意 completion，而是把 UC-EXT 的新输入覆盖与 UC-CRIT 的完整原输出覆盖接在**同一张图**上。普通球交可行只处理差预算；恢复条件在每个新输入再加位置依赖的 tube/cone 截面，交集可能为空。§3 的凸像投影只保持一个固定凸像集，不能直接保持随输入移动的非线性中心。即使某个全域恢复场本身属于 Hölder 类，也未证明它和任意已有图兼容。

### UC-Q3 · 预算 completion 与原完整零集/真 EB 的保真

固定一个有 bounded graph collar 的局部原图、原零集 $S$、真 EB $d(y,S)\le\psi(r_F(y))$ 和 §3 的方向 profile。**问题**：在不预先假设完整 $J$ 覆盖的情况下，给原图可检验条件，使某个同预算 completion 的目标输入球全部纤维落回原 collar，且该 completion 在所需输出窗与原 $F$ 相同；继而保持原真 EB 和原零目标。

§4 的相对极大性和 (UC25) 提供一个可用但可能过强的门。更弱的有限 boundary/exclusion 证书能否代替相对极大性仍未闭。关键量词是**每个**完整 completion 纤维点，而非找一支近处输出；若原图外还有兼容 remote branch，局部观测覆盖不能传成完整原关系覆盖。零集保真也受总次数限制，不能凭“同参数 completion”偷授。已有 [completion budget](../canonical/completion_budget_gate.md) 与 [full-fiber coverage](../canonical/full_fiber_coverage.md) 是相关工具，不是这个一般方向版本的完整答案。

这些问题的价值不同于重新命名一般模。UC-Q1 是原预算普适扩张几何；UC-Q2 是方向恢复与同预算扩张的兼容；UC-Q3 是原算法与 completion 的全部纤维保真。三者都可能产生真定理或真反例，当前都不宣称解决。

<a id="uc-evidence"></a>
## 8. 一手核验、复算和接收边界

一手比较已直接重开：Gárciga Otero–Iusem [2010-05-17作者10页稿](https://webdoc.sub.gwdg.de/ebook/serien/e/IMPA_A/672.pdf)，Definition 2 p.2、Proposition 5 p.5、Theorem 2 pp.6–7、Corollary 2 p.7；Evens–Pas–Latafat–Patrinos [2305.03605v2 HTML](https://arxiv.org/html/2305.03605v2)，Assumption I.a2、Proposition 4.12 及 Appendix B.2。前者的固定二次极大性借单调图双射得到合适参数的满射；后者也把同固定半单调极大性与合适步长下的完整 resolvent 满域相连。§2 不反驳这些定理：其图在更宽二次类中不极大，只在更严格的非线性原预算中极大。weak-Minty 的 Assumption I.a2 则仍是独立满域前件。

同常数 Hilbert 扩张接口依赖 [HE-EXTENSION](../canonical/holder_extension.md#he-extension) 已明确核验的 Azagra–Le Gruyer–Mudarra Theorem 1.2；本轮另直接读取 [arXiv:1810.10288v3](https://arxiv.org/pdf/1810.10288v3) 的 Theorem 2，PDF p.3 及同页证明：任意 Hilbert 源/目标、任意源子集、保持相同 Lipschitz 常数。这与本页 $J(D)\subset E$、目标 $H$、常数上界 $1$ 逐项匹配；常值退化可直接常值扩张。v3 的 Theorem 2 不混称出版版 Theorem 1.2。[2021出版页面](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/kirszbrauns-theorem-via-an-explicit-formula/15797B44C630B0E2A4BB12547759929D)仅用于核书目。本页没有从摘要导入附加保持性质。条件负定和 (UC18) 嵌入的承重推导已直接写在正文，未把未读的 Schoenberg 定理作为隐形一步。Bernstein 名称只是 (UC14) 的常用识别；本页仅使用已明确给定的正测度表示。

独占复算入口：

```text
python3 research/code/unified_ppa/coverage_verify.py
```

标准库、确定性、无 seed。精确 Fraction 检查 (UC6)/(UC7) 的平方形式、整数层图差、核失败 $3/8$、两球缺口的 $5/4<2$ 证书；有限浮点检查 critical product boundary 的增长及 native 完整模型反演。代码不证明 Zorn/Helly、全称核正性或全局次数，也不替代独立数学接收。

本次实际结果：2401 组精确平方等价、100 组显式预算逆函数、1764 组整数层图差全部通过；99 个非整数两球交点样本的最小 gap 为 $0.011124404043994285$；精确 midpoint 平方 gap 为 $3/4$，非条件负定二次型为 $3/8$；1089 个 critical 原生模型反演最大误差为 $0$。有限样本不替代 §2 的任意非整数新点排他与 §5 的无穷远增长证明。

交付范围核对：原预算固定性在 §2、§3 分别检查；全对量词与完整/窗口身份在 §1、§4 明列；真残差在 §2 取完整 infimum；§5 的方向条件不由扩张自动保持已明说；三轮路线从 naive maximality、正核 extension 到 critical restoration 的真实成功/失败均保存。本轮独立读者已全文冷读 UC1–33，未发现数学必须修补项；作者再逐段检查公式分隔、控制字符及 reader route。Markdown 内部研究稿无期刊格式、图注、Word 编辑身份或图像渲染要求。外部先行性仍未穷尽，闭合身份注册 C280/C281；末节 UC-Q1/Q2/Q3 保持 open，不认证外部首创。
