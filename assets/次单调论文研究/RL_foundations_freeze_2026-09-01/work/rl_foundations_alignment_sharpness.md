# RL foundations: nonisolated solution alignment, drift, and exponent sharpness

> Task: RL-FND-SHARP-04. Internal mathematical foundation and proof audit.
> This file makes no literature-novelty claim and does not modify the proposed
> main foundation file.

## 0. Conclusions that can be frozen

1. A non-circular alignment quantity is obtained from nearest-solution
   anchor transport, not by defining it as a root of the desired output
   rate. For a localized resolvent branch \(J\), the canonical pointwise
   quantities are

   \[
   a_J(x):=d\bigl(x,P_S(Jx)\bigr),
   \qquad
   \delta_J(x):=d\bigl(P_S(x),P_S(Jx)\bigr),
   \]

   where the distance between two sets is their infimal distance. Their
   local envelopes are equivalent up to universal constants after adding
   the normal input distance \(d(x,S)\).

2. If the output-side error bound has gauge \(\psi=o(\mathrm{id})\), then

   \[
   d(Jx,S)
   \le
   \psi\!\left(\frac{2}{\lambda}a_J(x)\right).
   \]

   Consequently, \(a_J(x)=O(d(x,S)^\theta)\) and the power error bound
   \(\psi(t)=\rho t^q\) give

   \[
   d(Jx,S)=O\bigl(d(x,S)^{\theta q}\bigr).
   \]

3. Exact output projections are convenient but not necessary. An
   \(\varepsilon\)-nearest output anchor is enough when its additive
   tolerance is \(o(\|w\|)\), where \(w=(x-Jx)/\lambda\). To retain the
   stronger \(q\)-order reflected expansion around that same approximate
   anchor, the stronger tolerance \(O(\|w\|^q)\) is needed.

4. The product \(\theta q\) is sharp only under joint saturation of the
   alignment scale, residual scale, and error-bound scale. Sharpness of
   \(\theta\) and \(q\) on unrelated sequences does not imply sharpness of
   their product.

5. GX-071 jointly saturates all three scales and has exact normalized limit
   \(1\); it is a valid minimax sharpness witness. GX-072 has alignment
   exponent \(1\), despite all-pairs exponent \(\gamma<1\), and its orbit
   has uniform two-sided order \(q>\gamma q\). GX-073 has only linear
   fixed-target regularity and no invariant small neighborhood, so its
   one-step exponent is not a convergence order.

6. A reviewer-facing limitation must remain visible. Under a superlinear
   error bound,

   \[
   a_J(x)=\lambda\|w(x)\|(1+o(1)).
   \]

   Analytically, the alignment composition inequality is therefore a
   geometric reformulation of the residual-step estimate. The structural
   content is the split into normal distance and nearest-solution drift; the
   bare composition inequality should not be advertised as a deep theorem
   by itself.

---

## 1. Localized setting and non-circular profiles

Let \(H\) be a Hilbert space, \(F:H\rightrightarrows H\),

\[
S:=F^{-1}(0)\ne\varnothing,
\qquad
\lambda>0.
\]

Let \(\Gamma\subset\operatorname{gph}F\) be a named graph localization and
let \(D\subset H\) be a Minty-input domain on which \(\Gamma\) defines a
single-valued branch \(J:D\to H\). Thus, for every \(x\in D\),

\[
y:=Jx,
\qquad
w:=\frac{x-y}{\lambda},
\qquad
(y,w)\in\Gamma.
\tag{1.1}
\]

Nothing below asserts range coverage, branch existence outside \(D\), or
equality of \(J\) with every value of the full resolvent.

For \(\varepsilon\ge0\), define

\[
P_S^\varepsilon(z)
:=
\{p\in S:\ \|z-p\|\le d(z,S)+\varepsilon\}.
\tag{1.2}
\]

When \(P_S(z)\ne\varnothing\), write \(P_S(z)=P_S^0(z)\). Exact
projections exist, for example, when \(S\) is closed and convex, or locally
in finite dimensions when \(S\) is closed. They need not exist for an
arbitrary closed nonconvex subset of an infinite-dimensional Hilbert space.

