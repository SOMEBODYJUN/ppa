#!/usr/bin/env python3
"""Finite arithmetic checks for C222; the canonical proof carries the quantifiers.

Run: python3 research/code/gppa_novelty/structure_priority_check.py
Standard library only. Deterministic seed 222031004, binary64 tolerances below.
"""

from fractions import Fraction
from math import dist, hypot, sqrt
from random import Random
import json


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def norm(a):
    return hypot(*a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def scalar_checks():
    count = 0
    for i in range(10001):
        t = Fraction(i, 10000)
        assert min(3 * t, 2 * (1 - t * t)) <= 6 * t * (1 - t)
        count += 1
    worst_slack = float("inf")
    for gamma in (.001, .01, .1, .25, .5, .75, .9, .99, .999):
        alpha = (1 - gamma) / 6
        ts = [0.0, 1.0] + [i / 10000 for i in range(1, 10000)]
        ts += [10.0 ** -i for i in range(1, 301)]
        for t in ts:
            slack = t ** gamma - t
            assert slack + 2e-14 >= (1 - gamma) * t * (1 - t)
            excess = alpha * min(3 * t, 2 * (1 - t * t))
            assert t + excess <= t ** gamma + 2e-14
            worst_slack = min(worst_slack, t ** gamma - t - excess)
            count += 1
    return {"scalar_checks": count, "minimum_numeric_slack": worst_slack}


def square_checks():
    rng = Random(222031004)
    K = ((-.5, -.5), (-.5, .5), (.5, -.5), (.5, .5))
    k0 = K[0]
    D = sqrt(2)
    gamma, eta, lam = .5, .1, 1.7
    alpha = min((1 - gamma) / 6, eta / 3)

    def projection(a):
        return tuple(max(-.5, min(.5, x)) for x in a)

    def e(y):
        d2 = min(dist(y, k) ** 2 for k in K)
        return scale(-alpha * d2 / (D * D), sub(y, k0))

    def r(a):
        p = projection(a)
        return add(p, e(p))

    def g(a):
        return scale(.5, add(a, r(a)))

    c, M = (1 - eta) / 2, (2 + eta) / 2
    step = c / (M * M)
    contraction = sqrt(1 - 2 * step * c + step * step * M * M)

    def f(u):
        a = u
        for _ in range(600):
            b = sub(a, scale(step, sub(g(a), u)))
            if dist(a, b) / (1 - contraction) < 2e-12:
                a = b
                break
            a = b
        else:
            raise AssertionError("G inversion did not meet its error bound")
        assert dist(g(a), u) < 5e-12
        return scale(1 / lam, sub(a, u)), a

    points = list(K) + [(0., 0.), (.1, -.2), (.5, 0.)]
    points += [(rng.uniform(-3, 3), rng.uniform(-3, 3)) for _ in range(160)]
    count = 0
    max_approximation = 0.
    values = [f(x) for x in points]
    for u, (fu, a) in zip(points, values):
        assert dist(add(u, scale(lam, fu)), a) < 1e-11
        assert dist(sub(u, scale(lam, fu)), r(a)) < 1e-11
        approximation = dist(fu, scale(1 / lam, sub(u, projection(u))))
        assert approximation <= alpha * D / lam + 1e-11
        max_approximation = max(max_approximation, approximation)
        count += 3
    for k in K:
        assert norm(f(k)[0]) < 1e-11
    assert norm(f((0., 0.))[0]) > 1e-4
    for i, u in enumerate(points):
        for j in range(i + 1, len(points)):
            v = points[j]
            fu, a = values[i]
            fv, b = values[j]
            assert dist(r(u), r(v)) <= D ** (1 - gamma) * dist(u, v) ** gamma + 1e-12
            assert dist(fu, fv) <= (1 + eta) / (lam * (1 - eta)) * dist(u, v) + 1e-10
            assert dot(sub(g(u), g(v)), sub(u, v)) >= c * dist(u, v) ** 2 - 1e-12
            assert dist(r(a), r(b)) <= D ** (1 - gamma) * dist(a, b) ** gamma + 1e-12
            count += 4
    return {
        "square_checks": count,
        "seed": 222031004,
        "parameters": {"gamma": gamma, "eta": eta, "lambda": lam, "alpha": alpha},
        "points": len(points),
        "max_observed_uniform_error": max_approximation,
        "proved_construction_error_bound": alpha * D / lam,
        "inverse_iteration_contraction_bound": contraction,
    }


if __name__ == "__main__":
    print(json.dumps({"status": "PASS", **scalar_checks(), **square_checks()}, indent=2))
