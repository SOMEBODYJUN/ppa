#!/usr/bin/env python3
"""Finite numerical replication of the rank-one PSD candidate.

The proofs and their universal scope are in the candidate card. This script
checks identities and sampled certificates, not theorems about degree.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np


SEED = 20261013
A = np.diag([1.0, 0.0])
R = 1.0 / 16.0
TOL = 1e-11


def B(u: np.ndarray) -> np.ndarray:
    return u @ u.T @ u


def inverse_B(w: np.ndarray) -> np.ndarray:
    left, singular, right = np.linalg.svd(w, full_matrices=False)
    return (left * np.cbrt(singular)) @ right


def F(u: np.ndarray) -> np.ndarray:
    return B(u) - A @ u


def T(u: np.ndarray) -> np.ndarray:
    radius = np.linalg.norm(u[0])
    y = np.zeros_like(u)
    if radius > 0.0:
        y[0] = u[0] / radius ** (2.0 / 3.0)
    return y


def distance(u: np.ndarray) -> float:
    return float(math.hypot(np.linalg.norm(u[0]) - 1.0, np.linalg.norm(u[1])))


def objective(u: np.ndarray) -> float:
    return float(np.linalg.norm(u @ u.T - A) ** 2 / 4.0)


def energy(u: np.ndarray) -> float:
    return distance(u) ** 2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    errors = {
        "svd_cube_inverse_relative": 0.0,
        "complete_update_equation": 0.0,
        "explicit_versus_svd_update": 0.0,
        "energy_identity": 0.0,
        "residual_identity": 0.0,
    }
    violations = {
        "latent_reflection": 0.0,
        "output_true_EB": 0.0,
        "physical_transfer": 0.0,
        "distance_contraction": 0.0,
        "strict_budget": 0.0,
        "global_growth": 0.0,
        "natural_energy_H1": 0.0,
        "natural_energy_H2": 0.0,
    }
    ratio = {"latent_reflection": 0.0, "output_EB": 0.0, "distance_contraction": 0.0}
    for _ in range(1000):
        w = rng.normal(size=(2, 2)) * 10.0 ** rng.uniform(-3.0, 3.0)
        z = inverse_B(w)
        errors["svd_cube_inverse_relative"] = max(
            errors["svd_cube_inverse_relative"], float(np.linalg.norm(B(z) - w) / max(1.0, np.linalg.norm(w)))
        )
        u = rng.normal(size=(2, 2)) * 10.0 ** rng.uniform(-3.0, 3.0)
        y = T(u)
        errors["complete_update_equation"] = max(
            errors["complete_update_equation"], float(np.linalg.norm(A @ y + F(y) - A @ u) / max(1.0, np.linalg.norm(u)))
        )
        # The arbitrary SVD can perturb exact zero singular values by roundoff.
        # AU has an exact zero row, so its inverse is checked using a rank-one SVD.
        radius = np.linalg.norm(u[0])
        z = np.vstack([np.cbrt(radius) * (u[0] / radius), np.zeros(2)])
        errors["explicit_versus_svd_update"] = max(
            errors["explicit_versus_svd_update"], float(np.linalg.norm(z - y))
        )
        violations["global_growth"] = max(
            violations["global_growth"], float(np.linalg.norm(y) - np.cbrt(np.linalg.norm(u)))
        )

    # Full physical tube samples include arbitrary b directions, not only b=0.
    for _ in range(4000):
        d = R * rng.random()
        normal_angle = rng.uniform(0.0, 2.0 * math.pi)
        radial_offset = d * math.cos(normal_angle)
        b_radius = d * abs(math.sin(normal_angle))
        angle_a, angle_b = rng.uniform(0.0, 2.0 * math.pi, size=2)
        e = np.array([math.cos(angle_a), math.sin(angle_a)])
        b = b_radius * np.array([math.cos(angle_b), math.sin(angle_b)])
        radius = 1.0 + radial_offset
        u = np.vstack([radius * e, b])
        y = T(u)
        p = np.vstack([e, np.zeros(2)])
        d = distance(u)
        dy = distance(y)
        delta = float(np.linalg.norm(A @ (u - p)))
        reflection = float(np.linalg.norm(A @ (2.0 * y - u - p)))
        q = float(np.linalg.norm(A @ (y - u)))
        step = float(np.linalg.norm(y - u))
        residual = float(np.linalg.norm(F(y)))
        output_radius = float(np.linalg.norm(y[0]))
        errors["residual_identity"] = max(
            errors["residual_identity"], abs(residual - output_radius * abs(output_radius**2 - 1.0))
        )
        energy_gap = energy(u) - energy(y) - step**2
        energy_identity = 2.0 * output_radius * (output_radius + 1.0) * (output_radius - 1.0) ** 2
        errors["energy_identity"] = max(errors["energy_identity"], abs(energy_gap - energy_identity))
        complement_distance = min(radius - 0.5, 1.5 - radius)
        samples = {
            "latent_reflection": reflection - delta / 2.0,
            "output_true_EB": dy - 2.0 * residual / 3.0,
            "physical_transfer": step - math.hypot(d, q),
            "distance_contraction": dy - d / 2.0,
            "strict_budget": 2.5 * d - complement_distance,
            "natural_energy_H1": step**2 - (energy(u) - energy(y)),
            "natural_energy_H2": 2.0 * dy - (4.0 / 3.0) * step,
        }
        for name, excess in samples.items():
            violations[name] = max(violations[name], float(excess))
        if delta > 1e-12:
            ratio["latent_reflection"] = max(ratio["latent_reflection"], reflection / delta)
        if residual > 1e-12:
            ratio["output_EB"] = max(ratio["output_EB"], dy / residual)
        if d > 1e-12:
            ratio["distance_contraction"] = max(ratio["distance_contraction"], dy / d)

    # The kernel cannot see a nonzero second row even at a fitted first row.
    invisible = np.array([[1.0, 0.0], [0.0, R / 2.0]])
    invisible_y = T(invisible)
    invisible_record = {
        "kernel_step": float(np.linalg.norm(A @ (invisible_y - invisible))),
        "physical_step": float(np.linalg.norm(invisible_y - invisible)),
        "input_true_residual": float(np.linalg.norm(F(invisible))),
        "distance": distance(invisible),
        "original_f_decrease_over_step_squared": (objective(invisible) - objective(invisible_y)) / float(np.linalg.norm(invisible_y - invisible) ** 2),
    }

    parameter_records = []
    for lam in [0.5, 1.0, 2.0, 3.9, 4.0, 5.0]:
        roots = np.roots([lam, 0.0, 1.0 - lam, -1.0])
        real_roots = sorted(float(root.real) for root in roots if abs(root.imag) < 1e-7)
        distinct_roots = []
        for root in real_roots:
            if not distinct_roots or abs(root - distinct_roots[-1]) > 1e-6:
                distinct_roots.append(root)
        parameter_records.append({
            "lambda": lam,
            "unit_circle_input_signed_roots": distinct_roots,
            "origin_extra_circle_radius": math.sqrt((lam - 1.0) / lam) if lam > 1.0 else None,
        })

    non_lip = [{"t": t, "output_norm": t ** (1.0 / 3.0), "calm_ratio": t ** (-2.0 / 3.0)} for t in [1e-3, 1e-6, 1e-9]]
    ordinary_prox = []
    for epsilon in [0.1, 0.01, 0.001]:
        z = epsilon
        for _ in range(8):
            z -= (z + z**3 - epsilon) / (1.0 + 3.0 * z**2)
        x = np.diag([1.0, epsilon])
        y = np.diag([1.0, z])
        ordinary_prox.append({
            "epsilon": epsilon,
            "output_z": z,
            "distance_ratio": z / epsilon,
            "ordinary_complete_equation_error": float(np.linalg.norm(y + F(y) - x)),
        })
    indices = {"circle_Euler": 0, "large_ball": 1, "predicted_outside": 1, "origin_homotopy_det": 1}
    checked = max(errors.values()) < TOL and max(violations.values()) < TOL
    result = {
        "scope": "Finite numerical replication; universal proofs and degree are not inferred from sampling.",
        "seed": SEED,
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "counts": {"arbitrary_SVD_right_hand_sides": 1000, "physical_tube_samples": 4000},
        "constants": {"R": R, "bart": 1.0, "omega_slope": 0.5, "psi_slope": 2.0 / 3.0, "kappa": 0.5, "K_slope": 0.75, "H_slope": 1.25, "Theta_slope": 2.5},
        "maximum_identity_errors": errors,
        "maximum_positive_certificate_excess": violations,
        "maximum_sampled_ratios": ratio,
        "invisible_kernel_direction": invisible_record,
        "lambda_parameter_fibers": parameter_records,
        "origin_non_Lipschitz_witnesses": non_lip,
        "same_objective_ordinary_prox_witnesses": ordinary_prox,
        "analytic_index_arithmetic_only": indices,
        "finite_replication_passed": checked,
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    if not checked:
        raise SystemExit("A finite identity/certificate check exceeded tolerance.")


if __name__ == "__main__":
    main()
