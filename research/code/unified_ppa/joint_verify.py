#!/usr/bin/env python3
"""Finite checks for unified_ppa_joint_parent.md.

Standard library only. Fraction checks are exact; floating checks use the
explicit tolerance below. No finite check certifies the general theorem,
infinite length, full-fiber coverage, or external novelty.
"""
from fractions import Fraction as F
from itertools import product
import json
import math

TOL = 2e-12


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def norm2(a):
    return dot(a, a)


def algebra_checks():
    values = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    count = 0
    for coords in product(values, repeat=4):
        a, b = coords[:2], coords[2:]
        A, B, C = norm2(a), norm2(b), dot(a, b)
        t2 = norm2(tuple(x + y for x, y in zip(a, b)))
        reflected2 = norm2(tuple(x - y for x, y in zip(a, b)))
        assert t2 == A + 2 * C + B
        assert reflected2 == A - 2 * C + B
        assert t2 - reflected2 == 4 * C
        assert C * C <= A * B
        for lam in [F(1, 3), F(1), F(3)]:
            f = tuple(v / lam for v in b)
            assert dot(a, f) == C / lam
            assert norm2(f) == B / lam**2
            for mu, rho in [(F(1, 2), F(-1, 3)), (F(-1), F(2))]:
                # Exact scaled semimonotone deficit identity.
                original = dot(a, f) - mu * A - rho * norm2(f)
                scaled = C - lam * mu * A - (rho / lam) * B
                assert scaled == lam * original
        count += 1
    # PSD versus positive rank-one attack: A=B=1,C=0,t^2=2.
    assert F(1) * F(1) - F(0)**2 > 0
    assert (F(1) + F(1))**2 > F(2)
    return count


def semimonotone_feature_checks():
    values = [F(i, 2) for i in range(-4, 5)]
    parameters = list(product([F(0), F(1, 4), F(1), F(2)],
                              [F(1, 3), F(1), F(3)]))
    count = 0
    for coords in product(values, repeat=4):
        a, b = coords[:2], coords[2:]
        A, B, C = norm2(a), norm2(b), dot(a, b)
        t2 = A + 2 * C + B
        for m, k in parameters:
            if C < m * A:
                continue
            q2 = min(A, k * k * B)
            D = 1 + 2 * m + max(m * m, 1 / (k * k))
            assert t2 >= D * q2
            count += 1
    # Exact formula JP25 at the minimizing feature point for nu=0.
    minimizers = 0
    for m, k in parameters:
        h = max(m, 1 / k)
        scale = max(F(1), 1 / (k * h)**2)
        A, B, C = scale, scale * h * h, scale * m
        assert C * C <= A * B
        assert min(A, k * k * B) == 1
        D = 1 + 2 * m + max(m * m, 1 / (k * k))
        assert A + 2 * C + B == D
        minimizers += 1
    return count, minimizers


def slow_branch_identity_checks():
    count = 0
    for denominator in range(1, 65):
        for numerator in range(1, denominator + 1):
            q = F(numerator, denominator)
            t = q + q**3
            increment = 1 / q**2 - 1 / t**2
            rhs = (2 + q**2) / (1 + q**2)**2
            assert increment == rhs
            assert 0 < increment <= 2
            assert t - q == q**3
            assert min(q, q**3) == q**3
            count += 1
    return count


def gu3_exact_checks():
    count = 0
    for denominator in range(1, 17):
        for numerator in range(1, denominator + 1):
            root_t = F(numerator, denominator)
            t = root_t**2
            for sign in [-1, 1]:
                for drift in [F(0), root_t]:
                    a = (drift, sign * t / 2)
                    b = (-drift, sign * t / 2)
                    q = t / 2
                    assert a[1] == b[1]
                    assert a[0] + b[0] == 0
                    assert q * q == a[1] * a[1]
                    assert norm2(tuple(x + y for x, y in zip(a, b))) == 4 * q * q
                    assert b[0] * b[0] <= 2 * q
                    # True residual is the norm of the straight branch.
                    assert min(q*q, q*q + 2*q) == q*q
                    count += 1
    # A simple certified W(t)=t+4 sqrt(t) dominates JP31 for gamma=1/2:
    # 4(1-1/sqrt(2)) >= 1 iff 3 >= 2 sqrt(2), checked by squares.
    assert F(9) > F(8)
    return count


