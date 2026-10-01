# RL 基础层冻结：定义、量词、Minty 域与代数字典

> Project: `monotonicity-regularity-seesaw-2026-09`  
> Paper family / stage / task: `T / T2 / RL-FND-DEF-01`  
> Status: **definition-layer freeze candidate**  
> Scope: 本文件只固定 RL 理论的对象、量词、域、存在性语言和基础代数。它不陈述或证明 PPA 收敛、收敛阶、sharpness、maximality 或新颖性。

## 0. 证据边界与使用规则

本文件综合并校正以下项目材料：

- `upload/01-RL_Submonotonicity-.md`；
- `research/rl_novelty_and_publication_assessment.md`；
- `work/rl_proof_referee.md`；
- `work/rl_exact_prior_art.md`；
- `work/rl_nearest_deepread.md`。

允许据此使用的主张只有三类：

1. 下列定义及其完整量词；
2. 由 Minty--Cayley 坐标和内积恒等式直接推出的等价关系；
3. 关于 restricted/full resolvent 的存在性与单值性的逻辑区分。

下列主张不在本文件中成立：RL 的定义级新颖性、RL 自动产生满域 resolvent、PPA 自动存在或收敛、指数乘积是精确阶、临界常数是 sharp、以及任意 maximal-extension 结论。

---

## 1. 统一符号与约定

### 1.1 空间、图与零点集

全文固定：

- $H$ 是实 Hilbert 空间；
- $F:H\rightrightarrows H$ 是任意集合值算子；
- $\lambda>0$ 是固定 Cayley/PPA 参数；
- 
  \[
  \operatorname{gph}F:=\{(u,u^*)\in H\times H:u^*\in F(u)\};
  \]
- 
  \[
  S:=F^{-1}(0)=\{u\in H:0\in F(u)\}.
  \]

除非另有明示，$S$ 总指全局零点集 $F^{-1}(0)$，不是 $S\cap U$ 或某个选定分支的零点集。

距离采用

\[
d(x,A):=\inf_{a\in A}\|x-a\|,
\qquad d(x,\varnothing):=+\infty.
\]

特别地，

\[
r_F(u):=d(0,F(u)),
\qquad r_F(u)=+\infty\quad\text{若 }F(u)=\varnothing.
\]

不默认 $S$ 闭、凸或 proximinal。若必须使用近似最近点，可写

\[
P_S^\varepsilon(x)
:=\{p\in S:\|x-p\|\le d(x,S)+\varepsilon\},
\qquad \varepsilon>0.
\]

只要 $S\ne\varnothing$，该集合非空；精确投影 $P_S(x)$ 只有在另有存在性保证时才使用。

### 1.2 Graph restriction

对任意 $\Gamma\subset\operatorname{gph}F$，称 $\Gamma$ 为一个 **restricted graph**。若 $U,W\subset H$，记

\[
\Gamma_{U,W}
:=\operatorname{gph}F\cap(U\times W)
=\{(u,u^*):u\in U,\ u^*\in F(u)\cap W\}.
\]

这同时限制 base variable 和 graph output。仅限制 $u\in U$ 的集合

\[
\operatorname{gph}F\cap(U\times H)
\]

是另一种 restriction；不得在未声明 $W=H$ 时把它与 $\Gamma_{U,W}$ 混用。

对 $\bar z=(\bar u,\bar u^*)\in\operatorname{gph}F$，本文件中的 **graph-local** 一律意为：存在 $\bar u$ 与 $\bar u^*$ 的邻域 $U,W$，并在 $\Gamma_{U,W}$ 上陈述性质。

---

## 2. Minty--Cayley 坐标与自然域

### Definition 2.1（Minty 与 reflected 坐标）

对 $z=(u,u^*)\in H\times H$，定义

\[
M_\lambda z:=u+\lambda u^*,
\qquad
C_\lambda z:=u-\lambda u^*.
\]

对 restricted graph $\Gamma\subset\operatorname{gph}F$，定义它的自然 Minty 域

\[
D_\lambda(\Gamma)
:=M_\lambda(\Gamma)
=\{u+\lambda u^*:(u,u^*)\in\Gamma\}.
\]

对 full graph，简记

\[
D_\lambda(F)
:=D_\lambda(\operatorname{gph}F)
=\operatorname{ran}(I+\lambda F).
\]

### Proposition 2.2（坐标重构）

对任意 $z=(u,u^*)$，令 $x=M_\lambda z$、$r=C_\lambda z$。则

\[
u=\frac{x+r}{2},
\qquad
u^*=\frac{x-r}{2\lambda}.
\]

因此 $z\mapsto(M_\lambda z,C_\lambda z)$ 是一一对应的线性坐标变换。

**Proof.** 将 $x=u+\lambda u^*$ 与 $r=u-\lambda u^*$ 相加、相减即可。 $\square$

### Definition 2.3（full resolvent relation 与 reflected relation）

不预设存在性或单值性，定义

\[
J_{\lambda F}(x)
:=(I+\lambda F)^{-1}(x)
=\{u\in H:x-u\in\lambda F(u)\},
\]

以及

\[
R_{\lambda F}(x)
:=\{2u-x:u\in J_{\lambda F}(x)\}.
\]

它们首先是 relations，并且

\[
\operatorname{dom}J_{\lambda F}
=\operatorname{dom}R_{\lambda F}
=D_\lambda(F).
\]

只有在已经证明取值唯一时，才把 $J_{\lambda F}$ 或 $R_{\lambda F}$ 当作映射书写。

### Definition 2.4（restricted resolvent relation）

对 $\Gamma\subset\operatorname{gph}F$，定义

