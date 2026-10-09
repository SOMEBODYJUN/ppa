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

Both use only the Python standard library; no random seed. `sharp_dynamics_results.json` records exact Fraction Cauchy/derivative/star/sign/localization gates, symmetric coefficients through degree12, profile/reduced quartic/asymptotic constants, three genuine two-variable implicit trajectories of100000 steps, and independent Decimal50/80-digit repetitions. The implementation uses the exact analytic derivatives, evaluates the analytic remainder by its convergent series near cancellation, and verifies both original proximal coordinate equations after Newton solving. Its recorded residuals and tolerances are diagnostic computational errors, not interval proofs. The axis formula and both tangent signs are checked. Finite sqrt(k) distances are deliberately compared honestly with the proved limit: the small certified initial radius causes a long transient, so those finite values do not by themselves demonstrate the asymptotic distance constant.

`independent_complete_review.py` independently recomputes the exact rational majorants and solves the unreduced two-coordinate equations for50000 steps from h0=.002,t0=.010 with lambda=1/128. Its residual tolerance is1e-13, ratio tolerance1e-4 and inverse-square slope relative tolerance.003; it checks a radial-axis step separately. Its stdout is retained in `independent_complete_results.json`.

Actual parent reruns passed. [Verification manifest](verification_manifest.json) fixes all six code/result hashes, Python version, commands, arithmetic and precision. [Analytic proof](../../topics/sparse_recovery/sharp_instance_dynamics.md) proves the full box, all complete fibers, all local inputs, true-residual bound and infinite-time asymptotic; finite checks do not prove those quantifiers, maximal windows, arbitrary models or novelty. [Independent mathematical reception](../../audit/SPARSE_COMPLETE_DYNAMICS_REVIEW_2026_10_09.md) and [cross-review](../../audit/SPARSE_THRESHOLD_REVIEW_2026_10_09.md#sr-cross-dynamics) are separate evidence from the computations.
