# NFB source-priority follow-up: old updates, old geometry, and the residual 2026 theorem

Date: 2026-10-09. Read-only baseline: `94cbbbd9bacb61787eeee583e0282b890455849a`.
This is a literature/derivation audit, not a new Claim or a worldwide novelty certificate.
No Claim, graph, state register, or commit was changed. The only accompanying code is
[`nfb_source_priority_check.py`](nfb_source_priority_check.py).

**Finding.** The 2026 paper does not introduce the underlying momentum-corrected
NFB update, its relaxed update, semimonotonicity, nonmonotone PPA convergence, or
nonmonotone PPA linear point convergence for the first time. All have specific older
primary predecessors. However, identity of the update does not establish identity of
the theorem: the inspected predecessors do not directly prove the full 2026
relaxed, nonlinear-kernel, anchored-comonotone Hilbert-space theorem. The strongest
plausible residual contribution is this convergence proof and its explicit parameter
conditions, with resulting genuinely nonmonotone CV/FHRB/primal-dual guarantees.
That residual is provisional until the remaining warped-nonmonotone references are read.

## 1. Exact primary evidence and version priority

The 2026 comparison target is Pesquet–Roldán,
[*Nonlinear Forward-Backward Algorithm for Solving Non-monotone+Lipschitz Inclusions
with Applications to Adjoint Mismatch Problems*](https://arxiv.org/abs/2608.22687v1),
2026-08-24. I read its fixed repository PDF, especially pp.3–8, 12–16, 17–29,
and §5. The file has SHA-256
`14db75596189d898d97aa9389b3e1a50bbe2ed70e207a3257d681cb4d01077b9`.
The existing `nfb_review.md` and `sol61_nfb_audit.md` correctly analyze its
coverage/noncoverage; those audits deliberately left imported-reference priority open.

| Primary predecessor | Version/date actually inspected | Exact relevant result |
| --- | --- | --- |
| [Morin–Banert–Giselsson, NFB with Momentum Correction](https://arxiv.org/abs/2112.00481) | v1, 2021-12-01; v5, 2023-09-29. [Journal publication](https://doi.org/10.1007/s11228-023-00700-4): 2023-11-03. | Algorithm 1 already in v1 p.5; v5 Assumptions 2.1/2.2, Theorem 3.1 pp.4–9; PDBTR §6.1. This is not a first-2024 algorithm. |
| [Roldán–Vega, Relaxed and Inertial NFB with Momentum](https://arxiv.org/abs/2412.02045v1) | v1, 2024-12-03. [Version of record](https://doi.org/10.1007/s10957-025-02694-5): 2025-05-23; full journal text not accessed. | Algorithm 2.2 p.3, (2.3); fixed-parameter non-inertial specialization of Theorem 4.4 p.8, through (4.2)–(4.5); PDBTR (5.9)/(5.10) pp.13–14. |
| [Evens–Pas–Latafat–Patrinos, PPPA/DRS without monotonicity](https://arxiv.org/abs/2305.03605) | v1, 2023-05-05; v2, 2024-05-06. | v1 Definition 4.1/Proposition 4.7: scalar anchored semimonotonicity and sum calculus; v1 Theorem 2.6 has linear-convergence proof. Clean v2 import: Definition 2.1, Assumption I, Theorems 2.4/2.13, Proposition 4.7. |
| [Evens–Latafat–Patrinos, CP without monotonicity](https://arxiv.org/abs/2312.06540) | v1, 2023-12-11; v2, 2024-07-09; v3, 2025-03-10 also downloaded. Comparisons below use v2. | Arbitrary symmetric **matrix** anchored semimonotonicity is already v1 Definition 1.2 p.3. v2 Definitions 1.1/1.2, Proposition 4.9, Theorem 5.1, Theorem 3.4/Corollary 5.4. |
| [Chouzenoux–Pesquet–Roldán, mismatched monotone+Lipschitz inclusions](https://arxiv.org/abs/2310.06402v1) | v1, 2023-10-10, full PDF read. [Journal metadata](https://doi.org/10.1137/23M1609166): published online 2024-10-23. | v1 Assumption 3.2/Proposition 3.4; Algorithm 6.1 p.18, Theorem 6.4 pp.20–23 give mismatched FHRB and linear point convergence. The journal abstract lists only FBHF/FDRF; do not silently attribute all v1 §6 content to the journal version. |

The PPPA v1 Theorem 2.6's literal final sentence mistakenly says that the projected
iterates converge R-linearly “to zero”; its proof explicitly concludes
`||w^k-w*||_Q` decays geometrically. The 2024 v2 Theorem 2.13 states the point
limit correctly. The priority of the mechanism is already 2023, but the exact
import below uses the corrected v2 statement.

## 2. The relaxed 2026 update is exactly an old algorithm

Use the 2026 symbols and set `H_M = τM-S`. Algorithm 3.7 is

\[
p_{n+1}=(M+A)^{-1}(Mx_n-Cx_n+u_n/\tau),\qquad
u_{n+1}=H_Mp_{n+1}-H_Mx_n,
\]
\[
x_{n+1}=(1-\theta)x_n+\theta p_{n+1}. \tag{P1}
\]

MBG Algorithm 1 is exactly (P1) when `θ=1`, `M_n=M`, `γ_n=τ`.
The arbitrary initial memory `u_0` is the same, not just a zero-memory limit.
Its parameter `ℓ` is `1/β` in the 2026 cocoercivity convention.

Roldán–Vega Algorithm 2.2 first forms
`y_n=x_n+α_n(x_n-x_{n-1})`, then performs the same implicit and memory steps
at `y_n`, then `x_{n+1}=(1-λ)y_n+λp_{n+1}`. Set

\[
\alpha_n=0,\quad \gamma_n=\tau,\quad M_n=M,\quad
\lambda=\theta,\quad \mu_{\rm RV}=\beta.
\tag{P2}
\]

This gives all three 2026 lines exactly, including the memory placement before
relaxation. Consequently neither nonlinear memory correction nor relaxation of
this correction is a new 2026 algorithmic operation. The 2026 paper itself says
on p.3 that it extends MBG's convergence analysis to comonotone operators.
It cites MBG as [48]; the Roldán–Vega 2024/2025 paper is absent from its reference list.
Absence of a citation is a bibliographic observation, not a misconduct judgment.

The theorem hypotheses differ substantially. MBG and RV require maximally
monotone `A`, cocoercive full-domain `C`, and a nonempty zero set. The 2026
Assumption 3.1 instead assumes full-domain single-valued warped inverse and
weak–strong closedness explicitly, and allows

\[
\langle x-z,a+Cz\rangle\ge\rho\|a+Cz\|_{S^{-1}}^2
\quad(a\in Ax, z\in\operatorname{zer}(A+C)),\quad \rho>-\beta,
\tag{P3}
\]

with negative `ρ`. It retains all graph points relative to every solution anchor,
but does not require all-pairs monotonicity. MBG/RV do not imply this new theorem
merely because their recurrence is identical.

### A real parameter improvement relative to RV v1, with an explicit limit

Let `ζ_n=ζ`, `γ_n=τ`, `α_n=0`, and put `h=2-θ-τ/(2β)`.
RV (4.4) gives `θ η_RV=h-c_RV ζ`, whereas 2026 (3.8) with `ρ̂=0`
gives `Δ_NFB=h-c_NFB ζ`. Their sufficient conditions require these quantities positive.

| Branch | `c_RV` from v1 (4.2)–(4.5) | `c_NFB` from (3.7)–(3.8) | Difference |
| --- | --- | --- | --- |
| `1≤θ<2` and `S-τM` monotone | `θ²+2θ-1` | `2` | `(θ-1)(θ+3)` |
| `1≤θ<2`, other kernels | `θ²+4θ-3` | `2θ` | `(θ-1)(θ+3)` |
| `0<θ<1` | `θ²-4θ+5` | `2(2-θ)` | `(θ-1)²` |

All differences are nonnegative and vanish at `θ=1`. For a fully legal scalar
instance, take `A=Id`, `C=0`, `S=Id`, `τ=1`, `M=17 Id/20`,
`θ=3/2`, `ζ=3/20`, and a finite zero-operator cocoercivity constant `β=10`.
Then `S-τM` is monotone, the warped inverse is a continuous full-domain inverse,
and

\[
\Delta_{\rm NFB}=3/20>0,\qquad
\theta\eta_{\rm RV}=-3/16<0.
\tag{P4}
\]

The actual state matrix on `(x,u)` is `[[7,30],[3,-3]]/37`, whose eigenvalues
are `(2±sqrt(115))/37`, both strictly inside the unit disk. Thus this is a
strictly enlarged **sufficient-certificate range against RV arXiv v1**, not an
operator or algorithm separation. The inaccessible 2025 RV version of record
may revise constants; no claim about improvement over its unread formulas is made.
MBG's fixed unrelaxed bound `1-2ζ-τ/(2β)>0` agrees with 2026 at `θ=1,ρ̂=0`.

## 3. Semimonotonicity and its sum rule have earlier exact antecedents

CP v1 Definition 1.2 already allows symmetric, possibly indefinite matrices
`M,R` and the anchored inequality

\[
\langle x-x_*,a-a_*\rangle\ge
\langle x-x_*,M(x-x_*)\rangle+\langle a-a_*,R(a-a_*)\rangle
\quad((x,a)\in\operatorname{gph}A).
\tag{P5}
\]

The 2026 Definition (2.3) uses bounded self-adjoint Hilbert-space operators in the
same roles, and a set of anchors rather than writing one anchor at a time.
On finite-dimensional spaces it is the same definition. The Hilbert-space
formulation is an extension in ambient scope; it is not a new finite-dimensional
metric semimonotonicity concept. Requiring every solution anchor is stronger than
the older one-anchor sufficient formulations.

NFB Lemma 2.2's proportional-metric sum rule is a special case of CP v2
Proposition 4.9. Map

\[
M_A=\nu_1S,\ R_A=\rho_1S^{-1},\quad
M_C=\nu_2S,\ R_C=\rho_2S^{-1},\quad \rho_1+\rho_2>0.
\]

Their matrix parallel sum is
`R_A □ R_C = (ρ_1ρ_2/(ρ_1+ρ_2)) S^{-1}`.
After the coordinate change `y=S^{1/2}x`, `b=S^{-1/2}a`, it is also exactly
the scalar PPPA Proposition 4.7, already present in v1. The general Hilbert
version follows by the same square identity:

\[
\rho\|a\|_{S^{-1}}^2+\beta\|c\|_{S^{-1}}^2
-\frac{\rho\beta}{\rho+\beta}\|a+c\|_{S^{-1}}^2
=\frac{\|\rho a-\beta c\|_{S^{-1}}^2}{\rho+\beta}\ge0.
\tag{P6}
\]

The strict positive sum is essential even when one coefficient is negative.
This derivation also works at a common anchor; it does not falsely replace
2026's anchored condition by all-pairs semimonotonicity.

## 4. The ordinary-PPA nonmonotone and linear branches are already covered

Set `C=0`, `M=S/τ`, `u_0=0`. Memory vanishes and (P1) becomes relaxed PPPA with

\[
T=A,\quad P=S/\tau,\quad V=\rho S^{-1},\quad
\lambda_n=\theta,\quad S_* =\operatorname{zer}A.
\tag{P7}
\]

This is an exact algorithm identity, not just equality of zero sets. Evens v2
Assumption I requires outer semicontinuity of `T`, full-domain preconditioned
resolvent, `V`-oblique weak Minty anchors, and
`η_min=1+λ_min(VP)>0`. In the finite-dimensional (P7) setting, 2026 graph closure
gives outer semicontinuity, and its inverse assumption gives the domain condition.
Here `η_min=1+ρ/τ`. Evens Theorem 2.4 allows

\[
0<\theta<2(1+\rho/\tau),\qquad
\theta\,[2(1+\rho/\tau)-\theta]>0.
\tag{P8}
\]

For `ρ≤0`, NFB Corollary 3.12(ii)'s `C=0,ζ=0` condition is exactly (P8):
`2-θ+2ρ/τ>0`. The zero `C` permits arbitrarily large **finite** `β`; a strict
limit margin lets one choose a large finite value. For positive `ρ`, NFB clips
`ρ̂` to zero and insists on `θ<2`; the older PPPA theorem can allow larger relaxations.
The 2026 nonlinear-memory Hilbert theorem is therefore not a wholesale enlargement
of the older finite-dimensional PPPA theorem.

**Concrete prior coverage of the repository overlap.** For `F=-Id`, ordinary
PPA step `τ=3`, take Evens `T=F`, `P=Id/3`, `V=-Id`, `S_*={0}`, `θ=1`.
The graph is closed, `J_{3F}=-Id/2` is full-domain and continuous,
`η_min=2/3`, and `κ=θ(2η_min-θ)=1/3`.
The true residual error bound has modulus one. Thus Theorems 2.4 and 2.13 both
apply, including physical point R-linear convergence, before the 2026 paper.
Theorem 2.13 gives the valid factor `sqrt(13)/4`; the exact orbit has factor `1/2`.
This example remains important as real NFB/repository overlap, but NFB is not its
earliest inspected source. The rotation example is also covered by older PPPA;
rotation is monotone, and must not be counted as an extra strictly nonmonotone example.

### Strong anchored semimonotonicity already supplies an error bound

This paragraph is an independent derivation, not a quoted theorem. For
`F=A+C`, (P3) strengthened by `μ||x-z||_S²`, `μ>0`, and cocoercivity of `C`
give, using (P6),

\[
\langle x-z,f\rangle\ge\mu\|x-z\|_S^2
+q\|f\|_{S^{-1}}^2,\quad
q=\frac{\rho\beta}{\rho+\beta},\quad f\in Fx.
\tag{P9}
\]

At `f=0`, this forces uniqueness. Write `d=||x-z||_S`, `r=||f||_{S^{-1}}`,
and `q_-=min(q,0)`. Cauchy–Schwarz gives
`μd²-dr+q_-r²≤0`, hence

\[
d\le K r,\qquad
K=\frac{1+\sqrt{1-4\mu q_-}}{2\mu}.
\tag{P10}
\]

Taking the infimum over the complete fiber gives a global true-residual error
bound in the transformed metric. For the `C=0` PPPA specialization, this makes
the metric-subregularity premise of the older linear theorem derivable.
To import Evens Theorem 2.13 exactly, one must still check its continuous
preconditioned-resolvent premise, and use its finite-dimensional space. A
single-valued full-domain inverse plus closed graph alone is not a continuity proof.
The 2026 theorem does not impose that separate continuity premise.
For the broad nonlinear-memory recurrence, (P10) alone does not make it PPPA:
an exact lifted algorithm and all lifted theorem gates would need to be proved.

## 5. CP, CV, FHRB, and adjoint mismatch are different priority questions

For `D=C=0`, NFB (4.30) is exactly the old relaxed CP update. Evens CP uses

\[
T_{PD}(x,v)=(Ax+L^*v,\ B^{-1}v-Lx),\quad
P=\begin{pmatrix}\tau^{-1}I&-L^*\\-L&\sigma^{-1}I\end{pmatrix}.
\tag{P11}
\]

Its `P(x_n-\bar x_n,v_n-\bar v_n)∈T_PD(\bar x_n,\bar v_n)` is equivalent
to the two resolvent lines, and relaxation is `λ=θ`. Older CP Theorem 5.1/
Corollary 5.3 maps component anchored semimonotonicity to an oblique weak Minty
matrix with primal block `(ρ_A □ ρ_B)I` and dual block `(μ_A □ μ_B)I`
(plus the stated range/nullspace blocks). This is an explicit antecedent for
the 2026 CP semimonotone analysis. The older theorem retains its outer
semicontinuity, full-domain, spectral step/range, and anchor-set conditions;
continuity is an additional gate for full unprojected point convergence at a
singular preconditioner. Do not omit those gates.

The older CP analysis allows `τσ||L||²=1` and, in some regimes, relaxations above
two; NFB uses a strongly positive product metric and `τσ||L||²<1`, `0<θ<2`.
NFB's introduction expressly identifies recovery of the old CP conditions.
There is no basis for claiming first nonmonotone CP convergence in 2026.
Conversely, nonzero cocoercive `C` in CV and the nonlinear Lipschitz `D` with
memory in FHRB/PDBTR are outside the plain two-operator CP recurrence, so the
old CP theorem is not by itself a direct proof of all NFB §4 statements.

The 2023 mismatched-inclusion preprint supplies a particularly close FHRB
antecedent. With fixed `K_n=K`, its Algorithm 6.1 is

\[
z_{n+1}=J_{\gamma A}\bigl(z_n-\gamma(2D_Kz_n-D_Kz_{n-1}+Cz_n)\bigr).
\tag{P12}
\]

NFB Algorithm 4.9 with `L=B=0`, `θ=1` has `p_n=z_n` after consistent
initialization and gives exactly (P12), with `τ=γ`, `D=D_K`.
The older Theorem 6.4(ii) already gives linear point convergence under
`ρ̂=ρ+αλ_min-Lip((L^*-K)BL)>0` and geometrically decreasing approximation
errors `ω_n=ω_0 η^n`; fixed mismatch has `ω_0=0`.
But Assumption 3.2(ii), via Proposition 3.4, forces the aggregate `A+D_K`
to be maximally monotone. This compensated-monotonicity theorem does not
duplicate the genuinely total-nonmonotone 2026 anchored-comonotone theorem.
The correct residual distinction concerns allowed geometry, not the labels
“mismatch,” “FHRB,” or “linear.”

## 6. Precise novelty disposition and remaining gates

| Candidate description of the 2026 contribution | Audit disposition |
| --- | --- |
| First NFB with nonlinear momentum correction | False against MBG v1 2021. |
| First relaxation of that update | False against RV v1 2024, with exact map (P2). |
| New finite-dimensional metric semimonotonicity / anchored sum rule | False as a primitive; earlier CP/PPPA definitions and calculus match. Hilbert-space scope is a modest extension. |
| First nonmonotone PPA convergence or linear point convergence | False against Evens PPPA v1/v2, with exact gates/example (P7)–(P10). |
| First nonmonotone CP convergence | False against Evens CP v1/v2. |
| First mismatched FHRB or FHRB linear convergence | False against Chouzenoux–Pesquet–Roldán v1 §6, but its aggregate is monotone. |
| Full relaxed NFB convergence for independent fixed SPD metric and fixed nonlinear kernel under anchored negative comonotonicity, plus strong-anchor linear rate | **Strongest plausible residual novelty among the inspected sources.** Same algorithm, materially different theorem assumptions/proof. |
| Improved monotone relaxed certificate over RV | Verified against arXiv v1, with (P4). Not yet verified against RV's 2025 version of record or all older relaxed schemes. |
| Full genuinely nonmonotone CV/FHRB/PDBTR application guarantees | Plausible residual consequences of the preceding new theorem. Their exact parameter ranges need comparison with other nonmonotone splitting papers; labels alone carry no novelty. |

The physical R-linear point estimate already implies a geometric finite-length
tail by the triangle inequality and summing a geometric series. Neither failure
to print the phrase “finite length” nor switching from a point estimate to its
summed tail creates a new priority distinction.

Unclosed external gates are substantive:

1. Papadimitriou–Vu, *On the convergence of warped proximal iterations for solving
   non-monotone inclusions and applications*, OPT 2023,
   [OpenReview](https://openreview.net/forum?id=6tFGOXyykI), NFB reference [49].
   The public page returned a verification wall; its public PDF request returned
   HTTP 403. I did not read its theorem and do not claim noncoverage. No login or
   bypass was attempted. Its exact kernel-dependent notions must be mapped before
   a worldwide-priority verdict on the residual theorem.
2. Trang–Nguyen, *Fast warped iteration for nonmonotone inclusions with a
   convergence rate of o(1/k)*, [DOI](https://doi.org/10.1080/10556788.2026.2617626),
   NFB reference [57], was not full-text audited in this follow-up.
3. RV's 2025 version of record is subscription-only at the retrieved publisher
   page. Formula-level comparisons apply to its 2024 arXiv v1 only.
4. The 2024 journal version of the mismatched-inclusion paper was not full-text
   compared with v1; the early v1 is sufficient for the version-scoped priority
   observation but not for a claim about its final §6 numbering/content.
5. The 2026 target's live arXiv page failed to fetch in browsing. Its fixed,
   hashed, full repository PDF supplied the mathematical evidence; this failure
   is not evidence that the paper is absent or withdrawn.

This source-priority audit does not weaken the existing full-graph quadratic-anchor
obstruction. Even the older inspected Evens weak-Minty class assumes a fixed
quadratic anchor on the graph it uses. However, its own restricted-graph
variant and possible alternative formulations require separate gates; NFB
noncoverage must not be turned into absence of every prior method.

## 7. Reproducibility, hashes, and retrieval locators

All newly downloaded PDFs/texts are scratch intermediates in
`tmp/nfb_priority/`; none were added as new canonical literature files.

| Downloaded file | SHA-256 |
| --- | --- |
| `mbg_v1.pdf` | `c95aae56ce33ce871a42ef47018c5c2b9850af6fd61bfa5d25cac511b2a6213d` |
| `mbg_v5.pdf` | `cb9e1fc399e9015a1a0c038fb715f185fadaececd8dc7d200d2eef8c38e73f39` |
| `rv_v1.pdf` | `5b437cd17ac1fbeb4f9ec0a9861cf17a589357433a6136d99a38f078c7d556a7` |
| `elpp_v1.pdf` | `4189e612584da43d70afb433857bbb41e9dd5afc16a99c04e63dcd5af7958f44` |
| `elpp_v2.pdf` | `f275fec745d247aa11b45ee5603f251eb93f26e6369a2cc19e446bd07f3962d5` |
| `elp_cp_v1.pdf` | `57bb40b2e2a917896098bcc1b4a8a0a94dc9a05c5738e739c00660df01c05ad1` |
| `elp_cp_v2.pdf` | `388dc9169630c63f50aadf748c263266ca4203ad173c04fcf69ff0ee113503d7` |
| `elp_cp_v3.pdf` | `dc3ead0aab2035e2ee94e18f5195bd54b118cc0c06d6c0914657cd56d2de69df` |
| `cpr_mismatch_v1.pdf` | `fd94cff81f48fb648d4890fa2bea1bc954c884f56231293e9198f59307fa237b` |

Run `python3 research/novelty/2026_10_09/nfb_source_priority_check.py`.
It passed 78 exact rational coefficient comparisons, 36 exact recurrence steps,
36 parallel-sum square completions, the strict monotone witness, and the
`F=-Id` Evens numerical constant check. These finite computations support
displayed algebra; the substitutions and implications above are the proofs.
The script uses only Python's standard library and mutates no files.

Primary web retrieval locators for the parent synthesis: MBG chronology
`turn6view0`, publisher `turn6view3`, full HTML `turn50view0`; RV chronology
`turn12view0`, full v1 PDF `turn50view1`/`turn58view4`, publisher `turn79view1`;
PPPA chronology `turn6view1`, full v2 HTML `turn50view3`/`turn58view3`;
CP chronology `turn6view2`, full v2 PDF `turn12view3`, full HTML `turn58view1`;
mismatch publisher `turn76search0`/`turn76search1`; inaccessible OpenReview
`turn95view0`. Open a predecessor source in the parent before citing its locator
in a user-facing synthesis, as required by the retrieval tool.
