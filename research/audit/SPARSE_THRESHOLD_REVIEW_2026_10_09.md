# Independent reconstruction of the sparse automatic threshold and complete resolvent

Date: 2026-10-09. Scope: C224–C226 in
[the canonical sparse module](../topics/sparse_recovery/automatic_regularity.md),
with the identities in [CLAIMS.md](../../CLAIMS.md#c224) and the scope failure
[F65](../../FAILED_ROUTES.md#f65). This document supplies a separate proof;
neither earlier agent approval nor finite computation is a premise.

**Verdict.** The statements of C224–C226 inspected here are mathematically
correct. In particular, the endpoint sixth coefficient is positive in the norm
and negative in the objective, and the complete-resolvent assertion really
excludes outputs outside the local active manifold. No fatal proof gap was
found. The role of the sharp threshold needs a precise separation:

| Property at every nonzero local minimum | Range proved directly here |
| --- | --- |
| Strict complementarity on inactive coordinates | Every \(1<p<2\) |
| Linear independence of active columns | Every \(p>1\) |
| Positive definite active objective Hessian | Every \(1<p\leq3/2\) |
| Singular-Hessian strict minima exist | Every \(3/2<p<2\), by C225's family |

Thus \(3/2\) is the sharp universal active-Hessian threshold in the stated
\((1,2)\) range. It is not the threshold for strict complementarity or support
rank. The wider support-rank observation is a proved refinement in this review,
not a claim of publication priority. Mathematical validity and publishability
are considered separately at the end.

## 1. Objects, quantifiers, and first-order formula

Let \(A\in\mathbb R^{m\times n}\) have no zero column, let
\(b\in\mathbb R^m\), \(\eta>0\), and \(p>1\). Put

\[
 Q=A^TA,\qquad c=A^Tb,\qquad
 g_p(x)=\|x\|_1-\|x\|_p,
 \qquad \Phi(x)=\tfrac12\|Ax-b\|_2^2+\eta g_p(x).
\]

All norms on estimates below are Euclidean unless a subscript specifies
otherwise. Let \(F=\partial_{\rm lim}\Phi\), and let
\(S=F^{-1}(0)\). A complete resolvent is the set

\[
 J_{\lambda F}(z)=\{y\in\mathbb R^n:z-y\in\lambda F(y)\}.
\]

Its definition initially permits every output in \(\mathbb R^n\), rather than
only outputs in a previously chosen local graph. The global proximal argmin is
the set of global minimizers of
\(y\mapsto\Phi(y)+\|y-z\|^2/(2\lambda)\); for a nonconvex objective it is not
identified with the resolvent by definition.

Fix a nonzero local minimizer \(\bar x\), and set
\(I=\operatorname{supp}\bar x\). The norm \(\|\cdot\|_p\) is continuously
differentiable away from the origin. Therefore the exact smooth sum rule gives

\[
 F(x)=Qx-c+\eta\bigl(\partial\|x\|_1-\nabla\|x\|_p\bigr),\qquad x\ne0.
 \tag{1}
\]

On active coordinates the stationarity equation is an equality; on inactive
coordinates it implies \(|(Q\bar x-c)_j|\leq\eta\). On the fixed support and
sign face the objective is real analytic. Its active Hessian

\[
 H=Q_{II}-\eta\nabla^2\|\bar x_I\|_p
 \tag{2}
\]

is positive semidefinite by the ordinary second-order necessary condition.
None of these observations assumes that all stationary points are minima.

## 2. Strict complementarity for the entire range \(1<p<2\)

Suppose \(j\notin I\) and \(|(Q\bar x-c)_j|=\eta\). Choose
\(\sigma\in\{-1,1\}\) with
\(\sigma(Q\bar x-c)_j=-\eta\). For \(t>0\), write
\(x(t)=\bar x+\sigma t e_j\) and \(R=\|\bar x\|_p>0\). Direct expansion, with
the linear data and \(\ell_1\) terms cancelling, yields

\[
 \Phi(x(t))-\Phi(\bar x)
 =\tfrac12\|A_j\|^2t^2
 -\eta\bigl[(R^p+t^p)^{1/p}-R\bigr].
 \tag{3}
\]

The bracket equals
\(p^{-1}R^{1-p}t^p+O(t^{2p})\). Since \(p<2\), the right side is negative
for all sufficiently small positive \(t\), contradicting local minimality.
Hence

\[
 |(Q\bar x-c)_j|<\eta\qquad(j\notin I).
 \tag{4}
\]

This argument uses neither a rank condition nor nonzero columns; it requires a
nonzero base point and \(p<2\). It does not exclude stationary points satisfying
an inactive equality: it proves that such a point is not a local minimum.

## 3. Active curvature: exact moment reduction

Signs can be removed by a diagonal orthogonal coordinate change. Thus, for this
section, write active coordinates as \(x_i>0\). For a nonzero active direction
\(z\), define

\[
 R=\Bigl(\sum_i x_i^p\Bigr)^{1/p},\quad
 w_i=x_i^p/R^p,\quad r_i=z_i/x_i,\quad
 a=\sum_iw_ir_i,\quad s_i=r_i-a,\quad
 \mu_k=\sum_iw_is_i^k.
 \tag{5}
\]

Here all weights are positive, \(\sum_iw_i=1\), and \(\mu_1=0\). Differentiating
the norm gives the useful exact quadratic identity

\[
 z^T\nabla^2\|x\|_p z=(p-1)R\mu_2.
 \tag{6}
\]

In particular the active norm Hessian is positive semidefinite and its kernel is
exactly the radial line \(\operatorname{span}\{x\}\), for every \(p>1\).

### 3.1 A radial null direction is impossible

Assume \(H\) is singular and take \(0\ne z\in\ker H\). If \(\mu_2=0\), then
\(z=ax\) with \(a\ne0\). Homogeneity gives
\(\nabla^2\|x\|_p x=0\), so \(Hz=0\) implies \(Q_{II}x=0\), and hence
\(A_Ix=0\). Dotting active stationarity with \(x\) gives

\[
 0=\|A_Ix\|^2-b^TA_Ix+\eta(\|x\|_1-\|x\|_p).
 \tag{7}
\]

If there are at least two active coordinates, the final parenthesis is strictly
positive, a contradiction. If there is one active coordinate, \(A_Ix=0\)
contradicts the nonzero-column assumption. Thus any hypothetical Hessian null
direction must have \(\mu_2>0\).

The use of \(c=A^Tb\) in (7) is structural: \(A_Ix=0\) also makes the linear
data term vanish. An arbitrary linear term paired with a positive semidefinite
quadratic does not have this property; Section 6 gives a counterexample.

### 3.2 Cubic cancellation and Pearson's exact square

For small \(t\), all factors in the following expression are positive, and

\[
 \frac{\|x+tz\|_p}{R}
 =(1+at)f\!\left(\frac{t}{1+at}\right),\qquad
 f(u)=\left(\sum_iw_i(1+us_i)^p\right)^{1/p}.
 \tag{8}
\]

The Taylor coefficients of \(f(u)=1+c_2u^2+c_3u^3+c_4u^4+O(u^5)\) are

\[
 \begin{aligned}
 c_2&=\frac{p-1}{2}\mu_2,\\
 c_3&=\frac{(p-1)(p-2)}6\mu_3,\\
 c_4&=\frac{(p-1)(p-2)(p-3)}{24}\mu_4
       -\frac{(p-1)^3}{8}\mu_2^2.
 \end{aligned}
 \tag{9}
\]

For example, these follow by first expanding the inner sum as
\(1+\binom p2\mu_2u^2+\binom p3\mu_3u^3+\binom p4\mu_4u^4+O(u^5)\)
and then applying the binomial expansion with exponent \(1/p\).
Formula (8) gives cubic coefficient \(c_3-ac_2\) and quartic coefficient
\(c_4-2ac_3+a^2c_2\) along the original direction.

Active stationarity kills the linear objective term; \(z\in\ker H\) kills the
quadratic objective term. The data term is quadratic and \(\ell_1\) is affine
on this face, so every remaining objective coefficient is \(-\eta R\) times
the corresponding norm coefficient. A two-sided local minimum must have zero
cubic term. Since \(c_2>0\), this requires \(a=c_3/c_2\), leaving norm quartic
coefficient

\[
 C_4=c_4-c_3^2/c_2.
 \tag{10}
\]

The necessary moment inequality is the following exact identity, so no imported
moment theorem or equality classification is needed:

\[
 D:=\mu_4-\mu_2^2-\frac{\mu_3^2}{\mu_2}
 =\sum_iw_i\left(s_i^2-\mu_2-\frac{\mu_3}{\mu_2}s_i\right)^2\geq0.
 \tag{11}
\]

Indeed, expansion of the square uses only \(\mu_1=0\) and
\(\sum_iw_i=1\). Substitution into (10) gives the stronger exact decomposition

\[
 \boxed{
 C_4=
 \frac{(p-1)(p-2)(p-3)}{24}D
 +\frac{(p-1)(3-2p)(p+1)}{24}\mu_2^2
 +\frac{(p-1)(2-p)(p+1)}{72}\frac{\mu_3^2}{\mu_2}.}
 \tag{12}
\]

For \(1<p<3/2\), all terms are nonnegative and the middle term is strictly
positive. Hence \(C_4>0\), making the objective's quartic coefficient negative.
This contradicts local minimality.

### 3.3 Endpoint equality: the sixth coefficient cannot be omitted

At \(p=3/2\), (12) becomes

\[
 C_4=\frac1{64}D+\frac5{576}\frac{\mu_3^2}{\mu_2}\geq0.
 \tag{13}
\]

Positive \(C_4\) already contradicts minimality. If \(C_4=0\), then
\(D=0\) and \(\mu_3=0\). Equality in (11), together with strictly positive
weights, forces \(s_i^2=\mu_2\) at every coordinate. Put
\(d=\sqrt{\mu_2}>0\). All \(s_i\) equal \(d\) or \(-d\); the zero first
moment forces total weight \(1/2\) on each sign. Moreover \(a=c_3/c_2=0\).
Thus the entire norm restriction, rather than only four Taylor coefficients,
reduces to

\[
 \frac{\|x+tz\|_{3/2}}R
 =\left(\frac{(1+dt)^{3/2}+(1-dt)^{3/2}}2\right)^{2/3}
 =1+\frac{d^2t^2}{4}+\frac{d^6t^6}{192}+O(t^8).
 \tag{14}
\]

For an explicit coefficient check, the inner average is
\(1+3u^2/8+3u^4/128+7u^6/1024+O(u^8)\), with \(u=dt\). Raising it to power
\(2/3\) gives zero fourth coefficient and sixth coefficient

\[
 \frac7{1536}-\frac1{512}+\frac1{384}=\frac1{192}.
\]

The objective's quadratic term was already zero, all odd terms vanish in this
balanced restriction, and its sixth coefficient is
\(-\eta R d^6/192<0\). This is the final contradiction. Consequently

\[
 H\succ0\qquad\text{at every specified minimum when }1<p\leq3/2.
 \tag{15}
\]

There is no unresolved endpoint equality case. Dropping the sixth-order step
would leave a real gap, because the fourth coefficient can equal zero.

## 4. Support rank does not need the \(3/2\) threshold

For completeness, suppose only \(p>1\) and \(\bar x\ne0\) is a local minimum.
Then \(H\succeq0\). If \(A_I\) were column rank deficient, choose
\(0\ne z\in\ker A_I\). By (6),

\[
 0\leq z^THz=-\eta(p-1)R\mu_2\leq0.
\]

It follows that \(\mu_2=0\), so \(z=a\bar x_I\) with \(a\ne0\), and therefore
\(A\bar x=0\). Equation (7) gives the same contradiction as before. Thus

\[
 \operatorname{rank} A_I=|I|\leq\operatorname{rank} A
 \qquad\text{for every }p>1.
 \tag{16}
\]

The canonical derivation from \(H\succ0\) is valid but proves a narrower
range than this direct second-order argument. This is a scope refinement, not
a repair of a false statement.

## 5. Sharpness above \(3/2\): full-space strict minima

Fix \(3/2<p<2\), set \(\eta=1\), \(\bar x=(1,1)\), and \(R=2^{1/p}\). Let
the positive definite matrix \(Q\) have eigenvalues \(\alpha>0\) on \((1,1)\)
and

\[
 \beta=R(p-1)/2
\]

on \((1,-1)\). Put
\(c=Q\bar x+(1-R/2)(1,1)\), \(A=Q^{1/2}\), and \(b=A^{-T}c\).
Thus \(Q=A^TA\), \(c=A^Tb\), all columns are nonzero, and active stationarity
at \(\bar x\) holds exactly. The active Hessian has eigenvalues \(\alpha\)
and zero.

Use coordinates \(x=(1+h+t,1+h-t)\). For

\[
 c_2=(p-1)/2,\qquad
 c_4=-\frac{(p-1)(2p-3)(p+1)}{24}<0,
\]

the exact symmetric norm representation and Taylor expansion give

\[
 \Phi(h,t)-\Phi(0,0)
 =\alpha h^2+\beta ht^2-Rc_4t^4
   +O(h^2t^2+|h|t^4+t^6).
 \tag{17}
\]

Here \(\Phi(h,t)\) denotes the original objective composed with the displayed
coordinate map. Since \(\partial_{hh}\Phi(0,0)=2\alpha>0\), the analytic
implicit function theorem applies to \(\partial_h\Phi=0\). It gives a unique
analytic even local critical curve

\[
 h(t)=-\frac\beta{2\alpha}t^2+O(t^4),
 \qquad
 \Phi(h(t),t)-\Phi(0,0)=Kt^4+O(t^6),
 \quad K=-Rc_4-\frac{\beta^2}{4\alpha}.
 \tag{18}
\]

Choose \(\alpha>\beta^2/(-4Rc_4)\), so \(K>0\). Shrinking a rectangle if
necessary makes \(\partial_{hh}\Phi\geq\alpha\), keeps the critical curve and
the vertical connecting segments inside it, and gives

\[
 \Phi(h,t)-\Phi(0,0)
 \geq\frac\alpha2|h-h(t)|^2+\frac K2t^4.
 \tag{19}
\]

The coordinate map is invertible and remains in the positive orthant locally,
so this proves a strict minimum in the full ambient space, not merely on a
tangent line. It also proves sharpness of the universal active-PD statement.

Every nearby stationary point lies on the curve (18). The derivative of its
reduced objective is \(4Kt^3+O(t^5)\), so after shrinking it vanishes only at
\(t=0\). Thus the point is stationary-isolated. Along the curve,

\[
 \|x(t)-\bar x\|=\sqrt2|t|(1+O(t^2)),\qquad
 r_F(x(t))=2\sqrt2K|t|^3+O(|t|^5).
 \tag{20}
\]

The residual formula follows from
\(\partial_h\Phi=F_1+F_2=0\) and \(\partial_t\Phi=F_1-F_2\).
If a ball \(B_\varepsilon(\bar x)\) contains no other stationary point, then
for \(x\in B_{\varepsilon/3}(\bar x)\), every stationary point outside that
ball is farther away than \(\bar x\). Hence
\(\operatorname{dist}(x,S)=\|x-\bar x\|\) there. Equation (20) excludes every
true-residual error bound with exponent greater than \(1/3\).

This section does not use a critical curve as a proximal invariant curve.
Actual PPA dynamics and a matching lower error bound are independent
obligations; their resolution must be carried by their own proof.

## 6. Scope attacks: zero columns, origin, and arbitrary linear terms

**A zero active column permits a flat minimum.** For
\(A=[0,1]\), \(b=0\), every \((a,0)\), \(a\ne0\), is a global minimum:
both the data term and the nonnegative penalty vanish there. Its active
Hessian is zero. This is an exact counterexample to removing the
nonzero-column hypothesis from the automatic-isolation assertion.

**The origin has a separate and complete minimum classification.** Along the
coordinate axis \(te_j\) the penalty vanishes, so

\[
 \Phi(te_j)-\Phi(0)=\tfrac12\|A_j\|^2t^2-c_jt.
\]

A local minimum at zero therefore requires \(c=0\). Conversely, if \(c=0\)
and there are no zero columns, then for every \(x\ne0\),

\[
 \Phi(x)-\Phi(0)=\tfrac12\|Ax\|^2+\eta g_p(x)>0.
\]

Indeed \(g_p\geq0\), with equality precisely on at-most-one-sparse vectors;
every nonzero such vector has strictly positive data cost. Thus zero is the
unique global minimum. For a nonzero stationary point, dotting (1) with \(x\)
would make the same strictly positive expression, with the quadratic doubled,
equal zero. Hence there are no nonzero stationary points when \(c=0\).

Origin stationarity alone is weaker. For example, with \(A=I_2\),
\(\eta=1\), and \(b=(0,1/2)\), the vectors \((0,1/2)\) belong to
\(\partial g_p(te_1)\) for every \(t>0\). Passing to the limit shows
\(c\in\partial_{\rm lim}g_p(0)\), so \(0\in F(0)\), but
\(\Phi(se_2)-\Phi(0)=s^2/2-s/2<0\) for \(0<s<1\). This explicitly shows why
the nonzero formula (1) cannot simply be evaluated at the origin and why
origin stationarity cannot be conflated with origin minimality.

**Least-squares compatibility cannot be dropped.** For a quadratic objective
\(\tfrac12x^TQx-c^Tx+g_p(x)\) with unrelated \(Q,c\), fix any \(p>1\), put
\(R=2^{1/p}\), \(\beta>R(p-1)/2\), and take

\[
 Q=\frac\beta2\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
 c=(1-R/2)(1,1),\qquad \bar x=(1,1).
\]

The Gram matrix can be represented by
\(A=\sqrt{\beta/2}[1,-1]\), which has no zero column, but \(c\notin
\operatorname{range}A^T\). In coordinates \(x=(u+t,u-t)\), with \(u\) near
one, the objective relative to its value on \(t=0\) is

\[
 \beta t^2+Ru-\|(u+t,u-t)\|_p.
\]

It vanishes identically on \(t=0\), has zero first derivative in \(t\), and
its second \(t\)-derivative at \((u,t)=(1,0)\) equals
\(2\beta-R(p-1)>0\). Continuity and the integral Taylor remainder give
nonnegativity for all nearby \((u,t)\). Thus \(\bar x\) is a flat local
minimum with a radial Hessian kernel. The least-squares condition excludes
exactly this mechanism through (7).

## 7. Complete quantitative resolvent theorem

Return to \(1<p\leq3/2\), the least-squares model, and the fixed nonzero local
minimum. If \(I^c\ne\varnothing\), define

\[
 \delta=\min_{j\notin I}\bigl[\eta-|(Q\bar x-c)_j|\bigr]>0.
\]

Every condition below involving \(\delta\) or an inactive row is omitted when
\(I\) is full. Choose a radius \(\rho>0\) such that its ball excludes zero,
preserves every active sign, and satisfies:

\[
 \begin{array}{ll}
 \text{(A)}&Q_{II}-\eta\nabla^2\|u\|_p\succeq mI
 \quad\text{on }B_\rho(\bar x_I),\quad m>0;\\[2mm]
 \text{(B)}&|(Qy-c)_j-\eta\nabla_j\|y\|_p|
 \leq\eta-\delta/2\quad
 (y\in B_\rho(\bar x),\ j\notin I).
 \end{array}
 \tag{21}
\]

An explicit way to choose these constants is given in Section 8. Put

\[
 C_n=n^{1/p-1/2},\quad L_p=\sqrt n+C_n,\quad
 M=\|Q\bar x-c\|+\|Q\|\rho/4+\eta L_p.
 \tag{22}
\]

Choose

\[
 0<\lambda_{\min}\leq\lambda_{\max},\quad
 \lambda_{\max}M<\rho/2,\qquad
 0<r<\min\{\rho/4,\lambda_{\min}\delta/2\}.
 \tag{23}
\]

Then for every \(\lambda\in[\lambda_{\min},\lambda_{\max}]\) and every
\(z\in B_r(\bar x)\), the complete set \(J_{\lambda F}(z)\) is a singleton,
equals the global proximal argmin, lies in \(B_r(\bar x)\), and has exactly
support \(I\) and the signs of \(\bar x_I\). Moreover, for any two inputs in
that ball,

\[
 \|J_{\lambda F}(z)-J_{\lambda F}(z')\|
 \leq\frac{\|z-z'\|}{1+\lambda m}.
 \tag{24}
\]

Thus (24) includes the anchored contraction claimed in C226 and supplies its
literal pairwise-contraction version.

### 7.1 Global output localization, including possible origin outputs

For \(p\leq2\), the norm comparison
\(\|v\|_p\leq C_n\|v\|_2\) and the triangle inequality show that \(g_p\) is
globally \(L_p\)-Lipschitz. Every Fréchet subgradient of an \(L_p\)-Lipschitz
function has Euclidean norm at most \(L_p\): combine its lower directional
first-order bound with the Lipschitz upper bound in every unit direction.
Passing to limits gives the same estimate for every limiting subgradient.

Globally, including at zero, the smooth sum rule is
\(F(y)=Qy-c+\eta\partial_{\rm lim}g_p(y)\). Hence a complete resolvent output
obeys, for some \(w\in\partial_{\rm lim}g_p(y)\) with \(\|w\|\leq L_p\),

\[
 (I+\lambda Q)(y-z)=\lambda(c-Qz-\eta w).
\]

Because \(Q\succeq0\), \(\|(I+\lambda Q)^{-1}\|\leq1\). Thus

\[
 \|y-z\|\leq\lambda(\|Qz-c\|+\eta L_p)
 \leq\lambda M<\rho/2,
 \qquad \|y-\bar x\|<3\rho/4.
 \tag{25}
\]

This step has not used a local formula at an unlocalized output. In particular
it excludes an origin output because the resulting ball excludes zero. It
also excludes every other possible remote output before the active argument
begins.

### 7.2 Identification and uniqueness

At a localized output, formula (1) is valid and the active signs are already
preserved. If \(j\notin I\) but \(y_j\ne0\), the resolvent equation and (B)
give

\[
 \operatorname{sign}(y_j)z_j
 =|y_j|+\lambda\operatorname{sign}(y_j)F_j(y)
 \geq |y_j|+\lambda\delta/2>\lambda\delta/2.
\]

But \(|z_j|\leq\|z-\bar x\|<r<\lambda_{\min}\delta/2\), a contradiction.
Every full output therefore lies on the same active manifold.

On that manifold let \(G\) be the smooth active gradient. Condition (A),
integrated along the line segment between two active points in the convex
ball, gives
\(\langle G(u)-G(v),u-v\rangle\geq m\|u-v\|^2\). For outputs belonging to
inputs \(z,z'\), subtracting their active resolvent equations gives

\[
 (1+\lambda m)\|u-v\|^2
 \leq\langle z_I-z'_I,u-v\rangle
 \leq\|z-z'\|\|u-v\|.
\]

This proves uniqueness for a fixed input and (24) for any two existing
outputs. It does not, by itself, prove that an output exists.

### 7.3 Existence and equality with the global proximal argmin

The proximal objective is continuous and coercive: both terms of \(\Phi\) are
nonnegative, and its added squared distance tends to infinity. It therefore
attains a global minimum. Fermat's rule places every such minimizer in the
complete resolvent. Since the latter has at most one element by Sections
7.1–7.2, it has exactly one element and coincides with the global argmin.

Stationarity at \(\bar x\) makes it an output for input \(\bar x\). Taking
\(z'=\bar x\) in (24) gives invariance of \(B_r(\bar x)\). For every sequence
\(\lambda_k\in[\lambda_{\min},\lambda_{\max}]\) and every
\(x_0\in B_r(\bar x)\), ordinary complete PPA has a unique sequence, identifies
the support after the first step, and satisfies

\[
 \|x_k-\bar x\|
 \leq (1+\lambda_{\min}m)^{-k}\|x_0-\bar x\|.
 \tag{26}
\]

### 7.4 True residual, isolation, and strictness

For \(x\in B_\rho(\bar x)\), an activated inactive coordinate and (B) imply
\(r_F(x)\geq\delta/2\). If no inactive coordinate is activated, the inactive
subgradient intervals contain zero, so
\(r_F(x)=\|G(x_I)\|\geq m\|x-\bar x\|\). Consequently

\[
 \|x-\bar x\|\leq C r_F(x),\qquad
 C=\max\{m^{-1},2\rho/\delta\},
 \tag{27}
\]

with the second constant omitted for full support. This is a strong linear
bound to the specified point using the true residual of the full limiting
subdifferential. It immediately implies local stationarity isolation.
To see strict local minimality without an unstated growth theorem, first
choose a neighborhood on which the assumed local-minimum inequality holds.
Any other equal-value point in its interior is itself a local minimum, hence
stationary. Shrinking into the isolation ball rules out all such points.

## 8. Verification of the explicit continuity constants

Set \(a_{\min}=\min_{i\in I}|\bar x_i|\), \(R=\|\bar x\|_p\),
\(s=|I|\), and \(C_s=s^{1/p-1/2}\). Define

\[
 r_0=\min\{a_{\min}/2,R/(2C_n)\},\quad
 d=a_{\min}/2,\quad N_0=R/2,\quad
 U=\max_{i\in I}|\bar x_i|+r_0,\quad V=\sqrt{s}\,U^{p-1}.
\]

The norm Hessian on the active ball is

\[
 \nabla^2\|u\|_p=(p-1)
 \left[N^{1-p}D-N^{1-2p}vv^T\right],
 \quad N=\|u\|_p,
 \quad D=\operatorname{diag}(|u_i|^{p-2}),
 \quad v_i=\operatorname{sign}(u_i)|u_i|^{p-1}.
 \tag{28}
\]

All coordinates stay away from zero and all line segments stay in the same
sign ball. The following direct bounds apply there:

\[
 \begin{array}{c|c|c}
 \text{factor}&\text{supremum bound}&\text{Euclidean Lipschitz bound}\\ \hline
 N&\text{lower bound }N_0&C_s\\
 D&d^{p-2}&(2-p)d^{p-3}\\
 v&V&(p-1)d^{p-2}\\
 N^{1-p}&N_0^{1-p}&(p-1)N_0^{-p}C_s\\
 N^{1-2p}&N_0^{1-2p}&(2p-1)N_0^{-2p}C_s\\
 vv^T&V^2&2V(p-1)d^{p-2}
 \end{array}
\]

The last line follows from
\(\|vv^T-ww^T\|\leq(\|v\|+\|w\|)\|v-w\|\). Applying the product difference
bound separately to the two terms in (28) yields exactly

\[
 \begin{aligned}
 L_H=(p-1)\bigl[&N_0^{1-p}(2-p)d^{p-3}
 +(p-1)N_0^{-p}C_s d^{p-2}\\
 &+2N_0^{1-2p}V(p-1)d^{p-2}
 +(2p-1)N_0^{-2p}C_sV^2\bigr].
 \end{aligned}
 \tag{29}
\]

Thus every term in the canonical bound has an explicit source; in particular
the negative scalar exponents cause no missing upper-coordinate dependence.
If \(h_{\min}=\lambda_{\min}(H)>0\), then imposing
\(\rho\leq h_{\min}/(2\eta L_H)\) gives (A) with
\(m=h_{\min}/2\). For one active coordinate the norm Hessian is identically
zero, so one can omit this restriction and take \(m=\|A_I\|^2\).

For (B), let \(B_Q=\max_{j\notin I}\|Q_j\|_2\). If \(\rho\leq r_0\), then
\(\|y\|_p\geq R-C_n\rho\geq R/2\), and for every inactive \(j\),

\[
 \begin{aligned}
 |(Qy-c)_j-\eta\nabla_j\|y\|_p|
 &\leq |(Q\bar x-c)_j|+B_Q\rho
       +\eta\left(\frac{2\rho}{R}\right)^{p-1}.
 \end{aligned}
 \tag{30}
\]

The additional restrictions

\[
 \rho\leq\frac\delta{4B_Q},\qquad
 \rho\leq\frac R2\left(\frac\delta{4\eta}\right)^{1/(p-1)}
 \tag{31}
\]

bound the last two terms by \(\delta/4\) each. Omit the first restriction when
\(B_Q=0\), and omit both for full support. Taking any positive \(\rho\) below
all applicable bounds proves (21). The constants are finite and positive for
the specified fixed minimum. There is no implicit uniformity over data or
minimizers and no claim that this radius is optimal.

## 9. Reproducibility, remaining scope, and publication assessment

The independent calculation performed for this review used Python's exact
`fractions.Fraction` arithmetic, without random sampling or file mutation, to
compose the symmetric endpoint series through degree eight. Its nonzero
coefficients were

\[
 1,\quad [u^2]=1/4,\quad [u^6]=1/192,\quad [u^8]=1/768.
\]

It also checked the two polynomial coefficient factorizations in (12) at
\(p=5/4,4/3,3/2,5/3,7/4\). These calculations corroborate the displayed algebra;
the exact identities (9)–(14), rather than those finitely many tests, prove the
universal result. The existing finite verifier was read through its stated
scope, but rerunning it is not claimed here.

The review supports retaining `derived-checked` for the inspected C224–C226
statements. It does not certify all stationary points, large proximal steps,
arbitrary initializations, convergence to global minima, signal recovery,
maximal basins, or optimal constants. The singular-minimum dynamics above the
threshold cannot inherit C226's strong-monotonicity proof.

For publication, the natural theorem-level center is the universal automatic
active-Hessian result, its endpoint equality mechanism, and the all-\(p\)
upper-side construction in the claimed \((1,2)\) scope. Strict complementarity,
support rank, conditional active-manifold rates, and elementary complete-output
localization should be presented in proportion to their supporting roles.
The complete-resolvent proof has a useful exact quantifier distinction, but its
truth does not make ordinary local proximal convergence a new mechanism.

This review imports no specialized external theorem beyond elementary
finite-dimensional calculus, subdifferential definitions/smooth sum and Fermat
rules, and the explicitly mapped analytic implicit function theorem in
Section 5. It performs no new literature search and certifies no paper fact.
The repository's [literature gate](../LITERATURE.md#lit-sparse-automatic-threshold)
records an existing model family and unresolved full-text priority checks.
Those checks remain necessary before describing the threshold as novel or
judging a specific journal submission ready. Internal mathematical reception
is neither a priority result nor external peer review.
