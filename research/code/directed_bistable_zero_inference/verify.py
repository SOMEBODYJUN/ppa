#!/usr/bin/env python3
"""Partial root discovery, exact certificates, and full-resolvent diagnostics.

The universal claims are proved in the candidate card. This script does not
enumerate all real roots, prove theorems from sampling, or benchmark all solvers.
"""
from fractions import Fraction as Q
from pathlib import Path
from time import perf_counter
import json
import platform
import numpy as np
import scipy
from scipy.optimize import root

N = 13
DEN = 10**12
B_NUMS = [-7, 4, 2, -3, 6, -5, 1, 8, -4, 3, -6, 5, -2]
B = [Q(k, 1000) for k in B_NUMS]
A, C = Q(7, 25), Q(11, 50)
D = [[Q(0) for _ in range(N)] for _ in range(N)]
for i in range(N):
    D[i][i] = A+C
    D[i][(i+1) % N] = -A
    D[i][(i-1) % N] = -C
dmat = np.array(D, dtype=float)
b = np.array(B, dtype=float)
RHO, EPS, MU = Q(1, 100), Q(1, 10**10), Q(1, 3)
DELTA, RADIUS = Q(1, 200), Q(1, 10000)

def f(z):
    return z**3-z+dmat@z-b

def jac(z):
    return np.diag(3*z*z-1)+dmat

def exact_f(z):
    return [z[i]**3-z[i]+sum(D[i][j]*z[j] for j in range(N))-B[i]
            for i in range(N)]

def exact_jac(z):
    return [[D[i][j]+(3*z[i]**2-1 if i == j else 0)
             for j in range(N)] for i in range(N)]