\[
J_{\lambda,\Gamma}(x)
:=\{u:\exists u^*\text{ 使 }(u,u^*)\in\Gamma,
\ x=u+\lambda u^*\},
\]

\[
R_{\lambda,\Gamma}(x)
:=\{u-\lambda u^*:(u,u^*)\in\Gamma,
\ x=u+\lambda u^*\}.
\]

二者的 domain 都恰为 $D_\lambda(\Gamma)$。restricted relation 总是 full relation 的子 relation：

\[
J_{\lambda,\Gamma}(x)\subset J_{\lambda F}(x),
\qquad
R_{\lambda,\Gamma}(x)\subset R_{\lambda F}(x).
\]

### Proposition 2.5（relational fixed points）

若 relation 的 fixed-point set 定义为

\[
\operatorname{Fix}_{\mathrm{rel}}J
:=\{x:x\in J(x)\},
\]

则

\[
\operatorname{Fix}_{\mathrm{rel}}J_{\lambda F}=S.
\]

对 restricted graph，

\[
\operatorname{Fix}_{\mathrm{rel}}J_{\lambda,\Gamma}
=\{p:(p,0)\in\Gamma\}.
\]

**Proof.** $x\in J_{\lambda F}(x)$ 当且仅当 $x-x=0\in\lambda F(x)$。restricted 情形同理，并额外要求 $(x,0)\in\Gamma$。 $\square$

---

## 3. RL 的冻结定义：all-pairs、restricted、global、local 与 anchored

### 3.1 Cayley modulus 与 power specialization

称 $\omega:[0,+\infty)\to[0,+\infty)$ 为一个 **Cayley modulus**，如果它有限、非减，满足

\[
\omega(0)=0,
\qquad
\lim_{t\downarrow0}\omega(t)=0.
\]

本文件用 $\omega$ 表示 graph/Cayley 一侧的 modulus；后文用 $\psi$ 表示 error-bound/subregularity 一侧的 gauge。二者不得混用。

power modulus 为

\[
\omega_{L,\gamma}(t):=Lt^\gamma,
\qquad L>0,\quad 0<\gamma\le1.
\]

### Definition 3.1（restricted all-pairs $\omega$-RL）

给定非空 $\Gamma\subset\operatorname{gph}F$。称 $\Gamma$ 在参数 $\lambda$ 下满足 **restricted all-pairs $\omega$-RL**，若

\[
\boxed{
\forall (u,u^*)\in\Gamma\;
\forall (v,v^*)\in\Gamma:\quad
\|(u-v)-\lambda(u^*-v^*)\|
\le
\omega\!\left(\|(u-v)+\lambda(u^*-v^*)\|\right).
}
\tag{RL_{\Gamma,\omega}}
\]

等价地，量词是对 $\Gamma\times\Gamma$ 中的每一对 graph points，而不是“对某个 selection”或“存在一对有利 selections”。

若 $\omega(t)=Lt^\gamma$，称其满足

\[
\mathrm{RL}_\Gamma(\lambda,L,\gamma).
\]

“pairwise RL”和“all-pairs RL”在本文件中是同义词。

### Definition 3.2（global RL）

称 $F$ 满足 **global $\omega$-RL** 或 global $\mathrm{RL}(\lambda,L,\gamma)$，若 Definition 3.1 对

\[
\Gamma=\operatorname{gph}F
\]

成立。global 修饰的是 graph quantifier，不表示 $D_\lambda(F)=H$。

### Definition 3.3（graph-local all-pairs RL）

固定 $\bar z=(\bar u,\bar u^*)\in\operatorname{gph}F$。称 $F$ 在 $\bar z$ **graph-locally all-pairs $\omega$-RL**，若存在 $\bar u$、$\bar u^*$ 的邻域 $U,W$，使

\[
\Gamma_{U,W}=\operatorname{gph}F\cap(U\times W)
\]

非空，且

\[
\forall (u,u^*),(v,v^*)\in\Gamma_{U,W}:
\quad
\|C_\lambda(u,u^*)-C_\lambda(v,v^*)\|
\le
\omega\!\left(
\|M_\lambda(u,u^*)-M_\lambda(v,v^*)\|
\right).
\]

若使用 power modulus，则必须同时打印 $(\lambda,L,\gamma,U,W)$。未给出 $U,W$ 的“local RL”不是完整假设。

### Definition 3.4（Minty-input-local RL；不同概念）

给定 restricted graph $\Gamma$、$\bar x\in D_\lambda(\Gamma)$ 及 $\bar x$ 的邻域 $V$，令

\[
\Gamma\!\mid_V
:=\{z\in\Gamma:M_\lambda z\in V\}.
\]

若 RL 对 $\Gamma\!\mid_V$ 的所有 pairs 成立，称其为 **在已声明 graph restriction $\Gamma$ 上的 Minty-input-local RL**。

这不等同于 Definition 3.3。以后若 locality 是在 Minty input 上，必须打印 $\Gamma$ 与 $V$，不得只写“locally”。

### Definition 3.5（cross/anchored $\omega$-RL）

给定两个非空 graph subsets

\[
\Gamma_{\mathrm m},\Gamma_{\mathrm a}
\subset\operatorname{gph}F,
\]

分别称为 moving set 与 anchor set。称 $F$ 满足从 $\Gamma_{\mathrm m}$ 到 $\Gamma_{\mathrm a}$ 的 **anchored $\omega$-RL**，若

