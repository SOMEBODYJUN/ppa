"""Exact and 80-digit finite checks for the independent intensity PPA candidate.

Run: python3 research/code/intensity_phase_critical_ppa/verify.py
Only the Python standard library is needed. The analytic proof is in
research/candidates/intensity_phase_critical_ppa.md; this script is not a proof.
"""

from decimal import Decimal as D, getcontext
from fractions import Fraction as Q
from pathlib import Path
import json
import math
import platform

PRECISION = 80
getcontext().prec = PRECISION
TOL = D("1e-65")


def cbrt(x):
    if not x:
        return D(0)
    sign = D(1) if x > 0 else D(-1)
    a = abs(x)
    y = (a.ln() / 3).exp()
    for _ in range(12):
        z = (2 * y + a / (y * y)) / 3
        if z == y:
            break
        y = z
    return sign * y


def norm(x):
    return sum((v * v for v in x), D(0)).sqrt()


def scale(a, x):
    return tuple(a * v for v in x)


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def prox(x):
    r = norm(x)
    return (D(0), D(0)) if not r else scale(cbrt(r) / r, x)


def gradient(y):
    return scale(sum((v * v for v in y), D(0)) - 1, y)


def cayley(x):
    return sub(scale(D(2), prox(x)), x)


def loss(x):
    return (sum((v * v for v in x), D(0)) - 1) ** 2 / 4


def poly_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def winding(points):
    increments = []
    for z, w in zip(points, points[1:] + points[:1]):
        cross = z[0] * w[1] - z[1] * w[0]
        dot = z[0] * w[0] + z[1] * w[1]
        increments.append(math.atan2(cross, dot))
    return sum(increments) / (2 * math.pi)


