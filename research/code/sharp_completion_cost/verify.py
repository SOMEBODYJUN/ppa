"""Finite checks for SC3--SC11; no implementation of a Hopf extension.

Run from repository root. Seed, arithmetic, tolerances and actual diagnostics
are saved beside this script. Analytic proofs carry the universal claims.
"""
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
SEED = 20261011
TOL = 3e-11


def index_model(x, k):
    x = np.asarray(x, dtype=float)
    out = x.copy()
    radius = math.hypot(x[0], x[1])
    if radius == 0:
        out[:2] = 0
    else:
        angle = k * math.atan2(x[1], x[0])
        out[:2] = radius * np.array([math.cos(angle), math.sin(angle)])
    return out


def project_ball(x, center, rho):
    v = x - center
    r = np.linalg.norm(v)
    return center + v * min(1.0, rho / r) if r else center.copy()


def run():
    rng = np.random.default_rng(SEED)
    report = {
        "python": platform.python_version(), "numpy": np.__version__,
        "seed": SEED, "arithmetic": "Fraction exact; NumPy binary64",
        "absolute_tolerance": TOL,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Finite arithmetic and local models, not Hopf or infinite-domain proof",
    }
    count_cases = 0
    for s in (1, 2, 3):
        for deficits in itertools.product(range(-3, 4), repeat=s):
            isolated = sum(k != 0 for k in deficits)
            nondeg = sum(abs(k) for k in deficits)
            # Construct each allocation independently and back-check each component.
            general_alloc = [[k] if k else [] for k in deficits]
            simple_alloc = [[1 if k > 0 else -1] * abs(k) for k in deficits]
            assert [sum(a) for a in general_alloc] == list(deficits)
            assert [sum(a) for a in simple_alloc] == list(deficits)
            assert sum(map(len, general_alloc)) == isolated
            assert sum(map(len, simple_alloc)) == nondeg
            # Independent finite search for the minimum number of signed unit indices.
            for k in deficits:
                minimum = next(n for n in range(abs(k) + 1)
                               if any(sum(v) == k for v in
                                      itertools.product((-1, 1), repeat=n)))
                assert minimum == abs(k)
            count_cases += 1
    cells = {"circle": [1, 1], "RP2": [1, 1, 1],
             "sphere2": [1, 0, 1], "genus2_surface": [1, 4, 1]}
    report["euler_table"] = {}
    for name, ranks in cells.items():
        chi = sum((-1) ** j * v for j, v in enumerate(ranks))
        deficit = 1 - chi
        assert chi + deficit == 1
        report["euler_table"][name] = {
            "chi": chi, "deficit": deficit,
            "isolated_min_connected_exterior": int(deficit != 0),
            "nondegenerate_min_connected_exterior": abs(deficit),
        }
    report["allocation_cases"] = count_cases

    winding_errors = []
    norm_error = 0.0
    model_cases = 0
    for k in range(-8, 9):
        if not k:
            continue
        angles = np.linspace(0, 2 * np.pi, 2049)
        output = np.array([index_model([np.cos(t), np.sin(t)], k)
                           for t in angles])
        phases = np.unwrap(np.arctan2(output[:, 1], output[:, 0]))
        winding = (phases[-1] - phases[0]) / (2 * np.pi)
        winding_errors.append(abs(winding - k))
        assert abs(winding - k) < TOL
        # Back-count all preimages of a nonzero target and each orientation sign.
        roots = [np.exp(2j * np.pi * j / abs(k)) for j in range(abs(k))]
        for root in roots:
            mapped = index_model([root.real, root.imag], k)
            assert np.linalg.norm(mapped - [1, 0]) < TOL
        assert len(roots) * (1 if k > 0 else -1) == k
        for n in (2, 3, 5):
            values = [np.zeros(n), np.r_[0., 0., np.ones(n - 2)],
                      np.r_[-1., 0., np.zeros(n - 2)]]
            values += list(rng.normal(size=(120, n)))
            for value in values:
                image = index_model(value, k)
                error = abs(np.linalg.norm(value) - np.linalg.norm(image))
                norm_error = max(norm_error, error)
                assert error < TOL
                assert (np.linalg.norm(image) == 0) == (np.linalg.norm(value) == 0)
                model_cases += 1
    report["index_model"] = {"cases": model_cases,
                             "max_norm_error": norm_error,
                             "max_winding_error": max(winding_errors)}

    radial_cases = 0
    for theta in map(Fraction, ("0", "1/4", "1/2", "3/4", "99/100")):
        q = max(theta, Fraction(1, 2))
        for rho in map(Fraction, ("1/8", "1", "2")):
            for ratio in map(Fraction, ("0", "1/2", "1", "1001/1000", "2", "1000")):
                r = ratio * rho
                upper = theta * r if r <= rho else theta * rho + (r - rho) / 2
                assert upper <= q * r
                assert r == 0 or upper < r
                if r > rho:
                    assert r - upper == (r + rho) / 2 - theta * rho
                radial_cases += 1
    report["fraction_radial_cases"] = radial_cases

    max_holder_excess = 0.0
    max_budget_error = 0.0
    graph_error = 0.0
    orbit_steps = 0
    data_cases = 0
    center = np.array([0.75, -0.375])
    for theta, angle, rho, gamma in itertools.product(
            (0.0, 0.5, 0.99), (0.0, np.pi / 2, np.pi),
            (0.125, 1.0), (0.25, 0.75)):
        rot = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        matrix = 2 * theta * rot - np.eye(2)
        matrix_norm = np.linalg.norm(matrix, ord=2)
        exact_budget = matrix_norm * (2 * rho) ** (1 - gamma)

        def cayley(x):
            return center + matrix @ (project_ball(x, center, rho) - center)

        def step(x):
            return (x + cayley(x)) / 2

        # Antipodal boundary values attain the exact local budget for these rotations.
        left, right = center + [rho, 0], center - [rho, 0]
        observed = np.linalg.norm(cayley(left) - cayley(right)) / (2 * rho) ** gamma
        max_budget_error = max(max_budget_error, abs(observed - exact_budget))
        assert abs(observed - exact_budget) < TOL
        inputs = [center, left, right, center + [1e-9, 0],
                  center + [1.001 * rho, 0], center + [1000 * rho, 0]]
        inputs += list(center + rng.normal(size=(120, 2)) * (3 * rho))
        for x in inputs:
            for y in inputs:
                gap = np.linalg.norm(cayley(x) - cayley(y))
                bound = exact_budget * np.linalg.norm(x - y) ** gamma
                max_holder_excess = max(max_holder_excess, gap - bound)
                assert gap <= bound + TOL
            u = step(x)
            for lam in (0.125, 1., 4.):
                v = (x - u) / lam
                error = max(np.linalg.norm(u + lam * v - x),
                            np.linalg.norm(u - lam * v - cayley(x)))
                graph_error = max(graph_error, error)
                assert error < TOL
        q = max(theta, 0.5)
        for initial in inputs[:6]:
            x = np.array(initial)
            initial_radius = np.linalg.norm(x - center)
            step_budget = (max(0, math.ceil(math.log(1e-13 / initial_radius)
                                          / math.log(q))) + 2
                           if initial_radius else 0)
            for _ in range(step_budget):
                r = np.linalg.norm(x - center)
                if r < 1e-12:
                    break
                x_next = step(x)
                assert np.linalg.norm(x_next - center) <= q * r + TOL
                x = x_next
                orbit_steps += 1
            assert np.linalg.norm(x - center) < 1e-11
        data_cases += 1
    report["singleton_samples"] = {
        "data_cases": data_cases, "orbit_steps": orbit_steps,
        "max_holder_excess": max_holder_excess,
        "max_exact_budget_error": max_budget_error,
        "max_graph_roundtrip_error": graph_error,
        "includes_zero_budget": True,
    }
    report["status"] = "PASS"
    (ROOT / "results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run()
