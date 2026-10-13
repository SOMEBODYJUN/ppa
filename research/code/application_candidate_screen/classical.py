"""Finite arithmetic checks supporting classical_topology_screen.md.

These checks do not establish all-fiber uniqueness, topology, or prior art.
Run: python3 research/code/application_candidate_screen/classical.py
"""
import json
from pathlib import Path
import numpy as np


def cubic_matrix_inverse(x):
    left, sig, right = np.linalg.svd(x, full_matrices=False)
    return (left * np.cbrt(sig)) @ right


def orthogonal_penalty_gradient(x):
    return x @ (x.T @ x - np.eye(x.shape[1]))


def low_rank_map(x):
    out = np.zeros_like(x)
    r = np.linalg.norm(x[0])
    if r:
        out[0] = x[0] / r ** (2 / 3)
    return out


rng = np.random.default_rng(20261013)
max_equation_error = 0.0
max_reflection_ratio = 0.0
max_true_eb_ratio = 0.0
max_compatibility_ratio = 0.0
max_low_rank_h1_violation = 0.0
max_low_rank_h2_ratio = 0.0
for _ in range(1000):
    # The certified Stiefel tube has d <= 1/8.
    left, _ = np.linalg.qr(rng.normal(size=(4, 2)))
    right, _ = np.linalg.qr(rng.normal(size=(2, 2)))
    dev = rng.normal(size=2)
    dev *= rng.uniform(1e-5, 1 / 8) / np.linalg.norm(dev)
    x = (left * (1 + dev)) @ right.T
    y = cubic_matrix_inverse(x)
    p = left @ right.T
    d = np.linalg.norm(x - p)
    d_plus = np.linalg.norm(y - p)
    residual = np.linalg.norm(orthogonal_penalty_gradient(y))
    max_equation_error = max(max_equation_error, np.linalg.norm(x-y-orthogonal_penalty_gradient(y)))
    max_reflection_ratio = max(max_reflection_ratio, np.linalg.norm(2*y-x-p)/d)
    max_true_eb_ratio = max(max_true_eb_ratio, d_plus / residual)
    max_compatibility_ratio = max(max_compatibility_ratio, d_plus/d)
    # Low-rank natural distance-squared ABS energy on the same physical tube.
    direction = rng.normal(size=2)
    direction /= np.linalg.norm(direction)
    x = np.vstack((direction*rng.uniform(15/16,17/16), rng.normal(size=2)/64))
    y = low_rank_map(x)
    r = np.linalg.norm(x[0])
    tau = np.linalg.norm(y[0])
    energy_in = (r-1)**2 + np.dot(x[1],x[1])
    energy_out = (tau-1)**2
    step = np.linalg.norm(x-y)
    max_low_rank_h1_violation = max(max_low_rank_h1_violation, step**2-(energy_in-energy_out))
    max_low_rank_h2_ratio = max(max_low_rank_h2_ratio, 2*abs(tau-1)/step)

# One exact support-singularity example: F(0)=R, hence every input has output 0.
# Nonzero stationary points solve t^3 - 4t + 1/2 = 0 with x=t^2>0.
positive_t = sorted(float(t.real) for t in np.roots([1,0,-4,1/2]) if abs(t.imag)<1e-12 and t.real>0)
sparse_stationary = [t*t for t in positive_t]
# Global-minimum scalar prox has a discontinuous threshold.
p, alpha, lam = 0.5, 1.0, 1.0
threshold_y = (2*lam*alpha*(1-p)/(1+lam)) ** (1/(2-p))
threshold_a = (1+lam)*threshold_y + lam*alpha*p*threshold_y**(p-1)
threshold_input = threshold_a - 4*lam
threshold_difference = ((1+lam)/2)*threshold_y**2-threshold_a*threshold_y+lam*alpha*threshold_y**p

results = {
    "seed":20261013,"samples":1000,
    "stiefel_full_equation_max_error":max_equation_error,
    "stiefel_tube_reflection_ratio_max":max_reflection_ratio,
    "stiefel_tube_true_EB_ratio_max":max_true_eb_ratio,
    "stiefel_tube_distance_factor_max":max_compatibility_ratio,
    "low_rank_H1_alpha1_max_violation":max_low_rank_h1_violation,
    "low_rank_H2_ratio_max":max_low_rank_h2_ratio,
    "sparse_positive_stationary_points":sparse_stationary,
    "sparse_argmin_threshold_input":threshold_input,
    "sparse_argmin_threshold_nonzero_output":threshold_y,
    "sparse_argmin_threshold_objective_difference":threshold_difference,
    "limits":"Finite checks only. Universal certificates and fatal objections are proved in the application screening report."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(results,indent=2)+"\n")
print(json.dumps(results,indent=2))
