#!/usr/bin/env python3
"""Exact scalar certificate plus finite numerical attacks of a Gaussian PPA.

Run: python research/code/gaussian_mixture_zero_inference/verify.py
Only the Fraction assertions are exact. Float64 root discovery is neither a
complete zero enumeration nor a proof of any universal quantifier.
"""
from fractions import Fraction
from pathlib import Path
import json
import math
import platform

import numpy as np
import scipy
from scipy.optimize import root

MU = np.array([[-4.0, 0.0], [4.0, 0.0], [0.0, 5.0]])
W = np.array([1.0, 2.0, 3.0]) / 6.0
LAM = 1.0 / 16.0
M = 0.9
R = 1e-5
KAPPA = 1.0 / math.sqrt(1.0 + (LAM * M) ** 2)


def data(x):
    x = np.asarray(x, dtype=float)
    logits = np.log(W) + MU @ x - np.sum(MU * MU, axis=1) / 2
    probs = np.exp(logits - logits.max())
    probs /= probs.sum()
    g = probs @ MU
    delta = MU - g
    covariance = np.einsum("i,ij,ik->jk", probs, delta, delta)
    return x - g, np.eye(2) - covariance, probs


def prox(x):
    x = np.asarray(x, dtype=float)
    out = root(lambda y: y + LAM * data(y)[0] - x,
               x / (1 + LAM),
               jac=lambda y: np.eye(2) + LAM * data(y)[1],
               tol=1e-12)
    residual = np.linalg.norm(out.x + LAM * data(out.x)[0] - x)
    assert residual < 2e-10 * max(1.0, np.linalg.norm(x)), (x, out, residual)
    return out.x


def classify(x):
    eig = np.linalg.eigvalsh(data(x)[1])
    return "minimum" if eig.min() > 0 else (
        "maximum" if eig.max() < 0 else "saddle")


