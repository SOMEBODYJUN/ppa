"""Exact arithmetic checks for the conditional C242 budget interface."""
from fractions import Fraction as F
import json
from pathlib import Path

rho = F(1, 8)
R = F(2)
gamma = F(1, 2)
gap = 1 - 2 * rho
k_pi = 4 / gap
k_d = (1 + rho * rho) * (1 + k_pi)
k_c0 = 1 + 2 * k_d
a_in = (1 - rho * rho) * rho
delta_a = R / 2 - a_in

assert gap == F(3, 4)
assert k_pi == F(16, 3)
assert k_d == F(1235, 192)
assert k_c0 == F(1331, 96)
assert a_in == F(63, 512)
assert delta_a == F(449, 512)

# With K_tau=1, K_e=0, evaluate the symbolic LB3 coefficient and reverse it.
inner = k_c0
outer = 1 + 2 * F(449, 512) + 2 * 0
bound_without_G = 2 * max(inner, outer)
assert bound_without_G == 2 * k_c0
assert bound_without_G / 2 == k_c0

result = {
    "rho": str(rho),
    "R": str(R),
    "gamma": str(gamma),
    "spectral_gap": str(gap),
    "K_Pi_bound": str(k_pi),
    "K_D0_bound": str(k_d),
    "K_C0_bound": str(k_c0),
    "a_in": str(a_in),
    "delta_a": str(delta_a),
    "LB3_symbolic": "2*G_W*max(1331/96, 1+2*K_e+(449/256)*K_tau)",
    "sanity_Ktau1_Ke0_without_G": str(bound_without_G),
    "status": "PASS",
}
Path(__file__).with_name("results.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2, ensure_ascii=False))

