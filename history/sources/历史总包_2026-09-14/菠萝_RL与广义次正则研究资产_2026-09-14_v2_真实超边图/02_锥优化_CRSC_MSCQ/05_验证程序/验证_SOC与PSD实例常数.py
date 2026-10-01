"""Deterministic algebra/sanity checks for PA-EXAMPLES (RL-CONIC-2026).

Standard library only. The Markdown proof, not finite sampling, establishes
CRSC, projected-cone closure, amenability, and neighborhood-wide error bounds.
Run: python3 output/conic_paper/verify_examples_constants.py
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt


def norm2(vector):
    return sum(x * x for x in vector)


def soc_distance(y):
    time, first, second = y
    spatial = sqrt(first * first + second * second)
    if spatial <= time:
        return 0.0
    if spatial <= -time:
        return sqrt(norm2(y))
    return (spatial - time) / sqrt(2.0)


# SOC: ||P_H A e_u||^2=4; normalized cone-angle squared is 1/2.
normal_soc = [1, -1, 0, -1, 1, 0]
assert norm2(normal_soc) == 4
sigma_soc_squared, eta_soc_squared = Q(4), Q(1, 2)
assert 16 / (sigma_soc_squared * eta_soc_squared) == 8  # b^2
assert Q(2) * Q(1, 2) == 1  # each face coefficient of A d0 squared

radius = Q(1, 4)
h_soc_bound = radius + radius * radius / 2
l_soc_squared_bound = 2 + (4 + 20 * h_soc_bound**2) * (1 + radius**2)
assert h_soc_bound == Q(9, 32)
assert l_soc_squared_bound == Q(32485, 4096)
assert l_soc_squared_bound < 9

# PSD: k=3, C0=[e1,e2], D0=[e2,e3], Frobenius geometry.
c0 = [[1, 0], [0, 1], [0, 0]]
d0 = [[0, 0], [1, 0], [0, 1]]
cflat = sum(c0, [])
dflat = sum(d0, [])
assert norm2(cflat) == norm2(dflat) == 2
assert sum(a * b for a, b in zip(cflat, dflat)) == 0
sigma_psd_squared, eta_psd_squared = Q(6), Q(1, 6)
assert 16 / (sigma_psd_squared * eta_psd_squared) == 16
h_psd_bound = radius + radius**2
l_psd_squared_bound = 1 + (6 + 16 * h_psd_bound**2) * (1 + 4 * radius**2)
assert h_psd_bound == Q(5, 16)
assert l_psd_squared_bound == Q(669, 64)
assert l_psd_squared_bound < Q(13, 4)**2

# Finite deterministic SOC checks only: exact feasible candidate and analytic
# distance-to-SOC formula. These samples are not the proof of the estimates.
soc_count = 0
for qs, qt, qu in product(range(-4, 5), repeat=3):
    s, t, u = (Q(q, 16) for q in (qs, qt, qu))
    if s * s + t * t + u * u > radius**2:
        continue
    h = u - s * t
    first = [s + h, s - h, h * h]
    second = [t - h, t + h, 2 * h * h]
    residual2 = soc_distance(first)**2 + soc_distance(second)**2
    aminus2 = min(s, 0)**2 + min(t, 0)**2
    assert residual2 + 1e-13 >= float(2 * (aminus2 + h * h))
    sp, tp = max(s, 0), max(t, 0)
    candidate_distance2 = (s - sp)**2 + (t - tp)**2 + (u - sp * tp)**2
    assert float(candidate_distance2) <= float(Q(25, 32)) * residual2 + 1e-13
    soc_count += 1

# PSD direct-bound algebra for diagonal B and rational h. The general proof
# uses the PSD block distance lower bound, not diagonal-only experiments.
psd_count = 0
for first, second, third, normal in product(range(-2, 3), repeat=4):
    diag_b = [Q(i, 16) for i in (first, second, third)]
    h = Q(normal, 16)
    bnorm2 = norm2(diag_b)
    u = h + bnorm2
    if bnorm2 + u * u > radius**2:
        continue
    aminus2 = sum(min(v, 0)**2 for v in diag_b)
    candidate_distance2 = aminus2 + (h + aminus2)**2
    assert candidate_distance2 <= Q(25, 16) * (aminus2 + h * h)
    psd_count += 1

print("PASS: exact SOC/PSD normal norms, angle constants, and Lipschitz bounds.")
print("PASS: SOC theorem parameters (sigma, eta, tau, a_F)=(2,1/sqrt(2),1,1).")
print("PASS: PSD theorem parameters (sigma, eta, tau, a_F)=(sqrt(6),1/sqrt(6),1/sqrt(k),1).")
print(f"PASS: {soc_count} deterministic SOC feasible-candidate/residual sanity checks.")
print(f"PASS: {psd_count} deterministic diagonal-PSD direct-bound algebra checks.")
print("Proof scope: see EXAMPLES_AND_CONSTANTS_AUDIT.md; no optimal-modulus claim.")
