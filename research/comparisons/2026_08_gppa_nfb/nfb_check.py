#!/usr/bin/env python3
"""Independent finite checks for nfb_review.md; analytic proofs remain in the review.

Run from the repository root:
  python research/comparisons/2026_08_gppa_nfb/nfb_check.py
Only the Python standard library is required. The adjacent JSON is reproducible.
"""

from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent


def gap(tau, beta, rho, theta, zeta, zeta_m, eta):
    """Source (3.8), denoted Delta in the review to avoid the PPA step lambda."""
    r = min(rho, 0)
    return (2 - theta - 2 * eta * zeta
            - (tau + 2 * r) ** 2 / (2 * tau * (beta + r * (1 + zeta / tau)))
            + 2 * r * tau * ((zeta / tau + zeta_m) ** 2 + 4 * zeta / tau))


def quadratic(v, matrix):
    return sum(v[i] * matrix[i][j] * v[j]
               for i in range(len(v)) for j in range(len(v)))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def completion_check():
    # S = [[2, .6], [.6, 1.3]] is SPD; use its exact rational inverse.
    S = [[Q(2), Q(3, 5)], [Q(3, 5), Q(13, 10)]]
    det = S[0][0] * S[1][1] - S[0][1] ** 2
    inv = [[S[1][1] / det, -S[0][1] / det],
           [-S[0][1] / det, S[0][0] / det]]
    rng = random.Random(260822687)
    checks = 0
    for beta in [Q(1, 3), Q(1), Q(7, 2)]:
        for ratio in [Q(-99, 100), Q(-1, 2), Q(0), Q(3, 2)]:
            rho = beta * ratio
            q = beta * rho / (beta + rho)
            for _ in range(100):
                w = [Q(rng.randint(-100, 100), 13) for _ in range(2)]
                c = [Q(rng.randint(-100, 100), 17) for _ in range(2)]
                a = [w[i] - c[i] for i in range(2)]
                residual = [c[i] - rho * w[i] / (beta + rho) for i in range(2)]
                lhs = rho * quadratic(a, inv) + beta * quadratic(c, inv)
                rhs = q * quadratic(w, inv) + (beta + rho) * quadratic(residual, inv)
                assert lhs == rhs
                assert lhs >= q * quadratic(w, inv)
                checks += 1
    return {"exact_fraction_cases": checks, "all_equalities_and_inequalities_pass": True,
            "S": [[float(x) for x in row] for row in S]}


def overlap_checks():
    # Pure rotation F(x1,x2)=(-x2,x1), source anchored semimonotonicity
    # mu=1/4,rho=-1/4. Source (3.8) includes the final -1/2 term.
    d_rotation = gap(Q(1), Q(1), Q(-1, 4), Q(1), Q(0), Q(1), Q(1))
    assert d_rotation == Q(1, 3)
    vector = [Q(3, 7), Q(-2, 9)]
    for _ in range(20):
        p = [(vector[0] + vector[1]) / 2, (-vector[0] + vector[1]) / 2]
        assert dot(p, p) == dot(vector, vector) / 2
        vector = p

    # Genuine nonmonotone F=-I, same Euclidean PPA step 3.
    d_neg = gap(Q(3), Q(100), Q(-11, 10), Q(1), Q(0), Q(1, 3), Q(1))
    assert d_neg > 0
    x = Q(5, 7)
    for _ in range(20):
        p_nfb = (x / 3) / (Q(1, 3) - 1)
        p_ppa = x / (1 - 3)
        assert p_nfb == p_ppa == -x / 2
        x = p_nfb

    # Nonzero C absorbed into a fixed positive metric: F=2I.
    d_affine = gap(Q(1), Q(3), Q(0), Q(1), Q(0), Q(1), Q(1))
    assert d_affine == Q(5, 6)
    x = Q(5, 7)
    for _ in range(20):
        p = (Q(3, 2) * x - Q(1, 2) * x) / 3
        assert p == x / 3
        x = p

    # Nonzero memory initialization also yields the ordinary PPA for F=I.
    d_memory = gap(Q(1), Q(10), Q(0), Q(1), Q(1, 10), Q(9, 10), Q(1))
    assert d_memory == Q(3, 4)
    x, u = Q(5, 7), Q(1, 14)
    for _ in range(20):
        assert u == x / 10
        p = (Q(9, 10) * x - Q(1, 10) * x + u) / Q(9, 5)
        u_new = -Q(1, 10) * (p - x)
        assert p == x / 2
        assert u_new == p / 10
        x, u = p, u_new
    return {
        "pure_rotation": {"source_gap_exact": str(d_rotation),
                          "physical_PPA_norm_factor": 1 / math.sqrt(2),
                          "C02_compatibility_test_at_lambda_1": 1},
        "negative_identity": {"source_gap_exact": str(d_neg), "source_gap": float(d_neg),
                              "physical_PPA_factor": -0.5, "RL_L": 2, "compatibility_kappa": 0.5},
        "nonzero_C_affine_absorption": {"source_gap_exact": str(d_affine), "physical_PPA_factor": 1 / 3},
        "nonzero_C_memory_compensation": {"source_gap_exact": str(d_memory), "physical_PPA_factor": 0.5},
        "exact_iterations_per_example": 20,
    }


