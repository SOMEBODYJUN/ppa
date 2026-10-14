#!/usr/bin/env python3
"""Supplementary checks for unified_ppa_inexact_interfaces.md.

Standard library only; no random seed, external data, or hidden solver.
Exact rational identities and finite deterministic samples do not prove
the universal statements, whose proofs are in the adjacent candidate.
"""
from fractions import Fraction as Q
import json
import math


TOL = 2e-10


def norm(v):
    return math.sqrt(sum(t * t for t in v))


def close(a, b, tol=TOL):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


def scalar_minimum_checks():
    """Check COH profile minimization, not the invalid reverse-EB step."""
    count = 0
    for K in (0.01, 0.3, 1.0, 100.0):
        for c in (0.03, 1.0, 3.0, 10.0):
            sigma_max = c / (math.sqrt(K * K + c) + K)
            for proportion in (0.0, 0.1, 0.75, 0.999):
                sigma = proportion * sigma_max
                kappa = K / (math.sqrt(K * K + c) - sigma)
                assert 0 < kappa < 1
                assert sigma < math.sqrt(c)
                profile = [math.sqrt((K * j / 1000) ** 2 + c)
                           - K * j / (1000 * kappa)
                           for j in range(1001)]
                close(min(profile), sigma)
                for j in range(1001):
                    theta = K * j / 1000
                    ratio = theta / (math.sqrt(theta * theta + c) - sigma)
                    assert ratio <= kappa + TOL
                count += 1
    return count


def diagonal_checks():
    K, lam, rho = 100.0, 3.0, 1.0
    c = lam * (lam - 2 * rho)
    sigma_max = c / (math.sqrt(K * K + c) + K)
    sigma = sigma_max / 2
    kappa = K / (math.sqrt(K * K + c) - sigma)
    count = 0
    for j in range(120):
        angle = 2 * math.pi * j / 120
        y = (math.cos(angle), math.sin(angle))
        w = (-y[0], y[1] / 100)
        W = norm(w)
        assert y[0] * w[0] + y[1] * w[1] >= -rho * W * W - TOL
        assert norm(y) <= K * W + TOL
        for l in range(24):
            eangle = 2 * math.pi * l / 24
            e = (sigma * W * math.cos(eangle), sigma * W * math.sin(eangle))
            x = tuple(y[i] + lam * w[i] + e[i] for i in range(2))
            assert norm(y) <= kappa * norm(x) + TOL
            count += 1
    return dict(c=c, sigma_max=sigma_max, sigma_used=sigma,
                certified_kappa=kappa, samples=count)


def cohypo_endpoint_checks():
    """Actual full-graph endpoint rotations, including beta=0 period two."""
    report = []
    for rho, beta, lam in ((0.0, 1.0, 1.0), (1.0, 0.0, 3.0),
                           (3.0, 4.0, 7.0), (1.0, 100.0, 3.0)):
        K = math.hypot(rho, beta)
        D = math.hypot(lam-rho, beta)
        sigma = D-K
        assert sigma > 0
        A = complex(-rho, beta)
        Z = A+lam
        T = (D/K) * A/Z
        close(abs(T), 1.0)
        assert abs(T-1) > 1e-8
        x = complex(0.1, -0.2)
        length = abs(x)
        step = abs((T-1)*x)
        for _ in range(100):
            w = (D/K)*x/Z
            y = A*w
            e = x-y-lam*w
            close(abs(e), sigma*abs(w))
            close(abs(y), K*abs(w))
            close((y.conjugate()*w).real, -rho*abs(w)**2)
            close(abs(y), length)
            close(abs(y-x), step)
            x = y
        report.append(dict(rho=rho, beta=beta, lambda_value=lam,
                           sigma_critical=sigma, constant_step=step))
    return report