def cubic_output(t):
    assert t >= 0
    lo, hi = 0.0, t
    for _ in range(70):
        mid = (lo + hi) / 2
        if mid + mid**3 <= t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def double_branch_prefix_checks(depth=13):
    count = 0
    max_defect = 0.0
    for initial in [0.125, 1.0]:
        frontier = [(initial, 0.0)]
        for _ in range(depth):
            following = []
            for t, length in frontier:
                g = cubic_output(t)
                assert t / 2 - TOL <= g <= t + TOL
                assert abs(g + g**3 - t) < TOL
                for q in [t / 2, g]:
                    s = t - q
                    new_length = length + s
                    defect = abs(new_length - (initial - q))
                    max_defect = max(max_defect, defect)
                    assert defect < TOL
                    assert new_length <= initial + TOL
                    following.append((q, new_length))
                    count += 1
            frontier = following
    # Signs are exactly preserved by oddness; no separate negative branch solve.
    return count, max_defect


def shell_potential_checks():
    # JP18a-c for p=3/2, c=ell=R=1; C is rounded upward to 24.
    p, delta, c, ell, radius, C = 1.5, 0.5, 1.0, 1.0, 1.0, 24.0
    assert C >= radius**(p-1)/(math.sqrt(c)*(1-2**(-delta)))
    assert C >= 2**(p+1)/(c*ell*delta)
    count = 0
    for i in range(1, 151):
        t = radius * i / 150
        for j in range(151):
            q = t * j / 150
            low, high = ell * q**p, math.sqrt(max(0.0, (t*t-q*q)/c))
            if low > high + 1e-14:
                continue
            # The largest feasible s is the worst case for this fixed t,q.
            assert high <= C*(t**delta-q**delta) + TOL
            count += 1
    return count


def nilpotent_full_graph_checks():
    """Parametrize every sampled complete output by x1=u+u^3.

    The complete-fiber proof uses strict monotonicity in the text. These are
    exact finite checks of the defining graph, residual and two-state bounds.
    """
    count = 0
    values = [F(i, 8) for i in range(-16, 17)]
    for u, v in product(values, repeat=2):
        x = (u + u**3, v)
        y = (F(0), u)
        selected = (u + u**3, v - u)
        assert tuple(a + b for a, b in zip(y, selected)) == x
        # The following output is exactly zero because its input first entry is zero.
        next_output = (F(0), F(0))
        assert next_output[1] + next_output[1]**3 == y[0]
        t2, q2 = norm2(x), norm2(y)
        step2 = norm2(tuple(a - b for a, b in zip(x, y)))
        residual2 = (u + u**3)**2
        assert q2 <= residual2 <= norm2(selected)
        assert q2 <= t2
        assert step2 <= 4 * t2  # s<=2t; next step q<=t; total<=3t.
        if x[0] == 0:
            assert u == 0
            assert q2 == 0 and step2 == t2
        if v == 0:
            assert step2 == t2 + q2  # The impossible-to-repeat radial feature.
        count += 1
    return count


def main():
    semimonotone, minimizers = semimonotone_feature_checks()
    branches, defect = double_branch_prefix_checks()
    result = {
        "status": "finite_checks_passed",
        "exact_gram_instances": algebra_checks(),
        "exact_semimonotone_feature_inequalities": semimonotone,
        "exact_semimonotone_feature_minimizers": minimizers,
        "exact_slow_branch_divergence_identity_instances": slow_branch_identity_checks(),
        "exact_gu3_direction_instances": gu3_exact_checks(),
        "double_branch_prefix_transitions": branches,
        "max_telescoping_float_defect": defect,
        "shell_potential_float_instances": shell_potential_checks(),
        "exact_nilpotent_complete_graph_instances": nilpotent_full_graph_checks(),
        "float_tolerance": TOL,
        "seed": None,
        "scope": "Finite instances only; universal proofs are in the candidate text."
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
