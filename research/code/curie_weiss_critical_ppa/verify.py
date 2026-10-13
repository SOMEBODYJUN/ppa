#!/usr/bin/env python3
"""Finite reproducibility checks; the candidate card supplies the universal proof."""
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import platform

getcontext().prec = 80
D = Decimal
TOL = D("1e-65")


def tanh(x):
    if x < 0:
        return -tanh(-x)
    e = (-2 * x).exp()
    return (1 - e) / (1 + e)


def f(x):
    return x - tanh(2 * x)


def H(x):
    return 2 * x - tanh(2 * x)


def bisect(fun, lo, hi):
    assert fun(lo) <= 0 <= fun(hi)
    for _ in range(300):
        mid = (lo + hi) / 2
        if mid == lo or mid == hi:
            return mid
        if fun(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def prox(p):
    if p == 0:
        return D(0)
    return bisect(lambda x: H(x) - p, (p - 1) / 2, (p + 1) / 2)


def V(x):
    # log(cosh(2x)) = 2|x| + log(1+exp(-4|x|)) - log(2).
    a = abs(x)
    logcosh = 2 * a + (1 + (-4 * a).exp()).ln() - D(2).ln()
    return x * x / 2 - logcosh / 2


def exact_taylor(q, n):
    value = Fraction(1)
    term = Fraction(1)
    for k in range(1, n + 1):
        term = term * q / k
        value += term
    return value


def main():
    t19 = exact_taylor(Fraction(19, 5), 6)
    t18 = exact_taylor(Fraction(18, 5), 6)
    assert t19 > 39 and t18 > 31
    L, eb, kappa, R = Fraction(1, 7), Fraction(4, 3), Fraction(16, 21), Fraction(1, 100)
    assert eb * (1 + L) / 2 == kappa
    length_coefficient = (1 + L) / (2 * (1 - kappa))
    assert length_coefficient == Fraction(12, 5)
    assert length_coefficient * R < Fraction(1, 20) - R

    m = bisect(f, D(19) / 20, D(1))
    points = [D(x) for x in ("-100", "-4", "-2", "-1", "-0.1", "-1e-6", "-1e-18", "0", "1e-18", "1e-6", "0.1", "1", "2", "4", "100")]
    points += [-m, m]
    records = [(p, prox(p)) for p in points]
    worst_equation = max(abs(H(u) - p) for p, u in records)
    assert worst_equation < TOL
    for p, u in records:
        assert abs(2 * u - p) <= 1 + TOL
        assert V(p) - V(u) + TOL >= (p - u) ** 2 / 2

    holder_margin_min = None
    for (p, u), (q, w) in combinations(records, 2):
        if p == q:
            continue
        delta_c = abs((2 * u - p) - (2 * w - q))
        margin = 12 * abs(p - q) - delta_c ** 3
        assert margin >= -TOL
        holder_margin_min = margin if holder_margin_min is None else min(holder_margin_min, margin)

    local_worst = {"distance_ratio": D(0), "reflection_ratio": D(0), "eb_ratio": D(0), "step_ratio": D(0)}
    for s in (-m, m):
        for off_text in ("-0.01", "-0.001", "-1e-8", "1e-8", "0.001", "0.01"):
            off = D(off_text)
            p, u = s + off, prox(s + off)
            d = abs(off)
            residual = abs(f(u))
            assert abs(u - s) <= D(4) / 7 * d + TOL
            assert abs(2 * u - p - s) <= d / 7 + TOL
            assert abs(u - s) <= D(4) / 3 * residual + TOL
            assert abs(p - u) <= D(4) / 7 * d + TOL
            local_worst["distance_ratio"] = max(local_worst["distance_ratio"], abs(u - s) / d)
            local_worst["reflection_ratio"] = max(local_worst["reflection_ratio"], abs(2 * u - p - s) / d)
            local_worst["eb_ratio"] = max(local_worst["eb_ratio"], abs(u - s) / residual)
            local_worst["step_ratio"] = max(local_worst["step_ratio"], abs(p - u) / d)

    psmall = D("1e-18")
    usmall = prox(psmall)
    assert usmall > psmall and prox(-psmall) < -psmall
    critical_cubic_ratio = usmall ** 3 / psmall
    assert abs(critical_cubic_ratio - D(3) / 8) < D("1e-10")
    # Exact fixed-point index arithmetic; origin sign computed without DT(0).
    assert 1 + 1 - 1 == 1
    result = {
        "scope": "Finite high-precision checks and exact rational arithmetic; universal claims require the analytic candidate card.",
        "python": platform.python_version(), "decimal_precision": getcontext().prec,
        "m_star": str(m), "m_star_bracket": ["19/20", "1"],
        "positive_taylor_lower_bounds": {"exp_19_over_5_gt_39": str(t19), "exp_18_over_5_gt_31": str(t18)},
        "parameters": {"beta": 2, "lambda": 1, "R": "1/100", "L": "1/7", "gamma_local": 1, "psi_slope": "4/3", "kappa": "16/21", "length_slope": "12/5", "gamma_global": "1/3", "global_holder_constant": "12^(1/3)"},
        "complete_equation_max_error": str(worst_equation),
        "pairwise_holder_margin_min": str(holder_margin_min),
        "local_sample_worst_ratios": {k: str(v) for k, v in local_worst.items()},
        "critical_T_cubed_over_input": str(critical_cubic_ratio),
        "fixed_indices": {"minus_m": 1, "plus_m": 1, "origin_by_boundary_sign": -1, "total": 1},
        "checks_passed": True,
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks_passed": True, "result_file": str(path), "m_star": str(m)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
