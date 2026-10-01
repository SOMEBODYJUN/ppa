# RL Research Context Package for AI Continuation
Version: 2026-09-05
Purpose: self-contained research memory for future AI work. This is not a manuscript and not a literature survey.

## 0. Operating instruction

Treat the statements below as the current research baseline unless a new task explicitly asks you to re-audit them.

Do **not** restart from generic generalized monotonicity.
Do **not** re-run dead-end searches already classified below.
Do **not** silently weaken or change the anchor, residual, locality, or selection quantifiers.
Do **not** equate operator-side RL with generic Hölder mapping theory merely because a transformed mapping is Hölder.

When a future task asks for new research, first identify which current result it builds on and which known obstruction it must avoid.

---

# 1. Core definitions and notation

Work primarily in finite-dimensional Euclidean space unless the task explicitly changes the setting.

Let

    F : R^n ⇒ R^n,
    λ > 0,
    J_{λF} = (I + λF)^(-1).

A proximal pair satisfies

    y ∈ J_{λF}(x)
    ⇔
    x = y + λv
    for some v ∈ F(y).

Let the local solution set be

    S = F^{-1}(0) ∩ D.

For graph points (u,u*),(v,v*)∈gph F define

    a = u-v,
    b = u*-v*.

## 1.1 RL graph condition

    ||a - λb|| ≤ L ||a + λb||^γ,
    L ≥ 0,
    0 < γ ≤ 1.

The inner-product form is called **RL-IP**, not a second definition:

    λ<a,b>
    ≥
    1/4[
        ||a+λb||^2
        -
        L^2 ||a+λb||^(2γ)
    ].

## 1.2 J-side equivalent geometry

For x+∈J(x), y+∈J(y):

    ||x+ - y+||^2
    +
    ||(x-x+) - (y-y+)||^2
    ≤
    1/2[
        ||x-y||^2
        +
        L^2||x-y||^(2γ)
    ].

If p∈S and p∈J(p), then for x+=y:

    ||x+ - p||^2
    +
    ||x-x+||^2
    ≤
    1/2[
        ||x-p||^2
        +
        L^2||x-p||^(2γ)
    ].

If p=P_S(x), define

    d  = d(x,S),
    s  = ||x-x+||,
    d+ = d(x+,S).

Then the basic energy inequality is

    d+^2 + s^2
    ≤
    1/2(d^2 + L^2 d^(2γ)).

## 1.3 General residual regularity

Use the general gauge version as the main assumption:

    d(y,S) ≤ ψ(d(0,F(y))),

where ψ is nondecreasing, ψ(0)=0, and ψ(t)→0 as t↓0.

The PPA identity gives

    d(0,F(x+)) ≤ s/λ,

hence

    d+ ≤ ψ(s/λ).

## 1.4 Step upper bound

From the anchored J-energy, with p=P_S(x),

    ||x+ - p||^2 ≥ (d-s)^2,

hence

    (d-s)^2 + s^2
    ≤
    1/2(d^2 + L^2 d^(2γ)),

so

    s ≤ 1/2(d + L d^γ).

Role:
- the **energy + regularity coupling** is the sharp route to distance contraction;
- the **step upper bound** is mainly for finite length, orbit localization, all-step existence, Cauchy convergence, and point convergence.

Do not swap these roles.

---

# 2. Sharpened linear calibration

When

    γ = 1,
    L^2 = 1 + 4τ,
    ψ(t) = ρ t,

the energy is

    d+^2 + s^2 ≤ (1+2τ)d^2

and regularity gives

    d+ ≤ (ρ/λ)s.

Directly coupling the two gives

    d+
    ≤
    [sqrt(1+2τ) ρ / sqrt(ρ^2+λ^2)] d.

Thus a sufficient contraction condition is

    2τρ^2 < λ^2.

Important lesson:
Do not route the proof through the coarse triangle-inequality step lower bound if the goal is the sharp parameter region. That loses the d+/s energy coupling.

---

# 3. Anchor hierarchy: never mix these

For nonisolated S, distinguish:

1. **fixed solution anchor** p̄∈S;
2. **output-nearest anchor** P_S(x+);
3. **input-nearest anchor** p=P_S(x).

The PPA distance energy using d(x,S) naturally requires the **input-nearest anchor**.

In tangent-normal phenomena:
- input-nearest anchor sees the tangential drift and may have sharp γ<1;
- output-nearest anchor can recenter away the tangential motion and often shows exponent 1;
- fixed anchor generally does not control d(x,S) without extra tangential localization.

---

# 4. All-pairs vs anchored RL

Do not assume full graph all-pairs RL is the right algorithmic assumption.

Full all-pairs RL forces injectivity of the Minty parametrization on the region where it is imposed. It can fail because of cross-branch Minty collisions even when all actual proximal branches have useful solution-anchored geometry.

