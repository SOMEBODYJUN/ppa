#!/usr/bin/env python3
"""Finite checks for the analytic complete-graph forcing frontier.

Python standard library only; no randomness and no general-theorem claim.
Run from the repository root:
    python3 research/code/inexact_forcing_attack/check_frontier.py
"""
import math

GAMMA = 0.5
P = 2.0
A = 1.0
B = 0.25
C = 1.0 - B


def norm(v):
    return math.hypot(*v)


def sub(v, w):
    return tuple(a - b for a, b in zip(v, w))


def prox(u):
    s, t = u
    return (s + A * abs(t) ** GAMMA, B * t)


def operator(y):
    _, z = y
    return (-A * (abs(z) / B) ** GAMMA, C * z / B)


def selected(t):
    return math.hypot(A * abs(t) ** GAMMA, C * t)


def check_step(x, u, eta, q=P, cap=None):
    y = prox(u)
    e = sub(x, u)
    w = operator(y)
    graph_error = norm(sub(sub(x, y), tuple(a + b for a, b in zip(w, e))))
    graph_tolerance = 5e-14 * (norm(x) + norm(y) + norm(w) + norm(e)) + 1e-300
    assert graph_error <= graph_tolerance, (x, u, graph_error)
    stop_rhs = eta * norm(w) ** q
    stop_tolerance = 2e-13 * max(norm(e), stop_rhs, 1e-300)
    assert norm(e) <= stop_rhs + stop_tolerance, (e, w)
    if cap is not None:
        assert norm(w) <= cap + 2e-13 * max(norm(w), cap, 1e-300)
    return y


def main():
    radius = 0.01
    holder_l = radius ** (1.0 - GAMMA) + 2.0 * A
    compatibility = B * (1.0 + radius ** (1.0 - GAMMA) / A) ** P
    residual_budget = (radius + holder_l * radius ** GAMMA) / 2.0
    assert compatibility < 0.5
    assert residual_budget < 1.0
    print(f"Exact C02 complete-graph gates: L={holder_l:.12g}, "
          f"compatibility={compatibility:.12g}, B(R)={residual_budget:.12g}")

    cap_parameter = 0.01
    cap = selected(cap_parameter)
    h_cap = selected(cap_parameter) ** P / cap_parameter
    eta_conv = C / h_cap
    eta_abs = 1.0 / h_cap
    assert eta_conv < 0.75 < eta_abs
    print(f"Finite cap frontier: eta_conv={eta_conv:.12g}, "
          f"eta_abs={eta_abs:.12g}, selected cap={cap:.12g}")

    endpoint_y = check_step((0.0, B * cap_parameter), (0.0, cap_parameter),
                            eta=eta_conv, cap=cap)
    assert endpoint_y[1] == B * cap_parameter
    zero_endpoint_y = check_step((0.0, 0.0), (0.0, cap_parameter),
                                 eta=eta_abs, cap=cap)
    assert zero_endpoint_y[1] > 0.0
    print("Exact finite-cap endpoint: drift and zero-escape boundary steps verified.")

    for sign in (1.0, -1.0):
        t = sign * 1e-8
        x = (0.0, B * t)
        for _ in range(5):
            y = check_step(x, (x[0], t), eta=0.75, cap=cap)
            assert y[1] == x[1]
            assert math.isclose(y[0] - x[0], abs(t) ** GAMMA,
                                rel_tol=2e-12, abs_tol=1e-16)
            x = y
    print("Critical coefficient: both-sign constant-distance drift verified.")

    for q in (1.0, 1.5):
        eta = 0.01
        t = 1e-24
        check_step((0.0, 0.0), (0.0, t), eta=eta, q=q, cap=cap)
        check_step((0.0, B * t), (0.0, t), eta=eta, q=q, cap=cap)
    print("Subcritical powers: tiny zero escape and drift steps verified.")

    q = 3.0
    eta = 100.0
    tiny_cap = 1e-8
    h_tiny = selected(tiny_cap) ** q / tiny_cap
    assert eta * h_tiny < C
    print(f"Higher power q=3: coefficient 100 admitted on tiny cap; "
          f"delta={eta*h_tiny:.12g} < {C:.12g}.")

    x = check_step((0.0, 0.0), (0.0, 16.0), eta=0.1)
    assert x == (4.0, 4.0)
    for k in range(2, 7):
        x = check_step(x, (x[0], 16.0), eta=0.1)
        assert x == (4.0 * k, 4.0)
    print("No cap: exact zero-input escape followed by far divergent drift verified.")

    cross_eta = 1.01 / h_cap
    t = cap_parameter
    eps = 0.005 * t
    y = check_step((0.0, -eps), (0.0, t), eta=cross_eta, cap=cap)
    assert y[1] > 0.0
    print("Above absorption threshold: opposite-sign accepted output verified.")

    hypo_ratios = []
    co_ratios = []
    for t in (1e-4, 1e-8, 1e-12):
        y = (t, t)
        w = operator(y)
        hypo_ratios.append(sum(a*b for a, b in zip(w, y)) / norm(y)**2)
        yc = (t ** (GAMMA / 2.0), t)
        wc = operator(yc)
        co_ratios.append(sum(a*b for a, b in zip(wc, yc)) / norm(wc)**2)
    assert all(a > b for a, b in zip(hypo_ratios, hypo_ratios[1:]))
    assert all(a > b for a, b in zip(co_ratios, co_ratios[1:]))
    print(f"Hypomonotonicity ratios: {hypo_ratios}")
    print(f"Cohypomonotonicity ratios: {co_ratios}")
    print("All finite instance checks passed; analytic proofs are in the note.")


if __name__ == "__main__":
    main()