\[
\boxed{
\forall (u,u^*)\in\Gamma_{\mathrm m}\;
\forall (v,v^*)\in\Gamma_{\mathrm a}:\quad
\|(u-v)-\lambda(u^*-v^*)\|
\le
\omega\!\left(\|(u-v)+\lambda(u^*-v^*)\|\right).
}
\tag{A-RL}
\]

若 $\Gamma_{\mathrm a}=\{(\bar u,\bar u^*)\}$，称为 **point-anchored RL at $(\bar u,\bar u^*)$**。

### Definition 3.6（solution-anchored RL）

给定非空 $S_0\subset S$ 及 moving graph $\Gamma_{\mathrm m}\subset\operatorname{gph}F$。令

\[
Z(S_0):=\{(p,0):p\in S_0\}.
\]

称 $F$ 在 $(\Gamma_{\mathrm m},S_0)$ 上满足 **solution-anchored $\omega$-RL**，若

\[
\boxed{
\forall (u,u^*)\in\Gamma_{\mathrm m}\;
\forall p\in S_0:\quad
\|(u-p)-\lambda u^*\|
\le
\omega\!\left(\|(u-p)+\lambda u^*\|\right).
}
\tag{S-RL}
\]

“RL at $S$”不是完整写法；必须声明 moving graph $\Gamma_{\mathrm m}$ 和 anchor target $S_0$。若 $S_0=S\cap V$，邻域 $V$ 也必须打印。

### 3.2 量词之间的严格关系

以下关系由定义直接得到：

| 已知 | 可推出 | 不可据此推出 |
|---|---|---|
| all-pairs RL on $\Gamma$ | 任意 $\Gamma_{\mathrm m},\Gamma_{\mathrm a}\subset\Gamma$ 间的 anchored RL | graph 外的任何比较 |
| global all-pairs RL | 每个 restricted graph 上的 all-pairs RL | $D_\lambda(F)=H$ |
| graph-local all-pairs RL | 对同一 $\Gamma_{U,W}$ 内 anchors 的 anchored RL | global RL |
| solution-anchored RL | 当前 graph point 与声明零点 anchors 的比较 | moving points 彼此之间的 all-pairs RL |
| point-anchored RL | 与一个固定 graph point的比较 | Minty injectivity或 resolvent 单值性 |

因此 anchored、local、restricted 和 all-pairs 不是可互换形容词。

---

## 4. RL 的基础代数与 resolvent-side 表示

### Proposition 4.1（内积形式）

对任意两个 graph points，置

\[
a:=u-v,
\qquad b:=u^*-v^*,
\qquad t:=\|a+\lambda b\|.
\]

则 pairwise $\omega$-RL 精确等价于

\[
\boxed{
\lambda\langle a,b\rangle
\ge
\frac14\bigl(t^2-\omega(t)^2\bigr).
}
\tag{RL\text{-}IP_\omega}
\]

power 情形为

\[
\boxed{
\lambda\langle a,b\rangle
\ge
\frac14\left(
\|a+\lambda b\|^2
-L^2\|a+\lambda b\|^{2\gamma}
\right).
}
\tag{RL-IP}
\]

**Proof.** 恒等式

\[
\|a-\lambda b\|^2
=\|a+\lambda b\|^2-4\lambda\langle a,b\rangle
\]

把 RL 平方后恰好给出所述不等式；两边均非负，反向同样成立。 $\square$

### Proposition 4.2（all-pairs RL 强制 restricted Minty injectivity）

若 $\Gamma$ 满足 all-pairs $\omega$-RL，则

\[
M_\lambda\mid_\Gamma:\Gamma\to D_\lambda(\Gamma)
\]

是单射。

**Proof.** 若 $M_\lambda z=M_\lambda z'$，RL 的右端为 $\omega(0)=0$，故 $C_\lambda z=C_\lambda z'$。由 Proposition 2.2 的坐标重构得 $z=z'$。 $\square$

### Corollary 4.3（restricted $J$ 与 $R$ 是自然域上的 maps）

若 $\Gamma$ 满足 all-pairs $\omega$-RL，则 $J_{\lambda,\Gamma}$ 和 $R_{\lambda,\Gamma}$ 在 $D_\lambda(\Gamma)$ 上均为单值映射，并且

\[
R_{\lambda,\Gamma}=2J_{\lambda,\Gamma}-I.
\]

此外，

\[
\boxed{
\forall x,y\in D_\lambda(\Gamma):\quad
\|R_{\lambda,\Gamma}x-R_{\lambda,\Gamma}y\|
\le\omega(\|x-y\|).
}
\tag{R_\omega}
\]

反之，若 $M_\lambda\mid_\Gamma$ 已知为单射，且由此定义的
$R_{\lambda,\Gamma}$ 满足式 $(R_\omega)$，则 $\Gamma$ 满足
all-pairs $\omega$-RL。

**Proof.** 单值性由 Proposition 4.2。若 $x=M_\lambda(u,u^*)$，则 $R_{\lambda,\Gamma}x=C_\lambda(u,u^*)$；将两个 graph points 代入即得双向等价。 $\square$

### Corollary 4.4（global RL 的准确 resolvent 结论）

若 $F$ global all-pairs $\omega$-RL，则 full relations $J_{\lambda F}$、$R_{\lambda F}$ 在其自然域

\[
D_\lambda(F)=\operatorname{ran}(I+\lambda F)
\]

上是单值 maps，并且 $R_{\lambda F}$ 在该域满足式 $(R_\omega)$。

此结论不含 $D_\lambda(F)=H$。

### Proposition 4.5（Cayley pullback）

给定任意 $D\subset H$ 和映射 $R:D\to H$，定义

