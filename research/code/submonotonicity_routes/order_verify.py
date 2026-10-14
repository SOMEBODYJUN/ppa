#!/usr/bin/env python3
"""Deterministic instance checks for variational_order_review.md.

Standard library only; analytic proofs in the report carry universal claims.
Run: python3 research/code/submonotonicity_routes/order_verify.py
"""
import json
import math


def bisect_root(fun, lo, hi, iterations=65):
    assert fun(lo) <= 1e-12 and fun(hi) >= -1e-12
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if fun(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def rational_quasi():
    lam = 3.0
    f = lambda y: y*y/(1+y*y)
    roots = [0.0, (-3-math.sqrt(5))/2, (-3+math.sqrt(5))/2]
    residuals = [abs(y+lam*f(y)) for y in roots]
    assert max(residuals) < 1e-14
    x = roots[1]
    sample = [x]
    defect = 0.0
    for k in range(1000):
        y = bisect_root(lambda t: t+lam*f(t)-x, x-lam, x)
        assert y < x
        defect = max(defect, abs(y+lam*f(y)-x))
        x = y
        if k+1 in (10, 100, 1000):
            sample.append(x)
    return {"zero_input_roots": roots, "max_zero_equation_defect": max(residuals),
            "negative_branch_samples_k_0_10_100_1000": sample,
            "max_iterated_equation_defect": defect}


def pseudo_multiple_fiber():
    f = lambda y: y*(2+math.sin(y))
    input_value = 3*math.pi
    outputs = [math.pi, 1.5*math.pi]
    defects = [abs(y+f(y)-input_value) for y in outputs]
    assert max(defects) < 1e-14
    return {"input": input_value, "two_distinct_complete_outputs": outputs,
            "equation_defects": defects,
            "zero_set": [0], "all_branch_absolute_contraction_bound": 0.5}


def pseudo_spiral():
    # Integer arithmetic checks the signed nonmonotonicity witness in VO6.
    x, y = (1, 0), (0, -2)
    def field(point):
        u, v = point
        radius_squared = u*u+v*v
        return (-radius_squared*v, radius_squared*u)
    fx, fy = field(x), field(y)
    monotonicity_pairing = sum((b-a)*(v-u) for a,b,u,v in zip(fx,fy,x,y))
    assert monotonicity_pairing == -6
    # Solve r_k^2 = r_{k+1}^2 + lambda^2 r_{k+1}^6.
    lam = 1.0
    r = 0.5
    length = 0.0
    sample = []
    max_defect = 0.0
    previous_v = r**-4
    last_increment = None
    for k in range(1, 200001):
        target = r*r
        rp = bisect_root(lambda t: t*t+lam*lam*t**6-target, 0.0, r)
        max_defect = max(max_defect, abs(rp*rp+lam*lam*rp**6-target))
        length += lam*rp**3
        vp = rp**-4
        last_increment = vp-previous_v
        previous_v = vp
        r = rp
        if k in (100, 1000, 10000, 100000, 200000):
            sample.append({"k": k, "radius": r,
                           "radius_asymptotic_ratio": r*(2*lam*lam*k)**0.25,
                           "partial_length": length})
    assert abs(sample[-1]["radius_asymptotic_ratio"]-1) < 1e-4
    assert abs(last_increment-2*lam*lam) < 1e-4
    return {"nonmonotonicity_witness": {"x": x, "y": y, "F_x": fx, "F_y": fy,
                                        "exact_monotonicity_pairing": monotonicity_pairing},
            "lambda": lam, "initial_radius": 0.5, "samples": sample,
            "last_inverse_fourth_power_increment": last_increment,
            "analytic_limit_of_increment": 2*lam*lam,
            "max_radius_equation_defect": max_defect}


def one_minty_anchor():
    lam = 16/3
    f = lambda y: y*(y-1)**2
    roots = [1.0, 0.25, 0.75]
    defects = [abs(y+lam*f(y)-1) for y in roots]
    assert max(defects) < 1e-14
    # Ratio at the unanchored zero 1 is 1/[y(y-1)].
    ratios = [1/(y*(y-1)) for y in (0.9, 0.99, 0.999, 0.9999)]
    return {"lambda": lam, "complete_zero_set": [0, 1],
            "input_1_three_complete_outputs": roots,
            "equation_defects": defects, "weak_minty_ratio_at_zero_1": ratios}


def cyclic_concave():
    loop = [0.0, 0.17, 0.31, 0.24, 0.09, 0.0]
    lhs = sum(-x*(y-x) for x,y in zip(loop, loop[1:]))
    square = 0.5*sum((y-x)**2 for x,y in zip(loop, loop[1:]))
    assert abs(lhs-square) < 1e-15
    return {"cyclic_sum": lhs, "half_sum_of_squared_edges": square,
            "lambda": 0.5, "complete_proximal_factor": 2,
            "unit_initial_value_after_10_steps": 1024}


def weak_minty_eb_constants():
    rho, lam, eb = -0.2, 1.0, 2.0
    sigma = 1+2*rho/lam
    kappa = eb/math.sqrt(eb*eb+lam*lam*sigma)
    return {"rho": rho, "lambda": lam, "linear_true_EB_C": eb,
            "positive_energy_coefficient": sigma, "distance_factor": kappa,
            "step_over_distance_bound": 1/math.sqrt(sigma),
            "length_over_initial_distance_bound": 1/(math.sqrt(sigma)*(1-kappa))}


if __name__ == "__main__":
    data = {"rational_quasimonotone": rational_quasi(),
            "pseudomonotone_multi_fiber": pseudo_multiple_fiber(),
            "pseudomonotone_infinite_length": pseudo_spiral(),
            "single_minty_anchor_zero_absorption_gap": one_minty_anchor(),
            "cyclic_submonotone_concave": cyclic_concave(),
            "weak_minty_linear_true_EB": weak_minty_eb_constants()}
    print(json.dumps(data, indent=2, ensure_ascii=False))
