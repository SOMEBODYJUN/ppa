# Isolated LaTeX environment

This directory repairs the available Debian TeX Live 2023 installation without
writing to system directories or the manuscript source tree. It needs the
existing `xetex`, `pdftex`, `luatex`, `bibtex`, `python3`, `curl`, and `rg` binaries,
and the installed `/usr/share/texmf` and `/usr/share/texlive/texmf-dist` trees.

## Rebuild and compile

```bash
bash tex-support/bootstrap.sh
bash tex-support/compile.sh path/to/main.tex tex-support/build/manuscript
bash tex-support/compile.sh tex-support/tests/chinese.tex tex-support/build/chinese xelatex
bash tex-support/compile.sh tex-support/tests/english.tex tex-support/build/english pdflatex
```

`compile.sh` runs LaTeX, BibTeX when the auxiliary file declares a bibliography,
and two further LaTeX passes, with one additional pass when labels request it.
It exits on compilation errors. Logs, PDFs, auxiliary files, font caches, and
formats stay under the chosen output directory or `tex-support`.
The default output directory is `tex-support/build/<source basename>`.
Use `source tex-support/env.sh` for manual TeX commands.

## Locked dependencies

`dependencies.json` records upstream URLs, versions, commit, and SHA-256 hashes.
The archives in `downloads/` allow an offline rebuild on this existing system.
If missing, bootstrap downloads and checks them; a changed archive fails rather
than being accepted silently. CTeX uses official tag `ctex-v2.5.10`, commit
`13a22565bdd14d750b604c2f1ed0fa1938cb6cd4`, including xeCJK 3.9.0 and zhnumber 3.0.
Fandol is version 0.3 from CTAN. The generated package metadata identifies this
exact archive snapshot through the upstream `ctxdocstrip` mechanism.

The environment is reproducible relative to the installed TeX Live 2023 trees;
it does not bundle or replace the system engines. PDF metadata uses UTC and a
fixed default `SOURCE_DATE_EPOCH` (2026-10-11 00:00:00 UTC), which may be overridden.

## Validation

Chinese `ctexart` and English `article` minimal documents compile successfully
to one-page A4 PDFs; their rendered previews confirm readable Chinese, English,
mathematics, font variants, theorem/proof environments, and cross-references.
The original submission `main.tex` compiles to a 19-page A4 PDF with BibTeX.
Its unresolved internal labels and font/style warnings belong to that source;
they are recorded separately in `validation.json`.