\[
\Gamma_R^\lambda
:=\left\{
\left(
\frac{x+Rx}{2},
\frac{x-Rx}{2\lambda}
\right):x\in D
\right\}.
\]

则

\[
D_\lambda(\Gamma_R^\lambda)=D,
\qquad
R_{\lambda,\Gamma_R^\lambda}=R.
\]

并且

\[
\Gamma_R^\lambda\text{ satisfies all-pairs }\omega\text{-RL}
\iff
\|Rx-Ry\|\le\omega(\|x-y\|)
\quad(\forall x,y\in D).
\]

**Proof.** 对定义中的 graph point 直接计算 $M_\lambda=x$ 与 $C_\lambda=Rx$，再用 Definition 3.1。 $\square$

该命题说明：RL 在 map side 就是自然 Minty 域上的普通 modulus/Hölder continuity。operator-side 理论若要有额外内容，必须来自 graph 结构、domain/range、calculus、regularity interaction 或 sharp realizability，而不是坐标改写本身。

### Proposition 4.6（firm-type 恒等式；coupled selections）

设 $M_\lambda\mid_\Gamma$ 是单射，并令
$T:=J_{\lambda,\Gamma}:D_\lambda(\Gamma)\to H$。则 $\Gamma$ 上的
all-pairs $\omega$-RL 精确等价于

\[
\boxed{
\|Tx-Ty\|^2
+\|(I-T)x-(I-T)y\|^2
\le
\frac12\left(
\|x-y\|^2+\omega(\|x-y\|)^2
\right)
}
\tag{F_\omega}
\]

对所有 $x,y\in D_\lambda(\Gamma)$ 成立。特别地，all-pairs RL 本身由
Proposition 4.2 保证上述单射前提。power 情形的右端为

\[
\frac12\left(\|x-y\|^2+L^2\|x-y\|^{2\gamma}\right).
\]

**Proof.** 令 $a=Tx-Ty$、$\lambda b=(I-T)x-(I-T)y$。则 $x-y=a+\lambda b$，而 $R_{\lambda,\Gamma}x-R_{\lambda,\Gamma}y=a-\lambda b$。平行四边形恒等式给出

\[
\|a\|^2+\|\lambda b\|^2
=\frac12\left(\|a+\lambda b\|^2+\|a-\lambda b\|^2\right),
\]

再用 Corollary 4.3。反向由同一恒等式恢复 reflected bound。 $\square$

若 $T$ 尚被视为 relation，则式 $(F_\omega)$ 的唯一无歧义 relational
版本是：

\[
\forall x,y\in D\;
\forall u\in T(x)\;
\forall v\in T(y):
\]

\[
\|u-v\|^2
+\|(x-u)-(y-v)\|^2
\le
\frac12\left(\|x-y\|^2+\omega(\|x-y\|)^2\right).
\tag{coupled-F}
\]

同一个 $u$ 必须同时出现在 $u-v$ 与 $x-u$ 中，同一个 $v$ 亦然。取 $x=y$ 可知 (coupled-F) 本身强迫 $u=v$，所以它使 relation 在 $D$ 上单值。

因此“multivalued $T$ 按 selection-wise AFNE 解释”不再采用：

- 若意思是对所有 coupled selections，则性质已经强迫单值；
- 若意思是存在有利 selections，则它不等价于 all-pairs RL。

本文建议把式 $(F_\omega)$ 称为 **RL 的 firm-type characterization**，不把 “additive firm nonexpansiveness” 当作独立假设或独立新对象。

---

## 5. Restricted branch、full relation、coverage 与 exclusion

### Definition 5.1（input coverage）

给定 $\Gamma\subset\operatorname{gph}F$ 与 $E\subset H$。称 $\Gamma$ **covers $E$ in Minty input**，若

\[
E\subset D_\lambda(\Gamma).
\tag{Coverage}
\]

若 $E=B(\bar x,r)$，这才是“local resolvent 在 $\bar x$ 附近处处存在”的明确 range 假设。

### Definition 5.2（named restricted resolvent branch）

若 $\Gamma$ all-pairs RL 且 $E\subset D_\lambda(\Gamma)$，定义

\[
T_{\Gamma,E}
:=J_{\lambda,\Gamma}\mid_E:E\to H.
\]

它是 full relation $J_{\lambda F}$ 的一个指定单值 selection，称为 **named restricted resolvent branch**。

这一定义只表示每个 $x\in E$ 有唯一的 $\Gamma$-graph realization；它不表示 full relation 在 $E$ 上没有其他、位于 $\Gamma$ 外的 selections。

### Definition 5.3（branch exclusion）

称 $\Gamma$ 在输入集 $E$ 上满足 **branch exclusion**，若

\[
\boxed{
\{z\in\operatorname{gph}F:M_\lambda z\in E\}
\subset\Gamma.
}
\tag{Exclusion}
\]

### Proposition 5.4（restricted branch 何时等于 full resolvent）

若

1. $\Gamma$ all-pairs RL；
2. $E\subset D_\lambda(\Gamma)$；
3. $\Gamma$ 在 $E$ 上满足 branch exclusion；

则

\[
\forall x\in E:\qquad
J_{\lambda F}(x)=\{T_{\Gamma,E}(x)\},
\]

且 full $R_{\lambda F}$ 在 $E$ 上也等于 restricted $R_{\lambda,\Gamma}$。

**Proof.** Coverage 给出至少一个 $\Gamma$-realization；exclusion 迫使 full graph 中同一输入的每个 realization 都属于 $\Gamma$；Proposition 4.2 再给唯一性。 $\square$

### 5.1 三个必须分开的性质

对一个 local branch，以下三项互不替代：

