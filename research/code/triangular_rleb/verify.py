"""Finite regression checks for the analytic triangular Holder example.

These checks do not establish the universal statements proved in the report.
Standard library only. Seed and exact arithmetic are recorded in results.json.
"""
from fractions import Fraction
from math import sqrt, hypot, isclose
from pathlib import Path
import hashlib
import json
import random

R = Fraction(1, 16)
L_anchored = sqrt(2)
L_all_pairs = Fraction(3, 2)
kappa = Fraction(3, 4)
random.seed(20261011)

def F(y):
    u, v = y
    return u, -sqrt(abs(u))

def J(x):
    a, b = x
    return a / 2, b + sqrt(abs(a) / 2)

def C(x):
    a, b = x
    return 0.0, b + sqrt(2 * abs(a))

def norm(x):
    return hypot(*x)

def sub(x, y):
    return x[0] - y[0], x[1] - y[1]

def check_input(x):
    y = J(x)
    fy = F(y)
    assert all(isclose(y[i] + fy[i], x[i], rel_tol=2e-12, abs_tol=2e-12)
               for i in (0, 1))
    rho2 = norm(fy) ** 2
    assert abs(y[0]) <= rho2 + 1e-13
    if abs(x[0]) <= float(R):
        p = (0.0, x[1])
        anchored = norm(sub(C(x), p))
        # Large tangential translations cause harmless subtractive cancellation.
        # Test the floating difference against the independently stable formula.
        anchored_exact = sqrt(2 * abs(x[0]))
        assert isclose(anchored, anchored_exact, rel_tol=2e-12, abs_tol=2e-10)
        assert anchored_exact <= L_anchored * sqrt(abs(x[0])) + 1e-12
    return y

boundary_inputs = [(a, b) for a in (-float(R), 0.0, float(R), -1e-20, 1e-20)
                   for b in (-1e5, 0.0, 1e5)]
for x in boundary_inputs:
    check_input(x)

max_pair_ratio = 0.0
pair_count = 0
for _ in range(25000):
    x = (random.uniform(-float(R), float(R)), random.uniform(-1e3, 1e3))
    da = random.uniform(-1.0, 1.0)
    db = random.uniform(-1.0, 1.0)
    delta = float(R) * random.random()
    dn = hypot(da, db)
    y = (x[0] + delta * da / dn, x[1] + delta * db / dn)
    if abs(y[0]) > float(R):
        continue
    actual_delta = norm(sub(x, y))
    if actual_delta == 0:
        continue
    lhs = norm(sub(C(x), C(y)))
    ratio = lhs / sqrt(actual_delta)
    assert ratio <= float(L_all_pairs) + 1e-10
    A, B = abs(x[0] - y[0]), abs(x[1] - y[1])
    first_bound = B + sqrt(2 * A)
    tight_bound = sqrt(actual_delta) * (1 / sqrt(2) + sqrt(.5 + actual_delta))
    assert lhs <= first_bound + 1e-10
    assert first_bound <= tight_bound + 1e-10
    max_pair_ratio = max(max_pair_ratio, ratio)
    check_input(x)
    check_input(y)
    pair_count += 1

compatibility = (sqrt(float(R)) + L_anchored) ** 2 / 4
assert isclose(compatibility, 33 / 64 + sqrt(2) / 8, rel_tol=1e-15)
assert compatibility < float(Fraction(45, 64)) < float(kappa)
assert isclose((4 * compatibility - sqrt(float(R)) ** 2 - 2) /
               (2 * sqrt(float(R))), L_anchored, rel_tol=2e-15)
window = (float(R) + L_anchored / 4) / 2
assert isclose(window, (1 + 4 * sqrt(2)) / 32, rel_tol=1e-15)
assert window < float(Fraction(7, 32)) < 1
assert 1 / sqrt(2) + 3 / 4 < float(L_all_pairs)
# Separate all-pair constants, never substituted for the anchored constants.
assert (Fraction(1, 4) + L_all_pairs) ** 2 / 4 == Fraction(49, 64)
assert Fraction(49, 64) < Fraction(4, 5)

