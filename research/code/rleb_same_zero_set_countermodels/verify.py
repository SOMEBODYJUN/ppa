#!/usr/bin/env python3
"""Reproducible finite checks for the analytic scalar comparison in the sibling report.

No external dependencies. Exact identities use rational polynomial coefficients;
numeric checks use CPython binary64. These checks do not prove the quantified
analytic claims, which are established in same_zero_set_countermodels.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
import json
import math
from pathlib import Path
import platform
import random


def poly_add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Q(0)) + coefficient
    return {m: c for m, c in out.items() if c}


def poly_mul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            monomial = (i + k, j + ell)
            out[monomial] = out.get(monomial, Q(0)) + x * y
    return {m: c for m, c in out.items() if c}


def poly_scale(a, c):
    return {m: c * x for m, x in a.items() if c * x}


def flat(y):
    return 0.0 if y == 0.0 else y * math.exp(-1.0 / (y * y))


def h(y):
    return y + flat(y)


def reflection_at_output(y):
    # C(h(y)) = 2y - h(y). This form avoids needless subtraction at large y.
    return 0.0 if y == 0.0 else -y * math.expm1(-1.0 / (y * y))


def prox_flat(x):
    if x == 0.0:
        return 0.0
    if x < 0.0:
        return -prox_flat(-x)
    # 0 <= F(y) <= y implies the entire unique positive root lies in [x/2, x].
    lo, hi = x / 2.0, x
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if mid == lo or mid == hi:
            break
        if h(mid) > x:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def main():
    q, s = {(1, 0): Q(1)}, {(0, 1): Q(1)}
    t, c = poly_add(q, s), poly_add(q, poly_scale(s, Q(-1)))
    energy_identity = poly_add(
        poly_mul(t, t), poly_mul(c, c),
        poly_scale(poly_mul(q, q), Q(-2)),
        poly_scale(poly_mul(s, s), Q(-2)),
    )
    assert energy_identity == {}
    nonexpansive_difference = poly_add(
        poly_mul(t, t), poly_scale(poly_mul(c, c), Q(-1)),
        poly_scale(poly_mul(q, s), Q(-4)),
    )
    assert nonexpansive_difference == {}
    good_kappa = Q(1, 2)
    good_energy_rhs_coefficient = Q(1, 2)
    good_energy_lhs_coefficient = Q(2)
    assert good_energy_lhs_coefficient * good_kappa**2 == good_energy_rhs_coefficient
    assert Q(1, 2) / (1 - good_kappa) == 1  # Theta_good(t) = t.

    rng = random.Random(20261013)
    outputs = [0.0]
    for _ in range(600):
        magnitude = 10.0 ** rng.uniform(-1.25, 2.0)
        outputs.append(magnitude * rng.choice((-1.0, 1.0)))
    largest_inverse_relative_error = 0.0
    largest_reflection_abs = 0.0
    largest_lipschitz_excess = 0.0
    largest_half_holder_excess = 0.0
    for y in outputs:
        x = h(y)
        reconstructed = prox_flat(x)
        err = abs(reconstructed - y) / max(1.0, abs(y))
        largest_inverse_relative_error = max(largest_inverse_relative_error, err)
        largest_reflection_abs = max(largest_reflection_abs, abs(reflection_at_output(y)))
        assert err < 5e-15
        assert abs(reflection_at_output(y)) <= 1.0 + 2e-15
    for _ in range(5000):
        y1, y2 = rng.choice(outputs), rng.choice(outputs)
        delta = abs(h(y1) - h(y2))
        cdiff = abs(reflection_at_output(y1) - reflection_at_output(y2))
        lip_excess = cdiff - delta
        holder_excess = cdiff - math.sqrt(2.0 * delta)
        largest_lipschitz_excess = max(largest_lipschitz_excess, lip_excess)
        largest_half_holder_excess = max(largest_half_holder_excess, holder_excess)
        assert lip_excess < 5e-13
        assert holder_excess < 5e-13

    ratios = []
    for y in (1.0, 0.5, 0.35, 0.25, 0.2, 0.15, 0.125):
        e = math.exp(-1.0 / (y * y))
        ratios.append({
            "output_y": y,
            "input_x_binary64": h(y),
            "residual": flat(y),
            "exp_minus_inverse_square": e,
            "output_input_ratio_binary64": 1.0 / (1.0 + e),
            "ratio_gap_exact_formula_e_over_1_plus_e_binary64": e / (1.0 + e),
            "rounds_ratio_to_one": 1.0 / (1.0 + e) == 1.0,
        })

    orbit_checks = []
    for x0 in (-10.0, -1.0, -0.35, 0.0, 0.35, 1.0, 10.0):
        x = x0
        accumulated = 0.0
        largest_residual = 0.0
        for _ in range(3000):
            y = prox_flat(x)
            assert abs(y) <= abs(x) + 5e-15
            assert x * y >= 0.0
            accumulated += abs(x - y)
            largest_residual = max(largest_residual, abs(x - h(y)))
            x = y
        assert abs(accumulated - (abs(x0) - abs(x))) < 1e-12
        orbit_checks.append({
            "initial": x0,
            "iterations": 3000,
            "last": x,
            "prefix_length": accumulated,
            "telescoping_length": abs(x0) - abs(x),
            "max_equation_error_binary64": largest_residual,
        })

    result = {
        "status": "all finite checks passed; universal statements have analytic proofs in report",
        "environment": {"python": platform.python_version(), "precision": "IEEE754 binary64", "seed": 20261013},
        "exact_polynomial_checks": {
            "t_squared_plus_c_squared_equals_2q_squared_plus_2s_squared": True,
            "t_squared_minus_c_squared_equals_4qs": True,
            "good_energy_gate_kappa_half": True,
            "good_tail_coefficient_one": True,
        },
        "finite_global_checks": {
            "number_outputs": len(outputs),
            "number_pairs": 5000,
            "max_inverse_relative_error": largest_inverse_relative_error,
            "max_abs_C_sampled": largest_reflection_abs,
            "max_positive_Lip1_excess": largest_lipschitz_excess,
            "max_positive_Holder_half_sqrt2_excess": largest_half_holder_excess,
        },
        "contraction_ratio_samples": ratios,
        "orbit_prefix_checks": orbit_checks,
        "numeric_caveat": "At tiny outputs the positive decrement lies below binary64 resolution. A displayed ratio of 1 is rounding, not an extra fixed point. No asymptotic convergence is inferred from finite prefixes.",
    }
    destination = Path(__file__).with_name("results.json")
    destination.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"saved": str(destination), "status": result["status"], "finite_global_checks": result["finite_global_checks"]}, indent=2))


if __name__ == "__main__":
    main()