Canonical multibranch separation:
Two different graph branches can have the same Minty input (a+λb=0) but different reflected outputs (a-λb≠0), so full all-pairs RL fails for every finite L.

Yet input-nearest anchored RL can hold uniformly branchwise and arbitrary history-dependent branch switching can still have finite length and converge.

Algorithmic lesson:
Do not pay the full all-pairs cost unless a result genuinely needs arbitrary pairwise resolvent geometry.

---

# 5. Known no-go / negative results

These are important. Future research should not repeatedly rediscover them.

## 5.1 Attractive isolated branches do not genuinely need γ<1

Let p be an isolated solution and y∈J_{λF}(x) satisfy local attraction

    ||y-p|| ≤ C||x-p||.

Then

    ||2(y-p)-(x-p)|| ≤ (2C+1)||x-p||.

Therefore exponent 1 is available.

If along an isolated branch

    ||R_p|| ≳ ||x-p||^γ,
    γ<1,

then ||y-p||/||x-p||→∞; the branch is not locally attractive.

Interpretation:
Genuine sublinear anchored RL is not a natural feature of ordinary attractive isolated-root dynamics.

## 5.2 Locally Lipschitz residual no-go

If F is single-valued, locally K-Lipschitz near a closed solution set S, and F(p)=0 for p∈S, then

    ||F(y)|| ≤ K d(y,S).

This holds whether S is isolated or a manifold.

The current genuine γ<1 compatibility mechanism forces a lower residual scale comparable to d(y,S)^γ; therefore ordinary locally Lipschitz vanishing models are structurally incompatible with the desired genuine γ<1 route.

Set-valued warning:
one small Lipschitz branch can already make the **minimum residual** too small.

Conclusion:
Nonisolatedness alone does not escape the no-go. A usable genuine γ<1 model needs, at minimum, a non-Lipschitz minimum residual scale together with a geometry allowing large tangential motion.

---

# 6. Flat nonisolated tangent-normal mechanism

Canonical geometry:

    S = R^m × {0}.

For input x=(t,z):

    d = ||z||.

A proximal output can have

    tangential displacement ~ d^γ,
    next normal distance  ~ d^β,

with

    0<γ<1<β.

Then:
- the total step is dominated by the tangential component;
- the selected residual is of the same d^γ scale;
- attraction to S is controlled by the normal d^β scale.

This explains how a large sublinear Hölder displacement can coexist with excellent convergence: the large term lives tangent to the solution set.

---

# 7. Direct F-side triangular semistable family

Let

    φ_r(z)=sign(z)|z|^r,
    a,b>0,
    0<α<δ<1,

and

    F_Σ(t,z)
    =
    {
      (-σ a φ_α(z), b φ_δ(z))
      :
      σ∈Σ
    },

with Σ={1} or {-1,1}.

Then

    S = R × {0}.

A proximal branch satisfies

    z = w + λ b φ_δ(w),
    τ = t + σ λ a φ_α(w).

As d=|z|→0,

    |w| ~ (λb)^(-1/δ) d^(1/δ),

and tangential drift

    |τ-t|
    ~
    a b^(-α/δ) λ^(1-α/δ) d^(α/δ).

Therefore

    γ* = α/δ,
    q  = 1/α,
    β  = 1/δ,
    γ*q = β.

The normal PPA rate is Q-superlinear of exact order β.

The minimum residual satisfies

    d(0,F(y)) ~ a d(y,S)^α.

For the two-branch model:
- full all-pairs RL fails due to same-Minty-input / different-output collisions;
- input-nearest anchored RL holds uniformly on both branches;
- arbitrary branch switching has finite length and converges to one point in S.

This is the canonical simple model for learning the genuine γ<1 mechanism.

---

# 8. Tangent-normal scale transport theorem

Let S be a C^2 solution manifold and y=q+m with r=||m||=d(y,S).

For an admissible proximal branch v∈F(y), suppose

    ||P_T(q)v|| ≍ A(r),
    ||P_N(q)v|| ≍ B(r),

with local positive scales A,B→0.

In the operator-normal dominated regime, under the required angular/noncancellation assumptions and

    r = o(B(r)),
    B(r) = o(A(r)),
    A(r)^2 = o(B(r)),

the proximal equation implies

    d(x,S) ≍ λ B(r),

hence

    r ≍ B^{-1}(d(x,S)/λ).

The transported anchored geometry is

    Ω_λ(d)
    ≍
    λ A(B^{-1}(d/λ)).

If the **full minimum residual** satisfies

    d(0,F(y)) ≍ A(r),

then

    ψ ≍ A^{-1},

