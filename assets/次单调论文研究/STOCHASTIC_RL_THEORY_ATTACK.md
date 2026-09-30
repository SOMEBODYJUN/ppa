# Stochastic RL: legal coupling interface, a dilution obstruction, and a flagship kill gate

Date: 2026-09-09. Task: `stochastic_rl_theory_attack`.

## Verdict

**Mathematical interface: GO as a provisional project theorem. A new flagship stochastic-RL theory: REPAIR / not established. The naive scalar lift of the genuinely nonlinear deterministic RL–EB mechanism: KILL.**

The distinction is substantive:

1. A probability reflector cannot be defined by the signed measure `2 μP − μ`. A legitimate reflector lives in a specified coupling, with its marginals and its reference invariant law recorded.
2. The same-noise relative displacement is not the actual Wasserstein displacement of successive laws. The stationary reference particle keeps moving. Ignoring that fact invalidates a direct deterministic finite-length proof.
3. For the linear exponent and the same-noise coupling, reflected geometry is **exactly** the Hilbert form of almost-firm-nonexpansiveness in expectation, not an extension.
4. There is a further obstruction to the nonlinear exponent: small-mass dilution prevents an ordinary full-law `q > 1` error bound for the usual squared-integral residuals, even when the underlying deterministic operator has the desired higher-order error bound. One must compose the conditional/pointwise certificates **before** averaging, or introduce and justify a different residual/shape-restricted domain.
5. A legal coupling-level theorem below does permit genuine `γ < 1`, multivalued selection, correlated initial laws, a nonisolated invariant family, whole-law convergence, and finite Wasserstein length. An explicit shear-plus-refresh class lies outside every finite almost-FNE-in-expectation bound. However, that example is a nonlinear deterministic mechanism combined with a conditional refresh. It establishes strict hypothesis-level separation, **not** a research-level strict extension of all existing stochastic convergence theories.

The useful new research lead is therefore the **compatibility / impossibility theory for lifting nonlinear graph certificates to laws**, not a renamed expected averagedness theorem. Priority of the elementary no-go below remains unverified.

## 1. Inputs and evidence scope

Reviewed the RL manuscript's definitions, coupled Minty chart, allowed-transition distinction, general-gauge Theorem 3.1, critical-exponent discussion and natural-class conclusions in `upload/01-RL_PPA_T5_core_manuscript_2026-09-07.md`. Reviewed the pertinent proof and comparison sections of all five existing Markov reports:

- `ATTACK_MARKOV_SUBREG_NECESSITY_CONJECTURE.md`;
- `AUDIT_MARKOV_COUNTEREXAMPLE.md`;
- `AUDIT_MARKOV_NOVELTY_AND_JOURNAL.md`;
- `ATTACK_MARKOV_CONDITIONAL_REPAIR.md`;
- `AUDIT_MARKOV_CONDITIONAL_REPAIR.md`.

