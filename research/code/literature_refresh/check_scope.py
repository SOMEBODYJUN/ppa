"""Exact finite checks for LR-GPPA-PHYSICAL / LR-HOLDER-REFERENCE.

Run from the repository root with --output to save an evidence record.
General proofs are in research/literature_refresh_2026_10_08.md. This script
does not verify universal statements or any external paper's whole proof.
"""
import argparse
import datetime as dt
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform


def check():
    cutoff = dt.date(2026, 10, 8)
    dated_sources = {
        "gppa_submission": "2026-08-03",
        "nfb_submission": "2026-08-24",
        "spingarn_journal_publication": "2026-08-27",
        "spingarn_v1_submission": "2025-04-01",
        "kkt_submission": "2026-10-06",
        "kirszbraun_submission": "2026-07-20",
        "monotone_fibres_submission": "2026-09-18",
    }
    days = {name: (cutoff - dt.date.fromisoformat(date)).days
            for name, date in dated_sources.items()}
    assert days["gppa_submission"] == 66
    assert days["nfb_submission"] == 45
    assert days["kkt_submission"] == 2
    assert days["kirszbraun_submission"] == 80
    assert days["spingarn_v1_submission"] == 555

    # GPPA v1 Example 1, all coordinates strictly positive: signs are 1.
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    x, y = (2, 1, 1), (1, 2, 1)
    def operator(z):
        assert min(z) > 0
        return tuple(1 + sum(a * b for a, b in zip(row, z))
                     for row in matrix)
    fx, fy = operator(x), operator(y)
    inner = (fx[0] - fy[0]) * (x[0] - y[0])
    assert fx == (8, 20, 32) and fy == (9, 21, 33)
    assert inner == -1

    # C197: exact legal GPPA steps for k=0,...,8. No inference from sampling.
    orbit = []
    for k in range(9):
        current = (Q(1, 2**k), Q((-1)**k))
        nxt = (Q(1, 2**(k+1)), Q((-1)**(k+1)))
        assert current[0] - nxt[0] == nxt[0]
        assert abs(nxt[1] - current[1]) == 2
        energy_gap = (current[0]**2 - nxt[0]**2
                      - (nxt[0] - current[0])**2 - 2*nxt[0]**2)
        assert energy_gap == 0
        assert nxt[0]**2 <= current[0]**2 / 3
        orbit.append({"k": k, "current": [str(z) for z in current],
                      "next": [str(z) for z in nxt],
                      "distance_to_S": str(current[0]),
                      "physical_vertical_step": "2",
                      "theorem_2_energy_gap": str(energy_gap)})

    # C198: rational points with rational square-root outputs.
    samples = ((Q(0), Q(0)), (Q(1, 100), Q(1, 10)),
               (Q(1, 4), Q(1, 2)), (Q(1), Q(1)))
    tested_pairs = 0
    for a, ca in samples:
        assert ca**2 == a
        for b, cb in samples:
            assert (ca-cb)**2 <= abs(a-b)
            tested_pairs += 1
    input_distance, output_distance = Q(1, 100), Q(1, 10)
    assert output_distance > input_distance
    assert output_distance**2 == input_distance

    return {
        "cutoff_utc": cutoff.isoformat(),
        "python": platform.python_version(),
        "arithmetic": "integers and fractions.Fraction; exact; no seed or tolerance",
        "claims": ["C197-v1", "C198-v1"],
        "evidence_scope": "finite consistency checks, not general proofs",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "days_before_cutoff": days,
        "gppa_example_1": {"x": x, "y": y, "F_x": fx, "F_y": fy,
                           "pair_monotonicity_inner_product": inner},
        "gppa_projection_orbit": orbit,
        "holder_reference": {"tested_pairs": tested_pairs,
                             "input_distance": str(input_distance),
                             "output_distance": str(output_distance),
                             "kirszbraun_k1_condition_satisfied": False},
        "all_finite_checks_passed": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = check()
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"Finite checks passed; evidence saved to {args.output}")
    else:
        print(rendered, end="")
