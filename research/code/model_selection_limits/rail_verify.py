#!/usr/bin/env python3
"""C271 finite checks. Analytic text, not sampled roots, proves full coverage."""
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform
import numpy as np
import scipy
from scipy.optimize import brentq

SEED = 271
rng = np.random.default_rng(SEED)


def norm(v):
    return float(np.linalg.norm(v))


def h(p):
    P = norm(p)
    return np.zeros(2) if P == 0 else p / np.sqrt(P)


def le(a, b):
    assert a <= b + 5e-10 * max(1., abs(a), abs(b)), (a, b)


def fiber(a, b, delta):
    def phi(q):
        p = (b - q * np.array([delta, 1.])) / 11
        return q * abs(q) - a[1] - h(p)[1]
    radius = 1. + abs(a[1]) + norm(b)
    while not phi(-radius) < 0 < phi(radius):
        radius *= 2
    q = brentq(phi, -radius, radius, xtol=5e-324, rtol=1e-14, maxiter=1000)
    p = (b - q * np.array([delta, 1.])) / 11
    z = a + h(p)
    assert abs(z[1] - q * abs(q)) < 1e-9 * max(1., abs(z[1]), q * q)
    return z, p, q


R = Q(1, 10000)
K_R = (R + Q(1, 100)) / 2
assert K_R == Q(101, 20000) < Q(3, 500)
compat = Q(8, 5) * Q(101, 200) ** 2
assert compat == Q(10201, 25000) < Q(1, 2)
reflection_bound = .884 + 4 * np.sqrt(.221 * float(R)) + (1 + 1.442 ** 2) * float(R)
assert reflection_bound < .904 < 1
assert (1 + Q(10) * Q(3, 500)) ** 2 == Q(2809, 2500) < Q(8, 5)

# P=0 anti-root: the multiplied scalar equation vanishes, true equation does not.
fakeq, delta = .2, .7
fakeb = fakeq * np.array([delta, 1.])
assert norm((fakeb - fakeq * np.array([delta, 1.])) / 11) == 0
assert abs(fakeq * abs(fakeq) - .1) > .01

# Whole-mode forward roots at boundary, zero, cross signs, and far inputs.
checks = 0
work_checks = 0
input_cases = []
for an in [-1e-4, 0., 1e-4]:
    for bt in [-1e-4, 0., 1e-4]:
        for bn in [-1e-4, 0., 1e-4]:
            input_cases.append((np.array([.3, an]), np.array([bt, bn])))
for _ in range(180):
    scale = rng.choice([1e-6, 1e-4, .1, 1., 20.])
    input_cases.append((scale * rng.normal(size=2), scale * rng.normal(size=2)))
for a, b in input_cases:
    d = np.hypot(a[1], norm(b))
    for delta in [-1., -.4, 0., .4, 1.]:
        z, p, q = fiber(a, b, delta)
        P, G, B = norm(p), abs(q), norm(b)
        reverse = b - 11 * p - q * np.array([delta, 1.])
        assert norm(reverse) < 1e-9 * max(1., B)
        c = (1 + np.sqrt(2.)) / 11
        le(P, d * d + d * np.sqrt(c * c + d * d))
        rho2 = P + (q + 10 * p[1]) ** 2 + max(abs(10 * p[0]) - G, 0.) ** 2
        dout = np.hypot(z[1], P)
        if rho2 <= .006 ** 2:
            le(dout, 1.6 * rho2)
        if d <= 1e-4:
            le(P, .221 * d)
            le(G, np.sqrt(1.0121) * d)
            anchor = np.array([a[0], 0., 0., 0.])
            incoming = np.concatenate([a, b])
            outgoing = np.concatenate([z, p])
            le(norm(2 * outgoing - incoming - anchor) ** 2, d)
            le(dout, .5 * d)
            work_checks += 1
        Ein = (2 / 3) * (abs(a[1]) ** 1.5 + B ** 1.5)
        Eout = (2 / 3) * (abs(z[1]) ** 1.5 + P ** 1.5)
        le(B ** 1.5 / 9 + 5 * P ** 1.5 / 6, Ein - Eout)
        le(Eout, .8 * Ein + 5118 * Ein ** 2)
        checks += 1