### Definition 1.1 (pointwise output alignment)

Assume \(P_S(Jx)\ne\varnothing\). Define

\[
a_J(x):=d\bigl(x,P_S(Jx)\bigr).
\tag{1.3}
\]

This asks how far the input is from a solution anchor nearest to the output.
It contains neither \(d(Jx,S)^{1/q}\), a desired rate exponent, nor an
error-bound modulus.

### Definition 1.2 (nearest-anchor drift)

Assume both projection sets are nonempty and define

\[
\delta_J(x)
:=
d\bigl(P_S(x),P_S(Jx)\bigr)
=
\inf_{\substack{p_x\in P_S(x)\\p_y\in P_S(Jx)}}
\|p_x-p_y\|.
\tag{1.4}
\]

This is the smallest motion along \(S\) needed to pass from an
input-nearest anchor to an output-nearest anchor. It vanishes automatically
at an isolated solution and equals \(|z|^\gamma\) in GX-071.

Fix a local input region \(U\subset D\). For \(r>0\), define

\[
\begin{aligned}
\mathcal A_J(r)
&:=
\sup\{a_J(x):x\in U,\ 0<d(x,S)\le r\},\\
\Delta_J(r)
&:=
\sup\{\delta_J(x):x\in U,\ 0<d(x,S)\le r\},\\
\chi_J(r)
&:=
\sup\{d(x,S)+\delta_J(x):
       x\in U,\ 0<d(x,S)\le r\}.
\end{aligned}
\tag{1.5}
\]

In particular, \(\chi_J(r)\le r+\Delta_J(r)\). The cumulative supremum in
the definition of \(\chi_J\), rather than the possibly unattained radius
\(r\), is needed for the exact comparison below.

Empty suprema are \(0\). A uniform \(\theta\)-alignment profile means

\[
\mathcal A_J(r)\le K r^\theta
\qquad(0<r\le r_0),
\tag{1.6}
\]

or, equivalently by Lemma 1.3, \(\chi_J(r)=O(r^\theta)\). Define

\[
\theta_*:=
\sup\{\theta>0:\ \mathcal A_J(r)=O(r^\theta)\}.
\tag{1.7}
\]

If \(U\) contains non-solution inputs arbitrarily close to \(S\), then
\(\theta_*\le1\), since \(a_J(x)\ge d(x,S)\).

### Lemma 1.3 (alignment and drift are equivalent profiles)

For \(r_x:=d(x,S)\),

\[
r_x\le a_J(x)\le r_x+\delta_J(x)\le3a_J(x).
\tag{1.8}
\]

Consequently,

\[
\mathcal A_J(r)\le\chi_J(r)\le3\mathcal A_J(r),
\tag{1.9}
\]

and the two envelopes have the same maximal power exponent.

#### Proof

Every point of \(P_S(Jx)\) lies in \(S\), so \(a_J(x)\ge r_x\). Choose
\(p_x\in P_S(x)\) and \(p_y\in P_S(Jx)\) within an arbitrary
\(\eta>0\) of attaining (1.4). Then

\[
a_J(x)\le\|x-p_y\|
\le r_x+\delta_J(x)+\eta.
\]

Let \(\eta\downarrow0\). Conversely, choose \(p_y\in P_S(Jx)\) within
\(\eta\) of attaining (1.3) and any \(p_x\in P_S(x)\). Then

\[
\delta_J(x)\le\|p_x-p_y\|
\le r_x+a_J(x)+\eta.
\]

Hence

\[
r_x+\delta_J(x)
\le2r_x+a_J(x)
\le3a_J(x).
\]

Taking suprema proves (1.9). \(\square\)

### Lemma 1.4 (under a superlinear error bound, alignment is step scale)

Suppose a nondecreasing gauge \(\psi\) satisfies

\[
d(y,S)\le\psi(d(0,F(y))),
\qquad
\frac{\psi(t)}t\to0,
\tag{1.10}
\]

and the attained branch residuals tend to zero. Then

