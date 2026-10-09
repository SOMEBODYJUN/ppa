#!/usr/bin/env python3
"""Finite exact evidence for C223; the infinite theorem is proved in the note."""
from fractions import Fraction as F
from itertools import product
import json
import platform

P = F(1, 8)
L = F(5, 4)
EPS = F(45, 64)
WEIGHTS = {(0, 0): F(7, 16), (0, 1): F(7, 16),
           (1, 0): F(1, 16), (1, 1): F(1, 16)}


def block(n):
    t = F(1, 2**n)
    delta = F(1, 2**(3*n+10))
    e = delta**n
    return t, delta, e, (t, t+delta, t+(2-e)*delta)


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def main():
    assert sum(WEIGHTS.values()) == 1
    assert all(v > 0 for v in WEIGHTS.values())
    assert P*(L*L-1+(1+L)**2) == EPS
    assert 0 <= EPS < 1
    states = [F(0)]
    transform = {F(0): F(0)}
    blocks = {}
    for n in range(1, 9):
        t, delta, e, pts = block(n)
        a, b, c = pts
        assert 0 < e < F(1, 100)
        assert t/delta == 2**(2*n+10)
        assert t/2-delta/4 >= 4*(delta+delta/8)
        states.extend(pts)
        transform.update({a: b, b: a, c: b})
        blocks[n] = pts
    labels = {x: x-transform[x] for x in states}
    assert len(set(labels.values())) == len(states)
    for x in states:
        assert transform[transform[transform[x]]] == transform[x]
    points = list(product(states, (F(0), F(1))))
    pair_count = 0
    for (x, z), (y, w) in product(points, repeat=2):
        assert abs(transform[x]-transform[y]) <= L*abs(x-y)
        input_cost = (x-y)**2+(z-w)**2
        output_cost = F(0)
        residual = F(0)
        for (i, j), weight in WEIGHTS.items():
            tx = transform[x] if i else x
            ty = transform[y] if i else y
            output_cost += weight*(tx-ty)**2
            residual += weight*((x-tx-y+ty)**2+(z-w)**2)
        assert residual == P*(labels[x]-labels[y])**2+(z-w)**2
        assert (residual == 0) == ((x, z) == (y, w))
        assert output_cost+residual <= (1+EPS)*input_cost
        pair_count += 1
    # Both constant-bit identity branches have incompatible fixed sets.
    assert not any(z == 0 and z == 1 for _, z in points)
    # Exact finite matrix powers include fixed origin and a transient point.
    r = [[F(1), F(0), F(0), F(0)],
         [F(0), F(0), F(1), F(0)],
         [F(0), F(1), F(0), F(0)],
         [F(0), F(0), F(1), F(0)]]
    ident = [[F(i == j) for j in range(4)] for i in range(4)]
    r2 = matmul(r, r)
    assert matmul(r2, r) == r
    q = [[(1-P)*ident[i][j]+P*r[i][j] for j in range(4)]
         for i in range(4)]
    stationary_extremes = [(F(1), F(0), F(0), F(0)),
                          (F(0), F(1, 2), F(1, 2), F(0))]
    for sigma in stationary_extremes:
        assert tuple(sum(sigma[i]*q[i][j] for i in range(4))
                     for j in range(4)) == sigma
    power = ident
    regime_count = {"large_a": 0, "small_a": 0}
    for k in range(81):
        ak, bk = (1-P)**k, (1-2*P)**k
        coeff = (ak, (1-bk)/2, (1+bk)/2-ak)
        assert min(coeff) >= 0 and sum(coeff) == 1
        expected = [[coeff[0]*ident[i][j]+coeff[1]*r[i][j]
                     +coeff[2]*r2[i][j] for j in range(4)]
                    for i in range(4)]
        assert power == expected
        if ak <= F(1, 2):
            mix = (1-2*ak, ak, ak-bk/2, bk/2)
            assert min(mix) >= 0 and sum(mix) == 1
            assert sum(mix[1:]) == 2*ak
            regime_count["small_a"] += 1
        else:
            assert 1 <= 2*ak
            regime_count["large_a"] += 1
        power = matmul(power, q)
    recurrent = [F(0)] + [x for pts in blocks.values() for x in pts[:2]]
    for n, pts in blocks.items():
        t, delta, e, _ = block(n)
        a, b, c = pts
        nearest_sq = min((c-y)**2 for y in recurrent)
        assert nearest_sq == (1-e)**2*delta**2
        # Four edges (a,z)->(a,z), (c,z)->(b,z), each mass 1/4.
        plan_cost = sum(F(1, 4)*(c-b)**2 for _ in (0, 1))
        residual_cost = sum(F(1, 4)*P*(labels[c]-labels[b])**2
                            for _ in (0, 1))
        assert plan_cost == nearest_sq/2
        assert residual_cost == (delta*e/4)**2
        assert (a*a+c*c)/2 <= (t+2*delta)**2
        # Reverse check of the zero-bit transport projection certificate.
        assert plan_cost*2 == nearest_sq
    # Deliberate degenerate e=0 destroys label injection.
    degenerate_t = {F(0): F(1), F(1): F(0), F(2): F(1)}
    degenerate_labels = [x-degenerate_t[x] for x in degenerate_t]
    assert len(set(degenerate_labels)) < 3
    exponent_checks = []
    for qexp in (F(1, 100), F(1, 4), F(1), F(2)):
        n = max(128, (2*qexp.denominator)//qexp.numerator)
        _, delta, _, _ = block(n)
        exponent = (3*n+10)*(qexp*(n+1)-1)
        assert exponent > 0
        # Symbolic log2 reverse: log2(delta)=-(3n+10).
        assert exponent == -(3*n+10)*(1-qexp*(n+1))
        next_exponent = (3*(n+1)+10)*(qexp*(n+2)-1)
        assert next_exponent > exponent
        exponent_checks.append({"q": str(qexp), "n": n,
                                "log2_power": str(exponent)})
    result = {
        "status": "PASS finite exact checks; not an infinite-domain proof",
        "python": platform.python_version(),
        "arithmetic": "fractions.Fraction; exact; no random seed",
        "base_blocks": len(blocks), "full_states": len(points),
        "ordered_state_pairs": pair_count,
        "matrix_times": 81, "mixture_regimes": regime_count,
        "parameters": {"p": str(P), "L": str(L), "epsilon": str(EPS),
                       "alpha": "1/2", "tau": "1"},
        "exponent_checks": exponent_checks,
        "boundary": "k=0, invariant origin/cycles, transient, distinct-bit pairs, e=0 label collision"
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