and the loop closes:

    ψ(Ω_λ(d)/λ)
    ≍
    B^{-1}(d/λ).

Interpretation:

    A,B
      → A∘B^{-1}   (anchored RL / reflected scale)
      → A^{-1}      (residual regularity)
      → B^{-1}      (normal PPA attraction)

The power identity γq=β is only a specialization of this scale transport.

---

# 9. Tangential necessity theorem

Let S be C^2, p=P_S(x), and y a locally attractive proximal branch with

    d(y,S)=O(d(x,S)).

Suppose

    ||R_p|| ≍ ω(d),
    d=o(ω(d)).

Then the leading reflected displacement is asymptotically tangent:

    ||P_{N_S(p)} R_p|| = o(ω(d)).

Moreover the nearest solution drift satisfies

    q-p
    =
    (1/2)R_p + o(ω(d)),

so

    ||q-p|| ≍ ω(d).

For ω(d)=d^γ, γ<1:
genuine Hölder reflected displacement is not merely allowed to be tangential; for an attractive branch its leading part is tangential and is the scale of motion of the nearest solution point along S.

---

# 10. Curvature–operator competition

For curved S, write the selected residual at y as tangent/normal pieces

    u = P_T(q)v,
    w = P_N(q)v.

A second-order expansion of the proximal normal balance gives, after consistent normal transport,

    n
    =
    transported(m + λw)
    -
    (λ^2/2) II_p(u,u)
    +
    lower-order terms.

Important sign/cancellation fact:
The naive chord contribution +1/2 II(t,t) is not the final term. Eliminating the tangent proximal equation cancels one full II(t,t), leaving the net coefficient -1/2.

Thus the competition is genuinely vectorial:

    λ w
    vs
    -(λ^2/2) II_p(u,u).

Since ||u||≍A(r), curvature enters at scale A(r)^2.

## 10.1 Phase classification

### Regime I: operator-normal dominated

    A(r)^2 = o(B(r))

Then

    d(x,S) ≍ B(r)

(up to λ scaling), recovering the scale transport theorem.

### Regime II: critical coupling

    A(r)^2 ≍ B(r).

Leading normal operator and curvature terms are same order. They may reinforce, partially cancel, or fully cancel as vectors.

If the leading vector coefficient is nonzero:

    d(x,S) ≍ A(r)^2.

If it cancels:
first-order scales A,B no longer determine the next rate. Higher-order geometry, subleading operator terms, output normal error, directional approach, and logarithmic corrections can take over.

There is no universal “next exponent” in the resonant case.

### Regime III: curvature dominated

    B(r) = o(A(r)^2)

and the second fundamental form is nondegenerate in the active tangential direction.

Then

    d(x,S) ≍ λ^2 A(r)^2,

while

    ||R_p|| ≍ λ A(r).

Therefore universally

    ||R_p|| ≍ sqrt(d(x,S)),

so the sharp anchored Hölder exponent is

    γ = 1/2.

This square-root law does not require A to be a pure power.

## 10.2 Higher-order geometric leakage

If the second fundamental form vanishes along the active tangent direction but the first nonzero geometric normal leakage is order k, then under the corresponding domination assumptions one expects/derives

    d ≍ A(r)^k,
    |R_p| ≍ d^(1/k).

Do not treat this as universally available under only C^2 regularity; finite k may require additional smoothness and nondegeneracy.

---

# 11. General-scale finite-length caveat

Superlinear set attraction does not by itself imply point convergence for arbitrary scales.

If tangential increments behave like A(d_{k+1}), one must control

    Σ_k A(d_{k+1}).

A useful sufficient Dini-type condition is

    ∫_0^{r0} A(t)/t dt < ∞.

For power A(t)=t^α, α>0, combined with superlinear normal collapse, summability is automatic.

Do not infer point convergence from set-distance convergence without a finite-length or other point-selection mechanism.

---

# 12. Verification/usability results worth remembering

A practical RL theory exists mainly through direct F-side certificates, especially for anchored RL.

Useful certificate families already derived/explored:
- hypomonotonicity → explicit γ=1 RL constant;
- Jacobian/Cayley local tests;
- sector / angle + magnitude-gap conditions;
- radial / star conditions;
- monotone core + smooth perturbation;
- branchwise affine / piecewise linear verification;
- relative-Minty perturbation;
- block/product aggregation.

Priority rule:
Do not expand this into an abstract closure-property catalogue. A property is high priority only if it shortens

    model → RL certificate → computable parameters → algorithm conclusion.

---

# 13. Known research traps / "do not repeat"

