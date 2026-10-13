# Independent final value review: computable forcing and its precision frontier

Date: 2026-10-13. This is a scoped mathematical and contribution review, not a worldwide priority certificate or a review of the main manuscript. The review follows `AGENTS.md`, `RESEARCH_PROTOCOL.md`, and the repository academic-writing skill in proof/referee mode. No canonical record, Claim ledger, graph, or manuscript was edited by this reviewer.

## 1. Decision and the one result worth retaining

**Retain one central result: a capped, computable precision law for directly accepted real-graph proximal outputs, with an exact critical-Hölder precision frontier.** Its strongest form uses the inverse reflection modulus to compare a computable upper bound on output distance with a computable lower bound on input distance. The general convergence theorem supplies the sufficient certificate; the complete triangular model identifies an actual power and coefficient obstruction. The two parts answer one question: how accurately must the inner equation be solved to guarantee convergence of every accepted output?

The current mathematics supports a useful technical contribution, potentially a focused methods/theory note. It does not yet support a major new convergence principle, a high-value natural application beyond established theories, or a claim of worldwide novelty. The absorption proof is short and elementary. The precision frontier, complete-output quantifiers, local cap, and finite physical length are the part that makes the package more informative than a renamed contraction perturbation lemma.

**No fatal mathematical gap was found** in the reviewed ordinary theorem, its independent forcing-budget extension, inverse-modulus test, physical GPPA extension, or the sharp capped frontier. This verdict is conditional on preserving the stated graph, window, coverage, and physical-transfer hypotheses. The conservative classical-parameter comparison and the absence of an actual inner-solver complexity theorem must remain visible.

## 2. Exact mathematics received and independently reconstructed

The primary objects are `research/candidates/inexact_rleb_forcing.md` (IRF-v1, including IRF-PHI, IRF-INV and IRF43) and `research/candidates/inexact_forcing_obstructions.md` (IF1–IF25). C249 and C213 were read as separate baselines. C249 controls exact allowed physical transitions. C213 propagates error added to an exact kernel output. Neither identity alone supplies the new accepted graph relation.

For the ordinary theorem, the decisive chain is

\[
u=\lambda\|w\|\le\widehat B(d+E),\qquad
d(y,S)\le\psi(r_F(y))\le\psi(u/\lambda),
\qquad E=\|x-y-\lambda w\|.
\]

The cap first places both the shifted Minty input and the true-residual evaluation inside their certified windows. The reflected graph condition then proves the residual bound for an arbitrary accepted witness. The inequality uses the true residual in the correct direction; it does not require a minimum-norm graph selection. An exact seed passes the residual cap by graph geometry, before any accepted-orbit argument. Finally, finite-prefix estimates prove that each actual next iterate remains in the input region, so subsequent exact-seed coverage is available. There is no circular use of retention or uniqueness.

IRF-PHI makes the mechanism particularly transparent. With

\[
\psi(\widehat B(t)/\lambda)\le\kappa_0t,
\qquad \phi(\widehat B(t))\le\theta t,
\qquad \kappa_0+\theta<1,
\]

the accepted rule \(E\le\phi(u)\) yields

\[
E\le\frac{\theta}{1-\theta}d,
\qquad d(y,S)\le\frac{\kappa_0}{1-\theta}d.
\]

This correctly separates the EB exponent from the forcing exponent. It avoids the false assertion that an EB exponent \(p\) automatically makes \(q\ge p\) necessary when the reflected exponent satisfies \(\gamma p>1\). In that regime the frontier is governed by \(1/\gamma\), as the obstruction note explicitly proves.

### The inverse-modulus test survives the discontinuity attack

Define

\[
Q(u)=\inf\{t\in[0,\rho]:u\le B(t)\},
\qquad 0\le u\le\bar u\le B(\rho).
\]

This definition does not assume that the infimum is attained. For every member \(t\) of the defining set, the scalar compatibility gives \(\psi(u/\lambda)\le\kappa_0t\). Taking the infimum proves

\[
\psi(u/\lambda)\le\kappa_0Q(u).
\]

Likewise, the actual graph inequality \(u\le B(d+E)\) directly gives \(Q(u)\le d+E\). Neither inference requires continuity away from zero. Since \(B(t)\ge t/2\) and \(B\) is continuous at zero, \(Q\) is finite on the cap, tends to zero at zero, and is positive at every positive argument.

For \(\kappa_0<\kappa<1\) and \(0<\theta<1\), the proposed test

\[
E\le\min\left\{\theta Q(u),\ Q(u)-\frac{\psi(u/\lambda)}{\kappa}\right\}
\]

therefore proves

\[
\psi(u/\lambda)\le\kappa[Q(u)-E]\le\kappa d,
\qquad E\le\frac{\theta}{1-\theta}d.
\]

