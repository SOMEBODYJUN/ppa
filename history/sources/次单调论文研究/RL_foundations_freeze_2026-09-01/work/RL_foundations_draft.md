# RL 基础理论 canonical draft

> 内部基础稿；暂不做语言润色。RL 是项目内部代号，正式公开命名尚未锁定。本文只组织可由所给材料支持的定义、代数与条件定理，不主张新颖性、最大性或文献优先权。

## 0. 范围与统一约定

全文令 \(H\) 为实 Hilbert 空间，\(F:H\rightrightarrows H\)，
\(\lambda>0\)，并记

\[
\operatorname{gph}F:=\{(u,u^*)\in H\times H:u^*\in F(u)\},
\qquad
S:=F^{-1}(0).
\]

对 \(A\subset H\)，

\[
d(x,A):=\inf_{a\in A}\|x-a\|,
\qquad d(x,\varnothing):=+\infty,
\]

并令

\[
r_F(u):=d(0,F(u)).
\]

不默认 \(S\) 闭、凸或 proximinal。若 \(S\ne\varnothing\) 且
\(\varepsilon>0\)，记

\[
P_S^\varepsilon(x)
:=\{p\in S:\|x-p\|\le d(x,S)+\varepsilon\};
\]

该集合总非空。只有在最近点确实存在时才写
\(P_S(x):=P_S^0(x)\)。

### Definition 0.1（Minty--Cayley 坐标）

对 \(z=(u,u^*)\in H\times H\)，定义

\[
M_\lambda z:=u+\lambda u^*,
\qquad
C_\lambda z:=u-\lambda u^*.
\]

于是，若 \(x=M_\lambda z\)、\(r=C_\lambda z\)，则

\[
u=\frac{x+r}{2},
\qquad
u^*=\frac{x-r}{2\lambda}.
\tag{0.1}
\]

对任意 graph restriction \(\Gamma\subset\operatorname{gph}F\)，定义

\[
D_\lambda(\Gamma):=M_\lambda(\Gamma).
\]

空 restriction 允许出现，并约定 \(D_\lambda(\varnothing)=\varnothing\)。

### Definition 0.2（full relation 与 restricted relation）

full resolvent 与 reflector 首先是 relations：

\[
J_{\lambda F}(x)
:=\{u:x-u\in\lambda F(u)\},
\qquad
R_{\lambda F}(x)
:=\{2u-x:u\in J_{\lambda F}(x)\}.
\]

其共同自然域为

\[
D_\lambda(F):=\operatorname{ran}(I+\lambda F).
\]

对 \(\Gamma\subset\operatorname{gph}F\)，定义

\[
J_{\lambda,\Gamma}(x)
:=\{u:\exists u^*,\ (u,u^*)\in\Gamma,\ x=M_\lambda(u,u^*)\},
\]

\[
R_{\lambda,\Gamma}(x)
:=\{C_\lambda(u,u^*):(u,u^*)\in\Gamma,\ x=M_\lambda(u,u^*)\}.
\]

二者的自然域均为 \(D_\lambda(\Gamma)\)，且都是相应 full relation
的子 relation。除非已证明单值，否则不把它们当作 maps。

### Definition 0.3（RL 的量词层）

称有限非减函数

\[
\omega:[0,+\infty)\to[0,+\infty),
\qquad
\omega(0)=0,\qquad \omega(t)\to0\ (t\downarrow0)
\]

为 Cayley modulus。power specialization 为

\[
\omega_{L,\gamma}(t):=Lt^\gamma,
\qquad L\ge0,\qquad 0<\gamma\le1.
\]

\(L=0\) 是允许的退化端点。此时 all-pairs (RL) 强迫
\(R_{\lambda,\Gamma}\) 为常值 map；\(\gamma\) 因而不可识别，任何
sharp-\(\gamma\) 表述均无意义。

给定任意 \(\Gamma\subset\operatorname{gph}F\)，称其满足
restricted all-pairs \(\omega\)-RL，若

\[
\forall (u,u^*)\in\Gamma\ \forall(v,v^*)\in\Gamma:
\quad
\|(u-v)-\lambda(u^*-v^*)\|
\le
\omega\!\left(\|(u-v)+\lambda(u^*-v^*)\|\right).
\tag{RL}
\]

当 \(\Gamma=\varnothing\) 时，上述全称命题按通常逻辑真空成立；任何
resolvent 或算法结论仍须另给非空性与 input coverage。若
\(\Gamma=\operatorname{gph}F\)，称为 global all-pairs RL；这里
“global”只修饰 graph quantifier，不表示 \(D_\lambda(F)=H\)。

对 \((\bar u,\bar u^*)\in\operatorname{gph}F\)，graph-local
all-pairs RL 指存在邻域 \(U\ni\bar u\)、\(W\ni\bar u^*\)，使

\[
\Gamma_{U,W}:=\operatorname{gph}F\cap(U\times W)
\]

上的每一对 graph points 都满足 (RL)。这与只限制 Minty input 的
locality 不同。

给定 moving set \(\Gamma_{\rm m}\subset\operatorname{gph}F\) 与
非空 \(S_0\subset S\)，称其满足 solution-anchored
\(\omega\)-RL，若

\[
\forall(u,u^*)\in\Gamma_{\rm m}\ \forall p\in S_0:
\quad
\|(u-p)-\lambda u^*\|
\le
\omega\!\left(\|(u-p)+\lambda u^*\|\right).
\tag{A-RL}
\]

all-pairs RL 可验证同一 restriction 内的 anchored RL；反向一般不成立，
anchored RL 也不蕴含 Minty injectivity。

### Definition 0.4（residual-windowed gauge error bound）

称

\[
\psi:[0,\eta_\psi)\to[0,+\infty)
\]

为 error-bound gauge，若其有限、非减，且
\(\psi(0)=0\)、\(\psi(t)\to0\) 当 \(t\downarrow0\)。
固定 \(\bar u\in S\)。本文采用双局部化 convention：
\(F\) 在 \((\bar u,0)\) 满足 residual-windowed local gauge
error bound，是指存在邻域 \(U\ni\bar u\) 和
\(0<\delta<\eta_\psi\)，使

\[
\forall u\in U\ \text{with }r_F(u)<\delta:
\quad
d(u,S)\le\psi(r_F(u)).
\tag{GEB}
\]

residual window 是定义的一部分；对一般 gauge，(GEB) 不与
neighborhood-only convention 自动等价。

power 情形为

\[
\psi(t)=\rho t^q,\qquad \rho>0,\quad q>0,
\]

即

\[
d(u,S)\le\rho\,r_F(u)^q.
\tag{PEB}
\]

对正 power gauge，windowed 与 neighborhood-only 版本在缩邻域后等价：
若 (PEB) 在 \(U\) 且 \(r_F(u)<\delta\) 时成立，则在任意

\[
U'\subset U\cap B(\bar u,\rho\delta^q)
\]

