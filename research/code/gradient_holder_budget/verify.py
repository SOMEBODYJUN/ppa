"""Check explicit boundary data for the gradient Hölder budget."""

import hashlib
import json
import math
import platform
from pathlib import Path


def fit_kappa(gamma):
    left, right = 1e-9, 20.0
    for _ in range(85):
        middle = (left + right) / 2
        if 2 * middle / math.sinh(2 * middle) > gamma:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def check_endpoint():
    worst = 0.0
    pairs = 0
    for gamma in (0.05, 0.1, 0.5, 0.9, 0.99):
        kappa = fit_kappa(gamma)
        assert abs(2 * kappa / math.sinh(2 * kappa) - gamma) < 1e-12

        def coordinate_map(t):
            return math.tanh(kappa * t) / math.tanh(kappa)

        assert [coordinate_map(t) for t in (-1, 0, 1)] == [-1, 0, 1]
        assert coordinate_map(0.5) > 0.5 and coordinate_map(2) < 2
        for i in range(-60, 61):
            for j in range(i + 1, 61):
                u, v = i / 10, j / 10
                ratio = (coordinate_map(v) - coordinate_map(u)) / ((v - u) ** gamma * 2 ** (1 - gamma))
                assert ratio <= 1 + 1e-12
                pairs += 1
                worst = max(worst, ratio)
    return pairs, worst


if __name__ == '__main__':
    count, worst = check_endpoint()
    print(json.dumps({
        'claim_version': 'C296-v1',
        'python': platform.python_version(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'inputs': 'five exponents, center and separated real coordinate pairs, no randomness',
        'arithmetic': 'binary64 with 1e-12 decision slack; analytic text supplies exact bounds',
        'pairs': count,
        'largest_ratio_to_diameter_budget': worst,
    }, indent=2))