\[
\bigl|a_J(x)-\lambda\|w\|\bigr|
\le d(y,S)
\le\psi(\|w\|),
\tag{1.11}
\]

and along every nontrivial local sequence,

\[
\frac{a_J(x)}{\lambda\|w\|}\to1.
\tag{1.12}
\]

#### Proof

For every \(p\in P_S(y)\),

\[
\bigl|\|x-p\|-\|x-y\|\bigr|
\le\|y-p\|=d(y,S).
\]

Take the infimum over \(p\), use
\(\|x-y\|=\lambda\|w\|\), and use
\(d(0,F(y))\le\|w\|\). \(\square\)

Lemma 1.4 is both useful and limiting. The profile is independently
defined, but after imposing superlinear subregularity it is asymptotically
equivalent to the step-length profile. Definition 1.2 is what keeps the
isolated/nonisolated geometry visible.

---

## 2. Alignment--error-bound composition

### Theorem 2.1 (exact-projection gauge composition)

Assume the setting of Section 1, exact projection existence for the points
under consideration, and (1.10). Shrink the residual localization so that

\[
\psi(t)\le\frac{\lambda}{2}t
\tag{2.1}
\]

for every attained \(t=\|w(x)\|\). Then

\[
\boxed{
d(Jx,S)
\le
\psi\!\left(\frac{2}{\lambda}a_J(x)\right)
\le
\psi\!\left(\frac{2}{\lambda}
  [d(x,S)+\delta_J(x)]\right).}
\tag{2.2}
\]

If

\[
\Omega_J(r)
:=
\sup\{d(Jx,S):x\in U,\ 0<d(x,S)\le r\},
\tag{2.3}
\]

then

\[
\boxed{
\Omega_J(r)
\le
\psi\!\left(\frac{2}{\lambda}\mathcal A_J(r)\right)
\le
\psi\!\left(\frac{2}{\lambda}\chi_J(r)\right).}
\tag{2.4}
\]

#### Proof

Put \(t=\|w\|\) and \(a=a_J(x)\). Lemma 1.4 and (2.1) give

\[
a\ge\lambda t-d(Jx,S)
\ge\lambda t-\psi(t)
\ge\frac{\lambda}{2}t.
\]

Thus \(t\le2a/\lambda\). Monotonicity of \(\psi\) and the error bound
give

\[
d(Jx,S)\le\psi(t)
\le\psi\!\left(\frac{2a}{\lambda}\right).
\]

Lemma 1.3 and then taking suprema prove the remaining claims. \(\square\)

### Corollary 2.2 (power law and the \(\theta q\) upper exponent)

Let \(q>1\), \(\rho>0\), and suppose

\[
d(y,S)\le\rho\,d(0,F(y))^q.
\tag{2.5}
\]

If

\[
\mathcal A_J(r)\le K r^\theta,
\qquad
0<\theta\le1,
\tag{2.6}
\]

then, after shrinking the residual localization if necessary,

\[
\boxed{
d(Jx,S)
\le
\rho\left(\frac{2K}{\lambda}\right)^q
d(x,S)^{\theta q}.}
\tag{2.7}
\]

The same conclusion holds when \(\chi_J(r)\le K r^\theta\). Equation
(2.7) is an upper guarantee, not an exact-order statement without the
joint lower bounds in Proposition 4.1.

### Proposition 2.3 (all-pairs RL is one verifier, not the definition)

Let \(R=2J-I\). Suppose that for every relevant \(x\), an input-nearest
solution \(p_x\in P_S(x)\) belongs to the named zero branch, so that
\(Jp_x=Rp_x=p_x\), and suppose

\[
\|Rx-Rp_x\|\le L\|x-p_x\|^\gamma,
\qquad
0<\gamma\le1.
\tag{2.8}
\]

Then

\[
2\lambda\|w\|
=\|x-Rx\|
\le d(x,S)+L d(x,S)^\gamma.
\tag{2.9}
\]

Under the superlinear error bound,

\[
a_J(x)=O\bigl(d(x,S)+d(x,S)^\gamma\bigr),
\tag{2.10}
\]

