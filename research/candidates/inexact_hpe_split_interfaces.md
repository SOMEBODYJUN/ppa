# Inexact, extragradient, relaxation and splitting interfaces for RLEB

Date: 2026-10-13. This is a scoped candidate report, not a canonical claim or a priority certificate. It uses the repository mathematics-review mode, C249-v1, and the latest F86–F91/2026-10-13 novelty boundaries. No manuscript, ledger, canonical definition or graph is changed.

The main migration should remain the **uncorrected real-graph inexact PPA with computable gauge forcing**, not an HPE or splitting wrapper. The additional anisotropic HPE bridge below isolates why a scalar Euclidean relative-error test can fail when tangential movement is larger than distance to the zero set. It is implementable and controls all accepted outputs. Its scalar monotone reduction gives a short classical proof, so it is a subordinate mechanism example rather than evidence of a high-value application or an independent new convergence principle.

## 1. Freeze the states and residuals

Let $X=\mathbb R^n$, $F:X\rightrightarrows X$, $S=F^{-1}(0)$ nonempty and closed, $\lambda>0$, and $r_F(y)=\inf\{\|w\|:w\in F(y)\}$. Empty fibers have residual $+\infty$. A real-graph inexact proximal triple is

\[
w\in F(y),\qquad e=\lambda w+y-x.
\tag{1}
\]

There are two different next states:

\[
\text{inexact PPA: }x^+=y,\qquad
\text{real-graph HPE: }x^+=x-\lambda w=y-e.
\tag{2}
\]

The true-residual estimate from (1) is only $r_F(y)\le\|w\|$. It gives no direct upper bound for $r_F(x^+)$ in the HPE algorithm. An endpoint error bound at $y$ must therefore be followed by a distance transfer to $y-e$, or a separate true-graph bridge at $x^+$.

The BIS enlargement for a maximal monotone operator is also a different object. From $w\in F^\varepsilon(y)$ one cannot write $r_F(y)\le\|w\|$. For a general nonmonotone $F$, even the standard zero-enlargement identity $F^0=F$ is unavailable. This report uses real graph points; it does not import an enlargement residual as the true residual.

### Primary-source boundary