The first term controls physical length and localization; the second enforces the desired distance decrease. Its posterior interpretation is exact: \(Q(u)-E\) is a certified lower bound on the unknown input distance, whereas \(\psi(u/\lambda)\) is a certified upper bound on output distance. Exact seeds satisfy both terms because \(\kappa>\kappa_0\). This also covers zero absorption without strict positivity of the EB gauge. The separate residual cap remains necessary for using a local certificate.

This is a better main stopping rule than presenting \(E\le\eta\psi(u/\lambda)\) as universally optimal. When \(\psi(u/\lambda)\ll Q(u)\), the inverse test can permit substantially larger defects. It is still only a sufficient scalar certificate. No proof establishes that it is the largest safe rule for every operator having the displayed upper bounds.

The inverse test also has a cleaner finite-acceptance interface. Its budget is at least \(c_*Q(u)\), where \(c_*=\min\{\theta,1-\kappa_0/\kappa\}>0\). If true graph pairs from an inner method converge to an exact seed with \(u_*>0\) strictly below the cap, then eventually \(u_j\ge u_*/2\), while the equation defects tend to zero. The positive bound \(c_*Q(u_*/2)\) proves finite acceptance. This argument requires neither positive-point continuity nor strict positivity of \(\psi\). It is an interface conditional on inner convergence, not a construction or complexity analysis of that inner method.

### Physical GPPA scope is correct but genuinely conditional

The kernel proof uses \(\|v(x)-v(p)\|\le A d^\beta\) and never needs a physical point whose image equals \(v(x)-e\). That avoids an invalid lift for a nonsurjective kernel. IRF43 has the correct factor

\[
\kappa=\left(\frac{CA}{1-\theta}\right)^{1/\beta},
\qquad CA+\theta<1.
\]

However, the physical-transfer hypothesis must control every accepted transition, including outputs not yet known to remain in the local input set. It is not a consequence of kernel residual control. At zero, this hypothesis is what forbids motion inside an invisible kernel fiber. The claim is thus a valid conditional extension, not proof that arbitrary noninjective-kernel methods converge physically.

## 3. The sharp frontier is an actual theorem, with limited meaning

For the critical complete family

\[
J(s,t)=(s+a|t|^\gamma,bt),\quad
0<\gamma<1,\quad 0<b<1,\quad p=1/\gamma,
\]

write

\[
W(t)^2=a^2|t|^{2\gamma}+(1-b)^2t^2,
\qquad H_q(T)=T^{\gamma q-1}
\bigl(a^2+(1-b)^2T^{2-2\gamma}\bigr)^{q/2}.
\]

For \(q\ge p\), the cap \(\|\lambda w\|\le W(T)\) is exactly \(|t|\le T\) on the complete accepted graph. The note correctly proves the equivalence

\[
\text{all accepted trajectories from }d(x^0,S)\le T
\text{ have finite length and converge to }S
\quad\Longleftrightarrow\quad
\eta H_q(T)<1-b.
\]

Sufficiency bounds every error direction by \(\|e\|\le\delta|t|\), so \(|x_2|\ge(1-\delta)|t|\) and \(|y_2|\le b|x_2|/(1-\delta)\). Exact outputs supply coverage of the whole input tube. Necessity uses the admissible constant-normal trajectory at \(t=T\), which starts at distance \(bT\), has positive constant tangent displacement, and fails at equality as well as above it. No favorable sign, branch, or selected residual is hidden in this proof.

The three power regimes are correct. When \(\gamma q<1\), arbitrarily small nonzero normal levels admit both escape from a zero and persistent drift. At \(\gamma q=1\), the asymptotic coefficient has a strict endpoint. When \(\gamma q>1\), every fixed finite coefficient works on a small enough cap. The separate zero-absorption threshold \(\eta H_q(T)<1\) is strictly weaker than the convergence threshold. The far-output construction verifies that a sufficiently small initial distance cannot replace the cap in a purely local theorem.

The sharp reflected exponent and true EB exponent are both attained by this complete operator. Its local hypo/cohypomonotonicity failures are analytic ratio limits, and the translation-invariance addition excludes every zero anchor in the weak-Minty inequality. These are meaningful hypothesis exclusions. They do not refute HPE convergence theorems, which impose hypotheses the model violates.

The exact dynamics of the diagnostic model are nevertheless simple. With

\[
\mathcal H(s,t)=\left(s+\frac{a}{1-b^\gamma}|t|^\gamma,t\right),
\]

direct substitution gives

\[
\mathcal H\circ J\circ\mathcal H^{-1}(\xi,t)=(\xi,bt).
\]

The conjugacy is Hölder rather than locally bi-Lipschitz at the zero line. This calculation does not remove the Euclidean forcing obstruction, but it does prevent describing the example as intrinsically complicated dynamics or a major natural application. Its value is the precision loss caused by a sharp Hölder tangent displacement and a complete all-output stopping relation.