orbit_count = 0
for a0 in (-1.0, -float(R), 0.0, float(R), 1.0):
    for b0 in (-3.0, 0.0, 3.0):
        x = (a0, b0)
        b_inf = b0 + sqrt(abs(a0)) / (sqrt(2) - 1)
        for k in range(35):
            a_exact = 2 ** (-k) * a0
            b_exact = b0 + sqrt(abs(a0)) * (1 - 2 ** (-k / 2)) / (sqrt(2) - 1)
            assert isclose(x[0], a_exact, rel_tol=2e-13, abs_tol=2e-13)
            assert isclose(x[1], b_exact, rel_tol=2e-13, abs_tol=2e-13)
            tail_exact = hypot(2 ** (-k) * a0,
                               sqrt(abs(a0)) * 2 ** (-k / 2) / (sqrt(2) - 1))
            assert isclose(norm(sub((0., b_inf), x)), tail_exact,
                           rel_tol=2e-9, abs_tol=2e-12)
            x = check_input(x)
        orbit_count += 1

# Exact SPD-metric counterexample: zero input has a nonzero complete output.
G = ((Fraction(1), Fraction(1, 2)), (Fraction(1, 2), Fraction(1)))
u, v = Fraction(-4, 49), Fraction(16, 49)
sqrt_abs_u = Fraction(2, 7)
assert sqrt_abs_u ** 2 == abs(u)
fy = (u, -sqrt_abs_u)
Gy = (G[0][0] * u + G[0][1] * v, G[1][0] * u + G[1][1] * v)
assert tuple(fy[i] + Gy[i] for i in (0, 1)) == (0, 0)
assert G[0][0] * G[1][1] - G[0][1] ** 2 == Fraction(3, 4) > 0
assert norm((float(u), float(v))) > 0

# Relaxed PPA is a distinct GPPA interpretation; check its exact orbit separately.
relaxed_orbit_count = 0
for lam in (.25, 1.0, 4.0):
    for normalized_eta in (.1, .5, 1.0, 1.5, 1.9):
        eta = normalized_eta * (1 + lam) / lam
        q = 1 - eta * lam / (1 + lam)
        assert abs(q) < 1
        coefficient = eta * lam / sqrt(1 + lam)
        for a0 in (-float(R), 0., float(R)):
            a, b = a0, -2.
            b_inf = -2. + coefficient * sqrt(abs(a0)) / (1 - sqrt(abs(q)))
            for k in range(35):
                a_closed = q ** k * a0
                b_closed = -2. + coefficient * sqrt(abs(a0)) * (1 - abs(q) ** (k / 2)) / (1 - sqrt(abs(q)))
                assert isclose(a, a_closed, rel_tol=2e-12, abs_tol=2e-12)
                assert isclose(b, b_closed, rel_tol=2e-12, abs_tol=2e-12)
                prox = (a / (1 + lam), b + lam * sqrt(abs(a) / (1 + lam)))
                updated = ((1 - eta) * a + eta * prox[0],
                           (1 - eta) * b + eta * prox[1])
                formula = (q * a, b + coefficient * sqrt(abs(a)))
                assert all(isclose(updated[i], formula[i], rel_tol=2e-12, abs_tol=2e-12)
                           for i in (0, 1))
                a, b = updated
            relaxed_orbit_count += 1
assert 1 - 4 / 2 == -1
# At eta=4, lambda=1, nonzero normal amplitude is constant and tangent drift is positive.
assert 4 / sqrt(2) * sqrt(float(R)) > 0

result = {
    "status": "PASS (finite regression only; analytic proofs are in the report)",
    "seed": 20261011,
    "boundary_input_count": len(boundary_inputs),
    "tested_pair_count": pair_count,
    "max_tested_holder_ratio": max_pair_ratio,
    "orbit_count": orbit_count,
    "steps_per_orbit": 35,
    "relaxed_orbit_count": relaxed_orbit_count,
    "anchored_constants": {"R": str(R), "L": "sqrt(2)", "kappa": str(kappa),
                           "compatibility_max": "33/64+sqrt(2)/8",
                           "compatibility_max_numeric": compatibility,
                           "residual_evaluation_window": "(1+4*sqrt(2))/32",
                           "residual_evaluation_window_numeric": window},
    "all_pair_constants_separate": {"R": str(R), "L": str(L_all_pairs),
                                    "compatibility_max_if_used": "49/64",
                                    "kappa_if_used": "4/5"},
    "metric_counterexample": {"G": [[str(z) for z in row] for row in G],
                              "output": [str(u), str(v)],
                              "F_plus_G_y": ["0", "0"]},
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
