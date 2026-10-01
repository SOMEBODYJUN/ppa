# Boundary counterexample audit — PA-BOUNDARY

Project: RL-CONIC-2026. Paper family: theoretical (T). Gate supplied by orchestrator: T4/T5 boundary gate. Date: 2026-09-09.

Status: **boundary mathematics PASS_CANDIDATE; publication wording CONDITIONALLY_READY**. No counterexample-invalidating gap was found. The universal *necessity* direction is independently established below. Its sufficiency direction remains an explicit dependency on the separate amenable-cone CRSC-to-MSCQ theorem; this bounded audit does not replace that theorem's full proof audit. No stage is advanced and no main manuscript is edited.

## 1. Scope and reviewed inputs

- `output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md`, especially Sections 2, 5.2, 7–9.
- `output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md`, especially Section 5 and the necessity/equivalence portion of Section 6A.
- `output/verify_product_cone_crsc_mscq.py`, read completely and rerun without modification.
- [Lourenço–Roshchina–Saunderson, *Amenable Cones Are Particularly Nice*](https://bflourenco.github.io/papers/amenable_nice.pdf): equation (2.4), Proposition 2.3, Section 5, Propositions 5.1–5.2, Theorem 5.3, and the relevant proofs. Proposition 5.1 establishes niceness; Proposition 5.2 establishes nonamenability; Theorem 5.3 records existence. The cone and its geometric tangency are prior work.
- [Author-hosted minimal-face CRSC paper](https://www.ime.usp.br/~ghaeser/crsc-redcones.pdf): equation (1), Definitions 2.1, 3.1–3.2. Definition 3.1 requires both the facial constant-rank property and closedness of the adjoint polar image at the reference point. A constant derivative alone proves only the rank component.

The primary-source pages above were opened directly on 2026-09-09. This is a bounded source check, not a literature-priority search.

## 2. Findings at a glance

| Audit question | Finding | Required qualification |
| --- | --- | --- |
| Is the LRS cone really a nice proper cone? | Yes: niceness is imported from Proposition 5.1; properness is also proved directly below. | Attribute the cone, not merely its formula. |
| Is the selected set a genuine face? | Yes: it is exposed by the nonnegative linear functional “fourth minus third coordinate”. | State this, so that the full feasible set is identified rather than inferred from the path. |
| Does full facial CRCQ hold? | Yes, at the apex with the identity cone reduction. | Check closedness in addition to ranks; all rank tests hold on one common neighborhood, indeed all of the input space. |
| Are the orders correct? | Input distance is exactly computable and is Θ(t³); the true cone residual is positive and O(t⁵). | Only the explicitly constructed residual upper bound is known here to be Θ(t⁵). |
| Is a sequence insufficient for local failure? | No. One path with unbounded ratios already contradicts every uniform neighborhood estimate. | Write the ε–κ quantifiers; do not mistake a negative result for a positive error-bound verification. |
| Is distance to the actual feasible set used? | Yes: isometry gives distance to the entire inverse image, exactly. | Do not replace it by distance to the apex or to one feasible ray. |
| Does one explicit counterexample prove universal necessity? | No; the separate arbitrary-face inclusion argument does. | Quantify over every face and permit varying finite-dimensional input spaces. |
| Is “amenability iff universal CRSC-to-MSCQ” justified? | Necessity: yes independently. Sufficiency: yes conditional on the paper's positive theorem. | Keep the cone fixed and proper nice; constants may depend on the face/map. |

## 3. Paper-ready proposition: the face-inclusion test

**Proposition B1 (face inclusion and amenability).** Let C be a closed convex cone in a finite-dimensional Euclidean space E, let F be a closed face of C, and put L = span F. Equip L with the induced Euclidean norm and let i_F:L→E be inclusion. Then

\[
\Omega_F:=i_F^{-1}(C)=F,
\qquad
d_L(y,\Omega_F)=d_E(y,F),\quad y\in L.
\tag{B1}
\]

The system i_F(y)∈C satisfies MSCQ at zero if and only if F is amenable in C, meaning that there is a_F>0 such that

\[
d_E(y,F)\le a_F d_E(y,C)\qquad\text{for every }y\in L.
\tag{B2}
\]

If C is nice, then the inclusion satisfies the full facial CRCQ at zero. Moreover, for this fixed apex representation, the derivative-image closedness and minimal-linearized-face conditions A1/A2 hold globally.

**Proof.** First C∩span F=F. For completeness, if y∈C∩span F, write y=f_1−f_2 with f_1,f_2∈F. Since y+f_2=f_1∈F and F is a face of a cone, y∈F. The equality of distances follows because the inclusion is isometric and all points of F lie in L.

The forward implication of (B2) to local MSCQ is immediate. Conversely, suppose that some ε,κ>0 satisfy

\[
d_L(y,\Omega_F)\le\kappa d_E(y,C)
\qquad(y\in L,\ \|y\|<\varepsilon).
\]

For arbitrary nonzero y∈L choose λ>0 with λ\|y\|<ε. Since C and F are cones, both distances scale by λ. Applying the local inequality to λy and cancelling λ proves (B2) with a_F=κ. At y=0 it is immediate. No constant uniform in F is asserted.

Now suppose C is nice. The adjoint of inclusion is P_L. Niceness gives closedness of C*+L⊥, and the elementary identity

\[
P_L C^*=(C^*+L^\perp)\cap L
\tag{B3}
\]

therefore proves that i_F* C* is closed in L. The same is true for the negative polar image. For every face Q of C, D i_F(y)*[Q⊥]=P_L[Q⊥] is independent of y; hence all facial rank tests hold simultaneously on the whole input space. Also Im D i_F∩C=L∩C=F, and P_{F⊥}D i_F=0. Thus the minimal face is F, minimal-face CRSC holds, and the frozen derivative conditions A1/A2 are global. ∎

**Interpretation.** For every nonamenable face of a nice cone, this construction gives a linear, indeed C∞, full-facial-CRCQ counterexample to MSCQ. The implication does not require a special formula for the cone. It also does not say that *every* CRSC representation over a nonamenable cone fails MSCQ.

## 4. Paper-ready proposition: the explicit apex counterexample

**Proposition B2 (full facial CRCQ without MSCQ).** Let

\[
\alpha(t)=(\cos t,\sin t,1),\quad
\beta(t)=(\cos t,\sin t,-1),\qquad 0\le t\le2\pi,
\]
\[
\gamma(t)=\left(2\cos(2t)-1,\ 2\sin(2t),\
\frac98\cos t-\frac18\cos(3t)\right),\qquad0\le t\le\pi,
\]
\[
B=\operatorname{conv}(\alpha\cup\beta\cup\gamma),
\qquad K=\operatorname{cone}(B\times\{1\})\subset\mathbb R^4.
\]

This is the cone of [Lourenço–Roshchina–Saunderson, Section 5](https://bflourenco.github.io/papers/amenable_nice.pdf); its niceness is Proposition 5.1 there. Define the linear isometry

\[
A:\mathbb R^3\to\mathbb R^4,
\qquad A(a,b,c)=(a,b,c/\sqrt2,c/\sqrt2),
\]

and Ω=A^{-1}(K). The inclusion Ax∈K satisfies full facial CRCQ at x=0, but there are no ε,κ>0 for which

\[
d_{\mathbb R^3}(x,\Omega)
\le\kappa d_{\mathbb R^4}(Ax,K)
\qquad\text{for all }\|x\|<\varepsilon.
\tag{B4}
\]

**Proof.** The set B is compact. It contains the solid cylinder conv(α∪β), hence has nonempty interior in R³. Its height-one conic lift K is full-dimensional and pointed. It is closed: if λ_j(b_j,1) converges, then λ_j converges by the fourth coordinate; compactness of B treats a positive limit, and boundedness of B forces the entire vector to zero when λ_j→0.

Writing c=cos t gives

\[
\gamma_3(t)=\frac32c-\frac12c^3,
\qquad
1-\gamma_3(t)=\frac12(1-c)^2(2+c).
\tag{B5}
\]

For c∈[−1,1], the height is at most one, with equality only at c=1. Consequently B∩{z=1}=conv α, since no point of β and no new point of γ has height one. The nonnegative functional (a,b,z,s)↦s−z thus exposes the face

\[
J=K\cap\{z=s\}
=\{(a,b,s,s):s\ge\sqrt{a^2+b^2}\}.
\tag{B6}
\]

In particular, Im A=span J, K∩Im A=J, and

\[
\Omega=\{(a,b,c):c\ge\sqrt2\sqrt{a^2+b^2}\}.
\tag{B7}
\]

The isometry A identifies R³ with span J. Proposition B1 and niceness of K give full facial CRCQ, including adjoint-image closedness; the constant derivative supplies one common neighborhood for all faces.

For 0<t<π/2 put

\[
a_t=2\cos(2t)-1,\quad b_t=2\sin(2t),\quad
r_t=\sqrt{a_t^2+b_t^2}=\sqrt{1+8\sin^2t}>1,
\]
\[
x_t=t(a_t,b_t,\sqrt2),\qquad y_t=Ax_t=t(a_t,b_t,1,1).
\]

Then x_t→0 and y_t∈span J\setminus J; since K is closed and K∩span J=J, the actual residual δ_t:=d(y_t,K) is strictly positive. The point t(γ(t),1) lies in K, so

\[
0<\delta_t\le q_t
:=t\bigl(1-\gamma_3(t)\bigr)
=\frac38t^5+O(t^7).
\tag{B8}
\]

The distance to the *entire* feasible set is exactly

\[
d(x_t,\Omega)=d(y_t,J)
=t\sqrt{\frac23}(r_t-1).
\tag{B9}
\]

To justify the projection in (B9), for the unscaled vector (a_t,b_t,1,1) and a fixed s≥0, minimizing over the disk a²+b²≤s² gives squared distance

\[
\bigl(\max\{r_t-s,0\}\bigr)^2+2(1-s)^2.
\]

Its minimizer is s_t=(r_t+2)/3∈(1,r_t). On 0≤s≤r_t the objective is strictly convex with this stationary point; on s≥r_t it is minimized at r_t, which cannot improve the minimum. The minimum value is (2/3)(r_t−1)². Isometry and cone homogeneity now prove (B9).

Since

\[
r_t-1=\frac{8\sin^2t}{\sqrt{1+8\sin^2t}+1}
=4t^2+O(t^4),
\]

we obtain

\[
d(x_t,\Omega)=4\sqrt{\frac23}\,t^3+O(t^5)
=\Theta(t^3),
\qquad 0<\delta_t=O(t^5).
\tag{B10}
\]

In particular,

\[
\frac{d(x_t,\Omega)}{\delta_t}
\ge\frac{d(x_t,\Omega)}{q_t},
\qquad
\lim_{t\downarrow0}t^2\frac{d(x_t,\Omega)}{q_t}
=\frac{32}{3}\sqrt{\frac23}>0.
\tag{B11}
\]

Thus the actual ratio tends to infinity, which contradicts (B4) on every neighborhood of zero. ∎

### 4.1 Explicit neighborhood quantifiers without relying on numerical Taylor checks

There is also an elementary quantitative contradiction. For 0<t<π/2,

\[
\sin t\ge\frac2\pi t,\quad r_t+1\le4,\quad
1-\cos t\le\frac12t^2,
\]

so (B5), (B8), and (B9) imply

\[
d(x_t,\Omega)\ge\frac8{\pi^2}\sqrt{\frac23}\,t^3,
\qquad q_t\le\frac38t^5,
\qquad\|x_t\|\le\sqrt{11}\,t.
\]

Let c_0=64√(2/3)/(3π²). For any proposed κ,ε>0, choose

\[
0<t<\min\left\{\frac\pi2,\frac{\varepsilon}{\sqrt{11}},
\sqrt{\frac{c_0}{\kappa}}\right\}.
\]

Then \|x_t\|<ε and d(x_t,Ω)/δ_t≥c_0/t²>κ. Hence the negation of MSCQ is proved with its full quantifiers, not only suggested by finitely many samples.

### 4.2 What the estimates do not prove

- They do not compute d(y_t,K) exactly or establish a lower bound proportional to t⁵ for that distance. The equality and Θ(t⁵) statement belong to q_t, not to δ_t.
- They do not establish an optimal Hölder exponent for the system, or a globally valid Hölder error bound.
- They do not show failure in every nearby direction. Such a statement is unnecessary: MSCQ would have to hold for every nearby input, so one violating path suffices.
- They do not rely on restricting the feasible set to a path or a ray. Formula (B7) gives the whole feasible cone. If a definition localizes Ω to Ω∩B(0,R), its nearest-point projection for sufficiently small x_t is still inside that ball: Ω is a closed convex cone containing zero and \|P_Ωx_t\|≤\|x_t\|. Thus that localization cannot remove the counterexample.
- The “global A1/A2” phrase concerns the fixed apex representation and its constant derivative. It should not be used to assert results about every new local reduction chosen at arbitrary nonapex reference points.

## 5. Paper-ready universal characterization with exact quantifiers

**Corollary B3 (universal characterization inside the proper nice class).** Fix a finite-dimensional closed, pointed, full-dimensional nice cone C⊂E. Assume the paper's amenable-cone theorem: every C¹ apex system satisfying frozen minimal-face CRSC over an amenable cone has MSCQ. Then the following properties are equivalent:

1. C is amenable.
2. For every finite-dimensional Euclidean input space X, every open neighborhood V of a reference point x̄∈X, and every G∈C¹(V,E) with G(x̄)=0, frozen minimal-face CRSC at x̄ implies the existence of κ,ε>0 such that
   \[
   d_X(x,G^{-1}(C))\le\kappa d_E(G(x),C)
   \quad(x\in B(x̄,\varepsilon)\subset V).
   \]
3. The same universal statement holds with full facial CRCQ in place of minimal-face CRSC.
4. For every face F of C, the linear inclusion i_F:span F→E has MSCQ at zero.

**Proof.** (1)⇒(2) is precisely the cited positive theorem, not a consequence of the counterexample. Since full facial CRCQ implies minimal-face CRSC, (2)⇒(3). By Proposition B1, niceness makes every face inclusion satisfy full facial CRCQ, so (3)⇒(4). Again by Proposition B1, (4) gives amenability of every face, hence (1). ∎

The logical point is the arbitrary-face test, not the existence of one four-dimensional example. The constants in (2)–(4) may depend on G, x̄, and F. No common κ, common radius, or uniform amenability constant over all faces is required. Input dimension must not be silently fixed below the dimensions of the face spans. The trivial face {0} has a zero-dimensional inclusion and a vacuous bound; the full face has the identity inclusion and constant one. Neither creates an obstruction.

Niceness is used in the reverse direction to ensure that the testing inclusions belong to the quantified CRSC/CRCQ class. Removing that standing assumption would require a separate argument; the displayed equivalence must not be advertised for arbitrary closed cones based on this proof.

## 6. Evidence and execution status

The reviewed verification script was executed with:

```text
python3 output/verify_product_cone_crsc_mscq.py
```

Exit code: 0. Its output was:

```text
PASS: exact source-cone Taylor coefficients 3/8 at order 4 and 4 at order 2.
PASS: joint two-SOC and PSD4 normal/dual-face rank identities.
apex path t, certified distance/residual-upper-bound ratio:
0.10000  854.228
0.05000  3466.49
0.02500  13917.5
0.01250  55722.1
Scope: exact formulas and rank sanity checks; full hypotheses/proofs are in Markdown.
```

The word “certified” above is quoted as execution output, **not endorsed as a numerical-certification claim**. Lines 11–26 use exact rational arithmetic for formal Taylor coefficients. Lines 67–72 use floating-point trigonometry and square roots without interval enclosures. They evaluate the analytic lower-bound expression d(x_t,Ω)/q_t, not the true ratio d(x_t,Ω)/δ_t. Their evidence status is a numerical sanity check. The proof of divergence is analytic, and Section 4.1 makes it independent of floating-point error.

The script does not assert monotonicity of successive ratios, does not solve the projection problem onto K, and does not computationally verify niceness or all infinitely many facial rank tests. Those are mathematical/source-based claims. Its sampled two-SOC and PSD rank checks are outside this boundary subtask and were not reinterpreted as full-neighborhood verification.

The original two source files and script were only read/run, never edited. SHA-256 identifiers of the reviewed versions:

```text
0e675fe1aae0b9a2838f25681ae2354461792d5dd3c32fbd77cf3ab726756c37  ATTACK_PRODUCT_CONE_CRSC_MSCQ.md
51607d371b73a6b400a6cf704f130f267be30e499a9ba85e51205223e997284b  AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md
3dfd4bd08699c0a79e4eacfd02c306fbe8d21bd855685054bfa94b6873bb9f76  verify_product_cone_crsc_mscq.py
```

## 7. Three review lenses and proof-gap list

### Contribution

The boundary is mathematically meaningful: niceness and full facial CRCQ do not supply the face-to-cone residual comparison. Nevertheless, the LRS cone and tangency mechanism are imported, and the universal necessity direction is the elementary face-inclusion test. A first-use or first-characterization claim requires the separate priority audit. This task supplies no journal ranking or acceptance prediction.

### Methods

No blocking mathematical gap was found in the boundary argument. The following minimum repairs should be included when converting the working notes into a paper; the propositions above provide those repairs.

| ID | Location and evidence | Severity | Consequence | Minimum repair | Ideal repair |
| --- | --- | --- | --- | --- | --- |
| B-01 | Attack §7.2, projection stated as minimizing (r−s)²+2(1−s)² without first accounting for an interior disk point. | MINOR | The active-boundary assertion is implicit. | Show the positive-part objective and s_t∈(1,r_t), as in B2. | Retain the two-line global projection proof. |
| B-02 | Attack §7.1, universal property in a short boxed sentence. | MODERATE | A reader may read fixed input dimension or a uniform constant across maps/faces into the result. | State the X,G,x̄ quantifiers and map-/face-dependent κ,ε. | Use B3 as a formal corollary after the positive theorem. |
| B-03 | Attack §9 and script line 66: “certified” ratios. | MODERATE | Overstates floating-point evidence; the denominator is not the actual cone distance. | Say “numerical checks of the analytic distance-to-residual-upper-bound ratio”. | Use stable factorizations and, only if numerical certification is needed, actual interval bounds. |
| B-04 | Attack §7.2 and audit §5, local failure summarized by a diverging ratio. | MINOR | No logical error, but the full-neighborhood negation and positivity of the true residual are implicit. | Add δ_t>0 and the κ–ε contradiction. | Use the explicit estimate in §4.1. |
| B-05 | Attack §7.2, full facial CRCQ claim. | MINOR | Constant derivative alone would prove only the facial rank property. The main text already adds niceness, so there is no missing hypothesis. | Keep the closed-image proof, preferably identity (B3). | Cite Definition 3.1 and specify the identity reduction at zero. |
| B-06 | Audit §6A calls the equivalence a pass; Attack §7.1 calls it a candidate. | MINOR | Acceptance labels may hide dependency on the positive theorem. | Separate necessity verified here from sufficiency supplied by Theorem 5.2. | Use theorem dependencies and bounded gate labels consistently. |

### Communication

Keep the following exclusions explicit: nonamenability is a property of the face relative to the original cone, not of the face as an abstract cone; the actual residual is O(t⁵), not proven Θ(t⁵); no globally optimal error-bound exponent is claimed; and full-neighborhood *failure* needs only one violating path. The source curve parameter is γ:[0,π]→R³; do not accidentally extend it to [0,2π] when copying α/β notation.

Readiness synthesis: **CONDITIONALLY_READY** for insertion of the boundary section after the modest wording repairs. There are no shared mathematical blockers for B1–B2 or the necessity half of B3. The positive theorem's sufficiency audit and worldwide priority audit remain separate. Expected repair is editorial/proof-explication, not a new experiment or a cone-class enlargement.

## 8. Deliverables, limitations, and quality checks

Deliverable: this audit, including manuscript-ready Propositions B1–B2, Corollary B3, explicit ε–κ estimates, and evidence labels. No figures were planned or rendered. No third-party API, external software installation, or user account operation was required. No manual action is needed for this bounded task.

Completed quality checks: exact full feasible set; Euclidean isometry; positive residual; global vs local distance; active projection branch; Taylor powers before and after apex scaling; all-face/common-neighborhood rank quantifiers; closed adjoint image; positive dual/negative polar sign equivalence; arbitrary-face necessity; constants nonuniform across maps/faces; zero/full faces; immutable source/script review; script execution scope.

## 9. Standard SCI expert contract

```yaml
contract_version: "1.0"
expert_skill: sci-skills-presubmission-review
project_id: RL-CONIC-2026
paper_family: theoretical
stage_id: "T4/T5 boundary gate"
task_id: PA-BOUNDARY
task_status: COMPLETE
inputs_reviewed:
  - output/ATTACK_PRODUCT_CONE_CRSC_MSCQ.md
  - output/AUDIT_GENERAL_NICE_CONE_CRSC_MSCQ_RANK_SANDWICH.md
  - output/verify_product_cone_crsc_mscq.py
  - LRS primary article, equation (2.4), Proposition 2.3, Section 5, Propositions 5.1-5.2, Theorem 5.3
  - author-hosted crsc-redcones.pdf, equation (1), Definitions 2.1 and 3.1-3.2
outputs:
  - output/conic_paper/BOUNDARY_COUNTEREXAMPLE_AUDIT.md
evidence_status:
  - VERIFIED_USER_MATERIAL: source working manuscript, prior audit, and script reviewed read-only
  - VERIFIED_SOURCE: exact LRS cone formula and published niceness/nonamenability statements
  - VERIFIED_SOURCE: full facial CRCQ includes closedness as well as all-face rank constancy
  - AI_INFERENCE: independent proofs of the exact feasible set, projection formula, apex orders, and all-neighborhood MSCQ failure
  - AI_INFERENCE: arbitrary-face inclusion proves universal necessity; no fixed-dimension or uniform-modulus claim
  - EXECUTED_LOCAL: original standard-library script rerun successfully, exit code 0
  - PENDING_VERIFICATION: worldwide priority and first-use claims, not covered by this bounded audit
assumptions:
  - finite-dimensional Euclidean spaces with the stated isometric face inclusions
  - proper nice cone retained for the universal CRSC/CRCQ characterization
  - universal sufficiency depends on the separate amenable-cone positive theorem
  - supplied stage label is preserved descriptively and does not confer stage authority
author_input_needed: []
manual_actions: []
quality_checks:
  - full facial rank property and adjoint-image closedness checked separately
  - Theta(t^3) input distance versus positive O(t^5) actual residual distinguished
  - actual feasible set and localized feasible-set distance checked
  - arbitrary epsilon-kappa negation of MSCQ written explicitly
  - every-face and varying-input-space quantifiers checked
  - local-to-global cone homogeneity checked
  - numerical sanity checks not treated as interval-certified or general proofs
conflicts: []
conflict_resolution_status: NOT_REQUIRED
merge_permission: orchestrator_only
recommended_next_action: incorporate Propositions B1-B2 and Corollary B3 with the listed wording repairs after checking the positive theorem dependency
stage_acceptance_recommendation: PASS_CANDIDATE
```

**One next action:** 由 orchestrator 核对正向定理依赖后，将 B1–B3 及上述残差/量词措辞修订合入边界章节；本审查不自行推进阶段。
