# Sharp sparse automatic structure and complete proximal dynamics

[Standalone English manuscript](sharp_sparse_regularity.tex) and [compiled PDF](sharp_sparse_regularity.pdf) collect the complete statements and self-contained proofs of C224–C228. The mathematical center is automatic active-Hessian positivity at every nonzero local minimum for 1<p<=3/2, with the endpoint sixth-order argument and strict-minimum counterexamples for every3/2<p<2. Strict complementarity for1<p<2 and support independence for finitep>1 have separate ranges and are supporting structure, not additional3/2 thresholds.

The complete-resolvent theorem provides computable continuity/curvature constants, a common positive step interval, all-output exclusion, independently proved global-proximal existence/equality, support identification, invariant ball, strong true-residual linear EB and variable-step contraction. The fixedp=7/4 example separately proves sharp exponent1/3, completeprox on the closed1/64 ball for every0<lambda<=1/128, and the actual fixed-step off-axis norm limit16/sqrt(13lambdaR); the radial axis is exactly geometric. No critical-curve invariance or upper-side uniform exponent is assumed.

## Canonical dependencies and actual reception

- [Automatic structure, family and explicit windows](../../topics/sparse_recovery/automatic_regularity.md): C224–C226 and C228.
- [Explicit residual and actual full-PPA proof](../../topics/sparse_recovery/sharp_instance_dynamics.md): C227, including the separately recorded noninvariance obstruction.
- [Independent threshold and cross-dynamics review](../../audit/SPARSE_THRESHOLD_REVIEW_2026_10_09.md) and [complete-prox/dynamics review](../../audit/SPARSE_COMPLETE_DYNAMICS_REVIEW_2026_10_09.md): actual reconstruction and final source-transcription scope.
- [Finite computational record](../../code/sparse_regularity/README.md): reproducible inputs, arithmetic, precision, tolerances and blind spots.
- [Precise primary-source audit](../../audit/SPARSE_PRIORITY_AUDIT_2026_10_09.md): 2015 published support antecedent accepted; Wang–Zhang2017 Appendix inspected but main body unavailable; Huo–Chen–Ge–Ng2023 body unavailable. Exact threshold publication priority and journal suitability are not certified. If an exact antecedent appears, the novelty claim must be withdrawn; ordinary local convergence cannot replace it by relabeling.

## Build and visual verification

In a normal TeX Live installation, from this directory run twice:

```sh
pdflatex -interaction=nonstopmode -halt-on-error sharp_sparse_regularity.tex
```

Packages: geometry, amsmath, amssymb, amsthm, mathtools, microtype, booktabs, hyperref; standard scalable Computer Modern/AMS fonts. No external figures or inputs are required.

The present restricted runtime had TeX Live source/packages/fonts but lacked a prebuilt pdflatex format and pdftex.map. A format was built under scratch from its installed pdflatex.ini, and a scratch map combined the installed AMS/Computer Modern maps. Nothing outside the workspace was modified. The resulting PDF is an actual LaTeX compilation, with embedded scalable fonts. The final compile log has no undefined references, missing citations, overfull boxes or errors. All twelve pages were rendered with system Poppler and inspected; the last cosmetic operator change was recompiled and its affected page inspected. Manuscript reception independently compared all41 dynamics displays and complete definitions/quantifiers against the accepted module.

The adjacent `manuscript_verification.json` records final source/PDF fingerprints, page count and the scope of this visual check. Intermediate format, log and page images are reproducible scratch work and are not research assets.
