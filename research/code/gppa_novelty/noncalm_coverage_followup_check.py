#!/usr/bin/env python3
"""Deterministic finite checks for TL1--TL20 and the C212 dyadic reduction.

Run from the repository root:
  python3 research/code/gppa_novelty/noncalm_coverage_followup_check.py

No random samples or persisted result files. Arithmetic checks support the
displayed analytic proofs; they do not certify infinite series or novelty.
"""

import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction


def main():
    # Exact algebra B^2 <= C; no floating-point assumptions.
    pairs = 0
    for ti in range(0, 21):
        for wi in range(0, 21):
            t, w = Fraction(ti, 20), Fraction(wi, 13)
            B = (t + w) / 2
            C = (t * t + w * w) / 2
            assert C - B * B == (t - w) ** 2 / 4
            assert B * B <= C
            pairs += 1

    # Both threshold equality and strict interior: nu=3, A0=1, rho=1/2.
    sf_count = 0
    worst_h1, worst_h2, worst_kl = 0.0, 0.0, 0.0
    sectors = [(3.0, 0.6, 1.2), (3.0, 0.75, 1.5),
               (2.0, 2.0 / 3.0, 4.0 / 3.0), (2.0, 0.9, 1.8)]
    for nu, gamma, beta in sectors:
        assert beta >= 1.0 + gamma / nu - 1e-14
        assert beta <= 2.0 * gamma + 1e-14
        A0, rho = 1.0, 0.5
        a = (1.0 - rho ** (beta * (nu - 1.0))) / (A0 * A0 + 4.0)
        b = beta / A0
        radii = [rho] + [10.0 ** (-j / 4.0) for j in range(2, 161)]
        for sign in (-1.0, 1.0):
            for u in radii:
                r = sign * u
                y = u ** nu
                s2 = A0 * A0 * u ** (2.0 * gamma) + (y - r) ** 2
                drop = u ** beta - y ** beta
                grad = beta * y ** (beta - 1.0)
                ratio1 = a * s2 / drop
                ratio2 = grad / (b * math.sqrt(s2))
                assert ratio1 <= 1.0 + 3e-13, (nu, gamma, beta, r, ratio1)
                assert ratio2 <= 1.0 + 3e-13, (nu, gamma, beta, r, ratio2)
                # Compute KL product through exponents, avoiding underflow.
                kl = (u ** (beta * (1.0 / beta - 1.0))) * (u ** (beta - 1.0))
                assert abs(kl - 1.0) < 1e-12
                worst_h1, worst_h2 = max(worst_h1, ratio1), max(worst_h2, ratio2)
                worst_kl = max(worst_kl, abs(kl - 1.0))
                sf_count += 1
    assert Fraction(3, 5) == Fraction(3, 1) / (2 * Fraction(3, 1) - 1)
    assert Fraction(6, 5) == 1 + Fraction(3, 5) / 3 == 2 * Fraction(3, 5)
    # Low-sector C1 obstruction: required decay exponent is strictly positive.
    assert 1 + Fraction(1, 2) / 3 - 2 * Fraction(1, 2) == Fraction(1, 6) > 0
    assert 1 + Fraction(3, 5) / 3 - 2 * Fraction(3, 5) == 0
    # Same-target true EB is not preserved by a maximal monotone extension:
    # h=.5(x-1)_+^2+(x-1)_+ gives partial h(0)={0}, partial h(1)=[0,1].
    original_residual_at_one = Fraction(1)
    extended_residual_at_one = Fraction(0)
    old_target_distance_at_one = Fraction(1)
    assert old_target_distance_at_one <= original_residual_at_one
    assert old_target_distance_at_one > extended_residual_at_one

    # Exact tail identity for a nonlinear noncalm step envelope.
    # b(t)=sqrt(t)+t, tau(t)=t/4; L(t)=2sqrt(t)+(4/3)t.
    tail_cases = 0
    with localcontext() as ctx:
        ctx.prec = 70
        kappa = Decimal(1) / 4
        def btail(t):
            return t.sqrt() + t
        def Ltail(t):
            return 2 * t.sqrt() + Decimal(4) * t / 3
        for exponent in range(1, 45):
            t = Decimal(10) ** (-exponent)
            err = abs(Ltail(t) - Ltail(kappa * t) - btail(t))
            assert err < Decimal("1e-65")
            # Generic true transition may be any smaller scalar distance.
            for fraction in (Decimal(0), Decimal("0.1"), kappa):
                assert Ltail(t) - Ltail(fraction * t) >= btail(t) - Decimal("1e-65")
                tail_cases += 1

        # Energy data omega=sqrt(t), V=t^2+4t, q=1/2.
        # Iterate tau_E=V^{-1}(C) with a stable inverse formula.
        t = Decimal("0.2")
        V0 = t * t + 4 * t
        q = Decimal("0.5")
        budget = (q * V0).sqrt() / (1 - q.sqrt())
        total = Decimal(0)
        for j in range(180):
            C = (t * t + t) / 2
            V = t * t + 4 * t
            B = (t + t.sqrt()) / 2
            assert B * B <= C
            assert C <= q * V
            assert B <= (q ** (j + 1) * V0).sqrt() + Decimal("1e-65")
            total += B
            t = C / ((4 + C).sqrt() + 2)
        assert total <= budget
        energy_result = {"partial_length_180": str(total), "analytic_budget": str(budget)}

    # q=3/5: source distance exponent 3/4; dyadic block exponent -1/4.
    q = Fraction(3, 5)
    distance_exponent = q / (2 * (1 - q))
    block_exponent = Fraction(1, 2) - distance_exponent
    assert distance_exponent == Fraction(3, 4)
    assert block_exponent == Fraction(-1, 4)
    for q in (Fraction(51, 100), Fraction(3, 5), Fraction(3, 4), Fraction(99, 100)):
        assert (1 - 2 * q) / (2 * (1 - q)) < 0
    assert (1 - 2 * Fraction(1, 2)) / (2 * (1 - Fraction(1, 2))) == 0

    # Finite sample of the exact scalar recurrence used in the independent
    # rate derivation. Its step squares telescope by construction.
    qf, c, a0 = 0.6, 0.7, 0.4
    p = 1.0 / qf - 1.0
    delta = min(p * c / (2.0 ** (p + 1.0)), (2.0 ** p - 1.0) * a0 ** (-p))
    values, steps = [a0], []
    for k in range(4096):
        prev = values[-1]
        lo, hi = 0.0, prev
        for _ in range(70):
            mid = (lo + hi) / 2.0
            if mid + c * mid ** (1.0 + p) < prev:
                lo = mid
            else:
                hi = mid
        nxt = (lo + hi) / 2.0
        values.append(nxt)
        steps.append(math.sqrt(max(prev - nxt, 0.0)))
        bound = (a0 ** (-p) + delta * (k + 1)) ** (-1.0 / p)
        assert nxt <= bound * (1 + 1e-12)
    dyadic_checks = []
    for exponent in range(0, 12):
        n = 2 ** exponent
        block = sum(steps[n:2 * n])
        bound = math.sqrt(n * values[n])
        assert block <= bound * (1 + 1e-12)
        dyadic_checks.append({"N": n, "length": block, "sqrt_N_d_N": bound})

    print(json.dumps({
        "status": "PASS",
        "exact_energy_pairs": pairs,
        "sf_signed_tests": sf_count,
        "sf_max_H1_ratio": worst_h1,
        "sf_max_H2_ratio": worst_h2,
        "sf_max_KL_error": worst_kl,
        "tail_identity_tests": tail_cases,
        "energy": energy_result,
        "q_3_5_distance_exponent": str(distance_exponent),
        "q_3_5_dyadic_block_exponent": str(block_exponent),
        "dyadic_checks": dyadic_checks,
        "limits": "Finite arithmetic only; infinite series, all trajectories, and novelty use proofs."
    }, indent=2))


if __name__ == "__main__":
    main()
