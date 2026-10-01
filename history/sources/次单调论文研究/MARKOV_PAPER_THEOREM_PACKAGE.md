# Identification and rate obstructions for invariant transport discrepancies

## Proof-bearing theorem package

Date: 2026-09-09. Task: `markov_paper_formalization`.

This is a mathematical extraction and consolidation, not a submission-ready manuscript or a priority certificate. All new mathematical statements below are **PROJECT_PROOF / AI_INFERENCE**: proofs are supplied, and the underlying constructions have independent project audits. Those labels do not mean external peer review. The source material is listed in Section 10. A targeted primary-text check of Pischke–Powell was added during consolidation; no new broad priority search is claimed.

The package has four logically separate conclusions:

1. Even random convex projections with one-step convergence need not have an invariant-identifying synchronous transport discrepancy.
2. On a fixed finite state space, exact zero identification is equivalent to a global linear EB. Tight-edge polytopes give a finite native identification test and the sharp coefficient.
3. In contrast, an infinite compact two-map example has exact zeros and uniform geometric convergence but no positive-Hölder EB and no gauge compatible with a specified almost-firm scalar contraction formula.
4. Compact exact-zero models still admit some general gauge. Conditional specifications provide a different, correlation-aware certificate in a stronger transport metric. A separate mass-dilution theorem explains why deterministic higher-order EBs do not automatically lift to full-law RMS bounds.

The results do **not** establish a new nonlinear-RL convergence theorem, necessity for every random proximal subclass, or that the paper already meets any journal's acceptance threshold.

### Claim ledger

| Result | Object and metric | Mathematical conclusion | Claim expressly excluded |
|---|---|---|---|
| Theorem 2 | Original synchronous discrepancy; ordinary joint \(W_2\) | Natural false zeros despite one-step convergence | Failure of subregularity to the discrepancy's own zero set |
| Theorem F | Same discrepancy on fixed finite states | Exact zeros iff global linear EB; finite native verifier and sharp coefficient | A uniform coefficient over changing systems or a polynomial-time guarantee |
| Theorem 4 | Same original discrepancy; ordinary \(W_2\) on a compact subset of \(\mathbb R\) | Exact zeros, global Q-contraction, no positive-Hölder EB | Absence of every general gauge |
| Corollary 5 | Fixed almost-firm parameters and a specified scalar formula | No locally strict contraction-compatible gauge | Impossibility of all other rate certificates |
| Theorem 1 | Compact continuous random-map setting | Exact zeros imply a general gauge without any convergence assumption | A computable or rate-compatible modulus |
| Theorems 6–7 | Conditional specification residual; fixed-marginal conditional transport | Sharp binary constants, exact nonuniform gauge/rates/length | Necessity or sharpness in ordinary joint \(W_2\) |
| Theorem 8 | Gaussian conditional residual; \(W_{2,Q}\) | Sharp EB constant \(\zeta^{-1/2}\), valid geometric factor | Priority or sharpness of the asserted contraction factor |
| Propositions 9–10 | Coupled-state information | A valid coupling identity and a conditional recoupling repair | Direct application of finite-dimensional T5 to a space of laws |
| Proposition M | Mixture-rich law neighborhoods and moment residuals | Necessary order \(q\le r/p\); RMS excludes \(q>1\) under explicit support/vanishing assumptions | An obstruction for all ergodic kernels or every residual |

## 1. Definitions, domains and quantifiers

Let \(G\) be a nonempty compact subset of \(\mathbb R^d\), with the inherited Euclidean distance. It need not be convex. Let \((\Xi,\mathcal F,\vartheta)\) be a probability space and let \((\xi,x)\mapsto T_\xi x\) be jointly measurable, with \(T_\xi:G\to G\) continuous for almost every \(\xi\). Fresh i.i.d. indices, independent of the current state, determine the actual updates. Write

\[
\mu P=\int (T_\xi)_\#\mu\,\vartheta(d\xi),\qquad
\mathcal I=\{\pi\in\mathscr P(G):\pi P=\pi\},
\qquad d(\mu)=\inf_{\pi\in\mathcal I}W_2(\mu,\pi).
\tag{1.1}
\]

Assume \(\mathcal I\ne\varnothing\). On compact \(G\), every probability law has finite second moment. Let \(\operatorname{Opt}(\mu,\pi)\) be the set of couplings minimizing the **full squared Euclidean transport cost**. Define

\[
c_R(x,y)=\mathbb E\bigl\|(x-T_\xi x)-(y-T_\xi y)\bigr\|^2,
\]
\[
\boxed{\Psi(\mu)^2=
\inf_{\pi\in\mathcal I}\;
\inf_{\eta\in\operatorname{Opt}(\mu,\pi)}
\int c_R(x,y)\,\eta(dx,dy).}
\tag{1.2}
\]

The same index \(\xi\) is used on both members of each input pair. The inner minimization is **not** over all couplings and **not** over separately sampled update noises. The residual (1.2) is not \(W_2(\mu,\mu P)\). We use the supplied source's Euclidean specialization throughout.

The expected almost-firm inequality with parameters \(0<\alpha<1\), \(\varepsilon_f\ge0\), and \(\tau=(1-\alpha)/\alpha\) is

\[
\mathbb E\|T_\xi x-T_\xi y\|^2+
\tau c_R(x,y)\le(1+\varepsilon_f)\|x-y\|^2.
\tag{1.3}
\]

Any local invocation of (1.3) must state its allowed state pairs. Our examples satisfy a global version, and Corollary 5 also treats complete state neighborhoods of the accumulation point.

A local invariant-set gauge bound at \(\bar\pi\in\mathcal I\) means: there exist \(r>0\) and a nondecreasing \(\rho\), with \(\rho(0)=0\), such that

\[
\forall\mu\in\mathscr P(G),\quad
W_2(\mu,\bar\pi)<r\ Longrightarrow\ d(\mu)\le\rho(\Psi(\mu)).
\tag{1.4}
\]

A positive-Hölder bound is (1.4) with \(\rho(s)=Ks^q\), \(K<\infty\), \(q>0\). The exponent is on the residual. A bound to \(Z_\Psi:=\Psi^{-1}(0)\), instead of to \(\mathcal I\), is a different assertion whenever \(Z_\Psi\ne\mathcal I\). A continuous, strictly increasing, unbounded function vanishing at zero will be called a **strict general gauge** when its inverse is needed.

The convergence quantifiers used below are:

\[
\begin{array}{ll}
\text{uniform one-step Q-contraction:}&
\exists c<1\ \forall\mu:\ d(\mu P)\le c\,d(\mu);\\
\text{uniform fixed-block contraction:}&
\exists N\ge1,\ c_N<1\ \forall\mu:\ d(\mu P^N)\le c_Nd(\mu);\\
\text{uniform relative convergence to laws:}&
\exists C<\infty,\ r_0<1\ \forall\mu\ \exists\pi^\mu\in\mathcal I\ \forall k\ge0:\\[-2mm]
&\hspace{10mm}W_2(\mu P^k,\pi^\mu)\le Cr_0^k d(\mu).
\end{array}
\tag{1.5}
\]

All rate factors are nonnegative. A factor zero is permitted. One constant for each individual orbit is not the last assertion in (1.5). Finite length means \(\sum_k W_2(\mu P^{k+1},\mu P^k)<\infty\), a statement about **laws**, not sample paths.

## 2. The compactness boundary

### Theorem 1 — attainment and existence of a general gauge

Under the assumptions of Section 1, \(P\) is continuous on \(\mathscr P(G)\), \(\mathcal I\) is compact, the infimum in (1.2) is attained for each \(\mu\), and \(\Psi\) is lower semicontinuous. Moreover, the following are equivalent:

1. \(\Psi^{-1}(0)=\mathcal I\).
2. There exists a strict general gauge \(\rho\) such that \(d(\mu)\le\rho(\Psi(\mu))\) for every \(\mu\in\mathscr P(G)\).

No convergence hypothesis is needed.

**Proof.** If \(f\) is continuous on \(G\), then \(x\mapsto\mathbb E f(T_\xi x)\) is continuous by bounded dominated convergence. Thus \(P\) is weakly continuous. Weak convergence and \(W_2\) convergence agree on compact \(G\), so \(\mathcal I\) is closed and compact.

The same dominated-convergence argument shows that \(c_R\) is continuous and bounded on \(G\times G\). For fixed \(\mu\), the feasible set of pairs \((\pi,\eta)\) in (1.2) is nonempty and compact. Indeed, the marginal constraints are closed, \(\pi\in\mathcal I\) is closed, and optimality is the closed equality
\(\int\|x-y\|^2d\eta=W_2(\mu,\pi)^2\).
The continuous objective therefore attains its minimum.

If \(\mu_n\to\mu\), choose minimizing \((\pi_n,\eta_n)\), and pass to a subsequence attaining the liminf of their objective values and then to a convergent subsequence of these pairs. The limit is feasible for \(\mu\), by the same closed constraints. Hence
\(\Psi(\mu)^2\le\liminf_n\Psi(\mu_n)^2\), proving lower semicontinuity.

Suppose the zero set is correct. Define
\[
\omega(s)=\sup\{d(\mu):\Psi(\mu)\le s\},\qquad s\ge0.
\tag{2.1}
\]
The set in (2.1) is nonempty because invariant laws are included. Thus \(\omega\) is finite and nondecreasing, and \(\omega(0)=0\). If \(\omega(s)\not\to0\) as \(s\downarrow0\), choose \(s_n\downarrow0\) and laws with \(\Psi(\mu_n)\le s_n\) and \(d(\mu_n)\ge e>0\). A convergent subsequence, lower semicontinuity, and continuity of distance give a noninvariant zero, a contradiction.

Here is an explicit majorant construction, so no regularity of \(\omega\) away from zero is tacitly assumed. Choose \(B>\operatorname{diam}G\) and a strictly decreasing sequence \(s_n\downarrow0\) such that \(\omega(s_n)\le B2^{-n}\). Set
\(\rho(0)=0\), \(\rho(s_n)=B2^{1-n}\), interpolate linearly on each \([s_{n+1},s_n]\), and set \(\rho(s)=B+(s-s_1)\) for \(s\ge s_1\). On each such interval,
\(\rho(s)\ge B2^{-n}\ge\omega(s_n)\ge\omega(s)\).
Above \(s_1\), \(\rho\ge B>\omega\). This gives the claimed strict gauge. Conversely, any such EB forces \(\Psi(\mu)=0\Rightarrow d(\mu)=0\). Diagonal coupling already gives \(\Psi=0\) on \(\mathcal I\). ∎