1. **uniqueness on the restricted range**：由 all-pairs RL 推出；
2. **input coverage**：必须由 $E\subset D_\lambda(\Gamma)$ 另行假设或证明；
3. **full-branch exclusion**：必须由 (Exclusion) 另行假设或证明。

若以后迭代 $T_{\Gamma,E}$，还需另行检查 self-map/invariance，例如

\[
T_{\Gamma,E}(E)\subset E
\]

或更一般的 outer/inner localization margin。RL 定义本身不含此性质。

---

## 6. Gauge 与 power metric subregularity 的冻结 convention

### Definition 6.1（error-bound gauge）

给定 $\eta_\psi\in(0,+\infty]$。称

\[
\psi:[0,\eta_\psi)\to[0,+\infty)
\]

为一个 **error-bound gauge**，若它有限、非减，并满足

\[
\psi(0)=0,
\qquad
\lim_{t\downarrow0}\psi(t)=0.
\]

右连续性不是本定义的必要部分。若后续需要用 asymptotic equivalent 替换 $\psi$，应另加右连续性或使用单调右包络。

### Definition 6.2（local gauge metric subregularity at $(\bar u,0)$）

固定 $\bar u\in S$，并固定 Definition 6.1 的 gauge
$\psi:[0,\eta_\psi)\to[0,+\infty)$。称 $F$ 在 $(\bar u,0)$ 对
$0$ 满足 **local gauge metric subregularity with gauge $\psi$**，若存在
$\bar u$ 的邻域 $U$ 和常数 $\delta\in(0,\eta_\psi)$，使

\[
\boxed{
\forall u\in U\text{ with }r_F(u)<\delta:\quad
d(u,S)\le\psi(r_F(u)).
}
\tag{GMSR}
\]

这里左端默认使用全局 $S=F^{-1}(0)$。若理论需要指定 target subset $S_0\subset S$，必须另写

\[
d(u,S_0)\le\psi(r_F(u))
\tag{GMSR_{S_0}}
\]

并称其为 **target-set error bound relative to $S_0$**。除非 $S_0$ 与 $S$ 在 $U$ 中局部一致，不把它静默称为标准 metric subregularity。

### Definition 6.3（power metric subregularity；指数在 residual 上）

取

\[
\psi(t)=\rho t^q\quad(t\ge0),
\qquad \rho>0,\quad q>0.
\]

Definition 6.2 变为

\[
\boxed{
\exists U\ni\bar u,\ \exists\delta>0,\ \exists\rho>0:\quad
\forall u\in U\text{ with }r_F(u)<\delta,
\quad
d(u,S)\le\rho\,r_F(u)^q.
}
\tag{MSR_q}
\]

本项目固定采用“幂在 residual 上”的 convention。也就是说，$q$ 是

\[
d(u,S)\lesssim d(0,F(u))^q
\]

中的指数；不得把文献中

\[
d(u,S)^\alpha\lesssim d(0,F(u))
\]

或 Hölder order $\omega\in(0,1]$ 的指数不经倒数换算直接记作同一个
$q$。

当前研究关注的 $q>1$ 是 stronger-than-linear residual error bound。这个取值范围是研究对象，不写入一般 Definition 6.3，也不把 $q\ge1/\gamma$ 当作定义的一部分。

### 6.1 该定义不提供什么

由于 $r_F(u)=+\infty$ 当 $F(u)=\varnothing$，(GMSR) 在这些点不施加约束。因此：

- metric subregularity 不推出 $u\in\operatorname{dom}F$；
- 不推出 $x\in\operatorname{ran}(I+\lambda F)$；
- 不推出 resolvent branch 存在；
- 不推出 $S$ 闭、graph 闭或 limit membership。

同一个 $(q,\rho)$ 必须在声明的 $U$ 上统一有效。沿每个点分别选取不同
$\rho(u)$ 不属于上述定义。

---

## 7. $\gamma=1$ 的 tied semimonotonicity 字典

### Definition 7.1（restricted $(\mu,\rho)$-semimonotonicity）

给定 $\Gamma\subset\operatorname{gph}F$ 与 $\mu,\rho\in\mathbb R$。称 $F$ 在 $\Gamma$ 上 $(\mu,\rho)$-semimonotone，若

\[
\forall (u,u^*),(v,v^*)\in\Gamma:\quad
\langle u-v,u^*-v^*\rangle
\ge
\mu\|u-v\|^2+\rho\|u^*-v^*\|^2.
\tag{SM}
\]

### Proposition 7.2（RL 的 Lipschitz endpoint 是 tied curve）

固定 $L>0$，定义

\[
\theta_L:=\frac{1-L^2}{2(1+L^2)},
\qquad
\mu_L:=\frac{\theta_L}{\lambda},
\qquad
\rho_L:=\lambda\theta_L=\lambda^2\mu_L.
\]

则对同一个 restricted graph $\Gamma$，下列条件精确等价：

1. $\Gamma$ 满足 $\mathrm{RL}_\Gamma(\lambda,L,1)$；
2. $F$ 在 $\Gamma$ 上 $(\mu_L,\rho_L)$-semimonotone；
3. 对 $A=\lambda F$ 的相应 scaled graph，
   
   \[
   \langle a,c\rangle
   \ge
   \theta_L(\|a\|^2+\|c\|^2),
   \qquad c=\lambda b.
   \]

**Proof.** 展开

\[
\|a-\lambda b\|^2\le L^2\|a+\lambda b\|^2
\]

并把内积项移到右侧，得到