so \(\theta=\gamma\) is an admissible, possibly nonoptimal, alignment
exponent. Directly combining (2.9) with the error bound recovers

\[
d(Jx,S)
\le
\psi\!\left(
\frac{d(x,S)+L d(x,S)^\gamma}{2\lambda}
\right).
\tag{2.11}
\]

GX-072 proves that (2.10) may be strictly pessimistic: its all-pairs
maximal exponent is \(\gamma<1\), while its alignment exponent is \(1\).

#### Proof

Use \(x-Rx=2(x-Jx)=2\lambda w\) and the triangle inequality through
\(p_x\). Lemma 1.4 gives (2.10), and monotonicity of \(\psi\) gives
(2.11). \(\square\)

---

## 3. Exact versus approximate output anchors

Exact output-nearest anchors are not necessary. What is necessary is a
quantitatively controlled connection to the output's nearest-solution
geometry.

Let \(e:[0,t_0]\to[0,\infty)\) be a declared tolerance gauge and define

\[
a_{J,e}(x)
:=
d\bigl(x,P_S^{e(\|w\|)}(Jx)\bigr).
\tag{3.1}
\]

For \(w\ne0\), the approximate projection set is nonempty whenever
\(e(\|w\|)>0\), even if \(S\) is not proximinal.

### Theorem 3.1 (approximate-output-anchor composition)

Suppose (1.10) holds and, for some fixed \(0\le\kappa<1\),

\[
\psi(t)+e(t)\le\kappa\lambda t
\tag{3.2}
\]

for all sufficiently small attained \(t=\|w\|>0\). Then

\[
\boxed{
d(Jx,S)
\le
\psi\!\left(
\frac{a_{J,e}(x)}{(1-\kappa)\lambda}
\right).}
\tag{3.3}
\]

In particular, \(e(t)=o(t)\) is sufficient whenever \(\psi(t)=o(t)\).

#### Proof

For every \(p\in P_S^{e(t)}(Jx)\),

\[
\begin{aligned}
\|x-p\|
&\ge\|x-Jx\|-\|Jx-p\|\\
&\ge\lambda t-d(Jx,S)-e(t)\\
&\ge\lambda t-\psi(t)-e(t)\\
&\ge(1-\kappa)\lambda t.
\end{aligned}
\]

Take the infimum, solve for \(t\), and apply the nondecreasing error-bound
gauge. \(\square\)

For a drift formulation without proximinality, choose

\[
p_x\in P_S^{\varepsilon_x}(x),
\qquad
p_y\in P_S^{e(\|w\|)}(Jx),
\]

with \(\varepsilon_x=o(d(x,S))\), and define the infimal distance between
these approximate projection sets. The proof gains only the additive term
\(\varepsilon_x\), so the same power exponent is unchanged.

| Intended conclusion | Sufficient output-projection tolerance |
|---|---|
| Gauge/power set-distance composition | \(e(\|w\|)=o(\|w\|)\), or (3.2) |
| Moving-anchor asymptotic norm ratio | \(e(\|w\|)=o(\|w\|)\) |
| \(q\)-order defect \(Rx-p=-(x-p)+O(\|x-p\|^q)\) | \(e(\|w\|)=O(\|w\|^q)\) |

An arbitrary fixed solution anchor is insufficient in the nonisolated case.
An uncontrolled additive \(\varepsilon\) can invalidate (3.3).

---

## 4. What exponent sharpness requires

For a map-level upper exponent, use \(\Omega_J\) from (2.3). Call \(p>0\)
an exact local exponent in the two-sided witness sense when

\[
\Omega_J(r)=O(r^p)
\tag{4.1}
\]

and there is a sequence \(x_n\to S\), \(r_n=d(x_n,S)\downarrow0\), with

\[
d(Jx_n,S)\ge c r_n^p
\tag{4.2}
\]

for some \(c>0\). For an actual orbit, the corresponding two-sided exact
order is

\[
0<\liminf_k\frac{r_{k+1}}{r_k^p}
\le
\limsup_k\frac{r_{k+1}}{r_k^p}<\infty.
\tag{4.3}
\]

