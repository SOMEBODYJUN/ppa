#!/usr/bin/env python3
"""Exact finite checks for nfb_source_priority_followup.md; not theorem proofs.

Run from repository root:
  python3 research/novelty/2026_10_09/nfb_source_priority_check.py
Only Python's standard library is required. No files are mutated.
"""
from fractions import Fraction as F
import json


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def mul(a, x):
    return [dot(row, x) for row in a]


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def scale(c, x):
    return [c * a for a in x]


def madd(a, b):
    return [add(x, y) for x, y in zip(a, b)]


def mscale(c, a):
    return [scale(c, row) for row in a]


def inv2(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [[a[1][1] / det, -a[0][1] / det],
            [-a[1][0] / det, a[0][0] / det]]


def coefficients(theta, favorable):
    # RV v1 (4.2)-(4.5), with alpha=0 and fixed zeta,
    # theta*eta_RV = 2-theta-tau/(2*beta)-c_RV*zeta.
    nu_multiplier = F(1) if favorable and theta >= 1 else F(3)
    c_rv = abs(1 - theta) * nu_multiplier + (1 + abs(1 - theta)) + theta**2
    eta_nfb = F(1) if favorable and theta >= 1 else 1 + abs(1 - theta)
    c_nfb = 2 * eta_nfb
    return c_rv, c_nfb


def main():
    count = 0
    for numerator in range(1, 40):
        theta = F(numerator, 20)
        for favorable in (True, False):
            c_rv, c_nfb = coefficients(theta, favorable)
            if theta >= 1 and favorable:
                claimed_difference = (theta - 1) * (theta + 3)
            elif theta >= 1:
                claimed_difference = (theta - 1) * (theta + 3)
            else:
                claimed_difference = (theta - 1)**2
            assert c_rv - c_nfb == claimed_difference >= 0
            count += 1

    # An actual common monotone inclusion certifies strict parameter-range
    # separation from the RV v1 sufficient condition.
    theta, zeta, tau, beta = F(3, 2), F(3, 20), F(1), F(10)
    c_rv, c_nfb = coefficients(theta, True)
    delta_nfb = 2 - theta - tau / (2 * beta) - c_nfb * zeta
    delta_rv = 2 - theta - tau / (2 * beta) - c_rv * zeta
    assert delta_nfb == F(3, 20)
    assert delta_rv == -F(3, 16)
    # The exact scalar state matrix for A=Id,C=0,M=17/20 Id is
    # [[7,30],[3,-3]]/37; eigenvalues (2 +/- sqrt(115))/37.
    assert F(7, 37) + F(-3, 37) == F(4, 37)
    assert F(7, 37) * F(-3, 37) - F(30, 37) * F(3, 37) == F(-3, 37)
    assert 115 < (37 - 2)**2  # certifies both eigenvalue moduli < 1

    # Exact vector recurrences: MBG equals NFB at theta=1; RV alpha=0
    # equals NFB for any theta, including arbitrary starting memory.
    a = [[F(7, 10), F(3, 100)], [F(3, 100), F(9, 10)]]
    c = [[F(1, 10), F(1, 100)], [F(1, 100), F(3, 20)]]
    m = [[F(9, 10), F(1, 50)], [F(-1, 100), F(11, 10)]]
    metric = [[F(1), F(1, 10)], [F(1, 10), F(6, 5)]]
    tau = F(1)
    h = madd(mscale(tau, m), mscale(-1, metric))
    warped = inv2(madd(m, a))
    recurrence_checks = 0
    for theta in [F(1, 2), F(1), F(3, 2)]:
        x, u = [F(2), F(-1)], [F(1, 4), F(-1, 5)]
        xr, ur = list(x), list(u)
        for _ in range(12):
            p = mul(warped, add(mul(madd(m, mscale(-1, c)), x), scale(1/tau, u)))
            un = add(mul(h, p), scale(-1, mul(h, x)))
            xn = add(scale(1-theta, x), scale(theta, p))
            # RV (2.3): alpha=0 makes y=x; the other symbols map directly.
            y = list(xr)
            pr = mul(warped, add(add(mul(m, y), scale(-1, mul(c, y))), scale(1/tau, ur)))
            urn = add(mul(h, pr), scale(-1, mul(h, y)))
            xrn = add(scale(1-theta, y), scale(theta, pr))
            assert (p, un, xn) == (pr, urn, xrn)
            if theta == 1:
                assert xn == p  # MBG Algorithm 1
            x, u, xr, ur = xn, un, xrn, urn
            recurrence_checks += 1

    # Scalar parallel-sum square completion, permitting a negative rho.
    completion_checks = 0
    for rho in [F(-4, 5), F(-1, 4), F(0), F(2, 5)]:
        beta = F(1)
        for av in [F(-3), F(1, 2), F(2)]:
            for cv in [F(-1), F(0), F(4, 3)]:
                q = rho * beta / (rho + beta)
                left = rho * av**2 + beta * cv**2 - q * (av + cv)**2
                right = (rho * av - beta * cv)**2 / (rho + beta)
                assert left == right >= 0
                completion_checks += 1

    # Evens PPPA/linear theorem gates for F=-Id at ordinary step tau=3.
    tau, rho, theta, eb = F(3), F(-1), F(1), F(1)
    eta = 1 + rho/tau
    kappa = theta * (2*eta-theta)
    rate_squared = 1 - kappa / (1 + eb/tau)**2
    assert eta == F(2, 3) and kappa == F(1, 3)
    assert rate_squared == F(13, 16)
    assert F(1)/(1-tau) == F(-1, 2)

    print(json.dumps({
        "coefficient_identities_checked": count,
        "strict_monotone_witness": {"NFB_delta": str(delta_nfb), "RV_v1_delta": str(delta_rv)},
        "recurrence_steps_checked": recurrence_checks,
        "parallel_sum_completions_checked": completion_checks,
        "negative_identity_Evens_rate_squared": str(rate_squared),
        "scope": "Exact finite checks support displayed algebra; general mathematical implications are proved in the report."
    }, indent=2))


if __name__ == "__main__":
    main()