1. Do not keep searching for usable genuine γ<1 in ordinary isolated smooth/Lipschitz root models. The no-go is structural.
2. Do not assume nonisolatedness alone solves the no-go. Need non-Lipschitz minimum residual + scale separation.
3. Do not identify selected proximal residual with d(0,F(y)).
4. Do not interchange fixed, output-nearest, and input-nearest anchors.
5. Do not use the coarse step-upper-bound→ψ route when sharp contraction parameters matter.
6. Do not make full all-pairs RL the default algorithmic assumption.
7. Do not treat γq as a universal exact law outside the verified scale assumptions.
8. Do not compress general scale behavior into pure power exponents if logs/slow variation matter.
9. Do not treat A^2=o(B) as a technical nuisance; its failure enters a real curvature regime.
10. Do not assume critical cancellation has a universal next exponent.
11. Do not infer point convergence solely from d(x_k,S)→0.
12. Do not conclude "RL is old" merely because generic Hölder mappings or reflected resolvents are studied. Keep operator-side, J-side, reflector-side, and regularity layers distinct.
13. Do not spend major research effort on random inversion/scaling/closure properties unless they enable verification, construction, or an algorithm theorem.
14. Do not over-anchor on the first natural application found.

---

# 14. Current natural application benchmark

A specialized but natural proof-of-concept has been identified in a nonmonotone Maxwellian rate-type thermo-viscoelastic model near a spinodal turning point under constant-stress pseudo-creep.

On a designated stable half-branch:

    A(r) ≍ r^ℓ,
    B(r) ≍ r^(ℓ+1/2),
    residual ≍ r^ℓ.

For 0<ℓ<1/2:

    B=o(A^2),

hence curvature dominated:

    γ*=1/2,
    q=1/ℓ,
    β=1/(2ℓ).

Independent proximal asymptotics match the theory.

Status:
- useful proof-of-concept that curvature-induced RL behavior can arise in an existing model;
- branch-specific and specialized;
- currently only a benchmark, not the central flagship of the program.

Future application/model searches should aim to find a clearly more compelling external hook rather than merely extending this model.

---

# 15. Manuscript triage: what currently belongs where

## Strong candidates for first-paper main text

1. RL definition + RL-IP + J-side generalized firm geometry.
2. General-ψ PPA theorem with sharp energy coupling and finite-length/local-existence closure.
3. Identification of the genuinely Hölder regime:
   - isolated attractive branch ⇒ exponent 1 available;
   - locally Lipschitz residual no-go.
4. Nonisolated tangent-normal mechanism and the simple triangular F-side family.
5. General tangent-normal scale transport theorem, after full proof audit.
6. Anchored vs all-pairs separation as an algorithmically meaningful distinction.
7. A small number of practical verification corollaries.

## Use cautiously / possible appendix / possible second paper

- full curvature/operator phase theory;
- universal γ=1/2 curvature-dominated law;
- critical resonance and cancellation zoo;
- higher-order 1/k geometric leakage;
- non-power/logarithmic endpoint phenomena;
- extensive verification catalogue;
- specialized natural applications.

The curvature theory is mathematically strong enough that it may deserve its own paper rather than being consumed as a technical section of the first RL/PPA paper.

---

# 16. Research prioritization

The program is no longer "explore all RL properties."

High-value goals are:

1. **Human proof audit and consolidation** of the main structural theorems.
2. **External significance**: identify a phenomenon other communities already care about that the tangent-normal/curvature theory explains sharply.
3. **Natural model certification** from original model data, not theorem-designed toy models.
4. **Manuscript architecture**: decide which results form one coherent first paper and which should be held for a second paper.
5. **Readable exposition**: motivation-first, minimal helper notation, J-centered, explicit proof roles.

For AI task allocation:
- use a deep single-problem model (Pro-style) for one hard theorem, converse, sharpness audit, or external-significance bridge;
- use a long-context research agent (Codex-style) for systematic model/literature searches and report-building.

---

# 17. Current open questions that actually matter

Do not generate a long list. The current high-value questions are roughly:

1. Can the general tangent-normal scale theorem and tangential necessity theorem be made publication-grade with minimal, directly verifiable F-side assumptions?
2. Is there a broad, recognizable external problem class where the curvature/operator phase law explains a known but previously model-specific rate/threshold?
3. Should the curvature phase transition be part of the first RL/PPA paper or developed as a separate second paper?

Everything else is lower priority unless it directly supports one of these.

---

# 18. Writing principles

- Motivation before abstraction.
- J_{λF} is the main algorithmic object; reflector is an equivalent representation, not the narrative center.
- Keep formulas visible; avoid helper notation used once.
- Explicitly explain "what do we need next?" in proofs.
- Separate:
  geometry → contraction,
  step bound → finite length/local closure.
- Do not overclaim novelty from γ=1 slices, generic Hölder mapping literature, or known maximal-monotone q-subregularity results.
- Preserve all locality/branch/anchor qualifications in theorem statements.
