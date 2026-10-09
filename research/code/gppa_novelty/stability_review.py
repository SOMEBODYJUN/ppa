#!/usr/bin/env python3
"""Finite arithmetic checks for the 2026-10-09 stability review.

The general theorem is proved in Markdown. These checks verify graph identities,
an exact affine fixed orbit, and the harmonic orbit attaining the skew-family
bound. They do not claim worst-case sharpness over arbitrary monotone relations.
"""

from fractions import Fraction as Q
import json
import math


def check_exact_identities():
    # Orthogonal r and w attain the cancellation squared identity.
    alpha = Q(7, 5)
    w = (Q(3), Q(0))
    residual = (Q(0), Q(4))
    u = tuple(alpha * x + y for x, y in zip(w, residual))
    dot = lambda x, y: sum(a * b for a, b in zip(x, y))
    assert dot(residual, w) == 0
    assert dot(residual, residual) == dot(u, u) - alpha**2 * dot(w, w)

    # F=N_[s,infinity), v=Id: a legal one-step output at s attains RS9.
    s, distance, lam, eps = Q(2), Q(3), Q(2, 3), Q(1, 4)
    incoming, exact_output = s - distance, s
    f = (incoming - exact_output) / lam - eps * exact_output
    assert f <= 0  # exact_output=s, so f lies in the full normal-cone fibre
    assert abs(f) == distance / lam + eps * s

    # Exact fixed orbit for F(x)=mu(x-s); persistent constant negative error.
    mu, lam, eps, s, delta = Q(1), Q(1), Q(1, 10), Q(2), Q(1, 100)
    s_eps = mu * s / (mu + eps)
    p = 1 / (1 + lam * (mu + eps))
    x = s_eps - delta / (1 - p)
    hat = s_eps + p * (x - s_eps)
    f = mu * (hat - s)
    assert hat - delta == x
    assert x - hat == lam * (f + eps * hat)
    distance_tube = eps * abs(s) / (mu + eps) + delta / (1 - p)
    residual_tube = mu * eps * abs(s) / (mu + eps) + mu * delta / (lam * (mu + eps))
    assert abs(x - s) == distance_tube
    assert abs(f) == residual_tube

    # Same-object overlap: earlier 2606.01536v2 T3 vs C216, rho(t)=t/mu.
    a = abs(s)
    b = delta * (1 + lam * eps) / (lam**2 * eps) + eps * a
    c216 = delta + b / mu
    earlier_t3 = delta * (1 + 1 / (lam * eps)) + eps * a / mu
    assert c216 - earlier_t3 == delta
    assert distance_tube < earlier_t3 < c216

    # Global inverse gate has L/m >= 1: charging physical error at hat is tighter.
    L, inverse_lower = Q(3), Q(2)
    actual_noise = L * delta / inverse_lower * (1 + 1 / (lam * eps))
    hat_noise = delta + L * delta / (inverse_lower * lam * eps)
    assert actual_noise - hat_noise == delta * (L / inverse_lower - 1) > 0
    return {
        "affine_exact_distance": str(distance_tube),
        "affine_exact_residual": str(residual_tube),
        "earlier_t3_distance": str(earlier_t3),
        "c216_distance": str(c216),
        "actual_minus_hat_noise": str(actual_noise - hat_noise),
    }


def check_skew_family():
    rows = []
    for alpha in [1.0001, 1.01, 1.1, 2.0, 10.0]:
        lam, delta = 0.7, 0.03
        dimensionless_beta = alpha * math.sqrt(alpha * alpha - 1)
        beta = dimensionless_beta / lam
        t = 1 / complex(alpha, lam * beta)
        radius = abs(t)
        phase = t / radius
        amplitude = delta / (1 - radius)
        maximum = delta / lam * alpha / math.sqrt(alpha * alpha - 1)
        for k in [0, 1, 3, 19]:
            x = amplitude * phase**k
            x_next = amplitude * phase ** (k + 1)
            error = delta * phase ** (k + 1)
            hat = t * x
            f = 1j * beta * hat
            assert abs(x_next - hat - error) < 1e-10 * max(1, amplitude)
            assert abs(x - hat - lam * (f + (alpha - 1) / lam * hat)) < 1e-10 * max(1, amplitude)
            assert math.isclose(abs(error), delta, rel_tol=1e-11)
            assert math.isclose(abs(f), maximum, rel_tol=1e-9)
        # Sample either side of the analytic stationary point and broad ends.
        for scale in [0.001, 0.1, 0.5, 1, 2, 10, 1000]:
            b = dimensionless_beta * scale
            gain = b / (math.sqrt(alpha * alpha + b * b) - 1)
            assert gain <= alpha / math.sqrt(alpha * alpha - 1) * (1 + 1e-9)
        c216_residual = delta / lam * alpha / (alpha - 1)
        assert maximum < c216_residual
        rows.append({
            "alpha": alpha,
            "lambda_beta_at_maximum": dimensionless_beta,
            "skew_sharp_residual": maximum,
            "c216_residual": c216_residual,
        })
    return rows


if __name__ == "__main__":
    print(json.dumps({"exact_checks": check_exact_identities(), "skew_family": check_skew_family()}, indent=2))
