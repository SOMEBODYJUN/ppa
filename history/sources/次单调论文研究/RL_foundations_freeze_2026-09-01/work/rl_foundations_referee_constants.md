# RL 基础层独立审稿：常数、边界情形与 GX-071--074 压力测试

> Project: monotonicity-regularity-seesaw-2026-09  
> Task: RL-FND-REF-CONST-06  
> Role: 独立 max 数学审稿人  
> 审查对象：work/rl_foundations_definitions.md；work/rl_foundations_ppa_theorem.md  
> 原文件修改：无  
> 文献检索：未进行（按任务禁止）

## 0. 总裁决

两份候选稿的核心代数与局部 PPA 收敛证明通过独立复算。没有发现会
推翻 RL--IP、inverse/scaling、Theorem 3.1 或 power recurrence 的错误。

总状态为 **PASS_AFTER_REPAIR**：

| 类型 | 数量 | 结论 |
|---|---:|---|
| 核心定理 FAIL | 0 | 未发现错误常数或反例 |
| 实质内容 PASS | 17 | 主代数链和主收敛链闭合 |
| 冻结前 REPAIR | 4 | 两个边界/术语修复，两个假设接口澄清 |

四项修复是：

1. 定义稿的 \(L>0\) 与 PPA 稿的 \(L\ge 0\) 必须统一，并单列
   \(L=0\) 的 \(q\)-phase；
2. 区分 upper order、two-sided exact exponent 和 exact Q-factor；
3. 说明 endpoint-quantified A 与 B 已隐含 \(S\) 在 \(U\) 中相对闭；
4. 若从标准 at-\((\bar u,0)\) local GMSR 导入 E，还要验证
   \(Tx\) 位于 error-bound 的 base neighborhood。

这些修复不改变已经显示的 \(1/2\)、\(1+L\)、
\(\rho(L/(2\lambda))^q\) 或
\(\rho(1+L)/(2\lambda)\)。

---

## 1. 定义层逐项复算

### D-01. Minty--Cayley 重构

**PASS.** 若

\[
x=u+\lambda u^*,\qquad r=u-\lambda u^*,
\]

则

\[
u=\frac{x+r}{2},\qquad
u^*=\frac{x-r}{2\lambda}.
\]

因此相同 Minty input 与相同 Cayley output 唯一恢复 graph point。

### D-02. RL 的内积形式

**PASS.** 置

\[
a=u-v,\qquad b=u^*-v^*,\qquad
t=\|a+\lambda b\|.
\]

恒等式

\[
\|a-\lambda b\|^2
=t^2-4\lambda\langle a,b\rangle
\]

给出精确等价

\[
\|a-\lambda b\|\le \omega(t)
\iff
\lambda\langle a,b\rangle
\ge \frac14\bigl(t^2-\omega(t)^2\bigr).
\]

两边非负，所以平方没有引入伪解。power 情形的
\(L^2t^{2\gamma}\) 与 \(1/4\) 均正确。

### D-03. all-pairs RL 与 Minty injectivity

