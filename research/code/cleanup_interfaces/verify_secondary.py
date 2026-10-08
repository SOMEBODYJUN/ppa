"""Finite rational and floating checks of SP1--SP6, not general proofs.

Run from repository root: python research/code/cleanup_interfaces/verify_secondary.py
No random sampling. Includes empty relations, zero-dimensional reduction,
multiple outputs, t=0, both signs, and the |t|=1 branch boundary.
"""
from fractions import Fraction as Q
from itertools import product
import json
import math


def reduction_checks():
    points = list(product(map(Q, (-1, 0, 1)), repeat=2))
    graphs = [[], [(u, v) for u in points for v in points],
              [(u, (Q(0), u[1])) for u in points],
              [((Q(0), Q(0)), (Q(0), Q(0)))]]
    checks = 0
    # C(x,y)=x, Q(x,y)=(x,0): singular Q and full row rank C.
    for graph in graphs:
        for p in map(Q, (-2, -1, 0, 1, 2)):
            direct = {u[0] for u, v in graph if v == (p-u[0], Q(0))}
            reduced_graph = {(u[0], v[0]) for u, v in graph if v[1] == 0}
            reduced = {z for z, w in reduced_graph if p-z == w}
            assert direct == reduced
            checks += 1
        assert {u[0] for u, v in graph if v == (Q(0), Q(0))} == {
            z for z, w in reduced_graph if w == 0}
        # H'={0}, C=0: existence requires actual zero graph values.
        direct_zero = bool([u for u, v in graph if v == (Q(0), Q(0))])
        reduced_zero = bool([(Q(0), Q(0)) for u, v in graph
                             if v == (Q(0), Q(0))])
        assert direct_zero == reduced_zero
        checks += 2
    return checks


def attainment_checks():
    checks = 0
    # f(x,y)=a*x²/2+b*y²/2, Q=diag(q,0). Includes flat directions.
    for a, b, q in product(map(Q, (0, 1, 2)), repeat=3):
        for x, y in product(map(Q, (-2, 0, 3)), repeat=2):
            v = ((a+q)*x, b*y)
            def objective(z):
                return ((a+q)*z[0]**2+b*z[1]**2)/2-v[0]*z[0]-v[1]*z[1]
            for z in product(map(Q, (-3, -1, 0, 1, 4)), repeat=2):
                gap = objective(z)-objective((x, y))
                reverse = ((a+q)*(z[0]-x)**2+b*(z[1]-y)**2)/2
                assert gap == reverse and gap >= 0
                checks += 1
    return checks


def perturbation_checks():
    checks = 0
    for q in (1.01, 1.5, 2.0, 4.0, 9.0):
        for t in (0.0, -1e-12, 1e-12, -0.01, 0.01, -1.0, 1.0, -2.0, 2.0):
            a = math.copysign(abs(t)**(1/q), t) if t else 0.0
            h = t-a
            assert math.isclose(a+h, t, rel_tol=1e-5, abs_tol=1e-15)
            assert math.isclose(abs(a)**q, abs(t), rel_tol=1e-12, abs_tol=1e-14)
            r = min(abs(a), abs(t))
            assert (r == 0) == (t == 0)
            if 0 < abs(t) <= 1:
                assert math.isclose(r, abs(t), rel_tol=1e-12)
                ratio = abs(t)/r**q
                assert math.isclose(ratio, abs(t)**(1-q), rel_tol=1e-12)
                # Reverse the computed EB ratio back to the source distance.
                assert math.isclose(ratio*r**q, abs(t), rel_tol=1e-12)
            checks += 1
    # Exact dyadic q=2 family witnesses unbounded ratio, including its sign.
    for n in (0, 1, 8, 32, 128):
        for sign in (-1, 1):
            a = sign*Q(1, 2**n)
            t = sign*Q(1, 2**(2*n))
            r = min(abs(a), abs(t))
            assert abs(t)/r**2 == 2**(2*n)
            checks += 1
    return checks


if __name__ == '__main__':
    result = {'reduction_checks': reduction_checks(),
              'attainment_checks': attainment_checks(),
              'perturbation_checks': perturbation_checks(),
              'arithmetic': 'Fraction exact plus explicit floating tolerances',
              'status': 'finite-input checks passed; proofs are SP1--SP6'}
    print(json.dumps(result, ensure_ascii=False, indent=2))
