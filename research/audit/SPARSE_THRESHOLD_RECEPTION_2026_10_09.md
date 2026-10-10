# Independent threshold reception: a quartic endpoint proof and all finite upper exponents

Date: 2026-10-09. This review reconstructs C224/C228 and the sharp family
from the least-squares model, then compares that reconstruction with
[the canonical module](../topics/sparse_recovery/automatic_regularity.md)
and Section 2 of [the manuscript](../manuscripts/sparse_regularity/sharp_sparse_regularity.tex).
The moment reduction was reconstructed before reading those proofs. A second
proof-group agent independently checked both new deductions below. This is
internal mathematical evidence, not publication-priority evidence.

**Result.** No fatal objection was found to the inspected statements. Two
substantive additions are available: the endpoint also has a fourth-order
contradiction on a curved radial perturbation, and C225's construction works
for every **finite** (p>3/2), without the current upper restriction (p<2).
The second addition changes a quantified range and therefore requires a new
Claim version; this review does not silently enlarge C225-v1. C226's complete
resolvent and C227's dynamics are outside this review's reception scope.

## 1. Independent reconstruction of the curvature bottleneck

Let (A\in\mathbb R^{m\times n}) have no zero columns, (b\in\mathbb R^m),
(\eta>0), and (1<p<\infty). Set

\[
 \Phi(x)=\tfrac12\|Ax-b\|^2+\eta(\|x\|_1-\|x\|_p),\qquad
 Q=A^TA,\quad c=A^Tb.
\]

Fix a nonzero local minimum (x), restrict to its active face, and remove
coordinate signs by an orthogonal sign change. Thus (x_i>0) on that face.
The active Hessian (H=Q_{II}-\eta\nabla^2\|x\|_p) is positive semidefinite.
For a hypothetical nonzero (z\in\ker H), put

\[
 R=\|x\|_p,\quad w_i=x_i^p/R^p,\quad r_i=z_i/x_i,
 \quad a=\sum_iw_ir_i,\quad s_i=r_i-a,\quad
 \mu_k=\sum_iw_is_i^k.
\]

The norm Hessian identity is

\[
 z^T\nabla^2\|x\|_p z=(p-1)R\mu_2.
 \tag{R1}
\]

The case (\mu_2=0) is radial. It would imply (Ax=0), since the norm
Hessian annihilates (x) and (Hz=0). Active stationarity dotted with (x)
would then give (0=\eta(\|x\|_1-\|x\|_p)). This is impossible for two or
more active coordinates, and a single active coordinate contradicts the
nonzero-column assumption. Thus (\mu_2>0). The same Euler argument proves

\[
 q:=\|Ax\|^2>0
 \tag{R2}
\]

at every nonzero local minimum under these hypotheses.

Use the exact factorization

\[
 \frac{\|x+tz\|_p}{R}=(1+at)f\!\left(\frac{t}{1+at}\right),
 \qquad f(u)=\left(\sum_iw_i(1+us_i)^p\right)^{1/p}.
\]

Writing (f(u)=1+c_2u^2+c_3u^3+c_4u^4+O(u^5)), direct expansion gives

\[
 c_2=\frac{p-1}{2}\mu_2,\qquad
 c_3=\frac{(p-1)(p-2)}6\mu_3,\qquad
 c_4=\frac{(p-1)(p-2)(p-3)}{24}\mu_4
       -\frac{(p-1)^3}{8}\mu_2^2.
\]

Stationarity and (Hz=0) cancel the objective's linear and quadratic terms.
Its cubic term must vanish, so (a=c_3/c_2). The straight-line norm's
quartic coefficient divided by (R) is consequently (C_4=c_4-c_3^2/c_2).
The exact identity

\[
 \mu_4-\mu_2^2-\frac{\mu_3^2}{\mu_2}
 =\sum_iw_i\left(s_i^2-\mu_2-\frac{\mu_3}{\mu_2}s_i\right)^2
 \tag{R3}
\]

gives, for (1<p\le3/2),

\[
 C_4\ge(p-1)\left[
 \frac{(3-2p)(p+1)}{24}\mu_2^2+
 \frac{(2-p)(p+1)}{72}\frac{\mu_3^2}{\mu_2}\right]\ge0.
 \tag{R4}
\]

