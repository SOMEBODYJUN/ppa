"""Exact arithmetic checks of C218, not a proof or a novelty search."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import itertools
import json
import platform


def n2(v):
    return sum(x * x for x in v)


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


checks = 0
for t1, t2, x1, x2 in itertools.product(
    (F(-1, 4), F(0), F(1, 4), F(1, 2), F(3, 4), F(1)),
    (F(-1, 2), F(0), F(1, 3), F(1)),
    (F(-2), F(0), F(1, 5)),
    (F(-1), F(0), F(3, 2)),
):
    x = (x1, x2)
    tx = (t1 * x1, t2 * x2)
    ix = sub(x, tx)
    cx = sub(tuple(2 * u for u in tx), x)
    assert n2(tx) + n2(ix) == (n2(x) + n2(cx)) / 2
    L = max(abs(2 * t1 - 1), abs(2 * t2 - 1))
    epsilon = max(F(0), (L * L - 1) / 2)
    assert n2(tx) + n2(ix) <= (1 + epsilon) * n2(x)
    assert n2(cx) <= L * L * n2(x)
    checks += 1

sharp = []
for lam, eps, d in itertools.product(
    (F(1, 4), F(1), F(3)),
    (F(1, 100), F(1, 4), F(1), F(20)),
    (F(0), F(1, 10000), F(1), F(10)),
):
    y = d / (1 + lam * eps)
    s = d - y
    assert s + (s / lam) / eps == d
    sharp.append({"lambda": str(lam), "epsilon": str(eps), "distance": str(d)})

# gamma=1/2, nu=3, r=t^2: exact noncalm lower ratio 1/t.
boundary = []
for j in (1, 2, 4, 8, 16, 32):
    t = F(1, 2**j)
    r = t * t
    e2 = t * t + r**6
    assert e2 / (r * r) >= (1 / t)**2
    # A diagonal bi-Lipschitz H=(2 xi, y/3) gives exact divergent ratio.
    transformed_ratio2 = (4 * t * t + r**6 / 9) / (r * r / 9)
    assert transformed_ratio2 >= 36 / (t * t)
    boundary.append({"r": str(r), "noncalm_lower_ratio": str(1 / t)})

paper_boundary = [
    {"L": str(L), "epsilon": str(max(F(0), (L * L - 1) / 2)),
     "admitted_definition_2_3": max(F(0), (L * L - 1) / 2) < 1}
    for L in (F(0), F(1), F(3, 2), F(7, 4), F(2))
]
root = Path(__file__).resolve().parents[3]
source = root / "research/canonical/gppa_almost_averaged_bridge.md"
result = {
    "python": platform.python_version(),
    "seed": None,
    "arithmetic": "fractions.Fraction, exact; deterministic finite enumeration",
    "identity_cases": checks,
    "sharp_bridge_cases": len(sharp),
    "noncalm_boundary": boundary,
    "source_violation_domain": paper_boundary,
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "scope": "Finite algebra and representative boundaries; no universal proof or priority certification.",
    "all_checks_passed": True,
}
out = Path(__file__).with_name("almost_averaged_results.json")
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
