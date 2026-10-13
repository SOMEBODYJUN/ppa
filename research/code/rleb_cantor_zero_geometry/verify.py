"""Exact rational checks of an infinite-Cantor complete PPA model.

Run: python3 research/code/rleb_cantor_zero_geometry/verify.py

No finite Cantor approximation is used. Rational membership is decided by
exact normalized ternary state repetition; a detected middle third supplies
the exact component endpoints and hence the exact distance.
"""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json


ZERO, ONE = Q(0), Q(1)
F_ONE = Q(1, 56)


def cantor_classify(x: Q) -> dict:
    """Decide rational membership in the actual infinite ternary Cantor set."""
    x = Q(x)
    if x < 0:
        return {"kind": "left", "steps": 0}
    if x > 1:
        return {"kind": "right", "steps": 0}
    normalized, left, width = x, ZERO, ONE
    seen = set()
    steps = 0
    while True:
        if normalized in (ZERO, ONE, Q(1, 3), Q(2, 3)):
            return {"kind": "cantor", "steps": steps, "reason": "endpoint"}
        if normalized in seen:
            return {"kind": "cantor", "steps": steps, "reason": "periodic"}
        seen.add(normalized)
        if Q(1, 3) < normalized < Q(2, 3):
            return {
                "kind": "gap", "a": left + width / 3,
                "b": left + 2 * width / 3, "steps": steps,
            }
        if normalized < Q(1, 3):
            normalized *= 3
            width /= 3
        else:
            left += 2 * width / 3
            normalized = 3 * normalized - 2
            width /= 3
        steps += 1


def distance(x: Q) -> Q:
    x = Q(x)
    info = cantor_classify(x)
    if info["kind"] == "left":
        return -x
    if info["kind"] == "right":
        return x - 1
    if info["kind"] == "cantor":
        return ZERO
    return min(x - info["a"], info["b"] - x)


def F(y: Q) -> Q:
    y = Q(y)
    if y < 0:
        return y
    if y > 1:
        return y - 1
    return distance(y) / 2


def H(y: Q) -> Q:
    return Q(y) + F(y)


def T(x: Q) -> Q:
    x = Q(x)
    info = cantor_classify(x)
    if info["kind"] == "left":
        return x / 2
    if info["kind"] == "right":
        return (x + 1) / 2
    if info["kind"] == "cantor":
        return x
    a, b = info["a"], info["b"]
    threshold = a + 3 * (b - a) / 4
    if x <= threshold:
        return a + 2 * (x - a) / 3
    return b + 2 * (x - b)


def reflection(x: Q) -> Q:
    return 2 * T(x) - Q(x)


def limit_map(x: Q) -> Q:
    x = Q(x)
    info = cantor_classify(x)
    if info["kind"] == "left":
        return ZERO
    if info["kind"] == "right":
        return ONE
    if info["kind"] == "cantor":
        return x
    return info["a"]


def exact_total_length(x: Q) -> Q:
    return abs(Q(x) - limit_map(x))


def potential(x: Q) -> Q:
    """Exact integral int_0^x F, including rational periodic Cantor points.

    Inside [0,1], self similarity gives f(t)=f(3t)/9 on the left third
    and f(t)=8*f(1)/9+f(3t-2)/9 on the right. Periodic normalized
    states therefore close by an exact affine equation, not truncation.
    """
    x = Q(x)
    if x < 0:
        return x * x / 2
    if x > 1:
        return F_ONE + (x - 1) ** 2 / 2
    normalized, offset, scale = x, ZERO, ONE
    seen = {}
    while True:
        if normalized == 0:
            return offset
        if normalized == 1:
            return offset + scale * F_ONE
        if normalized in seen:
            old_offset, old_scale = seen[normalized]
            value_at_cycle = (offset - old_offset) / (old_scale - scale)
            return offset + scale * value_at_cycle
        seen[normalized] = (offset, scale)
        if Q(1, 3) <= normalized <= Q(1, 2):
            middle = F_ONE / 9 + (normalized - Q(1, 3)) ** 2 / 4
            return offset + scale * middle
        if Q(1, 2) < normalized <= Q(2, 3):
            middle = 8 * F_ONE / 9 - (Q(2, 3) - normalized) ** 2 / 4
            return offset + scale * middle
        if normalized < Q(1, 3):
            normalized *= 3
            scale /= 9
        else:
            offset += scale * 8 * F_ONE / 9
            scale /= 9
            normalized = 3 * normalized - 2


