"""Finite checks for the proposed sections; analytic proofs remain authoritative."""
from pathlib import Path
from fractions import Fraction as Q
import json
import math

BASE = Path(__file__).resolve().parent
checks = 0
for aa in range(-5, 6):
    for bb in range(-5, 6):
        for ll in (Q(1, 4), Q(1), Q(3)):
            for cc in (Q(0), Q(1, 2), Q(1), Q(2), Q(5)):
                a, b = Q(aa), Q(bb)
                direct = (a - ll*b)**2 <= cc**2*(a + ll*b)**2
                mu = (1 - cc**2)/(2*ll*(1 + cc**2))
                balanced = a*b >= mu*a*a + ll*ll*mu*b*b
                assert direct == balanced
                if cc >= 1:
                    tau = (cc**2 - 1)/4
                    assert direct == (ll*a*b >= -tau*(a + ll*b)**2)
                checks += 1

# Exact junction, minimum, and index calculations.
r = Q(3, 4)
assert -r*r/6 == r*r/2 - r + Q(3, 8)
assert -r/3 == r - 1
assert Q(1, 2) - 1 + Q(3, 8) == -Q(1, 8)
assert (1 - Q(3, 2))**2 == Q(1, 4)

rows = []
for L in (0., .5, 1., 2., 5.):
    for ratio in (.05, .5, 1., 2., 10.):
        rho = math.sqrt((1 + L*L)/(2*(1 + ratio*ratio)))
        assert abs(2*(1 + ratio*ratio)*rho*rho - (1 + L*L)) < 1e-11
        assert (rho < 1) == (L*L < 1 + 2*ratio*ratio)
        rows.append(dict(L=L, lambda_over_K=ratio, rho_E=rho,
                         direct_gate=(1 + L)/(2*ratio), energy_contracts=rho < 1))

def norm(v):
    return math.hypot(*v)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def scale(k, v):
    return [k*x for x in v]

def add(a, b):
    return [x+y for x, y in zip(a, b)]

def sub(a, b):
    return [x-y for x, y in zip(a, b)]

def f(y):
    r = norm(y)
    return -r*r/6 if r <= .75 else r*r/2 - r + 3/8

def grad(y):
    r = norm(y)
    return scale(-1/3, y) if r <= .75 else scale(1 - 1/r, y)

def T(x):
    r = norm(x)
    return scale(1.5, x) if r <= .5 else scale((1 + 1/r)/2, x)

def point(r, angle):
    return [r*math.cos(angle), r*math.sin(angle)]

prox, strong = 0, 0
for r in (0., 1e-9, .49, .5, .5000001, .75, .9, 1., 1.25, 2., 10.):
    for angle in (0., .7, math.pi, 4.1):
        x = point(r, angle)
        y = T(x)
        assert norm(sub(add(y, grad(y)), x)) < 1e-12
        hy = f(y) + norm(sub(y, x))**2/2
        for offset in ([0., 0.], [.3, 0.], [-.7, .1], [0., 1.1]):
            z = add(y, offset)
            hz = f(z) + norm(sub(z, x))**2/2
            assert hz >= hy + norm(sub(z, y))**2/3 - 1e-12
            strong += 1
        prox += 1

points = [point(r, a) for r in (0., .1, .749999, .75, .750001, 1., 3.)
          for a in (0., 1., 3.)]
convex = 0
for y in points:
    for z in points:
        gy = f(y) + dot(y, y)/6
        gz = f(z) + dot(z, z)/6
        assert gz >= gy + dot(add(grad(y), scale(1/3, y)), sub(z, y)) - 1e-12
        convex += 1

tube = 0
for r in (.75, .8, .99, 1., 1.01, 1.2, 1.25):
    for angle in (0., .7, 2.1, math.pi):
        x = point(r, angle)
        y = T(x)
        p = scale(1/r, x)
        assert norm(sub(sub(scale(2, y), x), p)) < 1e-12
        assert abs(abs(norm(y) - 1) - abs(r - 1)/2) < 1e-12
        assert abs(norm(grad(y)) - abs(norm(y) - 1)) < 1e-12
        tube += 1

result = dict(status="PASS finite checks; analytic proofs govern universal statements",
              algebra_exact_samples=checks, linear_gate_samples=len(rows),
              linear_gate_rows=rows, proximal_boundary_samples=prox,
              strong_convexity_pairs=strong, convex_support_pairs=convex,
              circle_tube_samples=tube, junction="3/4, exact C1 equality",
              minimum_value="-1/8", origin_index_sign=1)
(BASE / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "linear_gate_rows"}, ensure_ascii=False))
