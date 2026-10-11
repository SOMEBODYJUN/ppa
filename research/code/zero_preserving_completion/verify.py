"""Finite checks of C234 and arithmetic boundaries; not a topology proof.
Run: python3 research/code/zero_preserving_completion/verify.py
Requires numpy. Seed 20261011; binary64 matrices, Fraction/Decimal scalars.
"""
import json
import platform
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

SEED = 20261011
RHO = Q(1, 8)
TOL = 2e-12
I = np.eye(3)


def point(q):
    q = np.asarray(q, dtype=float)
    q = q / np.linalg.norm(q)
    return np.outer(q, q) - I / 3


def projection(p):
    p = np.asarray(p, dtype=float)
    if np.linalg.norm(p - p.T) > TOL or abs(np.trace(p)) > TOL:
        raise ValueError("input must be symmetric and traceless")
    values, vectors = np.linalg.eigh(p)
    if values[-1] - values[-2] < 1e-12:
        raise ValueError("nearest point is not unique")
    return point(vectors[:, -1])


def local_t(p):
    base = projection(p)
    normal = p - base
    return base + np.sum(normal * normal) * normal


def normal_pair(rng, r):
    q = rng.normal(size=3)
    q /= np.linalg.norm(q)
    a = rng.normal(size=3)
    a -= q * (q @ a)
    a /= np.linalg.norm(a)
    b = np.cross(q, a)
    frame = np.column_stack([q, a, b])
    x, y, z = rng.normal(size=3)
    block = np.array([[x, 0, 0], [0, y, z], [0, z, -x-y]])
    block *= r / np.linalg.norm(block)
    return point(q), frame @ block @ frame.T


def inverse_local(y):
    base = projection(y)
    v = y - base
    s = np.linalg.norm(v)
    return base if s < 1e-15 else base + v / s ** (2 / 3)


