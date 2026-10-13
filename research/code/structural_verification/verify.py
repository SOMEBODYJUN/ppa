#!/usr/bin/env python3
"""Finite arithmetic and inverse-equation checks; universal claims are analytic."""
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform

import numpy as np
from scipy.optimize import root


def bisect_decimal(fn, lo, hi, iterations=500):
    flo, fhi = fn(lo), fn(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    assert flo < 0 < fhi, (flo, fhi)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if mid == lo or mid == hi:
            break
        if fn(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def coefficient(z):
    z32 = abs(z) * abs(z).sqrt()
    return 2 - z32 / (1 + z32)


def normal_root(a, z):
    if a == 0:
        return D(0)
    sgn = D(1) if a > 0 else D(-1)
    aa = abs(a)
    return sgn * bisect_decimal(lambda u: u**3 + coefficient(z)*u-aa**3,
                               D(0), aa)


def three_checked_outputs(a):
    """At least three roots; this function does not enumerate the full fiber."""
    r = normal_root(a, D(0))
    if a == 0:
        return [(r, D(0))]
    def fn(t):
        u = normal_root(a, t*t)
        return t*(1+t**3)**2-D('0.75')*u*u
    t = bisect_decimal(fn, D(0), D('0.75')*a*a)
    u = normal_root(a, t*t)
    return [(r, D(0)), (u, t*t), (u, -t*t)]


def c1_back_substitute(a, u, z):
    e1 = u**3 + coefficient(z)*u-a**3
    az = D(0) if z == 0 else -D('1.5')*(D(1) if z > 0 else D(-1))*abs(z).sqrt()/(1+abs(z)*abs(z).sqrt())**2
    e2 = z+az*u*u/2
    s1 = max(abs(a)**3, D('1e-280'))
    s2 = max(abs(z), D('1e-280')) if z else D(1)
    return max(abs(e1)/s1, abs(e2)/s2)


def gram_v(z):
    return z @ z.T @ z


def scaled_native_gram(t, lam=1.):
    """Four exact rescaled equations avoid subtracting 1+O(t^2) from 1."""
    tau = abs(t)**(2/3)
    def eq(x):
        a2, e1, b1, d2 = x
        a = 1+t*t*a2
        s1 = a*b1+tau*e1*d2
        return np.array([
            a2*(a*a+a+1+lam)+a*e1*e1+s1*b1-2,
            (a*a+t*t*e1*e1+lam)*e1+tau*s1*d2-(1+t*t),
            s1*a+(t*t*b1*b1+tau*tau*d2*d2)*b1-(1+t*t),
            (tau*b1*b1+d2*d2)*d2+s1*e1-1,
        ])
    dlimit = (lam/(1+lam))**(1/3)
    initial = [(1-(1/(1+lam))**2)/(3+lam), 1/(1+lam), 1., dlimit]
    result = root(eq, initial, method='hybr', options={'xtol': 1e-11})
    assert np.max(np.abs(eq(result.x))) < 1e-10, result.message
    a2, e1, b1, d2 = result.x
    z = np.array([[1., t], [t, 0.]])
    y = np.array([[1+t*t*a2, t*b1], [t*e1, tau*d2]])
    f_y = np.column_stack((y[:, 0]-np.array([1., 0.]), np.zeros(2)))
    residual = gram_v(y)+lam*f_y-gram_v(z)
    error = float(np.linalg.norm(y-np.array([[1., 0.], [0., 0.]])))
    step = float(np.linalg.norm(y-z))
    energy = .5*(t*t-(y[0, 0]-1)**2-y[1, 0]**2)
    # Reconstructing 1+t^2*a2 in binary64 loses an O(eps) term, amplified by lam.
    # The polynomial rescaled equations above preserve this term without subtraction.
    raw_rounding_bound = 5e-13+4*np.finfo(float).eps*max(1., lam)
    assert np.max(np.abs(residual)) < raw_rounding_bound, (t, lam, residual.tolist())
    return {'t': t, 'D_over_t_2_3': float(d2), 'limit': dlimit,
            'scaled_residual': float(np.max(np.abs(eq(result.x)))),
            'full_equation_residual': float(np.max(np.abs(residual))),
            'raw_rounding_bound': float(raw_rounding_bound),
            'point_error_over_input': error/(np.sqrt(2)*t),
            'H1_ratio': energy/(step*step)}


def mixed_v(y, p=2., q=4.):
    u, z = y[:-1], y[-1:]
    r, t = np.linalg.norm(u), np.linalg.norm(z)
    if r == t == 0:
        return np.zeros_like(y)
    factor = (r**q+t**q)**((p-q)/q)
    return factor*np.r_[r**(q-2)*u, t**(q-2)*z]


def main():
    out = {'python': platform.python_version(), 'numpy': np.__version__,
           'decimal_precision': 100, 'bisection_iterations_max': 500,
           'scope': 'finite checks only; not a proof or full numerical fiber enumeration'}
    with localcontext() as ctx:
        ctx.prec = 100
        radius = Q(1, 4)
        ratio = radius**2+radius**8+Q(3, 4)*radius**5
        assert ratio == Q(4145, 65536) < Q(1, 4)
        out['flat_exact_certificate_ratio'] = str(ratio)
        checked = []
        worst = D(0)
        for a in map(D, ['0', '0.25', '-0.25', '0.01', '4']):
            roots = three_checked_outputs(a)
            for u, z in roots:
                res = c1_back_substitute(a, u, z)
                worst = max(worst, res)
                assert res < D('1e-90')
                assert abs(u)**3+abs(u) <= abs(a)**3+D('1e-90')
                assert abs(z) <= D('0.75')*u*u+D('1e-90')
            checked.append({'input_a': str(a), 'roots_checked': [[str(u), str(z)] for u, z in roots],
                            'not_full_fiber_enumeration': True})
        out['c1_multiroot_checks'] = checked
        out['c1_max_relative_backsubstitution'] = str(worst)
        r = normal_root(D('0.25'), D(0))
        z = r**4/D(100)
        subproblem_gap = z*z/2-r*r*z*z.sqrt()/(2*(1+z*z.sqrt()))
        assert subproblem_gap < 0
        out['central_root_nonminimum_gap'] = str(subproblem_gap)
        # Central-root policy is a valid full policy; it is not a global argmin.
        trajectory = []
        a = D('0.25')
        for _ in range(5):
            u = normal_root(a, D(0))
            trajectory.append({'u': str(a), 'next_over_cube': str(u/(a**3))})
            a = u
        out['nonminimizing_policy_cubic_ratios'] = trajectory
        # The remote fibers at zero input are exact algebraic identities.
        assert all(u**3+(u-2*u**3) == 0 for u in [-1, 0, 1])
        out['local_only_zero_fiber'] = [-1, 0, 1]
        r = D('.01')
        assert 2*r**6-r**4/4 < 0
        out['identity_reflection_counterexample_inner_product'] = str(2*r**6-r**4/4)
        # Same group for every unit nonzero data vector and m>=2.
        rr = D('1e-8')
        ll = 3*((1+rr)**2+1)
        eta = (1-rr)**2
        qlam = ll/D(10000)+ll/eta*(ll/D(10000)).sqrt()
        ch = (16*ll).sqrt().sqrt()
        theta = ch*rr.sqrt()/(1-D('.25').sqrt())
        assert qlam < D('.148') < D('.25')
        assert theta < D('.000627') < D('.5')
        out['native_gram_certificate'] = {'L': str(ll), 'eta': str(eta),
                                          'q_lambda': str(qlam), 'Theta_R': str(theta)}
        # Borderline cascade certificate fails while dynamics still contract.
        beta_critical = Q(1, 4)*Q(2)**2
        assert beta_critical == 1
        lam, qnorm = D(2), D('.25')
        t = D('1e-12')
        ratio_critical = ((t.sqrt()+(t+4*lam*lam*4*qnorm).sqrt())/(2*lam))**2
        assert ratio_critical > 1
        out['cascade_certificate_critical_ratio'] = str(ratio_critical)
    out['native_gram_sharp_witness'] = [scaled_native_gram(t, lam)
                                        for lam in [.1, 1., 10000.]
                                        for t in [-1e-4, 1e-2, 1e-4, 1e-6, 1e-10]]
    # Coupled normal SPD case, genuine mixed kernel; finite inverse checks.
    aa = np.array([[2., .5], [.5, 1.]])
    lam = .7
    x = np.array([.2, -.1, 1.4])
    initial_x = x.copy()
    p, q = 2., 4.
    r0, t0 = np.linalg.norm(x[:2]), abs(x[2])
    tangent_limit = t0*(1+(r0/t0)**q)**(-(q-p)/(q*(p-1)))
    steps = []
    for _ in range(3):
        vx = mixed_v(x)
        fn = lambda y: mixed_v(y)+lam*np.r_[aa@y[:2], 0.]-vx
        y = root(fn, np.r_[np.zeros(2), tangent_limit], tol=1e-11).x
        assert np.linalg.norm(fn(y)) < 1e-11
        assert np.linalg.norm(y[:2]) <= np.linalg.norm(x[:2])+1e-12
        assert abs(y[2]) <= abs(x[2])+1e-12
        steps.append({'normal': float(np.linalg.norm(y[:2])), 'tangent': float(y[2]),
                      'backsubstitution': float(np.linalg.norm(fn(y)))})
        x = y
    out['mixed_power_coupled_inverse'] = {'input': initial_x.tolist(),
                                         'explicit_tangent_limit': tangent_limit, 'steps': steps}
    # Center p=2 is exactly ordinary PPA rather than cubic.
    x0 = np.array([.2, -.1, 0.])
    y0 = np.r_[np.linalg.solve(np.eye(2)+lam*aa, x0[:2]), 0.]
    center_error = float(np.linalg.norm(mixed_v(y0)+lam*np.r_[aa@y0[:2], 0.]-mixed_v(x0)))
    assert center_error < 1e-14
    out['mixed_power_center_linear_identity_error'] = center_error
    out['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    target = Path(__file__).with_name('output.json')
    target.write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({'status': 'PASS', 'output': str(target),
                      'c1_relative_residual': out['c1_max_relative_backsubstitution'],
                      'native_gram_q': out['native_gram_certificate']['q_lambda'],
                      'finite_native_witnesses': len(out['native_gram_sharp_witness'])}, indent=2))


if __name__ == '__main__':
    main()
