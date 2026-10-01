# RL Project Handoff

> Current mathematical state only.  
> This file contains **definitions, the current main theorem, its proof, established boundaries, and directly relevant supporting results**.  
> It contains **no research goal, no future-work instructions, and no exploratory research agenda**.

---

# A. Definitions and notation

Work in finite-dimensional Euclidean space.

Let

$$
F:\mathbb R^n\rightrightarrows\mathbb R^n,
\qquad
D\subset\mathbb R^n,
\qquad
\lambda>0.
$$

Define

$$
S:=F^{-1}(0)\cap D,
$$

and assume throughout that

$$
S\neq\varnothing
$$

and that \(S\) is closed.

The resolvent is

$$
J_{\lambda F}:=(I+\lambda F)^{-1}.
$$

Thus

$$
x^+\in J_{\lambda F}(x)
$$

is equivalent to

$$
\frac{x-x^+}{\lambda}\in F(x^+).
\tag{A.1}
$$

Because \(S\) is closed in finite-dimensional Euclidean space, for every \(x\) there exists

$$
p\in P_S(x)
$$

such that

$$
\|x-p\|=d(x,S).
$$

---

## A.1 RL

For two graph points

$$
(u,u^*),(v,v^*)\in\operatorname{gph}F,
$$

write

$$
a:=u-v,
\qquad
b:=u^*-v^*.
$$

The RL condition is

$$
\boxed{
\|a-\lambda b\|
\le
L\|a+\lambda b\|^\gamma,
\qquad
L\ge0,
\quad
0<\gamma\le1.
}
\tag{RL}
$$

---

## A.2 RL-IP

Squaring (RL) gives the equivalent inner-product form

$$
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
$$

RL-IP is an equivalent representation of RL, not a separate definition.

---

## A.3 \(J_{\lambda F}\)-side equivalent form

Let

$$
x^+\in J_{\lambda F}(x),
\qquad
y^+\in J_{\lambda F}(y).
$$

Then RL is equivalent, on the corresponding graph pairs, to

$$
\boxed{
\|x^+-y^+\|^2
+
\|(x-x^+)-(y-y^+)\|^2
\le
\frac12
\left(
\|x-y\|^2
+
L^2\|x-y\|^{2\gamma}
\right).
}
\tag{J-RL}
$$

If \(p\in S\), then \(p\in J_{\lambda F}(p)\). Hence taking

$$
y=y^+=p
$$

gives

$$
\boxed{
\|x^+-p\|^2
+
\|x-x^+\|^2
\le
\frac12
\left(
\|x-p\|^2
+
L^2\|x-p\|^{2\gamma}
\right).
}
\tag{A.2}
$$

When

$$
p\in P_S(x),
$$

define

$$
d:=d(x,S),
\qquad
s:=\|x-x^+\|,
\qquad
d_+:=d(x^+,S).
$$

Since

$$
d_+\le \|x^+-p\|,
$$

(A.2) implies

$$
\boxed{
d_+^2+s^2
\le
\frac12
\left(
d^2+L^2d^{2\gamma}
\right).
}
\tag{E}
$$

---

## A.4 General residual regularity

Let

$$
\psi:[0,\infty)\to[0,\infty)
$$

be nondecreasing, with

$$
\psi(0)=0,
\qquad
\psi(t)\to0
\quad\text{as }t\downarrow0.
$$

The local regularity condition is

$$
\boxed{
d(y,S)
\le
\psi\bigl(d(0,F(y))\bigr).
}
\tag{Reg}
$$

For a proximal step, (A.1) gives

$$
d(0,F(x^+))
\le
\frac{\|x-x^+\|}{\lambda}
=
\frac{s}{\lambda}.
$$

Therefore

$$
\boxed{
d_+
\le
\psi(s/\lambda).
}
\tag{R}
$$

---

# B. Current main theorem

## Theorem — Local PPA convergence from \(J\)-RL geometry and general gauge regularity

Fix

$$
\bar x\in S.
$$

