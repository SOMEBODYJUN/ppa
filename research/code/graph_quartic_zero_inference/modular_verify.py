#!/usr/bin/env python3
"""Exact, dependency-free checks for the temporary modular regularity audit.

The n=13 certificate uses only a 13 by 13 matrix. A 9 by 9 quotient
multiplication check is included solely as a two-variable sanity check.
No hidden root list, production quotient matrix, or numerical tolerance is used.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


def cycle_laplacian(n):
    assert n >= 3
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        out[i][i] += 1
        out[j][j] += 1
        out[i][j] -= 1
        out[j][i] -= 1
    return out


def graph_linear(n, coupling):
    return [[coupling * x - (i == j) for j, x in enumerate(row)]
            for i, row in enumerate(cycle_laplacian(n))]


def det_exact(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    answer = Q(1)
    n = len(a)
    for col in range(n):
        pivot_row = next((r for r in range(col, n) if a[r][col]), None)
        if pivot_row is None:
            return Q(0)
        if pivot_row != col:
            a[col], a[pivot_row] = a[pivot_row], a[col]
            answer = -answer
        pivot = a[col][col]
        answer *= pivot
        for r in range(col + 1, n):
            multiplier = a[r][col] / pivot
            for c in range(col + 1, n):
                a[r][c] -= multiplier * a[col][c]
            a[r][col] = Q(0)
    return answer


def residue(x, prime=3):
    x = Q(x)
    if x.denominator % prime == 0:
        raise ValueError("coefficient is not in Z_(3)")
    return x.numerator * pow(x.denominator, -1, prime) % prime


def det_mod(matrix, prime=3):
    a = [[residue(x, prime) for x in row] for row in matrix]
    answer = 1
    n = len(a)
    for col in range(n):
        pivot_row = next((r for r in range(col, n) if a[r][col]), None)
        if pivot_row is None:
            return 0
        if pivot_row != col:
            a[col], a[pivot_row] = a[pivot_row], a[col]
            answer = -answer
        pivot = a[col][col]
        answer = answer * pivot % prime
        for r in range(col + 1, n):
            multiplier = a[r][col] * pow(pivot, -1, prime) % prime
            for c in range(col + 1, n):
                a[r][c] = (a[r][c] - multiplier * a[col][c]) % prime
            a[r][col] = 0
    return answer % prime


def add_term(polynomial, monomial, coefficient):
    polynomial[monomial] = polynomial.get(monomial, Q(0)) + coefficient
    if not polynomial[monomial]:
        del polynomial[monomial]


def normal_form_factory(a, b, reverse=False):
    n = len(a)

    @lru_cache(None)
    def reduce_monomial(exponent):
        candidates = [i for i in range(n) if exponent[i] >= 3]
        if not candidates:
            return {exponent: Q(1)}
        i = candidates[-1] if reverse else candidates[0]
        rest = list(exponent)
        rest[i] -= 3
        out = {}
        replacements = [(tuple(rest), b[i])]
        for j in range(n):
            term = rest[:]
            term[j] += 1
            replacements.append((tuple(term), -a[i][j]))
        for monomial, coefficient in replacements:
            if coefficient:
                for e, c in reduce_monomial(monomial).items():
                    add_term(out, e, coefficient * c)
        return out

    def reduce_polynomial(polynomial):
        out = {}
        for exponent, coefficient in polynomial.items():
            for e, c in reduce_monomial(exponent).items():
                add_term(out, e, coefficient * c)
        return out

    return reduce_polynomial


def tiny_quotient_check():
    a = [[Q(-1), Q(1, 4)], [Q(1, 4), Q(-2)]]
    b = [Q(1, 1000), Q(-3, 1000)]
    normal = normal_form_factory(a, b)
    reversed_normal = normal_form_factory(a, b, reverse=True)
    # Compare alternative reductions of every monomial in this finite test box.
    comparisons = 0
    for exponent in product(range(9), repeat=2):
        assert normal({exponent: Q(1)}) == reversed_normal({exponent: Q(1)})
        comparisons += 1
    basis = list(product(range(3), repeat=2))
    # delta=(3x^2+a00)(3y^2+a11)-a01*a10.
    delta = {(2, 2): Q(9), (2, 0): 3*a[1][1], (0, 2): 3*a[0][0],
             (0, 0): a[0][0]*a[1][1]-a[0][1]*a[1][0]}
    multiplication = [[Q(0) for _ in basis] for _ in basis]
    index = {e: i for i, e in enumerate(basis)}
    for col, e in enumerate(basis):
        multiplied = {tuple(x+y for x, y in zip(e, f)): c for f, c in delta.items()}
        for f, c in normal(multiplied).items():
            multiplication[index[f]][col] = c
    scalar = det_mod(a)
    for r in range(9):
        for c in range(9):
            assert residue(multiplication[r][c]) == (scalar if r == c else 0)
    assert det_mod(multiplication) == pow(scalar, 9, 3)
    return {"variables": 2, "quotient_rank": 9,
            "alternative_monomial_reductions_compared": comparisons,
            "det_A_mod3": scalar, "det_multiplication_delta_mod3": det_mod(multiplication)}


def main():
    a13 = graph_linear(13, Q(1, 4))
    exact13 = det_exact(a13)
    assert exact13 == -Q(1, 4**12)
    assert det_mod(a13) == 2
    # Any integer numerator over 1000 is admissible, including multiples of 3.
    assert all(residue(Q(k, 1000)) == k % 3 for k in range(-20, 21))

    a12 = graph_linear(12, Q(1))
    assert det_exact(a12) == 0 and det_mod(a12) == 0
    kernel12 = [Q(x) for x in [2, 1, -1, -2, -1, 1] * 2]
    assert all(sum(row[j]*kernel12[j] for j in range(12)) == 0 for row in a12)

    a6 = graph_linear(6, Q(1, 3))
    assert det_exact(a6) == 0
    try:
        det_mod(a6)
        raise AssertionError("nonintegral coefficients were silently reduced")
    except ValueError:
        pass

    # The affine-term denominator assumption cannot be dropped in the general lemma.
    ac = [[Q(0), Q(1)], [Q(1), Q(3)]]
    bc = [Q(1, 27), Q(1, 3)]
    uc = [Q(1, 3), Q(0)]
    fc = [uc[i]**3 + sum(ac[i][j]*uc[j] for j in range(2))-bc[i] for i in range(2)]
    dc = [[ac[i][j] + (3*uc[i]**2 if i == j else 0) for j in range(2)] for i in range(2)]
    assert fc == [0, 0] and det_exact(dc) == 0 and det_mod(ac) == 2

    # Exactly nine roots of (x^3-x,y^3-y), all real and regular.
    toy_roots = list(product([-1, 0, 1], repeat=2))
    toy_indices = [(3*x*x-1)*(3*y*y-1) for x, y in toy_roots]
    assert len(toy_roots) == 9 and all(d != 0 for d in toy_indices)
    index_sum = sum(1 if d > 0 else -1 for d in toy_indices)
    assert index_sum == 1
    output = {
        "target": {"n": 13, "J": "1/4", "b_denominator": 1000,
                   "det_A_exact": str(exact13), "det_A_mod3": 2,
                   "distinct_complex_zero_count": 3**13,
                   "production_quotient_matrix_constructed": False},
        "degenerate_cycle": {"n": 12, "J": "1", "b": 0,
                             "det_DF_at_zero": "0", "kernel_vector": [str(x) for x in kernel12]},
        "nonintegral_J_cycle": {"n": 6, "J": "1/3", "b": 0,
                                "mod3_reduction_rejected": True, "det_DF_at_zero": "0"},
        "nonintegral_b_counterexample": {"A": [[str(x) for x in row] for row in ac],
                                         "b": [str(x) for x in bc], "root": [str(x) for x in uc],
                                         "det_A_mod3": 2, "det_DF_at_root": "0"},
        "tiny_quotient": tiny_quotient_check(),
        "toy_root_count": {"distinct_complex_and_real_roots": 9,
                           "known_strict_minima": 4, "extra_real_roots": 5, "sum_indices": index_sum},
        "scope": "Exact instance checks; general algebraic and degree proofs are in the candidate modular certificate."
    }
    destination = Path(__file__).with_name("modular_results.json")
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