The present task directly revisited the original HLS formulas, Definition 3.1, Definition 3.3 and Theorem 2.6 in [HLS, *Rates of Convergence for Chains of Expansive Markov Operators*](https://arxiv.org/html/2206.05213v3). Conditional Wasserstein is an existing tool; its disintegration construction is documented in [Chemseddine–Hagemann–Steidl–Wald, JMLR 2025](https://jmlr.org/papers/v26/24-0586.html). No new transport metric is claimed.

`PROJECT_PROOF` below denotes a complete local derivation, classified as `AI_INFERENCE`, not a peer-reviewed or globally novel result. The output is provisional until independently audited by the orchestrator.

## 2. Exact relation to HLS: where renaming must stop

Let `X,Y` be a coupling of two input laws and apply the same update label. Set

\[
h=X-Y,\qquad a=T_\xi X-T_\xi Y,\qquad b=h-a.
\]

The identity

\[
\|a\|^2+\|b\|^2=\tfrac12\bigl(\|h\|^2+\|2a-h\|^2\bigr)
\tag{2.1}
\]

holds samplewise. Consequently

\[
\mathbb E\|2a-h\|^2\le L^2\|h\|^2
\quad\Longleftrightarrow\quad
\mathbb E\|a\|^2+\mathbb E\|b\|^2
\le\tfrac{1+L^2}{2}\|h\|^2.
\tag{2.2}
\]

Thus for the source parameter `α_H = 1/2`, this is exactly expected almost-firmness with

\[
\epsilon=(L^2-1)/2.
\]

For the source convention `0 ≤ ε < 1`, the corresponding range is `1 ≤ L² < 3`; stronger reflected bounds can of course imply the zero-violation bound. More generally, the HLS coefficient on `b²` is `(1−α_H)/α_H`. Formula (2.2) is its balanced coefficient-one slice. These are literal algebraic identities, not a claim that all parameter slices coincide.

The source's law-level inequality additionally quantifies over the indicated optimal input couplings. An estimate for one handpicked coupling is not automatically that statement. Nor does its invariant discrepancy automatically identify invariant laws; source identification and regularity assumptions are separate.

**KILL condition:** if proposed stochastic RL means only (2.2), followed by the same source discrepancy EB and scalar decay recurrence, the proposal is a reformulation of HLS.

## 3. Why physical and law-space displacements cannot be interchanged

Suppose `Y ~ π` and `Y⁺ = TξY ~ π`. Stationarity is equality of laws, not the random-variable identity `Y⁺ = Y`. The synchronous defect is

\[
b=(X-X^+)-(Y-Y^+).
\]

In general neither `W₂(μ,μP) ≤ ‖b‖₂` nor `X−X⁺ = b` holds.

### Natural parallel-projection test

Let `T_j(u,v)=(u,j)`, with a fair bit `j`. Then `μP=μ_U⊗β`, where `β=(δ₀+δ₁)/2`. Existing project proofs give

\[
\Psi(\mu)=W_2(\mu_V,\beta).
\]

For

\[
\mu_t=\tfrac12\delta_{(1/2-t,0)}+
\tfrac12\delta_{(1/2+t,1)},\quad 0<t<1/2,
\]

the source residual is zero, while `μ_tP ≠ μ_t`. An optimal input comparison keeping the second coordinate identical has synchronous defect zero at every step. Any bound on the genuine law step by this defect is false.

### A correct recoupling inequality, and its limitation

Define the ghost law

\[
\widehat\mu=\mathcal L(Y^+ + X-Y),\quad
\mathcal C=W_2(\mu,\widehat\mu).
\]

The actual joint variables give

\[
W_2(\mu,\mu P)\le\mathcal C+\|b\|_{L^2}.
\tag{3.1}
\]

This is valid because `Y⁺+X−Y−X⁺=b`. But `C` is an additional correlation/recoupling loss, not zero by stationarity. Assuming an unexplained upper bound on it merely relocates the hard verification problem. In the projection witness it can carry the entire law movement.

## 4. Small-mass dilution: a no-go for the naive nonlinear lift

### Proposition 4.1 — superlinear full-law EB obstruction

Let the target invariant be `δ₀` on a Euclidean state space containing a nonzero point `a`. Let a nonnegative native residual be

\[
\mathcal R(\mu)^2=\int c(x)\,\mu(dx),\qquad
c(0)=0,\quad 0<c(a)<\infty.
\]

The statement also holds if this equality is replaced by an upper bound for the mixture witnesses below. Then on **no full W₂ neighborhood of `δ₀`** is there a finite `K` and exponent `q>1` such that

\[
W_2(\mu,\delta_0)\le K\mathcal R(\mu)^q.
\tag{4.1}
\]

Proof. Put `μ_ε=(1−ε)δ₀+εδ_a`. Then

\[
W_2(\mu_\epsilon,\delta_0)=\sqrt\epsilon\|a\|,
\qquad \mathcal R(\mu_\epsilon)=\sqrt{\epsilon c(a)}.
\]

Inequality (4.1) would imply

\[
\|a\|\le Kc(a)^{q/2}\epsilon^{(q-1)/2},
\]

which is impossible as `ε ↓ 0`. These laws eventually lie in every W₂ ball about `δ₀`. ∎

The result does **not** forbid every `q>1` Wasserstein error bound for every conceivable residual. It applies to this native quadratic-integral class, including a synchronous residual to a Dirac target, and to any other residual bounded above on these mixtures by a constant times `√ε`. A residual rescaled with mass, a nonquadratic residual, a support/shape-restricted family, or a different target geometry requires separate analysis.

### Corollary 4.2 — the critical deterministic exponent need not survive averaging

Any gauge valid in Proposition 4.1 must satisfy `ψ(t) ≥ c₀t` for all sufficiently small `t`, for some `c₀>0`. Therefore if a scalar lifted reflected estimate only supplies `B(d) ~ C d^γ`, `0<γ<1`, its composition `ψ(B(d))` cannot certify `ψ(B(d)) ≤ κd`, `κ<1`, near zero. The deterministic critical mechanism `γq = 1` requires `q>1`, precisely the exponent destroyed by dilution.

This is a **certificate obstruction**, not a nonconvergence theorem.

### Concrete deterministic-to-law failure

For a state with tangential coordinate `t` and normal coordinate `y`, consider

\[
J(t,y)=(t+c|y|^\gamma,\eta y),\quad
c>0,\quad 0<\eta<1.
\]

Its normal distance decreases geometrically and its step obeys the pointwise higher-order estimate

\[
|y^+|\le\eta c^{-1/\gamma}\|J(t,y)-(t,y)\|^{1/\gamma}.
\]

For laws mixing a solution state with a fixed normal excursion, the distance to the invariant family `P₂(R×{0})` and the root-mean-square step both scale as `√ε`. The aggregated order `1/γ>1` estimate fails. The pointwise proof remains correct; only its purported scalar law lift fails.

### Correct moment order

From a pointwise bound `d_+ ≤ K r^q`, the valid integrated statement is

\[
\|d_+\|_2\le K\|r\|_{2q}^{q},
\tag{4.2}
\]

not `K‖r‖₂^q` when `q>1`. If `r ≤ C d^γ`, then composing before integration gives

\[
\|d_+\|_2\le KC^q\|d\|_{2q\gamma}^{q\gamma}.
\]

At `qγ=1`, this becomes a genuine L² contraction. This is the correct route for a nonlinear interface.

## 5. A legal coupling-level RL–gauge theorem

The following formulation is deliberately explicit about law couplings, coverage and the invariant reference family. It never subtracts probability measures.

Let `(M,D)` be a complete space of probability laws, with `D=W₂`, or the existing conditional W₂ on a fixed conserved marginal. Let `I⊂M` be a nonempty closed common invariant family for all allowed transition kernels. If policies vary, the conclusion below concerns a common invariant family; it is not a statement about an undefined single stationary kernel.

For each `μ`, prescribe an admissible reference-coupling family `Q(μ)` whose first marginal is `μ` and whose second marginal belongs to `I`. Define

\[
E(\mu)=\min_{\chi\in Q(\mu)}\|X-Y\|_2.
\tag{5.1}
\]

Require measurable realizability and attainment where used, and include the diagonal reference when `μ∈I`. Then `D(μ,I)≤E(μ)` and `E^{-1}(0)=I`. The family `Q` must be specified from the model, not fabricated after observing convergence. If `Q` is the family of all transport couplings with invariant targets, `E` is ordinary set distance whenever the minimum exists. Restricting `Q` can strengthen the certificate topology and must be disclosed.

For every allowed law transition `μ→μ⁺`, assume there is a joint law of `(X,Y,X⁺,Z)` such that:

- `X~μ`, `X⁺~μ⁺`; the joint `(X,X⁺)` is a **law transport coupling**, not necessarily the physical Markov pair;
- `(X,Y)` realizes (5.1), and `(X⁺,Z)∈Q(μ⁺)`;
- all equal conserved variables required by a conditional metric remain equal in the relevant couplings;
- with `d=|X−Y|` and `s=|X−X⁺|`, almost surely

\[
|2X^+-X-Y|\le\omega(d),\qquad
|X^+-Z|\le\psi(s/\lambda).
\tag{5.2}
\]

Here the gauges are nondecreasing, vanish at zero, and their effective pointwise domain is part of the assumption. Write

\[
B(t)=\tfrac12(t+\omega(t)),\qquad
\Phi(t)=\psi(B(t)/\lambda).
\]

### Theorem 5.1 — energy, nonlinear composition and whole-law convergence

Every such transition satisfies

\[
D(\mu,\mu^+)\le\|s\|_2\le\|B(d)\|_2,
\qquad E(\mu^+)\le\|\Phi(d)\|_2,
\tag{5.3}
\]

and

\[
D(\mu^+,I)^2+\|s\|_2^2
\le\tfrac12\left(E(\mu)^2+\|\omega(d)\|_2^2\right).
\tag{5.4}
\]

For (5.4), in a conditional metric the reference marginal `Y` must be in the same conserved-marginal class as `X⁺`. When `Q` is restricted, (5.4) controls ordinary distance to `I`, **not necessarily the stronger certificate `E(μ⁺)`**. This distinction is important.

Suppose on an open law domain `V⊂M`, every input with `E(μ)≤r` has a nonempty set of allowed transitions and all such transitions admit the above joint realization. Suppose also

\[
\Phi(d)\le\kappa d\quad\text{almost surely},\quad 0<\kappa<1,
\]

and a nondecreasing `B̂` satisfies `‖B(d)‖₂≤B̂(E(μ))`. Set

\[
H(e)=\sum_{k\ge0}\widehat B(\kappa^ke).
\]

If `E(μ₀)≤r`, `H(E(μ₀))<∞` and

\[
\operatorname{dist}_D(\mu_0,M\setminus V)>H(E(\mu_0)),
\tag{5.5}
\]

then every successive allowed law selection continues indefinitely, remains in `V`, has finite D-length and converges to a single law `π∞∈I`. Quantitatively,

\[
E(\mu_k)\le\kappa^kE(\mu_0),\quad
\sum_{j\ge k}D(\mu_j,\mu_{j+1})
\le\sum_{j\ge k}\widehat B(\kappa^jE(\mu_0)).
\tag{5.6}
\]

Proof. For `a=X⁺−Y`, `b=X−X⁺`, one has `a+b=X−Y`. The triangle and parallelogram identities give `s≤B(d)` and `|a|²+s²≤(d²+ω(d)²)/2` pointwise. The first and last marginals give the transport bounds in (5.3)–(5.4); the output reference gives `E(μ⁺)≤‖X⁺−Z‖₂≤‖Φ(d)‖₂`. Pointwise compatibility yields contraction of `E` after integration. Summing the successive D-step bounds and using (5.5) proves continuation by induction, without assuming future coverage. The law sequence is Cauchy in complete `M`; its limit lies in closed `I` since `D(μ_k,I)≤E(μ_k)→0`. The same tail sum proves (5.6). ∎

This proves **law** convergence and finite **Wasserstein** length. Physical sample paths can move forever at stationarity. No almost-sure convergence of the original particles is asserted.

For `ω(t)=Lt^γ`, `0<γ≤1`, Jensen and Minkowski give the explicit

\[
\widehat B(e)=\tfrac12(e+Le^\gamma).
\]

More generally, `‖Φ(d)‖₂` is controlled by the upper concave envelope of `z↦Φ(√z)²` evaluated at `E(μ)²`, provided the pointwise support interval is included in that envelope's domain. This is the correct moment closure; replacing it by `Φ(E(μ))` without the needed concavity is generally false.

### Coverage and nonvacuity gate

The theorem does not prove kernel existence or reference attainment from geometry. Nor does it prove the joint coupling compatible with two independently selected certificates exists. These are explicit coverage and matching requirements, analogous to the deterministic manuscript's allowed-transition issue. An abstract theorem satisfying them only by using an already-known invariant limit is not a native verifier.

In particular, once `(X,X⁺)` is permitted to be a nonphysical law coupling, (5.2) is not automatically an inequality on the original sampled proximal graph. A future native verifier must show that the chosen recoupling retains the required graph / selection information. The theorem cannot be advertised as directly applying to all random proximal maps merely because each physical update has an RL estimate.

## 6. A fully verified nonlinear multivalued class beyond HLS's finite expected almost-FNE hypothesis

This is an existence / separation example, **not the proposed flagship application**.

Let state space be `R×[0,1]×{0,1}` with Euclidean cost. Let `β` be the fair-bit law and choose

\[
\gamma=1/2,\qquad\eta=1/4,\qquad C\in[1,11/10].
\]

At each step, conditional on `(t,y)`, choose any measurable probability law for `C` supported in that interval; it may be a deterministic branch or a genuinely random selection. Require that this selection does not inspect the old bit given `(t,y)`. Update the law by the kernel

\[
(t,y,z)\longmapsto
(t+C\sqrt y,\;y/4,\;Z_{\rm fresh}),\quad
Z_{\rm fresh}\sim\beta\text{ independently of the updated slow coordinates}.
\tag{6.1}
\]

Every such kernel has the same invariant family

\[
I=\{\nu(dt)\delta_0(dy)\beta(dz):\nu\in P_2(\mathbb R)\}.
\tag{6.2}
\]

Indeed invariant normal second moments force `y=0`; then the tangential coordinate is fixed and the bit is refreshed. Conversely every law in (6.2) is invariant. Finite second moments and global coverage hold for every allowed selection. Different `C` give genuinely different transition outputs when `y>0`. The associated inverse graph `F(w)∋x−w` for all these allowed `w` is set-valued; the theorem concerns this allowed-transition family, not an unproved AP-RL condition for its entire Minty inverse. Distinct outputs at one input actually preclude that stronger all-pairs condition.

### Native reference, preserving initial correlations

Disintegrate `μ(dz|t,y)` and define

\[
E(\mu)^2=\int y^2\,d\mu+
\int W_2(\mu(dz\mid t,y),\beta)^2\,\mu_{t,y}(dt,dy).
\tag{6.3}
\]

Couple the old bit `z` optimally to `Z~β` conditionally on `(t,y)`. Define `Y=(t,0,Z)`. Its law is invariant because the target conditional law of `Z` is always `β`; the cost is exactly (6.3). This supplies `Q(μ)` explicitly and vanishes exactly on (6.2). It does not discard correlation between the initial bit and the slow state.

Sample `C` independently of that bit pair conditional on `(t,y)`, and set

\[
X^+=(t+C\sqrt y,y/4,Z),\quad
Z_*=(t+C\sqrt y,0,Z).
\]

The marginal of `X⁺` is precisely the kernel-updated law in (6.1). This is allowed even though its coupling with the original bit is not the physical refresh coupling. The target `Z` is independent of `(t,y,C)`, so `Z_*` has an invariant law. The output bit is independent of both output slow coordinates; consequently

\[
E(\mu^+)^2=\tfrac1{16}\int y^2\,d\mu\le\tfrac1{16}E(\mu)^2.
\tag{6.4}
\]

### Genuine nonlinear RL and pointwise order-two EB

Put `d=|X−Y|=√(y²+|z−Z|²)≤√2`, `s=|X−X⁺|`. Then

\[
|2X^+-X-Y|^2
=4C^2y+\tfrac14y^2+|z-Z|^2
\le d^2+4(11/10)^2d.
\]

Thus choose `ω(t)=√(t²+4(11/10)²t)`, genuinely of order `t^{1/2}`. Further, `s≥C√y≥√y`, giving the pointwise EB

\[
|X^+-Z_*|=y/4\le s^2/4.
\tag{6.5}
\]

The composed gauge has

\[
\frac{\Phi(t)}t
=\frac1{16}\left(\sqrt t+
\sqrt{t+4(11/10)^2}\right)^2
\le\frac1{16}\left(2^{1/4}+
\sqrt{\sqrt2+121/25}\right)^2<0.852
\]

for `0<t≤√2`. Hence the actual nonlinear RL–EB interface certifies a uniform contraction with `κ=0.852` for **all initial laws on this state domain**, including correlated laws. The stronger direct estimate (6.4) gives `κ=1/4`; do not claim the scalar interface has the best rate.

Also

\[
\|B(d)\|_2\le\widehat B(E),\qquad
\widehat B(e)=\tfrac12\left(e+\sqrt{e^2+4(11/10)^2e}\right).
\]

Its geometric-series sum is finite. Thus Theorem 5.1 gives a whole-law limit in (6.2) and finite W₂ length for every allowed sequence of kernels. No continuity of the policy is needed for this explicit verification, only the stated measurable kernels and conditional independence. If the law of `C` depends on the old bit, this proof no longer applies without a new coupling; that larger selection scope is not claimed.

### Strict separation from finite expected almost-FNE

Take a fixed allowed constant branch `C=c` and compare states `(t,h,z)` and `(t,0,z)` under the same fresh bit. Their mean squared output difference is

\[
c^2h+h^2/16,
\]

while their squared input difference is `h²`. The ratio diverges as `h↓0`. Thus no finite expected almost-nonexpansiveness constant, hence no finite HLS expected almost-FNE constant, holds on any full state neighborhood of `y=0` in the native Euclidean metric. The same failure is visible directly between the output laws of these Dirac inputs; changing the random representation cannot repair it.

This is strict separation from the specified HLS hypotheses. It does **not** show superiority over partial/normal-coordinate convergence theory, state-dependent Lyapunov techniques, or deterministic convergence followed by conditioning. In fact the model was deliberately made triangular and admits the stronger elementary estimate (6.4). It must therefore be **KILLED as a standalone flagship novelty witness**.

## 7. Required adversarial tests

### 7.1 The natural parallel projection is detected

For `T_j(u,v)=(u,j)`, freeze the conserved marginal `ν=μ_U` and use conditional transport. Set

\[
E(\mu)=\left[\int W_2(\mu(dv\mid u),\beta)^2\,\nu(du)\right]^{1/2}.
\]

Couple the conditional old coordinate optimally to `V'~β`, let `Y=X⁺=(u,V')`, and use `Z=Y`. Then `|2X⁺−X−Y|=|X−Y|`, `s=|X−Y|`, and output reference error is zero. The reference coupling gives the actual updated law and exact identification. For `μ_t` of Section 3, `E(μ_t)=1/√2`, although `Ψ(μ_t)=0`. Thus the legal definition is not blind to the counterexample. The metric is stronger than ordinary joint W₂; this is not a same-topology necessity repair.

### 7.2 Pointwise gauges cannot simply be applied to RMS residuals

Section 4 gives an exact analytical counterexample. It remains valid on a bounded state domain: small probability, rather than a large state excursion, defeats the asserted superlinear full-law EB.

### 7.3 Accurate zeros plus energy need not imply convergence

On `R`, the deterministic transition `T(x)=−x` has unique point target zero, reflection modulus `ω(t)=3t`, step `s=2|x|`, and exact output EB `|T(x)|=s/2`. The composed estimate is `Φ(t)=t`, not a strict decrease. The actual nonzero orbit is period two. Thus correct target identification and finite reflection/EB constants are insufficient without the compatibility condition. For the full Markov invariant-law problem of this deterministic sign-flip kernel, invariant laws are symmetric, so this test is expressly a fixed-point/Dirac test; it is not falsely advertised as a unique-invariant-law Markov example.

### 7.4 Different residuals cannot be swapped into one energy identity

The existing conditional report gives a two-bit law with squared invariant distance `1/4`, next squared distance `1/8`, and conditional-specification residual squared `1/4`. Their sum is `3/8>1/4`. Hence a native conditional residual need not be the synchronous dissipation in an RL identity. Theorem 5.1 insists that the same coupling supplies reflection and step, and that the output EB is verified in that coupling.

### 7.5 A stronger, genuinely multivalued natural pressure test

The sibling application task supplied the unit-sphere normal-cone example. On sphere states the full limiting-normal resolvent is `{x,−x}`. Fair sign selection gives `K=(I+A)/2`, with `A` the antipodal pushforward, so `K²=K` and all laws reach an antipodally symmetric invariant law in one step. Under the physical common-sign representation, output pair distances do not decrease and the expected synchronous defect is `2|x−y|²`. Thus the source expected-firm energy and any compatible EB of its own cannot explain the actual one-step symmetrization without accounting for recoupling.

This corroborates the recoupling issue on a true multivalued proximal object. Its positive resolution is elementary group averaging / two-point fibers, not a new flagship theorem. Detailed scope and proof are supplied by `multivalued_random_application`; this report does not claim an independent full audit of that sibling result.

## 8. Publication-value decision

| Claim | Decision |
|---|---|
| `2 μP−μ` is a probability-space reflected resolvent | KILL: usually a signed measure |
| Expected linear RL on common-noise pairs is a new theory | KILL: exact HLS slice |
| A synchronous relative residual controls physical/law step by stationarity alone | KILL: parallel-projection counterexample |
| A deterministic q>1 EB lifts to an L² scalar law EB | KILL: Proposition 4.1 |
| Matched four-point law coupling + pointwise gauges gives local whole-law convergence | GO as project proof; standard metric completion part is not novel |
| The shear–refresh class has true γ<1, nonunique invariant laws and selection robustness | GO under precisely stated selection and reference conditions |
| That class lies outside finite expected almost-FNE in the same native metric | GO by an explicit diverging ratio |
| Therefore it strictly enlarges every existing stochastic convergence framework | NOT ESTABLISHED |
| This package is already a SIAM/Mathematical Programming flagship | NOT ESTABLISHED / REPAIR |

The most useful interface advance is the separation of three operations that cannot be silently interchanged: **select a coupling, compose nonlinear certificates, then integrate**. A promising high-value theorem would classify when a native set-valued stochastic proximal/splitting graph admits this matching, and when dilution or recoupling makes it impossible. The positive example must couple the genuinely nonlinear/multivalued geometry with the stochastic invariant-law mechanism in an essential way; a Cartesian refresh attachment is not enough.

Local arithmetic verification actually executed with Python's standard `math` library gives the maximum composed coefficient in Section 6 as `0.8510291675876296`, confirming the stated `0.852` upper bound. The q=2 dilution ratios at masses `10^-2, 10^-4, 10^-8` are respectively `10, 100, 10000`; the corresponding non-FNE ratio at normal inputs `10^-2, 10^-4, 10^-8` is `100.0625, 10000.0625, 100000000.0625`. These are sanity checks of the displayed exact proofs, not independent theorem validation.

The sibling `random_proximal_extension_attack` independently reviewed Sections 4–5 through the proof and reported no error in the dilution scaling, marginal matching, distinction between `E` and actual set distance, or coverage/finite-length induction. Its explicit caution is the nonphysical-coupling/native-graph gap just stated above. This is a bounded internal audit, not a global-priority or application audit.

## 9. Return contract

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review
project_id: null
paper_family: theoretical
stage_id: null
task_id: stochastic_rl_theory_attack
task_status: PROVISIONAL
inputs_reviewed:
  - RL core manuscript sections listed in Section 1
  - five prior Markov reports listed in Section 1
  - HLS primary definition and theorem formulas
  - conditional-Wasserstein primary publication record
outputs:
  - output/STOCHASTIC_RL_THEORY_ATTACK.md
evidence_status:
  - VERIFIED_SOURCE: exact HLS expected almost-FNE comparison
  - VERIFIED_USER_MATERIAL: previously audited projection and conditional-residual counterexamples
  - AI_INFERENCE: small-mass dilution proposition and corollary
  - AI_INFERENCE: matched-coupling theorem and nonlinear shear-refresh application
  - EXECUTED_LOCAL: composed coefficient and dilution/non-FNE arithmetic checks
  - PENDING_VERIFICATION: independent theorem audit and global priority
assumptions:
  - law couplings are distinguished from physical Markov path couplings
  - conditional gauges are composed before averaging
  - reference-coupling coverage and attainment are explicit assumptions
  - nonlinear example policy does not inspect the old refreshed bit conditional on slow coordinates
author_input_needed: []
manual_actions: []
quality_checks:
  - no signed measure is used as a probability reflector
  - exact HLS parameter relationship derived
  - natural projection false zero is detected by the replacement reference
  - q greater than one aggregation tested by exact dilution witnesses
  - genuine non-Lipschitz source separation proved
  - nonisolated invariant family and all allowed selections retained
  - full-law convergence separated from sample-path convergence
  - coverage and finite-length proof stated rather than presumed
  - standard lifting is not presented as flagship novelty
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: Independently audit the dilution obstruction and coupling theorem, then seek one native non-product stochastic multifunction where both nonlinear geometry and stationary recoupling are essential.
stage_acceptance_recommendation: REPAIR
```

**One primary next action:** audit the dilution obstruction and matched-coupling theorem, then require a genuinely non-product native application before promoting stochastic RL to the flagship.
