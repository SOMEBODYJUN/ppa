#!/usr/bin/env python3
"""Finite boundary checks for gauge_unification_review.md; not universal proof.

Run: python3 research/code/submonotonicity_routes/gauge_verify.py
Python standard library; Fraction checks exact; floating trajectory tol 1e-12.
No random sampling, no external dependencies, no generated files.
"""

from fractions import Fraction as Q
from itertools import product
from math import hypot, sqrt
import json


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def norm2(x):
    return dot(x, x)


def main():
    checks = {}
    identity_count = 0
    vals = [Q(i, 3) for i in range(-3, 4)]
    for ax, ay, bx, by in product(vals, repeat=4):
        a, b = (ax, ay), (bx, by)
        z, c = (ax+bx, ay+by), (ax-bx, ay-by)
        assert 4*dot(a, b) == norm2(z)-norm2(c)
        identity_count += 1
    checks['exact_identity_pairs'] = identity_count

    semimono_count = 0
    for m, sigma in product([Q(-3, 4), Q(-1, 4), Q(0), Q(1, 4), Q(1)], repeat=2):
        A, B, Delta = 1+m+sigma, m-sigma, 1-4*m*sigma
        for a, b in product(vals, repeat=2):
            z, c = a+b, a-b
            assert 4*(a*b-m*a*a-sigma*b*b) == (1-m-sigma)*z*z-A*c*c-2*B*z*c
            if A != 0:
                assert A*((c+B*z/A)**2)-Delta*z*z/A == -4*(a*b-m*a*a-sigma*b*b)
            semimono_count += 1
    checks['exact_semimonotone_expansions'] = semimono_count

    # Critical primal gauge: F(x)=-x+x^3, |x|<=1/4.
    critical_count = 0
    for x, y in product([Q(i, 40) for i in range(-10, 11)], repeat=2):
        a, b = x-y, (-x+x**3)-(-y+y**3)
        assert a*b >= -a*a+a**4/4
        assert abs(a+b) >= abs(a)**3/4
        if x != y:
            assert a+b != 0
        critical_count += 1
    checks['exact_critical_cubic_pairs'] = critical_count

    # D(r,s)=rs*(1-1/(1+(r+s)^4)); diagonal strictness but no uniform envelope.
    remote = []
    for n in [1, 2, 10, 100, 1000]:
        r = s = Q(n)
        D = r*s*(1-1/(1+(r+s)**4))
        u2 = r*r+s*s-2*D
        c2 = 2*(r*r+s*s)-u2
        assert 0 < D < r*r
        assert 0 < u2 <= (r+s)**2
        assert c2 > 0
        remote.append({'n': n, 'input': sqrt(float(u2)), 'reflection': sqrt(float(c2))})
    checks['remote_diagonal_strictness'] = remote

    # gamma=1/2 and t=1/n^4 make t^gamma and all comparison squares rational.
    separation = []
    for n in [2, 4, 8, 16, 32]:
        t, q = Q(1, n**4), Q(1, n**2)
        z, a, b = (Q(0), t), (q, t/2), (-q, t/2)
        c = (2*q, Q(0))
        assert norm2(c) == 4*t
        assert dot(a, b) == t*t/4-t
        assert norm2(a)+norm2(b) == (norm2(z)+norm2(c))/2
        # rho(q)^2+g(q)^2 <= 2q^2 <= C(t), while q>kappa*t for all kappa<1.
        assert 2*q*q <= (t*t+4*t)/2
        assert q > t
        separation.append({'t': str(t), 'q': str(q), 'q_over_t': str(q/t)})
    checks['exact_C250_separation_witnesses'] = separation

    # Every branch policy of length 12; normal contraction is exact analytically.
    r0, worst_length, worst_normal_error = 1/16, 0.0, 0.0
    for bits in product([0, 1], repeat=12):
        u, r, length = 0.0, r0, 0.0
        for k, bit in enumerate(bits):
            y_u, y_r = u+bit*sqrt(abs(r)), r/2
            chosen_w = (u-y_u, r-y_r)
            expected_w = (-bit*sqrt(2)*sqrt(abs(y_r)), y_r)
            assert hypot(chosen_w[0]-expected_w[0], chosen_w[1]-expected_w[1]) < 1e-12
            length += hypot(y_u-u, y_r-r)
            u, r = y_u, y_r
            worst_normal_error = max(worst_normal_error, abs(r-r0*2**(-k-1)))
        worst_length = max(worst_length, length)
    length_bound = sqrt(r0)/(1-2**(-.5))+r0
    assert worst_length <= length_bound+1e-12
    checks['all_4096_branch_prefixes'] = {
        'steps': 12, 'worst_length': worst_length,
        'infinite_length_bound': length_bound,
        'worst_normal_error': worst_normal_error,
        'floating_tolerance': 1e-12,
    }
    # Complete true EB + distance contraction does not imply physical absorption.
    drift_count = 0
    for du, dv, de in product(vals, vals, [Q(-1), Q(0), Q(1)]):
        a, b = (du, dv), (du, de)
        lhs = float(dot(a, b))
        rhs = -sqrt(float(norm2(a)))*min(sqrt(float(norm2(b))), 1.0)
        assert lhs >= rhs-1e-12
        drift_count += 1
    checks['zero_fiber_drift_budget_checks'] = drift_count
    x = (Q(0), Q(0))
    for k in range(20):
        y = (x[0]/2, x[1]+1)
        assert (x[0]-y[0], x[1]-y[1]) == (y[0], Q(-1))
        assert abs(y[0]) == 0 and norm2((x[0]-y[0], x[1]-y[1])) == 1
        x = y
    checks['zero_input_drifting_prefix'] = {'steps': 20, 'endpoint': [str(v) for v in x]}
    print(json.dumps({'status': 'finite_checks_passed', 'checks': checks}, indent=2))


if __name__ == '__main__':
    main()
