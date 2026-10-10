"""Finite checks for TC7--TC11; no external dependencies, no claim of proof.

Run from repo root: python3 research/code/topological_completion/verify.py
The report uses exact rational junctions, seed 20261010, binary64 randomized
geometry and independently coded forward/inverse radial functions.
"""
import json
import math
import random
import sys
from fractions import Fraction as Q
from pathlib import Path

SEED = 20261010
TOL = 3e-11


def tau(r):
    if r <= .5:
        return 1.75 * r
    if r <= 1.5:
        return 1 + (r - 1) ** 3
    if r <= 3:
        return r / 4 + .75
    return r / 2


def inverse_tau(s):
    if s <= .875:
        return 4 * s / 7
    if s <= 1.125:
        t = s - 1
        return 1 + math.copysign(abs(t) ** (1 / 3), t)
    if s <= 1.5:
        return 4 * s - 3
    return 2 * s


def norm(x):
    return math.sqrt(sum(v * v for v in x))


def radial(x, radius):
    r = norm(x)
    return [0.0] * len(x) if r == 0 else [radius(r) * v / r for v in x]


def subtract(x, y):
    return [a - b for a, b in zip(x, y)]


def cayley(x):
    return subtract([2 * v for v in radial(x, tau)], x)


def original_f(y):
    return subtract(radial(y, inverse_tau), y)


def run():
    rng = random.Random(SEED)
    B = 1 + 2 / (3 * math.sqrt(6))
    exact = [lambda r: Q(7, 4) * r, lambda r: 1 + (r - 1) ** 3,
             lambda r: r / 4 + Q(3, 4), lambda r: r / 2]
    for i, r in enumerate([Q(1, 2), Q(3, 2), Q(3)]):
        assert exact[i](r) == exact[i + 1](r)
    max_error = 0.0
    for r in [0, .5, .875, 1, 1.125, 1.5, 3, 10, 1e6]:
        error = abs(inverse_tau(tau(r)) - r)
        assert error <= TOL * max(1, r)
        max_error = max(max_error, error)

    # Derivative/tangential bounds and extremum: analytic formulas sampled.
    max_slope = 0.0
    for i in range(40001):
        r = 4 * i / 40000
        c = 2 * tau(r) - r
        derivative = 2.5 if r < .5 else (
            6 * (r - 1) ** 2 - 1 if r < 1.5 else (-.5 if r < 3 else 0))
        max_slope = max(max_slope, abs(derivative), abs(c / r) if r else 2.5)
        assert abs(c) <= B + TOL
    assert max_slope <= 2.5 + TOL
    r_peak = 1 - 1 / math.sqrt(6)
    assert abs(2 * tau(r_peak) - r_peak - B) < TOL

    max_lip_ratio = 0.0
    max_holder_ratio = 0.0
    samples = 0
    for n in [1, 2, 3, 7]:
        for _ in range(2500):
            x = [rng.uniform(-4, 4) for _ in range(n)]
            y = [rng.uniform(-4, 4) for _ in range(n)]
            tx = radial(x, tau)
            fx = original_f(tx)
            error = norm(subtract([a + b for a, b in zip(tx, fx)], x))
            max_error = max(max_error, error)
            assert error <= TOL * max(1, norm(x))
            d = norm(subtract(x, y))
            cd = norm(subtract(cayley(x), cayley(y)))
            max_lip_ratio = max(max_lip_ratio, cd / d)
            assert cd <= 2.5 * d + TOL
            for gamma in [.25, .5, .75, .99]:
                L = 2.5 ** gamma * (2 * B) ** (1 - gamma)
                ratio = cd / (L * d ** gamma)
                max_holder_ratio = max(max_holder_ratio, ratio)
                assert ratio <= 1 + TOL
            samples += 1

    max_eb_ratio = 0.0
    max_contraction = 0.0
    for i in range(10001):
        t = -.5 + i / 10000
        output_t = tau(1 + t) - 1
        f_norm = abs(t - t ** 3)
        assert abs(output_t - t ** 3) < TOL
        if abs(t) > 1e-12:
            # The EB uses output_t algebraically; near 0 radius subtraction
            # loses digits, so the matching ratio uses exact displayed t^3.
            ratio = abs(t ** 3) / f_norm ** 3
            max_eb_ratio = max(max_eb_ratio, ratio)
            max_contraction = max(max_contraction, abs(t ** 3) / abs(t))
            assert ratio <= float(Q(64, 27)) + TOL
    assert max_contraction <= .25 + TOL
    indices = []
    for n in range(1, 9):
        chi = 1 + (-1) ** (n - 1)
        origin = (-1) ** n
        assert chi + origin == 1
        indices.append({'ambient_n': n, 'sphere_chi': chi,
                        'origin_index': origin, 'total': chi + origin})
    result = {
        'python_version': sys.version,
        'seed': SEED, 'arithmetic': 'Fraction exact junctions; IEEE binary64 geometry',
        'absolute_relative_tolerance': TOL, 'random_pairs': samples,
        'max_complete_resolvent_identity_error': max_error,
        'max_sampled_C_slope': max_slope, 'max_random_C_lipschitz_ratio': max_lip_ratio,
        'max_normalized_holder_ratio': max_holder_ratio,
        'B': B, 'L_gamma_half': math.sqrt(5 * B),
        'max_matching_EB_ratio': max_eb_ratio, 'EB_bound_exact': '64/27',
        'max_tube_distance_contraction': max_contraction,
        'indices': indices,
        'scope': 'Finite arithmetic/geometry checks only; not proof of index theorem or universal claims.'
    }
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run()
