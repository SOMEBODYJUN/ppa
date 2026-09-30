"""Deterministic checks for ATTACK_RANDOM_PROXIMAL_CORRELATION_AWARE.md.

The symbolic and finite-dimensional checks support, but do not replace, the
measure-theoretic proofs. No simulated convergence is reported as a theorem.
"""

from fractions import Fraction as F

import numpy as np


def matrix_certificate():
    normals = [
        np.array([1.0, 0.0]),
        np.array([0.0, 1.0]),
        np.array([1.0, 1.0]) / np.sqrt(2.0),
    ]
    offsets = [0.0, 0.0, 1.0]
    hessians = [np.outer(n, n) for n in normals]
    matrices = [np.linalg.inv(np.eye(2) + h) for h in hessians]
    shifts = [0.5 * d * n for d, n in zip(offsets, normals)]
    average = sum(matrices) / 3.0
    contraction = sum(a.T @ a for a in matrices) / 3.0
    defect = sum((np.eye(2) - a).T @ (np.eye(2) - a) for a in matrices) / 3.0
    assert np.allclose(np.linalg.eigvalsh(contraction), [0.5, 0.75])
    assert np.allclose(np.linalg.eigvalsh(defect), [1.0 / 12.0, 1.0 / 6.0])
    assert all(np.isclose(np.linalg.norm(a, 2), 1.0) for a in matrices)
    assert not np.allclose(matrices[0] @ matrices[2], matrices[2] @ matrices[0])
    mean = np.linalg.solve(np.eye(2) - average, sum(shifts) / 3.0)
    assert np.allclose(mean, normals[2] / 2.0)
    assert not np.allclose(matrices[0] @ mean + shifts[0], mean)
    rng = np.random.default_rng(7310909)
    max_ratio = 0.0
    for _ in range(1000):
        v = rng.normal(size=2)
        ratio = sum(np.linalg.norm(a @ v) ** 2 for a in matrices) / (3.0 * np.dot(v, v))
        assert ratio <= 0.75 + 1e-12
        max_ratio = max(max_ratio, ratio)
    print("Noncommuting inconsistent quadratic prox: eigenvalues and 1000 pair checks PASS")
    print("Native c^2 = 3/4, eta = 1/12; invariant mean =", mean)
    print("Max sampled synchronous squared ratio =", max_ratio)


def scalar_exact_checks():
    for a in [F(1, 5), F(1, 3), F(1, 2), F(4, 5)]:
        variance = (1 - a) / (1 + a)
        assert a * a * variance + (1 - a) ** 2 == variance
        for shift in [F(1, 10), F(-2, 7), F(1)]:
            error2 = shift**2
            residual2 = (1 - a) ** 2 * shift**2
            next_error2 = a * a * shift**2
            assert error2 == residual2 / (1 - a) ** 2
            assert next_error2 == a * a * error2
        physical_stationary_step2 = (1 - a) ** 2 * (variance + 1)
        assert physical_stationary_step2 == 2 * (1 - a) ** 2 / (1 + a)
        assert physical_stationary_step2 > 0
    a = F(1, 2)
    diagonal_error2 = F(2, 3)
    diagonal_residual2 = F(1, 3)
    # Conditional output is two equally weighted atoms u/2 +/- 1/2.
    # Coupling each atom to its half of Uniform[-1,1] gives variance 1/12.
    diagonal_next_error2 = F(1, 12) + a * a * F(1, 3)
    assert diagonal_next_error2 == F(1, 6)
    assert diagonal_next_error2 == a * a * diagonal_error2
    assert diagonal_residual2 == (1 - a) ** 2 * (F(1, 3) + 1)
    print("Scalar AR-prox variance, translation sharpness, stationary-step obstruction PASS")
    print("a=1/2 diagonal conditional (E^2,R^2,E_+^2) = (2/3,1/3,1/6)")


if __name__ == "__main__":
    matrix_certificate()
    scalar_exact_checks()
    print("ALL RANDOM PROXIMAL CORRELATION-AWARE CHECKS PASSED")