Solodov–Svaiter, *A Hybrid Approximate Extragradient–Proximal Point Algorithm Using the Enlargement of a Maximal Monotone Operator*, Set-Valued Analysis 7 (1999), 323–345, [author PDF](https://pages.cs.wisc.edu/~solodov/solsva99Teps.pdf), Definition 2.1 and Algorithm 3.1, pp.329 and 331–332, use

\[
w\in T^\varepsilon(y),\quad
\|\lambda w+y-x\|^2+2\lambda\varepsilon
 \le\sigma^2\|y-x\|^2,
\quad x^+=x-\lambda w.
\tag{3}
\]

Their Theorem 3.1 is a monotone global convergence result. The rotation example immediately preceding it demonstrates that the correction in (3) is essential: keeping their accepted intermediate point as the next state is not their algorithm and can diverge.

Combettes–Pennanen, *Proximal Methods for Cohypomonotone Operators* (2004), [author PDF](https://pcombet.math.ncsu.edu/sicon3.pdf), Algorithm 1.1, Definitions 2.1–2.2, Lemma 2.4 and Theorem 3.1, already treat local inexact relaxed nonmonotone proximal iterations. Their operator inverse admits a localized maximal hypomonotone extension; their two errors satisfy summability and a localization budget. Lemma 2.4 reduces a suitable relaxed resolvent to a maximal monotone resolvent. Thus “inexact + relaxed + nonmonotone” alone is not a novelty claim.

Buscaglia–Lotito–Parente–Solodov, *A General Framework for Symmetric and Asymmetric Variable Metric Proximal Point Methods, with Relations between Relative-Errors and Summable-Errors*, [author manuscript](https://pages.cs.wisc.edu/~solodov/blps24VMprox.pdf), dated August 8, 2025, was inspected at §§1–2, Algorithm 4.1, Theorems 4.3–4.4, and §5/Theorem 5.1. Algorithm 4.1 uses maximal monotone $T$, uniformly bounded positive metrics and a hybrid correction. Theorem 5.1 nevertheless reproduces every sufficiently late uncorrected monotone-PPA orbit satisfying its summable-relative output criterion through asymmetric metrics. Thus different update formulas alone do not exclude this framework.

### Main-route evaluator: nonlinear gauge stopping and the modern overlap

Here is a self-contained sufficient interface for the proposed main route. On the same certified perturbed-input collar, assume every complete exact output $y\in J_{\lambda F}(q)$ has a selected real graph value $w=(q-y)/\lambda$ with

\[
\lambda\|w\|\le B(d(q,S)),\qquad
d(y,S)\le\psi(r_F(y)),\qquad
\psi(B(t)/\lambda)\le\kappa_0t,
\quad 0<\kappa_0<1.
\tag{M1}
\]

The same true-residual evaluation cap and complete-output localization must hold at every accepted $q,y$. Accept real triples (1) under the computable selected-value criterion

\[
\|e\|\le\eta\psi(\|w\|),\qquad x^+=y,
\quad 0\le\eta<\frac{1-\kappa_0}{\kappa_0}.
\tag{M2}
\]

Since $q=x+e$ and $r_F(y)\le\|w\|$, monotonicity of $\psi$ gives $\|e\|\le\eta\kappa_0d(q,S)$ and

\[
d(q,S)\le\frac{d(x,S)}{1-\eta\kappa_0},
\qquad
d(x^+,S)\le\frac{\kappa_0}{1-\eta\kappa_0}d(x,S).
\tag{M3}
\]

The actual uncorrected physical step obeys

\[
\|y-x\|\le
B\left(\frac{d(x,S)}{1-\eta\kappa_0}\right)
 +\frac{\eta\kappa_0}{1-\eta\kappa_0}d(x,S).
\tag{M4}
\]

Summability of that modulus on the new geometric scale supplies the physical length/retention budget. Exact triples supply coverage. The selected value in (M2) is observable; it is not asserted to equal the true residual. The contraction proof uses the valid upper-bound direction $r_F(y)\le\|w\|$.

The modern monotone overlap is substantial. Suppose $\psi(r)\le Cr^p$, $p>1$, the already proved main contraction yields $\|w_k\|\le C_1 Q^{k\gamma}$ for some $\gamma>0$, and the same algorithm has $F$ maximal monotone. Eventually $\|e_k\|\le\lambda\|w_k\|/2$, so

\[
\frac{\|e_k\|}{\|y_k-x_k\|}
\le\frac{2\eta C}{\lambda}\|w_k\|^{p-1},
\qquad
\sum_k\frac{\|e_k\|}{\|y_k-x_k\|}<\infty.
\tag{M5}
\]

For this monotone specialization, nonexpansivity gives
$\|y_k-J_{\lambda F}x_k\|\le\|e_k\|$ because $y_k=J_{\lambda F}(x_k+e_k)$. Hence its orbit satisfies the summable-relative output condition used in the modern representation theorem. This is our deduction from its stated criterion, not a source claim about nonmonotone gauge forcing. It is a posteriori when the main contraction was needed to establish (M5); it does not prove that the old paper had already certified the nonmonotone application.

The translated noncalm complete graph chosen for the main paper fails the source's maximal-monotone input and also fails finite local inverse hypomonotonicity. Those are useful exact input boundaries. A blanket exclusion of nonlinear coordinate changes, tailored variable metrics, all monotone lifts, or all classical scalar reductions is not established here. In particular, the power-gauge test itself can be a stricter stopping rule inside an older algorithm when the older operator conditions hold.

A slightly stronger fixed-linear boundary is elementary. For the translated template $F(s,t)=(-c|t|^\gamma,Dt)$, $c,D>0$, $0<\gamma<1$, no constant invertible matrix $M$ makes $MF$ monotone on an open rectangle about a zero-line point. Compare $(s,t)$ with $(s\pm h,0)$, where $h>0$ is fixed small. In the monotonicity pairing, the term $\mp hM_{11}c|t|^\gamma$ first forces $M_{11}=0$, because it dominates the terms of order $|t|^{\gamma+1}$ and $t^2$. The remaining term $\pm hM_{12}Dt$ then forces $M_{12}=0$, since it dominates those same higher powers. The first row would vanish. This excludes a fixed invertible codomain multiplication of the native graph; it does not address state-dependent metrics or nonlinear/product representations.

## 2. Option A: ordinary real-graph HPE, under a linear physical-step bridge

This is a proved conditional bridge from an **existing exact** physical certificate, not a new algorithmic framework.

Assume that, on one certified perturbed-input collar $V$, every complete exact output $y\in J_{\lambda F}(q)$ satisfies

\[
d(y,S)\le\kappa d(q,S),\qquad
\|y-q\|\le C d(q,S),
\quad 0<\kappa<1,
\tag{4}
\]

and those fibers are nonempty. Consider all triples (1) with

\[
q=x+e\in V,
\qquad \|e\|\le\sigma\|y-x\|,
\qquad x^+=x-\lambda w.
\tag{5}
\]

The collar requirement is part of the accepted relation. It cannot be deleted and then recovered by an infinite-orbit argument. Exact triples ($e=0$) give coverage whenever $x\in V$. Set

\[
\alpha=\frac{\sigma}{1-\sigma},\qquad b=\alpha C.
\]

Since $y\in J_{\lambda F}(q)$, the relative test and (4) give

\[
\|e\|\le\sigma(\|y-q\|+\|e\|)
 \le\sigma(Cd(q,S)+\|e\|),
\quad \|e\|\le b\,d(q,S).
\]

If $b<1$, then $d(q,S)\le d(x,S)+\|e\|$ yields

\[
d(q,S)\le\frac{d(x,S)}{1-b},\qquad
\|e\|\le\frac b{1-b}d(x,S).
\tag{6}
\]

Consequently, the actual corrected state has

\[
d(x^+,S)\le d(y,S)+\|e\|
 \le\frac{\kappa+b}{1-b}d(x,S),
\qquad
\|x^+-x\|=\|y-q\|
 \le\frac C{1-b}d(x,S).
\tag{7}
\]

The factor $Q=(\kappa+b)/(1-b)$ is below one if

\[
b<\frac{1-\kappa}{2},
\quad\text{equivalently}\quad
\sigma<\frac{1-\kappa}{2C+1-\kappa}.
\tag{8}
\]

This controls every accepted triple. The finite length and tail are bounded by

\[
\Theta_A(t)=\frac{Ct}{(1-b)(1-Q)}.
\tag{9}
\]

For an open certified state domain $U$, the strict budget $\Theta_A(d(x^0,S))<d(x^0,X\setminus U)$ supplies finite-prefix retention, provided (4)–(5) and exact coverage are available at every retained input. This is the same induction used in C249; closure of $S$ identifies the Cauchy limit. For $x\in S$, (6) forces $e=0$, and (4) forces $y=x$. Thus the complete accepted relation absorbs $S$, and its fixed set is $S$ when the full-zero target is used.

**Limit.** C249 allows $\|y-q\|\asymp d(q,S)^\gamma$ with $\gamma<1$. The proof above requires a uniform linear physical-step bound and does not cover those noncalm examples. Replacing $C d(q,S)$ by an arbitrary sublinear modulus does not preserve the absorption argument.

## 3. Option B: anisotropic real-graph HPE for a genuinely nonmonotone model

### Complete operator and exact PPA

Fix $0<g<p<1$ and define the continuous, single-valued, full operator on $\mathbb R^2$ by

\[
F(u,z)=\bigl(f(u),h(u)\bigr),\qquad
f(u)=\operatorname{sgn}(u)|u|^p,\quad
h(u)=\operatorname{sgn}(u)|u|^g,
\tag{10}
\]

where both functions vanish at zero. Its exact full zero set is $S=\{0\}\times\mathbb R$. Its true residual is

\[
r_F(u,z)=\sqrt{|u|^{2p}+|u|^{2g}},\qquad
d((u,z),S)=|u|\le r_F(u,z)^{1/g}.
\tag{11}
\]

For input $x=(a,b)$ the exact complete resolvent is unique: $u+\lambda f(u)=a$ is a strictly increasing onto scalar equation and

\[
J_{\lambda F}(a,b)=\bigl(u,b-\lambda h(u)\bigr).
\tag{12}
\]

Writing $t=|a|$ gives $|u|\le(t/\lambda)^{1/p}$ and $|u|\le t$. With $\beta=g/p\in(0,1)$, the nearest input zero is $(0,b)$, and

\[
\|2J_{\lambda F}x-x-(0,b)\|
 \le t+2\lambda^{1-\beta}t^\beta,
\quad
\|J_{\lambda F}x-x\|
 \le t+\lambda^{1-\beta}t^\beta.
\tag{13}
\]

Equations (11)–(13), exact coverage and a sufficiently small cap give a complete ordinary C249 certificate: $v=I$, $a(t)=t$, $\omega(t)=t+2\lambda^{1-\beta}t^\beta$, $K(t)=t+\lambda^{1-\beta}t^\beta$, $h_0(t,s)=s$, $\psi(s)=s^{1/g}$. Indeed $\psi(K(t)/\lambda)/t=O(t^{1/p-1})\to0$. The geometric physical tail converges because $\beta>0$.

The operator is genuinely nonmonotone and is not locally inverse-hypomonotone on any open graph collar containing a segment of $S$. For $y_1=(t,-c)$, $y_2=(0,0)$ with fixed small $c>0$ and $t\downarrow0$,

\[
\frac{\langle F(y_1)-F(y_2),y_1-y_2\rangle}
 {\|F(y_1)-F(y_2)\|^2}
=\frac{t^{p+1}-ct^g}{t^{2p}+t^{2g}}\longrightarrow-\infty.
\tag{14}
\]

Every finite co-hypomonotonicity constant is therefore excluded on that complete local graph. This is a precise exclusion of the Combettes–Pennanen input property, not an exclusion of all classical analysis or all representations.

### Why the ordinary HPE test fails

Take $x=(0,b)\in S$, $u>0$, $y=(u,b-\lambda u^g)$, and $w=F(y)$. The real proximal equation error is

\[
e=(u+\lambda u^p,0).
\]

For every fixed $\sigma>0$, $\|e\|\le\sigma\|y-x\|$ holds for all sufficiently small positive $u$, because $g<p$. Yet

\[
x^+=x-\lambda w=(-\lambda u^p,b-\lambda u^g)\notin S.
\tag{15}
\]

All witnesses and outputs can be arbitrarily close to the initial zero. Thus no shrinking of a local Euclidean collar repairs zero absorption for the full accepted HPE relation. In particular, a C249-style length budget with $\Theta(0)=0$ cannot hold. This is stronger than a failure to optimize constants; it is a legal real-graph accepted transition from a zero.

### Implementable corrected algorithm

Choose $0\le\sigma\le\bar\sigma<1$. Given $x=(a,b)$:

1. Find **any** $u\in\mathbb R$ satisfying the scalar computable test

   \[
   |\lambda f(u)+u-a|\le\sigma|u-a|.
   \tag{16}
   \]

2. Set $y=(u,b-\lambda h(u))$, $w=F(y)$ and $e=(\lambda f(u)+u-a,0)$.
3. Perform the actual HPE correction $x^+=(a-\lambda f(u),b-\lambda h(u))$.

The scalar exact root always passes, so the accepted relation is nonempty at every input. Bisection of $u+\lambda f(u)=a$ produces a passing nonexact root for any $\sigma>0$ after finitely many iterations when $a\ne0$; at $a=0$ the exact root is known. The test uses the known normal coordinate. It imposes stricter accuracy in the normal direction than an isotropic physical-step test; it does not assert that $d(x,S)$ is available for arbitrary unknown zero sets.

### All accepted outputs, actual endpoint, and finite length

Suppose $a>0$. Equation (16) excludes $u\le0$ and $u\ge a$ unless the zero case applies, since those cases have $|\lambda f(u)+u-a|>|u-a|$. Thus $0<u<a$, and

\[
(1-\sigma)(a-u)\le\lambda u^p
 \le(1+\sigma)(a-u).
\tag{17}
\]

Hence $u\le((1+\bar\sigma)a/\lambda)^{1/p}$. With $a^+=a-\lambda u^p$, (17) gives

\[
-\sigma a\le a^+
 \le\sigma a+(1-\sigma)u,
\quad
|a^+|\le\sigma a+(1-\sigma)u.
\tag{18}
\]

The negative-input case follows by oddness. Choose any $0<\kappa<1$ and $R>0$ such that

\[
\left(\frac{1+\bar\sigma}{\lambda}\right)^{1/p}
 R^{1/p-1}\le\kappa.
\tag{19}
\]

Then **every** accepted output for $|a|\le R$ satisfies

\[
d(x^+,S)=|a^+|\le Q|a|,
\qquad Q=\bar\sigma+(1-\bar\sigma)\kappa<1,
\tag{20}
\]

and has actual physical displacement

\[
\|x^+-x\|=\lambda\|F(y)\|
\le H_B(|a|)
:=(1+\bar\sigma)|a|
 +\lambda^{1-\beta}(1+\bar\sigma)^\beta |a|^\beta.
\tag{21}
\]

Therefore all accepted output policies, all choices of $\sigma_k\le\bar\sigma$, and all sign changes induced by the correction have

\[
d(x^k,S)\le Q^k d(x^0,S),\qquad
\sum_{k\ge0}\|x^{k+1}-x^k\|
 \le\Theta_B(d(x^0,S)),
\tag{22}
\]

where the explicit physical tail is

\[
\Theta_B(t)=\frac{(1+\bar\sigma)t}{1-Q}
 +\frac{\lambda^{1-\beta}(1+\bar\sigma)^\beta t^\beta}
 {1-Q^\beta}.
\tag{23}
\]

The full operator is globally defined, so $U=\mathbb R^2$ gives automatic retention. For a smaller open physical domain, the strict budget $\Theta_B(d(x^0,S))<d(x^0,X\setminus U)$ proves prefix retention. The Cauchy limit belongs to the exact full zero line. If $a=0$, (16) forces $u=0$, so **every** accepted output is $x$; the accepted HPE fixed set is exactly $S$.

The endpoint bridge in (18)–(20) is essential. The graph value $w$ is evaluated at $y$, and (21) does not identify it with $r_F(x^+)$. The full endpoint residual (11) remains a separate quantity.

For a fully numerical contract, take $p=1/2$, $g=1/3$, $\lambda=1$, $\bar\sigma=1/2$, $\kappa=1/2$ and $R=1/64$. Then $\beta=2/3$, (19) holds, $Q=3/4$, and

\[
H_B(t)=\tfrac32t+(\tfrac32t)^{2/3}.
\]

For the exact C249 interface on the same cap, $K(R)=5/64$, $\psi(s)=s^3$, $\bar t=5/64$, and $K(t)^3/t\le(1/64)(5/4)^3<1/2$.

**Prior positive and value.** The normal coordinate is a monotone scalar equation. Equations (17)–(23) are an elementary inexact scalar-PPA/correction proof plus a summable tangential readout. The full vector operator fails inverse hypomonotonicity, but this does not create a difficult independent convergence mechanism. The legitimate content is the all-output error-direction distinction and a reusable physical lifting check. A naturally supplied normal projection, nonlinear curved zero set, or a task with genuine coupled normal equations would need an additional theorem and application; none is asserted here.

## 4. Option C: underrelaxed PPA with convex physical zero set

Assume the existing C249 certificate gives all-output distance contraction $d(y,S)\le\kappa d(x,S)$ and physical step $\|y-x\|\le H(d(x,S))$, and assume additionally that $S$ is convex. For every complete $y\in\mathcal J(x)$ and every policy $\theta\in[\theta_*,1]$, $\theta_*>0$, define

\[
x^+=(1-\theta)x+\theta y.
\tag{24}
\]

Convexity of the distance function gives the actual physical endpoint bridge

\[
d(x^+,S)\le[1-\theta(1-\kappa)]d(x,S)
 \le Q_Cd(x,S),\quad
Q_C=1-\theta_*(1-\kappa)<1,
\]

and $\|x^+-x\|\le H(d(x,S))$. All-output coverage follows from exact coverage. The fixed set is unchanged because $\theta>0$. The new tail is $\Theta_C(t)=\sum_{j\ge0}H(Q_C^jt)$. It is finite whenever the original monotone-modulus tail $\sum_jH(\kappa^jt)$ is finite: writing $a=\log Q_C/\log\kappa\in(0,1]$, each index $\lfloor ja\rfloor$ occurs at most $\lceil1/a\rceil+1$ times, so $\Theta_C(t)\le(\lceil1/a\rceil+1)\Theta(t)$. The strict new-tail budget gives prefix retention and finite length.

This bridge genuinely allows nonmonotone $F$ and all complete exact roots, including (10), but it is standard averaging geometry. Relaxation itself is not a promising primary migration claim. For nonconvex $S$, convexity cannot be silently retained. A separately proved distance-interpolation defect of order $C\theta(1-\theta)\|y-x\|^2$ would preserve contraction when $H(t)^2=o(t)$; neither that structural defect nor its complete curved-output scope is proved in this report. Overrelaxation $\theta>1$ is also outside the proof.

## 5. Option D: genuine DR/ADMM splitting requires a native residual bridge

For $F=A+B$, the complete Douglas–Rachford state transition at a fixed $\lambda$ is

\[
x\in J_{\lambda A}(z),\qquad
y\in J_{\lambda B}(2x-z),\qquad
z^+=z+y-x.
\tag{25}
\]

The state is $z$; $x,y$ are shadows. Its exact lifted fixed-state target is

\[
S_D=\{x+\lambda a:a\in A(x),\ -a\in B(x)\}.
\tag{26}
\]

For any selected transition, $z^+=z$ iff $x=y$, in which case $0\in A(x)+B(x)$. Conversely, every decomposition in (26) gives a stationary selection. With nonunique resolvents this is only a fixed-set identity: it does not force all other selections from the same fixed state to be stationary. Complete coverage and full zero-fiber absorption need independent checks.

The inclusion values are at different points. One cannot add $a\in A(x)$ and $b\in B(y)$ and declare a graph value of $F(y)$. A concrete true-residual bridge is available if $A$ is a single-valued $L$-Lipschitz map on the entire output collar. Then

\[
a=(z-x)/\lambda=A(x),\qquad
b=(2x-z-y)/\lambda\in B(y),
\]

so $A(y)+b\in F(y)$ and

\[
r_F(y)\le\|A(y)-A(x)+(x-y)/\lambda\|
 \le(L+1/\lambda)\|x-y\|
 =(L+1/\lambda)\|z^+-z\|.
\tag{27}
\]

For physical readout and length, if $J_{\lambda A}$ is single-valued and $L_J$-Lipschitz on the retained state domain, then

\[
\|x_{k+1}-x_k\|\le L_J\|z_{k+1}-z_k\|,
\qquad y_k=x_k+(z_{k+1}-z_k).
\tag{28}
\]

Finite state length then gives finite $x$-length and finite $y$-length (the latter is bounded by $(L_J+2)$ times the state length), and the two shadows have the same limit. Equation (27) and closed graph of $F$ identify that limit as a physical zero. All identities hold for every selected $B$-root; finite length of $z$ itself is not established by these identities.

Defining $G_T=T^{-1}-I$ for the entire DR state relation $T$ gives $z-z^+\in G_T(z^+)$ and $G_T^{-1}(0)=\operatorname{Fix}T$. This can wrap any transition relation. It is a tautological real-graph encoding, not a transfer of an original $F$-RLEB certificate to DR, and not a new splitting theorem. To obtain a genuine migration, one must prove from the native $A,B$ assumptions the complete $T$-RLEB geometry, (26) coverage/absorption, an error bound to $S_D$, and the physical bridge. ADMM or a primal-dual product lift has analogous obligations; changing the state does not remove them.

## 6. Decision for the main migration

| Route | Completed usable result | Fatal or missing issue | Recommendation |
| --- | --- | --- | --- |
| Ordinary real-graph HPE with isotropic constant relative tolerance | Equations (4)–(9), if the exact physical step is linear and the perturbed-input collar is certified | Noncalm full-graph example (15) leaves zeros under any positive fixed tolerance | Conditional side result; do not present as the generic noncalm extension |
| Anisotropic real-graph HPE | Exact algorithm (16), complete coverage, true residual (11), actual endpoint (20), uniform length/retention (23), outside finite local inverse hypomonotonicity | Reduced monotone scalar proof is already short; no established natural high-value task | Best proved bridge here; use to motivate direction-sensitive stopping, with honest limited value |
| Underrelaxed PPA | Complete-output convex-zero bridge (24), inherited summability and strict retention | Curved-zero defect and overrelaxation not supplied; averaging is standard | Supporting interface only |
| DR/ADMM/primal-dual splitting | Native residual bridge (27), shadow length bridge (28), correct lifted target (26) | No general native RLEB transfer; generic graph wrapper is tautological | Keep as open application development, not the main theorem |

The best current migration target remains a real-graph inexact theorem with an implementable stopping criterion tied to the relevant normal/error-bound scale and an explicit physical endpoint bridge. HPE can be included only when its correction is analyzed as in (7) or (18). None of the alternatives above by itself establishes a stronger high-value field-level contribution than the main inexact RLEB project.