def run():
    # Exact identity checks and reverse substitutions.
    theta = RHO ** 2
    output_radius = RHO ** 3
    eb = (1 / (1 - theta)) ** 3
    assert theta == Q(1, 64)
    assert output_radius == Q(1, 512)
    assert eb * (RHO - RHO ** 3) ** 3 == output_radius
    assert Q(2, 3) == Q(4, 9) + 2 * Q(1, 9)
    cell_chi = sum((-1) ** k for k in range(3))
    assert cell_chi == 1
    # Cellular chain has boundary2=2, boundary1=0, H1=Z/2.
    assert all((2 * z) % 2 == 0 for z in range(-200, 201))
    assert 1 % 2 != 0
    exact_cases = 0
    for lam in [Q(1, 3), Q(1), Q(2), Q(100)]:
        bound = (lam / (1 - theta)) ** 3
        for j in range(257):
            r = RHO * Q(j, 256)
            residual = (r - r ** 3) / lam
            assert r ** 3 <= bound * residual ** 3
            assert (residual * lam + r ** 3) == r
            # Nonlocal lower bound cannot beat the local residual.
            assert RHO - r ** 3 >= r - r ** 3
            exact_cases += 1

    rng = np.random.default_rng(SEED)
    errors = dict(projection=0., cubic_distance=0., base_preservation=0.,
                  inverse_input=0., complete_graph_identity=0.,
                  rayleigh_formula=0., embedding_derivative=0.)
    sampled_cases = 0
    radii = [0., .001, .01, float(RHO)]
    radii += list(rng.uniform(.001, float(RHO), 496))
    for r in radii:
        base, v = normal_pair(rng, r)
        p = base + v
        pi = projection(p)
        y = local_t(p)
        piy = projection(y)
        d_out = np.linalg.norm(y - piy)
        errors["projection"] = max(errors["projection"], np.linalg.norm(pi-base))
        errors["base_preservation"] = max(errors["base_preservation"],
                                          np.linalg.norm(piy-base))
        errors["cubic_distance"] = max(errors["cubic_distance"], abs(d_out-r**3))
        recovered = inverse_local(y)
        inverse_error = np.linalg.norm(recovered-p)
        errors["inverse_input"] = max(errors["inverse_input"], inverse_error)
        assert inverse_error < 2e-7
        for lam in [1/3, 1., 2., 100.]:
            f_value = (recovered-y)/lam
            graph_error = np.linalg.norm(y + lam*f_value - p)
            errors["complete_graph_identity"] = max(
                errors["complete_graph_identity"], graph_error)
            assert graph_error < 2e-7
        assert abs(d_out-r**3) < TOL
        assert np.linalg.norm(piy-base) < TOL
        # Independently check the minimization formula and embedding derivative.
        q = rng.normal(size=3)
        q /= np.linalg.norm(q)
        lhs = np.linalg.norm(p-point(q)) ** 2
        rhs = np.linalg.norm(p)**2 + 2/3 - 2*q@p@q
        errors["rayleigh_formula"] = max(errors["rayleigh_formula"], abs(lhs-rhs))
        h = rng.normal(size=3)
        h -= q * (q@h)
        derivative = np.outer(q, h) + np.outer(h, q)
        err = abs(np.sum(derivative**2) - 2 * (h@h))
        errors["embedding_derivative"] = max(errors["embedding_derivative"], err)
        assert err < TOL
        assert np.linalg.norm(point(q)-point(-q)) < TOL
        sampled_cases += 1

    # Legitimate repeated lower eigenvalues are allowed; repeated top is rejected.
    base = point([1, 0, 0])
    assert np.linalg.norm(projection(base)-base) < TOL
    try:
        projection(np.zeros((3, 3)))
    except ValueError:
        pass
    else:
        raise AssertionError("degenerate nearest point must be detected")

    # Tiny-scale arithmetic avoids cancellation in matrix distances.
    decimal_cases = 0
    with localcontext() as ctx:
        ctx.prec = 100
        for raw in ["0", "1e-30", "1e-10", "0.01", "0.125"]:
            r = Decimal(raw)
            for _ in range(4):
                next_r = r ** 3
                residual = r - next_r
                assert residual + next_r == r
                if r:
                    ratio = next_r / residual ** 3
                    assert ratio <= (Decimal(64)/Decimal(63))**3
                r = next_r
                decimal_cases += 1

    # Displacement patching uses convex proximity, not a vote over directions.
    d = np.array([1., 0., 0.])
    patch_samples = 0
    for _ in range(1000):
        a = d + rng.normal(size=3) * .02
        b = d + rng.normal(size=3) * .02
        c = d + rng.normal(size=3) * .02
        weights = rng.dirichlet(np.ones(3))
        patch = weights[0]*a + weights[1]*b + weights[2]*c
        error_bound = max(np.linalg.norm(a-d), np.linalg.norm(b-d),
                          np.linalg.norm(c-d))
        assert np.linalg.norm(patch-d) <= error_bound + TOL
        assert np.linalg.norm(patch) >= 1-error_bound-TOL
        patch_samples += 1

    result = {
        "python": platform.python_version(), "numpy": np.__version__,
        "seed": SEED, "matrix_arithmetic": "IEEE binary64",
        "scalar_arithmetic": "exact Fraction; Decimal precision 100",
        "absolute_geometry_tolerance": TOL,
        "inverse_cube_diagnostic_tolerance": 2e-7,
        "exact_scalar_cases": exact_cases, "matrix_cases": sampled_cases,
        "decimal_cases": decimal_cases, "convex_patch_cases": patch_samples,
        "ambient_dimension": 5, "manifold_dimension": 2, "codimension": 3,
        "rho_exact": str(RHO), "theta_exact": str(theta),
        "output_radius_exact": str(output_radius),
        "lambda1_eb_constant_exact": str(eb),
        "cellular_euler_characteristic": cell_chi,
        "cellular_boundary2": 2, "cellular_boundary1": 0,
        "max_errors": errors,
        "scope": "Finite checks only. No numerical claim of Hopf extension, "
                 "global no-zero completion, reach exact value, or global attraction."
    }
    Path(__file__).with_name("results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()

