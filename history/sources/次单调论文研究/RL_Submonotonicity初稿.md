# 当前研究成果整理：RL-submonotonicity、Additive Firm Nonexpansiveness 与 PPA 收敛

> 说明：本文档只整理目前已经明确得到、可以继续作为研究底稿使用的定义、Lemma、定理与系数分析。暂定名称 **RL-submonotonicity** 与 **additive firm nonexpansiveness** 仅作为内部研究代号，后续仍需做 prior-art 审计后再决定正式命名。

---

## 0. 基本设定

设 \(H\) 为 Hilbert 空间，\(F:H\rightrightarrows H\)，\(\lambda>0\)，并记

\[
J_{\lambda F}:=(I+\lambda F)^{-1},\qquad
S:=F^{-1}(0)=\operatorname{Fix}J_{\lambda F}.
\]

新情形主要考虑

\[
0<\gamma<1,\qquad L>0.
\]

---

# 一、定义

## Definition 1：RL-\((\lambda,L,\gamma)\)-submonotonicity

暂用 **RL-submonotonicity** 这个名字。

称 \(F\) 满足 RL-\((\lambda,L,\gamma)\)-submonotonicity，如果对任意

\[
(u,u^*),(v,v^*)\in\operatorname{gph}F,
\]

令

\[
a:=u-v,\qquad b:=u^*-v^*,
\]

都有

\[
\boxed{
\|a-\lambda b\|
\le
L\|a+\lambda b\|^\gamma.
}
\tag{RL}
\]

等价的内积形式为

\[
\boxed{
\lambda\langle a,b\rangle
\ge
\frac14
\left(
\|a+\lambda b\|^2
-
L^2\|a+\lambda b\|^{2\gamma}
\right).
}
\tag{RL-IP}
\]

因为

\[
\|a-\lambda b\|^2
=
\|a+\lambda b\|^2-4\lambda\langle a,b\rangle.
\]

---

## Definition 2：\((L,\gamma)\)-additive firm nonexpansiveness

名字暂定。

称映射 \(J\) 满足 \((L,\gamma)\)-**additive firm nonexpansiveness**，如果

\[
\boxed{
\|Jx-Jy\|^2
+
\|(I-J)x-(I-J)y\|^2
\le
\frac12
\left(
\|x-y\|^2
+
L^2\|x-y\|^{2\gamma}
\right)
}
\tag{AFNE}
\]

对相应区域内所有 \(x,y\) 成立。

当 \(J\) 多值时，按 selection-wise 解释；若局部单值，则就是通常的映射性质。

---

## Definition 3：power metric subregularity

称 \(F\) 相对于

\[
S=F^{-1}(0)
\]

满足 \(q\)-阶 metric subregularity，如果局部存在 \(\rho>0\)，使

\[
\boxed{
d(u,S)
\le
\rho\,d(0,F(u))^q.
}
\tag{MSR-q}
\]

当前 PPA 收敛结果真正使用的是

\[
q\ge \frac1\gamma>1.
\]

---

## Definition 4：gauge subregularity

更一般地，给定递增 gauge

\[
\psi:\mathbb R_+\to\mathbb R_+,\qquad \psi(0)=0,
\]

如果局部有

\[
\boxed{
d(u,S)
\le
\psi\!\left(d(0,F(u))\right),
}
\tag{GMSR}
\]

则称 \(F\) 满足相应的 gauge subregularity。

幂函数情形就是

\[
\psi(t)=\rho t^q.
\]

---

# 二、基本 Lemma

## Lemma 1：RL-submonotonicity 与 resolvent 性质精确等价

令

\[
J:=J_{\lambda F}.
\]

取

\[
x=u+\lambda u^*,\qquad
y=v+\lambda v^*,
\]

其中

\[
(u,u^*),(v,v^*)\in\operatorname{gph}F.
\]

则

\[
u=Jx,\qquad v=Jy,
\]

并且

\[
a=u-v=Jx-Jy,
\]

\[
\lambda b
=
(I-J)x-(I-J)y,
\]

\[
x-y=a+\lambda b.
\]

由平行四边形恒等式，

\[
\|a\|^2+\|\lambda b\|^2
=
\frac12
\left(
\|a+\lambda b\|^2+\|a-\lambda b\|^2
\right).
\]

因此：

\[
\boxed{
F\text{ 满足 (RL)}
\iff
J_{\lambda F}\text{ 满足 (AFNE)}.
}
\tag{Equiv}
\]

也就是说，我们的两个新对象不是两个独立假设，而是**同一个数学结构在 graph side 和 resolvent side 的两个表示**。

---

# 三、PPA 的一步估计

令

\[
x^+=J_{\lambda F}(x),
\qquad
s:=x-x^+,
\qquad
r:=d(x,S).
\]

则

\[
\frac{s}{\lambda}\in F(x^+).
\]

---

## Lemma 2：基本能量估计

若 \(F\) 满足 (RL)，则

\[
\boxed{
d(x^+,S)^2+\|x-x^+\|^2
\le
\frac12
\left(
r^2+L^2r^{2\gamma}
\right).
}
\tag{E}
\]

