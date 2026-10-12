#!/usr/bin/env python3
"""Finite arithmetic/back-substitution checks, not proofs of complete relations."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform
import numpy as np

SEED = 266269
rng = np.random.default_rng(SEED)


def norm(x):
    return float(np.linalg.norm(x))


def power(x, exponent):
    r = norm(x)
    return np.zeros_like(x) if r == 0 else r ** (exponent - 1) * x


def gap(x, s):
    return .75 * norm(x) ** (4 / 3) + .25 * norm(s) ** 4 - float(x @ s)


def check_le(a, b):
    assert a <= b + 2e-10 * max(1., abs(a), abs(b)), (a, b)


def intervals_integral(intervals, t, a):
    pieces = sorted((max(0., l), min(t, u)) for l, u in intervals if l < t)
    merged = []
    for l, u in pieces:
        if l >= u:
            continue
        if merged and l <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], u)
        else:
            merged.append([l, u])
    return sum(u ** a - l ** a for l, u in merged)


results = {"python": platform.python_version(), "numpy": np.__version__, "seed": SEED}

# OP4: exact coefficient product, discriminant, and the firm witness.
p = [Q(-1, 2), Q(1)]
q = [Q(1, 2), Q(2), Q(4)]
prod = [Q(0)] * 4
for i, x in enumerate(p):
    for j, y in enumerate(q):
        prod[i + j] += x * y
assert prod == [Q(-1, 4), Q(-1, 2), Q(0), Q(4)]
assert q[1] ** 2 - 4 * q[2] * q[0] == -4
assert Q(3, 2) * (Q(5, 4) - Q(3, 2)) == Q(-3, 8)
results["argmin_exact"] = {"shifted_derivative_coefficients": [str(t) for t in prod],
                           "quadratic_discriminant": "-4", "firm_product": "-3/8"}

# PK1/2 exponent corners, including a<1, q gamma=1 and ordinary distance power.
corners = [(Q(1, 100), Q(100)), (Q(1, 5), Q(5)), (Q(1, 2), Q(2)),
           (Q(2, 3), Q(3, 2)), (Q(3, 4), Q(2)), (Q(1), Q(1)), (Q(1), Q(1000))]
out = []
for gamma, qval in corners:
    b = 1 / qval
    a = min(2 * gamma, 1 + b)
    theta = b / a
    assert 0 < 2 * b <= a <= 2 and a <= 2 * gamma and theta <= Q(1, 2)
    R = .5 if a >= 1 else min(.5, float(a) ** (1 / float(1 + b - a)) / 2)
    assert R ** float(1 + b - a) <= float(a) + 1e-15
    out.append({"gamma": str(gamma), "q": str(qval), "a": str(a),
                "b": str(b), "theta": str(theta), "R": R})
results["exponent_corners"] = out

# PK6: finite dense-interval prefix and the restricted-index weighted sum.
centers = []
seen = set()
for denominator in range(2, 30):
    for numerator in range(1, denominator):
        val = Q(numerator, denominator)
        if val not in seen:
            seen.add(val)
            centers.append(float(val) / 2)
eps = .1
R = .5
intervals = [(r * (1 - eps * 2. ** (-j - 5)),
              min(R, r * (1 + eps * 2. ** (-j - 5))))
             for j, r in enumerate(centers[:150], start=1)]
weighted_checks = 0
for a in [.02, .2, .4, 1., 1.5, 2.]:
    for t in R * np.geomspace(1e-9, 1., 70):
        lhs = intervals_integral(intervals, float(t), a)
        check_le(lhs, .375 * eps * float(t) ** a)
        weighted_checks += 1
results["weighted_interval_prefix_checks"] = weighted_checks

# FY2/3/5: all-sign back substitution and actual nearest point candidates (finite samples).
fy_checks = 0
nearest_checks = 0
for a in [-8., -1., -.01, 0., .01, 1., 8.]:
    for b in [-3., -1., -.03, 0., .03, 1., 3.]:
        y = np.array([a, np.cbrt(a)])
        F = np.array([np.cbrt(y[0]) - y[1], y[1] ** 3 - y[0]])
        assert norm(F) < 1e-12
        assert norm(np.array([a, 0.]) - np.array([y[0], 0.]) - 2 * F) < 1e-12
        roots = np.roots([3., 0., 0., -3 * a, 1., -b])
        real = [float(z.real) for z in roots if abs(z.imag) < 1e-7]
        assert real
        c = min(real, key=lambda z: (a - z ** 3) ** 2 + (b - z) ** 2)
        d = np.hypot(a - c ** 3, b - c)
        check_le(abs(a - c ** 3), d)
        if d <= 1 + 1e-12:
            check_le(norm(y - [a, b]), 3 * d ** (1 / 3))
            nearest_checks += 1
        fy_checks += 1
for u in [-10., -1., -.001, 0., .001, 1., 10.]:
    for w in [-10., -1., -.001, 0., .001, 1., 10.]:
        check_le(abs(np.cbrt(u) - np.cbrt(w)), (4 * abs(u - w)) ** (1 / 3))
results["one_step_fy_back_substitutions"] = fy_checks
results["nearest_curve_finite_checks"] = nearest_checks

# VF2-8: generate arbitrary stationary roots then reverse to their real input.
vector_checks = 0
max_reverse_error = 0.
for n in [1, 2, 4]:
    for lam in [.01, 1., 10., 100.]:
        for scale in [1e-4, .1, 1., 10.]:
            for _ in range(30):
                r = scale * rng.normal(size=n)
                s = scale * rng.normal(size=n)
                if vector_checks % 23 == 0:
                    s = -r
                if vector_checks % 29 == 0:
                    s = np.zeros(n)
                x = power(r, 3)
                qvec = x - power(s, 3)
                e = r - s
                a = x + lam * e
                b = power(power(s, 5) - lam * qvec, 1 / 5)
                err = norm(power(b, 5) - power(s, 5) + lam * qvec)
                relative_err = err / max(1., norm(power(b, 5)), norm(power(s, 5)), lam * norm(qvec))
                assert relative_err < 1e-10
                max_reverse_error = max(max_reverse_error, relative_err)
                M = max(norm(a) ** (1 / 3), norm(b))
                check_le(max(norm(r), norm(s)), M)
                N = a - power(b, 3)
                rho = 1 / (1 + 14 * lam / (15 * M * M))
                check_le(norm(qvec), rho * norm(N))
                check_le(norm(e), (4 * norm(qvec)) ** (1 / 3))
                check_le(norm(s - b), (16 * lam * norm(qvec)) ** (1 / 5))
                step = norm(np.concatenate([a - x, b - s]))
                check_le(step, lam * (4 * norm(qvec)) ** (1 / 3) + (16 * lam * norm(qvec)) ** (1 / 5))
                # Independent natural-energy identity V3 from the second proof.
                dvec = b - s
                Dphi = .75 * (norm(a) ** (4 / 3) - norm(x) ** (4 / 3)) - float(r @ (a - x))
                Dpsi = .25 * (norm(b) ** 4 - norm(s) ** 4) - float(power(s, 3) @ dvec)
                delta = gap(a, b) - gap(x, s)
                rhs = Dphi + Dpsi + lam * norm(e) ** 2 + float((power(b, 5) - power(s, 5)) @ dvec) / lam - lam * float(e @ dvec)
                assert abs(delta - rhs) < 2e-8 * max(1., abs(delta), abs(rhs))
                check_le(norm(dvec) ** 4 / 12, Dpsi)
                check_le(float(e @ dvec), 0.)
                vector_checks += 1
results["vector_stationary_reverse_checks"] = vector_checks
results["max_relative_reverse_error"] = max_reverse_error

# H1 counter-family, finite diagnostic only; the order argument is analytic.
counter = []
lam = 10.
for t in [.1, .03, .01, .003, .001]:
    r = np.array([t])
    s = np.array([t + t ** 3 / lam])
    x = power(r, 3)
    b = power(power(s, 5) + lam * (power(s, 3) - x), .2)
    step2 = norm(x) ** 2 + norm(s - b) ** 2
    counter.append({"t": t, "input_gap_over_step2": gap(np.zeros(1), b) / step2,
                    "b_over_t": float(b[0] / t)})
assert counter[-1]["input_gap_over_step2"] < counter[0]["input_gap_over_step2"] / 1000
results["natural_quadratic_H1_counter_family"] = counter

# GR3/4/6/10: reverse arbitrary unique stationary outputs through the full Gram inverse.
def gram_v(Z):
    return Z @ Z.T @ Z


def gram_inverse(W):
    left, singular, right = np.linalg.svd(W, full_matrices=False)
    return (left * np.cbrt(singular)) @ right


gram_checks = 0
for m in [2, 3, 5]:
    for lam in [.03, 1., 10.]:
        for scale in [.001, .1, 1., 3.]:
            for _ in range(15):
                Y = scale * rng.normal(size=(m, 2))
                if gram_checks % 17 == 0:
                    Y[:, 1] = 0.
                F = np.zeros_like(Y)
                F[:, 0] = Y[:, 0]
                Z = gram_inverse(gram_v(Y) + lam * F)
                incoming, outgoing = gram_v(Z), gram_v(Y)
                rel = norm(incoming - outgoing - lam * F) / max(1., norm(incoming))
                assert rel < 1e-9
                check_le(norm(Y - Z), 2 * norm(outgoing - incoming) ** (1 / 3))
                uin, uout = incoming[:, 0], outgoing[:, 0]
                check_le(norm(uout) ** 2 + lam ** 2 * norm(Y[:, 0]) ** 2, norm(uin) ** 2)
                assert norm(incoming[:, 1] - outgoing[:, 1]) < 1e-8 * max(1., norm(incoming))
                P = Z.copy()
                P[:, 0] = 0.
                delta = norm(incoming - gram_v(P))
                check_le(norm(2 * outgoing - incoming - gram_v(P)), delta)
                d = norm(Z[:, 0])
                if lam == 10 and d <= 1e-6 and norm(Z[:, 1]) < 2:
                    check_le(delta, 5 * d)
                    check_le(norm(Y[:, 0]), .5 * d)
                M = (2 * norm(incoming)) ** (1 / 3)
                rho = M ** 2 / np.sqrt(M ** 4 + lam ** 2)
                check_le(norm(uout), rho * norm(uin))
                gram_checks += 1
ThetaR = 2 * 5 ** (1 / 3) * .01 / (1 - 2 ** (-1 / 3))
assert ThetaR < .167
results["gram_stationary_reverse_checks"] = gram_checks
results["gram_Theta_R"] = ThetaR

# Scalar balanced t^7 perturbation: use scaled variables to avoid cancellation near zero.
from scipy.optimize import root
scaled_gram = []
lam = 10.
zeta = 1.
for t in [.2, .1, .03, .01, .003]:
    def equations(uv):
        U, V = uv
        return [lam * U + t ** 6 * (U * U + V * V) * U - 1 - zeta ** 2 * t ** 12,
                (U * U + V * V) * V - zeta - zeta ** 3 * t ** 12]
    solve = root(equations, [.1, 1.])
    assert solve.success and norm(np.array(equations(solve.x))) < 1e-9
    U, V = solve.x
    check_le(0., V)
    scaled_gram.append({"t": t, "U": float(U), "V": float(V),
                        "pair_input_distance": t ** 7, "output_second_column": t ** 3 * float(V)})
results["gram_t7_reverse_family"] = scaled_gram

# Work-window boundaries (d=R, b=0/1/near2), independent scalar root arithmetic.
boundary_checks = 0
for a0 in [-1e-6, 0., 1e-6]:
    for b0 in [-1.999, -1., 0., 1., 1.999]:
        uin = a0 * (a0 * a0 + b0 * b0)
        kin = b0 * (a0 * a0 + b0 * b0)
        if b0 == 0:
            # u^3+10u=a0^3; monotone bisection avoids tiny-root solver tolerances.
            low, high = sorted([0., a0])
            for _ in range(90):
                middle = (low + high) / 2
                if middle ** 3 + 10 * middle < uin:
                    low = middle
                else:
                    high = middle
            u, w = (low + high) / 2, 0.
        else:
            def equations(uw):
                u, w = uw
                return [(u * u + w * w + 10) * u - uin, (u * u + w * w) * w - kin]
            sol = root(equations, [uin / (10 + b0 * b0), b0])
            assert sol.success and norm(np.array(equations(sol.x))) < 1e-10
            u, w = sol.x
        Zin = np.array([[a0, b0], [0., 0.]])
        Yout = np.array([[u, w], [0., 0.]])
        P = Zin.copy()
        P[:, 0] = 0.
        delta = norm(gram_v(Zin) - gram_v(P))
        check_le(delta, 5 * abs(a0))
        check_le(norm(2 * gram_v(Yout) - gram_v(Zin) - gram_v(P)), delta)
        check_le(abs(u), .5 * abs(a0))
        check_le(norm(Yout - Zin), 2 * norm(gram_v(Yout) - gram_v(Zin)) ** (1 / 3))
        boundary_checks += 1
results["gram_work_window_boundary_checks"] = boundary_checks
results["scope"] = "Finite arithmetic only: no certification of all fibers, limiting subgradients, KL, infinite trajectories, optimal exponents, or priority. Universal conclusions are analytic in the canonical texts."
results["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
target = Path(__file__).with_name("results.json")
target.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"output": str(target), "sha256": results["script_sha256"],
                  "vector_checks": vector_checks, "weighted_checks": weighted_checks}, ensure_ascii=False))
