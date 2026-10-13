# Primary-source review for the nonexact PPA migration

Date: 2026-10-13. Scope: priority and algorithm identity, with positive recovery of prior methods. This is an original review report, not a canonical theorem or a worldwide novelty certificate. Read against C249-v1 in `research/canonical/physical_rleb_gppa.md` and C213 in `research/canonical/gppa_inexact_modulus.md`. Mathematical review follows the repository academic-writing skill, review mode. No complete third-party paper is stored here.

## 1. Decision before choosing a contribution

The literal extension “an exact contraction remains stable under output errors” is established fixed-point analysis. The combination “nonmonotone PPA + constant relative error + linear convergence” also has an explicit 2003 predecessor. It is not a credible headline by itself. The promising comparison unit is narrower: an implementable **real-graph defect** rule for the unchanged complete relation, general error-bound and reflection moduli, physical finite length with a degenerate kernel, and a sharp forcing threshold. Each of these qualifications must survive positive mappings to old methods.

The current theorem agent's candidate uses

\[
w\in F(y),\qquad e=x-y-\lambda w,\qquad
\|e\|\le\eta\psi(\|w\|),\qquad \lambda\|w\|\le\bar s.
\tag{N1}
\]

The norm of the selected graph value is observable; the true residual only satisfies \(r_F(y)\le\|w\|\). The candidate is not the same object as C213's assumed single-valued kernel resolvent with additive output perturbation. Its value should be assessed at this distinction, not by relabeling C213.

## 2. Wang–Li–Ng 2023: a material unresolved priority check

