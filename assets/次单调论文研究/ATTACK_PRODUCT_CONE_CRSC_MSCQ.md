# Product-cone upgrade: CRSC, nonlinear facial reduction, and amenable-cone MSCQ

Date: 2026-09-09. Status: MATHEMATICAL AUDIT PASS; main theorem and explicit counterexample frozen; worldwide priority not certified. Independent audit: output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md.

## 1. Target and outcome

The hard-stop target was a genuine product-cone/high-dimensional-face result, or an explicit obstruction. A stronger unified candidate has emerged:

1. For every finite-dimensional **nice** proper cone, minimal-face CRSC automatically supplies the two nearby stability conditions A1/A2 and nonlinear facial reduction.
2. For every **amenable** proper cone, minimal-face CRSC implies MSCQ for arbitrary C1 nonlinear data.
3. This includes finite products of smooth strictly convex cones and all positive-semidefinite cones. The proof never assumes blockwise MSCQ.

The new step is a rank sandwich on two fixed dual-face subspaces, followed by normal correction on a common manifold. Pataki's closed-image criterion, amenability, and the constant-rank theorem are established tools. Their exact implication for this CRSC hypothesis is the claim to audit.

## 2. Exact frozen setup

Let X and E be finite-dimensional Euclidean spaces. Let C be a closed pointed full-dimensional convex cone. Let G:V→E be C1 on an open neighborhood V of a feasible reference xbar, with G(xbar)=0. Put
\[
\Omega=G^{-1}(C),\quad A=DG(\bar x),\quad
F=F_{\min}(\operatorname{Im}A\cap C),\quad
H=F^\perp,\quad S=\operatorname{span}F^\triangle,
\]
where the positive dual and conjugate face are
\[
C^*=\{y:\langle y,c\rangle\ge0\ (\forall c\in C)\},
\qquad F^\triangle=C^*\cap F^\perp.
\]
Minimal-face CRSC means:
\[
A^*C^*\ \hbox{is closed},\qquad
\operatorname{rank}(DG(x)^*|_H)=r
:=\operatorname{rank}(A^*|_H)
\]
for every x in one neighborhood of xbar. Polar signs do not change closedness or rank. The face F and the reduction G are frozen at xbar.

For an original constraint g(x)∈K at a nonapex point, this theorem is applied to its fixed local reduction G=Xi∘g with reduced cone C. A local Lipschitz constant of Xi transfers the final residual estimate back to d(g(x),K). All statements concern the same original feasible set locally.

If the reduced ambient space is zero-dimensional, G and C are both the zero object: local equivalence makes every sufficiently near input feasible. This is a separate trivial branch, with arbitrary positive error-bound constant; no normalized direction, smallest positive singular value, or relative-boundary distance is invoked.