def main():
    # A finite Taylor sum is a strict lower bound for exp(18).
    taylor18 = sum((Fraction(18) ** k / math.factorial(k)
                    for k in range(19)), Fraction(0))
    assert taylor18 > 10**7
    off_ratio_bound = Fraction(3, 10**7)
    off_mass_bound = 2 * off_ratio_bound
    covariance_bound = 64 * off_mass_bound
    center_residual_bound = 8 * off_mass_bound
    assert covariance_bound < Fraction(1, 10)
    assert center_residual_bound < Fraction(5, 10**6)
    assert center_residual_bound / Fraction(9, 10) < Fraction(1, 10**5)
    # Exact kappa < .999, hence Theta(R) < 1000 R = .01.
    kappa_squared = Fraction(25600, 25681)
    assert kappa_squared < Fraction(999, 1000) ** 2
    budget_lower = Fraction(1, 20) - 2 * Fraction(1, 10**5)
    assert Fraction(1, 100) < budget_lower
    boundary_lower = ((1 + Fraction(1, 16) * Fraction(9, 10))
                      * Fraction(1, 10)**2
                      - Fraction(1, 10) * (Fraction(1, 10**5)
                         + Fraction(1, 10**5)
                         + Fraction(1, 16) * Fraction(5, 10**6)))
    assert boundary_lower > 0

    minima = []
    for mu in MU:
        out = root(lambda x: data(x)[0], mu,
                   jac=lambda x: data(x)[1], tol=1e-12)
        assert np.linalg.norm(data(out.x)[0]) < 1e-12
        assert np.linalg.norm(out.x - mu) < 1e-5
        minima.append(out.x)

    center_start_orbits = []
    for mu, p in zip(MU, minima):
        x = mu.copy()
        length = 0.0
        max_distance = float(np.linalg.norm(x-p))
        steps = 0
        while np.linalg.norm(data(x)[0]) > 1e-12 and steps < 500:
            y = prox(x)
            length += float(np.linalg.norm(y-x))
            x = y
            steps += 1
            max_distance = max(max_distance, float(np.linalg.norm(x-p)))
        assert np.linalg.norm(data(x)[0]) <= 1e-12
        assert max_distance <= R
        center_start_orbits.append({"start": mu.tolist(), "steps": steps,
            "terminal_point": x.tolist(), "terminal_true_residual": float(np.linalg.norm(data(x)[0])),
            "total_length": length, "max_distance_to_numerical_root": max_distance})

    found = []
    attempts = 0
    for a in np.linspace(-4, 4, 25):
        for b in np.linspace(0, 5, 25):
            attempts += 1
            out = root(lambda x: data(x)[0], [a, b],
                       jac=lambda x: data(x)[1], tol=1e-11)
            if (np.linalg.norm(data(out.x)[0]) < 1e-9
                    and not any(np.linalg.norm(out.x - z) < 1e-5 for z in found)):
                found.append(out.x)
    found.sort(key=lambda x: tuple(x))
    roots = []
    for x in found:
        vals, vectors = np.linalg.eigh(data(x)[1])
        eps = 1e-6
        numerical_forward = []
        numerical_reverse = []
        for direction in vectors.T:
            perturbed = x + eps * direction
            numerical_forward.append(float(np.linalg.norm(prox(perturbed) - x) / eps))
            numerical_reverse.append(float(np.linalg.norm(
                perturbed + LAM * data(perturbed)[0] - x) / eps))
        roots.append({"point": x.tolist(), "type": classify(x),
                      "true_residual": float(np.linalg.norm(data(x)[0])),
                      "hessian_eigenvalues": vals.tolist(),
                      "PPA_derivative_eigenvalues": (1/(1+LAM*vals)).tolist(),
                      "forward_eigen_direction_finite_ratio": numerical_forward,
                      "reverse_H_eigen_direction_finite_ratio": numerical_reverse,
                      "observed_index": int(np.sign(np.prod(vals)))})

    rng = np.random.default_rng(20261013)
    local_ratios = []
    reflected_ratios = []
    eb_ratios = []
    for p in minima:
        for _ in range(128):
            direction = rng.normal(size=2)
            direction /= np.linalg.norm(direction)
            d = R * rng.uniform(0.2, 1.0)
            x = p + d * direction
            y = prox(x)
            local_ratios.append(float(np.linalg.norm(y-p)/np.linalg.norm(x-p)))
            reflected_ratios.append(float(np.linalg.norm(2*y-x-p)/np.linalg.norm(x-p)))
            eb_ratios.append(float(np.linalg.norm(data(y)[0])/np.linalg.norm(y-p)))
    assert max(local_ratios) < KAPPA + 1e-6
    assert max(reflected_ratios) < 1 + 1e-6
    assert min(eb_ratios) > M - 1e-6

    angles = np.linspace(0, 2*np.pi, 720, endpoint=False)
    boundary = 6 * np.array([np.cos(angles), np.sin(angles)]).T
    boundary_prox_norms = [float(np.linalg.norm(prox(x))) for x in boundary]
    boundary_residuals = [float(np.linalg.norm(data(x)[0])) for x in boundary]
    assert max(boundary_prox_norms) <= 101/17 + 1e-9
    assert min(boundary_residuals) >= 1 - 1e-9

    far_inputs = []
    for magnitude in (1000.0, 1000000.0):
        for direction in ([1, 0], [0, 1], [0, -1], [1, 1], [-1, 1]):
            direction = np.asarray(direction, dtype=float)
            direction /= np.linalg.norm(direction)
            x = magnitude * direction
            y = prox(x)
            far_inputs.append({"input": x.tolist(), "output": y.tolist(),
                "prox_equation_residual": float(np.linalg.norm(y+LAM*data(y)[0]-x)),
                "C_norm_over_input_norm": float(np.linalg.norm(2*y-x)/magnitude)})

    out = {
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "seed": 20261013, "precision": "float64"},
        "scope": "Exact Fraction scalar assertions; finite float64 attacks, not full zero enumeration.",
        "parameters": {"centers": MU.tolist(), "weights": W.tolist(), "lambda": LAM,
                       "m": M, "R": R, "bar_t": R/LAM, "M0": R/LAM/M,
                       "kappa": KAPPA, "Theta_R": R/(1-KAPPA),
                       "local_strong_monotone_PPA_factor": 1/(1+LAM*M)},
        "exact_bounds": {"Taylor_exp18_lower_numerator": str(taylor18.numerator),
                         "Taylor_exp18_lower_denominator": str(taylor18.denominator),
                         "Taylor_exp18_lower_float": float(taylor18),
                         "off_ratio_bound": str(off_ratio_bound),
                         "off_mass_bound": str(off_mass_bound),
                         "covariance_bound": str(covariance_bound),
                         "center_residual_bound": str(center_residual_bound),
                         "boundary_outward_lower": str(boundary_lower),
                         "budget_lower": str(budget_lower)},
        "certified_center_roots_numerical_representatives": [p.tolist() for p in minima],
        "complete_PPA_center_start_orbits": center_start_orbits,
        "discovery_attempts": attempts, "discovered_roots": roots,
        "observed_counts": {kind: sum(r["type"] == kind for r in roots)
                            for kind in ("minimum", "saddle", "maximum")},
        "observed_total_index": sum(r["observed_index"] for r in roots),
        "local_tests": {"samples": len(local_ratios),
                       "max_PPA_distance_ratio": max(local_ratios),
                       "max_reflected_anchor_ratio": max(reflected_ratios),
                       "min_true_residual_over_distance": min(eb_ratios)},
        "global_boundary_tests": {"samples": len(boundary),
                                 "max_prox_norm": max(boundary_prox_norms),
                                 "min_true_residual": min(boundary_residuals),
                                 "proven_prox_upper": 101/17, "proven_residual_lower": 1},
        "far_input_tests": far_inputs,
        "reliable_unknown_cluster_conclusion": {"total_index": -2, "nonempty": True,
             "number_lower_bound": 1,
             "exclusion": "No assertion of exactly two saddles or at least two unknown roots."},
    }
    target = Path(__file__).with_name("results.json")
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"result": "passed", "json": str(target),
                      "observed_counts": out["observed_counts"],
                      "observed_total_index": out["observed_total_index"],
                      "kappa": KAPPA, "Theta_R": R/(1-KAPPA),
                      "local_tests": out["local_tests"],
                      "global_boundary_tests": out["global_boundary_tests"]}, indent=2))


if __name__ == "__main__":
    main()
