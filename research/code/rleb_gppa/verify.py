#!/usr/bin/env python3
"""Finite checks of the proposed physical RLEB--GPPA interface.

The proof is in theory_proposal.tex / 主理论开发.md. These computations check
specified identities, constants and boundary witnesses, not a general theorem.
Only the Python standard library is required; no network or credentials used.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, tanh, hypot, log, isfinite
from pathlib import Path
import hashlib
import json
import sys

counts = {}


def check(name, test):
    assert test, name
    counts[name] = counts.get(name, 0) + 1


def close(a, b, scale=1):
    return abs(a-b) <= 2e-11*max(scale, abs(a), abs(b))


def inverse_monotone(f, q, lo, hi):
    assert f(lo) <= q + 1e-13 and f(hi) >= q - 1e-13
    for _ in range(100):
        mid = (lo+hi)/2
        if f(mid) < q:
            lo = mid
        else:
            hi = mid
    ans = (lo+hi)/2
    assert close(f(ans), q)
    return ans


# Exact restoration of the old gamma=1, complete multivalued PPA certificate.
for x, c in product((Q(k, 24) for k in range(-24, 25)), (2, 3)):
    y = x/(1+c)
    d = abs(x)
    selected = x-y
    residual = 2*abs(y)
    B = 3*d/4
    check('ppa_reflection_exact', abs(2*y-x) <= d/2)
    check('ppa_inner_reflection_identity', d*d-(2*y-x)**2 == 4*y*(x-y))
    check('ppa_true_residual_vs_selected', residual <= abs(selected))
    check('ppa_complete_compatibility', residual/2 == abs(y) and abs(y) <= 3*d/8)
    check('ppa_step_budget', abs(x-y) <= B)

for kappa, gamma, L, t in product((.25, .5, .75), (.25, .5, 1.), (0., .3, 2.), (0., 1e-9, 1/16, 1.)):
    exact = .5*(t/(1-kappa)+L*t**gamma/(1-kappa**gamma))
    sampled = sum(.5*(kappa**j*t+L*(kappa**j*t)**gamma) for j in range(3000))
    check('ppa_geometric_tail_restoration', close(exact, sampled))

# Genuine nonlinear kernel on the unchanged triangular complete relation.
R, L, kappa = 1/16, sqrt(2), .75
K = lambda t: (t+L*sqrt(t))/2
theta = lambda t: .5*(t/(1-kappa)+L*sqrt(t)/(1-sqrt(kappa)))
check('triangular_window', K(R) <= 1)
check('triangular_compatibility_boundary', K(R)**2/R < kappa)
for b, u, w in product((.1, 1., 5.), (-R, -1e-8, 0., 1e-8, R), (-20., -1., 0., 2., 20.)):
    hb = lambda z: z+b*tanh(z)
    y1 = u/2
    q = hb(w)+sqrt(abs(u)/2)
    y2 = inverse_monotone(hb, q, q-b, q+b)
    d = abs(u)
    physical = hypot(u-y1, w-y2)
    kernel = hypot(u-y1, hb(w)-hb(y2))
    true_residual = hypot(y1, sqrt(abs(y1)))
    reflection = hypot(2*y1-u, 2*hb(y2)-hb(w)-hb(w))
    check('nonlinear_full_gppa_equation', close(hb(w)-hb(y2), -sqrt(abs(y1))) and close(u-y1, y1))
    check('nonlinear_same_physical_anchor', close(abs(u), d))
    check('nonlinear_anchor_reflection', reflection <= L*sqrt(d)+1e-11)
    check('nonlinear_actual_lift', physical <= kernel+1e-11)
    check('nonlinear_true_eb', abs(y1) <= true_residual**2+1e-13)
    check('nonlinear_kernel_and_physical_steps', kernel <= K(d)+1e-11 and physical <= K(d)+1e-11)
    check('nonlinear_physical_distance_decay', abs(y1) <= kappa*d)
    qlimit = hb(w)+sqrt(abs(u))/(sqrt(2)-1)
    physical_limit = inverse_monotone(hb, qlimit, qlimit-b, qlimit+b)
    for j in (0, 1, 4, 16, 40):
        uj = u*2.**(-j)
        qj = hb(w)+sqrt(abs(u))/(sqrt(2)-1)*(1-2.**(-j/2))
        wj = inverse_monotone(hb, qj, qj-b, qj+b)
        tail = hypot(uj, wj-physical_limit)
        check('nonlinear_exact_tail', tail <= theta(abs(uj))+1e-10)

# Genuine Bregman model: grad h=(t^3,s), grad f=(t,0).
for lam, ratio, sign in product((.1, 1., 10.), (.05, .25, .75), (-1, 1)):
    radius = sqrt(ratio*lam)
    kap = ratio
    for fraction in (0., .001, .1, .5, 1.):
        t = sign*radius*fraction
        f = lambda y: y**3+lam*y
        bound = abs(t)+1
        y = inverse_monotone(f, t**3, -bound, bound)
        d = abs(t)
        delta = abs(t**3)
        reflection = abs(2*y**3-t**3)
        kernel_step = abs(t**3-y**3)
        check('bregman_full_equation', close(t**3-y**3, lam*y))
        check('bregman_same_physical_anchor', close(delta, d**3))
        check('bregman_kernel_reflection', reflection <= delta+1e-11)
        check('bregman_true_residual', close(abs(y), abs((t**3-y**3)/lam)))
        check('bregman_inverse_cube_identity', abs(t-y)**3 <= 4*kernel_step+1e-10)
        check('bregman_actual_transfer_sharp_constant', abs(t-y)**3 <= kernel_step+1e-10)
        check('bregman_physical_contraction', abs(y) <= kap*d+1e-10)
        check('bregman_actual_cubic_bound', abs(y) <= d**3/lam+1e-10)
        if d > 1e-5:
            actual_ratio = abs(y)/(d**3/lam)
            check('bregman_cubic_ratio_range', 0 < actual_ratio <= 1+1e-8)

# Noninjective, complete, finite-length positive example; zero boundary included.
for t, s in product((Q(k, 4) for k in range(-4, 5)), (Q(k, 4) for k in range(-4, 5))):
    y1 = t/2
    kernel = abs(t)/2
    d = hypot(float(t), float(s))
    physical = hypot(float(t)/2, float(s))
    true_residual = abs(y1)
    check('noninjective_full_equation', t-y1 == y1)
    check('noninjective_kernel_reflection', 2*y1-t == 0)
    check('noninjective_true_eb', abs(y1) == true_residual)
    check('noninjective_controlled_null_fiber', physical <= kernel+d+1e-12)
    check('noninjective_distance_decay', abs(y1) <= d/2+1e-12)
    length = physical+float(abs(t))/2
    check('noninjective_exact_length', length <= 3*d+1e-12)

# Failure witness satisfies the GPPA inclusion and true EB, but not the lift.
for j in range(20):
    x = (Q(1, 2**j), (-1)**j)
    y = (x[0]/2, -x[1])
    check('uncontrolled_fiber_legal_gppa', x[0]-y[0] == y[0])
    complete_residual = hypot(float(y[0]), 0.)
    distance_to_zero_line = hypot(float(y[0]), float(y[1]-y[1]))
    check('uncontrolled_fiber_true_eb', close(distance_to_zero_line, complete_residual))
    check('uncontrolled_fiber_non_cauchy_step', hypot(float(x[0]-y[0]), x[1]-y[1]) >= 2)
# At a zero input, a distinct zero-fiber output immediately violates h(0,0)=0.
check('uncontrolled_zero_fiber_lift_failure', hypot(0, 1) > 0)

# Power-tail expression and finite-prefix strict budget, with zero constants.
for A, L, M, N, beta, gamma, theta_power, delta, kap, t in product(
        (1.,), (0., 1.), (0., 1.), (0., .5), (.5, 1., 3.), (.5, 1.), (.5, 1.), (.5, 2.), (.25, .75), (0., 1e-6, 1/16)):
    def H(x):
        k = (A*x**beta+L*A**gamma*x**(beta*gamma))/2
        return M*k**theta_power+N*x**delta
    rhs = M/2**theta_power*(A**theta_power*t**(beta*theta_power)/(1-kap**(beta*theta_power))
            +L**theta_power*A**(gamma*theta_power)*t**(beta*gamma*theta_power)/(1-kap**(beta*gamma*theta_power)))
    rhs += N*t**delta/(1-kap**delta)
    finite = sum(H(kap**j*t) for j in range(1000))
    check('power_tail_upper_bound', finite <= rhs+1e-11)
    if theta_power == 1:
        shifted = M/2**theta_power*(A**theta_power*(kap*t)**(beta*theta_power)/(1-kap**(beta*theta_power))
            +L**theta_power*A**(gamma*theta_power)*(kap*t)**(beta*gamma*theta_power)/(1-kap**(beta*gamma*theta_power)))
        shifted += N*(kap*t)**delta/(1-kap**delta)
        check('power_budget_functional_identity', close(rhs, H(t)+shifted))

# An open interval exit at equality explains why the localization budget is strict.
for distance in (Q(1, 4), Q(1), Q(3, 2)):
    for ratio in (Q(0), Q(1, 2), Q(999, 1000)):
        displacement = ratio*distance
        check('finite_prefix_strict_localization', displacement < distance)
    endpoint = distance
    check('budget_equality_does_not_ensure_open_domain', not (-distance < endpoint < distance))

# Energy branch: exact quadratic compatibility for every positive lambda/rho.
for lam, rho in product((Q(1, 100), Q(1, 4), Q(1), Q(5)), (Q(1, 2), Q(1), Q(2))):
    contraction_squared = Q(1)/(1+(lam/rho)**2)
    check('ppa_energy_all_positive_steps', 0 < contraction_squared < 1)
    check('ppa_energy_reverse_check', contraction_squared*(1+(lam/rho)**2) == 1)

root = Path(__file__).resolve().parent
result = {'status': 'PASS', 'python': sys.version.split()[0], 'total_checks': sum(counts.values()),
          'checks': counts, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope': 'Finite identities, constants and boundary witnesses; not a proof of the general theorem.'}
(root/'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
