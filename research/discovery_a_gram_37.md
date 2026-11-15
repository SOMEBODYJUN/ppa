# Discovery A: the missing (3/7) Hölder exponent for the pure Gram GPPA prox

**Date:** 2026-11-14  
**Status:** discovery candidate; not a theorem and not a priority claim.

## 1. Exact question

The current C270 record studies the complete, single-valued map

\[
 T_\lambda=(v+\lambda P)^{-1}\circ v,
 \qquad P([a\ b])=[a\ 0],
 \qquad v(Z)=ZZ^TZ,
\]

on (X=\mathbb R^{m\times 2}), (m\ge 2), with Frobenius norm and fixed (\lambda>0).  In column variables (Z=[a\ b]), (Y=T_\lambda(Z)=[\alpha\ \beta]) is the unique solution

\[
 (\|\alpha\|^2+\lambda)\alpha+\langle\alpha,\beta\rangle\beta
   =\|a\|^2a+\langle a,b\rangle b,
\tag{A1}
\]
\[
 \langle\alpha,\beta\rangle\alpha+\|\beta\|^2\beta
   =\langle a,b\rangle a+\|b\|^2b.
\tag{A2}
\]

C270 proves on bounded sets that (T_\lambda) is (1/3)-Hölder and that no common exponent (>3/7) can hold.  The open interval is the only unresolved quantitative part of that claim.

The precise candidate is:

> **Candidate A (exact two-point modulus).** For every (M<\infty) and (\lambda>0), there exists (C=C(M,\lambda,m)) such that for all (Z,Z'\) with (\|Z\|_F,\|Z'\|_F\le M),
> \[
> \|T_\lambda(Z)-T_\lambda(Z')\|_F^{7/3}
> \le C\,\|Z-Z'\|_F.
> \tag{A3}
> \]
> Equivalently (T_\lambda) is (3/7)-Hölder on every bounded set.  The exponent is sharp at the origin, already on the collinear two-column slice.

The claim is deliberately about the complete physical prox and two arbitrary inputs.  It is separate from (i) the fixed-zero calm estimate, (ii) the (1/3)-Hölder limit readout, and (iii) any trajectory rate.

## 2. Reproducible sharpness calculation

Take a unit vector (c\in\mathbb R^m), (t\downarrow0), and (\zeta\ne0), and define

\[
 Z_t=[tc\ 0],\qquad Z_t'=[tc\ \zeta t^7c].
\]

Then (\|Z_t-Z_t'\|_F=|\zeta|t^7).  Write the outputs as
\(Y_t=[\alpha_t c\ 0]) and (Y_t'=[\alpha_t'c\ \beta_t'c]); uniqueness and the collinear symmetry force this form.  The first output satisfies

\[
 (\alpha_t^2+\lambda)\alpha_t=t^3,
 \qquad \alpha_t=t^3/\lambda+O(t^9).
\]

For the perturbed input, set \(\alpha_t'=t^3U_t\), \(\beta_t'=t^3W_t\).  Substitution into (A1)–(A2) gives

\[
 \lambda U_t+t^6(U_t^2+W_t^2)U_t=1+\zeta^2t^{12},
\tag{A4}
\]
\[
 (U_t^2+W_t^2)W_t=\zeta+\zeta^3t^{12}.
\tag{A5}
\]

Every bounded sequence has the unique limit
\[
 U_t\to\lambda^{-1},\qquad
 (\lambda^{-2}+W_\zeta^2)W_\zeta=\zeta,
\]
with (W_\zeta\ne0).  Hence
\[
 \|T_\lambda(Z_t')-T_\lambda(Z_t)\|_F
   =|W_\zeta|t^3+o(t^3),
\]
and
\[
 \frac{\|T_\lambda(Z_t')-T_\lambda(Z_t)\|_F^{\,q}}
      {\|Z_t'-Z_t\|_F}
 \asymp t^{3q-7}.
\]
For every (q>3/7) this diverges, so no larger common exponent is possible.  This is an exact asymptotic witness, not a finite numerical search.

The same balance has a useful angular interpretation in the collinear slice.  If (a=tc) and (b=s c), then the input cross-coordinate is (k\sim t^2s), while the observed first-column output is (\alpha\sim t^3/\lambda).  The unobserved output solves (r_Y^2\beta=k).  The transition (s\sim t^7) is exactly where the cubic-root regime (\beta\sim k^{1/3}) meets the linearized regime (\beta\sim k/t^6); both give (\beta\sim t^3).  This Newton balance explains the number (3/7).

## 3. Why the existing (1/3) argument does not close (A3)

The quartic monotonicity estimate for (v), combined with the (\lambda P) term, yields for (h=\|Y-Y'\|_F), (d=\|Z-Z'\|_F), and (q=\|\alpha-\alpha'\|),

\[
 c h^4+\lambda q^2
 \le \langle v(Z)-v(Z'),Y-Y'\rangle
 \le C_M d h,
\]

and therefore only (h\le C d^{1/3}).  The missing gain must use the conserved second-column equation (k(Y)=k(Z)) and the fact that the first-column equation can nearly cancel (\Delta v(Y)) against (\lambda\Delta\alpha).  Any proof that treats the two columns independently will lose the (7/3) balance.

## 4. Concrete proof obligations

The following are the smallest obligations that would turn Candidate A into a theorem.

1. **Output boundedness.** On (|Z\|,\|Z'\|\le M), prove a uniform bound on (|Y\|,|Y'\|) from the coercive equations (already available in C270 in a weaker form).

2. **Conserved-cross-coordinate estimate.** Set (r=\|\beta-\beta'\|), (q=\|\alpha-\alpha'\|).  From (k(Y)=k(Z)) and the cubic monotonicity of (\beta\mapsto\|\beta\|^2\beta), prove a dichotomy of the form
   \[
   r\lesssim q^{1/3}
   \quad\text{or}\quad
   r\lesssim \frac{d}{\rho^2},
   \]
   where (\rho\) is the larger singular/radial scale of the two input columns.  The first branch is the cubic regime; the second is the linearized regime away from the zero stratum.

3. **Scale coupling.** Show that when (\rho\) is small, the first-column equation forces (q\lesssim h^3) and (\rho\lesssim h^{1/3}) in the only regime where the two-column difference can be worst.  Combining (r\lesssim d/\rho^2) with (\rho\lesssim h^{1/3}) gives (d\gtrsim h^{7/3}).  If (\rho\gtrsim h^{1/3}), use the first branch and the equation for (u) to obtain the same lower bound.

4. **Rank-stratum reduction.** The singular locus of (Dv) consists of rank-deficient matrices.  A proof should stratify into (a) a uniformly nondegenerate stratum, where (T_\lambda) is Lipschitz, (b) rank-one strata, reducible by an orthogonal change of coordinates to the collinear equations above plus transverse perturbations, and (c) the origin.  The transverse terms are nonnegative in the quartic monotonicity identity and should not worsen the (3/7) exponent.

5. **Sharpness after extension.** The collinear witness above lies in every (m\ge2) by embedding (c\) in one coordinate, so a proof of the upper bound would immediately give exactness for the full matrix problem.

An alternative route is a semialgebraic Łojasiewicz proof for the polynomial graph defined by (A1)–(A2), with a Newton polygon at the origin.  The only candidate critical arc has weights \\(\operatorname{wt}(a)=1,\operatorname{wt}(b)=7,\operatorname{wt}(\alpha)=\operatorname{wt}(\beta)=3\\), yielding (7/3) in (A3).  This route must still rule out transverse arcs with a smaller quotient.

## 5. Objections and status

* The (3/7) upper bound is not proved here.  A numerical fit or a finite arc search would be evidence only, not a theorem.
* Existing C273 changes the data to a nonzero target and obtains a different pointwise (2/3) exponent; it does not close C270 because the zero set and kernel center differ.
* The same algorithm has a classical full-domain finite-length proof, so the value of Candidate A is an exact regularity theorem for the complete physical prox, not a claim that the algorithm is classically inaccessible.
* External priority is unverified.  Before upgrading the status, search for Hölder regularity/Łojasiewicz exponents of inverses of cubic Gram maps with a one-column linear perturbation, and compare exact statements rather than titles.

## 6. Minimal next experiment

Symbolically eliminate (U,W) in the collinear slice and derive a two-regime inequality uniform in (t,s):
\[
 |\beta(t,s)-\beta(t,0)|\le C\,(t|s|)^{3/7}
\]
for (t,|s|\le1), then lift the estimate to rank-one matrix strata.  A failure on a transverse rank-two arc would falsify Candidate A and identify the true exponent.