Assume there are neighborhoods \(U',U\) of \(\bar x\) and a set \(D\subset\mathbb R^n\) such that:

### (i) Closed nonempty local solution set

$$
S=F^{-1}(0)\cap D
$$

is nonempty and closed.

### (ii) Resolvent stays in \(D\)

$$
J_{\lambda F}:D\rightrightarrows D.
$$

### (iii) Local one-step existence

For every

$$
x\in U'\cap D,
$$

there exists at least one

$$
x^+\in J_{\lambda F}(x)\cap U.
$$

### (iv) Local \(J\)-side RL estimate

For every relevant

$$
x\in U'\cap D,
\qquad
x^+\in J_{\lambda F}(x)\cap U,
$$

and every

$$
p\in P_S(x),
$$

the estimate

$$
\boxed{
\|x^+-p\|^2
+
\|x-x^+\|^2
\le
\frac12
\left(
d(x,S)^2
+
L^2d(x,S)^{2\gamma}
\right)
}
\tag{B.1}
$$

holds for fixed

$$
L\ge0,
\qquad
0<\gamma\le1.
$$

### (v) Local general-gauge regularity

For every relevant

$$
y\in U\cap D,
$$

$$
\boxed{
d(y,S)
\le
\psi\bigl(d(0,F(y))\bigr),
}
\tag{B.2}
$$

where \(\psi\) is nondecreasing, \(\psi(0)=0\), and \(\psi(t)\to0\) as \(t\downarrow0\).

### (vi) Scalar compatibility

There exist

$$
\kappa\in(0,1)
$$

and

$$
\delta_0>0
$$

such that for every

$$
0<d<\delta_0
$$

and every pair of nonnegative numbers \(s,d_+\) satisfying

$$
d_+^2+s^2
\le
\frac12(d^2+L^2d^{2\gamma})
\tag{B.3}
$$

and

$$
d_+
\le
\psi(s/\lambda),
\tag{B.4}
$$

one necessarily has

$$
\boxed{
d_+\le\kappa d.
}
\tag{B.5}
$$

Then there exists

$$
\varepsilon>0
$$

such that for every

$$
x^0\in B_\varepsilon(\bar x)\cap D,
$$

one can choose recursively

$$
x^{k+1}\in J_{\lambda F}(x^k)\cap U
$$

for all \(k\ge0\), and the resulting local orbit satisfies

$$
\boxed{
d(x^{k+1},S)
\le
\kappa\,d(x^k,S).
}
\tag{B.6}
$$

Hence

$$
d(x^k,S)
\le
\kappa^k d(x^0,S).
\tag{B.7}
$$

Moreover,

$$
\boxed{
\sum_{k=0}^\infty
\|x^{k+1}-x^k\|
<\infty.
}
\tag{B.8}
$$

Therefore \((x^k)\) is Cauchy, so

$$
x^k\to x^\infty
$$

for some

$$
x^\infty\in S.
$$

---

# C. Proof of the main theorem

The proof has two different roles:

$$
\boxed{
\text{energy + regularity}
\Longrightarrow
\text{distance contraction}
}
$$

and

$$
\boxed{
\text{RL step estimate}
\Longrightarrow
\text{finite length and local orbit closure}.
}
$$

---

## C.1 One-step contraction

Take

$$
x\in U'\cap D
$$

and choose

$$
x^+\in J_{\lambda F}(x)\cap U.
$$

Let

$$
p\in P_S(x),
$$

and define

$$
d:=d(x,S),
\qquad
s:=\|x-x^+\|,
\qquad
d_+:=d(x^+,S).
$$

From (B.1),

$$
d_+^2+s^2
\le
\frac12(d^2+L^2d^{2\gamma}).
\tag{C.1}
$$

Because

$$
\frac{x-x^+}{\lambda}\in F(x^+),
$$

we have

$$
d(0,F(x^+))
\le
\frac{s}{\lambda}.
$$

Using (B.2) and monotonicity of \(\psi\),

$$
d_+
\le
\psi(s/\lambda).
\tag{C.2}
$$

Thus \(d,s,d_+\) satisfy the scalar compatibility conditions, so whenever

$$
0<d<\delta_0,
$$

$$
\boxed{
d_+\le\kappa d.
}
\tag{C.3}
$$

---

## C.2 Step upper bound

Since

$$
x^+-p
=
(x-p)-(x-x^+),
$$

we have

$$
\|x^+-p\|^2
=
d^2+s^2
-
2\langle x-p,x-x^+\rangle.
$$

By Cauchy–Schwarz,

$$
\langle x-p,x-x^+\rangle
\le
ds.
$$

Therefore

$$
\boxed{
\|x^+-p\|^2
\ge
(d-s)^2.
}
\tag{C.4}
$$

Substituting into (B.1),

$$
(d-s)^2+s^2
\le
\frac12(d^2+L^2d^{2\gamma}).
$$

Rearranging,

$$
(2s-d)^2
\le
L^2d^{2\gamma}.
$$

Hence

$$
\boxed{
s
\le
\frac12(d+Ld^\gamma).
}
\tag{C.5}
$$

---

## C.3 Geometric decay

Let

$$
d_k:=d(x^k,S),
\qquad
s_k:=\|x^{k+1}-x^k\|.
$$

As long as the iterates remain in the certified local region,

$$
d_{k+1}\le\kappa d_k,
$$

so

$$
\boxed{
d_k\le\kappa^k d_0.
}
\tag{C.6}
$$

---

## C.4 Summability of the steps

Using (C.5) and (C.6),

$$
s_k
\le
\frac12
\left(
\kappa^k d_0
+
L\kappa^{\gamma k}d_0^\gamma
\right).
$$

Therefore

$$
\sum_{k=0}^\infty s_k
\le
\frac12
\left[
\frac{d_0}{1-\kappa}
+
\frac{Ld_0^\gamma}{1-\kappa^\gamma}
\right].
\tag{C.7}
$$

---

## C.5 Local one-step existence gives the whole orbit

Choose \(R>0\) such that

$$
B_R(\bar x)
\subset
U\cap U'.
$$

Choose \(\varepsilon>0\) small enough that

$$
\varepsilon<\delta_0
$$

and

$$
\boxed{
\varepsilon
+
\frac12
\left[
\frac{\varepsilon}{1-\kappa}
+
\frac{L\varepsilon^\gamma}{1-\kappa^\gamma}
\right]
<
R.
}
\tag{C.8}
$$

Take

$$
x^0\in B_\varepsilon(\bar x)\cap D.
$$

Since \(\bar x\in S\),

$$
d_0
\le
\|x^0-\bar x\|
<
\varepsilon.
$$

The local one-step existence assumption gives \(x^1\).

Inductively, if \(x^0,\ldots,x^k\) have been chosen, then

$$
\|x^k-\bar x\|
\le
\|x^0-\bar x\|
+
\sum_{j=0}^{k-1}s_j.
$$

Using (C.7),

$$
\|x^k-\bar x\|
<
\varepsilon
+
\frac12
\left[
\frac{\varepsilon}{1-\kappa}
+
\frac{L\varepsilon^\gamma}{1-\kappa^\gamma}
\right]
<
R.
$$

Thus

$$
x^k\in U'\cap D,
$$

so local one-step existence can be used again.

Hence the entire local orbit can be constructed.

---

## C.6 Cauchy convergence and limit in \(S\)

For \(m>n\),

$$
\|x^m-x^n\|
\le
\sum_{k=n}^{m-1}s_k.
$$

Because

$$
\sum_{k=0}^\infty s_k<\infty,
$$

the sequence is Cauchy.

Hence in \(\mathbb R^n\),

$$
x^k\to x^\infty.
$$

Also,

$$
d(x^k,S)
\le
\kappa^k d_0
\to0.
$$

Since \(S\) is closed,

$$
\boxed{
x^\infty\in S.
}
$$

---

# D. Already-established boundaries and facts

---

## D.1 Isolated local solution + established contraction

Suppose \(p\in S\) is locally isolated, so for some neighborhood \(V\),

$$
S\cap V=\{p\}.
$$

Assume \(x,x^+\in V\) and the main theorem gives

$$
d(x^+,S)
\le
\kappa d(x,S).
$$

Then

$$
d(x,S)=\|x-p\|,
\qquad
d(x^+,S)=\|x^+-p\|,
$$

hence

$$
\|x^+-p\|
\le
\kappa\|x-p\|.
\tag{D.1}
$$

Also,

$$
\|x-x^+\|
\le
(1+\kappa)\|x-p\|.
$$

Therefore

$$
\boxed{
\|x^+-p\|^2
+
\|x-x^+\|^2
\le
\frac12
\left(
1+(2\kappa+1)^2
\right)
\|x-p\|^2.
}
\tag{D.2}
$$

Thus, for the \(J\)-side comparison with this isolated solution \(p\), exponent

$$
\gamma=1
$$

is available.

This does **not** imply that the full all-pairs RL condition for \(F\) has exponent \(1\).

---

## D.2 Nonisolated solution sets allow motion along \(S\)

When \(S\) is nonisolated,

$$
d(x^+,S)\ll d(x,S)
$$

does not imply that \(x^+\) is close to the same solution point \(p\in P_S(x)\).

The output may move substantially along \(S\) while becoming much closer to \(S\).

This geometric freedom has already been identified.

---

## D.3 Full all-pairs RL and solution comparison are different

Full all-pairs RL controls arbitrary pairs of graph points.

The PPA proof above only uses the \(J\)-side estimate obtained by comparing the current step with a solution point.

These are different requirements.

There are multivalued examples in which full all-pairs RL fails because two different graph values have the same Minty input, while the solution comparison needed by the PPA proof remains valid.

---

## D.4 For multivalued \(F\), the selected value and \(d(0,F(y))\) are different

From a proximal step,

$$
\frac{x-y}{\lambda}\in F(y).
$$

This gives only

$$
d(0,F(y))
\le
\left\|
\frac{x-y}{\lambda}
\right\|.
$$

Equality need not hold.

Therefore a regularity argument involving

$$
d(0,F(y))
$$

must concern the full value set \(F(y)\), not only the value selected by one proximal step.

---

## D.5 One-step existence does not imply existence of the whole orbit

The assumption

$$
x\in U'\cap D
\Longrightarrow
J_{\lambda F}(x)\cap U\neq\varnothing
$$

only gives one step.

The whole local orbit exists because the finite-length estimate keeps all iterates inside the region where the one-step existence assumption can be reused.

---

## D.6 Set-distance convergence does not by itself imply point convergence

The statement

$$
d(x^k,S)\to0
$$

does not, by itself, imply that \(x^k\) converges to a particular point when \(S\) is nonisolated.

The main theorem obtains point convergence through

$$
\sum_k\|x^{k+1}-x^k\|<\infty.
$$

---

## D.7 The coarse step-bound route can lose contraction information

The step upper bound

$$
s\le\frac12(d+Ld^\gamma)
$$

is useful for finite length.

However, using only

$$
d_+\le\psi(s/\lambda)
$$

and substituting the step upper bound can produce a strictly more restrictive contraction condition.

The sharper route keeps

$$
d_+^2+s^2
\le
\frac12(d^2+L^2d^{2\gamma})
$$

and

$$
d_+\le\psi(s/\lambda)
$$

coupled.

---

# E. Directly relevant supporting results and examples

---

## E.1 Sharpened linear calibration

Take

$$
\gamma=1,
\qquad
L^2=1+4\tau,
$$

and

$$
\psi(t)=\rho t.
$$

Then

$$
d_+^2+s^2
\le
(1+2\tau)d^2
$$

and

$$
d_+
\le
\frac{\rho}{\lambda}s.
$$

Hence

$$
\boxed{
d_+
\le
\frac{\sqrt{1+2\tau}\,\rho}
{\sqrt{\rho^2+\lambda^2}}
\,d.
}
\tag{E.1}
$$

A sufficient contraction condition is

$$
\boxed{
2\tau\rho^2<\lambda^2.
}
\tag{E.2}
$$

---

## E.2 Step estimate used for finite length

For every relevant step,

$$
\boxed{
\|x-x^+\|
\le
\frac12
\left(
d(x,S)
+
L\,d(x,S)^\gamma
\right).
}
\tag{E.3}
$$

---

## E.3 Multibranch separating example

Let

$$
F(y)=\{-y,y\},
\qquad
\lambda>2.
$$

Then

$$
S=\{0\},
$$

and

$$
J_{\lambda F}(x)
=
\left\{
\frac{x}{1+\lambda},
\frac{x}{1-\lambda}
\right\}.
$$

Full all-pairs RL fails because different graph branches can create a Minty collision.

Nevertheless, relative to the solution \(0\), both resolvent outputs satisfy the same linear estimate with

$$
L=\frac{\lambda+1}{\lambda-1}.
$$

Also,

$$
d(y,S)=d(0,F(y))=|y|.
$$

Every branch choice satisfies

$$
|x^{k+1}|
\le
\frac1{\lambda-1}|x^k|.
$$

Thus arbitrary history-dependent branch switching still converges.

---

## E.4 A genuinely non-power regularity gauge

Define near \(0\)

$$
F(0)=0,
$$

and for \(x\neq0\),

$$
F(x)
=
\frac{\operatorname{sgn}(x)}
{\log(e+1/|x|)}.
$$

Then

$$
S=\{0\}.
$$

For small \(x\),

$$
d(0,F(x))
=
\frac1{\log(e+1/|x|)}.
$$

Solving for \(|x|\) gives

$$
\boxed{
\psi(t)
=
\frac1{e^{1/t}-e}.
}
\tag{E.4}
$$

Thus locally,

$$
d(x,S)
=
\psi(d(0,F(x))).
$$

---

## E.5 A direct \(\gamma=1\) verification rule from hypomonotonicity

Suppose that on the relevant graph pairs,

$$
\langle a,b\rangle
\ge
-h\|a\|^2,
\qquad
h\ge0,
$$

and

$$
\lambda h<1.
$$

Then RL with \(\gamma=1\) holds with

$$
\boxed{
L=
\frac{1+\lambda h}{1-\lambda h}.
}
\tag{E.5}
$$

This gives a direct \(F\)-side certificate without first computing the resolvent explicitly.

---

# End of handoff

This file intentionally contains no research goal and no future-work agenda.