**PASS.** 若 \(M_\lambda z=M_\lambda z'\)，RL 的右端为
\(\omega(0)=0\)，故 \(C_\lambda z=C_\lambda z'\)，再由 D-01
得到 \(z=z'\)。

该结论确实依赖 all-pairs 量词；point-/solution-anchored RL
不能比较两个 moving points。定义稿已经正确区分。

### D-04. firm-type characterization

**PASS.** 对 \(T=J_{\lambda,\Gamma}\)，令

\[
a=Tx-Ty,\qquad
c=(I-T)x-(I-T)y=\lambda b.
\]

则 \(x-y=a+c\)，而 \(Rx-Ry=a-c\)，所以

\[
\|a\|^2+\|c\|^2
=\frac12\bigl(\|x-y\|^2+\|Rx-Ry\|^2\bigr).
\]

这精确给出原稿的 firm-type 公式。coupled relational 版本中取
\(x=y\)，左端为 \(2\|u-v\|^2\)、右端为零，确实强迫单值。

### D-05. \(\gamma=1\) tied semimonotonicity

**PASS，包括 \(L=0\) 的代数延拓。** 展开

\[
\|a-\lambda b\|^2
\le L^2\|a+\lambda b\|^2
\]

得到

\[
2\lambda(1+L^2)\langle a,b\rangle
\ge
(1-L^2)\bigl(\|a\|^2+\lambda^2\|b\|^2\bigr).
\]

因此

\[
\theta_L=\frac{1-L^2}{2(1+L^2)},\qquad
\mu_L=\frac{\theta_L}{\lambda},\qquad
\rho_L=\lambda\theta_L=\lambda^2\mu_L
\]

全部正确。参数边界为：

| \(L\) | \(\theta_L\) | 结论 |
|---:|---:|---|
| \(0<L<1\) | \(>0\) | positive tied semimonotonicity |
| \(L=1\) | \(0\) | ordinary monotonicity |
| \(L>1\) | \(<0\) | negative tied semimonotonicity |
| \(L=0\) | \(1/2\) | \(a=\lambda b\)，reflector 常值 |

最后一行说明公式本身没有理由排除 \(L=0\)。

### D-06. Luke--Tam 型参数

**PASS.** 当 \(L\ge1\)，

\[
\tau_L=\frac{L^2-1}{4}
\]

精确给出

\[
\lambda\langle a,b\rangle
\ge-\tau_L\|a+\lambda b\|^2.
\]

反向恢复 \(L=\sqrt{1+4\tau_L}\)。该等价只是代数换算，
不携带 maximality、满域或局部图假设；原稿已正确限定。

### D-07. inverse rule

**PASS.** inverse graph 的差分是 \((b,a)\)，且

\[
\|b-\lambda^{-1}a\|
=\lambda^{-1}\|a-\lambda b\|,
\]

\[
\|b+\lambda^{-1}a\|^\gamma
=\lambda^{-\gamma}\|a+\lambda b\|^\gamma.
\]

所以新常数满足

\[
L'\lambda^{-\gamma}=L\lambda^{-1},
\]

即

\[
\boxed{L'=L\lambda^{\gamma-1}}.
\]

再次 inverse 后恢复 \(L\)。\(\gamma=1\) 时常数不变；
\(0<\gamma<1\) 时它依赖 \(\lambda\) 与单位缩放。

### D-08. positive output scaling

**PASS，建议文字澄清。** 在 \(c\Gamma\) 上 output difference
为 \(cb\)，取新 step \(\lambda/c\) 后

\[
(\lambda/c)(cb)=\lambda b.
\]

因此

\[
\Gamma\in{\rm RL}(\lambda,L,\gamma)
\iff
c\Gamma\in{\rm RL}(\lambda/c,L,\gamma).
\]

等价的固定新 step 写法为

\[
c\Gamma\in{\rm RL}(\mu,L,\gamma)
\iff
\Gamma\in{\rm RL}(c\mu,L,\gamma).
\]

建议用这两式替换“参数回到 \(c\lambda\) 或 \(\lambda/c\)”的口语句，
避免读者混淆哪个参数属于哪个 graph。这不是公式错误。

### D-09. \(L=0\) convention

**REPAIR-1.** 定义稿把 power modulus 和 inverse rule 写成
\(L>0\)，PPA 稿从一开始允许 \(L\ge0\)，且主证明对 \(L=0\)
完全有效。最终基础稿若不修复会自相矛盾。

推荐统一为

\[
\boxed{L\ge0,\qquad0<\gamma\le1.}
\]

并注明：当 \(L=0\) 时，
\(C_\lambda z=C_\lambda z'\)，即 restricted reflector 常值；
\(\gamma\) 不可识别，任何 sharp-\(\gamma\) 主张都无意义。
Propositions 7.2、8.2、8.3 的代数均可直接包含 \(L=0\)。

---

## 2. 一步估计与局部 PPA 主定理

### P-01. named Minty branch

**PASS.** Assumption B 给

\[
\sigma(x)=(Tx,Vx),\qquad
x=Tx+\lambda Vx,
\]

所以

\[
Vx=\frac{x-Tx}{\lambda}\in F(Tx).
\]

它是明确的 range coverage，不排除 \(G\) 外的 full-resolvent
branches。算法对象与 full relation 的区分正确。

### P-02. epsilon-nearest anchors 与 \(1/2\)

**PASS.** 恒等式

\[
2(x-Tx)=(x-p_n)-(2Tx-x-p_n)
\]

给出

\[
2\|x-Tx\|
\le \|x-p_n\|+L\|x-p_n\|^\gamma.
\]

令 \(\|x-p_n\|\to r=d(x,S)\) 得

\[
\boxed{
\|x-Tx\|\le\frac12(r+Lr^\gamma).
}
\]

不需要 \(S\) proximinal。\(1/2\) 在 A 的信息层面不能普遍改小：
若某 anchored pair 满足

\[
x-p=re,\qquad Rx-p=-Lr^\gamma e,
\]

则三角不等式取等，step 恰为
\((r+Lr^\gamma)/2\)。

### P-03. selected residual 与 gauge recurrence

**PASS.** 由 selected graph residual

\[
d(0,F(Tx))
\le\frac{\|x-Tx\|}{\lambda}
\le\frac{r+Lr^\gamma}{2\lambda}.
\]

E 与 \(\psi\) 非减给

\[
\boxed{
d(Tx,S)\le
\Phi_\gamma(r):=
\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right).
}
\]

方向正确；原稿没有把 selected residual 错当成最小 residual。

### P-04. limsup contraction

**PASS.** 若

\[
c_\gamma=
\limsup_{r\downarrow0}\frac{\Phi_\gamma(r)}r<1,
\]

则任取 \(c_\gamma<\theta<1\)，按 limsup 定义存在
\(\delta_\theta>0\)，使

\[
\Phi_\gamma(r)\le\theta r
\quad(0<r\le\delta_\theta).
\]

\(r=0\) 被单独处理，不依赖商式。

### P-05. finite-length margin

**PASS.** 由 \(r_k\le\theta^kr_0\) 得

\[
\|x^{k+1}-x^k\|
\le
\frac12\left(
\theta^kr_0+
L\theta^{\gamma k}r_0^\gamma
\right).
\]

求和得到

\[
\boxed{
B_\gamma(r_0,\theta)
=\frac12\left(
\frac{r_0}{1-\theta}
+
\frac{Lr_0^\gamma}{1-\theta^\gamma}
\right).
}
\]

因此

\[
\|x^0-\bar x\|+B_\gamma(r_0,\theta)<R
\]

确实保证所有有限 iterates 与极限均在开球 \(U\) 内。
从第 \(k\) 步重新求和也给

\[
\|x^k-x^\infty\|
\le B_\gamma(r_k,\theta).
\]

### P-06. \(r=0\)、非闭 \(S\) 与 endpoint

**PASS WITH REPAIR-2.** 若 \(r=0\)，P-02 给 \(Tx=x\)，
B 再给

\[
0=\frac{x-Tx}{\lambda}\in F(x),
\]

所以 \(x\in S\)。endpoint proof 正确，且不需要另外调用
\(S\) closed 或 \(T\) continuous。

但 B+A 同时已经隐含

\[
\boxed{U\cap\overline S=U\cap S.}
\]

因此“No closedness is needed”应解释为“不把 closedness 另列为假设”，
而不是允许 A 与 \(U\) 内的非闭零集极限点并存。

最小修复是在相关句后增加：

> B 与 endpoint-quantified A 已蕴含 \(S\) 在 \(U\) 中相对闭。

### P-07. 不连续 \(T\)

**PASS.** proof 没有使用
\(Tx^k\to Tx^\infty\)；它在 \(x^\infty\) 重新调用 A。
第 5.4 节给出 \(T\) 在每个非零点不连续但定理仍成立的模型。

### P-08. 从 local GMSR 导入 E

**REPAIR-3，接口说明而非定理错误。** Theorem 3.1 直接在所有相关
outputs \(Tx\) 上假设 E，所以 proof 正确。

若最终稿改由 Definition 6.2 的 at-\((\bar u,0)\) local GMSR
推出 E，除 residual cutoff 外还必须验证

\[
Tx\in U_{\rm EB}.
\]

只缩小 active distance \(\delta\) 会使 selected residual 变小，
但不一定使 \(Tx\) 靠近固定 \(\bar u\)；非孤立 \(S\) 时尤其如此。

建议添加：

> 若 E 由标准 local GMSR 推出，还需另证 relevant outputs
> 位于其 base neighborhood；本定理直接假设 output-relative E。

### P-09. all-pairs branch verification

**PASS.** all-pairs RL 给 \(M_\lambda|_G\) injective；
coverage 后可定义 \(\sigma\)；distance equality (4.3) 给
\(S_G\) 中 epsilon-nearest anchors。full resolvent 唯一性仍需

\[
M_\lambda^{-1}(U)\cap\operatorname{gph}F
\subset G.
\]

restricted uniqueness 没有被偷换成 full uniqueness。

---

## 3. power bounds、临界系数与 order

### Q-01. 总 recurrence

**PASS.** 对 \(\psi(t)=\rho t^q\)，

\[
\boxed{
r_+
\le
\frac{\rho}{(2\lambda)^q}
(r+Lr^\gamma)^q.
}
\]

### Q-02. \(0<\gamma<1,\ L>0\)

**PASS.** 因为

\[
r+Lr^\gamma
=r^\gamma(r^{1-\gamma}+L),
\]

在 \(0\le r\le\delta_0\) 上

\[
r_+\le C_{\delta_0}r^{\gamma q},
\]

\[
C_{\delta_0}
=
\frac{\rho}{(2\lambda)^q}
(\delta_0^{1-\gamma}+L)^q.
\]

令 \(p=\gamma q\)：

- \(p>1\)：\(C_{\delta_0}\delta_0^{p-1}\to0\)，可取严格 contraction；
- \(p=1\)：临界充分系数为
  \[
  \boxed{
  \kappa_\gamma
  =\rho\left(\frac{L}{2\lambda}\right)^q;
  }
  \]
- \(p<1\)：该 upper bound 不推出 convergence 或 divergence。

非有限终止且 \(p>1\) 时，

\[
\frac{r_{k+1}}{r_k}
\le C_{\delta_0}r_k^{p-1}\to0.
\]

### Q-03. \(\gamma=1\)

**PASS.** 两项同阶，故

\[
\boxed{
r_+\le A_1r^q,\qquad
A_1=
\rho\left(\frac{1+L}{2\lambda}\right)^q.
}
\]

当 \(q=1\)，严格充分系数是

\[
\boxed{
\kappa_1=
\rho\frac{1+L}{2\lambda}.
}
\]

不能删掉 \(1\)。原稿的 \(\gamma=1\) 常数正确。

### Q-04. gauge-envelope tests

**PASS.** 当 \(0<\gamma<1\)、\(L>0\)，

\[
t(r)=
\frac{r+Lr^\gamma}{2\lambda}
=
r^\gamma
\frac{r^{1-\gamma}+L}{2\lambda},
\]

所以

\[
\frac{\psi(t(r))}{r}
=
\frac{\psi(t(r))}{t(r)^{1/\gamma}}
\left(
\frac{r^{1-\gamma}+L}{2\lambda}
\right)^{1/\gamma}.
\]

因此

\[
\limsup_{t\downarrow0}
\frac{\psi(t)}{t^{1/\gamma}}
<
\left(\frac{2\lambda}{L}\right)^{1/\gamma}
\]

确实充分。对 \(\gamma=1\)，阈值
\(2\lambda/(1+L)\) 也正确。两者均未被误称为必要条件。

### Q-05. \(L=0\) 的遗漏 branch

**REPAIR-1 的定理侧补充。** 当 \(L=0\)，无论打印哪个 \(\gamma\)，

\[
\boxed{
r_+
\le
\frac{\rho}{(2\lambda)^q}r^q.
}
\]

phase 由 \(q\) 而非 \(\gamma q\) 决定：

- \(q>1\)：local upper order \(q\)；
- \(q=1\)：临界充分条件 \(\rho/(2\lambda)<1\)；
- \(q<1\)：该 bound 单独不推出 contraction。

Corollary 5.1 以 \(L>0\) 正确避开了错误，但完整基础稿应单列此边界。

### Q-06. upper order 与 exact Q-factor

**REPAIR-4.** 原稿正确说明
\(O(r_k^p)\) 只是 upper order。式 (5.16)

\[
0<
\liminf\frac{r_{k+1}}{r_k^p}
\le
\limsup\frac{r_{k+1}}{r_k^p}
<\infty
\]

给出 two-sided \(\Theta(r_k^p)\) 或 exact exponent \(p\)，
但不保证 quotient 有极限。

例如

\[
r_{k+1}=a_kr_k^p,\qquad
a_k=
\begin{cases}
1,&k\ \text{even},\\
2,&k\ \text{odd},
\end{cases}
\]

对足够小 \(r_0\) 收敛，normalized quotient 有正 liminf 和有限
limsup，但没有 exact Q-factor。

建议冻结三层语言：

1. \(r_{k+1}=O(r_k^p)\)：upper order；
2. \(r_{k+1}=\Theta(r_k^p)\)：two-sided exact exponent；
3. \(r_{k+1}/r_k^p\to c\in(0,\infty)\)：exact Q-order with factor \(c\)。

PPA corollaries 当前只主张第一层，安全。GX-071 给第三层且 factor 1；
GX-072 当前上下界只直接给第二层，除非另证 orbit quotient 的极限。

### Q-07. 临界系数的 claim strength

**PASS.** \(\kappa_\gamma\) 与 \(\kappa_1\) 被称为 Lemma 2.1
产生的严格充分系数，没有声称 necessary、optimal 或 sharp。
等于或大于 1 只表示该 proof inconclusive。第 5.6 节给出实际收敛但
该 scalar certificate 失败的模型。

---

## 4. GX-071--074 压力测试

### GX-071：精确 \(\gamma q\) 与切向漂移

**PASS.** 模型满足

\[
t_{k+1}=t_k+r_k^\gamma,\qquad
r_{k+1}=r_k^\alpha,\qquad
\alpha=\gamma q>1.
\]

normal distance 的 Q-factor 精确为 1，但总位移含
\(r_k^\gamma\) tangential drift。其预算

\[
\sum_{k\ge0}r_k^\gamma
\le
\frac{r_0^\gamma}
{1-r_0^{\gamma(\alpha-1)}}
\]

说明仅有 \(d(x^0,S)\) 小不能保证 rectangle self-map；
切向 margin 有实质作用。该例是 reverse-calibrated attainability，
不证明普遍 \(\gamma q\) 规律。

### GX-072：all-pairs exponent 与 anchored exponent 分离

**PASS.** maximal all-pairs exponent 是 \(\gamma\)，但 against
\(S=\{0\}\) 的 anchored exponent 是 1，且

\[
\|Jz\|=\Theta(\|z\|^q).
\]

机械使用 all-pairs certificate 只给 \(O(r^{\gamma q})\)，使用真实
anchored geometry 则给 \(O(r^q)\)。当前证据直接支持 two-sided
exact exponent \(q\)；exact Q-factor 需另证 quotient 极限。

### GX-073：one-step scaling 不是收敛率

**PASS.** anchored exponent \(\alpha<1\)，full-map linear MSR
的 \(q=1\)，并且

\[
\frac12r^\alpha\le |Jx|\le2r^\alpha.
\]

小的非零点会扩张并离开窗口。它不反驳 Theorem 3.1，因为 scalar
condition 正好失败；它反驳把 one-step power law 直接称为 rate。

### GX-074：natural-domain RL 不产生 coverage

**PASS.** 离散 graph 有

\[
D_\lambda(F)=K,\qquad
J=R=I\quad\text{on }K,
\]

并在 bounded natural domain 上满足所有
\(0<\gamma\le1\) 的 RL certificate；fixed-target gauge bounds
又是 domain-vacuous。但 \(K\) 不含 0 周围的 input ball，所以无法启动
Theorem 3.1。RL 与 subregularity 均不替代 B。

### 压力测试总表

| 风险 | 例子 | 裁决 |
|---|---|---|
| 忽略 Minty coverage | GX-074 | 反例否定；B 必须独立 |
| 忽略切向 localization | GX-071 | 反例否定；margin 必须显式 |
| 把 all-pairs \(\gamma q\) 当 actual exact order | GX-072 | 反例否定 |
| 把 one-step power law 当 convergence rate | GX-073 | 反例否定 |

四例都与修复后的 theorem package 相容，没有产生核心 FAIL。

---

## 5. 极端模型

### 5.1 \(L=0\)

取 \(F(u)=u/\lambda\)。则

\[
J_{\lambda F}x=\frac{x}{2},\qquad
R_{\lambda F}x=0,\qquad S=\{0\}.
\]

它对每个 \(0<\gamma\le1\) 都满足
\({\rm RL}(\lambda,0,\gamma)\)。取 \(\psi(t)=\lambda t\)，则

\[
r_+=\frac12r,\qquad
\Phi_\gamma(r)=\frac12r.
\]

这验证 \(L=0\) 主定理有效，也证明此时不能用 \(\gamma q\)
给 phase 命名。

### 5.2 \(\gamma=1\)、非有限终止且常数取等

取

\[
F=\frac{2}{\lambda}I.
\]

则

\[
T=\frac13I,\qquad
R=-\frac13I,\qquad
L=\frac13,\qquad
\rho=\frac{\lambda}{2}.
\]

于是

\[
b_1(r)=\frac23r=\|x-Tx\|,
\]

\[
\kappa_1
=
\frac{\lambda}{2}
\frac{1+1/3}{2\lambda}
=\frac13,
\qquad
r_{k+1}=\frac13r_k.
\]

这同时验证 \(1/2\)、\(1+L\) 与 \(\kappa_1\)。

### 5.3 \(r=0\)

若 \(x\in U\) 且 \(d(x,S)=0\)，A 与 P-02 给 \(Tx=x\)，
B 给 \(0\in F(x)\)。所以在 B+A 下，\(x\notin S\) 的
zero-distance active input 不可能存在。

### 5.4 \(T\) 在每个非零点不连续

令 \(H=\mathbb R\)、\(\lambda=1\)，

\[
F(u)=
\begin{cases}
u,&u\in\mathbb Q,\\
2u,&u\notin\mathbb Q.
\end{cases}
\]

则 full resolvent 为

\[
T(x)=
\begin{cases}
x/2,&x\in\mathbb Q,\\
x/3,&x\notin\mathbb Q,
\end{cases}
\]

并在每个 \(x\ne0\) 不连续。仍有 \(S=\{0\}\)，且

\[
|2Tx-x|\le\frac13|x|.
\]

A 以 \(\gamma=1,L=1/3\) 成立。取 \(\psi(t)=t\)，E 成立且

\[
\Phi_1(r)=\frac23r<r.
\]

有理轨道按 \(1/2\) 收缩，无理轨道按 \(1/3\) 收缩。
Theorem 3.1 不依赖 \(T\) 的全局 continuity。

### 5.5 \(S\) 全局非闭

令 \(\lambda=1\)、\(s_n=2-1/n\)，定义

\[
F(u)=\{u\}\quad(|u|<1/4),\qquad
F(s_n)\ni0,
\]

其余点取空值，并令 \(2\notin S\)。则

\[
S=\{0\}\cup\{s_n:n\ge1\}
\]

全局非闭。在 \(U=(-1/2,1/2)\) 上取 \(T(x)=x/2\)，有
\(R=0,L=0\)，A 对 anchor 0 成立，且 \(\psi(t)=t\) 给 E。
轨道收敛到 0。故不要求全局 closedness 的主张正确；同时
\(S\cap U=\{0\}\) 相对闭，与 P-06 一致。

### 5.6 实际收敛但 scalar test 失败

令 \(T=cI\)，\(1/2<c<1\)，并取

\[
F=\frac{1-c}{\lambda c}I,\qquad
R=(2c-1)I,\qquad L=2c-1.
\]

实际 \(r_+=cr\)。精确 error-bound modulus 是
\(\rho=\lambda c/(1-c)\)，而 composed coefficient 为

\[
\kappa_1
=
\rho\frac{1+L}{2\lambda}
=
\frac{c^2}{1-c}.
\]

在 \(c=0.8\) 时它大于 1，尽管实际轨道线性收敛。
所以 \(\kappa_1<1\) 只能称 sufficient；原稿用语正确。

### 5.7 一步有限终止

取 \(F=N_{\{0\}}\)，即 \(F(0)=H\)、其余点空。则

\[
J_{\lambda F}=0,\qquad
R_{\lambda F}=-I,\qquad
L=1,\quad\gamma=1.
\]

任意初值一步到 0。normalized ratio 在终止后无定义；
原稿把 ratio 结论限定到 nonterminating orbit 是必要且正确的。

---

## 6. 给 integrator 的最小修复

### R1. 统一 \(L=0\)

把 definitions 的 power modulus、inverse rule 及相关 propositions
统一为 \(L\ge0\)，并加入：

> \(L=0\) 时 reflector 常值，\(\gamma\) 不可识别；power recurrence
> 为 \(r_+\le\rho(2\lambda)^{-q}r^q\)，phase 由 \(q\) 决定。

### R2. 冻结 order 术语

- \(O(r^p)\)：upper order；
- \(\Theta(r^p)\)：two-sided exact exponent；
- quotient \(\to c\in(0,\infty)\)：exact Q-order/factor。

GX-072 当前只直接证明第二层；GX-071 证明第三层。

### R3. 打印 endpoint A 的隐含闭性

在“No closedness”后写明

\[
B+A\Longrightarrow U\cap\overline S=U\cap S.
\]

### R4. 打印 E 的导入接口

若从 standard local GMSR 导出 E，必须另证
\(Tx\in U_{\rm EB}\) 与 residual cutoff；否则保留 current
output-relative E。

### 可选文字优化

把 scaling 末句写成

\[
c\Gamma\in{\rm RL}(\mu,L,\gamma)
\iff
\Gamma\in{\rm RL}(c\mu,L,\gamma).
\]

---

## 7. 最终审查表

| 项目 | 状态 | 结果 |
|---|---|---|
| RL--IP \(1/4\) | PASS | 精确 |
| Minty injectivity | PASS | 量词正确 |
| firm-type \(1/2\) | PASS | 精确 |
| \(\gamma=1\) tied 参数 | PASS | 精确 |
| Luke--Tam \(\tau_L\) | PASS | 精确 |
| inverse coefficient | PASS | \(L\lambda^{\gamma-1}\) |
| output scaling | PASS | step 为 \(\lambda/c\) |
| \(L=0\) convention | REPAIR | 两稿不一致 |
| one-step factor \(1/2\) | PASS | 可取等 |
| selected residual | PASS | 不误作 equality |
| gauge limsup | PASS | factorization 正确 |
| finite-length margin | PASS | 两个级数正确 |
| endpoint \(r=0\) | PASS/REPAIR | proof 对；需说明相对闭 |
| discontinuous \(T\) | PASS | 显式模型通过 |
| \(p=\gamma q,\ L>0\) | PASS | 三相正确 |
| \(\gamma=1\) 的 \(1+L\) | PASS | 不可删 1 |
| \(L=0\) power branch | REPAIR | 应补 \(q\)-phase |
| upper/exact 术语 | REPAIR | 需区分 factor |
| GX-071--074 | PASS | 四个逻辑边界均相容 |

---

## 8. SCI-Skills Expert Contract 1.0

~~~yaml
    contract_version: "1.0"
    expert_skill: "independent-max-mathematical-referee"
    project_id: "monotonicity-regularity-seesaw-2026-09"
    paper_family: "T"
    stage_id: "T2"
    task_id: "RL-FND-REF-CONST-06"
    task_status: "COMPLETE"
    inputs_reviewed:
      - "work/rl_foundations_definitions.md"
      - "work/rl_foundations_ppa_theorem.md"
      - "research/example_properties.md (GX-071--GX-074)"
      - "work/c_gx066_077.md (GX-071--GX-074 algebra only)"
    outputs:
      - "work/rl_foundations_referee_constants.md"
    evidence_status:
      - label: "VERIFIED_ALG"
        item: "All requested algebraic identities and convergence constants were independently rederived."
      - label: "EXECUTED_LOCAL"
        item: "Exact-rational tied-parameter tests, inverse scale tests, and a linear equality model passed."
      - label: "VERIFIED_LOCAL_MATERIAL"
        item: "GX-071--GX-074 were used only as algebraic pressure tests."
      - label: "NOT_PERFORMED"
        item: "No literature or novelty search was performed."
    assumptions:
      - "H is a real Hilbert space and lambda>0."
      - "B, A, and E have the exact universal quantifiers printed in the reviewed PPA file."
      - "The local GX report accurately defines its generated graphs."
    author_input_needed: []
    manual_actions: []
    quality_checks:
      - "Recomputed every coefficient requested by the task."
      - "Tested L=0, gamma=1, r=0, globally nonclosed S, discontinuous T, finite termination, and nontermination."
      - "Separated coverage, restricted uniqueness, and full-resolvent exclusion."
      - "Separated sufficient coefficients from necessary or sharp thresholds."
      - "Separated upper order, exact exponent, and exact Q-factor."
      - "Did not modify either reviewed source file."
    conflicts:
      - conflict_id: "RL-REF-C01"
        conflict_type: "parameter_boundary"
        claim: "The two foundations files use one convention for L."
        competing_values:
          - "Definitions: L>0."
          - "PPA theorem: L>=0."
        recommended_resolution: "Adopt L>=0 and print the constant-reflector/q-phase degeneration."
      - conflict_id: "RL-REF-C02"
        conflict_type: "rate_terminology"
        claim: "Two-sided normalized bounds equal an exact Q-factor."
        recommended_resolution: "Adopt the three-level terminology in R2."
      - conflict_id: "RL-REF-C03"
        conflict_type: "hidden_assumption_strength"
        claim: "Endpoint A has no local closure consequence."
        recommended_resolution: "State U intersect closure(S)=U intersect S."
      - conflict_id: "RL-REF-C04"
        conflict_type: "regularity_interface"
        claim: "A residual cutoff alone imports standard local GMSR into E."
        recommended_resolution: "Also verify output base-neighborhood membership."
    conflict_resolution_status: "UNRESOLVED_PENDING_INTEGRATOR"
    merge_permission: "orchestrator_only"
    stage_acceptance_recommendation: "PASS_AFTER_REPAIR"
    recommended_next_action: "Apply R1--R4, then run a fresh proof-only check on the repaired integrated draft."
~~~
