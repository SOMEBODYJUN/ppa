# Rockafellar output errors and the nonmonotone hybrid comparison

Date: 2026-10-13. Review scope: primary-source criteria and precise algorithm identity for `research/canonical/gppa_inexact_modulus.md`. This note does not register a canonical theorem or establish worldwide novelty. No source PDF is stored in the repository. Source facts below are condensed; the subsequent comparisons and counterexample are independent calculations.

## 1. Rockafellar 1976: primary facts

R. T. Rockafellar, *Monotone operators and the proximal point algorithm*, SIAM J. Control Optim. 14 (1976), 877–898, DOI [10.1137/0314056](https://doi.org/10.1137/0314056). [Author-hosted scan](https://sites.math.washington.edu/~rtr/papers/rtr066-MonoOpProxPoint.pdf); [public university-hosted scan](https://www.cs.cmu.edu/~suvrit/teach/papers/1976_rockafellar_monotone_operators_proximal_point_algorithm.pdf). The relevant author-scan pages were read and visually checked.

For maximal monotone (T) on a real Hilbert space, (P_k=(I+c_kT)^{-1}). Page 880 states

\[
(A)\quad\|z^{k+1}-P_kz^k\|\le\epsilon_k,\qquad\sum_k\epsilon_k<\infty;
\]
\[
(B)\quad\|z^{k+1}-P_kz^k\|\le\delta_k\|z^{k+1}-z^k\|,\qquad\sum_k\delta_k<\infty.
\]

(A',B') replace the left side by (\operatorname{dist}(0,S_k(z^{k+1}))), divide the respective right side by (c_k), and use (S_k=T+c_k^{-1}(\cdot-z^k)). Proposition 3, p. 882, proves (\|z^{k+1}-P_kz^k\|\le c_k\operatorname{dist}(0,S_k(z^{k+1}))).

Theorem 1, p. 883: under (A), (\inf c_k>0), boundedness is equivalent to existence of a zero; the bounded orbit converges weakly to a zero and its steps vanish.

Theorem 2, pp. 885–886: under (B), boundedness, nondecreasing (c_k\to c_\infty\le\infty), unique zero (\bar z), and (\|z-\bar z\|\le a\|w\|) for every (z\in T^{-1}(w),\|w\|\le\tau), eventually

\[
\|z^{k+1}-\bar z\|\le q_k\|z^k-\bar z\|,
\quad q_k=\frac{\mu_k+\delta_k}{1-\delta_k},
\quad\mu_k=\frac a{\sqrt{a^2+c_k^2}}.
\]

(q_k<1), (q_k\to\mu_\infty); (c_\infty=\infty) gives superlinear convergence. Remark 2, p. 887, permits (\delta_k\to\delta_\infty<(1-\mu_\infty)/2) if (A) also holds.

## 2. Same-algorithm consequences for the canonical output-error model

These are comparisons derived here, not additional attributed paper statements.

* With (v=I), fixed (\lambda=c_k), and (A=T), GI3 is literally (z^{k+1}=P_kz^k+e_k). If (\sum\|e_k\|<\infty), the same orbit satisfies Rockafellar's (A). No correction step or state change is needed. His hypotheses require global maximal monotonicity and cover all Hilbert-space inputs; GI1–2 instead posit coverage on the actual image and a separately certified contraction window.
* The relative output rule (\|e_k\|\le\delta_k\|z^{k+1}-z^k\|) is literally (B) when (\sum\delta_k<\infty). Theorem 2 supplies a rate for this same uncorrected orbit, with its explicit additional assumptions. Therefore a general claim that relative errors for PPA necessarily demand an HPE correction would be false.
* For a monotone instance satisfying the all-fiber inverse bound above, firm nonexpansiveness gives the eventual exact-output contraction (\mu_k). For a strongly monotone (T), the direct resolvent contraction is (q=(1+\alpha\lambda)^{-1}). Applying the distance triangle inequality to a perturbed output gives (D_{k+1}=qD_k+E_k); expanding this scalar recursion gives GI5's convolution, and constant (E_k\le\delta) gives the radius (\delta/(1-q)). This is elementary contraction perturbation calculus. The calculation, by itself, is not a new inexact PPA algorithm or a novelty discriminator.
* The genuine scope to examine is the certification of the same complete relation, the actual image (Q=v(H)), localization, and transport of physical errors through (v). A change of variables does not by itself remove classical prior art. Conversely, Rockafellar's all-fiber inverse bound at a unique zero is stronger than a distance-to-a-nonunique-zero-set error bound; the two conditions must not be identified.

## 3. Iusem–Pennanen–Svaiter: primary version and algorithm facts

Publication: A. N. Iusem, T. Pennanen, B. F. Svaiter, *Inexact variants of the proximal point algorithm without monotonicity*, SIAM J. Optim. 13 (2003), 1080–1097, DOI [10.1137/S1052623401399587](https://doi.org/10.1137/S1052623401399587). Read version: [Svaiter-hosted author manuscript](https://w3.impa.br/~benar/docs/iusem/sv-ius-penn.pdf), dated December 24, 2006, 23 pages. Do not equate this version's typography with the 2003 final publication.

Equations (10)–(15), manuscript p. 4, use

\[
v_n\in T(y_n),\quad\gamma_nv_n+y_n-x_n=e_n,
\quad x_{n+1}=x_n-\gamma_nv_n=y_n-e_n.
\]

Algorithm 1 requires (\|e_n\|\le\sigma(\hat\gamma/2-\rho)\|v_n\|). Algorithm 2 requires (\|e_n\|\le\nu\|y_n-x_n\|), where

\[
t=2\rho/\hat\gamma,\qquad
\nu=\frac{\sqrt{\sigma+(1-\sigma)t^2}-t}{1+t},
\quad\sigma\in[0,1),\quad\hat\gamma=\inf_n\gamma_n>2\rho.
\]

The introduction and Proposition 2 impose maximal inverse hypomonotonicity: (T^{-1}) is (\rho)-hypomonotone; (Y_\rho(T)=(T^{-1}+\rho I)^{-1}) is maximal monotone. Theorem 1, manuscript p. 13, also requires convex (U), nonempty closed (S\cap U), (B(0,\beta)\subset V), ((S\cap U)+B(0,\delta)\subset U), and (d(x_0,S\cap U)\le\min\{\delta,\beta\hat\gamma/2\}); allowed graph points remain in (U\times V), with weak convergence. Its printed hypothesis omits the inverse despite the introduction and proof. Theorem 2, manuscript p. 16, adds inverse Lipschitzness and gives contraction estimates for the corrected states.

## 4. Exact algebraic bridge and a manuscript defect

The following derivations are independent of whether the manuscript's displayed theorem wording is repaired.

Write (M=(T^{-1}+\rho I)^{-1}) and (c=\gamma-\rho>0). For every admitted graph pair (v\in T(y)), its transformed pair is (v\in M(y+\rho v)). Thus

\[
y+\rho v=J_{cM}(x+e),\qquad
\alpha=\frac\gamma{\gamma-\rho},\qquad
x^+=(1-\alpha)x+\alpha J_{cM}(x+e)-\alpha e.
\]

When (e=0) and (\gamma>2\rho), (1<\alpha<2): exact PPA for (T) is the same physical-state iteration as overrelaxed monotone PPA for (M), with the transformed parameter. This is a positive equivalence; nonmonotonicity of (T) alone does not exclude the monotone mechanism. For (e\ne0), the corrected state is (y-e), while the directly accepted approximate proximal point is (y=J_{\gamma T}(x+e)). Neither is, by definition, GI3 with (e) as its output error. If a local resolvent modulus (L) applies at both actual inputs, the correction has output error (J_{\gamma T}(x+e)-J_{\gamma T}(x)-e), bounded by ((L+1)\|e\|); this is a conditional bridge.

The author manuscript's Corollary 4, p. 17, claims superlinear convergence for both algorithms when (\gamma_n\to\infty). Its Algorithm 2 allows a direct counterexample. Set (H=\mathbb R), (T=I), (\rho=1), (\gamma_n=n+3), and (0<\sigma<1), so the permitted constant (\nu) above lies in ((0,1)). Choose any (x_0>0) and

\[
y_n=\frac{1-\nu}{\gamma_n+1-\nu}x_n,\qquad
v_n=y_n,\qquad e_n=\nu(y_n-x_n).
\]

Then (v_n\in T(y_n)), the inclusion residual equals (e_n), and the relative inequality holds with equality. The corrected update is

\[
x_{n+1}=\frac{1-\nu+\gamma_n\nu}{\gamma_n+1-\nu}x_n.
\]

All global inverse hypomonotonicity, zero existence, parameter, and inverse Lipschitz conditions hold. The positive ratio tends to (\nu>0), while eventually remaining below a fixed constant less than one; hence (x_n\to0) linearly and not superlinearly. This refutes that manuscript's unrestricted Algorithm 2 superlinear clause, not its weak-convergence theorem or every version of the published paper. The published 2003 final text remains an explicit verification obligation before attributing this defect to it.

## Review handoff

The primary reader route is algorithm identity → applicable classical theorem → transformed nonmonotone algorithm → explicit defect. Rockafellar's formulas and theorem assumptions were visually verified at the cited printed pages. IPS formulas were checked against the author manuscript's searchable text and independently substituted above; its final published typography is unverified. Terminology preserves output error, subproblem residual, corrected state, full inverse fiber, and local graph window as separate objects. No canonical file was changed.
