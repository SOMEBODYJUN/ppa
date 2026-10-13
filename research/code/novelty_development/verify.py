#!/usr/bin/env python3
"""Finite back-substitutions for the exact classical bridges, not priority proofs."""
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import platform

import numpy as np
import scipy
from scipy.optimize import root, brentq


def load_previous_helpers():
    path = Path(__file__).parents[1] / "structural_verification/verify.py"
    spec = importlib.util.spec_from_file_location("structural_helpers", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # does not call the old main or rerun its suite
    return module, path


def power_map(x, exponent):
    norm = np.linalg.norm(x)
    return np.zeros_like(x) if norm == 0 else norm**(exponent-1)*x


def spd_roots(a):
    vals, vecs = np.linalg.eigh(a)
    assert np.min(vals) > 0
    return (vecs*np.sqrt(vals)) @ vecs.T, (vecs/np.sqrt(vals)) @ vecs.T


def gram_v(z):
    return z @ z.T @ z


def gram_inverse(w):
    left, singular, right = np.linalg.svd(w, full_matrices=False)
    return (left*np.cbrt(singular)) @ right


def mixed_value(x, p, q):
    r, t = np.linalg.norm(x[:-1]), abs(x[-1])
    return (r**q+t**q)**(p/q)/p


def mixed_grad(x, p, q):
    r, t = np.linalg.norm(x[:-1]), abs(x[-1])
    if r == t == 0:
        return np.zeros_like(x)
    factor = (r**q+t**q)**((p-q)/q)
    return factor*np.r_[r**(q-2)*x[:-1], t**(q-2)*x[-1]]


def partial_dual_value(xi, ell, p, q):
    ps, qs = p/(p-1), q/(q-1)
    return (np.linalg.norm(xi)**qs+abs(ell)**qs)**(ps/qs)/ps


def partial_dual_grad(xi, ell, p, q):
    ps, qs = p/(p-1), q/(q-1)
    n, s = np.linalg.norm(xi), abs(ell)
    if n == 0:
        return np.zeros_like(xi)
    return (n**qs+s**qs)**((ps-qs)/qs)*n**(qs-2)*xi


def main():
    previous, helper_path = load_previous_helpers()
    out = {"scope": "finite checks; all-input/all-output claims are proved analytically",
           "python": platform.python_version(), "numpy": np.__version__,
           "scipy": scipy.__version__, "decimal_precision": 100,
           "binary_float": "IEEE binary64", "seed": "none; deterministic inputs",
           "numerical_absolute_tolerance": 2e-9}
    with localcontext() as context:
        context.prec = 100
        # Same leading rate does not identify two different proximal algorithms.
        comparison = []
        for m in (1, 2, 3, 5):
            for a in (D('0.1'), D('0.001')):
                bregman = previous.bisect_decimal(lambda r: r**m+r-a**m, D(0), a)
                centered = previous.bisect_decimal(lambda r: r-(a-r)**m, D(0), a)
                comparison.append({"m": m, "a": str(a),
                                   "bregman_output": str(bregman),
                                   "centered_power_output": str(centered),
                                   "same_output": bregman == centered,
                                   "bregman_ratio": str(bregman/a**m),
                                   "centered_ratio": str(centered/a**m)})
                assert m == 1 or bregman != centered
        out['different_algorithms'] = comparison
        # At least three valid roots: this is not a numerical full-fiber enumeration.
        kappa, radius, tangent_B = D('0.5'), D('0.1'), D('0.75')
        length_L = 1+kappa+tangent_B*kappa**2*radius
        abs_a = (1-kappa**2)/length_L**2
        abs_b = 2*kappa/(1-kappa)
        multiroot = []
        for a in (D(0), D('0.1'), D('-0.1'), D('0.001'), D('-0.001')):
            roots = previous.three_checked_outputs(a)
            for u, z in roots:
                step2 = (u-a)**2+z**2
                assert a*a-u*u+ D('1e-95') >= abs_a*step2
                assert 4*u*u <= abs_b**2*step2 + D('1e-95')
                old_f = previous.coefficient(D(0))*a*a/2
                new_f = previous.coefficient(z)*u*u/2
                # NG12's original f also has a local ABS descent certificate.
                f_a = (D('0.5')-radius**4)/length_L**2
                assert old_f-new_f+D('1e-95') >= f_a*step2
                residual = previous.c1_back_substitute(a, u, z)
                assert residual < D('1e-90')
                multiroot.append({"input_normal": str(a), "output": [str(u), str(z)],
                                  "relative_equation_residual": str(residual),
                                  "E_H1_margin": str(a*a-u*u-abs_a*step2),
                                  "E_H2_squared_margin": str(abs_b**2*step2-4*u*u),
                                  "original_f_H1_margin": str(old_f-new_f-f_a*step2)})
        out['C272_nonminimum_root_ABS_checks'] = multiroot

    matrix = np.array([[2., .5], [.5, 1.]])
    square, inverse_square = spd_roots(matrix)
    normal = []
    for m in (1, 2, 3, 5):
        for a in (np.zeros(2), np.array([.2, -.1]), np.array([-.2, .1]),
                  np.array([4., -2.])):
            lam = .7
            rhs = power_map(a, m)
            equation = lambda y: power_map(y, m)+lam*matrix@y-rhs
            solution = root(equation, a, options={'xtol': 1e-11})
            y = solution.x
            scale = max(1., np.linalg.norm(rhs))
            residue = np.linalg.norm(equation(y))/scale
            eta_in = inverse_square@rhs
            eta = inverse_square@power_map(y, m)
            grad = square@power_map(square@eta, 1/m)
            dual_residue = np.linalg.norm(eta+lam*grad-eta_in)/scale
            inverse_error = np.linalg.norm(power_map(square@eta, 1/m)-y)
            assert max(residue, dual_residue, inverse_error/scale) < 2e-9
            normal.append({'m': m, 'lambda': lam, 'input': a.tolist(), 'output': y.tolist(),
                           'original_scaled_residual': float(residue),
                           'dual_PPA_scaled_residual': float(dual_residue),
                           'physical_inverse_error': float(inverse_error)})
    out['C272_SPD_exact_dual_PPA'] = normal

    c = np.array([1., 0.])
    gram = []
    inputs = (np.zeros((2, 2)), np.column_stack((c, np.zeros(2))),
              np.array([[.4, .5], [-.2, .8]]), np.array([[5., -2.], [3., 4.]]),
              np.array([[1., .01], [.01, 0.]]))
    for z in inputs:
        for lam in (1., 10.):
            wz = gram_v(z)
            def equation(flat):
                y = flat.reshape((2, 2))
                f = np.column_stack((y[:, 0]-c, np.zeros(2)))
                return (gram_v(y)+lam*f-wz).ravel()
            if np.linalg.norm(z) == 0:
                r = brentq(lambda a: a**3+lam*a-lam, 0., 1., xtol=1e-14)
                y = np.array([[r, 0.], [0., 0.]])
            else:
                solution = root(equation, z.ravel(), options={'xtol': 1e-11})
                y = solution.x.reshape((2, 2))
            scale = max(1., np.linalg.norm(wz))
            original = np.linalg.norm(equation(y.ravel()))/scale
            wy = gram_v(y)
            recovered = gram_inverse(wy)
            eta, ell = wy[:, 0], wz[:, 1]
            grad = gram_inverse(np.column_stack((eta, ell)))[:, 0]-c
            dual = np.linalg.norm(eta+lam*grad-wz[:, 0])/scale
            fenchel = abs(.25*np.sum(np.linalg.svd(z, compute_uv=False)**4)
                          +.75*np.sum(np.linalg.svd(wz, compute_uv=False)**(4/3))
                          -np.sum(z*wz))/scale
            assert max(original, dual, fenchel, np.linalg.norm(recovered-y)/scale) < 2e-9
            gram.append({'lambda': lam, 'input': z.tolist(), 'output': y.tolist(),
                         'original_scaled_residual': float(original),
                         'dual_PPA_scaled_residual': float(dual),
                         'conserved_tangent_error': float(np.linalg.norm(wy[:, 1]-ell)),
                         'Fenchel_scaled_error': float(fenchel),
                         'SVD_physical_inverse_error': float(np.linalg.norm(recovered-y))})
    out['C273_full_slice_PPA'] = gram

    mixed = []
    for p, q in ((2., 4.), (3., 5.)):
        for initial in (np.array([.2, -.1, 1.]), np.array([-.2, .1, -1.]),
                        np.array([0., 0., 1.]), np.zeros(3), np.array([2., -1., 3.])):
            lam = .7
            rhs = mixed_grad(initial, p, q)
            def equation(y):
                return mixed_grad(y, p, q)+lam*np.r_[matrix@y[:-1], 0.]-rhs
            if np.linalg.norm(initial) == 0:
                y = np.zeros(3)
            else:
                solution = root(equation, initial, options={'xtol': 1e-11})
                y = solution.x
            scale = max(1., np.linalg.norm(rhs))
            wy = mixed_grad(y, p, q)
            ell = rhs[-1]
            eta_in, eta = inverse_square@rhs[:-1], inverse_square@wy[:-1]
            grad = square@partial_dual_grad(square@eta, ell, p, q)
            dual_error = np.linalg.norm(eta+lam*grad-eta_in)/scale
            inverse_error = np.linalg.norm(partial_dual_grad(wy[:-1], ell, p, q)-y[:-1])
            phi = mixed_value(y, p, q)-ell*y[-1]
            fenchel = abs(phi+partial_dual_value(wy[:-1], ell, p, q)-np.dot(wy[:-1], y[:-1]))
            original_error = np.linalg.norm(equation(y))/scale
            assert max(original_error, dual_error, inverse_error/scale, fenchel/scale) < 2e-9
            mixed.append({'p': p, 'q': q, 'lambda': lam, 'input': initial.tolist(),
                          'output': y.tolist(), 'ell': float(ell),
                          'original_scaled_residual': float(original_error),
                          'dual_PPA_scaled_residual': float(dual_error),
                          'partial_dual_inverse_error': float(inverse_error),
                          'partial_Fenchel_error': float(fenchel)})
    # Central p=2 is exactly linear: this is not a q-1 trajectory.
    a = np.array([.2, -.1])
    center_y = np.linalg.solve(np.eye(2)+.7*matrix, a)
    assert np.linalg.norm(mixed_grad(np.r_[center_y, 0.], 2., 4.)
                          +.7*np.r_[matrix@center_y, 0.]-np.r_[a, 0.]) < 1e-14
    out['C274_partial_dual_PPA'] = mixed
    out['C274_p2_center'] = {'input': a.tolist(), 'output': center_y.tolist(),
                            'algorithm': '(I+lambda A)^-1 a; ordinary linear PPA'}

    out['exact_rate_arithmetic'] = {
        'C272': [{'m': m, 'source_growth_nu': str(1+Q(1, m)),
                  'source_prox_p': 1, 'derived_order': str(1/(Q(1, m)))} for m in (2, 3, 5)],
        'C274_nonzero_leaf': [{'q': q, 'nu': str(Q(q, q-1)),
                              'derived_order': str(1/(Q(q, q-1)-1))} for q in (3, 4, 5)],
        'C274_center_gate': [{'p': str(p), 'nu': str(p/(p-1)),
                             'source_superlinear_gate': bool(1 > p/(p-1)-1)}
                            for p in (Q(3, 2), Q(2), Q(3))]}
    out['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out['helper_sha256'] = hashlib.sha256(helper_path.read_bytes()).hexdigest()
    path = Path(__file__).with_name('output.json')
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'normal_PPA_cases': len(normal),
                      'Gram_PPA_cases': len(gram), 'mixed_PPA_cases': len(mixed),
                      'checked_C1_outputs': len(multiroot), 'output': str(path)}, indent=2))


if __name__ == '__main__':
    main()