A positive finite normalized limit is stronger and must be stated
separately.

### Proposition 4.1 (joint-saturation criterion)

Let \(x_n\) be a local sequence and put

\[
r_n=d(x_n,S),\quad
a_n=a_J(x_n),\quad
t_n=\|w(x_n)\|,\quad
s_n=d(Jx_n,S).
\]

Suppose, for some \(\theta,q>0\),

\[
a_n\asymp r_n^\theta,
\qquad
t_n\asymp a_n,
\qquad
s_n\asymp t_n^q.
\tag{4.4}
\]

Then

\[
s_n\asymp r_n^{\theta q}.
\tag{4.5}
\]

If

\[
\frac{a_n}{r_n^\theta}\to A>0,
\quad
\frac{t_n}{a_n}\to B>0,
\quad
\frac{s_n}{t_n^q}\to C>0,
\tag{4.6}
\]

then

\[
\boxed{
\frac{s_n}{r_n^{\theta q}}
\to C B^q A^q.}
\tag{4.7}
\]

#### Proof

Multiply the three normalized ratios. \(\square\)

Sharpness of the two marginal exponents on unrelated sequences is
insufficient. GX-071 uses the same normal ray for all three limits. In
GX-072, all-pairs roughness is attained by two moving oscillatory inputs,
while solution alignment is linear.

---

## 5. GX-071: exact \(\gamma q\) through nonisolated drift

Let

\[
0<\gamma<1,
\qquad
q>\frac1\gamma,
\qquad
\alpha:=\gamma q>1,
\]

and

\[
J(t,z)=(t+|z|^\gamma,P_\alpha z),
\qquad
S=\mathbb R\times\{0\}.
\tag{5.1}
\]

The ambient \(J\) is a global triangular bijection and generates

\[
F(s,u)=\bigl(-|u|^{1/q},P_{1/\alpha}u-u\bigr).
\tag{5.2}
\]

Put \(r=|z|\), \(x=(t,z)\), and \(y=Jx\). The input and output
projections are unique:

\[
p_x=(t,0),
\qquad
p_y=(t+r^\gamma,0).
\tag{5.3}
\]

Therefore

\[
\delta_J(x)=r^\gamma,
\qquad
a_J(x)=\sqrt{r^{2\gamma}+r^2}
=r^\gamma\sqrt{1+r^{2(1-\gamma)}}.
\tag{5.4}
\]

The graph residual and next normal distance are

\[
w=x-Jx=(-r^\gamma,z-P_\alpha z),
\qquad
d(Jx,S)=r^\alpha.
\tag{5.5}
\]

Direct normalization gives

\[
\frac{a_J(x)}{r^\gamma}\to1,
\qquad
\frac{\|w\|}{a_J(x)}\to1,
\qquad
\frac{d(Jx,S)}{\|w\|^q}\to1.
\tag{5.6}
\]

Thus Proposition 4.1 applies with \(A=B=C=1\), and

\[
\boxed{
\frac{d(Jx,S)}{d(x,S)^{\gamma q}}=1}
\tag{5.7}
\]

identically. Hence:

- the alignment exponent is exactly \(\theta_*=\gamma\);
- the full-mapping error-bound exponent is maximally \(q\), with endpoint
  modulus \(1\);
- the same normal ray jointly attains the two exponents;
- the PPA recurrence is exactly \(r_{k+1}=r_k^{\gamma q}\), with normalized
  limit \(1\).

The all-pairs reflected exponent is also maximally \(\gamma\), since at a
fixed interior tangential coordinate

\[
\frac{\|R(t,z)-R(t,0)\|}{|z|^\gamma}\to2.
\tag{5.8}
\]

### Branch legality and invariant RL subwindow

The \(J/F\) branch is global and unique; no branch-existence or exclusion
problem occurs. The bounded tube is needed only for the restricted RL
quantifiers. If \(0<r_0<1\), then

\[
r_k=r_0^{\alpha^k},
\qquad
t_{k+1}=t_k+r_k^\gamma,
\]

and