A cone is **nice** if C*+Jperp is closed for every face J. It is **amenable** if every face J admits a finite a_J with
\[
d(y,J)\le a_Jd(y,C)\qquad(y\in\operatorname{span}J).
\tag{A}
\]
Amenability implies niceness. Strictly convex cones, symmetric cones, polyhedral cones, and finite products of amenable cones are amenable; these are existing results of [Lourenço, Definition 8, Propositions 9, 11, 13 and 33](https://optimization-online.org/wp-content/uploads/2017/11/6348.pdf).

## 3. The imported closed-image theorem and the missing rank sandwich

For a nice C, Pataki's criterion gives, for the minimal face F above,
\[
A^*C^*\ \hbox{closed}
\Longleftrightarrow
\begin{cases}
\ker A^*\cap\operatorname{ri}F^\triangle\ne\varnothing,\\
\operatorname{Im}A\cap S^\perp
=\operatorname{Im}A\cap\operatorname{span}F,
\end{cases}
\tag{P}
\]
and equivalently
\[
A^*F^\triangle=A^*H.
\tag{P'}
\]
The displayed form is reproduced as Theorem 5.1 in the [author-hosted minimal-face CRSC paper](https://www.ime.usp.br/~ghaeser/crsc-redcones.pdf), explicitly attributed to Pataki, Theorem 1. We use its hypotheses, including niceness.

### Lemma 3.1 — Rank sandwich

Under CRSC and niceness, on one neighborhood,
\[
\operatorname{rank}(DG(x)^*|_S)
=\operatorname{rank}(DG(x)^*|_H)=r.
\tag{3.1}
\]

**Proof.** Since S⊂H, the left rank is at most r by CRSC. At xbar, (P') makes it exactly r. A nonzero r×r minor persists by continuity, giving the reverse inequality nearby. For r=0 both ranks are zero. ∎

This elementary sandwich is the point that replaces the extra A1/A2 hypotheses in the published facial-reduction proof. It must be audited independently before claiming the open removal is settled.

### Lemma 3.2 — Continuous kernel projections

If a continuous matrix field B(x) has constant rank near xbar, its orthogonal kernel projection is continuous. This follows by fixing a nonzero maximal minor and solving the kernel in a continuous local graph chart; equivalently its Moore–Penrose inverse is continuous on a fixed-rank stratum. We only use continuity, not differentiability.

## 4. Nice cones: full-neighborhood stability and facial reduction

### Theorem 4.1 — A1/A2 are automatic for nice cones

Under Section 2 and niceness, there is one open neighborhood on which
\[
DG(x)^*C^*\ \hbox{is closed},\qquad
F_{\min}(\operatorname{Im}DG(x)\cap C)=F.
\tag{4.1}
\]

**Proof.** First handle F=C: a vector Adbar∈int C exists by the definition of the minimal face; it persists, giving both statements by strict feasibility and bounded dual lifts.

Assume F is proper. By (P), choose
\(Y_0\in\operatorname{ri}F^\triangle\cap\ker A^*\).
The face Ftriangle is nonzero because nice cones are facially exposed. Let B(x)=DG(x)* restricted to S. Lemma 3.1 fixes its rank. Project Y0 onto ker B(x) inside S. The resulting Y(x) is continuous, equals Y0 at xbar, and remains in ri Ftriangle. Hence
\[
DG(x)^*Y(x)=0.
\]
For any v∈Im DG(x)∩C, its pairing with Y(x) vanishes. As Y(x) is in the relative interior of the conjugate face and C is facially exposed, this forces v∈F.

If F={0}, this already shows the minimal face is F. Otherwise choose dbar such that Adbar∈ri F; existence follows by summing finitely many elements of Im A∩C whose minimal containing face is F. Put B_H(x)=P_HDG(x), which has constant rank by CRSC. Orthogonally project dbar onto ker B_H(x). The projected d(x) converges to dbar because P_HAdbar=0. Therefore
\[
DG(x)d(x)\in\operatorname{span}F,\qquad
DG(x)d(x)\to Adbar\in\operatorname{ri}F.
\]
It belongs to ri F nearby. Thus the minimal face is exactly F.

Finally Lemma 3.1 and the inclusion of kernels give
\[
\ker(P_SDG(x))=\ker(P_HDG(x)).
\]
Equivalently,
\[
\operatorname{Im}DG(x)\cap S^\perp
=\operatorname{Im}DG(x)\cap\operatorname{span}F.
\]
Together with Y(x), criterion (P), now using the just-proved minimal face F at x, yields closedness. ∎

### Lemma 4.2 — Positive normal angle

Set
\[
U=\operatorname{Im}(P_HA),\qquad
D=\overline{P_HC}\subset H.
\]
Then U∩D={0}.

**Proof.** If u=P_HAd∈D, then \(\langle u,y\rangle\ge0\) for every y∈Ftriangle, by projection and continuity. For any h∈H, (P') provides y∈Ftriangle with A*y=A*h. Therefore
\[
\langle u,h\rangle=\langle Ad,h\rangle
=\langle Ad,y\rangle=\langle u,y\rangle\ge0.
\]
This holds also for −h. Thus u is orthogonal to H while belonging to H, and u=0. ∎

The closure in D is essential: projected nonpolyhedral cones can be nonclosed. The proof controls that closure, so a missing-limit-direction defect is not being ignored.

### Lemma 4.3 — Quantitative correction to the common face manifold

Put
\[
\phi=P_HG,\qquad M=\{x:\phi(x)=0\}.
\]
Under CRSC and niceness, every sufficiently near x admits xhat∈M with
\[
\|x-\widehat x\|\le b\,d(G(x),C).
\tag{4.2}
\]
If r>0, a valid bound is
\[
b=\frac4{\sigma\eta},\qquad
\sigma=\sigma_{\min}^+(P_HA),\quad
\eta=\min_{\substack{u\in U\\\|u\|=1}}d(u,D)>0.
\tag{4.3}
\]
If r=0, take b=0 and xhat=x.

**Proof.** The rank of Dphi is r by CRSC. For r>0, Lemma 4.2 gives the positive compact-sphere angle η. Apply the constant-rank/angle construction explicitly: with N=ker Dphi(xbar), use
\[
\Theta(x)=(P_U\phi(x),P_N(x-\bar x)).
\]
Its derivative is invertible. In local product inverse coordinates x=θ(u,z), constant rank gives
\[
\phi(\theta(u,z))=u+\beta(u),\quad
\beta(u)\in U^\perp\cap H,\quad
\beta(0)=D\beta(0)=0.
\]
Shrink so that \(\|D_u\theta\|\le2/\sigma\) and \(\|D\beta\|\le\eta/2\). Then
\[
d(\phi(x),D)\ge(\eta/2)\|u\|,
\quad
\widehat x=\theta(0,z),\quad
\|x-\widehat x\|\le2\|u\|/\sigma.
\]
Since projection is nonexpansive and D contains P_H C,
\[
d(\phi(x),D)\le d(G(x),C),
\]
proving (4.2). If r=0, phi is locally constant at zero. ∎

### Corollary 4.4 — Nonlinear facial reduction without A1/A2

For nice cones under CRSC,
\[
G^{-1}(C)=G^{-1}(F)\quad\hbox{locally at }\bar x.
\tag{4.4}
\]

Indeed, feasible points have d(phi,D)=0. The angle/coordinate argument forces u=0, so phi=0; hence G(x)∈C∩span F=F. The opposite inclusion is immediate. This proof is independent of the published proposition's use of A1/A2, although Theorem 4.1 also supplies them.

## 5. Amenable cones: the joint nonlinear MSCQ theorem

### Lemma 5.1 — Relative interior correction on M

If F≠{0}, select a unit d0∈ker Dphi(xbar) with
\[
v_0=Ad_0\in\operatorname{ri}F,\qquad
\tau_F=d_{\operatorname{span}F}(v_0,\operatorname{rbd}F)>0.
\]
There is a neighborhood in M where every xhat admits xplus∈M with G(xplus)∈F and
\[
\|x^+-\widehat x\|\le c\,d(G(\widehat x),F),
\qquad c=\frac4{\tau_F}.
\tag{5.1}
\]

**Proof.** In the constant-rank chart M={θ(0,z)}, choose a fixed coordinate direction w0 with D_zθ(0,zbar)w0=d0. Along z+t w0, G takes values in span F. Shrink the chart so that its G-directional derivative differs from v0 by at most τF/4, while the input-directional derivative has norm at most 2. For rF=d(G(xhat),F), put t=2rF/τF. Using a closest point of F, the usual cone-ball correction gives an endpoint in F: its perturbation norm is at most rF+tτF/4<tτF. Input path length is at most 2t=4rF/τF. All paths stay in the chart after nesting neighborhoods. ∎

### Theorem 5.2 — CRSC implies MSCQ for amenable cones

Let C be amenable and satisfy the proper-cone assumptions of Section 2. Let G be C1 on an open neighborhood of xbar with G(xbar)=0 and satisfy frozen minimal-face CRSC. Then
\[
d(x,\Omega)\le\kappa\,d(G(x),C)
\tag{5.2}
\]
locally. For F={0}, κ=b is valid when b>0; the trivial locally feasible case admits any positive κ. For F≠{0}, let a_F be an amenability constant, b as in (4.3), L_G a local Lipschitz bound for G, and c=4/τF. One valid upper bound is
\[
\boxed{\kappa=b+c\,a_F(1+L_Gb).}
\tag{5.3}
\]
These constants are effective local upper bounds, not optimal moduli or a numerically fixed radius.

**Proof.** Amenability implies niceness, so Lemma 4.3 supplies xhat∈M and
\(\|x-\widehat x\|\le b r\), r=d(G(x),C).
Since G(xhat)∈span F,
\[
d(G(\widehat x),F)
\le a_Fd(G(\widehat x),C)
\le a_F(1+L_Gb)r.
\]
If F={0}, xhat is already feasible. Otherwise apply Lemma 5.1 on M and add the two correction lengths. This yields (5.3). ∎

For a locally equivalent original reduction G=Xi∘g, a local Lipschitz constant LXi gives
\(d(G(x),C)\le LXi\,d(g(x),K)\).
Thus κLXi is an original MSCQ constant. Local projection continuity keeps the closest K-point in the reduction neighborhood.

## 6. Why this genuinely covers products and higher-dimensional faces

### 6.1 Finite products of smooth strictly convex cones

Let C=Π_i C_i. Every face is F=Π_i F_i. If a_i is an amenability constant of F_i, orthogonal product distances give
\[
d(y,F)^2=\sum_i d(y_i,F_i)^2
\le(\max_i a_i)^2\sum_i d(y_i,C_i)^2
\]
for y∈span F. Hence a_F=max_i a_i.

For a smooth strictly convex factor, its zero and full faces are immediate. If F_i=R+v_i with unit v_i, take
\(a_i=1/d(-v_i,C_i)\).
Thus all finite p-cone products are covered, including mixtures of different exponents, scalar inequality blocks, and apex/nonapex blocks after the frozen reduction.

This product calculation concerns **output-cone amenability**, not blockwise input error bounds. The input map G may couple all variables across all blocks; the single joint normal map P_HG, its rank, its angle, and its common manifold are used before correcting the entire F. No intersection regularity is silently assumed.

### 6.2 Positive-semidefinite cones

For C=S+^m, any face has the form F={URU*:R∈S+^k}, with U having orthonormal columns. A vector in span F is UBU* with B symmetric. Its projection onto S+^m is U B+ U*, which already lies in F. Therefore
\[
d(Y,F)=d(Y,S_+^m)\qquad(Y\in\operatorname{span}F),
\]
so a_F=1. Theorem 5.2 covers arbitrary-rank faces, including high-dimensional nonpolyhedral proper faces. The nonapex standard Schur-complement reduction returns a smaller PSD cone and is locally smooth.

### 6.3 A coupled two-SOC nonlinear model

Let v=(1,1,0), n=(1,−1,0), e=(0,0,1), h(s,t,u)=u−st, and define
\[
G_1=sv+hn+h^2e,\qquad
G_2=tv-hn+2h^2e,\qquad C=Q_3\times Q_3.
\]
At the origin the joint derivative image meets C exactly in
\(F=\mathbb R_+v\times\mathbb R_+v\), a two-dimensional proper face. The projected joint normal map is a vector function of h alone whose derivative with respect to h never vanishes. Consequently the required minimal-face normal rank is one on a whole neighborhood. Moreover \(A^*F^\triangle=A^*F^\perp=\mathbb R(0,0,1)\), so the exact joint adjoint cone image is closed by Pataki.

The first SOC block forces h≥0, and the second forces h≤0. Hence the complete nonlinear feasible set is
\[
\Omega=\{(s,t,u):s\ge0,\ t\ge0,\ u=st\}.
\]
This is a curved, nonisolated common feasible set. Each block separately has a strict derivative direction, while the joint system has none. The proof of the theorem acts on the common equation h=0 and then on the joint face. It does not infer intersection regularity from separate block regularity.

### 6.4 A PSD example with arbitrarily large nonpolyhedral proper face

Let k≥2, let B∈S^k and u∈R be the inputs, and set h=u−tr(B²). Fix k×2 matrices C0,D0, at least one nonzero. Define
\[
G(B,u)=
\begin{pmatrix}
B & hC_0+h^2D_0\\
hC_0^T+h^2D_0^T & h\,\operatorname{diag}(1,-1)
\end{pmatrix}\in S^{k+2}.
\tag{6.1}
\]
At (0,0), the minimal linearized face is
\[
F=\left\{\begin{pmatrix}B&0\\0&0\end{pmatrix}:B\succeq0\right\},
\]
whose dimension is k(k+1)/2 and which is nonpolyhedral. The adjoint image of its conjugate PSD face is the entire u-axis: the lower diagonal positive-semidefinite multipliers generate both signs of the scalar h derivative. The full normal adjoint image is the same axis. Hence the joint cone image is closed.

The normal output depends only on h, and its h derivative is always nonzero because its lower diagonal block is diag(1,−1). Since Dh/du=1, the required normal rank stays exactly one. Thus CRSC holds.

For every input, positive semidefiniteness of the lower principal block forces h=0. Conversely, when h=0 all cross terms vanish. Therefore
\[
G(B,u)\succeq0
\Longleftrightarrow B\succeq0,\quad u=\operatorname{tr}(B^2).
\]
Theorem 5.2 supplies MSCQ for this nonlinear representation. This example demonstrates high-dimensional nonpolyhedral faces and coupled nonlinear normal components; it does not claim that no elementary direct analysis can solve the example.


## 7. Sharp boundary of the route: why facewise residual transfer matters

Niceness supplies rank/closure geometry, but Theorem 5.2 uses amenability in exactly one line: converting the cone residual to the face residual once G lies in span F.

There is a conditional necessity statement independent of any claim about whether particular nonamenable nice cones have been constructed:

For a nice cone C, if every linear inclusion \(G:\operatorname{span}F\hookrightarrow E\), at zero and for every face F, satisfies MSCQ under CRSC, then C is amenable.

Indeed, for that G, minimal face is F, P_HDG=0 has constant rank, and niceness gives closed G*C*. MSCQ is exactly d(y,F)≤κd(y,C) near zero in span F. Cone homogeneity extends it globally. Thus blanket MSCQ for all CRSC maps over a fixed nice cone necessarily contains amenability.

Consequently, for a proper nice cone C, the following candidate equivalence follows from Theorem 5.2:
\[
\boxed{C\text{ amenable}
\Longleftrightarrow
\text{every C1 map satisfying frozen CRSC at an apex has MSCQ}.}
\tag{7.1}
\]
The right side may be restricted to linear face inclusions for the reverse implication. The next subsection instantiates the obstruction with a checked published cone.

### 7.2 An explicit full-CRCQ counterexample outside amenability

The needed nice-but-nonamenable cone is already available in [Lourenço–Roshchina–Saunderson, Section 5, Proposition 5.1, SIAM Journal on Optimization 32(3), 2022](https://bflourenco.github.io/papers/amenable_nice.pdf). Use their curves
\[
\alpha(t)=(\cos t,\sin t,1),\quad
\beta(t)=(\cos t,\sin t,-1),\quad 0\le t\le2\pi,
\]
\[
\gamma(t)=\left(2\cos(2t)-1,\ 2\sin(2t),\
\frac98\cos t-\frac18\cos(3t)\right),\quad 0\le t\le\pi,
\]
and set
\[
B=\operatorname{conv}(\alpha\cup\beta\cup\gamma),\qquad
K=\operatorname{cone}(B\times\{1\})\subset\mathbb R^4.
\]
The cited proposition proves K nice. It is pointed, closed and full-dimensional. Its exposed face
\[
J=\{(a,b,s,s):s\ge\sqrt{a^2+b^2}\}
\]
is the cone over the upper disk face of B. The source cone and its niceness are imported, not newly invented.

Let X=R3 with its Euclidean norm and define the linear isometry
\[
G(a,b,c)=(a,b,c/\sqrt2,c/\sqrt2).
\tag{7.2}
\]
Its range is span J. Thus its minimal face is J, and **all** face-rank tests are constant on the entire input space because DG is constant. Niceness of K gives closed G*K*: indeed, closedness of P_spanJ K* is equivalent to closedness of K*+Jperp. Therefore the exact full facial CRCQ, not merely CRSC, holds at the apex.

Here is a direct residual witness, independently adapted to the apex. Put
\[
a(t)=2\cos(2t)-1,\quad b(t)=2\sin(2t),\quad
r(t)=\sqrt{a(t)^2+b(t)^2}=\sqrt{5-4\cos(2t)},
\]
\[
u(t)=t(a(t),b(t),\sqrt2)\longrightarrow0.
\]
The output is \(G(u(t))=t(a(t),b(t),1,1)\). Since \((\gamma(t),1)\in K\),
\[
d(G(u(t)),K)
\le t\left(1-\frac98\cos t+\frac18\cos(3t)\right)
=\frac38t^5+O(t^7).
\tag{7.3}
\]
Because G is isometric and K∩span J=J,
\[
d(u(t),G^{-1}(K))
=d(G(u(t)),J).
\]
For small positive t, r(t)>1. Projection onto J reduces to minimizing
\((r(t)-s)^2+2(1-s)^2\), whose minimizer is \(s=(r(t)+2)/3\). Hence
\[
d(u(t),G^{-1}(K))
=t\sqrt{\frac23}(r(t)-1)
=4\sqrt{\frac23}\,t^3+O(t^5).
\tag{7.4}
\]
The quotient of the input distance by the cone residual diverges at least as a positive multiple of t^{-2}. Thus MSCQ fails at zero while full facial CRCQ holds.

This supplies an actual negative answer to an unrestricted nice/nonpolyhedral CRCQ→MSCQ assertion, while leaving the amenable-cone positive theorem intact. The cone and the underlying tangency phenomenon are established prior work; the exact CRCQ representation, apex scaling, and implication boundary must be audited for prior use before a novelty claim.


## 8. Novelty audit and claim boundaries

The minimal-face paper's author-hosted Theorem 5.2 imposes A1/A2 and explicitly leaves their removal open. Theorem 4.1 targets that exact removal for nice cones, rather than adding either assumption back.

Lourenço's amenable-cone machinery primarily treats affine conic feasibility and establishes the facial residual property; Theorem 5.2 here uses a nonlinear common-manifold correction controlled by CRSC. Its amenability concept, product calculus, symmetric-cone constants, and facial residual transfer are not new.

The known seq-CPLD separation is **not** a new contribution: the JOTA 2022 source already gives an example from which facial/sequential separation follows. Our parabola example is illustrative and nonisolated, not a first-separation claim.

Priority and theorem-level compatibility with all modern nonlinear cone-reduction/error-bound results remain to be checked. No journal acceptance level is certified. A correct general nice-cone removal plus amenable-cone MSCQ would be materially stronger than the earlier rank-one-face theorem; a flaw in (P') or in the common-manifold correction would invalidate that upgrade.

## 9. Audit checklist and hard-stop status

- [x] Verify Pataki (P') under exactly niceness and F=minimal face.
- [x] Attack the fixed-subspace rank sandwich.
- [x] Check the continuously projected strict exposing multiplier.
- [x] Verify U∩closure(P_H C)={0}, including high-dimensional faces.
- [x] Verify the two corrections concern the same joint input map.
- [x] Audit F=0, F=C, r=0 and nonapex reduction cases; zero-dimensional reduction stated separately.
- [x] Check necessity (7.1) against the precise nice/amenable definitions.
- [ ] Complete new-source priority audit.

Hard-stop outcome: the general proof and explicit counterexample passed independent mathematical review. This scope is now frozen; no further cone-class enlargement is included. Worldwide priority remains an independent gate.

The companion standard-library script output/verify_product_cone_crsc_mscq.py was executed successfully. It verifies the exact apex-path Taylor coefficients, the two-SOC and PSD4 normal/dual-face rank identities, and increasing certified distance-to-residual ratios on decreasing positive t. The script is an algebraic check, not a replacement for the general proofs.

## 10. Direct RL interface

For the constraint relation M(x)=G(x)−C, the theorem gives its native linear regularity gauge ψ_M(t)=κt. If the operator F used by RL has the same local zeros and an independently verified residual comparison d(G(x),C)≤χ(d(0,F(x))), then ψ_F=κχ. This keeps the RL and regularity verifications separate as requested. The theorem does not itself produce a genuine nonlinear RL exponent or a higher-order residual comparison.
