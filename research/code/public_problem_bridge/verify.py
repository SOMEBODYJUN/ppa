"""Exact finite checks for C144's public-question bridge, not a general proof.

Run from any directory with Python 3; no third-party dependencies or randomness.
Enumerates transport-polytope vertices for specified two-source targets, all
quarter-mass laws on a four-point state space, and rational firmness pairs.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import platform


def cost(x, y):
    return sum((a - b) ** 2 for a, b in zip(x, y))


def transport_vertices(source, target):
    """Uniform two-source law to uniform 2- or 4-target law: all vertices.

    Row one has mass 1/2, columns mass 1/m. After eliminating row two,
    feasible row-one weights lie in [0,1/m] and sum to 1/2. For even m,
    every vertex selects precisely m/2 saturated columns.
    """
    m = len(target)
    assert m in (2, 4)
    plans = []
    for chosen in combinations(range(m), m // 2):
        first = [F(1, m) if j in chosen else F(0) for j in range(m)]
        plan = [first, [F(1, m) - a for a in first]]
        c = sum(plan[i][j] * cost(source[i], target[j])
                for i in range(2) for j in range(m))
        r = sum(plan[i][j] * (source[i][1] - target[j][1]) ** 2
                for i in range(2) for j in range(m))
        plans.append((c, r))
    minimum = min(c for c, _ in plans)
    residual = min(r for c, r in plans if c == minimum)
    return minimum, residual, len(plans)


def update(law):
    """State order (left,0), (left,1), (right,0), (right,1)."""
    left, right = law[0] + law[1], law[2] + law[3]
    return (left / 2, left / 2, right / 2, right / 2)


def main():
    tests = []
    for t in (F(0), F(1, 100), F(1, 16), F(1, 4), F(49, 100), F(1, 2)):
        source = [(F(1, 2) - t, F(0)), (F(1, 2) + t, F(1))]
        nearest = [(F(1, 2), F(0)), (F(1, 2), F(1))]
        limit = [(x, y) for x in (F(1, 2) - t, F(1, 2) + t)
                 for y in (F(0), F(1))]
        c0, r0, n0 = transport_vertices(source, nearest)
        c1, r1, n1 = transport_vertices(source, limit)
        # To nearest, after update, all first-coordinate costs equal t^2;
        # match second coordinates for zero added cost.
        c_after = sum(F(1, 4) * (x - F(1, 2)) ** 2 for x, _ in limit)
        assert (c0, r0, c1, r1, c_after) == (t*t, 0, 2*t*t, 0, t*t)
        # Reverse checks recover t^2 from both independent cost expressions.
        assert c1 / 2 == c0 == c_after
        tests.append(dict(t=str(t), nearest_cost_squared=str(c0),
                          limit_cost_squared=str(c1),
                          optimal_residual_squared=str(r1),
                          after_update_nearest_cost_squared=str(c_after),
                          enumerated_vertices=n0+n1))

    grid = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
    states = list(product(grid, repeat=2))
    pair_count = 0
    for x, y in product(states, repeat=2):
        # Each projection has output difference (dx,0), and displacement
        # difference (0,dy), independent of the selected bit.
        out = (x[0] - y[0]) ** 2
        residual = (x[1] - y[1]) ** 2
        assert out + residual == cost(x, y)
        pair_count += 1

    law_count = 0
    for masses in product(range(5), repeat=4):
        if sum(masses) != 4:
            continue
        law = tuple(F(a, 4) for a in masses)
        assert update(update(law)) == update(law)
        assert sum(update(law)) == 1
        law_count += 1

    result = dict(python=platform.python_version(), arithmetic="fractions.Fraction",
                  seed=None, tolerance="none; exact", status="PASS",
                  firmness_pairs=pair_count, quarter_mass_laws=law_count,
                  transport_cases=tests,
                  limits="Finite checks do not prove arbitrary-law OT optimality, "
                         "general necessity, or literature novelty; see canonical proof.")
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