Theorem 1 concerns existence, not usefulness, of a modulus. It prevents a claim that an exact-zero compact continuous example has “no generalized gauge whatsoever.”

## 3. Natural random convex projections miss dependence

### Theorem 2 — one-step convergence with false zeros, including nearest and limit anchors

Let \(G=[0,1]^2\), \(\beta=(\delta_0+\delta_1)/2\), and select with equal probabilities
\[
T_j(x,y)=(x,j),\qquad j\in\{0,1\}.
\tag{3.1}
\]
These are Euclidean projections onto the disjoint closed convex horizontal faces. They are firmly nonexpansive, have no common fixed point, and satisfy (1.3) with \(\alpha=1/2\), \(\varepsilon_f=0\). For every joint law \(\mu\),
\[
\mu P=\mu_x\otimes\beta,\quad P^2=P,\quad
\mathcal I=\{\nu\otimes\beta:\nu\in\mathscr P([0,1])\},
\tag{3.2}
\]
\[
\boxed{\Psi(\mu)=W_2(\mu_y,\beta),\qquad
d_{W_2}(\mu,Z_\Psi)=\Psi(\mu).}
\tag{3.3}
\]
In particular,
\(Z_\Psi=\{\mu:\mu_y=\beta\}\supsetneq\mathcal I\).

For \(0<t<1/2\), set
\[
\mu_t=\tfrac12\delta_{(1/2-t,0)}+\tfrac12\delta_{(1/2+t,1)},
\qquad \bar\pi=\delta_{1/2}\otimes\beta.
\tag{3.4}
\]
Then
\[
\Psi(\mu_t)=0,\quad d(\mu_t)=W_2(\mu_t,\bar\pi)=t,
\quad \mu_t\to\bar\pi\in\mathcal I.
\tag{3.5}
\]
The false zero persists if the outer infimum is restricted either to nearest invariant targets or, for these witnesses, to the actual invariant limit \(\mu_tP\). It also persists for every source-style finite-composition discrepancy and for a sum of successive synchronous displacement-difference squares. Consequently no gauge vanishing at zero can satisfy (1.4) at \(\bar\pi\), although every law becomes invariant after one update.

**Proof.** Each update preserves the first coordinate and replaces the second by an independent fair bit, giving (3.2). For input points \((x,y),(x',y')\), the synchronous displacement difference is \((0,y-y')\), and the output difference is \((x-x',0)\). Their squared norms add to the input squared distance. This proves exact firmness and the lower bound in (3.3), since every invariant target has second marginal \(\beta\).

For the matching upper bound, fix \(a\in[0,1]\), take target \(\delta_a\otimes\beta\), and lift an optimal coupling of \(\mu_y\) and \(\beta\) by the original conditional law of \(x\) given \(y\). Its horizontal cost \(\int|x-a|^2d\mu\) is independent of the coupling. The lifted coupling is therefore optimal for the full squared distance and has discrepancy \(W_2(\mu_y,\beta)\). Changing only the second coordinate by the same optimal marginal transport gives a law in \(Z_\Psi\) at that distance. Marginalization supplies the reverse bound, proving (3.3).

To prove the distance in (3.5) against every possible invariant target, center the first coordinate. Represent the source by \((tS,(S+1)/2)\), where \(S\) is a fair sign. Write an arbitrary invariant target as \((X,(W+1)/2)\), where \(W\) is fair, \(|X|\le1/2\), and \(X,W\) are independent. In any coupling put \(m=\Pr(S\ne W)\). Then
\[
\mathbb E[WX]=0,\qquad
|\mathbb E[SX]|=|\mathbb E[(S-W)X]|\le m.
\]
The squared cost is at least
\[
t^2+\mathbb E X^2-2t\mathbb E[SX]+m
\ge t^2+\mathbb E X^2+(1-2t)m\ge t^2.
\]
The same-second-coordinate coupling to \(X=0\), namely to \(\bar\pi\), attains \(t^2\). It also has discrepancy zero, proving the nearest-anchor assertion.

For the actual limit anchor, write its centered first and second coordinates as \((tU,(W+1)/2)\), with independent fair signs \(U,W\). Every coupling has cost
\(4t^2\Pr(S\ne U)+\Pr(S\ne W)\).
When \(U=W\), the least pointwise cost is zero; when \(U\ne W\), it is \(\min\{4t^2,1\}=4t^2\). Since \(\Pr(U\ne W)=1/2\), every coupling costs at least \(2t^2\). Taking \(S=W\) attains that value and preserves the second coordinate, so this pairwise optimal coupling has zero discrepancy.

