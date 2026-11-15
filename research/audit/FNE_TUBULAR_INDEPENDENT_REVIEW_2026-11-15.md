# Generalized FNE tubular theorem: independent attack and convex salvage

## Verdict

The proposed theorem is **vacuous for a positive-dimensional compact boundaryless \(C^2\) fixed manifold**, even when firm nonexpansiveness is assumed only on a tubular neighborhood. A global fixed-set convexity argument is insufficient for a local map, because a long chord can leave the tube; the correct local replacement is a short-chord lemma. Firmness plus the normal contraction forces every sufficiently short chord of \(S\) back into \(S\). A \(C^2\) manifold with this local chord property has zero second fundamental form and is locally affine, so a compact boundaryless positive-dimensional component cannot exist.

If “manifold” is allowed to have boundary and \(S\) is a compact convex body or convex segment, there is a valid salvage: the normal contraction directly gives an \(O(t)\) bound on the displacement of metric projections, and therefore finite length. This is a convex fixed-set lemma rather than a new curved-manifold mechanism.

## Exact assumptions

Let \(S\subset\mathbb R^n\) be compact \(C^2\) without boundary, let \(U_\rho=\{d(\cdot,S)<\rho\}\), and let \(J:U_\rho\to U_\rho\) be single-valued firmly nonexpansive,
\[
\|Jx-Jy\|^2\le \langle Jx-Jy,x-y\rangle \quad(x,y\in U_\rho).
\]
Assume \(Jp=p\) for every \(p\in S\), and \(d(Jx,S)\le q\,d(x,S)\) for all \(x\in U_\rho\), with \(0\le q<1\). The contraction itself forces every local fixed point to lie in \(S\).

## Fatal obstruction for curved fixed manifolds: local short chords

Firm nonexpansiveness implies nonexpansiveness. Fix \(p,q\in S\) with \(\|p-q\|<\rho\). The entire chord \(z_\tau=(1-\tau)p+\tau q\) lies in \(U_\rho\), because \(d(z_\tau,S)\le\min\{\tau,1-\tau\}\|p-q\|<\rho\). For \(0<\tau<1\),
\[
\|Jz_\tau-p\|\le\|z_\tau-p\|=\tau\|p-q\|,\qquad
\|Jz_\tau-q\|\le\|z_\tau-q\|=(1-\tau)\|p-q\|.
\]
The triangle inequality gives equality throughout, so \(Jz_\tau=z_\tau\). Applying the normal contraction at this fixed point gives
\[
d(z_\tau,S)=d(Jz_\tau,S)\le q\,d(z_\tau,S),
\]
and therefore \(z_\tau\in S\). Thus every sufficiently short chord of \(S\) lies in \(S\).

To see the geometric consequence, take a \(C^2\) curve \(\gamma\subset S\) with \(\gamma(0)=p\), \(\gamma'(0)=v\in T_pS\). The midpoint
\[
z_h=\frac{\gamma(h)+\gamma(-h)}2
=p+\frac12\gamma''(0)h^2+o(h^2)
\]
belongs to \(S\) for small \(h\). A \(C^2\) submanifold has normal displacement \(O(\|z_h-p\|^2)=O(h^4)\) from its tangent plane, so the normal component of \(\gamma''(0)\) must vanish. Hence the second fundamental form satisfies \(\mathrm{II}_p(v,v)=0\) for every \(p,v\), and polarization gives \(\mathrm{II}\equiv0\). Each positive-dimensional connected component is locally an affine subspace; a compact boundaryless affine component cannot exist. A zero-dimensional compact manifold is finite, so the only remaining local models are isolated fixed points (or, if boundary is allowed, convex pieces).

## Convex salvage: sharp elementary displacement estimate

If boundary is allowed and \(S\) is a nonempty closed convex set, there is a valid salvage (compactness is optional for the local estimate). For \(x\) near \(S\), let
\[
p=P_Sx,\quad t=\|x-p\|,\quad y=Jx,\quad p'=P_Sy,\quad t'=\|y-p'\|.
\]
Since \(p\in\operatorname{Fix}J\), firm nonexpansiveness gives
\[
\|y-p\|^2\le \langle y-p,x-p\rangle.
\]
Write \(e=x-p\), \(a=p'-p\), \(n=y-p'\). The projection variational inequality gives \(\langle a,e\rangle\le0\), while \(\|n\|=t'\) and \(\|e\|=t\). Hence
\[
\|a+n\|^2=\|y-p\|^2
 \le \langle a+n,e\rangle
 \le \langle n,e\rangle
 \le tt'.
\]
By the triangle inequality,
\[
\|a\|\le \|a+n\|+\|n\|
\le \sqrt{tt'}+t'
\le (\sqrt q+q)t.
\tag{FNE-TANG}
\]
Thus the metric projection of the next point moves by \(O(t)\), uniformly in the point. The full step obeys
\[
\|Jx-x\|
\le t+\|p'-p\|+t'
\le (1+\sqrt q+2q)t.
\tag{FNE-STEP}
\]

For an orbit \(x_{k+1}=Jx_k\) with \(t_k=d(x_k,S)\), the hypothesis gives \(t_k\le q^kt_0\), so
\[
\sum_{k\ge0}\|x_{k+1}-x_k\|
\le \frac{1+\sqrt q+2q}{1-q}\,t_0<\infty.
\]
The orbit is Cauchy and converges to \(x_\infty\in S\), because \(t_k\to0\) and \(S\) is closed. This proves a complete finite-length statement for the convex fixed-set class.

## Scope and next decision

- The curved \(C^2\) tubular extension is rejected at the object-definition level, before any second-order curvature estimate.
- The convex salvage is exact under the stated quantifiers and needs no \(C^2\) tubular projection; it is a reusable lemma, but its novelty is unverified and likely classical.
- To obtain a nontrivial compact curved fixed set, one must leave firm nonexpansiveness (for example, use a merely nonexpansive or general continuous resolvent-like map) and then reprove any \(O(t)\) tangential estimate from a different hypothesis.
- The normal-contraction assumption alone does not create a curved fixed manifold; the local chord obstruction is the decisive evidence.
