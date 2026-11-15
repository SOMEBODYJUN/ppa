# Falsification audit: the generalized FNE tubular candidate

## Candidate under review

Let (Ssubsetmathbb R^n) be a compact (C^2) embedded boundaryless submanifold, let (U_ho={x:d(x,S)<ho}) be a tubular neighborhood, and let (J:U_ho	o U_ho) be single-valued and firmly nonexpansive. Assume

\[
Jp=pquad(pin S),
\qquad d(Jx,S)le q,d(x,S),quad 0<q<1.
\tag{F0}
\]

The proposed geometric conclusion introduces (p=P_Sx), (z=Jx), (q'=P_Sz), (m=z-q'), and (a=q'-p), then seeks a (C^2) chord estimate yielding (|a|=O(\sqrt q,d(x,S))), followed by finite length and convergence.

## 1. The core conclusion is an immediate Hilbert-space inequality

Firm nonexpansiveness and the fixed graph point (p) give
\[
\|z-p\|^2\le \langle z-p,x-p\rangle.
\tag{F1}
\]
Writing (x-p=n) with (|n|=t=d(x,S)), Cauchy–Schwarz gives
\[
\|z-p\|\le t.
\tag{F2}
\]
The standard Hilbert identity strengthens this to
\[
\|z-p\|^2+\|x-z\|^2\le \|x-p\|^2=t^2.
\tag{F3}
\]
Consequently, for every iterate (x_{k+1}=Jx_k),
\[
\|x_{k+1}-x_k\|le d(x_k,S)=:t_k,
\qquad t_{k+1}le q,t_k.
\tag{F4}
\]
Therefore
\[
\sum_{k=0}^{\infty}\|x_{k+1}-x_k\|
\le \sum_{k=0}^{\infty}t_0q^k
=\frac{t_0}{1-q}<\infty.
\tag{F5}
\]
The iterates are Cauchy. Since (S) is closed and (t_k	o0), their limit belongs to (S). No (C^2) structure, positive reach, projection (P_Sz), or tangential chord estimate is used. The same proof works for any closed (S) and any map satisfying the pointwise fixed-point inequality (F3), even when (S) is highly nonsmooth.

This also shows that the proposed (O(\sqrt q,t)) bound for (a=q'-p) is not needed. A crude triangle estimate already gives (|a|\le\|z-p\|+\|m\|\le(1+q)t). If a sharper (C\sqrt q,t) coefficient is desired, it requires a separate geometric lemma and is irrelevant to the convergence claim.

## 2. Scope checks and actual failure modes

### Multivalued resolvents

If (J) is multivalued, the argument still applies to every legal step (z\in Jx) provided:

1. each graph pair ((x,z)) satisfies the fixed-point firm inequality (F1) for every (p\in S), equivalently the resolvent graph is firmly nonexpansive against the fixed graph points;
2. every allowed output obeys (d(z,S)\le qd(x,S));
3. the next input remains in the domain.

This is the natural graph formulation for a maximal monotone resolvent when (S\subset\operatorname{zer}F). It does **not** follow if only one selected branch is FNE or if the contraction is proved for one branch but the policy may choose another. A branchwise statement must therefore carry “all outputs” quantifiers.

### Projection of (z)

The point (q'=P_Sz) is only single-valued when (z) lies inside a positive-reach tube. Under the stated codomain (J:U_\rho\to U_\rho), this is available. If the codomain assumption is dropped, (d(z,S)\le qt) implies (z\in U_\rho) only when (qt<\rho); a theorem allowing (t\ge\rho/q) cannot use a unique projection. This is a domain/quantifier issue, not an FNE obstruction.

### What fails without the contraction gate

Firm nonexpansiveness alone gives Fejér monotonicity and asymptotic regularity, but no geometric rate (t_{k+1}\le qt_k). The finite-length estimate (F5) then disappears. In infinite-dimensional Hilbert spaces a firmly nonexpansive map with fixed points may have Picard iterates that converge only weakly; in a local/nonclosed domain even existence of a limit can require additional assumptions. Thus (q<1) is the substantive gate in this candidate.

### What fails if fixed points are not in the map's domain

Using (F1) requires the comparison point (p\in S) to be a fixed graph point. If (Jp) is undefined, or (p\) is merely a limit point of approximate fixed points, no such inequality follows. Replacing (Jp=p) by (d(Jp,S)=0) changes the claim and can permit tangential drift.

## 3. Literature priority check

The open-access paper by Bërdëllima, Lauster, and Luke, “\(\alpha\)-Firmly nonexpansive operators on metric spaces,” *J. Fixed Point Theory Appl.* 24 (2022), Article 14, gives the relevant pointwise fixed-point inequality as Proposition 4(ii): for a pointwise firmly nonexpansive mapping at a fixed point (p),
\[
d(Tx,p)^2\le d(x,p)^2-c\,d(Tx,x)^2
\]
in a (2)-uniformly convex setting; their Theorems 27 and 30 derive convergence and quantitative rates under fixed-point regularity/error bounds.  In a Hilbert space (c=2), this is exactly (F3) (up to the parameter convention).  The proposed tubular theorem is therefore an elementary local corollary once the additional normal contraction (t_{k+1}\le qt_k) is assumed.

This source does not itself state the exact (C^2)-manifold formulation (F0), but it removes any novelty claim based on the firmness-to-finite-length mechanism. The manifold chord estimate would only be a geometric embellishment. A priority claim would require a genuinely new setting, such as a non-Hilbert metric where the fixed-point inequality has curvature error, or a contraction condition inferred from a natural operator rather than assumed.

## 4. Verdict

**淘汰 as a major-contribution candidate.** Under the exact stated assumptions, (F3)–(F5) prove the desired convergence and finite length without the proposed (C^2) machinery. The result is useful as a clean scope lemma for later work, especially to record the all-output quantifiers for multivalued resolvents, but it cannot support a top-journal main theorem by itself. To obtain a nontrivial problem, remove or derive the distance contraction from a natural PPA/GPPA hypothesis, or move to an almost-firm/curved metric setting where a residual error must be controlled.

