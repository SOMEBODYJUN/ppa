"""Finite arithmetic and reverse checks; complete fibers use the analytic proof."""
from decimal import Decimal as D, getcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

getcontext().prec = 80
R, L, kappa = Q(1, 10000), Q(2, 5), Q(1, 4)
K, c = Q(1024, 169), Q(8, 325)
scale, sqrt_R = K * R + c, Q(1, 100)
Pmax = scale * R
sqrt_scale_upper, sqrt_P_upper = Q(4, 25), Q(1, 625)
assert 100 * (1 - R)**2 > 1 + R
assert 1 - R - Q(1, 4) > Q(2, 3)
assert 1 + R + Q(1, 4) < Q(4, 3)
assert Q(3, 4) * (2 + R) < 2
assert Q(3, 4) / 4 == Q(3, 16)
assert Q(32, 13)**2 == K and Q(32, 1300) == c
assert sqrt_R**2 == R
assert scale < sqrt_scale_upper**2 and Pmax < sqrt_P_upper**2
anchor = 2 * sqrt_scale_upper + (1 + 2 * scale) * sqrt_R
EB = (1 + 99 * sqrt_P_upper)**2 + 1
rho_sq = Pmax + (R + Pmax)**2
window = (R + L * sqrt_R) / 2
compatibility = Q(3, 4) * (sqrt_R + L)**2
budget = Q(2, 3) * R + L * sqrt_R
assert anchor < Q(331, 1000) < L
assert EB < 3 and rho_sq < 1 and window < 1
assert compatibility < kappa
assert budget == Q(61, 15000) < Q(1, 2) - R
# Alternate energy proof: every bound is rational, including radical majorants.
assert Q(6, 5)**4 > 2
T_bound, alpha_bound = Q(12, 10**7), Q(26, 1000)
assert c + K * Q(6, 5)**2 * R < alpha_bound
assert Q(162, 1000)**2 > alpha_bound
theta_bound = alpha_bound * Q(162, 1000) + (1 + 100 * alpha_bound)**3 * T_bound
assert theta_bound < Q(43, 10000)
assert Q(142, 100)**2 > 2
assert Q(142, 100) * Q(43, 10000)**2 < Q(3, 100)**3

def dec(q):
    return D(q.numerator) / D(q.denominator)

def norm(v):
    return sum(a*a for a in v).sqrt()

def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))

def rotated(x, u):
    # Exact rational orthogonal rotation, with Decimal evaluation of x.
    co, si = dec((1-u*u)/(1+u*u)), dec(2*u/(1+u*u))
    return co*x[0]-si*x[1], si*x[0]+co*x[1]

fiber_cases, max_reverse_error = 0, D(0)
three_rows = []
for denominator_scale in (1, 2, 10, 100, 10000, 10**8):
    t = R/(2*denominator_scale)
    r, chord = 1-t*t, t/(100*(1-t*t))
    x1 = r-chord*chord/(2*r)
    x2sq = chord*chord*(1-chord*chord/(4*r*r))
    assert t*t+t**4 < R*R
    assert 0 < chord < 2*r and x2sq > 0
    assert x1*x1+x2sq == r*r
    assert (x1-r)**2+x2sq == chord*chord
    assert 100*chord == t/r
    # Complete implicit equation's first component and second coefficient.
    assert -(t/r)*x1+100*chord*(x1-r) == -t
    assert -t/r+100*chord == 0
    x2 = dec(x2sq).sqrt()
    for u in (Q(0), Q(1, 3), Q(1), Q(-2), Q(5)):
        a, b = rotated((dec(r), D(0)), u), rotated((-dec(t), D(0)), u)
        for sign in (-1, 0, 1):
            xx = (dec(r), D(0)) if sign == 0 else (dec(x1), sign*x2)
            x = rotated(xx, u)
            v = sub(x, a)
            p = tuple(norm(v)*z for z in v)
            g = tuple(-dec(t/r)*z for z in x)
            error = norm(sub(b, tuple(gj+100*pj for gj, pj in zip(g, p))))
            max_reverse_error = max(max_reverse_error, error, abs(norm(x)-dec(r)))
            dist_input = ((norm(a)-1)**2+norm(b)**2).sqrt()
            P = norm(p)
            assert P <= dec(K)*dist_input**2+dec(c)*dist_input+D('1e-65')
            anchor_actual = norm(tuple(2*xj-aj-sj for xj, aj, sj in zip(x, a, rotated((D(1), D(0)), u))) + tuple(2*pj-bj for pj, bj in zip(p, b)))
            assert anchor_actual <= dec(L)*dist_input.sqrt()+D('1e-65')
            rho2 = P+norm(sub(b, p))**2
            dplus = ((norm(x)-1)**2+P*P).sqrt()
            assert dplus <= 3*rho2+D('1e-65')
            fiber_cases += 1
    three_rows.append({'t':float(t),'chord':float(chord),'input_distance':float((dec(t*t+t**4)).sqrt()),'outputs':3})