def gu3_checks():
    count = 0
    gamma, alpha, eta, sigma = 0.5, 0.7, 0.4, 0.8
    kappa = 1 / (2 - sigma)
    for sign in (-1, 1):
        for size in (1e-8, 0.0025, 0.1, 1, 100):
            s = sign * size
            for branch in (0, 1):
                w = (-branch * 2 ** gamma * size ** gamma, s)
                y = (2.0, s)
                for en_sign in (-1, 0, 1):
                    for et_sign in (-1, 0, 1):
                        e = (et_sign * eta * size ** alpha, en_sign * sigma * size)
                        x = tuple(y[i] + w[i] + e[i] for i in range(2))
                        d = abs(x[1])
                        assert abs(s) <= kappa * d + TOL
                        bound = ((1 + sigma) * kappa * d
                                 + 2 ** gamma * (kappa * d) ** gamma
                                 + eta * (kappa * d) ** alpha)
                        assert norm(tuple(y[i] - x[i] for i in range(2))) <= bound + TOL
                        count += 1
    s = Q(1, 256)
    drift = math.sqrt(2 * float(s))
    e = (0.0, -float(s))
    w = (-drift, float(s))
    for k in range(16):
        x = (k * drift, float(s))
        y = ((k + 1) * drift, float(s))
        close(x[0] - y[0] - w[0], e[0])
        close(x[1] - y[1] - w[1], e[1])
        close(abs(e[1]), abs(w[1]))
    return dict(samples=count, critical_sigma=1, drift_per_step=drift)


def joint_branch_checks():
    """Exact rational checks of full sign/branch/defect choices."""
    count = 0
    sigma = Q(3, 4)
    for y in [Q(k, 7) for k in range(-30, 31)]:
        for w in (y, y ** 3):
            for fraction in [Q(k, 8) for k in range(-8, 9)]:
                e = sigma * fraction * abs(w)
                x = y + w + e
                assert abs(e) <= sigma * abs(w)
                assert abs(x - y) == abs(x) - abs(y)
                assert abs(x - y) >= (1 - sigma) * min(abs(y), abs(y) ** 3)
                if y:
                    assert x * y > 0 and abs(y) < abs(x)
                count += 1
    return count


def L(lam, sigma):
    a = 1 + lam
    if sigma <= lam / a:
        return a - sigma * lam
    return math.sqrt((1 + 2 * lam) * (1 - sigma * sigma))


def projector_checks():
    count = 0
    sharp_identities = []
    for lam in (0.1, 0.3, 1.0, 3.0, 10.0):
        a = 1 + lam
        critical = math.sqrt(2 * lam / (1 + 2 * lam))
        for sigma in (0.0, 0.03, 0.2, lam / a, critical * 0.999, critical, 0.99):
            lo = math.sqrt(1 - sigma * sigma)
            value = L(lam, sigma)
            # Include both the critical point and interval endpoints explicitly.
            rstar = a * lo / math.sqrt(1 + 2 * lam)
            candidates = [lo, 1.0]
            if lo <= rstar <= 1:
                candidates.append(rstar)
            candidates += [lo + (1 - lo) * j / 1000 for j in range(1001)]
            values = [a * r - lam * math.sqrt(max(0, r*r - lo*lo)) for r in candidates]
            close(min(values), value, 1e-8)
            assert all(v >= value - 1e-8 for v in values)
            # Reconstruct an extremal true-graph pair for every sampled r.
            for r in candidates[::40]:
                y = (r, math.sqrt(max(0, 1 - r*r)))
                t = a*r - lam * math.sqrt(max(0, r*r - lo*lo))
                x = (t, 0.0)
                e = (x[0] - a*y[0], -lam*y[1])
                close(norm(e), sigma * lam, 1e-8)
                assert norm(y) <= norm(x) / value + 1e-8
                if sigma < 1:
                    As = 1 / (a - sigma * lam)
                    Bs = sigma / math.sqrt((1-sigma*sigma) * (a*a-sigma*sigma*lam*lam))
                    assert abs(y[0]) <= As*abs(x[0]) + 1e-8
                    assert abs(y[1]) <= Bs*abs(x[0]) + 1e-8
                count += 1
        # End-point rotating-orbit equality: exact rational squared norm.
    for lam in (Q(1, 10), Q(1, 3), Q(1), Q(3), Q(10)):
        ctheta = (1 + lam) / (1 + 2 * lam)
        ssquare = 1 - ctheta**2
        defect_square = (1 - (1 + lam)*ctheta)**2 + lam**2 * ssquare
        expected = lam**2 * (2 * lam)/(1 + 2 * lam)
        assert defect_square == expected
        sharp_identities.append(dict(lambda_value=str(lam), cos_theta=str(ctheta),
                                     defect_square=str(defect_square)))
    return dict(samples=count, exact_critical_identities=sharp_identities)


