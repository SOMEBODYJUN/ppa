# Independent review: sparse automatic regularity and complete quartic dynamics

**Date:** 2026-10-09. **Base revision inspected:** `8ff3ae18ed46d36e5ab97c27255289204a3b46b7`.

**Reception:** the C224–C226 proof in
[`automatic_regularity.md`](../topics/sparse_recovery/automatic_regularity.md)
and the complete explicit-instance proof subsequently written in
[`sharp_instance_dynamics.md`](../topics/sparse_recovery/sharp_instance_dynamics.md)
have been independently reconstructed. No mathematical blocker was found in
the latter candidate. This is internal mathematical reception, not external
peer review or a priority determination. The independent arithmetic and
actual two-coordinate recurrence check is
[`independent_complete_review.py`](../code/sparse_regularity/independent_complete_review.py).

## Reconstruction before reading the detailed candidate

The following obligations were identified independently from the model and
the requested conclusion:

- A local smooth inverse does not establish anything about distant outputs of
  the original complete limiting-subdifferential resolvent. A globally valid
  bounded-penalty-subgradient estimate must be used before restricting the
  outputs to a positive-coordinate region.
- At-most-one stationary proximal point does not itself prove existence. A
  coercive global proximal objective supplies existence independently; Fermat
  then places its minimizer in the already localized complete graph.
- For the singular-Hessian example, local positive definiteness cannot be
  assumed. A positive displacement-gradient inner product can instead prove
  strictness, stationary isolation, the residual lower bound, and invariance.
- The radial critical curve is not generally invariant under the ordinary
  Euclidean PPA. The trajectory must be analyzed in its genuine two-coordinate
  implicit equations, with a proof that the radial coordinate follows the
  leading quadratic profile.
- Symmetric inputs on the radial axis are an exceptional geometric branch.
  The polynomial-tail quantifier must exclude exactly this axis, and the
  coordinate (t) has a different normalization from Euclidean distance.

The original C225 text correctly left the matching residual and actual
trajectory obligations open. The new explicit proof closes these obligations
for its one specified (p=7/4) instance.

## C224–C226 scope and completeness

The automatic strict-complementarity argument uses the exact one-coordinate
objective variation: cancellation of the first-order term leaves a positive
quadratic and a negative order-(t^p) term. For (p<2), equality in an inactive
stationarity inequality cannot occur at a nonzero local minimum.

The active-Hessian proof starts only from the second-order necessary condition
at the assumed local minimum. It does not insert SOSC as a hypothesis. The
radial null direction is excluded using (c=A^Tb), homogeneity, and the
nonzero-column assumption. For nonradial null directions, the centered-moment
calculation, the exact Pearson square identity, and the vanishing cubic give
the displayed quartic lower bound. Its coefficient is positive for

\[
1<p<3/2.
\]

At the endpoint, quartic equality forces equal total weights on the two values
\(\pm\sqrt{\mu_2}\), zero radial coefficient, and the exact positive sixth norm
coefficient \(\mu_2^3/192\). The objective's negative sixth coefficient excludes
a local minimum. These steps give active PD rather than assuming it.

C226's complete-fiber argument remains globally valid at the origin because it
uses the smooth sum rule with \(\partial_{\rm lim}(\|\cdot\|_1-\|\cdot\|_p)\),
not a nonexistent norm gradient at zero. Its globally bounded subgradients and
the PSD resolvent of \(Q\) produce the displacement estimate for every output.
Only then are the inactive strict margins and the active Hessian invoked.
Support identification, full-output uniqueness, and active contraction follow
on the resulting common neighborhood. Global proximal existence is a
separate continuous/coercive minimization argument.

The explicit continuity radius and each of the four displayed terms in
\(L_H\) are consistent with the scalar mean-value bounds, the norm equivalence
constant, and the rank-one difference estimate. A positive lower step bound
is required for one common inactive identification radius and a uniform
geometric rate. The constants are local to the specified minimum and data;
there is no data-uniform conditioning or global recovery claim.

## Explicit instance and historical constants

For the proposed matrix and linear term,

\[
R=2^{4/7},\quad
Q=\frac R{16}\begin{pmatrix}19&13\\13&19\end{pmatrix},\quad
c=(1+3R/2)(1,1),
\]

the eigenvalues are \(2R\) radially and \(3R/8\) tangentially. Since \(Q\succ0\),
\(A=Q^{1/2}\), \(b=A^{-T}c\) realize actual least squares with \(A^Tb=c\).
At \(\bar x=(1,1)\), the norm gradient is \((R/2,R/2)\), so active stationarity
is exact, and the tangent Hessian vanishes.

Put \(s=1+h\), \(u=t/s\), and

\[
f(u)=\left(\frac{(1+u)^{7/4}+(1-u)^{7/4}}2\right)^{4/7}.
\]

The exact objective difference is

\[
\varphi(h,t)/R=2h^2+\frac38t^2-s(f(u)-1).
\]

The independently computed coefficients are

