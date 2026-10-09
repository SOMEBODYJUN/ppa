#!/usr/bin/env python3
"""Fixed p=7/4 complete-PPA certificate arithmetic and genuine 2D trajectories.

Run from any directory: python3 research/code/sparse_regularity/sharp_dynamics_verify.py
Only Python's standard library is used. Exact Fraction inequalities certify the
displayed numerical constants; finite trajectories corroborate but do not prove
the analytic universal statements in sharp_instance_dynamics.md. In particular,
global output exclusion and global-proximal equality are proved there, not by a
numerical search for other stationary points.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from math import sqrt
from pathlib import Path
import json
import platform
import time


def binomial(p, n):
    value = F(1)
    for j in range(n):
        value *= (p-j)/(j+1)
    return value


def symmetric_series(p, degree=12):
    inner = [binomial(p, n) if n and n % 2 == 0 else F(0)
             for n in range(degree+1)]
    out = [F(1)] + [F(0)]*degree
    term = out[:]
    for j in range(1, degree+1):
        term = [sum(term[k]*inner[n-k] for k in range(n+1))
                for n in range(degree+1)]
        for n in range(degree+1):
            out[n] += binomial(1/p, j)*term[n]
    return out


def exact_certificate():
    r = F(7, 8)
    v = F(1, 196)
    delta = F(21, 32)*r*r + F(35, 2048)*r**4/(1-r*r)
    majorants = [2/r**6/(1-v),
                 2/r**6*(6/(1-v)+2*v/(1-v)**2),
                 2/r**6*(30/(1-v)+26*v/(1-v)**2+8*v*v/(1-v)**3)]
    assert delta == F(214375, 393216) < 1
    assert all(a < b for a, b in zip(majorants, [5, 28, 140]))
    bracket = F(95, 1024)-F(11, 8192)-(28+F(5, 32))/961
    assert bracket > F(1, 32)
    comparison = (2*F(9, 64)**2 + F(33, 32)**4)/64
    assert comparison < F(1, 32)
    tangent_bound = (F(3, 124) + F(11, 64*32**2)*F(32, 31)**3
                     + F(28, 32**4)*F(32, 31)**5)
    assert tangent_bound < F(1, 32)
    assert F(3, 7)+F(3, 64)+F(5, 2) < 3
    assert F(7, 5)**7 < 16 < F(3, 2)**7
    assert F(10, 7)**2 > 2 and F(15, 14)**14 > 2
    assert 25 < 32  # 5 < 4 sqrt(2): output coordinates < 1/32.
    coefficients = symmetric_series(F(7, 4))
    assert coefficients[2] == F(3, 8)
    assert coefficients[4] == -F(11, 256)
    radial = -F(3, 32)
    quartic = 2*radial**2+F(3, 8)*radial+F(11, 256)
    assert quartic == F(13, 512)
    tangent_cubic = F(3, 4)*radial+F(11, 64)
    assert tangent_cubic == 4*quartic == F(13, 128)
    return {
        'analytic_disk': str(r), 'G_minus_one_majorant': str(delta),
        'E_Eprime_Edoubleprime_majorants': list(map(str, majorants)),
        'star_square_quartic_lower_coefficient': str(bracket),
        'star_comparison_required_less_than_1_32': str(comparison),
        'tangent_factor_derivative_majorant': str(tangent_bound),
        'symmetric_norm_series': {str(k): str(v) for k, v in enumerate(coefficients) if v},
        'radial_quadratic_coefficient': str(radial),
        'reduced_quartic_over_R': str(quartic),
        'actual_tangent_cubic_after_tracking_over_R': str(tangent_cubic),
        'all_exact_checks_passed': True,
    }


# The same two-variable formulas support float trajectories and independent
# 50/80-digit Decimal checks. No point is projected onto the critical curve.
def fields(h, t, R, one, power):
    s = one+h
    u = t/s
    p = 7*one/4
    exponent = 4*one/7
    plus, minus = one+u, one-u
    G = (power(plus, p)+power(minus, p))/2
    Gp = p*(power(plus, p-one)-power(minus, p-one))/2
    Gpp = p*(p-one)*(power(plus, p-2*one)+power(minus, p-2*one))/2
    f = power(G, exponent)
    fp = exponent*power(G, exponent-one)*Gp
    fpp = (exponent*(exponent-one)*power(G, exponent-2*one)*Gp*Gp
           + exponent*power(G, exponent-one)*Gpp)
    gh = R*(4*h-(f-one-u*fp))
    gt = R*(3*t/4-fp)
    Hhh = R*(4-u*u*fpp/s)
    Hht = R*u*fpp/s
    Htt = R*(3*one/4-fpp/s)
    return gh, gt, Hhh, Hht, Htt


def proximal_step(old_h, old_t, lam, R, one, power, tolerance):
    h, t = old_h, old_t
    for iteration in range(12):
        gh, gt, Hhh, Hht, Htt = fields(h, t, R, one, power)
        a = one+lam*Hhh/2
        b = lam*Hht/2
        d = one+lam*Htt/2
        rh = h+lam*gh/2-old_h
        rt = t+lam*gt/2-old_t
        determinant = a*d-b*b
        assert determinant > 0
        dh = (d*rh-b*rt)/determinant
        dt = (a*rt-b*rh)/determinant
        h -= dh
        t -= dt
        if abs(dh)+abs(dt) < tolerance:
            break
    else:
        raise AssertionError('2D Newton iteration did not converge')
    gh, gt, *_ = fields(h, t, R, one, power)
    residual = max(abs(h+lam*gh/2-old_h), abs(t+lam*gt/2-old_t))
    assert residual < 10*tolerance
    return h, t, residual


def floating_trajectory(initial_h, initial_t, steps=100000):
    one = 1.0
    R = 2.0**(4.0/7.0)
    lam = 1.0/128
    h, t = initial_h, initial_t
    assert sqrt(2*(h*h+t*t)) <= 1.0/64
    slope_target = 13*lam*R/128
    norm_target = 16/sqrt(13*lam*R)
    checkpoints = {0, 100, 1000, 10000, steps}
    traces = []
    largest_residual = 0.0
    previous_norm = sqrt(2*(h*h+t*t))
    inverse_anchor = None
    for k in range(steps+1):
        if k == 1000:
            inverse_anchor = t**-2 if t else None
        if k in checkpoints:
            traces.append({
                'k': k, 'h': h, 't': t,
                'h_over_t2': h/(t*t) if t else None,
                'sqrt_k_distance': sqrt(k)*sqrt(2*(h*h+t*t)),
                'sqrt_k_distance_proved_limit': norm_target,
                'post_transient_inverse_square_slope':
                    (t**-2-inverse_anchor)/(k-1000)
                    if t and inverse_anchor is not None and k > 1000 else None,
                'inverse_square_slope_proved_limit': slope_target,
            })
        if k == steps:
            break
        h, t, residual = proximal_step(h, t, lam, R, one, pow, 2e-16)
        largest_residual = max(largest_residual, residual)
        norm = sqrt(2*(h*h+t*t))
        assert norm <= previous_norm+2e-14
        assert norm <= 1.0/64+2e-14
        previous_norm = norm
        if initial_t:
            assert t*initial_t > 0
    if initial_t:
        assert abs(h/(t*t)+3.0/32) < 2e-4
        measured = (t**-2-inverse_anchor)/(steps-1000)
        assert abs(measured/slope_target-1) < 0.004
    return {'initial_h': initial_h, 'initial_t': initial_t, 'steps': steps,
            'largest_proximal_coordinate_residual': largest_residual,
            'checkpoints': traces}


def decimal_check(precision):
    with localcontext() as ctx:
        ctx.prec = precision
        one = D(1)
        power = lambda value, exponent: (value.ln()*exponent).exp()
        R = power(D(2), D(4)/7)
        lam = one/128
        t = one/1000
        h = -3*t*t/32
        tol = D(10)**(-precision+8)
        start_inverse = one/(t*t)
        largest_residual = D(0)
        for _ in range(300):
            h, t, residual = proximal_step(h, t, lam, R, one, power, tol)
            largest_residual = max(largest_residual, residual)
        measured = (one/(t*t)-start_inverse)/300
        target = 13*lam*R/128
        assert abs(h/(t*t)+D(3)/32) < D('0.000002')
        assert abs(measured/target-1) < D('0.0001')
        # The geometric axis is checked by the same genuine two-variable solver.
        axis_h, axis_t = one/256, D(0)
        for _ in range(30):
            axis_h, axis_t, _ = proximal_step(axis_h, axis_t, lam, R, one, power, tol)
        expected_h = (one/256)/(one+2*lam*R)**30
        assert axis_t == 0 and abs(axis_h-expected_h) < 100*tol
        return {
            'precision_digits': precision, 'steps': 300,
            'h_over_t2': str(h/(t*t)),
            'inverse_square_slope': str(measured), 'proved_slope_limit': str(target),
            'relative_slope_difference': str(measured/target-one),
            'largest_proximal_coordinate_residual': str(largest_residual),
            'axis_steps': 30, 'axis_formula_error': str(abs(axis_h-expected_h)),
        }


def main():
    start = time.monotonic()
    output = {
        'python': platform.python_version(),
        'arithmetic': 'Fraction exact; float genuine 2D iterations; Decimal 50/80 digit repetitions',
        'seed': None, 'p': '7/4', 'lambda': '1/128', 'input_radius': '1/64',
        'exact_certificate': exact_certificate(),
        'decimal_checks': [decimal_check(50), decimal_check(80)],
        'floating_trajectories': [
            floating_trajectory(1.0/256, 1.0/100),
            floating_trajectory(-1.0/256, -1.0/100),
            floating_trajectory(0.0, 1.0/100),
        ],
        'scope': ('Finite exact arithmetic and actual two-variable PPA trajectory checks. '
                  'The norm-limit value is analytic: the finite raw sqrt(k) distances '
                  'remain far from it because the certified step and input scale have a '
                  'long transient. The post-transient reciprocal-square slopes check '
                  'the asymptotic drift without claiming a finite run proves the limit. '
                  'Complete-fiber uniqueness and global proximal equality are proved '
                  'in research/topics/sparse_recovery/sharp_instance_dynamics.md.'),
    }
    output['elapsed_seconds'] = time.monotonic()-start
    path = Path(__file__).with_name('sharp_dynamics_results.json')
    path.write_text(json.dumps(output, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({'saved': str(path), 'all_checks_passed': True,
                      'elapsed_seconds': output['elapsed_seconds']}))


if __name__ == '__main__':
    main()