def membership_bounds():
    count = 0
    for y in ((0.1, -0.2), (3.0, 4.0), (-2.0, 1.0)):
        w = y  # Complete F=Id; the exact member is known for verification.
        for delta in (0, 0.01, 0.2):
            for j in range(24):
                angle = 2*math.pi*j/24
                wt = (w[0]+delta*math.cos(angle), w[1]+delta*math.sin(angle))
                Wlo, Whi = max(0, norm(wt)-delta), norm(wt)+delta
                assert Wlo <= norm(w) + TOL <= Whi + 2*TOL
                lam = 3.0
                e = (0.03, -0.04)
                x = tuple(y[i]+lam*w[i]+e[i] for i in range(2))
                et = tuple(x[i]-y[i]-lam*wt[i] for i in range(2))
                assert norm(e) <= norm(et)+lam*delta+TOL
                count += 1
    # Nonzero approximate points never pass in a zero-input kernel fiber.
    sigma = 0.9
    for j in range(1, 100):
        y = (0.0, 1/j)
        e = (0.0, -y[1])  # P=diag(1,0), lambda=1, P x=0.
        assert norm(e) > sigma * norm(y)
    return count


def moving_strong_monotone_counterexamples():
    """Exact arithmetic for root's zero-error singular/SPD moving attacks."""
    lam = Q(1, 10)
    # A = [[1,-3],[3,1]], Px=x in the current-point orthonormal basis.
    yp = (Q(1, 2), Q(-3, 2))
    Ap = (yp[0]-3*yp[1], 3*yp[0]+yp[1])
    assert (1-yp[0], Q(0)) == tuple(lam*a for a in Ap)
    singular_gain_squared = sum(v*v for v in yp)
    assert singular_gain_squared == Q(5, 2) > 1
    # M=diag(1,1/10), T=1/31 [[20,3],[-30,11]].
    T = ((Q(20, 31), Q(3, 31)), (Q(-30, 31), Q(11, 31)))
    for x in ((Q(1), Q(0)), (Q(0), Q(1))):
        y = tuple(sum(T[i][j]*x[j] for j in range(2)) for i in range(2))
        Ay = (y[0]-3*y[1], 3*y[0]+y[1])
        Mdelta = (x[0]-y[0], (x[1]-y[1])/10)
        assert Mdelta == tuple(lam*a for a in Ay)
    trace = T[0][0]+T[1][1]
    det = T[0][0]*T[1][1]-T[0][1]*T[1][0]
    assert trace == 1 and det == Q(10, 31)
    assert trace*trace-4*det < 0 and det < 1
    adaptive_gain_squared = T[0][0]**2+T[1][0]**2
    assert adaptive_gain_squared == Q(1300, 961) > 1
    return dict(singular_gain_squared=str(singular_gain_squared),
                spd_gain_squared=str(adaptive_gain_squared),
                fixed_spd_spectral_radius_squared=str(det),
                fixed_spd_trace=str(trace),
                metric_eigenvalues=["1/10", "1"], error="exactly zero")


def main():
    report = {
        "scope": "finite supplementary checks; analytic proofs remain necessary",
        "seed": "none: deterministic grids",
        "tolerance": TOL,
        "cohypo_profile_cases": scalar_minimum_checks(),
        "diagonal": diagonal_checks(),
        "cohypo_actual_endpoints": cohypo_endpoint_checks(),
        "gu3": gu3_checks(),
        "joint_branch_exact_cases": joint_branch_checks(),
        "projector": projector_checks(),
        "membership_cases": membership_bounds(),
        "moving_strong_monotone_attacks": moving_strong_monotone_counterexamples(),
        "status": "all checks passed",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
