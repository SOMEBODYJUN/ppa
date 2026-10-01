"""Exact arithmetic for the lazy four-state strictness example.

The exhaustive domain is justified in Section 10 of
MARKOV_FINITE_STATE_EXACT_ZERO_LINEAR_EB.md: the monotone-coupling
polyhedral subdivision has precisely the probability-grid vertices z/4,
where z has four nonnegative integer entries summing to four.
No numerical optimizer or floating-point tolerance is used.
"""

from fractions import Fraction
from itertools import product


POINTS = (0, 1, 3, 4)
DISPLACEMENTS = (-1, -2, -1, 4)
HALF = Fraction(1, 2)


def costs_at_grid_vertex(counts, update_probability=HALF):
    """Return C-cost, lazy R-cost and unique monotone coupling."""
    source = list(counts)
    target = [1, 1, 1, 1]
    i = j = 0
    cost = Fraction(0)
    residual = Fraction(0)
    coupling = []
    while i < 4 and j < 4:
        if source[i] == 0:
            i += 1
            continue
        if target[j] == 0:
            j += 1
            continue
        units = min(source[i], target[j])
        source[i] -= units
        target[j] -= units
        mass = Fraction(units, 4)
        cost += mass * (POINTS[i] - POINTS[j]) ** 2
        residual += mass * update_probability * (DISPLACEMENTS[i] - DISPLACEMENTS[j]) ** 2
        coupling.append((i, j, mass))
    assert not any(source) and not any(target)
    return cost, residual, coupling


def main():
    # Strict Monge inequality guarantees that OT plans cannot cross.
    for i, k, j, ell in product(range(4), repeat=4):
        if i < k and j < ell:
            crossing = (POINTS[i] - POINTS[ell]) ** 2 + (POINTS[k] - POINTS[j]) ** 2
            ordered = (POINTS[i] - POINTS[j]) ** 2 + (POINTS[k] - POINTS[ell]) ** 2
            assert crossing - ordered == 2 * (POINTS[k] - POINTS[i]) * (POINTS[ell] - POINTS[j]) > 0

    vertices = [z for z in product(range(5), repeat=4) if sum(z) == 4]
    assert len(vertices) == 35
    best = Fraction(0)
    maximizers = []
    zero_vertices = []
    for z in vertices:
        cost, residual, coupling = costs_at_grid_vertex(z)
        if residual == 0:
            assert cost == 0 and z == (1, 1, 1, 1)
            zero_vertices.append(z)
            continue
        ratio = cost / residual
        if ratio > best:
            best = ratio
            maximizers = [(z, cost, residual, coupling)]
        elif ratio == best:
            maximizers.append((z, cost, residual, coupling))
    assert zero_vertices == [(1, 1, 1, 1)]
    assert best == 26
    assert len(maximizers) == 1
    assert maximizers[0][:3] == ((0, 0, 3, 1), Fraction(13, 4), Fraction(1, 8))

    # Dropping input-OT optimality gives a spurious zero at this law.
    relaxed_witness = (2, 1, 0, 1)
    cost, residual, _ = costs_at_grid_vertex(relaxed_witness)
    assert cost == Fraction(5, 4) and residual == Fraction(1, 4)
    assert DISPLACEMENTS[0] == DISPLACEMENTS[2]
    # Relaxed plan: 0->0, 0->3, 1->1, 4->4, each with mass 1/4.
    relaxed_plan = ((0, 0), (0, 2), (1, 1), (3, 3))
    relaxed_residual = sum(
        Fraction(1, 4) * HALF * (DISPLACEMENTS[i] - DISPLACEMENTS[j]) ** 2
        for i, j in relaxed_plan
    )
    relaxed_cost = sum(
        Fraction(1, 4) * (POINTS[i] - POINTS[j]) ** 2
        for i, j in relaxed_plan
    )
    assert relaxed_residual == 0 and relaxed_cost == Fraction(9, 4)
    assert relaxed_cost > cost

    # A small update probability meets the source's epsilon < 1 regime.
    small_probability = Fraction(1, 100)
    small_ratios = []
    for z in vertices:
        small_cost, small_residual, _ = costs_at_grid_vertex(z, small_probability)
        if small_residual:
            small_ratios.append(small_cost / small_residual)
        else:
            assert z == (1, 1, 1, 1)
    assert max(small_ratios) == 13 / small_probability == 1300
    images = (1, 3, 4, 0)
    violations = []
    for i, j in product(range(4), repeat=2):
        if i != j:
            input_cost = (POINTS[i] - POINTS[j]) ** 2
            update_cost = (images[i] - images[j]) ** 2
            displacement_cost = (DISPLACEMENTS[i] - DISPLACEMENTS[j]) ** 2
            violations.append(small_probability * (Fraction(update_cost + displacement_cost, input_cost) - 1))
    assert max(violations) == 40 * small_probability == Fraction(2, 5)
    local_cost, local_residual, _ = costs_at_grid_vertex((1, 0, 2, 1), small_probability)
    assert local_cost == 1 and local_residual == Fraction(1, 400)

    print("PASS: all 35 polyhedral subdivision vertices checked exactly")
    print("PASS: sole zero-residual vertex is uniform stationary law")
    print(f"Sharp squared W2 error-bound constant: {best}")
    print(f"Unique maximizing count vector z (law z/4): {maximizers[0][0]}")
    print(f"At maximizer: distance squared={maximizers[0][1]}, discrepancy squared={maximizers[0][2]}")
    print("PASS: relaxed zero-cost coupling is not input-OT optimal")
    print("PASS: p=1/100 has sharp squared constant 1300 and balanced violation 2/5 < 1")
    print("PASS: local adjacent-mass witness has squared ratio 4/p")


if __name__ == "__main__":
    main()