## 4. Strongest prior recoveries and honest exclusions

**Rockafellar 1976.** Independently opened the [author-hosted scan](https://sites.math.washington.edu/~rtr/papers/rtr066-MonoOpProxPoint.pdf), particularly Proposition 3, p. 882, and the criterion/theorem locations reported in `rockafellar_hpe_review.md`. For maximal monotone \(F\), Proposition 3 converts subproblem residual to exact-output error. In present notation, \(y=J_{\lambda F}(x-e)\), so nonexpansiveness gives \(\|y-J_{\lambda F}x\|\le\|e\|\). Summable graph defects therefore supply the classical summable output-error condition for the same uncorrected iterates. This recovery does not rely on unique zeros. The stronger inverse-Lipschitz rate theorem has separate assumptions and must not be conflated with general metric subregularity.

**Combettes–Pennanen 2004.** Independently read [the author preprint](https://pcombet.math.ncsu.edu/sicon3.pdf), Algorithm 1.1, Lemma 2.4 and Theorem 3.1. For one operator, relaxation one, output perturbation zero, and their inclusion error equal to \(-e\), its update is exactly the current uncorrected graph-defect update. The theorem supplies local convergence under maximal cohypomonotonicity, its parameter/localization conditions, and a small summable-error budget. Lemma 2.4 maps the resolvent to a relaxed monotone resolvent. Thus nonmonotonicity and an equation residual are not new algorithmic features. The sharp triangular model escapes this particular route because no finite local cohypomonotonicity constant exists.

**A direct stronger classical calculation.** This paragraph is an independent derivation. Suppose the same graph points satisfy \(\langle y-p,w\rangle\ge-\rho\|w\|^2\), the true linear EB has constant \(K\), and \(\lambda>2\rho\). At \(z=x-e=y+\lambda w\), expansion gives

\[
d(y,S)\le\vartheta d(z,S),\qquad
\lambda\|w\|\le c_\rho d(z,S),
\]
\[
\vartheta=\frac{K}{\sqrt{K^2+\lambda(\lambda-2\rho)}},
\qquad c_\rho=\sqrt{\frac\lambda{\lambda-2\rho}}.
\]

Consequently a graph rule \(E\le\sigma\lambda\|w\|\) yields
\(d(y,S)\le\vartheta d(x,S)/(1-\sigma c_\rho)\) whenever \(\sigma c_\rho<1\). The sufficient contraction threshold is \(\sigma c_\rho<1-\vartheta\). Ordinary monotonicity is \(\rho=0\), and admits a positive tolerance for every \(\lambda>0\). By comparison, the IRF direct certificate with \(\omega(t)=t\), \(\psi(r)=Kr\) requires \(K/\lambda+\sigma<1\). The new theorem therefore recovers a conservative overlap, not the full classical parameter range or best rate. The draft now states this correctly.

**Modern HPE and metric frameworks.** Independently read the [Buscaglia–Lotito–Parente–Solodov author manuscript](https://pages.cs.wisc.edu/~solodov/blps24VMprox.pdf), Definitions 2.2–2.3, Theorems 4.4 and 5.1, and the surrounding comparison. Their setting is maximally monotone and their rate assumption is inverse calmness, which does not require a unique zero. Theorem 5.1 represents summable-relative-output-error iterates through an asymmetric metric framework. Hence neither nonisolated zeros nor the mere presence of an HPE correction establishes noncontainment. A fixed same-state bridge must be checked, and broad corrected-framework representability must be conceded where proved. The current sharp model is nonmonotone; the theorem's general all-output assertion is not directly supplied by the checked monotone framework.

The 2026 GPPA stability primary text at [arXiv:2608.01584v1](https://arxiv.org/html/2608.01584v1) was independently opened. Its regularized-operator and persistent-output-error result remains a relevant positive baseline, as mapped in `primary_review.md`. It is not literally the fixed-operator real-graph acceptance relation here. The Wang–Li–Ng full text and the exact 2026 warped-iteration source were not independently recovered in this review; their assigned primary-source reports remain necessary before any comprehensive external-priority assertion.

## 5. Value, remaining obligations, and exclusions from the headline

The inverse-modulus rule improves the practical content: it identifies a computable posterior input-distance lower estimate, it allows forcing power to differ from the EB power, and it exposes the error scale \(1/\gamma\) in a way matched by a complete countermodel. The cap and all-output quantifiers make this a reliable acceptance theorem rather than a selected good-branch analysis. These points justify retaining the result.

The mathematical mechanism remains scalar absorption plus a summable step envelope. The result does not itself construct an inner solver, estimate the required constants, recognize an exact zero in finite precision, or accommodate approximate graph membership. Those are substantive implementation boundaries, not mere editorial footnotes. If practical algorithmic value is claimed, a specified inner method with a verified acceptance or work bound is the next required evidence.

A natural cubic game already covered by a cohypomonotone transformation or a direct Banach argument cannot certify an exclusive advantage for this theorem. Such an example may illustrate the stopping rule, but its natural origin does not turn an overlapping convergence guarantee into a new theorem class. No priority or application claim should be based on an example until its actual strongest classical recovery is recorded.

The recommended headline should concern **computable inner precision under reflected Hölder regularity**, not “a new nonmonotone PPA,” “the first relative-error PPA,” “a generalization of all classical inexact PPA,” or an unqualified “optimal stopping rule.” The exact finite-cap coefficient is sharp for the displayed complete model; the universal theorem's sufficient constants are not proved optimal. C213's convolution, the elementary monotone overlap, and the conditional kernel migration should remain supporting material.

## 6. Verification and handoff record

The review reconstructed the general one-step proof, zero absorption, exact-seed cap, gauge domains, inverse infimum/jump arguments, finite-prefix retention, physical-transfer use, capped iff proof, endpoint counterexample, forcing-power regimes, and finite hypo/cohypomonotonicity exclusions. The repository frontier verifier was run successfully:

`python3 research/code/inexact_forcing_attack/check_frontier.py`.

An independent Python calculation also reconstructed both-sign graph equations and the Hölder conjugacy; for \(a=\lambda=1\), \(b=1/4\), \(\gamma=1/2\), \(T=10^{-2}\), it obtained

\[
\eta_{\rm conv}=0.7458048477315102,
\qquad \eta_{\rm abs}=0.9944064636420137.
\]

At 90% of the convergence threshold, 10,000 sampled complete accepted errors (seed 20261013, both normal signs and arbitrary Euclidean error directions) obeyed the proved factor \(\kappa=0.769230769230769\). These finite checks support the displayed instances; the analytic arguments establish the quantified result. A monotone comparison with \(K=2\), \(\lambda=1\), \(\sigma=0.05\) gave the classical factor 0.941502306315701 despite \(K/\lambda=2\), verifying concretely why full classical recovery cannot be claimed.

Reader route: decision → exact accepted relation → inverse-modulus proof → sharp family → strongest prior recoveries → contribution boundary. Each source paragraph separates source facts from this review's algebraic mappings. No layout, venue-compliance, manuscript-release or full-library claim is made. The eventual canonical text must receive its own cold read if its statement or normalization changes.

## 7. Actual canonical cold read and closed findings

The subsequently written canonical texts were read directly, not accepted by identity with the candidates:

| Canonical artifact | SHA-256 of the received bytes |
| --- | --- |
| `research/topics/inexact_ppa/real_graph_stopping.md` | `0772536451595f614bd85100c534f189d8fb61239adb3c95710ebe0770b3ed12` |
| `research/topics/inexact_ppa/sharp_precision_frontier.md` | `13fa339f1f2cad89aa1468598129beaa8ace50eac73f11a64fc413141b3da12b` |

C275 IG1–IG11 preserves the inverse-modulus proof, all accepted graph witnesses, true-residual direction, exact-seed nonemptiness, cap, zero absorption and finite-prefix retention. IG12–IG14 are the direct forcing-budget specialization. The implementation paragraph now uses the positive lower budget proved above and explicitly says \(x\notin S\), so it does not confuse a nonzero vector with positive distance to a nonisolated zero set.

One actual mathematical omission was found and repaired in the canonical power specialization. Before repair, IG14 omitted \(0<\gamma\le1\). Its formula need not bound smaller scales for \(\gamma>1\): \(\gamma=2\), \(p=q=1/2\), \(c=a=0.1\), \(L=\lambda=\rho=1\) gives a displayed coefficient sum of 0.2, but at \(t=10^{-8}\), \(\psi(B(t))/t\approx707.1068\). The canonical version now states the intended exponent and coefficient ranges and restricts \(Q(u)\asymp u^{1/\gamma}\) to the appropriate positive-Hölder-coefficient case. This closes the omission; it did not affect IG1–IG11.

C276 was also read after migration. The new complete-fiber formula IF26 is correct in both directions: at fixed normal parameter \(t\), the normal defect is \(r-t\), and the remaining Euclidean error budget gives precisely the displayed tangent interval. The new accepted-output-strip example satisfies the cap and graph test and lies outside the original exact-output strip, correctly identifying the missing set inclusion. The canonical text now explicitly declares \(\eta\ge0\) and \(q>0\). The sharp iff, equality drift, cap removal and all-anchor weak-Minty exclusions remain valid.

**Canonical verdict:** no unresolved fatal mathematical objection in C275 or C276 at the recorded bytes. The two constitute the same retained precision-law result described in Section 1. This internal acceptance does not change the moderate value judgment, the strongest-prior overlaps, or the external-priority limits. The main manuscript was not reviewed or modified.