def matrix_inverse_det(a):
    n = len(a)
    u = [row[:]+[Q(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    det = Q(1)
    for j in range(n):
        k = next(k for k in range(j, n) if u[k][j])
        if k != j:
            u[k], u[j] = u[j], u[k]
            det = -det
        pivot = u[j][j]
        det *= pivot
        u[j] = [v/pivot for v in u[j]]
        for i in range(n):
            if i != j:
                c = u[i][j]
                u[i] = [v-c*w for v, w in zip(u[i], u[j])]
    inverse = [row[n:] for row in u]
    for i in range(n):
        for j in range(n):
            assert sum(a[i][k]*inverse[k][j] for k in range(n)) == int(i == j)
    return inverse, det

def ldl_positive(a):
    ell = [[Q(0) for _ in range(N)] for _ in range(N)]
    pivots = []
    for j in range(N):
        ell[j][j] = Q(1)
        pivot = a[j][j]-sum(ell[j][k]**2*pivots[k] for k in range(j))
        assert pivot > 0
        pivots.append(pivot)
        for i in range(j+1, N):
            ell[i][j] = (a[i][j]-sum(ell[i][k]*ell[j][k]*pivots[k]
                                   for k in range(j)))/pivot
    for i in range(N):
        for j in range(N):
            assert sum(ell[i][k]*pivots[k]*ell[j][k] for k in range(N)) == a[i][j]
    return pivots

def moddet(a):
    u = [[v.numerator*pow(v.denominator, -1, 3) % 3 for v in row] for row in a]
    det = 1
    for j in range(len(u)):
        k = next(k for k in range(j, len(u)) if u[k][j])
        if k != j:
            u[k], u[j] = u[j], u[k]
            det = -det
        pivot = u[j][j]
        det = det*pivot % 3
        for i in range(j+1, len(u)):
            c = u[i][j]*pow(pivot, -1, 3) % 3
            for k in range(j, len(u)):
                u[i][k] = (u[i][k]-c*u[j][k]) % 3
    return det % 3

def qs(x):
    return f'{x.numerator}/{x.denominator}'

def quantize(z):
    return [Q(int(round(float(v)*DEN)), DEN) for v in z]

def refine(z):
    for _ in range(8):
        dz = np.linalg.solve(jac(z), f(z))
        z = z-dz
        if np.linalg.norm(dz) < 1e-15:
            break
    return z

def stable_cert(z):
    c = quantize(z)
    assert max(map(abs, c)) <= Q(101, 100)
    j = exact_jac(c)
    symmetric = [[(j[i][k]+j[k][i])/2-(Q(2, 5) if i == k else 0)
                  for k in range(N)] for i in range(N)]
    pivots = ldl_positive(symmetric)
    res = exact_f(c)
    res_l1 = sum(map(abs, res))
    assert res_l1 < MU*EPS
    return c, {'center_numerators': [int(v*DEN) for v in c],
               'center_denominator': DEN, 'residual_l1': qs(res_l1),
               'root_error_bound': qs(res_l1/MU),
               'ldl_pivots_sym_DF_minus_two_fifths_I': [qs(v) for v in pivots]}

def negative_cert(z):
    c = quantize(refine(z))
    inv, det = matrix_inverse_det(exact_jac(c))
    assert det < 0
    rho = Q(1, 10**7)
    norm_inv = max(sum(map(abs, row)) for row in inv)
    diag_change = 3*(2*max(map(abs, c))*rho+rho*rho)
    contraction = norm_inv*diag_change
    res = exact_f(c)
    displacement = max(abs(sum(inv[i][j]*res[j] for j in range(N))) for i in range(N))
    assert contraction < Q(1, 2)
    assert displacement+contraction*rho < rho
    # The exact Banach map c+e -> c+e-BF(c+e) preserves this cube and
    # contracts it. The same inequality keeps DF invertible throughout.
    return c, {'center_numerators': [int(v*DEN) for v in c],
               'center_denominator': DEN, 'infinity_radius': qs(rho),
               'det_DF_center': qs(det), 'inverse_norm_infinity': qs(norm_inv),
               'contraction_upper_bound': qs(contraction),
               'center_newton_displacement': qs(displacement),
               'newton_invariance_bound': qs(displacement+contraction*rho),
               'certified_fixed_point_index': -1}

def prox(x, initial=None):
    if np.array_equal(x, -b):
        return np.zeros(N)
    rhs = x+b
    y0 = np.cbrt(rhs) if initial is None else initial
    h = lambda y: y**3+dmat@y-rhs
    dh = lambda y: np.diag(3*y*y)+dmat
    result = root(h, y0, jac=dh, tol=1e-12)
    y = result.x
    for _ in range(8):
        dy = np.linalg.solve(dh(y), h(y))
        y = y-dy
        if np.linalg.norm(dy) < 1e-14:
            break
    assert np.linalg.norm(h(y)) <= 2e-10*(1+np.linalg.norm(rhs))
    return y

def main():
    clock = perf_counter()
    rng = np.random.default_rng(20261013)
    stable = []
    discovery = perf_counter()
    for start in range(18):
        z = rng.choice([-1., 1.], N)
        # Euler proposals only discover roots. They are not the certified PPA.
        for _ in range(500):
            z = z-.2*f(z)
            if np.linalg.norm(f(z)) < 1e-8:
                break
        z = refine(z)
        if (np.linalg.norm(f(z)) < 1e-9 and
            np.linalg.eigvalsh((jac(z)+jac(z).T)/2)[0] > .4 and
            all(np.linalg.norm(z-w) > 1e-5 for w in stable)):
            stable.append(z)
    assert len(stable) == 16
    discovery_seconds = perf_counter()-discovery
    certification = perf_counter()
    stable_pairs = [stable_cert(z) for z in stable]
    centers = [c for c, _ in stable_pairs]
    separations = [sum((centers[i][k]-centers[j][k])**2 for k in range(N))
                   for i in range(16) for j in range(i)]
    assert min(separations) > 1
    assert Q(2, 5)-6*Q(101, 100)*RHO-3*RHO*RHO > MU
    assert DELTA+EPS < RHO
    assert 9*400 < 10*361  # 3/sqrt(10) < 19/20
    assert 20*RADIUS < DELTA-RADIUS
    linear = [[D[i][j]-int(i == j) for j in range(N)] for i in range(N)]
    assert moddet(linear) == 2
    cert_seconds = perf_counter()-certification

    # Prediction has already been obtained from the 16 local certificates.
    # This independent search checks 15 witnesses afterwards, not all zeros.
    rng = np.random.default_rng(20261014)
    negative = []
    for attempt in range(2000):
        z = root(f, rng.uniform(-1.4, 1.4, N), jac=jac, tol=1e-11).x
        if (np.linalg.norm(f(z)) < 1e-9 and np.linalg.det(jac(z)) < 0 and
            all(np.linalg.norm(z-w) > 1e-5 for w in negative)):
            negative.append(z)
        if len(negative) == 15:
            break
    assert len(negative) == 15
    negative_pairs = [negative_cert(z) for z in negative]
    neg_centers = [c for c, _ in negative_pairs]
    nr = Q(1, 10**7)
    for i, c in enumerate(neg_centers):
        assert all(max(abs(c[k]-d[k]) for k in range(N)) > 2*nr
                   for d in neg_centers[:i])
        # An infinity distance >.02 excludes all stable .005 physical tubes.
        assert all(max(abs(c[k]-d[k]) for k in range(N)) > Q(1, 50)
                   for d in centers)

    rng = np.random.default_rng(20261015)
    inputs = [np.zeros(N), -b, np.ones(N)*1.1, -np.ones(N)*1.1,
              np.ones(N)*1e6, np.linspace(-1e6, 1e6, N)]
    inputs += [rng.uniform(-1.1, 1.1, N) for _ in range(100)]
    max_reverse = 0.
    for x in inputs:
        y = prox(x)
        max_reverse = max(max_reverse, float(np.linalg.norm(y+f(y)-x)/(1+np.linalg.norm(x))))
    local_max_ratio = 0.
    for p in stable:
        for _ in range(20):
            direction = rng.normal(size=N)
            x = p+float(RADIUS)*rng.random()*direction/np.linalg.norm(direction)
            y = prox(x, p)
            t, q = np.linalg.norm(x-p), np.linalg.norm(y-p)
            assert np.linalg.norm(2*y-x-p) <= t+1e-10
            assert q <= 3*np.linalg.norm(f(y))+1e-10
            assert q <= .75*t+1e-10
            local_max_ratio = max(local_max_ratio, float(q/t))
    for t in [-1., -.01, 0., .01, 1.]:
        y = t*np.ones(N)
        x = -b+t**3*np.ones(N)
        assert np.linalg.norm(y+f(y)-x) < 1e-12
    # Beyond the critical coefficient the complete fiber contains at least
    # these three points, even for the same heterogeneous b.
    lam = 1.25
    x = -lam*b
    for t in [0., np.sqrt((lam-1)/lam), -np.sqrt((lam-1)/lam)]:
        y = t*np.ones(N)
        assert np.linalg.norm(y+lam*f(y)-x) < 1e-12
    data = {'scope': 'partial local certificates plus analytic global gates; no complete real-root enumeration',
            'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
            'model': {'n': N, 'forward_weight': qs(A), 'backward_weight': qs(C),
                      'bias_numerators': B_NUMS, 'bias_denominator': 1000, 'lambda': 1, 'kernel': 'identity'},
            'discovery': {'stable_starts': 18, 'stable_seed': 20261013,
                          'certified_stable_roots': 16, 'discovery_seconds': discovery_seconds,
                          'stable_certificate_seconds': cert_seconds,
                          'negative_seed': 20261014, 'negative_attempts': attempt+1,
                          'certified_negative_index_witnesses': 15},
            'uniform_RLEB': {'center_hessian_sym_margin': '2/5', 'rho': qs(RHO),
                             'root_center_error_bound': qs(EPS), 'mu': qs(MU),
                             'delta': qs(DELTA), 'R': qs(RADIUS), 'a': 't', 'omega': 't',
                             'h': 'q', 'psi': '3t', 'bar_t': 1, 'rho_energy': 'q',
                             'g': 'q/3', 'kappa': '3/sqrt(10)', 'Theta_upper_bound': '20t',
                             'strict_budget_left': qs(20*RADIUS), 'strict_budget_right': qs(DELTA-RADIUS)},
            'global': {'det_DF_constant_mod3': 2, 'total_fixed_point_index': 1,
                       'known_index': 16, 'unseen_index': -15,
                       'unseen_real_root_lower_bound': 15, 'unseen_real_count_parity': 'odd',
                       'complex_distinct_root_count': 3**N,
                       'complex_count_is_not_real_count_or_cost_lower_bound': True},
            'diagnostics': {'full_prox_inputs_tested': len(inputs), 'local_inputs_tested': 320,
                            'max_normalized_reverse_error': max_reverse,
                            'max_local_distance_ratio': local_max_ratio,
                            'zero_input_output_norm': float(np.linalg.norm(prox(np.zeros(N)))),
                            'critical_and_supercritical_complete_fiber_witnesses_checked': True},
            'stable_roots': [r for _, r in stable_pairs],
            'negative_index_witnesses': [r for _, r in negative_pairs],
            'total_seconds_including_optional_reverse_witness_search': perf_counter()-clock}
    out = Path(__file__).resolve().with_name('results.json')
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: data[k] for k in ['discovery', 'global', 'diagnostics']}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
