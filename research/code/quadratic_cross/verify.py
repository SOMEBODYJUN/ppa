"""Check finite algebra for C290–C292 using exact rational arithmetic."""

from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import platform


def uniform_budget(squared_excess, support):
    total = sum(squared_excess[i, j] for i, j in combinations(support, 2))
    return total / len(support) ** 2


def certify_graph(size, edges):
    scale = F(1, size)
    pairs = list(combinations(range(size), 2))
    nonedges = set(pairs) - edges
    raw_images = [{pair for pair in nonedges if i in pair} for i in range(size)]
    for i, entries in enumerate(raw_images):
        entries.update((i, private, 'private') for private in range(size - len(entries)))
        assert len(entries) == size

    squared_excess = {}
    input_squared = 8 * (size - 1) * scale**2
    for i, j in pairs:
        image_squared = len(raw_images[i] ^ raw_images[j]) * scale**2
        assert image_squared**2 <= input_squared
        squared_excess[i, j] = image_squared - input_squared / 4
        assert squared_excess[i, j] == (2 * scale**2 if (i, j) in edges else 0)

    supports = [support for k in range(1, size + 1) for support in combinations(range(size), k)]
    clique = max(len(support) for support in supports if all(pair in edges for pair in combinations(support, 2)))
    exact_budget = scale**2 * (1 - F(1, clique))
    assert max(uniform_budget(squared_excess, support) for support in supports) == exact_budget
    for k in range(2, size + 1):
        threshold = scale**2 * (1 - F(1, k - 1))
        assert (exact_budget > threshold) == (clique >= k)


def check_weights():
    checked = 0
    for count in range(1, 6):
        for sizes in product(range(4), repeat=count):
            total = sum(sizes)
            if total == 0:
                continue
            weights = [F(size, total) for size in sizes]
            errors = [F(i, count) for i in range(count)]
            for split in range(count + 1):
                mass = sum(weights[:split])
                budget = sum(w * e for w, e in zip(weights[:split], errors))
                mixed = sum(weights[i] * weights[j] * errors[i] for i in range(split) for j in range(split, count))
                assert mixed == (1 - mass) * budget
                assert mass * budget + mixed == budget
                cap = F(count - 1, 2 * count)
                assert (1 - sum(w**2 for w in weights)) / 2 <= cap
                checked += 1
        uniform = [F(1, count)] * count
        assert (1 - sum(w**2 for w in uniform)) / 2 == F(count - 1, 2 * count)
    return checked


def check_empirical_weights():
    # A signed excess table confirms that no pairwise nonnegativity is needed.
    excess = ((0, 3, -5), (3, 0, 2), (-5, 2, 0))
    weights = (F(1, 5), F(2, 5), F(2, 5))
    expected = sum(weights[i] * weights[j] * excess[i][j] for i, j in combinations(range(3), 2))
    for count in range(1, 6):
        actual = F(0)
        for sample in product(range(3), repeat=count):
            chance = F(1)
            for i in sample:
                chance *= weights[i]
            estimate = F(sum(excess[i][j] for i, j in combinations(sample, 2)), count**2)
            actual += chance * estimate
        assert actual == (1 - F(1, count)) * expected
    return 5


def main():
    graphs_checked = 0
    for size in range(2, 6):
        pairs = list(combinations(range(size), 2))
        for choices in product((False, True), repeat=len(pairs)):
            certify_graph(size, {pair for pair, enabled in zip(pairs, choices) if enabled})
            graphs_checked += 1
    result = {
        'claim_versions': ['C290-v1', 'C291-v1', 'C292-v1'],
        'arithmetic': 'integer and Fraction exact, no randomness',
        'python': platform.python_version(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'all_labeled_graphs_sizes_2_to_5': graphs_checked,
        'mixed_weight_splits': check_weights(),
        'empirical_support_sizes_checked': check_empirical_weights(),
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