证明只需在 (AFNE) 中把一个点取为任意 \(p\in S\)，注意

\[
Jp=p,
\]

然后对 \(p\in S\) 取下确界。

---

## Lemma 3：PPA step 的 Hölder 上界

在相同条件下，

\[
\boxed{
\|x-x^+\|
\le
\frac12
\left(
r+Lr^\gamma
\right).
}
\tag{Step}
\]

因此当 \(0<\gamma<1\) 时，

\[
\boxed{
\|x-x^+\|=O(r^\gamma).
}
\]

推导如下。取 \(p\in S\)，令

\[
a=x^+-p,\qquad s=x-x^+.
\]

由 (RL)，

\[
\|a-s\|\le L\|a+s\|^\gamma.
\]

而

\[
a+s=x-p.
\]

又因为

\[
2s=(a+s)-(a-s),
\]

故三角不等式给出

\[
2\|s\|
\le
\|a+s\|+\|a-s\|
\le
\|x-p\|+L\|x-p\|^\gamma.
\]

对 \(p\in S\) 取下确界，即得 (Step)。

---

## Lemma 4：residual 上界

因为

\[
\frac{x-x^+}{\lambda}\in F(x^+),
\]

所以

\[
d(0,F(x^+))
\le
\frac{\|x-x^+\|}{\lambda}.
\]

结合 Lemma 3：

\[
\boxed{
d(0,F(x^+))
\le
\frac{r+Lr^\gamma}{2\lambda}.
}
\tag{Res}
\]

---

# 四、核心一步递推

## Lemma 5：RL + \(q\)-subregularity 的距离递推

若同时满足

\[
d(u,S)\le\rho\,d(0,F(u))^q,
\]

则

\[
\boxed{
d(x^+,S)
\le
\frac{\rho}{(2\lambda)^q}
\left(
r+Lr^\gamma
\right)^q.
}
\tag{Rec}
\]

特别地，当 \(r\downarrow0\)，

\[
\boxed{
d(x^+,S)
=
O\!\left(r^{\gamma q}\right).
}
\tag{Order}
\]

这是目前 PPA 理论最核心的一步递推。

---

# 五、PPA 收敛定理

以下都理解为**局部定理**：RL 条件、subregularity 和所选 PPA branch 在一个较大邻域内有效，并从足够小的内部邻域开始；采用 two-radius localization 保证迭代不会跑出有效区域。

---

## Theorem 1：超临界情形

假设

\[
0<\gamma<1,
\]

\(F\) 满足局部 RL-\((\lambda,L,\gamma)\)-submonotonicity，并满足

\[
d(u,S)\le\rho\,d(0,F(u))^q.
\]

若

\[
\boxed{
\gamma q>1,
}
\tag{C1}
\]

则对充分接近 \(S\) 的初值，PPA

\[
x^{k+1}\in J_{\lambda F}(x^k)
\]

局部收敛到某个

\[
\bar x\in S.
\]

令

\[
r_k:=d(x^k,S),
\]

则

\[
\boxed{
r_{k+1}=O(r_k^{\gamma q}).
}
\]

因此距离到解集具有阶

\[
\boxed{\gamma q>1}
\]

的超线性递推。

同时

\[
\sum_k\|x^{k+1}-x^k\|<\infty,
\]

所以迭代点本身收敛，而不仅仅是

\[
d(x^k,S)\to0.
\]

---

## Theorem 2：临界情形

在相同假设下，如果

\[
\boxed{
\gamma q=1
}
\]

并且

\[
\boxed{
\rho
\left(
\frac{L}{2\lambda}
\right)^q
<1,
}
\tag{C2}
\]

则充分局部的 PPA 同样收敛到某个

\[
\bar x\in S.
\]

事实上，由

\[
\frac{r_{k+1}}{r_k}
\le
\frac{\rho}{(2\lambda)^q}
\left(
r_k^{1-\gamma}+L
\right)^q
\]

得到

\[
\boxed{
\limsup_{k\to\infty}
\frac{r_{k+1}}{r_k}
\le
\rho
\left(
\frac{L}{2\lambda}
\right)^q
<1.
}
\]

因此距离到解集至少局部线性收敛。

---

# 六、Gauge 版本

## Theorem 3：一般 regularity compensation

若

\[
d(u,S)
\le
\psi(d(0,F(u))),
\]

则 Lemma 4 直接给出

\[
\boxed{
d(x^+,S)
\le
\psi\!\left(
\frac{r+Lr^\gamma}{2\lambda}
\right).
}
\tag{GaugeRec}
\]

定义

\[
\Phi(r)
:=
\psi\!\left(
\frac{r+Lr^\gamma}{2\lambda}
\right).
\]

如果

\[
\boxed{
\limsup_{r\downarrow0}
\frac{\Phi(r)}{r}
<1,
}
\tag{GC}
\]

则充分局部的 PPA 收敛到 \(S\) 中某一点。

一个方便的充分条件是

