"""Finite deterministic area benchmark and full-resolvent identity checks.
Run: python3 research/code/tangential_area/verify_area.py
No finite output proves C232. Uses standard-library binary64, seed 20261010.
"""
import cmath
import json
import math
import random
import sys
from pathlib import Path


def d(r, p, omega):
    return 0j if r == 0 else abs(r) ** p * cmath.exp(1j * omega / abs(r))


def T(u, p, omega):
    w, z, r = u
    b = d(r, p, omega)
    return w + b, z + .5 * (w.conjugate() * b).imag, r / (1 + abs(r))


def F(u, p, omega):
    w, z, r = u
    assert abs(r) < 1
    s = r / (1 - abs(r))
    b = d(s, p, omega)
    return -b, -.5 * (w.conjugate() * b).imag, s - r


def run():
    rng = random.Random(20261010)
    max_error = 0.0
    for p in [1 / 3, .75, 1.25]:
        for omega in [math.pi, math.pi / 2, 2 * math.pi]:
            for _ in range(500):
                u = complex(rng.uniform(-2, 2), rng.uniform(-2, 2)), rng.uniform(-2, 2), rng.uniform(-2, 2)
                y = T(u, p, omega)
                f = F(y, p, omega)
                err = max(abs(y[i] + f[i] - u[i]) for i in range(3))
                max_error = max(max_error, err)
                assert err < 1e-9
                residual = math.sqrt(abs(f[0]) ** 2 + f[1] ** 2 + f[2] ** 2)
                assert abs(y[2]) <= residual ** (1 / p) + 1e-10
    rows = []
    N, t0 = 200000, 8
    for p in [1 / 3, .75]:
        for phase_quarters in [1, 2, 4]:
            w, z, s2 = 0j, 0.0, 0.0
            marker = None
            for n in range(N):
                a = (t0 + n) ** (-p)
                # Exact quarter-turn phase: avoids large trigonometric arguments.
                b = a * 1j ** ((phase_quarters * (t0 + n)) % 4)
                z += .5 * (w.conjugate() * b).imag
                w += b
                s2 += a * a
                if n == N // 2 - 1:
                    marker = z, s2, w
            ratio = (z - marker[0]) / (s2 - marker[1])
            corrected_ratio = None
            if phase_quarters == 1:
                q = 1j
                b_next = (t0 + N) ** (-p) * q ** ((t0 + N) % 4)
                w_inf_estimate = w + b_next / (1 - q)
                first_order = .5 * (w_inf_estimate.conjugate() * (w - marker[2])).imag
                corrected_ratio = (z - marker[0] - first_order) / (s2 - marker[1])
                assert abs(corrected_ratio - .25) < 1e-4
            else:
                assert z == 0
            rows.append({'p': p, 'omega_over_pi': phase_quarters / 2,
                         'w_abs': abs(w), 'z': z, 'tail_area_ratio': ratio,
                         'first_order_removed_area_ratio': corrected_ratio})
    report = {'python_version': sys.version, 'seed': 20261010, 'precision': 'IEEE binary64', 'iterations': N,
              't0': t0, 'initial_w_z': [0, 0], 'max_identity_error': max_error,
              'identity_tolerance': 1e-9, 'area_ratio_tolerance': 1e-4,
              'rows': rows, 'scope': 'Finite checks only; does not prove C232.'}
    Path(__file__).with_name('area_results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    run()
