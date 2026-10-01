"""Independent deterministic arithmetic checks, not a substitute for proofs."""
import math
import random

rng = random.Random(20260908)
lam, b, c, alpha = 1.3, 0.8, 2.4, 2 / 3
minty_error = 0.0
for _ in range(2000):
    p, q = rng.uniform(-2, 2), rng.uniform(-1, 1)
    y = abs(q) / c
    t = p + lam * b * y ** alpha
    branch = 1 if q >= 0 else -1
    v_t = -b * y ** alpha
    v_y = (branch * c - 1) * y / lam
    minty_error = max(minty_error, abs(t + lam * v_t - p), abs(y + lam * v_y - q))
    assert abs(y - abs(q) / c) < 1e-14

disk_error = 0.0
for tau in [0.0, 0.4]:
    for y0 in [0.08, 0.125]:
        t, y = tau, y0
        for k in range(20):
            expected = tau + 2 / 3 * y0 ** (2 / 3) * (1 - 4 ** (-k))
            disk_error = max(disk_error, abs(t - expected), abs(y - 8 ** (-k) * y0))
            y /= 8
            t += 2 * y ** (2 / 3)

# Two branches sharing a Minty input have unequal reflection outputs.
collision_gap = abs((2 / 2 - 1) - (2 / 3 - 1))
assert math.isclose(collision_gap, 1 / 3)

# M1/SO-06 logic benchmark: fixed F={(-sqrt(y),y),(-sqrt(y),-3y)}.
# Complete direct-Minty inverse is single-valued and full-domain exactly at tau>1/3.
coverage_checks = []
for tau in [0.1, 1 / 3, 0.5, 1.0, 2.0]:
    positive_coefficient, second_coefficient = 1 + tau, 1 - 3 * tau
    full = second_coefficient < 0
    coverage_checks.append((tau, full))
    if full:
        for q in [-0.2, 0.0, 0.2]:
            y = q / positive_coefficient if q >= 0 else q / second_coefficient
            assert y >= 0
            t = 0.4 + tau * math.sqrt(y)
            assert math.isclose(t - tau * math.sqrt(y), 0.4)
    elif second_coefficient > 0:
        assert not math.isclose(0.2 / positive_coefficient, 0.2 / second_coefficient)

# B5 minimal example J(p,q) = (p + sqrt(abs(q)), abs(q)/2).
# Summable input errors force at least harmonic tangential growth.
a_err, tangential, normal, err_sum, harmonic = 1e-4, 0.0, 0.0, 0.0, 0.0
for k in range(1, 100001):
    h = a_err / k ** 2
    tangential += math.sqrt(normal + h)
    normal = (normal + h) / 2
    err_sum += h
    harmonic += 1 / k
assert tangential + 1e-12 >= math.sqrt(a_err) * harmonic
assert err_sum < a_err * math.pi ** 2 / 6

# An unchanged small normal coordinate satisfies arbitrarily small fixed relative error.
relative = []
for d in [1e-2, 1e-4, 1e-6, 1e-8]:
    error = d
    actual_step = math.sqrt(2 * d)
    relative.append(error / actual_step)
    assert math.isclose(error / actual_step, math.sqrt(d / 2))

assert minty_error < 1e-12
assert disk_error < 1e-12
print({
    "seed": 20260908,
    "two_branch_samples": 2000,
    "two_branch_Minty_max_error": minty_error,
    "disk_orbit_max_error": disk_error,
    "disk_L": (1 / 8) ** (1 / 3) + 8 * (1 / 8) ** (2 / 3),
    "disk_certificate_factor": (3 / 4) ** 1.5,
    "reverse_collision_reflection_gap_at_unit_input": collision_gap,
    "M1_direct_Minty_tau_coverage": coverage_checks,
    "inexact_steps": 100000,
    "inexact_error_sum": err_sum,
    "inexact_distance": normal,
    "inexact_tangent": tangential,
    "harmonic_tangent_lower_bound": math.sqrt(a_err) * harmonic,
    "fixed_relative_error_ratios": relative,
})
