# Discovery B: monotonicity is a structural anti-winding gate for C287

## Candidate status

This is a **candidate structural lemma / open extension**, not a major-contribution claim. It gives a concrete obstruction to importing the C287-v2 non-Dini winding mechanism into the monotone, maximal-monotone, or convex-subdifferential PPA classes. The derivation below is self-contained from the monotonicity inequality; no numerical experiment is being promoted to a theorem.

## Exact object and proposed claim

Fix (0<q<1), (R>0), and write points in the annulus (A_R={(1+t)p:p\in\mathbb S^1, 0\le t\le R}). Consider the radial-twist proximal candidate
\[
J((1+t)p)=(1+qt)R_{\theta(t)}p, \qquad p\in\mathbb S^1,
\]
where (R_{\theta(t)}) is planar rotation and (\theta(0)=0). Suppose there is a monotone relation (F\) (not yet assumed maximal) and a step \(\lambda>0\) such that, for every (x\in A_R),
\[
Jx\in J_{\lambda F}(x),\qquad
(Jx,(x-Jx)/\lambda)\in\operatorname{gph}F.
\]
The exact local claim is:

> **B1 (firm-angle obstruction).** For every (t\in[0,R]),
> \[
> \cos\theta(t)\ \ge\ \frac{1+qt}{1+t}.
> \]
> Consequently, with the principal angle ( |\theta(t)|\le\pi\),
> \[
> 1-\cos\theta(t)\le \frac{(1-q)t}{1+t},
> \qquad
> |\theta(t)|\le \frac{\pi}{\sqrt2}\sqrt{\frac{(1-q)t}{1+t}}.
> \]
> In particular, if (t_k=q^k t_0), then
> \[
> \sum_{k\ge0}|\theta(t_k)|
> \le \frac{\pi}{\sqrt2}\sqrt{1-q}\,\frac{\sqrt{t_0}}{1-\sqrt q}<\infty.
> \]

For the C287 radial twist, (t_k=q^k t_0) is exactly the normal-distance recurrence. Hence B1 implies finite total angular variation and point convergence of every nonzero orbit in this ansatz; its dense-circle, infinite-length mechanism cannot coexist with monotonicity.

## Proof of B1

Take two points at the same radius, (x=(1+t)p) and (x'=(1+t)p'), with (p,p'\in\mathbb S^1). Put (r=1+t), (s=1+qt), and (u=p-p'\). The two graph points of (F) are
\[
(y,v)=\bigl(sR_{\theta(t)}p,(x-y)/\lambda\bigr),
\quad
(y',v')=\bigl(sR_{\theta(t)}p',(x'-y')/\lambda\bigr).
\]
Monotonicity gives
\[
0\le\langle y-y',v-v'\rangle
 =\lambda^{-1}\bigl(\langle y-y',x-x'\rangle-\|y-y'\|^2\bigr).
\]
Since (y-y'=sR_{\theta(t)}u) and (x-x'=ru),
\[
\langle y-y',x-x'\rangle=rs\cos\theta(t)\,\|u\|^2,
\qquad
\|y-y'\|^2=s^2\|u\|^2.
\]
For (p\ne p'), division by (s\|u\|^2>0) yields (r\cos\theta(t)\ge s), which is B1.

For (z\in[-\pi,\pi]), (1-\cos z=2\sin^2(|z|/2)\ge 2z^2/\pi^2). Applying this to B1 gives the displayed square-root bound and the geometric-series estimate.

## Direct attack on C287-v2

C287-v2 uses, for small (t),
\[
 b(t)=\frac{\omega(t)-Kt}{4},\qquad
 \theta(t)=2\arctan b(t),
\]
with (K=20), and (omega) continuous, nondecreasing, concave, (omega(0)=0), and
\(
\int_0\omega(t)\,dt/t=\infty
\).
Because (\omega(t)/t\to\infty), (b(t)\sim\omega(t)/4) and (\theta(t)\sim\omega(t)/2) along the shrinking window. Any function obeying (\omega(t)\le C\sqrt t) near zero has finite Dini integral, since
\[
\int_0^\varepsilon\frac{\omega(t)}t\,dt
\le C\int_0^\varepsilon t^{-1/2}\,dt<\infty.
\]
Therefore a non-Dini (omega) cannot satisfy the B1 square-root angle gate in the C287 profile. More explicitly, for the standard example \(\omega(t)=1/\log(e/t)\) (on a sufficiently small interval), \(\theta(t)/\sqrt t\to\infty\), while B1 forces this ratio to stay bounded. Thus the C287 relation is necessarily nonmonotone on every sufficiently small annular window. This is a genuine obstruction, not a failure of the C287 construction itself: C287 deliberately does not assume monotonicity.

## What this could become

A plausible sharpened theorem is:

1. **Radial-twist monotone theorem.** Under B1 and the exact radial contraction (d(Jx,\mathbb S^1)=q,d(x,\mathbb S^1)), every orbit in the annulus has finite length and converges to one point of \(\mathbb S^1\). The proof is the angular series above plus the radial increments (t_k-t_{k+1}=(1-q)t_k). This is a complete theorem for the displayed ansatz once the local graph inclusion is fixed.
2. **Monotone PPA extension (open).** Replace the rigid common-angle ansatz by a general monotone full graph with a (C^2) compact zero manifold and a uniform normal contraction. Determine whether the firm inequality gives a tangential displacement bound (O(\sqrt t)) in a tubular chart. If yes, it would rule out any non-Dini winding for the entire monotone class.
3. **Cyclically monotone / convex subdifferential strengthening (open but likely rigid).** In a smooth single-valued patch, cyclic monotonicity adds symmetry of the derivative and should eliminate the skew rotational component rather than merely forcing an (O(\sqrt t)) bound. This must be proved separately; it cannot be inferred from ordinary monotonicity.

## Fatal objections and scope boundaries

- B1 uses graph points at the **same radius** and therefore applies to the C287 common-angle radial twist. It does not by itself control a general nonradial map or a moving nearest-point frame on an arbitrary manifold.
- The hypothesis is local graph inclusion plus monotonicity. It does not prove full Minty coverage, maximality, a true residual EB, or a global RL estimate for a new model.
- The argument only gives a square-root angle bound. It does not prove that every monotone PPA has finite length under arbitrary geometric distance contraction; the tangent-chart extension is the main proof obligation.
- The conclusion is a structural obstruction/salvage result, not an external-priority claim. A literature search is still needed before calling the resulting monotone-class theorem novel.

## Minimal reproducible algebra check

For (q=1/2), (t=10^{-4}), B1 gives (\cos\theta\ge(1+5\cdot10^{-5})/(1+10^{-4})\approx0.99995), hence \(|\theta|\lesssim10^{-2}). A C287 choice \(\omega(t)=1/\log(e/t)\) has \(\omega(10^{-4})\approx0.105) and (\theta\approx0.052), already above the square-root gate; the asymptotic ratio diverges as (t\downarrow0).

## Recommended next mathematical task

Ask an independent reviewer to attack the annular monotone theorem in a full graph setting: check whether comparing same-radius points is legitimate when (J_{\lambda F}) is multivalued, whether maximal monotonicity adds hidden branches, and whether the tangent-frame version can be proved with only a (C^2) tubular chart. If it survives, construct a monotone radial PPA with the sharp (\sqrt t) angle rate to test the exponent, then compare against C287-v2's non-Dini obstruction.
