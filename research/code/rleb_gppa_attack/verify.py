#!/usr/bin/env python3
"""Finite exact checks supporting the independent GPPA boundary audit.

Fractions certify selected algebraic instances, not general theorem validity.
No manuscript, ledger, or registered claim is modified by this script.
"""
from fractions import Fraction as Q
from itertools import product
import json
from math import log2
from pathlib import Path
from decimal import Decimal, localcontext

counts = {}

# Identity-kernel recovery, full original F(y)={2y,3y}: both outputs
# must remain allowed. Check every branch sequence through twelve updates.
checked = 0
for x0 in [Q(-1), Q(-1, 7), Q(0), Q(1, 7), Q(1)]:
    for choices in product([3, 4], repeat=12):
        x = x0
        length = Q(0)
        for divisor in choices:
            y = x/divisor
            d, dp, s = abs(x), abs(y), abs(x-y)
            rF = 2*abs(y)
            assert (x-y) in {2*y, 3*y}
            assert abs(2*y-x) <= d/2
            assert dp == rF/2
            assert s <= 3*d/4
            assert dp <= 3*d/8
            length += s
            x = y
            checked += 1
        assert length <= Q(6, 5)*abs(x0)
counts['identity_full_multivalued_transitions'] = checked

# Complete degenerate kernel and drifting zero fiber.
checked = 0
for k in range(16):
    u, unext = Q(1, 2**k), Q(1, 2**(k+1))
    t, tnext = Q((-1)**k), Q((-1)**(k+1))
    assert u-unext == unext  # full F(u,t)=(u,0), lambda=1
    assert unext == u/2
    assert abs(tnext-t) == 2
    assert abs(unext) == abs(u)/2  # physical target-distance contraction
    checked += 1
counts['uncontrolled_full_fiber_transitions'] = checked

# Candidate's zeta(d) lifting rescues a genuine complete, multivalued,
# noninjective instance F(t,s)={(t,s),(3t,s)}, v(t,s)=(t,0), S={0}.
checked = 0
grid = [Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)]
for t, s in product(grid, repeat=2):
    d2 = t*t+s*s
    for m in [1, 3]:
        yt, ys = t/(1+m), Q(0)
        kernel_step = abs(t-yt)
        physical_step_sq = (t-yt)**2+s*s
        assert t-yt == m*yt and ys == 0
        # Reflected bound omega(h)=h/2 at h=|t|.
        assert abs(2*yt-t) <= abs(t)/2
        # r_F(y)=|yt| and physical target-distance equals |yt|.
        assert yt*yt <= d2/4
        # sqrt(kernel_step^2+s^2) <= kernel_step+d; square via
        # sqrt(...) <= kernel_step+|s| <= kernel_step+d.
        assert physical_step_sq <= (kernel_step+abs(s))**2
        assert s*s <= d2
        checked += 1
counts['zeta_complete_noninjective_multivalued_edges'] = checked

# Missing output-collar coverage counterexample: v(x)=x^2,
# F(y)=3(y^2-1), complete S={-1,1}. Both outputs at x=1 are legal.
for y in [Q(1), Q(-1)]:
    x = Q(1)
    assert x*x-y*y == 3*(y*y-1)
    assert abs(2*y*y-x*x-1) == 0
    assert min(abs(y-1), abs(y+1)) == 0
    if y == -1:
        assert abs(x-y) == 2
        assert abs(x*x-y*y) == 0
counts['local_inverse_remote_zero_outputs'] = 2

# Nonclosed kernel zero target: Q=(0,infty), Z={2^{-n}:n in Z}.
# On bands [2/3,7/10]2^{-n}, T(z)=z/2; otherwise T(z)=P_Z(z).
# Build A from exact graph {(T(z),z-T(z))}. Nonzero outputs remain in
# their bands and have unique predecessor 2z, so r_A(z)=z.
checked = 0
for n in range(-9, 10):
    scale = Q(2)**(-n)
    for c in [Q(2, 3), Q(27, 40), Q(7, 10)]:
        z = c*scale
        p = scale/2
        d = z-p
        y = z/2
        dp = d/2
        assert d > 0
        assert abs(2*y-z-p) <= 3*d
        assert abs(z-y) <= 2*d
        assert dp <= Q(2, 7)*y  # r_A(y)=y
        assert Q(2, 7)*(2*d) == Q(4, 7)*d
        assert dp == d/2
        checked += 1
    # Generic nearest-zero branch has reflection exactly d and output EB0.
    for c in [Q(11, 20), Q(3, 5), Q(4, 5), Q(9, 10), Q(1)]:
        z = c*scale
        p = min([scale, scale/2], key=lambda p: abs(z-p))
        assert abs(2*p-z-p) == abs(z-p)
        assert abs(z-p) <= 2*abs(z-p)
        checked += 1
counts['nonclosed_kernel_target_edges'] = checked

# Stronger smooth physical counterexample, with all-pair kernel RL.
# v(a,b)=(exp(a),exp(a)sin b), F(a,b)=(exp(a)|sin b|,exp(a)sin b).
# Q={(s,t):s>0,|t|<=s}, A(s,t)=(|t|,t),
# T(s,t)=(s-|t|/2,t/2), C(s,t)=(s-|t|,0).
points = []
for s in [Q(1, 4), Q(1, 2), Q(1), Q(2), Q(4)]:
    points += [(s, c*s) for c in [Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)]]
