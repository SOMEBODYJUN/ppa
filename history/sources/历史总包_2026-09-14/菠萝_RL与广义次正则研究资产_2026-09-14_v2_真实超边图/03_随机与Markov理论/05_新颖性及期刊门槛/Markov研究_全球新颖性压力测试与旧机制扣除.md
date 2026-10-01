# Markov invariant-transport programme: global-priority stress test

Date: 2026-09-09. Task: `markov_global_novelty_audit`. Expert: `sci-skills-literature-search`.

## 1. Decision

**RETAIN the exact-source obstruction programme; REPAIR its novelty positioning; DO NOT certify global priority or a SIAM/Mathematical Programming-ready paper.**

The strongest surviving candidate is the compact Euclidean, exact-zero, all-initial-law counterexample: uniform one-step contraction to the invariant set and uniform relative geometric convergence coexist with failure of every positive-Hölder error bound for the *specified invariant synchronous transport discrepancy*. The independent mathematical audit has passed this construction. This literature audit found no exact earlier theorem/counterexample with that complete package. That is a bounded negative search result, not proof that nobody has done it.

The natural two-projection example is an excellent lead example, but the ingredients “random projections”, “one-step stationarity”, “false zeros can occur”, “correlations need conditional transport”, and “mixing does not guarantee coercivity of every dissipation certificate” all have prior art. The useful candidate contribution is their exact conjunction for the source discrepancy, including its closed form and blindness of the entire specified synchronous-residual history.

**Subsequent structural advance:** the companion finite-state supplement now proves exact zeros iff global linear EB for the original residual, gives a sharp finite certificate, and supplies an OT-dependent lazy four-state witness where pointwise displacement injectivity fails but the source EB holds. With a small update probability this witness meets a balanced expected almost-firm violation below one, yet excludes the specified source scalar-rate-compatible gauges. This strengthens the candidate into a finite/infinite classification package; global priority and whole-paper journal readiness remain unverified.

**Important addition beyond the previous project audit:** Andrieu–Lee–Power–Wang already give a convergent chain whose every fixed-block multiplicative reversibilization fails a weak Poincaré inequality, and explain that exponential bounded-observable decay can coexist with this failure. This is an obligatory conceptual comparison, not a direct disproof of our exact-source novelty. See Section 4 below.

## 2. Scope, inputs, and labels

Inputs reviewed:

- `output/ATTACK_MARKOV_SUBREG_NECESSITY_CONJECTURE.md`, especially Sections 0, 9–11.
- `output/AUDIT_MARKOV_COUNTEREXAMPLE.md`, including completed Sections 11–15.
- `output/AUDIT_MARKOV_NOVELTY_AND_JOURNAL.md`.
- Relevant theorem, interpretation and prior-art sections of `output/ATTACK_MARKOV_CONDITIONAL_REPAIR.md` and `output/AUDIT_MARKOV_CONDITIONAL_REPAIR.md`.
- The primary sources and exact locators below. This task did not rerun the mathematical verification scripts; their reported execution belongs to the independent audit, not to this search task.

The original object remains

\[
\Psi(\mu)^2=\inf_{\pi\in\mathcal I}\inf_{\eta\in\operatorname{Opt}_{W_2}(\mu,\pi)}
\int\mathbb E\lVert (x-T_\xi x)-(y-T_\xi y)\rVert^2\,d\eta,
\qquad\mathcal I=\operatorname{inv}P.
\]

`VERIFIED` below means that the stated evidence/scope is checked. It does **not** mean worldwide novelty is verified. `NOT NOVEL` concerns only the claim actually named in its row. `PENDING` means that exact priority, or a required theorem-level comparison, is unresolved.

