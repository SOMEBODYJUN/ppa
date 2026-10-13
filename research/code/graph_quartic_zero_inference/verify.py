#!/usr/bin/env python3
"""Find finitely many minima; certify only selected points, using exact rationals.

This is not a root enumeration and does not assert that all minima were found.
Run from the repository: python research/code/graph_quartic_zero_inference/verify.py
Only NumPy/SciPy and Python's standard library are used.
"""

from fractions import Fraction as Q
from pathlib import Path
from time import perf_counter
import argparse
import json
import platform

import numpy as np
import scipy
from scipy.optimize import minimize


N = 13
SEED = 20261013
DEFAULT_START_COUNT = 17
DEFAULT_SELECT_COUNT = 16
DEN = 10**12
J = Q(1, 4)
B_NUMS = [-7, 4, 2, -3, 6, -5, 1, 8, -4, 3, -6, 5, -2]
B = [Q(k, 1000) for k in B_NUMS]
RHO = Q(1, 100)
DELTA = Q(1, 200)
M = Q(2, 5)
EPSILON = Q(1, 10**10)
R = Q(1, 10000)
SUP_Z = Q(101, 100)
CENTER_MARGIN = Q(1, 2)
OUT = Path(__file__).resolve().with_name('results.json')

L = 2*np.eye(N) - np.roll(np.eye(N), 1, axis=0) - np.roll(np.eye(N), -1, axis=0)
b = np.array(B_NUMS, dtype=float)/1000


def energy(u):
    return float(np.sum((u*u-1)**2)/4 + float(J)/2*u@L@u - b@u)


def gradient(u):
    return u**3-u+float(J)*L@u-b


def hessian(u):
    return np.diag(3*u*u-1)+float(J)*L


def exact_f(z):
    return [z[i]**3-z[i]+J*(2*z[i]-z[(i-1) % N]-z[(i+1) % N])-B[i]
            for i in range(N)]