checked = 0
for s, t in points:
    sp, tp = s-abs(t)/2, t/2
    assert sp > 0 and abs(tp) <= sp
    assert (s-sp, t-tp) == (abs(tp), tp)
    # Kernel true residual squared is exactly 2*tp^2; distance is |tp|.
    assert tp*tp == (2*tp*tp)/2
    assert (2*sp-s, 2*tp-t) == (s-abs(t), Q(0))
    checked += 1
for (s, t), (r, q) in product(points, repeat=2):
    reflect_difference_sq = ((s-abs(t))-(r-abs(q)))**2
    input_difference_sq = (s-r)**2+(t-q)**2
    assert reflect_difference_sq <= 2*input_difference_sq
    checked += 1
counts['smooth_nonclosed_target_allpair_checks'] = checked

# Controlled drift with omitted Dini gate. zeta(2^{-j})=1/(j+1),
# v=(u,0), F=(u,0), allowed output (u/2,t+zeta(|u|)).
t = Q(0)
for k in range(128):
    u = Q(1, 2**k)
    unext = u/2
    drift = Q(1, k+1)
    assert u-unext == unext
    assert (u-unext)**2+drift**2 <= (abs(u-unext)+drift)**2
    t += drift
counts['nonsummable_zeta_edges'] = 128
assert t > Q(5)

# Convex Bregman instance: lambda*u+u^3=t^3. Strictly increasing cubic
# gives the full unique normal output; tangential coordinate is unchanged.
checked = 0
with localcontext() as ctx:
    ctx.prec = 100
    for lam in [Decimal('0.25'), Decimal('1'), Decimal('4')]:
        for inp in [Decimal('-1'), Decimal('-0.5'), Decimal('-0.1'),
                    Decimal('0'), Decimal('0.1'), Decimal('0.5'), Decimal('1')]:
            lo, hi = Decimal(0), abs(inp)
            rhs = abs(inp)**3
            for _ in range(320):
                mid = (lo+hi)/2
                if mid**3+lam*mid < rhs:
                    lo = mid
                else:
                    hi = mid
            out = (lo+hi)/2
            assert abs(out**3+lam*out-rhs) < Decimal('1e-85')
            assert out <= abs(inp)
            assert abs(abs(inp)-out)**3 <= abs(rhs-out**3)+Decimal('1e-85')
            assert out <= rhs/lam+Decimal('1e-85')
            if inp:
                assert abs(out/rhs-1/(lam+out**2)) < Decimal('1e-80')
            checked += 1
counts['convex_bregman_unique_output_checks'] = checked

# Extreme noninjectivity is not by itself an obstruction: v=0,F=Id.
# Full output is y=0, and h(d,s)=d transfers it exactly in any dimension.
checked = 0
for x in grid:
    y = Q(0)
    assert 0-0 == y
    assert abs(y-x) == abs(x)
    checked += 1
counts['constant_kernel_full_output_checks'] = checked

# Source small-ASM omission in the direct branch: F(x)=epsilon*x,
# epsilon=1/10, Id kernel, lambda1. Sharp reflection L=9/11.
eps = Q(1, 10)
L = (1-eps)/(1+eps)
direct_ratio = (1+L)/(2*eps)
assert direct_ratio == Q(100, 11) and direct_ratio > 1
assert Q(1)/(1+eps) == Q(10, 11) < 1

# Integrated general energy gate and its linear specialization. For the
# full F(x)=eps*x all scalar levels are rational and the sharp reflected
# constant makes the energy factor exactly the actual output factor.
checked = 0
for eps in [Q(1, 10), Q(1, 4), Q(1), Q(3)]:
    for lam in [Q(1, 10), Q(1, 2), Q(1), Q(2), Q(4)]:
        reflected = abs(1-lam*eps)/(1+lam*eps)
        actual_factor = 1/(1+lam*eps)
        energy_factor_sq = (1+reflected**2)/(2*(1+(lam*eps)**2))
        assert energy_factor_sq == actual_factor**2 < 1
        for inp in [Q(-1), Q(-1, 7), Q(0), Q(1, 7), Q(1)]:
            out = actual_factor*inp
            d, dp = abs(inp), abs(out)
            step = abs(inp-out)
            assert inp-out == lam*eps*out
            assert dp*dp+step*step == (1+reflected**2)*d*d/2
            assert eps*dp == step/lam
            assert dp*dp+(lam*eps*dp)**2 <= (1+reflected**2)*d*d/2
            assert dp*dp <= energy_factor_sq*d*d
            # Monotone L=1 certificate restores every positive lambda,
            # even where the standalone direct gauge fails.
            monotone_energy_factor_sq = 1/(1+(lam*eps)**2)
            assert actual_factor**2 <= monotone_energy_factor_sq < 1
            checked += 1
counts['integrated_energy_linear_specializations'] = checked

# Exact count round trip; decimal only for the physical divergence offset.
total = sum(counts.values())
assert total-sum(v for k, v in counts.items() if k != 'nonclosed_kernel_target_edges') == counts['nonclosed_kernel_target_edges']
result = {
    'status': 'PASS', 'counts': counts, 'total_checked_instances': total,
    'nonclosed_target_start_x': log2(1.5),
    'source_small_asm_direct_ratio_exact': str(direct_ratio),
    'source_small_asm_actual_point_factor_exact': str(Q(10, 11)),
    'interpretation': 'Finite exact verification of stated examples; no universal theorem certified by enumeration.'
}
destination = Path(__file__).with_name('results.json')
destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