\[
f(u)=1+\frac38u^2-\frac{11}{256}u^4+E(u),\qquad
\varphi/R=2h^2+\frac38ht^2+\frac{11}{256}t^4+
O(h^2t^2+|h|t^4+t^6).
\]

The historical input radius \(1/64\) and upper step \(1/128\) are valid with a
fully analytic certificate. They need not be weakened or left unverified.
For any input in the closed radius-\(1/64\) ball, the global subgradient
estimate yields

\[
\|y-z\|\le\lambda\bigl(\|Qz-c\|+\sqrt2+2^{1/14}\bigr),
\]

for every output of the complete graph. The bracket is less than

\[
\frac37+\frac3{64}+\frac{10}7+\frac{15}{14}
=2.975446428571\ldots<3.
\]

Consequently every output has displacement less than \(5/128\) from \(\bar x\)
and satisfies \(|h|,|t|<1/32\), since \(25<32\). This rules out remote outputs,
including nonsmooth outputs and zero, before any local Hessian argument.

On this convex box both original coordinates are at least \(15/16\). The
norm-Hessian estimate gives the conservative bound

\[
0\preceq\nabla^2\|x\|_{7/4}\preceq\frac45R^{-3/4}I\prec I.
\]

Thus \(\nabla^2\Phi\succ-I\), and the proximal stationary map has positive
definite Jacobian for every \(0<\lambda\le1/128\). All complete outputs are in
the same convex box, so uniqueness is genuine full-fiber uniqueness. The
continuous nonnegative global objective plus the quadratic proximal term is
coercive, giving independent existence. Therefore this unique output also is
the unique global proximal minimizer.

## Analytic remainder and star certificate

The complex radius \(r=7/8\) is valid: the positive, decreasing even
coefficients of \(G(u)=((1+u)^{7/4}+(1-u)^{7/4})/2\) give

\[
|G(u)-1|\le\frac{21}{32}r^2+
\frac{35}{2048}\frac{r^4}{1-r^2}
=\frac{214375}{393216}<1.
\]

The chosen branch of \(G^{4/7}\) is analytic on a neighborhood of the closed
disk, with modulus less than two. Cauchy estimates and the even power-series
tail imply, for all real \(|u|\le1/16\),

\[
|E|\le5|u|^6,\quad |E'|\le28|u|^5,\quad |E''|\le140|u|^4.
\]

The exact rational upper constants before rounding are approximately
\(4.47923\), \(26.92131\), and \(134.97500\). The second derivative majorant
uses the coefficient \(26v/(1-v)^2\); replacing 26 by 22 in that particular
summation formula would be an arithmetic error.

For \(D=\langle x-\bar x,\nabla\Phi(x)\rangle\), differentiation gives exactly

\[
D/R=4h^2+\frac98hu^2+\frac34h^2u^2+
\left(\frac{11}{64}+\frac{11h}{256}\right)u^4-hE-uE'.
\]

On \(|h|,|t|\le1/32\), \(|u|\le1/31\). Completion of the square leaves the
rational coefficient

\[
\frac{95}{1024}-\frac{11}{8192}-\frac{28+5/32}{961}
=0.062131756674\ldots>\frac1{32}.
\]

Also \(2(9/64)^2+(33/32)^4=1.170533180236\ldots<2\). These facts give

\[
D\ge\frac R{64}(h^2+t^4).
\]

Integration along a ray proves a strict local minimum; positivity proves
stationary isolation. Since the box is smooth and positive-coordinate,
\(r_F=\|\nabla\Phi\|\) is the true complete residual there. With
\(d=\sqrt{2(h^2+t^2)}\),

\[
d\,r_F\ge D\ge Rd^4/512,
\]

which proves the matching strong residual error bound with exponent \(1/3\).
On the analytic radial critical curve,

\[
h_*(t)=-3t^2/32+O(t^4),\quad
\varphi(h_*(t),t)=13Rt^4/512+O(t^6),\quad
r_F\sim13R|t|^3/(128\sqrt2),
\]

so every exponent greater than \(1/3\) fails. The closed input ball is small
enough that the entire stationary set has the same nearest point \(\bar x\).

The exact squared-distance identity

\[
\|z-\bar x\|^2=\|y-\bar x\|^2+2\lambda D(y)+
\lambda^2\|\nabla\Phi(y)\|^2
\]

proves invariance for every permitted step, with no SOSC at this singular
minimum. Summation proves convergence for fixed positive \(\lambda\), and
also for arbitrary steps in a fixed positive interval
\([\lambda_{\min},\lambda_{\max}]\subset(0,1/128]\).

## Actual trajectory, exceptional axis, and normalization

The ordinary Euclidean proximal equations are

\[
h_k=h_{k+1}+(\lambda/2)\varphi_h(h_{k+1},t_{k+1}),\qquad
t_k=t_{k+1}+(\lambda/2)\varphi_t(h_{k+1},t_{k+1}).
\]

The factors \(1/2\) are essential. They come from the metric
\(\|x-x_k\|^2=2[(h-h_k)^2+(t-t_k)^2]\).

