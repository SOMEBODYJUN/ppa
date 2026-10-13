#!/usr/bin/env python3
"""Finite checks of the nonnegative full relation and exact constant arithmetic."""
from decimal import Decimal, getcontext
from fractions import Fraction
import json
from pathlib import Path
import platform

getcontext().prec = 80
D = Decimal
TOL = D("1e-65")


def cbrt(x):
    if not x:
        return D(0)
    return (abs(x).ln() / 3).exp() * (1 if x > 0 else -1)


def f(x):
    return (x - 1) * (x - 2) * (x - 3)


def prox(p):
    return D(0) if p <= -6 else 2 + cbrt(p - 2)


def potential_positive(x):
    assert x >= 0
    t = x - 2
    return t ** 4 / 4 - t ** 2 / 2


def main():
    # Id+f identity is verified exactly at rational sample states.
    for u in [Fraction(0), Fraction(1, 4), Fraction(1), Fraction(2), Fraction(3), Fraction(4), Fraction(17, 3)]:
        assert u + f(u) == (u - 2) ** 3 + 2
    assert Fraction(25, 16) < Fraction(64, 27)
    assert Fraction(9, 16) > Fraction(8, 27)
    assert Fraction(83, 64) > Fraction(5, 4)
    L, eb, kappa, R = Fraction(1, 2), Fraction(4, 5), Fraction(3, 5), Fraction(1, 16)
    assert eb * (1 + L) / 2 == kappa
    length = (1 + L) / (2 * (1 - kappa))
    assert length == Fraction(15, 8)
    assert length * R < Fraction(1, 4) - R

    points = [D(x) for x in ("-100", "-6.000000000000000001", "-6", "-5.999999999999999999", "-4", "-1", "0", "0.5", "1", "1.999999999999999999", "2", "2.000000000000000001", "3", "4", "10", "100")]
    equation_error = D(0)
    for p in points:
        u = prox(p)
        assert u >= 0
        if u == 0:
            assert p <= -6  # p-u belongs to the full normal-cone fiber (-inf,-6].
        else:
            error = abs(p - u - f(u))
            equation_error = max(equation_error, error)
            assert error < TOL
        if p >= 0:
            assert u > 0
            assert potential_positive(p) - potential_positive(u) + TOL >= (p - u) ** 2 / 2

    assert 0 < prox(D(-4)) < prox(D(4)) < 4
    local_worst = {"distance_ratio": D(0), "reflection_ratio": D(0), "eb_ratio": D(0), "step_ratio": D(0)}
    for s in (D(1), D(3)):
        for off_text in ("-0.0625", "-0.01", "-1e-8", "1e-8", "0.01", "0.0625"):
            off = D(off_text)
            p, u = s + off, prox(s + off)
            d = abs(off)
            residual = abs(f(u))
            assert abs(u - s) <= d / 2 + TOL
            assert abs(2 * u - p - s) <= d / 2 + TOL
            assert abs(u - s) <= D(4) / 5 * residual + TOL
            assert abs(p - u) <= D(3) / 4 * d + TOL
            local_worst["distance_ratio"] = max(local_worst["distance_ratio"], abs(u - s) / d)
            local_worst["reflection_ratio"] = max(local_worst["reflection_ratio"], abs(2 * u - p - s) / d)
            local_worst["eb_ratio"] = max(local_worst["eb_ratio"], abs(u - s) / residual)
            local_worst["step_ratio"] = max(local_worst["step_ratio"], abs(p - u) / d)

    # Exact input p=2 has three real positive outputs when lambda=2.
    lam = D(2)
    a = ((lam - 1) / lam).sqrt()
    above_critical = [2 - a, D(2), 2 + a]
    for u in above_critical:
        assert u > 0 and abs(2 - u - lam * f(u)) < TOL
    eps = D("1e-18")
    assert prox(2 + eps) > 2 + eps
    assert prox(2 - eps) < 2 - eps
    assert abs((prox(2 + eps) - 2) ** 3 / eps - 1) < TOL
    # Full C cannot be globally sublinear Holder: C(p)=-p for p<=-6.
    for n in (D(10), D(100), D(1000)):
        assert 2 * prox(-n) + n == n

    result = {
        "scope": "Finite high-precision checks and exact rational arithmetic; universal claims and indices require the analytic candidate card.",
        "python": platform.python_version(), "decimal_precision": getcontext().prec,
        "parameters": {"cubic_coefficients": [1, -6, 11, -6], "lambda": 1, "domain": "[0,infinity)", "normal_cone_fiber_at_zero": "(-infinity,-6]", "R": "1/16", "L": "1/2", "gamma_local": 1, "psi_slope": "4/5", "kappa": "3/5", "length_slope": "15/8"},
        "complete_equation_max_error": str(equation_error),
        "large_ball": {"radius": 4, "left_output": str(prox(D(-4))), "right_output": str(prox(D(4))), "strict_inside": True},
        "local_sample_worst_ratios": {k: str(v) for k, v in local_worst.items()},
        "critical_input": 2, "critical_output": 2, "critical_local_holder_power": "1/3",
        "above_critical_lambda_2_outputs_at_input_2": [str(x) for x in above_critical],
        "full_zero_set": [1, 2, 3], "target_M": [1, 3],
        "fixed_indices": {"one": 1, "three": 1, "two_by_boundary_sign": -1, "total": 1},
        "global_sublinear_reflection_holder": False,
        "checks_passed": True,
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks_passed": True, "result_file": str(path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
