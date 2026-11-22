#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p build
# Some minimal TeX Live installations contain the sources but no search
# database or precompiled format. Rebuild only those local generated files.
if ! kpsewhich pdflatex.fmt >/dev/null 2>&1; then
  export TEXMF="{$PWD/build/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
  export TEXMFVAR="$PWD/build/var"
  export TEXMFCONFIG="$PWD/build/config"
  export TEXFORMATS="$PWD/build/formats:"
  export TEXFONTMAPS="$PWD/build/texmf/fonts/map//:"
  mkdir -p build/formats build/var build/config build/texmf/fonts/map
  if [[ ! -f build/formats/pdflatex.fmt ]]; then
    pdftex -ini -etex -progname=pdflatex -jobname=pdflatex \
      -interaction=nonstopmode -halt-on-error \
      -output-directory=build/formats pdflatex.ini >build/format.stdout 2>&1
  fi
  python3 - <<'PY'
from pathlib import Path
base = Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts')
maps = [base / (name + '.map') for name in
        ('cm', 'cmextra', 'latxfont', 'symbols', 'euler')]
maps.append(Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map'))
Path('build/texmf/fonts/map/pdftex.map').write_text(
    '\n'.join(path.read_text() for path in maps if path.exists()))
PY
fi
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=build main.tex
cp build/main.pdf DD_draft.pdf