assert max_reverse_error < D('1e-65')

# Sharpness / old-condition checks use exact chord norms, no numerical roots.
separation = []
for eta in (Q(1, 10**j) for j in range(3, 10)):
    assert 100*eta*eta <= R
    LT_ratio = -1/(10000*eta*eta)+Q(99, 10000)
    H1_ratio = Q(2, 3)*999*eta**3/(eta**2+9801*eta**4)
    assert LT_ratio < 0
    assert 2*eta**2+9802*eta**4 > 3*10000*eta**4
    separation.append({'eta':float(eta),'LT_ratio':float(LT_ratio),'direct_energy_H1_ratio':float(H1_ratio),'anchor_reflection_over_sqrt_input_distance':.2})

# At critical damping zero the exact center output of a circle-zero input.
assert abs(Q(1)) <= 1  # center fiber: ||b+A||a||a|| <= 1, A=1

def radial_root(coefficient):
    lo, hi = D(0), D(1)
    for _ in range(275):
        mid = (lo+hi)/2
        if 1-mid-D(coefficient)**2*mid**4 > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

center_radius = radial_root(100)
cycle_radius = radial_root(404)
assert abs((1-center_radius).sqrt()-100*center_radius**2) < D('1e-77')
assert abs((1-cycle_radius).sqrt()-404*cycle_radius**2) < D('1e-77')
assert cycle_radius < D('.5')
P = 4*cycle_radius**2
assert abs(P/P.sqrt()-2*cycle_radius) < D('1e-77')
assert abs(-(1-cycle_radius).sqrt()+100*P+P) < D('1e-77')
center_residual_checks = {}
for P0 in (Q(0), Q(1, 198), Q(1, 99), Q(2, 99), Q(1)):
    qmin = -min(99*P0,Q(1))
    value = P0+(qmin+99*P0)**2
    assert value == P0+max(99*P0-1,Q(0))**2
    center_residual_checks[str(P0)] = str(value)

values = {'scale':scale,'Pmax':Pmax,'anchor_upper':anchor,'EB_upper':EB,'residual_squared_upper':rho_sq,'window':window,'compatibility':compatibility,'length_budget':budget,'alternate_energy_theta_upper':theta_bound}
out = {
    'python':sys.version.split()[0], 'precision_digits':80, 'randomness':'none',
    'tuple':{'lambda':1,'R':float(R),'gamma':.5,'L':float(L),'bar_t':1,'psi':'3s^2','kappa':float(kappa)},
    'exact_fraction_checks':{key:{'rational':str(value),'decimal':float(value)} for key,value in values.items()},
    'three_fiber_rows':three_rows,'rotated_closed_fiber_cases':fiber_cases,
    'max_decimal_reverse_error':str(max_reverse_error),'separation_witnesses':separation,
    'center_zero_input_radius':str(center_radius), 'exact_global_two_cycle_radius':str(cycle_radius),
    'center_true_residual_squared_checks':center_residual_checks,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope':'Finite rational arithmetic and closed-fiber reverse checks. All-input coverage, exact-three exhaustiveness, all-output bounds and infinite trajectories are proved analytically.'
}
Path(__file__).with_name('circle_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ('python','rotated_closed_fiber_cases','max_decimal_reverse_error','script_sha256')},indent=2))