def all_gaps(max_depth: int):
    for depth in range(1, max_depth + 1):
        for digits in product((0, 2), repeat=depth - 1):
            left = sum((Q(d, 3 ** i) for i, d in enumerate(digits, 1)), ZERO)
            a = left + Q(1, 3 ** depth)
            yield depth, a, a + Q(1, 3 ** depth)


def stringify(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): stringify(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [stringify(v) for v in value]
    return value


def main():
    count = {"point": 0, "gap": 0, "pair": 0, "repelling": 0,
             "orbit": 0, "prox_comparison": 0, "quartic": 0}
    samples = {Q(-100), Q(-2), Q(-1), Q(-1, 100), ZERO, ONE,
               Q(1, 4), Q(3, 4), Q(1, 13), Q(12, 13), Q(1, 10),
               Q(9, 10), Q(1, 7), Q(1, 2), Q(2), Q(100), Q(101, 100)}
    pairs = set(samples)
    gap_list = list(all_gaps(6))
    offsets = [Q(0), Q(1, 1000), Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 3),
               Q(1, 2), Q(2, 3), Q(3, 4), Q(7, 8), Q(15, 16),
               Q(999, 1000), Q(1)]
    for depth, a, b in gap_list:
        length = b - a
        assert cantor_classify(a)["kind"] == "cantor"
        assert cantor_classify(b)["kind"] == "cantor"
        for offset in offsets:
            x = a + offset * length
            samples.add(x)
            if 0 < offset < 1:
                info = cantor_classify(x)
                assert (info["kind"], info["a"], info["b"]) == ("gap", a, b)
            if offset in (Q(0), Q(1, 2), Q(3, 4), Q(1)):
                pairs.add(x)
        midpoint, threshold = a + length / 2, a + 3 * length / 4
        assert H(midpoint) == threshold
        assert T(threshold) == midpoint
        assert a + 2 * (threshold - a) / 3 == b + 2 * (threshold - b)
        count["gap"] += 1
        for power in (3, 8, 20, 60):
            epsilon = length / 2 ** power
            x, y = b - epsilon, b - 2 * epsilon
            assert T(x) == y
            assert distance(x) == epsilon
            assert distance(y) == 2 * epsilon
            assert abs(F(y)) == epsilon == abs(x - y)
            assert exact_total_length(x) == length - epsilon
            assert limit_map(x) == a and limit_map(b) == b
            count["repelling"] += 1

    for x in sorted(samples):
        y = T(x)
        assert H(y) == x
        assert T(H(x)) == x
        assert distance(x) <= 2 * abs(F(x))
        assert distance(y) <= 2 * abs(F(y))
        assert ZERO <= reflection(x) <= ONE
        assert (F(x) == 0) == (distance(x) == 0)
        assert (T(x) == x) == (distance(x) == 0)
        assert potential(1 - x) == F_ONE - potential(x) if 0 <= x <= 1 else True
        count["point"] += 1

    records = {x: (F(x), H(x), T(x), reflection(x)) for x in sorted(pairs)}
    for x, z in combinations(sorted(pairs), 2):
        delta = z - x
        fx, hx, tx, rx = records[x]
        fz, hz, tz, rz = records[z]
        assert abs(fz - fx) <= delta
        assert delta / 2 <= hz - hx <= 2 * delta
        assert fx + x / 2 <= fz + z / 2
        assert delta / 2 <= tz - tx <= 2 * delta
        assert ZERO <= rz - rx <= min(3 * delta, ONE)
        # Squared form of the gamma=1/2 bound, checked exactly.
        assert (rz - rx) ** 2 <= 3 * delta
        count["pair"] += 1

    # The exact geometric tail checks the infinite gap-area sum.
    partial = sum((Q(2 ** (n - 1), 8 * 9 ** n) for n in range(1, 21)), ZERO)
    tail = Q(2 ** 20, 8 * 9 ** 21) / (1 - Q(2, 9))
    assert partial + tail == F_ONE
    assert potential(Q(1, 4)) == Q(1, 560)
    assert potential(Q(3, 4)) == Q(9, 560)
    assert potential(Q(1, 2)) == F_ONE / 2
    periodic = {str(x): cantor_classify(x) for x in (Q(1, 4), Q(3, 4),
                 Q(1, 13), Q(12, 13), Q(1, 10), Q(9, 10))}
    assert all(info["kind"] == "cantor" and info["reason"] == "periodic"
               for info in periodic.values())

    # Prefix telescoping and exact terminal length apply to every orbit case.
    orbit_initials = [Q(-100), Q(-2), Q(0), Q(1, 4), Q(1), Q(2), Q(100)]
    orbit_initials += [a + Q(999, 1000) * (b - a) for _, a, b in gap_list]
    for initial in orbit_initials:
        current, traveled, terminal = initial, ZERO, limit_map(initial)
        for _ in range(90):
            following = T(current)
            if initial < 0:
                assert current <= following <= terminal
            else:
                assert terminal <= following <= current
            traveled += abs(following - current)
            assert traveled + exact_total_length(following) == exact_total_length(initial)
            assert limit_map(following) == terminal
            current = following
            count["orbit"] += 1

    # Exact finite minimization comparisons supplement, not replace, strong
    # convexity of f(y)+|y-x|^2/2 proved in the accompanying text.
    trial_points = sorted(pairs)
    for x in trial_points[::max(1, len(trial_points) // 40)]:
        minimizer = T(x)
        optimum = potential(minimizer) + (minimizer - x) ** 2 / 2
        for y in trial_points:
            assert potential(y) + (y - x) ** 2 / 2 >= optimum
            count["prox_comparison"] += 1

    assert T(Q(-2)) == -1 and T(Q(2)) == Q(3, 2)
    assert Q(-2) < T(Q(-2)) and T(Q(2)) < Q(2)

    # Optional same-operator/different-target quartic comparison.
    # Inputs x=y^3 certify T(x)=y exactly, without numerical cube roots.
    quartic = {"local_L": Q(1, 2), "local_EB_coefficient": Q(100, 171),
               "local_kappa": Q(1, 2), "local_R": Q(1, 4),
               "direct_compatibility_coefficient": Q(25, 57)}
    assert quartic["direct_compatibility_coefficient"] < quartic["local_kappa"]
    for denominator in (10, 100, 1000, 10 ** 10):
        y = Q(1, denominator)
        x, fy = y ** 3, y ** 3 - y
        assert x - y == fy
        assert y > x and y / x == denominator ** 2
        count["quartic"] += 1
    for sign in (-1, 1):
        for y0 in [Q(9, 10), Q(19, 20), ONE, Q(21, 20), Q(11, 10)]:
            y = sign * y0
            x = y ** 3
            if abs(x - sign) <= Q(1, 4):
                assert abs(y - sign) <= Q(100, 171) * abs(y ** 3 - y)
                assert abs(2 / (3 * y ** 2) - 1) <= Q(1, 2)
                count["quartic"] += 1

    report = {
        "status": "all exact rational assertions passed",
        "model": "actual infinite Cantor set; lambda=1; v=Id; complete F and T",
        "counts": count,
        "cantor_gap_depths": [1, 6],
        "rational_membership": "exact normalized ternary-state cycle detection",
        "periodic_cantor_examples": periodic,
        "infinite_gap_integral": {
            "partial_levels": 20, "partial": partial, "exact_tail": tail,
            "sum": F_ONE,
        },
        "global_constants": {"F_Lipschitz": ONE, "weak_convexity": Q(1, 2),
                             "H_strong_monotonicity": Q(1, 2),
                             "H_Lipschitz": Q(2), "reflection_Lipschitz": Q(3),
                             "reflection_oscillation": ONE,
                             "true_EB_coefficient": Q(2)},
        "repelling_identity": "d(T(b-epsilon),C)=2epsilon; length=(b-a)-epsilon",
        "quartic_optional": quartic,
        "scope": "Finite exact checks support formulas; universal proofs are in the markdown.",
    }
    destination = Path(__file__).with_name("results.json")
    destination.write_text(json.dumps(stringify(report), ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(stringify({"status": report["status"], "counts": count,
                               "json": str(destination)}), ensure_ascii=False))


if __name__ == "__main__":
    main()
