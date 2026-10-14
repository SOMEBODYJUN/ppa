#!/usr/bin/env python3
"""Re-run independent finite verifiers and preserve actual outputs/versions."""
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys

def main():
    folder=Path(__file__).resolve().parent
    root=folder.parents[2]
    names=["primal_verify.py","inverse_verify.py","semimonotone_verify.py",
           "gauge_verify.py","order_verify.py","route_bridge_verify.py"]
    records=[]
    for name in names:
        path=folder/name
        run=subprocess.run([sys.executable,str(path)],cwd=root,text=True,capture_output=True)
        records.append({"script":str(path.relative_to(root)),
                        "sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                        "returncode":run.returncode,"stdout":run.stdout,"stderr":run.stderr})
        if run.returncode:
            print(run.stdout,run.stderr)
            raise SystemExit(run.returncode)
    payload={"scope":"finite back-substitution only; analytic reports prove quantifiers",
             "python":platform.python_version(),"commands":[
             "python3 "+r["script"] for r in records],"runs":records,
             "runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (folder/"all_verifiers_output.json").write_text(
        json.dumps(payload,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"passed","verifiers":len(records),
                     "output":"research/code/submonotonicity_routes/all_verifiers_output.json"}))
if __name__=="__main__":
    main()