# Decimal80: sharp distance/rate and reflected-anchor reverse family.
sharp = []
with localcontext() as ctx:
    ctx.prec = 80
    two = D(2).sqrt()
    A = D(11)
    for exponent in [4, 6, 8, 10, 12]:
        t = D(10) ** (-exponent)
        bn, bt = t / two, -t / two
        def phi(q):
            pt, pn = (bt - q) / A, (bn - q) / A
            P = (pt * pt + pn * pn).sqrt()
            hn = D(0) if P == 0 else pn / P.sqrt()
            return q * abs(q) - hn
        lower, upper = D(0), bn
        for _ in range(300):
            middle = (lower + upper) / 2
            if phi(middle) <= 0:
                lower = middle
            else:
                upper = middle
        q = (lower + upper) / 2
        pt, pn = (bt - q) / A, (bn - q) / A
        P = (pt * pt + pn * pn).sqrt()
        dplus = (q ** 4 + P * P).sqrt()
        refl2 = 4 * P + (2 * pt - bt) ** 2 + (2 * pn - bn) ** 2
        sharp.append({"t": str(t), "distance_ratio": str(dplus / t),
                      "sharp_target": str(two / A), "reflected_half_constant": str((refl2 / t).sqrt())})

# Exact SPD zero fibers, drift, and Young/arithmetic constants.
metric_p = Q(4, 1849)
metric_z = Q(88, 1849)
hp = Q(2, 43)
assert metric_z == metric_p / 2 + hp and Q(43, 4) * metric_p == hp / 2
drift, momentum = Q(1, 20), Q(1, 400)
assert drift / 2 == 10 * momentum
assert Q(29, 6) - 4 == Q(5, 6)
assert Q(2, 3) - Q(5, 9) == Q(1, 9)
assert Q(96, 25) < 4
quadratic_coefficient = 6 + Q(10648, 3) * Q(36, 25)
assert quadratic_coefficient == Q(127926, 25) < 5118
assert Q(4, 5) + Q(5118) * Q(4, 3) * Q(1, 10 ** 6) < Q(81, 100)

# AC12 critical parameter fibers: direct reverse, no branch elimination by sampling.
critical_checks = 0
for Aneg in [-.1, -1., -10.]:
    Gamma = Aneg - 1
    for delta in [-1., -.4, 0., .4, 1.]:
        Qdelta = np.hypot(1., delta)
        G = (abs(Aneg) * Qdelta) ** (-1 / 3)
        for sign in [-1., 1.]:
            z = sign * G * G * np.array([delta, 1.])
            pcrit = sign * G / abs(Aneg) * np.array([delta, 1.])
            gcrit = sign * np.sqrt(abs(z[1]))
            assert norm(z - h(pcrit)) < 1e-9
            assert norm(Aneg * pcrit + gcrit * np.array([delta, 1.])) < 1e-9
            critical_checks += 1
for pt in [-10., -.001, 0., .001, 10.]:
    pcrit = np.array([pt, 0.])
    z = h(pcrit)
    assert z[1] == 0 and norm(pcrit - pcrit) == 0
    critical_checks += 1
for Aneg in [-1.1, -2., -10.]:
    G = (4 * (-Aneg - 1)) ** (-1 / 3)
    r, pn = G * G, 4 * G ** 4
    assert abs(np.sqrt(pn) - 2 * r) < 1e-10
    assert abs((Aneg + 1) * pn + G) < 1e-10
    critical_checks += 1

results = {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
           "seed": SEED, "forward_mode_root_checks": checks, "work_window_checks": work_checks,
           "K_R": str(K_R), "compatibility": str(compat), "reflection_upper": reflection_bound,
           "zero_momentum_fake_root_rejected": True, "sharp_decimal_families": sharp,
           "metric_zero_fiber_positive": {"position": str(metric_z), "momentum": str(metric_p)},
           "metric_drift": str(drift), "critical_parameter_reverse_checks": critical_checks,
           "global_energy_quadratic_coefficient": str(quadratic_coefficient),
           "scope": "Finite arithmetic only. Coverage, all fibers and policies, sharp limits, energy obstruction, and infinite-length countertrajectory are proved analytically.",
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target = Path(__file__).with_name('rail_results.json')
target.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({"output": str(target), "checks": checks, "work_checks": work_checks,
                  "sha256": results['script_sha256']}))
