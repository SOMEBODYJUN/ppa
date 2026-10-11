#!/usr/bin/env python3
"""Finite arithmetic and inverse checks; analytic proofs remain in the report."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import numpy as np


def main():
    out = {"seed": 20261011, "scope": "finite checks, not a universal proof"}
    checks = 0
    # Same simple full relation: exact off-diagonal SPD zero fiber.
    mat = ((F(1), F(1, 2)), (F(1, 2), F(1)))
    determinant = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    assert determinant == F(3, 4) and mat[0][0] > 0
    for s, t, root in [(F(0), F(0), F(0)), (F(-4, 49), F(16, 49), F(2, 7))]:
        assert root * root == abs(s)
        assert s + mat[0][0] * s + mat[0][1] * t == 0
        assert -root + mat[1][0] * s + mat[1][1] * t == 0
        checks += 3
    out["off_diagonal_zero_fiber"] = ["(0,0)", "(-4/49,16/49)"]
    # Independent scalar-kernel attack, including noncoverage and unit boundary.
    scalar_rows = []
    for a in [F(1, 10), F(1), F(3, 2), F(2), F(3), F(4), F(6)]:
        if a == 3:
            assert (a - 3) * F(7) != a * F(1)
            scalar_rows.append({"a": str(a), "coverage_nonzero": False})
            checks += 1
            continue
        q = a / (a - 3)
        assert (a - 3) * q == a
        assert (abs(q) < 1) == (0 < a < F(3, 2))
        scalar_rows.append({"a": str(a), "q": str(q), "strictly_stable": abs(q) < 1})
        checks += 2
    assert F(1, 3) * (1 + 2) / 2 == F(1, 2)
    out["scalar_kernel_attack"] = scalar_rows
    # Generic non-diagonal coordinate conversion and full residual reverse check.
    rng = np.random.default_rng(out["seed"])
    worst = 0.0
    for diagonal in [np.array([1e-8, 2.0]), np.array([0.25, 4.0]), np.array([1.0, 1.0])]:
        rot = np.array([[math.cos(0.37), -math.sin(0.37)], [math.sin(0.37), math.cos(0.37)]])
        M = rot @ np.diag(diagonal) @ rot.T
        eig, basis = np.linalg.eigh(M)
        Q = basis @ np.diag(np.sqrt(eig)) @ basis.T
        Qi = np.linalg.inv(Q)
        B = np.array([[2.0, 0.3], [-0.1, 1.0]])
        lam = 0.7
        G = Qi @ B @ Qi
        TG = np.linalg.inv(np.eye(2) + lam * G)
        TX = np.linalg.solve(M + lam * B, M)
        for _ in range(40):
            x = rng.normal(size=2)
            y = TX @ x
            zplus = TG @ (Q @ x)
            err = np.linalg.norm(zplus - Q @ y)
            assert err <= 1e-7 * (1 + np.linalg.norm(zplus))
            assert np.linalg.norm(M @ (x - y) - lam * B @ y) <= 1e-12
            # The transformed complete single-value residual is Qi B y.
            f = B @ y
            r1 = np.linalg.norm(Qi @ f)
            r2 = math.sqrt(max(0, float(f @ np.linalg.solve(M, f))))
            assert math.isclose(r1, r2, rel_tol=2e-8, abs_tol=1e-8)
            assert np.linalg.norm(f) <= math.sqrt(float(eig[-1])) * r1 + 1e-9
            assert np.linalg.norm(y) <= np.linalg.norm(Q @ y) / math.sqrt(float(eig[0])) + 1e-9
            worst = max(worst, err)
            checks += 5
    out["coordinate_identity_max_error"] = worst
    # Positive diagonal kernel: complete inverse, exact orbit, geometric tail.
    diagonal_rows = []
    for a, b in [(1e-6, 3.0), (0.25, 0.5), (1.0, 1.0), (2.0, 7.0), (1e6, 2.0)]:
        q = a / (a + 1)
        R = 1.0
        for _ in range(300):
            L = math.sqrt((2 * q - 1) ** 2 * R + 4 * q / (b * math.sqrt(a)))
            gate = b * math.sqrt(a) * (math.sqrt(R) + L) ** 2 / 4
            if gate < 1:
                break
            R /= 2
        assert gate < 1 and R > 0
        for s0 in [-4.0, -1e-12, 0.0, 1e-12, 9.0]:
            t0 = -0.7
            s, t = s0, t0
            length = 0.0
            limit_t = t0 + math.sqrt(q * abs(s0)) / (b * (1 - math.sqrt(q)))
            for k in range(30):
                sn = q * s
                tn = t + math.sqrt(abs(sn)) / b
                assert math.isclose((a + 1) * sn, a * s, rel_tol=1e-12, abs_tol=1e-14)
                assert math.isclose(b * (tn - t), math.sqrt(abs(sn)), rel_tol=1e-7, abs_tol=1e-12)
                length += math.hypot(sn - s, tn - t)
                s, t = sn, tn
                expected_s = s0 * q ** (k + 1)
                expected_t = t0 + math.sqrt(q * abs(s0)) * (1 - q ** ((k + 1) / 2)) / (b * (1 - math.sqrt(q)))
                assert math.isclose(s, expected_s, rel_tol=1e-12, abs_tol=1e-14)
                assert math.isclose(t, expected_t, rel_tol=1e-7, abs_tol=1e-7)
                tail_bound = abs(s) + math.sqrt(q * abs(s)) / (b * (1 - math.sqrt(q)))
                assert math.hypot(s, t - limit_t) <= tail_bound + 1e-7
                assert length <= abs(s0) + math.sqrt(q * abs(s0)) / (b * (1 - math.sqrt(q))) + 1e-7
                checks += 6
        diagonal_rows.append({"a": a, "b": b, "q": q, "certified_R": R, "direct_gate": gate})
    out["positive_diagonal_witness"] = diagonal_rows
    # Degenerate complete fiber: exact legal recurrence, true EB and lost motion.
    for k in range(30):
        t, tn = F(1, 2 ** k), F(1, 2 ** (k + 1))
        s, sn = F((-1) ** k), F((-1) ** (k + 1))
        assert t - tn == tn
        assert abs(sn - s) == 2
        assert abs(t) == t  # true residual equals distance to full zero line
        checks += 3
    # Boundary of the new witness: b=0 destroys coverage for nonzero first input.
    for a in [F(0), F(1), F(2)]:
        # b=0 forces splus=0 in the second equation, hence a*sinput=0.
        assert (a * F(1) == 0) == (a == 0)
        checks += 1
    out["degenerate_boundary"] = "lost-fiber oscillation; b=0 nonzero normal-input coverage fails for a>0"
    out["assertions"] = checks
    out["status"] = "PASS"
    out["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