\[
\boxed{
\limsup_{t\downarrow0}
\frac{\psi(t)}{t^{1/\gamma}}
<
\left(
\frac{2\lambda}{L}
\right)^{1/\gamma}.
}
\tag{GC'}
\]

幂函数

\[
\psi(t)=\rho t^q
\]

正好给出前面的两个定理。

---

# 七、当前成果的最短逻辑链

\[
\boxed{
\begin{array}{c}
\text{RL-submonotonicity of }F\\[1mm]
\Updownarrow\\[1mm]
\text{additive firm nonexpansiveness of }J_{\lambda F}\\[2mm]
\Downarrow\\[2mm]
\|x-x^+\|
\le
\dfrac12\big(d(x,S)+Ld(x,S)^\gamma\big)\\[3mm]
+\quad
d(u,S)\le\rho d(0,F(u))^q\\[2mm]
\Downarrow\\[2mm]
d(x^+,S)
\le
\dfrac{\rho}{(2\lambda)^q}
\big(d(x,S)+Ld(x,S)^\gamma\big)^q\\[3mm]
\Downarrow\\[2mm]
\gamma q>1
\quad\text{或}\quad
\gamma q=1,\
\rho(L/2\lambda)^q<1\\[2mm]
\Downarrow\\[2mm]
\boxed{\text{local PPA convergence}.}
\end{array}}
\]

---

# 八、系数分析：与 Luke–Tam 的三角不等式处理之区别

下面保留上一条回答原文，不作改写。

对，**看起来奇怪，但其实两边三角不等式扮演的角色完全不同**。所以 Luke 那里三角不等式会损失，而我们这里目前三角不等式反而给了更好的界。

Luke–Tam 那边，设

\[
r=d(x,S),\qquad r_+=d(x^+,S),\qquad s=\|x-x^+\|.
\]

他们有一个本来就很有信息量的平方耦合：

\[
r_+^2+s^2\le (1+2\tau)r^2,
\]

以及 subregularity

\[
r_+\le \frac{\rho}{\lambda}s.
\]

这两个可以**直接联立**：

\[
s^2\ge \frac{\lambda^2}{\rho^2}r_+^2,
\]

所以

\[
\left(1+\frac{\lambda^2}{\rho^2}\right)r_+^2
\le (1+2\tau)r^2.
\]

这就得到我们之前改进的系数。Luke 如果绕道三角不等式

\[
r\le s+r_+,
\]

就把原来那个很好的“平方正交型信息”压成了线性信息，所以会变差。

---

但我们这里恰好相反。

令

\[
a=x^+-p,\qquad s=x-x^+,\qquad z=x-p=a+s,
\]

我们的基本条件直接给

\[
\|a-s\|\le Lr^\gamma.
\]

于是有**精确恒等式**

\[
2s=z-(a-s),
\]

因此三角不等式直接给

\[
\boxed{
\|s\|
\le \frac12(r+Lr^\gamma).
}
\]

这已经非常贴近原始 RL 条件。

如果反而把它平方，变成 AFNE：

\[
\|a\|^2+\|s\|^2
\le
\frac12(r^2+L^2r^{2\gamma}),
\]

再丢掉 \(\|a\|^2\)，只能得到

\[
\|s\|
\le
\frac1{\sqrt2}\sqrt{r^2+L^2r^{2\gamma}}.
\]

局部 \(r\to0\) 时，两者分别是

\[
\boxed{\frac L2 r^\gamma}
\qquad\text{和}\qquad
\boxed{\frac L{\sqrt2}r^\gamma}.
\]

显然

\[
\frac12<\frac1{\sqrt2}.
\]

所以我们这里**平方化反而损失了信息，直接对原始 RL 条件用三角不等式更强**。

---

因此两者的区别可以非常干净地记成：

\[
\boxed{
\begin{array}{ll}
\text{Luke--Tam:}&
\text{三角不等式破坏了已有的平方耦合，所以不是最优；}\\[1mm]
\text{我们:}&
\text{三角不等式直接作用于原始 Hölder 图关系，平方化反而更松。}
\end{array}}
\]

还有一个很值得后面研究的点：**我们目前并没有证明**
\[
\frac12(r+Lr^\gamma)
\]
在“RL + \(q\)-subregularity”全部信息下就是最终最优常数。

尤其孤立零点时，subregularity 会进一步约束 \(a\)，确实可能继续改进；但在**非孤立零点集**里，\(a\) 可以有很大的切向分量而 \(d(x^+,S)\) 很小，所以这个三角界很可能真的接近 sharp。

这恰好也是为什么非孤立情形值得 Codex 去专门做 **sharp constant / extremal example**。

---

# 九、当前研究对象的数学本质

当前研究的核心不是 reflected resolvent 本身，而是下面这一套结构：

\[
\boxed{
F\text{ 的新 generalized monotonicity}
\iff
J_{\lambda F}\text{ 的新 additive/Hölder firm-type nonexpansiveness}
}
\]

再配合

\[
\boxed{
\text{higher-order / gauge subregularity}
}
\]

得到

\[
\boxed{
\text{PPA local convergence}.
}
\]

其中真正已经证明的收敛区域为

\[
\boxed{
\gamma q>1
}
\]

以及临界情形

\[
\boxed{
\gamma q=1,\qquad
\rho\left(\frac{L}{2\lambda}\right)^q<1.
}
\]
