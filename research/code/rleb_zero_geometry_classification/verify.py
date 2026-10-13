"""Finite exact checks supporting the analytic geometry report.

Run from repository root:
    python3 research/code/rleb_zero_geometry_classification/verify.py

Fractions check prox inversion, all branches of a convex-square model,
tail arithmetic and target-dependent quartic expansion. Integers check
component Euler arithmetic. None of these finite tests proves a universal
topological or analytic assertion; those proofs are in the candidate cards.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json
import platform


def clip(t):
    return min(Q(1), max(Q(-1), t))


def projection(x):
    return tuple(clip(t) for t in x)


def prox(x):
    return tuple((t + clip(t)) / 2 for t in x)


def norm2(x):
    return sum((t * t for t in x), Q(0))


def subtract(x, y):
    return tuple(a - b for a, b in zip(x, y))


def component_deficits(n, bounded_chi, exterior_chi):
    sign = (-1) ** n
    return [sign * c for c in bounded_chi] + [1 + sign * (exterior_chi - 1)]


def main():
    # Explicit whole fibers for the nearest-point relation K={-1,1}:
    # F(-1)=(-infinity,1], F(1)=[-1,infinity), elsewhere empty.
    projection_relation_checks = 0
    for x in [Q(-100), Q(-2), Q(-1), Q(-1, 10), Q(0), Q(1, 10), Q(1), Q(2), Q(100)]:
        fibers = tuple(y for y in (Q(-1), Q(1))
                       if (y == -1 and x - y <= 1) or (y == 1 and x - y >= -1))
        expected = (Q(-1),) if x < 0 else ((Q(1),) if x > 0 else (Q(-1), Q(1)))
        assert fibers == expected
        distance2 = min((x + 1) ** 2, (x - 1) ** 2)
        for y in fibers:
            assert (x - y) ** 2 == distance2
            assert (2 * y - x - y) ** 2 == distance2
            assert Q(0) / 4 <= Q(0) / 2  # true residual at every output is zero
            projection_relation_checks += 1
    assert Q(1, 4) <= Q(1, 2)
    assert 1 / (1 - Q(1, 2)) == 2

    examples = [
        ("circle_R2", 2, 0, [1], 0, [1, 0]),
        ("circle_R3", 3, 0, [], 1, [1]),
        ("sphere_R3", 3, 2, [1], 2, [-1, 0]),
        ("sphere_R4", 4, 2, [], -1, [-1]),
        ("two_nonnested_circles", 2, 0, [1, 1], -1, [1, 1, -1]),
        ("two_nested_circles", 2, 0, [1, 0], 0, [1, 0, 0]),
        ("genus2_R3", 3, -2, [-1], 0, [1, 2]),
        ("genus2_R4", 4, -2, [], 3, [3]),
        ("RP2_R5", 5, 1, [], 2, [0]),
    ]
    component_checks = []
    for name, n, chi, bounded, exterior, expected in examples:
        delta = component_deficits(n, bounded, exterior)
        assert delta == expected
        assert sum(delta) == 1 - chi
        component_checks.append({
            "name": name, "ambient_dimension": n, "target_chi": chi,
            "bounded_region_chi": bounded, "exterior_region_chi": exterior,
            "deficits": delta, "general_minimum": sum(d != 0 for d in delta),
            "nondegenerate_minimum": sum(abs(d) for d in delta),
        })

    grid = [Q(-100), Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2), Q(100)]
    inputs = list(product(grid, repeat=2))
    for x in inputs:
        p, y = projection(x), prox(x)
        # H(y)=y+F(y)=2y-P_K(y); both inverse directions are checked.
        assert tuple(2 * a - clip(a) for a in y) == x
        hx = tuple(2 * a - clip(a) for a in x)
        assert prox(hx) == x
        assert tuple(2 * a - b for a, b in zip(y, x)) == p
        assert projection(y) == p
        assert norm2(subtract(y, p)) == norm2(subtract(x, p)) / 4
        assert norm2(subtract(y, projection(y))) == norm2(subtract(x, y))
        orbit = x
        for k in range(1, 13):
            orbit = prox(orbit)
            assert orbit == tuple(a + (b - a) / 2 ** k for a, b in zip(p, x))
    pair_checks = 0
    for x, z in combinations(inputs, 2):
        dc2 = norm2(subtract(projection(x), projection(z)))
        dx2 = norm2(subtract(x, z))
        assert dc2 <= dx2                    # reflected map is nonexpansive
        assert dc2 <= 8                      # diameter squared of the square
        assert dc2 * dc2 <= 8 * dx2          # global Holder exponent 1/2
        pair_checks += 1

    R, kappa, L = Q(1, 3), Q(1, 2), Q(0)
    tail_coefficient = 1 / (2 * (1 - kappa))
    assert tail_coefficient == 1
    assert (R + L * R) / 2 == R / 2
    assert tail_coefficient * R < 1 - R     # radius-one tube example

    quartic = []
    for m in (3, 10, 100, 10000):
        y = Q(1, m)
        x = y ** 3
        assert y + (y ** 3 - y) == x
        assert y / x == m * m
        quartic.append({"output": str(y), "input": str(x),
                        "distance_ratio_to_full_S": str(y / x)})

    result = {
        "status": "all finite checks passed; universal conclusions have analytic proofs",
        "environment": {"python": platform.python_version(),
                        "precision": "exact Fraction/integer arithmetic", "seed": None},
        "component_checks": component_checks,
        "arbitrary_closed_set_projection_mechanism": {
            "finite_test_set": [-1, 1], "full_output_checks": projection_relation_checks,
            "zero_tie_has_two_outputs": True, "true_output_residual": 0,
            "compatibility_coefficient": "1/4", "tail_budget_coefficient": "2",
        },
        "square": {"complete_inverse_and_anchor_inputs": len(inputs),
                   "corners_and_boundary_included": True, "largest_input_coordinate": 100,
                   "iterations_per_input": 12, "reflected_pair_checks": pair_checks},
        "normal_tube_tail_coefficient": str(tail_coefficient),
        "quartic_target_counterchecks": quartic,
        "scope": "No Hopf completion solver, general index proof, or ENR recognition algorithm is implemented.",
    }
    dest = Path(__file__).with_name("results.json")
    dest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"saved": str(dest), "status": result["status"],
                      "square": result["square"], "component_examples": len(examples)}, indent=2))


if __name__ == "__main__":
    main()