For (p<3/2), the first inequality is strictly positive and already
contradicts local minimality on the straight line.

## 2. A fourth-order endpoint proof by radial adjustment

This alternative avoids needing an equality classification or a sixth-order
expansion. More generally, at any hypothetical Hessian-null direction write

\[
 \|x+tz\|_p=R+n_1t+n_2t^2+n_4t^4+O(t^5),
 \qquad n_2=Rc_2>0,\quad n_4=RC_4.
 \tag{R5}
\]

There is no cubic term by the preceding necessary condition. Homogeneity and
(Hz=0) imply (x^TQz=0) and (z^TQz=2\eta n_2). All first-order terms
cancel by stationarity. Hence, for (s,t) sufficiently small,

\[
 \begin{aligned}
 V(s,t)&:=\Phi((1+s)x+tz)-\Phi(x)\\
 &=\tfrac12qs^2+
   \eta n_2\frac{s}{1+s}t^2-
   \eta n_4\frac{t^4}{(1+s)^3}+O(t^5).
 \end{aligned}
 \tag{R6}
\]

The remainder is uniform for (s) near zero: it comes from the analytic
expansion at (t/(1+s)), multiplied by (1+s). Choose

\[
 s(t)=-\frac{\eta n_2}{q}t^2.
\]

Then

\[
 V(s(t),t)=
 -\left(\eta n_4+\frac{\eta^2n_2^2}{2q}\right)t^4+O(t^5).
 \tag{R7}
\]

Thus local minimality at any Hessian-null direction necessarily requires

\[
 n_4\le-\frac{\eta n_2^2}{2q}<0,
 \quad\text{equivalently}\quad
 C_4\le-\frac{\eta R c_2^2}{2\|Ax\|^2}<0.
 \tag{R8}
\]

This contradicts (R4) for the whole range (1<p\le3/2), including the
endpoint. The perturbation preserves every active sign for small (t), and
inactive coordinates remain zero, so it is admissible for the original
unconstrained problem. No invariance or dynamical interpretation of the curve
is used. The original straight-line sixth-order proof remains valid.

For completeness, its equality case at (p=3/2) is independently verified:
(R3)–(R4) and (C_4=0) force (\mu_3=0), (a=0), and (s_i=\pm d),
(d=\sqrt{\mu_2}>0), with total weight (1/2) at each value. Therefore

\[
 \frac{\|x+tz\|_{3/2}}R
 =\left(\frac{(1+dt)^{3/2}+(1-dt)^{3/2}}2\right)^{2/3}
 =1+\frac{d^2t^2}4+\frac{d^6t^6}{192}+O(t^8).
 \tag{R9}
\]

The objective's first nonzero term on this line is
(-\eta Rd^6t^6/192), also a contradiction. In particular the sign and
coefficient of the existing endpoint argument are correct.

## 3. The sharp family extends to every finite (p>3/2)

Fix any (3/2<p<\infty), and define

\[
 R=2^{1/p},\qquad \beta=\frac{R(p-1)}2,\qquad
 c_4=-\frac{(p-1)(2p-3)(p+1)}{24}<0,
\]

\[
 \alpha_0=\frac{\beta^2}{-4Rc_4}
   =\frac{3R(p-1)}{2(2p-3)(p+1)},\qquad \alpha>\alpha_0.
 \tag{R10}
\]

Let (Q) have eigenvalues (\alpha) on ((1,1)) and (\beta) on
((1,-1)); set

\[
 A=Q^{1/2},\quad \bar x=(1,1),\quad \eta=1,\quad
 c=Q\bar x+(1-R/2)(1,1),\quad b=A^{-T}c.
 \tag{R11}
\]

Both eigenvalues are positive, so (A) is invertible with no zero columns
and (A^Tb=c). At (\bar x), (\nabla\|\bar x\|_p=(R/2,R/2)), and
the norm Hessian has radial/tangent eigenvalues (0,\beta). Hence the
objective is stationary with active Hessian eigenvalues (\alpha,0).

Every finite (p>1) gives a real analytic norm on this positive neighborhood.
For (|h|+|t|<1), set

\[
 x=(1+h+t,1+h-t),\qquad
 f_p(u)=\left(\frac{(1+u)^p+(1-u)^p}{2}\right)^{1/p}.
\]

