"""C462 fixed-instance diagnostics; the universal proof is in the canonical note.

Python standard library only. Deterministic Decimal120, no random seed or data.
Numbers printed below are diagnostics, not interval arithmetic certificates.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import json
import hashlib
import sys
from pathlib import Path

getcontext().prec = 120
D = Decimal
B = R = D(1) / 4
R0 = D(1) / 8
assert Fraction(1, 16) / (Fraction(17, 16) / Fraction(9, 8)) == Fraction(9, 136)


def sign(x):
    return D(1) if x > 0 else D(-1) if x < 0 else D(0)


def update(p, r):
    t = abs(r)
    return p + B * min(max(p, D(0)).sqrt(), t), r * t / (1 + t)


def inverse(eta, z):
    a = abs(z)
    t = (a + (a * a + 4 * a).sqrt()) / 2
    if eta <= 0:
        p = eta
    elif eta <= t * t + B * t:
        p = (2 * eta / (B + (B * B + 4 * eta).sqrt())) ** 2
    else:
        p = eta - B * t
    return p, sign(z) * t


def norm(p, r):
    return (p * p + r * r).sqrt()


points = 0
tol = D('1e-100')
for p in map(D, ['-2', '-.01', '0', '1e-20', '1e-6', '.01', '1', '2']):
    for r in map(D, ['-.25', '-.125', '-1e-6', '0', '1e-6', '.125', '.25']):
        eta, z = update(p, r)
        pp, rr = inverse(eta, z)
        assert norm(pp - p, rr - r) < tol
        vp, vr = pp - eta, rr - z
        residual = norm(vp, vr)
        assert abs(z) <= R * residual + tol
        anchor = (p - eta) * (eta - p) + (r - z) * z
        assert anchor >= -B * B * r * r - tol
        assert abs(z) <= (D(9) / 136).sqrt() * abs(r) + tol
        points += 1


def selected_limit(log_inverse_epsilon):
    p = (-D(log_inverse_epsilon)).exp()
    r = R0
    first_cap = None
    for k in range(100):
        if first_cap is None and p >= r * r:
            first_cap = k
        if first_cap is not None:
            # The remaining tangential increment is <= B*r/(1-R).
            tail_cap = B * r / (1 - R)
            if tail_cap <= p * D('1e-105'):
                break
        p, r = update(p, r)
    else:
        raise AssertionError('diagnostic iteration cap reached')
    assert first_cap is not None
    z = D(log_inverse_epsilon)
    a0, b0 = D(8).ln(), D(10).ln()
    lower = B * (-2 * b0 / a0.sqrt() * z.sqrt()).exp()
    upper = D(5) / 6 * (-a0 / (2 * (2 * b0).sqrt()) * z.sqrt()).exp()
    if first_cap >= 2:
        assert lower <= p <= upper
    return {
        'log_inverse_epsilon': log_inverse_epsilon,
        'first_cap': first_cap,
        'negative_log_limit_gap': str(-p.ln()),
        'negative_log_gap_over_sqrt_log_inverse_epsilon': str(-p.ln() / z.sqrt()),
        'remaining_tail_relative_bound': str(tail_cap / p),
    }


print(json.dumps({'python_version': sys.version, 'precision': 120,
                  'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'roundtrip_and_DD1_points': points,
                  'diagnostics': [selected_limit(n) for n in [16, 64, 256, 1024, 4096, 16384]]},
                 indent=2))
