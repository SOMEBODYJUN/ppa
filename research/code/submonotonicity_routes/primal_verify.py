"""Finite checks accompanying primal_structural_review.md (no universal claim).

Run: python3 research/code/submonotonicity_routes/primal_verify.py
Python standard library only. Seed 20261014; exact rationals for polynomial
identities, IEEE-754 floats for inverse and orbit checks.
"""
from fractions import Fraction as Q
from math import copysign, hypot, sqrt
from random import Random


def root3(x):
    return copysign(abs(x) ** (1 / 3), x) if x else 0.0


def h(x):
    return copysign(sqrt(abs(x)), x) if x else 0.0


def quartic():
    grid = [Q(j, 10) for j in range(-20, 21)]
    for x in grid:
        for y in grid:
            d = x - y
            assert d * (x**3 - y**3) - d**4 / 4 == 3 * d**2 * (x + y) ** 2 / 4
    rng = Random(20261014)
    max_inverse_error = 0.0
    for _ in range(10000):
        z = rng.uniform(-10, 10)
        x = root3(z)
        max_inverse_error = max(max_inverse_error, abs(x**3 - z))
        assert abs(x**3 - z) < 2e-14
    print("quartic identity: 1681 exact pairs; inverse max error", max_inverse_error)
    for t in [1e-1, 1e-2, 1e-3, 1e-4]:
        z, r = t**3, 2 * t - t**3
        print("quartic bad LT ratio", t, (t**2 - t**4) / z**2, "R/z", r / z)
    for z in [1e-6, .125, 2.0, -.125, 0.0]:
        x, length = z, 0.0
        for _ in range(15):
            y = root3(x)
            length += abs(y - x)
            x = y
        target = copysign(1., z) if z else 0.
        assert abs(length - abs(x - z)) < 1e-14
        print("quartic PPA", z, "x15", x, "length15", length, "limit", target)


def particle():
    rng = Random(20261014)
    for gamma in [15., -.5]:
        max_error = 0.0
        min_gap = float("inf")
        for _ in range(10000):
            a, b = rng.uniform(-2, 2), rng.uniform(-2, 2)
            p = b / (1 + gamma)
            x = a + h(p)
            max_error = max(max_error, hypot(x - h(p) - a, (1 + gamma) * p - b))
            assert hypot(x - h(p) - a, (1 + gamma) * p - b) < 2e-15
            # Complete graph primal defect, arbitrary graph-point pair.
            dx, p0, p1 = rng.uniform(-2, 2), rng.uniform(-2, 2), rng.uniform(-2, 2)
            dp = p1 - p0
            s = hypot(dx, dp)
            inner = -dx * (h(p1) - h(p0)) + gamma * dp * dp
            gap = inner + sqrt(2) * s ** 1.5 + max(0., -gamma) * s * s
            min_gap = min(min_gap, gap)
            assert gap > -1e-12
        print("particle gamma", gamma, "inverse error", max_error, "min gauge slack", min_gap)
    for t in [1e-2, 1e-4, 1e-6]:
        print("stable particle M inner", t, 17*t*t-t**1.5)
    p0 = .01
    print("unstable complete PPA p0,p10:", p0, 2**10 * p0)


def lt_not_dg():
    delta = Q(1, 10)
    tau = delta / (1 - delta)**2
    points = []
    for k in range(-10, 11):
        x = Q(k, 100)
        vals = [Q(1)] if x < 0 else ([Q(-1)] if x > 0 else [Q(-1), Q(1)])
        points.extend((x, u) for u in vals)
    for x, u in points:
        for y, v in points:
            a, b = x-y, u-v
            assert a*b >= -tau*(a+b)**2
    print("LT jump example exact pair checks", len(points)**2, "tau", tau)
    for n in [100, 1000, 10000]:
        t = Q(1,n)
        assert ((2*t)*(-2))/(2*t) == -2
    print("DG normalized jump defect = -2 for all tested t")


if __name__ == "__main__":
    quartic()
    particle()
    lt_not_dg()
    print("Finite checks passed; forall claims require the report's analytic proofs.")