\[
\langle a,b\rangle
\ge
\frac{1-L^2}{2\lambda(1+L^2)}\|a\|^2
+\frac{\lambda(1-L^2)}{2(1+L^2)}\|b\|^2.
\]

这正是 $(\mu_L,\rho_L)$，反向展开相同。乘以 $\lambda$ 并置 $c=\lambda b$ 得第三式。 $\square$

### Proposition 7.3（Luke--Tam 参数换算）

当 $L\ge1$ 时，令

\[
\tau_L:=\frac{L^2-1}{4}\ge0.
\]

则 $\mathrm{RL}_\Gamma(\lambda,L,1)$ 精确等价于

\[
\boxed{
\lambda\langle a,b\rangle
\ge
-\tau_L\|a+\lambda b\|^2.
}
\tag{LT-SM}
\]

**Proof.** 在 Proposition 4.1 中令 $\gamma=1$，得到

\[
\lambda\langle a,b\rangle
\ge\frac{1-L^2}{4}\|a+\lambda b\|^2.
\]

代入 $\tau_L$ 即得。 $\square$

参数区域为：

| $L$ | $\theta_L$ | graph-side 位置 |
|---:|---:|---|
| $0<L<1$ | $>0$ | positive equal-parameter semimonotonicity；reflected map contraction |
| $L=1$ | $=0$ | ordinary monotonicity；reflected map nonexpansive |
| $L>1$ | $<0$ | negative tied semimonotonicity；Luke--Tam 型 nonnegative violation |

因此 $\gamma=1$ 分支不作为新定义主张。上述只是已有 semimonotonicity/submonotonicity 的 exact parameter dictionary。文献中特定命题可能另有限维、maximality、restricted-domain 或 $\tau<1/2$ 等假设；本文件的纯代数等价不自动扩张那些已发表定理的适用范围。

---

## 8. Inverse 与 output scaling

### Definition 8.1（inverse graph 与 output scaling）

对 $\Gamma\subset H\times H$ 与 $c>0$，记

\[
\Gamma^{-1}:=\{(u^*,u):(u,u^*)\in\Gamma\},
\]

\[
c\Gamma:=\{(u,cu^*):(u,u^*)\in\Gamma\}.
\]

若 $\Gamma\subset\operatorname{gph}F$，则

\[
\Gamma^{-1}\subset\operatorname{gph}F^{-1},
\qquad
c\Gamma\subset\operatorname{gph}(cF).
\]

### Proposition 8.2（inverse rule）

对 $L>0$、$0<\gamma\le1$，

\[
\boxed{
\Gamma\text{ satisfies }\mathrm{RL}(\lambda,L,\gamma)
\iff
\Gamma^{-1}\text{ satisfies }
\mathrm{RL}\!\left(\lambda^{-1},L\lambda^{\gamma-1},\gamma\right).
}
\tag{Inv}
\]

同一规则适用于 anchored RL，只需同时把 moving set 和 anchor set取 inverse。

**Proof.** 对 inverse graph，差分变为 $(b,a)$。于是

\[
\|b-\lambda^{-1}a\|
=\lambda^{-1}\|a-\lambda b\|,
\]

\[
\|b+\lambda^{-1}a\|^\gamma
=\lambda^{-\gamma}\|a+\lambda b\|^\gamma.
\]

比较系数得到新常数 $L\lambda^{\gamma-1}$；反向应用同一计算。 $\square$

当 $\gamma=1$ 时 inverse 保持 $L$；当 $0<\gamma<1$ 时 $L$ 随 $\lambda$ 和单位缩放，不能脱离参数比较其数值大小。

### Proposition 8.3（positive output-scaling rule）

对任意 $c>0$，

\[
\boxed{
\Gamma\text{ satisfies }\mathrm{RL}(\lambda,L,\gamma)
\iff
c\Gamma\text{ satisfies }
\mathrm{RL}(\lambda/c,L,\gamma).
}
\tag{Scale}
\]

因此在 full graph 层面，

\[
F\in\mathrm{RL}(\lambda,L,\gamma)
\iff
cF\in\mathrm{RL}(\lambda/c,L,\gamma).
\]

**Proof.** 在 $c\Gamma$ 上 output difference 是 $cb$，而

\[
(\lambda/c)(cb)=\lambda b.
\]

故 RL 两侧与原式逐项相同。 $\square$

该命题要求 resolvent parameter 与 output scaling 同时改变。固定 $\lambda$ 后把 $F$ 换成 $cF$，并不存在“自动保持同一个 RL certificate”的额外结论；正确比较应回到参数 $c\lambda$ 或 $\lambda/c$ 的明确换算。

---

## 9. 明确排除的伪结论与最小反例

下表是本基础层的强制边界。

