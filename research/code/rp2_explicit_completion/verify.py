"""Finite diagnostics for C264/C265; analytic proofs are in the canonical note."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import platform
import numpy as np

SEED = 20261012
TOL = 2e-10
RHO = 1 / 8
OUTER_TUBE = 1 / 4
AIN = 63 / 512
IDENTITY = np.eye(3)
M0 = np.diag([2 / 3, -1 / 3, -1 / 3])
AXIS = np.array([[0., 0., 0.], [0., 0., -1.], [0., 1., 0.]])
rng = np.random.default_rng(SEED)
checks = 0
errors = {}


def check(condition):
    global checks
    checks += 1
    assert condition


def near(name, left, right, tol=TOL):
    error = float(np.linalg.norm(np.asarray(left) - np.asarray(right)))
    errors[name] = max(errors.get(name, 0.), error)
    check(error <= tol)


def normalise(v):
    length = float(np.linalg.norm(v))
    if not math.isfinite(length) or length <= 1e-14:
        raise ValueError("Cannot normalise a zero or nonfinite vector")
    return v / length


def base(q):
    return np.outer(q, q) - IDENTITY / 3


def project(p):
    _, vectors = np.linalg.eigh(p)
    return base(vectors[:, -1])


def tubular_sample(radius):
    q = normalise(rng.normal(size=3))
    m = base(q)
    z = rng.normal(size=(3, 3))
    z = (z + z.T) / 2
    projector = np.outer(q, q)
    complement = IDENTITY - projector
    z = projector @ z @ projector + complement @ z @ complement
    z -= np.trace(z) * IDENTITY / 3
    n = normalise(z)
    return m + radius * n, m, n


def inner_raw(p):
    m = project(p)
    s = float(np.linalg.norm(p - m))
    n = (p - m) / s
    t = 8 * (s - RHO)
    w = AXIS @ m - m @ AXIS
    return (1 - t) * n + t * (p - M0) + t * (1 - t) * w


def cayley(p):
    norm = float(np.linalg.norm(p))
    if norm >= 2:
        return np.zeros((3, 3))
    m = project(p)
    s = float(np.linalg.norm(p - m))
    if s <= RHO:
        return m + (2 * s * s - 1) * (p - m)
    if s <= OUTER_TUBE:
        e = normalise(inner_raw(p))
    elif norm <= 1.5:
        e = normalise(p - M0)
    else:
        chi = 2 * (norm - 1.5)
        e = normalise(p - (1 - chi) * M0)
    tau = np.clip((norm - 1.25) / .75, 0., 1.)
    amplitude = AIN + (1 - AIN) * tau
    return p - 2 * amplitude * e


def exact_seminorm(radius, gamma):
    return (math.sqrt(2) + 2 * radius * (1 - 2 * radius**2)) / (
        math.sqrt(2) - 2 * radius
    )**gamma


def run():
    constants = {
        "inner_raw_lipschitz": 47,
        "inner_raw_margin": .25,
        "direction_lipschitz": 188,
        "cayley_lipschitz": float(Fraction(3025, 64)),
        "half_holder_upper": float(Fraction(3025, 32)),
        "original_half_holder_exact": exact_seminorm(RHO, .5),
        "collar_direction_lower": 8 * math.pi,
    }
    check(Fraction(1) + 2 * Fraction(63, 512) * 188 == Fraction(3025, 64))
    check(Fraction(449, 384) == (1 - Fraction(63, 512)) * Fraction(4, 3))
    check(1 + 2 * (Fraction(449, 384) + 4) < 12)
    near("budget_reverse", constants["half_holder_upper"] / 2,
         constants["cayley_lipschitz"])

    raw_min = math.inf
    samples = []
    for n in [normalise(np.diag([1., -1., 0.])),
              normalise(np.diag([0., 1., -1.]))]:
        p = M0 + OUTER_TUBE * n
        near("sharp_raw_margin", np.linalg.norm(inner_raw(p)), .25)
        raw_min = min(raw_min, float(np.linalg.norm(inner_raw(p))))
    for s in [0., 1e-7, RHO / 2, RHO, RHO + 1e-8, .2,
              OUTER_TUBE - 1e-8, OUTER_TUBE]:
        for _ in range(160):
            p, m, n = tubular_sample(s)
            near("projection", project(p), m)
            if s <= RHO:
                near("whole_tube_trace", cayley(p), m + (2 * s * s - 1) * s * n)
                output = (p + cayley(p)) / 2
                near("cubic_step", output, m + s**3 * n)
            if RHO <= s <= OUTER_TUBE:
                raw = inner_raw(p)
                raw_min = min(raw_min, float(np.linalg.norm(raw)))
                check(np.linalg.norm(raw) >= .25 - TOL)
            samples.append(p)

    # Exhaust the exceptional antipodal circle and collar endpoints.
    m_anchor = M0
    for angle in np.linspace(0., 2 * math.pi, 49):
        m = base(np.array([0., math.cos(angle), math.sin(angle)]))
        n = (m_anchor - m) / math.sqrt(2)
        p = m + RHO * n
        near("antipodal", normalise(p - M0), -n)
        near("straight_homotopy_zero", (n + normalise(p - M0)) / 2, 0.)
        for t in np.linspace(0., 1., 65):
            s = RHO + t / 8
            raw = inner_raw(m + s * n)
            check(np.linalg.norm(raw) >= .25 - TOL)
        near("inner_boundary_direction", normalise(inner_raw(p)), n)
        p_outer = m + OUTER_TUBE * n
        near("outer_tube_direction", normalise(inner_raw(p_outer)),
             normalise(p_outer - M0))

    # Matrix identity behind the raw margin, independently of the formula code.
    for _ in range(1000):
        s = rng.uniform(RHO, OUTER_TUBE)
        p, m, n = tubular_sample(s)
        t = 8 * (s - RHO)
        w = AXIS @ m - m @ AXIS
        c = m - M0
        near("rotation_normal_orthogonality", np.sum(w * n), 0.)
        near("rotation_chord_orthogonality", np.sum(w * c), 0.)
        near("rotation_chord_equal_norms", np.linalg.norm(w), np.linalg.norm(c))
        u = np.linalg.norm(c)**2 / 2
        b = 1 - t + s * t
        lower = b*b + u * (2*t*t*(1+(1-t)**2) - 2*math.sqrt(2)*b*t)
        check(np.linalg.norm(inner_raw(p))**2 >= lower - TOL)

    for radius in [0., 1.25, 1.5, 2., 2. + 1e-8, 10., 1e6]:
        for _ in range(40):
            z = rng.normal(size=(3, 3)); z = (z + z.T) / 2
            z -= np.trace(z) * IDENTITY / 3
            p = radius * normalise(z)
            c = cayley(p)
            check(np.isfinite(c).all())
            if radius >= 2:
                near("compact_support", c, np.zeros((3, 3)))
            elif np.linalg.norm(p - project(p)) > RHO + TOL:
                check(np.linalg.norm(p - c) >= 2 * AIN - TOL)
            samples.append(p)

    # Near seams: one-sided values tend to the same trace.
    for s in [RHO, OUTER_TUBE]:
        for _ in range(80):
            p, m, n = tubular_sample(s)
            near("tube_seam", cayley(p - 1e-9 * n), cayley(p + 1e-9 * n), 1e-6)
    for radius in [1.25, 1.5, 2.]:
        for _ in range(80):
            z = rng.normal(size=(3, 3)); z = (z + z.T) / 2
            z -= np.trace(z) * IDENTITY / 3; z = normalise(z)
            near("radial_seam", cayley((radius - 1e-9) * z),
                 cayley((radius + 1e-9) * z), 1e-6)

    ratios = []
    for _ in range(3000):
        p, q = samples[rng.integers(len(samples))], samples[rng.integers(len(samples))]
        gap = np.linalg.norm(p - q)
        if gap > 1e-10:
            lip = np.linalg.norm(cayley(p) - cayley(q)) / gap
            check(lip <= constants["cayley_lipschitz"] + TOL)
            check(lip * math.sqrt(gap) <= constants["half_holder_upper"] + TOL)
            ratios.append(lip)

    original_max = 0.
    for r in [0., 1e-8, RHO / 2, RHO]:
        for s in [0., 1e-8, RHO / 2, RHO]:
            n = normalise(np.diag([1., -1., 0.]))
            for sign in [-1., 1.]:
                u, v = r * n, sign * s * n
                beta = (1 - 2*r*r)*u - (1 - 2*s*s)*v
                rhs = ((1 - 2*r*r)*(1 - 2*s*s)*np.linalg.norm(u-v)**2
                       - 2*(r*r-s*s)**2*(1-2*(r*r+s*s)))
                near("radial_square_identity", np.linalg.norm(beta)**2, rhs)
                check(np.linalg.norm(beta)**2 <=
                      (1-(r+s)**2/2)**2*np.linalg.norm(u-v)**2 + TOL)
    for radius in [1e-4, 1/32, RHO]:
        m1 = M0; m2 = np.diag([-1/3, 2/3, -1/3])
        n = (m2 - m1) / math.sqrt(2)
        p, q = m1 + radius*n, m2 - radius*n
        cp = m1 + (2*radius**2-1)*radius*n
        cq = m2 - (2*radius**2-1)*radius*n
        for gamma in [.01, .25, .5, .99, 1.]:
            near("exact_seminorm_extremiser", np.linalg.norm(cp-cq) /
                 np.linalg.norm(p-q)**gamma, exact_seminorm(radius, gamma))
        for _ in range(2000):
            p, m, _ = tubular_sample(rng.uniform(0., radius))
            q, mm, _ = tubular_sample(rng.uniform(0., radius))
            r, s = np.linalg.norm(p-m), np.linalg.norm(q-mm)
            cp = m + (2*r*r-1)*(p-m); cq = mm + (2*s*s-1)*(q-mm)
            for gamma in [.25, .5, 1.]:
                ratio = np.linalg.norm(cp-cq)/np.linalg.norm(p-q)**gamma
                check(ratio <= exact_seminorm(radius, gamma) + TOL)
                if radius == RHO and gamma == .5:
                    original_max = max(original_max, float(ratio))

    # Reject undefined normalisation, including nonfinite inputs.
    for invalid in [np.zeros((3, 3)), np.full((3, 3), np.nan)]:
        try:
            normalise(invalid)
        except ValueError:
            check(True)
        else:
            check(False)
    result = {
        "scope": "finite binary64 diagnostics, not a proof or an optimal completion budget",
        "seed": SEED, "tolerance": TOL, "checks": checks,
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "constants": constants, "max_errors": errors,
        "observed_inner_raw_min": raw_min,
        "observed_global_lipschitz_max": max(ratios),
        "observed_original_half_holder_random_max": original_max,
    }
    Path(__file__).with_name("results.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"checks": checks, "constants": constants, "raw_min": raw_min}, indent=2))


if __name__ == "__main__":
    run()
