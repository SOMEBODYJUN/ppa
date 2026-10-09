# Sparse automatic regularity — C224/C225/C226 finite verification

Run from the repository root:

```sh
python3 research/code/sparse_regularity/verify.py
```

Python standard library only; no random seed (complete finite enumeration), exact `fractions.Fraction` algebra and independent 60/100-digit `decimal` calculations. The coordinating agent reran the original identical verifier successfully on 2026-10-09 before copying it here. Output is `automatic_regularity_results.json`.

Actual checks: 268200 finite moment/coefficient cases; the Pearson square identity and its endpoint equality conditions; p=3/2 symmetric coefficients 1/4, 0, 1/192; p=5/3, alpha=10 reduced strict-minimum values; inactive equality descent; A=I, b=(1,0), eta=1, xbar=(1,0), rho=1/16, lambda=1/100, input radius=1/250 complete-resolvent certificate and rational reverse checks.

Theorem proof and internal reception scope: [canonical mathematical module](../../topics/sparse_recovery/automatic_regularity.md#sr-evidence). Blind spots: finite enumeration does not prove general dimensions, the explicit L_H formula, all full fibers, publication novelty, or PPA asymptotic slow tails. Those universal claims, where promoted, are borne by the displayed analytic proof and its reception; matching upper-side EB/dynamics remain open.
