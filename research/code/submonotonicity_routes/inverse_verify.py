#!/usr/bin/env python3
"""Specific-instance checks; universal statements are proved in inverse_geometry_review.md.

Run: python3 research/code/submonotonicity_routes/inverse_verify.py
Python standard library only. Float checks do not certify general inequalities.
"""
from fractions import Fraction as Q
import json
import math
import platform
import random


def bisect(fun, lo, hi, steps=100):
    for _ in range(steps):
        mid = (lo + hi) / 2
        if fun(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def endpoint_step(x):
    sign = 1 if x >= 0 else -1
    p = abs(x)
    w = bisect(lambda z: z ** 3 + z / 2 - p, 0, 2 * p)
    return sign * (w ** 3 - w / 2)


def main():
    lam, rho, positive_slope = Q(3), Q(1), Q(1, 100)
    eigen_j = [1 / (1 - lam), 1 / (1 + lam * positive_slope)]
    eigen_c = [2 * v - 1 for v in eigen_j]
    eb = Q(100)
    reflected_l = max(abs(v) for v in eigen_c)
    direct_factor = eb * (1 + reflected_l) / (2 * lam)
    energy_q = (1 + reflected_l ** 2) / (2 * (1 + (lam / eb) ** 2))
    inverse_q = 1 / math.sqrt(1 + float(lam * (lam - 2 * rho) / eb ** 2))
    energy_threshold = bisect(lambda v: v * (v - 1) ** 2 - 20000, 2, 100)
    lt_threshold = bisect(lambda v: v * (v - 1) ** 2 - 2 * (v + 100) ** 2, 2, 200)
    lt_tau = (reflected_l ** 2 - 1) / 4
    lt_test = lt_tau * (1 + eb / lam) ** 2

    # Exact rational cubic uniform monotonicity identity, seed and grid recorded.
    random.seed(20261014)
    cubic_pairs = []
    for _ in range(200):
        w, z = Q(random.randint(-200, 200), 100), Q(random.randint(-200, 200), 100)
        t = w - z
        lhs = t * (w ** 3 - z ** 3) - t ** 4 / 4
        rhs = 3 * t ** 2 * (w + z) ** 2 / 4
        assert lhs == rhs and lhs >= 0
        cubic_pairs.append(float(lhs))

    x, length, rows = 0.1, 0.0, []
    for k in range(1, 100001):
        nx = endpoint_step(x)
        assert nx * x < 0 and abs(nx) < abs(x)
        length += abs(nx - x)
        x = nx
        if k in (100, 1000, 10000, 100000):
            rows.append({"k": k, "abs_x": abs(x), "k_x_squared": k * x ** 2, "prefix_length": length})

    shear = []
    gamma, c = 0.5, 2 ** 0.5
    for exponent in (2, 4, 6, 8):
        t = 10 ** (-exponent)
        du = (t ** (gamma / 2), t)
        dw = (-c * t ** gamma, t)
        ratio = -(du[0] * dw[0] + du[1] * dw[1]) / (dw[0] ** 2 + dw[1] ** 2)
        shear.append({"t": t, "required_cohypo_rho": ratio})

    result = {
        "environment": {"python": platform.python_version(), "dependencies": "standard library", "seed": 20261014},
        "diagonal": {"J_eigenvalues_exact": [str(v) for v in eigen_j], "C_eigenvalues_exact": [str(v) for v in eigen_c], "true_EB_K": str(eb), "sharp_RL_L": str(reflected_l), "sharp_cohypo_rho": str(rho), "actual_contraction": float(max(abs(v) for v in eigen_j)), "RL_direct_factor_exact": str(direct_factor), "RL_energy_q_exact": str(energy_q), "RL_energy_q": float(energy_q), "inverse_distance_q": inverse_q, "RL_direct_lambda_gate": ">101", "RL_energy_lambda_threshold": energy_threshold, "LT_tau_exact": str(lt_tau), "LT_tau_times_EB_factor_exact": str(lt_test), "LT_lambda_threshold": lt_threshold, "inverse_lambda_gate": ">2"},
        "cubic_exact_checks": {"pairs": len(cubic_pairs), "identity": "dw*(w^3-z^3)-dw^4/4 = 3*dw^2*(w+z)^2/4", "min_gap": min(cubic_pairs)},
        "endpoint_orbit": rows,
        "collision": {"lambda": 1, "epsilon": 0.1, "q": 1.5, "C": 1, "value_pair_radius": 0.5, "quadratic_to_gauge_ratio_bound": 1.01 * math.sqrt(0.5), "J_at_zero": [-0.1, 0.0, 0.1]},
        "shear_no_finite_co": shear,
        "scope": "Numerical and rational checks of named examples only; proofs and all quantifiers are in the review."
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
