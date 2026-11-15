"""Check finite weight and factorization identities used in C302."""

from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial, prod
from pathlib import Path
import platform


def compositions(n):
    if n == 0:
        yield ()
    for first in range(1, n + 1):
        for tail in compositions(n - first):
            yield (first,) + tail


def verify_weight_products():
    ratios = [F(3, 2) + F(k, 10) for k in range(1, 15)]
    normalized = [F(1)]
    for ratio in ratios:
        normalized.append(normalized[-1] * ratio)
    checks = 0
    for total in range(1, 14):
        for split in compositions(total):
            assert prod(normalized[part] for part in split) <= normalized[total]
            assert normalized[len(split)] * prod(normalized[part] for part in split) <= (
                normalized[1] ** len(split) * normalized[total]
            )
            checks += 1
    return checks


def verify_slow_d():
    thresholds = [2**power for power in range(1, 13)]

    def slow_d(t):
        return 1 + sum(min(t / threshold, F(1)) for threshold in thresholds)

    samples = [F(k, 8) for k in range(1, 1001)]
    old_d, old_ratio = F(0), F(0)
    for sample in samples:
        value = slow_d(sample)
        assert value >= old_d and sample / value >= old_ratio
        old_d, old_ratio = value, sample / value
    return len(samples)


def verify_moreau_slope():
    count = 0
    for lam in (F(1, 5), F(1), F(4)):
        for k in range(-10, 31):
            eigenvalue = F(k, 20) / lam
            mapped = eigenvalue / (1 + lam * eigenvalue)
            assert abs(mapped) <= 1 / lam
            count += 1
    return count


if __name__ == '__main__':
    print(json.dumps({
        'claim_version': 'C302-v1',
        'python': platform.python_version(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic': 'Fraction exact, no random inputs',
        'nonlinear_weight_product_checks': verify_weight_products(),
        'finite_slow_d_checks': verify_slow_d(),
        'moreau_eigenvalue_checks': verify_moreau_slope(),
    }, indent=2))
