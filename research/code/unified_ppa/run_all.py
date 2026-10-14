#!/usr/bin/env python3
"""Run this batch's five finite verifiers; analytic proofs remain authoritative."""
import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NAMES = ["joint_verify.py", "raw_verify.py", "coverage_verify.py",
         "curved_verify.py", "inexact_verify.py"]
runs = []
for name in NAMES:
    path = HERE / name
    result = subprocess.run([sys.executable, str(path)], cwd=ROOT,
                            capture_output=True, text=True, timeout=60)
    runs.append({"script": str(path.relative_to(ROOT)),
                 "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                 "command": "python3 " + str(path.relative_to(ROOT)),
                 "returncode": result.returncode,
                 "stdout": result.stdout, "stderr": result.stderr})
    print(f"{name}: {'PASS' if result.returncode == 0 else 'FAIL'}")
record = {"python": platform.python_version(), "platform": platform.platform(),
          "dependencies": {"raw_verify.py": {"numpy": importlib.metadata.version("numpy")}, "others": "standard library"},
          "scope": "Finite arithmetic, boundary and back-substitution checks. Universal claims are proved analytically in canonical text.",
          "runs": runs}
(HERE / "all_verifiers_output.json").write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n")
sys.exit(0 if all(r["returncode"] == 0 for r in runs) else 1)
