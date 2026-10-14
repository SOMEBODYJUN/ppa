#!/usr/bin/env python3
"""Finite-instance checks for unified_ppa_raw_calculus.md.

Run: python3 research/code/unified_ppa/raw_verify.py
Dependencies: Python 3 and NumPy. No SDP solver is required.
Exact symbolic checks establish only the displayed algebraic identities and
rational matrix certificates; universal claims are proved in the note.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction as F

import numpy as np


def json_number(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)


def identity(n):
    return np.array([[F(int(i == j)) for j in range(n)] for i in range(n)], dtype=object)


def zero(n, m=None):
    return np.full((n, n if m is None else m), F(0), dtype=object)


def diagonal(values):
    result = zero(len(values))
    for i, value in enumerate(values):
        result[i, i] = F(value)
    return result


def inverse2(A):
    determinant = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    return np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]], dtype=object) / determinant


def det2(A):
    return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]


def exact_raw_diag():
    D = diagonal([-1, F(1, 100)])
    V = identity(2) + 3 * D
    kappa = F(100, 103)
    H = kappa**2 * (V.T @ V) - identity(2)
    assert H[0, 0] > 0 and H[1, 1] == 0
    assert det2(V) != 0
    # A true graph inequality, not a selected-value residual equality.
    inverse_energy = V.T @ V - identity(2) - 3 * (D.T @ D)
    assert np.array_equal(inverse_energy, diagonal([0, F(303, 5000)]))
    return {
        "lambda": 3,
        "raw_V": str(V),
        "sharp_physical_kappa": str(kappa),
        "raw_contraction_LMI": str(H),
        "inverse_energy_remainder_matrix": str(inverse_energy),
        "C249_min_direct_factor": 50,
        "C250_min_energy_factor_squared": "25000/10009",
    }


def exact_robust_raw_lmi():
    D = diagonal([-1, F(1, 100)])
    eps, lam, kap, multiplier = F(1, 200), 3, F(99, 100), 600
    A = np.hstack([identity(2), zero(2)])
    B = np.hstack([zero(2), identity(2)])
    E = A + lam * B
    Q_error = eps**2 * (A.T @ A) - (B - D @ A).T @ (B - D @ A)
    target = kap**2 * (E.T @ E) - A.T @ A
    certified = target - multiplier * Q_error
    blocks = [certified[np.ix_([i, i + 2], [i, i + 2])] for i in range(2)]
    for block in blocks:
        assert block[0, 0] > 0 and det2(block) > 0
    return {
        "uncertainty_epsilon": str(eps),
        "certified_kappa": str(kap),
        "nonnegative_multiplier": multiplier,
        "exact_blocks": [str(b) for b in blocks],
        "exact_block_determinants": [str(det2(b)) for b in blocks],
        "elementary_raw_bound": "200/203",
        "true_residual_EB": 200,
    }


def noncommuting_cayley_identity():
    M = np.array([[F(1, 5), F(1, 20)], [F(1, 20), -F(1, 10)]], dtype=object)
    R = np.array([[F(1, 10), -F(3, 100)], [-F(3, 100), F(1, 20)]], dtype=object)
    Q, D = identity(2) + M + R, M - R
    H = identity(2) - M - R + D @ inverse2(Q) @ D
    A = np.hstack([identity(2), zero(2)])
    B = np.hstack([zero(2), identity(2)])
    P, C = A + B, A - B
    lhs = C.T @ Q @ C + P.T @ D @ C + C.T @ D @ P - P.T @ (identity(2) - M - R) @ P
    rhs = -4 * ((A.T @ B + B.T @ A) / 2 - A.T @ M @ A - B.T @ R @ B)
    assert np.array_equal(lhs, rhs)
    assert not np.array_equal(M @ R, R @ M)
    q_eigs = np.linalg.eigvalsh(np.array(Q).astype(float))
    h_eigs = np.linalg.eigvalsh(np.array(H).astype(float))
    assert q_eigs[0] > 0 and h_eigs[0] > 0
    return {"noncommuting": True, "Q_eigenvalues": q_eigs.tolist(),
            "H_eigenvalues": h_eigs.tolist(), "identity_exact": True}


def exact_signed_sum():
    R1, R2 = diagonal([-1, 2]), diagonal([2, 3])
    W = R1 + R2
    Rpar = R2 - R2 @ inverse2(W) @ R2
    B1 = np.hstack([identity(2), zero(2)])
    B2 = np.hstack([zero(2), identity(2)])
    B = B1 + B2
    deviation = B1 - inverse2(W) @ R2 @ B
    remainder = B1.T @ R1 @ B1 + B2.T @ R2 @ B2 - B.T @ Rpar @ B - deviation.T @ W @ deviation
    assert np.array_equal(remainder, zero(4))
    return {"R1": str(R1), "R2": str(R2), "R_parallel": str(Rpar),
            "exact_completed_square": True}


def gu3_checks():
    gamma, lam = 0.5, 1.0
    worst_distance, worst_step_excess = 0.0, -math.inf
    for t in np.logspace(-12, 3, 45):
        for sign in [-1, 1]:
            x = np.array([0.0, sign * t])
            for drift in [False, True]:
                y = np.array([x[0] + (t**gamma if drift else 0), x[1] / 2])
                graph_values = [np.array([0.0, y[1]]),
                                np.array([-2**gamma * abs(y[1])**gamma, y[1]])]
                w = (x - y) / lam
                assert any(np.linalg.norm(w - v) < 1e-10 * max(1.0, np.linalg.norm(v)) for v in graph_values)
                true_r = min(np.linalg.norm(v) for v in graph_values)
                assert abs(true_r - abs(y[1])) < 1e-12 * max(1, true_r)
                assert abs(w[1] - y[1]) < 1e-12 * max(1, t)
                assert abs(w[0]) <= 2**gamma * abs(y[1])**gamma * (1 + 1e-12)
                worst_distance = max(worst_distance, abs(y[1]) / t)
                worst_step_excess = max(worst_step_excess, np.linalg.norm(x - y) - (t / 2 + t**gamma))
    return {"gamma": gamma, "all_two_fibers_checked": True,
            "normal_contraction": worst_distance,
            "max_step_bound_excess": worst_step_excess,
            "C250_false_scalar_q_over_t_at_t_1e_minus12": 1e6,
            "length_bound_formula": "t+t^gamma/(1-2^(-gamma))"}


def critical_inverse_checks():
    # Polynomial coefficients in increasing degree, exact rational arithmetic.
    input_poly, output_poly = [F(0), F(1, 2), F(0), F(1)], [F(0), -F(1, 2), F(0), F(1)]
    def square(poly):
        result = [F(0)] * (2 * len(poly) - 1)
        for i, x in enumerate(poly):
            for j, y in enumerate(poly):
                result[i+j] += x*y
        return result
    exact_difference = [x-y for x, y in zip(square(input_poly), square(output_poly))]
    assert exact_difference == [F(0), F(0), F(0), F(0), F(2), F(0), F(0)]
    # Simulations support the asymptotic only; the note proves divergence.
    x, length = 0.01, 0.0
    checkpoints = {}
    for k in range(1, 100001):
        root = 2 * x
        for _ in range(5):
            root -= (root**3 + root / 2 - x) / (3 * root**2 + 0.5)
        y = x - root
        length += abs(root)
        x = y
        if k in {1000, 10000, 100000}:
            checkpoints[str(k)] = {"abs_x": abs(x), "k_times_x_squared": k * x*x,
                                   "length": length, "length_over_sqrt_k": length / math.sqrt(k)}
    # Test all cubic graph values when evaluating the true infimum.
    eb_margin = math.inf
    for y in np.linspace(-1/8, 1/8, 501):
        roots = np.roots([1.0, 0.0, -0.5, -y])
        values = [float(z.real) for z in roots if abs(z.imag) < 1e-10]
        true_r = min(abs(z) for z in values)
        eb_margin = min(eb_margin, true_r - 2*abs(y))
        assert true_r + 1e-10 >= 2*abs(y)
    return {"exact_energy": "x^2-y^2=2w^4", "true_local_EB_K": "1/2",
            "EB_state_window": "|y|<=1/8", "minimum_sampled_EB_margin": eb_margin,
            "simulation": checkpoints, "proved_asymptotic_constant": "1/32"}


def preservation_attacks():
    D = np.diag([-1.0, 0.01])
    # Replacing the physical kernel changes the algorithm, even for scalar SPD.
    preconditioned = np.linalg.solve(2*np.eye(2) + 3*D, 2*np.eye(2))
    singular_candidate = 3*np.eye(2) + 3*D
    assert abs(preconditioned[0, 0]) > 1 and np.linalg.det(singular_candidate) == 0
    # Full multivalued original F, each branch stable in a different fixed SPD.
    A1 = np.array([[0.5, 2.0], [0.0, 0.5]])
    A2 = A1.T
    P1, P2 = np.diag([1.0, 100.0]), np.diag([100.0, 1.0])
    own_norms = []
    for A, P in [(A1, P1), (A2, P2)]:
        sqrtP = np.diag(np.sqrt(np.diag(P)))
        own_norms.append(float(np.linalg.norm(sqrtP @ A @ np.linalg.inv(sqrtP), 2)))
    assert max(own_norms) < 1
    switched_rho = float(max(abs(np.linalg.eigvals(A2 @ A1))))
    assert switched_rho > 1
    F1, F2 = np.linalg.inv(A1) - np.eye(2), np.linalg.inv(A2) - np.eye(2)
    physical_residual_lower = min(np.linalg.svd(F1, compute_uv=False)[-1],
                                  np.linalg.svd(F2, compute_uv=False)[-1])
    assert physical_residual_lower > 0
    return {"changed_kernel_2I_negative_direction_factor": float(preconditioned[0, 0]),
            "changed_kernel_3I_coverage_matrix_is_singular": True,
            "branch_specific_SPD_norms": own_norms,
            "alternating_product_spectral_radius": switched_rho,
            "original_full_F_true_EB_K": float(1 / physical_residual_lower),
            "zero_fiber_drift_example": "F(u,v)={(u,0),(u,-1)}; J(0,b) contains (0,b+1)",
            "remote_full_fiber_example": "gphF=gphId union {(10,p-10):|p|<=1}; J(0) contains 10"}


def main():
    results = {"scope": "finite-instance algebra and attack checks; general proofs in canonical note",
               "linear_diag": exact_raw_diag(),
               "nonlinear_uncertainty_LMI": exact_robust_raw_lmi(),
               "noncommuting_matrix_identity": noncommuting_cayley_identity(),
               "signed_matrix_sum": exact_signed_sum(),
               "GU3": gu3_checks(),
               "critical_inverse": critical_inverse_checks(),
               "preservation_attacks": preservation_attacks()}
    print(json.dumps(results, ensure_ascii=False, indent=2, default=json_number))


if __name__ == "__main__":
    main()