Every nonempty composition of the maps (3.1) is \((x,y)\mapsto(x,j_{\rm last})\). Its residual difference is again \((0,y-y')\), and (3.3) repeats for the corresponding discrepancy. For a pathwise sum, use the optimal input coupling of (3.5), which has equal second coordinates. At the first step its displacement difference is zero. Under shared indices the second coordinates then remain equal, while the first-coordinate displacement is always zero. Every later summand is zero as well. ∎

Toward the fixed anchor \(\bar\pi\), both \(W_2(\mu_t,\bar\pi)\) and \(W_2(\mu_tP,\bar\pi)\) equal \(t\). Thus this chain is not a paracontraction toward every invariant anchor. There is no conflict with results requiring that additional property. The theorem disproves invariant identification, not ordinary metric subregularity to \(Z_\Psi\); the latter has exact constant one here.

### Theorem F — finite-state exact identification, sharp EB, and a native verifier

Fix distinct states \(G=\{g_1,\ldots,g_N\}\), the selected maps and their probabilities. In this subsection use **column** mass vectors \(\mu\in\Delta_N\) and row-stochastic transition matrix \(P\), so
\(\mathcal I=\{\pi\in\Delta_N:(P^T-I)\pi=0\}\). Put
\[
C_{ij}=\|g_i-g_j\|^2,\qquad
R_{ij}=\mathbb E\|(g_i-T_\xi g_i)-(g_j-T_\xi g_j)\|^2.
\tag{F.1}
\]
For a transport matrix \(\eta\), let \(r\eta,c\eta\) be its row and column sums; write \(C\cdot\eta=\sum_{ij}C_{ij}\eta_{ij}\). Set \(E(\mu)=d(\mu)^2\), \(\phi(\mu)=\Psi(\mu)^2\).

For this fixed data, exact zeros \(\phi^{-1}(0)=\mathcal I\) are equivalent to a global bound \(E\le B\phi\) for one finite \(B\). Both properties are decidable by finitely many polyhedral tests in exact rational/algebraic input arithmetic. A sharp coefficient is given below. No mixing, irreducibility, unique invariant law, or almost-firmness assumption is needed. A stochastic matrix alone is insufficient input: the selected random-map realization also determines \(R\).

**Exact representation.** Form the normalized transport-dual polyhedron
\[
\mathcal D_C=\{(u,v):u_i+v_j\le C_{ij},\ u_1=0\}.
\tag{F.2}
\]
It is nonempty and pointed: any lineality direction must satisfy \(a_i+b_j=0\) for every pair; all \(a_i\) are the same and normalization forces them, and all \(b_j\), to be zero. Let \((u^k,v^k)\), \(k=1,\ldots,L\), be its finitely many vertices, and define
\[
\mathcal E_k=\{(i,j):u_i^k+v_j^k=C_{ij}\},
\]
\[
\mathcal F_k=\{\eta\ge0:\textstyle\sum_{ij}\eta_{ij}=1,
(P^T-I)c\eta=0,\ \eta_{ij}=0\text{ outside }\mathcal E_k\}.
\tag{F.3}
\]
Each \(\mathcal F_k\) is compact or empty. One has the exact identities
\[
\bigcup_k\mathcal F_k
=\{\eta:c\eta\in\mathcal I,\ \eta\in\operatorname{Opt}(r\eta,c\eta)\},
\qquad
\phi(\mu)=\min_k\min_{\substack{\eta\in\mathcal F_k\\r\eta=\mu}}R\cdot\eta.
\tag{F.4}
\]
Empty fibers have value \(+\infty\). To prove (F.4), choose an optimal normalized dual vertex for each actual marginal pair. Such a vertex exists even with zero marginal entries: the finite attained optimal face of a pointed polyhedron has a vertex. Complementary slackness places every optimal plan on its tight edges. Conversely, a plan on those tight edges has zero primal–dual gap for its own row and column marginals, hence is optimal. This retains both original minimizations; it does not replace the anchor by a nearest invariant or relax input transport optimality. Compactness and finitely many branches prove attainment.

**Exact identification test.** Let \(\mathcal V\) be the union of vertices of the nonempty \(\mathcal F_k\). Then
\[
\boxed{\phi^{-1}(0)=\mathcal I
\iff (P^T-I)rv=0\quad
\text{for every }v\in\mathcal V\text{ with }R\cdot v=0.}
\tag{F.5}
\]
Indeed, the zero face \(\mathcal Z_k=\{\eta\in\mathcal F_k:R\cdot\eta=0\}\) is a face because \(R\ge0\), and hence is generated by exactly the zero-residual vertices. Condition (F.5) makes every row marginal on every zero face stationary. Conversely, each such vertex is admissible in the original discrepancy and so its row marginal must be stationary if zeros are correct. Invariants themselves always have a zero diagonal plan.

**Sharp EB coefficient.** Assuming (F.5), define
\[
\boxed{B_*=
\max_{\substack{v\in\mathcal V\\R\cdot v>0}}
\frac{E(rv)}{R\cdot v},\qquad \max\varnothing=0.}
\tag{F.6}
\]
This is the smallest squared coefficient in the global EB, so the optimal coefficient in \(d\le K\Psi\) is \(K_* =\sqrt{B_*}\).

To verify it, first note that \(E\) is convex: mixtures of optimal couplings to stationary targets have a stationary column marginal and give the corresponding convex cost bound. Decompose a minimizing plan in (F.4) into vertices \(\eta=\sum_v\lambda_vv\). Zero-residual vertices have stationary rows and hence \(E(rv)=0\). Convexity yields
\[
E(\mu)\le\sum_v\lambda_vE(rv)
\le B_*\sum_v\lambda_v(R\cdot v)=B_*\phi(\mu).
\]
Conversely, any valid \(B\) satisfies
\(E(rv)\le B\phi(rv)\le B(R\cdot v)\) at every positive-residual vertex, so \(B\ge B_*\). A global EB forces exact zeros by evaluation at \(\Psi=0\). This proves the equivalence and sharpness.

**Native finite verification procedure.** The following finite operations use only \(G,P\) and the actual selected-map residual matrix:

1. Enumerate the vertices of (F.2), their tight-edge graphs, and the nonempty polytopes (F.3).
2. On every nonempty zero face \(\mathcal Z_k\), maximize both signs of each coordinate of \((P^T-I)r\eta\). Exact identification holds iff all these maxima are zero. Equivalently use (F.5). A positive maximum returns an explicit false-zero coupling and nonstationary source law.
3. If identification passes, enumerate \(\mathcal V\). For each positive-residual vertex compute \(E(rv)\) by the finite LP minimizing \(C\cdot\gamma\) subject to \(\gamma\ge0\), \(r\gamma=rv\), \((P^T-I)c\gamma=0\). Formula (F.6) returns the exact sharp squared coefficient.

For rational input matrices, all LP/vertex values and \(B_*\) are rational. Arbitrary real inputs require an exact-comparison representation or oracle; “finite polyhedral certificate” is not a claim of Turing decidability for unrepresented real numbers. No polynomial-time or practical large-state complexity bound is asserted.

**Optional continuity conclusion.** The same fixed finite data also make \(\phi\) globally Lipschitz and continuous piecewise affine. Here is a complete reduction to the classical fixed-matrix Hoffman bound. With \(b=(\mu,\pi)\), let \(w(b)=W_2(\mu,\pi)^2\), \(D=\operatorname{diam}G\). Changing the two coordinates of a coupling by maximal couplings gives
\(|w(b)-w(b')|\le(D^2/2)\|b-b'\|_1\): the chance either coordinate changes is bounded by the sum of the marginal total variations, and cost changes by at most \(D^2\) on that event. The optimal plan set is
\(\mathsf S(b)=\{\eta\ge0:(r\eta,c\eta)=b,\ C\cdot\eta=w(b)\}\).
Hoffman's bound for this fixed constraint matrix gives a uniform finite \(H\) with
\[
\operatorname{dist}_1(\eta,\mathsf S(b'))
\le H(\|b-b'\|_1+|w(b)-w(b')|),\qquad \eta\in\mathsf S(b).
\]
Both sets are nonempty; interchanging them bounds their Hausdorff distance. Minimizing the linear functional \(R\cdot\eta\) is therefore Lipschitz in \((\mu,\pi)\), with a uniform coefficient. Taking the minimum over the same compact stationary polytope preserves that coefficient in \(\mu\). Finally, each branch in (F.4) has a polyhedral epigraph, as a linear projection of its defining polyhedron. Finite subdivision by all domain faces and affine-piece crossings gives a finite piecewise-affine lower envelope; continuity extends the pieces to their cell closures. This uses classical [Hoffman's fixed-matrix error bound](https://nvlpubs.nist.gov/nistpubs/jres/049/4/v49.n04.a05.pdf), not a new general polyhedral principle. ∎

Theorem F makes the infinite state domain in Theorem 4 structurally necessary for the exact-zero/no-Hölder phenomenon. It makes no uniform claim over changing finite systems. Their coefficients can diverge as smaller blocks are included.

**Why the optimal-transport restriction matters.** On \(G=\{0,1,3,4\}\), take the four-cycle \(0\mapsto1\mapsto3\mapsto4\mapsto0\) and \(P=(1-p)I+pT_\#\), \(0<p<1\). Its invariant law is uniform, and its active residual labels are \((-1,-2,-1,4)\): 0 and 3 have the same signature. Nevertheless exact zeros hold. A zero-residual plan must couple the mass at 1 to 1 and mass at 4 to 4, each of target mass \(1/4\). Any off-diagonal zero-label coupling between 0 and 3 crosses the positive pair \((1,1)\), contradicting strict monotonicity of optimal squared-distance transport on the line. Thus only the diagonal uniform plan is possible.

The law with masses \((1/2,1/4,0,1/4)\) does have a zero-residual *nonoptimal* plan: send masses \(1/4\) along \(0\to0,0\to3,1\to1,4\to4\). Its cost is \(9/4\), while the monotone optimal plan costs \(5/4\) and has discrepancy squared \(p/2\). A native verifier ignoring tight edges would misclassify this example. The exact arithmetic script `output/verify_finite_state_ot_strictness.py` checks the normalization \(p=1/2\) and obtains \(E\le26\phi\). Residual squared costs scale exactly with \(p\), so the general sharp bound is
\[
E\le(13/p)\phi,
\]
attained at masses \((0,0,3/4,1/4)\), where \(E=13/4\), \(\phi=p/4\). The exhaustive domain is the 35 vectors \(z/4\), \(z_i\ge0\) integers, \(\sum_i z_i=4\): in cumulative-mass coordinates, all subdivision walls are cumulative masses equal to \(j/4\), so every cell vertex is on that grid. Both costs are affine on each cell; the zero vertex has both costs zero. Consequently checking the 35 ratios is a complete finite certificate, not sampling of arbitrary initial laws.

The balanced expected almost-firm excess is exactly \(40p\): direct substitution over the six distinct state pairs gives active excess factors \(4,0,5/8,-1/2,4,40\), respectively, in the pair order \((0,1),(0,3),(0,4),(1,3),(1,4),(3,4)\). Thus \(p<1/40\), for example \(p=1/100\), gives \(\varepsilon_f=40p<1\). Every entry of \(P^3\) is positive: the probabilities for 0, 1, 2, or 3 active updates are positive and reach all four states from each start. The resulting finite Doeblin minorization proves geometric mixing. The script's normalization \(p=1/2\) is **not** within the \(\varepsilon_f<1\) range; the small-\(p\) version is. No compatibility of its sharp EB constant with (4.20) is inferred. Its role is strictness of the native verifier, not a new convergence application.

## 4. Exact zeros and geometric convergence without any positive-Hölder EB

### Lemma 3 — finite-block transport certificates

On the ordered states \(0,1/2,1,h\), \(h=2-e\), \(0\le e\le1/100\), use the table
\[
T:(0,1/2,1,h)\mapsto(1,1/2,0,1),
\qquad P=\tfrac78I+\tfrac18T_\#.
\tag{4.1}
\]
For a row law \(v=(a,b,c,d)\), its invariant set is
\(\mathcal I_e=\{(r,1-2r,r,0):0\le r\le1/2\}\).
Let \(E_e(v)=d_{W_2}(v,\mathcal I_e)^2\). Define the row forms
\[
f_A=(1,0,-1,3)/4,\quad f_B=(-1,0,1,5)/4,
\quad f_C=(-3,-2,1,7)/4,\quad f_D=(-5,-4,-1,9)/4.
\]
Then
\[
E_0(v)=\max_{j\in\{A,B,C,D\}}vf_j^T,\qquad
E_0(vP)\le\tfrac{15}{16}E_0(v),
\tag{4.2}
\]
and
\[
(1-e)^2E_0(v)\le E_e(v)\le E_0(v),\qquad
E_e(vP)\le\frac{15}{16(1-e)^2}E_e(v).
\tag{4.3}
\]
For \(s=1/4\), \(v_s=(s,1-2s,0,s)\), one has
\[
E_e(v_s)=s(1-e)^2.
\tag{4.4}
\]

**Proof.** The stationarity equations force \(d=0\), \(a=c\), and no further restrictions. In the transport problem, destination mass may be distributed arbitrarily on \(0,1/2,1\), subject to equal arrivals at 0 and 1. The row-mass constraints already force normalization. Finite linear-program duality gives
\[
E_e(v)=\max_{\lambda\in\mathbb R}\sum_xv_x f_\lambda(x),
\quad
f_\lambda(x)=\min\{x^2-\lambda,(x-1/2)^2,(x-1)^2+\lambda\}.
\tag{4.5}
\]
The primal is feasible and has bounded finite costs. At \(e=0\), the possible breakpoints are
\(-3/4,-1/4,1/4,3/4,5/4,7/4\).
The values at the two outer breakpoints are componentwise dominated by those at \(-1/4\) and \(5/4\), respectively. Substitution at the four remaining breakpoints gives \(f_A,f_B,f_C,f_D\); outside the breakpoint range the objective cannot improve. This proves the first equality in (4.2).

In row-transition convention the matrix is
\[
P=\begin{pmatrix}
7/8&0&1/8&0\\0&1&0&0\\1/8&0&7/8&0\\0&0&1/8&7/8
\end{pmatrix}.
\]
With \(q_0=15/16\), the following exact column identities certify contraction:
\[
\begin{aligned}
q_0(\tfrac9{10}f_A+\tfrac1{10}f_B)^T-Pf_A^T&=(0,0,0,\tfrac18)^T,\\
q_0(\tfrac1{10}f_A+\tfrac9{10}f_B)^T-Pf_B^T&=0,\\
q_0(\tfrac2{15}f_A+\tfrac{23}{30}f_C+\tfrac1{10}f_D)^T-Pf_C^T&=(0,\tfrac3{64},0,0)^T,\\
q_0(\tfrac{11}{90}f_A+\tfrac{79}{90}f_D)^T-Pf_D^T&=(\tfrac18,\tfrac{17}{96},\tfrac9{64},0)^T.
\end{aligned}
\tag{4.6}
\]
Each mixture is convex and each slack is nonnegative. Multiplication by any probability row law and maximization proves the second inequality in (4.2). The factor \(15/16\) is sharp for squared distance, since \(E_0(v_sP)=15s/16\) and \(E_0(v_s)=s\).

Replacing 2 by \(2-e\) leaves the feasible mass transports unchanged. Each altered cost to a destination \(z\in\{0,1/2,1\}\) has ratio
\((1-e/(2-z))^2\in[(1-e)^2,1]\) to its old value. This proves the cost sandwich and then (4.3).

For (4.4), send the fourth-state mass to 1 and retain the other masses; the target is invariant and the cost is \(s(1-e)^2\). At \(\lambda=1/4\), the source dual values are
\((-1/4,0,1/4,(h-1)^2+1/4)\), giving the same objective for \(v_s\). Equality follows. ∎

### Theorem 4 — a compact two-map exact-zero counterexample

For \(n\ge1\), define
\[
t_n=2^{-n},\quad \delta_n=2^{-3n-10},\quad
e_n=\delta_n^n,\quad h_n=2-e_n,
\quad G_n=t_n+\delta_n\{0,1/2,1,h_n\},
\]
\[
G=\{0\}\cup\bigcup_{n\ge1}G_n\subset\mathbb R.
\tag{4.7}
\]
Let \(T\) be the translated/scaled table (4.1) in every block and let \(T(0)=0\). Select only the two maps \(I,T\), with probabilities \(7/8,1/8\). Then:

**(a)** \(G\) is compact, \(T\) is globally \(5/4\)-Lipschitz on \(G\), and (1.3) holds globally with \(\alpha=1/2\), \(\varepsilon_f=45/64<1\).

**(b)** Invariant laws give zero mass to each fourth state and equal masses to the first and third states in every block; masses at midpoints and 0 are arbitrary. These are all invariant laws, and
\[
\boxed{\Psi^{-1}(0)=\mathcal I.}
\tag{4.8}
\]

**(c)** Every initial law satisfies
\[
\boxed{d(\mu P)^2\le\frac{3125}{3267}d(\mu)^2.}
\tag{4.9}
\]
This common bound is not asserted sharp. If \(R=T_\#\), \(\Pi=(R+R^2)/2\), \(L=5/4\), and \(r_0=\sqrt{7/8}\), then
\[
\boxed{W_2(\mu P^k,\Pi\mu)\le
C r_0^k d(\mu),\quad C=\sqrt2L^2(1+L^2).}
\tag{4.10}
\]
In particular, every orbit converges to the specified invariant law \(\Pi\mu\), with
\[
\sum_{k\ge0}W_2(\mu P^{k+1},\mu P^k)
\le C\frac{1+r_0}{1-r_0}d(\mu).
\tag{4.11}
\]

**(d)** For every \(q>0\), every finite \(K\), and every \(r>0\), there is a law \(\nu\) with \(W_2(\nu,\delta_0)<r\) and
\[
d(\nu)>K\Psi(\nu)^q.
\tag{4.12}
\]
Thus ordinary linear metric subregularity and every positive-Hölder EB fail at \(\delta_0\), although the zero set is correct. A general gauge does exist by Theorem 1.

**Proof.** We supply the global transport and attainment arguments; neither may be replaced by a finite-block heuristic.

**Geometry and maps.** Each block is finite and isolated, and its positions tend to 0, so \(G\) is compact. On block \(n\), the largest secant slope is \(1/(1-e_n)\le100/99\), and \(|T(x)-x|\le\delta_n\). If \(n<m\), then \(\delta_m\le\delta_n/8\) and
\[
\operatorname{dist}(G_n,G_m)\ge t_n/2-\delta_n/4
\ge4(\delta_n+\delta_m),
\tag{4.13}
\]
because \(t_n/\delta_n=2^{2n+10}\ge4096\). Consequently
\(|T(x)-T(y)|\le|x-y|+\delta_n+\delta_m\le(5/4)|x-y|\)
for cross-block pairs. For pairs with 0, the stronger inequality \(t_n\ge4096\delta_n\) suffices. Thus \(T\) is globally \(L\)-Lipschitz and continuous. Since \(I-T\) is \((1+L)\)-Lipschitz,
\[
\mathbb E|T_\xi x-T_\xi y|^2+c_R(x,y)
\le\left[\tfrac78+\tfrac18\big((5/4)^2+(9/4)^2\big)\right]|x-y|^2
=(1+45/64)|x-y|^2.
\]

**Stationarity and global distance.** The singleton stationarity equations give exactly the invariant description in (b). Let \(S\) be \(G\) with every fourth state removed; every invariant law is supported on \(S\). Put \(m_n=\mu(G_n)\) and, when \(m_n>0\), let \(v_n\) be the conditional mass vector in block \(n\). We claim
\[
\boxed{d(\mu)^2=\sum_{n\ge1}m_n\delta_n^2E_{e_n}(v_n).}
\tag{4.14}
\]
Terms with \(m_n=0\) are zero and do not require a conditional choice.

For the local dual (4.5), an optimizer can be chosen in
\([-1/4,h_n-3/4]\subset[-1/4,5/4]\).
Indeed, on \(\lambda<-1/4\) all four lower envelopes are nondecreasing in \(\lambda\); on \(\lambda>h_n-3/4\) all four are nonincreasing. Clamping to this interval therefore cannot reduce any source dual value. For a maximizing \(\lambda_n\), put
\(g_n(0)=\lambda_n\), \(g_n(1/2)=0\), \(g_n(1)=-\lambda_n\), and use \(f_{\lambda_n}\) as the source potential. Then
\[
f_{\lambda_n}(x)+g_n(z)\le|x-z|^2,
\quad f_{\lambda_n}\le9/4,
\quad |g_n|\le5/4,
\quad \int g_n\,d\pi_n=0
\tag{4.15}
\]
for every invariant local law \(\pi_n\). The upper bound on \(f\) follows by using the midpoint destination.

Translate these potentials to each block and multiply by \(\delta_n^2\). Set both potentials to zero at 0, defining the destination potential only on \(S\). They are bounded measurable functions; in fact they tend to zero at the accumulation point. From (4.13), for \(n\ne m\),
\[
|x-z|^2\ge16(\delta_n+\delta_m)^2
\ge\tfrac94\delta_n^2+\tfrac54\delta_m^2
\ge f(x)+g(z),\quad x\in G_n,\ z\in G_m\cap S.
\]
The inequalities involving 0 follow from \(t_n\ge4096\delta_n\). Therefore \(f(x)+g(z)\le|x-z|^2\) on **all of \(G\times S\)**. For any coupling to any invariant law, integrating gives the lower bound in (4.14), since the destination potential integrates to zero blockwise and hence globally. Conversely, sum the local optimal primal couplings, weighted by \(m_n\), and couple mass at 0 diagonally. This gives an invariant target and proves the reverse inequality. No assumption that arbitrary optimal transport preserves blocks has been made.

The kernel preserves each block's total mass. Apply (4.3) in (4.14) and use \(e_n\le1/100\) to obtain
\[
d(\mu P)^2\le\frac{15}{16(99/100)^2}d(\mu)^2
=\frac{3125}{3267}d(\mu)^2.
\]

**Exact zeros.** The nonzero labels of \(I-T\) in block \(n\) are
\(-\delta_n,\delta_n,\delta_n(1-e_n)\).
They are all distinct within and across blocks, because consecutive scales differ by a factor eight and \(1-e_n\ge99/100\). The zero label occurs exactly at midpoints and 0. By Theorem 1, a zero of \(\Psi\) has a minimizing invariant target and an optimal coupling. Its discrepancy integral is zero, so it preserves these labels almost surely. Each nonzero-label source point must couple to the identical target point. In particular, no fourth-state source mass is possible; endpoint masses equal those of an invariant target and are balanced. The remaining mass lies on fixed points. Hence the source itself is invariant. The diagonal coupling proves the converse. Attainment is crucial: distinct but accumulating labels alone would not justify this step.

**Convergence to an individual law.** The table gives \(T^3=T\). Let \(a_k=(7/8)^k\), \(b_k=(3/4)^k\). The number of active updates is binomial, giving the exact positive mixture
\[
\mu P^k=a_k\mu+\tfrac{1-b_k}{2}R\mu+
\left(\tfrac{1+b_k}{2}-a_k\right)R^2\mu.
\tag{4.16}
\]
The three coefficients are the probabilities of zero, odd, and positive-even numbers of active updates. Further, \(R\Pi=\Pi\), \(\Pi\mu\in\mathcal I\), and \(\operatorname{Lip}\Pi\le L^2\) in \(W_2\). When \(a_k\le1/2\), rewrite (4.16) as
\[
(1-2a_k)\Pi\mu+a_k\mu+(a_k-b_k/2)R\mu+(b_k/2)R^2\mu.
\tag{4.17}
\]
All weights are nonnegative, and the nonstationary weights sum to \(2a_k\). Couple every component to \(\Pi\mu\), which is fixed by \(R,R^2\). Convexity of squared transport cost under such mixture couplings gives
\(W_2(\mu P^k,\Pi\mu)^2\le2a_kL^4W_2(\mu,\Pi\mu)^2\).
If \(a_k>1/2\), the original mixture (4.16) yields the same bound since its total weight is \(1\le2a_k\). For a nearest invariant \(\pi\),
\[
W_2(\mu,\Pi\mu)\le W_2(\mu,\pi)+W_2(\Pi\pi,\Pi\mu)
\le(1+L^2)d(\mu).
\]
This proves (4.10). The triangle inequality between successive iterates through \(\Pi\mu\), followed by summation, proves (4.11).

**Failure of every positive power.** Put the mass vector \(v_s\), \(s=1/4\), entirely in block \(n\), and call the resulting law \(\nu_n\). Its support tends to 0, so \(\nu_n\to\delta_0\). Equations (4.4) and (4.14) give
\[
d(\nu_n)=(1-e_n)\delta_n\sqrt s.
\tag{4.18}
\]
The coupling used in (4.4) is globally nearest and therefore pairwise optimal. Its only nonzero residual difference is on the fourth-to-third pair, with magnitude \(\delta_ne_n\) for the active map. Thus, by exact zero identification and noninvariance,
\[
0<\Psi(\nu_n)\le\sqrt{ps}\,\delta_ne_n
=\sqrt{ps}\,\delta_n^{n+1},\qquad p=1/8.
\tag{4.19}
\]
For each fixed \(q>0\),
\[
\frac{d(\nu_n)}{\Psi(\nu_n)^q}
\ge\frac{(1-e_n)\sqrt s}{(ps)^{q/2}}
\delta_n^{1-q(n+1)}\longrightarrow\infty.
\]
This proves (4.12) with all its quantifiers. ∎

The constructed domain is countable and non-semialgebraic; the update family has only **two** continuous maps. No claim that this is itself a random convex-proximal model is needed. The natural projection model and this exact-zero model perform different logical jobs.

### Corollary 5 — no compatible gauge for the fixed almost-firm scalar formula

For a strict general gauge \(\rho\), fix \(0<\alpha<1\), \(\tau=(1-\alpha)/\alpha\), and a finite valid violation \(\varepsilon_f\). Define the source-style scalar expression
\[
\Theta_\rho(t)^2=(1+\varepsilon_f)t^2-\tau[\rho^{-1}(t)]^2.
\tag{4.20}
\]
“Locally strict contraction-compatible” means that (1.4) holds, (4.20) is real, and \(0\le\Theta_\rho(t)<t\) for all sufficiently small \(t>0\). This definition fixes the formula and its parameters; it is not a synonym for all useful rate information.

In Theorem 4, no such gauge exists for any fixed parameters whose almost-firm inequality is valid on a complete state neighborhood of 0 (and hence none exists for globally valid parameters).

**Proof.** Every complete state neighborhood of 0 contains a full block. In any such block, compare its fourth point with its third point. Their input distance is \(\delta_n(1-e_n)\), while their active-map output distance is \(\delta_n\). Thus
\[
\frac{\mathbb E|T_\xi x-T_\xi y|^2}{|x-y|^2}
=\tfrac78+\frac{1}{8(1-e_n)^2}>1.
\tag{4.21}
\]
Because the additional defect term in (1.3) is nonnegative, every fixed valid \(\varepsilon_f\) on that neighborhood is strictly positive. The third point is in an invariant support, so restricting the comparison anchor to invariant-support points does not remove (4.21).

If \(\Theta_\rho(t)<t\), then
\(\rho^{-1}(t)>\sqrt{\varepsilon_f/\tau}\,t\).
Substitute \(t=\rho(s)\), valid for all sufficiently small \(s>0\), to get
\[
\rho(s)<\sqrt{\tau/\varepsilon_f}\,s.
\tag{4.22}
\]
Combining this local linear envelope with the EB gives a local linear bound for \(\Psi\), contrary to Theorem 4(d). The witnesses (4.19) have residuals tending to zero, so the required local ranges are met. ∎

This rules out gauges compatible with (4.20), while Theorem 1 supplies slower gauges not compatible with that formula. It neither contradicts the observed geometric rate nor excludes stronger native, non-scalar, or differently parameterized rate proofs.

## 5. Correlation-aware binary conditional repair

This section deliberately changes the certificate and transport restriction. Let \(U\) be a standard Borel space, fix a probability law \(\nu\), and let \(X=\{0,1\}^m\). Set
\[
\mathscr M_\nu=\{\mu(du,dx)=\nu(du)\mu_u(dx)\},\qquad
\mathsf W_\nu(\mu,\eta)^2=\int W_2(\mu_u,\eta_u)^2\,\nu(du).
\tag{5.1}
\]
Here squared Euclidean cost on \(X\) is Hamming cost. The distance (5.1) allows only transport preserving \(u\). It is an existing conditional/fibered Wasserstein distance, not a newly introduced metric. Finite fibers make conditional laws and optimal coupling choices measurable, for example by selecting among the finitely many bases of the finite transport linear program with a deterministic tie rule.

Let \(b_i(u)\in(0,1)\), \(p_i(u)>0\) be measurable and satisfy \(\sum_i p_i(u)\le1\) almost everywhere. In fiber \(u\), choose coordinate \(i\) with probability \(p_i(u)\), replace it by an independent \(\operatorname{Bern}(b_i(u))\), and use identity for the remaining probability. The actual kernel preserves \(u\). Put
\[
\beta_u=\bigotimes_i\operatorname{Bern}(b_i(u)),\qquad
\pi_\nu(du,dx)=\nu(du)\beta_u(dx),\quad E(\mu)=\mathsf W_\nu(\mu,\pi_\nu).
\]
Define the coordinate-conditional residual
\[
d_i(u;\mu)^2=
\sum_{x_{-i}}\mu_u(x_{-i})
\left|\mu_u(X_i=1\mid x_{-i})-b_i(u)\right|,
\]
\[
\boxed{\mathcal R(\mu)^2=\int\sum_i p_i(u)d_i(u;\mu)^2\,\nu(du).}
\tag{5.2}
\]
The residual holds **all untouched coordinates** \((u,x_{-i})\) fixed. Values of conditionals on null conditioning events do not matter. Unlike (1.2), (5.2) is directly defined from the current law and native update specification, with no minimization over unknown invariant laws.

State-dependent sampling gives a legitimate Markov kernel but not automatically a continuous random-map realization on a Euclidean product. When \(p_i,b_i\) are constant, the actual random state maps are ordinary coordinate projections, with the conserved coordinate left untouched.

### Theorem 6 — exact zeros and sharp uniform binary equivalence

Let \(a_* =\operatorname{ess\,inf}_{u\sim\nu}\min_i p_i(u)\). Then \(\pi_\nu\) is the unique invariant law in \(\mathscr M_\nu\), and
\[
\mathcal R(\mu)=0\iff\mu=\pi_\nu\iff\mu P=\mu.
\tag{5.3}
\]
If \(a_*>0\), the optimal uniform EB coefficient and the optimal \(k\)-step distance factors are
\[
\boxed{E(\mu)\le a_*^{-1/2}\mathcal R(\mu),\qquad
E(\mu P^k)\le(1-a_*)^{k/2}E(\mu),\quad k\ge1.}
\tag{5.4}
\]
If \(a_*=0\), no finite uniform linear EB exists and the optimal uniform factor for each fixed \(k\ge1\) is 1. More precisely, the following are equivalent:

1. \(a_*>0\).
2. \(\exists K<\infty\ \forall\mu\in\mathscr M_\nu:\ E(\mu)\le K\mathcal R(\mu)\).
3. \(\exists c<1\ \forall\mu:\ E(\mu P)\le cE(\mu)\).
4. \(\exists N\ge1,c_N<1\ \forall\mu:\ E(\mu P^N)\le c_NE(\mu)\).
5. \(\exists C<\infty,c<1\ \forall\mu\ \forall k\ge0:\ E(\mu P^k)\le Cc^kE(\mu)\).

The same equivalence and the same optimal constants hold on any fixed full \(\mathsf W_\nu\)-ball of positive radius about \(\pi_\nu\). The marginal \(\nu\) and this conditional metric remain fixed in every quantifier.

**Proof.** First, for any law \(\gamma\) on \(X\) and product Bernoulli target \(\beta\),
\[
W_2(\gamma,\beta)^2\le
\sum_i\mathbb E_\gamma
\left|\gamma(X_i=1\mid X_{-i})-b_i\right|.
\tag{5.5}
\]
To prove (5.5), sequentially couple, given the past pairs, the law of \(X_i\) conditional on \(X_{<i}\) with the fixed target Bernoulli law. The first marginal is \(\gamma\), and the second is \(\beta\), because its conditional law is fixed even given all preceding pairs. Its expected cost is the sum of discrepancies conditioned on \(X_{<i}\). The tower property and convexity of absolute value bound each by the corresponding discrepancy conditioned on \(X_{-i}\). This proves (5.5).

Apply (5.5) fiberwise: if \(a_*>0\), then \(E^2\le\mathcal R^2/a_*\). Without a uniform lower bound, \(\mathcal R=0\) still forces every \(d_i=0\) almost everywhere, because the weights are positive; (5.5) then gives \(\mu=\pi_\nu\).

For convergence, optimally couple \(\mu_u\) with \(\beta_u\), choose the same update coordinate and the same fresh bit on both sides, and leave all other coordinates unchanged. A mismatch in coordinate \(i\) survives with probability \(1-p_i(u)\), so expected squared cost decreases by at least factor \(1-\min_i p_i(u)\). This proves the contraction in (5.4). For each fixed fiber this factor is below 1 and \(\beta_u\) is invariant; hence it is the only invariant fiber law. Since invariance disintegrates when \(u\) is preserved, (5.3) follows. Dominated convergence also gives convergence of every law when merely \(p_i>0\) almost everywhere, even if \(a_*=0\).

To prove sharpness, for each \(\epsilon>0\) choose an index \(i\) and a positive-measure set \(A\) on which \(p_i<a_*+\epsilon\). Such a choice exists because there are finitely many coordinates. On \(A\), perturb only the \(i\)-th factor of \(\beta_u\), toward its farther endpoint, by a common mixing amount \(s\in(0,1]\); outside \(A\), do not perturb. Let \(h(u)>0\) be the resulting coordinate probability difference. All other discrepancies vanish and exactly
\[
E^2=\int_Ah\,d\nu,\quad
\mathcal R^2=\int_Ap_i h\,d\nu,\quad
E(\mu P^k)^2=\int_A(1-p_i)^kh\,d\nu.
\tag{5.6}
\]
The last identity follows because the law remains a product with only that factor perturbed; its probability difference is multiplied by \(1-p_i\) at each step. The lower transport bound comes from the changed marginal, and changing only that coordinate attains it. Letting \(\epsilon\downarrow0\) proves every claimed optimal coefficient, including factor 1 and infinite EB coefficient when \(a_*=0\). Letting \(s\downarrow0\) makes the witnesses arbitrarily local without changing their ratios.

The implications from (1) to (2) and (3), and from (3) to (4) and (5), now follow from (5.4). The witnesses exclude (2) and (4) when \(a_*=0\). Finally, (5) implies (4) by choosing a common \(N\) with \(Cc^N<1\). This argument also applies to a full local ball because the claimed estimate already covers all its initial laws and every time. ∎

For \(a_*>0\), putting \(c_* =\sqrt{1-a_*}\) gives the law-space length bound
\[
\sum_{k\ge0}\mathsf W_\nu(\mu P^{k+1},\mu P^k)
\le\frac{1+c_*}{1-c_*}E(\mu).
\tag{5.7}
\]
It is an upper bound from the triangle inequality through \(\pi_\nu\), not an asserted optimal length constant.

### Theorem 7 — exact nonuniform one-bit modulus, rates and law-space length

Take \(m=1\), denote the refresh probability by \(a(u)\in(0,1]\), and write current and target probabilities as \(r(u),b(u)\). Put
\(h=|r-b|\), \(M=\max\{b,1-b\}\). Every measurable \(0\le h\le M\) is realizable, by moving toward a farther endpoint. Then
\[
E_k^2=\int(1-a)^kh\,d\nu,\quad
\mathcal R_k^2=\int a(1-a)^kh\,d\nu,
\]
\[
\mathsf W_\nu(\mu P^{k+1},\mu P^k)^2=\mathcal R_k^2
=E_k^2-E_{k+1}^2.
\tag{5.8}
\]
The smallest **nondecreasing uniform modulus** satisfying \(E\le\phi(\mathcal R)\) is
\[
\boxed{\phi(t)^2=
\sup\left\{\int h\,d\nu:0\le h\le M,\ \int ah\,d\nu\le t^2\right\}
=\inf_{\lambda\ge0}\left[\lambda t^2+\int M(1-\lambda a)_+\,d\nu\right].}
\tag{5.9}
\]
It obeys \(\phi(0)=0\) and \(\phi(t)\to0\) as \(t\downarrow0\). It is bounded and eventually saturated, so it is not described as a globally strictly increasing gauge.

Every law converges in \(\mathsf W_\nu\), and the exact worst-law absolute error and the exact length for a specified initial law are
\[
\boxed{\sup_{\mu\in\mathscr M_\nu}E(\mu P^k)^2
=\int M(1-a)^k\,d\nu,}
\tag{5.10}
\]
\[
\boxed{\sum_{k\ge0}\mathsf W_\nu(\mu P^{k+1},\mu P^k)
=\sum_{k\ge0}\left[\int a(1-a)^kh\,d\nu\right]^{1/2}.}
\tag{5.11}
\]

**Proof.** Refresh sends \(r-b\) to \((1-a)(r-b)\). Squared transport distance between Bernoulli laws is the absolute probability difference, proving (5.8). Realizability of every \(h\) proves the first formula in (5.9) and minimality among nondecreasing uniform moduli.

For duality, set \(d\zeta=M\,d\nu\), \(h=Mf\), \(0\le f\le1\), and \(B=t^2\). The primal maximizes \(\int f\,d\zeta\) subject to \(\int af\,d\zeta\le B\). For every \(\lambda\ge0\),
\(f\le\lambda af+(1-\lambda a)_+\), proving the dual upper bound. If \(B\ge\int a\,d\zeta\), take \(f=1\) and \(\lambda=0\). If \(B=0\), the primal value is zero since \(a>0\) almost everywhere; the dual values tend to zero as \(\lambda\to\infty\), by dominated convergence. Otherwise choose \(q\in(0,1]\) with
\[
\int_{\{a<q\}}a\,d\zeta\le B\le\int_{\{a\le q\}}a\,d\zeta.
\]
Fill \(f=1\) on \(a<q\), \(f=0\) on \(a>q\), and choose a constant fraction on \(a=q\) to make the budget exact. If that level has zero mass, the two bounds already coincide. With \(\lambda=1/q\), the pointwise dual bound is equality on each of the three regions. This proves (5.9), including atomic environments.

For every \(\epsilon>0\),
\[
\phi(t)^2\le t^2/\epsilon+\int_{\{a\le\epsilon\}}M\,d\nu.
\]
First take \(t\downarrow0\), then \(\epsilon\downarrow0\), to prove continuity at zero. Dominated convergence in (5.8) proves convergence. The farthest-endpoint law realizes \(h=M\), so (5.10) is attained. Summing the exact step identities proves (5.11). ∎

For example, with uniform \(\nu\) on \((0,1)\), \(b=1/2\), and \(a(u)=u^r\), \(r>0\), filling \([0,s]\) first gives, below the saturation threshold,
\[
\phi(t)=2^{-r/[2(r+1)]}(r+1)^{1/[2(r+1)]}t^{1/(r+1)}.
\tag{5.12}
\]
For the farthest-endpoint law,
\[
E_k^2=\frac1{2r}B(1/r,k+1),\qquad
\mathcal R_k^2=\frac1{2r}B(1+1/r,k+1).
\]
The beta-integral asymptotics imply \(E_k\asymp k^{-1/(2r)}\) and \(\mathcal R_k\asymp k^{-(1+1/r)/2}\). Hence the worst-law length is finite exactly when \(r<1\). For \(a(u)=e^{-1/u}\), choosing \(h=(1/2)1_{[0,s]}\) gives
\(E^2=s/2\), \(\mathcal R^2\le(s/2)e^{-1/s}\); thus no positive-Hölder modulus exists although (5.9) still does. These variable-probability examples are kernel statements, not claims of a finite continuous-RFI realization.

The scalar profile is an existing-type weak-Poincaré/spectral mechanism, not a new convergence paradigm. In the fair-bit case, on \(\pi=\nu\otimes\operatorname{Bern}(1/2)\), put
\(g(u,x)=\sqrt{2h(u)}(2x-1)\). Then \(g\) is centered on each fiber,
\[
\|g\|_2^2=2E^2,\qquad
\langle g,(I-P)g\rangle=2\mathcal R^2,
\qquad E_{2k}^2=\tfrac12\|P^kg\|_2^2.
\tag{5.13}
\]
On this invariant-complement subspace \(P\) is multiplication by \(1-a\), and the optimal bounded weak-Poincaré remainder is exactly \(\int(1-\lambda a)_+d\nu\). The nonergodic conserved-variable component must not be omitted when making this comparison.

## 6. A genuinely coupled Gaussian conditional certificate

### Theorem 8 — sharp Gaussian conditional EB and a native contraction bound

Let \(Q\in\mathbb R^{m\times m}\) be symmetric positive definite, \(m_0\in\mathbb R^m\), and \(\beta=N(m_0,Q^{-1})\). Let \(p_i>0\), \(\sum_i p_i=1\), and define
\[
D=\operatorname{diag}(p_i/Q_{ii}),\qquad
\zeta=\lambda_{\min}(Q^{1/2}DQ^{1/2})>0.
\tag{6.1}
\]
At each step select \(i\), draw \(\xi_i\sim N(0,Q_{ii})\), and apply
\[
T_{i,\xi}(x)=x+
\frac{(Qm_0)_i+\xi_i-(Qx)_i}{Q_{ii}}e_i.
\tag{6.2}
\]
These are \(Q\)-orthogonal projections onto random affine hyperplanes and are precisely Gaussian Gibbs coordinate updates. Off-diagonal entries of \(Q\) are allowed. On all probability laws with finite second moment, set
\[
\mathcal R_Q(\mu)^2=
\sum_i p_iQ_{ii}\int
W_2\bigl(\mu_i(\cdot\mid x_{-i}),\beta_i(\cdot\mid x_{-i})\bigr)^2\,
\mu_{-i}(dx_{-i}).
\tag{6.3}
\]
Then
\[
\boxed{W_{2,Q}(\mu,\beta)^2\le\zeta^{-1}\mathcal R_Q(\mu)^2,}
\tag{6.4}
\]
\[
\boxed{W_{2,Q}(\mu P,\beta)\le\sqrt{1-\zeta}\,W_{2,Q}(\mu,\beta).}
\tag{6.5}
\]
The coefficient \(\zeta^{-1/2}\) in the unsquared EB is optimal globally and on every full positive-radius \(W_{2,Q}\)-ball about \(\beta\). Equation (6.5) is a valid factor, whose sharpness is not asserted here. The invariant law in the finite-second-moment class is unique, and \(\mathcal R_Q(\mu)=0\iff\mu=\beta\).

**Proof.** Put
\(A_i=I-e_ie_i^TQ/Q_{ii}\). Identical-noise updates send differences \(h\) to \(A_ih\), and
\[
\sum_i p_i\|A_ih\|_Q^2
=\|h\|_Q^2-h^TQDQh
\le(1-\zeta)\|h\|_Q^2.
\tag{6.6}
\]
The target is invariant under each Gibbs coordinate kernel. Applying the shared-noise coupling to an optimal input coupling proves (6.5). Also, \(\operatorname{tr}(Q^{1/2}DQ^{1/2})=1\), so \(0<\zeta\le1\) and the factor is well defined.

For the stronger EB, keep the marginals fixed at \(\mu,\beta\). Starting from any finite-cost coupling \((X,Y)\), update the first coordinate chain using \(\mu\)'s own full conditional. More precisely, conditional on the current pair and selected \(i\), optimally couple
\(X_i'\sim\mu_i(\cdot\mid X_{-i})\) with
\(Z_i\sim\beta_i(\cdot\mid X_{-i})\), using one-dimensional quantiles; then set
\[
Y_i'=Z_i+\bar m_i(Y_{-i})-\bar m_i(X_{-i}),
\]
where
\(\bar m_i(x_{-i})=(m_0)_i-\sum_{j\ne i}Q_{ij}(x_j-(m_0)_j)/Q_{ii}\)
is the Gaussian conditional mean. Leave the other coordinates unchanged. Conditional variances are independent of the conditioning value, so the second update has precisely the target conditional at \(Y_{-i}\). Thus the full marginals stay \(\mu,\beta\) at every step. Quantile coupling ensures measurability; null conditioning sets are immaterial. All costs are finite because both marginals have finite second moments and the Gaussian conditional means are affine.

With \(h=X-Y\), \(\epsilon_i=X_i'-Z_i\), the updated difference is
\(h'=A_ih+e_i\epsilon_i\). Orthogonality gives
\(A_i^TQe_i=0\), so pointwise
\[
\|h'\|_Q^2=\|A_ih\|_Q^2+Q_{ii}\epsilon_i^2.
\]
If \(C_n\) is the expected coupling cost after \(n\) updates, the unchanged first marginal and optimal conditional coupling yield
\[
C_{n+1}\le(1-\zeta)C_n+\mathcal R_Q(\mu)^2.
\]
Every \(C_n\) is a cost for the same marginal pair, hence bounds \(W_{2,Q}(\mu,\beta)^2\) from above. Iteration and \(n\to\infty\) prove (6.4). No stationary-coupling existence or regularity of \(\mu\)'s conditionals is needed.

For sharpness take \(\mu=N(m_0+v,Q^{-1})\). Translation coupling is optimal, and the conditional mean shifts give
\[
W_{2,Q}(\mu,\beta)^2=v^TQv,\qquad
\mathcal R_Q(\mu)^2=v^TQDQv.
\]
Choose \(Q^{1/2}v\) in a least-eigenvalue eigenspace of \(Q^{1/2}DQ^{1/2}\). Equality holds in (6.4). Scaling \(v\) proves local sharpness. Exact zeros follow from (6.4), and any invariant finite-moment law equals \(\beta\) by (6.5). ∎

This strengthens the earlier triangle coefficient \((1-\sqrt{1-\zeta})^{-1}\) to the sharp \(\zeta^{-1/2}\). It does not establish the global priority of that Gaussian tensorization statement. The precision-matrix sampling eigenvalue is already a mature Gaussian Gibbs object; it must not be advertised as newly discovered.

## 7. What the repair gives in ordinary Wasserstein, and what it does not

When \(U\subset\mathbb R^\ell\) and \(\nu\) has finite second moment, ordinary joint \(W_2\) is defined and allows more couplings than (5.1). Thus a conditional EB yields the valid **sufficient** ordinary invariant-set bound
\[
d_{W_2}(\mu,\operatorname{inv}P)
\le W_2(\mu,\pi_\nu)
\le\mathsf W_\nu(\mu,\pi_\nu)
\le K\mathcal R(\mu).
\tag{7.1}
\]
Conditional convergence likewise implies ordinary joint convergence. Neither necessity, sharp constants, nor an ordinary relative rate normalized by the smaller ordinary initial error follows from (7.1).

For the one-step projections of Theorem 2, on laws supported on \([0,1]\times\{0,1\}\), put
\(r(u)=\mu(Y=1\mid X=u)\). Then
\[
\mathcal R(\mu)^2=\int|r(u)-1/2|\,\mu_x(du)
=\mathsf W_{\mu_x}(\mu,\mu P)^2.
\tag{7.2}
\]
It is zero exactly at invariant laws. For \(\mu_t\) in (3.4),
\(\Psi(\mu_t)=0\), but \(\mathcal R(\mu_t)=1/\sqrt2\), while \(d(\mu_t)=t\to0\). Hence no finite upper comparison \(\mathcal R\le C\Psi\) is possible, and the conditional metric is not locally equivalent to ordinary joint distance across varying conserved marginals. Equation (7.2) is a repair of identification, not a proof that the original discrepancy was necessary.

Even for a fixed nonatomic conserved marginal, local equivalence may fail. A direct example uses uniform \(u\in[0,1]\): divide the interval into \(2n\) equal consecutive cells, set the bit deterministically to 0 on the first cell of each pair and 1 on the second, and let the target bit be conditionally fair. The conditional squared error is always \(1/2\). Ordinary transport can keep half the mass fixed and move the other half horizontally to the adjacent cell, retaining its bit, at displacement \(1/(2n)\). The target is the product of uniform \(u\) and the fair bit, and the squared cost is \(1/(8n^2)\to0\). This proves non-equivalence without changing the conserved marginal.

## 8. A safe RL interface and an explicit recoupling condition

### Proposition 9 — the coupled Hilbert identity, with no measure reflector

Let \(\pi\in\mathcal I\), \(\eta\in\operatorname{Opt}(\mu,\pi)\), and use a shared index in the input coupling. Define
\[
w=W_2(\mu,\pi),\qquad
D_\eta^2=\int c_R\,d\eta,
\quad A_\eta=\int\mathbb E\|T_\xi x-T_\xi y\|^2d\eta.
\]
If
\[
\int\mathbb E\|2(T_\xi x-T_\xi y)-(x-y)\|^2d\eta\le\Omega(w)^2,
\tag{8.1}
\]
then
\[
A_\eta+D_\eta^2\le\frac{w^2+\Omega(w)^2}{2},\qquad
D_\eta\le\frac{w+\Omega(w)}2,\qquad
\sqrt{A_\eta}\le\frac{w+\Omega(w)}2.
\tag{8.2}
\]

**Proof.** In the Hilbert space \(L^2(\eta\otimes\vartheta;\mathbb R^d)\), let
\(a=T_\xi x-T_\xi y\), \(b=(x-y)-a\).
Then \(\|a+b\|_2=w\), \(\|a-b\|_2\le\Omega(w)\). The parallelogram and triangle identities give (8.2). ∎

For affine orthogonal coordinate projections, \(\Omega(w)=w\), the linear monotone slice. The identity is entirely on coupled state differences. It neither defines \(2\mu P-\mu\) as a probability measure nor establishes a genuinely nonlinear \(\gamma<1\) advantage. In general \(2\mu P-\mu\) is signed, and the finite-dimensional T5 theorem cannot be applied verbatim to the infinite-dimensional space of laws.

The conditional specification residual is not generally this matched synchronous defect. For example, with two fair target bits and equal random-scan probabilities, take the law with masses \((1/2,0,1/4,1/4)\) on \(00,01,10,11\). Its target is uniform; exact transport and direct conditionals give
\[
E^2=1/4,\qquad E_+^2=1/8,\qquad\mathcal R^2=1/4.
\tag{8.3}
\]
Indeed the initial transport moves mass \(1/4\) from \(00\) to \(01\); the updated masses are \((5/16,3/16,5/16,3/16)\), whose excess-to-deficit transport cost is \(1/8\); both coordinate conditional discrepancies are \(1/4\). Thus \(E_+^2+\mathcal R^2>E^2\). Substituting \(\mathcal R\) for \(D_\eta\) in (8.2) would be invalid. Only the one-bit model has the exact matched energy identities (5.8).

### Proposition 10 — an explicit sufficient recoupling-loss hypothesis for necessity

Suppose \(d(\mu P)\le c\,d(\mu)\), \(c<1\), on a specified class of laws. For each source-optimal invariant pair define
\[
\Delta_\eta=A_\eta-d(\mu P)^2\ge0.
\tag{8.4}
\]
The quantity includes both nonoptimality of the synchronous output coupling and the advantage of changing the invariant anchor after the update. Assume that for every law in the class there are feasible pairs \((\pi_j,\eta_j)\) with \(D_{\eta_j}\to\Psi(\mu)\) and
\(\Delta_{\eta_j}\le\chi D_{\eta_j}^2\), for one finite common \(\chi\ge0\). Then
\[
d(\mu)\le\frac{1+\sqrt\chi}{1-c}\Psi(\mu).
\tag{8.5}
\]
Alternatively, if the same near-minimizing pairs satisfy
\(\Delta_{\eta_j}\le\sigma^2d(\mu)^2\), with \(c^2+\sigma^2<1\), then
\[
d(\mu)\le\frac{\Psi(\mu)}{1-\sqrt{c^2+\sigma^2}}.
\tag{8.6}
\]

**Proof.** Shared-noise output coupling has second marginal \(\pi P=\pi\), so \(A_\eta\ge d(\mu P)^2\). Minkowski gives
\[
d(\mu)\le W_2(\mu,\pi)\le D_\eta+\sqrt{A_\eta}
=D_\eta+\sqrt{d(\mu P)^2+\Delta_\eta}.
\]
Under the first condition this is at most
\((1+\sqrt\chi)D_\eta+c\,d(\mu)\).
Rearrange and pass to the near-minimizing limit. Under the second condition it is at most
\(D_\eta+\sqrt{c^2+\sigma^2}\,d(\mu)\), giving (8.6). ∎

This is an elementary conditional repair, not a flagship theorem by itself. Its quantifier over pairs approaching the **same** discrepancy infimum is essential. Having a loss bound for unrelated couplings does not prove (8.5). In Theorem 2's witness with nearest anchor, \(D_\eta=0\), \(A_\eta=t^2\), \(d(\mu_tP)=0\), so \(\Delta_\eta=t^2>0\): the omitted information is visible exactly in (8.4).

The legitimate relationship to the core RL manuscript is a common discipline: geometry, residual, target, actual transition, and localization must match. The deterministic core's Proposition 3.5 already separates actual convergence from compatibility of a scalar certificate. The present Markov examples add an independent failure mode—optimal transport and invariant-anchor changes can erase dependence information. Neither mechanism proves that the other theorem is necessary or universally stronger.

### Proposition M — mass dilution obstructs higher-order RMS law bounds

Let \(S\subset\mathbb R^d\) be nonempty and closed, \(1\le p,r<\infty\), and let \(\mathcal I\subset\mathscr P_p(S)\) be an invariant-law family supported on \(S\). Fix \(\pi\in\mathcal I\) and a Markov kernel \(P\) with \(\pi P=\pi\). Let \(c\ge0\) be measurable, with \(c=0\) \(\pi\)-almost everywhere. Suppose there is a state \(a\) with \(0<c(a)<\infty\), with \(P(a,\cdot)\) having finite \(p\)-th moment, and with
\[
e(a)=\left[\int d(y,S)^pP(a,dy)\right]^{1/p}>0.
\]
Define \(\mathcal R_r(\mu)=(\int c(x)^r\mu(dx))^{1/r}\). If there exist \(K<\infty\), \(q>0\), and a full \(W_p\)-neighborhood of \(\pi\) on which
\[
d_{W_p}(\mu P,\mathcal I)\le K\mathcal R_r(\mu)^q,
\tag{M.1}
\]
then necessarily \(q\le r/p\). The conclusion also holds if only the mixture laws used in the proof are included and \(\mathcal R_r\) is replaced by any residual bounded above by a common constant times their \(\epsilon^{1/r}\) scaling.

**Proof.** For \(\mu_\epsilon=(1-\epsilon)\pi+\epsilon\delta_a\), diagonal coupling of the common part gives
\[
W_p(\mu_\epsilon,\pi)^p
\le\epsilon\int\|a-x\|^p\pi(dx)\to0.
\]
Thus every sufficiently small \(\epsilon\) lies in the stated neighborhood. Linearity gives
\(\mu_\epsilon P=(1-\epsilon)\pi+\epsilon P(a,\cdot)\).
Every coupling to a law on \(S\) costs at least the integral of \(d(y,S)^p\) over its first marginal, so
\[
d_{W_p}(\mu_\epsilon P,\mathcal I)\ge\epsilon^{1/p}e(a),
\qquad \mathcal R_r(\mu_\epsilon)=\epsilon^{1/r}c(a).
\]
If \(q>r/p\), (M.1) would imply
\(e(a)\le Kc(a)^q\epsilon^{q/r-1/p}\to0\), a contradiction. ∎

For the usual \(p=r=2\), every \(q>1\) is excluded under these hypotheses. The support separation and stationarity-vanishing residual are essential: for a full-support invariant family, \(S\) may be the entire state domain and \(e(a)=0\); for a physical displacement residual that remains positive at equilibrium, \(c=0\) fails. The proposition is therefore not a universal no-go for arbitrary Markov discrepancies, including (1.2).

The exact scalar moment counterpart is elementary. For nonnegative finite measurable \(e,c\), assume there is a common zero \(s\) and a nonzero excursion \(a\) as above. Then
\[
\|e\|_{L^p(\mu)}\le K\|c\|_{L^r(\mu)}^q
\quad\text{for every finitely supported probability law }\mu
\]
holds iff both \(pq\le r\) and \(e(x)\le Kc(x)^q\) for all states hold. Necessity follows from Dirac laws and the two-point mixtures; sufficiency follows from
\(\|e\|_p\le K\|c\|_{pq}^q\le K\|c\|_r^q\).
This is a comparison of positive moments even if \(pq<1\). In particular a deterministic \(q>1\) EB naturally lifts through a \(2q\)-moment, not automatically an RMS residual. Composing a matched pointwise RL/EB transfer **before** integration can avoid the erroneous intermediate RMS inequality. Existence of the matched transport references remains a separate native hypothesis.

A small law-space radius does not bound every sampled state: an arbitrarily rare excursion of any fixed finite amplitude belongs to every sufficiently small full law neighborhood. Pointwise support restrictions must therefore be retained separately from Wasserstein localization.

### Closest general stochastic regularity comparison

[Pischke–Powell, *Convergence guarantees for stochastic algorithms solving non-unique problems in metric spaces*, arXiv:2605.06129v1](https://arxiv.org/html/2605.06129v1), already treats regularity in mean for nonunique zero sets (Definition 3.4), Jensen lifting of convex forward moduli and their convex-envelope modification (Lemma 3.8, Remark 3.9), and measurable moving solution anchors (Definition 4.2). Theorem 4.8 gives quantitative convergence under stochastic quasi-Fejér and regularity assumptions; Theorem 5.1 applies the framework to stochastic PPA for a normal convex integrand. Definition 3.6's footnote explicitly notes the difficulty of state-local assumptions in stochastic settings.

Consequently, general gauges, nonunique targets, stochastic PPA, or moving anchors alone are not new contributions here. Their stated framework concerns actual random-state convergence to a zero set; the present source-discrepancy problem concerns invariant laws that may be non-Dirac and may not concentrate on common fixed points. Native transport/reference matching is not supplied merely by renaming their solution anchors. This is a domain distinction, not a demonstrated strict extension of their theory. [Primary definitions and theorems](https://arxiv.org/html/2605.06129v1).

## 9. Optional dependent finite-state import

The following correct supplement can be retained as an application of classical Dobrushin comparison, not as a claimed new comparison principle.

Let \(\beta>0\) on \(\{0,1\}^m\), let \(C=(c_{ij})\ge0\), \(c_{ii}=0\), \(\operatorname{spr}(C)<1\), and assume
\[
\operatorname{TV}(\beta_i(\cdot\mid x_{-i}),\beta_i(\cdot\mid y_{-i}))
\le\sum_j c_{ij}1_{x_j\ne y_j}.
\]
Select coordinate \(i\) with \(p_i>0\), \(\sum_i p_i\le1\), using identity for the remaining probability. For weights \(w_i>0\), let \(E_w^2\) be optimal transport to \(\beta\) for cost \(\sum_iw_i1_{x_i\ne y_i}\). Put
\[
r_i(\mu)=\mathbb E_\mu\operatorname{TV}(\mu_i(\cdot\mid X_{-i}),\beta_i(\cdot\mid X_{-i})),
\quad \mathcal R_w^2=\sum_i p_iw_i r_i.
\]
Then
\[
E_w(\mu)^2\le w^T(I-C)^{-1}r(\mu)
\le\left(\max_i\frac{[w^T(I-C)^{-1}]_i}{p_iw_i}\right)\mathcal R_w(\mu)^2.
\tag{9.1}
\]
To verify it directly, couple the Gibbs chain using \(\mu\)'s full conditionals with the target Gibbs chain, using maximal conditional couplings. Both marginals remain fixed. A finite-state Cesàro limit supplies a stationary joint coupling. If \(d_i\) is its mismatch probability, its coordinate stationarity and the conditional triangle inequality imply
\(p_i d_i\le p_i(r_i+\sum_jc_{ij}d_j)\).
Cancel \(p_i>0\) and multiply by \((I-C)^{-1}\ge0\). Its cost gives (9.1), including laws \(\mu\) with zero atoms; their null-event conditionals have no marginal effect.

For convergence set \(B=I-D_p+D_pC\). The vector \(v=(I-C)^{-1}\boldsymbol1>0\) obeys \(Bv=v-D_p\boldsymbol1<v\), so \(\operatorname{spr}(B)<1\). Set
\(w^T=\boldsymbol1^T(I-B)^{-1}\) and
\(\theta=\max_j(w_j-1)/w_j<1\).
Then \(w^TB\le\theta w^T\). Shared maximal coupling of two target Gibbs chains gives mismatch update \(d^+\le Bd\), and thus
\(E_w(\mu P)\le\sqrt\theta E_w(\mu)\).
This produces explicit native coefficients but asserts no necessity of the Dobrushin bound and no novelty for its matrix comparison mechanism.

## 10. Evidence, limitations and manuscript use

### Materials read

- `output/ATTACK_MARKOV_SUBREG_NECESSITY_CONJECTURE.md`, including the countable-block construction.
- `output/AUDIT_MARKOV_COUNTEREXAMPLE.md`, including its completed extension audit and rate-compatibility corollary.
- `output/ATTACK_MARKOV_CONDITIONAL_REPAIR.md`.
- `output/AUDIT_MARKOV_CONDITIONAL_REPAIR.md`, including its sharper Gaussian EB proof.
- `upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md` in full, especially Sections 2–3 and the certificate-versus-actual-contraction separation.
- `output/MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md`, finite-polyhedral representation, native test, sharp vertex coefficient, and continuity proof.
- `output/AUDIT_STOCHASTIC_MASS_DILUTION_AND_MATCHING.md`, Sections 2–3 and 5.1, for the audited dilution assumptions and Pischke–Powell boundary.
- Pischke–Powell primary HTML: Definitions 3.4, 3.6, 4.2 and the retrieved Lemma 3.8 / Theorem 5.1 context, checked during this consolidation.

The upstream source records identify the original discrepancy and almost-firm scalar formula in [Hermer–Luke–Sturm](https://arxiv.org/html/2206.05213v3), the nonparacontractive necessity discussion in [Luke](https://link.springer.com/article/10.1007/s10107-024-02124-w), and the later assumption/conjecture discussion in [Luke–Schultze–Grubmüller](https://link.springer.com/article/10.1007/s10107-025-02319-9). Their prose questions are motivation; the precise implications refuted here are the displayed statements of this package. The existing conditional metric, Dobrushin comparison, Gaussian scan geometry, and weak-Poincaré overlaps are documented in the two conditional-repair files. Apart from the targeted comparison above, this task relies on those supplied source audits and does not claim a new full-text priority audit.

### Executed local verification

The following scripts were rerun for this consolidation; their analytic arguments, not numerical prefixes, establish the infinite-family theorems:

```text
python3 output/audit_markov_counterexample_exact.py
python3 output/audit_markov_extensions_exact.py
python3 output/verify_markov_conditional_repair_independent.py
python3 output/verify_finite_state_ot_strictness.py
```

The first two runs completed with their respective `ALL INDEPENDENT EXACT CHECKS PASSED` and `ALL INDEPENDENT EXTENSION CHECKS PASSED` messages. The third completed with `ALL INDEPENDENT AUDIT CHECKS PASSED`, including 165 binary-simplex laws, interacting Gibbs, coupled Gaussian, and actual-map expected-energy checks. The fourth checked all 35 exact subdivision vertices and returned squared coefficient 26 at its \(p=1/2\) normalization, hence \(13/p\) by exact scaling. A separate exact `Fraction` calculation checked all six active excess factors in the small-\(p\) four-cycle variant. No experiment or worldwide novelty verification is inferred from these computations.

### Repairs made in the formalization

- A wrong-zero-set failure and a genuine exact-zero subregularity failure receive different theorems.
- A finite-state theorem gives exact native decidability and the sharp coefficient, not merely existence of an unspecified EB.
- The four-cycle verifier witness uses small refresh probability when the \(\varepsilon_f<1\) source range is required.
- Global transport decoupling is proved by source/destination dual potentials on \(G\times S\), including every cross-block pair.
- Infimum attainment precedes the exact-zero proof.
- “No rate-compatible gauge” is restricted to fixed valid parameters and the explicit formula (4.20).
- The compactness majorant is constructed with intervalwise domination, not assumed continuous by assertion.
- Binary sharpness keeps all-initial-law quantifiers, a fixed conserved marginal, and the specified conditional metric.
- The Gaussian EB uses the independently audited sharp coefficient; contraction sharpness is not deduced from EB sharpness.
- Conditional law-space length is distinguished from stochastic sample-path length.
- A conditional residual is never substituted for an unmatched synchronous RL defect.
- The connection to RL is a matched-certificate interface and an information-loss warning, not a claimed nonlinear-RL exclusive application.
- The mass-dilution obstruction retains common-support separation, stationarity-vanishing residuals, moment orders, and mixture-rich law-domain quantifiers.
- Pischke–Powell's general stochastic regularity, moving anchors, and stochastic PPA results are retained as substantive prior scope.

### Remaining editorial and research risks

The mathematical statements here are suitable for independent line-by-line review. Their novelty is not thereby established. A journal assessment must compare the exact source-discrepancy obstruction and countable construction against prior counterexamples, and compare the Gaussian EB with corrected conditional-transport/tensorization literature. The scalar nonuniform profile and the Dobrushin supplement are established-type mechanisms. The original prose question has several possible rate/domain interpretations; a title or abstract must name the exact discrepancy and exact conclusion instead of announcing an unrestricted resolution. No new figure is needed for this theorem package, and none was generated.

The defensible central theorem narrative is: **the original invariant transport discrepancy has an exact finite-state native verifier, but infinite compact state spaces admit exact-zero, geometrically convergent counterexamples to every positive-Hölder EB. Identification, modulus existence, and rate compatibility are separate questions. Conditional specifications can recover a certificate, at the explicitly stated cost of a stronger transport restriction.**

## 11. Expert return contract

```yaml
contract_version: "1.0"
expert_skill: sci-skills-manuscript-writing
project_id: null
paper_family: null
stage_id: null
task_id: markov_paper_formalization
task_status: COMPLETE
inputs_reviewed:
  - output/ATTACK_MARKOV_SUBREG_NECESSITY_CONJECTURE.md
  - output/AUDIT_MARKOV_COUNTEREXAMPLE.md
  - output/ATTACK_MARKOV_CONDITIONAL_REPAIR.md
  - output/AUDIT_MARKOV_CONDITIONAL_REPAIR.md
  - upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md
  - output/MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md
  - output/AUDIT_STOCHASTIC_MASS_DILUTION_AND_MATCHING.md, Sections 2-3 and 5.1
  - Pischke-Powell arXiv 2605.06129v1, specified primary-text sections
outputs:
  - output/MARKOV_PAPER_THEOREM_PACKAGE.md
evidence_status:
  - VERIFIED_USER_MATERIAL: the five required proof-bearing inputs were reviewed
  - AI_INFERENCE: self-contained proofs and exact statement consolidation
  - EXECUTED_LOCAL: four verification scripts rerun and exact four-cycle energy calculation
  - VERIFIED_SOURCE: targeted Pischke-Powell definition and theorem-scope check
  - PENDING_VERIFICATION: global priority and submission-level final audit
assumptions:
  - The original discrepancy keeps optimal full-cost couplings and shared update noise.
  - Conditional-metric theorems freeze the conserved marginal.
  - Rate-compatible means compatibility with the explicit fixed-parameter scalar formula.
  - Gaussian and ordinary joint Wasserstein claims require finite second moments.
author_input_needed: []
manual_actions: []
quality_checks:
  - Every requested theorem family has a precise statement and proof.
  - Identification, true zero-set regularity, and scalar rate compatibility are separated.
  - Countable transport and minimum-attainment arguments are explicit.
  - Existing positive mechanisms and topology changes remain visible.
  - No journal acceptance, blanket priority, or nonlinear-RL exclusivity is claimed.
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: Independently audit the final theorem statements and their nearest-prior scope before extracting a submission abstract.
stage_acceptance_recommendation: PASS_CANDIDATE
```

**One primary next action:** independently audit this consolidated theorem package and its nearest-prior scope before extracting a submission abstract.
