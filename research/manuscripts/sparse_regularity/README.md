# Sharp automatic structure and complete proximal dynamics

The [standalone English manuscript](sharp_sparse_regularity.tex) and [compiled PDF](sharp_sparse_regularity.pdf) contain complete statements and self-contained proofs of C224–C230. The mathematical center is automatic active-Hessian positivity at every nonzero local minimum for1<p<=3/2, with no RIP, genericity or assumed SOSC. The endpoint sixth-order certificate and an independent curved radial fourth-order proof are both retained. Strict-minimum singular-Hessian examples exist for every finitep>3/2. Strict complementarity (1<p<2) and support independence (finitep>1) have separate wider ranges; support independence has an acknowledgedp=2 antecedent.

The quantitative complete-resolvent theorem gives computable curvature/continuity radii and a common positive step interval. It proves all-output exclusion, identification, independently obtained global-proximal existence, fullJ=globalprox, invariance and variable-step local linear convergence. Neither SOSC, an error bound nor complete single-valuedness is assumed.

The specifiedp=7/4 instance has the matching sharp strong true-residual exponent1/3. On the closed1/64 ball and every0<lambda<=1/128, the full proximal relation is single-valued, equals globalprox and stays in that ball. Every off-axis initial point has the actual norm limit16/sqrt(13lambdaR) after multiplication bysqrt(k), with h_k/t_k²→−3/32; the radial axis has its separate exact geometric law. The critical curve is expressly shown not to be invariant.

Two supporting boundary proofs are included: the equality-parameterp=3 sextic strict minimum has sharp true-residual exponent1/5, ruling out a universal upper-side1/3; the specified quartic instance has sharp KL exponent3/4, yielding the classical energyO(k^-2) and pointO(k^-1/2) upper bounds. Classical KL tools apply. They do not by themselves establish complete-output exclusion or the exact nonaxis constant.

## Canonical proofs and actual independent reception

- [Automatic structure, upper family and explicit windows](../../topics/sparse_recovery/automatic_regularity.md): C224–C226 and C228.
- [Fixed-instance residual, actual full-PPA and KL proof](../../topics/sparse_recovery/sharp_instance_dynamics.md): C227 and C230.
- [Sextic scope boundary](../../topics/sparse_recovery/sextic_boundary.md): C229, with matching full-neighborhood residual proof, no new PPA claim.
- [Final four-group reception](../../audit/SPARSE_FINAL_RECEPTION_2026_10_10.md): two independent structural reconstructions, separate complete-prox/trajectory reconstruction, actual final transcription checks and precise priority/value scope. Earlier [threshold](../../audit/SPARSE_THRESHOLD_REVIEW_2026_10_09.md) and [complete-dynamics](../../audit/SPARSE_COMPLETE_DYNAMICS_REVIEW_2026_10_09.md) receptions remain as prior evidence.
- [Reproducible finite checks](../../code/sparse_regularity/README.md): exact rational identities, independent precision checks and actual two-variable updates, separated from universal analytic proofs.

## Submission and prior-comparison boundary

This is a mathematically complete, internally independently checked submission candidate. It is not external peer review, journal acceptance or certified first publication. The [bounded primary-source comparison](../../audit/SPARSE_PRIORITY_AUDIT_2026_10_09.md#final-submission-source-check) records the actual models, theorem/page locators, source versions and reading scopes. The published2015 support antecedent is accepted. Complete2026 fractional and2023 block-recovery bodies, generic2014 smoothing results and the classic ABS framework are compared. Wang–Zhang2017 main statements/body, Huo–Chen–Ge–Ng2023 body and the relevant Zhao2018 body remain unavailable; their lack of access is not absence evidence.

No exact matching threshold theorem has been identified in the passages actually read. The contribution wording remains bounded, with the sharp automatic active-PD theorem at the center. If a complete matching antecedent is later found, withdraw the corresponding novelty and reassess independent-paper value; ordinary local rates cannot replace it by relabeling. These literature limits do not prevent delivery of the mathematical candidate.

## Build and visual verification

In a normal TeX Live installation, from this directory run twice:

    pdflatex -interaction=nonstopmode -halt-on-error sharp_sparse_regularity.tex

Packages: geometry, amsmath, amssymb, amsthm, mathtools, microtype, booktabs, hyperref; standard scalable Computer Modern/AMS fonts. No external figures or source inputs are required.

The restricted runtime used installed TeX sources/fonts with a scratch-built pdflatex format and scratch map combining installed AMS/Computer Modern maps; nothing outside the workspace was changed. The final source was compiled twice with actual LaTeX. Its log contains no errors, missing citations, undefined references, overfull boxes or warnings. All14 pages were rendered at85dpi with system Poppler and visually inspected. The explicit complete-dynamics theorem stays intact on page8; the new sextic proof is on page5, KL proof on page13 and compact bibliography on page14, with no orphan reference page, clipping or overlap.

The19 dynamic source labels now use ordinary numbered equation environments and all references were checked after two passes. A reviewer caught the initial unnumbered-environment transcription issue before the final compile; that correction is recorded in the final reception. The adjacent manuscript_verification.json records current hashes and actual review scope. Intermediate formats, logs and page images are reproducible scratch work.