| 伪结论 | 状态 | 最小理由或反例 |
|---|---|---|
| restricted all-pairs RL $\Rightarrow$ Minty input neighborhood coverage | **False** | $\Gamma=\{(0,0)\}$ 满足任意 RL，但 $D_\lambda(\Gamma)=\{0\}$。 |
| restricted all-pairs RL $\Rightarrow$ full resolvent 在 restricted range 上单值 | **False** | 在 $H=\mathbb R$ 取 $\Gamma=\{(0,0)\}$，并令 full graph 另含 $(1,-1/\lambda)$。两点的 Minty input 都是 $0$，故 $J_{\lambda F}(0)\supset\{0,1\}$，而 restricted $J_{\lambda,\Gamma}(0)=0$。 |
| point-/solution-anchored RL $\Rightarrow$ moving graph 上 Minty injectivity | **False** | 在 $H=\mathbb R$ 取 solution-anchor target $S_0=\{0\}$，moving points 取 $(1,0)$ 与 $(0,1/\lambda)$。二者对 anchor $(0,0)$ 均满足 $L=1$ 的任意 power anchored bound，但 Minty input 同为 $1$，graph points 不同。 |
| gauge/power subregularity $\Rightarrow$ resolvent 存在 | **False** | 令 $F(0)=\{0\}$，且 $F(u)=\varnothing$ 对 $u\ne0$。任意 power bound 在 $0$ 附近按本 convention 成立，但 $D_\lambda(F)=\{0\}$。 |
| global RL $\Rightarrow D_\lambda(F)=H$ | **False** | 同一 singleton graph 反例已足够；global 只表示量词覆盖 full graph。 |
| RL $\Rightarrow$ graph closed、zero set closed、maximality或 range closed | **False / not established** | RL 是 pairwise increment inequality，不含任何闭性或 maximal-extension假设。 |
| local RL + local subregularity $\Rightarrow$ branch self-map/invariance | **False / separate task** | locality 只规定当前有效 graph/window；是否离开 window 取决于另行的 coverage 与 margin。 |
| $\mathrm{RL}(\lambda,L,\gamma)$ 中打印的 $\gamma$ 自动是 optimal exponent | **False** | 在有界 Minty 域上，$K$-Lipschitz $R$ 对任意 $0<\gamma<1$ 都满足 Hölder bound $K\Delta^{1-\gamma}t^\gamma$，其中 $\Delta=\operatorname{diam}D$。 |
| firm-type formula 是独立于 RL 的第二个新假设 | **False** | Proposition 4.6 表明它只是同一 Cayley inequality 的平行四边形重写。 |
| $\gamma=1$ 是新的 generalized monotonicity class | **False** | Proposition 7.2--7.3 给出 tied semimonotonicity 与 Luke--Tam 参数的 exact dictionary。 |
| power subregularity指数 $q$ 自动是 sharp，或与 $\gamma$ 自动形成 exact orbit order | **Not a theorem here** | Definition 6.3 只是 upper error-bound certificate；sharpness与算法轨道均属后续理论。 |

### 9.1 Bounded-domain Hölder 弱化的计算

若 $R:D\to H$ 是 $K$-Lipschitz 且 $\operatorname{diam}D\le\Delta<\infty$，则对 $0<\gamma<1$，

\[
\|Rx-Ry\|
\le K\|x-y\|
\le K\Delta^{1-\gamma}\|x-y\|^\gamma.
\]

所以一个 local/subunit RL certificate 本身不证明 reflected geometry genuinely non-Lipschitz，也不证明 $\gamma$ sharp。

---

## 10. 后续所有 RL 定理的最小声明清单

任何使用本基础层的后续定理，至少必须显式声明下列数据；缺一项时不得用一句“充分局部”代替。

| 层 | 必须打印的数据 |
|---|---|
| Ambient | 实 Hilbert 空间 $H$、算子 $F$、参数 $\lambda$ |
| Graph geometry | full graph 或具体 $\Gamma$；all-pairs 或 anchored；若 local，给 $U,W$ 或 Minty neighborhood $V$ |
| RL certificate | $\omega$，或 $L,\gamma$，以及它对哪些 ordered/cross pairs 成立 |
| Natural domain | $D_\lambda(\Gamma)$；若需要输入邻域，明确写 coverage $E\subset D_\lambda(\Gamma)$ |
| Algorithmic object | full $J_{\lambda F}$ 还是 named $T_{\Gamma,E}$ |
| Branch status | 是否只迭代 restricted branch；若声称 full resolvent 唯一，给 branch exclusion |
| Regularity | reference $(\bar u,0)$、target $S$ 或显式 $S_0$、邻域 $U$、residual window $\delta$、统一 gauge/常数 |
| Set geometry | 是否需要 $S$ 闭、局部一致、投影存在或仅用 $\varepsilon$-nearest anchors |
| Localization | self-map、outer/inner radii或 step-budget margin；不得从 distance-to-$S$ closeness 自动推断 |
| Claim strength | upper guarantee、exact order、necessary condition 与 sharp constant 必须分别标注 |

以下写法从本文件起停用：

- “当 $J$ 多值时按 selection-wise 解释”；
- “$F$ locally RL”但不写 graph/Minty localization；
- 在只有 restricted RL 时写任意 $x^+\in J_{\lambda F}(x)$；
- 把 $D_\lambda(\Gamma)$ 默认为 $H$；
- 把 anchored RL 当作 all-pairs RL；
- 把 $d(u,S)\le\rho d(0,F(u))^q$ 当作 resolvent existence 条件；
- 未证明 optimality 时称 $\gamma$、$q$、$\gamma q$ 或某个常数为 sharp。

---

## 11. Specialist findings、限制与质量检查

### Specialist findings

1. RL 最稳定的基础对象是 restricted graph $\Gamma$ 上的 Cayley-modulus inequality；global、local 与 anchored 都应由 $\Gamma$ 和 pair quantifier 派生，而不是另行依赖含糊文字。
2. all-pairs RL 的直接结构后果恰是 $M_\lambda\mid_\Gamma$ 单射，以及 restricted reflector 在 $D_\lambda(\Gamma)$ 上具有 modulus $\omega$。
3. existence、coverage、full-branch uniqueness 与 self-map 是四个不同问题；只有 restricted uniqueness 来自 RL。
4. gauge/power subregularity固定采用 residual-side exponent，并明确保留空值处的 vacuity。
5. $\gamma=1$ 已精确落在 tied semimonotonicity 曲线上；这一分支应作为边界校准，而非定义级新颖性。

### Limitations and risks

