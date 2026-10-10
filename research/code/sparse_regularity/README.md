# Sparse automatic regularity — C224/C225/C226 finite verification

Run from the repository root:

```sh
python3 research/code/sparse_regularity/verify.py
```

Python standard library only; no random seed (complete finite enumeration), exact `fractions.Fraction` algebra and independent 60/100-digit `decimal` calculations. The coordinating agent reran the original identical verifier successfully on 2026-10-09 before copying it here. Output is `automatic_regularity_results.json`.

Actual checks: 268200 finite moment/coefficient cases; the Pearson square identity and its endpoint equality conditions; p=3/2 symmetric coefficients 1/4, 0, 1/192; p=5/3, alpha=10 reduced strict-minimum values; inactive equality descent; A=I, b=(1,0), eta=1, xbar=(1,0), rho=1/16, lambda=1/100, input radius=1/250 complete-resolvent certificate and rational reverse checks.

Theorem proof and internal reception scope: [canonical mathematical module](../../topics/sparse_recovery/automatic_regularity.md#sr-evidence). Blind spots: finite enumeration does not prove general dimensions, the explicit L_H formula, all full fibers, publication novelty, or PPA asymptotic slow tails. Those universal claims, where promoted, are borne by the displayed analytic proof and its reception; the fixedp=7/4 matching EB/dynamics are now proved independently by C227.


## C227: explicit quartic instance and genuine complete PPA

Run from the repository root:

```sh
python3 research/code/sparse_regularity/sharp_dynamics_verify.py
python3 research/code/sparse_regularity/independent_complete_review.py > research/code/sparse_regularity/independent_complete_results.json
```

Both use only the Python standard library; no random seed. `sharp_dynamics_results.json` records exact Fraction Cauchy/derivative/star/sign/localization gates, symmetric coefficients through degree12, profile/reduced quartic/asymptotic constants, three genuine two-variable implicit trajectories of100000 steps, and independent Decimal50/80-digit repetitions. The implementation evaluates the exact analytic derivatives directly and verifies both original proximal coordinate equations after Newton solving. Binary64 cancellation is diagnostic; the independent Decimal repetitions and analytic remainder certificate are recorded separately. Its recorded residuals and tolerances are diagnostic computational errors, not interval proofs. The axis formula and both tangent signs are checked. Finite sqrt(k) distances are deliberately compared honestly with the proved limit: the small certified initial radius causes a long transient, so those finite values do not by themselves demonstrate the asymptotic distance constant.

`independent_complete_review.py` independently recomputes the exact rational majorants and solves the unreduced two-coordinate equations for50000 steps from h0=.002,t0=.010 with lambda=1/128. Its residual tolerance is1e-13, ratio tolerance1e-4 and inverse-square slope relative tolerance.003; it checks a radial-axis step separately. Its stdout is retained in `independent_complete_results.json`.

## C225-v2: all finite upper exponents and separate strictness boundary

Run `python3 research/code/sparse_regularity/upper_family_verify.py` from the repository root. It records exact Fraction composition of the symmetric norm through fourth order, reverse checks of alpha0 and K, the retained endpoint sixth coefficient, and 80-digit independent coefficients at exponents just above 3/2, at 2, and through 100. It also checks the curved-path negative quartic coefficient, the exact global-minimum decomposition giving inactive saturation for every p>=2, and the removable kappa(0)=3/8 used in the genuine tracking recurrence. The actual finite parameter grid and outputs are in `upper_family_results.json`; no randomness is used. These checks corroborate algebra, not all-real-p statements or infinite-time dynamics.

The analytic [C225-v2 proof](../../topics/sparse_recovery/automatic_regularity.md#sr-sharpness-all-p) carries the expanded existence quantifier. The strict-complementarity counterexample is proved by a global sum-of-nonnegative-terms identity and norm ordering. C226's p<=3/2 constants and C227's specified-instance scope remain unchanged.

Actual parent reruns passed. [Verification manifest](verification_manifest.json) fixes all six code/result hashes, Python version, commands, arithmetic and precision. [Analytic proof](../../topics/sparse_recovery/sharp_instance_dynamics.md) proves the full box, all complete fibers, all local inputs, true-residual bound and infinite-time asymptotic; finite checks do not prove those quantifiers, maximal windows, arbitrary models or novelty. [Independent mathematical reception](../../audit/SPARSE_COMPLETE_DYNAMICS_REVIEW_2026_10_09.md) and [cross-review](../../audit/SPARSE_THRESHOLD_REVIEW_2026_10_09.md#sr-cross-dynamics) are separate evidence from the computations.

## Final independent arithmetic and sextic scope boundary

Run from the repository root:

    python3 research/code/sparse_regularity/sextic_boundary_verify.py > research/code/sparse_regularity/sextic_boundary_results.txt
    python3 research/code/sparse_regularity/final_dynamics_verify.py > research/code/sparse_regularity/final_dynamics_results.json

Both implementations were produced independently of the reviewed project verifiers and use only Python's standard library, with no random seed. The first uses exact Fraction polynomial identities and series through degree8: Pearson decomposition, endpoint sixth coefficient, general upper-family coefficients and the new p3 equality-parameter sextic profile/reduced coefficient. It proves finite algebraic facts, not the analytic neighborhood/isolated-zero-set assertions of C229. Those are in [its self-contained proof](../../topics/sparse_recovery/sextic_boundary.md).

The second reconstructs even analytic coefficients by the formal differential equation G H'=(4/7)G'H, checks Cauchy/star/sign/localization constants exactly, and solves both original implicit coordinate equations using stable series evaluation and two-variable Newton. It uses at most8 Newton passes per step, correction stopping tolerance2e-18, binary64 computations, four declared initial points, lambdas1/128 and1/1024, and counts10000,10000,4000,15000. A small-tangent run starts at(h,t)=(0.01,1e-8), exercising the non-circular tracking claim; both tangent signs and the separate axis law are checked. Maximum recorded coordinate residual is1.735e-18; final tracking ratios differ from−3/32 by less than9e-7 and reciprocal-square slope ratios differ from1 by less than4e-5. The finite sqrt(k)*distance remains far from the proved limit and is explicitly recorded as a transient. A truncated analytic series and float Newton are diagnostics, not validated interval bounds or universal trajectory proofs.

C230's sharp KL3/4 proof and scalar barrier are analytic. No trajectory plot, numerical energy fit or finite run is substituted for them. All output fingerprints and exact invocation strings are in the adjacent manifest.
