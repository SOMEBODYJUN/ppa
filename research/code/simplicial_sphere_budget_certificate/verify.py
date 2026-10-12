"""Finite checks for the C258 normalized-barycentric sphere certificate."""
from math import sqrt
from pathlib import Path
import json
import numpy as np


def certificate(vertices, simplices, values, witnesses, etas, G=1.0):
    if not np.isfinite(G) or G < 1:
        raise ValueError("the quasiconvex factor must be finite and at least one")
    vertices = np.asarray(vertices, dtype=float)
    values = np.asarray(values, dtype=float)
    if not np.all(np.isfinite(vertices)) or not np.all(np.isfinite(values)):
        raise ValueError("non-finite geometric data")
    vals, qvals = [], []
    for simplex, u, eta in zip(simplices, witnesses, etas):
        idx = list(simplex)
        X = vertices[idx]
        M = np.vstack([X.T, np.ones(len(idx))])
        invM = np.linalg.inv(M)
        grads = invM[:, :-1]
        Q = float(np.sum(np.linalg.norm(grads, axis=1)))
        y = values[idx]
        u = np.asarray(u, dtype=float)
        unorm = np.linalg.norm(u)
        if not np.isfinite(unorm) or unorm <= 0:
            raise ValueError("witness must be finite and nonzero")
        u = u / unorm
        if not (0 < eta <= 1) or not np.isfinite(eta):
            raise ValueError("eta must lie in (0,1]")
        dots = y @ u
        if float(np.min(dots)) + 1e-12 < eta:
            raise AssertionError(("hemisphere margin", float(np.min(dots)), eta))
        if not np.all(np.isfinite(dots)) or float(np.max(np.abs(np.linalg.norm(y, axis=1) - 1))) > 1e-12:
            raise AssertionError("vertex is not on sphere")
        vals.append(float(eta))
        qvals.append(Q)
    eta = min(vals)
    Q = max(qvals)
    return {"Q": Q, "eta": eta, "G": G, "Lip_bound": G * Q / eta}


def collar_bound(epsilon, Kg, Ktilde, delta):
    if not (0 <= epsilon < 2):
        raise ValueError("the normalized straight collar needs epsilon<2")
    if not np.isfinite(delta) or delta <= 0:
        raise ValueError("collar width must be positive")
    mu = sqrt(1 - epsilon * epsilon / 4)
    return {"mu_c": mu, "Lip_bound": (Kg + Ktilde + epsilon / delta) / mu}


# 2D: two triangles of a unit square, target S^1, common witness e_1.
v2 = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
a = np.pi / 6
b = np.pi / 4
y2 = np.array([[1, 0], [np.cos(a), np.sin(a)], [np.cos(b), np.sin(b)], [1, 0]])
r2 = certificate(v2, [(0, 1, 2), (0, 2, 3)], y2,
                 [[1, 0], [1, 0]], [np.cos(b), np.cos(b)], G=sqrt(2))
assert r2["eta"] > 0 and r2["Lip_bound"] > 0

# 5D: standard 5-simplex, target S^4; all vertices lie in the e_0 hemisphere.
v5 = np.vstack([np.zeros(5), np.eye(5)])
y5 = [np.array([1., 0, 0, 0, 0])]
for j in range(1, 6):
    q = np.zeros(5)
    q[0] = 1.
    q[j - 1] += 0.5
    y5.append(q / np.linalg.norm(q))
y5 = np.asarray(y5)
r5 = certificate(v5, [(0, 1, 2, 3, 4, 5)], y5,
                 [[1, 0, 0, 0, 0]], [1 / sqrt(1.25)], G=1.0)
assert r5["eta"] > 0 and r5["Lip_bound"] > 0

collar = collar_bound(0.25, Kg=3.0, Ktilde=4.0, delta=0.1)
assert collar["mu_c"] > 0 and collar["Lip_bound"] > 0
try:
    collar_bound(2.0, Kg=1.0, Ktilde=1.0, delta=1.0)
except ValueError:
    pass
else:
    raise AssertionError("antipodal collar was accepted")
for bad_delta in (0.0, -1.0):
    try:
        collar_bound(0.25, Kg=1.0, Ktilde=1.0, delta=bad_delta)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid collar width was accepted")

# Deliberately invalid margins and witnesses must be rejected.
try:
    certificate(v5, [(0, 1, 2, 3, 4, 5)], y5,
                [[1, 0, 0, 0, 0]], [0.95], G=1.0)
except AssertionError:
    pass
else:
    raise AssertionError("invalid hemisphere margin was accepted")
for bad_eta in (0.0, -0.1):
    try:
        certificate(v5, [(0, 1, 2, 3, 4, 5)], y5,
                    [[1, 0, 0, 0, 0]], [bad_eta], G=1.0)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid eta was accepted")
try:
    certificate(v5, [(0, 1, 2, 3, 4, 5)], y5,
                [[0, 0, 0, 0, 0]], [0.1], G=1.0)
except ValueError:
    pass
else:
    raise AssertionError("zero witness was accepted")

result = {
    "status": "PASS",
    "two_dimensional": r2,
    "five_dimensional": r5,
    "collar": collar,
    "invalid_margin_test": "rejected",
    "invalid_eta_and_witness_tests": "rejected",
    "invalid_collar_width_tests": "rejected",
    "limitations": "Toy certificates only; no RP2 triangulation, exact boundary collar, or L*=L0 claim.",
}
Path(__file__).with_name("results.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2, ensure_ascii=False))