The exact tangent equation is odd in \(t\), with strictly positive multiplier
on the box. In particular \(t_{k+1}=0\) if and only if \(t_k=0\). For nonzero
\(t_0\), all iterates keep its sign and \(t_k/t_{k+1}\to1\). On \(t_0=0\), the
exact formula is

\[
t_k=0,\qquad h_k=(1+2\lambda R)^{-k}h_0.
\]

The diagonal radial axis therefore cannot be included in an all-input
polynomial-tail statement.

For nonzero \(t_0\), set \(w_k=h_k/t_k^2\),
\(q=(1+2\lambda R)^{-1}\), and \(b_0=3\lambda R/16\). The radial equation gives

\[
w_{k+1}=q(t_k/t_{k+1})^2w_k-qb_0+\epsilon_k,
\qquad \epsilon_k\to0.
\]

The divided remainder is \(O(|h_{k+1}|+t_{k+1}^2)\), so this step does not
assume \(w_k\) bounded. The coefficient tends to \(q<1\); eventual scalar
contraction first bounds \(w_k\), then forces its limit to the fixed point
\(-3/32\). This is the noncircular radial-following proof.

Substitution at the actual trajectory yields

\[
t_k=t_{k+1}\left[1+\frac{13\lambda R}{256}t_{k+1}^2+
o(t_{k+1}^2)\right],\qquad
|t_{k+1}|^{-2}-|t_k|^{-2}\longrightarrow\frac{13\lambda R}{128}.
\]

Thus

\[
\sqrt{k}|t_k|\to\sqrt{128/(13\lambda R)},\qquad
\sqrt{k}\|x_k-\bar x\|\to16/\sqrt{13\lambda R}.
\]

The claimed constant 16 belongs to Euclidean distance. Assigning that same
constant to \(|t_k|\) would produce a factor-\(\sqrt2\) error. The candidate
states both constants correctly. No invariant critical-curve premise enters
this argument. Its asymptotic constant is asserted for one fixed step, as
required; it is not silently extended to arbitrary variable steps.

The proof does not assert a residual asymptotic along the actual iterates.
The first tracking limit alone only gives
\(h_k+3t_k^2/32=o(t_k^2)\); stronger radial remainder control would be needed
before extracting the leading actual residual coefficient.

## Reproducible independent checks and final scope

Running `python research/code/sparse_regularity/independent_complete_review.py`
succeeds. Besides the exact rational gates above, it solves the genuine
two-dimensional implicit equations for 50,000 steps from
\((h_0,t_0)=(0.002,0.010)\), inside the certified ball. It reports

- \(h_k/t_k^2=-0.093749017814\), against the analytic limit \(-0.09375\);
- inverse-\(t^2\) increment \(0.001179017682\), against
  \(13\lambda R/128=0.001179072617\), relative discrepancy
  \(-4.66\times10^{-5}\);
- zero error in a checked exact radial-axis step.

These finite checks corroborate arithmetic and the actual implicit dynamics;
the analytic certificate carries remote exclusion, all-output uniqueness,
all-input invariance, true residual, and all off-axis tail quantifiers.
No maximal basin, maximal step, uniform theorem over all degenerate minima,
global attraction, or published novelty is established by this review.

## Standalone manuscript reception

The final source
[`sharp_sparse_regularity.tex`](../manuscripts/sparse_regularity/sharp_sparse_regularity.tex)
was separately inspected after compilation on 2026-10-09. This reception
covers mathematical source transcription and theorem/reference agreement;
it does not claim an independent visual PDF-layout inspection.

All 41 display equations in the dynamics section agree exactly with the
accepted `sharp_instance_dynamics.md` module after removing whitespace,
equation tags, and labels. Manual tags D.1 through D.19 occur once each in
order. The source has no duplicate labels or unresolved `ref`/`eqref`
references. The repaired definition \(S=F^{-1}(0)\) is correct, as are the
complete resolvent and true-residual definitions. The theorem retains the
closed input ball, all-output quantifiers, independent global minimizer
identity, fixed-step scope, exceptional radial axis, factors \(\lambda/2\),
tangent constant \(\sqrt{128/(13\lambda R)}\), and Euclidean-distance constant
\(16/\sqrt{13\lambda R}\).

The broader structural statement that support columns are independent for
every \(p>1\) is valid: the weighted-variance norm-Hessian identity excludes
nonradial vectors in \(\ker A_I\), and least-squares stationarity excludes the
remaining radial direction. Its transcription agrees with that argument.
The explicit continuity budgets, common positive step interval, true linear
residual bound, and origin exception have also retained their mathematical
scope.

No fatal mathematical transcription or operator error was found. The source
definition `a_*=min_{i\in I}|\bar x_i|` has a cosmetic operator-spacing issue:
the usual command is `\min`. This does not change the stated value or any
proof. No manuscript source edits were performed by this reviewer, and the
previous computations were not rerun merely for this transcription review.
