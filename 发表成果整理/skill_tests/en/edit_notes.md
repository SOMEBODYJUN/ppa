# English edit notes

Mode: lightweight English editing with LaTeX preservation; Class D (surface changes). Authority: `input.tex`; no outside manuscript or test material was inspected.

Loaded and used:

- `/workspace/scratch/15cd717a5884/ppa/.agents/skills/academic-writing-skills/SKILL.md`
- Its `references/mathematics.md`, `prose-and-citation-editing.md`, `universal-integrity.md`, `execution-and-acceptance.md`, `lifecycle-and-routing.md`, and `reviewer-red-team-and-release.md`.
- `/root/.codex/skills/builtins/pdf/SKILL.md` for intended rendering verification.
- The academic skill's `scripts/audit_prose_patterns.py` (inspected and imported for its `audit_text` diagnostic).

Edits: replaced the verbose opening with “This section discusses convergence under the stated assumptions” and shortened “provided that” to “provided.” All other prose was retained. Scientific claims, qualifications, notation, and commands were preserved.

Exact-candidate checks:

- Source comparison: all six inline mathematical spans and all 12 LaTeX command tokens are identical and in the same order; preamble and environment sequence are unchanged.
- Meaning check, lines 5–7: retained the true residual for each actual proximal output, the error bound, reflected-resolvent exponent, strict condition `$q\gamma>1$`, certified-neighborhood condition, strict length budget, and the finite-length/convergence conclusion for the allowed orbit. No full-fiber, global, uniqueness, or stronger rate claim was added.
- Reader walkthrough, lines 4–7: the opening names the topic; the residual precedes the error bound that uses it; the localization condition is followed by its length-budget safeguard and the bounded convergence conclusion. Simulated an ordinary spoken reading. Necessary technical terms were retained rather than replaced with synonyms.
- Exact prose diagnostic: `audit_text` returned no findings using protected terms from the supplied excerpt. Mathematical spans were excluded from the prose scan. Manual review found no redundant stock framing, unstable terminology, or unsupported transition in the candidate.
- Structural/identity check: no author, citation, label, comment, reply, or identity-bearing metadata commands were added. No captions or venue formatting are involved.
- Compilation attempted with `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error`; unavailable because the installed engine lacks `pdflatex.fmt`. No PDF was generated, so saved-layout inspection remains unavailable.

Functional-completeness retrospective: the requested local language edit is covered; scientific meaning and source structure are preserved. No semantic change requires propagation. Scientific proof verification, absent surrounding manuscript context, and whole-paper or venue readiness are outside scope; there are no citations to reconcile. Rendering is the remaining unavailable check.

Checked candidate SHA-256: `1867d889b441eddf61ff536f786f998df2b730f0129e0aee28a4a1f1547840f9`.