The objective difference satisfies the exact identity

\[
 V(h,t)=\alpha h^2+\beta t^2-
 R(1+h)\left[f_p\!\left(\frac{t}{1+h}\right)-1\right].
 \tag{R12}
\]

Expansion gives (f_p(u)=1+(p-1)u^2/2+c_4u^4+O(u^6)), and thus

\[
 V(h,t)=\alpha h^2+\beta ht^2-Rc_4t^4+
 O(h^2t^2+|h|t^4+t^6).
 \tag{R13}
\]

The analytic implicit function theorem gives an even radial critical curve

\[
 h=g(t)=-\frac{\beta}{2\alpha}t^2+O(t^4),\qquad
 V(g(t),t)=Kt^4+O(t^6),\quad
 K=-Rc_4-\frac{\beta^2}{4\alpha}>0.
 \tag{R14}
\]

After shrinking the neighborhood, (V_{hh}\ge\alpha) and the reduced
objective is at least (Kt^4/2). Taylor's integral remainder gives

\[
 V(h,t)\ge\tfrac\alpha2|h-g(t)|^2+\tfrac K2t^4.
 \tag{R15}
\]

This proves a strict **full-space** local minimum with singular active
Hessian. A completely specified choice is (\alpha=2\alpha_0), for which

\[
 K=\frac{R(p-1)(2p-3)(p+1)}{48}>0.
 \tag{R16}
\]

All nearby stationary points lie on (g); there the reduced derivative is
(4Kt^3+O(t^5)), which has only the zero (t=0) locally. Thus (\bar x)
is isolated stationary. On (g),

\[
 \|x-\bar x\|\sim\sqrt2|t|,\qquad
 \operatorname{dist}(0,\partial_{\rm lim}\Phi(x))
 =|V_t(g(t),t)|/\sqrt2\sim2\sqrt2K|t|^3.
\]

In a sufficiently smaller ball, distance to the full stationary set equals
distance to (\bar x), since all other stationary points are outside a
fixed larger neighborhood. Every local residual error bound with exponent
greater than (1/3) therefore fails for this family, for every finite
(p>3/2). No matching estimate or PPA tail for the entire family is asserted
here. This extension excludes (p=\infty), where the positive-coordinate
maximum norm is nonsmooth at ((1,1)).

## 4. Boundary and arithmetic checks

- **One active coordinate.** On its fixed sign face the norm difference is
  identically zero and the active Hessian is (\|A_i\|^2>0), for all
  finite (p>1). The moment proof does not divide by a vanishing variance
  in this case; the radial case is excluded first.
- **Zero column.** For (A=[0,1]), (b=0), all nonzero ((a,0)) are
  global minima because the objective is nonnegative and vanishes there.
  Their active Hessian is zero. This is an actual exception.
- **Origin.** Both signed coordinate-axis variations force (A^Tb=0)
  whenever zero is a local minimum. Conversely, if (A^Tb=0) and there
  are no zero columns, then
  (\Phi(x)-\Phi(0)=\|Ax\|^2/2+\eta(\|x\|_1-\|x\|_p)>0)
  for every (x\ne0). Euler stationarity excludes all nonzero stationary
  points. The smooth norm-gradient formula is not applied at zero.
- **Support rank.** If (A_Iz=0), positive semidefiniteness of (H) and
  (R1) force (z\in\operatorname{span}\{x\}); the Euler/nozero-column
  argument excludes it. This proves C228's whole finite (p>1) range.
- **Inactive strictness.** Saturation of an inactive inequality yields the
  exact signed-coordinate difference
  (\|A_j\|^2t^2/2-\eta[(R^p+t^p)^{1/p}-R]), negative for small positive
  (t) whenever (1<p<2). The extension in Section 3 does not extend
  this separate assertion beyond that range.

Exact rational arithmetic with Python's standard-library `fractions` checks
the endpoint coefficients (1/4,0,1/192), and checks (R10)/(R16) at
(p=7/4,2,5/2,3,4,10). These finite checks only guard against algebraic
transcription errors; (R10)–(R16) supply the universal proof. No external
theorem beyond elementary Taylor expansion and the ordinary analytic
implicit function theorem is imported. Publication priority was not searched
or assessed in this review.
