# C273 development and exact-object novelty review

Review date: 2026-10-13. Scope: `research/canonical/native_gram_structural.md`, C273-v1, NG1–NG28 and its eventual-ABS section. No canonical text, manuscript, Git state, or authentication was changed in this subtask. This report separates primary-paper facts, exact mathematical mappings, and novelty judgments. A bounded search does not establish public priority.

## Verdict

C273 is a rigorously checked **specific structural example with sharp regularity and certificate boundaries**. Its strongest still-unmatched component in the inspected primary literature is the exact all-input, fixed-solution exponent $2/3$ for the *composition* $(v+\lambda F_c)^{-1}v$ at $[c\ 0]$, together with its explicit noncalm witness and the uniform-neighborhood original-objective H1 obstruction. I did not find that exact combination already stated for the same native, unshifted Gram kernel and nonzero partial-column regression.

This does **not** presently support calling C273 a substantial new general convergence theorem, a new Gram geometry, a new fractional-root mechanism, or a new matrix-recovery application. General Bregman theory already gives its whole-orbit convergence; an exact ordinary dual PPA recovers its quantitative finite length. Matrix Schatten mirrors, affine observation sets, and Bregman-projection implicit bias are established ingredients. The application is a transparent diagnostic model; its loss already has a globally Lipschitz gradient and the observed column has the trivial exact optimizer $a=c$. No practical improvement over ordinary quadratic PPA has been demonstrated.

## Exact object and the claim that must be compared

For $m\ge2$, $c\ne0$, and fixed $\lambda>0$,

\[
f_c([a\ b])=\tfrac12\|a-c\|^2,
\quad h(Z)=\tfrac14\|Z\|_{S,4}^4,
\quad v(Z)=ZZ^TZ,
\quad S_c=\{[c\ b]\}.
\]

The complete implicit algorithm has a unique root for every input. The kernel acts on raw $Z$, not on $[a-c\ b]$. At the fixed solution $p=[c\ 0]$, C273 proves

\[
\|T(Z)-p\|\le C\|Z-p\|^{2/3}
\]

for every nearby input. Its sharp family $Z_t=[C n+t w\quad t n]$, $C=\|c\|$, $w\perp n$, gives

\[
\beta_\perp\sim\left(\frac{C\lambda}{C^2+\lambda}\right)^{1/3}t^{2/3}w,
\quad f_c(Z_t)-f_c(TZ_t)=\Theta(t^2),
\quad\|TZ_t-Z_t\|^2=\Theta(t^{4/3}).
\]

The exponent is pointwise at a fixed solution. It is not a two-input exponent, a uniform constant over all $S_c$, or an exact convergence order for every orbit. H1 fails as a uniform full-neighborhood contract at $p$; every individual orbit nevertheless admits eventual original-$f_c$ H1/H2 constants.

## Development of the field and strongest exact comparisons

The relevant development is not a progression from “old methods require a positive quadratic kernel” to “RLEB first allows flat kernels.” Convex Bregman monotonicity predates modern relative-smoothness analyses and does not require that quadratic lower bound. Modern Gram kernels were developed for quartic factorized objectives and computationally useful forward steps. Their positive quadratic terms address both relative-smoothness and conditioning. C273 instead puts an elementary quadratic loss in the implicit proximal term and isolates what removing quadratic kernel curvature does to the physical update map.

