#!/usr/bin/env python3
"""Formula checks for unified_curved_zero_certificate.md; not a fiber proof.

Python >=3.10, standard library only, deterministic grids, float64.
Run from repository root: python3 research/code/unified_ppa/curved_verify.py
"""
from math import cos, sin, sqrt


def radial_ratio(s, lam, m, b, gamma, model):
    u = abs(s)
    a = 1 + lam * m
    b2 = lam * lam * b * b
    if model == "plain":
        gn = m * s
        delta = 2 * a * s + a * a * s * s + b2 * u ** (2 * gamma)
    elif model == "compensated":
        root = sqrt(1 - b2 * u ** (2 * gamma))
        gn = m * s - lam * b * b * u ** (2 * gamma) / (1 + root)
        delta = 2 * a * s * root + a * a * s * s
    elif model == "quadratic":
        gn = m * s - lam * b * b * u ** (2 * gamma) / 2
        delta = (2 * a * s + a * a * s * s
                 - a * b2 * s * u ** (2 * gamma)
                 + b2 * b2 * u ** (4 * gamma) / 4)
    else:
        raise ValueError(model)
    radius = sqrt(1 + delta)
    # Rationalization prevents cancellation in radius - 1 at tiny scales.
    signed_ratio = delta / ((radius + 1) * u)
    return signed_ratio, gn, radius


def check_vector_identities():
    worst = 0.0
    for model in ("plain", "compensated", "quadratic"):
        for gamma in (0.2, 0.25, 0.4, 0.5, 0.7):
            for s in (-1e-3, -1e-5, 1e-5, 1e-3):
                for b in (0.7, 1.0, 2.0):
                    lam, m, theta = 0.5, 2.0, 0.731
                    _, gn, radius = radial_ratio(s, lam, m, b, gamma, model)
                    tangent = b * abs(s) ** gamma
                    x1 = (1 + s + lam * gn) * cos(theta) - lam * tangent * sin(theta)
                    x2 = (1 + s + lam * gn) * sin(theta) + lam * tangent * cos(theta)
                    err = abs(x1 * x1 + x2 * x2 - radius * radius)
                    worst = max(worst, err)
                    assert err < 2e-14
    return worst


def check_compensated_window():
    lam, m, c, cap, gamma = 1.0, 1.0, 1.0, 3.0, 0.2
    a, bcap = 1 + lam * m, lam * lam * cap * cap
    r = min(((a - 1) / (4 * a * bcap)) ** (1 / (2 * gamma)),
            (a - 1) / (2 * a * (a + 1))) / 2
    alpha = a * (2 * sqrt(1 - bcap * r ** (2 * gamma)) - a * r) / (2 + a * r)
    assert alpha > 1
    assert cap / c > a ** gamma  # C250 strict scalar exclusion.
    min_ratio = float("inf")
    for i in range(401):
        b = c + (cap - c) * i / 400
        for j in range(1, 401):
            for sign in (-1, 1):
                s = sign * r * j / 400
                ratio, _, _ = radial_ratio(s, lam, m, b, gamma, "compensated")
                assert ratio * sign > 0
                min_ratio = min(min_ratio, abs(ratio))
                assert abs(ratio) + 1e-12 >= alpha
    return r, alpha, min_ratio, cap / c, a ** gamma


def check_reach_bound():
    """Unit circle specialization of the empty-normal-ball bound, all t grid."""
    lam, m, cap, radius, reach = 0.2, 3.0, 2.0, 1e-3, 1.0
    coeff = lam * lam * cap * cap / (2 * (reach - (1 + lam * m) * radius))
    minimum_margin = float("inf")
    for gamma in (0.5, 0.7, 1.0):
        assert coeff * radius ** (2 * gamma - 1) < lam * m
        for i in range(101):
            t = i / 100
            for j in range(1, 101):
                for sign in (-1, 1):
                    s = sign * radius * j / 100
                    ratio, _, _ = radial_ratio(s, t * lam, m, cap, gamma, "plain")
                    lower = 1 + t * lam * m - t * t * coeff * abs(s) ** (2 * gamma - 1)
                    minimum_margin = min(minimum_margin, abs(ratio) - lower)
                    assert abs(ratio) + 2e-12 >= lower
    return coeff, minimum_margin


def check_critical_attacks():
    # gamma=1/2: m = lambda*c^2/2, A=1.5. Inner inverse radial factor < 1.
    critical = radial_ratio(-1e-5, 1.0, 0.5, 1.0, 0.5, "plain")[0]
    assert -1 < critical < 0
    # gamma<1/2: both close sides of the uncompensated tube go outside.
    plain = [radial_ratio(sign * 1e-12, 1, 1, 1, 0.2, "plain")[0]
             for sign in (-1, 1)]
    assert all(value > 0 for value in plain)
    # A quadratic compensator still fails for gamma<1/4.
    truncated = [radial_ratio(sign * 1e-16, 1, 1, 1, 0.2, "quadratic")[0]
                 for sign in (-1, 1)]
    assert all(value > 0 for value in truncated)
    # The exact compensator has the correct sign and factor tending to A=2.
    exact = [radial_ratio(sign * 1e-12, 1, 1, 1, 0.2, "compensated")[0]
             for sign in (-1, 1)]
    assert exact[0] < -1 and exact[1] > 1
    return critical, plain, truncated, exact


if __name__ == "__main__":
    print("Maximum squared-radius identity error:", check_vector_identities())
    print("Reach empty-ball coefficient and minimum grid margin:", check_reach_bound())
    natural_r = 1e-3
    natural_alpha = 2 - (9 / (2 * (1 - 2 * natural_r))) * sqrt(natural_r)
    assert natural_alpha > 1.857 and 3 > 2 ** 0.75
    print("Uncompensated UC29 parameters:",
          {"lambda": 1, "m": 1, "c": 1, "C": 3, "gamma": 0.75,
           "R": natural_r, "alpha": natural_alpha,
           "C/c": 3, "A^gamma": 2 ** 0.75})
    r, alpha, actual, ratio, scalar = check_compensated_window()
    print("Compensated full-window parameters:",
          {"lambda": 1, "m": 1, "c": 1, "C": 3, "gamma": 0.2,
           "R": r, "alpha_lower": alpha, "grid_min_ratio": actual,
           "C/c": ratio, "A^gamma": scalar})
    critical, plain, truncated, exact = check_critical_attacks()
    print("Critical plain inner signed ratio (must be in (-1,0)):", critical)
    print("Subcritical plain two-side signed ratios (both exterior):", plain)
    print("Truncated compensation two-side signed ratios (both exterior):", truncated)
    print("Exact compensation two-side signed ratios (opposite signs):", exact)
    print("PASS: deterministic formula/window checks; analytic fiber proofs remain in the note.")