- 本文件没有核验新的外部文献，也不解决 Moursi--Vanderwerff 2025 的全文风险。
- 本文件没有建立 RL maximal extension、surjectivity、closedness 或 calculus。
- 本文件没有选择最终论文究竟以 all-pairs class 还是 solution-anchored algorithmic hypothesis 为主；它只保证二者以后不再混写。
- 本文件没有证明任何 PPA recurrence、invariance、limit membership、rate 或 sharpness。

### Quality checks completed

- [x] 每个 RL 定义均打印了 graph sets 与完整 universal quantifiers；
- [x] graph-local 与 Minty-input-local 分开；
- [x] anchored 与 all-pairs 分开；
- [x] full relation 与 restricted branch 分开；
- [x] existence、single-valuedness、coverage、exclusion 与 self-map 分开；
- [x] multivalued firm-type formula改为 coupled-selection量词，并证明其强迫单值；
- [x] gauge/power subregularity固定 residual-side exponent convention；
- [x] $\gamma=1$ 参数由原式重新展开核算；
- [x] inverse/scaling公式逐项核算；
- [x] 使用 Python 内置 Fraction 对 RL--IP、firm identity 与
  $\gamma=1$ tied coefficients 作 exact arithmetic 复算，并对 inverse
  coefficient 作多参数数值复算；全部 assertions 通过；
- [x] 每个 proposition 均附最短闭合证明；
- [x] 未写收敛证明，未修改 RL 主文件；
- [x] 未把阴性检索、新颖性、sharpness或期刊层级写成已证事实。

---

## 12. SCI-Skills Expert Contract 1.0

```yaml
contract_version: "1.0"
expert_skill: "sci-skills-manuscript-writing"
project_id: "monotonicity-regularity-seesaw-2026-09"
paper_family: "T"
stage_id: "T2"
task_id: "RL-FND-DEF-01"
task_status: "COMPLETE"
inputs_reviewed:
  - "upload/01-RL_Submonotonicity-.md"
  - "research/rl_novelty_and_publication_assessment.md"
  - "work/rl_proof_referee.md"
  - "work/rl_exact_prior_art.md"
  - "work/rl_nearest_deepread.md"
outputs:
  - "work/rl_foundations_definitions.md"
evidence_status:
  - label: "VERIFIED_USER_MATERIAL"
    item: "RL/IP algebra, draft definitions, and stated PPA-side conventions were reviewed from the supplied project files."
  - label: "AI_INFERENCE"
    item: "Minty injectivity, restricted/full branch logic, coupled-selection formulation, inverse/scaling rules, and minimal counterexamples were rederived directly."
  - label: "VERIFIED_USER_MATERIAL"
    item: "The reviewed project reports record full-text source support for the gamma=1 tied semimonotonicity/Luke-Tam positioning; this bounded task did not independently repeat that external-source audit."
  - label: "EXECUTED_LOCAL"
    item: "Built-in Python exact-rational assertions passed for RL-IP, the firm identity, and gamma=1 tied coefficients; multi-parameter numerical assertions passed for the inverse coefficient."
  - label: "PENDING_VERIFICATION"
    item: "No global novelty conclusion is made; the unresolved nonlinear-modulus and Moursi-Vanderwerff full-text audit remains outside this task."
assumptions:
  - "All displayed geometry is over a real Hilbert space."
  - "The five reviewed project files accurately record their cited-source access depth."
  - "RL is treated as a working internal label; final public nomenclature is not fixed here."
author_input_needed: []
manual_actions: []
quality_checks:
  - "Complete graph and selection quantifiers printed for every RL variant."
  - "Global, restricted, graph-local, Minty-local, anchored, and all-pairs notions separated."
  - "Natural Minty domains and relational resolvents defined before map notation is used."
  - "Existence, restricted single-valuedness, full-branch exclusion, and self-map status separated."
  - "Gauge and power subregularity conventions fixed with empty-value behavior explicit."
  - "gamma=1, inverse, and scaling identities independently rederived."
  - "Exact-rational and multi-parameter coefficient checks executed locally and passed."
  - "Every proposition includes a concise proof."
  - "No convergence proof and no modification of the main RL draft."
conflicts:
  - conflict_id: "RL-FND-C01"
    conflict_type: "quantifier"
    claim: "The draft's multivalued selection-wise AFNE wording can represent all-pairs RL."
    source_or_locator: "upload/01-RL_Submonotonicity-.md, Definition 2; work/rl_proof_referee.md, Section 2"
    competing_values_or_interpretations:
      - "For-all coupled selections, which already forces single-valuedness."
      - "Exists-selection wording, which is not equivalent to all-pairs RL."
    recommended_resolution: "Adopt Proposition 4.6 and retire unqualified selection-wise wording."
  - conflict_id: "RL-FND-C02"
    conflict_type: "domain"
    claim: "Local RL allows unrestricted use of the full resolvent near a solution."
    source_or_locator: "upload/01-RL_Submonotonicity-.md, Theorems 1-3; work/rl_proof_referee.md, Sections 4-5"
    competing_values_or_interpretations:
      - "Restricted RL gives a unique named branch only on its Minty range."
      - "Full-resolvent existence and uniqueness require coverage and exclusion."
    recommended_resolution: "Use Definitions 5.1-5.3 in every later theorem."
conflict_resolution_status: "UNRESOLVED"
merge_permission: "orchestrator_only"
stage_acceptance_recommendation: "REPAIR"
recommended_next_action: "由独立 proof-referee 对本定义层做一次逐量词反向压力测试；通过后再由 orchestrator 合并进 RL 基础理论主稿。"
```