| Primary source and exact locator | Established result | Exact C273 relation |
|---|---|---|
| Bauschke–Borwein–Combettes, *Bregman Monotone Optimization Algorithms*, SIAM JCO 42(2), 596–636 (2003), DOI [10.1137/S0363012902407120](https://doi.org/10.1137/S0363012902407120). [Author full text](https://pcombet.math.ncsu.edu/sicon2.pdf), Definition 3.1, Example 4.6, Algorithm 4.12, Proposition 4.13, Theorem 4.14, author-PDF pp. 6, 20, 22. | Bounded class-$\mathcal B$ orbits converge under strict kernel convexity, cluster-point stationarity and Bregman consistency. Positive strong convexity is not required. | All hypotheses pass. The exact mapping below supplies boundedness and stationarity. This already gives whole-orbit convergence for all inputs and all fixed $\lambda>0$, but the theorem itself does not supply C273's finite length or rate. |
| Carlen–Lieb, *Optimal Hypercontractivity for Fermi Fields and Related Non-commutative Integration Inequalities*, [arXiv:hep-th/9209053v1](https://arxiv.org/pdf/hep-th/9209053), 15 Sep 1992; Commun. Math. Phys. 155, 27–46 (1993), Appendix Theorem 6 and (A.5). | The normalized Schatten-$p$ gradient is locally $(p-1)$-Hölder for $1<p\le2$ away from the zero matrix, without a full-rank assumption. Trace Clarkson gives power-$p$ uniform convexity for $p\ge2$. | At $p=4/3$, transposition and a locally Lipschitz norm factor yield cube-root inverse $1/3$ behavior near nonzero rank-deficient matrices. Even nonzero rank-deficiency inverse regularity predates Ricard. Neither source analyzes C273's partial-loss composition. |
| Éric Ricard, *Hölder estimates for the noncommutative Mazur maps*, [arXiv:1407.8334v3](https://arxiv.org/pdf/1407.8334v3), 5 Nov 2014, unnumbered main theorem p. 1; published Archiv der Mathematik 104, 37–45 (2015), DOI 10.1007/s00013-014-0710-9. | $M_{p,q}(x)=x|x|^{(p-q)/q}$ is $\min(p/q,1)$-Hölder on unit balls for $1\le p,q<\infty$. | $v=M_{4,4/3}$ and $v^{-1}=M_{4/3,4}$, using rectangular corner/block embedding. Generic inverse exponent $1/3$ is old. The theorem does not give the improved $2/3$ exponent of the partially regularized composition. |
| Dragomir–d'Aspremont–Bolte, *Quartic First-Order Methods for Low-Rank Minimization*, [arXiv:1901.10791v3](https://arxiv.org/pdf/1901.10791v3), header 17 Feb 2021; manuscript last revised 18 Jan 2021; DOI [10.1007/s10957-021-01820-3](https://doi.org/10.1007/s10957-021-01820-3). Eq. (10), Proposition 2.4, Theorem 3.1. | Gram kernels combine norm/Gram quartics with $\sigma\|Z\|^2/2$, $\sigma>0$; the iteration linearizes the smooth loss; convergence assumes strong kernel convexity and a coercive semialgebraic objective. | Gives the actual Gram-kernel and low-rank factorization motivation. Its $\sigma>0$ and forward iteration are different from C273. C273 has neither a low-rank constraint nor a factorized recovery objective, so this background cannot confer an established recovery benefit. |
| Laude–Ochs–Cremers, *Bregman Proximal Mappings and Bregman–Moreau Envelopes under Relative Prox-Regularity*, [arXiv:1907.04306](https://arxiv.org/pdf/1907.04306), Definition 2.3, Corollary 3.23. | The local Lipschitz prox corollary requires a Legendre supercoercive kernel that is $C^2$ with positive definite Hessian at every interior point, suitable prox-regular/prox-bounded objective, and sufficiently small step. | Pure Gram fails the Hessian condition at $[c\ 0]$ in directions $[0\ w]$, $w\perp c$. This corollary does not cover the sharp C273 effect; failure of its premise does not itself prove novelty. |
| Akhtiamov–Ghane–Pooladzandi–Hassibi, *Implicit Bias and Convergence of Matrix Stochastic Mirror Descent*, [arXiv:2602.18997v2](https://arxiv.org/pdf/2602.18997), 27 Feb 2026, DOI 10.48550/arXiv.2602.18997, Eq. (2), Assumptions 1, Theorem 1, Example 3. | Underdetermined matrix observations, matrix mirror descent, and initial-point Bregman-projection bias; theorem assumes a positive strong-convexity constant and convexity of $\psi-\eta L_t$. The $p\ge2$ example adds a positive Frobenius quadratic to the Schatten power. | Close application ingredients are established. The forward stochastic algorithm and positive quadratic term do not equal C273. Pure Gram also makes $h-\eta f_c$ fail convexity at the origin for every $\eta>0$. |

Each row is based on the primary full text, not a search-snippet theorem import. Ricard's published DOI was identified from metadata; its Springer endpoint was inaccessible, so the reviewed mathematical version is explicitly the arXiv v3.

### Complete mapping into BBC 2003

This is this review's exact mapping, not a claim that BBC printed C273's regression example. Their kernel is $h$, target is $S_c$, and operator is the full $T$ of C273. For every $s\in S_c$, $Y=T(Z)$,

\[
\langle s-Y,v(Z)-v(Y)\rangle=-\lambda\|\alpha-c\|^2\le0.
\]

Hence $T\in\mathcal B$ and its Bregman monotonicity yields

\[
D_h(s,Z_{k+1})+D_h(Z_{k+1},Z_k)\le D_h(s,Z_k).
\]

Homogeneity gives $D_h(s,Z)=h(s)+3h(Z)-\langle v(Z),s\rangle$, which is coercive in $Z$. Thus the orbit is bounded. C273's global quartic Bregman lower bound makes physical steps tend to zero; bounded-set Lipschitz continuity of $v$ and the full equation force $a_{k+1}-c\to0$. Every cluster point lies in $S_c$. Convex $S_c$, strict $h$, and continuous finite-dimensional $v$ supply Example 4.6's uniqueness condition; the same quartic bound supplies consistency. Finite-dimensional compactness supplies a strong cluster point. Theorem 4.14 therefore applies directly.

## Exact ordinary dual PPA recovery of the quantitative conclusion

This is a self-contained classical recovery, beyond merely saying the proof “resembles” a dual argument. The conjugate and its gradient are

\[
h^*(W)=\tfrac34\operatorname{tr}((W^TW)^{2/3}),\qquad
\nabla h^*(W)=v^{-1}(W).
\]

The SVD calculation is immediate: maximize $\sum_i\sigma_i(W)s_i-s_i^4/4$ over $s_i\ge0$, giving $s_i=\sigma_i(W)^{1/3}$ and value $3\sigma_i(W)^{4/3}/4$.

The second gradient column $k_0$ is conserved. Define the finite $C^1$, strictly convex coercive function

\[
\psi_{k_0}(u)=h^*([u\ k_0])-\langle c,u\rangle.
\]

Then NG3 is equivalent, in both directions, to the ordinary Euclidean PPA

\[
u_k-u_{k+1}=\lambda\nabla\psi_{k_0}(u_{k+1}).
\]

Its unique minimizer $u_*$ corresponds to $[c\ b_*]$ with $cc^Tb_*+\|b_*\|^2b_*=k_0$. Firmness bounds the whole dual orbit by $\|u-u_*\|\le D_0$. Every inverse image of this *entire dual ball* has primal norm at most $M_*=(2Q)^{1/3}$, where $Q$ is NG27's bound. On the primal ball, $0\preceq D^2h\preceq L_*I$. A secant-matrix argument gives

\[
\|v(Z)-v(Z')\|^2\le L_*\langle v(Z)-v(Z'),Z-Z'\rangle.
\]

For equal $k_0$, this is strong monotonicity of $\nabla\psi_{k_0}$ with modulus $1/L_*$ on the dual ball. Ordinary strong-monotonicity PPA therefore gives $\rho=L_* /(L_*+\lambda)$; the old/global physical inverse estimate supplies the $\rho^{k/3}$ physical tail and finite-length sum NG28. Thus even the quantitative global positive is an exact ordinary-PPA specialization with a known power inverse lift, rather than an exclusive RLEB phenomenon.

The limit is also exactly the Bregman projection of the initial state onto the affine target:

\[
Z_*=\operatorname{argmin}_{Z\in S_c}D_h(Z,Z_0),
\]

whose unconstrained $b$ stationarity is precisely NG26. C273's formula is an explicit readout of this established selection mechanism.

## Fractional singularity mechanism: old method, unmatched precise realization

Avrachenkov–Ejov–Filar, *On Newton's polygons, Gröbner bases and series expansions of perturbed polynomial programs*, Banach Center Publications 71 (2006), 29–38, DOI [10.4064/bc71-0-2](https://doi.org/10.4064/bc71-0-2), was read through the [official ten-page full text](https://www.impan.pl/shop/en/publication/transaction/download/product/86491). Section 2, equations (4)–(6), already constructs quartic-program stationary coordinates with leading perturbation powers $1/3$ and $2/3$. Its later sections analyze polynomial branches with Newton polygons. This is a different parametric objective and is not an exact prior theorem for the convex native-Gram prox.

**Interpretation:** C273's transverse equation is the elementary dominant balance $D^3\sim Ct^2$. The fractional power is not a newly discovered singularity mechanism. The all-input $2/3$ upper bound uses a more specific fact, namely that the conserved block perpendicular to $c$ has only quadratic input size and the normal residual has linear input size. Generic Puiseux existence or generic cube-inverse Hölder continuity does not automatically prove that uniform upper bound. The contribution, if publicly unmatched, lies in establishing this precise composition/anchor cancellation and its algorithmic consequences.

Marcus Carlsson, [*Perturbation theory for matrix square root and matrix modulus*, arXiv:1810.01464](https://arxiv.org/pdf/1810.01464), Section 3, Theorem 3.1, gives rank-sensitive power expansions in terms of a kernel Schur-complement root for PSD perturbations and $1<p<3$. The cube-root endpoint $p=3$ is excluded and expressly left for further analysis. It corroborates that rank-sensitive root geometry is a developed subject, but does not cover C273's nonspectral partially regularized composition. Likewise Ding–Sun–Sun–Toh, [arXiv:1810.09856](https://arxiv.org/pdf/1810.09856), Theorem 5, transfers local Lipschitz regularity between spectral operators and their singular-value maps; C273's first-column projection breaks the symmetry needed for that direct theorem.

Penz–Laestadius, [*Adaptation of Moreau–Yosida regularization to the modulus of convexity*, arXiv:2504.01772v2](https://arxiv.org/pdf/2504.01772), 13 Aug 2025, Theorem 6.1 and Corollary 6.3, provide generalized power-Moreau conjugacy and $(p-1)$-Hölder gradients in strictly convex $p$-smooth spaces, $p\le2$. There is an exact algebraic identification here: with $G=h+\lambda f_c$,

\[
G^*=(\lambda f_c)^*\square h^*,\qquad
(\lambda f_c)^*([u\ k])=\langle c,u\rangle+\frac{\|u\|^2}{2\lambda}+\delta_{\{0\}}(k).
\]

Taking the dual Schatten-$4/3$ norm makes $h^*$ the $p=4/3$ power-Moreau kernel. Schatten-$4/3$ smoothness follows by duality from Schatten-$4$ power convexity; the trace Clarkson estimate is explicitly present in Carlen–Lieb's Appendix (A.5), while power-convexity/smoothness duality is Proposition 2.5 in Penz–Laestadius. Thus this gives a direct general prior for the partially regularized inverse's $1/3$ gradient estimate as well. Its conclusion concerns $\nabla G^*$, not the improved fixed-solution exponent of $\nabla G^*\circ v$.

The inverse itself has a sharp $1/3$ defect at the nonzero dual point $Q_0=v([c\ 0])$: for unit $w\perp c$ and $s>0$,

\[
(v+\lambda F_c)([c\ s^{1/3}w])=[\|c\|^2c\quad s w].
\]

This elementary specialization separates the old/generic inverse singularity from the composition's improved $2/3$ input exponent.

## Value and positioning after learning the development

The example should be retained because it answers a concrete structural question accurately: removing the quadratic Gram term can produce a noncalm physical update at a genuine nonzero-data solution even though the objective is quadratic, convex, and has an exact linear true residual error bound. The uniform-neighborhood H1 failure has a clean explanation: loss decrease has order $t^2$, while invisible/free-column drift has order $t^{2/3}$ and its squared norm has order $t^{4/3}$.

Its convergence claim should be presented with BBC and the ordinary dual PPA side by side. Its selected-limit formula should be presented as Bregman-projection readout. Its practical role is a stress test of degenerate coupled geometry, not evidence for faster regression or a solved low-rank recovery problem. Its global inverse exponent should not be promoted to a novelty claim. The eventual-ABS positive must remain visible; omitting it would exaggerate the significance of the H1 witness.

A stronger general contribution would require a theorem that determines sharp physical regularity from the rank of a general observation map and the first surviving mixed kernel terms, with a uniform all-output proof across a meaningful family. C273 supplies one useful nontrivial instance for such a program; it does not presently prove that general theorem. This is an evaluation of its present scope, not an additional claim or completed extension.

## Search and verification limits

Searches covered pure Gram/Schatten quartic kernels, matrix cube/Mazur inverses, partial-observation regularization, Bregman proximal regularity, rank-sensitive matrix power perturbation, polynomial-program Puiseux sensitivity, and matrix mirror implicit bias. No exact prior for the same $T$, fixed anchor $[c\ 0]$, and sharp all-input $2/3$ theorem was located. That negative search result supports only “not found in the inspected primary literature,” not “first published.”

No full copyrighted paper was saved to the repository. The mathematical sources are primary author/publisher/arXiv full texts linked above. The direct Springer's Ricard DOI endpoint failed; arXiv v3 was read. The root agent must reopen any primary source it cites in a user-facing answer. Public-priority certification and a broad bibliographic saturation search remain unfinished.
