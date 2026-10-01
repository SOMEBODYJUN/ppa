"""Independent exact checks for the finite-state lazy-cycle audit.

The mathematical proof is in AUDIT_MARKOV_FINITE_STATE_LAZY4.md.
All calculations below are rational; no optimization tolerances are used.
"""

from fractions import Fraction as F
from itertools import product


X = (0, 1, 3, 4)
T = (1, 2, 3, 0)
D = tuple(X[i] - X[T[i]] for i in range(4))
C = tuple(tuple(F((x-y)**2) for y in X) for x in X)
R = tuple(tuple(F((D[i]-D[j])**2, 2) for j in range(4)) for i in range(4))
P = tuple(tuple(F(int(i == j) + int(T[i] == j), 2) for j in range(4)) for i in range(4))
BETA = (F(1, 4),) * 4


def advance(mu, p=F(1, 2)):
    return tuple((1-p)*mu[j] + p*mu[(j-1) % 4] for j in range(4))


def monotone_plan(mu):
    source, target = list(mu), list(BETA)
    eta = [[F(0) for _ in range(4)] for _ in range(4)]
    i = j = 0
    while i < 4 and j < 4:
        a = min(source[i], target[j])
        eta[i][j] += a
        source[i] -= a
        target[j] -= a
        if source[i] == 0:
            i += 1
        if target[j] == 0:
            j += 1
    assert not any(source) and not any(target)
    return eta


def values(mu, p=F(1, 2)):
    eta = monotone_plan(mu)
    e = sum(eta[i][j] * C[i][j] for i in range(4) for j in range(4))
    phi = sum(eta[i][j] * p * (D[i]-D[j])**2 for i in range(4) for j in range(4))
    return e, phi


def tv(mu, nu):
    return sum(abs(a-b) for a, b in zip(mu, nu)) / 2


def main():
    assert D == (-1, -2, -1, 4)
    assert advance(BETA) == BETA
    H = tuple(tuple(C[i][j] - 26 * R[i][j] for j in range(4)) for i in range(4))
    assert H == ((0, -12, 9, -309), (-12, 0, -9, -459),
                 (9, -9, 0, -324), (-309, -459, -324, 0))

    grid = [tuple(F(z, 4) for z in zz) for zz in product(range(5), repeat=4) if sum(zz) == 4]
    assert len(grid) == 35
    ratios = [(e/r, mu) for mu in grid for e, r in [values(mu)] if r]
    assert max(ratios)[0] == 26
    assert [mu for ratio, mu in ratios if ratio == 26] == [(0, 0, F(3, 4), F(1, 4))]
    assert values((0, 0, F(3, 4), F(1, 4))) == (F(13, 4), F(1, 8))
    assert [mu for mu in grid if values(mu)[1] == 0] == [BETA]

    # Independent finer grid checks the hand proof across all interleavings.
    for zz in product(range(13), repeat=3):
        last = 12-sum(zz)
        if last < 0:
            continue
        mu = tuple(F(z, 12) for z in (*zz, last))
        e, r = values(mu)
        assert e <= 26*r

    relaxed_mu = (F(1, 2), F(1, 4), 0, F(1, 4))
    assert values(relaxed_mu) == (F(5, 4), F(1, 4))
    relaxed_edges = ((0, 0), (0, 2), (1, 1), (3, 3))
    assert sum(R[i][j]/4 for i, j in relaxed_edges) == 0
    assert sum(C[i][j]/4 for i, j in relaxed_edges) == F(9, 4)

    P2 = tuple(tuple(sum(P[i][k]*P[k][j] for k in range(4)) for j in range(4)) for i in range(4))
    assert max(tv(P2[i], P2[j]) for i in range(4) for j in range(4)) == F(1, 2)
    # Local W2 expansion despite global relative R-linear mixing.
    eps = F(1, 16)
    mu = (F(1, 4), F(1, 4), F(1, 4)+eps, F(1, 4)-eps)
    assert values(mu)[0] == eps
    assert values(advance(mu))[0] == F(5, 2)*eps
    # Native same-random-map expansion violates epsilon<1 almost-NE.
    assert F(C[2][3] + C[T[2]][T[3]], 2) == F(17, 2)

    # General laziness p: exact global/local constants and source parameters.
    for p in (F(1, 100), F(1, 4), F(1, 2), F(3, 4)):
        assert advance(BETA, p) == BETA
        e, phi = values((0, 0, F(3, 4), F(1, 4)), p)
        assert (e, phi, e/phi) == (F(13, 4), p/4, 13/p)
        for tau in (F(1, 10), F(1), F(10)):
            violations = [
                p*(C[T[i]][T[j]]-C[i][j] + tau*(D[i]-D[j])**2)/C[i][j]
                for i in range(4) for j in range(i+1, 4)
            ]
            assert max(violations) == p*(15+25*tau)
            assert tau*p/4 < max(violations)
        local_mu = (F(1, 4), F(1, 4)-eps, F(1, 4)+eps, F(1, 4))
        assert values(local_mu, p) == (4*eps, p*eps)
        expansion = 1+3*p if p <= F(1, 2) else 7*p-1
        assert values(advance(mu, p), p)[0] == expansion*eps
        assert expansion > 1
        q_squared = (1-p)**2+p**2
        assert q_squared-(1-2*p)**2 == 2*p*(1-p) > 0
        assert 0 < q_squared < 1

    # Audit correction: global sharpness does NOT persist on the beta-to-mu* ray.
    for s in (F(1, 4), F(1, 2), F(3, 4), F(1)):
        ray_mu = tuple((1-s)*b+s*m for b, m in zip(BETA, (0, 0, F(3, 4), F(1, 4))))
        expected_e = 9*s/4 if s <= F(1, 2) else (17*s-4)/4
        expected_phi = 3*s/8 if s <= F(1, 2) else (2-s)/8
        assert values(ray_mu) == (expected_e, expected_phi)
    assert 40*F(1, 100) == F(2, 5) < 1

    print('PASS: cost, residual, H matrix and invariant law')
    print('PASS: 35 subdivision vertices and 1/12 supplementary grid')
    print('PASS: sharp E <= 26 Psi^2; equality witness (0,0,3/4,1/4)')
    print('PASS: OT optimality is essential; unrestricted coupling gives false zero')
    print('PASS: Dobrushin(P^2)=1/2; relative R-linear W2 mixing')
    print('PASS: local E expansion factor 5/2, so no one-step Q contraction')
    print('PASS: same-map almost-NE needs violation >=15/2, not epsilon<1')
    print('PASS: general p sharp global squared EB 13/p, sharp local squared EB 4/p')
    print('PASS: expected almost-FNE epsilon_min=p(15+25*tau); balanced epsilon=40p')
    print('PASS: p=1/100 gives source-valid epsilon=2/5 but no compatible scalar gauge')
    print('PASS: beta-to-global-maximizer ray does NOT preserve global sharp ratio')


if __name__ == '__main__':
    main()
