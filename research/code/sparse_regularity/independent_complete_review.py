#!/usr/bin/env python3
"""Independent exact certificate and numerical recurrence check.

The finite recurrence check is diagnostic.  The inequalities checked using
Fraction and the audit's analytic argument carry the universal quantifiers.
"""

from fractions import Fraction as F
from math import hypot, sqrt
import json


def exact_checks():
    radius = F(7, 8)
    zero_free_bound = F(21, 32)*radius**2 + F(35, 2048)*radius**4/(1-radius**2)
    assert zero_free_bound == F(214375, 393216) < 1
    v = F(1, 196)
    scale = 2 / radius**6
    tail = scale / (1-v)
    first = scale * (6/(1-v) + 2*v/(1-v)**2)
    second = scale * (30/(1-v) + 26*v/(1-v)**2 + 8*v*v/(1-v)**3)
    assert tail < 5 and first < 28 and second < 140
    star_coefficient = F(95, 1024) - F(11, 8192) - (28+F(5, 32))/961
    assert star_coefficient > F(1, 32)
    coordinate_comparison = 2*F(9, 64)**2 + F(33, 32)**4
    assert coordinate_comparison < 2
    global_M_bound = F(3, 7)+F(3, 64)+F(10, 7)+F(15, 14)
    assert global_M_bound < 3
    assert F(7, 5)**7 < 16 < F(3, 2)**7
    assert F(15, 14)**14 > 2
    assert 25 < 32  # 5/(128 sqrt(2)) < 1/32.
    beta = F(3, 32)
    tangent_coefficient = F(3, 4)*(-beta)+F(11, 64)
    assert tangent_coefficient == F(13, 128)
    sign_bound = F(3, 124)+F(11, 64*32**2)*F(32, 31)**3+F(28, 32**4)*F(32, 31)**5
    assert sign_bound < F(1, 32)
    return {
        "complex_zero_free_bound": str(zero_free_bound),
        "cauchy_tail_constants": [float(tail), float(first), float(second)],
        "star_square_remainder_coefficient": float(star_coefficient),
        "coordinate_comparison": float(coordinate_comparison),
        "global_M_upper_bound": float(global_M_bound),
        "tangent_gradient_cubic_coefficient_over_R": str(tangent_coefficient),
        "t_tail_squared_constant_times_lambda_R": "128/13",
        "distance_tail_squared_constant_times_lambda_R": "256/13",
        "tangent_sign_bound": float(sign_bound),
    }


P = 7/4
R = 2**(4/7)
LAMBDA = 1/128


def phi_derivatives(h, t):
    m = 1+h
    u = t/m
    g = ((1+u)**P+(1-u)**P)/2
    gp = P*((1+u)**(P-1)-(1-u)**(P-1))/2
    gpp = P*(P-1)*((1+u)**(P-2)+(1-u)**(P-2))/2
    a = 1/P
    f = g**a
    fp = a*g**(a-1)*gp
    fpp = a*(a-1)*g**(a-2)*gp**2+a*g**(a-1)*gpp
    ph = R*(4*h+1-f+u*fp)
    pt = R*(3*t/4-fp)
    phh = R*(4-u*u*fpp/m)
    pht = R*u*fpp/m
    ptt = R*(3/4-fpp/m)
    return ph, pt, phh, pht, ptt


def ppa_step(h_old, t_old):
    h, t = h_old, t_old
    for _ in range(8):
        ph, pt, phh, pht, ptt = phi_derivatives(h, t)
        rh = h+LAMBDA*ph/2-h_old
        rt = t+LAMBDA*pt/2-t_old
        aa = 1+LAMBDA*phh/2
        ab = LAMBDA*pht/2
        bb = 1+LAMBDA*ptt/2
        determinant = aa*bb-ab*ab
        dh = (bb*rh-ab*rt)/determinant
        dt = (aa*rt-ab*rh)/determinant
        h -= dh
        t -= dt
        if max(abs(dh), abs(dt)) < 2e-16:
            break
    assert max(abs(rh), abs(rt)) < 1e-13
    return h, t


def recurrence_check():
    h, t = .002, .010
    assert sqrt(2)*hypot(h, t) < 1/64
    inv_square_at_start = None
    max_distance = sqrt(2)*hypot(h, t)
    for k in range(50000):
        h, t = ppa_step(h, t)
        assert t > 0
        distance = sqrt(2)*hypot(h, t)
        assert distance <= max_distance+1e-13
        if k == 39999:
            inv_square_at_start = 1/(t*t)
    measured = (1/(t*t)-inv_square_at_start)/10000
    predicted = 13*LAMBDA*R/128
    assert abs(h/t**2+3/32) < 1e-4
    assert abs(measured/predicted-1) < 0.003
    # Verify the exact radial formula against one numerical resolvent step.
    radial_h = .005
    next_h, next_t = ppa_step(radial_h, 0.0)
    assert abs(next_h-radial_h/(1+2*LAMBDA*R)) < 1e-14
    assert next_t == 0.0
    return {
        "steps": 50000,
        "h_over_t_squared": h/t**2,
        "limiting_ratio": -3/32,
        "measured_inverse_t_squared_increment": measured,
        "predicted_increment": predicted,
        "relative_increment_error": measured/predicted-1,
        "radial_exact_step_error": next_h-radial_h/(1+2*LAMBDA*R),
    }


if __name__ == "__main__":
    print(json.dumps({"exact": exact_checks(), "recurrence": recurrence_check()}, indent=2))