\[
\sum_{k\ge0}r_k^\gamma
\le
B(r_0):=
\frac{r_0^\gamma}{1-r_0^{\gamma(\alpha-1)}}.
\tag{5.9}
\]

For the restricted tube
\((-M,M)\times(-\delta,\delta)\), it is sufficient to choose

\[
0<r_0\le\delta_0<\min\{\delta,1\},
\qquad
-M<t_0<M-B(\delta_0).
\tag{5.10}
\]

The exact tube condition replaces \(B(r_0)\) by the actual convergent sum.
The whole rectangle is not a self-map. Even if the orbit leaves this RL
tube, the global \(J\) remains legal and still converges whenever
\(0<r_0<1\).

### Evidentiary weight

GX-071 is the simplest current canonical power-shear normal form for exact
\(\theta q\). It is nonoscillatory and algebraically clean, but it remains
reverse-calibrated: the normal exponent was set to \(\alpha=\gamma q\),
while the residual was separately set to have scale \(|u|^{1/q}\). It
proves attainability and minimax exponent sharpness, not genericity,
necessity, or an application-derived compensation law. The optimal
restricted all-pairs RL constant remains unknown; this does not affect
exponent sharpness.

---

## 6. GX-072: all-pairs \(\gamma\), but alignment \(1\) and orbit \(q\)

Let

\[
q>1,
\qquad
0<\gamma<1,
\qquad
\beta:=q/\gamma-1>0,
\]

\[
h(x)=|x|^q\sin(|x|^{-\beta}),
\qquad
J(x,y)=(P_qx,P_qy+h(x)).
\tag{6.1}
\]

The triangular \(J\) is a global homeomorphism. Locally \(S=\{0\}\);
the statement is local because distant fixed points are not excluded.
Thus, in the isolated-zero localization,

\[
P_S(x)=P_S(Jx)=\{0\},
\qquad
\delta_J(x)=0,
\qquad
a_J(x)=d(x,S)=\|x\|.
\tag{6.2}
\]

The exact alignment exponent is \(1\). The verified estimate is

\[
2^{-1-q/2}\|z\|^q
\le\|Jz\|
\le\sqrt5\,\|z\|^q.
\tag{6.3}
\]

Choose \(\delta>0\) inside the isolated-zero localization with
\(\sqrt5\,\delta^{q-1}<1\). Then \(B_\delta(0)\) is invariant, every
nonzero orbit remains nonzero and converges, and

\[
0<2^{-1-q/2}
\le\frac{r_{k+1}}{r_k^q}
\le\sqrt5<\infty.
\tag{6.4}
\]

Thus \(q\) is the exact orbit exponent in the uniform two-sided sense and
\(q>\gamma q\). A positive finite limit in (6.4) has not been proved and
must not be claimed; the oscillatory phase is not controlled and may prevent
convergence of the normalized ratio. For map-level sharpness, phase-zero inputs \((x_n,0)\)
satisfy

\[
\frac{\|J(x_n,0)\|}{\|(x_n,0)\|^q}=1,
\tag{6.5}
\]

so every exponent above \(q\) fails.

The two-scale extrema calculation independently gives maximal local
all-pairs reflected exponent

\[
\gamma=\frac{q}{\beta+1}<1.
\tag{6.6}
\]

More precisely, for the adjacent extrema sequence,

\[
\frac{\|R(x_n,0)-R(y_n,0)\|}
{|x_n-y_n|^\gamma}
\longrightarrow
4\left(\frac{\beta}{\pi}\right)^\gamma.
\tag{6.7}
\]

Thus the optimal endpoint RL constant is at least the displayed limit, but
its exact value remains unknown. This roughness is attained by two nearby
nonzero inputs, not against the solution anchor. Hence

\[
\text{all-pairs exponent }\gamma
\;<\;
\text{alignment exponent }1,
\qquad
\text{actual orbit exponent }q>\gamma q.
\]

The frequency choice \(\beta=q/\gamma-1\) is reverse-calibrated, and the
triangular oscillation is engineered. It is a strong separation witness,
not evidence that arbitrary natural operators exhibit a prescribed pair
\((\gamma,q)\).

---

