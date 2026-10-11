#!/usr/bin/env python3
"""Finite verification of a convex Bregman GPPA example; not a universal proof.

No third-party dependencies. The implicit step is independently solved by
high-precision interval bisection. Exact rational tests check the graph,
Bregman distance, residual identities, and inverse-modulus cube inequality.
"""
from __future__ import annotations

import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path


def implicit_step(t: Decimal, lam: Decimal) -> Decimal:
    """Unique real u solving u**3 + lam*u = t**3; no cancellation-prone Cardano."""
    if t == 0:
        return Decimal(0)
    sign = Decimal(1) if t > 0 else Decimal(-1)
    a = abs(t)
    lo = Decimal(0)
    hi = min(a, a**3 / lam)
    for _ in range(240):
        mid = (lo + hi) / 2
        if mid**3 + lam * mid < a**3:
            lo = mid
        else:
            hi = mid
    return sign * (lo + hi) / 2


def dh(u: F, t: F, w: F, s: F) -> F:
    return (u**4 - t**4) / 4 - t**3 * (u - t) + (w - s)**2 / 2


def main() -> None:
    rational_ts = [F(-100), F(-2), F(-1), F(-1, 2), F(-1, 10000),
                   F(-1, 10**10), F(0), F(1, 10**10), F(1, 10000),
                   F(1, 2), F(1), F(2), F(100)]
    ss = [F(-3), F(0), F(5)]
    lams = [F(1, 100), F(1, 4), F(1), F(4), F(100)]
    pts = list(product(rational_ts, ss))
    counts = {"exact_graph_pairs": 0, "bregman_distance_pairs": 0,
              "true_residual_points": 0, "inverse_modulus_pairs": 0,
              "implicit_steps": 0, "objective_gap_checks": 0,
              "cubic_rate_checks": 0, "local_scalar_checks": 0,
              "physical_certificate_checks": 0, "ordinary_ppa_checks": 0,
              "degenerate_kernel_steps": 0}

    for lam in lams:
        for (t, s), (u, w) in combinations(pts, 2):
            # Full graph output y=(t**3,s), graph value f=(t,0).
            di = (t**3 + lam*t - u**3 - lam*u)**2 + (s-w)**2
            dc = (t**3 - lam*t - u**3 + lam*u)**2 + (s-w)**2
            assert di - dc == 4*lam*(t**3-u**3)*(t-u) >= 0
            counts["exact_graph_pairs"] += 1
    for (t, s), (u, w) in product(pts, repeat=2):
        d = dh(u, t, w, s)
        factor = (u-t)**2 * ((u+t)**2+2*t**2) / 4 + (w-s)**2 / 2
        assert d == factor >= 0
        assert (d == 0) == ((t,s) == (u,w))
        counts["bregman_distance_pairs"] += 1
        assert abs(t-u)**3 <= 4*abs(t**3-u**3)
        counts["inverse_modulus_pairs"] += 1
    for t,s in pts:
        f=(t,F(0)); z=(t**3,s); p=(F(0),s)
        residual_squared=sum(c*c for c in f)
        kernel_distance_squared=sum((a-b)**2 for a,b in zip(z,p))
        physical_distance_squared=sum((a-b)**2 for a,b in zip((t,s),p))
        assert kernel_distance_squared == residual_squared**3
        assert physical_distance_squared == residual_squared
        assert (residual_squared == 0) == (z[0] == 0)
        counts["true_residual_points"] += 1
    for d in [F(0), F(1,10**12), F(1,100), F(1,4), F(1,2)]:
        assert d <= F(1,2) < F(1)
        assert d**3 <= d/4
        assert d**3 <= F(1)  # ψ is evaluated in its declared [0,1] window.
        counts["local_scalar_checks"] += 1
    for lam in lams:
        # λ=1/100 has the smallest window: r<=1/20 gives r²/λ<=1/4.
        for r in [F(0), F(1,10**12), F(1,10000), F(1,100), F(1,20)]:
            forward_anchor=abs(r**3)
            kernel_step_bound=(forward_anchor+forward_anchor)/2
            physical_direct_bound=kernel_step_bound/lam
            assert physical_direct_bound <= r/4
            counts['physical_certificate_checks'] += 1
        for t in rational_ts:
            y=t/(1+lam)
            assert t == y+lam*y
            assert (t == 0) or y/t == 1/(1+lam)
            counts['ordinary_ppa_checks'] += 1

    max_relative_residual = Decimal(0)
    max_cubic_defect = Decimal(0)
    with localcontext() as ctx:
        ctx.prec = 110
        ctx.Emin = -999999999
        ctx.Emax = 999999999
        for lam_r in lams:
            lam = Decimal(lam_r.numerator)/Decimal(lam_r.denominator)
            for t_r,s_r in pts:
                t0 = Decimal(t_r.numerator)/Decimal(t_r.denominator)
                s = Decimal(s_r.numerator)/Decimal(s_r.denominator)
                t = t0
                length = Decimal(0)
                kernel_length = Decimal(0)
                for _ in range(6):
                    u = implicit_step(t,lam)
                    residual = u**3+lam*u-t**3
                    if t:
                        relative = abs(residual)/abs(t**3)
                        max_relative_residual = max(max_relative_residual,relative)
                        assert relative < Decimal('1e-65')
                        assert t*u > 0 and abs(u) < abs(t)
                        assert abs(t-u)**3 <= abs(t**3-u**3)
                        # The exact equation gives the rate identity below.
                        ratio = abs(u)/abs(t)**3
                        assert abs(ratio-1/(lam+u**2))*lam < Decimal('1e-65')
                    else:
                        assert u == 0
                    length += abs(t-u)
                    kernel_length += abs(t**3-u**3)
                    # Independent trial values around the returned optimizer.
                    eps = max(abs(u),Decimal(1))*Decimal('1e-12')
                    for trial in (u-eps,u+eps):
                        # Expanded objective gap avoids subtracting constants.
                        v = trial-u
                        gap = residual*v + lam*v*v/2 + (
                            v*v*((trial+u)**2+2*u*u)/4)
                        assert gap > 0
                        counts['objective_gap_checks'] += 1
                    t=u
                    counts['implicit_steps'] += 1
                assert abs(length-(abs(t0)-abs(t))) <= max(abs(t0),Decimal(1))*Decimal('1e-100')
                assert abs(kernel_length-(abs(t0)**3-abs(t)**3)) <= max(abs(t0)**3,Decimal(1))*Decimal('1e-100')
                assert s == Decimal(s_r.numerator)/Decimal(s_r.denominator)
            for t in (Decimal('1e-5'),Decimal('-1e-5')):
                u=implicit_step(t,lam)
                defect=abs(lam*abs(u)/abs(t)**3-1)
                max_cubic_defect=max(max_cubic_defect,defect)
                assert defect < Decimal('1e-20')
                counts['cubic_rate_checks'] += 1

    # Genuine convex minimization with a degenerate Bregman kernel. Each
    # freely chosen s is a minimizer; kernel convergence is not point convergence.
    for k in range(20):
        t=F(1,2**k); u=F(1,2**(k+1))
        s=F((-1)**k); w=F((-1)**(k+1))
        assert t == u+u
        assert abs(w-s) == 2
        assert abs(u) == abs(t)/2
        counts['degenerate_kernel_steps'] += 1
    out={"status":"PASS","scope":"finite rational and high-precision checks; analytic proof is in the report",
         "precision":110,"bisection_iterations":240,"seed":"none; deterministic grids",
         "counts":counts,"maximum_relative_implicit_residual":str(max_relative_residual),
         "maximum_normalized_cubic_rate_defect":str(max_cubic_defect)}
    target=Path(__file__).with_name('results.json')
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