| Claim | Status | Evidence and consequence |
|---|---|---|
| Source authors had not noticed possible false zeros in CAT(0) | **NOT NOVEL / false attribution** | HLS 2023 §3.2 expressly separates exact zeros from subregularity and warns that nonnegative pointwise discrepancy does not imply exact zeros. [HLS](https://arxiv.org/html/2206.05213v3) |
| Random convex projections can reach a stationary distribution after one step | **NOT NOVEL** | HLS Example 2.2 already gives random singleton projections with one-step attainment. Its 2023 nonexpansive paper also treats noisy hyperplane projections. [Example 2.2](https://arxiv.org/html/2206.05213v3), [Proposition 4.5](https://arxiv.org/html/2205.15897v2) |
| Two parallel projections have exactly \(\Psi(\mu)=W_2(\mu_y,\beta)\), miss correlations, and all source-style synchronous histories stay blind | **VERIFIED project proof; priority PENDING** | Independently audited project Sections 12/B1–B2. No exact matching prior example was located. The source warning and old projection model must be acknowledged. |
| Four-state sharp squared-distance Q-factor \(15/16\), wrong-zero-set subregularity, and relative R-rate simultaneously | **VERIFIED project proof; priority PENDING** | Independent audit A1–A11. This is not a counterexample to ordinary subregularity of that four-state \(\Psi\), which holds. |
| Exact zeros + uniform Q/R rates + no local positive-Hölder EB for fixed source \(\Psi\) | **VERIFIED project proof; priority PENDING** | Independent audit C1–C8. Existing RFI sufficient/consistent/paracontractive theorems do not directly cover the implication negated here. [Luke, Theorem 9 and §6](https://link.springer.com/article/10.1007/s10107-024-02124-w) |
| Fixed finite-state source \(\Psi\): exact zeros iff global linear \(W_2\)-EB, with sharp finite certificate | **VERIFIED new project derivation and independent audit; priority PENDING** | Companion `MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md` preserves both minimizations via OT-dual tight-edge polytopes, then gives vertex and Hoffman proofs. The polyhedral/Hoffman mechanism is classical, not a new general EB principle. |
| General bounded-domain piecewise-affine exact-zero-to-EB principle | **NOT NOVEL** | Dolgopolik 2023 Theorem 5 directly supplies bounded-domain norm EBs for nonconvex continuous PWA functions. Our residual's source-specific finite representation and sharp certificate must carry the contribution, not the general implication. [Primary theorem](https://arxiv.org/html/2210.02606v3) |
| Finite OT-dependent lazy cycle: collision of displacement signatures, exact source zeros, sharp EB, mixing, but no gauge compatible with the specified global pointwise almost-firm scalar rate formula | **VERIFIED derivation / exact arithmetic / cross-audit; priority PENDING** | Companion §10 uses \(G=\{0,1,3,4\}\), update probability \(p\), sharp squared EB constant \(13/p\), and \(p=1/100\) for balanced violation \(2/5<1\). This does not exclude general EB gauges or redesigned measure-level certificates. |
| Countable example also excludes every general gauge compatible with the fixed valid source almost-firm scalar contraction formula | **VERIFIED project corollary; priority PENDING** | Independent audit §14. This is a rate-formula-specific exclusion, not absence of all general gauges. The source scalar relation is existing. [HLS equation (20)](https://arxiv.org/html/2206.05213v3) |
| Compactness + exact zeros automatically yields some gauge | **NOT NOVEL principle** | Explicit modulus-of-regularity result exists in Kohlenbach–López-Acedo–Nicolae, Proposition 3.2/Remark 3.3. Adapting continuity to a nonnegative l.s.c. \(\Psi\) uses the same elementary compactness contradiction. [Primary PDF, p. 6](https://arxiv.org/pdf/1711.02130) |
| Defining the smallest gauge by a residual-constrained supremum is new | **NOT NOVEL principle** | Liu–Lourenço Proposition 3.3 defines a best consistent EB via the same extremal-value mechanism, in its finite-dimensional convex-feasibility setting. [Primary full text](https://arxiv.org/html/2008.12968v3) |
| Conditional/fibered Wasserstein and measurable fiberwise optimal couplings are new | **NOT NOVEL** | Peszek–Poyato, Lemma 3.6/Proposition 3.7; Chemseddine et al., Proposition 1/Corollary 2. [Fibered OT](https://arxiv.org/html/2203.08104v4), [conditional OT](https://arxiv.org/html/2403.18705v3) |
| Conditional local-specification comparison through \((I-C)^{-1}\) is a new Gibbs EB | **NOT NOVEL** | Direct instance of classical Dobrushin comparison, not merely a related idea: Rebeschini–van Handel Corollary 2.6. [Author PDF](https://web.math.princeton.edu/~rvan/dobrushin130819.pdf) |
| Independent refresh's minimum-probability contraction and sharpness mechanism | **NOT NOVEL mechanism; exact packaged theorem PENDING** | Ordinary coordinate coupling and a one-coordinate perturbation establish it. Useful specialization, weak flagship novelty without an additional structural theorem. |
| General gauges, optimal profiles and nonlinear scalar decay for slow fibers are a new stochastic paradigm | **NOT NOVEL** | Weak-Poincaré profile/convex-duality theory already gives this framework; our one-bit formulas reduce to a multiplication-operator profile. [ALPW 2022, §2/Remark 13](https://arxiv.org/html/2112.05605v2) |
| Gaussian precision/sampling eigenvalue \(\zeta\) is newly discovered | **NOT NOVEL** | Power 2026 Proposition 6 gives the same eigenvalue after similarity, and cites earlier Gaussian scan optimization. Its divergence is entropy, not our coordinate-conditional \(W_2\) residual. [Power](https://arxiv.org/html/2609.00408v1) |
| Audited Gaussian sharp conditional EB constant \(\zeta^{-1/2}\) is globally new | **PENDING** | The project proof is stronger than its original triangle constant, but corrected Marton conditional-transport and Gaussian Gibbs prior art still require exact inequality-level comparison. No priority clearance here. |
| “Geometric mixing can coexist with failure of all finite-step coercive dissipation certificates” is a first conceptual discovery | **NOT NOVEL at that breadth** | ALPW 2023 preprint/2026 paper §3.2.3, Example 65/Proposition 66 and following geometric-tail discussion. [Primary full text](https://arxiv.org/html/2312.11689v1) |
| Entire published conjecture is resolved regardless of metric, residual, algorithm class or rate quantifier | **NOT VERIFIED; must not claim** | The published discussion allows an appropriate metric; algorithm-specific hypotheses are not all represented by the artificial countable model. [Luke §6](https://link.springer.com/article/10.1007/s10107-024-02124-w), [X-FEL §3.2](https://link.springer.com/article/10.1007/s10107-025-02319-9) |

## 3. Direct RFI lineage: what is actually ruled out

The following accessible primary records were checked against the named sections, not inferred merely from titles:

1. **Hermer–Luke–Sturm, 2023**, *Rates of Convergence for Chains of Expansive Markov Operators*, Transactions of Mathematics and Its Applications 7(1), tnad001. Theorem 2.6, Definition 3.6, §3.2 and Theorem 3.7. The main theorem allows compact subsets of an ambient Hadamard space; the state subset need not itself be convex. The source also already has residual-domination plus contraction as a sufficient EB route. [Official article](https://academic.oup.com/imatrm/article/7/1/tnad001/7459406).

2. **Luke, published online 2024 / journal record 2025**, *Convergence in distribution of randomized algorithms: the case of partially separable optimization*, DOI 10.1007/s10107-024-02124-w. Theorem 9 assumes measure paracontraction and common gauge-monotonicity. Section 6 leaves a non-paracontractive question open. Our example is outside the former and gives a negative answer only to a precisely frozen fixed-\(W_2\), fixed-\(\Psi\), rate-specific version of the latter. [Official full text](https://link.springer.com/article/10.1007/s10107-024-02124-w).

3. **Luke–Schultze–Grubmüller, 2026**, *Stochastic algorithms for large-scale composite optimization: the case of likelihood maximization for X-FEL imaging*, DOI 10.1007/s10107-025-02319-9. Assumption 3(c), equations (15)–(17)/(39), and §3.2 require identification and gauge stability; they are not consequences of almost-firmness. Its specific likelihood algorithm remains a separate scope. [Official full text](https://link.springer.com/article/10.1007/s10107-025-02319-9).

4. The predecessor **arXiv:2007.06479** was submitted in 2020, but the accessed PDF is **v2, March 2022**. Its equation (29), pp. 15–17, already defines the Markov discrepancy, separates identification, and gives a contraction/residual-domination argument. The v1 PDF could not be read through this interface, so the reviewed v2 wording must not be backdated to 2020. [Version record](https://arxiv.org/abs/2007.06479), [accessed PDF](https://arxiv.org/pdf/2007.06479).

5. **Pischke–Powell, May 2026**, *Convergence guarantees for stochastic algorithms solving non-unique problems in metric spaces*, arXiv:2605.06129v1, uses a general regularity/modulus framework and stochastic quasi-Fejér estimates, including proximal applications. The inspected framework does not supply an earlier exact source-\(\Psi\) no-Hölder counterexample; it is nevertheless mandatory surrounding work if claiming a new general stochastic regularity theory. [Primary full text](https://arxiv.org/html/2605.06129v1).

Targeted correction/erratum searches for the two Mathematical Programming DOIs and HLS did not locate a matching correction or counterexample. This is not a completeness guarantee. Dynamic HTML dates and search “published today” labels were ignored when actual version headers/records disagreed.

## 4. Most serious conceptual precedent: weak-Poincaré counterexamples

ALPW's *Weak Poincaré Inequalities for Markov chains: theory and applications* was publicly posted **18 December 2023**; the official publication is **Annals of Applied Probability 36(1), 46–107 (2026), DOI 10.1214/25-AAP2185**. Its accessible §3.2.3 constructs a countable renewal-level chain: deterministic motion along each level, random choice of the next level at its end. Example 65/Proposition 66 show convergence although \((P^*)^kP^k\) has no WPI for any fixed \(k\). The following paragraph states that geometric level-length tails give exponential decay in the bounded-observable normalization. [Preprint](https://arxiv.org/html/2312.11689v1), [official publication](https://projecteuclid.org/journals/annals-of-applied-probability/volume-36/issue-1/Weak-Poincar%C3%A9-inequalities-for-Markov-chains-Theory-and-applications/10.1214/25-AAP2185.full).

The differences below are **our mathematical comparison**, not a claim that ALPW discuss our discrepancy:

| Axis | ALPW precedent | Present exact-zero candidate |
|---|---|---|
| Certificate | Observable Dirichlet form of a kernel/reversibilization | State-displacement difference, optimized only over input-\(W_2\)-optimal couplings to invariant laws |
| Dependence on implementation | Kernel/operator and invariant reference law | Fixed random-map realization matters |
| Quantification | \(L^2\) observable norms with a specified sieve, e.g. oscillation | Every initial probability law; Q-contraction to the invariant **set** and relative R-rate to its law-dependent limit |
| Geometry | Countable measurable renewal-level chain | A compact subset of \(\mathbb R\), globally Lipschitz actual maps, expected almost-firmness |
| Zero obstruction | Fixed-block reversibilizations are reducible | \(\Psi^{-1}(0)=\mathcal I\) exactly; quantitative separation still flatter than every positive power |
| Genuine remaining comparison | Broad dissipation-versus-mixing separation is already known | Whether this exact optimal-coupling/compact-Euclidean package has an earlier realization remains PENDING |

Do not write “the first example where geometric convergence fails to imply a regularity inequality”. A defensible statement names the original invariant synchronous discrepancy and all its geometry/quantifiers. Conversely, ALPW is not enough to mark the exact present theorem NOT NOVEL: its displayed certificate and convergence norms are different, and a transfer theorem has not been proved.

## 5. Positive repair: imports versus possible new interface

### 5.1 Conditional is not automatically adapted

For a conserved marginal \(\nu\), the frozen-fiber distance
\[
\mathsf W_\nu(\mu,\eta)^2=\int W_2(\mu_u,\eta_u)^2\,d\nu(u)
\]
and measurable optimal fiberwise couplings are existing results, with full theorem access now obtained for Peszek–Poyato (2023), Lemma 3.6 and Proposition 3.7. Chemseddine et al. (JMLR 2025) explicitly give the expected-conditional-distance identity. Neither distance should be presented as an invented tool. [Peszek–Poyato](https://arxiv.org/html/2203.08104v4), [Chemseddine et al.](https://jmlr.org/papers/v26/24-0586.html).

Adapted/nested Wasserstein has a different principal constraint: nonanticipative temporal information. Backhoff-Veraguas–Bartl–Beiglböck–Eder (2020) develop adapted Wasserstein to retain information ordinary Wasserstein misses. That supplies prior art for the broader information-sensitive-transport principle; it is not the exact fixed-conserved-variable repair. [Official article](https://link.springer.com/article/10.1007/s00780-020-00426-3).

The candidate interface is therefore: **diagnose the fixed source residual, specify precisely which dependence it loses, and prove an algorithm-native replacement with explicit comparison maps**. Simply conditioning an old theorem fiber by fiber is standard lifting. Also, the stronger conditional topology cannot be called locally equivalent to ordinary joint \(W_2\); the audited projection sequence already disproves that equivalence.

### 5.2 Dobrushin and Gaussian claims

Rebeschini–van Handel Corollary 2.6 already compares measures by local conditional discrepancies through \(D=\sum_{n\ge0}C^n=(I-C)^{-1}\). Kantorovich duality turns its bounded local-oscillation estimate into the weighted-Hamming EB used in the project. Thus that EB is a direct specialization. Wang–Wu (2014) supplies the established Gibbs coupling/rate context. [Comparison theorem](https://web.math.princeton.edu/~rvan/dobrushin130819.pdf), [Gibbs rates](https://arxiv.org/html/1410.4329v1).

Recent overlap is particularly close. Sam Power's **31 August 2026** preprint, Theorem 2, proves weighted conditional-entropy tensorization and nonuniform-scan convergence; Proposition 6 gives
\[
\lambda_{\min}(G_p^{1/2}D_0^{-1/2}QD_0^{-1/2}G_p^{1/2}),
\]
the same eigenvalue as the project's \(\zeta=\lambda_{\min}(Q^{1/2}\operatorname{diag}(p_i/Q_{ii})Q^{1/2})\). This equality is elementary similarity/singular-value algebra. [Power](https://arxiv.org/html/2609.00408v1).

The July 2026 version of *Wasserstein Contraction of Coordinate Ascent Variational Inference* also gives Gibbs influence estimates from conditional transportation-information and cross-smoothness, §5.2. It further weakens any broad claim of a new native Gibbs verifier. It does not by itself identify the project's sharp quadratic conditional EB. [Primary full text](https://arxiv.org/html/2605.30253v3).

The sharp \(\zeta^{-1/2}\) EB remains **PENDING** at exact-priority level. Marton's 2004 Euclidean conditional-transport paper and its **2010 correction** must be compared using corrected constants; this audit checked the original record but did not finish that corrected theorem-level exclusion. [Original record](https://arxiv.org/abs/math/0410168), [correction](https://projecteuclid.org/journals/annals-of-probability/volume-38/issue-1/Measure-concentration-for-Euclidean-distance-in-the-case-of-dependent/10.1214/09-AOP463.full).

### 5.3 The nonuniform one-bit gauge is an optimal spectral profile

The project's identities
\[
E^2=\int h\,d\nu,\quad R^2=\int ah\,d\nu,\quad E_k^2=\int(1-a)^kh\,d\nu,\quad0\le h\le M
\]
give
\[
\phi(t)^2=\inf_{\lambda\ge0}\left\{\lambda t^2+\int M(1-\lambda a)_+\,d\nu\right\}.
\]
This exact binary transport identification is project work. Its optimization is the standard threshold/fractional-knapsack duality, and its abstract gauge-to-rate interpretation is established weak-Poincaré profile theory. With \(f=\sqrt h\) and multiplication \(A f=af\), the three quantities are \(\|f\|_2^2\), \(\langle Af,f\rangle\), and \(\|(I-A)^{k/2}f\|_2^2\). To impose a zero-mean convention, realize this on the odd-in-bit subspace over a fair auxiliary bit; do not apply a full-space variance inequality across conserved variables. This is an **AI_INFERENCE algebraic comparison**, not a different execution of the algorithm.

ALPW 2022 Definitions 4–6/Theorem 8/Remark 13 already connect a general WPI profile, convex conjugacy and one-step nonlinear scalar decay without information loss. The 2023/2026 continuation further develops optimal profiles and necessity. The project's non-power gauge should be presented as an exactly solvable specialization, not a new rate paradigm. [2022 full text](https://arxiv.org/html/2112.05605v2), [continuation](https://arxiv.org/html/2312.11689v1).

### 5.4 Other adjacent tools screened

- Rudolf–Schweizer's Wasserstein perturbation theory already controls kernel and stationary-law errors under suitable ergodicity. It does not use the same optimal-coupling synchronous residual. [Primary paper](https://arxiv.org/html/1503.04123v3).
- Sixta–Rosenthal–Brown's common-random-number method, Theorem 3.1, bounds distance to stationarity from a specified coupled-chain distance and initialization assumptions. It is not equivalent to summing displacement-difference residuals. [Primary paper](https://arxiv.org/html/2309.15735v3).
- Yano–Yasutomi studies synchronizing random-map realizations of finite-state mixing chains. Kernel mixing versus realization-dependent path synchronization is an old distinction. [Primary paper](https://arxiv.org/html/1006.0534v2).
- *Mode-Weighted Transport Certificates for State-Dependent Reflected Switching Diffusions*, August 2026, defines a different separating hybrid transport cost; its counterexample concerns the triangle inequality, not false invariant zeros. It was screened and excluded as an exact match. [Primary paper](https://arxiv.org/html/2608.01992v1).

## 6. Safe abstract-level claims

The following wording is scientifically safe **as a description of the audited project proofs**, without “first”, “previously unknown”, or a promise of worldwide priority:

> We study identification and rate obstructions for the invariant synchronous transport discrepancy used in random-function-iteration convergence theory. Two random convex projections reach an invariant law in one step, while their discrepancy depends only on a refreshed marginal and is blind to correlations, including along the entire corresponding synchronous-residual history. We also construct a compact Euclidean random-function iteration with exact invariant zero identification, a uniform one-step contraction toward its invariant set, and uniform relative geometric convergence, but with no local Hölder discrepancy error bound of any positive order. In contrast, compactness and lower semicontinuity yield an unrestricted general error-bound gauge once zeros are identified. These results separate convergence, identification, and rate-compatible regularity for the specified discrepancy. Conditional-transport certificates provide explicit repairs in selected coordinate-refresh models, using established optimal-transport and Gibbs comparison tools.

If the manuscript has no substantial positive theorem beyond current specializations, omit the last sentence rather than advertising a new framework. To call the source question “answered”, use: **a negative answer to the fixed-discrepancy, fixed-Wasserstein, rate-matched necessity implication**, not “the conjecture is completely solved”.

Unsafe abstract/title wording:

- “The first counterexample to metric subregularity being necessary for Markov convergence.”
- “All general error bounds fail despite exact zeros on compact spaces.”
- “We introduce conditional/adapted Wasserstein geometry.”
- “A new Dobrushin/Gaussian spectral-gap theorem.”
- “The results establish an exclusive nonlinear RL or multivalued-resolvent advantage.” The existing stochastic proofs do not establish that advantage.

## 7. Research decision and remaining evidence

There is sufficient evidence to continue a **focused obstruction/classification paper**, because the exact-zero counterexample attacks a specifically published residual necessity problem while preserving unusually strong convergence quantifiers. There is insufficient evidence to certify either global novelty or a complete top-journal contribution. A collection of correct old specializations does not fill that gap.

The highest-value remaining theorem-level work is a structural classification that is not a standard spectral/conditional lifting: a finite/natural algorithm class explaining exactly when the fixed \(\Psi\) identifies invariants and has a useful rate-compatible EB, together with the necessary transport/recoupling information. The countable model and the random-projection model must remain compulsory negative tests.

The finite-state lead is now **PROVED and independently mathematically audited** in `MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md`. For fixed finite \(G\), maps and probabilities, the original nested \(\Psi^2\) has an exact finite tight-edge-polytope representation and is globally Lipschitz and continuous piecewise affine. Exact zeros are equivalent to a global linear \(W_2\)-EB, with a sharp finite vertex certificate and a separate Hoffman proof. No mixing hypothesis is needed. This proves that an exact-zero/no-Hölder counterexample of the stated kind must leave the fixed finite-state class. Priority of this exact application is still pending; general polyhedral error bounds are classical. The supplement also distinguishes existence of an EB from a constant compatible with a prescribed almost-firm rate formula.

## 8. Search record and limits

Mode: high-intensity targeted priority/overlap reconnaissance, not a systematic review. Date: 2026-09-09. Platform-native search and ordinary primary webpages/PDFs only. No third-party database API, account integration, or private/unpublished manuscript access. Search interface did not provide reliable total hit counts; none are invented. Duplicate arXiv/publisher versions were merged by title/authors/DOI while retaining version-specific content limits.

Core exact queries executed included:

```text
"invariant transport discrepancy" counterexample
"Markov" "metric subregularity" necessity convergence
"Wasserstein" "error bound" "Hölder"
"metric subregularity" "Markov" 2025 2026 counterexample
"transport discrepancy" "Hölder"
"transport discrepancy" "counterexample" Markov
"Markov transport discrepancy" -site:researchgate.net -site:scispace.com -site:emergentmind.com
"invariant" "transport discrepancy" "zero" -site:researchgate.net -quantum -polar
"geometric convergence" "metric subregularity" counterexample Markov
"linear convergence" "transport discrepancy" -site:researchgate.net -site:scispace.com -site:emergentmind.com
"consistent error bound" "compact" Liu Lourenco
"modulus of regularity" "compact" Kohlenbach Lopez-Acedo Nicolae
"Moduli of regularity and rates of convergence for Fejér monotone sequences" pdf
"Weak Poincaré inequalities for Markov chains: theory and applications"
"weak Poincare" "Gibbs" conditional Wasserstein
"Gibbs" "Wasserstein" "conditional" Marton 2019
"Gaussian Gibbs" "Wasserstein" "spectral gap" 2024 2025 2026
"Wasserstein" "sum" "conditional distributions" "Marton"
"Wasserstein" "approximate tensorization" Gaussian Gibbs
Rebeschini van Handel "Comparison Theorems" Gibbs measures 2014
Gaussian Gibbs sampler optimal convergence rate precision matrix Roberts Sahu 1997
"adapted Wasserstein" "topology" Pflug Pichler Backhoff 2020 2024
"same Markov" "synchronous" coupling representation
"10.1007/s10107-024-02124-w" correction erratum
"10.1007/s10107-025-02319-9" correction erratum
"2206.05213" counterexample correction
"invariant Markov transport discrepancy" 2026 September
"invariant transport discrepancy" "finite"
"transport discrepancy" "polyhedral"
"invariant transport discrepancy" "Hoffman"
"invariant transport discrepancy" "piecewise"
"Markov transport discrepancy" finite polyhedral error bound
"transport discrepancy" "linear programming"
"lexicographic" "optimal transport" "error bound"
"Hermer" "Luke" "Sturm" "finite" "subregularity"
"transport discrepancy" "Hoffman" Markov
"transport discrepancy" "piecewise" Markov
"transport discrepancy" "lexicographic"
"Lipschitz Continuity of Solutions of Linear Inequalities, Programs and Complementarity Problems" pdf
"Weak sharp minima in mathematical programming" Burke Ferris pdf
"Some continuity properties of polyhedral multifunctions" "1981" pdf
```

Secondary sites that appeared in discovery results were not used as evidence for technical conclusions. Original papers were opened instead. False positives excluded included quantum gauge invariance, unrelated graph transport metrics, generative-model discrepancies and ordinary statistical approximation error bounds. Failed HTML accesses were replaced only with available primary PDFs/official records; inaccessible theorem comparisons remain explicitly pending. Marton's correction is an identified reason for withholding sharpness priority clearance.

## 9. Exact expert return contract

```yaml
contract_version: "1.0"
expert_skill: sci-skills-literature-search
project_id: null
paper_family: null
stage_id: null
task_id: markov_global_novelty_audit
task_status: PROVISIONAL
inputs_reviewed:
  - output/ATTACK_MARKOV_SUBREG_NECESSITY_CONJECTURE.md
  - output/AUDIT_MARKOV_COUNTEREXAMPLE.md
  - output/AUDIT_MARKOV_NOVELTY_AND_JOURNAL.md
  - relevant conditional-repair theorem and audit sections
  - primary sources and exact locators in this report
outputs:
  - output/MARKOV_GLOBAL_NOVELTY_AUDIT.md
  - output/MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md
  - output/verify_finite_state_ot_strictness.py
evidence_status:
  - VERIFIED_SOURCE: direct RFI definitions, hypotheses and published open-question boundaries
  - VERIFIED_SOURCE: explicit compact modulus and best consistent error-bound precedents
  - VERIFIED_SOURCE: conditional/fibered OT, Dobrushin and 2026 scan-eigenvalue overlaps
  - VERIFIED_SOURCE: ALPW finite-block WPI counterexample and exponential-decay discussion
  - VERIFIED_USER_MATERIAL: independent mathematical audit of exact-zero/no-Hölder construction
  - AI_INFERENCE: exact comparison of source residuals, WPI profiles and rate quantifiers
  - PENDING_VERIFICATION: worldwide priority of the exact joint counterexample
  - PENDING_VERIFICATION: corrected Marton comparison and sharp Gaussian conditional EB priority
assumptions:
  - source discrepancy, random-map realization and ordinary W2 are fixed for the negative theorem
  - all-law uniform relative convergence is not replaced by pointwise or bounded-observable convergence
author_input_needed: []
manual_actions: []
quality_checks:
  - no absence-of-search-hit converted into global novelty
  - source authors credited for already-known false-zero possibility
  - compact general gauge distinguished from positive-Hölder and rate-compatible gauges
  - conditional metric distinguished from ordinary and adapted Wasserstein
  - existing mechanisms separated from exact project formulations
  - current versions distinguished from first submission dates and dynamic HTML headers
  - corrections and inaccessible theorem comparisons explicitly flagged
conflicts:
  - conflict_id: GLOBAL-FIRST-MIXING-VS-COERCIVITY
    type: novelty_scope
    claim: broad first separation between geometric Markov convergence and all finite-block coercivity
    source: ALPW arXiv 2312.11689v1 Section 3.2.3
    competing_values: established WPI counterexample versus narrower project synchronous-transport obstruction
    recommended_resolution: state the exact source residual and retain the ALPW comparison
  - conflict_id: COMPACT-GAUGE-PRIORITY
    type: novelty_scope
    claim: automatic compact generalized gauge is a new theorem principle
    source: Kohlenbach-Lopez-Acedo-Nicolae 2019 Proposition 3.2 and Liu-Lourenco Proposition 3.3
    competing_values: existing compactness/modulus construction versus its application to Psi
    recommended_resolution: present as a standard lemma with the Psi-specific compactness verification
conflict_resolution_status: UNRESOLVED
merge_permission: orchestrator_only
recommended_next_action: Freeze the exact-source obstruction theorem and complete its structural comparison with ALPW before making an abstract-level priority claim.
stage_acceptance_recommendation: REPAIR
```

**One primary next action:** freeze the exact-source obstruction theorem and complete its structural comparison with ALPW before making an abstract-level priority claim.