上，对所有 \(u\in U'\) 都成立；当 \(r_F(u)\ge\delta\) 时使用
\(d(u,S)\le\|u-\bar u\|<\rho\delta^q\le\rho r_F(u)^q\)。

(GEB)/(PEB) 是 full-mapping 条件，因为 \(r_F\) 对 \(F(u)\) 中所有
values 取 infimum。对某个 graph branch 只知
\(\|u-p\|\le C\|u^*\|^q\) 是 branchwise 条件，不能无附加覆盖条件改称
full-mapping error bound。

### Definition 0.5（coverage、exclusion 与 invariance）

若 \(E\subset H\)，则：

1. \(\Gamma\) covers \(E\) 指 \(E\subset D_\lambda(\Gamma)\)；
2. \(\Gamma\) excludes remote branches on \(E\) 指
   \[
   \{z\in\operatorname{gph}F:M_\lambda z\in E\}\subset\Gamma;
   \tag{EX}
   \]
3. 一个 named iteration 的 invariance 指其实际轨道始终留在定理的
   input 与 graph window；它可由 self-map 证明，也可由有限步长预算证明。

三者互不替代。特别地，coverage 是存在性，exclusion 是 full relation
唯一性，invariance 是迭代合法性。

## 1. Minty--Cayley 基础等价

### Theorem 1.1（RL、内积、reflector 与 firm-type 的精确等价）

令 \(\Gamma\subset\operatorname{gph}F\)，并令 \(\omega\) 为 Cayley
modulus。对

\[
a:=u-v,\qquad b:=u^*-v^*,\qquad
t:=\|a+\lambda b\|,
\]

下列陈述精确等价：

1. \(\Gamma\) 满足 all-pairs \(\omega\)-RL；
2. 对 \(\Gamma\times\Gamma\) 中所有 pairs，
   \[
   \lambda\langle a,b\rangle
   \ge\frac14\bigl(t^2-\omega(t)^2\bigr);
   \tag{1.1}
   \]
3. \(M_\lambda|_\Gamma\) 单射，且由此定义的 restricted reflector
   \(R_{\lambda,\Gamma}:D_\lambda(\Gamma)\to H\) 满足
   \[
   \|R_{\lambda,\Gamma}x-R_{\lambda,\Gamma}y\|
   \le\omega(\|x-y\|)
   \quad(\forall x,y\in D_\lambda(\Gamma));
   \tag{1.2}
   \]
4. 对所有 \(z=(u,u^*),z'=(v,v^*)\in\Gamma\)，令
   \(x=M_\lambda z\)、\(y=M_\lambda z'\)，都有
   \[
   \|u-v\|^2+\|\lambda(u^*-v^*)\|^2
   \le\frac12\left(\|x-y\|^2+\omega(\|x-y\|)^2\right).
   \tag{1.3}
   \]

在这些条件下，restricted resolvent
\(T:=J_{\lambda,\Gamma}:D_\lambda(\Gamma)\to H\) 是 map，
\(R_{\lambda,\Gamma}=2T-I\)，而 (1.3) 可写成

\[
\|Tx-Ty\|^2+\|(I-T)x-(I-T)y\|^2
\le\frac12\left(\|x-y\|^2+\omega(\|x-y\|)^2\right).
\tag{1.4}
\]

**Proof.**
恒等式

\[
\|a-\lambda b\|^2
=\|a+\lambda b\|^2-4\lambda\langle a,b\rangle
\]

给出 1 \(\Leftrightarrow\) 2。若两个 graph points 有相同 Minty
input，则 1 的右端为 \(\omega(0)=0\)，故 Cayley outputs 也相同；
由 (0.1) 得两 graph points 相同。因此 \(M_\lambda|_\Gamma\) 单射，
且 (RL) 在坐标中正是 (1.2)。反向把 \(x,y\) 拉回 graph 即得 (RL)。
最后，平行四边形恒等式给出

\[
\|a\|^2+\|\lambda b\|^2
=\frac12\bigl(\|a+\lambda b\|^2+\|a-\lambda b\|^2\bigr),
\]

故 1 \(\Leftrightarrow\) 4。 \(\square\)

**Remark 1.2（自然域边界）.**
若 \(\Gamma=\operatorname{gph}F\)，Theorem 1.1 只使 full
\(J_{\lambda F}\)、\(R_{\lambda F}\) 在
\(D_\lambda(F)=\operatorname{ran}(I+\lambda F)\) 上单值；不推出
满域、maximality、graph closedness 或 range closedness。例如
\(F(u)=\{0\}\) 对 \(0<u<1\)，其余点空值，则
\(\mathrm{RL}(\lambda,1,1)\) global 成立，而 graph、\(S\) 与自然域
均为非闭的 \((0,1)\) 型集合。

### Proposition 1.3（Cayley pullback realization）

给定任意 \(D\subset H\) 与 map \(R:D\to H\)，定义 abstract graph
（等价地，把它视为其所生成 relation 的 graph）

\[
\Gamma_R^\lambda
:=\left\{
\left(\frac{x+Rx}{2},\frac{x-Rx}{2\lambda}\right):x\in D
\right\}.
\tag{1.5}
\]

则

\[
D_\lambda(\Gamma_R^\lambda)=D,\qquad
R_{\lambda,\Gamma_R^\lambda}=R,
\]

且

\[
\Gamma_R^\lambda\text{ satisfies all-pairs }\omega\text{-RL}
\Longleftrightarrow
\|Rx-Ry\|\le\omega(\|x-y\|)
\quad(\forall x,y\in D).
\tag{1.6}
\]

**Proof.**
定义中的 graph point 直接满足 \(M_\lambda=x\) 与 \(C_\lambda=Rx\)；
把它们代入 (RL) 即得。 \(\square\)

因此 RL 在 map side 的精确含义就是自然 Minty 域上的普通
modulus continuity；额外 operator content 必须来自 graph、domain、
regularity 或 algorithmic interaction。

### Proposition 1.4（named branch 与 full resolvent）

设 \(\Gamma\) 满足 all-pairs RL，且
\(E\subset D_\lambda(\Gamma)\)。则

\[
T_{\Gamma,E}
:=\pi_1\circ(M_\lambda|_\Gamma)^{-1}\big|_E:E\to H
\tag{1.7}
\]

是一个 named restricted resolvent branch。若再有 (EX)，则

\[
J_{\lambda F}(x)=\{T_{\Gamma,E}x\}
\quad(\forall x\in E).
\tag{1.8}
\]

**Proof.**
Theorem 1.1 给出 restricted inverse 的唯一性，coverage 给出每个
\(x\in E\) 的 existence。(EX) 迫使 full graph 中具有该 Minty input
的每个 realization 都落入 \(\Gamma\)，再由 restricted injectivity
得唯一性。 \(\square\)

**Remark 1.5（coverage 反例）.**
令 \(K=\{0\}\cup\{1/k:k\ge1\}\) 且
\(\operatorname{gph}F=K\times\{0\}\)（GX-074）。自然域仅为 \(K\)，
\(J=R=I\) 在 \(K\) 上满足每个 \(0<\gamma\le1\) 的 bounded-domain
RL certificate，但任何 generic 近零 input 均无 resolvent step。

## 2. \(\gamma=1\) 字典、inverse 与 scaling

### Theorem 2.1（三个精确代数规则）

令 \(L\ge0\)、\(0<\gamma\le1\)，并令
\(\Gamma\subset\operatorname{gph}F\)。

**(a) \(\gamma=1\) tied semimonotonicity.** 定义

\[
\theta_L:=\frac{1-L^2}{2(1+L^2)},\qquad
\mu_L:=\frac{\theta_L}{\lambda},\qquad
\rho_L:=\lambda\theta_L=\lambda^2\mu_L.
\tag{2.1}
\]

则 \(\Gamma\) 满足 \(\mathrm{RL}(\lambda,L,1)\) 当且仅当

\[
\langle u-v,u^*-v^*\rangle
\ge
\mu_L\|u-v\|^2+\rho_L\|u^*-v^*\|^2
\tag{2.2}
\]

对所有 pairs 成立。当 \(L\ge1\)，令
\(\tau_L:=(L^2-1)/4\)，同一条件也等价于

\[
\lambda\langle a,b\rangle
\ge-\tau_L\|a+\lambda b\|^2.
\tag{2.3}
\]

**(b) Inverse.** 记
\(\Gamma^{-1}:=\{(u^*,u):(u,u^*)\in\Gamma\}\)。则

\[
\Gamma\in\mathrm{RL}(\lambda,L,\gamma)
\Longleftrightarrow
\Gamma^{-1}\in
\mathrm{RL}\!\left(\lambda^{-1},
L\lambda^{\gamma-1},\gamma\right).
\tag{2.4}
\]

**(c) Positive output scaling.** 对 \(c>0\)，记
\(c\Gamma:=\{(u,cu^*):(u,u^*)\in\Gamma\}\)。则

\[
\Gamma\in\mathrm{RL}(\lambda,L,\gamma)
\Longleftrightarrow
c\Gamma\in\mathrm{RL}(\lambda/c,L,\gamma).
\tag{2.5}
\]

在 full-graph 语言中，两个定参读法是

\[
F@\lambda\Longleftrightarrow cF@(\lambda/c),
\qquad
cF@\lambda\Longleftrightarrow F@(c\lambda),
\tag{2.6}
\]

其中 \(L,\gamma\) 保持不变。

**Proof.**
展开
\(\|a-\lambda b\|^2\le L^2\|a+\lambda b\|^2\)，整理内积项即得
(2.1)--(2.3)。对 inverse graph，差分变为 \((b,a)\)，且

\[
\|b-\lambda^{-1}a\|
=\lambda^{-1}\|a-\lambda b\|,
\qquad
\|b+\lambda^{-1}a\|^\gamma
=\lambda^{-\gamma}\|a+\lambda b\|^\gamma,
\]

故常数变为 \(L\lambda^{\gamma-1}\)。对 \(c\Gamma\)，output
difference 为 \(cb\)，而 \((\lambda/c)(cb)=\lambda b\)，两侧逐项
与原式相同。 \(\square\)

**Remark 2.2（命名与文献边界）.**
\(\gamma=1\) 是 tied semimonotonicity/submonotonicity 的精确参数切片，
不是本文声称的新类。higher-order subregularity 与非孤立 PPA
superlinear convergence 亦已有相关结果；本文只冻结所述 branchwise、
endpoint 与 two-anchor 结构。Wang--Li--Ng 2023 及
Moursi--Vanderwerff 2025 的精确公式覆盖仍待全文核对，故不作排他性表述。

## 3. 从 all-pairs RL 验证 named branch

### Proposition 3.1（all-pairs verifier）

令 \(S\ne\varnothing\)，\(G\subset\operatorname{gph}F\) 满足
\(\mathrm{RL}(\lambda,L,\gamma)\)，其中 \(L\ge0\)、
\(0<\gamma\le1\)。设 \(U\subset D_\lambda(G)\)，并定义

\[
\sigma:=(M_\lambda|_G)^{-1}:U\to G,
\qquad
\sigma(x)=(Tx,Vx).
\tag{3.1}
\]

再令

\[
S_G:=\{p\in S:(p,0)\in G\}.
\]

若对某个 active set \(\mathcal A\subset U\) 有

\[
d(x,S_G)=d(x,S)\qquad(\forall x\in\mathcal A),
\tag{3.2}
\]

则对每个 \(x\in\mathcal A\)，存在 \(p_n\in S_G\) 使
\(\|x-p_n\|\to d(x,S)\)，并且

\[
\|2Tx-x-p_n\|\le L\|x-p_n\|^\gamma
\qquad(\forall n).
\tag{3.3}
\]

此外，对所有 \(x,y\in U\)，

\[
\|(2T-I)x-(2T-I)y\|
\le L\|x-y\|^\gamma.
\tag{3.4}
\]

**Proof.**
Theorem 1.1 与 coverage 定义 \(\sigma\)。由 (3.2) 取
\(\varepsilon\)-nearest \(p_n\in S_G\)，再把
\(\sigma(x)\) 与 \((p_n,0)\) 代入 all-pairs RL，得到 (3.3)。
把 \(\sigma(x),\sigma(y)\) 代入同一不等式得到 (3.4)。 \(\square\)

该命题使用 all-pairs RL 来同时获得 restricted injectivity 与 anchored
estimate。下面的收敛定理本身只需要 named branch 与 anchored estimate。

## 4. Named-branch local gauge PPA

固定 \(\bar x\in S\)、\(R>0\)，令

\[
U:=B(\bar x,R).
\]

取 \(L\ge0\)、\(0<\gamma\le1\)，以及 error-bound gauge
\(\psi:[0,\eta_\psi)\to[0,+\infty)\)。取 \(\delta>0\) 足够小，使

\[
h_\gamma(\delta)
:=\frac{\delta+L\delta^\gamma}{2\lambda}
<\eta_\psi.
\tag{4.1}
\]

令

\[
\mathcal A_\delta
:=\{x\in U:d(x,S)\le\delta\}.
\]

以下三个假设的量词均覆盖整个 \(\mathcal A_\delta\)，包括
\(d(x,S)=0\) 的 interior limit points。

**B（named Minty coverage）.** 存在
\(G\subset\operatorname{gph}F\) 与指定映射

\[
\sigma:U\to G,\qquad M_\lambda\sigma(x)=x\quad(\forall x\in U).
\tag{B}
\]

写 \(\sigma(x)=(Tx,Vx)\)，则

\[
x=Tx+\lambda Vx,\qquad
Vx=\frac{x-Tx}{\lambda}\in F(Tx).
\tag{4.2}
\]

**A（epsilon-nearest anchored RL）.** 对每个
\(x\in\mathcal A_\delta\)，令 \(r=d(x,S)\)。存在可依赖于 \(x\) 的
序列 \(p_n\in S\)，使

\[
\|x-p_n\|\to r
\tag{4.3}
\]

且

\[
\|2Tx-x-p_n\|\le L\|x-p_n\|^\gamma
\quad(\forall n).
\tag{4.4}
\]

**E（output-point residual-windowed error bound）.** 对每个
\(x\in\mathcal A_\delta\)，

\[
r_F(Tx)<\eta_\psi,
\qquad
d(Tx,S)\le\psi(r_F(Tx)).
\tag{E}
\]

若 E 来自 Definition 0.4，则必须另核 \(Tx\) 落在其 base-variable
neighborhood；(4.1) 与下面的 residual bound 负责 residual window。

### Lemma 4.1（一步 step--residual--distance 链）

定义

\[
b_\gamma(r):=\frac12(r+Lr^\gamma),
\qquad
\Phi_\gamma(r)
:=\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right).
\tag{4.5}
\]

在 B、A、E 下，对每个 \(x\in\mathcal A_\delta\)，令
\(x^+:=Tx\)、\(r=d(x,S)\)，则

\[
\|x-x^+\|\le b_\gamma(r),
\tag{4.6}
\]

\[
r_F(x^+)
\le\frac{b_\gamma(r)}{\lambda}
=\frac{r+Lr^\gamma}{2\lambda},
\tag{4.7}
\]

\[
d(x^+,S)\le\Phi_\gamma(r).
\tag{4.8}
\]

**Proof.**
由恒等式

\[
2(x-Tx)=(x-p_n)-(2Tx-x-p_n)
\]

和 (4.4)，

\[
2\|x-Tx\|
\le\|x-p_n\|+L\|x-p_n\|^\gamma.
\]

令 \(n\to\infty\) 得 (4.6)。由 (4.2)，
\((x-Tx)/\lambda\in F(Tx)\)，故 (4.7) 成立。最后用 E、
\(\psi\) 的非减性及 (4.7) 得 (4.8)。 \(\square\)

### Theorem 4.2（localized gauge--PPA convergence）

在 B、A、E 下，设

\[
c_\gamma
:=\limsup_{r\downarrow0}\frac{\Phi_\gamma(r)}r<1.
\tag{4.9}
\]

任选 \(c_\gamma<\theta<1\)，并取
\(0<\delta_\theta\le\delta\)，使

\[
\Phi_\gamma(r)\le\theta r
\quad(0<r\le\delta_\theta).
\tag{4.10}
\]

若 \(x^0\in U\)、\(r_0=d(x^0,S)\le\delta_\theta\)，且

\[
\|x^0-\bar x\|+B_\gamma(r_0,\theta)<R,
\tag{4.11}
\]

其中

\[
B_\gamma(r,\theta)
:=\frac12\left(
\frac{r}{1-\theta}
+\frac{Lr^\gamma}{1-\theta^\gamma}
\right),
\tag{4.12}
\]

则 named iteration

\[
x^{k+1}=T(x^k)
\tag{4.13}
\]

对所有 \(k\) 合法，始终留在 \(U\)，具有有限长度，并强收敛到某个
\(x^\infty\in S\)。更精确地，

\[
r_k:=d(x^k,S)\le\theta^k r_0,
\tag{4.14}
\]

\[
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|
\le B_\gamma(r_0,\theta),
\tag{4.15}
\]

\[
\|x^k-x^\infty\|\le B_\gamma(r_k,\theta).
\tag{4.16}
\]

**Proof.**
若 \(r_0=0\)，Lemma 4.1 给 \(Tx^0=x^0\)，轨道恒定。设
\(r_0>0\)。归纳假设 \(x^k\in U\) 且
\(r_k\le\theta^kr_0\)。若 \(r_k=0\)，轨道从此恒定；否则由
(4.8)、(4.10)，

\[
r_{k+1}\le\theta r_k\le\theta^{k+1}r_0.
\]

同时

\[
\|x^{k+1}-x^k\|
\le\frac12\left(\theta^kr_0+
L\theta^{\gamma k}r_0^\gamma\right).
\tag{4.17}
\]

对 (4.17) 求部分和并用 (4.11)，每个下一 iterate 都严格留在
\(U\)，闭合归纳；求无限和得 (4.15)，故轨道 Cauchy。令其极限为
\(x^\infty\)。严格 margin 仍给 \(x^\infty\in U\)，而距离函数
1-Lipschitz 及 (4.14) 给 \(d(x^\infty,S)=0\)。A 的量词覆盖该
interior input，故 Lemma 4.1 在 \(x^\infty\) 给
\(Tx^\infty=x^\infty\)；再由 B 得
\(0\in F(x^\infty)\)，所以 \(x^\infty\in S\)。
最后，对任意 \(j\ge0\)，

\[
r_{k+j}\le\theta^j r_k.
\]

从 \(k\) 起对 Lemma 4.1 的 step bound 求和，即得 (4.16)。
\(\square\)

**Remark 4.3（四层逻辑）.**
B 是 input coverage 加 named selection；A 是 anchored、不是
all-pairs 假设；(4.11) 证明轨道 invariance；全程未使用 branch
exclusion。因此结论只针对 (4.13)。只有另有 (EX) 时，才可把它改写成
full resolvent 的唯一 PPA step；若无 (EX)，不能量化任意
\(x^{k+1}\in J_{\lambda F}(x^k)\)。

endpoint-quantified A 与 B 还蕴含

\[
U\cap\overline S=U\cap S.
\tag{4.18}
\]

所以“不另假设 closedness”并不表示 A、B 允许 \(U\) 内存在
零距离但不属于 \(S\) 的点。

## 5. Power corollaries

### Corollary 5.1（\(0<\gamma<1\)，非退化 \(L>0\)）

在 Theorem 4.2 的假设中令

\[
\psi(t)=\rho t^q,\qquad \rho>0,\quad q>0,
\]

并额外设 \(0<\gamma<1\)、\(L>0\)。则

\[
r_+\le
\frac{\rho}{(2\lambda)^q}(r+Lr^\gamma)^q.
\tag{5.1}
\]

令 \(p:=\gamma q\)。对 \(0<r\le\delta_0\le\delta\)，

\[
r_+\le C_{\delta_0}r^p,
\qquad
C_{\delta_0}
:=\frac{\rho}{(2\lambda)^q}
(\delta_0^{1-\gamma}+L)^q.
\tag{5.2}
\]

1. 若 \(p>1\)，可缩小 \(\delta_0\) 使
   \[
   \theta_{\delta_0}
   :=C_{\delta_0}\delta_0^{p-1}<1.
   \]
   在 \(r_0\le\delta_0\) 且 (4.11) 以
   \(\theta_{\delta_0}\) 成立时，Theorem 4.2 适用，并有
   \[
   r_{k+1}=O(r_k^{\gamma q}).
   \tag{5.3}
   \]
   非有限终止时 \(r_{k+1}/r_k\to0\)。
2. 若 \(p=1\)，令
   \[
   \kappa_\gamma
   :=\rho\left(\frac{L}{2\lambda}\right)^q.
   \tag{5.4}
   \]
   若 \(\kappa_\gamma<1\)，可缩小 \(\delta_0\) 使
   \(\theta_{\delta_0}:=C_{\delta_0}<1\)，再施加相应 margin。
   对非终止轨道，
   \[
   \limsup_k\frac{r_{k+1}}{r_k}
   \le\kappa_\gamma<1.
   \tag{5.5}
   \]
3. 若 \(p<1\)，(5.1) 本身不推出局部收敛或发散。

**Proof.**
因

\[
r+Lr^\gamma=r^\gamma(r^{1-\gamma}+L),
\]

(5.2) 立即成立。\(p>1\) 时右端相对 \(r\) 的系数趋零；
\(p=1\) 时该系数趋于 (5.4)；随后逐项调用 Theorem 4.2。
\(p<1\) 时该 upper bound 相对 \(r\) 不产生 contraction。
\(\square\)

### Corollary 5.2（\(\gamma=1\)，包括 \(L=0\)）

在同一 power 假设下令 \(\gamma=1\)、\(L\ge0\)。则

\[
r_+\le A_1r^q,
\qquad
A_1:=\rho\left(\frac{1+L}{2\lambda}\right)^q.
\tag{5.6}
\]

若 \(q>1\)，缩小 \(\delta_0\) 使
\(A_1\delta_0^{q-1}<1\)，并施加 Theorem 4.2 的 margin，即得
\(r_{k+1}=O(r_k^q)\)。若 \(q=1\) 且

\[
\kappa_1:=\rho\frac{1+L}{2\lambda}<1,
\tag{5.7}
\]

则得到线性 upper contraction，且非终止轨道的 ratio limsup 不超过
\(\kappa_1\)。若 \(q<1\)，(5.6) 单独不推出局部收敛或发散。

**Proof.**
在 (5.1) 的原始一步式中代入 \(\gamma=1\)，有
\(r+Lr=(1+L)r\)，再按 \(q>1,q=1,q<1\) 比较
\(A_1r^{q-1}\) 即得。 \(\square\)

### Corollary 5.3（退化 \(L=0\) 的 \(q\)-phase）

在 power gauge 下，若 \(L=0\)，则无论 certificate 中打印哪个
\(0<\gamma\le1\)，都有

\[
r_+\le\frac{\rho}{(2\lambda)^q}r^q.
\tag{5.8}
\]

因此 \(q>1\) 时得到 local upper order \(q\)；\(q=1\) 时本路径的
临界充分条件为 \(\rho/(2\lambda)<1\)；\(q<1\) 时 (5.8) 单独不推出
contraction。此时 phase 由 \(q\) 而非 \(\gamma q\) 控制。

**Proof.**
在 (5.1) 中令 \(L=0\)，再比较
\(\rho(2\lambda)^{-q}r^{q-1}\) 与 \(1\)。 \(\square\)

**Remark 5.4（upper、two-sided exponent 与 Q-factor）.**
(5.3)、(5.6)、(5.8) 是 one-step upper-order guarantees。
two-sided exact exponent \(p\) 要求

\[
0<
\liminf_k\frac{r_{k+1}}{r_k^p}
\le
\limsup_k\frac{r_{k+1}}{r_k^p}
<+\infty.
\tag{5.9}
\]

只有进一步证明

\[
\frac{r_{k+1}}{r_k^p}\to c\in(0,+\infty)
\tag{5.10}
\]

时，才称 exact Q-order with factor \(c\)。有限终止不具有正的
Q-factor。临界系数
\(\kappa_\gamma,\kappa_1\) 是本证明路径的充分系数，未证明必要或最优。
\(L=0\) 时 Corollary 5.1 的 \(\gamma q\) 主导项消失，应回到原式读取
\(q\)-power，而不是沿用 \(\gamma q\) 标签。

## 6. Moving-anchor asymptotic reflection

### Theorem 6.1（superlinear gauge 与 output-near anchor）

令 \(\psi:[0,\eta)\to[0,+\infty)\) 有限、非减且
\(\psi(t)=o(t)\)。考虑任意 graph point
\((y,w)\in\operatorname{gph}F\)，其中
\(0<\|w\|<\eta\)，并设

\[
d(y,S)\le\psi(r_F(y)).
\tag{6.1}
\]

令 \(e:[0,\eta)\to[0,+\infty)\) 满足 \(e(t)=o(t)\)，并选择
\(p\in S\) 使

\[
\|y-p\|\le d(y,S)+e(\|w\|).
\tag{6.2}
\]

若 \(e(\|w\|)>0\)，该选择不需 proximinality；若 \(e=0\)，则须另有
exact projection。定义

\[
x:=y+\lambda w,\qquad
\widehat x:=y-\lambda w,
\]

\[
\vartheta(t):=\psi(t)+e(t),
\qquad
\delta_w:=\frac{\vartheta(\|w\|)}{\lambda\|w\|}.
\tag{6.3}
\]

当 \(\delta_w<1\) 时，

\[
\frac{1-\delta_w}{1+\delta_w}
\le
\frac{\|\widehat x-p\|}{\|x-p\|}
\le
\frac{1+\delta_w}{1-\delta_w},
\tag{6.4}
\]

\[
\frac{\|\widehat x-(2p-x)\|}{\|x-p\|}
\le\frac{2\delta_w}{1-\delta_w}.
\tag{6.5}
\]

因此沿任意 \(w_n\to0\)、\(w_n\ne0\) 的合法序列，

\[
\frac{\|\widehat x_n-p_n\|}{\|x_n-p_n\|}\to1,
\qquad
\widehat x_n-p_n
=-(x_n-p_n)+o(\|x_n-p_n\|).
\tag{6.6}
\]

**Proof.**
由 \(r_F(y)\le\|w\|\)、\(\psi\) 非减及 (6.1)--(6.2)，
\(\|y-p\|\le\vartheta(\|w\|)\)。令
\(a:=y-p\)、\(t:=\lambda w\)，则
\(x-p=a+t\)、\(\widehat x-p=a-t\) 且
\(\|a\|\le\delta_w\|t\|\)。正、反三角不等式给 (6.4)。
又

\[
\widehat x-(2p-x)=2a,
\qquad
\|x-p\|\ge(1-\delta_w)\|t\|,
\]

故得 (6.5)。最后 \(\delta_{w_n}\to0\)，得到 (6.6)。
\(\square\)

### Corollary 6.2（power defect）

若 \(q>1\)，且

\[
d(y,S)\le\rho r_F(y)^q,
\qquad
\|y-p\|\le d(y,S)+c\|w\|^q
\]

其中 \(c\ge0\)，令 \(A:=\rho+c\)。当
\((A/\lambda)\|w\|^{q-1}\le1/2\) 时，

\[
\|\widehat x-(2p-x)\|
\le
\frac{2^{q+1}A}{\lambda^q}\|x-p\|^q.
\tag{6.7}
\]

**Proof.**
\(\|y-p\|\le A\|w\|^q\)，且小量条件给
\(\|x-p\|\ge\lambda\|w\|/2\)。再用
\(\widehat x-(2p-x)=2(y-p)\)。 \(\square\)

该结论围绕 output-nearest 或定量 output-near 的 moving zero；不自动
改成 fixed zero、input-nearest zero、set-distance ratio，也不产生
all-pairs reflector regularity或 resolvent branch existence。

## 7. Fixed-anchor 与 isolated-zero \(q\)-flatness

### Theorem 7.1（graph germ 上的 branchwise \(q\)-flatness 等价）

固定 \(p\in S\)、\(q>1\)，并令
\(\Gamma\subset\operatorname{gph}F\) 含 \((p,0)\)。对
\((y,w)\in\Gamma\) 令

\[
x:=y+\lambda w,\qquad \widehat x:=y-\lambda w.
\]

在 \((p,0)\) 的充分小 graph germ 上，下列三种 uniform
big-\(O\) 性质等价：

\[
\mathrm{(B_q)}\quad \|y-p\|\le C_B\|w\|^q,
\]

\[
\mathrm{(J_q)}\quad \|y-p\|\le C_J\|x-p\|^q,
\]

\[
\mathrm{(R_q)}\quad
\|\widehat x-(2p-x)\|\le C_R\|x-p\|^q.
\]

可安全转移的常数为

\[
C_J=C_B(2/\lambda)^q,\qquad
C_B=C_J(2\lambda)^q,\qquad
C_R=2C_J.
\tag{7.1}
\]

这些不声称是最优 moduli。

**Proof.**
由 \(\mathrm{(B_q)}\)，缩小 germ 使
\(C_B\|w\|^{q-1}\le\lambda/2\)，则

\[
\|x-p\|\ge\lambda\|w\|-\|y-p\|
\ge\frac{\lambda}{2}\|w\|,
\]

得到 \(\mathrm{(J_q)}\)。反之，由 \(\mathrm{(J_q)}\) 缩小 germ
使 \(C_J\|x-p\|^{q-1}\le1/2\)，则

\[
\lambda\|w\|
\ge\|x-p\|-\|y-p\|
\ge\frac12\|x-p\|,
\]

得到 \(\mathrm{(B_q)}\)。最后

\[
\widehat x-(2p-x)=2(y-p)
\]

给出 \(\mathrm{(J_q)}\Longleftrightarrow\mathrm{(R_q)}\)。
\(\square\)

### Proposition 7.2（general superlinear gauges 的 rescaled equivalence）

令

\[
\alpha,\beta:[0,\eta)\to[0,+\infty)
\]

在零附近有限、非减，满足
\(\alpha(0)=\beta(0)=0\) 及
\(\alpha(t)=o(t)\)、\(\beta(t)=o(t)\)。在 Theorem 7.1 的 graph
germ 上：

\[
\|y-p\|\le\beta(\|w\|)
\Longrightarrow
\|y-p\|\le
\beta\!\left(\frac{2}{\lambda}\|x-p\|\right),
\tag{7.G1}
\]

\[
\|y-p\|\le\alpha(\|x-p\|)
\Longrightarrow
\|y-p\|\le
\alpha(2\lambda\|w\|).
\tag{7.G2}
\]

reflection defect 仍恰为相应 \(J\)-control 的两倍。若希望两方向使用
同一个 gauge、只差 multiplicative constants，还需 fixed-dilation
stability：

\[
\psi(ct)=O(\psi(t))\quad(t\downarrow0)
\]

对相关固定 \(c>0\) 成立。任意 \(\psi=o(\mathrm{id})\) 不足够；
\(t_{n+1}=t_n^2\) 上构造的单调阶梯 gauge 即给反例。

**Proof.**
第一式中缩小 germ 使
\(\beta(\|w\|)\le\lambda\|w\|/2\)，于是
\(\|w\|\le2\|x-p\|/\lambda\)；第二式中使
\(\alpha(\|x-p\|)\le\|x-p\|/2\)，于是
\(\|x-p\|\le2\lambda\|w\|\)。分别用单调性。 \(\square\)

### Proposition 7.3（full error bound 与 branchwise bound 的方向）

令 \(q>0\)。若 \(p\) 是 locally isolated zero，并把其 neighborhood
缩小到

\[
d(y,S)=\|y-p\|\qquad(\forall y\in U),
\tag{7.2a}
\]

且 full mapping 在 \(U\) 上满足 \(q\)-power error bound，则对每个
\((y,w)\in\operatorname{gph}F\) with \(y\in U\)，

\[
\|y-p\|\le\rho\|w\|^q.
\tag{7.2}
\]

反向地，若某 graph restriction \(\Gamma\) residual-complete，即存在
\(U_{\rm c}\ni p,\eta>0\) 使

\[
\{(y,w):y\in U_{\rm c},\ w\in F(y),\ \|w\|<\eta\}\subset\Gamma,
\tag{7.3}
\]

且 (7.2) 在 \(\Gamma\) 上 uniform 成立，则缩小 \(U_{\rm c}\) 后，full mapping
满足 \(\|y-p\|\le C r_F(y)^q\)。只在一个 favorable branch 上成立的
(7.2) 不足以推出 full error bound。

**Proof.**
local isolation 给 \(d(y,S)=\|y-p\|\)。full bound 与
\(r_F(y)\le\|w\|\) 立即给 (7.2)。反向，若
\(r_F(y)<\eta\)，取 \(w_n\in F(y)\) 使
\(\|w_n\|\downarrow r_F(y)\)，由 residual completeness 与 (7.2)
令 \(n\to\infty\)。若 \(r_F(y)\ge\eta\)，在更小的
\(\|y-p\|<d_0\) 邻域使用
\(\|y-p\|\le(d_0/\eta^q)r_F(y)^q\)。 \(\square\)

### Theorem 7.4（isolated zero 上的 named PPA）

令 \(p\in S\) locally isolated、\(q>1\)。选定并固定一个已经充分缩小
的 neighborhood \(U\ni p\)，使

\[
d(y,S)=\|y-p\|\qquad(\forall y\in U),
\tag{7.3a}
\]

并在 \(U\) 上假设

\[
d(y,S)\le\rho r_F(y)^q.
\tag{7.4}
\]

令 \(T:V\to H\) 是覆盖 \(p\) 的 named resolvent branch：

\[
T(x)\in J_{\lambda F}(x),\qquad
w(x):=\frac{x-Tx}{\lambda}\in F(Tx),\qquad T(p)=p.
\tag{7.5}
\]

假设存在明确的 input neighborhood \(V_0\subset V\) of \(p\)，使

\[
Tx\in U,\qquad \|w(x)\|<\eta
\quad(\forall x\in V_0),
\tag{7.5a}
\]

其中

\[
\rho\eta^{q-1}\le\lambda/2.
\tag{7.6}
\]

则

\[
\|Tx-p\|\le C_q\|x-p\|^q,
\qquad
C_q:=\rho(2/\lambda)^q,
\tag{7.7}
\]

\[
\|(2T-I)x-(2p-x)\|\le2C_q\|x-p\|^q.
\tag{7.8}
\]

若 \(\overline B(p,\delta_0)\subset V_0\)，取
\(0<\delta\le\delta_0\) 与 \(0<\theta<1\) 使

\[
C_q\delta^{q-1}\le\theta.
\tag{7.9}
\]

则 \(T(\overline B(p,\delta))\subset B(p,\delta)\)，每个 named
orbit 收敛到 \(p\)，并满足 upper recurrence

\[
r_{k+1}\le C_qr_k^q,
\qquad
r_k\le
C_q^{(q^k-1)/(q-1)}r_0^{q^k},
\quad r_k:=\|x^k-p\|.
\tag{7.10}
\]

**Proof.**
Proposition 7.3 给
\(\|Tx-p\|\le\rho\|w(x)\|^q\)。由 (7.6)，

\[
\|x-p\|
\ge\lambda\|w(x)\|-\|Tx-p\|
\ge\frac{\lambda}{2}\|w(x)\|,
\]

得到 (7.7)；(7.8) 来自恒等式
\((2T-I)x-(2p-x)=2(Tx-p)\)。(7.7)、(7.9) 给 ball invariance
及 contraction；迭代 (7.10) 的第一式即得第二式。 \(\square\)

### Corollary 7.5（isolated superlinear-gauge named PPA）

在 Theorem 7.4 的全部 localization 假设下，特别保留
\(V_0\)、\(Tx\in U\) 与 (7.3a)，令

\[
\psi:[0,\eta_\psi)\to[0,+\infty)
\]

为有限非减 gauge，并以

\[
d(y,S)\le\psi(r_F(y)),\qquad \psi(t)=o(t)
\]

替换 power bound。缩小 residual 与 input windows，使

\[
\|w(x)\|<\eta_\psi,\qquad
\psi(t)\le\lambda t/2,\qquad
\frac{2}{\lambda}\|x-p\|<\eta_\psi
\tag{7.10a}
\]

对所有相关 \(x\) 与 attained \(t=\|w(x)\|\) 成立。则

\[
\|Tx-p\|
\le
\psi\!\left(\frac{2}{\lambda}\|x-p\|\right)
=o(\|x-p\|).
\tag{7.11}
\]

因此充分小 input ball invariant；除有限终止外，
\[
\frac{\|x^{k+1}-p\|}{\|x^k-p\|}\to0.
\tag{7.12}
\]

**Proof.**
isolation 给 \(\|Tx-p\|\le\psi(\|w(x)\|)\)，小量条件给
\(\|x-p\|\ge\lambda\|w(x)\|/2\)。用 \(\psi\) 非减得 (7.11)，
再缩小 ball 使右端不超过 \(\theta\|x-p\|\)，闭合 invariance 与
ratio 结论。 \(\square\)

### Proposition 7.6（exact \(q\)-order factor 的附加判据）

令 \(q>1\)，并取 Theorem 7.4 在其 invariant ball 内生成的 named
nonterminating orbit。则 \(x^k,x^{k+1}\to p\)，从而

\[
w_k:=\frac{x^k-x^{k+1}}{\lambda}\to0.
\tag{7.13a}
\]

若进一步

\[
\frac{\|x^{k+1}-p\|}{\|w_k\|^q}
\to\mu\in(0,+\infty),
\tag{7.13}
\]

则

\[
\frac{\|x^{k+1}-p\|}{\|x^k-p\|^q}
\to\frac{\mu}{\lambda^q}.
\tag{7.14}
\]

**Proof.**
(7.13) 与 \(q>1\) 给
\(\|x^{k+1}-p\|=o(\|w_k\|)\)。由
\(x^k-p=(x^{k+1}-p)+\lambda w_k\)，
\(\|x^k-p\|/(\lambda\|w_k\|)\to1\)，代回即得。 \(\square\)

Theorem 7.4 仍只控制 named branch；任意 full-resolvent selections
需要 branch exclusion。其 \(q\) 是 upper order，只有
Proposition 7.6 一类 normalized branch limit 才能升级为带正
Q-factor 的 exact Q-order。

## 8. 非孤立解集的 alignment 与 \(\theta q\)

令 \(D\) 是一个 named Minty-input domain，且
\(J:D\to H\) 为 single-valued branch。对 \(x\in D\)，记

\[
y:=Jx,\qquad
w:=\frac{x-y}{\lambda},\qquad
(y,w)\in\operatorname{gph}F.
\tag{8.1}
\]

固定 local input region \(U\subset D\) 与 \(r_0>0\)，并令

\[
\mathcal F_{r_0}
:=\{x\in U:0<d(x,S)\le r_0\}.
\tag{8.1a}
\]

本节的 exact-profile statements 假设对每个
\(x\in\mathcal F_{r_0}\)，两个 sets \(P_S(x)\) 与 \(P_S(Jx)\)
都非空。这个假设覆盖 envelope 的整个 index family，而不只是某条
事后选择的 sequence。定义

\[
d(A,B):=\inf\{\|a-b\|:a\in A,\ b\in B\}
\quad(A,B\ne\varnothing).
\tag{8.2a}
\]

\[
a_J(x):=d(x,P_S(Jx)),
\tag{8.2}
\]

\[
\delta_J(x):=
d(P_S(x),P_S(Jx)).
\tag{8.3}
\]

\(a_J\) 是 input 到 output-nearest solution anchors 的距离；
\(\delta_J\) 是 input-nearest 与 output-nearest anchors 的最小 drift。
二者均未用所欲证明的 output rate 定义，因而不是循环量。

### Lemma 8.1（alignment 与 drift profile）

对每个 \(x\in\mathcal F_{r_0}\)，令 \(r_x:=d(x,S)\)。则

\[
r_x\le a_J(x)
\le r_x+\delta_J(x)
\le3a_J(x).
\tag{8.4}
\]

因此对 \(0<r\le r_0\)，定义

\[
\mathcal A_J(r)
:=\sup_{\substack{x\in U\\0<d(x,S)\le r}}a_J(x),
\]

\[
\chi_J(r)
:=\sup_{\substack{x\in U\\0<d(x,S)\le r}}
\bigl(d(x,S)+\delta_J(x)\bigr),
\]

并约定所有非负 envelope 的空 supremum 为 \(0\)。则

\[
\mathcal A_J(r)\le\chi_J(r)\le3\mathcal A_J(r).
\tag{8.5}
\]

**Proof.**
因 \(P_S(Jx)\subset S\)，有 \(r_x\le a_J(x)\)。分别选取近似实现
\(\delta_J(x)\) 的 \(p_x\in P_S(x),p_y\in P_S(Jx)\)，得
\(a_J(x)\le r_x+\delta_J(x)\)。反向，用近似实现 \(a_J(x)\) 的
\(p_y\) 与任意 \(p_x\in P_S(x)\)，得
\(\delta_J(x)\le r_x+a_J(x)\)，故
\(r_x+\delta_J(x)\le2r_x+a_J(x)\le3a_J(x)\)。取 supremum 即得。
\(\square\)

### Theorem 8.2（superlinear gauge composition）

设

\[
\psi:[0,\eta_\psi)\to[0,+\infty)
\]

为有限非减 gauge。假设对每个 \(x\in\mathcal F_{r_0}\)，
\(\|w(x)\|<\eta_\psi\)，且在相应 output \(y=Jx\) 上，

\[
d(y,S)\le\psi(r_F(y)),
\qquad
\psi(t)=o(t),
\tag{8.6}
\]

且 residual 足够小，使
\(\psi(t)\le\lambda t/2\) 对所有 attained \(t=\|w(x)\|\) 成立。
对任意还满足

\[
\frac{2}{\lambda}
\bigl[d(x,S)+\delta_J(x)\bigr]<\eta_\psi
\tag{8.6a}
\]

的 \(x\in\mathcal F_{r_0}\)，有

\[
d(Jx,S)
\le
\psi\!\left(\frac{2}{\lambda}a_J(x)\right)
\le
\psi\!\left(
\frac{2}{\lambda}[d(x,S)+\delta_J(x)]
\right).
\tag{8.7}
\]

因此，若某 \(K>0,\theta>0\) 满足

\[
\mathcal A_J(r)\le Kr^\theta
\quad(0<r\le r_0),
\tag{8.8}
\]

并把 \(r_0\) 缩小到

\[
\mathcal A_J(r)<\frac{\lambda\eta_\psi}{2},
\qquad
\frac{2K}{\lambda}r^\theta<\eta_\psi
\quad(0<r\le r_0).
\tag{8.8a}
\]

则所有 envelope gauge arguments 都在定义域内，且

\[
\sup_{\substack{x\in U\\0<d(x,S)\le r}}d(Jx,S)
\le
\psi\!\left(\frac{2}{\lambda}\mathcal A_J(r)\right)
\le
\psi\!\left(\frac{2K}{\lambda}r^\theta\right).
\tag{8.9}
\]

在 power case \(\psi(t)=\rho t^q\)、\(q>1\) 中，

\[
\boxed{
d(Jx,S)
\le
\rho(2K/\lambda)^q\,d(x,S)^{\theta q}.}
\tag{8.10}
\]

这是 uniform upper exponent。

**Proof.**
对每个 \(p\in P_S(y)\)，

\[
\bigl|\|x-p\|-\|x-y\|\bigr|\le\|y-p\|=d(y,S).
\]

取 infimum 得

\[
\bigl|a_J(x)-\lambda\|w\|\bigr|
\le d(y,S)
\le\psi(\|w\|).
\tag{8.11}
\]

小量条件于是给 \(a_J(x)\ge\lambda\|w\|/2\)，即
\(\|w\|\le2a_J(x)/\lambda\)。用
\(r_F(y)\le\|w\|\)、\(\psi\) 非减及 Lemma 8.1，得到 (8.7)；
在 (8.8a) 下取 local supremum 得 (8.9)，代入 power gauge 得
(8.10)。
\(\square\)

### Proposition 8.3（无 proximinality 的 approximate-anchor 版本）

令

\[
\psi:[0,\eta_\psi)\to[0,+\infty),
\qquad
e:[0,\eta_\psi)\to[0,+\infty)
\]

其中 \(\psi\) 有限、非减。考虑满足

\[
0<t:=\|w(x)\|<\eta_\psi,
\qquad
d(Jx,S)\le\psi(r_F(Jx))
\tag{8.11a}
\]

的相关 inputs，并定义

\[
a_{J,e}(x)
:=d\bigl(x,P_S^{e(\|w\|)}(Jx)\bigr).
\]

假设对每个相关 nonzero attained \(t=\|w\|\)，该 approximate
projection set 非空；在不假设 proximinality 时，一个充分条件是
\(e(t)>0\)。

若存在 \(0\le\kappa<1\)，使所有充分小 attained \(t=\|w\|>0\)
满足

\[
\psi(t)+e(t)\le\kappa\lambda t,
\tag{8.12}
\]

且

\[
\frac{a_{J,e}(x)}{(1-\kappa)\lambda}<\eta_\psi,
\tag{8.12a}
\]

则

\[
d(Jx,S)
\le
\psi\!\left(
\frac{a_{J,e}(x)}{(1-\kappa)\lambda}
\right).
\tag{8.13}
\]

**Proof.**
对 \(p\in P_S^{e(t)}(Jx)\)，

\[
\|x-p\|
\ge\lambda t-d(Jx,S)-e(t)
\ge(1-\kappa)\lambda t.
\]

取 infimum，解出 \(t\)，再用 error bound 与 \(\psi\) 非减。
\(\square\)

当 \(\psi=o(\mathrm{id})\) 时，(8.11) 还说明

\[
a_J(x)=\lambda\|w(x)\|(1+o(1)).
\tag{8.14}
\]

因此 composition inequality 在分析上与 residual-step estimate
同阶；其结构作用是显式分离 normal distance 与 nearest-solution drift，
而不是凭空产生一个独立 rate law。isolated zero 时
\(\delta_J=0\)、\(\theta=1\)；非孤立时 drift 可使
\(\theta<1\)。

## 9. Sharpness 边界

对

\[
\Omega_J(r)
:=\sup_{\substack{x\in U\\0<d(x,S)\le r}}d(Jx,S),
\]

并同样约定空 supremum 为 \(0\)。

称 \(p>0\) 在 map-level two-sided witness 意义下为 exact local
exponent，若 \(\Omega_J(r)=O(r^p)\)，且存在
\(x_n\to S\)、\(r_n=d(x_n,S)\downarrow0\) 与 \(c>0\)，使

\[
d(Jx_n,S)\ge cr_n^p.
\tag{9.1}
\]

对实际非终止轨道，two-sided exact exponent 使用 (5.9)；
positive finite normalized limit，即 (5.10) 的 exact Q-factor，
是更强结论。

### Proposition 9.1（joint saturation）

沿同一 local sequence，记

\[
r_n=d(x_n,S),\quad
a_n=a_J(x_n),\quad
t_n=\|w(x_n)\|,\quad
s_n=d(Jx_n,S).
\]

若

\[
a_n\asymp r_n^\theta,\qquad
t_n\asymp a_n,\qquad
s_n\asymp t_n^q,
\tag{9.2}
\]

则 \(s_n\asymp r_n^{\theta q}\)。若进一步

\[
\frac{a_n}{r_n^\theta}\to A>0,\quad
\frac{t_n}{a_n}\to B>0,\quad
\frac{s_n}{t_n^q}\to C>0,
\]

则

\[
\frac{s_n}{r_n^{\theta q}}\to CB^qA^q.
\tag{9.3}
\]

**Proof.**
将三个 two-sided 关系或三个 normalized ratios 相乘。 \(\square\)

\(\theta\) 与 \(q\) 在不同 sequences 上分别 sharp，不足以推出
\(\theta q\) sharp；必须由同一 sequence joint saturation。

令

\[
P_a(t):=\operatorname{sgn}(t)|t|^a.
\]

以下 GX-071--GX-073 均取生成步长 \(\lambda=1\)。

### Example 9.2（GX-071：exact \(\gamma q\) 的 attainability witness）

取

\[
0<\gamma<1,\qquad q>1/\gamma,\qquad
\alpha:=\gamma q>1,\qquad \lambda=1,
\]

\[
J(t,z):=(t+|z|^\gamma,P_\alpha z),
\qquad
S=\mathbb R\times\{0\}.
\tag{9.4}
\]

\(J\) 是 global triangular bijection；由 \(F=J^{-1}-I\) 得

\[
F(s,u)=\bigl(-|u|^{1/q},P_{1/\alpha}u-u\bigr).
\tag{9.5}
\]

对 \(x=(t,z)\)、\(r=|z|\)，

\[
d(x,S)=r,\qquad d(Jx,S)=r^\alpha=r^{\gamma q}.
\tag{9.6}
\]

input/output projections 为

\[
p_x=(t,0),\qquad p_y=(t+r^\gamma,0),
\]

故

\[
\delta_J(x)=r^\gamma,\qquad
a_J(x)=\sqrt{r^{2\gamma}+r^2}\sim r^\gamma.
\tag{9.7}
\]

又

\[
w=x-Jx=(-r^\gamma,z-P_\alpha z),
\qquad
\|w\|\sim r^\gamma,
\tag{9.8}
\]

且从 (9.5)

\[
r_F(s,u)^2
=|u|^{2/q}+|P_{1/\alpha}u-u|^2,
\]

所以 \(d((s,u),S)\le r_F(s,u)^q\)，endpoint exponent \(q\)
沿 \(u\to0\) 被 attained。于是

\[
\frac{a_J(x)}{r^\gamma}\to1,\qquad
\frac{\|w\|}{a_J(x)}\to1,\qquad
\frac{d(Jx,S)}{\|w\|^q}\to1,
\]

并且

\[
\frac{d(Jx,S)}{d(x,S)^{\gamma q}}=1.
\tag{9.9}
\]

在任意 bounded tube 上，

\[
R(t,z)=(t+2|z|^\gamma,\,2P_\alpha z-z)
\]

为 \(\gamma\)-Hölder：\(|\,|z|^\gamma-|z'|^\gamma|\le|z-z'|^\gamma\)，
其余 linear/local-Lipschitz increments 在 bounded domain 上可降为
\(\gamma\)-Hölder。取 \((t,z)\) 与 \((t,0)\) 时 quotient 趋于 \(2\)，
故 exponent \(\gamma\) 不能提高。

轨道满足

\[
r_{k+1}=r_k^\alpha,\qquad
t_{k+1}=t_k+r_k^\gamma.
\]

若 \(0<r_0<1\)，则

\[
\sum_{k\ge0}r_k^\gamma
\le
\frac{r_0^\gamma}{1-r_0^{\gamma(\alpha-1)}}.
\tag{9.10}
\]

因此 positive tangential margin 给出 invariant RL subwindow；整个
rectangle 不是 self-map。

**Verdict.**
GX-071 证明 \(\theta q=\gamma q\) 在声明 class 中可 attained，且有
normalized limit \(1\)。它是 reverse-calibrated power-shear witness，
不证明 genericity、necessity 或 universal compensation；optimal
restricted RL constant 仍未知。

### Example 9.3（GX-072：all-pairs \(\gamma\)，但 alignment \(1\)、orbit \(q\)）

取

\[
q>1,\qquad0<\gamma<1,\qquad
\beta:=q/\gamma-1,
\]

\[
h(0):=0,\qquad
h(x):=|x|^q\sin(|x|^{-\beta})\quad(x\ne0),
\]

\[
J(x,y):=(P_qx,P_qy+h(x)).
\tag{9.11}
\]

\(J\) 是 global triangular homeomorphism；令

\[
F:=J^{-1}-I,\qquad R:=2J-I\qquad(\lambda=1).
\]

其零点在足够小
localization 中 isolated。因而

\[
\delta_J(z)=0,\qquad a_J(z)=\|z\|,
\]

alignment exponent 为 \(1\)。直接分情况估计给

\[
2^{-1-q/2}\|z\|^q
\le\|Jz\|
\le\sqrt5\,\|z\|^q.
\tag{9.12}
\]

故充分小 ball invariant，每个非零 orbit 有 uniform two-sided
\(q\)-scaling，即 two-sided exact exponent \(q\)。

对 generated \(F\)，写

\[
u:=Jz,\qquad w:=z-u\in F(u).
\]

由 (9.12)，\(\|u\|=\Theta(\|z\|^q)=o(\|z\|)\)，故

\[
\frac{\|w\|}{\|z\|}\to1,
\qquad
d(u,S)=\|u\|=\Theta(\|w\|^q).
\tag{9.12a}
\]

由于 \(J\) 是 bijection，每个 nearby \(u\) 的 residual 唯一，
所以这是 full \(q\)-MSR，而非 selected-branch 标签。取 phase-zero
\(\xi_n:=(\pi n)^{-1/\beta}\) 与 \(z_n=(\xi_n,0)\)，有
\(Jz_n=(\xi_n^q,0)\)；故任何 power \(p>q\) 都失败。

函数 \(h\) 的 two-scale estimate 给

\[
|h(x)-h(y)|\le C|x-y|^{q/(\beta+1)}
=C|x-y|^\gamma.
\]

为闭合 sharpness 证据链，取 adjacent phase-extremum points

\[
s_n:=2\pi n+\frac{\pi}{2},\qquad
t_n:=s_n+\pi,\qquad
x_n:=s_n^{-1/\beta},\qquad
y_n:=t_n^{-1/\beta}.
\tag{9.12b}
\]

则

\[
|x_n-y_n|
\sim\frac{\pi}{\beta}s_n^{-1/\beta-1},
\qquad
h(x_n)-h(y_n)
\sim2s_n^{-q/\beta}.
\tag{9.12c}
\]

由于 \(\gamma(1+1/\beta)=q/\beta\)，且 reflector 的 oscillatory
coordinate 是 \(2h\)，

\[
\frac{
\|R(x_n,0)-R(y_n,0)\|
}{
|x_n-y_n|^\gamma
}
\longrightarrow
4\left(\frac{\beta}{\pi}\right)^\gamma.
\tag{9.12d}
\]

故任何大于 \(\gamma\) 的 all-pairs exponent 均失败。于是 reflector
的 maximal local all-pairs exponent 是 \(\gamma\)，但

\[
\text{actual orbit order }q>\gamma q.
\]

**Verdict.**
GX-072 判决 all-pairs roughness 只能给 admissible、可能保守的
alignment exponent；不能把 \(\gamma q\) 称为 universal exact
exponent 或 Q-factor。
(9.12) 给 two-sided exact exponent \(q\)，但 oscillatory phase 未证明 normalized
ratio 收敛，故不声称 positive finite limit。其构造同样经过频率反向校准。

### Example 9.4（GX-073：one-step scale 不等于 convergence order）

在自然 Minty 域 \([-\delta,\delta]\)，取

\[
0<\alpha<1,\qquad\beta>0,\qquad0<\delta<1,\qquad\lambda=1,
\]

\[
R(0):=0,\qquad
R(x):=P_\alpha(x)[2+\sin(|x|^{-\beta})]\quad(x\ne0),
\qquad
J:=\frac{I+R}{2}.
\tag{9.13}
\]

定义 underlying relation

\[
\operatorname{gph}F
:=\Gamma_R^1
=\{(Jx,x-Jx):x\in[-\delta,\delta]\}.
\tag{9.13a}
\]

其 local solution set 为 \(\{0\}\)。against-zero bound 为

\[
|x|^\alpha\le|R(x)|\le3|x|^\alpha,
\]

所以 anchored exponent 是 \(\alpha\)，exact local constant 为 \(3\)。
取与 (9.12b) 相同的 adjacent phase-extremum points，并令

\[
\eta_*=\frac{\alpha}{\beta+1}<\alpha.
\]

则

\[
R(x_n)-R(y_n)\sim2s_n^{-\alpha/\beta},
\qquad
|x_n-y_n|^{\eta_*}
\sim
\left(\frac{\pi}{\beta}\right)^{\eta_*}
s_n^{-\alpha/\beta},
\tag{9.13b}
\]

从而

\[
\frac{|R(x_n)-R(y_n)|}{|x_n-y_n|^{\eta_*}}
\longrightarrow
2\left(\frac{\beta}{\pi}\right)^{\eta_*}.
\tag{9.13c}
\]

结合相应 two-scale upper bound，maximal all-pairs exponent 为
\(\eta_*\)。

若 \(r=|x|>0\) 且
\(c(x):=2+\sin(r^{-\beta})\in[1,3]\)，则

\[
r_+:=|Jx|
=\frac{r+c(x)r^\alpha}{2},
\qquad
\frac12r^\alpha\le r_+\le2r^\alpha.
\tag{9.14}
\]

因为 \(0<r<1\)、\(\alpha<1\)，有 \(r_+>r\)。若非零 orbit 永远
留在自然域，则单调 radii 收敛到某个 \(0<\ell<1\)；在 \(\ell\) 处
连续性迫使
\(\ell^{1-\alpha}=c(\ell)\ge1\)，矛盾。因此它有限步离开自然域。
对 (9.13a) 中任意 local graph representation，令
\(u:=Jx\)、\(w:=x-Jx\)。则

\[
|u|=\frac{r+c(x)r^\alpha}{2},
\qquad
|w|=\frac{c(x)r^\alpha-r}{2},
\]

并且

\[
\frac{|u|}{|w|}
=
\frac{c(x)+r^{1-\alpha}}{c(x)-r^{1-\alpha}}
\longrightarrow1
\tag{9.14a}
\]

uniformly over \(c(x)\in[1,3]\)，因而也 uniformly over every
local preimage of the same \(u\)。对 residual infimum 取极限得到

\[
\frac{d(u,S)}{r_F(u)}\to1.
\tag{9.14b}
\]

故 full fixed-target regularity 的 maximal power 为 \(1\)，exact
linear modulus 为 \(1\)，并不满足本章的 superlinear \(q>1\) premise。

**Verdict.**
GX-073 的 \(\Theta(r^\alpha)\) 是精确 one-step scale，不是收敛阶；
它判决 scalar contraction 与 invariant domain 不能从 exponent 标签
中省略。

### 三例总判决

| 例 | all-pairs / anchored | full error-bound / alignment | 动力学 | 可支持的 claim |
|---|---|---|---|---|
| GX-071 | bounded-tube all-pairs exponent \(\gamma\) | full endpoint \(q\)，alignment \(\theta=\gamma\) | exact \(r_+=r^{\gamma q}\)，需 tangential margin | \(\theta q\) attainability 与 normalized limit \(1\) |
| GX-072 | maximal all-pairs \(\gamma\)，anchored/fixed exponent \(1\) | isolated，alignment \(1\)，full endpoint \(q\) | uniform two-sided \(q\)-scaling；Q-factor 未证 | all-pairs \(\gamma q\) 可严格保守 |
| GX-073 | anchored \(\alpha\)，all-pairs \(\alpha/(\beta+1)\) | full maximal power \(1\) | expansion 并有限 escape | one-step exponent 不是 convergence order |

## 10. Theorem dependency / assumption ledger

### 10.1 依赖图谱

| 结果 | 直接依赖 | 不依赖 / 不推出 |
|---|---|---|
| Theorem 1.1 | Minty--Cayley 坐标、all-pairs quantifier | coverage、maximality、闭性 |
| Proposition 1.3 | 任意 map 的 Cayley pullback | operator-side coverage、regularity interaction |
| Proposition 1.4 | all-pairs injectivity + coverage；full equality另需 exclusion | invariance |
| Theorem 2.1 | 纯代数 | 文献新颖性、固定参数下无规则 scaling |
| Proposition 3.1 | all-pairs RL、coverage、zero-anchor distance equality | output error bound、orbit convergence |
| Lemma 4.1 | named branch B、anchored A、output E | all-pairs RL、projection存在 |
| Theorem 4.2 | Lemma 4.1、scalar limsup \(<1\)、strict margin、endpoint-wide A | \(S\) closed、\(T\) continuous、global self-map、exclusion |
| Corollaries 5.1--5.3 | Theorem 4.2 + full power E | exact exponent/Q-factor、必要阈值 |
| Theorem 6.1 | superlinear full gauge at output、output-near anchor | RL、branch existence、fixed-anchor law |
| Theorem 7.1 | fixed graph germ、\(q>1\) | full-mapping error bound |
| Proposition 7.2 | superlinear branchwise gauge | literal same-gauge equivalence，除非 dilation-stable |
| Proposition 7.3 | isolation；converse另需 residual completeness | favorable branch \(\Rightarrow\) full bound |
| Theorem 7.4 / Corollary 7.5 | isolated full power/gauge EB、named coverage、output return、small residual | RL；arbitrary full selection |
| Theorem 8.2 | named branch、output full gauge、projection profile、superlinearity | exact \(\theta q\)、all-pairs exponent optimality |
| Proposition 9.1 | 同一 sequence 的三重 two-sided saturation | 不同 sequences 的 marginal sharpness |

### 10.2 易混假设的判别账本

| 轴 | 强/弱对象 | 本稿规则 |
|---|---|---|
| graph scope | full / restricted | global 只表示 full-graph quantifier；restricted 结论只在自然域 |
| pair scope | all-pairs / anchored | all-pairs 可验证 anchored；anchored 不给 injectivity |
| branch scope | full relation / named branch | named branch 不排除 remote full selections |
| domain | coverage / exclusion / invariance | 分别对应存在、full 唯一、轨道合法 |
| error bound | full residual / selected residual | full 用 \(r_F=\inf_{w\in F(y)}\|w\|\)；selected law 需 residual completeness 才可反推 full |
| locality | base neighborhood / residual window | gauge convention 双局部化；power 可缩邻域等价 |
| solution geometry | isolated / nonisolated | isolated drift 为零；nonisolated 需 alignment profile |
| rate strength | upper order / two-sided exact exponent / exact Q-factor | 三层逐级增强，不互相替代 |
| sharpness | coverage / exclusion / invariance / exponent | 一个反例只判决其实际测试的层，不作 universal seesaw |

## 11. 保留的边界与待审问题

1. RL 正式命名未锁；\(\gamma=1\) 应继续作为已知 semimonotonicity
   参数字典，而非定义级贡献。
2. local gauge--PPA 的 step 常数与 critical coefficient 的 joint
   optimality 未知；现有值只属 sufficient route。
3. GX-071 的 optimal restricted all-pairs RL constant、GX-072/073 的
   optimal endpoint all-pairs constants仍未知，但不影响 exponent 判决。
4. output-anchor/alignment 结构与 Wang--Li--Ng 2023、
   Moursi--Vanderwerff 2025 的 theorem-level overlap 仍待 full-text
   核验；阴性检索不是 novelty proof。
5. 尚无 application-derived、非 reverse-calibrated 的 exact
   \(\theta q\) witness。GX-071 只证明 attainable，不证明 natural 或
   universal。
6. 若将 Assumption A 从所有 active inputs 弱化为只沿 orbit 成立，
   endpoint membership 必须改由 local closedness of \(S\) 或足够的
   continuity/closed-graph 机制闭合。