def obstruction_checks():
    # C191 data: D=[-1,1], f=2, b=lambda=1, alpha=2/3, M=7, C=R+.
    # t=eps^(1/3)>0 gives V_D(t)={1}; n=0 gives w=(-eps^(2/3),7eps).
    natural = []
    large_V = [[10000.0, 3000.0], [3000.0, 20000.0]]
    for exponent in [3, 6, 9, 12, 15, 18]:
        e = 10.0 ** (-exponent)
        h = [e ** (1 / 3), e]
        w = [-e ** (2 / 3), 7 * e]
        inner, norm2 = dot(h, w), dot(w, w)
        natural.append({"epsilon": e, "anchor_ratio": inner / norm2,
                        "gap_for_large_PSD_V": inner + quadratic(w, large_V)})
    assert natural[-1]["gap_for_large_PSD_V"] < 0
    assert all(natural[i + 1]["anchor_ratio"] < natural[i]["anchor_ratio"]
               for i in range(len(natural) - 1))

    cap = []
    for exponent in [3, 6, 9, 12, 15]:
        e = 10.0 ** (-exponent)
        h, w = [e ** 0.25, 0, e], [-2 * math.sqrt(e), 0, 3 * e]
        cap.append({"epsilon": e, "anchor_ratio": dot(h, w) / dot(w, w)})
    assert all(cap[i + 1]["anchor_ratio"] < cap[i]["anchor_ratio"]
               for i in range(len(cap) - 1))

    # C141, gamma=1/2, nu=2, A=B=1, second anchor coordinate 0.
    superlinear = []
    for exponent in [3, 6, 9, 12, 15, 18]:
        e = 10.0 ** (-exponent)
        h = [e ** 0.125, 0, e]
        w = [-e ** 0.25, 0, math.sqrt(e) - e]
        superlinear.append({"epsilon": e, "anchor_ratio": dot(h, w) / dot(w, w)})
    assert all(superlinear[i + 1]["anchor_ratio"] < superlinear[i]["anchor_ratio"]
               for i in range(len(superlinear) - 1))

    logarithmic = []
    for a in [0.5, 1.0, 2.0]:
        rows = []
        for s in [10, 30, 100, 300, 500]:
            y = math.exp(-s) / 4
            ell = (1 + s) ** (-a)
            h, w = [math.sqrt(ell), y], [-ell, 3 * y]
            rows.append({"s": s, "anchor_ratio": dot(h, w) / dot(w, w),
                         "asymptotic_ratio": -(1 + s) ** (a / 2)})
        assert all(rows[i + 1]["anchor_ratio"] < rows[i]["anchor_ratio"]
                   for i in range(len(rows) - 1))
        logarithmic.append({"a": a, "rows": rows})
    return {"natural_C191": natural, "cap_C137": cap,
            "superlinear_C141": superlinear, "logarithmic_C10": logarithmic,
            "status": "Finite evidence only; divergence and universal metric exclusion are proved analytically in nfb_review.md."}


def product_compression_check():
    # A genuinely mixed product metric; zero dual residual eliminates the lifted variable.
    inv = [[Q(2), Q(3, 5)], [Q(3, 5), Q(13, 10)]]
    x, z, residual = Q(3, 7), Q(-2, 9), Q(5, 11)
    cases = 0
    for dual in [Q(-1000000), Q(-3, 2), Q(0), Q(7, 3), Q(1000000)]:
        for dual_anchor in [Q(-200), Q(0), Q(300)]:
            h = [x - z, dual - dual_anchor]
            w = [residual, Q(0)]
            assert dot(h, w) == (x - z) * residual
            assert quadratic(w, inv) == inv[0][0] * residual ** 2
            cases += 1
    return {"exact_fraction_cases": cases, "non_diagonal_metric": True,
            "arbitrarily_large_lifted_variable_changes_neither_pairing_nor_residual_quadratic": True}


def main():
    pdf = HERE / "sources/nfb_2608.22687v1.pdf"
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert digest == "14db75596189d898d97aa9389b3e1a50bbe2ed70e207a3257d681cb4d01077b9"
    output = {"source_pdf_sha256": digest,
              "scope": "Independent arithmetic and witness checks, not a proof by finite search.",
              "completion": completion_check(), "exact_PPA_overlaps": overlap_checks(),
              "obstruction_witnesses": obstruction_checks(),
              "standard_product_compression": product_compression_check()}
    dest = HERE / "nfb_results.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"result_file": str(dest), "all_assertions_pass": True,
                      "completion_cases": output["completion"]["exact_fraction_cases"],
                      "negative_identity_source_gap": output["exact_PPA_overlaps"]["negative_identity"]["source_gap"]},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