## 7. GX-073: one-step scaling and finite escape

Let

\[
0<\alpha<1,
\qquad
\beta>0,
\qquad
0<\delta<1,
\]

and on the natural Minty domain \([-\delta,\delta]\) set

\[
R(x)=P_\alpha(x)[2+\sin(|x|^{-\beta})],
\qquad
J=\frac{I+R}{2}.
\tag{7.1}
\]

Although \(J\) folds in primal-output coordinates and the generated \(F\)
is set-valued, \(J_F\) is the exact single-valued resolvent on its natural
Minty domain, not an arbitrary selection. The local solution set is
\(S=\{0\}\). The full generated multifunction has maximal fixed-target
regularity exponent \(q_*=1\), with exact linear modulus \(1\). Hence the
superlinear premise of Theorems 2.1 and 3.1 is absent.

For \(r=|x|>0\) and
\(c(x)=2+\sin(r^{-\beta})\in[1,3]\),

\[
r_+:=|Jx|
=\frac{r+c(x)r^\alpha}{2},
\qquad
\frac{r_+}{r^\alpha}
=\frac{r^{1-\alpha}+c(x)}2.
\tag{7.2}
\]

Thus

\[
\frac12r^\alpha\le r_+\le2r^\alpha,
\tag{7.3}
\]

with local envelope liminf \(1/2\) and limsup \(3/2\). Since
\(0<r<1\) and \(c(x)\ge1\), one has \(r_+>r\). If a nonzero orbit
remained forever in the natural domain, its increasing radii would converge
to some \(\ell>0\); continuity at \(\ell\) would imply a fixed point, which
would require \(\ell^{1-\alpha}=c(\ell)\ge1\), impossible for
\(\ell<1\). Hence the restricted resolvent orbit leaves its natural domain
in finite time. No sufficiently small symmetric neighborhood is invariant.

The anchored reflected exponent is maximally \(\alpha\), with exact local
constant \(3\), while the all-pairs exponent is maximally

\[
\eta_*=\frac{\alpha}{\beta+1}<\alpha.
\tag{7.4}
\]

Along the adjacent-extrema sequence,

\[
\frac{|R(x_n)-R(y_n)|}{|x_n-y_n|^{\eta_*}}
\longrightarrow
2\left(\frac{\beta}{\pi}\right)^{\eta_*}.
\tag{7.5}
\]

The optimal endpoint all-pairs constant is therefore at least this limit
and otherwise remains unknown. These are one-step regularity facts, not
PPA convergence orders. GX-073 is a localization/invariance guard example,
not a counterexample to the \(q>1\) alignment theorem and not an exact
\(\theta q\) witness.

---

## 8. Final classification and claim-safe wording

| Item | Mathematically established | Claim that must be avoided |
|---|---|---|
| Alignment profile | Projection-based \(a_J\) and drift-based \(r+\delta_J\) are equivalent up to factor \(3\) | Defining alignment as \(d(Jx,S)^{1/q}\), which is circular |
| Gauge composition | \(\Omega_J(r)\le\psi(2\mathcal A_J(r)/\lambda)\) under a named branch and superlinear gauge | Calling the composition alone a deep or novel classification theorem |
| Approximate anchors | \(o(\|w\|)\)-nearest output anchors preserve the exponent | Using an uncontrolled \(\varepsilon\)-nearest or arbitrary fixed solution anchor |
| Product exponent | \(\theta q\) is a uniform upper exponent | Calling it exact without joint lower saturation |
| GX-071 | Exact normalized \(\gamma q\) recurrence and invariant RL subwindow | Natural, necessary, or universal compensation law |
| GX-072 | Uniform two-sided orbit exponent \(q>\gamma q\) | Claiming a normalized orbit limit without proof |
| GX-073 | Exact one-step exponents and finite escape from the Minty domain | Calling \(\Theta(r^\alpha)\) a convergence order |

The foundation can safely freeze the following narrative:

> A superlinear output error bound converts a resolvent-step/alignment scale
> into a normal-distance scale through gauge composition. Isolated solutions
> have zero nearest-anchor drift and hence the full \(q\)-order. For a
> nonisolated solution set, tangential movement of the nearest solution
> anchor can enlarge the step from \(r\) to \(r^\theta\), producing the
> upper exponent \(\theta q\). This product is exact only when alignment,
> residual, and error-bound scales are jointly attained.

No application-derived exact-\(\gamma q\) example is present in the
reviewed assets. GX-071 is already the minimal power-shear normal form;
making it shorter does not remove its reverse calibration. Finding a
prox-regular-manifold, variational-inclusion, or optimization-derived
example with the same joint saturation is a separate research task, not a
gap in the correctness of the foundation.

---

## 9. Source and proof audit

Reviewed project assets:

- work/rl_genuine_exponent.md;
- research/example_properties.md;
- work/c_gx066_077.md;
- research/gap_examples.md;
- upload/01-RL_Submonotonicity-.md;
- work/rl_proof_referee.md.

Quality checks completed:

- separated fixed, input-nearest, output-nearest, and all-pairs anchors;
- made the Minty branch and its domain explicit;
- avoided exact projections without an exact/approximate existence route;
- proved the gauge theorem before specializing to powers;
- distinguished upper order, two-sided exact order, and normalized limit;
- required joint rather than marginal exponent saturation;
- rechecked all parameter ranges and invariant-domain conditions of
  GX-071--073;
- retained the unknown status of optimal endpoint RL constants;
- made no prior-art or novelty claim.

Source-level repair notes not applied to the source files:

- in work/c_gx066_077.md, the GX-072 phrase
  “residual-jump-in-scale mechanism” is stale: the residual tends to zero,
  so the correct mechanism label is SUPERLINEAR-GERM/scale separation, as
  already reflected in research/example_properties.md;
- the GX-071 parameter line in work/c_gx066_077.md contains the TeX typo
  “,qquad” instead of “,\(\qquad\)”;
- “selected iteration” for GX-073 is weaker than the verified fact: on its
  natural Minty domain, \(J_F\) is the exact unique restricted resolvent.

## Expert contract

~~~yaml
contract_version: "1.0"
expert_skill: sci-skills-manuscript-writing
project_id: monotonicity-regularity-seesaw-2026-09
paper_family: T
stage_id: T5
task_id: RL-FND-SHARP-04
task_status: COMPLETE
inputs_reviewed:
  - work/rl_genuine_exponent.md
  - research/example_properties.md
  - work/c_gx066_077.md
  - research/gap_examples.md
  - upload/01-RL_Submonotonicity-.md
  - work/rl_proof_referee.md
outputs:
  - work/rl_foundations_alignment_sharpness.md
evidence_status:
  - VERIFIED_USER_MATERIAL: GX-071--073 definitions, ranges, and project audits
  - VERIFIED_ALG: exact/approximate projection-profile composition proofs
  - VERIFIED_ALG: joint-saturation criterion and GX-071 normalized limits
  - VERIFIED_ALG: GX-072 two-sided q-order and GX-073 finite escape
  - AI_INFERENCE: publication significance and naturalness assessments only
assumptions:
  - a named single-valued Minty branch exists on the stated local input domain
  - the error bound holds at every branch output used in the theorem
  - exact-profile statements assume the named projection sets are nonempty
  - approximate-profile statements use tolerances satisfying Theorem 3.1
  - convergence statements additionally use the displayed invariant conditions
author_input_needed: []
manual_actions: []
quality_checks:
  - no circular definition through the desired output rate
  - complete exact-projection and epsilon-nearest-anchor quantifiers
  - explicit proof of theta-times-q gauge composition
  - map-level, orbit-level, and normalized-limit sharpness separated
  - joint rather than marginal exponent saturation checked
  - GX-071--073 parameter, branch, and invariance audit completed
  - unknown optimal RL constants preserved as unknown
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: integrate Definitions 1.1--1.2, Theorems 2.1 and 3.1, Proposition 4.1, and the claim-safe example verdicts into the optimized RL foundation while retaining the step-profile caveat
stage_acceptance_recommendation: PASS_CANDIDATE
~~~