def run():
    # Exact algebra, independent of any symbolic package.
    polynomial_identities = {}
    for alpha in [Q(1, 2), Q(1), Q(2), Q(4), Q(5)]:
        product = poly_mul([Q(-1), Q(1)], [Q(1), alpha, alpha])
        assert product == [Q(-1), 1 - alpha, Q(0), alpha]
        polynomial_identities[str(alpha)] = [str(q) for q in product]
    assert Q(3, 100) + Q(9, 10) - 1 == -Q(7, 100)
    assert Q(9, 10) * Q(19, 10) == Q(171, 100)
    assert Q(100, 171) * Q(7, 10) == Q(70, 171) < Q(1, 2)
    assert Q(7, 5) * Q(1, 16) == Q(7, 80) < Q(3, 16)
    assert Q(7, 10) * Q(1, 16) == Q(7, 160) < 1

    directions = [(D(1), D(0)), (D(0), D(1)),
                  (D(-1), D(0)), (D(3) / 5, D(4) / 5)]
    local_t = [-D(1) / 16, -D("1e-40"), -D("1e-20"),
               D(0), D("1e-20"), D("1e-40"), D(1) / 16]
    local_t += [-D(1) / 16 + D(i) / (16 * 1000) for i in range(2001)]
    extrema = {"reflection_ratio": D(0), "true_EB_ratio": D(0),
               "distance_contraction": D(0), "resolvent_relative_error": D(0)}
    for t in local_t:
        for e in directions:
            x = scale(1 + t, e)
            y = prox(x)
            p = e
            d = abs(t)
            dy = abs(norm(y) - 1)
            reflected = norm(sub(sub(scale(D(2), y), x), p))
            residual = norm(gradient(y))
            step = norm(sub(x, y))
            error = norm(sub(sub(x, y), gradient(y)))
            extrema["resolvent_relative_error"] = max(
                extrema["resolvent_relative_error"], error / max(D(1), norm(x)))
            assert error <= TOL * max(D(1), norm(x))
            assert reflected <= D(2) / 5 * d + TOL
            assert dy <= D(100) / 171 * residual + TOL
            assert dy <= d / 2 + TOL
            assert step <= D(7) / 10 * d + TOL
            assert D(7) / 5 * d < D(1) / 4 - d
            # The complete global-min prox is an ABS-positive example.
            assert loss(y) + step * step / 2 <= loss(x) + TOL
            if d > D("1e-50"):
                extrema["reflection_ratio"] = max(extrema["reflection_ratio"], reflected / d)
                extrema["distance_contraction"] = max(extrema["distance_contraction"], dy / d)
            if residual > D("1e-50"):
                extrema["true_EB_ratio"] = max(extrema["true_EB_ratio"], dy / residual)

    special_inputs = []
    for rs in ["0", "1e-120", "1e-80", "1e-20", "0.5", "0.75", "1",
               "1.25", "2", "1e6", "1e30", "1e120"]:
        r = D(rs)
        x = (r, D(0))
        y = prox(x)
        error = norm(sub(sub(x, y), gradient(y)))
        assert error <= TOL * max(D(1), r)
        special_inputs.append({"input_radius": rs, "output_radius": str(norm(y)),
                               "resolvent_relative_error": str(error / max(D(1), r))})

    near_origin = []
    for exponent in [3, 12, 30, 60, 120]:
        r = D(10) ** -exponent
        lip_ratio = cbrt(r) / r
        assert lip_ratio == r ** (D(-2) / 3) or abs(
            lip_ratio / (r ** (D(-2) / 3)) - 1) < TOL
        near_origin.append({"radius": str(r), "T_pointwise_Lipschitz_ratio": str(lip_ratio)})

    far_c = []
    for exponent in [3, 6, 12, 30, 60, 120]:
        r = D(10) ** exponent
        c = abs(2 * cbrt(r) - r)
        far_c.append({"radius": str(r), "C_over_radius": str(c / r),
                      "C_over_radius_to_half": str(c / r.sqrt())})
    assert far_c[-1]["C_over_radius"] != "0"
    assert abs(D(far_c[-1]["C_over_radius"]) - 1) < D("1e-60")

    # Finite boundary winding observations. Degree claims are proved in the text.
    windings = {}
    for radius in [.1, 15 / 16, 17 / 16, 2.0]:
        coefficient = radius - radius ** (1 / 3)
        boundary = [(coefficient * math.cos(2 * math.pi * j / 4096),
                     coefficient * math.sin(2 * math.pi * j / 4096))
                    for j in range(4096)]
        value = winding(boundary)
        assert abs(value - 1) < 1e-12
        windings[str(radius)] = value
    assert abs(windings[str(17 / 16)] - windings[str(15 / 16)]) < 1e-12

    # Exact multiple complete stationary fibers above the critical step.
    zero_fibers = []
    for alpha in [D(2), D(4), D(5)]:
        output_radius = (1 - 1 / alpha).sqrt()
        assert abs((1 - alpha + alpha * output_radius ** 2) * output_radius) < TOL
        zero_fibers.append({"alpha": str(alpha), "stationary_zero_input":
                            ["origin", "circle_radius=" + str(output_radius)],
                            "global_min_zero_input": "circle only"})
    stationary_extra_at_M = []
    for alpha in [D(4), D(5)]:
        discriminant = (1 - 4 / alpha).sqrt()
        roots = [D(1), (-1 - discriminant) / 2, (-1 + discriminant) / 2]
        for y in roots:
            assert abs(alpha * y ** 3 + (1 - alpha) * y - 1) < TOL
        stationary_extra_at_M.append({"alpha": str(alpha), "signed_outputs": [str(y) for y in roots]})

    # Scalar radius iteration and exact telescoping length, including far inputs.
    orbit_checks = []
    for initial in [D("1e-60"), D("0.8"), D("1.2"), D("1e60")]:
        r, length = initial, D(0)
        for _ in range(200):
            nxt = cbrt(r)
            length += abs(nxt - r)
            r = nxt
        assert abs(length + abs(r - 1) - abs(initial - 1)) < TOL * max(D(1), initial)
        orbit_checks.append({"initial_radius": str(initial), "radius_after_200": str(r),
                             "finite_length_plus_exact_remaining": str(length + abs(r - 1))})

    result = {
        "python": platform.python_version(), "arithmetic": "Fraction exact algebra; Decimal 80 significant digits; binary64 boundary winding",
        "decimal_precision": PRECISION, "decimal_absolute_relative_tolerance": str(TOL),
        "symbolic_engine": "SymPy/mpmath unavailable; exact Fraction polynomial multiplication replaces symbolic factor checks",
        "certificate": {"b": "1", "lambda": "1", "R": "1/16", "gamma": "1", "L": "2/5",
                        "bar_t": "1", "psi": "100 q / 171", "kappa": "1/2",
                        "length": "7 d / 5", "compatibility_ratio": "70/171"},
        "exact_factor_checks": polynomial_identities,
        "local_inputs_with_directions": len(local_t) * len(directions),
        "sampled_extrema": {k: str(v) for k, v in extrema.items()},
        "zero_critical_far_inputs": special_inputs, "origin_non_Lipschitz": near_origin,
        "far_reflection_obstruction": far_c, "boundary_winding_observations": windings,
        "zero_input_above_critical": zero_fibers, "M_input_at_alpha4_and5": stationary_extra_at_M,
        "orbit_checks": orbit_checks,
        "scope": "Finite checks only. Full coverage, true EB, compatibility, uniform strict budget and index claims require the analytic proof. No global reflected sublinear Holder certificate is claimed."
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "passed", "results": str(path),
                      "local_inputs_with_directions": result["local_inputs_with_directions"],
                      "decimal_precision": PRECISION}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
