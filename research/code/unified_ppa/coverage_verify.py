#!/usr/bin/env python3
"""Finite checks for unified_ppa_coverage_frontier.md; not a theorem prover.

Python standard library, deterministic, no seed. Fractions are exact; the
explicit inverse-budget and critical-boundary checks use tolerance 1e-12.
"""

from fractions import Fraction as F
from itertools import product
import json
import math


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def omega_squared_from_u(u):
    return u + min(u * u, u)


def twice_w_at_inverse(u):
    return 2 * u + min(u * u, u)


def inverse_f(w):
    return math.sqrt(1 + 2 * float(w)) - 1 if w <= F(3, 2) else 2 * float(w) / 3


def budget(w):
    return (float(w) - inverse_f(w)) / 2


def omega(t):
    return t * math.sqrt(1 + min(t * t, 1))


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def main():
    results = {"status": "finite_checks_passed", "seed": None, "float_tolerance": 1e-12}
    pair_count = 0
    exact_slack_equivalence_count = 0
    # Compare the explicit inverse budget against the independent squared
    # condition. Cases safely away from equality are compared numerically;
    # the polynomial rearrangement is exact in every case.
    points = list(product([F(i, 2) for i in range(-3, 4)], repeat=2))
    for a, b in product(points, repeat=2):
        w = dot(a, a) + dot(b, b)
        z = tuple(x + y for x, y in zip(a, b))
        c = tuple(x - y for x, y in zip(a, b))
        u = dot(z, z)
        c2 = dot(c, c)
        assert c2 == 2 * w - u
        polynomial_slack = twice_w_at_inverse(u) - 2 * w
        reflected_slack = omega_squared_from_u(u) - c2
        assert polynomial_slack == reflected_slack
        exact_slack_equivalence_count += 1
        graph_slack = float(dot(a, b)) + budget(w)
        if abs(graph_slack) > 1e-10:
            assert (graph_slack > 0) == (reflected_slack > 0)
        assert budget(w) >= -1e-12
        assert budget(w) <= float(w) / 6 + 1e-12
        pair_count += 1
    results["budget_pair_checks"] = pair_count
    results["exact_squared_equivalence_checks"] = exact_slack_equivalence_count

    inverse_checks = 0
    for numerator in range(0, 100):
        u = F(numerator, 16)
        w = twice_w_at_inverse(u) / 2
        assert abs(inverse_f(w) - float(u)) <= 1e-12
        inverse_checks += 1
    results["explicit_inverse_checks"] = inverse_checks

    layer_checks = 0
    layer_points = list(product(range(-3, 4), [F(-1), F(0), F(1, 2)], [F(0), F(1)]))
    for p, q in product(layer_points, repeat=2):
        dk = p[0] - q[0]
        h2 = sum(((p[i] - q[i]) ** 2 for i in (1, 2)), F(0))
        u = F(dk * dk) + h2
        c2 = F(2 * dk * dk) + h2
        assert c2 <= omega_squared_from_u(u)
        # In original graph coordinates, W and inner product are rational
        # despite x_1 and lambda*v_1 containing sqrt(2).
        w = F(3, 2) * dk * dk + h2
        inner = -F(dk * dk, 4)
        assert float(inner) + budget(w) >= -1e-12
        layer_checks += 1
    results["exact_layer_graph_checks"] = layer_checks

    # Two-anchor intersection is empty at every sampled nonintegral p.
    # The analytical proof is the strict inequality omega(t)<sqrt(2)*t.
    gap_checks = []
    for i in range(1, 100):
        alpha = i / 100
        gap = math.sqrt(2) - omega(alpha) - omega(1 - alpha)
        assert gap > 0
        gap_checks.append(gap)
    midpoint_radii_sum_squared = F(5, 4)
    centres_distance_squared = F(2)
    assert midpoint_radii_sum_squared < centres_distance_squared
    results["sampled_two_ball_gaps"] = len(gap_checks)
    results["smallest_sampled_gap"] = min(gap_checks)
    results["exact_midpoint_gap_squared"] = str(centres_distance_squared - midpoint_radii_sum_squared)

    # Conditional negative-type violation uses exact rational squared kernel.
    source_points = [F(1, 2), F(0), F(1)]
    weights = [F(-1), F(1, 2), F(1, 2)]
    assert sum(weights) == 0
    cnd_value = sum(
        (weights[i] * weights[j] * omega_squared_from_u((source_points[i] - source_points[j]) ** 2)
         for i in range(3) for j in range(3)),
        F(0),
    )
    assert cnd_value == F(3, 8)
    results["exact_non_cnd_witness"] = str(cnd_value)

    # Critical product boundary: gamma=1/2, c=1, epsilon=1/4,
    # L=1/2, C0=0, m_E=M=1. The asymptotic theorem, not these finite
    # radii, establishes the claim for every sufficiently large radius.
    critical_bounds = []
    gamma, c, epsilon, ell, const, m_e, em = 0.5, 1.0, 0.25, 0.5, 0.0, 1.0, 1.0
    for radius in [16, 64, 256, 1024, 4096, 16384]:
        k_bound = (c - epsilon) * radius ** gamma - ell * em ** gamma * radius ** (gamma * gamma) - const
        e_bound = (m_e * em - ell) * radius ** gamma - ell * em ** gamma * radius ** (gamma * gamma) - const
        assert k_bound > 0 and e_bound > 0
        critical_bounds.append({"R": radius, "K_boundary_lower_bound": k_bound, "E_boundary_lower_bound": e_bound})
    results["critical_product_bounds"] = critical_bounds

    inverse_model_checks = 0
    max_inverse_error = 0.0
    for target in product([i / 8 for i in range(-16, 17)], repeat=2):
        # T_minus(k,e)=(sign(k)*sqrt(abs(k)),e), inverse k=sign(t)*t^2.
        k, e = sign(target[0]) * target[0] ** 2, target[1]
        c_value = (k - sign(k) * math.sqrt(abs(k)), 0.0)
        mapped = (k - c_value[0], e - c_value[1])
        err = math.hypot(mapped[0] - target[0], mapped[1] - target[1])
        assert err <= 1e-12
        max_inverse_error = max(max_inverse_error, err)
        inverse_model_checks += 1
    results["critical_native_inverse_checks"] = inverse_model_checks
    results["critical_native_max_error"] = max_inverse_error
    results["limits"] = [
        "Finite checks do not prove universal extension, Helly, CND positivity, or degree.",
        "Maximality and complete-fiber statements are supplied by the analytical text.",
        "No theorem status or novelty status is upgraded by this script.",
    ]
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
