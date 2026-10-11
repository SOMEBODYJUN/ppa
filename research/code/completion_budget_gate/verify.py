#!/usr/bin/env python3
"""Finite arithmetic checks for C238-C240; no global completion solver."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import platform
import random

SEED = 238240
rng = random.Random(SEED)


def sqdist(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


variance_ratios = []
radius_errors = []
for gamma in [0.001, 0.05, 0.2, 0.5, 0.8, 0.99, 0.999]:
    for _ in range(40):
        dim = rng.choice([1, 2, 5])
        pts = [[rng.uniform(-1, 1) for _ in range(dim)]
               for _ in range(rng.randint(1, 7))]
        x = [3.0] + [rng.uniform(-1, 1) for _ in range(dim - 1)]
        weights = [rng.uniform(0.01, 1) for _ in pts]
        weights = [w / sum(weights) for w in weights]
        ds = [sqdist(x, p) for p in pts]
        variance = sum(w * z ** gamma for w, z in zip(weights, ds))
        variance -= 0.5 * sum(weights[i] * weights[j]
                             * sqdist(p, q) ** gamma
                             for i, p in enumerate(pts)
                             for j, q in enumerate(pts))
        b = min(ds) ** gamma / (4 * math.gamma(1 - gamma)
                                * math.log(4) ** gamma)
        assert variance + 3e-12 >= b > 0
        variance_ratios.append(variance / b)
        rpow = max(ds) ** (gamma / 2)
        eta = b / (rpow + math.sqrt(rpow * rpow - b))  # L=1
        error = abs(eta * (2 * rpow - eta) - b)
        assert error < 3e-12
        assert eta > 0
        radius_errors.append(error)
        for dsq in ds:
            radius = dsq ** (gamma / 2)
            assert math.sqrt(dsq ** gamma - b) + eta <= radius + 3e-12

# Exact conjugation signs on a basis of Sym_0(3): two diagonal, three off-diagonal.
signs = [e for e in product([-1, 1], repeat=3) if math.prod(e) == 1]
chars = [[1, 1, e[0] * e[1], e[0] * e[2], e[1] * e[2]] for e in signs]
fixed_coordinates = [i for i in range(5) if all(c[i] == 1 for c in chars)]
assert fixed_coordinates == [0, 1]
mi = [[F(int(i == j)) - F(1, 3) for j in range(3)] for i in range(3)]
assert all(sum(z * z for z in m) == F(2, 3) for m in mi)
assert all(sqdist(mi[i], mi[j]) == 2 for i in range(3) for j in range(i))
rho = F(1, 8)
assert (2 * rho) ** 2 < 2
assert 1 - 3 == -2
orthogonal_signs = list(product([-1, 1], repeat=3))
joint_stabilizer = [e for e in orthogonal_signs
                    if all(e[i] * e[j] == 1 for i in range(3) for j in range(i))]
assert joint_stabilizer == [(-1, -1, -1), (1, 1, 1)]
boundary_radial_determinant = (1 - rho ** 2) * (1 - 3 * rho ** 2)
assert boundary_radial_determinant == F(3843, 4096) > 0

# A fully covered 1D illustration of the certificate estimate, not the RP2 test.
# N=[-1,1], T0(x)=x/2, C0=0, gamma=1/2, chosen budget L=1 (not minimal).
gamma, budget = 0.5, 1.0
s, h, delta = F(1, 25), F(1, 50), F(1, 100)
rad = F(2)
assert float(s) + budget * float(s) ** gamma < 1
assert float(rad) > budget ** (1 / (1 - gamma))
positive_net = [F(26, 25) + i * h for i in range(49)]
assert positive_net[-1] == rad
net = [-x for x in reversed(positive_net)] + positive_net
anchor_net = [F(-1) + i * delta for i in range(201)]
assert anchor_net[-1] == 1
# Endpoint equality and exact spacing certify both closed interval covers.
assert all(b - a == h for a, b in zip(positive_net, positive_net[1:]))
assert all(b - a == delta for a, b in zip(anchor_net, anchor_net[1:]))
min_displacement = min(abs(float(x)) for x in net)  # v_i=0
threshold = float(h) + budget * float(h) ** gamma
assert min_displacement > threshold
min_anchor_rhs = min(budget * abs(float(x - p)) ** gamma
                     - 2 * budget * float(delta) ** gamma
                     for x in net for p in anchor_net)
assert min_anchor_rhs >= -3e-12
assert all(0 <= budget * abs(float(x - y)) ** gamma for x in net for y in net)

result = {
    "python": platform.python_version(), "seed": SEED, "arithmetic": "binary64 and exact Fraction",
    "variance_cases": len(variance_ratios), "gamma_values": [0.001, 0.05, 0.2, 0.5, 0.8, 0.99, 0.999],
    "minimum_variance_to_bound_ratio": min(variance_ratios),
    "maximum_radius_identity_error": max(radius_errors),
    "D2_fixed_space_dimension": len(fixed_coordinates), "slice_index_deficit": -2,
    "RP2_point_norm_squared": "2/3", "RP2_pair_distance_squared": "2",
    "single_diagonal_bias_sign_stabilizer_size": len(orthogonal_signs),
    "two_bias_stabilizer": joint_stabilizer,
    "tube_boundary_planar_determinant": str(boundary_radial_determinant),
    "interval_certificate": {"dimension": 1, "budget": budget, "minimal_local_budget": 0,
                             "h": str(h), "delta": str(delta), "test_points": len(net),
                             "anchor_points": len(anchor_net), "minimum_displacement": min_displacement,
                             "displacement_threshold": threshold, "minimum_buffered_anchor_rhs": min_anchor_rhs},
    "limitations": "Finite arithmetic only; no RP2 completion/certificate, exact L0 optimization, global extension solver, or novelty claim."
}
Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
