# Free particle complete-fiber checks

Run `python research/code/free_particle_rleb/verify.py` from the repository root.
The script uses only Python's standard library and writes `results.json` beside itself.
It checks signed and zero inputs, tube boundaries, globally recovered graph points,
exact iterate formulas, small-distance full-pair reflected inequalities, metric roots
including double roots, residual identities, and the C241-v2 arithmetic budget.

Seed: 20261011. Exact constants use `Fraction`; square roots and sampled roots use
binary64 with stated tolerances. No interval numerical proof is claimed. The result
records the Python version and verifier SHA256. Universal conclusions follow from
[the analytic proof](../../canonical/free_particle_rleb.md), independently of the samples.

`optimization_verify.py` independently checks the convex comparator and records
`optimization_candidate_checks.json`; its finite scope is specified in that script.
