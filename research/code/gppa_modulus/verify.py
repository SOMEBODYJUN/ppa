"""Finite checks for the GPPA general-modulus extension; never a proof by testing.

Standard library only. Exact rational algebra is distinguished from deterministic
floating-point examples. Running this file overwrites only its own results.json.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import platform
import random

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SEED = 20261009
rng = random.Random(SEED)
checks = {}


def norm(v):
    return math.sqrt(sum(t * t for t in v))


def sub(v, w):
    return tuple(a - b for a, b in zip(v, w))


def exact_energy():
    count = 0
    # Verify the exact parallelogram identity and source ASM energy inclusion,
    # including small lambda*epsilon where the direct test cannot contract.
    for a1 in [F(-3), F(0), F(1, 7), F(2)]:
        for a2 in [F(-1, 3), F(0), F(4)]:
            for b1 in [F(-2), F(0), F(5, 11)]:
                a, b = (a1, a2), (b1, F(1, 2))
                lhs = sum(x * x for x in a) + sum(x * x for x in b)
                plus, minus = tuple(x + y for x, y in zip(a, b)), sub(a, b)
                rhs = (sum(x * x for x in plus) + sum(x * x for x in minus)) / 2
                assert lhs == rhs
                count += 1
    rows = []
    for lam in [F(1, 100), F(1, 3), F(1), F(100)]:
        for eps in [F(1, 100), F(1), F(7)]:
            z = lam * eps
            energy_q2 = 1 / (1 + z * z)
            anchor_q = 1 / (1 + z)
            printed_q2 = 1 / (1 + 2 * z)
            assert 0 < energy_q2 < 1
            assert anchor_q * anchor_q <= printed_q2 < 1
            # Reverse substitution in V and W, not just numerical comparison.
            assert (1 + z * z) * energy_q2 == 1
            assert (1 + z) * anchor_q == 1
            rows.append({"lambda": str(lam), "epsilon": str(eps),
                         "energy_factor_squared": str(energy_q2),
                         "anchor_factor": str(anchor_q),
                         "direct_test_fails": z <= 1})
    return {"parallelogram_cases": count, "ASM_parameters": rows}


def power_boundaries():
    rows = []
    # Ratios are computed from the full (t+L*t**gamma)/(2*lambda),
    # including the linear term at the critical coefficient-one boundary.
    for gamma, q, C, L, lam in [
        (.5, 3., 1., 2., 1.), (.5, 2., .25, 2., 1.),
        (.5, 2., 1., 2., 1.), (.5, 1., 1., 2., 1.),
        (1., 1., 1., .5, 1.), (1., 1., 1., 1., 1.),
    ]:
        ts = [10. ** (-k) for k in [2, 4, 8, 12]]
        ratios = [C * ((t + L * t ** gamma) / (2 * lam)) ** q / t for t in ts]
        for t, ratio in zip(ts, ratios):
            backward = ratio * t
            forward = C * ((t + L * t ** gamma) / (2 * lam)) ** q
            assert math.isclose(backward, forward, rel_tol=1e-13)
        exponent = gamma * q
        if exponent > 1:
            assert ratios[-1] < ratios[0] and ratios[-1] < 1
        elif exponent < 1:
            assert ratios[-1] > ratios[0]
        elif gamma < 1:
            coefficient = C * (L / (2 * lam)) ** q
            if coefficient == 1:
                assert all(r > 1 for r in ratios)
            else:
                assert math.isclose(ratios[-1], coefficient, rel_tol=2e-6)
        else:
            exact = C * ((1 + L) / (2 * lam)) ** q
            assert all(math.isclose(r, exact, rel_tol=1e-13) for r in ratios)
        rows.append({"gamma": gamma, "q_EB": q, "C": C,
                     "gamma_times_q": exponent, "ratios": ratios})
    # Exact coefficient-one critical failure with perfect-square inputs.
    for u in [F(1, 10), F(1, 100), F(1, 10000)]:
        t = u * u
        ratio = ((t + 2 * u) / 2) ** 2 / t
        assert ratio == (1 + u / 2) ** 2 > 1
    return rows


def inverse_normal(z, b=.5):
    # Monotone g(y)=y+b*tanh(y); bracketing includes negative/zero values.
    if z == 0:
        return 0.
    lo, hi = min(z, 0.) - b, max(z, 0.) + b
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid + b * math.tanh(mid) < z:
            lo = mid
        else:
            hi = mid
    y = (lo + hi) / 2
    assert math.isclose(y + b * math.tanh(y), z, rel_tol=2e-14, abs_tol=2e-15)
    return y


def V(x, b=.5, c=.25):
    return x[0] + c * math.sin(x[1]), x[1] + b * math.tanh(x[1])


def Vinverse(z, b=.5, c=.25):
    y = inverse_normal(z[1], b)
    return z[0] - c * math.sin(y), y


def nonlinear_conjugation():
    pairs = 0
    samples = [(0., 0.), (100., 0.), (0., -100.), (-5., 3.)]
    samples += [(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(80)]
    for x in samples:
        back = Vinverse(V(x))
        assert norm(sub(back, x)) <= 1e-12 * (1 + norm(x))
    for x in samples:
        for y in samples:
            dv, dx = sub(V(x), V(y)), sub(x, y)
            dot = sum(a * b for a, b in zip(dv, dx))
            assert dot + 1e-12 >= (1 - .25 / 2) * norm(dx) ** 2
            assert norm(dx) <= 1.25 * norm(dv) + 1e-12
            pairs += 1
    rows = []
    for nu in [1.25, 2., 3., 4.]:
        for gamma in [.25, .5, .8]:
            for r in [0., -.125, .125, .8]:
                z = (-.75, r)
                znext = (z[0] + abs(r) ** gamma, abs(r) ** nu)
                x, xnext = Vinverse(z), Vinverse(znext)
                Y = znext[1]
                normal_root = Y ** (1 / nu) if Y else 0.
                f = (-Y ** (gamma / nu) if Y else 0.,
                     (1 if r >= 0 else -1) * normal_root - Y)
                error = norm(sub(sub(V(x), V(xnext)), f))
                assert error < 1e-12
                # Full graph minimum is the positive branch, even at a
                # negative input whose selected value is the negative branch.
                true_residual = math.hypot(-f[0], normal_root - Y)
                selected_residual = norm(f)
                assert true_residual <= selected_residual + 1e-12
                q = nu / gamma
                assert Y <= true_residual ** q + 1e-12
                assert abs(xnext[1]) <= Y + 1e-12
                rows.append({"nu": nu, "gamma": gamma, "input_normal": r,
                             "warped_equation_error": error,
                             "full_residual": true_residual,
                             "selected_residual": selected_residual})
    return {"strong_monotonicity_pair_cases": pairs, "steps": rows,
            "warning": "Finite samples corroborate; universal proofs are in normative text."}


def perturbation():
    theta, delta = F(1, 2), F(3, 17)
    D0 = F(5, 7)
    D, z = D0, F(0)
    rows = []
    for k in range(40):
        E = delta
        D = theta * D + E
        explicit = theta ** (k + 1) * D0 + delta * (1 - theta ** (k + 1)) / (1 - theta)
        assert D == explicit
        z = theta * z + (-1) ** k * delta
        backward = (2 * delta / 3) * ((-1) ** k + theta ** (k + 1))
        assert z == backward
        assert abs(z) <= D
        rows.append({"k": k + 1, "envelope": str(D), "alternating_output": str(z)})
    return {"theta": str(theta), "delta": str(delta),
            "tube_bound": str(delta / (1 - theta)), "exact_steps": rows}


def shell_boundary():
    rows = []
    for q in [F(1, 3), F(1, 2), F(3, 4), F(1), F(2)]:
        exponent = 2 - 1 / q
        rows.append({"q_EB": str(q), "shell_exponent": str(exponent),
                     "sufficient_geometric_series_summable": exponent > 0})
        assert (exponent > 0) == (q > F(1, 2))
    return rows


def log_and_spiral():
    # Rigorous tail bounds are in the text. This only tests integral envelopes
    # at a finite set of k and the physical chord identity with backward check.
    rows = []
    for a in [1.25, 1.5, 2.5]:
        A, b = 5., math.log(4.)
        N = 50000
        for k in [10, 100, 1000]:
            finite = sum((A + j * b) ** (-a) for j in range(k, N))
            lower = (A + k * b) ** (1 - a) / (b * (a - 1))
            upper = (A + k * b) ** (-a) + lower
            remainder_lo = (A + N * b) ** (1 - a) / (b * (a - 1))
            remainder_hi = remainder_lo + (A + N * b) ** (-a)
            assert finite + remainder_hi >= lower - 1e-12
            assert finite + remainder_lo <= upper + 1e-12
            rho = (lower + upper) / 2
            inc = (A + k * b) ** (-a)
            rho2 = rho - inc
            angle = 1 / rho2 - 1 / rho
            chord = math.sqrt((rho - rho2) ** 2 + 4 * rho * rho2 * math.sin(angle / 2) ** 2)
            point1 = (rho * math.cos(1 / rho), rho * math.sin(1 / rho))
            point2 = (rho2 * math.cos(1 / rho2), rho2 * math.sin(1 / rho2))
            assert math.isclose(chord, norm(sub(point1, point2)), rel_tol=1e-10, abs_tol=1e-12)
            rows.append({"a": a, "k": k, "tail_interval": [lower, upper],
                         "approx_spiral_chord": chord, "k_times_chord": k * chord})
    return rows


checks["exact_energy"] = exact_energy()
checks["power_boundaries"] = power_boundaries()
checks["nonlinear_conjugation"] = nonlinear_conjugation()
checks["inexact_convolution"] = perturbation()
checks["monotone_shell_boundary"] = shell_boundary()
checks["log_spiral_finite_corroboration"] = log_and_spiral()
result = {"status": "PASS", "seed": SEED, "python": platform.python_version(),
          "dependencies": "Python standard library only", "arithmetic":
          "Fraction for algebra/edge coefficients; IEEE-754 floats for conjugation and finite log intervals",
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "checks": checks, "scope": "Finite corroboration only; no universal, novelty or infinite-series proof."}
(HERE / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"status": result["status"], "check_groups": len(checks),
                  "output": str((HERE / "results.json").relative_to(ROOT))}))