**Verified paper fact, abstract only.** J. Wang, C. Li, K. F. Ng, *Convergence Rate of Inexact Proximal Point Algorithms for Operator with Hölder Metric Subregularity*, SIAM J. Optim. **33**(3) (2023), 1996–2020, DOI [10.1137/22M152147X](https://doi.org/10.1137/22M152147X). The publisher lists online publication 2023-08-04, acceptance 2023-02-27. Its abstract concerns maximal monotone operators on Hilbert spaces, Rockafellar-type inexact PPA, local/global strong convergence under Hölder metric subregularity, and rate estimates. It says the exact specialization improves Li–Mordukhovich 2012.

**Access record.** The official `/doi/full/` and `/doi/pdf/` routes both redirected to the abstract/access page. The [CUHK institutional record](https://research.cuhk.edu.hk/en/publications/convergence-rate-of-inexact-proximal-point-algorithms-for-operato-2/) supplied DOI links, not an open manuscript. Targeted title/DOI/author searches did not produce a lawfully public complete primary text. No paywall or account barrier was circumvented.

**Unverified.** The exact error tests, exponent conventions, all theorem numbers, summability assumptions, permissible constant forcing, and finite-length claims have not been read. Therefore this report does **not** claim (N1) is absent from Wang–Li–Ng, does not claim to recover all their theorems, and does not attribute a guessed criterion to them. This remains a priority gate before a publication-level novelty claim involving Hölder inexact PPA.

## 3. Combettes–Pennanen 2004: same-algorithm positive recovery

**Verified source and version.** P. L. Combettes and T. Pennanen, *Proximal Methods for Cohypomonotone Operators*, SIAM J. Control Optim. **43**(2) (2004), 731–742, DOI [10.1137/S0363012903427336](https://doi.org/10.1137/S0363012903427336). Read [author preprint `sicon3.pdf`](https://pcombet.math.ncsu.edu/sicon3.pdf), 12 pages, headed “to appear”; do not silently assign its draft pagination to the published version. Actual mathematical reading: Algorithm 1.1, Definition 2.2, Lemma 2.4, Theorem 3.1 and its proof, Theorem 4.3 and its operator mapping.

**Paper fact.** Algorithm 1.1 is

\[
v_n\in y_n-x_n+\gamma_nA_{i(n)}(y_n),\qquad
x_{n+1}=x_n+\lambda_n(y_n+u_n-x_n).
\tag{CP1}
\]

Theorem 3.1 assumes local maximal \(\rho_i\)-cohypomonotonicity, nonempty closed common local zeros with a uniform neighborhood margin, bounded index gaps, \(\inf_n(\gamma_n-\rho_{i(n)})>0\), and

\[
\frac{\lambda_n}{1-\rho_{i(n)}/\gamma_n}\in[\varepsilon,2-\varepsilon].
\]

It requires a sufficiently close seed, a small absolute budget \(\sum_n(\|u_n\|+2\|v_n\|)\), and selection of \(y_n\) in a specified ball. It proves viability, uniqueness in that ball, and weak convergence. Lemma 2.4 gives

\[
I+(1-\rho/\gamma)(J_{\gamma A}-I)
=J_{(\gamma-\rho)C},\quad C=(A^{-1}+\rho I)^{-1}.
\tag{CP2}
\]

Here \(C\) is maximal monotone when the global inverse hypothesis holds. Theorem 3.1 implements the same identity through a local maximal extension.

**Own algorithm identification.** Take one operator, \(\lambda_n=1\), \(u_n=0\), \(v_n=-e_n\). Then (CP1) is precisely the ordinary real-graph inexact PPA \(e_n=x_n-y_n-\gamma_n w_n\), with next iterate \(y_n\). Summable graph defects are already covered locally when the other hypotheses hold. Unrelaxed convergence is within the displayed relaxation interval for sufficiently large \(\gamma_n/\rho\). This is a positive recovery of the same update; it is not a claim that the old theorem handles every defect accepted by (N1).

**Own rate derivation for the same exact algorithm.** Suppose the solution-anchored graph inequality

\[
\langle y-p,w\rangle\ge-\rho\|w\|^2,
\quad p\in S,\quad w\in A(y),
\tag{CP3}
\]

holds on all actual pairs under consideration, and the same output satisfies the true linear EB \(d(y,S)\le K r_A(y)\). For \(x-y=\gamma w\), a nearest \(p\in P_S(x)\) gives

\[
\begin{aligned}
\|y-p\|^2+\gamma(\gamma-2\rho)\|w\|^2
&\le\|x-p\|^2,\\
d(y,S)&\le
\frac{K}{\sqrt{K^2+\gamma(\gamma-2\rho)}}d(x,S),\qquad\gamma>2\rho.
\end{aligned}
\tag{CP4}
\]

The proof is expansion of \(\|y-p+\gamma w\|^2\), followed by \(r_A(y)\le\|w\|\). In finite dimensions with closed nonempty \(S\), nearest points exist. From the first line also \(\|x-y\|\le\sqrt{\gamma/(\gamma-2\rho)}d(x,S)\); thus the geometric distance decrease yields finite length. Localization still needs a finite-prefix budget ensuring every pair remains in the certified graph block. Equation (CP4) is this review's derivation, not a claimed theorem quotation. It explains why merely appending a linear EB and length conclusion to cohypomonotone PPA gives little priority protection.

## 4. Iusem–Pennanen–Svaiter 2003 and Rockafellar 1976

The independent primary read and exact version/error mapping are in [`rockafellar_hpe_review.md`](rockafellar_hpe_review.md). The material consequences for this migration are:

1. A constant relative tolerance for nonmonotone PPA already predates this project; the precise correction rule must be compared, rather than treating every old relative rule as summable.
2. For maximal monotone \(T\), real-graph defect control can be converted positively to proximity to the exact resolvent. This conversion is not automatically available for a merely solution-anchored reflected modulus or a noninjective nonlinear kernel.
3. Unique-solution inverse Lipschitz estimates, true-residual subregularity to a nonisolated zero set, and Hölder EB are different assumptions. A failure of one inverse hypothesis does not establish novelty of the other cases.

## 5. Luke–Tam 2025: the correct output-perturbation baseline

**Paper fact, published version read.** D. R. Luke and M. K. Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, MOR Articles in Advance, 2025-11-21, DOI [10.1287/moor.2025.0863](https://doi.org/10.1287/moor.2025.0863), [13-page publisher PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863). Read Definition 2, Proposition 4, Assumption 2, Theorem 2 and proof, §5. Theorem 2 uses local graph/value windows, maximal submonotonicity, linear metric subregularity, coverage, and selection in a local ball. Proposition 4 identifies the reflected truncated resolvent as Lipschitz. The paper assumes exact evaluation for its main deterministic theorem; §5 explicitly describes conventional vanishing-error analysis and stochastic invariant-distribution extensions.

**Own positive recovery.** If its certified exact relation has \(d(Tx,S)\le\kappa d(x,S)\), the unchanged output-perturbation update \(x^+=Tx+a\) immediately gives

\[
d(x^+,S)\le\kappa d(x,S)+\|a\|.
\tag{LT1}
\]

Iteration yields the exact geometric convolution and persistent tube. If the prior proof supplies \(\|Tx-x\|\le B(d(x,S))\), then \(\|x^+-x\|\le B(d(x,S))+\|a\|\). These are precisely the logical shape of C213. Arbitrary-modulus summability must still be checked; no generic \(\ell^1\)-error condition implies finite physical length through an arbitrary inverse gauge. Thus C213 is useful organization, but its convolution mechanism is not a new PPA principle.

## 6. The 2026 GPPA stability result: positive closest warped baseline

**Paper fact, v1 read.** B. K. Le, B. S. Mordukhovich, M. A. Théra, [arXiv:2608.01584v1](https://arxiv.org/html/2608.01584v1), submitted 2026-08-03. Read Definitions 1–3, Theorems 2 and 4 with proofs. Theorem 2 assumes pair adaptive strong monotonicity and \(\operatorname{ran}v\subseteq\operatorname{ran}(\gamma F+v)\); it obtains kernel-distance contraction, and distance-to-zero linear convergence with an \(R\)-Lipschitz inverse. Theorem 4 uses the regularized operator \(\widetilde F=F+\epsilon v\), pair monotonicity, globally Lipschitz \(v\), \(R\)-continuity of \(F^{-1}\), and nonempty zero sets for both operators. Its update is

\[
x_{k+1}\in J^v_{\gamma\widetilde F}(x_k)+y_{k+1},\qquad
\|y_{k+1}\|\le\delta=\epsilon^2.
\]

It gives a limiting distance tube tending to zero as \(\epsilon\downarrow0\).

**Own comparison.** This is a positive nonvanishing-error theorem for the same warped-resolvent architecture. It changes \(F\), accepts physical output error, and guarantees a tube. The proposed fixed-\(F\) real-graph forcing theorem could supply different output acceptance and finite length, but neither point nor novelty follows from the older paper's lack of bijectivity. First map the actual regularized algorithm and preserve its genuine guarantee.

## 7. Modern stronger frameworks and forcing-power search

**Paper fact, exact author version distinguished.** Buscaglia–Lotito–Parente–Solodov, SIOPT **35** (2025), 2518–2543, DOI [10.1137/24M1713132](https://doi.org/10.1137/24M1713132). The [author PDF](https://pages.cs.wisc.edu/~solodov/blps24VMprox.pdf) actually read is a 25-page review manuscript, title page “Submitted August 8, 2025”; its numbering is not silently attributed to the final publication. This reader independently checked §5 equations (5.1)–(5.4), Theorem 5.1 and the relevant construction, while the HPE/splitting agent checked Algorithm 4.1 and Theorems 4.3–4.4. For maximally monotone \(T\), (5.2) requires summable relative **output** errors in uniformly controlled symmetric metrics. Theorem 5.1 represents every sufficiently late orbit satisfying that test as the identical iterate sequence of Algorithm 4.1, using asymmetric metrics. Therefore a correction-based framework can positively contain an uncorrected orbit; update appearance alone does not exclude it.

**Own power-forcing bridge.** In a monotone specialization, \(\|e_k\|\le\eta C\|w_k\|^p\), \(p>1\), gives \(\|x_k-y_k\|\ge\lambda\|w_k\|-\|e_k\|\ge(\lambda/2)\|w_k\|\) eventually. Hence

\[
\frac{\|e_k\|}{\|x_k-y_k\|}
\le\frac{2\eta C}{\lambda}\|w_k\|^{p-1}.
\]

If the proposed contraction proof gives geometric \(\|w_k\|\), these ratios are summable. Monotone resolvent nonexpansivity converts the graph defect to output error at most \(\|e_k\|\); the same late orbit then satisfies (5.2), with \(B_k=I\), and is represented by Theorem 5.1. This is a verified positive overlap after establishing the stated bounds, not a circular import of the old theorem to establish them. The noncalm triangular full relation (D1) does not automatically admit the same representation: the source requires a maximally monotone operator and explicit metric assumptions. Arbitrary nonlinear lifts are not excluded by this comparison.

The HPE/splitting review agent also owns [Inexact Warped Resolvent Iterations, arXiv:2606.15426](https://arxiv.org/abs/2606.15426), the nonlinear warped projection/correction comparison. That source remains an explicit additional check; no unverified full-algorithm containment is asserted here.

Targeted searches for residual-power forcing plus Hölder/higher-order-subregular PPA did not locate an exact counterpart of (N1). This is negative retrieval evidence only. Mordukhovich–Ouyang [arXiv:1507.04825v1](https://arxiv.org/pdf/1507.04825), 2015-07-17, was read in the relevant introduction/Definition 3.1 and §§4–5: it concerns higher-order subregularity, perturbation sensitivity, and Newton/quasi-Newton applications; it is not an inexact-PPA theorem. Classical inexact Newton and regularized Newton already use residual-dependent forcing powers. Consequently “choose an error proportional to a residual power” is not a priority claim by itself.

## 8. Positive recovery target and remaining novelty gate

For \(\psi(s)=Ks\), a small enough (N1) tolerance should positively recover a conventional relative graph-residual error test and hence the overlapping monotone/cohypomonotone algorithms. The theorem should record this recovery even if its sufficient threshold is more conservative than a published sharp constant. For an invertible bi-Lipschitz kernel, explicitly map defects through the kernel and inverse moduli, and concede the standard coordinate proof when it applies.

The most valuable open comparison is the critical general-modulus regime: reflected growth \(\omega(t)\asymp t^\gamma\), EB \(\psi(s)\asymp s^p\), \(\gamma p=1\), possibly nonisolated zeros and physical tangential drift. The proposed forcing \(\|e\|\lesssim\|w\|^p\) may be strictly tighter than a fixed relative graph test when \(p>1\). A constructive necessity example could make the migration substantive. A monotone one-dimensional \(p>1\) example alone is insufficient evidence: its reflected resolvent can be Lipschitz and its exact PPA can already be superlinear.

### Independent check of the triangular drift frontier

For \(a>0\), \(0<b<1\), \(0<\gamma<1\), \(p=1/\gamma\), and \(\lambda=1\), the root's proposed full operator is

\[
F(s,t)=\left(-a|t/b|^\gamma,\frac{1-b}{b}t\right),
\quad S=\mathbb R\times\{0\},\quad
J_F(s,t)=(s+a|t|^\gamma,bt).
\tag{D1}
\]

The resolvent formula follows by solving the second coordinate first, then the first; it is complete, single valued, and globally covered. Exact iterates have geometric normal distance and summable horizontal increments. This is a diagnostic model with an explicit solution, not evidence of a broad natural application.

Write \(c=(1-b)/b\), \(r(t)=\|F(s,t)\|\), and \(\psi(r)=(b/a^p)r^p\). For \(t\ne0\),

\[
g(t):=\frac{\psi(r(t))}{|t|}
=\left(1+\frac{(1-b)^2b^{2\gamma-2}}{a^2}
 |t|^{2-2\gamma}\right)^{1/(2\gamma)}\longrightarrow1,
\tag{D2}
\]

so the true EB holds and is asymptotically exact. For an accepted real graph pair \(y=(y_1,t)\), the second defect equation is \(t=b(x_2-e_2)\). Under \(\|e\|\le\eta\psi(r(t))\) and \(|t|\le R\),

\[
|t|\le\frac{b}{1-b\eta g(R)}|x_2|,
\tag{D3}
\]

provided the denominator is positive. For every \(\eta<(1-b)/b\), a sufficiently small \(R\) makes the coefficient less than one. The graph equation and triangle inequality give
\(\|y-x\|\le a b^{-\gamma}|t|^\gamma+[c+\eta g(R)]|t|\), so geometric normal contraction gives finite physical length for all admitted local outputs.

At \(\eta_c=(1-b)/b\), choose any nonzero \(t\), let

\[
y=(x_1+a|t/b|^\gamma,t),\qquad
e=(0,-ct),\qquad x_2=t.
\tag{D4}
\]

Then \(w=F(y)\), \(e=x-y-w\), and \(\|e\|=c|t|\le\eta_c\psi(\|w\|)\). Iterating preserves distance \(|t|\) and drifts horizontally forever. The same transition satisfies every fixed Euclidean relative-step tolerance when \(|t|\) is small enough, because

\[
\frac{\|e\|}{\|y-x\|}
=\frac{(1-b)b^{\gamma-1}}a|t|^{1-\gamma}\longrightarrow0.
\tag{D5}
\]

The ratio to \(\|w\|\) also tends to zero. Thus the nonlinear precision exponent has a concrete all-orbit consequence; an arbitrary fixed Euclidean relative tolerance cannot replace it.

The frontier \(\eta_c\) is a **model asymptotic threshold**. A general sufficient theorem using \(\kappa_0>b\) may have the smaller budget \((1-\kappa_0)/\kappa_0\). These must not be presented as the same sharp constant. Equation (D3) supplies the approach to the model endpoint, and (D4) refutes it at equality.

For a nonlinear kernel, a shifted kernel input \(v(x)+e_v\) need not belong to \(v(X)\). A proof using graph reflection directly, without inventing an exact proximal point at that input, can be a meaningful extension. It still owes physical control of fibers and all accepted transitions; kernel convergence does not give physical convergence by itself.

**Verdict.** Proceed with the real-graph/general-modulus/physical theorem and the checked drift frontier. This is a credible technical-to-moderate contribution package: a precision design principle with a sharp diagnostic boundary, plus a concise general theorem. The scalar absorption argument alone is elementary; the explicit toy model alone is not a major natural application. Do not promote the literal perturbation lemma, constant-relative-error slogan, or simple linear-EB cohypomonotone specialization to the main contribution. The inaccessible Wang–Li–Ng full text and the modern framework comparison remain explicit limits on external priority, not blockers to proving a correctly scoped internal result.

## 9. Review completeness

Checked: current C249/C213 object distinction; primary CP algorithm, localization, monotone-transform proof and positive same-update recovery; published Luke–Tam exact/noise boundary; GPPA v1 error model; a positive classical energy+EB rate derivation; triangular frontier equations D1–D5; targeted forcing-power retrieval. Received and inspected: Rockafellar/HPE/IPS exact-source report. Unverified: WLN2023 complete text, exhaustive international priority, broad recovery of every published rate, sharpness of the universal sufficient theorem's constants. No canonical claim, manuscript, or global literature ledger was modified by this report.