def exact_hessian(z, shift=Q(0)):
    a = [[Q(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        a[i][i] = 3*z[i]**2-1+2*J-shift
        a[i][(i-1) % N] = -J
        a[i][(i+1) % N] = -J
    return a


def exact_ldl(a):
    """Symmetric no-pivot LDL^T; strict positivity of every D certifies SPD."""
    n = len(a)
    ell = [[Q(0) for _ in range(n)] for _ in range(n)]
    diagonal = []
    for j in range(n):
        ell[j][j] = Q(1)
        d = a[j][j] - sum(ell[j][k]**2*diagonal[k] for k in range(j))
        assert d > 0, (j, d)
        diagonal.append(d)
        for i in range(j+1, n):
            ell[i][j] = (a[i][j] - sum(ell[i][k]*ell[j][k]*diagonal[k]
                                     for k in range(j)))/d
    # Reconstruction is an exact additional check, independent of float spectra.
    for i in range(n):
        for j in range(n):
            assert sum(ell[i][k]*diagonal[k]*ell[j][k] for k in range(n)) == a[i][j]
    return diagonal


def rational(q):
    return f'{q.numerator}/{q.denominator}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--starts', type=int, default=DEFAULT_START_COUNT,
                        help='number of numerical local solves (default: 17)')
    parser.add_argument('--select', type=int, default=DEFAULT_SELECT_COUNT,
                        help='number of first distinct candidates to certify (default: 16)')
    args = parser.parse_args()
    start_count, select_count = args.starts, args.select
    assert 0 < select_count <= start_count
    t_all = perf_counter()
    rng = np.random.default_rng(SEED)
    candidates = []
    attempts = []
    t_solve = perf_counter()
    for k in range(start_count):
        initial = rng.choice([-1., 1.], N)
        result = minimize(energy, initial, jac=gradient, hess=hessian,
                          method='trust-exact', options={'gtol': 1e-11, 'maxiter': 100})
        z = result.x.copy()
        newton_steps = 0
        for _ in range(8):
            step = np.linalg.solve(hessian(z), gradient(z))
            z -= step
            newton_steps += 1
            if np.linalg.norm(step) < 1e-15:
                break
        residual = float(np.linalg.norm(gradient(z)))
        eig_min = float(np.linalg.eigvalsh(hessian(z))[0])
        accepted = residual < 1e-10 and eig_min > 0
        unique = accepted and all(np.linalg.norm(z-w['z']) > 1e-5 for w in candidates)
        attempts.append({'start': k, 'iterations': int(result.nit),
                         'newton_steps': newton_steps, 'accepted_numeric': bool(accepted),
                         'new_candidate': bool(unique)})
        if unique:
            candidates.append({'z': z, 'start': k, 'energy': energy(z),
                               'residual_numeric': residual, 'hessian_min_numeric': eig_min})
    solve_seconds = perf_counter()-t_solve
    assert len(candidates) >= select_count, 'not enough distinct numerical candidates; increase --starts'

    # Quantization to rational centers is followed by exact checks, not tolerance tests.
    selected = candidates[:select_count]
    exact_centers = [[Q(int(round(float(u)*DEN)), DEN) for u in c['z']]
                     for c in selected]
    variation = 6*SUP_Z*RHO+3*RHO**2
    assert CENTER_MARGIN-variation > M
    assert DELTA+EPSILON < RHO
    records = []
    t_cert = perf_counter()
    for i, (candidate, z) in enumerate(zip(selected, exact_centers)):
        assert max(map(abs, z)) <= SUP_Z
        assert min(map(abs, z)) > EPSILON
        pivots = exact_ldl(exact_hessian(z, CENTER_MARGIN))
        residual = exact_f(z)
        residual_l1 = sum(map(abs, residual))
        assert residual_l1 < M*EPSILON
        records.append({
            'id': i+1, 'discovery_start': candidate['start'],
            'sign_pattern': ''.join('+' if u > 0 else '-' for u in z),
            'center_numerators': [int(u*DEN) for u in z],
            'center_denominator': DEN,
            'exact_f': [rational(u) for u in residual],
            'exact_f_l1': rational(residual_l1),
            'exact_error_bound_l1_over_m': rational(residual_l1/M),
            'ldl_pivots_for_hessian_minus_half_I': [rational(p) for p in pivots],
            'ldl_min_pivot_numeric': float(min(pivots)),
            'energy_numeric': candidate['energy'],
            'hessian_min_numeric': candidate['hessian_min_numeric'],
            'residual_norm_numeric': candidate['residual_numeric'],
        })
    squared_separations = [sum((exact_centers[i][k]-exact_centers[j][k])**2
                              for k in range(N))
                           for i in range(select_count) for j in range(i)]
    min_sep_squared = min(squared_separations) if squared_separations else None
    if min_sep_squared is not None:
        assert min_sep_squared > 1
    # The irrational energy factor is below 15/16 by this integer inequality.
    assert 25*256 < 29*225
    assert 16*R < DELTA-R
    cert_seconds = perf_counter()-t_cert

    data = {
        'scope': 'finite numerical discovery followed by exact local certificates; not full root enumeration',
        'model': {'dimension': N, 'graph': 'cycle C_13', 'J': rational(J),
                  'b_numerators': B_NUMS, 'b_denominator': 1000, 'lambda': 1, 'kernel': 'identity'},
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                        'scipy': scipy.__version__},
        'search': {'seed': SEED, 'initial_local_solves': start_count,
                   'numeric_distinct_minimum_candidates': len(candidates),
                   'selected_exact_certified_minima': select_count,
                   'selected_first_discovery_starts': [c['start'] for c in selected],
                   'local_solver': 'scipy.optimize.minimize trust-exact + at most 8 Newton refinement steps',
                   'numerical_discovery_seconds': solve_seconds,
                   'exact_certificate_seconds': cert_seconds,
                   'total_seconds': perf_counter()-t_all,
                   'nominal_total_degree_homotopy_path_count': 3**N,
                   'path_count_comparison_scope': 'operation-count reference only; not a runtime benchmark or a lower bound',
                   'attempts': attempts},
        'uniform_certificate': {
            'center_infinity_bound': rational(SUP_Z), 'center_hessian_strict_lower_margin': rational(CENTER_MARGIN),
            'center_ball_radius': rational(RHO), 'hessian_variation_upper_bound': rational(variation),
            'local_hessian_lower_bound_m': rational(M), 'root_center_error_strict_bound': rational(EPSILON),
            'target_ball_radius_delta': rational(DELTA), 'input_distance_R': rational(R),
            'min_center_separation_squared': rational(min_sep_squared) if min_sep_squared is not None else None,
            'min_center_separation_numeric': float(min_sep_squared)**.5 if min_sep_squared is not None else None,
            'C250_kappa': '5/sqrt(29)', 'C250_kappa_numeric': 5/np.sqrt(29),
            'C250_length_coefficient_numeric': 1/(1-5/np.sqrt(29)),
            'rational_kappa_upper_bound': '15/16', 'rational_length_upper_bound': '16 t',
            'strict_uniform_budget_16R': rational(16*R), 'distance_to_U_complement_lower_bound_delta_minus_R': rational(DELTA-R),
            'direct_local_distance_factor': '5/7', 'C249_direct_gate': 'fails for the selected L=1, psi=5t/2 constants',
            'C254_scope': 'not an instance of the original global sublinear reflection hypothesis'},
        'minima': records,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({
        'numeric_candidates': len(candidates), 'exact_certified_minima': select_count,
        'local_solves': start_count, 'discovery_seconds': solve_seconds,
        'certificate_seconds': cert_seconds,
        'min_selected_numeric_hessian_eigenvalue': min(c['hessian_min_numeric'] for c in selected),
        'max_exact_error_bound': max(float(Q(c['exact_error_bound_l1_over_m'])) for c in records),
        'min_center_separation': float(min_sep_squared)**.5 if min_sep_squared is not None else None,
        'output': str(OUT),
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
